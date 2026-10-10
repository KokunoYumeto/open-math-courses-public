# Figure 11BS.1 — Geometric cpc sections at actual rank restrictions

Read the complete mathematical argument in **Section 11BS**, equations
**KE.1–KE.24** and the elementary rotation proof **KEF.1–KEF.4**. The three
routes are sufficient geometric providers with explicit inputs; their
hypotheses are not inferred from reduced norm exactness.

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

## Exact providers and limits

The starting extension has the original reduced kernel and norm from
Section 11BQ/IX.1–IX.12. It is separable. A supplied cpc section then permits
the actual ideal/cone KK equivalence in KT-KK-14 Theorem 4.1 and scalar
boundary exactness in Theorem 4.2. Norm exactness alone does not supply that
section or choose a coherent scalar cycle.

**Route 1 (KE.3–KE.8).** Supply an actual continuous functor
`R:G|W→G|F`, identity on the closed invariant reduction, whose map from every
whole source fibre is a bijection. Supply `0≤χ≤1`, `χ|F=1`, with compact
sets `{g:R(g)∈L,χ(rg)≥δ,χ(sg)≥δ}` for every compact `L` and `δ>0`.
The pullback kernel is
`sqrt(χ(rg))sqrt(χ(sg))f(R(g))`. Endpoint tapers make it a reduced-norm limit
of actual compact kernels, with I-norm error at most `2√δ ‖f‖_I`.
The **entire** regular matrix is exactly

\[
\lambda_x(\sigma(f))=D_xV_x^*\lambda_{\rho(x)}(f)V_xD_x,
\qquad D_x\delta_h=\sqrt{\chi(rh)}\delta_h.
\]

This proves cpc at every matrix size and retains all isotropy. Open-reduction
inclusion has the original reduced norm, verified by exact right-translated
source fibres even if W is not invariant. Compact-word injective shadowing
does not supply this bijective retraction or its common support control.

**Route 2 (KE.9–KE.14).** Supply a **genuine smooth proper global** Lie-isometry
H action on the original, possibly incomplete, manifold. Actual normal slices
have compact stabilizers `K_j`. A cpc slice extension is averaged over the
**compact** `K_j` with normalized Haar measure. Compact slice cutoffs, induction
and a locally finite quotient partition give the equivariant extension S.
Proper transporter compactness and the locally finite enlarged quotient
supports prove its actual `C₀` tails; a formal infinite sum is not enough.
No Haar average over a noncompact H is used.

For an actual germ-faithful countable subgroup `Γ≤H`, all source-fibre bases
are the original `ℓ²(Γ)` bases, including isotropy. Equivariance of the
subprobability measures `μ_x` gives the exact weak operator integral

\[
\lambda_x(\widehat S(q))=\int_F\lambda_z(q)\,d\mu_x(z),
\qquad \mu_x(F)\le1,\quad \mu_x=\delta_x\text{ on }F.
\]

This proves complete positivity and original reduced contractivity. It does
not replace local jets by a global action or add H arrows to the original
Γ groupoid. Nuclearity of the reduced crossed product is not assumed.

**Route 3 (KE.15–KE.17).** Supply the actual product `G=ℋ×J`, with passive
unit parameter `J=(−2,2)` and `B=Cᵣ*(ℋ)`. Its regular norms prove literally
`A=C₀(J,B)` and `Q=C₀(K,B)`. Retain the B-valued input on K and use the
exact convex endpoint formula on every bounded gap `(a,c)`:

\[
(Eb)(t)=\frac{c-t}{c-a}b(a)+\frac{t-a}{c-a}b(c).
\]

An outer left gap uses `(t+2)/(c+2)b(c)` and an outer right gap uses
`(2-t)/(2-a)b(a)`. Empty K gives zero. Positivity and contractivity hold at
all matrix sizes. Endpoint and accumulating-gap continuity and `C₀` tails
are proved. No nuclearity of B or deterministic neighbourhood retraction is
needed.

## The exact incomplete singular example

The parameter set is

\[
K=\{0\}\cup\bigcup_{n\ge1}[a_n,c_n],\quad a_n=2^{-n},\quad c_n=\tfrac54 2^{-n}.
\]

The figure draws the exact rational endpoints for `n=1,…,6` using the affine
display map `t↦160+1000t`; the infinitely many remaining intervals are stated
to accumulate at zero. It is a parameter schematic, not a plotted embedding
of the warped manifold or an approximation to its metric.

On `S²×(−2,2)`, using the original unit round sphere metric, set

\[
u_n(t)=2^{-n}\exp[-1/((t-a_n)(c_n-t))]\quad(a_n<t<c_n),
\qquad u_n=0\text{ otherwise},\quad u=\sum_nu_n,
\]
\[
g=dt^2+e^{2u(t)}g_{S^2}.
\]

The exact derivative estimates make u smooth and flat at zero and all
interval endpoints. The original metric is incomplete at the absent ±2
ends. Curvature and connected first-jet uniqueness give the **full actual**
Killing ranks three on `F=S²×K`, including every boundary and zero, and four
outside F (KE.18–KE.21). No tangent manifold is assigned to F. In particular
there is no neighbourhood retraction onto F near t=0, while Route 3 still
provides the section.

The exact rotations used as original nonunit arrows are

\[
A=\begin{pmatrix}1&0&0\\0&-3/5&-4/5\\0&4/5&-3/5\end{pmatrix},\qquad
B=\begin{pmatrix}-3/5&0&4/5\\0&1&0\\-4/5&0&-3/5\end{pmatrix}.
\]

They come from `(1+2i)/√5` and `(1+2j)/√5`. Section **11BS**,
**KEF.1–KEF.4**, proves that they generate a free dense subgroup of SO(3), by
primitive modulo-five reduced words and irrational-angle circle density.
The public reproduction needs no external dense-free-subgroup theorem or
paid slice link. Each actual arrow `(x,t)→(Ax,t)` or `(x,t)→(Bx,t)` preserves
t and the displayed warped metric. Distinct rotations cannot agree on a
sphere open set, so the actual germ groupoid is the product rotation groupoid.
All original isotropy is retained. The regular-matrix interpolation works
without amenability or nuclearity of B.

KE.22 and KE.23 separately test the two invalid shortcuts: unrelated positive
bisection extensions can produce an indefinite regular matrix, and closure
of local jets can contain a parameter that is no actual local isometry germ.
Neither countertest proves universal nonsemisplitting. These conditional
providers yield excision at their actual hypotheses; they do not infer a
final scalar normal/physical cycle or erase the scalar boundary choice.
