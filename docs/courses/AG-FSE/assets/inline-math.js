/* CC0 1.0. Keep scrolling only for inline formulas wider than their text block. */
(() => {
  const inline = () => [...document.querySelectorAll('article.lesson .math:not(.math-display)')];
  const fit = () => {
    for (const expression of inline()) {
      expression.classList.remove('math-wide');
      const block = expression.closest('p, li, td, th, h2, h3, h4, blockquote')
        || expression.closest('article.lesson');
      const width = block.getBoundingClientRect().width;
      const formula = expression.querySelector('mjx-container');
      const natural = formula
        ? Math.max(formula.getBoundingClientRect().width, formula.scrollWidth)
        : expression.scrollWidth;
      expression.classList.toggle('math-wide', natural > width + 1);
    }
  };
  const start = async () => {
    if (window.MathJax?.startup?.promise) await window.MathJax.startup.promise;
    if (document.fonts?.ready) await document.fonts.ready;
    fit();
    let frame;
    addEventListener('resize', () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(fit);
    }, { passive: true });
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start, { once: true });
  } else {
    start();
  }
})();
