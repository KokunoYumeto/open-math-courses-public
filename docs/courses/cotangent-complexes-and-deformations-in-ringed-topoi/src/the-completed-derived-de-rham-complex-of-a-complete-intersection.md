# The completed derived de Rham complex of a complete intersection

*Written by Claude Opus 5.5 (Anthropic) on 22 October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(B=Q/I\) be a quotient of an algebra \(Q\) whose cotangent complex is its flat module of differentials, by a weakly regular ideal. The Čech nerve of \(Q\) over the base, completed along the kernel of its map to \(B\), is an algebraic model of the infinitesimal neighbourhoods of \(\operatorname{Spec}B\) in \(\operatorname{Spec}Q\) and its powers. This lesson computes its graded pieces: the first is the two-term complex \(I/I^2\to\Omega^1_Q\otimes B\), a model of the cotangent complex, and over a ring containing \(\mathbb Q\) the others are its symmetric powers. It deduces that, over such a ring, the completed Čech nerve does not depend on the presentation \(B=Q/I\) and is filtered quasi-isomorphic to the Hodge-completed derived de Rham complex of \(B\).

**Prerequisites.** [*The derived de Rham complex*](the-derived-de-rham-complex.md) (Lemmas 1.2–1.4, Definition 4.1, Theorem 4.2, Corollaries 5.3–5.4); [*Cohomology of flat formal categories with divided powers*](cohomology-of-flat-formal-categories-with-divided-powers.md) (Proposition 1.1); [*Formal categories with divided powers and the Čech–Alexander complex*](formal-categories-with-divided-powers-and-the-cech-alexander-complex.md) (Proposition 1.6, Corollary 3.4); from the AI-integrated Stacks project, divided powers and divided power envelopes [[Tags 07GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dpa.html#dpa-definition-divided-powers), [07H8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/crystalline.html#crystalline-lemma-divided-power-envelope), [07HA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/crystalline.html#crystalline-equation-divided-power-envelope)]; [*Cotangent complexes of simplicial rings*](cotangent-complexes-of-simplicial-rings.md) (Proposition 1.3, Definition 2.3, Exercise 5.1); [*Localization morphisms and the cotangent complex*](localization-morphisms-and-the-cotangent-complex.md) (Proposition 4.1); [*Weakly regular ideals*](weakly-regular-ideals.md) (Definition 2.4, Theorem 3.3); [*Weak complete intersections*](weak-complete-intersections.md) (Definition 2.1, Proposition 2.2, Theorem 4.2); [*Non-additive functors of complexes in a ringed topos*](non-additive-functors-of-complexes-in-a-ringed-topos.md) (Section 2, Lemma 4.1); [*Derived tensor products of simplicial modules*](derived-tensor-products-of-simplicial-modules.md) (Lemma 1.1, Proposition 2.2).

## Conventions

\(T\) is a topos and rings are commutative. For a map of rings \(A\to B\), \(L_{B/A}\) is the cotangent complex, \(H_0(L_{B/A})=\Omega^1_{B/A}\) [[Stacks, Tag 08UR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-H0-L-morphism-sheaves-rings)], and maps \(A\to P\to B\) give the transitivity triangle [[Tag 08SZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cotangent.html#cotangent-lemma-triangle-sheaves-rings)] and its long exact homology sequence, natural in commutative diagrams. For a surjection \(P\to B\) with kernel \(I\), \(H_0(L_{B/P})=0\) and \(H_1(L_{B/P})=I/I^2\) naturally; if \(I\) is weakly regular, \(L_{B/P}\cong(I/I^2)[1]\) (Proposition 2.2 (2) of the lesson on weak complete intersections). For a cosimplicial module \(V\), \(N(V)\) is its normalized cochain complex; for a functor \(F\) of modules and a complex \(X\) in degrees \(\geq0\), \(F(X)=NF\Gamma^\bullet X\) as in Section 2.1 of the lesson on non-additive functors, so that \(NF(V)=F(NV)\). Inverse systems of filtered complexes and filtered quasi-isomorphisms are as in Definition 4.1 of the lesson on the derived de Rham complex.

## 1. Weakly smooth algebras

**Definition 1.1.** A map of rings \(A\to Q\) of \(T\) is *weakly smooth*, and \(Q\) is weakly smooth over \(A\), if \(Q\) is flat over \(A\), \(L_{Q/A}\to\Omega^1_{Q/A}\) is a quasi-isomorphism and \(\Omega^1_{Q/A}\) is a flat \(Q\)-module.

**Proposition 1.2.**

1. A free \(A\)-algebra, or more generally the symmetric algebra of a flat \(A\)-module, is weakly smooth. For a smooth morphism of schemes \(X\to S\), \(\mathcal O_X\) is weakly smooth over \(f^{-1}\mathcal O_S\).
2. If \(Q\) is weakly smooth over \(A\) and \(Q'\) is weakly smooth over \(Q\), then \(Q'\) is weakly smooth over \(A\).
3. If \(Q\) is weakly smooth over \(A\), then \(Q\otimes_AA'\) is weakly smooth over \(A'\) for every \(A\)-algebra \(A'\). If \(Q\) and \(A'\) are weakly smooth over \(A\), so is \(Q\otimes_AA'\).

**Proof.** (1) The first case is Proposition 1.3 of the lesson on cotangent complexes of simplicial rings, with flatness of \(\operatorname{Sym}_A(E)\) and \(\Omega^1=\operatorname{Sym}_A(E)\otimes_AE\). For a smooth morphism, \(\mathcal O_X\) is flat over \(f^{-1}\mathcal O_S\), \(\Omega^1_{X/S}\) is locally free, and \(L_{X/S}\to\Omega^1_{X/S}\) is a quasi-isomorphism (Proposition 5.1 of the lesson *The cotangent complex*, on affine opens, with Proposition 3.2 of the lesson on localization morphisms).

(2) Flatness is transitive. In the triangle \(L_{Q/A}\otimes_QQ'\to L_{Q'/A}\to L_{Q'/Q}\to\), the outer terms are flat modules in degree \(0\), so \(L_{Q'/A}\) has homology only in degree \(0\), and the sequence
\[
\begin{aligned}0\to\Omega^1_{Q/A}\otimes_QQ'&\to\Omega^1_{Q'/A}\\&\to\Omega^1_{Q'/Q}\to0\end{aligned}
\]
is exact; an extension of flat modules is flat.

(3) \(Q\) is flat over \(A\), so \(\operatorname{Tor}_i^A(Q,A')=0\) for \(i>0\), and Proposition 4.1 of the lesson on localization morphisms gives \(L_{Q\otimes A'/A'}\cong L_{Q/A}\otimes_QQ\otimes_AA'\), a flat module \(\Omega^1_{Q/A}\otimes_AA'\) in degree \(0\). Flatness is stable under base change. The second statement follows from the first, with \(Q\otimes_AA'\) weakly smooth over \(A'\) and \(A'\) over \(A\), by (2). \(\square\)

## 2. The first graded piece

**Construction 2.1.** Let \(A\to Q\) be a map of rings and \(Q\to B\) a surjection with kernel \(I\). The *Čech nerve* of \(Q\) over \(A\) is the cosimplicial \(A\)-algebra \(C=C_{Q/A}\), \(C^m=Q^{\otimes_A(m+1)}\), whose cofaces insert \(1\) and whose codegeneracies multiply adjacent factors. The total multiplication \(\mu\colon C^m\to Q\) is a map of cosimplicial algebras from \(C\) to the constant \(Q\), and the coface \(\iota\colon Q\to C^m\) onto the first factor is a section of it in each degree. Put
\[
\begin{aligned}J&=\ker(C\xrightarrow{\mu}Q),\\K&=\ker(C\to Q\to B),\end{aligned}
\]
cosimplicial ideals with \(J\subseteq K\), \(J^0=0\) and \(K^0=I\). The *completed Čech nerve* \(\widehat C^K_{Q/A}\) is the inverse system of cosimplicial algebras \((C/K^r)_{r\geq1}\), filtered by the \(K^s/K^r\).

The ideal \(J\) is the augmentation ideal of the affine category \(C\) in the sense of the lessons on formal categories with divided powers, and \(J^1/(J^1)^2=\Omega^1_{Q/A}\), the class of \(d^0(q)-d^1(q)\) corresponding to \(dq\), as in those lessons.

**Lemma 2.2.** There is an exact sequence of cosimplicial \(B\)-modules
\[
\begin{aligned}0\to(J/J^2)\otimes_QB&\longrightarrow K/K^2\\&\longrightarrow I/I^2\to0,\end{aligned}
\]
with \(I/I^2\) constant, the second map induced by \(\mu\), and \(J/J^2\) a \(Q\)-module through \(C/J=Q\).

**Proof.** In each degree, \(C^m=\iota(Q)\oplus J^m\) as \(Q\)-modules through \(\iota\), and \(K^m=\iota(I)\oplus J^m\). So \((K^m)^2=\iota(I^2)+\iota(I)J^m+(J^m)^2\), with \(\iota(I^2)\subseteq\iota(Q)\) and the other terms in \(J^m\). The map \(K^m/(K^m)^2\to I/I^2\) induced by \(\mu\) is surjective, and its kernel is the image of \(J^m\), which is \(J^m/(\iota(I)J^m+(J^m)^2)\), that is, \((J^m/(J^m)^2)\otimes_QQ/I\). The maps are compatible with the cosimplicial structure because \(\mu\) is a map of cosimplicial algebras. \(\square\)

**Proposition 2.3.** Suppose \(\Omega^1_{Q/A}\) is a flat \(Q\)-module. Then the normalized cochain complex of \(K/K^2\) is the complex
\[
N(K/K^2)=\big(I/I^2\xrightarrow{\ d\ }\Omega^1_{Q/A}\otimes_QB\big)
\]
in degrees \(0\) and \(1\), with \(d(\bar f)=df\otimes1\).

**Proof.** Let \(\bar C\) be the divided power envelope of the affine category \(C\), with augmentation ideal \(\bar J\) (Corollary 3.4 of the lesson on formal categories with divided powers). In each degree \(m\), the map \(C^m/(J^m)^2\to\bar C^m/(\bar J^m)^{[2]}\) is an isomorphism. Indeed, the ideal \(J^m/(J^m)^2\) of \(C^m/(J^m)^2\) has square zero, so \(\gamma_1=\mathrm{id}\) and \(\gamma_n=0\) for \(n\geq2\) define divided powers on it, the axioms of [Tag 07GL] reducing to identities between products of at least two of its elements. The universal property of the envelope [Tag 07H8] gives a map \(\bar C^m\to C^m/(J^m)^2\) of \(C^m\)-algebras compatible with the divided powers, which kills \((\bar J^m)^{[2]}\); and \(\bar C^m\) is generated over \(C^m\) by the divided powers \(\gamma_n(f)\), \(f\in J^m\) [Tag 07HA], which lie in \((\bar J^m)^{[2]}\) for \(n\geq2\). So \(J/J^2=\bar J/\bar J^{[2]}\) as cosimplicial modules, and the module of differentials of \(\bar C\) is \(J^1/(J^1)^2=\Omega^1_{Q/A}\), which is flat. By Proposition 1.1 (1) of the lesson on cohomology of flat formal categories, applied to \(\bar C\), \(N(J/J^2)\) is \(\Omega^1_{Q/A}\) placed in degree \(1\); tensoring with \(B\) over \(Q\), which commutes with normalization, \(N((J/J^2)\otimes_QB)\) is \(\Omega^1_{Q/A}\otimes_QB\) in degree \(1\). The normalization of the constant \(I/I^2\) is \(I/I^2\) in degree \(0\). Normalization is exact, so Lemma 2.2 gives \(N^0(K/K^2)=K^0/(K^0)^2=I/I^2\), \(N^1(K/K^2)=\Omega^1_{Q/A}\otimes_QB\) and \(N^m=0\) for \(m\geq2\). The differential is the coboundary \(d^0-d^1\colon K^0\to K^1\), which lands in \(J^1\), followed by the class in \(J^1/(J^1)^2\otimes_QB=\Omega^1_{Q/A}\otimes_QB\); by the identification of Construction 2.1 this class is \(df\otimes1\). \(\square\)

**Corollary 2.4.** In the situation of Proposition 2.3, suppose moreover that \(Q\) is weakly smooth over \(A\). Then the cohomology of \(N(K/K^2)\) is \(H_1(L_{B/A})\) in degree \(0\) and \(\Omega^1_{B/A}\) in degree \(1\), and a map of such presentations \(Q\to Q'\), over \(A\) and \(B\), induces a quasi-isomorphism of these complexes. If \(I\) is weakly regular, \(N(K/K^2)\) is quasi-isomorphic to \(L_{B/A}[-1]\).

**Proof.** In the long exact sequence of the triangle of \(A\to Q\to B\), \(H_1(L_{Q/A}\otimes_QB)=0\) because \(L_{Q/A}\) is a flat module in degree \(0\), so
\[
\begin{aligned}0&\to H_1(L_{B/A})\to H_1(L_{B/Q})=I/I^2\\&\to\Omega^1_{Q/A}\otimes_QB\to\Omega^1_{B/A}\to0\end{aligned}
\]
is exact. The middle map is \(d\) (Lemma 4.1 of the lesson on weak complete intersections). This exact sequence is natural for maps of presentations, which therefore induce the identity on \(H_1(L_{B/A})\) and on \(\Omega^1_{B/A}\), hence a quasi-isomorphism. If \(I\) is weakly regular, \(L_{B/A}\) is isomorphic to the complex \(I/I^2\to\Omega^1_{Q/A}\otimes_QB\) in degrees \(-1\), \(0\) by Theorem 4.2 of the lesson on weak complete intersections, which is \(N(K/K^2)[1]\). \(\square\)

**Proposition 2.5 (arbitrary affine categories).** Let \(C\) be an affine \(A\)-category, identified with its nerve, a cosimplicial \(A\)-algebra, let \(J\) be its augmentation ideal, the kernel of the augmentation \(\mu\colon C\to C^0\) induced by the maps \([m]\to[0]\), and put \(U=J^1\). Let \(C\to B\) be a surjective map of cosimplicial \(A\)-algebras onto a constant \(B\), with kernel \(K\), and \(I=K^0\).

1. There is an exact sequence of cosimplicial \(B\)-modules \(0\to(J/J^2)\otimes_{C^0}B\to\) \(K/K^2\to I/I^2\to0\), with \(I/I^2\) constant.
2. If \(U/U^2\) is a flat \(C^0\)-module, \(N(K/K^2)\) is the complex \(I/I^2\xrightarrow{\ d\ }(U/U^2)\otimes_{C^0}B\) in degrees \(0\) and \(1\), where \(d\) is induced by \(d^0-d^1\colon C^0\to U\).

No condition on \(I\) is needed.

**Proof.** The map \(C\to B\) is \(\mu\) followed by its component \(C^0\to B\) of degree \(0\): it is compatible with \(C(t)=\mu^m\) for \(t\colon[m]\to[0]\). So \(J\subseteq K\) and \(K^0=I\). For a map \(v\colon[0]\to[m]\), \(\iota=C(v)\) is a section of \(\mu^m\), so \(C^m=\iota(C^0)\oplus J^m\) as \(C^0\)-modules through \(\iota\); on \(J/J^2\) the \(C^0\)-module structures through the various \(C(v)\) agree, since \(C(v)(a)-C(v')(a)\) lies in \(J^m\). With \(\mu\), \(\iota\), \(C^0\) and \(U/U^2\) in place of the total multiplication, the first coface, \(Q\) and \(\Omega^1_{Q/A}\), the proofs of Lemma 2.2 and Proposition 2.3 apply word for word. \(\square\)

## 3. Characteristic zero: the graded pieces

From now on \(A\) is a ring of \(T\) in which every nonzero integer is invertible, \(Q\) is weakly smooth over \(A\), and \(I\) is weakly regular. Then \(B\) is a weak complete intersection over \(A\) (Theorem 4.2 of the lesson on weak complete intersections). Over such a ring every ideal has a unique divided power structure, \(x\mapsto x^n/n!\), so the Čech nerve is its own divided power envelope along \(J\), divided powers of ideals are powers, and \(\Gamma=\operatorname{Sym}\) as functors of modules.

**Proposition 3.1.**

1. For every \(m\), \(K^m\) is a weakly regular ideal of \(C^m\), and the multiplication from \(\operatorname{Sym}^r_B(K^m/(K^m)^2)\) to \((K^m)^r/(K^m)^{r+1}\) is an isomorphism for every \(r\).
2. The complex \(N(K^r/K^{r+1})\) is \(\operatorname{Sym}^r\) of the complex \(I/I^2\xrightarrow{d}\Omega^1_{Q/A}\otimes_QB\), and it is quasi-isomorphic to \(\Lambda^rL_{B/A}[-r]\); it vanishes in degrees \(>r\).

**Proof.** (1) \(C^m\) is weakly smooth over \(A\) by Proposition 1.2 (3) and (2), and \(C^m\to B\) is surjective with kernel \(K^m\). Since \(B\) is a weak complete intersection over \(A\), Theorem 4.2 of the lesson on weak complete intersections shows that \(K^m\) is weakly regular, and Theorem 3.3 (1) of the lesson on weakly regular ideals gives the isomorphism.

(2) By (1), \(K^r/K^{r+1}=\operatorname{Sym}^r_B(K/K^2)\) as cosimplicial modules, so \(N(K^r/K^{r+1})\) is \(N\operatorname{Sym}^r(K/K^2)=\operatorname{Sym}^r(N(K/K^2))\), the latter in the sense of Section 2.1 of the lesson on non-additive functors, and \(N(K/K^2)\) is the complex of Proposition 2.3, of flat modules: \(I/I^2\) by weak regularity, \(\Omega^1_{Q/A}\otimes_QB\) by base change. As \(\operatorname{Sym}^r=\Gamma^r\), Corollary 5.3 of the lesson on the derived de Rham complex identifies it with \(\operatorname{Kos}^\bullet(d)_r\), and Corollary 5.4 there with \(\Lambda^rL_{B/A}[-r]\). The vanishing is the dual of Proposition 2.1 of the lesson on non-additive functors, \(\operatorname{Sym}^r\) having degree \(r\) and \(N(K/K^2)\) living in degrees \([0,1]\). \(\square\)

**Corollary 3.2.** Let \(Q'\to B\) and \(Q''\to B\) be two such presentations, with kernels \(I'\), \(I''\). There is a canonical chain of filtered quasi-isomorphisms between \(\widehat C^{K'}_{Q'/A}\) and \(\widehat C^{K''}_{Q''/A}\), after normalization.

**Proof.** \(Q=Q'\otimes_AQ''\) is weakly smooth over \(A\) by Proposition 1.2 (3), maps onto \(B\), and its kernel is weakly regular by Theorem 4.2 of the lesson on weak complete intersections. The maps \(Q'\to Q\leftarrow Q''\) over \(B\) induce maps of the completed Čech nerves, compatible with the filtrations. On the first graded piece they are quasi-isomorphisms after normalization by Corollary 2.4. On the \(r\)-th graded piece they are \(\operatorname{Sym}^r\) of these, by Proposition 3.1, which are quasi-isomorphisms by Lemma 4.1 of the lesson on non-additive functors, the complexes being bounded and flat. By induction on the length of the filtration, the maps are quasi-isomorphisms on every \(N(K^s/K^r)\). \(\square\)

## 4. The comparison theorem

**Theorem 4.1.** Let \(A\) be a ring in which every nonzero integer is invertible, \(Q\) a weakly smooth \(A\)-algebra and \(B=Q/I\) with \(I\) weakly regular. There is a canonical chain of filtered quasi-isomorphisms between the Hodge-completed derived de Rham complex \(\widehat{L\Omega}^\bullet_{B/A}\) and the normalized completed Čech nerve \(N(\widehat C^K_{Q/A})\), filtered by the powers of \(K\).

**Proof.** By Corollary 3.2 we may choose the presentation. Let \(P=P_A(B)\) be the standard resolution and take \(Q=P_0=A[B]\), free over \(A\). For every \(n\), \(P_n\) is free over \(A\), hence weakly smooth, and \(P_n\to B\) is surjective with kernel \(I_n\), weakly regular because \(B\) is a weak complete intersection. The Čech nerves \(C_{P_n/A}\) form a mixed object, simplicial in \(n\) and cosimplicial in \(m\), with cosimplicial ideals \(J_n\subseteq K_n\) as in Construction 2.1. All realizations below are realizations in the direction \(n\) (Definition 1.1 of the lesson on the derived de Rham complex) of normalized cochains in the direction \(m\), taken on the quotients by the filtrations.

*The Hodge side.* By Theorem 4.2 of the lesson on the derived de Rham complex, the realization of \(N(C_{P/A}/J^r)\), filtered by the \(J^s\), is filtered quasi-isomorphic to \(L\Omega^\bullet_{B/A}/F^r\); here the divided power envelopes are the Čech nerves themselves.

*The map (\*) from the \(J\)-adic to the \(K\)-adic completion*, induced by \(J\subseteq K\). Fix \(m\). By Proposition 1.1 (a) of the lesson on cohomology of flat formal categories, \(J^r/J^{r+1}=\operatorname{Sym}^r_{P_n}(J/J^2)\) in degree \(m\), and by Proposition 3.1 (1), \(K^r/K^{r+1}=\operatorname{Sym}^r_B(K/K^2)\). By Lemma 2.2, \(J/J^2\to K/K^2\) factors as \(J/J^2\to(J/J^2)\otimes_{P_n}B\to K/K^2\), the second map injective with cokernel \(I_n/I_n^2\). As simplicial modules in \(n\): the first map is a quasi-isomorphism because \(J/J^2\) is flat over \(P_n\) and \(P\to B\) is a quasi-isomorphism (Proposition 2.2 of the lesson on derived tensor products); and \(n\mapsto I_n/I_n^2\) is acyclic. Indeed, the bisimplicial module \(L_{B/P}\), with columns \(L_{B/P_n}\), has an acyclic diagonal by Exercise 5.1 of the lesson on cotangent complexes of simplicial rings, \(P\to B\) being a quasi-isomorphism; its columns are naturally quasi-isomorphic to \((I_n/I_n^2)[1]\), through \(L_{B/P_n}\to\tau_{\leq1}L_{B/P_n}\leftarrow H_1(L_{B/P_n})[1]\); so by Lemma 1.2 of the lesson on the derived de Rham complex and the diagonal lemma (Lemma 1.1 of the lesson on derived tensor products), \(n\mapsto I_n/I_n^2\) is acyclic. Hence \(J/J^2\to K/K^2\) is a quasi-isomorphism of simplicial modules in every degree \(m\), between flat \(P\)- and \(B\)-modules, and so is \(\operatorname{Sym}^r\) of it, through
\[
\begin{aligned}\operatorname{Sym}^r_P(J/J^2)&\to\operatorname{Sym}^r_P(J/J^2)\otimes_PB\\&=\operatorname{Sym}^r_B(J/J^2\otimes_PB)\\&\to\operatorname{Sym}^r_B(K/K^2)\end{aligned}
\]
(Lemma 4.1 of the lesson on non-additive functors). The normalized cochains of both graded pieces vanish in degrees \(m>r\) (Proposition 3.1 (2), and the same argument for \(J\), whose \(N(J/J^2)\) lives in degree \(1\)), and the normalized cochains are natural direct summands. Filtering by \(m\), a finite filtration, and applying Lemma 1.2 of the lesson on the derived de Rham complex in the direction \(n\), (\*) is a quasi-isomorphism on every graded piece, hence on every \(N(\cdot/F^r)\) restricted to \(F^s\).

*The map (\*\*) from the constant object.* The degeneracies \(P_0\to P_n\) form a map of simplicial algebras from the constant \(P_0\) to \(P\), over \(B\), and induce maps of completed Čech nerves. For each \(n\), \(P_0\to P_n\) is a map of presentations, so by Corollary 2.4 it induces a quasi-isomorphism on the normalized first graded pieces, and, as in Corollary 3.2, on all \(N(K^s/K^r)\). By Lemma 1.2 of the lesson on the derived de Rham complex, the realizations are quasi-isomorphic, and by Lemma 1.4 there the realization of the constant object is homotopy equivalent to \(N(\widehat C^K_{P_0/A})\).

Composing, \(\widehat{L\Omega}^\bullet_{B/A}\) is connected to \(N(\widehat C^K_{Q/A})\) by filtered quasi-isomorphisms of inverse systems. \(\square\)

So, over a ring containing \(\mathbb Q\), the Hodge-completed derived de Rham complex of a weak complete intersection \(B=Q/I\) is computed by the formal completion of the Čech nerve of any weakly smooth presentation, and its graded pieces \(\Lambda^rL_{B/A}[-r]\) are the symmetric powers of the two-term complex \(I/I^2\to\Omega^1_{Q/A}\otimes_QB\).

**Remark 4.2.** For a morphism of schemes \(f\colon X\to S\) over \(\mathbb Q\) that factors as a closed immersion \(X\to Y\), defined by a weakly regular ideal, followed by a smooth \(Y\to S\), Theorem 4.1 applied to \(A=f^{-1}\mathcal O_S\), \(Q\) the inverse image of \(\mathcal O_Y\) and \(B=\mathcal O_X\), on the topos of \(X\), identifies \(\widehat{L\Omega}^\bullet_{X/S}\) with the formal completion along \(X\) of the Čech nerve of \(Y\) over \(S\).

## 5. Exercises

**Exercise 5.1.** Let \(A\) be a ring containing \(\mathbb Q\), \(f\in A\) a nonzerodivisor and \(B=A/fA\). Using the presentation \(Q=A\), show that \(\widehat{L\Omega}^\bullet_{B/A}\) is filtered quasi-isomorphic to the inverse system \((A/f^rA)_{r\geq1}\), filtered by the \(f^sA/f^rA\).

**Exercise 5.2.** Let \(A\) be a ring containing \(\mathbb Q\), \(Q=A[x]\) and \(B=Q/(x^2)\). Write the complex \(N(K/K^2)\) of Proposition 2.3 and compute its cohomology. Deduce \(H_1(L_{B/A})\) and \(\Omega^1_{B/A}\).

## 6. Complete solutions

**Solution 5.1.** \(Q=A\) is weakly smooth over \(A\), and \(I=fA\) is weakly regular (Proposition 4.2 of the lesson on weakly regular ideals). The Čech nerve of \(A\) over \(A\) is the constant cosimplicial algebra \(A\), with \(J=0\) and \(K=fA\) in every degree. So \(\widehat C^K_{A/A}\) is the constant cosimplicial inverse system \((A/f^rA)_r\), whose normalized cochains are \(A/f^rA\) in degree \(0\), filtered by the \(f^sA/f^rA\). Theorem 4.1 gives the claim. In particular \(H^0(L\Omega^\bullet_{B/A}/F^r)\cong A/f^rA\), which makes Exercise 6.2 of the lesson on the derived de Rham complex explicit.

**Solution 5.2.** \(I=(x^2)\), \(I/I^2\) is free over \(B\) on the class of \(x^2\), and \(\Omega^1_{Q/A}\otimes_QB\) is free on \(dx\). The differential sends \(\overline{x^2}\) to \(2x\,dx\), and \(b\,\overline{x^2}\mapsto2bx\,dx\). Since \(2\) is invertible, its kernel is \(xB\cdot\overline{x^2}\cong A\) and its cokernel is \(B\,dx/xB\,dx\cong A\). So \(H^0(N(K/K^2))\cong A\), generated by the class of \(x^3\), and \(H^1\cong A\), generated by \(dx\). By Corollary 2.4, \(H_1(L_{B/A})\cong A\) and \(\Omega^1_{B/A}\cong B\,dx/(2x\,dx)=A\,dx\).

## Sources

Weakly smooth algebras, the computation of the first graded piece of the completed Čech nerve of a presentation, its symmetric powers, the independence of the presentation and the comparison with the Hodge-completed derived de Rham complex are due to Illusie, in his work on the cotangent complex; he states Proposition 2.5 (2) for a weakly regular \(I\). In characteristic \(p\) the same comparison, for smooth presentations with regular kernels, rests on Berthelot's description of the graded ring of the divided power envelope of a regular ideal, and identifies the derived de Rham complex with crystalline cohomology; Bhatt, *p-adic derived de Rham cohomology* ([arXiv:1204.6560](https://arxiv.org/abs/1204.6560)), Section 3, and *Completions and derived de Rham cohomology* ([arXiv:1207.6193](https://arxiv.org/abs/1207.6193)) extend these comparisons.
