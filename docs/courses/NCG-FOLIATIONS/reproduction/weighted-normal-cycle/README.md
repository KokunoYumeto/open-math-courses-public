# Positive completeness weight and the original normal phase

Original mathematical diagram and generator expression: CC0 1.0, to the extent of rights held. No external mathematical image, source text, font bytes or SVG glyph outlines are incorporated. SVG text uses the viewer's installed fonts. Separately installed rendering software and fonts retain their own terms.

Run `python -B generate.py --output-dir generated` using Python 3. The standard-library program generates `weighted-normal-cycle.svg` and `data.json`, retaining the exact formula and numerical samples. Run `node render.cjs generated` using an existing Playwright/Chromium installation to render the PNG. Optional PLAYWRIGHT_MODULE and CHROME_EXECUTABLE environment variables select those existing installations; no runtime or font is bundled.

Proof: Theorem 11BM.1, WN.1–WN.11, WB.1–WB.6 and Exercises 291–293. The numerical curve does not prove self-adjointness or completeness: those follow from the exhaustion, exact cutoff bounds and full domain argument. Original q-dimensional normal data, full inverse coefficient, Clifford order and positive disk pairing are retained. The figure makes no reduced physical graph assertion. Historical context: Connes, A survey of foliations and operator algebras, Section 8; full inverse conventions: Theorem 7.17.
