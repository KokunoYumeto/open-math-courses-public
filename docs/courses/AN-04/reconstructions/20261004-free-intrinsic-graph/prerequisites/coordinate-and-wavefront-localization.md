# Coordinate transport and directional localization

This is a bounded modified selection from AN03-U012, Sections 2, 7–8
and 18.1–18.3, with connecting arguments for the present intrinsic
class.

Original principal author and publisher: AN-03 course-writing task /
AN-03 local course project, 2026. Earlier modification: AN-03 course-writing task and
OpenAI Codex. This selection and its connecting arguments: GPT-6 Astra
(OpenAI), Ultra, 4 October 2026; publisher: AN-04 local course project.
Original text: CC0.

The free human sources are Gerd Grubb's author-hosted
[Chapter 8, Section 8.1](https://web.math.ku.dk/~grubb/dist8n.pdf),
and Lars Hörmander's freely readable
[*Fourier integral operators. I*, Section 2.5](https://projecteuclid.org/journals/acta-mathematica/volume-127/issue-none/Fourier-integral-operators-I/10.1007/BF02392052.pdf).
Only the coordinate-amplitude and Fourier directional arguments specified
below are used. Every proof needed here is supplied in the programme.

## T0. Inputs, test functions and the distributional coordinate map

The earlier analytic inputs are [P1, B0–B6](dyadic-endpoint.md),
[P2, O0–O6](ordinary-operator-calculus.md), and
[P3, M0–M8](measure-and-l2.md) and [L0–L3](fourier-l2.md).
They supply the exact ordinary amplitude expansion, its differentiated
remainders, proper support, smoothing kernels, Fourier inversion and
the local \(B^s_{2,\infty}\) estimates.
Smooth finite-dimensional calculus, finite cutoffs and compactness have
the same exact U001 proofs as [C0](conic-frequency-coordinates.md).
The compact parameter integral and integration-by-parts arguments use
the earlier U001 contract FTC-TAYLOR-COMPACT-PARAMETERS and the exact
[P17.2–P17.5 proofs](../../20261004-free-stationary-phase/global-integral-prerequisite-completions.md).
Compact chart substitution is proved in
[U001 P21.3–P21.4](../../20261004-free-stationary-phase/change-of-variables-prerequisite-completions.md).
No new theorem about general distribution kernels
or arbitrary smooth-map pullbacks is assumed.

Write \(\langle u,\varphi\rangle\) for the bilinear pairing of a
scalar distribution with a compact smooth test density, represented
as \(\varphi(y)\,dy\) in coordinates. Continuity on tests with
support in a fixed compact \(K\) implies a finite-order estimate
\[
 |\langle u,\varphi\rangle|
 \le C_K\max_{|\alpha|\le M_K}\|\partial^\alpha\varphi\|_\infty .
 \tag{T1}
\]
Indeed a zero neighborhood making the pairing less than one contains
an intersection of finitely many test-seminorm balls. Their maximum
is bounded by a constant times the displayed seminorm for the largest
of their derivative orders. Rescaling a nonzero test proves (T1);
the zero-seminorm case follows by arbitrary rescaling.

For a compactly supported distribution \(v\), choose
\(\tau\in C_c^\infty\) equal to one near its support and define
\(\widehat v(\xi)=\langle v,\tau e^{-iy\cdot\xi}\rangle\).
The value is independent of \(\tau\), since a test vanishing near
the support pairs to zero. To justify that last assertion from the
definition of support, cover its compact test support outside
\(\operatorname{supp}v\) by finitely many open sets on each of
which the distribution vanishes, and use the U001 finite partition.
The product rule and (T1) give, for every fixed \(\alpha\),
\[
 |\partial_\xi^\alpha\widehat v(\xi)|
 \le C_\alpha\langle\xi\rangle^M.
 \tag{T2}
\]
Here the derivative corresponds to the test multiplier
\((-iy)^\alpha\), on the same fixed compact support; the order
\(M\) in (T1) works for all fixed \(\alpha\).
Taylor's formula in the parameter \(\xi\), in each of the finitely
many required test seminorms, justifies these derivatives.
This also makes \(v\) a tempered distribution.

Let \(\kappa:U_y\to V_x\) be a smooth diffeomorphism and
\(g=\kappa^{-1}\). The distribution representing \(u\circ g\) is
defined by
\[
 \langle T_\kappa u,\psi\rangle
 =\langle u,(\psi\circ\kappa)|\det D\kappa|\rangle .
 \tag{T3}
\]
The test on the right has compact support in \(U\). On every
fixed output compact set, the product and chain rules bound all
its test seminorms by finitely many seminorms of \(\psi\).
Thus the map on tests is continuous, and (T3) defines a distribution.
The determinant is smooth and nonzero; its absolute value is smooth
because its sign is locally constant.
The determinant chain rule proves
\(T_\lambda T_\kappa=T_{\lambda\circ\kappa}\) and
\(T_gT_\kappa=I\), by direct substitution in (T3).
The completed change-of-variables proof U001 P21.3–P21.4 identifies
(T3) with ordinary composition for smooth functions, after compact
localization. P3 M8 identifies these compact integrals with Lebesgue
integrals. This is the function identity needed for the kernel argument.
The same test bounds give continuity on distributions. For the
strong dual topology, the image of a bounded test set is bounded:
the inverse image of each zero neighborhood under a continuous
linear map is a zero neighborhood. This proves the required bound
on each strong-dual seminorm.

## T1. Transport an ordinary symbol with both Jacobians

Let \(A\) be a properly supported ordinary operator of order \(d\)
on \(U\). Its transported operator is
\[
 A^\kappa=T_\kappa A T_g.
 \tag{T4}
\]
Then \(A^\kappa\) is a proper ordinary operator of the same order.
For a full local symbol \(a\), its principal symbol is
\[
 a^\kappa(\kappa(y),\eta)
   =a(y,D\kappa(y)^T\eta)\pmod{S^{d-1}}.
 \tag{T5}
\]
The assertion includes matrix symbols in their fixed matrix order.

**Proof.** P2 O5 reduces each compact localization to finitely many
compact amplitude kernels plus a compact smooth kernel. A smooth
kernel transports to
\[
 K^\kappa(x,z)=K(g(x),g(z))|\det Dg(z)|,
 \tag{T6}
\]
which is again smooth, with compact support for a compact kernel.
So consider one symbol kernel near the diagonal in a convex base
neighborhood. Put
\[
 L(y,w)=\int_0^1D\kappa(w+t(y-w))\,dt.
 \tag{T7}
\]
The fundamental theorem of calculus proves
\(\kappa(y)-\kappa(w)=L(y,w)(y-w)\), and
\(L(y,y)=D\kappa(y)\).
On a sufficiently small neighborhood of a compact diagonal piece,
\(\det L\) stays away from zero by continuity and compactness.
The cofactor inverse formula and the compact parameter derivative
proof give bounded derivatives of \(L\) and \(L^{-1}\) there.

Use \(x=\kappa(y)\), \(z=\kappa(w)\) and
\(\xi=L(y,w)^T\eta\) in the kernel integral. With a compact cutoff
\(\chi(y,w)=1\) near the relevant diagonal piece, the new amplitude is
\[
 c(x,z,\eta)=
 \chi(y,w)a(y,L(y,w)^T\eta)
 \frac{|\det L(y,w)|}{|\det D\kappa(w)|},
 \quad (y,w)=(g(x),g(z)).
 \tag{T8}
\]
The numerator is the frequency Jacobian. The denominator is the
input base Jacobian. Neither can be omitted.

This identity also holds for the distribution kernels: first insert
a smooth frequency cutoff tending to one, where the changes of
variables and test pairings are ordinary integrals. Such transformed
cutoffs have the form \(r(\varepsilon L^T\eta)\), with \(r=1\)
near zero. Every base derivative is uniformly bounded: differentiating
the argument produces \(\varepsilon\eta\), which is bounded on
the support of a derivative of \(r\), since \(L\) is uniformly
invertible. Higher product and chain rules give the same bound.
For fixed frequency these cutoffs and all base derivatives tend
to those of one. Against a compact kernel test, integrate by parts
in \(z\) using \((1-\Delta_z)^k/\langle\eta\rangle^{2k}\),
exactly as in P2 O4. Base derivatives preserve amplitude order,
so the resulting integrand has a uniform integrable bound
\(C\langle\eta\rangle^{d-2k}\) when \(2k>d+n\).
Dominated convergence from P3 proves the same kernel limit as
the untransformed regularization. P2 O0 product-test detection
identifies the two kernels.

Here are all derivative estimates needed in (T8).
On these compact sets, invertibility gives
\(\langle L^T\eta\rangle\asymp\langle\eta\rangle\).
A frequency derivative differentiates \(a\) in frequency and
loses one order. A base derivative differentiating \(L^T\eta\)
introduces one linear factor in \(\eta\) and one frequency
derivative of \(a\), for net order zero. Direct base derivatives
of \(a\), and derivatives of the cutoffs, determinant ratio and
inverse chart, cost zero. Repeated chain and product rules
therefore give
\[
 |\partial_x^\beta\partial_z^\gamma\partial_\eta^\alpha c|
 \le C_{\alpha\beta\gamma}\langle\eta\rangle^{d-|\alpha|}.
 \tag{T9}
\]
Every constant uses finitely many derivatives on the fixed compacts.
The compact-amplitude theorem P2 O4 now gives a left symbol \(b\)
with, for every integer \(N\ge1\),
\[
 b(x,\eta)-
 \sum_{|\alpha|<N}\frac{\partial_\eta^\alpha D_z^\alpha
                         c(x,z,\eta)|_{z=x}}{\alpha!}
 \in S^{d-N}.
 \tag{T10}
\]
This includes every differentiated remainder estimate. At the
diagonal the two Jacobians in (T8) cancel. The \(N=1\) formula
therefore gives (T5). A finite cover of the compact diagonal
part, with the finite partition already supplied in U001,
finishes the local assertion; the omitted off-diagonal kernels
are smooth by P2 O4.

Finally the support relation transforms by the homeomorphism
\(\kappa\times\kappa\). For a compact set in one output factor,
its inverse image is compact, the original proper projection
bounds the other factor by a compact set, and \(\kappa\) maps
that compact set to a compact set. This proves both proper
projections. Transposing the continuous test maps identifies
(T4) on all distributions, using T0. \(\square\)

## T2. Conic smoothing and composition

A full symbol is *smoothing at* \((y_0,\xi_0)\), \(\xi_0\ne0\),
if it is in \(S^{-N}\) for every \(N\) on one open base and
frequency cone about that point, with all differentiated estimates.
Define the essential support \(\operatorname{ess}(A)\) to be
the complementary closed conic set of a local full symbol.

This definition is independent of the full-symbol representative:
after compact kernel localization, a symbol is recovered by the
Fourier transform in the difference variable of its kernel.
Fourier inversion and P2 O0 show uniqueness. Altering a kernel
localization away from the diagonal changes that compact kernel
by a smooth compact kernel, whose difference-variable transform
is \(S^{-\infty}\) by integration by parts. These are exactly
the changes of local representatives used here.

It is also independent of coordinates. In (T10), each coefficient
is a finite sum of derivatives of \(a\) at
\((y,D\kappa(y)^T\eta)\), multiplied by smooth coefficients and
polynomials in \(\eta\). If \(a\) is smoothing on a cone there,
every coefficient is smoothing on a fixed smaller transformed
cone. The remainder is in \(S^{d-N}\) for arbitrary \(N\)
on that same cone. Hence \(b\) is smoothing there. Applying
the assertion to \(g\) proves the converse. The resulting
cotangent transformation is
\[
 (y,\xi)\longmapsto
       (\kappa(y),D\kappa(y)^{-T}\xi).
 \tag{T11}
\]

The full product formula P2 O3 also gives
\[
 \operatorname{ess}(AB)
 \subset\operatorname{ess}(A)\cap\operatorname{ess}(B).
 \tag{T12}
\]
Indeed, on a cone where either factor is smoothing, every term
in each finite differential product expansion is smoothing.
The remainder is in \(S^{d+d'-N}\) for every \(N\), with
all derivatives. This proves smoothing on that same cone.
Local compact cutoffs and P2 O6 account for the proper
composition and smooth off-diagonal remainders. A compact
localized symbol with empty essential support is globally
\(S^{-\infty}\): a finite cover of its compact base and
unit-frequency directions supplies each fixed seminorm bound.
Its kernel is smooth by P2 O4. These facts also justify all
uses of “equal modulo smoothing” below.

## T3. Coordinate and frame invariance of iterated regularity

For a closed conic Lagrangian \(\Lambda\), use the original intrinsic
definition: every word in proper order-one operators whose
symbols restrict to order zero on \(\Lambda\) must take \(u\)
into \(B^s_{2,\infty,\mathrm{loc}}\), with
\(s=-m-n/4\), including the empty word.

This definition is invariant under a base diffeomorphism and
a smooth invertible change of finite-rank frame.
To prove it, T1 and (T5) carry precisely the admissible
operators to the admissible operators for (T11).
Ordinary conic symbol orders are preserved: every derivative
of the base-dependent linear frequency substitution gains
at most the frequency power cancelled by the corresponding
frequency derivative, as in (T9). The order-zero error in
an order-one principal symbol stays order zero.
Conjugation preserves products exactly,
\[
 T_\kappa(L_1\cdots L_Nu)
       =L_1^\kappa\cdots L_N^\kappa T_\kappa u.
 \tag{T13}
\]
P1 B5 preserves the local Besov space for this exact real
exponent \(s\), including the supremum endpoint.
Thus (T13) proves one implication, and the inverse chart
proves the other.

For a frame matrix \(F(x)\), multiplication by \(F\) and
\(F^{-1}\) preserves the local Besov space by P1 B4.
The transported operator \(FLF^{-1}\) is proper, and P2
gives principal symbol \(F l F^{-1}\) modulo \(S^0\).
Its restriction to the Lagrangian is therefore of order zero
exactly when that of \(l\) is. The product cancellation in
(T13) applies with \(F\) in place of \(T_\kappa\).
This proves the frame assertion without commuting matrix
factors. In the half-density frame the additional factor is
\(|\det Dg(x)|^{1/2}\), smooth and nonzero; it is the same
case, with the smooth-root proof in U001.

All assertions are local in the base. Here is why local
operator tests suffice. For a fixed compact output and a word
of length \(N\), choose nested compact neighborhoods within
the chart and scalar cutoffs
\(\chi_0,\ldots,\chi_N\), with \(\chi_{j+1}=1\) near
\(\operatorname{supp}\chi_j\). Replace the localized word by
\(\chi_0L_1\chi_1L_2\cdots L_N\chi_Nu\).
In the telescoping difference, each factor
\(\chi_jL_{j+1}(1-\chi_{j+1})\) has its variables separated.
Properness and P2 O4 make its output smooth; every factor
to its left preserves smooth functions by P2 O5.
The difference is consequently smooth. Compact kernels
inside the chart extend by zero and remain ordinary proper
operators, while multiplication of their principal symbols
by these scalar cutoffs preserves the vanishing condition.
A finite base partition on a compact set proves equivalence
with the original local definition. No global elliptic
inverse has entered this coordinate argument.

## W1. Fourier cutoffs and the definition of wavefront

A nonzero covector \((y_0,\xi_0)\) is regular for \(u\) if
some compact smooth \(\chi=1\) near \(y_0\) makes
\(\widehat{\chi u}\) rapidly decreasing in an open cone
about \(\xi_0\). Rapid decrease here means every power
bound for its values. This defines the complement of
\(\operatorname{WF}(u)\).

For a compact distribution \(v\) and \(b\in C_c^\infty\),
Fourier inversion on the test, with (T1), gives
\[
 \widehat{bv}(\xi)=(2\pi)^{-n}
       \int\widehat b(\xi-\eta)\widehat v(\eta)\,d\eta.
 \tag{W1}
\]
The integral converges absolutely by (T2) and Schwartz
decrease of \(\widehat b\). It converges in each fixed
test seminorm before pairing: differentiated Fourier
inversion supplies additional polynomial factors, defeated
by further Schwartz decay. Thus passing the distribution
through the integral is justified by (T1).

If \(\widehat v\) is rapidly decreasing in a cone \(V\),
then \(\widehat{bv}\) is rapidly decreasing in every cone
\(W\) whose angular closure is contained in \(V\).
For \(\xi\in W,\eta\notin V\),
\[
 |\xi-\eta|\ge c(|\xi|+|\eta|).
 \tag{W2}
\]
To prove the positive constant, normalize
\(|\xi|+|\eta|=1\) and minimize on the resulting closed
bounded set, including zero endpoints. A zero minimum
would give two equal nonzero vectors in disjoint angular
sets; both zero is excluded by the normalization.
Homogeneity restores (W2).
In (W1), on \(\eta\in V\) use rapid decrease of both
factors and
\(1+|\xi|\le(1+|\xi-\eta|)(1+|\eta|)\).
Taking both decay exponents above \(N+n+1\) yields
\(C_N(1+|\xi|)^{-N}\) after integration.
On the complementary region, take the decay exponent
of \(\widehat b\) above \(N+M+n+1\) and apply (T2)
and (W2). This proves the assertion with every \(N\).

The same convolution argument holds for a tempered
distribution whose Fourier transform is a polynomially
bounded function: dual Fourier inversion gives (W1)
and the same absolutely convergent integrals.
This version will be used for a Fourier multiplier output.

A cutoff merely nonzero at \(y_0\) gives the same definition:
multiply by its smooth reciprocal on a smaller neighborhood
and apply the result just proved. The regular set is open
and conic, and the definition is unchanged on restricting
to a smaller base open set. Smooth multiplication cannot
enlarge wavefront; a smooth invertible matrix cannot change
the union of the component wavefront sets, by applying
this assertion to its entries and then to its inverse.

A distribution is smooth near a point exactly when all
directions there are regular. For the nontrivial implication,
cover the unit sphere by finitely many of the regular
direction cones, shrink the base cutoff to the intersection
of their neighborhoods, and apply (W1). The resulting
compact distribution has rapidly decreasing Fourier values
in every direction. Its inverse Fourier integral and every
derivative are absolutely convergent, so it is smooth.
The inverse distribution identity in P3 identifies this
function with that distribution. The converse follows by
integration by parts for compact smooth functions.

## W2. The complete nonstationary bound for a chart

For a real phase \(\Phi(y,\xi,\eta)\), linear in the two
frequency vectors, assume on the fixed compact amplitude
support \(K\) that
\[
 \begin{gathered}
 |\partial_y^\alpha\Phi|\le C_\alpha R,\qquad
 |\nabla_y\Phi|\ge cR,\\
 R=|\xi|+|\eta|\ge1.
 \end{gathered}
 \tag{W3}
\]
For \(I=\int a(y)e^{i\Phi}\,dy\), use the full operators
\[
 \begin{aligned}
 L&=\sum_j\frac{\partial_{y_j}\Phi}{i|\nabla_y\Phi|^2}
                       \partial_{y_j},\\
 Le^{i\Phi}&=e^{i\Phi},\\
 L^ta&=-\sum_j\partial_{y_j}
       \left(\frac{\partial_{y_j}\Phi}{i|\nabla_y\Phi|^2}a\right),\\
 I&=\int (L^t)^Na\,e^{i\Phi}\,dy .
 \end{aligned}
 \tag{W4}
\]
The superscript \(t\) is the bilinear transpose.
All derivatives of each coefficient are \(O(R^{-1})\).
Indeed divide the phase by \(R\); its derivatives are
bounded, its squared gradient is bounded below by \(c^2\),
and repeated reciprocal, product and chain rules give the
claim, retaining the single outside factor \(R^{-1}\).
By induction, \((L^t)^Na\) is a finite sum with \(N\)
such factors and amplitude derivatives of order at most
\(N\). Compact integration and integration by parts give
\[
 |I|\le C_NR^{-N}
       \max_{|\alpha|\le N}\|\partial^\alpha a\|_\infty .
 \tag{W5}
\]
For \(R<1\), the direct compact integral gives the same
bound with \(R\) replaced by \(1+R\).
Any fixed further parameter derivative introduces only
finitely many frequency factors; take that many additional
integrations in (W4). This proves the differentiated
versions used below, not just an estimate of values.

## W3. Diffeomorphisms transport exactly the cotangent direction

The coordinate map (T3) satisfies
\[
 \operatorname{WF}(T_\kappa u)
 =\{(\kappa(y),D\kappa(y)^{-T}\xi):
                         (y,\xi)\in\operatorname{WF}(u)\}.
 \tag{W6}
\]

**Proof.** Suppose \(u\) is regular at \((y_0,\xi_0)\).
Put \(x_0=\kappa(y_0)\) and
\(\eta_0=D\kappa(y_0)^{-T}\xi_0\).
Choose \(v=\chi u\) compactly supported, with \(\chi=1\)
near \(y_0\), whose transform is rapidly decreasing on
a cone \(V\) about \(\xi_0\).
Take \(b\) supported sufficiently close to \(x_0\),
with \(g(\operatorname{supp}b)\) inside that neighborhood.
Equations (T3) and Fourier inversion on its test give
\[
 \begin{aligned}
 \widehat{bT_\kappa u}(\eta)
  &=(2\pi)^{-n}\int \widehat v(\xi)I(\eta,\xi)\,d\xi,\\
 I(\eta,\xi)
  &=\int b(\kappa(y))|\det D\kappa(y)|
                    e^{i(y\cdot\xi-\kappa(y)\cdot\eta)}\,dy .
 \end{aligned}
 \tag{W7}
\]
For fixed \(\eta\), the inner transform decays faster
than any power for large \(\xi\), either by ordinary
test-function Fourier decay or by W2. Thus the outer
integral and its derivation from (T1) are justified.

The phase gradient is
\(\xi-D\kappa(y)^T\eta\).
On the compact support, the matrix and its inverse have
bounded norms. Consequently this gradient is bounded
below by \(c(|\xi|+|\eta|)\) whenever
\(|\xi|\) is sufficiently small or sufficiently large
relative to \(|\eta|\).
For comparable lengths, shrink the base support and
an output cone \(W\) about \(\eta_0\) so that
the directions of \(D\kappa(y)^T\eta\), \(\eta\in W\),
lie in a cone whose angular closure is inside \(V\).
Compact separation as in (W2) gives the same lower
bound if \(\xi\notin V\).
All higher phase derivatives have the upper bounds (W3).

On these separated regions, (W5) and (T2) give an
integral bounded by
\[
 C_N\int(1+|\xi|+|\eta|)^{-N}(1+|\xi|)^M\,d\xi
 \le C'_N(1+|\eta|)^{M+n-N},\quad N>M+n .
 \tag{W8}
\]
The last estimate follows by
\(\xi=(1+|\eta|)\zeta\), leaving the integrable
factor \((1+|\zeta|)^{M-N}\).
Choose \(N\) for any prescribed output decay.
On the remaining comparable region \(\xi\in V\),
use arbitrary rapid decrease of \(\widehat v\)
and the constant bound for the compact integral \(I\).
Its integration volume is at most
\(C(1+|\eta|)^n\), so arbitrary output decay follows
again. This proves regularity at \((x_0,\eta_0)\).
Apply the proved implication to the inverse map \(g\)
and the exact composition law in T0. The two inclusions
give (W6). \(\square\)

## W4. Ordinary operators and compact microlocal cutoffs

For a proper ordinary operator \(P\),
\[
 \operatorname{WF}(Pu)
 \subset \operatorname{ess}(P)\cap\operatorname{WF}(u).
 \tag{W9}
\]
Here is a direct proof that requires no elliptic parametrix.
Localize the output compactly. P2 O5 confines the input to
a compact set; input terms separated from the output are
smooth by P2 O4. For the remaining symbol piece, P1 B4
gives the Fourier formula
\[
 \widehat{Pv}(\xi)=(2\pi)^{-n}
   \int\widehat p_y(\xi-\eta,\eta)\widehat v(\eta)\,d\eta,
 \quad
 |\widehat p_y(\zeta,\eta)|
       \le C_N\langle\zeta\rangle^{-N}\langle\eta\rangle^d .
 \tag{W10}
\]
For a compact distribution \(v\), this formula follows by
Fourier inversion on tests and the finite-order bound,
or by the regularizations in P2; the displayed integral
converges absolutely for each fixed \(\xi\), by (T2)
and a sufficiently large \(N\).

If the input is regular at the point under consideration,
choose the input cutoff inside that regular neighborhood.
In (W10) split into the cone where \(\widehat v\) is rapidly
decreasing and its complement. The first part is controlled
by rapid decrease and the Schwartz factor; the second
uses (W2). The estimates in the proof of W1, with \(M+d\)
in place of the polynomial exponent, give rapid output
decrease on a smaller cone.
If instead \(p\) is smoothing on a base and frequency
cone, choose the output cutoff inside that base set.
In the good frequency cone, integration by parts in the
base variable gives, for arbitrary \(N,J\),
\[
 |\widehat p_y(\zeta,\eta)|
       \le C_{N,J}\langle\zeta\rangle^{-N}
                         \langle\eta\rangle^{-J}.
 \tag{W11}
\]
This defeats the polynomial input. Outside it, angular
separation and (W10) give the same rapid output bound.
Smooth kernel remainders preserve regularity. This proves
both exclusions in (W9), including for matrix entries.

Given \(\rho=(y_0,\xi_0)\), choose nested small base and
angular neighborhoods. Smooth finite cutoffs from U001,
homogenized off zero, give a real smooth frequency cutoff
\(\gamma(\xi)\), zero near \(\xi=0\), homogeneous of degree
zero for large \(|\xi|\), supported in the larger angular
cone and equal to one in the smaller cone for large
frequency. Homogenization is explicit: apply a smooth
cutoff to \(\xi/|\xi|\) and multiply by a radial cutoff;
the smooth-root proof makes this map smooth off zero.
Take compact \(\varphi,\chi\), with \(\varphi=1\) near
\(y_0\) and \(\chi=1\) near \(\operatorname{supp}\varphi\).
Set
\[
 Q=\varphi(y)\gamma(D)\chi.
 \tag{W12}
\]
Its kernel has compact support in both base variables,
so it is proper. P2 O4 gives a full symbol
\(\varphi(y)\gamma(\xi)+S^{-\infty}\): in its amplitude
expansion every positive \(z\)-derivative of \(\chi(z)\)
vanishes on the support of \(\varphi\), and every
remainder has arbitrarily negative order.
Thus \(\operatorname{ess}(Q)\) lies in the prescribed
base/angular neighborhood and \(Q\) is elliptic at
\(\rho\), with principal symbol one nearby.

Moreover, for every distribution \(u\),
\[
 \rho\notin\operatorname{WF}(u-Qu).
 \tag{W13}
\]
Near \(y_0\), where \(\chi=\varphi=1\), the difference
equals \(v-\gamma(D)v\), \(v=\chi u\). Its Fourier
transform is \((1-\gamma)\widehat v\), zero at high
frequency in the smaller cone. Multiplying by a smaller
base cutoff preserves rapid decrease by W1, in its
polynomial-Fourier-transform version. This proves (W13).
If \(u\) was regular throughout the chosen cone, (W9)
and the essential-support bound make \(Qu\) smooth.

## W5. Iterated regularity has wavefront contained in the Lagrangian

If \(u\) satisfies the intrinsic word condition of T3, then
\[
 \operatorname{WF}(u)\subset\Lambda.
 \tag{W14}
\]
We give the proof with one fixed output cutoff for every
word length, so that arbitrarily high local regularity
is obtained on one neighborhood.

Fix \(\rho\notin\Lambda\). Closedness of \(\Lambda\)
permits a product of base and angular neighborhoods
whose closure is disjoint from \(\Lambda\).
Choose \(Q\) as in W4, supported in a smaller such product.
Choose a proper scalar operator
\[
 L=\varphi_1(y)\gamma_1(D)\langle D\rangle\chi_1
 \tag{W15}
\]
with the cutoffs equal to one on a neighborhood of the
essential support of \(Q\), but still with its principal
support disjoint from \(\Lambda\).
The principal symbol of \(L\) therefore vanishes on
\(\Lambda\); multiply by the identity for a vector bundle.
On a fixed cone about \(\operatorname{ess}(Q)\), its
full symbol equals \(\langle\xi\rangle\) modulo
\(S^{-\infty}\), by the same amplitude argument as W4.
P2's full product expansion shows, for every integer
\(N\ge1\), that the symbol of \(L^N\) equals
\(\langle\xi\rangle^N\) modulo \(S^{-\infty}\)
on that cone. Every term with a positive base derivative
of this frequency-only symbol vanishes.

Let \(q\) be a compact-base full symbol of \(Q\).
Quantize \(q(y,\xi)\langle\xi\rangle^{-N}\) with a
proper kernel cutoff equal to one near the diagonal;
call the result \(B_N\), of order \(-N\).
Its full symbol has that value modulo \(S^{-\infty}\).
On the cone just chosen, the composition expansion gives
the full symbol \(q\) for \(B_NL^N\), modulo smoothing.
Outside \(\operatorname{ess}(Q)\), \(q\) and every
derivative are smoothing, so every product coefficient
and remainder is smoothing there as well.
These two open sets cover all directions. Compact
localization and the finite-cover argument of T2 imply
\[
 \begin{gathered}
 R_N=B_NL^N-Q,\\
 R_N\ \hbox{has a smooth}\\
 \hbox{proper kernel}.
 \end{gathered}
 \tag{W16}
\]
All cutoffs may be taken in one fixed compact coordinate
region; their differences away from the diagonal are
smooth by P2 O4.

The word condition gives \(L^Nu\in B^s_{\mathrm{loc}}\).
P1 B6 applied to \(B_N\), and (W16), give
\(Qu\in B^{s+N}_{\mathrm{loc}}\) for every \(N\).
After any compact output cutoff, P1 B1 embeds this into
\(H^{s+N-1}\). For any derivative order \(k\), choose
\(N\) with \(s+N-1>k+n/2\); weighted Cauchy–Schwarz
then makes the inverse Fourier integral and its
derivatives of order at most \(k\) absolutely convergent.
This is the same Fourier proof as P1 B2 and shows
\(Qu\) is smooth. Equation (W13) now makes \(u\)
regular at \(\rho\), proving (W14). \(\square\)

## Two normalization checks with complete solutions

**Exercise T1.** In one dimension let \(\kappa(y)=2y\)
and \(A=D_y=-i\partial_y\). Determine the transported
operator and explain both Jacobians in (T8).

**Solution.** Since \(T_gf(y)=f(2y)\),
\(A^\kappa f(x)=2D_xf(x)\).
Here \(L=2\), so the symbol is \(a(2\eta)=2\eta\).
The frequency Jacobian is 2 and the input base Jacobian
is \(1/2\); their product is one. Omitting either would
give the wrong coefficient. For comparison,
\(T_\kappa\delta_0=2\delta_0\) as a scalar distribution:
(T3) evaluates the test \(2\psi(2y)\) at \(y=0\).
This scalar-density factor is distinct from the
principal-symbol cancellation. \(\square\)

**Exercise T2.** For
\(\kappa(y_1,y_2)=(y_1+(y_1^2+y_2^2)/2,y_2)\),
find the image of the covector \((\lambda,0)\) at
\((0,s)\), \(\lambda>0\), and check the principal symbol
of the transported \(D_{y_2}\).

**Solution.** On this curve,
\[
 D\kappa=\begin{pmatrix}1&s\\0&1\end{pmatrix},
 \qquad D\kappa^{-T}
       \begin{pmatrix}\lambda\\0\end{pmatrix}
       =\begin{pmatrix}\lambda\\-s\lambda\end{pmatrix}.
 \tag{W17}
\]
The new base point is \((s^2/2,s)\).
Formula (T5) takes the old symbol \(\xi_2\) to
\((D\kappa^T\eta)_2=s\eta_1+\eta_2\).
Direct differentiation of \(f(\kappa(y))\) gives
\(D_{y_2}(f\circ\kappa)
 =y_2(D_{x_1}f)\circ\kappa+(D_{x_2}f)\circ\kappa\).
The coefficient is on the left, as required by left
quantization. On the transformed conormal covector
\((\lambda,-s\lambda)\), this principal symbol vanishes.
Thus the operator and wavefront cotangent conventions
agree with the exact model in C6. \(\square\)

## Supplied scope and remaining localization

This component proves ordinary coordinate transport, invariance of the
intrinsic word condition under charts and frames, Fourier wavefront
covariance, proper microlocal cutoffs, pseudolocality, and (W14).
The converse using an arbitrary elliptic order-zero test still needs
the full conic parametrix and finite conic reconstruction.
Those proofs, the prescribed nondegenerate and clean phase converse,
the refined symbol order theorem and global Maslov data remain in
the original course scope. This component does not clear publication.
