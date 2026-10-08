# Sheaves of modules and their derived categories

*Original lesson: Claude Opus 5.5 (Anthropic), September 2026, released under CC0; its historical notice records a separate Claude AI spot-check. Sections 8–9 and the initial prerequisite routing are a candidate revision drafted by OpenAI Codex on 1 October 2026; the exact model identity of that initial drafting remains unverified. The added proofs of Baer's criterion, the support sequence, inverse-image adjunction, short-exact-sequence triangles and bounded-below derived functors, and their current AI self-check, are by OpenAI GPT-6 Astra in Codex, Ultra reasoning effort. Whole-course proof completion remains unfinished. Original text: public domain (CC0).*

This lesson sets up the homological algebra of sheaves of modules on a topological space, in the generality that microlocal sheaf theory needs. It shows that sheaves of left modules over any sheaf of rings, commutative or not, form an abelian category with exact filtered colimits, a generator and functorial injective embeddings. From this it obtains right derived functors, first on bounded-below complexes and then, through K-injective resolutions, on all complexes. For a commutative sheaf of rings it then treats K-flat resolutions, the derived tensor product, the adjunction between derived pullback and pushforward, the internal derived Hom and its composition map. It ends with the localization triangle for a locally closed set and a closed part of it, and with the two sign conventions for distinguished triangles that are in use.

Every result that needs no tensor product is proved for left modules over an arbitrary sheaf of rings, so it also applies to constant sheaves of noncommutative rings. The worked examples show which hypotheses cannot be dropped: an unbounded complex of injectives need not be K-injective, sections need not commute with infinite direct sums, products of sheaves need not be exact, and derived functors of bounded complexes need not be bounded.

The lesson assumes the basic language of sheaves on a topological space (sections, restriction maps, stalks and germs) and of homological algebra: abelian categories, complexes and their cohomology, the homotopy category, the derived category and triangulated categories. Its sheaf-theoretic prerequisite is the earlier programme lesson Sheaves on topological spaces, specifically Theorem 2.2, Theorem 3.1 and the algebraic-structure discussion at the end of Section 6. Section 1 distinguishes those established internal proofs from background whose full programme proof is still outstanding. Section 7 now proves the unbounded K-injective existence theorem rather than assuming it; the localization foundations still need their exact earlier programme treatment.

Basic references are [Schapira, *Categories and Homological Algebra*], [Schapira, *Algebra and Topology*] and [Stacks]. Resolutions of unbounded complexes by K-injective and K-flat complexes go back to [Spaltenstein 1988].

<span id="SH-FND-DC-01"></span><span id="sh-fnd-dc-01"></span>

## 1. Conventions and background

### Conventions

- \(X\) is a topological space. \(\mathcal O\) is a sheaf of rings on \(X\): associative, with \(1\), not necessarily commutative. \(\operatorname{Mod}(\mathcal O)\) is the category of sheaves of left \(\mathcal O\)-modules. For a ring \(A\), \(\operatorname{Mod}(A)\) is the category of left \(A\)-modules. When a result needs \(\mathcal O\) commutative we say so; then \((X,\mathcal O)\) is a ringed space.
- For a unital ring \(k\), \(k_X\) is the constant sheaf, and \(\operatorname{Mod}(k_X)\) is the category of sheaves of left \(k\)-modules. The ring \(k\) need not be commutative.
- \(F_x\) is the stalk at \(x\), a left module over the stalk ring \(\mathcal O_x\); \(s_x\) is the germ of a section \(s\). For an open \(j:U\hookrightarrow X\), \(j^{-1}\) is restriction, \(j_*\) is direct image, and \(j_!\) is extension by zero ([Lemma 5.2](#sh-fnd-dc-05)). \(x_*J\) is a skyscraper sheaf ([Lemma 5.3](#sh-fnd-dc-05)).
- Complexes are cohomological. The shift is \((K[1])^n=K^{n+1}\) with \(d_{K[1]}=-d_K\). The Hom complex is
\[
\operatorname{Hom}^n(K,L)=\prod_{p\in\mathbb Z}\operatorname{Hom}(K^p,L^{p+n}),\qquad df=d_L\circ f-(-1)^nf\circ d_K ,
\]
and the total complex of a tensor product has the differential \(d(a\otimes b)=da\otimes b+(-1)^{|a|}a\otimes db\).
- \(K(\mathcal A)\) is the homotopy category and \(D(\mathcal A)\) the derived category of an abelian category \(\mathcal A\). A complex is *acyclic* if all its cohomology vanishes. "Qis" means quasi-isomorphism.
- A complex \(I\) is *K-injective*, or *homotopically injective*, if \(\operatorname{Hom}_{K(\mathcal A)}(M,I)=0\) for every acyclic \(M\). For commutative \(\mathcal O\), a complex \(P\) of \(\mathcal O\)-modules is *K-flat* if \(\operatorname{Tot}(M\otimes_{\mathcal O}P)\) is acyclic for every acyclic \(M\).
- A sheaf \(F\) is *flabby* if \(F(X)\to F(V)\) is onto for every open \(V\). Then \(F(W)\to F(V)\) is onto for all opens \(V\subset W\), because \(F(X)\to F(V)\) factors through \(F(W)\).
- *Sections with support.* Let \(W\subset X\) be locally closed, and choose an open set \(\Omega\supset W\) in which \(W\) is closed. For a sheaf \(F\), the sheaf \(\Gamma_WF\) of sections supported in \(W\) is given by \((\Gamma_WF)(V)=\{s\in F(V\cap\Omega):\operatorname{supp}s\subset W\}\) for \(V\) open. It does not depend on \(\Omega\). The intersection of two choices is again a choice, so it is enough to compare \(\Omega\) with a choice \(\Omega'\subset\Omega\). A section over \(V\cap\Omega\) supported in \(W\) vanishes on the open set \(V\cap(\Omega\setminus W)\), and \(V\cap\Omega\) is covered by \(V\cap\Omega'\) and \(V\cap(\Omega\setminus W)\); so restriction to \(V\cap\Omega'\) is injective on such sections. A section over \(V\cap\Omega'\) supported in \(W\) glues with \(0\) on \(V\cap(\Omega\setminus W)\); so restriction is also onto. For closed \(W\) one can take \(\Omega=X\). For open \(W=U\) one can take \(\Omega=U\), so \(\Gamma_U=j_*j^{-1}\) for \(j:U\hookrightarrow X\).

### Established prerequisites and remaining background

The sheafification and isomorphism criteria below have exact earlier programme proofs. The filtered-colimit argument, Baer's criterion, the support sequence, inverse-image adjunction and bounded-below resolution construction are proved here. Section 6 proves (H) and the conditional construction (D); Section 7 proves (K), including its size and extension lemmas; Sections 8–9 prove the unbounded K-flat construction and tensor invariance. Remaining obligations include the underlying construction of the derived category and its triangulated structure and the general constructions in Sections 10–12. Existing supporting proofs in those later sections are retained at their stated scopes; this revision does not certify the whole lesson as proof-closed.

*Sheaves and modules.*

- **(S) Sheafification.** For a presheaf \(P\) of left \(\mathcal O\)-modules there are a sheaf \(P^+\) of left \(\mathcal O\)-modules and a map \(\theta:P\to P^+\) such that every map from \(P\) to a sheaf factors uniquely through \(\theta\), and \(\theta\) is bijective on stalks. Two consequences are used often. Every section of \(P^+\) is, near each point, the image of a section of \(P\), since germs agree. And if \(P\) is *separated* (a section with all germs zero is zero), \(\theta\) is injective on sections. *Internal proof:* Sheaves on topological spaces, Theorem 2.2 and the module-structure verification following Section 6. The same germ construction works for left modules over a noncommutative sheaf of rings: the action on germs respects its order, and local identities glue. *Historical comparison:* [Stacks, Tags 007Z, 0080 and 0089].
- **(I) Stalks detect isomorphisms.** A morphism of sheaves that is bijective on every stalk is an isomorphism. *Internal proof:* Sheaves on topological spaces, Theorem 3.1, isomorphism case: unique local inverse images glue. An inverse to a bijective module-linear morphism is module-linear. *Historical comparison:* [Stacks, Tag 007T].
- **(F) Filtered colimits are exact.** Filtered colimits of modules over a ring are exact. The index category must be filtered: colimits of pushout diagrams, for instance, are not left exact. *Reference:* [Schapira, *Categories and Homological Algebra*, Chapter 2].
  *Proof of (F).* An element of a filtered colimit has a representative at one index; a finite set of representatives and relations can be moved to one later index. If a representative from \(A_i\) maps to zero in \(\varinjlim B_i\), its image is zero at a later index, hence it is zero there by injectivity of \(A_j\to B_j\). If an element represented in \(B_i\) maps to zero in \(\varinjlim C_i\), pass to an index where that image vanishes; exactness there supplies a preimage in \(A_j\). An element represented in \(C_i\) lifts to \(B_i\). These three observations prove exactness of the colimit sequence. For a filtered category rather than a directed partially ordered set, the additional condition that parallel arrows become equal ensures the same finite-relation criterion. \(\square\)

- **(B) Baer's criterion.** A left module \(E\) over a ring \(A\) is injective if every \(A\)-linear map from a left ideal of \(A\) to \(E\) extends to \(A\). *Reference:* [Baer 1940].
  *Proof of (B).* Injectivity immediately gives the stated extension property. Conversely, suppose that property holds. Let \(N\subset M\) be left \(A\)-modules and \(f:N\to E\) linear. Order its extensions \((N',f')\), with \(N\subset N'\subset M\), by restriction. A chain has an upper bound: take the union of its submodules and the compatible union of its maps. Zorn's lemma gives a maximal extension \((N',f')\). If \(x\in M\setminus N'\), put \(J=\{a\in A:ax\in N'\}\). This is a left ideal, and \(a\mapsto f'(ax)\) is a linear map \(J\to E\). By assumption it extends to \(b:A\to E\). Define
  \[
  f''(n+ax)=f'(n)+b(a)\quad(n\in N',\ a\in A).
  \]
  If \(n+ax=n'+a'x\), then \((a-a')x=n'-n\), so \(a-a'\in J\) and \(b(a-a')=f'(n'-n)\). Thus the formula is well defined. It is linear and extends \(f'\) to the strictly larger submodule \(N'+Ax\), contradicting maximality. Hence \(N'=M\), and every map from a submodule extends. This is injectivity. Only the usual axiom of choice, in its Zorn form, is used; no existence theorem for injectives is assumed. \(\square\)

- **(Γ) Supports.** Let \(Z\subset X\) be locally closed and \(Z'\subset Z\) closed in \(Z\). For every sheaf \(F\) of abelian groups, the sequence \(0\to\Gamma_{Z'}F\to\Gamma_ZF\to\Gamma_{Z\setminus Z'}F\), given by the inclusion of supports and by restriction, is exact. If \(F\) is flabby, the last map is onto. *Reference:* [Stacks, Tags 0A39 and 09SV] (sections with support; flasque sheaves).
  *Proof of (Γ).* Choose an open \(\Omega\) in which \(Z\) is closed. Then \(Z'\) is closed in \(\Omega\), and \(Z\setminus Z'\) is closed in \(\Omega\setminus Z'\). Over an open \(V\subset X\), the restriction map in the statement is
  \[
  \{s\in F(V\cap\Omega):\operatorname{supp}s\subset Z\}
  \longrightarrow
  \{t\in F(V\cap(\Omega\setminus Z')):\operatorname{supp}t\subset Z\setminus Z'\}.
  \]
  Its kernel consists exactly of sections supported in \(Z'\), giving exactness on the left on every open set. If \(F\) is flabby, extend \(t\) to a section \(s\) on \(V\cap\Omega\). The extension already vanishes on \(V\cap(\Omega\setminus Z)\), since that open lies in \(V\cap(\Omega\setminus Z')\), where it agrees with \(t\). Its support, taken in \(V\cap\Omega\), is therefore contained in \(Z\). Thus it belongs to the domain and lifts \(t\). This proves surjectivity on sections, hence on sheaves. The maps are module-linear when \(F\) is a sheaf of modules; no commutativity of the coefficient ring is needed. \(\square\)

*Complexes.* Let \(\mathcal A\) and \(\mathcal B\) be abelian categories.

- **(H) Maps into K-injective complexes.** If \(I\) is K-injective, then for every complex \(L\) the map \(\operatorname{Hom}_{K(\mathcal A)}(L,I)\to\operatorname{Hom}_{D(\mathcal A)}(L,I)\) is bijective. *Reference:* [Stacks, Tag 070I].
- **(K) K-injective resolutions.** Call \(\mathcal A\) a *Grothendieck* abelian category if it has all small colimits, its filtered colimits are exact, and it has a *generator*: an object \(G\) such that \(\operatorname{Hom}(G,-)\) is faithful. In such a category every complex \(K\) has a qis \(K\to I(K)\), functorial in \(K\) and injective in each degree, into a K-injective complex whose terms are injective objects. *Internal proof:* [Section 7](#sh-fnd-dc-07), Theorem 7.2 and Lemmas 7.2.1–7.2.5, with both functorial constructions and the final union. *Source credit:* AI Integrated Stacks Project, Injectives, through Tag 079P.
- **(D) Derived functors.** Suppose that every complex of \(\mathcal A\) has a qis into a K-injective complex. Then every additive functor \(\Phi:\mathcal A\to\mathcal B\) has a right derived functor \(R\Phi:D(\mathcal A)\to D(\mathcal B)\), and \(R\Phi(K)=\Phi(I)\) for every qis \(K\to I\) into a K-injective complex. *Reference:* [Stacks, Tag 070K].
- **(T) The triangle of a short exact sequence.** A termwise exact sequence \(0\to A\to B\to C\to0\) of complexes gives a distinguished triangle \(A\to B\to C\to A[1]\) in \(D(\mathcal A)\), and a morphism of such sequences gives a morphism of triangles. The third arrow and its sign are made explicit in Lemma 13.3. *Reference:* [Stacks, Tag 0152].

  *Proof of (T).* Write the injection as \(i\) and the surjection as \(p\). With the cone convention \(d(b,a)=(d_Bb+i(a),-d_Aa)\), the map
  \[
  q:\operatorname{Cone}(i)\longrightarrow C,\qquad q(b,a)=p(b)
  \]
  is a chain map and termwise onto. Its kernel identifies with \(A^n\oplus A^{n+1}\) in degree \(n\), with differential \((a,a')\mapsto(d_Aa+a',-d_Aa')\). The degree-minus-one map \(h(a,a')=(0,a)\) satisfies \(dh+hd=1\). Hence the kernel is contractible, and the cohomology exact sequence makes \(q\) a quasi-isomorphism. Transport the cone triangle \(A\to B\to\operatorname{Cone}(i)\to A[1]\) along \(q\), which is invertible in \(D\). Its first two arrows are the given ones. A commuting diagram of short exact sequences gives a commuting diagram of these cones and their maps \(q\); inverting \(q\) proves naturality. With the alternative convention for the last cone arrow, negate the last arrow throughout, as explained in Section 13. This proof uses the defining cone triangles of the derived category, not an assumption about injective resolutions. \(\square\)

<span id="SH-FND-DC-02"></span><span id="sh-fnd-dc-02"></span>

## 2. Module sheaves form an abelian category

**Theorem 2.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\).

1. \(\operatorname{Mod}(\mathcal O)\) is additive. A morphism \(\varphi:F\to G\) has a kernel, computed on sections: \((\operatorname{Ker}\varphi)(U)=\ker\varphi_U\). It has a cokernel: the sheafification of \(U\mapsto\operatorname{coker}\varphi_U\).
2. For each \(x\), the stalk functor \(F\mapsto F_x\), from \(\operatorname{Mod}(\mathcal O)\) to \(\operatorname{Mod}(\mathcal O_x)\), is additive, and \((\operatorname{Ker}\varphi)_x=\ker\varphi_x\), \((\operatorname{Coker}\varphi)_x=\operatorname{coker}\varphi_x\).
3. \(\operatorname{Mod}(\mathcal O)\) is abelian, and each stalk functor is exact.
4. A sequence \(F\to G\to H\) with zero composite is exact at \(G\) if and only if \(F_x\to G_x\to H_x\) is exact at \(G_x\) for every \(x\). A morphism \(\varphi\) is a monomorphism (epimorphism, isomorphism) if and only if every \(\varphi_x\) is one.

*Reference:* [Stacks, Tag 01AG] proves (3) and (4) for commutative \(\mathcal O\); the same arguments apply to any sheaf of rings, since kernels and cokernels are computed stalkwise and no commutativity is used.

**Proof.** (1) Morphisms add on sections, and composition is bilinear. The zero sheaf is a zero object. Finite direct sums are formed on sections: \(U\mapsto F(U)\oplus G(U)\) is a sheaf, because sections glue coordinatewise. Let \(\varphi:F\to G\). The presheaf \(U\mapsto\ker\varphi_U\) is a sheaf. Indeed, let a section \(s\) of \(F\) lie in the kernel on each set of an open cover. Then \(\varphi(s)\) vanishes on that cover, so \(\varphi(s)=0\), since \(G\) is a sheaf. Sections of the kernel that agree on overlaps glue in \(F\), and by this remark the glued section lies in the kernel. Each \(\varphi_U\) is \(\mathcal O(U)\)-linear, so the kernel is a subpresheaf of left modules. A morphism \(E\to F\) whose composite with \(\varphi\) is zero lands in it on every open set. So it is the kernel. For the cokernel, let \(P(U)=\operatorname{coker}\varphi_U\), a presheaf of left \(\mathcal O\)-modules. By (S), morphisms \(P^+\to H\) into a sheaf \(H\) correspond to morphisms of presheaves \(P\to H\). These are the morphisms \(G\to H\) that vanish after \(\varphi\). So \(P^+\) is the cokernel.

(2) The stalk \(F_x=\varinjlim_{U\ni x}F(U)\) is a left module over \(\mathcal O_x=\varinjlim_{U\ni x}\mathcal O(U)\), and the functor is additive. The open neighbourhoods of \(x\) form a filtered system, and filtered colimits are exact (F). Hence \((\operatorname{Ker}\varphi)_x=\varinjlim_U\ker\varphi_U=\ker\varphi_x\). By (S), \(\theta\) is bijective on stalks, so \((P^+)_x=P_x\); and by (F) again, \(P_x=\varinjlim_U\operatorname{coker}\varphi_U=\operatorname{coker}\varphi_x\).

(3) The coimage of \(\varphi\) is the cokernel of \(\operatorname{Ker}\varphi\to F\). The image is the kernel of \(G\to\operatorname{Coker}\varphi\). By (2), at each \(x\) the canonical map \(\operatorname{Coim}\varphi\to\operatorname{Im}\varphi\) becomes the canonical map \(\operatorname{Coim}\varphi_x\to\operatorname{Im}\varphi_x\) of \(\mathcal O_x\)-modules. That map is an isomorphism, because modules over a ring form an abelian category. By (I) the map of sheaves is an isomorphism. Its inverse is \(\mathcal O\)-linear, as the map is. So \(\operatorname{Mod}(\mathcal O)\) is abelian. The stalk functor preserves kernels and cokernels by (2), so it is exact.

(4) Exactness at \(G\) means that \(\operatorname{Im}(F\to G)\to\operatorname{Ker}(G\to H)\) is an isomorphism. Both sides are built from kernels and cokernels. By (2), the map at \(x\) is the same map for the stalk sequence. If every stalk sequence is exact, (I) gives exactness. Conversely, exact functors preserve exactness. A sheaf whose stalks all vanish is zero, since each section then vanishes on an open cover. Hence \(\varphi\) is a monomorphism iff \(\operatorname{Ker}\varphi=0\) iff every \(\ker\varphi_x=0\). The same holds with cokernels. An isomorphism is a morphism that is both. \(\square\)

The proof never uses commutativity of \(\mathcal O\). In particular, Theorem 2.1 holds for the constant sheaf \(k_X\) of any unital ring \(k\), commutative or not.

<span id="SH-FND-DC-03"></span><span id="sh-fnd-dc-03"></span>

## 3. Limits, colimits, stalks, and sections of sums

**Theorem 3.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\).

1. Every small diagram \((F_i)\) in \(\operatorname{Mod}(\mathcal O)\) has a limit, computed on sections. So \(\Gamma(U,-)\) commutes with limits.
2. Every small diagram has a colimit: the sheafification of the presheaf colimit. Stalks commute with colimits: \((\varinjlim_iF_i)_x=\varinjlim_i(F_i)_x\).
3. Filtered colimits are exact.
4. Finite direct sums are computed on sections.
5. If \(U\) is a quasi-compact open set, the canonical map \(\bigoplus_i\Gamma(U,F_i)\to\Gamma(U,\bigoplus_iF_i)\) is bijective for every family. Without quasi-compactness it can fail to be onto (Example 2).
6. Products exist and are computed on sections, but they need not be exact (Example 3).

*Reference:* [Stacks, Tag 01AH], for parts (1)–(4) and commutative \(\mathcal O\).

**Proof.** (1) Let \(L(U)=\varprojlim_iF_i(U)\), with coordinatewise restriction and module structure. It is a sheaf. A local section on a cover is a compatible family on each piece. Glue each coordinate in \(F_i\). The glued coordinates again form a compatible family, because the transition maps are morphisms of sheaves and sections of a sheaf are determined locally. A morphism \(E\to L\) is the same as a compatible family of morphisms \(E\to F_i\), open set by open set. So \(L\) is the limit, and \(\Gamma(U,L)=\varprojlim_i\Gamma(U,F_i)\).

(2) Let \(P(U)=\varinjlim_iF_i(U)\). By (S), morphisms \(P^+\to H\) into a sheaf correspond to compatible families of morphisms \(F_i\to H\). So \(P^+\) is the colimit. At \(x\),
\[
(P^+)_x=P_x=\varinjlim_{U\ni x}\varinjlim_iF_i(U)=\varinjlim_i\varinjlim_{U\ni x}F_i(U)=\varinjlim_i(F_i)_x ,
\]
since colimits commute with colimits.

(3) Let \(0\to A_i\to B_i\to C_i\to0\) be exact, naturally in \(i\) over a filtered category. At each \(x\), by (2), the stalk sequence of the colimits is the filtered colimit of the exact sequences \(0\to(A_i)_x\to(B_i)_x\to(C_i)_x\to0\). It is exact by (F). Since exactness is checked on stalks ([Theorem 2.1](#sh-fnd-dc-02)(4)), the colimit sequence is exact.

(4) This was shown in the proof of [Theorem 2.1](#sh-fnd-dc-02)(1).

(5) Let \(S=\bigoplus_iF_i\), the sheafification of \(P(V)=\bigoplus_iF_i(V)\). The germ at \(x\) of \(p=(p_i)\in P(V)\) is \((p_{i,x})_i\in\bigoplus_i(F_i)_x\). If all germs of \(p\) vanish, each \(p_i\) has zero germs and is zero. So \(P\) is separated, and \(\theta:P(V)\to S(V)\) is injective for every \(V\). For \(V=U\) this is the injectivity of the canonical map. For surjectivity, let \(t\in S(U)\). By (S), every point of \(U\) has an open neighbourhood \(V\subset U\) and some \(p\in P(V)\) with \(\theta(p)=t|_V\). As \(U\) is quasi-compact, finitely many such pairs \((V_1,p_1),\ldots,(V_m,p_m)\) cover \(U\). Each \(p_k\) has finitely many nonzero coordinates. Let \(J\) be the finite set of indices that occur, and \(S_J=\bigoplus_{i\in J}F_i\). By (4), \(S_J\) is a sheaf. It is also a subpresheaf of \(P\) that contains all \(p_k\). On \(V_k\cap V_l\), the restrictions of \(p_k\) and \(p_l\) have the same image under the injective map \(\theta\), so they are equal. Glue them to \(s\in S_J(U)=\bigoplus_{i\in J}F_i(U)\). Then \(\theta(s)\) and \(t\) agree on each \(V_k\), so \(\theta(s)=t\).

(6) Products are limits, so (1) applies. Example 3 shows that a product of epimorphisms need not be an epimorphism. \(\square\)

The proofs use no commutativity of \(\mathcal O\). A related fact, not used here, is the analogue of (5) for filtered colimits: on a compact Hausdorff space \(X\), global sections commute with filtered colimits of sheaves. The key step is that sections over a compact subset are germs of sections over its open neighbourhoods [Schapira, *Algebra and Topology*, Proposition 5.6.1].

<span id="SH-FND-DC-04"></span><span id="sh-fnd-dc-04"></span>

## 4. Exact inverse image

**Theorem 4.1.** Let \(f:X\to Y\) be continuous and \(\mathcal O_Y\) a sheaf of rings on \(Y\).

1. On \(X\), \(f^{-1}\mathcal O_Y\) is a sheaf of rings, with stalks \((f^{-1}\mathcal O_Y)_x=\mathcal O_{Y,f(x)}\). For \(G\in\operatorname{Mod}(\mathcal O_Y)\), \(f^{-1}G\) is a sheaf of left \(f^{-1}\mathcal O_Y\)-modules, and the canonical map \(G_{f(x)}\to(f^{-1}G)_x\) is an isomorphism of \(\mathcal O_{Y,f(x)}\)-modules.
2. \(f^{-1}:\operatorname{Mod}(\mathcal O_Y)\to\operatorname{Mod}(f^{-1}\mathcal O_Y)\) is exact and commutes with colimits.
3. For a unital ring \(k\), \(f^{-1}k_Y=k_X\) as sheaves of rings. So \(f^{-1}:\operatorname{Mod}(k_Y)\to\operatorname{Mod}(k_X)\) is exact, and \((f^{-1}G)_x=G_{f(x)}\) as \(k\)-modules. This holds for every unital ring \(k\), commutative or not.
4. \(f^{-1}\) is left adjoint to \(f_*:\operatorname{Mod}(f^{-1}\mathcal O_Y)\to\operatorname{Mod}(\mathcal O_Y)\).

All four assertions are proved below. *Historical references:* [Schapira, *Algebra and Topology*, Chapter 5]; [Stacks, Tag 01AJ] for exactness on sheaves of abelian groups.

**Proof of (1)–(3).** Recall that \(f^{-1}G\) is the sheafification of the presheaf \(V\mapsto\varinjlim_{W\supset f(V)}G(W)\), where \(W\) runs over the open sets containing \(f(V)\). We use its description by germs. For \(V\subset X\) open, \(f^{-1}G(V)\) is the set of maps \(s\) that give each \(x\in V\) an element \(s(x)\in G_{f(x)}\), such that each point of \(V\) has an open neighbourhood \(V'\subset V\), an open \(W\supset f(V')\) and a section \(g\in G(W)\) with \(s(x')=g_{f(x')}\) for all \(x'\in V'\). The condition is local, so this is a sheaf of sets. Take \(G=\mathcal O_Y\) to get \(f^{-1}\mathcal O_Y\). Sum, product and the action are defined pointwise, through the ring \(\mathcal O_{Y,f(x)}\) and its module \(G_{f(x)}\). They preserve the local condition: if near a point \(s\) is represented by \(g\in G(W)\) and \(a\) by \(h\in\mathcal O_Y(W')\), then near that point \(as\) is represented by \(h|_{W\cap W'}\,g|_{W\cap W'}\). This gives the ring and module structures. Evaluation at \(x\) is a ring map, and a module map over it.

Evaluation \((f^{-1}G)_x\to G_{f(x)}\) is onto: \(g\in G(W)\) with \(W\ni f(x)\) defines a section over \(f^{-1}(W)\). It is one-to-one: if \(s(x)=0\), represent \(s\) near \(x\) by \(g\in G(W)\). Then \(g_{f(x)}=0\), so \(g\) vanishes on an open \(W_0\ni f(x)\), and \(s\) vanishes on \(V'\cap f^{-1}(W_0)\). The canonical map \(G_{f(x)}\to(f^{-1}G)_x\) sends the germ of \(g\) to the germ of the section defined by \(g\). It is inverse to evaluation. This proves (1).

(2) Exactness can be checked on stalks ([Theorem 2.1](#sh-fnd-dc-02)(4)). By (1), the stalk of \(f^{-1}G\) at \(x\) is \(G_{f(x)}\), so on stalks \(f^{-1}\) acts as the identity, and \(f^{-1}\) is exact. For a colimit, the canonical map \(\varinjlim_if^{-1}G_i\to f^{-1}\varinjlim_iG_i\) is, at \(x\), the map \(\varinjlim_i(G_i)_{f(x)}\to(\varinjlim_iG_i)_{f(x)}\). This map is bijective, because stalks commute with colimits ([Theorem 3.1](#sh-fnd-dc-03)(2)). So the canonical map is an isomorphism by (I).

(3) A germ of a section of \(k_Y\) is the germ of a locally constant function. So the sections of \(f^{-1}k_Y\) over \(V\) are the maps \(V\to k\) that are constant near each point, that is, the sections of \(k_X\). The ring operations agree pointwise. The argument never uses commutativity of \(k\). \(\square\)

**Proof of (4).** Let \(G\) be an \(\mathcal O_Y\)-module and \(F\) an \(f^{-1}\mathcal O_Y\)-module. A map \(\alpha:f^{-1}G\to F\) sends a section \(g\in G(W)\) to the image under \(\alpha\) of its pullback section on \(f^{-1}(W)\). This defines
\[
\beta_W:G(W)\longrightarrow F(f^{-1}(W))=(f_*F)(W).
\]
The maps commute with restriction and are \(\mathcal O_Y(W)\)-linear through the canonical map \(\mathcal O_Y(W)\to(f^{-1}\mathcal O_Y)(f^{-1}(W))\).

Conversely, suppose \(\beta:G\to f_*F\) is \(\mathcal O_Y\)-linear. Locally a section \(s\) of \(f^{-1}G\) on \(V\) is represented by a section \(g\in G(W)\), with \(f(V)\subset W\). Send it to \(\beta_W(g)|_V\). If two representatives have the same germ at \(x\), their germs in \(G_{f(x)}\) agree, so they agree on some smaller neighbourhood \(W'\) of \(f(x)\). Their proposed images therefore agree near \(x\). This proves independence of representatives; the proposed local images glue uniquely. Multiplication is checked after locally representing the scalar by a section of \(\mathcal O_Y\), so the glued map is \(f^{-1}\mathcal O_Y\)-linear. The two constructions undo one another on local representatives, and hence everywhere. They commute with maps of \(G\) and \(F\); this is the adjunction. \(\square\)

**Remark 4.2.** For a morphism of ringed spaces \(f:(X,\mathcal O_X)\to(Y,\mathcal O_Y)\), the module pullback \(f^*=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}(-)\) is only right exact, and Example 5 shows that it can fail to be exact. When the structure map \(f^{-1}\mathcal O_Y\to\mathcal O_X\) is an isomorphism, it identifies \(f^*\) with the exact functor \(f^{-1}\). The comparison is through this specified structure map, not an unlabelled equality of coefficient sheaves.

<span id="SH-FND-DC-05"></span><span id="sh-fnd-dc-05"></span>

## 5. Enough injectives, functorially

Theorem 5.4 embeds every sheaf of modules into a product of skyscraper sheaves, one at each point, built from injective modules that contain the stalks. Choosing such an injective module separately for each stalk would already give enough injectives. The explicit construction of Lemma 5.1 makes the embedding a functor, for modules over any ring.

**Lemma 5.1 (functorial injective embeddings of modules).** Let \(A\) be a ring. Put \(E_A=\operatorname{Hom}_{\mathbb Z}(A,\mathbb Q/\mathbb Z)\), a left \(A\)-module by \((a\varphi)(b)=\varphi(ba)\). For a left \(A\)-module \(M\) put
\[
I_A(M)=\prod_{\varphi\in\operatorname{Hom}_A(M,E_A)}E_A,\qquad \iota_M(m)=(\varphi(m))_\varphi .
\tag{5.1}
\]
Then \(I_A(M)\) is injective and \(\iota_M\) is injective. For \(u:M\to N\), the formula \(I_A(u)\bigl((y_\varphi)_\varphi\bigr)=(y_{\chi\circ u})_{\chi}\), with \(\chi\) running over \(\operatorname{Hom}_A(N,E_A)\), makes \(I_A\) a functor and \(\iota\) a natural transformation.

**Proof.** \(E_A\) is a left module: \(((aa')\varphi)(b)=\varphi(baa')=(a(a'\varphi))(b)\). The maps
\[
\Phi(\varphi)=\bigl(m\mapsto\varphi(m)(1)\bigr),\qquad \Psi(\psi)=\bigl(m\mapsto(b\mapsto\psi(bm))\bigr)
\]
are inverse bijections between \(\operatorname{Hom}_A(M,E_A)\) and \(\operatorname{Hom}_{\mathbb Z}(M,\mathbb Q/\mathbb Z)\), natural in \(M\). Here \(\Psi(\psi)\) is \(A\)-linear, since \(\Psi(\psi)(am)(b)=\psi(bam)=(a\,\Psi(\psi)(m))(b)\). The group \(\mathbb Q/\mathbb Z\) is an injective \(\mathbb Z\)-module. To see this, use Baer's criterion (B): the ideals of \(\mathbb Z\) are the \(n\mathbb Z\). For \(n=0\) there is nothing to extend. For \(n\geq1\), a map \(n\mathbb Z\to\mathbb Q/\mathbb Z\) sending \(n\) to \(q\) extends to \(\mathbb Z\) by sending \(1\) to any \(q'\) with \(nq'=q\), which exists since \(\mathbb Q/\mathbb Z\) is divisible. Exact sequences of \(A\)-modules are exact as groups. So \(\operatorname{Hom}_A(-,E_A)\cong\operatorname{Hom}_{\mathbb Z}(-,\mathbb Q/\mathbb Z)\) is exact, and \(E_A\) is injective. A product of injectives is injective, because \(\operatorname{Hom}(-,\prod E)=\prod\operatorname{Hom}(-,E)\) and products of exact sequences of groups are exact. So \(I_A(M)\) is injective. If \(m\neq0\), define \(\psi\) on the subgroup \(\mathbb Zm\) by \(\psi(m)=1/n+\mathbb Z\) if \(m\) has finite order \(n\geq2\), and \(\psi(m)=1/2+\mathbb Z\) if \(m\) has infinite order. Extend \(\psi\) to \(M\), as \(\mathbb Q/\mathbb Z\) is injective. Then \(\varphi=\Psi(\psi)\) has \(\varphi(m)(1)=\psi(m)\neq0\), so \(\iota_M(m)\neq0\). Finally \(I_A(u)(\iota_M(m))=(\chi(u(m)))_\chi=\iota_N(u(m))\), and the displayed formula gives \(I_A(vu)=I_A(v)I_A(u)\) and \(I_A(\mathrm{id})=\mathrm{id}\). \(\square\)

**Lemma 5.2 (extension by zero from an open set).** Let \(j:U\hookrightarrow X\) be open and \(B\) a sheaf of left \(\mathcal O|_U\)-modules. For \(V\subset X\) open put
\[
j_!B(V)=\{\,s\in B(U\cap V):\ \operatorname{supp}s\text{ is closed in }V\,\}.
\]
1. \(j_!B\) is a sheaf of left \(\mathcal O\)-modules, with \((j_!B)_x=B_x\) for \(x\in U\) and \((j_!B)_x=0\) for \(x\notin U\). So \(j_!\) is exact.
2. \(\operatorname{Hom}_{\mathcal O}(j_!B,G)\cong\operatorname{Hom}_{\mathcal O|_U}(B,G|_U)\), naturally in \(B\) and \(G\).
3. \(\operatorname{Hom}_{\mathcal O}(j_!\mathcal O_U,G)\cong G(U)\) by \(\varphi\mapsto\varphi(1)\). For opens \(V\subset W\), the morphism \(j_{V!}\mathcal O_V\to j_{W!}\mathcal O_W\) that corresponds to \(1\in\mathcal O(V)=(j_{W!}\mathcal O_W)(V)\) is a monomorphism, and under these identifications it induces restriction \(G(W)\to G(V)\).

**Proof.** (1) Supports of sections are closed in their domains. Closedness of a support in \(V\) is a local condition on \(V\), so sections of \(B\) glue within \(j_!B\), and \(j_!B\) is a sheaf. Module operations do not enlarge supports. If \(x\in U\), the opens inside \(U\) are cofinal among neighbourhoods of \(x\), and there \(j_!B=B\); so \((j_!B)_x=B_x\). If \(x\notin U\) and \(s\in j_!B(V)\) with \(x\in V\), then \(x\notin\operatorname{supp}s\), and this support is closed in \(V\); so \(s\) vanishes near \(x\) and the stalk is \(0\). Exactness is checked on stalks ([Theorem 2.1](#sh-fnd-dc-02)(4)), and on each stalk \(j_!\) acts as the identity or as zero; so \(j_!\) is exact.

(2) A morphism \(j_!B\to G\) restricts over \(U\) to a morphism \(B\to G|_U\). Conversely, let \(\alpha:B\to G|_U\) and \(s\in j_!B(V)\). The section \(\alpha(s)\) on \(U\cap V\) and the section \(0\) on \(V\setminus\operatorname{supp}s\) agree on the overlap. The two open sets cover \(V\), because \(\operatorname{supp}s\subset U\cap V\). Glue them to a section of \(G\) over \(V\). This defines the inverse bijection; linearity and naturality are checked on the two pieces.

(3) By (2), a morphism \(j_!\mathcal O_U\to G\) is a left-linear map \(\mathcal O_U\to G|_U\), and such a map is \(a\mapsto as\) with \(s\) the image of \(1\in\mathcal O(U)\). For \(V\subset W\), \((j_{W!}\mathcal O_W)(V)=\mathcal O(V)\). At \(x\in V\) the morphism is the identity of \(\mathcal O_x\); at other points its source stalk is \(0\). So it is injective on every stalk, hence a monomorphism by [Theorem 2.1](#sh-fnd-dc-02)(4). Composing with it sends the morphism with \(\varphi(1)=s\in G(W)\) to the one with value \(s|_V\) at \(1\). \(\square\)

**Lemma 5.3 (skyscrapers).** Let \(x\in X\) and let \(J\) be a left \(\mathcal O_x\)-module. Put \(x_*J(V)=J\) if \(x\in V\) and \(0\) otherwise, with identity restrictions between opens containing \(x\), and let \(\mathcal O(V)\) act through \(\mathcal O(V)\to\mathcal O_x\). Then \(x_*J\) is a sheaf of left \(\mathcal O\)-modules, and
\[
\operatorname{Hom}_{\mathcal O}(F,x_*J)\cong\operatorname{Hom}_{\mathcal O_x}(F_x,J),
\tag{5.2}
\]
naturally in \(F\) and \(J\). If \(J\) is injective, then \(x_*J\) is injective.

**Proof.** Let \(x\in V\) and let \((V_i)\) cover \(V\). Some \(V_i\) contains \(x\). Compatible sections agree on all \(V_i\) that contain \(x\), since their pairwise overlaps contain \(x\); this common value is the glued section, and it is unique. If \(x\notin V\), all sections are \(0\). A morphism \(\varphi:F\to x_*J\) has components \(\varphi_V\), for \(x\in V\), that are compatible with restriction. So they define an \(\mathcal O_x\)-linear map \(F_x\to J\). Conversely, given \(g:F_x\to J\), put \(\varphi_V(s)=g(s_x)\) if \(x\in V\) and \(0\) otherwise. These constructions are inverse. If \(J\) is injective, \(\operatorname{Hom}_{\mathcal O}(-,x_*J)\cong\operatorname{Hom}_{\mathcal O_x}((-)_x,J)\) is exact, because the stalk functor is exact ([Theorem 2.1](#sh-fnd-dc-02)(3)). \(\square\)

**Theorem 5.4 (functorial injective embeddings).** Let \(\mathcal O\) be any sheaf of rings on \(X\). Put
\[
E(F)=\prod_{x\in X}x_*\bigl(I_{\mathcal O_x}(F_x)\bigr),
\]
where \(I_{\mathcal O_x}\) is the functor (5.1) for the ring \(\mathcal O_x\), and let \(\iota_F:F\to E(F)\) have \(x\)-component the morphism that corresponds under (5.2) to \(\iota_{F_x}:F_x\to I_{\mathcal O_x}(F_x)\). Then \(E(F)\) is injective, \(\iota_F\) is a monomorphism, and \(E\) is a functor with \(\iota\) natural. So \(\operatorname{Mod}(\mathcal O)\) has enough injectives, with functorial injective embeddings.

*Reference:* [Stacks, Tag 01DI] gives functorial injective embeddings for commutative \(\mathcal O\).

**Proof.** Products exist and are computed on sections ([Theorem 3.1](#sh-fnd-dc-03)(1)), and a product of injectives is injective, as in the proof of Lemma 5.1. Each factor is injective by Lemmas 5.1 and 5.3. Explicitly, \(\iota_F\) sends \(s\in F(V)\) to \((\iota_{F_x}(s_x))_{x\in V}\). If this is zero, each \(s_x=0\), as \(\iota_{F_x}\) is injective, so \(s=0\). Kernels are computed on sections ([Theorem 2.1](#sh-fnd-dc-02)(1)), so \(\iota_F\) is a monomorphism. For \(u:F\to G\) put \(E(u)=\prod_xx_*(I_{\mathcal O_x}(u_x))\). Naturality of \(\iota\) holds factor by factor, by Lemma 5.1. \(\square\)

**Corollary 5.5.** (1) Every injective \(\mathcal O\)-module is flabby. (2) For \(U\) open, the restriction of an injective \(\mathcal O\)-module \(I\) to \(U\) is an injective \(\mathcal O|_U\)-module.

**Proof.** (1) For \(V\subset W\), Lemma 5.2(3) gives a monomorphism \(j_{V!}\mathcal O_V\to j_{W!}\mathcal O_W\). Applying the exact functor \(\operatorname{Hom}(-,I)\) turns it into the restriction \(I(W)\to I(V)\), which is therefore onto. Take \(W=X\). (2) By Lemma 5.2(2), \(\operatorname{Hom}_{\mathcal O|_U}(-,I|_U)\cong\operatorname{Hom}_{\mathcal O}(j_!(-),I)\). This is a composite of exact functors. \(\square\)

<span id="SH-FND-DC-06"></span><span id="sh-fnd-dc-06"></span>

## 6. Right derived functors on bounded-below complexes

**Theorem 6.1.** Let \(\mathcal A\) and \(\mathcal B\) be abelian, and assume that every object of \(\mathcal A\) embeds in an injective object. Let \(\Phi:\mathcal A\to\mathcal B\) be additive.

1. Every bounded-below complex \(K\) has a qis \(K\to I\) into a bounded-below complex of injectives. If \(K^n=0\) for \(n<a\), it can be chosen injective in each degree, with \(I^n=0\) for \(n<a\).
2. Such an \(I\) is K-injective (Lemma 6.2). Hence \(\operatorname{Hom}_{K(\mathcal A)}(L,I)=\operatorname{Hom}_{D(\mathcal A)}(L,I)\) for every \(L\). A morphism into \(I\) extends along a qis, uniquely up to homotopy.
3. The rule \(R\Phi(K)=\Phi(I)\) gives a triangulated functor \(D^+(\mathcal A)\to D^+(\mathcal B)\), and this functor is the right derived functor \(R\Phi\). If \(\Phi\) is left exact, \(R^0\Phi=\Phi\) and \((R^i\Phi)_i\) is a universal \(\delta\)-functor.
4. (Leray) If \(\Phi\) is left exact and \(J\) is a bounded-below complex with \(R^i\Phi(J^n)=0\) for all \(i>0\) and all \(n\), then \(\Phi(J)\to R\Phi(J)\) is an isomorphism. Left exactness cannot be dropped. For a general additive \(\Phi\), the terms must also satisfy \(\Phi(J^n)\cong R^0\Phi(J^n)\), which holds by (3) when \(\Phi\) is left exact. For \(\Phi=-\otimes_{\mathbb Z}\mathbb Z/2\) on \(\operatorname{Mod}(\mathbb Z)\) and \(J=\mathbb Z\) in degree \(0\), the injective resolution \(\mathbb Q\to\mathbb Q/\mathbb Z\) gives \(R\Phi(\mathbb Z)=0\), because \(\mathbb Q\) and \(\mathbb Q/\mathbb Z\) are divisible, while \(\Phi(\mathbb Z)=\mathbb Z/2\).
5. For \(\mathcal A=\operatorname{Mod}(\mathcal O)\), with \(\mathcal O\) any sheaf of rings, (1)–(4) hold by Theorem 5.4. This gives \(Rf_*\), \(R\Gamma(U,-)\), the sheaf \(R\Gamma_Z\) of sections with support (Section 1) and \(R\operatorname{Hom}_{\mathcal O}(G,-)\) on \(D^+\).

We first prove the resolution assertion, then the comparison and derived-functor assertions. The localization \(K(\mathcal A)\to D(\mathcal A)\) and elementary cohomology exact sequences are the categorical background specified in Section 1, not extra existence assumptions about resolutions. *Sources:* [AI Integrated Stacks Project, derived.tex], the lemmas labelled \(\texttt{lemma-subcategory-right-resolution}\), \(\texttt{lemma-injective-resolutions-exist}\), \(\texttt{lemma-K-injective}\), and \(\texttt{lemma-leray-acyclicity}\). The explicit construction and expanded checks below are by OpenAI GPT-6 Astra in Codex, Ultra effort.

### Constructing the bounded-below resolution

**Proof of Theorem 6.1(1).** The elementary operation is to replace one term of a complex by an injective object. Suppose \(C\) is a complex and choose a monomorphism \(u:C^n\to E\), with \(E\) injective. Form the pushout
\[
P=(E\oplus C^{n+1})/\operatorname{im}(u,-d_C^n).
\]
Replace \(C^n\) by \(E\) and \(C^{n+1}\) by \(P\). The incoming differential is \(u d_C^{n-1}\), the new differential \(E\to P\) sends \(e\) to \([e,0]\), and the outgoing differential sends \([e,c]\) to \(d_C^{n+1}c\). These maps square to zero: \([u(c),0]=[0,d_Cc]\), and \(d_C^2=0\). This gives a complex \(C'\) and a chain map \(C\to C'\).

The map \(C^{n+1}\to P\) is a monomorphism: its kernel would come from an element \((u(c),-d_Cc)\) with \(u(c)=0\), hence \(c=0\). This statement also follows directly from the kernel universal property of the pushout in an abelian category, so it does not presume that objects have underlying elements. The map of complexes is termwise monic. Its quotient is the two-term complex
\[
E/u(C^n)\ \xrightarrow{\ 1\ }\ E/u(C^n)
\]
in degrees \(n,n+1\), and zero in other degrees. It is contractible, so the cohomology exact sequence proves that \(C\to C'\) is a quasi-isomorphism.

Start at \(n=a\), then perform the operation at \(a+1,a+2,\ldots\). Once degree \(n\) has been replaced, later operations leave that object unchanged; once degree \(n+1\) has been replaced, the differential out of degree \(n\) is unchanged as well. Define \(I\) using these eventual objects and differentials. This uses no infinite colimit in \(\mathcal A\): each degree is defined at a finite stage. All its terms are injective, it is zero below \(a\), and the map \(K\to I\) is termwise monic. For fixed \(r\), the three terms and two differentials computing \(H^r\) have stabilized after finitely many steps. Every step was a quasi-isomorphism, so \(H^r(K)\to H^r(I)\) is an isomorphism. This proves (1). \(\square\)

**Lemma 6.2 (bounded-below complexes of injectives are K-injective).** Let \(I\) be a complex of injectives with \(I^n=0\) for \(n<a\), and let \(A\) be acyclic. Then every chain map \(f:A\to I\) is null-homotopic.

**Proof.** We build maps \(s^n:A^n\to I^{n-1}\) with
\[
f^n=d\,s^n+s^{n+1}d\qquad\text{for all }n .
\tag{6.1}
\]
Put \(s^n=0\) for \(n\leq a\). Then (6.1) holds for \(n<a\), where both sides are \(0\). Suppose \(s^k\) is built for \(k\leq n\) and (6.1) holds for all indices below \(n\). Put \(g=f^n-d\,s^n:A^n\to I^n\). Using (6.1) at \(n-1\), and \(d^2=0\),
\[
g\,d=f^nd-d\,s^nd=d\,f^{n-1}-d\bigl(f^{n-1}-d\,s^{n-1}\bigr)=0 .
\]
So \(g\) vanishes on the image of \(d:A^{n-1}\to A^n\). As \(A\) is acyclic, that image is the kernel of \(d:A^n\to A^{n+1}\). Hence \(h(da)=g(a)\) is a well-defined map from the image of \(d\) in \(A^{n+1}\) to \(I^n\). Since \(I^n\) is injective, \(h\) extends to \(s^{n+1}:A^{n+1}\to I^n\). Then \(s^{n+1}d=g\), which is (6.1) at \(n\). \(\square\)

The induction needs a place to start. Example 1 shows that without a lower bound the conclusion fails. A special case has a second proof: if \(I\) is itself acyclic, it splits and is contractible, so every chain map into it is null-homotopic.

### Comparing resolutions and defining the derived functor

**Lemma 6.3 (maps into a K-injective complex).** For a K-injective \(I\), a quasi-isomorphism \(s:M\to N\) induces a bijection
\[
s^*:\operatorname{Hom}_{K(\mathcal A)}(N,I)
\longrightarrow\operatorname{Hom}_{K(\mathcal A)}(M,I).
\]
Consequently the natural map from either homotopy-category Hom group to the corresponding derived-category Hom group with target \(I\) is bijective. This proves background assertion (H).

**Proof.** The complex \(\operatorname{Hom}^\bullet(A,I)\) is acyclic when \(A\) is acyclic: its degree-\(r\) cohomology is \(\operatorname{Hom}_{K(\mathcal A)}(A,I[r])\), which vanishes because a shift of \(A\) is again acyclic. Put \(U=\operatorname{Hom}^\bullet(N,I)\), \(V=\operatorname{Hom}^\bullet(M,I)\), and \(u=s^*:U\to V\). In degree \(r\), write a map out of \(\operatorname{Cone}(s)\) as \((a,b)\in U^r\oplus V^{r-1}\). Its differential is
\[
(a,b)\longmapsto (d_Ua,\ d_Vb+(-1)^{r+1}u(a)).
\]
Thus \((a,b)\mapsto((-1)^{r-1}b,a)\) is a chain isomorphism onto \(\operatorname{Cone}(u)[-1]\): its differential is \((v,a)\mapsto(-d_Vv-u(a),d_Ua)\). This explicitly identifies the Hom complex out of \(\operatorname{Cone}(s)\) with the shifted cone of
\[
\operatorname{Hom}^\bullet(N,I)\longrightarrow
\operatorname{Hom}^\bullet(M,I).
\]
The cone of \(s\) is acyclic. Thus this map of Hom complexes is a quasi-isomorphism; its degree-zero cohomology gives the displayed bijection.

Here is a direct use of the localization universal property that avoids assuming a choice of roofs. The contravariant functor \(H(L)=\operatorname{Hom}_K(L,I)\) sends every quasi-isomorphism to an isomorphism by the first paragraph, so it factors through \(D(\mathcal A)^{\mathrm{op}}\). For \(v:L\to I\) in \(D\), apply this factored functor to \(v\) and to the element \(1_I\); this gives an element of \(\operatorname{Hom}_K(L,I)\). The resulting map is inverse to the natural map into \(\operatorname{Hom}_D(L,I)\): one composite fixes every chain-homotopy class, and the other is a natural endomorphism of the representable functor \(\operatorname{Hom}_D(-,I)\) fixing \(1_I\). Naturality for inverted quasi-isomorphisms follows by inverting their naturality squares. Every derived morphism is generated by ordinary morphisms and these inverses, so the second composite fixes all morphisms too. \(\square\)

**Proof of Theorem 6.1(2)–(3), and of (D).** Choose a resolution \(q_K:K\to I_K\). For bounded-below \(K\), use part (1); for (D), use the existence assumed in that assertion. A chain map \(f:K\to L\) has a unique homotopy-class extension \(\bar f:I_K\to I_L\) satisfying \(\bar f q_K=q_L f\) in \(K(\mathcal A)\), by Lemma 6.3. Uniqueness proves compatibility with composition and identities. If \(f\) is a quasi-isomorphism, \(\bar f\) is one too. A quasi-isomorphism between K-injectives is a homotopy equivalence: apply Lemma 6.3 first to obtain a left inverse and again to show the other composite is the identity.

An additive \(\Phi\) preserves chain homotopies, shifts and mapping cones, since these involve only finite direct sums, differentials and sums of maps. Therefore \(\Phi(\bar f)\) is invertible in \(K(\mathcal B)\) whenever \(\bar f\) is a homotopy equivalence. The assignment \(K\mapsto\Phi(I_K)\) consequently factors through \(D(\mathcal A)\). Different choices of \(I_K\) give a unique natural comparison isomorphism: extend the identity of \(K\) between the two resolutions and apply the preceding argument. These comparisons satisfy the cocycle identity by uniqueness. For bounded-below inputs all resolutions can be bounded below, so the values lie in \(D^+(\mathcal B)\).

The functor is triangulated. Shifts of K-injectives are K-injective, and the cone of a map between K-injectives is K-injective: apply \(\operatorname{Hom}^\bullet(A,-)\) for acyclic \(A\); its cone has zero cohomology because both end complexes do. Every triangle in \(D\) is isomorphic to the image of a cone triangle, and comparison with these K-injective cones reduces the claim to the fact that \(\Phi\) preserves cones and shifts.

For clarity, the universal property is also included. Applying \(\Phi\) to \(q_K\) gives a natural comparison
\(\eta_K:\Phi(K)\to R\Phi(K)\) in \(D(\mathcal B)\).
If \(T:D(\mathcal A)\to D(\mathcal B)\) is another functor with a natural map \(\theta_K:\Phi(K)\to T(K)\) on the homotopy category, the only possible induced map \(R\Phi(K)\to T(K)\) is
\[
\Phi(I_K)\xrightarrow{\theta_{I_K}}T(I_K)
\xrightarrow{T(q_K)^{-1}}T(K).
\]
It is natural by the comparison equation for \(\bar f\), it composes with \(\eta\) to \(\theta\), and it is forced by that equation at \(q_K\). This is the right-derived-functor property.

If \(\Phi\) is left exact and \(M\) is in degree zero, the initial exact sequence \(0\to M\to I^0\to I^1\) gives \(H^0(\Phi(I))=\Phi(M)\). The resolution has no negative terms. Short exact sequences give cone triangles, hence the long exact sequences defining a \(\delta\)-functor \(R^i\Phi\).

Here are the details of universality of that \(\delta\)-functor. Each monomorphism \(M\to E\) into an injective kills \(R^i\Phi(M)\) after mapping to \(R^i\Phi(E)\) for \(i>0\), because \(E[0]\) is already a resolution. Let \(T^i\) be any other cohomological \(\delta\)-functor and choose a natural map \(R^0\Phi\to T^0\). In \(0\to M\to E\to C\to0\), exactness says that
\[
R^0\Phi(C)\longrightarrow R^1\Phi(M)
\quad\text{is onto},\qquad
R^{i-1}\Phi(C)\xrightarrow{\ \sim\ }R^i\Phi(M)\quad(i>1).
\]
For \(i=1\), compose the chosen degree-zero map at \(C\) with the boundary into \(T^1(M)\). This vanishes on the image of \(R^0\Phi(E)\), by naturality and exactness of \(T\), so it descends uniquely. Inductively, compose the degree-\((i-1)\) map at \(C\) with the boundary into \(T^i(M)\) and the inverse of the displayed isomorphism. Given a map \(M\to M'\), extend its composite into an injective containing \(M'\) across \(M\to E\); this gives a morphism of the two short exact sequences. Induction and naturality of boundary maps prove naturality of the constructed degree-\(i\) map. Two embeddings of the same \(M\) are compared with their diagonal embedding into the finite sum of the two injectives. The same argument proves independence of the embedding. Compatibility with arbitrary connecting maps follows by embedding the middle term of a short exact sequence into an injective and using the induced diagram of cokernels; the defining construction is precisely the connecting-map square in that diagram. Finally the displayed surjection and isomorphisms force every degree of any extension. Thus the extension exists uniquely as a morphism of \(\delta\)-functors. This proves universality. \(\square\)

### Why acyclic terms suffice in the bounded-below case

In the universality argument above, compatibility with an arbitrary boundary can be checked without any further resolution theorem. For \(0\to M\to N\to P\to0\), embed \(N\) in an injective \(E\) and put \(C=E/M\). The identity on \(M\), the embedding \(N\to E\), and the induced map \(P\to C\) give a morphism to \(0\to M\to E\to C\to0\). Naturality of each \(\delta\)-functor gives
\[
\delta_{M,N,P}^i=\delta_{M,E,C}^i\circ R^i\Phi(P\to C),
\]
and the same formula for \(T\). The constructed maps commute with the second boundary by their definition and with \(P\to C\) by their established naturality. They therefore commute with the first boundary as well.

**Proof of Theorem 6.1(4)–(5).** Call an object \(A\) right \(\Phi\)-acyclic when the comparison \(\Phi(A)[0]\to R\Phi(A[0])\) is an isomorphism. For left exact \(\Phi\), part (3) shows that this is equivalent to \(R^i\Phi(A)=0\) for \(i>0\). For a general additive functor the degree-zero comparison must additionally be an isomorphism, as the statement requires.

First let \(J\) have only finitely many nonzero terms, all right \(\Phi\)-acyclic. Remove its bottom term using the degreewise split sequence
\[
0\longrightarrow \sigma_{\ge a+1}J\longrightarrow J
\longrightarrow J^a[-a]\longrightarrow0,
\]
where \(\sigma\) denotes brutal truncation, with the indicated boundary differential set to zero. Applying \(\Phi\) still gives a degreewise split exact sequence. The associated cone triangles and the natural comparison with \(R\Phi\) show, by induction on the number of terms and the cohomology exact sequences, that \(\Phi(J)\to R\Phi(J)\) is an isomorphism.

For a bounded-below \(J\), fix an integer \(r\) and use
\[
0\longrightarrow \sigma_{\ge r+2}J\longrightarrow J
\longrightarrow \sigma_{\le r+1}J\longrightarrow0.
\]
The last complex is bounded. The first, and also its image under \(\Phi\), vanish in degrees below \(r+2\). By (1) it has an injective resolution vanishing below \(r+2\), so its derived image also has no cohomology below \(r+2\). The two long exact sequences therefore identify degree-\(r\) cohomology of both middle terms with that of the bounded last terms. The already proved bounded case gives the desired isomorphism in degree \(r\). This holds for every \(r\), proving (4). Part (5) now follows by applying the construction with the injective embeddings of Theorem 5.4. No countability, commutativity, spectral sequence, or exactness of infinite products of sheaves was used. \(\square\)

<span id="SH-FND-DC-07"></span><span id="sh-fnd-dc-07"></span>

## 7. K-injective resolutions of unbounded complexes

**Proposition 7.1 (a generator).** Let \(\mathcal O\) be any sheaf of rings on \(X\), and \(G=\bigoplus_{U}j_{U!}\mathcal O_U\), the sum over all open sets \(U\). Then:

- (a) for every subsheaf \(N\subsetneq M\) there is a morphism \(G\to M\) that does not factor through \(N\);
- (b) \(\operatorname{Hom}_{\mathcal O}(G,-)\) is faithful: a nonzero morphism \(M\to M'\) stays nonzero after composing with some \(G\to M\);
- (c) every \(M\) receives an epimorphism from a direct sum of copies of \(G\).

Together with [Theorem 3.1](#sh-fnd-dc-03)(2)–(3), which give all colimits and exact filtered colimits, this makes \(\operatorname{Mod}(\mathcal O)\) a Grothendieck abelian category in the sense of (K).

*Reference:* [Stacks, Tag 079V] states the generator for commutative \(\mathcal O\).

**Proof.** A section \(s\in M(U)\) gives \(e_s:j_{U!}\mathcal O_U\to M\) with \(e_s(1)=s\) (Lemma 5.2(3)). Composing with the projection \(G\to j_{U!}\mathcal O_U\) gives \(\tilde e_s:G\to M\). (a) A subobject of \(M\) in \(\operatorname{Mod}(\mathcal O)\) is a subsheaf, since kernels are computed on sections. If \(N\neq M\), there are \(U\) and \(s\in M(U)\setminus N(U)\). If \(\tilde e_s\) factored through \(N\), then \(s=e_s(1)\) would lie in \(N(U)\). (b) If \(\varphi:M\to M'\) is nonzero, then \(\varphi(s)\neq0\) for some section \(s\in M(U)\). So \(\varphi\circ\tilde e_s\neq0\): on the summand \(j_{U!}\mathcal O_U\) it sends \(1\) to \(\varphi(s)\). (c) The sum of all \(\tilde e_s\), over all pairs \((U,s)\), is a morphism \(\bigoplus_{(U,s)}G\to M\) whose image contains every section. So it is onto on stalks, hence an epimorphism. \(\square\)

The three forms of "generator" are equivalent in any abelian category with direct sums (Exercise 2). The definition in (K) uses form (b).

**Theorem 7.2.** For every complex \(K\) of left \(\mathcal O\)-modules there is a qis \(K\to I(K)\), functorial in \(K\) and injective in each degree, into a K-injective complex whose terms are injective. Consequently, every additive functor \(\Phi:\operatorname{Mod}(\mathcal O)\to\mathcal B\) into an abelian category has a right derived functor \(R\Phi:D(\mathcal O)\to D(\mathcal B)\), with \(R\Phi(K)=\Phi(I(K))\). In particular \(Rf_*\), \(R\Gamma(U,-)\) and the sheaf \(R\Gamma_Z\) are defined on the unbounded derived category.

*Source and credit.* The construction below follows the Stacks project in the pinned AI Integrated Stacks Project edition, *Injectives*, sections “Injectives in Grothendieck categories” and “K-injectives in Grothendieck categories”, through Tag 079P. That chapter credits Christian Serpé's work and its relationship to Spaltenstein's resolutions. The proof here includes all the size, extension and homotopy arguments that it uses. It was checked and expanded by OpenAI GPT-6 Astra in Codex, Ultra reasoning effort. In particular, the compatible-homotopy argument below replaces the source's appeal to an ordinal inverse-limit lemma. This is an expository variant, not a claim of a new existence theorem.

### Why unbounded resolutions require a different construction

In the bounded-below case there was a first degree from which to construct a homotopy. An unbounded complex has no such starting point. Instead we will arrange that every map from an acyclic complex is null-homotopic. There are too many acyclic complexes to attach them all at once. The first part of the proof reduces the tests to a set of small complexes; the second kills those tests and makes the final terms injective.

For the construction let \(\mathcal A\) be any locally small Grothendieck abelian category: it has small coproducts, exact filtered colimits, and a generator \(U\). Here “generator” means that \(\operatorname{Hom}(U,-)\) detects distinct morphisms. Proposition 7.1 and Theorem 3.1 give these properties for our module sheaves. Sets, well-orderings and the axiom of choice are understood in the fixed universe. The argument uses elementary abelian-category kernels, images, quotients and pushouts, but not the construction of the derived category.

We use two consequences of the filtered-colimit axiom. Coproducts are exact: a coproduct is the filtered colimit of its finite subsums, and finite direct sums are exact. Also filtered colimits commute with cohomology of complexes: exactness preserves kernels and cokernels in the formula for cohomology. Thus a filtered union of acyclic complexes is acyclic, and a filtered composite of monic quasi-isomorphisms is a monic quasi-isomorphism.

### Size bounds and maps into increasing unions

**Lemma 7.2.1 (a set of subobjects and bounded representatives).** For every object \(B\), its subobjects form a set. Write \(s(B)\) for the cardinality of this set. A subobject or quotient of \(B\) has size at most \(s(B)\). For each infinite cardinal \(\mu\), there is a set of representatives of the isomorphism classes of objects with \(s(B)\leq\mu\).

*Proof.* Associate to a subobject \(V\subset B\) the subset of \(\operatorname{Hom}(U,B)\) consisting of maps that factor through \(V\). This subset determines \(V\): the images of all maps \(U\to V\) fill \(V\). Indeed, if their sum had a proper image \(W\subsetneq V\), the nonzero quotient map \(V\to V/W\) would, by the generator property, have nonzero composite with some map \(U\to V\), a contradiction. Hence subobjects inject into a power set of a Hom set.

Subobjects of a subobject remain subobjects of \(B\). Subobjects of a quotient correspond, by inverse image, to subobjects of \(B\) containing its kernel. This proves the size inequalities.

For each proper subobject \(V\subsetneq B\), choose a map \(a_V:U\to B\) not factoring through \(V\). Such a map exists by applying the generator property to \(B\to B/V\). The sum of these maps is onto: a proper image would be one of the subobjects the chosen maps were required to escape. There are at most \(s(B)\) summands. Therefore, if \(s(B)\leq\mu\), \(B\) is a quotient of \(U^{(\mu)}\), after adding zero summands if necessary. Its isomorphism class is represented by the quotient by one of the set of subobjects of \(U^{(\mu)}\). This proves the last assertion. \(\square\)

**Lemma 7.2.2 (smallness for monic systems).** Suppose that \((B_\beta)_{\beta<\lambda}\) is an increasing ordinal-indexed system of subobjects with union \(B\), and \(\operatorname{cf}(\lambda)>s(A)\). Every map \(A\to B\) factors through some \(B_\beta\).

*Proof.* The inverse images \(A_\beta=A\times_B B_\beta\) form an increasing family of subobjects of \(A\), with union \(A\). To see the last equality without using elements, take filtered colimits of the kernel diagrams for
\[
A\oplus B_\beta\longrightarrow B,\qquad (a,b)\longmapsto f(a)-b.
\]
Exactness identifies the resulting kernel with \(A\times_B B=A\). At most \(s(A)\) distinct subobjects occur among the \(A_\beta\). Choose an index for each distinct one. The cofinality assumption bounds all those indices by a single \(\gamma<\lambda\), so \(A_\gamma\) contains every \(A_\beta\), and is \(A\). The pullback property gives the required factorization. \(\square\)

Recall that the cofinality of a limit ordinal is the least cardinality of an unbounded subset of it. We will always choose a limit ordinal with cofinality larger than a specified infinite cardinal \(\mu\); one may take the initial ordinal of \(\mu^+\). Indeed, a family of at most \(\mu\) ordinals below \(\mu^+\) has union of cardinality at most \(\mu\), hence is bounded below \(\mu^+\). This also explains why countably many factorization stages below such an ordinal have a common upper bound.

### Enough injectives, with a functorial choice

**Lemma 7.2.3 (the generator extension test).** An object \(E\) is injective if and only if every map \(V\to E\), where \(V\subset U\), extends to \(U\).

*Proof.* Necessity is the definition of injectivity. Conversely, take a monomorphism \(A\subset B\) and a map \(A\to E\). Order its extensions to subobjects of \(B\) by restriction. This is a set by Lemma 7.2.1 and local smallness. The union of a chain, with the compatible map to \(E\), is an upper bound, so Zorn's lemma gives a maximal extension \(a:A'\to E\).

If \(A'\neq B\), the nonzero quotient \(B\to B/A'\) has nonzero composite with some \(\psi:U\to B\). Put \(V=\psi^{-1}(A')\). The map \(a\psi:V\to E\) extends to \(b:U\to E\) by assumption. It vanishes on \(\ker\psi\), since its restriction there is \(a\psi=0\), so it descends to \(\operatorname{im}\psi\). This descended map and \(a\) agree on \(A'\cap\operatorname{im}\psi\). They therefore give a map \(A'+\operatorname{im}\psi\to E\), strictly extending \(a\), a contradiction. Thus \(A'=B\). \(\square\)

For an object \(M\), form the pushout
\[
\begin{array}{ccc}
\displaystyle\bigoplus_{(V,a)}V&\longrightarrow&M\\
\big\downarrow&&\big\downarrow\\
\displaystyle\bigoplus_{(V,a)}U&\longrightarrow&\mathcal E(M),
\end{array}
\qquad
(V,a):\ V\subset U,\quad a:V\to M .
\tag{7.3}
\]
This is a set-indexed coproduct by Lemma 7.2.1. The left arrow is monic because coproducts are exact; its pushout \(M\to\mathcal E(M)\) is monic. Every selected map \(V\to M\) extends to \(U\to\mathcal E(M)\). A map \(M\to M'\) takes the summand labelled \((V,a)\) to the summand labelled by its composite, so \(\mathcal E\) and the embedding are functorial.

Iterate \(\mathcal E\), taking unions at limit stages. Choose a fixed \(\lambda_0\) with \(\operatorname{cf}(\lambda_0)>s(U)\), and call the union \(E(M)\). Given \(V\subset U\) and a map \(V\to E(M)\), Lemma 7.2.2 makes it factor through a stage before \(\lambda_0\), since \(s(V)\leq s(U)\). At the next stage (7.3) extends it to \(U\). Lemma 7.2.3 now proves that \(E(M)\) is injective. We have constructed functorial monomorphisms \(M\to E(M)\). The functor \(E\) need not be additive; no subsequent argument assumes that it is.

### A set of acyclic test complexes

**Lemma 7.2.4 (bounded small lifts).** There is an infinite cardinal \(\kappa\), depending only on \(\mathcal A\) and \(U\), such that every nonzero acyclic complex contains a nonzero bounded-above acyclic subcomplex all of whose terms have size at most \(\kappa\).

*Proof.* For an infinite cardinal \(\mu\), set
\[
c(\mu)=\max\{\mu,\aleph_0,s(U^{(\mu)})\}.
\]
This function is nondecreasing: an inclusion of index sets gives a split monomorphism between the corresponding coproducts.

First consider an epimorphism \(p:B\to C\), with \(s(C)\leq\mu\). For each proper subobject \(C'\subset C\), the map \(B\to C/C'\) is nonzero. Choose \(b_{C'}:U\to B\) whose composite is nonzero. The image \(B'\) of their sum maps onto \(C\), because its image escapes every proper \(C'\). It is a quotient of at most \(\mu\) copies of \(U\), and hence \(s(B')\leq c(\mu)\). Notice that this argument does not assert that maps from \(U\) lift through epimorphisms: \(U\) was not assumed projective.

Put \(\kappa_0=\max\{s(U),\aleph_0\}\), \(\kappa_{r+1}=c(\kappa_r)\), and \(\kappa=\sup_{r<\omega}\kappa_r\). Let \(A^\bullet\) be acyclic and let \(\psi:U\to A^n\). Set
\[
N^n=\operatorname{im}\psi,\qquad
N^{n+1}=d(N^n),\qquad N^j=0\quad(j>n+1).
\]
The resulting complex is already exact at and above degree \(n+1\). Both nonzero terms have size at most \(\kappa_0\). If \(N^j\) has been constructed for \(j\geq k\), use the epimorphism
\[
(d^{k-1})^{-1}\!\left(\ker(N^k\to N^{k+1})\right)
\longrightarrow \ker(N^k\to N^{k+1}).
\]
It is onto because \(A^\bullet\) is acyclic. The small-lift construction gives a subobject \(N^{k-1}\) mapping onto that kernel. If \(s(N^k)\leq\kappa_r\), it can be chosen with \(s(N^{k-1})\leq\kappa_{r+1}\). Descending through all integers constructs a bounded-above acyclic subcomplex containing \(\operatorname{im}\psi\), with every term of size at most \(\kappa\). Only finite iterates of \(c\) are used at each degree; we do not assume \(c(\kappa)=\kappa\).

If \(A^\bullet\neq0\), choose a degree with \(A^n\neq0\) and a nonzero \(\psi:U\to A^n\). The constructed subcomplex is nonzero. \(\square\)

Choose a set \(\mathscr S\) of representatives of all bounded-above acyclic complexes with term sizes at most \(\kappa\). Such a set exists: Lemma 7.2.1 supplies a set of choices for each term, and local smallness supplies a set of differentials between each pair of choices; there are only countably many degrees. Restrict that set of complexes to the ones satisfying \(d^2=0\), acyclicity and boundedness above.

**Lemma 7.2.5 (testing K-injectivity on a set).** Suppose that every term of \(I^\bullet\) is injective and every chain map \(S^\bullet\to I^\bullet\), for \(S^\bullet\in\mathscr S\), is null-homotopic. Then \(I^\bullet\) is K-injective.

*Proof.* Take an acyclic \(A^\bullet\). Starting with \(F_0=0\), build an increasing continuous filtration by acyclic subcomplexes. If \(F_\beta\neq A\), the quotient \(A/F_\beta\) is nonzero and acyclic. Choose in it a nonzero small acyclic subcomplex from Lemma 7.2.4, and let \(F_{\beta+1}\) be its inverse image. At a limit stage take the union. Successor exactness follows from the short exact sequence of complexes; limit exactness follows from exact filtered colimits. The construction exhausts \(A\): the subcomplexes of \(A\) form a set, since they are among the sequences of subobjects of its terms. A strictly increasing chain longer than that set is impossible. Every nonzero successor quotient \(F_{\beta+1}/F_\beta\) is isomorphic to an element of \(\mathscr S\).

Let \(f:A\to I\) be a chain map. We construct null-homotopies \(h_\beta\) of \(f|_{F_\beta}\) that agree on earlier stages. At a successor, extend each component \(h_\beta^n:F_\beta^n\to I^{n-1}\) to a map \(\widetilde h^n:F_{\beta+1}^n\to I^{n-1}\), using injectivity. The map
\[
g=f|_{F_{\beta+1}}-d_I\widetilde h-\widetilde h\,d_F
\]
is a chain map, as \(d_I^2=d_F^2=0\). It vanishes on \(F_\beta\), and so descends to a chain map \(\bar g:F_{\beta+1}/F_\beta\to I\). By the test assumption \(\bar g=d_I k+k d\) for a degree-minus-one map \(k\). With \(\pi:F_{\beta+1}\to F_{\beta+1}/F_\beta\), put \(h_{\beta+1}=\widetilde h+k\pi\). This extends \(h_\beta\) and satisfies \(f=d_Ih_{\beta+1}+h_{\beta+1}d_F\).

At a limit stage the compatible components define maps out of the union, and the same identity holds because it holds on every earlier stage. At exhaustion they give a null-homotopy of \(f\). Thus every map from every acyclic complex to \(I\) is null-homotopic, exactly the definition of K-injectivity. This proof does not pass cohomology through an inverse limit. \(\square\)

### Killing tests and inserting injective objects

There are two operations, with different purposes.

For \(S\in\mathscr S\), let \(C(S)=\operatorname{Cone}(1_S)\), with
\[
C(S)^n=S^n\oplus S^{n+1},\qquad
d(a,b)=(da+b,-db).
\]
The map \(S\to C(S)\), \(a\mapsto(a,0)\), is monic and null-homotopic: \(a\mapsto(0,a)\) is a homotopy for it. The same formula contracts \(C(S)\). Its quotient by \(S\) is \(S[1]\), which is acyclic. Define \(P(M)\) by pushing out all these inclusions along all chain maps \(S\to M\):
\[
\begin{array}{ccc}
\displaystyle\bigoplus_{(S,w)}S&\xrightarrow{\ \sum w\ }&M\\
\big\downarrow&&\big\downarrow\\
\displaystyle\bigoplus_{(S,w)}C(S)&\longrightarrow&P(M).
\end{array}
\tag{7.4}
\]
Then \(M\to P(M)\) is termwise monic. Its quotient is the coproduct of the acyclic complexes \(S[1]\), hence is acyclic. It is therefore a quasi-isomorphism. Every chosen \(w\) becomes null-homotopic in \(P(M)\), using the corresponding cone. Indexing by all maps makes \(P\) and its embedding functorial.

The second operation uses the embeddings \(i_A:A\to E(A)\) constructed above. Set
\[
J(M)^n=E(M^n)\oplus E(M^{n+1}),\qquad
d_J(a,b)=(b,0),\qquad
u^n=(i_{M^n},\,i_{M^{n+1}}d_M).
\tag{7.5}
\]
The equation \(d_Ju=ud_M\) follows from \(d_M^2=0\), and \(u\) is monic because its first component is monic. Let \(Q=J(M)/u(M)\), with quotient map \(v:J(M)\to Q\), and define
\[
N(M)=\operatorname{Cone}(v)[-1],\qquad
N(M)^n=Q^{n-1}\oplus J(M)^n,
\]
\[
d_N(q,j)=(-d_Qq-v(j),d_Jj),\qquad
M\longrightarrow N(M),\quad m\longmapsto(0,u(m)).
\tag{7.6}
\]
These formulas are identities of component morphisms in the abelian category; they do not require objects to have underlying sets of elements. They show directly that the last map is a monic chain map. Its degree-\(n\) map factors through the injective subobject \(0\oplus J(M)^n\) of \(N(M)^n\). A finite direct sum of injectives is injective, since a map into it extends component by component.

The quotient \(N(M)/M\) has terms \(Q^{n-1}\oplus Q^n\), differential
\[
D(q,a)=(-dq-a,da),
\]
and contraction \(h(q,a)=(0,-q)\): substitution gives \(Dh+hD=1\). Thus \(M\to N(M)\) is a quasi-isomorphism. Naturality of \(i_A\) gives functoriality of every map in (7.5)–(7.6), even though \(E\) need not be additive.

The roles of the two operations are worth separating:
\[
\begin{gathered}
T_\beta\xrightarrow{\text{kill test maps}}P(T_\beta),\\
P(T_\beta)\xrightarrow{\text{insert injectives}}T_{\beta+1}.
\end{gathered}
\tag{7.7}
\]
Both arrows are monic quasi-isomorphisms. Neither intermediate complex is asserted to be K-injective.

### The final union and its two checks

Choose once and for all a limit ordinal \(\lambda\) of cofinality greater than \(\kappa\). Define
\[
T_0(M)=M,\qquad
T_{\beta+1}(M)=N(P(T_\beta(M))),\qquad
T_\gamma(M)=\varinjlim_{\beta<\gamma}T_\beta(M)
\]
at limit stages, and put \(I(M)=T_\lambda(M)\). All transitions are monic quasi-isomorphisms, including at limits by exactness of filtered colimits. Hence \(M\to I(M)\) is monic and a quasi-isomorphism. The choices of \(U,\mathscr S,\lambda_0,\lambda\) are fixed independently of \(M\), so the construction is functorial in \(M\).

First, every term \(I(M)^n\) is injective. Given \(V\subset U\) and a map \(V\to I(M)^n\), smallness factors it through \(T_\beta(M)^n\) for some \(\beta<\lambda\). Its composite into \(T_{\beta+1}(M)^n\) factors through the injective object \(J(P(T_\beta(M)))^n\) by (7.6). Extend \(V\to J(P(T_\beta(M)))^n\) to \(U\), and compose into \(I(M)^n\). Lemma 7.2.3 proves injectivity. This is a proof about the final terms, not an assertion that filtered colimits of injectives are automatically injective.

Second, let \(S\in\mathscr S\) and \(w:S\to I(M)\) be a chain map. Every component factors through a stage by Lemma 7.2.2, since \(s(S^n)\leq\kappa\). There are countably many components. As \(\operatorname{cf}(\lambda)>\kappa\geq\aleph_0\), all components factor through a single \(T_\beta(M)\). They already commute with the differentials there: their commutators vanish after the monomorphism \(T_\beta(M)^{n+1}\to I(M)^{n+1}\), and hence vanish before it. Thus \(w\) factors as a chain map. Operation \(P\) makes that map null-homotopic at the next stage, so it is null-homotopic in \(I(M)\). Lemma 7.2.5 proves K-injectivity.

Apply this construction to \(\mathcal A=\operatorname{Mod}(\mathcal O)\). It proves the resolution assertion of Theorem 7.2, including termwise injectivity, naturality and noncommutative coefficients. The derived-functor assertion follows from the comparison and construction already proved in Section 6, now without a boundedness restriction. The separate programme obligation to construct the derived category itself remains as stated in Section 1; it is not used to obtain the resolutions. \(\square\)

### Exercises on the unbounded construction

**Smallness degree by degree.** Explain why factoring every component of a chain map into a union is not enough unless one finds a single stage, and why the cofinality chosen above supplies one.

*Solution.* The component in degree \(n\) may first factor at an index \(\beta_n\), and the indices may be unbounded if the union is indexed by \(\omega\). The different components then need not define a map into any fixed stage. Here \(\sup_{n\in\mathbb Z}\beta_n<\lambda\), because the index set is countable and \(\operatorname{cf}(\lambda)>\aleph_0\). At a common upper bound, the differential identities follow from monicity into the final union. Boundedness above alone does not reduce the number of degrees to a finite set.

**Check the cone signs.** Verify the contraction used for \(N(M)/M\).

*Solution.* In degree \(n\), \(h(q,a)=(0,-q)\) lies in \(Q^{n-2}\oplus Q^{n-1}\). Thus
\[
Dh(q,a)=(q,-dq),\qquad
hD(q,a)=(0,dq+a),
\]
whose sum is \((q,a)\). This checks the sign of both the off-diagonal map in (7.6) and the contraction; replacing just one of these signs would break the calculation.

**Why both operations are needed.** Identify precisely where termwise injectivity is used in Lemma 7.2.5, and where the operation \(P\) is used.

*Solution.* Termwise injectivity extends the previously fixed homotopy on \(F_\beta\) to a degree-minus-one map on \(F_{\beta+1}\). That extension usually does not yet satisfy the homotopy equation. Its error descends to the small acyclic quotient, and the test property supplies the correction \(k\). Operation \(P\), iterated sufficiently far, establishes that test property. Termwise injectivity by itself does not kill maps from unbounded acyclic complexes, as Example 1 below shows.

**No exact-product shortcut.** Locate every limit operation in the existence proof and decide whether it requires exact products or exact inverse limits.

*Solution.* The construction of \(E(M)\), the acyclic filtration and the complexes \(T_\gamma(M)\) use filtered colimits of monomorphisms; their exactness is a Grothendieck-category axiom. At limit stages compatible homotopies are maps out of a colimit, supplied by its universal property. Sets of subcomplexes and the countable choices of their terms use products of sets only; no exactness of a product functor in \(\mathcal A\) is asserted. Thus the proof does not assume exact products or exact inverse limits in \(\mathcal A\). That matters for sheaves, whose products need not be exact.

**Corollary 7.3.** (1) If \(I\) is a K-injective complex of \(\mathcal O\)-modules and \(U\) is open, \(I|_U\) is K-injective. (2) If \(f:X\to Y\) is continuous, \(\mathcal O_X=f^{-1}\mathcal O_Y\), and \(I\) is a K-injective complex of \(\mathcal O_X\)-modules, then \(f_*I\) is K-injective. (3) On bounded-below complexes, the derived functors of Theorem 7.2 agree with those of [Theorem 6.1](#sh-fnd-dc-06).

**Proof.** (1) and (2): a functor \(u\) with an exact left adjoint \(v\) preserves K-injectivity. Indeed, the adjunction on modules gives one on complexes, compatible with homotopies. So for acyclic \(A\), \(\operatorname{Hom}_K(A,uI)\cong\operatorname{Hom}_K(vA,I)=0\), since \(vA\) is acyclic. Apply this to \(j_!\dashv j^{-1}\), where \(j_!\) is exact and left adjoint to restriction by Lemma 5.2, and to \(f^{-1}\dashv f_*\), where \(f^{-1}\) is exact and left adjoint to \(f_*\) by [Theorem 4.1](#sh-fnd-dc-04)(2) and (4). (3) A bounded-below injective resolution is K-injective by Lemma 6.2, and two K-injective resolutions of the same complex are homotopy equivalent. \(\square\)

**Remark 7.4 (complexes of injectives).** An unbounded complex of injectives need not be K-injective (Example 1). If \(\operatorname{Mod}(\mathcal O)\) has finite homological dimension, every complex of injectives is K-injective. This is not used.

**Remark 7.5 (why a Grothendieck category).** Products in \(\operatorname{Mod}(\mathbb Z_{\mathbb R})\) are not exact (Example 3). So a criterion for K-injective resolutions that needs exact products does not apply to sheaves in general. Constructions by inverse limits of resolutions of truncations work for modules over a ring, where products are exact; for sheaves they need extra care. This is why Theorem 7.2 goes through the Grothendieck property.

**Remark 7.6 (no bounded output).** Theorem 7.2 asserts no bounded output. Exercise 4 gives a bounded input with unbounded \(R\operatorname{Hom}\).

<span id="SH-FND-DC-08"></span><span id="sh-fnd-dc-08"></span>

## 8. K-flat resolutions

Throughout Sections 8–9, \(\mathcal O\) is commutative. Tensor products of complexes mean **direct-sum totalizations**, with the differential fixed in Section 1. No boundedness, finite global dimension, separation, or compactness condition on \(X\) is imposed.

We will construct a resolution by repeatedly killing the cycles in the kernel of a surjective map. This avoids assuming that a complex of flat terms is already K-flat; Example 1 shows that assumption would be false.

### Flat building blocks

Put \(B_U=j_{U!}\mathcal O_U\) for an open \(U\subset X\). Lemma 5.2 gives
\[
\operatorname{Hom}_{\mathcal O}(B_U,M)=M(U).
\tag{8.1}
\]
For every module sheaf \(M\), form the set-indexed sum
\[
L(M)=\bigoplus_{U\subset X\ {\rm open}}\ \bigoplus_{s\in M(U)}B_U .
\tag{8.2}
\]
The map \(\lambda_M:L(M)\to M\) sends the generator indexed by \(s\) to \(s\), using (8.1). Every germ is represented by such a local section, so \(\lambda_M\) is an epimorphism. This is a sum of extensions by zero, not a claim that \(M(X)\) generates the sheaf.

**Lemma 8.A (flatness and stalks).** A module sheaf \(M\) is flat if and only if every \(M_x\) is flat over \(\mathcal O_x\). In particular \(B_U\), \(L(M)\), and direct sums of flat module sheaves are flat.

**Proof.** The tensor sheaf is the sheafification of the sectionwise tensor presheaf. Its stalk is
\[
(F\otimes_{\mathcal O}M)_x=F_x\otimes_{\mathcal O_x}M_x .
\tag{8.3}
\]
Here is the relevant finite-relation argument. A tensor is a finite sum of elementary tensors. Represent all its factors on one neighbourhood of \(x\). An equality between tensors is generated by finitely many additive and balancing relations. Represent their scalar and module entries on a common smaller neighbourhood; each equality of germs in this finite certificate holds after a further shrinking. This proves both surjectivity and injectivity of (8.3), even though the section rings vary with the neighbourhood.

If every \(M_x\) is flat, (8.3) and Theorem 2.1 show that tensoring with \(M\) preserves exact sequences. Conversely, an injection \(A\to B\) of \(\mathcal O_x\)-modules gives an injection \(x_*A\to x_*B\) of module sheaves: these maps are injective on sections. If \(M\) is flat, tensoring preserves this injection, and its stalk at \(x\) is \(A\otimes M_x\to B\otimes M_x\). Tensor products are right exact, by their presentation with generators and relations, so this proves that \(M_x\) is flat.

The stalks of \(B_U\) are \(\mathcal O_x\) or zero (Lemma 5.2); both are flat. Stalks commute with direct sums. A direct sum of flat modules is flat because its tensor functor is the direct sum of their exact tensor functors, and direct sums of exact module sequences remain exact coordinatewise. This proves the final assertions. \(\square\)

**Lemma 8.B (operations preserving K-flatness).** A flat sheaf in a single degree is K-flat. Direct sums and filtered colimits of K-flat complexes are K-flat. If
\[
0\longrightarrow P\longrightarrow Q\longrightarrow R\longrightarrow0
\tag{8.4}
\]
is a degreewise split exact sequence of complexes and \(P,R\) are K-flat, then \(Q\) is K-flat. Every bounded-above complex of flat sheaves is K-flat.

**Proof.** If \(A\) is acyclic and \(M\) is flat, tensor the exact sequences
\(0\to Z^nA\to A^n\to Z^{n+1}A\to0\)
with \(M\). They identify the kernels and images in \(A\otimes M\), proving its acyclicity. Shifting a complex does not change this conclusion.

Tensor totalization commutes with direct sums and filtered colimits. These operations are exact for module sheaves by Theorem 3.1 (an arbitrary sum is the filtered colimit of its finite partial sums). They therefore commute with cohomology: kernels and images in an exact filtered colimit are the colimits of the corresponding kernels and images. Apply this to \(A\otimes P_i\) to obtain the assertions about sums and colimits.

After tensoring (8.4) with any complex \(A\), the sequence remains degreewise split exact, including after totalization. Its long exact cohomology sequence proves the extension assertion. The splitting is only a splitting of the underlying graded sheaves; it need not respect the differentials.

A bounded complex of flat sheaves is K-flat by induction on its length, using its bottom-degree term as the quotient and the remaining tail as the subcomplex in (8.4). If \(P\) is merely bounded above, its brutal lower truncations \(P^{\geq m}\) are bounded complexes and are subcomplexes of \(P\). As \(m\) decreases their union is \(P\). The filtered-colimit assertion proves the last statement. \(\square\)

**Theorem 8.1 (K-flat resolutions).** Every complex \(G\) of \(\mathcal O\)-modules has a quasi-isomorphism \(P\to G\), surjective in each degree, where \(P\) is K-flat and every \(P^n\) is flat.

**Proof.** For a sheaf \(M\), let \(D_n(M)\) have \(M\) in degrees \(n,n+1\), identity differential between them, and zero elsewhere. A map \(M\to G^n\) extends uniquely to a chain map \(D_n(M)\to G\), with upper component its composite with \(d_G\). Start with
\[
P_0=\bigoplus_{n\in\mathbb Z}D_n(L(G^n)),\qquad
\epsilon_0:P_0\longrightarrow G.
\tag{8.5}
\]
Use \(\lambda_{G^n}\) on the lower term of the \(n\)-th summand. The map is onto in every degree. Each disk is contractible. Tensoring a contraction \(h\) on the second factor with a complex \(A\) gives the contraction \(a\otimes p\mapsto(-1)^{|a|}a\otimes h(p)\). Thus \(P_0\) is K-flat; its terms are flat by Lemma 8.A.

Suppose \(P_s\to G\) has been built, and put \(K_s=\ker(\epsilon_s)\), a subcomplex. For every integer \(q\), open \(U\), and section
\[
z\in Z^q(K_s)(U),
\]
add a copy of \(B_U\) in degree \(q-1\). Write its generator locally as \(e_z\), and prescribe
\[
d e_z=z,\qquad \epsilon_{s+1}(e_z)=0.
\tag{8.6}
\]
These are morphisms of sheaves by (8.1). The two conditions needed for them to define a complex over \(G\) hold: \(dz=0\) and \(\epsilon_s(z)=0\). Explicitly, if \(V_s^n\) is the sum of the newly added \(B_U\)'s in degree \(n\), the underlying graded sheaf is \(P_s\oplus V_s\), with differential
\[
d(p,v)=(d_{P_s}p+\alpha_s(v),0),
\]
where \(\alpha_s:V_s^n\to P_s^{n+1}\) sends each generator to its chosen cycle. Since \(d_{P_s}\alpha_s=0\), its square is zero.

The inclusion \(P_s\to P_{s+1}\) is degreewise split, and the quotient is \(V_s\) with zero differential. It is a direct sum of shifts of the flat sheaves \(B_U\), hence K-flat. Lemma 8.B proves by induction that every \(P_s\) is K-flat. Its terms remain direct sums of the flat building blocks.

Set \(P=\varinjlim_{s\geq0}P_s\). The maps to \(G\) agree, and the map \(\epsilon:P\to G\) is termwise onto already from \(P_0\). Its terms are flat, and \(P\) is K-flat by Lemma 8.B. Exactness of filtered colimits gives
\[
\ker(\epsilon)=\varinjlim_s K_s,\qquad
H^q(\ker\epsilon)=\varinjlim_s H^q(K_s).
\tag{8.7}
\]
Each transition \(H^q(K_s)\to H^q(K_{s+1})\) is zero. Indeed, a stalk class is locally represented by a cycle section \(z\); the next stage supplies \(e_z\) in the kernel with \(de_z=z\). Thus every term in the colimit on the right of (8.7) maps to zero at the next stage, and the colimit vanishes. The kernel of \(\epsilon\) is acyclic. The long exact sequence for \(0\to\ker\epsilon\to P\to G\to0\) proves that \(\epsilon\) is a quasi-isomorphism. \(\square\)

The stages can create new cycles; the next stage kills them. A germ involves a finite stage, so a countable sequence of these stages suffices. Nothing in the construction asks sections to lift through an arbitrary sheaf epimorphism: generators are added for sections that actually exist on each open.

**Lemma 8.2 (making another resolution termwise surjective).** If \(Q\to G\) is a quasi-isomorphism with \(Q\) K-flat, then \(Q\oplus P_0\to G\), the sum of that map and (8.5), is a termwise-surjective K-flat resolution. If \(Q\) also has flat terms, so does this enlargement.

**Proof.** The new map is onto because \(\epsilon_0\) is. The complex \(P_0\) is contractible, and the inclusion \(Q\to Q\oplus P_0\) is a quasi-isomorphism commuting with the maps to \(G\). The new map is therefore a quasi-isomorphism. The direct sum is K-flat by Lemma 8.B; this uses no termwise-flatness assumption on \(Q\). If its terms are flat, Lemma 8.A gives flatness of the enlarged terms as well. \(\square\)

**Remark 8.3 (what the construction does not prove).** Extensions by zero of structure sheaves need not be projective objects in the category of module sheaves. The construction gives a resolution suitable for **tensor products**, not a K-projective resolution for computing arbitrary Hom functors. Neither an inverse limit of injective truncations nor exactness of products of sheaves was used.

*Mathematical sources.* Compare [AI Integrated Stacks Project, cohomology.tex, section “Flat resolutions”], especially the lemmas labelled \(\texttt{lemma-K-flat-resolution}\), \(\texttt{lemma-colimit-K-flat}\), and \(\texttt{lemma-bounded-flat-K-flat}\); their upstream tags include 06YF and 06YD. That treatment constructs compatible bounded-above resolutions. The proof above instead starts with a surjective disk complex and attaches local cycles directly. It is an expository alternative, not a claim of a new resolution theorem. The classical reference is [Spaltenstein 1988].

<span id="SH-FND-DC-09"></span><span id="sh-fnd-dc-09"></span>

## 9. The derived tensor product

A K-flat replacement protects a tensor computation even when the other variable is unbounded and nonflat. There are two different invariance statements to check.

**Lemma 9.A (tensoring a quasi-isomorphism).** If \(P\) is K-flat and \(u:A\to B\) is a quasi-isomorphism, then \(u\otimes1_P\) is a quasi-isomorphism. If \(v:P\to P'\) is a quasi-isomorphism between K-flat complexes, then \(1_G\otimes v\) is a quasi-isomorphism for **every** complex \(G\).

**Proof.** Tensoring commutes with cones: with the conventions in Section 1, the map identifying \(\operatorname{Cone}(u)\otimes P\) with \(\operatorname{Cone}(u\otimes1_P)\) is obtained by distributing the two direct-sum summands. Substitution in the cone differential \((b,a)\mapsto(db+u(a),-da)\) checks the signs. Since the first cone is acyclic by K-flatness, so is the second. A map is a quasi-isomorphism exactly when its cone is acyclic, which proves the first assertion.

For the second, take the resolution \(Q\to G\) constructed in Theorem 8.1. In the commuting square
\[
\begin{array}{ccc}
Q\otimes P&\longrightarrow&Q\otimes P'\\
\downarrow&&\downarrow\\
G\otimes P&\longrightarrow&G\otimes P',
\end{array}
\tag{9.1}
\]
both vertical arrows are quasi-isomorphisms by the first assertion. The top arrow is also one: \(Q\) is K-flat, and the chain symmetry \(a\otimes b\mapsto(-1)^{|a||b|}b\otimes a\) interchanges the factors. The bottom arrow is consequently a quasi-isomorphism, by applying cohomology to the square. Notice the role of K-flatness of **both** \(P\) and \(P'\) in the vertical arrows. \(\square\)

**Theorem 9.1 (the derived tensor product).** Choose a K-flat resolution \(P\to F\). The rule
\[
G\longmapsto G\otimes_{\mathcal O}P
\]
defines an exact functor \(-\otimes^L_{\mathcal O}F:D(\mathcal O)\to D(\mathcal O)\), canonically independent of the resolution. If \(Q\to G\) is K-flat, then
\[
G\otimes P\ \longleftarrow\ Q\otimes P\
\longrightarrow\ Q\otimes F
\tag{9.2}
\]
consists of quasi-isomorphisms. Thus either variable, or both, may be resolved.

**Proof.** Tensoring with \(P\) respects chain homotopies: a homotopy in the first variable tensors with \(1_P\), with the total differential as in Section 1. It therefore gives a functor on the homotopy category. Lemma 9.A shows that it inverts quasi-isomorphisms, so the defining universal property of \(D(\mathcal O)\), the localization of that homotopy category, gives the asserted functor. Tensoring commutes with shifts and cones, with the same signs checked in Lemma 9.A. Thus it takes the distinguished triangles, in the convention of Section 13, to distinguished triangles.

Here is the comparison between resolutions; it does not assume a direct map between arbitrary choices. First suppose \(P_1\to F\) and \(P_2\to F\) are termwise surjective. Form the ordinary fibre product of complexes
\[
W=P_1\times_F P_2.
\tag{9.3}
\]
The projection \(W\to P_1\) is termwise surjective with kernel \(\ker(P_2\to F)\), and the analogous statement holds with the indices exchanged. Both kernels are acyclic, so both projections are quasi-isomorphisms. Resolve \(W\) by a termwise-surjective K-flat complex \(R\). The resulting maps \(R\to P_i\) are quasi-isomorphisms between K-flat complexes. By Lemma 9.A they give natural isomorphisms in the derived category
\[
G\otimes P_1\ \longleftarrow\ G\otimes R\
\longrightarrow\ G\otimes P_2
\tag{9.4}
\]
for every \(G\).

Two choices \(R,R'\to W\) have a common refinement: resolve \(R\times_W R'\), whose projections are again surjective quasi-isomorphisms. Every triangle to the \(P_i\) commutes. After tensoring, the refinement maps are invertible in the derived category, so the comparisons (9.4) agree. For three resolutions \(P_i\to F\), resolve \(P_1\times_F P_2\times_F P_3\). Its maps to each pairwise fibre product are surjective quasi-isomorphisms, by the same kernel calculation. This proves the cocycle identity for the comparisons. They are natural in \(G\), since all their arrows are tensor products of fixed comparison maps with \(1_G\).

If a chosen resolution is not termwise surjective, Lemma 8.2 enlarges it by a contractible disk complex. The inclusion into that enlargement is a quasi-isomorphism between K-flat complexes, compatible with the maps to \(F\), so Lemma 9.A supplies the same comparison. This proves independence for every K-flat resolution, not only the ones chosen in Theorem 8.1.

Finally the left map of (9.2) is a quasi-isomorphism because \(P\) is K-flat and \(Q\to G\) is a quasi-isomorphism. The right map is one because \(Q\) is K-flat and \(P\to F\) is a quasi-isomorphism. \(\square\)

The lesson Supporting verifications for open prerequisites already proves the associativity, symmetry, unit and pullback coherence formulas on these models. Those calculations are retained; the present construction supplies the resolution-existence and tensor-invariance inputs they use. The comparisons above also explain why replacing a model never authorizes replacing a bounded-output assertion by an unbounded one.

**Bounded output is a separate question.** Example 4 gives two bounded objects whose derived tensor product has nonzero cohomology in every degree \(\leq0\). A finite weak global dimension of \(\mathcal O\) rules this out. Later lessons requiring bounded outputs must prove or assume that additional bound explicitly.

**Exercise 9.2 (why one stage is not enough).** On the one-point space with ring \(\mathbb Z\), let \(G=\mathbb Z/2\) in degree zero. Use just the two-term disk \(P_0=(\mathbb Z\xrightarrow{1}\mathbb Z)\) in degrees \(0,1\), mapping onto \(G\) by reduction in degree zero. Find a kernel cycle that must be killed. Attach its cell and show why the resulting complex still is not a resolution.

*Solution.* The kernel is \(2\mathbb Z\xrightarrow{1}\mathbb Z\), whose \(H^1\) is \(\mathbb Z/2\). Its degree-one generator \(b\) is a cycle. If \(a\) denotes the original degree-zero generator with \(da=b\), attach \(e\) in degree zero with \(de=b\) and \(\epsilon(e)=0\). Now \(d(a-e)=0\) and \(\epsilon(a-e)=1\pmod2\), as required for lifting the target class. But \(2(a-e)\) is a nonzero kernel cycle in degree zero, with no degree-minus-one boundary yet. Attach \(f\) in degree minus one with \(df=2(a-e)\). In this simplified example the resulting augmented complex is a resolution: \(d:\mathbb Zf\to\mathbb Za\oplus\mathbb Ze\) is injective, its image is twice the kernel of the next differential, and the degree-zero cohomology is \(\mathbb Z/2\). The general construction attaches every existing local kernel cycle at each stage, rather than guessing in advance how many steps suffice. \(\square\)

*Mathematical sources.* The two invariance statements correspond to the pinned AI Integrated Stacks Project lemmas labelled \(\texttt{lemma-K-flat-quasi-isomorphism}\) and \(\texttt{lemma-derived-tor-quasi-isomorphism-other-side}\), and its derived tensor construction (upstream tags 06YA, 06YG and 06YH). We have supplied their arguments here rather than replacing the proofs by links.

<span id="SH-FND-DC-10"></span><span id="sh-fnd-dc-10"></span>

## 10. Pullback and pushforward are adjoint on unbounded complexes

**Theorem 10.1.** For every morphism \(f:(X,\mathcal O_X)\to(Y,\mathcal O_Y)\) of commutative ringed spaces, \(Lf^*:D(\mathcal O_Y)\to D(\mathcal O_X)\) is left adjoint to \(Rf_*\), bifunctorially.

*Reference:* [Stacks, Tag 079W].

We use Theorem 10.1 without proof. For constant commutative coefficients, the unbounded adjunction is also proved directly in the lesson Supporting verifications for open prerequisites. The next proposition removes commutativity whenever \(\mathcal O_X=f^{-1}\mathcal O_Y\), in particular for constant coefficients.

**Proposition 10.2.** Let \(f:X\to Y\) be continuous, \(\mathcal O_Y\) any sheaf of rings, and \(\mathcal O_X=f^{-1}\mathcal O_Y\). Then \(Rf_*:D(\mathcal O_X)\to D(\mathcal O_Y)\) exists, and there are isomorphisms
\[
\operatorname{Hom}_{D(\mathcal O_X)}(f^{-1}B,E)\cong\operatorname{Hom}_{D(\mathcal O_Y)}(B,Rf_*E),
\tag{10.1}
\]
natural in \(B\in D(\mathcal O_Y)\) and \(E\in D(\mathcal O_X)\). This includes every constant sheaf of a unital ring \(k\), commutative or not.

*Reference:* [Stacks, Tag 079W] needs commutative rings.

**Proof.** Choose a K-injective resolution \(E\to I\) (Theorem 7.2). Then \(Rf_*E=f_*I\), and \(f_*I\) is K-injective by Corollary 7.3(2). Since \(f^{-1}\) is exact ([Theorem 4.1](#sh-fnd-dc-04)(2)), \(f^{-1}B\) represents the derived pullback of \(B\). Maps in the derived category into the K-injective complexes \(I\) and \(f_*I\) are homotopy classes of chain maps, by (H). The adjunction \(f^{-1}\dashv f_*\) of [Theorem 4.1](#sh-fnd-dc-04)(4) holds for complexes and respects homotopies. Together these give
\[
\operatorname{Hom}_D(f^{-1}B,E)=\operatorname{Hom}_K(f^{-1}B,I)\cong\operatorname{Hom}_K(B,f_*I)=\operatorname{Hom}_D(B,Rf_*E).
\]
Naturality in \(B\) and in \(E\) holds because the chain-level adjunction is natural for maps of complexes, and a change of K-injective model is a homotopy equivalence. This proves (10.1). \(\square\)

<span id="SH-FND-DC-11"></span><span id="sh-fnd-dc-11"></span>

## 11. Internal derived Hom

In this section \(\mathcal O\) is commutative.

**Theorem 11.1.** (a) For \(L,M\in D(\mathcal O)\), \(R\mathcal Hom(L,M)=\mathcal Hom^\bullet(L,I)\), with \(M\to I\) K-injective, is well defined. (b) \(R\mathcal Hom(K,R\mathcal Hom(L,M))\cong R\mathcal Hom(K\otimes^L L,M)\), functorially. (c) \(R\mathcal Hom(L,M)|_U\cong R\mathcal Hom(L|_U,M|_U)\) for \(U\) open.

*Reference:* [Stacks, Tags 08DH, 08DJ, 08DL and 0A8S].

We use Theorem 11.1 without proof. The chain-level proofs that later lessons rely on are given in the lesson Supporting verifications for open prerequisites: currying, the K-injectivity of \(\mathcal Hom^\bullet(P,I)\) for K-flat \(P\), the adjunction \(\operatorname{Hom}_D(T,R\mathcal Hom(B,C))\cong\operatorname{Hom}_D(T\otimes^LB,C)\), and open restriction.

Two warnings. The output can be unbounded above for bounded inputs (Exercise 4). And for a continuous map that is not an open embedding, the comparison between internal derived Hom and inverse image need not be an isomorphism; see the closing example of Supporting verifications for open prerequisites.

<span id="SH-FND-DC-12"></span><span id="sh-fnd-dc-12"></span>

## 12. The composition map

In this section \(\mathcal O\) is commutative.

**Theorem 12.1.** For \(K,L,M\in D(\mathcal O)\) there is a canonical morphism
\[
c_{K,L,M}:R\mathcal Hom(L,M)\otimes^L R\mathcal Hom(K,L)\longrightarrow R\mathcal Hom(K,M).
\]

*Reference:* [Stacks, Tag 0A8V], which calls \(c\) functorial in \(K,L,M\) and leaves out the proof of functoriality; in \(L\) this can only mean dinaturality, as explained below.

The morphism \(c\) is induced by the composition of Hom complexes. Its properties are proved in the lesson Supporting verifications for open prerequisites: \(c\) is the transpose of evaluating into \(L\) and then into \(M\); it is associative and unital; and it is natural in \(K\) and \(M\).

In \(L\) the right notion is dinaturality, which is also proved there. The object \(L\) occurs covariantly in one factor and contravariantly in the other, so the domain of \(c\) is not a functor of \(L\), and "natural in \(L\)" has no meaning.

<span id="SH-FND-DC-13"></span><span id="sh-fnd-dc-13"></span>

## 13. The localization triangle, and signs

For a locally closed \(W\subset X\), \(\Gamma_W:\operatorname{Mod}(\mathcal O)\to\operatorname{Mod}(\mathcal O)\) is the sheaf of sections supported in \(W\) (Section 1). It is a left exact additive functor, and \(R\Gamma_W\) denotes its right derived functor on \(D(\mathcal O)\) (Theorem 7.2).

**Theorem 13.1.** Let \(\mathcal O\) be any sheaf of rings on \(X\), \(Z\subset X\) locally closed, and \(Z'\subset Z\) closed in \(Z\). For \(K\in D(\mathcal O)\) there is a distinguished triangle
\[
R\Gamma_{Z'}K\longrightarrow R\Gamma_ZK\longrightarrow R\Gamma_{Z\setminus Z'}K\longrightarrow R\Gamma_{Z'}K[1],
\tag{13.1}
\]
functorial in \(K\). The first two arrows come from the inclusion of supports and from restriction. The third is the connecting morphism of the triangle (T) attached to the termwise exact sequence (13.2) below.

*Reference:* [Stacks, Tag 0G72] proves Corollary 13.2 for commutative \(\mathcal O\).

**Proof.** Let \(K\to I\) be as in Theorem 7.2: \(I\) is K-injective with injective terms. Each \(I^n\) is flabby (Corollary 5.5(1)). For a flabby sheaf \(F\), the sequence
\[
0\to\Gamma_{Z'}F\to\Gamma_ZF\to\Gamma_{Z\setminus Z'}F\to0
\tag{13.2}
\]
is exact by (Γ), a statement about sheaves of abelian groups. Here all terms are \(\mathcal O\)-modules (a section of \(\Gamma_WF\) is a section of \(F\) over an open set, supported in \(W\), and \(\mathcal O\) acts through restriction), and the maps are \(\mathcal O\)-linear. Exactness in \(\operatorname{Mod}(\mathcal O)\) is checked on stalks, as for abelian sheaves ([Theorem 2.1](#sh-fnd-dc-02)(4)), so (13.2) is exact in \(\operatorname{Mod}(\mathcal O)\). Applying (13.2) to each \(I^n\) gives a termwise exact sequence of complexes. By (T) it yields a distinguished triangle in \(D(\mathcal O)\). By Theorem 7.2, \(R\Gamma_W K=\Gamma_W(I)\) for each \(W\). This gives (13.1).

For functoriality, let \(u:K\to K'\) in \(D(\mathcal O)\), with resolution \(K'\to I'\). Since \(I'\) is K-injective, \(\operatorname{Hom}_D(I,I')=\operatorname{Hom}_K(I,I')\) by (H). So \(u\) is represented by a chain map \(\tilde u:I\to I'\), unique up to homotopy. Applying the three functors to \(\tilde u\) gives a morphism of termwise exact sequences, hence a morphism of the triangles; the triangle of (T) is natural for such morphisms. Homotopic chain maps give equal maps in \(D\) on each term. The same argument shows that another choice of \(I\) gives an isomorphic triangle. \(\square\)

**Corollary 13.2 (a closed set and its open complement).** Let \(Z\) be closed and \(j:U=X\setminus Z\hookrightarrow X\). For \(K\in D(\mathcal O)\) there is a distinguished triangle
\[
R\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^{-1}K\longrightarrow R\Gamma_ZK[1],
\tag{13.3}
\]
functorial in \(K\).

**Proof.** Apply Theorem 13.1 to the pair \((X,Z)\). Here \(\Gamma_X=\mathrm{id}\), \(X\setminus Z=U\), and \(\Gamma_U=j_*j^{-1}\) (Section 1). With \(I\) as in the proof, \(\Gamma_U(I)=j_*(I|_U)\). By Corollary 7.3(1), \(I|_U\) is K-injective, and it is a resolution of \(j^{-1}K\) because \(j^{-1}\) is exact. So \(j_*(I|_U)=Rj_*(j^{-1}K)\). \(\square\)

For bounded-below \(K\), Corollary 7.3(3) shows that (13.1) can also be computed with a bounded-below injective resolution. The sign of its third arrow depends on a convention, discussed next.

**Lemma 13.3 (the sign of the connecting morphism).** Let \(0\to A\xrightarrow{a}B\xrightarrow{b}C\to0\) be a termwise exact sequence of complexes in an abelian category. Let \(\operatorname{Cone}(a)^n=B^n\oplus A^{n+1}\) with \(d(y,x)=(dy+a(x),-dx)\), and let \(p(y,x)=x\) and \(q(y,x)=b(y)\), so that \(p:\operatorname{Cone}(a)\to A[1]\) and \(q:\operatorname{Cone}(a)\to C\) is a qis. Let \(\delta:H^n(C)\to H^{n+1}(A)\) be the connecting map: for a cycle \(z\), choose \(y\) with \(b(y)=z\) and the \(x\) with \(a(x)=dy\), and set \(\delta[z]=[x]\). Then
\[
H^n(p)\circ H^n(q)^{-1}=-\delta .
\tag{13.4}
\]
Two conventions for distinguished triangles are in use. For a chain map \(f:A\to B\), form \(\operatorname{Cone}(f)\) in the same way, with the inclusion \(i:B\to\operatorname{Cone}(f)\) and the projection \(p:\operatorname{Cone}(f)\to A[1]\). The *first convention* declares distinguished the triangles isomorphic to some \((f,i,p)\); the *second convention* declares distinguished those isomorphic to some \((f,i,-p)\). Kashiwara and Schapira use the first; [Stacks] and this lesson use the second. Under the second convention, the triangle attached to the sequence has third arrow \(-p\circ q^{-1}\), which by (13.4) induces \(+\delta\) on cohomology. Under the first, it has third arrow \(p\circ q^{-1}\), which induces \(-\delta\). More generally, the distinguished triangles of the first convention are exactly those of the second with the third arrow negated. Equivalently, by Exercise 5(i), the triangles of the second convention are the *antidistinguished* triangles of the first: those that become distinguished for the first convention when all three arrows are negated.

**Proof.** Let \(z\), \(y\), \(x\) be as stated. Then \(a(dx)=d\,dy=0\), so \(dx=0\), because \(a\) is injective. The element \((y,-x)\) is a cycle of \(\operatorname{Cone}(a)\), since \(d(y,-x)=(dy-a(x),dx)=(0,0)\). Also \(q(y,-x)=z\) and \(p(y,-x)=-x\). So \(H^n(p)H^n(q)^{-1}[z]=[-x]=-\delta[z]\). For the comparison of the two conventions, let \((\varphi_1,\varphi_2,\varphi_3)\) be an isomorphism of triangles from \((f,i,p)\) to \((u,v,w)\). Then the same maps give an isomorphism from \((f,i,-p)\) to \((u,v,-w)\). So the two classes differ exactly by the sign of the third arrow, in \(K(\mathcal A)\) and hence in \(D(\mathcal A)\). \(\square\)

**Remark 13.4 (working with both conventions).** When a formula taken from a text that uses the first convention contains the third arrow of a triangle, for instance a connecting morphism of a triangle of derived functors, negate that arrow before combining it with (13.3). Negating two arrows of a triangle gives an isomorphic triangle, so it is enough to track one sign per triangle (Exercise 5).

<span id="SH-FND-DC-14"></span><span id="sh-fnd-dc-14"></span>

## 14. Worked examples

**Example 1 (a two-periodic complex: injective and free terms, acyclic, yet neither K-injective nor K-flat).** Let \(R=\mathbb Z/4\) and let \(C\) be the complex with \(C^n=R\) for all \(n\) and every differential equal to multiplication by \(2\).

- *\(C\) is acyclic.* The kernel of multiplication by \(2\) is \(\{0,2\}\), which is also its image.
- *Its terms are free and injective.* \(R\) is free over itself. It is injective by Baer's criterion (B): its ideals are \(0\), \((2)\) and \(R\), and a linear map \((2)\to R\) sends \(2\) to some \(c\) with \(2c=0\), that is \(c\in\{0,2\}\); it extends to \(R\) by \(1\mapsto0\) or \(1\mapsto1\).
- *\(C\) is not contractible.* A homotopy \(s\) is multiplication by elements \(s_n\in R\) in each degree, and \((ds+sd)^n=2s_n+2s_{n+1}\) lies in \(2R\). It is never \(1\). So \(\mathrm{id}_C\neq0\) in \(K(R)\).
- *\(C\) is not K-injective.* \(C\) is acyclic, but \(\operatorname{Hom}_{K(R)}(C,C)\ni\mathrm{id}_C\neq0\). So the lower bound in Lemma 6.2 cannot be dropped, and neither can the finite-dimension hypothesis in Remark 7.4: \(R\) has infinite global dimension (Exercise 4).
- *\(C\) is not K-flat.* Suppose it were. Let \(M\) be any complex and \(P\to M\) a K-flat resolution. The cone of \(P\to M\) is acyclic, so its tensor product with the K-flat \(C\) is acyclic, and \(\operatorname{Tot}(P\otimes C)\to\operatorname{Tot}(M\otimes C)\) is a qis. And \(\operatorname{Tot}(P\otimes C)\) is acyclic, since \(P\) is K-flat and \(C\) is acyclic. So \(M\otimes C\) would be acyclic for every \(M\). But for \(M=\mathbb Z/2\) in degree \(0\), \(M\otimes C\) has \(\mathbb Z/2\) in each degree and zero differentials, so its cohomology is \(\mathbb Z/2\) in every degree. So flat, even free, terms do not make a complex K-flat.

*Sheaf versions.* On any nonempty space \(X\) with \(\mathcal O=R_X\), the complex of constant sheaves \(C_X\) is acyclic with flat terms, and \((\mathbb Z/2)_X\otimes C_X\) has cohomology sheaves \((\mathbb Z/2)_X\) in every degree; so it is not K-flat. For \(x\in X\), the skyscraper complex \(x_*C\) has injective terms (Lemma 5.3) and is acyclic, since \(x_*\) is exact on sections. If \(\mathrm{id}_{x_*C}\) were null-homotopic, taking stalks at \(x\) would make \(\mathrm{id}_C\) null-homotopic. So \(x_*C\) is an acyclic complex of injective sheaves that is not K-injective: an unbounded complex of injectives need not be K-injective.

**Example 2 (sections do not commute with infinite sums).** Let \(X=\mathbb N\) with the discrete topology, \(k\neq0\) a ring, and \(F_n=n_*k\), the skyscraper at the point \(n\). On a discrete space, a sheaf is determined by its stalks, and its global sections are the families of stalk elements. The stalk of \(\bigoplus_nF_n\) at \(m\) is \(k\), coming from \(F_m\) alone. So
\[
\Gamma\Bigl(X,\bigoplus_nF_n\Bigr)=\prod_{m\in\mathbb N}k,\qquad \bigoplus_n\Gamma(X,F_n)=\bigoplus_{n\in\mathbb N}k ,
\]
and the canonical map is the inclusion of finitely supported sequences, which is not onto. \(X\) is not quasi-compact. On a finite discrete space the map is bijective, as [Theorem 3.1](#sh-fnd-dc-03)(5) predicts.

**Example 3 (products of sheaves are not exact).** Let \(X=\mathbb R\), \(k\neq0\), \(U_n=(-1/n,1/n)\) for \(n\geq1\), \(A_n=j_{U_n!}k_{U_n}\), and \(B=0_*k\), the skyscraper at \(0\). Let \(\varphi_n:A_n\to B\) correspond under Lemma 5.2(2) to evaluation at \(0\) of locally constant functions on open sets of \(U_n\). At \(0\) it is the identity of \(k\); at other points the target stalk is \(0\). So each \(\varphi_n\) is an epimorphism. Now look at \(\prod_n\varphi_n\) at \(0\). The target stalk is \(\prod_nk\), because \((\prod_nB)(V)=\prod_nk\) when \(0\in V\). A germ of the domain is represented on some \(V=(-\varepsilon,\varepsilon)\) by a family \((s_n)\) with \(s_n\in A_n(V)\). If \(n>1/\varepsilon\), then \(U_n\subsetneq V\), and \(s_n\) is a constant \(c\) on the connected set \(U_n\) whose support must be closed in \(V\). The support \(U_n\) is not closed in \(V\), so \(c=0\). Hence the image of the germ has only finitely many nonzero coordinates. The stalk map lands in \(\bigoplus_nk\subsetneq\prod_nk\), so \(\prod_n\varphi_n\) is not an epimorphism.

**Example 4 (a derived tensor product with unbounded output).** Let \(R=\mathbb Z/4\). The complex \(P:\ \cdots\to R\xrightarrow{2}R\xrightarrow{2}R\to0\), with the last \(R\) in degree \(0\), maps to \(\mathbb Z/2\) (in degree \(0\)) by reduction mod \(2\). This is a qis: the kernel of reduction is \(\{0,2\}=2R\), which is the image of the last map, and each other kernel equals the next image, as in Example 1. \(P\) is a bounded-above complex of free modules, so it is K-flat by fact (a) of Section 8. Hence \(\mathbb Z/2\otimes^L_R\mathbb Z/2=\mathbb Z/2\otimes_RP\), the complex \(\cdots\to\mathbb Z/2\xrightarrow{0}\mathbb Z/2\to0\). Its cohomology is \(\mathbb Z/2\) in every degree \(\leq0\). Both inputs are bounded, and the output is not. With constant sheaves on any nonempty \(X\), the same computation holds for \(\mathcal O=R_X\).

**Example 5 (inverse image versus module pullback).** Let \(X=Y\) be a point, \(\mathcal O_Y=\mathbb Z\) and \(\mathcal O_X=\mathbb Z/2\), with the ring map \(\mathbb Z\to\mathbb Z/2\). Then \(f^{-1}\) is the identity on abelian groups, but the module pullback is \(f^*M=\mathbb Z/2\otimes_{\mathbb Z}M\). It sends the exact sequence \(0\to\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z/2\to0\) to \(\mathbb Z/2\xrightarrow{0}\mathbb Z/2\to\mathbb Z/2\to0\), whose first map is not injective. For constant sheaves of rings, \(\mathcal O_X=f^{-1}\mathcal O_Y\), so \(f^*=f^{-1}\) is exact (Theorem 4.1).

**Example 6 (the localization triangle on the Sierpiński space).** Let \(S=\{o,c\}\) with open sets \(\emptyset\), \(\{o\}\) and \(S\). The point \(c\) is closed and \(o\) is open. Let \(k\) be a ring and \(\mathcal O=k_S\).

- *Sheaves.* An open cover of \(S\) contains \(S\) itself, and an open cover of \(\{o\}\) contains \(\{o\}\). So every presheaf with \(F(\emptyset)=0\) is a sheaf. A sheaf is a \(k\)-linear map \(r:M\to N\), with \(M=F(S)\) and \(N=F(\{o\})\), and a morphism is a commuting square. The stalks are \(F_c=M\) and \(F_o=N\), because the smallest open neighbourhoods are \(S\) and \(\{o\}\).
- *Operations.* Let \(Z=\{c\}\), \(U=\{o\}\) and \(j:U\hookrightarrow S\). Then \(j^{-1}F=N\), \(j_*N=(N\xrightarrow{\mathrm{id}}N)\), and \(\Gamma_ZF=(\ker r\to0)\), since a section over \(\{o\}\) supported in \(Z\) is zero. The map \(F\to j_*j^{-1}F\) is \((r,\mathrm{id}_N)\). The functor \(j_*\) is exact, so \(Rj_*j^{-1}F=j_*j^{-1}F\).
- *Flabbiness.* \(F\) is flabby if and only if \(r\) is onto. The sequence \(0\to\Gamma_ZF\to F\to j_*j^{-1}F\to0\) is \(0\to\ker r\to M\xrightarrow{r}N\) over \(S\) and \(0\to0\to N\to N\to0\) over \(\{o\}\). It is exact on the right exactly when \(r\) is onto, as (13.2) predicts for flabby sheaves.
- *The triangle.* By (13.3) and its long exact sequence of cohomology sheaves,
\[
0\to H^0R\Gamma_ZF\to F\xrightarrow{(r,\mathrm{id})}j_*j^{-1}F\to H^1R\Gamma_ZF\to0,
\]
and \(H^qR\Gamma_ZF=0\) for \(q\neq0,1\). So \(H^0R\Gamma_ZF=(\ker r\to0)\) and \(H^1R\Gamma_ZF=(\operatorname{coker}r\to0)\), both concentrated at the closed point. With the second sign convention of Section 13, the map \(j_*j^{-1}F\to H^1R\Gamma_ZF\) is the connecting map \(\delta\) of Lemma 13.3 for (13.2) applied to a resolution \(I\) of \(F\); with the first convention it is \(-\delta\).

## Exercises

**Exercise 1 (stalks as left adjoints).** Let \(x\in X\). Show that \(F\mapsto F_x\) is left adjoint to \(J\mapsto x_*J\), and deduce that stalks commute with all colimits in \(\operatorname{Mod}(\mathcal O)\).

*Solution.* The adjunction is (5.2), natural in both variables (Lemma 5.3). For a diagram \((F_i)\) and every \(\mathcal O_x\)-module \(J\),
\[
\operatorname{Hom}\bigl((\varinjlim F_i)_x,J\bigr)\cong\operatorname{Hom}\bigl(\varinjlim F_i,x_*J\bigr)\cong\varprojlim\operatorname{Hom}(F_i,x_*J)\cong\varprojlim\operatorname{Hom}((F_i)_x,J)\cong\operatorname{Hom}\bigl(\varinjlim(F_i)_x,J\bigr),
\]
naturally in \(J\). By the Yoneda lemma, \((\varinjlim F_i)_x\cong\varinjlim(F_i)_x\). Tracing the identity of \(\varinjlim(F_i)_x\) through the chain shows that this isomorphism is inverse to the canonical map \(\varinjlim(F_i)_x\to(\varinjlim F_i)_x\). This is a second proof of the stalk formula in [Theorem 3.1](#sh-fnd-dc-03)(2).

**Exercise 2 (three forms of a generator).** Let \(\mathcal C\) be an abelian category with direct sums and \(G\) an object. Show that these are equivalent: (a) for every \(N\subsetneq M\) some morphism \(G\to M\) does not factor through \(N\); (b) \(\operatorname{Hom}(G,-)\) is faithful; (c) every object receives an epimorphism from a direct sum of copies of \(G\).

*Solution.* (c)\(\Rightarrow\)(a): let \(\pi:G^{(I)}\to M\) be an epimorphism. If every \(G\to M\) factored through \(N\), so would every component of \(\pi\), hence \(\pi\) itself. Then \(M=\operatorname{Im}\pi\subset N\), so \(N=M\). (a)\(\Rightarrow\)(b): if \(\varphi:M\to M'\) is nonzero, then \(\operatorname{Ker}\varphi\subsetneq M\). So some \(g:G\to M\) does not factor through \(\operatorname{Ker}\varphi\), that is, \(\varphi g\neq0\). (b)\(\Rightarrow\)(c): let \(\pi:\bigoplus_{g\in\operatorname{Hom}(G,M)}G\to M\) be the sum of all \(g\), and \(q:M\to\operatorname{Coker}\pi\). Every \(g\) factors through \(\pi\), so \(qg=0\) for all \(g\). By (b), \(q=0\). So \(\pi\) is an epimorphism. For \(\mathcal C=\operatorname{Mod}(\mathcal O)\) and \(G=\bigoplus_Uj_{U!}\mathcal O_U\), Proposition 7.1 checks all three directly.

**Exercise 3 (injectives on the Sierpiński space).** In Example 6, let \(k\) be a field. Show that \((r:M\to N)\) is injective in \(\operatorname{Mod}(k_S)\) if and only if \(r\) is onto. Show that \(j_!k\) is not injective.

*Solution.* If the sheaf is injective, it is flabby (Corollary 5.5(1)), so \(r\) is onto. Conversely let \(r\) be onto and \(K=\ker r\). Over a field, \(M\cong K\oplus N\) compatibly with \(r\). So the sheaf is the sum of \((K\to0)=c_*K\) and \((N\xrightarrow{\mathrm{id}}N)=j_*N\). A sum of two injectives is injective. The first is injective by Lemma 5.3, as every vector space is injective. For the second, a morphism \((s:A\to B)\to(N\xrightarrow{\mathrm{id}}N)\) is a pair \((\alpha,\beta)\) with \(\beta s=\alpha\), so it is determined by \(\beta:B\to N\). Hence \(\operatorname{Hom}(-,j_*N)\cong\operatorname{Hom}_k((-)_o,N)\), which is exact because stalks are exact and \(N\) is injective over \(k\). Finally \(j_!k=(0\to k)\) by Lemma 5.2: a section over \(S\) would need support closed in \(S\) and contained in \(\{o\}\), and \(\{o\}\) is not closed. Its \(r\) is not onto, so \(j_!k\) is not injective. Extension by zero does not preserve injectives.

**Exercise 4 (unbounded \(R\operatorname{Hom}\)).** Let \(R=\mathbb Z/4\). Compute \(\operatorname{Ext}^i_R(\mathbb Z/2,\mathbb Z/2)\) for all \(i\).

*Solution.* Embed \(\mathbb Z/2\) in \(R\) by \(1\mapsto2\). The sequence \(0\to\mathbb Z/2\to R\xrightarrow{2}R\xrightarrow{2}R\to\cdots\) is exact, as in Example 1, and its terms are injective (Example 1). So it is an injective resolution, bounded below, hence K-injective (Lemma 6.2), and it computes \(R\operatorname{Hom}_R(\mathbb Z/2,\mathbb Z/2)\). A linear map \(\mathbb Z/2\to R\) sends \(1\) to an element killed by \(2\), that is to \(0\) or \(2\). So \(\operatorname{Hom}_R(\mathbb Z/2,R)\cong\mathbb Z/2\), and multiplication by \(2\) acts on it as \(0\), since \(2\cdot2=0\). The Hom complex is \(\mathbb Z/2\xrightarrow{0}\mathbb Z/2\xrightarrow{0}\cdots\) in degrees \(0,1,2,\ldots\). Hence \(\operatorname{Ext}^i_R(\mathbb Z/2,\mathbb Z/2)\cong\mathbb Z/2\) for every \(i\geq0\), and \(0\) for \(i<0\). Two bounded inputs give an output that is unbounded above, and \(R\) has infinite global dimension. On a one-point space the same computation is a statement about sheaves.

**Exercise 5 (signs of triangles).** Let \((u,v,w)\) be a distinguished triangle \(X\to Y\to Z\to X[1]\) in a triangulated category. (i) Show that \((u,-v,-w)\), \((-u,v,-w)\) and \((-u,-v,w)\) are isomorphic to \((u,v,w)\), hence distinguished. (ii) Show that the identity functor of \(K(\mathcal A)\), with the natural isomorphism \(-\mathrm{id}\) between the shift and itself, is a triangulated equivalence from the structure of the first sign convention of Section 13 to that of the second.

*Solution.* (i) An isomorphism of triangles \((a,b,c)\) from \((u,v,w)\) produces the triangle \((bua^{-1},cvb^{-1},a[1]wc^{-1})\). Taking \((a,b,c)=(1,1,-1)\), \((-1,1,1)\) and \((1,-1,1)\) gives the three triangles, in this order. (ii) A triangulated functor is a pair \((\Phi,\xi)\) with \(\xi:\Phi\circ[1]\cong[1]\circ\Phi\), and it sends \((u,v,w)\) to \((\Phi u,\Phi v,\xi\circ\Phi w)\). With \(\Phi=\mathrm{id}\) and \(\xi=-\mathrm{id}\), it sends \((u,v,w)\) to \((u,v,-w)\). By Lemma 13.3 this maps the distinguished triangles of the first convention exactly onto those of the second. The same pair also maps the triangles of the second convention onto those of the first, so it is a triangulated equivalence whose inverse has the same form. Negating one arrow is not the same as negating two. For example, in \(D(\mathbb Z/9)\) let \((u,v,w)\) be the triangle of the exact sequence \(0\to\mathbb Z/3\to\mathbb Z/9\to\mathbb Z/3\to0\). If \((u,v,-w)\) were distinguished for the same structure, a morphism of triangles \((1,1,c)\) from \((u,v,w)\) would exist. Then \(cv=v\) forces \(c=1\), since \(v\) is onto and \(\operatorname{End}(\mathbb Z/3)=\mathbb Z/3\); and then \(-w=w\), so \(2w=0\). But \(w\neq0\) in \(\operatorname{Ext}^1(\mathbb Z/3,\mathbb Z/3)\cong\mathbb Z/3\), because the sequence does not split, and \(2\) is invertible modulo \(3\).

## Where this leads

### Further exercises on the prerequisite constructions

**Exercise 6 (why the extension property matters).** Show directly that \(\mathbb Z\), as a module over itself, is not injective. Does the map from its ideal \(2\mathbb Z\) that sends \(2\) to \(1\) extend?

*Solution.* An extension \(b:\mathbb Z\to\mathbb Z\) would satisfy \(2b(1)=b(2)=1\), impossible for an integer \(b(1)\). The ideal map is a witness to the failure of Baer's criterion. The obstruction is divisibility, not merely the existence of additive generators.

**Exercise 7 (one pushout resolution by hand).** Apply the first construction in Section 6 to \(\mathbb Z[0]\), using \(\mathbb Z\hookrightarrow\mathbb Q\). Identify the next term and finish the resolution.

*Solution.* Degree one initially vanishes. The pushout is therefore \(\mathbb Q/\mathbb Z\), and the new complex is \(\mathbb Q\to\mathbb Q/\mathbb Z\), in degrees zero and one, with the quotient map as differential. Both terms are divisible and hence injective over \(\mathbb Z\): a map \(n\mathbb Z\to E\) extends by choosing an \(n\)-th root of its value at \(n\), and Baer's criterion applies. The kernel is \(\mathbb Z\), and the quotient map is onto, so the inclusion from \(\mathbb Z[0]\) is a quasi-isomorphism. Its quotient complex has \(\mathbb Q/\mathbb Z\) in both degrees with identity differential, precisely the contractible quotient used in the general construction.

**Exercise 8 (how far to truncate).** Explain why the acyclicity proof computing degree-\(r\) cohomology retains terms through degree \(r+1\), rather than stopping at \(r\).

*Solution.* In the short exact sequence with tail starting at \(r+2\), both its \(H^r\) and \(H^{r+1}\) vanish. The long exact sequence then makes the degree-\(r\) map from the middle complex to its truncation an isomorphism. A tail starting at \(r+1\) can have nonzero \(H^{r+1}\), so this reasoning would not give surjectivity. Concretely, take \(A\xrightarrow{1}A\) in degrees \(r,r+1\), with \(A\ne0\). Its \(H^r\) is zero; the brutal truncation through degree \(r\) is \(A[-r]\), whose \(H^r\) is \(A\).

**Exercise 9 (inverse image and its unit).** Write the unit \(G\to f_*f^{-1}G\) and the counit \(f^{-1}f_*F\to F\) of Theorem 4.1(4), and check a triangular identity.

*Solution.* On \(W\subset Y\), the unit sends \(g\) to the locally represented section \(x\mapsto g_{f(x)}\) on \(f^{-1}(W)\). A local representative for a section of \(f^{-1}f_*F\) is a section \(t\in F(f^{-1}(W))\); the counit restricts \(t\) to the open set on which that representative is being used. Starting with a locally represented section of \(f^{-1}G\), the composite \(f^{-1}G\to f^{-1}f_*f^{-1}G\to f^{-1}G\) first pulls its representative back and then restricts it again; the resulting germ at every point is unchanged. Stalks detect equality, so this is the identity. Starting with \(t\in(f_*F)(W)\) checks the other triangular identity by the same restriction formula.

### Subsequent lessons

- *Noncommutative coefficients.* The lesson Continuing cohomology through a moving boundary uses Theorems 2.1 and 6.1 for sheaves of modules over a noncommutative ring \(k\).
- *Acyclic resolutions.* The lesson Comparing sheaves through local support tests computes derived functors with acyclic resolutions, as in Theorem 6.1(4).
- *Unique lifts.* The lesson Proper-support composition through a change of base uses the lifts of Theorem 6.1(2), unique up to homotopy.
- *The unbounded layer.* The course *Microlocal Sheaves* uses the unbounded constructions of Sections 7–13 as its ordinary categorical layer: K-injective resolutions, the derived tensor product and Hom, the composition map, and the localization triangle with the second sign convention.

## References

- [Stacks] The Stacks project authors, *The Stacks project*, 2026, [stacks.math.columbia.edu](https://stacks.math.columbia.edu).
- [AI Integrated Stacks Project] The Stacks project authors and the contributors to the user's AI-integrated fork, *Cohomology of Sheaves*, [commit 565b10e987aba5969b21145a0833f42d69f96790, cohomology.tex](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex), section “Flat resolutions”. Attribution of individual AI changes follows the fork records; aggregate model history is not substituted for per-change evidence.
- [AI Integrated Stacks Project, derived.tex] The same pinned edition, [Derived Categories](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex): injective resolutions, K-injective comparison and Leray's acyclicity lemma. The proofs are checked and expanded in Section 6 rather than left as external prerequisites. The truncation argument for Leray's lemma follows this source; the explicit pushout construction writes out the dual resolution argument.
- [AI Integrated Stacks Project, injectives.tex] The same pinned edition, [Injectives](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/injectives.tex), sections “Injectives in Grothendieck categories” and “K-injectives in Grothendieck categories”, from the subobject-size lemma through the functorial K-injective embedding theorem (Tag 079P). These are the source passages read for Section 7. Their attribution to Serpé and Spaltenstein is retained; reading these passages is not represented as a separate reading of those original papers. The full construction is included, checked and expanded here.
- [Spaltenstein 1988] N. Spaltenstein, Resolutions of unbounded complexes, *Compositio Mathematica* 65 (1988), no. 2, 121–154, open at [numdam.org](https://www.numdam.org/item/CM_1988__65_2_121_0/).
- [Schapira, *Categories and Homological Algebra*] P. Schapira, [*An Introduction to Categories and Homological Algebra*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/HA.pdf), lecture notes, version of 1 March 2026.
- [Schapira, *Algebra and Topology*] P. Schapira, [*Algebra and Topology*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/AlTo.pdf), lecture notes.
- [Baer 1940] R. Baer, [*Abelian groups that are direct summands of every containing abelian group*](https://www.ams.org/journals/bull/1940-46-10/S0002-9904-1940-07306-9/S0002-9904-1940-07306-9.pdf), Bull. Amer. Math. Soc. **46** (1940), 800–806.
