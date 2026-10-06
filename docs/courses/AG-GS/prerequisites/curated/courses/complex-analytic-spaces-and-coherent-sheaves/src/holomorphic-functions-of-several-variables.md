# Holomorphic functions of several variables

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Scalar analytic prerequisite integration by GPT-6 Astra (OpenAI), Codex, Ultra; this contribution is not a full independent review. Public domain (CC0).*

This lesson extends the basic theory of holomorphic functions from one complex variable to several. Holomorphy in several variables is defined one variable at a time, and the Cauchy integral formula on a polydisc then turns it into a power series theory: holomorphic functions are smooth, satisfy the identity theorem and the maximum principle, are closed under locally uniform limits, and form a space in which bounded sets are relatively compact (Montel's theorem). The last section proves the Riemann extension theorem across the zero set of a holomorphic function, which every later lesson of this course uses.

We assume the theory of holomorphic functions of one variable as developed in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), whose text is J. Lebl's *Guide to Cultivating Complex Analysis*; results from it are cited by their numbers in that text, for example "[Complex Analysis, Theorem 3.2.15]". From real analysis we use uniform convergence, Fubini's theorem for continuous functions on products of compact sets, and differentiation under the integral sign, as in the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20).

For the proofs of the polydisc formula and Taylor expansion, the exact earlier programme inputs are Cauchy's formula on a disc, Theorem 2.3 and Lemma 1.1, Riemann integration on compact rectangles, Lemma 0.1, and termwise differentiation of power series, Lemma 3.1. These proofs precede any operator-algebra application. In Lemma 0.1 only the scalar case is required here; its bounded-functional separation argument is needed for the Banach-valued extension, not for scalar integration. Circle parametrization converts the torus integrals below into iterated Riemann integrals on compact intervals, so no measure-theoretic Fubini theorem is required.

Basic references are [Lebl SCV] and [Demailly].

## 1. Polydiscs and the definition of holomorphy

We write points of \(\mathbf C^n\) as \(z=(z_1,\ldots,z_n)\). For \(a\in\mathbf C^n\) and a vector of radii \(r=(r_1,\ldots,r_n)\) with \(r_j>0\), the **polydisc** and its **distinguished boundary** are

\[
\Delta(a;r)=\{z:\ |z_j-a_j|<r_j\ \text{for all } j\},\qquad
T(a;r)=\{\zeta:\ |\zeta_j-a_j|=r_j\ \text{for all } j\}.
\tag{1.1}
\]

The closed polydisc \(\overline\Delta(a;r)\) is the product of the closed discs. The distinguished boundary is an \(n\)-dimensional torus; for \(n\geq2\) it is much smaller than the topological boundary of the polydisc. Multi-index notation is used throughout: for \(\alpha\in\mathbf N^n\), \(|\alpha|=\alpha_1+\cdots+\alpha_n\), \(\alpha!=\alpha_1!\cdots\alpha_n!\), \(z^\alpha=z_1^{\alpha_1}\cdots z_n^{\alpha_n}\) and \(r^\alpha=r_1^{\alpha_1}\cdots r_n^{\alpha_n}\).

**Definition 1.1.** Let \(U\subset\mathbf C^n\) be open. A function \(f:U\to\mathbf C\) is **holomorphic** if it is continuous and, for every \(j\) and every choice of the other coordinates, the function of one variable \(z_j\mapsto f(z_1,\ldots,z_n)\) is holomorphic on the open set of \(\mathbf C\) where it is defined. The holomorphic functions on \(U\) form a ring \(\mathcal O(U)\).

Continuity is part of the definition. It is in fact automatic (a theorem of Hartogs), but no result of this course needs that theorem.

**Theorem 1.2 (Cauchy formula on a polydisc).** Let \(f\) be holomorphic on a neighbourhood of a closed polydisc \(\overline\Delta(a;r)\). Then for every \(z\in\Delta(a;r)\),

\[
f(z)=\frac1{(2\pi i)^n}\int_{T(a;r)}\frac{f(\zeta)}{(\zeta_1-z_1)\cdots(\zeta_n-z_n)}\,d\zeta_1\cdots d\zeta_n ,
\tag{1.2}
\]

where the integral is the iterated integral over the \(n\) circles \(|\zeta_j-a_j|=r_j\), each oriented counterclockwise.

**Proof.** Induction on \(n\); the case \(n=1\) is Cauchy's formula, Theorem 2.3, with the circle index equal to one by Lemma 1.1. Let \(n\geq2\) and write \(z=(z',z_n)\). For fixed \(\zeta'\) with \(|\zeta_j-a_j|=r_j\) for \(j<n\), the function \(z_n\mapsto f(\zeta',z_n)\) is holomorphic near the closed disc \(|z_n-a_n|\leq r_n\), so

\[
f(\zeta',z_n)=\frac1{2\pi i}\int_{|\zeta_n-a_n|=r_n}\frac{f(\zeta',\zeta_n)}{\zeta_n-z_n}\,d\zeta_n .
\]

For fixed \(z_n\), the function \(z'\mapsto f(z',z_n)\) is holomorphic in \(n-1\) variables near \(\overline\Delta(a';r')\), so the induction hypothesis gives \(f(z',z_n)\) as the \((n-1)\)-fold integral of \(f(\zeta',z_n)/\prod_{j<n}(\zeta_j-z_j)\). Substituting the one-variable formula for \(f(\zeta',z_n)\) gives (1.2) as an iterated integral. The integrand is continuous on the compact torus \(T(a;r)\). Parametrizing each circle and applying Lemma 0.1(3) interchanges any two adjacent integrations, hence permits every order. \(\square\)

## 2. Power series and the regularity of holomorphic functions

**Theorem 2.1 (power series expansion).** Let \(f\) be holomorphic on a neighbourhood of \(\overline\Delta(a;r)\). Put

\[
c_\alpha=\frac1{(2\pi i)^n}\int_{T(a;r)}\frac{f(\zeta)}{(\zeta-a)^{\alpha+\mathbf 1}}\,d\zeta,
\qquad (\zeta-a)^{\alpha+\mathbf 1}=\prod_{j=1}^n(\zeta_j-a_j)^{\alpha_j+1}.
\tag{2.1}
\]

Then:

1. (Cauchy estimates) \(|c_\alpha|\,r^\alpha\leq\sup_{T(a;r)}|f|\) for every \(\alpha\);
2. the series \(\sum_\alpha c_\alpha(z-a)^\alpha\) converges absolutely and uniformly on every smaller closed polydisc \(\overline\Delta(a;\rho)\), \(\rho_j<r_j\), and its sum is \(f(z)\);
3. \(f\) is infinitely differentiable on \(\Delta(a;r)\); every partial derivative \(\partial^\alpha f=\partial^{|\alpha|}f/\partial z_1^{\alpha_1}\cdots\partial z_n^{\alpha_n}\) is holomorphic and \(\partial^\alpha f(a)=\alpha!\,c_\alpha\).

**Proof.** (1) Estimate (2.1) directly: the torus has total length \(\prod 2\pi r_j\) and \(|\zeta-a|^{\alpha+\mathbf 1}=r^{\alpha+\mathbf 1}\).

(2) For \(z\in\overline\Delta(a;\rho)\) and \(\zeta\in T(a;r)\), put \(q_j=|z_j-a_j|/r_j\leq\rho_j/r_j<1\). The geometric series

\[
\frac1{\zeta_j-z_j}=\sum_{k\geq0}\frac{(z_j-a_j)^k}{(\zeta_j-a_j)^{k+1}}
\]

converges absolutely, with the \(k\)-th term bounded by \(q_j^k/r_j\). Multiplying the \(n\) series, the kernel of (1.2) becomes \(\sum_\alpha(z-a)^\alpha/(\zeta-a)^{\alpha+\mathbf 1}\), with the \(\alpha\)-th term bounded by \(\prod_j q_j^{\alpha_j}/r_j\). This multiple series converges uniformly in \((z,\zeta)\in\overline\Delta(a;\rho)\times T(a;r)\), since \(\sum_\alpha\prod_j(\rho_j/r_j)^{\alpha_j}=\prod_j(1-\rho_j/r_j)^{-1}\). Integrating term by term against the bounded function \(f\) gives \(f(z)=\sum c_\alpha(z-a)^\alpha\), and the Cauchy estimates give \(|c_\alpha(z-a)^\alpha|\leq\sup_T|f|\prod_j(\rho_j/r_j)^{\alpha_j}\), which proves absolute and uniform convergence.

(3) A power series converging absolutely on \(\overline\Delta(a;\rho)\) may be differentiated term by term in each variable on the open polydisc \(\Delta(a;\rho)\), the differentiated series again converging locally uniformly: in each variable this is Lemma 3.1 and its difference-quotient proof, and the bound \(|c_\alpha|\leq M r^{-\alpha}\) shows that \(\sum|\alpha_j c_\alpha(z-a)^{\alpha-e_j}|\) converges uniformly on \(\overline\Delta(a;\rho)\) whenever \(\rho_j<r_j\). Iterating, all partial derivatives \(\partial^\alpha f\) exist, are given by power series, and are continuous; since every point of \(\Delta(a;r)\) is the centre of a closed polydisc on which \(f\) is holomorphic, this holds on all of \(\Delta(a;r)\). The derivatives are holomorphic, being continuous and given by convergent power series in each variable. Evaluating the differentiated series at \(a\) gives \(\partial^\alpha f(a)=\alpha!\,c_\alpha\). \(\square\)

We write \(\partial/\partial z_j=\frac12(\partial/\partial x_j-i\,\partial/\partial y_j)\) and \(\partial/\partial\bar z_j=\frac12(\partial/\partial x_j+i\,\partial/\partial y_j)\), where \(z_j=x_j+iy_j\).

**Proposition 2.2.** For a function \(f\) on an open set \(U\subset\mathbf C^n\), the following are equivalent:

1. \(f\) is holomorphic;
2. \(f\) is continuously differentiable (in the real sense) and \(\partial f/\partial\bar z_j=0\) for \(j=1,\ldots,n\);
3. every point of \(U\) has a neighbourhood on which \(f\) is the sum of a convergent power series.

**Proof.** (1) implies (3) by Theorem 2.1. If (3) holds, term-by-term differentiation, as in the proof of Theorem 2.1(3), shows that \(f\) is continuously differentiable, and each monomial is annihilated by \(\partial/\partial\bar z_j\); this gives (2). If (2) holds, \(f\) is continuous, and each one-variable restriction is continuously differentiable and satisfies the Cauchy–Riemann equation in its variable, hence is holomorphic. \(\square\)

A map \(F=(F_1,\ldots,F_m):U\to\mathbf C^m\) is **holomorphic** if each component is holomorphic. By Proposition 2.2 and the chain rule for the operators \(\partial/\partial z_j,\partial/\partial\bar z_j\), a composite of holomorphic maps is holomorphic, and its complex Jacobian matrix \((\partial F_k/\partial z_j)\) is the product of the Jacobian matrices. The holomorphic inverse function theorem and the implicit function theorem are proved in [Complex analytic spaces and analytification, Lemma 2.2](course:AG-QC/complex-analytic-spaces-and-analytification#2-local-analytic-algebra): a holomorphic map with invertible complex Jacobian at a point has a holomorphic local inverse, and \(r\) holomorphic equations with Jacobian of rank \(r\) cut out a complex submanifold of codimension \(r\).

**Theorem 2.3 (identity theorem).** Let \(U\) be connected and \(f\in\mathcal O(U)\). If \(f\) vanishes on a nonempty open subset of \(U\), or if all partial derivatives of \(f\) vanish at one point, then \(f=0\) on \(U\).

**Proof.** Let \(E\) be the set of points at which all partial derivatives \(\partial^\alpha f\), including \(f\) itself, vanish. It is closed, because the derivatives are continuous. It is open: at \(a\in E\) all coefficients of the power series of Theorem 2.1 vanish, so \(f=0\) on a polydisc about \(a\), and then all derivatives vanish there. Each hypothesis says \(E\neq\emptyset\), so \(E=U\). \(\square\)

Unlike in one variable, zeros are never isolated when \(n\geq2\): for instance \(f(z)=z_1\) vanishes on a whole hyperplane. Lesson 4 describes the zero sets precisely.

**Theorem 2.4 (maximum principle).** Let \(U\) be connected and \(f\in\mathcal O(U)\). If \(|f|\) has a local maximum at a point \(a\in U\), then \(f\) is constant.

**Proof.** Choose a ball \(B\) about \(a\) on which \(|f|\leq|f(a)|\). For each unit vector \(v\), the function \(g(t)=f(a+tv)\) is holomorphic on a disc about \(0\in\mathbf C\) (Proposition 2.2 and the chain rule) and \(|g|\) has a maximum at \(0\). By the one-variable maximum modulus principle [Complex Analysis, Theorem 3.3.6], \(g\) is constant, so \(f=f(a)\) on the line segment through \(a\) in direction \(v\) inside \(B\). These segments cover \(B\), so \(f\) is constant on \(B\), and Theorem 2.3 applied to \(f-f(a)\) gives the result. \(\square\)

## 3. Limits, the space of holomorphic functions, and Montel's theorem

**Theorem 3.1 (Weierstrass convergence theorem).** Let \(f_k\in\mathcal O(U)\) converge uniformly on compact subsets of \(U\) to a function \(f\). Then \(f\) is holomorphic, and for every \(\alpha\) the derivatives \(\partial^\alpha f_k\) converge to \(\partial^\alpha f\) uniformly on compact subsets.

**Proof.** The limit \(f\) is continuous. Each one-variable restriction of \(f\) is a locally uniform limit of holomorphic functions of one variable, hence holomorphic by Corollary 3.5, proved using Morera's theorem. So \(f\) is holomorphic. For the derivatives, cover a compact set \(K\subset U\) by finitely many polydiscs \(\Delta(a;\rho)\) with \(\overline\Delta(a;r)\subset U\) for some \(r_j>\rho_j\). Differentiating (1.2) under the integral sign gives, for \(z\in\overline\Delta(a;\rho)\),

\[
\partial^\alpha g(z)=\frac{\alpha!}{(2\pi i)^n}\int_{T(a;r)}\frac{g(\zeta)}{(\zeta-z)^{\alpha+\mathbf 1}}\,d\zeta,
\qquad
\sup_{\overline\Delta(a;\rho)}|\partial^\alpha g|\leq\frac{\alpha!\,r^{\mathbf 1}}{(r-\rho)^{\alpha+\mathbf 1}}\sup_{T(a;r)}|g|
\tag{3.1}
\]

for every \(g\) holomorphic near \(\overline\Delta(a;r)\). Apply (3.1) to \(g=f_k-f\). \(\square\)

For a compact set \(K\subset U\) put \(\|f\|_K=\sup_K|f|\). Choosing compact sets \(K_1\subset K_2\subset\cdots\) with \(K_m\) contained in the interior of \(K_{m+1}\) and \(\bigcup K_m=U\), the seminorms \(\|\cdot\|_{K_m}\) define on \(\mathcal O(U)\) the topology of uniform convergence on compact subsets. It is given by the metric \(d(f,g)=\sum_m2^{-m}\min(1,\|f-g\|_{K_m})\), and by Theorem 3.1 it is complete. Thus \(\mathcal O(U)\) is a **Fréchet space**: a complete metrizable locally convex vector space. Lesson 10 uses this structure systematically.

**Theorem 3.2 (Montel's theorem).** Let \(\mathcal F\subset\mathcal O(U)\) be locally bounded: every compact \(K\subset U\) has \(\sup_{f\in\mathcal F}\|f\|_K<\infty\). Then every sequence in \(\mathcal F\) has a subsequence converging uniformly on compact subsets of \(U\); its limit is holomorphic.

**Proof.** First we show equicontinuity on compact sets. Let \(K\subset U\) be compact, cover it by finitely many polydiscs \(\Delta(a;\rho)\) with \(\overline\Delta(a;2\rho)\subset U\), and let \(M\) bound \(|f|\) on the union of the closed polydiscs \(\overline\Delta(a;2\rho)\) for all \(f\in\mathcal F\). By (3.1) with \(r=2\rho\), all first partial derivatives \(\partial f/\partial z_j\) are bounded by \(2^nM/\min_j\rho_j\) on each \(\overline\Delta(a;\rho)\). Since \(\partial f/\partial\bar z_j=0\), integrating along the segment from \(w\) to \(z\) gives \(f(z)-f(w)=\int_0^1\sum_j\frac{\partial f}{\partial z_j}(w+t(z-w))\,(z_j-w_j)\,dt\), hence \(|f(z)-f(w)|\leq C|z-w|\) with \(C=n2^nM/\min_j\rho_j\), for \(z,w\) in one convex polydisc \(\Delta(a;\rho)\) and every \(f\in\mathcal F\). A Lebesgue-number argument for the finite cover then shows that \(\mathcal F\) is equicontinuous on \(K\).

By the Arzelà–Ascoli theorem [Complex Analysis, Theorem 6.1.6], every sequence in \(\mathcal F\) has a subsequence converging uniformly on \(K_1\); a further subsequence converges uniformly on \(K_2\), and so on. The diagonal subsequence converges uniformly on each \(K_m\), hence on every compact subset of \(U\). The limit is holomorphic by Theorem 3.1. \(\square\)

In terms of the Fréchet topology: a subset of \(\mathcal O(U)\) is bounded exactly when it is locally bounded, and Montel's theorem says that closed bounded subsets of \(\mathcal O(U)\) are compact. Consequently, if \(V\subset U\) is open with compact closure \(\overline V\subset U\), the restriction map \(\mathcal O(U)\to\mathcal O(V)\) is a **compact operator**: it maps the neighbourhood \(\{f:\ \|f\|_{\overline V}<1\}\) of \(0\) into a relatively compact set.

## 4. The Riemann extension theorem

The zero set \(Z(h)=h^{-1}(0)\) of a holomorphic function \(h\) on a connected open set \(U\) has empty interior unless \(h=0\), by Theorem 2.3. We first record the elementary "good direction" lemma that underlies this lesson and the next.

**Lemma 4.1.** Let \(h\) be holomorphic near \(a\in\mathbf C^n\) and not identically zero near \(a\). For all vectors \(v\in\mathbf C^n\) outside a closed set with empty interior, the function \(t\mapsto h(a+tv)\) of one variable is not identically zero near \(t=0\). For such \(v\), after a linear change of coordinates taking \(v\) to the last basis vector, there are radii \(r'\) and \(r_n\) such that \(h\) is holomorphic near \(\overline\Delta(a';r')\times\{|z_n-a_n|\leq r_n\}\) and has no zero with \(|z_n-a_n|=r_n\), \(z'\in\overline\Delta(a';r')\).

**Proof.** Group the power series of \(h\) at \(a\) by degree: \(h(a+w)=\sum_{k\geq0}h_k(w)\), with \(h_k\) a homogeneous polynomial of degree \(k\). Since \(h\) is not identically zero near \(a\), some \(h_k\) is not the zero polynomial, by Theorem 2.3; let \(m\) be the least such \(k\). Then \(h(a+tv)=t^mh_m(v)+O(t^{m+1})\), which is not identically zero whenever \(h_m(v)\neq0\). The zero set of the nonzero polynomial \(h_m\) is closed with empty interior (a polynomial vanishing on an open set is zero). For such \(v\), in the new coordinates \(t\mapsto h(a',a_n+t)\) is not identically zero, so it has no zero on some circle \(|t|=r_n\) inside its domain, its zeros being isolated. By continuity of \(h\) and compactness of that circle, there is \(r'\) such that \(h(z',z_n)\neq0\) whenever \(z'\in\overline\Delta(a';r')\) and \(|z_n-a_n|=r_n\). \(\square\)

**Theorem 4.2 (Riemann extension theorem).** Let \(U\subset\mathbf C^n\) be open and \(h\in\mathcal O(U)\) not identically zero on any connected component of \(U\). Let \(f\) be holomorphic on \(U\setminus Z(h)\) and locally bounded near \(Z(h)\), that is, every point of \(Z(h)\) has a neighbourhood \(W\) with \(f\) bounded on \(W\setminus Z(h)\). Then \(f\) extends uniquely to a holomorphic function on \(U\).

**Proof.** Uniqueness holds because \(U\setminus Z(h)\) is dense in \(U\). For existence it suffices, by uniqueness, to extend \(f\) near each point \(a\in Z(h)\). Choose coordinates and radii as in Lemma 4.1, with the closed polydisc \(\overline P\subset U\), where \(P=\Delta(a';r')\times\{|z_n-a_n|<r_n+\varepsilon\}\) and \(\varepsilon>0\) is so small that \(h\neq0\) on the compact set \(\overline\Delta(a';r')\times\{r_n-\varepsilon\leq|z_n-a_n|\leq r_n+\varepsilon\}\); such \(\varepsilon\) exists by compactness, since \(h\neq0\) where \(|z_n-a_n|=r_n\). Then \(f\) is bounded, say by \(M\), on \(\overline P\setminus Z(h)\): finitely many neighbourhoods on which \(f\) is bounded cover the compact set \(\overline P\cap Z(h)\), and \(f\) is continuous on the remaining compact part of \(\overline P\), which misses \(Z(h)\).

Fix \(z'\in\Delta(a';r')\). The one-variable function \(z_n\mapsto h(z',z_n)\) is not identically zero, so it has finitely many zeros in the disc \(|z_n-a_n|\leq r_n-\varepsilon\) and none in the closed annulus where \(r_n-\varepsilon\leq|z_n-a_n|\leq r_n+\varepsilon\). Away from these zeros, \(z_n\mapsto f(z',z_n)\) is holomorphic and bounded by \(M\). By the one-variable Riemann extension theorem [Complex Analysis, Theorem 5.2.2] it extends to a holomorphic function \(g_{z'}\) on \(|z_n-a_n|<r_n+\varepsilon\). Define, for \(z\in\Delta(a';r')\times\{|z_n-a_n|<r_n\}\),

\[
F(z',z_n)=\frac1{2\pi i}\int_{|\zeta-a_n|=r_n}\frac{f(z',\zeta)}{\zeta-z_n}\,d\zeta .
\tag{4.1}
\]

The set \(\overline\Delta(a';r')\times\{|\zeta-a_n|=r_n\}\) misses \(Z(h)\), so \(f\) is holomorphic on a neighbourhood of it. Hence the integrand of (4.1) is continuously differentiable in \((z',z_n)\), jointly continuously in \(\zeta\), and annihilated by every \(\partial/\partial\bar z_j\). Differentiating under the integral sign, \(F\) is continuously differentiable with \(\partial F/\partial\bar z_j=0\), so \(F\) is holomorphic by Proposition 2.2. By the one-variable Cauchy formula applied to \(g_{z'}\), \(F(z',z_n)=g_{z'}(z_n)\), which equals \(f(z',z_n)\) whenever \(h(z',z_n)\neq0\). Thus \(F\) extends \(f\) near \(a\). \(\square\)

**Corollary 4.3.** If \(U\) is connected and \(h\in\mathcal O(U)\) is not identically zero, then \(U\setminus Z(h)\) is connected and dense in \(U\).

**Proof.** Density was noted above. If \(U\setminus Z(h)\) were the disjoint union of two nonempty open sets \(V_0,V_1\), the function equal to \(0\) on \(V_0\) and to \(1\) on \(V_1\) would be holomorphic and bounded on \(U\setminus Z(h)\). Its extension \(F\in\mathcal O(U)\) from Theorem 4.2 takes only the values \(0\) and \(1\) on the dense set \(U\setminus Z(h)\), hence everywhere by continuity. The connected set \(U\) has connected image under \(F\), so \(F\) is constant, a contradiction. \(\square\)

A subset \(A\) of an open set \(U\subset\mathbf C^n\) is an **analytic subset** if it is closed in \(U\) and every point \(a\in U\) has a neighbourhood \(W\) and finitely many \(g_1,\ldots,g_k\in\mathcal O(W)\) with \(A\cap W=\{z\in W:\ g_1(z)=\cdots=g_k(z)=0\}\). (Near points outside \(A\) one may take \(g_1=1\).)

**Corollary 4.4.** Let \(A\) be an analytic subset of \(U\) with empty interior. Every function holomorphic on \(U\setminus A\) and locally bounded near \(A\) extends uniquely to a holomorphic function on \(U\). If \(U\) is connected, so is \(U\setminus A\).

**Proof.** Let \(a\in A\), with local equations \(g_1,\ldots,g_k\) on a connected neighbourhood \(W\). Not all \(g_i\) vanish identically on \(W\), otherwise \(A\supset W\). Choose \(g=g_i\neq0\). Then \(A\cap W\subset Z(g)\), and \(f\) restricted to \(W\setminus Z(g)\) is holomorphic and locally bounded near \(Z(g)\). Theorem 4.2 extends it to \(F\in\mathcal O(W)\). Since \(W\setminus Z(g)\) is dense in \(W\setminus A\), \(F=f\) on \(W\setminus A\). The local extensions agree on overlaps by density of \(U\setminus A\), which proves the first statement. Connectedness follows exactly as in Corollary 4.3. \(\square\)

## 5. Complex manifolds

A **complex manifold** of dimension \(n\) is a Hausdorff, second countable topological space \(M\) with an atlas of homeomorphisms \(\varphi_i:U_i\to V_i\) onto open subsets of \(\mathbf C^n\) whose transition maps \(\varphi_j\circ\varphi_i^{-1}\) are holomorphic. A function on an open subset of \(M\) is holomorphic if it is holomorphic in every chart; the holomorphic functions form a sheaf of rings \(\mathcal O_M\). All results of Sections 2–4 are local and invariant under holomorphic changes of coordinates, so they hold on complex manifolds: the identity theorem and the maximum principle on connected manifolds, Weierstrass convergence and Montel's theorem for \(\mathcal O(U)\), \(U\subset M\) open, and the Riemann extension theorem across analytic subsets with empty interior. The stalk \(\mathcal O_{M,x}\) is isomorphic, via a chart centred at \(x\), to the ring \(\mathbf C\{z_1,\ldots,z_n\}\) of convergent power series studied in Lesson 2.

## 6. Exercises

**Exercise 6.1.** Prove Liouville's theorem in several variables: a bounded holomorphic function on \(\mathbf C^n\) is constant.

*Solution.* Expand \(f\) at \(0\) on the polydisc \(\Delta(0;(R,\ldots,R))\). By the Cauchy estimates, \(|c_\alpha|\leq\sup|f|/R^{|\alpha|}\) for every \(R>0\). Letting \(R\to\infty\) gives \(c_\alpha=0\) for \(\alpha\neq0\), so \(f=c_0\) near \(0\), and hence everywhere by Theorem 2.3.

**Exercise 6.2.** Show that the power series of \(f(z)=1/(1-z_1-z_2)\) at \(0\) converges absolutely exactly on the set \(\{|z_1|+|z_2|<1\}\), which is not a polydisc.

*Solution.* Expanding the geometric series, \(f=\sum_{k\geq0}(z_1+z_2)^k=\sum_{\alpha}\binom{\alpha_1+\alpha_2}{\alpha_1}z_1^{\alpha_1}z_2^{\alpha_2}\), and all coefficients are positive. The sum of the absolute values of the terms at \(z\) is \(\sum_k(|z_1|+|z_2|)^k\), which is finite exactly when \(|z_1|+|z_2|<1\). A polydisc containing \((1-\varepsilon,0)\) and \((0,1-\varepsilon)\) contains \((1-\varepsilon,1-\varepsilon)\), where \(|z_1|+|z_2|>1\) for \(\varepsilon<1/2\). So this region is not a polydisc.

**Exercise 6.3.** Let \(f(z_1,z_2)=z_1/z_2\) on \(\mathbf C^2\setminus Z(z_2)\). Show that \(f\) has no holomorphic extension to \(\mathbf C^2\), and explain which hypothesis of Theorem 4.2 fails.

*Solution.* An extension \(F\) would be continuous at \((1,0)\), but \(f(1,t)=1/t\) is unbounded as \(t\to0\). The function is not locally bounded near the points \((z_1,0)\) with \(z_1\neq0\), which is the hypothesis that fails. Near the origin itself \(f\) is also unbounded, since \(f(t,t^2)=1/t\).

**Exercise 6.4.** Show that the unit ball \(\{f\in\mathcal O(\Delta):\ |f|\leq1\}\) of bounded holomorphic functions on a polydisc \(\Delta\) is compact in the topology of uniform convergence on compact subsets.

*Solution.* It is locally bounded, so every sequence in it has a subsequence converging uniformly on compact subsets, by Theorem 3.2. The limit is holomorphic by Theorem 3.1 and still satisfies \(|f|\leq1\) pointwise. The topology is metrizable, so sequential compactness is compactness.

**Exercise 6.5.** Let \(n\geq2\). Show that a holomorphic function on \(\mathbf C^n\) whose zero set is contained in a single point is nowhere zero.

*Solution.* Suppose \(f(a)=0\). If \(f\) vanished identically, its zero set would be all of \(\mathbf C^n\); so \(f\neq0\). By Lemma 4.1 we may choose coordinates centred at \(a\) and radii with \(f(z',z_n)\neq0\) for \(|z'|\leq r'\), \(|z_n|=r_n\), and the function \(z_n\mapsto f(0',z_n)\) has a zero at \(0\) inside \(|z_n|<r_n\). The number of zeros of \(z_n\mapsto f(z',z_n)\) inside the circle is given by the argument principle [Complex Analysis, Theorem 5.4.1], an integral depending continuously on \(z'\); being an integer it is constant, and it is at least one at \(z'=0'\). So for every \(z'\) with \(|z'|<r'\) there is a zero \((z',z_n)\). Since \(n\geq2\), there are infinitely many such \(z'\), giving infinitely many zeros, a contradiction.

## References

- [Lebl SCV] J. Lebl, *Tasty Bits of Several Complex Variables*, version 4.4 (2026), licensed CC BY-SA 4.0 (dual-licensed with CC BY-NC-SA 4.0). <https://www.jirka.org/scv/>
- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
