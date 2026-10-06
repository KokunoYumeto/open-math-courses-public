# Flat morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent local AI review found corrections in the preceding version; this revision awaits independent correction verification. Public domain (CC0).*

A family can change its geometry without creating a new algebraic relation among its parameters. Flatness expresses this distinction. The equation \(uv=t\) gives a family whose smooth hyperbolas become two intersecting lines. The equation \(tu=0\) gives a different phenomenon: an entire extra direction appears only over \(t=0\). We will distinguish these families, explain why flat families spread across open subsets of their base, and construct a flat limit with an embedded point.

We assume affine schemes, localization, quasi-coherent sheaves, and the tensor-product definition of flat modules. The background topics are **Tor and flat modules**, **Faithful flatness and the local criterion for flatness**, **Quasi-compact morphisms and morphisms of finite type and finite presentation**, and **Quasi-finite morphisms and Chevalley's theorem**. In particular we use the ideal test for flat modules, faithful flatness of a flat local homomorphism, and Chevalley's constructibility theorem for finitely presented morphisms. Their precise forms are recorded at the end. Basic references are the Stacks Project and Vakil's *The Rising Sea*.

## 1. Detecting flatness in a family

For a morphism \(f:X\to S\) and \(x\in X\), put \(s=f(x)\). A quasi-coherent sheaf \(\mathcal F\) is **flat over \(S\) at \(x\)** when \(\mathcal F_x\) is flat as an \(\mathcal O_{S,s}\)-module. The morphism is flat at \(x\) when this holds for \(\mathcal O_X\). Flatness means flatness at every point. A faithfully flat morphism means a flat, surjective morphism.

**Proposition 1.1 (affine detection).** The sheaf \(\mathcal F\) is flat over \(S\) if and only if, for every pair of affine opens \(U=\operatorname{Spec}B\subset X\), \(V=\operatorname{Spec}A\subset S\) with \(f(U)\subset V\), the module \(\mathcal F(U)\) is flat over \(A\). It suffices to test affine covers of the base and of their inverse images.

**Proof.** Write \(M=\mathcal F(U)\). If \(M\) is \(A\)-flat, localizing it as a \(B\)-module preserves \(A\)-flatness: localization is a filtered colimit of copies of \(M\), and filtered colimits preserve exact sequences. At a prime \(\mathfrak q\subset B\) over \(\mathfrak p\subset A\), elements outside \(\mathfrak p\) are already invertible on \(M_{\mathfrak q}\), so this is equivalent to \(A_{\mathfrak p}\)-flatness.

Conversely suppose every such stalk is flat. For a finitely generated ideal \(J\subset A\), consider the kernel of

\[
J\otimes_A M\longrightarrow M.
\]

It is a \(B\)-module. At \(\mathfrak q\) the displayed map becomes \(J_{\mathfrak p}\otimes_{A_{\mathfrak p}}M_{\mathfrak q}\to M_{\mathfrak q}\), which is injective. A module whose localizations at all primes vanish is zero. The ideal test now proves that \(M\) is flat. This establishes the equivalence and the assertion about covers. The same argument proves locality after restricting either scheme. ∎

For an affine morphism \(f\), the sheaf \(\mathcal F\) is flat over \(S\) precisely when \(f_*\mathcal F\) is flat over \(S\): on \(V\) the module of sections of the latter is \(\mathcal F(f^{-1}V)\), and the inverse image is affine. See [Stacks, Tags [01U4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-module-characterize) and [0FLM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-pushforward-flat-affine)].

Here are immediate examples. Polynomial rings are free over their coefficient rings, so \(\mathbb A^n_S\to S\) is flat. The usual affine charts prove the same for \(\mathbb P^n_S\). Localization proves flatness of open immersions and of \(\operatorname{Spec}\mathcal O_{X,x}\to X\). For a Noetherian local ring \(A\), its completion is faithfully flat over \(A\); this is a completion theorem, recalled with its locator below.

Over \(k[t]\), the algebra \(k[t,u,v]/(uv-t)\) is torsion free: after substituting \(t=uv\), it is the domain \(k[u,v]\). A torsion-free module over a principal ideal domain is flat: every nonzero ideal \((a)\) is a free module of rank one, and its tensor map into the module is the injective multiplication map by \(a\). Apply the ideal test. Its special fibre has equation \(uv=0\). In contrast, \(k[t,u]/(tu)\) is not flat: multiplication by \(t\), injective on \(k[t]\), kills the nonzero class of \(u\). The fibres themselves are vector spaces over fields and hence flat over those fields. That observation says nothing about flatness over the parameter ring.

## 2. Changing the base and following generizations

**Proposition 2.1 (permanence).** Flat morphisms are stable under composition and arbitrary base change. Products of flat morphisms over a base are flat. More generally, if \(\mathcal F_x\) is flat over \(\mathcal O_{Y,f(x)}\) and this local ring is flat over \(\mathcal O_{Z,gf(x)}\), then \(\mathcal F\) is flat over \(Z\) at \(x\). If \(\mathcal F\) is flat over \(S\) at \(x\), its pullback is flat at every point above \(x\) after any base change.

**Proof.** Composition follows by factoring the tensor functor through the intermediate ring; both tensor functors are exact. For base change, if \(A\to A'\), an \(A'\)-module \(N\) satisfies

\[
N\otimes_{A'}(A'\otimes_A M)\simeq N\otimes_A M.
\]

Thus \(A'\otimes_A M\) is \(A'\)-flat whenever \(M\) is \(A\)-flat. Proposition 1.1 globalizes this calculation. For the pointwise assertion first pass to \(B_{\mathfrak q}\) and \(A_{\mathfrak p}\). At a point above \(\mathfrak q\), localizing \(B\otimes_A A'\) already inverts every element of \(B\setminus\mathfrak q\); the preceding tensor calculation and localization apply there. A product factors as a base change of one factor followed by the other. ∎

A generization of a point is a point whose closure contains it. In an affine spectrum this means a smaller prime ideal.

**Theorem 2.2 (lifting generizations).** If \(f:X\to S\) is flat, \(x\in X\), and \(s'\) is a generization of \(f(x)\), then some generization \(x'\) of \(x\) maps to \(s'\).

**Proof.** Every open neighbourhood of \(f(x)\) contains \(s'\). Choose affine neighbourhoods, with primes \(\mathfrak q\subset B\) and \(\mathfrak p\subset A\). The local map \(A_{\mathfrak p}\to B_{\mathfrak q}\) is flat and local, hence faithfully flat. Its spectrum is surjective. The prime representing \(s'\) in \(\operatorname{Spec}A_{\mathfrak p}\) therefore lifts to a prime of \(B_{\mathfrak q}\). Its inverse image in \(B\) is contained in \(\mathfrak q\), as required. ∎

Consequently the image of a flat morphism is stable under generization. If \(\xi\) is the generic point of an irreducible component of \(X\), its image has no proper generization: such a generization would lift to a proper generization of \(\xi\). Thus \(f(\xi)\) is a generic point of an irreducible component of \(S\). If \(S\) is irreducible, every irreducible component of \(X\) dominates \(S\). Finite presentation is unnecessary for this conclusion. References are [Stacks, Tags [00HS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-flat-going-down) and [03HV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-generalizations-lift-flat)].

## 3. What flatness does to the topology

We need a topological observation that works for arbitrary spectra. Equip \(\operatorname{Spec}A\) with the **constructible topology**, in which every \(D(a)\) and \(V(a)\) is open and closed. This space is compact. One proof assigns to an ultrafilter \(\mathscr U\) the prime

\[
\mathfrak p_{\mathscr U}=\{a:V(a)\in\mathscr U\}.
\]

The identities for vanishing sets show this is an ideal and is prime: \(V(ab)=V(a)\cup V(b)\), while \(V(a)\cap V(b)\subset V(a+b)\). It is proper since \(V(1)=\varnothing\). Every basic constructible neighbourhood of this prime belongs to the ultrafilter, proving compactness by the ultrafilter characterization. Ring maps induce continuous maps for this topology.

**Lemma 3.1.** A constructibly compact subset \(C\subset\operatorname{Spec}A\) that is stable under specialization is Zariski closed. In particular, a constructible subset stable under generization is open.

**Proof.** If \(\mathfrak p\) belongs to the Zariski closure of \(C\), the subsets \(C\cap D(a)\), for \(a\notin\mathfrak p\), are nonempty and have the finite intersection property. They are constructibly closed in \(C\). Compactness supplies \(\mathfrak q\in C\) avoiding every \(a\notin\mathfrak p\). Thus \(\mathfrak q\subset\mathfrak p\), so specialization stability gives \(\mathfrak p\in C\). For the second assertion apply the first to the constructible complement; constructible subsets of a spectrum are compact in the constructible topology. ∎

**Theorem 3.2 (openness).** A flat morphism locally of finite presentation is universally open.

**Proof.** Cover any open subset of \(X\) by affine opens \(U\) mapping to affine opens \(V\subset S\). The induced map \(U\to V\) is finitely presented. Chevalley's theorem says that its image is constructible. Theorem 2.2 makes this image stable under generization. Lemma 3.1 makes it open in \(V\), hence in \(S\). Taking unions proves openness. Arbitrary base change preserves flatness and local finite presentation, so the same proof establishes universal openness. ∎

**Theorem 3.3 (quotient topology).** If \(f:X\to S\) is quasi-compact, flat and surjective, a subset \(T\subset S\) is open, respectively closed, precisely when \(f^{-1}T\) is open, respectively closed.

**Proof.** It suffices to descend closedness locally on an affine open \(V\subset S\). Cover the quasi-compact scheme \(f^{-1}V\) by finitely many affine opens \(U_i\). If \(Z=f^{-1}T\) is closed, each \(Z\cap U_i\) is affine and its image in \(V\) is constructibly compact. Their finite union is \(T\cap V\), by surjectivity. This union is stable under specialization. Indeed, if \(s\in T\) and \(s_1\) specializes \(s\), choose \(x_1\) over \(s_1\); lift the generization \(s\) to a generization \(x\) of \(x_1\). Since the inverse image of \(T\) is closed and contains \(x\), it contains \(x_1\), and \(s_1\in T\). Lemma 3.1 applies. Openness follows by taking complements; the reverse implications follow from continuity. ∎

These are [Stacks, Tags [01UA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-fppf-open) and [02JY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-fpqc-quotient-topology)]. The proof also explains why quasi-compactness cannot simply be omitted from the second theorem.

For example, \(\operatorname{Spec}\mathbb Q\to\operatorname{Spec}\mathbb Z\) is flat but its image is the generic point, which is not open. Now take the disjoint union

\[
X=\operatorname{Spec}\mathbb Q\ \amalg\ \coprod_{p\text{ prime}}\operatorname{Spec}\mathbb Z_{(p)}\longrightarrow\operatorname{Spec}\mathbb Z.
\]

It is flat and surjective. The inverse image of the generic point is open: it is the whole first summand and \(D(p)\) in the \(p\)-summand. The map therefore fails to give the quotient topology. Its source is not quasi-compact, since infinitely many nonempty disjoint open summands are needed to cover it.

## 4. Flat closed subschemes

A closed immersion has no new points in a fibre. Flatness puts an even stronger constraint on its local ring maps.

**Lemma 4.1.** For an ideal \(I\subset A\), the quotient \(A/I\) is flat over \(A\) if and only if every \(a\in I\) satisfies \(a=ab\) for some \(b\in I\). At every prime in \(V(I)\), the localized ideal is then zero.

**Proof.** If the quotient is flat, tensoring \((a)\hookrightarrow A\) with it is injective. For \(a\in I\) this map is zero, so \((a)/I(a)=0\). Hence \(a=ab\) for some \(b\in I\). Conversely, at a prime containing \(I\), the equation \((1-b)a=0\) kills \(a\) on localization, because \(1-b\) is a unit there. At a prime not containing \(I\) the quotient localizes to zero. Every localized quotient is therefore either \(A_{\mathfrak p}\) or zero, and is flat. Proposition 1.1 proves flatness. ∎

**Theorem 4.2.** Closed subschemes flat over \(X\) correspond bijectively to closed subsets of \(X\) stable under generization. Every morphism whose set-theoretic image lies in such a subset factors uniquely through its flat closed subscheme. Connected components consequently have a canonical flat closed subscheme structure.

**Proof.** Work first in \(\operatorname{Spec}A\). A flat quotient has generization-stable image by Theorem 2.2. Its ideal is uniquely determined by this image \(Z\): by Lemma 4.1 it equals the kernel of \(A\to\prod_{\mathfrak p\in Z}A_{\mathfrak p}\). To see the equality in the other direction, a nonzero element of \(A/I\) remains nonzero in some localization of that module, necessarily at a prime in \(Z\).

For existence write \(Z=V(J)\), with \(J\) radical, and set

\[
I=\{a\in A:a=aj\text{ for some }j\in J\}.
\]

This is an ideal: if \(a=aj\), \(b=bk\), then \(a+b=(a+b)(j+k-jk)\), and multiplication by any scalar preserves the condition. It lies in \(J\). If a prime \(\mathfrak p\) contains \(I\), the multiplicative set \((A\setminus\mathfrak p)(1+J)\) avoids zero: an equality \(s(1+j)=0\) would place \(s=-sj\) in \(I\). Choose a prime \(\mathfrak q\) disjoint from this set. Then \(\mathfrak q\subset\mathfrak p\), and \(\mathfrak q+J\) is proper, for otherwise \(\mathfrak q\) would meet \(1+J\). A maximal ideal containing \(\mathfrak q+J\) lies in \(Z\); generization stability puts \(\mathfrak q\) in \(Z\), and specialization stability puts \(\mathfrak p\) in \(Z\). Thus \(V(I)=V(J)\) and \(\sqrt I=J\). For \(a=aj\), a power \(j^n\) lies in \(I\), and \(a=aj^n\). Lemma 4.1 proves flatness.

The affine constructions agree on overlaps by uniqueness and hence glue. For the factorization assertion, pull back the flat closed immersion to the source of the proposed morphism. Its image is the whole source. The just-proved uniqueness says that this pullback equals the whole source as a scheme. Finally, a connected component is closed and stable under both specialization and generization: the closure of a point is connected and cannot leave its component. Apply the correspondence. ∎

**Corollary 4.3.** A flat closed immersion of finite presentation is the inclusion of an open and closed subscheme.

**Proof.** The image is closed by definition and open by Theorem 3.2. At every point of the image Lemma 4.1 says that the defining ideal has zero stalk, so the immersion identifies the subscheme with that open subscheme. ∎

References are [Stacks, Tags [04PW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-characterize-flat-closed-immersions), [04PX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-scheme-structure-connected-component) and [0819](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-flat-closed-immersions-finite-presentation)]. The component structure can retain nilpotents; it is not the reduced induced structure.

## 5. Finding a flat part of an arbitrary finite type family

We prove generic flatness for reduced bases, including those that are not Noetherian. The key is that, on a dense open, polynomial relations can be arranged with an invertible leading coefficient. The free modules below may have infinite rank.

**Lemma 5.1 (generic freeness).** Let \(A\) be reduced, \(P=A[z_1,\ldots,z_n]\), and \(M\) a finite \(P\)-module. There is a dense open subset of \(\operatorname{Spec}A\) covered by principal opens \(D(a)\) on which \(M_a\) is \(A_a\)-free and finitely presented as a \(P_a\)-module. If \(A\) is a domain, one such \(a\ne0\) suffices.

**Proof.** We induct on the number of variables. A finite module has a finite filtration with cyclic quotients: take successive spans of a finite generating list. If the assertion holds for both ends of an exact sequence, intersect their dense good opens. On a smaller principal open both ends are free over the coefficient ring, so the sequence splits over that ring and its middle is free. The middle is finitely presented over the polynomial ring as well: lift finite generators and finite relation lists of the two ends to obtain a finite relation list for the middle. Thus it suffices to consider \(P/J\), with no finiteness assumption on \(J\).

Let \(C\subset A\) be generated by all coefficients of all polynomials in \(J\). The union of \(D(C)\) and the open complement of the closure of \(D(C)\) is dense. On a principal open contained in the latter, every coefficient vanishes: its vanishing set is the whole spectrum there, and that coefficient ring is reduced. Hence \(J=0\) there and the assertion holds. On \(D(C)\), use the principal opens where an actual coefficient is invertible. We can therefore suppose \(J\) contains a polynomial \(g\) with at least one unit coefficient.

A finite further procedure makes every nonzero coefficient of \(g\) a unit on a dense union of opens. For a coefficient \(c\) that is not a unit, split into \(D(c)\) and the open complement of its closure. Their union is dense. On the first \(c\) becomes a unit; on the second it becomes zero, by reducedness. After finitely many such splits the procedure terminates, because \(g\) has only finitely many coefficients and an existing unit coefficient stays a unit. The union of the resulting opens is dense; at each split a dense open subset of the original region is retained.

If \(g\) is constant, its unit coefficient makes \(P/J=0\). Otherwise make the triangular change

\[
z_i=w_i+w_n^{e_i}\ (i<n),\qquad z_n=w_n.
\]

Choose the positive integers \(e_i\) so that the finitely many weights \(\alpha_n+\sum_{i<n}e_i\alpha_i\) of monomials occurring in \(g\) are all different. For instance successive powers of an integer larger than every exponent occurring do this. The largest-weight monomial contributes the unique highest power of \(w_n\), with a unit coefficient. Dividing by that coefficient makes \(g\) monic in \(w_n\). Consequently \(P/J\) is finite over \(A[w_1,\ldots,w_{n-1}]\). Apply the induction hypothesis to this module. Its finite presentation over that smaller polynomial ring implies finite presentation over \(P\): add the finitely many relations describing multiplication by \(w_n\) on a finite generating list. This completes the induction, including \(n=0\), where a nonzero polynomial with a unit coefficient is simply a unit. All reductions used finite intersections or dense unions of open subsets, so they prove the dense-open assertion.

If \(A\) is a domain, the dense open obtained is nonempty and contains some nonempty principal open \(D(a)\). Its defining element is nonzero. ∎

**Corollary 5.2.** If \(A\) is reduced, \(B\) is a finite type \(A\)-algebra, and \(M\) is a finite \(B\)-module, there is a dense open of the base on which, locally on principal opens, both \(B\) and \(M\) are free over the base, \(B\) is finitely presented as an algebra, and \(M\) is finitely presented over \(B\).

**Proof.** Choose \(P\twoheadrightarrow B\). Both \(B\) and \(M\) are finite \(P\)-modules. Apply Lemma 5.1 to each and intersect the good opens. Finite presentation of \(P\twoheadrightarrow B\) as a module says its kernel is finitely generated, hence \(B\) is a finitely presented algebra. A finite presentation of \(M\) over \(P\) yields one over \(B\) by tensoring that presentation with \(B\); right exactness suffices. ∎

This proves, in particular, the Noetherian-domain generic freeness theorem [Stacks, Tag [051R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-generic-flatness-Noetherian)], and the algebra behind [Stacks, Tags [051S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-generic-flatness-finitely-presented) and [052B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-proposition-generic-flatness-reduced)].

**Theorem 5.3 (generic flatness).** Let \(S\) be reduced, \(f:X\to S\) finite type, and \(\mathcal F\) quasi-coherent of finite type. There is a dense open \(U\subset S\) such that \(X_U\to U\) is flat and of finite presentation, and \(\mathcal F|_{X_U}\) is flat over \(U\) and finitely presented over \(\mathcal O_{X_U}\). This includes the integral-base case.

**Proof.** Work over an affine open \(\operatorname{Spec}A\subset S\). Its inverse image has a finite affine cover \(X_i=\operatorname{Spec}B_i\). Write \(M_i\) for the module of \(\mathcal F\) there. Apply Corollary 5.2 to all \(B_i,M_i\).

Finite presentation of the whole morphism also requires quasi-separatedness; we must check overlaps. Write \(X_i\setminus(X_i\cap X_j)=V(J_{ij})\) for an ideal \(J_{ij}\subset B_i\), and apply Corollary 5.2 also to the finite module \(B_i/J_{ij}\). There are only finitely many pairs. Intersect all their dense good opens. Near every point of this intersection take a common principal open where all conclusions hold. Now \(B_i/J_{ij}\) is finitely presented, so \(J_{ij}\) is finitely generated. Its complement is therefore a finite union of principal opens. All overlaps are quasi-compact. Thus \(X_U\to U\) is quasi-compact, quasi-separated and locally of finite presentation, hence of finite presentation. Flatness of it and of the sheaf follows from Proposition 1.1. These properties are local on the base, so the good opens obtained over affine opens of \(S\) have a union that is open and dense and satisfies all assertions. ∎

See [Stacks, Tags [052A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-proposition-generic-flatness) and [052B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-proposition-generic-flatness-reduced)]. Reducedness matters: over \(\operatorname{Spec}k[\epsilon]/(\epsilon^2)\), the closed subscheme \(\operatorname{Spec}k\) is not flat, since Lemma 4.1 fails for the ideal \((\epsilon)\). The base has only one point, so there is no smaller nonempty open on which to repair the failure.

## 6. A flat collision with an embedded point

Let \(A=k[t]\) and consider the two lines in \(\mathbb A^3_A\) with ideals \((x,y)\) and \((x-t,z)\). Set

\[
J=(x(x-t),\ y(x-t),\ xz,\ yz).
\]

In \(A[x,y,z]/J\), the relations \(x^2=tx\), \(xy=ty\), \(xz=yz=0\) reduce every monomial to an \(A\)-linear combination of

\[
1,\ x,\ y,y^2,y^3,\ldots,\ z,z^2,z^3,\ldots.
\]

This list is independent. Restrict to the two lines, obtaining a map to \(A[z]\times A[y]\). The listed elements map respectively to \((1,1)\), \((0,t)\), \((0,y^a)\), \((z^b,0)\). If a finite linear combination vanishes, the first coordinate kills its constant and \(z\)-coefficients; the second kills its \(y\)-coefficients and then its \(x\)-coefficient, since \(t\) is a non-zero-divisor in \(A\). Thus the map is injective, and \(J=(x,y)\cap(x-t,z)\). The quotient is free over \(A\), so the family is flat. It is also \(t\)-torsion free, which proves \(J:t^\infty=J\): this is already the saturated closure of the general family.

At \(t=0\) the ideal is

\[
J_0=(x^2,xy,xz,yz).
\]

Its radical is \((x,yz)\), the ideal of the two meeting lines. The nonzero class of \(x\) is annihilated by \((x,y,z)\), and its annihilator is exactly that maximal ideal by the displayed basis. Hence the origin is an embedded associated point. More explicitly,

\[
0\longrightarrow k\cdot x\longrightarrow k[x,y,z]/J_0\longrightarrow k[y,z]/(yz)\longrightarrow0.
\]

The kernel has length one. Flatness has retained information that would disappear if one took only the reduced union after collision.

For the projective comparison, homogenize in \(\mathbb P^3_A\), using a coordinate \(w\). The ideal becomes \((x(x-tw),y(x-tw),xz,yz)\). In degree \(n\ge1\), an \(A\)-basis is

\[
w^n,\ xw^{n-1},\ y^aw^{n-a}\ (1\le a\le n),\ z^bw^{n-b}\ (1\le b\le n).
\]

Reduction and restriction prove spanning and independence exactly as above. Both fibres therefore have Hilbert polynomial \(2n+2\). The reduced pair of meeting lines has polynomial \(2n+1\); the embedded point contributes the missing one. This calculation is a complete explanation of the limit, without inferring flatness from a picture.

## 7. Exercises

1. **Easy.** Compare \(k[r,s]/(s^2-r)\) and \(k[r,s]/(rs)\) as \(k[r]\)-modules. Give a basis or an explicit failed injection.
2. **Easy.** Let \(f:X\to S\) be finite with \(S\) Noetherian. Prove that \(f\) is flat exactly when \(f_*\mathcal O_X\) is locally free. For \(\operatorname{char}k\ne2\), apply this to the normalization of \(y^2=x^2(x+1)\).
3. **Medium.** Prove that every irreducible component of a flat \(X\to S\) dominates an irreducible base \(S\). Explain whether finite presentation was used.
4. **Medium.** Prove Corollary 4.3 using openness. Give a closed immersion that fails flatness.
5. **Medium.** Verify both counterexamples in Section 3, including the open inverse image in every summand of the disjoint union.
6. **Hard.** Reconstruct the family of Section 6 from its two component ideals. Prove saturation, calculate the special fibre's embedded point, and calculate its projective Hilbert polynomial.

## 8. Solutions

**1.** Division by the monic polynomial \(s^2-r\) leaves a unique remainder \(a(r)+b(r)s\), so the first algebra is free with basis \(1,s\). In the second the class of \(s\) is nonzero, as specialization \(r=0\) shows, but \(r\) kills it. Tensoring the injective map \(k[r]\xrightarrow{r}k[r]\) with this algebra is therefore not injective.

**2.** On an affine base a finite morphism corresponds to a finite module \(B\) over a Noetherian ring \(A\), and it is flat exactly when this module is flat by Proposition 1.1. A finite flat module over a Noetherian local ring is free: lift a basis modulo the maximal ideal to a surjection from a finite free module; flatness makes the kernel's reduction zero, and the kernel is finite, so Nakayama's lemma kills it. Such a basis and its relations extend to a neighbourhood because the module is finitely presented. This proves local freeness, and the converse is immediate.

For the node use \(x=u^2-1\), \(y=u(u^2-1)\). The image ring \(k[x,y]/(y^2-x^2(x+1))\) embeds in \(k[u]\), which is finite because \(u^2=x+1\); the fraction fields agree since \(u=y/x\). The polynomial ring is integrally closed, hence gives the normalization. Away from \(x=0\), the equality \(u=y/x\) makes the map an isomorphism. At the node the fibre is \(k[u]/(u^2-1)\), of dimension two, while the generic rank is one. A finite locally free module has locally constant rank, and the curve is irreducible, so this normalization is not flat.

**3.** Let \(\xi\) be the generic point of an irreducible component. Lift the generic point of \(S\), a generization of \(f(\xi)\), to a generization of \(\xi\). Minimality of the prime representing \(\xi\) says this lift is \(\xi\) itself. The component's image contains the generic point of \(S\) and is dense. No finite-presentation hypothesis enters the argument.

**4.** Openness makes the closed image open as well. Lemma 4.1 identifies the local rings along that image with the local rings of the ambient scheme, proving it is the indicated open subscheme. The inclusion of the origin in \(\mathbb A^1_k\) fails flatness: multiplication by the coordinate is injective on \(k[t]\) but acts by zero on its quotient \(k\).

**5.** Every localization is flat, so both maps are flat. Any nonempty basic open \(D(n)\subset\operatorname{Spec}\mathbb Z\), \(n\ne0\), contains all primes not dividing \(n\), and therefore contains closed points. The singleton generic point is not open. In \(\operatorname{Spec}\mathbb Z_{(p)}\) there are exactly the generic point and the closed point \((p)\); its generic singleton is \(D(p)\). These opens, together with the whole \(\mathbb Q\)-summand, give the open inverse image claimed. Each closed point of the target is hit by its own local summand. Finally, the open summands form an infinite cover with no finite subcover, so this surjective map to an affine scheme is not quasi-compact.

**6.** Each generator of \(J\) vanishes on both lines. Reduction to the listed monomials and their independent images in \(A[z]\times A[y]\) prove there are no further relations and identify \(J\) with the intersection. Its quotient is free, hence multiplication by every power of \(t\) is injective; this is precisely saturation. Specialization gives \(J_0\), and quotienting further by \(x\) gives the reduced pair of lines. The kernel is \(k\cdot x\), with annihilator \((x,y,z)\), hence is the length-one embedded point at the origin. After homogenization the degree-\(n\) list in Section 6 has \(2n+2\) elements for every \(n\ge1\), independent by restriction. This proves the Hilbert polynomial on both fibres. The reduced meeting lines have the same list with the \(xw^{n-1}\) element removed and therefore polynomial \(2n+1\).

## What this lesson does not prove

The background algebra includes the ideal criterion: \(M\) is flat over \(A\) exactly when \(J\otimes_A M\to M\) is injective for every finitely generated ideal \(J\subset A\) [Stacks, Tag [00HD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-flat)]; a flat local homomorphism is faithfully flat [Stacks, Tag [00HR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-local-flat-ff)]; and faithfully flat ring maps are surjective on spectra [Stacks, Tag [00HQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-ff-rings)].

Chevalley's theorem says the image of a finitely presented morphism between affine schemes is constructible [Stacks, Tag [054K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-theorem-chevalley)]. Standard facts about finite presentation used here are its affine characterization and the equivalence with quasi-compactness, quasi-separatedness and local finite presentation [Stacks, Tags [01TP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-finite-presentation) and [01TQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-finite-presentation-characterize)]. Completion of a Noetherian local ring is faithfully flat [Stacks, Tag [00MC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-faithfully-flat)]. These are prerequisite results; the proofs of the geometric flatness theorems and generic flatness above do not depend on an omitted version of those theorems.

The blow-up of \(\mathbb A^2\) at its origin is another non-flat example. In its chart \(x=u,y=uv\), at a closed point of the exceptional curve the source local ring has dimension two, the base local ring has dimension two, and the fibre local ring has dimension one. The flat dimension formula would give \(2=2+1\), which is impossible. We prove that formula in **Flatness criteria, dimension and the flat locus**.

The internal proof providers are [Tor and flat modules](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-07.html) for module flatness, [Faithful flatness and the local criterion for flatness](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-08.html) for faithful detection, and [Completion](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-19.html), Theorem 3.2, for faithful flatness of Noetherian local completion. [Quasi-finite morphisms and Chevalley’s theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-06.html), Section 4, supplies constructible images at finite-presentation generality, and [Quasi-compact morphisms and finiteness conditions](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-02.html) supplies the finite-presentation characterizations. These lessons are written; the exact statements needed here are those just specified.

## References

- [The Stacks Project](https://stacks.math.columbia.edu/), *Morphisms of Schemes*: flat morphisms, flat closed immersions and generic flatness; [Tags 01U2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-flat), [04PV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-flat-closed-immersions) and [0529](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-generic-flatness). Tag references identify individual statements. The linked text is **AI Integrated Stacks Project**, an edition with AI-proposed corrections and AI-written additions that have not been reviewed by the Stacks Project maintainers.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, Sections 24.1 and 24.5, on flatness and its topological consequences. [Author's book page](https://math.stanford.edu/~vakil/216blog/).
