# Holomorphy in Banach spaces, Stone's theorem and resolvent convergence

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions (the results used from other lessons, with the proof of Fact 1.10, and the references) are self-checked by the writing AI. Public domain (CC0).*

A self-adjoint operator \(H\) on a Hilbert space is rarely handled directly. One works instead with bounded objects built from it: the unitary operators \(e^{itH}\), the resolvents \((H-\lambda)^{-1}\), and the vectors on which power series in \(H\) converge. This lesson develops the tools that connect these objects. Section 2 decides when a function with values in a Banach space is holomorphic, by testing it against a family of functionals. Sections 3 and 4 study one-parameter groups through their generators and prove Stone's theorem: every strongly continuous unitary group has the form \(e^{itH}\) for exactly one self-adjoint \(H\), and the domain of \(H\) consists of the vectors whose orbit is differentiable at \(t=0\). Section 5 shows that a dense subspace of the domain which the group maps into itself is a core. Section 6 proves Nelson's theorem: a closed symmetric operator with a dense set of analytic vectors is self-adjoint. Sections 7 to 9 treat convergence of unbounded self-adjoint operators in the strong resolvent sense: its equivalent forms in terms of unitary groups and of the functional calculus, a test through cores, what a limit of resolvents can be when it is not a resolvent, and the passage to inverses, logarithms and imaginary powers.

These tools are used throughout the theory of operator algebras. The modular operator of a weight comes with a one-parameter unitary group, and one has to pass between a group and its generator, find domains and cores, and approximate generators by simpler operators. Flows on C\*-algebras, one-parameter groups of automorphisms \(\alpha_t\) with \(t\mapsto\alpha_t(x)\) continuous in norm for each \(x\), raise the same questions, and Sections 3 and 5 are stated for Banach spaces so that they apply there as well.

The lesson assumes basic functional analysis (the Hahn–Banach and uniform boundedness theorems), complex analysis in one variable, Lebesgue integration, and the spectral theorem for self-adjoint operators with its functional calculus, as developed in the lesson Spectral calculus with its domains retained. Section 1 lists exactly what is used. The lesson Analytic elements and strip arguments reaches Stone's theorem, cores and analytic vectors by another route, through analytic continuation of orbits into strips. Here the route is through difference quotients and averages, and Sections 3 to 5 use no complex analysis.

Basic references are [van Neerven] and [Teschl]; [McMullen] is an openly available text for the complex analysis used. Stone's theorem was announced in [Stone 1930]. That weakly holomorphic functions are holomorphic was proved in [Dunford 1938]. Analytic vectors were introduced by Nelson. The link between convergence of resolvents and convergence of the semigroups they generate goes back to [Trotter 1958].

## 1. Conventions and background

### Conventions

*Spaces.* All vector spaces are complex. \(X\) denotes a Banach space, \(X^*\) its dual space and \(B(X)\) the algebra of bounded operators on \(X\). \(\mathcal H\) denotes a Hilbert space of arbitrary dimension. Its inner product \(\langle\xi,\eta\rangle\) is linear in \(\xi\) and conjugate-linear in \(\eta\). For \(z_0\in\mathbb C\) and \(0<r\le\infty\) we write \(\Delta(z_0,r)=\{z\in\mathbb C : |z-z_0|<r\}\).

*Operators.* An operator \(T\) in \(X\) is a linear map from a subspace \(D(T)\) of \(X\) into \(X\). We write \(S\subseteq T\) if \(T\) extends \(S\); an equality \(S=T\) includes equality of domains. \(T\) is closed if its graph is closed in \(X\times X\); then \(D(T)\) is a Banach space for the graph norm \(\|x\|_T=\|x\|+\|Tx\|\). \(T\) is closable if the closure of its graph is the graph of an operator, the closure \(\overline T\). A subspace \(D\subseteq D(T)\) of a closed operator \(T\) is a *core* for \(T\) if it is dense in \(D(T)\) for the graph norm; equivalently, the closure of the restriction \(T|_D\) is \(T\).

*Adjoints.* Let \(T\) be densely defined in \(\mathcal H\). Then \(D(T^*)\) is the set of vectors \(\eta\) for which \(\xi\mapsto\langle T\xi,\eta\rangle\) is bounded on \(D(T)\), and \(T^*\eta\) is the vector with \(\langle T\xi,\eta\rangle=\langle\xi,T^*\eta\rangle\) for all \(\xi\in D(T)\). The following facts come straight from this definition. \(T^*\) is closed, because the defining identities survive limits of pairs \((\eta,T^*\eta)\). If \(S\subseteq T\) and \(S\) is densely defined, then \(T^*\subseteq S^*\). For every scalar \(\lambda\), \(\ker(T^*-\bar\lambda)=\operatorname{ran}(T-\lambda)^\perp\). The operator \(T\) is *symmetric* if \(T\subseteq T^*\), that is, \(\langle T\xi,\eta\rangle=\langle\xi,T\eta\rangle\) for \(\xi,\eta\in D(T)\); then \(\langle T\xi,\xi\rangle\) is real. A closable operator and its closure have the same adjoint, since the identity \(\langle T\xi,\eta\rangle=\langle\xi,T^*\eta\rangle\) passes to limits in the graph. A symmetric operator is closable, because its graph lies in the closed graph of \(T^*\), and its closure is again symmetric, by taking limits in the defining identity. \(T\) is *self-adjoint* if \(T=T^*\), and *essentially self-adjoint* if \(\overline T\) is self-adjoint. If \(K\) is self-adjoint, \(T\) is symmetric and \(K\subseteq T\), then \(T=K\), because \(K\subseteq T\subseteq T^*\subseteq K^*=K\).

*Convergence of operators.* A net \((Y_j)_{j\in J}\) in \(B(\mathcal H)\) is a family indexed by a directed set; sequences are the case \(J=\mathbb N\). The net converges to \(Y\) *strongly* if \(Y_j\xi\to Y\xi\) for every \(\xi\), and *weakly* if \(\langle Y_j\xi,\eta\rangle\to\langle Y\xi,\eta\rangle\) for all \(\xi,\eta\). The index \(j\) is used for nets and \(n\) for sequences; the letter \(i\) always denotes the imaginary unit.

### Results used from other lessons

**Fact 1.1** (norms from functionals). In a normed space \(X\), \(\|x\|=\sup\{|\varphi(x)| : \varphi\in X^*,\ \|\varphi\|\le1\}\) for every \(x\in X\). Proved in Hahn–Banach, Baire and the basic theorems on Banach spaces, Corollary 2.3(2).

**Fact 1.2** (uniform boundedness). A family of bounded linear maps from a Banach space into a normed space that is bounded at each point is bounded in norm. Proved in Hahn–Banach, Baire and the basic theorems on Banach spaces, Theorem 4.2.

**Fact 1.3** (vector-valued integrals). A continuous function \(f\) on a compact interval or on a circle, with values in a Banach space, has a Riemann integral, the norm limit of its Riemann sums, and \(\|\int f\|\le\int\|f\|\). Proved in Analytic kernels for unbounded modular operators, §MA-02; see also the conventions of Cauchy's theorem for cycles and its consequences and, e.g., [van Neerven, Propositions 1.43 and 1.44]. Passing to the limit in Riemann sums shows that the integral is linear in \(f\), additive over adjacent intervals and unchanged by a translation of the variable, and that bounded linear maps pass through it. If \(f\) is continuous on \([0,\infty)\) and \(\|f(t)\|\le m(t)\) with \(m\) integrable, the norm bound shows that the integrals over \([0,R]\) converge in norm as \(R\to\infty\); the limit \(\int_0^\infty f\) has the same properties.

**Fact 1.4** (power series of holomorphic functions). Let \(\varphi\) be a complex function that is holomorphic on a disc \(\Delta(z_0,\rho)\), \(0<\rho\le\infty\). Then \(\varphi(z)=\sum_{n\ge0}c_n(z-z_0)^n\) on the whole disc, where for every \(0<r<\rho\)
\[
c_n=\frac1{2\pi i}\oint_{|\zeta-z_0|=r}\frac{\varphi(\zeta)}{(\zeta-z_0)^{n+1}}\,d\zeta,\qquad |c_n|\le r^{-n}\max_{|\zeta-z_0|=r}|\varphi(\zeta)|.
\]
Proved in Cauchy's theorem for cycles and its consequences, Theorem 3.2. See also [McMullen, Theorem 1.6].

**Fact 1.5** (Runge's theorem). Let \(K\subseteq\mathbb C\) be compact with connected complement, and let \(h\) be holomorphic on an open set containing \(K\). For every \(\varepsilon>0\) there is a polynomial \(p\) with \(|p-h|<\varepsilon\) on \(K\). This is the case \(S=\{\infty\}\) of Runge's theorem on a compact set, [Lebl CA, Theorem 9.2.3](https://www.jirka.org/ca/): the rational functions whose only pole is at \(\infty\) are the polynomials, and \(\{\infty\}\) meets the only component of \((\mathbb C\cup\{\infty\})\setminus K\). [Lebl CA] is an open text, the text of the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50). See also [McMullen, Theorem 1.56].

**Fact 1.6** (calculus on an interval). A real function that is continuous on \([a,b]\) and has derivative zero on \((a,b)\) is constant. Taylor's formula: if \(g\) is real, \(g^{(m-1)}\) is continuous on \([a,b]\) and \(g^{(m)}\) exists on \((a,b)\), then for \(x_0\neq x\) in \([a,b]\) there is \(y\) between them with \(g(x)=\sum_{k<m}g^{(k)}(x_0)(x-x_0)^k/k!+g^{(m)}(y)(x-x_0)^m/m!\). Proved in the core course [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10), whose text is [Lebl RA]: the first statement is the mean value theorem, [Theorem 4.2.4](https://www.jirka.org/ra/html/sec_mvt.html#thm_mvt), applied on \([a,x]\) for \(a<x\le b\), and Taylor's formula is [Theorem 4.3.2](https://www.jirka.org/ra/html/sec_taylor.html#thm_taylor) with \(n=m-1\).

**Fact 1.7** (Lebesgue integration). The monotone convergence theorem and the dominated convergence theorem hold for sequences of measurable functions, and a Riemann integrable function on a compact interval is Lebesgue integrable with the same integral. Proved in Measure and Hilbert space tools for Haar integration: the convergence theorems are Theorems 2.1 and 2.2 there, and Lemma 6.1 there compares the two integrals for continuous functions, the case used in this lesson. For Riemann integrable functions in general see [Fremlin, Measure Theory, Volume 1, 134Kb](https://www1.essex.ac.uk/maths/people/fremlin/cont13.htm) (free; Volumes 1 and 2 of this text are the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)).

**Fact 1.8** (spectral calculus). Let \(H\) be a self-adjoint operator on \(\mathcal H\).

- (a) There is a unique projection-valued measure \(E_H\) on the Borel sets of \(\mathbb R\) with \(H=\int\lambda\,dE_H(\lambda)\). For \(\xi\in\mathcal H\), \(\mu_\xi(B)=\langle E_H(B)\xi,\xi\rangle\) is a positive Borel measure of total mass \(\|\xi\|^2\).
- (b) For a Borel function \(f\colon\mathbb R\to\mathbb C\), the operator \(f(H)=\int f\,dE_H\) is closed and densely defined, \(D(f(H))=\{\xi : \int|f|^2d\mu_\xi<\infty\}\), and \(\|f(H)\xi\|^2=\int|f|^2d\mu_\xi\). Moreover \(f(H)^*=\bar f(H)\), so \(f(H)\) is self-adjoint when \(f\) is real. Changing \(f\) on a Borel set \(N\) with \(E_H(N)=0\) does not change \(f(H)\).
- (c) If \(f\) is bounded, then \(\|f(H)\|\le\sup|f|\) and \(\langle f(H)\xi,\xi\rangle=\int f\,d\mu_\xi\). On bounded Borel functions the map \(f\mapsto f(H)\) is linear and multiplicative, sends \(1\) to the identity, and sends \(\bar f\) to \(f(H)^*\).
- (d) For Borel functions \(f,g\), \(D(f(H)g(H))=D(g(H))\cap D((fg)(H))\), and \(f(H)g(H)\xi=(fg)(H)\xi\) on this domain. Also \(f(H)+g(H)\subseteq(f+g)(H)\).
- (e) If \(f_n\to f\) pointwise and \(|f_n|\le h\) with \(\int h^2d\mu_\xi<\infty\), then \(\xi\) belongs to every \(D(f_n(H))\) and to \(D(f(H))\), and \(f_n(H)\xi\to f(H)\xi\). In particular, if \(|f_n|\le C\) and \(f_n\to f\) pointwise, then \(f_n(H)\to f(H)\) strongly.
- (f) For a real Borel function \(\psi\), \(E_{\psi(H)}(B)=E_H(\psi^{-1}(B))\), and \(f(\psi(H))=(f\circ\psi)(H)\) for every Borel function \(f\).
- (g) \(H\ge0\), that is \(\langle H\xi,\xi\rangle\ge0\) on \(D(H)\), if and only if \(E_H((-\infty,0))=0\). Moreover \(\ker H=E_H(\{0\})\mathcal H\).
- (h) If \((a_k)_{k\in I}\) are real numbers, the operator \((Mx)_k=a_kx_k\) on \(D(M)=\{x\in\ell^2(I) : \sum_k|a_kx_k|^2<\infty\}\) is self-adjoint, and \((f(M)x)_k=f(a_k)x_k\).

These facts are proved in Spectral calculus with its domains retained, §§SK-04–SK-10.

**Fact 1.9** (Stone–Weierstrass). A subalgebra of \(C_0(\mathbb R)\) that is closed under complex conjugation, separates the points of \(\mathbb R\) and has no common zero is dense in \(C_0(\mathbb R)\) for the supremum norm. This is Theorem 10.1 of The Stone–Weierstrass theorem for functions vanishing at infinity.

**Fact 1.10** (functions on the line). For an open set \(D\subseteq\mathbb R\), the smooth functions with compact support in \(D\) are dense in \(L^2(D)\). For \(f\in L^2(\mathbb R)\), \(\|f(\cdot+h)-f\|_2\to0\) as \(h\to0\).

*Proof.* We use two facts from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): Lebesgue measure is translation invariant ([Fremlin, Measure Theory, Volume 1, 134A](https://www1.essex.ac.uk/maths/people/fremlin/cont13.htm)), and the continuous functions with bounded support are dense in \(L^2(\mathbb R)\) ([Fremlin, Volume 2, 244Hb](https://www1.essex.ac.uk/maths/people/fremlin/cont24.htm)). For the second statement, let \(g\) be continuous and zero outside \([-R,R]\). For \(|h|\le1\), \(\|g(\cdot+h)-g\|_2\le(2R+2)^{1/2}\sup_x|g(x+h)-g(x)|\), which tends to \(0\) by uniform continuity. Translation is an isometry of \(L^2(\mathbb R)\), so \(\|f(\cdot+h)-f\|_2\le2\|f-g\|_2+\|g(\cdot+h)-g\|_2\), and density gives the claim.

For the first statement, let \(f\in L^2(D)\), extended by \(0\) to \(\mathbb R\), and \(\varepsilon>0\). The compact sets \(K_n=\{x\in D:|x|\le n,\ \operatorname{dist}(x,\mathbb R\setminus D)\ge1/n\}\) (\(K_n=[-n,n]\) if \(D=\mathbb R\)) increase to \(D\), so dominated convergence gives \(n\) with \(\|f-f1_{K_n}\|_2<\varepsilon\). Choose a continuous \(g\) with bounded support and \(\|g-f1_{K_n}\|_2<\varepsilon\), and put \(\chi(x)=\max(0,1-2n\operatorname{dist}(x,K_n))\). Since \(0\le\chi\le1\) and \(\chi=1\) on \(K_n\), the continuous function \(u=\chi g\) satisfies \(\|u-f1_{K_n}\|_2\le\|g-f1_{K_n}\|_2<\varepsilon\), and it vanishes outside \(\{x:\operatorname{dist}(x,K_n)\le1/(2n)\}\).

Next we smooth \(u\). Let \(\phi(x)=e^{-1/x}\) for \(x>0\) and \(\phi(x)=0\) for \(x\le0\). By induction, \(\phi^{(k)}(x)=p_k(1/x)e^{-1/x}\) for \(x>0\), with polynomials \(p_k\). Since \(s^me^{-s}\to0\) as \(s\to\infty\), both \(\phi^{(k)}(x)\) and \(\phi^{(k)}(x)/x\) tend to \(0\) as \(x\downarrow0\); so, by induction on \(k\), \(\phi^{(k)}\) is differentiable at \(0\) with \(\phi^{(k+1)}(0)=0\), and \(\phi\) is smooth. For \(0<\delta<1/(4n)\) let \(\rho_\delta(x)=c_\delta\,\phi(\delta^2-x^2)\), with \(c_\delta>0\) chosen so that \(\int\rho_\delta=1\). It is smooth, nonnegative and zero for \(|x|\ge\delta\). Put \(u_\delta(x)=\int u(y)\rho_\delta(x-y)\,dy\). Each \(\rho_\delta^{(k+1)}\) is uniformly continuous, so by the mean value theorem the difference quotients of \(\rho_\delta^{(k)}\) converge uniformly to \(\rho_\delta^{(k+1)}\); hence derivatives of every order may be taken under the integral, which runs over the compact support of \(u\), and \(u_\delta\) is smooth. It vanishes outside \(L=\{x:\operatorname{dist}(x,K_n)\le3/(4n)\}\), a compact subset of \(D\) that does not depend on \(\delta\). Finally \(u_\delta(x)-u(x)=\int(u(x-s)-u(x))\rho_\delta(s)\,ds\), so \(|u_\delta(x)-u(x)|\le\sup_{|s|\le\delta}|u(x-s)-u(x)|\), which tends to \(0\) uniformly in \(x\) as \(\delta\to0\). Hence \(\|u_\delta-u\|_2\le|L|^{1/2}\sup|u_\delta-u|\to0\), and \(\|u_\delta-f\|_2<3\varepsilon\) for small \(\delta\). \(\square\)

See also, e.g., [van Neerven, Propositions 2.29 and 2.32].

## 2. Holomorphic functions with values in a Banach space



Throughout this section \(G\subseteq\mathbb C\) is open and \(f\colon G\to X\). For \(z_0\in G\) let \(\rho(z_0)\in(0,\infty]\) be the supremum of the radii \(r\) with \(\Delta(z_0,r)\subseteq G\). So \(\Delta(z_0,\rho(z_0))\) is the largest open disc about \(z_0\) inside \(G\).

**Definition 2.1.**

1. \(f\) is *holomorphic* if for every \(z\in G\) the difference quotients \((f(w)-f(z))/(w-z)\) converge in norm as \(w\to z\). The limit is written \(f'(z)\).
2. A subspace \(F\subseteq X^*\) is *norming* if \(\|x\|=\sup\{|\varphi(x)| : \varphi\in F,\ \|\varphi\|\le1\}\) for every \(x\in X\). By Fact 1.1, \(X^*\) itself is norming.
3. \(f\) is *\(F\)-holomorphic* if \(\varphi\circ f\) is holomorphic for every \(\varphi\in F\).
4. \(f\) is *locally bounded* if each point of \(G\) has a neighbourhood on which \(\|f\|\) is bounded; equivalently, \(\|f\|\) is bounded on every compact subset of \(G\).

**Theorem 2.2.** For \(f\colon G\to X\) the following are equivalent.

- (a) \(f\) is holomorphic.
- (b) Every \(z_0\in G\) has a disc \(\Delta(z_0,\delta)\subseteq G\) on which \(f(z)=\sum_{n\ge0}(z-z_0)^na_n\), with \(a_n\in X\) and the series convergent in norm.
- (c) \(f\) is \(F\)-holomorphic for some norm-closed norming subspace \(F\subseteq X^*\).
- (d) \(f\) is locally bounded and \(F\)-holomorphic for some norming subspace \(F\subseteq X^*\).

When they hold, \(f\) has norm derivatives of all orders, and for every \(z_0\in G\):

- (e) the series in (b) converges in norm on the whole disc \(\Delta(z_0,\rho(z_0))\), and \(a_n=f^{(n)}(z_0)/n!\);
- (f) for every \(0<r<\rho(z_0)\),
\[
a_n=\frac1{2\pi i}\oint_{|\zeta-z_0|=r}\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}\,d\zeta,\qquad \|a_n\|\le r^{-n}\max_{|\zeta-z_0|=r}\|f(\zeta)\|.
\tag{2.1}
\]

*Reference:* [Dunford 1938] for the case \(F=X^*\).

**Proof.** *(a) implies (c).* Take \(F=X^*\). It is closed, and it is norming by Fact 1.1. For \(\varphi\in X^*\), the function \(\varphi\circ f\) has derivative \(\varphi(f'(z))\) at \(z\), because \(\varphi\) is linear and continuous.

*(c) implies (d).* Let \(K\subseteq G\) be compact. For \(\varphi\in F\), the function \(\varphi\circ f\) is holomorphic, hence continuous, hence bounded on \(K\). For \(z\in K\) define \(\Lambda_z\colon F\to\mathbb C\) by \(\Lambda_z(\varphi)=\varphi(f(z))\). Since \(F\) is norming, \(\Lambda_z\) is bounded and \(\|\Lambda_z\|=\|f(z)\|\). The family \((\Lambda_z)_{z\in K}\) is bounded at each point of \(F\), and \(F\) is a Banach space because it is closed in \(X^*\). By Fact 1.2, \(\sup_{z\in K}\|f(z)\|<\infty\).

*(d) implies (b), (e) and (f).* Fix \(z_0\in G\) and write \(\rho=\rho(z_0)\). For \(0<r<\rho\) the circle \(|\zeta-z_0|=r\) is a compact subset of \(G\), so \(M(r)=\sup_{|\zeta-z_0|=r}\|f(\zeta)\|\) is finite.

Step 1: the coefficients as functionals. Let \(\varphi\in F\). By Fact 1.4, \(\varphi(f(z))=\sum_nc_n(\varphi)(z-z_0)^n\) on \(\Delta(z_0,\rho)\), where for every \(0<r<\rho\)
\[
c_n(\varphi)=\frac1{2\pi i}\oint_{|\zeta-z_0|=r}\frac{\varphi(f(\zeta))}{(\zeta-z_0)^{n+1}}\,d\zeta,\qquad |c_n(\varphi)|\le r^{-n}M(r)\,\|\varphi\|.
\]
The integral is linear in \(\varphi\). So \(c_n\) belongs to the dual space \(F'\) of the normed space \(F\), and \(\|c_n\|\le r^{-n}M(r)\). The dual of a normed space is a Banach space whether or not \(F\) is closed.

Step 2: continuity. Define \(\iota\colon X\to F'\) by \(\iota(x)(\varphi)=\varphi(x)\). Since \(F\) is norming, \(\iota\) is a linear isometry. Let \(0<s<r<\rho\). For \(|z-z_0|\le s\) we have \(\sum_n\|c_n\|\,|z-z_0|^n\le M(r)\sum_n(s/r)^n<\infty\). So \(g(z)=\sum_nc_n(z-z_0)^n\) converges in \(F'\), uniformly on the closed disc of radius \(s\). Evaluating at \(\varphi\in F\) gives \(g(z)(\varphi)=\varphi(f(z))\), so \(g(z)=\iota(f(z))\). As a uniform limit of polynomials, \(g\) is continuous. Since \(\iota\) is an isometry, \(f\) is norm continuous on \(\Delta(z_0,\rho)\).

Step 3: the coefficients lie in \(X\). Fix \(n\) and \(0<r<\rho\). By Step 2 the integrand in (2.1) is continuous on the circle, so the integral \(a_n\) exists in \(X\) (Fact 1.3). Every \(\varphi\in F\) passes through the integral, so \(\varphi(a_n)=c_n(\varphi)\), that is, \(\iota(a_n)=c_n\). Hence \(a_n\) does not depend on \(r\), and \(\|a_n\|=\|c_n\|\le r^{-n}M(r)\), which is the bound in (2.1). In particular \(\sum_n\|a_n\|\,|z-z_0|^n<\infty\) for every \(z\in\Delta(z_0,\rho)\), and
\[
\iota\Big(\sum_na_n(z-z_0)^n\Big)=\sum_nc_n(z-z_0)^n=\iota(f(z)).
\]
Since \(\iota\) is injective, \(f(z)=\sum_na_n(z-z_0)^n\) on \(\Delta(z_0,\rho)\). This proves (b) with \(\delta=\rho\), the convergence statement in (e), and (f).

*(b) implies (a), and the formula for \(a_n\).* We show: if \(\sum_na_n(z-z_0)^n\) converges in norm on \(\Delta(z_0,\delta)\), then its sum \(p\) is holomorphic there, and \(p'\) is the sum of the derived series \(\sum_{n\ge1}na_n(z-z_0)^{n-1}\), which converges on the same disc. Let \(0<s<s_1<\delta\). The terms of the series at a point with \(|z-z_0|=s_1\) tend to zero, so \(\|a_n\|\le Cs_1^{-n}\) for some constant \(C\). Let \(z\neq w\) lie in the closed disc of radius \(s\), and put \(u=w-z_0\), \(v=z-z_0\). For \(n\ge1\),
\[
\frac{u^n-v^n}{u-v}-nv^{n-1}=\sum_{k=0}^{n-1}(u^k-v^k)v^{n-1-k}.
\]
Since \(|u^k-v^k|\le ks^{k-1}|u-v|\), the right side has modulus at most \(n^2s^{n-2}|u-v|\), and it vanishes for \(n=1\). Therefore
\[
\Big\|\frac{p(w)-p(z)}{w-z}-\sum_{n\ge1}na_nv^{n-1}\Big\|\le|w-z|\;C\sum_{n\ge2}n^2s^{n-2}s_1^{-n},
\]
and the last sum is finite. Letting \(w\to z\) proves the claim. The derived series is again a power series that converges on \(\Delta(z_0,\delta)\), so \(p\) has derivatives of all orders there. Evaluating the \(k\) times derived series at \(z_0\) gives \(p^{(k)}(z_0)=k!\,a_k\).

We have shown that (a) implies (c), (c) implies (d), (d) implies (b) and (b) implies (a), together with (e) and (f). \(\square\)

**Remark 2.3.**

1. In (c) the closedness of \(F\) serves only to produce local boundedness through Fact 1.2; the step from (d) to (b) does not use it. Example 2.5 shows that local boundedness cannot be dropped from (d).
2. Some useful norming subspaces. If \(X=Y^*\) is the dual of a Banach space \(Y\), the canonical image of \(Y\) in \(X^*\) is closed and norming. For a von Neumann algebra \(N\) with predual \(N_*\), this gives: a function \(f\colon G\to N\) is holomorphic in norm as soon as \(\omega\circ f\) is holomorphic for every normal functional \(\omega\). For \(X=B(\mathcal H)\), the functionals \(x\mapsto\langle x\xi,\eta\rangle\) span a norming subspace, so a locally bounded operator-valued function whose matrix coefficients \(\langle f(z)\xi,\eta\rangle\) are holomorphic is holomorphic in norm. For \(X=\mathcal H\) and a dense subspace \(D\subseteq\mathcal H\), the functionals \(\langle\cdot,\eta\rangle\) with \(\eta\in D\) span a norming subspace; this case is treated directly in the lesson *Analytic kernels for unbounded modular operators*.

**Example 2.4** (the disc in (e) cannot be enlarged). Let \(X=\ell^\infty\), the bounded sequences \((x_k)_{k\ge0}\), and \(f(z)=(z^k)_{k\ge0}\) on the unit disc \(\Delta(0,1)\). The coordinate functionals \(x\mapsto x_k\) span a norming subspace \(F\) of \(X^*\), because \(\|x\|_\infty=\sup_k|x_k|\). Each coordinate \(z\mapsto z^k\) is holomorphic, and \(\|f(z)\|_\infty=1\). By Theorem 2.2(d), \(f\) is holomorphic. By Steps 1 and 3 of the proof, \(\varphi(a_n)\) is the \(n\)-th Taylor coefficient of \(\varphi\circ f\); for the coordinate functionals this gives \(a_n=e_n\), the \(n\)-th unit sequence. Indeed, for \(|z|<1\),
\[
\Big\|f(z)-\sum_{k<m}z^ke_k\Big\|_\infty=\sup_{k\ge m}|z|^k=|z|^m\to0.
\]
When \(|z|\ge1\), the terms \(z^ke_k\) have norm \(|z|^k\ge1\) and do not tend to zero. So the series converges exactly on \(\Delta(0,1)=\Delta(0,\rho(0))\).

**Example 2.5** (local boundedness cannot be omitted from (d)). We construct polynomials \(p_1,p_2,\ldots\) such that \(\sum_n|p_n(z)|^2<\infty\) for every \(z\in\mathbb C\), while \(\sum_n|p_n(z)|^2\) is unbounded on every neighbourhood of \(0\). Then \(f(z)=(p_n(z))_{n\ge1}\) maps \(\mathbb C\) into \(\ell^2\). Every coordinate \(\langle f(z),e_n\rangle=p_n(z)\) is a polynomial, and the coordinate functionals span a norming subspace \(F\) of \((\ell^2)^*\), since the finitely supported vectors are dense in \(\ell^2\). So \(f\) is \(F\)-holomorphic for a norming \(F\). But \(f\) is not bounded near \(0\), hence not continuous, hence not holomorphic.

Let \(\mathbb R_{\ge0}=[0,\infty)\), viewed as a subset of \(\mathbb C\). For \(n\ge1\) put
\[
L_n=\{z : |z|\le n,\ \operatorname{dist}(z,\mathbb R_{\ge0})\ge 1/n\}\cup[1/n,n]\cup\{0\},\qquad w_n=\frac1{2n},\qquad K_n=L_n\cup\{w_n\}.
\]
The set \(K_n\) is compact. Its complement is connected. Indeed, a point \(z\notin K_n\) with \(|z|\le n\) satisfies \(\operatorname{dist}(z,\mathbb R_{\ge0})<1/n\). If \(z\) is real, it lies in \((-1/n,1/n)\); move it vertically by less than \(1/n-|z|\). Then move it horizontally to the right. Along this path the distance to \(\mathbb R_{\ge0}\) stays below \(1/n\), and after the first move the path avoids the real axis; so it stays outside \(K_n\) until it reaches the connected set \(\{|z|>n\}\).

The point \(w_n\) has distance at least \(1/(2n)\) from \(L_n\): points of the first set in \(L_n\) have distance at least \(1/n\) from \(\mathbb R_{\ge0}\), which contains \(w_n\), and \(w_n\) has distance \(1/(2n)\) from \([1/n,n]\cup\{0\}\). Let \(h_n=0\) on the set of points at distance less than \(1/(8n)\) from \(L_n\), and \(h_n=n\) on the disc \(\Delta(w_n,1/(8n))\). These two open sets are disjoint, so \(h_n\) is holomorphic on their union, which contains \(K_n\). By Fact 1.5 there is a polynomial \(p_n\) with \(|p_n-h_n|<2^{-n}\) on \(K_n\). Thus \(|p_n|<2^{-n}\) on \(L_n\), and \(|p_n(w_n)|>n-1\).

Every \(z\in\mathbb C\) lies in \(L_n\) for all large \(n\). If \(z\notin\mathbb R_{\ge0}\), then \(\operatorname{dist}(z,\mathbb R_{\ge0})>0\), so \(z\) lies in the first set of \(L_n\) as soon as \(n\ge|z|\) and \(1/n\le\operatorname{dist}(z,\mathbb R_{\ge0})\). If \(z>0\), then \(z\in[1/n,n]\) for large \(n\). And \(0\in L_n\) for all \(n\). Hence \(\sum_n|p_n(z)|^2<\infty\) for every \(z\). On the other hand \(\|f(w_n)\|\ge|p_n(w_n)|>n-1\), and \(w_n\to0\).

**Example 2.6** (resolvents). Let \(H\) be self-adjoint on \(\mathcal H\). For \(\lambda\in\mathbb C\setminus\mathbb R\) let \(r_\lambda(x)=(x-\lambda)^{-1}\) and \(R(\lambda)=r_\lambda(H)\); Lemma 7.1 shows that \(R(\lambda)=(H-\lambda)^{-1}\). Since \(|r_\lambda|\le1/|\operatorname{Im}\lambda|\) on \(\mathbb R\), Fact 1.8(c) gives \(\|R(\lambda)\|\le1/|\operatorname{Im}\lambda|\). The scalar identity \(r_\lambda-r_\mu=(\lambda-\mu)r_\lambda r_\mu\) and Fact 1.8(c) give the *resolvent identity*
\[
R(\lambda)-R(\mu)=(\lambda-\mu)R(\lambda)R(\mu).
\tag{2.2}
\]
Hence \(\|R(\lambda)-R(\mu)\|\le|\lambda-\mu|/(|\operatorname{Im}\lambda|\,|\operatorname{Im}\mu|)\), so \(R\) is norm continuous, and \((R(\lambda)-R(\mu))/(\lambda-\mu)=R(\lambda)R(\mu)\to R(\mu)^2\) as \(\lambda\to\mu\). So \(R\colon\mathbb C\setminus\mathbb R\to B(\mathcal H)\) is holomorphic, with \(R'=R^2\). The operators \(R(\lambda)\) commute with each other, and the product rule, which holds for norm-differentiable operator-valued functions with the usual proof, gives \((R^k)'=kR^{k+1}\); so \(R^{(k)}=k!\,R^{k+1}\). The largest disc about \(\mu\) inside \(\mathbb C\setminus\mathbb R\) has radius \(|\operatorname{Im}\mu|\), so Theorem 2.2(e) gives
\[
R(\lambda)=\sum_{k\ge0}(\lambda-\mu)^kR(\mu)^{k+1}\qquad(|\lambda-\mu|<|\operatorname{Im}\mu|),
\tag{2.3}
\]
where the \(k\)-th term has norm at most \(|\lambda-\mu|^k/|\operatorname{Im}\mu|^{k+1}\). The same formula also follows from (2.2) and the geometric series for \((1-(\lambda-\mu)R(\mu))^{-1}\).

## 3. Strongly continuous semigroups and their generators

A reference for this section is [van Neerven, Section 13.1].

**Lemma 3.1** (calculus for vector-valued functions). Let \(I\subseteq\mathbb R\) be an interval.

1. If \(f\colon I\to X\) is continuous and \(c\in I\), then \(t\mapsto\int_c^tf(s)\,ds\) is differentiable on \(I\), with derivative \(f(t)\); at an endpoint of \(I\) the derivative is one-sided.
2. If \(g\colon[a,b]\to X\) is continuous and has derivative zero on \((a,b)\), then \(g\) is constant.
3. If \(g\colon[a,b]\to X\) has a continuous derivative on \([a,b]\), then \(g(b)-g(a)=\int_a^bg'(s)\,ds\).
4. Let \(t\mapsto B_t\in B(X)\) be strongly continuous on \(I\) with \(\sup_{t\in I}\|B_t\|<\infty\). Let \(u\colon I\to X\) be differentiable at \(t_0\in I\), and suppose that \(t\mapsto B_tu(t_0)\) is differentiable at \(t_0\), with derivative \(y\). Then \(t\mapsto B_tu(t)\) is differentiable at \(t_0\), with derivative \(B_{t_0}u'(t_0)+y\).

**Proof.** (1) By Fact 1.3, \(\|h^{-1}\int_t^{t+h}f(s)\,ds-f(t)\|\le\sup_{|s-t|\le|h|}\|f(s)-f(t)\|\), which tends to \(0\) as \(h\to0\).

(2) For \(\varphi\in X^*\), the real and imaginary parts of \(\varphi\circ g\) are real functions with derivative zero, hence constant by Fact 1.6. So \(\varphi(g(b)-g(a))=0\) for every \(\varphi\), and \(g(b)=g(a)\) by Fact 1.1. The same applies to every subinterval.

(3) By (1), the function \(t\mapsto g(t)-g(a)-\int_a^tg'(s)\,ds\) has derivative zero; apply (2).

(4) Put \(v_t=(u(t)-u(t_0))/(t-t_0)\). Then
\[
\frac{B_tu(t)-B_{t_0}u(t_0)}{t-t_0}=B_tv_t+\frac{B_tu(t_0)-B_{t_0}u(t_0)}{t-t_0}.
\]
The second term tends to \(y\). For the first, \(B_tv_t-B_{t_0}u'(t_0)=B_t(v_t-u'(t_0))+(B_t-B_{t_0})u'(t_0)\), which tends to \(0\) by the uniform bound on \(\|B_t\|\) and strong continuity. \(\square\)

**Definition 3.2.** A *semigroup* on \(X\) is a family \((T_t)_{t\ge0}\) in \(B(X)\) with \(T_0=1\) and \(T_{s+t}=T_sT_t\) for \(s,t\ge0\). It is *strongly continuous* if \(T_tx\to x\) as \(t\downarrow0\), for every \(x\in X\). Its *generator* is the operator \(A\) with
\[
D(A)=\Big\{x\in X : \lim_{t\downarrow0}t^{-1}(T_tx-x)\text{ exists}\Big\},\qquad Ax=\lim_{t\downarrow0}t^{-1}(T_tx-x).
\]
A *group* on \(X\) is a family \((T_t)_{t\in\mathbb R}\) in \(B(X)\) with \(T_0=1\) and \(T_{s+t}=T_sT_t\) for all real \(s,t\). It is strongly continuous if \(T_tx\to x\) as \(t\to0\), and its generator is defined as above with the two-sided limit \(t\to0\). For a semigroup and \(t>0\) we put
\[
J_tx=\int_0^tT_sx\,ds .
\]

**Proposition 3.3.** Let \((T_t)_{t\ge0}\) be a strongly continuous semigroup with generator \(A\).

1. For every \(\tau>0\), \(\sup_{0\le t\le\tau}\|T_t\|<\infty\), and \(t\mapsto T_tx\) is continuous on \([0,\infty)\) for every \(x\).
2. For \(x\in X\) and \(t>0\), \(J_tx\in D(A)\) and \(AJ_tx=T_tx-x\).
3. \(t^{-1}J_tx\to x\) as \(t\downarrow0\), for every \(x\). In particular \(D(A)\) is dense in \(X\).
4. If \(x\in D(A)\), then \(T_tx\in D(A)\) and \(AT_tx=T_tAx\) for every \(t\ge0\). The function \(t\mapsto T_tx\) has the continuous derivative \(t\mapsto T_tAx\) on \([0,\infty)\), and \(T_tx-x=J_tAx\).
5. \(A\) is closed.

**Proof.** (1) First, there are \(\delta>0\) and \(C\ge1\) with \(\|T_t\|\le C\) for \(0\le t\le\delta\). Otherwise there are \(t_k\downarrow0\) with \(\|T_{t_k}\|\to\infty\). By Fact 1.2 some \(x\) then has \(\sup_k\|T_{t_k}x\|=\infty\), which contradicts \(T_{t_k}x\to x\). For \(0\le t\le\tau\) write \(t=m\delta+r\) with an integer \(0\le m\le\tau/\delta\) and \(0\le r<\delta\). Then \(\|T_t\|=\|T_\delta^mT_r\|\le C^{m+1}\le C^{\tau/\delta+1}\). For continuity, let \(t\ge0\). For \(h>0\), \(T_{t+h}x-T_tx=T_t(T_hx-x)\to0\) as \(h\downarrow0\). For \(0<h\le t\), \(T_{t-h}x-T_tx=T_{t-h}(x-T_hx)\), whose norm is at most \(\sup_{0\le s\le t}\|T_s\|\,\|x-T_hx\|\to0\).

(2) By (1) the integrand is continuous. For \(h>0\), \(T_hJ_tx=\int_0^tT_{s+h}x\,ds=\int_h^{t+h}T_sx\,ds\), since \(T_h\) passes through the integral. So
\[
h^{-1}(T_h-1)J_tx=h^{-1}\int_t^{t+h}T_sx\,ds-h^{-1}\int_0^hT_sx\,ds\longrightarrow T_tx-x\qquad(h\downarrow0),
\]
by Lemma 3.1(1).

(3) Lemma 3.1(1) at \(t=0\) gives \(t^{-1}J_tx\to T_0x=x\), and \(J_tx\in D(A)\) by (2).

(4) For \(h>0\), \(h^{-1}(T_h-1)T_tx=T_t\,h^{-1}(T_hx-x)\to T_tAx\). Hence \(T_tx\in D(A)\), \(AT_tx=T_tAx\), and the right derivative of \(s\mapsto T_sx\) at \(t\) is \(T_tAx\). For \(0<h\le t\),
\[
h^{-1}(T_tx-T_{t-h}x)-T_tAx=T_{t-h}\big(h^{-1}(T_hx-x)-Ax\big)+(T_{t-h}Ax-T_tAx),
\]
which tends to \(0\) by the bound in (1) and the continuity of \(s\mapsto T_sAx\). So \(s\mapsto T_sx\) is differentiable with the continuous derivative \(s\mapsto T_sAx\), and Lemma 3.1(3) gives \(T_tx-x=\int_0^tT_sAx\,ds=J_tAx\).

(5) Let \(x_k\in D(A)\) with \(x_k\to x\) and \(Ax_k\to y\). By (4), \(T_tx_k-x_k=J_tAx_k\), and \(\|J_tAx_k-J_ty\|\le t\sup_{0\le s\le t}\|T_s\|\,\|Ax_k-y\|\to0\). So \(T_tx-x=J_ty\) for every \(t>0\). By (3), \(t^{-1}(T_tx-x)=t^{-1}J_ty\to y\) as \(t\downarrow0\). Thus \(x\in D(A)\) and \(Ax=y\). \(\square\)

**Proposition 3.4** (the resolvent as a Laplace transform). Let \((T_t)_{t\ge0}\) be a strongly continuous semigroup with generator \(A\) and \(M:=\sup_{t\ge0}\|T_t\|<\infty\). For every \(\mu\in\mathbb C\) with \(\operatorname{Re}\mu>0\), the operator \(\mu-A\) maps \(D(A)\) bijectively onto \(X\), and
\[
(\mu-A)^{-1}x=\int_0^\infty e^{-\mu t}T_tx\,dt,\qquad \|(\mu-A)^{-1}\|\le\frac M{\operatorname{Re}\mu}.
\tag{3.1}
\]

**Proof.** The integrand is continuous, with norm at most \(Me^{-(\operatorname{Re}\mu)t}\|x\|\). So the integral \(Lx\) exists by Fact 1.3, \(L\) is linear, and \(\|L\|\le M/\operatorname{Re}\mu\). For \(h>0\), \(T_hLx=\int_0^\infty e^{-\mu t}T_{t+h}x\,dt=e^{\mu h}\int_h^\infty e^{-\mu s}T_sx\,ds\). Hence
\[
h^{-1}(T_h-1)Lx=\frac{e^{\mu h}-1}{h}\int_h^\infty e^{-\mu s}T_sx\,ds-\frac1h\int_0^he^{-\mu s}T_sx\,ds\longrightarrow\mu Lx-x\qquad(h\downarrow0).
\]
So \(Lx\in D(A)\) and \((\mu-A)Lx=x\). Now let \(x\in D(A)\). By Proposition 3.3(4) and Lemma 3.1(4) (with \(B_s=e^{-\mu s}\cdot1\)), the function \(s\mapsto e^{-\mu s}T_sx\) has the continuous derivative \(s\mapsto e^{-\mu s}T_s(Ax-\mu x)\). Lemma 3.1(3) on \([0,R]\) gives \(e^{-\mu R}T_Rx-x=\int_0^Re^{-\mu s}T_s(A-\mu)x\,ds\). As \(R\to\infty\) the left side tends to \(-x\), so \(L(\mu-A)x=x\). Hence \(\mu-A\) is injective on \(D(A)\) and onto \(X\), with inverse \(L\). \(\square\)

**Proposition 3.5** (uniqueness). Two strongly continuous semigroups with the same generator are equal.

**Proof.** Let \((S_t)_{t\ge0}\) and \((T_t)_{t\ge0}\) both have generator \(A\). Fix \(x\in D(A)\) and \(t>0\), and put \(w(s)=T_{t-s}S_sx\) for \(0\le s\le t\). The function \(w\) is continuous, because \(\|T_{t-s'}S_{s'}x-T_{t-s}S_sx\|\le\|T_{t-s'}\|\,\|S_{s'}x-S_sx\|+\|(T_{t-s'}-T_{t-s})S_sx\|\) and Proposition 3.3(1) applies to both semigroups. By Proposition 3.3(4) for \(S\), the function \(u(s)=S_sx\) is differentiable with derivative \(AS_sx\), and \(S_sx\in D(A)\). By Proposition 3.3(4) for \(T\), for \(y\in D(A)\) the function \(s\mapsto T_{t-s}y\) is differentiable on \((0,t)\) with derivative \(-T_{t-s}Ay\). Lemma 3.1(4), with \(B_s=T_{t-s}\), gives \(w'(s)=T_{t-s}AS_sx-T_{t-s}AS_sx=0\) for \(0<s<t\). By Lemma 3.1(2), \(T_tx=w(0)=w(t)=S_tx\). The bounded operators \(T_t\) and \(S_t\) agree on the dense subspace \(D(A)\), so they are equal. \(\square\)

**Proposition 3.6** (groups). Let \((T_t)_{t\in\mathbb R}\) be a strongly continuous group with generator \(A\).

1. \((T_t)_{t\ge0}\) and \((T_{-t})_{t\ge0}\) are strongly continuous semigroups, with generators \(A\) and \(-A\).
2. For every \(t\in\mathbb R\), \(T_tD(A)=D(A)\) and \(AT_tx=T_tAx\) for \(x\in D(A)\); and \(t\mapsto T_tx\) has the continuous derivative \(t\mapsto T_tAx\) on \(\mathbb R\).
3. Two strongly continuous groups with the same generator are equal.
4. If \(M:=\sup_{t\in\mathbb R}\|T_t\|<\infty\), then \(\mu-A\) maps \(D(A)\) bijectively onto \(X\) for every \(\mu\) with \(\operatorname{Re}\mu\neq0\). The inverse is given by (3.1) when \(\operatorname{Re}\mu>0\), and by \((\mu-A)^{-1}x=-\int_0^\infty e^{\mu t}T_{-t}x\,dt\) when \(\operatorname{Re}\mu<0\).

**Proof.** (1) Both families are semigroups, and they are strongly continuous because \(T_tx\to x\) as \(t\to0\) from either side. Let \(A_+\) and \(A_-\) be their generators. If \(x\in D(A)\), then both one-sided limits exist, and \(A_+x=Ax\), \(A_-x=-Ax\). Conversely, let \(x\in D(A_+)\). For \(h\downarrow0\),
\[
\frac{T_{-h}x-x}{-h}=T_{-h}\,\frac{T_hx-x}{h}\longrightarrow A_+x,
\]
because \(\|T_{-h}\|\) is bounded for \(0\le h\le1\) (Proposition 3.3(1) for \((T_{-t})_{t\ge0}\)) and \(T_{-h}A_+x\to A_+x\). So the two-sided limit exists, \(x\in D(A)\), and \(A_+=A\). The same argument applied to the group \((T_{-t})_{t\in\mathbb R}\), whose generator is \(-A\), gives \(A_-=-A\).

(2) For \(t\ge0\) this is Proposition 3.3(4) for \((T_t)_{t\ge0}\). For \(t\le0\) it is Proposition 3.3(4) for \((T_{-t})_{t\ge0}\), whose generator is \(-A\). Applying the inclusion \(T_tD(A)\subseteq D(A)\) to \(-t\) gives equality. For \(x\in D(A)\) and fixed \(t\), \(h^{-1}(T_{t+h}x-T_tx)=T_t\,h^{-1}(T_hx-x)\to T_tAx\) as \(h\to0\) from either side.

(3) By (1), the forward halves of the two groups have the same generator \(A\), and the backward halves the same generator \(-A\). Apply Proposition 3.5 to each.

(4) For \(\operatorname{Re}\mu>0\) apply Proposition 3.4 to \((T_t)_{t\ge0}\). For \(\operatorname{Re}\mu<0\) apply it to \((T_{-t})_{t\ge0}\), whose generator is \(-A\), at the point \(-\mu\): the operator \(-\mu+A\) is a bijection with inverse \(x\mapsto\int_0^\infty e^{\mu t}T_{-t}x\,dt\), and \(\mu-A=-(-\mu+A)\). \(\square\)

## 4. Stone's theorem

A reference for this section is [van Neerven, Section 13.5].

A *unitary group* on \(\mathcal H\) is a group \((U_t)_{t\in\mathbb R}\) of unitary operators, in the sense of Definition 3.2.

**Lemma 4.1.** For a unitary group \((U_t)\) the following are equivalent.

1. \(\langle U_t\xi,\xi\rangle\to\|\xi\|^2\) as \(t\to0\), for every \(\xi\).
2. \((U_t)\) is strongly continuous.
3. \(t\mapsto U_t\xi\) is continuous on \(\mathbb R\), for every \(\xi\).

**Proof.** Since \(\|U_t\xi\|=\|\xi\|\), we have \(\|U_t\xi-\xi\|^2=2\|\xi\|^2-2\operatorname{Re}\langle U_t\xi,\xi\rangle\); so (1) implies (2). The identity \(\|U_t\xi-U_s\xi\|=\|U_{t-s}\xi-\xi\|\) shows that (2) implies (3). Clearly (3) implies (1). \(\square\)

**Theorem 4.2.** Let \(H\) be self-adjoint, and let \(U_t=e^{itH}\) be the function \(\lambda\mapsto e^{it\lambda}\) of \(H\).

1. \((U_t)_{t\in\mathbb R}\) is a strongly continuous unitary group. For every \(t\), \(U_tD(H)=D(H)\), and \(HU_t\xi=U_tH\xi\) for \(\xi\in D(H)\).
2. For \(\xi\in\mathcal H\) the following are equivalent:
   - (i) \(\xi\in D(H)\);
   - (ii) \(t^{-1}(U_t\xi-\xi)\) converges in norm as \(t\to0\);
   - (iii) there are real \(t_k\to0\), \(t_k\neq0\), and a vector \(\zeta\) such that \(t_k^{-1}(U_{t_k}\xi-\xi)\to\zeta\) weakly;
   - (iv) \(\liminf_{t\to0}\|t^{-1}(U_t\xi-\xi)\|<\infty\).

   When they hold, the limit in (ii) is \(iH\xi\). In particular the generator of \((U_t)\) is \(iH\).

**Proof.** (1) Since \(|e^{it\lambda}|=1\) and the bounded functional calculus is a unital \(*\)-homomorphism (Fact 1.8(c)), each \(U_t\) is unitary, \(U_0=1\) and \(U_sU_t=U_{s+t}\). By Fact 1.8(b), \(\|U_t\xi-\xi\|^2=\int|e^{it\lambda}-1|^2\,d\mu_\xi(\lambda)\). The integrand is at most \(4\) and tends to \(0\) as \(t\to0\), so along every sequence \(t_n\to0\) the integral tends to \(0\) by dominated convergence (Fact 1.7). For the domains, apply Fact 1.8(d) to the functions \(\lambda\) and \(e^{it\lambda}\). The product \(HU_t\) has domain \(D(U_t)\cap D((\lambda e^{it\lambda})(H))=D(H)\), because \(|\lambda e^{it\lambda}|=|\lambda|\). So \(U_t\xi\in D(H)\) exactly when \(\xi\in D(H)\), that is, \(U_tD(H)=D(H)\). Also \(HU_t\xi=(\lambda e^{it\lambda})(H)\xi\), and \(U_tH\xi=(e^{it\lambda}\lambda)(H)\xi\) for \(\xi\in D(H)\) by the same fact. These are equal.

(2) *(i) implies (ii).* Let \(\xi\in D(H)\) and \(g_t(\lambda)=t^{-1}(e^{it\lambda}-1)-i\lambda\). By Fact 1.8(d), \(t^{-1}(U_t\xi-\xi)-iH\xi=g_t(H)\xi\). From \(|e^{i\theta}-1|\le|\theta|\) we get \(|g_t(\lambda)|\le2|\lambda|\), and \(\int\lambda^2d\mu_\xi<\infty\) because \(\xi\in D(H)\). Also \(g_t(\lambda)\to0\) as \(t\to0\). By Fact 1.8(e), \(g_{t_k}(H)\xi\to0\) along every sequence \(t_k\to0\), so \(t^{-1}(U_t\xi-\xi)\to iH\xi\).

*(ii) implies (iii)* is clear.

*(iii) implies (iv).* A weakly convergent sequence is bounded in norm, by Fact 1.2 applied to the functionals \(\eta\mapsto\langle\eta,v_k\rangle\), where \(v_k=t_k^{-1}(U_{t_k}\xi-\xi)\).

*(iv) implies (i).* Choose \(t_k\to0\), \(t_k\neq0\), with \(\|t_k^{-1}(U_{t_k}\xi-\xi)\|\le C\). Let \(N>0\). By Fact 1.8(b),
\[
\int_{[-N,N]}\big|t_k^{-1}(e^{it_k\lambda}-1)\big|^2\,d\mu_\xi(\lambda)\le C^2 .
\]
From \(|e^{i\theta}-1-i\theta|\le\theta^2/2\) we get \(|t^{-1}(e^{it\lambda}-1)-i\lambda|\le|t|N^2/2\) for \(|\lambda|\le N\). So the integrand converges to \(\lambda^2\) uniformly on \([-N,N]\), and \(\int_{[-N,N]}\lambda^2d\mu_\xi\le C^2\). By monotone convergence (Fact 1.7), \(\int\lambda^2d\mu_\xi\le C^2\), so \(\xi\in D(H)\).

The last assertion follows from (i) implies (ii). \(\square\)

**Theorem 4.3** (Stone's theorem). Let \((U_t)_{t\in\mathbb R}\) be a unitary group on \(\mathcal H\) with \(\langle U_t\xi,\xi\rangle\to\|\xi\|^2\) as \(t\to0\), for every \(\xi\). Let \(A\) be its generator. Then \(H:=-iA\) is self-adjoint, and \(U_t=e^{itH}\) for every \(t\). If \(K\) is self-adjoint and \(U_t=e^{itK}\) for every \(t\), then \(K=H\).

*Reference:* [Stone 1930].

**Proof.** By Lemma 4.1 the group is strongly continuous, so Section 3 applies. By Proposition 3.3(3),(5) and Proposition 3.6(1), \(A\) is densely defined and closed, and so is \(H\).

*\(H\) is symmetric.* Let \(\xi,\eta\in D(H)=D(A)\). Since \(U_t^*=U_{-t}\),
\[
\langle A\xi,\eta\rangle=\lim_{t\to0}\big\langle t^{-1}(U_t\xi-\xi),\eta\big\rangle=\lim_{t\to0}\big\langle\xi,t^{-1}(U_{-t}\eta-\eta)\big\rangle=-\langle\xi,A\eta\rangle,
\]
because \((-t)^{-1}(U_{-t}\eta-\eta)\to A\eta\). Hence \(\langle H\xi,\eta\rangle=-i\langle A\xi,\eta\rangle=i\langle\xi,A\eta\rangle=\langle\xi,-iA\eta\rangle=\langle\xi,H\eta\rangle\).

*\(H\) is self-adjoint.* Let \(\eta\in D(H^*)\) and \(\zeta=H^*\eta\). For \(\varepsilon>0\) and \(\xi\in\mathcal H\), Proposition 3.3(2) gives \(J_\varepsilon\xi\in D(A)\) and \(HJ_\varepsilon\xi=-i(U_\varepsilon\xi-\xi)\). Hence
\[
\big\langle\xi,\,i(U_{-\varepsilon}\eta-\eta)\big\rangle=\big\langle-i(U_\varepsilon\xi-\xi),\eta\big\rangle=\langle HJ_\varepsilon\xi,\eta\rangle=\langle J_\varepsilon\xi,\zeta\rangle=\int_0^\varepsilon\langle U_s\xi,\zeta\rangle\,ds=\Big\langle\xi,\int_0^\varepsilon U_{-s}\zeta\,ds\Big\rangle .
\]
The last two steps pass the bounded functional \(\langle\cdot,\zeta\rangle\) through the integral, use \(\langle U_s\xi,\zeta\rangle=\langle\xi,U_{-s}\zeta\rangle\), and then pass \(\langle\cdot,\xi\rangle\) through the integral of \(s\mapsto U_{-s}\zeta\) and take complex conjugates. Since \(\xi\) is arbitrary, \(i(U_{-\varepsilon}\eta-\eta)=\int_0^\varepsilon U_{-s}\zeta\,ds\), so
\[
\varepsilon^{-1}(U_{-\varepsilon}\eta-\eta)=-i\,\varepsilon^{-1}\int_0^\varepsilon U_{-s}\zeta\,ds\longrightarrow-i\zeta\qquad(\varepsilon\downarrow0),
\]
by Lemma 3.1(1). The semigroup \((U_{-t})_{t\ge0}\) has generator \(-A\) (Proposition 3.6(1)). So \(\eta\in D(A)\) and \(-A\eta=-i\zeta\). Hence \(H\eta=-iA\eta=\zeta=H^*\eta\). This shows \(H^*\subseteq H\); together with \(H\subseteq H^*\) it gives \(H=H^*\).

*The group.* By Theorem 4.2, \((e^{itH})_{t\in\mathbb R}\) is a strongly continuous group with generator \(iH=A\). By Proposition 3.6(3), \(U_t=e^{itH}\) for every \(t\).

*Uniqueness.* If \(U_t=e^{itK}\) with \(K\) self-adjoint, Theorem 4.2 shows that the generator of \((U_t)\) is \(iK\). So \(iK=A=iH\). \(\square\)

**Remark 4.4.** Theorems 4.2 and 4.3 show that \(H\mapsto(e^{itH})_{t\in\mathbb R}\) is a bijection from the self-adjoint operators on \(\mathcal H\) onto the strongly continuous unitary groups on \(\mathcal H\). For \(U_t=e^{itH}\), each \(U_t\) maps \(D(H)\) onto itself; a vector \(\xi\) lies in \(D(H)\) exactly when \(t\mapsto U_t\xi\) is differentiable at \(t=0\), and even a weak derivative along one sequence suffices; and then the derivative at every \(t\) is \(iU_tH\xi=iHU_t\xi\) (Proposition 3.6(2)). The spectral measure of \(H\) gives \(U_t=\int e^{it\lambda}\,dE_H(\lambda)\), so the group is the Fourier transform of the spectral measure of its generator. No separability or countability assumption on \(\mathcal H\) enters, and weak continuity of the group at \(t=0\) is enough.

**Corollary 4.5** (positive generators). Every strongly continuous unitary group has the form \(U_t=B^{it}:=e^{it\log B}\) for exactly one positive self-adjoint operator \(B\) with \(\ker B=0\); namely \(B=e^H\), where \(H\) is as in Theorem 4.3.

**Proof.** The function \(\exp\) is real and positive, so \(B:=\exp(H)\) is self-adjoint by Fact 1.8(b). By Fact 1.8(f), \(E_B((-\infty,0])=E_H(\exp^{-1}((-\infty,0]))=E_H(\varnothing)=0\). By Fact 1.8(g), \(B\ge0\) and \(\ker B=0\). As \(E_B\) vanishes off \((0,\infty)\), the operator \(\log B\) is defined, and by Fact 1.8(f), \(\log B=(\log\circ\exp)(H)=H\). So \(B^{it}=e^{itH}=U_t\). Conversely, let \(C\ge0\) with \(\ker C=0\) and \(C^{it}=U_t\) for all \(t\). Then \(\log C\) is self-adjoint and \(e^{it\log C}=U_t\), so \(\log C=H\) by Theorem 4.3. Since \(E_C\) vanishes off \((0,\infty)\) and \(\exp\circ\log\) is the identity there, Fact 1.8(f) gives \(C=\exp(\log C)=\exp(H)=B\). \(\square\)

**Proposition 4.6** (operators commuting with the group). Let \(U_t=e^{itH}\) with \(H\) self-adjoint, and let \(b\in B(\mathcal H)\). Then \(bU_t=U_tb\) for every \(t\) if and only if \(bH\subseteq Hb\), that is, \(bD(H)\subseteq D(H)\) and \(Hb\xi=bH\xi\) for \(\xi\in D(H)\).

**Proof.** Suppose \(b\) commutes with every \(U_t\), and let \(\xi\in D(H)\). Then \(t^{-1}(U_tb\xi-b\xi)=b\,t^{-1}(U_t\xi-\xi)\to ibH\xi\). By Theorem 4.2(2), \(b\xi\in D(H)\) and \(iHb\xi=ibH\xi\).

Conversely suppose \(bH\subseteq Hb\). Let \(\xi\in D(H)\) and \(t>0\), and put \(w(s)=U_{t-s}bU_s\xi\) for \(0\le s\le t\); \(w\) is continuous. The function \(u(s)=bU_s\xi\) has derivative \(ibHU_s\xi\), by Proposition 3.6(2) and Theorem 4.2. Since \(U_s\xi\in D(H)\), the hypothesis gives \(u(s)\in D(H)\) and \(Hu(s)=bHU_s\xi\). For \(y\in D(H)\) the function \(s\mapsto U_{t-s}y\) has derivative \(-iU_{t-s}Hy\). By Lemma 3.1(4),
\[
w'(s)=U_{t-s}\,ibHU_s\xi-iU_{t-s}Hu(s)=iU_{t-s}\big(bHU_s\xi-bHU_s\xi\big)=0\qquad(0<s<t).
\]
By Lemma 3.1(2), \(U_tb\xi=w(0)=w(t)=bU_t\xi\). For \(t<0\) apply this to the group \((U_{-t})=(e^{it(-H)})\), noting that \(b(-H)\subseteq(-H)b\). Both sides are bounded and agree on the dense subspace \(D(H)\). \(\square\)

**Remark 4.7.** Suppose every \(U_t\) belongs to a von Neumann algebra \(N\subseteq B(\mathcal H)\). Then every unitary \(v\) in the commutant \(N'\) commutes with all \(U_t\), so Proposition 4.6 gives \(vH\subseteq Hv\) and \(v^*H\subseteq Hv^*\). Hence \(v\) maps \(D(H)\) onto itself and commutes with \(H\) there. In the terminology of the lesson *Spectral calculus with its domains retained*, \(H\) is affiliated with \(N\), and that lesson shows that the spectral projections and the bounded Borel functions of \(H\) then belong to \(N\). By Corollary 4.5 the same holds for the positive operator \(B\) with \(B^{it}=U_t\).

**Example 4.8** (multiplication groups). Let \((a_k)_{k\in I}\) be real numbers and \((U_tx)_k=e^{ita_k}x_k\) on \(\ell^2(I)\). By Fact 1.8(h), \(U_t=e^{itM}\), where \(M\) is multiplication by \((a_k)\) on its maximal domain; so \(M\) is the self-adjoint operator of Theorem 4.3 for this group. Theorem 4.2(2) says that \(t^{-1}(U_tx-x)\) converges if and only if \(\sum_ka_k^2|x_k|^2<\infty\). The "if" part can also be seen directly: the \(k\)-th coordinate of \(t^{-1}(U_tx-x)\) tends to \(ia_kx_k\) and has modulus at most \(|a_kx_k|\), so dominated convergence for sums gives the limit \((ia_kx_k)_k\). The index set \(I\) may be uncountable.

## 5. Cores of generators

A reference for this section is [van Neerven, Section 13.1].

**Theorem 5.1.** Let \((T_t)_{t\ge0}\) be a strongly continuous semigroup on \(X\) with generator \(A\), and let \(D\subseteq D(A)\) be a subspace that is dense in \(X\). Let \(\Theta\subseteq[0,\infty)\) be a set whose closure contains an interval \([a,b]\) with \(a<b\), and suppose that \(T_tD\subseteq D\) for every \(t\in\Theta\). Then the closure of \(D\) in the graph norm of \(A\) contains \(T_aD(A)\). Consequently:

1. if \(a=0\), then \(D\) is a core for \(A\); in particular, a subspace of \(D(A)\) that is dense in \(X\) and that every \(T_t\), \(t\ge0\), maps into itself is a core;
2. if \((T_t)\) is the restriction to \(t\ge0\) of a strongly continuous group, then \(D\) is a core for \(A\); for groups, \(\Theta\) may be any subset of \(\mathbb R\) whose closure contains a nondegenerate interval.

**Proof.** Let \(D_1\) be the closure of \(D\) in the Banach space \((D(A),\|\cdot\|_A)\). For \(t\ge0\), \(T_t\) maps \(D(A)\) into itself with \(\|T_tx\|_A\le\|T_t\|\,\|x\|_A\), because \(AT_tx=T_tAx\) (Proposition 3.3(4)). For \(x\in D(A)\), the map \(t\mapsto T_tx\) is continuous for the graph norm, because \(t\mapsto T_tx\) and \(t\mapsto T_tAx\) are continuous.

Step 1: \(T_tD_1\subseteq D_1\) for \(a\le t\le b\). Let \(x\in D\) and choose \(t_k\in\Theta\) with \(t_k\to t\). Then \(T_{t_k}x\in D\) and \(T_{t_k}x\to T_tx\) in the graph norm, so \(T_tx\in D_1\). If \(x\in D_1\), choose \(x_k\in D\) with \(x_k\to x\) in the graph norm. Then \(T_tx_k\in D_1\) and \(T_tx_k\to T_tx\) in the graph norm, so \(T_tx\in D_1\).

Step 2: \(T_aJ_\varepsilon x\in D_1\) for \(x\in D_1\) and \(0<\varepsilon\le b-a\). By Step 1, \(s\mapsto T_{a+s}x\) is a continuous map from \([0,\varepsilon]\) into the Banach space \((D_1,\|\cdot\|_A)\). Its Riemann integral for the graph norm lies in \(D_1\). The inclusion of \((D(A),\|\cdot\|_A)\) into \(X\) is bounded, so this integral equals the integral in \(X\), which is \(\int_0^\varepsilon T_{a+s}x\,ds=T_aJ_\varepsilon x\).

Step 3: \(T_aJ_\varepsilon x\in D_1\) for every \(x\in X\). Choose \(x_k\in D\) with \(x_k\to x\) in \(X\), using the density of \(D\). By Step 2, \(T_aJ_\varepsilon x_k\in D_1\). Moreover \(T_aJ_\varepsilon x_k\to T_aJ_\varepsilon x\) in \(X\), and by Proposition 3.3(2),(4),
\[
AT_aJ_\varepsilon x_k=T_a(T_\varepsilon x_k-x_k)\longrightarrow T_a(T_\varepsilon x-x)=AT_aJ_\varepsilon x .
\]
So the convergence holds in the graph norm, and \(T_aJ_\varepsilon x\in D_1\) because \(D_1\) is closed.

Step 4: \(T_aD(A)\subseteq D_1\). Let \(x\in D(A)\). By Proposition 3.3(3),(4), \(\varepsilon^{-1}J_\varepsilon x\to x\) and \(A\varepsilon^{-1}J_\varepsilon x=\varepsilon^{-1}J_\varepsilon Ax\to Ax\), so \(\varepsilon^{-1}J_\varepsilon x\to x\) in the graph norm. Since \(T_a\) is bounded for the graph norm, \(\varepsilon^{-1}T_aJ_\varepsilon x\to T_ax\) in the graph norm, and Step 3 gives \(T_ax\in D_1\).

For (1), \(T_0=1\), so \(D_1=D(A)\). For (2), the same four steps work verbatim for a group and an interval \([a,b]\subseteq\mathbb R\), using Proposition 3.6(2) in Step 3; and \(T_aD(A)=D(A)\) by Proposition 3.6(2). \(\square\)

**Corollary 5.2.** Let \(H\) be self-adjoint, and let \(D\subseteq D(H)\) be a dense subspace with \(e^{itH}D\subseteq D\) for all \(t\) in a set whose closure contains a nondegenerate interval. Then \(D\) is a core for \(H\). In particular \(D(H^k)\) for \(k\ge1\), \(D^\infty(H)=\bigcap_kD(H^k)\) and \(\bigcup_{n\ge1}E_H([-n,n])\mathcal H\) are cores for \(H\).

**Proof.** By Theorem 4.2 the generator of \((e^{itH})\) is \(iH\), whose graph norm equals that of \(H\); so Theorem 5.1(2) applies. For the three subspaces, note first that by Fact 1.8(d) and induction, \(H^k=(\lambda^k)(H)\), with domain \(\{\xi : \int\lambda^{2k}d\mu_\xi<\infty\}\); here we use \(\lambda^{2k-2}\le1+\lambda^{2k}\) and the finiteness of \(\mu_\xi\). Each \(U_t=e^{itH}\) commutes with every \(E_H(B)\) (Fact 1.8(c)), so \(\mu_{U_t\xi}(B)=\|E_H(B)U_t\xi\|^2=\|E_H(B)\xi\|^2=\mu_\xi(B)\). Hence \(U_t\) preserves every domain defined by an integrability condition on \(\mu_\xi\), and it preserves each \(E_H([-n,n])\mathcal H\). A vector \(\xi\in E_H([-n,n])\mathcal H\) has \(\mu_\xi\) concentrated on \([-n,n]\), so it lies in every \(D(H^k)\). Finally \(E_H([-n,n])\xi\to\xi\) for every \(\xi\) by Fact 1.8(e), so all three subspaces are dense. \(\square\)

**Example 5.3** (the momentum operator). Let \(\mathcal H=L^2(\mathbb R)\) and \((U_tf)(x)=f(x+t)\). Each \(U_t\) is unitary, \(U_sU_t=U_{s+t}\), and the group is strongly continuous by Fact 1.10. Let \(A\) be its generator. For a smooth \(f\) with compact support,
\[
t^{-1}\big(f(x+t)-f(x)\big)-f'(x)=t^{-1}\int_0^t\big(f'(x+s)-f'(x)\big)\,ds ,
\]
which has modulus at most \((|t|/2)\sup|f''|\) and vanishes outside the compact set \(Q=\operatorname{supp}f+[-1,1]\) when \(|t|\le1\). So \(\|t^{-1}(U_tf-f)-f'\|_2\le(|t|/2)\sup|f''|\,|Q|^{1/2}\to0\). Hence the smooth functions with compact support lie in \(D(A)\), with \(Af=f'\). They form a dense subspace (Fact 1.10) that every \(U_t\) maps into itself. By Theorem 5.1 they form a core for \(A\). By Stone's theorem, \(U_t=e^{itP}\), where \(P=-iA\) is self-adjoint and is the closure of the operator \(f\mapsto-if'\) on smooth functions with compact support. By Theorem 4.2, \(D(P)\) is the set of \(f\in L^2(\mathbb R)\) for which \(t^{-1}(f(\cdot+t)-f)\) converges in \(L^2\) as \(t\to0\).

**Example 5.4** (a dense subspace of the domain that is not a core). Let \(\mathcal H=\ell^2(\mathbb Z)\), \((Hx)_n=nx_n\) on its maximal domain, and \(U_t=e^{itH}\), so \((U_tx)_n=e^{int}x_n\) (Fact 1.8(h)). The finitely supported sequences form a dense subspace \(c_{00}\) that every \(U_t\) maps into itself, so \(c_{00}\) is a core for \(H\). Now let
\[
D'=\Big\{x\in c_{00} : \sum_nx_n=0\Big\}.
\]
*\(D'\) is dense in \(\mathcal H\).* Let \(v_N=N^{-1}\sum_{n=1}^Ne_n\), so \(\|v_N\|=N^{-1/2}\to0\) and \(\sum_n(v_N)_n=1\). For \(x\in c_{00}\), the vectors \(x-(\sum_nx_n)v_N\) lie in \(D'\) and converge to \(x\).

*\(D'\) is not a core.* For \(x\in D(H)\) the Cauchy–Schwarz inequality gives
\[
\sum_n|x_n|\le\Big(\sum_n(1+n^2)|x_n|^2\Big)^{1/2}\Big(\sum_n\frac1{1+n^2}\Big)^{1/2}\le c\,\|x\|_H ,
\]
with \(c^2=\sum_n(1+n^2)^{-1}\). So \(\ell(x)=\sum_nx_n\) is a linear functional on \(D(H)\) that is continuous for the graph norm. It vanishes on \(D'\), hence on the graph closure of \(D'\), but \(\ell(e_0)=1\) and \(e_0\in D(H)\).

Theorem 5.1 does not apply because \(D'\) is not invariant: \(U_t(e_0-e_1)=e_0-e^{it}e_1\) has coordinate sum \(1-e^{it}\neq0\) unless \(t\in2\pi\mathbb Z\). On the other hand \(U_t=1\) for \(t\in2\pi\mathbb Z\), so \(D'\) is invariant under \(U_t\) for all \(t\) in the closed set \(2\pi\mathbb Z\). Hence the hypothesis on \(\Theta\) in Theorem 5.1 cannot be weakened to an unbounded discrete set of times.

## 6. Analytic vectors

**Definition 6.1.** Let \(T\) be an operator in \(X\), and let \(T^n\) denote the \(n\)-fold product with its natural domain. The vectors in \(D^\infty(T)=\bigcap_{n\ge1}D(T^n)\) are the *smooth vectors* of \(T\). A smooth vector \(\xi\) is *analytic* if \(\sum_ns^n\|T^n\xi\|/n!<\infty\) for some \(s>0\). Its *radius* \(r(\xi)\in(0,\infty]\) is the supremum of such \(s\), and \(\xi\) is *entire* if \(r(\xi)=\infty\). We write \(D^\omega(T)\) for the set of analytic vectors of \(T\).

**Lemma 6.2.** Let \(T\) be an operator in \(X\).

1. \(D^\omega(T)\) is a subspace, \(TD^\omega(T)\subseteq D^\omega(T)\), and \(r(T\xi)\ge r(\xi)\).
2. Let \(T\) be closed and \(\xi\in D^\omega(T)\). For \(|z|<r(\xi)\) the series
\[
\Phi_\xi(z)=\sum_{n\ge0}\frac{z^n}{n!}T^n\xi
\]
converges in norm and defines a holomorphic function on \(\Delta(0,r(\xi))\). For such \(z\): \(\Phi_\xi(z)\in D^\omega(T)\); \(T^k\Phi_\xi(z)=\Phi_{T^k\xi}(z)\) for every \(k\); \(r(\Phi_\xi(z))\ge r(\xi)-|z|\); and \(\Phi_\xi'=\Phi_{T\xi}=T\Phi_\xi\). Moreover \(\Phi_{\Phi_\xi(w)}(z)=\Phi_\xi(z+w)\) whenever \(|z|+|w|<r(\xi)\).

**Proof.** (1) The inequality \(\|T^n(\lambda\xi+\eta)\|\le|\lambda|\,\|T^n\xi\|+\|T^n\eta\|\) shows that \(r(\lambda\xi+\eta)\ge\min(r(\xi),r(\eta))\). Let \(0<s<s'<r(\xi)\). The terms \(s'^m\|T^m\xi\|/m!\) of a convergent series are bounded, say by \(C\). Then
\[
\sum_n\frac{s^n}{n!}\|T^{n+1}\xi\|\le\frac C{s'}\sum_n(n+1)\Big(\frac s{s'}\Big)^n<\infty,
\]
so \(T\xi\) is analytic with \(r(T\xi)\ge s\). As \(s<r(\xi)\) was arbitrary, \(r(T\xi)\ge r(\xi)\).

(2) The series converges absolutely for \(|z|<r(\xi)\). A norm-convergent power series is holomorphic, and its derivative is the termwise derivative (Theorem 2.2), which is \(\Phi_{T\xi}\). The partial sums \(q_m(z)=\sum_{n\le m}z^nT^n\xi/n!\) lie in \(D(T)\), and \(Tq_m(z)\) are the partial sums of \(\Phi_{T\xi}(z)\), which converge because \(r(T\xi)\ge r(\xi)\) by (1). Since \(T\) is closed, \(\Phi_\xi(z)\in D(T)\) and \(T\Phi_\xi(z)=\Phi_{T\xi}(z)\). By induction, using (1) for \(T^k\xi\), we get \(T^k\Phi_\xi(z)=\Phi_{T^k\xi}(z)\) for every \(k\). Hence, for \(s>0\) with \(s+|z|<r(\xi)\),
\[
\sum_k\frac{s^k}{k!}\|T^k\Phi_\xi(z)\|\le\sum_k\sum_n\frac{s^k|z|^n}{k!\,n!}\|T^{n+k}\xi\|=\sum_m\frac{(s+|z|)^m}{m!}\|T^m\xi\|<\infty,
\]
so \(\Phi_\xi(z)\) is analytic and \(r(\Phi_\xi(z))\ge r(\xi)-|z|\). The same computation, without norms, shows that the double series \(\sum_k\sum_nz^kw^nT^{n+k}\xi/(k!\,n!)\) converges absolutely when \(|z|+|w|<r(\xi)\). Summing it first over \(n\) gives \(\Phi_{\Phi_\xi(w)}(z)\); grouping the terms with \(n+k=m\) gives \(\sum_m(z+w)^mT^m\xi/m!=\Phi_\xi(z+w)\). \(\square\)

**Theorem 6.3** (Nelson's theorem). Let \(T\) be a symmetric operator in \(\mathcal H\).

1. If \(T\) is closed and \(D^\omega(T)\) is dense, then \(T\) is self-adjoint and \(D^\omega(T)\) is a core for \(T\).
2. If \(D^\omega(T)\) is dense, then \(T\) is essentially self-adjoint.

*Reference:* due to Nelson.

**Proof.** (1) Write \(D^\omega=D^\omega(T)\). For \(\xi\in D^\omega\) and real \(t\) with \(|t|<r(\xi)\) put \(V_t\xi=\Phi_\xi(it)\).

Step 1: \(V_t\) is isometric and preserves radii. Let \(g(t)=\|\Phi_\xi(it)\|^2\) for \(|t|<r(\xi)\). By Lemma 6.2(2), \(t\mapsto\Phi_\xi(it)\) is differentiable with derivative \(iT\Phi_\xi(it)\), and \(\Phi_\xi(it)\in D(T)\). So
\[
g'(t)=2\operatorname{Re}\big\langle iT\Phi_\xi(it),\Phi_\xi(it)\big\rangle=-2\operatorname{Im}\big\langle T\Phi_\xi(it),\Phi_\xi(it)\big\rangle=0,
\]
because \(\langle T\zeta,\zeta\rangle\) is real for \(\zeta\in D(T)\). By Fact 1.6, \(g\) is constant, so \(\|V_t\xi\|=\|\xi\|\). Applying this to \(T^k\xi\), whose radius is at least \(r(\xi)\), and using \(T^kV_t\xi=V_tT^k\xi\) from Lemma 6.2(2), we get \(\|T^kV_t\xi\|=\|T^k\xi\|\) for all \(k\). So \(r(V_t\xi)=r(\xi)\).

Step 2: a local group law. If \(s,t\) are real with \(|s|+|t|<r(\xi)\), then \(V_sV_t\xi=V_{s+t}\xi\): this is the last statement of Lemma 6.2(2) with \(z=is\) and \(w=it\), and \(V_s\) is defined on \(V_t\xi\) because \(r(V_t\xi)=r(\xi)\). Since \(s\) and \(t\) enter symmetrically, also \(V_tV_s\xi=V_{s+t}\xi\). By induction on \(k\), if \(|c|<r(\eta)\) and \(m\ge1\), then \(V_{c/m}^k\eta=V_{kc/m}\eta\) for \(k\le m\); in particular \(V_{c/m}^m\eta=V_c\eta\).

Step 3: a group of isometries of \(D^\omega\). For real \(u\) and \(\xi\in D^\omega\) choose an integer \(m\ge1\) with \(|u|/m<r(\xi)\), and put \(V_u\xi=V_{u/m}^m\xi\). All the vectors \(V_{u/m}^k\xi\) have radius \(r(\xi)\) by Step 1, so this is defined. It does not depend on \(m\): if \(m'\) is another choice, Step 2 applied to each vector \(V_{u/m}^k\xi\) gives \(V_{u/m}=V_{u/(mm')}^{m'}\) on it, so \(V_{u/m}^m\xi=V_{u/(mm')}^{mm'}\xi\), and the right side is symmetric in \(m\) and \(m'\). Each \(V_u\) maps \(D^\omega\) into \(D^\omega\), is linear (the power series are linear in \(\xi\), and \(r\) of a linear combination is at least the minimum of the radii), and is isometric. For real \(u,v\), choose \(m\) with \((|u|+|v|)/m<r(\xi)\). On vectors of radius \(r(\xi)\) the operators \(V_{u/m}\) and \(V_{v/m}\) commute and \(V_{u/m}V_{v/m}=V_{(u+v)/m}\), by Step 2. Hence \(V_uV_v\xi=V_{u/m}^mV_{v/m}^m\xi=(V_{u/m}V_{v/m})^m\xi=V_{(u+v)/m}^m\xi=V_{u+v}\xi\). Also \(V_0=1\).

Step 4: a unitary group. Each \(V_u\) is an isometry on the dense subspace \(D^\omega\), so it extends to an isometry \(\widetilde V_u\) of \(\mathcal H\). The group law extends by continuity, and \(\widetilde V_u\widetilde V_{-u}=1\) shows that \(\widetilde V_u\) is onto; so \((\widetilde V_u)\) is a unitary group. For \(\xi\in D^\omega\), \(\widetilde V_t\xi-\xi=\Phi_\xi(it)-\Phi_\xi(0)\to0\) as \(t\to0\). For general \(\xi\) and \(\varepsilon>0\) choose \(\eta\in D^\omega\) with \(\|\xi-\eta\|<\varepsilon\); then \(\|\widetilde V_t\xi-\xi\|\le2\varepsilon+\|\widetilde V_t\eta-\eta\|\). So the group is strongly continuous.

Step 5: identification. By Stone's theorem, \(\widetilde V_t=e^{itK}\) for a self-adjoint \(K\). For \(\xi\in D^\omega\), \(t^{-1}(\widetilde V_t\xi-\xi)=t^{-1}(\Phi_\xi(it)-\Phi_\xi(0))\to i\Phi_\xi'(0)=iT\xi\). By Theorem 4.2(2), \(\xi\in D(K)\) and \(K\xi=T\xi\). The subspace \(D^\omega\subseteq D(K)\) is dense and invariant under every \(\widetilde V_t\). By Corollary 5.2 it is a core for \(K\), so \(K\) is the closure of \(K|_{D^\omega}=T|_{D^\omega}\). As \(T\) is closed, \(K\subseteq T\). Since \(K\) is self-adjoint and \(T\) is symmetric, \(T=K\) (Section 1). So \(T\) is self-adjoint, and \(D^\omega\) is a core for it.

(2) A symmetric operator is closable, and \(\overline T\) is symmetric. Since \(\overline T\) extends \(T\), every analytic vector of \(T\) is an analytic vector of \(\overline T\), with the same powers. So \(D^\omega(\overline T)\) is dense, and \(\overline T\) is self-adjoint by (1). \(\square\)

**Proposition 6.4.** Let \(H\) be self-adjoint and \(n>0\). Every \(\xi\in E_H([-n,n])\mathcal H\) is an entire vector of \(H\), with \(\|H^k\xi\|\le n^k\|\xi\|\). Hence \(D^\omega(H)\) is dense. Consequently a closed symmetric operator is self-adjoint if and only if its analytic vectors are dense.

**Proof.** For such \(\xi\) the measure \(\mu_\xi\) is concentrated on \([-n,n]\), so by the proof of Corollary 5.2, \(\xi\in D(H^k)\) and \(\|H^k\xi\|^2=\int\lambda^{2k}d\mu_\xi\le n^{2k}\|\xi\|^2\). Then \(\sum_ks^k\|H^k\xi\|/k!\le e^{sn}\|\xi\|\) for every \(s>0\). Density follows from \(E_H([-n,n])\xi\to\xi\) (Fact 1.8(e)). The last sentence combines this with Theorem 6.3(1). \(\square\)

**Example 6.5** (smooth vectors are not enough). Let \(\mathcal H=L^2(0,1)\), let \(D\) be the smooth functions with compact support in \((0,1)\), which are dense by Fact 1.10, and let \(Tf=-if'\) on \(D(T)=D\). For \(f\in D\) and every smooth function \(g\) on \([0,1]\), integration by parts gives
\[
\langle Tf,g\rangle=\int_0^1-if'(x)\overline{g(x)}\,dx=\int_0^1f(x)\,\overline{-ig'(x)}\,dx=\langle f,-ig'\rangle ,
\]
because \(f\) vanishes near \(0\) and \(1\). With \(g\in D\) this shows that \(T\) is symmetric. Since \(TD\subseteq D\), every vector of \(D\) is a smooth vector of \(T\). But \(T\) is not essentially self-adjoint. Indeed, for \(\eta(x)=e^{-x}\) the identity gives \(\langle Tf,\eta\rangle=\langle f,i\eta\rangle\), so \(\eta\in D(T^*)\) and \(T^*\eta=i\eta\). If \(\overline T\) were self-adjoint, then \(T^*=\overline T^{\,*}=\overline T\) would be self-adjoint, and \(\langle T^*\eta,\eta\rangle\) would be real; but it equals \(i\|\eta\|^2\neq0\).

By Theorem 6.3(2), the analytic vectors of \(T\) are therefore not dense. In fact \(D^\omega(T)=0\). Let \(f\in D\) be analytic and \(0<s<r(f)\), so that \(\sum_ks^k\|T^{k+1}f\|/k!<\infty\) by Lemma 6.2(1). Since \(f^{(k)}\) vanishes near \(0\), the Cauchy–Schwarz inequality gives \(|f^{(k)}(x)|=|\int_0^xf^{(k+1)}|\le\|f^{(k+1)}\|_2=\|T^{k+1}f\|\) for \(x\in[0,1]\). Hence \(s^k\sup|f^{(k)}|/k!\to0\). Taylor's formula (Fact 1.6), applied to the real and imaginary parts of \(f\), bounds the error of the Taylor polynomial of degree \(m-1\) at \(x_0\) by \(2\sup|f^{(m)}|\,|x-x_0|^m/m!\), which tends to \(0\) when \(|x-x_0|\le s\). So \(f\) equals its Taylor series about every point \(x_0\in[0,1]\) on \([x_0-s,x_0+s]\cap[0,1]\). All derivatives of \(f\) vanish at \(0\), so \(f=0\) on \([0,s]\); then all derivatives vanish at \(s\), so \(f=0\) on \([0,2s]\); and so on. Thus \(f=0\).

## 7. Strong resolvent convergence

A reference for strong resolvent convergence is [Teschl, Section 6.6].

For a self-adjoint operator \(H\) and \(\lambda\in\mathbb C\setminus\mathbb R\) we write \(R(\lambda)=r_\lambda(H)\) as in Example 2.6; for self-adjoint operators \(H_j\) we write \(R_j(\lambda)\).

**Lemma 7.1** (resolvents of a self-adjoint operator). Let \(H\) be self-adjoint and \(\lambda,\mu\in\mathbb C\setminus\mathbb R\).

1. \(R(\lambda)\) maps \(\mathcal H\) onto \(D(H)\); \((H-\lambda)R(\lambda)=1\), and \(R(\lambda)(H-\lambda)\xi=\xi\) for \(\xi\in D(H)\). Thus \(R(\lambda)=(H-\lambda)^{-1}\). Moreover \(\|R(\lambda)\|\le1/|\operatorname{Im}\lambda|\), \(R(\lambda)^*=R(\bar\lambda)\), \(R(\lambda)R(\mu)=R(\mu)R(\lambda)\), and the resolvent identity (2.2) holds.
2. \(\|R(\lambda)\xi\|^2=\operatorname{Im}\langle R(\lambda)\xi,\xi\rangle/\operatorname{Im}\lambda\) for every \(\xi\).
3. \(HR(\lambda)=1+\lambda R(\lambda)\), so \(\|HR(\lambda)\|\le1+|\lambda|/|\operatorname{Im}\lambda|\).
4. With \(U_t=e^{itH}\),
\[
R(\lambda)\xi=-i\int_0^\infty e^{-i\lambda t}U_t\xi\,dt\quad(\operatorname{Im}\lambda<0),\qquad R(\lambda)\xi=i\int_0^\infty e^{i\lambda t}U_{-t}\xi\,dt\quad(\operatorname{Im}\lambda>0).
\tag{7.1}
\]

**Proof.** (1) By Fact 1.8(b),(d), the function \(x-\lambda\) of \(H\) is \(H-\lambda\), with domain \(D(H)\). Apply Fact 1.8(d) to \(f(x)=x-\lambda\) and \(g=r_\lambda\), whose product is \(1\). The product \((H-\lambda)R(\lambda)\) has domain \(\mathcal H\cap\mathcal H\) and equals \(1\). The product \(R(\lambda)(H-\lambda)\) has domain \(D(H)\cap\mathcal H\) and equals \(1\) there. So \(R(\lambda)\) is the inverse of \(H-\lambda\), and it maps \(\mathcal H\) onto \(D(H)\). The remaining statements come from Example 2.6 and Fact 1.8(c): \(\bar r_\lambda=r_{\bar\lambda}\), and bounded functions of \(H\) commute.

(2) By (1) and (2.2) with \(\mu=\bar\lambda\), \(R(\lambda)^*R(\lambda)=R(\bar\lambda)R(\lambda)=(R(\lambda)-R(\bar\lambda))/(\lambda-\bar\lambda)\). Taking \(\langle\,\cdot\,\xi,\xi\rangle\) gives
\[
\|R(\lambda)\xi\|^2=\frac{\langle R(\lambda)\xi,\xi\rangle-\overline{\langle R(\lambda)\xi,\xi\rangle}}{2i\operatorname{Im}\lambda}=\frac{\operatorname{Im}\langle R(\lambda)\xi,\xi\rangle}{\operatorname{Im}\lambda}.
\]

(3) \(HR(\lambda)=(H-\lambda)R(\lambda)+\lambda R(\lambda)=1+\lambda R(\lambda)\).

(4) By Theorem 4.2, \((U_t)\) is a strongly continuous unitary group with generator \(iH\), so Proposition 3.6(4) applies with \(M=1\). Put \(\mu=i\lambda\); then \(\mu-iH=-i(H-\lambda)\), so \(R(\lambda)=-i(\mu-iH)^{-1}\). If \(\operatorname{Im}\lambda<0\), then \(\operatorname{Re}\mu>0\), and (3.1) gives the first formula. If \(\operatorname{Im}\lambda>0\), then \(\operatorname{Re}\mu<0\), and Proposition 3.6(4) gives \((\mu-iH)^{-1}=-\int_0^\infty e^{i\lambda t}U_{-t}\,dt\), which is the second formula. \(\square\)

**Lemma 7.2.** Let \((Y_j)\) and \((Z_j)\) be nets in \(B(\mathcal H)\) over the same directed set.

1. If \(Y_j\to Y\) and \(Z_j\to Z\) strongly and \(\sup_j\|Y_j\|<\infty\), then \(Y_jZ_j\to YZ\) strongly.
2. If \(Y_j\to Y\) weakly, then \(Y_j^*\to Y^*\) weakly.
3. If \(Y_j\to Y\) weakly and \(\|Y_j\xi\|\to\|Y\xi\|\) for every \(\xi\), then \(Y_j\to Y\) strongly.
4. If \(Y_j\) and \(Y\) are unitary and \(Y_j\to Y\) weakly, then \(Y_j\to Y\) strongly.

**Proof.** (1) \(\|(Y_jZ_j-YZ)\xi\|\le\|Y_j\|\,\|(Z_j-Z)\xi\|+\|(Y_j-Y)Z\xi\|\). (2) \(\langle Y_j^*\xi,\eta\rangle=\overline{\langle Y_j\eta,\xi\rangle}\). (3) \(\|(Y_j-Y)\xi\|^2=\|Y_j\xi\|^2-2\operatorname{Re}\langle Y_j\xi,Y\xi\rangle+\|Y\xi\|^2\to0\). (4) is (3), since \(\|Y_j\xi\|=\|\xi\|=\|Y\xi\|\). \(\square\)

**Lemma 7.3** (propagation through a half-plane). Let \((H_j)\) be a net of self-adjoint operators, and suppose that \(R_j(\mu)\) converges strongly, to an operator \(R'(\mu)\), for some \(\mu\) with \(\operatorname{Im}\mu>0\).

1. Then \(R_j(\lambda)\) converges strongly for every \(\lambda\) with \(\operatorname{Im}\lambda>0\). The limits \(R'(\lambda)\) satisfy \(R'(\lambda)=\sum_k(\lambda-\nu)^kR'(\nu)^{k+1}\) whenever \(\operatorname{Im}\nu>0\) and \(|\lambda-\nu|<\operatorname{Im}\nu\).
2. If moreover \(R'(\mu)=R(\mu)\) for the resolvent \(R\) of a self-adjoint operator \(H\), then \(R'(\lambda)=R(\lambda)\) for every \(\lambda\) with \(\operatorname{Im}\lambda>0\).

The same holds with the lower half-plane in place of the upper one.

**Proof.** (1) Let \(\Omega\) be the set of points \(\nu\) of the upper half-plane at which \(R_j(\nu)\) converges strongly. Let \(\nu\in\Omega\) and \(|\lambda-\nu|<\operatorname{Im}\nu\), and put \(q=|\lambda-\nu|/\operatorname{Im}\nu<1\). By (2.3), \(R_j(\lambda)=\sum_k(\lambda-\nu)^kR_j(\nu)^{k+1}\), and the \(k\)-th term has norm at most \(q^k/\operatorname{Im}\nu\) for every \(j\). By Lemma 7.2(1) each term converges strongly, to \((\lambda-\nu)^kR'(\nu)^{k+1}\), whose norm has the same bound. Given \(\xi\) and \(\varepsilon>0\), choose \(m\) with \(\sum_{k>m}2q^k\|\xi\|/\operatorname{Im}\nu<\varepsilon\). Then
\[
\Big\|R_j(\lambda)\xi-\sum_k(\lambda-\nu)^kR'(\nu)^{k+1}\xi\Big\|\le\Big\|\sum_{k\le m}(\lambda-\nu)^k\big(R_j(\nu)^{k+1}-R'(\nu)^{k+1}\big)\xi\Big\|+\varepsilon,
\]
and the finite sum tends to \(0\). So \(\lambda\in\Omega\), with the stated series. Thus \(\Omega\) contains the disc of radius \(\operatorname{Im}\nu\) about each of its points \(\nu\). If \(\lambda\) lies in the upper half-plane and in the closure of \(\Omega\), choose \(\nu\in\Omega\) with \(|\lambda-\nu|<\operatorname{Im}\lambda/2\); then \(\operatorname{Im}\nu>\operatorname{Im}\lambda/2>|\lambda-\nu|\), so \(\lambda\in\Omega\). Hence \(\Omega\) is nonempty, open and relatively closed in the connected upper half-plane, so it is the whole half-plane.

(2) Let \(\Omega'\) be the set of \(\nu\) in the upper half-plane with \(R'(\nu)=R(\nu)\). It contains \(\mu\). If \(\nu\in\Omega'\) and \(|\lambda-\nu|<\operatorname{Im}\nu\), then by (1) and by (2.3) for \(H\), \(R'(\lambda)=\sum_k(\lambda-\nu)^kR(\nu)^{k+1}=R(\lambda)\). The argument of (1) shows that \(\Omega'\) is the whole upper half-plane.

For the lower half-plane use \(|\operatorname{Im}\nu|\) in place of \(\operatorname{Im}\nu\). \(\square\)

**Theorem 7.4.** Let \(H\) and \(H_j\) (\(j\) in a directed set) be self-adjoint operators on \(\mathcal H\). Consider the conditions:

- (a) \(R_j(\lambda)\to R(\lambda)\) strongly for every \(\lambda\in\mathbb C\setminus\mathbb R\);
- (b) \(R_j(\lambda_0)\to R(\lambda_0)\) weakly for some \(\lambda_0\in\mathbb C\setminus\mathbb R\);
- (c) \(f(H_j)\to f(H)\) strongly for every bounded continuous \(f\colon\mathbb R\to\mathbb C\);
- (d) \(e^{itH_j}\to e^{itH}\) weakly for every \(t\in\mathbb R\);
- (e) \(e^{itH_j}\to e^{itH}\) strongly, uniformly for \(t\) in compact subsets of \(\mathbb R\).

Then (a), (b), (c) and (e) are equivalent, and they imply (d). If the net is a sequence, then (d) implies (a), so all five conditions are equivalent.

*Reference:* [Trotter 1958].

When (a) holds, we say that \(H_j\) *converges to \(H\) in the strong resolvent sense*.

**Proof.** Write \(U_j(t)=e^{itH_j}\) and \(U(t)=e^{itH}\).

*(a) implies (b)* is clear.

*(b) implies (a).* By Lemma 7.1(2),
\[
\|R_j(\lambda_0)\xi\|^2=\frac{\operatorname{Im}\langle R_j(\lambda_0)\xi,\xi\rangle}{\operatorname{Im}\lambda_0}\longrightarrow\frac{\operatorname{Im}\langle R(\lambda_0)\xi,\xi\rangle}{\operatorname{Im}\lambda_0}=\|R(\lambda_0)\xi\|^2 ,
\]
so Lemma 7.2(3) gives strong convergence at \(\lambda_0\). Also \(R_j(\bar\lambda_0)=R_j(\lambda_0)^*\to R(\lambda_0)^*=R(\bar\lambda_0)\) weakly, by Lemma 7.2(2), and the same argument gives strong convergence at \(\bar\lambda_0\). Lemma 7.3(2), in both half-planes, gives (a).

*(a) implies (c).* Let \(\mathcal A\) be the set of \(f\in C_0(\mathbb R)\) with \(f(H_j)\to f(H)\) strongly. It is a linear subspace. It is closed under products, by Lemma 7.2(1) and Fact 1.8(c), since \(\|f(H_j)\|\le\sup|f|\). It is closed in the supremum norm, since
\[
\|(f(H_j)-f(H))\xi\|\le2\sup|f-g|\,\|\xi\|+\|(g(H_j)-g(H))\xi\| .
\]
By (a) it contains every \(r_\lambda\), \(\lambda\notin\mathbb R\). The algebra generated by these functions is closed under conjugation (\(\bar r_\lambda=r_{\bar\lambda}\)), separates points (\(r_i\) is injective) and has no common zero (\(r_i\) never vanishes). By Fact 1.9 it is dense in \(C_0(\mathbb R)\), so \(\mathcal A=C_0(\mathbb R)\). Now let \(f\) be bounded and continuous, \(\xi\in\mathcal H\) and \(\varepsilon>0\). Put \(\chi_k(x)=\max(0,\min(1,k+1-|x|))\). Then \(\chi_k\in C_0(\mathbb R)\), \(0\le\chi_k\le1\) and \(\chi_k\to1\) pointwise, so \(\chi_k(H)\xi\to\xi\) by Fact 1.8(e). Fix \(k\) with \(\|\xi-\chi_k(H)\xi\|<\varepsilon\) and write \(\chi=\chi_k\). Since \(\chi\in\mathcal A\), eventually \(\|\xi-\chi(H_j)\xi\|<2\varepsilon\). Since \(f\chi\in C_0(\mathbb R)=\mathcal A\) and \(f(H_j)=(f\chi)(H_j)+f(H_j)(1-\chi(H_j))\),
\[
\|f(H_j)\xi-f(H)\xi\|\le\|(f\chi)(H_j)\xi-(f\chi)(H)\xi\|+\sup|f|\,\|\xi-\chi(H_j)\xi\|+\sup|f|\,\|\xi-\chi(H)\xi\|,
\]
which is eventually less than \(\varepsilon+3\varepsilon\sup|f|\).

*(c) implies (a):* take \(f=r_\lambda\), which is bounded and continuous on \(\mathbb R\).

*(c) implies (d):* take \(f(x)=e^{itx}\).

*(a) implies (e).* By what we have shown, (a) implies (d), and by Lemma 7.2(4), \(U_j(t)\to U(t)\) strongly for every \(t\). Write \(R_j=R_j(i)\) and \(R=R(i)\). Fix \(\eta\in\mathcal H\) and put \(g_j(t)=U_j(t)R_j\eta-U(t)R\eta\). By Theorem 4.2 and Proposition 3.6(2), \(t\mapsto U_j(t)R_j\eta\) has the continuous derivative \(iU_j(t)H_jR_j\eta\), and \(\|H_jR_j\eta\|\le2\|\eta\|\) by Lemma 7.1(3). By Lemma 3.1(3), \(\|U_j(t)R_j\eta-U_j(s)R_j\eta\|\le2\|\eta\|\,|t-s|\), and the same holds for \(U\) and \(R\). So every \(g_j\) satisfies \(\|g_j(t)-g_j(s)\|\le4\|\eta\|\,|t-s|\). Moreover
\[
g_j(t)=U_j(t)(R_j-R)\eta+(U_j(t)-U(t))R\eta\longrightarrow0
\]
for every \(t\). Let \(\tau>0\) and \(\varepsilon>0\), and choose points \(t_1,\ldots,t_m\) in \([-\tau,\tau]\) such that every \(t\in[-\tau,\tau]\) is within \(\varepsilon\) of one of them. Eventually \(\|g_j(t_l)\|<\varepsilon\) for all \(l\), and then \(\|g_j(t)\|<\varepsilon(1+4\|\eta\|)\) for all \(|t|\le\tau\). Hence
\[
\sup_{|t|\le\tau}\|(U_j(t)-U(t))R\eta\|\le\sup_{|t|\le\tau}\|g_j(t)\|+\|(R_j-R)\eta\|\longrightarrow0 .
\]
The range of \(R\) is \(D(H)\), which is dense, and \(\|U_j(t)-U(t)\|\le2\). Given \(\xi\) and \(\delta>0\), choose \(\eta\) with \(\|\xi-R\eta\|<\delta\); then \(\sup_{|t|\le\tau}\|(U_j(t)-U(t))\xi\|\le2\delta+\sup_{|t|\le\tau}\|(U_j(t)-U(t))R\eta\|\). This proves (e).

*(e) implies (d)* is clear.

*(e) implies (a).* By (7.1) with \(\lambda=-i\),
\[
R_j(-i)\xi-R(-i)\xi=-i\int_0^\infty e^{-t}\big(U_j(t)-U(t)\big)\xi\,dt .
\]
For \(\tau>0\), the norm of the right side is at most \(\sup_{0\le t\le\tau}\|(U_j(t)-U(t))\xi\|+2e^{-\tau}\|\xi\|\). So \(R_j(-i)\to R(-i)\) strongly, and (b) implies (a).

*(d) implies (a) for sequences.* By Lemma 7.2(4), \(U_n(t)\xi\to U(t)\xi\) for each \(t\). The continuous functions \(t\mapsto e^{-t}\|(U_n(t)-U(t))\xi\|\) tend to \(0\) pointwise and are bounded by \(2e^{-t}\|\xi\|\). By dominated convergence (Fact 1.7) their integrals over \([0,\infty)\) tend to \(0\). As in the previous step, \(R_n(-i)\to R(-i)\) strongly, and (b) implies (a). \(\square\)

**Remark 7.5.**

1. Strong resolvent convergence to a *given* self-adjoint operator can thus be tested at a single non-real point, and weak convergence there suffices. Without a given limit this fails; see Section 8.
2. Exercise 5 shows that (d) does not imply (a) for nets. The proof of (d) implies (a) uses dominated convergence, which is a statement about sequences.
3. In (c) the function must be continuous; see Example 7.7(3).

**Theorem 7.6** (a test through a core). Let \(H\) be self-adjoint, let \(D\) be a core for \(H\), and let \((H_j)\) be a net of self-adjoint operators. Suppose that every \(\xi\in D\) lies in \(D(H_j)\) for all \(j\) beyond some \(j(\xi)\), and that \(H_j\xi\to H\xi\). Then \(H_j\) converges to \(H\) in the strong resolvent sense.

**Proof.** For \(\xi\in D\) and \(j\) beyond \(j(\xi)\),
\[
\big(R_j(i)-R(i)\big)(H-i)\xi=R_j(i)\big((H-i)\xi-(H_j-i)\xi\big)=R_j(i)(H-H_j)\xi ,
\]
whose norm is at most \(\|(H-H_j)\xi\|\to0\). The subspace \((H-i)D\) is dense in \(\mathcal H\): every vector has the form \((H-i)x\) with \(x\in D(H)\) (Lemma 7.1(1)), and if \(x_k\in D\) converge to \(x\) in the graph norm, then \((H-i)x_k\to(H-i)x\). Since \(\|R_j(i)-R(i)\|\le2\), the convergence \(R_j(i)\to R(i)\) extends from this dense subspace to all of \(\mathcal H\). Theorem 7.4 completes the proof. \(\square\)

A version of Theorem 7.6, in which \(D\) lies in every \(D(H_j)\), is proved by another method in the lesson *Spectral calculus with its domains retained*, together with its consequence Theorem 7.4(c).

**Example 7.7.**

1. Let \(H\) be self-adjoint and \(H_n=n^{-1}H\). The operator \(0\) is bounded with domain \(\mathcal H\), so its graph norm is equivalent to the norm of \(\mathcal H\), and the dense subspace \(D(H)\) is a core for it. For \(\xi\in D(H)\), \(H_n\xi=n^{-1}H\xi\to0\). By Theorem 7.6, \(H_n\to0\) in the strong resolvent sense, and by Theorem 7.4, \(e^{itH/n}\to1\) strongly, uniformly for \(t\) in compact sets.
2. On \(\ell^2(\mathbb N)\) let \(P_n\) be the projection onto \(\mathbb Ce_n\) and \(H_n=nP_n\). For a finitely supported \(\xi\), \(H_n\xi=0\) once \(n\) is beyond the support, and the finitely supported vectors form a core for \(0\). By Theorem 7.6, \(H_n\to0\) in the strong resolvent sense. Nevertheless, for \(\xi=(1/k)_{k\ge1}\) we get \(H_n\xi=e_n\), which does not converge. The resolvents do not converge in norm either: the resolvent of \(0\) at \(i\) is \(i\cdot1\), and \(\|R_n(i)-i\|\ge|(n-i)^{-1}-i|\to1\).
3. Let \(H_n=1/n\) on \(\mathbb C\) and \(f=1_{(0,\infty)}\). Then \(H_n\to0\) in the strong resolvent sense, but \(f(H_n)=1\) for every \(n\) while \(f(0)=0\). So (c) of Theorem 7.4 fails for this discontinuous \(f\).

## 8. When the limit of the resolvents is not a resolvent

The next lemma recognizes resolvents among families of bounded operators.

**Lemma 8.1.** Let \(\mathcal K\) be a Hilbert space, and let \(Q(\lambda)\), \(\lambda\in\mathbb C\setminus\mathbb R\), be bounded operators on \(\mathcal K\) with
\[
Q(\lambda)-Q(\mu)=(\lambda-\mu)Q(\lambda)Q(\mu),\qquad Q(\lambda)^*=Q(\bar\lambda),
\tag{8.1}
\]
and with \(\ker Q(\lambda_1)=0\) for one \(\lambda_1\). Then there is a unique self-adjoint operator \(K\) in \(\mathcal K\) with \(Q(\lambda)=(K-\lambda)^{-1}\) for every \(\lambda\in\mathbb C\setminus\mathbb R\).

**Proof.** Exchanging \(\lambda\) and \(\mu\) in (8.1) shows \(Q(\lambda)Q(\mu)=Q(\mu)Q(\lambda)\). If \(Q(\mu)\xi=0\), then \(Q(\lambda)\xi=Q(\mu)\xi+(\lambda-\mu)Q(\lambda)Q(\mu)\xi=0\); so all the kernels coincide, and every \(Q(\lambda)\) is injective. The identity \(Q(\mu)=Q(\lambda)\big(1+(\mu-\lambda)Q(\mu)\big)\), which is (8.1) rearranged, shows \(\operatorname{ran}Q(\mu)\subseteq\operatorname{ran}Q(\lambda)\); by symmetry all the ranges equal one subspace \(D\). It is dense, because \(D^\perp=\ker Q(\lambda)^*=\ker Q(\bar\lambda)=0\).

Define \(K=\lambda+Q(\lambda)^{-1}\) on \(D\). This does not depend on \(\lambda\). Indeed, let \(\xi=Q(\lambda)\eta\). By (8.1) and commutativity, \(Q(\mu)\big(\eta+(\lambda-\mu)\xi\big)=Q(\mu)\eta+\big(Q(\lambda)-Q(\mu)\big)\eta=\xi\), so \(Q(\mu)^{-1}\xi=\eta+(\lambda-\mu)\xi\) and \(\mu\xi+Q(\mu)^{-1}\xi=\lambda\xi+\eta=\lambda\xi+Q(\lambda)^{-1}\xi\).

\(K\) is symmetric. Let \(\xi,\zeta\in D\), and write \(\xi=Q(\lambda)\eta\) and \(\zeta=Q(\bar\lambda)\theta\). Then \(K\xi=\lambda\xi+\eta\) and \(K\zeta=\bar\lambda\zeta+\theta\). Moreover \(\langle\eta,\zeta\rangle=\langle\eta,Q(\bar\lambda)\theta\rangle=\langle Q(\lambda)\eta,\theta\rangle=\langle\xi,\theta\rangle\). Hence \(\langle K\xi,\zeta\rangle=\lambda\langle\xi,\zeta\rangle+\langle\xi,\theta\rangle=\langle\xi,K\zeta\rangle\).

\(K\) is self-adjoint. For every \(\lambda\notin\mathbb R\), \(K-\lambda=Q(\lambda)^{-1}\) maps \(D\) onto \(\mathcal K\). Let \(\eta\in D(K^*)\) and choose \(\zeta\in D\) with \((K-\bar\lambda)\zeta=(K^*-\bar\lambda)\eta\). Since \(K\subseteq K^*\), the vector \(\eta-\zeta\) lies in \(\ker(K^*-\bar\lambda)=\operatorname{ran}(K-\lambda)^\perp=0\). So \(\eta=\zeta\in D\), and \(K^*\subseteq K\). Together with \(K\subseteq K^*\) this gives \(K=K^*\), and \((K-\lambda)^{-1}=Q(\lambda)\).

If \(K'\) is self-adjoint with \((K'-\lambda)^{-1}=Q(\lambda)\), then \(D(K')=\operatorname{ran}Q(\lambda)=D\) and \(K'=\lambda+Q(\lambda)^{-1}=K\). \(\square\)

**Theorem 8.2.** Let \((H_j)\) be a net of self-adjoint operators on \(\mathcal H\). Suppose that \(R_j(\lambda_0)\) and \(R_j(\mu_0)\) converge strongly for some \(\lambda_0\) with \(\operatorname{Im}\lambda_0>0\) and some \(\mu_0\) with \(\operatorname{Im}\mu_0<0\).

1. \(R_j(\lambda)\) converges strongly for every \(\lambda\in\mathbb C\setminus\mathbb R\), to an operator \(R'(\lambda)\). These satisfy \(\|R'(\lambda)\|\le1/|\operatorname{Im}\lambda|\), \(R'(\lambda)^*=R'(\bar\lambda)\) and \(R'(\lambda)-R'(\mu)=(\lambda-\mu)R'(\lambda)R'(\mu)\).
2. The kernel \(N=\ker R'(\lambda)\) does not depend on \(\lambda\), and \(N^\perp\) is the closure of the range of \(R'(\lambda)\).
3. Let \(P\) be the projection onto \(N^\perp\). There is a unique self-adjoint operator \(H_0\) in the Hilbert space \(N^\perp\) with \(R'(\lambda)\xi=(H_0-\lambda)^{-1}P\xi\) for all \(\xi\in\mathcal H\) and \(\lambda\notin\mathbb R\).
4. For every \(f\in C_0(\mathbb R)\), \(f(H_j)\to f(H_0)P\) strongly.
5. \((H_j)\) converges in the strong resolvent sense to some self-adjoint operator on \(\mathcal H\) if and only if \(N=0\), that is, if and only if \(R'(\lambda)\) is injective for one, or every, \(\lambda\notin\mathbb R\). The limit is then \(H_0\).

*Remark.* Strong convergence of the resolvents at one point of each half-plane does not by itself give strong resolvent convergence to a self-adjoint operator: the operators \(H_n=n\) on \(\mathbb C\) show this (Example 8.3), so the kernel condition in (5) is needed.

**Proof.** (1) Lemma 7.3(1), applied in both half-planes, gives strong convergence everywhere off the real line. A strong limit of operators of norm at most \(c\) has norm at most \(c\). The resolvent identity passes to the limit by Lemma 7.2(1). Finally \(\langle R'(\lambda)\xi,\eta\rangle=\lim_j\langle R_j(\lambda)\xi,\eta\rangle=\lim_j\langle\xi,R_j(\bar\lambda)\eta\rangle=\langle\xi,R'(\bar\lambda)\eta\rangle\).

(2) The first part of the proof of Lemma 8.1 shows that the kernels coincide. The orthogonal complement of the range of \(R'(\lambda)\) is \(\ker R'(\lambda)^*=\ker R'(\bar\lambda)=N\).

(3) Put \(\mathcal K=N^\perp\). Each \(R'(\lambda)\) vanishes on \(N\) and maps \(\mathcal H\) into \(\mathcal K\). So \(R'(\lambda)=R'(\lambda)P\), and the restriction \(Q(\lambda)\) of \(R'(\lambda)\) to \(\mathcal K\) is a bounded operator on \(\mathcal K\) with trivial kernel, since \(N\cap\mathcal K=0\). The family \((Q(\lambda))\) satisfies (8.1), with adjoints taken in \(\mathcal K\): for \(\xi,\eta\in\mathcal K\), \(\langle Q(\lambda)\xi,\eta\rangle=\langle\xi,R'(\bar\lambda)\eta\rangle=\langle\xi,Q(\bar\lambda)\eta\rangle\). Lemma 8.1 gives \(H_0\).

(4) For a bounded Borel function \(f\) put \(\Phi(f)=f(H_0)P\), where \(f(H_0)\) acts on \(\mathcal K\). Then \(\Phi\) is linear, \(\|\Phi(f)\|\le\sup|f|\), and \(\Phi(fg)=\Phi(f)\Phi(g)\), because \(g(H_0)P\) maps into \(\mathcal K\), where \(P\) acts as the identity. Also \(\Phi(r_\lambda)=R'(\lambda)\) by (3). As in the proof of Theorem 7.4, the set of \(f\in C_0(\mathbb R)\) with \(f(H_j)\to\Phi(f)\) strongly is a subspace, closed under products and uniform limits, which contains every \(r_\lambda\). By Fact 1.9 it is all of \(C_0(\mathbb R)\).

(5) If \(N=0\), then \(P=1\), and (3) says that \(R_j(\lambda)\to(H_0-\lambda)^{-1}\) strongly for every \(\lambda\notin\mathbb R\). Conversely, suppose that \(H_j\to H\) in the strong resolvent sense. Each \(R'(\lambda)=(H-\lambda)^{-1}\) is then injective, so \(N=0\), and \(H=H_0\) by the uniqueness in (3). \(\square\)

**Example 8.3** (escape to infinity).

1. Let \(\mathcal H\neq0\) and \(H_n=n\cdot1\). Then \(R_n(\lambda)=(n-\lambda)^{-1}\cdot1\to0\) in norm for every \(\lambda\notin\mathbb R\), so the hypotheses of Theorem 8.2 hold with \(N=\mathcal H\). No self-adjoint operator is a strong resolvent limit of \((H_n)\), and \(f(H_n)=f(n)\to0\) for every \(f\in C_0(\mathbb R)\), as (4) predicts.
2. Let \(\mathcal H=\mathcal K\oplus\mathcal K'\), let \(K\) be self-adjoint in \(\mathcal K\), and let \(H_n=K\oplus n\cdot1\). Then \(N=\mathcal K'\), \(H_0=K\), and \(f(H_n)\to f(K)\oplus0\) for \(f\in C_0(\mathbb R)\). If \(\mathcal K'\neq0\), the unitary groups do not converge on \(\mathcal K'\) for \(t\notin2\pi\mathbb Z\): if \(e^{itn}\) converged, then \(e^{it(n+1)}-e^{itn}=e^{itn}(e^{it}-1)\to0\) would force \(e^{it}=1\).

**Example 8.4** (one half-plane is not enough). Let \(\mathcal H=\ell^2(\mathbb N_0)\) with basis \(e_0,e_1,\ldots\), and let \(S\) be the unilateral shift, \(Se_k=e_{k+1}\). For \(n\ge1\) let \(U_n\) be the unitary operator with \(U_ne_k=e_{k+1}\) for \(0\le k<n\), \(U_ne_n=-e_0\), and \(U_ne_k=-e_k\) for \(k>n\). On the span of \(e_0,\ldots,e_n\) we have \(U_n^{n+1}=-1\), so every eigenvalue \(z\) of \(U_n\) there satisfies \(z^{n+1}=-1\); on the rest \(U_n=-1\). Hence \(1-U_n\) is invertible. Put
\[
H_n=i(1+U_n)(1-U_n)^{-1}.
\]
Since \(U_n^*=U_n^{-1}\), a short computation gives \((1-U_n^*)^{-1}(1+U_n^*)=-(1-U_n)^{-1}(1+U_n)\), so \(H_n^*=H_n\): each \(H_n\) is bounded and self-adjoint. From \((H_n+i)(1-U_n)=i(1+U_n)+i(1-U_n)=2i\) we get
\[
R_n(-i)=(H_n+i)^{-1}=\frac{1-U_n}{2i},\qquad R_n(i)=R_n(-i)^*=-\frac{1-U_n^*}{2i}.
\]
For each \(k\), \(U_ne_k=e_{k+1}=Se_k\) once \(n>k\), so \(U_n\to S\) strongly, and \(R_n(-i)\to(1-S)/(2i)\) strongly. By Lemma 7.3, \(R_n(\lambda)\) converges strongly at every point of the lower half-plane. But \(U_n^*e_0=-e_n\), so \(R_n(i)e_0=-(e_0+e_n)/(2i)\) does not converge; by Lemma 7.3, \(R_n(\lambda)\) converges strongly at no point of the upper half-plane.

The limit \((1-S)/(2i)\) is injective and has dense range, since \(\ker(1-S)=0\) and \(\ker(1-S^*)=0\) in \(\ell^2\). Yet it is not the resolvent of any self-adjoint operator: resolvents of self-adjoint operators are normal, because \(R(\lambda)^*=R(\bar\lambda)\) commutes with \(R(\lambda)\), while \(S^*S=1\neq SS^*\). So Theorem 8.2 needs one point in each half-plane, and Theorem 7.4(b) needs the limit to be the resolvent of the given operator \(H\).

## 9. Inverses, logarithms and imaginary powers

For a positive self-adjoint operator \(B\) with \(\ker B=0\), the measure \(E_B\) vanishes off \((0,\infty)\) by Fact 1.8(g), so \(\log B\) is a self-adjoint operator, and \(B^{it}=e^{it\log B}\).

**Theorem 9.1.** Let \((H_j)\) be a net of self-adjoint operators converging to a self-adjoint operator \(H\) in the strong resolvent sense. Let \(W\subseteq\mathbb R\) be open and \(\varphi\colon W\to\mathbb R\) continuous, such that \(|\varphi(x)|\to\infty\) as \(x\to p\) within \(W\), for every point \(p\notin W\) that is a limit of points of \(W\). Suppose that \(E_{H_j}(\mathbb R\setminus W)=0\) for every \(j\) and \(E_H(\mathbb R\setminus W)=0\). Then \(\varphi(H_j)\to\varphi(H)\) in the strong resolvent sense, and \(e^{it\varphi(H_j)}\to e^{it\varphi(H)}\) strongly, uniformly for \(t\) in compact sets.

Here \(\varphi(H)\) means \(\psi(H)\) for the function \(\psi\) equal to \(\varphi\) on \(W\) and to \(0\) off \(W\); by Fact 1.8(b) the values off \(W\) do not matter.

**Proof.** Let \(g(x)=(\varphi(x)-i)^{-1}\) for \(x\in W\) and \(g(x)=0\) for \(x\notin W\). Then \(|g|\le1\), since \(|\varphi-i|\ge1\). The function \(g\) is continuous on \(W\). Let \(p\notin W\). If \(p\) is not a limit of points of \(W\), then \(g=0\) near \(p\). Otherwise \(|g(x)|\le1/|\varphi(x)|\to0\) as \(x\to p\) within \(W\), and \(g=0\) off \(W\). So \(g\) is bounded and continuous on \(\mathbb R\). The functions \(g\) and \((\psi-i)^{-1}\) differ only off \(W\). Since \(E_{H_j}(\mathbb R\setminus W)=0\), Fact 1.8(b) and (f), applied to the function \(r_i\), and Lemma 7.1(1) for the self-adjoint operator \(\psi(H_j)\) give \(g(H_j)=(r_i\circ\psi)(H_j)=r_i(\psi(H_j))=(\psi(H_j)-i)^{-1}\); likewise \(g(H)=(\psi(H)-i)^{-1}\). By Theorem 7.4, (a) implies (c), so \((\psi(H_j)-i)^{-1}\to(\psi(H)-i)^{-1}\) strongly. By Theorem 7.4 again, now for the operators \(\psi(H_j)\) and \(\psi(H)\), condition (b) holds, hence (a) and (e) hold. \(\square\)

**Corollary 9.2.** Suppose that \(H_j\) converges to \(H\) in the strong resolvent sense, and consider three cases.

1. If all \(H_j\) and \(H\) are positive with zero kernel, then \(\log H_j\to\log H\) in the strong resolvent sense, and \(H_j^{it}\to H^{it}\) strongly, uniformly for \(t\) in compact sets.
2. If all \(H_j\) and \(H\) have zero kernel, then \(H_j^{-1}\to H^{-1}\) in the strong resolvent sense.
3. For every continuous \(\varphi\colon\mathbb R\to\mathbb R\), \(\varphi(H_j)\to\varphi(H)\) in the strong resolvent sense.

**Proof.** (1) Take \(W=(0,\infty)\) and \(\varphi=\log\). For a positive self-adjoint \(C\) with zero kernel, \(E_C((-\infty,0])=0\) by Fact 1.8(g). The only point outside \(W\) that is a limit of points of \(W\) is \(0\), and \(|\log x|\to\infty\) as \(x\downarrow0\). Theorem 9.1 applies, and \(e^{it\log H_j}=H_j^{it}\).

(2) Take \(W=\mathbb R\setminus\{0\}\) and \(\varphi(x)=1/x\). For a self-adjoint \(C\) with zero kernel, \(E_C(\{0\})=0\) by Fact 1.8(g), and \(\varphi(C)=C^{-1}\). Indeed, with \(\varphi(0)=0\), Fact 1.8(d) gives \(\varphi(C)C=1_{\mathbb R\setminus\{0\}}(C)=1\) on \(D(C)\), and \(C\varphi(C)=1\) on \(D(\varphi(C))\); so \(\varphi(C)\) is the inverse of \(C\), with domain \(\operatorname{ran}C\).

(3) Take \(W=\mathbb R\); there is nothing to check. \(\square\)

**Example 9.3** (the limit must have zero kernel). Let \(H_n=1/n\) on \(\mathbb C\). Each \(H_n\) is positive with zero kernel, and \(H_n\to0\) in norm, hence in the strong resolvent sense. But \(H_n^{it}=n^{-it}\) has no limit for \(t\neq0\). Suppose \(n^{-it}\to c\). Then \((2n)^{-it}=2^{-it}n^{-it}\to2^{-it}c\), and also \((2n)^{-it}\to c\), so \(2^{-it}=1\) because \(|c|=1\). In the same way \(3^{-it}=1\). Then \(t\log2\) and \(t\log3\) lie in \(2\pi\mathbb Z\setminus\{0\}\), so \(\log3/\log2\) is rational, say \(p/q\) with positive integers \(p,q\); this gives \(3^q=2^p\), which is impossible. In terms of Section 8, \(\log H_n=-\log n\) escapes to \(-\infty\): its resolvents tend to \(0\).

## Exercises

**Exercise 1.** Let \(X=C[0,1]\) with the supremum norm, \(G=\mathbb C\setminus[1,\infty)\), and \(f(z)(x)=1/(1-zx)\). Show that \(f\colon G\to X\) is holomorphic. Find its Taylor series about \(0\) and about \(-1\), and show that their discs of convergence are exactly the discs \(\Delta(0,\rho(0))\) and \(\Delta(-1,\rho(-1))\) of Theorem 2.2(e).

*Solution.* If \(z\in G\) and \(x\in[0,1]\), then \(zx\neq1\): otherwise \(x\neq0\) and \(z=1/x\in[1,\infty)\). So \(f(z)\in X\). The point evaluations \(g\mapsto g(x)\) span a norming subspace of \(X^*\), and each \(z\mapsto1/(1-zx)\) is holomorphic on \(G\). For a compact \(Q\subseteq G\), the continuous function \((z,x)\mapsto|1-zx|\) is positive on the compact set \(Q\times[0,1]\), hence at least some \(c>0\); so \(\|f(z)\|\le1/c\) on \(Q\). Theorem 2.2(d) applies.

About \(0\): \(\rho(0)=1\), and \(f(z)=\sum_nz^nx^n\), where \(x^n\) denotes the monomial, which has norm \(1\). The terms have norm \(|z|^n\), so the series converges exactly for \(|z|<1\). About \(-1\): \(\rho(-1)=\operatorname{dist}(-1,[1,\infty))=2\). Since \(1-zx=(1+x)\big(1-(z+1)x/(1+x)\big)\),
\[
f(z)=\sum_n(z+1)^n\frac{x^n}{(1+x)^{n+1}}\qquad(|z+1|<2),
\]
the geometric series converging uniformly in \(x\) because \(|(z+1)x/(1+x)|\le|z+1|/2<1\). For \(n\ge1\) the function \(x^n/(1+x)^{n+1}\) has derivative \(x^{n-1}(n-x)(1+x)^{-n-2}\ge0\) on \([0,1]\), so its maximum is its value \(2^{-n-1}\) at \(x=1\). So for \(n\ge1\) the \(n\)-th term has norm \(|z+1|^n2^{-n-1}\), which does not tend to zero when \(|z+1|\ge2\). The disc of convergence is exactly \(\Delta(-1,2)\).

**Exercise 2.** Let \(H\) be self-adjoint, \(\xi\in\mathcal H\) and \(s>0\). Show that \(\xi\) is an analytic vector of \(H\) with \(r(\xi)\ge s\) if and only if \(\xi\in D(e^{\tau|H|})\) for every \(0<\tau<s\). Deduce that \(\xi\) is entire if and only if \(\xi\in D(e^{\tau|H|})\) for every \(\tau>0\). For \((Hx)_k=kx_k\) on \(\ell^2(\mathbb N)\) and \(\xi=(e^{-k})_{k\ge1}\), find \(r(\xi)\).

*Solution.* Here \(e^{\tau|H|}\) is the function \(e^{\tau|\lambda|}\) of \(H\), and by Corollary 5.2, \(\xi\in D(H^k)\) if and only if \(\int\lambda^{2k}d\mu_\xi<\infty\), with \(\|H^k\xi\|^2=\int\lambda^{2k}d\mu_\xi\).

Suppose \(\xi\in D(e^{\tau|H|})\) for every \(\tau<s\). Fix \(0<\sigma<\tau<s\). From \(e^{\tau|\lambda|}\ge(\tau|\lambda|)^k/k!\) we get \(|\lambda|^k\le k!\,\tau^{-k}e^{\tau|\lambda|}\), so \(\xi\in D(H^k)\) and \(\|H^k\xi\|\le k!\,\tau^{-k}\|e^{\tau|H|}\xi\|\). Then \(\sum_k\sigma^k\|H^k\xi\|/k!\le\|e^{\tau|H|}\xi\|\sum_k(\sigma/\tau)^k<\infty\). So \(\xi\) is analytic with \(r(\xi)\ge\sigma\), and letting \(\sigma\uparrow s\) gives \(r(\xi)\ge s\).

Conversely let \(r(\xi)\ge s\) and \(0<\tau<s\), so \(C=\sum_k\tau^k\|H^k\xi\|/k!<\infty\). The partial sums \(q_m(\lambda)=\sum_{k\le m}\tau^k|\lambda|^k/k!\) increase to \(e^{\tau|\lambda|}\). In \(L^2(\mu_\xi)\) the triangle inequality gives \(\|q_m\|_{L^2(\mu_\xi)}\le\sum_{k\le m}\tau^k\|H^k\xi\|/k!\le C\). By monotone convergence, \(\int e^{2\tau|\lambda|}d\mu_\xi\le C^2\), so \(\xi\in D(e^{\tau|H|})\). The statement about entire vectors follows by letting \(s\to\infty\).

For the example, \(\|e^{\tau|H|}\xi\|^2=\sum_ke^{2\tau k}e^{-2k}\), which is finite exactly when \(\tau<1\). By the criterion, \(r(\xi)\ge1\); and \(r(\xi)>1\) is impossible, since it would put \(\xi\) into \(D(e^{\tau|H|})\) for some \(\tau>1\). So \(r(\xi)=1\).

**Exercise 3.** Let \(A\) be the generator of a strongly continuous semigroup \((T_t)_{t\ge0}\) on \(X\). Show that \(D(A^2)=\{x\in D(A) : Ax\in D(A)\}\) is a core for \(A\).

*Solution.* By Theorem 5.1(1) it suffices to show two things: \(D(A^2)\) is dense in \(X\), and every \(T_t\) maps it into itself. Invariance: if \(x\in D(A^2)\), then \(T_tx\in D(A)\) and \(AT_tx=T_tAx\), which lies in \(D(A)\) because \(Ax\in D(A)\) (Proposition 3.3(4)); so \(T_tx\in D(A^2)\). Density: let \(x\in X\) and \(\varepsilon,\delta>0\). The vector \(y=J_\varepsilon x\) lies in \(D(A)\) with \(Ay=T_\varepsilon x-x\) (Proposition 3.3(2)). Then \(J_\delta y\in D(A)\), and by Proposition 3.3(4), \(AJ_\delta y=J_\delta Ay\), which lies in \(D(A)\) by Proposition 3.3(2). So \(J_\delta J_\varepsilon x\in D(A^2)\). Finally,
\[
\big\|\delta^{-1}\varepsilon^{-1}J_\delta J_\varepsilon x-x\big\|\le\big\|\delta^{-1}J_\delta\big\|\,\big\|\varepsilon^{-1}J_\varepsilon x-x\big\|+\big\|\delta^{-1}J_\delta x-x\big\|,
\]
where \(\|\delta^{-1}J_\delta\|\le\sup_{0\le s\le1}\|T_s\|\) for \(\delta\le1\). By Proposition 3.3(3) the right side tends to \(0\) as \(\varepsilon\downarrow0\) and then \(\delta\downarrow0\).

**Exercise 4.** Let \(H_j\to H\) in the strong resolvent sense, and let \(a<b\) be real numbers with \(E_H(\{a\})=E_H(\{b\})=0\). Show that \(E_{H_j}((a,b))\to E_H((a,b))\) strongly. Show by an example that the condition on \(a\) and \(b\) cannot be dropped.

*Solution.* Let \(u_k(x)=\min(1,k\operatorname{dist}(x,\mathbb R\setminus(a,b)))\) and \(v_k(x)=\max(0,1-k\operatorname{dist}(x,[a,b]))\). These are continuous, \(0\le u_k\le1_{(a,b)}\le1_{[a,b]}\le v_k\le1\), \(u_k\uparrow1_{(a,b)}\) and \(v_k\downarrow1_{[a,b]}\) pointwise. Write \(P_j=E_{H_j}((a,b))\) and \(P=E_H((a,b))\). By Fact 1.8(c), for every \(\xi\),
\[
\langle u_k(H_j)\xi,\xi\rangle\le\langle P_j\xi,\xi\rangle\le\langle v_k(H_j)\xi,\xi\rangle .
\]
By Theorem 7.4(c), letting \(j\) run gives
\[
\langle u_k(H)\xi,\xi\rangle\le\liminf_j\langle P_j\xi,\xi\rangle\le\limsup_j\langle P_j\xi,\xi\rangle\le\langle v_k(H)\xi,\xi\rangle .
\]
As \(k\to\infty\), dominated convergence for the finite measure \(\mu_\xi\) (Fact 1.7) turns the outer terms into \(\mu_\xi((a,b))\) and \(\mu_\xi([a,b])\), which are equal because \(E_H(\{a\})=E_H(\{b\})=0\). So \(\langle P_j\xi,\xi\rangle\to\langle P\xi,\xi\rangle\) for every \(\xi\). By polarization, \(\langle Y\xi,\eta\rangle=\frac14\sum_{m=0}^3i^m\langle Y(\xi+i^m\eta),\xi+i^m\eta\rangle\), so \(P_j\to P\) weakly. Since \(\|P_j\xi\|^2=\langle P_j\xi,\xi\rangle\to\langle P\xi,\xi\rangle=\|P\xi\|^2\), Lemma 7.2(3) gives strong convergence. For the example take \(H_n=1/n\) on \(\mathbb C\) and \((a,b)=(0,1)\): then \(E_{H_n}((0,1))=1\) for every \(n\ge2\), while \(E_0((0,1))=0\); here \(a=0\) is an eigenvalue of the limit.

**Exercise 5.** Show that in Theorem 7.4, (d) does not imply (a) for nets. Use a net of real numbers \(h_\alpha\) with \(h_\alpha\to\infty\) and \(e^{ith_\alpha}\to1\) for every real \(t\).

*Solution.* We first prove Dirichlet's approximation theorem in the form needed. Let \(\theta_1,\ldots,\theta_m\) be real and \(Q\ge1\) an integer. Consider the \(Q^m+1\) points \((\{l\theta_1\},\ldots,\{l\theta_m\})\), \(l=0,\ldots,Q^m\), of the cube \([0,1)^m\), where \(\{y\}\) is the fractional part of \(y\). Cut the cube into \(Q^m\) boxes of side \(1/Q\). Two of the points, for \(l<l'\), lie in the same box, so \(q=l'-l\) is an integer with \(1\le q\le Q^m\) such that every \(q\theta_k\) lies within \(1/Q\) of an integer.

Let \(\Lambda\) be the set of pairs \(\alpha=(F,Q)\), with \(F\subseteq\mathbb R\) finite and \(Q\ge1\) an integer, ordered by \((F,Q)\le(F',Q')\) if \(F\subseteq F'\) and \(Q\le Q'\). This is a directed set. For \(\alpha=(F,Q)\) with \(F=\{t_1,\ldots,t_m\}\), apply the previous paragraph to \(\theta_k=Qt_k/(2\pi)\), and put \(h_\alpha=qQ\); if \(F\) is empty, put \(h_\alpha=Q\). Then \(h_\alpha\ge Q\), and \(t_kh_\alpha/(2\pi)=q\theta_k\) lies within \(1/Q\) of an integer, so \(|e^{it_kh_\alpha}-1|\le2\pi/Q\) for \(t_k\in F\). Given \(t\) and \(\varepsilon>0\), choose \(Q_0\) with \(2\pi/Q_0<\varepsilon\); for \(\alpha\ge(\{t\},Q_0)\) we have \(|e^{ith_\alpha}-1|<\varepsilon\). So \(e^{ith_\alpha}\to1\) for every \(t\), and \(h_\alpha\to\infty\).

Now let \(H_\alpha=h_\alpha\) and \(H=0\) on \(\mathbb C\). Then \(e^{itH_\alpha}\to1=e^{itH}\) for every \(t\), so (d) holds. But \(R_\alpha(i)=(h_\alpha-i)^{-1}\to0\), while \(R(i)=(0-i)^{-1}=i\). So (a) fails. By Theorem 7.4, condition (e) fails as well: the convergence \(e^{ith_\alpha}\to1\) is not uniform on compact sets.

## References



- [McMullen] C. T. McMullen, *Advanced Complex Analysis*, course notes for Mathematics 213a, Harvard University, version of
  2 December 2025. Free at https://people.math.harvard.edu/~ctm/papers/home/text/class/harvard/213a/course/course.pdf
- [Trotter 1958] H. F. Trotter, Approximation of semi-groups of operators, *Pacific Journal of Mathematics* 8 (1958), 887–919. Openly available from the journal's archive. Free at https://doi.org/10.2140/pjm.1958.8.887
- [Dunford 1938] N. Dunford, Uniformity in linear spaces, *Transactions of the American Mathematical Society* 44 (1938), 304–356. Free at https://www.ams.org/journals/tran/1938-044-02/S0002-9947-1938-1501971-X/
- [van Neerven] J. van Neerven, *Functional Analysis*, Cambridge Studies in Advanced Mathematics 201, Cambridge University Press,
  2022; arXiv:2112.11166, version 7 (17 July 2025). Free at https://arxiv.org/abs/2112.11166
- [Lebl CA] J. Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*, version 1.9 (11 July 2026), open textbook under CC BY-SA 4.0 and CC BY-NC-SA 4.0, [www.jirka.org/ca](https://www.jirka.org/ca/). It is the text of the core course *Complex Analysis*.
- [Lebl RA] J. Lebl, *Basic Analysis I* and *Basic Analysis II: Introduction to Real Analysis*, version 6.3 (15 May 2026), open textbook under CC BY-SA 4.0 and CC BY-NC-SA 4.0, [www.jirka.org/ra](https://www.jirka.org/ra/). It is the text of the core courses *Real Analysis I* and *Real Analysis II*.

- [Stone 1930] M. H. Stone, Linear transformations in Hilbert space. III. Operational methods and group theory, *Proceedings
  of the National Academy of Sciences of the U.S.A.* 16 (1930), 172–175. Free at
  https://pmc.ncbi.nlm.nih.gov/articles/PMC1075964/
- [Teschl] G. Teschl, *Mathematical Methods in Quantum Mechanics, with Applications to Schrödinger Operators*, Graduate
  Studies in Mathematics 99, American Mathematical Society, 2009; online edition free from the author:
  https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf
