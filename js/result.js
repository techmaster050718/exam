/**
 * js/result.js
 * Result page: score card, subject-wise analysis, answer review.
 */
(function () {
  'use strict';

  const { App } = window;
  let paperMeta = null;
  let paperData = null;
  let questions = [];
  let state     = null;
  let activeFilter = 'all';

  /* ── Boot ───────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', async () => {
    App.initTheme();
    App.qs('#theme-toggle').addEventListener('click', () => {
      const t = App.toggleTheme();
      App.qs('#theme-toggle').textContent = t === 'dark' ? '☀️' : '🌙';
    });
    App.qs('#theme-toggle').textContent = App.getTheme() === 'dark' ? '☀️' : '🌙';

    const paperId = App.getParam('paper');
    if (!paperId) { window.location.href = 'index.html'; return; }

    const root = App.qs('#result-root');
    App.showLoading(root, 'Loading results…');

    try {
      const papers = await App.loadPapersList();
      paperMeta = papers.find((p) => p.id === paperId);
      if (!paperMeta) throw new Error(`Paper "${paperId}" not found`);

      state = App.getPaperState(paperId);
      if (!state || state.status !== 'submitted') {
        // Not submitted — redirect home
        window.location.href = 'index.html';
        return;
      }

      paperData = await App.loadPaper(paperMeta.file);
      questions = App.flattenQuestions(paperData);

      // Find next paper
      const idx     = papers.findIndex((p) => p.id === paperId);
      const nextP   = papers[idx + 1] || null;

      render(root, nextP, papers);

    } catch (err) {
      App.showError(root, 'Failed to load result', err.message.replace(/\n/g, '<br>'));
    }
  });

  /* ── Render ─────────────────────────────────────────────── */
  function render(root, nextPaper, allPapers) {
    root.innerHTML = '';

    root.appendChild(buildScoreHero());
    root.appendChild(buildSubjectTable());
    root.appendChild(buildAttemptHistory());
    root.appendChild(buildAnswerReview());
    root.appendChild(buildActions(nextPaper, allPapers));
  }

  /* ── Score Hero ─────────────────────────────────────────── */
  function buildScoreHero() {
    const wrap = App.el('div', { className: 'section-box glass score-hero' });

    // Label
    wrap.appendChild(App.el('div', { className: 'score-label' }, paperMeta.title));

    // Big score
    wrap.appendChild(App.el('div', { className: 'score-main', 'aria-live': 'polite' },
      String(state.score)
    ));
    wrap.appendChild(App.el('div', { className: 'score-total' },
      `out of ${state.totalMark} marks`
    ));

    // Percentage badge
    const pct = state.percentage;
    const pctClass = pct >= 60 ? 'pct-high' : pct >= 35 ? 'pct-mid' : 'pct-low';
    wrap.appendChild(App.el('div', { className: `score-pct ${pctClass}` },
      `${pct}%`
    ));

    // Stats grid
    const grid = App.el('div', { className: 'result-stats-grid' });
    const stats = [
      { cls: 'stat-correct',  val: state.correct,                    lbl: 'Correct' },
      { cls: 'stat-wrong',    val: state.wrong,                      lbl: 'Wrong' },
      { cls: 'stat-unatt',    val: state.unattempted,                lbl: 'Unattempted' },
      { cls: 'stat-penalty',  val: `−${state.penalty}`,              lbl: 'Marks Lost' },
      { cls: 'stat-accuracy', val: `${state.accuracy}%`,             lbl: 'Accuracy' },
      { cls: 'stat-time',     val: App.formatDuration(state.timeTakenSec), lbl: 'Time Taken' },
    ];
    stats.forEach(({ cls, val, lbl }) => {
      grid.appendChild(App.el('div', { className: `result-stat ${cls}` },
        App.el('span', { className: 'result-stat-val' }, String(val)),
        App.el('span', { className: 'result-stat-lbl' }, lbl)
      ));
    });

    wrap.appendChild(grid);
    return wrap;
  }

  /* ── Subject-wise Table ─────────────────────────────────── */
  function buildSubjectTable() {
    const wrap = App.el('div', { className: 'section-box glass' });
    wrap.appendChild(App.el('h2', { className: 'section-box-title' }, '📚 Subject-wise Performance'));

    const sections = state.sectionStats || App.computeSectionStats(questions, state.answers, paperMeta);

    // Identify best/worst when score variation exists
    const withPct = sections.map((s) => ({ ...s, _pct: s.marks / s.totalMarks }));
    let minPct = Infinity, maxPct = -Infinity;
    withPct.forEach((s) => {
      if (s._pct > maxPct) maxPct = s._pct;
      if (s._pct < minPct) minPct = s._pct;
    });
    const hasVariation = sections.length > 1 && maxPct > minPct;

    const table = App.el('table', { className: 'subj-table' });
    const thead = App.el('thead', {},
      App.el('tr', {},
        App.el('th', {}, 'Subject'),
        App.el('th', {}, 'Total'),
        App.el('th', {}, 'Attempted'),
        App.el('th', {}, 'Correct'),
        App.el('th', {}, 'Wrong'),
        App.el('th', {}, 'Marks'),
        App.el('th', {}, 'Score %'),
        App.el('th', {}, 'Bar')
      )
    );
    table.appendChild(thead);

    const tbody = App.el('tbody');
    sections.forEach((s, i) => {
      const pct = s.totalMarks > 0
        ? Math.round((Math.max(s.marks, 0) / s.totalMarks) * 10000) / 100
        : 0;
      const tr  = App.el('tr', {});
      const isBest  = hasVariation && withPct[i]._pct === maxPct;
      const isWorst = hasVariation && withPct[i]._pct === minPct && !isBest;
      if (isBest)  tr.classList.add('highlight-best');
      if (isWorst) tr.classList.add('highlight-worst');

      const barClass = pct >= 60 ? '' : pct >= 35 ? 'bar-warning' : 'bar-danger';
      const bar = App.el('div', { className: 'subj-bar-wrap' },
        App.el('div', { className: `subj-bar-fill ${barClass}`, style: { width: `${pct}%` } })
      );

      const badge = isBest ? ' 🏆 (Strongest)' : isWorst ? ' ⚠️ (Weakest)' : '';

      tr.appendChild(App.el('td', {}, s.name + badge));
      tr.appendChild(App.el('td', {}, String(s.total)));
      tr.appendChild(App.el('td', {}, String(s.attempted)));
      tr.appendChild(App.el('td', { style: { color: 'var(--success)' } }, String(s.correct)));
      tr.appendChild(App.el('td', { style: { color: 'var(--danger)' } },  String(s.wrong)));
      tr.appendChild(App.el('td', {}, String(s.marks)));
      tr.appendChild(App.el('td', {}, `${pct}%`));
      tr.appendChild(App.el('td', {}, bar));

      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
    const tableWrap = App.el('div', { style: { overflowX: 'auto', WebkitOverflowScrolling: 'touch', width: '100%' } });
    tableWrap.appendChild(table);
    wrap.appendChild(tableWrap);
    return wrap;
  }

  /* ── Attempt History ────────────────────────────────────── */
  function buildAttemptHistory() {
    const attempts = state.attempts || [];
    if (attempts.length === 0) return App.el('div');

    const details = document.createElement('details');
    details.className = 'collapsible mb-lg';
    if (attempts.length <= 3) details.open = true;

    const summ = document.createElement('summary');
    summ.innerHTML = `📋 Attempt History (${attempts.length})  <span style="font-size:var(--text-xs);color:var(--text-muted)">▼</span>`;
    details.appendChild(summ);

    const content = App.el('div', { className: 'collapsible-content' });
    const list = App.el('div', { className: 'attempt-history-list' });

    attempts.forEach((a, i) => {
      const isCurrent = i === attempts.length - 1;
      const row = App.el('div', { className: `attempt-row${isCurrent ? ' current-attempt' : ''}` },
        App.el('span', {}, `#${i + 1}  ${App.formatDate(a.date)}`),
        App.el('span', { style: { color: 'var(--accent)', fontWeight: '700' } },
          `${a.score}/${a.totalMark}  (${a.percentage}%)  — ${App.formatDuration(a.timeTakenSec)}`
        )
      );
      if (isCurrent) {
        row.appendChild(App.el('span', { className: 'status-badge badge-completed', style: { marginLeft: '8px' } }, '← This attempt'));
      }
      list.appendChild(row);
    });

    content.appendChild(list);
    details.appendChild(content);
    return details;
  }

  /* ── Answer Review ──────────────────────────────────────── */
  function buildAnswerReview() {
    const details = document.createElement('details');
    details.className = 'collapsible mb-lg';
    details.open = true;

    const summ = document.createElement('summary');
    summ.innerHTML = `📝 Full Answer Review  <span style="font-size:var(--text-xs);color:var(--text-muted)">▼</span>`;
    details.appendChild(summ);

    const content = App.el('div', { className: 'collapsible-content' });

    // Filter buttons
    const filters = App.el('div', { className: 'review-filters', role: 'group', 'aria-label': 'Filter questions' });
    const filterDefs = [
      { key: 'all',         label: 'All' },
      { key: 'correct',     label: '✓ Correct' },
      { key: 'wrong',       label: '✗ Wrong' },
      { key: 'unattempted', label: '— Unattempted' },
      { key: 'marked',      label: '◉ Marked' },
    ];
    filterDefs.forEach(({ key, label }) => {
      const btn = App.el('button', {
        className: `filter-btn${key === activeFilter ? ' active' : ''}`,
        'aria-pressed': key === activeFilter ? 'true' : 'false',
        dataset: { filter: key }
      }, label);
      btn.addEventListener('click', () => {
        activeFilter = key;
        App.qsa('.filter-btn').forEach((b) => {
          b.classList.toggle('active', b.dataset.filter === key);
          b.setAttribute('aria-pressed', b.dataset.filter === key ? 'true' : 'false');
        });
        renderReviewCards(reviewList);
      });
      filters.appendChild(btn);
    });
    content.appendChild(filters);

    // Review list
    const reviewList = App.el('div', { id: 'review-list' });
    renderReviewCards(reviewList);
    content.appendChild(reviewList);

    details.appendChild(content);
    return details;
  }

  function renderReviewCards(container) {
    container.innerHTML = '';
    const keys = ['A', 'B', 'C', 'D'];
    const marked = state.marked || [];

    let count = 0;
    questions.forEach((q, globalIdx) => {
      // answers keys may be strings after JSON round-trip
      const rawChosen = state.answers[globalIdx] ?? state.answers[String(globalIdx)];
      const chosen   = (rawChosen === undefined || rawChosen === null) ? undefined : Number(rawChosen);
      const answered = chosen !== undefined;
      const correct  = answered && chosen === q.answer;
      const wrong    = answered && chosen !== q.answer;
      const isMarked = marked.includes(globalIdx);

      // Filter
      if (activeFilter === 'correct'     && !correct)    return;
      if (activeFilter === 'wrong'       && !wrong)      return;
      if (activeFilter === 'unattempted' && answered)    return;
      if (activeFilter === 'marked'      && !isMarked)   return;

      count++;
      const cardClass = correct ? 'card-correct' : wrong ? 'card-wrong' : 'card-unatt';
      const card = App.el('div', { className: `review-card ${cardClass}` });

      // Header
      const header = App.el('div', { className: 'review-q-header' },
        App.el('span', { className: 'review-q-num' }, `Q${globalIdx + 1} · ${q.sectionName}`)
      );
      const tagWrap = App.el('div', { style: { display: 'flex', gap: '4px', flexWrap: 'wrap' } });
      if (correct)  tagWrap.appendChild(App.el('span', { className: 'review-status-tag tag-correct' }, '✓ Correct'));
      if (wrong)    tagWrap.appendChild(App.el('span', { className: 'review-status-tag tag-wrong' },   '✗ Wrong'));
      if (!answered)tagWrap.appendChild(App.el('span', { className: 'review-status-tag tag-unatt' },   '— Skipped'));
      if (isMarked) tagWrap.appendChild(App.el('span', { className: 'review-status-tag tag-marked' },  '◉ Marked'));
      header.appendChild(tagWrap);
      card.appendChild(header);

      // Question text
      const qText = App.el('div', { className: 'review-q-text' });
      qText.innerHTML = App.renderText(q.q);
      card.appendChild(qText);

      // Options
      const optList = App.el('div', { className: 'review-options' });
      q.options.forEach((opt, oi) => {
        const isAnswer   = oi === q.answer;
        const isChosen   = oi === chosen;
        const isBothWrong = isChosen && !isAnswer;

        let cls = 'review-opt';
        let icon = '';
        if (isAnswer)        { cls += ' opt-correct'; icon = '✓'; }
        else if (isBothWrong){ cls += ' opt-selected-wrong'; icon = '✗'; }

        const optEl = App.el('div', { className: cls },
          App.el('span', { className: 'opt-icon' }, icon),
          App.el('span', { className: 'opt-key-label' }, keys[oi]),
          App.el('span', {})
        );
        optEl.querySelector('span:last-child').innerHTML = App.renderText(opt);

        // Show "Your answer" label
        if (isChosen) {
          const lbl = App.el('span', {
            style: {
              fontSize: 'var(--text-xs)',
              marginLeft: 'auto',
              color: isAnswer ? 'var(--success)' : 'var(--danger)',
              fontWeight: '700',
              flexShrink: '0'
            }
          }, 'Your answer');
          optEl.appendChild(lbl);
        }

        optList.appendChild(optEl);
      });
      card.appendChild(optList);
      container.appendChild(card);
    });

    if (count === 0) {
      container.appendChild(App.el('div', {
        className: 'text-center text-muted',
        style: { padding: 'var(--space-xl)' }
      }, 'No questions match this filter.'));
    }
  }

  /* ── Action Buttons ─────────────────────────────────────── */
  function buildActions(nextPaper, allPapers) {
    const wrap = App.el('div', { className: 'result-actions' });

    const homeBtn = App.el('a', { href: 'index.html', className: 'btn btn-secondary btn-lg' }, '← Back to Home');
    wrap.appendChild(homeBtn);

    const retakeBtn = App.el('button', { className: 'btn btn-secondary btn-lg' }, '🔄 Retake Paper');
    retakeBtn.addEventListener('click', () => {
      if (!confirm(`Retake "${paperMeta.title}"? Your previous scores will remain safely saved in history.`)) return;
      const prevAttempts = [...(state.attempts || [])];
      App.savePaperState(paperMeta.id, {
        status: 'in_progress',
        answers: {},
        marked: [],
        visited: [],
        currentQuestion: 0,
        startedAt: new Date().toISOString(),
        totalQuestions: questions.length,
        attempts: prevAttempts,
      });
      window.location.href = `test.html?paper=${paperMeta.id}`;
    });
    wrap.appendChild(retakeBtn);

    if (nextPaper) {
      const nextBtn = App.el('button', { className: 'btn btn-primary btn-lg' },
        `Next: ${nextPaper.title} →`
      );
      nextBtn.addEventListener('click', async () => {
        App.showToast('Loading next paper…');
        try {
          const data = await App.loadPaper(nextPaper.file);
          const qs   = App.flattenQuestions(data);
          const existing = App.getPaperState(nextPaper.id);
          if (!existing || existing.status === 'not_started' || !existing.status) {
            App.savePaperState(nextPaper.id, {
              status: 'in_progress',
              answers: {},
              marked: [],
              visited: [],
              currentQuestion: 0,
              startedAt: new Date().toISOString(),
              totalQuestions: qs.length,
              attempts: existing ? (existing.attempts || []) : [],
            });
          }
          window.location.href = `test.html?paper=${nextPaper.id}`;
        } catch (err) {
          App.showToast('Could not load next paper: ' + err.message, 'error');
        }
      });
      wrap.appendChild(nextBtn);
    }

    return wrap;
  }
})();
