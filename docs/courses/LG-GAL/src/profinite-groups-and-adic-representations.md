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

## 0G. Integral generators for finite local extensions

We now prove the integral-basis and monogenic assertions used in the discriminant proof. Its field scope is every finite separable extension of a complete discretely valued field with finite residue field, in particular every finite extension of a finite extension of \(\mathbf Q_p\). The only field foundations used are the earlier proofs above: Lemma 0B.1, Lemma 0D.1, Proposition 0E.1 and Proposition 0F.2. The present assertions use those written arguments.

### 0G.1. Valuation and finite-lattice interfaces

Let \(K\) be such a field, \(R\) its valuation ring and \(\pi\) a uniformizer. Proposition 0E.1 actually proves that the integer ring \(S\) of a finite separable \(F/K\) is a complete DVR, finite free over \(R\), and that
\[
 [F:K]=ef,
\]
where \(e\) is its ramification index and \(f\) its residue degree. Normalize the extended valuation by \(v(\pi)=1\), so its value group on \(F\) is \(e^{-1}\mathbf Z\). Uniqueness makes every embedding into a common finite normal closure an isometry. The same proof supplies separable embeddings and an integral trace lattice; none of these assertions is inferred only from its title.

### 0G.2. Eisenstein roots and the full integral ring

**Lemma 0G.2.** Assume the displayed polynomial is separable. If
\[
 P(T)=T^n+c_{n-1}T^{n-1}+\cdots+c_0,
 \qquad v(c_j)\ge1\ (j<n),\quad v(c_0)=1,
\]
then a root \(t\) generates a totally ramified extension of degree \(n\), and
\[
 \mathcal O_{K(t)}=R[t].
 \tag{IG1}
\]

*Proof.* A root is integral, hence has nonnegative valuation by Proposition 0E.1. Valuation zero would make its leading power the unique smallest term. Thus \(v(t)>0\). If \(v(t)<1/n\), the leading term is strictly smaller than the constant and every intermediate term: for \(0<j<n\),
\(1+jv(t)-nv(t)=1-(n-j)v(t)>0\). If \(v(t)>1/n\), the constant is strictly smaller than every other term. Both contradict the ultrametric inequality for a sum zero. Hence \(v(t)=1/n\).

Its value group forces the ramification index to be divisible by \(n\). The degree formula makes the field degree at least \(n\); the polynomial gives the opposite inequality. Thus the degree and ramification index are exactly \(n\), and its residue field is the base residue field. The polynomial is the minimal polynomial and is irreducible.

Write a field element uniquely as \(x=\sum_{j=0}^{n-1}a_jt^j\), with \(a_j\in K\). The valuations of its nonzero terms are \(v(a_j)+j/n\); these are pairwise distinct modulo \(\mathbf Z\). Their minimum occurs once, so it is \(v(x)\). Indeed a term of uniquely least valuation cannot cancel a sum of strictly larger valuation. Consequently \(v(x)\ge0\) exactly when every \(v(a_j)+j/n\ge0\). Since \(v(a_j)\) is integral and \(0\le j/n<1\), this is equivalent to every \(a_j\in R\). This proves (IG1). ∎

### 0G.3. The unramified field and a uniformizer basis

Let the residue field of \(S\) be \(k_F\), of degree \(f\) over \(k\). Finite fields are separable and have a primitive element by Lemma 0F.1. Choose \(\bar\theta\) generating \(k_F/k\), and lift its monic irreducible polynomial to \(P_0\in R[T]\). The simple-root Hensel proof of Lemma 0D.1 gives a root \(\theta\in S\) with residue \(\bar\theta\).

Proposition 0F.2 proves directly that
\[
 E=K(\theta),\qquad R_E=R[\theta]
\]
is unramified of degree \(f\). Its uniformizer is \(\pi\), and its residue field is already \(k_F\). The degree formula therefore gives \([F:E]=e\), with this extension totally ramified.

Take any uniformizer \(t\) of \(S\). Its valuation is \(1/e\), so its first \(e\) powers are linearly independent over \(E\): the nonzero terms of any putative relation have distinct valuation classes modulo \(\mathbf Z\). Since \([F:E]=e\), these powers form a basis and \(F=E(t)\).

Every conjugate of \(t\) over \(E\) has valuation \(1/e\), by uniqueness in a common finite normal closure. In its monic degree-\(e\) minimal polynomial, the coefficient which is an elementary symmetric product of \(j\) roots has valuation at least \(j/e\). It belongs to \(E\), whose value group is \(\mathbf Z\), so every nonleading coefficient is in \(\pi R_E\); the constant product has valuation exactly one. The polynomial is Eisenstein. Lemma 0G.2 now gives
\[
 S=R_E[t]=R[\theta,t].
 \tag{IG2}
\]
This includes the unramified case \(e=1\).

### 0G.4. A single integral generator over the original base

**Theorem 0G.4.** There is \(\alpha\in S\) such that \(S=R[\alpha]\), and a power basis in \(\alpha\) is an integral basis over \(R\).

*Proof.* The field is generated by \(\theta,t\). For each pair of distinct embeddings of \(F/K\), equality of their values on \(\theta+ct\) excludes at most one scalar \(c\in K\), unless their values on \(t\) coincide. In that exceptional situation their values on \(\theta\) differ, so equality excludes no scalar. The unit set \(R^\times\) is infinite: for example the elements \(1+\pi^j\), \(j\ge1\), are distinct. Choose a unit \(c\) avoiding the finitely many exclusions and set
\[
 \alpha=\theta+ct.
\]
Its distinct embedding images number \([F:K]\), so the actual separable embedding count in Lemma 0B.1 proves \(F=K(\alpha)\).

Its monic minimal polynomial \(Q\) has coefficients in \(R\): its roots are integral, their elementary symmetric expressions lie in \(K\), and \(R\) is integrally closed. Put \(A=R[\alpha]\). This is free of rank \([F:K]=ef\) over \(R\), with its power basis, and complete in the \(\pi\)-adic topology.

In a common finite normal closure, reduction of every conjugate of \(\alpha\) equals reduction of the corresponding conjugate of \(\theta\), since all conjugates of \(t\) have positive valuation. The \(f\) embeddings of \(E/K\) extend to exactly \(e\) embeddings of \(F/K\) each, by Lemma 0B.1. Thus the root-product calculation gives
\[
 \bar Q=\bar P_0^{\,e},\qquad
 A/\pi A\simeq k[T]/(\bar P_0^{\,e}).
 \tag{IG3}
\]
The equality can be checked after the injective extension into the common residue algebraic closure; its coefficients then give the same equality over \(k\).

This quotient is local, with maximal ideal generated by \(\bar P_0\): Bezout makes a polynomial prime to \(\bar P_0\) a unit modulo its \(e\)-th power, whereas the ideal of \(\bar P_0\) is nilpotent and has field quotient. Units modulo \(\pi A\) lift to units in \(A\) by a convergent geometric series. Hence \(A\) is local, with maximal ideal
\[
 J=(\pi,P_0(\alpha)).
\]
By (IG3), \(P_0(\alpha)^e\in\pi A\). Expanding a product of \(e\) generators of \(J\) therefore gives
\[
 J^e\subset\pi A\subset J.
 \tag{IG4}
\]
Their powers show that the two adic topologies are equivalent; in particular \(A\) is complete and separated for \(J\).

The reduction of \(P_0'(\alpha)\) in \(A/J\simeq k_F\) is nonzero, since \(\bar P_0\) is separable. It is therefore a unit in \(A\). Apply the actual general complete-ring Hensel proof of Lemma 0D.1, with ideal \(J\), initial value \(\alpha\), and polynomial \(P_0\). This supplies \(\theta_A\in A\) with
\[
 P_0(\theta_A)=0,\qquad \theta_A-\alpha\in J.
\]
Inside \(S\), every element of \(J\) has positive valuation, and \(\alpha\) has residue \(\bar\theta\). Thus \(\theta_A\) and \(\theta\) are roots of \(P_0\) with that same simple residue root. Uniqueness in the Hensel proof on \(S\) gives \(\theta_A=\theta\). Since \(c\) is a unit of \(R\),
\[
 t=c^{-1}(\alpha-\theta)\in A.
\]
Equation (IG2) now gives \(S\subset A\), while \(A\subset S\) was its construction. Hence \(S=A\), proving the theorem. ∎

### 0G.5. Exact proof use and human-source boundary

The freely accessible [Milne, *Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Proposition 7.55 and Remark 7.56, printed pp.129–130, provides the uniformizer/valuation material for Sections 0G.2–3. The full power-basis integrality and single-generator argument are written above; the assertions in the notes are not being substituted for those proofs. The simple-root and field-degree inputs are the actual earlier Lesson01 proofs identified in Section 0G.1.

These proofs supply the finite-separable, finite-residue-field Eisenstein and integral-monogenic interfaces used in later discriminant calculations. Trace duality, Hilbert's formula and the elliptic conductor equality still require their separate arguments.

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

The more general assertion is Kronecker–Weber: finite-order continuous characters of \(G_{\mathbb Q}\) correspond to Dirichlet characters, with an unramified arithmetic Frobenius evaluated as \(\chi(p)\). An actual programme proof is *Kronecker–Weber and the maximal abelian extension of the rationals*, Theorem 20.2 and Proposition 20.5. These are written proofs, rather than future lesson titles: Theorem 20.2 uses Proposition 20.1 and the earlier ray-field theorem, and Proposition 20.5 passes to characters. The full ray-field prerequisite chain remains required. The quadratic calculation above, the cyclotomic surjectivity proof and every representation theorem here use none of that classification.

### 3A. An explicit arithmetic pair of lattices

We now prove the elliptic example at this point. The geometric prerequisites are actual earlier programme proofs in *Abelian varieties*: Corollary 2.3 proves that a morphism taking identity to identity is a homomorphism; Theorems 6.1–6.2 prove that multiplication by an integer prime to the characteristic has degree its square on an elliptic curve and is finite étale; Proposition 6.3 and Theorem 6.8 construct the finite étale quotient by a finite translation subgroup; Theorems 6.7 and 7.1–7.2 prove reverse isogenies, finite torsion structure and torsion transition maps; Theorem 9.0 constructs the cubic group law; Lemma 9.11 proves curve Riemann–Roch and duality; Example 9.12 embeds a genus-one group curve as a pointed cubic. The precise written scopes were inspected. This construction uses the stated earlier geometric proofs. The following argument supplies the specific isogeny, pairing and inertia comparison, without importing them from a later LG-GAL lesson.

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

## 5A. Sheaf cohomology from local lifting

This section supplies the abstract sheaf arguments needed in Section 6. Its proofs apply to a small site with finite limits. They do not assume geometric points, Noetherian rings, or an already constructed cohomology theory. An application to an étale basis must still prove that the chosen category and coverings have these properties. In particular, the algebraic local form, openness, finite-presentation descent and strict-local identifications required in Section 6 are separate geometric obligations.

A site here is a category \(\mathcal C\) equipped with covering families, including identities, stable under pullback and composition. A sheaf of abelian groups \(F\) assigns groups and restriction maps to objects, and a section over a covered object is exactly a family of sections agreeing on all fibre products. All constructions take place in one fixed universe. Covering families can be replaced by their covering sieves, namely the sets of arrows they generate; hence the indexing data below form sets. Set-theoretic choice, including Zorn's lemma, is the background convention.

### 5A.1. Matching families and exact sheafification

**SH1.** Every abelian presheaf \(P\) has a sheafification \(P^\#\). Sheafification is an exact left adjoint to inclusion of sheaves. A presheaf section becomes zero after sheafification if and only if it is zero on a covering. Every section of \(P^\#\) is locally represented by sections of \(P\).

*Proof.* For each object \(U\), form \(P^+(U)\) from matching families on coverings of \(U\). Identify two families when their restrictions agree on a common covering refinement. A common refinement exists by pulling back the two coverings and composing coverings. Addition is defined after such a refinement. Restrictions are obtained by pulling back the covering. These rules give an abelian presheaf and a map \(P\to P^+\).

If a matching family defines zero in \(P^+(U)\), its entries vanish on a refinement, by the defining equivalence. Consequently a section of \(P(U)\) maps to zero precisely when it vanishes on a covering. Also \(P^+\) is separated: equality after restriction to a covering can be witnessed by refinements on its members, and their composite is a refinement over \(U\).

For a separated presheaf \(Q\), the presheaf \(Q^+\) is a sheaf. To glue a family of its sections, choose a representing covering on each member of the original covering. Agreement on overlaps says that the representing entries agree on refinements. Separatedness of \(Q\) then makes them agree on the whole overlap, because equality can be tested on its covering. Thus the entries are one matching family on the composite covering. This gives a glued section; separatedness proves uniqueness. Applying this to \(Q=P^+\) gives
\[
 P^\#=(P^+)^+.
 \tag{SC1}
\]
The two local representation steps compose. The zero criterion for the original section follows by composing the coverings witnessing its zero at the two steps.

A map \(P\to F\) into a sheaf sends a matching family to its unique glued section in \(F\). This extends the map uniquely over \(P^+\), then over (SC1). Conversely an extension restricts to the original map. This proves the adjunction.

Finite products and kernels commute with sheafification. For products, represent finitely many sections on one common refinement. For a kernel, represent a section locally in \(P\); the assertion that its image is zero can be witnessed after a further refinement, so it is locally a section of the presheaf kernel. The same refinements prove injectivity of these identifications. A presheaf surjection remains locally surjective after sheafification: locally represent the target section, and lift its representing section. Sheafification preserves cokernels by its adjunction, or by the same local description of quotient sections. These facts prove exactness. \(\square\)

Kernels of maps of sheaves are computed section by section. Cokernels are sheafifications of presheaf cokernels. The natural coimage-to-image map is an isomorphism because this holds for groups locally, and SH1 identifies both sheafifications. Thus abelian sheaves form an abelian category. In particular,
\[
 F\longrightarrow G\longrightarrow H
 \text{ is exact at }G
 \quad\Longleftrightarrow\quad
 \begin{gathered}
 s\in G(U),\ s\mapsto0\\
 \text{lifts locally to }F.
 \end{gathered}
 \tag{SC2}
\]
Here and below “locally” means on a covering in the site, rather than on an assumed topological space.

### 5A.2. Colimits and the distinction between local and global lifting

**SH2.** Products and all other limits of abelian sheaves are computed section by section. Colimits are sheafifications of presheaf colimits. Filtered colimits and arbitrary direct sums of abelian sheaves are exact.

*Proof.* A limit of sheaves is a sheaf: a matching family is glued in every component, and the component gluing maps respect every arrow of the limit diagram by uniqueness. The adjunction in SH1 gives the colimit assertion.

For groups, a filtered colimit consists of stage representatives, with two representatives equal when their images agree at a common later stage. This description also holds for a filtered category: finitely many objects and arrows have a common receiving object, and finitely many parallel arrows can be equalized later. It proves that filtered colimits of groups commute with finite products and kernels, and preserve exact sequences of groups.

A short exact sequence of sheaves need not be surjective on sections. Nevertheless filtered sheaf colimits are exact. A representative of a target section lifts locally at its own stage by (SC2). If a middle representative has zero image after sheafification of the group colimit, SH1 first gives a covering on which that image is zero in the group colimit. On each member it is already zero at some later stage; (SC2) then lifts it after another covering. Composite coverings give exactness at the middle. Monomorphisms remain monomorphisms because they are sectionwise injective, filtered group colimits preserve that property, and SH1 is exact. This proves the assertion without claiming that an arbitrary filtered colimit is already a sheaf.

For direct sums, every presheaf section has finite support. Finitely many locally required lifts or zero relations can be handled on a common refinement. The same argument and SH1 prove exactness. \(\square\)

If the site has a basis whose coverings admit finite refinements, a filtered colimit of sheaves on that basis is already a sheaf: the finite equalizer for a covering commutes with the filtered group colimit, by the representative argument just given. This is the additional finiteness needed for the sectionwise comparison in Lemma 6.3; it is not an assertion about all sites.

### 5A.3. Enough injectives without an assumption about points

A sheaf \(J\) is injective if every map \(A\to J\) extends over every monomorphism \(A\hookrightarrow B\). Define
\[
 P_U=\bigl(V\longmapsto
       \mathbb Z[\operatorname{Hom}_{\mathcal C}(V,U)]\bigr)^\#.
 \qquad
 \operatorname{Hom}(P_U,F)=F(U).
 \tag{SC3}
\]
The group in brackets is the free abelian group on the displayed set. The equality follows directly: the image of the identity arrow determines a natural map on all generators, and the adjunction SH1 extends it uniquely to \(P_U\). The \(P_U\) generate sheaves, since all sections of a sheaf give a surjection from a direct sum of these sheaves.

**SH3.** Every abelian sheaf embeds in an injective abelian sheaf.

*Proof.* First we prove an extension criterion. Suppose \(J\) has the extension property only for all subobjects \(K\subset P_U\), for all \(U\). Given \(A\subset B\) and a map \(A\to J\), order its extensions to intermediate subobjects of \(B\) by inclusion. A chain has an upper bound: take its sheaf colimit, which remains a subobject of \(B\) by SH2, and glue the compatible maps. The subobjects and maps involved form a set. Zorn gives a maximal extension \(C\to J\). If \(C\ne B\), choose \(b\in B(U)\setminus C(U)\). Let \(p:P_U\to B\) be its map (SC3), and put \(K=p^{-1}(C)\). Extend \(K\to C\to J\) to \(t:P_U\to J\). The map
\[
 C\oplus P_U\longrightarrow J,\qquad
 (c,v)\longmapsto \phi(c)+t(v)
 \tag{SC4}
\]
kills the kernel of \((c,v)\mapsto c+p(v)\): that kernel consists of \((-p(k),k)\) for \(k\in K\). Thus (SC4) factors through the sheaf image \(C+\operatorname{im}p\). It extends \(\phi\) over a strictly larger subobject, since that subobject contains \(b\). This contradicts maximality. The criterion is proved.

We construct a sheaf satisfying the criterion. Fix representatives of all \(K\subset P_U\). This is a set: a subsheaf is specified by subsets of the component section sets, with their restriction maps. Choose an infinite cardinal \(\lambda\) bounding the objects and arrows of the site, all these sheaves' total section sets, and all arrows in a covering sieve. Choose an ordinal \(\kappa\) with cofinality greater than \(\lambda\); the initial ordinal of the successor cardinal \(\lambda^+\) works. Indeed at most \(\lambda\) ordinals below it each have cardinality at most \(\lambda\), so their union still has cardinality at most \(\lambda\) and cannot be cofinal.

Start with \(F_0=F\). For each successor step, take every pair \((K\subset P_U,\phi:K\to F_\alpha)\) and form the pushout
\[
 F_{\alpha+1}=
 \operatorname{coker}\left[
 \bigoplus_{(K,U,\phi)}K
 \longrightarrow
 F_\alpha\oplus\bigoplus_{(K,U,\phi)}P_U
 \right],
 \qquad k\longmapsto(\phi(k),-k).
 \tag{SC5}
\]
The arrow \(F_\alpha\to F_{\alpha+1}\) is injective. In fact the map from the direct sum of the \(K\) to the direct sum of the \(P_U\) is injective by SH2, so a relation with zero second component has zero first component as well. Each map \(\phi\) extends over its \(P_U\) in (SC5). At a limit step take the sheaf colimit. SH2 keeps every transition injective.

At the final limit \(\kappa\), this colimit is sectionwise. To see this, a matching family on a covering sieve has at most \(\lambda\) entries and compatibility equations. Choose their stage representatives, then stages where all equations hold. Cofinality makes one stage suffice. The sheaf condition at that stage gives a glued representative. Equality is verified in the same way. Hence the sectionwise colimit is itself a sheaf.

Any map \(K\to F_\kappa\) factors through one \(F_\alpha\), \(\alpha<\kappa\). Choose representatives for every image section of \(K\), then a stage where all restriction equations hold. There are at most \(\lambda\) sections and equations, so again cofinality supplies one stage. At the next step (SC5) extends the map over \(P_U\). Its composite into \(F_\kappa\) proves the extension criterion. Thus \(F\hookrightarrow F_\kappa\) is the required embedding. This argument uses no assertion that sheafification takes an injective presheaf to an injective sheaf. \(\square\)

### 5A.4. Resolutions, comparison and local vanishing

**SH4.** The groups \(H^n(U,F)\) are well defined by taking an injective resolution \(F\to I^\bullet\) and the cohomology of \(I^\bullet(U)\). Positive-degree classes become zero on a covering of \(U\).

*Proof.* Apply SH3 to \(F\), then to each successive cokernel. This constructs an exact augmented resolution. To extend a map \(F\to G\) to resolutions, first extend \(F\to G\to J^0\) over \(I^0\). After a chain map has been constructed through degree \(r\), its next required map is defined on the image of \(d:I^r\to I^{r+1}\), because the preceding chain identity makes it zero on the kernel. Extend it over \(I^{r+1}\) using injectivity of \(J^{r+1}\).

Two such chain maps are homotopic. Their degree-zero difference kills \(F\), so it factors through the image of \(I^0\to I^1\); extend that factor into \(J^0\) over \(I^1\). Subtract its homotopy boundary. The new difference is zero in degree zero, and the same argument in each degree gives the remaining homotopy. Comparison maps for the identity in both directions have composites homotopic to the identity. They therefore induce inverse cohomology isomorphisms, independent of choices.

For an exact sequence \(0\to F\to G\to H\to0\), embed \(F,H\) into injectives \(I_F,I_H\). Extend \(F\to I_F\) over \(G\), and combine it with \(G\to H\to I_H\). The resulting map \(G\to I_F\oplus I_H\) is injective: an element in its kernel first lies in \(F\), where the first component is injective. The three cokernels form another short exact sequence, as follows by lifting a cokernel representative and checking its kernel. Repeating gives split exact rows of injective resolutions. A closed section of the quotient resolution lifts to the middle resolution; its boundary lifts uniquely to the subresolution. This defines the connecting map, and the same lifting calculation proves exactness of the long cohomology sequence. Comparison and homotopy prove naturality.

Finally a class of positive degree \(n\) is represented by \(z\in I^n(U)\) with \(dz=0\). Exactness of the resolution says that \(I^{n-1}\to\ker(d:I^n\to I^{n+1})\) is an epimorphism of sheaves. By (SC2), \(z\) is locally a boundary. This proves local vanishing without a spectral sequence. \(\square\)

### 5A.5. Why slice restriction preserves injectives

Let \(\mathcal C/U\) have objects arrows \(V\to U\), and coverings inherited from \(\mathcal C\). Restriction is
\[
 r_UF(V\to U)=F(V).
 \tag{SC6}
\]
It is exact: kernels are sectionwise, and local lifts in (SC2) are coverings of that same slice object.

**SH5.** Restriction \(r_U\) has an exact left adjoint and therefore takes injective sheaves to injective sheaves.

*Proof.* For a sheaf \(G\) on the slice, form
\[
 j_{U!}G=
 \left(V\longmapsto
   \bigoplus_{\phi:V\to U}G(V,\phi)\right)^\#.
 \tag{SC7}
\]
Restriction along \(W\to V\) sends the summand indexed by \(\phi\) to the summand indexed by its composite. A map from this presheaf to \(F\) is exactly a family of maps \(G(V,\phi)\to F(V)\) compatible with slice arrows. By SH1, this is a map \(G\to r_UF\), proving the adjunction.

For an exact sequence of slice sheaves, monomorphisms remain injective in the presheaf direct sums. A section requiring a lift, or a section mapping to zero, involves only finitely many summands. For each summand (SC2) supplies a covering; pull back these finitely many coverings to one common refinement. The required lift or kernel witness is then valid in their direct sum. SH1 gives exactness of (SC7).

Given a monomorphism \(A\to B\) on the slice and a map \(A\to r_UI\), the adjunction gives a map \(j_{U!}A\to I\). Exactness makes \(j_{U!}A\to j_{U!}B\) injective; injectivity of \(I\) extends the map. The adjunction brings it back to \(B\to r_UI\). Thus \(r_UI\) is injective. Since restriction is exact, it restricts an injective resolution to an injective resolution. Consequently the definition in SH4 agrees with cohomology on the slice. \(\square\)

### 5A.6. An exact inverse image and the higher-image presheaf

**SH6.** Let \(a:\mathcal C\to\mathcal D\) preserve finite limits and covering families. There is an adjunction \(f^{-1}\dashv f_*\) on abelian sheaves, with exact \(f^{-1}\), and
\[
 (f_*G)(V)=G(aV),\qquad
 R^nf_*G=
 \bigl(V\longmapsto H^n(aV,G)\bigr)^\#.
 \tag{SC8}
\]

*Proof.* The first rule gives a sheaf because \(a\) preserves the fibre products in the sheaf equalizer and sends coverings to coverings. Before sheafification define the inverse image by
\[
 (L_aF)(W)=
 \varinjlim_{(V,\beta:W\to aV)} F(V).
 \tag{SC9}
\]
The colimit uses refinements: \(V'\to V\) and \(\beta':W\to aV'\) with \(a(V'\to V)\beta'=\beta\) send a section to its restriction. This indexing category is filtered in the direction of these restriction maps. It is nonempty by the terminal object. Products give common refinements; equalizers give refinements equalizing parallel arrows, since \(a\) preserves them. Thus (SC9) preserves finite limits of presheaves by the filtered-representative proof in SH2.

A map from \(L_aF\) to a presheaf \(G\) on \(\mathcal D\) is equivalent to maps \(F(V)\to G(aV)\): restrict the latter along each \(\beta\), and use (SC9); in the reverse direction take \(\beta=\operatorname{id}_{aV}\). These operations are inverse. Sheafifying (SC9) and using SH1 proves the adjunction. The functor \(f^{-1}\) preserves kernels by the finite-limit calculation and SH1, and preserves cokernels by its adjunction. It is additive, so it is exact.

An exact left adjoint makes its right adjoint preserve injectives, by the extension argument in SH5. To compute \(R^nf_*G\), choose \(G\to I^\bullet\). In each object \(V\), the complex \(f_*I^\bullet\) is \(I^\bullet(aV)\). The sheaf cohomology of this complex is the sheafification of its presheaf cohomology: kernels are sectionwise and images are sheafified images by SH1. SH4 and SH5 identify that presheaf with the one in (SC8). This proves the higher-image formula before using any continuity theorem. Compositions of inverse images have their canonical identification because they have the same right adjoint; the adjunction bijections also make these identifications associative. \(\square\)

### 5A.7. Stalks of a point functor and their precise hypothesis

A point functor is a functor \(\tau:\mathcal C\to\mathrm{Sets}\) preserving finite limits such that every covering induces a surjection \(\coprod\tau(U_i)\to\tau(U)\). Its neighbourhoods are pairs \((U,u)\), \(u\in\tau(U)\). Define
\[
 F_\tau=\varinjlim_{(U,u)}F(U),
 \tag{SC10}
\]
using arrows preserving the chosen element, in the refinement direction.

**SH7.** The neighbourhood index for (SC10) is filtered. Sheafification leaves (SC10) unchanged, and this stalk functor is exact and commutes with colimits. For a conservative family of such functors, exactness of sheaf complexes is equivalent to exactness of their stalk complexes.

*Proof.* The terminal object gives a neighbourhood, products give common refinements, and equalizers equalize parallel neighbourhood arrows. Their chosen elements exist because \(\tau\) preserves these finite limits. Thus filtered group representatives apply.

A matching family at a neighbourhood is represented in the stalk by one of its entries: lift its chosen element to a covering member using the covering-surjectivity condition. Equality or zero in sheafification is witnessed on a covering by SH1, and the same lifting chooses a neighbourhood witnessing that equality or zero in (SC10). Apply this twice to (SC1). Hence sheafification leaves the stalk unchanged. Filtered group colimits preserve exact sequences of presheaves, and (SC2) supplies local lifts at a covering member over the chosen element for exact sequences of sheaves. This proves exactness. The colimit assertion follows either from representatives or from SH2 and the unchanged-sheafification assertion.

“Conservative” means that a map inducing isomorphisms at every stated stalk is an isomorphism of sheaves. A sheaf with all stalks zero is then zero, by applying this definition to its map to the zero sheaf. Exactness of stalks identifies the stalks of the cohomology sheaf of a complex with its group cohomology at each stalk. Consequently zero stalk cohomology forces that cohomology sheaf to be zero. This proves the criterion. It does not assert that a proposed geometric family is conservative; that geometric assertion needs its own proof.

In particular (SC8) gives the stalk formula
\[
 (R^nf_*G)_\tau
 =\varinjlim_{(V,v)}H^n(aV,G).
 \tag{SC11}
\]
This is a presheaf-and-stalk statement. Identifying its right side with cohomology of an inverse-limit scheme is the additional continuity theorem, not part of the definition of a stalk. \(\square\)

### 5A.8. The full covering nerve and the injective contraction

For a cover \(\mathcal U=\{U_i\to U\}\), put
\[
 U_{i_0\ldots i_p}=U_{i_0}\times_U\cdots\times_U U_{i_p},
 \qquad
 \check C^p(\mathcal U,F)=
       \prod_{(i_0,\ldots,i_p)}F(U_{i_0\ldots i_p}).
 \tag{SC12}
\]
All ordered tuples occur, including repeated indices. The differential is the alternating sum of restrictions along deletion of one entry. Two deletions occur twice with opposite signs, so its square is zero.

**SH8.** If \(I\) is injective, its augmented complex \(I(U)\to\check C^\bullet(\mathcal U,I)\) is exact.

*Proof.* Work on \(\mathcal C/U\). Take the augmented chain complex of free abelian sheaves on the covering nerve, with degree \(p\) equal to the direct sum of the free sheaves on the objects \(U_{i_0\ldots i_p}\), and degree \(-1\) the free sheaf on the terminal object. Its boundary deletes entries with alternating signs. This complex is exact locally: on a covering member there is a chosen lift of its structure arrow to one of the \(U_i\). Insert that chosen lift as the first entry. If \(\partial\) is the boundary and \(s\) this insertion, then
\[
 \partial s+s\partial=1,
 \qquad s_{-1}(1)=\text{the chosen lift}.
 \tag{SC13}
\]
Indeed the first deletion of the inserted entry returns the original tuple. Every other deletion cancels with the corresponding term of \(s\partial\). To apply this to sheaf sections, first represent a section locally by a finite sum of free generators, using SH1; choose covering lifts for the finitely many terminal arrows involved and refine their coverings together. The same contraction then witnesses local exactness for every cycle. Equation (SC2) proves exactness of the sheaf chain complex.

SH5 makes \(r_UI\) injective. Apply \(\operatorname{Hom}(-,r_UI)\) to the exact chain complex. This remains exact: a map defined on a cycle subobject extends to the preceding free sheaf by injectivity, which is precisely the required cochain-boundary witness. Formula (SC3) identifies the resulting complex with (SC12), including its augmentation. This proves the assertion. \(\square\)

The requirement to keep the full nerve matters even for a covering consisting of one map. Its self-fibre products need not equal the covering object. Deleting all positive degrees because there is only one index changes the complex.

### 5A.9. Derived comparison using only finite diagonals

**SH9.** For an injective resolution \(F\to I^\bullet\), the augmentation is a cohomology isomorphism
\[
 I^\bullet(U)\longrightarrow
 \operatorname{Tot}\check C^\bullet(\mathcal U,I^\bullet),
 \quad
 d=d_h+(-1)^p d_v\text{ in bidegree }(p,q).
 \tag{SC14}
\]
In every total degree only finitely many bidegrees occur. No convergence assumption for an unbounded filtration is required.

*Proof.* The horizontal and vertical differentials commute, so the two mixed terms in \(d^2\) cancel; their separate squares are zero. Each augmented horizontal row is exact by SH8. Take a total cocycle of degree \(n\). Its component of largest positive horizontal degree \(p\) is horizontally closed: the next horizontal component of its boundary has no other contributor. Row exactness expresses that component as \(d_hb\). Subtract \(db\); this removes it and creates components only at smaller horizontal degrees. After finitely many repetitions, the cocycle has horizontal degree zero only. It is horizontally closed, so it is the augmentation of a section in \(I^n(U)\); the vertical cycle identity says that this section is closed.

For injectivity, if an augmented cocycle is a total boundary, perform the same elimination on the primitive, starting with its largest positive horizontal degree. Since the boundary has horizontal degree zero only, its largest component is horizontally closed. After the finite elimination the primitive is horizontally closed in degree zero, and therefore is the augmentation of a section in \(I^{n-1}(U)\). The original cocycle was already a boundary there. For degree zero the absence of negative-degree primitives gives injectivity directly. This proves (SC14).

In a fixed column the vertical complex is a product of the restricted injective resolutions on the objects in (SC12). SH5 computes its cohomology as the corresponding product of \(H^q(U_{i_0\ldots i_p},F)\). Products of groups are exact: lifts across surjections can be chosen independently in every component. For a finite cover, the products at each degree are finite, so SH2 also justifies commuting them with filtered colimits. Together SH4, SH8 and (SC14) supply the exact row, local-vanishing and finite-diagonal arguments used in Lemma 6.5. \(\square\)

The free reference material is the Stacks project authors' [abelian-sheaf constructions](https://stacks.math.columbia.edu/tag/03CM), [injective existence theorem](https://stacks.math.columbia.edu/tag/01DL), [point criteria](https://stacks.math.columbia.edu/tag/00YJ), and [cohomology-on-sites chapter](https://stacks.math.columbia.edu/download/sites-cohomology.pdf). SH1–SH9 give the proofs used here; in particular SH3 constructs its injective extension directly, and SH9 supplies the finite elimination. These references are reading material, not substitutes for any step. The geometric hypotheses needed to apply them to the étale basis of Section 6 remain separately specified there.

### 5A.10. Graded exercise: local lifts, slices and one covering map

**Exercise 5A.1 (100 points).** Work on the sites and with the definitions of SH1–SH9.

1. **(10 points)** Prove the zero criterion for the original presheaf map \(P\to P^\#\). Explain why a surjection of sheaves need not be surjective on sections.
2. **(10 points)** Prove exactness of a filtered colimit of sheaf short exact sequences without assuming the colimit is sectionwise.
3. **(10 points)** Verify the kernel calculation in (SC4) and injectivity of the first arrow into (SC5).
4. **(10 points)** Identify both cardinal bounds needed at the last limit in SH3. Explain why bounding only the sections of the extension domains is insufficient.
5. **(10 points)** Verify the adjunction (SC7) and prove its exactness by a finite-support lifting argument.
6. **(10 points)** In (SC9), construct a common refinement and an equalizer refinement. Explain which direction the restriction maps have.
7. **(10 points)** Derive (SC8) and (SC11) without applying a continuity theorem.
8. **(10 points)** Prove (SC13), including degree \(-1\), and check the sign in (SC14).
9. **(10 points)** Let \(G=\{1,s\}\), \(s^2=1\). On the site of finite left \(G\)-sets with jointly surjective covers, let \(F(V)\) be the \(G\)-invariant functions \(V\to\mathbb F_2\). For the single covering map \(G\to\{*\}\), compute its first Čech cohomology with the full nerve.
10. **(10 points)** Explain why the preceding calculation invalidates the “distinct indices only” truncation for that cover. State precisely which étale prerequisites SH1–SH9 do and do not prove.

*Full solution.*

1. SH1 first says that a section maps to zero in \(P^+\) exactly when it vanishes on a covering. If its image vanishes in \((P^+)^+\), restrict to a covering where it is zero in \(P^+\), then to the coverings witnessing those zeros in \(P\). The composite is a covering of the original object. Conversely restriction-zero sections clearly become zero in both plus steps. A sheaf epimorphism means every section lifts on a covering by (SC2); the local lifts can differ on overlaps by kernel sections and therefore need not glue to a global lift. The epimorphism assertion alone provides no compatible choice of lifts.

2. A target representative at stage \(i\) lifts locally at stage \(i\). A middle representative with zero image in the sheafified colimit is, by SH1, zero in the group colimit after a covering. On each member it becomes zero at a later stage; exactness there supplies another covering with lifts from the left sheaf. Compose those coverings. The left colimit is injective because all stage maps on sections are injective, filtered group representatives preserve injectivity, and SH1 preserves it under sheafification. This gives all three exactness assertions.

3. If \(c+p(v)=0\), then \(p(v)=-c\in C\), so \(v\in K\), and the pair is \((-p(v),v)\). Conversely each such pair is in the kernel. On it (SC4) is \(-\phi(p(v))+t(v)=0\) by the extension condition. In (SC5), a relation whose second component is zero comes from an element of the direct sum of the \(K\) whose image in the direct sum of the \(P_U\) is zero. That inclusion is injective by SH2, so the relation is zero. Consequently the map from \(F_\alpha\) is injective.

4. First bound the entries and compatibility equations of covering sieves; this makes the final pointwise colimit a sheaf. Second bound all sections and restriction equations of every \(K\subset P_U\); this makes a map out of \(K\) factor through one stage. The first assertion is required before the second can use section representatives in the final colimit. Without a bound on covering size, a matching family could require stages cofinal in the last ordinal and fail to have a representative at any earlier stage. This is why a bound on extension-domain sections alone is insufficient.

5. A presheaf map out of the direct sum in (SC7) is a map on each summand \(G(V,\phi)\), natural for every arrow over \(U\). These are exactly a slice map into \(r_UF\). SH1 supplies and uniquely determines its sheaf extension. For exactness, a presheaf section has finitely many summands. Lift or kill each one on a slice covering, then use successive fibre products for a common refinement. Its underlying covering in \(\mathcal C\) supplies the required witness after sheafification. Monomorphisms remain injective on every summand, and SH1 preserves their injection. Thus this is an exact left adjoint, so SH5's extension argument really proves preservation of injectives by slice restriction.

6. For \((V,\beta)\) and \((V',\beta')\), take \(V\times V'\); finite-limit preservation gives its map from \(W\), with the two given components. For two parallel refinements, take their equalizer in \(\mathcal C\). Its image under \(a\) is the equalizer, so the chosen map from \(W\) factors through it. A refinement arrow goes from the smaller source neighbourhood to the larger one; the contravariant presheaf restriction goes in the reverse direction and is the colimit transition. The terminal object ensures this category is nonempty. These are exactly the filtered axioms in the direction used by (SC9).

7. Evaluate \(f_*I^\bullet\) on \(V\). It is the complex \(I^\bullet(aV)\); SH5 says restriction to that slice preserves its injective resolution. Its group cohomology is \(H^n(aV,G)\). SH1 turns the presheaf cohomology into the sheaf cohomology, proving (SC8). SH7 says stalks are the filtered neighbourhood colimit and that sheafification leaves them unchanged; applying it to (SC8) proves (SC11). Neither step identifies a cohomology group with that of a limit scheme.

8. In degree \(p\geq0\), the first term in the boundary of an inserted tuple returns the original tuple. Its remaining \(p+1\) terms cancel with insertion after the corresponding deletions, because their signs differ by one exponent. In degree \(-1\), the augmentation of the chosen lift is \(1\). These prove (SC13) at every augmented degree. The mixed terms of the total differential on bidegree \((p,q)\) have coefficients \((-1)^{p+1}\) and \((-1)^p\); they cancel since \(d_h\) and \(d_v\) commute. Their individual squares vanish, so the total differential has square zero.

9. Invariant functions form a sheaf: a jointly surjective cover supplies the values everywhere; equality on pairwise fibre products makes those values independent of the lift; equivariance descends because all covering maps are equivariant. The diagonal \(G\)-action on \(G^{p+1}\) has orbit coordinates given by successive ratios, so the first three Čech groups are
\[
 \check C^0=\mathbb F_2,\qquad
 \check C^1=\operatorname{Map}(G,\mathbb F_2),\qquad
 \check C^2=\operatorname{Map}(G^2,\mathbb F_2).
 \tag{SCT1}
\]
The first differential is zero, and the next one is
\[
 (dc)(g,h)=c(h)-c(gh)+c(g).
 \tag{SCT2}
\]
Evaluate at \((1,1)\): a cocycle has \(c(1)=0\). At \((s,s)\) the condition is \(2c(s)-c(1)=0\), automatically satisfied in \(\mathbb F_2\). The pairs \((1,s)\) and \((s,1)\) give the same already satisfied condition. Thus \(c(s)\) is arbitrary, and there are no nonzero boundaries:
\[
 \check H^1(G\to\{*\},F)=\mathbb F_2.
 \tag{SCT3}
\]
This is a Čech computation; no identification with derived cohomology is needed for the counterexample.

10. A distinct-indices truncation would have no positive terms for this single-map cover, and would incorrectly make the group in (SCT3) zero. A repeated index represents a genuine self-fibre product here, not a redundant copy of the same open set. SH1–SH9 prove abstract sheafification, exact colimits, enough injectives, derived comparison, local vanishing, exact slice restriction, the finite-limit site adjunction, its higher-image presheaf, abstract point stalks, and the full covering contraction. They do not prove the algebraic étale local form, flatness, open images, geometric conservativity, finite-data scheme descent or the identification of a neighbourhood ring with a strict henselization. Those remain explicit prerequisites for the geometric application in Section 6. \(\square\)

## 5B. The algebra and geometry of the étale site

This section proves the geometric inputs used by Section 6. All base rings are commutative with identity, and no Noetherian hypothesis is imposed on an étale base ring. Noetherian completion is an intermediate tool whose hypotheses are proved and checked below. The local presentations are square-Jacobian presentations; a monic one-variable presentation is one special case. The continuity proof only requires the square-Jacobian form and the open-image theorem proved here.

The reading order is the following. Basic module and finite-presentation arguments come first. They lead to finite field fibres and a complete-local lifting calculation. That calculation proves flatness of every square-Jacobian chart, including over an arbitrary base. We then prove the full étale criterion, open images, the finite-cover basis, and the conservative geometric stalks. The final construction gives the actual local étale neighbourhood ring used in Corollary 6.8.

### 5B.1. Fractions, finite modules and principal patching

**EA1.** Localization of modules is exact. Tensor product is right exact and commutes with colimits. A module is zero if all its prime localizations are zero. A finitely generated module over a local ring satisfies Nakayama's lemma.

*Proof.* In \(S^{-1}M\), a fraction \(m/s\) is zero exactly when some \(t\in S\) kills \(m\). This tests kernels and images in any localized exact sequence, and representatives lift across a surjection. Tensor product is the abelian group generated by symbols \(m\otimes n\), modulo additivity and scalar-balancing relations. Quotienting one factor therefore quotients the tensor product by exactly the corresponding relations; this proves right exactness. The same presentation proves commutation with colimits. In a filtered colimit any element or equality involves only finitely many representatives and relations, so occurs at one common stage.

If \(0\ne m\in M\), choose a maximal ideal containing its proper annihilator. The element \(m/1\) cannot be zero at that ideal, because an element outside the ideal cannot belong to the annihilator. This proves the localization test. It also proves the useful finite witness: if a finite module \(M\) has \(M_{\mathfrak p}=0\), choose one denominator outside \(\mathfrak p\) killing each of its finitely many generators; their product kills the whole module.

For Nakayama, let \(M=JM\), with generators \(m_1,\ldots,m_r\) and \(J\) contained in the maximal ideal of a local ring \(R\). Write \(m_i=\sum_j a_{ij}m_j\), \(a_{ij}\in J\). Multiplying by the adjugate of \(1-(a_{ij})\) shows that its determinant kills every generator. The adjugate identity follows from the determinant expansion: an off-diagonal entry is the determinant with two equal rows and is zero, while each diagonal entry is the determinant. The determinant is congruent to \(1\) modulo the maximal ideal, so is a unit. Hence \(M=0\). Applying this to a finite quotient also shows that elements generating \(M/JM\) lift to generators of \(M\). \(\square\)

For later use, tensoring \(0\to K\to P\to B\to0\) with any module remains exact on the left if \(B\) is flat. Here is an elementary proof. Present the module as \(N=F/L\), with \(F\) free. If an element of \(K\otimes F\) maps into the image of \(P\otimes L\), choose such a representative there. Its image in \(B\otimes L\) maps to zero in \(B\otimes F\); flatness makes that map injective. Right exactness then lifts the representative from \(K\otimes L\). Since \(K\otimes F\to P\otimes F\) is injective for a free \(F\), the original element already vanishes in \(K\otimes N\). Thus
\[
 0\longrightarrow K\otimes N\longrightarrow P\otimes N
 \longrightarrow B\otimes N\longrightarrow0
 \quad\text{if }B\text{ is flat}.
 \tag{ET1}
\]

**EA2.** A finite principal cover of \(\operatorname{Spec}R\) gives the usual gluing of modules and rings. Its existence and inclusions of principal opens have finite power witnesses.

*Proof.* We first prove the prime test used in the topology. If \(f\) is not in the radical of an ideal \(J\), the powers of \(f\) avoid \(J\). A maximal ideal among ideals containing \(J\) and avoiding these powers exists by Zorn. It is prime: if neither \(a\) nor \(b\) belongs to it, each of the enlarged ideals meets the powers of \(f\); multiplying the two witnessing equations shows that \(ab\) cannot belong to the original ideal. This produces a prime containing \(J\) and avoiding \(f\). Consequently
\[
 D(f)\subset\bigcup_iD(g_i)
 \quad\Longleftrightarrow\quad
 f^N=\sum_i c_i g_i
 \quad\text{for some finite sum and }N.
 \tag{ET2}
\]
In particular principal opens cover the whole spectrum exactly when their elements generate the unit ideal. Every cover of an affine spectrum by principal opens has a finite subcover: the equation for \(1\) is finite. The nilradical is the intersection of the prime ideals, by the same test.

Suppose \(D(c_1),\ldots,D(c_r)\) cover. For any common sufficiently large exponent \(N\), their powers still generate the unit ideal, by (ET2), so choose \(\sum_i a_i c_i^N=1\). If elements \(m_i\in M_{c_i}\) agree on overlaps, clear the finitely many denominators and overlap witnesses until \(c_i^N m_i\) is represented by \(n_i\in M\) and \(n_i=c_i^N m_j\) in every \(M_{c_j}\). Then
\[
 m=\sum_i a_i n_i
 \tag{ET3}
\]
restricts to each \(m_j\). If a global element is zero on all members, sufficiently large powers of all the \(c_i\) kill it; the unit equation kills it. This proves uniqueness. Taking \(M=R\) gives ring gluing, since addition and multiplication can be checked on the cover. It constructs the structure sheaf on principal opens with sections \(R_f\); its stalk at \(\mathfrak p\) is \(R_{\mathfrak p}\).

A ring map \(A\to B\) gives a map of these affine schemes by inverse images of primes and the maps on fractions. Conversely a morphism of affine schemes gives a map on global sections; the unit test in local rings identifies its inverse images of \(D(a)\), and hence its point map and all maps on fractions. Thus affine scheme maps correspond to ring maps. Affine fibre products are spectra of tensor products: maps out of the tensor product correspond exactly to pairs of compatible ring maps. For general schemes these affine constructions glue on common refinements. Gluing along open isomorphisms satisfying a cocycle consists of the quotient of the disjoint union by these identifications, with the section sheaf glued by (ET3); each chart remains an open affine chart. Compatible chart maps glue uniquely. These constructions also verify the stated fibre-product universal property. \(\square\)

**EA3.** Finite presentation is local on a finite principal cover of the source.

*Proof.* Let \(B\) be an \(A\)-algebra and suppose \(B_{b_i}\) is finitely presented over \(A\) for a finite principal cover of \(\operatorname{Spec}B\). Choose finite algebra generators in each localization, with their numerators in \(B\), and choose coefficients of a unit equation in the \(b_i\). Let \(C\subset B\) be the \(A\)-subalgebra generated by these finitely many numerators, coefficients and elements \(b_i\). The same unit equation holds in \(C\), and \(C_{b_i}\to B_{b_i}\) is surjective. The \(C\)-module \(B/C\) is therefore zero at each \(b_i\). For each of its elements, finitely many localization witnesses and a unit equation as in EA2 show it is zero. Thus \(C=B\), so \(B\) is finitely generated over \(A\).

Choose a surjection \(P=A[Z_1,\ldots,Z_t]\to B\), with kernel \(J\). We need its relations to be finite. The following comparison verifies independence of a finite presentation from the chosen generators. If \(B=A[Y_1,\ldots,Y_s]/(r_1,\ldots,r_e)\), write \(Y_i=p_i(Z)\) and \(Z_j=q_j(Y)\) in \(B\). Then
\[
 J=(r_i(p(Z)),\ Z_j-q_j(p(Z))).
 \tag{ET4}
\]
The two substitution maps give inverse maps between the quotient on the right and \(B\); the relations \(Y_i-p_i(q(Y))\) already hold modulo the \(r_i\). This proves (ET4). The same reasoning, adding one generator for an inverse, applies to a localized polynomial algebra.

Lift \(b_i\) to \(\widetilde b_i\in P\). The localized ideals \(J_{\widetilde b_i}\) are consequently finite. Choose finitely many elements of \(J\) generating them after localization. Add to their ideal \(J_0\) a lift of the unit equation \(1-\sum_i c_i b_i^N\). In \(P/J_0\) the \(\widetilde b_i\) now generate the unit ideal and \((J/J_0)_{\widetilde b_i}=0\) for every \(i\). EA2 again gives \(J/J_0=0\). Thus \(J\) is finitely generated. This proves finite presentation. \(\square\)

Localization \(A\to A_f\) is finitely presented by adjoining an inverse with relation \(fZ-1\). Composition of finitely presented algebra maps is finitely presented: combine the two finite lists of generators and lift the second list of relations to the first polynomial presentation. Base change preserves finite presentation by applying the same presentation to the new coefficient ring.

### 5B.2. Noetherian algebra and finite field extensions

**EA4.** Polynomial rings over Noetherian rings, their quotients and localizations are Noetherian. Finite modules over a Noetherian ring have finite submodules. A Noetherian spectrum has finitely many irreducible components.

*Proof.* For a submodule of \(A^r\), project to its last coordinate. The image is an ideal, and the kernel is a submodule of \(A^{r-1}\). Induction supplies finite generators for both and hence for the original submodule. Presenting a finite module as a quotient of \(A^r\) gives the assertion for all finite modules.

For an ideal \(J\subset A[T]\), its leading coefficients form an ideal of \(A\): align degrees by powers of \(T\) before adding, and scalar multiplication preserves a leading coefficient unless it becomes zero. Choose finitely many polynomials of \(J\) whose leading coefficients generate that ideal, and let \(d\) bound their degrees. Every polynomial of degree at least \(d\) can have its leading term canceled by multiples of these chosen polynomials; repetition leaves degree less than \(d\). The elements of \(J\) of degree less than \(d\) form an \(A\)-submodule of \(A^d\), so are finitely generated by the preceding paragraph. These two lists generate \(J\). Iteration gives several variables. Ideals of a quotient lift to ideals; ideals of a localization are extensions of their contractions. Both therefore stay finite. The integers are Noetherian because a nonzero ideal is generated by its least positive element, using division with remainder. In particular every finitely generated subring generated from the integers is Noetherian.

Closed subsets form a descending-chain-finite collection because their radical ideals form ascending chains. A minimal closed set failing to be a finite union of irreducible closed sets could be decomposed into two proper closed subsets, each a finite union by minimality. This is a contradiction. An irreducible closed set is \(V(\mathfrak p)\) for a prime \(\mathfrak p\): if a product belongs to its radical but neither factor does, its two vanishing subsets give a forbidden decomposition; the converse follows because nonempty principal opens in a prime spectrum intersect. Its generic point is \(\mathfrak p\). This proves the component assertion and the Noetherian closed-subset induction used later. \(\square\)

**EA5.** Every finitely generated domain over a field is finite over a polynomial subalgebra. Every field finitely generated as an algebra over a field is a finite algebraic extension.

*Proof.* Write the domain as \(k[x_1,\ldots,x_n]\). If the generators are algebraically independent, there is nothing to prove. Otherwise choose a nonzero polynomial relation whose exponents are at most \(D\), and put \(b=D+1\). For \(i<n\), make the polynomial substitution
\[
 X_i=Y_i+X_n^{b^i}.
 \tag{ET5}
\]
The powers of \(X_n\) contributed by the leading substitutions of distinct monomials are distinct, because their exponents are the distinct base-\(b\) integers \(a_n+\sum_{i<n}a_i b^i\). Thus the transformed relation has a unique highest \(X_n\)-term with nonzero constant coefficient. Divide by this coefficient to make it monic. Hence \(x_n\) is integral over \(k[y_1,\ldots,y_{n-1}]\), and the original generators are polynomials in \(x_n\) and these \(y_i\). A monic equation bounds the necessary powers of \(x_n\), so the domain is a finite module over that smaller generated domain. Induct on the number of generators. Finiteness is transitive because products of two finite generating lists generate the composite module. This proves the first assertion in every characteristic.

If the domain is itself a field \(L\), its polynomial subalgebra must be a field as well. Indeed in a finite extension every element is integral: write multiplication on a finite generating tuple and apply the adjugate to the matrix \(TI-M\), then apply the resulting monic relation to the element \(1\). In particular \(a^{-1}\in L\) is integral for each nonzero \(a\) in the subalgebra. Multiplying its monic equation by \(a^{n-1}\) expresses \(a^{-1}\) in that subalgebra. A polynomial algebra in a positive number of variables is not a field, since quotienting by one variable gives a nonzero ring. Thus there are no variables and \(L/k\) is finite.

We will also use finite lying over in this specific scope. If \(R\hookrightarrow C\) is an injective finite algebra map and \(\mathfrak p\) is a prime of \(R\), then \(C_{\mathfrak p}\) is a nonzero finite \(R_{\mathfrak p}\)-module. Nakayama prevents \(C_{\mathfrak p}/\mathfrak pC_{\mathfrak p}\) from being zero. A maximal ideal of this nonzero algebra gives a prime of \(C\) over \(\mathfrak p\). \(\square\)

Polynomial division over a field cancels the leading term at each step and ends at smaller degree. The Euclidean algorithm therefore computes a greatest common divisor; tracing its successive remainder equations expresses that divisor as a combination of the original polynomials. In particular coprimality gives a Bézout equation. We use this elementary polynomial test for the factor equations below.


A finite separable field extension has a primitive element. Over an infinite base, combine two generators as \(\alpha+c\beta\), avoiding the finitely many scalars at which two embeddings coincide; Lemma 0B.1 shows that the number of distinct embeddings then forces this element to generate. Induct on the generator list. Over a finite base, a finite extension is a finite field whose multiplicative group is cyclic: in a finite abelian group, products of elements of relatively prime orders have the product order, so combining their prime-power parts realizes the exponent as an element order. In a field the polynomial with that exponent has at most that many roots, so the group order is at most the exponent and hence equals it. A generator of the multiplicative group generates the field. This proves the primitive-element fact in both cases without a cardinality restriction on the base.

### 5B.3. Completion, including the flatness proof

**EA6.** Let \(A\) be Noetherian, \(I\subset A\), and \(N\subset M\) finite modules. There is \(c\) such that
\[
 N\cap I^nM=I^{n-c}(N\cap I^cM)\qquad(n\geq c).
 \tag{ET6}
\]
Completion is exact on finite modules, and
\[
 \widehat M=\widehat A\otimes_A M.
 \tag{ET7}
\]

*Proof.* The Rees algebra \(A[It]\) is generated by finitely many \(a_it\), so is Noetherian by EA4. The graded module \(\bigoplus_{n\geq0}I^nM\,t^n\) is finite over it, generated in degree zero. Its submodule \(\bigoplus(N\cap I^nM)t^n\) is finite. Split its finite generators into homogeneous parts, and bound their degrees by \(c\). Raising each smaller degree to \(c\) gives exactly (ET6); the reverse inclusion follows by multiplying elements already in the intersection.

For \(0\to N\to M\to Q\to0\), the exact quotient sequences have left term \(N/(N\cap I^nM)\). Their transition maps on these left terms are surjective. A compatible element on the right has compatible middle lifts: after choosing a lift at level \(n+1\), subtract a lift of its discrepancy in the left term at level \(n\). Induction constructs all levels. Kernels are identified level by level. Thus their inverse limit is exact. The two filtrations on \(N\) are cofinal by (ET6), so the left limit is \(\widehat N\), proving exact completion.

A finite presentation \(A^s\to A^r\to M\to0\) exists by EA4. Its completed cokernel is the cokernel of \(\widehat A^s\to\widehat A^r\). Right exactness of tensor product identifies this with \(\widehat A\otimes_A M\), proving (ET7). \(\square\)

**EA7.** The completion of a Noetherian ring is Noetherian and flat. The maximal-ideal completion of a Noetherian local ring is local and faithfully flat, has the same residue field, and is separated and complete for its extended maximal ideal.

*Proof.* Equations (ET6)–(ET7) show that tensoring with \(\widehat A\) preserves injections between finite \(A\)-modules. This implies flatness on all modules, not only on finite ones. Given any injection \(M'\subset M\), write \(M\) as the filtered union of its finite submodules \(M_j\). Each intersection \(M'\cap M_j\) is finite by EA4, and these intersections exhaust \(M'\). The corresponding finite injections remain injective after tensoring. Filtered colimits of groups are exact by their finite-representative description, and tensor product commutes with them by EA1. Hence the original injection remains injective.

For every \(n\), exact completion of \(0\to I^n\to A\to A/I^n\to0\) gives
\[
 \widehat A/I^n\widehat A=A/I^n.
 \tag{ET8}
\]
The image of \(\widehat{I^n}=\widehat A\otimes I^n\) is exactly \(I^n\widehat A\), and the completion of the right module is itself. Thus \(\widehat A\) is complete and separated for \(I\widehat A\), with the same associated graded ring. That graded ring is a quotient of a polynomial algebra over \(A/I\), on the initial classes of finite generators of \(I\), and is Noetherian by EA4.

To prove that \(\widehat A\) is Noetherian, let \(J\) be any ideal. Its graded ideal of initial forms has a finite list of homogeneous generators represented by \(g_j\in J\) of orders \(d_j\). They may be chosen from actual initial forms: a finite generating list of the ideal involves only finitely many of those forms. For \(x\in J\), cancel its initial form by a combination of the \(g_j\), choosing the coefficients in \(I^{\max(0,n-d_j)}\widehat A\) when the remainder has order \(n\). The remainder's order rises by at least one. The coefficients accumulated for each \(g_j\) are Cauchy and converge in the complete ring. Separatedness gives \(x=\sum_j a_jg_j\) at the limit. Thus these finitely many elements generate the actual ideal, without assuming it is closed.

For a local ring with \(I=\mathfrak m\), (ET8) gives residue field \(k\). An element with nonzero residue is a unit: multiply by a lift of the residue inverse, then invert \(1-u\), \(u\in\mathfrak m\widehat A\), by the convergent series \(\sum_{r\geq0}u^r\). This proves that \(\widehat A\) is local. Its flatness is already proved. For a nonzero module, a nonzero element gives an injection \(A/J\hookrightarrow M\) with \(J\) proper and hence contained in \(\mathfrak m\). Tensoring preserves that injection, and \(\widehat A/J\widehat A\) maps onto the nonzero residue field. Consequently tensoring cannot kill a nonzero module. This is faithful flatness. \(\square\)

Here is the complete-local vector lifting used below. If \(R\) is complete and separated for its maximal ideal, a polynomial system \(F=(F_1,\ldots,F_n)\) and a residue solution \(a\) with invertible Jacobian determinant have exactly one lift with that residue. Choose an initial lift and repeatedly set
\[
 a_{\mathrm{new}}=a-J_F(a)^{-1}F(a).
 \tag{ET9}
\]
The polynomial Taylor formula has remainder in the square of the correction ideal; this follows by expanding monomials, with no division by factorials. The errors successively belong to \(\mathfrak m,\mathfrak m^2,\mathfrak m^4,\ldots\), and the Jacobian stays invertible because its reduction stays fixed. Completeness gives a root. If two roots differ by a vector in \(\mathfrak m^r\), the same Taylor formula and the inverse Jacobian put their difference in \(\mathfrak m^{2r}\). Separatedness proves uniqueness. This extends the one-variable proof of Lemma 0D.1.

### 5B.4. Differentials and infinitesimal lifting

For an \(A\)-algebra \(B\), define \(\Omega_{B/A}\) as the \(B\)-module on symbols \(db\), modulo additivity, the product rule and \(da=0\) for \(a\in A\). A map from it to a \(B\)-module is exactly an \(A\)-derivation, by its presentation. For \(P=A[X_1,\ldots,X_n]\), polynomial expansion proves that a derivation is determined freely by the \(dX_i\). If \(B=P/K\), descending a derivation is exactly killing the derivatives of elements of \(K\), so
\[
 K/K^2\xrightarrow{\alpha} B^n\longrightarrow\Omega_{B/A}
 \longrightarrow0,\qquad
 \alpha(f)=(\partial_1f,\ldots,\partial_nf).
 \tag{ET10}
\]
The product rule makes \(\alpha\) well defined. Differentials commute with localization and base change: derivations of a fraction use \(d(s^{-1})=-s^{-2}ds\), and the universal generators after scalar extension give the same presentation. These explicit rules prove the assertions.

A ring map is formally étale if, for every \(A\)-algebra \(C\) and ideal \(J\) with \(J^2=0\), every \(A\)-map \(B\to C/J\) has a unique lift to \(C\). A square-Jacobian chart is
\[
 B=\left(A[X_1,\ldots,X_n]/(F_1,\ldots,F_n)\right)_{h\Delta},
 \qquad
 \Delta=\det(\partial_jF_i).
 \tag{ET11}
\]
The case \(n=0\) is a localization.

**EA8.** Each chart (ET11) is formally étale and has zero differentials.

*Proof.* Lift the images of the \(X_i\) arbitrarily to \(C\). The errors \(F_i(a)\) lie in \(J\), and the Jacobian is invertible: an element invertible modulo a nilpotent ideal is invertible, since a lifted inverse differs from an inverse by a finite geometric-series correction. The correction \(-J_F(a)^{-1}F(a)\) belongs to \(J^n\). Taylor expansion has zero remainder because \(J^2=0\), so it gives an exact root. Any two lifts differ by such a vector, and their difference is killed by the invertible Jacobian; hence it is zero. The inverted element stays a unit and its inverse is uniquely determined. Formula (ET10) gives \(\Omega=0\). Iterating the square-zero lift through the quotients \(C/J^r\) proves unique lifting for every nilpotent \(J\). \(\square\)

**EA9.** A finitely presented formally étale algebra is covered by principal charts of the form (ET11).

*Proof.* Write \(B=P/K\) with \(K\) finite. Uniqueness applied to the square-zero ring \(B\oplus M\) makes every derivation to \(M\) zero: the two maps \(b\mapsto(b,0)\) and \(b\mapsto(b,db)\) would otherwise differ. Taking \(M=\Omega_{B/A}\) gives \(\Omega=0\), so (ET10) makes \(\alpha\) surjective.

Existence supplies a section \(s:B\to P/K^2\). The difference \(p\mapsto p-s(\bar p)\) is a derivation into \(K/K^2\), with the \(B\)-action, and restricts to the identity on that module. Thus it gives \(\beta:B^n\to K/K^2\) with \(\beta\alpha=1\). Surjectivity makes \(\alpha\) an isomorphism. Choose \(f_1,\ldots,f_n\in K\) whose derivative vectors are the standard basis modulo \(K\). Then they generate \(K/K^2\), and their Jacobian determinant is \(1\) modulo \(K\).

At a prime \(Q\) of \(P\) containing \(K\), the finite module \(K_Q/(f_1,\ldots,f_n)_Q\) equals \(K_Q\) times itself. Nakayama gives zero. EA1 gives an element \(h\notin Q\) where \(K_h=(f_1,\ldots,f_n)_h\). Inverting also the Jacobian determinant therefore gives the required chart around the image point. These principal charts cover \(\operatorname{Spec}B\); EA2 gives a finite subcover. \(\square\)

### 5B.5. The field fibre and its infinitesimal structure

**EA10.** A finite-type algebra over a field with zero differentials is a finite product of finite separable field extensions. These products are formally étale.

*Proof.* First extend scalars from \(k\) to an algebraic closure \(\overline k\); the differentials stay zero by (ET10). The resulting algebra \(D\) is Noetherian by EA4. At a maximal ideal its residue field is \(\overline k\) by EA5. For the local algebra \(L=D_{\mathfrak n}\), the residue map splits its \(\overline k\)-structure and gives
\[
 \mathfrak nL/(\mathfrak nL)^2
       \simeq\Omega_{L/\overline k}\otimes_L\overline k.
 \tag{ET12}
\]
Indeed \(b\mapsto b-\bar b\) modulo the square is a derivation into the left module, and \(u\mapsto du\) gives the inverse on generators. The product rule verifies the first map because the product of the two differences vanishes modulo the square. Thus (ET12) is zero. Nakayama applied to the finite maximal ideal makes it zero, so every such local ring is a field.

Every prime is contained in a maximal ideal. Localizing there now shows that the prime equals that maximal ideal. EA4 therefore makes the spectrum a finite set of maximal ideals. The algebra is reduced: a nilpotent element vanishes in all its local fields and hence is zero by EA1. The finite maximal ideals are pairwise comaximal and their intersection is zero by EA2. Chinese remaindering gives \(D\simeq\overline k^{\,r}\). To check that remaindering, for \(I+J=R\) choose \(a+b=1\), \(a\in I,b\in J\); the element \(x b+y a\) has the prescribed residues \(x,y\), and the kernel is \(I\cap J=IJ\). Induction gives the finite product.

Independent vectors over \(k\) remain independent after a field extension, by extending them to a vector-space basis. Thus the original algebra has finite dimension, since its scalar extension has dimension \(r\). It is reduced for the same scalar-extension reason, and decomposes into finite field factors by the same prime and remainder argument. Every factor \(K\) is separable: if some element had an inseparable minimal polynomial \(f\), then \(\overline k[T]/(f)\) would have a nonzero nilpotent, from its repeated roots. This algebra injects into \(\overline k\otimes_k K\), because field scalar extension preserves injections. That contradicts its reducedness. Conversely the primitive-element result after EA5 identifies a separable factor with \(k[T]/(f)\), \(f'\) invertible, so it is a chart (ET11) and is formally étale by EA8.

For a product of these factors we must also lift the idempotents. If \(J^2=0\), lift an idempotent to \(u\in C\), put \(\delta=u^2-u\in J\), and note that \((2u-1)^2=1+4\delta\) is a unit. Then
\[
 e=u-(2u-1)^{-1}\delta,\qquad e^2=e.
 \tag{ET13}
\]
If two idempotents differ by \(a\in J\), their equation gives \((2e-1)a=0\); since \((2e-1)^2=1\), they coincide. No inversion of \(2\) was used. The lifted product idempotents are orthogonal: their pairwise products are idempotents lifting zero and so are zero. Their sum is an idempotent lifting \(1\) and so is \(1\). They split \(C\) into its corresponding factor rings. Lift each separable field map in that factor using EA8, then combine the maps. The idempotents and field lifts are unique. This proves the product assertion. \(\square\)

For any square-Jacobian chart, (ET10) gives zero differentials on each field fibre. EA10 therefore makes every nonempty fibre a finite disjoint union of separable points. In particular a point \(\mathfrak q\) over \(\mathfrak p\) has a finite separable residue extension, and
\[
 \mathfrak pB_{\mathfrak q}=\mathfrak qB_{\mathfrak q}.
 \tag{ET14}
\]
The local fibre is a field; the equality follows by taking its maximal ideal. This assertion precedes, and is not obtained by assuming, flatness.

### 5B.6. Flatness of the square-Jacobian chart over every base

**EA11.** Every chart (ET11) is flat over \(A\), including when \(A\) is not Noetherian.

*Proof.* Suppose first \(A\) is Noetherian. Its chart algebra is Noetherian by EA4. Fix \(\mathfrak q\), with contraction \(\mathfrak p\), and complete the local rings:
\[
 R=\widehat{A_{\mathfrak p}},\qquad
 S=\widehat{B_{\mathfrak q}}.
 \tag{ET15}
\]
EA7 constructs their complete local structures and residue fields. The base map extends to \(R\to S\): maximal-ideal powers in the first ring map into those in the second, so a Cauchy sequence has a unique image limit.

Choose a primitive element \(\theta\) of the finite separable residue extension \(K/k\) in EA10 and a monic lift \(f\) of its minimal polynomial to \(A_{\mathfrak p}[T]\). Put \(R'=R[T]/(f)\). Monic division gives a free \(R\)-module with basis \(1,T,\ldots,T^{d-1}\): a nonzero multiple of a monic polynomial cannot have degree below \(d\), even when coefficients have zero divisors. Thus \(R'\) is complete and separated coordinate by coordinate and has residue field \(K\). Its maximal ideal is \(\mathfrak m_RR'\); an element with nonzero residue has an inverse by the geometric series from EA7. It is Noetherian by EA4.

The images of the chart coordinates in \(K\) solve its equations with invertible Jacobian. Formula (ET9) gives their unique lifts to \(R'\); the inverted element has nonzero residue, so is a unit. This defines a local map \(B_{\mathfrak q}\to R'\), because every element outside \(\mathfrak q\) still has nonzero residue. It extends continuously to \(S\to R'\).

In the other direction lift \(\theta\) to \(S\) and use Lemma 0D.1 to lift the simple root of \(f\). This gives \(R'\to S\). The composite on \(R'\) fixes \(R\) and sends \(T\) to a root with its prescribed residue, so uniqueness of the simple-root lift makes it the identity. The other composite fixes the chart coordinates by the vector uniqueness in (ET9), and therefore fixes \(B_{\mathfrak q}\), including all its denominators. Continuity and density make it the identity on \(S\). We have proved, as rings,
\[
 S\simeq R[T]/(f),
 \quad\text{finite free of rank }[K:k]\text{ over }R.
 \tag{ET16}
\]
This statement does not assert that the original chart is finite over \(A\).

EA7 makes \(R\) flat over \(A_{\mathfrak p}\), so \(S\) is flat over it. The same lemma makes \(S\) faithfully flat over \(B_{\mathfrak q}\). For any injection of \(A_{\mathfrak p}\)-modules, the kernel after tensoring with \(B_{\mathfrak q}\) becomes zero after tensoring with \(S\), and faithful flatness forces that kernel to be zero. Thus \(B_{\mathfrak q}\) is flat over \(A_{\mathfrak p}\). Localizing a proposed tensor kernel on \(\operatorname{Spec}B\) now gives zero everywhere; EA1 forces it to be zero. This proves flatness of \(B\) over the Noetherian \(A\).

For an arbitrary \(A\), put all finitely many coefficients of \(F_i,h\) into the subring \(A_0\) generated by them and the integers. EA4 makes \(A_0\) Noetherian. Define exactly the same chart over it, inverting \(h\Delta\); the preceding proof makes that chart \(B_0\) flat over \(A_0\). Polynomial quotient and localization commute with base change by their generator-and-inverse presentations, so \(B=A\otimes_{A_0}B_0\). Tensor associativity identifies \(B\)-tensoring of \(A\)-modules with \(B_0\)-tensoring of their underlying \(A_0\)-modules. Hence it preserves injections and is flat. This proves the assertion over every base ring. \(\square\)

### 5B.7. The full étale criterion, stability and diagonal

**EA12.** For a finitely presented \(A\)-algebra \(B\), the following conditions are equivalent:

1. \(B\) is flat over \(A\) and \(\Omega_{B/A}=0\).
2. \(B\) is formally étale.
3. \(\operatorname{Spec}B\) has a cover by square-Jacobian charts (ET11).

*Proof.* Condition 2 implies 3 by EA9. A chart satisfies 1 by EA8 and EA11. If charts cover, the tensor kernel of an injection and the differential module vanish after localization on all charts, so they vanish by EA1. Thus 3 implies 1.

Assume 1 and write \(B=P/K\) with \(K\) finite. At \(\mathfrak q\) over \(\mathfrak p\), scalar extension to \(k=\kappa(\mathfrak p)\) identifies the fibre ideal with \(K\otimes_A k\), by (ET1) applied to the flat quotient \(B\). The fibre has zero differentials and is a finite product of separable fields by EA10, and is therefore formally étale. Apply the proof of EA9 to its specified polynomial presentation. It supplies \(n\) fibre equations whose derivative vectors are the standard basis modulo the fibre ideal and which generate that ideal at the chosen point. Lift these equations to \(K\) after localizing the base at \(\mathfrak p\).

In \(P_Q\), where \(Q\) is the prime above the point, the finite quotient \(K_Q/(f_1,\ldots,f_n)_Q\) is zero modulo \(\mathfrak p\). Thus it equals \(\mathfrak p\) times itself and is zero by Nakayama. Clear the finitely many base denominators and the finite annihilator witnesses of EA1. This gives a principal neighbourhood where \(K=(f_1,\ldots,f_n)\) and the Jacobian is invertible. It is (ET11), proving 3 without assuming a Noetherian base.

To prove 3 implies 2 globally, uniqueness needs no gluing assumption: two lifts across \(J^2=0\) differ by an \(A\)-derivation \(B\to J\), with the action induced by \(B\to C/J\). The product rule follows by expanding the difference, and \(\Omega=0\) makes it zero. For existence take a finite principal chart cover, pull back its elements to \(C/J\), and lift them to \(C\). They still cover because a lifted unit equation differs from \(1\) by a nilpotent. EA8 lifts the map on each localization. Uniqueness just proved makes the local maps agree on overlaps. EA2 glues them to an \(A\)-algebra map \(B\to C\). This proves condition 2 and all equivalences. \(\square\)

We call these algebras étale. Equivalently they are finitely presented, flat and formally unramified: uniqueness of lifts is exactly \(\Omega=0\), by the difference-of-lifts calculation and the square-zero test \(B\oplus M\). No perfection or characteristic restriction is part of the definition.

**EA13.** Étale maps are stable under composition, base change and localization. Any \(A\)-map between two finitely presented étale \(A\)-algebras is étale. The diagonal of an étale morphism is an open immersion.

*Proof.* For composition, lift the intermediate algebra first, then the second algebra; uniqueness at both stages proves formal étaleness. Finite presentation composes by EA3. For base change, a map from \(B\otimes_A A'\) to an \(A'\)-algebra is exactly a \(B\)-map compatible with its specified \(A'\)-structure. The unique \(A\)-lift extends to the tensor product. Finite presentation is preserved, so EA12 applies. Localization of the source preserves unique lifting because an element invertible modulo a nilpotent ideal lifts to a unit. A principal localization has finite presentation; base localization is the already proved base-change case.

If \(B=A[X]/(f)\) and \(C=A[Y]/(g)\) are finitely presented and the images of \(X_i\) in \(C\) are \(p_i(Y)\), then
\[
 C\simeq B[Y]/(g(Y),X_i-p_i(Y)).
 \tag{ET17}
\]
The evident substitution maps are inverse; the relations \(f(p(Y))\) already belong to the ideal \((g)\). Thus the given map is finitely presented. Its unique \(A\)-lift is a \(B\)-lift, because its restriction to \(B\) agrees with the specified \(B\)-structure by the unique lifting property of \(B\). Hence it is étale by EA12.

For the diagonal put \(T=B\otimes_A B\), with multiplication \(\mu:T\to B\) and kernel \(J\). The ideal \(J\) is generated by the finitely many differences of the algebra generators. The map
\[
 b\longmapsto b\otimes1-1\otimes b
 \quad\text{gives}\quad
 J/J^2\simeq\Omega_{B/A}.
 \tag{ET18}
\]
To verify the identification, the displayed difference satisfies the derivation rules modulo \(J^2\) and generates \(J/J^2\). For a derivation \(d:B\to M\), the rule \(b\otimes c\mapsto (bc,c\,d(b))\) is an \(A\)-algebra map to the square-zero ring \(B\oplus M\). Its restriction to \(J\) kills \(J^2\) and sends the displayed difference to \(db\). These two maps are inverse on generators, proving (ET18).

Thus \(J=J^2\). At a prime \(Q\) containing \(J\), Nakayama kills the finite ideal \(J_Q\). EA1 provides \(h\notin Q\) with \(J_h=0\). On this open the quotient map identifies \(T_h\) with \(B_{\mu(h)}\). These opens cover the diagonal image, making the diagonal an isomorphism onto an open subset. The scheme assertion follows on affine charts around each diagonal point; the affine identifications agree on overlaps by their maps. \(\square\)

### 5B.8. Open images, including the arbitrary-ring step

**EA14.** Every étale morphism has open image, universally under base change.

*Proof.* We first prove the needed constructibility result over a Noetherian affine base. For an injective finite-type map of domains \(A\to B\), let \(K=\operatorname{Frac}A\). EA5 makes \(B\otimes_A K\) finite over a polynomial subalgebra \(K[z_1,\ldots,z_r]\). Clear denominators of the \(z_i\) and of the monic equations for the finitely many algebra generators of \(B\). For one nonzero \(a\in A\) this gives
\[
 A_a[z_1,\ldots,z_r]\hookrightarrow B_a
 \quad\text{a finite algebra map}.
 \tag{ET19}
\]
The left map is injective by algebraic independence over \(K\). Finite lying over in EA5 and the prime \(\mathfrak p[z_1,\ldots,z_r]\) for each base prime show that the image contains \(D(a)\).

Here is the Noetherian induction that gives constructibility for any finite-type algebra. Induct on closed subsets \(Y\) of the target, proving the assertion for all finite-type maps into each such subset. If \(Y\) is reducible, its finitely many proper irreducible components reduce the assertion to the induction hypothesis, by taking inverse images. If it is irreducible, the source has finitely many irreducible components by EA4. A component whose image closure is proper is handled on that smaller closed subset. A component dominating \(Y\) is a finite-type domain over the reduced domain of \(Y\), with an injective map; (ET19) puts a dense principal open of \(Y\) in its image. Its image on the remaining proper closed subset is the image of the finite-type base change there, so is constructible by induction. The finite union of these component images is constructible. Passing to reduced components does not change point images, and their quotient maps stay finite type. This proves the assertion, with no dimension bound.

For a flat map \(A\to B\), the image is stable under generization. At \(\mathfrak q\) over \(\mathfrak p\), the local map \(A_{\mathfrak p}\to B_{\mathfrak q}\) is faithfully flat. Indeed for a nonzero module choose a cyclic submodule \(A_{\mathfrak p}/J\); flatness preserves its injection, and its tensor quotient is nonzero because \(JB_{\mathfrak q}\) lies in the maximal ideal. For \(\mathfrak p'\subset\mathfrak p\), tensoring \(\kappa(\mathfrak p')\) therefore gives a nonzero ring. A prime of this ring gives a prime of \(B_{\mathfrak q}\) contracting to \(\mathfrak p'\), as quotienting by \(\mathfrak p'\) and inverting its complement describes that tensor ring. This is the desired generization.

A constructible generization-stable subset of a Noetherian spectrum is open. Its complement \(C\) is constructible and specialization-stable. In the closure of \(C\), each irreducible component's generic point lies in \(C\): a finite union of locally closed pieces is dense, so some piece has dense intersection with that component; its open part then contains the generic point. Specialization stability includes the entire component, so \(C\) equals its closure. This proves openness. Thus every flat finite-type map over a Noetherian base has open image. Restricting to a principal source open preserves flatness and finite type, so the map is open on every open set.

For a chart over arbitrary \(A\), use exactly the finite coefficient ring \(A_0\) and flat chart \(B_0\) of EA11. Its image is open by the Noetherian argument. The image after base change is its inverse image as a set: the fibre over \(\mathfrak p\) is the fibre over its contraction tensored with the field \(\kappa(\mathfrak p)\). A nonzero algebra over a field remains nonzero after field extension, since independent vectors remain independent; a nonzero ring has a prime. Therefore a fibre is nonempty before this extension exactly when it is nonempty afterwards. The inverse image of the open image is open.

Every étale affine chart is covered by the charts of EA12. The image of an arbitrary source open is the union of images of such smaller charts. All are open by the argument just given, and affine target covers give the scheme assertion. Base change is étale by EA13, so the same proof establishes universal openness. This is the general open-image proof; it does not assume a one-variable local form. \(\square\)

### 5B.9. Schemes, the finite-cover basis and geometric stalks

A scheme morphism is étale if it is affine-locally given by the equivalent conditions in EA12. The local condition agrees with locally finite presentation, flatness and zero relative differentials. Indeed fractions localize the differential presentation, and vanishing at every prime implies vanishing by EA1. For flatness, localize any proposed tensor kernel at source primes; local flatness over the contracted base local ring makes each localization zero, so EA1 makes the kernel zero. Finite presentation on an affine source can be patched by EA3. Thus these conditions really are local conditions on source and target.

Recall the following conventions. A morphism is quasi-compact if inverse images of affine opens are quasi-compact, and quasi-separated if its relative diagonal is quasi-compact. Finite presentation means locally finite presentation together with these two conditions. A scheme is quasi-separated precisely when intersections of affine opens are quasi-compact: pull back its diagonal on products of affine charts; its inverse image is their intersection. These are the qcqs conditions used in Section 6.

**EA15.** Over a qcqs scheme \(T\), the finite-presentation étale objects form a basis \(\mathcal B_T\) with finite limits and finite covering refinements. Base change preserves its finite limits and covers. The slice over an étale object is its étale site.

*Proof.* Quasi-compactness is stable under base change: over an affine base, cover its quasi-compact inverse image by finitely many affine charts, whose pullbacks to an affine new base are the affine tensor products of EA2. They still give a finite cover. Composition is checked by covering a quasi-compact inverse image by finitely many affine opens and using finite covers of their inverse images. The relative diagonal of a base change is the base change of the relative diagonal. The diagonal of a composite factors through the diagonal of the first morphism and a base change of the second one. These descriptions prove the same stability for quasi-separatedness. Local finite-presentation ring equations and EA3 prove its stability under base change and composition.

In particular a finite-presentation object over qcqs \(T\) has qcqs source: quasi-compactness follows by composition, and its absolute diagonal factors through its relative diagonal and a base change of the base diagonal. Identity and fibre products are therefore in \(\mathcal B_T\), by EA13 and the preceding stability. For parallel maps \(V\rightrightarrows W\), their equalizer is the inverse image of the open diagonal of \(W/T\). That diagonal is quasi-compact by finite presentation. A quasi-compact open immersion is finitely presented: over an affine target its open source is a finite union of principal opens, each given by adjoining an inverse, and EA3 gives the affine-local finite presentation; its diagonal is an isomorphism. Thus this equalizer is again in the basis. Terminal objects, products and equalizers construct all finite limits.

Every étale object has a cover by affine source charts over affine target charts with finite algebraic presentations. A smaller principal source chart suffices around any chosen point. If \(T\) is quasi-separated, an affine target open maps to \(T\) by a quasi-compact open immersion: its intersections with other affine target opens are quasi-compact. Thus these small charts really are finite-presentation objects over \(T\), using composition. Every cover of a basis object can now be refined by such charts. EA14 makes their images open; the quasi-compact source of the covered object selects finitely many images covering it. This proves finite refinement.

Maps between étale objects are themselves étale. On affine charts this is the algebra assertion in EA13. For two finite-presentation objects the map is also finitely presented globally: its graph is a base change of the quasi-compact open diagonal of the target object, and its projection is a base change of the source object's map to \(T\). Both are finitely presented. Consequently the coverings and their iterated fibre products used in Section 6 remain in the basis. Joint surjectivity is preserved by base change: a nonempty field fibre stays nonempty after residue field extension, by the vector-space argument in EA14. Finite limits commute with base change by their fibre-product and equalizer universal properties. This proves the base-change assertion.

For an étale \(U\to T\), an étale object over \(U\) composes to one over \(T\). Conversely an object étale over \(T\) with a map to \(U\) is étale over \(U\), by the maps-between-objects assertion. The arrows and jointly surjective covers are identical under these two constructions. They give the slice equivalence; for finite-presentation objects its finite-presentation assertions follow from the graph argument above.

For completeness, the sites can be presented by small categories. Affine finite presentations over the affine target charts have a set of coefficient lists and maps. For qcqs \(T\), finite affine covers, finite principal overlap covers and their gluing equations encode all basis objects by a set of finite data. In general start with \(T\) and that set of affine étale charts, and close under finite limits; these are still a set of objects. They cover every étale object. Their matching families determine sheaves on the whole site: refine two covers by fibre products, identify their matching families by the sheaf equalizer, and glue on a composite cover. The same argument extends a sheaf from the small presentation and restricts it back, giving inverse constructions. When comparing a set of scheme maps, include the set of their base-change objects and again close under finite limits. This leaves the matching-family sheaves unchanged and makes the base-change functors the finite-limit, cover-preserving functors of SH6. Thus the inverse-image and slice arguments apply without an assumption about the size of a class of schemes. \(\square\)

**EA16.** Geometric points give conservative point functors on the étale site. Their stalks, and exactness tested on those stalks, are the stalks of SH7.

*Proof.* Choose for every point \(x\) an algebraic closure \(\Omega_x\) of \(\kappa(x)\) and its map \(\bar x:\operatorname{Spec}\Omega_x\to T\). On an object \(V\), set
\[
 \tau_{\bar x}(V)=
       \operatorname{Hom}_T(\operatorname{Spec}\Omega_x,V).
 \tag{ET20}
\]
It preserves finite limits by their universal property. It lifts coverings: pull a covering back along the chosen lift to \(\operatorname{Spec}\Omega_x\). It remains jointly surjective by EA15. Every nonempty étale chart over this algebraically closed field has an \(\Omega_x\)-point, since its field algebra is a product of copies of \(\Omega_x\) by EA10. One such point gives the required covering lift. Hence this is a point functor in the precise sense of SH7.

We prove conservativity, not just the point axioms. Every ordinary point \(v\) of an étale \(V\) over \(x\) admits a lift from \(\Omega_x\): on its affine field-fibre chart, EA10 makes \(\kappa(v)/\kappa(x)\) finite separable, so it embeds in \(\Omega_x\). Suppose a section of a sheaf is zero in every geometric stalk over its object \(V\). For each \(v\), choose such a lift. The filtered representative test of SH7 gives a refinement \(W\to V\) carrying that lift on which the section is zero. The images of these refinements cover \(V\), because each contains its corresponding \(v\); the sheaf condition gives zero on \(V\). Applied to kernel sections, this proves injectivity of a map that is injective on all geometric stalks.

If a map \(F\to G\) is stalkwise surjective, take \(s\in G(V)\) and the same lifts at all \(v\). Stalk surjectivity gives a representative preimage on a neighbourhood; common refinement with \(V\), followed by a refinement witnessing equality, gives a local preimage of \(s\) on \(W\to V\) through that lift. Again these maps cover \(V\). Thus the map is an epimorphism by (SC2). Stalkwise bijectivity is therefore an isomorphism. This proves conservativity, and SH7 now proves the exact-complex stalk criterion. \(\square\)

The geometric inverse-image stalk formula is also an actual consequence of these constructions. For a scheme map \(p:T'\to T\) and a geometric \(\bar t'\), let \(\bar t\) be its composite into \(T\), using the same algebraically closed field. Then
\[
 (p^{-1}F)_{\bar t'}\simeq F_{\bar t}.
 \tag{ET21}
\]
The point-functor argument above applies to that field even if it is not algebraic over \(\kappa(t)\). To prove the formula, the free sheaf \(P_V\) of (SC3) has stalk \(\mathbb Z[\tau_{\bar t}(V)]\). Indeed a germ of an arrow into \(V\) maps to its chosen lift; every lift is represented by the identity of \(V\), and two representations with equal lifts agree on their fibre-product refinement over \(V\). Free abelian groups commute with these colimits by their finite-generator presentation, and SH7 removes sheafification. The adjunction SH6 and (SC3) identify \(p^{-1}P_V\) with the free sheaf on \(V\times_TT'\): they represent the same maps to any sheaf. Its lifts are exactly the lifts of \(V\) after composing \(\bar t'\) with \(p\). Thus (ET21) holds on these free sheaves and their sums. Every sheaf has a presentation by two such sums: use all its sections for a surjection and then all sections of its kernel. Both stalk functors and inverse image are exact and commute with colimits by SH2, SH6 and SH7, so taking the cokernel proves (ET21) for the sheaf. The construction on arrows makes it natural.


**EA17.** Pointed affine étale neighbourhoods are cofinal for a geometric stalk, and their opposite category is filtered without a poset assumption.

*Proof.* A chosen lift lies in an affine source chart mapping into an affine target chart. Shrink to a finite-presentation principal chart there; its chosen lift still factors through it. Thus affine neighbourhoods suffice. Fibre products give common neighbourhoods, followed by the same affine shrinking. For two parallel neighbourhood arrows, their equalizer is the inverse image of the open diagonal from EA13. It contains the chosen lift. An affine neighbourhood inside that open equalizes the arrows. These are exactly the common-refinement and equalization axioms. Ring maps go in the reverse direction, giving the filtered colimit. Restricting to a fixed affine target neighbourhood is cofinal by intersecting with its inverse image. \(\square\)

### 5B.10. The actual strict local neighbourhood ring

**EA18.** Fix \(T=\operatorname{Spec}A\), a prime \(\mathfrak p\), and an algebraic closure \(\Omega\) of its residue field \(k\). Let \(R\) be the ring colimit of its pointed affine étale neighbourhoods. Then \(R\) is faithfully flat over \(A_{\mathfrak p}\) and local, with residue the separable closure \(k^{\mathrm{sep}}\) inside \(\Omega\). Every finite-presentation étale \(R\)-algebra with a prescribed residue point has a unique \(R\)-section lifting it. The ring is strictly Henselian and is the local-neighbourhood construction \(A_{\mathfrak p}^{\mathrm{sh}}\) with that chosen residue closure.

*Proof.* The index is filtered by EA17. Every stage has its chosen map into \(\Omega\), and the maps induce \(\rho:R\to\Omega\). Its image is contained in \(k^{\mathrm{sep}}\): every stage value lies in the finite separable residue field of its fibre point, by EA10. All fractions from \(A\setminus\mathfrak p\) occur by principal target neighbourhoods, so the image contains \(k\). It contains every finite separable extension in \(\Omega\) as well. Choose its primitive element and separable monic polynomial over \(k\), lift the finitely many coefficients to \(A_a\), \(a\notin\mathfrak p\), and take the chart obtained by quotienting by that polynomial and inverting its derivative. The chosen root gives a pointed neighbourhood whose residue contains the element. Hence the image is exactly \(k^{\mathrm{sep}}\).

If a stage element has nonzero value under \(\rho\), its principal source localization is another pointed étale neighbourhood. It is therefore invertible in \(R\). If its value is zero, it belongs to the chosen prime of the stage. Localizing at that prime and applying (ET14) puts its image in \(\mathfrak pR\), because all those local denominators are already units in \(R\). Hence the maximal ideal equals \(\mathfrak pR\). Thus
\[
 \mathfrak m_R=\mathfrak pR=\ker\rho,\qquad R/\mathfrak m_R=k^{\mathrm{sep}}.
 \tag{ET22}
\]
The residue field is separably closed. To verify this, a separable polynomial and its coprimality witness with its derivative use only finitely many coefficients in \(k^{\mathrm{sep}}\), hence belong to a finite separable extension of \(k\). Its roots are separable over that finite field and therefore over \(k\). The latter transitivity follows from EA10: after tensoring with an algebraic closure, a finite separable extension splits into copies of that closure, and a further separable extension does so in each factor; the resulting reduced tensor algebra excludes an inseparable element by the test in EA10. All the roots thus belong to \(k^{\mathrm{sep}}\).

Each pointed affine stage is flat over \(A\) by EA12. EA1 makes their filtered colimit flat as well. All elements of \(A\setminus\mathfrak p\) are units in \(R\), so it is flat over \(A_{\mathfrak p}\). This map is local by (ET22), and the flat local faithfulness proof in EA14 makes it faithfully flat.


Consider an étale \(R\)-algebra with its chosen residue point. Choose a square-Jacobian chart around that point by EA12. Its coefficients, and elements representing the finitely many residue coordinate values, come from one pointed stage \(B\) by filteredness. Use the identical Jacobian equations over \(B\), with the indicated values in \(\Omega\). They define another pointed étale \(A\)-neighbourhood, by EA13. Its coordinate images in \(R\) solve the equations exactly and give an \(R\)-section of the chart, hence of the original algebra. This proves existence with the prescribed residue.

Two sections with the same residue point coincide. Pull back the open diagonal of that étale algebra along the pair of sections. The resulting open of \(\operatorname{Spec}R\) contains its closed point. Any open containing the closed point of a local spectrum is the whole spectrum: one of its principal neighbourhoods has an element outside the maximal ideal, hence a unit. Thus the two sections agree everywhere. This proves uniqueness without assuming that \(R\) is Noetherian or complete.

Here is also the usual factor-lifting test for Henselianity, proved directly. For a monic polynomial whose residue factors as two coprime monic polynomials \(g,h\) of degrees \(r,s\), write equations for the \(r+s\) coefficients of the two monic lifts. Their Jacobian at the residue factorization is the linear map
\[
 (u,v)\longmapsto uh+gv,\qquad
 k^{\mathrm{sep}}[T]_{<r}\oplus k^{\mathrm{sep}}[T]_{<s}
 \longrightarrow k^{\mathrm{sep}}[T]_{<r+s}.
 \tag{ET23}
\]
Its kernel is zero: coprimality makes \(g\) divide \(u\), so the degree bound gives \(u=0\), then \(v=0\). The spaces have the same finite dimension, so the determinant is nonzero. The square-Jacobian chart and the section property just proved give the unique lifted factors. This is the monic coprime-factor definition of a Henselian local ring; together with (ET22) it proves strict Henselianity.

The local-neighbourhood construction can use stage local rings \(B_{\mathfrak q}\) instead of the affine rings \(B\). Every denominator outside the chosen \(\mathfrak q\) becomes a unit by a principal pointed refinement. The maps from these local rings to \(R\) and from the affine colimit to their colimit are consequently inverse. They also allow the base to be replaced by \(A_{\mathfrak p}\): refine a pointed presentation over it to a square-Jacobian chart by EA12; its finitely many coefficients and denominators come from an \(A_a\), \(a\notin\mathfrak p\), while their chosen residue maps are unchanged. This proves the asserted construction of \(A_{\mathfrak p}^{\mathrm{sh}}\) rather than assuming its identification with the neighbourhood colimit.

Equivalently the affine index consists of triples \((B,\mathfrak q,\iota)\), where \(B\) is étale over \(A\), \(\mathfrak q\) lies over \(\mathfrak p\), and \(\iota:\kappa(\mathfrak q)\hookrightarrow k^{\mathrm{sep}}\) extends the residue embedding. A map from \(B\) to \(\Omega\) determines its kernel and that field embedding; the finite separable field-fibre result makes its image lie in \(k^{\mathrm{sep}}\). Conversely each such triple gives exactly that chosen geometric lift. Arrows preserve the lift exactly when they preserve this residue embedding. Thus the colimit is the strict-henselization construction by pointed étale local algebras with the specified residue closure, with all its local, flat and lifting assertions proved above.



One useful universal property is explicit in the proof. If a local \(A\)-algebra \(S\) is equipped with the chosen residue embedding and has the same étale residue-section property, every pointed stage has a unique compatible map into \(S\). Their colimit gives the unique local map \(R\to S\) with those residue maps. No universal property for rings lacking that stated lifting hypothesis is being imported. \(\square\)

The freely accessible primary reading is the Stacks project authors' [Noetherian completion](https://stacks.math.columbia.edu/tag/0BNH), [formal étaleness](https://stacks.math.columbia.edu/tag/00UP), [normalization](https://stacks.math.columbia.edu/tag/00OX), [étale morphisms](https://stacks.math.columbia.edu/tag/03PA), [geometric stalks](https://stacks.math.columbia.edu/tag/03PN), and [strict local construction](https://stacks.math.columbia.edu/tag/0BSK). EA1–EA18 supply the arguments actually used by this lesson. In particular, (ET16) is proved before flatness, EA11 gives the arbitrary-base step, and EA15–EA17 prove the point and finite-cover hypotheses rather than treating those hypotheses as citations. These are foundations for continuity. Section 6A now proves nilpotent-site invariance, finite pushforward, closed support and the integral universal-homeomorphism comparison. The later curve Kummer, Brauer and duality computations remain separate proofs.

### 5B.11. Graded exercise: the algebra behind a geometric stalk

**Exercise 5B.1 (100 points).** Each part is worth 10 points. Use the constructions of EA1–EA18, proving the stated calculations rather than inferring étaleness from a missing hypothesis.

1. Let \(A=k[t]\), \(I=(t)\), and \(N=t^rA\subset A\), \(r\geq1\). Determine a sharp Artin–Rees bound, identify the completion, and explain the difference between its flatness over \(A\) and faithful flatness over \(A_{(t)}\).
2. Apply (ET5) to \(k[X,T]/(X^2+T^3)\), with \(Y=X-T^4\). Exhibit its finite free module over \(k[Y]\), in every characteristic.
3. Starting from a section \(B=P/K\to P/K^2\), prove the splitting of (ET10). With zero differentials, explain exactly where finite generation and Nakayama produce a square-Jacobian chart.
4. Let \(A=k[t]\) and \(B=A/(t)\). Compute the relative differential module, disprove flatness, and construct a square-zero lifting diagram with no lift.
5. Let \(f=T^2+T+1\), \(\delta=2T+1\), and \(B=(\mathbb Z[T]/(f))_\delta\). Compute the multiplication matrix of \(\delta\), the image in \(\operatorname{Spec}\mathbb Z\), the fibres at \(2,3,7\), and the completion at its point over \(2\).
6. For \(F_1=X^2+Y-a\), \(F_2=Y^2+X-b\), compute a square-zero Newton correction from errors \(e_1,e_2\). State the required inverted element and show why the proof works without dividing by \(2\).
7. For \(k=\mathbb F_p(s)\) and \(K=k[u]/(u^p-s)\), prove that \(K\) is a field, compute \(\Omega_{K/k}\), and give two distinct lifts across a square-zero ideal. Explain why flatness of this extension does not make it étale.
8. Prove covering lift and conservativity for the geometric point functor. Then prove the inverse-image stalk formula using free sheaves and their presentations.
9. Verify the idempotent correction (ET13) in characteristic \(2\). For the residue factors \(g=T^2+aT+b\), \(h=T+c\), compute the coefficient Jacobian determinant in (ET23) and interpret its nonvanishing.
10. Let \(E=\bigcup_{n\geq1}\mathbb F_{p^{n!}}\) inside an algebraic closure. Prove that \(E/\mathbb F_p\) is formally étale and flat but is not finitely presented. Explain what the new foundations still leave to prove in the later curve-cohomology calculation.

*Full solution.*

1. Direct divisibility gives
\[
 N\cap I^nA=t^{\max(r,n)}A.
 \tag{ETX1}
\]
For \(n\geq r\), this is \(t^{n-r}(N\cap I^rA)=t^nA\). Thus \(c=r\) works. If \(c<r\), take \(n=r\): the right side of (ET6) would be \(t^{2r-c}A\), strictly smaller than \(t^rA\). This proves sharpness. A compatible sequence of polynomials modulo \(t^n\) determines, and is determined by, its successive coefficients, so the completion is \(k[[t]]\). EA7 makes it flat over \(A\). It is not faithfully flat over this nonlocal \(A\): the nonzero module \(A/(t-1)\) is killed after tensoring, since \(1-t\) is invertible by its geometric series in \(k[[t]]\). For \(A_{(t)}\), the completion has the same quotients and is faithfully flat by the local assertion EA7. The distinction is the local, proper-maximal-ideal hypothesis, not a failure of completion exactness on finite modules.

2. The substitution gives
\[
 T^8+2YT^4+T^3+Y^2=0.
 \tag{ETX2}
\]
The substitution and its inverse \(X=Y+T^4\) identify the algebra with the quotient of \(k[Y,T]\) by this monic degree-eight polynomial. Monic division gives a unique remainder of degree less than eight, so the basis is
\[
 1,T,T^2,\ldots,T^7.
 \tag{ETX3}
\]
Uniqueness follows because multiplication of a nonzero polynomial by a monic degree-eight polynomial has its leading nonzero coefficient in degree at least eight. In characteristic \(2\) the middle coefficient in (ETX2) disappears, but the degree-eight monic coefficient and the proof are unchanged. No separability or domain assertion is needed for this module calculation.

3. Define \(d(p)=p-s(\bar p)\) in \(K/K^2\). Expanding a product and using the square-zero ideal proves that this is a derivation, with \(d(f)=f\bmod K^2\) for \(f\in K\). The free polynomial differential module gives \(\beta:B^n\to K/K^2\), with \(\beta\alpha=1\). If \(\Omega=0\), \(\alpha\) is also surjective by (ET10), hence is an isomorphism. Choose actual equations mapping to its basis. They generate \(K/K^2\); the finite quotient by them therefore equals \(K\) times itself at a prime containing \(K\). Nakayama makes that local quotient zero. The finitely many ideal generators then give one denominator witnessing zero on a principal open, by EA1. Its Jacobian determinant is \(1\) modulo \(K\) and can also be inverted. This is the exact local chart step; neither a basis for the original ideal nor a Noetherian base was assumed.

4. Every element of \(B\) comes from \(A\), so all its relative differential generators are zero:
\[
 \Omega_{B/A}=0.
 \tag{ETX4}
\]
Multiplication by \(t\) is injective on \(A\) but becomes the zero map on the nonzero module \(B\), disproving flatness. Take \(C=A/(t^2)\), \(J=(t)/(t^2)\). Then \(J^2=0\) and \(C/J=B\). The identity map to \(C/J\) cannot lift as an \(A\)-map \(B\to C\): the element \(t\) is zero in the source but its specified base image in \(C\) is nonzero. Thus the lifting existence and flatness hypotheses are both essential; finite presentation and zero differentials alone do not suffice.

5. On the basis \(1,T\), use \(T^2=-T-1\). The matrix is
\[
 M_\delta=
 \begin{pmatrix}1&-2\\2&-1\end{pmatrix},
 \qquad M_\delta^2=-3\,1,\qquad
 \det(Z\,1-M_\delta)=Z^2+3.
 \tag{ETX5}
\]
Thus \(\delta^2=-3\) in the algebra, and inverting \(\delta\) is exactly inverting \(3\). One implication follows from this square identity; for the other, \(\delta^{-1}=-\delta/3\). The algebra is finite free of rank two over \(\mathbb Z[1/3]\), so its fibre over every prime there is nonzero. Its image is \(D(3)\).

At \(2\), \(f\) has no root in \(\mathbb F_2\) and is irreducible of degree two; its derivative is \(1\), so the fibre is \(\mathbb F_4\). At \(3\), \(f=(T-1)^2\) and \(\delta=2(T-1)\) is nilpotent; its localization is the zero ring, so the fibre is empty. At \(7\), the distinct roots are \(2,4\), with nonzero derivatives; remaindering gives \(\mathbb F_7\times\mathbb F_7\). At the unique point over \(2\), (ET16) identifies the completed local ring with
\[
 \mathbb Z_2[T]/(T^2+T+1),
 \quad\text{free of rank two over }\mathbb Z_2.
 \tag{ETX6}
\]
Here \(\mathbb Z_2=\varprojlim\mathbb Z/2^n\): odd denominators in \(\mathbb Z_{(2)}\) are already units modulo every \(2^n\), so this is the completion in (ET15). This describes a local completion, not finiteness over the original \(\mathbb Z\).

6. At a tuple \((x,y)\), put \(\Delta=4xy-1\). The Jacobian and correction are
\[
 J_F=
 \begin{pmatrix}2x&1\\1&2y\end{pmatrix},\qquad
 d_x=\frac{e_2-2ye_1}{\Delta},\qquad
 d_y=\frac{e_1-2xe_2}{\Delta}.
 \tag{ETX7}
\]
The linear corrections are \(-e_1,-e_2\). The new errors are consequently \(d_x^2,d_y^2\), which vanish when the errors belong to a square-zero ideal. Inverting \(\Delta\) is the required chart condition; no inversion of \(2\) occurs. In characteristic \(2\), \(\Delta=-1\) and the same formulas solve the system. For a general nilpotent ideal repeat this lift through its successive square-zero quotients, as in EA8.

7. The element \(s\) is not a \(p\)-th power in \(\mathbb F_p(s)\). The order at \(s=0\) of a \(p\)-th power of a rational function is divisible by \(p\), while that of \(s\) is \(1\); the order is defined by counting powers of \(s\) in numerator and denominator. In an algebraic closure \(T^p-s=(T-\alpha)^p\). A proper monic factor of degree \(0<r<p\) would be \((T-\alpha)^r\); its next coefficient \(-r\alpha\) would put \(\alpha\) in \(k\), a contradiction. Hence the polynomial is irreducible and \(K\) is a field. Its relative derivative is zero, so (ET10) gives
\[
 \Omega_{K/k}=K\,du.
 \tag{ETX8}
\]
In \(K[\epsilon]/(\epsilon^2)\), both \(u\mapsto u\) and \(u\mapsto u+\epsilon\) are \(k\)-maps lifting the identity, since \((u+\epsilon)^p=u^p\). They are distinct. The extension is flat because vector spaces have bases and tensoring with a field extension preserves injections, but the nonzero differential module and lifting nonuniqueness exclude étaleness.

8. Finite limits are preserved by maps from \(\operatorname{Spec}\Omega\), by their universal property. Pull a cover back to this algebraically closed field. Joint surjectivity survives field extension, and a nonempty étale chart has a point with that same field by EA10. Thus the chosen lift reaches a covering member. If all germs of a section vanish, for each ordinary point choose its residue embedding into the fixed closure. A refinement through that lift witnesses vanishing, by SH7. These refinements cover the object, so the section is zero. For a target section under a stalkwise surjection, represent its preimage germ and refine until the image equality holds; the same covering argument gives local preimages. This proves injectivity, epimorphy and hence conservativity.

For inverse image, a free sheaf on \(V\) has stalk the free group on the geometric lifts of \(V\): existence is the identity representative, and equality is witnessed by the fibre product over \(V\). The adjunction identifies its inverse image with the free sheaf on \(V\times_TT'\). These lifts are the same after composing the chosen point with \(p\). A two-term presentation by sums of free sheaves exists by (SC3). Exactness and preservation of those sums give (ET21) for its cokernel, naturally. This does not infer a higher-cohomology limit theorem merely from a stalk definition.

9. In characteristic \(2\), \(2u-1=1\), so (ET13) is \(e=u+(u^2-u)=u^2\). The square-zero condition on \(\delta=u^2-u\) gives \(u^4-u^2=0\), proving \(e^2=e\). Its difference from \(u\) is in the nil ideal. If another lift differs by \(a\) in that ideal, its idempotent equation gives \((2e-1)a=a=0\), proving uniqueness.

Write the coefficient variations of \(g,h\) as \(u=u_0+u_1T\), \(v=v_0\). The coefficients of \(uh+gv\) give
\[
 \begin{pmatrix}
 c&0&b\\
 1&c&a\\
 0&1&1
 \end{pmatrix},
 \qquad
 \det=c^2-ac+b=g(-c).
 \tag{ETX9}
\]
This is nonzero exactly when the linear factor \(h\) does not divide \(g\), hence when they are coprime. Over the strict local residue field, its invertibility defines the Jacobian chart for lifting the factors. EA18 gives its unique section. The calculation works in every characteristic.

10. The finite fields are nested because \(n!\) divides \((n+1)!\): iterating the corresponding Frobenius identity puts each smaller field inside the next. Lemma 0F.1 supplies their sizes and degrees. Each is separable, since its elements are roots of \(T^{p^{n!}}-T\), whose derivative is \(-1\), and is étale by the primitive-element chart of EA10. Across a square-zero ideal, lift the map on every finite stage. Uniqueness makes these lifts compatible, so they define one unique lift on the union. This proves formal étaleness. It is also flat as a field extension, or as a filtered colimit of flat modules by EA1.

Any finite list of elements of \(E\) belongs to one finite stage; the algebra it generates remains in that finite field. Since the stage degrees \(n!\) are unbounded, the whole union cannot be finitely generated, and hence cannot be finitely presented. Thus formal étaleness need not itself be étaleness without the finite-presentation hypothesis. The new foundations prove the geometric site and continuity inputs in Lesson 1. The nilpotent-site, closed-support and finite-pushforward arguments are now supplied in NP1–NP12 in Section 6A. The later curve Kummer/degree and higher-vanishing calculations still require their own complete programme proofs; a citation or this field example cannot replace them. \(\square\)

## 6. A higher-cohomological continuity foundation

Later lessons use étale cohomology in the elliptic Euler-characteristic and curve trace calculations. SH1–SH9 supply the abstract sheaf foundations, and EA1–EA18 supply their algebraic and geometric étale inputs over arbitrary base rings. Sections6.2–6.6 now prove higher continuity at its full abelian coefficient scope;Sections6.7–6.8 derive filtered-coefficient,strict-local and pro-étale applications. The proof uses the actual square-Jacobian local presentations and open-image theorem established in this lesson.

### 6.1. Scope and actual earlier interfaces

Let \(I\) be a small filtered category. Our notation for an arrow \(a:i\to j\) includes the affine scheme map \(f_a:X_j\to X_i\). The \(X_i\) are quasi-compact and quasi-separated, and \(X=\varprojlim_i X_i\), with projection \(p_i:X\to X_i\). A coefficient system consists of abelian etale sheaves \(F_i\) and maps
\[
 \alpha_a:f_a^{-1}F_i\longrightarrow F_j
 \tag{HC1}
\]
compatible with identities and composition. Set
\[
 L(F_i)=\varinjlim_i p_i^{-1}F_i.
 \tag{HC2}
\]
Associativity of fibre products and inverse image is always interpreted through its canonical identifications. The compatibility in (HC1) includes those identifications; it does not assume that pullback functors are literally equal under composition.

The actual abstract proof bindings in this lesson are SH1–SH2 for exact sheafification and filtered colimits,SH3–SH4 for injective resolutions and local vanishing,SH5 for exact slice restriction preserving injectives,SH6 for the exact inverse-image adjunction and higher-image cohomology presheaf,SH7 for the stalk of a point functor,and SH8–SH9 for the full covering contraction and finite-diagonal comparison. Section6.5 gives the remaining simultaneous vanishing induction. None of these proofs depends on a separately named diagnostic lesson. EA15–EA17 now prove the finite-cover basis,slice equivalence and conservative geometric stalks;EA18 constructs and identifies the strict local neighbourhood ring.

The actual geometric proof bindings are EA1–EA3 for localization,affine gluing,finite witnesses and finite-presentation patching;EA4–EA7 for the Noetherian algebra,normalization and exact faithful local completion used in the flatness proof;EA8–EA12 for square-Jacobian lifting,finite separable field fibres and the full arbitrary-base étale criterion;EA13 for stability,maps between étale objects and the open diagonal;EA14 for universal open images;EA15 for finite limits,finite covering refinements,base-change functors and the slice equivalence;EA16–EA17 for conservative geometric points,exact stalks and affine pointed refinements;and EA18 for the actual strict local construction. Section6.2 supplies the finite-data scheme-limit and covering descent proof using these square-Jacobian charts. None of these inputs is discharged by a diagnostic lesson or a source citation.

### 6.2. Finite etale data on an affine-transition limit

EA15 supplies the following basis and covering facts. Use the basis \(\mathcal B_T\) of etale morphisms of finite presentation \(V\to T\) for a qcqs scheme \(T\). Their sources are qcqs. The identity is in this basis; finite fibre products stay in it. Every etale object has a cover by members of this basis: take affine source charts over affine target charts and their finitely presented local etale equations. Covers of a basis object have a finite refinement by basis objects. Indeed etale maps have open images, as proved below, and the target is quasi-compact. Choosing finitely many small affine charts whose images cover produces the refinement. Thus sheaves on this basis, with these finite coverings, determine sheaves on the whole small etale site. Explicitly their sections on another object are matching families on a basis cover; refining two covers and using the sheaf equalizer identifies these families independently of the chosen cover.

**Lemma 6.2.** Each \(V\in\mathcal B_X\) is the base change of some \(V_i\in\mathcal B_{X_i}\). Morphisms between such objects, equality of morphisms, and every finite covering descend to a sufficiently late stage. In particular every finite covering and its finite iterated fibre products can be used at one common stage.

*Proof.* We spell out the finite-data assertions, including the covering assertion. Choose one index \(i_0\) and a finite affine open cover of \(X_{i_0}\). Pullbacks of these opens to every later stage and to the limit are affine, because all transition maps are affine. On such a chart their rings satisfy
\[
 A=\varinjlim_j A_j.
 \tag{HC3}
\]
This constructs the limit scheme by gluing the affine limits. To check the gluing, cover each overlap of base charts by finitely many principal opens, using quasi-separatedness. Ring localization commutes with (HC3): a fraction has a stage numerator and denominator, and an equality of fractions is a finite ring equation at a later stage. Hence on these principal opens the affine limits have the identical restriction rings and canonical overlap identifications. Their cocycle identities are inherited from the stage identities; ordinary scheme gluing then constructs \(X\). A compatible family of maps into the \(X_j\) gives a map into each of these affine limits by the universal property of ring colimits, and these maps glue uniquely. This verifies the inverse-limit universal property. Its projection to \(X_{i_0}\) is affine. It is quasi-compact; its diagonal is quasi-compact because its relative diagonal over \(X_{i_0}\) is affine and the base diagonal is quasi-compact. Thus the limit is qcqs. For a general filtered category use its coslice \(i_0/I\); that category is filtered and its forgetful functor is cofinal. Indeed any other index has a common receiving index with \(i_0\), and any two such choices and their finitely many parallel composites can be equalized at a further receiving index. These same common-stage operations both prove cofinality and realize all finite equations used below.

For affine algebras, a finite presentation \(A[Z_1,\ldots,Z_s]/(r_1,\ldots,r_t)\) descends by choosing representatives of its finitely many coefficients. A map between two finitely presented algebras descends by choosing the images of finitely many generators. Its finitely many defining relations hold at some common later stage. Equality of two such maps is likewise witnessed by finitely many equalities on generators. This proves the affine object, map and equality assertions.

We will also need the same assertion for quasi-compact opens. In an affine scheme such an open is a finite union \(\bigcup D(g_b)\). Its defining elements descend. The inclusion
\[
 D(g)\subset\bigcup_bD(h_b)
 \quad\Longleftrightarrow\quad
 g^N=\sum_b c_bh_b\text{ for some }N,c_b
 \tag{HC4}
\]
is a finite ring identity. To justify the equivalence, the inclusion says that every prime containing the \(h_b\) contains \(g\). If \(g\) were outside their radical, a maximal ideal disjoint from its powers in the quotient ring, obtained by Zorn, would give a contrary prime. Radical membership is exactly the power identity. Thus inclusions and equality of finite-union opens hold at some later stage whenever they hold on the limit. A finite affine cover gives the identical conclusion on any qcqs scheme already descended. Intersections of its affine opens are quasi-compact by quasi-separatedness, so only finitely many principal charts and identities are needed.

An object \(V\to X\) of the stated basis has a finite affine cover whose members map into the pulled-back base charts. Each algebra is finitely presented. Refine further by finitely many principal square-Jacobian charts from EA12. Their polynomial equations and inverted products of the principal element with the Jacobian determinant are finite coefficient data. At a common stage use the identical presentations. EA8 and EA11 prove their unique lifting and flatness over that stage ring,so EA12 makes them étale. This gives the actual chart descent over arbitrary rings.

For clarity, the gluing of these charts also descends. A pairwise overlap is a quasi-compact open in each source chart and hence a finite union of principal opens. Descend those principal elements first. On finitely many principal refinements, the overlap identifications are maps between finite-presentation algebras; descend their finitely many generator images and relations. Their inverse identities descend by the affine equality assertion. The equality of the domains on each triple overlap is an equality of quasi-compact opens, governed by (HC4), and the cocycle identities are finitely many equalities of maps on principal charts. Choose one later stage where all of these identities hold. Glue the affine charts there along these open isomorphisms. The quotient of their disjoint union by the open identifications has the stated chart topology, and the structure sheaves glue by the cocycle identity. This constructs a scheme and its map to \(X_i\); its base change is \(V\). The map is etale on the charts. It is quasi-compact and quasi-separated because the chart list and all overlaps are finite and quasi-compact, and consequently it is of finite presentation. This proves object descent.

Maps between two descended objects have the same finite description. Preimages of a finite affine target cover are quasi-compact opens of the source. One useful verification of this claim is that any map from a quasi-compact scheme to a quasi-separated scheme is quasi-compact: its graph is a base change of the quasi-compact target diagonal, and projection from the product is quasi-compact. Descend these preimage opens by (HC4), choose finite principal source refinements mapping into the target charts, and descend the corresponding algebra maps. Their agreement on overlaps, and equality of two entire maps, are finite identities on these refinements. Thus map descent and eventual equality are proved without a separate scheme-limit theorem.

Here is also an elementary open-image calculation. On a standard etale chart write \(B=(A[T]/(f))_g\), with \(f\) monic of degree \(d\), and absorb \(f'\) into the inverted element if necessary. Put \(B_0=A[T]/(f)\), a free \(A\)-module of rank \(d\). A prime \(\mathfrak p\) is in the image of \(\operatorname{Spec}(B_0)_g\) exactly when \(g\) is not nilpotent in \(B_0\otimes_A\kappa(\mathfrak p)\). Multiplication by \(g\) on this finite-dimensional algebra is nilpotent exactly when its characteristic polynomial is \(T^d\). For the forward implication, choose a basis adapted to the filtration by the kernels of its powers; the matrix is strictly triangular. For the reverse implication the adjugate polynomial identity \((TI-M)\operatorname{adj}(TI-M)=\det(TI-M)I\) gives the characteristic-polynomial identity at \(M\): expand in powers of \(T\), compare coefficients and multiply successively by powers of \(M\); the adjacent terms telescope. Thus \(M^d=0\). The image is consequently a finite union of principal opens given by the nonleading characteristic-polynomial coefficients. For general square-Jacobian charts,EA14 proves open images;their unions give general étale images,and a quasi-compact source gives a quasi-compact image. The monic calculation above is an explicit special case. Images of scheme morphisms commute setwise with field base change here: a nonempty fibre remains nonempty after extending its residue field, since a nonzero vector in its nonzero coordinate algebra stays nonzero under field scalar extension.

Now descend a finite covering \(W_b\to V\) and its maps to one stage. The maps there are etale, by the actual algebra and graph proofs EA13 and EA15. Their images have union a quasi-compact open \(O_i\subset V_i\), and its inverse image on the limit is all of \(V\). On finitely many affine charts its closed complement is \(V(h_1,\ldots,h_m)\). Emptiness after (HC3) gives an identity \(1=\sum c_ah_a\) in the limit ring. That finite identity holds at a later stage. Taking a common stage for the finite chart list makes the complement empty, so the family is a covering there. Fibre products are formed by the same finite presentations and commute with base change. This proves every assertion. \(\square\)

### 6.3. The degree-zero comparison for a general coefficient system

**Lemma 6.3.** If \(V=V_i\times_{X_i}X\) is a basis object, then
\[
 \Gamma(V,L(F_i))
 =\varinjlim_{(a:i\to j)}\Gamma(V_j,F_j),
 \qquad V_j=V_i\times_{X_i}X_j.
 \tag{HC5}
\]
In particular, filtered sheaf colimits on a fixed qcqs scheme commute with sections on every basis object. The assertion also holds for sheaves of sets.

*Proof.* Define the right-hand side as a presheaf \(H\) on the limit basis. Lemma 6.2 makes it independent of a chosen descended presentation: any two presentations and their isomorphism agree at a common later stage. It also defines restriction maps, because the relevant morphisms descend and their equalities become equalities later.

This presheaf is a sheaf. Descend a finite covering of \(V\) to a covering of \(V_j\). Every finite iterated intersection descends with it. The degree-zero sheaf equalizer at each stage is
\[
 F_j(V_j)\longrightarrow\prod_bF_j(W_{b,j})
 \rightrightarrows\prod_{b,c}F_j(W_{b,j}\times_{V_j}W_{c,j}).
 \tag{HC6}
\]
Filtered colimits commute with these finite products and equalizers: finitely many representatives have a common target, and finitely many equality relations hold together at a further target. Taking the colimit of (HC6) proves exactly the sheaf equalizer for \(H\). Finite coverings generate the basis topology by 6.2.

Finally \(H=L(F_i)\), as an actual sheaf, by its universal property. For any sheaf \(G\) on \(X\), compatible maps \(p_i^{-1}F_i\to G\) are equivalently compatible maps \(F_i\to p_{i,*}G\). Their section maps on descended basis objects give a unique map from the right side of (HC5) to \(G(V)\). Conversely a map \(H\to G\) supplies those section maps by the stage-to-colimit arrows. Objects and arrows descend, so the two constructions are inverse. This identifies the universal sheaf colimit and proves (HC5). The same argument uses finite limits of sets without addition. \(\square\)

### 6.4. Compatible resolutions with injective components

Let \(\mathcal A\) be the category of systems (HC1). It is abelian with kernels and cokernels at each index: inverse image is exact, so the induced structure maps on those kernels and cokernels are compatible. Evaluation at an index is exact.

**Lemma 6.4.** Every system embeds in an injective object of \(\mathcal A\) whose components are injective sheaves. It therefore has a resolution in \(\mathcal A\) with injective components at every degree.

*Proof.* For an index \(i\), evaluation has a right adjoint \(R_i\). On a sheaf \(M\) at \(X_i\), its component at \(j\) is
\[
 (R_iM)_j=\prod_{a:j\to i}f_{a,*}M.
 \tag{HC7}
\]
An empty product is the zero abelian sheaf. For \(b:j\to k\), the projection indexed by \(a\circ b:j\to i\), followed by the counit, gives the component of
\(f_b^{-1}(R_iM)_j\to(R_iM)_k\) indexed by \(a:k\to i\). The counit identities give the composition law: both successive constructions are adjoint to projection onto the factor indexed by the same composite arrow. A map from a system \(F\) to (HC7) is uniquely determined by \(F_i\to M\); all other components are its composites with (HC1) and adjunction. This proves the asserted right adjunction, including for an index category with parallel arrows.

Choose embeddings \(F_i\hookrightarrow J_i\) into injective sheaves, using the actual enough-injectives proof in the cohomology lesson. Their adjoints give
\[
 F\longrightarrow\prod_iR_iJ_i=:J.
 \tag{HC8}
\]
At index \(i\), the identity-arrow factor of \(R_iJ_i\) is the chosen embedding, so (HC8) is componentwise injective. Since evaluation is exact, its right adjoint takes an injective to an injective object of \(\mathcal A\). Products of injectives are injective: extending a map across a monomorphism is done in each component, and the product universal property combines the extensions. Thus \(J\) is injective in \(\mathcal A\).

Each component of \(J\) is also injective as a sheaf. Every factor in (HC7) is a direct image of an injective; its inverse-image left adjoint is exact, so the same extension argument proves injectivity of that factor. The product remains injective. Apply (HC8) successively to cokernels to construct the stated resolution.

Here are the comparison and exact-sequence arguments in this category. A map of systems extends to a chain map between two such resolutions. In degree zero extend its composite into the target injective across the source augmentation. After degrees through \(a\) are constructed, the map \(d\phi^a\) kills the kernel of the source differential, by exactness and the preceding chain identity; it therefore defines a map on its image in degree \(a+1\). Extend that map to the whole next source term by target injectivity. Two extensions induce homotopic chain maps: their difference in degree zero kills the augmentation and factors through the image of the source differential; extend this factor to a map into the target degree-zero injective, and subtract its homotopy boundary. The new difference is zero in degree zero. Repeat in each degree. Every extension occurs in \(\mathcal A\), so the resulting maps and homotopies respect the coefficient structure.

For a short exact sequence \(0\to A\to B\to C\to0\) of systems, choose embeddings \(A\to J_A\), \(C\to J_C\) of the kind just constructed. Extend \(A\to J_A\) across \(B\), and combine that extension with \(B\to C\to J_C\). This embeds \(B\) into \(J_A\oplus J_C\): an element of its kernel first maps to zero in \(C\), hence lies in \(A\), where the first component is injective. The resulting diagram has split exact injective middle row \(0\to J_A\to J_A\oplus J_C\to J_C\to0\). Its three cokernels form another short exact sequence, by the kernel/cokernel calculation in that diagram. Repeat on the cokernels. This gives degreewise split exact compatible injective resolutions and hence the connecting maps by lifted cocycle boundaries. \(\square\)

### 6.5. Why these limit sheaves are acyclic

**Lemma 6.5.** Suppose every component \(J_i\) of a coefficient system is injective. Then \(E=L(J_i)\) is acyclic for sections on every \(V\in\mathcal B_X\):
\[
 H^n(V,E)=0\qquad(n>0).
 \tag{HC9}
\]

*Proof.* Let \(\mathcal U=\{W_b\to V\}\) be a finite basis covering. Descend the objects, arrows and covering to one stage by 6.2. Lemma 6.3 identifies its Cech complex with
\[
 \check C^\bullet(\mathcal U,E)
 =\varinjlim_j\check C^\bullet(\mathcal U_j,J_j).
 \tag{HC10}
\]
Each degree has finitely many tuples of indices, so its products commute with the filtered colimit. The complex at every stage has zero positive cohomology. This is the actual injective Cech proof: the augmented chain complex of free abelian sheaves on the covering nerve is locally contracted by inserting one chosen covering lift as its first entry; hence it is exact. Applying Hom into \(J_j\) gives the exact augmented Cech complex. Filtered colimits of abelian groups preserve exactness, so (HC10) has zero positive Cech cohomology.

Here is the full step from Cech vanishing to derived vanishing. Induct simultaneously on \(n>0\) over all basis objects. Assume (HC9) in degrees strictly between zero and \(n\). A class \(\xi\in H^n(V,E)\) dies on a covering, by the local vanishing proof: represent it by a closed section in degree \(n\) of an injective resolution, and lift that section locally through the previous differential, using exactness as sheaves. Refine this covering by a finite basis covering.

We give the finite double-complex argument explicitly, so this step requires no additional spectral-sequence convergence theorem. Let \(E\to K^\bullet\) be an injective resolution on \(X\), and put \(D^{a,b}=\check C^a(\mathcal U,K^b)\). The horizontal and vertical differentials commute, and on its first-quadrant total complex use
\[
 d=d_h+(-1)^a d_v\quad\hbox{on }D^{a,b}.
 \tag{HC11}
\]
The augmented horizontal rows \(K^b(V)\to D^{0,b}\to D^{1,b}\to\cdots\) are exact by the injective covering contraction above. Their augmentation is injective on cohomology. Here is the needed verification: if an augmented degree-\(n\) cocycle is \(dB\), remove the largest positive Cech-degree component \(B^{a,b}\). Since \(dB\) has only Cech degree zero, \(d_hB^{a,b}=0\); horizontal exactness writes it as \(d_hC^{a-1,b}\). Subtract \(dC\) from \(B\), reducing that largest degree. There are finitely many components, so this ends with \(B^{0,n-1}\) horizontally closed. It is the augmentation of a section of \(K^{n-1}(V)\); hence the original class is already a boundary in \(K^\bullet(V)\).

Represent \(\xi\) by a closed section \(z\in K^n(V)\). Its restrictions are boundaries, so its augmentation \(z_0\in D^{0,n}\) is \(d_vb_0\) for some \(b_0\in D^{0,n-1}\). Successively for \(1\leq a\leq n-1\), choose \(b_a\in D^{a,n-1-a}\) such that
\(d_vb_a=(-1)^{a+1}d_hb_{a-1}\).
The right-hand side is vertically closed: for \(a=1\) use \(d_hz_0=0\), and subsequently use \(d_h^2=0\). Its vertical degree is \(n-a\), strictly between zero and \(n\). The induction hypothesis on all iterated intersections makes it a vertical boundary, so the choices exist. Products here are finite, and slice restriction of \(K^\bullet\) is an injective resolution by SH5 and the actual étale/slice equivalence EA15.

The only remaining component of \(d(\sum b_a)\) besides \(z_0\) is \(d_hb_{n-1}\in D^{n,0}\). It is vertically closed, hence is a Cech cochain of \(E\), and it is horizontally closed. Positive Cech vanishing in (HC10) writes it as \(d_hw\) for \(w\in\check C^{n-1}(\mathcal U,E)\). Replace \(b_{n-1}\) by \(b_{n-1}-w\); its vertical differential is unchanged, and now \(d(\sum b_a)=z_0\). The injectivity of the augmentation just proved gives \(\xi=0\). For \(n=1\) this argument uses only \(b_0\) and \(w\), with no intermediate choices. This proves the simultaneous induction in every degree. \(\square\)

### 6.6. Higher continuity at its full coefficient scope

**Theorem 6.6.** With the hypotheses of 6.1, the canonical map is an isomorphism for every \(n\geq0\):
\[
 \varinjlim_i H^n(X_i,F_i)
 \xrightarrow{\sim} H^n(X,L(F_i)).
 \tag{HC12}
\]
The comparison is natural in morphisms of systems, commutes with connecting homomorphisms and with restriction to any descended basis object. No torsion, finite generation, constructibility or cartesian-coefficient hypothesis is required.

*Proof.* Resolve the system in \(\mathcal A\) as \(F\to J^\bullet\) by 6.4. At every index this is an injective resolution. The functor \(L\) is exact: all inverse images are exact and filtered colimits of abelian sheaves are exact by SH1–SH2 and SH6,applied to the site functors constructed in EA15. Hence \(L(F)\to L(J^\bullet)\) is a resolution. Each term is sections-acyclic by 6.5, including on the final basis object \(X\).

An acyclic resolution computes derived sections for the following explicit reason. If \(F\to E^\bullet\) is such a resolution, put \(Z^0=F\) and \(Z^{a+1}=\operatorname{coker}(Z^a\hookrightarrow E^a)\). In
\(0\to Z^a\to E^a\to Z^{a+1}\to0\), acyclicity gives \(H^b(Z^{a+1})=H^{b+1}(Z^a)\) for \(b>0\). The group of degree-\(n\) cocycles in \(\Gamma(E^\bullet)\) is \(\Gamma(Z^n)\); its quotient by the previous boundaries is \(H^1(Z^{n-1})=H^n(F)\). Degree zero is \(\Gamma(F)\) by left exactness. Thus the resolution above really computes the target of (HC12).

By 6.3 its section complex is
\[
 \Gamma(X,L(J^\bullet))
 =\varinjlim_i\Gamma(X_i,J_i^\bullet).
 \tag{HC13}
\]
Filtered colimits of abelian groups commute with cohomology of complexes. Elementwise, a representative whose differential becomes zero is a cycle at a later stage, and a cycle that becomes a boundary has a boundary witness at a later stage. These two finite-equation tests give respectively surjectivity and injectivity of that comparison. Taking degree-\(n\) cohomology in (HC13) proves (HC12).

We check that this is the canonical higher comparison, not merely an abstract isomorphism. Choose an injective resolution \(L(F)\to K^\bullet\) on \(X\). The extension induction in 6.4 applies to any exact source resolution and injective target resolution; it constructs a chain map \(L(J^\bullet)\to K^\bullet\) extending the identity of \(L(F)\), uniquely up to homotopy. Its section map gives the acyclic-resolution identification above. Compose it with \(p_i^{-1}J_i^\bullet\to L(J^\bullet)\). This is a map from the exact pullback of the injective resolution of \(F_i\) into \(K^\bullet\), extending the canonical coefficient map \(p_i^{-1}F_i\to L(F)\). Such a map is exactly the injective-resolution construction of pullback on cohomology followed by the coefficient map; the same comparison induction proves its independence of choices. Thus taking its cohomology gives the stage-to-limit canonical map in (HC12).

Comparison maps and homotopies in 6.4 prove naturality in coefficient-system morphisms. Its split exact resolutions prove compatibility with connecting homomorphisms: inverse image, \(L\), sections and the section-colimit comparison preserve the degreewise split rows, and their lifted cocycle boundaries agree. Replacing \(X_i\) by a descended \(V_i\) and all its base changes repeats the identical proof and gives restriction compatibility. The same canonical-map description proves functoriality under compatible maps of inverse systems of schemes and coefficients: composing pullbacks is represented by composing these chain maps, and any two extensions of the same coefficient map are homotopic. No uniform bound on cohomological degrees is used; in 6.5 each fixed total degree has finitely many components. \(\square\)

The freely accessible primary targets are [Stacks, Theorem 59.51.3](https://stacks.math.columbia.edu/tag/09YQ), its [compatible-injective construction](https://stacks.math.columbia.edu/tag/0EXZ), and its [site-level continuity proof](https://stacks.math.columbia.edu/tag/09YP). They were read as materials. 6.2--6.6 supply the actual finite-data, resolution and acyclicity arguments rather than using these citations as proofs.

### 6.7. Filtered sheaves and higher direct images

**Corollary 6.7.** On every qcqs scheme \(T\), for every filtered system of abelian etale sheaves \(F_i\),
\[
 \varinjlim_iH^n(T,F_i)
 =H^n(T,\varinjlim_iF_i)
 \quad(n\geq0).
 \tag{HC14}
\]
If \(f:S\to T\) is qcqs, with arbitrary target \(T\), then
\[
 \varinjlim_iR^nf_*F_i
 =R^nf_*(\varinjlim_iF_i).
 \tag{HC15}
\]

*Proof.* For (HC14), set every scheme in 6.6 equal to \(T\) and every transition map equal to its identity. This also proves the assertion for any qcqs etale object, so in particular it supplies filtered coefficient continuity on all the intersections used in the closed-support calculation.

For (HC15), work on the affine etale basis of the target. Its inverse image under a qcqs \(f\) is a qcqs scheme. The actual higher-image presheaf proof SH6,with the site constructions EA15,computes the degree-\(n\) higher-image sheaf by sheafifying \(V\mapsto H^n(S\times_TV,F_i)\). Equation (HC14) compares the filtered colimit of these presheaves with the cohomology presheaf of the colimit sheaf. Sheafification is a left adjoint and commutes with colimits. Sheafifying that comparison proves (HC15). \(\square\)

### 6.8. Strict localizations and pro-etale changes of base

**Corollary 6.8.** Let \(f:S\to T\) be qcqs and let \(\bar t\) be a geometric point. Let \(R\) be the ring colimit of its affine pointed etale neighbourhoods over a fixed affine open of \(T\). Then, for every abelian sheaf \(F\) and every \(n\geq0\),
\[
 (R^nf_*F)_{\bar t}
 =H^n(S\times_T\operatorname{Spec}R,F|_{S\times_T\operatorname{Spec}R}).
 \tag{HC16}
\]
If \(T'=\varprojlim_\lambda T_\lambda\to T\) is a limit of qcqs etale \(T\)-schemes with affine transitions, the canonical comparison for its base-changed \(f'\) is an isomorphism:
\[
 p^{-1}R^nf_*F\xrightarrow{\sim}R^nf'_*p_S^{-1}F.
 \tag{HC17}
\]

*Proof.* The actual pointed-neighbourhood proof EA17 makes the category cofiltered: fibre products give common refinements, and the open diagonal of an etale morphism equalizes arrows near the chosen lift. Its affine subcategory suffices. Maps between affine neighbourhoods are affine. Each \(S\times_TV\) is qcqs, and their inverse limit is the scheme in (HC16). The direct-image stalk formula SC11 is proved in SH7 from SH6 before continuity is used; its left side is the colimit of their cohomology groups. Apply 6.6 to that actual cofiltered system, with the pulled-back coefficients. This proves (HC16) without replacing a filtered category by a poset. The actual construction EA18,with the specified separable residue-field closure,identifies \(R\) with the strict henselization of \(\mathcal O_{T,t}\).

For (HC17), etale restriction at a finite stage is slice localization: the two direct-image presheaves are identical on the slice, and slice restriction is exact and preserves injectives. Hence its canonical comparison is an isomorphism at every etale stage.

Here is the passage to the limit as an explicit stalk computation. A pointed finite-presentation etale neighbourhood \(V'\) of a geometric \(\bar t'\) on \(T'\) descends to some \(V_\lambda\to T_\lambda\), by 6.2. For its later base changes \(V_\mu\), 6.6 gives
\[
 H^n(S\times_TV',F|_{S\times_TV'})
 =\varinjlim_{\mu\geq\lambda}
 H^n(S\times_TV_\mu,F|_{S\times_TV_\mu}).
 \tag{HC18}
\]
Here an inequality denotes the corresponding coslice if the index is a filtered category. To verify the neighbourhood colimit carefully, consider the category of pairs \((\lambda,V_\lambda)\), with \(V_\lambda\to T_\lambda\) a basis object and a lift of \(\bar t'\) to it. Refinements are maps from later-stage basis objects into the base changes of earlier ones, preserving the chosen lifts. This category is cofiltered: choose a common receiving stage, form fibre products for common refinements, and equalize parallel arrows by the open etale diagonal and an affine neighbourhood of the chosen point. Parallel stage arrows can first be equalized by filteredness.

Base change of these pairs to \(T'\) supplies all pointed basis neighbourhoods there, by 6.2. Their arrows and equalities are supplied after refinement by the same descent lemma. Consequently their cohomology colimit is the right-side stalk in (HC17), by SC11 and the geometric stalk proof EA16. Equation (HC18) says that each class on such a limit neighbourhood is represented at a later-stage pair, and each equality of two stage classes is realized after a later-stage refinement. Thus replacing these limit-neighbourhood groups by the finite-stage groups in (HC18) changes neither classes nor their equality relations in that stalk colimit.

The same pairs suffice for the neighbourhood colimit at \(\bar t=p\bar t'\) on \(T\). Indeed any pointed neighbourhood \(W\to T\) is refined by an affine neighbourhood of the paired lift in \(W\times_TT_\lambda\); over qcqs \(T_\lambda\) that affine etale neighbourhood is a finite-presentation basis object. Two arrows from a pair to \(W\) are equalized near the lift by the open diagonal of \(W/T\); take an affine neighbourhood in that equalizer. Common refinements use fibre products at a common stage. These statements give the actual representatives and equality relations of the pointed-neighbourhood colimit; they do not assume a cofinal poset. SC11 and EA16 therefore identify the finite-stage colimit with \((R^nf_*F)_{\bar t}\). The actual inverse-image stalk formula ET21 identifies this with the stalk of the left side of (HC17). All the identifications use canonical restrictions and the finite-stage slice comparison, so their composite is the stalk of its canonical base-change map. Every stalk comparison is an isomorphism. The conservative geometric stalk proof EA16 detects isomorphisms,proving (HC17). This includes the generic-point pro-etale restriction used in the surface coordinate argument. \(\square\)

The base-ring version follows directly too: if \(B=\varinjlim B_i\), \(S\to\operatorname{Spec}A\) is qcqs and the coefficients are pulled from \(S\), apply 6.6 to \(S\times_A\operatorname{Spec}B_i\). These are qcqs with affine transitions, and their limit coefficients are the pullback sheaf by the inverse-image universal property. This is the full comparison formerly imported as (2.3), with its filtered-coefficient special case and the natural maps required in the curve argument.

### 6.9. Proof and source boundary

The higher-continuity theorem6.6 now has its actual prerequisite proofs in this lesson:SH1–SH9 and EA1–EA18,followed by the finite-data descent in6.2. Its scope includes arbitrary abelian and noncartesian coefficient systems. Sections6.7–6.8 prove its filtered-coefficient,higher-image,strict-local and pro-étale applications. These author proofs do not certify the remaining arithmetic dependencies elsewhere in the lesson or an independent whole-lesson review.

The proof of6.5 is a finite double-complex calculation. SH3–SH6 and6.4–6.6 supply existence,comparison,homotopy,exact-sequence and acyclic-resolution arguments. EA2–EA3 supplies affine gluing and finite-presentation patching;EA8–EA14 supplies full local Jacobian presentations,flatness,stability and universal open images;EA15–EA17 supplies finite covering refinements,exact site functors and conservative geometric stalks. SC11 computes the higher-image stalk before continuity,ET21 gives the inverse-image stalk formula,and EA18 constructs the strict local ring \(R\) used inHC16. The finite-data scheme-limit and covering argument is the actual6.2 proof. Section 6A now supplies the complete nilpotent-site, finite-pushforward and closed-support arguments and the normalization branch sequence. The curve Kummer and higher-vanishing calculations remain separate requirements.

## 6A. Nilpotent invariance, finite pushforward and closed support

The special-fibre argument in Lesson 8 uses three site results: invariance under the reduction immersion, exact finite pushforward with the actual geometric-fibre stalks, and the description of sheaves supported at finitely many closed points. We prove these results here, before their programme use. The invariance theorem covers integral universal homeomorphisms, including infinite integral algebras. The finite-pushforward theorem covers arbitrary finite morphisms; neither flatness nor finite presentation of the finite algebra is assumed.

The prerequisites are the actual proofs SH1–SH9, EA1–EA18 and Sections 6.2–6.8 of this lesson. The finite algebra calculation retains every nilpotent layer. Its local lifting step uses a generating tuple whose reduction is a basis; it does not assume that the tuple is a free basis over the original ring.

### 6A.1. Set-valued sheaves, point adjoints and degree-zero continuity

**NP1.** The sheafification, point and inverse-image constructions above also work for sheaves of sets. Stalks commute with colimits and finite limits, geometric stalks detect isomorphisms, and
\[
 (f^{-1}F)_{\bar y}=F_{f\bar y}
 \tag{NS1}
\]
holds for a set-valued sheaf as well as for an abelian sheaf.

*Proof.* Construct the two plus operations of SH1 from matching families and common refinements, omitting addition. Local representation and local equality have the same proofs. They prove that sheafification preserves finite limits: finitely many representatives and equalities can be put on one common refinement. Colimits are sheafifications of presheaf colimits by the same adjunction. A stalk is the filtered neighbourhood colimit, which commutes with finite limits of sets by the finite-representative argument. Covering lifts identify the stalk before and after sheafification, as in SH7, so it also commutes with all colimits.

For conservativity, replace the kernel-section argument of EA16 by a pair of sections: if their images agree, stalk injectivity makes their germs agree, and neighbourhood refinements through every ordinary point give a covering on which they agree. Stalk surjectivity gives local preimages in exactly the EA16 construction. Thus stalkwise bijectivity is an isomorphism. The finite-limit site functor of EA15 gives a left adjoint \(f^{-1}\) on sets by (SC9) and sheafification; its right adjoint is the same direct-image section rule.

Here is a point-adjoint proof of (NS1). If \(\tau\) is a geometric point functor and \(E\) a set, then
\[
 (\tau_*E)(V)=\operatorname{Map}(\tau(V),E)
 \tag{NS2}
\]
is a sheaf. A cover surjects on lifts, and lifts on its pairwise fibre products are the pairs with equal base lift, so matching functions glue uniquely. A map \(F\to\tau_*E\) is exactly a map \(F_\tau\to E\): evaluate a section at each lift and use its neighbourhood representative. These constructions are inverse. Thus the stalk is left adjoint to (NS2).

For a point \(\bar y\) upstairs, fibre-product universality gives \(\tau_{\bar y}(V\times_XY)=\tau_{f\bar y}(V)\). Consequently \(f_*\tau_{\bar y,*}=\tau_{f\bar y,*}\). The corresponding left adjoints are canonically equal, proving (NS1), with its natural maps. For abelian groups use products of groups instead of function sets; the same argument applies.

Every sheaf of sets has a presentation by sums of sheafified representables. Put \(P_U=(\operatorname{Hom}(-,U))^\#\). The identity section gives \(\operatorname{Hom}(P_U,F)=F(U)\). The sum over all such sections surjects onto \(F\). Cover its kernel pair by another such sum. The coequalizer of the resulting two arrows is \(F\): at each stalk this is the ordinary quotient of a surjective set map by its kernel pair, and stalks preserve these colimits and detect the comparison isomorphism. On the qcqs basis the same construction uses its basis objects, since they cover the whole site.

Finally Lemma 6.3 already proves degree-zero continuity for sets by finite covering equalizers. Applied to the affine pointed neighbourhoods of \(\bar x\), it gives, for a qcqs map and a set-valued sheaf,
\[
 (f_*F)_{\bar x}
   =\Gamma(Y\times_X\operatorname{Spec}R,F_R),
 \qquad R=\mathcal O_{X,x}^{\mathrm{sh}},
 \tag{NS3}
\]
where \(F_R\) is inverse image. Indeed the left side is the neighbourhood colimit of the sections of \(F\) on the corresponding inverse images; 6.3 compares exactly that colimit with the sections on their affine-transition limit. EA17–EA18 construct its index and ring, and inverse-image associativity identifies the limit coefficients with \(F_R\). For abelian sheaves this is also the \(n=0\) case of (HC16). No positive-degree assertion for sets is being used. \(\square\)

### 6A.2. Lifting across a nil ideal of unbounded exponent

A nil ideal means that each of its elements is nilpotent; a single common nilpotence exponent is not part of this definition. A finitely generated nil ideal is nilpotent. If generators \(a_i\) satisfy \(a_i^{e_i}=0\), then
\[
 (a_1,\ldots,a_r)^{\,1+\sum_i(e_i-1)}=0.
 \tag{NS4}
\]
Every monomial of that total degree contains one forbidden power. This also shows that extension of a nil ideal to another algebra is nil: every one of its elements uses only finitely many nil generators.

**NP2.** If \(B\) is a finitely presented étale \(A\)-algebra, \(C\) is an \(A\)-algebra, and \(J\subset C\) is nil, then
\[
 \operatorname{Hom}_A(B,C)\longrightarrow
 \operatorname{Hom}_A(B,C/J)
 \quad\text{is bijective}.
 \tag{NS5}
\]

*Proof.* Write a finite polynomial presentation of \(B\) and lift the images of its finitely many generators arbitrarily to \(C\). The errors in its finitely many relations belong to \(J\). Their finitely generated ideal \(J_0\) is nilpotent by (NS4). The chosen images therefore give a map \(B\to C/J_0\), whose reduction is the prescribed map to \(C/J\). EA12 gives unique lifting across a square-zero ideal; iterating through the powers of the nilpotent \(J_0\) gives a lift to \(C\). If two lifts agree modulo \(J\), their differences on the finite generator list generate another nilpotent ideal \(J_1\). They agree modulo \(J_1\), so nilpotent uniqueness gives equality. This proves both assertions without an exponent for the whole \(J\). \(\square\)

**NP3.** For a closed immersion \(j:X_0\hookrightarrow X\) with the same underlying space, base change is an equivalence of categories of étale schemes and an equivalence of their small étale sheaf categories.

*Proof.* On an affine of \(X\), the immersion is quotient by an ideal contained in every prime, hence a nil ideal by EA2. All its base changes are the same kind of closed immersion, by (NS4). They give homeomorphisms of underlying spaces.

First extend (NS5) to maps of schemes. Let \(W_0\hookrightarrow W\) be such a nil immersion over \(X\) and let \(V\to X\) be étale. A map \(W_0\to V\) lifts uniquely. Choose affine target étale charts over affine base charts and affine source charts in their inverse images. On each source chart (NS5) gives the lift. Two lifts have the same underlying point map, because \(W_0\) has every point of \(W\); around each point they can therefore be compared in one common affine target chart. Algebraic uniqueness gives equality there. It gives agreement on all source overlaps, so the local maps glue by EA2. This proves the scheme assertion, including non-quasi-compact source schemes.

For object lifting, work first over affine \(X\). Cover an étale \(V_0\to X_0\) by its affine square-Jacobian charts. Lift their polynomial coefficients and their inverted elements to \(X\); the identical Jacobian presentations define étale charts \(V_i\to X\) by EA8–EA12. Each reduction is the original chart. An overlap downstairs has a unique open lift inside each \(V_i\), by the homeomorphism of spaces. Its given map into the other reduced chart lifts uniquely by the scheme assertion just proved. The inverse map and every cocycle identity also lift uniquely. The lifted maps are therefore inverse open isomorphisms and satisfy the cocycle. Glue the charts by EA2 to obtain an étale \(V\to X\) reducing to \(V_0\).

For general \(X\), perform that construction over its affine opens. On base overlaps use the same unique map-lifting assertion to identify the restrictions; its uniqueness proves the cocycle, so they glue. Thus every object lifts, and the scheme map assertion proves full faithfulness. Fibre products commute with base change; covers correspond because every object's nil reduction has the same points and a covering is joint surjectivity. Matching families on these corresponding objects and covers give inverse sheaf functors.

The equivalence on abelian sheaves is exact and preserves injectives by its inverse exact adjunction. Terminal objects correspond, so sections correspond. Applying this to an injective resolution gives
\[
 H^q(X,F)\simeq H^q(X_0,j^{-1}F)\quad(q\geq0).
 \tag{NS6}
\]
Constant sheaves correspond: they are sheafifications of the same constant presheaves under the category equivalence. This proves the reduction-cohomology assertion at its full nil-ideal scope. \(\square\)

This transports coefficient objects rather than identifying their structure maps. For \(X=\operatorname{Spec}k[\epsilon]/(\epsilon^2)\), the transported structure sheaf has sections \(k[\epsilon]/(\epsilon^2)\); its map to \(\mathcal O_{\operatorname{Spec}k}\) has kernel \(k\epsilon\). Likewise the units \(1+a\epsilon\) form an additive copy of \(k\). Those nilpotent function and unit layers remain in the transported coefficient sheaf even though the constant étale cohomology is invariant.

### 6A.3. Finite algebras over the constructed strict local ring

**NP4.** Let \(R\) be the strict local ring constructed in EA18, with maximal ideal \(\mathfrak m\) and separably closed residue field \(k\). Every finite \(R\)-algebra is a finite product of local rings, with finite purely inseparable, and still separably closed, residue fields over \(k\).

*Proof.* A finite-dimensional algebra \(C\) over any field is Noetherian. Every prime quotient is a finite-dimensional domain, hence a field: multiplication by a nonzero element is injective and therefore surjective on its finite vector space. EA4 thus gives finitely many maximal ideals. Their intersection is the nilradical by EA2; its finite generators and (NS4) give a nilpotence power. Powers of distinct maximal ideals are still comaximal, because expanding a sufficiently high power of \(a+b=1\) puts every term in one of the two ideal powers. Chinese remaindering, with a common power killing the product, gives
\[
 C=\prod_i C_i,
 \tag{NS7}
\]
where each \(C_i\) is local Artinian with its full nilpotent maximal ideal. This is also the decomposition into its maximal-ideal localizations: outside that maximal ideal the residue is nonzero and hence a unit modulo the nilpotent ideal; the other factors vanish on localization.

Now let \(S\) be finite over \(R\). If \(S/\mathfrak mS=0\), Nakayama makes \(S=0\), the empty-product case. Otherwise choose generators \(g_1,\ldots,g_d\) lifting a \(k\)-basis of \(C=S/\mathfrak mS\); Nakayama makes them generate \(S\). A lift \(u\in S\) of an idempotent \(\bar u\in C\) acts on this tuple by a matrix over \(R\). The adjugate identity on that generating tuple makes its monic characteristic polynomial \(P\) annihilate \(u\). No freeness of \(S\) was used. Modulo \(\mathfrak m\) the tuple is a basis, so the matrix is the actual multiplication operator of \(\bar u\), an idempotent operator. Decomposing its vector space into kernel and image gives
\[
 \bar P=T^a(T-1)^b,\qquad a+b=d.
 \tag{NS8}
\]
If \(a\) or \(b\) is zero the required idempotent lift is \(1\) or \(0\). Otherwise EA18 lifts this coprime monic factorization to \(P=FG\), with the indicated reductions. The factors generate the unit ideal in \(R[T]\): the coefficient map \((v,w)\mapsto vF+wG\), with degrees less than \(b,a\), is a square matrix invertible modulo \(\mathfrak m\), by the Bézout and degree test. Its determinant is a unit in the local \(R\), so its inverse expresses \(1=vF+wG\). Chinese remaindering supplies an idempotent polynomial equal to \(0\) modulo \(F\) and \(1\) modulo \(G\). Evaluate it at \(u\). Its reduction is \(\bar u\), because evaluating a polynomial at an idempotent uses exactly its values at \(0,1\). This proves existence of the lifted idempotent.

For uniqueness, \(\mathfrak mS\) is contained in every maximal ideal of \(S\). A maximal quotient is a field finite and integral over the image \(R/\mathfrak p\); the inverse-integrality argument of EA5 makes that image a field. Its prime is consequently the unique maximal ideal \(\mathfrak m\). Thus \(\mathfrak mS\) is in the Jacobson radical. An idempotent in it is zero, since \(1-e\) is a unit and \(e(1-e)=0\). For two lifts \(e,e'\), both \(e(1-e')\) and \(e'(1-e)\) are idempotents in that ideal, so vanish, giving \(e=e'\).

The orthogonal idempotents of (NS7) therefore lift uniquely to orthogonal idempotents summing to \(1\), giving \(S=\prod_i S_i\). Each \(S_i\) is local: every maximal ideal contracts to \(\mathfrak m\), and \(C_i\) has one maximal ideal. Its residue field \(k_i\) is finite over \(k\).

Such a field is purely inseparable. In positive characteristic, write an irreducible polynomial as \(g(T^{p^e})\) with \(g'\ne0\); \(g\) is irreducible, hence separable. Since \(k\) is separably closed it has degree one. Thus a power of every element of \(k_i\) belongs to \(k\), and one exponent suffices for its finite generator list. The field \(k_i\) remains separably closed: for a separable polynomial over it, raise the coefficients to that common \(p\)-power. Its distinct roots are raised to the same powers and remain distinct, so it becomes a separable polynomial over \(k\), with every root in \(k\). Each original root is both separable and purely inseparable over \(k_i\), so belongs to \(k_i\). In characteristic zero the finite residue extension is already trivial. This proves all the field assertions. \(\square\)

### 6A.4. Lifting in a finite local algebra without a free-module assumption

**NP5.** Every local factor \(S_i\) of NP4 has the full étale residue-section property: an étale \(S_i\)-scheme with a prescribed point over its residue field \(k_i\) has a unique \(S_i\)-section through that point.

*Proof.* Choose a square-Jacobian chart around the point. Its reduction over the local Artinian algebra \(C_i=S_i/\mathfrak mS_i\) has that point over \(k_i\). The kernel \(C_i\to k_i\) is nilpotent; NP2 gives the unique lift of its coordinates to \(C_i\). Thus the reduced polynomial system has an actual solution \(\bar x\in C_i^n\) with invertible Jacobian over \(C_i\).

Choose \(g_1=1,g_2,\ldots,g_d\) in \(S_i\) lifting a \(k\)-basis of \(C_i\). They generate over \(R\) by Nakayama. Choose expressions over \(R\) for their finitely many products and for the finitely many coefficients of the system. These expressions need not be unique. They give a surjection
\[
 \pi:R^d\twoheadrightarrow S_i,\qquad
 \bar\pi:k^d\xrightarrow{\sim} C_i.
 \tag{NS9}
\]
Using a fixed parenthesization, expand the polynomial equations on the tuples \(x_j=\sum_l V_{jl}g_l\). This produces \(nd\) polynomial coordinate equations \(P_{jl}(V)\) over \(R\), whose image under \(\pi\) is the original system. Modulo \(\mathfrak m\) the chosen product expressions are the actual multiplication table of \(C_i\), because \(\bar\pi\) is a basis isomorphism. Hence their Jacobian at the coordinate vector of \(\bar x\) is exactly
\[
 J_P(\bar x):k^{nd}\simeq C_i^n
          \xrightarrow{\,J_F(\bar x)\,}C_i^n\simeq k^{nd}.
 \tag{NS10}
\]
It is invertible. The square-Jacobian chart of these coordinate equations is therefore étale over \(R\) and has the displayed \(k\)-point. EA18 gives an \(R\)-section, so the coordinate equations vanish exactly in \(R\). Their images give the required solution in \(S_i\). The inverted element is a unit because its residue at the local \(S_i\) point is nonzero. This defines the required section of the original chart and then of the scheme.

If two sections have the same residue point, their pair pulls the open diagonal back to an open of \(\operatorname{Spec}S_i\) containing its closed point. Such an open is the whole local spectrum, as proved in EA18. They therefore coincide. This argument also treats non-affine étale schemes by choosing the chart around the prescribed point; the case of no polynomial variables is simply a localization by a unit. Applying the monic factor-coefficient system (ET23) over this local ring gives its Henselian factor-lifting property; with the separably closed residue field from NP4, it is strictly Henselian. Neither flatness nor a finite presentation of \(S_i\) over \(R\) was assumed. \(\square\)

**NP6.** On the spectrum of one of these local factors, sections of any étale sheaf equal its closed geometric stalk. For abelian sheaves they are exact and have no positive derived cohomology.

*Proof.* The residue field \(k_i\) is separably closed. Any geometric lift to an étale neighbourhood of the closed point comes from a \(k_i\)-valued point: its local finite étale field fibre has only copies of \(k_i\), by EA10. NP5 gives a section of that neighbourhood with this chosen lift. Thus every germ representative pulls back to a global section. If two global sections have the same germ, a neighbourhood witnessing equality has such a section, so pulling back gives equality globally. We have proved the canonical bijection, and group isomorphism in the abelian case,
\[
 \Gamma(\operatorname{Spec}S_i,F)=F_{\bar s_i}.
 \tag{NS11}
\]
The stalk is exact by EA16 and SH7. Evaluating an injective resolution is therefore an exact augmented group complex, so \(H^q(\operatorname{Spec}S_i,F)=0\) for \(q>0\). This identifies global sections with the closed stalk; sheaves may still have other stalks on other points of the local spectrum. \(\square\)

### 6A.5. Finite pushforward and its actual stalk formula

**NP7.** Let \(f:Y\to X\) be any finite morphism and \(F\) an étale sheaf of sets or abelian groups on \(Y\). For a geometric \(\bar x\) there is a canonical isomorphism
\[
 (f_*F)_{\bar x}
       =\prod_{\bar y\in|Y\times_X\bar x|}F_{\bar y}.
 \tag{NS12}
\]
The index is the finite set of geometric fibre points, with their chosen common algebraically closed field. Scheme lengths are not multiplicities in this product.

*Proof.* Restrict to an affine neighbourhood \(X=\operatorname{Spec}A\). The finite inverse image is affine, \(\operatorname{Spec}B\), with \(B\) a finite \(A\)-module. An affine morphism is qcqs: affine inverse images are quasi-compact, and its affine diagonal is the closed immersion from the multiplication quotient \(B\otimes_AB\to B\). Quotient spectra and their localized quotient sheaves give this closed immersion directly by EA2. Thus (NS3), and (HC16) for groups, apply.

Over the strict local \(R\) of EA18, put \(S=R\otimes_AB\). It is a finite \(R\)-algebra, so NP4–NP6 give its full local decomposition. Sections over its disjoint factors are the product of their sections: their cover has empty pairwise intersections, and the sheaf equalizer is exactly that product. Each factor's sections are its closed geometric stalk.

These factors are indexed precisely by the geometric fibre points. Their closed residue fields \(k_i/k\) are finite purely inseparable and embed uniquely in the chosen algebraic closure \(\Omega\). After extension to \(\Omega\), the nilpotent ideals of the local Artinian factors stay nilpotent. Each quotient \(k_i\otimes_k\Omega\) has one prime: any prime quotient of a finite-dimensional \(\Omega\)-algebra is a field and equals \(\Omega\), and the embedding of \(k_i\) into it is the unique purely inseparable embedding. Hence each factor gives one point of the geometric fibre, even if its fibre has length greater than one. Formula (NS1) identifies the closed stalk of \(F_R\) with \(F_{\bar y}\) on \(Y\). Combining these facts with (NS3) proves (NS12).

All maps are the restriction-to-germ maps. In particular this is the natural stalk formula, compatible with maps of coefficient sheaves; an ordering merely orders its factors. If the fibre is empty, the algebra \(S\) is zero by Nakayama and the product is the one-element set or zero group, as required. \(\square\)

**NP8.** On abelian étale sheaves, finite pushforward is exact, has zero positive higher direct images, commutes with all colimits, and gives
\[
 H^q(Y,F)=H^q(X,f_*F)\quad(q\geq0).
 \tag{NS13}
\]

*Proof.* Stalks are exact, and (NS12) is a finite product of stalks. Finite products of groups preserve exact sequences: kernels are componentwise, and a preimage can be chosen in each of the finitely many components. The geometric exactness criterion EA16 therefore proves exactness of \(f_*\). Applying it to an injective resolution makes its higher cohomology sheaves zero, so \(R^qf_*=0\) for \(q>0\).

The right adjoint \(f_*\) preserves injectives because its inverse-image left adjoint is exact, by SH6 and EA15. Thus if \(F\to I^\bullet\) is an injective resolution upstairs, \(f_*F\to f_*I^\bullet\) is an injective resolution downstairs. Its section complex is literally \(\Gamma(Y,I^\bullet)\). This proves (NS13), with natural maps and no spectral-sequence premise.

For colimits, take the canonical comparison from the colimit of the direct images to the direct image of the colimit. At a geometric stalk (NS12) makes it the comparison of a colimit with a finite product of group stalks. Stalks commute with colimits by SH7. A finite product of groups is also their finite direct sum, and sums commute with colimits by their universal property. Thus every stalk comparison is an isomorphism and EA16 proves the assertion. For sheaves of sets the same reasoning proves commutation with filtered colimits, whose finite-product comparison is the finite-representative test. We do not use an arbitrary-colimit assertion for set-valued finite products. \(\square\)

Finite pushforward also satisfies arbitrary change of base, for set and abelian sheaves. In a cartesian square with finite vertical map, the natural map from the inverse image of its direct image to the direct image of the upstairs inverse image is an isomorphism. Construct it from the inverse-image/direct-image adjunction and the equality of their two composite inverse images. At a geometric point of the new base, (NS12) and (NS1) identify its two sides with products of the same original upstairs stalks. The fibre-product universal property identifies their indices: a lift to the base-changed finite scheme is exactly a lift to the original finite scheme with the given base geometric point. The comparison is the identity on each restriction-to-germ factor. Conservativity proves the isomorphism. This includes bases with inseparable residue extensions and nilpotent structure; it does not assume the finite map is flat.

### 6A.6. Closed support and the separably closed point

**NP9.** For a closed immersion \(i:Z\hookrightarrow X\), direct image is an exact fully faithful functor on abelian étale sheaves. Its essential image consists exactly of sheaves with zero geometric stalks outside \(Z\), and \(i^{-1}\) is its inverse on that image.

*Proof.* A quotient algebra \(A/I\) is finite over \(A\), generated by \(1\), even if \(I\) is not finitely generated. Thus NP7–NP8 apply. The geometric fibre of a closed immersion is empty outside \(Z\), and is one point with the same geometric field on \(Z\). Hence
\[
 (i_*G)_{\bar x}=
 \begin{cases}
   G_{\bar z},&x\in Z,\\
   0,&x\notin Z.
 \end{cases}
 \tag{NS14}
\]
Together with (NS1), this identifies the counit \(i^{-1}i_*G\to G\) at each stalk with the identity. The canonical maps can also be read directly as the single-factor restriction in (NS12). Thus the counit is an isomorphism. The adjunction then proves full faithfulness.

The unit \(F\to i_*i^{-1}F\) is likewise the identity at a point of \(Z\); outside \(Z\) its target is zero. It is an isomorphism exactly when those outside stalks of \(F\) vanish, by EA16. This proves the essential-image assertion and inverse. Exactness was already NP8. Applying (NS13) gives \(H^q(X,i_*G)=H^q(Z,G)\). \(\square\)

If \(k\) is separably closed, its finite-presentation étale schemes are finite disjoint unions of \(\operatorname{Spec}k\), by EA10. Every étale scheme over it is a disjoint union of such points: each point has one of these open affine field charts, and a singleton field chart is an open component; these components cover the scheme. The component inclusions are a covering. Consequently a sheaf is determined by its value \(M\) on the point, with value the corresponding product of \(M\)'s on every disjoint union. Conversely that rule is a sheaf, since matching values along a jointly surjective covering are exactly values on the covered points. The categories of set and abelian sheaves are therefore respectively sets and groups. In particular
\[
 \Gamma(\operatorname{Spec}k,M_k)=M,\qquad
 H^q(\operatorname{Spec}k,G)=0\quad(q>0)
 \tag{NS15}
\]
for every abelian sheaf \(G\).

For a finite collection of closed points \(s\) in \(X\), their disjoint union is a closed subscheme with the reduced residue fields. On any affine open, their distinct maximal ideals are pairwise comaximal and EA10 remaindering gives its quotient algebra; localization gives the same quotients on smaller opens, so these closed immersions glue. NP9 decomposes supported sheaves into the point direct images. If these fields are separably closed, their point sheaves are just the groups in (NS15). The finite sum of such direct images is sections-acyclic, and its sections are the direct sum of the point groups. This is the precise closed-support assertion needed for the branch cokernel.

### 6A.7. Integral universal homeomorphisms and cohomology

**NP10.** A finite universal homeomorphism gives an equivalence of small étale sheaf categories, for sets and for abelian groups.

*Proof.* At every geometric point its fibre has exactly one point: base change is a homeomorphism of spaces, and a finite algebra over an algebraically closed field has that field as every residue. Formula (NS12) has exactly one factor. Together with (NS1), it identifies both the adjunction unit \(G\to f_*f^{-1}G\) and counit \(f^{-1}f_*F\to F\) on geometric stalks with the identity. In the counit this is the single-factor evaluation, and in the unit it is the pullback germ. NP1 and EA16 detect their isomorphisms. These two inverse adjunction maps prove the equivalence. \(\square\)

**NP11.** The same equivalence, and étale-cohomology invariance, holds for any integral universal homeomorphism, without finite generation of the integral algebra.

*Proof.* We supply the algebra and limit steps. For an injective integral ring map \(A\subset B\), every prime of \(A\) lifts to \(B\). Localize at that prime. If \(1\) belonged to \(\mathfrak pB_{\mathfrak p}\), its witnessing equation would involve finitely many integral elements. They generate a finite \(A_{\mathfrak p}\)-algebra: successive monic equations bound the necessary products of their powers. That finite algebra still contains \(A_{\mathfrak p}\) injectively, and Nakayama prevents its unit from belonging to \(\mathfrak p\) times itself. Thus the quotient of the whole \(B_{\mathfrak p}\) by \(\mathfrak p\) is nonzero, and a prime there gives the lift.

It follows that an integral affine map sends each closed subset to the vanishing set of the kernel of its quotient algebra: apply the preceding lying-over proof to the quotient of the base by that kernel. Integral algebras stay integral after base change, since their monic equations persist and every element uses finitely many such integral generators. Thus integral maps are universally closed. Surjectivity is also stable under base change: over a point, a nonempty fibre stays nonempty after field extension, by the vector-space test of EA14. These statements justify the point-image assertions used next.

Work first with \(X=\operatorname{Spec}A\) and \(Y=\operatorname{Spec}B\). An integral morphism is affine with integral coordinate algebra. Express \(B\) as the filtered union of its finite \(A\)-subalgebras \(B_i\), allowing the image of \(A\) if its kernel is nonzero. Each map \(\operatorname{Spec}B\to\operatorname{Spec}B_i\) is integral and universally surjective, by the just proved lying-over statement and base change. Therefore \(f_i:\operatorname{Spec}B_i\to X\) is surjective and universally injective: two distinct points after any base change would have distinct lifts to \(Y\), contradicting universal injectivity of \(f\). It is finite and universally closed, hence a universal homeomorphism. We have
\[
 Y=\varprojlim_iY_i,\qquad Y_i=\operatorname{Spec}B_i,
 \quad f_i:Y_i\to X\text{ finite universal homeomorphisms}.
 \tag{NS16}
\]
The transition maps are affine. Their finite generation or flatness is not required for the limit theorem.

First prove that the unit \(G\to f_*f^{-1}G\) is an isomorphism. At a geometric \(\bar x\), use its strict local ring \(R\). Formula (NS3) computes the target stalk as sections on \(Y_R\). This is the affine-transition limit of the \((Y_i)_R\). Lemma 6.3, for the pulled-back set coefficients, identifies its sections with the colimit of their sections. By NP10, each finite stage's sections of \(f_{i,R}^{-1}G_R\) are \(\Gamma(\operatorname{Spec}R,G_R)\). The canonical unit maps make the stage restriction maps the identity under these identifications. NP6 for \(S=R\) and (NS1) identify this last group or set with \(G_{\bar x}\). Thus this comparison is exactly the unit stalk, and is an isomorphism. Conservativity gives the unit isomorphism, so \(f^{-1}\) is fully faithful.

It is also essentially surjective. On the qcqs étale basis of \(Y\), an object \(U\) descends to some \(U_i\) over \(Y_i\), by the actual finite-data proof 6.2. Its sheafified representable satisfies
\[
 P_U=p_i^{-1}P_{U_i}
     =f^{-1}\bigl(f_{i,*}P_{U_i}\bigr).
 \tag{NS17}
\]
Here inverse image of a sheafified representable is the one on its base change: by the adjunction, both represent the functor \(H\mapsto H(U_i\times_{Y_i}Y)\). The second equality is NP10 and inverse-image associativity. Thus every basis generator belongs to the image of \(f^{-1}\). NP1 presents any sheaf by two coproducts of such generators. Both coproducts are in the image, and full faithfulness lifts their two relation arrows to \(X\). The left adjoint \(f^{-1}\) preserves their coequalizer, proving that the presented sheaf is also in its image. This proves the equivalence on the affine base.

For general \(X\), restrict to affine opens. Direct image and inverse image on these open slices are the same section and base-change constructions, by SH5, SH6 and EA15. The affine equivalences therefore identify the global unit and counit on every such slice, or at every geometric stalk. They are globally isomorphisms. Equivalence of set sheaves preserves finite products and the defining group operations, so it also gives the abelian equivalence; both inverse functors are exact.

Terminal objects correspond, and hence sections correspond. Exact equivalences preserve injectives. Applying them to an injective resolution proves the canonical comparison
\[
 H^q(X,F)\xrightarrow{\sim}H^q(Y,f^{-1}F)\quad(q\geq0).
 \tag{NS18}
\]
Constant set sheaves are coproducts of the terminal sheaf, and the inverse image preserves these coproducts and their group operations. Thus constant abelian coefficients are preserved. This proves the full integral-homeomorphism cohomology assertion used by the reduction map. The nil immersion result NP3 is also its directly proved special case. \(\square\)

### 6A.8. The normalization branch sequence with all coefficients retained

**NP12.** Let \(\nu:\widetilde Y\to Y\) be finite and surjective and an isomorphism away from a finite set \(S\) of closed points with separably closed residue fields. Let \(b_s\) be the number of geometric points over \(s\). For any abelian group \(M\), there is an exact sequence
\[
 0\longrightarrow M_Y\longrightarrow\nu_*M_{\widetilde Y}
 \longrightarrow\bigoplus_{s\in S}
      i_{s,*}\bigl(M^{b_s}/\operatorname{diag}M\bigr)
 \longrightarrow0.
 \tag{NS19}
\]
After choosing a first branch, the point quotient is \(M^{b_s-1}\).

*Proof.* A constant sheaf has stalk \(M\): its constant presheaf has that neighbourhood colimit, unchanged by sheafification in SH7. NP7 identifies the middle stalk with the product of one \(M\) for each geometric branch. The first arrow is the pullback constant section, hence the diagonal. Surjectivity of \(\nu\) makes \(b_s\geq1\), and the diagonal is injective, including for an arbitrary group \(M\). Away from \(S\) it is an isomorphism. Its cokernel is therefore supported on \(S\), and NP9 identifies it with the point direct images of these stalk quotients; (NS15) identifies the point category with groups.

The map
\[
 (a_1,\ldots,a_b)\longmapsto
       (a_2-a_1,\ldots,a_b-a_1)
 \tag{NS20}
\]
has kernel the diagonal and is surjective by taking \(a_1=0\). This proves the quotient identification. Different branch orderings give the same canonical quotient; the displayed coordinate identification records its chosen ordering. Every stalk calculation keeps the full finite fibre algebra in NP7, so a nonreduced branch contributes one factor per geometric point rather than per scheme length. This proves (NS19) as a sheaf sequence.

NP8–NP9 identify its middle cohomology with that of \(\widetilde Y\) and make its point cokernel acyclic. SH4's long exact sequence consequently gives
\[
\begin{aligned}
0&\longrightarrow \Gamma(Y,M_Y)
 \longrightarrow\Gamma(\widetilde Y,M_{\widetilde Y})
 \longrightarrow\bigoplus_{s\in S}M^{b_s-1}\\
 &\longrightarrow H^1(Y,M_Y)
 \longrightarrow H^1(\widetilde Y,M_{\widetilde Y})
 \longrightarrow0,
\end{aligned}
 \tag{NS21}
\]
and canonical isomorphisms in degrees \(q\geq2\). No cohomology rank for the normalization components was assumed.

For a nonempty connected scheme, sections of the constant sheaf are \(M\). Indeed a section is locally represented on an étale cover by constant values. The images of the covering maps are open by EA14. Two unequal values cannot have intersecting images: an intersection point has a geometric lift to their fibre product, where the two stalk values would have to agree. Thus the images with each value form disjoint opens covering the scheme; connectedness allows one value. This proves the component-constant interpretation of the first map in (NS21) whenever the components are connected. \(\square\)

The free primary reading is the Stacks project authors' [nilpotent site invariance](https://stacks.math.columbia.edu/tag/025H), [Henselian finite algebras](https://stacks.math.columbia.edu/tag/04GE), [finite higher direct images](https://stacks.math.columbia.edu/tag/03QN), [closed support](https://stacks.math.columbia.edu/tag/04E1), and [topological invariance](https://stacks.math.columbia.edu/tag/04DY). NP1–NP12 supply the proofs used here. The coefficient-frame construction (NS9)–(NS10) supplies the nonflat finite-algebra lifting step, and (NS16)–(NS17) supply the infinite integral step. The later projective-line/genus-one Kummer, degree, Brauer and higher-vanishing calculations remain separate proofs; neither (NS19) nor topological invariance computes those ranks by itself.

### 6A.9. Graded exercise: nilpotents, fibres and branch cohomology

**Exercise 6A.1 (100 points).** Each part is worth 10 points. All cohomology refers to the small étale site.

1. Let \(A=k[\epsilon_1,\epsilon_2,\ldots]/(\epsilon_i^{i+1})\), \(I=(\epsilon_i)\). Prove that \(I\) is nil but not nilpotent, and prove the étale and constant-cohomology comparison with \(k\).
2. For \(A=k[\epsilon]/(\epsilon^2)\), compute its nilpotent units. Explain why \(\mu_m(A)\to\mu_m(k)\) is an isomorphism when \(m\) is invertible, and why \(\mu_p\) has extra sections in characteristic \(p\).
3. In NP4, explain why the characteristic-polynomial idempotent lift works even when the finite algebra is not free. Prove its uniqueness when the kernel is in the Jacobson radical rather than nilpotent.
4. Let \(k\) be algebraically closed, \(R=k[[t]]\) and \(S=R/(t^r)[\epsilon]/(\epsilon^2)\), \(r\geq1\). Use \(T^2-T-\epsilon\) to carry out the coordinate-frame lifting of NP5. Compute the coefficient Jacobian and exhibit its exact root.
5. For \(k=\mathbb F_p(s)\), \(K=k[u]/(u^p-s)\), compute the geometric fibre of \(\operatorname{Spec}K\to\operatorname{Spec}k\). State its finite-pushforward and cohomology consequences without confusing its length with a branch count.
6. With \(R,S\) as in part 4, let \(Y=\operatorname{Spec}(R\times S)\to\operatorname{Spec}R\). For an abelian group \(M\), compute the direct image of its constant sheaf, including the closed and generic geometric stalks.
7. Prove the closed-support equivalence using the unit and counit, and compute the cohomology of a sheaf supported at finitely many separably closed points.
8. Let \(A=k[t^2,t^3]\subset B=k[t]\). Prove that this finite morphism is a universal homeomorphism in every characteristic. Compute its cusp fibre and explain the invariant cohomology and the differing function rings.
9. Let \(k\) be algebraically closed of characteristic different from \(2\), \(A=k[t^2-1,t(t^2-1)]\subset k[t]\). Compute its two-branch point quotient and the resulting degree-one exact sequence, retaining any unproved cohomology of the normalization.
10. Let \(A=\mathbb F_p[s]\), \(B=\bigcup_n\mathbb F_p[s^{1/p^n}]\). Prove that the morphism is an integral universal homeomorphism that is not finite. Derive its cohomology comparison from the actual infinite-step proof.

*Full solution.*

1. Each element of \(I\) is an expression in finitely many \(\epsilon_i\). Those generators have individual finite exponents, so (NS4) makes that element nilpotent. For every \(N\), choose \(i\geq N\). Setting all other variables to zero maps \(A\) onto \(k[T]/(T^{i+1})\), where the image of \(\epsilon_i^N\) is nonzero. Thus \(I^N\ne0\); there is no uniform exponent. The quotient is \(k\). NP2 lifts maps through this nil ideal by putting their finitely many relation errors in a nilpotent subideal. NP3 lifts and glues the étale charts and identifies covers, giving its category equivalence and
\[
 H^q(\operatorname{Spec}A,M_A)
     =H^q(\operatorname{Spec}k,M_k).
 \tag{NX1}
\]
If \(k\) is separably closed these groups are \(M\) in degree zero and zero in positive degrees by (NS15). No such vanishing was asserted for other fields.

2. The kernel on units consists of \(1+a\epsilon\). Multiplication and inverse are
\[
 (1+a\epsilon)(1+b\epsilon)=1+(a+b)\epsilon,
 \qquad(1+a\epsilon)^{-1}=1-a\epsilon.
 \tag{NX2}
\]
Hence it is the additive group of \(k\). If \(m\) is invertible, the polynomial \(T^m-1\) at a residue root has invertible derivative \(mT^{m-1}\); the unique nil lift NP2 gives the isomorphism on its root groups. In characteristic \(p\),
\[
 (1+a\epsilon)^p=1
 \tag{NX3}
\]
for every \(a\), whereas a field has only \(1\) as a \(p\)-th root of \(1\). Thus the natural structure-coefficient map has a nonzero kernel. The coefficient object transported by the site equivalence is the original root sheaf, with these nil sections, rather than the root sheaf of the reduced structure ring. Constant coefficients remain the ones compared in (NX1).

3. Lift a residue basis to a generating tuple, using Nakayama. Multiplication by \(u\) is a matrix on that tuple. The adjugate of \(u\,1-M\) gives its characteristic polynomial killing every generator and hence killing \(1\), so it annihilates \(u\). Reducing makes the tuple a true basis, and multiplication by the residue idempotent is an idempotent linear operator, with characteristic polynomial \(T^a(T-1)^b\). Coprime monic lifting and the coefficient Bézout inverse give the exact polynomial idempotent described in NP4. Only the residue tuple was assumed a basis.

If \(e,e'\) reduce to the same idempotent, then \(e(1-e')\) and \(e'(1-e)\) are idempotents in the Jacobson-radical kernel. For such an idempotent \(v\), \(1-v\) is a unit and \(v(1-v)=0\), so \(v=0\). Thus \(e=ee'=e'\). This is valid for the kernel \(\mathfrak mS\), which need not be nilpotent; uniqueness was not inferred from a square-zero formula.

4. The finite \(R\)-algebra \(S\) is not flat: multiplication by \(t^r\) is injective on \(R\) and becomes zero on nonzero \(S\). Modulo \(t\), its basis is \(1,\epsilon\). This is a generating tuple over \(R\), with relations \(t^r\) killing both generators, and not a free \(R\)-basis. Write \(T=a+b\epsilon\). The coordinate equations are
\[
 P_1=a^2-a,\qquad P_2=(2a-1)b-1.
 \tag{NX4}
\]
Their residue solution is \(a=0,b=-1\), and
\[
 J_P=
 \begin{pmatrix}
 2a-1&0\\
 2b&2a-1
 \end{pmatrix},
 \qquad\det J_P=(2a-1)^2.
 \tag{NX5}
\]
Its value at that residue solution is \(1\). The same coefficients \(a=0,b=-1\) solve the equations exactly over \(R\), giving \(T=-\epsilon\) in \(S\). Direct substitution gives \(T^2-T-\epsilon=0\). The chart derivative \(2T-1=-1-2\epsilon\) is a unit, with inverse \(-1+2\epsilon\), including in characteristic \(2\). This is the nonflat coefficient-frame step, not a tensor-flatness argument. The strict local properties of \(R\) follow from EA7 and (ET9), with its algebraically closed residue: choose a Jacobian chart at any residue point and lift its tuple in the complete ring.

5. The irreducibility and non-\(p\)-th-power argument are proved in Exercise 5B.1, part 7. After extension to an algebraic closure \(\Omega\), choose the unique root \(\alpha^p=s\). The fibre is
\[
 \Omega[T]/(T-\alpha)^p.
 \tag{NX6}
\]
It has length \(p\) on the basis \(1,(T-\alpha),\ldots,(T-\alpha)^{p-1}\), but one geometric point. The morphism is finite, surjective and universally injective: its diagonal ideal is generated by \(u-v\) and has \(p\)-th power zero; after any base change it therefore has every point of the fibre product. Surjectivity follows from lying over, and finite universal closedness makes each bijective base change a homeomorphism. NP7 uses one factor in its stalk formula, and NP10 gives an equivalence of étale sheaves and the isomorphism of cohomology for all transported coefficients. These assertions do not replace the function field \(k\) by the different field \(K\).

6. At the closed point the fibre algebra is \(k\times k[\epsilon]/(\epsilon^2)\). It has vector-space dimension \(3\), but two geometric points, so the stalk is \(M^2\). At a generic geometric point the torsion factor \(S\) becomes zero, leaving one point and stalk \(M\). The whole nil scheme \(\operatorname{Spec}S\) has reduced point \(\operatorname{Spec}k\). Its nil ideal \((t,\epsilon)\) has exponent \(r+1\), with \(t^{r-1}\epsilon\ne0\), by its polynomial basis. NP3 and the factorization through the closed point therefore identify
\[
 f_*M_Y=M_X\oplus i_*M,
 \tag{NX7}
\]
where \(i:\operatorname{Spec}k\hookrightarrow\operatorname{Spec}R\). This also follows by checking the natural comparison at its geometric stalks. Global sections are \(M^2\), and positive cohomology vanishes by NP6 on the two local components and NP8. No factor of \(2r\) or \(3\) appears in the constant-sheaf branch count.

7. For the closed immersion, (NS14) makes the counit the identity on each upstairs stalk. The unit is the identity on the closed subset and maps to zero outside it. Conservativity gives the counit isomorphism and gives a unit isomorphism exactly for sheaves whose outside stalks vanish. The adjunction then identifies this subcategory with sheaves on the closed subscheme. At finitely many separably closed points these are a finite product of groups. The direct sum of their direct images has sections the sum of the groups, and positive cohomology zero by (NS13) and (NS15). This uses reduced point coefficients to describe the supported sheaf, without identifying the finite-fibre structure rings with their residue fields.

8. The element \(t\) satisfies a monic quadratic over \(A\), and \(B=A+At\), so the map is finite and surjective by lying over. In its tensor square put \(u=t\otimes1\), \(v=1\otimes t\). Their squares and cubes agree, and the integral polynomial identity
\[
 (u-v)^3=
 4(u^3-v^3)-3(u+v)(u^2-v^2)
 \tag{NX8}
\]
makes the diagonal ideal nilpotent in every characteristic. To see that this gives universal injectivity, two distinct points of any base change over one base point would give a point of their fibre product, by the nonzero tensor product of their residue fields. Such a point cannot lie on the diagonal, contradicting the diagonal's full underlying space. Finite universal closedness and surjectivity now prove the universal homeomorphism assertion.

At the cusp point, the full fibre ring is
\[
 k[t]/(t^2,t^3)=k[t]/(t^2).
 \tag{NX9}
\]
It is one point of length two. Topological invariance NP10 compares all étale cohomology with transported coefficients. The function rings differ: \(t\notin k[t^2,t^3]\), since every polynomial expression has monomial exponents in the semigroup generated by \(2,3\), which omits \(1\). We did not infer any unproved vanishing on the affine line from the comparison.

9. Put \(x=t^2-1\), \(y=t(t^2-1)\). The monic equation \(t^2=x+1\) makes the extension finite. On \(D(x)\), \(t=y/x\), so it is an isomorphism there. The complement on the target is the one point \(x=y=0\): modulo \(x\) the relation \(y^2=x^2(x+1)\) makes \(y\) nilpotent. Its fibre is
\[
 k[t]/(t^2-1)=k\times k
 \tag{NX10}
\]
at \(t=1,-1\). Thus the cokernel is \(M^2/\operatorname{diag}M\simeq M\). Both source and target are nonempty connected spectra of domains, so their constant sections are \(M\), as proved in NP12. The differences of these two branch values of the same global constant are zero. Equation (NS21) gives
\[
 0\longrightarrow M\longrightarrow H^1(\operatorname{Spec}A,M_A)
 \longrightarrow H^1(\operatorname{Spec}k[t],M)\longrightarrow0.
 \tag{NX11}
\]
The latter cohomology remains in the sequence until its own proof is supplied. The degree-\(q\) groups agree for \(q\geq2\). Thus the branch calculation is complete without importing a cohomology computation of the normalization.

10. Write \(u_n=s^{1/p^n}\). Each algebra \(B_n=\mathbb F_p[u_n]\) is finite over \(A\), with \(s=u_n^{p^n}\), and its fibre over a geometric value \(s=a\) is the one-point algebra \(\Omega[u_n]/(u_n-a^{1/p^n})^{p^n}\). Equivalently its diagonal ideal has \(p^n\)-th power zero. The preceding finite lying-over and diagonal arguments prove that every stage is a universal homeomorphism.

The union is integral, since every element belongs to a finite integral stage. Its diagonal ideal is generated by the differences \(u_n\otimes1-1\otimes u_n\), each nilpotent. Every element uses finitely many of them, so (NS4) makes the whole ideal nil. Integral lying over gives surjectivity; the diagonal argument and integral universal closedness give the universal homeomorphism. It is not finite: a finite \(A\)-module generating list would be in one stage and generate only that stage, while the next polynomial ring has \(u_{n+1}\notin\mathbb F_p[u_{n+1}^p]\) by its monomial exponents.

For cohomology, use exactly NP11. Its unit is a stalk isomorphism from finite-stage invariance and degree-zero continuity, and its essential image contains every descended sheafified representable. The two-sum presentation then gives the full sheaf equivalence, preserving injectives and sections. Hence all abelian cohomology comparisons follow. Merely knowing each finite stage's constant cohomology would not prove this equivalence for arbitrary sheaves; the unit and generator steps are essential. \(\square\)

## Proof register and unresolved arithmetic dependencies

The representation core has proofs in this lesson. Lemmas 0A.1–0A.2 supply DVR freeness, commensurability, composition series and additivity. Lemmas 0B.1–0B.2 and Proposition 0C.1 supply the Galois facts actually used. Lemmas 0D.1–0D.2 and Proposition 0E.1 establish lifting, finite coefficient fields and unique complete valuations. Lemma 0F.1 and Proposition 0F.2 construct unramified fields and Frobenius. Lemma 3.0 proves cyclotomic surjectivity. Theorems 1.2, 2.1, 2.2, 2.4, Proposition 3.1 and Theorem 4.1 therefore have their dependencies available before use. All four exercise solutions use these proofs. SH1–SH9 and EA1–EA18 supply the abstract and geometric étale foundations. Section6 proves higher continuity and its filtered,strict-local and pro-étale applications with actual in-lesson prerequisites. NP1–NP12 additionally prove full nil-ideal invariance, arbitrary finite pushforward and base change, closed support, integral universal-homeomorphism invariance and the normalization branch sequence. The other recorded arithmetic dependencies and independent whole-lesson review remain required.

Lemma 3.3 and Example 3.4 supply the torsion pairing, explicit degree-five isogeny, rational Tate-module identification and full residual inertia comparison before any use. The earlier geometric proofs used in that construction are identified at the start of §3A and were read in their current programme edition. The stated earlier geometric prerequisites remain required. The written Kronecker–Weber provider, Theorem 20.2 and Proposition 20.5 of the named class-field lesson, uses the earlier ray-field theorem and its prerequisites. The elliptic construction and class-field classification depend on those earlier results. Citations identify reading materials and actual providers; their presence alone does not close a proof obligation.

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

- [Stacks, continuity] *The Stacks project*, [Theorem 59.51.3](https://stacks.math.columbia.edu/tag/09YQ), [the compatible-injective construction](https://stacks.math.columbia.edu/tag/0EXZ), and [the site-level continuity proof](https://stacks.math.columbia.edu/tag/09YP). Sections 6.1–6.8 write the finite-data, resolution, acyclicity and canonical-comparison proofs; these free human materials identify the targets and do not replace those proofs.

These materials were read directly in their free primary editions. The proof register above identifies the earlier programme dependencies whose verification remains required.
