# K-injective resolutions in Grothendieck abelian categories

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original text: public domain (CC0). Authorship and sources are listed in the [course notice](../LICENCE.md).*

A bounded-below resolution has a first degree. For an unbounded complex, starting farther and farther to the left does not by itself produce a compatible resolution. The solution developed here is to enforce the desired extension and homotopy properties on a set of small tests, then take a sufficiently long increasing union. The size estimates ensure that every test into the union appeared at an earlier stage where the construction dealt with it.

Read [Sheaves of modules on a ringed space](sheaves-of-modules-on-a-ringed-space.md), Theorems 2.1 and 3.1 and Lemmas 5.1–5.2; [Injective modules and bounded-below derived functors](injective-modules-and-bounded-below-derived-functors.md), Section 3 and Theorem 4.1; and [Complexes, cones and localization](complexes-cones-and-localization.md), Theorems 3.1, 4.2 and 5.1. Those readings supply abelian categories, exact filtered colimits of module sheaves, Hom complexes, cones, localization, and the comparison theorem for K-injectives. We use sets and choice in a fixed universe. A larger universe temporarily accommodates localization; this lesson proves that its Hom sets lie in the original universe.

The construction follows the Stacks project authors’ *Injectives*, sections on Grothendieck categories and K-injective complexes, and *Derived Categories*, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). The chapter credits Christian Serpé and the relation to Nicolas Spaltenstein’s *Resolutions of unbounded complexes*. The size bounds and transfinite construction are developed below before their derived-functor applications. Source attribution appears in the [course notice](../LICENCE.md).
## 1. The Grothendieck hypotheses

An abelian category has **AB3** if it has all small coproducts, **AB4** if those coproducts are exact, and **AB5** if it has coproducts and exact filtered colimits. The starred conditions refer respectively to products, exact products, and exact cofiltered limits. A **generator** \(U\) means that \(\operatorname{Hom}(U,-)\) is faithful: distinct morphisms become distinct after precomposition with some map from \(U\). A locally small abelian category satisfying AB5 and having a generator is a **Grothendieck abelian category**. “Locally small” means that each Hom collection is a set in the chosen universe.

AB3 gives every small colimit. For a diagram \((A_i)\), take the cokernel of the map from the sum over its arrows to the sum over its objects, whose component for \(i\to j\) is the inclusion at \(i\) minus the diagram map followed by the inclusion at \(j\). Maps out of this cokernel are exactly compatible families of maps out of the diagram, which proves its universal property. AB5 implies AB4: a coproduct of short exact sequences is the filtered colimit of the exact finite subsums. Exact filtered colimits also commute with cohomology, since they preserve the kernels and cokernels defining it. These facts will be used at successor and limit stages.

In an abelian category with coproducts the generator condition has two useful equivalent forms. Every proper subobject \(N\subsetneq M\) is escaped by some map \(U\to M\); and every object is a quotient of a coproduct of copies of \(U\). Faithfulness implies the first form by applying it to the nonzero quotient map \(M\to M/N\). That form implies the second: sum all maps from \(U\) into \(M\); their image cannot be proper. The second implies faithfulness: if a morphism is nonzero, an epimorphism from a coproduct of copies of \(U\) cannot kill it on every summand. We use all three forms without assuming that \(U\) is projective.

**Proposition 1.1 (a generator).** Let \(\mathcal O\) be any sheaf of rings on \(X\), and \(G=\bigoplus_{U}j_{U!}\mathcal O_U\), the sum over all open sets \(U\). Then:

- (a) for every subsheaf \(N\subsetneq M\) there is a morphism \(G\to M\) that does not factor through \(N\);
- (b) \(\operatorname{Hom}_{\mathcal O}(G,-)\) is faithful: a nonzero morphism \(M\to M'\) stays nonzero after composing with some \(G\to M\);
- (c) every \(M\) receives an epimorphism from a direct sum of copies of \(G\).

Together with Theorem 3.1 of the first lesson, which gives all colimits and exact filtered colimits, this makes \(\operatorname{Mod}(\mathcal O)\) a Grothendieck abelian category as defined above.

*Reference:* [AI Integrated Stacks Project, unbounded complexes](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex#L6992) states this generator for commutative \(\mathcal O\).

**Proof.** A section \(s\in M(U)\) gives \(e_s:j_{U!}\mathcal O_U\to M\) with \(e_s(1)=s\) (Lemma 5.1 of the first lesson). Composing with the projection \(G\to j_{U!}\mathcal O_U\) gives \(\tilde e_s:G\to M\). (a) A subobject of \(M\) in \(\operatorname{Mod}(\mathcal O)\) is a subsheaf, since kernels are computed on sections. If \(N\neq M\), there are \(U\) and \(s\in M(U)\setminus N(U)\). If \(\tilde e_s\) factored through \(N\), then \(s=e_s(1)\) would lie in \(N(U)\). (b) If \(\varphi:M\to M'\) is nonzero, then \(\varphi(s)\neq0\) for some section \(s\in M(U)\). So \(\varphi\circ\tilde e_s\neq0\): on the summand \(j_{U!}\mathcal O_U\) it sends \(1\) to \(\varphi(s)\). (c) The sum of all \(\tilde e_s\), over all pairs \((U,s)\), is a morphism \(\bigoplus_{(U,s)}G\to M\) whose image contains every section. So it is onto on stalks, hence an epimorphism. \(\square\)

The three forms of generator are equivalent by the argument preceding the proposition.

## 2. Sizes and functorial injective embeddings

In the bounded-below case there was a first degree from which to construct a homotopy. An unbounded complex has no such starting point. Instead we will arrange that every map from an acyclic complex is null-homotopic. There are too many acyclic complexes to attach them all at once. The first part of the proof reduces the tests to a set of small complexes; the second kills those tests and makes the final terms injective.

For the construction let \(\mathcal A\) be any locally small Grothendieck abelian category: it has small coproducts, exact filtered colimits, and a generator \(U\). Here “generator” means that \(\operatorname{Hom}(U,-)\) detects distinct morphisms. Proposition 1.1 and Theorem 3.1 of the first lesson give these properties for our module sheaves. Sets, well-orderings and the axiom of choice are understood in the fixed universe. The argument uses elementary abelian-category kernels, images, quotients and pushouts, but not the construction of the derived category.

We use two consequences of the filtered-colimit axiom. Coproducts are exact: a coproduct is the filtered colimit of its finite subsums, and finite direct sums are exact. Also filtered colimits commute with cohomology of complexes: exactness preserves kernels and cokernels in the formula for cohomology. Thus a filtered union of acyclic complexes is acyclic, and a filtered composite of monic quasi-isomorphisms is a monic quasi-isomorphism.

### Size bounds and maps into increasing unions

**Lemma 2.1 (a set of subobjects and bounded representatives).** For every object \(B\), its subobjects form a set. Write \(s(B)\) for the cardinality of this set. A subobject or quotient of \(B\) has size at most \(s(B)\). For each infinite cardinal \(\mu\), there is a set of representatives of the isomorphism classes of objects with \(s(B)\leq\mu\).

*Proof.* Associate to a subobject \(V\subset B\) the subset of \(\operatorname{Hom}(U,B)\) consisting of maps that factor through \(V\). This subset determines \(V\): the images of all maps \(U\to V\) fill \(V\). Indeed, if their sum had a proper image \(W\subsetneq V\), the nonzero quotient map \(V\to V/W\) would, by the generator property, have nonzero composite with some map \(U\to V\), a contradiction. Hence subobjects inject into a power set of a Hom set.

Subobjects of a subobject remain subobjects of \(B\). Subobjects of a quotient correspond, by inverse image, to subobjects of \(B\) containing its kernel. This proves the size inequalities.

For each proper subobject \(V\subsetneq B\), choose a map \(a_V:U\to B\) not factoring through \(V\). Such a map exists by applying the generator property to \(B\to B/V\). The sum of these maps is onto: a proper image would be one of the subobjects the chosen maps were required to escape. There are at most \(s(B)\) summands. Therefore, if \(s(B)\leq\mu\), \(B\) is a quotient of \(U^{(\mu)}\), after adding zero summands if necessary. Its isomorphism class is represented by the quotient by one of the set of subobjects of \(U^{(\mu)}\). This proves the last assertion. \(\square\)

**Lemma 2.2 (smallness for monic systems).** Suppose that \((B_\beta)_{\beta<\lambda}\) is an increasing ordinal-indexed system of subobjects with union \(B\), and \(\operatorname{cf}(\lambda)>s(A)\). Every map \(A\to B\) factors through some \(B_\beta\).

*Proof.* The inverse images \(A_\beta=A\times_B B_\beta\) form an increasing family of subobjects of \(A\), with union \(A\). To see the last equality without using elements, take filtered colimits of the kernel diagrams for
\[
A\oplus B_\beta\longrightarrow B,\qquad (a,b)\longmapsto f(a)-b.
\]
Exactness identifies the resulting kernel with \(A\times_B B=A\). At most \(s(A)\) distinct subobjects occur among the \(A_\beta\). Choose an index for each distinct one. The cofinality assumption bounds all those indices by a single \(\gamma<\lambda\), so \(A_\gamma\) contains every \(A_\beta\), and is \(A\). The pullback property gives the required factorization. \(\square\)

**Cardinal bound under choice.** For every infinite cardinal \(\mu\), one has \(|\mu\times\mu|=\mu\). Consequently a union of at most \(\mu\) sets, each of cardinality at most \(\mu\), has cardinality at most \(\mu\).

**Proof.** Identify cardinals with their initial ordinals, using choice. Every infinite initial ordinal is a limit ordinal. To prove this elementary fact, for any infinite ordinal \(\gamma\) define a bijection \(\gamma+1\to\gamma\) by sending the added top element \(\gamma\) to \(0\), sending each finite ordinal \(n\) to \(n+1\), and fixing every ordinal \(\alpha\) with \(\omega\leq\alpha<\gamma\). Thus a successor of an infinite ordinal cannot be the first ordinal of its cardinality. We now prove the pair bound by induction on infinite cardinals. Well-order the pairs \((\alpha,\beta)\in\mu\times\mu\) by the lexicographic order of
\[
\bigl(\max(\alpha,\beta),\alpha,\beta\bigr).
\]
This is a well-order: any nonempty collection of pairs has a least maximum, then a least first coordinate among pairs with that maximum, and then a least second coordinate. Every predecessor of a pair with maximum \(\gamma\) lies in \((\gamma+1)\times(\gamma+1)\). The cardinal \(\nu=|\gamma+1|\) is smaller than \(\mu\). If \(\nu\) is finite, this square is finite; if it is infinite, its cardinality is \(\nu\) by the induction hypothesis. Thus every proper initial segment of the pair order has cardinality smaller than \(\mu\). This also starts the induction at \(\mu=\aleph_0\), where all such squares are finite. If the order type were greater than the ordinal \(\mu\), the pair in position \(\mu\) would have \(\mu\) predecessors, a contradiction. Its order type is therefore at most \(\mu\). The injection \(\alpha\mapsto(\alpha,0)\) gives the reverse cardinal inequality, proving equality.

For the union assertion, well-order its index set \(J\), choose an injection \(J\to\mu\), and, by choice, choose injections of the indexed sets into \(\mu\). Their disjoint union injects into \(\mu\times\mu\). The ordinary union injects into that disjoint union by assigning each element to the least index at which it occurs. The pair bound proves the assertion. \(\square\)

Recall that the cofinality of a limit ordinal is the least cardinality of an unbounded subset of it. We will always choose a limit ordinal with cofinality larger than a specified infinite cardinal \(\mu\); one may take the initial ordinal of \(\mu^+\), which is a limit by the first paragraph of the proof above. Indeed, each ordinal below \(\mu^+\) has cardinality at most \(\mu\). The cardinal bound just proved shows that the union of a family of at most \(\mu\) such ordinals has cardinality at most \(\mu\). This union, which is their supremum, is therefore strictly below the initial ordinal of \(\mu^+\), so the family is bounded. It follows that the cofinality is greater than \(\mu\). In particular, countably many factorization stages below our chosen ordinal have a common upper bound whenever \(\mu\geq\aleph_0\).

### Enough injectives, with a functorial choice

**Lemma 2.3 (the generator extension test).** An object \(E\) is injective if and only if every map \(V\to E\), where \(V\subset U\), extends to \(U\).

*Proof.* Necessity is the definition of injectivity. Conversely, take a monomorphism \(A\subset B\) and a map \(A\to E\). Order its extensions to subobjects of \(B\) by restriction. This is a set by Lemma 2.1 and local smallness. The union of a chain, with the compatible map to \(E\), is an upper bound, so Zorn's lemma gives a maximal extension \(a:A'\to E\).

If \(A'\neq B\), the nonzero quotient \(B\to B/A'\) has nonzero composite with some \(\psi:U\to B\). Put \(V=\psi^{-1}(A')\). The map \(a\psi:V\to E\) extends to \(b:U\to E\) by assumption. It vanishes on \(\ker\psi\), since its restriction there is \(a\psi=0\), so it descends to \(\operatorname{im}\psi\). This descended map and \(a\) agree on \(A'\cap\operatorname{im}\psi\). They therefore give a map \(A'+\operatorname{im}\psi\to E\), strictly extending \(a\), a contradiction. Thus \(A'=B\). \(\square\)

**Theorem 2.4 (functorial injective embeddings).** Every object \(M\) has a natural monomorphism into an injective object \(E(M)\).

**Proof.** For an object \(M\), form the pushout
\[
\begin{array}{ccc}
\displaystyle\bigoplus_{(V,a)}V&\longrightarrow&M\\
\big\downarrow&&\big\downarrow\\
\displaystyle\bigoplus_{(V,a)}U&\longrightarrow&\mathcal E(M),
\end{array}
\qquad
(V,a):\ V\subset U,\quad a:V\to M .
\tag{2.1}
\]
This is a set-indexed coproduct by Lemma 2.1. The left arrow is monic because coproducts are exact; its pushout \(M\to\mathcal E(M)\) is monic. Every selected map \(V\to M\) extends to \(U\to\mathcal E(M)\). A map \(M\to M'\) takes the summand labelled \((V,a)\) to the summand labelled by its composite, so \(\mathcal E\) and the embedding are functorial.

Iterate \(\mathcal E\), taking unions at limit stages. Choose a fixed \(\lambda_0\) with \(\operatorname{cf}(\lambda_0)>s(U)\), and call the union \(E(M)\). Given \(V\subset U\) and a map \(V\to E(M)\), Lemma 2.2 makes it factor through a stage before \(\lambda_0\), since \(s(V)\leq s(U)\). At the next stage (2.1) extends it to \(U\). Lemma 2.3 now proves that \(E(M)\) is injective. We have constructed functorial monomorphisms \(M\to E(M)\). The functor \(E\) need not be additive; no subsequent argument assumes that it is. \(\square\)

## 3. Testing on a set of acyclic complexes

**Lemma 3.1 (bounded small lifts).** There is an infinite cardinal \(\kappa\), depending only on \(\mathcal A\) and \(U\), such that every nonzero acyclic complex contains a nonzero bounded-above acyclic subcomplex all of whose terms have size at most \(\kappa\).

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

Choose a set \(\mathscr S\) of representatives of all bounded-above acyclic complexes with term sizes at most \(\kappa\). Such a set exists: Lemma 2.1 supplies a set of choices for each term, and local smallness supplies a set of differentials between each pair of choices; there are only countably many degrees. Restrict that set of complexes to the ones satisfying \(d^2=0\), acyclicity and boundedness above.

**Lemma 3.2 (testing K-injectivity on a set).** Suppose that every term of \(I^\bullet\) is injective and every chain map \(S^\bullet\to I^\bullet\), for \(S^\bullet\in\mathscr S\), is null-homotopic. Then \(I^\bullet\) is K-injective.

*Proof.* Take an acyclic \(A^\bullet\). Starting with \(F_0=0\), build an increasing continuous filtration by acyclic subcomplexes. If \(F_\beta\neq A\), the quotient \(A/F_\beta\) is nonzero and acyclic. Choose in it a nonzero small acyclic subcomplex from Lemma 3.1, and let \(F_{\beta+1}\) be its inverse image. At a limit stage take the union. Successor exactness follows from the short exact sequence of complexes; limit exactness follows from exact filtered colimits. The construction exhausts \(A\): the subcomplexes of \(A\) form a set, since they are among the sequences of subobjects of its terms. A strictly increasing chain longer than that set is impossible. Every nonzero successor quotient \(F_{\beta+1}/F_\beta\) is isomorphic to an element of \(\mathscr S\).

Let \(f:A\to I\) be a chain map. We construct null-homotopies \(h_\beta\) of \(f|_{F_\beta}\) that agree on earlier stages. At a successor, extend each component \(h_\beta^n:F_\beta^n\to I^{n-1}\) to a map \(\widetilde h^n:F_{\beta+1}^n\to I^{n-1}\), using injectivity. The map
\[
g=f|_{F_{\beta+1}}-d_I\widetilde h-\widetilde h\,d_F
\]
is a chain map, as \(d_I^2=d_F^2=0\). It vanishes on \(F_\beta\), and so descends to a chain map \(\bar g:F_{\beta+1}/F_\beta\to I\). By the test assumption \(\bar g=d_I k+k d\) for a degree-minus-one map \(k\). With \(\pi:F_{\beta+1}\to F_{\beta+1}/F_\beta\), put \(h_{\beta+1}=\widetilde h+k\pi\). This extends \(h_\beta\) and satisfies \(f=d_Ih_{\beta+1}+h_{\beta+1}d_F\).

At a limit stage the compatible components define maps out of the union, and the same identity holds because it holds on every earlier stage. At exhaustion they give a null-homotopy of \(f\). Thus every map from every acyclic complex to \(I\) is null-homotopic, exactly the definition of K-injectivity. This proof does not pass cohomology through an inverse limit. \(\square\)

## 4. Constructing the unbounded resolution

**Theorem 4.1.** In a locally small Grothendieck abelian category, every complex \(M\) has a functorial, termwise monic quasi-isomorphism \(M\to I(M)\), where each term of \(I(M)\) is injective and \(I(M)\) is K-injective.

**Proof.**

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
\tag{4.1}
\]
Then \(M\to P(M)\) is termwise monic. Its quotient is the coproduct of the acyclic complexes \(S[1]\), hence is acyclic. It is therefore a quasi-isomorphism. Every chosen \(w\) becomes null-homotopic in \(P(M)\), using the corresponding cone. Indexing by all maps makes \(P\) and its embedding functorial.

The second operation uses the embeddings \(i_A:A\to E(A)\) constructed above. Set
\[
J(M)^n=E(M^n)\oplus E(M^{n+1}),\qquad
d_J(a,b)=(b,0),\qquad
u^n=(i_{M^n},\,i_{M^{n+1}}d_M).
\tag{4.2}
\]
The equation \(d_Ju=ud_M\) follows from \(d_M^2=0\), and \(u\) is monic because its first component is monic. Let \(Q=J(M)/u(M)\), with quotient map \(v:J(M)\to Q\), and define
\[
N(M)=\operatorname{Cone}(v)[-1],\qquad
N(M)^n=Q^{n-1}\oplus J(M)^n,
\]
\[
d_N(q,j)=(-d_Qq-v(j),d_Jj),\qquad
M\longrightarrow N(M),\quad m\longmapsto(0,u(m)).
\tag{4.3}
\]
These formulas are identities of component morphisms in the abelian category; they do not require objects to have underlying sets of elements. They show directly that the last map is a monic chain map. Its degree-\(n\) map factors through the injective subobject \(0\oplus J(M)^n\) of \(N(M)^n\). A finite direct sum of injectives is injective, since a map into it extends component by component.

The quotient \(N(M)/M\) has terms \(Q^{n-1}\oplus Q^n\), differential
\[
D(q,a)=(-dq-a,da),
\]
and contraction \(h(q,a)=(0,-q)\): substitution gives \(Dh+hD=1\). Thus \(M\to N(M)\) is a quasi-isomorphism. Naturality of \(i_A\) gives functoriality of every map in (4.2)–(4.3), even though \(E\) need not be additive.

The roles of the two operations are worth separating:
\[
\begin{gathered}
T_\beta\xrightarrow{\text{kill test maps}}P(T_\beta),\\
P(T_\beta)\xrightarrow{\text{insert injectives}}T_{\beta+1}.
\end{gathered}
\tag{4.4}
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

First, every term \(I(M)^n\) is injective. Given \(V\subset U\) and a map \(V\to I(M)^n\), smallness factors it through \(T_\beta(M)^n\) for some \(\beta<\lambda\). Its composite into \(T_{\beta+1}(M)^n\) factors through the injective object \(J(P(T_\beta(M)))^n\) by (4.3). Extend \(V\to J(P(T_\beta(M)))^n\) to \(U\), and compose into \(I(M)^n\). Lemma 2.3 proves injectivity. This is a proof about the final terms, not an assertion that filtered colimits of injectives are automatically injective.

Second, let \(S\in\mathscr S\) and \(w:S\to I(M)\) be a chain map. Every component factors through a stage by Lemma 2.2, since \(s(S^n)\leq\kappa\). There are countably many components. As \(\operatorname{cf}(\lambda)>\kappa\geq\aleph_0\), all components factor through a single \(T_\beta(M)\). They already commute with the differentials there: their commutators vanish after the monomorphism \(T_\beta(M)^{n+1}\to I(M)^{n+1}\), and hence vanish before it. Thus \(w\) factors as a chain map. Operation \(P\) makes that map null-homotopic at the next stage, so it is null-homotopic in \(I(M)\). Lemma 3.2 proves K-injectivity.

Apply this construction to \(\mathcal A=\operatorname{Mod}(\mathcal O)\). It proves the resolution assertion of Theorem 4.1, including termwise injectivity, naturality and noncommutative coefficients. The unbounded derived-functor consequences are proved in Section 5 below. The derived category was constructed in the common reading; the existence proof here only uses complexes and homotopies. \(\square\)


## 5. Derived functors, adjoints and products

Let \(Q:K(\mathcal A)\to D(\mathcal A)\) denote localization. By Theorem 3.3 of the preceding lesson, maps into a K-injective complex satisfy

\[
\operatorname{Hom}_{K}(K,I)=\operatorname{Hom}_{D}(QK,QI).
\tag{5.1}
\]

That theorem also proves that a quasi-isomorphism between K-injectives is a homotopy equivalence. We now use it without boundedness restrictions. Although the construction of \(I(M)\) is functorial on chain maps, its functor need not be additive. The additive functor on the derived category is obtained from (5.1), rather than by claiming additivity of the transfinite construction.

**Theorem 5.1 (right derived functors on all complexes).** Suppose every complex of an abelian category \(\mathcal A\) has a quasi-isomorphism \(q_K:K\to I_K\) into a K-injective complex. For every exact functor of triangulated categories \(F:K(\mathcal A)\to\mathcal T\), there is an exact right derived functor

\[
RF:D(\mathcal A)\longrightarrow\mathcal T,
\qquad RF(K)=F(I_K).
\]

Its comparison \(\eta:F\to RF\circ Q\) is initial among natural comparisons from \(F\) to a functor on \(D(\mathcal A)\). In particular, for any additive \(\Phi:\mathcal A\to\mathcal B\), with \(\mathcal B\) abelian, \(R\Phi:D(\mathcal A)\to D(\mathcal B)\) is computed by applying \(\Phi\) degreewise to a K-injective resolution.

**Proof.** The full subcategory \(K_{\mathrm{inj}}\subset K(\mathcal A)\) of K-injectives is closed under shifts and cones by Lemma 3.1 of the preceding lesson. Equation (5.1) shows that \(Q\) restricted to this subcategory is fully faithful, and the resolution hypothesis makes it essentially surjective. Define an inverse \(R\) explicitly: send \(K\) to \(I_K\), and a derived morphism \(v:QK\to QL\) to the unique homotopy class \(Rv:I_K\to I_L\) satisfying

\[
Q(Rv)=Q(q_L)\,v\,Q(q_K)^{-1}.
\tag{5.2}
\]

Existence and uniqueness follow from (5.1). The same formula proves preservation of identities, composition and addition. For an ordinary homotopy class \(f:K\to L\), injectivity of the map in (5.1) gives \((Rf)q_K=q_Lf\) already in \(K(\mathcal A)\).

The inverse \(R\) is exact. Its shift comparison is the unique isomorphism \(I_{K[1]}\cong I_K[1]\) inducing the corresponding isomorphism in \(D\). A morphism between K-injectives has a K-injective cone. For any distinguished triangle in \(D\), compare its first arrow with the unique arrow between the chosen K-injectives. The cone triangle of that arrow maps under \(Q\) to a distinguished triangle with the same first arrow. The triangle morphism axiom and the long exact representable sequences, proved in the common reading, supply an isomorphism on the third objects compatible with all arrows. Full faithfulness lifts this isomorphism and its equations to \(K_{\mathrm{inj}}\). Thus \(R\) transports distinguished triangles to distinguished triangles, with the stated shift comparison. Set \(RF=F\circ R\) and \(\eta_K=F(q_K)\); the equality just proved gives naturality.

To verify universality, take any functor \(T:D(\mathcal A)\to\mathcal T\) and natural \(\theta:F\to TQ\). Define

\[
\alpha_K=T(Qq_K)^{-1}\theta_{I_K}:
F(I_K)\longrightarrow T(QK).
\tag{5.3}
\]

Naturality of \(\theta\) for the representative \(Rv\), together with (5.2), proves naturality of \(\alpha\) for every derived morphism \(v\). Naturality for \(q_K\) gives \(\alpha_K\eta_K=\theta_K\). This factorization is unique: at a K-injective object \(I\), its resolution map \(q_I\) is a homotopy equivalence, so \(F(q_I)\) is invertible and forces \(\alpha_I\). Naturality for the isomorphism \(Qq_K\) then forces \(\alpha_K\). Consequently the displayed construction has exactly the right-derived universal property. It also proves independence of the chosen resolutions and comparisons.

Finally, an additive \(\Phi\) preserves chain homotopies, shifts, and finite direct sums, and carries the defining matrix of a cone to that of the cone of the image map. Composing its functor on homotopy categories with \(K(\mathcal B)\to D(\mathcal B)\) is therefore exact. Apply the result to this \(F\). On bounded-below cohomology it agrees with the preceding lesson: its bounded-below injective resolution is K-injective, and (5.1) uniquely compares it with any unbounded resolution. \(\square\)

For a Grothendieck category, (5.1) also settles the size of derived morphisms. \(\operatorname{Hom}_{K}(K,I_L)\) is the quotient of the set of chain maps by the set-valued homotopy relation; chain maps and homotopies are subsets of countable products of original-universe Hom sets. Thus \(D(\mathcal A)\) is locally small in the original universe, including when \(\mathcal A\) is a large category of sheaves.

**Proposition 5.2 (exact left adjoints).** Let \(u:\mathcal A\to\mathcal B\) be exact and left adjoint to an additive \(v:\mathcal B\to\mathcal A\). Then \(v\) preserves K-injectives.

**Proof.** The adjunction on objects identifies chain maps and their homotopies componentwise, hence

\[
\operatorname{Hom}_{K(\mathcal A)}(A,vI)
=\operatorname{Hom}_{K(\mathcal B)}(uA,I).
\]

If \(A\) is acyclic, exactness of \(u\) makes \(uA\) acyclic and K-injectivity makes the right side zero. This is the definition of K-injectivity of \(vI\). \(\square\)

In particular, restriction \(j^{-1}\) to an open subset preserves K-injectives because its left adjoint \(j_!\) is exact. For a continuous \(f:X\to Y\) with \(\mathcal O_X=f^{-1}\mathcal O_Y\), the exact left adjoint \(f^{-1}\) shows that \(f_*\) preserves K-injectives. For an arbitrary morphism of ringed spaces, \(Rf_*\) still exists by Theorems 4.1 and 5.1 applied to module sheaves; preservation by the underived \(f_*\) requires an exact left adjoint, for example flat module pullback. Section 6 gives a failure when pullback is not exact.

**Proposition 5.3 (existence of products in \(\mathcal A\)).** A locally small abelian category with a generator and small coproducts has all small products. In particular a Grothendieck category satisfies \(\mathrm{AB3}^{*}\).

**Proof.** Fix a family \((A_i)_{i\in J}\). For any cone \((f_i:T\to A_i)\), let \(N\subset T\) be the sum of all subobjects on which every \(f_i\) vanishes. This is a set of subobjects by Lemma 2.1, so its sum exists as the image of their coproduct. Each \(f_i\) vanishes on the sum. The induced family on \(B=T/N\) is **jointly monic**, meaning that a map killed by all its components is zero. Indeed, if a subobject of \(B\) is killed by every component, its inverse image in \(T\) would enlarge \(N\); hence it is zero. Apply this to the image of a map killed by the family. This constructs a jointly monic quotient of every cone, without using products or intersections to define it.

For a jointly monic cone on \(B\), the map of sets

\[
\operatorname{Hom}(U,B)\longrightarrow
\prod_{i\in J}\operatorname{Hom}(U,A_i)
\]

is injective: the difference of two maps with equal images is killed by every component. Let \(\nu\) be the cardinality of the product on the right and set \(\mu=\max(2^\nu,\aleph_0)\). The subobject-to-subset argument in Lemma 2.1 gives \(s(B)\le\mu\). That lemma supplies a set of representatives of all possible \(B\), and local smallness supplies a set of all their cones to \((A_i)\). Take the coproduct \(C\) of all these jointly monic cones, with the induced maps \(C\to A_i\), and divide by their common vanishing subobject as in the first paragraph. Call the result \(P\).

Every cone on \(T\) factors through its jointly monic quotient \(B\), through a representative included as a summand of \(C\), and then through \(P\). Thus a map \(T\to P\) inducing the given cone exists. It is unique because the cone on \(P\) is jointly monic. This is the universal property of \(\prod_i A_i\). The empty product is zero and the construction still works: its only jointly monic cone has zero source. \(\square\)

The proposition proves existence, not exactness, of products. Products of sheaves already existed in the first lesson, but their epimorphisms can fail to be onto on stalks.

**Proposition 5.4 (products and coproducts in the derived category).** A Grothendieck category has all small derived products and coproducts. A coproduct is represented by the termwise sum of any representatives. A product is represented by the termwise product of K-injective resolutions.

**Proof.** Put \(P=\prod_i I_i\) for K-injectives \(I_i\). Componentwise projections identify the complex of abelian groups \(\operatorname{Hom}^\bullet(A,P)\) with \(\prod_i\operatorname{Hom}^\bullet(A,I_i)\). Products of abelian groups are exact: kernels are coordinatewise and coordinatewise lifts prove surjectivity using choice. Therefore if \(A\) is acyclic, the product Hom complex is acyclic. Thus \(P\) is K-injective. For any \(K\), exactness of those group products and (5.1) give

\[
\operatorname{Hom}_{D}(K,P)
=\prod_i\operatorname{Hom}_{D}(K,I_i),
\]

which proves the product property. The proof assumes exact products in abelian groups, not in \(\mathcal A\).

For the sum \(S=\bigoplus_i K_i\), and any K-injective \(I\), the Hom complex identifies with \(\prod_i\operatorname{Hom}^\bullet(K_i,I)\). The same exactness gives \(\operatorname{Hom}_K(S,I)=\prod_i\operatorname{Hom}_K(K_i,I)\). Equation (5.1) and a K-injective resolution of every target prove the coproduct property in \(D\). AB4 ensures that changing representatives by quasi-isomorphisms changes their sum by a quasi-isomorphism. \(\square\)

### Finite cohomological dimension and acyclic models

**Proposition 5.5.** Let \(F:\mathcal A\to\mathcal B\) be an additive left-exact functor, with \(\mathcal A\) Grothendieck and \(\mathcal B\) abelian. Suppose \(R^qF(M)=0\) for all objects \(M\) and all \(q>d\), for one integer \(d\geq0\). Then every unbounded complex \(C\) whose terms are \(F\)-acyclic computes \(RF(C)\) by the termwise complex \(F(C)\). Here \(F\)-acyclic means \(R^qF(C^n)=0\) for \(q>0\). The bound must be uniform over all objects.

**Proof.** First let \(A\) be an acyclic complex of \(F\)-acyclic objects. Its cycle sequences are
\[
0\to Z^nA\to A^n\to Z^{n+1}A\to0.
\]
Their derived-functor long exact sequences give, for \(q\geq1\),
\[
R^qF(Z^{n+1}A)\simeq R^{q+1}F(Z^nA).
\]
Iterating \(d\) times yields
\(R^1F(Z^{n+1}A)\simeq R^{d+1}F(Z^{n+1-d}A)=0\).
For \(d=0\) this vanishing is the original hypothesis. Thus applying \(F\) to every cycle sequence leaves it short exact. The resulting images of consecutive differentials are exactly the kernels of the next differentials, so \(F(A)\) is acyclic.

Choose the monic, termwise-injective K-injective resolution \(C\hookrightarrow I\) of Theorem 4.1, and put \(Q=I/C\). It is acyclic. For every degree, the sequence \(0\to C^n\to I^n\to Q^n\to0\) and its long exact derived sequence show that \(Q^n\) is \(F\)-acyclic and that \(0\to F(C^n)\to F(I^n)\to F(Q^n)\to0\) is exact. The first part proves \(F(Q)\) acyclic. Therefore \(F(C)\to F(I)\) is a quasi-isomorphism. The latter complex computes \(RF(C)\) by Theorem 5.1. Its canonical comparison also proves naturality and independence of \(I\). \(\square\)

This is the right-derived version of the finite-dimensional acyclic-model argument in Joseph Lipman, [*Notes on Derived Functors and Grothendieck Duality*, §2.7, Proposition 2.7.5(a)](https://www.math.purdue.edu/~jlipman/Duality.pdf). It supplies a useful unbounded extension of the bounded-below acyclic-resolution criterion. Without the uniform finite-dimensional hypothesis, termwise acyclicity alone is insufficient justification.

A second useful consequence of Proposition 5.4 is that small coproducts of distinguished triangles are distinguished. Represent each triangle by a cone triangle, using the common reading's localization theorem. Taking the termwise direct sum commutes with the cone differential and with its negative final projection. AB4 preserves the quasi-isomorphisms that identify the original triangles with those representatives. The resulting sum is therefore a cone triangle in the derived category. This is the coproduct assertion discussed by Lipman in §3.8.

For the alternative resolution construction using finite higher-product dimension, continue with [Inverse limits and unbounded resolutions](inverse-limits-and-unbounded-resolutions.md). Its extra hypothesis concerns passage to the inverse limit; the exact-filtered-union existence proof in this lesson requires no such hypothesis.

## 6. Examples that isolate the hypotheses

**Unbounded termwise injectivity.** Over \(R=k[\epsilon]/(\epsilon^2)\), the complex with \(R\) in every integer degree and differential multiplication by \(\epsilon\) is acyclic, because \(\ker(\epsilon)=\epsilon R=\operatorname{im}(\epsilon)\). Its terms are injective: the only ideals are \(0,\epsilon R,R\), and a map \(\epsilon R\to R\) sends \(\epsilon\) to an element \(\epsilon a\), so it extends by sending \(1\) to \(a\); the Baer criterion was proved in the preceding lesson. Its identity is not null-homotopic, because each expression \(\epsilon h^n+h^{n+1}\epsilon\) has image in \(\epsilon R\) and cannot equal \(1_R\). Taking the acyclic complex itself as a source proves that it is not K-injective. Theorem 4.1 must change this complex, although its terms are already injective.

**Pushforward can lose K-injectivity.** Take one-point ringed spaces with ring map \(\mathbb Z\to\mathbb F_2\). The module pushforward is restriction of scalars. The complex \(\mathbb F_2[0]\) is K-injective over \(\mathbb F_2\): a linear map from a subspace extends after choosing a basis, so every vector space is injective, and the bounded-below lemma applies. Consider the acyclic complex of abelian groups

\[
A^\bullet=(\mathbb Z\xrightarrow{2}\mathbb Z
\xrightarrow{\mathrm{mod}\,2}\mathbb F_2),
\qquad\text{in degrees }0,1,2.
\]

The map \(A\to\mathbb F_2[0]\) that is reduction modulo two in degree zero and zero elsewhere is a chain map. A null-homotopy would imply \(\mathrm{mod}\,2=h^1\circ2\), impossible for a homomorphism \(h^1:\mathbb Z\to\mathbb F_2\). Thus the pushed-forward complex is not K-injective. Its left adjoint \(\mathbb F_2\otimes_{\mathbb Z}-\) is not exact, since it sends the injection \(2:\mathbb Z\to\mathbb Z\) to zero. This matches the hypothesis of Proposition 5.2 exactly.

**An unbounded derived product.** The injective group \(\mathbb Q/\mathbb Z\) placed in degree \(-m\) is \((\mathbb Q/\mathbb Z)[m]\). The product of these complexes for \(m\ge0\) has one copy of \(\mathbb Q/\mathbb Z\) in every nonpositive degree, zero elsewhere, and zero differential. Proposition 5.4 makes it K-injective and the product in \(D(\mathbb Z)\). It has nonzero cohomology in arbitrarily negative degrees, so it is not bounded below. This also shows why resolving only bounded-below targets would miss objects of the unbounded category.

## 7. Exercises with checked solutions

**Exercise 1 (easy: a concrete generator).** For a discrete finite space \(X\) with constant ring \(R\), identify the generator \(G\) of Proposition 1.1 and prove directly that it detects morphisms. Does the proposition require \(R\) to be commutative?

**Solution.** A sheaf of modules is a tuple \((M_x)_{x\in X}\), and \(j_{U!}\mathcal O_U\) has stalk \(R\) at points of \(U\) and zero elsewhere. Thus \(G_x=\bigoplus_{U\ni x}R\). If a tuple of maps has a nonzero component at \(x\), choose an element there with nonzero image. The summand belonging to the singleton \(\{x\}\) gives a map into the source tuple detecting that element. For a left module, \(R\to M_x\), \(a\mapsto am\), is left linear for every associative unital \(R\). No commutativity is used. The empty-space module category has only its zero object, and its zero generator is faithful there.

**Exercise 2 (medium: \(\mathrm{AB3}^{*}\) without \(\mathrm{AB4}^{*}\)).** Give the size bound that makes the product construction in Proposition 5.3 a set-sized construction. Explain why it proves no exactness statement about products of sheaves.

**Solution.** With \(H_i=\operatorname{Hom}(U,A_i)\), every jointly monic cone on \(B\) embeds \(\operatorname{Hom}(U,B)\) into the set \(\prod_i H_i\). A subobject of \(B\) is determined by the subset of maps from \(U\) that factor through it. Hence \(s(B)\le2^{|\prod_i H_i|}\), and Lemma 2.1 provides a set of representatives. For each representative, the cones form a subset of \(\prod_i\operatorname{Hom}(B,A_i)\), also a set. Their union is a set, so their coproduct is permitted by AB3. This argument concerns a universal property. It supplies no common open neighbourhood on which infinitely many stalkwise lifts exist. The product-of-epimorphisms counterexample in Section 6 of the first lesson therefore remains compatible with AB3*.

**Exercise 3 (medium: the unbounded direct image).** For an arbitrary morphism of ringed spaces, construct \(Rf_*\), explain its agreement with bounded-below \(Rf_*\), and say when \(f_*I\) can itself be used as a K-injective complex on the target.

**Solution.** The module categories are Grothendieck by Proposition 1.1 and the first lesson. Choose a K-injective resolution \(K\to I_K\) by Theorem 4.1. Define \(Rf_*K\) as \(f_*I_K\) in the target derived category, with morphisms obtained by applying \(f_*\) to the unique comparison homotopy classes. Additivity of \(f_*\) makes it preserve homotopies and cones, so Theorem 5.1 proves existence, exactness and uniqueness. A bounded-below injective resolution is K-injective and is uniquely homotopy equivalent to any chosen K-injective resolution of the same object, giving agreement. If the left adjoint \(f^*\) is exact, Proposition 5.2 proves that \(f_*I_K\) is K-injective on the target. The one-point example in Section 6 proves that this final claim cannot be made for arbitrary ring maps.

**Exercise 4 (hard: what a transfinite step does for groups).** Work in \(\operatorname{Mod}(\mathbb Z)\), with generator \(U=\mathbb Z\). For \(M=\mathbb Z[0]\), describe an explicit nonzero small acyclic complex that occurs among the tests, and write the contraction that kills any map from it in \(P(M)\). Then check the contraction of \(N(P(M))/P(M)\). Explain why a countable sequence of steps has not been shown sufficient.

**Solution.** The complex \(S=(\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb Z/2)\) in degrees \(0,1,2\) is bounded above and acyclic, with terms having at most countably many subobjects. After replacing it by its representative it belongs to \(\mathscr S\). Every selected chain map \(w:S\to M\) has an attached copy of \(C(S)\). If \(e:C(S)\to P(M)\) is its pushout map, then the degree-minus-one map \(a\mapsto e(0,a)\) satisfies \(dh+hd=jw\), because \(d(0,a)=(a,-da)\). For this particular \(M\), \(w^0:\mathbb Z\to\mathbb Z\) can be multiplication by any integer and the other components vanish; the same formula kills all these maps.

Put \(L=P(M)\), \(Q=J(L)/L\). In \(N(L)/L\), write a term as \((q,a)\in Q^{n-1}\oplus Q^n\). Its differential is \(D(q,a)=(-dq-a,da)\) and \(h(q,a)=(0,-q)\). Direct substitution gives \(Dh(q,a)=(q,-dq)\) and \(hD(q,a)=(0,dq+a)\), whose sum is \((q,a)\). Thus this quotient is contractible. Finally, a test has countably many components. Their first factorization stages could be unbounded in \(\omega\); no single finite stage would then contain the chain map. The chosen cofinality greater than \(\kappa\ge\aleph_0\) ensures a common stage and makes the next-step killing argument valid.

**Exercise 5 (hard: compatible homotopies at a limit).** In Lemma 3.2, explain why choosing an unrelated null-homotopy at each filtration stage is insufficient. Derive the successor correction that makes the chosen homotopies agree.

**Solution.** A map out of a union is induced by compatible maps on its subobjects. Unrelated null-homotopies need not restrict to one another, so they define no homotopy on the union. Suppose \(h_\beta\) has been fixed. Termwise injectivity extends it to an arbitrary graded map \(\widetilde h\) on \(F_{\beta+1}\). The error \(g=f-d\widetilde h-\widetilde h d\) is a chain map and restricts to zero on \(F_\beta\). It factors through \(\pi:F_{\beta+1}\to F_{\beta+1}/F_\beta\). This quotient is a small acyclic test, so its error map is \(dk+kd\). Define \(h_{\beta+1}=\widetilde h+k\pi\). Then \(dh_{\beta+1}+h_{\beta+1}d=f\), and its restriction is the prescribed \(h_\beta\), because \(\pi\) vanishes there. At a limit, the universal property of the colimit assembles these compatible components and their equations. This uses exact filtered colimits to keep the filtration acyclic, but no exact inverse-limit assertion.

The next lesson constructs K-flat resolutions by a different method. This theorem is not needed for their existence; the two resolution tools address different variables of derived operations.

Sources: the Stacks project authors, *Injectives*, [the complete pinned chapter](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/injectives.tex), especially the proofs corresponding to Tags 0E8N and 079C–079P; *Derived Categories*, [the pinned K-injective section](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex#L9967), for comparison, derived functors, products and exact adjoints. The elementary large-cofinality argument in Section 2 is also the proof of [Stacks, Tag 05N3, in the pinned AI Integrated edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/sets.tex#L217). N. Spaltenstein, *Resolutions of unbounded complexes*, Compositio Mathematica 65 (1988), 121–154, is [available from Numdam](https://www.numdam.org/item/CM_1988__65_2_121_0/). See the [course notice](../LICENCE.md).
