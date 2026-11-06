/** Home dashboard: subjects, overall progress, and data management. */
(function () {
  'use strict'; const { App } = window; const root = App.qs('#app');
  document.addEventListener('DOMContentLoaded', init);
  async function init() {
    App.initTheme(); const toggle = App.qs('#theme-toggle'); toggle.textContent = App.getTheme() === 'dark' ? '☀️' : '🌙'; toggle.onclick = () => { toggle.textContent = App.toggleTheme() === 'dark' ? '☀️' : '🌙'; };
    App.showLoading(root, 'Loading subjects…');
    try { const [site, papers, raw] = await Promise.all([App.applyBranding(), App.loadPapersList(), App.loadSubjects()]); render(site, App.normaliseSubjects(raw, papers), papers); } catch (err) { App.showError(root, 'Could not load practice papers', err.message); }
  }
  function render(site, subjects, papers) {
    const overall = App.getOverallProgress(papers); root.innerHTML = '';
    root.appendChild(summary([[`${overall.completed}/${overall.total}`, 'Papers completed'], [overall.completed ? `${overall.avg}%` : '—', 'Average score'], [overall.bestPaper ? `${overall.bestPaper.pct}%` : '—', 'Best score'], [overall.bestPaper ? overall.bestPaper.title : '—', 'Best paper']]));
    root.appendChild(App.el('div', { className: 'section-header' }, App.el('h2', { className: 'section-title' }, 'Choose a subject'), App.el('span', { className: 'text-muted' }, `${subjects.length} subjects`)));
    const grid = App.el('div', { className: 'subjects-grid' }); subjects.forEach((s) => grid.appendChild(subjectCard(s, papers.filter((p) => App.subjectIdFor(p, subjects) === s.id)))); root.appendChild(grid);
    root.appendChild(footer(site.footer));
  }
  function summary(stats) { const wrap = App.el('div', { className: 'summary-strip glass' }); stats.forEach(([v, l]) => wrap.appendChild(App.el('div', { className: 'summary-stat' }, App.el('span', { className: 'summary-stat-value' }, v), App.el('span', { className: 'summary-stat-label' }, l)))); return wrap; }
  function subjectCard(s, papers) { const done = papers.filter((p) => App.getPaperState(p.id)?.status === 'submitted'); const avg = done.length ? Math.round(done.reduce((n,p) => n + (App.getPaperState(p.id).percentage || 0), 0) / done.length * 10) / 10 : null; const card = App.el(papers.length ? 'a' : 'div', { className: `subject-card glass${papers.length ? '' : ' is-empty'}`, ...(papers.length ? { href: `subject.html?subject=${encodeURIComponent(s.id)}` } : {}) }); card.append(App.el('div', { className: 'subject-icon' }, s.icon || '📚'), App.el('div', { className: 'card-title' }, s.title), App.el('p', { className: 'subject-description' }, s.description || 'Practice papers'), App.el('div', { className: 'subject-card-stats' }, papers.length ? `${papers.length} papers · ${done.length} completed${avg === null ? '' : ` · ${avg}% average`}` : 'Coming soon')); return card; }
  function footer(message) {
    const f = App.el('footer', { className: 'home-footer' });
    const reset = App.el('button', { className: 'btn btn-danger btn-sm reset-data-btn' }, '🗑 Reset All Data');
    reset.onclick = () => {
      if (confirm('Reset all progress and settings? This cannot be undone.')) {
        App.resetAll();
        location.reload();
      }
    };
    f.append(App.el('p', { className: 'footer-message' }, message), reset);
    return f;
  }
})();
