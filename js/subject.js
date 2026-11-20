/** Subject page: paper cards and cross-paper section analytics. */
(function () {
  'use strict'; const { App } = window; const root = App.qs('#subject-root');
  document.addEventListener('DOMContentLoaded', init);
  async function init() {
    App.initTheme();
    App.initLanguageMode();
    const revisionLink = App.qs('#revision-link');
    revisionLink.addEventListener('click', (event) => {
      event.preventDefault();
      window.location.assign(revisionLink.href);
    });
    const toggle = App.qs('#theme-toggle');
    toggle.textContent = App.getTheme() === 'dark' ? '☀️' : '🌙';
    toggle.addEventListener('click', () => {
      toggle.textContent = App.toggleTheme() === 'dark' ? '☀️' : '🌙';
    });
    App.showLoading(root, 'Loading subject…');
    try {
      const [site, papers, raw] = await Promise.all([App.applyBranding(), App.loadPapersList(), App.loadSubjects()]);
      const subjects = App.normaliseSubjects(raw, papers);
      const subject = subjects.find((s) => s.id === App.getParam('subject'));
      if (!subject) throw new Error('This subject does not exist.');
      document.title = `${subject.title} – ${site.name}`;
      const subjectPapers = papers.filter((p) => App.subjectIdFor(p, subjects) === subject.id);
      await render(subject, subjectPapers);
      if (['up-police-si', 'rrb-alp'].includes(subject.id)) await renderQuestionBankSearch(subject, subjectPapers);
    } catch (err) { App.showError(root, 'Could not load subject', err.message); }
  }
  async function render(subject, papers) { root.innerHTML = ''; root.append(App.el('nav', { className: 'breadcrumb', 'aria-label': 'Breadcrumb' }, App.el('a', { href: 'index.html' }, 'Home'), App.el('span', {}, '›'), App.el('span', {}, subject.title)), App.el('section', { className: 'subject-hero' }, App.el('span', { className: 'subject-icon' }, subject.icon || '📚'), App.el('div', {}, App.el('h1', {}, subject.title), App.el('p', {}, subject.description || 'Practice papers')))); const practicePapers = papers.filter((paper) => paper.file); const stats = getStats(practicePapers); root.appendChild(summary([[`${stats.completed}/${practicePapers.length}`, 'Papers completed'], [stats.avg === null ? '—' : `${stats.avg}%`, 'Average score'], [stats.best === null ? '—' : `${stats.best}%`, 'Best score']])); if (subject.id === 'cds') root.appendChild(renderCdsAnalysis(papers)); if (stats.completed) root.appendChild(await weakTopics(practicePapers)); root.appendChild(App.el('div', { className: 'section-header' }, App.el('h2', { className: 'section-title' }, 'Practice papers and PYQ sources'))); if (subject.id === 'cds') root.appendChild(renderCdsFilters(papers)); const grid = App.el('div', { className: 'papers-grid', id: 'cds-papers-grid' }); papers.forEach((p) => grid.appendChild(paperCard(p))); if (!papers.length) grid.appendChild(App.el('p', { className: 'text-muted' }, 'Coming soon.')); root.appendChild(grid); }

  async function renderQuestionBankSearch(subject, papers) {
    const indexedQuestions = (await Promise.all(papers.map(async (paper) => {
      const data = await App.loadPaper(paper.file);
      return App.flattenQuestions(data).map((question) => ({ paper, question }));
    }))).flat();
    const input = App.el('input', {
      id: 'bank-question-search',
      type: 'search',
      placeholder: 'हिंदी / English, exam, subject, year, shift…',
      autocomplete: 'off',
      'aria-label': 'Search Hindi or English questions, options, exam, subject, year, or shift',
    });
    const status = App.el('p', { className: 'bank-search-status', role: 'status' }, 'Search questions and options in Hindi or English, or search by exam, subject, year, or shift.');
    const results = App.el('div', { className: 'bank-search-results' });
    const search = App.el('section', { className: 'bank-question-search glass', 'aria-labelledby': 'bank-search-title' },
      App.el('h2', { id: 'bank-search-title', className: 'section-title' }, `Search ${subject.title} question bank`),
      input,
      status,
      results
    );
    const paperHeader = root.querySelector('.section-header');
    root.insertBefore(search, paperHeader || null);

    input.addEventListener('input', () => {
      const query = input.value.trim().toLocaleLowerCase();
      results.innerHTML = '';
      if (!query) {
        status.textContent = 'Search questions and options in Hindi or English, or search by exam, subject, year, or shift.';
        return;
      }

      const matches = indexedQuestions.filter(({ paper, question }) =>
        App.getQuestionSearchText(question, paper).includes(query)
      );
      status.textContent = matches.length
        ? `Showing ${Math.min(matches.length, 50)} of ${matches.length} matching questions.`
        : 'No questions match this search.';
      matches.slice(0, 50).forEach(({ paper, question }) => {
        const card = App.el('article', { className: 'bank-search-result' });
        const metadata = [
          paper.title,
          question.sectionName,
          question.year,
          question.shift,
          question.sourceType,
        ].filter(Boolean).join(' · ');
        card.append(
          App.el('div', { className: 'bank-search-metadata' }, metadata),
          App.el('div', { className: 'bank-search-question' }, App.renderBilingualText(question.q))
        );
        const options = App.el('div', { className: 'bank-search-options' });
        question.options.forEach((option, index) => {
          options.appendChild(App.el('div', { className: 'bank-search-option' },
            `${String.fromCharCode(65 + index)}. `,
            App.renderBilingualText(option)
          ));
        });
        card.append(
          options,
          App.el('a', {
            className: 'btn btn-primary btn-sm',
            href: `test.html?paper=${encodeURIComponent(paper.id)}&question=${question.globalIndex}`,
          }, 'Open question')
        );
        results.appendChild(card);
      });
    });
    window.addEventListener(App.LANGUAGE_MODE_EVENT, () => {
      input.dispatchEvent(new Event('input'));
    });
  }
  function summary(stats) { const wrap = App.el('div', { className: 'summary-strip glass' }); stats.forEach(([v,l]) => wrap.appendChild(App.el('div', { className: 'summary-stat' }, App.el('span', { className: 'summary-stat-value' }, v), App.el('span', { className: 'summary-stat-label' }, l)))); return wrap; }
  function getStats(papers) { const states = papers.map((p) => App.getPaperState(p.id)).filter((s) => s?.status === 'submitted'); const values = states.map((s) => s.percentage || 0); return { completed: states.length, avg: values.length ? Math.round(values.reduce((a,b)=>a+b,0)/values.length*10)/10 : null, best: values.length ? Math.max(...values) : null }; }
  async function weakTopics(papers) { const all = {}; await Promise.all(papers.map(async (p) => { const state = App.getPaperState(p.id); if (state?.status !== 'submitted') return; const data = await App.loadPaper(p.file); (state.sectionStats || App.computeSectionStats(App.flattenQuestions(data), state.answers, p)).forEach((s) => { (all[s.name] ||= []).push(s.percentage); }); })); const topics = Object.entries(all).map(([name, vals]) => [name, Math.round(vals.reduce((a,b)=>a+b,0)/vals.length*10)/10]).sort((a,b)=>a[1]-b[1]).slice(0,3); const box = App.el('section', { className: 'weak-topics glass' }, App.el('h2', { className: 'section-title' }, 'Weak topics'), App.el('p', {}, 'Lowest average section scores across completed papers.')); const list = App.el('ul'); topics.forEach(([n,v]) => list.appendChild(App.el('li', {}, `${n}: ${v}%`))); box.appendChild(list); return box; }
  function renderCdsAnalysis(papers) {
    const realSources = papers.filter((paper) => paper.paperType === 'REAL_PYQ').length;
    const prediction = papers.find((paper) => paper.paperType === 'PREDICTED');
    const box = App.el('section', { className: 'glass weak-topics' },
      App.el('h2', { className: 'section-title' }, 'CDS PYQ Sources and Analysis'),
      App.el('p', {}, `${realSources} subject-paper source links are registered across four sessions. The PDFs open on their archive hosts; question text has not been copied into this site and cannot be attempted in the in-app timer or scoring engine.`)
    );
    box.append(
      App.el('p', {}, 'Source pages identify these as previous-year CDS papers, but their contents have not been independently matched against UPSC originals. Open each source to inspect its paper and answer information.'),
      App.el('h3', {}, 'In-app analysis status'),
      App.el('p', {}, 'No real-PYQ questions have been imported, so topic frequencies, difficulty trends and 10-year recurrence statistics are not yet available. The prediction paper remains a separate original practice set.'),
      App.el('p', { className: 'text-muted' }, `Source-linked subject papers: ${realSources} · Imported real-PYQ questions: 0 · Prediction questions: ${prediction ? 300 : 0}`)
    );
    return box;
  }
  function renderCdsFilters(papers) {
    const controls = App.el('div', { className: 'cds-filters' });
    const type = App.el('select', { 'aria-label': 'Filter by paper type' },
      new Option('Type: All', 'all'), new Option('REAL PYQ', 'REAL_PYQ'), new Option('PREDICTED', 'PREDICTED')
    );
    const subject = App.el('select', { 'aria-label': 'Filter by subject' },
      new Option('Subject: All', 'all')
    );
    const year = App.el('select', { 'aria-label': 'Filter by year' },
      new Option('Year: All', 'all')
    );
    const session = App.el('select', { 'aria-label': 'Filter by session' },
      new Option('Session: All', 'all')
    );
    [...new Set(papers.map((paper) => paper.paperSubject).filter(Boolean))].sort().forEach((value) => {
      subject.add(new Option(value, value));
    });
    [...new Set(papers.map((paper) => String(paper.year)).filter(Boolean))].sort((a, b) => b.localeCompare(a)).forEach((value) => {
      year.add(new Option(value, value));
    });
    [...new Set(papers.map((paper) => paper.session).filter(Boolean))].sort().forEach((value) => {
      session.add(new Option(value, value));
    });
    controls.append(type, year, session, subject);
    controls.addEventListener('change', () => {
      const grid = App.qs('#cds-papers-grid');
      grid.innerHTML = '';
      const visible = papers.filter((p) =>
        (type.value === 'all' || p.paperType === type.value) &&
        (subject.value === 'all' || p.paperSubject === subject.value) &&
        (year.value === 'all' || String(p.year) === year.value) &&
        (session.value === 'all' || p.session === session.value)
      );
      visible.forEach((p) => grid.appendChild(paperCard(p)));
      if (!visible.length) grid.appendChild(App.el('p', { className: 'text-muted' }, 'No CDS papers match these filters.'));
    });
    return controls;
  }
  function paperCard(p) {
    const card = App.el('article', { className: 'paper-card glass' },
      App.el('div', { className: 'card-title' }, p.title),
      App.el('div', { className: 'card-subtitle' }, p.subtitle),
      App.el('div', { className: 'card-meta' },
        App.el('span', { className: 'meta-chip' }, p.paperType || 'Practice'),
        ...(p.durationMin ? [App.el('span', { className: 'meta-chip' }, `⏱ ${p.durationMin} min`)] : []),
        ...(p.paperSubject ? [App.el('span', { className: 'meta-chip' }, p.paperSubject)] : []),
        ...(p.sourceUrl ? [App.el('span', { className: 'meta-chip' }, 'External source · not in-app scored')] : []),
        ...(!p.sourceUrl ? [App.el('span', { className: 'meta-chip' }, `+${p.correctMark} / −${p.negativeMark}`)] : [])
      )
    );
    if (p.sourceUrl) {
      card.appendChild(App.el('div', { className: 'card-actions' },
        App.el('a', {
          className: 'btn btn-primary',
          href: p.sourceUrl,
          target: '_blank',
          rel: 'noopener noreferrer'
        }, p.sourceType === 'EXTERNAL_ARCHIVE_LISTING' ? 'Open archive listing' : 'Open source PDF')
      ));
      card.appendChild(App.el('p', { className: 'text-muted' }, p.verificationStatus));
      return card;
    }
    const state = App.getPaperState(p.id);
    if (state?.status === 'submitted') card.appendChild(App.el('div', { className: 'card-score' }, App.el('span', { className: 'card-score-value' }, `${state.score}/${state.totalMark}`), App.el('span', { className: 'card-score-label' }, `${state.percentage}%`)));
    card.appendChild(App.el('div', { className: 'card-actions' }, App.el('a', { className: 'btn btn-primary', href: state?.status === 'submitted' ? `result.html?paper=${p.id}` : `test.html?paper=${p.id}` }, state?.status === 'submitted' ? '📊 View Result' : state?.status === 'in_progress' ? '↩ Resume' : '▶ Start')));
    return card;
  }
})();
