# Reconstructing a weight from a modular cocycle

**Self-checked by the writing AI.**

A cocycle specifies how a second modular motion differs from a first. Recovering a weight requires more than recognizing the resulting automorphisms: different weights can have the same modular group. We construct the missing GNS map, prove its full Hilbert-algebra axioms, and identify its relative operator on the entire mixed finite domain. The construction works on an arbitrary von Neumann algebra.

The mathematical antecedent is Takesaki, *Theory of Operator Algebras II*, VIII.3, Theorem 3.8 and its analytic-domain lemmas. Theorem 3.7 in that edition is the chain rule. The proof below organizes the reconstruction around a general analytic-core lemma and a conjugation identity. In particular it gives the approximation argument for the complete relative graph explicitly.

## The reconstruction problem and its inputs

Let \(M\) be a von Neumann algebra and let \(\varphi\) be a faithful normal semifinite weight. Use its faithful normal GNS representation to regard \(M\subseteq B(H)\), and write

\[
\Lambda=\Lambda_\varphi,\qquad
S_\varphi=J\Delta^{1/2},\qquad
\sigma_t=\sigma_t^\varphi.
\tag{CX.1}
\]

Inner products are linear in the first variable. The finite left ideal is
\(\mathfrak n=\{x:\varphi(x^*x)<\infty\}\). All Hilbert spaces, projection families and directed sets are arbitrary.

A **unitary modular cocycle** is a family \(u_t\in\mathcal U(M)\) such that \(t\mapsto u_t\) is strongly continuous and

\[
u_{s+t}=u_s\sigma_s(u_t)\qquad(s,t\in\mathbb R).
\tag{CX.2}
\]

Strong continuity is intrinsic here: on a uniformly bounded set the faithful normal representation preserves the sigma-strong topology. Taking \(s=t=0\) gives \(u_0=1\), and the identity with \(-t\) gives the inverse formulas. Unitarity also implies strong continuity of the adjoints.

We will prove that there is a unique faithful normal semifinite weight \(\psi\) with

\[
[D\psi:D\varphi]_t=u_t.
\tag{CX.3}
\]

The cocycle on the left is the balanced-matrix cocycle of SI-14. Thus its meaning is already fixed independently of the construction to follow.

The exact inputs are:

- Completing the two multiplication domains through Fullness and recovery of the original weight, the full correspondence between left Hilbert algebras and faithful normal semifinite weights, including their finite ideals and actual GNS maps;
- The commutant and the integral orbit identity through The opposite structure of a Tomita algebra, the modular commutant theorem, analytic finite algebra, and identification of the modular powers of a Tomita algebra;
- Contractive approximation from a nonunital algebra and HAP-07, bounded strong* approximation of operators and bounded strong approximation of an individual left-bounded GNS vector;
- Finite positive cutoffs characterize semifiniteness, finite positive contraction nets, and CP-06, the complete norming predual;
- Consequences for GNS maps and sums of weights's GNS graph theorem, for sigma-strong convergence of algebra elements and weak convergence of GNS vectors;
- Unbounded measurable functions and SK-07–09, spectral domains and transported functional calculus;
- Gaussian normalization and its Fourier transform and MA-04, MA-06, MA-08–09 and MA-14–16, Fourier uniqueness, the hyperbolic integral kernel, strip bounds, analytic continuation and Gaussian integrals;
- Ordinary relative GNS maps are a specialization and SI-14, the closed ordinary relative graph and the spatial formula for the already defined cocycle; SC-10's injectivity of the numerator-to-spatial-derivative map.

The proof does not presume a faithful state, a countable decomposition, a common natural-cone realization, or the converse being proved. No action or crossed-product cocycle theorem is used.

## An analytic unitary core determines all powers

We first isolate a Hilbert-space argument that will be used twice.

**Lemma.** Let \(V_t\) be a strongly continuous unitary group on a Hilbert space \(K\). Suppose a dense linear subspace \(\mathcal D\) has maps \(V_z:\mathcal D\to\mathcal D\), \(z\in\mathbb C\), which form an algebraic group, agree with \(V_t\) for real \(t\), and make \(z\mapsto V_z\xi\) norm-entire for every \(\xi\in\mathcal D\). Then

\[
P=\overline{V_{-i/2}|_{\mathcal D}}
\tag{CX.4}
\]

is positive, injective and self-adjoint, and

\[
V_t=P^{2it},\qquad
V_z\xi=P^{2iz}\xi.
\tag{CX.5}
\]

Every vector of \(\mathcal D\) belongs to every real-power domain of \(P\), and \(\mathcal D\) is a core for each power separately and for each finite sum of their graph norms.

**Proof.** Analytic continuation of the real unitary adjoint identity gives

\[
\langle V_z\xi,\eta\rangle
=\langle\xi,V_{-\bar z}\eta\rangle
\quad(\xi,\eta\in\mathcal D).
\tag{CX.6}
\]

The two sides are scalar-entire in \(z\), and agree for real \(z\), which justifies this continuation without introducing an unbounded adjoint informally. The group law and real unitarity show that the norm of \(V_{t+is}\xi\) equals the norm of \(V_{is}\xi\). It is therefore bounded on every finite horizontal strip.

For \(a\in\mathbb R\), the operator \(L_a=V_{-ia}|_{\mathcal D}\) is symmetric by (CX.6), and

\[
\langle L_a\xi,\xi\rangle
=\|V_{-ia/2}\xi\|^2\geq0.
\tag{CX.7}
\]

Apply the vector contour identity MA-15 to the entire group \(z\mapsto V_{az}\). It gives

\[
\xi=\int_{\mathbb R}
 \frac{(I+V_{-ia})V_{at+ia/2}\xi}
      {e^{\pi t}+e^{-\pi t}}\,dt .
\tag{CX.8}
\]

The preceding horizontal bounds make this a norm integral. Its finite Riemann sums lie in \((I+L_a)\mathcal D\), so that range is dense.

Here are the closed-operator details. Let \(L=\overline{L_a}\). It is positive symmetric, and
\(\|(I+L)\xi\|\geq\|\xi\|\). Closedness of \(L\) makes the range of \(I+L\) closed: if the images are Cauchy, both the vectors and their \(L\)-images are Cauchy. Its dense range is consequently all of \(K\). If \(\eta\in D(L^*)\), take
\(\xi=(I+L)^{-1}(I+L^*)\eta\). The difference \(\eta-\xi\) belongs to
\(\ker(I+L^*)=\operatorname{ran}(I+L)^\perp=0\). Hence \(L=L^*\).

In particular (CX.4) is positive self-adjoint. Its range is dense, since \(V_{-i/2}\mathcal D=\mathcal D\), and therefore its kernel is zero. Flipping the graph on this invariant domain shows

\[
\overline{V_{i/2}|_{\mathcal D}}=P^{-1}.
\tag{CX.9}
\]

Indeed the closure of the flipped graph of \(P|_{\mathcal D}\) is the graph of \(P^{-1}\).

We still have to identify the real group. For \(s\in\mathbb R\), put

\[
T_s=\int_{\mathbb R}\frac{e^{-ist}}{2\cosh(\pi t)}V_t\,dt.
\]

The second contour identity in MA-15 gives

\[
T_s(e^{-s/2}P+e^{s/2}P^{-1})\xi=\xi
\quad(\xi\in\mathcal D)
\tag{CX.10}
\]

and proves that the range of the displayed expression on \(\mathcal D\) is dense. The positive self-adjoint spectral operator

\[
D_s=e^{-s/2}P+e^{s/2}P^{-1},
\qquad D(D_s)=D(P)\cap D(P^{-1}),
\]

has spectral function at least two. Thus \(D_s^{-1}\) is bounded, and (CX.10), on its dense range, identifies

\[
T_s=D_s^{-1}
=\int_{\mathbb R}\frac{e^{-ist}}{2\cosh(\pi t)}P^{2it}\,dt,
\tag{CX.11}
\]

where the last identity is MA-06 applied to \(P^2\). Fourier uniqueness MA-04 on each continuous scalar matrix coefficient, after division by \(2\cosh(\pi t)\), yields \(V_t=P^{2it}\). MA-09 recognizes the given entire continuation and its domains, proving (CX.5). The earlier essential self-adjointness of every \(L_a\) then shows that its closure is \(P^{2a}\).

For the simultaneous core assertion, let \(g_r(s)=\exp(-(\log s)^2/r)\) on \(s>0\). The Gaussian transform MA-03 makes \(g_r(P)\) a Gaussian average of \(V_t\). For \(\xi\in\mathcal D\), that average need not itself have been assumed to belong to \(\mathcal D\); instead approximate its integral by finite Riemann sums of \(V_t\xi\). These converge in every selected power graph norm, since on \(\mathcal D\) the power commutes with \(V_t\), and each corresponding orbit has an integrable Gaussian bound. For an arbitrary vector in the common domain of finitely many powers, \(g_r(P)\) tends to the identity in their combined graph norm by scalar dominated convergence. For fixed \(r\), every \(P^a g_r(P)\) in that finite list is bounded, so approximate the original Hilbert vector by vectors of \(\mathcal D\) before using the Riemann sums. These two approximations prove density in the required graph norm. \(\square\)

**Averaging corollary.** Suppose instead that a dense linear subspace \(\mathcal F\subseteq K\) is invariant under every \(V_t\) and under

\[
V(f)=\int_{\mathbb R}f(t)V_t\,dt\qquad(f\in L^1(\mathbb R)).
\tag{CX.11a}
\]

Let \(\mathcal F_{\mathrm{an}}\) consist of the vectors in \(\mathcal F\) with a Hilbert-norm entire orbit whose entire extension stays in \(\mathcal F\). Then \(\mathcal F_{\mathrm{an}}\) is a core for every closed complex-time operator of the group.

To prove this, for \(\xi\in\mathcal F\) and \(r>0\) define

\[
\xi_r(z)=\sqrt{r/\pi}\int_{\mathbb R}e^{-r(t-z)^2}V_t\xi\,dt.
\tag{CX.11b}
\]

For every \(z\), the scalar kernel belongs to \(L^1\), so \(\xi_r(z)\in\mathcal F\) by the assumed invariance. The kernel is \(L^1\)-norm entire: on compact sets of \(z\), all its derivatives have an integrable Gaussian bound. Thus (CX.11b) is Hilbert-norm entire. Real translation gives its actual orbit, and complex translations give the extensions of its translated vectors. Hence \(\xi_r(0)\in\mathcal F_{\mathrm{an}}\), this analytic space is invariant under all complex translations, and \(\xi_r(0)\to\xi\). It is dense in \(K\). Apply the lemma to this space. If \(V_z=P^{2iz}\) and \(z=t+is\), then \(D(V_z)=D(P^{-2s})\), and multiplication by the unitary \(P^{2it}\) preserves the graph norm. The real-power core assertion therefore proves the claim for every complex parameter, including its exact domain.

No norm-continuous action on an additional Banach graph space was assumed. If \(\mathcal F\) has such a norm and satisfies \(\|V(f)\xi\|_{\mathcal F}\leq C_\xi\|f\|_1\), the same \(L^1\)-kernel argument makes (CX.11b) entire in that stronger norm as well. This covers that interpretation of an \(\mathcal F\)-valued entire extension without confusing it with operator-norm continuity of every real orbit.

## Two identities on the full finite left ideal

We need identities for every \(x\in\mathfrak n\), not only for vectors in the finite analytic algebra.

**Symmetry identity.** For \(x,y\in\mathfrak n\),

\[
JxJ\Lambda(y)=yJ\Lambda(x).
\tag{CX.12}
\]

**Proof.** On the full finite-star Hilbert algebra, MF-05–06 identifies \(JxJ\) with right multiplication by \(J\Lambda(x)\). Its bounded multiplication identity gives (CX.12). For a general \(x\in\mathfrak n\), HAP-07 and WH-11 give finite-star \(x_n\) with

\[
\Lambda(x_n)\to\Lambda(x),\qquad
x_n\to x\ \hbox{strongly},\qquad
\|x_n\|\leq\|x\|.
\]

For finite-star \(y\), pass to the limit in the two sides of (CX.12). Approximate a general \(y\in\mathfrak n\) in the same way; the two limits use, respectively, norm convergence of \(\Lambda(y_n)\) and strong convergence of \(y_n\) on the fixed vector \(J\Lambda(x)\). This proves the full assertion. \(\square\)

An element \(a\in M\) is **entire for \(\sigma\)** if its real orbit extends to an operator-norm entire map \(z\mapsto\sigma_z(a)\). This is equivalent to a sigma-weak-entire extension. To see that the weaker convention suffices, let \(F\) take values in \(M=(M_*)^*\), with \(z\mapsto\omega(F(z))\) entire for every \(\omega\in M_*\). On any compact disc \(K\), each of these scalar functions is bounded. The closed sets

\[
E_n=\{\omega\in M_*:\sup_{z\in K}|\omega(F(z))|\leq n\}
\]

cover the Banach space \(M_*\). At least one has interior. The complete-metric fact used here has a short proof: if all the closed sets had empty interior, choose nested nonempty closed balls, with radii tending to zero, each contained in the preceding ball's interior and avoiding the next closed set. Completeness gives a point in every ball, contrary to the cover. An interior ball in one \(E_n\), and differences of its points, now give a common bound \(\sup_{z\in K}\|F(z)\|<\infty\), since the predual is norming. On a circle of radius \(R\), the scalar Cauchy coefficients therefore define elements \(A_k\in(M_*)^*=M\) with \(\|A_k\|\leq C R^{-k}\). Their norm-convergent power series agrees with \(F\) against every predual test, hence agrees in \(M\). This proves norm holomorphy. Norm-entire maps are plainly sigma-weak-entire.

For an entire element, the group law, multiplicativity and
\(\sigma_z(a)^*=\sigma_{\bar z}(a^*)\) follow by analytic continuation, initially in one variable and then in the other.

**Right multiplier lemma.** If \(a\) is entire for \(\sigma\) and \(x\in\mathfrak n\), then \(xa\in\mathfrak n\), and

\[
\Lambda(xa)=J\sigma_{-i/2}(a^*)J\Lambda(x).
\tag{CX.13}
\]

In particular

\[
\|\Lambda(xa)\|\leq\|\sigma_{-i/2}(a^*)\|\,\|\Lambda(x)\|.
\tag{CX.14}
\]

**Proof.** First suppose that \(a\) is the bounded left multiplier of a vector in MF-07's finite analytic algebra. On that algebra, MF-11's right multiplication formula and
\(J\Lambda(a)=\Lambda(\sigma_{-i/2}(a^*))\)
give exactly (CX.13). Approximate an arbitrary \(\Lambda(x)\), \(x\in\mathfrak n\), by bounded left multipliers of finite analytic vectors, in Hilbert norm and strongly in \(M\). Such approximation follows by HAP-07, followed for each finite-star approximant by MF-08's Gaussian approximation. The operator norms remain bounded. Products with the fixed \(a\) converge strongly, while the right side of (CX.13) converges in norm. NW-12 proves both membership of the limit in \(\mathfrak n\) and the asserted formula.

To remove the finite-vector condition on \(a\), first fix \(r>0\) and use the Gaussian average

\[
a_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}\sigma_t(a)\,dt.
\tag{CX.15}
\]

For this intermediate step \(a\) could be any bounded element of \(M\). The integral is a strong* operator integral. For every complex \(z\) its continuation is obtained by replacing the kernel by \(e^{-r(t-z)^2}\), with operator norm at most \(e^{r(\operatorname{Im}z)^2}\|a\|\).

HAP-05 applied to the finite analytic algebra supplies a net of its multipliers \(a_j\), uniformly bounded by \(\|a\|\), tending strongly* to \(a\). For fixed \(r,z\), the Gaussian averages \((a_j)_r(z)\) converge strongly* to \(a_r(z)\), with a uniform bound. To justify this assertion for nets, cut the integral to a compact interval. A uniformly bounded net of operators converging strongly converges uniformly on any compact set of test vectors. Apply this to the continuous compact orbits \(\Delta^{-it}\xi\), then integrate; the Gaussian tail has a bound independent of \(j\). The adjoints are handled with the conjugate Gaussian kernel. This proof does not apply a sequence-only dominated-convergence principle to an arbitrary net.

The averages \((a_j)_r\) remain finite analytic multipliers by MF-08 and its power bounds. The formula already proved for them passes to \(a_r\) by NW-12, using strong convergence of \(x(a_j)_r\) and of
\(J\sigma_{-i/2}((a_j)_r^*)J\) on \(\Lambda(x)\).

Finally assume that \(a\) is entire. Its norm-continuous orbit and that of the fixed element \(\sigma_{-i/2}(a^*)\) give

\[
a_r\to a,\qquad
\sigma_{-i/2}(a_r^*)\to\sigma_{-i/2}(a^*)
\quad\hbox{in operator norm}.
\]

For the second equality, analytic continuation of (CX.15) is also the Gaussian average of the orbit of \(\sigma_{-i/2}(a^*)\). This follows by a contour shift, or by uniqueness of the entire continuation of the commuting Gaussian and real-translation operations. Finite horizontal strips are uniformly bounded because
\(\|\sigma_{t+is}(a)\|=\|\sigma_{is}(a)\|\).
Pass once more through the GNS graph theorem. This proves (CX.13–14) on the full stated domain. \(\square\)

## Three motions and their analytic domains

Define

\[
\alpha_t(x)=u_t\sigma_t(x)u_t^*,\qquad
\rho_t(x)=u_t\sigma_t(x),\qquad
V_t=u_t\Delta^{it}.
\tag{CX.16}
\]

The first is a strongly* continuous group of normal *-automorphisms of \(M\). The second is a group of linear isometries of \(M\), continuous in the strong* topology on each orbit. The third is a strongly continuous unitary group on \(H\). Every group law follows by inserting (CX.2); no commutation of \(u_t\) with \(\Delta\) is asserted.

The real identities

\[
\begin{aligned}
\rho_t(bxa)&=\alpha_t(b)\rho_t(x)\sigma_t(a),\\
\sigma_t(x^*y)&=\rho_t(x)^*\rho_t(y),\\
\alpha_t(xy^*)&=\rho_t(x)\rho_t(y)^*
\end{aligned}
\tag{CX.17}
\]

will also be used at complex parameters, with conjugated parameters wherever a star occurs. Since \(\sigma\) preserves \(\varphi\),

\[
\rho_t(\mathfrak n)=\mathfrak n,\qquad
\Lambda(\rho_t(x))=V_t\Lambda(x),\qquad
\|\Lambda(\rho_t(x))\|=\|\Lambda(x)\|.
\tag{CX.18}
\]

Let \(\mathcal A,\mathcal B,\mathcal C\) be the entire elements for \(\sigma,\alpha,\rho\), respectively, with operator-norm entire continuations. The first two are *-algebras and the third is a linear space. Each is sigma-strong* dense in \(M\): Gaussian averages of any orbit are entire and tend to the original element. The norm integral construction uses the Gaussian kernel in \(L^1(\mathbb R)\), interpreted as a strong* operator integral before differentiating in operator norm.

Complex continuation of (CX.17) gives

\[
\mathcal B\mathcal C\mathcal A\subseteq\mathcal C,\qquad
\mathcal C^*\mathcal C\subseteq\mathcal A,\qquad
\mathcal C\mathcal C^*\subseteq\mathcal B,
\tag{CX.19}
\]

and, for \(x,y\in\mathcal C\),

\[
\sigma_z(x^*y)=\rho_{\bar z}(x)^*\rho_z(y),
\qquad
\alpha_z(xy^*)=\rho_z(x)\rho_{\bar z}(y)^*.
\tag{CX.20}
\]

For example the second expression is norm-entire in \(z\), agrees with the real orbit and therefore is its unique entire extension. The complex group identities follow by applying uniqueness successively in the parameters.

The domain used for reconstruction is

\[
\mathcal E=\{x\in\mathcal C:
                \rho_z(x)\in\mathfrak n\text{ for every }z\in\mathbb C\}.
\tag{CX.21}
\]

The GNS vector map \(z\mapsto\Lambda(\rho_z(x))\) is norm-entire for every \(x\in\mathcal E\). This implication deserves a proof.

For a right-bounded vector \(\theta\) in the full right Hilbert algebra, let \(R_\theta\) be its bounded right multiplier. WH's mixed multiplication identity gives

\[
R_\theta\Lambda(\rho_z(x))=\rho_z(x)\theta.
\tag{CX.22}
\]

Consequently all scalar tests against vectors \(R_\theta^*\eta\) are entire and bounded on finite horizontal strips. The linear span of these test vectors is dense: its orthogonal complement is the common kernel of the right multipliers, which is zero by nondegeneracy of the full right algebra.

For real \(t,s\), (CX.18) and the complex group law give

\[
\Lambda(\rho_{t+is}(x))=V_t\Lambda(\rho_{is}(x)).
\tag{CX.23}
\]

Fix two imaginary levels \(s_0<s_1\). On each boundary the dense scalar tests in (CX.22) have bound
\(\|\Lambda(\rho_{is_j}(x))\|\) times the test-vector norm. Apply the bounded-strip maximum principle to each test. Taking the supremum over the dense test space proves the same maximum norm bound for the GNS vectors throughout the strip. Thus they are locally norm bounded. Approximation of arbitrary test vectors, followed by the Cauchy coefficient argument of MA-14, proves norm holomorphy. This supplies the analytic GNS conclusion from exactly the membership requirement in (CX.21).

The domain \(\mathcal E\) is invariant under every \(\rho_z\), and

\[
\mathcal B\mathcal E\mathcal A\subseteq\mathcal E.
\tag{CX.24}
\]

Indeed (CX.17) at complex parameters uses left-ideal covariance and the full right multiplier lemma (CX.13) for the factor \(\sigma_z(a)\). All domains are therefore present; it would not suffice here to know right multiplication only on the finite-star algebra.

There is also a two-sided *-ideal on the reference side:

\[
\mathcal J_0=\operatorname{span}\{x^*y:x,y\in\mathcal E\}
\quad\text{is an ideal of }\mathcal A.
\tag{CX.24a}
\]

Right multiplication by \(a\in\mathcal A\) acts on the second factor through \(\mathcal E\mathcal A\subseteq\mathcal E\); left multiplication is the adjoint of the same assertion for \(a^*\). Taking adjoints interchanges the two factors. Formula (CX.20) also makes this ideal invariant under every \(\sigma_z\). The corresponding ideal on the other side is constructed next.

## Gaussian elements supply all required densities

For \(x\in\mathfrak n\) and \(r>0\), put

\[
x_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}\rho_t(x)\,dt .
\tag{CX.25}
\]

For every complex \(z\),

\[
\begin{aligned}
\rho_z(x_r)&=\sqrt{r/\pi}\int_{\mathbb R}
                       e^{-r(t-z)^2}\rho_t(x)\,dt,\\
\Lambda(\rho_z(x_r))&=\sqrt{r/\pi}\int_{\mathbb R}
                       e^{-r(t-z)^2}V_t\Lambda(x)\,dt.
\end{aligned}
\tag{CX.26}
\]

The first integral is a strong* operator integral and the second is a Hilbert norm integral. To prove their compatibility, use the same finite Riemann sums. They lie in the graph of \(\Lambda\), are uniformly bounded in operator norm by the scalar absolute-integral bound, and converge in the two stated topologies. NW-12 puts the limiting pair in that graph. Thus \(x_r\in\mathcal E\), with

\[
\|\rho_z(x_r)\|\leq e^{r(\operatorname{Im}z)^2}\|x\|,
\qquad
\|\Lambda(\rho_z(x_r))\|
 \leq e^{r(\operatorname{Im}z)^2}\|\Lambda(x)\|.
\tag{CX.27}
\]

Differentiation of the Gaussian under its locally uniform integrable bounds proves norm-entire dependence in each norm.

As \(r\to\infty\),

\[
x_r\to x\ \hbox{strongly*},\qquad
\Lambda(x_r)\to\Lambda(x)\ \hbox{in norm},\qquad
\|x_r\|\leq\|x\|.
\tag{CX.28}
\]

The first limit uses strong* continuity of the orbit on each test vector; the second uses strong continuity of \(V_t\). Both are the ordinary approximate-identity estimate for a positive Gaussian of integral one.

It follows that \(\Lambda(\mathcal E)\) is dense in \(H\). There is also a net \(e_j\in\mathcal E\), \(\|e_j\|\leq1\), tending strongly* to \(1\). To construct it, take the finite positive contractions \(f_i\to1\) from WG-008, and approximate each \(f_i\) by (CX.25) on each prescribed finite set of strong* tests to any prescribed tolerance. Direct the finite test sets and tolerances, and choose the two successive approximations. This is a bounded net; no countable strong* dense set is presumed.

Set

\[
\mathcal I=\operatorname{span}\{xy^*:x,y\in\mathcal E\}.
\tag{CX.29}
\]

It is a *-ideal of \(\mathcal B\), and is stable under every \(\alpha_z\), by (CX.20) and (CX.24). It is in particular a *-algebra. Its represented operator algebra is nondegenerate and has bicommutant \(M\). For detail, \(e_je_j^*\in\mathcal I\) tends strongly to \(1\). If \(b\in\mathcal B\), then \(be_je_j^*\in\mathcal I\) and tends strongly to \(b\). The strong closure of \(\mathcal I\) therefore contains the sigma-strong* dense algebra \(\mathcal B\), and equals \(M\).

## Constructing the new GNS map

For a finite sum in \(\mathcal I\), propose

\[
\eta\!\left(\sum_{k=1}^n x_ky_k^*\right)
 =\sum_{k=1}^n x_kJ\Lambda(\rho_{-i/2}(y_k)).
\tag{CX.30}
\]

The map is well-defined, linear and injective, and its range is dense in \(H\).

**Proof of well-definedness.** Write \(r(x)=\rho_{-i/2}(x)\). If
\(z=\sum_kx_ky_k^*\), expand the squared norm of the proposed vector. Antiunitarity of \(J\), followed by (CX.13), gives

\[
\begin{aligned}
\left\|\sum_kx_kJ\Lambda(r(y_k))\right\|^2
&=\sum_{j,k}
 \langle\Lambda(r(y_j)),
             Jx_j^*x_kJ\Lambda(r(y_k))\rangle\\
&=\sum_{j,k}
 \langle\Lambda(r(y_j)),
       \Lambda(r(y_k)\sigma_{-i/2}(x_k^*x_j))\rangle\\
&=\sum_j\langle\Lambda(r(y_j)),\Lambda(r(z^*x_j))\rangle .
\end{aligned}
\tag{CX.31}
\]

The analytic element \(x_k^*x_j\) belongs to \(\mathcal A\), by (CX.19). The last product uses the first identity of (CX.17). Moreover \(z^*x_j\in\mathcal E\), by (CX.24). Thus every term has its stated finite domain. If \(z=0\), the final sum is zero. Applying this to the difference of two presentations proves well-definedness. Linearity now follows from the formula, noting that \(y\mapsto J\Lambda(r(y))\) is conjugate-linear, as is \(y\mapsto y^*\).

For \(b\in\mathcal B\) and \(z\in\mathcal I\), the formula gives

\[
\eta(bz)=b\eta(z),\qquad
\eta(zb)=J\alpha_{-i/2}(b^*)J\eta(z).
\tag{CX.32}
\]

For the second identity it is enough to set \(z=xy^*\), write \(zb=x(b^*y)^*\), and use
\(\rho_{-i/2}(b^*y)=\alpha_{-i/2}(b^*)\rho_{-i/2}(y)\).
Conjugation by \(J\) puts the bounded factor in \(M'\), so it commutes with \(x\).

For fixed \(y\in\mathcal E\), the contractions of CX-05 give

\[
\eta(e_jy^*)\to J\Lambda(\rho_{-i/2}(y)).
\tag{CX.33}
\]

The vectors on the right form a dense set because \(\rho_{-i/2}\mathcal E=\mathcal E\) and \(\Lambda(\mathcal E)\) is dense. Hence \(\eta(\mathcal I)\) is dense. Finally, if \(\eta(z)=0\), apply (CX.32) with \(b\in\mathcal I\). It gives \(z\eta(b)=\eta(zb)=0\). Density of the range forces \(z=0\). This proves injectivity. \(\square\)

## The conjugation identity makes a Hilbert algebra

Transfer multiplication and adjoint from \(\mathcal I\) to
\(\mathcal H_0=\eta(\mathcal I)\):

\[
\eta(z)\eta(w)=\eta(zw),\qquad
\eta(z)^\sharp=\eta(z^*).
\tag{CX.34}
\]

These operations are well-defined by injectivity. Left multiplication by \(\eta(z)\) is exactly the bounded operator \(z\in M\); its adjoint is left multiplication by \(\eta(z^*)\), using the Hilbert inner product.

Define the complex algebraic action

\[
W_z\eta(b)=\eta(\alpha_z(b)),\qquad b\in\mathcal I.
\tag{CX.35}
\]

For \(b=xy^*\), formula (CX.30) becomes

\[
W_z\eta(xy^*)
 =\rho_z(x)J\Lambda(\rho_{\bar z-i/2}(y)).
\tag{CX.36}
\]

This is norm-entire: the first factor is operator-norm entire, and the two conjugations in the second factor turn its antiholomorphic parameter into a holomorphic vector. For real \(t\), it is the restriction of the explicit unitary

\[
K_t=u_tJu_tJ\Delta^{it}.
\tag{CX.37}
\]

Indeed insert \(\rho_t(x)=u_t\sigma_t(x)\) and
\(\Lambda(\rho_{t-i/2}(y))=u_t\Delta^{it}\Lambda(\rho_{-i/2}(y))\)
in (CX.36), and commute the \(M'\)-factor \(Ju_tJ\) past the \(M\)-factor \(\sigma_t(x)\). The cocycle law proves that \(K_sK_t=K_{s+t}\); \(J\Delta^{it}=\Delta^{it}J\) and \(M\) commutes with \(JMJ\) in that calculation. The group is strongly continuous.

The decisive imaginary-time identity is

\[
W_{-i/2}\eta(b)=J\eta(b^*)\qquad(b\in\mathcal I).
\tag{CX.38}
\]

For \(b=xy^*\), the left side of (CX.38) is
\(\rho_{-i/2}(x)J\Lambda(y)\).
The right side is
\(JyJ\Lambda(\rho_{-i/2}(x))\).
These are equal by the full-domain symmetry (CX.12). Linearity gives the identity for every finite sum.

Apply CX-02 to \(K_t\) on the dense invariant space \(\mathcal H_0\). The positive self-adjoint operator

\[
Q=\overline{W_{-i/2}|_{\mathcal H_0}}
\]

is injective, and (CX.38) gives

\[
S_0\eta(b)=\eta(b^*)=JW_{-i/2}\eta(b),\qquad
\overline{S_0}=JQ.
\tag{CX.39}
\]

Thus the involution is closable. Its closed graph is invariant under interchange of its two coordinates, since the initial graph has that property; hence its closure is an involution on its actual range domain.

Products are dense in \(H\). If \(\xi\) is orthogonal to all \(\eta(zw)=z\eta(w)\), then \(z^*\xi=0\) for every \(z\in\mathcal I\), because \(\eta(\mathcal I)\) is dense. Nondegeneracy of \(\mathcal I\) gives \(\xi=0\). We have now verified every left Hilbert-algebra axiom: dense vector space, bounded left multiplication, its adjoint identity, dense products and closable involution.

The closed involution has polar conjugation \(J\) and positive part \(Q\), literally on the present Hilbert space. No standard-form identification has been inserted. The algebraic action \(W_z\) has the adjoint and star identities obtained by continuation from real \(t\). Equation (CX.38) gives its modular inner-product identity; equivalently, (CX.39) and CX-02 identify its modular data directly:

\[
\Delta_0=Q^2,\qquad \Delta_0^{it}=K_t.
\tag{CX.40}
\]

Thus \(\mathcal H_0\) is a Tomita algebra, and is a graph core for every real modular power by CX-02.

## The weight obtained from the completed algebra

Apply WH's full Hilbert-algebra-to-weight construction to \(\mathcal H_0\). Its generated left von Neumann algebra is \(\mathcal I''=M\). It supplies a faithful normal semifinite weight \(\psi\), on this very algebra, whose GNS Hilbert space can be identified with \(H\) and whose GNS map satisfies

\[
\Lambda_\psi(z)=\eta(z)\qquad(z\in\mathcal I).
\tag{CX.41}
\]

Here the assertion includes \(\mathcal I\subseteq
\mathfrak n_\psi\cap\mathfrak n_\psi^*\), the precise finite-domain identities of WH, and normality for arbitrary increasing positive nets. There is no finiteness assertion about \(\psi(1)\).

The full completion retains the closed involution and generated algebra. MF and (CX.40) therefore give

\[
J_\psi=J,\qquad
\Delta_\psi^{it}=K_t,\qquad
\sigma_t^\psi=\alpha_t.
\tag{CX.42}
\]

The last identity follows because the factor \(Ju_tJ\) in (CX.37) commutes with \(M\). It includes invariance of \(\psi\) on the entire positive cone, finite or infinite.

A second exact finite-domain statement is

\[
\mathcal E^*\subseteq\mathfrak n_\psi,\qquad
\Lambda_\psi(y^*)=J\Lambda(\rho_{-i/2}(y))
\quad(y\in\mathcal E).
\tag{CX.43}
\]

To prove it, use \(e_j\in\mathcal E\) from CX-05. Then \(e_jy^*\in\mathcal I\), these elements are uniformly bounded and tend strongly to \(y^*\), and their GNS vectors, by (CX.33) and (CX.41), converge in norm to the stated vector. The GNS graph theorem NW-12 applies to \(\psi\). It proves membership as well as the vector equality. This is the point where the finite mixed domain of the forthcoming relative operator becomes concrete.

Knowing only the final modular automorphism identity in (CX.42) would not yet prove reconstruction of the prescribed cocycle. We identify the relative operator next.

## The entire mixed relative graph is recovered

SI-12 constructs the densely defined closed relative map

\[
T=\overline{T_0},\qquad
T_0\Lambda(x)=\Lambda_\psi(x^*),\quad
x\in\mathfrak n_\varphi\cap\mathfrak n_\psi^*.
\tag{CX.44}
\]

The source and target are the two specified GNS Hilbert spaces; the identification (CX.41) now places both on \(H\). We will show that \(\Lambda(\mathcal E)\) is a core for this full operator. Merely showing that it is dense in \(H\) would not suffice.

For a mixed finite element \(x\), (CX.18) shows that \(\rho_t(x)\in\mathfrak n_\varphi\). On the other side,

\[
\rho_t(x)^*=u_t^*\alpha_t(x^*)\in\mathfrak n_\psi,
\tag{CX.45}
\]

because \(\alpha=\sigma^\psi\) preserves that ideal. Its two GNS orbit vectors are

\[
\begin{aligned}
\Lambda(\rho_t(x))&=V_t\Lambda(x),\\
\Lambda_\psi(\rho_t(x)^*)&=u_t^*\Delta_\psi^{it}\Lambda_\psi(x^*).
\end{aligned}
\tag{CX.46}
\]

Both are strongly continuous unitary orbits. In fact \(u_t^*\) is an \(\alpha\)-cocycle, since

\[
u_s^*\alpha_s(u_t^*)=\sigma_s(u_t^*)u_s^*=u_{s+t}^*,
\]

so the unitaries in the second line form a group.

Take the Gaussian \(x_r\) from (CX.25), using this mixed \(x\). It belongs to \(\mathcal E\), by CX-05. Applying the GNS graph theorem for both weights to the same Riemann sums gives, in addition to (CX.26),

\[
\Lambda_\psi(x_r^*)
 =\sqrt{r/\pi}\int_{\mathbb R}
       e^{-rt^2}u_t^*\Delta_\psi^{it}\Lambda_\psi(x^*)\,dt.
\tag{CX.47}
\]

The scalar Gaussian here is real; taking adjoints of the finite sums therefore introduces no parameter ambiguity. The two strongly continuous unitary orbits give

\[
\Lambda(x_r)\to\Lambda(x),\qquad
\Lambda_\psi(x_r^*)\to\Lambda_\psi(x^*)
\quad\hbox{in norm}.
\tag{CX.48}
\]

Thus every pair in the initial graph (CX.44) is a norm limit of graph pairs with \(x_r\in\mathcal E\). Since that initial graph is itself a core for \(T\), \(\Lambda(\mathcal E)\) is a core for \(T\).

On this smaller graph, (CX.43) gives

\[
T\Lambda(y)=J\Lambda(\rho_{-i/2}(y))
\qquad(y\in\mathcal E).
\tag{CX.49}
\]

Apply CX-02 to the unitary group \(V_t=u_t\Delta^{it}\) on
\(\mathcal D=\Lambda(\mathcal E)\). Its complex action is the norm-entire GNS continuation proved in CX-04; faithfulness of \(\Lambda\), (CX.21) and its translation invariance make this an algebraic group on \(\mathcal D\). We obtain a positive injective self-adjoint \(P\) with

\[
P=\overline{\Lambda(y)\mapsto
                     \Lambda(\rho_{-i/2}(y))},\qquad
V_t=P^{2it}.
\tag{CX.50}
\]

Taking graph closures in (CX.49), using the just proved core assertion, yields the exact operator identities

\[
T=JP,\qquad T^*T=P^2,\qquad
(T^*T)^{it}=u_t\Delta^{it}.
\tag{CX.51}
\]

In particular \(D(T)=D(P)\). Equality here follows from equality of graph closures on a demonstrated common core. It is not inferred from agreement of coefficient formulas on a merely dense vector set.

## Existence, uniqueness and the prescribed cocycle

**Theorem.** Every unitary modular cocycle satisfying (CX.2) is the balanced-matrix cocycle of a unique faithful normal semifinite weight:

\[
[D\psi:D\varphi]_t=u_t\qquad(t\in\mathbb R).
\tag{CX.52}
\]

Its modular group is \(x\mapsto u_t\sigma_t^\varphi(x)u_t^*\).

**Proof of existence.** Represent \(M\) on \(H_\varphi\), and put the opposite weight \(\varphi^{\mathrm{opp}}\) on its commutant, as in SI-02. The ordinary relative identification SI-12 gives

\[
\frac{d\psi}{d\varphi^{\mathrm{opp}}}=T^*T=P^2,\qquad
\frac{d\varphi}{d\varphi^{\mathrm{opp}}}=\Delta.
\tag{CX.53}
\]

The latter is the same identification with identical weights and the ordinary closed Tomita map. SI-14's spatial formula for the balanced-matrix cocycle and (CX.51) now give

\[
[D\psi:D\varphi]_t
  =P^{2it}\Delta^{-it}
  =u_t.
\]

The construction in CX-08 already proves faithfulness, normality and semifiniteness without a state reduction.

**Proof of uniqueness.** If another faithful normal semifinite weight \(\chi\) has the same cocycle, SI-14 with the same commutant reference implies

\[
\left(\frac{d\chi}{d\varphi^{\mathrm{opp}}}\right)^{it}
 =u_t\Delta^{it}
 =\left(\frac{d\psi}{d\varphi^{\mathrm{opp}}}\right)^{it}
\quad(t\in\mathbb R).
\tag{CX.54}
\]

Equality of these unitary groups implies equality of their positive injective self-adjoint operators. Here is an explicit spectral-calculus justification. For such an operator \(A\), let \(L=\log A\), with its spectral domain. The scalar integral and bounded functional calculus give

\[
(L-iI)^{-1}=i\int_0^\infty e^{-t}A^{-it}\,dt.
\tag{CX.54a}
\]

The integral is strong and norm bounded by one. The scalar identity is \(i\int_0^\infty e^{-t}e^{-it\lambda}\,dt=(\lambda-i)^{-1}\), for real \(\lambda\). Thus the group determines this resolvent, its range \(D(L)\), and \(L\) on that range. It determines \(A=\exp L\), with the full spectral domain. SC-10's injectivity of the spatial derivative in its normal numerator therefore gives \(\chi=\psi\) on \(M_+\), including infinite values. \(\square\)

The zero algebra causes no exception: its unique weight and identity unitary family satisfy the statements with zero Hilbert space. On every nonzero algebra, no finite total mass is required.

## A formula that determines the reconstructed finite values

The construction gives an explicit dense-domain measurement. For \(x,y\in\mathcal E\), both adjoints belong to \(\mathfrak n_\psi\), and

\[
\psi(xy^*)
 =\left\langle
    \Lambda(\rho_{-i/2}(x)),
    \Lambda(\rho_{-i/2}(y))
   \right\rangle .
\tag{CX.55}
\]

The left side means the linear extension of the weight to \(\mathfrak m_\psi\), whose membership follows from \(xy^*=(x^*)^*y^*\). For detail,

\[
\psi(xy^*)=
\langle\Lambda_\psi(y^*),\Lambda_\psi(x^*)\rangle
=\langle J\Lambda(\rho_{-i/2}(y)),
         J\Lambda(\rho_{-i/2}(x))\rangle,
\]

which is (CX.55) by antiunitarity. In particular

\[
\psi(xx^*)=\|\Lambda(\rho_{-i/2}(x))\|^2.
\tag{CX.56}
\]

The formula explains why real-time implementation alone loses information. Replacing \(u_t\) by \(c^{it}u_t\), \(c>0\), preserves \(\alpha_t\), while its analytic value at \(-i/2\) is multiplied by \(\sqrt c\). Formula (CX.56) therefore multiplies the new weight by \(c\).

More generally the full mixed domain is described by the relative graph:

\[
\overline{\{(\Lambda_\varphi(x),\Lambda_\psi(x^*)):
          x\in\mathfrak n_\varphi\cap\mathfrak n_\psi^*\}}
  =\{(\xi,JP\xi):\xi\in D(P)\}.
\tag{CX.57}
\]

The closure is in the product Hilbert norm. It does not assert that every vector of \(D(P)\) equals one bounded GNS element. That distinction matters for unbounded weights.

## An arbitrary-cardinality example with noncommuting densities

Let \(I\) be any index set. Choose positive invertible finite matrices \(h_i,k_i\in M_2(\mathbb C)\) and set

\[
M=\prod_{i\in I}M_2(\mathbb C),\quad
\varphi(a)=\sum_i\operatorname{Tr}(h_i a_i),\quad
\psi(a)=\sum_i\operatorname{Tr}(k_i a_i)
\quad(a\geq0).
\tag{CX.58}
\]

The sums are suprema of finite subsums. Each is faithful and normal; arbitrary positive increasing suprema commute with these finite subsums. Finite central block cuts belong to the finite definition algebra and converge strongly to \(1\), proving semifiniteness. The matrices need no common upper or lower spectral bound.

The standard GNS realization is the Hilbert direct sum of Hilbert–Schmidt spaces,

\[
H=\bigoplus_i\operatorname{HS}(\mathbb C^2),\qquad
\Lambda_\varphi(x)=(x_i h_i^{1/2})_i,\qquad
J(Z_i)=(Z_i^*)_i.
\]

The family

\[
(u_t)_i=k_i^{it}h_i^{-it}
\tag{CX.59}
\]

is unitary, strongly continuous and satisfies the \(\sigma^\varphi\)-cocycle law. For strong continuity, first truncate the square-summable family of Hilbert vectors to finitely many blocks; the tail is controlled uniformly in \(t\) by the unitary norm. On the finite truncation ordinary finite-dimensional continuity applies. This proves continuity for an arbitrary index set, without selecting a countable family that separates \(H\).

For the two groups in the proof,

\[
(V_tZ)_i=k_i^{it}Z_i h_i^{-it},\qquad
(K_tZ)_i=k_i^{it}Z_i k_i^{-it}.
\tag{CX.60}
\]

On finite block vectors the positive half operator is

\[
(PZ)_i=k_i^{1/2}Z_i h_i^{-1/2}.
\tag{CX.61}
\]

Its full domain is the set of \(Z\in H\) for which the right side is square summable. This follows by diagonalizing the positive left and right matrix multipliers on each block, and taking their self-adjoint Hilbert direct sum. Finite block truncations converge in that graph norm. Thus \(T=JP\) gives exactly the mixed adjoint map, and (CX.56) recovers \(\psi\). Noncommuting \(h_i,k_i\) generally make \(u_t\) fail the untwisted unitary-group law even on a single block.

## Problems with full solutions

**Problem 1. Detect the weight scale.** For a faithful normal semifinite \(\varphi\), let \(u_t=e^{iat}1\) with \(a\in\mathbb R\). Find the reconstructed weight and both operators \(V_t,K_t\).

**Solution.** The family is a cocycle because its values are scalar and form a unitary group. Its analytic scalar at \(z=-i/2\) is \(e^{a/2}\). Equations (CX.55–56), or uniqueness applied to the scalar transport of SI-14, give
\(\psi=e^a\varphi\). We have

\[
V_t=e^{iat}\Delta_\varphi^{it},\qquad
K_t=e^{iat}e^{-iat}\Delta_\varphi^{it}
     =\Delta_\varphi^{it}.
\]

The first group records the scale through the relative operator; the second implements the unchanged modular automorphisms.

**Problem 2. Check the imaginary-time sign without assuming a trace.** On \(M_2(\mathbb C)\), let
\(\varphi(a)=\operatorname{Tr}(ha)\),
\(\psi(a)=\operatorname{Tr}(ka)\),
where \(h,k>0\) need not commute. Compute \(\rho_{-i/2}(x)\), and verify (CX.56).

**Solution.** The real motion is
\(\rho_t(x)=k^{it}xh^{-it}\), so its entire continuation gives

\[
\rho_{-i/2}(x)=k^{1/2}xh^{-1/2}.
\]

Consequently

\[
\Lambda_\varphi(\rho_{-i/2}(x))=k^{1/2}x,\qquad
\|\Lambda_\varphi(\rho_{-i/2}(x))\|_{\mathrm{HS}}^2
  =\operatorname{Tr}(x^*kx)
  =\operatorname{Tr}(kxx^*)=\psi(xx^*).
\]

Changing the sign of the imaginary parameter would replace both half powers and would not give this weight in general.

**Problem 3. The relative domain can be proper even with scalar cocycles on each block.** In (CX.58), take \(I=\mathbb N\), \(h_n=I_2\), \(k_n=n^2I_2\). Determine \(D(P)\), \(D(P^2)\), and a vector in the first but not the second.

**Solution.** Here \(PZ=(nZ_n)_n\), so

\[
D(P)=\{Z:\sum_n n^2\|Z_n\|_{\mathrm{HS}}^2<\infty\},\qquad
D(P^2)=\{Z:\sum_n n^4\|Z_n\|_{\mathrm{HS}}^2<\infty\}.
\]

For \(Z_n=n^{-2}E_{11}\), the first sum is \(\sum_n n^{-2}<\infty\) and the second is \(\sum_n1=\infty\). All \(u_t\) are bounded unitaries, yet their reconstructed relative operator is unbounded with a proper domain.

**Problem 4. Why density alone was insufficient.** On \(\ell^2(\mathbb N)\), let \(A\) be the positive self-adjoint operator \((A\xi)_n=n\xi_n\), with its square-summability domain. Let \(\mathcal D_0\) consist of the finitely supported sequences whose coordinates sum to zero. Show that \(\mathcal D_0\) is Hilbert-norm dense but is not a core for \(A\).

**Solution.** For a fixed basis vector \(e_k\) and \(N>k\), the vector

\[
e_k-\frac1N\sum_{n=N+1}^{2N}e_n
\]

belongs to \(\mathcal D_0\) and has distance \(N^{-1/2}\) from \(e_k\). Thus every basis vector lies in its Hilbert closure. On \(D(A)\), however, the series
\(\ell(\xi)=\sum_n\xi_n\) converges absolutely and satisfies

\[
|\ell(\xi)|\leq
 \left(\sum_{n=1}^\infty n^{-2}\right)^{1/2}\|A\xi\|.
\]

It is therefore continuous in the graph norm. It vanishes on \(\mathcal D_0\) and on its graph closure, but \(\ell(e_k)=1\). That graph closure is a proper subspace of \(D(A)\). Agreement with a densely defined restriction therefore cannot identify the full operator. CX-09 instead approximates both entries of every mixed finite graph pair, and only then takes the already specified relative graph closure.

## Scope and further uses

The construction proves the inverse theorem for arbitrary strongly continuous unitary cocycles of an NSF weight. It supplies the full analytic right multiplier lemma, dense operator and GNS domains, a faithful normal semifinite reconstructed weight, its exact relative graph, and uniqueness of the weight. Every invocation of the infinite weight is either on its positive cone or on an explicitly verified finite linear domain.

An operator-to-spatial-weight converse can now produce a unitary cocycle in a support corner and apply CX-10 there. That application still has to specify the corner algebra, its faithful reference weight and the comparison of spatial operators. The present theorem does not silently extend a weight through an unspecified quotient. Partial-isometry cocycles, operator-valued weights, crossed-product dual weights and action cohomology retain their separate statements and ownership.

