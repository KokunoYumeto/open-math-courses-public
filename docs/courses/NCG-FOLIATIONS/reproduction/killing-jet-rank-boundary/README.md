# Figure 11BT.1 — Killing jets and compactness at a rank boundary

Read the complete mathematical arguments in **Section 11BT**, equations
**KJ.1–KJ.8**, the exact warped instance in **Section 11BT.7**, and
**KJC.1–KJC.9**. Real Killing germs give the Hermitian complex jet module;
its full stalk rank and the original normal degree remain distinct.

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

## Exact field, action and quotient

The real bundle and its Hermitian complexification are

\[
J_{\mathbb R}=TT\oplus\mathfrak{so}(TT),\qquad
J=J_{\mathbb R}\otimes_{\mathbb R}\mathbb C,\qquad
\operatorname{rank}_{\mathbb C}J=Q=q(q+1)/2.
\]

Use the real value metric and real Hilbert–Schmidt skew metric, then their
Hermitian complexifications. Local real Killing fields give the original
jets `jX=(X,∇X)`. The actual module is the uniform closure of complex scalar
localizations **`f jX`**, not `j(fX)` and not a claim that fX is Killing.
Its fibres are the complexified full real stalk images with dimension
`k(x)`. It is countably generated and isometrically included as a closed
submodule in `Γ₀(J)`.

Actual original local-isometry transport is exactly

\[
(v,A)\longmapsto(dg\,v,dg\,A\,dg^{-1}),
\]

acting first on the real jets and then complex linearly. The original domains
are preserved. For closed invariant F with open complement U, the coefficient
module quotient has exact norm

\[
\|s+E_KC_0(U)\|=\sup_{x\in F}\|s(x)\|.
\]

It retains ambient germs even when F is singular. This proves no cpc algebra
section or mapping-cone inverse. An adjointable ambient inclusion would give
a continuous finite-bundle projection with trace k(x), impossible at a genuine
rank jump. This excludes an ambient adjoint; it does not exclude the actual
closed Hilbert submodule (KJ.1–KJ.8).

## The actual unit rank-three/six geometry

On `T=(ℝ/ℤ)²×(−2,2)`, use

\[
g=dt^2+e^{2u(t)}(dx^2+dy^2),\qquad
u(t)=\varepsilon e^{-1/(1-t^2)}\ (|t|<1),\quad u=0\ (|t|\ge1),\quad\varepsilon>0.
\]

The original metric is incomplete at the omitted ends ±2. The actual groupoid
is units. Rank is three on the closed `F=𝕋²×[−1,1]` and six on the open
`U=𝕋²×((−2,−1)∪(1,2))`, including the correct boundary rank.
For `E₀=∂t`, `E₁=a^{-1}∂x`, `E₂=a^{-1}∂y`, `a=e^u` and `H=u′`, the exact
real angular Killing-jet columns are

\[
AE_0=H(v_1E_1+v_2E_2),\quad
AE_1=-Hv_1E_0+cE_2,\quad
AE_2=-Hv_2E_0-cE_1.
\]

They span smooth real L; complexify it and its orthogonal complement W.
Their exact Hermitian jet norm is
`(1+2H²)(|v₁|²+|v₂|²)+2|c|²`, including the two skew matrix entries and no
extra a factor in c. The literal entire module is

\[
E_K=\Gamma_0(L)\oplus\Gamma_0(U,W|_U),\qquad J=L\oplus W,
\]

with complex ranks three and three, and W sections extended by zero.
`P_W` is adjointable **on E_K**. It supplies no adjointable ambient inclusion.
This coordinate splitting is the unit example only; arbitrary nonunit
flat-end local isometries can mix radial and angular directions. The intrinsic
whole stalk action still transports correctly (Section 11BT.4).

## Uniform module-compactness failure and exact constants

Take `x₀=(x,y,1)`, `x_n=(x,y,1+1/n)`, `n≥2`, and `f∈C_c(T)` with
`0≤f≤1`, equal to one near x₀. Both W components of a rank-one operator tend
to zero along x_n. Uniform finite-rank approximation therefore proves for
**every** module compact K that
`‖(P_W K P_W)_{x_n}‖→0`. But `fP_W` has identity W block of norm one for all
large n. Its distance to `𝒦(E_K)` is exactly **one**, although every single
fibre is a finite-dimensional compact operator (KJC.1–KJC.4).

The tensor Fock module is
`ℱ=⊕_{r≥0} E_K^{⊗r}` with degree zero `C₀(T)` and positive number operator
`N(ξ_r)=(rξ_r)`. Its **whole** domain is the set where
`Σ_r r²⟨ξ_r,ξ_r⟩` converges in `C₀(T)` norm. Pointwise convergence is not
enough. The bounded diagonal resolvents prove closedness, regularity and
self-adjointness on this domain. Each complete fibre inverse is compact:
finite degree multiplicities `k(x)^r` and the tail norm
`1/(1+(R+1)²)` prove it directly.

Nevertheless the actual degree-one compression is exactly

\[
\iota_1^* f(1+N^2)^{-1}\iota_1=(f/2)1_{E_K}.
\]

Its W block norm stays **1/2** and is noncompact. The full localized inverse
has distance **1/2** from module compacts: this gives the lower bound, while
subtracting its compact vacuum block gives the matching upper bound
(KJC.5–KJC.6). No auxiliary index is assigned to this explicit
positive number operator.

## Whole-domain W repair and retained scope

On the actual U use the exact proper multiplier

\[
\lambda(t)=1+(t^2-1)^{-2}+(4-t^2)^{-2},\qquad
\operatorname{Dom}M_\lambda=\{s\in E_W:\lambda s\in E_W\}.
\]

It tends to infinity at **all four** endpoints `−2,−1,1,2`. The domain keeps
uniform weighted vanishing in the ideal-supported module. Compact sections
are dense; `(λ±i)^{-1}` maps the whole E_W into that domain, giving actual
closed regular self-adjoint resolvent inverses. The bounded multiplier
`λ/(λ±i)` need not vanish at F; it acts on sections which already vanish there.
It supplies no ambient complement.

Properness gives `(λ±i)^{-1}∈C₀(U)`. Finite-rank bundle partitions prove
that these are genuine module compacts. For every ambient `f∈C₀(T)`,

\[
f(1+M_\lambda^2)^{-1}=M_{f|_U/(1+\lambda^2)}\in\mathcal K(E_W).
\]

The coefficient lies in C₀(U), tends uniformly to zero at all four endpoints,
and extends continuously by zero across ±1. This repairs **W compactness
only**, without adjoining missing endpoints or completing the original metric
(KJC.7–KJC.9). It does not construct an index-one auxiliary, holonomy covariance,
a reduced representation, a proper anchored kernel or the final scalar/physical
normal class. The original full inverse Spin-c coefficient, normal degree q,
right Cl₃ and original positive disk remain the prescribed data.
