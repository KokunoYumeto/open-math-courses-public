# Rational maps and birational morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A rational map records a morphism wherever it is defined, while permitting us to discard a smaller closed set. This makes function fields geometrically useful: a field homomorphism can specify a map before its exceptional points are understood. The exceptional set still matters. Projection from a point of a surface may remain undefined there, whereas a rational map from a regular curve to a proper target always extends.

We use the equalizer theorem from The diagonal and separated morphisms, the valuative criterion from Proper morphisms, and the conventions of Normalization. A **variety over \(k\)** means an integral separated scheme of finite type over \(k\). A curve in the extension theorems is integral and of dimension one. Normal curves have normal local rings; they need not be smooth over an imperfect field. The algebraic fact that a one-dimensional Noetherian normal local domain is a DVR is proved in Discrete valuation rings, normal rings and Serre's criterion, Theorem 1.2.

## 1. Maps defined on dense opens

A **rational map** \(X\dashrightarrow Y\) is an equivalence class of pairs \((U,f)\), where \(U\subset X\) is a dense open and \(f:U\to Y\) is a morphism. Two pairs are equivalent when the morphisms agree on some dense open contained in both domains. This is an equivalence relation: intersections of finitely many dense opens are dense, so two agreements can be intersected to prove transitivity. For schemes over \(k\), all representative morphisms are over \(k\).

A rational map is not generally a morphism on the union of its representative domains. Agreement on a dense open does not automatically imply agreement everywhere on the overlap. The following theorem supplies exactly that implication under useful hypotheses.

**Theorem 1.1 (largest domain).** If \(X\) is reduced and \(Y\) is separated, every rational map \(X\dashrightarrow Y\) has a unique representative on the union of all its representative domains. This union is its largest **domain of definition**.

**Proof.** Let \(f:U\to Y\) and \(g:V\to Y\) represent the same rational map. Their equalizer on \(U\cap V\) is a closed subscheme, since the diagonal of \(Y\) is closed. Its underlying closed set contains a dense open, hence is all of \(U\cap V\). On an affine open of \(U\cap V\), every element of its defining ideal therefore belongs to every prime ideal. It is nilpotent, and is zero because \(X\) is reduced. Thus the equalizer is the entire scheme \(U\cap V\).

All representative morphisms consequently agree on their overlaps and glue on their union \(D\). This glued morphism still represents the original class. Any other representative on \(D\) agrees with it on a dense open, so the same equalizer argument makes it equal everywhere. Every representative domain is contained in \(D\) by construction. \(\square\)

This is [Stacks, Tag 0A1Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-rational-map-from-reduced-to-separated). Over a base \(S\), the same proof applies to \(S\)-rational maps when \(Y\to S\) is separated. The theorem concerns the rational map itself, rather than one choice of coordinates: a coordinate formula may have removable common factors.

For an integral scheme \(X\), its generic point \(\eta\) has residue field

\[
K(X)=\mathcal O_{X,\eta}.
\]

For every nonempty affine open \(\operatorname{Spec}A\subset X\), this is \(\operatorname{Frac}(A)\). A rational function is a rational map to \(\mathbb A^1\), or equivalently a regular function on a dense open, considered up to restriction. These rational functions form exactly \(K(X)\). Indeed, a regular function on a nonempty open is determined by its germ at \(\eta\): restriction to affine opens embeds their domains into the same fraction field. Conversely \(a/b\in\operatorname{Frac}(A)\), with \(b\ne0\), is regular on \(D(b)\). Addition and multiplication are performed on intersections of domains. See [Stacks, Tag 01RV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-integral-scheme-rational-functions).

One cannot compose arbitrary rational maps. The constant map \(\mathbb A^1\to\mathbb A^1\) with value zero cannot be followed by the rational function \(1/t\) on its displayed domain \(D(t)\); there is no nonempty source open mapping into that domain. For integral schemes, **dominant** rational maps avoid this problem. A representative is dominant precisely when it sends the generic point to the target's generic point. It then meets every nonempty target open, whose inverse image is a nonempty, hence dense, source open. Dominant rational maps therefore compose, and further restriction makes composition independent of representatives.

## 2. Function fields determine dominant rational maps

**Theorem 2.1 (field correspondence).** Let \(X,Y\) be varieties over \(k\). Pullback gives a bijection

\[
\{\text{dominant rational maps }X\dashrightarrow Y\}
\longleftrightarrow
\{k\text{-embeddings }K(Y)\hookrightarrow K(X)\}.
\tag{2.1}
\]

Composition of rational maps corresponds to composition of embeddings in the reverse direction. The construction of a representative and its uniqueness also hold for integral finite-type \(k\)-schemes without a separatedness assumption.

**Proof.** A dominant representative sends \(\eta_X\) to \(\eta_Y\). Its map of local rings there is a \(k\)-homomorphism \(K(Y)\to K(X)\); a homomorphism of fields is injective. Restricting the representative does not change this map.

Conversely, let \(\phi:K(Y)\hookrightarrow K(X)\) be a \(k\)-embedding. Choose nonempty affine opens \(\operatorname{Spec}A\subset X\) and \(\operatorname{Spec}B\subset Y\). The \(k\)-algebra \(B\) has finitely many generators \(b_1,\ldots,b_r\). Write their images in \(\operatorname{Frac}(A)\) as fractions and let \(s\in A\setminus\{0\}\) be the product of their denominators. Then \(\phi\) restricts to an injective map

\[
B\longrightarrow A_s.
\]

This defines \(D(s)\to\operatorname{Spec}B\subset Y\). Its generic-point map has kernel zero, so it is dominant and induces the prescribed embedding.

To prove uniqueness, two representatives with the same generic-point map can both be restricted to the inverse image of any common affine neighborhood of \(\eta_Y\). On a nonempty affine source open inside that intersection, their homomorphisms from the target coordinate ring have the same images in \(K(X)\). Since the source coordinate ring embeds in \(K(X)\), the homomorphisms are equal. The representatives thus agree on a dense open. This argument does not require separatedness. The rule for composition follows from composition of ring homomorphisms. \(\square\)

The finite-type assumption on the target supplies the finite list of denominators. The theorem is the geometric content of [Stacks, Tag 0BXN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-theorem-varieties-rational-maps).

Let the category of finitely generated field extensions of \(k\) have \(k\)-embeddings as its arrows. The functor \(X\mapsto K(X)\) is an **anti-equivalence** from varieties with dominant rational maps to this category. Theorem 2.1 gives full faithfulness. For essential surjectivity, write a finitely generated extension as \(K=k(a_1,\ldots,a_r)\). The domain \(A=k[a_1,\ldots,a_r]\subset K\) is finitely generated and has fraction field \(K\). Its affine spectrum is a variety giving the required field. Different choices of \(A\) can give different schemes, but the same birational geometry.

## 3. Birational maps and birational morphisms

Two integral schemes are **birational** when some nonempty opens in them are isomorphic. Equivalently they admit inverse rational maps. Here is the latter equivalence explicitly. Suppose \(f: X\dashrightarrow Y\) and \(g: Y\dashrightarrow X\) have rational composites equal to the identities. Choose representatives, then shrink a nonempty open \(W\subset X\) so that \(f(W)\) lies in the domain of \(g\) and \(gf\) is the identity on \(W\). Shrink a nonempty open \(V_1\subset Y\) so that \(g(V_1)\subset W\) and \(fg\) is the identity on \(V_1\). Such restrictions are possible by dominance and the asserted rational identities. Put \(W_1=W\cap f^{-1}(V_1)\). Then \(g(V_1)\subset W_1\), and the restrictions \(W_1\to V_1\) and \(V_1\to W_1\) are inverse morphisms. Conversely an isomorphism of nonempty opens gives inverse rational maps. See [Stacks, Tag 0BAA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-birational-integral).

**Corollary 3.1.** Integral finite-type \(k\)-schemes \(X,Y\) are birational over \(k\) if and only if \(K(X)\) and \(K(Y)\) are \(k\)-isomorphic.

**Proof.** An isomorphism of nonempty opens identifies their generic local rings. Conversely, a field isomorphism and its inverse give rational maps by Theorem 2.1. Their composites induce identity field maps, hence are identity rational maps by uniqueness. The preceding restriction argument yields isomorphic nonempty opens. \(\square\)

For schemes with finitely many irreducible components, a **birational morphism** \(f:X\to Y\) means that it bijects generic points of irreducible components and induces isomorphisms of their local rings. For integral schemes this says that the generic point maps to the generic point and \(K(Y)\to K(X)\) is an isomorphism. This is the convention of [Stacks, Tag 01RO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-birational). For integral finite-type \(k\)-schemes, a birational morphism therefore restricts to an isomorphism of nonempty opens, by the same proof with its given representative.

There is also a useful version allowing nilpotents: a birational morphism between schemes with finitely many irreducible components restricts to an isomorphism on dense opens if it is locally of finite presentation, or if it is locally of finite type and the target is reduced. The complete proof is [Stacks, Tag 0BAC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-birational-birational). Its algebra explains the alternatives. After separating the finitely many components into disjoint dense opens, one works with a finite-type map \(B\to A\) whose generic localization is an isomorphism. Finitely many denominators express the generators of \(A\) as elements of a localization of \(B\), making the localized map surjective. Reducedness of the irreducible target makes its map to its generic local ring injective, giving injectivity immediately. Alternatively finite presentation makes the kernel finitely generated, so another finite list of denominators kills it. This last step is why mere finite type without reducedness does not suffice.

A field isomorphism alone does not produce a morphism everywhere. The normalization of a nodal curve from the preceding lesson is a finite birational morphism, but separates its two branches at the node. Conversely a birational rational map can contract a curve on part of its domain and have points where it does not extend at all.

Finite type also matters in passing from equal function fields to isomorphic opens. The natural morphism \(\operatorname{Spec}k(t)\to\operatorname{Spec}k[t]\) is birational in the generic-point sense. Its source is a single point, whereas no nonempty open of the affine line is a single point. To see this over every field, any nonempty open contains some \(D(f)\), with \(f\ne0\). There is an irreducible polynomial not dividing \(f\): if all irreducibles belonged to the finite list of factors of \(f\), an irreducible factor of one plus their product would contradict that list. The corresponding closed point lies in \(D(f)\), as does the generic point. This birational morphism is not of finite type over \(k\).

## 4. Extending across a curve point

**Theorem 4.1 (extension at a DVR).** Let \(X\) be an integral finite-type curve over \(k\), let \(x\) be a closed point with \(R=\mathcal O_{X,x}\) a DVR, and let \(Y\) be proper over \(k\). A morphism \(f:U\to Y\) on a nonempty open \(U\subset X\) extends uniquely to a morphism on \(U\cup W\), for some open neighborhood \(W\) of \(x\).

**Proof.** The generic value gives \(\operatorname{Spec}K(X)\to Y\). The valuative criterion of properness supplies a unique extension \(\operatorname{Spec}R\to Y\). Choose an affine open \(V=\operatorname{Spec}B\subset Y\) containing the image of the closed point of \(\operatorname{Spec}R\). Its inverse image is an open containing that closed point, hence is the entire local spectrum. The extension consequently corresponds to \(B\to R\).

As \(Y\) is of finite type, choose finite \(k\)-algebra generators of \(B\). Their images in \(R\) are represented by regular functions on a common affine neighborhood \(W\) of \(x\). All relations among those generators hold in \(K(X)\), and therefore in \(\Gamma(W,\mathcal O_X)\), which embeds in that field. They define a morphism \(W\to V\). It has the same generic value as \(f\). On \(U\cap W\), the two maps agree by the reduced-to-separated equalizer argument. They glue to an extension on \(U\cup W\). Any two extensions agree on their common domain by that same argument. \(\square\)

The proof separates two operations: properness extends to a local valuation spectrum, and finite generation spreads that local map to a neighborhood. This is [Stacks, Tags 0BX7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-extend-across) and [0BXY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-extend-over-dvr), here in the integral-curve case needed below.

**Corollary 4.2.** Every rational map from a normal finite-type integral curve over \(k\) to a proper \(k\)-scheme extends uniquely to the entire curve.

**Proof.** Each closed point has a one-dimensional Noetherian normal local domain, hence a DVR. The generic point is already in the original domain and has a field as local ring. These are all the points of an integral finite-type curve. Apply Theorem 4.1 at every missing closed point and glue the extensions by uniqueness. \(\square\)

In particular, two normal proper curves with \(k\)-isomorphic function fields are isomorphic. Corollary 3.1 gives inverse rational maps; Corollary 4.2 extends them to morphisms on both curves. Their composites agree with the identities on dense opens, hence everywhere by separatedness and reducedness. This is [Stacks, Tag 0BXZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-extend-over-normal-curve).

For projective space the local extension is particularly concrete. Represent the generic value by \([a_0:\cdots:a_n]\), with \(a_i\in K(X)\) not all zero. If \(\pi\) is a uniformizer, multiply all entries by \(\pi^{-m}\), where \(m\) is the minimum valuation of the nonzero entries. The resulting coordinates lie in \(R\), with at least one a unit. They define an \(R\)-point of \(\mathbb P^n\). A common neighborhood represents these finitely many functions and keeps the unit entry nonvanishing. This proves extension directly and explains why an apparent common zero of homogeneous coordinates on a regular curve is removable.

## 5. Three birational constructions

**Projection from a point.** Projection from \(p=[0:0:1]\) is

\[
\mathbb P^2\dashrightarrow\mathbb P^1,
\qquad [x:y:z]\longmapsto[x:y].
\]

Its displayed domain is \(\mathbb P^2\setminus\{p\}\). On the affine chart \(z=1\), the lines \((x,y)=(t,0)\) and \((0,t)\) give the distinct constant values \([1:0]\) and \([0:1]\) away from \(p\). An extension would restrict to these constants at \(p\) as well, since each line is reduced and the target separated. Thus no extension exists there. Curve extension does not apply: the source local ring at \(p\) has dimension two and is not a DVR.

**The Cremona involution.** Consider

\[
c:\mathbb P^2\dashrightarrow\mathbb P^2,
\qquad [x:y:z]\longmapsto[yz:xz:xy].
\tag{5.1}
\]

The coordinates vanish simultaneously exactly at the three coordinate vertices. On \(xyz\ne0\), applying (5.1) twice gives \([x^2yz:xy^2z:xyz^2]=[x:y:z]\); hence this is a birational involution. The line \(x=0\), away from the vertices, is contracted to \([1:0:0]\), and cyclically for the other two lines. The formula defines a morphism along those punctured lines despite failing to be an isomorphism there. Exercise 6.2 checks that each of the three omitted vertices is an unavoidable indeterminacy point.

**Projection from a split quadric.** Over any field, put

\[
Q=V(X_0X_3-X_1X_2)\subset\mathbb P^3,
\qquad p=[1:0:0:0].
\]

This quadric is smooth: on each coordinate chart the equation eliminates the opposite coordinate and leaves an affine plane. It is integral, for its chart \(X_3\ne0\) is an affine plane and dense; the equation is irreducible, being linear in \(X_0\) with relatively prime coefficient \(X_3\) and constant term \(-X_1X_2\). Projection from \(p\) gives

\[
Q\dashrightarrow\mathbb P^2,
\quad [X_0:X_1:X_2:X_3]\longmapsto[X_1:X_2:X_3].
\]

A rational inverse is

\[
[A:B:C]\longmapsto[AB:AC:BC:C^2].
\tag{5.2}
\]

The coordinates in (5.2) satisfy the quadric equation. On \(C\ne0\) and \(X_3\ne0\), the two formulas are inverse, using \(X_0X_3=X_1X_2\). Thus this is a stereographic parametrization of the split quadric by a plane. The inverse formula has base points \([1:0:0]\) and \([0:1:0]\). The two lines of \(Q\cap V(X_3)\) through \(p\) are contracted by the forward projection to these two distinct points. Their values cannot both extend at \(p\). The construction is birational over every field; it makes no assertion that every quadric surface over every field has such a rational point or is split.

## 6. Exercises and solutions

**Exercise 6.1 (easy).** Prove that projection \([x:y:z]\mapsto[x:y]\) does not extend across \([0:0:1]\), including over a finite field.

**Solution.** An open neighborhood of the point pulls back along each of the two affine lines in Section 5 to a nonempty open of \(\mathbb A^1\) containing zero. Its punctured part is dense as a scheme, even if it has few rational points. On one punctured line the map is constantly \([1:0]\), on the other constantly \([0:1]\). The equalizer theorem forces the same constants on the whole respective neighborhoods. Evaluating at their common origin gives incompatible values. The argument uses scheme-theoretic density, so it is independent of the size of \(k\).

**Exercise 6.2 (medium).** Find the largest domain of the Cremona map.

**Solution.** Formula (5.1) defines a morphism off the three vertices. Near \([1:0:0]\), put \(u=y/x,v=z/x\); its coordinates are \([uv:v:u]\). On \(u=0,v\ne0\) the value is \([0:1:0]\); on \(v=0,u\ne0\) it is \([0:0:1]\). The argument of Exercise 6.1 forbids extension at the vertex. Cyclic permutation forbids it at the other two. Since \(\mathbb P^2\) is reduced and the target separated, Theorem 1.1 applies. Its largest domain is precisely the complement of those three points, including the contracted punctured coordinate lines.

**Exercise 6.3 (medium).** Construct the dominant rational map corresponding to \(k(t)\hookrightarrow k(u,v)\), \(t\mapsto u/v\), and determine whether the embedding identifies the function fields. Explain why any embedding between finitely generated function fields arises similarly.

**Solution.** For \(X=\mathbb A^2\) and \(Y=\mathbb A^1\), the map on \(D(v)\) is \((u,v)\mapsto u/v\). It is dominant because \(u/v\) is transcendental over \(k\): a polynomial relation, multiplied by a sufficient power of \(v\), would give a nonzero polynomial in the algebraically independent variables \(u,v\). The fields have transcendence degrees two and one, so they are not isomorphic. In general choose finitely many generators of an affine target algebra. Express their images as fractions on an affine source open and invert the product of the denominators. Relations hold in the fraction field and hence in the localized source domain. This produces a morphism with injective generic pullback. Equality of pullbacks forces equality on a smaller affine open, giving the full correspondence, rather than merely an existence claim.

**Exercise 6.4 (medium).** Show directly that a rational map from a regular integral finite-type curve to \(\mathbb P^n\) extends to the whole curve.

**Solution.** At each closed point the regular one-dimensional local ring is a DVR, by the DVR characterization cited in the prerequisites. Write the generic map as a nonzero homogeneous tuple. Subtract the minimum coordinate valuation by multiplying the tuple by a common power of a uniformizer. All coordinates become regular at the point and one becomes a unit. Represent them on a common affine neighborhood and shrink so the unit stays invertible. The tuple there defines a projective-space morphism with the prescribed generic value. It agrees with the original map, and with every other such extension, on overlaps by Theorem 1.1. These neighborhoods and the original domain cover the curve, so they glue. No smoothness or algebraic closure of the ground field is needed.

**Exercise 6.5 (hard).** Give separate counterexamples showing why reducedness of the source and separatedness of the target enter the uniqueness assertion for largest domains.

**Solution.** First set \(X=\operatorname{Spec}k[t,\epsilon]/(\epsilon^2,t\epsilon)\), and let the target be \(\mathbb A^1\) with coordinate \(w\). The two global morphisms \(w\mapsto0\) and \(w\mapsto\epsilon\) are distinct, since \(\epsilon\ne0\) in this ring. On \(D(t)\), however, \(\epsilon=0\). This is a dense open because the reduced scheme is \(\mathbb A^1\). The two global morphisms represent the same rational map. Its domain union is already all of \(X\), but it has no unique global representative.

For the other example, let \(Y\) be the affine line with doubled origin, obtained by gluing two copies of \(\mathbb A^1\) along \(D(t)\). The two chart inclusions \(\mathbb A^1\to Y\) agree on \(D(t)\) and send zero to different origins. They are distinct global representatives of the same rational map from a reduced source. Again the domain union is the whole source, while uniqueness fails. These examples refute a largest-domain theorem with a unique representative after either hypothesis is removed; they do not assert that the set-theoretic union itself fails to be open.

## References and proof dependencies

All four central results are proved above. Their scheme-theoretic support is supplied by the preceding lessons on equalizers and properness, and the written commutative-algebra lesson on DVRs. The field correspondence and the extension theorem are compared with the exact linked Stacks proofs. The Stacks project authors, *The Stacks project*, are consulted in the AI Integrated Stacks Project edition at commit `565b10e987aba5969b21145a0833f42d69f96790`; the linked source is under GNU FDL 1.2. Its expression is not reproduced here.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §§7.5 and 15.3, supplies an alternative discussion of rational maps and the curve extension theorem. The coordinate examples and all proofs and solutions here use independent exposition. Their conclusions distinguish birational equivalence from an everywhere-defined morphism, and an everywhere-defined morphism from an isomorphism.
