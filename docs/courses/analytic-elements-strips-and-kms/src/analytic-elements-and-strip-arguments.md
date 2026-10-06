# Analytic elements and strip arguments

*Written by Claude Opus 5.5 (Anthropic), September 2026, extended October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October additions (Lemmas 10.6–10.7, Corollary 10.8, Theorem 10.9 and the revision of the references) are self-checked by the writing AI. Public domain (CC0).*

This lesson develops the complex analysis that modular theory runs on. A one-parameter group of operators \(U_t\) often has orbits \(t\mapsto U_tx\) that continue holomorphically into a horizontal strip of the complex plane. The values of such a continuation on the far edge of the strip define unbounded operators: for the unitary group \(\Delta^{it}\) of a positive injective operator \(\Delta\), they give \(\Delta^{1/2}\) and \(\Delta\) (Theorem 8.1). The same continuations express the Kubo–Martin–Schwinger (KMS) condition, which singles out the modular automorphism group of a weight. The lesson develops these tools in the generality that modular theory needs: uniformly bounded groups on Banach spaces and on dual Banach spaces, arbitrary Hilbert spaces and arbitrary von Neumann algebras, with no separability assumed.

One idea runs through the whole lesson. A function that is continuous on a closed strip, holomorphic inside and zero on one edge vanishes. So an identity that holds on the real line persists on the strip whenever it can be written as a closed condition: a functional that annihilates the orbit, a bounded operator that intertwines two groups, a closed graph, or membership in a von Neumann algebra. Gaussian averages supply many elements whose orbits continue to the whole plane, and uniform boundedness of the group makes every continuation bounded.

Sections 2–6 treat groups on Banach spaces: holomorphy tested by functionals, Gaussian averages, strip functions, analytic generators, and continuation through closed conditions. Section 7 treats conjugate-linear operators and closed involutions, Section 8 unitary groups (with proofs of Stone's theorem and of the analytic vector theorem), and Section 9 automorphism groups of von Neumann algebras. Sections 10 and 11 apply these tools to the strip condition for bounded functionals and for faithful normal semifinite weights. Sections 2–9 use no modular theory. Section 10 uses the modular group only in an example, and Section 11 uses the modular data of a weight, listed at its start.

The lesson assumes basic complex analysis and functional analysis, the spectral theorem for unbounded self-adjoint operators, and the elementary theory of von Neumann algebras. It builds on the lessons Analytic kernels for unbounded modular operators and The KMS boundary condition determines the modular group; Section 1 states in full what it uses from them. An openly available introduction is [Hiai]. The strip condition is the KMS condition of quantum statistical mechanics, which goes back to Kubo and to Martin and Schwinger and was formulated for infinite systems in [Haag–Hugenholtz–Winnink]; Takesaki showed that it characterizes the modular automorphism group.

## 1. Conventions and background

### Conventions

*Scalars and inner products.* All vector spaces are complex. Inner products are linear in the first variable and conjugate-linear in the second. Hilbert spaces are arbitrary; no separability is assumed anywhere.

*Strips.* For a real number \(a\), let
\[
\mathbb S(a)=\{z\in\mathbb C:\ \min(0,a)\le\operatorname{Im}z\le\max(0,a)\}
\tag{1.1}
\]
be the closed horizontal strip between the real axis and the line \(\operatorname{Im}z=a\), and \(\mathbb S^\circ(a)\) its interior (empty when \(a=0\)). The lesson *Analytic kernels for unbounded modular operators* writes \(S_\alpha\) for \(\mathbb S(-\alpha)\), and *The KMS boundary condition determines the modular group* writes \(\overline{\mathcal S}\) for \(\mathbb S(1)\).

### Results used from other lessons

The lesson uses the following facts, together with the facts about weights listed at the start of Section 11, and nothing else. Each names the place where it is proved.

*Standard facts.*

- *Analysis.* Lebesgue's dominated and monotone convergence theorems and Fatou's lemma (Measure and Hilbert space tools for Haar integration, Theorems 2.1 and 2.2), and Fubini's theorem ([Fremlin, Measure Theory, Volume 2, Theorem 252B](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm), free; Volumes 1 and 2 of this text are the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)). For scalar holomorphic functions, from Cauchy's theorem for cycles and its consequences: the Cauchy integral formula (Theorem 2.3) and the Cauchy power series (Theorem 3.2); Morera's theorem, that a continuous function whose integral around every closed triangle vanishes is holomorphic (Theorem 3.4); the identity theorem (Theorem 3.7); the maximum modulus principle on rectangles (the proof of Theorem 3.6 applies to a closed rectangle, with \(r_0\) the distance from \(c\) to its boundary, which the circle \(|z-c|=r_0\) meets); the fact that a locally uniform limit of holomorphic functions is holomorphic (Corollary 3.5); and Liouville's theorem, that a bounded entire function is constant, which follows from the Cauchy estimates (Corollary 3.3).
- *Harmonic functions and normal families.* Real and imaginary parts of holomorphic functions are harmonic, and a real harmonic function on a domain that attains a local maximum is constant (the maximum principle); Morera's theorem; Montel's theorem: a locally bounded family of holomorphic functions on an open set has, in every sequence, a subsequence that converges uniformly on compact subsets. These are [Lebl CA, Section 7.1 and Theorem 7.1.11, Theorem 3.3.5, Theorem 6.2.2](https://www.jirka.org/ca/), the text of the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50).
- *Normed spaces.* The Hahn–Banach theorem (Hahn–Banach, Baire and the basic theorems on Banach spaces, Corollary 2.3(2) and (3)): in a normed space \(X\), \(\|x\|=\sup\{|f(x)|:f\in X^*,\ \|f\|\le1\}\), and a closed subspace is the common zero set of the functionals in \(X^*\) that vanish on it. The uniform boundedness theorem (Theorem 4.2 there): a family of bounded linear maps from a Banach space to a normed space that is bounded at each point is bounded in norm. The Banach–Alaoglu theorem (Weak topologies, Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian, Theorem 3.1): the closed unit ball of a dual space is weak\*-compact.
- *Hilbert spaces.* The Riesz representation theorem, and the projection theorem: a closed subspace \(L\) of \(H\) satisfies \(H=L\oplus L^\perp\) and \(L=L^{\perp\perp}\). Both are proved in Hilbert spaces and compact operators, Theorems 2.2 and 2.3, the projection theorem for real and complex Hilbert spaces alike. We use it for the real Hilbert space obtained from a complex one by keeping only the real part of the inner product.
- *Spectral calculus.* A self-adjoint operator \(A\) has a spectral measure \(P\). Every Borel function \(f\) defines \(f(A)=\int f\,dP\) on the exact domain of the vectors \(\xi\) with \(\int|f|^2d\mu_\xi<\infty\), where \(\mu_\xi=\langle P(\cdot)\xi,\xi\rangle\), and then \(\|f(A)\xi\|^2=\int|f|^2d\mu_\xi\). A positive self-adjoint operator has a unique positive self-adjoint square root, and \(D(A)\) is a core for \(A^{1/2}\). For a positive injective \(A\) the calculus gives the powers \(A^z\) and the logarithm \(\log A\), and the spectral projections \(1_{[1/n,n]}(A)\) increase strongly to \(1\). If a unitary \(U\) satisfies \(UAU^*=A\), domains included, then \(U\) commutes with every \(f(A)\), in particular with every spectral projection of \(A\). These are proved in Spectral calculus with its domains retained: the spectral measure and the domains in SK-05 and SK-06; the square root, its uniqueness, the powers and the logarithm in SK-07; and the commutation in SK-08, by the transport formula (SK.23) with \(W=U\). The cutoffs of SK-09 give the rest: for \(\xi\in D(A^{1/2})\), the vectors \(1_{[0,n]}(A)\xi\) lie in \(D(A)\) and converge to \(\xi\) in the graph norm of \(A^{1/2}\); and \(1_{[1/n,n]}(A)\) increases strongly to \(1_{(0,\infty)}(A)=1\), because the spectral measure of a positive injective operator is carried by \((0,\infty)\).
- *Von Neumann algebras.* Let \(N\subseteq B(H)\) be a von Neumann algebra. The bicommutant theorem: \(N=N''\). The predual \(N_*\) is the space of \(\sigma\)-weakly continuous linear functionals on \(N\), and \(N\) is its dual. A \(*\)-automorphism of \(N\) is isometric and normal, hence \(\sigma\)-weakly continuous. Multiplication is separately \(\sigma\)-weakly continuous, and on bounded sets the weak and \(\sigma\)-weak topologies agree. States of a unital C\*-algebra have norm one. These are proved in the course *Foundations of von Neumann algebras*: the bicommutant theorem in The double commutant theorem, Theorem 4.4; the duality in Compact and trace-class operators, Theorem 9.4(b); isometry in C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients, Corollary 4.6 and normality in The universal enveloping von Neumann algebra of a C\*-algebra, and W\*-algebras, Corollary 11.4; the two facts on topologies in Compact and trace-class operators, Proposition 8.6(a) and Lemma 8.5; and the norm of a state in Representations and positive functionals, Proposition 4.2(3).

*From the prerequisite lessons.* The lesson Analytic kernels for unbounded modular operators proves the following, in its sections MA-02, MA-08, MA-09 and MA-15.

- *Vector-valued integrals.* Let \(B\) be a Banach space and \(f:\mathbb R\to B\) a norm-continuous function with \(\|f(t)\|\le m(t)\) for an integrable function \(m\). Then \(f\) has a norm integral \(\int_{\mathbb R}f(t)\,dt\): the Riemann integrals over compact intervals exist, and they converge in norm as the intervals grow. The integral is a norm limit of Riemann sums over compact intervals, it satisfies \(\|\int f\|\le\int\|f\|\), and bounded linear maps pass through it. The same holds for integrals of continuous functions over circles. We use the Gaussian kernels
\[
g_r(t)=\sqrt{r/\pi}\,e^{-rt^2}\qquad(r>0),
\tag{1.2}
\]
which are probability densities.
- *Two facts about strips.* Let \(a\neq0\), and let \(\Phi\) be a function with values in a Banach space that is continuous on \(\mathbb S(a)\) and holomorphic on \(\mathbb S^\circ(a)\).
  - *Boundary uniqueness.* If \(\Phi\) vanishes on one of the two boundary lines, then \(\Phi=0\).
  - *Bounded-strip maximum principle.* If \(\Phi\) is bounded and \(\|\Phi\|\le m\) on both boundary lines, then \(\|\Phi\|\le m\) on \(\mathbb S(a)\).

  We use them mostly for scalar functions. The proof of boundary uniqueness contains a Morera argument across a line, which we use on its own: a function that is continuous on an open set and holomorphic off a horizontal line is holomorphic on the whole set. It lets us glue two functions that are holomorphic on adjacent strips and agree on their common line.
- *Spectral domains and strips.* Let \(A\) be positive, self-adjoint and injective, let \(\alpha\neq0\) be real and \(\xi\in H\). Then \(\xi\in D(A^\alpha)\) if and only if the orbit \(t\mapsto A^{it}\xi\) extends to a bounded, norm-continuous function on \(\mathbb S(-\alpha)\) that is norm-holomorphic on its interior. The extension is then \(z\mapsto A^{iz}\xi\).
- *A self-adjointness criterion.* Let \(D\subseteq H\) be a dense subspace and \(U(z):D\to D\) (\(z\in\mathbb C\)) linear maps with \(U(0)=1\) and \(U(z+w)=U(z)U(w)\), such that \(z\mapsto U(z)\xi\) is norm-entire for every \(\xi\in D\). Suppose that each \(U(t)\), \(t\) real, extends to a bounded operator on \(H\), and that \(\sup_t\|U(t)\|<\infty\). If \(U(ia)\) is positive and symmetric on \(D\) for some real \(a\), then it is essentially self-adjoint.

The lesson The KMS boundary condition determines the modular group proves the following, in its sections KM-02 (existence) and KM-05 (uniqueness).

- *The KMS characterization of the modular group.* Let \(\varphi\) be a faithful normal semifinite weight on a von Neumann algebra \(M\), for instance a faithful normal positive functional. Put \(\mathfrak n_\varphi=\{x\in M:\varphi(x^*x)<\infty\}\) and \(\mathfrak a_\varphi=\mathfrak n_\varphi\cap\mathfrak n_\varphi^*\), and extend \(\varphi\) linearly to the span \(\mathfrak m_\varphi\) of the products \(y^*x\) with \(x,y\in\mathfrak n_\varphi\). The modular automorphism group \(\sigma^\varphi\) is the only one-parameter group \(\sigma\) of \(*\)-automorphisms of \(M\) with the following two properties: \(\varphi\circ\sigma_t=\varphi\) on \(M_+\) for all real \(t\); and for all \(x,y\in\mathfrak a_\varphi\), some bounded continuous function \(F\) on \(\mathbb S(1)\), holomorphic inside, satisfies \(F(t)=\varphi(\sigma_t(x)y)\) and \(F(t+i)=\varphi(y\sigma_t(x))\) for real \(t\).

## 2. Holomorphy tested by a norming set of functionals

A function with values in a Banach space \(X\) is *norm-holomorphic* on an open set if it is complex differentiable there in the norm of \(X\). A subspace \(F\subseteq X^*\) *norms* \(X\) if \(\|x\|=\sup\{|f(x)|:f\in F,\ \|f\|\le1\}\) for every \(x\in X\).

**Lemma 2.1** (Holomorphy tested by functionals). Let \(X\) be a Banach space, \(F\subseteq X^*\) a subspace that norms \(X\), \(\Omega\subseteq\mathbb C\) open, and \(\Phi:\Omega\to X\) a function such that \(f\circ\Phi\) is holomorphic for every \(f\in F\).
1. If \(F\) is norm closed, then \(\Phi\) is bounded on every compact subset of \(\Omega\).
2. If \(\Phi\) is bounded on compact subsets, then \(\Phi\) is norm-holomorphic. More precisely, let the closed disc \(|z-z_0|\le R\) lie in \(\Omega\) and let \(C\) bound \(\|\Phi\|\) on it. There are \(b_n\in X\) with \(\|b_n\|\le CR^{-n}\) and
\[
\Phi(z)=\sum_{n\ge0}b_n(z-z_0)^n\quad\text{in norm, for }|z-z_0|<R.
\tag{2.1}
\]

**Proof.** (1) Let \(K\subseteq\Omega\) be compact. Each \(f\circ\Phi\) is continuous, hence bounded on \(K\). The map \(\iota:X\to F^*\), \(\iota(x)(f)=f(x)\), is a linear isometry because \(F\) norms \(X\). So \(\{\iota(\Phi(z)):z\in K\}\) is a family of bounded functionals on the Banach space \(F\) that is bounded at each point of \(F\). The uniform boundedness theorem bounds its norms, and since \(\iota\) is isometric, \(\|\Phi\|\) is bounded on \(K\).

(2) First replace \(F\) by its norm closure \(\overline F\), which still norms \(X\). If \(f_k\in F\) tend to \(f\in\overline F\) in norm, then \(|f_k(\Phi(z))-f(\Phi(z))|\le\|f_k-f\|\,\|\Phi(z)\|\). Since \(\Phi\) is bounded on compact sets, \(f_k\circ\Phi\to f\circ\Phi\) uniformly on compact sets. A locally uniform limit of holomorphic functions is holomorphic (Cauchy formula). So we may assume \(F\) closed, and \(\iota:X\to F^*\) is an isometry as in (1).

Fix the disc and \(C\). For \(f\in F\) and \(n\ge0\) put
\[
c_n(f)=\frac1{2\pi i}\oint_{|\zeta-z_0|=R}\frac{f(\Phi(\zeta))}{(\zeta-z_0)^{n+1}}\,d\zeta .
\]
This is linear in \(f\), and \(|c_n(f)|\le CR^{-n}\|f\|\), so \(c_n\in F^*\) with \(\|c_n\|\le CR^{-n}\). By the scalar Cauchy series, \(f(\Phi(z))=\sum_nc_n(f)(z-z_0)^n\) for \(|z-z_0|<R\). Because \(\|c_n\|\le CR^{-n}\), the series \(\sum_nc_n(z-z_0)^n\) converges in the norm of \(F^*\), and its value at each \(f\) is \(f(\Phi(z))\). So it equals \(\iota(\Phi(z))\). Hence \(\iota\circ\Phi\) is a locally uniform limit of polynomials with coefficients in \(F^*\), so it is norm continuous on the open disc; since \(\iota\) is isometric, so is \(\Phi\). Now fix \(R'<R\). The function \(\Phi\) is norm continuous on the circle \(|\zeta-z_0|=R'\), so the integrals
\[
b_n=\frac1{2\pi i}\oint_{|\zeta-z_0|=R'}\frac{\Phi(\zeta)}{(\zeta-z_0)^{n+1}}\,d\zeta
\]
exist in \(X\) as Riemann integrals. Applying \(f\in F\) and using the scalar Cauchy formula on both circles gives \(\iota(b_n)=c_n\). Therefore \(\|b_n\|\le CR^{-n}\) and (2.1) holds in the norm of \(X\). A norm-convergent power series is norm-holomorphic inside its disc of convergence. \(\square\)

Three cases are used below. \(F=X^*\) norms \(X\) by the Hahn–Banach theorem. If \(X=F^*\) is the dual of a Banach space \(F\), the canonical copy of \(F\) in \(X^*\) norms \(X\) by the definition of the dual norm. If \(X=H\) is a Hilbert space and \(D\subseteq H\) is dense, the functionals \(\langle\,\cdot\,,\eta\rangle\) with \(\eta\in D\) span a subspace that norms \(H\). In this last case, Lemma 2.1(2) says that a function that is bounded on compact sets, and whose scalar tests \(\langle\Phi(\cdot),\eta\rangle\) with \(\eta\in D\) are holomorphic, is norm-holomorphic.

## 3. Bounded one-parameter groups and Gaussian averages

A reference for this section and the next is [Kustermans 1997].

**Setting.** Throughout Sections 3–6, \(X\) is a Banach space, \(F\subseteq X^*\) is a subspace, closed in norm, that norms \(X\), and \(U=(U_t)_{t\in\mathbb R}\) is a family of bounded operators on \(X\) with \(U_0=1\) and \(U_{s+t}=U_sU_t\). We assume:
- **(G1)** \(f\circ U_t\in F\) for every \(f\in F\) and \(t\in\mathbb R\);
- **(G2)** \(t\mapsto f(U_tx)\) is continuous for every \(x\in X\) and \(f\in F\);
- **(G3)** \(M:=\sup_t\|U_t\|<\infty\);
- **(G4)** for every \(x\in X\) and every continuous integrable \(k:\mathbb R\to\mathbb C\) there is an element \(U_kx\in X\) with
\[
f(U_kx)=\int_{\mathbb R}k(t)\,f(U_tx)\,dt\qquad(f\in F).
\tag{3.1}
\]

Since \(F\) norms \(X\), the element in (G4) is unique. We write \(\tau\) for the weak topology \(\sigma(X,F)\), and "\(\tau\)-continuous" for continuity in it. By (G1) each \(U_t\) is \(\tau\)-continuous.

Two cases satisfy (G1)–(G4) whenever (G3) holds.
- **(N)** *Norm-continuous groups.* \(F=X^*\), and \(t\mapsto U_tx\) is norm continuous for every \(x\). Then (G1) and (G2) are clear, and \(U_kx\) is the norm integral \(\int k(t)U_tx\,dt\) of Section 1, which exists because the integrand is norm continuous and bounded by \(M\|x\|\,|k(t)|\); bounded functionals pass through it. A strongly continuous unitary group on a Hilbert space is the main example, with \(M=1\).
- **(W\*)** *Weak\*-continuous groups on a dual space.* \(X=F^*\) for a Banach space \(F\), (G1) holds (equivalently, each \(U_t\) is the adjoint of a bounded operator on \(F\)), and (G2) holds. Then \(f\mapsto\int k(t)f(U_tx)\,dt\) is a bounded linear functional on \(F\), of norm at most \(M\|k\|_1\|x\|\), that is, an element \(U_kx\) of \(X\). The main example is a \(\sigma\)-weakly continuous group of \(*\)-automorphisms of a von Neumann algebra, with \(F\) the predual and \(M=1\) (Section 9).

In neither case is (G3) automatic: the group \(U_t=e^t\) on \(X=\mathbb C\) satisfies everything in case (N) except (G3). The uniform boundedness theorem only bounds \(\|U_t\|\) for \(t\) in compact sets. Example 4.4 shows that (G3) cannot be dropped from Theorem 4.2(3). This lesson works only with uniformly bounded groups; for groups with \(\|U_t\|\le Me^{\omega|t|}\), the definitions below would need exponential weights.

**Proposition 3.1.**
1. \(U_k\) is linear, \(\|U_kx\|\le M\|k\|_1\|x\|\), and \(U_sU_k=U_kU_s=U_{k(\cdot-s)}\) for real \(s\).
2. (*Intertwiners.*) Let \((Y,G,V)\) be a second system as in the Setting, and \(B:X\to Y\) a bounded linear map with \(g\circ B\in F\) for \(g\in G\) and \(BU_t=V_tB\) for all \(t\). Then \(BU_kx=V_kBx\). If instead \(B\) is conjugate-linear, with \(\overline{g\circ B}\in F\) for \(g\in G\), then \(BU_kx=V_{\bar k}Bx\).
3. (*Gaussian continuation.*) For \(x\in X\), \(r>0\) and \(z\in\mathbb C\) put \(G^x_r(z)=U_{k}x\) with \(k(t)=g_r(t-z)\), and \(x_r=G^x_r(0)\). Then \(G^x_r\) is norm-entire,
\[
\|G^x_r(z)\|\le Me^{r(\operatorname{Im}z)^2}\|x\|,\qquad U_sG^x_r(z)=G^x_r(z+s),\qquad G^x_r(t)=U_tx_r
\tag{3.2}
\]
for real \(s,t\).
4. (*Approximation.*) \(\|x_r\|\le M\|x\|\), and \(x_r\to x\) in \(\tau\) as \(r\to\infty\). In case (N), \(x_r\to x\) in norm.

**Proof.** (1) Linearity and the bound follow from (3.1), since \(F\) norms \(X\) and \(|f(U_tx)|\le M\|f\|\|x\|\). For \(f\in F\), (G1) gives \(f(U_sU_kx)=(f\circ U_s)(U_kx)=\int k(t)f(U_{s+t}x)\,dt\). The substitution \(v=s+t\) turns this into \(f(U_{k(\cdot-s)}x)\). The same computation applies to \(U_kU_sx\), whose integrand is \(k(t)f(U_tU_sx)\).

(2) For \(g\in G\), \(g(BU_kx)=(g\circ B)(U_kx)=\int k(t)\,g(BU_tx)\,dt=\int k(t)\,g(V_tBx)\,dt=g(V_kBx)\). In the conjugate-linear case, \(\overline{g(BU_kx)}=(\overline{g\circ B})(U_kx)=\int k(t)\,\overline{g(V_tBx)}\,dt\), and conjugating gives \(g(V_{\bar k}Bx)\).

(3) Write \(z=u+iv\). Then \(|g_r(t-z)|=e^{rv^2}g_r(t-u)\), so the kernel is integrable with \(\|g_r(\cdot-z)\|_1=e^{rv^2}\), and (1) gives the bound. For \(f\in F\), the function \(z\mapsto f(G^x_r(z))=\int g_r(t-z)f(U_tx)\,dt\) is entire. Indeed, \(|f(U_tx)|\le M\|f\|\|x\|\), and on a compact set of \(z\) the kernel and its complex derivative are bounded by a constant times \((1+|t|)e^{-rt^2/2}\): expand \((t-u)^2\) and use \(2|tu|\le t^2/2+2u^2\), and note that the derivative adds only the factor \(2r(t-z)\). So differentiation under the integral sign is justified by dominated convergence. The bound in (3.2) makes \(G^x_r\) bounded on compact sets, and Lemma 2.1(2) makes it norm-entire. The covariance is (1) with \(k=g_r(\cdot-z)\): \(U_sU_kx=U_{k(\cdot-s)}x\), and \(k(t-s)=g_r(t-(z+s))\). At \(z=0\) it gives \(G^x_r(t)=U_tx_r\).

(4) The bound is (1) with \(\|g_r\|_1=1\). Since \(\int g_r=1\), we have \(f(x_r)-f(x)=\int g_r(t)\bigl(f(U_tx)-f(x)\bigr)\,dt\) for \(f\in F\). Split the integral at \(|t|=\delta\), where \(\delta>0\), and use \(|f(U_tx)-f(x)|\le(M+1)\|f\|\|x\|\) on the outer part:
\[
|f(x_r)-f(x)|\le\sup_{|t|\le\delta}|f(U_tx)-f(x)|+(M+1)\|f\|\|x\|\int_{|t|>\delta}g_r(t)\,dt .
\]
The first term is small for small \(\delta\) by (G2). For fixed \(\delta\) the second tends to \(0\) as \(r\to\infty\). In case (N) the same estimate holds with \(\|U_tx-x\|\) in place of \(|f(U_tx)-f(x)|\). \(\square\)

## 4. Strip functions of orbits

We keep the Setting of Section 3.

**Definition 4.1.** Let \(a\in\mathbb R\) and \(x\in X\). A *strip function* of \(x\) on \(\mathbb S(a)\) is a map \(\Phi:\mathbb S(a)\to X\) such that
- **(S1)** \(\Phi(t)=U_tx\) for every real \(t\);
- **(S2)** \(\Phi\) is \(\tau\)-continuous on \(\mathbb S(a)\);
- **(S3)** \(f\circ\Phi\) is holomorphic on \(\mathbb S^\circ(a)\) for every \(f\in F\).

No boundedness and no norm continuity is assumed. Strip functions of \(x\) and \(y\) add to a strip function of \(x+y\), and scalar multiples behave in the same way.

**Theorem 4.2.**
1. (*Uniqueness.*) Each \(x\) has at most one strip function on \(\mathbb S(a)\); we call it \(\Phi_x\) (or \(\Phi^a_x\)). If \(b\) lies between \(0\) and \(a\), the restriction of \(\Phi^a_x\) to \(\mathbb S(b)\) is \(\Phi^b_x\).
2. (*Covariance.*) \(\Phi_x(z+s)=U_s\Phi_x(z)\) for \(z\in\mathbb S(a)\) and real \(s\).
3. (*Automatic boundedness.*) \(\Phi_x\) is bounded, with \(\sup_{\mathbb S(a)}\|\Phi_x\|\le M\sup\{\|\Phi_x(ib)\|:ib\in\mathbb S(a)\}<\infty\), and it is norm-holomorphic on \(\mathbb S^\circ(a)\).
4. (*Maximum principle and three lines.*) \(\sup_{\mathbb S(a)}\|\Phi_x\|\le M\max(\|x\|,\|\Phi_x(ia)\|)\). If \(a\neq0\), \(t\) is real and \(0\le b/a\le1\), then
\[
\|\Phi_x(t+ib)\|\le M\,\|x\|^{1-b/a}\,\|\Phi_x(ia)\|^{b/a}.
\tag{4.1}
\]
5. (*Smoothing.*) For \(r>0\), the map \(z\mapsto(\Phi_x(z))_r\) is the strip function of \(x_r\) on \(\mathbb S(a)\). It equals the restriction of \(G^x_r\) from Proposition 3.1(3).
6. (*Case (N).*) In case (N), \(\Phi_x\) is norm continuous on \(\mathbb S(a)\).

**Proof.** (1) Let \(\Phi,\Psi\) be strip functions of \(x\) and \(f\in F\). The scalar function \(f\circ(\Phi-\Psi)\) is continuous on \(\mathbb S(a)\) by (S2), holomorphic inside by (S3), and zero on the real line by (S1). Boundary uniqueness makes it zero. Since \(F\) separates the points of \(X\), \(\Phi=\Psi\). The restriction of \(\Phi^a_x\) to \(\mathbb S(b)\) satisfies (S1)–(S3) there.

(2) Fix \(s\). The maps \(z\mapsto U_s\Phi_x(z)\) and \(z\mapsto\Phi_x(z+s)\) are both strip functions of \(U_sx\). For the first, \(f\circ U_s\in F\) by (G1), so \(f\circ U_s\circ\Phi_x\) is continuous and holomorphic inside; for the second, translation preserves (S2) and (S3). At real \(t\) both give \(U_{s+t}x\). Apply (1).

(3) Let \(I=\{ib\in\mathbb S(a)\}\), a compact segment. For each \(f\in F\), \(f\circ\Phi_x\) is continuous, hence bounded on \(I\). As in the proof of Lemma 2.1(1), the uniform boundedness theorem gives \(C:=\sup_I\|\Phi_x\|<\infty\). By (2), \(\Phi_x(t+ib)=U_t\Phi_x(ib)\), so \(\|\Phi_x(t+ib)\|\le MC\). Since \(\Phi_x\) is bounded, Lemma 2.1(2) makes it norm-holomorphic inside.

(4) If \(a=0\) there is nothing to prove. Let \(a\neq0\), \(f\in F\), \(\|f\|\le1\), and \(h=f\circ\Phi_x\). By (3), \(h\) is bounded and continuous on \(\mathbb S(a)\) and holomorphic inside. On the real line \(|h(t)|=|f(U_tx)|\le M\|x\|\). On the other boundary line, (2) gives \(|h(t+ia)|=|f(U_t\Phi_x(ia))|\le M\|\Phi_x(ia)\|\). The bounded-strip maximum principle bounds \(|h|\) by \(M\max(\|x\|,\|\Phi_x(ia)\|)\); taking the supremum over \(f\) gives the first claim. For (4.1) we use the following scalar bound, Hadamard's three lines theorem, and again take the supremum over \(f\).

*Three lines.* Let \(a>0\) and let \(h\) be bounded and continuous on \(\mathbb S(a)\), holomorphic inside, with \(|h|\le m_0\) on \(\mathbb R\) and \(|h|\le m_1\) on \(\mathbb R+ia\). Then \(|h(t+ib)|\le m_0^{1-b/a}m_1^{b/a}\) for \(0\le b\le a\). Indeed, let \(\varepsilon>0\), \(p=\log(m_0+\varepsilon)\), \(q=\log(m_1+\varepsilon)\), and
\[
L(z)=\Bigl(1+\frac{iz}a\Bigr)p-\frac{iz}a\,q .
\]
For \(z=t+ib\) we have \(\operatorname{Re}L(z)=(1-b/a)p+(b/a)q\), which is bounded on \(\mathbb S(a)\). So \(he^{-L}\) is bounded and continuous on \(\mathbb S(a)\), holomorphic inside, and of modulus at most \(1\) on both boundary lines. By the bounded-strip maximum principle its modulus is at most \(1\) everywhere, that is, \(|h(t+ib)|\le(m_0+\varepsilon)^{1-b/a}(m_1+\varepsilon)^{b/a}\). Let \(\varepsilon\to0\). For \(a<0\), apply the bound to \(k(z)=h(-z)\) on \(\mathbb S(-a)\): \(k\) is bounded by \(m_0\) on \(\mathbb R\) and by \(m_1\) on \(\mathbb R-ia\), and \(h(t+ib)=k(-t-ib)\) with \((-b)/(-a)=b/a\). With \(m_0=M\|x\|\) and \(m_1=M\|\Phi_x(ia)\|\) this gives (4.1).

(5) Let \(\Psi(z)=(\Phi_x(z))_r\). For \(f\in F\), (3.1) and (2) give
\[
f(\Psi(z))=\int_{\mathbb R}g_r(t)\,f(U_t\Phi_x(z))\,dt=\int_{\mathbb R}g_r(t)\,f(\Phi_x(z+t))\,dt .
\]
By (3), the integrand is bounded by \(\|f\|\sup\|\Phi_x\|\,g_r(t)\), and it is continuous in \(z\) by (S2). Dominated convergence makes \(f\circ\Psi\) continuous on \(\mathbb S(a)\). On \(\mathbb S^\circ(a)\) the integrand is holomorphic in \(z\), and Fubini's theorem shows that its integral around every closed triangle vanishes; Morera's theorem makes \(f\circ\Psi\) holomorphic. At real \(s\), \(\Psi(s)=(U_sx)_r=U_sx_r\) by Proposition 3.1(1). So \(\Psi\) is a strip function of \(x_r\). The restriction of \(G^x_r\) is another one, by Proposition 3.1(3), since a norm-entire function is \(\tau\)-continuous. Apply (1).

(6) By (5), \(\Phi_x-G^x_r\) is the strip function of \(x-x_r\), and its value at \(ia\) is \(\Phi_x(ia)-(\Phi_x(ia))_r\). By (4),
\[
\sup_{\mathbb S(a)}\|\Phi_x-G^x_r\|\le M\max\bigl(\|x-x_r\|,\ \|\Phi_x(ia)-(\Phi_x(ia))_r\|\bigr).
\]
In case (N) the right side tends to \(0\) as \(r\to\infty\), by Proposition 3.1(4) applied to \(x\) and to \(\Phi_x(ia)\). So \(\Phi_x\) is a uniform norm limit of the norm-continuous functions \(G^x_r\). \(\square\)

**Remark 4.3.** Definition 4.1 asks for neither boundedness nor norm continuity. By Theorem 4.2(3), strip functions are automatically bounded, and by Theorem 4.2(6), weak continuity is enough in case (N). One can also ask for a bounded, norm-continuous extension; for norm-continuous groups this gives the same class. Example 4.4 shows that (G3) is needed for (3). Example 9.3 shows that (6) fails in case (W\*): there the \(\tau\)-continuity at the boundary cannot be improved.

**Example 4.4** (Uniform boundedness is needed). Let \(X=\mathbb C\) and \(U_t=e^t\). This is case (N) without (G3). The orbit of \(1\) has the strip function \(z\mapsto e^z\) on every \(\mathbb S(a)\), and \(|e^{s+iu}|=e^s\) is unbounded. So Theorem 4.2(3) fails without (G3).

## 5. Analytic generators and entire elements

A reference for analytic generators is [Cioranescu–Zsidó].

**Definition 5.1.** For \(a\neq0\), let \(D(U_{ia})\) be the set of \(x\in X\) that have a strip function on \(\mathbb S(a)\), and put \(U_{ia}x=\Phi_x(ia)\). Put \(U_0=1\). An element is *entire* if it lies in \(D_\infty=\bigcap_{a\in\mathbb R}D(U_{ia})\).

For a unitary group \(U_t=A^{it}\), with \(A\) positive, self-adjoint and injective, \(U_{ia}=A^{-a}\) with its exact domain (Theorem 8.1(1) below). So \(U_{-i/2}=A^{1/2}\) and \(U_{-i}=A\).

**Theorem 5.2.**
1. \(U_{ia}\) is linear. For real \(s\), \(U_sD(U_{ia})=D(U_{ia})\) and \(U_{ia}U_sx=U_sU_{ia}x\).
2. \(U_{ia}\) is closed: its graph is norm closed in \(X\oplus X\).
3. \(U_{ia}\) is injective, and \(U_{ia}^{-1}=U_{-ia}\).
4. (*Composition.*) If \(b,c\) are real numbers of the same sign, then \(U_{ic}U_{ib}=U_{i(b+c)}\), domains included. For all real \(b,c\), \(U_{ic}U_{ib}\subseteq U_{i(b+c)}\). In particular \(D(U_{ia})\subseteq D(U_{ib})\) when \(b\) lies between \(0\) and \(a\), and then \(U_{ib}x=\Phi^a_x(ib)\).
5. (*Entire elements.*) \(D_\infty\) is a linear subspace. For \(x\in D_\infty\) put \(U_zx=U_{\operatorname{Re}z}U_{i\operatorname{Im}z}x\). Then \(z\mapsto U_zx\) is norm-entire and bounded on every horizontal strip of finite width, \(U_zx\in D_\infty\), and \(U_{z+w}x=U_zU_wx\) for all \(z,w\in\mathbb C\).
6. (*Density and cores.*) For every \(x\in X\) and \(r>0\), \(x_r\in D_\infty\) and \(U_zx_r=G^x_r(z)\). If \(x\in D(U_{ia})\), then \(U_{ia}x_r=(U_{ia}x)_r\). Hence \(D_\infty\) is \(\tau\)-dense in \(X\). In case (N) it is norm dense and a core for every \(U_{ia}\). In case (W\*), every \(x\in D(U_{ia})\) is the \(\tau\)-limit of the entire elements \(x_r\), with \(U_{ia}x_r\to U_{ia}x\) in \(\tau\), \(\|x_r\|\le M\|x\|\) and \(\|U_{ia}x_r\|\le M\|U_{ia}x\|\).
7. (*Bounds.*) If \(x\in D(U_{ia})\) and \(b\) lies between \(0\) and \(a\), then \(\|U_{ib}x\|\le M\|x\|^{1-b/a}\|U_{ia}x\|^{b/a}\).

**Proof.** (1) Linearity holds because strip functions add. By the proof of Theorem 4.2(2), \(z\mapsto U_s\Phi_x(z)\) is the strip function of \(U_sx\); evaluating at \(ia\) gives \(U_{ia}U_sx=U_sU_{ia}x\). Applying this with \(-s\) gives equality of the domains.

(2) Let \(x_n\in D(U_{ia})\), \(x_n\to x\) and \(U_{ia}x_n\to y\) in norm. By the maximum principle of Theorem 4.2(4), applied to the strip function \(\Phi_{x_n}-\Phi_{x_m}\) of \(x_n-x_m\),
\[
\sup_{\mathbb S(a)}\|\Phi_{x_n}-\Phi_{x_m}\|\le M\max\bigl(\|x_n-x_m\|,\ \|U_{ia}x_n-U_{ia}x_m\|\bigr)\to0 .
\]
So \(\Phi_{x_n}\) converges uniformly in norm to some \(\Phi\). For \(f\in F\), \(f\circ\Phi\) is a uniform limit of the continuous functions \(f\circ\Phi_{x_n}\), holomorphic inside; hence \(\Phi\) satisfies (S2) and (S3). Also \(\Phi(t)=\lim U_tx_n=U_tx\) and \(\Phi(ia)=y\). So \(x\in D(U_{ia})\) and \(U_{ia}x=y\).

(3) Let \(x\in D(U_{ia})\) and \(\Psi(w)=\Phi_x(w+ia)\) for \(w\in\mathbb S(-a)\); then \(w+ia\in\mathbb S(a)\). By covariance (Theorem 4.2(2)), \(\Psi(t)=U_t\Phi_x(ia)=U_tU_{ia}x\). So \(\Psi\) is the strip function of \(U_{ia}x\) on \(\mathbb S(-a)\), and \(U_{-ia}U_{ia}x=\Psi(-ia)=x\). Exchanging \(a\) and \(-a\) gives the rest.

(4) Reversing time exchanges signs: the family \(\tilde U_t=U_{-t}\) satisfies the Setting, and \(z\mapsto\Phi(-z)\) turns strip functions for \(U\) on \(\mathbb S(-a)\) into strip functions for \(\tilde U\) on \(\mathbb S(a)\). So \(\tilde U_{ia}=U_{-ia}\), and it suffices to treat \(b>0\).

*Same sign, \(b,c>0\).* Let \(x\in D(U_{ib})\) with \(y=U_{ib}x\in D(U_{ic})\). Define \(\Phi\) on \(\mathbb S(b+c)\) by \(\Phi=\Phi_x\) on \(\mathbb S(b)\) and \(\Phi(z)=\Phi_y(z-ib)\) for \(b\le\operatorname{Im}z\le b+c\). On the line \(\operatorname{Im}z=b\) both formulas give \(U_ty\), by covariance. So \(\Phi\) is \(\tau\)-continuous. For \(f\in F\), \(f\circ\Phi\) is continuous and holomorphic off that line; the Morera argument across a line (Section 1) makes it holomorphic on \(\mathbb S^\circ(b+c)\). Thus \(x\in D(U_{i(b+c)})\) and \(U_{i(b+c)}x=\Phi_y(ic)=U_{ic}U_{ib}x\). Conversely, let \(x\in D(U_{i(b+c)})\). By Theorem 4.2(1) the restriction of \(\Phi_x\) to \(\mathbb S(b)\) shows \(x\in D(U_{ib})\) with \(U_{ib}x=\Phi_x(ib)\). By covariance, the function \(w\mapsto\Phi_x(w+ib)\) on \(\mathbb S(c)\) is a strip function of \(U_{ib}x\). So \(U_{ib}x\in D(U_{ic})\), with \(U_{ic}U_{ib}x=\Phi_x(i(b+c))\).

*Opposite signs, \(b>0>c\).* Let \(x\in D(U_{ib})\) and \(y=U_{ib}x\in D(U_{ic})\). If \(b+c\ge0\), then \(x\in D(U_{i(b+c)})\) with \(U_{i(b+c)}x=\Phi_x(i(b+c))\) by the nesting just proved. The function \(w\mapsto\Phi_x(w+ib)\) is the strip function of \(y\) on \(\mathbb S(-b)\), which contains \(\mathbb S(c)\), so \(U_{ic}y=\Phi_x(i(b+c))\). If \(b+c<0\), then \(c=(b+c)+(-b)\) with both parts negative, so the same-sign case gives \(U_{ic}=U_{i(b+c)}U_{-ib}\). Since \(U_{-ib}y=x\) by (3), \(U_{ic}y=U_{i(b+c)}x\), with \(x\in D(U_{i(b+c)})\).

(5) Let \(x\in D_\infty\) and \(c>0\). The strip functions \(\Phi^c_x\) and \(\Phi^{-c}_x\) agree on the real line. Together they give a \(\tau\)-continuous function on \(\{|\operatorname{Im}z|\le c\}\) whose scalar tests are holomorphic in the open strip, by the Morera argument across a line. By covariance and (4), its value at \(s+ib\) is \(U_sU_{ib}x=U_{s+ib}x\). It is bounded by Theorem 4.2(3), so it is norm-holomorphic on \(|\operatorname{Im}z|<c\) by Lemma 2.1(2). As \(c\) is arbitrary, \(z\mapsto U_zx\) is norm-entire. Now let \(c\) be any real number. The function \(w\mapsto U_{w+ic}x\) restricted to any \(\mathbb S(b)\) is a strip function of \(U_{ic}x\); so \(U_{ic}x\in D_\infty\) with \(U_{ib}U_{ic}x=U_{i(b+c)}x\). With (1) this gives \(U_zx\in D_\infty\) and
\[
U_{s+ib}U_{t+ic}x=U_{s+t}U_{ib}U_{ic}x=U_{(s+t)+i(b+c)}x .
\]

(6) By Proposition 3.1(3), the restriction of \(G^x_r\) to each \(\mathbb S(a)\) is a strip function of \(x_r\): it is norm-entire, hence \(\tau\)-continuous, and \(G^x_r(t)=U_tx_r\). So \(x_r\in D_\infty\) and \(U_zx_r=G^x_r(z)\). If \(x\in D(U_{ia})\), Theorem 4.2(5) gives \(U_{ia}x_r=G^x_r(ia)=(\Phi_x(ia))_r=(U_{ia}x)_r\). The remaining statements follow from Proposition 3.1(4), applied to \(x\) and to \(U_{ia}x\).

(7) By (4), \(U_{ib}x=\Phi^a_x(ib)\). Apply (4.1) with \(t=0\). \(\square\)

**Remark 5.3.** In case (W\*), \(D_\infty\) need not be norm dense. An entire element has a norm-continuous orbit, by (5). The elements with norm-continuous orbits form a norm-closed subspace, because \(\|U_t\|\le M\) for all \(t\); Example 9.3 shows that this subspace can be proper. Theorem 5.2(2) shows that \(U_{ia}\) is norm closed, and (6) supplies \(\tau\)-convergent smoothings. Whether the graph of \(U_{ia}\) is \(\tau\)-closed in case (W\*) is not decided in this lesson.

## 6. Continuation through annihilators, intertwiners and closed graphs

Identities that hold on the real line persist on the strip whenever they are expressed by closed conditions. This section makes that precise. Let \((X,F,U)\) and \((Y,G,V)\) be two systems as in the Setting of Section 3. Part (4) below uses conjugate-linear operators, which Section 7 studies in detail: a map \(T\) is *conjugate-linear* if \(T(\lambda\xi+\eta)=\bar\lambda T\xi+T\eta\), and it is *closed* if its graph is closed.

**Proposition 6.1.**
1. (*Annihilators.*) Let \(\Phi\) be the strip function of \(x\) on \(\mathbb S(a)\), and \(f\in F\) with \(f(U_tx)=0\) for all real \(t\). Then \(f(\Phi(z))=0\) for all \(z\in\mathbb S(a)\).
2. (*Bounded intertwiners.*) Let \(B:X\to Y\) be bounded and linear, with \(g\circ B\in F\) for \(g\in G\) and \(BU_t=V_tB\). Then \(BD(U_{ia})\subseteq D(V_{ia})\) and \(V_{ia}Bx=BU_{ia}x\). If instead \(B\) is conjugate-linear, with \(\overline{g\circ B}\in F\) for \(g\in G\) and \(BU_t=V_tB\), then \(BD(U_{ia})\subseteq D(V_{-ia})\) and \(V_{-ia}Bx=BU_{ia}x\).
3. (*Closed linear operators, case (N).*) Let both systems be in case (N), and let \(T:D(T)\subseteq X\to Y\) be a closed linear operator with \(U_tD(T)\subseteq D(T)\) and \(TU_tx=V_tTx\) for \(x\in D(T)\).
   - (a) If \(x\in D(T)\), then \(x_r\in D(T)\) and \(Tx_r=(Tx)_r\). So the elements \(x_r\), with \(x\in D(T)\) and \(r>0\), lie in \(D(T)\cap D_\infty(U)\), form a core for \(T\), and are mapped by \(T\) into \(D_\infty(V)\). (Other elements of \(D(T)\cap D_\infty(U)\) need not be: see Remark 6.3.)
   - (b) If \(x\in D(T)\cap D(U_{ia})\) and \(Tx\in D(V_{ia})\), then \(U_{ia}x\in D(T)\) and \(TU_{ia}x=V_{ia}Tx\).
4. (*Closed conjugate-linear operators on Hilbert spaces.*) Let \(H,K\) be Hilbert spaces with groups \(U,V\) in case (N), and let \(T:D(T)\subseteq H\to K\) be a closed conjugate-linear operator with \(U_tD(T)\subseteq D(T)\) and \(TU_t\xi=V_tT\xi\) for \(\xi\in D(T)\).
   - (a) If \(\xi\in D(T)\), then \(\xi_r\in D(T)\) and \(T\xi_r=(T\xi)_r\). So \(D(T)\cap D_\infty(U)\) is a core for \(T\).
   - (b) If \(\xi\in D(T)\cap D(U_{ia})\) and \(T\xi\in D(V_{-ia})\), then \(U_{ia}\xi\in D(T)\) and \(TU_{ia}\xi=V_{-ia}T\xi\). If \(\xi\in D(T)\) is entire and \(T\xi\) is entire, then \(U_z\xi\in D(T)\) and \(TU_z\xi=V_{\bar z}T\xi\) for all \(z\in\mathbb C\).
5. (*Membership in a von Neumann algebra.*) Let \(N\subseteq B(H)\) be a von Neumann algebra and \(\Phi:\mathbb S(a)\to B(H)\) a function such that every \(z\mapsto\langle\Phi(z)\xi,\eta\rangle\) is continuous on \(\mathbb S(a)\) and holomorphic inside. If \(\Phi(t)\in N\) for all real \(t\), then \(\Phi(z)\in N\) for all \(z\in\mathbb S(a)\).

**Proof.** (1) The function \(f\circ\Phi\) is continuous, holomorphic inside and zero on the real line. Apply boundary uniqueness.

(2) In the linear case, \(z\mapsto B\Phi_x(z)\) satisfies (S1)–(S3) for \(Bx\) and \(V\): at real \(t\) it takes the value \(BU_tx=V_tBx\), and for \(g\in G\), \(g\circ B\circ\Phi_x=(g\circ B)\circ\Phi_x\) with \(g\circ B\in F\). Evaluate at \(ia\). In the conjugate-linear case put \(\Psi(w)=B\Phi_x(\bar w)\) for \(w\in\mathbb S(-a)\); then \(\bar w\in\mathbb S(a)\). For \(g\in G\), \(g(\Psi(w))\) is the complex conjugate of \((\overline{g\circ B})(\Phi_x(\bar w))\), which is continuous and antiholomorphic in \(w\). So \(g\circ\Psi\) is continuous and holomorphic inside, and \(\Psi(t)=BU_tx=V_tBx\). Hence \(\Psi\) is the strip function of \(Bx\) on \(\mathbb S(-a)\), and \(V_{-ia}Bx=\Psi(-ia)=B\Phi_x(ia)\).

(3a) The graph \(\Gamma(T)\) is closed in \(X\oplus Y\) and invariant under each \(U_t\oplus V_t\). The pair \((x_r,(Tx)_r)\) is the norm integral of the continuous integrable function \(t\mapsto g_r(t)(U_tx,V_tTx)\), whose values lie in \(\Gamma(T)\). It is a norm limit of Riemann sums over compact intervals, and these lie in the subspace \(\Gamma(T)\). As \(\Gamma(T)\) is closed, \(Tx_r=(Tx)_r\). By Proposition 3.1(4) and Theorem 5.2(6), \(x_r\to x\), \(Tx_r\to Tx\), \(x_r\in D_\infty(U)\) and \((Tx)_r\in D_\infty(V)\).

(3b) The direct sum \(Z=X\oplus Y\), with the group \(U\oplus V\), is again in case (N), and \(z\mapsto(\Phi_x(z),\Phi_{Tx}(z))\) is the strip function of \((x,Tx)\). Its real values lie in \(\Gamma(T)\). By the Hahn–Banach theorem, \(\Gamma(T)\) is the common zero set of the functionals in \(Z^*\) that vanish on it. By (1) each of them vanishes on the whole strip function. So \((U_{ia}x,V_{ia}Tx)\in\Gamma(T)\).

(4) Regard \(E=H\oplus K\) as a real Hilbert space with inner product \(\operatorname{Re}(\langle u,u'\rangle+\langle v,v'\rangle)\) and orthogonal complement \(\perp\). The graph \(\Gamma(T)\) is a closed real subspace, so \(\Gamma(T)=\Gamma(T)^{\perp\perp}\) by the projection theorem.

(a) A Riemann sum \(\sum_jc_jU_{t_j}\xi\) with real coefficients satisfies \(T\sum_jc_jU_{t_j}\xi=\sum_jc_jV_{t_j}T\xi\), because \(T\) is conjugate-linear and the \(c_j\) are real. The Gaussian is real, so the argument of (3a) applies.

(b) Let \((\eta,\zeta)\in\Gamma(T)^\perp\). For \(u\in D(T)\), both \((u,Tu)\) and \((iu,T(iu))=(iu,-iTu)\) lie in \(\Gamma(T)\). The first gives \(\operatorname{Re}\langle u,\eta\rangle+\operatorname{Re}\langle Tu,\zeta\rangle=0\); the second gives \(-\operatorname{Im}\langle u,\eta\rangle+\operatorname{Im}\langle Tu,\zeta\rangle=0\). Together:
\[
\langle u,\eta\rangle+\langle\zeta,Tu\rangle=0\qquad(u\in D(T)).
\tag{6.1}
\]
Put \(\Psi(z)=\Phi_{T\xi}(\bar z)\) for \(z\in\mathbb S(a)\), where \(\Phi_{T\xi}\) is the strip function of \(T\xi\) on \(\mathbb S(-a)\), and
\[
h(z)=\langle\Phi_\xi(z),\eta\rangle+\langle\zeta,\Psi(z)\rangle .
\]
The second term is the complex conjugate of the antiholomorphic function \(\langle\Psi(z),\zeta\rangle\), so \(h\) is continuous on \(\mathbb S(a)\) and holomorphic inside. For real \(t\), \(h(t)=\langle U_t\xi,\eta\rangle+\langle\zeta,TU_t\xi\rangle=0\) by (6.1). So \(h=0\), by boundary uniqueness. Since \(\operatorname{Re}h(z)\) is the real inner product of \((\Phi_\xi(z),\Psi(z))\) with \((\eta,\zeta)\), the pair \((\Phi_\xi(z),\Psi(z))\) lies in \(\Gamma(T)^{\perp\perp}=\Gamma(T)\). At \(z=ia\) this says \(TU_{ia}\xi=\Psi(ia)=V_{-ia}T\xi\). For entire \(\xi\) and \(z=s+ib\), use this with \(a=b\). Then \(U_z\xi=U_sU_{ib}\xi\) lies in \(D(T)\), because \(U_sD(T)\subseteq D(T)\), and \(TU_sU_{ib}\xi=V_sTU_{ib}\xi\). With the definition of \(U_z\) and \(V_z\) in Theorem 5.2(5), \(TU_z\xi=V_sV_{-ib}T\xi=V_{\bar z}T\xi\).

(5) Let \(m'\in N'\) and \(\xi,\eta\in H\). The function \(z\mapsto\langle\Phi(z)m'\xi,\eta\rangle-\langle\Phi(z)\xi,m'^*\eta\rangle\) is continuous, holomorphic inside and zero on the real line, since \(\Phi(t)\) commutes with \(m'\). By boundary uniqueness it vanishes, so \(\Phi(z)\) commutes with \(N'\) and \(\Phi(z)\in N''=N\) by the bicommutant theorem. \(\square\)

**Remark 6.2.** Part (4), with \(T\) linear and \(V_{ia}\) in place of \(V_{-ia}\), gives (3) for Hilbert spaces by the same computation. Part (4) also gives the identity \(SU_z\xi=U_{\bar z}S\xi\) of Corollary 7.7, one of the analytic properties of a Tomita algebra.

**Remark 6.3** (on part (3a)). An entire element of \(D(T)\) need not have an entire image. On \(L^2(\mathbb R)\) let \(U_t=V_t\) be multiplication by \(e^{itu}\), and \(T\) multiplication by \(e^{u^2}\) on its maximal domain. By Theorem 8.1(1) below, with \(A\) multiplication by \(e^u\), a vector \(f\) is entire exactly when \(e^{cu}f\in L^2\) for every real \(c\). The vector \(\xi(u)=e^{-u^2}/(1+u^2)\) is entire and lies in \(D(T)\), but \(T\xi=1/(1+u^2)\) is not entire.

## 7. Conjugate-linear adjoints, polar decomposition and closed involutions

A modern, openly available treatment of closed involutions, in the language of standard subspaces, is [Neeb–Ólafsson].

**Definitions 7.1.** Let \(H,K\) be Hilbert spaces. A map \(T:D(T)\to K\), defined on a subspace \(D(T)\subseteq H\), is *conjugate-linear* if \(T(\lambda\xi+\eta)=\bar\lambda T\xi+T\eta\). Its graph \(\Gamma(T)=\{(\xi,T\xi)\}\) is a real subspace of \(H\oplus K\), not a complex one. Closedness, closability and the closure \(\overline T\) are defined through the graph, as for linear operators. A bounded conjugate-linear bijection \(J\) of \(H\) with \(\langle J\xi,J\eta\rangle=\langle\eta,\xi\rangle\) is *antiunitary*. Throughout, \(E=H\oplus K\) (or \(K\oplus H\)) is regarded as a real Hilbert space with inner product \(\operatorname{Re}(\langle u,u'\rangle+\langle v,v'\rangle)\), and \(\perp\) means the orthogonal complement in it.

*The adjoint.* Let \(T\) be densely defined. If \(T\) is linear, \(T^*\) is the usual adjoint: \(\langle T\xi,\eta\rangle=\langle\xi,T^*\eta\rangle\). If \(T\) is conjugate-linear, \(D(T^*)\) is the set of \(\eta\in K\) for which the linear functional \(\xi\mapsto\langle\eta,T\xi\rangle\) is bounded on \(D(T)\), and \(T^*\eta\in H\) is the vector given by the Riesz theorem:
\[
\langle\xi,T^*\eta\rangle=\langle\eta,T\xi\rangle,\qquad\text{equivalently}\qquad\langle T\xi,\eta\rangle=\langle T^*\eta,\xi\rangle
\tag{7.1}
\]
for \(\xi\in D(T)\), \(\eta\in D(T^*)\). Then \(T^*\) is conjugate-linear. For an antiunitary \(J\), \(J^*=J^{-1}\).

**Lemma 7.2** (Adjoints). Let \(T\) be densely defined, linear or conjugate-linear.
1. \(T^*\) is closed. With \(R:H\oplus K\to K\oplus H\), \(R(u,v)=(v,-u)\), we have \(\Gamma(T^*)=R(\Gamma(T)^\perp)\).
2. \(T\) is closable if and only if \(T^*\) is densely defined. Then \(T^{**}=\overline T\) and \((\overline T)^*=T^*\).
3. \(\ker T^*=(\operatorname{ran}T)^\perp\).
4. If \(J:K\to L\) is a bounded conjugate-linear map and \(T\) is linear, then \((JT)^*=T^*J^*\), domains included.

**Proof.** (1) In both cases, \((\eta,\zeta)\in\Gamma(T^*)\) means that a complex identity holds for every \(\xi\in D(T)\): \(\langle T\xi,\eta\rangle=\langle\xi,\zeta\rangle\) (linear case) or \(\langle T\xi,\eta\rangle=\langle\zeta,\xi\rangle\) (conjugate-linear case). Replacing \(\xi\) by \(i\xi\) multiplies both sides by \(i\) in the first case and by \(-i\) in the second. So the identity holds for all \(\xi\) as soon as its real part does. The real part reads \(\operatorname{Re}\langle T\xi,\eta\rangle-\operatorname{Re}\langle\xi,\zeta\rangle=0\) in both cases, that is, \((\xi,T\xi)\perp(-\zeta,\eta)\). Hence \((\eta,\zeta)\in\Gamma(T^*)\) if and only if \((-\zeta,\eta)\in\Gamma(T)^\perp\), and \(R(-\zeta,\eta)=(\eta,\zeta)\). Orthogonal complements are closed and \(R\) is an isometry.

(2) Since \(R\) is a real isometry, \(\Gamma(T^*)^\perp=R(\Gamma(T)^{\perp\perp})=R(\overline{\Gamma(T)})\). If \(T^*\) is densely defined, (1) applied to \(T^*\), with the analogous map \(R'(u,v)=(v,-u)\), gives \(\Gamma(T^{**})=R'R(\overline{\Gamma(T)})=-\overline{\Gamma(T)}=\overline{\Gamma(T)}\). So \(\overline{\Gamma(T)}\) is a graph, \(T\) is closable and \(T^{**}=\overline T\). Conversely, let \(T\) be closable and \(\eta\perp D(T^*)\). Then \((\eta,0)\perp(\kappa,T^*\kappa)\) for all \(\kappa\in D(T^*)\), so \((\eta,0)\in\Gamma(T^*)^\perp=R(\overline{\Gamma(T)})\), that is, \((0,\eta)\in\overline{\Gamma(T)}\). As \(\overline{\Gamma(T)}\) is a graph, \(\eta=0\). Finally \(\Gamma(T)\) and its closure have the same orthogonal complement, so \((\overline T)^*=T^*\).

(3) \(T^*\eta=0\) exactly when \(\langle T\xi,\eta\rangle=0\) for all \(\xi\in D(T)\).

(4) By (7.1) for \(J\), \(\langle\eta,JT\xi\rangle=\langle T\xi,J^*\eta\rangle\). This is a bounded function of \(\xi\) exactly when \(J^*\eta\in D(T^*)\), and then it equals \(\langle\xi,T^*J^*\eta\rangle\). \(\square\)

**Lemma 7.3** (The operator \(T^*T\)). Let \(T:D(T)\subseteq H\to K\) be closed, densely defined and conjugate-linear. Then \(T^*T\) is a linear, positive, self-adjoint operator, \(D(T^*T)\) is a core for \(T\), \(D((T^*T)^{1/2})=D(T)\), and \(\|(T^*T)^{1/2}\xi\|=\|T\xi\|\).

**Proof.** \(T^*T\) is linear as the composite of two conjugate-linear maps. By Lemma 7.2(1), \(\Gamma(T)^\perp=\{(T^*\kappa,-\kappa):\kappa\in D(T^*)\}\). Given \(h\in H\), the projection theorem in \(E\), applied to the closed subspace \(\Gamma(T)\), decomposes \((h,0)=(\xi,T\xi)+(T^*\kappa,-\kappa)\) with \(\xi\in D(T)\). Then \(\kappa=T\xi\) and \(h=\xi+T^*T\xi\). So \(1+T^*T\) maps \(D(T^*T)\) onto \(H\). By (7.1), \(\langle T^*T\xi,\zeta\rangle=\langle T\zeta,T\xi\rangle\) for \(\xi\in D(T^*T)\), \(\zeta\in D(T)\); in particular \(\langle T^*T\xi,\xi\rangle=\|T\xi\|^2\) and \(\|(1+T^*T)\xi\|\ge\|\xi\|\). So \(B=(1+T^*T)^{-1}\) is an everywhere-defined contraction. It is symmetric: if \(h=(1+T^*T)\xi\) and \(h'=(1+T^*T)\xi'\), then \(\langle Bh,h'\rangle=\langle\xi,\xi'\rangle+\langle\xi,T^*T\xi'\rangle=\langle\xi,\xi'\rangle+\langle T\xi',T\xi\rangle\), and \(\langle h,Bh'\rangle=\langle\xi,\xi'\rangle+\langle T^*T\xi,\xi'\rangle=\langle\xi,\xi'\rangle+\langle T\xi',T\xi\rangle\) as well. It is positive, since \(\langle Bh,h\rangle=\|\xi\|^2+\|T\xi\|^2\), and injective. The inverse of an injective bounded self-adjoint operator is self-adjoint (its graph is the flip of a self-adjoint graph), so \(T^*T=B^{-1}-1\) is self-adjoint and positive.

For the core property use the graph inner product \(\langle\xi,\zeta\rangle_T=\langle\xi,\zeta\rangle+\langle T\zeta,T\xi\rangle\). It is sesquilinear because the two conjugations cancel, and \(D(T)\) is complete for it because \(T\) is closed. If \(\xi\in D(T)\) is \(\langle\cdot,\cdot\rangle_T\)-orthogonal to \(D(T^*T)\), then for all \(\zeta\in D(T^*T)\), \(0=\langle\xi,\zeta\rangle+\langle T\zeta,T\xi\rangle=\langle\xi,(1+T^*T)\zeta\rangle\). So \(\xi\) is orthogonal to \(H\), and \(\xi=0\). Finally, \(A=T^*T\) and \(A^{1/2}\) satisfy \(\|A^{1/2}\zeta\|^2=\langle A\zeta,\zeta\rangle=\|T\zeta\|^2\) on \(D(A)\), which is a core for \(A^{1/2}\) (spectral calculus) and for \(T\). Both operators are closed, so their domains are the completions of \(D(A)\) in the same graph norm. \(\square\)

**Lemma 7.4** (Polar decomposition). Let \(T\) be as in Lemma 7.3 and \(|T|=(T^*T)^{1/2}\). There is a unique conjugate-linear partial isometry \(W\) with initial space \(\overline{\operatorname{ran}|T|}\) and \(T=W|T|\). Its final space is \(\overline{\operatorname{ran}T}\). Conversely, if \(T=W'B\) with \(B\) positive self-adjoint and \(W'\) a bounded conjugate-linear map with \(W'^*W'\) the projection onto \(\overline{\operatorname{ran}B}\), then \(B=|T|\) and \(W'=W\).

**Proof.** By Lemma 7.3, \(|T|\xi\mapsto T\xi\) is a well-defined conjugate-linear isometry from \(\operatorname{ran}|T|\) onto \(\operatorname{ran}T\). Extend it by continuity to \(\overline{\operatorname{ran}|T|}\) and by \(0\) on the complement. For the converse, Lemma 7.2(4) gives \(T^*=(W'B)^*=BW'^*\), so \(T^*T=BW'^*W'B=B^2\), since \(W'^*W'\) fixes \(\operatorname{ran}B\). Uniqueness of positive square roots (spectral calculus) gives \(B=|T|\), and then \(W'\) and \(W\) agree on \(\operatorname{ran}|T|\) and vanish on its complement. \(\square\)

**Lemma 7.5** (Antiunitary transport). Let \(J\) be antiunitary on \(H\) and \(A\) self-adjoint with spectral measure \(P\). Then \(P'(\beta)=JP(\beta)J^{-1}\) is the spectral measure of the self-adjoint operator \(JAJ^{-1}\), and for every Borel function \(f\),
\[
Jf(A)J^{-1}=\bar f(JAJ^{-1}),\qquad D\bigl(\bar f(JAJ^{-1})\bigr)=J\,D(f(A)).
\tag{7.2}
\]

**Proof.** Each \(P'(\beta)\) is an orthogonal projection, \(P'\) is countably additive in the strong topology, and \(P'(\mathbb R)=1\). For \(\xi\in H\), \(\langle P'(\beta)J\xi,J\xi\rangle=\langle JP(\beta)\xi,J\xi\rangle=\langle\xi,P(\beta)\xi\rangle\), so the scalar measure of \(J\xi\) for \(P'\) is that of \(\xi\) for \(P\). For a simple function \(f=\sum_kc_k1_{\beta_k}\), \(Jf(A)J^{-1}=\sum_k\bar c_kP'(\beta_k)\), because \(J\) is conjugate-linear. Uniform limits extend this to bounded Borel \(f\). For general \(f\), the domain of \(\int\bar f\,dP'\) consists of the vectors \(J\xi\) with \(\int|f|^2d\mu_\xi<\infty\), which is \(JD(f(A))\), and the truncations \(f1_{\{|f|\le n\}}\) converge on it. With \(f(\lambda)=\lambda\) this shows \(JAJ^{-1}=\int\lambda\,dP'(\lambda)\), so \(P'\) is its spectral measure. \(\square\)

**Theorem 7.6** (Closed involutions). Let \(S\) be a closed, densely defined, conjugate-linear operator on \(H\) with \(S(D(S))\subseteq D(S)\) and \(S^2\xi=\xi\) for \(\xi\in D(S)\). Put \(F=S^*\) and \(\Delta=FS\).
1. \(S\) maps \(D(S)\) bijectively onto itself, and \(S^{-1}=S\).
2. \(F\) is again a closed, densely defined involution: \(F(D(F))=D(F)\) and \(F^2=1\) there.
3. \(\Delta\) is positive, self-adjoint and injective; \(D(\Delta^{1/2})=D(S)\) and \(\|\Delta^{1/2}\xi\|=\|S\xi\|\).
4. There is a unique antiunitary \(J\) with \(S=J\Delta^{1/2}\). It satisfies \(J=J^{-1}=J^*\).
5. \(J\Delta J=\Delta^{-1}\). More generally \(Jf(\Delta)J=\bar f(\Delta^{-1})\) for every Borel \(f\) on \((0,\infty)\). In particular \(J\Delta^{it}=\Delta^{it}J\) and \(J\Delta^\alpha J=\Delta^{-\alpha}\) for real \(t,\alpha\), with \(JD(\Delta^\alpha)=D(\Delta^{-\alpha})\).
6. \(S=\Delta^{-1/2}J\), \(F=J\Delta^{-1/2}=\Delta^{1/2}J\), and \(D(F)=D(\Delta^{-1/2})\).
7. If \(S=J'B\) with \(J'\) antiunitary and \(B\) positive self-adjoint, then \(J'=J\) and \(B=\Delta^{1/2}\).

If \(S_0\) is densely defined, closable, conjugate-linear, and satisfies \(S_0(D(S_0))\subseteq D(S_0)\) and \(S_0^2=1\) there, then its closure satisfies the hypotheses: the flip \((u,v)\mapsto(v,u)\) maps \(\Gamma(S_0)\) onto itself, hence also its closure. The domain \(D(S)\) is complete for \(\langle\xi,\eta\rangle_S=\langle\xi,\eta\rangle+\langle S\eta,S\xi\rangle\), and \(D(S_0)\) is dense in it.

**Proof.** (1) is immediate from \(S^2=1\) on \(D(S)\).

(2) \(F\) is closed by Lemma 7.2(1), and densely defined by Lemma 7.2(2), since \(S\) is closed. Let \(\phi(u,v)=(v,u)\) denote the flip on \(H\oplus H\); it is a real isometry, and \(\phi(\Gamma(S))=\Gamma(S)\) by (1). A direct check gives \(\phi\circ R=-R\circ\phi\). By Lemma 7.2(1),
\[
\phi(\Gamma(F))=\phi R(\Gamma(S)^\perp)=R\phi(\Gamma(S)^\perp)=R\bigl(\phi(\Gamma(S))^\perp\bigr)=R(\Gamma(S)^\perp)=\Gamma(F),
\]
using that \(-R\phi(\cdot)\) and \(R\phi(\cdot)\) have the same image on a real subspace. So the flip of the graph of \(F\) is the graph of \(F\): \(F\) is injective, \(F(D(F))=D(F)\), and \(F^{-1}=F\).

(3) Lemma 7.3 gives everything except injectivity. If \(\Delta\xi=0\), then \(\|S\xi\|=\|\Delta^{1/2}\xi\|=0\), so \(\xi=S(S\xi)=0\).

(4) By Lemma 7.4, \(S=J\Delta^{1/2}\) with \(J\) a conjugate-linear partial isometry from \(\overline{\operatorname{ran}\Delta^{1/2}}=(\ker\Delta^{1/2})^\perp=H\) onto \(\overline{\operatorname{ran}S}=\overline{D(S)}=H\). A conjugate-linear isometry satisfies \(\langle J\xi,J\eta\rangle=\langle\eta,\xi\rangle\) by polarization, so \(J\) is antiunitary. Uniqueness is (7).

(5), (6) Since \(S=S^{-1}\) and \(\Delta^{1/2}\) is injective with inverse \(\Delta^{-1/2}\),
\[
S=S^{-1}=\Delta^{-1/2}J^{-1}=J^{-1}\bigl(J\Delta^{-1/2}J^{-1}\bigr).
\]
By Lemma 7.5, \(B=J\Delta^{-1/2}J^{-1}\) is positive, self-adjoint and injective, and \(J^{-1}\) is antiunitary; so \(J^{-1*}J^{-1}=1\) is the projection onto \(\overline{\operatorname{ran}B}=H\). The uniqueness in Lemma 7.4 gives \(J^{-1}=J\) and \(J\Delta^{-1/2}J=\Delta^{1/2}\). By Lemma 7.5 with the real function \(\lambda^{-1/2}\), \(J\Delta^{-1/2}J=(J\Delta J)^{-1/2}\), so \((J\Delta J)^{-1/2}=\Delta^{1/2}\); applying \(s\mapsto s^{-2}\) to both sides gives \(J\Delta J=\Delta^{-1}\). Lemma 7.5 then gives \(Jf(\Delta)J=\bar f(J\Delta J)=\bar f(\Delta^{-1})\). With \(f(\lambda)=\lambda^{it}\), \(\bar f(\lambda^{-1})=\lambda^{it}\); with \(f(\lambda)=\lambda^\alpha\), \(\bar f(\lambda^{-1})=\lambda^{-\alpha}\). An antiunitary involution satisfies \(\langle J\xi,\eta\rangle=\langle J\xi,J(J\eta)\rangle=\langle J\eta,\xi\rangle\), so \(J^*=J\). Now \(S=J\Delta^{1/2}=(J\Delta^{1/2}J)J=\Delta^{-1/2}J\), and by Lemma 7.2(4), \(F=(J\Delta^{1/2})^*=\Delta^{1/2}J^*=\Delta^{1/2}J=J(J\Delta^{1/2}J)=J\Delta^{-1/2}\). Hence \(D(F)=D(\Delta^{-1/2})\).

(7) If \(S=J'B\), then \(\ker B\subseteq\ker S=\{0\}\), so \(J'^*J'=1\) is the projection onto \(\overline{\operatorname{ran}B}\). Lemma 7.4 gives \(B=|S|=\Delta^{1/2}\) and \(J'=J\).

The completeness of \(\langle\cdot,\cdot\rangle_S\) is the closedness of \(S\), and \(D(S_0)\) is dense in it because \(\Gamma(S)\) is the closure of \(\Gamma(S_0)\). \(\square\)

**Corollary 7.7** (Analytic vectors of a closed involution). In Theorem 7.6, let \(U_t=\Delta^{it}\), a strongly continuous unitary group. Then \(SU_t=U_tS\) and \(FU_t=U_tF\) with \(U_tD(S)=D(S)\). The set \(\mathcal E\) of entire vectors \(\xi\) of \(U\) is \(S\)-invariant and \(F\)-invariant, it is a core for \(S\), \(F\), \(\Delta^{1/2}\) and \(\Delta^{-1/2}\), and for \(\xi,\eta\in\mathcal E\) and \(z\in\mathbb C\):
\[
SU_z\xi=U_{\bar z}S\xi,\qquad\langle U_z\xi,\eta\rangle=\langle\xi,U_{-\bar z}\eta\rangle,\qquad\langle S\xi,S\eta\rangle=\langle U_{-i}\eta,\xi\rangle .
\tag{7.3}
\]
Here \(U_{-i}=\Delta\) and \(U_{-i/2}=\Delta^{1/2}\), by Theorem 8.1(1) below. Together with the fact that the vectors of \(\mathcal E\) are entire, the identities (7.3) are the analytic part of the axioms of a Tomita algebra for the group \(\Delta^{i\alpha}\). The multiplicativity of \(\Delta^{i\alpha}\) concerns a Hilbert algebra and is not treated here.

**Proof.** \(SU_t=J\Delta^{1/2}\Delta^{it}=\Delta^{it}J\Delta^{1/2}=U_tS\) by Theorem 7.6(5), with \(U_tD(\Delta^{1/2})=D(\Delta^{1/2})\); similarly for \(F\). By Proposition 6.1(4a) with \(V=U\), Gaussian averages of vectors in \(D(S)\) stay in \(D(S)\) and are entire, and \(S\xi_r=(S\xi)_r\); so \(\mathcal E\cap D(S)\) is a core for \(S\). Every entire \(\xi\) lies in \(D(U_{-i/2})=D(\Delta^{1/2})=D(S)\), and \(S\xi=J\Delta^{1/2}\xi\) is entire: \(\Delta^{1/2}\xi=U_{-i/2}\xi\) is entire by Theorem 5.2(5), and \(J\) maps entire vectors to entire vectors by Proposition 6.1(2) (conjugate-linear case), because \(J\) commutes with every \(U_t\). So \(\mathcal E\subseteq D(S)\), \(S\mathcal E\subseteq\mathcal E\), and \(\mathcal E\) is a core for \(S\). The same argument applies to \(F\), and cores for \(S\) and \(F\) are cores for \(\Delta^{1/2}\) and \(\Delta^{-1/2}\) because the graph norms agree (\(\|S\xi\|=\|\Delta^{1/2}\xi\|\), \(\|F\xi\|=\|\Delta^{-1/2}\xi\|\)). The first identity in (7.3) is Proposition 6.1(4b) with \(V=U\). The second holds for real \(z\) because \(U_t^*=U_{-t}\); both sides are entire in \(z\) (the right side is the conjugate of an antiholomorphic function), so they agree everywhere by the identity theorem. For the third, \(\langle S\xi,S\eta\rangle=\langle J\Delta^{1/2}\xi,J\Delta^{1/2}\eta\rangle=\langle\Delta^{1/2}\eta,\Delta^{1/2}\xi\rangle=\langle\Delta\eta,\xi\rangle\). \(\square\)

**Example 7.8** (An explicit closed involution). On \(H=L^2(\mathbb R)\) let \((Sf)(s)=e^s\,\overline{f(-s)}\), with \(D(S)=\{f:e^{-u}f(u)\in L^2\}\). Then \(S^2=1\) on \(D(S)\) and \(S\) is closed and densely defined. From (7.1), \((S^*k)(u)=e^{-u}\overline{k(-u)}\). So \(\Delta=S^*S\) is multiplication by \(e^{-2u}\), \(\Delta^{1/2}\) is multiplication by \(e^{-u}\), and \(J=S\Delta^{-1/2}\) is \((Jk)(s)=\overline{k(-s)}\). One checks \(J\Delta J=\Delta^{-1}\) directly: \((J\Delta Jk)(s)=e^{2s}k(s)\). Both \(\Delta\) and \(\Delta^{-1}\) are unbounded. The modular group \(\Delta^{it}\) is multiplication by \(e^{-2itu}\), and \(U_{ia}=\Delta^{-a}\) is multiplication by \(e^{2au}\) (Theorem 8.1(1)). The entire vectors are the \(f\) with \(e^{c|u|}f\in L^2\) for every \(c\), for instance Gaussians, and they form a core for \(S\), as Corollary 7.7 predicts.

## 8. Unitary groups: spectral form, Stone's theorem, cores and analytic vectors

Here \(H\) is a Hilbert space and \(U\) a strongly continuous unitary group on it; this is case (N) with \(M=1\).

**Theorem 8.1.**
1. (*Spectral groups.*) Let \(A\) be positive, self-adjoint and injective, and \(U_t=A^{it}\). For real \(a\), \(D(U_{ia})=D(A^{-a})\) and \(U_{ia}=A^{-a}\); the strip function of \(\xi\in D(A^{-a})\) is \(z\mapsto A^{iz}\xi\).
2. (*Self-adjointness.*) For every strongly continuous unitary group \(U\) and real \(a\), the operator \(U_{ia}\) is positive, self-adjoint and injective. For entire \(\xi,\eta\), \(\langle U_z\xi,\eta\rangle=\langle\xi,U_{-\bar z}\eta\rangle\).
3. (*Stone's theorem.*) Put \(A=U_{-i}\). Then \(A\) is positive, self-adjoint and injective, \(U_t=A^{it}\) for all real \(t\), and no other positive self-adjoint injective operator has this property. With \(H_0=\log A\), \(U_t=e^{itH_0}\), and \(D(H_0)\) is the set of \(\xi\) for which \(t^{-1}(U_t\xi-\xi)\) converges as \(t\to0\); the limit is \(iH_0\xi\).
4. (*Cores.*) Let \(H_0\) be as in (3) and \(\mathcal D\subseteq D(H_0)\) a dense subspace with \(U_t\mathcal D\subseteq\mathcal D\) for all \(t\). Then \(\mathcal D\) is a core for \(H_0\).
5. (*Analytic vectors.*) Let \(T\) be closed, densely defined and symmetric. Call \(\xi\) an *analytic vector* of \(T\) if \(\xi\in\bigcap_nD(T^n)\) and \(\sum_ns^n\|T^n\xi\|/n!<\infty\) for some \(s>0\); let \(r(\xi)\in(0,\infty]\) be the supremum of such \(s\). The analytic vectors form a subspace \(\mathcal D_0\) with \(T\mathcal D_0\subseteq\mathcal D_0\). If \(\mathcal D_0\) is dense, then \(T\) is self-adjoint and \(\mathcal D_0\) is a core for \(T\).

*Reference:* part (3) is Stone's theorem [Stone 1930], and part (5) is Nelson's analytic vector theorem.

**Proof.** (1) Let \(a\neq0\) and \(\alpha=-a\). By the criterion on spectral domains and strips (Section 1), \(\xi\in D(A^\alpha)\) exactly when the orbit extends to a bounded, norm-continuous function on \(\mathbb S(-\alpha)=\mathbb S(a)\) that is norm-holomorphic inside, and the extension is then \(A^{iz}\xi\). Such an extension is a strip function. Conversely, by Theorem 4.2(3) and (6) every strip function is bounded and norm continuous, and by Lemma 2.1(2) it is norm-holomorphic inside. So the two conditions agree, and \(U_{ia}\xi=A^{i(ia)}\xi=A^{-a}\xi\).

(2) Both sides of the identity are entire in \(z\) (the right side is the complex conjugate of an antiholomorphic function), and they agree for real \(z\) because \(U_t^*=U_{-t}\); so they agree everywhere, by the identity theorem. At \(z=ia\), where \(-\bar z=ia\), the identity says that \(U_{ia}\) is symmetric on \(D_\infty\). Also \(\langle U_{ia}\xi,\xi\rangle=\langle U_{ia/2}U_{ia/2}\xi,\xi\rangle=\langle U_{ia/2}\xi,U_{ia/2}\xi\rangle\ge0\) for entire \(\xi\), by Theorem 5.2(5) and the identity with \(z=ia/2\). The self-adjointness criterion of Section 1 applies to the dense subspace \(D_\infty\) and the maps \(U_z\): by Theorem 5.2(5) and (6), \(D_\infty\) is dense, the \(U_z\) map it into itself, satisfy \(U_{z+w}=U_zU_w\) and have norm-entire orbits, and the real \(U_t\) are unitary. So the positive symmetric operator \(U_{ia}\) on \(D_\infty\) is essentially self-adjoint. Since \(U_{ia}\) is closed and \(D_\infty\) is a core for it (Theorem 5.2(2) and (6)), \(U_{ia}\) is that self-adjoint closure. It is injective by Theorem 5.2(3).

(3) By (2), \(A\) is positive, self-adjoint and injective. Let \(P_n=1_{[1/n,n]}(A)\). By Theorem 5.2(1), \(U_t\) commutes with \(U_{-i}=A\), domains included, that is, \(U_tAU_t^*=A\); so \(U_t\) commutes with every \(P_n\) (spectral calculus, Section 1). Fix \(n\) and \(\xi\in P_nH\), and write \(A_n\) for the restriction of \(A\) to \(P_nH\), a bounded invertible operator. By Theorem 5.2(3) and (4), \(U_{-ik}=A^k\) and \(U_{ik}=A^{-k}\) for integers \(k\ge0\). Since \(P_nH\subseteq D(A^k)\) for all \(k\in\mathbb Z\), \(\xi\) lies in every \(D(U_{ik})\), hence, by the nesting in Theorem 5.2(4), in every \(D(U_{ia})\): \(\xi\) is entire. By Proposition 6.1(2), applied to \(B=P_n\), \(U_z\xi\in P_nH\). Put
\[
Q(z)=A_n^{-iz}U_z\xi\qquad(z\in\mathbb C).
\]
Here \(A_n^{-iz}=\exp(-iz\log A_n)\) is norm-entire because \(\log A_n\) is bounded, so \(Q\) is entire. By Theorem 5.2(5), \(U_zA\xi=U_zU_{-i}\xi=U_{-i}U_z\xi=AU_z\xi\), and hence
\[
Q(z-i)=A_n^{-iz}A_n^{-1}U_zU_{-i}\xi=A_n^{-iz}A_n^{-1}AU_z\xi=Q(z).
\]
For \(-1\le u\le0\), \(\|Q(s+iu)\|\le\|A_n^u\|\,\|U_sU_{iu}\xi\|\le n\,\|U_{iu}\xi\|\), which is bounded by continuity. So \(Q\) is bounded on a period strip, hence on \(\mathbb C\). By Liouville's theorem, applied to \(z\mapsto\langle Q(z),\eta\rangle\) for each \(\eta\), \(Q\) is constant: \(A^{-it}U_t\xi=Q(t)=Q(0)=\xi\). Thus \(U_t=A^{it}\) on each \(P_nH\). These subspaces increase to a dense subspace because \(A\) is injective, and both sides are unitary. If \(U_t=B^{it}\) for another positive self-adjoint injective \(B\), then (1) gives \(B=U_{-i}=A\). For the last statement, let \(\mu_\xi\) be the spectral measure of \(\xi\) for \(H_0\). If \(\xi\in D(H_0)\), then
\[
\Bigl\|\frac{U_t\xi-\xi}t-iH_0\xi\Bigr\|^2=\int\Bigl|\frac{e^{it\lambda}-1}t-i\lambda\Bigr|^2d\mu_\xi(\lambda)\to0
\]
by dominated convergence, with bound \(4\lambda^2\). If the limit exists, the integrals \(\int|t^{-1}(e^{it\lambda}-1)|^2d\mu_\xi\) stay bounded as \(t\to0\), and Fatou's lemma gives \(\int\lambda^2d\mu_\xi<\infty\), so \(\xi\in D(H_0)\).

(4) Let \(\overline{T_0}\) be the closure of \(T_0=H_0|_{\mathcal D}\); then \(\overline{T_0}\subseteq H_0\). On \(\mathcal D\), \(U_t\) maps the graph of \(T_0\) into itself, because \(H_0U_t\zeta=U_tH_0\zeta\); hence \(U_t\) preserves the graph of \(\overline{T_0}\), and Proposition 6.1(3a) applies to \(\overline{T_0}\) with \(V=U\). For \(\zeta\in D(H_0)\), (3) shows that \(t\mapsto U_t\zeta\) is continuously differentiable with derivative \(iU_tH_0\zeta\), so integration by parts gives
\[
(H_0\zeta)_r=\int g_r(t)\,U_tH_0\zeta\,dt=i\int g_r'(t)\,U_t\zeta\,dt .
\tag{8.1}
\]
Let \(\xi\in D(H_0)\) and choose \(\xi_m\in\mathcal D\) with \(\xi_m\to\xi\). By Proposition 6.1(3a), \((\xi_m)_r\in D(\overline{T_0})\) and \(\overline{T_0}(\xi_m)_r=(H_0\xi_m)_r=i\int g_r'(t)U_t\xi_m\,dt\), which tends to \(i\int g_r'(t)U_t\xi\,dt=(H_0\xi)_r\) as \(m\to\infty\), because \(g_r'\) is integrable and each \(U_t\) is unitary. Also \((\xi_m)_r\to\xi_r\). As \(\overline{T_0}\) is closed, \(\xi_r\in D(\overline{T_0})\) and \(\overline{T_0}\xi_r=(H_0\xi)_r\). As \(r\to\infty\), \(\xi_r\to\xi\) and \((H_0\xi)_r\to H_0\xi\) by Proposition 3.1(4), so closedness again gives \(\xi\in D(\overline{T_0})\).

(5) *Subspace and invariance.* Clearly \(r(\lambda\xi+\eta)\ge\min(r(\xi),r(\eta))\). If \(0<s<s'<r(\xi)\), the terms \(s'^m\|T^m\xi\|/m!\) are bounded by some \(C\), so
\[
\sum_n\frac{s^n\|T^{n+k}\xi\|}{n!}\le C\,s'^{-k}\sum_n\frac{(n+k)!}{n!}\Bigl(\frac s{s'}\Bigr)^n<\infty .
\]
Hence \(r(T^k\xi)\ge r(\xi)\) for every \(k\).

*Local evolution.* For \(\xi\in\mathcal D_0\) and \(|t|<r(\xi)\) put \(V_t\xi=\sum_n(it)^nT^n\xi/n!\), a norm-convergent series. Its partial sums \(p_m\) lie in \(D(T)\), and \(Tp_m\) are the partial sums of the series for \(V_tT\xi\). As \(T\) is closed, \(V_t\xi\in D(T)\) and \(TV_t\xi=V_tT\xi\); by induction \(T^kV_t\xi=V_tT^k\xi\). The function \(f(t)=\|V_t\xi\|^2\) is differentiable, with \(f'(t)=2\operatorname{Re}\langle iTV_t\xi,V_t\xi\rangle=0\) because \(\langle T\zeta,\zeta\rangle\) is real. So \(\|V_t\xi\|=\|\xi\|\). Applied to \(T^k\xi\), this gives \(\|T^kV_t\xi\|=\|T^k\xi\|\), so \(V_t\xi\in\mathcal D_0\) with \(r(V_t\xi)\ge r(\xi)\).

*Deficiency.* Let \(T_0=T|_{\mathcal D_0}\), and let \(\eta\in D(T_0^*)\) with \(T_0^*\eta=i\eta\). For \(\xi\in\mathcal D_0\), \(\langle T^n\xi,\eta\rangle=\langle T^{n-1}\xi,i\eta\rangle=-i\langle T^{n-1}\xi,\eta\rangle\), so \(\langle T^n\xi,\eta\rangle=(-i)^n\langle\xi,\eta\rangle\) and
\[
\langle V_t\xi,\eta\rangle=\sum_n\frac{(it)^n(-i)^n}{n!}\langle\xi,\eta\rangle=e^t\langle\xi,\eta\rangle .
\]
Fix \(0<t_0<r(\xi)\) and let \(\xi_k=V_{t_0}^k\xi\). By the previous step, \(\xi_k\in\mathcal D_0\), \(r(\xi_k)\ge r(\xi)\), \(\|\xi_k\|=\|\xi\|\) and \(\langle\xi_k,\eta\rangle=e^{kt_0}\langle\xi,\eta\rangle\). So \(e^{kt_0}|\langle\xi,\eta\rangle|\le\|\xi\|\|\eta\|\) for all \(k\), and \(\langle\xi,\eta\rangle=0\). As \(\mathcal D_0\) is dense, \(\eta=0\). The case \(T_0^*\eta=-i\eta\) is the same with \(t_0<0\).

*Conclusion.* By Lemma 7.2(3), applied to the linear operators \(T_0\pm i\), and by the deficiency step, \(\operatorname{ran}(T_0\pm i)^\perp=\ker(T_0^*\mp i)=\{0\}\). The closure \(\overline{T_0}\) is symmetric and \(\|(\overline{T_0}\pm i)\zeta\|^2=\|\overline{T_0}\zeta\|^2+\|\zeta\|^2\), so \(\operatorname{ran}(\overline{T_0}\pm i)\) is closed and dense, hence equal to \(H\). If \(\eta\in D(T_0^*)\), choose \(\zeta\in D(\overline{T_0})\) with \((\overline{T_0}+i)\zeta=(T_0^*+i)\eta\). Since \(\overline{T_0}\subseteq T_0^*\), \((T_0^*+i)(\eta-\zeta)=0\), so \(\eta=\zeta\). Thus \(T_0^*=\overline{T_0}\) is self-adjoint. Finally \(\overline{T_0}\subseteq T\subseteq T^*\subseteq T_0^*=\overline{T_0}\), so \(T=\overline{T_0}\). \(\square\)

**Remark 8.2.** Here Stone's theorem (3) comes from the analytic generator \(U_{-i}\), the self-adjointness criterion and a periodicity argument, and the analytic vector theorem (5) is proved without Stone's theorem. Exercise 2 identifies the analytic vectors of a self-adjoint \(T\) with the vectors that are strip-analytic for \(e^{itT}\) on some symmetric strip.

## 9. Entire elements of automorphism groups of von Neumann algebras

**Setting.** Let \(N\subseteq B(K)\) be a von Neumann algebra with predual \(N_*\), the \(\sigma\)-weakly continuous linear functionals on \(N\). Let \(\sigma=(\sigma_t)_{t\in\mathbb R}\) be a group of \(*\)-automorphisms of \(N\) such that \(t\mapsto\omega(\sigma_t(x))\) is continuous for \(x\in N\), \(\omega\in N_*\). Each \(\sigma_t\) is normal, hence \(\sigma\)-weakly continuous, and isometric. Since \(N\) is the dual of \(N_*\), the triple \((N,N_*,\sigma)\) is in case (W\*) of Section 3 with \(M=1\), and its topology \(\tau\) is the \(\sigma\)-weak topology. We write \(\sigma_{ia}\), \(D(\sigma_{ia})\), \(\sigma_z\) and \(N_\infty\) for \(U_{ia}\), \(D(U_{ia})\), \(U_z\) and \(D_\infty\). For \(x\in D(\sigma_{ia})\) and \(w\in\mathbb S(a)\) we also write \(\sigma_w(x)\) for \(\Phi_x(w)\); by covariance and Theorem 5.2(4), \(\sigma_{s+iu}(x)=\sigma_s(\sigma_{iu}(x))\), and for entire \(x\) this agrees with Theorem 5.2(5).

An equivalent definition takes the \(x\) for which \(t\mapsto\sigma_t(x)\) extends to an \(N\)-valued entire function. This agrees with \(N_\infty\). An element of \(N_\infty\) has a norm-entire extension by Theorem 5.2(5). Conversely, if every \(\omega\in N_*\) composes holomorphically with an extension, Lemma 2.1, applied to the norm-closed norming subspace \(N_*\) of \(N^*\), makes the extension norm-entire, so its restrictions to strips are strip functions.

**Theorem 9.1.**
1. (*Adjoints.*) \(x\in D(\sigma_{ia})\) if and only if \(x^*\in D(\sigma_{-ia})\), and then \(\sigma_{-ia}(x^*)=\sigma_{ia}(x)^*\). For entire \(x\), \(\sigma_{\bar z}(x^*)=\sigma_z(x)^*\).
2. (*Products.*) If \(x\in D(\sigma_{ia})\) and \(y\in N_\infty\), then \(xy,yx\in D(\sigma_{ia})\), with \(\sigma_{ia}(xy)=\sigma_{ia}(x)\sigma_{ia}(y)\) and \(\sigma_{ia}(yx)=\sigma_{ia}(y)\sigma_{ia}(x)\). Consequently \(N_\infty\) is a unital \(*\)-subalgebra, \(\sigma_z(N_\infty)=N_\infty\), each \(\sigma_z\) is multiplicative on \(N_\infty\), and \(\sigma_{z+w}=\sigma_z\sigma_w\) there.
3. (*Density.*) \(N_\infty\) is \(\sigma\)-weakly dense in \(N\). For \(x\in N\) and \(r>0\), \(x_r\in N_\infty\), \(\|\sigma_z(x_r)\|\le e^{r(\operatorname{Im}z)^2}\|x\|\), and \(x_r\to x\) \(\sigma\)-weakly.
4. (*Implemented groups.*) Suppose \(W\) is a strongly continuous unitary group on \(K\) with \(\sigma_t(x)=W_txW_t^*\) for \(x\in N\). If \(x\in D(\sigma_{ia})\) and \(\xi\in D(W_{ia})\), then \(x\xi\in D(W_{ia})\) and \(W_{ia}x\xi=\sigma_{ia}(x)W_{ia}\xi\).
5. (*Form criterion.*) In the situation of (4), let \(\mathcal D_0\subseteq K\) be a dense subspace of \(W\)-entire vectors, \(x\in N\) and \(a\in\mathbb R\). For \(\xi,\eta\in\mathcal D_0\) the function \(h_{\xi,\eta}(w)=\langle xW_{-w}\xi,W_{-\bar w}\eta\rangle\) is entire. Then \(x\in D(\sigma_{ia})\) if and only if there is \(C\) with
\[
|h_{\xi,\eta}(t+ia)|\le C\,\|\xi\|\,\|\eta\|\qquad(t\in\mathbb R,\ \xi,\eta\in\mathcal D_0).
\tag{9.1}
\]
In that case \(\langle\sigma_w(x)\xi,\eta\rangle=h_{\xi,\eta}(w)\) for \(w\in\mathbb S(a)\) and \(\xi,\eta\in\mathcal D_0\), and \(\|\sigma_{ia}(x)\|\le C\).

**Proof.** (1) The map \(x\mapsto x^*\) is conjugate-linear, isometric and commutes with every \(\sigma_t\). For \(\omega\in N_*\), the functional \(x\mapsto\overline{\omega(x^*)}\) is again in \(N_*\). Apply Proposition 6.1(2), conjugate-linear case, in both directions. For entire \(x\) and \(z=s+ib\), \(\sigma_z(x)^*=\sigma_s(\sigma_{ib}(x))^*=\sigma_s(\sigma_{-ib}(x^*))=\sigma_{\bar z}(x^*)\).

(2) Put \(\Psi(z)=\Phi_x(z)\sigma_z(y)\) on \(\mathbb S(a)\). For \(\omega\in N_*\),
\[
\omega(\Psi(z))-\omega(\Psi(z_0))=\omega\bigl(\Phi_x(z)(\sigma_z(y)-\sigma_{z_0}(y))\bigr)+\omega\bigl((\Phi_x(z)-\Phi_x(z_0))\sigma_{z_0}(y)\bigr).
\]
The first term is at most \(\|\omega\|\sup\|\Phi_x\|\,\|\sigma_z(y)-\sigma_{z_0}(y)\|\), which tends to \(0\) because \(z\mapsto\sigma_z(y)\) is norm continuous (Theorem 5.2(5)) and \(\Phi_x\) is bounded (Theorem 4.2(3)). The second tends to \(0\) because \(m\mapsto\omega(m\sigma_{z_0}(y))\) is \(\sigma\)-weakly continuous (multiplication is separately \(\sigma\)-weakly continuous) and \(\Phi_x\) satisfies (S2). Inside the strip \(\Psi\) is a product of norm-holomorphic functions. At real \(t\), \(\Psi(t)=\sigma_t(x)\sigma_t(y)=\sigma_t(xy)\). So \(\Psi\) is the strip function of \(xy\). The case \(yx\) is the same. If \(x,y\) are entire, this holds for every \(a\); with (1) and Theorem 5.2(5) it gives the algebraic statements, since \(\sigma_z(xy)=\sigma_s(\sigma_{ib}(x)\sigma_{ib}(y))=\sigma_z(x)\sigma_z(y)\) for \(z=s+ib\), and \(1\in N_\infty\).

(3) This is Proposition 3.1(3)–(4) and Theorem 5.2(6) with \(M=1\).

(4) Let \(\Psi(z)=\Phi_x(z)\Phi_\xi(z)\), where \(\Phi_\xi\) is the strip function of \(\xi\) for \(W\), which is norm continuous by Theorem 4.2(6). As in (2), \(\Psi\) is weakly continuous on \(\mathbb S(a)\): \(\Phi_x\) is bounded and \(\sigma\)-weakly, hence weakly, continuous. It is holomorphic inside, and \(\Psi(t)=W_txW_t^*W_t\xi=W_tx\xi\). So \(\Psi\) is the strip function of \(x\xi\) for \(W\).

(5) Suppose \(x\in D(\sigma_{ia})\). For \(\xi,\eta\in\mathcal D_0\), the function \(k(w)=\langle\sigma_w(x)\xi,\eta\rangle\) is continuous on \(\mathbb S(a)\), holomorphic inside, and \(k(t)=\langle W_txW_{-t}\xi,\eta\rangle=\langle xW_{-t}\xi,W_{-t}\eta\rangle=h_{\xi,\eta}(t)\). By boundary uniqueness, \(k=h_{\xi,\eta}\) on \(\mathbb S(a)\), and (9.1) holds with \(C=\|\sigma_{ia}(x)\|\), since \(\sigma_{t+ia}(x)=\sigma_t(\sigma_{ia}(x))\).

Conversely assume (9.1). For \(w=s+iu\in\mathbb S(a)\), \(W_{-w}\xi=W_{-s}W_{-iu}\xi\) and \(W_{-\bar w}\eta=W_{-s}W_{iu}\eta\), so \(|h_{\xi,\eta}(w)|\le\|x\|\,\|W_{-iu}\xi\|\,\|W_{iu}\eta\|\). This is bounded on \(\mathbb S(a)\) for fixed \(\xi,\eta\). On the real line \(|h_{\xi,\eta}|\le\|x\|\|\xi\|\|\eta\|\). The bounded-strip maximum principle gives \(|h_{\xi,\eta}(w)|\le\max(\|x\|,C)\|\xi\|\|\eta\|\) on \(\mathbb S(a)\). For fixed \(w\), \(h_{\xi,\eta}(w)\) is linear in \(\xi\) and conjugate-linear in \(\eta\) on the subspace \(\mathcal D_0\), so there is a unique \(c(w)\in B(K)\) with \(\langle c(w)\xi,\eta\rangle=h_{\xi,\eta}(w)\) and \(\|c(w)\|\le\max(\|x\|,C)\). At real \(t\), \(c(t)=\sigma_t(x)\). For \(\xi,\eta\in\mathcal D_0\), \(w\mapsto\langle c(w)\xi,\eta\rangle\) is continuous on \(\mathbb S(a)\) and holomorphic inside; by the uniform bound and density this holds for all \(\xi,\eta\in K\). By Proposition 6.1(5), \(c(w)\in N\). The function \(c\) is bounded and weakly continuous, hence \(\sigma\)-weakly continuous, since the two topologies agree on bounded sets. It is norm-holomorphic inside by Lemma 2.1(2), with the vector functionals as norming set. So \(c\) is the strip function of \(x\), and \(x\in D(\sigma_{ia})\). On the line \(\operatorname{Im}w=a\) the form is bounded by \(C\), so \(\|\sigma_{ia}(x)\|=\|c(ia)\|\le C\). \(\square\)

**Remark 9.2.** Part (2) is stated for one strip-analytic and one entire factor. For two factors that are only strip-analytic, the product of two merely \(\sigma\)-weakly continuous functions need not be \(\sigma\)-weakly continuous, and this lesson does not treat that case. Part (5) turns bounds on two boundary lines into analyticity of an operator; Theorem 11.1(5) uses it.

**Example 9.3** (Case (W\*): no norm continuity at the boundary). On \(K=\ell^2(\mathbb N_0)\) let \(W_te_n=e^{i\mu_nt}e_n\) with \(\mu_{2k}=k\) and \(\mu_{2k+1}=0\), and \(\sigma_t=\operatorname{Ad}W_t\) on \(N=B(K)\). Write \(e_{jk}\) for the matrix unit \(e_{jk}\xi=\langle\xi,e_k\rangle e_j\). Let \(x=\sum_ke_{2k,2k+1}\), a partial isometry. Then \(\sigma_t(x)=\sum_ke^{ikt}e_{2k,2k+1}\). For \(\operatorname{Im}z\ge0\), let \(\Phi(z)\) be the operator with \(\Phi(z)e_{2k+1}=e^{ikz}e_{2k}\) and \(\Phi(z)e_{2k}=0\). Then \(\|\Phi(z)\|\le1\), and \(\langle\Phi(z)\xi,\eta\rangle=\sum_ke^{ikz}\langle\xi,e_{2k+1}\rangle\langle e_{2k},\eta\rangle\) converges uniformly, so \(\Phi\) is bounded, weakly (hence \(\sigma\)-weakly) continuous and holomorphic. Thus \(x\in D(\sigma_{ia})\) for every \(a>0\), and \(\Phi\) is norm-holomorphic where \(\operatorname{Im}z>0\). But \(\|\sigma_t(x)-x\|=\sup_k|e^{ikt}-1|\ge\sqrt3\) for \(0<|t|<2\pi/3\), since the angles \(kt\) meet every arc of length \(|t|\). So the strip function is not norm continuous on the real line, and \(x\) is not a norm limit of entire elements. Also \(x\notin D(\sigma_{-ia})\) for \(a>0\): the scalar continuation of \(\langle\sigma_t(x)e_{2k+1},e_{2k}\rangle=e^{ikt}\) would be \(e^{ikz}\) by boundary uniqueness, and its value \(e^{ka}\) at \(z=-ia\) is unbounded in \(k\), against Theorem 4.2(3).

## 10. Strip arguments for bounded functionals



**Definition 10.1** (Strip condition, modular condition). Let \(A\) be a C\*-algebra, \(\sigma\) a group of \(*\)-automorphisms of \(A\), and \(\omega\) a bounded linear functional on \(A\). The pair \((x,y)\in A\times A\) satisfies the *strip condition* if some function \(F_{x,y}\), bounded and continuous on \(\mathbb S(1)\) and holomorphic inside, satisfies
\[
F_{x,y}(t)=\omega(\sigma_t(x)y),\qquad F_{x,y}(t+i)=\omega(y\sigma_t(x))\qquad(t\in\mathbb R).
\tag{10.1}
\]
By boundary uniqueness there is at most one such function. A state satisfies the *modular condition* if it is \(\sigma\)-invariant and every pair satisfies the strip condition.

If \(\sigma\) is strongly continuous (\(t\mapsto\sigma_t(x)\) norm continuous), then \((A,A^*,\sigma)\) is in case (N) with \(M=1\). The proofs of Theorem 9.1(1)–(3) then apply word for word, with the norm topology in place of the \(\sigma\)-weak one. So the entire elements \(A_\infty\) form a norm-dense unital \(*\)-subalgebra when \(A\) is unital, \(\sigma_z\) is multiplicative on it, and \(\sigma_{\bar z}(x^*)=\sigma_z(x)^*\).

**Example 10.2** (A trace-class density on \(B(H)\)). Let \((e_k)_{k\ge0}\) be an orthonormal basis of \(H\), \(\lambda_k>0\) with \(\sum_k\lambda_k<\infty\), and \(h=\sum_k\lambda_ke_{kk}\), where \(e_{jk}\xi=\langle\xi,e_k\rangle e_j\). Every positive injective trace-class operator has this form (spectral theorem for compact self-adjoint operators). Put \(\varphi(x)=\sum_k\lambda_k\langle xe_k,e_k\rangle=\operatorname{Tr}(hx)\). It is a faithful normal positive functional: \(\varphi(x^*x)=\sum_k\lambda_k\|xe_k\|^2\), and monotone convergence gives normality. We show \(\sigma^\varphi_t(x)=h^{it}xh^{-it}\).

Write \(x_{kj}=\langle xe_j,e_k\rangle\), and let \(\sigma_t(x)=h^{it}xh^{-it}\); then \(\varphi\circ\sigma_t=\varphi\). Expanding in the basis,
\[
\varphi(\sigma_t(x)y)=\sum_{j,k}\lambda_k\Bigl(\frac{\lambda_k}{\lambda_j}\Bigr)^{it}x_{kj}y_{jk},\qquad
\varphi(y\sigma_t(x))=\sum_{j,k}\lambda_j\Bigl(\frac{\lambda_k}{\lambda_j}\Bigr)^{it}x_{kj}y_{jk}.
\]
Define \(F(z)=\sum_{j,k}\lambda_k(\lambda_k/\lambda_j)^{iz}x_{kj}y_{jk}\). For \(z=s+iu\) with \(0\le u\le1\), each term has modulus \(\lambda_k^{1-u}\lambda_j^u|x_{kj}||y_{jk}|\le(\lambda_k+\lambda_j)(|x_{kj}|^2+|y_{jk}|^2)/2\). Since \(\sum_j|x_{kj}|^2=\|x^*e_k\|^2\) and \(\sum_k|x_{kj}|^2=\|xe_j\|^2\), and similarly for \(y\), the sum of these bounds is at most \((\|x\|^2+\|y\|^2)\operatorname{Tr}h\). So the series converges uniformly on \(\mathbb S(1)\), and \(F\) is bounded, continuous, and holomorphic inside. At \(z=t\) it gives \(\varphi(\sigma_t(x)y)\); at \(z=t+i\) the factor \((\lambda_k/\lambda_j)^{-1}\) turns \(\lambda_k\) into \(\lambda_j\), giving \(\varphi(y\sigma_t(x))\). So \(\sigma\) satisfies the modular condition, and the KMS characterization of the modular group (Section 1) gives \(\sigma^\varphi=\sigma\). No normalization of \(\operatorname{Tr}h\) is needed, since that characterization holds for every faithful normal semifinite weight. If the ratios \(\lambda_k/\lambda_{k+1}\) are unbounded, choose a sparse set \(Q\) of indices along which \(r_k=\lambda_k/\lambda_{k+1}\to\infty\) and put \(x=\sum_{k\in Q}e_{k,k+1}\). Then \(\sigma_t(x)=\sum_{k\in Q}r_k^{it}e_{k,k+1}\), and at \(t=\pi/\log r_k\) the norm \(\|\sigma_t(x)-x\|\) is \(2\). So this modular orbit is not norm continuous.

**Theorem 10.3.**
1. (*Invariance is automatic.*) Let \(A\) be unital, \(\sigma\) any group of \(*\)-automorphisms, and \(\omega\) a bounded linear functional such that every pair \((x,1)\) satisfies the strip condition. Then \(\omega\circ\sigma_t=\omega\) for all \(t\).
2. (*Analytic form.*) Let \(A\) be unital and \(\sigma\) strongly continuous. For a bounded linear functional \(\omega\) the following are equivalent:
   - (i) every pair satisfies the strip condition;
   - (ii) \(\omega(\sigma_i(x)y)=\omega(yx)\) for all \(x\in A_\infty\) and \(y\in A\);
   - (iii) (ii) holds for all \(x\) in a norm-dense subspace \(\mathcal D_1\subseteq A_\infty\) with \(\sigma_t(\mathcal D_1)\subseteq\mathcal D_1\) for real \(t\), and all \(y\in A\).

   Then \(|F_{x,y}|\le\|\omega\|\,\|x\|\,\|y\|\) on \(\mathbb S(1)\), and \(\omega\) is \(\sigma\)-invariant.
3. (*The set of modular states.*) Let \(A\) be unital and \(\sigma\) strongly continuous. The set \(K\) of states that satisfy the modular condition is convex and weak\*-compact. It may be empty.

**Proof.** (1) Fix \(x\) and let \(F=F_{x,1}\). Since \(\sigma_t(1)=1\), \(F(t)=\omega(\sigma_t(x))=F(t+i)\). Define \(G(z)=F(z-ni)\) for \(n\le\operatorname{Im}z\le n+1\), \(n\in\mathbb Z\). The definitions agree on the lines \(\operatorname{Im}z=n\), so \(G\) is continuous on \(\mathbb C\), holomorphic off those lines, and holomorphic everywhere by the Morera argument across a line (Section 1). It is bounded, since \(F\) is. By Liouville's theorem \(G\) is constant, so \(\omega(\sigma_t(x))=G(t)=G(0)=\omega(x)\). No continuity of \(\sigma\) and no positivity of \(\omega\) was used.

(2) (i)\(\Rightarrow\)(ii): for \(x\in A_\infty\), \(z\mapsto\omega(\sigma_z(x)y)\) is continuous on \(\mathbb S(1)\), holomorphic inside and equal to \(F_{x,y}\) on the real line. By boundary uniqueness it equals \(F_{x,y}\), and at \(z=i\) it gives \(\omega(\sigma_i(x)y)=F_{x,y}(i)=\omega(yx)\). (ii)\(\Rightarrow\)(iii) is trivial.

(iii)\(\Rightarrow\)(i): for \(x\in\mathcal D_1\), put \(G_x(z)=\omega(\sigma_z(x)y)\). It is continuous and holomorphic, because \(z\mapsto\sigma_z(x)\) is norm-entire, and it is bounded on \(\mathbb S(1)\) because \(\|\sigma_{s+iu}(x)\|=\|\sigma_{iu}(x)\|\) is bounded for \(0\le u\le1\). Its boundary values are \(G_x(t)=\omega(\sigma_t(x)y)\) and, by (iii) applied to \(\sigma_t(x)\in\mathcal D_1\), \(G_x(t+i)=\omega(\sigma_i(\sigma_t(x))y)=\omega(y\sigma_t(x))\). For general \(x\), choose \(x_n\in\mathcal D_1\) with \(x_n\to x\). On both boundary lines \(|G_{x_n}-G_{x_m}|\le\|\omega\|\,\|x_n-x_m\|\,\|y\|\), because each \(\sigma_t\) is isometric. By the bounded-strip maximum principle, \(G_{x_n}\) converges uniformly on \(\mathbb S(1)\); the limit is bounded, continuous, holomorphic inside, and has the boundary values (10.1). The bound on \(F_{x,y}\) follows from the maximum principle, since both boundary values are at most \(\|\omega\|\|x\|\|y\|\) in modulus. Invariance follows from (1).

(3) By (1) and (2), \(K\) is the set of states \(\omega\) with \(\omega(\sigma_i(x)y-yx)=0\) for all \(x\in A_\infty\) and \(y\in A\). Each of these conditions is linear and weak\*-closed. The state space of a unital C\*-algebra is convex and weak\*-compact: since states have norm one, it is a weak\*-closed subset of the unit ball of \(A^*\), which is weak\*-compact by the Banach–Alaoglu theorem. Example 10.5 gives an empty \(K\). \(\square\)

**Remark 10.4.** For a normal functional on a von Neumann algebra with a \(\sigma\)-weakly continuous group, the implication (i)\(\Rightarrow\)(ii) holds with the same proof. The converse argument uses norm approximation by entire elements, which in case (W\*) is available only for elements whose orbits are norm continuous (Remark 5.3). Theorem 10.9 below proves the converse in general, with the Poisson representation of bounded holomorphic functions on a strip in place of norm approximation.

**Example 10.5** (An empty set of modular states). Let \(A=C(\mathbb T)\), \(\mathbb T=\mathbb R/2\pi\mathbb Z\), with the norm-continuous rotations \(\sigma_t(f)(\theta)=f(\theta-t)\). For a state \(\omega\) with the modular condition, commutativity gives \(F_{x,y}(t+i)=\omega(y\sigma_t(x))=\omega(\sigma_t(x)y)=F_{x,y}(t)\), and the periodicity argument in the proof of Theorem 10.3(1) makes \(F_{x,y}\) constant. With \(x(\theta)=e^{i\theta}\) and \(y=\bar x\), \(\sigma_t(x)y\) is the constant \(e^{-it}\), so \(\omega(\sigma_t(x)y)=e^{-it}\) is not constant. So \(K=\emptyset\) in Theorem 10.3(3).

### Poisson representation on a strip and the \(\sigma\)-weakly continuous case

**Lemma 10.6** (the Poisson kernel of \(\mathbb S(1)\)). For \(z=x+iy\) with \(0<y<1\) and \(t\in\mathbb R\) put
\[
P_0(z,t)=\frac{\sin\pi y}{2\bigl(\cosh\pi(t-x)-\cos\pi y\bigr)},\qquad
P_1(z,t)=\frac{\sin\pi y}{2\bigl(\cosh\pi(t-x)+\cos\pi y\bigr)} .
\tag{10.2}
\]

1. \(P_0,P_1>0\), \(\int_{\mathbb R}P_0(z,t)\,dt=1-y\) and \(\int_{\mathbb R}P_1(z,t)\,dt=y\).
2. \(P_0(z,t)=\operatorname{Im}\dfrac{e^{\pi t}}{e^{\pi t}-e^{\pi z}}\) and \(P_1(z,t)=-\operatorname{Im}\dfrac{e^{\pi t}}{e^{\pi t}+e^{\pi z}}\); so for fixed \(t\) both are harmonic functions of \(z\) on \(\mathbb S^\circ(1)\).
3. Let \(g_0,g_1:\mathbb R\to\mathbb C\) be bounded and continuous. The function \(u=P[g_0,g_1]\), defined by
\[
u(z)=\int_{\mathbb R}P_0(z,t)g_0(t)\,dt+\int_{\mathbb R}P_1(z,t)g_1(t)\,dt\quad(z\in\mathbb S^\circ(1)),\qquad u(t)=g_0(t),\quad u(t+i)=g_1(t),
\]
is continuous on \(\mathbb S(1)\), its real and imaginary parts are harmonic on \(\mathbb S^\circ(1)\), and \(|u|\le\max(\sup|g_0|,\sup|g_1|)\).

**Proof.** (1) Here \(\sin\pi y>0\) and \(\cosh\ge1>|\cos\pi y|\). Let \(0<a<\pi\). Differentiation gives
\[
\frac{d}{du}\arctan\frac{e^u-\cos a}{\sin a}=\frac{e^u\sin a}{\sin^2a+(e^u-\cos a)^2}=\frac{\sin a}{2(\cosh u-\cos a)} ,
\]
and the arctangent increases from \(\arctan(-\cot a)=a-\frac\pi2\) at \(u=-\infty\) to \(\frac\pi2\) at \(u=+\infty\). So
\(\int_{\mathbb R}\sin a\,du/(2(\cosh u-\cos a))=\pi-a\). With \(a=\pi y\) and \(u=\pi(t-x)\) this gives \(\int P_0\,dt=1-y\);
with \(a=\pi-\pi y\), which changes the sign of \(\cos a\), it gives \(\int P_1\,dt=y\).

(2) With \(w=e^{\pi z}\), so that \(\operatorname{Im}w=e^{\pi x}\sin\pi y>0\), and \(s\) real, \(\operatorname{Im}\frac1{s-w}=\frac{\operatorname{Im}w}{|s-w|^2}\). For \(s=e^{\pi t}\),
\[
\frac{e^{\pi t}\operatorname{Im}w}{|e^{\pi t}-w|^2}=\frac{e^{\pi(t+x)}\sin\pi y}{e^{2\pi t}-2e^{\pi(t+x)}\cos\pi y+e^{2\pi x}}=P_0(z,t),
\]
and \(s=-e^{\pi t}\) gives \(P_1\) in the same way. The functions \(z\mapsto e^{\pi t}/(e^{\pi t}\mp e^{\pi z})\) are holomorphic on \(\mathbb S^\circ(1)\), where \(e^{\pi z}\) is not real, and real and imaginary parts of holomorphic functions are harmonic (background).

(3) The bound follows from (1). Let \(K\) be a compact subset of \(\mathbb S^\circ(1)\), with \(\delta\le y\le1-\delta\) and \(|x|\le R\) on \(K\). For \(A\) real and \(\delta\le y\le1-\delta\), \(\cosh A\mp\cos\pi y\ge\frac12(1-\cos\pi\delta)\cosh A\). Every partial derivative of order at most two of \(P_j(\cdot,t)\) is a sum of terms (derivatives of the numerator and of \(D=\cosh\pi(t-x)\mp\cos\pi y\)) divided by powers \(D^k\), with numerators at most a constant times \(\cosh^{k-1}\pi(t-x)\); so on \(K\) these derivatives are at most \(C_Ke^{-\pi|t|}\). Dominated convergence allows differentiation under the integral sign twice, so \(u\) is twice continuously differentiable on \(\mathbb S^\circ(1)\), and \(\Delta u=\int\Delta P_0\,g_0+\int\Delta P_1\,g_1=0\) by (2), for real and imaginary parts alike.

It remains to show continuity at the boundary. Let \(t_0\in\mathbb R\) and \(z=x+iy\to t_0\) with \(0<y<1\). The second integral is at most \(y\sup|g_1|\to0\). For the first, \(\int P_0(z,t)g_0(t)\,dt-(1-y)g_0(t_0)=\int P_0(z,t)(g_0(t)-g_0(t_0))\,dt\). Given \(\varepsilon>0\), choose \(\eta>0\) with \(|g_0(t)-g_0(t_0)|\le\varepsilon\) for \(|t-t_0|\le\eta\). That part of the integral is at most \(\varepsilon\). On \(|t-t_0|>\eta\) and for \(|x-t_0|<\eta/2\), \(|t-x|>\eta/2\) and \(P_0(z,t)\le\sin(\pi y)/(2(\cosh\pi(t-x)-1))\), whose integral over \(|t-x|>\eta/2\) is \(\sin(\pi y)\) times a finite constant and tends to \(0\). So \(u(z)\to g_0(t_0)\). At the upper line, \(P_1(x+iy,t)=P_0(x+i(1-y),t)\) and \(P_0(x+iy,t)=P_1(x+i(1-y),t)\), and the same argument gives \(u(z)\to g_1(t_0)\) as \(z\to t_0+i\). \(\square\)

**Lemma 10.7** (uniqueness). Let \(h\) be a bounded real function on \(\mathbb S(1)\), continuous, harmonic on \(\mathbb S^\circ(1)\), and \(0\) on both boundary lines. Then \(h=0\).

**Proof.** The function \(v(x,y)=\cosh x\,\cos(y-\tfrac12)\) is harmonic, and \(v\ge\cos(\tfrac12)\cosh x>0\) on \(\mathbb S(1)\). Let \(\varepsilon>0\) and \(|h|\le C\). For \(|x|\ge R\), with \(R\) large, \(h-\varepsilon v\le C-\varepsilon\cos(\tfrac12)\cosh x<0\). On the closed rectangle \(Q=[-R,R]\times[0,1]\) the continuous function \(h-\varepsilon v\) attains its maximum. If it did so at an interior point, it would be constant on the interior by the maximum principle for harmonic functions (background), hence on \(Q\) by continuity; in either case the maximum is attained on the boundary of \(Q\), where \(h-\varepsilon v\le0\). So \(h\le\varepsilon v\) on \(\mathbb S(1)\) for every \(\varepsilon>0\), and \(h\le0\). The same for \(-h\) gives \(h=0\). \(\square\)

**Corollary 10.8** (Poisson representation). Let \(G\) be bounded and continuous on \(\mathbb S(1)\) and holomorphic on \(\mathbb S^\circ(1)\). Then \(G=P[G|_{\mathbb R},G(\cdot+i)]\), that is, \(G(z)=\int P_0(z,t)G(t)\,dt+\int P_1(z,t)G(t+i)\,dt\) for \(z\in\mathbb S^\circ(1)\).

**Proof.** The real part of \(G-P[G|_{\mathbb R},G(\cdot+i)]\) is bounded, continuous on \(\mathbb S(1)\), harmonic inside (Lemma 10.6(3) and the background), and \(0\) on both lines; Lemma 10.7 makes it \(0\). The same holds for the imaginary part. \(\square\)

**Theorem 10.9** (the \(\sigma\)-weakly continuous case). Let \(N\), \(N_*\) and \(\sigma\) be as in Section 9, and let \(\omega\in N_*\). The following are equivalent:

- (i) every pair \((x,y)\in N\times N\) satisfies the strip condition (10.1);
- (ii) \(\omega(\sigma_i(x)y)=\omega(yx)\) for all \(x\in N_\infty\) and \(y\in N\).

Then \(|F_{x,y}|\le\|\omega\|\,\|x\|\,\|y\|\) on \(\mathbb S(1)\), and \(\omega\circ\sigma_t=\omega\) for all \(t\).

**Proof.** (i)\(\Rightarrow\)(ii) is Remark 10.4. Assume (ii), and let \(x,y\in N\). For \(r>0\), Theorem 9.1(3) gives \(x_r\in N_\infty\) with \(\|x_r\|\le\|x\|\), \(\|\sigma_z(x_r)\|\le e^{r(\operatorname{Im}z)^2}\|x\|\), and \(x_r\to x\) \(\sigma\)-weakly as \(r\to\infty\). The function \(G_r(z)=\omega(\sigma_z(x_r)y)\) is entire, because \(z\mapsto\sigma_z(x_r)\) is norm-entire (Proposition 3.1(3)), and it is bounded on \(\mathbb S(1)\). Its boundary values are \(g_{0,r}(t)=\omega(\sigma_t(x_r)y)\) and, by (ii) applied to \(\sigma_t(x_r)\in N_\infty\) and by \(\sigma_{t+i}=\sigma_i\sigma_t\) on \(N_\infty\) (Theorem 9.1(2)), \(g_{1,r}(t)=G_r(t+i)=\omega(y\sigma_t(x_r))\). Both are at most \(\|\omega\|\,\|x\|\,\|y\|\) in modulus. By Corollary 10.8, \(G_r=P[g_{0,r},g_{1,r}]\), so \(|G_r|\le\|\omega\|\,\|x\|\,\|y\|\) on \(\mathbb S(1)\).

Put \(g_0(t)=\omega(\sigma_t(x)y)\) and \(g_1(t)=\omega(y\sigma_t(x))\). They are bounded and continuous, because \(t\mapsto\sigma_t(x)\) is \(\sigma\)-weakly continuous, multiplication is separately \(\sigma\)-weakly continuous and \(\omega\) is normal. For the same reasons, and because each \(\sigma_t\) is \(\sigma\)-weakly continuous, \(g_{j,r}(t)\to g_j(t)\) for every \(t\) as \(r\to\infty\). Let \(F=P[g_0,g_1]\). By Lemma 10.6(3), \(F\) is continuous on \(\mathbb S(1)\) with \(F(t)=\omega(\sigma_t(x)y)\) and \(F(t+i)=\omega(y\sigma_t(x))\), and \(|F|\le\|\omega\|\,\|x\|\,\|y\|\). For \(z\in\mathbb S^\circ(1)\), dominated convergence in the Poisson integrals gives \(G_r(z)\to F(z)\). Take a sequence \(r_n\to\infty\). The functions \(G_{r_n}\) are holomorphic and uniformly bounded on \(\mathbb S^\circ(1)\), so by Montel's theorem (background) every subsequence has a further subsequence that converges uniformly on compact subsets. Its limit is \(F\), and a uniform limit of holomorphic functions on compact sets is holomorphic, since the integrals over triangles pass to the limit and Morera's theorem applies (background). So \(F\) is holomorphic on \(\mathbb S^\circ(1)\), and the pair \((x,y)\) satisfies (10.1) with \(F_{x,y}=F\). Invariance follows from Theorem 10.3(1). \(\square\)

For a state, Theorem 10.9 says that the modular condition can be tested on the \(\sigma\)-weakly dense algebra \(N_\infty\), with no norm continuity of the orbits.

## 11. Strip arguments for faithful normal semifinite weights

Sections 2–10 do not depend on this section; it prepares later lessons on modular theory. It uses the modular data of a weight, listed below.

**Setting.** Let \(M\) be a von Neumann algebra and \(\varphi\) a faithful normal semifinite weight on \(M\). Write \(\mathfrak n=\mathfrak n_\varphi=\{x\in M:\varphi(x^*x)<\infty\}\), \(\mathfrak m=\mathfrak m_\varphi\), \(\mathfrak a=\mathfrak a_\varphi=\mathfrak n\cap\mathfrak n^*\), and \(H\) for the GNS space with map \(\Lambda\); we identify \(M\) with its image on \(H\). The following facts are proved in the course *Modular theory and weights*, at the places named.
- **(W1)** \(\mathfrak n\) is a left ideal; \(\mathfrak m=\operatorname{span}\mathfrak n^*\mathfrak n\) is spanned by \(\mathfrak m^+=\mathfrak m\cap M_+=\{x\ge0:\varphi(x)<\infty\}\), and \(\varphi\) extends linearly to \(\mathfrak m\); if \(x\in\mathfrak m^+\), then \(x^{1/2}\in\mathfrak a\). (General weights: finite domains, GNS spaces, and normal representations, §§WG-003–WG-004; the last statement holds because \((x^{1/2})^*x^{1/2}=x\) and \(x^{1/2}\) is self-adjoint.)
- **(W2)** \(\langle\Lambda(x),\Lambda(y)\rangle=\varphi(y^*x)\) and \(\Lambda(mx)=m\Lambda(x)\) for \(x,y\in\mathfrak n\), \(m\in M\); \(\Lambda(\mathfrak n)\) is dense. (General weights, §WG-006; the representation is faithful by §WG-010.)
- **(W3)** The map \(\Lambda(x)\mapsto\Lambda(x^*)\) on \(\Lambda(\mathfrak a)\) is closable; its closure \(S\) is a closed involution, so \(S=J\Delta^{1/2}\) as in Theorem 7.6. Moreover, for \(x\in\mathfrak n\): \(x\in\mathfrak a\) if and only if \(\Lambda(x)\in D(S)\), and then \(S\Lambda(x)=\Lambda(x^*)\). (Closability is Weights and the Hilbert spaces of multiplication, §WH-10. By §WH-11 there, \(\Lambda(\mathfrak a)\) is a full left Hilbert algebra whose left-bounded vectors are exactly the elements of \(\Lambda(\mathfrak n)\). Fullness means that the left-bounded vectors in \(D(S)\) are the elements of \(\Lambda(\mathfrak a)\) (The full left Hilbert algebra obtained by dualizing twice, §§FL-03–FL-04), and \(\Lambda\) is injective because \(\varphi\) is faithful.)
- **(W4)** \(\sigma_t(x)=\Delta^{it}x\Delta^{-it}\) defines the modular group, a \(\sigma\)-weakly continuous group of automorphisms of \(M\); \(\varphi\circ\sigma_t=\varphi\) on \(M_+\); and \(\Lambda(\sigma_t(x))=\Delta^{it}\Lambda(x)\) for \(x\in\mathfrak n\). (The modular group and its analytic algebra, §MF-06, equations (MF.31)–(MF.33).)
- **(W5)** There is an increasing net \((e_\lambda)\) in \(\mathfrak m^+\) with \(\|e_\lambda\|\le1\) and supremum \(1\); and \(\varphi(\sup_\lambda x_\lambda)=\sup_\lambda\varphi(x_\lambda)\) for bounded increasing nets in \(M_+\) (normality). (The net is General weights, §WG-008; normality is the definition of a normal weight.)
- **(W6)** (used in (4b), (5) and (7)) Let \(\mathfrak a_0\) be the set of \(x\in\mathfrak a\) with \(\Lambda(x)\in\bigcap_{n\in\mathbb Z}D(\Delta^n)\) and \(\Delta^n\Lambda(x)\in\Lambda(\mathfrak a)\) for all \(n\in\mathbb Z\). Then \(\Lambda(\mathfrak a_0)\) is dense in \(H\). The set \(\Lambda(\mathfrak a_0)\) is the maximal Tomita algebra of the weight. (The modular group and its analytic algebra, §§MF-07–MF-09: \(\Lambda(\mathfrak a_0)\) is the algebra \(\mathcal A_0\) of (MF.34) for \(\mathcal A=\Lambda(\mathfrak a)\), and MF-08 and MF-09 prove it dense.)

By Theorem 8.1(1) and the nesting in Theorem 5.2(4), the vectors \(\Lambda(x)\), \(x\in\mathfrak a_0\), are entire for \(\Delta^{it}\). We write \(D(\sigma_{ia})\), \(\sigma_z\), \(M_\infty\) as in Section 9, and \(U_t=\Delta^{it}\), so that \(U_{-i/2}=\Delta^{1/2}\) (Theorem 8.1(1)).

**Theorem 11.1.**
1. (*Closability from the strip condition.*) Let \(A\) be a C\*-algebra, \(\sigma\) a group of \(*\)-automorphisms, and \(\omega\) a weight on \(A\) that is \(\sigma\)-invariant and satisfies the strip condition (10.1) for all \(x,y\in\mathfrak a_\omega\), with \(\omega\) extended linearly to \(\mathfrak m_\omega\). Let \(\Lambda_\omega\) be its GNS map. If \(x_n\in\mathfrak a_\omega\), \(\Lambda_\omega(x_n)\to0\) and \(\Lambda_\omega(x_n^*)\to\eta\), then \(\eta=0\). Hence \(\Lambda_\omega(x)\mapsto\Lambda_\omega(x^*)\) is a well-defined, closable, conjugate-linear map on \(\Lambda_\omega(\mathfrak a_\omega)\).
2. (*Right multiplication.*) If \(a\in D(\sigma_{-i/2})\) and \(x\in\mathfrak a\), then \(ax\in\mathfrak a\) and \(\Delta^{1/2}\Lambda(ax)=\sigma_{-i/2}(a)\Delta^{1/2}\Lambda(x)\). Equivalently, if \(b\in D(\sigma_{i/2})\) and \(y\in\mathfrak a\), then \(yb\in\mathfrak a\) and
\[
\Lambda(yb)=J\sigma_{i/2}(b)^*J\,\Lambda(y).
\tag{11.1}
\]
Moreover \(yb\in\mathfrak n\) and (11.1) hold for every \(y\in\mathfrak n\).
3. (*Modules.*) \(D(\sigma_{-i/2})\mathfrak a\subseteq\mathfrak a\), \(\mathfrak aD(\sigma_{i/2})\subseteq\mathfrak a\), \(D(\sigma_{-i/2})\mathfrak m\subseteq\mathfrak m\) and \(\mathfrak mD(\sigma_{i/2})\subseteq\mathfrak m\). So \(\mathfrak a\) and \(\mathfrak m\) are closed under left and right multiplication by elements of \(D(\sigma_{-i/2})\cap D(\sigma_{i/2})\). This set contains \(M_\infty\), so \(\mathfrak a\) and \(\mathfrak m\) are \(M_\infty\)-bimodules; whether the set itself is closed under products is not decided in this lesson.
4. (*Two-point functions.*)
   - (a) Let \(a\in D(\sigma_{-i/2})\cap D(\sigma_{i/2})\) and \(z=w^*v\) with \(v,w\in\mathfrak n\). Let \(\Psi\) be the strip function of \(a\) on the symmetric strip \(|\operatorname{Im}\zeta|\le1/2\) (glued along the real line as in the proof of Theorem 5.2(5)). Then \(F_z(\alpha)=\langle J\Psi(\alpha-i/2)^*J\Lambda(v),\Lambda(w)\rangle\) is bounded and continuous on \(\mathbb S(1)\), holomorphic inside, and \(F_z(t)=\varphi(\sigma_t(a)z)\), \(F_z(t+i)=\varphi(z\sigma_t(a))\). If \(a\) is entire, \(F_z(\alpha)=\varphi(\sigma_\alpha(a)z)\) for all \(\alpha\).
   - (b) Let \(a\in M\) with \(\mathfrak na\subseteq\mathfrak n\) and \(\mathfrak na^*\subseteq\mathfrak n\), and let \(x,y\in\mathfrak a_0\). Then \(F(\alpha)=\langle a\Delta^{-i\alpha}\Lambda(x),\Delta^{-i\bar\alpha+1}\Lambda(y)\rangle\) is entire, bounded on \(\mathbb S(1)\), and \(F(t)=\varphi(\sigma_t(a)xy^*)\), \(F(t+i)=\varphi(xy^*\sigma_t(a))\).
   - The conditions \(\mathfrak na\subseteq\mathfrak n\), \(\mathfrak na^*\subseteq\mathfrak n\) are equivalent to \(a\mathfrak m\subseteq\mathfrak m\), \(\mathfrak ma\subseteq\mathfrak m\) (\(a\) is a *multiplier* of \(\mathfrak m\)).
5. (*Analytic form of the modular condition.*) For \(a\in M\) the following are equivalent: (i) \(a\in D(\sigma_i)\); (ii) \(\mathfrak na\subseteq\mathfrak n\), and there is \(b\in M\) with \(\mathfrak nb^*\subseteq\mathfrak n\) and \(\varphi(xa)=\varphi(bx)\) for all \(x\in\mathfrak m\). If they hold, every \(b\) as in (ii) equals \(\sigma_i(a)\).
6. (*Centralizer.*) An element \(a\in M\) satisfies \(\sigma_t(a)=a\) for all \(t\) if and only if \(a\) is a multiplier of \(\mathfrak m\) and \(\varphi(az)=\varphi(za)\) for all \(z\in\mathfrak m\).
7. (*Tomita ideal.*) \(\mathfrak a_0^*=\mathfrak a_0\), \(M_\infty\mathfrak a_0\subseteq\mathfrak a_0\) and \(\mathfrak a_0M_\infty\subseteq\mathfrak a_0\).

*Remark.* Part (1) proves the closability statement without assuming the weight faithful, semifinite or lower semicontinuous.

**Proof.** (1) We use (W1)–(W2) for \(\omega\) on \(A\): the finite domains, the linear extension of \(\omega\) to \(\mathfrak m_\omega\), and the GNS map \(\Lambda_\omega\) into the completion \(H_\omega\) of \(\mathfrak n_\omega\) modulo null vectors. For a weight on a C\*-algebra they are constructed in Finite domains and the GNS space of a C\*-weight, §§CS-01–CS-02. Let \(y\in\mathfrak a_\omega\), and let \(F_n\) be the strip function of the pair \((y,x_n^*)\). By (W2) for \(\omega\),
\[
F_n(t)=\omega(\sigma_t(y)x_n^*)=\langle\Lambda_\omega(x_n^*),\Lambda_\omega(\sigma_t(y^*))\rangle,\qquad F_n(t+i)=\omega(x_n^*\sigma_t(y))=\langle\Lambda_\omega(\sigma_t(y)),\Lambda_\omega(x_n)\rangle .
\]
Invariance gives \(\|\Lambda_\omega(\sigma_t(y^*))\|^2=\omega(\sigma_t(yy^*))=\|\Lambda_\omega(y^*)\|^2\) and similarly for \(\sigma_t(y)\). So on the lower line \(|F_n-F_m|\le\|\Lambda_\omega(x_n^*)-\Lambda_\omega(x_m^*)\|\,\|\Lambda_\omega(y^*)\|\), and on the upper line \(|F_n-F_m|\le\|\Lambda_\omega(y)\|\,\|\Lambda_\omega(x_n)-\Lambda_\omega(x_m)\|\), uniformly in \(t\). The bounded-strip maximum principle makes \((F_n)\) uniformly Cauchy on \(\mathbb S(1)\). The limit \(F\) is bounded, continuous, holomorphic inside, vanishes on the upper line, and equals \(\langle\eta,\Lambda_\omega(\sigma_t(y^*))\rangle\) on the lower line. Boundary uniqueness gives \(F=0\), so \(\langle\eta,\Lambda_\omega(y^*)\rangle=F(0)=0\). As \(\mathfrak a_\omega^*=\mathfrak a_\omega\), \(\eta\) is orthogonal to \(\Lambda_\omega(\mathfrak a_\omega)\). But \(\eta\) is a limit of vectors \(\Lambda_\omega(x_n^*)\) in that subspace, so \(\eta=0\). With the constant sequence \(x_n=x\), this shows that \(\Lambda_\omega(x)=0\) implies \(\Lambda_\omega(x^*)=0\), so the map is well defined.

(2) Let \(a\in D(\sigma_{-i/2})\) and \(x\in\mathfrak a\). By (W3), \(\Lambda(x)\in D(S)=D(\Delta^{1/2})=D(U_{-i/2})\). By Theorem 9.1(4), with \(N=M\), \(K=H\) and \(W=U\), which implements \(\sigma\) by (W4), the vector \(a\Lambda(x)=\Lambda(ax)\) lies in \(D(\Delta^{1/2})\) and \(\Delta^{1/2}\Lambda(ax)=\sigma_{-i/2}(a)\Delta^{1/2}\Lambda(x)\). Since \(ax\in\mathfrak n\) and \(\Lambda(ax)\in D(S)\), (W3) gives \(ax\in\mathfrak a\) and
\[
\Lambda(x^*a^*)=S\Lambda(ax)=J\sigma_{-i/2}(a)\Delta^{1/2}\Lambda(x)=J\sigma_{-i/2}(a)J\,\Lambda(x^*),
\]
using \(J^2=1\) and \(J\Delta^{1/2}\Lambda(x)=S\Lambda(x)=\Lambda(x^*)\). Put \(b=a^*\) and \(y=x^*\). By Theorem 9.1(1), \(b\in D(\sigma_{i/2})\) exactly when \(a\in D(\sigma_{-i/2})\), with \(\sigma_{-i/2}(a)=\sigma_{i/2}(b)^*\). This is (11.1) for \(y\in\mathfrak a\).

Now let \(y\in\mathfrak n\), \(b\in D(\sigma_{i/2})\), \(R=J\sigma_{i/2}(b)^*J\), and \((e_\lambda)\) as in (W5). By (W1), \(e_\lambda^{1/2}\in\mathfrak a\). So \(e_\lambda^{1/2}y\in\mathfrak n\) (left ideal) and \((e_\lambda^{1/2}y)^*=y^*e_\lambda^{1/2}\in\mathfrak n\); that is, \(e_\lambda^{1/2}y\in\mathfrak a\). By the first part and (W2),
\[
\varphi(b^*y^*e_\lambda yb)=\|\Lambda(e_\lambda^{1/2}yb)\|^2=\|Re_\lambda^{1/2}\Lambda(y)\|^2\le\|R\|^2\|\Lambda(y)\|^2 .
\]
The net \(b^*y^*e_\lambda yb\) increases to \(b^*y^*yb\), so (W5) gives \(\varphi(b^*y^*yb)\le\|R\|^2\|\Lambda(y)\|^2\), that is, \(yb\in\mathfrak n\). Finally \(e_\lambda^{1/2}\to1\) strongly: for \(0\le e\le1\), \(\|(1-e^{1/2})\zeta\|^2\le\langle(1-e^{1/2})\zeta,\zeta\rangle\le\langle(1-e)\zeta,\zeta\rangle\). So \(\Lambda(e_\lambda^{1/2}yb)=e_\lambda^{1/2}\Lambda(yb)\to\Lambda(yb)\), while \(Re_\lambda^{1/2}\Lambda(y)\to R\Lambda(y)\). This is (11.1).

(3) The statements about \(\mathfrak a\) are (2). For \(\mathfrak m\), let \(z=w^*v\) with \(v,w\in\mathfrak n\); such products span \(\mathfrak m\). If \(a\in D(\sigma_{-i/2})\), then \(a^*\in D(\sigma_{i/2})\) by Theorem 9.1(1), so \(wa^*\in\mathfrak n\) by (2) and \(az=(wa^*)^*v\in\mathfrak n^*\mathfrak n\). If \(b\in D(\sigma_{i/2})\), then \(zb=w^*(vb)\) with \(vb\in\mathfrak n\). Entire elements lie in both domains.

(4a) Let \(t\) be real. The element \(b_t=\sigma_t(a^*)\) lies in \(D(\sigma_{i/2})\), and by Theorem 9.1(1) and Theorem 5.2(1), \(\sigma_{i/2}(b_t)^*=\sigma_t(\sigma_{-i/2}(a))=\Psi(t-i/2)\). By (2), \(\Lambda(wb_t)=J\Psi(t-i/2)J\Lambda(w)\). Hence
\[
\varphi(\sigma_t(a)z)=\varphi\bigl((wb_t)^*v\bigr)=\langle\Lambda(v),J\Psi(t-i/2)J\Lambda(w)\rangle=\langle J\Psi(t-i/2)^*J\Lambda(v),\Lambda(w)\rangle=F_z(t),
\]
using \((JcJ)^*=Jc^*J\). Also \(\sigma_t(a)\in D(\sigma_{i/2})\) with \(\sigma_{i/2}(\sigma_t(a))=\Psi(t+i/2)\), so (2) gives \(\Lambda(v\sigma_t(a))=J\Psi(t+i/2)^*J\Lambda(v)\), and \(\varphi(z\sigma_t(a))=\langle\Lambda(v\sigma_t(a)),\Lambda(w)\rangle=F_z(t+i)\). The map \(c\mapsto Jc^*J\) is linear and isometric, and it is weakly continuous, since \(\langle Jc^*J\xi,\eta\rangle=\langle cJ\eta,J\xi\rangle\). As \(\Psi\) is bounded, weakly continuous and holomorphic inside its strip, \(F_z\) is bounded, continuous on \(\mathbb S(1)\) and holomorphic inside. If \(a\) is entire, the same computation with complex \(\alpha\) in place of \(t\) (using \(\sigma_\alpha(a)^*=\sigma_{\bar\alpha}(a^*)\) and \(\sigma_{i/2}(\sigma_{\bar\alpha}(a^*))^*=\sigma_{\alpha-i/2}(a)\)) gives \(F_z(\alpha)=\varphi(\sigma_\alpha(a)z)\).

(4b) By (W4), \(\mathfrak n\sigma_t(a)=\sigma_t(\mathfrak na)\subseteq\mathfrak n\), and likewise for \(a^*\). So \(u=\sigma_t(a)x\) lies in \(\mathfrak a\): it is in \(\mathfrak n\), and \(u^*=x^*\sigma_t(a^*)\in\mathfrak n\). Similarly \(u'=\sigma_t(a^*)y\in\mathfrak a\). The vectors \(\Lambda(x),\Lambda(y)\) are entire, so \(F\) is entire; for \(\alpha=s+iv\) with \(0\le v\le1\), \(|F(\alpha)|\le\|a\|\,\|\Delta^v\Lambda(x)\|\,\|\Delta^{1-v}\Lambda(y)\|\), which is bounded. Since \(\Delta^{1/2}=JS\) and \(J\) is antiunitary,
\[
F(t)=\langle\sigma_t(a)\Lambda(x),\Delta\Lambda(y)\rangle=\langle\Delta^{1/2}\Lambda(u),\Delta^{1/2}\Lambda(y)\rangle=\langle S\Lambda(y),S\Lambda(u)\rangle=\langle\Lambda(y^*),\Lambda(u^*)\rangle=\varphi(uy^*),
\]
and
\[
F(t+i)=\langle\sigma_t(a)\Delta\Lambda(x),\Lambda(y)\rangle=\langle\Delta^{1/2}\Lambda(x),\Delta^{1/2}\Lambda(u')\rangle=\langle S\Lambda(u'),S\Lambda(x)\rangle=\varphi(xu'^*)=\varphi(xy^*\sigma_t(a)).
\]
For the equivalence: if \(\mathfrak na\subseteq\mathfrak n\) and \(\mathfrak na^*\subseteq\mathfrak n\), then \(w^*va=w^*(va)\) and \(aw^*v=(wa^*)^*v\) lie in \(\mathfrak n^*\mathfrak n\). Conversely, if \(a\mathfrak m\subseteq\mathfrak m\) and \(\mathfrak ma\subseteq\mathfrak m\), then \(a^*\mathfrak m=(\mathfrak ma)^*\subseteq\mathfrak m\). For \(y\in\mathfrak n\), \(a^*y^*ya\in\mathfrak m\cap M_+=\mathfrak m^+\) by (W1), so \(\varphi((ya)^*ya)<\infty\) and \(ya\in\mathfrak n\). The same argument applies to \(a^*\).

(5) (i)\(\Rightarrow\)(ii). Let \(a\in D(\sigma_i)\) and \(b=\sigma_i(a)\). By the nesting in Theorem 5.2(4), \(a\in D(\sigma_{i/2})\), so \(\mathfrak na\subseteq\mathfrak n\) by (2). By Theorem 9.1(1), \(a^*\in D(\sigma_{-i})\) with \(\sigma_{-i}(a^*)=b^*\), and by Theorem 5.2(3), \(b^*\in D(\sigma_i)\subseteq D(\sigma_{i/2})\); so \(\mathfrak nb^*\subseteq\mathfrak n\). By Theorem 5.2(4), \(\sigma_{i/2}(b^*)=\sigma_{i/2}\sigma_{-i}(a^*)=\sigma_{-i/2}(a^*)=\sigma_{i/2}(a)^*\). For \(x=w^*v\) with \(v,w\in\mathfrak n\), (11.1) gives
\[
\varphi(xa)=\langle\Lambda(va),\Lambda(w)\rangle=\langle J\sigma_{i/2}(a)^*J\Lambda(v),\Lambda(w)\rangle,
\]
\[
\varphi(bx)=\langle\Lambda(v),\Lambda(wb^*)\rangle=\langle\Lambda(v),J\sigma_{i/2}(a)J\Lambda(w)\rangle=\langle J\sigma_{i/2}(a)^*J\Lambda(v),\Lambda(w)\rangle .
\]
By linearity \(\varphi(xa)=\varphi(bx)\) on \(\mathfrak m\).

(ii)\(\Rightarrow\)(i). Let \(b\) be as in (ii). *Step 1.* If \(y\in\mathfrak a\) and \(c\in M\) with \(yc\in\mathfrak a\), then
\[
\Delta^{1/2}\Lambda(yc)=JS\Lambda(yc)=J\Lambda(c^*y^*)=Jc^*S\Lambda(y)=(Jc^*J)\,\Delta^{1/2}\Lambda(y).
\tag{11.2}
\]
Under (ii), \(ya\) and \(yb^*\) lie in \(\mathfrak a\) for every \(y\in\mathfrak a\): they lie in \(\mathfrak n\), and their adjoints \(a^*y^*\), \(by^*\) lie in the left ideal \(\mathfrak n\). Put \(a'=Ja^*J\) and \(b''=JbJ\).

*Step 2.* Let \(x,y\in\mathfrak a_0\) and define the entire functions
\[
h(w)=\langle a'\Delta^{-iw}\Lambda(x),\Delta^{-i\bar w}\Lambda(y)\rangle,\qquad k(w)=\langle b''^*\Delta^{-iw}\Lambda(x),\Delta^{-i\bar w}\Lambda(y)\rangle .
\]
For real \(t\) let \(x_t=\sigma_{-t}(x)\) and \(y_t=\sigma_{-t}(y)\); they lie in \(\mathfrak a\), and \(\Lambda(x_t)=\Delta^{-it}\Lambda(x)\), \(\Lambda(y_t)=\Delta^{-it}\Lambda(y)\) are entire vectors. Compute \(c(t)=\varphi(y_t^*x_ta)=\langle\Lambda(x_ta),\Lambda(y_t)\rangle\) in two ways. By (11.2) with \(c=a\),
\[
c(t)=\langle\Delta^{1/2}\Lambda(x_ta),\Delta^{-1/2}\Lambda(y_t)\rangle=\langle a'\Delta^{1/2}\Delta^{-it}\Lambda(x),\Delta^{-1/2}\Delta^{-it}\Lambda(y)\rangle=h(t+i/2).
\]
By (ii) with \(y_t^*x_t\in\mathfrak m\), and (11.2) with \(c=b^*\),
\[
c(t)=\varphi(by_t^*x_t)=\langle\Lambda(x_t),\Lambda(y_tb^*)\rangle=\langle\Delta^{-1/2}\Lambda(x_t),b''\Delta^{1/2}\Lambda(y_t)\rangle=k(t-i/2).
\]
So the entire functions \(w\mapsto h(w+i/2)\) and \(w\mapsto k(w-i/2)\) agree on the real line, hence everywhere: \(h(w+i)=k(w)\). In particular \(|h(t+i)|=|k(t)|\le\|b\|\,\|\Lambda(x)\|\,\|\Lambda(y)\|\).

*Step 3.* Apply Theorem 9.1(5) to the von Neumann algebra \(B(H)\), the unitary group \(\Delta^{it}\), the group \(\sigma'_t=\operatorname{Ad}\Delta^{it}\) on \(B(H)\), the dense subspace \(\mathcal D_0=\Lambda(\mathfrak a_0)\) of entire vectors (dense by (W6)), the operator \(a'\), strip height \(1\) in (9.1), and \(C=\|b\|\). Its function \(h_{\xi,\eta}\) is \(h\). So \(a'\) has a strip function \(c'\) on \(\mathbb S(1)\) for \(\sigma'\), with \(\langle c'(w)\xi,\eta\rangle=h(w)\) on \(\mathcal D_0\); in particular \(c'(i)=b''^*\), since \(h(i)=k(0)\).

*Step 4.* Put \(\Theta(c)=Jc^*J\) on \(B(H)\). By Theorem 7.6(5), \(J\Delta^{it}=\Delta^{it}J\), so \(\Theta\sigma'_t=\sigma'_t\Theta\), and \(\Theta(a')=a\), \(\Theta(b''^*)=b\). The function \(w\mapsto\Theta(c'(w))\) is bounded, weakly continuous (as in (4a)), holomorphic inside by Lemma 2.1(2), and equals \(\sigma'_t(a)=\sigma_t(a)\in M\) at real \(t\). By Proposition 6.1(5) its values lie in \(M\), so it is the strip function of \(a\) for \(\sigma\) on \(\mathbb S(1)\). Hence \(a\in D(\sigma_i)\) and \(\sigma_i(a)=\Theta(c'(i))=b\).

(6) If \(a\) is a multiplier of \(\mathfrak m\) with \(\varphi(az)=\varphi(za)\), then by the last statement of (4) and by (5) with \(b=a\), \(a\in D(\sigma_i)\) and \(\sigma_i(a)=a\). Its strip function \(\Phi\) on \(\mathbb S(1)\) satisfies \(\Phi(t+i)=\sigma_t(\sigma_i(a))=\Phi(t)\). For \(\omega\in M_*\), the periodic extension of \(\omega\circ\Phi\) is entire and bounded, as in the proof of Theorem 10.3(1), hence constant; so \(\omega(\sigma_t(a))=\omega(a)\) for all \(\omega\), and \(\sigma_t(a)=a\). Conversely, if \(\sigma_t(a)=a\) for all \(t\), the constant function is a strip function, so \(a\) is entire with \(\sigma_i(a)=a\), and (5) with \(b=a\), together with (4), gives the multiplier property and \(\varphi(xa)=\varphi(ax)\) on \(\mathfrak m\).

(7) Let \(x\in\mathfrak a_0\) and \(\Delta^n\Lambda(x)=\Lambda(x_n)\) with \(x_n\in\mathfrak a\). *Adjoints:* \(\Lambda(x^*)=J\Delta^{1/2}\Lambda(x)\) lies in every \(D(\Delta^n)\), because \(\Delta^{1/2}\Lambda(x)\) is entire and \(JD(\Delta^{-n})=D(\Delta^n)\) (Theorem 7.6(5)); and \(\Delta^n\Lambda(x^*)=J\Delta^{1/2}\Delta^{-n}\Lambda(x)=S\Lambda(x_{-n})=\Lambda(x_{-n}^*)\in\Lambda(\mathfrak a)\). So \(x^*\in\mathfrak a_0\). *Left multiplication:* let \(a\in M_\infty\). By (2), \(ax\in\mathfrak a\). By Theorem 9.1(4), applied on every strip, \(\Lambda(ax)=a\Lambda(x)\) is entire and \(\Delta^n\Lambda(ax)=\sigma_{-in}(a)\Delta^n\Lambda(x)=\sigma_{-in}(a)\Lambda(x_n)=\Lambda(\sigma_{-in}(a)x_n)\), which lies in \(\Lambda(\mathfrak a)\) by (2), since \(\sigma_{-in}(a)\in M_\infty\). So \(ax\in\mathfrak a_0\). *Right multiplication:* \(xa=(a^*x^*)^*\) with \(a^*\in M_\infty\) and \(x^*\in\mathfrak a_0\). \(\square\)

**Remark 11.2.** In (2) and (3) the multiplying elements need only be analytic on a half strip, and in (4a) on the symmetric strip \(|\operatorname{Im}\zeta|\le1/2\); none of them needs to be entire, and (2) holds for all \(y\in\mathfrak n\). Example 11.3 shows that the half strip in (2) cannot be shortened.

**Example 11.3** (The half strip in Theorem 11.1(2) cannot be shortened). Take Example 10.2 with \(\lambda_k=e^{-k^2}\), fix \(0<s_0<1/2\), and let \(b\) be the weighted shift \(be_k=\beta_ke_{k+1}\) with \(\beta_k=e^{-s_0(2k+1)}\). By Example 10.2, \(\sigma_z(b)\) should act by \(e_k\mapsto\beta_k(\lambda_{k+1}/\lambda_k)^{iz}e_{k+1}\), and for \(z=s+iu\) the weights have modulus \(e^{(u-s_0)(2k+1)}\le1\) when \(0\le u\le s_0\). As in Example 9.3, these operators form a strip function, so \(b\in D(\sigma_{is_0})\). Now test (11.1) on \(y=e_{0m}\) (\(m\ge1\)): \(\|\Lambda(y)\|^2=\varphi(e_{mm})=\lambda_m\), and \(yb=\beta_{m-1}e_{0,m-1}\), so
\[
\frac{\|\Lambda(yb)\|^2}{\|\Lambda(y)\|^2}=\frac{\beta_{m-1}^2\lambda_{m-1}}{\lambda_m}=e^{(1-2s_0)(2m-1)}\longrightarrow\infty .
\]
So \(\Lambda(y)\mapsto\Lambda(yb)\) is unbounded: no bounded operator satisfies (11.1), and \(b\notin D(\sigma_{i/2})\). Here \(\varphi\) is finite, so \(yb\in\mathfrak n\) holds trivially; what fails is the bounded formula.

## Exercises

**Exercise 1 (log-convexity).** In the Setting of Section 3, let \(U\) be isometric (\(M=1\)), \(a>0\), and \(x\in D(U_{ia})\). Show that \(b\mapsto\log\|U_{ib}x\|\) is convex on \([0,a]\), with \(\log0=-\infty\).

*Solution.* Let \(0\le b_1<b_2\le a\) and \(y=U_{ib_1}x\). By Theorem 5.2(4), \(y\in D(U_{i(b_2-b_1)})\) and \(U_{i(b-b_1)}y=U_{ib}x\) for \(b_1\le b\le b_2\). Theorem 5.2(7) for \(y\) on the strip of width \(b_2-b_1\) gives \(\|U_{ib}x\|\le\|U_{ib_1}x\|^{1-\theta}\|U_{ib_2}x\|^\theta\) with \(\theta=(b-b_1)/(b_2-b_1)\). Taking logarithms gives convexity.

**Exercise 2 (analytic vectors and strips).** Let \(T\) be self-adjoint and \(U_t=e^{itT}\). Show that \(\xi\) is an analytic vector of \(T\) with \(r(\xi)\ge s_0\), in the sense of Theorem 8.1(5), if and only if \(\xi\in D(U_{is})\cap D(U_{-is})\) for every \(0<s<s_0\).

*Solution.* By Theorem 8.1(1) with \(A=e^T\), \(D(U_{is})\cap D(U_{-is})=D(A^{-s})\cap D(A^s)=D(e^{s|T|})\), since \(e^{2s\lambda}+e^{-2s\lambda}\) and \(e^{2s|\lambda|}\) are comparable. Let \(\mu\) be the spectral measure of \(\xi\). If \(\xi\in D(e^{s'|T|})\) and \(s<s'\), then \(|\lambda|^n\le n!\,s'^{-n}e^{s'|\lambda|}\) gives \(\|T^n\xi\|\le n!\,s'^{-n}\|e^{s'|T|}\xi\|\), so \(\sum_ns^n\|T^n\xi\|/n!<\infty\). Conversely, if \(\sum_ns^n\|T^n\xi\|/n!<\infty\), the vectors \(\sum_{n\le m}s^n|T|^n\xi/n!\) converge in norm, because \(\||T|^n\xi\|=\|T^n\xi\|\); their squared norms are \(\int(\sum_{n\le m}s^n|\lambda|^n/n!)^2d\mu\), and monotone convergence gives \(\int e^{2s|\lambda|}d\mu<\infty\).

**Exercise 3 (a conjugate-linear adjoint).** On \(L^2(\mathbb R)\) let \(C\) be complex conjugation and \(g\) a measurable function. Let \(T=CM_g\), where \(M_g\) is multiplication by \(g\) on its maximal domain. Find \(T^*\), \(T^*T\) and the polar decomposition of \(T\), and decide when \(T\) is an involution.

*Solution.* For \(f\in D(M_g)\), \(\langle k,Tf\rangle=\int kgf\), a bounded function of \(f\) exactly when \(gk\in L^2\). By (7.1), \(\langle f,T^*k\rangle=\int kgf\), so \(T^*k=\overline{gk}\): \(T^*=CM_g=T\). Then \(T^*Tf=\overline{g\,\overline{gf}}=|g|^2f\), so \(|T|=M_{|g|}\) and \(T=(CM_u)M_{|g|}\) with \(u=g/|g|\) on \(\{g\ne0\}\) and \(u=0\) elsewhere; \(CM_u\) is a conjugate-linear partial isometry with initial space \(L^2(\{g\ne0\})\). Finally \(T^2f=\bar ggf\), so \(T\) is an involution exactly when \(|g|=1\) almost everywhere; then \(\Delta=1\) and \(J=T\). Example 7.8 shows an involution with nontrivial \(\Delta\), obtained by adding the reflection \(s\mapsto-s\).

**Exercise 4 (the modular condition on \(M_2(\mathbb C)\)).** Let \(\omega=\operatorname{Tr}(\rho\,\cdot)\) with \(\rho=\operatorname{diag}(p,1-p)\), \(0<p<1\). Using Section 10, find all groups \(\sigma_t=\operatorname{Ad}e^{itK}\), \(K\) self-adjoint, for which \(\omega\) satisfies the modular condition.

*Solution.* By Theorem 10.3(1), \(\omega\) is \(\sigma\)-invariant, that is, \(e^{-itK}\rho e^{itK}=\rho\) for all \(t\), so \(K\) commutes with \(\rho\). If \(p\ne1/2\), then \(K=\operatorname{diag}(\kappa_1,\kappa_2)\) and \(\sigma_z(e_{12})=e^{iz(\kappa_1-\kappa_2)}e_{12}\). Condition (ii) of Theorem 10.3(2) with \(x=e_{12}\), \(y=e_{21}\) reads \(e^{-(\kappa_1-\kappa_2)}p=\omega(e_{22})=1-p\), so \(\kappa_1-\kappa_2=\log\frac p{1-p}\). The remaining matrix units give the same condition or trivial ones, so \(\sigma_t=\operatorname{Ad}\rho^{it}\), the modular group, in agreement with the KMS characterization of the modular group (Section 1). If \(p=1/2\), then \(\omega\) is a trace and (ii) says \(\omega((\sigma_i(x)-x)y)=0\) for all \(y\), so \(\sigma_i(x)=x\) for all \(x\); then \(e^{\kappa_1-\kappa_2}=1\) for the eigenvalues of \(K\), \(K\) is scalar, and \(\sigma\) is trivial.

## Where this leads

Sections 2–9 are the analytic input to the Tomita–Takesaki theorem. The closed involution and its polar decomposition are Theorem 7.6. The analytic properties of a Tomita algebra are Corollary 7.7, together with Proposition 6.1(4) and Theorem 9.1(4)–(5). The essential self-adjointness and Stone arguments are Theorem 8.1, together with the self-adjointness criterion of Section 1. One caution applies there. A bounded operator applied to an entire orbit gives a function that is not itself an orbit, so Theorem 4.2(4) does not bound it as stated; such a function is bounded on horizontal strips by Theorem 5.2(5), and the bounded-strip maximum principle applies to it directly.

Sections 10 and 11 serve the KMS condition, the centralizer of a weight and relative modular theory. The Tomita algebra of a weight, its density, and the fact that its elements are entire for the modular group are treated in the lesson *The modular group and its analytic algebra*. Perturbations of a weight by densities affiliated with its centralizer are treated in *Fixed elements and changes of density*.

## References



- [Lebl CA] J. Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*, version 1.9 (11 July 2026), open textbook under CC BY-SA 4.0 and CC BY-NC-SA 4.0, [www.jirka.org/ca](https://www.jirka.org/ca/). It is the text of the core course *Complex Analysis*.
- [Hiai] F. Hiai, *Concise lectures on selected topics of von Neumann algebras*, 2020, [arXiv:2004.02383](https://arxiv.org/abs/2004.02383); published as *Lectures on Selected Topics in von Neumann Algebras*, EMS Series of Lectures in Mathematics, EMS Press, 2021.
- [Neeb–Ólafsson] K.-H. Neeb and G. Ólafsson, *Antiunitary representations and modular theory*, in: 50th Sophus Lie Seminar, Banach Center Publications 113, 2017, 291–362, [arXiv:1704.01336](https://arxiv.org/abs/1704.01336).
- [Cioranescu–Zsidó] I. Cioranescu and L. Zsidó, Analytic generators for one-parameter groups, *Tôhoku Mathematical Journal* (2) 28 (1976), 327–362. https://www.jstage.jst.go.jp/article/tmj1949/28/3/28_3_327/_article
- [Haag–Hugenholtz–Winnink] R. Haag, N. M. Hugenholtz and M. Winnink, On the equilibrium states in quantum statistical mechanics, *Communications in Mathematical Physics* 5 (1967), 215–236. Free at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-5/issue-3/On-the-equilibrium-states-in-quantum-statistical-mechanics/cmp/1103840050.full
- [Kustermans 1997] J. Kustermans, One-parameter representations on C\*-algebras, preprint (1997), arXiv:funct-an/9707009.
  Free at https://arxiv.org/abs/funct-an/9707009
- [Stone 1930] M. H. Stone, Linear transformations in Hilbert space. III. Operational methods and group theory, *Proceedings
  of the National Academy of Sciences of the U.S.A.* 16 (1930), 172–175. Free at
  https://pmc.ncbi.nlm.nih.gov/articles/PMC1075964/
