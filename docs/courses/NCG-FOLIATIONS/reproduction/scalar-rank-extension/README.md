# Figure 11BR.1 — Scalar extension across actual rank jumps

Read the complete mathematical argument in **Section 11BR**, equations
**SE.1–SE.35**. This schematic shows the scalar extension criterion and two
concrete actual unit examples with different outcomes. It does not impose a
universal whole-transfer identity on the original graph-normal problem.

## Portable reproduction

The six reproduction files are `generate.py`, `data.json`, the named SVG
and PNG, `render.cjs` and this `README.md`. Use Python 3 and Node.js. Install
Playwright and its Chromium browser if they are not already available:

```text
npm install playwright
npx playwright install chromium
```

Run the following commands from this directory:

```text
python generate.py
node render.cjs
```

`generate.py` requires only the Python standard library. It deterministically
writes the exact symbolic JSON data and an editable SVG with native text and
vector geometry. Its complete data and drawing primitives are in the script;
edit those and regenerate, or edit the SVG directly for a one-off rendering.
The figure is 900 × 1700 pixels. The SVG coordinates are display coordinates,
not measured Riemannian coordinates or an asserted geometric embedding.

The renderer uses an installed Playwright module and its installed Chromium
by default. Optional `PLAYWRIGHT_MODULE` and `CHROME_EXECUTABLE` environment
variables select an existing module and browser. For example, in PowerShell:

```powershell
$env:PLAYWRIGHT_MODULE = '<path to installed Playwright module>'
$env:CHROME_EXECUTABLE = '<path to installed Chrome or Chromium executable>'
python generate.py
node render.cjs
```

Replace the placeholders with paths on the rendering system. No machine path
is embedded in the generator or renderer. The renderer opens an opaque,
zero-margin HTML page containing the SVG, waits for installed fonts, and checks
every native text bounding box for clipping and pairwise overlap before
writing the PNG. Its stdout records dimensions, label count and check results.
Use `node render.cjs --check-only` to run these checks without replacing the PNG.
Visually inspect the PNG as well. Font substitutions can change text metrics;
rerun the checks on the rendering system rather than assuming identical glyph
metrics. Arial/Helvetica and Cambria Math/Georgia are requested, with native
fallbacks. No font bytes or outlined glyphs are bundled.

The original diagram expression, data, generator, rendering wrapper and
explanatory text are **CC0 1.0**. Installed fonts and external software retain
their actual terms. No external images, paper pages or software bundles are
included. Read the complete mathematical argument in the section and equations
specified at the beginning of this README.

## Exact mathematical content and proof locators

For an actual separable semisplit reduced extension
`0→Iᵣ→Aᵣ→Qᵣ→0`, the obstruction to lifting
`x_I∈KK^q(Iᵣ,ℂ)` is

\[
o(x_I)=\partial_r\otimes_{I_r}x_I\in KK^{q+1}(Q_r,\mathbb C).
\]

Its vanishing is equivalent to existence of an actual scalar lift; the odd
boundary remains on the left of the original degree-q factor. The set of lifts
is an affine translate of the image of the quotient pullback, with no claim
that this pullback is injective. These are SE.1–SE.5, using the actual
separable semisplit ideal/cone proof in KT-KK-14, Theorems 4.1–4.2.

For q=4, the actual point-foliation geometry is
`T={w∈L^{⊗2}:‖w‖<4}`, `F={‖w‖≤1}`, `E=T∖F`, with the originally supplied
curved interior and flat quotient-annulus metric. Its absent outer end is at
finite original distance. Keep that given metric `g`; the figure introduces
no alternative normal metric. The single tautological projection
`e([z])=zz*/(z*z)` pulls back to `e_A=e∘p` and restricts literally to `e_I`
and `e_Q`. The modules are exactly `e_AA²`, `e_II²`, `e_QQ²`. The first two
are multiplier projections, not asserted members of the nonunital algebras.
Multiplication by algebra elements is compact on those finite section
modules, giving the actual even zero-operator bundle cycles (SE.11–SE.14).

`C(F)≃C(S²)` and the split sphere extension together with the actual Bott
inverse products give `KK^5(Q,ℂ)=0`, without UCT (SE.7–SE.10).
For `M=p*L`, the carrier and operator are literal:

\[
H_M=L^2(T,M\otimes S_{\rm inv},d\mathrm{vol}_g)
=e_A L^2(T,S_{\rm inv},d\mathrm{vol}_g)^2,
\]
\[
R=(16-\|w\|^2)^{-1},\quad
\alpha=(1+|dR|_g^2)^{-1/2},\quad
D_M^\alpha=\alpha^{1/2}N_M\alpha^{1/2}.
\]

The **whole** self-adjoint domain is local `H¹` with the weighted expression
in `L²` distributionally, as displayed in SE.17. Positive speed supplies
complete cutoffs for this domain while the original normal metric remains
the symbol datum; no global unweighted `H¹` domain or new missing-end boundary
condition is asserted. The original full inverse central line and final
right `Cl₄` action are retained. Actual section multiplication and creation
connections prove the scalar product SE.18–SE.20. Identity `M` gives the
original untwisted class; tautological `M` gives the selected sign twist,
which is kept globally distinct. Positive ambient disk isotopy gives the
original `b_U=i_*b_V` and the unchanged pairing `+1` (SE.21–SE.22).

For q=3, keep the actual unit groupoid on
`(ℝ/ℤ)²×(−2,2)` with

\[
g=dt^2+e^{2u(t)}(dx^2+dy^2),\qquad
u(t)=\varepsilon e^{-1/(1-t^2)}\ (|t|<1),\quad u=0\ (|t|\ge1),
\quad\varepsilon>0.
\]

The original ends ±2 are absent at finite distance. Rank is three on the
**closed** middle layer, including ±1, and six on both open exteriors
(SE.23–SE.25). All ranks are full actual Killing-germ ranks, not ranks of
chosen global torus vector fields. In the stated six-field order,

\[
H(m,n)=\begin{pmatrix}I_3&N(m,n)\\0&I_3\end{pmatrix},\qquad
N(m,n)=\begin{pmatrix}n&0&0\\-m&0&0\\0&-m&-n\end{pmatrix}.
\]

Scaling only the left exterior translations by √2 gives
`H(m/√2,n/√2)`. Both actual overlap families generate the **one** discrete
label group `Γ₆=ℤ⁴×ℤ`, through `H(a+c/√2,b+d/√2)` and the chart-index
coordinate. Discrete label topology is not the usual dense matrix topology
(SE.26–SE.28).

The **one** auxiliary uses only `(a,b)` and has

\[
\widehat D^+=-\frac{i}{2\pi}\partial_{\theta_1}
+\frac1{2\pi}\partial_{\theta_2},\qquad
V_{(a,b,c,d,j)}=e^{2\pi i(a\theta_1+b\theta_2)}.
\]

Its whole periodic domain is `H¹(X̂)`. It is the sum of one even character
and the full periodic Dirac, so its scalar unit index is one. The left
transitions use ignored `(c,d)` and return `1`. The right family retains all
modes `(k-x)+i(ℓ-y)` until the uniform complement gap is proved. Its remaining
zero-mode clutch map `−x−iy` has positive winding, giving return `1+b=[B]`
(SE.29–SE.31).

With the original ordered inverse normal class and final right `Cl₃`,
`[1_X]d_X=0`, `b d_X=+1`. Both interval inverse classes use increasing t.
For `J₋=(−2,−1)` and `J₊=(1,2)`, the interval classes are
`s_±∈KK¹(ℂ,C₀(J_±))`. Put `ŝ_±=[1_X]⊠s_±∈KK¹(ℂ,I_±)`.
The positive exponential boundary gives **`(ŝ₋,−ŝ₊)`**, retaining the torus
coefficient. Both interval inverse pairings are `+1`. Thus the quotient-unit
scalar readback is `0−1=−1` in `KK⁴(ℂ,ℂ)` (SE.32–SE.35), even while every
original positive three-disk has pairing `+1`. This selected ideal class
cannot extend, but the original untwisted d₃ still extends on this actual
unit geometry. The countertest excludes automatic coherence of normalized
auxiliaries, not existence of that original class.

The full-homotopy scalar readback uses **KT-KK-10 Theorem 2.3 and
Corollary 2.4**, beyond the operator-homotopy picture in KT-KK-07. Actual
simultaneous suspension is **KT-KK-12 Proposition 8.2**, with Proposition 8.1
for coefficient descent. These proof locators are retained in the figure
and data. General nonunit variable-rank scalar choice, excision and geometric
realization remain at their actual stated frontier. Connes is credited for
the historical graph-normal question only; no protected expression is imported.
