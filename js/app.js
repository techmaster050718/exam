/**
 * js/app.js
 * Shared helpers: storage, scoring, paper loading, theme, utilities.
 * Uses a simple IIFE module pattern exposed on window.App.
 */
(function () {
  'use strict';

  /* ── Storage Key ────────────────────────────────────────── */
  const STORAGE_KEY = 'ibps_mocktest_v1';
  const THEME_KEY   = 'ibps_mocktest_theme';

  /* ── Storage Helpers ────────────────────────────────────── */
  function loadStore() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  }

  function saveStore(store) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
    } catch (e) {
      console.warn('localStorage write failed:', e);
    }
  }

  function getPaperState(paperId) {
    const store = loadStore();
    return store[paperId] || null;
  }

  function savePaperState(paperId, state) {
    const store = loadStore();
    store[paperId] = state;
    saveStore(store);
  }

  function clearPaperState(paperId) {
    const store = loadStore();
    delete store[paperId];
    saveStore(store);
  }

  function resetAll() {
    localStorage.removeItem(STORAGE_KEY);
    localStorage.removeItem(THEME_KEY);
  }

  /* ── Paper Loader ───────────────────────────────────────── */
  async function loadPapersList() {
    return await fetchJSON('data/papers.json');
  }

  async function loadSubjects() { return await fetchJSON('data/subjects.json'); }
  async function loadSite() { return await fetchJSON('data/site.json'); }

  async function applyBranding() {
    const site = await loadSite();
    document.querySelectorAll('[data-site-name]').forEach((el) => { el.textContent = site.name; });
    document.querySelectorAll('[data-site-tagline]').forEach((el) => { el.textContent = site.tagline; });
    document.querySelectorAll('[data-site-footer]').forEach((el) => { el.textContent = site.footer; });
    const prefix = document.body.dataset.pageTitle;
    document.title = prefix ? `${prefix} – ${site.name}` : site.name;
    return site;
  }

  function normaliseSubjects(subjects, papers) {
    const listed = Array.isArray(subjects) ? subjects : [];
    const ids = new Set(listed.map((s) => s.id));
    if (papers.some((p) => !p.subject || !ids.has(p.subject))) {
      listed.push({ id: 'general', title: 'General', description: 'General practice papers', icon: '📚' });
    }
    return listed;
  }

  function subjectIdFor(paper, subjects) {
    return paper.subject && subjects.some((s) => s.id === paper.subject) ? paper.subject : 'general';
  }

  async function loadPaper(filePath) {
    return await fetchJSON(filePath);
  }

  async function fetchJSON(url) {
    let response;
    try {
      response = await fetch(url);
    } catch (err) {
      throw new FetchError(
        `Could not load "${url}".\n\nThis site uses fetch() which requires a local server on file:// URLs.\n\nPlease open this project with VS Code Live Server or run:\n  python -m http.server\nthen visit http://localhost:8000`,
        err
      );
    }
    if (!response.ok) {
      throw new FetchError(`HTTP ${response.status} loading "${url}"`, null);
    }
    return response.json();
  }

  class FetchError extends Error {
    constructor(msg, cause) {
      super(msg);
      this.name = 'FetchError';
      this.cause = cause;
    }
  }

  /* ── Question Flattening ────────────────────────────────── */
  /**
   * Returns flat array of question objects each with extra fields:
   * { sectionName, sectionIndex, localIndex, globalIndex, q, options, answer }
   */
  function flattenQuestions(paperData) {
    const flat = [];
    let globalIdx = 0;
    paperData.sections.forEach((section, sectionIndex) => {
      section.questions.forEach((q, localIndex) => {
        flat.push({
          ...q,
          sectionName: section.name,
          sectionIndex,
          localIndex,
          globalIndex: globalIdx++,
        });
      });
    });
    return flat;
  }

  /* ── Scoring ────────────────────────────────────────────── */
  function computeScore(questions, answers, paperMeta) {
    const correctMark  = paperMeta.correctMark  ?? 1;
    const negativeMark = paperMeta.negativeMark ?? 0.25;
    const totalMark    = questions.length * correctMark;

    let correct = 0, wrong = 0, unattempted = 0;

    questions.forEach((q) => {
      // After JSON round-trip, object keys become strings — check both
      const chosen = answers[q.globalIndex] ?? answers[String(q.globalIndex)];
      if (chosen === undefined || chosen === null) {
        unattempted++;
      } else if (Number(chosen) === q.answer) {
        correct++;
      } else {
        wrong++;
      }
    });

    const rawScore    = correct * correctMark - wrong * negativeMark;
    const score       = Math.round(rawScore * 100) / 100;
    const percentage  = totalMark > 0 ? Math.round((score / totalMark) * 10000) / 100 : 0;
    const penalty     = Math.round(wrong * negativeMark * 100) / 100;
    const attempted   = correct + wrong;
    const accuracy    = attempted > 0 ? Math.round((correct / attempted) * 10000) / 100 : 0;

    return { score, totalMark, percentage, correct, wrong, unattempted, penalty, accuracy, attempted };
  }

  function computeSectionStats(questions, answers, paperMeta) {
    const correctMark  = paperMeta.correctMark  ?? 1;
    const negativeMark = paperMeta.negativeMark ?? 0.25;
    const sections = {};

    questions.forEach((q) => {
      const name = q.sectionName;
      if (!sections[name]) {
        sections[name] = { name, total: 0, correct: 0, wrong: 0, unattempted: 0, marks: 0 };
      }
      const s = sections[name];
      s.total++;
      // After JSON round-trip, object keys become strings
      const chosen = answers[q.globalIndex] ?? answers[String(q.globalIndex)];
      if (chosen === undefined || chosen === null) {
        s.unattempted++;
      } else if (Number(chosen) === q.answer) {
        s.correct++;
        s.marks += correctMark;
      } else {
        s.wrong++;
        s.marks -= negativeMark;
      }
    });

    return Object.values(sections).map((s) => ({
      ...s,
      marks:      Math.round(s.marks * 100) / 100,
      totalMarks: s.total * correctMark,
      attempted:  s.correct + s.wrong,
      percentage: s.total > 0
        ? Math.round((Math.max(s.marks, 0) / (s.total * correctMark)) * 10000) / 100
        : 0,
    }));
  }

  /* ── Time Helpers ───────────────────────────────────────── */
  function formatTime(totalSeconds) {
    const s = Math.max(0, Math.round(totalSeconds));
    const h = Math.floor(s / 3600);
    const m = Math.floor((s % 3600) / 60);
    const sec = s % 60;
    if (h > 0) return `${pad(h)}:${pad(m)}:${pad(sec)}`;
    return `${pad(m)}:${pad(sec)}`;
  }

  function pad(n) { return String(n).padStart(2, '0'); }

  function formatDuration(totalSeconds) {
    const s = Math.max(0, Math.round(totalSeconds));
    const h = Math.floor(s / 3600);
    const m = Math.floor((s % 3600) / 60);
    const sec = s % 60;
    const parts = [];
    if (h) parts.push(`${h}h`);
    if (m) parts.push(`${m}m`);
    if (sec || !parts.length) parts.push(`${sec}s`);
    return parts.join(' ');
  }

  function formatDate(isoString) {
    if (!isoString) return '—';
    const d = new Date(isoString);
    return d.toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' }) +
      ' ' + d.toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' });
  }

  /* ── Text Sanitisation & Rendering ─────────────────────── */
  /**
   * Safely renders question text. Escapes HTML, then converts:
   *   ^x or ^10 or ^(expr)  ->  <sup>...</sup>
   */
  function renderText(raw) {
    if (!raw) return '';
    // Escape HTML special characters
    const escaped = String(raw)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
    // Convert superscripts: ^(expression) or ^alphanumeric
    return escaped
      .replace(/\^\(([^)]+)\)/g, '<sup>$1</sup>')
      .replace(/\^([A-Za-z0-9]+)/g, '<sup>$1</sup>');
  }

  /* ── DOM Helpers ────────────────────────────────────────── */
  function qs(selector, parent = document) { return parent.querySelector(selector); }
  function qsa(selector, parent = document) { return [...parent.querySelectorAll(selector)]; }

  function el(tag, attrs = {}, ...children) {
    const elem = document.createElement(tag);
    Object.entries(attrs).forEach(([k, v]) => {
      if (k === 'className') elem.className = v;
      else if (k === 'dataset') Object.assign(elem.dataset, v);
      else if (k === 'style') Object.assign(elem.style, v);
      else if (k.startsWith('on')) elem.addEventListener(k.slice(2).toLowerCase(), v);
      else elem.setAttribute(k, v);
    });
    children.forEach((c) => {
      if (c === null || c === undefined) return;
      if (typeof c === 'string' || typeof c === 'number') {
        elem.appendChild(document.createTextNode(String(c)));
      } else {
        elem.appendChild(c);
      }
    });
    return elem;
  }

  function showError(container, title, message, extra = '') {
    container.innerHTML = `
      <div class="error-screen">
        <div class="error-icon">⚠️</div>
        <div class="error-title">${title}</div>
        <div class="error-message">${message}</div>
        ${extra ? `<pre class="error-code">${extra}</pre>` : ''}
        <a href="index.html" class="btn btn-primary">← Back to Home</a>
      </div>`;
  }

  function showLoading(container, message = 'Loading…') {
    container.innerHTML = `
      <div class="loading-screen">
        <div class="spinner" role="status" aria-label="Loading"></div>
        <div class="loading-text">${message}</div>
      </div>`;
  }

  /* ── Toast ──────────────────────────────────────────────── */
  let toastContainer = null;
  function ensureToastContainer() {
    if (!toastContainer) {
      toastContainer = el('div', { className: 'toast-container', 'aria-live': 'polite' });
      document.body.appendChild(toastContainer);
    }
  }

  function showToast(message, type = '', duration = 2800) {
    ensureToastContainer();
    const t = el('div', { className: `toast ${type ? 'toast-' + type : ''}` });
    t.textContent = message;
    toastContainer.appendChild(t);
    setTimeout(() => {
      t.classList.add('toast-out');
      t.addEventListener('animationend', () => t.remove(), { once: true });
    }, duration);
  }

  /* ── Theme ──────────────────────────────────────────────── */
  function initTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const theme = saved || (prefersDark ? 'dark' : 'light');
    document.documentElement.dataset.theme = theme;
    return theme;
  }

  function toggleTheme() {
    const current = document.documentElement.dataset.theme;
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    localStorage.setItem(THEME_KEY, next);
    return next;
  }

  function getTheme() { return document.documentElement.dataset.theme || 'light'; }

  /* ── URL Helpers ────────────────────────────────────────── */
  function getParam(name) {
    return new URLSearchParams(window.location.search).get(name);
  }

  /* ── Progress Calculations ──────────────────────────────── */
  function getOverallProgress(papersList) {
    const store = loadStore();
    let completed = 0, totalPct = 0, bestPaper = null, bestPct = -Infinity;

    papersList.forEach((p) => {
      const state = store[p.id];
      if (state && state.status === 'submitted') {
        completed++;
        totalPct += state.percentage || 0;
        if ((state.percentage || 0) > bestPct) {
          bestPct = state.percentage || 0;
          bestPaper = { title: p.title, pct: state.percentage };
        }
      }
    });

    const avg = completed > 0 ? Math.round((totalPct / completed) * 10) / 10 : 0;
    return { completed, total: papersList.length, avg, bestPaper };
  }

  /* ── Expose ─────────────────────────────────────────────── */
  window.App = {
    // Storage
    loadStore, saveStore, getPaperState, savePaperState, clearPaperState,
    resetAll,
    // Data
    loadPapersList, loadPaper, loadSubjects, loadSite, applyBranding, normaliseSubjects, subjectIdFor, flattenQuestions,
    // Scoring
    computeScore, computeSectionStats,
    // Time
    formatTime, formatDuration, formatDate, pad,
    // Text
    renderText,
    // DOM
    qs, qsa, el, showError, showLoading,
    // Toast
    showToast,
    // Theme
    initTheme, toggleTheme, getTheme,
    // URL
    getParam,
    // Progress
    getOverallProgress,
    // Errors
    FetchError,
  };
})();
