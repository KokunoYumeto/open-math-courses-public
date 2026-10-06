# Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check; revised and self-checked by that writing AI in October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all five solutions, completed its elementary and Bochner-density proofs and supplied the exact prerequisites, October 2026. Public domain (CC0).*

A Banach algebra is an algebra with a complete norm that satisfies \(\|xy\|\leq\|x\|\|y\|\). The bounded operators on a Banach space and the continuous functions on a compact space are the basic examples. This lesson develops the elementary theory of Banach algebras, on which the rest of the operator-algebra course stands.

The central object is the spectrum of an element \(x\): the set of complex numbers \(\lambda\) for which \(\lambda-x\) has no inverse. For a matrix it is the set of eigenvalues. In every nonzero unital Banach algebra the spectrum keeps the properties that make eigenvalues useful. It is compact and not empty, and the norms of the powers of \(x\) determine its size (Sections 4 and 5). Holomorphic functions can be applied to \(x\), and the spectrum of \(f(x)\) is the image of the spectrum of \(x\) under \(f\) (Section 6); Sections 7 and 8 apply this to the exponential and the logarithm, and to small perturbations of \(x\). For a commutative algebra the spectrum is described by the characters, the nonzero homomorphisms into \(\mathbb C\), and the Gelfand transform maps every commutative Banach algebra to continuous functions on its character space (Sections 9 to 11). Sections 12 and 13 work out two examples from harmonic analysis: the convolution algebras of a locally compact group and of its actions, and the algebra of absolutely convergent Fourier series, where Gelfand theory gives Wiener's lemma. Along the way, the calculus is built on cycles rather than on one closed curve, so that it applies to functions defined near a disconnected spectrum. Modular ideals and characters are treated in algebras that need not be commutative, and the Gelfand–Mazur theorem is proved for normed algebras that need not be complete.

The lesson uses the Hahn–Banach and Banach–Alaoglu theorems, Urysohn's lemma for locally compact spaces, and Cauchy's theorem for cycles. They are proved in earlier lessons; the exact statements and places are listed under "Results used from other lessons". Section 12 also uses Haar measure, from the lesson Haar measure on locally compact groups.

The spectral radius formula connects the norm estimates on powers to the spectrum. It leads to the Gelfand representation, while the holomorphic calculus converts scalar analytic identities into identities in the algebra. All three constructions and their consequences are proved below.

## Conventions

*Algebras.* All algebras are complex and associative. An algebra need not have an identity, and need not be commutative. "Ideal" means two-sided ideal; one-sided ideals are called left or right ideals. An algebra \(A\) is *unital* if it has an element \(1\) with \(1x=x1=x\) for all \(x\). Such an element is unique. The zero algebra \(\{0\}\) is unital, with \(1=0\). We call a unital algebra *nontrivial* when \(1\neq0\), that is, when \(A\neq\{0\}\). In a unital algebra we write \(\lambda\) for \(\lambda1\).

*Norms.* A *normed algebra* is an algebra with a norm such that \(\|xy\|\leq\|x\|\|y\|\). A *Banach algebra* is a complete normed algebra. We do not assume \(\|1\|=1\). [Proposition 3.1](#oa-fnd-bn-03) shows how to arrange it, and almost nothing below depends on it.

*Spectra.* \(\sigma_A(x)\) is the spectrum, \(\rho_A(x)=\mathbb C\setminus\sigma_A(x)\) the resolvent set, \(R_x(\lambda)=(\lambda-x)^{-1}\) the resolvent, and \(r(x)\) the spectral radius ([Section 4](#oa-fnd-bn-06)).

*Duality.* \(E^*\) is the dual of a normed space \(E\). The weak\* topology on \(E^*\) is the topology of pointwise convergence on \(E\).

*Operators and functions.* \(B(E)\) is the algebra of bounded operators on a Banach space \(E\). Hilbert spaces are complex, and inner products are linear in the first variable. LCH means locally compact Hausdorff. For an LCH space \(\Omega\), \(C_0(\Omega)\) is the algebra of continuous functions that vanish at infinity, with the supremum norm, and \(C_c(\Omega)\) consists of those with compact support. \(H(U)\) is the algebra of holomorphic functions on an open set \(U\subseteq\mathbb C\).

## Results used from other lessons

The lesson uses results proved in these earlier lessons:
- [Hahn–Banach, Baire and the basic theorems on Banach spaces](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md), cited as *the Hahn–Banach lesson*;
- [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md), cited as *the lesson on weak topologies*;
- [Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md), cited as *the Hilbert-space lesson*;
- [Cauchy's theorem for cycles and its consequences](cauchy-s-theorem-for-cycles-and-its-consequences.md), cited as *the lesson on Cauchy's theorem*;
- The Stone–Weierstrass theorem for functions vanishing at infinity and Haar measure on locally compact groups.

The results are these.
- **Hahn–Banach theorem** (the Hahn–Banach lesson, Corollary 2.3(2)). For every \(a\) in a normed space \(E\) there is \(\varphi\in E^*\) with \(\|\varphi\|\leq1\) and \(\varphi(a)=\|a\|\). So \(a=0\) if \(\varphi(a)=0\) for every \(\varphi\in E^*\).
- **Banach–Alaoglu theorem** (the lesson on weak topologies, Theorem 3.1). The closed unit ball of \(E^*\) is weak\* compact.
- **Urysohn's lemma** (Proposition 4.2(2) and Corollary 5.2 of the Stone–Weierstrass lesson). Let \(\Omega\) be an LCH space, and let \(K\subseteq U\subseteq\Omega\) with \(K\) compact and \(U\) open. Then some \(f\in C_c(\Omega)\) has \(0\leq f\leq1\), \(f=1\) on \(K\) and \(\operatorname{supp}f\subseteq U\). Choose an open \(V\supseteq K\) with compact closure in \(U\), and apply Corollary 5.2 to \(K\) and \(\Omega\setminus V\).
- **Zorn's lemma** (the Hahn–Banach lesson, Theorem 1.1). A nonempty partially ordered set in which every chain has an upper bound has a maximal element. It is used in Sections 9 and 10 and in Exercise 2.
- **Hilbert spaces** (the Hilbert-space lesson, Theorem 2.3, Corollary 3.2 and Section 8). Every \(T\in B(H)\) has an adjoint \(T^*\in B(H)\), the unique operator with \(\langle T\xi,\eta\rangle=\langle\xi,T^*\eta\rangle\) for all \(\xi,\eta\in H\), and \(T^{**}=T\). The unit vectors \(e_n\) form orthonormal bases of \(\ell^2(\mathbb N)\) and \(\ell^2(\mathbb Z)\).
- **Complex analysis** (the lesson on Cauchy's theorem, Theorems 4.2, 5.1 and 6.1). Cauchy's theorem for cycles, for functions with values in a Banach space, and the existence of a cycle that surrounds a given compact set. They are restated as Theorems 6.1 and 6.2 at the start of Section 6, after cycles have been defined.
- **Haar measure.** Section 12 uses a left Haar measure on a locally compact group and its modular function. The facts it needs are stated where they are used, with links to the lesson Haar measure on locally compact groups, where they are proved.
- **Elementary integration** is proved in [Lemma 0.1 of the Cauchy lesson](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-07), for Banach-valued functions too: interval Riemann integrals, the fundamental theorem and chain rule, rectangle interchange and parameter differentiation. [Lemma 3.1 and Theorem 3.2 there](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-03) prove the power-series and Taylor statements. The absolutely convergent products and commuting binomial formula are proved next.

### Absolutely convergent products

**Lemma 0.1** (Products and regrouping). In a Banach algebra, the product of two absolutely convergent series is the sum of the products of their terms, and that double series may be regrouped in any countable partition of its index set. In particular, for series indexed by nonnegative integers,
\[
\left(\sum_{j\geq0}a_j\right)
\left(\sum_{k\geq0}b_k\right)
=\sum_{n\geq0}\sum_{j+k=n}a_jb_k .
\]
If \(xy=yx\) in a unital algebra, then
\((x+y)^n=\sum_{j=0}^n\binom njx^jy^{n-j}\).

**Proof.** The scalar estimate
\(\sum_{j,k}\|a_jb_k\|\leq(\sum_j\|a_j\|)(\sum_k\|b_k\|)\)
follows first for finite rectangles and then by taking suprema of finite subsums. For finite subsets \(J,K\), the norm sum outside \(J\times K\) is at most
\[
\left(\sum_{j\notin J}\|a_j\|\right)\sum_k\|b_k\|
+\sum_j\|a_j\|\left(\sum_{k\notin K}\|b_k\|\right),
\]
which tends to zero as \(J,K\) exhaust the indices. Thus finite double sums form a Cauchy net and converge by completeness; sums over rectangles converge to the product by continuity of multiplication. For any countable grouping, each group itself has an absolutely convergent sum, and the sum of the norms of the grouped sums is at most the original norm sum. The tail estimate shows that the grouped series has the same limit: first keep a finite rectangle with small complementary norm sum, then keep all groups containing its finitely many terms. This proves the regrouping claim, including the groups \(j+k=n\). Finally, multiplication of the binomial identity for \(n\) by \(x+y\), using \(xy=yx\) and \(\binom nj+\binom n{j-1}=\binom{n+1}j\), proves it for \(n+1\); the case \(n=0\) is the identity. \(\square\)


## 1. Banach algebras and C\*-algebras

**Definition 1.1.**
1. An *involution* on an algebra \(A\) is a map \(x\mapsto x^*\) with \((x^*)^*=x\), \((x+y)^*=x^*+y^*\), \((\lambda x)^*=\bar\lambda x^*\) and \((xy)^*=y^*x^*\).
2. An *involutive Banach algebra* is a Banach algebra together with an isometric involution: \(\|x^*\|=\|x\|\).
3. A *C\*-algebra* is an involutive Banach algebra in which \(\|x^*x\|=\|x^*\|\|x\|\) for every \(x\). Because the involution is isometric, this says \(\|x^*x\|=\|x\|^2\) (the *C\*-identity*).

**Proposition 1.2.**
1. Multiplication is jointly continuous: \[
\begin{gathered}
\|x_1y_1-x_2y_2\|\\
\leq\|x_1\|\|y_1-y_2\|+\|x_1-x_2\|\|y_2\|.
\end{gathered}
\]
2. For a Banach space \(E\), \(B(E)\) with the operator norm is a Banach algebra.
3. (*The C\*-identity alone is enough.*) Let \(A\) be an algebra with an involution and a complete submultiplicative norm such that \(\|x^*x\|=\|x\|^2\) for all \(x\). Then \(\|x^*\|=\|x\|\), so \(A\) is a C\*-algebra.
4. For an LCH space \(\Omega\), \(C_0(\Omega)\) is a commutative C\*-algebra under pointwise operations, with \(x^*=\bar x\). It is unital exactly when \(\Omega\) is compact; then it is written \(C(\Omega)\). This includes \(\Omega=\varnothing\): \(C_0(\varnothing)=\{0\}\) is unital, and \(\varnothing\) is compact.
5. For a Hilbert space \(H\), \(B(H)\) with the operator adjoint is a C\*-algebra. It is commutative exactly when \(\dim H\leq1\). Every norm-closed \(*\)-subalgebra of \(B(H)\) is a C\*-algebra.

**Proof.** (1) Write \(x_1y_1-x_2y_2=x_1(y_1-y_2)+(x_1-x_2)y_2\).

(2) \(\|ST\xi\|\leq\|S\|\|T\xi\|\leq\|S\|\|T\|\|\xi\|\). Let \((T_n)\) be Cauchy in operator norm. For each \(\xi\), \((T_n\xi)\) is Cauchy; put \(T\xi=\lim_nT_n\xi\). Then \(T\) is linear, and \(\|T\xi-T_n\xi\|\leq\sup_{m\geq n}\|T_m-T_n\|\,\|\xi\|\). So \(T\) is bounded and \(T_n\to T\).

(3) \(\|x\|^2=\|x^*x\|\leq\|x^*\|\|x\|\), so \(\|x\|\leq\|x^*\|\) (also when \(x=0\)). Apply this to \(x^*\).

(4) Pointwise products and conjugates of functions in \(C_0(\Omega)\) stay in \(C_0(\Omega)\). The supremum norm is submultiplicative, conjugation is isometric, and \(\|\bar xx\|_\infty=\sup|x|^2=\|x\|_\infty^2\). For completeness, let \((x_n)\) be uniformly Cauchy. It converges uniformly to a continuous \(x\). Given \(\varepsilon>0\), take \(n\) with \(\|x-x_n\|_\infty<\varepsilon/2\). Then \(\{|x|\geq\varepsilon\}\) is a closed subset of the compact set \(\{|x_n|\geq\varepsilon/2\}\), so \(x\in C_0(\Omega)\). If \(\Omega\) is compact, the constant \(1\) lies in \(C_0(\Omega)\). Conversely, let \(u\) be an identity. For \(p\in\Omega\), Urysohn's lemma gives \(x\in C_c(\Omega)\) with \(x(p)=1\), and \(ux=x\) gives \(u(p)=1\). So \(u\equiv1\). Since \(u\) vanishes at infinity, \(\Omega=\{|u|\geq1/2\}\) is compact.

(5) For \(\xi\in H\), \(\|T\xi\|^2=\langle T^*T\xi,\xi\rangle\leq\|T^*T\|\|\xi\|^2\). So \(\|T\|^2\leq\|T^*T\|\leq\|T^*\|\|T\|\), which gives \(\|T\|\leq\|T^*\|\). Since \(T^{**}=T\), also \(\|T^*\|\leq\|T\|\); hence \(\|T^*\|=\|T\|\) and \(\|T^*T\|=\|T\|^2\). If \(\dim H\leq1\), then \(B(H)=\mathbb C1\). If \(e_1,e_2\) are orthonormal, put \(E_{ij}\xi=\langle\xi,e_j\rangle e_i\). Then \(E_{12}E_{21}=E_{11}\neq E_{22}=E_{21}E_{12}\). A norm-closed \(*\)-subalgebra is complete and inherits the C\*-identity. \(\square\)

So C\*-algebras can be described in two ways. Concretely, they are the norm-closed \(*\)-subalgebras of the algebras \(B(H)\); part (5) shows that these are C\*-algebras. Abstractly, they are the algebras that satisfy the axioms of Definition 1.1. The two descriptions give the same objects: every C\*-algebra has a faithful representation on a Hilbert space, that is, it is isometrically \(*\)-isomorphic to a norm-closed \(*\)-subalgebra of some \(B(H)\). This is the Gelfand–Naimark theorem. Its proof needs positive functionals and the representations they define, which are beyond this lesson.

## 2. Invertible elements and the Neumann series

Let \(A\) be a unital algebra. An element \(y\) is a *left inverse* of \(x\) if \(yx=1\), and a *right inverse* if \(xy=1\). If \(x\) has both, they coincide: \(y=y(xz)=(yx)z=z\). Then \(x\) is *invertible*, and this element is its inverse \(x^{-1}\). The invertible elements form a group \(G(A)\), with \((xy)^{-1}=y^{-1}x^{-1}\). If \(\pi:A\to B\) is a unital homomorphism, that is \(\pi(1)=1\), then \(\pi(G(A))\subseteq G(B)\) and \(\pi(x^{-1})=\pi(x)^{-1}\).

**Proposition 2.1** (Neumann series). Let \(A\) be a unital Banach algebra and \(\|1-x\|<1\). Then \(x\) is invertible, and
\[
x^{-1}=\sum_{n=0}^\infty(1-x)^n,
\tag{2.1}
\]
where \((1-x)^0=1\) and the series converges in norm. Moreover \(\|x^{-1}\|\leq\|1\|+\|1-x\|/(1-\|1-x\|)\).

**Proof.** Put \(y=1-x\). Since \(\|y^n\|\leq\|y\|^n\) for \(n\geq1\), the partial sums \(s_N=\sum_{n=0}^Ny^n\) form a Cauchy sequence, with limit \(s\). Now \((1-y)s_N=s_N(1-y)=1-y^{N+1}\), which tends to \(1\). So \(xs=sx=1\). The norm bound is the sum of the norms of the terms. \(\square\)

**Proposition 2.2** (the invertible group is open, and inversion is continuous). Let \(A\) be a nontrivial unital Banach algebra, \(x_0\in G(A)\), and \(\|x-x_0\|<1/\|x_0^{-1}\|\). Then \(x\) is invertible,
\[
x^{-1}=\sum_{n=0}^\infty\big[x_0^{-1}(x_0-x)\big]^n\,x_0^{-1},
\tag{2.2}
\]
\[
\begin{gathered}
\|x^{-1}-x_0^{-1}\|\\
\leq\frac{\|x_0^{-1}\|^2\,\|x-x_0\|}{1-\|x_0^{-1}\|\,\|x-x_0\|}.
\end{gathered}
\tag{2.3}
\]
Consequently \(G(A)\) is open, and \(x\mapsto x^{-1}\) is continuous on \(G(A)\). The distance from \(x_0\in G(A)\) to the set of noninvertible elements is at least \(1/\|x_0^{-1}\|\). If \(x_n\in G(A)\) converge to a noninvertible element, then \(\|x_n^{-1}\|\to\infty\).

**Proof.** Put \(y=x_0^{-1}(x_0-x)\), so \(\|y\|\leq\|x_0^{-1}\|\|x-x_0\|<1\) and \(x=x_0(1-y)\). By (2.1), \(1-y\) is invertible with inverse \(\sum_ny^n\). So \(x\) is a product of invertible elements, and \(x^{-1}=(1-y)^{-1}x_0^{-1}\), which is (2.2). The difference \(x^{-1}-x_0^{-1}=\sum_{n\geq1}y^nx_0^{-1}\) has norm at most \(\|x_0^{-1}\|\,\|y\|/(1-\|y\|)\). Since \(t\mapsto t/(1-t)\) increases on \([0,1)\), this gives (2.3). The distance statement restates the first claim. For the last one, if \(x_n\to x\) and \(x\notin G(A)\), then \(\|x-x_n\|\geq1/\|x_n^{-1}\|\). \(\square\)

In the zero algebra every element is invertible, with inverse \(0\), which is why Proposition 2.2 assumes \(A\neq\{0\}\). [Corollary 5.6(4)](#oa-fnd-bn-09) weakens the hypothesis of Proposition 2.1 to \(r(1-x)<1\).

## 3. Identities and the unitization

This section shows that the norm of an identity can be taken to be \(1\), adjoins an identity to an arbitrary algebra, and puts a C\*-norm on the result when the algebra is a C\*-algebra without identity.

### The norm of the identity

**Proposition 3.1.** Let \(A\) be a nontrivial unital Banach algebra.
1. \(\|1\|\geq1\).
2. Put \(\|x\|_\ell=\sup\{\|xy\|:\|y\|\leq1\}\), the operator norm of left multiplication \(L_x:y\mapsto xy\). This is an algebra norm on \(A\), with
\[
\|x\|/\|1\|\leq\|x\|_\ell\leq\|x\|\quad\text{and}\quad\|1\|_\ell=1 .
\]
So \((A,\|\cdot\|_\ell)\) is a Banach algebra whose norm is equivalent to the given one. If \(\|1\|=1\), the two norms coincide.
3. If \(A\) has an isometric involution, then \(1^*=1\), and \(N(x)=\max(\|x\|_\ell,\|x^*\|_\ell)\) is an equivalent Banach algebra norm with \(N(x^*)=N(x)\) and \(N(1)=1\).
4. If \(A\) is a C\*-algebra, then \(\|1\|=1\).

**Proof.** (1) \(\|1\|=\|1\cdot1\|\leq\|1\|^2\) and \(\|1\|\neq0\).
(2) \(\|xy\|\leq\|x\|\|y\|\) gives \(\|x\|_\ell\leq\|x\|\). Testing \(L_x\) at \(y=1/\|1\|\) gives \(\|x\|_\ell\geq\|x\|/\|1\|\). The map \(x\mapsto L_x\) is linear and \(L_{xy}=L_xL_y\), so \(\|\cdot\|_\ell\) is a submultiplicative seminorm; by the lower bound it is a norm. Equivalent norms have the same Cauchy sequences, so it is complete. Finally \(L_1\) is the identity operator of the nonzero space \(A\), of norm \(1\). If \(\|1\|=1\), the two bounds coincide.
(3) \(1^*\) is an identity: \(1^*x=(x^*1)^*=x\) and \(x1^*=(1x^*)^*=x\). So \(1^*=1\). The function \(N\) is a norm. It is submultiplicative because \(\|(xy)^*\|_\ell=\|y^*x^*\|_\ell\leq\|y^*\|_\ell\|x^*\|_\ell\). Clearly \(N(x^*)=N(x)\), and \(N(1)=1\) because \(1^*=1\). For equivalence, \(\|x\|/\|1\|\leq N(x)\leq\max(\|x\|,\|x^*\|)=\|x\|\).
(4) \(\|1\|=\|1^*1\|=\|1\|^2\) and \(\|1\|\neq0\). \(\square\)

The zero algebra shows that "nontrivial" cannot be dropped: there \(1=0\), and no norm gives \(\|1\|=1\). The left-regular norm of (2) controls \(\|1\|\) but says nothing about the involution. Taking the maximum with \(x\mapsto\|x^*\|_\ell\) in (3) restores isometry without losing \(N(1)=1\). It is common to assume \(\|1\|=1\) whenever an identity exists. By (2) and (3) this costs nothing up to an equivalent norm. We keep the general norm, because every estimate below survives it.

### Adjoining an identity

**Construction 3.2.** For any algebra \(A\), let \(A_1=A\oplus\mathbb C\) with the linear structure of the direct sum and the product
\[
\begin{gathered}
(a,\lambda)(b,\mu)\\
=(ab+\lambda b+\mu a,\ \lambda\mu).
\end{gathered}
\tag{3.1}
\]
If \(A\) has an involution, put \((a,\lambda)^*=(a^*,\bar\lambda)\). Write \(j(a)=(a,0)\), \(q(a,\lambda)=\lambda\), and \(1=(0,1)\). If \(A\) is normed, put \(\|(a,\lambda)\|_1=\|a\|+|\lambda|\).

**Proposition 3.3.**
1. \(A_1\) is a unital algebra with identity \((0,1)\). The map \(j\) is an injective homomorphism onto an ideal \(j(A)\) of codimension one, and \(q\) is a unital homomorphism onto \(\mathbb C\) with kernel \(j(A)\). \(A_1\) is commutative exactly when \(A\) is. If \(A\) has an involution, so does \(A_1\), and \(j\) and \(q\) preserve it.
2. If \(A\) is a normed algebra, so is \((A_1,\|\cdot\|_1)\), with \(\|1\|_1=1\). The map \(j\) is isometric and \(|q(u)|\leq\|u\|_1\). If \(A\) is a Banach algebra, so is \(A_1\), and \(j(A)\) is closed. If the involution of \(A\) is isometric, so is that of \(A_1\).
3. If \(A\) has an identity \(1_A\), then \((a,\lambda)\mapsto(a+\lambda1_A,\lambda)\) is an algebra isomorphism of \(A_1\) onto the product algebra \(A\times\mathbb C\). In particular \(j(1_A)\) is an idempotent of \(A_1\) different from the new identity \((0,1)\). The construction adds a new identity even when \(A\) has one.
4. If \(A\) is a C\*-algebra with a nonzero projection \(p=p^*=p^2\) (for example \(A=\mathbb C\)), then \((A_1,\|\cdot\|_1)\) is not a C\*-algebra.

**Proof.** (1) Both ways of bracketing \((a,\lambda)(b,\mu)(c,\nu)\) give the first coordinate \(abc+\lambda bc+\mu ac+\nu ab+\lambda\mu c+\lambda\nu b+\mu\nu a\) and the second coordinate \(\lambda\mu\nu\). Bilinearity is clear, and \((0,1)\) is an identity. The formulas for \(j\) and \(q\) are homomorphic, and \(\ker q=j(A)\), which is an ideal because \((a,\lambda)(b,0)=(ab+\lambda b,0)\) and \((b,0)(a,\lambda)=(ba+\lambda b,0)\). For the involution, both \(\big((a,\lambda)(b,\mu)\big)^*\) and \((b,\mu)^*(a,\lambda)^*\) equal \((b^*a^*+\bar\lambda b^*+\bar\mu a^*,\bar\lambda\bar\mu)\).
(2) \[
\begin{gathered}
\|ab+\lambda b+\mu a\|+|\lambda\mu|\\
\leq\|a\|\|b\|+|\lambda|\|b\|+|\mu|\|a\|+|\lambda||\mu|\\
=\|(a,\lambda)\|_1\|(b,\mu)\|_1.
\end{gathered}
\] Completeness of a sum norm on \(A\times\mathbb C\) follows coordinatewise. The rest is immediate.
(3) Call the map \(\Phi\). Both \(\Phi\big((a,\lambda)(b,\mu)\big)\) and \(\Phi(a,\lambda)\Phi(b,\mu)\) equal \((ab+\lambda b+\mu a+\lambda\mu1_A,\lambda\mu)\). Its inverse is \((a,\lambda)\mapsto(a-\lambda1_A,\lambda)\). Under \(\Phi\), \(j(1_A)\) becomes \((1_A,0)\), which is not the identity \((1_A,1)\).
(4) In a C\*-algebra, \(\|p\|=\|p^*p\|=\|p\|^2\), so \(\|p\|=1\). The element \(u=(-2p,1)\) is self-adjoint, and \(u^*u=u^2=(4p^2-4p,1)=(0,1)\). So \(\|u^*u\|_1=1\), while \(\|u\|_1^2=9\). \(\square\)

The construction works for every \(A\), whether or not \(A\) already has an identity. Proposition 3.4 below replaces the sum norm by a C\*-norm when \(A\) is a nonunital C\*-algebra, and Section 4 uses \(A_1\) to define the quasi-spectrum.

### A C\*-norm on the unitization

Let \(A\) be a C\*-algebra and \(A_1\) its unitization (Construction 3.2). Since \(j(A)\) is an ideal, each \(u\in A_1\) acts on \(A\) by left multiplication, \(b\mapsto ub\). We identify \(a\in A\) with \(j(a)\) and write \(u=a+\lambda\). Put
\[
p(u)=\sup\{\|ub\|:\ b\in A,\ \|b\|\leq1\}.
\]

**Proposition 3.4.**
1. \(p\) is a submultiplicative seminorm on \(A_1\), \(p(u)\leq\|u\|_1\), and \(p(a)=\|a\|\) for \(a\in A\).
2. \(p(u)^2\leq p(u^*u)\leq p(u^*)p(u)\). Consequently \(p(u^*)=p(u)\) and \(p(u^*u)=p(u)^2\).
3. If \(A\) is not unital, then \(p(u)=0\) only for \(u=0\). If \(A\) has an identity \(1_A\), then \(p(u)=0\) exactly for \(u\in\mathbb C(1_A-1)\).
4. If \(A\) is not unital, then \((A_1,p)\) is a unital C\*-algebra containing \(A\) isometrically as a closed ideal of codimension one. Moreover \(|\lambda|\leq p(a+\lambda)\), so \(p\) equals the norm \(N(a,\lambda)=\max\big(p(a+\lambda),|\lambda|\big)\).

**Proof.** (1) \(\|(a+\lambda)b\|\leq(\|a\|+|\lambda|)\|b\|\) gives \(p(u)\leq\|u\|_1\). Left multiplication is linear in \(u\), and the operator of \(uv\) is the product of the operators of \(u\) and \(v\); so \(p\) is a submultiplicative seminorm. For \(a\in A\), \(p(a)\leq\|a\|\). If \(a\neq0\), test at \(b=a^*/\|a\|\), which has norm one: \(\|ab\|=\|aa^*\|/\|a\|=\|a^*\|^2/\|a\|=\|a\|\).
(2) Let \(b\in A\) with \(\|b\|\leq1\). The elements \(ub\) and \(b^*(u^*u)b\) lie in \(A\), and \((ub)^*(ub)=b^*(u^*u)b\). The C\*-identity in \(A\) gives
\[
\begin{gathered}
\|ub\|^2\\
=\|b^*(u^*u)b\|\\
\leq\|b^*\|\,\|(u^*u)b\|\\
\leq p(u^*u).
\end{gathered}
\]
Take the supremum over \(b\), and use submultiplicativity. If \(p(u)=0\), the same inequality for \(u^*\) gives \(p(u^*)^2\leq p(u)p(u^*)=0\). Otherwise it gives \(p(u)\leq p(u^*)\) and \(p(u^*)\leq p(u)\). In both cases \(p(u^*)=p(u)\), and then \(p(u)^2\leq p(u^*u)\leq p(u)^2\).
(3) Let \(p(a+\lambda)=0\), that is, \(ab+\lambda b=0\) for all \(b\in A\). If \(\lambda=0\), then \(\|a\|=p(a)=0\). If \(\lambda\neq0\), put \(e=-a/\lambda\in A\); then \(eb=b\) for every \(b\), so \(e\) is a left identity of \(A\). Its adjoint is a right identity: \(be^*=(eb^*)^*=b\). Hence \(e=ee^*=e^*\), so \(e\) is a two-sided identity of \(A\), and \(u=\lambda(1-e)=-\lambda(1_A-1)\). So \(p\) has zero kernel when \(A\) is not unital. If \(A\) has an identity \(1_A\), then \((1_A-1)b=b-b=0\) for all \(b\), and \(1_A-1\neq0\) in \(A_1\) because its scalar part is \(-1\).
(4) By (1)–(3), \(p\) is a submultiplicative norm with the C\*-identity and an isometric involution, and it agrees with the norm of \(A\) on \(A\). Next we prove completeness. Look at the functional \(q(a+\lambda)=\lambda\). Its kernel \(A\) is complete for \(p\), hence closed in \((A_1,p)\). A nonzero linear functional with closed kernel is bounded. Indeed, choose \(u_0\) with \(q(u_0)=1\) and put \(\delta=\inf\{p(u_0-k):k\in A\}>0\); if \(q(u)\neq0\), then \(u/q(u)-u_0\in A\), so \(p(u)\geq\delta|q(u)|\). So \(|\lambda|\leq\delta^{-1}p(a+\lambda)\). Also \(\|a\|=p(a)\leq p(a+\lambda)+|\lambda|p(1)\), and \(p(1)\leq1\). So \(p\) is equivalent to the complete norm \(\|\cdot\|_1\), and \((A_1,p)\) is a C\*-algebra. It is unital with \(p(1)=1\) by Proposition 3.1(4), since \(A\neq\{0\}\). Finally, \(q\) is a character of this Banach algebra, and characters of Banach algebras have norm at most \(1\) ([Proposition 10.3(1)](#oa-fnd-bn-17)). So \(|q(u)|\leq p(u)\), and hence \(N=p\). \(\square\)

Parts (1) and (2) hold for every C\*-algebra. Part (3) gives the exact kernel of \(p\): the left-regular seminorm is a norm if and only if \(A\) is not unital. The norm \(N=\max(p,|q|)\) keeps the scalar coordinate, and we call \(A_1\) with this norm the *forced unitization* of \(A\). It is a C\*-algebra for every C\*-algebra \(A\): for nonunital \(A\), (4) shows that \(N=p\), and for unital \(A\) see Exercise 5. The proof of (4) uses the bound \(|\omega(x)|\leq\|x\|\) for characters from Section 10. That bound is proved from Sections 3 and 4 alone, without this proposition, so the argument is not circular.

**Example 3.5.** Let \(\Omega\) be LCH and not compact, and \(A=C_0(\Omega)\), which is not unital by [Proposition 1.2(4)](#oa-fnd-bn-01). For \(u=f+\lambda\), \(p(u)=\sup_{\omega\in\Omega}|f(\omega)+\lambda|\). Indeed, \(\|ub\|_\infty\leq\sup|f+\lambda|\) when \(\|b\|_\infty\leq1\). Conversely, for \(\omega_0\in\Omega\), Urysohn's lemma gives \(b\in C_c(\Omega)\) with \(0\leq b\leq1\) and \(b(\omega_0)=1\), and then \(\|ub\|_\infty\geq|f(\omega_0)+\lambda|\). Since \(f\) vanishes at infinity, \(|\lambda|\leq p(u)\), as (4) predicts. If \(\Omega\) is compact, \(A\) is unital with \(1_A\equiv1\), and \(p(1_A-1)=\sup|1-1|=0\), as (3) predicts.

## 4. The spectrum

### Spectrum and quasi-spectrum

**Definition 4.1.** Let \(A\) be unital and \(x\in A\). The *spectrum* of \(x\) is
\[
\sigma_A(x)=\{\lambda\in\mathbb C :\ \lambda-x\ \text{is not invertible}\},
\]
and its complement \(\rho_A(x)\) is the *resolvent set*. For an arbitrary algebra \(A\) and \(x\in A\), the *quasi-spectrum* is \(\sigma'_A(x)=\sigma_{A_1}(j(x))\), computed in the unitization of [Construction 3.2](#oa-fnd-bn-04). The *spectral radius* is \(r(x)=\sup\{|\lambda|:\lambda\in\sigma'_A(x)\}\in[0,\infty]\).

The quasi-spectrum matters mainly when \(A\) has no identity, but we define it for every \(A\). When \(A\) is unital, part (1) below shows that it is \(\sigma_A(x)\cup\{0\}\), which has the same radius as \(\sigma_A(x)\) whenever \(\sigma_A(x)\) is not empty.

**Proposition 4.2.**
1. \(0\in\sigma'_A(x)\). If \(A\) is unital, \(\sigma'_A(x)=\sigma_A(x)\cup\{0\}\). So \(r(x)=\sup\{|\lambda|:\lambda\in\sigma_A(x)\}\) when \(A\) is unital and \(\sigma_A(x)\neq\varnothing\).
2. Let \(A\) be unital, \(x,y\in A\) and \(\lambda\neq0\). If \(\lambda-xy\) has inverse \(u\), then \(\lambda-yx\) has inverse \(\lambda^{-1}(1+yux)\). Hence \(\sigma_A(xy)\cup\{0\}=\sigma_A(yx)\cup\{0\}\). For every algebra, \(\sigma'_A(xy)=\sigma'_A(yx)\) and \(r(xy)=r(yx)\).
3. If \(\pi:A\to B\) is a unital homomorphism, then \(\sigma_B(\pi(x))\subseteq\sigma_A(x)\). If \(B\) is a subalgebra of the unital algebra \(A\) with \(1_A\in B\), then \(\sigma_A(x)\subseteq\sigma_B(x)\) for \(x\in B\).
4. If \(x\in G(A)\), then \(0\notin\sigma_A(x)\) and \(\sigma_A(x^{-1})=\{\lambda^{-1}:\lambda\in\sigma_A(x)\}\).
5. \(\sigma_A(x-c)=\sigma_A(x)-c\) for \(c\in\mathbb C\), and \(\sigma_A(cx)=c\,\sigma_A(x)\) for \(c\neq0\).

**Proof.** (1) The map \(q:A_1\to\mathbb C\) is a unital homomorphism with \(q(j(x))=0\). If \(j(x)\) had an inverse \(w\), then \(1=q(j(x))q(w)=0\). If \(A\) is unital, Proposition 3.3(3) identifies \(A_1\) with \(A\times\mathbb C\) and \(j(x)\) with \((x,0)\). An element \((a,\mu)\) of \(A\times\mathbb C\) is invertible exactly when \(a\in G(A)\) and \(\mu\neq0\). So \(\lambda-(x,0)=(\lambda-x,\lambda)\) fails to be invertible exactly when \(\lambda\in\sigma_A(x)\) or \(\lambda=0\).

(2) From \((\lambda-xy)u=1\) we get \(xyu=\lambda u-1\), so \(yxyux=\lambda yux-yx\). Hence
\[
\begin{gathered}
(\lambda-yx)(1+yux)\\
=\lambda+\lambda yux-yx-yxyux\\
=\lambda .
\end{gathered}
\]
From \(u(\lambda-xy)=1\) we get \(uxy=\lambda u-1\), so \(yuxyx=\lambda yux-yx\), and \((1+yux)(\lambda-yx)=\lambda\) in the same way. For an arbitrary algebra, apply this in \(A_1\) to \(j(x)\) and \(j(y)\); both quasi-spectra contain \(0\).

(3) \(\pi(\lambda-x)=\lambda-\pi(x)\), and \(\pi\) maps invertible elements to invertible elements ([Section 2](#oa-fnd-bn-02)). For the second claim, an inverse in \(B\) is an inverse in \(A\).

(4) For \(\lambda\neq0\), \(\lambda-x=(-\lambda x)(\lambda^{-1}-x^{-1})\), and \(-\lambda x\) is invertible and commutes with \(\lambda^{-1}-x^{-1}\). So \(\lambda-x\) is invertible exactly when \(\lambda^{-1}-x^{-1}\) is.

(5) \(\lambda-(x-c)=(\lambda+c)-x\) and \(\lambda-cx=c(\lambda/c-x)\). \(\square\)

**Examples 4.3.**
- *The \(\{0\}\) in (2) is needed.* On \(\ell^2(\mathbb N)\) let \(Se_n=e_{n+1}\). Then \(S^*e_0=0\) and \(S^*e_{n+1}=e_n\), so \(S^*S=1\), while \(SS^*\) is the orthogonal projection \(P\) onto the closed span of \(e_1,e_2,\dots\). Since \(0\neq P\neq1\), \(\sigma(P)=\{0,1\}\): for \(\lambda\notin\{0,1\}\) the inverse of \(\lambda-P\) is \(\lambda^{-1}(1-P)+(\lambda-1)^{-1}P\), while \(P\) and \(1-P\) have nonzero kernels. So \(\sigma(SS^*)=\{0,1\}\) and \(\sigma(S^*S)=\{1\}\).
- *Matrices.* In \(M_n(\mathbb C)\), \(xy\) is invertible exactly when \(yx\) is, because \(\det(xy)=\det(yx)\). So there \(\sigma(xy)=\sigma(yx)\).
- *The spectrum depends on the algebra.* Example 4.6 below gives an element whose spectrum is the unit circle in one algebra and the closed unit disc in a closed subalgebra.

### The resolvent; the spectrum is compact

Let \(A\) be a unital Banach algebra and \(x\in A\). Put \(c_1=\max(1,\|1\|)\). If \(A=\{0\}\), every resolvent is \(0\); there \(1/0\) is read as \(\infty\), here and in Section 8.

**Proposition 4.4.**
1. If \(|\lambda|>\|x\|\), then \(\lambda\in\rho_A(x)\),
\[
R_x(\lambda)=\sum_{n=0}^\infty\frac{x^n}{\lambda^{n+1}},
\tag{4.1}
\]
and \(\|R_x(\lambda)\|\leq c_1/(|\lambda|-\|x\|)\).
2. If \(\lambda_0\in\rho_A(x)\) and \(|\lambda-\lambda_0|<1/\|R_x(\lambda_0)\|\), then \(\lambda\in\rho_A(x)\) and
\[
\begin{gathered}
R_x(\lambda)\\
=\sum_{n=0}^\infty(\lambda_0-\lambda)^n\,R_x(\lambda_0)^{n+1}.
\end{gathered}
\tag{4.2}
\]
Hence \(\rho_A(x)\) is open, and \(\operatorname{dist}(\lambda_0,\sigma_A(x))\geq1/\|R_x(\lambda_0)\|\).
3. \(\sigma_A(x)\) is compact and lies in the closed disc of radius \(\|x\|\). For every Banach algebra \(A\) and \(x\in A\), \(\sigma'_A(x)\) is compact and not empty, and \(r(x)\leq\|x\|\).
4. (*Resolvent identity.*) For \(\lambda,\mu\in\rho_A(x)\), \(R_x(\lambda)-R_x(\mu)=(\mu-\lambda)R_x(\lambda)R_x(\mu)\). All resolvents \(R_x(\lambda)\) commute with each other and with every element that commutes with \(x\).
5. \(R_x\) is continuous on \(\rho_A(x)\). For each \(\varphi\in A^*\), \(\varphi\circ R_x\) is given near each \(\lambda_0\in\rho_A(x)\) by a power series in \(\lambda-\lambda_0\); so it is holomorphic, with a continuous derivative.
6. \(\|R_x(\lambda)\|\to0\) as \(|\lambda|\to\infty\), and \(\|R_x(\lambda)\|\to\infty\) as \(\lambda\in\rho_A(x)\) approaches a point of \(\sigma_A(x)\).

**Proof.** (1) Since \(\|x/\lambda\|<1\), (2.1) makes \(1-x/\lambda\) invertible with inverse \(\sum_n(x/\lambda)^n\). So \(\lambda-x=\lambda(1-x/\lambda)\) is invertible, with inverse (4.1). As \(\|x^0\|=\|1\|\leq c_1\) and \(\|x^n\|\leq\|x\|^n\), the norm is at most \(\sum_nc_1\|x\|^n/|\lambda|^{n+1}=c_1/(|\lambda|-\|x\|)\).
(2) Write \(\lambda-x=(\lambda_0-x)\big[1-(\lambda_0-\lambda)R_x(\lambda_0)\big]\). Since \(\|(\lambda_0-\lambda)R_x(\lambda_0)\|<1\), the bracket is invertible by (2.1), with inverse \(\sum_n(\lambda_0-\lambda)^nR_x(\lambda_0)^n\), which commutes with \(R_x(\lambda_0)\). This gives (4.2). The whole disc of radius \(1/\|R_x(\lambda_0)\|\) about \(\lambda_0\) lies in \(\rho_A(x)\).
(3) By (1) and (2), \(\sigma_A(x)\) is closed and bounded. For an arbitrary Banach algebra, apply this in \(A_1\), where \(\|j(x)\|_1=\|x\|\). The quasi-spectrum contains \(0\) by Proposition 4.2(1).
(4) \(\lambda-x\) and \(\mu-x\) commute, so their inverses commute, and \[
\begin{gathered}
R_x(\lambda)-R_x(\mu)\\
=R_x(\lambda)\big[(\mu-x)-(\lambda-x)\big]R_x(\mu).
\end{gathered}
\] If \(y\) commutes with \(x\), it commutes with \(\lambda-x\) and hence with its inverse.
(5) The series (4.2) converges uniformly on smaller discs about \(\lambda_0\). Apply \(\varphi\) term by term.
(6) The first claim is (1). The second follows from (2): \(\|R_x(\lambda)\|\geq1/\operatorname{dist}(\lambda,\sigma_A(x))\). \(\square\)

**Examples 4.5** (completeness is needed).
- Give \(\mathbb C[z]\) the norm \(\|p\|=\max_{|z|\leq1}|p(z)|\). It is a unital normed algebra, but not complete. A nonzero polynomial multiple of \(z-\lambda\) has degree at least one, so \(z-\lambda\) is never invertible: \(\sigma(z)=\mathbb C\), which is not bounded.
- In the field \(\mathbb C(z)\) of rational functions, every \(z-\lambda\) is invertible, so \(\sigma(z)=\varnothing\). By the Gelfand–Mazur theorem ([Corollary 5.3](#oa-fnd-bn-08)), \(\mathbb C(z)\) carries no algebra norm at all.

### The spectrum depends on the algebra

**Example 4.6.** Let \(B=C(\mathbb T)\), and let \(A\) be the closure in \(B\) of the polynomials in \(z\) (the disc algebra, seen on the circle). Then \(\sigma_B(z)=\mathbb T\), while \(\sigma_A(z)\) is the closed unit disc. In general, if \(A\) is a closed subalgebra of a unital Banach algebra \(B\) with \(1_B\in A\), then \(\sigma_B(x)\subseteq\sigma_A(x)\), and every boundary point of \(\sigma_A(x)\) lies in \(\sigma_B(x)\).

**Proof.** In \(B\), \(z-\lambda\) is invertible exactly when it has no zero on \(\mathbb T\), that is, when \(|\lambda|\neq1\). For \(A\), write \(c_n(g)=\frac1{2\pi}\int_0^{2\pi}g(e^{i\theta})e^{-in\theta}\,d\theta\). Polynomials in \(z\) have \(c_n=0\) for \(n<0\), and \(|c_n(g)-c_n(p)|\leq\|g-p\|_\infty\), so every \(g\in A\) has \(c_n(g)=0\) for \(n<0\). Suppose \(|\lambda|<1\) and \((z-\lambda)g=1\) with \(g\in A\). Comparing coefficients, \(c_{n-1}(g)-\lambda c_n(g)\) is \(1\) for \(n=0\) and \(0\) otherwise. If \(\lambda=0\), this gives \(c_{-1}(g)=1\), which is impossible. If \(\lambda\neq0\), it gives \(c_0(g)=-1/\lambda\) and \(c_n(g)=c_{n-1}(g)/\lambda\) for \(n\geq1\), so \(|c_n(g)|=|\lambda|^{-n-1}\to\infty\), although \(|c_n(g)|\leq\|g\|_\infty\). So the open disc lies in \(\sigma_A(z)\). Since \(\sigma_A(z)\) is closed and \(\|z\|=1\), \(\sigma_A(z)\) is the closed disc.

For the general claim, \(\sigma_B(x)\subseteq\sigma_A(x)\) is Proposition 4.2(3). Let \(\lambda\) be a boundary point of \(\sigma_A(x)\), and suppose \(\lambda\notin\sigma_B(x)\). Choose \(\lambda_n\in\rho_A(x)\) with \(\lambda_n\to\lambda\). In \(B\), \((\lambda_n-x)^{-1}\to(\lambda-x)^{-1}\) by continuity of inversion ([Proposition 2.2](#oa-fnd-bn-02)). The left sides lie in the closed set \(A\), so \((\lambda-x)^{-1}\in A\), and \(\lambda\in\rho_A(x)\). This contradicts \(\lambda\in\sigma_A(x)\), which holds because \(\sigma_A(x)\) is closed. \(\square\)

This cannot happen for a C\*-subalgebra of a C\*-algebra: there the two spectra agree. This is proved in the [next lesson, on C\*-algebras](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-06).

## 5. Nonempty spectrum and the spectral radius formula

### The spectrum is not empty; the Gelfand–Mazur theorem

**Lemma 5.1** (circle means). Let \(0\leq r_1<r_2\leq\infty\), and let \(g\) be holomorphic with a continuous derivative on the annulus \(\{r_1<|\lambda|<r_2\}\). Then
\[
M(\rho)=\frac1{2\pi}\int_0^{2\pi}g(\rho e^{i\theta})\,d\theta
\]
does not depend on \(\rho\in(r_1,r_2)\). If \(g\) is holomorphic with a continuous derivative on the disc \(\{|\lambda|<r_2\}\), then \(M(\rho)=g(0)\) for \(0<\rho<r_2\).

**Proof.** The integrand has the \(\rho\)-derivative \(g'(\rho e^{i\theta})e^{i\theta}\), which is continuous in \((\rho,\theta)\), so we may differentiate under the integral sign. For \(\rho>0\),
\[
\begin{gathered}
M'(\rho)\\
=\frac1{2\pi}\int_0^{2\pi}g'(\rho e^{i\theta})e^{i\theta}\,d\theta\\
=\frac1{2\pi i\rho}\int_0^{2\pi}\frac{d}{d\theta}\,g(\rho e^{i\theta})\,d\theta\\
=0,
\end{gathered}
\]
because \(\theta\mapsto g(\rho e^{i\theta})\) has period \(2\pi\). In the second case \(M(\rho)\to g(0)\) as \(\rho\to0\), by continuity of \(g\) at \(0\). \(\square\)

This lemma is all the complex analysis that this section needs.

**Theorem 5.2** (the spectrum is not empty). If \(A\) is a nontrivial unital Banach algebra, then \(\sigma_A(x)\neq\varnothing\) for every \(x\in A\).

**Proof.** Suppose \(\sigma_A(x)=\varnothing\), and let \(\varphi\in A^*\). The function \(g=\varphi\circ R_x\) is holomorphic on \(\mathbb C\) with a continuous derivative, by [Proposition 4.4(5)](#oa-fnd-bn-07). By Lemma 5.1 with \(r_2=\infty\), and by the bound \(\|R_x(\lambda)\|\leq c_1/(|\lambda|-\|x\|)\) of Proposition 4.4(1), for \(\rho>\|x\|\),
\[
|g(0)|=|M(\rho)|\leq\max_{|\lambda|=\rho}|g(\lambda)|\leq\frac{c_1\|\varphi\|}{\rho-\|x\|}.
\]
Letting \(\rho\to\infty\) gives \(\varphi(R_x(0))=0\). Since this holds for every \(\varphi\), the Hahn–Banach theorem gives \(R_x(0)=-x^{-1}=0\). Then \(1=xx^{-1}=0\), which contradicts \(A\neq\{0\}\). \(\square\)

In the zero algebra, \(0-0=0=1\) is invertible, so \(\sigma(0)=\varnothing\); the hypothesis \(A\neq\{0\}\) is needed. The usual proof applies Liouville's theorem to \(\varphi\circ R_x\); Lemma 5.1 is the part of that argument that is needed here.

**Corollary 5.3** (Gelfand–Mazur theorem, for normed algebras). Let \(A\) be a nontrivial unital normed algebra, not necessarily complete, in which every nonzero element is invertible. Then \(A=\mathbb C1\), and \(\lambda\mapsto\lambda1\) is the only unital algebra isomorphism of \(\mathbb C\) onto \(A\).

**Proof.** Let \(\hat A\) be the completion of \(A\). To extend multiplication explicitly, represent \(x,y\in\hat A\) by Cauchy sequences \(x_n,y_n\in A\), and define \(xy\) to be the class of \(x_ny_n\). These sequences are bounded, and
\[
\begin{aligned}
\|x_ny_n-x_my_m\|
&\leq\|x_n\|\|y_n-y_m\|\\
&\quad+\|x_n-x_m\|\|y_m\|\longrightarrow0 .
\end{aligned}
\]
The same estimate for two choices of representing sequences proves independence of those choices. The bound \(\|xy\|\leq\|x\|\|y\|\), bilinearity, associativity and the identity laws pass to the limit from \(A\). Thus \(\hat A\) is a Banach algebra with the same identity, still nonzero under the isometric embedding of \(A\).

Let \(x\in A\). By Theorem 5.2 there is \(\lambda\in\sigma_{\hat A}(x)\). Then \(x-\lambda\) is not invertible in \(\hat A\), so it is not invertible in \(A\), and therefore \(x-\lambda=0\). A unital algebra homomorphism \(\psi:\mathbb C\to A\) satisfies \(\psi(\lambda)=\lambda\psi(1)=\lambda1\). \(\square\)

Complex scalars matter: over the real field the statement fails, since \(\mathbb C\) and the quaternions, with their usual absolute values, are real normed division algebras.

### The spectral radius formula

**Theorem 5.4** (spectral radius formula). For every element \(x\) of a Banach algebra \(A\),
\[
\begin{gathered}
r(x)\\
=\lim_{n\to\infty}\|x^n\|^{1/n}\\
=\inf_{n\geq1}\|x^n\|^{1/n}.
\end{gathered}
\tag{5.1}
\]

Step 1 below gives the lower spectral-radius bound directly, before any limit of roots is known to exist. Remark 5.5 supplies a second proof using submultiplicativity.

**Proof.** By Proposition 4.2(1) and [Proposition 3.3(2)](#oa-fnd-bn-04) we may compute in \(A_1\), where \(\|j(x)^n\|_1=\|x^n\|\). So let \(A\) be unital. If \(A=\{0\}\), both sides are \(0\), since \(\sigma'_A(x)=\{0\}\). Let \(A\) be nontrivial.

*Step 1: \(r(x)\leq\|x^n\|^{1/n}\) for every \(n\geq1\).* Let \(\lambda\in\sigma_A(x)\). In \(A\),
\[
\begin{gathered}
x^n-\lambda^n\\
=(x-\lambda)p(x)\\
=p(x)(x-\lambda),\\
p(x)\\
=\sum_{k=0}^{n-1}\lambda^{n-1-k}x^k .
\end{gathered}
\]
If \(x^n-\lambda^n\) had an inverse \(w\), then \(p(x)w\) would be a right inverse and \(wp(x)\) a left inverse of \(x-\lambda\), which is not invertible. So \(\lambda^n\in\sigma_A(x^n)\), and \(|\lambda|^n\leq\|x^n\|\) because the spectrum of \(x^n\) lies in the disc of radius \(\|x^n\|\) ([Proposition 4.4(1)](#oa-fnd-bn-07)). Take the supremum over \(\lambda\).

*Step 2: \(\limsup_n\|x^n\|^{1/n}\leq r(x)\).* Fix \(n\geq0\) and \(\varphi\in A^*\). Since \(\sigma_A(x)\) lies in the closed disc of radius \(r(x)\), the function \(g(\lambda)=\lambda^{n+1}\varphi(R_x(\lambda))\) is holomorphic with a continuous derivative on \(\{|\lambda|>r(x)\}\) (Proposition 4.4(5)). For \(\rho>\|x\|\) the series (4.1) converges uniformly on \(|\lambda|=\rho\), and integrating term by term gives
\[
\begin{gathered}
\frac1{2\pi}\int_0^{2\pi}g(\rho e^{i\theta})\,d\theta\\
=\sum_{k\geq0}\varphi(x^k)\,\frac1{2\pi}\int_0^{2\pi}(\rho e^{i\theta})^{n-k}\,d\theta\\
=\varphi(x^n).
\end{gathered}
\]
By Lemma 5.1, the left side is the same for every \(\rho>r(x)\). So \(|\varphi(x^n)|\leq\rho^{n+1}m(\rho)\|\varphi\|\) for every \(\rho>r(x)\), where \(m(\rho)=\max_{|\lambda|=\rho}\|R_x(\lambda)\|\) is finite because \(R_x\) is continuous. By the Hahn–Banach theorem, \(\|x^n\|\leq\rho^{n+1}m(\rho)\) for all \(n\). Hence \(\limsup_n\|x^n\|^{1/n}\leq\rho\), and we let \(\rho\) decrease to \(r(x)\).

Steps 1 and 2 give \[
\begin{gathered}
r(x)\\
\leq\inf_n\|x^n\|^{1/n}\\
\leq\liminf_n\|x^n\|^{1/n}\\
\leq\limsup_n\|x^n\|^{1/n}\\
\leq r(x).
\end{gathered}
\] \(\square\)

**Remark 5.5.** Submultiplicativity alone shows that the limit in (5.1) exists. Here is the elementary argument often called Fekete’s lemma in this multiplicative form. Put \(s_n=\|x^n\|\). If some \(s_k=0\), all powers from \(k\) onwards are zero and the limit is zero. Otherwise fix \(k\), write \(n=qk+r\) with \(0\leq r<k\), and put \(C_k=\max(1,s_1,\ldots,s_{k-1})\), with \(C_1=1\). Submultiplicativity gives \(s_n\leq C_ks_k^q\), including \(r=0\) without an identity factor. Hence \(\limsup_ns_n^{1/n}\leq s_k^{1/k}\). Taking the infimum over \(k\), and noting that every \(s_n^{1/n}\) is at least that infimum, proves convergence to \(\inf_{k\geq1}s_k^{1/k}\). The content of Theorem 5.4 is that this limit is the spectral radius.

**Corollary 5.6.**
1. \(r(x^k)=r(x)^k\) and \(r(cx)=|c|\,r(x)\).
2. \(r(xy)=r(yx)\) for all \(x,y\).
3. If \(xy=yx\), then \(r(xy)\leq r(x)r(y)\) and \(r(x+y)\leq r(x)+r(y)\).
4. If \(A\) is unital and \(r(1-x)<1\), then \(x\) is invertible, and the series (2.1) converges absolutely.

**Proof.** (1) follows from (5.1). (2) is Proposition 4.2(2). (3) \((xy)^n=x^ny^n\) gives the first bound. For the second, fix \(\varepsilon>0\). By (5.1) there is \(C\geq1\) with \(\|x^k\|\leq C(r(x)+\varepsilon)^k\) and \(\|y^k\|\leq C(r(y)+\varepsilon)^k\) for all \(k\geq0\). The binomial theorem holds for commuting elements, and gives \(\|(x+y)^n\|\leq C^2(r(x)+r(y)+2\varepsilon)^n\). (4) Choose \(\rho\) with \(r(1-x)<\rho<1\). By (5.1), \(\|(1-x)^n\|\leq\rho^n\) for large \(n\), so the series converges absolutely, and the proof of Proposition 2.1 applies. \(\square\)

**Examples 5.7.**
- A nonzero nilpotent element \(N\) (\(N^m=0\)) has \(r(N)=0<\|N\|\).
- *The Volterra operator.* On \(C([0,1])\) with the supremum norm, let \((Vf)(t)=\int_0^tf(s)\,ds\). Put \(W_n(t)=\int_0^t(t-s)^{n-1}f(s)/(n-1)!\,ds\). The fundamental theorem gives \(W_1=Vf\). For \(n\geq2\), the moving-endpoint formula in [Lemma 0.1(4) of the Cauchy lesson](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-07) gives \(W_n'=W_{n-1}\) and \(W_n(0)=0\). Thus \(W_n=VW_{n-1}\) by the fundamental theorem, and induction gives \(V^nf=W_n\). So \(\|V^n\|=1/n!\), with equality at \(f\equiv1\) and \(t=1\). Since at least half of the factors of \(n!\) are at least \(n/2\), \((n!)^{1/n}\geq(n/2)^{1/2}\to\infty\). So \(r(V)=0\). The spectrum is not empty (Theorem 5.2) and lies in \(\{0\}\), so \(\sigma(V)=\{0\}\), although \(V\neq0\).
- *Commutativity is needed in (3).* In \(M_2(\mathbb C)\), \(E_{12}\) and \(E_{21}\) square to \(0\), so each has spectral radius \(0\). But \(E_{12}+E_{21}\) has eigenvalues \(\pm1\), and \(E_{12}E_{21}=E_{11}\) has eigenvalues \(0,1\); both have spectral radius \(1\).
- *Self-adjoint elements of a C\*-algebra.* If \(x=x^*\), then \(\|x^2\|=\|x^*x\|=\|x\|^2\), so \(\|x^{2^k}\|=\|x\|^{2^k}\) for all \(k\), and (5.1) along the subsequence \(2^k\) gives \(r(x)=\|x\|\). The same holds for normal elements; this is proved in the [next lesson, on C\*-algebras](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-02).

**Remark 5.8** (at most one C\*-norm). A \(*\)-algebra carries at most one norm that makes it a C\*-algebra. Indeed, let \(N\) be such a norm and \(u\) an element. Since \(u^*u\) is self-adjoint, the last example gives \(N(u)^2=N(u^*u)=r(u^*u)\). The spectral radius \(r(u^*u)\) is determined by the quasi-spectrum of \(u^*u\), which is defined algebraically and does not depend on the norm. In particular, for a nonunital C\*-algebra \(A\), the C\*-norm \(p\) on \(A_1\) of [Proposition 3.4](#oa-fnd-bn-05) is the only norm that makes \(A_1\) a C\*-algebra.

## 6. The holomorphic functional calculus

For a polynomial \(p\), the element \(p(x)\) makes sense in every unital algebra. This section defines \(f(x)\) for every function \(f\) that is holomorphic on a neighbourhood of \(\sigma_A(x)\), by Cauchy's integral formula with the resolvent in place of \((\lambda-z)^{-1}\). It then proves that \(f\mapsto f(x)\) is a homomorphism, and that the spectrum of \(f(x)\) is \(f(\sigma_A(x))\).

### Paths, cycles and integrals

A *path* is a piecewise continuously differentiable map \(\gamma:[a,b]\to\mathbb C\). It is *closed* if \(\gamma(a)=\gamma(b)\). A *cycle* \(\Gamma\) is a finite family of closed paths \(\gamma_1,\dots,\gamma_m\), read as a formal sum. \(\Gamma^*\) is the union of their images, a compact set, and \(\ell(\Gamma)\) is the total length. For a continuous map \(F\) from \(\Gamma^*\) into a Banach space \(X\),
\[
\int_\Gamma F(\lambda)\,d\lambda=\sum_{k=1}^m\int_{a_k}^{b_k}F(\gamma_k(t))\,\gamma_k'(t)\,dt .
\]
Each term is the Riemann integral of a piecewise continuous \(X\)-valued function on an interval. It exists for the same reason as for scalar functions: uniform continuity makes the Riemann sums a Cauchy net, and \(X\) is complete. The integral is linear in \(F\), satisfies \(\|\int_\Gamma F\|\leq\ell(\Gamma)\sup_{\Gamma^*}\|F\|\), and commutes with bounded linear maps: \(T\int_\Gamma F=\int_\Gamma T\circ F\). This applies to functionals, and to multiplication on either side by a fixed element of a Banach algebra. Uniform limits pass through the integral. For a continuous \(F\) on \(\Gamma_1^*\times\Gamma_2^*\) the two iterated integrals agree: apply a functional, use the scalar statement for continuous functions on rectangles, and then the Hahn–Banach theorem. The *index* of a point \(z\notin\Gamma^*\) is
\[
\operatorname{Ind}_\Gamma(z)=\frac1{2\pi i}\int_\Gamma\frac{d\lambda}{\lambda-z}.
\]
A cycle \(\Gamma\) *surrounds* a compact set \(K\) in an open set \(U\supseteq K\) if \(\Gamma^*\subseteq U\setminus K\), \(\operatorname{Ind}_\Gamma=1\) on \(K\), and \(\operatorname{Ind}_\Gamma=0\) on \(\mathbb C\setminus U\). The empty cycle surrounds the empty set.

We use two facts proved in [Cauchy's theorem for cycles and its consequences](cauchy-s-theorem-for-cycles-and-its-consequences.md), cited as *the lesson on Cauchy's theorem*.

**Theorem 6.1** (Cauchy's theorem). Let \(U\subseteq\mathbb C\) be open and let \(\Gamma\) be a cycle in \(U\) with \(\operatorname{Ind}_\Gamma(\alpha)=0\) for every \(\alpha\notin U\). Let \(g:U\to X\) be a map into a Banach space such that \(\varphi\circ g\) is holomorphic for every \(\varphi\in X^*\). Then \(g\) is continuous, \(\int_\Gamma g(\lambda)\,d\lambda=0\), and
\[
\begin{gathered}
g(z)\operatorname{Ind}_\Gamma(z)\\
=\frac1{2\pi i}\int_\Gamma\frac{g(\lambda)}{\lambda-z}\,d\lambda\\
(z\in U\setminus\Gamma^*).
\end{gathered}
\]

This is Theorem 6.1(1)–(2) of the lesson on Cauchy's theorem. Its scalar case is Theorem 4.2 there. Applying a functional \(\varphi\in X^*\) reduces both formulas to the scalar case, and the Hahn–Banach theorem then gives them in \(X\).

We use the formula only at points of index \(1\) or \(0\). At a point \(z\) of index \(0\) it is the first conclusion, applied to \(\lambda\mapsto g(\lambda)/(\lambda-z)\) on \(U\setminus\{z\}\). Applied on a disc, the formula gives the Taylor expansion of a holomorphic function at each point, in the usual way.

**Theorem 6.2** (surrounding cycles). If \(K\subseteq U\subseteq\mathbb C\) with \(K\) compact and \(U\) open, some cycle made of finitely many oriented segments surrounds \(K\) in \(U\).

This is Theorem 5.1 of the lesson on Cauchy's theorem.

**Lemma 6.3** (index). Let \(\Gamma\) be a cycle. On \(\mathbb C\setminus\Gamma^*\), the function \(\operatorname{Ind}_\Gamma\) takes integer values, is constant on each connected component, and is \(0\) on the unbounded component. For the positively oriented circle \(|\lambda-c|=\rho\), the index is \(1\) on the open disc and \(0\) outside the closed disc.

**Proof.** Let \(\gamma:[a,b]\to\mathbb C\) be a closed path and \(z\notin\gamma([a,b])\). Put \(h(t)=\int_a^t\gamma'(s)/(\gamma(s)-z)\,ds\). The continuous function \(F(t)=e^{-h(t)}(\gamma(t)-z)\) has derivative \(e^{-h}\big(-h'(\gamma-z)+\gamma'\big)=0\) wherever \(\gamma\) is differentiable, so \(F\) is constant. Since \(\gamma(b)=\gamma(a)\neq z\), \(F(b)=F(a)\) gives \(e^{-h(b)}=1\), so \(h(b)/(2\pi i)\) is an integer. The index of a cycle is a sum of such integers. For \(z,w\notin\Gamma^*\), with \(d(\cdot)=\operatorname{dist}(\cdot,\Gamma^*)\),
\[
|\operatorname{Ind}_\Gamma(z)-\operatorname{Ind}_\Gamma(w)|\leq\frac{\ell(\Gamma)\,|z-w|}{2\pi\,d(z)\,d(w)} .
\]
So \(\operatorname{Ind}_\Gamma\) is continuous and integer-valued, hence constant on components. Also \(|\operatorname{Ind}_\Gamma(z)|\leq\ell(\Gamma)/(2\pi d(z))<1\) when \(d(z)\) is large, so the index is \(0\) far out, hence on the whole unbounded component. For the circle, the index at the centre is \(\frac1{2\pi i}\int_0^{2\pi}\frac{i\rho e^{it}}{\rho e^{it}}\,dt=1\). \(\square\)

Two sets built from a cycle \(\Gamma\) that surrounds a compact set \(K\) in an open set \(U\) are used below:
\[
\begin{gathered}
O_\Gamma\\
=\{z\notin\Gamma^*:\operatorname{Ind}_\Gamma(z)=1\},\\
K_\Gamma\\
=\Gamma^*\cup\{z\notin\Gamma^*:\operatorname{Ind}_\Gamma(z)\neq0\}.
\end{gathered}
\]
By Lemma 6.3, \(O_\Gamma\) is open, and it contains \(K\). The set \(K_\Gamma\) is closed, since its complement is the open set where the index is \(0\), and bounded, since the index is \(0\) on the unbounded component; so \(K_\Gamma\) is compact. Both sets lie in \(U\), because \(\Gamma^*\subseteq U\) and the index is \(0\) off \(U\).

### Definition of the calculus

**Definition 6.4** (holomorphic functional calculus). Let \(A\) be a unital Banach algebra, \(x\in A\), \(U\subseteq\mathbb C\) open with \(\sigma_A(x)\subseteq U\), and \(f\in H(U)\). Choose a cycle \(\Gamma\) that surrounds \(\sigma_A(x)\) in \(U\), which exists by Theorem 6.2, and put
\[
\begin{gathered}
f(x)\\
=\frac1{2\pi i}\int_\Gamma f(\lambda)\,(\lambda-x)^{-1}\,d\lambda\\
=\frac1{2\pi i}\int_\Gamma f(\lambda)\,R_x(\lambda)\,d\lambda .
\end{gathered}
\tag{6.1}
\]
The integrand is continuous on \(\Gamma^*\), because \(\Gamma^*\subseteq\rho_A(x)\) and the resolvent is continuous there ([Proposition 4.4(5)](#oa-fnd-bn-07)).

**Proposition 6.5.**
1. Every cycle that surrounds \(\sigma_A(x)\) in \(U\) gives the same element \(f(x)\).
2. If \(f\in H(U)\) and \(g\in H(V)\) agree on an open set \(W\) with \(\sigma_A(x)\subseteq W\subseteq U\cap V\), then \(f(x)=g(x)\). So \(f(x)\) depends only on the germ of \(f\) at \(\sigma_A(x)\), and (6.1) defines \(f(x)\) for every \(f\) holomorphic on some neighbourhood of \(\sigma_A(x)\). These functions form an algebra, with the operations taken on the intersection of the domains.
3. For \(\varphi\in A^*\), \(\varphi(f(x))=\frac1{2\pi i}\int_\Gamma f(\lambda)\,\varphi(R_x(\lambda))\,d\lambda\).
4. \(f(x)\) commutes with every element of \(A\) that commutes with \(x\).
5. If \(\chi:A\to\mathbb C\) is a unital homomorphism, then \(\chi(f(x))=f(\chi(x))\).

**Proof.** (1) Let \(\Gamma\) and \(\Gamma'\) both surround \(\sigma_A(x)\) in \(U\). Put \(V=U\setminus\sigma_A(x)\), an open set, and let \(\Gamma-\Gamma'\) be the cycle formed by the paths of \(\Gamma\) and the reversed paths of \(\Gamma'\). It lies in \(V\). For \(\alpha\notin V\), either \(\alpha\notin U\), where both indices are \(0\), or \(\alpha\in\sigma_A(x)\), where both are \(1\); so \(\operatorname{Ind}_{\Gamma-\Gamma'}(\alpha)=0\). The map \(\lambda\mapsto f(\lambda)R_x(\lambda)\) from \(V\) to \(A\) becomes holomorphic after any functional is applied (Proposition 4.4(5)). By Cauchy's theorem 6.1, its integral over \(\Gamma-\Gamma'\) is \(0\).
(2) A cycle that surrounds \(\sigma_A(x)\) in \(W\) also surrounds it in \(U\) and in \(V\), because its index is \(0\) off \(W\). Compute both \(f(x)\) and \(g(x)\) with it.
(3) and (4) Functionals and multiplications pass through the integral, and every \(R_x(\lambda)\) commutes with the elements that commute with \(x\) (Proposition 4.4(4)).
(5) \(\chi\) is continuous, because a character of a Banach algebra has norm at most \(1\) ([Proposition 10.3(1)](#oa-fnd-bn-17); its proof does not use the calculus). Applying \(\chi\) to \((\lambda-x)R_x(\lambda)=1\) gives \(\chi(R_x(\lambda))=(\lambda-\chi(x))^{-1}\). Also \(\chi(x)\in\sigma_A(x)\): otherwise \(\chi(x)-x\) would be invertible, and \(1=\chi\big((\chi(x)-x)(\chi(x)-x)^{-1}\big)=0\). By Cauchy's theorem 6.1 for the scalar function \(f\) at the point \(\chi(x)\),
\[
\begin{gathered}
\chi(f(x))\\
=\frac1{2\pi i}\int_\Gamma\frac{f(\lambda)}{\lambda-\chi(x)}\,d\lambda\\
=f(\chi(x))\operatorname{Ind}_\Gamma(\chi(x))\\
=f(\chi(x)).\\
\square
\end{gathered}
\]

**Remark 6.6** (one circle or one path). Let \(C=\partial D(c,r)\) be positively oriented, with \(\sigma_A(x)\subseteq D(c,r)\) and \(\bar D(c,r)\subseteq U\). Then [Lemma 1.1 of the Cauchy lesson](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-01) gives index \(1\) on the spectrum and \(0\) outside \(U\), so this one circle surrounds \(\sigma_A(x)\) in \(U\). More generally a single closed path with these two index conditions is a surrounding cycle and may be used in (6.1). The precise index conditions are all the calculus needs.

The requirement that the region bounded by \(C\) lie in \(U\) cannot be dropped. Take \(A=\mathbb C\), \(x=0\), \(a\neq0\), \(U=\mathbb C\setminus\{a\}\) and \(f(\lambda)=1/(\lambda-a)\). The circle \(|\lambda|=|a|/2\) gives \(\frac1{2\pi i}\oint f(\lambda)\lambda^{-1}\,d\lambda=-1/a\), while the circle \(|\lambda|=2|a|\) gives \(-1/a+1/a=0\). If the second circle were allowed, it would give \(f(x)=0\) and, for \(g(\lambda)=\lambda-a\), \(g(x)=-a\), but \((fg)(x)=1\); so the product rule of Theorem 6.7 below would fail.

Even with this requirement, one curve reaches fewer functions than cycles do. If \(\sigma_A(x)\) has two separated pieces, the function that is \(0\) near one piece and \(1\) near the other is holomorphic near \(\sigma_A(x)\), but no single curve whose inside lies in its domain encloses both pieces. Example 6.12 uses exactly this function.

*Nonunital algebras.* If \(A\) has no identity, apply the calculus in \(A_1\) to \(j(x)\), whose spectrum is \(\sigma'_A(x)\). Since \(q\) is a unital homomorphism with \(q(j(x))=0\), part (5) gives \(q(f(x))=f(0)\). So \(f(x)\in j(A)\) exactly when \(f(0)=0\). The [next lesson](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-08) proves the analogue for the continuous functional calculus of a normal element of a C\*-algebra.

### The calculus is a unital homomorphism

**Theorem 6.7** (the calculus is a homomorphism). Let \(A\) be a unital Banach algebra, \(x\in A\), and \(U\supseteq\sigma_A(x)\) open. The map \(f\mapsto f(x)\) from \(H(U)\) to \(A\) is a unital algebra homomorphism: it is linear, \((fg)(x)=f(x)g(x)\), \(1(x)=1\), and \(u(x)=x\) for \(u(\lambda)=\lambda\). So \(p(x)\) has its usual meaning for every polynomial \(p\). The map is continuous: if \(f_n\to f\) uniformly on compact subsets of \(U\), then \(f_n(x)\to f(x)\). Any two elements \(f(x),g(x)\) commute.

The proof below uses cycles satisfying the exact index conditions. Remark 6.6 explains the conditions required for a single curve, and Example 6.12 shows why cycles are useful for disconnected spectra.

**Proof.** Linearity is clear.

*Products.* Choose a cycle \(\Gamma_2\) that surrounds \(\sigma_A(x)\) in \(U\). The set \(K_2=K_{\Gamma_2}\), defined after Lemma 6.3, is compact and lies in \(U\); choose a cycle \(\Gamma_1\) that surrounds \(K_2\) in \(U\). Since \(\sigma_A(x)\subseteq K_2\), \(\Gamma_1\) also surrounds \(\sigma_A(x)\) in \(U\). Moreover \(\Gamma_1^*\cap\Gamma_2^*=\varnothing\), \(\operatorname{Ind}_{\Gamma_2}(\lambda)=0\) for \(\lambda\in\Gamma_1^*\) (such \(\lambda\) lie outside \(K_2\)), and \(\operatorname{Ind}_{\Gamma_1}(\mu)=1\) for \(\mu\in\Gamma_2^*\subseteq K_2\). By the resolvent identity, for \(\lambda\in\Gamma_1^*\) and \(\mu\in\Gamma_2^*\),
\[
R_x(\lambda)R_x(\mu)=\frac{R_x(\mu)-R_x(\lambda)}{\lambda-\mu}.
\tag{6.2}
\]
With the rules for integrals stated at the start of this section,
\[
\begin{gathered}
f(x)g(x)\\
=\frac1{(2\pi i)^2}\int_{\Gamma_1}\int_{\Gamma_2}f(\lambda)g(\mu)R_x(\lambda)R_x(\mu)\,d\mu\,d\lambda\\
=I_1-I_2,
\end{gathered}
\]
where
\[
\begin{gathered}
I_1\\
=\frac1{(2\pi i)^2}\int_{\Gamma_2}g(\mu)R_x(\mu)\Big(\int_{\Gamma_1}\frac{f(\lambda)}{\lambda-\mu}\,d\lambda\Big)d\mu,\\
I_2\\
=\frac1{(2\pi i)^2}\int_{\Gamma_1}f(\lambda)R_x(\lambda)\Big(\int_{\Gamma_2}\frac{g(\mu)}{\lambda-\mu}\,d\mu\Big)d\lambda .
\end{gathered}
\]
By Cauchy's theorem 6.1 for \(g\), the inner integral of \(I_2\) is \(-2\pi i\operatorname{Ind}_{\Gamma_2}(\lambda)g(\lambda)=0\), so \(I_2=0\). By Cauchy's theorem 6.1 for \(f\), the inner integral of \(I_1\) is \(2\pi i\operatorname{Ind}_{\Gamma_1}(\mu)f(\mu)=2\pi i f(\mu)\). So \(I_1=\frac1{2\pi i}\int_{\Gamma_2}f(\mu)g(\mu)R_x(\mu)\,d\mu=(fg)(x)\).

*The functions \(1\) and \(u\).* Both are entire, so by Proposition 6.5(2) we may compute them with \(U=\mathbb C\) and \(\Gamma\) the positively oriented circle \(|\lambda|=\rho\), where \(\rho>\|x\|\). By Lemma 6.3, and since \(\sigma_A(x)\) lies in the disc of radius \(\|x\|\) ([Proposition 4.4(1)](#oa-fnd-bn-07)), \(\Gamma\) surrounds \(\sigma_A(x)\) in \(\mathbb C\). By (4.1), \(\lambda^mR_x(\lambda)=\sum_nx^n\lambda^{m-n-1}\) uniformly on \(\Gamma^*\), and \(\frac1{2\pi i}\oint\lambda^{m-n-1}\,d\lambda\) is \(1\) if \(n=m\) and \(0\) otherwise. So \(1(x)=x^0=1\) and \(u(x)=x\).

*Continuity.* With one fixed \(\Gamma\), \[
\begin{gathered}
\|f_n(x)-f(x)\|\\
\leq\frac{\ell(\Gamma)}{2\pi}\sup_{\Gamma^*}|f_n-f|\,\sup_{\Gamma^*}\|R_x\|.
\end{gathered}
\]

*Commutation.* \(f(x)g(x)=(fg)(x)=(gf)(x)=g(x)f(x)\). \(\square\)

**Proposition 6.8** (power series). Let \(f(\lambda)=\sum_nc_n(\lambda-c)^n\) converge for \(|\lambda-c|<\rho_0\), and let \(r(x-c)<\rho_0\). Then \(\sigma_A(x)\) lies in the disc \(|\lambda-c|<\rho_0\), and \(f(x)=\sum_nc_n(x-c)^n\), with the series converging in norm. In particular, the calculus of \(\lambda\mapsto e^\lambda\) is \(\exp x=\sum_nx^n/n!\) ([Section 7](#oa-fnd-bn-14)).

**Proof.** By parts (5) and (1) of [Proposition 4.2](#oa-fnd-bn-06), \(\sigma_A(x)=c+\sigma_A(x-c)\) lies in \(|\lambda-c|\leq r(x-c)\). Choose \(\rho\) with \(r(x-c)<\rho<\rho_0\), and let \(\Gamma\) be the positively oriented circle \(|\lambda-c|=\rho\). By Lemma 6.3 it surrounds \(\sigma_A(x)\) in the disc \(\{|\lambda-c|<\rho_0\}\). The series of \(f\) converges uniformly on \(\Gamma^*\). Integrating term by term, and using the theorem for the polynomials \((\lambda-c)^n\), gives \(f(x)=\sum_nc_n(x-c)^n\); the partial sums converge in norm. \(\square\)

**Example 6.9.** Let \(x=\alpha+N\) with \(N^2=0\) and \(N\neq0\), for instance a \(2\times2\) Jordan block. Then \(\sigma_A(x)=\{\alpha\}\) (the spectrum of \(N\) is not empty and \(r(N)=0\)), and by the proposition \(f(x)=f(\alpha)+f'(\alpha)N\) for every \(f\) holomorphic near \(\alpha\). So \(f(x)\) is not determined by the values of \(f\) on \(\sigma_A(x)\).

### Spectral mapping and composition

**Theorem 6.10** (invertibility, spectral mapping and composition). Let \(A\) be a unital Banach algebra, \(x\in A\), \(U\supseteq\sigma_A(x)\) open, and \(f\in H(U)\).
1. \(f(x)\) is invertible if and only if \(f\) has no zero on \(\sigma_A(x)\). Then \(f(x)^{-1}=(1/f)(x)\), where \(1/f\) is holomorphic on the open set \(\{\lambda\in U:f(\lambda)\neq0\}\supseteq\sigma_A(x)\).
2. (*Spectral mapping theorem.*) \(\sigma_A(f(x))=f(\sigma_A(x))\).
3. (*Composition.*) Let \(V\supseteq f(\sigma_A(x))\) be open and \(g\in H(V)\). Then \(g\circ f\) is holomorphic on \(U\cap f^{-1}(V)\), which contains \(\sigma_A(x)\), and \((g\circ f)(x)=g(f(x))\).

**Proof.** (1) If \(f\) has no zero on \(\sigma_A(x)\), then \(1/f\) is holomorphic on \(W=\{\lambda\in U:f(\lambda)\neq0\}\supseteq\sigma_A(x)\), and \(f\cdot(1/f)=1\) on \(W\). By Theorem 6.7 and Proposition 6.5(2), \(f(x)(1/f)(x)=(1/f)(x)f(x)=1\). Conversely, let \(f(\alpha)=0\) with \(\alpha\in\sigma_A(x)\). The Taylor expansion of \(f\) at \(\alpha\) (from Cauchy's theorem 6.1) has no constant term. So \(k(\lambda)=f(\lambda)/(\lambda-\alpha)\) for \(\lambda\neq\alpha\), with \(k(\alpha)=f'(\alpha)\), defines \(k\in H(U)\), and \(f(\lambda)=(\lambda-\alpha)k(\lambda)\). By Theorem 6.7, \(f(x)=(x-\alpha)k(x)=k(x)(x-\alpha)\). If \(f(x)\) had an inverse \(w\), then \(k(x)w\) would be a right inverse and \(wk(x)\) a left inverse of the noninvertible element \(x-\alpha\).
(2) For \(\beta\in\mathbb C\), \((f-\beta)(x)=f(x)-\beta\) by Theorem 6.7. By (1), \(\beta\in\sigma_A(f(x))\) if and only if \(f-\beta\) has a zero on \(\sigma_A(x)\), that is, \(\beta\in f(\sigma_A(x))\).
(3) The set \(U_0=U\cap f^{-1}(V)\) is open, contains \(\sigma_A(x)\), and \(g\circ f\in H(U_0)\). By (2), \(f(\sigma_A(x))=\sigma_A(f(x))\). Choose a cycle \(\Gamma_V\) that surrounds \(f(\sigma_A(x))\) in \(V\). The set \(O=O_{\Gamma_V}\), defined after Lemma 6.3, is open, lies in \(V\), and contains \(f(\sigma_A(x))\). So \(W=U\cap f^{-1}(O)\) is an open subset of \(U_0\) that contains \(\sigma_A(x)\). Choose a cycle \(\Gamma_W\) that surrounds \(\sigma_A(x)\) in \(W\). For \(\zeta\in\Gamma_V^*\) and \(\lambda\in W\) we have \(f(\lambda)\in O\), so \(f(\lambda)\neq\zeta\). Thus \(\lambda\mapsto(\zeta-f(\lambda))^{-1}\) is holomorphic on \(W\), and by (1), applied in \(W\),
\[
(\zeta-f(x))^{-1}=\frac1{2\pi i}\int_{\Gamma_W}(\zeta-f(\lambda))^{-1}R_x(\lambda)\,d\lambda .
\]
Since \(\Gamma_V\) surrounds \(\sigma_A(f(x))\) in \(V\), inserting this and exchanging the order of integration (the integrand is continuous on \(\Gamma_V^*\times\Gamma_W^*\)) gives
\[
\begin{gathered}
g(f(x))\\
=\frac1{2\pi i}\int_{\Gamma_V}g(\zeta)(\zeta-f(x))^{-1}\,d\zeta\\
=\frac1{2\pi i}\int_{\Gamma_W}\Big(\frac1{2\pi i}\int_{\Gamma_V}\frac{g(\zeta)}{\zeta-f(\lambda)}\,d\zeta\Big)R_x(\lambda)\,d\lambda .
\end{gathered}
\]
For \(\lambda\in\Gamma_W^*\), \(f(\lambda)\in O\subseteq V\setminus\Gamma_V^*\), so by Cauchy's theorem 6.1 the inner integral is \(g(f(\lambda))\operatorname{Ind}_{\Gamma_V}(f(\lambda))=g(f(\lambda))\). Hence \[
\begin{gathered}
g(f(x))\\
=\frac1{2\pi i}\int_{\Gamma_W}(g\circ f)(\lambda)R_x(\lambda)\,d\lambda\\
=(g\circ f)(x),
\end{gathered}
\] by Proposition 6.5(2). \(\square\)

**Remark 6.11** (cycles are needed). The proof of (1) uses the function \(1/f\), which is holomorphic only where \(f\) has no zero. There may be no single closed curve that encloses \(\sigma_A(x)\) and has its inside in that domain, although the conclusion is true. For example, in \(A=C(\mathbb T)\) with \(x(z)=z\), \(f(\lambda)=\lambda\) and \(h=1/f\), every closed path \(C\) disjoint from \(\mathbb T\) and having index \(1\) on \(\mathbb T\) also has index \(1\) at \(0\), where \(h(\lambda)=1/\lambda\) is not defined. Indeed, the connected image of \(C\) lies entirely inside or entirely outside the unit circle. In the first case \(\mathbb T\) lies in its unbounded complementary component, so its index would be zero. In the second case the closed unit disc is a connected set disjoint from \(C\), so the index is constant there and equals \(1\) at \(0\). The cycle made of the circles \(|\lambda|=2\) and \(|\lambda|=1/2\), the second one reversed, surrounds \(\mathbb T\) in \(\mathbb C\setminus\{0\}\), and (1) gives \(h(x)=x^{-1}\).

*Characters.* For commutative \(A\), (2) also follows from Proposition 6.5(5) and the description of the spectrum by characters in [Theorem 11.1](#oa-fnd-bn-18): \[
\begin{gathered}
\sigma_A(f(x))\\
=\{\chi(f(x))\}\\
=\{f(\chi(x))\}\\
=f(\sigma_A(x)),
\end{gathered}
\] with \(\chi\) running over the characters.

### Idempotents from a disconnected spectrum

**Example 6.12.** Let \(A\) be a unital Banach algebra, and let \(x\in A\) have spectrum \(\sigma_A(x)=K_0\cup K_1\), where \(K_0\) and \(K_1\) are disjoint, compact and nonempty. Choose disjoint open sets \(U_0\supseteq K_0\) and \(U_1\supseteq K_1\), and let \(f\) be \(0\) on \(U_0\) and \(1\) on \(U_1\). Then \(f\in H(U_0\cup U_1)\) and \(f^2=f\). The element \(e=f(x)\) satisfies \(e^2=e\) (Theorem 6.7), \(ex=xe\) (Proposition 6.5(4)), and \(\sigma_A(e)=f(\sigma_A(x))=\{0,1\}\) (Theorem 6.10); so \(e\neq0\) and \(e\neq1\). No single closed curve whose closed inside lies in \(U_0\cup U_1\) encloses \(\sigma_A(x)\): the closed region bounded by it is connected, so it lies in \(U_0\) or in \(U_1\). So \(e\) is out of reach of a calculus built on one closed curve. For the matrix \(x=\begin{pmatrix}1&1\\0&2\end{pmatrix}\), with \(K_0=\{1\}\) and \(K_1=\{2\}\), Exercise 3 at the end of the lesson gives \(e=x-1=\begin{pmatrix}0&1\\0&1\end{pmatrix}\), which is indeed idempotent.

## 7. Exponential, logarithm and the invertible group

Let \(A\) be a nontrivial unital Banach algebra. Let \(D=\mathbb C\setminus(-\infty,0]\), and let \(\operatorname{Log}\lambda=\ln|\lambda|+i\arg\lambda\) with \(\arg\lambda\in(-\pi,\pi)\) be the principal logarithm on \(D\).

*Facts about \(\operatorname{Log}\).* It is continuous on \(D\), \(e^{\operatorname{Log}\lambda}=\lambda\), and \(\operatorname{Log}(e^w)=w\) when \(|\operatorname{Im}w|<\pi\). It is holomorphic with derivative \(1/\lambda\): if \(\lambda\to\lambda_0\) in \(D\), then \(w=\operatorname{Log}\lambda\to w_0=\operatorname{Log}\lambda_0\), and \[
\begin{gathered}
(\operatorname{Log}\lambda-\operatorname{Log}\lambda_0)/(\lambda-\lambda_0)\\
=(w-w_0)/(e^w-e^{w_0})\to e^{-w_0}\\
=1/\lambda_0.
\end{gathered}
\] On the disc \(|\lambda-1|<1\), which lies in \(D\), the series \(-\sum_{n\geq1}(1-\lambda)^n/n\) has the same derivative \(\sum_{n\geq1}(1-\lambda)^{n-1}=1/\lambda\) and the same value \(0\) at \(\lambda=1\). So it equals \(\operatorname{Log}\) there.

**Proposition 7.1.**
1. \(\exp x=\sum_{n\geq0}x^n/n!\) converges absolutely, and it is the calculus of \(\lambda\mapsto e^\lambda\). If \(xy=yx\), then \(\exp(x+y)=\exp x\exp y\). Hence \(\exp(-x)=(\exp x)^{-1}\), \(\exp(A)\subseteq G(A)\), and \(t\mapsto\exp(tx)\) is a norm-continuous homomorphism from \((\mathbb R,+)\) into \(G(A)\).
2. Let \(G_0(A)\) be the connected component of \(1\) in \(G(A)\), the *principal component*. It is an open and closed normal subgroup of \(G(A)\), and it consists of the elements that can be joined to \(1\) by a continuous path in \(G(A)\). It contains \(\exp(A)\). The quotient \(G(A)/G_0(A)\) is the *index group*.
3. If \(\sigma_A(x)\subseteq D\), put \(\log x=\operatorname{Log}(x)\), the calculus of \(\operatorname{Log}\). Then \(\exp(\log x)=x\). If \(r(x-1)<1\), then \(\log x=-\sum_{n\geq1}(1-x)^n/n\).
4. If \(\sigma_A(x)\) lies in the strip \(S=\{|\operatorname{Im}\lambda|<\pi\}\), then \(\sigma_A(\exp x)\subseteq D\) and \(\log(\exp x)=x\).
5. \(G_0(A)\) is the subgroup generated by \(\exp(A)\). If \(A\) is commutative, \(G_0(A)=\exp(A)\).

**Proof.** (1) \(\|x^n/n!\|\leq\|x\|^n/n!\) for \(n\geq1\). [Proposition 6.8](#oa-fnd-bn-11), with \(c=0\) and \(\rho_0=\infty\), identifies \(\exp x\) with the calculus of \(e^\lambda\). For commuting \(x\) and \(y\), the Cauchy product of the two absolutely convergent series is allowed, and the binomial theorem turns it into \(\sum_n(x+y)^n/n!\). Also \(\exp0=1\). For continuity, \[
\begin{gathered}
\|\exp(tx)-\exp(t_0x)\|\\
\leq\|\exp(t_0x)\|\,\|\exp((t-t_0)x)-1\|\\
\leq\|\exp(t_0x)\|\big(e^{|t-t_0|\|x\|}-1\big).
\end{gathered}
\]
(2) \(G(A)\) is open ([Proposition 2.2](#oa-fnd-bn-02)), so each of its points has a ball around it inside \(G(A)\), and balls are convex. Hence the path components of \(G(A)\) are open. Each is also closed in \(G(A)\), since its complement is a union of path components. So the path component of \(1\) is connected, open and closed in \(G(A)\); it is therefore the connected component \(G_0(A)\). If \(\alpha\) and \(\beta\) are paths in \(G(A)\) from \(1\) to \(a\) and to \(b\), then \(t\mapsto\alpha(t)\beta(t)\) and \(t\mapsto\alpha(t)^{-1}\) are paths from \(1\) to \(ab\) and to \(a^{-1}\); the second is continuous because inversion is continuous (Proposition 2.2). For \(c\in G(A)\), \(t\mapsto c\alpha(t)c^{-1}\) is a path from \(1\) to \(cac^{-1}\). So \(G_0(A)\) is a normal subgroup. The path \(t\mapsto\exp(tx)\), \(0\leq t\leq1\), joins \(1\) to \(\exp x\).
(3) By the composition rule, [Theorem 6.10(3)](#oa-fnd-bn-12), with \(f=\operatorname{Log}\) and \(g=\exp\), \(\exp(\log x)=(\exp\circ\operatorname{Log})(x)=x\), because \(\exp\circ\operatorname{Log}\) is the identity function on \(D\). If \(r(x-1)<1\), Proposition 6.8 with \(c=1\) and \(\rho_0=1\) gives the series.
(4) By the spectral mapping theorem, Theorem 6.10(2), \(\sigma_A(\exp x)=\exp(\sigma_A(x))\). For \(\lambda=a+ib\) with \(|b|<\pi\), \(e^\lambda=e^ae^{ib}\) is not in \((-\infty,0]\). So \(\sigma_A(\exp x)\subseteq D\). By Theorem 6.10(3) with \(f=\exp\) and \(g=\operatorname{Log}\), \(\log(\exp x)=(\operatorname{Log}\circ\exp)(x)\). On the open set \(S\supseteq\sigma_A(x)\), \(\operatorname{Log}\circ\exp\) is the identity function, so \((\operatorname{Log}\circ\exp)(x)=x\) by [Proposition 6.5(2)](#oa-fnd-bn-10) and Theorem 6.7.
(5) Let \(\Gamma_e\) be the subgroup generated by \(\exp(A)\). By (1) and (2), \(\Gamma_e\subseteq G_0(A)\). If \(\|y-1\|<1\), then \(r(y-1)<1\), so \(\sigma_A(y)\) lies in the disc \(|\lambda-1|<1\), inside \(D\), and \(y=\exp(\log y)\in\exp(A)\) by (3). If \(g\in\Gamma_e\) and \(\|z-g\|<1/\|g^{-1}\|\), then \(\|g^{-1}z-1\|<1\), so \(z=g(g^{-1}z)\in\Gamma_e\). So \(\Gamma_e\) is open. Its complement in \(G_0(A)\) is a union of cosets \(g\Gamma_e\), each open, so \(\Gamma_e\) is also closed in \(G_0(A)\). Since \(G_0(A)\) is connected, \(\Gamma_e=G_0(A)\). If \(A\) is commutative, \(\exp(A)\) is already a subgroup by (1), so \(G_0(A)=\exp(A)\). \(\square\)

Part (5) shows what the logarithm of (3) is good for.

**Example 7.2** (a nontrivial index group). Let \(A=C(\mathbb T)\), the continuous functions on the unit circle, and let \(z\) be the identity function. It is invertible, with inverse \(\bar z\). By (5), \(G_0(A)=\exp(A)\), and \(\exp g=e^{g}\) pointwise. Suppose \(z=e^{g}\) with \(g\in C(\mathbb T)\), and put \(h(t)=g(e^{it})-it\) for \(t\in[0,2\pi]\). Then \(e^{h(t)}=1\), so \(h\) takes values in \(2\pi i\mathbb Z\); being continuous, it is constant. But \(h(2\pi)=g(1)-2\pi i\neq g(1)=h(0)\). So \(z\notin G_0(A)\), and the index group of \(C(\mathbb T)\) is not trivial.

## 8. Perturbation of the spectrum

**Theorem 8.1** (upper semicontinuity of the spectrum). Let \(A\) be a unital Banach algebra and \(U\subseteq\mathbb C\) open. The set \(E_U=\{x\in A:\sigma_A(x)\subseteq U\}\) is open. More precisely, if \(\sigma_A(x_0)\subseteq U\), then \(M=\sup_{\lambda\notin U}\|R_{x_0}(\lambda)\|\) is finite, and \(\sigma_A(x)\subseteq U\) whenever \(M\|x-x_0\|<1\).

**Proof.** If \(A=\{0\}\), every spectrum is empty and \(E_U=A\); all resolvents have norm zero, so take \(M=0\). If \(U=\mathbb C\), take \(M=0\) (the supremum of an empty family of nonnegative numbers); there is nothing to prove. Otherwise \(F=\mathbb C\setminus U\) is closed and contained in \(\rho_A(x_0)\). The continuous function \(\lambda\mapsto\|R_{x_0}(\lambda)\|\) is bounded on the compact set \(F\cap\{|\lambda|\leq\|x_0\|+1\}\), and by the bound of [Proposition 4.4(1)](#oa-fnd-bn-07) it is at most \(c_1\) when \(|\lambda|\geq\|x_0\|+1\). So \(M<\infty\). If \(M\|x-x_0\|<1\) and \(\lambda\in F\), then \[
\begin{gathered}
\|(\lambda-x)-(\lambda-x_0)\|\\
=\|x-x_0\|<1/\|R_{x_0}(\lambda)\|,
\end{gathered}
\] so \(\lambda-x\) is invertible by [Proposition 2.2](#oa-fnd-bn-02). \(\square\)

**Theorem 8.2** (continuity of the calculus). Let \(f\in H(U)\). The map \(x\mapsto f(x)\) is continuous on the open set \(E_U\), and it is locally Lipschitz: each \(x_0\in E_U\) has \(\delta>0\) and \(L\) with \(\|f(x)-f(x_0)\|\leq L\|x-x_0\|\) for \(\|x-x_0\|<\delta\). In particular, for a compact \(K\subseteq U\), the map is continuous on \(A_K=\{x:\sigma_A(x)\subseteq K\}\), which is contained in \(E_U\).

The set \(A_K\) need not be open: in a nontrivial algebra, for \(K=\{0\}\), it contains \(0\) but no \(\varepsilon1\) with \(\varepsilon\neq0\). So continuity on the open set \(E_U\) is the stronger statement.

**Proof.** If \(A=\{0\}\), the calculus is identically zero and the estimate holds with \(\delta=L=1\). Otherwise choose a cycle \(\Gamma\) that surrounds \(\sigma_A(x_0)\) in \(U\). The open set \(O_\Gamma\), defined after Lemma 6.3, contains \(\sigma_A(x_0)\) and lies in \(U\). By Theorem 8.1 there is \(\delta_1>0\) with \(\sigma_A(x)\subseteq O_\Gamma\) for \(\|x-x_0\|<\delta_1\). For such \(x\), \(\Gamma\) surrounds \(\sigma_A(x)\) in \(U\), so \(f(x)\) and \(f(x_0)\) are integrals over the same \(\Gamma\). Let \(M_\Gamma=\max_{\Gamma^*}\|R_{x_0}\|\), and suppose also \(\|x-x_0\|\leq1/(2M_\Gamma)\). Then (2.3), applied to \(\lambda-x_0\) and \(\lambda-x\), gives \(\|R_x(\lambda)\|\leq2M_\Gamma\) on \(\Gamma^*\). The second resolvent identity
\[
\begin{gathered}
R_x(\lambda)-R_{x_0}(\lambda)\\
=R_x(\lambda)\,(x-x_0)\,R_{x_0}(\lambda)
\end{gathered}
\tag{8.1}
\]
then gives \(\|R_x(\lambda)-R_{x_0}(\lambda)\|\leq2M_\Gamma^2\|x-x_0\|\) on \(\Gamma^*\). Hence \(\|f(x)-f(x_0)\|\leq\frac{\ell(\Gamma)}{\pi}\big(\sup_{\Gamma^*}|f|\big)M_\Gamma^2\,\|x-x_0\|\). \(\square\)

**Example 8.3** (the spectrum is not continuous). On \(\ell^2(\mathbb Z)\) with orthonormal basis \((e_n)\), a bounded sequence \(w=(w_n)\) defines the weighted shift \(W_we_n=w_ne_{n+1}\). It maps the basis to orthogonal vectors, so \(\|W_w\|=\sup_n|w_n|\). Also \(W_w^ke_n=w_nw_{n+1}\cdots w_{n+k-1}e_{n+k}\), so \(\|W_w^k\|\) is the supremum of the products of \(k\) consecutive weights. For \(t\in\mathbb C\) let \(W_t\) have weights \(w_0=t\) and \(w_n=1\) for \(n\neq0\). Then \(\|W_t-W_0\|=|t|\).
- *\(\sigma(W_0)\) is the closed unit disc.* \(\|W_0\|=1\). For \(|\lambda|<1\), the vector \(v=\sum_{n\leq0}\lambda^{-n}e_n\) lies in \(\ell^2(\mathbb Z)\), and \(W_0v=\sum_{n\leq-1}\lambda^{-n}e_{n+1}=\lambda v\). So every \(\lambda\) with \(|\lambda|<1\) is an eigenvalue, and the closed spectrum contains the closed disc.
- *For \(t\neq0\), \(\sigma(W_t)\) lies in the unit circle.* Every product of \(k\) consecutive weights contains the weight \(t\) at most once, so \(\|W_t^k\|\leq\max(1,|t|)\) and \(r(W_t)\leq1\) by the spectral radius formula (5.1). \(W_t\) is invertible, with \(W_t^{-1}e_{n+1}=w_n^{-1}e_n\), and the same count gives \(\|W_t^{-k}\|\leq\max(1,1/|t|)\), so \(r(W_t^{-1})\leq1\). By [Proposition 4.2(4)](#oa-fnd-bn-06), \(\sigma(W_t)\) lies in \(\{|\lambda|\geq1\}\), hence in the circle.

So \(W_t\to W_0\) in norm while every \(\sigma(W_t)\), \(t\neq0\), stays in the circle and \(\sigma(W_0)\) is the whole disc. A small perturbation can make the spectrum much smaller; by Theorem 8.1, it can never make it much larger. Theorem 8.1 cannot be improved to continuity.

## 9. Modular ideals, maximal ideals and quotient algebras

**Definition 9.1.** Let \(A\) be an algebra.
1. A left ideal \(L\) is *modular* if some \(u\in A\) satisfies \(x-xu\in L\) for all \(x\in A\); such a \(u\) is a *right unit modulo \(L\)*. A two-sided ideal \(I\) is *modular* if \(A/I\) is unital, that is, if some \(u\) satisfies \(x-xu\in I\) and \(x-ux\in I\) for all \(x\). In a commutative algebra the two notions agree for ideals. Modular ideals are also called *regular*, and \(u\) is then called an *identity modulo* the ideal. Every left ideal of a unital algebra is modular, with \(u=1\).
2. A proper left ideal is *maximal* if no proper left ideal strictly contains it. Maximal two-sided ideals are defined in the same way among two-sided ideals.

**Lemma 9.2** (no norm is needed). Let \(L\) be a left ideal of an algebra \(A\), with a right unit \(u\) modulo \(L\).
1. Every left ideal that contains \(L\) is modular, with the same \(u\).
2. \(L=A\) if and only if \(u\in L\).
3. If \(L\) is proper, it lies in a maximal left ideal, and that ideal is modular.

The same holds for two-sided modular ideals, with maximality among two-sided ideals.

**Proof.** (1) is clear. (2) If \(u\in L\), then \(x=(x-xu)+xu\in L\) for every \(x\), because \(xu\in L\). (3) Let \(\mathcal F\) be the set of left ideals \(J\supseteq L\) with \(u\notin J\). By (2), \(L\in\mathcal F\). The union of a chain in \(\mathcal F\) is a left ideal that contains \(L\) and not \(u\). So Zorn's lemma gives a maximal element \(M\) of \(\mathcal F\), and \(M\) is proper. If \(J\) is a left ideal with \(M\subsetneq J\), then \(J\notin\mathcal F\), so \(u\in J\), and \(J=A\) by (1) and (2). So \(M\) is a maximal left ideal, and it is modular by (1). For two-sided ideals, run the same argument with two-sided ideals and a two-sided unit modulo \(I\). \(\square\)

**Proposition 9.3** (modular ideals stay away from the unit). Let \(A\) be a Banach algebra, not necessarily commutative, and \(L\) a proper modular left ideal with right unit \(u\). Then \(\|u-\ell\|\geq1\) for every \(\ell\in L\). Consequently the closure of \(L\) is again a proper modular left ideal, and every maximal modular left ideal is closed. The same holds for two-sided ideals.

**Proof.** Suppose \(\|u-\ell\|<1\) for some \(\ell\in L\). Then \(y=\sum_{n\geq1}(u-\ell)^n\) converges, and \(y(u-\ell)=y-(u-\ell)\). Rearranged, this says \(u=y-yu+y\ell+\ell\). Here \(y-yu\in L\) because \(u\) is a right unit modulo \(L\), \(y\ell\in L\) because \(L\) is a left ideal, and \(\ell\in L\). So \(u\in L\), and \(L=A\) by Lemma 9.2, a contradiction. The closure \(\bar L\) is a left ideal because multiplication is continuous. The element \(u\) is a right unit modulo \(\bar L\), and \(\operatorname{dist}(u,\bar L)=\operatorname{dist}(u,L)\geq1\); so \(u\notin\bar L\), and \(\bar L\neq A\). If \(L\) is maximal, then \(L=\bar L\). A two-sided unit modulo an ideal is in particular a right unit, so the two-sided case follows. \(\square\)

**Proposition 9.4** (quotient algebras). Let \(I\) be a closed ideal of a Banach algebra \(A\). With the quotient norm \(\|x+I\|=\inf\{\|x+k\|:k\in I\}\), the algebra \(A/I\) is a Banach algebra. If \(I\) is proper and modular, with unit \(u\) modulo \(I\), then \(u+I\) is the identity of \(A/I\), and \(\|u+I\|\geq1\).

**Proof.** First this formula defines a norm. If \(\|x+I\|=0\), there are \(k_n\in I\) with \(x+k_n\to0\), so \(-x\in I\) by closedness; the converse is immediate. For a nonzero scalar \(\lambda\), representatives of \(\lambda x+I\) are exactly \(\lambda(x+k)\), \(k\in I\), which proves homogeneity. The triangle inequality follows from \(\|(x+k)+(y+m)\|\leq\|x+k\|+\|y+m\|\) by taking the two infima independently. Also the quotient map is contractive, since the infimum is at most \(\|x\|\). The quotient of a Banach space by a closed subspace is complete: if \(\sum_n\|x_n+I\|<\infty\), choose representatives with \(\|x_n\|\leq\|x_n+I\|+2^{-n}\); then \(\sum_nx_n\) converges in \(A\), and its class is the sum of the series in \(A/I\); and this property implies completeness. Indeed, from a Cauchy sequence \(y_n\) in any such normed space choose a subsequence \(y_{n_k}\) with \(\|y_{n_{k+1}}-y_{n_k}\|\leq2^{-k}\). The series of these differences converges, so the subsequence converges by telescoping; the original Cauchy sequence has the same limit. For \(x,y\in A\) and \(k,m\in I\), \((x+k)(y+m)\in xy+I\), so \(\|xy+I\|\leq\|x+k\|\|y+m\|\); take the infimum over \(k\) and \(m\). The last claim is Proposition 9.3. \(\square\)

**Example 9.5** (completeness is needed). In the normed algebra \(\mathbb C[z]\) of [Examples 4.5](#oa-fnd-bn-07) (norm \(\max_{|z|\leq1}|p(z)|\)), the ideal \(I=(z-2)\mathbb C[z]\) is maximal, since \(\mathbb C[z]/I\cong\mathbb C\) through \(p\mapsto p(2)\), and it is modular because \(\mathbb C[z]\) is unital. But it is dense. With \(p_N=-\frac12\sum_{n=0}^N(z/2)^n\) we get \((z-2)p_N-1=-(z/2)^{N+1}\), of norm \(2^{-N-1}\). So the distance from \(1\) to \(I\) is \(0\), and this maximal ideal is not closed. The character \(p\mapsto p(2)\) is unbounded, since the polynomials \(z^n\) have norm \(1\) and value \(2^n\). Compare [Proposition 10.3(1)](#oa-fnd-bn-17).

## 10. Characters

### Maximal ideals and characters of commutative algebras

**Definition 10.1.** A *character* of an algebra \(A\) is a nonzero algebra homomorphism \(A\to\mathbb C\), and \(\operatorname{Ch}(A)\) is the set of characters. A nonzero homomorphism into \(\mathbb C\) is automatically onto, because its image is a nonzero subspace of \(\mathbb C\).

**Proposition 10.2.**
1. In a unital commutative algebra, every noninvertible element lies in a maximal ideal. No norm is needed.
2. Let \(A\) be a commutative Banach algebra and \(\mathfrak m\) a maximal modular ideal, with unit \(u\) modulo \(\mathfrak m\). Then \(\mathfrak m\) is closed, and \(A/\mathfrak m\) is a field. The map \(\lambda\mapsto\lambda(u+\mathfrak m)\) is the only unital algebra isomorphism of \(\mathbb C\) onto \(A/\mathfrak m\). Let \(\omega_{\mathfrak m}(x)\) be the number \(\lambda\) with \(x+\mathfrak m=\lambda(u+\mathfrak m)\). Then \(\omega_{\mathfrak m}\) is a character with kernel \(\mathfrak m\).
3. For a commutative Banach algebra \(A\), \(\mathfrak m\mapsto\omega_{\mathfrak m}\) is a bijection from the set \(\mathcal M(A)\) of maximal modular ideals onto \(\operatorname{Ch}(A)\). Its inverse is \(\omega\mapsto\ker\omega\).
4. In any algebra, two characters with the same kernel are equal, and the kernel of a character is a maximal modular ideal of codimension one.

**Proof.** (1) If \(x\) is not invertible, then \(Ax\) is an ideal (as \(A\) is commutative) that does not contain \(1\); indeed \(1=ax\) would make \(x\) invertible. By [Lemma 9.2](#oa-fnd-bn-15), with \(u=1\), it lies in a maximal ideal, which contains \(x=1x\).
(2) \(\mathfrak m\) is closed by Proposition 9.3. So \(A/\mathfrak m\) is a commutative Banach algebra (Proposition 9.4) with identity \(u+\mathfrak m\neq0\). Its ideals correspond to the ideals of \(A\) that contain \(\mathfrak m\), so its only ideals are \(\{0\}\) and itself. By (1), every nonzero element of \(A/\mathfrak m\) is invertible; otherwise it would lie in a maximal ideal of \(A/\mathfrak m\), which can only be \(\{0\}\). So \(A/\mathfrak m\) is a field, and by the Gelfand–Mazur theorem ([Corollary 5.3](#oa-fnd-bn-08)) every element is a multiple of \(u+\mathfrak m\). A unital algebra homomorphism \(\psi:\mathbb C\to A/\mathfrak m\) satisfies \(\psi(\lambda)=\lambda\psi(1)\), so it equals \(\lambda\mapsto\lambda(u+\mathfrak m)\). Hence \(\omega_{\mathfrak m}\) is the quotient map followed by the inverse of this isomorphism. It is a homomorphism, it is nonzero because \(\omega_{\mathfrak m}(u)=1\), and its kernel is \(\mathfrak m\).
(4) Let \(\omega\) be a character, and choose \(u\) with \(\omega(u)=1\). Then \(x-xu\) and \(x-ux\) lie in \(\ker\omega\) for every \(x\), so \(\ker\omega\) is a modular ideal. It has codimension one, so it is maximal. Let \(\omega'\) be a character with the same kernel. From \(x-\omega(x)u\in\ker\omega'\) we get \(\omega'(x)=\omega(x)\omega'(u)\), and from \(u-u^2\in\ker\omega'\) we get \(\omega'(u)=\omega'(u)^2\). Since \(\omega'\neq0\), \(\omega'(u)\neq0\); so \(\omega'(u)=1\) and \(\omega'=\omega\).
(3) By (2), \(\ker\omega_{\mathfrak m}=\mathfrak m\). By (4), for \(\omega\in\operatorname{Ch}(A)\), \(\ker\omega\in\mathcal M(A)\), and \(\omega_{\ker\omega}=\omega\) because both have the same kernel. \(\square\)

*Automatic continuity.* For a commutative Banach algebra, the continuity of characters can be read off from (2): the kernel of a character is a maximal modular ideal, hence closed, and a linear functional with closed kernel is continuous. Proposition 10.3(1) below gives a direct proof with the bound \(\|\omega\|\leq1\), for noncommutative algebras as well. Example 9.5 shows that completeness cannot be dropped.

### Characters are contractive; the character space

**Proposition 10.3.** Let \(A\) be a Banach algebra, not necessarily commutative.
1. For every character \(\omega\) and every \(x\in A\), \(\omega(x)\in\sigma'_A(x)\), and \(|\omega(x)|\leq r(x)\leq\|x\|\). So every character is continuous, with \(\|\omega\|\leq1\). If \(A\) is unital, \(\omega(1)=1\).
2. With the weak\* topology, \(\operatorname{Ch}(A)\cup\{0\}\) is compact, and \(\operatorname{Ch}(A)\) is locally compact Hausdorff. If \(A\) is unital, \(\operatorname{Ch}(A)\) is compact.
3. For \(x\in A\), the function \(\hat x(\omega)=\omega(x)\) lies in \(C_0(\operatorname{Ch}(A))\).
4. The characters of \(A_1\) are \(q\) and the maps \(\omega_1(a+\lambda)=\omega(a)+\lambda\) with \(\omega\in\operatorname{Ch}(A)\). The map \(\omega\mapsto\omega_1\) is a homeomorphism of \(\operatorname{Ch}(A)\) onto \(\operatorname{Ch}(A_1)\setminus\{q\}\), which is open in the compact space \(\operatorname{Ch}(A_1)\).

**Proof.** (1) The map \(\omega_1\) of (4) is a unital homomorphism \(A_1\to\mathbb C\) (a direct check with (3.1)), and \(\omega_1(\omega(x)-j(x))=0\). If \(\omega(x)-j(x)\) had an inverse \(w\) in \(A_1\), applying \(\omega_1\) would give \(1=0\). So \(\omega(x)\in\sigma'_A(x)\), and \(|\omega(x)|\leq r(x)\leq\|x\|\) because the quasi-spectrum lies in the disc of radius \(\|x\|\) ([Proposition 4.4(3)](#oa-fnd-bn-07)). If \(A\) is unital, then \(\omega(1)^2=\omega(1)\), and \(\omega(1)=0\) would give \(\omega(x)=\omega(x)\omega(1)=0\) for all \(x\).
(2) By (1), \(\operatorname{Ch}(A)\cup\{0\}\) lies in the closed unit ball of \(A^*\), which is weak\* compact by the Banach–Alaoglu theorem. It is weak\* closed: if a net of characters, or zeros, converges pointwise to \(\omega_0\), then \(\omega_0\) is linear, and \(\omega_0(xy)=\lim\omega_i(x)\omega_i(y)=\omega_0(x)\omega_0(y)\). So \(\operatorname{Ch}(A)\cup\{0\}\) is compact and Hausdorff. The point \(0\) is closed, so \(\operatorname{Ch}(A)\) is open in it, hence locally compact Hausdorff. If \(A\) is unital, \(\operatorname{Ch}(A)=\{\omega\in\operatorname{Ch}(A)\cup\{0\}:\omega(1)=1\}\) is closed, hence compact.
(3) \(\hat x\) is weak\* continuous by definition. For \(\varepsilon>0\), the set \(\{\omega:|\omega(x)|\geq\varepsilon\}\) equals \(\{\varphi\in\operatorname{Ch}(A)\cup\{0\}:|\varphi(x)|\geq\varepsilon\}\), since it misses \(0\). It is closed in a compact space, hence compact.
(4) Let \(\chi\) be a character of \(A_1\); then \(\chi(1)=1\) by (1). Its restriction to \(j(A)\) is a homomorphism. If the restriction is \(0\), then \(\chi=q\). Otherwise it is a character \(\omega\) of \(A\), and \(\chi=\omega_1\). Each \(\omega_1\) is a character. The map \(\omega\mapsto\omega_1\) is a bijection onto \(\operatorname{Ch}(A_1)\setminus\{q\}\), continuous in both directions, because \(\omega_1(a+\lambda)=\omega(a)+\lambda\) and \(\omega=\omega_1\circ j\). The space \(\operatorname{Ch}(A_1)\) is compact by (2), and \(\operatorname{Ch}(A_1)\setminus\{q\}\) is open in it. \(\square\)

In (4), when \(\operatorname{Ch}(A)\) is not compact, \(\operatorname{Ch}(A_1)\) is its one-point compactification, with \(q\) as the point at infinity. Below we use only the description of the points.

**Examples 10.4.**
- For \(n\geq2\), \(M_n(\mathbb C)\) has no characters. A character vanishes on \(E_{ij}\) for \(i\neq j\), since \(E_{ij}^2=0\). Then \(\omega(E_{ii})=\omega(E_{ij}E_{ji})=0\) for every \(i\), and \(\omega(1)=\sum_i\omega(E_{ii})=0\), which contradicts (1).
- A nonzero Banach space with the zero product is a commutative Banach algebra without characters, since \(\omega(x)^2=\omega(x^2)=0\).
- For normed algebras that are not complete, (1) fails: see Example 9.5.

## 11. The Gelfand representation

**Theorem 11.1** (Gelfand representation). Let \(A\) be a commutative Banach algebra, and define \(\mathcal G:A\to C_0(\operatorname{Ch}(A))\) by \(\mathcal G(x)=\hat x\).
1. \(\mathcal G\) is an algebra homomorphism, and \(\|\hat x\|_\infty=r(x)\leq\|x\|\).
2. If \(A\) is unital, then \(\operatorname{Ch}(A)\) is compact and \(\sigma_A(x)=\hat x(\operatorname{Ch}(A))\).
3. In general, \(\sigma'_A(x)=\hat x(\operatorname{Ch}(A))\cup\{0\}\).


**Proof.** (2) Compactness is Proposition 10.3(2). If \(\lambda\in\sigma_A(x)\), then \(\lambda-x\) lies in a maximal ideal \(\mathfrak m\) by Proposition 10.2(1), which is modular because \(A\) is unital, and \(\omega_{\mathfrak m}(\lambda-x)=0\); that is, \(\lambda=\hat x(\omega_{\mathfrak m})\). Conversely, let \(\omega\in\operatorname{Ch}(A)\). Then \(\omega(1)=1\) (Proposition 10.3(1)) and \(\omega(x-\omega(x))=0\). If \(x-\omega(x)\) had an inverse \(w\), then \(1=\omega\big((x-\omega(x))w\big)=0\). So \(\hat x(\omega)=\omega(x)\in\sigma_A(x)\).
(3) \(A_1\) is a unital commutative Banach algebra, so by (2) \(\sigma'_A(x)=\sigma_{A_1}(j(x))=\{\chi(j(x)):\chi\in\operatorname{Ch}(A_1)\}\). By Proposition 10.3(4) this set is \[
\begin{gathered}
\{\omega(x):\omega\in\operatorname{Ch}(A)\}\cup\{q(j(x))\}\\
=\hat x(\operatorname{Ch}(A))\cup\{0\}.
\end{gathered}
\]
(1) The operations on \(C_0(\operatorname{Ch}(A))\) are pointwise, and \(\widehat{xy}(\omega)=\omega(xy)=\hat x(\omega)\hat y(\omega)\). By (3), \(r(x)=\max\big(\sup|\hat x|,0\big)=\|\hat x\|_\infty\); this includes the case \(\operatorname{Ch}(A)=\varnothing\), where \(C_0(\varnothing)=\{0\}\). \(\square\)

For the zero algebra, which is unital, \(\operatorname{Ch}(A)=\varnothing=\sigma_A(0)\), in agreement with (2).

### The radical and semisimple algebras

**Definition 11.2.** Let \(A\) be a commutative Banach algebra. The map \(\mathcal G\) of Theorem 11.1 is the *Gelfand representation*; \(\operatorname{Ch}(A)\) is the *spectrum* (or character space) of \(A\), and its members are the *characters*. The kernel of \(\mathcal G\) is the *radical* \(\operatorname{rad}(A)\). The algebra is *semisimple* if \(\operatorname{rad}(A)=\{0\}\).

**Proposition 11.3.** Let \(A\) be a commutative Banach algebra.
1. \(\operatorname{rad}(A)=\{x:r(x)=0\}=\bigcap_{\mathfrak m\in\mathcal M(A)}\mathfrak m\), which is \(A\) when \(\mathcal M(A)\) is empty. It is a closed ideal.
2. If \(A\) is semisimple, then \(\mathcal G\) is an injective homomorphism of \(A\) onto a subalgebra of \(C_0(\operatorname{Ch}(A))\), with \(\|\hat x\|_\infty\leq\|x\|\). This subalgebra separates the points of \(\operatorname{Ch}(A)\) and vanishes at no point.

**Proof.** (1) \(\|\hat x\|_\infty=r(x)\) by Theorem 11.1. Also \(\hat x=0\) means \(\omega(x)=0\) for every character, that is, \(x\in\ker\omega_{\mathfrak m}=\mathfrak m\) for every \(\mathfrak m\in\mathcal M(A)\) ([Proposition 10.2(3)](#oa-fnd-bn-16)). The radical is the kernel of the continuous homomorphism \(\mathcal G\), so it is a closed ideal.
(2) Injectivity is the definition. Distinct characters differ at some \(x\), and a character \(\omega\neq0\) has some \(\hat x(\omega)\neq0\). \(\square\)

So every commutative semisimple Banach algebra is isomorphic, as an algebra, to an algebra of continuous functions that vanish at infinity on a locally compact Hausdorff space. The isomorphism is contractive, but in general it is not isometric ([Proposition 13.2(5)](#oa-fnd-bn-21)).

**Example 11.4** (the characters of \(C_0(\Omega)\)). Let \(\Omega\) be LCH. Every character \(\omega\) of \(C_0(\Omega)\) is an evaluation \(f\mapsto f(p)\), and \(p\mapsto\text{(evaluation at }p)\) is a homeomorphism of \(\Omega\) onto \(\operatorname{Ch}(C_0(\Omega))\). So \(\hat f\) is \(f\) itself, and \(\mathcal G\) is isometric.

*Proof.* First we find a point \(p\) at which every \(f\in\ker\omega\) vanishes. Suppose, to the contrary, that for every \(p\in\Omega\) some \(f_p\in\ker\omega\) has \(f_p(p)\neq0\). Choose \(g\) with \(\omega(g)=1\). The set \(C=\{|g|\geq1/2\}\) is compact, and it is not empty, since \(\|g\|_\infty\geq|\omega(g)|=1\) by [Proposition 10.3(1)](#oa-fnd-bn-17). So finitely many sets \(\{f_{p_i}\neq0\}\) cover it, and \(h=\sum_i\bar f_{p_i}f_{p_i}\) lies in the ideal \(\ker\omega\) and is positive on \(C\). Let \(m=\min_Ch>0\) and \(s=1/\max(h,m)\), a bounded continuous function. Then \(gs\in C_0(\Omega)\), so \(ghs=(gs)h\in\ker\omega\). On \(C\), \(hs=1\), so \(g-ghs=0\); off \(C\), \(0\leq hs\leq1\) gives \(|g-ghs|\leq|g|<1/2\). So \(\|g-ghs\|_\infty\leq1/2\), while \(\omega(g-ghs)=1\). This contradicts the bound \(|\omega(x)|\leq\|x\|\) of Proposition 10.3(1). Hence some \(p\) has \(f(p)=0\) for all \(f\in\ker\omega\).

Next, \(\omega\) is evaluation at this \(p\). Evaluation at \(p\) is nonzero (Urysohn), and its kernel contains \(\ker\omega\); both kernels have codimension one, so they are equal, and [Proposition 10.2(4)](#oa-fnd-bn-16) gives \(\omega=\) evaluation at \(p\).

Finally, the map is a homeomorphism. Distinct points give distinct evaluations (Urysohn). The map is weak\* continuous, since \(p\mapsto f(p)\) is continuous for each \(f\). Its inverse is continuous too: if evaluations at \(p_i\) converge to evaluation at \(p\) but \(p_i\) stays outside a neighbourhood \(U\) of \(p\) along a subnet, a Urysohn function \(f\) with \(f(p)=1\) and support in \(U\) gives \(0=f(p_i)\to1\), a contradiction.

**Examples 11.5.**
- *Radicals.* A Banach space with the zero product is its own radical. The dual numbers \(\mathbb C[\varepsilon]\), with \(\varepsilon^2=0\) and norm \(|a|+|b|\) for \(a+b\varepsilon\), are unital with radical \(\mathbb C\varepsilon\).
- *The Wiener algebra* ([Section 13](#oa-fnd-bn-21)) is semisimple, and its Gelfand representation is injective but not isometric.

## 12. Group algebras and transformation-group algebras

This section builds the convolution algebras of a locally compact group and of its actions on a locally compact space. It decides when they have an identity and when they are commutative. It uses Haar measure, from the lesson Haar measure on locally compact groups.

*Setting.* \(G\) is a locally compact Hausdorff group with identity \(e\) and a left Haar measure \(\mu\), written \(ds\) (existence of Haar measure). Compact sets have finite measure, and \(\mu\) is outer regular: the measure of a Borel set is the infimum of the measures of the open sets that contain it (Radon measures). Nonempty open sets have positive measure (positivity of Haar measure). The modular function \(\Delta:G\to(0,\infty)\) is the continuous homomorphism with \(\int f(ts)\,dt=\Delta(s)^{-1}\int f(t)\,dt\) (the modular function). The inversion formula \(\int f(t^{-1})\Delta(t)^{-1}\,dt=\int f(t)\,dt\) (inversion), applied to \(t\mapsto k(st)\) after left invariance, gives for every \(s\in G\)
\[
\begin{gathered}
\int k(t)\,dt\\
=\int k(sr^{-1})\,\Delta(r)^{-1}\,dr .
\end{gathered}
\tag{12.1}
\]
\(\Omega\) is an LCH space with a continuous right action \((\omega,s)\mapsto\omega s\) such that \(\omega e=\omega\) and \(\omega(st)=(\omega s)t\). Each map \(\omega\mapsto\omega s\) is a homeomorphism, with inverse \(\omega\mapsto\omega s^{-1}\). On \(K=C_c(\Omega\times G)\) put
\[
\begin{gathered}
(x\star y)(\omega,s)\\
=\int_Gx(\omega,t)\,y(\omega t,t^{-1}s)\,dt,\\
x^\sharp(\omega,s)\\
=\Delta(s)^{-1}\,\overline{x(\omega s,s^{-1})},\\
\|x\|_1\\
=\int_GX(s)\,ds,
\end{gathered}
\tag{12.2}
\]
where \(X(s)=\sup_{\omega\in\Omega}|x(\omega,s)|\). When \(\Omega\) is a single point, \(K=C_c(G)\) with convolution and the \(L^1\) norm.

For \(x\in K\), let \(K_x\) and \(L_x\) be the projections of \(\operatorname{supp}x\) to \(\Omega\) and to \(G\); both are compact. By the lemma on continuous functions of two variables in the section on iterated integrals on products, with the roles of the factors exchanged, \(s\mapsto x(\cdot,s)\) is continuous from \(G\) into \(C_0(\Omega)\) with the supremum norm. So \(X\) is continuous and vanishes off \(L_x\), and \(\|x\|_1<\infty\). If \(\|x\|_1=0\), then \(X=0\), because a nonzero continuous function \(X\geq0\) with compact support has positive integral (positivity of Haar measure). So \(\|\cdot\|_1\) is a norm.

*Uniform continuity.* For \(x\in K\), \(\sup_{\omega,s}|x(\omega,sr)-x(\omega,s)|\to0\) as \(r\to e\). This is the usual proof of the uniform continuity of functions in \(C_c(G)\) (topological groups), with the point of \(\Omega\) carried along. Let \(\eta>0\). For each \((p,s)\in\operatorname{supp}x\), continuity of \((p',v)\mapsto x(p',sv)\) at \((p,e)\) gives an open \(P\ni p\) and a symmetric open neighbourhood \(W\) of \(e\) with \(|x(p',sv)-x(p,s)|<\eta/2\) for \(p'\in P\) and \(v\in WW\). Finitely many of the sets \(P\times sW\) cover \(\operatorname{supp}x\); call them \(P_j\times s_jW_j\), and let \(W\) be the intersection of the \(W_j\). Let \(r\in W\). If \((p,s)\in\operatorname{supp}x\), then \((p,s)\in P_j\times s_jW_j\) for some \(j\); writing \(s=s_jv\), both \(x(p,s)\) and \(x(p,sr)=x(p,s_j(vr))\) are within \(\eta/2\) of \(x(p_j,s_j)\), because \(v\) and \(vr\) lie in \(W_jW_j\). If \((p,sr)\in\operatorname{supp}x\), the same argument applies to \(sr\) and \(r^{-1}\in W\). Otherwise both values are \(0\). So \(|x(p,sr)-x(p,s)|<\eta\) whenever \(r\in W\).

**Proposition 12.1** (the transformation-group algebra). (12.2) makes \(K\) a \(*\)-algebra with a submultiplicative norm and an isometric involution. For \(x,y,z\in K\):
\[
\begin{gathered}
x\star y\in K,\\
(x\star y)\star z\\
=x\star(y\star z),\\
x^\sharp\in K,\\
x^{\sharp\sharp}\\
=x,\\
(x\star y)^\sharp\\
=y^\sharp\star x^\sharp,\\
\|x\star y\|_1\\
\leq\|x\|_1\|y\|_1,\\
\|x^\sharp\|_1\\
=\|x\|_1,
\end{gathered}
\]
and \(\star\) is bilinear and \(\sharp\) conjugate-linear. So the completion \(\mathfrak A(\Omega,G)\) of \(K\) is an involutive Banach algebra. The isometric identification \(\mathfrak A(\Omega,G)\cong L^1(G,C_0(\Omega))\) and density of \(K\) are proved just after the algebra laws.

**Proof.** *\(x\star y\in K\).* For fixed \((\omega,s)\), the integrand \(t\mapsto x(\omega,t)y(\omega t,t^{-1}s)\) is continuous and vanishes off \(L_x\). If \((x\star y)(\omega,s)\neq0\), some \(t\) has \((\omega,t)\in\operatorname{supp}x\) and \(t^{-1}s\in L_y\), so \(\omega\in K_x\) and \(s\in L_xL_y\). So \(x\star y\) vanishes outside the compact set \(K_x\times L_xL_y\). For continuity, let \(F(\omega,s,t)\) be the integrand, a continuous function on \(\Omega\times G\times G\). Fix \((\omega_0,s_0)\) and \(\eta>0\). Each \(t\in L_x\) has neighbourhoods \(N_t\) of \((\omega_0,s_0)\) and \(O_t\) of \(t\) with \(|F(\omega,s,t')-F(\omega_0,s_0,t)|<\eta/2\) on \(N_t\times O_t\). Finitely many \(O_{t_i}\) cover \(L_x\); let \(N\) be the intersection of the corresponding \(N_{t_i}\). For \((\omega,s)\in N\) and \(t'\in L_x\), comparing both \(F(\omega,s,t')\) and \(F(\omega_0,s_0,t')\) with \(F(\omega_0,s_0,t_i)\) gives \(|F(\omega,s,t')-F(\omega_0,s_0,t')|<\eta\). So \(|(x\star y)(\omega,s)-(x\star y)(\omega_0,s_0)|\leq\eta\,\mu(L_x)\).

*The norm.* \(|(x\star y)(\omega,s)|\leq\int X(t)Y(t^{-1}s)\,dt\). The function \((t,s)\mapsto X(t)Y(t^{-1}s)\) lies in \(C_c(G\times G)\), so its two iterated integrals agree (iterated integrals on products), and left invariance gives \[
\begin{gathered}
\|x\star y\|_1\\
\leq\int X(t)\big(\int Y(t^{-1}s)\,ds\big)dt\\
=\|x\|_1\|y\|_1.
\end{gathered}
\]

*Associativity.* For fixed \((\omega,s)\),
\[
\begin{gathered}
((x\star y)\star z)(\omega,s)\\
=\iint x(\omega,r)\,y(\omega r,r^{-1}t)\,z(\omega t,t^{-1}s)\,dr\,dt,\\
(x\star(y\star z))(\omega,s)\\
=\int x(\omega,r)\int y(\omega r,v)\,z(\omega rv,v^{-1}r^{-1}s)\,dv\,dr .
\end{gathered}
\]
In the inner integral on the right, substitute \(v=r^{-1}t\) (left invariance); it becomes \(\int y(\omega r,r^{-1}t)z(\omega t,t^{-1}s)\,dt\). The integrand \((r,t)\mapsto x(\omega,r)y(\omega r,r^{-1}t)z(\omega t,t^{-1}s)\) is continuous and vanishes off \(L_x\times L_xL_y\), so, as in the norm estimate, the order of integration may be exchanged.

*The involution.* \(x^\sharp\) is continuous because \(\Delta\) is. If \(x^\sharp(\omega,s)\neq0\), then \((\omega s,s^{-1})\in\operatorname{supp}x\), so \(s\in L_x^{-1}\) and \(\omega=(\omega s)s^{-1}\) lies in the compact image of \(K_x\times L_x\) under the action. So \(x^\sharp\in K\). Next,
\[
\begin{gathered}
x^{\sharp\sharp}(\omega,s)\\
=\Delta(s)^{-1}\overline{x^\sharp(\omega s,s^{-1})}\\
=\Delta(s)^{-1}\Delta(s^{-1})^{-1}x(\omega,s)\\
=x(\omega,s).
\end{gathered}
\] Since \(\omega\mapsto\omega s\) is a bijection of \(\Omega\), \(\sup_\omega|x^\sharp(\omega,s)|=\Delta(s)^{-1}X(s^{-1})\), and the inversion formula gives \(\|x^\sharp\|_1=\int\Delta(s)^{-1}X(s^{-1})\,ds=\|x\|_1\). Finally, using \(\Delta(t)^{-1}\Delta(t^{-1}s)^{-1}=\Delta(s)^{-1}\),
\[
\begin{gathered}
(y^\sharp\star x^\sharp)(\omega,s)\\
=\Delta(s)^{-1}\,\overline{\int x(\omega s,s^{-1}t)\,y(\omega t,t^{-1})\,dt},\\
(x\star y)^\sharp(\omega,s)\\
=\Delta(s)^{-1}\,\overline{\int x(\omega s,r)\,y(\omega sr,r^{-1}s^{-1})\,dr},
\end{gathered}
\]
and the substitution \(r=s^{-1}t\) turns the second integral into the first.

*Completion.* The product and the involution are bounded, so they extend to the completion, and all the identities persist by continuity. \(\square\)

*The Bochner-space identification.* Here \(L^1(G,E)\), for a Banach space \(E\), can be defined as the completion, in the norm \(\int\|f(s)\|\,ds\), of finite-valued simple functions supported on Borel sets of finite Haar measure, after identifying functions of norm zero. This definition makes no separability or sigma-compactness assumption on \(G\) or \(E\).

For \(E=C_0(\Omega)\), the map \(x\mapsto[s\mapsto x(\cdot,s)]\) from \(K\) is isometric and takes values in this completion. Indeed, the coefficient map is norm continuous and vanishes off the compact \(L_x\), as proved before Proposition 12.1. Its image is compact. Choose finitely many norm balls of radius \(\varepsilon\) covering that image, and partition \(L_x\) into the Borel preimages of these balls, assigning each point to the first ball containing its value. Replacing the coefficient on each part by that ball’s centre gives a finite-valued simple function with error at most \(\varepsilon\mu(L_x)\) in \(L^1\). If \(\mu(L_x)=0\), the coefficient map already has norm zero.

The image of \(K\) is dense. To approximate a simple function \(\sum_{j=1}^na_j1_{E_j}\) with \(a_j\in C_0(\Omega)\) and \(\mu(E_j)<\infty\), use Proposition 3.1(4) of the Haar lesson to choose \(h_j\in C_c(G)\) close to \(1_{E_j}\) in scalar \(L^1\). The error in replacing the simple function by \(\sum_jh_ja_j\) is at most \(\sum_j\|a_j\|\|1_{E_j}-h_j\|_1\), so it can be made arbitrarily small. Next choose \(b_j\in C_c(\Omega)\) uniformly close to \(a_j\), using Proposition 2.1(3) of the Stone–Weierstrass lesson. The function \(x(\omega,s)=\sum_jb_j(\omega)h_j(s)\) belongs to \(K\), and the further error is at most \(\sum_j\|a_j-b_j\|_\infty\|h_j\|_1\). This too can be made arbitrarily small. Since simple functions are dense by the defining completion, \(K\) is dense in \(L^1(G,C_0(\Omega))\).

An isometry extends uniquely to an isometry of completions; its range is closed and dense, hence all of the target. Consequently \(\mathfrak A(\Omega,G)\cong L^1(G,C_0(\Omega))\) isometrically. The product and involution are the unique continuous extensions of (12.2), and the laws proved on \(K\) persist by continuity. The later lesson *Recovering covariance with nonunital coefficients* in *Crossed products and the flow of weights* develops representations of this algebra. Its representation results are not needed for this identification.


**Remark 12.2** (the factor \(\Delta(s)^{-1}\)). With the product (12.2), the involution is isometric only with the factor \(\Delta(s)^{-1}\), for the modular function normalized by \(\int f(ts)\,dt=\Delta(s)^{-1}\int f(t)\,dt\). With the factor \(\Delta(s)\) instead, the inversion formula would give \(\int\Delta(s)X(s^{-1})\,ds=\int\Delta(s)^{-2}X(s)\,ds\), which differs from \(\|x\|_1\) on every non-unimodular group for suitable \(x\). The right action enters the product as \(y(\omega t,t^{-1}s)\) and the involution as \(x(\omega s,s^{-1})\); Proposition 12.1 checks that these choices are compatible.

**Proposition 12.3** (the group algebra). \(L^1(G)\), with \((xy)(t)=\int x(s)y(s^{-1}t)\,ds\) and \(x^*(t)=\Delta(t)^{-1}\overline{x(t^{-1})}\), is an involutive Banach algebra. It is \(\mathfrak A(\Omega,G)\) for \(\Omega\) a single point: \(C_c(G)\) is dense in \(L^1(G)\) (density of compactly supported functions), \(L^1(G)\) is complete, and the \(L^1\) convolution extends the product of \(C_c(G)\) continuously (convolution). The algebra laws on all of \(L^1(G)\) are also proved directly in the lesson on Haar measure, in the section on convolution.

**Theorem 12.4** (when the transformation-group algebra has an identity). Let \(\Omega\) be nonempty. Then \(\mathfrak A(\Omega,G)\) has an identity exactly when \(\Omega\) is compact and \(G\) is discrete. In that case the identity is \(\varepsilon=c^{-1}1_{\Omega\times\{e\}}\), where \(c=\mu(\{e\})>0\); moreover \(\|\varepsilon\|_1=1\) and \(\varepsilon^\sharp=\varepsilon\).

The hypothesis that \(\Omega\) is nonempty is needed. If \(\Omega=\varnothing\), then \(K=\{0\}\) and \(\mathfrak A=\{0\}\), and the equivalence fails whichever convention is used for the zero algebra. If \(\{0\}\) counts as unital, the left side holds for every \(G\); if it does not, the left side fails for every \(G\). The right side holds exactly when \(G\) is discrete.

**Proof.** *Sufficiency.* In a discrete group, points are open and compact sets are finite. By left invariance \(\mu(\{s\})=\mu(\{e\})=c\) for all \(s\), and \(c>0\) because nonempty open sets have positive measure. Every subset of \(G\) is open, and the measure of an open set is the supremum of the measures of its compact subsets (Radon measures); this gives \(\mu(E)=c\cdot\#E\), and \(\int f\,d\mu=c\sum_sf(s)\) for \(f\geq0\) or integrable. The function \(\varepsilon\) is continuous, since \(\Omega\times\{e\}\) is open and closed, and it has compact support because \(\Omega\) is compact. For \(x\in K\), \((\varepsilon\star x)(\omega,s)=c\cdot c^{-1}x(\omega e,s)=x(\omega,s)\), and \((x\star\varepsilon)(\omega,s)=c\,x(\omega,s)\,c^{-1}\), since only \(t=s\) contributes. By continuity \(\varepsilon\) is an identity of \(\mathfrak A\). Also \(\|\varepsilon\|_1=c\cdot c^{-1}=1\), and \(\varepsilon^\sharp=\varepsilon\) because \(\Delta\equiv1\) on a discrete group (discrete groups are unimodular).

*A right approximate identity.* Let \(\Omega\) be nonempty, and fix \(\omega_0\in\Omega\). Let \(\lambda=(V,L)\) run over the pairs of an open neighbourhood \(V\) of \(e\) and a compact \(L\subseteq\Omega\) containing \(\omega_0\), directed by \((V,L)\leq(V',L')\) when \(V'\subseteq V\) and \(L'\supseteq L\). For each \(V\) choose \(h_V\in C_c(G)\) with \(h_V\geq0\), \(\operatorname{supp}h_V\subseteq V\) and \(\int h_V=1\) (approximate identities), and for each \(L\) choose \(\varphi_L\in C_c(\Omega)\) with \(0\leq\varphi_L\leq1\) and \(\varphi_L=1\) on \(L\) (Urysohn's lemma). Put \(\varepsilon_\lambda(\omega,s)=\varphi_L(\omega)h_V(s)\). Then \(\varepsilon_\lambda\in K\), and \(\|\varepsilon_\lambda\|_1=\int h_V=1\) because \(\sup\varphi_L=\varphi_L(\omega_0)=1\). We claim that \(a\star\varepsilon_\lambda\to a\) for every \(a\in\mathfrak A\).

First let \(x\in K\). The image \(C_x\) of \(\operatorname{supp}x\) under the action \((\omega,t)\mapsto\omega t\) is compact. If \(L\supseteq C_x\), then \(\varphi_L(\omega t)=1\) whenever \(x(\omega,t)\neq0\), so by (12.1)
\[
\begin{gathered}
(x\star\varepsilon_\lambda)(\omega,s)\\
=\int x(\omega,t)\,h_V(t^{-1}s)\,dt\\
=\int x(\omega,sr^{-1})\,h_V(r)\,\Delta(r)^{-1}\,dr .
\end{gathered}
\]
Since \(\int h_V=1\),
\[
\begin{gathered}
(x\star\varepsilon_\lambda)(\omega,s)-x(\omega,s)\\
=\int\big[x(\omega,sr^{-1})\Delta(r)^{-1}-x(\omega,s)\big]h_V(r)\,dr .
\end{gathered}
\]
Fix a compact neighbourhood \(N_0\) of \(e\), and take \(V\subseteq N_0\). For \(r\in V\), the bracket vanishes unless \(s\in L_xN_0\), and its absolute value is at most
\[
\begin{gathered}
\beta(V)\\
=\sup_{r\in V}\big(|\Delta(r)^{-1}-1|\,\|x\|_\infty\\
+\sup_{\omega,s}|x(\omega,sr^{-1})-x(\omega,s)|\big).
\end{gathered}
\] So \(\|x\star\varepsilon_\lambda-x\|_1\leq\beta(V)\,\mu(L_xN_0)\). By continuity of \(\Delta\) and the uniform continuity above, \(\beta(V)\to0\) as \(V\) shrinks. For \(a\in\mathfrak A\) and \(x\in K\), \(\|a\star\varepsilon_\lambda-a\|\leq2\|a-x\|+\|x\star\varepsilon_\lambda-x\|\), and \(K\) is dense.

*Necessity.* Suppose \(\mathfrak A\) has an identity \(1_{\mathfrak A}\). Then \(\varepsilon_\lambda=1_{\mathfrak A}\star\varepsilon_\lambda\to1_{\mathfrak A}\), so the net \((\varepsilon_\lambda)\) is Cauchy: there is \(\lambda_0=(V_0,L_0)\) with \(\|\varepsilon_\lambda-\varepsilon_{\lambda'}\|_1<1/2\) for all \(\lambda,\lambda'\geq\lambda_0\).

(i) *\(G\) is discrete.* Suppose not. Then \(\mu(\{e\})=0\). Otherwise every point would have the same positive measure; a compact neighbourhood of \(e\) would be finite, because compact sets have finite measure; and \(\{e\}\), the interior of that neighbourhood minus finitely many other points, would be open. By outer regularity, \(e\) has open neighbourhoods of arbitrarily small measure. Let \(m_0=\max h_{V_0}>0\), and choose an open neighbourhood \(V'\subseteq V_0\) of \(e\) with \(\mu(V')<1/(2m_0)\). Then \((V',L_0)\geq\lambda_0\). Both functions carry the factor \(\varphi_{L_0}\), whose supremum is \(1\), so
\[
\begin{gathered}
\|\varepsilon_{(V_0,L_0)}-\varepsilon_{(V',L_0)}\|_1\\
=\int|h_{V_0}-h_{V'}|\\
\geq\int_{V'}(h_{V'}-h_{V_0})\\
\geq1-m_0\,\mu(V')>\tfrac12,
\end{gathered}
\]
a contradiction.

(ii) *\(\Omega\) is compact.* Suppose not. The support of \(\varphi_{L_0}\) is compact, so some \(\omega_1\in\Omega\) lies outside it. Put \(L'=L_0\cup\{\omega_1\}\). Then \((V_0,L')\geq\lambda_0\), and
\[
\begin{gathered}
\|\varepsilon_{(V_0,L_0)}-\varepsilon_{(V_0,L')}\|_1\\
=\int\sup_\omega|\varphi_{L_0}(\omega)-\varphi_{L'}(\omega)|\,h_{V_0}(s)\,ds\\
=\|\varphi_{L_0}-\varphi_{L'}\|_\infty\\
\geq|0-1|\\
=1,
\end{gathered}
\]
a contradiction. \(\square\)

**Corollary 12.5** (the identity of \(L^1(G)\)). \(L^1(G)\) has an identity exactly when \(G\) is discrete. The identity is then \(c^{-1}1_{\{e\}}\) with \(c=\mu(\{e\})\). This is Theorem 12.4 with \(\Omega\) a point, together with Proposition 12.3. For counting measure (\(c=1\)), the lesson on Haar measure proves the same by a different argument, in the section on approximate identities.

**Theorem 12.6** (commutativity of \(L^1(G)\)). \(L^1(G)\) is commutative if and only if \(G\) is abelian.

**Proof.** If \(G\) is abelian, then \(\Delta\equiv1\), since abelian groups are unimodular (the modular function). When \(\Delta\equiv1\), the convolution \((xy)(t)\) can also be written as \(\int x(ts^{-1})y(s)\,ds\) (convolution). This gives \[
\begin{gathered}
(xy)(t)\\
=\int x(ts^{-1})y(s)\,ds\\
=\int y(s)x(s^{-1}t)\,ds\\
=(yx)(t),
\end{gathered}
\] since \(ts^{-1}=s^{-1}t\). Conversely, suppose \(L^1(G)\) is commutative, and let \(s,t\in G\) with \(st\neq ts\). Choose disjoint open sets \(O_1\ni st\) and \(O_2\ni ts\), and then, by continuity of multiplication, open sets \(V\ni s\) and \(W\ni t\) with \(VW\subseteq O_1\) and \(WV\subseteq O_2\). By Urysohn's lemma choose nonzero \(f,g\in C_c(G)\) with \(f,g\geq0\), \(\operatorname{supp}f\subseteq V\) and \(\operatorname{supp}g\subseteq W\). Then \(fg\) and \(gf\) (convolutions) are continuous (convolution); \(fg\) vanishes outside the compact set \(\operatorname{supp}f\cdot\operatorname{supp}g\subseteq O_1\), and \(gf\) vanishes outside \(O_2\). They agree almost everywhere, hence everywhere: a nonzero continuous function is nonzero on a nonempty open set, which has positive measure. So \(fg=gf\) vanishes outside \(O_1\) and outside \(O_2\), which are disjoint; hence \(fg=0\). But \(\int fg=\int f\int g>0\): the integral of a convolution is the product of the integrals, and \(\int f\) and \(\int g\) are positive because Haar measure gives positive integrals to nonzero functions \(f\geq0\) in \(C_c(G)\). This is a contradiction. \(\square\)

## 13. The Wiener algebra and Wiener's lemma

This section works out the Gelfand theory of the algebra of absolutely convergent Fourier series and deduces Wiener's lemma. By part (1) of Proposition 13.2 below, this algebra is the group algebra of \(\mathbb Z\) with counting measure, that is, \(\ell^1(\mathbb Z)\) with convolution.

*Setting.* A continuous function on \([0,1]\) with \(f(0)=f(1)\) is the same as a continuous function on the circle \(\mathbb R/\mathbb Z\), and we treat it so. Put \(e_n(s)=e^{2\pi ins}\) and \(\hat f(n)=\int_0^1f(s)e^{-2\pi ins}\,ds\). Let \(W\) be the set of continuous \(1\)-periodic \(f\) with \(\sum_n|\hat f(n)|<\infty\), and put \(\|f\|_W=\sum_n|\hat f(n)|\). In this section \(\hat f(n)\) is a Fourier coefficient; the Gelfand transform is written out in words.

**Lemma 13.1** (uniqueness of Fourier coefficients). A continuous \(1\)-periodic function \(h\) with \(\hat h(n)=0\) for all \(n\) is zero.

**Proof.** The Fejér kernel \(F_N=\sum_{|n|\leq N}\big(1-\frac{|n|}{N+1}\big)e_n\) equals \(\frac1{N+1}\big|\sum_{k=0}^Ne_k\big|^2\geq0\) and has integral \(1\) over \([0,1]\). Since \(|\sum_{k=0}^Ne_k(t)|=|\sin((N+1)\pi t)/\sin(\pi t)|\), for \(0<\delta<1/2\) and \(\delta\leq t\leq1-\delta\) we have \(F_N(t)\leq1/\big((N+1)\sin^2(\pi\delta)\big)\). The function \(\sigma_N(s)=\int_0^1h(s-t)F_N(t)\,dt\) equals \(\sum_{|n|\leq N}\big(1-\frac{|n|}{N+1}\big)\hat h(n)e_n(s)=0\). On the other hand, reading \(t\) modulo \(1\),
\[
\begin{gathered}
|\sigma_N(s)-h(s)|\\
\leq\int_0^1|h(s-t)-h(s)|F_N(t)\,dt\\
\leq\sup_{|t|\leq\delta}|h(s-t)-h(s)|+\frac{2\|h\|_\infty}{(N+1)\sin^2(\pi\delta)} .
\end{gathered}
\]
By uniform continuity the first term is small for small \(\delta\); then the second is small for large \(N\). So \(h=\lim_N\sigma_N=0\). \(\square\)

**Proposition 13.2.**
1. For \(f\in W\), \(f(s)=\sum_n\hat f(n)e_n(s)\), uniformly in \(s\), and \(\|f\|_\infty\leq\|f\|_W\). \(W\) is a commutative unital Banach algebra under pointwise multiplication, with \(\widehat{fg}(n)=\sum_k\hat f(k)\hat g(n-k)\). The map \(f\mapsto(\hat f(n))_n\) is an isometric algebra isomorphism of \(W\) onto \(\ell^1(\mathbb Z)\) with convolution.
2. For each \(t\in\mathbb R/\mathbb Z\), \(\omega_t(f)=f(t)\) is a character of \(W\).
3. \(e_1\) is invertible in \(W\), and \(\|e_1\|_W=\|e_1^{-1}\|_W=1\). For every character \(\omega\), \(|\omega(e_1)|=1\), so \(\omega(e_1)=e^{2\pi it}\) for exactly one \(t=t_\omega\in0,1)\).
4. \(\omega(f)=f(t_\omega)\) for every \(f\in W\).
5. \(t\mapsto\omega_t\) is a homeomorphism of the circle \(\mathbb R/\mathbb Z\) onto \(\operatorname{Ch}(W)\). The Gelfand transform of \(f\) is \(f\) itself, seen on the circle. \(W\) is semisimple, and its Gelfand representation is not isometric.
6. (*Wiener's lemma.*) If \(f\in W\) has no zero, then \(1/f\in W\): the Fourier coefficients of \(1/f\) are absolutely summable.

Part (5) identifies the character space with the circle. This is different from the closed interval: removing an interior point disconnects the interval, whereas removing any point leaves the circle connected.

**Proof.** (1) Since \(\sum_n|\hat f(n)|<\infty\), the series \(\sum_n\hat f(n)e_n\) converges uniformly to a continuous periodic function \(g\), whose coefficients are \(\hat f(n)\) (integrate term by term). By Lemma 13.1, \(f=g\), and \(|f(s)|\leq\sum_n|\hat f(n)|\). For \(f,g\in W\), the product of the two absolutely convergent series may be rearranged: \(fg=\sum_nc_ne_n\) with \(c_n=\sum_k\hat f(k)\hat g(n-k)\) and \(\sum_n|c_n|\leq\|f\|_W\|g\|_W\). This series converges uniformly, so \(\widehat{fg}(n)=c_n\), \(fg\in W\) and \(\|fg\|_W\leq\|f\|_W\|g\|_W\). The map \(f\mapsto(\hat f(n))\) is linear, isometric and multiplicative into \(\ell^1(\mathbb Z)\) with convolution. It is onto, because for \(c\in\ell^1(\mathbb Z)\) the function \(\sum_nc_ne_n\) lies in \(W\) and has coefficients \(c\). The space \(\ell^1(\mathbb Z)\) is \(L^1\) for counting measure and is complete by [Theorem 3.2 of the measure-tools lesson. Thus \(W\) is complete. The constant \(1=e_0\) is the identity, of norm \(1\).
(2) Evaluation is linear and multiplicative, and \(\omega_t(1)=1\).
(3) \(e_1e_{-1}=1\), and both have norm \(1\). Characters have norm at most \(1\) ([Proposition 10.3(1)](#oa-fnd-bn-17)), so \(|\omega(e_1)|\leq1\) and \(|\omega(e_1)|^{-1}=|\omega(e_{-1})|\leq1\).
(4) \(\omega(e_n)=\omega(e_1)^n=e^{2\pi int_\omega}\) for all \(n\in\mathbb Z\), negative \(n\) through inverses. The partial sums of \(\sum_n\hat f(n)e_n\) converge to \(f\) in \(W\), because the tails of \(\sum_n|\hat f(n)|\) tend to \(0\). Since \(\omega\) is continuous (Proposition 10.3(1)), \(\omega(f)=\sum_n\hat f(n)e^{2\pi int_\omega}=f(t_\omega)\) by (1).
(5) By (3) and (4), \(\omega=\omega_{t_\omega}\), so \(t\mapsto\omega_t\) is onto \(\operatorname{Ch}(W)\). It is one-to-one because \(e_1\) separates the points of the circle, and it is weak\* continuous because \(t\mapsto f(t)\) is continuous for each \(f\). A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism. The Gelfand transform of \(f\) sends \(\omega_t\) to \(f(t)\), so it vanishes only when \(f=0\), and \(W\) is semisimple. Its Gelfand norm is \(\|f\|_\infty\). For \(f=e_0+e_1-e_2\), multiplying by \(e_{-1}\) gives \[
\begin{gathered}
|f(s)|\\
=|e^{-2\pi is}+1-e^{2\pi is}|\\
=|1-2i\sin(2\pi s)|\\
\leq\sqrt5,
\end{gathered}
\] while \(\|f\|_W=3\).
(6) If \(f\) has no zero, then the Gelfand transform of \(f\) has no zero on \(\operatorname{Ch}(W)\), by (5). Since the spectrum of \(f\) is the range of its Gelfand transform ([Theorem 11.1(2)](#oa-fnd-bn-18)), \(0\notin\sigma_W(f)\). So \(f\) has an inverse \(g\in W\), and \(fg=1\) pointwise gives \(g=1/f\). \(\square\)

## Exercises

**Exercise 1** (medium; the algebra \(\ell^1(\mathbb Z_{\geq0})\)). Let \(A\) be the space of sequences \((x_n)_{n\geq0}\) with \(\|x\|=\sum_n|x_n|<\infty\), with the product \((xy)_n=\sum_{k=0}^nx_ky_{n-k}\). Let \(\delta_m\) be the sequence with \(1\) in place \(m\) and \(0\) elsewhere. Show that \(\operatorname{Ch}(A)\) is homeomorphic to the closed unit disc \(\bar{\mathbb D}\), with Gelfand transform \(\hat x(z)=\sum_nx_nz^n\); that \(A\) is semisimple; and that \(\sigma_A(\delta_1)=\bar{\mathbb D}\).

*Solution.* \(A\) is a commutative unital Banach algebra, with identity \(\delta_0\); submultiplicativity follows by rearranging absolutely convergent double series, as in [Proposition 13.2(1)](#oa-fnd-bn-21). Also \(\delta_1^n=\delta_n\), and \(x=\sum_nx_n\delta_n\) in norm. For a character \(\omega\), \(z=\omega(\delta_1)\) satisfies \(|z|\leq\|\delta_1\|=1\), because characters have norm at most \(1\) ([Proposition 10.3(1)](#oa-fnd-bn-17)), and by continuity \(\omega(x)=\sum_nx_nz^n\). Conversely, for \(|z|\leq1\), \(x\mapsto\sum_nx_nz^n\) is a character, by the Cauchy product formula for absolutely convergent series. So \(\omega\mapsto\omega(\delta_1)\) is a bijection of \(\operatorname{Ch}(A)\) onto \(\bar{\mathbb D}\). It is weak\* continuous, and \(\operatorname{Ch}(A)\) is compact (Proposition 10.3(2)), so it is a homeomorphism. If \(\hat x=0\) on \(\bar{\mathbb D}\), then \(x_n=\frac1{2\pi}\int_0^{2\pi}\hat x(e^{i\theta})e^{-in\theta}\,d\theta=0\) for all \(n\), integrating the uniformly convergent series term by term; so \(A\) is semisimple. Finally \(\sigma_A(\delta_1)=\hat\delta_1(\operatorname{Ch}(A))=\bar{\mathbb D}\) by [Theorem 11.1(2)](#oa-fnd-bn-18).

**Exercise 2** (medium; spectra of commuting elements). Let \(A\) be a unital Banach algebra and \(x,y\in A\) with \(xy=yx\). Show that \(\sigma_A(x+y)\subseteq\sigma_A(x)+\sigma_A(y)\) and \(\sigma_A(xy)\subseteq\sigma_A(x)\sigma_A(y)\), and that commutativity cannot be dropped.

*Solution.* The subalgebra generated by \(1,x,y\) is commutative, and the union of a chain of commutative subalgebras is commutative. By Zorn's lemma there is a maximal commutative subalgebra \(B\) containing \(1,x,y\). Its closure is commutative, by continuity of multiplication, so \(B\) is closed. If \(b\in B\) is invertible in \(A\), then \(b^{-1}\) commutes with every \(c\in B\) (multiply \(cb=bc\) by \(b^{-1}\) on both sides), so the algebra generated by \(B\) and \(b^{-1}\) is commutative, and maximality gives \(b^{-1}\in B\). Hence \(\sigma_B(b)=\sigma_A(b)\) for \(b\in B\). Since \(B\) is a commutative unital Banach algebra, [Theorem 11.1(2)](#oa-fnd-bn-18) gives \[
\begin{gathered}
\sigma_A(x+y)\\
=\sigma_B(x+y)\\
=\{\omega(x)+\omega(y):\omega\in\operatorname{Ch}(B)\}\\
\subseteq\sigma_B(x)+\sigma_B(y)\\
=\sigma_A(x)+\sigma_A(y),
\end{gathered}
\] and the same for \(xy\). Without commutativity, \(E_{12}+E_{21}\) has spectrum \(\{1,-1\}\), while \(\sigma(E_{12})+\sigma(E_{21})=\{0\}\). Also \(E_{12}E_{21}=E_{11}\) has spectrum \(\{0,1\}\), whereas \(\sigma(E_{12})\sigma(E_{21})=\{0\}\).

**Exercise 3** (medium; polynomial identities). Let \(P(\lambda)=(\lambda-\alpha_1)\cdots(\lambda-\alpha_n)\) with distinct \(\alpha_i\), and let \(x\) be an element of a nontrivial unital Banach algebra with \(P(x)=0\). Show that \(\sigma_A(x)\subseteq\{\alpha_1,\dots,\alpha_n\}\), and that \(f(x)=Q(x)\) for every \(f\) holomorphic near these points, where \(Q\) is the polynomial of degree less than \(n\) with \(Q(\alpha_i)=f(\alpha_i)\). Compute the idempotent \(e\) of [Example 6.12](#oa-fnd-bn-22).

*Solution.* By the spectral mapping theorem ([Theorem 6.10(2)](#oa-fnd-bn-12)), \(P(\sigma_A(x))=\sigma_A(P(x))=\sigma_A(0)=\{0\}\), so \(\sigma_A(x)\subseteq\{\alpha_1,\dots,\alpha_n\}\). Let \(U\) be a union of small disjoint discs around the \(\alpha_i\) on which \(f\) is holomorphic. The function \(f-Q\) vanishes at each \(\alpha_i\), and each \(\alpha_i\) is a simple zero of \(P\). So, as in the proof of Theorem 6.10(1), \(k=(f-Q)/P\) extends holomorphically across each \(\alpha_i\), and \(f-Q=Pk\) on \(U\). By [Theorem 6.7](#oa-fnd-bn-11), \(f(x)-Q(x)=P(x)k(x)=0\). For the matrix of Example 6.12, \((x-1)(x-2)=0\); with \(f(1)=0\) and \(f(2)=1\) we get \(Q(\lambda)=\lambda-1\), so \(e=x-1\).

**Exercise 4** (hard; the index group has no torsion). Let \(A\) be a commutative nontrivial unital Banach algebra. Show that if \(x\in G(A)\) and \(x^n\in G_0(A)\) for some \(n\geq1\), then \(x\in G_0(A)\).

*Solution.* By [Proposition 7.1(5)](#oa-fnd-bn-14), \(x^n=\exp y\) for some \(y\). Put \(z=\exp(y/n)\in G_0(A)\) and \(w=xz^{-1}\). Since \(A\) is commutative, \(w^n=x^nz^{-n}=\exp(y)\exp(-y)=1\). By the spectral mapping theorem ([Theorem 6.10(2)](#oa-fnd-bn-12)), \(\{\lambda^n:\lambda\in\sigma_A(w)\}=\sigma_A(w^n)=\{1\}\), so \(\sigma_A(w)\) lies in the finite set of \(n\)-th roots of unity. Choose \(0<\rho<1\) so small that the open discs of radius \(\rho\) around these roots are disjoint (for \(n\geq2\), adjacent roots are \(2\sin(\pi/n)\) apart, so \(\rho=1/2\) is too large once \(n\geq7\)). Write each root as \(\zeta=e^{i\theta}\) with \(\theta\) real. On the disc around \(\zeta\), \(|\lambda/\zeta-1|=|\lambda-\zeta|<\rho<1\), so \(L(\lambda)=\operatorname{Log}(\lambda/\zeta)+i\theta\) is holomorphic there and \(e^{L(\lambda)}=(\lambda/\zeta)\zeta=\lambda\). Together these functions define \(L\in H(U)\) on the union \(U\) of the discs, with \(\exp\circ L=\) identity. By the composition rule, Theorem 6.10(3), \(\exp(L(w))=w\), so \(w\in\exp(A)=G_0(A)\), and \(x=wz\in G_0(A)\). The set \(U\) is not connected, so this uses the calculus over cycles.

**Exercise 5** (easy; the unitization of a unital C\*-algebra). Let \(A\) be a C\*-algebra with identity \(1_A\), and let \(N(a+\lambda)=\max\big(p(a+\lambda),|\lambda|\big)\) on \(A_1\), as in [Proposition 3.4](#oa-fnd-bn-05). Show that \(p(a+\lambda)=\|a+\lambda1_A\|\), and that \((a,\lambda)\mapsto(a+\lambda1_A,\lambda)\) is an isometric \(*\)-isomorphism of \((A_1,N)\) onto \(A\oplus\mathbb C\) with the norm \(\max(\|b\|,|\mu|)\). Conclude that \((A_1,N)\) is a C\*-algebra, without using the inequality of Proposition 3.4(2).

*Solution.* For \(b\in A\), \((a+\lambda)b=(a+\lambda1_A)b\), so \(p(a+\lambda)\) is the norm of left multiplication by the element \(a+\lambda1_A\) of \(A\), which is \(\|a+\lambda1_A\|\) by Proposition 3.4(1). So \(N(a+\lambda)=\max(\|a+\lambda1_A\|,|\lambda|)\), which is the norm of the image \((a+\lambda1_A,\lambda)\). The map is an algebra isomorphism by [Proposition 3.3(3)](#oa-fnd-bn-04), and it preserves the involution because \((a+\lambda1_A)^*=a^*+\bar\lambda1_A\). The algebra \(A\oplus\mathbb C\) with componentwise operations and the maximum norm is a C\*-algebra, because the C\*-identity holds in each component. So \((A_1,N)\) is a C\*-algebra.

## Where this leads

- The next lesson, [on C\*-algebras and their continuous functional calculus](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md), specializes this theory to C\*-algebras. There the norm of every normal element equals its spectral radius (compare the last of Examples 5.7), and a commutative C\*-algebra is isometrically \(*\)-isomorphic to \(C_0\) of its character space, so that its Gelfand representation is isometric and onto. The spectrum of an element of a C\*-subalgebra is the same in both algebras (contrast Example 4.6). The characters of \(C_0(\Omega)\), which are needed there, are identified with the points of \(\Omega\) in Example 11.4.
- Representations of \(L^1(G)\) and of \(\mathfrak A(\Omega,G)\), and the crossed products they lead to, are the subject of the course *Crossed products and the flow of weights*.
- Not treated here: the calculus of several commuting elements and joint spectra; the Shilov boundary; Wiener–Tauberian theorems; the Jacobson radical of noncommutative algebras; the identification of the index group of \(C(\mathbb T)\) with \(\mathbb Z\); a description of the image of the Gelfand map.

## References


*Freely accessible reading:* [Vahid Shirbisheh, *Lectures on C*-algebras*, §2.5](https://arxiv.org/html/1211.3404v2) gives a route through holomorphic functional calculus; this lesson includes the general cycle-index conditions. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.
