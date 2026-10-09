# Global boundary operators, dual action and elliptic parametrices

This component retains AN03-U034 Sections 2.1–2.5, 3.5 and 4.1. Original author: Codex, September 2026, CC0. Current exact proof connections and clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0. All original mathematical displays remain unchanged.

## Exact scope and prerequisite proofs

The [geometry companion](stretched-kernels-and-compressed-geometry.md) supplies all conventions and (GL1)–(GL24), including the smooth-family definition at the new face. The [local boundary calculus](../20261005-local-boundary-calculus/boundary-adjoints-composition-and-distributions.md) supplies every ordered near/far product and adjoint remainder. Its [conormal-action companion](../20261005-local-boundary-calculus/boundary-bounds-and-conormal-action.md) supplies full conormal continuity, residual receiving estimates and the negative-order no-gain examples. The [positive-order proof](../20261005-positive-boundary-orders/positive-order-halfspace-bounds.md) supplies (PS1)–(PS17) on both original half-space Sobolev scales at every real index, including rectangular systems.

The [intrinsic conormal symbol proof](../20261005-conormal-symbols-and-corners/intrinsic-conormal-symbols.md) supplies the full coordinate law and quotient; the [conormal test proof](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md) supplies all Besov and ordinary operator bounds. The dual conormal and jet proof supplies the definitions, (GA1)–(GA2), (GD1)–(GD12), weak density, actual trace and corrected intrinsic derivatives. Thus the retained references to those equations below are exact earlier proofs. Formal adjoints use the fixed Hermitian metrics and half-density pairing. The supported space includes boundary distributions; the restricted space is its actual interior quotient. All orders are real.

For the global chart patching use the complete [locally finite partition PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md); on a boundary manifold its same relative-half-ball construction gives precompact charts with locally finite closures. Use the complete [ordinary operator calculus](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) for interior charts, all-real Hilbert and quotient duality, and [Fourier measure theory](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) for the integrals and limits. The approved antecedent is Hörmander III, Sections 18.2–18.3.

The compressed wave-front definition and its tangential consequences are subsequent work; the local parametrix below proves the complete elliptic operator identity needed there. It does not by itself restore the higher-order Cauchy lesson.

## 2. Proper global operators and conormal smoothing

### 2.1. The global kernel and its actual pushforward

Choose a smooth function \(t\) on the stretched square, positive off its
new face and vanishing simply on that face. Near a boundary diagonal point
it can be the original \((x_n+y_n)/2\). Define the order-\(m\) class by
kernels represented as
\[
 k=t^{-1/2}H,\qquad
 H\in I^m(X\widehat\times X,\widehat\Delta;\Omega^{1/2}),
 \qquad H\text{ flat on both original side faces}.
 \tag{GC1}
\]
Here conormality at the new face has precisely the smooth family meaning
specified in the geometry companion. A bundle kernel additionally has values in
\(\operatorname{Hom}(E_y,F_x)\). Multiplication by its smooth frame
changes is included in the conormal topology.

There is a well-defined pushforward despite the separate factor
\(t^{-1/2}\). Indeed, in the original normal chart, let a test
half-density have coefficient \(p(x,y)\). Its pullback has coefficient
\(t^{1/2}p(\beta(x',y',t,r))\), since the absolute normal determinant is
\(t\). Thus the actual pairing is
\[
 \langle\beta_*k,p\rangle
 =\int_0^\infty
   \left\langle H(x',y',t,r),
       p(x',t(1+r/2),y',t(1-r/2))\right\rangle_{x',y',r}\,dt.
 \tag{GC2}
\]
The conormal family is a smooth distribution-valued function of \(t\).
On a compact interval its pairing with the smooth compact test family is
bounded by finitely many test derivatives and symbol seminorms, by (C4).
The integral is consequently well defined and continuous. To verify compactness here, cover the given compact test support by finitely many relatively compact product charts. Over each closed smaller chart the resolved normal coordinate lies in the compact interval \([-2,2]\), and \(t=(x_n+y_n)/2\) is bounded. The coordinate description (GL4) therefore makes the inverse image compact. Away from the corner the blowdown is a diffeomorphism. Those
facts reduce the general pairing to finitely many such charts. Equation
(GC2) is the complete meaning of pairing \(k\) with the pulled-back test
half-density. Neither square-root factor is separately discarded, and no
pairing of an arbitrary distribution with a nonsmooth test coefficient is
asserted.

If \(\bar t\) is another admissible defining function, Hadamard's formula
gives \(\bar t=c t\), with \(c>0\) smooth near the new face. Away from
that face both functions are positive. Hence
\[
 \bar H=\bar t^{1/2}k=c^{1/2}H.
 \tag{GC3}
\]
Multiplication by \(c^{1/2}\), and by its smooth inverse, preserves the
conormal class and side flatness. The kernel, its pairing and its order
are independent of this choice.

Every compactly localized kernel of (GC1) is the original half-space
kernel of a lacunary order-\(m\) symbol by (GL19)–(GL21). Away from the
lifted diagonal the localized resolved coefficient is smooth, and the
same inverse gives a residual symbol. The latter assertion also applies
between distinct boundary charts: coordinates in the two charts may be
used as the two independent tangential variables in the smooth kernel;
there is no conormal singularity to align. Near an actual diagonal point
use the same coordinate chart on both factors. Interior charts give the
ordinary conormal pseudodifferential kernel by (C18).

The local theorem on smooth inputs therefore proves a continuous map
\[
 A:C_c^\infty(X;\Omega^{1/2}\otimes E)
       \longrightarrow C^\infty(X;\Omega^{1/2}\otimes F).
 \tag{GC4}
\]
For fixed input support and a fixed output compact set, only finitely many
product charts occur. Each local estimate uses finitely many derivatives
of the input, and the sum of these estimates is finite. This proves the
stated LF-to-Fréchet continuity. Formula (GL24) supplies its boundary
value, and the original formula (5.2) supplies every normal jet. Conversely
the local quantizations have exactly (GC1) by (GL13)–(GL18), so this kernel
description and the patched local definition determine the same class.
We denote it by \(\Psi_b^m(X;E,F)\).

To check coordinate invariance at all orders, the stretched coordinate
change is (GL5), its conormal change is (GL10), and its complete amplitude
and determinant are (C19). Reducing that entire amplitude by (C5) gives
the transformed symbol, with the full order-\((m-N)\) remainder after
\(N\) terms. All frequency factors created by a base derivative pair
with a frequency derivative and retain order \(m\). Thus the operator
class, not only its leading term, is coordinate invariant. The local
construction and the pushforward above agree in the interior and then
as distributions by the same conormal family pairing (GC2).

### 2.2. The symbol quotient and actual realization of every symbol

For a compressed symbol \(a\), the original principal half-density of
the kernel is the class of
\[
 a(x',t,\xi',\rho)t^{-1/2}
       |dx'\,dt\,d\xi'\,d\rho|^{1/2}.
 \tag{GC5}
\]
The singular half-density multiplying \(a\) is the invariant absolute
symplectic half-density in (GL12). The complete determinant law (C20)
therefore gives a scalar symbol, or a section of
\(\operatorname{Hom}(E,F)\), on \(\widetilde T^*X\), of ordinary order
\(m\), modulo order \(m-1\). Both (GL16) and (GL17) remain its actual
lower-order kernel remainder. Define \(S^m(\widetilde T^*X)\) using every
local compact base set, all base derivatives, and the frequency bound
\(\langle(\xi',\rho)\rangle^{m-|\alpha|}\). The fibre transformation
(GL10) and its inverse have smooth bounded coefficients on each compact
chart; the chain rule proves that this definition is intrinsic. The
leading symbol map has kernel exactly \(\Psi_b^{m-1}\), by the local
normal-form kernel assertion (C21).

We prove surjectivity while retaining the original prescribed symbol.
Choose a locally finite cover by precompact boundary or interior charts
\(U_j\), with locally finite closures. Choose a partition \(\varphi_j\)
with support in these charts and \(\psi_j\in C_c^\infty(U_j)\) equal to
one on a neighborhood of \(\operatorname{supp}\varphi_j\). For a given
symbol \(a\), compactly localize a full representative \(a_j\) in the
\(j\)-th frame so that it equals \(a\) on that neighborhood. In a
boundary chart take exactly the lacunary modification
\[
 (a_j)_\rho(x,\xi)=\int a_j(x,\xi',\xi_n-v)\rho(v)\,dv,
 \quad \widehat\rho\in C_c^\infty((-1/2,1)),\quad
 \widehat\rho=1\text{ near }0.
 \tag{GC6}
\]
Keep \(a_j=(a_j)_\rho+[a_j-(a_j)_\rho]\): the bracket is residual by
the full Taylor integral (4.8), and every original symbol seminorm
remains controlled. Quantize the first term and set
\[
 A=\sum_j\varphi_j T_{(a_j)_\rho}\psi_j
 \tag{GC7}
\]
in boundary charts, using ordinary quantization for interior charts.
The sum is locally finite and has order \(m\). Its two support projections
are proper: above a compact base set only finitely many chart closures
occur, and both factors in each term have compact support in that chart.
The leading term is \(\sum_j\varphi_j a=a\). Multiplication on the input
has its complete product remainder, of order \(m-1\), from (8.3);
\(\psi_j=1\) near the working diagonal. The residual bracket in (GC6)
has not become an equality between the original full symbol and its
modification; it is explicitly the error in this realization. This gives
both quotients
\[
 \Psi_b^m/\Psi_b^{m-1}\simeq
 S^m(\widetilde T^*X)/S^{m-1}(\widetilde T^*X),
 \tag{GC8}
\]
with the same isomorphism when the operator spaces are restricted to
proper support. The bundle version follows in the same charts, with the
actual frame transitions and (GC5).

### 2.3. Proper composition, adjoints and all asymptotic remainders

Let \(A\in\Psi_b^m(X;F,G)\) and
\(B\in\Psi_b^{m'}(X;E,F)\) be properly supported. For every compact
output set the support of \(A\) meets only a compact set of intermediate
variables, and that compact set meets only a compact input set under
\(B\). The reverse argument starts at a compact input set. This proves
proper support of the composed operator and permits all intermediate
partitions to be finite on the compact sets under consideration.

We give the localization argument, since a residual kernel at the new
face need not be a smooth kernel on the original square. Localize near
an output-input diagonal point. A sufficiently small common chart
contains both variables. Split the intermediate variable into a slightly
larger part of that chart and its complement. On the complementary part
both kernels are separated from their actual diagonal, so their resolved
coefficients are smooth with side flatness. On the chart part use the
original local ordered product theorem (8.1)–(8.3). Any localization of
either factor off its own diagonal gives a residual symbol by (GL19)–(GL21).
That theorem then gives a residual product: its finite-order bound holds
for every real order assigned to the residual factor, while its complete
far term (8.2) is residual as well.

For clarity, this also handles two different boundary charts. For a
localized rectangular kernel \(R(x,y)\) whose resolved coefficient is smooth, with output and input
coordinates taken from their respective charts, the literal inverse is
\[
 A_R(x,z)=x_nR\bigl(x,(x'-z',x_n(1-z_n))\bigr),
 \qquad a_R(x,\xi)=\int e^{-iz\cdot\xi}A_R(x,z)\,dz.
 \tag{GC9a}
\]
This is the same (GL19) inverse written at fixed \(x_n>0\), with all
chart half-density factors included in \(R\). Resolved smoothness,
side flatness, compact chart cutoffs and the full far estimates of
(GL19)–(GL21) make \(a_R\) residual and lacunary. The two coordinate
tuples both range in Euclidean half spaces, so the original local product
theorem applies to these rectangular symbols with the intermediate
coordinate tuple used as its common integration variable. If only one
factor has a diagonal singularity, use its chart for the intermediate
variable and its adjacent variable; the other is represented by
(GC9a). If neither factor has a singularity, either choice works. Near
a fixed output-input point off the diagonal, use disjoint neighborhoods
of those two points and split the intermediate variable into their
neighborhoods and the complement. At least one factor in each term is
then separated from its diagonal, and the preceding argument proves a
residual result. This proves the required smoothness off the lifted
diagonal, its family regularity at the new face, and its side flatness;
it does not replace a corner residual by an ordinary smoothing kernel.

In the common chart the complete product symbol is \(c=c_1+c_2\), where
\(c_1\) and \(c_2\) are the actual (8.1) and (8.2), with the original
factor order \(a\) before \(b\). The full expansion is
\[
 c\sim\sum_\alpha\frac1{\alpha!}\partial_\xi^\alpha a(x,\xi)
 D_{x'}^{\alpha'}D_v^{\alpha_n}
 b(x',v x_n,\xi',v\xi_n)\big|_{v=1},
 \qquad
 c-\sum_{|\alpha|<N}(\cdots)\in S^{m+m'-N}.
 \tag{GC9}
\]
The exact far contribution \(c_2\in S^{-\infty}\) is part of \(c\).
All its seminorms and the remainder seminorms are controlled by finitely
many seminorms of the two original factors, by that local proof. Hence
\[
 AB\in\Psi_b^{m+m'},\qquad
 \sigma(AB)=\sigma(A)\sigma(B).
 \tag{GC10}
\]
For matrices this is \(E\xrightarrow{\sigma(B)}F
\xrightarrow{\sigma(A)}G\); no order is exchanged. The same argument
proves that the residual class is a two-sided ideal among properly
supported operators of any finite order.

Transposition of the stretched square exchanges \(x,y\) and sends
\(r\) to \(-r\), keeping \(t=(x_n+y_n)/2\). Its kernel half-density
law is
\[
 H_{A^*}(x',y',t,r)=H_A(y',x',t,-r)^*.
 \tag{GC11}
\]
Conormality and side flatness are preserved. The local adjoint (7.3),
including the residual adjoint of \(a-a_\rho\), gives
\(a^\dagger-a^*\in S^{m-1}\). Thus
\[
 A^*\in\Psi_b^m(X;F,E),\quad
 \sigma(A^*)=\sigma(A)^*,\quad
 (\lambda A+\mu B)^*=\overline\lambda A^*+\overline\mu B^*.
 \tag{GC12}
\]
Proper support is preserved by this exchange. All adjoints here use the
fixed metrics and the original half-density pairing.

The calculus admits full asymptotic sums. Here is the construction needed
later for parametrices. In each chart let \(a_j\in S^{m-j}\) be the
actual localized symbols to be summed. Choose \(f\) zero on the unit
frequency ball and one outside twice that ball. Choose \(R_j\) increasing
so that \(f(\xi/R_j)a_j\) has each of the first \(j\) seminorms in
\(S^{m-j+1}\) at most \(2^{-j}\), on the first \(j\) compact base sets.
This is possible because the support has \(|\xi|\ge R_j\), giving the
extra factor \(R_j^{-1}\); frequency derivatives of the cutoff have the
same bound after the product rule. The exact sum
\[
 a_{\mathrm{sum}}=\sum_{j=0}^\infty f(\xi/R_j)a_j,
 \qquad
 a_{\mathrm{sum}}-\sum_{j<N}a_j\in S^{m-N}
 \tag{GC13}
\]
converges in the stated seminorms. For the remainder, its infinite tail
lies in \(S^{m-N}\); each of its finitely many low-frequency differences
is residual. Lacunarize the full sum by (GC6), retaining the new residual
difference, and patch as in (GC7). Each finite off-diagonal discrepancy
is residual by the localization argument above. Consequently the global
operator differs from every prescribed finite operator sum by exactly
the asserted lower-order class. This proves asymptotic completeness,
including on the proper-support subspace, without omitting any finite
term or its remainder.

### 2.4. The supported and restricted Sobolev maps

For \(m\ge0\) and every real \(s\), the actual local theorem (PS1)–(PS17)
gives the supported bound with loss \(m\). Smooth coordinate changes
and frame multiplications on compact sets are bounded on every real
Sobolev scale: integer bounds follow by the chain and product rules,
negative integers by their exact adjoints with the Jacobian, and
intermediate orders by the full dyadic estimate in the conormal test proof. Explicitly choose integers \(a<s<b\) and frequency blocks \(\Pi_j\), \(j\ge0\). For the localized coordinate/frame map \(T\), its two integer bounds give
\[
 2^{ls-js}\|\Pi_lT\Pi_j\|_{2\to2}
 \le C
 \begin{cases}
 2^{-(j-l)(s-a)},&j\ge l,\\
 2^{-(l-j)(b-s)},&j<l.
 \end{cases}
 \tag{GB1}
\]
The right side is a summable sequence in \(l-j\). Applying the triangle inequality to the sum of its shifts on \(\ell^2\) bounds the output dyadic square norm by the input norm. Plancherel identifies those norms with \(H^s\). Finite Fourier sums converge in \(H^s\); their images converge in the same space and in distributions to the actual coordinate map. This proves the bound for the original distributional map, including negative noninteger \(s\). The inverse coordinate map obeys the same argument. Boundary coordinate changes extend to open neighborhoods, preserve the closed half-space locally, and their adjoints retain the full Jacobian; the same bounds therefore pass to supported subspaces and to restriction quotients by taking the infimum over representatives. On a fixed compact input set, proper support and a
partition reduce \(A\) to finitely many of those bounds. A rectangular
residual term has every order, so use its original order-zero bound and
the continuous inclusion \(H^s\subset H^{s-m}\), valid for \(m\ge0\).
Thus, for each compact \(K\), there is a compact \(K'\) and a constant
depending on finitely many localized full-symbol seminorms such that
\[
 \operatorname{supp}u\subset K\quad\Longrightarrow\quad
 \operatorname{supp}Au\subset K',\qquad
 \|Au\|_{\dot H^{s-m}(K')}
       \le C\|u\|_{\dot H^s(K)}.
 \tag{GC14}
\]
The supported action is the original transpose action (9.1), so it
includes distributions supported at the boundary. Both localizations
and coordinates keep those terms; they are not zeroed by a chosen
extension. For a nonproper operator the same proof gives local output
bounds for compact input.

The corresponding restricted map follows from the exact local quotient
map (PS16)–(PS17). Local supported representatives give the bounded map;
the local action preserves the full ideal of distributions supported
only on the boundary by (9.2), so different representatives have the
same interior output. Taking the infimum over representatives in each
fixed chart gives the restricted norm bound. Patch the actual quotient
maps using the same finite cutoffs. This proves
\(\overline H^s_{\mathrm{comp}}\to\overline H^{s-m}_{\mathrm{loc}}\),
and the compact-output assertion under proper support. No gain of
\(-m\) is asserted when \(m<0\); the original residual examples prohibit
such a claim.

### 2.5. The supported conormal class and the residual receiving map

For real \(m\), let \(\mathcal A^m(X)\) consist of distributions supported
in the closed manifold which, in every boundary chart and its extension,
are conormal of order \(m\) to \(x_n=0\). Explicitly put
\(\kappa=-m-n/4\) and require
\[
 Pu\in B^\kappa_{2,\infty,\mathrm{loc}}
 \quad\text{for every }P\in\operatorname{Diff}_b(X),
 \qquad \operatorname{supp}u\subset X.
 \tag{GA1}
\]
The topology uses all these local seminorms. Multiplication, coordinate
changes and finite frame transitions are continuous on those Besov
spaces by (C2)–(C3), and (GL9) identifies the intrinsic tangent fields.
Moving a coefficient through a word in tangent fields leaves only
shorter words with smooth coefficients. Hence (GA1) is intrinsic and
agrees exactly with (C15), with the original shift \(-m-n/4\).

The coordinate seminorms can use \(D'\) and \(X_n=x_nD_n\). The precise
comparison with the original weighted derivatives is
\[
 x_n^kD_n^k=\prod_{j=0}^{k-1}(X_n+ij),\qquad
 X_n^k=\sum_{j=0}^k c_{kj}\,x_n^jD_n^j,
 \tag{GA2}
\]
where the first polynomial identity defines an invertible triangular
change of basis and the second is its inverse. The first follows by
\(D_n x_n=x_nD_n-i\) and induction: multiplying
\(x_n^kD_n^k\) by \(X_n+ik\) on the right gives
\(x_n^{k+1}D_n^{k+1}\). These identities retain every lower term and its
factor \(i\). Tangential derivatives commute with \(X_n\). On compact
sets all smooth-coefficient tangent words reduce to these generators.
In particular (GA1) makes \(u\) smooth in the interior by repeated
ordinary derivatives there and the local Sobolev estimate.

If \(A\in\Psi_b^d\) is proper, its local conormal preservation theorem
11.2, with the actual index \(\kappa=-m-n/4\), gives
\[
 A:\mathcal A^m(X;E)\longrightarrow\mathcal A^m(X;F)
 \tag{GA3}
\]
continuously, for every real \(m,d\). Finite localized product estimates
prove the global continuity as in (GC14). An off-diagonal resolved term
is residual and obeys the same theorem in the rectangular chart.
The order \(d\) does not change the conormal index: the local proof
factorizes each full tangent derivative of the original operator through
an even-order totally characteristic differential operator and applies
the order-zero Besov bound to its two complete factors. In particular
neither the original frequency nor a positive-order remainder is omitted.

There is a stronger receiving statement for a residual operator
\(R\in\Psi_b^{-\infty}\). Fix an input compact set and \(N>0\).
For every tangent word \(P\), the composition \(PR\) is still residual,
by the local product formulas and (GC10). Its order-zero bound therefore
gives
\[
 \|PRu\|_{H^{-N}(K')}\le C_{P,N,K}\|u\|_{\dot H^{-N}(K)},
 \qquad
 Ru\in\mathcal A^{N-n/4}(X).
 \tag{GA4}
\]
The inclusion \(H^{-N}\subset B^{-N}_{2,\infty}\) is immediate from
the dyadic \(\ell^2\) and \(\ell^\infty\) norms. Any compactly supported
distribution of order \(L\) belongs to \(H^{-N}\) for
\(N>L+n/2\): its Fourier transform is bounded by
\(C\langle\xi\rangle^L\), and the weighted square integral converges
for exactly that strict inequality. The same estimate is uniform on a
family with fixed support and bounded distribution-order seminorm.
Thus
\[
 R:\mathcal E'(X)\longrightarrow
       \mathcal A(X):=\bigcup_{m\in\mathbb R}\mathcal A^m(X),
 \tag{GA5}
\]
with the explicit fixed-Sobolev-source continuity in (GA4). This is a
conormal receiving map, not an assertion that a residual operator
produces a smooth function at the boundary.

### 3.5. Proper totally characteristic operators on the dual class

Let \(B\in\Psi_b^d(X;E,F)\) be properly supported. Its formal adjoint
\(B^*\) preserves \(\mathcal A^m\) continuously for every \(m\), by
(GC12) and (GA3). Given a compact output test \(v\in\mathcal A^m\),
proper support places \(B^*v\) in a compact set depending only on the
support of \(v\); its full conormal seminorms are bounded by finitely
many input seminorms. Define the actual dual action by
\[
 (Bu)(v)=u(B^*v).
 \tag{GD13}
\]
For a smooth boundary test, (GD3) and the preceding estimate prove
\(Bu\in\mathcal A'\). For smooth \(u\), the local adjoint identity
(7.6) makes (GD13) the original kernel action. For general \(u\),
(GD5) and weak continuity extend that equality; in the interior it
matches the usual distributional operator. The coefficient order and
bundle maps remain those of the original \(B\), with no scalar
commutation of matrices.

The boundary jet formula extends as well. In a local half-space chart,
let \(a\in S^d_{\mathrm{la}}\), and define the \(k\)-th interior normal
derivative of \(u\) by iterating (GD9), then taking (GD8). For smooth
\(u\), the exact formula is
\[
 \begin{aligned}
 \bigl(\nabla_n^{\mathrm{int},k}T_au\bigr)|_{x_n=0}
   &=\sum_{j=0}^k\binom{k}{j}
       a_{kj}(x',D')
       \bigl(\nabla_n^{\mathrm{int},j}u|_{x_n=0}\bigr),\\
 a_{kj}(x',\xi')
   &=\sum_{i=0}^j\binom{j}{i}
       \bigl(D_{x_n}^{k-j}D_{\xi_n}^{i}a\bigr)
                   (x',0,\xi',0).
 \end{aligned}
 \tag{GD14}
\]
Every coefficient in the inner sum and the outer binomial factor is
retained. Its \(i\)-th summand has order \(d-i\). The tangent boundary
operator \(a_{kj}(x',D')\) acts continuously on boundary distributions
after compact localization; this is the ordinary local symbol action.
The left and right sides of (GD14) are weakly continuous in \(u\) by
(GD8), (GD9), (GD13) and the boundary operator continuity. Smooth
functions are weakly dense by (GD5), so (GD14) holds for every
\(u\in\mathcal A'\). It is a statement about their actual boundary
traces, not about an arbitrary supported representative's raw
distributional normal derivatives.

## 4. Compressed wave fronts

### 4.1. Ellipticity and the characteristic set at every symbol order

Let \(B\in\Psi_b^m(X;E,F)\) and let \(b\) be its complete local
symbol. At a nonzero compressed covector \(q=(x_0,\zeta_0)\), call
\(B\) elliptic if the two bundle ranks agree and there are a base
neighborhood \(U\), an open cone \(\Gamma\) containing
\(\zeta_0\), constants \(c,R>0\), and local frames such that
\[
 b(x,\zeta):E_x\to F_x\text{ is invertible},\qquad
 \|b(x,\zeta)^{-1}\|\le c^{-1}\langle\zeta\rangle^{-m}
 \quad(x\in U,\ \zeta\in\Gamma,\ |\zeta|\ge R).
 \tag{GW1}
\]
The set of covectors where this fails is \(\operatorname{Char}B\).
Changing the representative by \(S^{m-1}\) does not change (GW1):
\(b_0^{-1}(b-b_0)\) is \(O(\langle\zeta\rangle^{-1})\), so for
large \(|\zeta|\) its ordered Neumann series is invertible. Explicitly for a matrix \(E\) with \(\|E\|<1\), the partial sums of \(\sum_{\nu\ge0}(-E)^\nu\) are Cauchy in the finite-dimensional matrix norm, and multiplication by \(I+E\) leaves the error \((-E)^{N+1}\), whose norm tends to zero. The limit is the two-sided inverse. Smooth
frame changes conjugate or left/right multiply by uniformly invertible
matrices on a smaller compact chart. Thus the definition is intrinsic.
The complement of the characteristic set is open and conic; the set
itself is closed and conic in \(\widetilde T^*X\setminus0\).

The inverse in (GW1) has the exact order \(-m\) on a smaller cone.
Differentiate \(b^{-1}b=I_E\):
\[
 \partial_{\zeta_j}b^{-1}
   =-b^{-1}(\partial_{\zeta_j}b)b^{-1},\qquad
 \partial_{x_j}b^{-1}
   =-b^{-1}(\partial_{x_j}b)b^{-1}.
 \tag{GW2}
\]
Repeated product differentiation keeps the original matrix order.
Every frequency derivative lowers the order by one; every base
derivative leaves it unchanged. Multiplying by a conic cutoff gives a
global chart symbol of order \(-m\). This proves the symbol estimate
needed for an actual microlocal parametrix.

Here is the complete construction. Choose nested cones
\(\Gamma_0\Subset\Gamma_1\Subset\Gamma\) and base neighborhoods
\(U_0\Subset U_1\Subset U\), with a smooth large-frequency cutoff
\(\chi\) supported in \(U_1\times\Gamma_1\) and equal to one on
\(U_0\times\Gamma_0\) for \(|\zeta|\) large. Set
\(c_0=\chi b^{-1}\), with the original map \(F\to E\).
The lacunary realization (GC6)–(GC7) changes this by a residual
symbol only. The ordered product gives
\[
 c_0\# b=\chi I_E+e_1,\qquad e_1\in S^{-1},
 \quad e_1\text{ residual away from the elliptic working cone}.
 \tag{GW3}
\]
Suppose the sum \(c_0+\cdots+c_{N-1}\) has error
\(e_N\in S^{-N}\), residual away from that cone. Its next correction is
\[
 c_N=-\chi_1e_N b^{-1}\in S^{-m-N},
 \qquad (e_N+c_N b)=0
 \quad\text{where }\chi_1=1\text{ on the nonresidual support of }e_N.
 \tag{GW4}
\]
The actual product \(c_N\# b-c_Nb\) is one order lower by (GC9),
so the new error is in \(S^{-N-1}\), still residual off the
elliptic cone. One fixed larger cutoff suffices: take \(\chi_1=1\) near the closed base-angular support of \(\chi\), inside the elliptic chart. The finite local product formula shows that away from this support every term of \(e_1\) is zero to arbitrary symbol order, because every term contains a derivative of \(c_0\); its full remainder can be assigned arbitrarily negative order. Inductively the same is true for \(e_N\) and \(c_N\). In the transition region of \(\chi_1\) these errors are already residual, so its derivatives create only residual terms. Low frequencies are compact and hence residual. This justifies the stated cancellation with no division outside the elliptic region.

The cutoff \(\chi_1\) is supported inside the cone
where \(b^{-1}\) exists. At each stage the part not cancelled by
\(\chi_1=1\) was already residual; include it in the final residual
instead of dividing it by \(b\). Asymptotic summation (GC13) produces
a single properly supported \(C\in\Psi_b^{-m}(F,E)\) with the
global localized identity
\[
 CB=Q+R,
 \qquad Q=\operatorname{Op}(\chi I_E)\in\Psi_b^0(E,E),
 \quad R\in\Psi_b^{-\infty},
 \tag{GW5}
\]
and \(Q\) is elliptic on \(U_0\times\Gamma_0\). The low-frequency
part and all coordinate-patching errors are residual, and every
finite error is retained until its correction in (GW4).
The same construction on \(b c=I_F\) yields a right parametrix
when needed; it is a separate ordered calculation, not inferred by
commuting the matrices in (GW4).

