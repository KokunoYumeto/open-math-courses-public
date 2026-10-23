# Cotangent complexes of simplicial rings

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cotangent complex of a map of rings \(A\to B\) of a topos is computed from the standard resolution of \(B\) by free \(A\)-algebras. Applied degreewise to a map of simplicial rings, the same construction produces a bisimplicial module whose diagonal \(L^\Delta_{B/A}\) is the cotangent complex of the map of simplicial rings. This lesson proves its basic properties. When \(B\) is degreewise a symmetric algebra of a flat module, \(L^\Delta_{B/A}\) is quasi-isomorphic to the module of differentials \(\Omega^1_{B/A}\). It is invariant under quasi-isomorphisms of the map \(A\to B\). And \(C\mapsto L^\Delta_{C/A}\otimes_CB\) is the left derived functor of \(C\mapsto\Omega^1_{C/A}\otimes_CB\) on algebras over \(B\), so that \(L^\Delta_{B/A}\) corepresents derivations in the homotopy category of algebras over \(B\). In particular, every degreewise free resolution of a map of rings computes its cotangent complex.

**Prerequisites.** [*The cotangent complex*](course:AG-HP/the-cotangent-complex#1-simplicial-algebra-and-the-standard-resolution) (Theorem 1.1, Section 10); [*Homotopy sheaves and the free abelian Whitehead theorem*](homotopy-sheaves-and-the-free-abelian-whitehead-theorem.md) (Propositions 5.5 and 5.7, Corollary 7.2); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Theorem 3.2: Deligne–Lazard; Lemma 4.1); [*Simplicial rings and modules in a topos*](simplicial-rings-and-modules-in-a-topos.md) (Lemma 1.2, Definition 3.1, Lemma 3.2, Theorem 4.2); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Lemma 1.1, Lemma 2.1, Proposition 2.2).

## Conventions

\(T\) is a topos; rings are commutative with \(1\). A simplicial ring is a simplicial object of the category of rings of \(T\); its modules and algebras are simplicial modules and simplicial algebras, as in the lesson on simplicial rings and modules in a topos. A map of simplicial modules, or of simplicial rings, is a *quasi-isomorphism* if it induces isomorphisms on all homotopy sheaves, that is, on the homology sheaves of the normalized complexes; the unnormalized complex has the same homology [[Stacks, Tag 019A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-decompose-associated-complexes)]. For a simplicial ring \(B\), \(D_\bullet(B)\) is the localization of the category of \(B\)-modules at the quasi-isomorphisms. A ring of \(T\) is regarded as a constant simplicial ring.

For a ring \(\Lambda\) of \(T\) and a sheaf of sets \(X\), \(\Lambda^{(X)}\) is the free \(\Lambda\)-module on \(X\) and \(\Lambda[X]=\operatorname{Sym}_\Lambda(\Lambda^{(X)})\) the free \(\Lambda\)-algebra on \(X\); thus \(\Lambda^{(X)}=\Lambda\otimes_{\mathbb Z}\mathbb Z^{(X)}\) and \(\Lambda[X]=\Lambda\otimes_{\mathbb Z}\mathbb Z[X]\). The functor \(X\mapsto\Lambda[X]\) is left adjoint to the functor \(U\) from \(\Lambda\)-algebras to sheaves of sets that forgets the algebra structure. A \(\Lambda\)-algebra is *free* if it is isomorphic to some \(\Lambda[X]\), and a simplicial algebra \(C\) over a simplicial ring \(\Lambda\) is *degreewise free* if every \(C_n\) is a free \(\Lambda_n\)-algebra; the isomorphisms \(C_n\cong\Lambda_n[X_n]\) need not be compatible with the simplicial maps. The module of differentials of a free algebra is free on the \(dx\), \(x\in X\):
\[
\begin{aligned}\Omega^1_{\Lambda[X]/\Lambda}&=\Lambda[X]\otimes_\Lambda\Lambda^{(X)}\\&=\Lambda[X]\otimes_{\mathbb Z}\mathbb Z^{(X)}.\end{aligned}
\]
This holds for presheaves by the case of rings, and differentials commute with sheafification [[Stacks, Tag 08TP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sites-modules.html#sites-modules-lemma-differentials-sheafify)]. For a map of rings \(\Lambda\to\Lambda'\) and a map of sheaves of sets \(X\to X'\), the induced map of differentials sends \(f\,dx\) to the image of \(f\) times \(dx'\), where \(x'\) is the image of \(x\).

For a map of rings \(A\to B\) of \(T\), \(P_A(B)\) is the standard resolution [[Stacks, Tag 08SR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-definition-standard-resolution-sheaves-rings)]: \(P_A(B)_0=A[B]\) and \(P_A(B)_n=A[P_A(B)_{n-1}]\), formed on the underlying sheaves of sets, with faces and degeneracies coming from the adjunction. It is a simplicial \(A\)-algebra, functorial in commutative squares of rings, and its augmentation \(P_A(B)\to B\) is a quasi-isomorphism: on underlying simplicial sheaves of sets it is a homotopy equivalence [[Stacks, Tag 08NC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial), [Tag 08ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-lemma-standard-simplicial-homotopy)]. The cotangent complex is \(L_{B/A}=\Omega^1_{P_A(B)/A}\otimes_{P_A(B)}B\) [[Stacks, Tag 08SS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-definition-cotangent-complex-morphism-sheaves-rings)], as in Section 10 of [*The cotangent complex*](course:AG-HP/the-cotangent-complex#extensions-of-sheaves-of-algebras). With the convention \(P_A(B)_{-1}=B\), the formula for differentials of free algebras gives, functorially in commutative squares, the formula (0.1): for \(n\geq0\),
\[
(L_{B/A})_n=B\otimes_{\mathbb Z}\mathbb Z^{(P_A(B)_{n-1})}.
\]

## 1. Free algebras and polynomial algebras on flat modules

Fix a ring \(A\) of \(T\). Write \(F(X)=A[X]\) for the free algebra on a sheaf of sets \(X\), \(\eta\colon X\to UF(X)\) for the unit and \(\varepsilon\colon FU\to1\) for the counit of the adjunction, and \(G=FU\). For an \(A\)-algebra \(B\), \(P_A(B)_n=G^{n+1}B\), with faces \(d_i=G^i\varepsilon_{G^{n-i}B}\colon G^{n+1}B\to G^nB\) for \(0\leq i\leq n\). The augmentation is \(\varepsilon_B\colon GB\to B\).

**Lemma 1.1.** Let \(X\) be a sheaf of sets, \(C_n=P_A(A[X])_n\) for \(n\geq0\) and \(C_{-1}=A[X]\), with \(d_0=\varepsilon_{A[X]}\colon C_0\to C_{-1}\). Let \(\Phi\) be a functor from \(A\)-algebras to an additive category. Put \(t_n=G^{n+1}(F\eta_X)\colon C_n\to C_{n+1}\) for \(n\geq-1\); these are maps of \(A\)-algebras. Then the augmented complex
\[
\begin{aligned}&\cdots\to\Phi(C_1)\xrightarrow{\partial_1}\Phi(C_0)\\&\qquad\xrightarrow{\partial_0}\Phi(C_{-1})\to0,\\&\partial_n=\textstyle\sum_{i=0}^n(-1)^i\Phi(d_i),\end{aligned}
\]
is contractible: the maps \(k_n=(-1)^{n+1}\Phi(t_n)\colon\Phi(C_n)\to\Phi(C_{n+1})\) satisfy \(\partial_0k_{-1}=1\) and \(\partial_{n+1}k_n+k_{n-1}\partial_n=1\) for \(n\geq0\). In particular, if \(\Phi\) takes values in abelian sheaves, the augmentation \(\Phi(P_A(A[X]))\to\Phi(A[X])\) is a quasi-isomorphism of simplicial abelian sheaves.

**Proof.** Two identities between maps of algebras hold: \(d_{n+1}t_n=1\) on \(C_n\), and \(d_it_n=t_{n-1}d_i\) on \(C_n\) for \(0\leq i\leq n\). For the first, \(d_{n+1}t_n=G^{n+1}(\varepsilon_{A[X]}\circ F\eta_X)=1\) by the triangle identity. For the second, write \(f=G^{n-i}(F\eta_X)\), a map from \(G^{n-i}A[X]\) to \(G^{n+1-i}A[X]\), so that \(t_n=G^{i+1}f\) and \(t_{n-1}=G^if\). Naturality of \(\varepsilon\) gives \(\varepsilon_{G^{n+1-i}A[X]}\circ Gf=f\circ\varepsilon_{G^{n-i}A[X]}\); applying \(G^i\) gives \(d_it_n=t_{n-1}d_i\).

Apply \(\Phi\). First, \(\partial_0k_{-1}=\Phi(d_0t_{-1})=1\). For \(n\geq0\), expand \(\partial_{n+1}k_n=(-1)^{n+1}\sum_{i=0}^{n+1}(-1)^i\Phi(d_it_n)\). By the two identities, the terms with \(i\leq n\) add up to \((-1)^{n+1}\Phi(t_{n-1})\partial_n\), and the term \(i=n+1\) is \(1\). So
\[
\partial_{n+1}k_n=(-1)^{n+1}\Phi(t_{n-1})\partial_n+1,
\]
while \(k_{n-1}\partial_n=(-1)^n\Phi(t_{n-1})\partial_n\). The sum is \(1\). For abelian sheaves, the augmented unnormalized complex of \(\Phi(C)\) is acyclic, so the unnormalized complex of \(\Phi(C)\) has homology \(\Phi(C_{-1})\) in degree \(0\), through the augmentation, and \(0\) elsewhere; this is the homology of the constant simplicial object \(\Phi(C_{-1})\). \(\square\)

The contraction consists of the maps \(\Phi(t_n)\). So if \(\Phi\) takes values in complexes of abelian sheaves, as the de Rham complex does, the \(k_n\) are maps of complexes.

**Remark 1.2.** With the faces indexed in the opposite order, \(d'_i=G^{n-i}\varepsilon_{G^iB}\), the same maps \(t_n\) satisfy \(d'_0t_n=1\) and \(d'_{i+1}t_n=t_{n-1}d'_i\), by the same two arguments, and then \(k'_n=\Phi(t_n)\), without the sign, is a contraction. So Lemma 1.1 does not depend on the convention for the faces.

**Proposition 1.3.** Let \(E\) be a flat \(A\)-module and \(B=\operatorname{Sym}_A(E)\). The map \(L_{B/A}\to\Omega^1_{B/A}\) induced by the augmentation \(P_A(B)\to B\) is a quasi-isomorphism.

**Proof.** *Free modules.* Let \(E=A^{(X)}\), so \(B=A[X]\), and put \(P=P_A(B)\). The composite
\[
\Omega^1_{P/A}\to\Omega^1_{P/A}\otimes_PB=L_{B/A}\to\Omega^1_{B/A}
\]
is \(\Omega^1_{-/A}\) applied to the augmentation, a quasi-isomorphism by Lemma 1.1. The first map is the tensor product of the \(P\)-module \(\Omega^1_{P/A}\), which is degreewise free and hence flat, with the quasi-isomorphism \(P\to B\); it is a quasi-isomorphism by Proposition 2.2 of the lesson on derived tensor products. By two out of three, the second map is a quasi-isomorphism.

*Flat modules.* By Theorem 3.2 of the lesson on non-additive functors, \(E\) is the local inductive limit of a local system of finite free modules. The constructions \(E\mapsto\operatorname{Sym}_A(E)\), \(B\mapsto P_A(B)\), \(\Omega^1\) and \(L\) are built from free modules on sheaves of sets, symmetric powers, tensor products and finite limits, which commute with local inductive limits (Propositions 5.5 and 5.7 (2) of the Whitehead lesson and Section 4 of the lesson on non-additive functors). So the map of the proposition is the local inductive limit of the corresponding maps for the finite free modules, which are quasi-isomorphisms by the first case. Homotopy sheaves commute with local inductive limits (Proposition 5.7 (1) and (4) of the Whitehead lesson), so the map is a quasi-isomorphism. \(\square\)

## 2. The cotangent complex of a map of simplicial rings

**Construction 2.1.** Let \(A\to B\) be a map of simplicial rings. For \(n\geq0\), \(P_{A_n}(B_n)\) is a simplicial \(A_n\)-algebra. A map \(\theta\colon[n']\to[n]\) of \(\Delta\) gives a commutative square from \(A_n\to B_n\) to \(A_{n'}\to B_{n'}\), hence a map of simplicial rings \(P_{A_n}(B_n)\to P_{A_{n'}}(B_{n'})\). So \((n,m)\mapsto P_{A_n}(B_n)_m\) is a bisimplicial ring \(P_A(B)\). Its *rows* are the simplicial \(A\)-algebras \(P_A(B)_{\bullet,m}\colon n\mapsto P_{A_n}(B_n)_m\), and its *columns* the standard resolutions \(P_{A_n}(B_n)\). Regarding \(A\) and \(B\) as bisimplicial rings constant in the direction \(m\), \(P_A(B)\) is an \(A\)-algebra augmented to \(B\). Its diagonal is the simplicial \(A\)-algebra \(P^\Delta_A(B)\), with \(P^\Delta_A(B)_n=P_{A_n}(B_n)_n\), augmented to \(B\).

**Lemma 2.2.** \(P^\Delta_A(B)\) is degreewise free over \(A\): \(P^\Delta_A(B)_n=A_n[P_{A_n}(B_n)_{n-1}]\), with \(P_{A_n}(B_n)_{-1}=B_n\). The augmentation \(P^\Delta_A(B)\to B\) is a quasi-isomorphism and an epimorphism in each degree.

**Proof.** The first statement is the definition. The augmentation is the diagonal of the map of bisimplicial rings \(P_A(B)\to B\), whose column \(n\) is the augmentation \(P_{A_n}(B_n)\to B_n\), a quasi-isomorphism. By Lemma 1.1 of the lesson on derived tensor products, applied to the underlying bisimplicial abelian sheaves, the diagonal is a quasi-isomorphism. In degree \(n\) the augmentation is a composite of faces of the standard resolution, which have sections, and of the counit \(A_n[B_n]\to B_n\), which is surjective. \(\square\)

**Definition 2.3.** The bisimplicial \(B\)-module \(L_{B/A}\) has the terms \((L_{B/A})_{n,m}=(L_{B_n/A_n})_m\), with \(B\) constant in the direction \(m\). The *cotangent complex* of \(A\to B\) is its diagonal; with \(P^\Delta=P^\Delta_A(B)\),
\[
\begin{aligned}L^\Delta_{B/A}&=\Delta L_{B/A}\\&=\Omega^1_{P^\Delta/A}\otimes_{P^\Delta}B.\end{aligned}
\]
The two descriptions agree: both have the term \(\Omega^1_{P_{A_n}(B_n)_n/A_n}\otimes B_n\) in degree \(n\), with the same simplicial maps.

**Proposition 2.4.**

1. \(L^\Delta_{B/A}\) is degreewise free, hence flat: \((L^\Delta_{B/A})_n=B_n\otimes_{\mathbb Z}\mathbb Z^{(P_{A_n}(B_n)_{n-1})}\).
2. If \(A\) and \(B\) are constant, \(L^\Delta_{B/A}=L_{B/A}\).
3. A commutative square of simplicial rings from \(A\to B\) to \(A'\to B'\) induces maps \(L^\Delta_{B/A}\to L^\Delta_{B'/A'}\) of \(B\)-modules and \(L^\Delta_{B/A}\otimes_BB'\to L^\Delta_{B'/A'}\) of \(B'\)-modules, functorially in the square.
4. The augmentation \(P^\Delta\to B\) induces a map of \(B\)-modules \(c\colon L^\Delta_{B/A}\to\Omega^1_{B/A}\), natural in \(A\to B\). It is the diagonal of the map of bisimplicial modules \(L_{B/A}\to\Omega^1_{B/A}\), with \(\Omega^1_{B/A}\) constant in the direction \(m\), whose column \(n\) is the map \(L_{B_n/A_n}\to\Omega^1_{B_n/A_n}\) of Proposition 1.3.

**Proof.** (1) is (0.1) in each degree. (2) If \(A\) and \(B\) are constant, \(L_{B/A}\) is constant in the direction \(n\), and its diagonal is its column. (3) follows from the functoriality of the standard resolution in commutative squares, and (4) from the definitions. \(\square\)

**Proposition 2.5.** Suppose that for every \(n\) there is a flat \(A_n\)-module \(E_n\) with \(B_n\cong\operatorname{Sym}_{A_n}(E_n)\) as \(A_n\)-algebras; for instance, \(B\) degreewise free over \(A\). Then \(c\colon L^\Delta_{B/A}\to\Omega^1_{B/A}\) is a quasi-isomorphism, and \(\Omega^1_{B/A}\) is a flat \(B\)-module.

**Proof.** Column \(n\) of the map of bisimplicial modules in Proposition 2.4 (4) is \(L_{B_n/A_n}\to\Omega^1_{B_n/A_n}\), a quasi-isomorphism by Proposition 1.3. By Lemma 1.1 of the lesson on derived tensor products, the diagonal \(c\) is a quasi-isomorphism. The isomorphisms \(B_n\cong\operatorname{Sym}(E_n)\) are used one degree at a time, so they need not be compatible with the simplicial maps. Finally \(\Omega^1_{B_n/A_n}\cong B_n\otimes_{A_n}E_n\) is a flat \(B_n\)-module. \(\square\)

## 3. Invariance under quasi-isomorphisms

**Theorem 3.1.** Let
\[
\begin{array}{ccc}A&\longrightarrow&B\\ {\scriptstyle u}\downarrow&&\downarrow{\scriptstyle v}\\ A'&\longrightarrow&B'\end{array}
\]
be a commutative square of simplicial rings in which \(u\) and \(v\) are quasi-isomorphisms.

1. For every \(m\geq0\), the maps of rows \(P_A(B)_{\bullet,m}\to P_{A'}(B')_{\bullet,m}\), \(\Omega^1_{P_A(B)_{\bullet,m}/A}\to\Omega^1_{P_{A'}(B')_{\bullet,m}/A'}\) and \((L_{B/A})_{\bullet,m}\to(L_{B'/A'})_{\bullet,m}\) are quasi-isomorphisms.
2. The maps \(L^\Delta_{B/A}\to L^\Delta_{B'/A'}\) and \(L^\Delta_{B/A}\otimes_BB'\to L^\Delta_{B'/A'}\) are quasi-isomorphisms.

**Proof.** Write \(P_m=P_A(B)_{\bullet,m}\) and \(P'_m=P_{A'}(B')_{\bullet,m}\), with \(P_{-1}=B\) and \(P'_{-1}=B'\). Since \(P_{A_n}(B_n)_m=A_n[P_{A_n}(B_n)_{m-1}]\), the Conventions and (0.1) give the isomorphisms (3.1) of simplicial abelian sheaves
\[
\begin{aligned}P_m&=A\otimes_{\mathbb Z}\mathbb Z[P_{m-1}],\\ \Omega^1_{P_m/A}&=P_m\otimes_{\mathbb Z}\mathbb Z^{(P_{m-1})},\\ (L_{B/A})_{\bullet,m}&=B\otimes_{\mathbb Z}\mathbb Z^{(P_{m-1})},\end{aligned}
\]
compatible with the simplicial maps, which are induced by maps of rings and of sheaves of sets, and the same with primes, compatibly with the maps induced by the square.

We show by induction on \(m\geq-1\) that \(P_m\to P'_m\) is a quasi-isomorphism; for \(m=-1\) it is \(v\). Let \(m\geq0\). The map \(P_{m-1}\to P'_{m-1}\) is a quasi-isomorphism and a homomorphism of simplicial abelian sheaves, so \(\mathbb Z^{(P_{m-1})}\to\mathbb Z^{(P'_{m-1})}\) is a quasi-isomorphism by Corollary 7.2 of the Whitehead lesson. These are degreewise free \(\mathbb Z\)-modules, and their normalized complexes consist of flat modules. By Lemma 4.1 of the lesson on non-additive functors, applied to \(\operatorname{Sym}^k_{\mathbb Z}\) and the normalized complexes, \(\operatorname{Sym}^k_{\mathbb Z}(\mathbb Z^{(P_{m-1})})\to\operatorname{Sym}^k_{\mathbb Z}(\mathbb Z^{(P'_{m-1})})\) is a quasi-isomorphism for every \(k\); taking the direct sum over \(k\), so is \(\mathbb Z[P_{m-1}]\to\mathbb Z[P'_{m-1}]\). Factor \(P_m\to P'_m\) as
\[
\begin{aligned}A\otimes_{\mathbb Z}\mathbb Z[P_{m-1}]&\to A\otimes_{\mathbb Z}\mathbb Z[P'_{m-1}]\\&\to A'\otimes_{\mathbb Z}\mathbb Z[P'_{m-1}].\end{aligned}
\]
The first map is \(A\otimes_{\mathbb Z}-\) applied to a quasi-isomorphism between flat simplicial \(\mathbb Z\)-modules, and the second is \(u\otimes_{\mathbb Z}\mathbb Z[P'_{m-1}]\) with \(\mathbb Z[P'_{m-1}]\) flat. Both are quasi-isomorphisms by Lemma 2.1 of the lesson on derived tensor products. This proves the claim on \(P_m\).

By (3.1), the maps on \(\Omega^1\) and on \(L\) factor as
\[
\begin{aligned}P_m\otimes\mathbb Z^{(P_{m-1})}&\to P'_m\otimes\mathbb Z^{(P_{m-1})}\\&\to P'_m\otimes\mathbb Z^{(P'_{m-1})},\\ B\otimes\mathbb Z^{(P_{m-1})}&\to B'\otimes\mathbb Z^{(P_{m-1})}\\&\to B'\otimes\mathbb Z^{(P'_{m-1})},\end{aligned}
\]
tensor products over \(\mathbb Z\). The first maps tensor the quasi-isomorphisms \(P_m\to P'_m\) and \(v\) with the flat \(\mathbb Z^{(P_{m-1})}\). The second maps tensor the quasi-isomorphism between flat modules \(\mathbb Z^{(P_{m-1})}\to\mathbb Z^{(P'_{m-1})}\) with \(P'_m\) and \(B'\). By Lemma 2.1 of the lesson on derived tensor products all four are quasi-isomorphisms. This proves (1).

(2) By (1), the map of bisimplicial modules \(L_{B/A}\to L_{B'/A'}\) is a quasi-isomorphism on every row. By Lemma 1.1 of the lesson on derived tensor products, its diagonal \(L^\Delta_{B/A}\to L^\Delta_{B'/A'}\) is a quasi-isomorphism. The map \(L^\Delta_{B/A}\to L^\Delta_{B/A}\otimes_BB'\) is the tensor product of the flat \(B\)-module \(L^\Delta_{B/A}\) with the quasi-isomorphism \(v\), a quasi-isomorphism by Proposition 2.2 of that lesson. The second assertion follows by two out of three. \(\square\)

**Corollary 3.2.** In the situation of Theorem 3.1, suppose that every \(B_n\) is isomorphic to \(\operatorname{Sym}_{A_n}(E_n)\) with \(E_n\) a flat \(A_n\)-module; for instance, \(B\) degreewise free over \(A\). Then the quasi-isomorphisms
\[
\begin{aligned}\Omega^1_{B/A}\otimes_BB'&\xleftarrow{\;c\otimes B'\;}L^\Delta_{B/A}\otimes_BB'\\&\longrightarrow L^\Delta_{B'/A'}\end{aligned}
\]
give a canonical isomorphism \(\Omega^1_{B/A}\otimes_BB'\cong L^\Delta_{B'/A'}\) in \(D_\bullet(B')\).

**Proof.** By Proposition 2.5, \(c\) is a quasi-isomorphism between flat \(B\)-modules, so \(c\otimes_BB'\) is a quasi-isomorphism by Proposition 2.2 of the lesson on derived tensor products. The other map is a quasi-isomorphism by Theorem 3.1 (2). \(\square\)

**Remark 3.3.** The proof uses only that \(c\colon L^\Delta_{B/A}\to\Omega^1_{B/A}\) is a quasi-isomorphism and that \(\Omega^1_{B/A}\) is flat. The conclusion holds whenever these two conditions do.

**Corollary 3.4.** In the situation of Theorem 3.1, suppose that \(B\) and \(B'\) are degreewise symmetric algebras of flat modules over \(A\) and \(A'\); for instance, degreewise free. Then \(\Omega^1_{B/A}\to\Omega^1_{B'/A'}\) and \(\Omega^1_{B/A}\otimes_BB'\to\Omega^1_{B'/A'}\) are quasi-isomorphisms.

**Proof.** In the commutative square formed by \(L^\Delta_{B/A}\to L^\Delta_{B'/A'}\), the maps \(c\) and \(\Omega^1_{B/A}\to\Omega^1_{B'/A'}\), the vertical maps \(c\) are quasi-isomorphisms by Proposition 2.5 and the top map by Theorem 3.1 (2). So the bottom map is a quasi-isomorphism. The map \(\Omega^1_{B/A}\to\Omega^1_{B/A}\otimes_BB'\) tensors the flat module \(\Omega^1_{B/A}\) with the quasi-isomorphism \(v\), and the second statement follows by two out of three. \(\square\)

**Corollary 3.5.** Let \(A\to B\) be a map of rings of \(T\) and \(P\to B\) a quasi-isomorphism of simplicial \(A\)-algebras with \(P\) degreewise free over \(A\). Then \(\Omega^1_{P/A}\to\Omega^1_{P/A}\otimes_PB\) is a quasi-isomorphism, and there is a canonical isomorphism \(\Omega^1_{P/A}\otimes_PB\cong L_{B/A}\) in \(D_\bullet(B)\). If \(P\to P'\) is a map of two such resolutions over \(B\), the induced map \(\Omega^1_{P/A}\otimes_PB\to\Omega^1_{P'/A}\otimes_{P'}B\) is a quasi-isomorphism compatible with these isomorphisms.

**Proof.** Apply Corollary 3.2 to the square with top row \(A\to P\), bottom row \(A\to B\), \(u=1_A\) and \(v\) the augmentation: it gives \(\Omega^1_{P/A}\otimes_PB\cong L^\Delta_{B/A}\), which is \(L_{B/A}\) by Proposition 2.4 (2). The first statement is Proposition 2.2 of the lesson on derived tensor products, \(\Omega^1_{P/A}\) being flat by Proposition 2.5. For a map \(P\to P'\) over \(B\), which is a quasi-isomorphism by two out of three, Corollary 3.4 shows that \(\Omega^1_{P/A}\otimes_PP'\to\Omega^1_{P'/A}\) is a quasi-isomorphism between flat \(P'\)-modules; tensoring with \(B\) over \(P'\) gives the claim, and compatibility with the isomorphisms follows from the naturality of \(c\) and Proposition 2.4 (3). \(\square\)

## 4. The cotangent complex as a derived functor

Fix a simplicial ring \(A\) and an \(A\)-algebra \(B\). Let \(A\text{-}\mathrm{Alg}/B\) be the category of \(A\)-algebras over \(B\), \(D(A\text{-}\mathrm{Alg}/B)\) its localization at the quasi-isomorphisms, and \(\operatorname{Hotfib}(A\text{-}\mathrm{Alg}/B)\) the category of Theorem 4.2 (3) of the lesson on simplicial rings: algebras over \(B\) whose structure map is a fibration, up to homotopy over \(B\). There the quasi-isomorphisms admit a calculus of right fractions, and the localization is \(D(A\text{-}\mathrm{Alg}/B)\). Consider the functor
\[
\begin{aligned}&\Phi\colon A\text{-}\mathrm{Alg}/B\to B\text{-}\mathrm{Mod},\\&\Phi(C)=\Omega^1_{C/A}\otimes_CB,\end{aligned}
\]
and the natural map \(c_C\otimes B\colon L^\Delta_{C/A}\otimes_CB\to\Phi(C)\).

**Proposition 4.1.**

1. The functor \(C\mapsto L^\Delta_{C/A}\otimes_CB\) carries quasi-isomorphisms to quasi-isomorphisms, so it induces a functor \(L\Phi\colon D(A\text{-}\mathrm{Alg}/B)\to D_\bullet(B)\). Both this functor and \(\Phi\) carry homotopic maps over \(B\) to homotopic maps.
2. For every \(C\) in \(\operatorname{Hotfib}(A\text{-}\mathrm{Alg}/B)\), the pro-object \(C'\mapsto\Phi(C')\) of \(D_\bullet(B)\), indexed by the quasi-isomorphisms \(C'\to C\) of \(\operatorname{Hotfib}(A\text{-}\mathrm{Alg}/B)\), is essentially constant with value \(L^\Delta_{C/A}\otimes_CB\), through the maps \(c\). So \(L\Phi\), with the transformation \(c\otimes B\), is the left derived functor of \(\Phi\), in the sense dual to [[Stacks, Tag 05S9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/derived.html#derived-definition-right-derived-functor-defined)].

**Proof.** (1) Let \(f\colon C'\to C\) be a quasi-isomorphism over \(B\). Theorem 3.1 (2), applied to the square with \(u=1_A\) and \(v=f\), shows that \(L^\Delta_{C'/A}\otimes_{C'}C\to L^\Delta_{C/A}\) is a quasi-isomorphism. Both sides are flat \(C\)-modules, so tensoring with \(B\) over \(C\) gives a quasi-isomorphism by Proposition 2.2 of the lesson on derived tensor products, and that is the map \(L^\Delta_{C'/A}\otimes_{C'}B\to L^\Delta_{C/A}\otimes_CB\). A homotopy of maps of algebras over \(B\) is a family of maps of algebras in each degree, over \(B\), satisfying the relations of [[Stacks, Tag 019M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/simplicial.html#simplicial-remark-homotopy-better)]. Both functors are formed degree by degree from the triples \(A_n\to C_n\to B_n\), so they carry such families to homotopies.

(2) Let \(J\) be the full subcategory of the quasi-isomorphisms \(C'\to C\) with \(C'\) degreewise free over \(A\). It is cofinal: for a quasi-isomorphism \(C'\to C\), the composite \(P^\Delta_A(C')\to C'\to C\) lies in \(J\). Indeed \(P^\Delta_A(C')\to C'\) is a quasi-isomorphism and an epimorphism (Lemma 2.2), hence a fibration by Lemma 3.2 (2) of the lesson on simplicial rings, so \(P^\Delta_A(C')\to B\) is a fibration by Lemma 3.2 (4) there. By the calculus of right fractions, the category of quasi-isomorphisms with target \(C\) is cofiltered [[Stacks, Tag 04VH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-lemma-right-localization), [Tag 05Q4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-remark-right-localization-morphisms-colimit)], and so is its full cofinal subcategory \(J\). A map \(C''\to C'\) in \(J\) is a quasi-isomorphism between degreewise free \(A\)-algebras, so \(\Omega^1_{C''/A}\otimes_{C''}C'\to\Omega^1_{C'/A}\) is a quasi-isomorphism between flat \(C'\)-modules by Corollary 3.4, and tensoring with \(B\) over \(C'\) shows that \(\Phi(C'')\to\Phi(C')\) is a quasi-isomorphism. A pro-object indexed by a cofiltered category whose transition maps are isomorphisms is essentially constant [[Stacks, Tag 05PU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-definition-essentially-constant-diagram)], and restricting to a cofinal subcategory does not change a pro-object. Its value is \(\Phi(P^\Delta_A(C))\), which is \(\Omega^1_{P^\Delta/A}\otimes_{P^\Delta}B=L^\Delta_{C/A}\otimes_CB\), and the transition map to \(\Phi(C)\) is \(c\otimes B\). \(\square\)

For a \(B\)-module \(M\), let \(B\oplus M\) be the trivial square-zero extension, an \(A\)-algebra over \(B\). A quasi-isomorphism \(M\to M'\) induces a quasi-isomorphism \(B\oplus M\to B\oplus M'\), so \(M\mapsto B\oplus M\) induces a functor \(D_\bullet(B)\to D(A\text{-}\mathrm{Alg}/B)\). The structure map \(B\oplus M\to B\) is a fibration: on normalized complexes it is the projection \(NB\oplus NM\to NB\).

**Proposition 4.2.** For every \(B\)-module \(M\) there is an isomorphism, natural in \(M\in D_\bullet(B)\),
\[
\begin{aligned}&\operatorname{Hom}_{D_\bullet(B)}(L^\Delta_{B/A},M)\\&\quad\cong\operatorname{Hom}_{D(A\text{-}\mathrm{Alg}/B)}(B,B\oplus M).\end{aligned}
\]

**Proof.** *Strict maps.* For \(C\) in \(A\text{-}\mathrm{Alg}/B\) and a \(B\)-module \(F\), the universal properties of differentials and of trivial square-zero extensions give, degree by degree and compatibly with the simplicial maps, the bijections (4.1)
\[
\begin{aligned}&\operatorname{Hom}_B(\Omega^1_{C/A}\otimes_CB,F)\\&\quad\cong\operatorname{Der}_A(C,F)\\&\quad\cong\operatorname{Hom}_{A\text{-}\mathrm{Alg}/B}(C,B\oplus F),\end{aligned}
\]
where \(F\) is a \(C\)-module through \(C\to B\): a map of \(A\)-algebras \(C\to B\oplus F\) over \(B\) is the structure map plus an \(A\)-derivation \(C\to F\).

*Homotopies.* Let \(\operatorname{Path}(F)=\underline{\operatorname{Homs}}(\Delta[1],F)\). The functor \(\underline{\operatorname{Homs}}(\Delta[1],-)\) commutes with direct sums and products, so \(\underline{\operatorname{Homs}}(\Delta[1],B\oplus F)\) is the trivial extension of \(\underline{\operatorname{Homs}}(\Delta[1],B)\) by \(\operatorname{Path}(F)\), and the path object of \(B\oplus F\) over \(B\), formed by the paths lying over constant paths of \(B\), is \(B\oplus\operatorname{Path}(F)\). Applying (4.1) with \(\operatorname{Path}(F)\) in place of \(F\) matches homotopies of maps of \(B\)-modules with homotopies of maps of algebras over \(B\), and so the equivalence relations they generate. Hence the bijection (4.2)
\[
\begin{aligned}&\operatorname{Hom}_{\operatorname{Hot}_\bullet(B)}(\Phi(C),F)\\&\quad\cong\operatorname{Hom}_{\operatorname{Hot}(A\text{-}\mathrm{Alg}/B)}(C,B\oplus F).\end{aligned}
\]

*Localization.* By Proposition 4.1 (2) for \(C=B\), the pro-object \(\Phi(C)\), over the quasi-isomorphisms \(C\to B\) of \(\operatorname{Hotfib}(A\text{-}\mathrm{Alg}/B)\), is essentially constant with value \(L^\Delta_{B/A}\). So
\[
\begin{aligned}&\operatorname{Hom}_{D_\bullet(B)}(L^\Delta_{B/A},M)\\&\quad=\varinjlim_{C\to B}\operatorname{Hom}_{D_\bullet(B)}(\Phi(C),M).\end{aligned}
\]
By the calculus of left fractions in \(\operatorname{Hot}_\bullet(B)\) (Theorem 4.2 (1) of the lesson on simplicial rings, and Lemma 1.2 there), dually to [[Stacks, Tag 05Q4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-remark-right-localization-morphisms-colimit)],
\[
\begin{aligned}&\operatorname{Hom}_{D_\bullet(B)}(\Phi(C),M)\\&\quad=\varinjlim_{M\to F}\operatorname{Hom}_{\operatorname{Hot}_\bullet(B)}(\Phi(C),F),\end{aligned}
\]
over the quasi-isomorphisms \(M\to F\). Interchanging the two filtered colimits and using (4.2), \(\operatorname{Hom}_{D_\bullet(B)}(L^\Delta_{B/A},M)\) is
\[
\begin{aligned}&\varinjlim_{M\to F}\ \varinjlim_{C\to B}\operatorname{Hom}_{\operatorname{Hot}(A\text{-}\mathrm{Alg}/B)}(C,B\oplus F)\\&\quad=\varinjlim_{M\to F}\operatorname{Hom}_{D(A\text{-}\mathrm{Alg}/B)}(B,B\oplus F),\end{aligned}
\]
the last step by the calculus of right fractions in \(\operatorname{Hotfib}(A\text{-}\mathrm{Alg}/B)\), which contains \(B\) and \(B\oplus F\) [[Stacks, Tag 05Q4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/categories.html#categories-remark-right-localization-morphisms-colimit)]. Each quasi-isomorphism \(M\to F\) induces an isomorphism \(B\oplus M\to B\oplus F\) of \(D(A\text{-}\mathrm{Alg}/B)\), so the transition maps of the last colimit are bijections and it equals \(\operatorname{Hom}_{D(A\text{-}\mathrm{Alg}/B)}(B,B\oplus M)\). Every step is natural in \(M\). \(\square\)

So \(L^\Delta_{B/A}\) is the value at \(B\) of the left derived functor of \(C\mapsto\Omega^1_{C/A}\otimes_CB\), and it corepresents derivations of \(B\) over \(A\) in the homotopy category of algebras over \(B\).

## 5. Exercises

**Exercise 5.1.** Let \(A\to A'\) be a quasi-isomorphism of simplicial rings. Show that \(L^\Delta_{A'/A}\) is acyclic.

**Exercise 5.2.** Let \(A\) be a ring of \(T\), \(X\) a simplicial sheaf of sets and \(B=A[X]\), the simplicial \(A\)-algebra with \(B_n=A[X_n]\). Show that \(L^\Delta_{B/A}\) is quasi-isomorphic to \(B\otimes_{\mathbb Z}\mathbb Z^{(X)}\). For the augmentation \(B\to A\) sending every \(x\in X\) to \(0\), show that \(L^\Delta_{B/A}\otimes_BA\) is quasi-isomorphic to \(A\otimes_{\mathbb Z}\mathbb Z^{(X)}\), whose homotopy sheaves are the homology sheaves of \(X\) with coefficients in \(A\).

## 6. Complete solutions

**Solution 5.1.** Apply Theorem 3.1 to the square with top row \(1_A\colon A\to A\), bottom row \(A\to A'\), \(u=1_A\) and \(v\) the given quasi-isomorphism. Part (2) gives a quasi-isomorphism \(L^\Delta_{A/A}\otimes_AA'\to L^\Delta_{A'/A}\). Every \(A_n\) is the symmetric algebra of the zero module over itself, so Proposition 2.5 gives a quasi-isomorphism \(L^\Delta_{A/A}\to\Omega^1_{A/A}=0\) between flat \(A\)-modules. Tensoring with \(A'\) preserves it (Proposition 2.2 of the lesson on derived tensor products), so \(L^\Delta_{A/A}\otimes_AA'\) is acyclic, and so is \(L^\Delta_{A'/A}\).

**Solution 5.2.** Each \(B_n=A[X_n]=\operatorname{Sym}_A(A^{(X_n)})\), so Proposition 2.5 gives a quasi-isomorphism \(c\colon L^\Delta_{B/A}\to\Omega^1_{B/A}\) between flat \(B\)-modules. By the Conventions, \(\Omega^1_{B_n/A}=B_n\otimes_{\mathbb Z}\mathbb Z^{(X_n)}\), and the simplicial maps, induced by maps of sheaves of sets, match: \(\Omega^1_{B/A}=B\otimes_{\mathbb Z}\mathbb Z^{(X)}\). The augmentation is a map of simplicial algebras because the simplicial maps of \(B\) send generators to generators. By Proposition 2.2 of the lesson on derived tensor products, \(c\otimes_BA\) is a quasi-isomorphism, and \(\Omega^1_{B/A}\otimes_BA=A\otimes_{\mathbb Z}\mathbb Z^{(X)}=A^{(X)}\). The homotopy sheaves of \(A^{(X)}\) are, by definition, the homology sheaves of \(X\) with coefficients in \(A\).

## Sources

The cotangent complex of a map of simplicial rings, its computation for degreewise symmetric algebras of flat modules, its invariance under quasi-isomorphisms and its description as a derived functor that corepresents derivations are due to Illusie, in his work on the cotangent complex. The corepresentability of derivations in the homotopy category of simplicial algebras goes back to Quillen. The standard resolution, the cotangent complex of a map of sheaves of rings and the standard simplicial object of an adjunction are taken from the AI-integrated Stacks project.
