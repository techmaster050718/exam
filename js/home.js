/**
 * js/home.js
 * Home page: paper list, progress dashboard, import/export.
 */
(function () {
  'use strict';

  const { App } = window;
  const root = App.qs('#app');

  /* ── Bootstrap ──────────────────────────────────────────── */
  async function init() {
    App.initTheme();
    App.qs('#theme-toggle').addEventListener('click', () => {
      const t = App.toggleTheme();
      App.qs('#theme-toggle').textContent = t === 'dark' ? '☀️' : '🌙';
    });
    App.qs('#theme-toggle').textContent = App.getTheme() === 'dark' ? '☀️' : '🌙';

    App.showLoading(root, 'Loading practice papers…');

    let papers;
    try {
      papers = await App.loadPapersList();
    } catch (err) {
      App.showError(root, 'Could not load papers', err.message.replace(/\n/g, '<br>'));
      return;
    }

    // Pre-calculate question count for each paper so cards always display accurate counts
    const paperCounts = {};
    await Promise.all(papers.map(async (p) => {
      try {
        const data = await App.loadPaper(p.file);
        const count = data.sections.reduce((acc, s) => acc + (s.questions ? s.questions.length : 0), 0);
        paperCounts[p.id] = count;
      } catch {
        paperCounts[p.id] = null;
      }
    }));

    render(papers, paperCounts);
  }

  /* ── Render ─────────────────────────────────────────────── */
  function render(papers, paperCounts = {}) {
    // Overall progress
    const prog = App.getOverallProgress(papers);

    // Find first not-completed
    const store = App.loadStore();
    const nextPaper = papers.find((p) => {
      const s = store[p.id];
      return !s || s.status !== 'submitted';
    });

    root.innerHTML = '';

    // Summary strip
    const summaryEl = buildSummary(prog);
    root.appendChild(summaryEl);

    // Recommendation
    if (nextPaper) {
      const rec = App.el('div', { className: 'recommendation glass' },
        App.el('span', {}, '🎯'),
        App.el('span', {}, 'Next recommended: '),
        App.el('strong', {}, nextPaper.title)
      );
      root.appendChild(rec);
    }

    // Section header
    const hdr = App.el('div', { className: 'section-header' },
      App.el('h2', { className: 'section-title' }, 'Practice Papers'),
      App.el('span', { className: 'text-muted', style: { fontSize: 'var(--text-sm)' } },
        `${papers.length} papers available`)
    );
    root.appendChild(hdr);

    // Grid
    const grid = App.el('div', { className: 'papers-grid', id: 'papers-grid' });
    papers.forEach((p) => {
      const count = paperCounts[p.id] || null;
      const card = buildPaperCard(p, store[p.id] || null, count);
      grid.appendChild(card);
    });
    root.appendChild(grid);

    // Footer
    root.appendChild(buildFooter());
  }

  /* ── Summary Strip ──────────────────────────────────────── */
  function buildSummary(prog) {
    const wrap = App.el('div', { className: 'summary-strip glass' });

    const stats = [
      { val: `${prog.completed}/${prog.total}`, lbl: 'Papers Completed' },
      { val: prog.completed > 0 ? `${prog.avg}%` : '—', lbl: 'Average Score' },
      { val: prog.bestPaper ? `${prog.bestPaper.pct}%` : '—', lbl: 'Best Score' },
      { val: prog.bestPaper ? prog.bestPaper.title : '—', lbl: 'Best Paper' },
    ];

    stats.forEach(({ val, lbl }) => {
      wrap.appendChild(App.el('div', { className: 'summary-stat' },
        App.el('span', { className: 'summary-stat-value' }, val),
        App.el('span', { className: 'summary-stat-label' }, lbl)
      ));
    });

    return wrap;
  }

  /* ── Paper Card ─────────────────────────────────────────── */
  function buildPaperCard(paper, state, questionCount = null) {
    const card = App.el('div', { className: 'paper-card glass' });

    // Count total questions from state or pre-loaded count
    const totalQ = state ? (state.totalQuestions || questionCount || '?') : (questionCount || '?');

    // Determine status
    let statusClass, statusText, statusDot;
    if (!state || state.status === 'not_started') {
      statusClass = 'badge-not-started';
      statusText  = 'Not Started';
      statusDot   = '○';
    } else if (state.status === 'in_progress') {
      const answered = Object.keys(state.answers || {}).length;
      statusClass = 'badge-in-progress';
      statusText  = `In Progress (${answered}/${totalQ})`;
      statusDot   = '◐';
    } else {
      statusClass = 'badge-completed';
      statusText  = 'Completed';
      statusDot   = '✓';
    }

    // Header
    const badgeEl = App.el('span', { className: `status-badge ${statusClass}` }, statusDot, ' ' + statusText);
    card.appendChild(App.el('div', { className: 'card-header' },
      App.el('div', {},
        App.el('div', { className: 'card-title' }, paper.title),
        App.el('div', { className: 'card-subtitle' }, paper.subtitle)
      ),
      badgeEl
    ));

    // Best score badge
    if (state && state.attempts && state.attempts.length > 0) {
      const best = state.attempts.reduce((b, a) => a.percentage > b.percentage ? a : b, state.attempts[0]);
      card.appendChild(App.el('div', {},
        App.el('span', { className: 'best-score-badge' },
          '🏆 Best: ', `${best.percentage}%`
        )
      ));
    }

    // Meta chips
    const meta = App.el('div', { className: 'card-meta' });
    meta.appendChild(App.el('span', { className: 'meta-chip' }, `⏱ ${paper.durationMin} min`));
    if (totalQ !== '?') {
      meta.appendChild(App.el('span', { className: 'meta-chip' }, `📝 ${totalQ} questions`));
    }
    meta.appendChild(App.el('span', { className: 'meta-chip' }, `+${paper.correctMark} / −${paper.negativeMark}`));
    card.appendChild(meta);

    // Score if completed
    if (state && state.status === 'submitted') {
      const pctClass = state.percentage >= 60 ? 'text-success' : state.percentage >= 35 ? '' : 'text-danger';
      card.appendChild(App.el('div', { className: 'card-score' },
        App.el('span', { className: 'card-score-value' }, `${state.score}/${state.totalMark}`),
        App.el('span', { className: `card-score-label ${pctClass}` }, `${state.percentage}%  ·  ${state.correct}✓  ${state.wrong}✗`)
      ));

      // Progress bar (pct of total marks)
      const pct = Math.max(0, Math.min(100, state.percentage));
      card.appendChild(App.el('div', { className: 'progress-bar-wrap' },
        App.el('div', { className: 'progress-bar-fill', style: { width: `${pct}%` } })
      ));
    } else if (state && state.status === 'in_progress') {
      const answered = Object.keys(state.answers || {}).length;
      const tq = typeof totalQ === 'number' ? totalQ : (state.totalQuestions || 1);
      const pct = Math.round((answered / tq) * 100);
      card.appendChild(App.el('div', { className: 'progress-bar-wrap' },
        App.el('div', { className: 'progress-bar-fill', style: { width: `${pct}%` } })
      ));
    }

    // Attempt history
    if (state && state.attempts && state.attempts.length > 0) {
      const hist = document.createElement('details');
      hist.className = 'attempt-history';
      const summ = document.createElement('summary');
      summ.textContent = `📋 ${state.attempts.length} attempt${state.attempts.length > 1 ? 's' : ''} history`;
      hist.appendChild(summ);
      const list = App.el('ul', { className: 'attempt-list' });
      [...state.attempts].reverse().forEach((a, i) => {
        list.appendChild(App.el('li', { className: 'attempt-item' },
          App.el('span', {}, App.formatDate(a.date)),
          App.el('span', {}, `${a.score}/${a.totalMark}  (${a.percentage}%)`)
        ));
      });
      hist.appendChild(list);
      card.appendChild(hist);
    }

    // Action buttons
    const actions = App.el('div', { className: 'card-actions' });

    if (!state || state.status === 'not_started') {
      const startBtn = App.el('button', { className: 'btn btn-primary' }, '▶ Start');
      startBtn.addEventListener('click', () => startPaper(paper));
      actions.appendChild(startBtn);
    } else if (state.status === 'in_progress') {
      const resumeBtn = App.el('button', { className: 'btn btn-primary' }, '↩ Resume');
      resumeBtn.addEventListener('click', () => window.location.href = `test.html?paper=${paper.id}`);
      actions.appendChild(resumeBtn);
      const retakeBtn = App.el('button', { className: 'btn btn-ghost btn-sm' }, '🔄 Retake');
      retakeBtn.addEventListener('click', () => retakePaper(paper, state));
      actions.appendChild(retakeBtn);
    } else {
      const reviewBtn = App.el('button', { className: 'btn btn-primary' }, '📊 View Result');
      reviewBtn.addEventListener('click', () => window.location.href = `result.html?paper=${paper.id}`);
      actions.appendChild(reviewBtn);
      const retakeBtn = App.el('button', { className: 'btn btn-secondary' }, '🔄 Retake');
      retakeBtn.addEventListener('click', () => retakePaper(paper, state));
      actions.appendChild(retakeBtn);
    }

    card.appendChild(actions);
    return card;
  }

  /* ── Paper Actions ──────────────────────────────────────── */
  async function startPaper(paper, prevAttempts = []) {
    // Load the paper first to get question count
    App.showToast('Starting paper…');
    try {
      const data = await App.loadPaper(paper.file);
      const questions = App.flattenQuestions(data);
      const now = new Date().toISOString();
      App.savePaperState(paper.id, {
        status: 'in_progress',
        answers: {},
        marked: [],
        visited: [],
        currentQuestion: 0,
        startedAt: now,
        totalQuestions: questions.length,
        attempts: prevAttempts,
      });
      window.location.href = `test.html?paper=${paper.id}`;
    } catch (err) {
      App.showToast('Error: ' + err.message, 'error', 5000);
    }
  }

  function retakePaper(paper, state) {
    if (!confirm(`Retake "${paper.title}"? Your current in-progress attempt will be cleared.\nAll completed attempt scores are preserved in history.`)) return;
    // Preserve completed attempts history when clearing state
    const prevAttempts = [...(state.attempts || [])];
    App.clearPaperState(paper.id);
    // Start fresh but carry over previous attempts
    startPaper(paper, prevAttempts);
  }

  /* ── Footer / Data Management ───────────────────────────── */
  function buildFooter() {
    const footer = App.el('div', { className: 'home-footer' });

    const exportBtn = App.el('button', { className: 'btn btn-secondary btn-sm' }, '⬇ Export Progress');
    exportBtn.addEventListener('click', () => {
      const data = App.exportStore();
      const blob = new Blob([data], { type: 'application/json' });
      const url  = URL.createObjectURL(blob);
      const a    = App.el('a', { href: url, download: 'ibps-mocktest-progress.json' });
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
      App.showToast('Progress exported!', 'success');
    });

    const importBtn = App.el('button', { className: 'btn btn-secondary btn-sm' }, '⬆ Import Progress');
    importBtn.addEventListener('click', () => {
      const inp = App.el('input', { type: 'file', accept: '.json' });
      inp.addEventListener('change', (e) => {
        const file = e.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (re) => {
          try {
            App.importStore(re.target.result);
            App.showToast('Progress imported!', 'success');
            setTimeout(() => window.location.reload(), 800);
          } catch {
            App.showToast('Invalid file. Could not import.', 'error');
          }
        };
        reader.readAsText(file);
      });
      inp.click();
    });

    const resetBtn = App.el('button', { className: 'btn btn-danger btn-sm' }, '🗑 Reset All Data');
    resetBtn.addEventListener('click', () => {
      if (confirm('Reset ALL progress? This cannot be undone.')) {
        App.resetAll();
        App.showToast('All data reset.', 'success');
        setTimeout(() => window.location.reload(), 800);
      }
    });

    footer.appendChild(exportBtn);
    footer.appendChild(importBtn);
    footer.appendChild(resetBtn);
    return footer;
  }

  /* ── Boot ───────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', init);
})();
