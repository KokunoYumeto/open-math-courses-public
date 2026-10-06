/* DG-CHAR reader support. Independently authored; CC0-1.0.
 * Measure the typeset inline formula after fonts load, and again on resize.
 * The source TeX and every mathematical symbol remain unchanged.
 */
(function () {
  "use strict";
  var scheduled = false;
  function sizeInlineMath() {
    scheduled = false;
    document.querySelectorAll(".lesson .math:not(.math-display)").forEach(function (formula) {
      formula.style.width = "";
      var typeset = formula.querySelector("mjx-container");
      var width = Math.max(formula.scrollWidth,
        typeset ? typeset.getBoundingClientRect().width : 0);
      formula.style.width = (Math.ceil(width) + 1) + "px";
    });
  }
  function scheduleSizing() {
    if (!scheduled) {
      scheduled = true;
      window.requestAnimationFrame(sizeInlineMath);
    }
  }
  window.addEventListener("load", function () {
    var ready = window.MathJax && window.MathJax.startup && window.MathJax.startup.promise;
    Promise.resolve(ready).then(function () {
      return document.fonts ? document.fonts.ready : undefined;
    }).then(function () {
      sizeInlineMath();
      window.addEventListener("resize", scheduleSizing);
      if (document.fonts && document.fonts.addEventListener) {
        document.fonts.addEventListener("loadingdone", scheduleSizing);
      }
    });
  });
}());
