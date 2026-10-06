# Profinite groups and ℓ-adic representations

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A representation turns Galois automorphisms into linear operators. Its coefficient field matters: continuous complex representations of a profinite group have finite image, whereas continuous ℓ-adic representations can retain an infinite part of the group. Integral lattices connect the latter representations to finite fields. The lattice is a choice; the composition factors of its reduction are intrinsic.

The proofs begin with the algebra and topology needed for the representation arguments. In particular, an unwritten prerequisite title is not a proof: §§0A–0F supply the lattice algebra, finite and infinite Galois theory, completeness, root lifting and unramified extensions used below. The freely accessible primary materials are Taylor's article, Ribet's author copy, the original Stacks project and Milne's freely available author notes. Their links and exact reading locators appear at the end; the proofs are written here, rather than delegated to those links. Section 3A supplies the complete specific elliptic comparison. The final dependency note records the earlier geometric and class-field prerequisite chains.

Let \(E/\mathbb Q_\ell\) be finite, let \(\mathcal O\) be its ring of integers, choose a uniformizer \(\pi\), and put \(k=\mathcal O/\pi\mathcal O\). Proposition 0E.1 proves the properties implicit in this notation. An \(\mathcal O\)-lattice in an \(n\)-dimensional \(E\)-vector space is a free \(\mathcal O\)-submodule of rank \(n\) which spans the space. All representations of topological groups in this chapter are continuous. We use arithmetic Frobenius: on a finite residue field of size \(q\), it acts by \(x\mapsto x^q\). Its construction is in §0F. No reciprocity theorem or Weil–Deligne relation is used in this lesson.

## 0A. The algebra needed for lattices and composition factors

A **discrete valuation** on a field \(F\) is a surjective function \(v:F^\times\to\mathbb Z\) satisfying \(v(xy)=v(x)+v(y)\) and \(v(x+y)\ge\min(v(x),v(y))\) when \(x+y\ne0\). Its valuation ring is \(R=\{0\}\cup\{x:v(x)\ge0\}\). Choose \(\varpi\) with \(v(\varpi)=1\). A nonzero element of \(R\) is \(u\varpi^a\), with \(u\) a unit and \(a\ge0\): divide by the indicated power, and both the resulting element and its inverse have valuation zero. Every nonzero ideal is \(\varpi^aR\), since the nonempty set of valuations of its nonzero elements has a least member. In particular \(R\) is a principal ideal domain. We put \(v(0)=+\infty\).

**Lemma 0A.1 (freeness, bounds and finite quotients).** A submodule of \(R^n\) is free of rank at most \(n\) and is finitely generated. A finitely generated torsion-free \(R\)-module is free. Two full lattices \(L,M\) in \(F^n\) satisfy
\[
 \varpi^aL\subseteq M\subseteq\varpi^{-b}L
 \quad\text{for some }a,b\ge0.
\]
If \(M\subseteq L\), the quotient \(L/M\) is killed by a power of \(\varpi\) and has finite length. If \(R/\varpi R\) is finite, every \(L/\varpi^aL\) is a finite set.

**Proof.** Induct on \(n\). Project a submodule \(N\subseteq R^n\) to its first coordinate. If the image is zero, use the induction hypothesis in \(R^{n-1}\). Otherwise its image is an ideal \(dR\). Choose \(z\in N\) projecting to \(d\). Every element is uniquely the sum of a multiple of \(z\) and an element of the projection kernel. Thus \(N=Rz\oplus\ker\), and induction proves the claim, including finite generation. For a finitely generated torsion-free module \(T\), the map \(T\to F\otimes_RT\) is injective: localization kills exactly those elements annihilated by a nonzero scalar. Choose coordinates in the finite-dimensional span of its generators. Multiplication by one sufficiently large power of \(\varpi\) puts every generator in \(R^n\), reducing freeness to the preceding case. Its rank equals its dimension after extending scalars to \(F\).

Express a basis of \(M\) in a basis of \(L\), and also the latter basis in the former. Each of these two finite matrices has entries whose valuations are bounded below. Clearing the two sets of denominators gives the displayed bounds. If \(M\subseteq L\), the first bound kills \(L/M\) by \(\varpi^a\). Its successive quotients for the filtration by powers of \(\varpi\) are finite-dimensional over \(R/\varpi R\), and therefore have finite composition series. Finally \(\varpi^jR/\varpi^{j+1}R\simeq R/\varpi R\); induction on \(a\), followed by a basis of \(L\), proves finiteness. \(\square\)

We will also use the **determinant trick**. If multiplication by \(x\) preserves a nonzero finitely generated submodule \(T\) of a field extension of the fraction field of \(R\), choose generators \(t_1,\ldots,t_s\) and write \(xt_i=\sum_j a_{ij}t_j\), with \(a_{ij}\in R\). The adjugate identity applied to \(xI-(a_{ij})\) gives \(\det(xI-(a_{ij}))t_i=0\). Since one \(t_i\) is nonzero, this monic polynomial vanishes at \(x\). Thus \(x\) is integral over \(R\). Conversely, finitely many integral elements generate a finite \(R\)-module: their defining monic equations reduce all sufficiently high powers. This also proves that sums and products of integral elements are integral, and that integrality is transitive, by applying the trick to the finite module containing their products. A valuation ring is integrally closed in its fraction field: if \(v(x)<0\), the leading term of a monic equation has strictly smaller valuation than every other term and cannot be cancelled.

For a local ring \((A,\mathfrak m)\), the same trick proves the form of **Nakayama's lemma** needed here. If a finitely generated module \(T\) satisfies \(\mathfrak mT=T\), write generators as combinations of themselves with coefficients in \(\mathfrak m\). The determinant of \(I-(a_{ij})\) belongs to \(1+\mathfrak m\), hence is a unit, and kills every generator. Therefore \(T=0\).

**Lemma 0A.2 (Jordan–Hölder and exact-sequence additivity).** A finite-dimensional representation over a field has a composition series. Its multiset of simple factors is independent of the series. The same conclusions hold for an \(R\)-module with a commuting group action that is finitely generated and killed by a power of \(\varpi\). In an exact sequence, the factors of the middle object are the union, with multiplicity, of those of its subobject and quotient.

**Proof.** In the first case a strictly increasing chain of subobjects has length at most the dimension. In the second case use
\(\sum_j\dim_{R/\varpi R}(\varpi^jT/\varpi^{j+1}T)\): it is finite and bounds the length of a strict chain. Indeed intersect each subobject with \(\varpi^jT\) and take its image in \(\varpi^jT/\varpi^{j+1}T\). These images form increasing chains of vector subspaces. If every image for two nested subobjects agrees, cancel their lifts successively through the finite filtration to see the subobjects agree; hence a strict step increases at least one of the finitely many dimensions. Choose a maximal proper subobject and continue, so a series exists. For uniqueness, induct on this bound. If two series have the same penultimate subobject \(A\), induction applies to \(A\). Otherwise let their distinct maximal proper subobjects be \(A,B\). Then \(A+B=T\), and the maps to quotients give
\[
 A/(A\cap B)\simeq T/B,\qquad
 B/(A\cap B)\simeq T/A.
\]
Both quotients are simple. By induction the factors in \(A\) are those in \(A\cap B\), together with \(T/B\); the factors in \(B\) are those in the intersection, together with \(T/A\). Adding the final simple quotient gives the same multiset in either series. A series in a subobject followed by the inverse images of a series in its quotient proves additivity. In the second category every simple object is killed by \(\varpi\): otherwise \(\varpi S=S\), which contradicts the nilpotence of \(\varpi\) on \(S\). Thus its simple objects are precisely the relevant simple residue-field representations. \(\square\)

Two elementary matrix facts used below can be justified directly. For \(A\in M_n(F)\), write \(\operatorname{adj}(XI-A)=\sum B_jX^j\). Comparing coefficients in
\((XI-A)\operatorname{adj}(XI-A)=\det(XI-A)I\) makes each \(B_j\) a polynomial in \(A\), and substitution yields \(\det(XI-A)|_{X=A}=0\). This is Cayley–Hamilton. Over \(\mathbb C\), every polynomial has a root: its modulus attains a minimum because it tends to infinity at infinity; if its value at a minimizing point were nonzero, the first nonconstant term in its expansion there could be given the opposite argument by a sufficiently small displacement, decreasing the modulus. More explicitly, after division by that value the expansion is \(1+cz^r+O(z^{r+1})\); choose \(cz^r=-t\), \(t>0\), and for small \(t\) the error is smaller than \(t/2\), contradicting minimality. Division by the resulting linear factor and induction split the polynomial. Thus a complex matrix has eigenvalues, and Cayley–Hamilton implies that a matrix all of whose eigenvalues are \(1\) is \(1\) plus a nilpotent matrix.

## 0B. Finite Galois theory and extension of embeddings

Fix a separable closure \(K^{\mathrm{sep}}\). Algebraic closures and the choice principle for extending partially defined embeddings are part of our set-theoretic foundations. The following proves the field-theoretic statements used in this lesson.

**Lemma 0B.1.** A finite separable extension of degree \(d\) has exactly \(d\) embeddings into a separable closure over its base field. An embedding of an intermediate algebraic field extends to a base-field automorphism of the separable closure. A finite normal separable extension \(L/K\) has \([L:K]\) automorphisms.

**Proof.** For a simple extension, embeddings correspond exactly to the distinct roots of its irreducible polynomial: substitution defines a map of \(K[X]/(f)\), and every embedding must take the generator to such a root. For a finite extension generated by several separable elements, extend an embedding one generator at a time. At each step the number of choices is the degree of that step. Multiplying these numbers gives the tower degree, because the products of the basis elements of the steps form a basis.

For an arbitrary algebraic intermediate field, order partial extensions of the embedding by inclusion. A chain has its union as an extension. A maximal extension exists by the choice principle. If its domain omits an element, a root of the transformed minimal polynomial extends it one step, a contradiction. Every chosen root lies in the separable closure: it is a conjugate over the base of an element separable over that base. The resulting base-field embedding of the separable closure is onto, since it permutes the finite set of roots of each separable polynomial over the base, and every element belongs to one such set. A finite normal extension likewise contains every conjugate of each generator, so each of its \([L:K]\) embeddings lands in \(L\) and is an automorphism. \(\square\)

**Lemma 0B.2 (finite fixed-field theorem).** If \(H\) is a finite group of automorphisms of a field \(L\), then \([L:L^H]=|H|\) and \(\operatorname{Gal}(L/L^H)=H\). For a finite normal separable extension \(L/K\), subgroups and intermediate fields correspond by fixed fields and stabilizers; normal subgroups give Galois quotients.

**Proof.** Distinct field homomorphisms \(\sigma_i:L\to L\) are linearly independent over \(L\) as functions. Indeed, choose a nonzero relation \(\sum a_i\sigma_i(x)=0\) for all \(x\), with the fewest nonzero coefficients, and normalize one coefficient to \(1\). Evaluating at \(xy\) and subtracting \(\sigma_j(y)\) times the relation at \(x\), for a \(y\) on which two of the homomorphisms differ, produces a shorter nonzero relation, a contradiction.

Put \(m=|H|\), \(F=L^H\). Independence says that some \(m\) evaluation columns \((\sigma(x_j))_{\sigma\in H}\) are independent over \(L\). Those \(x_j\) are independent over \(F\), so \([L:F]\ge m\). Conversely, take any \(m+1\) elements of \(L\). Their evaluation columns have a nonzero relation over \(L\). Choose one with smallest support and normalize one nonzero coefficient to \(1\). Applying \(\tau\in H\) to the equations permutes the rows, hence gives another relation with that coefficient \(1\). Subtracting gives a relation with smaller support, so every coefficient is \(H\)-fixed. The identity row now gives an \(F\)-linear dependence. Thus \([L:F]\le m\). The orbit polynomial \(\prod_{y\in Hx}(X-y)\) belongs to \(F[X]\) and has distinct roots in \(L\). Every minimal polynomial over \(F\) therefore splits separably in \(L\). Lemma 0B.1 shows that the full automorphism group has size \([L:F]=m\), so it is \(H\).

For \(L/K\) normal and separable, its fixed field under its full group is \(K\), by this equality of degrees. If \(M\) is intermediate, \(L/M\) is still normal and separable, and the same argument gives \(L^{\operatorname{Gal}(L/M)}=M\). Applying the first paragraph to a subgroup gives the other inverse. Conjugating a subgroup conjugates its fixed field. Therefore a normal subgroup fixes a normal separable intermediate field; restriction to that field is onto by Lemma 0B.1 and has that subgroup as kernel, proving the quotient assertion. \(\square\)

## 0C. Profinite groups and infinite Galois theory

A **profinite group** is an inverse limit of finite discrete groups. Products of finite discrete sets are compact and Hausdorff. Here is the compactness argument, to specify the topology being used: an ultrafilter on the product chooses exactly one part of each finite coordinate partition. The selected coordinate values form a point, and every basic cylinder around it belongs to the ultrafilter. Hence every ultrafilter converges. If an open cover had no finite subcover, its closed complements would generate a proper filter; extending it to an ultrafilter would contradict convergence. An inverse limit is closed in the product, because compatibility of two coordinates is a closed condition, so it is compact Hausdorff as well.

Kernels of finitely many coordinate maps have an intersection that is an open normal subgroup. Such intersections form an identity-neighbourhood basis. Any open subgroup of a compact group has finite index, because its open cosets cover the group and admit a finite subcover. A closed subgroup of a profinite group is again profinite: map it to its finite coordinate images; compatibility, closedness and compactness identify it with their inverse limit. A quotient by a closed normal subgroup is likewise the inverse limit of its finite quotients: finite-coordinate cosets separate a point outside that subgroup, and the same compactness argument establishes surjectivity.

**Proposition 0C.1.** Restriction gives
\[
 G_K=\operatorname{Gal}(K^{\mathrm{sep}}/K)
 \simeq\varprojlim_{L/K\text{ finite Galois}}\operatorname{Gal}(L/K).
\]
The topology has an open normal identity-neighbourhood basis given by the kernels of these restrictions. Closed subgroups correspond to intermediate fields; any subgroup has the same fixed field as its closure. Restriction to a Galois intermediate extension is surjective.

**Proof.** Every element of the separable closure lies in a finite Galois extension: adjoin the finitely many roots of its separable minimal polynomial. Composita of finitely many such extensions are still finite Galois, as they are splitting fields of the product of the defining polynomials. A compatible family of finite automorphisms therefore defines a map on the union. Compatibility makes it preserve addition, multiplication and inverses, and the family of inverse automorphisms gives its inverse. This proves the inverse-limit description and the stated topology; compactness and Hausdorffness were proved above. Surjectivity of each restriction, including restriction to an infinite Galois intermediate field, follows from Lemma 0B.1.

If \(H\) is a subgroup, the stabilizer of any element is closed (indeed open), so \(H\) and \(\overline H\) fix the same elements. Suppose \(H\) is closed and \(g\notin H\). A finite restriction \(r_L\) has \(r_L(g)\notin r_L(H)\): otherwise every cylinder about \(g\) meets \(H\), contradicting closedness. Finite Galois theory then finds an element of \(L^{r_L(H)}\) moved by \(g\). This element is fixed by \(H\), so \(\operatorname{Gal}(K^{\mathrm{sep}}/(K^{\mathrm{sep}})^H)=H\). Conversely, if \(M\) is intermediate and \(x\notin M\), its separable minimal polynomial over \(M\) has another root. An embedding moving \(x\) to that root extends by Lemma 0B.1 to an automorphism fixing \(M\). Hence the fixed field of \(\operatorname{Gal}(K^{\mathrm{sep}}/M)\) is exactly \(M\). The proofs also work inside any normal separable algebraic extension of \(K\). \(\square\)

The construction of \(\mathbb Z_\ell\) used here is
\(\varprojlim_a\mathbb Z/\ell^a\mathbb Z\). A nonzero compatible tuple has a least index where it is nonzero; it is uniquely \(\ell^ru\), with \(u\) a unit. This proves that \(\mathbb Z_\ell\) is a discrete valuation ring and that its fraction field is \(\mathbb Q_\ell\). Congruences define its complete topology: a Cauchy sequence eventually has constant value modulo each \(\ell^a\), and those eventual values form its limit. Its residue field is \(\mathbb F_\ell\). The compatible residues of an integer give an injection \(\mathbb Z\hookrightarrow\mathbb Z_\ell\), since a nonzero integer is not divisible by every power of \(\ell\); extending fractions gives \(\mathbb Q\hookrightarrow\mathbb Q_\ell\). The same construction, with a uniformizer in place of \(\ell\), identifies any complete discrete valuation ring \(R\) with \(\varprojlim_aR/\varpi^aR\).

## 0D. Root lifting and factor lifting

**Lemma 0D.1 (simple-root Hensel).** Let \(R\) be complete for the powers of an ideal \(I\), with \(R\simeq\varprojlim R/I^a\). Suppose \(f\in R[X]\), \(f(x_1)\in I\) and \(f'(x_1)\) is a unit. There is a unique root \(x\) of \(f\) congruent to \(x_1\) modulo \(I\), provided elements congruent to \(f'(x_1)\) modulo \(I\) remain units. This proviso holds for a complete local ring and its maximal ideal, and for a complete finite algebra over a complete DVR with \(I\) generated by the base uniformizer.

**Proof.** If \(f(x_a)\in I^a\), put
\[
 x_{a+1}=x_a-f(x_a)/f'(x_a).
\]
The correction is in \(I^a\). The polynomial expansion
\(f(x_a+h)=f(x_a)+f'(x_a)h+h^2c\) puts \(f(x_{a+1})\) in \(I^{2a}\subseteq I^{a+1}\). The derivatives remain units by the hypothesis. The corrections define a Cauchy sequence with a limit \(x\), and polynomial evaluation is continuous, so \(f(x)=0\). If \(x,y\) are congruent roots, then
\(0=f(y)-f(x)=(y-x)(f'(x)+(y-x)c)\), with the second factor a unit, so \(y=x\). In a local ring an element outside the maximal ideal is a unit. In the complete finite algebra, \(1-z\) is invertible for \(z\in I\) by the convergent geometric series; an element whose image modulo \(I\) is a unit is therefore itself a unit. This proves the proviso in both situations. \(\square\)

**Lemma 0D.2 (coprime factor lifting).** Over a complete DVR \(R\), if a monic polynomial \(f\) reduces to \(\bar g\bar h\) with monic coprime factors, then there are unique monic lifts \(g,h\) of these respective degrees with \(f=gh\).

**Proof.** Write \(r=\deg\bar g\), \(s=\deg\bar h\). The residue-field map
\[
 (u,v)\longmapsto u\bar h+\bar gv,
 \quad \deg u<r,\quad\deg v<s,
\]
is an isomorphism onto the polynomials of degree less than \(r+s\). Its kernel is zero: coprimality forces \(\bar g\mid u\) and \(\bar h\mid v\), so both vanish; the source and target dimensions agree. Suppose monic lifts \(g_a,h_a\) give the factorization modulo \(\varpi^a\). Use the isomorphism to express \((f-g_ah_a)/\varpi^a\) modulo \(\varpi\) as \(u\bar h+\bar gv\). Adding \(\varpi^au\) and \(\varpi^av\) to the respective lifts corrects the factorization modulo \(\varpi^{a+1}\), with the same degrees. Completeness gives factors. For uniqueness, if two pairs agree modulo \(\varpi^a\), their difference equation modulo \(\varpi^{a+1}\) has the same zero-kernel map, so they agree modulo \(\varpi^{a+1}\). Induction and separatedness finish the proof. \(\square\)

## 0E. Finite extensions of complete discretely valued fields

**Proposition 0E.1 (existence, uniqueness and completeness of the valuation).** Let \(K\) be complete for a nontrivial discrete valuation, with valuation ring \(R\), uniformizer \(\varpi\) and finite residue field. For a finite separable extension \(F/K\), the integral closure \(S\) of \(R\) in \(F\) is a complete discrete valuation ring with fraction field \(F\) and finite residue field. Its valuation gives the unique absolute value on \(F\) extending that on \(K\). If its uniformizer is \(\pi_F\), its ramification index \(e\) is defined by \(\varpi=u\pi_F^e\). Writing \(f=[S/\pi_FS:R/\varpi R]\), one has
\[
 [F:K]=ef,\qquad
 |x|_F=|N_{F/K}(x)|_K^{1/[F:K]}.
\]
In particular these conclusions apply to every finite extension of \(\mathbb Q_\ell\).

**Proof.** We first justify the finite integral-closure construction. A nontrivially valued field is infinite. A finite separable extension of an infinite field has a primitive element: for two generators \(\alpha,\beta\), its finitely many distinct embeddings can take the same value on \(\alpha+c\beta\) only for finitely many scalars \(c\), unless they agree on both generators. Choose another \(c\). The number of distinct images is then \([K(\alpha,\beta):K]\), by Lemma 0B.1, so \(\alpha+c\beta\) generates this extension. Induct on the number of generators. If \(F=K(\theta)\) and \(\theta_1,\ldots,\theta_n\) are the distinct conjugates, the Vandermonde matrix \((\theta_i^j)_{i,0\le j<n}\) is invertible: its determinant is the nonzero product of their differences, as follows by successively factoring those differences from the alternating determinant. In the power basis the trace pairing has matrix \(V^{\mathsf t}V\); indeed multiplication diagonalizes after the embeddings, and its trace is the sum of the conjugates. Thus the trace pairing is nondegenerate.

Scale a \(K\)-basis of \(F\) by powers of \(\varpi\) so that all its members are integral. This is possible because if \(x\) satisfies a monic equation over \(K\), substitution of \(\varpi^a x\) makes its coefficient of degree \(n-j\) equal to \(\varpi^{aj}\) times the old coefficient, which is integral for sufficiently large \(a\). Those integral basis elements generate an \(R\)-lattice \(T\). If \(z\in S\) and \(t\in T\), then \(zt\) is integral. Its trace is integral, since it is the sum of its integral conjugates, and belongs to \(K\); it therefore lies in \(R\), by integral closedness proved in §0A. It follows that
\[
 T\subseteq S\subseteq T^*=
 \{z\in F:\operatorname{Tr}_{F/K}(zT)\subseteq R\}.
\]
Nondegeneracy identifies \(T^*\) with a full lattice. Lemma 0A.1 now makes \(S\) a finite free \(R\)-module of rank \(n\). Its fraction field is \(F\), and it is complete for the \(\varpi\)-adic topology by an \(R\)-basis. It is integrally closed by transitivity of integrality from §0A.

We next prove that \(S\) is local. All its maximal ideals contain \(\varpi\): for an integral extension, if the upper quotient by a maximal ideal is a field, the lower domain quotient is a field too. To see this, the inverse of a nonzero lower element in the upper field is integral; multiplying its monic equation by the appropriate power of that element expresses the inverse in the lower quotient. The contraction is therefore the unique maximal ideal of \(R\). The ring \(C=S/\varpi S\) is finite. In any finite commutative ring the intersection \(J\) of the maximal ideals is nilpotent. Indeed the descending powers stabilize, say \(J^a=J^{a+1}\); the determinant proof of Nakayama applies to \(J^a\), since every element of \(1+J\) is a unit (otherwise it would lie in some maximal ideal). Hence \(J^a=0\). Distinct maximal ideals and their powers are comaximal: expand \(1=(b+c)^{2a-1}\) with \(b+c=1\) to prove the assertion for their \(a\)-th powers. The Chinese remainder map consequently writes \(C\) as the product of its quotients by sufficiently high powers of its maximal ideals. The map is onto by the same Bezout equations, and its kernel is the product of those powers, namely a power of \(J\), hence zero. If \(C\) had more than one maximal ideal, this product would contain a nontrivial idempotent.

Every idempotent of \(C\) lifts to \(S\): apply Lemma 0D.1 with \(I=\varpi S\) to \(X^2-X\). The derivative \(2x-1\) is invertible modulo \(\varpi\), since its square is \(1\) at an idempotent, and units lift by a geometric series. The domain \(S\) has only the idempotents \(0,1\). Thus \(C\), and hence \(S\), is local. Denote its maximal ideal by \(\mathfrak n\).

Choose a nonzero \(a\in\mathfrak n\), for example \(a=\varpi\). Its monic minimal polynomial over \(K\) has coefficients in \(R\): these are symmetric polynomials in its integral conjugates and belong to the integrally closed base. Its nonzero constant coefficient belongs to \(aS\). Therefore \(S/aS\) is killed by some power of \(\varpi\), and is finite. Its maximal ideal is nilpotent by the preceding finite-ring argument, so \(\mathfrak n^r\subseteq aS\) for some \(r\). Choose the least such positive \(r\), and choose \(b\in\mathfrak n^{r-1}\setminus aS\); if \(r=1\), take \(b=1\). Then \(t=b/a\notin S\) and \(t\mathfrak n\subseteq S\). If \(t\mathfrak n\subseteq\mathfrak n\), the determinant trick applied to the finitely generated nonzero ideal \(\mathfrak n\) would make \(t\) integral over \(S\), contradicting its integral closedness. Hence some \(y\in\mathfrak n\) has \(ty\) a unit. Rescale \(t\) by that unit; then \(ty=1\) and \(t\mathfrak n\subseteq S\), which gives \(\mathfrak n=yS\). Set \(\pi_F=y\).

Repeated division by \(\pi_F\) of a nonzero element terminates. To check this without assuming a valuation, multiplication by \(\pi_F\) on \(C\) is nilpotent, so \(N_{F/K}(\pi_F)\) is divisible by \(\varpi\). Norms of elements of \(S\) belong to \(R\). Thus \(x\in\pi_F^aS\) forces
\(v_K(N(x))\ge a\,v_K(N(\pi_F))\), which bounds \(a\) for \(x\ne0\). Every nonzero element is now uniquely \(\pi_F^a\) times a unit. This supplies a discrete valuation on \(F\), and \(\varpi=u\pi_F^e\) for some \(e>0\). The \(\varpi\)-adic and \(\pi_F\)-adic topologies agree, so \(S\) is complete; a Cauchy sequence in \(F\) is bounded and eventually belongs to a single fractional lattice \(\varpi^{-b}S\), which proves completeness of \(F\). Its residue field is a quotient of the finite ring \(C\).

The absolute value \(|\varpi|_K^{v_F(x)/e}\) extends the base value. For any other extension, an integral element has absolute value at most \(1\), since otherwise the leading term of its monic equation dominates all other terms. A unit of \(S\) and its inverse are both integral, so its value is \(1\); the equation \(\varpi=u\pi_F^e\) fixes the value of \(\pi_F\). Since \(F=S[1/\varpi]\), this proves uniqueness everywhere. Finally \(S/\varpi S\), computed using its free \(R\)-basis, has residue-base dimension \(n\). Computed using the \(e\)-step filtration by \(\pi_F\), that dimension is \(ef\), proving \(n=ef\). Norms of units are units. Taking norms in \(\varpi=u\pi_F^e\) gives \(e\,v_K(N(\pi_F))=n\), so the asserted norm formula follows for a uniformizer, units, and hence every element. \(\square\)

## 0F. Finite residue fields, unramified extensions and Frobenius

**Lemma 0F.1 (finite fields).** In an algebraic closure of \(\mathbb F_q\), the roots of \(X^{q^r}-X\) form a field \(k_r\) with \(q^r\) elements. It is the unique subfield with that cardinality, and
\(\operatorname{Gal}(k_r/\mathbb F_q)\) is cyclic of order \(r\), generated by \(x\mapsto x^q\). Its multiplicative group is cyclic. Every finite extension of \(\mathbb F_q\) is such a field, and every algebraic element belongs to one of them.

**Proof.** The polynomial has derivative \(-1\), hence exactly \(q^r\) distinct roots in its splitting field. Frobenius powers preserve sums and products, so these roots are closed under addition, multiplication and nonzero inverses. They form a field. A field of \(q^r\) elements has every element among these roots: multiplication by a nonzero element permutes its nonzero elements, and taking the product of all those elements gives \(x^{q^r-1}=1\). This proves uniqueness. Its dimension over \(\mathbb F_q\) is \(r\) by cardinality of a vector space. The \(q\)-power map has order exactly \(r\): its \(r\)-th power is the identity, and if its \(d\)-th power were the identity with \(0<d<r\), a polynomial of degree \(q^d\) would have \(q^r\) roots. These \(r\) automorphisms exhaust the group by Lemma 0B.1.

For cyclicity, let \(e\) be the exponent of the finite abelian multiplicative group. For each prime dividing \(e\), choose an element whose order has the largest possible power of that prime, and take its prime-primary part. The product of these commuting elements has order \(e\): coprime orders multiply, as can be checked by raising a purported smaller annihilating power. Every group element is a root of \(X^e-1\), so the group has size at most \(e\); the element of order \(e\) proves the opposite inequality. Hence it generates the group. A finite extension has cardinality \(q^r\), so the earlier root argument identifies it with \(k_r\). Every algebraic element generates a finite extension; consequently their union is the algebraic closure. \(\square\)

**Proposition 0F.2 (unramified lifting).** Let \(K,R,\varpi\) be as in Proposition 0E.1, with residue field \(k=\mathbb F_q\). There is a unique degree-\(r\) unramified subextension \(K_r\) of a fixed separable closure, once its residue field is identified with \(k_r\). Its valuation ring has uniformizer \(\varpi\) and residue field \(k_r\). Reduction gives
\[
 \operatorname{Gal}(K_r/K)\simeq\operatorname{Gal}(k_r/k).
\]
The extensions with \(r\mid s\) are nested. Their union \(K^{\mathrm{nr}}\) has group \(\widehat{\mathbb Z}=\varprojlim_r\mathbb Z/r\mathbb Z\), with arithmetic Frobenius acting as \(x\mapsto x^q\) on the residue algebraic closure. Inertia is the kernel of
\(G_K\to\operatorname{Gal}(K^{\mathrm{nr}}/K)\); equivalently it is the kernel of the action on the residue algebraic closure. In particular, all roots of unity of order prime to the residue characteristic lie in \(K^{\mathrm{nr}}\), and their Frobenius action is the \(q\)-th power.

**Proof.** Choose a generator \(\alpha\) of \(k_r/k\) using Lemma 0F.1, and lift its monic irreducible polynomial to \(f\in R[X]\). This polynomial is irreducible over \(K\): a monic factor over \(K\) has integral coefficients because its roots are integral and its coefficients are symmetric polynomials in them; integral closedness puts these coefficients in \(R\). Reduction of two nonconstant monic factors would contradict irreducibility of \(\bar f\). Thus \(R[X]/(f)=B\) is a domain free over \(R\) of rank \(r\), and \(B/\varpi B=k_r\). The ring \(B\) is complete by its displayed basis. Every element outside \(\varpi B\) is a unit: lift its inverse modulo \(\varpi\), then invert the resulting element of \(1+\varpi B\) by a geometric series. Every nonzero element is \(\varpi^a\) times a unit, since its finitely many basis coordinates are not all divisible by arbitrarily high powers. Thus \(B\) is a DVR, is integrally closed, and is the entire integral closure of \(R\) in its fraction field \(K_r\). Its ramification index is \(1\), so this is an unramified extension.

In \(B\), each conjugate of \(\alpha\) is a simple residue root of \(\bar f\), because finite fields are separable: their Frobenius is bijective, and an irreducible polynomial with zero derivative would be a polynomial in \(X^p\) with all its coefficients \(p\)-th powers, hence a \(p\)-th power. Lemma 0D.1 lifts these distinct roots uniquely. They are all roots of \(f\), so \(K_r\) is Galois. A residue automorphism sends \(\alpha\) to one such conjugate and lifts by sending the generator to its unique root lift. These \(r\) automorphisms prove the reduction isomorphism.

In any finite unramified extension with residue field \(k_r\), Lemma 0D.1 lifts \(\alpha\) to a root of \(f\). The subfield generated by this root has degree \(r\); Proposition 0E.1 gives degree \(r\) for the whole extension, so the fields are equal. This proves uniqueness. If \(r\mid s\), apply the same lifting inside \(K_s\) to obtain the inclusion. Conversely an inclusion of finite residue fields requires divisibility of their dimensions, so these inclusions account for the whole directed system.

Uniqueness of valuations in Proposition 0E.1 makes every \(K\)-automorphism of the separable closure preserve its valuation ring and act on residues. Its residue field is an algebraic closure of \(k\): every finite extension has finite residue field, and the fields \(K_r\) already realize every \(k_r\). An automorphism acts trivially there exactly when it acts trivially on each \(K_r\), by their reduction isomorphisms. Lemma 0B.1 extends an automorphism of their union to the separable closure. Proposition 0C.1 and Lemma 0F.1 therefore give the stated surjective quotient and its compatible arithmetic Frobenius generator.

Finally let \(m\) be prime to the residue characteristic. The polynomial \(X^m-1\) has \(m\) distinct roots in the residue algebraic closure, all in some \(k_r\). Lemma 0D.1 lifts them uniquely inside \(K_r\). They give all \(m\) roots in the separable closure, so inertia fixes them. Frobenius sends a root to a root with residue equal to its \(q\)-th power; that power is itself a root with this residue, so uniqueness identifies them. \(\square\)

## 1. What continuity remembers

For a field \(K\) with a chosen separable closure, write \(G_K=\operatorname{Gal}(K^{\mathrm{sep}}/K)\). Proposition 0C.1 identifies it with the inverse limit of the finite groups \(\operatorname{Gal}(L/K)\), supplies the open normal identity-neighbourhood basis and proves compactness, Hausdorffness and the closed-subgroup correspondence. It also proves why an arbitrary subgroup has the same fixed field as its closure.

A continuous homomorphism from a compact group to a discrete group has finite image: the inverse images of singleton elements of its image form an open cover, so compactness leaves only finitely many of them. Its kernel is open, and it factors through that finite quotient. Thus a representation over a finite field, with its discrete topology, factors through a finite quotient. A complex matrix group has a different topology, but an analogous conclusion follows from a special property of that topology.

**Lemma 1.1 (no small subgroups).** In the operator norm on \(M_n(\mathbb C)\), the set
\[
 U=\{A\in\operatorname{GL}_n(\mathbb C):\|A-1\|<1/2\}
\]
contains no subgroup other than \(\{1\}\).

**Proof.** Suppose every integral power of \(A\) belongs to \(U\). If \(Av=\lambda v\) with \(v\ne0\), then
\(\|(A^m-I)v\|=|\lambda^m-1|\|v\|\le\|A^m-I\|\|v\|\), so \(|\lambda^m-1|<1/2\) for every integer \(m\). Eigenvalues exist by the complex polynomial argument of §0A. If \(|\lambda|>1\), positive powers contradict this inequality; if \(|\lambda|<1\), negative powers do. Thus \(|\lambda|=1\).

If \(\lambda\ne1\), replace \(\lambda\) by its inverse if necessary and write \(\lambda=e^{i\theta}\), with \(0<\theta\le\pi\). Choose the least positive integer \(m\) with \(m\theta\ge\pi/2\). Then \(\pi/2\le m\theta<3\pi/2\), apart from a harmless possible endpoint, so \(|\lambda^m-1|\ge\sqrt2\). This too is impossible. Every eigenvalue is therefore \(1\).

Write \(A=1+B\), where \(B\) is nilpotent. If \(B\ne0\), let \(r\ge1\) be the largest integer with \(B^r\ne0\). For positive integers \(m\),
\[
 A^m-1=\sum_{j=1}^r\binom mj B^j.
\]
At least one matrix entry is a polynomial in \(m\) of degree \(r\) with nonzero leading coefficient. It is unbounded, contradicting \(\|A^m-1\|<1/2\). Hence \(A=1\). Apply this argument to each element of a subgroup contained in \(U\). \(\square\)

**Theorem 1.2.** A continuous representation \(\rho:G\to\operatorname{GL}_n(\mathbb C)\) of a profinite group has open kernel and finite image.

**Proof.** The inverse image of \(U\) is a neighbourhood of the identity. It contains an open normal subgroup \(H\). The subgroup \(\rho(H)\) lies in \(U\), so Lemma 1.1 gives \(H\subset\ker\rho\). The index of an open subgroup of a compact group is finite: its cosets form an open cover, which has a finite subcover. Thus \(\rho\) factors through the finite group \(G/H\). \(\square\)

Such a representation of an absolute Galois group is an **Artin representation**. The corresponding assertion fails for \(\operatorname{GL}_n(E)\): for each positive \(a\), the congruence subgroup \(1+\pi^aM_n(\mathcal O)\) is a nontrivial subgroup inside a small neighbourhood of the identity. The topology permits infinite compact images.

## 2. Bringing an ℓ-adic representation into integral coordinates

**Theorem 2.1 (stable lattice).** Let \(G\) be a compact topological group and let \(\rho:G\to\operatorname{GL}(V)\) be continuous, with \(V\) finite dimensional over \(E\). There is a lattice \(L\subset V\) satisfying \(\rho(g)L=L\) for every \(g\in G\).

**Proof.** Choose any lattice \(L_0\). Its stabilizer in \(\operatorname{GL}(V)\) is open: in an \(\mathcal O\)-basis it is \(\operatorname{GL}_n(\mathcal O)\), which contains \(1+\pi M_n(\mathcal O)\). The latter is an identity neighbourhood of invertible matrices: its determinants reduce to \(1\), and the adjugate gives integral inverses. Translating this neighbourhood by every element of the stabilizer proves openness. Its inverse image \(H\subset G\) is an open subgroup, hence has finite index by §0C. Choose representatives \(g_1,\dots,g_t\) for \(G/H\), and set
\[
 L=\sum_{j=1}^t\rho(g_j)L_0.
\]
This is the sum of the entire finite orbit of \(L_0\), so \(G\) preserves it. It is finitely generated over \(\mathcal O\), torsion free, and spans \(V\). Lemma 0A.1 proves its freeness and that its rank is \(\dim_EV\). Thus it is a lattice. \(\square\)

In a basis of \(L\), the representation takes values in \(\operatorname{GL}_n(\mathcal O)\). Reduction gives
\[
 \bar\rho_L:G\longrightarrow\operatorname{GL}(L/\pi L).
\]
Its image is finite. More generally every quotient \(L/\pi^aL\) is finite by Lemma 0A.1. Reduction is continuous because its congruence kernel is open. The equality \(\mathcal O=\varprojlim_a\mathcal O/\pi^a\mathcal O\), proved in §0C using completeness from Proposition 0E.1, gives \(L=\varprojlim_a L/\pi^aL\) in a basis. Hence the original integral action is precisely their inverse limit.

For a finite-dimensional representation \(W\), a **composition series** is a filtration by invariant subspaces with simple successive quotients. Lemma 0A.2 proves that their isomorphism classes, with multiplicity, do not depend on the series. Their direct sum is the **semisimplification** \(W^{\mathrm{ss}}\). Semisimplification forgets extensions, and consequently it need not recover \(W\).

**Theorem 2.2 (independence of the lattice).** For two stable lattices \(L,L'\) in the same representation, there is an isomorphism
\[
 (L/\pi L)^{\mathrm{ss}}\simeq(L'/\pi L')^{\mathrm{ss}}.
\]

**Proof.** Multiplication by a power of \(\pi\) identifies a lattice with a scaled lattice as a \(G\)-module, and induces an isomorphism of its reductions. Lemma 0A.1 proves commensurability, so scale \(L'\) until \(L'\subset L\). Put \(Q=L/L'\), a finite-length \(\mathcal O\)-module carrying a \(G\)-action.

Apply multiplication by \(\pi\) to the exact sequence \(0\to L'\to L\to Q\to0\). Because multiplication by \(\pi\) is injective on each lattice, the kernel-and-cokernel sequence is
\[
 0\longrightarrow Q[\pi]\longrightarrow L'/\pi L'
 \longrightarrow L/\pi L\longrightarrow Q/\pi Q\longrightarrow0.
 \tag{1}
\]
For clarity, the first map sends \(q\in Q[\pi]\), lifted to \(x\in L\), to \(\pi x\bmod\pi L'\). It is well-defined and injective: changing the lift changes \(\pi x\) by \(\pi L'\), and \(\pi x\in\pi L'\) implies \(x\in L'\). Its image is exactly the kernel of the next map, because that kernel is \((L'\cap\pi L)/\pi L'\). The last map is induced by \(L\to Q\); its kernel is \((L'+\pi L)/\pi L\). This proves (1) directly, without an unproved exact-sequence lemma.

Every module in (1) is a finite-dimensional \(k\)-representation. The two end terms have the same composition factors. In the category of finite-length \(\mathcal O\)-modules with compatible \(G\)-action, Lemma 0A.2 proves Jordan–Hölder, exact-sequence additivity and that every simple object is killed by \(\pi\). The exact sequence
\[
 0\to Q[\pi]\to Q\xrightarrow{\pi}Q\to Q/\pi Q\to0
\]
therefore gives equality of the multiplicities of every simple \(k[G]\)-module in \(Q[\pi]\) and \(Q/\pi Q\). Taking composition factors in (1) now proves the assertion. \(\square\)

This proof uses exact sequences rather than character theory. The characteristic-polynomial route is also valid, and is proved in Theorem 2.4 below. For lattice reductions the polynomials agree because they reduce \(\det(X-\rho(g))\). In positive characteristic, ordinary traces alone do not suffice. For example, in characteristic \(\ell\), the trivial representation of dimension \(\ell\) and the zero representation both have trace zero at every group element but have different dimensions and characteristic polynomials. Even with the same dimension, traces can fail: over \(\mathbb F_3\), take a group of order \(2\) and compare three copies of its trivial character with three copies of its sign character. Both traces vanish, whereas at the nonidentity element their characteristic polynomials are \((X-1)^3\) and \((X+1)^3\).

**Example 2.3 (an extension can disappear).** The additive group \(\mathbb Z_\ell\) acts on \(E^2\) by
\[
 \rho(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\]
The lattice \(L=\mathcal Oe_1+\mathcal Oe_2\) is stable. Its reduction is a nonsplit extension of the trivial character by itself: \(\rho(1)\) is nonidentity unipotent. The lattice \(L'=\mathcal Oe_1+\mathcal O(\pi e_2)\) is also stable. In its displayed basis the upper-right entry is \(\pi t\), so its reduction is the two-dimensional trivial representation. Both semisimplifications are \(1\oplus1\).

**Theorem 2.4 (characteristic-polynomial Brauer–Nesbitt).** Let \(F\) be any field, \(G\) any group, and \(V,W\) finite-dimensional semisimple \(F\)-representations. If the characteristic polynomials of \(g\) on \(V,W\) agree for every \(g\in G\), then \(V\simeq W\). For arbitrary representations the same condition identifies their semisimplifications.

**Proof.** There are two points to prove: group elements must determine the characteristic polynomials of all elements of their generated algebra, and those algebra polynomials must determine the simple multiplicities. Ordinary traces cannot supply the first point in small characteristic.

For matrices \(A_1,\ldots,A_s\) of the same size, use commuting variables \(t_1,\ldots,t_s\). A word is a nonempty sequence in the alphabet \(1,\ldots,s\); it is primitive if it is not a proper power. Choose one representative of each primitive word up to cyclic rotation. Put \(A_w=A_{i_1}\cdots A_{i_d}\), \(t_w=t_{i_1}\cdots t_{i_d}\). The identity
\[
 \det\left(I-\sum_i t_iA_i\right)
 =\prod_{w\ \mathrm{primitive\ cyclic}}
       \det(I-t_wA_w)
 \tag{2}
\]
holds in the ring of formal power series. The product is well-defined because only finitely many words affect any fixed total degree. Here is a proof in every characteristic. First give each matrix entry an independent indeterminate over \(\mathbb Z\) and work over \(\mathbb Q\). The formal identity
\[
 \log\det(I-zB)=-\sum_{m\ge1}\frac{z^m}{m}\operatorname{tr}(B^m)
 \tag{3}
\]
follows by differentiating: the adjugate formula for the derivative of a determinant gives
\(-\operatorname{tr}(B(I-zB)^{-1})\); expand the inverse as a geometric series and integrate, using constant term zero. This uses only formal series over \(\mathbb Q\).

Apply (3) to \(B=\sum t_iA_i\). In the trace expansion each word of length \(m\) occurs once. Every cyclic word has a unique primitive cyclic root \(w\), say of length \(d\), and is its \(r\)-th power with \(m=dr\). This is the elementary periodicity of a circular sequence: its rotations fixing it form a subgroup of the cyclic rotation group, whose least positive shift is the length of its primitive root. There are exactly \(d\) distinct linear rotations. Traces are invariant under cyclic rotation, since \(\operatorname{tr}(AB)=\operatorname{tr}(BA)\) follows by expanding the diagonal entries. Thus the coefficient \(1/m\) on that cyclic class becomes \(d/m=1/r\). Grouping gives the sum of the logarithms \(\log\det(I-t_wA_w)\), proving (2) over \(\mathbb Q\). Both sides of (2), degree by degree, have integral polynomial coefficients in the generic matrix entries. The injection of that integer polynomial ring into its rational extension shows the coefficients are equal over \(\mathbb Z\). Specializing gives (2) over any field, including positive characteristic. This proves the determinant identity used here without importing the word-factorization theorem in the freely accessible primary paper [Reutenauer–Schützenberger 1987, equation (6)].

Now take \(A_i\) to be the operators of finitely many group elements \(g_i\). Every \(A_w\) is the operator of a group element, so the hypothesis makes the right side of (2) identical for \(V,W\). Substitute \(t_i=za_i\) for any \(a_i\in F\). The left sides are polynomials in \(z\), and their equality says that every group-algebra element \(a=\sum a_i g_i\) has the same characteristic polynomial on \(V,W\). Their dimensions already agree by the hypothesis at the identity. Thus all elements of the finite-dimensional image algebra
\(A\subseteq\operatorname{End}_F(V)\oplus\operatorname{End}_F(W)\)
have equal characteristic polynomials on the two modules.

We prove the required algebra assertion. A submodule of a finite direct sum of simple modules has a complement: choose a direct sum \(C\) of simple submodules disjoint from it, with the largest possible dimension. If their sum is not the whole module, one of the original simple summands is not contained in the sum, so meets it trivially and can be added to \(C\), a contradiction. A quotient is semisimple too, because the images of the simple summands span it and are simple or zero; successively discard any summand already in their span. This also proves that the submodule, identified with a quotient by its complement, is semisimple.

The faithful semisimple module \(M=V\oplus W\) embeds the left regular module \({}_AA\) in a finite direct sum of copies of \(M\): send \(a\) to \((am_j)_j\) for a vector-space basis \((m_j)\) of \(M\). This is injective and \(A\)-linear. Hence \({}_AA\) is semisimple by the preceding paragraph. Write
\(A\simeq\bigoplus_i S_i^{r_i}\) as a left module with pairwise nonisomorphic simples. A map between distinct simples is zero, and a nonzero endomorphism of a simple is invertible, because its kernel and image are submodules. Thus its endomorphism algebra is the product of matrix algebras over the division rings \(\operatorname{End}_A(S_i)\). On the other hand, every endomorphism of \({}_AA\) is right multiplication by its value at \(1\), so this algebra is \(A^{\mathrm{op}}\). The projections onto the isotypic summands are central idempotents in this endomorphism algebra, hence are right multiplication by central idempotents \(e_i\in A\). They are also left multiplication by \(e_i\).

Each simple \(A\)-module appearing in \(M\) is one of these \(S_i\): a nonzero vector gives a surjection \(A\to S\). Such a map kills all different isotypic summands. Applying it to \(e_j a\) shows that \(e_j\) acts as the identity on \(S_j\) and zero on every other \(S_i\). If \(S_i\) occurs with multiplicity \(m_i\) in \(V\), then
\[
 \det(X-e_i\mid V)
 =(X-1)^{m_i\dim_FS_i}X^{\dim_FV-m_i\dim_FS_i}.
\]
The same formula for \(W\) and equality of these polynomials identify the exponents, because \(X\) and \(X-1\) are distinct coprime linear factors in every field. Therefore every multiplicity agrees, proving \(V\simeq W\). Finally a basis adapted to a composition series makes an operator block triangular, so its characteristic polynomial is the product of those on the simple factors. Replacing arbitrary representations by their semisimplifications does not change it; Lemma 0A.2 then supplies the last assertion. \(\square\)

## 3. Roots of unity and Tate twists

The \(m\)-th roots of unity in a characteristic-zero algebraic closure form a cyclic group of order \(m\). The polynomial \(X^m-1\) has exactly \(m\) distinct roots; cyclicity follows by the exponent-and-root-count argument in Lemma 0F.1, which works for any finite subgroup of a field's multiplicative group. Choose a primitive \(\ell\)-th root. Given a primitive \(\ell^a\)-th root, any \(\ell\)-th root of it has order \(\ell^{a+1}\), since raising it to \(\ell\) has order \(\ell^a\). This inductively gives compatible primitive roots \(\zeta_{\ell^a}\), with \(\zeta_{\ell^{a+1}}^\ell=\zeta_{\ell^a}\). The actions
\[
 g(\zeta_{\ell^a})=\zeta_{\ell^a}^{\chi_{\ell,a}(g)}
\]
define compatible characters with values in \((\mathbb Z/\ell^a\mathbb Z)^\times\). Their inverse limit is the **cyclotomic character**
\[
 \chi_\ell:G_{\mathbb Q}\longrightarrow\mathbb Z_\ell^\times.
\]
It is continuous because each finite-level character has open kernel by Proposition 0C.1. Its values are units since an automorphism preserves the order of a primitive root, and compatibility follows by applying the automorphism to the displayed power relation.

**Lemma 3.0 (cyclotomic surjectivity).** The image of \(\chi_\ell\) is all of \(\mathbb Z_\ell^\times\).

**Proof.** For \(a\ge1\), the primitive \(\ell^a\)-th roots have polynomial
\[
 \Phi_{\ell^a}(X)=\sum_{j=0}^{\ell-1}X^{j\ell^{a-1}}.
\]
Indeed multiplying by \(X^{\ell^{a-1}}-1\) gives \(X^{\ell^a}-1\), so its roots are exactly those of order \(\ell^a\). Modulo \(\ell\),
\(\Phi_{\ell^a}(1+T)=T^{\ell^{a-1}(\ell-1)}\): the identity \((1+T)^{\ell^b}=1+T^{\ell^b}\) follows from the binomial theorem and induction, and substitution in the geometric sum gives this formula. Its constant coefficient is \(\ell\), so is not divisible by \(\ell^2\), whereas all nonleading coefficients are divisible by \(\ell\).

This makes the polynomial irreducible over \(\mathbb Q\), by the following direct Eisenstein argument. A monic polynomial over \(\mathbb Z\) can have a monic factorization over \(\mathbb Q\) only with factors in \(\mathbb Z[T]\): their coefficients are rational symmetric polynomials in integral roots, hence integral by the finite-module argument of §0A; an integral rational number is an integer, since a monic equation for \(c/d\) in lowest terms forces \(d\mid c^n\). Reducing two proposed nonconstant monic factors of the displayed polynomial modulo \(\ell\) would make each a positive power of \(T\), so both constant coefficients would be divisible by \(\ell\), contradicting their product's divisibility by exactly one power. Translation \(X=1+T\) preserves factorization, hence \(\Phi_{\ell^a}\) is irreducible too.

The field \(\mathbb Q(\zeta_{\ell^a})\) contains every \(\ell^a\)-th root and is Galois by Lemma 0B.1. Irreducibility gives degree \(\ell^{a-1}(\ell-1)\), equal to the number of units modulo \(\ell^a\). The injective exponent map of its Galois group is thus onto those units. A compatible tuple of units defines compatible automorphisms of this increasing cyclotomic union by \(\zeta_{\ell^a}\mapsto\zeta_{\ell^a}^{u_a}\). Lemma 0B.1 extends the resulting automorphism to \(\mathbb Q^{\mathrm{sep}}\), giving the tuple as a value of \(\chi_\ell\). \(\square\)

**Proposition 3.1.** At every prime \(p\ne\ell\), the character \(\chi_\ell\) is unramified and
\[
 \chi_\ell(\operatorname{Frob}_p)=p.
\]

**Proof.** To define the local restriction, choose an embedding of \(\mathbb Q^{\mathrm{sep}}\) into an algebraic closure of \(\mathbb Q_p\); extend a partial embedding by the argument of Lemma 0B.1. Every local automorphism preserves this embedded field, because it permutes the roots of each polynomial over \(\mathbb Q\). Its restriction therefore acts on the cyclotomic roots. Proposition 0F.2, applied with \(m=\ell^a\) and residue cardinality \(p\), proves that these roots lie in the unramified union, are fixed by inertia, and are sent to their \(p\)-th powers by arithmetic Frobenius. Thus \(\chi_{\ell,a}(\operatorname{Frob}_p)=p\bmod\ell^a\). Changing the Frobenius lift by inertia has no effect. Taking the inverse limit proves the assertion, with the integer \(p\) identified with its compatible residue tuple in \(\mathbb Z_\ell^\times\). \(\square\)

The one-dimensional representation \(E(1)\) is the space \(E\) with action \(\chi_\ell\). For an integer \(m\), define \(E(m)\) using \(\chi_\ell^m\), including negative powers, and write \(V(m)=V\otimes_EE(m)\). In particular,
\[
 \operatorname{tr}(\operatorname{Frob}_p\mid E(m))=p^m
 \quad(p\ne\ell).
\]
These twists have infinite image unless \(m=0\). Indeed Lemma 3.0 supplies elements with cyclotomic values \((1+\ell)^r\), \(r\ge1\). If \(m\ne0\), their \(m\)-th powers are distinct rational numbers, and §0C gives the injection \(\mathbb Q\hookrightarrow\mathbb Q_\ell\hookrightarrow E\). If \(E(m)\simeq E(n)\), an invertible map between their one-dimensional spaces forces equality of their characters. Evaluating at any prime \(p\ne\ell\) gives \(p^{m-n}=1\) in \(E\), hence \(m=n\) by the same rational injection. Such a prime exists, for example \(2\) unless \(\ell=2\), in which case take \(3\).

**Example 3.2 (a quadratic character).** Let \(\eta(g)\) be the sign determined by \(g(i)=\eta(g)i\). It factors through \(\operatorname{Gal}(\mathbb Q(i)/\mathbb Q)\). For an odd prime, \(i^p=i\) if \(p\equiv1\pmod4\), and \(i^p=-i\) if \(p\equiv3\pmod4\). Thus
\[
 \eta(\operatorname{Frob}_p)=
 \begin{cases}1,&p\equiv1\pmod4,\\-1,&p\equiv3\pmod4.\end{cases}
\]
This is the Dirichlet character \(\chi_{-4}\): it is the multiplicative character of \((\mathbb Z/4\mathbb Z)^\times\) sending \(1\) to \(1\) and \(3\) to \(-1\), extended by zero on even integers. Multiplicativity follows by multiplying the two residue classes. Proposition 0F.2 with \(m=4\) proves that it is unramified at every odd prime. At \(2\), \(i\notin\mathbb Q_2\): an integral square is congruent to \(0\) or \(1\pmod4\), as follows by squaring its residue classes, whereas \(-1\equiv3\pmod4\). Thus \(\mathbb Q_2(i)/\mathbb Q_2\) has degree \(2\). The identity \((i-1)^2=-2i\), with \(i\) a unit, gives \(v_2(i-1)=1/2\) for the uniquely extended base-normalized valuation from Proposition 0E.1. Hence its ramification index is \(2\), its residue degree is \(1\), and its full nontrivial quadratic group is inertia by Proposition 0F.2 and the fixed-field correspondence. This proves ramification at \(2\).

The more general assertion is Kronecker–Weber: finite-order continuous characters of \(G_{\mathbb Q}\) correspond to Dirichlet characters, with an unramified arithmetic Frobenius evaluated as \(\chi(p)\). An actual programme proof is *Kronecker–Weber and the maximal abelian extension of the rationals*, Theorem 20.2 and Proposition 20.5. These are written proofs, rather than future lesson titles: Theorem 20.2 uses Proposition 20.1 and the earlier ray-field theorem, and Proposition 20.5 passes to characters. That ray-field theorem and its prerequisites are not checked in this lesson; the dependency note at the end records this. The quadratic calculation above, the cyclotomic surjectivity proof and every representation theorem here use none of that classification.

### 3A. An explicit arithmetic pair of lattices

We now prove the elliptic example at this point. The geometric prerequisites are actual earlier programme proofs in *Abelian varieties*: Corollary 2.3 proves that a morphism taking identity to identity is a homomorphism; Theorems 6.1–6.2 prove that multiplication by an integer prime to the characteristic has degree its square on an elliptic curve and is finite étale; Proposition 6.3 and Theorem 6.8 construct the finite étale quotient by a finite translation subgroup; Theorems 6.7 and 7.1–7.2 prove reverse isogenies, finite torsion structure and torsion transition maps; Theorem 9.0 constructs the cubic group law; Lemma 9.11 proves curve Riemann–Roch and duality; Example 9.12 embeds a genus-one group curve as a pointed cubic. The precise written scopes were inspected. The following argument supplies the specific isogeny, pairing and inertia comparison, without importing them from a later LG-GAL lesson.

**Lemma 3.3 (the torsion pairing needed here).** For an elliptic curve \(A/\mathbb Q\), put
\[
 T_5A=\varprojlim_n A[5^n](\overline{\mathbb Q}),
 \qquad V_5A=T_5A\otimes_{\mathbb Z_5}\mathbb Q_5,
\]
where the transition is multiplication by five. Then \(T_5A\) is free of rank two, its reduction is canonically \(A[5]\), and \(\det(A[5])=\bar\chi_5\). A rational isogeny identifies the rational Tate modules.

**Proof.** The earlier multiplication and torsion proofs give
\(A[5^n]\simeq(\mathbb Z/5^n)^2\), with surjective transitions. One can see the inverse limit directly: lift a basis at level one successively through these transitions. A lift of a basis at level \(n\) generates level \(n+1\), since subtracting a combination of its two lifts leaves an element of the kernel \(A[5]\), generated by their \(5^n\)-multiples. Their orders are \(5^{n+1}\), so counting \(5^{2n+2}\) elements makes them a basis. Coherent coefficients give \(T_5A\simeq\mathbb Z_5^2\). Projection to level one is onto. If a coherent tuple \((P_n)\) has \(P_1=0\), then \(Q_n=P_{n+1}\) belongs to \(A[5^n]\), is coherent and satisfies \(5Q_n=P_n\). Thus the projection's kernel is precisely \(5T_5A\). All these maps commute with Galois. Continuity follows because the action on each finite set factors through the splitting field of its finitely many algebraic coordinates.

We construct the required alternating perfect pairing rather than assuming its determinant consequence. Work over \(\overline{\mathbb Q}\). On a smooth projective group curve \(C\), a nonzero cotangent vector at its identity translates to a nowhere vanishing differential: the differential of multiplication trivializes the cotangent line by translation, with inverse provided by translation by the negative point. Its canonical line bundle is therefore trivial. The earlier Riemann–Roch proof gives \(h^0(D)=\deg D\) for a divisor of positive degree: the dual divisor \(-D\) has no nonzero section, since an effective divisor cannot have negative degree. It also shows that every degree-zero class is \([(R)-(O)]\): add \((O)\), obtain an effective divisor of degree one, hence a point. Uniqueness follows because \(h^0((O))=1\); a principal divisor \((R)-(O)\), with \(R\ne O\), would give a nonconstant function with its only pole a simple pole at \(O\). The earlier cubic law agrees with addition of these point classes. For a finite translation quotient \(B\), its smooth proper group-curve structure and the same differential argument give genus one. Example 9.12 embeds \(B\) by \(|3O|\) as a smooth cubic with identity flex. Corollary 2.3 applied to the identity map between this pointed cubic and the existing quotient group identifies their group laws. Thus addition of point classes on \(B\) agrees with the quotient law used below.

For \(Q\in A[5]\), let \(D_Q=(Q)-(O)\). The degree-zero divisor \([5]^*D_Q\) is principal. Indeed choose \(R\) with \(5R=Q\); its positive fibre has points \(R+U\), \(U\in A[5]\). Their sum is \(25R+\sum_U U=5Q=O\), since the torsion points pair as \(U,-U\). The negative fibre has sum zero too. Choose a rational function \(g_Q\) with this divisor and define
\[
 e_5(P,Q)=\frac{g_Q(X)}{g_Q(X+P)},\qquad P,Q\in A[5].
 \tag{3A.1}
\]
The quotient has zero divisor and hence is constant: on a projective curve a regular function is constant, as follows also from \(h^0(0)=1\). Multiplying \(g_Q\) by a scalar leaves the ratio unchanged. Translation composes ratios, proving multiplicativity in \(P\); five repetitions give \(e_5(P,Q)^5=1\). If \(D_Q+D_{Q'}-D_{Q+Q'}=\operatorname{div}(h)\), then \(g_Qg_{Q'}/g_{Q+Q'}\) is a scalar multiple of \(h\circ[5]\). This function is invariant under translation by \(P\), proving multiplicativity in \(Q\). Applying a field automorphism to this construction proves Galois equivariance, including the action on \(\mu_5\).

If \(e_5(P,Q)=1\) for all \(P\), then \(g_Q\) is invariant under the 25 translations in \(A[5]\). They are distinct automorphisms over the subfield \([5]^*\overline{\mathbb Q}(A)\), whose extension degree is 25. The finite fixed-field theorem of §0B identifies that invariant subfield with the displayed one. Thus \(g_Q=h\circ[5]\). Equality of divisors and injectivity of pullback of divisors show \(D_Q=\operatorname{div}(h)\): each fibre is nonempty and its multiplicities are positive, so pullback cannot kill a nonzero coefficient. The point-class injectivity just proved gives \(Q=O\). Hence \(Q\mapsto e_5(-,Q)\) is an injection into the character group of \((\mathbb Z/5)^2\), which has 25 elements; it is a bijection.

For alternation, take nonzero \(P\) and form the earlier finite étale quotient \(\beta:A\to B=A/\langle P\rangle\) of degree five. Multiplication by five factors as \([5]=v\beta\), with \(v:B\to A\) of degree five. Choose \(R\) with \(5R=P\). The five points in the fibre of \(v\) over \(P\) have sum \(5\beta R+\sum_{U\in\ker v}U=\beta P=O\); the fibre over \(O\) has sum zero. Consequently \(v^*D_P\) is principal on \(B\), by the preceding degree-zero class argument. Its function pulls back to a possible \(g_P\) on \(A\), which is invariant under translation by \(P\). Formula (3A.1) gives \(e_5(P,P)=1\), also true for \(P=O\). Bilinearity then gives \(e_5(P,Q)=e_5(Q,P)^{-1}\), so the pairing is alternating and perfect.

For an \(\mathbb F_5\)-basis \(P,Q\), perfection makes \(e_5(P,Q)\) a primitive fifth root. If \(g\) has matrix \(M\) on this basis, bilinearity and alternation give
\(e_5(gP,gQ)=e_5(P,Q)^{\det M}\). Galois equivariance makes the same value \(e_5(P,Q)^{\bar\chi_5(g)}\). Therefore \(\det M=\bar\chi_5(g)\).

Finally let \(\phi:A\to A'\) be a rational isogeny. The earlier reverse-isogeny proof supplies \(\psi:A'\to A\) and an integer \(d\ne0\) such that \(\psi\phi=[d]\) and \(\phi\psi=[d]\). On the torsion inverse limits these equations persist. After tensoring with \(\mathbb Q_5\), \(d^{-1}T_5\psi\) is the inverse of \(T_5\phi\). This proves the rational identification. \(\square\)

**Example 3.4 (rationally identical, integrally different).** The two curves
\[
 E_1:y^2+y=x^3-x^2-10x-20,
 \qquad E_2:y^2+y=x^3-x^2
 \tag{3A.2}
\]
have a degree-five rational isogeny, isomorphic \(V_5\), and nonisomorphic reductions of their integral \(T_5\). Both reductions have semisimplification \(1\oplus\bar\chi_5\).

We give the complete comparison. The cubics are smooth: for \(Y=2y+1\) their equations are \(Y^2=D(x)\), where \(D=4(x^3-x^2+a_4x+a_6)+1\), and in each case \(\gcd(D,D')=1\); at infinity their unique point \(O=[0:1:0]\) is smooth. The cubic group-law proof therefore applies. A secant of slope \(\lambda\) and intercept \(\nu\) gives
\[
 x(P+Q)=\lambda^2+1-x(P)-x(Q),\qquad
 y(P+Q)=-\lambda x(P+Q)-\nu-1,
\]
because substituting its line equation into the cubic gives the three intersection roots, and inversion is \((x,y)\mapsto(x,-y-1)\). For doubling the slope is \((3x^2-2x+a_4)/(2y+1)\), by differentiating the equation. Thus \(P_2=(0,0)\) on \(E_2\) satisfies \(2P_2=(1,-1)\), \(3P_2=(1,0)\), \(4P_2=(0,-1)\), \(5P_2=O\). On \(E_1\), \(P_1=(5,5)\) similarly has double \((16,-61)\), triple \((16,60)\), fourth multiple \((5,-6)\), and fifth multiple \(O\). These are rational points of exact order five.

On \(E_2\), define the rational map \(\phi=(X,Y)\) by
\[
 X=\frac{x^5-2x^4+3x^3-2x+1}{x^2(x-1)^2},
\]
\[
 Y=\frac{x^6y-3x^5y+x^4y-x^4-3x^3y-x^3
             +6x^2y+3x^2-6xy-3x+2y+1}{x^3(x-1)^3}.
 \tag{3A.3}
\]
Here is an algebraic verification of the map, without assuming a general isogeny formula. For \(S=\{(0,0),(0,-1),(1,0),(1,-1)\}\), compute
\(X=x+\sum_{Q\in S}(x(P+Q)-x(Q))\) and
\(Y=y+\sum_{Q\in S}(y(P+Q)-y(Q))\) using the displayed secant formulas. Reduction by \(y^2+y=x^3-x^2\) yields (3A.3). Substitution and the same reduction give the polynomial identity
\[
 Y^2+Y-X^3+X^2+10X+20=0.
\]
For example, this identity can be checked by multiplying by \(x^6(x-1)^6\), then replacing every \(y^2\) by \(x^3-x^2-y\); the constant and linear coefficients in \(y\) both vanish. Thus the image is \(E_1\). A rational map from a smooth curve to a projective curve extends at every point: scale its projective coordinates in the local DVR so that all are integral and at least one is a unit. The defining homogeneous equations remain zero, and these extensions glue by equality in the function field. At \(O\), \(x\) and \(y\) have poles of orders two and three; the leading terms of (3A.3) are \(x,y\), so \(\phi(O)=O\). The earlier Corollary 2.3 makes it a homomorphism. The numerator and denominator of \(X\) are coprime, and their degrees are five and four. Hence the rational function \(X\) on the \(x\)-line has degree five. Both elliptic \(x\)-maps have degree two, so multiplicativity of function-field degrees gives \(2\deg\phi=2\cdot5\), and \(\deg\phi=5\). Lemma 3.3 identifies \(V_5E_1\) and \(V_5E_2\).

To distinguish the reductions, we compute their fifth torsion at 11 directly. For either equation in (3A.2), put
\[
 b_2=-4,\quad b_4=2a_4,\quad b_6=1+4a_6,
 \quad b_8=-4a_6-1-a_4^2,
\]
\[
 B=3x^4+b_2x^3+3b_4x^2+3b_6x+b_8,
\]
\[
 C=2x^6+b_2x^5+5b_4x^4+10b_6x^3+10b_8x^2
                 +(b_2b_8-b_4b_6)x+b_4b_8-b_6^2,
 \qquad H=D^2C-B^3.
\]
The doubling slope above gives \(x(2P)=x-B/D\). To compute \(x(3P)\), set \(x_2=x-B/D\),
\(y_2=-\lambda x_2-y+\lambda x-1\), and use the secant slope \((y_2-y)/(x_2-x)\); clearing denominators and the curve equation gives \(x(3P)=x-DC/B^2\). Consequently
\[
 x(3P)-x(2P)=-\frac{H(x)}{D(x)B(x)^2}.
 \tag{3A.4}
\]
For these two curves, direct polynomial division gives \(\gcd(H,DB)=1\) and \(\gcd(H,H')=1\), with \(\deg H=12\). Thus every root of \(H\) gives two distinct points, and (3A.4) says \(3P=\pm2P\). The plus sign would force \(P=O\), whereas the minus sign says \(5P=O\). Conversely a nonzero point killed by five is killed by neither two nor three, so its denominators are nonzero and its coordinate is a root of \(H\). These twelve roots therefore give exactly the 24 nonzero fifth-torsion points. All identities here can be checked by ordinary polynomial multiplication; no division-polynomial recurrence is being imported.

For \(E_1\) the factorization is
\[
 H=(x-5)(x-16)(5x^2+5x-29)
    (x^4+x^3+11x^2+41x+101)
    (x^4+15x^3+120x^2+200x+155).
 \tag{3A.5}
\]
Let the last three factors be \(f_0,f_1,f_2\), respectively. The simple-root Hensel proof of Lemma 0D.1 will account for all of their roots in \(\mathbb Q_{11}\). Write \(x=5+11z\); then
\[
 f_0/121=5z^2+5z+1,
\]
\[
 f_1/1331=11z^4+21z^3+16z^2+6z+1,
 \qquad f_2/1331=11z^4+35z^3+45z^2+25z+5.
\]
Modulo 11 the first has simple roots \(z=1,9\); the second has simple roots \(z=1,7,8\). The original polynomial \(f_1\) has one further simple root \(x=6\) modulo 11. The third transformed polynomial has simple root \(z=3\); the original \(f_2\) has simple root \(x=3\). Its remaining two roots have \(z=1+11s\), since substitution into the third transformed polynomial and division by 121 gives
\[
 1331s^4+869s^3+216s^2+24s+1
       \equiv7s^2+2s+1\pmod {11},
\]
with simple roots \(s=2,4\). Hensel lifts these distinct branches, furnishing two, four and four roots of the three factors. Together with 5 and 16 they exhaust (3A.5).

The \(y\)-coordinates are unramified too. For a root \(x=5+11z\),
\[
 D(x)=121U(z),\qquad
 U(z)=1+20z+56z^2+44z^3\equiv(z-1)^2\pmod {11}.
\]
If \(z\not\equiv1\), its leading unit is a nonzero square, so Lemma 0D.1 gives a square root in \(\mathbb Q_{11}\). If \(z=1+11s\), then
\[
 U(z)/121=1+24s+188s^2+484s^3\equiv(s+1)^2\pmod {11}.
\]
For the branches \(z\equiv1\) of \(f_0,f_1\), their equations give \(s\equiv8,3\), respectively: divide the value at \(z=1\) by 11 and solve the first derivative congruence. The two branches of \(f_2\) have \(s\equiv2,4\). None is \(-1\), so this second unit also has a square root in \(\mathbb Q_{11}\). At the smooth roots \(x\equiv6,3\), \(D(x)\equiv5\), a nonzero square modulo 11. The rational roots have their rational \(y\)-coordinates already listed. In all cases \(y=(-1\pm\sqrt D)/2\) lies in \(\mathbb Q_{11}\). Thus inertia at 11 acts trivially on \(E_1[5]\).

For \(E_2\),
\[
 H=x(x-1)h(x),\qquad
 h=5x^{10}-15x^9+x^8+96x^7-189x^6+171x^5
                  -84x^4+10x^3+25x^2-20x+5.
 \tag{3A.6}
\]
Write \(h(8+t)=\sum_{i=0}^{10}c_it^i\). The exact coefficients, in increasing order, are
\[
 (3529267621,4605073660,2705043209,941758730,215152036,
  33695035,3662659,272800,13321,385,5),
\]
and their 11-adic valuations are
\[
 (3,3,3,2,2,1,1,1,1,1,0).
 \tag{3A.7}
\]
Let \(t\) be any root and \(r=v_{11}(t)\), with base normalization \(v_{11}(11)=1\). If \(r\le0\), the term \(c_{10}t^{10}\) has strictly smallest valuation and cannot cancel, a contradiction. For \(r>0\), the minimum is controlled by \(3\), \(1+5r\), and \(10r\); every other term is strictly above the minimum. For \(0<r<1/5\), the last is uniquely smallest; for \(1/5<r<2/5\), the middle is uniquely smallest; for \(r>2/5\), the first is uniquely smallest. A vanishing sum cannot have a unique term of smallest valuation, by the valuation inequality applied after division by that term. Hence \(r=1/5\) or \(2/5\). Every such root has a nonintegral valuation and therefore lies outside the maximal unramified extension of \(\mathbb Q_{11}\): all its finite unramified subextensions have base-normalized value group \(\mathbb Z\), by §0F. A root gives fifth torsion by (3A.4), so inertia moves at least one point of \(E_2[5]\). Its action is nontrivial. The two actual residual representations are consequently nonisomorphic.

Each rational point \(P_i\) supplies a Galois-fixed one-dimensional subspace in \(E_i[5]\). Lemma 3.3 identifies the determinant as \(\bar\chi_5\), so the quotient is that character and
\[
 0\longrightarrow1\longrightarrow E_i[5]\longrightarrow\bar\chi_5
 \longrightarrow0.
\]
Their semisimplifications are \(1\oplus\bar\chi_5\). These are distinct characters by Lemma 3.0. Lemma 3.3 identifies \(E_i[5]\) with the reduction of \(T_5E_i\), completing every assertion of the example. In particular the isogeny gives two lattices in the same rational representation whose reductions differ. \(\square\)

The construction of (3A.1) can be compared with Milne's freely accessible *Abelian varieties*, I §13, pp.57–58. Its properties needed here, including alternation, have been proved above. The elementary secant calculations can be compared with Sutherland's free Lecture 5, §5.4; (3A.3)–(3A.7) were derived and checked directly for these two equations.

## 4. Finding a nonsplit reduction

Ribet's lemma makes a reducible residual representation useful even when the original representation is irreducible. We prove the oriented version, so the desired character occurs as the subrepresentation.

**Theorem 4.1 (Ribet's lattice lemma).** Suppose \(\rho:G\to\operatorname{GL}_2(E)\) is an irreducible continuous representation of a compact group and the semisimplification of a lattice reduction is \(\chi_1\oplus\chi_2\), where \(\chi_1,\chi_2:G\to k^\times\) are distinct. There is a stable lattice whose reduction fits into a nonsplit exact sequence
\[
 0\longrightarrow\chi_1\longrightarrow\bar\rho
 \longrightarrow\chi_2\longrightarrow0.
\]

**Proof.** Theorem 2.1 gives a stable lattice. Choose \(g_0\) such that \(\chi_1(g_0)\ne\chi_2(g_0)\). In a basis adapted to a residual composition series its characteristic polynomial is the product of the two character factors, so modulo \(\pi\) it has two distinct nonzero roots. Lemma 0D.1 gives roots \(\alpha_1,\alpha_2\in\mathcal O\) of the characteristic polynomial of \(\rho(g_0)\), labelled by their reductions, and \(\alpha_1-\alpha_2\) is a unit. The operators
\[
 P_1=\frac{\rho(g_0)-\alpha_2}{\alpha_1-\alpha_2},
 \qquad P_2=1-P_1
\]
are complementary idempotents preserving the lattice. Indeed its characteristic polynomial is \((X-\alpha_1)(X-\alpha_2)\), and Cayley–Hamilton from §0A gives the idempotent relations by substitution. Their sum is \(1\), so the lattice is their direct sum; after extending scalars each image is the corresponding one-dimensional eigenspace. Lemma 0A.1 proves that the two direct summands are free of rank one. Choose generators \(e_1,e_2\). Then \(\rho(g_0)=\operatorname{diag}(\alpha_1,\alpha_2)\), and write
\[
 \rho(g)=\begin{pmatrix}a_g&b_g\\c_g&d_g\end{pmatrix}
\]
in this basis, with entries in \(\mathcal O\).

The residual representation is reducible. Its invariant line must be an eigenspace of \(g_0\), so it is one of the two coordinate lines. Consequently either every \(b_g\) belongs to \(\pi\mathcal O\), or every \(c_g\) does. The resulting triangular diagonal entries are its subobject and quotient characters, and hence are \(\chi_1,\chi_2\) by Lemma 0A.2. The distinct eigenvalues at \(g_0\) fix their order: \(a_g\bmod\pi=\chi_1(g)\), \(d_g\bmod\pi=\chi_2(g)\), whichever coordinate line is initially invariant.

Irreducibility over \(E\) implies that neither family \((b_g)\) nor \((c_g)\) is identically zero: either vanishing family would make a coordinate line invariant over \(E\). Their nonempty sets of valuations have least members \(b,c\ge0\), by discreteness; the ideals are \(\pi^b\mathcal O\), \(\pi^c\mathcal O\), and an entry realizes each least valuation. Reducibility gives \(b+c\ge1\). Replace the basis by \(\pi^be_1,e_2\). The new matrix is
\[
 \begin{pmatrix}a_g&\pi^{-b}b_g\\\pi^bc_g&d_g\end{pmatrix}.
\]
All entries are integral. The determinant is a unit, so these matrices and their inverses preserve the new lattice. Modulo \(\pi\), every lower-left entry vanishes and at least one upper-right entry is nonzero. The first coordinate line is the character \(\chi_1\), and the quotient is \(\chi_2\).

If the extension split, its complementary invariant line would be the \(\chi_2(g_0)\)-eigenspace of \(g_0\), namely the second coordinate line. That would force every upper-right entry to vanish modulo \(\pi\), a contradiction. \(\square\)

The distinctness hypothesis gives integral eigenspace projectors. It is precisely the step that cannot be repeated verbatim when \(\chi_1=\chi_2\). Reversing the labels in the theorem also produces the opposite orientation of a nonsplit extension.

## 5. Exercises and complete solutions

**Exercise 5.1 (easy).** Prove that \(\mathbb Q_\ell(m)\) and \(\mathbb Q_\ell(n)\), as representations of \(G_{\mathbb Q}\), are isomorphic only for \(m=n\).

**Solution.** A nonzero intertwining map between one-dimensional spaces forces equality of their characters. Evaluate at arithmetic Frobenius for a prime \(p\ne\ell\). Proposition 3.1 gives \(p^m=p^n\). This is an equality of rational numbers inside \(\mathbb Q_\ell\), and hence \(m=n\). Conversely equal integers define identical actions.

**Exercise 5.2 (medium).** Establish the no-small-subgroups property of \(\operatorname{GL}_n(\mathbb C)\), and explain where profiniteness is used to deduce finiteness of the image.

**Solution.** For a subgroup in the ball \(\|A-1\|<1/2\), all powers of each element remain in the ball. Eigenvalues off the unit circle leave it through positive or negative powers. An eigenvalue on the unit circle other than \(1\) has a power with nonpositive real part. A nonidentity matrix with all eigenvalues \(1\) has a nonzero nilpotent part, whose powers grow polynomially. Thus every element is the identity, as calculated in Lemma 1.1. Profiniteness supplies an open subgroup in the inverse image of this ball; compactness makes its index finite. Compactness alone would not supply that open subgroup, as the usual action of the circle on \(\mathbb C\) illustrates.

**Exercise 5.3 (medium).** Starting from an arbitrary lattice, construct a stable one. For the action of Example 2.3, compute two nonisomorphic reductions explicitly.

**Solution.** Take the sum of its finite orbit, as in Theorem 2.1; openness of its stabilizer and compactness make the orbit finite. In Example 2.3, reduction of \(L\) sends \(t=1\) to \(\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\), whereas reduction of \(L'\) sends every \(t\) to the identity. These representations cannot be isomorphic, since conjugating the identity gives the identity. Their composition factors are two copies of the trivial character.

**Exercise 5.4 (hard).** Prove Ribet's lemma with a prescribed order of distinct residual characters. Indicate why an irreducible representation cannot have all upper-right or all lower-left entries zero in the eigenbasis used in the proof.

**Solution.** Use the two integral projectors of \(\rho(g_0)\), form the ideals of the two off-diagonal families, and scale the first eigenvector by the generator \(\pi^b\) of the upper-right ideal. The calculations in Theorem 4.1 make the upper-right ideal a unit ideal and the lower-left ideal a subset of \(\pi\mathcal O\). Hence the reduction is upper triangular with characters \(\chi_1,\chi_2\), and it does not split because its only possible \(g_0\)-stable complement is not \(G\)-stable. If all lower-left entries were zero before scaling, \(Ee_1\) would be an invariant line over \(E\). If all upper-right entries were zero, \(Ee_2\) would be one. Either contradicts irreducibility. These observations justify finiteness of both valuations used in the scaling.

## Proof register and unresolved arithmetic dependencies

The representation core has proofs in this lesson. Lemmas 0A.1–0A.2 supply DVR freeness, commensurability, composition series and additivity. Lemmas 0B.1–0B.2 and Proposition 0C.1 supply the Galois facts actually used. Lemmas 0D.1–0D.2 and Proposition 0E.1 establish lifting, finite coefficient fields and unique complete valuations. Lemma 0F.1 and Proposition 0F.2 construct unramified fields and Frobenius. Lemma 3.0 proves cyclotomic surjectivity. Theorems 1.2, 2.1, 2.2, 2.4, Proposition 3.1 and Theorem 4.1 therefore have their dependencies available before use. All four exercise solutions use these proofs.

Lemma 3.3 and Example 3.4 supply the torsion pairing, explicit degree-five isogeny, rational Tate-module identification and full residual inertia comparison before any use. The earlier geometric proofs used in that construction are identified at the start of §3A. The written Kronecker–Weber proof, Theorem 20.2 and Proposition 20.5 of the named class-field lesson, uses the earlier ray-field theorem; that theorem and its prerequisites are not checked in this lesson. Citations identify reading materials and actual providers; their presence alone does not close a proof obligation.

## References

- [Taylor 2004] Richard Taylor, *Galois representations*, §1, printed pp. 74–77: the Galois topology, local residue action, Artin representations and the cyclotomic example. [Freely accessible Numdam article](https://www.numdam.org/item/AFST_2004_6_13_1_73_0/), [complete primary PDF](https://www.numdam.org/item/AFST_2004_6_13_1_73_0.pdf). Taylor uses geometric Frobenius in that discussion; this lesson defines and proves its arithmetic normalization explicitly.
- [Ribet 1976] Kenneth A. Ribet, *A modular construction of unramified p-extensions of \(\mathbb Q(\mu_p)\)*, Proposition 2.1 and proof, printed pp. 154–155. [Freely accessible author's copy](https://math.berkeley.edu/~ribet/Articles/invent_34.pdf). Theorem 4.1 proves the distinct-character oriented version through integral eigenspace projectors and valuation minima.
- [Stacks, Tag 0BMI] *The Stacks project*, Fields §9.22, Lemmas 9.22.1–9.22.3, Theorem 9.22.4 and Lemma 9.22.5: topology, inverse limits, fixed fields and restriction. [Original free statements and proofs](https://stacks.math.columbia.edu/tag/0BMI). The corresponding proofs for this lesson are in §§0B–0C.
- [Stacks, Tag 04GM] *The Stacks project*, Lemma 10.153.9: lifting a simple root in a complete local ring. [Original free statement and proof](https://stacks.math.columbia.edu/tag/04GM). Lemma 0D.1 proves the form used here, including uniqueness; Lemma 0D.2 proves coprime factor lifting.
- [Stacks, Tag 00PD] *The Stacks project*, Lemma 10.119.7: characterizations of discrete valuation rings. [Original free statement and proof](https://stacks.math.columbia.edu/tag/00PD). Proposition 0E.1 proves the integral-closure case here, including the principal maximal ideal argument.
- [Milne, FT] J. S. Milne, *Fields and Galois Theory*, free author notes, version 5.10, September 2022. Chapter 3, Proposition 3.2, Theorem 3.4, Corollary 3.11 and Theorem 3.17; Chapter 4, finite fields; Chapter 5, Lemma 5.9 and Theorem 5.10 on cyclotomic extensions. [Freely accessible author's PDF](https://jmilne.org/math/CourseNotes/FT.pdf). The narrower prime-power cyclotomic assertion actually needed here is proved in Lemma 3.0.
- [Milne, ANT] J. S. Milne, *Algebraic Number Theory*, free author notes, Chapter 7, Proposition 7.31 and Theorems 7.32–7.33 on lifting, Theorem 7.38 and Corollaries 7.40–7.42 on valued extensions, Proposition 7.50 and Corollaries 7.51–7.52 on unramified fields. [Freely accessible author's PDF](https://jmilne.org/math/CourseNotes/ANT.pdf). Sections 0D–0F give the proofs used here, including construction rather than an assumed existence theorem for unramified extensions.
- [Reutenauer–Schützenberger 1987] Christophe Reutenauer and Marcel-Paul Schützenberger, *A formula for the determinant of a sum of matrices*, Theorem and equations (4)–(6), printed pp. 300–301. [Freely accessible author's copy](https://reutenauer.math.uqam.ca/wp-content/uploads/2024/04/Determinant-of-a-sum.pdf). The determinant identity and its specialization needed for characteristic-polynomial Brauer–Nesbitt are fully proved in Theorem 2.4; the proof there uses universal formal logarithms and cyclic words.

- [Milne, AV] J. S. Milne, [*Abelian varieties*, free author notes](https://www.jmilne.org/math/CourseNotes/AV.pdf), I §13, pp.57–58, for the divisor construction of the torsion pairing. Lemma 3.3 proves its required properties here.
- [Sutherland, Lecture 5] Andrew V. Sutherland, [*Isogeny kernels and division polynomials*, freely available MIT lecture notes](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf), 26 September 2023, §5.4, for elementary group-law computations. The specific map and fifth-torsion identities in Example 3.4 are computed directly.

These materials were read directly in their free primary editions. No paid book is cited or used as a mathematical source in this lesson. The source-read record includes retrieval dates, exact locators, hashes and the unresolved programme dependencies.
