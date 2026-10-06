# Normal extension and complete tangential action

Original source: AN03-U034, *Global boundary operators, compressed wave fronts, and normal extension*, written by Codex, September 2026, CC0. Current complete proof connections and clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0. All original mathematical displays in the selected sections remain unchanged.

Use \(D=-i\partial\), forward Fourier exponential \(e^{-ix\cdot\xi}\) and inverse factor \((2\pi)^{-n}\), on smooth Hausdorff second-countable manifolds with boundary and finite-rank bundles. The [global geometry](../20261005-global-boundary-operators/stretched-kernels-and-compressed-geometry.md) and [complete operator calculus](../20261005-global-boundary-operators/global-boundary-operator-calculus.md) prove (GL1)–(GL24), (GC1)–(GC14), (GA1)–(GA5), (GD13)–(GD14) and (GW1)–(GW5), including exact proper support, residual receiving and ordered elliptic parametrices. The [conormal test spaces](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md), [dual distributions and intrinsic jets](../20261005-conormal-test-foundations/dual-conormal-distributions-and-jets.md), and [full conormal intersection proof](../20261005-conormal-test-foundations/conormal-duality-implies-smoothness.md) supply (C1)–(C17), (GD1)–(GD12), and (SP1)–(SP15). A smooth boundary function is represented by its zero extension when paired with ambient supported distributions.

The exact [local boundary action](../20261005-local-boundary-calculus/boundary-tests-and-lacunary-symbols.md) and [distributional calculus](../20261005-local-boundary-calculus/boundary-adjoints-composition-and-distributions.md) supply all commutators, boundary jets and weak approximation, including distributions supported entirely on the boundary. The [ordinary wave-front proof](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md) and [conic parametrices](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md) give the interior and tangential boundary calculus. The [locally finite partition PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md), [Fourier](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), and [measure proofs](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) supply the remaining foundations. Source credit: the approved Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid; the mathematical arguments and exact prerequisites are included.

## Exact extension, topology and pairing conventions

The [compressed wave-front companion](compressed-wavefront-and-differential-action.md) proves (GW6)–(GW16), the compact-localization convention and the common finite-sum tester. The [normal-extension proof](../20261005-normal-extension/normal-extension-and-boundary-defect.md) proves (GE1)–(GE20), the complete boundary defect, existence and uniqueness among all supported extensions of the weighted equation. Its first theorem permits arbitrary finite tangential orders on a fixed product collar; the invariant wave-front theorem here assumes total differential order \(m\) and an invertible principal normal coefficient.

All sources and solutions in ambient equations are their actual supported representatives. Extendibility means that the interior distribution has some ambient distribution extension across the boundary. In (GT6), \({}^{\mathrm t}\) is the bilinear transpose on the dual density. If one instead uses Hermitian half-density pairings, complex conjugation of the test identifies this formula with the adjoint convention (GD13); the resulting operator on \(u\) is identical.

For periodic Fourier reconstruction use the complete Fejér and differentiated-series proof in [Section 13.2 of the scalar-kernel companion](../20261005-restored-analytic-composition/scalar-kernels-and-strong-topology.md). For tangential kernel amplitudes and every finite remainder use [O4 of the ordinary calculus](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md), with the normal variable as a parameter. The original half-space extension and all its finite seminorm estimates are in Section 3 of the local boundary test component.

### 5.6. The noncharacteristic boundary wave-front class

Write \(\widetilde T^*X\) for the compressed cotangent bundle of
(GL11)–(GL18), and embed \(T^*\partial X\setminus0\) as its
boundary covectors with zero normal compressed component. Define
the exact class
\[
 \mathcal N(X)
  :=\{v\in\mathcal A'(X):
       \operatorname{WF}_b(v)|_{\partial X}
       \subset T^*\partial X\setminus0\}.
 \tag{GE21}
\]
This is a condition on the already-defined wave-front set (GW6),
not a replacement for the dual conormal requirement.

Let \(P\) be a smooth ordinary differential operator of total
order \(m\ge1\) whose boundary is noncharacteristic, and let an
extendible interior distribution \(u\) solve \(Pu=f\) with
\(f\in\mathcal N(X)\). In one product chart retain the complete
normal expansion
\[
 P=a_m(x)D_n^m+
       \sum_{j=0}^{m-1}a_j(x,D')D_n^j,
 \qquad a_m(x',0)\text{ invertible}.
 \tag{GE22}
\]
Shrinking the chart makes \(a_m(x)\) invertible throughout it.
Multiplying the equation on the *left* by its inverse gives the
normal-monic operator
\(P'=a_m^{-1}P\) and source \(f'=a_m^{-1}f\).
The order of matrix multiplication is retained. Smooth
multiplication preserves \(\mathcal A'\) by (GD13) and preserves
the boundary wave-front condition by (GW12); thus
\(f'\in\mathcal N\). Sections 5.3–5.5 give the unique local
\(U\in\mathcal A'\) with
\[
 x_n^m(P'U-f')=0,
 \qquad x_n^m(PU-f)=0.
 \tag{GE23}
\]
The second equality follows by multiplying the first on the left
by \(a_m\), which commutes with the scalar \(x_n^m\). In (GE23)
the composition \(x_n^mP\) is also its actual totally
characteristic differential action on supported distributions:
the original coefficients, their product order, and the raw
ambient normal derivatives agree with (GD13) after transposition.

The full noncharacteristic estimate (GW16), with the original
defining function \(\phi=x_n\) in this chart, applies to this
\(U\):
\[
 \operatorname{WF}_b(U)|_{\partial X}
 \subset
 \operatorname{WF}_b(x_n^mPU)|_{\partial X}
       \cup(T^*\partial X\setminus0)
 =\operatorname{WF}_b(x_n^mf)|_{\partial X}
       \cup(T^*\partial X\setminus0).
 \tag{GE24}
\]
Multiplication by \(x_n^m\) is a proper order-zero
totally characteristic operator after localization. The full
forward inclusion (GW12), rather than an unsupported assertion
about its zero set, gives
\[
 \operatorname{WF}_b(x_n^mf)|_{\partial X}
       \subset\operatorname{WF}_b(f)|_{\partial X}
       \subset T^*\partial X\setminus0.
 \tag{GE25}
\]
Equations (GE24)–(GE25) prove \(U\in\mathcal N\).
On overlapping boundary charts, two such local extensions have the
same interior restriction and belong to \(\mathcal A'\), so (GD4)
makes them equal. The product coordinate changes and bundle maps
preserve \(\mathcal A'\) by the full conormal coordinate and dual-pairing proofs (C2), (C15), (GD3)–(GD4) and the compressed wave-front
condition by (GL11)–(GL18) and (GW6). The local extensions therefore
glue to a global \(U\in\mathcal N(X)\), uniquely determined by the
interior \(u\):
\[
 Pu=f\text{ in }X^\circ,\quad f\in\mathcal N(X),\quad
 \partial X\text{ noncharacteristic for }P
 \quad\Longrightarrow\quad
 \exists!\,U\in\mathcal N(X),\ U|_{X^\circ}=u.
 \tag{GE26}
\]
The uniqueness in (GE26) is also immediate from (GD4). Its
existence uses the actual weighted equation (GE23); an arbitrary
ambient extension would not supply the conclusion.
For an order-zero \(P=a_0(x)\) invertible at the boundary, local
inversion gives \(U=a_0^{-1}f\in\mathcal N\) by (GD13) and
(GW12), with the same interior restriction and uniqueness by
(GD4). Thus (GE26) also covers this endpoint without applying
the positive-order companion construction to a zero-dimensional
system.

## 6. Tangential action at the boundary

### 6.1. The actual tangential action and the conormal topology

Let \(b(x',t,\xi')\in S^d\), \(d\in\mathbb R\), smooth down to
\(t=0\), with its original full family of tangential symbol
seminorms. Its left quantization, with the same Fourier convention
as (GL13), is
\[
 (B_bv)(x',t)=(2\pi)^{-(n-1)}
     \int e^{i(x'-y')\cdot\xi'}b(x',t,\xi')v(y',t)
                  \,dy'\,d\xi'.
 \tag{GT1}
\]
For \(n=1\), the tangential dimension is zero and (GT1) is smooth
multiplication. Insert the actual proper-support kernel cutoff of
\(B_b\) in (GT1) when needed. It maps compact smooth tests to
compact smooth tests, including in the normal variable. Its
transpose \(B_b^{\mathrm t}\) is another properly supported
tangential operator of order \(d\), with smooth \(t\)-dependent
coefficients; this follows directly by transposing the kernel and
Taylor-expanding \(b(y',t,\xi')\) in \(y'-x'\), retaining the exact
far kernel as a tangential smoothing term. Thus (GT1) acts by
transposition on every distribution for which proper support is
specified, before any wave-front restriction is imposed.

We prove the stronger topology statement needed below. With the
actual \(\mathcal A^k\) seminorms (GE1), for each compact chart
\(K\), real \(k\), and finite \(L\), there are a compact \(K'\),
finite \(L'\), and \(C\) such that
\[
 p_{k,K,L}(B_bv)\le C p_{k,K',L'}(v)
 \quad(v\in\mathcal A^k_{K'}),
 \qquad
 p_{k,K,L}(B_b^{\mathrm t}v)\le C p_{k,K',L'}(v).
 \tag{GT2}
\]
Here the compact sets are chosen to include the source and target
of the properly supported localized kernel. To prove the Besov
part, first localize both base variables to compact sets and extend
the resulting smooth \(x=(x',t)\)-dependence periodically on a
larger box. At \(t=0\), use the smooth collar extension of
Section 3 of the linked local lesson before periodic extension;
for each finite estimate its extension bounds involve only a
finite number of the original one-sided symbol seminorms.
Its Fourier series is
\[
 b(x,\xi')=\sum_{\ell\in\mathbb Z^n}
       e^{i\ell\cdot x}b_\ell(\xi'),\qquad
 |\partial_{\xi'}^\beta b_\ell(\xi')|
   \le C_{N\beta}\langle\ell\rangle^{-N}
                         \langle\xi'\rangle^{d-|\beta|}
 \quad(\forall N).
 \tag{GT3}
\]
A smooth symbol-valued collar extension exists explicitly. Write \(v_j(x',\xi')=\partial_t^jb(x',0,\xi')\) and choose a fixed smooth cutoff \(\chi=1\) near zero. On \(t<0\) set
\[
 \widetilde b(x',t,\xi')
   =\sum_{j=0}^{\infty}\chi(t/\epsilon_j)\frac{t^j}{j!}v_j(x',\xi').
 \tag{BW3}
\]
For \(j\ge1\), choose \(\epsilon_j\downarrow0\) so that every derivative in \(t\) through \(\lfloor j/2\rfloor\), measured in the first \(\lfloor j/2\rfloor\) tangential symbol seminorms, is at most \(2^{-j}\) for the \(j\)-th summand. The product rule bounds it by constants times \(\epsilon_j^{j-k}\) for \(k\le j/2\), so this choice is possible. Completeness of the symbol seminorm space gives convergence with every fixed collection of derivatives. Each summand is its uncut polynomial near zero, so the \(r\)-th normal jet of the sum is exactly \(v_r\); termwise jet evaluation is justified by that derivative convergence. The extension joins smoothly to \(b\) in every symbol seminorm. Compact base cutoffs then give the smooth periodic extension used in (GT3).

Periodic inversion here is the full Fejér/product-box proof of Section 13.2, followed by absolute differentiated-series convergence. For a finite target estimate, only finitely many coefficient decay and derivative bounds are used. These can be obtained with constants depending on finitely many original one-sided seminorms: take a sufficiently high finite Taylor polynomial in the negative normal variable, multiplied by a fixed cutoff, and join it to the original symbol for \(t\ge0\). The joined extension is \(C^J\), with every required frequency derivative and weighted symbol estimate, where \(J\) may be chosen as large as that finite argument requires. Its \(C^J\) periodic Fourier expansion already gives all those bounds. It equals the original symbol on the half-space, so proves the same original operator estimate there. There is no assertion that one bounded finite-jet formula simultaneously gives a smooth extension at every order.

This follows by integrating by parts \(N\) times in the compact
base Fourier coefficient; every base derivative of the original
symbol has the same order \(d\). Choose an even integer
\(M=2r\ge\max(d,0)\). The full Fourier multiplier
\(b_\ell(\xi')\langle\xi'\rangle^{-M}\) is bounded uniformly in
\((\xi',\xi_n)\) by \(C_N\langle\ell\rangle^{-N}\), so it is
bounded on \(B^s_{2,\infty}(\mathbb R^n)\) for every real \(s\):
it commutes with each full dyadic projection and Plancherel gives
the bound on each block. The factor
\(\langle\xi'\rangle^M=(1+|\xi'|^2)^r\) is the *complete*
finite polynomial in tangential derivatives, not an isotropic
replacement. Multiplication by \(e^{i\ell\cdot x}\) shifts full
frequency by \(\ell\); direct dyadic overlap shows its
\(B^s_{2,\infty}\) operator bound grows by at most a fixed
polynomial in \(\langle\ell\rangle\). More explicitly, on the fixed compact output set insert a compact multiplier \(\chi e^{i\ell\cdot x}\). The proved coordinate/multiplier estimate (C2) uses finitely many smooth seminorms; each is bounded by \(C\langle\ell\rangle^L\) by the product rule. This supplies the required polynomial bound with one fixed \(L\). Choosing \(N\) larger than
that degree plus \(n+1\), then summing (GT3), proves
\[
 \|B_bv\|_{B^s_{2,\infty}}
 \le C_{s,b}\sum_{|\beta|\le M}
          \|D'^\beta v\|_{B^s_{2,\infty}}.
 \tag{GT4}
\]
The same argument applies to every normal and tangential base
derivative of \(b\), including the transpose symbol and its exact
far smoothing kernel. For a general smooth proper kernel cutoff \(\kappa(x',y',t)\), retain the complete amplitude \(\kappa b\). The exact O4 amplitude reduction, with \(t\) as a parameter and every \(t\)-derivative included, gives a left tangential symbol of the same order and its actual far smooth tangential kernel. Apply the preceding bounds to that full symbol. A compact far kernel has a residual left symbol by its exact tangential Fourier inverse, with all parameter derivatives. Thus the estimates hold for the actual cutoff kernel, not only for cutoffs that factor into two multipliers.

The normal variable is unchanged by the kernel in (GT1), hence
\(t^aB_b=B_bt^a\). Differentiate the full expression rather than
identifying normal and tangential orders:
\[
 t^aD_n^aD'^\gamma(B_bv)
 =\sum_{j=0}^{a}\sum_{\beta\le\gamma}
       \binom aj\binom\gamma\beta
       t^j B_{D_n^jD_{x'}^\beta b}
        \bigl(t^{a-j}D_n^{a-j}D'^{\gamma-\beta}v\bigr).
 \tag{GT5}
\]
The formula also applies termwise to the proper kernel cutoff;
its derivatives are included in the differentiated symbol.
Every \(t^j\) is a smooth compact multiplier, and (GT4) controls
the remaining tangential operator by finitely many further
\(D'\) seminorms. This proves (GT2), with *each* original normal
weight and derivative retained. In particular \(B_b\) and
\(B_b^{\mathrm t}\) preserve every filtered \(\mathcal A^k\),
and the dual formula
\[
 (B_bu)(v)=u(B_b^{\mathrm t}v)
 \tag{GT6}
\]
defines a weakly continuous map \(\mathcal A'\to\mathcal A'\).
The stronger action statement follows from the explicit topology
estimate; it does not identify \(B_b\) with an isotropic
\(n\)-covariable pseudodifferential symbol.

### 6.2. The equatorial compressed cutoff

Choose a smooth conic symbol \(t_0(\xi',\rho)\) of order zero,
independent of \(x'\), with the original low-frequency cutoff, so
that
\[
 t_0=1\quad(2|\rho|<|\xi'|,\ |\xi'|>1),\qquad
 t_0=0\quad(|\rho|>|\xi'|).
 \tag{GT7}
\]
In tangential dimension zero the equatorial set is empty; take \(t_0=0\), and the assertions about nonzero tangential covectors are vacuous. Otherwise use the displayed equatorial cutoff. Multiply by a smooth normal base cutoff equal to one on
\(0\le t<1\) and supported in \(t<2\). The construction on the
unit sphere is possible because the closed equatorial band and
the normal caps are disjoint. Apply the *original* lacunarization
of Lemma 4.4 to this full symbol and write
\(t_\rho\in S^0_{\mathrm{la}}\). The difference
\(t_\rho-t_0\) is residual, with its original normal-base
decay; it does not change the principal compressed symbol.
Let \(T=T_{t_\rho}\), localized properly in a boundary chart.

For \(u\in\mathcal N\), put \(w=(I-T)u\). At every boundary
tangential covector \(q\), the full symbol of \(I-T\) is residual
on a conic neighborhood of \(q\), so (GW9) removes \(q\) from
\(\operatorname{WF}_b(w)\). At every other boundary covector
\(q\), the definition of \(\mathcal N\) removes \(q\) from
\(\operatorname{WF}_b(u)\), and (GW12) removes it from
\(\operatorname{WF}_b(w)\). Thus the boundary portion is empty:
\[
 \operatorname{WF}_b((I-T)u)|_{\partial X}=\varnothing.
 \tag{GT8}
\]
On a compact boundary patch, closedness of \(\operatorname{WF}_b\)
on the compact cosphere gives a collar in which it remains empty.
The finite microlocal cover argument (GW7) then makes a spatially
localized \(w\) an element of \(\mathcal A\). Equation (GT2)
gives \(B_bw\in\mathcal A\). We have therefore proved, as a
local *conormal equality* rather than an unproved smoothness claim,
\[
 B_bu=B_bTu+v,
 \qquad v\in\mathcal A\text{ near the boundary}.
 \tag{GT9}
\]
The equality is between the actual distributional actions (GT6).

Because \(t_\rho\) is independent of \(x'\), the unlocalized
Kohn–Nirenberg composition in (GT1) is exact:
\[
 B_bT_{t_\rho}=T_a,
 \qquad a(x',t,\xi',\rho)=b(x',t,\xi')t_\rho(t,\xi',\rho).
 \tag{GT10}
\]
Indeed integration in the intermediate tangential variable gives
\((2\pi)^{n-1}\delta(\eta'-\xi')\); no derivative of
\(t_\rho\) in \(x'\) appears. The support of \(t_0\) in (GT7)
ensures that on the high-frequency nonresidual part
\(\langle\xi'\rangle\asymp\langle(\xi',\rho)\rangle\).
All \(\xi'\), \(\rho\), and base derivatives of the product
therefore obey the full order-\(d\) symbol bounds. The residual
difference from lacunarization remains residual after
multiplication by \(b\), using arbitrary residual order to
absorb its fixed order \(d\). Since normal Fourier convolution
does not change a tangential multiplier, the product retains
the original lacunarity. Thus \(a\in S^d_{\mathrm{la}}\).

Proper-support cutoffs make (GT10) an equality modulo a residual
*full* compressed operator. To verify the asserted residual class,
write each far tangential cutoff as a kernel factor vanishing near
\(x'=y'\) and integrate by parts in \(\xi'\) arbitrarily many
times. On the nonresidual support of \(t_0\), the entire normal
frequency is bounded by a constant times \(|\xi'|\), so this
gain is arbitrary in the full \((\xi',\rho)\) order. The
lacunarization remainder is already residual. Derivatives of the
cutoff and amplitude obey the same bounds, proving the full
residual assertion. Its action on supported distributions lies
in \(\mathcal A\) by (GA5), so it does not affect the boundary
wave-front conclusions.

### 6.3. Boundary action, microsupport, and elliptic comparison

The local boundary wave-front set of \(v\in\mathcal A\) is empty
by definition, and adding such a \(v\) does not change a
wave-front set: a regularizing tester for one summand works for
the sum, and subtracting the same \(v\) gives the reverse
inclusion. Equations (GT9)–(GT10) and (GW12) therefore give
\[
 \operatorname{WF}_b(B_bu)|_{\partial X}
   =\operatorname{WF}_b(T_au)|_{\partial X}
   \subset\operatorname{WF}_b(u)|_{\partial X}
   \subset T^*\partial X\setminus0.
 \tag{GT11}
\]
Since (GT6) also gives \(B_bu\in\mathcal A'\), this proves
\(B_b:\mathcal N\to\mathcal N\) with the original tangential
operator. It also proves that the action is continuous in the
weak topology of \(\mathcal A'\) tested on fixed conormal
functions.

Suppose \(b\) is of order \(-\infty\) on a conic neighborhood of
the complement of a closed tangential cone \(\Gamma\) at the
boundary. This means a full base/parameter neighborhood of those boundary points, with every normal derivative included in the residual estimates; a statement only about the restricted symbol \(b_0\) would not suffice. At a tangential covector \(q\notin\Gamma\), the full
symbol \(a=b t_\rho\) is of order \(-\infty\) on a compressed
cone about \(q\). The original residual localization (GW9)
excludes \(q\) from \(\operatorname{WF}_b(T_au)\). At normal
compressed directions (GT11) already excludes every covector.
Hence the exact boundary microsupport statement is
\[
 \operatorname{WF}_b(B_bu)|_{\partial X}
 \subset\operatorname{WF}_b(u)|_{\partial X}\cap\Gamma.
 \tag{GT12}
\]

Write \(b_0(x',\xi')=b(x',0,\xi')\). At a tangential boundary
covector \(q=(x',0,\eta',0)\), (GT7), (GL18), and (GC4) give
the actual principal compressed symbol of \(T_a\):
\[
 \sigma_d(T_a)(q)=\sigma_d(b_0)(x',\eta')\cdot 1.
 \tag{GT13}
\]
The boundary operator action (GL24) has the same principal
symbol, with the original \((2\pi)^{-(n-1)}\) Fourier factor.
If \(b_0\) is elliptic at \(q\), then \(T_a\) is elliptic
there. The exact elliptic inclusion (GW10), applied to
\(T_au=B_bu-v\) from (GT9), gives
\[
 \operatorname{WF}_b(u)|_{\partial X}
   \subset
   \operatorname{WF}_b(B_bu)|_{\partial X}
       \cup\operatorname{Char}(b_0).
 \tag{GT14}
\]
The factor order in (GT13) stays matrix order; for vector bundles,
ellipticity means the actual boundary matrix is invertible.

### 6.4. What the argument gives in the interior

At an interior point \((x',t)\), \(t>0\), the tangential action
is the family (GT1). The full kernel is a tangential
pseudodifferential kernel times \(\delta(t-s)\). Split it with a
cutoff in \(x'-y'\) that is one near zero. Off the tangential
diagonal the tangential kernel is smooth, by arbitrary integration
by parts in \(\xi'\). Its output can therefore be singular only
in the normal variable, so every covector there has \(\xi'=0\).
On the tangential diagonal, fix an output covector with
\(\xi'\ne0\) and take a conic cutoff on which
\(|\xi'|\ge c|(\xi',\xi_n)|\) for some \(c>0\). The full
symbol \(b(x,\xi')\) obeys the ordinary isotropic symbol
estimates on that cone, since its only frequency derivatives are
in \(\xi'\) and \(\langle\xi'\rangle\asymp\langle\xi\rangle\)
there. The complementary frequency cutoff has no output
wave-front in this cone by nonstationary integration in the
full oscillatory kernel. Here is the precise Fourier estimate for this localization. First multiply the input by a compact cutoff supported in its regular base neighborhood and equal to one near the chosen output neighborhood. The omitted input is separated tangentially from that output whenever \(t=s\), so belongs to the off-tangential-diagonal term treated below. For the resulting compact input \(v\) and compact output localization, the full-frequency formula is
\[
 \widehat{B_bv}(\xi)
 =(2\pi)^{-n}\int
   \widehat b_x(\xi-\eta,\eta')\,\widehat v(\eta)\,d\eta,
 \qquad
 |\widehat b_x(\zeta,\eta')|
 \le C_N\langle\zeta\rangle^{-N}
                \langle\eta\rangle^{\max(d,0)} .
 \tag{BW2}
\]
It follows first on smooth inputs by Fourier inversion; the finite distribution order and sufficiently large \(N\) give the exact distributional extension. Split the integral into the input regular cone and its complement, with the output in a strictly smaller cone. In the first part \(\widehat v\) has arbitrary decay. In the second part angular separation gives
\(|\xi-\eta|\ge c(|\xi|+|\eta|)\), so the displayed arbitrary \(N\) defeats the fixed polynomial input order. Integration gives arbitrary output decay. The off-tangential-diagonal kernel has, for each fixed number of normal derivatives, arbitrary tangential Fourier decay by differentiation in its smooth output \(x'\); its normal growth is bounded by the finite input distribution order. On the cone \(|\xi'|\ge c|\xi|\), this also gives arbitrary full-frequency decay. These are the complete local pseudolocal estimates used for the retained kernel. Together with (GW13), this gives the exact interior
inclusion
\[
 \operatorname{WF}_b(B_bu)|_{T^*X^\circ\cap\{\xi'\ne0\}}
       \subset
       \operatorname{WF}_b(u)|_{T^*X^\circ\cap\{\xi'\ne0\}}.
 \tag{GT15}
\]
The region on which (GT15) is useful depends on the actual
wave-front covectors of \(u\). It does not claim an all-interior
inclusion: at \(\xi'=0\), a tangential smoothing kernel can
carry a normal singularity between distinct tangential points
at the same \(t\), precisely because the kernel still contains
\(\delta(t-s)\). For example, take a properly supported smooth
tangential kernel \(K(x',y')\) with
\(K(x'_1,y'_0)\ne0\) and \(x'_1\ne y'_0\), and
\(u=\delta(x'-y'_0)\otimes\delta(t-t_0)\) with \(t_0>0\).
Then \(B_bu=K(x',y'_0)\delta(t-t_0)\) has a pure-normal
wave-front covector at \((x'_1,t_0)\), while \(u\) has no
wave-front there. This proves that the exception is necessary,
rather than leaving an all-interior claim untested.

