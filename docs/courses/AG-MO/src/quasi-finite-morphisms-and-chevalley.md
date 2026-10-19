# Quasi-finite morphisms and Chevalley’s theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A finite map has finite fibres, but finite fibres alone do not prevent points from disappearing when a parameter specializes. Quasi-finiteness describes that weaker condition. Chevalley’s theorem addresses a different question: what shape can an image have? Under the right finiteness hypothesis, the answer is a finite combination of algebraic equalities and inequalities. Such a set need be neither open nor closed, nor even locally closed.

We use Affine morphisms, relative Spec, and finite morphisms, Limits of schemes and Noetherian approximation, and the Jacobson theorem proved in Finiteness of morphisms. The algebraic Noether normalization used in Section 4 is the already written Krull dimension and Noether normalization, Corollary 3.2. Its theorem applies to every nonzero finite type algebra over a field, including finite fields and algebras with nilpotents. It does not require the algebra to be a domain.

## 1. An isolated point of a fibre

For \(f:X\to S\) locally of finite type and \(x\in X\), put \(s=f(x)\). We say that \(f\) is **quasi-finite at \(x\)** when \(x\) is isolated in the fibre \(X_s=X\times_S\operatorname{Spec}\kappa(s)\). It is **locally quasi-finite** when this holds at every point. It is **quasi-finite** when it is locally quasi-finite and quasi-compact; equivalently, its local condition is accompanied by finite type, rather than only local finite type.

**Theorem 1.1 (pointwise tests).** For \(f\) locally of finite type, the following conditions at \(x\) are equivalent:

1. \(x\) is isolated in \(X_s\).
2. \(x\) is closed in \(X_s\), and no distinct point of \(X_s\) specializes to \(x\).
3. \(\kappa(x)/\kappa(s)\) is finite, and no distinct point of \(X_s\) specializes to \(x\).

On an affine neighbourhood in the fibre, these conditions are also equivalent to its local ring at \(x\) being finite-dimensional over \(\kappa(s)\).

**Proof.** The fibre is locally of finite type over a field, hence is Jacobson by the second lesson. An isolated point forms a nonempty open containing a closed point, so is itself closed. It has no distinct generization, because every open containing a point also contains its generizations. This proves (1) implies (2).

For the converse choose an affine fibre neighbourhood \(\operatorname{Spec}C\) containing \(x\), with \(C\) of finite type over \(k=\kappa(s)\), and let its prime be \(\mathfrak q\). There are finitely many irreducible components because \(C\) is Noetherian. A component containing \(\mathfrak q\) has its generic point specializing to \(\mathfrak q\), so under (2) it is just \(\{\mathfrak q\}\). Remove all components not containing \(\mathfrak q\). The resulting open is exactly \(\{\mathfrak q\}\); thus \(x\) is isolated in the full fibre too. A closed point of a finite type algebra over a field has finite residue extension by the Nullstellensatz in the internal algebra lesson The Nullstellensatz and Jacobson rings, Theorem 1.3. Conversely, a finite residue extension makes the prime maximal: the domain \(C/\mathfrak q\), contained in that finite algebraic field and containing \(k\), is a field by the integral-domain-over-a-field argument of the preceding lesson. This proves the equivalence of (2) and (3).

Finally, the isolated point is also closed. Choose a principal neighbourhood containing only it. Its ring is a zero-dimensional Noetherian local ring, hence Artinian; its nilpotent maximal ideal has a finite filtration with finite-dimensional factors over its finite residue extension. Thus the ring, which equals \(C_{\mathfrak q}\), is finite-dimensional over \(k\). Conversely, a finite-dimensional \(C_{\mathfrak q}\) has only its maximal prime. It has finite residue field and no proper prime below \(\mathfrak q\), giving (3). \(\square\)

These are [Stacks, Tag 01TH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-quasi-finite-at-point-characterize), with the affine local-ring test at [Tag 00PJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-isolated-point). Nilpotents are allowed: a double point can be isolated. Finite residue degree alone is insufficient. A closed point of the affine line over a field has finite residue field, but has the generic point of that line as a distinct generization.

**Theorem 1.2 (finite fibres).** A finite type morphism is quasi-finite if and only if all its fibres are finite sets. These finite fibres are discrete topological spaces.

**Proof.** For a quasi-finite map every fibre point is isolated. The fibre is quasi-compact by base change, so the cover by its singleton opens has a finite subcover. Conversely, a finite fibre locally of finite type over a field is Jacobson. Every point in a finite Jacobson space is closed: its closure is the closure of the closed points it contains, and a finite union of closed points is closed. Thus each point belongs to this finite union and is closed. A finite space whose points are closed is discrete. Hence every fibre point is isolated. With finite type this is quasi-finiteness. \(\square\)

The source is [Stacks, Tags 02NG and 02NH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-quasi-finite). A finite morphism is quasi-finite by the preceding lesson. This is a statement about the finite underlying point set, not a claim that a fibre algebra is reduced.

## 2. Stability and missing boundary points

**Proposition 2.1.** Locally quasi-finite morphisms survive base change and composition. The same holds for quasi-finite morphisms. Every immersion is locally quasi-finite; a quasi-compact immersion is quasi-finite.

**Proof.** For base change, let \(x'\) lie over a point \(x\) where \(f\) is quasi-finite. In an affine chart of the original fibre, choose an open containing just \(x\). Its ring is a finite-dimensional algebra over the residue field of the base by Theorem 1.1. After extending that field to the residue field of the new base point, it is still finite-dimensional. Its spectrum is finite and discrete, so each point over \(x\), including \(x'\), is isolated in the base-changed fibre. Local finite type survives base change, proving the local assertion.

For composition \(X\xrightarrow f Y\xrightarrow g S\), fix \(x\), with images \(y,s\). Choose an open neighbourhood of \(y\) whose fibre over \(s\) has only the point \(y\). Inside its inverse image choose an open neighbourhood of \(x\) whose fibre over \(y\) has only \(x\). The fibre of this latter neighbourhood over \(s\) maps into the single point \(y\); its points over \(y\) are exactly the points of the fibre over that point. Thus it has only \(x\). Local finite type of the composite follows from the second lesson, so the composite is locally quasi-finite. Quasi-compactness survives composition and base change, giving the global assertions. An immersion is locally of finite type, and each nonempty fibre is one point with the base residue field; hence it is locally quasi-finite. \(\square\)

These are [Stacks, Tags 01TL–01TN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-quasi-finite). In particular, every open immersion is locally quasi-finite. It is quasi-finite in our convention exactly when it is quasi-compact. Omitting that qualification would incorrectly turn an arbitrary open immersion into a finite type map. A finite open immersion is exactly an inclusion of an open-and-closed subscheme: finite implies closed image, and an open-and-closed inclusion is a closed immersion, hence finite.

The nodal normalization from the preceding lesson gives a different boundary phenomenon. Assume \(\operatorname{char}k\ne2\), and use

\[
A=k[u^2-1,u(u^2-1)]\subset B=k[u].
\]

Remove the normalization point \(u=-1\), obtaining \(\operatorname{Spec}B_{u+1}\to\operatorname{Spec}A\). This is of finite type and has finite fibres as a restriction of the finite normalization, so is quasi-finite. It is not finite: if \(B_{u+1}\) were integral over \(A\), the element \((u+1)^{-1}\) would be integral over \(B\) as well. The normality of \(k[u]\) would put it in \(k[u]\), a contradiction. The other point over the node remains, so the map is still surjective. Quasi-finite and surjective need not imply finite.

## 2A. An algebraic proof of openness

The pointwise tests in Section 1 and the integral-extension proofs in the prerequisite algebra course suffice for this argument. The conductor lemmas in The theorem on formal functions, Appendix Z are a prerequisite here; their proofs use those same pointwise tests, not openness or Chevalley’s theorem.

### The algebraic neighbourhood

**Theorem 2A.1 (algebraic Zariski Main Theorem).** Let \(R\to B\) be finite type and let \(C\subset B\) consist of the elements integral over \(R\). If \(\mathfrak q\in\operatorname{Spec}B\) is a quasi-finite point over \(R\), there is \(g\in C\setminus\mathfrak q\) such that

\[
C_g=B_g.
\tag{2A.1}
\]

Equality means equality through the natural localization map. In particular a neighbourhood of \(\mathfrak q\) maps isomorphically to an open of \(\operatorname{Spec}C\). We will prove this by induction, first explaining the one-variable calculation. The two conductor facts used in the finite-extension step are proved in Appendix Z of The theorem on formal functions, with the precise lemmas identified below.

**Lemma 2A.2 (one algebra generator).** Theorem 2A.1 holds when \(B=R[b]\).

**Proof.** Put \(\mathfrak p=\mathfrak q\cap R\). Write \(B=R[T]/I\). Some polynomial in \(I\) has a coefficient outside \(\mathfrak p\). Otherwise the fibre would be \(\kappa(\mathfrak p)[T]\), which has no isolated points: a closed point has the zero prime as a proper generalization, and the zero prime has transcendental residue field. Either contradicts the quasi-finite point test. Thus in \(B\) there is a relation

\[
a_m b^m+\cdots+a_0=0
\tag{2A.2}
\]

with coefficients in \(C\), at least one outside \(\mathfrak q\). We may start with coefficients in the image of \(R\); allowing \(C\) will permit induction on the degree.

For \(m\geq1\), the element \(a_m b\) is integral over \(C\). Multiplying (2A.2) by \(a_m^{m-1}\) gives the monic equation

\[
(a_m b)^m+a_{m-1}(a_m b)^{m-1}
+a_{m-2}a_m(a_m b)^{m-2}+\cdots+a_0a_m^{m-1}=0.
\tag{2A.3}
\]

Transitivity of integrality therefore puts \(a_m b\) in \(C\). If \(a_m\notin\mathfrak q\), take \(g=a_m\): then \(b=(a_m b)/a_m\in C_g\), and \(B_g=C_g\). If \(a_m\in\mathfrak q\), combine the first two terms as
\((a_m b+a_{m-1})b^{m-1}\). This is a relation of smaller degree with coefficients in \(C\). At least one coefficient still lies outside \(\mathfrak q\), because \(a_m b\in\mathfrak q\) and the new coefficient is congruent to \(a_{m-1}\). Repeat. A degree-zero relation with its sole coefficient outside \(\mathfrak q\) is impossible, so a leading coefficient outside \(\mathfrak q\) must eventually occur. Localization is injective on the inclusion \(C\subset B\), proving the desired equality. \(\square\)

This is the monogenic calculation of [Stacks, Tag 00Q8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-finite-monogenic). It uses neither domains nor reducedness.

### Conductors and induction

For an inclusion \(A\subset B\), its **conductor** is

\[
J=\{u\in B:uB\subset A\}.
\tag{2A.4}
\]

It is an ideal of \(B\) contained in \(A\). At an element \(u\in J\), localization makes \(A_u=B_u\), since \(v=(uv)/u\) for every \(v\in B\). The conductor thus locates where a finite extension becomes an equality.

We use the following two proved algebraic lemmas from The theorem on formal functions, Appendix Z. Suppose \(A\subset B\), \(A\) is integrally closed in \(B\), and \(B\) is finite over \(A[b]\). Let \(J\) be the conductor from \(B\) to \(A[b]\).

* If \(u\sum_i a_i b^i\in\sqrt J\), with \(u\in B\) and \(a_i\in A\), then every \(ua_i\in\sqrt J\). The full proof is Lemma Z.6, with Situation Z.4 and the leading-coefficient proofs in Lemmas Z.1–Z.5.
* If reduced rings \(A_0\subset B_0\) contain an element \(b_0\) such that \(u\sum_i a_i b_0^i=0\) always implies every \(ua_i=0\), and \(B_0\) is finite over \(A_0[b_0]\), then \(B_0/A_0\) is quasi-finite at no point. This is the strongly transcendental case; its complete proof is Lemma Z.11, with Definition Z.7 and Lemmas Z.8–Z.10. That proof passes to a minimal component and uses the integral polynomial-algebra case.

These lemmas apply over arbitrary rings with precisely the stated hypotheses. Their proofs, including localization in the presence of zero divisors and the passage to a minimal component, are written in that programme appendix.

**Lemma 2A.3 (finite over one generator).** Suppose \(A\subset B\), \(A\) is integrally closed in \(B\), \(B\) is finite over \(A[b]\), and \(B/A\) is quasi-finite at \(\mathfrak q\). There is \(h\in A\setminus\mathfrak q\) with \(A_h=B_h\).

**Proof.** The first conductor fact says that the image of \(b\) in \(B/\sqrt J\) satisfies the second fact's condition over
\(A/(A\cap\sqrt J)\). Both quotient rings are reduced. The finite extension descends to their quotients. Thus this quotient extension has no quasi-finite point. If \(\mathfrak q\) contained \(J\), it would give just such a point: its fibre is a closed subspace of the original fibre, so the isolated point remains isolated and its residue extension remains finite. This contradiction proves \(J\not\subset\mathfrak q\).

Choose \(u\in J\setminus\mathfrak q\), giving \(A[b]_u=B_u\). The contracted point of \(\operatorname{Spec}A[b]\) is quasi-finite, because its local fibre ring agrees with the original one. The integral closure of \(A\) in \(A[b]\) is \(A\). Lemma 2A.2 therefore gives \(a\in A\setminus\mathfrak q\) with \(A_a=A[b]_a\). In this ring write \(u=c/a^N\), with \(c\in A\). Its image is outside the chosen prime, so \(c\notin\mathfrak q\). Invert \(h=ac\). Then both \(a\) and \(u\) are units and the two equalities give \(A_h=B_h\). \(\square\)

**Proof of Theorem 2A.1.** Replacing \(R\) by its image in \(B\) does not change its fibres or integral closure. Choose the least \(n\) such that \(B\) is finite over \(R[b_1,\ldots,b_n]\). For \(n=0\), all of \(B\) is integral over \(R\), so \(C=B\).

For \(n=1\), replace the base by \(C\). The extension remains quasi-finite at \(\mathfrak q\): its fibre is a subspace of the old fibre and \(B\) is still a finite-type \(C\)-algebra. The ring \(C\) is integrally closed in \(B\) by transitivity. Also \(B\) is finite over \(C[b_1]\). Lemma 2A.3 applies and proves (2A.1).

For \(n>1\), let \(D\subset B\) be the integral closure of \(R[b_1,\ldots,b_{n-1}]\) in \(B\). The same permanence argument makes \(B/D\) quasi-finite at \(\mathfrak q\), and \(B\) is finite over \(D[b_n]\). Lemma 2A.3 supplies \(v\in D\setminus\mathfrak q\) with \(D_v=B_v\).

We cannot directly apply induction to \(D\): it need not be finitely generated over \(R\). Instead, choose finitely many numerators in \(D\) for a finite \(R\)-algebra generating list of \(B_v\). Let \(E\subset D\) be generated over \(R\) by those numerators, \(v\), and \(b_1,\ldots,b_{n-1}\). Then \(E_v=B_v\), and \(E\) is finite over \(R[b_1,\ldots,b_{n-1}]\), since its added generators are integral over that ring. At the contracted prime its local ring and local fibre ring agree with those of \(B\), so it is quasi-finite over \(R\).

Induction supplies the integral closure \(F\) of \(R\) in \(E\) and \(w\in F\setminus\mathfrak q\) with \(F_w=E_w\). Write \(v=c/w^M\) in this localization, with \(c\in F\setminus\mathfrak q\). Inverting \(g=wc\) makes \(v,w\) units, hence
\(F_g=E_g=B_g\). Since \(F\subset C\subset B\), it follows that \(C_g=B_g\). \(\square\)

The induction is [Stacks, Tag 00Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-main-theorem). The finite intermediate algebra is indispensable; integral closure itself need not be finite type.

### Openness of the quasi-finite locus

**Theorem 2A.4.** The quasi-finite locus of a locally finite-type morphism is open.

**Proof.** Work on an affine chart \(R\to B\). At a quasi-finite prime use Theorem 2A.1 to obtain \(C_g=B_g\). Choose finitely many integral numerators in \(C\) that, together with \(g^{-1}\), generate \(B_g\) over \(R\). Let \(D\subset C\) be the \(R\)-algebra generated by those numerators and \(g\). It is finite over \(R\), and \(D_g=B_g\). A finite map is quasi-finite, and restricting its source to an open preserves local quasi-finiteness. Thus all points of \(D(g)\subset\operatorname{Spec}B\) are quasi-finite over \(R\). These affine neighbourhoods prove openness and glue across source charts. \(\square\)


## 3. Constructible sets

An open subset \(U\) of a topological space \(T\) is **retrocompact** if its intersection with every quasi-compact open of \(T\) is quasi-compact. A subset is **constructible** if it is a finite union of sets \(U\setminus V\) with \(U,V\) retrocompact open. A subset is **locally constructible** if this holds on an open cover. Constructible sets form a Boolean algebra: finite unions and intersections of retrocompact opens are retrocompact, and taking complements or finite intersections of their differences gives further finite combinations of the same form.

On \(\operatorname{Spec}R\), retrocompact opens are precisely the quasi-compact opens. They are finite unions of principal opens. Consequently every constructible subset is a finite union of sets

\[
D(g)\cap V(h_1,\ldots,h_m).
\tag{3.1}
\]

In particular, closed subsets defined by arbitrary infinitely generated ideals need not be constructible on a non-Noetherian affine scheme.

**Theorem 3.1 (Noetherian constructibility).** In a Noetherian topological space \(T\), the constructible subsets are precisely the finite unions of locally closed subsets. A subset \(E\) is constructible if and only if for every irreducible closed \(Z\subset T\), either \(E\cap Z\) is not dense in \(Z\), or it contains a nonempty open subset of \(Z\). The inverse image of a constructible set under a continuous map between Noetherian spaces is constructible.

**Proof.** Every open of a Noetherian space is quasi-compact, so it is retrocompact. A difference of two opens is locally closed. Conversely, a locally closed subset is an open intersected with a closed subset, hence a difference of opens. This proves the first assertion and, by taking inverse images of open and closed sets, the final assertion.

Suppose \(E\) is constructible and \(E\cap Z\) is dense in irreducible \(Z\). Express that intersection as a finite union of locally closed subsets. Their closures cover \(Z\), so irreducibility makes at least one closure equal to \(Z\). That locally closed subset is then a nonempty open of \(Z\).

Conversely, suppose the stated condition holds but \(E\) is not constructible. By the descending-chain condition choose a minimal closed \(F\) such that \(E\cap F\) is not constructible in \(F\). If \(F\) had several irreducible components, its intersection with each proper component would be constructible by minimality. Their finite union would make \(E\cap F\) constructible, so \(F\) is irreducible. If \(E\cap F\) is not dense, its closure is a proper closed subset of \(F\), and minimality again makes it constructible. Otherwise it contains a nonempty open \(W\) of \(F\). The remainder is \(E\cap(F\setminus W)\), constructible by minimality. Its union with \(W\) is constructible, the final contradiction. \(\square\)

These are [Stacks, Tags 005L, 053Y, and 053Z](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/topology.html#topology-lemma-characterize-constructible-Noetherian). The criterion quantifies over every irreducible closed subset, not just the components of \(T\).

Two useful locality facts hold on schemes. Intersecting a constructible set with an open subset preserves constructibility in that open: a quasi-compact open there is also a quasi-compact open in the original space, so the retrocompactness test restricts. A locally constructible set is therefore constructible on every affine open. Indeed, refine its defining open cover on that affine to a finite principal-open cover; pieces constructible in a principal open are constructible in the affine scheme by localization and (3.1). On a qcqs scheme a finite affine cover then makes every locally constructible set globally constructible. Its affine opens and all their quasi-compact subopens are retrocompact in the whole scheme by quasi-separatedness, so their finite Boolean descriptions extend globally.

## 4. Why a dominant finite type map contains an open

**Lemma 4.1 (the generic image lemma).** Let \(A\subset B\) be an injective ring map with \(A\) a domain and \(B\) a finite type \(A\)-algebra. There is a nonzero \(a\in A\) such that \(D(a)\subset\operatorname{Spec}A\) is contained in the image of \(\operatorname{Spec}B\).

**Proof.** Put \(K=\operatorname{Frac}A\). Injectivity makes \(B\otimes_AK\) nonzero. Noether normalization, Corollary 3.2 in the internal algebra lesson named in the introduction, gives a polynomial subring

\[
K[t_1,\ldots,t_d]\subset B\otimes_AK
\]

over which this algebra is finite. Represent the \(t_i\) in \(B_a\) for some nonzero \(a\). Fix finitely many algebra generators \(b_j\) of \(B\). Each \(b_j\) satisfies a monic equation with coefficients in \(K[t_1,\ldots,t_d]\). Invert one further product of nonzero elements of \(A\) to represent all coefficients and make all these finite equations hold in \(B_a\). This last step is valid even if \(B\) has \(A\)-torsion: an equation zero after tensoring with \(K\) is killed by some nonzero denominator.

Algebraic independence over \(K\) makes \(A_a[t_1,\ldots,t_d]\to B_a\) injective. The monic equations make \(B_a\) integral and of finite type over that subring, hence finite. Lying over makes its spectrum surject onto the polynomial-ring spectrum. The latter surjects onto \(\operatorname{Spec}A_a\), since the polynomial algebra over every residue field is nonzero. Thus every point of \(D(a)\) belongs to the image. \(\square\)

This lemma does not need \(A\) Noetherian. The Noetherian hypothesis in the next theorem makes a finite induction on closed subsets possible. The lemma is a concrete explanation of the dense-open step: finite field-level relations become valid after inverting finitely many coefficients and denominators.

**Theorem 4.2 (Noetherian Chevalley theorem).** For a finite type morphism \(f:X\to Y\) between Noetherian schemes, the image of every constructible subset of \(X\) is constructible in \(Y\).

**Proof.** First consider the full image. To apply Theorem 3.1, take an irreducible closed \(Z\subset Y\) for which \(f(X)\cap Z\) is dense. The inverse image of \(Z\), with any closed subscheme structure defining it, is Noetherian and has finitely many irreducible components. One component has dense image in \(Z\): the closures of the finitely many component images cover \(Z\), and irreducibility forces one to be all of \(Z\). Give that component and \(Z\) reduced structures. We have a dominant finite type map between integral schemes.

Choose an affine open of \(Z\), and a nonempty affine open in its inverse image on that component. Its map is still dominant, because the generic point of the source maps to the generic point of \(Z\). The corresponding ring map is an injective finite type map from a domain. Lemma 4.1 gives a nonempty open of \(Z\) contained in its image. It lies in \(f(X)\cap Z\). The criterion of Theorem 3.1 proves that \(f(X)\) is constructible.

Now express a constructible \(E\subset X\) as a finite union of locally closed subsets. Give each such subset its reduced locally closed subscheme structure. Its map to \(Y\) is of finite type: closed immersions are of finite type, and the open part is quasi-compact on a Noetherian scheme. Apply the full-image result to each piece, and take their finite union. \(\square\)

The same results are treated in [Stacks, Tag 054K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-theorem-chevalley). Vakil’s *The Rising Sea*, §8.4, emphasizes the equivalent elimination question: which parameter values allow a polynomial system, including nonvanishing conditions, to have a solution? The proof above uses Noether normalization for the dense-open step and gives the full Noetherian induction through Theorem 3.1.

## 5. Chevalley by Noetherian approximation

**Theorem 5.1 (general Chevalley theorem).** Let \(f:X\to Y\) be quasi-compact and locally of finite presentation. The image of every locally constructible subset of \(X\) is locally constructible in \(Y\). If \(Y\) is qcqs, that image is constructible. In particular, when \(Y\) is qcqs the image of every constructible subset is constructible.

**Proof.** First take an affine map \(\operatorname{Spec}B\to\operatorname{Spec}A\) with \(B\) finitely presented over \(A\). A constructible set is a finite union of pieces (3.1) in \(\operatorname{Spec}B\). Write \(A\) as the filtered union of its finite type \(\mathbf Z\)-subalgebras, as in the limits lesson. A finite presentation of \(B\) descends to an algebra \(B_i\) over one of these subalgebras \(A_i\); the finitely many elements defining all the pieces also descend. Let \(E_i\) be the resulting constructible set in \(\operatorname{Spec}B_i\). Then \(E\) is its inverse image under base change. Both stage schemes are Noetherian, so Theorem 4.2 makes \(F_i=f_i(E_i)\) constructible.

The image after base change is exactly the inverse image of \(F_i\). For the nontrivial inclusion, if a new-base point lies over a point in \(F_i\), choose a stage point of \(E_i\) above it. The tensor product of its residue field with the new-base residue field over the common base residue field is nonzero, and has a prime ideal. That prime supplies a point in the base-changed source and in the inverse image of \(E_i\). The reverse inclusion is immediate. A finite principal-open description of \(F_i\) pulls back to one over \(A\), so the image is constructible.

For the scheme assertion, restrict to an affine open \(V\subset Y\). Quasi-compactness makes \(f^{-1}(V)\) quasi-compact, so cover it by finitely many affine opens \(U_a\). Each chart map \(U_a\to V\) is of finite presentation, by the affine characterization from the second lesson. A locally constructible set restricts to a constructible set in every \(U_a\), by Section 3. The affine result makes each image constructible in \(V\), and the finite union is \(f(E)\cap V\). This proves local constructibility on \(Y\). If \(Y\) is qcqs, Section 3 turns it into global constructibility. \(\square\)

The precise source distinction is [Stacks, Tag 054J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-chevalley) for the qcqs target and [Tag 054K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-theorem-chevalley) for local constructibility on an arbitrary target. The argument does not assume \(f\) quasi-separated: it descends finitely many affine algebras and Boolean conditions, rather than a global finitely presented model of \(X\). This distinction keeps the theorem’s full stated generality.

Finite type alone over a non-Noetherian base is insufficient. Let \(A=k[x_1,x_2,\ldots]\), \(I=(x_1,x_2,\ldots)\), and \(X=\operatorname{Spec}(A/I)\). Its finite closed immersion has image \(V(I)\), the one maximal ideal \(I\). This singleton is not constructible. A constructible description would use only finitely many polynomial conditions and hence only finitely many variables. Setting those variables to zero makes membership agree for the prime generated by them and for \(I\), although the former prime omits every unused variable and is not in \(V(I)\). The map is finite type but not finite presentation. Closedness of an image does not guarantee its constructibility here.

## 6. Exercises with solutions

**Exercise 6.1 (easy: a constructible image with a missing line).** Compute the image of \((a,b)\mapsto(a,ab)\) on \(\mathbf A^2_k\) as a subset of the scheme, and prove that it is not locally closed.

**Solution.** With target coordinates \(x,z\), the fibre ring at a point with residue field \(L\) is \(L[b]/(xb-z)\). If \(x\ne0\) it is \(L\); if \(x=0\), it is nonzero exactly when \(z=0\). Thus the image is \(D(x)\cup V(x,z)\), including all scheme points specified by those conditions. It is dense because it contains \(D(x)\). A dense locally closed subset would be open in the whole plane. Any neighbourhood of the origin contains the generic point of the line \(x=0\), which the image omits. The image is therefore not open and not locally closed, although it is constructible.

**Exercise 6.2 (easy: the open-immersion qualification).** Prove that an open immersion is locally quasi-finite, that a quasi-compact open immersion is quasi-finite, and that arbitrary open immersions need not be quasi-finite. Characterize the finite open immersions.

**Solution.** A nonempty fibre of an open immersion is \(\operatorname{Spec}\kappa(s)\), so has one isolated point. Open immersions are locally of finite type. With quasi-compactness this is quasi-finiteness by definition. For a counterexample without it, take \(A=k[x_1,x_2,\ldots]\) and \(U=\bigcup_iD(x_i)\subset\operatorname{Spec}A\). This cover has no finite subcover: for any finite list of indices, the ideal generated by those variables is prime and avoids some other variable, giving a point in \(U\) outside that finite union. Thus \(U\) is not quasi-compact and its open immersion is not quasi-finite. Finally, finite maps have closed image. If an open subscheme is also closed, its inclusion is a closed immersion: glue the zero ideal on it and the unit ideal on its open complement. It is consequently finite.

**Exercise 6.3 (medium: the irreducible-closed test).** Give the Noetherian constructibility criterion a usable form: show that if a subset \(E\) satisfies its dense-open alternative on every irreducible closed subset, then for every closed \(F\), \(E\cap F\) is constructible in \(F\).

**Solution.** The alternative restricts to \(F\), since an irreducible closed subset of \(F\) is closed in the whole space. Repeat the minimal-bad-closed-subset proof of Theorem 3.1 inside \(F\). A reducible minimal bad subset is the finite union of proper irreducible components whose intersections are already constructible. An irreducible one either has a proper closure of its intersection with \(E\), or has a nonempty open contained in \(E\). In the first case use that proper closure; in the second use its closed complement. Both contradict minimality. This proves the assertion for every \(F\), including the empty subset.

**Exercise 6.4 (medium: dominant varieties).** Show that the image of a dominant morphism of varieties contains a dense open of its target. Here a variety is an integral separated scheme of finite type over a field.

**Solution.** A morphism of varieties is of finite type: this follows from finite-type cancellation applied to their structure morphisms, together with quasi-compactness over the Noetherian target. Its image is constructible by Theorem 4.2 and dense by dominance. Apply Theorem 3.1 to the irreducible target itself. The resulting nonempty open is dense. Alternatively, choose compatible affine opens and apply Lemma 4.1 to the resulting injective map of finite type domains. Dominance does not imply that the entire image is open; Exercise 6.1 gives a dominant map with a nonopen image.

**Exercise 6.5 (hard: keeping the generality in approximation).** Deduce Theorem 5.1 from the Noetherian theorem. Identify the finite data that descend and explain why quasi-separatedness of \(X\to Y\) is unnecessary. Also justify the equality of images under base change used in that deduction.

**Solution.** On an affine target, quasi-compactness gives a finite affine source cover. On each source chart, local finite presentation gives a finite list of algebra generators and relations. Constructibility gives finitely many elements specifying principal opens and finitely generated closed conditions. Descend all their coefficients and elements to one finite type \(\mathbf Z\)-subalgebra of the target ring. The stage map is between Noetherian affine schemes, so its image of each stage constructible piece is constructible. A point above that stage image lifts after base change because the tensor product of the two relevant residue fields over their common field is nonzero: it is a nonzero vector-space extension of either field, so its spectrum is nonempty. Thus the new image is precisely the inverse image of the stage image, whose finite Boolean conditions pull back.

Take the finite union over source charts, then work separately on each affine target chart to obtain local constructibility. On a qcqs target the finite affine-cover argument makes it global. The source charts do not have to glue to a descended global source scheme, so their intersections need no finiteness hypothesis. That is why imposing quasi-separatedness of the original morphism would unnecessarily weaken the theorem.

## Sources and proof dependencies

The primary reference is *The Stacks project*, read in its AI Integrated Stacks Project edition: quasi-finite point tests at 01TH and 00PJ, finite fibres at 02NG–02NH, stability at 01TL–01TN, constructible topology at 005L and 053Y–053Z, and Chevalley at 054J–054K and its algebra version 00FE. The internal algebra proof of Noether normalization is *Krull dimension and Noether normalization*, Corollary 3.2; the Jacobson and residue-field inputs are named in Section 1. All four assigned results and all five exercises are proved in this lesson. Openness of the quasi-finite locus is proved in Section 2A, from the pointwise criterion in Section 1 and the complete prerequisite conductor proofs in Appendix Z of *The theorem on formal functions*. Referenced Stacks source text retains the GNU Free Documentation License; none is reproduced here. Vakil’s *The Rising Sea*, §8.4, was consulted for the geometric image and elimination viewpoints. The expression here is independent CC0 material.
