# From Weyl symbols to operators and changes of coordinates

A symbol product becomes an operator calculus only after its factors act on a common space. We first prove that every symplectically temperate symbol acts on Schwartz functions and tempered distributions. The proof measures how far each localized symbol lies from the origin in a norm adapted to both differentiation and multiplication. We then use this operator calculus to study conformal changes of scale, affine symplectic coordinates and changes of quantization.

We use the symbol seminorms and localization of [AN03-U001](metric-localization.md), the quadratic Fourier multipliers of [AN03-U002](gauss-transform-estimates.md), the exact Fourier interfaces of [AN03-P001](prerequisite-bridges.md), and the Weyl formulas of [AN03-U004](weyl-metric-products.md). The convention is \(D=-i\partial\), on \(W=\mathbb R_x^n\oplus\mathbb R_\xi^n\), \(n\ge1\), with
\[
\sigma((x,\xi),(y,\eta))=\xi\cdot y-x\cdot\eta.
\tag{A1}
\]
Write \(q_X=g_X^\sigma\). A symplectically temperate metric is slowly varying and satisfies, with \(C\ge1\), \(N\ge0\),
\[
q_X(T)\le Cq_Y(T)(1+q_Y(X-Y))^N.
\tag{A2}
\]
A weight is positive, locally \(g\)-continuous, and satisfies
\(m(Y)\le Cm(X)(1+q_Y(X-Y))^N\), with its own constants.

The additional entry requirements are completeness and compact smooth density in \(L^2\), and the usual Lebesgue convergence theorems, as in AN03-U004. The needed Hilbert-space integrals are constructed below. For the assertion about bounded sets in the strong distribution dual we use complete-metric Baire; the exact reading is specified at the end. We prove its needed consequence below. No Schwartz kernel theorem is needed for the direct constructions in this unit: AN03-U004 already defines the symbol-to-kernel map by Fourier transformation.

## AN03-WCA-001 — Polynomial control and the two topologies

Let \(e(X)=|X|^2\) in the fixed canonical coordinates; \(e^\sigma=e\). Constants in comparisons with \(e\) may depend on the forms at the origin. There is a finite \(K\) such that
\[
C^{-1}(1+|X|^2)^{-K}e
\le g_X,q_X\le C(1+|X|^2)^K e,
\qquad
C^{-1}(1+|X|^2)^{-K}\le m(X)\le C(1+|X|^2)^K.
\tag{A3}
\]
These statements require no uncertainty inequality.

Indeed, (A2) with \(Y=0\) bounds \(q_X\) by a fixed form times a power of \(1+|X|^2\). In particular \(q_X(X)\) has such a bound. The primal version of (A2), with the other point at the origin, now gives
\(g_X\le Cg_0(1+q_X(X))^N\).
Dualizing the two upper bounds gives both lower bounds. The weight inequality with one point at zero gives its upper bound. Its reciprocal is temperate by AN03-WP-002, giving the lower bound. Enlarging a common \(K\) proves (A3).

Consequently every coordinate derivative of \(a\in S(m,g)\) has polynomial growth, with degree allowed to depend on the derivative order. In particular \(a\) defines a tempered distribution. On a bounded symbol set the growth bound for each fixed derivative is uniform. Thus bounded symbols converging in \(C^\infty_{\rm loc}\) converge in \(\mathcal S'\): pair their zeroth-order common polynomial bound with the rapid decay of a test function, and apply dominated convergence. We call this bounded-set local-smooth topology the **weak symbol topology**, as in AN03-U002.

For \(u\in\mathcal S(\mathbb R^n)\), use the increasing norms
\[
Q_r(u)=\sum_{|\alpha|+|\beta|\le r}\|x^\alpha D^\beta u\|_2.
\tag{A4}
\]
They define the usual Schwartz topology. One direction follows by integrating a sufficiently rapidly decreasing bound. For the other, choose an integer \(s>n/2\). Fourier inversion, Cauchy–Schwarz and Schwartz Plancherel give
\[
\|v\|_\infty\le (2\pi)^{-n}\|\widehat v\|_1
\le C_s\sum_{|\gamma|\le s}\|D^\gamma v\|_2.
\tag{A5}
\]
Apply this to \(v=x^\alpha D^\beta u\) and expand its derivatives. This controls every usual Schwartz seminorm by a finite \(Q_r\). The familiar completeness of Schwartz space also follows directly: uniform limits of all weighted derivatives are compatible derivatives by the fundamental theorem of calculus on coordinate boxes.

On the complex-linear distribution dual \(\mathcal S'\) we use the **strong dual topology**. In particular, the distribution bracket is linear in its test function; Hilbert-space adjoints will be converted to bilinear transposes explicitly. The strong-dual seminorms are
\[
p_B(u)=\sup_{\phi\in B}|\langle u,\phi\rangle|,
\tag{A6}
\]
where \(B\) ranges over bounded subsets of \(\mathcal S\). A bounded subset \(\mathcal U\) of this dual satisfies a common finite-order estimate
\[
|\langle u,\phi\rangle|\le C Q_r(\phi)
\quad(u\in\mathcal U,\ \phi\in\mathcal S).
\tag{A7}
\]
Here is the Baire argument, including the point where that prerequisite enters. Strong boundedness gives pointwise boundedness on each \(\phi\). The closed sets
\(\{\phi:\sup_{u\in\mathcal U}|\langle u,\phi\rangle|\le j\}\), \(j=1,2,\ldots\), cover the complete metrizable space \(\mathcal S\). One has interior. Subtract two points in a small neighborhood inside it to obtain a uniform bound on a neighborhood of zero. That neighborhood contains a set \(Q_r<\varepsilon\); rescaling proves (A7). No assertion of joint continuity of the unrestricted distribution action follows from this argument.

## AN03-WCA-002 — An affine-invariant Fourier norm

For \(a\in\mathcal S(W)\), set
\[
\|a\|_{\mathcal F L^1}=(2\pi)^{-2n}\|\widehat a\|_{L^1(W^*)}.
\tag{A8}
\]
Then
\[
\|a^w\|_{L^2\to L^2}\le \|a\|_{\mathcal F L^1}.
\tag{A9}
\]
To prove it, write \(a\) by Fourier inversion as the integral of plane waves. AN03-WP-005 gives norm-one operators for every such wave. For \(u\in\mathcal S\), their actions depend continuously on the wave frequency in \(L^2\), by the explicit translation and modulation formulas. Multiply this continuous Hilbert-space-valued function by \(\widehat a\). On every compact cube its Riemann sums converge in \(L^2\): uniform continuity makes the difference between any two sufficiently fine sums arbitrarily small, and \(L^2\) is complete. The norm of each resulting integral is at most the integral of \(|\widehat a|\|u\|_2\). This also bounds differences between integrals over increasing cubes, whose tails tend to zero because \(\widehat a\in L^1\). It constructs the full integral in \(L^2\) and proves its triangle inequality. Pairing with a Schwartz test and using scalar Fourier inversion identifies it with \(a^wu\). Formula (A9) follows, first on Schwartz inputs and then on \(L^2\) by density. Thus no estimate for a general oscillatory kernel or general vector-valued integration theorem is being assumed.

This norm is unchanged by any invertible affine change of the phase-space variables, even one that is not symplectic. If \(b(X)=a(TX+Z)\), then
\[
\widehat b(\Theta)
=|\det T|^{-1}e^{i\langle T^{-t}\Theta,Z\rangle}
\widehat a(T^{-t}\Theta).
\]
Changing variables in its \(L^1\) norm cancels the determinant.

It is also controlled by finitely many Schwartz seminorms. More particularly, if \(a\) is supported in a fixed-radius ball for a positive form \(Q\), centered at \(X_0\), then
\[
\|a^w\|\le C\sum_{j\le s}\sup_X|a|_{j,Q}(X),
\qquad s>n\text{ an integer}.
\tag{A10}
\]
Use an affine map making \(Q\) Euclidean and its center zero. The Fourier \(L^1\) estimate used in (A5), now in dimension \(2n\), requires \(s>(2n)/2=n\). On the fixed support, the derivative \(L^2\) norms are bounded by their suprema. Affine invariance proves (A10) with no determinant of \(Q\) left over.

## AN03-WCA-003 — Distance, division and counting

Choose the partition \((\phi_\nu)\) of AN03-U001 and fixed radii
\(0<a<b<c<r_*\), with supports in \(B_{X_\nu}(a)\). Put
\[
g_\nu=g_{X_\nu},\quad m_\nu=m(X_\nu),\quad
U_\nu=B_{X_\nu}(b),\quad U'_\nu=B_{X_\nu}(c),\quad
a_\nu=\phi_\nu a.
\]
The larger balls have bounded multiplicity. Localization gives
\(\sup|a_\nu|_{j,g_\nu}\le C_jm_\nu p_{\le j}(a;m,g)\).
The notation \(p_{\le j}\) denotes the sum of symbol seminorms of orders at most \(j\).

The form
\[
r_\nu=(e+g_\nu)^\sigma,\qquad
r_\nu(Y)=\min_{Y=U+V}\big(g_\nu^\sigma(U)+|V|^2\big),
\qquad
R_\nu=\inf_{Y\in U_\nu}r_\nu(Y)^{1/2}
\tag{A11}
\]
uses the dual-of-a-sum identity proved in AN03-WP-001. There is no factor2 here, since the primal form is a sum rather than a mean. All forms are positive definite and the balls nonempty, so \(R_\nu\) is finite; it can be zero.

One may replace \(e\) throughout this construction by any fixed positive form \(e_0\). There are constants \(c,C>0\) with \(ce\le e_0\le Ce\). Adding \(g_\nu\), and then dualizing, shows that \((e_0+g_\nu)^\sigma\) and \(r_\nu\) are comparable with constants independent of \(\nu\). Their distances and center-growth bounds are consequently equivalent. Choosing canonical Euclidean coordinates therefore imposes no restriction on the reference form.

**Localized decay.** For each integer \(M\ge0\) there is a finite \(J_M\) such that
\[
\|a_\nu^w u\|_2
\le C_Mm_\nu(1+R_\nu)^{-M}
p_{\le J_M}(a;m,g)Q_M(u).
\tag{A12}
\]
The constants are uniform in \(\nu\).

Here are the geometric and differential details. If \(R_\nu>0\), minimize the \(r_\nu\)-norm on the compact closure of \(U_\nu\). Let \(P\) be a minimizing point. Differentiating along each segment from \(P\) into that closed ellipsoid gives a supporting linear form
\[
L(Y)=r_\nu(P,Y)/r_\nu(P)^{1/2}
=\sigma(Y,t),\qquad
e(t)+g_\nu(t)=1,\qquad
L(Y)\ge R_\nu\quad(Y\in U_\nu).
\tag{A13}
\]
The normalization follows by ordinary quadratic duality, composed with \(\sigma\). In particular \(L_\nu=L(X_\nu)\ge R_\nu\). Positivity on the \(g_\nu\)-ball of radius \(b\) gives
\(\sqrt{g_\nu^\sigma(t)}\le L_\nu/b\).
On the support ball of radius \(a\), therefore,
\(L\ge(1-a/b)L_\nu\).
Differentiating the reciprocal shows explicitly that
\[
\sup|L_\nu/L|_{k,g_\nu}
\le k!\,b^{-k}(1-a/b)^{-k-1}.
\tag{A14}
\]
Division of a supported smooth symbol by \(L\), followed by extension by zero outside \(U_\nu\), is consequently smooth and preserves its support.

The affine Weyl identity of AN03-WP-005, used on the right, is
\[
a_\nu^wu
=(a_\nu/L)^w L^wu
+\frac{i}{2}\{a_\nu/L,L\}^wu,
\qquad
\{a_\nu/L,L\}=-L^{-1}\partial_t a_\nu.
\tag{A15}
\]
There is no derivative of \(L\) in the last expression, since
\(\partial_t L=\sigma(t,t)=0\).
Both new symbols have frozen seminorm bounds with weight
\(m_\nu/L_\nu\); the differentiated one uses one additional source derivative and \(g_\nu(t)^{1/2}\le1\). Repeat (A15) \(M\) times. Every resulting symbol has weight \(m_\nu L_\nu^{-M}\), and every input is \((L^w)^j u\) with \(j\le M\). Since \(|t|\le1\), expanding these powers and commuting coordinates and derivatives bounds their \(L^2\) norms by \(C_MQ_M(u)\). Apply (A10) to each of the finitely many terms. This proves (A12) when \(R_\nu>1\). For \(R_\nu\le1\), (A10) itself proves it after enlarging the constant. Thus zero distance causes no division by zero.

**Polynomial counting.** There are finite constants \(B,P,C\) such that
\[
|X_\nu|^2\le C(1+R_\nu^2)^B,\qquad
\#\{\nu:R_\nu\le r\}\le C(1+r)^P.
\tag{A16}
\]
Consequently
\[
\sum_\nu(1+R_\nu)^{-L}<\infty\qquad(L>P).
\tag{A17}
\]

We give the missing volume argument in full. Let \(T\ge1\) and \(R_\nu^2\le T\). Choose \(Y\in U_\nu\) with \(r_\nu(Y)\le2T\), and take a minimizing decomposition \(Y=U+V\) in (A11). Then
\(g_\nu^\sigma(U)\le2T\) and \(|V|^2\le2T\).
Slow variation gives \(q_Y(U)\le C T\). Formula (A2), comparing \(V\) to \(Y\), implies
\[
q_V\le CT^Nq_Y,\qquad q_V(U)\le CT^{N+1}.
\tag{A18}
\]
By (A3), both \(g_V\) and \(q_V\) lie between
\(C^{-1}T^{-K}e\) and \(CT^Ke\). Hence
\(|U|^2\le CT^{K+N+1}\).
Applying (A2) in the other direction, with its now controlled distance \(q_V(U)\), gives
\[
q_Y\le CT^{K+N(N+1)}e,
\qquad
g_Y\le CT^{K+N}e.
\tag{A19}
\]
Dualizing supplies the lower bounds as well. Take, for example,
\(B=K+(N+1)^2\), enlarged if needed to absorb the preceding fixed exponents. Local comparison with \(g_\nu\), and
\(g_\nu(X_\nu-Y)<b^2\), now give
\[
C^{-1}T^{-B}e\le g_\nu\le CT^Be,\qquad
|Y|^2+|X_\nu|^2\le CT^B.
\tag{A20}
\]

A Euclidean ball centered at this \(Y\) with radius
\(\kappa T^{-B/2}\) lies in \(U'_\nu\), for a fixed small \(\kappa>0\), because its \(g_\nu\)-radius is less than the gap \(c-b\). These small balls inherit the bounded multiplicity of \(U'_\nu\), while all lie in one Euclidean ball of radius \(C T^{B/2}\). Integrating their characteristic functions bounds the number of indices by \(CT^{2nB}\). The argument applies first to every finite subcollection, so it bounds the whole index set. This proves (A16), for example with \(P=4nB\). Its center bound follows by taking \(T=1+R_\nu^2\). Finally split the indices into dyadic bands of \(1+R_\nu\); their contributions in (A17) form a geometric series when \(L>P\). No uncertainty assumption or bound on a vertical part of the metric was used.

## AN03-WCA-004 — The full Schwartz and distribution action

**Theorem.** If \(g\) is symplectically temperate and \(m\) is a temperate weight for \(g\), then
\[
a^w:\mathcal S\longrightarrow\mathcal S,\qquad
a^w:\mathcal S'\longrightarrow\mathcal S'
\quad(a\in S(m,g))
\tag{A21}
\]
are continuous. For each \(r\) there are finite \(J,t\) such that
\[
Q_r(a^wu)\le C_r p_{\le J}(a;m,g)Q_t(u).
\tag{A22}
\]
The first action is jointly continuous in symbol and function. Both actions depend continuously on a bounded symbol set with its weak symbol topology, uniformly on bounded sets of inputs, using the Schwartz topology or the strong distribution topology respectively. The distribution action is separately continuous and hypocontinuous: fixing a bounded set in either factor gives continuity uniformly over that set. It is not, in general, jointly continuous on the unrestricted product.

To prove (A22) first for \(r=0\), sum (A12). By (A3) and (A16), \(m_\nu\) is bounded by a power of \(1+R_\nu\). Choosing \(M\) larger than that power plus \(P\) makes the sum finite by (A17).

For all output derivatives and moments, let \(F(X)=\sigma(X,t)+d\) be a fixed affine form. The distributional identity
\[
F^w a_\nu^w
=\big(Fa_\nu+\{F,a_\nu\}/(2i)\big)^w
\tag{A23}
\]
holds before any general operator-composition theorem. On the support ball,
\[
|F(X)|\le |F(X_\nu)|+a\sqrt{g_\nu^\sigma(t)},\qquad
|\partial_t a_\nu|_{k,g_\nu}
\le \sqrt{g_\nu(t)}\,|a_\nu|_{k+1,g_\nu}.
\]
Both forms \(g_\nu,g_\nu^\sigma\) obey (A3). Thus the new symbol in (A23) has frozen seminorms bounded by
\(C_km_\nu(1+|X_\nu|^2)^{K_1}p_{\le k+1}(a;m,g)\).
Iterating for any fixed word of \(r\) coordinates and derivatives gives the same assertion with a finite exponent \(K_r\) and \(r\) additional derivatives. Apply (A12) to these new supported symbols, then use (A16) and choose its decay order large enough to dominate the polynomial factors and the counting exponent. This proves (A22) for every word, hence every \(Q_r\).

Each partial sum \(\sum a_\nu^wu\) is Schwartz, and the estimates just proved make the series Cauchy in all Schwartz seminorms. It therefore converges in \(\mathcal S\). The symbol partial sums remain bounded in \(S(m,g)\) and converge locally smoothly to \(a\). By (A3) they converge in \(\mathcal S'\), so continuity of the distributional kernel construction identifies the Schwartz limit with the already defined \(a^wu\). This also proves independence of the partition.

For weak symbol continuity, the summable tails of these estimates are uniform on bounded symbol sets and on bounded sets of Schwartz inputs. Each finite sum is continuous under local smooth convergence: its symbols have fixed compact support, and (A10) and the preceding finite derivative estimates apply. Uniformly small tails and continuous finite sums prove the assertion for \(\mathcal S\).

Let \(C\phi=\overline\phi\). The adjoint identity \((a^w)^*=(\overline a)^w\) gives the bilinear transpose test map \((a^w)^t=C(\overline a)^wC\). Define the extension by
\(\langle a^wu,\phi\rangle=\langle u,(a^w)^t\phi\rangle\).
It agrees with the operator already constructed on regular distributions from Schwartz functions. Conjugation preserves every \(Q_r\), so a bounded set of tests has bounded image under this transpose for fixed \(a\), proving strong-dual continuity through (A6). For symbols in a bounded set, (A22) makes the union of those images bounded, giving uniform continuity in the distribution input. For distributions in a bounded set, apply (A7) and then (A22) to the transpose tests; this gives a finite symbol-seminorm estimate, uniformly over that set. The weak symbol continuity already proved for bounded sets of test functions gives the corresponding strong-dual conclusion. These observations prove all stated hypocontinuity and bounded-set assertions.

The distinction from unrestricted joint continuity is necessary. Already take \(g=e\), \(m=1\), and symbols independent of \(\xi\), so that quantization is ordinary multiplication. A symbol neighborhood controls only finitely many seminorms, say through order \(J\). With a fixed cutoff \(\chi=1\) near zero, the functions
\[
a_k(x)=c k^{-J}\chi(x)e^{ikx_1}
\tag{A24}
\]
lie in that neighborhood for a sufficiently small fixed \(c>0\). Every neighborhood of zero in \(\mathcal S'\) contains a sufficiently small fixed multiple of
\(\partial_{x_1}^{J+1}\delta_0\), because scalar multiplication is continuous. Pairing its product with \(a_k\) against a test equal to one near zero has magnitude proportional to \(k\). Thus no pair of unrestricted input neighborhoods controls even this one scalar output seminorm. The same argument applies to the weak distribution topology. For a bounded set of distributions, (A7) rules out this defect by supplying a common order.

**General metric operator composition.** Under either the one-metric or the compatible two-metric hypotheses of AN03-WP-007,
\[
(a\#b)^w=a^wb^w
\quad\hbox{on both }\mathcal S\hbox{ and }\mathcal S'.
\tag{A25}
\]
Choose bounded Schwartz approximants \(a_j,b_j\) from AN03-U001. The identity holds for them by AN03-WP-006. Formula (A22) makes the family \(a_j^w\) equicontinuous on Schwartz space, while weak symbol continuity gives
\(b_j^wu\to b^wu\) and \(a_j^wb^wu\to a^wb^wu\) in \(\mathcal S\).
Thus their composites converge to \(a^wb^wu\). The symbol products are bounded and converge weakly to \(a\#b\) by AN03-WP-007; the theorem just proved identifies the other limit with \((a\#b)^wu\). This proves (A25) on \(\mathcal S\) without circularity.

For completeness, Schwartz functions are weakly dense in \(\mathcal S'\). If \(\rho\) is a compact smooth mollifier of integral one and \(\chi\) a compact cutoff equal to one near zero, then
\(\chi(X/R)(u*\rho_{1/R})(X)\) is Schwartz and converges to \(u\) distributionally. On tests this is the convergence
\(\check\rho_{1/R}*(\chi(\cdot/R)\phi)\to\phi\) in \(\mathcal S\), proved by Taylor's formula and the rapid decay seminorms. All fixed operators in (A25) are transposes of continuous Schwartz maps and are therefore weakly continuous on \(\mathcal S'\). The identity extends from the dense subspace to every distribution.

## AN03-WCA-005 — Conformal changes of measuring scale

**Enlargement theorem.** Let \(g\) be symplectically temperate. Suppose
\[
G_X=\mu(X)g_X,\qquad \mu\ge1,
\tag{A26}
\]
is slowly varying and satisfies \(G\le G^\sigma\). Then \(G\) is symplectically temperate. No temperateness or ordinary continuity of \(\mu\) is an assumption.

Put \(h_g^2=\sup g/g^\sigma\). The uncertainty condition for \(G\) is
\(\mu^2h_g^2\le1\). We prove
\(G_Y\le C G_X(1+G_Y^\sigma(X-Y))^L\).
Set \(d=X-Y\), \(a=\mu(X)\), \(b=\mu(Y)\), and
\(t=G_Y^\sigma(d)=q_Y(d)/b\).
If \(G_X(d)\) is within the slow-variation radius of \(G\), its local comparison proves the assertion.

Otherwise \(G_X(d)\ge c_G>0\). If \(g_Y(d)\) is within the slow-variation radius of \(g\), then \(g_X\) and \(g_Y\) are comparable and
\[
c_G\le a g_X(d)\le C a g_Y(d)
\le C a h_g(Y)^2q_Y(d)
=C(a/b)\big(b^2h_g(Y)^2\big)t\le C(a/b)t.
\]
Thus \(b/a\le Ct\), and \(G_Y/G_X\le Ct\).
In the remaining case \(g_Y(d)\ge c_g>0\). Since \(G_Y\le G_Y^\sigma\),
\[
b c_g\le b g_Y(d)\le t,\qquad q_Y(d)=bt\le c_g^{-1}t^2.
\]
The original temperateness gives
\[
G_Y=(b/a)(g_Y/g_X)G_X
\le C(1+t)^{2N+1}G_X,
\]
where \(a\ge1\) was used. These three cases prove the theorem with finite structural constants.

**Conformal compatibility.** Suppose \(g_1,g_2\) are symplectically temperate, \(g_2=\mu g_1\) for a positive function \(\mu\), and \(h_1,h_2\le1\). Then the pair is compatible in the precise sense of AN03-WP-002 and
\[
h_2=\mu h_1,\qquad H^2=h_1h_2,\qquad H=\sqrt{h_1h_2}\le1.
\tag{A27}
\]
The identities follow from quadratic scaling and the definition of \(H\). To prove the first cross test, write \(q_j=g_j^\sigma\). Own temperateness also has a distance bound based at \(X\):
\[
q_{1,X}\le Cq_{1,Y}(1+q_{1,X}(X-Y))^L.
\]
Indeed the reverse own comparison bounds the \(Y\)-based distance by a power of the \(X\)-based distance, which can be inserted into (A2). If \(g_{1,X}(X-Y)\) is small, slow variation gives the cross comparison directly. If it is at least \(c>0\), use \(\mu(X)h_1(X)=h_2(X)\le1\) to get
\[
q_{2,X}(X-Y)^2
=\mu(X)^{-2}q_{1,X}(X-Y)^2
\ge h_1(X)^2q_{1,X}(X-Y)^2
\ge c\,q_{1,X}(X-Y).
\]
The last displayed own bound is therefore controlled by a power of \(1+q_{2,X}(X-Y)\). This is the first cross test. Interchange the two metrics for the other. Their scalar factor need not be bounded above or below by a fixed constant.

## AN03-WCA-006 — Constructing every affine symplectic covariance

A map \(\chi(X)=SX+Z\) is affine symplectic when
\(\sigma(ST,SU)=\sigma(T,U)\). The following five types generate all such maps:
\[
\begin{gathered}
(x,\xi)\mapsto(x+a,\xi),\qquad
(x,\xi)\mapsto(x,\xi+b),\\
(x_j,\xi_j)\mapsto(\xi_j,-x_j),\\
(x,\xi)\mapsto(Tx,T^{-t}\xi),\qquad
(x,\xi)\mapsto(x,\xi-Ax),\quad A=A^t.
\end{gathered}
\tag{A28}
\]

Here is a block proof that also handles singular position blocks. Translations remove \(Z\). Write the linear symplectic matrix as
\(S=\left(\begin{smallmatrix}A&B\\ C&D\end{smallmatrix}\right)\).
Its first \(n\) columns are linearly independent and \(A^tC=C^tA\). Consequently
\[
(A+iC)^*(A+iC)=A^tA+C^tC
\]
is positive definite: the right side vanishes on a vector only if both \(A\) and \(C\) annihilate it. Thus the real polynomial \(\det(A+tC)\) is not identically zero, since its value at \(t=i\) is nonzero. It has degree at most \(n\), so one of any \(n+1\) distinct real values of \(t\) makes \(A+tC\) invertible. The root bound used here follows by dividing out \(t-t_j\) at each distinct root \(t_j\); each division lowers the degree by one. Left multiplication by the upper shear
\(\left(\begin{smallmatrix}I&tI\\0&I\end{smallmatrix}\right)\) makes the position block invertible. Upper shears are conjugates of lower shears by the product of the pair swaps in (A28).

For an invertible position block, the symplectic identities imply that
\(CA^{-1}\) and \(A^{-1}B\) are symmetric and
\(D=A^{-t}+CA^{-1}B\). Hence
\[
S=
\begin{pmatrix}I&0\\ CA^{-1}&I\end{pmatrix}
\begin{pmatrix}A&0\\0&A^{-t}\end{pmatrix}
\begin{pmatrix}I&A^{-1}B\\0&I\end{pmatrix}.
\tag{A29}
\]
Each factor is generated by (A28); undo the preliminary shear to finish the proof. This uses only determinants, elementary polynomial division and the positive quadratic identity above.

**Covariance theorem.** For every affine symplectic \(\chi\) there is a unitary \(U_\chi\) on \(L^2(\mathbb R^n)\), preserving \(\mathcal S\) and extending to an automorphism of \(\mathcal S'\), such that
\[
U_\chi^{-1}L^wU_\chi=(L\circ\chi)^w,\qquad
U_\chi^{-1}a^wU_\chi=(a\circ\chi)^w.
\tag{A30}
\]
The first identity holds for every real affine \(L\), as an equality of the selfadjoint closures described in AN03-WP-005. The second holds for every tempered symbol \(a\), as an identity \(\mathcal S\to\mathcal S'\). The unitary is unique up to a constant of modulus one.

For the generators, take respectively
\[
\begin{array}{c|c}
\chi& U_\chi u(x)\\ \hline
(x+a,\xi)&u(x-a)\\
(x,\xi+b)&e^{ib\cdot x}u(x)\\
(x_j,\xi_j)\mapsto(\xi_j,-x_j)&\mathcal F_{0,j}u(x)\\
(Tx,T^{-t}\xi)&|\det T|^{-1/2}u(T^{-1}x)\\
(x,\xi-Ax)&e^{-ix\cdot Ax/2}u(x).
\end{array}
\tag{A31}
\]
Here \(\mathcal F_{0,j}\) is the normalized Fourier transform in just the \(j\)-th variable. Change of variables and Plancherel prove unitarity. Differentiation proves preservation of Schwartz space and of its topology; each inverse has the same property. The bilinear transpose \(U_\chi^t=CU_\chi^{-1}C\) therefore defines the distribution extension by \(\langle U_\chi u,\phi\rangle=\langle u,U_\chi^t\phi\rangle\); it agrees with the original map on Schwartz functions. Direct substitution gives the intertwining of \(x_j,D_j\), hence of every affine \(L\). Since Schwartz space is a core for each real affine observable, these identities pass to the selfadjoint closures. Products of the displayed unitaries implement products of the affine maps.

We justify both uniqueness and the distributional extension of covariance. A bounded unitary commuting with all closed \(x_j,D_j\) commutes with their translation and modulation groups. For example, on the domain of \(x_j\), differentiate
\(e^{-itx_j}Ue^{itx_j}u\); domain preservation follows from commutation with the closed operator, and the derivative is zero. Density extends the resulting equality to \(L^2\). The same argument applies to \(D_j\), whose group is the translation group explicitly proved in AN03-WP-005. Thus no prior preservation of \(\mathcal S\) by this unknown unitary has been assumed.

Fourier inversion of \(\phi\in\mathcal S(\mathbb R^n)\) then shows that \(U\) commutes with multiplication by \(\phi\). Fix \(h(x)=e^{-|x|^2}>0\) and set \(b=Uh/h\), initially a locally square-integrable function. For every \(\phi\in C_c^\infty\),
\[
U(\phi h)=\phi Uh=b\phi h.
\]
Since every compact smooth function is of the form \(\phi h\), boundedness gives
\(\|b\psi\|_2\le\|U\|\|\psi\|_2\) for all such \(\psi\).
For a bounded measurable set \(E\), approximate its indicator in \(L^2\) by compact smooth functions and select a subsequence converging almost everywhere. To obtain that subsequence, choose squared errors at most \(2^{-j}\); Tonelli makes the sum of the pointwise squared errors finite almost everywhere. Fatou's inequality gives
\(\int_E|b|^2\le\|U\|^2|E|\). The needed nonnegative Fatou inequality follows from the increasing tail infima: their integrals are bounded by the liminf of the original integrals, and monotone convergence follows from Tonelli applied to their nonnegative successive differences. Applying the resulting set inequality to the intersection of a ball with \(\{|b|>\|U\|+\varepsilon\}\) proves \(|b|\le\|U\|\) almost everywhere. Density now gives \(Uu=bu\) on all \(L^2\). Commutation with translations means
\(b(x+t)=b(x)\) almost everywhere for each fixed \(t\). Convolving with a compact smooth mollifier makes this an everywhere translation-invariant smooth function, hence a constant. Letting the mollifier radius tend to zero in distributions shows that \(b\) itself is constant: the constants converge by testing against one function of integral one. Unitarity makes its modulus one. Comparing any two implementations of \(\chi\) reduces to this commuting case, proving uniqueness.

For covariance of symbols, first exponentiate the affine intertwining. This can be checked without an abstract functional calculus: the explicit affine groups in AN03-WP-005 preserve \(\mathcal S\); differentiating the product of one inverse group with the conjugate of the other gives zero there. Density supplies equality on \(L^2\). Thus (A30) holds for all plane-wave symbols. Fourier inversion and their norm-one operator bounds extend it to Schwartz symbols. Finally, the symbol-to-kernel map, affine pullback of distributions, and conjugation by \(U_\chi\) are continuous in distributional pairings. The weak density proved after (A25) extends (A30) to every \(a\in\mathcal S'(W)\).

An affine pullback here uses the usual distributional change of variables. Symplectic matrices have \(|\det S|=1\), as follows already by taking determinants in \(S^tJS=J\). The conclusion does not supply a canonical simultaneous choice of the phases of all \(U_\chi\); products implement composition but may differ from another chosen implementation by a scalar.

The metric version follows directly. Define
\[
(\chi^*g)_X(T)=g_{\chi(X)}(ST),\qquad \chi^*m=m\circ\chi.
\tag{A32}
\]
Symplectic duality commutes with this pullback, slow variation and temperateness keep the same constants, and \(h_{\chi^*g}=h_g\circ\chi\). The chain rule identifies the symbol seminorms under \(a\mapsto a\circ\chi\). Thus covariance also transports the full metric symbol classes without changing their structural hypotheses.

## AN03-WCA-007 — Reflection and changes of quantization

Assume now that \(g\) is symplectically temperate, \(g\le g^\sigma\), \(m\) is a temperate weight, and
\[
g_{(x,\xi)}(t,\tau)=g_{(x,\xi)}(t,-\tau).
\tag{A33}
\]
This reflection condition says that the position and frequency directions are orthogonal for \(g\) at each point. It is needed here to keep the same metric class under all quantization changes; it was not needed for (A21).

For every fixed \(k\in\mathbb R\), the distributional Fourier multiplier
\[
T_k=\exp(i k\langle D_x,D_\xi\rangle)
\tag{A34}
\]
is a continuous automorphism of \(S(m,g)\), weakly continuous on bounded symbol sets, with inverse \(T_{-k}\). If \(h^2=\sup g/g^\sigma\), then for every integer \(N\ge0\),
\[
T_k a-\sum_{j<N}\frac{(ik\langle D_x,D_\xi\rangle)^j}{j!}a
\in S(h^Nm,g),
\tag{A35}
\]
with finite source-seminorm estimates for all output derivatives and the same bounded-set continuity.

To check the normalization, the doubled auxiliary phase \(2p\cdot q\) has symmetric representing map \((p,q)\mapsto(q,p)\). Its phase dual at \((t,\tau)\) is \(g^\sigma(t,-\tau)\), which equals \(g^\sigma(t,\tau)\) by (A33) and quadratic inversion. The actual phase \(k p\cdot q\), for \(k\ne0\), therefore has dual
\(4k^{-2}g^\sigma\) and parameter \(|k|h/2\) in AN03-U002's convention. If necessary replace \(g\) by one fixed sufficiently small positive multiple to make this parameter at most one. That replacement leaves the symbol spaces unchanged with equivalent seminorms and preserves all required comparisons. AN03-GAU-007–008 prove (A35), absorbing fixed powers of \(|k|/2\) in its constants. For \(k=0\) the map is the identity and the assertion is immediate.

The Gauss extension agrees with the stated distributional multiplier. Indeed bounded compact approximants converge in \(\mathcal S'\) by (A3); their Gauss images are bounded in the asserted polynomially growing target class and converge locally smoothly. Thus both definitions are limits of the same sequence in distributional pairings. Multiplication of the Fourier multipliers now proves \(T_kT_l=T_{k+l}\), hence the automorphism assertion. No uniform estimate for unbounded \(k\) is claimed.

Let \(\operatorname{Op}_\tau\) have the kernel base point
\((1-\tau)x+\tau y\), as in AN03-WP-004. The kernel coordinate calculation of AN03-WP-008, valid for every tempered symbol, gives
\[
\operatorname{Op}_s(T_{\tau-s}a)=\operatorname{Op}_\tau(a).
\tag{A36}
\]
Uniqueness of the symbol follows by inverse partial Fourier transformation of the kernel. In particular, if \(a,c\) are left and right symbols and \(b\) is their Weyl symbol, then
\[
\begin{gathered}
b=T_{-1/2}a=T_{1/2}c,\qquad
a=T_{1/2}b=T_1c,\\
c=T_{-1}a=T_{-1/2}b.
\end{gathered}
\tag{A37}
\]
All these symbols lie in the same \(S(m,g)\). Combining (A36) with (A21) proves their Schwartz and distribution actions, with precisely the topologies stated in AN03-WCA-004.

There is an elementary action proof under the additional vertical bound
\[
g_{(x,\xi)}(0,\tau)\le|\tau|^2.
\tag{A38}
\]
It is useful to see exactly what this stronger hypothesis buys. For each fixed \(\beta\), directional symbol estimates and (A3) give
\[
|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|
\le C_{\alpha,\beta}p_{\le|\alpha|+|\beta|}(a;m,g)
(1+|x|+|\xi|)^{K_\beta},
\tag{A39}
\]
where \(K_\beta\) is independent of \(\alpha\). The vertical factor contributes at most one to each coordinate frequency derivative; the factors from the fixed position derivatives have a polynomial bound. The left operator is
\((2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi\).
After any fixed output derivatives, multiplication by \((1+|x|^2)^M\) transfers \((1-\Delta_\xi)^M\) onto the amplitude. Formula (A39) leaves only a fixed power of \(1+|x|\), independent of \(M\), and the Schwartz decay of \(\widehat u\) makes the frequency integrals finite. Choosing \(M\) large proves every desired output seminorm with finitely many source seminorms. Adjoint transposition and the quantization changes give the other actions. The more general proof of (A21) removes (A38) entirely, while the reflection condition remains in the same-class quantization theorem.

## AN03-WCA-008 — Left products and the subprincipal coefficient

Keep the reflected one-metric hypotheses of the preceding section, and take
\(a_j\in S(m_j,g)\), \(j=1,2\). Their left operator composite has left symbol
\[
a_1\circ_L a_2
=T_{1/2}\big((T_{-1/2}a_1)\#(T_{-1/2}a_2)\big)
\in S(m_1m_2,g).
\tag{A40}
\]
This identity follows from (A25) and (A37); it holds on both \(\mathcal S\) and \(\mathcal S'\). For Schwartz symbols it also gives the exact differential-multiplier formula
\[
a_1\circ_L a_2
=\left.\exp(i\langle D_\xi,D_y\rangle)
\big(a_1(x,\xi)a_2(y,\eta)\big)\right|_{(y,\eta)=(x,\xi)}.
\tag{A41}
\]
For general symbols the right side denotes its bounded weak extension, defined by (A40).

Here is the phase calculation. Pulling the outer \(T_{1/2}\) back before restriction replaces its differential variables by \(D_x+D_y,D_\xi+D_\eta\). The three quantization phases and the Weyl phase add to
\[
\begin{split}
&\tfrac12\langle D_x+D_y,D_\xi+D_\eta\rangle
-\tfrac12\langle D_x,D_\xi\rangle-\tfrac12\langle D_y,D_\eta\rangle\\
&\hspace{25mm}
+\tfrac12\big(\langle D_\xi,D_y\rangle-\langle D_x,D_\eta\rangle\big)
=\langle D_\xi,D_y\rangle.
\end{split}
\tag{A42}
\]
All these constant-coefficient operators commute on the product Schwartz space. In Fourier variables the restriction and outer multiplier identity is obtained by replacing the output frequency by the sum of the two input frequencies, so it is valid for their full exponentials as well as for polynomials.

Every finite truncation satisfies
\[
a_1\circ_L a_2-
\sum_{|\alpha|<N}\frac{1}{\alpha!}
(\partial_\xi^\alpha a_1)(D_x^\alpha a_2)
\in S(h^Nm_1m_2,g),
\tag{A43}
\]
with finite seminorm estimates and weak bounded-set continuity. One can obtain this without imposing an unproved direct Gauss estimate for the degenerate phase in (A41). Expand each of the three quantization maps in (A40) and the Weyl product only to order \(N-1\), using their proved remainders. The coefficient of degree \(j\) in a quantization expansion maps \(S(w,g)\) to \(S(h^jw,g)\): it is the difference of remainders of orders \(j\) and \(j+1\). The analogous Weyl coefficient maps two weighted classes to the product weight times \(h^j\). These statements hold for every temperate weight \(w\), including products with powers of \(h\). Thus each discarded term has weight at least \(h^N m_1m_2\); \(h\le1\) permits the inclusion for higher powers. Only finitely many terms and seminorms occur. The terms below degree \(N\) combine by the polynomial identity (A42), giving exactly (A43). This is a finite remainder argument, not an assertion of convergence of an infinite series.

For a classical polyhomogeneous left symbol, write
\(a\sim a_m+a_{m-1}+\cdots\), where the coefficient \(a_{m-j}\) is homogeneous in \(\xi\) of degree \(m-j\) away from zero, with the usual symbol remainder estimates. Formula (A37) and (A35), in the classical \((1,0)\) metric, give
\[
b_m=a_m,\qquad
b_{m-1}=a_{m-1}+\frac{i}{2}
\sum_{\ell=1}^n\partial_{x_\ell}\partial_{\xi_\ell}a_m.
\tag{A44}
\]
The sign follows from \(D_xD_\xi=-\partial_x\partial_\xi\).
Terms of order two in this expansion lower the frequency degree by at least two. Thus \(b_{m-1}\), the next Weyl coefficient, is the subprincipal symbol of the left operator in these coordinates. The calculation is local in \(x\): if the classical estimates are only local, first multiply by a position cutoff equal to one on the region in question and apply the remainder formula there. The finite coefficients agree on that region, and arbitrary-order remainder estimates make the conclusion independent of the cutoff.

For scalar classical operators with principal symbols \(a_0,b_0\) and subprincipal symbols \(a_s,b_s\), the Weyl product and scalar parity imply
\[
\begin{gathered}
(AB)_0=a_0b_0,\qquad
(AB)_s=a_sb_0+a_0b_s+\{a_0,b_0\}/(2i),\\
(A^*)_0=\overline{a_0},\qquad (A^*)_s=\overline{a_s}.
\end{gathered}
\tag{A45}
\]
For the commutator, regarded as an operator of order \(m_A+m_B-1\),
\[
[A,B]_0=\{a_0,b_0\}/i,\qquad
[A,B]_s=\big(\{a_s,b_0\}+\{a_0,b_s\}\big)/i.
\tag{A46}
\]
Indeed the even Weyl terms cancel for scalar symbols, and the first unused odd term lowers the total order by three. The product's order-one part comes from the two next homogeneous coefficients and its first Weyl bracket. Conjugation of a Weyl symbol gives the adjoint identities. These arguments establish every displayed rule, including cases where a displayed leading coefficient vanishes; the declared order then simply has a zero coefficient. No unchanged scalar-cancellation formula is asserted for matrices.

## AN03-WCX-001 — Four worked examples

**A metric larger than its dual.** Let \(g_X=7e\) and \(m(X)=1+|X|^2\). This constant metric is slowly varying and symplectically temperate, but \(g^\sigma=e/7\), so its uncertainty inequality fails. The weight is temperate: the triangle inequality bounds either ratio of \(1+|X|^2\) and \(1+|Y|^2\) by \(2(1+|X-Y|^2)\), which is bounded by a constant times \(1+q_Y(X-Y)\). The symbol \(a(x,\xi)=|x|^2+|\xi|^2\) belongs to \(S(m,g)\), and (A21) gives its actions on \(\mathcal S\) and \(\mathcal S'\). Here its operator is the familiar differential expression \(|x|^2-\Delta\). These actions do not imply boundedness on \(L^2\): for a nonzero compact smooth \(u\), translate it by \(Re_1\); its \(L^2\) norm stays fixed, whereas its pairing with \((|x|^2-\Delta)u\) after translation grows quadratically in \(R\). In the localization proof, \(r_\nu=e/8\), so the decay variable is an ordinary distance multiplied by \(1/\sqrt8\).

**An unbounded conformal factor.** Set \(s(X)=(1+|X|^2)^{1/2}\), \(g_X=s(X)^{-2}e\), and \(G=e\). The function \(s\) is 1-Lipschitz. Thus a sufficiently small \(g_X\)-displacement changes \(s\) by at most a fixed fraction of \(s(X)\), proving slow variation. The inequalities
\[
\frac{s(X)^2}{s(Y)^2}\le 2(1+|X-Y|^2),\qquad q_Y=s(Y)^2e\ge e
\tag{A47}
\]
prove symplectic temperateness, including the reversed ratio. Now \(G=\mu g\) with \(\mu=s^2\), which is unbounded. The local Planck parameters are \(h_g=s^{-2}\), \(h_G=1\), and the cross parameter is \(H=s^{-1}\). For unit input weights, conformal compatibility yields a product remainder in \(S(s^{-N},(g+G)/2)\) even though one input has Planck parameter identically one. Ordinary continuity of the conformal factor is also unnecessary: the pair \(g=e/4\), \(G=(1+\mathbf1_{\{x_1\ge0\}})g\) satisfies the enlargement hypotheses by uniform comparison with fixed positive forms, including at the jump.

**A quadratic shear of the oscillator.** In one dimension let \(Uu(x)=e^{-3ix^2/2}u(x)\). Direct differentiation gives \(U^{-1}DU=D-3x\). The associated map is \(\chi(x,\xi)=(x,\xi-3x)\), so covariance gives
\[
U^{-1}(x^2+D^2)U
=\big(x^2+(\xi-3x)^2\big)^w
=D^2-3(Dx+xD)+10x^2.
\tag{A48}
\]
The symmetrized middle term is essential. Replacing it by \(-6xD\) loses the constant \(3i\), because \(Dx=xD-i\). Although the final differential expression contains this imaginary constant when written in left order, its Weyl symbol is real and integration by parts shows that its action on \(\mathcal S\) is symmetric. The equality on \(\mathcal S\) is enough to verify the displayed algebra; no assertion about the oscillator's selfadjoint closure or spectral theorem is needed.

**Balancing a first-order differential operator.** Let \(b(x)=2+\sin x\). The left symbol of \(bD\) is \(b\xi\); (A44) gives the next Weyl coefficient \(ib'/2\). The symmetric operator on Schwartz functions
\[
B=\tfrac12(bD+Db)=bD-\tfrac i2b'
\tag{A49}
\]
has left symbol \(b\xi-ib'/2\). Its Weyl symbol is exactly \(b\xi\): all terms after the first quantization correction vanish because the symbol is linear in \(\xi\). Its subprincipal coefficient is therefore zero. This cancellation explains why a next left coefficient alone does not determine the subprincipal symbol.

## AN03-WCP-001 — Problems with solutions

**Problem 1.** The norm in (A8) is invariant under all invertible affine maps. Could the covariance theorem also hold for the map \((x,\xi)\mapsto(2x,2\xi)\) in one dimension?

**Solution.** No. Such an implementation, preserving \(\mathcal S\) as in the theorem, would intertwine \(x\) with \(2x\) and \(D\) with \(2D\). Conjugating their commutator on \(\mathcal S\) would give both \(iI\) and \([2x,2D]=4iI\). The contradiction concerns the symplectic form, not the Fourier norm: the change of variables proving invariance of that norm needs only an invertible matrix. Hence an affine-invariant upper bound is weaker than unitary covariance of every symbol.

**Problem 2.** In two dimensions consider the symplectic matrix with blocks
\(A=D=\operatorname{diag}(1,0)\), \(B=\operatorname{diag}(0,1)\), and \(C=\operatorname{diag}(0,-1)\). Carry out the singular-block step of (A29), using the preliminary upper shear with \(t=1\).

**Solution.** Multiplication on the left by \(\left(\begin{smallmatrix}I&I\\0&I\end{smallmatrix}\right)\) gives new blocks
\(A'=A+C=\operatorname{diag}(1,-1)\), \(B'=B+D=I\), \(C'=C\), \(D'=D\). The factorization uses the lower shear matrix \(C'(A')^{-1}=\operatorname{diag}(0,1)\), the cotangent lift of \(A'\), and the upper shear matrix \((A')^{-1}B'=\operatorname{diag}(1,-1)\). Multiplying those three block matrices yields the four new blocks just listed: the lower-right block is
\((A')^{-t}+C'(A')^{-1}B'=\operatorname{diag}(1,-1)+\operatorname{diag}(0,1)=D'\).
Undo the preliminary upper shear. The original map simply exchanges the second coordinate pair; the calculation checks that the general algorithm works even though its position block has rank one.

**Problem 3.** For \(b\in C^\infty(\mathbb R)\) with every derivative bounded, compute the exact left symbol of \(D^2b(x)\). Locate the term that would be lost by using pointwise symbol multiplication.

**Solution.** Apply (A43) to \(a_1=\xi^2\), \(a_2=b(x)\). Only frequency derivatives of orders zero, one and two survive, and they give
\[
\xi^2\circ_L b=b\xi^2-2ib'\xi-b''.
\tag{A50}
\]
Leibniz's rule independently gives \(D^2(bu)=bD^2u-2ib'Du-b''u\), verifying both signs and the factorial in the second derivative term. Pointwise multiplication loses both lower coefficients. The same calculation with \(a_1=\xi\), \(a_2=x\) gives \(\xi\circ_Lx=x\xi-i\); the outer conversion in (A40) changes the Weyl coefficient \(-i/2\) to this left coefficient \(-i\).

**Problem 4.** Take \(g=e\), \(m=1\), \(a(x,\xi)=e^{i(x+\xi)}\) in one dimension. Compute \(T_1a-a\). Does the first remainder in (A35) have a smooth Schwartz kernel? What can further remainder estimates alone say when \(h=1\)?

**Solution.** Since \(D_xD_\xi a=a\), its multiplier definition gives \(T_1a=e^i a\); therefore \(T_1a-a=(e^i-1)a\). The nonzero plane-wave Weyl operator is a modulation followed by translation, with a constant phase; its distribution kernel is supported on a shifted diagonal and is not smooth. When \(h=1\), every remainder space \(S(h^Nm,g)\) equals \(S(1,e)\). Increasing \(N\) still gives finite quantitative estimates, but those spaces alone express no improvement of decay or smoothing. One must also avoid treating a sequence of finite remainder bounds, whose constants depend on \(N\), as convergence of an infinite series.

**Problem 5.** Choose \(\chi\in C_c^\infty(\mathbb R)\) with \(\chi(0)=1\), and put \(a_j(x,\xi)=\chi(x-j)\), \(u_j=\delta_j\). Verify the bounded-set conclusion in (A21) for these moving inputs. Show what fails if \(u_j\) is replaced by \(v_j=e^{j^2}\delta_j\).

**Solution.** The symbols form a bounded set of \(S(1,e)\) and converge locally smoothly to zero. For any bounded test set \(B\) and every integer \(M\), its Schwartz seminorm bounds imply
\(\sup_{\phi\in B}|\phi(j)|\le C_{B,M}(1+j)^{-M}\).
Thus \(u_j\to0\) in the strong dual, the set \(\{u_j\}\) is bounded, and \(a_j^wu_j=u_j\to0\) strongly. By contrast the single Schwartz test \(\phi(x)=e^{-x^2/2}\) gives
\(\langle v_j,\phi\rangle=e^{j^2/2}\), so \(\{v_j\}\) is not even pointwise bounded, and \(a_j^wv_j=v_j\) fails to tend to zero. The boundedness hypothesis has content even when every individual input is tempered.

**Problem 6.** For smooth real \(b,c\) with all derivatives bounded, set
\(A=\frac12(bD+Db)\), \(B=\frac12(cD+Dc)\). Find the left and subprincipal symbols of \([A,B]\) and check them directly.

**Solution.** Put \(f=bc'-b'c\). The principal symbols are \(b\xi,c\xi\), with zero subprincipal symbols by (A49). Their bracket is \(f\xi\). Formulas (A46) therefore predict principal symbol \(-if\xi\) and zero subprincipal coefficient at declared order one. Directly write
\(A=-i(b\partial+b'/2)\) and \(B=-i(c\partial+c'/2)\). In their commutator the second derivative terms cancel, the first derivative coefficient is \(-f\), and the multiplication coefficient is \(-f'/2\). Thus
\[
[A,B]=-ifD-\tfrac12f',\qquad
\text{left symbol}=-if\xi-\tfrac12f'.
\tag{A51}
\]
The correction in (A44) adds \(\frac i2\partial_x\partial_\xi(-if\xi)=f'/2\), so the subprincipal coefficient vanishes as predicted. This calculation remains valid if \(f\) vanishes identically; then the declared leading and next coefficients are both zero.

## References, topology convention and further directions

The mathematical antecedent is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, corrected second printing (1994), §§18.5–18.6, in particular Propositions 18.5.6–18.5.7, Lemma 18.5.8, Theorems 18.5.9–18.5.10, Lemma 18.6.1 and Theorem 18.6.2. The course uses its own proof order and notation. The claims about general metrics, quantization and covariance are classical antecedents; the examples and solutions here illustrate them without asserting new theorems.

For comparison, Nicolas Lerner's author-hosted [chapter on phase-space metrics](https://webusers.imj-prg.fr/~nicolas.lerner/ch2booklerner.pdf), Lemma 2.2.21, Corollary 2.3.10 and Theorems 2.3.18–2.3.19, treats conformal metrics and changes of quantization. Its [appendix](https://webusers.imj-prg.fr/~nicolas.lerner/ch4booklerner.pdf), Theorem 4.4.3 and Proposition 4.4.4, discusses symplectic generators; Lemma 4.4.15 and Remark 4.4.19 address unitary implementations and distributional covariance. These are reading references. No open license for reusing their prose was verified, and no reference text is imported. The Fourier normalizations differ. In the checked metric chapter's printed page 100, retain the parameter in the exponential defining the quantization change and the outer transform converting a Weyl product back to a left symbol; (A34) and (A40) state the formulas used here.

The complete-metric prerequisite for (A7) is Paul Garrett's [*Review of metric spaces*, 2 February 2014](https://www-users.cse.umn.edu/~garrett/m/fun/notes_2012-13/01_metric_spaces.pdf), Theorem 4.0.1 on printed page 9: its nested-ball proof applies to every complete metric space. The [author's license notice](https://www-users.cse.umn.edu/~garrett/m/fun/) specifies CC BY 3.0 unless otherwise indicated. This is an external reading interface; its prose is not incorporated into the independently written programme text. Here the complete metric on \(\mathcal S\) is
\(d(u,v)=\sum_{r\ge0}2^{-r-1}\min(1,Q_r(u-v))\). A sequence Cauchy for this metric is Cauchy for each \(Q_r\), and conversely, so the completeness proof in AN03-WCA-001 supplies the exact hypothesis needed for that application. Fourier duality, Lebesgue integration and the \(L^2\) entry contracts remain the previously declared course dependencies, rather than new introductory chapters.

The distribution topology requires an explicit qualification of the antecedent's continuity wording. With the Fréchet symbol topology and the strong dual topology, (A24) disproves unrestricted joint continuity, even under the extra metric bound in (A38); it also disproves it for the weak distribution topology. The assertions proved here are separate continuity and hypocontinuity for the **strong** dual, together with bounded weak-symbol continuity uniform on strongly bounded inputs. Fixed-symbol maps are also weak-dual continuous by transposition. No claim of the same unrestricted bilinear continuity is made in an unstated alternative source convention. This records the exact mathematical interpretation used by the course rather than inferring an unqualified error from ambiguous terminology.

The next questions concern boundedness on \(L^2\), compactness and lower bounds for nonnegative symbols. The action estimate (A22) supplies the common Schwartz domain on which those questions can be asked, but it does not answer them. One can also ask how phases of the implementing unitaries fit together along loops of symplectic maps; uniqueness up to a scalar alone does not construct a continuous double cover. Both directions require further results. The present unit remains an independently authored draft at its explicit prerequisites, awaiting separate proof, correspondence, expression and artifact reviews.
