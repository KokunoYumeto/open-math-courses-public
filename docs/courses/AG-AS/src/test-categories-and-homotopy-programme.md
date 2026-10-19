# Test categories and Grothendieck's homotopy programme

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A simplicial set describes a homotopy type using simplices. A small category can do the same through its nerve, even when its arrows are not invertible. Grothendieck's test-category question asks which indexing categories can replace the simplex category while still giving a presheaf description of all homotopy types. The comparison must work both globally and over each representable presheaf. That second requirement is the local-test condition.

We prove that \(\Delta\) is a test category, including the local condition for every \(\Delta/[n]\). The proof starts with categories of elements and their right adjoint. It then proves a product lemma and an interval contraction before passing to slices. We prove Quillen's Theorem A by a diagram of two chains, then use it to convert contractible comma categories into weak equivalences. The last-vertex comparison is proved by realizing the diagram of all simplices. The lesson ends with modelizers and the higher-stack programme, connecting the one-type result of [Lesson 11](simplicial-sets-nerves-and-kan-complexes.md) to the question of coherent structures in every dimension.

Our source conventions are the settled definitions in Alexander Grothendieck's [Pursuing Stacks, arXiv:2111.01000v2](https://arxiv.org/abs/2111.01000v2), Section 44. Earlier sections use provisional terminology. Sections 28–31 supply the modelizing and asphericity discussion; the opening Sections 2–3 supply the higher-groupoid programme. We work with small categories in a fixed universe and allow a larger universe for their categories and presheaves. Geometric realization, homotopy groups and CW complexes are ordinary topology prerequisites.

## 1. Categories as homotopy types

### 1.1. Weak equivalence and asphericity

For a small category \(C\), its nerve has
\[
N(C)_n=\operatorname{Fun}([n],C).
\tag{1.1}
\]
Its geometric realization \(|N(C)|\) is a space. A functor \(u:A\to B\) is a *weak equivalence* if \(|N(u)|\) induces a bijection on path components and, for every base point and every \(r\geq1\), an isomorphism on \(\pi_r\). Denote this class by \(W_\infty\). It contains identities and satisfies two-out-of-three: in a composite, knowing any two of the three maps are weak equivalences proves the third is one. This follows directly on components and homotopy groups, transporting base points along paths when necessary.

A category is *aspherical* here if its nerve is weakly contractible: its realization is nonempty, has one path component, and has zero homotopy groups in every positive degree. In particular its fundamental group vanishes. This is Grothendieck's convention; in another common use of the word, an aspherical space may have a nontrivial fundamental group. That convention would change every criterion below. The empty category is not aspherical.

For \(u:A\to B\) and \(b\in B\), define the comma category \((u\downarrow b)\). An object is
\[
(a,\lambda),\qquad a\in A,\quad \lambda:u(a)\longrightarrow b.
\tag{1.2}
\]
A morphism from \((a,\lambda)\) to \((a',\lambda')\) is \(\alpha:a\to a'\) satisfying \(\lambda=\lambda' u(\alpha)\). We call \(u\) an *aspherical functor* if every \((u\downarrow b)\) is aspherical. Thus a category is aspherical exactly when its map to the one-object category \(\mathbf1\) is an aspherical functor.

#### Realizing a diagram of simplices

We first prove the elementary realization fact used twice below. All products and realizations may be taken in compactly generated spaces. This convention changes neither maps from spheres nor their homotopies, and therefore changes none of the weak equivalences considered here.

**Realization lemma.** Let \(E_{p,q}\) be a bisimplicial set. Its double realization is naturally homeomorphic to the realization of its diagonal. A map of bisimplicial sets which is a weak equivalence after realizing every horizontal row is a weak equivalence after double realization. The same conclusion holds with the two directions interchanged.

**Proof.** A bisimplicial set is the colimit of its bisimplices. Both realizations commute with those colimits. For a representable bisimplex, the diagonal is \(\Delta[p]\times\Delta[q]\). Its realization is the product of the two geometric simplices: order the successive changes of the two coordinates to triangulate that product by the monotone lattice paths from \((0,0)\) to \((p,q)\). On each path simplex the map sends a barycentric combination to the corresponding pair of barycentric combinations. These simplices cover the product and meet in their common faces. The map is therefore a homeomorphism, compatible with every ordinal map in both coordinates. Passing to colimits gives the first assertion.

For the second assertion, realize the horizontal direction first and write the resulting simplicial spaces as \(X_q\to Y_q\). They are CW complexes. Every degeneracy is the realization of a split injection of simplicial sets and is an inclusion of a CW subcomplex. The union \(L_qX\) of the degenerate subspaces is also a subcomplex. Its intersections are again degeneracy images of lower degrees: factor an ordinal surjection uniquely into its degeneracies, and use the simplicial identities to compute a common image. The same statements hold for \(Y\).

The \(q\)-th realization skeleton is obtained from the preceding skeleton by attaching \(X_q\times\Delta^q\) along
\[
(L_qX\times\Delta^q)\cup(X_q\times\partial\Delta^q).
\]
The elementary gluing fact for CW pairs says that a map of these pushout diagrams which is a weak equivalence on the old skeleton, the attaching space and the new piece is a weak equivalence on the pushout. One way to see the fact is to replace the maps by their mapping cylinders. Whitehead's theorem gives homotopy inverses on the CW pieces, and the homotopy extension property for the attaching inclusions makes these inverses and their homotopies compatible. Equivalently, the ordinary pushout along a cofibration computes the homotopy pushout. This uses the full CW Whitehead and homotopy extension proofs in *Homotopy fibres and the Serre spectral sequence*, Section B, and *Frame fields and primary obstructions*, Section E, of the programme's differential-geometric foundations.

Induction on \(q\), and on the finite union of degeneracy images defining \(L_q\), now proves the skeleton assertion. In that finite union the intersections just described involve only smaller degrees, so the same gluing fact applies; there is no assumption that a levelwise homotopy inverse preserves degeneracies. The product boundary pairs are cofibrations, so it applies to the displayed attaching diagram as well. Finally a sphere map or sphere homotopy meets finitely many cells of the realized CW complex, hence lies in a finite skeleton. The skeleton equivalences give the asserted isomorphisms on all homotopy groups and the bijection on components at the union. The other direction is identical. \(\square\)

**Quillen's Theorem A.** If each \((u\downarrow b)\) has weakly contractible nerve, the functor \(u:A\to B\) belongs to \(W_\infty\).

**Proof.** Form the bisimplicial set whose \((p,q)\)-bisimplices are diagrams
\[
a_0\longrightarrow\cdots\longrightarrow a_p,
\qquad
u(a_p)\longrightarrow b_0\longrightarrow\cdots\longrightarrow b_q.
\]
Faces delete an object and compose the neighbouring arrows; degeneracies insert an identity. In particular deleting \(a_p\) composes the connecting arrow with \(u(a_{p-1}\to a_p)\), and deleting \(b_0\) composes it with \(b_0\to b_1\). These operations commute, so the diagram really defines a bisimplicial set \(E\).

Forget the \(B\)-chain to map its double realization to \(|N(A)|\). For a fixed \(A\)-chain the other direction is the nerve of \((u(a_p)\downarrow B)\), which has initial object the identity of \(u(a_p)\). That nerve contracts by the natural-transformation construction of Section 1.2. Thus every vertical level is a disjoint union of contractible spaces mapping to the corresponding discrete set of \(A\)-chains. The realization lemma proves that the projection
\[
P:|E|\longrightarrow |N(A)|
\]
is weak.

Instead forget the \(A\)-chain to obtain
\[
Q:|E|\longrightarrow |N(B)|.
\]
For a fixed \(B\)-chain the horizontal direction is precisely \(N(u\downarrow b_0)\): the connecting arrow at the last \(A\)-object determines the earlier ones by composition. Its realization is weakly contractible by hypothesis. The realization lemma proves that \(Q\) is weak.

The two maps to \(|N(B)|\), namely \(Q\) and \(|N(u)|P\), are homotopic. On a bisimplex with coordinates \(t\in\Delta^p\), \(s\in\Delta^q\), evaluate the composite chain
\[
u(a_0)\longrightarrow\cdots\longrightarrow u(a_p)
\longrightarrow b_0\longrightarrow\cdots\longrightarrow b_q
\]
at the barycentric coordinates
\[
((1-z)t_0,\ldots,(1-z)t_p,zs_0,\ldots,zs_q),
\qquad 0\leq z\leq1.
\]
At \(z=0\) this is \(|N(u)|P\), and at \(z=1\) it is \(Q\). Deleting a vertex with zero weight or combining two weights on an identity arrow gives exactly the face and degeneracy identifications, including both connecting faces. Hence these formulas glue to a continuous homotopy on \(|E|\). Homotopic maps have the same weak-equivalence status. Since \(P\) and \(Q\) are weak, two-out-of-three gives the result for \(|N(u)|\). The argument also covers empty categories: if \(B\) is nonempty the hypothesis forces the relevant comma categories, and hence \(A\), to be nonempty; if \(B\) is empty both are empty. \(\square\)

The theorem is due to Quillen. This is an independently written proof of the ordinary-category theorem in the orientation of Grothendieck's *Pursuing Stacks*, Section 30. The modern opposite orientation can still be compared with Kerodon as a reference: reverse the chains and their barycentric coordinates to identify \(|N(C^{\mathrm{op}})|\) with \(|N(C)|\). No text from Kerodon is reused.

An aspherical functor need not be an equivalence of categories. The inclusion of the object \(0\) into the ordered category \([1]=\{0<1\}\) has a one-object comma category over either object. It is aspherical, but the object \(1\) is not isomorphic to an object in its image. Asphericity is also not preserved by arbitrary categorical base change: pull that inclusion back along the inclusion of \(1\); the resulting map is \(\varnothing\to\mathbf1\), whose comma category is empty. These examples distinguish a statement about homotopy types from a statement about categorical fibres or equivalences.

### 1.2. Natural transformations give homotopies

Let \(u,v:A\to B\) and let \(\theta:u\Rightarrow v\). Define
\[
H:A\times[1]\longrightarrow B,
\qquad H(a,0)=u(a),\quad H(a,1)=v(a).
\tag{1.3}
\]
On a morphism \((\alpha,0\to1)\), set \(H(\alpha,0\to1)=v(\alpha)\theta_a=\theta_{a'}u(\alpha)\). This equality is precisely naturality. For morphisms staying at \(0\) or \(1\), use \(u(\alpha)\) or \(v(\alpha)\). These formulas respect composition; a sequence in \([1]\) can change from \(0\) to \(1\) only once, and naturality makes that change compatible with any neighbouring arrow.

Nerves preserve products because a functor into a product is a pair of functors. Also \(N([1])=\Delta[1]\). Thus (1.3) gives a simplicial homotopy
\[
N(A)\times\Delta[1]\longrightarrow N(B)
\tag{1.4}
\]
between \(N(u)\) and \(N(v)\). Realizing it gives an ordinary homotopy. Explicitly, triangulate each prism \(\Delta^m\times[0,1]\) by the \(m+1\) simplices whose vertices first stay at height \(0\) and then stay at height \(1\). The simplicial map prescribes an affine realization on each such simplex. Its face identities make these prescriptions agree on shared faces and under all simplex identifications. They therefore glue to a continuous map \(|N(A)|\times[0,1]\to|N(B)|\). The interval is finite, so this prism description also verifies the usual realization identification with the product by the interval.

If \(c\) is final in \(C\), its unique incoming arrows give \(\mathrm{id}_C\Rightarrow\operatorname{const}_c\). The preceding construction contracts \(|N(C)|\) to its vertex \(c\). A category with an initial object contracts by \(\operatorname{const}_c\Rightarrow\mathrm{id}_C\). In both cases it is aspherical. The existence of a final object is a sufficient condition, not part of the definition.

If \(L\colon A\rightleftarrows B\colon R\) is an adjunction, its unit and counit give
\[
\mathrm{id}_A\Rightarrow RL,\qquad LR\Rightarrow\mathrm{id}_B.
\tag{1.5}
\]
Consequently \(|N(L)|\) and \(|N(R)|\) are homotopy inverse. This needs no claim that \(L\) or \(R\) is an equivalence of categories. For example, the map from a category with a final object to \(\mathbf1\) is left adjoint to the inclusion of that final object, and the nerve contraction is the unit homotopy.

## 2. The category-of-elements adjunction

### 2.1. Elements and slice functors

For a small category \(A\), write \(\widehat A=\mathrm{Set}^{A^{\mathrm{op}}}\). For \(X\in\widehat A\), its category of elements \(i_AX=A/X\) has objects \((a,x)\), with \(x\in X(a)\). A morphism
\[
(a,x)\longrightarrow(b,y)
\tag{2.1}
\]
is a morphism \(\alpha:a\to b\) in \(A\) such that \(x=\alpha^*y\). Composition is inherited from \(A\); the presheaf identity ensures that the condition in (2.1) is preserved. A map \(f:X\to Y\) gives \(i_Af(a,x)=(a,f(x))\), with the same underlying morphisms. Thus \(i_A:\widehat A\to\mathrm{Cat}\) is a functor.

For \(a\in A\), the slice \(A/a\) has objects \(\beta:b\to a\) and morphisms \(\gamma:b\to b'\) such that \(\beta=\beta'\gamma\). It has final object \(\mathrm{id}_a\). An arrow \(\alpha:a\to a'\) gives a functor
\[
\alpha_!:A/a\longrightarrow A/a',\qquad \beta\longmapsto\alpha\beta.
\tag{2.2}
\]
Define a presheaf, functorially in \(C\), by
\[
(j_AC)(a)=\operatorname{Fun}(A/a,C),\qquad
\alpha^*F=F\circ\alpha_!.
\tag{2.3}
\]
The functor sets in (2.3) are ordinary sets of functors. Natural transformations between those functors are not extra elements. In particular \(j_\Delta C\) is generally different from the ordinary nerve \(N(C)\), whose degree \(m\) is \(\operatorname{Fun}([m],C)\).

**Proposition 2.1.** The functor \(i_A\) is left adjoint to \(j_A\).

**Proof.** Given \(T:i_AX\to C\), associate to \(x\in X(a)\) the functor
\[
F_x:A/a\longrightarrow C,
\qquad F_x(\beta:b\to a)=T(b,\beta^*x).
\tag{2.4}
\]
On a slice arrow \(\gamma\), use the corresponding element-category arrow \(\gamma\); its defining equality follows from \(\beta=\beta'\gamma\). For \(\alpha:a\to a'\) and \(y\in X(a')\), the two functors \(F_{\alpha^*y}\) and \(F_y\alpha_!\) agree on objects and arrows. Hence (2.4) defines a presheaf map \(X\to j_AC\).

Conversely, suppose \(x\mapsto F_x\) is such a map. Define
\[
T(a,x)=F_x(\mathrm{id}_a).
\tag{2.5}
\]
For an arrow \(\alpha:(a,x)\to(b,y)\), naturality gives \(F_x=F_y\alpha_!\), so its source in (2.5) is \(F_y(\alpha)\). Use the image under \(F_y\) of the slice arrow \(\alpha\to\mathrm{id}_b\) to obtain its map to \(F_y(\mathrm{id}_b)\). For composable \(\alpha:a\to b\) and \(\beta:b\to c\), their two maps are the images, under \(F_z\), of the slice chain
\[
\beta\alpha\longrightarrow\beta\longrightarrow\mathrm{id}_c
\tag{2.6}
\]
in \(A/c\). Its composite is the slice arrow \(\beta\alpha\to\mathrm{id}_c\). This proves functoriality, including identities.

Starting with \(T\), (2.5) recovers its objects and the original arrows. Starting with the family \(F_x\), the reconstructed value at \(\beta:b\to a\) is \(F_{\beta^*x}(\mathrm{id}_b)=F_x(\beta)\), and the arrow reconstruction likewise recovers \(F_x\) on every slice arrow. The constructions are inverse and natural in both \(X\) and \(C\). They prove the adjunction. \(\square\)

The unit sends \(x\in X(a)\) to the functor \(\beta\mapsto(b,\beta^*x)\). The counit is evaluation:
\[
\varepsilon_C:i_Aj_AC\longrightarrow C,
\qquad (a,F)\longmapsto F(\mathrm{id}_a).
\tag{2.7}
\]
Its arrow formula is the one in (2.5). These explicit formulas will prevent confusion with the different last-object evaluation used in Section 3. The adjunction is the one in Pursuing Stacks, Section 29 and Section 44(a).

### 2.2. Weak, local and test categories

Declare a presheaf map \(f\) to be in \(W_A\) when \(i_Af\in W_\infty\). Call \(X\) an *aspherical presheaf* when \(i_AX\) is an aspherical category. These definitions use elements, rather than a topology on \(A\). Define the three conditions as follows.

| Condition on \(A\) | Requirement |
|---|---|
| Weak test | \(\varepsilon_C:i_Aj_AC\to C\) belongs to \(W_\infty\) for every small \(C\). |
| Local test | Every slice \(A/a\) is a weak test category. |
| Test | Both the weak-test and local-test conditions hold. |

These are the conventions of Pursuing Stacks, Section 44(a)–(c). The equivalent formulation of weak test given there as a localization comparison will be proved in Section 5 from the displayed counit condition. The local condition quantifies over all objects of \(A\); showing one favourable slice is insufficient.

**Proposition 2.2 — terminal-category criterion.** The category \(A\) is weak test if and only if \(j_AD\) is an aspherical presheaf for every small category \(D\) having a final object.

**Proof.** If \(A\) is weak test and \(D\) has a final object, the target of \(\varepsilon_D\) has contractible nerve by Section 1.2. Since \(\varepsilon_D\) is weak, its source \(i_Aj_AD\) is weakly contractible. This proves one direction.

For the converse, fix arbitrary \(C\) and \(c\in C\). There is an isomorphism of categories
\[
(\varepsilon_C\downarrow c)\cong i_Aj_A(C/c).
\tag{2.8}
\]
Indeed, an object on the left is \((a,F,\lambda:F(\mathrm{id}_a)\to c)\). It gives the functor \(A/a\to C/c\) which sends \(\beta:b\to a\) to
\[
F(\beta)\xrightarrow{F(\beta\to\mathrm{id}_a)}F(\mathrm{id}_a)
\xrightarrow{\lambda}c.
\tag{2.9}
\]
On slice arrows it uses \(F\); functoriality makes these arrows commute over \(c\). Conversely, a functor to \(C/c\) forgets to \(F\), and its value at \(\mathrm{id}_a\) gives \(\lambda\). Every other map to \(c\) must be (2.9), because there is a slice arrow \(\beta\to\mathrm{id}_a\). Thus these object constructions are inverse.

An arrow \(\alpha\) on the left requires \(F=F'\alpha_!\) and
\(\lambda=\lambda'F'(\alpha\to\mathrm{id}_{a'})\). This is precisely the condition that the associated functors into \(C/c\) agree after \(\alpha_!\). Therefore (2.8) is an isomorphism on arrows too. The category \(C/c\) has final object \(\mathrm{id}_c\), so the hypothesis makes every category in (2.8) aspherical. Quillen's Theorem A proves \(\varepsilon_C\in W_\infty\). If \(C\) is empty, so is \(i_Aj_AC\), since \(A/a\) is nonempty for every \(a\); the counit is the empty identity and is weak. This includes that boundary case. \(\square\)

In particular, a weak test category is aspherical. For \(C=\mathbf1\), its right adjoint is the terminal presheaf, and its category of elements is \(A\) itself. The counit condition says exactly that \(A\to\mathbf1\) is weak. This observation will distinguish local test from test in an example below.

## 3. Two lemmas before the test-category theorem

The following arguments concern ordinary nerves and categories of simplices. They do not assume that \(\Delta\) is already a test category. That order matters: a simplicial contraction of \(j_\Delta C\) will be useful only after we know that simplicial homotopies detect its category-of-elements homotopy type.

### 3.1. Last-object evaluation on strings

For a category \(C\), let \(E(C)=i_\Delta N(C)\). Its objects are strings \(\sigma:[m]\to C\). A morphism from \(\sigma\) to \(\tau:[\ell]\to C\) is an order-preserving \(\alpha:[m]\to[\ell]\) with \(\sigma=\tau\alpha\). Evaluation at the last object defines
\[
e_C:E(C)\longrightarrow C,
\quad e_C(\sigma)=\sigma(m),\quad
e_C(\alpha)=\tau(\alpha(m)\to\ell).
\tag{3.1}
\]
For a composite of ordinal maps, the corresponding arrows compose along their ordered intervals; thus (3.1) is a functor.

**Lemma 3.1.** The functor \(e_C\) is aspherical and belongs to \(W_\infty\).

**Proof.** Fix \(c\in C\). An object of \((e_C\downarrow c)\) is a string \(\sigma\) together with an arrow \(\lambda:\sigma(m)\to c\). Append this arrow and its target to obtain a string \(\sigma^+:[m+1]\to C\). Give it the map \(\mathrm{id}_c\) from its last object to \(c\). This defines an endofunctor \(P\) of the comma category.

To check its arrows, suppose \(\alpha:[m]\to[\ell]\) is a comma arrow from \((\sigma,\lambda)\) to \((\tau,\mu)\). Thus
\[
\sigma=\tau\alpha,
\qquad \lambda=\mu\,\tau(\alpha(m)\to\ell).
\tag{3.2}
\]
Define \(\alpha^+:[m+1]\to[\ell+1]\) by \(\alpha^+(i)=\alpha(i)\) for \(i\leq m\) and \(\alpha^+(m+1)=\ell+1\). The first equality in (3.2) verifies the old part of the string; the second verifies its arrows into the appended object. Hence \(\sigma^+=\tau^+\alpha^+\). The new last-object map is an identity, so the comma condition also holds. Extension by \(+\) respects identity and composition.

The inclusion of the old string gives a natural transformation \(\mathrm{id}\Rightarrow P\): its last-object arrow is \(\lambda\), exactly the required comma arrow. Let \(q\) be the one-term string \(c\) with map \(\mathrm{id}_c\). The inclusion of the new last vertex gives \(\operatorname{const}_q\Rightarrow P\), also natural because every \(\alpha^+\) preserves that new last vertex. By Section 1.2, the identity of the comma nerve is homotopic to \(N(P)\), and \(N(P)\) is homotopic to its constant map at \(q\). Reversing the latter homotopy and concatenating gives an actual contraction. Every comma category is therefore aspherical. Quillen's Theorem A gives the last assertion. \(\square\)

If \(C\) has a final object, it follows that \(E(C)\) is aspherical: its weak map to \(C\) has weakly contractible target. In particular, since nerves preserve products and \(N([r])=\Delta[r]\), we obtain
\[
i_\Delta\bigl(\Delta[m]\times\Delta[n]\bigr)
=E([m]\times[n])\quad\text{aspherical}.
\tag{3.3}
\]
The ordered product category has final object \((m,n)\). Notice that its simplices include degeneracies. Removing them would change the category used in the proof and would need another comparison argument.

### 3.2. Products with simplices and homotopy invariance

**Lemma 3.2.** For every simplicial set \(K\) and \(n\geq0\), the projection
\[
p:i_\Delta(K\times\Delta[n])\longrightarrow i_\Delta K
\tag{3.4}
\]
is aspherical. Consequently \(K\times\Delta[n]\to K\) belongs to \(W_\Delta\).

**Proof.** Fix \((m,x)\in i_\Delta K\). An object of \((p\downarrow(m,x))\) consists of a degree \(\ell\), an element \(y\in K_\ell\), a map \(\alpha:[\ell]\to[n]\), and a map \(\beta:[\ell]\to[m]\) satisfying \(y=\beta^*x\). Thus \(y\) is determined, and the remaining pair \((\beta,\alpha)\) is an \(\ell\)-simplex of \(\Delta[m]\times\Delta[n]\). An arrow is an ordinal map \(\gamma:[\ell]\to[\ell']\) satisfying
\[
\beta=\beta'\gamma,
\qquad \alpha=\alpha'\gamma.
\tag{3.5}
\]
The equality on \(y\) then follows automatically. This identifies the entire comma category, including its arrows, with the category in (3.3). It is aspherical. Quillen's Theorem A proves the claim. For empty \(K\), both element categories are empty, and the result remains valid. \(\square\)

**Lemma 3.3.** If \(f_0,f_1:K\to L\) are joined by a simplicial homotopy, then \(f_0\in W_\Delta\) if and only if \(f_1\in W_\Delta\). If the identity of a nonempty \(K\) is simplicially homotopic to a constant map, then \(K\) is an aspherical presheaf on \(\Delta\).

**Proof.** The projection \(K\times\Delta[1]\to K\) is in \(W_\Delta\) by Lemma 3.2. Its endpoint sections \(s_0,s_1\) also lie in \(W_\Delta\), because their composites with the projection are identities and the class satisfies two-out-of-three. If \(H:K\times\Delta[1]\to L\) is the homotopy, \(f_t=Hs_t\). Applying two-out-of-three twice shows that \(f_0,H,f_1\) are simultaneously weak.

For the second assertion, the constant self-map of \(K\) is therefore in \(W_\Delta\). It factors through \(\Delta[0]\), and
\[
i_\Delta\Delta[0]=\Delta
\tag{3.6}
\]
has final object \([0]\). Hence its nerve is contractible. On path components, an isomorphism factoring through a one-component space forces \(|N(i_\Delta K)|\) to have exactly one component. At the chosen constant vertex, its homotopy groups have an isomorphism factoring through zero groups, so every positive group vanishes. Path connectedness transfers this conclusion to all base points. Nonemptiness comes from the constant vertex. This is precisely asphericity. \(\square\)

The proof uses simplicial homotopies to control \(W_\Delta\) directly. It has not used a theorem identifying \(|N(i_\Delta K)|\) with \(|K|\). Such a comparison will be stated separately in Section 5; it is unnecessary for the required test-category theorem.

## 4. Delta is a test category

### 4.1. Contracting the right adjoint

For each \(m\), there is a last-vertex functor
\[
\ell_m:\Delta/[m]\longrightarrow[m],
\qquad (\beta:[p]\to[m])\longmapsto\beta(p).
\tag{4.1}
\]
If \(\gamma:[p]\to[q]\) is a slice arrow with \(\beta=\beta'\gamma\), then \(\beta(p)=\beta'(\gamma(p))\leq\beta'(q)\). Use this ordered arrow for \(\ell_m(\gamma)\). These arrows respect composition because an ordered category has at most one arrow between any two objects. For every \(\alpha:[m]\to[n]\),
\[
\ell_n\alpha_!=\alpha\ell_m.
\tag{4.2}
\]
The equality holds on objects by evaluation and on arrows by uniqueness. Thus precomposition with \(\ell_m\) gives a natural simplicial map
\[
N(C)\longrightarrow j_\Delta C.
\tag{4.3}
\]
For \(C=[1]\), write it as \(\lambda:\Delta[1]\to j_\Delta([1])\).

**Proposition 4.1.** If \(C\) has a final object \(c\), the simplicial set \(j_\Delta C\) admits a homotopy from its identity to its constant map at the constant functor with value \(c\). Hence \(j_\Delta C\) is an aspherical presheaf.

**Proof.** The unique arrows to \(c\) define a functor \(C\times[1]\to C\) as in (1.3), with endpoints \(\mathrm{id}_C\) and \(\operatorname{const}_c\). The functor \(j_\Delta\) preserves products, as is seen directly in (2.3): a functor into \(C\times D\) is a pair of functors. Apply it to this functor and precompose the second coordinate by \(\lambda\). This gives
\[
j_\Delta C\times\Delta[1]
\xrightarrow{\mathrm{id}\times\lambda}
j_\Delta C\times j_\Delta([1])
\longrightarrow j_\Delta C.
\tag{4.4}
\]
For completeness, the map has the following degreewise formula. For \(F:\Delta/[m]\to C\), \(t:[m]\to[1]\), and \(\beta:[p]\to[m]\), its value is
\[
H(F,t)(\beta)=
\begin{cases}
F(\beta)&t(\beta(p))=0,\\
c&t(\beta(p))=1.
\end{cases}
\tag{4.5}
\]
On a slice arrow the only possible endpoint patterns are \(0\to0\), \(0\to1\), \(1\to1\), because last vertices and \(t\) are nondecreasing. Use respectively the arrow of \(F\), the unique arrow into \(c\), or \(\mathrm{id}_c\). Composition holds within the constant patterns by functoriality, and across the change to \(1\) by uniqueness of the arrow into the final object. Formula (4.2) shows that restriction along every \(\alpha\) commutes with (4.5), so this is a simplicial map, not merely a collection of degreewise contractions.

At constant \(t=0\) the functor is \(F\); at constant \(t=1\) it is constant at \(c\). This proves the homotopy assertion. Its constant functors supply a vertex, so Lemma 3.3 applies and proves asphericity. \(\square\)

By Proposition 2.2, Proposition 4.1 already proves that \(\Delta\) is a weak test category. The construction is an interval argument of the kind developed in Pursuing Stacks, Section 31. Its explicit last-vertex formula here also prepares the slice proof.

### 4.2. Presheaves over a simplex

Fix \(n\geq0\), and put \(B=\Delta/[n]\). There is an equivalence
\[
\widehat B\simeq\mathrm{sSet}/\Delta[n].
\tag{4.6}
\]
Here is its construction. From a presheaf \(X\) on \(B\), form the simplicial set
\[
K_m=\coprod_{\alpha:[m]\to[n]}X([m],\alpha),
\tag{4.7}
\]
with map to \(\Delta[n]\) sending a member of that summand to \(\alpha\). For \(\gamma:[p]\to[m]\), restriction sends its summand into the summand for \(\alpha\gamma\), by the corresponding arrow in \(B\). The presheaf identities give the simplicial identities. Conversely, for a map \(K\to\Delta[n]\), take its fibre over \(\alpha\) in degree \(m\). Its restrictions give a presheaf on \(B\). The two constructions recover their objects and maps, giving (4.6).

Under this equivalence the element categories agree:
\[
i_BX\cong i_\Delta K.
\tag{4.8}
\]
Indeed, an object on either side is a degree \(m\), an ordinal map \(\alpha:[m]\to[n]\), and an element of the corresponding fibre. An arrow is an ordinal map preserving that element by restriction; preservation of \(\alpha\) is then exactly its compatibility with the structure map to \(\Delta[n]\).

For \(b=([m],\alpha)\in B\), there is also a canonical isomorphism
\[
B/b\cong\Delta/[m].
\tag{4.9}
\]
An object of \(B/b\) is an arrow into \(b\). Its underlying ordinal map \(\gamma:[p]\to[m]\) determines its domain in \(B\), namely \(([p],\alpha\gamma)\). Hence it is exactly an object of \(\Delta/[m]\). The morphism conditions are the same commuting triangles. These isomorphisms commute with postcomposition into a new object of \(B\).

Applying (2.3) and (4.9), the presheaf \(j_BC\) in (4.6) is therefore the object
\[
j_\Delta C\times\Delta[n]\longrightarrow\Delta[n].
\tag{4.10}
\]
Its degree \(m\) consists of a pair \((F,\alpha)\), with \(F:\Delta/[m]\to C\) and \(\alpha:[m]\to[n]\). A restriction along \(\gamma\) is \((F\gamma_!,\alpha\gamma)\). This verifies (4.10) on all operators. In particular the slice right adjoint is not replaced by the ordinary nerve of \(C\).

### 4.3. The global and local theorem

**Theorem 4.2 — Grothendieck.** The category \(\Delta\) is a test category. Every \(\Delta/[n]\), for \(n\geq0\), is also a test category.

**Proof.** Proposition 4.1 and the terminal-category criterion prove the weak-test condition for \(\Delta\). To prove the local condition, fix \(B=\Delta/[n]\) and let \(C\) have a final object. Its \(j_\Delta C\) is aspherical by Proposition 4.1. Lemma 3.2 says that
\[
i_\Delta(j_\Delta C\times\Delta[n])
\longrightarrow i_\Delta j_\Delta C
\tag{4.11}
\]
is weak. The target is aspherical, so the source is aspherical too. By (4.8)–(4.10), this source is \(i_Bj_BC\). Proposition 2.2 now proves that \(B\) is weak test. This holds for every \(n\), including \(n=0\), and proves that \(\Delta\) is local test. The two conditions together make it a test category.

Finally fix \(B=\Delta/[n]\) again. It is already weak test. Every slice \(B/b\) is \(\Delta/[m]\) by (4.9), and all these categories have just been proved weak test. Hence \(B\) is local test as well and therefore test. No assumption of strictness or of a geometric-realization comparison has entered the proof. \(\square\)

### 4.4. Products and further examples

A test category is *strict* when its category-of-elements comparison preserves binary products of homotopy types: for all \(X,Y\in\widehat A\), the natural functor
\[
i_A(X\times Y)\longrightarrow i_AX\times i_AY
\tag{4.12}
\]
is weak. The terminal comparison is already weak by the weak-test condition. This is the convention in Pursuing Stacks, Section 44(c).

**Proposition 4.3.** The category \(\Delta\) is strict test. For \(n\geq1\), its test-category slice \(\Delta/[n]\) is not strict.

**Proof.** At an object \(((m,x),(n,y))\) of the target of (4.12) for \(A=\Delta\), a comma object consists of a degree \(\ell\), maps \(\beta:[\ell]\to[m]\) and \(\gamma:[\ell]\to[n]\), and an element of \((X\times Y)_\ell\) necessarily equal to \((\beta^*x,\gamma^*y)\). The latter is determined. Comma arrows are precisely ordinal maps commuting with \(\beta\) and \(\gamma\). Thus the comma category is \(i_\Delta(\Delta[m]\times\Delta[n])\), aspherical by (3.3). Quillen's Theorem A makes (4.12) weak. Theorem 4.2 supplies the test condition, so \(\Delta\) is strict.

For \(B=\Delta/[n]\) with \(n\geq1\), take its two objects which are the distinct vertices \(0,1:[0]\to[n]\), and their representable presheaves \(X,Y\). The element category of a representable \(B(-,b)\) is \(B/b\), with final object \(\mathrm{id}_b\). Thus \(i_BX\) and \(i_BY\) are nonempty and contractible. But an object \(([m],\alpha)\) mapping to the vertex \(0\) requires \(\alpha\) constant at \(0\), whereas one mapping to \(1\) requires it constant at \(1\). No object admits both maps. Hence \(X\times Y\) is empty. The comparison (4.12) has empty source and nonempty target, so is not weak on components. This disproves strictness. For \(n=0\), the slice is isomorphic to \(\Delta\), so that exception is strict. \(\square\)

There are two further useful boundary examples. The one-object category \(\mathbf1\) is not weak test. Its right adjoint on \([1]\) is the discrete two-element presheaf, since a functor from \(\mathbf1\) chooses either object of \([1]\). Its element category has two components, although \([1]\) has contractible nerve. The counit cannot be weak. Having an aspherical indexing category by itself is insufficient.

The disjoint union \(\Delta\amalg\Delta\) is local test: every object lies in one component, and its slice is a \(\Delta/[n]\), weak test by Theorem 4.2. It is not weak test because its nerve has two components; the terminal counit therefore fails. So local test by itself is insufficient as well. The slices \(\Delta/[n]\) give the further test-category examples verified in the source, with their precise limitation on products. We need no unproved claim about a differently defined cube category.

## 5. Modelizers and the localization comparison

### 5.1. What a modelizer specifies

Write
\[
\mathrm{Hot}=\mathrm{Cat}[W_\infty^{-1}].
\tag{5.1}
\]
Localization means universally making all arrows in the indicated class invertible. Its morphisms can contain formal inverses of weak arrows, so it is not obtained by identifying only isomorphic categories. As throughout the lesson, universe enlargement addresses size.

A *modelizer* is a category \(M\), a class \(W\) of its arrows, and an equivalence of its localization with \(\mathrm{Hot}\), where \(W\) is exactly the class of arrows which become invertible in that localization. This last condition is called saturation. It specifies the weak equivalences along with the resulting category of homotopy types. It does not specify cofibrations, fibrations, factorization axioms or a particular Quillen model structure. The terminology and this distinction come from Pursuing Stacks, Section 28 and Section 29. We do not use the speculative uniqueness assumption discussed alongside those definitions.

The class \(W_\infty\) is saturated. Here is the argument, with its ordinary topology input made explicit. Nerve realizations are CW complexes. The exact preceding programme proof is [*Homotopy fibres and the Serre spectral sequence*, Section B](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/DG-CHAR/homotopy-fibres-and-the-serre-spectral-sequence.md), in *Differential-geometric foundations*. Lemmas B.1–B.2 and the relative homotopy sequence (B.4) prove cellular compression; the proof following Theorem B.5 applies it to a cellular mapping cylinder to prove CW Whitehead. Its displayed proof is path connected, and the extension to the present scope is short. Every CW component is open and closed: a characteristic disk lies in one path component, and the weak topology therefore tests the component and its complement as closed on every disk. A weak equivalence bijects those components. Apply the connected theorem on each corresponding pair and glue the homotopy inverses and their homotopies over the open components. This proves Whitehead for arbitrary CW complexes, including the empty complex. Replacing spaces of CW homotopy type by CW models gives that formulation as well. The independently written provider is current programme text; its immediate homotopy-extension and cellular-approximation proofs have the exact earlier locations recorded below. [Kerodon, Proposition 3.6.3.8](https://kerodon.net/tag/013X) remains a reference locator. Consequently realization gives a functor
\[
\mathrm{Hot}\longrightarrow\mathrm{Ho}(\mathrm{CW}),
\tag{5.2}
\]
where the target has continuous maps modulo homotopy. If a functor becomes invertible in \(\mathrm{Hot}\), its image is invertible in this target. An inverse in the homotopy category is a continuous map with both composites homotopic to the respective identities, so its nerve realization is a homotopy equivalence. It is therefore a weak homotopy equivalence, proving saturation. The reverse implication is part of the definition of localization.

### 5.2. Presheaves on a weak test category

**Proposition 5.1.** If \(A\) is weak test, the adjunction of Proposition 2.1 induces inverse equivalences
\[
\widehat A[W_A^{-1}]
\underset{j_A}{\overset{i_A}{\rightleftarrows}}
\mathrm{Hot}.
\tag{5.3}
\]
The class \(W_A\) is saturated. Thus \((\widehat A,W_A)\) is a modelizer.

**Proof.** By definition \(i_A\) preserves weak equivalences. For a functor \(u:C\to D\), naturality of the counit gives
\[
\varepsilon_D\,i_Aj_A(u)=u\,\varepsilon_C.
\tag{5.4}
\]
Both counits are weak because \(A\) is weak test. Two-out-of-three in this equality says that \(i_Aj_A(u)\) is weak if and only if \(u\) is weak. Hence \(j_A\) preserves weak equivalences, and it also reflects them with respect to the classes in question.

For the unit \(\eta_X:X\to j_Ai_AX\), the first adjunction triangle reads
\[
\varepsilon_{i_AX}\,i_A(\eta_X)=\mathrm{id}_{i_AX}.
\tag{5.5}
\]
Again the counit is weak, so \(i_A(\eta_X)\) is weak and \(\eta_X\in W_A\). Both functors descend to the localizations. All their units and counits become natural isomorphisms there, giving the equivalences (5.3). This proves the comparison, rather than just citing it as another test-category theorem.

If a presheaf map \(f\) becomes invertible in the left side of (5.3), its image \(i_Af\) becomes invertible in \(\mathrm{Hot}\). Saturation of \(W_\infty\) implies \(i_Af\in W_\infty\), which means exactly \(f\in W_A\). The other direction is automatic. Thus \(W_A\) is saturated. \(\square\)

The global modelizing conclusion needs only the weak-test condition. The local-test condition gives the same comparison over every representable: \(\widehat A/A(-,a)\) is equivalent to \(\widehat{A/a}\), by the fibre construction of (4.6) with \(A\) in place of \(\Delta\). For a test category, every one of these slice presheaf categories is therefore a modelizer as well. For \(A=\Delta\), equations (4.6)–(4.11) show exactly how the relative model and its right adjoint work.

Strictness adds control of products. It is useful when a homotopy model must retain products as part of a construction, rather than merely present the correct localized category. Proposition 4.3 supplies this additional property for \(\Delta\), and the slice counterexample shows it cannot be inferred for every test category.

### 5.3. The relation with ordinary geometric realization

We next prove the auxiliary comparison with ordinary realization. It is not an input to Theorem 4.2 or Proposition 5.1.

**Last-vertex comparison.** For every simplicial set \(K\), there is a natural simplicial map
\[
\lambda_K^+:N(i_\Delta K)\longrightarrow K
\tag{5.6}
\]
whose realization is a weak homotopy equivalence. The precise locator is [Kerodon, Corollary 11.9.11.5, in Subsection 11.9.11](https://kerodon.net/tag/01N8); its map is Construction 11.9.11.2. This archived subsection also points to the replacement treatment in Section 6.3.6. The proof below supplies the weak-equivalence assertion used here; the source remains a comparison locator, with no Kerodon text reused.

The map can be described directly. An \(r\)-simplex of its source is a chain of simplices of \(K\), with ordinal maps
\[
([m_0],x_0)\xrightarrow{\alpha_1}\cdots
\xrightarrow{\alpha_r}([m_r],x_r).
\tag{5.7}
\]
For each \(i\), transport the last vertex \(m_i\) to \([m_r]\) by the remaining ordinal maps. The resulting numbers \(v_0,\ldots,v_r\) are nondecreasing: at the next stage, \(\alpha_{i+1}(m_i)\leq m_{i+1}\), and all remaining maps preserve order. They define an order-preserving map \(v:[r]\to[m_r]\). Send (5.7) to \(v^*x_r\). Deleting an intermediate object leaves the corresponding transported last vertices unchanged; deleting the last object pulls back the final simplex by \(\alpha_r\); repeating an object repeats its transported last vertex. These verifications show the formula commutes with all faces and degeneracies. Applying a map of simplicial sets changes only the \(x_i\), proving naturality.

**Proof of the weak-equivalence assertion.** The map \(\lambda_K^+\) is the map described in (5.7). We prove its weak-equivalence assertion for every simplicial set, including simplicial sets with degenerate faces and repeated vertices.

Put \(C=i_\Delta K\). An object \(c=([n],x)\) defines a simplex \(D(c)=\Delta[n]\), and an arrow \(\alpha:c\to c'\) defines its ordinal simplicial map. Form a bisimplicial set \(H\) with
\[
H_{p,q}=\coprod_{c_0\to\cdots\to c_p}D(c_0)_q.
\]
The first horizontal face applies \(D(c_0\to c_1)\) to its simplex; the other horizontal faces delete an object, with composition where needed. The vertical operations are those of \(D(c_0)\). Functoriality of \(D\) makes them commute.

There are two augmentations. Forgetting the chosen simplex maps \(|H|\) to \(|N(C)|\). For each \(C\)-chain the vertical fibre is \(|\Delta[n_0]|\), a contractible geometric simplex, so this augmentation is weak by the realization lemma. The other augmentation evaluates the chosen simplex in \(K\). In fixed degree \(q\), the horizontal simplicial set is the nerve of the category with objects
\[
(c,\beta),\qquad c=([n],x),\quad\beta:[q]\to[n],
\]
and arrows \(\alpha\) satisfying \(\alpha\beta=\beta'\). Its evaluation \(\beta^*x\in K_q\) is constant on arrows. The fibre over \(\sigma\in K_q\) is exactly
\[
(([q],\sigma)\downarrow C).
\]
It has initial object the identity of \(([q],\sigma)\). Thus the horizontal augmentation is degreewise a disjoint union of contractible nerve realizations over \(K_q\). The realization lemma gives a weak equivalence \(|H|\to|K|\).

It remains to identify the map these two augmentations compare. On a bisimplex write \(c_i=([n_i],x_i)\), let \(\alpha_{ip}:[n_i]\to[n_p]\) be the composite remaining ordinal map, and let \(\beta:[q]\to[n_0]\) be its chosen simplex. In the last geometric simplex \(\Delta^{n_p}\), the evaluation augmentation has coordinate vector
\[
\alpha_{0p,*}\beta_*s,
\]
whereas last-vertex evaluation of its \(C\)-chain has coordinate vector
\[
\sum_{i=0}^p t_i e_{\alpha_{ip}(n_i)}.
\]
Here ordinal maps act by adding barycentric coordinates with the same image. Join the two displayed vectors by a straight segment inside \(\Delta^{n_p}\), and evaluate it by \(x_p\). The formula respects the horizontal and vertical face and degeneracy identifications. When the final object is deleted, its whole segment is the image of the corresponding segment in \(\Delta^{n_{p-1}}\); when the first object is deleted, the chosen simplex is transported by \(\alpha_{01}\). Hence it gives a homotopy between the evaluation augmentation and the composite through \(|\lambda_K^+|\).

Both augmentations are weak. Their homotopy and two-out-of-three therefore prove that
\[
|\lambda_K^+|:|N(i_\Delta K)|\longrightarrow |K|
\]
is weak. This supplies the complete comparison without treating the category of all simplices as the face poset of a nondegenerate simplicial complex. \(\square\)

The proved comparison says that \(W_\Delta\) is exactly the usual class of simplicial maps whose realizations are weak equivalences. Indeed, apply naturality of (5.6) to \(f:K\to L\); the two vertical realization comparisons are weak, so two-out-of-three equates the weak-equivalence status of \(|N(i_\Delta f)|\) and \(|f|\). This interpretation agrees with the simplicial model from Lesson 11.

#### Sphere maps in a realization

The cylinder and face-relation lemmas below refer to *Simplicial sets, nerves and Kan complexes*, §5.3: Lemmas 5.3a–5.3b and equations (5.11)–(5.14). We use their actual face-group conventions and based homotopies.

We next obtain just the realization comparison needed for the singular counit. We prove surjectivity of the canonical map from a Kan complex's face groups to the groups of its realization. A full injectivity assertion is unnecessary for the argument that follows and is not substituted for the assigned Whitehead theorem.

Let \(C(K)\) be the category of all simplices of \(K\). Let \(C_{\mathrm{face}}(K)\) have the same objects but only the injective ordinal maps as arrows. The last-vertex map restricts to a simplicial map
\[
\ell:N(C_{\mathrm{face}}(K))\longrightarrow K.
\tag{5.9}
\]

**Lemma 5.2.** Its realization is weak.

**Proof.** Apply the preceding Quillen A theorem to the inclusion \(u:C_{\mathrm{face}}(K)\to C(K)\). For \(c=([n],x)\), the comma category \((u\downarrow c)\) identifies with the category of ordinal maps \(\alpha:[m]\to[n]\), whose arrows are injective \(\beta:[m]\to[m']\) with \(\alpha=\alpha'\beta\). The simplex in its source is forced to be \(\alpha^*x\), so no choices of lifts are suppressed.

Append the value \(n\) to each \(\alpha\) to define \(\alpha^+:[m+1]\to[n]\), and append the last vertex to each injective arrow. This is a functor \(F\). Initial-segment inclusion gives a natural transformation \(1\to F\). Last-vertex inclusion gives a natural transformation from the constant object \(([0],n)\) to \(F\). These transformations contract the nerve, by the natural-transformation homotopies already proved. Thus the comma category is nonempty and contractible.

Quillen A makes \(|N(u)|\) weak. The already proved last-vertex map \(|N(C(K))|\to|K|\) is weak. Their composite is \(|\ell|\), proving the claim. \(\square\)

This nerve has a convenient triangulation. A nonidentity injective ordinal map strictly increases dimension. Hence a nondegenerate chain has distinct objects and distinct vertices. No face of that chain is degenerate, and two faces in the same simplex cannot be identified, since they have different vertex sets. Its characteristic simplex is therefore embedded. Two closed simplices intersect in a union of their faces. Subdividing these embedded simplices by their chains of faces gives the ordinary order complex of their face poset, a genuine simplicial complex, with a homeomorphism onto \(|N(C_{\mathrm{face}}(K))|\). Multiple arrows with the same endpoints remain distinct cells and acquire distinct barycentres; they are not identified by a face-poset shortcut. On every original simplex the subdivision homeomorphism is the usual barycentric affine map, so the pieces agree on faces.

The two spaces in Lemma 5.2 are CW complexes. The existing CW Whitehead proof consequently makes (5.9) a homotopy equivalence after realization. Its based version needs a small explicit refinement. Make the comparison cellular relative to its chosen vertex. In its mapping cylinder \(M\), write \(X\) for the domain and \(J\) for that vertex's cylinder segment. First prescribe the identity on \(X\) and contract \(J\) towards its domain endpoint. Homotopy extension from the subcomplex \(X\cup J\) extends this to \(M\). The last map sends \(X\cup J\) into \(X\), with \(J\) constant. The relative groups of \((M,X)\) vanish, so the existing cellular compression now moves that last map into \(X\), fixing \(X\cup J\). The resulting retraction \(r:M\to X\) sends all of \(J\) to the basepoint.

Restrict \(r\) to the codomain to obtain the based inverse. For its composite on \(X\), use the cylinder homotopy followed by \(r\); the basepoint remains fixed because \(r(J)\) is constant. For its composite on the codomain, push the prescribed compression homotopy back by the cylinder retraction onto the codomain; that retraction is constant on \(J\), so its basepoint also stays fixed. This gives both based comparison homotopies. Components can be handled separately, as in the existing test-category lesson. In particular the inverse can be based at \(([0],x)\) above \(x\).

We record explicitly the finite approximation argument. A compact subset of a closure-finite CW complex lies in a finite subcomplex. Otherwise choose one point of it in each of infinitely many open cells. Every subset of these chosen points intersects each closed cell in a finite closed set, so the weak topology makes every such subset closed. The chosen points are therefore a closed infinite discrete subset of the compact subset, a contradiction. Taking the finite union of the closures of the finitely many cells it meets gives the stated finite subcomplex.

A map from a finite complex \(P\) to a simplicial complex \(M\) is homotopic to a simplicial map after sufficiently many barycentric subdivisions of \(P\). To see this, cover its image by open vertex stars in the finite target subcomplex just obtained. Uniform continuity and the Lebesgue number on the finite source allow subdivisions whose closed vertex stars map into individual target open stars. Choose the corresponding target vertex for every source vertex. For a source simplex, an interior point belongs to all its vertex stars; its image lies in all the chosen target stars. Their vertices therefore belong to one target simplex. This gives a simplicial map. The original image and the affine image of that map lie in the same target simplex; the straight-segment homotopy there agrees on faces. A prescribed vertex can be fixed: first keep a small neighbourhood of that vertex in its target star, and choose that target vertex for it. This proves the based version as well.

Apply this to a based sphere map into \(|K|\), after the based inverse in Lemma 5.2 and the triangulation just described. Compose the resulting simplicial approximation into the subdivided nerve with its ordinary last-vertex map and then (5.9). The ordinary last-vertex map of a subdivided embedded simplex is homotopic to its subdivision homeomorphism by the straight segment in that simplex. The resulting map
\[
a:P\longrightarrow K
\tag{5.10}
\]
has realization based homotopic to the original sphere map. Here \(P\) can be an iterated barycentric subdivision of the standard boundary of an \((n+1)\)-simplex.

For use in normalizing (5.10), these triangulated spheres have a facet whose complementary closed ball is collapsible. Here are the geometric and combinatorial reasons. A barycentric subdivision of a polytopal simplicial sphere is polytopal: perform stellar subdivisions at its faces in decreasing dimension. For a face take a relative-interior point \(z\), an interior point \(q\) of the polytope, and put the new vertex at \(z+\varepsilon(z-q)\). Every supporting inequality of a facet containing the face is an equality at \(z\) and strict at \(q\), so this point is beyond that facet. All other inequalities are strict at \(z\), and remain strict for sufficiently small \(\varepsilon>0\). The visible region is precisely the star of that face, and coning its boundary to the new vertex replaces that star by its stellar subdivision. The new boundary is its stellar subdivision. Successively doing this for the faces gives the barycentric subdivision. Thus every finite iterated subdivision above is a simplicial convex-polytope boundary.

Such a boundary has a shelling starting with any prescribed facet and ending with one facet. Choose a generic oriented line \(\ell(t)\), with \(\ell(0)\) in the interior, exiting through the prescribed facet. Each supporting hyperplane meets it at a distinct nonzero parameter \(t_F\). List first the facets with \(t_F>0\) in increasing order, and then those with \(t_F<0\) in increasing order from the negative end towards zero. This is the line shelling order.

To check it, restrict the adjacent supporting inequalities to the simplex facet \(F\). At the point \(\ell(t_F)\), an adjacent inequality belonging to \(G\) is violated exactly when \(t_F/t_G>1\): its value at zero is strictly inside, and its equality occurs at \(t_G\). In the positive part of the list this selects exactly the earlier adjacent facets. In the negative part it selects exactly the later adjacent facets, so the earlier ones are its complementary, nonviolated faces. The intersection of \(F\) with the previously listed boundary is therefore, respectively, the visible or the invisible union of its codimension-one faces. Lower-dimensional intersections introduce no extra pieces: the supporting inequalities of the ridges bound the simplex \(F\), and any redundant inequality from a nonadjacent facet can be violated on a face only when a bounding ridge inequality already is. Before the first positive intersection the line is inside the polytope; at the last negative intersection it re-enters it. At all intervening intersections the point is outside the simplex \(F\), and at least one adjacent inequality is violated and at least one is not. The union is consequently nonempty after the first facet and proper before the last. A nonempty proper union of simplex faces is a ball: a vertex opposite an omitted face belongs to every retained face, expressing that union as the cone on its retained boundary intersections. This verifies the shelling condition and both end cases.

Omit the last facet. The preceding facets form a shellable ball \(A\). This ball is collapsible: reverse its shelling. For a last simplex whose retained intersection is a nonempty proper union of its faces, remove the remaining faces in pairs, pairing a face not in that intersection with its union with the vertex opposite an omitted face. Order pairs by decreasing dimension. Each pair is then a simplex with a single free face; the other faces have been retained or removed earlier. This removes exactly that simplex's complement of the retained intersection. Repeat through the shelling and finally collapse the first simplex to a vertex. Equivalently, reversing this list builds \(A\) from a vertex by horn attachments. Its collapse can end at any prescribed vertex: the same pairing for the first simplex ends there, and the preceding shelling removal leaves the whole first simplex. When fixing the sphere's basepoint, choose the initial facet to contain that vertex.

**Lemma 5.3.** If \(K\) is Kan, the canonical map
\[
\theta:\pi_n(K,x)\longrightarrow\pi_n(|K|,x)
\tag{5.11}
\]
is a surjective homomorphism for every \(n\geq1\). It maps a cycle to its characteristic simplex with its boundary collapsed.

**Proof.** A simplex (5.12) gives a relative prism homotopy by Lemma 5.3b of Lesson 11, so the map is well defined. The horn defining a product has final three faces \(b,c,a\). Its realized boundary, with the other faces collapsed, gives the pinch relation \([c]=[b][a]\). For \(n=1\) this is the triangle relation \(c=ba\). For \(n>1\), the three oriented faces have signs
\[
(-1)^{n-1},\quad(-1)^n,\quad(-1)^{n+1};
\]
after a common orientation change the relation is \(b-c+a=0\), exactly the same pinch product. Thus (5.11) is a homomorphism with the lesson's product convention.

Use (5.10) for any given class in the target. Choose the collapsible complementary ball \(A\subset P\) above, containing the based vertex. Its inclusion from that vertex is anodyne. the cylinder statement (5.14) of Lemma 5.3a in Lesson 11 contracts \(a|A\) to the constant map at \(x\), fixing the vertex: prescribe the original and constant maps at the two ends and that constant value on the vertex cylinder. the cylinder statement (5.13) of Lemma 5.3a in Lesson 11 extends this homotopy over \(P\), starting with \(a\). At its end all of \(A\) is constant. The sole remaining facet consequently gives an \(n\)-cycle in \(K\). The quotient \(P/A\) is its geometric simplex with the entire boundary collapsed.

This quotient identifies the realized map with (5.11) applied to that cycle, with degree \(+1\) or \(-1\) according to the ordering of the chosen facet. If its orientation is negative, replace the cycle class by its inverse. This retains the specified orientation of the original sphere and proves surjectivity. All homotopies kept the basepoint fixed. \(\square\)

Only CW Whitehead, the preceding Quillen A/last-vertex proofs, ordinary finite simplicial approximation and these displayed horn homotopies enter Lemma 5.3.

#### Singular cycles and arbitrary spaces

For any topological space \(T\),
\[
\operatorname{Sing}(T)_n=\operatorname{Cont}(|\Delta[n]|,T).
\]
It is Kan without any separation or local-contractibility hypothesis. In barycentric coordinates \(t_0,\ldots,t_n\), a retraction onto the \(k\)-th horn is
\[
\mu=\min_{i\ne k}t_i,\qquad
r_i=t_i-\mu\ (i\ne k),\quad r_k=t_k+n\mu.
\tag{5.12}
\]
It is continuous, has nonnegative coordinates of sum one, has a zero coordinate with index different from \(k\), and fixes the horn. A continuous horn map extends by composing with (5.12).

**Lemma 5.4.** For every \(t\in T\) and \(n\geq1\), realization of the domain of a singular cycle gives a natural isomorphism
\[
\psi:\pi_n(\operatorname{Sing}(T),t)\longrightarrow\pi_n(T,t).
\tag{5.13}
\]

**Proof.** A singular cycle is precisely a continuous map from \(\Delta^n\) to \(T\) constant at \(t\) on its boundary. The quotient \(\Delta^n/\partial\Delta^n\) is the based sphere. Thus every based sphere class has such a cycle representative.

An elementary homotopy (5.12) gives a based topological prism homotopy by Lemma 5.3b of Lesson 11. Conversely any based continuous homotopy of these sphere maps is a continuous map
\[
\Delta^n\times[0,1]\to T
\]
constant on the sides. Restrict it to the standard prism simplices \(P_i\). Those restrictions, with their affine face and degeneracy pullbacks, are a simplicial map \(\Delta[n]\times I\to\operatorname{Sing}(T)\). Lemma 5.3b of Lesson 11 makes its two cycles equivalent in the exact face definition. Hence (5.13) is bijective. The triangle/pinch argument and orientations in Lemma 5.3 verify its group law. Composition with a continuous map of spaces preserves all the constructions, giving naturality. \(\square\)

**Theorem 5.5.** The evaluation counit
\[
\epsilon_T:|\operatorname{Sing}(T)|\longrightarrow T,\qquad
[(\sigma,s)]\longmapsto\sigma(s),
\tag{5.8}
\]
is a weak homotopy equivalence for every topological space \(T\).

**Proof.** Face and degeneracy pullbacks make the displayed evaluations agree under all realization identifications. The quotient topology therefore makes (5.8) continuous.

Every point of \(T\) is a singular vertex, so the map is surjective on components. Every point of the realization lies in a characteristic simplex and is joined within it to a vertex. If two singular vertices are joined by a path in \(T\), that path is itself a singular one-simplex and joins them in the realization. Conversely the image of a realization path is a path in \(T\). Thus (5.8) bijects components.

At a singular vertex \(t\), the triangle
\[
\begin{array}{ccc}
\pi_n(\operatorname{Sing}(T),t)&\xrightarrow{\theta}&
 \pi_n(|\operatorname{Sing}(T)|,t)\\
&\searrow\psi&\downarrow(\epsilon_T)_*\\
&&\pi_n(T,t)
\end{array}
\tag{5.14}
\]
commutes strictly on representatives: evaluating a characteristic singular simplex returns the original continuous simplex. Lemma 5.3 says that \(\theta\) is surjective. Lemma 5.4 says that \(\psi\) is an isomorphism.

It follows that \((\epsilon_T)_*\) is surjective. For injectivity, write a class \(z\) in its kernel as \(\theta(a)\). Then \(\psi(a)=0\), so \(a=0\) by Lemma 5.4, and hence \(z=0\). The homomorphism is therefore an isomorphism in every positive degree.

Any other point of the realization is joined to a vertex by the path in its characteristic simplex. Ordinary basepoint transport along that path, and along its evaluated image, gives a commuting square of homotopy groups with the two transport maps isomorphisms. The result at that vertex proves the result at the original point. Thus all basepoints are covered. If \(T\) is empty, its singular set and realization are empty and the component assertion remains correct. This proves the theorem. \(\square\)

For arbitrary \(T\), the conclusion is a weak equivalence. If \(T\) has CW homotopy type, the existing CW Whitehead provider upgrades it to a homotopy equivalence. No such upgrade is asserted for a general space.

The arbitrary-space counit is the statement of [Kerodon, Corollary 3.6.4.2](https://kerodon.net/tag/0143). The argument above supplies it here in independent expression; the reference is not a copied proof. Combined with the last-vertex comparison for \(K=\operatorname{Sing}(T)\), it gives a nerve realization representing every ordinary weak homotopy type.

## 6. The higher-groupoid and higher-stack programme

### 6.1. The homotopy hypothesis

The *homotopy hypothesis* asks for an equivalence, at the appropriate homotopy level, between spaces and weak \(\infty\)-groupoids. Its truncated form asks that weak \(n\)-groupoids model precisely homotopy \(n\)-types: spaces with \(\pi_r=0\) for \(r>n\), without a connectedness assumption. This is a programme requiring a definition of weak higher groupoid and its weak equivalences. It is not a theorem about the naive structures obtained by making every higher composition and every coherence law strictly equal.

The proposed dictionary begins with points as objects, paths as arrows, homotopies of paths as two-arrows, and homotopies between those homotopies as three-arrows. Paths are invertible up to homotopy. Path concatenation depends on parametrization, and its associativity comparison is itself a homotopy. In successive dimensions these comparisons must have compatible further comparisons. Replacing them all by equalities is an additional constraint; it does not follow from the topological construction. This is the issue raised in Pursuing Stacks, Section 2 followed by the modelizing discussion in Section 3.

Lesson 11 supplies a complete result in the first nontrivial case: groupoids model homotopy one-types. The nerve of a groupoid is Kan, its higher groups vanish, and the fundamental-groupoid unit is a weak equivalence for a Kan one-type. Its horn proofs show the mechanism: choices of composites become irrelevant on homotopy classes because three-dimensional fillers provide the comparison. In a general Kan complex, higher simplices continue to carry information, and replacing it by its fundamental groupoid discards that information. Taking all those dimensions seriously is the higher-groupoid problem.

Test categories address a related but distinct issue. They give presheaf models for homotopy types and comparisons among those models. A presheaf on a test category is not automatically a chosen algebraic definition of weak \(\infty\)-groupoid. Proposition 5.1 proves that the localized presheaf category presents \(\mathrm{Hot}\); further work is needed to compare a particular higher-groupoid theory with it. This lesson proves the test-category theorem and describes that further programme, without claiming a general solution for unspecified higher-groupoid structures.

### 6.2. Descent in higher dimensions

Let \(\mathcal C\) be a site. The groupoid stacks of [Lesson 4](stacks-in-groupoids.md) have objects locally, isomorphisms on overlaps, and cocycle equations on triple overlaps. After taking nerves, those are families of one-types with descent. For higher stacks, the values can instead be general spaces or Kan complexes. An overlap comparison can have a homotopy between two choices; on a triple overlap there can be a homotopy between composites; that homotopy has its own compatibility on quadruple overlaps, and so on.

One way to organize the necessary local data is a *hypercover*. We describe its matching conditions precisely. Let \(U\in\mathcal C\), let \(h_U\) be its representable presheaf, and let \(U_\bullet\to h_U\) be an augmented simplicial presheaf, with each \(U_n\) a coproduct of representables. Write \(t_{n-1}\) for truncation and take coskeleton in the category of simplicial presheaves over \(h_U\). The relative matching object is
\[
M_n=\bigl(\operatorname{cosk}^{h_U}_{n-1}t_{n-1}U_\bullet\bigr)_n,
\qquad M_0=h_U.
\tag{6.1}
\]
Its sections are the compatible boundary data forced by earlier degrees. The convention in degree zero means there are no earlier data except the augmentation. A hypercover requires every matching map \(U_n\to M_n\) to be locally surjective: every section over a site object has lifts after a covering of that object. This formulation does not require the representable presheaves themselves to be sheaves.

The first three conditions can be read without any higher terminology:

| Degree | Matching data | Hypercover requirement |
|---|---|---|
| \(0\) | A section of \(h_U\) | \(U_0\to h_U\) is a covering map of presheaves. |
| \(1\) | Two vertices over the same section of \(h_U\) | \(U_1\to U_0\times_{h_U}U_0\) is locally surjective. |
| \(2\) | Three edges whose endpoints form the same three vertices | \(U_2\) locally supplies a triangle over every compatible boundary. |

In the last row, an edge on \(01\), one on \(12\), and one on \(02\) must have matching endpoints. There is no already defined composition on the presheaf \(U_1\) whose equality is being imposed. The triangle is new degree-two data above that boundary. Its degeneracies and faces must obey the simplicial identities because \(U_\bullet\) is a simplicial object. In subsequent degrees (6.1) similarly asks for local lifts of every compatible boundary assembled from the earlier data.

For an ordinary cover \(U_0\to h_U\), its Čech nerve has degree \(n\) equal to the \((n+1)\)-fold fibre product of \(U_0\) over \(h_U\). Its positive matching maps are isomorphisms: after choosing the vertices, its higher simplices are forced. A hypercover permits further covers of matching objects, and thereby allows additional local refinements in higher degrees. When the site has the usual representable fibre products, this Čech nerve is an example with coproducts of representables as above.

If \(F:\mathcal C^{\mathrm{op}}\to\mathrm{Kan}\), its value on a coproduct \(U_n=\coprod_i h_{V_{n,i}}\) is the product \(\prod_iF(V_{n,i})\). Equivalently it is the simplicial set of presheaf maps from \(U_n\) into the degreewise set-valued presheaves underlying \(F\); Yoneda identifies this with that product. Faces and degeneracies induce a cosimplicial diagram. The hyperdescent requirement is that the natural map
\[
F(U)\longrightarrow\operatorname{holim}_{[n]\in\Delta}F(U_n)
\tag{6.2}
\]
be a weak equivalence for every hypercover. Here \(\operatorname{holim}\) is the derived, or homotopy, limit; it retains compatibility homotopies and their higher coherences, instead of only demanding equalities in an ordinary limit. We state (6.2) as the condition being sought, not as a theorem asserting that every objectwise Kan presheaf satisfies it.

This extends the distinction already seen for groupoids. Having invertible arrows, or having Kan values, addresses the local homotopy type of each value. Descent addresses how those values glue along covers. Hyperdescent asks for the stronger gluing condition along all the higher matching refinements. Some usages of higher stack require this last condition, while others distinguish stacks from hypercomplete stacks; (6.2) specifies the convention whenever that stronger claim is made here.

### 6.3. Returning to algebraic geometry

The algebraic stacks studied in earlier lessons have geometric conditions in addition to descent: representability conditions on their diagonals, a topology for covers, and atlases with the specified smooth or étale properties. Taking their nerves explains their homotopy one-type values, but does not supply an atlas automatically. A higher-stack theory must specify its geometric conditions as well as its homotopy model and its descent convention.

Grothendieck's programme therefore asks several connected questions: which weak higher groupoids represent homotopy types, which combinatorial models permit local and relative constructions, and how those models support coherent descent on sites. Test categories answer a modelizing part of that question. Theorem 4.2 shows that simplices work both globally and locally, and Proposition 5.1 gives the resulting localization comparison. The broader construction of higher stacks, their geometric representability theory and the later derived-algebraic-geometry developments remain further topics. No theorem about all of them follows merely from declaring a presheaf category to be a modelizer.

## 7. Exercises and complete solutions

### Exercise 7.1 — easy

Show that the nerve of a category with a final object is contractible.

**Solution.** Let \(c\) be final in \(C\). For each \(a\), let \(\theta_a:a\to c\) be the unique arrow. If \(f:a\to b\), both \(\theta_bf\) and \(\theta_a\) are arrows from \(a\) to \(c\), so are equal. Thus \(\theta\) is a natural transformation from the identity functor to the constant functor at \(c\).

Define \(C\times[1]\to C\) by sending \((a,0)\) to \(a\), \((a,1)\) to \(c\), arrows at height zero to themselves, arrows at height one to \(\mathrm{id}_c\), and every mixed arrow to the unique arrow into \(c\). Composition is respected by the uniqueness just proved. Its nerve is a map \(N(C)\times\Delta[1]\to N(C)\) whose endpoints are the identity and the constant vertex \(c\). The prism triangulation in Section 1.2 realizes it as a continuous homotopy. This contracts the whole nerve realization, including every component and every positive homotopy group, to \(c\).

### Exercise 7.2 — medium

Show that the category of elements of \(\Delta[n]\) has a final object.

**Solution.** An element is a pair \(([m],\alpha:[m]\to[n])\). Its arrow to \(([\ell],\beta)\) is an ordinal map \(\gamma:[m]\to[\ell]\) with \(\alpha=\beta\gamma\). This is exactly the category \(\Delta/[n]\), including its degeneracies as arrows. The object \(([n],\mathrm{id}_{[n]})\) is final: the unique possible arrow to it is \(\alpha\), and that arrow always satisfies the required equality. Exercise 7.1 therefore proves that the category of elements has contractible nerve. For \(n=0\), this category is \(\Delta\), with final object \([0]\).

### Exercise 7.3 — medium

Show that a natural transformation \(u\Rightarrow v\) gives a simplicial homotopy between their nerves, and deduce that an adjunction induces a homotopy equivalence of nerves.

**Solution.** For \(\theta:u\Rightarrow v\), define \(H:A\times[1]\to B\) with the endpoint object values \(u(a),v(a)\). On a mixed arrow arising from \(f:a\to a'\), use
\[
v(f)\theta_a=\theta_{a'}u(f).
\tag{7.1}
\]
Naturality gives this equality. If a composable pair has a mixed arrow, its two images compose to the same mixed-arrow formula for the composite, again by (7.1); if it has no mixed arrow, functoriality of \(u\) or \(v\) gives the result. There cannot be a composable pair changing back from height one to zero. These cases verify every possible composition and the identity laws.

In each degree, \(N(A\times[1])=N(A)\times N([1])\), because a functor into a product is a pair of functors. Since \(N([1])=\Delta[1]\), the nerve of \(H\) is the required simplicial homotopy. For an adjunction \(L\dashv R\), apply this construction to its unit \(\mathrm{id}_A\Rightarrow RL\) and counit \(LR\Rightarrow\mathrm{id}_B\). After realization, these are homotopies between the two composites of \(|N(L)|,|N(R)|\) and the respective identities. They are therefore homotopy inverse maps. The conclusion concerns nerves; the functors themselves may fail to be equivalences of categories.

### Exercise 7.4 — hard

Prove that \(\Delta\) is a local test category. The conclusion must hold for every slice \(\Delta/[n]\), with the right-adjoint convention (2.3).

**Solution.** Fix arbitrary \(n\geq0\), put \(B=\Delta/[n]\), and let \(C\) have a final object \(c\). We prove the terminal-category criterion for \(B\).

First, \(j_\Delta C\) has the simplicial contraction (4.5). A simplex in its interval coordinate is \(t:[m]\to[1]\); at an object \(\beta:[p]\to[m]\), use \(F(\beta)\) before the value \(t(\beta(p))\) becomes one and \(c\) afterwards. Along a slice arrow last vertices can only increase, so the cases on arrows are an arrow of \(F\), the unique arrow into \(c\), or an identity. These compose and commute with every simplicial restriction, as (4.2) verifies. The endpoints are the identity and the constant functor.

To translate this contraction into element-category asphericity, use Lemma 3.2. Its product projection with \(\Delta[1]\) is weak: its comma category over \((m,x)\) is \(i_\Delta(\Delta[m]\times\Delta[1])\). The latter is the string element category of \([m]\times[1]\), and the append-final-object construction of Lemma 3.1 makes its map to that final-object category weak. Thus the comma categories are aspherical and Quillen A applies. Endpoint sections are weak by two-out-of-three, so homotopic maps are simultaneously weak by Lemma 3.3. In particular the constant self-map of \(j_\Delta C\) is weak. Factoring it through \(\Delta[0]\), whose element category has final \([0]\), forces one component and zero positive groups. Hence \(i_\Delta j_\Delta C\) is aspherical.

Next, a presheaf on \(B\) gives a simplicial set over \(\Delta[n]\) by taking the degreewise coproduct of its fibres over the maps \([m]\to[n]\). Its element category is exactly the element category of that total simplicial set. For \(b=([m],\alpha)\), an arrow into \(b\) is determined by its underlying map into \([m]\), so \(B/b\cong\Delta/[m]\). Therefore the presheaf \(j_BC\) corresponds exactly to \(j_\Delta C\times\Delta[n]\to\Delta[n]\). There is an isomorphism
\[
i_Bj_BC\cong i_\Delta(j_\Delta C\times\Delta[n]).
\tag{7.2}
\]
Lemma 3.2 with this \(n\) makes the projection of the right side to \(i_\Delta j_\Delta C\) weak. Its comma category is again the element category of \(\Delta[m]\times\Delta[n]\), a product nerve of a category with final \((m,n)\); hence the lemma applies for every degree. Its aspherical target proves that (7.2) is aspherical.

Finally, for arbitrary \(D\) and \(d\in D\), the comma category of \(\varepsilon_D:i_Bj_BD\to D\) over \(d\) is \(i_Bj_B(D/d)\), by (2.8). The category \(D/d\) has final object \(\mathrm{id}_d\), so the preceding argument makes every such comma category aspherical. Quillen A proves \(\varepsilon_D\) weak. For empty \(D\), it is the empty identity. Thus \(B\) is weak test. Since \(n\) was arbitrary, every \(\Delta/[n]\) is weak test, which is precisely the local-test condition on \(\Delta\). Combined with the separately proved weak-test condition in Proposition 4.1, it proves the assigned test-category theorem.

## 8. Prerequisites and sources

The owned proof of the assigned theorem is Theorem 4.2. Proposition 2.1 proves the elements adjunction; Proposition 2.2 proves the weak-test criterion. Lemmas 3.1–3.3 supply the noncircular comparison and homotopy arguments; Proposition 4.1 supplies the interval contraction; (4.6)–(4.10) identify every slice and its right adjoint. Proposition 4.3 proves the additional product claim and its slice counterexamples. Proposition 5.1 proves the modelizer comparison and saturation using the specified ordinary CW input. Every assigned exercise has a complete solution.

The exact primary edition is [Grothendieck, Pursuing Stacks, arXiv:2111.01000v2](https://arxiv.org/abs/2111.01000v2), 21 November 2021, shown there under CC0. Locators use its printed page numbers: Sections 28–29, pages 70–75, for modelizers and the adjunction; Sections 30–31, pages 76–80, for asphericity and intervals; Section 44(a)–(c), pages 111–116, for the settled weak/local/test/strict conventions and examples; Sections 2–3, pages 2–5, for the homotopy hypothesis and the coherence problem. These are source-grounded explanations, not historical quotation panels. In Section 44(a), criterion (v) the intended composite is \(i_Aj_A(C)=A/j_A(C)\); the printed \(j_Ai_A(C)\) in that spot is ill-typed under the source's own definitions. We use the well-typed composite (2.7).

Section 1.1 proves Quillen's Theorem A by the two-chain bisimplicial construction and the realization lemma. Section 5.3 proves last-vertex weak equivalence using the contractible undercategories of each simplex; no nondegeneracy restriction is imposed. The existing CW Whitehead provider in *Homotopy fibres and the Serre spectral sequence*, Section B, supplies both the realization lemma's CW gluing input and saturation, with the componentwise extension written in Section 5.1. Its immediate topological foundations are *Grassmannians and classifying maps*, Section 7, for compact subsets and quotient products; *Frame fields and primary obstructions*, Section E, for homotopy extension; and *Thom spaces and the Pontryagin–Thom construction*, Section B, for cellular approximation. All these are actually written lessons in the differential-geometric foundations course. Section 5.3 now also proves the arbitrary-space singular-realization counit. It writes out the restricted face-category comparison, finite sphere approximation, shelling and horn normalization, the singular face-group comparison and all basepoint transports. The horn and fibre foundations are proved in Lesson 11, §5.3. No injectivity assertion for a general Kan complex's realization map is silently used: its proved surjectivity and the singular face-group isomorphism give the counit result directly. This comparison is not needed for the test-category theorem.

[Stacks, Tag 0162](https://stacks.math.columbia.edu/tag/0162), the Simplicial Methods chapter, is background; the precise simplicial definitions used here were developed in Lesson 11. Maltsiniotis, La théorie de l'homotopie de Grothendieck, Astérisque 301, and Cisinski, Les préfaisceaux comme modèles des types d'homotopie, Astérisque 308, are named further references. We do not import a proof from them into this lesson. The general weak higher-groupoid hypothesis, higher-stack constructions and hyperdescent theorems are described as further work, not claimed as proved. Self-checked by the writing AI.
