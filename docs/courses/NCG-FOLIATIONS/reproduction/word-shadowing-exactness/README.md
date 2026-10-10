# Actual compact-word shadowing and reduced rank exactness

This portable original schematic accompanies Section 11BQ, Theorem 11BQ.1,
equations IX.1–IX.12 and Exercises 303–305. The figure explains the mechanism;
the complete mathematical argument remains in
the complete proof in Section11BQ. It is not replaced by the diagram.

The diagram's original expression, generator, symbolic data and rendering
wrapper are dedicated under **CC0 1.0**. This package includes no external
image, source-paper page, font bytes, outlined glyphs or software bundle.
Installed fonts and external software retain their own terms.

## Files and reproduction

- `generate.py`: deterministic Python standard-library generator.
- `data.json`: exact symbolic hypotheses, claims, roles, proof locators and
  integer display coordinates. The display coordinates are not metric values.
- `word-shadowing-exactness.svg`: editable text and vector geometry, 900 × 1400.
- `render.cjs`: portable browser rendering and native SVG label-bound checks.
- `word-shadowing-exactness.png`: inspected opaque PNG render at 900 × 1400.

Run `python generate.py` from this directory. Run `node render.cjs` with a
locally installed Playwright and its Chromium, or select the installed module
and browser with `PLAYWRIGHT_MODULE` and `CHROME_EXECUTABLE` environment
variables. The wrapper contains no machine-specific paths. It emits the PNG
only after checking every native text bounding box for clipping and pairwise
overlap. Actual font availability can change text metrics; rerun those checks
when rendering on another system. No font embedding is required.

## Exact notation and caption

The source report's original word base `x` is named **y₀** here, and its
nearby closed-set point `z` is named **x₀**. Thus

\[
x_0\in F,\qquad d(y_0,x_0)<\delta<\varepsilon/2,
\quad y_k=g_k\cdots g_1(y_0),\quad x_k=g_k\cdots g_1(x_0).
\]

The radius is chosen once for one fixed compact symmetric test `C`, including
the compact supports of the finitely many bisection summands and their
inverses. It is independent of word length, the regular source fibre and the
chosen component. Each prefix endpoint of the original tested word lies in
`K=s(C)∪r(C)`. All drawn circles use the same display radius. Their pixel
radius and the vertical pixel displacement illustrate the strict inequality
`δ<ε/2`; they do not assign numerical values to either parameter.

**Figure 11BQ.1 caption.** Schematic geometry with exact proof content:
one compact `C` and one original normal-ball radius for every word length
(IX.2–IX.5); arbitrary source-fibre coset right translation and unchanged
cutoff weights (IX.6–IX.8 and Section 11BQ); the full infinite-matrix Schur
estimate, exact quotient and actual rank restriction (IX.7–IX.12). Solid
arrows evaluate the same original actual word representatives. Dashed
comparisons are short original normal geodesics and their isometric images,
without arrowheads; they are not invented holonomy arrows. The green badge
marks membership in the closed invariant set `F` and asserts no shape or
manifold structure for it. The complete argument remains in the source
report and Section 11BQ.

## Independent edge and component check

Write `f=Σᵢfᵢ`, with each summand supported compactly inside a buffered
actual bisection. Its source coefficient `aᵢ` has continuous zero extension,
so on the common compact ambient neighbourhood

\[
|a_i(p)-a_i(p')|\le\omega(\delta)
\quad\text{when }d(p,p')\le\delta.
\]

Let `W` be any supported-word component based at `y₀`, let `J` denote actual
germ evaluation at `x₀`, and let `V e_w=e_{Jw}`. For an extra shadow
`i`-edge between the image vertices `Jw` and `Jv`, put
`p=r(w)` and `p′=r(Jw)`. The geometric estimate gives
`d(p,p′)≤δ`. There are two cases.

1. **The original coefficient is nonzero.** The buffered original arrow
   `gᵢ(p)` belongs to the fixed compact test. The actual word
   `gᵢ(p)w` is in the **full** word set `Wᵧ₀(C)`, whether or not it was
   already known to lie in the selected component `W`. The common buffered
   representative evaluates it to the proposed shadow target:
   `J(gᵢ(p)w)=Jv`. Injectivity on the full word set, proved using connected
   normal-ball uniqueness, gives `gᵢ(p)w=v`. Since `v∈W`, this establishes
   the original compressed edge as well. The coefficient difference is at
   most `ω(δ)`.
2. **The original coefficient is zero.** The shadow coefficient has absolute
   value at most `ω(δ)`. No original arrow at `p` is needed or asserted.
   This also covers `p` outside the bisection domain because the coefficient
   is extended continuously by zero. Missing support edges and missing
   actual arrows are not identified.

A nonzero original supported edge always has its actual shadow arrow on
the common ball. If its shadow coefficient is zero, its original coefficient
is at most `ω(δ)` by the same modulus. Each bisection gives at most one
matrix entry per row and per column in either compression. The difference
of the two matrices therefore has at most two possible positions per
`i` in each row and column, each controlled by `ω(δ)`. Thus the conservative
bound `2mω(δ)` is valid for both absolute row and column sums on the
**entire infinite** component. The Schur estimate gives IX.7, without a
finite-word truncation.

For an arbitrary actual vertex `h:s(h)→y₀`, right translation
`h′↦h′h⁻¹` is an exact onto basis isometry from its supported component to
`W⊂Wᵧ₀(C)`. It preserves endpoints and intertwines the original component
operator with `D Aᵧ₀ D`, where `D e_w=b(rw)e_w` and `0≤D≤1`.
Only the resulting compact-support words are evaluated at `x₀`. The domain
of `h` is not extended. The original diagonal weights are transported by
`V` unchanged: `VDV*` is their diagonal contraction on the image, zero on
the orthogonal complement. They are not re-evaluated at the shadow
endpoints. Consequently no continuity or derivative bound for the shrinking
cutoff `b` is required in this comparison.

Invariance gives `J(W)⊂(G|F)ₓ₀`. Compression and the two diagonal
contractions therefore give

\[
\|D A_{y_0}D\|\le\|f|_{G|F}\|_r+2m\omega(\delta).
\]

Take the supremum over every component of every regular fibre, use
`2mω(δ)<η`, and use `f-bfb∈I_U=Cᵣ*(G|U)`. Contractive restriction gives
the reverse quotient inequality, proving the exact IX.10 identity
`‖f+I_U‖=‖f|_(G|F)‖ᵣ`. The rank sequence in the figure is IX.12 for the
actual invariant open sets `Uⱼ={x:k(x)≥j}`, with `U₀=T`,
`U_(Q+1)=∅` and `Q=q(q+1)/2`. Its closed strata need not be manifolds.

**The edge argument.** The independence of
the full-word injection from the selected component and the unchanged
transport of `D` are made explicit here. The original incomplete metric,
actual isotropy, full inverse Spin-c coefficient, original degree `q`,
original disk and graph carrier remain prescribed. Norm exactness does not
construct or identify a scalar or physical graph class, disk pairing,
semisplit KK extension or compatibility of independently chosen transfers.

## Human-source credit

[Alain Connes, *A survey of foliations and operator algebras*](https://alainconnes.org/wp-content/uploads/foliationsfine.pdf)
is credited for the historical graph-normal question only. This diagram
and its proof expression are independently authored.

[Kevin Aguyar Brix, Toke Meier Carlsen and Aidan Sims, *Some results regarding the ideal structure of C*-algebras of étale groupoids*, Section 2, equation (2.1)](https://eprints.gla.ac.uk/316431/2/316431.pdf)
is credited for the established inner-exactness terminology only. The figure
does not import a proof, picture or wording from that paper.
