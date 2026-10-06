/* GPT-6.1 Sol (OpenAI), Codex, Ultra. Original course reader correction, CC0. */
(() => {
  'use strict';
  const ready = window.MathJax?.startup?.promise || Promise.resolve();
  ready.then(() => {
    const article = document.querySelector('article.lesson');
    if (!article) return;
    const expressions = [...article.querySelectorAll('.math:not(.math-display)')];
    function classify() {
      for (const expression of expressions) {
        const math = expression.querySelector('mjx-container');
        if (!math) continue;
        const block = expression.closest('p,li,td,th,dd,dt,h2,h3,h4,blockquote');
        const available = block?.clientWidth || article.clientWidth;
        const wide = math.getBoundingClientRect().width > available - 8;
        expression.classList.toggle('ag-as-wide-inline', wide);
        if (wide) {
          expression.tabIndex = 0;
          expression.setAttribute('aria-label', 'Scrollable mathematical expression');
        } else {
          expression.removeAttribute('tabindex');
          expression.removeAttribute('aria-label');
        }
      }
      document.documentElement.dataset.agAsInlineMathReady = 'true';
    }
    classify();
    let previousWidth = article.clientWidth;
    const observer = new ResizeObserver(() => {
      const width = article.clientWidth;
      if (width === previousWidth) return;
      previousWidth = width;
      requestAnimationFrame(classify);
    });
    observer.observe(article);
  }).catch(error => console.error('Course formula layout failed:', error));
})();
