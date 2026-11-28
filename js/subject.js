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
      if (subject.id === 'full-forms') await renderFullFormsFilters(subject, subjectPapers);
      if (subject.id === 'economics-india-world-trade') await renderEconomicsFilters(subject, subjectPapers);
    } catch (err) { App.showError(root, 'Could not load subject', err.message); }
  }
  async function render(subject, papers) { root.innerHTML = ''; root.append(App.el('nav', { className: 'breadcrumb', 'aria-label': 'Breadcrumb' }, App.el('a', { href: 'index.html' }, 'Home'), App.el('span', {}, '›'), App.el('span', {}, subject.title)), App.el('section', { className: 'subject-hero' }, App.el('span', { className: 'subject-icon' }, subject.icon || '📚'), App.el('div', {}, App.el('h1', {}, subject.title), App.el('p', {}, subject.description || 'Practice papers')))); const practicePapers = papers.filter((paper) => paper.contentMode !== 'EXTERNAL_SOURCE' && paper.file); const stats = getStats(practicePapers); root.appendChild(summary([[`${stats.completed}/${practicePapers.length}`, 'Papers completed'], [stats.avg === null ? '—' : `${stats.avg}%`, 'Average score'], [stats.best === null ? '—' : `${stats.best}%`, 'Best score']])); if (subject.id === 'cds') root.appendChild(renderCdsAnalysis(papers)); if (stats.completed) root.appendChild(await weakTopics(practicePapers));   root.appendChild(App.el('div', { className: 'section-header' }, App.el('h2', { className: 'section-title' }, 'Interactive practice papers and PYQ sources'))); if (['cds', 'capf-ac'].includes(subject.id)) root.appendChild(renderCdsFilters(papers)); const grid = App.el('div', { className: 'papers-grid', id: 'cds-papers-grid' }); papers.forEach((p) => grid.appendChild(paperCard(p))); if (!papers.length) grid.appendChild(App.el('p', { className: 'text-muted' }, 'Coming soon.')); root.appendChild(grid); }

  async function renderEconomicsFilters(subject, papers) {
    const indexedQuestions = (await Promise.all(papers.map(async (paper) => {
      const data = await App.loadPaper(paper.file);
      return App.flattenQuestions(data).map((question) => ({ paper, question }));
    }))).flat();
    const topics = [...new Set(indexedQuestions.map(({ question }) => question.topic).filter(Boolean))].sort();
    const difficulties = [...new Set(indexedQuestions.map(({ question }) => question.difficulty).filter(Boolean))].sort();
    const controls = App.el('div', { className: 'full-forms-filters' });
    const topic = App.el('select', { 'aria-label': 'Filter by economics topic' }, new Option('Topic: All', 'all'));
    topics.forEach((value) => topic.add(new Option(value, value)));
    const difficulty = App.el('select', { 'aria-label': 'Filter by difficulty' }, new Option('Difficulty: All', 'all'));
    difficulties.forEach((value) => difficulty.add(new Option(value, value)));
    const search = App.el('input', {
      type: 'search',
      placeholder: 'Search economics question or concept',
      'aria-label': 'Search economics question or concept',
    });
    const status = App.el('p', { className: 'bank-search-status', role: 'status' });
    const results = App.el('div', { className: 'bank-search-results' });
    controls.append(topic, difficulty, search);
    const filter = () => {
      results.innerHTML = '';
      const query = search.value.trim().toLocaleLowerCase();
      const matches = indexedQuestions.filter(({ question }) =>
        (topic.value === 'all' || question.topic === topic.value) &&
        (difficulty.value === 'all' || question.difficulty === difficulty.value) &&
        (!query || App.getQuestionSearchText(question, {}).includes(query))
      );
      status.textContent = matches.length
        ? `Showing ${Math.min(matches.length, 50)} of ${matches.length} matching economics questions.`
        : 'No economics questions match the selected filters.';
      matches.slice(0, 50).forEach(({ paper, question }) => {
        const card = App.el('article', { className: 'bank-search-result' },
          App.el('div', { className: 'bank-search-metadata' }, `${question.topic} · ${question.subtopic} · ${question.difficulty}`),
          App.el('div', { className: 'bank-search-question' }, App.renderBilingualText(question.q)),
          App.el('a', {
            className: 'btn btn-primary btn-sm',
            href: `test.html?paper=${encodeURIComponent(paper.id)}&question=${question.globalIndex}`,
          }, 'Open question')
        );
        results.appendChild(card);
      });
    };
    controls.addEventListener('change', filter);
    search.addEventListener('input', filter);
    const section = App.el('section', { className: 'glass full-forms-browser', 'aria-labelledby': 'economics-browser-title' },
      App.el('h2', { id: 'economics-browser-title', className: 'section-title' }, 'Browse Economics'),
      controls,
      status,
      results
    );
    const paperHeader = root.querySelector('.section-header');
    root.insertBefore(section, paperHeader || null);
    filter();
  }

  async function renderFullFormsFilters(subject, papers) {
    const indexedQuestions = (await Promise.all(papers.map(async (paper) => {
      const data = await App.loadPaper(paper.file);
      return App.flattenQuestions(data).map((question) => ({ paper, question }));
    }))).flat();

    const sectors = [...new Set(indexedQuestions.map(({ question }) => question.sector).filter(Boolean))].sort();
    const difficulties = [...new Set(indexedQuestions.map(({ question }) => question.difficulty).filter(Boolean))].sort();
    const controls = App.el('div', { className: 'full-forms-filters' });
    const sector = App.el('select', { 'aria-label': 'Filter by sector' }, new Option('Sector: All', 'all'));
    sectors.forEach((value) => sector.add(new Option(value, value)));
    const difficulty = App.el('select', { 'aria-label': 'Filter by difficulty' }, new Option('Difficulty: All', 'all'));
    difficulties.forEach((value) => difficulty.add(new Option(value, value)));
    const search = App.el('input', {
      id: 'full-forms-search',
      type: 'search',
      placeholder: 'Search abbreviation or full form',
      autocomplete: 'off',
      'aria-label': 'Search FULL FORMS abbreviation or full form',
    });
    const status = App.el('p', { className: 'bank-search-status', role: 'status' });
    const results = App.el('div', { className: 'bank-search-results' });
    controls.append(sector, difficulty, search);

    const filter = () => {
      const query = search.value.trim().toLocaleLowerCase();
      results.innerHTML = '';
      const matches = indexedQuestions.filter(({ question }) =>
        (sector.value === 'all' || question.sector === sector.value) &&
        (difficulty.value === 'all' || question.difficulty === difficulty.value) &&
        (!query || App.getQuestionSearchText(question, {}).includes(query))
      );
      status.textContent = matches.length
        ? `Showing ${Math.min(matches.length, 50)} of ${matches.length} matching full-form questions.`
        : 'No full-form questions match the selected filters.';
      matches.slice(0, 50).forEach(({ paper, question }) => {
        const card = App.el('article', { className: 'bank-search-result' });
        card.append(
          App.el('div', { className: 'bank-search-metadata' },
            `${question.sector} · ${question.subsector} · ${question.difficulty}`
          ),
          App.el('div', { className: 'bank-search-question' }, App.renderBilingualText(question.q)),
          App.el('div', { className: 'bank-search-options' },
            ...question.options.map((option, index) => App.el(
              'div',
              { className: `bank-search-option${index === question.answer ? ' correct' : ''}` },
              `${String.fromCharCode(65 + index)}. `,
              App.renderBilingualText(option)
            ))
          ),
          App.el('a', {
            className: 'btn btn-primary btn-sm',
            href: `test.html?paper=${encodeURIComponent(paper.id)}&question=${question.globalIndex}`,
          }, 'Open question')
        );
        results.appendChild(card);
      });
    };
    controls.addEventListener('change', filter);
    search.addEventListener('input', filter);

    const searchSection = App.el('section', {
      className: 'glass full-forms-browser',
      'aria-labelledby': 'full-forms-browser-title',
    },
      App.el('h2', { id: 'full-forms-browser-title', className: 'section-title' }, 'Browse FULL FORMS'),
      controls,
      status,
      results
    );
    const paperHeader = root.querySelector('.section-header');
    root.insertBefore(searchSection, paperHeader || null);
    filter();
  }

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
    const practicePapers = papers.filter((paper) => paper.contentMode !== 'EXTERNAL_SOURCE');
    const practiceQuestions = practicePapers.reduce((count, paper) => count + (paper.questionCount || 0), 0);
    const box = App.el('section', { className: 'glass weak-topics' },
      App.el('h2', { className: 'section-title' }, 'CDS PYQ Sources and Interactive Practice'),
      App.el('p', {}, `${realSources} official subject-paper source links are registered across four sessions. The PDFs open on the UPSC site; question text has not been copied into this site and cannot be attempted in the in-app timer or scoring engine.`)
    );
    box.append(
      App.el('p', {}, 'Each REAL PYQ record links to the original question-paper PDF published by UPSC. No answer key or question text is represented as internal content.'),
      App.el('h3', {}, 'In-app analysis status'),
      App.el('p', {}, 'No real-PYQ questions have been imported, so topic frequencies, difficulty trends and 10-year recurrence statistics are not yet available. Original practice papers below are interactive and independently scored.'),
      App.el('p', { className: 'text-muted' }, `Source-linked subject papers: ${realSources} · Imported real-PYQ questions: 0 · Interactive practice questions: ${practiceQuestions}`)
    );
    return box;
  }
  function renderCdsFilters(papers) {
    const controls = App.el('div', { className: 'cds-filters' });
    const type = App.el('select', { 'aria-label': 'Filter by paper type' },
      new Option('Type: All', 'all')
    );
    const typeLabels = { REAL_PYQ: 'REAL PYQ', PREDICTED: 'PREDICTED', PRACTICE: 'PRACTICE' };
    [...new Set(papers.map((paper) => paper.paperType).filter(Boolean))]
      .sort()
      .forEach((value) => type.add(new Option(typeLabels[value] || value, value)));
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
        App.el('span', { className: 'meta-chip' }, p.paperType === 'REAL_PYQ' && p.sourceAuthority === 'UPSC' ? 'REAL UPSC PAPER' : p.paperType || 'Practice'),
        ...(p.durationMin ? [App.el('span', { className: 'meta-chip' }, `⏱ ${p.durationMin} min`)] : []),
        ...(p.paperSubject ? [App.el('span', { className: 'meta-chip' }, p.paperSubject)] : []),
        ...(p.contentMode === 'EXTERNAL_SOURCE' ? [App.el('span', { className: 'meta-chip' }, 'External source · not in-app scored')] : []),
        ...(p.contentMode !== 'EXTERNAL_SOURCE' ? [App.el('span', { className: 'meta-chip' }, `+${p.correctMark} / −${p.negativeMark}`)] : [])
      )
    );
    if (p.contentMode === 'EXTERNAL_SOURCE') {
      card.appendChild(App.el('p', { className: 'text-muted' }, `Source: ${p.source}`));
      card.appendChild(App.el('p', { className: 'text-muted' }, 'Interactive attempt is unavailable: source questions have not been independently transcribed and verified for this site.'));
      card.appendChild(App.el('div', { className: 'card-actions' },
        App.el('a', {
          className: 'btn btn-primary',
          href: p.sourceUrl,
          target: '_blank',
          rel: 'noopener noreferrer'
        }, 'Open Original Paper')
      ));
      card.appendChild(App.el('p', { className: 'text-muted' }, p.verificationStatus));
      return card;
    }
    const state = App.getPaperState(p.id);
    if (state?.status === 'submitted') card.appendChild(App.el('div', { className: 'card-score' }, App.el('span', { className: 'card-score-value' }, `${state.score}/${state.totalMark}`), App.el('span', { className: 'card-score-label' }, `${state.percentage}%`)));
    const actions = App.el('div', { className: 'card-actions' },
      App.el('a', {
        className: 'btn btn-primary',
        href: state?.status === 'submitted' ? `result.html?paper=${p.id}` : `test.html?paper=${p.id}`,
      }, state?.status === 'submitted'
        ? '📊 View Result'
        : state?.status === 'in_progress'
          ? '↩ Resume'
          : p.exam === 'GATE CSE' ? 'Attempt Interactive Test' : '▶ Start')
    );
    if (p.patternUrl && p.syllabusUrl) {
      actions.append(
        App.el('a', { className: 'btn btn-secondary', href: p.patternUrl, target: '_blank', rel: 'noopener noreferrer' }, 'Official Pattern'),
        App.el('a', { className: 'btn btn-secondary', href: p.syllabusUrl, target: '_blank', rel: 'noopener noreferrer' }, 'Official Syllabus')
      );
      card.appendChild(App.el('p', { className: 'text-muted' }, p.sourceNote));
    }
    card.appendChild(actions);
    return card;
  }
})();
