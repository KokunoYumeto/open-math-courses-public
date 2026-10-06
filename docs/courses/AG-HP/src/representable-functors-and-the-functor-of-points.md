# Representable functors and the functor of points

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A parameter space should classify families as well as individual objects. For example, a morphism from a scheme \(T\) to projective space specifies an invertible sheaf on \(T\) together with generating sections. When \(T\) has nilpotents, this description also detects infinitesimal changes. Looking only at points over fields would discard that information.

This lesson develops a practical method for constructing parameter spaces. First describe what a family over \(T\) is, including its pullback along every morphism \(T'\to T\). Then find conditions selecting open parts of that family. If those parts have explicit parameter spaces and families glue uniquely, their spaces glue too. We apply this method to projective space and to projectivizations of arbitrary quasi-coherent modules. A final example constructs a parameter space for finite subschemes of the affine line.

We assume schemes, sheaf pullback, symmetric algebras, the affine and projective spectrum constructions, and the gluing theorem for schemes. Yoneda's lemma is a prerequisite: natural transformations \(h_X\to F\) correspond to elements of \(F(X)\). Basic references are [Stacks] and [Vakil]. The proofs below use these prerequisites to establish the representability statements themselves.

## 1 Families and equations

Fix a base scheme \(S\). A functor of families is a contravariant functor

\[
F:(\operatorname{Sch}/S)^{\mathrm{op}}\longrightarrow\operatorname{Sets}.
\]

For \(f:T'\to T\), write \(f^*\xi\) for the image of \(\xi\in F(T)\). A scheme \(X\) over \(S\) represents \(F\) if there is a natural bijection

\[
\operatorname{Hom}_S(T,X)\simeq F(T)
\]

for every \(S\)-scheme \(T\). The element corresponding to \(\operatorname{id}_X\) is the universal family. Its pullback is every family, in exactly one way.

The words “in exactly one way” apply to morphisms into the parameter space. A moduli problem formulated as isomorphism classes may have objects with automorphisms; the resulting class functor can lose the descent information carried by those automorphisms. We will encounter this issue for line bundles.

For instance, \(\mathbb A^1_S\) represents \(T\mapsto\Gamma(T,\mathcal O_T)\). Over an affine part of \(S\), a map into the affine line is a homomorphism from a polynomial algebra, determined by the image of its variable. These homomorphisms agree over overlaps and give the assertion for arbitrary \(T\). Addition of sections makes this functor a group functor, denoted \(\mathbb G_a\).

The open subscheme \(\mathbb G_m\subset\mathbb A^1_S\) represents invertible global sections. Likewise,

\[
\operatorname{GL}_{n,S}
=\operatorname{Spec}_S\mathcal O_S[x_{ij},\det(x_{ij})^{-1}]
\]

represents invertible \(n\)-by-\(n\) matrices. The inverse exists precisely when the determinant is a unit, by the adjugate identity. For a positive integer \(m\), the equation \(u^m=1\) defines the closed subgroup \(\mu_m\subset\mathbb G_m\). This construction works even when \(m\) is not invertible on \(S\). For example, over a field of characteristic \(p\), the coordinate ring of \(\mu_p\) is \(k[v]/(v^p)\), with \(v=u-1\). Its unique geometric point conceals a nonreduced scheme. Families over rings recover it.

## 2 Conditions that survive every test scheme

A morphism of functors \(G\to F\) is **representable** if, for every scheme \(T\) and every transformation \(h_T\to F\), the fibre product \(h_T\times_F G\) is represented by a scheme. By Yoneda, the test transformation amounts to a family \(\xi\in F(T)\).

An **open subfunctor** \(G\subset F\) is a subfunctor whose pullback to every \((T,\xi)\) is an open subscheme \(U_\xi\subset T\). Thus for every \(a:T'\to T\),

\[
a^*\xi\in G(T')
\quad\Longleftrightarrow\quad
a\text{ factors through }U_\xi.
\]

A **closed subfunctor** has the same definition with closed subschemes. Neither definition means merely that a subset of field-valued points looks open or closed. The condition includes arbitrary base change, including nilpotent test schemes.

**Proposition 2.1.** An open or closed subfunctor of \(h_X\) is represented by an open or closed subscheme of \(X\), respectively. Fibre products of representable functors over a representable functor are representable.

**Proof.** Test the subfunctor against \(\operatorname{id}_X\in h_X(X)\). The resulting subscheme \(Z\subset X\) has, by definition, exactly the morphisms into \(X\) that belong to the subfunctor. This identifies \(h_Z\) with it, naturally in every test scheme. For the second assertion, Yoneda identifies the transformations with morphisms \(X\to B\) and \(Y\to B\). The defining universal property of \(X\times_B Y\) identifies its points with \(h_X\times_{h_B}h_Y\). \(\square\)

For a concrete open condition, let \(q:\mathcal O_T^{n+1}\to L\) be a surjection with \(L\) invertible, and put \(s_i=q(e_i)\). The condition that \(s_i\) generate \(L\) selects an open subscheme of \(T\). On a trivialization of \(L\), it is the nonvanishing locus of the function expressing \(s_i\). These loci glue and commute with base change. A pointwise formulation and a functorial formulation agree here because a section generates a line bundle exactly where its residue is nonzero.

There is no corresponding general shortcut for closed conditions. A closed subscheme carries an ideal, not just its zero set. The two closed subschemes \(V(x)\) and \(V(x^2)\) of \(\mathbb A^1_k\) have the same geometric points, but the morphism defined by \(x\mapsto\epsilon\) on \(k[\epsilon]/(\epsilon^2)\) factors only through the latter.

## 3 Quotients of rank one and projective coordinates

Let \(E\) be a quasi-coherent \(\mathcal O_S\)-module. Define \(Q_E(T)\) to be the isomorphism classes of surjections

\[
q:f^*E\longrightarrow L,
\qquad f:T\longrightarrow S,
\]

where \(L\) is invertible. An isomorphism between \((L,q)\) and \((L',q')\) is an isomorphism \(a:L\to L'\) satisfying \(aq=q'\). Such an isomorphism is unique if it exists, since \(q\) is surjective. Pullback preserves surjectivity and invertibility, so this is a functor.

We use the quotient convention

\[
\mathbb P(E)=\operatorname{Proj}_S(\operatorname{Sym}_{\mathcal O_S}E).
\]

There is no finite-generation or local-freeness assumption in the next result. Those hypotheses give additional geometric properties, rather than the functorial description.

**Theorem 3.1.** The scheme \(\mathbb P(E)\) represents \(Q_E\). Its universal quotient is

\[
\pi^*E\twoheadrightarrow\mathcal O_{\mathbb P(E)}(1).
\]

**Proof.** Work first over \(S=\operatorname{Spec}A\), with \(E=\widetilde M\), and set \(B=\operatorname{Sym}_A M\). For \(e\in M=B_1\), the standard affine open \(D_+(e)\) has coordinate algebra

\[
C_e=(B[e^{-1}])_0.
\]

It is generated over \(A\) by the degree-zero fractions \(m/e\), for \(m\in M\). Indeed, every homogeneous element of degree \(d\) is a sum of products of \(d\) elements of \(M\), and division by \(e^d\) expresses it as a polynomial in these fractions. The statement includes all relations of \(B\).

On \(D_+(e)\), the degree-one localization \((B[e^{-1}])_1\) is free of rank one, generated by \(e\). Multiplication by \(e\) identifies it with \(C_e\). Consequently \(\mathcal O(1)\) is invertible on these opens, and the map from \(M\) to this line bundle is surjective there: the element \(e\) is already a generator. Because \(B\) is generated in degree one, the opens \(D_+(e)\) cover \(\operatorname{Proj}B\).

Now take \((L,q)\in Q_E(T)\). For each \(e\in M\), let \(T_e\) be the open where \(q(e)\) generates \(L\). These opens cover \(T\). At a point, surjectivity onto the stalk of \(L\) implies that some image of a local generator of the pullback of \(M\) has unit coefficient. Since the elements of \(M\) generate that pullback, one of their images has this property.

On \(T_e\), send \(m/e\) to \(q(m)/q(e)\). More explicitly, the graded map \(B\otimes_A\mathcal O_T\to\bigoplus_{d\geq0}L^{\otimes d}\) induced by \(q\), followed by trivialization using \(q(e)\), respects every relation in \(C_e\). It defines a morphism \(T_e\to D_+(e)\). On \(T_e\cap T_{e'}\), the ratio \(q(e')/q(e)\) is a unit. Replacing denominators gives the same maps on the projective overlap. The maps therefore glue to \(a:T\to\operatorname{Proj}B\).

Pulling back the universal quotient along \(a\) recovers \(q\), as is visible on each trivialization \(T_e\). Conversely, a morphism to \(\operatorname{Proj}B\) pulls back this quotient. Its restrictions to the inverse images of \(D_+(e)\) are determined by the fractions \(m/e\). Applying the construction again returns the original morphism. Isomorphic quotient pairs give the same fractions, so the construction descends to isomorphism classes. It is compatible with every pullback.

For general \(S\), perform this construction on affine opens. Symmetric algebra, localization, and the above fraction maps are compatible with restriction. The morphisms glue, and both inverse assertions can be checked on this cover. This proves the natural bijection on all \(S\)-schemes. \(\square\)

In particular \(E=\mathcal O_S^{n+1}\) gives \(\mathbb P^n_S\). A family consists of \(n+1\) sections of a line bundle with no common zero. On the chart where \(s_i\) generates, its coordinates are \(s_j/s_i\), for \(j\ne i\). On a chart overlap,

\[
\frac{s_j}{s_k}=\frac{s_j/s_i}{s_k/s_i}.
\]

This explains why a single global tuple of functions modulo a single global scalar does not describe every \(T\)-point: the line bundle need not be trivial.

If \(V\) is a finite-dimensional vector space, \(\mathbb P(V)\) in this convention parametrizes one-dimensional quotients of \(V\). A quotient dualizes to a line in \(V^\vee\). Hence lines in \(V\), viewed as subspaces, are parametrized by \(\mathbb P(V^\vee)\). Over a scheme, the corresponding family is a line subbundle whose quotient is locally free. An arbitrary rank-one subsheaf is insufficient: its cokernel may fail to be locally free, and pullback may destroy injectivity.

For example, the inclusion \(tA\subset A\), for \(A=k[t]\), is an inclusion of abstractly free rank-one modules. Its pullback to \(t=0\) is the zero map. It is not a line subbundle defining a family of lines.

## 4 The passage from charts to a scheme

A Zariski sheaf \(F\) is a functor for which compatible families on an open cover of \(T\) glue uniquely to an element of \(F(T)\). Every \(h_X\) is such a sheaf, by gluing morphisms. Suppose \(F_i\subset F\) are open subfunctors. They **cover** \(F\) if for every \(\xi\in F(T)\) their associated opens \(U_{i,\xi}\) cover \(T\). This is local membership, not the assertion that every entire family lies in one chart.

**Theorem 4.1.** If \(F\) is a Zariski sheaf and has a set of representable open subfunctors covering it, then \(F\) is representable.

**Proof.** Write \(F_i=h_{X_i}\). The overlap functor \(F_i\times_F F_j\) is represented by an open subscheme \(X_{ij}\subset X_i\), because \(F_j\to F\) is an open subfunctor. Interchanging the indices represents the same functor by \(X_{ji}\subset X_j\). Yoneda supplies a unique isomorphism \(X_{ij}\simeq X_{ji}\).

The triple overlap is \(F_i\times_F F_j\times_F F_k\). Both compositions from its realization in \(X_i\) to its realization in \(X_k\) induce its identity transformation. Yoneda therefore makes them equal. Scheme gluing gives \(X\) with these open charts and transition maps.

The universal elements \(\xi_i\in F(X_i)\) agree on overlaps, since the overlap identifications were defined through \(F\). The sheaf axiom gives \(\xi\in F(X)\), hence a natural transformation \(h_X\to F\). For \(\eta\in F(T)\), use the open cover \(U_{i,\eta}\) of \(T\). Membership in \(F_i\) gives a unique map \(U_{i,\eta}\to X_i\). On pairwise overlaps the resulting maps factor through \(X_{ij}\) and coincide there, since both represent the restriction of \(\eta\). They glue to \(a:T\to X\) with \(a^*\xi=\eta\).

For uniqueness, any such \(a\) has inverse image of \(X_i\) equal to \(U_{i,\eta}\): this is the defining base-change property of the open subfunctor. Its restriction is the already determined map into \(X_i\). Thus \(a\) is unique. \(\square\)

For quotient pairs \((L,q)\), the sheaf property holds despite taking isomorphism classes. Isomorphisms preserving a surjection are unique. Consequently the isomorphisms between pairs on overlaps automatically satisfy the cocycle condition. Line bundles and their maps glue. In contrast, a bare line bundle has scalar automorphisms; specifying only its isomorphism class does not specify overlap identifications.

The theorem does not imply that \(X\) is separated. Gluing two copies of \(\mathbb A^1_k\) by the identity on \(\mathbb G_m\) produces the affine line with doubled origin. Its representable functor has an open cover by two affine representables. Representability is a local construction; separation is a further compatibility condition on the diagonal.

## 5 Two instructive moduli problems

**Proposition 5.1.** The functor \(T\mapsto\operatorname{Pic}(T)\) on \(S\)-schemes is not representable if \(S\) is nonempty.

**Proof.** Choose a point \(s\in S\) and view \(T=\mathbb P^1_{\kappa(s)}\) as an \(S\)-scheme. Its line bundles \(\mathcal O_T\) and \(\mathcal O_T(1)\) restrict to isomorphic bundles on each of the two standard affine opens. They are not isomorphic on \(T\). Indeed, \(\mathcal O(1)\) has a two-dimensional space of global sections, whereas \(\mathcal O\) has a one-dimensional space. Thus two different elements of \(\operatorname{Pic}(T)\) have the same restrictions on a cover. The functor fails the uniqueness part of the sheaf axiom, which every representable functor satisfies. \(\square\)

The empty base is an exception: its category of schemes contains only the empty scheme. More generally, every line bundle is locally trivial, so the Zariski sheafification of this absolute class functor is the one-element sheaf. Relative Picard functors instead compare line bundles on \(X_T\) modulo those pulled back from \(T\). The fixed space \(X\) supplies information that does not disappear under localization of the parameter scheme.

Here is a moduli problem with a particularly explicit answer. Define \(H_d(T)\) to be closed subschemes \(Z\subset\mathbb A^1_T\) such that \(Z\to T\) is finite locally free of rank \(d\). We take \(d\geq1\); for \(d=0\), the empty subscheme is the only family. Finiteness is part of the definition, and “flat over the base” always means the parameter scheme \(T\).

**Theorem 5.2.** The functor \(H_d\) is represented by \(\mathbb A^d_S\), with universal equation

\[
x^d+a_{d-1}x^{d-1}+\cdots+a_0=0.
\]

**Proof.** Over \(T=\operatorname{Spec}A\), a family is a quotient \(B=A[x]/I\) that is finite locally free of rank \(d\) as an \(A\)-module. On every residue field, a quotient of the polynomial ring having dimension \(d\) is the quotient by a unique monic polynomial of degree \(d\). Hence \(1,x,\ldots,x^{d-1}\) is a basis of every residue-field fibre of \(B\).

The map \(A^d\to B\) defined by these powers is an isomorphism. To see this, localize at a prime of \(A\), choose a basis of the free rank-\(d\) module \(B\), and use its invertible determinant modulo the maximal ideal. The determinant is then a unit in that local ring. The map is an isomorphism at every prime, hence globally.

There are unique coefficients expressing \(x^d\) in this basis. Let \(f=x^d+\sum_{i<d}a_ix^i\) be the resulting relation. Division by a monic polynomial over any ring gives a free rank-\(d\) quotient \(A[x]/(f)\), with precisely that basis. Its surjection onto \(B\) sends a basis to a basis and is an isomorphism. Thus \(I=(f)\).

Conversely, every monic polynomial of degree \(d\) gives such a quotient. Both constructions commute with arbitrary change of \(A\). Over a nonaffine \(T\), the coefficients on affine opens agree by uniqueness; they glue to global sections of \(\mathcal O_T\). These sections are exactly the morphisms \(T\to\mathbb A^d_S\). \(\square\)

For \(d=2\), the equation \(x^2-t=0\) gives a finite free family over \(k[t]\). Its special fibre is a double point. Over a field of characteristic different from two, many other fibres consist of two distinct geometric points. The parameter space keeps both kinds of fibre within one family.

## 6 Exercises

1. **Basic.** Identify the universal element of \(\mathbb G_m\). Prove directly that it represents invertible global sections on arbitrary schemes, and identify the condition defining \(\mu_m\).

2. **Intermediate.** Construct the family of degree-three subschemes of \(\mathbb A^1\) defined by \(x^3-bx-c\). Explain why a fibre can change its number of geometric points without leaving the finite locally free moduli problem.

3. **Intermediate.** On the two standard affine opens of \(\mathbb P^1_k\), write the transition function for \(\mathcal O(1)\). Use it to explain why the class functor of line bundles loses information. Contrast this with the pair consisting of \(\mathcal O(1)\) and its two generating sections.

4. **Intermediate.** Let \(E\) be locally free of rank \(n+1\). Construct the charts of \(Q_E\) after trivializing \(E\), and compute their transitions. Determine which line bundle pulls back from \(\mathcal O_{\mathbb P(E)}(1)\).

5. **Advanced.** Let \(F\) be an fpqc sheaf on affine \(S\)-schemes. Suppose it has a Zariski cover by subfunctors represented by schemes, with open pullbacks tested on affine schemes. Prove that it has a unique extension as a Zariski sheaf to all \(S\)-schemes, and that this extension is representable. Explain the qualification “as a Zariski sheaf.”

## 7 Solutions

**1.** On \(\mathbb G_m=\operatorname{Spec}_S\mathcal O_S[u,u^{-1}]\), the universal element is \(u\). An invertible section \(v\) on \(T\) determines on every affine open the algebra homomorphism \(u\mapsto v\), \(u^{-1}\mapsto v^{-1}\). The maps agree on overlaps and glue. Conversely, pulling back \(u\) recovers \(v\); these operations are inverse and commute with pullback. Requiring \(v^m=1\) is precisely factoring the algebra map through \((u^m-1)\), so it defines \(\mu_m\).

**2.** Over \(A=k[b,c]\), division by \(x^3-bx-c\) makes the quotient free with basis \(1,x,x^2\). Thus it gives a morphism \(\mathbb A^2_k\to\mathbb A^3_k\), with coefficients \((a_2,a_1,a_0)=(0,-b,-c)\). At \((b,c)=(0,0)\), the quotient is \(k[x]/(x^3)\), a length-three scheme supported at one point. If the polynomial has three distinct roots over an algebraic closure, its geometric fibre consists of three reduced points. Length measures the vector-space dimension of the coordinate ring, including nilpotents, so it remains three in both cases.

**3.** Let \(t=x_1/x_0\) on the first chart. Frames given by \(x_0\) and \(x_1\) satisfy \(x_1=t x_0\) on the overlap. The nontrivial transition function constructs \(\mathcal O(1)\); it is invisible if one remembers only that both restrictions have the trivial isomorphism class. The two generating sections retain the ratios \((1,t)\) and \((t^{-1},1)\) in the respective frames. An isomorphism preserving both sections is unique, so overlap identifications of such pairs retain the gluing data. The two-dimensional global-section calculation in Proposition 5.1 proves that the resulting bundle is nontrivial.

**4.** In a frame \(e_0,\ldots,e_n\) of \(E\), the chart where \(q(e_i)\) generates has coordinates \(z_j=q(e_j)/q(e_i)\), with \(z_i=1\). On changing the chosen generator from \(i\) to \(k\), the coordinates become \(z_j/z_k\). For a change of frame \(e'_a=\sum_b g_{ba}e_b\), put \(w_a=\sum_b g_{ba}z_b\); on the chart where \(q(e'_k)\) generates, the coordinates are \(w_a/w_k\). All denominators are units on the designated opens. The line bundle has the same changes of frame as the chosen \(q(e_i)\); pulling back the universal quotient therefore recovers exactly \(L\), rather than its dual.

**5.** A Zariski covering of an affine scheme is an fpqc covering in the sheaf sense after refining to finitely many affine opens: an affine scheme is quasi-compact, and a finite disjoint union of affine opens is a faithfully flat quasi-compact cover. Thus \(F\) is a sheaf on the affine Zariski basis.

For an arbitrary \(T\), define \(\overline F(T)\) by giving an element of \(F(U)\) on each member of an affine open cover, with agreement on affine opens covering every pairwise intersection. Intersections need not be affine or quasi-compact; their affine opens still form a basis. The sheaf axiom on affine schemes proves that agreement is independent of this refinement. Passing to a common refinement shows that the definition is independent of the chosen cover. The same axiom glues these collections, so \(\overline F\) is a Zariski sheaf. To define pullback along a morphism, refine both source and target by affine opens so that the relevant source opens map into target opens, apply \(F\), and glue. Independence of refinements gives functoriality.

Extend each given open subfunctor in the same way. Its pullbacks on an arbitrary \(T\) glue from the prescribed open subschemes of its affine opens; their equality on overlaps follows by affine testing. Their unions cover \(T\), again checked on affine opens. A scheme representing the restricted subfunctor also represents its extension because morphisms into a scheme glue on affine opens. Theorem 4.1 now represents \(\overline F\). Any other Zariski sheaf extension is canonically isomorphic to this one, by the same gluing description. An arbitrary presheaf extension need not be determined by values on an affine basis; this is why the qualification is essential.

## What this lesson does not prove

We use Yoneda's lemma, gluing of schemes along open subschemes, and the standard affine charts of relative Proj as prerequisites. References are [Stacks, Tags 001P, 01JA, 01NS and 01O0]. We also use \(\Gamma(\mathbb P^1_k,\mathcal O(1))\simeq k^2\) and \(\Gamma(\mathbb P^1_k,\mathcal O)\simeq k\), which follow directly from homogeneous degree-one and degree-zero polynomials. No representability theorem for Hilbert or Picard functors is used here.

## References

- [Stacks] The Stacks project, *Schemes*, Tags 01JF–01JJ, and *Constructions of Schemes*, Tags 01ND–01NE and 01NS–01OB. These tags are retained in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#section-representable), an edition with AI-proposed corrections and AI-written additions. Projectivization is discussed in its [projective-bundle section](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#section-projective-bundle).
- [Vakil] R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, sections on functors of points, projective constructions, and the Grassmannian as a moduli space.
