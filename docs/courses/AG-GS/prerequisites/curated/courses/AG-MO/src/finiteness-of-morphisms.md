# Finiteness of morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

An equation may involve finitely many variables without imposing finitely many relations. A scheme may admit small affine charts without admitting a finite cover by them. These are different sources of infinitude, and different properties of a morphism control them.

We distinguish finite type from finite presentation, explain how both can be tested on charts, and prove a useful criterion for a quasi-compact image to be closed. The final section connects finite type with closed points over a Jacobson base. We assume localization, polynomial rings, quasi-coherent sheaves, and the diagonal results of The diagonal and separated morphisms. For the last section we use the algebraic Jacobson theorem from The Nullstellensatz and Jacobson rings. Basic references are AI Integrated Stacks Project and Vakil's *The Rising Sea*, §8.3.

Throughout, rings are commutative with identity and schemes need not be Noetherian or separated. The adjective “finite” will later describe module-finite affine morphisms; “finite type” here concerns algebra generators.

## 1. Finite covers over the base

A morphism \(f:X\to S\) is **quasi-compact** if \(f^{-1}(V)\) is quasi-compact for every affine open \(V\subset S\). Equivalently, the inverse image of every quasi-compact open is quasi-compact: cover that open by finitely many affine opens and take inverse images.

**Proposition 1.1.** Quasi-compactness is local on the target and is preserved by composition and arbitrary base change. Every closed immersion is quasi-compact.

**Proof.** Suppose \(S\) has an affine open cover \(V_i\) with \(f^{-1}(V_i)\) quasi-compact. Let \(V\subset S\) be another affine open. Choose finitely many distinguished opens of \(V\) covering \(V\), each contained in some \(V_i\). Each such distinguished open \(D\) is an affine, hence quasi-compact, open subset of \(V_i\), so it has a finite cover by distinguished opens of \(V_i\) contained in \(D\). The inverse image of each of the latter opens is the nonvanishing locus of a global function on the quasi-compact scheme \(f^{-1}(V_i)\). That locus is quasi-compact: cover the scheme by finitely many affines, on each of which it is distinguished affine. Thus \(f^{-1}(D)\), and then \(f^{-1}(V)\), are finite unions of quasi-compact opens.

For composition \(X\to Y\to S\), the inverse image in \(Y\) of an affine base open is quasi-compact. Its inverse image in \(X\) is therefore quasi-compact by the equivalent definition. For base change, work over \(V=\operatorname{Spec}A\subset S\) and an affine \(V'=\operatorname{Spec}A'\to V\). A finite affine cover \(f^{-1}(V)=\bigcup U_j\) pulls back to the finite affine cover \(U_j\times_V V'\). Such \(V'\) cover any new base, and the target-local assertion completes the argument. Finally, the inverse image under a closed immersion of an affine is a quotient spectrum and is affine. \(\square\)

Being quasi-compact is a property of the morphism. It does not follow merely from quasi-compactness of both schemes. In the doubled infinite-variable scheme of the preceding lesson, inclusion of one affine chart has non-quasi-compact inverse image over the other affine chart.

**Theorem 1.2.** For a quasi-compact morphism \(f:X\to S\), its image is closed if and only if its image is stable under specialization.

**Proof.** A closed subset is stable under specialization, so only the converse requires proof. The question is local on \(S\). Replace \(S\) by an affine open \(\operatorname{Spec}A\); then \(X\) has a finite affine cover \(\operatorname{Spec}B_1,\ldots,\operatorname{Spec}B_r\). The closure of the image is the union of the closures of their images, because the union is finite.

For a ring map \(A\to B\), the closure of its spectrum image is \(V(\ker(A\to B))\). Indeed, if \(D(a)\) misses the image, then \(B_a=0\), which means some power of \(a\) maps to zero. This proves that the basic open sets missing the image are precisely those missing this closed set.

Let \(\mathfrak p\) be in the closure of the image of one \(\operatorname{Spec}B_j\). The localization \(B_j\otimes_A A_{\mathfrak p}\) is nonzero. Otherwise some \(s\notin\mathfrak p\) would map to zero in \(B_j\), contradicting \(\ker(A\to B_j)\subset\mathfrak p\). Choose a prime in this nonzero localization. Its contraction \(\mathfrak q\subset A\) lies in \(\mathfrak p\) and belongs to the original image. Thus every point in the closure specializes from an image point. Specialization stability puts \(\mathfrak p\) itself in the image. The image equals its closure. \(\square\)

This proves a statement about the image of \(X\). A morphism is a closed map only when the same condition holds for the images of *all* closed subsets. Theorem 1.2 does not identify these two assertions.

## 2. Variables, equations and localization

An \(A\)-algebra \(B\) is **of finite type** if it has finitely many algebra generators, and **of finite presentation** if

\[
B\cong A[T_1,\ldots,T_n]/(F_1,\ldots,F_m)
\]

for finite \(n,m\). These conditions are independent of the chosen finite generating set. For finite presentation, here is a useful explicit argument. If \(b_1,\ldots,b_r\) are another set of generators, express each old generator as a polynomial \(G_i(b)\), and each \(b_j\) as a polynomial \(H_j(T)\). A presentation using the \(b_j\) has relations \(F_l(G)\) and \(b_j-H_j(G)\). Substituting proves that its quotient is \(B\), and there are finitely many relations.

Inverting one element preserves both conditions. If \(b\in B\), adjoining \(Z\) with relation \(bZ-1\) presents \(B_b\). Base change also preserves both: tensor the displayed presentation with a new base ring. Composition preserves both by adjoining the generators at the two stages; for finite presentation substitute the expressions for the intermediate algebra's generators into the second stage's relations.

The following patching fact is the reason charts suffice.

**Lemma 2.1.** Let \(b_1,\ldots,b_r\) generate the unit ideal of an \(A\)-algebra \(B\). If every \(B_{b_i}\) is of finite type over \(A\), then so is \(B\). If every \(B_{b_i}\) is of finite presentation over \(A\), then so is \(B\).

**Proof.** Choose finite algebra generators of each localization, expressed as fractions with numerators in \(B\). Let \(B_0\subset B\) be the \(A\)-subalgebra generated by all these numerators, the \(b_i\), and coefficients \(e_i\) in a relation \(1=\sum e_i b_i\). Then \((B_0)_{b_i}=B_{b_i}\). For any \(b\in B\), localization gives positive integers \(N_i\) with \(b_i^{N_i}b\in B_0\). The elements \(b_i^{N_i}\) generate the unit ideal in \(B_0\): expand a sufficiently large power of \(\sum e_i b_i=1\). A \(B_0\)-linear combination of the products \(b_i^{N_i}b\) is therefore \(b\). Hence \(B=B_0\), proving finite type.

For finite presentation choose a surjection \(P=A[T_1,\ldots,T_n]\to B\) with kernel \(I\), and lifts \(s_i,c_i\in P\) of \(b_i,e_i\). The element \(h=1-\sum c_i s_i\) belongs to \(I\). Each localized ideal \(I_{s_i}\) is finitely generated because \(B_{b_i}\) is finitely presented and \(P_{s_i}\) is a finitely presented algebra on a fixed finite generating set. More explicitly, introduce a variable for \(s_i^{-1}\), use the change-of-generators argument above, and then remove its relation \(s_iZ-1\); this leaves a finite generating set for the localized kernel. Clear denominators and choose finitely many elements of \(I\) that generate every \(I_{s_i}\). Let \(J\) be the ideal generated by all these elements and \(h\). In \(P/J\) the \(s_i\) generate the unit ideal, and the kernel of \(P/J\to B\) vanishes after localization at each \(s_i\). Every element of that kernel is killed by powers of all the \(s_i\); the same unit-ideal argument kills it globally. Thus \(I=J\), proving finite presentation. \(\square\)

The identical argument applies to a distinguished cover of the base, using elements of \(A\) in place of the \(b_i\). Localization on the base is also base change. These observations say that both ring-map properties are local on distinguished covers of source and target.

We use the affine communication principle for a ring-map property: if it survives localization on source and base and can be patched over finite distinguished covers, then a morphism having it on one compatible affine cover has it on every pair of affine opens mapping into one another. This is the usual affine communication lemma applied to morphisms; its precise formulation is [Stacks, Tag 01SU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-P-characterize). The principle uses distinguished refinements of affine covers and quasi-compactness of affine schemes. Lemma 2.1 supplies its nontrivial algebraic patching input here.

## 3. Finite type on every chart

A morphism is **locally of finite type** if it admits compatible affine covers for which the source coordinate rings are finite type algebras over the corresponding base rings. It is **of finite type** if it is locally of finite type and quasi-compact.

**Theorem 3.1.** A morphism \(f:X\to S\) is locally of finite type if and only if \(\Gamma(U)\) is of finite type over \(\Gamma(V)\) for every affine \(V\subset S\) and affine \(U\subset f^{-1}(V)\). Locally finite type and finite type are target-local and survive base change and composition. If \(gf\) is locally of finite type, then \(f\) is locally of finite type, without a condition on \(g\).

**Proof.** Lemma 2.1, localization stability and affine communication show that one compatible cover is equivalent to every affine pair. They also show target locality and invariance on restricting to open subschemes. The base-change calculation is \(B\mapsto B\otimes_A A'\), and finite algebra generators remain generators after tensoring. For composition choose compatible affine neighborhoods of the three points involved; composing finite generating sets proves the local assertion. Proposition 1.1 adds quasi-compactness for the finite-type assertions.

For cancellation, choose affine \(W\subset S\), \(V\subset g^{-1}(W)\), and \(U\subset f^{-1}(V)\). Set \(A=\Gamma(W)\), \(B=\Gamma(V)\), \(C=\Gamma(U)\). The hypothesis says that \(C\) has finitely many generators over \(A\). Those same elements generate \(C\) over \(B\), since the image of \(A\) is contained in the image of \(B\). The affine characterization proves the result. \(\square\)

A closed immersion is always of finite type. Its affine ring map is \(A\to A/I\), which needs no algebra generators, and it is quasi-compact. This puts no finiteness condition on the ideal \(I\).

The affine scheme \(\operatorname{Spec}k[x_1,x_2,\ldots]\) is not of finite type over \(k\): any finite collection of polynomials involves finitely many variables, and cannot generate a variable outside that collection. Another example is \(\operatorname{Spec}k[x]_{(x)}\). If this ring were generated by finitely many rational functions, their denominators would involve finitely many irreducible polynomials. Choose an irreducible polynomial other than \(x\) and these finitely many factors. Its reciprocal belongs to \(k[x]_{(x)}\) but not to the generated algebra. Such an irreducible exists by the polynomial version of Euclid's argument: if a finite list contained all irreducibles, an irreducible factor of one plus their product would be absent from it.

## 4. Finite presentation and its extra conditions

A morphism is **locally of finite presentation** if it has a compatible affine cover with finitely presented algebra maps. It is **of finite presentation** if it is locally of finite presentation, quasi-compact and quasi-separated. The last two requirements control the number of charts and the size of their overlaps.

**Theorem 4.1.** Local finite presentation is equivalent to finite presentation of the coordinate-ring map on every compatible affine pair. Both local finite presentation and finite presentation are target-local and stable under base change and composition. If \(S\) is locally Noetherian, local finite type and local finite presentation over \(S\) are equivalent; finite type and finite presentation over \(S\) are also equivalent.

**Proof.** For the first assertions apply Lemma 2.1 and affine communication as in Theorem 3.1, now keeping relations as well as generators. Tensor products preserve a finite list of relations, and composing two finite presentations gives a finite presentation by substitution. Quasi-compactness is stable by Proposition 1.1, and quasi-separatedness is stable by the diagonal theorem in the preceding lesson. These give the global assertions.

If \(A\) is Noetherian, \(A[T_1,\ldots,T_n]\) is Noetherian by the Hilbert basis theorem. Every ideal in it is finitely generated, so any finite type \(A\)-algebra is finitely presented. The converse needs no Noetherian hypothesis. Applied on affine charts this proves the local equivalence and also shows that the source is locally Noetherian. An affine open of a locally Noetherian scheme is Noetherian, so each open subset of it is quasi-compact. In particular intersections of affine opens are quasi-compact. The source is quasi-separated, and its morphism to any scheme is quasi-separated by diagonal cancellation. Thus a finite-type morphism over a locally Noetherian base has the extra quasi-separatedness needed for finite presentation. \(\square\)

There is a qualified cancellation theorem.

**Proposition 4.2.** If \(X\to S\) is locally of finite presentation and \(Y\to S\) is locally of finite type, then any \(S\)-morphism \(f:X\to Y\) is locally of finite presentation. If additionally \(X\to S\) is of finite presentation and \(Y\to S\) is quasi-separated, then \(f\) is of finite presentation.

**Proof.** On compatible affine charts write \(A\to B\to C\), with
\(B=A[b_1,\ldots,b_r]\) and \(C=A[c_1,\ldots,c_n]/(F_1,\ldots,F_m)\). Express the image of each \(b_i\) as a polynomial \(G_i(c)\). As a \(B\)-algebra, \(C\) has the finite presentation

\[
C\cong B[T_1,\ldots,T_n]/
\bigl(F_1,\ldots,F_m,\ b_1-G_1(T),\ldots,b_r-G_r(T)\bigr).
\]

The map from this quotient to \(C\) is an isomorphism: the first relations produce the \(A\)-algebra \(C\), and the remaining relations force the \(B\)-action to be precisely the given one. Thus the affine criterion proves the first assertion.

For the global assertion, diagonal cancellation makes \(f\) quasi-separated. Factor \(f\) as its graph followed by projection:
\(X\to X\times_S Y\to Y\). The graph is a base change of the quasi-compact diagonal of \(Y\to S\); hence it is quasi-compact. The projection is a base change of the quasi-compact map \(X\to S\). Their composite is quasi-compact, completing the definition. \(\square\)

The intermediate finite-type hypothesis cannot be removed. The maps

\[
\operatorname{Spec}k\longrightarrow
\operatorname{Spec}k[x_1,x_2,\ldots]\longrightarrow
\operatorname{Spec}k
\]

have identity composite, but the first sends every \(x_i\) to zero and is not locally of finite presentation. Its kernel \((x_1,x_2,\ldots)\) is not finitely generated. Any proposed finite list of its generators involves only finitely many variables, and setting those variables to zero shows that another variable cannot belong to the generated ideal. This same map is a closed immersion and is of finite type.

## 5. Closed points over Jacobson bases

A ring is **Jacobson** if every prime ideal is the intersection of the maximal ideals containing it. A scheme is Jacobson if its affine opens have Jacobson coordinate rings; equivalently, closed points are dense in every closed subset. Fields and \(\mathbf Z\) are Jacobson.

We assume the algebraic Jacobson theorem: a finite type algebra over a Jacobson ring is Jacobson; a maximal ideal of that algebra contracts to a maximal ideal of the base, and the resulting extension of residue fields is finite. This is proved in the prerequisite on the Nullstellensatz and Jacobson rings; an exact reference is [Stacks, Tag 00GB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-Jacobson-permanence).

**Theorem 5.1.** If \(f:X\to S\) is locally of finite type and \(S\) is Jacobson, then \(X\) is Jacobson. Every closed point \(x\in X\) maps to a closed point \(s\in S\), and \(\kappa(x)/\kappa(s)\) is finite. In particular, on a scheme locally of finite type over a field \(k\), a point is closed exactly when its residue field is finite over \(k\).

**Proof.** For affine opens \(U\subset f^{-1}(V)\), Theorem 3.1 gives a finite type algebra \(\Gamma(U)\) over the Jacobson ring \(\Gamma(V)\). The algebraic theorem makes every \(\Gamma(U)\) Jacobson. Hence \(X\) is Jacobson.

If \(x\) is closed in \(X\), its ideal in an affine neighborhood \(U\) is maximal. Its contraction to an affine target neighborhood \(V\) is maximal and the residue extension is finite. A point closed in an affine open of a Jacobson scheme is closed in the whole scheme. Here is a way to see this last assertion. Such a point is locally closed. If it had a distinct specialization \(s'\), an affine neighborhood of \(s'\) would also contain the original point; its closure in that affine is irreducible and has the original point as an open generic point. The Jacobson property gives a closed point in this nonempty singleton open, forcing the generic point to be closed there. It cannot then have a distinct specialization. This proves global closedness and the residue-field assertion.

Over \(k\), a point with finite residue field extension gives a \(k\)-algebra image inside a finite-dimensional field. That image is a finite-dimensional domain, so is a field (multiplication by a nonzero element is an injective, hence surjective, linear map). The point is therefore maximal in any affine neighborhood. Since \(X\) is Jacobson, it is globally closed. The reverse implication was already proved. \(\square\)

For \(\mathbf A^1_{\mathbf Q}\), closed points correspond to monic irreducible polynomials in \(\mathbf Q[t]\), and their residue fields are \(\mathbf Q[t]/(p)\). Equivalently, they correspond to finite Galois orbits in \(\overline{\mathbf Q}\). One orbit is one closed point; its individual roots become different geometric points after extending the base to an algebraic closure.

## 6. Exercises and solutions

**Exercise 6.1 (easy).** Let \(A=k[u_1,u_2,\ldots]\) and \(I=(u_2,u_4,u_6,\ldots)\). Show that \(\operatorname{Spec}(A/I)\to\operatorname{Spec}A\) is finite type and is not of finite presentation.

**Solution.** A quotient algebra has zero required algebra generators, and a closed immersion is quasi-compact, so the map is finite type. A quotient is finitely presented as an algebra exactly when its kernel is finitely generated, by the change-of-generators argument of Section 2. Any finite list in \(I\) uses finitely many even-indexed variables. Setting all variables appearing in that list to zero kills their generated ideal while leaving some other even-indexed variable nonzero. Thus \(I\) is not finitely generated. The affine criterion for local finite presentation rules out finite presentation of the morphism.

**Exercise 6.2 (easy).** What specialization prevents the image of \(D(t-2)\hookrightarrow\mathbf A^1_{\mathbf Q}\) from being closed? Compare it with the image of \(D(t)\hookrightarrow\mathbf A^1_k\).

**Solution.** The generic point \((0)\) belongs to \(D(t-2)\), but its specialization \((t-2)\) does not. This violates the criterion in Theorem 1.2. The open immersion is quasi-compact because its source is a distinguished affine open. In the second example the analogous omitted specialization is \((t)\), again from the generic point. These examples also show directly that the images are dense proper opens and hence are not closed.

**Exercise 6.3 (medium).** Prove local finite-type cancellation using ring generators. Does the same proof establish local finite-presentation cancellation?

**Solution.** On compatible affine charts \(A\to B\to C\), a finite set generating \(C\) over \(A\) also generates it over \(B\). This proves local finite-type cancellation. Relations are different: passing to a larger intermediate algebra can introduce infinitely many new relations. The map \(k[x_1,x_2,\ldots]\to k\) in Section 4 has infinitely generated kernel, despite the identity composite \(k\to k\). Thus the unqualified finite-presentation assertion is false. When \(B\) is finite type over \(A\), Proposition 4.2 adds finitely many compatibility relations and proves the qualified assertion.

**Exercise 6.4 (medium).** For \(X\) locally of finite type over a field, prove the closed-point criterion. In \(\mathbf A^1_{\mathbf Q}\), identify the point corresponding to the orbit of \(\sqrt[3]{2}\).

**Solution.** Closed points have finite residue extension by the algebraic Jacobson theorem applied to an affine neighborhood. Conversely, a finite residue extension makes the coordinate-ring image a finite-dimensional domain, hence a field, and maximality in an affine neighborhood gives global closedness in the Jacobson scheme. The orbit in question consists of the three roots of \(t^3-2\). Eisenstein's criterion at \(2\) proves that polynomial irreducible over \(\mathbf Q\), so it defines the closed point \((t^3-2)\), with residue field \(\mathbf Q[t]/(t^3-2)\) of degree three.

**Exercise 6.5 (hard).** Reprove the closed-image criterion without a Noetherian hypothesis. Locate the exact place where quasi-compactness enters. Show the conclusion can fail without it.

**Solution.** Over an affine target cover the source by finitely many affines. A point in the closure of their image lies in the closure of one affine image, because the union is finite. Localization at that point is nonzero in the chosen source ring, so it contains a prime whose contraction generalizes the point. Specialization stability puts the point into the image. This is precisely the proof of Theorem 1.2; finiteness of the affine cover is the indispensable step. For failure, let \(k\) be infinite and map \(\coprod_{a\in k}\operatorname{Spec}k\) to \(\mathbf A^1_k\) by the points \(t=a\). Its image consists of the \(k\)-rational closed points, is stable under specialization, and is dense because a nonzero polynomial has finitely many roots. It omits the generic point, so it is not closed. Its source, the inverse image of the affine target, is not quasi-compact.

## What this lesson does not prove

All asserted properties of scheme morphisms in this lesson have been proved from the specified prerequisites. The algebraic Jacobson theorem, the Hilbert basis theorem, affine communication for local ring-map properties, and the elementary affine spectrum and localization constructions are imported algebraic or scheme prerequisites. For the first and third, precise reference statements are [Stacks, Tag 00GB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-Jacobson-permanence) and [Stacks, Tag 01SU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-locally-P-characterize). Finite presentation and its behavior on inverse limits are developed in the next lesson.

## References

- The Stacks project authors, *The Stacks project*: quasi-compact morphisms [Tag 01K2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-section-quasi-compact); closed-image criterion [Tag 05JL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-image-quasi-compact-closed); finite type [Tag 01T0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-finite-type); finite presentation [Tag 01TO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-section-finite-presentation); qualified cancellation [Tag 02FV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-presentation-permanence); Noetherian comparison [Tag 01TX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-noetherian-finite-type-finite-presentation); Jacobson schemes [Tag 02J5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-Jacobson-universally-Jacobson). Links point to the AI Integrated Stacks Project English edition.
- Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, public draft of 27 July 2024, §8.3, especially the distinction between finite type and finite presentation. [Author's open text](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf).
