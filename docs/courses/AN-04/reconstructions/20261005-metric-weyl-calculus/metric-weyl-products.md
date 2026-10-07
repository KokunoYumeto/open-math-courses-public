# Weyl products with controlled metric remainders

This companion proves the compatible two-metric symbol product, including all finite remainders and their bounded-set continuity. Its one-metric case supplies the order-two remainder needed for scalar positivity. The direct kernel construction and affine observable domains are included. The unrestricted converse Schwartz kernel theorem and the separate extensions for an unbounded cross parameter are not selected.

This is a modified selection of AN03-U004, *Two measuring scales, one Weyl product*, from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task. Original publisher: AN-03 local course project. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Selection, exact prerequisite connections and identified additions: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Original text: CC0.

## W0. Included prerequisites and conventions

The [complete metric localization proofs, Sections 1–4 and 7](../20261004-free-intrinsic-graph/prerequisites/metric-localization.md) give the exact cover, partition, symbol spaces and bounded compact approximants. The [complete Gaussian multiplier proofs, Sections 1–8](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) give the Fourier multiplier, diagonal restriction, differentiated estimates and every finite remainder. Their [quadratic-form foundation](../20261004-free-intrinsic-graph/prerequisites/quadratic-multiplier-foundations.md) proves the ellipsoid duality, volumes and affine substitutions. [Fourier L1–L3](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) and [measure M0–M8](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) give Plancherel, density, distributions and convergence. The [proof map](proof-map.json) connects the finite spectral, inverse, determinant, exponential and Taylor steps to their complete earlier programme proofs.

The convention is \(D=-i\partial\), and the Hilbert inner product is linear in its first argument. Distributions themselves pair bilinearly with tests. Operator identities for general metric symbols will be justified in the [action companion](weyl-action-and-covariance.md); the product construction below starts with Schwartz symbols.

Throughout, \(V\) is a real vector space of dimension \(n\geq1\), \(W=V\oplus V^*\), and
\[
\sigma((x,\xi),(y,\eta))=\langle\xi,y\rangle-\langle x,\eta\rangle.
\tag{W1}
\]
Measures on \(V\) and \(V^*\) are dual for Fourier inversion with coefficient \((2\pi)^{-n}\). Multiplying one measure by a positive constant divides the other by that constant; the phase-space measure and all quantizations below are unchanged.

## 1. Quadratic forms and the cross parameter

For a positive-definite quadratic form \(q\) on \(W\), define
\[
q^\sigma(T)=\sup_{S\ne0}\frac{|\sigma(T,S)|^2}{q(S)}.
\tag{W2}
\]
This is positive definite. Ordinary quadratic duality, composed with the invertible linear map induced by \(\sigma\), gives
\[
(q^\sigma)^\sigma=q,\qquad (c q)^\sigma=c^{-1}q^\sigma,
\qquad q\leq C r\ \Longleftrightarrow\ r^\sigma\leq Cq^\sigma.
\tag{W3}
\]
For example, write \(q(T)=T^tQT\) in coordinates and let \(J\) represent \(\sigma\). Then \(q^\sigma(T)=T^tJQ^{-1}J^tT\); substitution proves the first identity, and inversion of positive matrices proves the order reversal. Alternatively, all three follow by mapping the unit ellipsoid to its polar ellipsoid and using that taking the polar twice returns the original ellipsoid.

We will need an exact formula for the dual of a sum. If \(F_1,F_2\) are positive quadratic forms on a finite-dimensional space and primes denote ordinary dual forms, then
\[
(F_1+F_2)'(\zeta)
=\min_{\zeta_1+\zeta_2=\zeta}
\big(F_1'(\zeta_1)+F_2'(\zeta_2)\big).
\tag{W4}
\]
To prove it, represent the forms by positive matrices \(A_1,A_2\). Put \(v=(A_1+A_2)^{-1}\zeta\) and \(\zeta_j=A_jv\). Every other decomposition is \((\zeta_1+e,\zeta_2-e)\). Expanding its objective gives the value \(v^t(A_1+A_2)v\), plus \(e^t(A_1^{-1}+A_2^{-1})e\); the mixed terms cancel. The latter quantity is nonnegative and vanishes only at \(e=0\). This proves both the minimum and its value. In particular, if \(g=(g_1+g_2)/2\),
\[
g^\sigma(T)=2\min_{T_1+T_2=T}
\big(g_1^\sigma(T_1)+g_2^\sigma(T_2)\big).
\tag{W5}
\]
The factor two comes from the factor one half in the mean; it is not optional.

At one point of phase space, set
\[
h_j^2=\sup_{T\ne0}\frac{g_j(T)}{g_j^\sigma(T)},\qquad
H^2=\sup_{T\ne0}\frac{g_1(T)}{g_2^\sigma(T)}
=\sup_{T\ne0}\frac{g_2(T)}{g_1^\sigma(T)}.
\tag{W6}
\]
The two expressions for \(H\) are equal by (W3): each is the least constant in one of the equivalent inequalities \(g_1\leq H^2g_2^\sigma\), \(g_2\leq H^2g_1^\sigma\). These are also equivalent to
\[
|\sigma(T,S)|^2\leq H^2g_1^\sigma(T)g_2^\sigma(S).
\tag{W7}
\]
Indeed, divide by \(g_2^\sigma(S)\), take the supremum over \(S\), and use (W3).

For the mean metric, write \(h_g^2=\sup g/g^\sigma\). Then
\[
\max(h_1^2,h_2^2,H^2)\leq4h_g^2
\leq h_1^2+h_2^2+2H^2.
\tag{W8}
\]
For the first inequality, \(g_j\leq2g\) and \(g^\sigma\leq2g_k^\sigma\) show that \(g_j(T)/g_k^\sigma(T)\leq4g(T)/g^\sigma(T)\), for both choices of \(j,k\). For the second, \(2g=g_j+g_k\leq(h_j^2+H^2)g_j^\sigma\). Dualizing gives \(2g_j\leq(h_j^2+H^2)g^\sigma\). Add the two inequalities. No uncertainty inequality has been assumed in this argument.

## 2. Transport between compatible metrics

Let \(g_1,g_2\) be slowly varying metrics on \(W\), in the sense of [Localizing symbols with moving metrics](../20261004-free-intrinsic-graph/prerequisites/metric-localization.md). Write \(q_j(X)=g_{j,X}^\sigma\). Each metric is assumed symplectically temperate, meaning that for fixed constants \(C,N\), uniformly in \(X,Y,T\),
\[
q_j(X)(T)\leq Cq_j(Y)(T)
\big(1+q_j(Y)(X-Y)\big)^N.
\tag{W9}
\]
By (W3), this is equivalent to the primal inequality
\(g_{j,Y}\leq Cg_{j,X}(1+q_j(Y)(X-Y))^N\).
Constants can be enlarged so that a common \(C\geq1\), \(N\geq0\) works for both metrics. The bases of the quadratic distances matter.

The cross tests are
\[
\begin{split}
q_1(X)(T)&\leq Cq_1(Y)(T)
\big(1+q_2(X)(Y-X)\big)^N,\\
q_2(X)(T)&\leq Cq_2(Y)(T)
\big(1+q_1(X)(Y-X)\big)^N.
\end{split}
\tag{W10}
\]
We call the pair compatible when these hold. They require more than temperateness of each metric separately.

**Lemma 2.1 (metric transport).** Under (W9)–(W10), there are common constants \(C,L\) such that, for all \(j,k\in\{1,2\}\),
\[
q_j(X)\leq Cq_j(Y)\big(1+q_k(Y)(X-Y)\big)^L,
\quad
g_{j,Y}\leq Cg_{j,X}\big(1+q_k(Y)(X-Y)\big)^L.
\tag{W11}
\]
Moreover, with \(g=(g_1+g_2)/2\), there are \(C',L'\) such that
\[
g_{j,Y}\leq C'g_{j,X}
\big(1+g_Y^\sigma(X-Y)\big)^{L'},\qquad j=1,2.
\tag{W12}
\]
Consequently \(g\) is symplectically temperate.

**Proof.** For \(j=k\), the first estimate in (W11) is (W9). For \(j\ne k\), (W9) gives
\[
1+q_k(X)(X-Y)\leq C_0\big(1+q_k(Y)(X-Y)\big)^{N+1}.
\]
Insert this into (W10). Dualizing gives the second estimate in (W11).

Fix \(X,Y\), choose any intermediate point \(Z\), and put
\[
R=1+q_1(Y)(X-Z)+q_2(Y)(Z-Y).
\]
Use (W11) first on the segment from \(Z\) to \(Y\), with \(k=2\). It gives
\[
g_{j,Y}\leq Cg_{j,Z}R^L,
\qquad q_1(Z)(X-Z)\leq Cq_1(Y)(X-Z)R^L\leq CR^{L+1}.
\]
Use (W11) again on the segment from \(X\) to \(Z\), now with \(k=1\). Thus
\[
g_{j,Z}\leq Cg_{j,X}(1+q_1(Z)(X-Z))^L
\leq C_1g_{j,X}R^{L(L+1)}.
\]
Multiplication gives an exponent \(L^2+2L\). Minimize \(R\) using (W5); its minimum is \(1+g_Y^\sigma(X-Y)/2\). This proves (W12). Adding the two primal inequalities proves temperateness of the mean. It is also slowly varying: if \(g_X(Y-X)\) is sufficiently small, then \(g_{j,X}(Y-X)\leq2g_X(Y-X)\) is small for both metrics, and their slow-variation comparisons can be added. ∎

A positive weight \(m\) is symplectically temperate for \(g\) if it is \(g\)-continuous locally and
\[
m(Y)\leq Cm(X)\big(1+g_Y^\sigma(X-Y)\big)^N.
\tag{W13}
\]
Its reciprocal has the same property, with possibly larger exponent. In fact, apply (W13) with \(X,Y\) exchanged and use (W9) to replace the resulting distance based at \(X\) by a power of the distance based at \(Y\). Local comparability also reverses. Products and positive real powers are handled in the same way.

Suppose \(m_j\) is initially temperate for its own \(g_j\). The additional weight tests are
\[
m_1(Y)\leq Cm_1(X)(1+q_2(X)(X-Y))^N,
\quad
m_2(Y)\leq Cm_2(X)(1+q_1(X)(X-Y))^N.
\tag{W14}
\]
For a compatible pair, these are equivalent to both weights being temperate for the mean \(g\). Here is the full reduction. Own temperateness and (W14), with the distance-base conversion used above, give
\(m_j(Y)\leq Cm_j(X)(1+q_k(Y)(X-Y))^L\) for either \(k\). Repeat the two-segment proof of (W12), replacing its primal metric factor by \(m_j\); the estimate for \(q_1(Z)\) is unchanged. Minimization proves (W13) for the mean. Local \(g\)-continuity follows from \(g_j\)-continuity and \(g_j\leq2g\).

Conversely, \(g_Y^\sigma\leq2q_k(Y)\), followed by the distance-base conversion for \(g_k\), turns mean temperateness into (W14). If only mean temperateness and \(g_j\)-continuity were given at the outset, the same inequality with \(k=j\) also proves own temperateness. This explains the exact weight hypotheses used later.

## 3. What the diagonal test requires

On \(W\times W\), use the product metric and weight
\[
G_{(Y,Z)}(T,S)=g_{1,Y}(T)+g_{2,Z}(S),\qquad
M(Y,Z)=m_1(Y)m_2(Z).
\tag{W15}
\]
The product metric is slowly varying and the product weight is locally \(G\)-continuous, directly from the separate local comparisons.

Use dual coordinates \((p,q;r,s)\) and the auxiliary quadratic phase
\(A_0(p,q;r,s)=2(q\cdot r-p\cdot s)\).
Its symmetric map in the convention of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) sends
\((p,q;r,s)\) to \((-s,r;q,-p)\). Substitution in that lesson's definition of the phase-dual form gives
\[
G_{(Y,Z)}^{A_0}(T,S)=q_2(Z)(T)+q_1(Y)(S).
\tag{W16}
\]
Consequently \(G_{(X,X)}\leq H(X)^2G_{(X,X)}^{A_0}\), and \(H(X)^2\) is the least possible constant. Notice the interchange of the two metrics in (W16).

**Theorem 3.1 (diagonal criterion).** The product metric is uniformly \(A_0\)-temperate at the points \((X,X)\) if and only if (W10) holds. If the individual weights are temperate for their own metrics, the product weight is uniformly \(A_0,G\)-temperate there if and only if (W14) holds.

**Proof of necessity.** In dual form, metric temperateness on the diagonal says
\[
q_1(X)(T)+q_2(X)(S)
\leq C\big(q_1(Y)(T)+q_2(Z)(S)\big)\mathcal D^L,
\quad
\mathcal D=1+q_2(Z)(X-Y)+q_1(Y)(X-Z).
\tag{W17}
\]
Set \(Z=X,S=0\) to obtain the first cross test. Set \(Y=X,T=0\) for the second. The analogous product-weight inequality is
\(m_1(Y)m_2(Z)\leq Cm_1(X)m_2(X)\mathcal D^L\).
The same substitutions and cancellation of a positive factor give (W14).

**Proof of sufficiency.** We supply the distance comparison that is needed for this implication. For any single temperate metric \(g\), write \(q(U)=g_U^\sigma\), and let
\[
\mathcal E=1+q(Y)(X-Z)+q(Z)(X-Y),\qquad P=Y+Z-X.
\]
Because \(P-Z=Y-X\) and \(P-Y=Z-X\), temperateness gives
\[
q(P)(X-Y)\leq C\mathcal E^{L+1},\qquad
q(P)(X-Z)\leq C\mathcal E^{L+1}.
\]
For example, the first is the comparison of \(q(P)\) with \(q(Z)\), whose controlling distance \(P-Z\) is exactly \(-(X-Y)\). Compare \(q(Y)\) with \(q(P)\); the controlling distance \(Y-P=X-Z\) is bounded by the second estimate. Do the analogous comparison for \(q(Z)\). We obtain
\[
q(Y)(X-Y)+q(Z)(X-Z)\leq C'\mathcal E^{(L+1)^2}.
\tag{W18}
\]

Now take the mean metric from Section 2. Its dual is at most twice each \(q_j\), so \(\mathcal E\leq2\mathcal D\). Apply (W12) to \(g_{1,Y}/g_{1,X}\) and \(g_{2,Z}/g_{2,X}\), and then (W18). This yields
\[
g_{1,Y}(T)+g_{2,Z}(S)
\leq C''\big(g_{1,X}(T)+g_{2,X}(S)\big)\mathcal D^{L''}.
\]
It is precisely the primal phase-temperateness condition from Section 5 of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md). Dualization gives (W17). The weights are temperate for the mean by the preceding weight equivalence, so applying (W13) and (W18) also proves the product-weight condition. ∎

Taking \(g_1=g_2=g\) makes the cross tests consequences of ordinary symplectic temperateness and its distance-base conversion. Thus one temperate metric and any two temperate weights always satisfy the diagonal conditions, with parameter \(H=h_g\). This includes metrics and weights with no initial ordinary continuity.

## 4. Kernels and the Weyl normalization

For \(a\in\mathcal S(W)\) and \(\tau\in\mathbb R\), define
\[
\operatorname{Op}_\tau(a)u(x)
=(2\pi)^{-n}\iint e^{i\langle x-y,\xi\rangle}
a((1-\tau)x+\tau y,\xi)u(y)\,dy\,d\xi.
\tag{W19}
\]
The choices \(\tau=0,1,1/2\) are left, right and Weyl quantization. We write \(a^w=\operatorname{Op}_{1/2}(a)\).

These definitions extend to every tempered distribution \(a\). For example, put
\[
K_a(z+t/2,z-t/2)
=(2\pi)^{-n}\int e^{i\langle t,\xi\rangle}a(z,\xi)\,d\xi,
\qquad
a(z,\xi)=\int e^{-i\langle t,\xi\rangle}
K_a(z+t/2,z-t/2)\,dt.
\tag{W20}
\]
Both equalities are identities of tempered distributions: partial Fourier transformation and the invertible linear coordinate map \((z,t)\mapsto(z+t/2,z-t/2)\) are continuous isomorphisms of Schwartz space and its dual. The absolute determinant of this coordinate map is one.

For \(u,v\in\mathcal S(V)\), define \(\langle a^wu,v\rangle\) by applying \(K_a\) to \(u(y)\overline{v(x)}\). This is a continuous map \(\mathcal S\to\mathcal S'\). Indeed, each Schwartz seminorm of the test tensor is bounded by a product of finitely many seminorms of \(u,v\); a tempered distribution is bounded by a finite sum of such seminorms. For a bounded set of Schwartz tests, the finitely many test seminorms have a common bound, so the same estimate proves continuity into the strong distribution dual as well. The same construction works for every \(\tau\). It also gives the usual weak integral interpretation of (W19). Only this direct symbol-to-kernel construction is needed here; no converse description of all continuous operators is being invoked.

For a finite polynomial in frequency, \(a(x,\xi)=\sum_\alpha a_\alpha(x)\xi^\alpha\), left and right quantization put the coefficients on the corresponding sides:
\[
\operatorname{Op}_0(a)u=\sum_\alpha a_\alpha D^\alpha u,
\qquad
\operatorname{Op}_1(a)u=\sum_\alpha D^\alpha(a_\alpha u).
\]
This remains valid for coefficients \(a_\alpha\in\mathcal S'(V)\) and \(u\in\mathcal S(V)\). Indeed, the inverse Fourier transform of \(\xi^\alpha\) is \(D_t^\alpha\delta(t)\). In the left kernel the coefficient is evaluated at \(x\), so pairing this delta derivative against the input differentiates \(u\); in the right kernel it is evaluated at \(y\), so the output derivative acts on the entire product \(a_\alpha u\). These kernels are defined by tensor products followed by invertible linear coordinate changes, and multiplication of a tempered coefficient by the smooth Schwartz input is well defined. No product of two arbitrary distributions is used.

Taking the complex conjugate and exchanging \(x,y\) in (W20) proves
\[
(a^w)^*=(\overline a)^w.
\tag{W21}
\]
Here the adjoint is the distributional sesquilinear adjoint on Schwartz functions. A real symbol therefore gives a symmetric Schwartz-domain operator whenever it has values in \(L^2\). Equation (W21) alone makes no assertion of selfadjoint closure for a general real symbol.

## 5. Affine observables and their unitary groups

For smooth symbols define
\[
\{a,b\}=\partial_\xi a\cdot\partial_xb-
\partial_xa\cdot\partial_\xi b.
\tag{W22}
\]
When one factor is affine, this is also defined for distributional other factors. Directly from (W20), multiplication of the output by \(x_j\) and differentiation by \(D_{x_j}\) give
\[
x_j a^w=(x_ja+\tfrac i2\partial_{\xi_j}a)^w,
\qquad
D_{x_j}a^w=(\xi_ja+\tfrac1{2i}\partial_{x_j}a)^w.
\]
For the first formula, write the output coordinate as \(z_j+t_j/2\), and integrate the \(t_j\) factor by parts in \(\xi_j\). For the second, \(\partial_{x_j}=\frac12\partial_{z_j}+\partial_{t_j}\) on the kernel. These operations on distributions are legitimate by duality. Linearity gives, for every affine \(L\),
\[
L^w a^w=\big(La+\{L,a\}/(2i)\big)^w.
\tag{W23}
\]

**Proposition 5.1 (affine unitary group).** For real affine \(L(x,\xi)=b\cdot x+c\cdot\xi+d\), the operator \(L^w=b\cdot x+c\cdot D+d\), initially on \(\mathcal S(V)\), is essentially selfadjoint. Its unitary group is
\[
U_tu(x)=e^{itd+it b\cdot x+it^2 b\cdot c/2}u(x+tc),
\qquad U_t=(e^{itL})^w.
\tag{W24}
\]

**Proof.** We first obtain the \(L^2\) Fourier transform from the Schwartz Plancherel prerequisite. The normalized transform \(\mathcal F_0=(2\pi)^{-n/2}\mathcal F\) is an isometry on \(\mathcal S\). If \(u_j\to u\) in \(L^2\), with \(u_j\in\mathcal S\), then \(\mathcal F_0u_j\) is Cauchy in \(L^2\); completeness defines its limit, independently of the approximating sequence. Density therefore extends \(\mathcal F_0\) to an isometry on all of \(L^2\). The normalized inverse extends by the same argument. Their compositions are the identity on the dense Schwartz subspace, hence on \(L^2\) by continuity. Thus the extension is unitary, using precisely Schwartz Plancherel and the declared density/completeness prerequisites.

Multiplication by a real linear function \(\ell\) on \(L^2\), with domain \(\{u:\ell u\in L^2\}\), is selfadjoint. If a vector lies in the adjoint domain, testing against compactly supported smooth functions identifies its adjoint value as \(\ell u\), so it belongs to the displayed domain; the reverse inclusion follows by integration. Compact cutoff followed by smooth convolution approximates every domain vector in the graph norm: on a fixed compact set \(\ell\) is bounded, and the error in commuting convolution past \(\ell\) is bounded by the mollifier radius times \(|\nabla\ell|\|u\|_2\). Thus \(C_c^\infty\), and hence \(\mathcal S\), is a core. The unitary Fourier transform gives the same conclusion for \(c\cdot D\), because its Fourier transform is multiplication by \(c\cdot\xi\).

If \(c=0\), this already proves the assertion. If \(c\ne0\), choose orthonormal coordinates with \(c=(\gamma,0,\ldots,0)\), \(\gamma>0\), and put
\[
\phi(x)=\gamma^{-1}
\left(b_1x_1^2/2+x_1\sum_{j>1}b_jx_j\right).
\]
Multiplication by \(e^{i\phi}\) is unitary and preserves Schwartz space, as does its inverse. Since \(c\cdot\nabla\phi=b\cdot x\),
\[
e^{-i\phi}(c\cdot D)e^{i\phi}=c\cdot D+b\cdot x.
\]
Unitary conjugation preserves selfadjointness and the core property. Addition of the real constant \(d\) completes the closure argument.

The formula for \(U_t\) in (W24) is unitary, preserves \(\mathcal S\), and obeys \(U_tU_s=U_{t+s}\). Its derivative on \(\mathcal S\) is \(iL^wU_t\). It is also the exponential of the closure just constructed: conjugate the translation group for \(c\cdot D\) by \(e^{i\phi}\); the identity
\(\phi(x+tc)-\phi(x)=t b\cdot x+t^2b\cdot c/2\)
gives exactly (W24). The pure multiplication case is immediate. Strong continuity follows from continuity of translations in \(L^2\), first for compactly supported smooth functions and then by density and the unitary norm bound. Finally, substituting \(e^{itL}\) into the distributional kernel formula sets \(y=x+tc\) and gives the same phase. ∎
**Editorial domain calculation in the original coordinates.** The affine proof can also retain the original vectors throughout. In the fixed original coordinates and density, let \(c\ne0\) and define
\[
 \phi_c(x)=\frac{(b\cdot x)(c\cdot x)}{|c|^2}
       -\frac{(b\cdot c)(c\cdot x)^2}{2|c|^4},\qquad
 M_cu=e^{i\phi_c}u.
 \tag{WA1}
\]
Both terms, including the possibly zero second term, remain. Direct differentiation gives
\[
 c\cdot\nabla\phi_c(x)=
 \frac{(b\cdot c)(c\cdot x)+(b\cdot x)|c|^2}{|c|^2}
 -\frac{(b\cdot c)\,2(c\cdot x)|c|^2}{2|c|^4}=b\cdot x.
 \tag{WA2}
\]
The original Fourier transform and inverse, with their full \((2\pi)^n\) norm identity and \((2\pi)^{-n}\) inverse factor, define the closed selfadjoint operator \(D_c=c\cdot D\) on
\[
 D(D_c)=\{u\in L^2(V):c\cdot\partial u\in L^2(V)
                         \text{ as a distribution}\}.
 \tag{WA3}
\]
Indeed the actual transform sends this distributional derivative to multiplication by \(ic\cdot\xi\); the multiplication-domain proof above and the full inverse transform give both inclusions of (WA3) and the selfadjoint domain. Its core is the inverse image of the multiplication core; that image lies in the original Schwartz space and is graph dense. Both Fourier norm factors remain in this comparison, as proved in [the Fourier prerequisite](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) with its complete Plancherel and distributional receiving maps.

The map \(M_c\) and its inverse are unitary for the original \(L^2\) measure and continuous inverse maps of the original Schwartz space: each derivative is a finite polynomial times the same modulus-one exponential. The distributional product rule and (WA2) prove the exact domain and action
\[
 \begin{aligned}
 D(\overline{L^w})&=\{u\in L^2:
            c\cdot Du+(b\cdot x+d)u\in L^2
                          \text{ as a distribution}\},\\
 \overline{L^w}&=M_c^{-1}D_cM_c+dI
       \quad\text{on that entire domain}.
 \end{aligned}
 \tag{WA4}
\]
The displayed sum is the condition; its two unbounded summands need not separately lie in \(L^2\). Equivalence with \(M_cu\in D(D_c)\) follows by subtracting the actual bounded term \(du\) and applying both directions of the distributional product rule. Unitary conjugation and the proved original core give selfadjointness and essential selfadjointness on \(\mathcal S\). No rotation or replacement vector is required. Moreover,
\[
 \begin{aligned}
 \phi_c(x+tc)-\phi_c(x)
 &=\frac{(b\cdot x+t b\cdot c)(c\cdot x+t|c|^2)
            -(b\cdot x)(c\cdot x)}{|c|^2}\\
 &\quad-\frac{(b\cdot c)((c\cdot x+t|c|^2)^2-(c\cdot x)^2)}{2|c|^4}
 =t b\cdot x+t^2 b\cdot c/2.
 \end{aligned}
 \tag{WA5}
\]
Thus both ordered conjugation maps recover (W24), its original phase and translation. For \(c=0\) the full domain is \(\{u:(b\cdot x+d)u\in L^2\}\), by the same multiplication proof. If also \(b=0\), this is all \(L^2\), with the exact scalar action \(dI\).

For later use write \(P=(p,q)\in W^*\) and let \(E_P(x,\xi)=e^{i(p\cdot x+q\cdot\xi)}\). The preceding calculation gives
\[
E_P^wu(x)=e^{ip\cdot(x+q/2)}u(x+q),\quad
E_P^wE_Q^w=e^{i\sigma(P,Q)/2}E_{P+Q}^w,
\quad \sigma(P,Q)=q\cdot r-p\cdot s
\tag{W25}
\]
for \(Q=(r,s)\). The last scalar factor follows by subtracting the phase of \(E_{P+Q}^w\) from the phase of the composite. Fourier inversion expresses a Schwartz symbol as a superposition of the \(E_P\)'s with integrable coefficient \((2\pi)^{-2n}\widehat a(P)\). Thus (W24), together with continuity in the symbol distribution, characterizes Weyl quantization. This claim uses the Fourier representation of arbitrary Schwartz symbols and its dual extension; it does not require pointwise Fourier integrability for every tempered distribution.

## 6. The exact Weyl product for Schwartz symbols

Let
\[
\mathcal A(P,Q)=\sigma(P,Q)/2,
\qquad
C_j(a,b)(X)=\frac1{j!}
\left[(i\mathcal A(D_X,D_Y))^j(a(X)b(Y))\right]_{Y=X}.
\tag{W26}
\]
For \(a,b\in\mathcal S(W)\), (W25) and Fourier inversion give
\[
a\#b=\left[e^{i\mathcal A(D_X,D_Y)}(a\otimes b)\right]_{Y=X},
\qquad (a\#b)^w=a^wb^w.
\tag{W27}
\]
All integrals of Fourier coefficients in this derivation are absolutely convergent; the plane-wave operators have \(L^2\) norm one. The resulting symbol is Schwartz, since the quadratic multiplier preserves \(\mathcal S(W\times W)\), and restriction to the diagonal preserves Schwartz space.

An equivalent formula, with no Fourier transforms left in it, is
\[
(a\#b)(X)=\pi^{-2n}\iint
a(X+S)b(X+T)e^{2i\sigma(T,S)}\,dS\,dT.
\tag{W28}
\]
For clarity about the constant and sign, the distributional Fourier transform of the kernel \(\pi^{-2n}e^{2i\sigma(T,S)}\), evaluated on the Fourier exponentials \(e^{iP\cdot S+iQ\cdot T}\), is \(e^{i\sigma(P,Q)/2}\). Indeed, integration in \(S\) imposes \(T=(q/2,-p/2)\). Its Jacobian is \(2^{-2n}\), so the coefficient is \(\pi^{-2n}(2\pi)^{2n}2^{-2n}=1\); the remaining phase is \((q\cdot r-p\cdot s)/2\). This calculation is an identity of tempered distributions, tested against Schwartz functions; it can equally be justified by Gaussian regularization and passage to that topology. Since the integrand in (W28) has integrable absolute value for Schwartz factors, the identity gives the ordinary integral as written.

The first two coefficients are
\[
C_0(a,b)=ab,\qquad C_1(a,b)=\{a,b\}/(2i).
\tag{W29}
\]
In fact, replacing each \(D\) by \(-i\partial\) in \(i\mathcal A(D_X,D_Y)\) gives exactly the second expression. The sign agrees with the affine identity (W23).

There are two related quadratic phases in this proof. The auxiliary phase of (W16) is \(A_0=2\sigma\); the actual multiplier in (W27) is \(\mathcal A=\sigma/2=A_0/4\). With the convention \(A(\Xi)=\langle B\Xi,\Xi\rangle\) fixed in [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md),
\[
G^{\mathcal A}=16G^{A_0},\qquad
h_{G,\mathcal A}(X,X)=H(X)/4.
\tag{W30}
\]
Scaling a quadratic phase by \(t\ne0\) scales its symmetric map by \(t\), hence its phase-dual form by \(t^{-2}\). This proves (W30) directly. Keeping these phases distinct prevents a normalization error in applying the Gauss estimate.

## 7. Products with distinct metrics

**Theorem 7.1 (distinct-metric Weyl product).** Let \(g_1,g_2\) be symplectically temperate, compatible metrics. Suppose \(H(X)\leq1\) everywhere, with \(H\) as in (W6). Set \(g=(g_1+g_2)/2\). Let \(m_j\) be positive, \(g_j\)-continuous weights, both symplectically temperate for \(g\). Then (W27) has a unique weakly continuous bilinear extension
\[
\#:\ S(m_1,g_1)\times S(m_2,g_2)\longrightarrow S(m_1m_2,g).
\tag{W31}
\]
For every integer \(N\geq0\),
\[
R_N(a,b)=a\#b-\sum_{j<N}C_j(a,b)
\quad\hbox{belongs to}\quad S(H^Nm_1m_2,g).
\tag{W32}
\]
These maps are continuous in the respective Fréchet symbol topologies and continuous on products of bounded source sets with their local smooth topologies. For every target derivative order \(k\), there is a finite \(J\) such that
\[
p_k(R_N(a,b);H^Nm_1m_2,g)
\leq C_{N,k}
p_{\leq J}(a;m_1,g_1)p_{\leq J}(b;m_2,g_2).
\tag{W33}
\]
Constants depend on the fixed dimension, orders and structural metric/weight constants. Individual inequalities \(g_j\leq g_j^\sigma\) and the mean inequality \(g\leq g^\sigma\) are not hypotheses.

**Proof.** Use \(G,M\) from (W15). The weight equivalence in Section 2 implies the own and cross weight conditions needed by Theorem 3.1. That criterion gives uniform temperateness along the diagonal for the auxiliary phase. By (W30), the same inequalities hold for the actual phase: its dual distances are larger, so the right sides of the required upper bounds only increase. Also \(G\leq G^{\mathcal A}\) on the diagonal because \(H/4\leq1\).

The tensor map \((a,b)\mapsto a\otimes b\) is a continuous bilinear map into \(S(M,G)\). To check this without coordinate assumptions, split every direction in \(W\times W\) into its two components. If its \(G\)-length is at most one, each component has length at most one for its corresponding metric. The multilinear product rule has at most \(2^l\) terms at derivative order \(l\), so
\[
p_l(a\otimes b;M,G)
\leq2^l p_{\leq l}(a;m_1,g_1)p_{\leq l}(b;m_2,g_2).
\tag{W34}
\]
The tensor map also preserves boundedness and local smooth convergence.

Apply Theorems 7.1 and 8.1 of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) on the linear diagonal subspace. The metric induced there by \(G\) is \(g_1+g_2=2g\), which defines the same symbol space as \(g\), with the factor \(2^{k/2}\) in order \(k\). The restricted weight is \(m_1m_2\), and the remainder factor in (W30) is \((H/4)^N\). The harmless fixed factor \(4^{-N}\) is absorbed in the seminorm bound. Equations (W31)–(W33) follow from the Gauss theorem and (W34).

The weight \(H\) is positive and locally \(g\)-continuous. Positivity follows from nondegeneracy in (W6); local comparison follows by comparing both metrics at nearby points and dualizing. It is also temperate for the mean: (W12) gives \(g_{j,Y}\leq Cg_{j,X}R^L\), where \(R=1+g_Y^\sigma(X-Y)\); dualizing the estimate for \(j=2\) gives \(q_2(Y)\geq C^{-1}q_2(X)R^{-L}\). Hence \(H(Y)\leq CH(X)R^L\). Thus the target weights in (W32) satisfy the asserted local and global conditions.

Finally, [Approximation on compact sets](../20261004-free-intrinsic-graph/prerequisites/metric-localization.md#7-approximation-on-compact-sets) gives compactly supported approximants to both input symbols that remain bounded and converge locally smoothly. For those approximants the definition agrees with (W27). Weak continuity passes to their limit and gives uniqueness. This is a bounded-set argument, rather than an incorrect claim of compact-support density in the full Fréchet topology. ∎

## W8. Source and receiving scope

The selected AN03-U004 arguments retain W1–W34 and WA1–WA5. The compatible-metric and cross-weight hypotheses, the bound \(H\le1\), all finite remainders and every topology in Theorem 7.1 are unchanged. The exact affine domains are also retained. The approved mathematical antecedents are Hörmander, *The Analysis of Linear Partial Differential Operators III*, 2007 eBook, ISBN 978-3-540-49938-1, §18.5, especially Propositions 18.5.2–3 and Theorems 18.5.4–5 (printed 153–156; PDF 168–171). The programme proofs give their full dual-of-a-sum, distance-base and Gaussian normalization calculations. No book text or files are included.

For scalar \(b\), the first correction to \(b\#b\) vanishes because \(\{b,b\}=0\). The order-two remainder is therefore precisely in \(S(h^2m^2,g)\) when \(b\in S(m,g)\) and \(g\le g^\sigma\). This is a symbol assertion. A bounded-operator conclusion additionally needs the operator bound in its actual metric; the Fefferman–Phong theorem is not inferred from the symbol assertion alone.
