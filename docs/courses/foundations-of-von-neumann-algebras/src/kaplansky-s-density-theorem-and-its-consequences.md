# Kaplansky's density theorem and its consequences

*Originally written by Claude Opus 5.5 (Anthropic), September 2026, with a separate historical AI spot-check; revised and self-checked by that writing AI in October 2026. GPT-6.1 Sol (OpenAI), at the Ultra setting, read and self-checked the full lesson and all five solutions, compared the exact programme prerequisites and supplied the remaining background details, October 2026. The bounded-net proof in Theorem 7.2 was added by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Public domain (CC0).*

The double commutant theorem says that a nondegenerate \(*\)-algebra \(A\) of operators is dense in its bicommutant \(A''\) for the strong and weak operator topologies. The nets that it produces can be unbounded. That makes them hard to use: a product of two strongly convergent nets need not converge unless the nets are bounded, and the functional calculus need not follow unbounded nets. Kaplansky's density theorem removes the difficulty. Every element of \(A''\) of norm at most one is a strong\(^*\) limit of a net of elements of \(A\) of norm at most one, and the same holds for self-adjoint and for positive elements.

This lesson proves the density theorem and the results that grow out of it. The engine is Kaplansky's continuity theorem: a continuous function of at most linear growth acts strongly continuously on normal operators. We show that linear growth is exactly the right condition. From the density theorem we then obtain the density of the unitary group of a unital C\(^*\)-algebra in the unitary group of its weak closure, with control of the distance to \(1\). Next come the noncommutative Egoroff and Lusin theorems: an element of \(A''\) agrees with an element of \(A\) on a projection that is large for a given normal state. They give Kadison's transitivity theorem, which says that an irreducible concrete C\(^*\)-algebra acts irreducibly in the purely algebraic sense. Finally, the up-down and up-down-up theorems build every self-adjoint element of \(A''\) from \(A\) by monotone limits, and give an order-theoretic description of von Neumann algebras.

Three tools are developed on the way. Section 2 shows that strong convergence of operators to a normal limit forces strong convergence of the adjoints, as long as the approximating operators are normal, or merely hyponormal. Section 3 proves Fuglede's theorem and builds the continuous functional calculus of finitely many commuting normal operators. Section 4 extends the functional calculus to bounded pointwise limits of continuous functions. This puts the spectral projections of an element of a von Neumann algebra inside the algebra, without the spectral theorem.

We assume the lessons [The double commutant theorem](the-double-commutant-theorem.md) and [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md). A few results are taken from [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md) (the exponential), The Stone–Weierstrass theorem for functions vanishing at infinity and Haar measure on locally compact groups (only its Riesz representation theorem). Facts from analysis are listed under *Results used from other lessons*.

The continuity theorem controls functional calculus along bounded nets; the density theorem then gives bounded approximants with the required order and adjoint properties. A freely readable treatment is [Blackadar].

## Conventions

Hilbert spaces are complex, of any dimension, and may be the zero space. Inner products are linear in the first variable. \(B(H)\) is the algebra of bounded operators on \(H\), and \(S=\{x\in B(H):\|x\|\le1\}\) is its closed unit ball. For a set \(X\subseteq B(H)\) we write \(X_h\) for its self-adjoint elements, \(X_+\) for its positive elements and \(U(X)\) for its unitaries. For instance, \(A_+\cap S\) is the set of positive elements of \(A\) of norm at most \(1\). The six operator topologies (weak, strong, strong\(^*\), \(\sigma\)-weak, \(\sigma\)-strong and \(\sigma\)-strong\(^*\)) are those of [the lesson on the double commutant theorem](the-double-commutant-theorem.md#oa-fnd-bi-01). "\(x_i\to x\) strongly" means that a net converges in the strong operator topology, and similarly for the other topologies.

We work with \(*\)-subalgebras of \(B(H)\); they need not be norm closed or contain \(1\). A norm-closed one is a *concrete C\(^*\)-algebra* on \(H\). The *weak closure* of a \(*\)-subalgebra \(A\) is its closure in the weak operator topology. By [the double commutant theorem](the-double-commutant-theorem.md#oa-fnd-bi-07) it is also the closure of \(A\) in the other five topologies, it is again a \(*\)-algebra, and it equals \(A''\) when \(A\) is nondegenerate, that is, when \([AH]=H\). A *von Neumann algebra* is a \(*\)-subalgebra \(M\) of \(B(H)\) with \(M=M''\). A linear functional on \(M\) is *normal* if it is \(\sigma\)-weakly continuous, and \(M_*^+\) is the set of positive normal functionals.

For vectors \(\xi,\eta\), \(\omega_\xi(x)=\langle x\xi,\xi\rangle\), and \(\theta_{\xi,\eta}\) is the rank-one operator \(\zeta\mapsto\langle\zeta,\eta\rangle\xi\). For projections \(p_i\), \(\bigvee_ip_i\) is the projection onto the closed span of their ranges, and \(\bigwedge_ip_i\) the projection onto the intersection of their ranges. A net \((x_i)\) of self-adjoint operators is *increasing* if \(i\le j\) implies \(x_i\le x_j\), and *decreasing* if \(i\le j\) implies \(x_i\ge x_j\). On \(\mathbb C^n\) we use the Euclidean norm \(|\lambda|\).

## Results used from other lessons

The facts below have full programme proofs at the stated loci. Human books and papers in the references provide historical context; they are not substitutes for these proofs.

1. *Dominated convergence*, with the full proof in Theorem 2.2 of Measure and Hilbert space tools for Haar integration. If measurable functions \(f_k\) converge pointwise to \(f\) and \(|f_k|\le g\) for an integrable \(g\), then \(\int|f_k-f|\to0\).
2. *Uniform boundedness* (Theorem 4.2 and Corollary 4.3(3) of Hahn–Banach, Baire and the basic theorems on Banach spaces). A family of bounded operators from a Banach space into a normed space that is bounded at each point is bounded in norm. In particular, a strongly convergent sequence in \(B(H)\) is bounded in norm.
3. *Liouville's theorem* (Corollary 3.3 of [Cauchy's theorem for cycles and its consequences](cauchy-s-theorem-for-cycles-and-its-consequences.md), with Lemma 3.1 there for power series). A bounded holomorphic function on \(\mathbb C\) is constant.
4. *Tychonoff's theorem* (Theorem 2.3 of [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md)). A product of compact spaces is compact.
5. *Orthonormal bases* (Theorem 4.1(4) of [Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md)). A separable Hilbert space has an orthonormal basis that is finite or countable.

Results proved in other lessons of the course are cited where they are used. The main ones are the operator topologies and the double commutant theorem ([The double commutant theorem](the-double-commutant-theorem.md)); the commutative Gelfand–Naimark theorem, the continuous functional calculus, the order on a C\(^*\)-algebra, the Löwner–Heinz inequality and approximate identities ([C\*-algebras](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md)); the exponential ([Banach algebras](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-14)); the Stone–Weierstrass theorem for \(C_0(X)\) (its lesson); and the Riesz representation theorem (Haar measure).

## 1. Bounded and monotone nets

Most arguments in this lesson pass to limits along nets. Two facts make this possible: products behave well along bounded nets, and bounded monotone nets always converge.

**Lemma 1.1** (bounded nets). Let \((x_i)\) and \((y_i)\) be nets in \(B(H)\) over the same directed set, with \(\sup_i\|x_i\|<\infty\).

1. If \(x_i\to x\) and \(y_i\to y\) strongly, then \(x_iy_i\to xy\) strongly.
2. If moreover \(\sup_i\|y_i\|<\infty\), and \(x_i\to x\) and \(y_i\to y\) strongly\(^*\), then \(x_iy_i\to xy\) strongly\(^*\).
3. A bounded net that converges strongly also converges \(\sigma\)-strongly and \(\sigma\)-weakly, and a bounded net that converges strongly\(^*\) also converges \(\sigma\)-strongly\(^*\). In particular \(\varphi(x_i)\to\varphi(x)\) for every normal functional \(\varphi\) on a von Neumann algebra that contains the net.

**Proof.** (1) For \(\xi\in H\),
\[
\begin{gathered}
\|(x_iy_i-xy)\xi\|\\
\le\|x_i\|\,\|(y_i-y)\xi\|+\|(x_i-x)y\xi\|,
\end{gathered}
\]
and both terms tend to \(0\). (2) By (1), \(x_iy_i\to xy\) strongly. The net \((y_i^*)\) is bounded, \(y_i^*\to y^*\) and \(x_i^*\to x^*\) strongly, so (1) gives \((x_iy_i)^*=y_i^*x_i^*\to y^*x^*\) strongly. (3) This is [Lemma 1.2(d) of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-01), together with the fact that the \(\sigma\)-strong topology is finer than the \(\sigma\)-weak one. \(\square\)

**Lemma 1.2** (closed sets). For \(r\ge0\), the ball \(rS\), the set \(B(H)_h\) and the cone \(B(H)_+\) are closed in each of the six topologies. So is the set \(\{x:x\ge c\}\) for a fixed self-adjoint \(c\).

**Proof.** The weak topology is the coarsest of the six, so it suffices to show weak closedness. Let \(x_i\to x\) weakly. If \(\|x_i\|\le r\), then \(|\langle x\xi,\eta\rangle|=\lim|\langle x_i\xi,\eta\rangle|\le r\|\xi\|\|\eta\|\), so \(\|x\|\le r\). If \(x_i=x_i^*\), then \(\langle x\xi,\eta\rangle=\lim\langle\xi,x_i\eta\rangle=\langle\xi,x\eta\rangle\). If \(x_i\ge c\), then \(\langle(x-c)\xi,\xi\rangle=\lim\langle(x_i-c)\xi,\xi\rangle\ge0\). \(\square\)

**Theorem 1.3** (Vigier's theorem). Let \((x_i)\) be an increasing net of self-adjoint operators with \(\sup_i\|x_i\|<\infty\). Then \((x_i)\) converges strongly to a self-adjoint operator \(x\), and \(x\) is the least upper bound of the net: \(x_i\le x\) for all \(i\), and \(x\le y\) for every self-adjoint \(y\) with \(x_i\le y\) for all \(i\). If all \(x_i\) lie in a von Neumann algebra \(M\), so does \(x\). Decreasing nets behave in the same way, with greatest lower bounds.

**Proof.** Let \(C=\sup_i\|x_i\|\). For each \(\xi\), the numbers \(\langle x_i\xi,\xi\rangle\) increase and are bounded by \(C\|\xi\|^2\), so they converge. By polarization, \(B(\xi,\eta)=\lim_i\langle x_i\xi,\eta\rangle\) exists for all \(\xi,\eta\). It is a sesquilinear form with \(|B(\xi,\eta)|\le C\|\xi\|\|\eta\|\) and \(B(\eta,\xi)=\overline{B(\xi,\eta)}\), so \(B(\xi,\eta)=\langle x\xi,\eta\rangle\) for a self-adjoint \(x\) with \(\|x\|\le C\). Since \(\langle x_i\xi,\xi\rangle\) increases to \(\langle x\xi,\xi\rangle\), we get \(x_i\le x\) for all \(i\); and if \(x_i\le y\) for all \(i\), then \(\langle x\xi,\xi\rangle=\lim\langle x_i\xi,\xi\rangle\le\langle y\xi,\xi\rangle\).

For strong convergence put \(d_i=x-x_i\). Then \(d_i\ge0\) and \(\|d_i\|\le2C\). For a positive operator \(d\), \(d^2\le\|d\|d\), because \(t^2\le\|d\|t\) on the interval \([0,\|d\|]\), which contains the spectrum of \(d\). Hence
\[
\|d_i\xi\|^2=\langle d_i^2\xi,\xi\rangle\le2C\langle d_i\xi,\xi\rangle\to0 .
\]
A von Neumann algebra is strongly closed, so \(x\in M\) when all \(x_i\) lie in \(M\). For a decreasing net apply this to \((-x_i)\). \(\square\)

**Corollary 1.4** (monotone nets of projections). An increasing net of projections \((p_i)\) converges strongly to \(\bigvee_ip_i\), and a decreasing net of projections converges strongly to \(\bigwedge_ip_i\). The limits lie in every von Neumann algebra that contains the net.

**Proof.** Let \((p_i)\) increase, with strong limit \(p\) (Theorem 1.3). By Lemma 1.1, \(p_i=p_i^2\to p^2\) strongly, so \(p=p^2\), and \(p\) is a projection. From \(p_i\le p\) we get \(p_iH\subseteq pH\) for all \(i\). Every vector \(p\xi=\lim p_i\xi\) lies in the closed span of the ranges \(p_iH\). So \(pH\) is exactly that closed span. For a decreasing net, apply this to the increasing net \((1-p_i)\): the limit is \(1-\bigvee_i(1-p_i)=\bigwedge_ip_i\). \(\square\)

## 2. Adjoints along nets of normal operators

The adjoint is not strongly continuous on \(B(H)\) when \(\dim H=\infty\). It is strongly continuous on the set of normal operators. We prove a slightly stronger statement, in which the approximating operators need only be hyponormal.

**Definition 2.1.** An operator \(a\) is *hyponormal* if \(\|a^*\xi\|\le\|a\xi\|\) for every \(\xi\in H\). Normal operators are hyponormal, and so are isometries, since \(\|v^*\xi\|\le\|\xi\|=\|v\xi\|\). An operator \(a\) is normal exactly when \(\|a^*\xi\|=\|a\xi\|\) for all \(\xi\): by polarization, this says \(\langle a^*a\xi,\xi\rangle=\langle aa^*\xi,\xi\rangle\) for all \(\xi\).

**Lemma 2.2.** For all \(a,b\in B(H)\) and \(\xi\in H\),
\[
\begin{gathered}
\|(a^*-b^*)\xi\|^2\\
=\|a^*\xi\|^2-\|b^*\xi\|^2\\
-2\operatorname{Re}\langle(a-b)b^*\xi,\xi\rangle .
\end{gathered}
\tag{2.1}
\]

**Proof.** Expanding the square, \[
\begin{gathered}
\|(a^*-b^*)\xi\|^2\\
=\|a^*\xi\|^2+\|b^*\xi\|^2-2\operatorname{Re}\langle a^*\xi,b^*\xi\rangle.
\end{gathered}
\] Now \(\operatorname{Re}\langle a^*\xi,b^*\xi\rangle=\operatorname{Re}\langle\xi,ab^*\xi\rangle=\operatorname{Re}\langle ab^*\xi,\xi\rangle\), and \(\langle ab^*\xi,\xi\rangle=\langle(a-b)b^*\xi,\xi\rangle+\|b^*\xi\|^2\). Substituting gives (2.1). \(\square\)

**Theorem 2.3.** Let \((a_i)\) be a net in \(B(H)\) that converges strongly to \(b\).

1. If every \(a_i\) is hyponormal, then \(b\) is hyponormal.
2. If every \(a_i\) is hyponormal and \(b\) is normal, then \(a_i^*\to b^*\) strongly. So \(a_i\to b\) strongly\(^*\).
3. If every \(a_i\) is normal, then \(a_i^*\to b^*\) strongly if and only if \(b\) is normal.

**Proof.** (1) The adjoint is weakly continuous, so \(a_i^*\to b^*\) weakly. Then \(\|b^*\xi\|^2=\lim_i\langle a_i^*\xi,b^*\xi\rangle\le\liminf_i\|a_i^*\xi\|\,\|b^*\xi\|\), hence \(\|b^*\xi\|\le\liminf_i\|a_i^*\xi\|\le\liminf_i\|a_i\xi\|=\|b\xi\|\).

(2) In (2.1) with \(a=a_i\), the last term tends to \(0\), because \((a_i-b)\eta\to0\) for the fixed vector \(\eta=b^*\xi\). Hyponormality gives \(\|a_i^*\xi\|^2\le\|a_i\xi\|^2\to\|b\xi\|^2=\|b^*\xi\|^2\). So \(\limsup_i\|(a_i^*-b^*)\xi\|^2\le0\).

(3) If \(b\) is normal, use (2). Conversely, if \(a_i^*\to b^*\) strongly, then \(\|b^*\xi\|=\lim\|a_i^*\xi\|=\lim\|a_i\xi\|=\|b\xi\|\) for every \(\xi\), so \(b\) is normal. \(\square\)

**Corollary 2.4.** On the set of normal operators, the strong and the strong\(^*\) topologies coincide, and the adjoint is strongly continuous there. A net of isometries that converges strongly to a unitary converges strongly\(^*\).

**Proof.** Both statements are Theorem 2.3(2). \(\square\)

**Example 2.5** (the limit must be normal). Let \((\xi_k)_{k\ge1}\) be an orthonormal sequence in \(H\). For \(n\ge1\) let \(u_n\) be the unitary with \(u_n\xi_k=\xi_{k+1}\) for \(k<n\), \(u_n\xi_n=\xi_1\), and \(u_n=1\) on the orthogonal complement of \(\xi_1,\dots,\xi_n\). Let \(v\) be the isometry with \(v\xi_k=\xi_{k+1}\) for all \(k\) and \(v=1\) on the orthogonal complement of all \(\xi_k\). For fixed \(k\), \(u_n\xi_k=v\xi_k\) as soon as \(n>k\), and \(u_n=v\) on the complement. The net is bounded, so \(u_n\to v\) strongly. The limit is not normal, since \(\|v^*\xi_1\|=0\ne1=\|v\xi_1\|\). As Theorem 2.3(3) predicts, the adjoints do not converge strongly: \(u_n^*\xi_1=\xi_n\), and these vectors are at mutual distance \(\sqrt2\). So a strong limit of unitaries need not be unitary, and a strong limit of normal operators need not be normal.

## 3. Commuting normal operators and their joint functional calculus

The continuity theorem of Section 5 is proved for several commuting normal operators at once. This section provides the functional calculus it needs. The first step is Fuglede's theorem, which shows that commuting normal operators also commute with each other's adjoints.

**Theorem 3.1** (Fuglede's theorem). Let \(a\in B(H)\) be normal and let \(b\in B(H)\) commute with \(a\). Then \(b\) commutes with \(a^*\).



**Proof.** We use the exponential \(\exp x=\sum_kx^k/k!\) of [the lesson on Banach algebras](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-14): \(\exp(x+y)=\exp x\exp y\) when \(xy=yx\). The adjoint is continuous and conjugate linear, so applying it to the partial sums gives \((\exp x)^*=\exp(x^*)\). For \(z\in\mathbb C\) define
\[
F(z)=\exp(za^*)\,b\,\exp(-za^*).
\]
Since \(b\) commutes with \(a\), it commutes with every partial sum of \(\exp(\bar za)\), hence with \(\exp(\bar za)\), and \(b=\exp(-\bar za)\,b\,\exp(\bar za)\). The operators \(a\) and \(a^*\) commute, so
\[
\begin{gathered}
F(z)\\
=\exp(za^*-\bar za)\,b\,\exp(\bar za-za^*)\\
=U(z)\,b\,U(z)^{-1},\\
U(z)\\
=\exp(za^*-\bar za).
\end{gathered}
\]
The operator \(X=za^*-\bar za\) satisfies \(X^*=-X\). Hence \(U(z)^*=\exp(X^*)=\exp(-X)=U(z)^{-1}\), so \(U(z)\) is unitary and \(\|F(z)\|=\|b\|\) for every \(z\).

Multiplying the two absolutely convergent series gives a norm-convergent power series \(F(z)=\sum_{m\ge0}z^mc_m\) for all \(z\), with \(c_0=b\) and \(c_1=a^*b-ba^*\). For fixed \(\xi,\eta\in H\), the function \(z\mapsto\langle F(z)\xi,\eta\rangle=\sum_mz^m\langle c_m\xi,\eta\rangle\) is therefore holomorphic on \(\mathbb C\), and it is bounded by \(\|b\|\|\xi\|\|\eta\|\). By Liouville's theorem it is constant, so its coefficient of \(z\) vanishes: \(\langle(a^*b-ba^*)\xi,\eta\rangle=0\). As \(\xi,\eta\) are arbitrary, \(a^*b=ba^*\). \(\square\)

**Definition 3.2.** A *commuting normal tuple* is an \(n\)-tuple \(a=(a_1,\dots,a_n)\) of normal operators on \(H\) with \(a_ja_k=a_ka_j\) for all \(j,k\). By Fuglede's theorem, each \(a_j\) also commutes with each \(a_k^*\). So the C\(^*\)-algebra \(C^*(1,a)\) generated by \(1,a_1,\dots,a_n\) is commutative: it is the norm closure of the polynomials in the pairwise commuting operators \(a_j,a_j^*\). Its characters form a compact space \(\Omega\), and the *joint spectrum* of \(a\) is
\[
\sigma(a)=\{(\chi(a_1),\dots,\chi(a_n)):\chi\in\Omega\}\subseteq\mathbb C^n .
\]

**Theorem 3.3** (the joint functional calculus). Let \(a\) be a commuting normal tuple on \(H\ne\{0\}\), and let \(\iota_j\) be the \(j\)-th coordinate function on \(\mathbb C^n\).

1. The map \(\Psi(\chi)=(\chi(a_1),\dots,\chi(a_n))\) is a homeomorphism of \(\Omega\) onto \(\sigma(a)\). So \(\sigma(a)\) is a nonempty compact set. It lies in \(\sigma(a_1)\times\dots\times\sigma(a_n)\), and its projection to the \(j\)-th coordinate is \(\sigma(a_j)\).
2. There is exactly one unital \(*\)-homomorphism \(f\mapsto f(a)\) from \(C(\sigma(a))\) into \(B(H)\) with \(\iota_j(a)=a_j\) for all \(j\). It is isometric, \(\|f(a)\|=\max_{\sigma(a)}|f|\), and its range is \(C^*(1,a)\). Each \(f(a)\) is normal.
3. \(f(a)\) commutes with every operator that commutes with \(a_1,\dots,a_n\).
4. For \(n=1\) this is the continuous functional calculus of a normal operator.

For a closed set \(G\supseteq\sigma(a)\) and a continuous \(f\) on \(G\) we write \(f(a)\) for \((f|_{\sigma(a)})(a)\). If \(f\) is bounded, then \(\|f(a)\|\le\sup_G|f|\).

**Proof.** (1) Characters of the commutative C\(^*\)-algebra \(B=C^*(1,a)\) are \(*\)-homomorphisms ([Theorem 2.1 of the lesson on C\*-algebras](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-04)), so a character is determined by its values at \(a_1,\dots,a_n\): it then knows its values at the \(a_j^*\), at all polynomials in them, and, being continuous, on \(B\). So \(\Psi\) is injective. It is continuous for the weak\(^*\) topology, and \(\Omega\) is compact, so \(\Psi\) is a homeomorphism onto its image \(\sigma(a)\). Since \(H\ne\{0\}\), \(B\ne\{0\}\) has characters, and \(\sigma(a)\) is not empty. In a commutative unital Banach algebra the spectrum of an element is the set of values of the characters on it ([the Gelfand representation](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-18)), and the spectrum of \(a_j\) in \(B\) is its spectrum in \(B(H)\) ([spectral permanence](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-06)). So \(\{\chi(a_j):\chi\in\Omega\}=\sigma(a_j)\), which gives the last two claims.

(2) By the commutative Gelfand–Naimark theorem, the Gelfand transform \(\mathcal G\) is an isometric \(*\)-isomorphism of \(B\) onto \(C(\Omega)\). Composition with \(\Psi\) is an isometric \(*\)-isomorphism of \(C(\sigma(a))\) onto \(C(\Omega)\). So \(f(a)=\mathcal G^{-1}(f\circ\Psi)\) defines an isometric \(*\)-isomorphism of \(C(\sigma(a))\) onto \(B\), and \(\iota_j(a)=\mathcal G^{-1}(\chi\mapsto\chi(a_j))=a_j\). Elements of \(B\) are normal, because \(B\) is commutative. For uniqueness, a second unital \(*\)-homomorphism with the same values at the \(\iota_j\) agrees with the first on the polynomials in the \(\iota_j\) and \(\bar\iota_j\). These are dense in \(C(\sigma(a))\) by the Stone–Weierstrass theorem, since they separate points and contain the constants. Both maps are contractive ([Theorem 4.2 of the lesson on C\*-algebras](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-12)), so they agree.

(3) An operator that commutes with all \(a_j\) commutes with all \(a_j^*\) by Fuglede's theorem, hence with all of \(B\).

(4) For \(n=1\) both calculi are unital \(*\)-homomorphisms that send \(\iota\) to \(a_1\), so they agree by uniqueness.

For the last statement, \(\|f(a)\|=\max_{\sigma(a)}|f|\le\sup_G|f|\). \(\square\)

**Example 3.4.** (a) Let \(H=\ell^2(\mathbb N)\) with basis \((\delta_k)\), and let \(a_j\) be the diagonal operator \(a_j\delta_k=\lambda^{(k)}_j\delta_k\) for bounded sequences \((\lambda^{(k)}_j)_k\), \(j=1,\dots,n\). Put \(\lambda^{(k)}=(\lambda^{(k)}_1,\dots,\lambda^{(k)}_n)\), and let \(K\) be the closure of \(\{\lambda^{(k)}:k\in\mathbb N\}\). Then \(\sigma(a)=K\). Indeed, \(f\mapsto\) the diagonal operator with entries \(f(\lambda^{(k)})\) is a unital \(*\)-homomorphism from \(C(K)\) into \(B(H)\). It is isometric, because the points \(\lambda^{(k)}\) are dense in \(K\), and it sends \(\iota_j\) to \(a_j\). Its range is therefore \(C^*(1,a)\), isomorphic to \(C(K)\), and the characters of \(C(K)\) are the evaluations at points of \(K\) ([the characters of \(C_0(\Omega)\)](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-04)). (b) For a projection \(p\ne0,1\), the pair \((p,1-p)\) has joint spectrum \(\{(1,0),(0,1)\}\), a proper subset of \(\sigma(p)\times\sigma(1-p)=\{0,1\}^2\).

## 4. Pointwise limits in the functional calculus

The continuous functional calculus does not produce spectral projections. A von Neumann algebra is strongly closed, so we can instead pass to strong limits of continuous functions of an operator. This section shows that bounded pointwise convergence of the functions gives strong convergence of the operators.

**Definition 4.1.** Let \(K\subseteq\mathbb C\) be compact. We write \(\mathcal B_1(K)\) for the set of functions \(\varphi:K\to\mathbb C\) for which there are continuous functions \(\varphi_k\) on \(K\) with \(\sup_k\max_K|\varphi_k|<\infty\) and \(\varphi_k(\lambda)\to\varphi(\lambda)\) for every \(\lambda\in K\). This set is a \(*\)-algebra under pointwise operations, and it contains \(C(K)\). Corollaries 4.3, 4.5 and 4.6 below show that it contains indicator functions of intervals, the argument function on the unit circle and binary digits.

**Theorem 4.2** (bounded pointwise limits). Let \(a\) be a normal operator with spectrum \(K\). For \(\varphi\in\mathcal B_1(K)\) and any sequence \((\varphi_k)\) as in Definition 4.1, the operators \(\varphi_k(a)\) converge strongly to an operator \(\varphi(a)\) that depends only on \(\varphi\). The map \(\varphi\mapsto\varphi(a)\) is a \(*\)-homomorphism from \(\mathcal B_1(K)\) into \(B(H)\) that extends the continuous functional calculus. It satisfies \(\|\varphi(a)\|\le\sup_K|\varphi|\), and \(\varphi\ge0\) implies \(\varphi(a)\ge0\). Every \(\varphi(a)\) lies in every von Neumann algebra that contains \(a\), and commutes with every operator that commutes with \(a\).

**Proof.** For \(\xi\in H\), the map \(f\mapsto\langle f(a)\xi,\xi\rangle\) is a positive linear functional on \(C(K)\), because \(f\ge0\) implies \(f(a)\ge0\). By the Riesz representation theorem there is a finite positive Borel measure \(\mu_\xi\) on \(K\) with
\[
\begin{gathered}
\langle f(a)\xi,\xi\rangle\\
=\int_Kf\,d\mu_\xi\\
(f\in C(K)),
\end{gathered}
\tag{4.1}
\]
and \(\mu_\xi(K)=\|\xi\|^2\). Functions in \(\mathcal B_1(K)\) are Borel, being pointwise limits of continuous functions.

Let \(\varphi_k\to\varphi\) as in Definition 4.1, with \(|\varphi_k|\le c\). For \(k,l\), by (4.1) applied to \(|\varphi_k-\varphi_l|^2\),
\[
\begin{gathered}
\|(\varphi_k(a)-\varphi_l(a))\xi\|^2\\
=\langle|\varphi_k-\varphi_l|^2(a)\xi,\xi\rangle\\
=\int|\varphi_k-\varphi_l|^2\,d\mu_\xi\\
\le2\int|\varphi_k-\varphi|^2\,d\mu_\xi+2\int|\varphi-\varphi_l|^2\,d\mu_\xi .
\end{gathered}
\]
The integrands tend to \(0\) pointwise and are bounded by \(4c^2\), which is integrable for the finite measure \(\mu_\xi\). By dominated convergence the right side tends to \(0\). So \((\varphi_k(a)\xi)\) is a Cauchy sequence. Call its limit \(\varphi(a)\xi\). The map \(\varphi(a)\) is linear, and \[
\begin{gathered}
\|\varphi(a)\xi\|^2\\
=\lim\int|\varphi_k|^2\,d\mu_\xi\\
=\int|\varphi|^2\,d\mu_\xi\\
\le(\sup_K|\varphi|)^2\|\xi\|^2.
\end{gathered}
\] If \(\psi_k\to\varphi\) is a second such sequence, then \(\|(\varphi_k(a)-\psi_k(a))\xi\|^2=\int|\varphi_k-\psi_k|^2\,d\mu_\xi\to0\), so the limit does not depend on the sequence. A constant sequence shows that the new map extends the continuous calculus.

Linearity is clear. Since \(\bar\varphi_k\to\bar\varphi\), we get \[
\begin{gathered}
\langle\bar\varphi(a)\xi,\eta\rangle\\
=\lim\langle\varphi_k(a)^*\xi,\eta\rangle\\
=\lim\langle\xi,\varphi_k(a)\eta\rangle\\
=\langle\xi,\varphi(a)\eta\rangle,
\end{gathered}
\] so \(\bar\varphi(a)=\varphi(a)^*\). If \(\psi_k\to\psi\) as well, then \(\varphi_k\psi_k\to\varphi\psi\) with a uniform bound, and \((\varphi_k\psi_k)(a)=\varphi_k(a)\psi_k(a)\to\varphi(a)\psi(a)\) strongly by Lemma 1.1. So \((\varphi\psi)(a)=\varphi(a)\psi(a)\). If \(\varphi\ge0\), then \(\langle\varphi(a)\xi,\xi\rangle=\lim\int\varphi_k\,d\mu_\xi=\int\varphi\,d\mu_\xi\ge0\), by dominated convergence again.

A von Neumann algebra \(N\) that contains \(a\) contains \(1\), \(a^*\) and all norm limits of polynomials in \(a,a^*\), so it contains every \(\varphi_k(a)\); it is strongly closed, so it contains \(\varphi(a)\). An operator that commutes with \(a\) commutes with \(a^*\) (Theorem 3.1), hence with every \(\varphi_k(a)\), hence with the strong limit \(\varphi(a)\). \(\square\)

**Corollary 4.3** (spectral projections). Let \(x\) be a self-adjoint element of a von Neumann algebra \(N\), let \(c\in\mathbb R\), and let \(p=1_{(c,\infty)}(x)\).

1. \(p\) is a projection in \(N\), and it commutes with every operator that commutes with \(x\).
2. \((x-c)p\ge0\) and \((x-c)(1-p)\le0\). In particular \(cp\le xp\) and \(x(1-p)\le c(1-p)\).
3. If \(c\ge0\) and \(x=exe\) for a projection \(e\), then \(p\le e\).
4. If \(c<\max\sigma(x)\), then \(p\ne0\). If \(c>\min\sigma(x)\), then \(p\ne1\).

**Proof.** The functions \(g_k(t)=\min(1,\max(0,k(t-c)))\) are continuous, take values in \([0,1]\) and increase to \(1_{(c,\infty)}\), so \(1_{(c,\infty)}\in\mathcal B_1(\sigma(x))\). (1) It is real and equal to its square, so \(p=p^*=p^2\) by Theorem 4.2, which also gives the rest. (2) The functions \((t-c)1_{(c,\infty)}(t)\) and \((c-t)(1-1_{(c,\infty)}(t))\) are nonnegative and lie in \(\mathcal B_1(\sigma(x))\); apply positivity in Theorem 4.2. (3) If \(c\ge0\), then \(g_k(0)=0\), so each \(g_k(x)\) is a norm limit of polynomials in \(x\) without constant term. Each such polynomial \(q(x)\) satisfies \(q(x)=eq(x)e\). So \(g_k(x)=eg_k(x)e\) and, in the limit, \(p=epe\), which means \(p\le e\). (4) If \(p=0\), then (2) gives \(x-c=(x-c)(1-p)\le0\), so \(\sigma(x)\subseteq(-\infty,c]\). If \(p=1\), then \(x-c=(x-c)p\ge0\), so \(\sigma(x)\subseteq[c,\infty)\). \(\square\)

**Corollary 4.4.** A von Neumann algebra \(N\) on \(H\ne\{0\}\) whose only projections are \(0\) and \(1\) is \(\mathbb C1\).

**Proof.** Let \(x\in N\) be self-adjoint. If \(\sigma(x)\) contained two points \(s<t\), then any \(c\) with \(s<c<t\) would give a projection \(1_{(c,\infty)}(x)\in N\) different from \(0\) and \(1\) (Corollary 4.3(4)). So \(\sigma(x)=\{\lambda\}\), and \(\|x-\lambda\|\), which is the spectral radius of the self-adjoint operator \(x-\lambda\) ([the norm of a normal element](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-01)), is \(0\). Every element of \(N\) is a combination of two self-adjoint elements of \(N\). \(\square\)

**Corollary 4.5** (unitaries are exponentials). Let \(u\) be a unitary in a von Neumann algebra \(N\).

1. There is a self-adjoint \(h\in N\) with \(\|h\|\le\pi\) and \(u=\exp(ih)\).
2. If \(\|u-1\|<2\), put \(\alpha=2\arcsin(\|u-1\|/2)<\pi\). Then \(h\) can be chosen in \(C^*(1,u)\), with \(\|h\|\le\alpha\).

**Proof.** The spectrum of \(u\) lies in the unit circle \(\mathbb T\). Let \(\arg:\mathbb T\to(-\pi,\pi]\) be the argument, \(\arg(e^{i\theta})=\theta\) for \(-\pi<\theta\le\pi\). For \(k\ge1\) let \(\varphi_k(e^{i\theta})=\theta\) for \(\theta\in[-\pi+1/k,\pi]\), and let \(\varphi_k\) be linear in \(\theta\) on \([-\pi,-\pi+1/k]\), from the value \(\pi\) at \(\theta=-\pi\) to the value \(-\pi+1/k\). Each \(\varphi_k\) is continuous on \(\mathbb T\), because its values at \(\theta=\pi\) and \(\theta=-\pi\), which describe the same point \(-1\), are both \(\pi\). The values lie in \([-\pi,\pi]\), and \(\varphi_k\to\arg\) pointwise on \(\mathbb T\). So \(\arg\in\mathcal B_1(\sigma(u))\).

(1) Put \(h=\arg(u)\). By Theorem 4.2, \(h\) is a self-adjoint element of \(N\) with \(\|h\|\le\pi\), and \(h^m=(\arg^m)(u)\) for every \(m\). The partial sums of \(\exp(ih)\) are therefore \(\big(\sum_{m\le M}(i\arg)^m/m!\big)(u)\). These functions converge uniformly on \(\mathbb T\) to \(e^{i\arg}\), which is the identity function \(\lambda\mapsto\lambda\). By the norm bound of Theorem 4.2, \(\exp(ih)=(e^{i\arg})(u)=u\).

(2) For \(\lambda\in\sigma(u)\), \(\lambda-1\) lies in the spectrum of \(u-1\), so \(|\lambda-1|\le\|u-1\|\). Since \(|e^{i\theta}-1|=2|\sin(\theta/2)|\), the spectrum lies in the arc \(\{e^{i\theta}:|\theta|\le\alpha\}\). There \(\arg\) is continuous, so \(h=\arg(u)\) is given by the continuous calculus, lies in \(C^*(1,u)\), and satisfies \(\|h\|\le\alpha\). \(\square\)

**Corollary 4.6** (dyadic expansion). Every \(x\) in a von Neumann algebra \(N\) with \(0\le x\le1\) is a norm-convergent sum \(x=\sum_{k\ge1}2^{-k}p_k\) of projections \(p_k\in N\), each a spectral projection of \(x\).

**Proof.** For \(t\in[0,1)\) let \(d_k(t)\in\{0,1\}\) be the \(k\)-th binary digit of \(t\), from the expansion \(t=\sum_k2^{-k}d_k(t)\) that does not end in an infinite string of ones, and put \(d_k(1)=1\) for all \(k\). Then \(d_k\) is the indicator function of a finite union of intervals of the form \([j2^{-k},(j+1)2^{-k})\), together with the point \(1\). Such functions lie in \(\mathcal B_1([0,1])\): the indicator function of \([\alpha,\beta)\) is the pointwise limit of continuous piecewise linear functions with values in \([0,1]\) that are \(1\) on \([\alpha,\beta-1/m]\) and \(0\) outside \((\alpha-1/m,\beta)\), and the indicator function of the point \(1\) is the pointwise limit of \(\max(0,1-m|t-1|)\). Put \(p_k=d_k(x)\), a projection in \(N\) by Theorem 4.2. For every \(t\in[0,1]\), \(|t-\sum_{k\le m}2^{-k}d_k(t)|\le2^{-m}\). By the norm bound of Theorem 4.2, \(\|x-\sum_{k\le m}2^{-k}p_k\|\le2^{-m}\). \(\square\)

## 5. Kaplansky's continuity theorem

We now come to Kaplansky's continuity theorem. It says that the functional calculus of a continuous function of at most linear growth is strongly continuous on commuting normal tuples, even along unbounded nets.

For a closed set \(G\subseteq\mathbb C^n\), let \(\mathcal N_G\) be the set of commuting normal \(n\)-tuples \(a\) on \(H\) with \(\sigma(a)\subseteq G\). A net \((a^{(i)})\) in \(\mathcal N_G\) *converges strongly* to \(a\) if \(a^{(i)}_j\to a_j\) strongly for each \(j\). For \(n=1\) and \(G=\mathbb R\), \(\mathcal N_G\) is the set of self-adjoint operators; for \(G=\mathbb T\) it is the set of unitaries. For an \(n\)-tuple \(a\) of arbitrary operators put
\[
R(a)=\Big(1+\sum_{k=1}^na_k^*a_k\Big)^{-1} .
\]

**Lemma 5.1** (resolvent estimates). Let \(a\) and \(b\) be \(n\)-tuples of operators.

1. \(0\le R(a)\le1\), \(\|a_jR(a)\|\le\frac12\), \(\|R(a)a_j^*\|\le\frac12\) and \(\|a_jR(a)a_k^*\|\le1\) for all \(j,k\).
2. \[
\begin{gathered}
R(a)-R(b)\\
=\sum_kR(a)\big[(b_k^*-a_k^*)b_k\\
+a_k^*(b_k-a_k)\big]R(b).
\end{gathered}
\]
3. If \((a^{(i)})\) is a net of \(n\)-tuples with \(a^{(i)}_k\to b_k\) and \(a^{(i)*}_k\to b_k^*\) strongly for every \(k\), then \(R(a^{(i)})\to R(b)\) and \(a^{(i)}_jR(a^{(i)})\to b_jR(b)\) strongly for every \(j\).

**Proof.** (1) Put \(X=\sum_ka_k^*a_k\ge0\) and \(R=R(a)=(1+X)^{-1}\). By the functional calculus of \(X\), \(0\le R\le1\) and \(RXR\le\frac14\), since \(t/(1+t)^2\le\frac14\) for \(t\ge0\). As \(a_j^*a_j\le X\), we get \(\|a_jR\|^2=\|Ra_j^*a_jR\|\le\|RXR\|\le\frac14\). The adjoint gives \(\|Ra_j^*\|\le\frac12\). Also \[
\begin{gathered}
\|a_jR^{1/2}\|^2\\
=\|R^{1/2}a_j^*a_jR^{1/2}\|\\
\le\|R^{1/2}XR^{1/2}\|\\
\le1,
\end{gathered}
\] since \(t/(1+t)\le1\); so \(\|a_jRa_k^*\|\le\|a_jR^{1/2}\|\,\|R^{1/2}a_k^*\|\le1\).

(2) \[
\begin{gathered}
R(a)-R(b)\\
=R(a)\big[(1+X_b)-(1+X_a)\big]R(b),
\end{gathered}
\] with \(X_a=\sum_ka_k^*a_k\) and \(X_b\) likewise, and \(b_k^*b_k-a_k^*a_k=(b_k^*-a_k^*)b_k+a_k^*(b_k-a_k)\).

(3) Write \(a=a^{(i)}\). By (1) and (2),
\[
\begin{gathered}
\|(R(a)-R(b))\xi\|\\
\le\sum_k\Big(\|(b_k^*-a_k^*)b_kR(b)\xi\|\\
+\tfrac12\|(b_k-a_k)R(b)\xi\|\Big),
\end{gathered}
\]
and each term tends to \(0\), because the vectors \(b_kR(b)\xi\) and \(R(b)\xi\) are fixed. Next, \[
\begin{gathered}
a_jR(a)-b_jR(b)\\
=(a_j-b_j)R(b)+a_j(R(a)-R(b)).
\end{gathered}
\] Inserting (2) and using \(\|a_jR(a)\|\le\frac12\) and \(\|a_jR(a)a_k^*\|\le1\),
\[
\begin{gathered}
\|(a_jR(a)-b_jR(b))\xi\|\\
\le\|(a_j-b_j)R(b)\xi\|\\
+\sum_k\Big(\tfrac12\|(b_k^*-a_k^*)b_kR(b)\xi\|\\
+\|(b_k-a_k)R(b)\xi\|\Big)\to0 .\\
\square
\end{gathered}
\]

**Theorem 5.2** (Kaplansky's continuity theorem). Let \(G\subseteq\mathbb C^n\) be closed, and let \(f:G\to\mathbb C\) be continuous with
\[
\sup_{\lambda\in G}\frac{|f(\lambda)|}{1+|\lambda|}<\infty .
\tag{5.1}
\]
If a net \((a^{(i)})\) in \(\mathcal N_G\) converges strongly to \(a\in\mathcal N_G\), then \(f(a^{(i)})\to f(a)\) strongly and strongly\(^*\).


**Proof.** *Step 1: a closed \(*\)-algebra of good functions.* Let \(\mathcal C\) be the set of bounded continuous functions \(g\) on \(G\) such that \(a\mapsto g(a)\) is strongly continuous on \(\mathcal N_G\). It contains the constants. It is closed under sums. It is closed under products: for \(g,k\in\mathcal C\),
\[
\begin{gathered}
g(a^{(i)})k(a^{(i)})-g(a)k(a)\\
=g(a^{(i)})\big(k(a^{(i)})-k(a)\big)\\
+\big(g(a^{(i)})-g(a)\big)k(a),
\end{gathered}
\]
and \(\|g(a^{(i)})\|\le\sup_G|g|\). It is closed under complex conjugation: \(\bar g(a)=g(a)^*\), and the operators \(g(a^{(i)})\) are normal and converge strongly to the normal operator \(g(a)\), so their adjoints converge strongly (Theorem 2.3(3)). It is closed under uniform limits: if \(g_m\to g\) uniformly on \(G\) with \(g_m\in\mathcal C\), then
\[
\begin{gathered}
\|(g(a^{(i)})-g(a))\xi\|\\
\le2\sup_G|g-g_m|\,\|\xi\|+\|(g_m(a^{(i)})-g_m(a))\xi\| .
\end{gathered}
\]
Finally, strong convergence of \(g(a^{(i)})\) to \(g(a)\) implies strong\(^*\) convergence, since all these operators are normal (Corollary 2.4).

*Step 2: two resolvent functions.* Let \(r(\lambda)=(1+|\lambda|^2)^{-1}\) and \(s_j(\lambda)=\lambda_jr(\lambda)\). Since the calculus is a \(*\)-homomorphism with \(\iota_k(a)=a_k\), we have \(r(a)=R(a)\) and \(s_j(a)=a_jR(a)\) for \(a\in\mathcal N_G\). If \(a^{(i)}\to a\) strongly in \(\mathcal N_G\), then also \(a^{(i)*}_k\to a_k^*\) strongly, by Corollary 2.4. Lemma 5.1(3) now shows \(r,s_j\in\mathcal C\).

*Step 3: functions vanishing at infinity.* The closed set \(G\) is locally compact. The functions \(r\) and \(s_j\) vanish at infinity on \(G\). The \(*\)-algebra they generate without constant terms consists of functions in \(C_0(G)\). It vanishes nowhere, because \(r>0\). It separates points: if \(r(\lambda)=r(\mu)\) and \(s_j(\lambda)=s_j(\mu)\) for all \(j\), then \(|\lambda|=|\mu|\) and \(\lambda_j=\mu_j\). By [the Stone–Weierstrass theorem for \(C_0(X)\)](stone-weierstrass-c0.md#oa-fnd-sw-09), this \(*\)-algebra is dense in \(C_0(G)\). It lies in \(\mathcal C\) by Steps 1 and 2, and \(\mathcal C\) is closed, so \(C_0(G)\subseteq\mathcal C\).

*Step 4: products with a coordinate.* Let \(k\in\mathcal C\). Then \(a\mapsto a_jk(a)\) is strongly continuous on \(\mathcal N_G\). Indeed, \(k(a)\) commutes with \(a_j\) (Theorem 3.3(3)), so
\[
\begin{gathered}
a^{(i)}_jk(a^{(i)})-a_jk(a)\\
=k(a^{(i)})\big(a^{(i)}_j-a_j\big)+\big(k(a^{(i)})-k(a)\big)a_j ,
\end{gathered}
\]
and \(\|k(a^{(i)})\|\le\sup_G|k|\).

*Step 5: bounded functions.* Let \(g\) be bounded and continuous on \(G\). Since \(r(\lambda)(1+|\lambda|^2)=1\),
\[
g=gr+\sum_j\iota_j\cdot(\bar\iota_jgr).
\tag{5.2}
\]
Here \(gr\in C_0(G)\), and \(\bar\iota_jgr\in C_0(G)\) because \(|\lambda_j|\,|g(\lambda)|\,r(\lambda)\le\sup|g|\cdot|\lambda|/(1+|\lambda|^2)\). Applying the calculus to (5.2), \(g(a)=(gr)(a)+\sum_ja_j\,(\bar\iota_jgr)(a)\). The first term is strongly continuous in \(a\) by Step 3, and each summand by Steps 3 and 4. So \(g\in\mathcal C\).

*Step 6: linear growth.* Let \(f\) satisfy (5.1) with constant \(C\). The identity (5.2) holds with \(f\) in place of \(g\). Now \(fr\in C_0(G)\), since \(|f|r\le C(1+|\lambda|)/(1+|\lambda|^2)\). Each \(\bar\iota_jfr\) is bounded and continuous, since \(|\lambda|(1+|\lambda|)\le2(1+|\lambda|^2)\) gives \(|\lambda_j||f|r\le2C\); so it lies in \(\mathcal C\) by Step 5. By Steps 3 and 4, \(f(a)=(fr)(a)+\sum_ja_j(\bar\iota_jfr)(a)\) is strongly continuous in \(a\), and strong\(^*\) continuity follows as in Step 1. \(\square\)

**Corollary 5.3.** Let \(G\subseteq\mathbb C^n\) be closed and \(f:G\to\mathbb C\) continuous.

1. If \(G\) is compact, the calculus of \(f\) is strongly continuous on \(\mathcal N_G\).
2. For every \(c>0\), the calculus of \(f\) is strongly continuous on the set of \(a\in\mathcal N_G\) with \(\|a_j\|\le c\) for all \(j\).
3. If a sequence \((a^{(m)})\) in \(\mathcal N_G\) converges strongly to \(a\in\mathcal N_G\), then \(f(a^{(m)})\to f(a)\) strongly.
4. For self-adjoint operators (\(n=1\), \(G=\mathbb R\)), every continuous \(f\) with \(|f(t)|\le C(1+|t|)\) acts strongly continuously. Examples are \(|t|\), \(\max(t,0)\), \(e^{it}\), \(2t/(1+t^2)\), and any continuous function on a compact interval, applied to self-adjoint operators with spectrum in that interval.

**Proof.** (1) A continuous function on a compact set is bounded, so (5.1) holds. (2) For a normal operator, the norm is the largest modulus of a point of the spectrum ([the norm of a normal element](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-01)), and \(\sigma(a_j)\) is the \(j\)-th projection of \(\sigma(a)\) (Theorem 3.3(1)). So the set in question is \(\mathcal N_{G_c}\) with the compact set \(G_c=\{\lambda\in G:|\lambda_j|\le c\text{ for all }j\}\), and (1) applies to \(f|_{G_c}\). (3) A strongly convergent sequence is bounded in norm by the uniform boundedness principle, so (2) applies. (4) is Theorem 5.2 and (1). \(\square\)

**Example 5.4** (the Cayley transform). For a self-adjoint \(h\) the *Cayley transform* \(\kappa(h)=(h-i)(h+i)^{-1}\) is the calculus of the bounded continuous function \((t-i)/(t+i)\), which has modulus \(1\). So \(\kappa(h)\) is unitary, and \(\kappa\) is strongly continuous on self-adjoint operators by Corollary 5.3(4). A direct estimate is also available. Since \(\kappa(h)=1-2i(h+i)^{-1}\), the resolvent identity gives
\[
\begin{gathered}
\kappa(h)-\kappa(k)\\
=2i\,(h+i)^{-1}(h-k)(k+i)^{-1},\\
\text{so}\\
\|(\kappa(h)-\kappa(k))\xi\|\\
\le2\|(h-k)(k+i)^{-1}\xi\|,
\end{gathered}
\]
because \(\|(h+i)^{-1}\|\le1\). For fixed \(k\) and \(\xi\) the right side tends to \(0\) as \(h\to k\) strongly.

## 6. Linear growth is necessary

Condition (5.1) cannot be weakened. In infinite dimensions, a continuous function of faster growth fails to act strongly continuously, although it still acts continuously on bounded sets and along sequences (Corollary 5.3).

**Theorem 6.1.** Let \(H\) be infinite-dimensional, \(G\subseteq\mathbb C^n\) closed, and \(f:G\to\mathbb C\) continuous. Suppose that for some \(g_0\in G\) the calculus of \(f\) is strongly continuous on \(\mathcal N_G\) at the constant tuple \(g_0\cdot1=(g_{0,1}1,\dots,g_{0,n}1)\). Then \(f\) satisfies (5.1). If \(\dim H<\infty\), every continuous \(f\) acts strongly continuously on \(\mathcal N_G\).

**Proof.** Suppose (5.1) fails. As \(f\) is bounded on the compact sets \(\{\lambda\in G:|\lambda|\le c\}\), there are \(t_k\in G\) with \(|t_k|\to\infty\) and \(|f(t_k)|\ge k(1+|t_k|)\). Then \(|f(t_k)-f(g_0)|\to\infty\) and \(|t_k-g_0|/|f(t_k)-f(g_0)|\to0\). Dropping finitely many \(k\), we may assume \(|f(t_k)-f(g_0)|\ge1\), and we put \(c_k=|f(t_k)-f(g_0)|^{-1}\in(0,1]\) and \(s_k=(1-c_k^2)^{1/2}\).

Fix a unit vector \(\xi\). Let \(\Lambda\) be the set of pairs \(\lambda=(F,k)\) with \(F\subseteq H\) a finite-dimensional subspace and \(k\ge1\), directed by \((F,k)\le(F',k')\) if \(F\subseteq F'\) and \(k\le k'\). For each \(\lambda=(F,k)\) choose a unit vector \(\eta_\lambda\) orthogonal to \(F\) and to \(\xi\), which exists because \(\dim H=\infty\). Put \(v_\lambda=c_k\xi+s_k\eta_\lambda\), a unit vector, \(p_\lambda=\theta_{v_\lambda,v_\lambda}\), and
\[
\begin{gathered}
a^{(\lambda)}\\
=g_0\cdot1+(t_k-g_0)\,p_\lambda,\\
\text{that is,}\\
a^{(\lambda)}_j\\
=g_{0,j}1+(t_{k,j}-g_{0,j})p_\lambda .
\end{gathered}
\]
These are commuting normal operators. The algebra \(C^*(1,a^{(\lambda)})\) is spanned by \(1\) and \(p_\lambda\), and its characters send \(p_\lambda\) to \(0\) or \(1\), so \(\sigma(a^{(\lambda)})=\{g_0,t_k\}\subseteq G\). The map \(\varphi\mapsto\varphi(g_0)(1-p_\lambda)+\varphi(t_k)p_\lambda\) is a unital \(*\)-homomorphism on \(C(\{g_0,t_k\})\) that sends each \(\iota_j\) to \(a^{(\lambda)}_j\), so by Theorem 3.3(2) it is the calculus: \(f(a^{(\lambda)})=f(g_0)(1-p_\lambda)+f(t_k)p_\lambda\).

*Strong convergence of the tuples.* Let \(\omega\in H\), and choose \(\lambda_0=(F_0,k_0)\) with \(\omega\in F_0\). For \(\lambda=(F,k)\ge\lambda_0\), \(\eta_\lambda\perp\omega\), so \(\langle\omega,v_\lambda\rangle=c_k\langle\omega,\xi\rangle\) and
\[
\|(a^{(\lambda)}_j-g_{0,j})\omega\|\le|t_k-g_0|\,c_k\,|\langle\omega,\xi\rangle|\to0 .
\]
*No convergence of the calculus.* On the other hand, \[
\begin{gathered}
\|(f(a^{(\lambda)})-f(g_0))\xi\|\\
=|f(t_k)-f(g_0)|\,|\langle\xi,v_\lambda\rangle|\\
=|f(t_k)-f(g_0)|\,c_k\\
=1
\end{gathered}
\] for every \(\lambda\). So \(f(a^{(\lambda)})\) does not converge strongly to \(f(g_0\cdot1)=f(g_0)1\).

If \(\dim H<\infty\), the strong topology is the norm topology. A net that converges in norm is eventually bounded, and Corollary 5.3(2) applies to its tail. \(\square\)

**Example 6.2** (squaring). On an infinite-dimensional \(H\), the map \(h\mapsto h^2\) on self-adjoint operators is not strongly continuous at \(0\). In the construction above take \(f(t)=t^2\), \(g_0=0\), \(t_k=k\) and \(c_k=k^{-2}\). Then \(h_\lambda=kp_\lambda\to0\) strongly, but \(\|h_\lambda^2\xi\|=k^2\,|\langle\xi,v_\lambda\rangle|=1\). By Corollary 5.3(3), no sequence can show this.

## 7. Kaplansky's density theorem

**Theorem 7.1** (Kaplansky's density theorem). Let \(A\) be a \(*\)-subalgebra of \(B(H)\), not necessarily norm closed or nondegenerate, and let \(M\) be its weak closure.

1. \(A\cap S\) is strongly\(^*\) dense in \(M\cap S\).
2. \(A_h\cap S\) is strongly\(^*\) dense in \(M_h\cap S\).
3. \(A_+\cap S\) is strongly\(^*\) dense in \(M_+\cap S\).
4. In each of (1)–(3), the closure of the smaller set in any of the six operator topologies is the larger set.


**Proof.** *Step 1: we may assume that \(A\) is norm closed.* Let \(\bar A\) be the norm closure of \(A\). It is a concrete C\(^*\)-algebra with the same weak closure \(M\). Every \(c\in\bar A\cap S\) is a norm limit of elements of \(A\cap S\): if \(c_m\in A\) and \(c_m\to c\) in norm, then \(c_m/\max(1,\|c_m\|)\in A\cap S\) also converges to \(c\). For self-adjoint \(c\) use \(\frac12(c_m+c_m^*)\). For positive \(c\), approximate \(c^{1/2}\in\bar A_h\cap S\) by \(d_m\in A_h\cap S\); then \(d_m^2\in A_+\cap S\) and \(d_m^2\to c\) in norm. Norm convergence implies strong\(^*\) convergence, so it suffices to prove (1)–(3) for \(\bar A\). From now on \(A\) is a C\(^*\)-algebra.

*Step 2: self-adjoint elements.* Let \(x\in M_h\cap S\). Put \(f(t)=2t/(1+t^2)\) on \(\mathbb R\) and \(g(s)=s/(1+\sqrt{1-s^2})\) on \([-1,1]\). Both are continuous, \(f(0)=g(0)=0\), \(|f|\le1\), and \(f(g(s))=s\) for \(s\in[-1,1]\): with \(s=\sin\theta\) and \(|\theta|\le\pi/2\), \(g(s)=\tan(\theta/2)\) and \(f(\tan(\theta/2))=\sin\theta\). The weak closure \(M\) is a norm-closed \(*\)-algebra, so \(y=g(x)\) lies in \(M\) ([the calculus without an identity](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-08)), and \(f(y)=x\) by the composition rule. By the double commutant theorem, \(M\) is also the strong\(^*\) closure of \(A\). Choose a net \((c_i)\) in \(A\) with \(c_i\to y\) strongly\(^*\), and put \(b_i=\frac12(c_i+c_i^*)\in A_h\). Then \(b_i\to y\) strongly. By Corollary 5.3(4), \(f(b_i)\to f(y)=x\) strongly, hence strongly\(^*\), since these operators are self-adjoint. Each \(f(b_i)\) lies in \(A_h\), because \(f(0)=0\), and has norm at most \(\max|f|=1\).

*Step 3: arbitrary elements.* Let \(x\in M\cap S\). On \(H\oplus H\) consider the \(*\)-algebra \(M_2(A)\) of \(2\times2\) matrices with entries in \(A\). A net of \(2\times2\) matrices converges weakly exactly when its four entries do, so the weak closure of \(M_2(A)\) is \(M_2(M)\). The self-adjoint matrix \(X=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}\) lies in \(M_2(M)\), and \(\|X\|=\|x\|\le1\), since \(X^2=\begin{pmatrix}xx^*&0\\0&x^*x\end{pmatrix}\). By Step 2 there is a net of self-adjoint \(Y_i=\begin{pmatrix}b_i&a_i\\a_i^*&d_i\end{pmatrix}\in M_2(A)\) with \(\|Y_i\|\le1\) and \(Y_i\to X\) strongly. The corner entries of a matrix are compressions of it, so \(\|a_i\|\le1\), \(a_i\to x\) strongly and \(a_i^*\to x^*\) strongly. So \(a_i\to x\) strongly\(^*\), with \(a_i\in A\cap S\).

*Step 4: positive elements.* Let \(x\in M_+\cap S\). Then \(x^{1/2}\in M_h\cap S\), and Step 2 gives \(b_i\in A_h\cap S\) with \(b_i\to x^{1/2}\) strongly\(^*\). By Lemma 1.1(2), \(b_i^2\to x\) strongly\(^*\), and \(b_i^2\in A_+\cap S\).

*Step 5: the six topologies.* A bounded net that converges strongly\(^*\) converges \(\sigma\)-strongly\(^*\) (Lemma 1.1(3)), and the \(\sigma\)-strong\(^*\) topology is the finest of the six. So each larger set lies in each closure of the smaller one. Conversely, \(M\cap S\), \(M_h\cap S\) and \(M_+\cap S\) are weakly closed, by Lemma 1.2 and because \(M\) is weakly closed. So the closures are exactly the larger sets. \(\square\)

**Remark 7.2** (norm density fails). In general \(A\cap S\) is not norm dense in \(M\cap S\). For an infinite-dimensional \(H\), the compact operators \(K(H)\) form a nondegenerate C\(^*\)-algebra whose weak closure is \(B(H)\) ([Example 4.6 of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-07)). For every compact \(k\), \(\|1-k\|\ge1\): otherwise \(k=1-(1-k)\) would be invertible by the Neumann series, and \(1=kk^{-1}\) would be compact, which is false in infinite dimensions. So \(1\) is not a norm limit of elements of \(K(H)\cap S\).

**Example 7.3** (the algebraic structure is needed). Kaplansky's theorem fails for self-adjoint subspaces that are not algebras. On \(H=\ell^2(\mathbb N)\) with basis \((\delta_m)\), let \(\omega(x)=\sum_m2^{-m}\langle x\delta_m,\delta_m\rangle\) and \(V=\ker\omega\). Then \(V^*=V\). By [Exercise 1.5 of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-01), \(V\) is not weakly closed. Its weak closure is a weakly closed subspace that strictly contains a subspace of codimension one, so it is \(B(H)\). But \(V\cap S\) is weakly closed. Indeed, a bounded weakly convergent net converges \(\sigma\)-weakly ([Lemma 1.2(d) of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-01)), and \(\omega\) is \(\sigma\)-weakly continuous, so \(\omega\) vanishes at every weak limit of a net in \(V\cap S\). So the weak closure of \(V\cap S\) is \(V\cap S\), which does not contain \(1\in B(H)\cap S\).

**Theorem 7.2** (The bounded-net algebra). Let \(A\subseteq B(H)\) be a norm-closed *-subalgebra, with no nondegeneracy or identity assumption. Let \(D\) consist of the strong limits of norm-bounded nets in \(A\). Then \(D\) is the strong closure of \(A\), and
\[
D\cap B(H)_1=\overline{A\cap B(H)_1}^{\,s}.
\]
The same statement holds for self-adjoint and positive unit balls. In the unrestricted unit ball, approximation can also be chosen strongly* convergent.

This is the bounded-net route of [G. A. Elliott and C. J. K. Griffin, *On a question of Kaplansky concerning his density theorem* (2024)](https://arxiv.org/html/2410.03668v1). It explains how bounded-set functional calculus suffices for density. The argument below uses the complete trace-duality and Krein–Šmulian proofs in the operator-topologies lesson: [trace duality, Theorem 5.4](compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.md#oa-fnd-lt-06), and [Krein–Šmulian and its bounded-ball consequence, Theorems 9.3 and 9.6](compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.md#oa-fnd-lt-10), together with [the double commutant lesson, Theorem 4.4](the-double-commutant-theorem.md#oa-fnd-bi-06). Those results do not use Kaplansky density. The stronger continuity theorem on unbounded normal nets remains Theorem 5.2 above.

**Proof.** Sums and scalar multiples of bounded approximating nets show that \(D\) is a complex vector space containing \(A\). If \(a_i\to x\) and \(b_j\to y\) strongly, with respective uniform bounds \(C,E\), the product net satisfies
\[
\begin{gathered}
\|(a_i b_j-xy)\xi\|\\
\le C\|(b_j-y)\xi\|+\|(a_i-x)y\xi\|\\
\longrightarrow0.
\end{gathered}
\]
Its norm is at most \(CE\), so \(xy\in D\).

Adjoints require convexity. If \(a_i\to x\) strongly and \(\|a_i\|\le C\), then \(a_i^*\to x^*\) weakly. The set \(A\cap CB(H)_1\) is convex. Weak and strong closures of a convex set agree, by Hahn–Banach separation, so \(x^*\) is a strong limit of a net from this same bounded set. Thus \(D=D^*\). Similarly, if \(x=x^*\in D\), the net \((a_i+a_i^*)/2\) converges weakly to \(x\) and lies in the convex set \(A_h\cap CB(H)_1\). Hence \(x\) has a bounded strong approximation by self-adjoint elements of \(A\).

For such a net \(h_i\to h\), all spectra lie in a fixed interval \([-C,C]\), enlarging \(C\) if necessary. Every continuous real function \(f\) on that interval with \(f(0)=0\) satisfies \(f(h_i)\to f(h)\) strongly. Indeed, approximate \(f\) uniformly by real polynomials and subtract their value at zero to obtain polynomials without constant term. Their functional calculi lie in \(A\); the error in operator norm is uniform over the whole net. Each polynomial converges strongly by bounded-net multiplication (Lemma 1.1). The same uniform error then proves strong convergence of \(f(h_i)\).

When \(\|h\|\le1\), choose \(f(t)=\max(-1,\min(t,1))\). Then \(f(h)=h\) and the \(f(h_i)\) are self-adjoint contractions in \(A\). If \(0\le h\le1\), use \(f(t)=\max(0,\min(t,1))\) to obtain positive contractions. Both functions vanish at zero, which is necessary when \(A\) has no identity.

For \(x\in D\), each entry of
\[
X=\begin{pmatrix}0&x\\x^*&0\end{pmatrix}\in B(H\oplus H)
\]
belongs to \(D\). A finite product of the directed sets for its entries gives a uniformly bounded strong approximating net from \(M_2(A)\): the matrix norm is at most the sum of its four entry norms. Thus \(X\) belongs to the bounded-net algebra associated with \(M_2(A)\). If \(\|x\|\le1\), then \(\|X\|\le1\), since \(X^2=\operatorname{diag}(xx^*,x^*x)\). The preceding self-adjoint argument on \(H\oplus H\) gives self-adjoint contractions \(X_i\in M_2(A)\) tending strongly to \(X\). Their upper-right entries \(c_i\) have norm at most one. Testing \(X_i\) on \((0,\xi)\) gives \(c_i\xi\to x\xi\), and testing on \((\xi,0)\) gives \(c_i^*\xi\to x^*\xi\). Consequently \(c_i\to x\) strongly*. This proves that every contraction of \(D\) lies in the strong closure of the unit ball of \(A\). The reverse inclusion follows directly from the definition of \(D\).

It remains to prove that \(D\) is closed; a union of bounded closures need not be closed merely by its definition. The preceding equality shows that \(D\cap B(H)_1\) is strongly closed. Scaling shows the same for \(D\cap rB(H)_1\), for every \(r>0\). Since \(D\) is convex, Theorem 9.6 of the operator-topologies lesson, proved from trace duality and Krein–Šmulian, makes \(D\) ultraweakly closed. Since \(D\) is a *-subalgebra, Theorem 4.4 of the double commutant lesson identifies its ultraweak and strong closures, also in the degenerate case. Hence \(D\) is strongly closed. It contains \(A\) and is contained in its strong closure, so equality follows. This proof has not used Theorem 7.1 or the unbounded-net continuity theorem. \(\square\)

For a *-algebra \(A_0\) that is not norm closed, apply the theorem to its norm closure \(A\). The unit ball of \(A_0\) is norm dense in that of \(A\): if \(\|a\|\le1\) and \(\|b-a\|<\delta\), with \(b\in A_0\), then \(b/(1+\delta)\) is a contraction and tends in norm to \(a\). Self-adjoint \(a\) can first be approximated by \((b+b^*)/2\). Thus the general contraction density follows without changing the strong closure. Positivity for a nonclosed *-algebra is handled by the square-root approximation in the proof of Theorem 7.1; functional calculus need not stay in \(A_0\).


## 8. The unitary group and its closures

**Theorem 8.1.** Let \(U(H)\) be the unitary group of \(B(H)\).

1. \(U(H)\) is closed for the strong\(^*\) topology.
2. On the set of isometries, the weak and the strong topologies coincide. On \(U(H)\), all six operator topologies coincide.
3. The strong closure of \(U(H)\) is the set of all isometries.
4. If \(\dim H=\infty\), the weak closure of \(U(H)\) is the unit ball \(S\). In particular, it contains all projections and all partial isometries. If \(\dim H<\infty\), \(U(H)\) is compact.
5. \(U(H)\) is complete for the strong\(^*\) uniform structure: if \((u_i)\) is a net of unitaries such that \((u_i\xi)\) and \((u_i^*\xi)\) are Cauchy nets for every \(\xi\), then it converges strongly\(^*\) to a unitary. If \(\dim H=\infty\), \(U(H)\) is not complete for the strong uniform structure.
6. \(U(H)\) is relatively compact in the weak topology. If \(\dim H=\infty\), it is not weakly compact.
7. The weak closure of \(U(H)\) is closed under products and adjoints.

**Proof.** (1) Let \(u_i\to u\) strongly\(^*\) with \(u_i\) unitary. Then \(\|u\xi\|=\lim\|u_i\xi\|=\|\xi\|\) and \(\|u^*\xi\|=\lim\|u_i^*\xi\|=\|\xi\|\). So \(u\) and \(u^*\) are isometries, and \(u\) is unitary.

(2) Let \(v_i\to v\) weakly, where all \(v_i\) and \(v\) are isometries. Then
\[
\begin{gathered}
\|(v_i-v)\xi\|^2\\
=\|v_i\xi\|^2+\|v\xi\|^2-2\operatorname{Re}\langle v_i\xi,v\xi\rangle\\
=2\|\xi\|^2-2\operatorname{Re}\langle v_i\xi,v\xi\rangle\to2\|\xi\|^2-2\|v\xi\|^2\\
=0 .
\end{gathered}
\]
On \(U(H)\), strong convergence implies strong\(^*\) convergence (Corollary 2.4), and \(U(H)\) is bounded, so Lemma 1.1(3) adds the three \(\sigma\)-topologies.

(3) A strong limit of isometries is an isometry, since \(\|v\xi\|=\lim\|v_i\xi\|\). Conversely, let \(v\) be an isometry and \(F\subseteq H\) a finite-dimensional subspace. Put \(F'=F+vF\). The map \(v|_F\) is a linear isometry of \(F\) onto \(vF\), and \(F'\ominus F\) and \(F'\ominus vF\) have the same finite dimension \(\dim F'-\dim F\). Extending \(v|_F\) by a unitary map of \(F'\ominus F\) onto \(F'\ominus vF\) gives a unitary \(W\) of \(F'\). Let \(u_F\) be \(W\) on \(F'\) and \(1\) on \(F'^\perp\). Then \(u_F\) is unitary and \(u_F=v\) on \(F\). Directed by inclusion, \(u_F\to v\) strongly: for \(\xi\in F_0\) and \(F\supseteq F_0\), \(u_F\xi=v\xi\).

(4) Let \(\dim H=\infty\) and \(x\in S\). Let \(F\) be a finite-dimensional subspace and \(c=P_Fx|_F\), a contraction on \(F\), where \(P_F\) is the projection onto \(F\). Since \(F^\perp\) is infinite-dimensional, it contains a subspace \(E\) with an isometry \(J\) of \(F\) onto \(E\). Put \(D=(1-c^*c)^{1/2}\) and \(D_*=(1-cc^*)^{1/2}\), operators on \(F\), and define \(u\) by
\[
\begin{gathered}
u(\xi+J\eta+\zeta)\\
=\big(c\xi+D_*\eta\big)+J\big(D\xi-c^*\eta\big)+\zeta\\
(\xi,\eta\in F,\ \zeta\perp F\oplus E).
\end{gathered}
\]
On \(F\oplus E\), identified with \(F\oplus F\), \(u\) is the block matrix \(W=\begin{pmatrix}c&D_*\\D&-c^*\end{pmatrix}\). The relations \(cD=D_*c\) and \(c^*D_*=Dc^*\) hold, because \(cq(c^*c)=q(cc^*)c\) for every polynomial \(q\), and hence for every continuous function in place of \(q\). With them,
\[
\begin{gathered}
W^*W\\
=\begin{pmatrix}c^*c+D^2&c^*D_*-Dc^*\\D_*c-cD&D_*^2+cc^*\end{pmatrix}\\
=1,\\
WW^*\\
=\begin{pmatrix}cc^*+D_*^2&cD-D_*c\\Dc^*-c^*D_*&D^2+c^*c\end{pmatrix}\\
=1 .
\end{gathered}
\]
So \(u\) is unitary, and \(P_FuP_F=c=P_FxP_F\). Hence \(\langle u\xi,\eta\rangle=\langle x\xi,\eta\rangle\) for all \(\xi,\eta\in F\). Every weak neighbourhood of \(x\) is determined by finitely many vectors, and \(F\) can be chosen to contain them, so \(x\) lies in the weak closure of \(U(H)\). Conversely, the weak closure lies in \(S\), which is weakly closed (Lemma 1.2). If \(\dim H<\infty\), \(U(H)\) is closed and bounded in the finite-dimensional space \(B(H)\).

(5) If \((u_i\xi)\) and \((u_i^*\xi)\) are Cauchy for every \(\xi\), let \(x\xi\) and \(y\xi\) be their limits. Then \(x\) and \(y\) are linear with norm at most \(1\), and \(\langle x\xi,\eta\rangle=\lim\langle\xi,u_i^*\eta\rangle=\langle\xi,y\eta\rangle\), so \(y=x^*\). Thus \(u_i\to x\) strongly\(^*\), and \(x\) is unitary by (1). If \(\dim H=\infty\), the sequence \((u_n)\) of Example 2.5 converges strongly in \(B(H)\), so it is Cauchy for the strong uniform structure; its only possible limit is the non-unitary isometry \(v\).

(6) The map \(x\mapsto(\langle x\xi,\eta\rangle)_{\xi,\eta}\), over pairs of unit vectors, identifies \(S\) with its image in the product of closed unit discs, and the weak topology with the product topology. The image is closed, because a pointwise limit of bounded sesquilinear forms of norm at most \(1\) is again such a form and so comes from an operator in \(S\). By Tychonoff's theorem, \(S\) is weakly compact, so \(U(H)\subseteq S\) is relatively compact. If \(\dim H=\infty\), \(U(H)\) is not weakly closed by (4), so it is not weakly compact.

(7) If \(\dim H=\infty\), the weak closure is \(S\) by (4). If \(\dim H<\infty\), it is \(U(H)\) itself. \(\square\)

The next result describes which positive contractions are products of two projections, a question that arises when one tries to reach all of \(S\) from projections and unitaries by products.

**Proposition 8.2** (products of two projections). Let \(0\le h\le1\), and let \(R\) be the closure of the range of \(h-h^2\). The following are equivalent.

1. \(h=efe\) for two projections \(e\) and \(f\).
2. There is a linear isometry of \(R\) into \(\ker h\).

Condition (2) holds, for example, if \(H\) is separable and \(\ker h\) is infinite-dimensional, or if \(\ker h\) contains a closed subspace isometric to \(H\).

**Proof.** Let \(E\) be the closure of the range of \(h\); then \(\ker h=E^\perp\), and \(R\subseteq E\). Write \(T\) for the restriction of \(h\) to \(E\). Since \(h-h^2\) vanishes on \(\ker h\), \(R\) is also the closure of the range of \(T-T^2\).

(2)\(\Rightarrow\)(1). Let \(V_0:R\to\ker h\) be a linear isometry, and let \(V:E\to\ker h\) be \(V_0\) on \(R\) and \(0\) on \(E\ominus R\). Then \(V^*V=P_R\), the projection of \(E\) onto \(R\), which commutes with \(T\), and \((T-T^2)^{1/2}P_R=(T-T^2)^{1/2}\). With respect to \(H=E\oplus\ker h\) define
\[
\begin{gathered}
f\\
=\begin{pmatrix}T&(T-T^2)^{1/2}V^*\\V(T-T^2)^{1/2}&V(1-T)V^*\end{pmatrix},\\
e\\
=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\end{gathered}
\]
Clearly \(f=f^*\) and \(efe=h\). To see \(f^2=f\), write \(B=(T-T^2)^{1/2}V^*\) and \(D=V(1-T)V^*\). Then \[
\begin{gathered}
T^2+BB^*\\
=T^2+(T-T^2)^{1/2}P_R(T-T^2)^{1/2}\\
=T;
\end{gathered}
\] \[
\begin{gathered}
TB+BD\\
=\big(T+(1-T)\big)(T-T^2)^{1/2}V^*\\
=B,
\end{gathered}
\] using \(V^*V=P_R\); and \[
\begin{gathered}
B^*B+D^2\\
=V\big((T-T^2)+(1-T)^2\big)V^*\\
=V(1-T)V^*\\
=D.
\end{gathered}
\]

(1)\(\Rightarrow\)(2). Let \(h=efe\), and put \(E'=eH\). The range of \(h\) lies in \(E'\), so \(E\subseteq E'\) and \(E'^\perp\subseteq\ker h\). Let \(T'\) be the restriction of \(h\) to \(E'\) and \(B'=ef(1-e)\), viewed as an operator from \(E'^\perp\) to \(E'\). The corner of \(f^2=f\) on \(E'\) gives \(T'^2+B'B'^*=T'\), so \(B'B'^*=T'-T'^2\). Define \(V\) on the range of \((T'-T'^2)^{1/2}\) by \(V\big((T'-T'^2)^{1/2}\xi\big)=B'^*\xi\). It is well defined and isometric, since \(\|B'^*\xi\|^2=\langle B'B'^*\xi,\xi\rangle=\|(T'-T'^2)^{1/2}\xi\|^2\). It extends to an isometry from the closure of that range, which is \(R\), into \(E'^\perp\subseteq\ker h\).

For the last statement: if \(H\) is separable, then \(R\) and \(\ker h\) have orthonormal bases that are finite or countable, the second one infinite, and mapping the first basis into the second gives an isometry. If there is an isometry of \(H\) into \(\ker h\), restrict it to \(R\). \(\square\)

**Example 8.3** (an infinite-dimensional kernel is not enough). Let \(K\) be a nonseparable Hilbert space, for instance \(\ell^2(\Gamma)\) for an uncountable set \(\Gamma\), let \(N\) be a separable infinite-dimensional Hilbert space, and let \(h=\frac12\cdot1_K\oplus0_N\) on \(H=K\oplus N\). Then \(0\le h\le1\), and \(\ker h=N\) is infinite-dimensional. But \(h-h^2=\frac14\cdot1_K\oplus0\), so \(R=K\) is nonseparable. An isometric image of a nonseparable space is nonseparable, while every subset of the separable space \(N\) is separable. So there is no isometry of \(R\) into \(\ker h\), and \(h\) is not a product \(efe\) of two projections.

Proposition 8.2 proves the exact dimension criterion; Example 8.3 proves directly that infinite-dimensional null space alone does not suffice on a nonseparable space.

In finite dimensions, Proposition 8.2 says that \(h=efe\) exactly when the rank of \(h-h^2\) is at most \(\dim\ker h\). For example, \(\operatorname{diag}(\frac12,0)\) on \(\mathbb C^2\) equals \(efe\) with \(e=\operatorname{diag}(1,0)\) and \(f\) the projection onto \(\mathbb C(1,1)\), while \(\frac12\) on \(\mathbb C\) is not a product of two projections of \(\mathbb C\).

## 9. Density of unitary groups

**Theorem 9.1** (density of unitary groups). Let \(A\) be a concrete C\(^*\)-algebra on \(H\) with \(1\in A\), and let \(M=A''\), its weak closure. For \(\lambda>0\) put
\[
\begin{gathered}
U(A,\lambda)\\
=\{u\in U(A):\|u-1\|\le\lambda\},\\
U(M,\lambda)\\
=\{u\in U(M):\|u-1\|\le\lambda\}.
\end{gathered}
\]
Then \(U(M,\lambda)\) is the strong\(^*\) closure of \(U(A,\lambda)\). In particular, \(U(A)\) is strongly\(^*\) dense in \(U(M)\).


**Proof.** *\(U(M,\lambda)\) is strongly\(^*\) closed.* It is the intersection of \(U(H)\), which is strongly\(^*\) closed (Theorem 8.1(1)), with \(M\), which is strongly closed, and with the ball \(\{x:\|x-1\|\le\lambda\}\), which is strongly closed (Lemma 1.2). It contains \(U(A,\lambda)\), hence its strong\(^*\) closure.

*Density.* Let \(u\in U(M,\lambda)\). Put \(\alpha=2\arcsin(\min(\lambda,2)/2)\in(0,\pi]\). There is a self-adjoint \(h\in M\) with \(\|h\|\le\alpha\) and \(u=\exp(ih)\): if \(\lambda<2\) use Corollary 4.5(2), noting \(2\arcsin(\|u-1\|/2)\le\alpha\); if \(\lambda\ge2\), then \(\alpha=\pi\) and Corollary 4.5(1) applies. By Kaplansky's density theorem 7.1(2), applied to \(h/\alpha\), there is a net \((h_i)\) in \(A_h\) with \(\|h_i\|\le\alpha\) and \(h_i\to h\) strongly. The unitaries \(u_i=\exp(ih_i)\) lie in \(A\), because \(A\) is a unital C\(^*\)-algebra. They satisfy
\[
\begin{gathered}
\|u_i-1\|\\
=\max_{t\in\sigma(h_i)}|e^{it}-1|\\
\le\max_{|t|\le\alpha}2|\sin(t/2)|\\
=2\sin(\alpha/2)\\
=\min(\lambda,2)\\
\le\lambda,
\end{gathered}
\]
so \(u_i\in U(A,\lambda)\). The function \(t\mapsto e^{it}\) is bounded and continuous, so \(u_i\to\exp(ih)=u\) strongly by Corollary 5.3(4), and strongly\(^*\) by Corollary 2.4. \(\square\)

**Remark 9.2** (strong density ignores topological obstructions). The proof approximates every unitary of \(M\) by exponentials \(\exp(ih)\) with \(h\in A_h\). In norm this is impossible in general. Let \(A\) be the algebra of multiplication operators by continuous functions on \(L^2(\mathbb T)\), for the normalized arc-length measure, which is isometrically isomorphic to \(C(\mathbb T)\). The unitary \(u\) of multiplication by \(z\) lies in \(A\). Every \(\exp(ih)\) with \(h\in A_h\) lies in the connected component of \(1\) in the invertible group of \(A\). This component is closed in the invertible group, and the invertible element \(u\) does not lie in it ([Example 7.2 of the lesson on Banach algebras](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-14)). So \(u\) is not a norm limit of such exponentials. It is a strong limit of them. Let \(h_k\in A_h\) be multiplication by the real continuous function \(\varphi_k\) on \(\mathbb T\) from the proof of Corollary 4.5. Then \(\exp(ih_k)\) is multiplication by \(e^{i\varphi_k}\), and \(e^{i\varphi_k(\lambda)}\to e^{i\arg\lambda}=\lambda\) at every point, so \(\exp(ih_k)\to u\) strongly by dominated convergence.

## 10. Approximation on large projections: the noncommutative Egoroff and Lusin theorems

Egoroff's theorem turns almost everywhere convergence into uniform convergence off a small set, and Lusin's theorem makes a measurable function continuous off a small set. In a von Neumann algebra, "off a small set" becomes "on a projection \(f\le e\) with \(\varphi(e-f)\) small", where \(\varphi\) is a positive normal functional and \(e\) a given projection. Throughout this section \(M\) denotes a von Neumann algebra on \(H\), and in Corollary 10.4 and Theorem 10.6, \(A\) is a concrete C\(^*\)-algebra acting nondegenerately on \(H\), with \(M=A''\). For a degenerate \(A\) one restricts to \([AH]\), where \(A\) acts nondegenerately and its weak closure is its bicommutant ([the double commutant theorem, Step 3](the-double-commutant-theorem.md#oa-fnd-bi-07)).

**Lemma 10.1** (cutting down a null net). Let \(e\in M\) be a projection and \((x_i)\) a bounded net in \(M\) with \(x_ie\to0\) strongly, and let \(\varepsilon>0\). Then there are projections \(e_i\le e\) in \(M\) with \(e_i\to e\) strongly and \(\|x_ie_i\|\le\varepsilon\) for every \(i\).

**Proof.** Let \(c=\sup_i\|x_i\|\) and \(y_i=ex_i^*x_ie\in M_+\). Then \(y_i=ey_ie\), and \(\|y_i\xi\|\le c\|x_ie\xi\|\to0\), so \(y_i\to0\) strongly. Let \(p_i=1_{(\varepsilon^2,\infty)}(y_i)\). By Corollary 4.3, \(p_i\) is a projection in \(M\) that commutes with \(y_i\) and with \(e\), \(p_i\le e\), and \(\varepsilon^2p_i\le y_ip_i\le y_i\), the last because \(y_i(1-p_i)=(1-p_i)y_i(1-p_i)\ge0\). So \(\varepsilon^2\|p_i\xi\|^2\le\langle y_i\xi,\xi\rangle\to0\), and \(p_i\to0\) strongly. Put \(e_i=e-p_i\), a projection with \(e_i\to e\) strongly. Since \(e_i\le1-p_i\) and \(y_i(1-p_i)\le\varepsilon^2(1-p_i)\) (Corollary 4.3(2)),
\[
\begin{gathered}
\|x_ie_i\|^2\\
=\|e_iy_ie_i\|\\
=\|e_iy_i(1-p_i)e_i\|\\
\le\varepsilon^2\|e_i(1-p_i)e_i\|\\
\le\varepsilon^2 .\\
\square
\end{gathered}
\]

**Theorem 10.2** (noncommutative Egoroff theorem). Let \(B\subseteq M\) be a bounded set, \(x\) an element of its strong closure, \(\varphi\in M_*^+\), \(e\in M\) a projection and \(\varepsilon>0\). Then there are a projection \(f\le e\) in \(M\) and a sequence \((b_k)\) in \(B\) with
\[
\begin{gathered}
\lim_{k\to\infty}\|(b_k-x)f\|\\
=0\\
\text{and}\\
\varphi(e-f)<\varepsilon .
\end{gathered}
\]

**Proof.** Choose a net \((b_i)_{i\in I}\) in \(B\) with \(b_i\to x\) strongly, and put \(d_i=b_i-x\), a bounded net with \(d_i\to0\) strongly. We choose indices \(i_1\le i_2\le\cdots\) and projections \(e=f_0\ge f_1\ge f_2\ge\cdots\) in \(M\) with
\[
\begin{gathered}
\|d_{i_k}f_k\|\\
\le2^{-k}\\
\text{and}\\
\varphi(f_{k-1}-f_k)<2^{-k}\varepsilon .
\end{gathered}
\tag{10.1}
\]
Suppose \(i_1,\dots,i_{k-1}\) and \(f_0,\dots,f_{k-1}\) are chosen (for \(k=1\), let \(i_0\) be any index). The net \((d_if_{k-1})_{i\ge i_{k-1}}\) is bounded and tends to \(0\) strongly. Lemma 10.1, with the projection \(f_{k-1}\), gives projections \(g_i\le f_{k-1}\) with \(g_i\to f_{k-1}\) strongly and \(\|d_ig_i\|=\|d_if_{k-1}g_i\|\le2^{-k}\). The bounded net \((f_{k-1}-g_i)\) tends to \(0\) strongly and \(\varphi\) is normal, so \(\varphi(f_{k-1}-g_i)\to0\) (Lemma 1.1(3)). Choose \(i_k\ge i_{k-1}\) with \(\varphi(f_{k-1}-g_{i_k})<2^{-k}\varepsilon\), and put \(f_k=g_{i_k}\).

Let \(f\) be the strong limit of the decreasing sequence \((f_k)\), a projection in \(M\) with \(f\le e\) (Corollary 1.4). By normality, \(\varphi(e-f)=\sum_k\varphi(f_{k-1}-f_k)<\varepsilon\). For each \(k\), \(f=f_kf\), so \(\|(b_{i_k}-x)f\|=\|d_{i_k}f_kf\|\le2^{-k}\). The sequence \(b_k=b_{i_k}\) has the required property. \(\square\)

The construction needs care at one point. At step \(k\) the projection \(f_k\) is chosen for the single index \(i_k\), and nothing is claimed about \(\|d_if_k\|\) for other indices \(i\ge i_k\); in general that norm stays large. For example, on \(\ell^2(\mathbb N)\) the operators \(d_m=\theta_{\delta_1,\delta_m}\) tend to \(0\) strongly, and \(\|d_mf\|=\|f\delta_m\|\) for every projection \(f\). For \(\varphi=\omega_{\delta_1}\) and \(f=1-\theta_{\delta_2,\delta_2}\) we have \(\varphi(1-f)=0\), yet \(\|d_mf\|=1\) for every \(m\ne2\). The theorem only claims, and the proof only gives, convergence along a diagonal sequence.

To control the norms of the approximants, we need to complete a column to a self-adjoint operator without increasing the norm.

**Lemma 10.3** (self-adjoint completion). Let \(a\in M\) be self-adjoint, \(e\in M\) a projection and \(c=\|ae\|\). There is a self-adjoint \(b\in M\) with \(be=ae\) and \(\|b\|=c\).

The proof below gives the required norm-preserving completion explicitly.

**Proof.** If \(c=0\), take \(b=0\). Otherwise put \(P=eae\) and \(Q=(1-e)ae\). Then \[
\begin{gathered}
P^2+Q^*Q\\
=ea(e+1-e)ae\\
=(ae)^*(ae)\\
\le c^2e.
\end{gathered}
\] So \(c^2e-P^2\ge Q^*Q\ge0\), and we let \(D=(c^2e-P^2)^{1/2}\in M\). It satisfies \(D=eDe\), and it commutes with \(P\).

*A contraction \(K\in M\) with \(Q=KD\).* Define \(K\) on the range of \(D\) by \(K(D\xi)=Q\xi\). This is well defined and contractive, because \(\|Q\xi\|^2=\langle Q^*Q\xi,\xi\rangle\le\langle D^2\xi,\xi\rangle=\|D\xi\|^2\). Extend \(K\) by continuity to the closure of the range of \(D\), and by \(0\) on its orthogonal complement \(\ker D\). Then \(Q=KD\) and \(\|K\|\le1\). For a unitary \(v\in M'\), \(v\) commutes with \(D\) and \(Q\), so \[
\begin{gathered}
vKv^*(D\xi)\\
=vKDv^*\xi\\
=vQv^*\xi\\
=Q\xi\\
=K(D\xi),
\end{gathered}
\] and \(vKv^*\) vanishes on \(\ker D\), which \(v\) maps onto itself. So \(vKv^*=K\). The unitaries of \(M'\) span \(M'\) ([unitaries span a unital C\*-algebra](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-10)), so \(K\in M''=M\). Since \(\ker D\supseteq(1-e)H\) and the range of \(K\) lies in the closure of the range of \(Q\), \(K=(1-e)Ke\).

*The completion.* Put \(b=P+KD+DK^*-KPK^*\). Then \(b=b^*\). Since \(K^*e=0\), \(be=P+KD=eae+(1-e)ae=ae\). For the norm, let \(J=\begin{pmatrix}P&D\\D&-P\end{pmatrix}\) on \(eH\oplus eH\). As \(P\) and \(D\) commute, \(J^2=(P^2+D^2)\oplus(P^2+D^2)=c^2e\oplus c^2e\), so \(\|J\|=c\). Let \(W:eH\oplus eH\to H\), \(W(\xi,\eta)=\xi+K\eta\). Since \(\xi\perp K\eta\), \(\|W(\xi,\eta)\|^2=\|\xi\|^2+\|K\eta\|^2\le\|\xi\|^2+\|\eta\|^2\), so \(\|W\|\le1\), and \(W^*\zeta=(e\zeta,K^*\zeta)\). A direct computation gives \[
\begin{gathered}
WJW^*\zeta\\
=Pe\zeta+DK^*\zeta+KDe\zeta-KPK^*\zeta\\
=b\zeta.
\end{gathered}
\] Hence \(\|b\|\le\|J\|=c\), and \(\|b\|\ge\|be\|=c\). \(\square\)

**Corollary 10.4** (approximation with norm control). Let \(\varphi\in M_*^+\), \(e\in M\) a projection, \(\varepsilon>0\) and \(\delta>0\).

1. For every \(x\in M\) there are \(a\in A\) and a projection \(f\le e\) in \(M\) with \(\|(x-a)f\|<\delta\), \(\|a\|\le\|xe\|\) and \(\varphi(e-f)<\varepsilon\).
2. If \(x\) is self-adjoint, \(a\) can be chosen self-adjoint, with the same three properties.
3. If \(1\in A\) and \(x\in U(M)\), \(a\) can be chosen in \(U(A)\) with \(\|(x-a)f\|<\delta\), \(\|a-1\|\le\|x-1\|\) and \(\varphi(e-f)<\varepsilon\).

**Proof.** In each case we apply Theorem 10.2 to a bounded set \(B\) and an element \(y\) of its strong closure with \(ye=xe\). Then \((b_k-y)f=(b_k-y)ef=(b_k-x)f\), and we take \(a=b_k\) for large \(k\).

(1) Let \(y=xe\) and \(B=A\cap\|xe\|S\). By Kaplansky's density theorem 7.1(1), \(y\) lies in the strong closure of \(B\).

(2) Let \(y\) be the self-adjoint completion of Lemma 10.3, with \(ye=xe\) and \(\|y\|=\|xe\|\), and \(B=A_h\cap\|xe\|S\). By Theorem 7.1(2), \(y\) lies in the strong closure of \(B\).

(3) Let \(y=x\) and \(B=U(A,\|x-1\|)\). By Theorem 9.1, \(x\) lies in its strong closure. \(\square\)

**Lemma 10.5** (correcting a unitary). Let \(w\in U(M)\) and let \(e\in M\) be a projection with \(\|(1-w)e\|\le\frac18\). There is \(v\in U(M)\) with \(ve=we\) and \(\|1-v\|\le6\|(1-w)e\|\).

**Proof.** If \(e=0\), take \(v=1\); if \(e=1\), take \(v=w\). Suppose otherwise. Put \(\delta=\|(1-w)e\|\) and \(f=wew^*\), a projection in \(M\) with \(fw=we\). Since \(e-f=(1-w)e+we(1-w^*)\) and \(\|e(1-w^*)\|=\delta\), we get \(\theta:=\|e-f\|\le2\delta\le\frac14\).

*A unitary map of \((1-e)H\) onto \((1-f)H\).* Let \(T=(1-f)(1-e)\in M\). Writing \(1-f=(1-e)-(f-e)\),
\[
\begin{gathered}
T^*T\\
=(1-e)(1-f)(1-e)\\
=(1-e)-(1-e)(f-e)(1-e)\\
\ge(1-\theta)(1-e),
\end{gathered}
\]
and in the same way \(TT^*\ge(1-\theta)(1-f)\). In the von Neumann algebra \((1-e)M(1-e)\) with unit \(1-e\), \(|T|=(T^*T)^{1/2}\) is invertible; let \(|T|^{-1}\) be its inverse there, extended by \(0\) on \(eH\). Put \(U=T|T|^{-1}\in M\). Then \(U^*U=|T|^{-1}T^*T|T|^{-1}=1-e\), so \(UU^*\) is a projection, the projection onto the range of \(U\), which equals the range of \(T\). That range lies in \((1-f)H\), and it contains the range of \(TT^*\), which is \((1-f)H\) because \(TT^*\) is invertible on \((1-f)H\). So \(UU^*=1-f\).

*\(U\) is close to \(1-e\).* On \((1-e)H\), \(T=(1-e)-(f-e)(1-e)\), so
\[
\begin{gathered}
U-(1-e)\\
=(1-e)\big(|T|^{-1}-(1-e)\big)\\
-(f-e)(1-e)|T|^{-1}.
\end{gathered}
\]
The spectrum of \(|T|^2\) in \((1-e)M(1-e)\) lies in \([1-\theta,1+\theta]\), and for \(|s|\le\theta\le\frac14\) we have \(|(1+s)^{-1/2}-1|\le\theta\) and \((1+s)^{-1/2}\le(1-\theta)^{-1/2}\le\frac2{\sqrt3}\). So \(\|U-(1-e)\|\le\theta+\frac2{\sqrt3}\theta\le2.2\,\theta\le4.4\,\delta\).

*The unitary \(v\).* Put \(v=we+U\). Then \(ve=we\), because \(Ue=0\). Next, \(U^*we=|T|^{-1}(1-e)(1-f)fw=0\) and \(eU^*=0\), so the cross terms in \(v^*v\) and \(vv^*\) vanish. Hence \(v^*v=ew^*we+U^*U=e+(1-e)=1\) and \(vv^*=wew^*+UU^*=f+(1-f)=1\). Finally \(1-v=(1-w)e+\big((1-e)-U\big)\), so \(\|1-v\|\le\delta+4.4\,\delta<6\delta\). \(\square\)

**Theorem 10.6** (noncommutative Lusin theorem). Let \(\varphi\in M_*^+\), \(e\in M\) a projection, \(\varepsilon>0\) and \(\delta>0\).

1. For every \(x\in M\) there are \(a\in A\) and a projection \(f\le e\) in \(M\) with \(xf=af\), \(\varphi(e-f)<\varepsilon\) and \(\|a\|\le(1+\delta)\|xf\|\).
2. If \(x\) is self-adjoint, \(a\) can be chosen self-adjoint, with the same properties.
3. If \(1\in A\) and \(x\in U(M)\), there are \(a\in U(A)\) and a projection \(f\le e\) in \(M\) with \(xf=af\), \(\varphi(e-f)<\varepsilon\) and \(\|a-1\|\le\|x-1\|+\delta\).

**Proof.** (1) and (2). If \(xe=0\), take \(a=0\) and \(f=e\). Otherwise, replacing \(x\) by \(x/\|xe\|\), we may assume \(\|xe\|=1\). Choose \(\delta'\in(0,\frac14)\) with \((1+\delta')/(1-2\delta')\le1+\delta\). Choose a unit vector \(\zeta\in eH\) with \(\|x\zeta\|^2\ge1-\delta'\), and put \(\psi=\varphi+\omega_\zeta\in M_*^+\) and \(\varepsilon'=\min(\varepsilon,\delta'^2)\).

We choose elements \(a_1,a_2,\dots\) of \(A\), self-adjoint in case (2), and projections \(e=f_0\ge f_1\ge f_2\ge\cdots\) in \(M\). Suppose \(a_1,\dots,a_{k-1}\) and \(f_0,\dots,f_{k-1}\) are chosen, and let \(x_{k-1}=x-\sum_{j<k}a_j\), which is self-adjoint in case (2). Corollary 10.4, part (1) or (2), applied to \(x_{k-1}\), the projection \(f_{k-1}\), the functional \(\psi\) and the numbers \(2^{-k}\varepsilon'\) and \(2^{-k}\delta'\), gives \(a_k\) and \(f_k\le f_{k-1}\) with
\[
\begin{gathered}
\|x_kf_k\|<2^{-k}\delta',\\
\|a_k\|\\
\le\|x_{k-1}f_{k-1}\|,\\
\psi(f_{k-1}-f_k)<2^{-k}\varepsilon',
\end{gathered}
\tag{10.2}
\]
where \(x_k=x_{k-1}-a_k\), since \((x_{k-1}-a_k)f_k=x_kf_k\).

By (10.2), \(\|a_1\|\le\|xe\|=1\) and \(\|a_k\|<2^{-k+1}\delta'\) for \(k\ge2\). So \(a=\sum_ka_k\) converges in norm, \(a\in A\), and \(\|a\|\le1+\delta'\); \(a\) is self-adjoint in case (2). Let \(f\) be the strong limit of the decreasing sequence \((f_k)\). Then \(f\le e\) is a projection in \(M\), and by normality \(\psi(e-f)<\varepsilon'\), so \(\varphi(e-f)<\varepsilon\). Since \(f=f_kf\), \(\|(x-\sum_{j\le k}a_j)f\|=\|x_kf_kf\|<2^{-k}\delta'\); letting \(k\to\infty\) gives \(xf=af\).

It remains to bound \(\|xf\|\) from below. We have \(\omega_\zeta(e-f)=\|(e-f)\zeta\|^2<\delta'^2\), and \(\|x(e-f)\|=\|xe(e-f)\|\le1\). Since \(\zeta=e\zeta\),
\[
\begin{gathered}
\|xf\|\\
\ge\|xf\zeta\|\\
=\|x\zeta-x(e-f)\zeta\|\\
\ge(1-\delta')^{1/2}-\delta'\\
\ge1-2\delta' .
\end{gathered}
\]
Hence \(\|a\|\le1+\delta'\le\frac{1+\delta'}{1-2\delta'}\|xf\|\le(1+\delta)\|xf\|\).

(3) We may assume \(\delta\le1\). Put \(w_1=x\) and \(f_1=e\). We choose \(u_k\in U(A)\), \(w_{k+1}\in U(M)\) and projections \(f_{k+1}\le f_k\) in \(M\), for \(k=1,2,\dots\), with
\[
\begin{gathered}
xf_{k+1}\\
=u_1u_2\cdots u_k\,w_{k+1}f_{k+1},\\
\|1-u_k\|\\
\le\|1-w_k\|,\\
\|1-w_{k+1}\|\\
\le2^{-k}\delta,\\
\varphi(f_k-f_{k+1})<2^{-k}\varepsilon .
\end{gathered}
\tag{10.3}
\]
Given \(w_k\) and \(f_k\) with \(xf_k=u_1\cdots u_{k-1}w_kf_k\) (for \(k=1\) this reads \(xe=w_1e\)), Corollary 10.4(3) gives \(u_k\in U(A)\) and \(f_{k+1}\le f_k\) with \(\|(w_k-u_k)f_{k+1}\|<2^{-k-3}\delta\), \(\|1-u_k\|\le\|1-w_k\|\) and \(\varphi(f_k-f_{k+1})<2^{-k}\varepsilon\). The unitary \(u_k^*w_k\in U(M)\) satisfies \[
\begin{gathered}
\|(1-u_k^*w_k)f_{k+1}\|\\
=\|(u_k-w_k)f_{k+1}\|<2^{-k-3}\delta\\
\le\frac18.
\end{gathered}
\] Lemma 10.5 gives \(w_{k+1}\in U(M)\) with \(w_{k+1}f_{k+1}=u_k^*w_kf_{k+1}\) and \(\|1-w_{k+1}\|\le6\cdot2^{-k-3}\delta<2^{-k}\delta\). Then
\[
\begin{gathered}
xf_{k+1}\\
=xf_kf_{k+1}\\
=u_1\cdots u_{k-1}w_kf_{k+1}\\
=u_1\cdots u_{k-1}u_k\,(u_k^*w_kf_{k+1})\\
=u_1\cdots u_k\,w_{k+1}f_{k+1},
\end{gathered}
\]
which completes the step.

By (10.3), \(\|1-u_1\|\le\|1-x\|\) and \(\|1-u_k\|\le\|1-w_k\|<2^{-k+1}\delta\) for \(k\ge2\). Let \(v_k=u_1\cdots u_k\). Then \(\|v_{k+1}-v_k\|=\|v_k(u_{k+1}-1)\|=\|u_{k+1}-1\|\), so \((v_k)\) converges in norm to a unitary \(a\in A\). From \[
\begin{gathered}
1-v_k\\
=(1-u_1)+u_1(1-u_2)\\
+\dots+u_1\cdots u_{k-1}(1-u_k)
\end{gathered}
\] we get \(\|1-a\|\le\sum_k\|1-u_k\|\le\|1-x\|+\delta\). Let \(f\) be the strong limit of \((f_k)\), so \(f\le e\) and \(\varphi(e-f)<\varepsilon\). Multiplying (10.3) by \(f\) on the right, \(xf=v_kw_{k+1}f\), so
\[
\begin{gathered}
\|xf-af\|\\
\le\|v_k(w_{k+1}-1)f\|+\|(v_k-a)f\|\\
\le2^{-k}\delta+\|v_k-a\|\to0 ,
\end{gathered}
\]
and \(xf=af\). \(\square\)

**Example 10.7** (the commutative case). Let \(\mu\) be Lebesgue measure on \([0,1]\), \(M\) the algebra of multiplication operators \(m_g\) by bounded measurable \(g\) on \(L^2[0,1]\), \(A\) the multiplication operators by continuous functions, and \(\varphi(m_g)=\int g\,d\mu\), the vector functional of the constant function \(1\). The projections of \(M\) are the operators \(m_{1_E}\), and \(\varphi(1-m_{1_E})=\mu([0,1]\setminus E)\). A bounded sequence \(g_k\to g\) almost everywhere gives \(m_{g_k}\to m_g\) strongly, by dominated convergence. Theorem 10.2 then yields a set \(E\) with small complement on which a sequence of the \(g_k\) converges uniformly, up to a null set: a form of Egoroff's theorem. Theorem 10.6(1) yields a continuous \(a\) that agrees with a bounded measurable \(g\) almost everywhere on a set \(E\) with small complement, with \(\max|a|\le(1+\delta)\operatorname{ess\,sup}_E|g|\): this is Lusin's theorem with control of the norm. (That \(M\) is the weak closure of \(A\) is shown in Exercise 14.2.)

## 11. Kadison's transitivity theorem

A concrete C\(^*\)-algebra \(A\) on \(H\) is *irreducible* if \(A\ne\{0\}\) and the only closed subspaces of \(H\) that are invariant under \(A\) are \(\{0\}\) and \(H\).

**Theorem 11.1** (Kadison's transitivity theorem). Let \(A\) be an irreducible concrete C\(^*\)-algebra on \(H\), let \(e\) be a projection of finite rank on \(H\), and let \(\varepsilon>0\).

1. For every \(b\in B(H)\) there is \(a\in A\) with \(ae=be\) and \(\|a\|\le(1+\varepsilon)\|be\|\). In particular \(Ae=B(H)e\).
2. If \(b\) is self-adjoint, \(a\) can be chosen self-adjoint with \(ae=be\) and \(\|a\|\le(1+\varepsilon)\|be\|\).
3. If \(b\ge0\), \(a\) can be chosen with \(a\ge0\), \(ae=be\) and \(\|a\|\le(1+\varepsilon)\|b\|\).
4. For every unitary \(u\in B(H)\) there is a unitary \(v\) in the C\(^*\)-algebra \(A+\mathbb C1\) with \(ve=ue\) and \(\|v-1\|\le\|u-1\|+\varepsilon\).


**Proof.** *The weak closure is \(B(H)\).* The closed subspace \([AH]\) is invariant and not \(\{0\}\), because \(A\ne\{0\}\); so \(A\) is nondegenerate. A projection in \(A'\) is the projection onto a closed invariant subspace ([Proposition 2.1(5) of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-02)), so the only projections of the von Neumann algebra \(A'\) are \(0\) and \(1\). By Corollary 4.4, \(A'=\mathbb C1\), so \(A''=B(H)\), and \(B(H)\) is the weak closure of \(A\).

*A normal functional that detects \(e\).* Let \(\varepsilon_1,\dots,\varepsilon_r\) be an orthonormal basis of \(eH\) and \(\varphi(y)=\sum_{j=1}^r\langle y\varepsilon_j,\varepsilon_j\rangle\), the trace of \(eye\). It is a positive normal functional on \(B(H)\). For a projection \(f\le e\), \(\varphi(e-f)\) is the rank of \(e-f\), an integer. So \(\varphi(e-f)<\frac12\) forces \(f=e\).

(1) and (2). Apply Theorem 10.6(1), respectively (2), to \(x=b\), \(M=B(H)\), the projection \(e\) and the functional \(\varphi\), with \(\frac12\) in place of \(\varepsilon\) and \(\varepsilon\) in place of \(\delta\). The projection \(f\) it produces is \(e\), so \(ae=be\) and \(\|a\|\le(1+\varepsilon)\|be\|\).

(3) Let \(e'\) be the projection onto the finite-dimensional space \(eH+b^{1/2}eH\). Choose \(\varepsilon'>0\) with \((1+\varepsilon')^2\le1+\varepsilon\). By (2) there is a self-adjoint \(c\in A\) with \(ce'=b^{1/2}e'\) and \(\|c\|\le(1+\varepsilon')\|b^{1/2}\|\). Put \(a=c^2\ge0\). Since \(e\le e'\), \(ce=b^{1/2}e\), and since \(b^{1/2}e=e'b^{1/2}e\),
\[
ae=c\,b^{1/2}e=c\,e'b^{1/2}e=b^{1/2}e'b^{1/2}e=be .
\]
Also \(\|a\|=\|c\|^2\le(1+\varepsilon')^2\|b\|\le(1+\varepsilon)\|b\|\).

(4) \(A+\mathbb C1\) is a unital concrete C\(^*\)-algebra with weak closure \(B(H)\). Apply Theorem 10.6(3) to it, with \(x=u\), the same \(\varphi\), \(\frac12\) in place of \(\varepsilon\) and \(\varepsilon\) in place of \(\delta\). \(\square\)

**Corollary 11.2.** Let \(A\) be an irreducible concrete C\(^*\)-algebra on \(H\).

1. If \(\xi_1,\dots,\xi_n\in H\) are linearly independent and \(\eta_1,\dots,\eta_n\in H\) are arbitrary, there is \(a\in A\) with \(a\xi_j=\eta_j\) for all \(j\).
2. For every \(\xi\ne0\), \(A\xi=H\). So \(H\) has no subspaces invariant under \(A\) except \(\{0\}\) and \(H\), closed or not: \(A\) acts *algebraically irreducibly*.
3. Let \(\pi\) be a representation of a C\(^*\)-algebra \(B\) on \(H\) such that \(\pi(B)\) is irreducible. Then \(\pi(B)\xi=H\) for every nonzero \(\xi\in H\).

**Proof.** (1) Let \(e\) be the projection onto the span of the \(\xi_j\). By linear independence there is \(b\in B(H)\) with \(b\xi_j=\eta_j\) for all \(j\) and \(b=0\) on \((eH)^\perp\). Theorem 11.1(1) gives \(a\in A\) with \(ae=be\). (2) is (1) with \(n=1\). (3) The image of a C\(^*\)-algebra under a representation is norm closed ([ranges of \(*\)-homomorphisms](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-25)), so it is a concrete C\(^*\)-algebra; apply (2) to it. \(\square\)

**Example 11.3** (norm closedness is needed). Let \(s\) be the unilateral shift on \(\ell^2(\{0,1,2,\dots\})\), \(s\delta_m=\delta_{m+1}\), and let \(P\) be the \(*\)-algebra of polynomials in \(s\) and \(s^*\). Then \(1-ss^*=\theta_{\delta_0,\delta_0}\), and \(s^i(1-ss^*)s^{*j}=\theta_{\delta_i,\delta_j}\), so \(P\) contains all matrix units. If a closed subspace \(W\ne\{0\}\) is invariant under \(P\), pick \(w\in W\) and \(j\) with \(\langle w,\delta_j\rangle\ne0\); then \(\theta_{\delta_i,\delta_j}w=\langle w,\delta_j\rangle\delta_i\in W\) for all \(i\), so \(W\) is the whole space. Thus \(P\) is irreducible in the topological sense. But \(s\) and \(s^*\) map finitely supported vectors to finitely supported vectors, so \(P\delta_0\) consists of finitely supported vectors and is not the whole space. So the \(*\)-algebra \(P\) is not algebraically irreducible, while its norm closure is, by Corollary 11.2.

## 12. Monotone limits: the up-down and up-down-up theorems

Kaplansky's theorem approximates elements of \(A''\) by bounded nets from \(A\). This section approximates self-adjoint elements of \(A''\) in the order: by increasing and decreasing nets, applied in turn.

**Definition 12.1.** Let \(X\) be a set of self-adjoint operators on \(H\). Then \(X^{\nearrow}\) consists of all strong limits of increasing *sequences* in \(X\) that are bounded in norm, and \(X^{\searrow}\) of all strong limits of such decreasing sequences. The sets \(X^{\uparrow}\) and \(X^{\downarrow}\) are defined in the same way with *nets* in place of sequences. By Vigier's theorem 1.3 such limits exist, and they are least upper, respectively greatest lower, bounds.

**Lemma 12.2.** Let \(X,Y\) be sets of self-adjoint operators.

1. \(X\subseteq X^{\nearrow}\subseteq X^{\uparrow}\) and \(X\subseteq X^{\searrow}\subseteq X^{\downarrow}\). If \(X\subseteq Y\), then \(X^{\uparrow}\subseteq Y^{\uparrow}\), and likewise for the other three operations.
2. If \(X\) is convex, or closed under sums, or closed under multiplication by nonnegative numbers, then so are \(X^{\nearrow},X^{\searrow},X^{\uparrow},X^{\downarrow}\).
3. \(-(X^{\uparrow})=(-X)^{\downarrow}\) and \(-(X^{\nearrow})=(-X)^{\searrow}\). More generally, for the order-reversing map \(t\mapsto1-t\): \(1-X^{\uparrow}=(1-X)^{\downarrow}\) and \(1-X^{\nearrow}=(1-X)^{\searrow}\), and with the roles of increasing and decreasing exchanged.
4. Let \(X\subseteq B(H)_+\cap S\), and let \(g:[0,1]\to[0,1]\) be continuous and operator monotone on \([0,1]\) (Definition 12.3) with \(g(X)\subseteq X\). Then \(g(Y)\subseteq Y\) for \(Y\) each of \(X^{\nearrow},X^{\searrow},X^{\uparrow},X^{\downarrow}\).
5. If \(X\subseteq M_+\cap S\) for a von Neumann algebra \(M\), then \(X^{\nearrow},X^{\searrow},X^{\uparrow},X^{\downarrow}\subseteq M_+\cap S\).

**Proof.** (1) Use constant sequences, and note that a sequence is a net. (2) If \(x_i\uparrow x\) and \(y_j\uparrow y\) are increasing nets in \(X\), then for \(t\in[0,1]\) the net \(tx_i+(1-t)y_j\), indexed by pairs \((i,j)\) with the product order, is increasing in \(X\) and converges strongly to \(tx+(1-t)y\). Sums and nonnegative multiples are handled the same way. For sequences use the pairs \((m,m)\). (3) Negation and \(t\mapsto1-t\) reverse the order and preserve strong limits. (4) If \(x_i\uparrow x\) in \(X\), then \(g(x_i)\) is an increasing net in \(X\), and \(g(x_i)\to g(x)\) strongly by Corollary 5.3(1). So \(g(x)\in X^{\uparrow}\). The other cases are the same. (5) \(M\) is strongly closed, and so are \(B(H)_+\) and \(S\) (Lemma 1.2). \(\square\)

**Definition 12.3.** A real continuous function \(g\) on an interval \(J\) is *operator monotone on \(J\)* if \(g(x)\le g(y)\) whenever \(x\le y\) are self-adjoint operators with spectra in \(J\).

Every operator monotone function is increasing, as one sees on multiples of \(1\). The converse fails: \(t\mapsto t^2\) is not operator monotone on \([0,\infty)\), since \(x=\begin{pmatrix}1&0\\0&0\end{pmatrix}\le y=\begin{pmatrix}2&1\\1&1\end{pmatrix}\), while \(y^2-x^2=\begin{pmatrix}4&3\\3&2\end{pmatrix}\) has determinant \(-1\) and so is not positive. By the [Löwner–Heinz inequality](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-17), \(t\mapsto t^\alpha\) is operator monotone on \([0,\infty)\) for \(0\le\alpha\le1\) (for \(\alpha=0\) the function is constant). We need two simpler families.

**Lemma 12.4** (resolvent-type operator monotone functions). Let \(c>0\).

1. \(g_c(t)=t/(c+t)\) is operator monotone on \([0,\infty)\). It takes values in \([0,1)\), \(g_c(0)=0\), and \(g_c\) increases as \(c\) decreases.
2. \(\phi_c(t)=t/(1+c(1-t))\) is operator monotone on \([0,1]\). It maps \([0,1]\) onto \([0,1]\), \(\phi_c(0)=0\), \(\phi_c(1)=1\), \(\phi_c\) decreases as \(c\) increases, and \(\phi_c(t)\to0\) as \(c\to\infty\) for \(t<1\).
3. For \(\alpha>0\), the function \(t/(\alpha+(1-\alpha)t)\) is operator monotone on \([0,1]\), and for \(0<\alpha\le1\) also on \([0,\infty)\).

**Proof.** Inversion reverses the order on invertible positive operators ([working with the order](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-16)). (1) \(g_c(t)=1-c(c+t)^{-1}\). If \(0\le x\le y\), then \(c+x\le c+y\), so \((c+y)^{-1}\le(c+x)^{-1}\) and \(g_c(x)\le g_c(y)\). (2) For \(t\in[0,1]\), \(\phi_c(t)=\frac{1+c}{c}\big(1+c(1-t)\big)^{-1}-\frac1c\). If \(0\le x\le y\le1\), then \(1+c(1-x)\ge1+c(1-y)\ge1\), so \(\big(1+c(1-x)\big)^{-1}\le\big(1+c(1-y)\big)^{-1}\) and \(\phi_c(x)\le\phi_c(y)\). The other claims are elementary. (3) For \(0<\alpha<1\) the function is \((1-\alpha)^{-1}g_c\) with \(c=\alpha/(1-\alpha)\); for \(\alpha=1\) it is \(t\); for \(\alpha>1\) it is \(\phi_c\) with \(c=\alpha-1\). \(\square\)

**Lemma 12.5** (a projection on countably many vectors). Let \(A\) be a concrete C\(^*\)-algebra on \(H\) with weak closure \(M\), let \(p\in M\) be a projection, and let \(\xi_1,\xi_2,\dots\in H\). There are \(y\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\) and a projection \(q\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\) such that, for all \(k\),
\[
\begin{gathered}
y(1-p)\xi_k\\
=0,\\
yp\xi_k\\
=p\xi_k,\\
q(1-p)\xi_k\\
=0,\\
qp\xi_k\\
=p\xi_k .
\end{gathered}
\]

**Proof.** Scaling the vectors changes nothing, so we assume \(\|\xi_k\|\le1\). Put \(\eta_k=(1-p)\xi_k\) and \(\zeta_k=p\xi_k\). By Kaplansky's density theorem 7.1(3), \(p\) is a strong limit of a net in \(A_+\cap S\). Since \(p\eta_k=0\) and \(p\zeta_k=\zeta_k\), for every \(m\) we can choose \(x_m\in A_+\cap S\) with
\[
\begin{gathered}
\|x_m\eta_k\|\\
\le4^{-m}\\
\text{and}\\
\|(1-x_m)\zeta_k\|\\
\le\tfrac1m\\
(k\\
\le m).
\end{gathered}
\]
For \(n\le m\) put \(X_{n,m}=\sum_{j=n}^m2^jx_j\) and \(y_{n,m}=g_1(X_{n,m})=X_{n,m}(1+X_{n,m})^{-1}\). Then \(y_{n,m}\in A_+\cap S\), since \(g_1(0)=0\) and \(0\le g_1\le1\).

*Monotonicity.* For fixed \(n\), \(X_{n,m}\) increases with \(m\), so \(y_{n,m}\) increases with \(m\) by Lemma 12.4(1), to a limit \(y_n\in(A_+\cap S)^{\nearrow}\). Since \(X_{n+1,m}\le X_{n,m}\), \(y_{n+1}\le y_n\), and \(y_n\) decreases to a limit \(y\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\).

*The vectors \(\eta_k\).* For \(k\le n\le m\), using \(g_1(t)\le t\),
\[
\begin{gathered}
\langle y_{n,m}\eta_k,\eta_k\rangle\\
\le\langle X_{n,m}\eta_k,\eta_k\rangle\\
\le\sum_{j\ge n}2^j\|x_j\eta_k\|\\
\le\sum_{j\ge n}2^{-j}\\
=2^{1-n}.
\end{gathered}
\]
So \(0\le\langle y\eta_k,\eta_k\rangle\le\langle y_n\eta_k,\eta_k\rangle\le2^{1-n}\) for all \(n\ge k\). Hence \(\|y^{1/2}\eta_k\|=0\) and \(y\eta_k=0\).

*The vectors \(\zeta_k\).* Since \(X_{n,m}\ge2^mx_m\), \(y_{n,m}\ge g_1(2^mx_m)\), so \(1-y_{n,m}\le(1+2^mx_m)^{-1}\). For \(t\in[0,1]\) and \(b>0\), \((1+bt)^{-1}\le(1+b(1-t))/(1+b)\), because \((1+bt)(1+b-bt)-(1+b)=b^2t(1-t)\ge0\). With \(b=2^m\) this gives \(1-y_{n,m}\le2^{-m}+(1-x_m)\). For \(k\le m\),
\[
\begin{gathered}
\langle(1-y_{n,m})\zeta_k,\zeta_k\rangle\\
\le2^{-m}+\|(1-x_m)\zeta_k\|\\
\le2^{-m}+\tfrac1m .
\end{gathered}
\]
Letting \(m\to\infty\), \(\langle(1-y_n)\zeta_k,\zeta_k\rangle\le0\). Since \(1-y_n\ge0\), \((1-y_n)\zeta_k=0\) for all \(n\), and in the limit \(y\zeta_k=\zeta_k\).

*The projection \(q\).* Let \(\phi_n\) be the functions of Lemma 12.4(2) with \(c=n\). They decrease to the indicator function \(1_{\{1\}}\) of the point \(1\) on \([0,1]\). So \(\phi_n(y)\) decreases, and its strong limit \(q\) is \(1_{\{1\}}(y)\), a projection (Theorem 4.2). We show \(q\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\). For fixed \(n\), \(\phi_n(y_{n,m})\in A_+\cap S\), since \(\phi_n(0)=0\). It increases with \(m\) (Lemma 12.4(2)) and converges strongly to \(\phi_n(y_n)\) (Corollary 5.3(1)). So \(z_n=\phi_n(y_n)\in(A_+\cap S)^{\nearrow}\). Next, \(z_{n+1}=\phi_{n+1}(y_{n+1})\le\phi_n(y_{n+1})\le\phi_n(y_n)=z_n\), using \(\phi_{n+1}\le\phi_n\) and operator monotonicity. Let \(z\) be the limit of the decreasing sequence \((z_n)\); then \(z\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\). On one hand, \(q\le\phi_n(y)\le\phi_n(y_n)=z_n\) for all \(n\), so \(q\le z\). On the other hand, for \(k\ge n\), \(\phi_n(y_k)\ge\phi_k(y_k)=z_k\ge z\); letting \(k\to\infty\), \(\phi_n(y)\ge z\) by Corollary 5.3(1), and letting \(n\to\infty\), \(q\ge z\). So \(q=z\).

Finally, \[
\begin{gathered}
\|q\eta_k\|^2\\
=\langle q\eta_k,\eta_k\rangle\\
\le\langle\phi_1(y)\eta_k,\eta_k\rangle\\
\le\langle y\eta_k,\eta_k\rangle\\
=0,
\end{gathered}
\] since \(\phi_1(t)=t/(2-t)\le t\) on \([0,1]\). And \(y\zeta_k=\zeta_k\) implies \(\psi(y)\zeta_k=\psi(1)\zeta_k\) for every continuous \(\psi\) (first for polynomials, then by uniform approximation), so \(\phi_n(y)\zeta_k=\zeta_k\) for all \(n\), and \(q\zeta_k=\zeta_k\). \(\square\)

**Theorem 12.6** (the up-down theorem). Let \(A\) be a concrete C\(^*\)-algebra acting nondegenerately on \(H\), and suppose that \(M=A''\) is \(\sigma\)-finite. Then
\[
\begin{gathered}
M_+\cap S\\
=\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\\
\text{and}\\
M_h\\
=\big((A_h)^{\nearrow}\big)^{\searrow}.
\end{gathered}
\]


**Proof.** The inclusions \(\supseteq\) hold by Lemma 12.2(5), and for \(M_h\) because \(M\) is strongly closed.

*Projections.* By [the characterization of \(\sigma\)-finite von Neumann algebras](the-double-commutant-theorem.md#oa-fnd-bi-13), \(H\) contains a countable set \(\{\xi_k\}\) that is separating for \(M\). Let \(p\in M\) be a projection. Lemma 12.5 gives \(y\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\subseteq M\) with \((y-p)\xi_k=y(1-p)\xi_k+(yp\xi_k-p\xi_k)=0\) for all \(k\). As \(y-p\in M\) vanishes on a separating set, \(y=p\).

*The unit.* In particular \(1=\lim y_n\) for a decreasing sequence \((y_n)\) in \((A_+\cap S)^{\nearrow}\). Each \(y_n\) satisfies \(1\le y_n\le1\), so \(y_n=1\), and \(1\in(A_+\cap S)^{\nearrow}\).

*Positive contractions.* Let \(x\in M_+\cap S\). By Corollary 4.6, \(x=\sum_k2^{-k}p_k\) with projections \(p_k\in M\). By the first step, each \(p_k\) is the limit of a decreasing sequence \((z_{k,n})_n\) in \((A_+\cap S)^{\nearrow}\). Put
\[
x_n=\sum_{k=1}^n2^{-k}z_{k,n}+2^{-n}\cdot1 .
\]
This is a convex combination of elements of the convex set \((A_+\cap S)^{\nearrow}\) (Lemma 12.2(2)), since the weights add up to \(1\) and \(1\in(A_+\cap S)^{\nearrow}\). So \(x_n\in(A_+\cap S)^{\nearrow}\). The sequence decreases:
\[
\begin{gathered}
x_n-x_{n+1}\\
=\sum_{k=1}^n2^{-k}(z_{k,n}-z_{k,n+1})+2^{-n-1}(1-z_{n+1,n+1})\\
\ge0 .
\end{gathered}
\]
It lies above \(x\): \(z_{k,n}\ge p_k\) and \(\sum_{k>n}2^{-k}p_k\le2^{-n}\), so \(x_n\ge\sum_{k\le n}2^{-k}p_k+2^{-n}\ge x\). For \(n\ge m\), using \(z_{k,n}\le1\) for \(k>m\),
\[
\begin{gathered}
x_n-x\\
\le\sum_{k=1}^m2^{-k}(z_{k,n}-p_k)+\sum_{k=m+1}^n2^{-k}+2^{-n}\\
=\sum_{k=1}^m2^{-k}(z_{k,n}-p_k)+2^{-m}.
\end{gathered}
\]
Let \(x'\) be the strong limit of \((x_n)\). Letting \(n\to\infty\) gives \(x\le x'\le x+2^{-m}\) for every \(m\). So \(x'=x\), and \(x\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\).

*Self-adjoint elements.* Let \(y\in M_h\), \(y\ne0\). Then \(x=(y+\|y\|)/(2\|y\|)\in M_+\cap S\), and \(y=2\|y\|x-\|y\|\cdot1\). Here \(2\|y\|x\in\big((A_h)^{\nearrow}\big)^{\searrow}\) by Lemma 12.2(2). Since \(1\in(A_h)^{\nearrow}\), \(-\|y\|\cdot1\in(A_h)^{\searrow}\subseteq\big((A_h)^{\nearrow}\big)^{\searrow}\) by Lemma 12.2(1) and (3). The set \(\big((A_h)^{\nearrow}\big)^{\searrow}\) is closed under sums by Lemma 12.2(2). \(\square\)

Without \(\sigma\)-finiteness the up-down theorem fails, even with nets in place of sequences (Section 13). The remedy is a third, increasing, limit. First we remove the need for a unit.

**Lemma 12.7** (adding a unit). Let \(A\) be a concrete C\(^*\)-algebra acting nondegenerately on \(H\), and \(\tilde A=A+\mathbb C1\).

1. For \(\varepsilon>0\) and \(x\in(\tilde A_+\cap S)^{\nearrow}\), \((1+\varepsilon)^{-1}(x+\varepsilon)\in(A_+\cap S)^{\uparrow}\).
2. \(\big((\tilde A_+\cap S)^{\nearrow}\big)^{\downarrow}\subseteq\big((A_+\cap S)^{\uparrow}\big)^{\downarrow}\).

**Proof.** (1) Let \(x_n\in\tilde A_+\cap S\) increase to \(x\), and put \(x_0=0\) and \(d_n=x_n-x_{n-1}\ge0\). Write \(d_n=c_n+\alpha_n\) with \(c_n\in A_h\) and \(\alpha_n\in\mathbb R\). We may take \(\alpha_n\ge0\): if \(1\in A\), take \(\alpha_n=0\); if not, \(y+\alpha\mapsto\alpha\) is a \(*\)-homomorphism of \(\tilde A\) onto \(\mathbb C\), which maps the positive element \(d_n\) to a nonnegative number. By [approximate identities](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-20), \(A\) has an increasing approximate identity \((u_i)_{i\in I}\) in \(A_+\cap S\). Its strong limit \(e_0\) (Theorem 1.3) satisfies \(e_0z=\lim u_iz=z\) for \(z\in A\), so \(e_0=1\) on \([AH]=H\): \(u_i\to1\) strongly.

*A scalar inequality.* Let \(c\) be self-adjoint and \(\alpha\ge0\) with \(c+\alpha\ge0\), and let \(0<\beta\le\varepsilon'\). Then
\[
c+(\alpha+\varepsilon')\,g_\beta(|c|)\ge0 ,
\tag{12.1}
\]
with \(g_\beta\) as in Lemma 12.4(1). By the functional calculus of \(c\) it suffices to check \(t+(\alpha+\varepsilon')|t|/(\beta+|t|)\ge0\) for \(t\in\sigma(c)\). For \(t\ge0\) this is clear. For \(t<0\), \(\alpha\ge|t|\), and the left side is at least \[
\begin{gathered}
-|t|+(|t|+\varepsilon')|t|/(\beta+|t|)\\
=|t|(\varepsilon'-\beta)/(\beta+|t|)\\
\ge0.
\end{gathered}
\]

*The approximating net.* Let \(\Lambda\) be the set of triples \(\lambda=(m,\beta,i)\) with \(m\ge1\), \(0<\beta\le\varepsilon2^{-m}\) and \(i\in I\), directed by \(m\le m'\), \(\beta\ge\beta'\), \(i\le i'\). For \(n\le m\) put
\[
\begin{gathered}
w_{n,\beta,i}\\
=c_n+(\alpha_n+\varepsilon2^{-n})\,g_\beta(u_i+|c_n|)\in A_h,\\
v_\lambda\\
=(1+\varepsilon)^{-1}\sum_{n=1}^mw_{n,\beta,i}.
\end{gathered}
\]
Each \(w_{n,\beta,i}\) lies in \(A\), because \(g_\beta(0)=0\) and \(u_i+|c_n|\in A_+\). Since \(u_i+|c_n|\ge|c_n|\) and \(g_\beta\) is operator monotone, (12.1) with \(\varepsilon'=\varepsilon2^{-n}\ge\beta\) gives \(w_{n,\beta,i}\ge0\). Since \(g_\beta\le1\), \(w_{n,\beta,i}\le c_n+\alpha_n+\varepsilon2^{-n}=d_n+\varepsilon2^{-n}\). So
\[
\begin{gathered}
0\\
\le v_\lambda\\
\le(1+\varepsilon)^{-1}(x_m+\varepsilon)\\
\le(1+\varepsilon)^{-1}(x+\varepsilon)\\
\le1 ,
\end{gathered}
\]
and \(v_\lambda\in A_+\cap S\). The net \((v_\lambda)\) increases: \(w_{n,\beta,i}\) increases when \(i\) increases or \(\beta\) decreases (Lemma 12.4(1)), and a larger \(m\) adds nonnegative terms. Let \(v\) be its strong limit. Then \(v\le(1+\varepsilon)^{-1}(x+\varepsilon)\).

For the reverse inequality fix \(N\), then \(m\ge N\) and \(\beta\in(0,\varepsilon2^{-m}]\). The terms with \(n>N\) are positive, so \(v\ge v_{(m,\beta,i)}\ge(1+\varepsilon)^{-1}\sum_{n\le N}w_{n,\beta,i}\) for every \(i\). As \(i\to\infty\), \(u_i+|c_n|\to1+|c_n|\) strongly within a bounded set, so \(g_\beta(u_i+|c_n|)\to g_\beta(1+|c_n|)\) strongly (Corollary 5.3(1)). Since \(1-g_\beta(t)=\beta/(\beta+t)\le\beta\) for \(t\ge1\), \(g_\beta(1+|c_n|)\ge(1-\beta)1\). By Lemma 1.2 the inequality passes to the limit, and
\[
\begin{gathered}
v\\
\ge(1+\varepsilon)^{-1}\sum_{n\le N}\big(c_n+(\alpha_n+\varepsilon2^{-n})(1-\beta)\big)\\
=(1+\varepsilon)^{-1}\Big(x_N+\varepsilon(1-2^{-N})\\
-\beta\sum_{n\le N}(\alpha_n+\varepsilon2^{-n})\Big).
\end{gathered}
\]
Here \(\beta\) can be arbitrarily small, so \(v\ge(1+\varepsilon)^{-1}(x_N+\varepsilon(1-2^{-N}))\). Letting \(N\to\infty\), \(v\ge(1+\varepsilon)^{-1}(x+\varepsilon)\). So \((1+\varepsilon)^{-1}(x+\varepsilon)=v\in(A_+\cap S)^{\uparrow}\).

(2) Let \(x_j\) be a decreasing net in \((\tilde A_+\cap S)^{\nearrow}\) with limit \(x\). By (1), \(y_{j,k}=(1+\frac1k)^{-1}(x_j+\frac1k)\in(A_+\cap S)^{\uparrow}\). For \(0\le t\le1\), \(\frac{kt+1}{k+1}-\frac{(k+1)t+1}{k+2}=\frac{1-t}{(k+1)(k+2)}\ge0\), so \(y_{j,k}\) decreases in \(k\); it also decreases in \(j\). The net \((y_{j,k})\) has limit \(x\). So \(x\in\big((A_+\cap S)^{\uparrow}\big)^{\downarrow}\). \(\square\)

**Lemma 12.8** (suprema of projections). Let \(Y\subseteq B(H)_+\cap S\) be convex, with \(0\in Y\) and \(g_\beta(Y)\subseteq Y\) for all \(\beta\in(0,1]\). If \((p_i)_{i\in I}\) is any family of projections in \(Y^{\uparrow}\), then \(\bigvee_ip_i\in Y^{\uparrow}\).

**Proof.** Put \(p=\bigvee_ip_i\). For each \(i\), choose an increasing net \((x_{i,j})_{j\in J_i}\) in \(Y\) with limit \(p_i\), and add to \(J_i\) a new least element \(0_i\) with \(x_{i,0_i}=0\); the net is still increasing, since \(x_{i,j}\ge0\). Let \(\Gamma\) be the set of functions \(\gamma\) on \(I\) with \(\gamma(i)\in J_i\) for all \(i\) and \(\gamma(i)=0_i\) for all but finitely many \(i\), ordered pointwise. It is directed. For \(\gamma\in\Gamma\) and \(k\ge1\) put
\[
\begin{gathered}
X_\gamma\\
=\sum_ix_{i,\gamma(i)},\\
y_{\gamma,k}\\
=g_{1/k}(X_\gamma)\\
=X_\gamma\big(\tfrac1k+X_\gamma\big)^{-1}.
\end{gathered}
\]
The sum is finite. If \(\gamma\) has \(N\ge1\) entries that are not least elements, then \(X_\gamma/N\in Y\) by convexity, and \(y_{\gamma,k}=g_{1/(kN)}(X_\gamma/N)\in Y\); if \(N=0\), \(y_{\gamma,k}=0\in Y\).

The net \((y_{\gamma,k})\) increases: \(X_\gamma\) increases with \(\gamma\), \(g_{1/k}\) is operator monotone (Lemma 12.4(1)), and \(g_{1/k}\le g_{1/k'}\) for \(k\le k'\). Let \(y\in Y^{\uparrow}\) be its limit. Then \(0\le y\le1\). Each \(x_{i,j}\le p_i\le p\), so \(x_{i,j}=px_{i,j}p\), hence \(X_\gamma=pX_\gamma p\), \(y_{\gamma,k}=py_{\gamma,k}p\) and \(y=pyp\).

Fix \(i\) and \(k\). For \(j\in J_i\), take \(\gamma\) with \(\gamma(i)=j\) and \(\gamma(i')=0_{i'}\) otherwise; then \(y\ge y_{\gamma,k}=g_{1/k}(x_{i,j})\). Letting \(j\) run through \(J_i\), \(g_{1/k}(x_{i,j})\to g_{1/k}(p_i)=\frac k{k+1}p_i\) strongly (Corollary 5.3(1)). By Lemma 1.2, \(y\ge\frac k{k+1}p_i\), and letting \(k\to\infty\), \(y\ge p_i\). Hence \(p_i(1-y)p_i\le p_i(1-p_i)p_i=0\), while \(1-y\ge0\) because \(y\le1\). So \((1-y)^{1/2}p_i=0\) and \(yp_i=p_i\). So \(y\xi=\xi\) for every \(\xi\) in the range of some \(p_i\), hence for every \(\xi\in pH\): \(yp=p\). With \(y=pyp\) this gives \(y=pyp=p\). \(\square\)

**Theorem 12.9** (the up-down-up theorem). Let \(A\) be a concrete C\(^*\)-algebra acting nondegenerately on \(H\), and \(M=A''\). Then
\[
\begin{gathered}
M_+\cap S\\
=\Big(\big((A_+\cap S)^{\uparrow}\big)^{\downarrow}\Big)^{\uparrow}\\
\text{and}\\
M_h\\
=\Big(\big((A_h)^{\uparrow}\big)^{\downarrow}\Big)^{\uparrow}.
\end{gathered}
\]
If \(1\in A\), then moreover \(M_+\cap S=\Big(\big((A_+\cap S)^{\nearrow}\big)^{\downarrow}\Big)^{\uparrow}\).


**Proof.** The inclusions \(\supseteq\) hold by Lemma 12.2(5).

*Step 1: the case \(1\in A\).* Put \(Y=\big((A_+\cap S)^{\nearrow}\big)^{\downarrow}\) and \(Y'=(A_+\cap S)^{\searrow}\). Both are convex subsets of \(B(H)_+\cap S\) that contain \(0\) (Lemma 12.2(1) and (2)). For \(\beta\in(0,1]\), \(g_\beta\) maps \([0,1]\) into \([0,1]\) and \(g_\beta(0)=0\), so \(g_\beta(A_+\cap S)\subseteq A_+\cap S\); by Lemma 12.2(4), \(g_\beta(Y)\subseteq Y\) and \(g_\beta(Y')\subseteq Y'\). So Lemma 12.8 applies to \(Y\) and to \(Y'\).

*Step 2: infima of projections in \(Y\).* Let \((q_i)\) be projections in \(Y\). Since \(1\in A\), the map \(t\mapsto1-t\) maps \(A_+\cap S\) onto itself, and Lemma 12.2(3) gives \(1-q_i\in1-Y=\big((A_+\cap S)^{\searrow}\big)^{\uparrow}=Y'^{\uparrow}\). By Lemma 12.8 applied to \(Y'\), \(\bigvee_i(1-q_i)\in Y'^{\uparrow}\). Hence \(\bigwedge_iq_i=1-\bigvee_i(1-q_i)\in1-Y'^{\uparrow}=Y\).

*Step 3: projections.* Let \(p\in M\) be a projection. For \(\xi\in pH\) and \(\eta\in(1-p)H\), Lemma 12.5 applied to \(p\) and the two vectors \(\xi,\eta\) gives a projection \(q_{\xi,\eta}\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\subseteq Y\) with \(q_{\xi,\eta}\xi=\xi\) and \(q_{\xi,\eta}\eta=0\). Put \(p_\xi=\bigwedge_{\eta\in(1-p)H}q_{\xi,\eta}\), which lies in \(Y\) by Step 2. Then \(p_\xi\xi=\xi\), and \(p_\xi\eta=p_\xi q_{\xi,\eta}\eta=0\) for every \(\eta\in(1-p)H\), so \(p_\xi\le p\). Hence \(p=\bigvee_{\xi\in pH}p_\xi\), and \(p\in Y^{\uparrow}\) by Lemma 12.8.

*Step 4: positive contractions.* Let \(x\in M_+\cap S\), and write \(x=\sum_k2^{-k}p_k\) with projections \(p_k\in M\) (Corollary 4.6). By Step 3 each \(p_k\) is the limit of an increasing net \((y_{k,j})_{j\in J_k}\) in \(Y\); add a least element with value \(0\) as in Lemma 12.8. Let \(\Gamma\) be the set of functions \(\gamma\) on \(\{1,2,\dots\}\) with \(\gamma(k)\in J_k\), equal to the least element for all but finitely many \(k\), ordered pointwise, and put \(x_\gamma=\sum_k2^{-k}y_{k,\gamma(k)}\). The sum is finite, and \(x_\gamma\in Y\), as a convex combination of elements of \(Y\) and \(0\). The net \((x_\gamma)\) increases, and \(x_\gamma\le x\). For every \(N\), \(\lim_\gamma x_\gamma\ge\sum_{k\le N}2^{-k}p_k\ge x-2^{-N}\). So \(x_\gamma\to x\), and \(x\in Y^{\uparrow}=\Big(\big((A_+\cap S)^{\nearrow}\big)^{\downarrow}\Big)^{\uparrow}\). This proves the last statement of the theorem, and the first one for unital \(A\).

*Step 5: the general case.* Let \(\tilde A=A+\mathbb C1\). Since \(A\) is nondegenerate, \(1\in A''\), so \(\tilde A''=A''=M\). By Step 4 for \(\tilde A\), and Lemma 12.7(2),
\[
\begin{gathered}
M_+\cap S\\
=\Big(\big((\tilde A_+\cap S)^{\nearrow}\big)^{\downarrow}\Big)^{\uparrow}\\
\subseteq\Big(\big((A_+\cap S)^{\uparrow}\big)^{\downarrow}\Big)^{\uparrow}.
\end{gathered}
\]

*Step 6: self-adjoint elements.* The decomposition used for Theorem 12.6 writes \(y\in M_h\) as \(2\|y\|x-\|y\|\cdot1\) with \(x\in M_+\cap S\). An increasing approximate identity of \(A\) converges strongly to \(1\) (proof of Lemma 12.7), so \(1\in(A_h)^{\uparrow}\) and \(-\|y\|\cdot1\in(A_h)^{\downarrow}\subseteq\Big(\big((A_h)^{\uparrow}\big)^{\downarrow}\Big)^{\uparrow}\). This set is closed under sums and contains \(2\|y\|x\) by Lemma 12.2. \(\square\)

**Corollary 12.10** (the monotone closure criterion). Let \(A\) be a concrete C\(^*\)-algebra acting nondegenerately on \(H\).

1. \(A\) is a von Neumann algebra if and only if the strong limit of every norm-bounded increasing net in \(A_h\) lies in \(A\).
2. If \(A''\) is \(\sigma\)-finite, for instance if \(H\) is separable, then \(A\) is a von Neumann algebra if and only if the strong limit of every norm-bounded increasing sequence in \(A_h\) lies in \(A\).

**Proof.** A von Neumann algebra is strongly closed, which gives "only if" in both parts. (1) Suppose \((A_h)^{\uparrow}\subseteq A_h\). Then \((A_h)^{\downarrow}=-(A_h)^{\uparrow}\subseteq A_h\) by Lemma 12.2(3), since \(-A_h=A_h\). Applying Lemma 12.2(1) three times, \(\Big(\big((A_h)^{\uparrow}\big)^{\downarrow}\Big)^{\uparrow}\subseteq A_h\). By Theorem 12.9, \((A'')_h\subseteq A_h\), and every element of \(A''\) is a combination of two self-adjoint elements of \(A''\). So \(A''=A\). (2) The same argument with sequences, using Theorem 12.6. A von Neumann algebra on a separable Hilbert space is \(\sigma\)-finite ([Remark 9.6 of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-13)). \(\square\)

**Example 12.11** (sequences are not enough without \(\sigma\)-finiteness). Let \(H=\ell^2([0,1])\), for counting measure on \([0,1]\), with basis \((\delta_t)\), and let \(A\) be the set of multiplication operators \(m_g\) by bounded Borel functions \(g\) on \([0,1]\). Since \(\langle m_g\delta_t,\delta_t\rangle=g(t)\), \(\|m_g\|=\sup|g|\), and \(g\) is determined by \(m_g\). Uniform limits of Borel functions are Borel, so \(A\) is a C\(^*\)-algebra; it contains \(1\). If \(g_k\) is a bounded increasing sequence of real Borel functions with pointwise limit \(g\), then \(g\) is Borel, and \(m_{g_k}\to m_g\) strongly by dominated convergence (for counting measure). So \(A\) contains the strong limits of its bounded increasing sequences of self-adjoint elements. But \(A\) is not a von Neumann algebra. There are subsets \(T\subseteq[0,1]\) that are not Borel: [Corollary 2.8 and Lemma 1.3 of the Polish-space lesson](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-12) prove that this uncountable Polish space has \(2^{\aleph_0}\) points but at most that many Borel sets, whereas Cantor’s diagonal theorem gives strictly more subsets. The cardinal identities and diagonal theorem have full proofs in Theorem 8.2 and Proposition 8.3 of the Hahn–Banach lesson. The operators \(m_{1_{T\cap F}}\), for finite \(F\subseteq[0,1]\), lie in \(A\) and increase strongly to \(m_{1_T}\), which lies in the weak closure \(A''\) but not in \(A\). Here \(A''\) is not \(\sigma\)-finite: it contains the uncountably many orthogonal projections \(m_{1_{\{t\}}}\).

**Example 12.12** (nondegeneracy is needed). Let \(H\ne\{0\}\) and \(A=\{0\}\). Then \(A'=B(H)\) and \(A''=\mathbb C1\), but every monotone limit of elements of \(A\) is \(0\). So \(1\in A''_+\cap S\) is not in any of the sets built from \(A\) in Theorems 12.6 and 12.9. The same happens for every \(A\) with \([AH]\ne H\): all monotone limits \(x\) of elements of \(A\) satisfy \(x=exe\) for the projection \(e\) onto \([AH]\), while \(1\in A''\). Restricting to \([AH]\) shows that both theorems hold for every concrete C\(^*\)-algebra if \(A''\) is replaced by the weak closure of \(A\).

## 13. The last increasing limit cannot be dropped

Theorem 12.9 uses three monotone limits where Theorem 12.6 uses two. The following example shows that the third one is needed when the von Neumann algebra is not \(\sigma\)-finite.

**Example 13.1.** Let \(H_d=\ell^2([0,1])\) for counting measure, with basis \((\delta_t)_{t\in[0,1]}\), and \(H_c=L^2[0,1]\) for Lebesgue measure. For \(g\in C[0,1]\) let \(m_g\) denote multiplication by \(g\) on either space, and let
\[
\begin{gathered}
A\\
=\{m_g\oplus m_g:g\in C[0,1]\}\\
\subseteq B(H_d\oplus H_c),\\
M\\
=A'',\\
z\\
=1\oplus0 .
\end{gathered}
\]
Since \(\|m_g\oplus m_g\|=\max|g|\), \(A\) is a unital concrete C\(^*\)-algebra. We show:

(a) Every element of \((A_h)^{\uparrow}\) is \(m_f\oplus m_f\) for a unique bounded lower semicontinuous \(f\) on \([0,1]\), namely the pointwise supremum of the net. Conversely every bounded lower semicontinuous \(f\) arises.

(b) \(z\in M\).

(c) If \(a\in(A_h)^{\uparrow}\) and \(a\ge z\), then \(a\ge1\). Consequently \(z\notin\big((A_h)^{\uparrow}\big)^{\downarrow}\), and in particular \(z\notin\big((A_+\cap S)^{\uparrow}\big)^{\downarrow}\).

(d) \(z\in\big((A_+\cap S)^{\searrow}\big)^{\uparrow}\), and \(M\) is not \(\sigma\)-finite.

So \(z\in M_+\cap S\) is reached by three monotone limits, as Theorem 12.9 asserts, but not by the first two.

*Proof of (a).* Let \((g_i)\) be an increasing net of real continuous functions with \(|g_i|\le C\), and \(f=\sup_ig_i\) pointwise. Then \(f\) is bounded and lower semicontinuous. For each rational \(r\), the open set \(\{f>r\}\) is the union of the open sets \(\{g_i>r\}\). For every rational-interval basic open set contained in some \(\{g_i>r\}\), choose one such index. There are countably many choices, and they cover \(\{f>r\}\), since each point has such a basic neighborhood inside one member of the cover. Collecting these indices over all rational \(r\) gives a sequence of indices, and since the index set is directed we can choose an increasing sequence \(i_1\le i_2\le\cdots\) that eventually lies above each of them. Then \(g_{i_n}\to f\) pointwise: if \(r<f(t)\) is rational, some chosen index \(j\) has \(g_j(t)>r\), and \(g_{i_n}(t)\ge g_j(t)\) for large \(n\). For \(\xi\) in \(H_d\) or \(H_c\) and \(i\ge i_n\),
\[
\begin{gathered}
\|(m_f-m_{g_i})\xi\|^2\\
=\int(f-g_i)^2|\xi|^2\\
\le2C\int(f-g_{i_n})|\xi|^2 ,
\end{gathered}
\]
the integral taken for counting measure or Lebesgue measure. The right side tends to \(0\) as \(n\to\infty\), by dominated convergence. So \(m_{g_i}\oplus m_{g_i}\to m_f\oplus m_f\) strongly. Uniqueness holds because \(f(t)=\langle a\delta_t,\delta_t\rangle\). Conversely, let \(f\) be bounded and lower semicontinuous, with \(|f|\le C\). The continuous functions \(g\) with \(-C\le g\le f\) form an upward directed family, since \(\max(g_1,g_2)\) is again one, and it is bounded in norm. Its pointwise supremum is \(f\): put \(g_n(t)=\inf_{s\in[0,1]}(f(s)+n|s-t|)\). The triangle inequality gives \(|g_n(t)-g_n(t')|\leq n|t-t'|\), so \(g_n\) is continuous. Also \(-C\leq g_n\leq f\leq C\), and \(g_n\) increases in \(n\). Given \(t\) and \(\varepsilon>0\), lower semicontinuity gives \(\rho>0\) with \(f(s)>f(t)-\varepsilon\) for \(|s-t|<\rho\). Outside that neighborhood, \(f(s)+n|s-t|\geq-C+n\rho\geq f(t)-\varepsilon\) once \(n\) is large. Hence \(g_n(t)\geq f(t)-\varepsilon\), proving \(g_n(t)\uparrow f(t)\). Indexed by itself, this family is an increasing net, and the corresponding net in \(A_h\) converges strongly to \(m_f\oplus m_f\).

*Proof of (b).* It suffices to show that every \(T\in A'\) commutes with \(z\), that is, has no off-diagonal parts. Let \(Q\) be the part of \(T\) that maps \(H_d\) to \(H_c\). Compressing \(T(m_g\oplus m_g)=(m_g\oplus m_g)T\) gives \(Qm_g=m_gQ\) for all \(g\). For \(t\in[0,1]\), \(m_g\delta_t=g(t)\delta_t\), so the function \(\eta_t=Q\delta_t\in L^2[0,1]\) satisfies \((g-g(t))\eta_t=0\) almost everywhere. With \(g(s)=s\) this says \((s-t)\eta_t(s)=0\) for almost every \(s\), so \(\eta_t=0\) almost everywhere. Hence \(Q=0\) on the dense span of the \(\delta_t\), and \(Q=0\). The part of \(T\) from \(H_c\) to \(H_d\) is the adjoint of the corresponding part \(Q'\) of \(T^*\in A'\), and \(Q'=0\) by the same argument. So \(z\in A''=M\).

*Proof of (c).* By (a), \(a=m_f\oplus m_f\) with \(f\) bounded. From \(a\ge z\), \(f(t)=\langle a\delta_t,\delta_t\rangle\ge\langle z\delta_t,\delta_t\rangle=1\) for every \(t\). So \(f\ge1\) everywhere, and \(a\ge1\) on both summands. If \(z\) were the limit of a decreasing net \((a_j)\) in \((A_h)^{\uparrow}\), then \(a_j\ge z\), so \(a_j\ge1\) for all \(j\), and \(z\ge1\), which is false because \(H_c\ne\{0\}\).

*Proof of (d).* For \(t\in[0,1]\) let \(h_{t,n}(s)=\max(0,1-n|s-t|)\). As \(n\to\infty\), \(h_{t,n}\) decreases to \(1_{\{t\}}\). By dominated convergence, \(m_{h_{t,n}}\to m_{1_{\{t\}}}\) strongly on \(H_d\) and \(m_{h_{t,n}}\to0\) strongly on \(H_c\), since \(\{t\}\) is a null set. For a finite set \(F\subseteq[0,1]\), the sums \(\sum_{t\in F}h_{t,n}\) have disjoint supports and values in \([0,1]\) once \(n\) is large, and they decrease to \(1_F\). So \(z_F=m_{1_F}\oplus0\in(A_+\cap S)^{\searrow}\). As \(F\) increases, \(z_F\) increases strongly to \(z\). So \(z\in\big((A_+\cap S)^{\searrow}\big)^{\uparrow}\). The projections \(z_{\{t\}}\), \(t\in[0,1]\), lie in \(M\) and are mutually orthogonal and nonzero, so \(M\) is not \(\sigma\)-finite. \(\square\)

## 14. Exercises

**Exercise 14.1** (hard; a second proof of the density theorem). For \(x\in B(H)\) put \(F(x)=2x(1+x^*x)^{-1}\) and, for \(y\in S\), \(G(y)=y\big(1+(1-y^*y)^{1/2}\big)^{-1}\).

(a) Show that \(\|F(x)\|\le1\), \(F(x)^*=F(x^*)\), \(G(F(x))=x\) for \(x\in S\), and \(F(G(y))=y\) for \(y\in S\).

(b) Show that \(F\) is continuous from \(B(H)\) to \(B(H)\) for the strong\(^*\) topology, along arbitrary nets.

(c) Deduce Theorem 7.1(1) for a unital concrete C\(^*\)-algebra \(A\).

*Solution.* (a) We use \(xq(x^*x)=q(xx^*)x\) for continuous \(q\), which holds for polynomials and then by uniform approximation. With \(t=x^*x\), \(F(x)^*F(x)=4t(1+t)^{-2}\le1\), since \(4t\le(1+t)^2\). Next, \[
\begin{gathered}
F(x)^*\\
=2(1+x^*x)^{-1}x^*\\
=2x^*(1+xx^*)^{-1}\\
=F(x^*).
\end{gathered}
\] For \(x\in S\), \(t\in[0,1]\), and \(1-4t/(1+t)^2=\big((1-t)/(1+t)\big)^2\), so
\[
\begin{gathered}
G(F(x))\\
=2x(1+t)^{-1}\Big(1+\tfrac{1-t}{1+t}\Big)^{-1}\\
=2x(1+t)^{-1}\tfrac{1+t}2\\
=x ,
\end{gathered}
\]
where all functions are evaluated at \(t=x^*x\). For \(y\in S\) put \(\sigma=(1-y^*y)^{1/2}\) and \(\chi=(1+\sigma)^{-1}\), functions of \(y^*y\). Then \[
\begin{gathered}
G(y)^*G(y)\\
=y^*y\chi^2\\
=(1-\sigma^2)(1+\sigma)^{-2}\\
=(1-\sigma)(1+\sigma)^{-1},
\end{gathered}
\] so \(1+G(y)^*G(y)=2(1+\sigma)^{-1}\), and \(F(G(y))=2y\chi\cdot\frac{1+\sigma}2=y\).

(b) Using \(x(1+x^*x)^{-1}=(1+xx^*)^{-1}x\),
\[
\begin{gathered}
x(1+x^*x)^{-1}-y(1+y^*y)^{-1}\\
=(1+xx^*)^{-1}\big[x(1+y^*y)-(1+xx^*)y\big]\\
(1+y^*y)^{-1}\\
=(1+xx^*)^{-1}\big[(x-y)+x(y^*-x^*)y\big]\\
(1+y^*y)^{-1}.
\end{gathered}
\]
Since \(\|(1+xx^*)^{-1}\|\le1\) and \(\|(1+xx^*)^{-1}x\|\le\frac12\),
\[
\begin{gathered}
\tfrac12\|(F(x)-F(y))\xi\|\\
\le\|(x-y)(1+y^*y)^{-1}\xi\|\\
+\tfrac12\|(y^*-x^*)y(1+y^*y)^{-1}\xi\| .
\end{gathered}
\]
For fixed \(y\) and \(\xi\), the right side tends to \(0\) when \(x\to y\) strongly\(^*\). Applying this to \(x^*,y^*\) and using \(F(x)^*=F(x^*)\) gives strong convergence of the adjoints.

(c) \(A\) is unital, so \(F(A)\subseteq A\cap S\) and \(G(A\cap S)\subseteq A\); with (a), \(F(A)=A\cap S\), and likewise \(F(M)=M\cap S\) for the weak closure \(M=A''\). By the double commutant theorem \(A\) is strongly\(^*\) dense in \(M\), and by (b) \(F(A)=A\cap S\) is strongly\(^*\) dense in \(F(M)=M\cap S\). \(\square\)

**Exercise 14.2** (medium; continuous functions on \(L^2[0,1]\)). Let \(\mu\) be Lebesgue measure on \([0,1]\), that is, the Radon measure that represents the Riemann integral, let \(A=\{m_g:g\in C[0,1]\}\) act on \(L^2[0,1]\) by multiplication, and let \(L=\{m_f:f\in L^\infty[0,1]\}\).

(a) For open \(U\subseteq[0,1]\) show \(m_{1_U}\in(A_+\cap S)^{\nearrow}\), and for closed \(F\) show \(m_{1_F}\in(A_+\cap S)^{\searrow}\).

(b) For every Borel set \(E\) show \(m_{1_E}\in\big((A_+\cap S)^{\nearrow}\big)^{\searrow}\).

(c) Deduce that \(A''=L\), and compare with Theorem 12.6.

*Solution.* (a) If \(U=[0,1]\), use \(g_k=1\); if \(U=\varnothing\), use \(g_k=0\). Otherwise \(g_k(t)=\min(1,k\operatorname{dist}(t,[0,1]\setminus U))\) is continuous with values in \([0,1]\) and increases pointwise to \(1_U\). So \(m_{g_k}\to m_{1_U}\) strongly, by dominated convergence: \(\|(m_{1_U}-m_{g_k})\xi\|^2=\int(1_U-g_k)^2|\xi|^2\,d\mu\). For closed \(F\), \(1-g_k\) built from \(U=[0,1]\setminus F\) decreases to \(1_F\).

(b) Radon measures are outer regular (Definition 2.1 of the lesson on Haar measure). So there are open sets \(U_k\supseteq E\) with \(\mu(U_k\setminus E)<1/k\), and replacing \(U_k\) by \(U_1\cap\dots\cap U_k\) we may assume that they decrease. Then \(1_{U_k}\) decreases to \(1_G\) with \(G=\bigcap_kU_k\supseteq E\) and \(\mu(G\setminus E)=0\). So \(m_{1_E}=m_{1_G}\) is the strong limit of the decreasing sequence \(m_{1_{U_k}}\), each of which lies in \((A_+\cap S)^{\nearrow}\) by (a).

(c) \(L\) is a von Neumann algebra that equals its own commutant (Theorem 9.1 of [Hilbert spaces and compact operators](hilbert-spaces-and-compact-operators.md)). Since \(A\subseteq L\), \(A'\supseteq L'=L\) and \(A''\subseteq L'=L\). Conversely, by (b) and Lemma 12.2(5), \(A''\) contains every \(m_{1_E}\), hence the norm closure of the simple functions, which is \(L\). This is the up-down theorem made concrete: \(A''\) is \(\sigma\)-finite, because \(m_f1=0\) forces \(f=0\), so the function \(1\) separates \(A''\), and every projection of \(A''\) is reached by one increasing and one decreasing sequence. \(\square\)

**Exercise 14.3** (easy; closedness of some classes of operators). Show that the self-adjoint operators and the positive operators form strongly closed sets, and that the normal operators form a strongly\(^*\) closed set. Show that if \(\dim H=\infty\), the normal operators and the unitaries do not form strongly closed sets.

*Solution.* The first two sets are weakly closed by Lemma 1.2. If \(a_i\to a\) strongly\(^*\) with \(a_i\) normal, then \(\|a\xi\|=\lim\|a_i\xi\|=\lim\|a_i^*\xi\|=\|a^*\xi\|\) for every \(\xi\), so \(a\) is normal; no boundedness is needed. In infinite dimensions, the unitaries \(u_n\) of Example 2.5 converge strongly to the isometry \(v\), which is not normal and not unitary. \(\square\)

**Exercise 14.4** (medium; finite-rank perturbations of the identity). Let \(\dim H=\infty\) and \(A=K(H)+\mathbb C1\), the compact operators with the identity adjoined.

(a) Show directly that every unitary \(u\in B(H)\) is the strong limit of unitaries \(u_F\) such that \(u_F-1\) has finite rank.

(b) Show that if \(\|u-1\|\le\lambda\), then \(u\) is a strong\(^*\) limit of unitaries \(v\in A\) with \(\|v-1\|\le\lambda\).

(c) Show that the construction of (a) does not control \(\|u_F-1\|\).

*Solution.* (a) For a finite-dimensional subspace \(F\), let \(F'=F+uF\). The argument of Theorem 8.1(3) extends \(u|_F\) to a unitary \(W\) of \(F'\). Let \(u_F=W\) on \(F'\) and \(1\) on \(F'^\perp\). Then \(u_F-1\) vanishes on \(F'^\perp\) and has range in \(F'\), so it has finite rank, and \(u_F\xi=u\xi\) for \(\xi\in F\). Directed by inclusion, \(u_F\to u\) strongly, and strongly\(^*\) by Corollary 2.4.

(b) \(A\) is a unital concrete C\(^*\)-algebra, and its weak closure is \(B(H)\), because already \(K(H)\) is weakly dense ([Example 4.6 of the double commutant lesson](the-double-commutant-theorem.md#oa-fnd-bi-07)). Theorem 9.1 gives a net in \(U(A,\lambda)\) that converges strongly\(^*\) to \(u\).

(c) Let \(\xi,\eta\) be orthonormal, \(0<\theta<\pi/2\), and let \(u\) be the rotation by \(\theta\) in the plane spanned by \(\xi,\eta\), and \(1\) on its orthogonal complement; then \(\|u-1\|=2\sin(\theta/2)\) is small for small \(\theta\). For \(F=\mathbb C\xi\), \(F'\) is that plane, and \(W\) must send \(\xi\) to \(u\xi\) and the unit vector \(\zeta\in F'\ominus F\) to a unit vector of \(F'\ominus uF\). Choosing \(W\zeta=-u\zeta\) is allowed, and then \(\|(u_F-1)\zeta\|=\|u\zeta+\zeta\|\ge2-\|u\zeta-\zeta\|\), which is close to \(2\). \(\square\)

**Exercise 14.5** (medium; Lusin's theorem with a norm bound). With the notation of Exercise 14.2, let \(f\) be a bounded real Borel function on \([0,1]\), and \(\varepsilon,\delta>0\). Show that there are a Borel set \(E\) with \(\mu([0,1]\setminus E)<\varepsilon\) and a real \(g\in C[0,1]\) with \(g=f\) almost everywhere on \(E\) and \(\max|g|\le(1+\delta)\operatorname{ess\,sup}_E|f|\).

*Solution.* By Exercise 14.2(c), \(m_f\in A''\). Every projection of \(A''=L\) is \(m_{1_E}\) for a Borel set \(E\), since a real \(h\) with \(h^2=h\) almost everywhere is an indicator function almost everywhere. The functional \(\varphi(m_h)=\int h\,d\mu=\langle m_h1,1\rangle\) is positive and normal. Apply Theorem 10.6(2) with \(x=m_f\), \(e=1\) and this \(\varphi\): there are a projection \(m_{1_E}\) with \(\mu([0,1]\setminus E)=\varphi(1-m_{1_E})<\varepsilon\) and a self-adjoint \(m_g\in A\) with \(m_fm_{1_E}=m_gm_{1_E}\) and \(\|m_g\|\le(1+\delta)\|m_fm_{1_E}\|\). The first relation says \(f=g\) almost everywhere on \(E\). Since \(\mu\) gives positive measure to every nonempty open set, \(\|m_g\|=\max|g|\) for continuous \(g\), and \(\|m_{f1_E}\|=\operatorname{ess\,sup}_E|f|\). \(\square\)

## 15. Historical notes

The \(\sigma\)-weak topology comes from trace-class duality, proved in the operator-topologies lesson. Its relationship with the strong and weak operator topologies, together with the double commutant theorem, supplies the prerequisites for the density arguments here. Peterson’s freely readable notes give a comparison for these constructions; the exact programme proofs are linked where they are used.

The proofs distinguish ordinary strong convergence from convergence of adjoints and from bounded strong convergence. This distinction is used in unitary approximation, the noncommutative Egoroff and Lusin arguments, transitivity and the up-down theorems. The bounded-net alternative in Theorem 7.2 develops Elliott and Griffin’s argument with its complete prerequisites.

## Where this leads

- The lesson [The universal enveloping von Neumann algebra of a \(C^*\)-algebra, and \(W^*\)-algebras](the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.md) uses Kaplansky's density theorem, the spectral projections of Section 4 and the monotone closure criterion of Corollary 12.10.
- [Projections and types of von Neumann algebras](projections-and-types-of-von-neumann-algebras.md) uses spectral projections inside a von Neumann algebra (Corollaries 4.3 and 4.4).
- Spatial tensor products of von Neumann algebras uses the density theorem to pass from algebraic tensor products to their weak closures with norm control.

## References

- [van Neerven] J. van Neerven, *Functional Analysis*, [corrected author version, arXiv:2112.11166v7](https://arxiv.org/pdf/2112.11166v7).
- [Blackadar] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, [revised author edition, 8 February 2017](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).

*Freely accessible reading:* [G. A. Elliott; C. J. K. Griffin, *On a question of Kaplansky concerning his density theorem*, main argument and concluding remark](https://arxiv.org/html/2410.03668v1) gives a route through the bounded-net method developed with its full prerequisites in Theorem 7.2. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.
