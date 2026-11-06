/**
 * js/test.js
 * Exam screen logic: timer, question navigation, palette,
 * keyboard shortcuts, auto-save, submit.
 */
(function () {
  'use strict';

  const { App } = window;

  /* ── State ──────────────────────────────────────────────── */
  let paperMeta    = null;
  let paperData    = null;
  let questions    = [];   // flat array
  let state        = null; // from localStorage
  let timerID      = null;
  let currentIdx   = 0;
  let isSubmitted  = false;

  /* ── Boot ───────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', async () => {
    App.initTheme();
    App.applyBranding().catch(() => {});
    bindClick('#theme-toggle', () => {
      const t = App.toggleTheme();
      const themeToggle = App.qs('#theme-toggle');
      if (themeToggle) themeToggle.textContent = t === 'dark' ? '☀️' : '🌙';
    });
    const themeToggle = App.qs('#theme-toggle');
    if (themeToggle) themeToggle.textContent = App.getTheme() === 'dark' ? '☀️' : '🌙';

    const paperId = App.getParam('paper');
    if (!paperId) { window.location.href = 'index.html'; return; }

    const mainEl = App.qs('#test-main');
    // Keep the pre-rendered exam controls in the DOM; replacing this container
    // with a loading screen would remove every element buildUI needs to wire up.
    App.qs('#q-text').textContent = 'Loading exam…';

    try {
      const papers = await App.loadPapersList();
      paperMeta = papers.find((p) => p.id === paperId);
      if (!paperMeta) throw new Error(`Paper "${paperId}" not found in papers.json`);

      paperData = await App.loadPaper(paperMeta.file);
      questions = App.flattenQuestions(paperData);

      state = App.getPaperState(paperId);

      // If not yet started, initialize fresh state for this paper
      if (!state) {
        state = {
          status: 'in_progress',
          answers: {},
          marked: [],
          visited: [],
          currentQuestion: 0,
          startedAt: new Date().toISOString(),
          totalQuestions: questions.length,
          attempts: [],
        };
        App.savePaperState(paperId, state);
      }

      // If already submitted, redirect to result
      if (state.status === 'submitted') {
        window.location.href = `result.html?paper=${paperId}`;
        return;
      }

      isSubmitted = false;
      currentIdx = state.currentQuestion || 0;

      // Ensure required state arrays exist (for older/migrated states)
      if (!state.visited) state.visited = [];
      if (!state.marked)  state.marked  = [];
      if (!state.answers) state.answers = {};
      if (!state.attempts) state.attempts = [];

      // Update total questions in state (in case it changed)
      state.totalQuestions = questions.length;
      App.savePaperState(paperId, state);

      buildUI();
      startTimer();
      renderQuestion(currentIdx);
      renderPalette();
      updateCounters();

      // Keyboard shortcuts
      document.addEventListener('keydown', handleKeyDown);

      // Warn before unload
      window.addEventListener('beforeunload', (e) => {
        if (!isSubmitted) {
          e.preventDefault();
          e.returnValue = 'Your test is in progress. Are you sure you want to leave?';
        }
      });

    } catch (err) {
      App.showError(mainEl, 'Failed to load paper', err.message.replace(/\n/g, '<br>'), err.stack || '');
    }
  });

  /* ── UI Builder ─────────────────────────────────────────── */
  function bindClick(selector, handler) {
    const element = App.qs(selector);
    if (!element) {
      console.warn(`test.js: missing UI element ${selector}`);
      return;
    }
    element.addEventListener('click', handler);
  }

  function buildUI() {
    // Set title
    App.qs('#test-title').textContent = paperMeta.title;

    // Section tabs
    const tabsEl = App.qs('#section-tabs');
    tabsEl.innerHTML = '';
    paperData.sections.forEach((sec, si) => {
      const btn = App.el('button', { className: 'section-tab', dataset: { sectionIndex: si } }, sec.name);
      btn.addEventListener('click', () => jumpToSection(si));
      tabsEl.appendChild(btn);
    });

    // Palette toggle (mobile)
    bindClick('#palette-toggle-btn', openPalette);
    bindClick('#palette-overlay', closePalette);
    bindClick('#palette-close-btn', closePalette);

    // Prev / Next / Clear / Mark buttons (desktop)
    bindClick('#btn-prev', () => navigate(-1));
    bindClick('#btn-next', () => navigate(1));
    bindClick('#btn-clear', clearSelection);
    bindClick('#btn-mark', toggleMark);

    // Sticky bottom nav (mobile)
    bindClick('#btn-prev-sticky', () => navigate(-1));
    bindClick('#btn-next-sticky', () => navigate(1));
    bindClick('#btn-mark-sticky', toggleMark);
    bindClick('#btn-palette-open', openPalette);

    // Submit buttons
    bindClick('#btn-submit', openSubmitModal);
    bindClick('#btn-submit-sticky', openSubmitModal);
    bindClick('#btn-submit-sidebar', openSubmitModal);
    bindClick('#modal-cancel', closeSubmitModal);
    bindClick('#modal-confirm', confirmSubmit);

    // Click backdrop to close modal
    const submitModal = App.qs('#submit-modal');
    if (submitModal) {
      submitModal.addEventListener('click', (e) => {
        if (e.target === submitModal) closeSubmitModal();
      });
    } else {
      console.warn('test.js: missing UI element #submit-modal');
    }
  }

  /* ── Timer ──────────────────────────────────────────────── */
  function startTimer() {
    const durationSec = (paperMeta.durationMin || 60) * 60;
    const initialRemaining = getRemainingSeconds(durationSec);
    if (initialRemaining <= 0) {
      updateTimerDisplay(0);
      autoSubmit();
      return;
    }
    updateTimerDisplay(initialRemaining);

    timerID = setInterval(() => {
      const remaining = getRemainingSeconds(durationSec);
      updateTimerDisplay(remaining);
      if (remaining <= 0) {
        clearInterval(timerID);
        autoSubmit();
      }
    }, 500);
  }

  function getRemainingSeconds(durationSec) {
    const startedAt = new Date(state.startedAt).getTime();
    const elapsed   = Math.floor((Date.now() - startedAt) / 1000);
    return Math.max(0, durationSec - elapsed);
  }

  function updateTimerDisplay(remaining) {
    const el   = App.qs('#timer');
    const text = App.formatTime(remaining);
    el.textContent = '⏱ ' + text;
    el.setAttribute('aria-label', 'Time remaining: ' + text);

    el.classList.remove('warning', 'danger');
    if (remaining <= 60)   el.classList.add('danger');
    else if (remaining <= 300) el.classList.add('warning');
  }

  /* ── Render Question ────────────────────────────────────── */
  function renderQuestion(idx) {
    if (idx < 0 || idx >= questions.length) return;
    currentIdx = idx;

    const q = questions[idx];

    // Update question number label
    App.qs('#q-num').textContent = `Question ${idx + 1} of ${questions.length}`;

    // Section context
    App.qs('#q-section').textContent = q.sectionName;

    // Question text (safe render)
    App.qs('#q-text').innerHTML = App.renderText(q.q);
    const questionImage = App.qs('#q-image');
    if (q.img) {
      questionImage.src = q.img;
      questionImage.alt = q.imgAlt || `Illustration for question ${idx + 1}`;
      questionImage.hidden = false;
    } else {
      questionImage.hidden = true;
      questionImage.removeAttribute('src');
    }

    // Options
    const optList = App.qs('#options-list');
    optList.innerHTML = '';
    const keys = ['A', 'B', 'C', 'D'];
    // Coerce stored answer to number (keys are strings after JSON parse)
    const rawSelected  = state.answers[idx];
    const selectedOpt  = (rawSelected !== undefined && rawSelected !== null) ? Number(rawSelected) : null;

    q.options.forEach((optText, oi) => {
      const isSelected = selectedOpt === oi;
      const li = App.el('li', {
        className: `option-item${isSelected ? ' selected' : ''}`,
        role: 'radio',
        'aria-checked': isSelected ? 'true' : 'false',
        tabindex: '0',
        dataset: { optIndex: oi }
      },
        App.el('span', { className: 'option-key' }, keys[oi]),
        App.el('span', { className: 'option-text' })
      );
      // Safe set text
      li.querySelector('.option-text').innerHTML = App.renderText(optText);
      if (Array.isArray(q.optionImgs) && q.optionImgs[oi]) {
        const image = App.el('img', { className: 'option-image', src: q.optionImgs[oi], alt: `Option ${keys[oi]}` });
        li.querySelector('.option-text').appendChild(image);
      }

      li.addEventListener('click', () => selectOption(oi));
      li.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selectOption(oi); }
      });
      optList.appendChild(li);
    });

    // Mark button state
    const isMarked = (state.marked || []).includes(idx);
    App.qs('#btn-mark').classList.toggle('active', isMarked);
    App.qs('#btn-mark-sticky').classList.toggle('active', isMarked);
    App.qs('#btn-mark').textContent = isMarked ? '🔵 Marked' : '🔵 Mark';

    // Prev/Next disabled states
    App.qs('#btn-prev').disabled = idx === 0;
    App.qs('#btn-next').disabled = idx === questions.length - 1;
    App.qs('#btn-prev-sticky').disabled = idx === 0;
    App.qs('#btn-next-sticky').disabled = idx === questions.length - 1;

    // Active section tab
    App.qsa('.section-tab').forEach((t) => {
      t.classList.toggle('active', Number(t.dataset.sectionIndex) === q.sectionIndex);
    });

    // Mark as "visited" (not-answered state if not answered)
    // We use the fact that a qn in answers[] means answered.
    // We just need to track visited — but our palette states handle it implicitly.

    // Save current question index
    state.currentQuestion = idx;
    saveState();

    // Highlight palette button
    App.qsa('.palette-btn').forEach((b) => {
      b.classList.toggle('current', Number(b.dataset.qIdx) === idx);
    });
    // Scroll palette to current
    const curBtn = App.qs(`.palette-btn[data-q-idx="${idx}"]`);
    if (curBtn) curBtn.scrollIntoView({ block: 'nearest' });
  }

  /* ── Option Selection ───────────────────────────────────── */
  function selectOption(optIdx) {
    if (isSubmitted) return;
    const rawPrev = state.answers[currentIdx] ?? state.answers[String(currentIdx)];
    const prev = (rawPrev !== undefined && rawPrev !== null) ? Number(rawPrev) : null;

    if (prev === optIdx) {
      // Deselect (unattempt)
      delete state.answers[currentIdx];
      delete state.answers[String(currentIdx)];
    } else {
      state.answers[currentIdx] = optIdx;
    }

    saveState();
    renderQuestion(currentIdx);
    updatePaletteBtn(currentIdx);
    updateCounters();
  }

  function clearSelection() {
    if (isSubmitted) return;
    delete state.answers[currentIdx];
    delete state.answers[String(currentIdx)];
    saveState();
    renderQuestion(currentIdx);
    updatePaletteBtn(currentIdx);
    updateCounters();
  }

  /* ── Marking ────────────────────────────────────────────── */
  function toggleMark() {
    if (isSubmitted) return;
    const marked = state.marked || [];
    const pos = marked.indexOf(currentIdx);
    if (pos === -1) {
      marked.push(currentIdx);
    } else {
      marked.splice(pos, 1);
    }
    state.marked = marked;
    saveState();
    renderQuestion(currentIdx);
    updatePaletteBtn(currentIdx);
    updateCounters();
  }

  /* ── Navigation ─────────────────────────────────────────── */
  function navigate(delta) {
    const next = currentIdx + delta;
    if (next >= 0 && next < questions.length) {
      renderQuestion(next);
    }
  }

  function jumpToSection(sectionIndex) {
    const q = questions.find((q) => q.sectionIndex === sectionIndex);
    if (q) { renderQuestion(q.globalIndex); closePalette(); }
  }

  function jumpToQuestion(idx) {
    renderQuestion(idx);
    closePalette();
  }

  /* ── Palette ────────────────────────────────────────────── */
  function renderPalette() {
    const grid = App.qs('#palette-grid');
    grid.innerHTML = '';
    questions.forEach((q, idx) => {
      const btn = App.el('button', {
        className: `palette-btn ${getPaletteState(idx)}`,
        dataset: { qIdx: idx },
        'aria-label': `Question ${idx + 1}`,
        tabindex: '-1',
      }, String(idx + 1));
      btn.addEventListener('click', () => jumpToQuestion(idx));
      if (idx === currentIdx) btn.classList.add('current');
      grid.appendChild(btn);
    });
  }

  function updatePaletteBtn(idx) {
    const btn = App.qs(`.palette-btn[data-q-idx="${idx}"]`);
    if (!btn) return;
    btn.className = `palette-btn ${getPaletteState(idx)}`;
    if (idx === currentIdx) btn.classList.add('current');
  }

  function getPaletteState(idx) {
    const answered = state.answers[idx] !== undefined;
    const marked   = (state.marked || []).includes(idx);
    // We track "visited" via currentQuestion history — simplify:
    // Any question the user has been to but not answered = not-answered (red)
    // Not-visited = never navigated to
    // We use a visited set stored in state
    const visited  = (state.visited || []).includes(idx);

    if (marked && answered) return 'state-marked-answered';
    if (marked)             return 'state-marked';
    if (answered)           return 'state-answered';
    if (visited)            return 'state-not-answered';
    return 'state-not-visited';
  }

  /* ── Counters ───────────────────────────────────────────── */
  function updateCounters() {
    const answered    = Object.values(state.answers || {}).filter(v => v !== undefined && v !== null && v !== '').length;
    const unanswered  = questions.length - answered;
    const marked      = (state.marked || []).length;

    App.qs('#counter-answered').textContent    = `✓ ${answered}`;
    App.qs('#counter-unanswered').textContent  = `✗ ${unanswered}`;
    App.qs('#counter-marked').textContent      = `◉ ${marked}`;
  }

  /* ── State Persistence ──────────────────────────────────── */
  function saveState() {
    // Track visited questions
    const visited = new Set(state.visited || []);
    visited.add(currentIdx);
    state.visited = [...visited];
    App.savePaperState(paperMeta.id, state);
  }

  /* ── Submit Flow ────────────────────────────────────────── */
  function openSubmitModal() {
    const answered   = Object.values(state.answers || {}).filter(v => v !== undefined && v !== null && v !== '').length;
    const unanswered = questions.length - answered;
    const marked     = (state.marked || []).length;

    App.qs('#modal-stat-answered').textContent   = answered;
    App.qs('#modal-stat-unanswered').textContent = unanswered;
    App.qs('#modal-stat-marked').textContent     = marked;

    App.qs('#submit-modal').classList.add('show');
    App.qs('#modal-confirm').focus();
  }

  function closeSubmitModal() {
    App.qs('#submit-modal').classList.remove('show');
  }

  function autoSubmit() {
    App.showToast('⏰ Time is up! Submitting your paper…', 'error', 3000);
    setTimeout(submitPaper, 1200);
  }

  function confirmSubmit() {
    closeSubmitModal();
    submitPaper();
  }

  function submitPaper() {
    if (isSubmitted) return;
    isSubmitted = true;
    clearInterval(timerID);

    // Calculate time taken
    const startedAt    = new Date(state.startedAt).getTime();
    const timeTakenSec = Math.round((Date.now() - startedAt) / 1000);

    // Score
    const scoreResult  = App.computeScore(questions, state.answers, paperMeta);
    const sectionStats = App.computeSectionStats(questions, state.answers, paperMeta);

    // Build history entry
    const histEntry = {
      date:       new Date().toISOString(),
      score:      scoreResult.score,
      totalMark:  scoreResult.totalMark,
      percentage: scoreResult.percentage,
      timeTakenSec,
    };

    const attempts = [...(state.attempts || []), histEntry];

    // Save final state
    const finalState = {
      ...state,
      status:      'submitted',
      submittedAt: new Date().toISOString(),
      timeTakenSec,
      score:       scoreResult.score,
      totalMark:   scoreResult.totalMark,
      percentage:  scoreResult.percentage,
      correct:     scoreResult.correct,
      wrong:       scoreResult.wrong,
      unattempted: scoreResult.unattempted,
      penalty:     scoreResult.penalty,
      accuracy:    scoreResult.accuracy,
      sectionStats,
      attempts,
    };

    App.savePaperState(paperMeta.id, finalState);
    App.showToast('✅ Paper submitted! Redirecting…', 'success');
    setTimeout(() => {
      window.location.href = `result.html?paper=${paperMeta.id}`;
    }, 1000);
  }

  /* ── Keyboard Shortcuts ─────────────────────────────────── */
  function handleKeyDown(e) {
    if (isSubmitted) return;
    // Don't fire if inside an input/textarea
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;

    const keyMap = { '1': 0, 'a': 0, '2': 1, 'b': 1, '3': 2, 'c': 2, '4': 3, 'd': 3 };
    const lk = e.key.toLowerCase();

    if (lk in keyMap) {
      e.preventDefault();
      selectOption(keyMap[lk]);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      e.preventDefault(); navigate(-1);
    } else if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      e.preventDefault(); navigate(1);
    } else if (lk === 'm') {
      e.preventDefault(); toggleMark();
    } else if (lk === 'x' || e.key === 'Escape') {
      clearSelection();
    }
  }

  /* ── Palette Drawer (mobile) ────────────────────────────── */
  function openPalette() {
    App.qs('#palette-sidebar').classList.add('open');
    App.qs('#palette-overlay').classList.add('show');
    document.body.style.overflow = 'hidden';
  }

  function closePalette() {
    App.qs('#palette-sidebar').classList.remove('open');
    App.qs('#palette-overlay').classList.remove('show');
    document.body.style.overflow = '';
  }
})();
