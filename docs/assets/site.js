/* Catalogue filters. Progressive enhancement: without JavaScript every course is listed on its
   subject shelf, and the subject chips are links to those shelves. */
(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const cards = [...document.querySelectorAll('.course-card')];
  if (!cards.length) return;
  const shelves = [...document.querySelectorAll('.shelf')];
  const subjectChips = [...document.querySelectorAll('.chip[data-subject]')];
  const bandChips = [...document.querySelectorAll('.chip[data-take-first]')];
  const search = document.getElementById('q');
  const count = document.getElementById('result-count');
  const empty = document.getElementById('empty-state');
  const reset = document.getElementById('reset-filters');
  const courseTotal = cards.filter(card => card.dataset.pointer !== '1').length;
  const normalize = value => value.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const subjects = new Set(subjectChips.map(chip => chip.dataset.subject));
  const bands = new Set(bandChips.map(chip => chip.dataset.takeFirst));
  const state = { subject: 'all', band: 'any', q: '' };

  const params = new URLSearchParams(window.location.search);
  if (subjects.has(params.get('subject'))) state.subject = params.get('subject');
  if (bands.has(params.get('take_first'))) state.band = params.get('take_first');
  if (params.get('q')) state.q = params.get('q').slice(0, 200);
  if (search) search.value = state.q;

  function syncUrl() {
    const next = new URLSearchParams();
    if (state.subject !== 'all') next.set('subject', state.subject);
    if (state.band !== 'any') next.set('take_first', state.band);
    if (state.q) next.set('q', state.q);
    const query = next.toString();
    const url = window.location.pathname + (query ? '?' + query : '') + window.location.hash;
    try { window.history.replaceState(null, '', url); } catch (error) { /* some local previews refuse this */ }
  }

  function apply() {
    const words = normalize(state.q).split(/\s+/).filter(Boolean);
    let shownCourses = 0;
    let shownCards = 0;
    for (const card of cards) {
      const pointer = card.dataset.pointer === '1';
      const visible = (state.subject === 'all' || card.dataset.subject === state.subject)
        && (state.band === 'any' || (!pointer && card.dataset.takeFirst === state.band))
        && words.every(word => normalize(card.dataset.search || '').includes(word));
      card.hidden = !visible;
      if (visible) {
        shownCards += 1;
        if (!pointer) shownCourses += 1;
      }
    }
    for (const shelf of shelves) {
      shelf.hidden = !shelf.querySelector('.course-card:not([hidden])');
    }
    for (const chip of subjectChips) chip.setAttribute('aria-pressed', String(chip.dataset.subject === state.subject));
    for (const chip of bandChips) chip.setAttribute('aria-pressed', String(chip.dataset.takeFirst === state.band));
    if (count) count.textContent = `${shownCourses} of ${courseTotal} courses shown`;
    if (empty) empty.hidden = shownCards !== 0;
    syncUrl();
  }

  for (const chip of subjectChips) {
    chip.setAttribute('role', 'button');
    chip.addEventListener('click', event => {
      event.preventDefault();
      state.subject = chip.dataset.subject;
      apply();
    });
    chip.addEventListener('keydown', event => {
      if (event.key === ' ') { event.preventDefault(); chip.click(); }
    });
  }
  for (const chip of bandChips) {
    chip.addEventListener('click', () => {
      state.band = chip.dataset.takeFirst;
      apply();
    });
  }
  if (search) {
    search.addEventListener('input', () => {
      state.q = search.value.trim().slice(0, 200);
      apply();
    });
  }
  if (reset) {
    reset.addEventListener('click', () => {
      state.subject = 'all';
      state.band = 'any';
      state.q = '';
      if (search) search.value = '';
      apply();
    });
  }
  apply();
})();
