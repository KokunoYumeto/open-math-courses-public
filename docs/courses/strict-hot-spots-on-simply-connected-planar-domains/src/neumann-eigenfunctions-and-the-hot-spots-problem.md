# Neumann eigenfunctions and the hot-spots problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Heat in an insulated plate tends to a constant temperature, and for large times the difference from that constant is governed by an eigenfunction of the first positive eigenvalue of the Laplacian with Neumann boundary conditions. Rauch's hot-spots conjecture of 1974 says that such an eigenfunction attains its maximum on the boundary. In this generality the conjecture is false: planar counterexamples with two holes, and later with one hole, are known [Bur05, Section 1 and Theorem 1.1], and convex counterexamples exist in all sufficiently large dimensions [dDP24]. Burdzy conjectured that it holds for every simply connected planar domain [Bur05, Conjecture 1.2(ii)].

This course proves the theorem of [OpenAI-HS]: on a bounded simply connected planar domain with smooth boundary, no eigenfunction of the first positive Neumann eigenvalue has a critical point inside the domain, and consequently every such eigenfunction attains its maximum and its minimum only on the boundary. The eigenvalue may be multiple; the statement holds for every eigenfunction. The proof assumes standard facts on Sobolev spaces and elliptic regularity of smooth domains, stated precisely in Section 1 as named hypotheses; everything else is proved in the course or in earlier lessons of the programme.

This lesson fixes the setting and the analytic facts used throughout, constructs the two eigenvalue problems, proves the strict inequality between the first positive Neumann eigenvalue and the first Dirichlet eigenvalue, and states the theorem.

- The setting and the named analytic facts (Section 1).
- Green's formulas and Poincaré inequalities (Section 2).
- The Dirichlet and Neumann eigenvalue problems (Section 3).
- The gap between the two eigenvalues (Section 4).
- The theorem and the plan of its proof (Section 5).

## 1. Setting and named analytic facts

Throughout, \(\Omega\subset\mathbb R^2\) is a nonempty bounded open set with \(C^\infty\) boundary: every boundary point \(x_0\) has a neighbourhood \(U\) in which, after a rotation and translation of coordinates taking \(x_0\) to \(0\), \(U\) is an open rectangle \((-a,a)\times(-b,b)\) and
\[
\Omega\cap U=\{(x_1,x_2)\in U:x_2>\gamma(x_1)\}
\]
for a \(C^\infty\) function \(\gamma\) with \(\gamma(0)=\gamma'(0)=0\) and \(|\gamma|<b/2\). Such coordinates are called a *boundary chart* at \(x_0\). We assume that \(\Omega\) is *simply connected*: it is connected and every closed path in \(\Omega\) is homotopic in \(\Omega\) to a constant path. The plane is identified with \(\mathbb C\) whenever convenient.

We write \(\nu\) for the outward unit normal on \(\partial\Omega\), \(\tau=i\nu\) for the unit tangent that keeps \(\Omega\) on its left, and \(ds\) for arclength on \(\partial\Omega\). A function belongs to \(C^\infty(\overline\Omega)\) if it is \(C^\infty\) in \(\Omega\) and each of its partial derivatives extends continuously to \(\overline\Omega\). For an integer \(k\ge0\), \(H^k(\Omega)\) is the space of real functions in \(L^2(\Omega)\) whose weak derivatives of order at most \(k\) lie in \(L^2(\Omega)\), and \(H^1_0(\Omega)\) is the closure of \(C^\infty_c(\Omega)\) in \(H^1(\Omega)\). Norms without a subscript are \(L^2(\Omega)\) norms.

Two groups of standard facts about such domains are used without proof in this course. They are named hypotheses of the course; the parts proved elsewhere in the programme are indicated.

**(SOB) Sobolev facts.**

1. (Gauss–Green.) \(\int_U\operatorname{div}V\,dx=\int_{\partial U}V\cdot\nu\,ds\) for every bounded open set \(U\subset\mathbb R^2\) with \(C^1\) boundary and every \(V\in C^1(\overline U;\mathbb R^2)\); we use it for \(\Omega\) and for \(\Omega\) with finitely many small closed discs removed.
2. (Density and trace.) \(C^\infty(\overline\Omega)\) is dense in \(H^k(\Omega)\) for every \(k\ge1\). Restriction to \(\partial\Omega\) extends from \(C^\infty(\overline\Omega)\) to a bounded linear map \(\operatorname{tr}\colon H^1(\Omega)\to L^2(\partial\Omega)\); its kernel is \(H^1_0(\Omega)\) and its range is dense in \(L^2(\partial\Omega)\).
3. (Rellich.) The inclusion \(H^1(\Omega)\to L^2(\Omega)\) is compact.
4. (Sobolev embedding.) \(H^{k+2}(\Omega)\subseteq C^k(\overline\Omega)\) for \(k\ge0\), with continuous inclusion: every element has a representative whose derivatives of order at most \(k\) extend continuously to \(\overline\Omega\).

Statements 2–4 are Theorems 3.3, 5.5, 5.8 and 4.2 of Chapter II of [Sho94]; statement 1 is the classical divergence theorem. The zero-trace space is described in the programme for \(C^1\) boundaries in Section 2 of [Boundary energy, local inverses, and harmonic data](course:elliptic-operators-and-boundary-problems/second-order-boundary), where (B6) identifies \(H^1_0(\Omega)\) with the functions of zero trace.

**(ER) Elliptic regularity.** Let \(k\ge0\) and \(f\in H^k(\Omega)\).

- (D) If \(w\in H^1_0(\Omega)\) and \(\int_\Omega\nabla w\cdot\nabla\phi=\int_\Omega f\phi\) for all \(\phi\in H^1_0(\Omega)\), then \(w\in H^{k+2}(\Omega)\).
- (N) If \(w\in H^1(\Omega)\) and \(\int_\Omega\nabla w\cdot\nabla\phi=\int_\Omega f\phi\) for all \(\phi\in H^1(\Omega)\), then \(w\in H^{k+2}(\Omega)\).

These are Theorems 6.1, 6.4 and 6.5 of Chapter III of [Sho94]. The programme proves the existence and uniqueness of the solution in (D) for every \(f\in L^2(\Omega)\) and every bounded open set ((B10) of [Boundary energy, local inverses, and harmonic data](course:elliptic-operators-and-boundary-problems/second-order-boundary)), the case \(k=0\) of (D), and the case of (D) with \(f\in C^\infty(\overline\Omega)\), where \(w\in C^\infty(\overline\Omega)\) ((B29) there). The Neumann statement (N) and the intermediate orders of (D) are not proved in the programme.

Three further results are proved in other lessons of the programme and are used freely:

- Solutions of elliptic equations with constant coefficients are real analytic: if \(P\) is an elliptic polynomial and \(u\) is a distribution on an open set with \(P(D)u=0\), then \(u\) is a real-analytic function ([Anisotropic derivative classes and analyticity](course:constant-coefficient-equations-and-solvability/AN02-L031), Theorem 3.1). We use it for \(\Delta+\mu\) with a constant \(\mu\), whose symbol \(\mu-|\xi|^2\) has the elliptic principal part \(-|\xi|^2\).
- A holomorphic function on a simply connected domain has a primitive, and a zero-free one has a holomorphic logarithm; real parts of holomorphic functions satisfy the mean-value property and the maximum principle; the argument principle and Rouché's theorem hold on bounded regions with piecewise smooth boundary ([Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01), Appendix A, Lemmas A.2 and A.3).
- The Riesz–Fréchet theorem and the projection theorem in Hilbert spaces ([Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators), Theorems 2.2 and 2.3).

A real-analytic function on a connected open set that vanishes on a nonempty open subset vanishes identically: the set of points at which all its derivatives vanish is closed by continuity, open because the function is given by its Taylor series near each point, and nonempty.

## 2. Green's formulas and Poincaré inequalities

For \(u\in H^2(\Omega)\) put \(\partial_\nu u=\operatorname{tr}(\nabla u)\cdot\nu\), using the trace of each component of \(\nabla u\in H^1(\Omega;\mathbb R^2)\).

**Lemma 2.1** (Green's formulas). For \(X\in H^1(\Omega;\mathbb R^2)\) and \(\phi\in H^1(\Omega)\),
\[
\begin{aligned}
&\int_\Omega(\operatorname{div}X)\phi+\int_\Omega X\cdot\nabla\phi\\
&\quad=\int_{\partial\Omega}(\operatorname{tr}X\cdot\nu)\operatorname{tr}\phi\,ds.
\end{aligned} \tag{2.1}
\]
In particular, for \(u\in H^2(\Omega)\),
\[
\begin{aligned}
&\int_\Omega(\Delta u)\phi+\int_\Omega\nabla u\cdot\nabla\phi\\
&\quad=\int_{\partial\Omega}(\partial_\nu u)\operatorname{tr}\phi\,ds.
\end{aligned} \tag{2.2}
\]

*Proof.* For \(X\) and \(\phi\) in \(C^\infty(\overline\Omega)\), (2.1) is (SOB 1) applied to \(V=\phi X\). Both sides of (2.1) are continuous on \(H^1\times H^1\): the boundary side because \(\operatorname{tr}\) is bounded into \(L^2(\partial\Omega)\) and the product of two \(L^2(\partial\Omega)\) functions is integrable. Density (SOB 2) gives the general case. Formula (2.2) is (2.1) with \(X=\nabla u\). \(\square\)

**Lemma 2.2.** If \(u\in H^1(\Omega)\) and \(\nabla u=0\), then \(u\) is almost everywhere equal to a constant.

*Proof.* Let \(B\) be a disc with \(\overline{2B}\subseteq\Omega\), where \(2B\) is the concentric disc of twice the radius, and let \(\rho_\varepsilon\) be a standard mollifier with \(\varepsilon\) smaller than the radius of \(B\). On \(B\) the function \(u*\rho_\varepsilon\) is smooth with gradient \((\nabla u)*\rho_\varepsilon=0\), hence constant, and it converges to \(u\) in \(L^2(B)\). So \(u\) is a.e. constant on every such disc. The set of points of \(\Omega\) near which \(u\) is a.e. equal to a given constant \(c\) is open, and by the same statement on overlapping discs its complement in \(\Omega\) is open too. Since \(\Omega\) is connected, one such set is all of \(\Omega\). \(\square\)

**Lemma 2.3** (Poincaré inequalities).

1. There is \(C\) with \(\|\phi\|\le C\|\nabla\phi\|\) for all \(\phi\in H^1_0(\Omega)\).
2. For every disc \(B\) with \(\overline B\subseteq\Omega\) there is \(C_B\) with \(\|u\|\le C_B(\|\nabla u\|+|u_B|)\) for all \(u\in H^1(\Omega)\), where \(u_B\) is the mean of \(u\) over \(B\). The same holds with the mean of \(u\) over \(\Omega\) in place of \(u_B\); in particular \(\|u\|\le C\|\nabla u\|\) when \(\int_\Omega u=0\).

*Proof.* Statement 1 is (B11) of [Boundary energy, local inverses, and harmonic data](course:elliptic-operators-and-boundary-problems/second-order-boundary): if \(|x_1|\le R\) on \(\Omega\), then \(\|\phi\|\le2R\|\partial_1\phi\|\).

For statement 2 suppose the contrary. Then there are \(u_n\) with \(\|u_n\|=1\) and \(\|\nabla u_n\|+|(u_n)_B|\to0\). By (SOB 3) a subsequence converges in \(L^2(\Omega)\) to some \(u\) with \(\|u\|=1\). Since \(\nabla u_n\to0\) in \(L^2\), the subsequence is Cauchy in \(H^1(\Omega)\), so \(u\in H^1(\Omega)\) and \(\nabla u=0\). By Lemma 2.2, \(u\) is a constant \(c\), and \(c=u_B=\lim(u_n)_B=0\), contradicting \(\|u\|=1\). The argument with the mean over \(\Omega\) is identical. \(\square\)

## 3. The Dirichlet and Neumann eigenvalue problems

With the Rayleigh quotient \(\mathcal R(w)=\int_\Omega|\nabla w|^2/\int_\Omega w^2\) of a nonzero \(w\in H^1(\Omega)\), and the subspace \(H^1_m(\Omega)\) of mean-zero functions in \(H^1(\Omega)\), define
\[
\begin{gathered}
\lambda_D=\inf\{\mathcal R(\phi):0\ne\phi\in H^1_0(\Omega)\},\\
\mu=\inf\{\mathcal R(v):0\ne v\in H^1_m(\Omega)\}.
\end{gathered}
\]
Let \(V\) be the space of real \(v\in H^1(\Omega)\) with
\[
\begin{gathered}
\int_\Omega\nabla v\cdot\nabla\phi=\mu\int_\Omega v\phi\\
(\phi\in H^1(\Omega)).
\end{gathered} \tag{3.1}
\]
Taking \(\phi=1\) shows \(\int_\Omega v=0\) for \(v\in V\), since \(\mu>0\) (Proposition 3.1). We call \(\mu\) the *first positive Neumann eigenvalue* and \(V\) its *eigenspace*; sources that count the constant eigenfunction first write \(\mu_2\) for \(\mu\). A *Dirichlet eigenfunction* for \(\lambda_D\) is a \(\phi\in H^1_0(\Omega)\) with \(\int\nabla\phi\cdot\nabla\psi=\lambda_D\int\phi\psi\) for all \(\psi\in H^1_0(\Omega)\).

**Proposition 3.1.**

1. \(\lambda_D>0\) and \(\mu>0\), and both infima are attained.
2. A function \(0\ne v\in H^1(\Omega)\) with \(\int v=0\) attains \(\mu\) if and only if \(v\in V\). A function \(0\ne\phi\in H^1_0(\Omega)\) attains \(\lambda_D\) if and only if it is a Dirichlet eigenfunction for \(\lambda_D\).
3. \(V\) is finite-dimensional, nonzero, and contained in \(C^\infty(\overline\Omega)\). Every \(v\in V\) satisfies \(\Delta v+\mu v=0\) in \(\Omega\) and \(\partial_\nu v=0\) on \(\partial\Omega\). Every Dirichlet eigenfunction \(\phi\) for \(\lambda_D\) lies in \(C^\infty(\overline\Omega)\) and satisfies \(\Delta\phi+\lambda_D\phi=0\) in \(\Omega\) and \(\phi=0\) on \(\partial\Omega\).
4. Every \(v\in V\) is real analytic in \(\Omega\). If \(v\in V\) vanishes on a nonempty open subset of \(\Omega\), then \(v=0\).

*Proof.* (1) Positivity follows from Lemma 2.3. Let \(v_n\) be mean-zero functions with \(\|v_n\|=1\) and \(\|\nabla v_n\|^2\to\mu\). By (SOB 3) a subsequence, still written \(v_n\), converges in \(L^2\) to some \(v\) with \(\|v\|=1\) and \(\int v=0\). With \(a_n=\|\nabla v_n\|^2\), the parallelogram law and the definition of \(\mu\), applied to the mean-zero function \((v_n+v_m)/2\), give
\[
\begin{aligned}
&\Bigl\|\nabla\frac{v_n-v_m}2\Bigr\|^2\\
&\quad=\frac{a_n+a_m}2-\Bigl\|\nabla\frac{v_n+v_m}2\Bigr\|^2\\
&\quad\le\frac{a_n+a_m}2-\mu\Bigl\|\frac{v_n+v_m}2\Bigr\|^2,
\end{aligned}
\]
and the right side tends to \(\mu-\mu\|v\|^2=0\). So \((v_n)\) is Cauchy in \(H^1(\Omega)\), its limit is \(v\), and \(\|\nabla v\|^2=\mu\). The same argument in the closed subspace \(H^1_0(\Omega)\) gives a minimizer for \(\lambda_D\).

(2) If \(v\) attains \(\mu\) and \(\phi\in H^1(\Omega)\) has mean zero, the quotient of \(v+t\phi\) is minimal at \(t=0\), and the vanishing of its derivative there is (3.1) for \(\phi\). For general \(\phi\), apply this to \(\phi\) minus its mean and use \(\int v=0\). Conversely, \(\phi=v\) in (3.1) gives \(\|\nabla v\|^2=\mu\|v\|^2\). The Dirichlet statement is proved in the same way within \(H^1_0(\Omega)\).

(3) By (1) and (2), \(V\ne0\). The space \(V\) is closed in \(H^1(\Omega)\) and \(\|\nabla v\|^2=\mu\|v\|^2\) on it. If it were infinite-dimensional, Gram–Schmidt in \(L^2\) would give \(e_n\in V\) with \(\|e_n-e_m\|^2=2\) for \(n\ne m\) and \(\|e_n\|_{H^1}^2=1+\mu\), contradicting (SOB 3). For \(v\in V\), (ER N) with \(k=1\) and \(f=\mu v\in H^1(\Omega)\) gives \(v\in H^3(\Omega)\); then \(f\in H^3(\Omega)\) and \(v\in H^5(\Omega)\), and so on. By (SOB 4), \(v\in C^\infty(\overline\Omega)\). Formula (2.2) with \(\phi\in C^\infty_c(\Omega)\) and (3.1) give \(\int(\Delta v+\mu v)\phi=0\), so \(\Delta v+\mu v=0\) in \(\Omega\). Then (2.2) with \(\phi\in C^\infty(\overline\Omega)\) gives \(\int_{\partial\Omega}(\partial_\nu v)\phi\,ds=0\); since these traces are dense in \(L^2(\partial\Omega)\), \(\partial_\nu v=0\). The Dirichlet statements follow in the same way from (ER D), and \(\phi=0\) on \(\partial\Omega\) because \(\phi\) is continuous on \(\overline\Omega\) with zero trace.

(4) By (3), \((\Delta+\mu)v=0\) in \(\Omega\) classically, hence in the sense of distributions, and the analyticity theorem quoted in Section 1 applies. The second statement follows because \(\Omega\) is connected. \(\square\)

**Lemma 3.2.** There is a Dirichlet eigenfunction \(\phi\) for \(\lambda_D\) with \(\phi\ge0\) and \(\int_\Omega\phi>0\).

*Proof.* Let \(\psi\) be a Dirichlet eigenfunction for \(\lambda_D\); it lies in \(C^\infty(\overline\Omega)\) and vanishes on \(\partial\Omega\). For \(\delta>0\) put \(G_\delta(t)=\sqrt{t^2+\delta^2}-\delta\). Then \(G_\delta(\psi)\in C^\infty(\overline\Omega)\) vanishes on \(\partial\Omega\), so it lies in \(H^1_0(\Omega)\) by (SOB 2). As \(\delta\to0\), \(G_\delta(\psi)\to|\psi|\) uniformly and \(\nabla G_\delta(\psi)=G_\delta'(\psi)\nabla\psi\to\operatorname{sgn}(\psi)\nabla\psi\) in \(L^2\), by dominated convergence. Hence \(|\psi|\in H^1_0(\Omega)\), and \(|\nabla|\psi||=|\nabla\psi|\) almost everywhere, because the set where \(\psi=0\) and \(\nabla\psi\ne0\) is locally a smooth curve, of measure zero. So \(|\psi|\) attains \(\lambda_D\), and \(\phi=|\psi|\) is a Dirichlet eigenfunction by Proposition 3.1(2). It is nonnegative and nonzero, so \(\int\phi>0\). \(\square\)

## 4. The gap between the two eigenvalues

The inequality below is the first case of the comparison of Friedlander and Filonov. The argument with plane waves is Filonov's [Fil04]; its strict form is needed later, where it identifies the equality case of a vector variational principle.

**Proposition 4.1.** \(\mu<\lambda_D\).

*Proof.* Work temporarily with complex-valued functions and the Hermitian form
\[
Q(w)=\int_\Omega|\nabla w|^2-\lambda_D\int_\Omega|w|^2,
\]
with polarization \(Q(w,z)\). For a real-valued \(w\), \(Q(w)\ge(\mu-\lambda_D)\|w\|^2\) if \(\int w=0\), by the definition of \(\mu\); and for complex \(w\), \(Q(w)=Q(\operatorname{Re}w)+Q(\operatorname{Im}w)\).

Let \(\phi\) be as in Lemma 3.2. For \(k\in\mathbb R^2\) with \(|k|^2=\lambda_D\) put \(e_k(x)=e^{ik\cdot x}\) and
\[
w_k=e_k-c_k\phi,\qquad c_k=\frac{\int_\Omega e_k}{\int_\Omega\phi}.
\]
Each \(w_k\) has mean zero. Since \(|\nabla e_k|^2=|k|^2=\lambda_D\) and \(|e_k|=1\), \(Q(e_k)=0\). Since \(\phi\) attains \(\lambda_D\), \(Q(\phi)=0\). Since \(-\Delta e_k=\lambda_De_k\) and \(\phi\in H^1_0(\Omega)\), integration by parts against approximants of \(\phi\) in \(C^\infty_c(\Omega)\) gives \(Q(e_k,\phi)=\int(-\Delta e_k-\lambda_De_k)\phi=0\). Hence \(Q(w_k)=0\), and so
\[
\begin{aligned}
&Q(\operatorname{Re}w_k)\\
&\quad+Q(\operatorname{Im}w_k)=0.
\end{aligned} \tag{4.1}
\]

Suppose \(\mu>\lambda_D\). Both terms of (4.1) are at least \((\mu-\lambda_D)\) times the squared norms of the real mean-zero functions \(\operatorname{Re}w_k\), \(\operatorname{Im}w_k\), so \(w_k=0\), that is, \(e_k=c_k\phi\). This is impossible: \(|e_k|=1\) everywhere, while \(\phi\) is continuous on \(\overline\Omega\) and vanishes on \(\partial\Omega\). Hence \(\mu\le\lambda_D\).

Suppose \(\mu=\lambda_D\). Then both terms of (4.1) are nonnegative, hence zero. A real mean-zero function \(w\) with \(Q(w)=0\) is zero or attains \(\mu\); by Proposition 3.1(2), \(\operatorname{Re}w_k\) and \(\operatorname{Im}w_k\) belong to \(V\). Thus every \(e_k\) with \(|k|^2=\lambda_D\) lies in the complex span \(W\) of \(V\) and \(\phi\), whose dimension is at most \(\dim V+1<\infty\). But plane waves with distinct frequencies are linearly independent on \(\Omega\): if \(\sum_{j=1}^na_je_{k_j}=0\) on \(\Omega\) with distinct \(k_j\), choose \(x_0\in\Omega\) and a unit vector \(e\) with the numbers \(k_j\cdot e\) distinct; differentiating \(t\mapsto\sum_ja_je^{ik_j\cdot x_0}e^{it\,k_j\cdot e}\) at \(t=0\) up to order \(n-1\) gives a Vandermonde system with distinct nodes \(ik_j\cdot e\), so all \(a_j=0\). The circle \(|k|^2=\lambda_D\) contains infinitely many points, which contradicts \(\dim W<\infty\). \(\square\)

## 5. The theorem

**Theorem 5.1** ([OpenAI-HS, Theorem 1.1]). Let \(\Omega\subset\mathbb R^2\) be a nonempty bounded simply connected open set with \(C^\infty\) boundary. For every \(0\ne u\in V\),
\[
\nabla u(x)\ne0\qquad(x\in\Omega).
\]

**Corollary 5.2** (strict hot spots). For every \(0\ne u\in V\) and every \(x\in\Omega\),
\[
\min_{\partial\Omega}u<u(x)<\max_{\partial\Omega}u.
\]

*Proof from Theorem 5.1.* The function \(u\) is continuous on the compact set \(\overline\Omega\) and attains its maximum and minimum there. An interior extremum would be a critical point, so the maximum of \(u\) over \(\overline\Omega\) equals its maximum over \(\partial\Omega\), and likewise for the minimum. If \(u(x)\) equalled one of them for some \(x\in\Omega\), then \(x\) would be an interior extremum. \(\square\)

The theorem is stronger than the corollary: it also excludes interior saddle points. It applies to every element of \(V\) without any assumption on \(\dim V\); Proposition 5.2 of [Conformal coordinates, Hopf's lemma and boundary signs](conformal-coordinates-hopfs-lemma-and-boundary-signs.md) shows \(\dim V\le2\), and this bound is used in the proof.

*The plan of the proof.* Each Cartesian derivative of \(u\) solves the same equation \(\Delta w+\mu w=0\), but its boundary values have no fixed sign. The Neumann condition relates the two derivatives: the vector \(\nabla u\) is tangent to \(\partial\Omega\). The lessons use this constraint as follows.

1. [Conformal coordinates, Hopf's lemma and boundary signs](conformal-coordinates-hopfs-lemma-and-boundary-signs.md) parametrizes \(\Omega\) by the unit disc through a conformal map that is smooth up to the boundary, and proves \(\dim V\le2\) from the sign pattern of eigenfunctions on the boundary.
2. [A variational principle for tangent vector fields](a-variational-principle-for-tangent-vector-fields.md) proves Rohleder's principle: for tangent vector fields \(X\), \(\int(|\operatorname{div}X|^2+|\operatorname{curl}X|^2)\ge\mu\int|X|^2\), with equality exactly for gradients of elements of \(V\).
3. [Boundary kernels and the multiplier identity](boundary-kernels-and-the-multiplier-identity.md) transfers the resulting nonnegative energy to a quadratic form \(E\) on boundary data on the circle and proves the multiplier identity: for the boundary gradient \(g\) of \(u\) and real Lipschitz multipliers \(b\), \(E(bg)\) is half the double integral of \(N(s,t)(b(s)-b(t))^2g(s)\cdot g(t)\) with a positive kernel \(N\).
4. [Reciprocal kernels and conditional negativity](reciprocal-kernels-and-conditional-negativity.md) proves the central kernel theorem: for each interior point \(p\), the kernel \(K(p,s)K(p,t)/N(s,t)\) is conditionally negative semidefinite, where \(K(p,\cdot)\) is the corresponding interior evaluation kernel.
5. [The absence of interior critical points](the-absence-of-interior-critical-points.md) realizes that kernel as a squared distance in a Hilbert space, uses its coordinates as multipliers, and shows that a critical point would produce either three independent eigenfunctions or an eigenfunction vanishing near a boundary arc.

## 6. Exercises

**6.1.** Let \(R=(0,a)\times(0,b)\) with \(a>b>0\) (a domain with corners, outside the class of this course). Show that \(u(x)=\cos(\pi x_1/a)\) satisfies \(\Delta u+(\pi/a)^2u=0\) and \(\partial_\nu u=0\) on the sides, and that \(\nabla u\) does not vanish in \(R\).

**6.2.** Show that every nonzero \(v\in V\) takes both signs in \(\Omega\).

**6.3.** For \(k\in\mathbb R^2\) with \(|k|^2=\lambda\) and a bounded open set \(\Omega\), compute \(\int_\Omega|\nabla\cos(k\cdot x)|^2-\lambda\int_\Omega\cos^2(k\cdot x)\) and show that it need not vanish. Explain why the proof of Proposition 4.1 uses complex plane waves.

**6.4.** Let \(\Omega_r=\{rx:x\in\Omega\}\) for \(r>0\). Show \(\mu(\Omega_r)=r^{-2}\mu(\Omega)\) and \(\lambda_D(\Omega_r)=r^{-2}\lambda_D(\Omega)\).

**6.5.** Suppose \(|x_1|\le R\) on \(\Omega\). Show \(\lambda_D\ge1/(4R^2)\).

## 7. Solutions

**6.1.** \(\Delta u=-(\pi/a)^2u\). On the vertical sides \(\partial_\nu u=\pm\partial_1u=\mp(\pi/a)\sin(\pi x_1/a)=0\) at \(x_1=0,a\), and on the horizontal sides \(\partial_\nu u=\pm\partial_2u=0\). The gradient is \((-(\pi/a)\sin(\pi x_1/a),0)\), which is nonzero for \(0<x_1<a\).

**6.2.** By (3.1) with \(\phi=1\), \(\int v=0\). A continuous function with zero integral that is not identically zero takes both signs.

**6.3.** \(|\nabla\cos(k\cdot x)|^2=\lambda\sin^2(k\cdot x)\), so the expression is \(-\lambda\int_\Omega\cos(2k\cdot x)\,dx\). For \(\Omega\) a small disc centred at \(0\) it is close to \(-\lambda|\Omega|\ne0\). For \(e_k=e^{ik\cdot x}\) the two terms cancel pointwise because \(|\nabla e_k|^2=\lambda|e_k|^2\); this is what makes \(Q(e_k)=0\).

**6.4.** The map \(v\mapsto v(\cdot/r)\) is a bijection from \(H^1(\Omega)\) onto \(H^1(\Omega_r)\) preserving the mean-zero condition and \(H^1_0\). It multiplies \(\int|\nabla v|^2\) by \(1\) and \(\int v^2\) by \(r^2\) in dimension two, so every Rayleigh quotient is multiplied by \(r^{-2}\).

**6.5.** By Lemma 2.3(1) in the form \(\|\phi\|\le2R\|\partial_1\phi\|\), \(\int|\nabla\phi|^2\ge\int|\partial_1\phi|^2\ge\|\phi\|^2/(4R^2)\) for \(\phi\in H^1_0(\Omega)\).

## References

- [OpenAI-HS] OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, OpenAI Math Release preprint, 24 September 2026, Theorem 1.1, Lemma 2.1. https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
- [Bur05] K. Burdzy, *The "hot spots" problem in planar domains with one hole*, arXiv:math/0405472, Theorem 1.1 and Conjecture 1.2. https://arxiv.org/abs/math/0405472
- [dDP24] J. de Dios Pont, *Convex sets can have interior hot spots*, arXiv:2412.06344. https://arxiv.org/abs/2412.06344
- [Fil04] N. Filonov, *An inequality for eigenvalues of the Dirichlet and Neumann problems for the Laplace operator*, Algebra i Analiz 16 (2004), no. 2, 172–176 (in Russian; English translation in St. Petersburg Math. J. 16 (2005), 413–416). https://www.mathnet.ru/eng/aa604
- [Sho94] R. E. Showalter, *Hilbert Space Methods for Partial Differential Equations*, Electronic Journal of Differential Equations, Monograph 01, 1994, Chapter II (Theorems 3.3, 4.2, 5.5, 5.8) and Chapter III (Theorems 6.1, 6.4, 6.5). https://ejde.math.txstate.edu/Monographs/01/
