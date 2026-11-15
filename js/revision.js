/**
 * js/revision.js
 * Revision Encyclopedia UI controller and vanilla markdown renderer.
 */
(function () {
  'use strict';

  let revisionIndex = null;
  let activeModuleId = null;
  const filterState = {
    category: 'All',
    exam: 'All',
    depth: 'All',
    time: 'All'
  };

  const { App } = window;
  const themeToggle = document.getElementById('theme-toggle');
  App.initTheme();
  if (themeToggle) {
    themeToggle.textContent = App.getTheme() === 'dark' ? '☀️' : '🌙';
    themeToggle.addEventListener('click', () => {
      themeToggle.textContent = App.toggleTheme() === 'dark' ? '☀️' : '🌙';
    });
  }

  // Simple, robust vanilla Markdown-to-HTML parser (no external dependencies)
  function renderMarkdown(md) {
    if (!md) return '';
    let lines = md.split('\n');
    let html = [];
    let inTable = false;
    let tableRows = [];
    let inCode = false;
    let codeBlock = [];

    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];

      // Code blocks
      if (line.trim().startsWith('```')) {
        if (inCode) {
          html.push('<pre><code>' + escapeHtml(codeBlock.join('\n')) + '</code></pre>');
          codeBlock = [];
          inCode = false;
        } else {
          inCode = true;
        }
        continue;
      }
      if (inCode) {
        codeBlock.push(line);
        continue;
      }

      // Tables
      if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
        if (!inTable) {
          inTable = true;
          tableRows = [];
        }
        // Check if delimiter row like | --- | --- |
        if (line.replace(/[\s|:-]/g, '').length === 0) {
          continue; // skip separator row
        }
        let cells = line.split('|').slice(1, -1).map(c => c.trim());
        tableRows.push(cells);
        continue;
      } else if (inTable) {
        // Flush table
        html.push(renderTable(tableRows));
        tableRows = [];
        inTable = false;
      }

      // Headings
      if (line.startsWith('# ')) {
        html.push('<h1>' + formatInline(line.slice(2)) + '</h1>');
      } else if (line.startsWith('## ')) {
        html.push('<h2>' + formatInline(line.slice(3)) + '</h2>');
      } else if (line.startsWith('### ')) {
        html.push('<h3>' + formatInline(line.slice(4)) + '</h3>');
      } else if (line.startsWith('#### ')) {
        html.push('<h4>' + formatInline(line.slice(5)) + '</h4>');
      } else if (line.startsWith('> ')) {
        html.push('<blockquote>' + formatInline(line.slice(2)) + '</blockquote>');
      } else if (line.startsWith('---')) {
        html.push('<hr class="revision-divider">');
      } else if (line.trim().startsWith('* ') || line.trim().startsWith('- ')) {
        let content = line.trim().slice(2);
        html.push('<ul><li>' + formatInline(content) + '</li></ul>');
      } else if (/^\d+\.\s/.test(line.trim())) {
        let content = line.trim().replace(/^\d+\.\s/, '');
        html.push('<ol><li>' + formatInline(content) + '</li></ol>');
      } else if (line.trim().length > 0) {
        html.push('<p>' + formatInline(line) + '</p>');
      }
    }

    if (inTable) {
      html.push(renderTable(tableRows));
    }
    if (inCode) {
      html.push('<pre><code>' + escapeHtml(codeBlock.join('\n')) + '</code></pre>');
    }

    // Clean up adjacent identical lists (combine <ul><li>...</ul> <ul><li>...</ul>)
    let output = html.join('\n')
      .replace(/<\/ul>\s*<ul>/g, '')
      .replace(/<\/ol>\s*<ol>/g, '');

    return output;
  }

  function renderTable(rows) {
    if (!rows || rows.length === 0) return '';
    let out = '<table><thead><tr>';
    let headers = rows[0];
    for (let h of headers) {
      out += '<th>' + formatInline(h) + '</th>';
    }
    out += '</tr></thead><tbody>';
    for (let r = 1; r < rows.length; r++) {
      out += '<tr>';
      for (let c of rows[r]) {
        out += '<td>' + formatInline(c) + '</td>';
      }
      out += '</tr>';
    }
    out += '</tbody></table>';
    return out;
  }

  function formatInline(str) {
    return str
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\$([^\$]+)\$/g, '<code class="math-inline">$1</code>');
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  async function init() {
    try {
      const res = await fetch('data/revision/revision-index.json');
      if (!res.ok) throw new Error('Could not load revision index');
      revisionIndex = await res.json();
      renderSidebar();
      setupSearch();

      // Check URL query param
      const urlParams = new URLSearchParams(window.location.search);
      const modParam = urlParams.get('module');
      if (modParam && revisionIndex.modules.some(m => m.id === modParam)) {
        loadModule(modParam);
      } else if (revisionIndex.modules.length > 0) {
        loadModule(revisionIndex.modules[0].id);
      }
    } catch (err) {
      console.error(err);
      document.getElementById('content-container').innerHTML = `
        <div class="revision-error" style="padding: 30px; text-align: center;">
          <h3>Failed to load revision materials</h3>
          <p>${err.message}</p>
          <p style="color:var(--text-muted); font-size:0.85rem;">Run with a local server (e.g. <code>python3 -m http.server</code>) to enable fetch.</p>
        </div>
      `;
    }
  }

  function moduleMatchesFilters(mod) {
    const categoryFilter = filterState.category;
    const examFilter = filterState.exam;
    const depthFilter = filterState.depth;
    const timeFilter = filterState.time;

    if (categoryFilter !== 'All') {
      const matchCategory =
        (mod.subCategory && mod.subCategory.toLowerCase() === categoryFilter.toLowerCase()) ||
        (mod.category && mod.category.toLowerCase() === categoryFilter.toLowerCase()) ||
        (mod.tags && mod.tags.some(tag => tag.toLowerCase() === categoryFilter.toLowerCase())) ||
        (mod.title && mod.title.toLowerCase().includes(categoryFilter.toLowerCase()));
      if (!matchCategory) return false;
    }

    if (examFilter !== 'All') {
      const exams = Array.isArray(mod.exams) ? mod.exams : [];
      const examMatch = exams.some(exam => exam.toLowerCase() === examFilter.toLowerCase());
      if (!examMatch) return false;
    }

    if (depthFilter !== 'All') {
      const depth = (mod.depth || 'Standard').toLowerCase();
      if (depth !== depthFilter.toLowerCase()) return false;
    }

    if (timeFilter !== 'All') {
      const timeValue = (mod.estimatedTime || mod.estimatedReadMin ? `${mod.estimatedTime || mod.estimatedReadMin} min` : '').toLowerCase();
      const normalized = timeFilter.toLowerCase();
      if (normalized === '10 sec' && !String(mod.estimatedTime || '').toLowerCase().includes('10 sec')) return false;
      if (normalized === '1 min' && !String(mod.estimatedTime || '').toLowerCase().includes('1 min')) return false;
      if (normalized === '5 min' && !String(mod.estimatedTime || '').toLowerCase().includes('5 min')) return false;
      if (normalized === 'deep revision' && !String(mod.depth || '').toLowerCase().includes('deep')) return false;
    }

    return true;
  }

  function getFilteredModules() {
    if (!revisionIndex || !revisionIndex.modules) return [];
    const queryValue = document.getElementById('revision-search')?.value?.toLowerCase().trim() || '';

    return revisionIndex.modules.filter(mod => {
      if (!moduleMatchesFilters(mod)) return false;
      if (!queryValue) return true;

      const haystack = [
        mod.title,
        mod.id,
        mod.file,
        mod.subCategory,
        ...(mod.tags || []),
        ...(mod.exams || []),
        ...(mod.subtopics || [])
      ].join(' ').toLowerCase();

      return haystack.includes(queryValue);
    });
  }

  function renderSidebar(filteredModules = null) {
    const container = document.getElementById('sidebar-categories');
    if (!container || !revisionIndex) return;

    const modulesToRender = filteredModules || getFilteredModules();
    let html = '';

    for (let cat of revisionIndex.categories) {
      let catMods = modulesToRender.filter(m => m.category === cat.id);
      if (catMods.length === 0) continue;

      html += `<div class="category-group">`;
      html += `<div class="category-title">${cat.icon} ${cat.name}</div>`;
      for (let mod of catMods) {
        const isActive = mod.id === activeModuleId ? 'active' : '';
        html += `<a class="module-item ${isActive}" data-id="${mod.id}" title="${mod.title}">
          ${mod.title.replace(/^[^-]+–\s*/, '').replace(/Revision Notes.*$/, '').trim()}
        </a>`;
      }
      html += `</div>`;
    }

    container.innerHTML = html || '<div style="padding: 12px 0; color: var(--text-muted); font-size: 0.85rem;">No modules match the current filters.</div>';

    container.querySelectorAll('.module-item').forEach(el => {
      el.addEventListener('click', () => {
        const modId = el.getAttribute('data-id');
        loadModule(modId);
      });
    });
  }

  function setupSearch() {
    const searchInput = document.getElementById('revision-search');
    if (!searchInput) return;

    const updateFilteredModules = () => {
      renderSidebar(getFilteredModules());
    };

    searchInput.addEventListener('input', updateFilteredModules);

    const categorySelect = document.getElementById('filter-category');
    const examSelect = document.getElementById('filter-exam');
    const depthSelect = document.getElementById('filter-depth');
    const timeSelect = document.getElementById('filter-time');
    const clearButton = document.getElementById('clear-filters');

    [categorySelect, examSelect, depthSelect, timeSelect].forEach(select => {
      if (!select) return;
      select.addEventListener('change', () => {
        filterState.category = document.getElementById('filter-category')?.value || 'All';
        filterState.exam = document.getElementById('filter-exam')?.value || 'All';
        filterState.depth = document.getElementById('filter-depth')?.value || 'All';
        filterState.time = document.getElementById('filter-time')?.value || 'All';
        renderSidebar(getFilteredModules());
      });
    });

    if (clearButton) {
      clearButton.addEventListener('click', () => {
        filterState.category = 'All';
        filterState.exam = 'All';
        filterState.depth = 'All';
        filterState.time = 'All';
        if (categorySelect) categorySelect.value = 'All';
        if (examSelect) examSelect.value = 'All';
        if (depthSelect) depthSelect.value = 'All';
        if (timeSelect) timeSelect.value = 'All';
        searchInput.value = '';
        renderSidebar();
      });
    }
  }

  async function loadModule(modId) {
    activeModuleId = modId;
    const mod = revisionIndex.modules.find(m => m.id === modId);
    if (!mod) return;

    // Update active highlight in sidebar
    document.querySelectorAll('.module-item').forEach(el => {
      el.classList.toggle('active', el.getAttribute('data-id') === modId);
    });

    // Update browser URL query param without full reload
    const url = new URL(window.location);
    url.searchParams.set('module', modId);
    window.history.replaceState({}, '', url);

    const mainContainer = document.getElementById('content-container');
    mainContainer.innerHTML = `<div class="revision-load-state">Loading ${mod.title}…</div>`;

    try {
      const res = await fetch(mod.file);
      if (!res.ok) throw new Error(`Could not load ${mod.file}`);
      const markdown = await res.text();
      const renderedHtml = renderMarkdown(markdown);

      mainContainer.innerHTML = `
        <div class="revision-meta-bar">
          <div>
            <span class="meta-badge">📖 ${mod.estimatedReadMin} min read</span>
            <span class="meta-badge meta-badge--topics">📑 ${mod.subtopicsCount} topics</span>
            <span class="meta-badge meta-badge--words">📝 ${mod.wordCount} words</span>
          </div>
          <a href="${mod.file}" download class="btn btn-outline" style="font-size:0.8rem; padding:4px 10px; text-decoration:none;">
            ⬇️ Download Raw Markdown
          </a>
        </div>
        <div class="rendered-markdown">
          ${renderedHtml}
        </div>
      `;
      // Scroll to top of content
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (err) {
      mainContainer.innerHTML = `<div class="revision-error">Error: ${err.message}</div>`;
    }
  }

  // Auto-init on DOM load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

