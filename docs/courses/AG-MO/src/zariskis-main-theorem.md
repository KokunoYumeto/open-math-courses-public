# Zariski's Main Theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A quasi-finite map has finite fibres, but it can omit points that would be present in a finite map. Zariski's Main Theorem makes this precise: with separatedness and a suitable base, it is an open part of a finite map. The algebraic theorem first finds that open part inside an integral closure. Finite generation then lets us replace the possibly infinite integral closure by a finite algebra.

We use the fibre tests of Quasi-finite morphisms and Chevalley's theorem, Affine, integral and finite morphisms, and the integral-extension results of Integral extensions: lying over, going up and going down. A quasi-finite morphism is of finite type and is quasi-finite at every point. Locally quasi-finite means locally of finite type with every point isolated in its fibre. An integral closure in an algebra refers to elements integral over the image of the base ring; the base map need not be injective.

## 1. The algebraic neighbourhood

**Theorem 1.1 (algebraic Zariski Main Theorem).** Let \(R\to B\) be finite type and let \(C\subset B\) consist of the elements integral over \(R\). If \(\mathfrak q\in\operatorname{Spec}B\) is a quasi-finite point over \(R\), there is \(g\in C\setminus\mathfrak q\) such that

\[
C_g=B_g.
\tag{1.1}
\]

Equality means equality through the natural localization map. In particular a neighbourhood of \(\mathfrak q\) maps isomorphically to an open of \(\operatorname{Spec}C\). We will prove this by induction, first explaining the one-variable calculation. The two conductor facts used in the finite-extension step are proved in Appendix Z of The theorem on formal functions, with the precise lemmas identified in Section 2.

**Lemma 1.2 (one algebra generator).** Theorem 1.1 holds when \(B=R[b]\).

**Proof.** Put \(\mathfrak p=\mathfrak q\cap R\). Write \(B=R[T]/I\). Some polynomial in \(I\) has a coefficient outside \(\mathfrak p\). Otherwise the fibre would be \(\kappa(\mathfrak p)[T]\), which has no isolated points: a closed point has the zero prime as a proper generalization, and the zero prime has transcendental residue field. Either contradicts the quasi-finite point test. Thus in \(B\) there is a relation

\[
a_m b^m+\cdots+a_0=0
\tag{1.2}
\]

with coefficients in \(C\), at least one outside \(\mathfrak q\). We may start with coefficients in the image of \(R\); allowing \(C\) will permit induction on the degree.

For \(m\geq1\), the element \(a_m b\) is integral over \(C\). Multiplying (1.2) by \(a_m^{m-1}\) gives the monic equation

\[
(a_m b)^m+a_{m-1}(a_m b)^{m-1}
+a_{m-2}a_m(a_m b)^{m-2}+\cdots+a_0a_m^{m-1}=0.
\tag{1.3}
\]

Transitivity of integrality therefore puts \(a_m b\) in \(C\). If \(a_m\notin\mathfrak q\), take \(g=a_m\): then \(b=(a_m b)/a_m\in C_g\), and \(B_g=C_g\). If \(a_m\in\mathfrak q\), combine the first two terms as
\((a_m b+a_{m-1})b^{m-1}\). This is a relation of smaller degree with coefficients in \(C\). At least one coefficient still lies outside \(\mathfrak q\), because \(a_m b\in\mathfrak q\) and the new coefficient is congruent to \(a_{m-1}\). Repeat. A degree-zero relation with its sole coefficient outside \(\mathfrak q\) is impossible, so a leading coefficient outside \(\mathfrak q\) must eventually occur. Localization is injective on the inclusion \(C\subset B\), proving the desired equality. \(\square\)

This is the monogenic calculation of [Stacks, Tag 00Q8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-finite-monogenic). It uses neither domains nor reducedness.

## 2. Conductors and induction

For an inclusion \(A\subset B\), its **conductor** is

\[
J=\{u\in B:uB\subset A\}.
\tag{2.1}
\]

It is an ideal of \(B\) contained in \(A\). At an element \(u\in J\), localization makes \(A_u=B_u\), since \(v=(uv)/u\) for every \(v\in B\). The conductor thus locates where a finite extension becomes an equality.

We use the following two proved algebraic lemmas from The theorem on formal functions, Appendix Z. Suppose \(A\subset B\), \(A\) is integrally closed in \(B\), and \(B\) is finite over \(A[b]\). Let \(J\) be the conductor from \(B\) to \(A[b]\).

* If \(u\sum_i a_i b^i\in\sqrt J\), with \(u\in B\) and \(a_i\in A\), then every \(ua_i\in\sqrt J\). The full proof is Lemma Z.6, with Situation Z.4 and the leading-coefficient proofs in Lemmas Z.1–Z.5.
* If reduced rings \(A_0\subset B_0\) contain an element \(b_0\) such that \(u\sum_i a_i b_0^i=0\) always implies every \(ua_i=0\), and \(B_0\) is finite over \(A_0[b_0]\), then \(B_0/A_0\) is quasi-finite at no point. This is the strongly transcendental case; its complete proof is Lemma Z.11, with Definition Z.7 and Lemmas Z.8–Z.10. That proof passes to a minimal component and uses the integral polynomial-algebra case.

These lemmas apply over arbitrary rings with precisely the stated hypotheses. Their proofs, including localization in the presence of zero divisors and the passage to a minimal component, are written in that programme appendix.

**Lemma 2.1 (finite over one generator).** Suppose \(A\subset B\), \(A\) is integrally closed in \(B\), \(B\) is finite over \(A[b]\), and \(B/A\) is quasi-finite at \(\mathfrak q\). There is \(h\in A\setminus\mathfrak q\) with \(A_h=B_h\).

**Proof.** The first conductor fact says that the image of \(b\) in \(B/\sqrt J\) satisfies the second fact's condition over
\(A/(A\cap\sqrt J)\). Both quotient rings are reduced. The finite extension descends to their quotients. Thus this quotient extension has no quasi-finite point. If \(\mathfrak q\) contained \(J\), it would give just such a point: its fibre is a closed subspace of the original fibre, so the isolated point remains isolated and its residue extension remains finite. This contradiction proves \(J\not\subset\mathfrak q\).

Choose \(u\in J\setminus\mathfrak q\), giving \(A[b]_u=B_u\). The contracted point of \(\operatorname{Spec}A[b]\) is quasi-finite, because its local fibre ring agrees with the original one. The integral closure of \(A\) in \(A[b]\) is \(A\). Lemma 1.2 therefore gives \(a\in A\setminus\mathfrak q\) with \(A_a=A[b]_a\). In this ring write \(u=c/a^N\), with \(c\in A\). Its image is outside the chosen prime, so \(c\notin\mathfrak q\). Invert \(h=ac\). Then both \(a\) and \(u\) are units and the two equalities give \(A_h=B_h\). \(\square\)

**Proof of Theorem 1.1.** Replacing \(R\) by its image in \(B\) does not change its fibres or integral closure. Choose the least \(n\) such that \(B\) is finite over \(R[b_1,\ldots,b_n]\). For \(n=0\), all of \(B\) is integral over \(R\), so \(C=B\).

For \(n=1\), replace the base by \(C\). The extension remains quasi-finite at \(\mathfrak q\): its fibre is a subspace of the old fibre and \(B\) is still a finite-type \(C\)-algebra. The ring \(C\) is integrally closed in \(B\) by transitivity. Also \(B\) is finite over \(C[b_1]\). Lemma 2.1 applies and proves (1.1).

For \(n>1\), let \(D\subset B\) be the integral closure of \(R[b_1,\ldots,b_{n-1}]\) in \(B\). The same permanence argument makes \(B/D\) quasi-finite at \(\mathfrak q\), and \(B\) is finite over \(D[b_n]\). Lemma 2.1 supplies \(v\in D\setminus\mathfrak q\) with \(D_v=B_v\).

We cannot directly apply induction to \(D\): it need not be finitely generated over \(R\). Instead, choose finitely many numerators in \(D\) for a finite \(R\)-algebra generating list of \(B_v\). Let \(E\subset D\) be generated over \(R\) by those numerators, \(v\), and \(b_1,\ldots,b_{n-1}\). Then \(E_v=B_v\), and \(E\) is finite over \(R[b_1,\ldots,b_{n-1}]\), since its added generators are integral over that ring. At the contracted prime its local ring and local fibre ring agree with those of \(B\), so it is quasi-finite over \(R\).

Induction supplies the integral closure \(F\) of \(R\) in \(E\) and \(w\in F\setminus\mathfrak q\) with \(F_w=E_w\). Write \(v=c/w^M\) in this localization, with \(c\in F\setminus\mathfrak q\). Inverting \(g=wc\) makes \(v,w\) units, hence
\(F_g=E_g=B_g\). Since \(F\subset C\subset B\), it follows that \(C_g=B_g\). \(\square\)

The induction is [Stacks, Tag 00Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-main-theorem). The finite intermediate algebra is indispensable; integral closure itself need not be finite type.

## 3. From local equalities to finite affine completions

**Theorem 3.1.** The quasi-finite locus of a locally finite-type morphism is open.

**Proof.** Work on an affine chart \(R\to B\). At a quasi-finite prime use Theorem 1.1 to obtain \(C_g=B_g\). Choose finitely many integral numerators in \(C\) that, together with \(g^{-1}\), generate \(B_g\) over \(R\). Let \(D\subset C\) be the \(R\)-algebra generated by those numerators and \(g\). It is finite over \(R\), and \(D_g=B_g\). A finite map is quasi-finite, and restricting its source to an open preserves local quasi-finiteness. Thus all points of \(D(g)\subset\operatorname{Spec}B\) are quasi-finite over \(R\). These affine neighbourhoods prove openness and glue across source charts. \(\square\)

This proves [Stacks, Tag 01TI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-quasi-finite-points-open) by the algebraic route. It also supplies the open quasi-finite neighbourhood used in the previous dimension lesson without any reliance on its semicontinuity theorem.

**Theorem 3.2 (affine completion).** If \(\operatorname{Spec}B\to\operatorname{Spec}R\) is quasi-finite, then there is a finite \(R\)-subalgebra \(D\subset C\) for which

\[
\operatorname{Spec}B\hookrightarrow\operatorname{Spec}D
\longrightarrow\operatorname{Spec}R
\tag{3.1}
\]

is an open immersion followed by a finite morphism.

**Proof.** Choose the elements \(g\) of Theorem 1.1 at every point. Quasi-compactness gives a finite list \(g_1,\ldots,g_r\in C\) with \(C_{g_i}=B_{g_i}\) and \(\bigcup_iD_B(g_i)=\operatorname{Spec}B\). For each \(i\), select integral numerators generating \(B_{g_i}\) with \(g_i^{-1}\). The \(R\)-subalgebra \(D\) generated by all these numerators and all the \(g_i\) is finite. On each basic open,
\(D_{g_i}=B_{g_i}\). The preimage of \(D_D(g_i)\) is exactly \(D_B(g_i)\), and these maps are isomorphisms. They cover the source, so the map identifies it with the open \(\bigcup_iD_D(g_i)\). Its immersion is quasi-compact because there are finitely many such opens. \(\square\)

This fills the finite-subalgebra construction in [Stacks, Tag 00QB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-quasi-finite-open-integral-closure), or [Tag 03GU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-quasi-finite-affine) in scheme language. The omitted part of a finite completion is allowed to contain extra points or components; a completion is not unique.

## 4. The separated scheme theorem

For a quasi-compact and quasi-separated \(f:X\to S\), the algebra \(f_*\mathcal O_X\) is quasi-coherent. Its proof by finite affine equalizers and localization was given in the ample-sheaf lesson. Form the integral subalgebra \(\mathcal C\subset f_*\mathcal O_X\) and set

\[
S'=\operatorname{Spec}_S\mathcal C.
\tag{4.1}
\]

To justify gluing, integral closure commutes with localization in base elements. Given a monic equation in a localized algebra, clear its coefficient denominators by scaling the element by a sufficiently high power of the base element; a further power kills any equality that initially holds only after localization. The resulting element satisfies a monic equation before localization. Thus every localized integral element lies in the localized integral closure; the converse follows by localizing its equation. On an affine base open the sheaf \(\mathcal C\) is consequently the sheaf associated to the algebraic integral closure. This proves its quasi-coherence and the stalk description; compare [Stacks, Tag 035F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-integral-closure).

Relative Spec gives a canonical factorization \(X\to S'\to S\), whose second arrow is integral. This construction is called normalization of \(S\) in \(X\). It need not produce a normal scheme: for \(X=S\) and the identity map it gives \(S'=S\), whatever \(S\) is.

**Theorem 4.1 (relative integral completion).** Assume in addition that \(f:X\to S\) is finite type and separated, and write \(h:X\to S'\) for the canonical map. Let \(U\subset X\) be the quasi-finite locus of \(f\). Then \(V=h(U)\) is open in \(S'\), and

\[
h^{-1}(V)=U,
\qquad
h|_U:U\xrightarrow{\sim}V.
\]

If \(f\) is quasi-finite, \(h:X\to S'\) is a quasi-compact open immersion. No Noetherian, finite-presentation or reducedness hypothesis is needed.

**Proof.** Apply Affine descent, Zariski Main and recognition of spaces, Theorem D5.2. Its relative integral closure \(Z\) is precisely \(S'\): both use all integral elements in the same section algebras, glued by their localization identifications. Its morphism \(j\) is our evaluation map \(h\). The theorem assumes exactly that \(f\) is finite type and separated over an arbitrary scheme. It proves that \(j(U)\) is open, that its full inverse image is \(U\), and that the restricted map is an isomorphism. This gives the displayed assertions.

For the last assertion, every point is quasi-finite, so \(U=X\). We check quasi-compactness locally on \(S\). Over an affine open \(S_0\), the scheme \(X_{S_0}\) is quasi-compact because \(f\) is finite type, and \(S'_{S_0}\) is affine. Cover the open image of \(X_{S_0}\) by principal opens of \(S'_{S_0}\); quasi-compactness selects finitely many. Its intersection with any principal open of \(S'_{S_0}\) is therefore a finite union of principal opens and is quasi-compact. Thus \(X_{S_0}\hookrightarrow S'_{S_0}\) is a quasi-compact open immersion. The schemes \(S'_{S_0}\) cover \(S'\), proving the assertion globally. This is also the argument in the same lesson, Corollary D7.2. \(\square\)

The proof of Theorem D5.2 handles the nonaffine step explicitly. Sections D3.1–D3.3 split a finite clopen part of the source after an elementary étale neighbourhood; Sections D4.1–D4.3 prove that integral closure survives that base change; Lemma D5.1 descends the resulting isomorphism. The integral algebra on a finite part is its entire algebra of functions. On the complementary part it remains the integral closure. This produces a clopen component of the completed target whose **whole inverse image** is the chosen finite part. The descent therefore gives the inverse-image equality as well as the open immersion. The proofs of all three ingredients appear in that lesson before Theorem D5.2.

The full closure condition matters. For \(X=\operatorname{Spec}k\amalg\operatorname{Spec}k\) over \(S=\operatorname{Spec}k\), the full integral algebra is \(k\times k\), and \(h\) is the identity on the two points. Choosing the diagonal subalgebra \(k\) instead gives a map from two points to one, so an arbitrary integral subalgebra cannot replace \(\mathcal C\).

The open immersion \(U\to V\) need not be quasi-compact when only a portion of \(X\) is quasi-finite. The quasi-compactness conclusion above uses \(U=X\). If \(X\) is empty, its section algebra and integral algebra are zero, \(S'\) is empty, and every assertion still holds.


The affine version also follows directly from Theorem 1.1: union the opens \(D_C(g)\). Their inverse images are the corresponding isomorphic opens in \(X\). Conversely a point in this inverse image is quasi-finite, since its local fibre is a localization of a fibre of the integral morphism, whose primes have no strict inclusions. The finite-type fibre criterion therefore makes the point quasi-finite. This is [Stacks, Tag 03GT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-theorem-main-theorem).

### Finite subalgebras of an integral quasi-coherent algebra

**Lemma 4.1a.** Let \(S\) be a quasi-compact, quasi-separated scheme, and let \(\mathcal C\) be an integral quasi-coherent \(\mathcal O_S\)-algebra. The finite quasi-coherent \(\mathcal O_S\)-subalgebras of \(\mathcal C\), ordered by inclusion, form a nonempty directed system, and their union is \(\mathcal C\). Equivalently,
\[
\mathcal C=\varinjlim_{\mathcal D\subset\mathcal C,\ \mathcal D\text{ finite and quasi-coherent}}\mathcal D.
\]
Here finite means finite as an \(\mathcal O_S\)-module. Every subalgebra contains the image of the identity section. The map \(\mathcal O_S\to\mathcal C\) need not be injective. Neither \(S\) nor \(\mathcal C\) is assumed Noetherian, reduced, or of finite presentation.

We first give the extension argument needed on a base which is not affine. A prerequisite programme proof of this argument is AG-QC-03, Lemma 4.4. Its complete proof works on arbitrary qcqs schemes. We include the argument here as well, with an elementary direct-image calculation in degree zero, so that the extension step does not require a reference to an external proof.

The affine foundations used in the calculation are the complete proved results in *Quasi-coherent sheaves and concentrated scheme maps*, Lemma 1.1, Theorem 1.2, Proposition 1.3 and Lemma 1.4: exact localization, the affine module/sheaf equivalence, quasi-coherence of kernels, images, tensor products and colimits, and quasi-compactness of intersections of quasi-compact opens in a quasi-separated scheme.

**Extension step.** Suppose \(U\subset S\) is a quasi-compact open, \(\mathcal F\) is quasi-coherent on \(S\), and \(\mathcal G\subset\mathcal F|_U\) is quasi-coherent of finite type. Then some finite-type quasi-coherent subsheaf \(\mathcal H\subset\mathcal F\) has restriction exactly \(\mathcal G\) on \(U\).

**Proof.** Write \(j:U\hookrightarrow S\). We need that \(j_*\mathcal Q\) is quasi-coherent for every quasi-coherent module \(\mathcal Q\) on \(U\). Fix an affine \(V=\operatorname{Spec}A\subset S\). Its intersection with \(U\) is quasi-compact by quasi-separatedness, hence is a union of finitely many principal opens \(D(f_i)\subset V\). The sheaf condition computes
\[
N:=\Gamma(U\cap V,\mathcal Q)
=\ker\left(\prod_i\Gamma(D(f_i),\mathcal Q)
\longrightarrow\prod_{i,j}\Gamma(D(f_if_j),\mathcal Q)\right),
\]
where the arrow is the difference of the two restrictions. For \(a\in A\), the same finite cover cut by \(D(a)\) computes sections over \(U\cap D(a)\). The affine equivalence identifies every term of this new equalizer with the localization at \(a\) of its old term. Exact localization commutes with the finite products and kernel. It follows that
\[
\Gamma(U\cap D(a),\mathcal Q)=N_a.
\]
These identifications commute with restrictions, so \(j_*\mathcal Q|_V=\widetilde N\). They prove the required quasi-coherence. Empty intersections contribute the zero module and cause no exception.

Apply this to \(\mathcal Q=\mathcal F|_U/\mathcal G\), and define
\[
\mathcal K=\ker\left(\mathcal F\longrightarrow j_*(\mathcal F|_U/\mathcal G)\right).
\]
It is a quasi-coherent subsheaf of \(\mathcal F\), and \(\mathcal K|_U=\mathcal G\), since restriction of the direct image to \(U\) returns its original sheaf.

First assume \(S=\operatorname{Spec}A\). Write \(\mathcal K=\widetilde M\), and choose a finite principal cover \(U=\bigcup_iD(f_i)\). Each \(M_{f_i}\) is finitely generated, because its associated sheaf is \(\mathcal G|_{D(f_i)}\). Choose numerators in \(M\) of a finite generating list for every \(M_{f_i}\); denominators are units in that localization. The submodule \(M'\subset M\) generated by all these finitely many numerators satisfies \(M'_{f_i}=M_{f_i}\) for every \(i\). Thus \(\widetilde{M'}\subset\mathcal F\) is of finite type and restricts exactly to \(\mathcal G\) on \(U\).

For general \(S\), choose a finite affine cover \(V_1,\ldots,V_r\). Start with the given subsheaf on \(U\), and successively enlarge this open by adjoining the \(V_i\). At each step the intersection of the already treated quasi-compact open \(W\) with \(V_i\) is quasi-compact. The affine construction just proved extends the existing subsheaf on \(W\cap V_i\) to a finite-type subsheaf of \(\mathcal F|_{V_i}\), with exactly the same restriction on the intersection. The two subsheaves therefore glue as subsheaves of \(\mathcal F|_{W\cup V_i}\). Quasi-coherence and finite type are local properties, so the glued subsheaf has both. After the finitely many steps it is the required \(\mathcal H\) on \(S\). \(\square\)

Consequently every quasi-coherent \(\mathcal F\) on \(S\) is the directed union of its finite-type quasi-coherent subsheaves. In fact, a section over an affine open belongs to the cyclic subsheaf it generates there; the extension step puts it in a global finite-type subsheaf. Such sections represent every stalk element. Sums of two finite-type quasi-coherent subsheaves are again quasi-coherent of finite type, which gives directedness.

**Proof of the algebra lemma.** Let \(\mathcal F\subset\mathcal C\) be a finite-type quasi-coherent submodule. Form the subalgebra generated by it and by the identity:
\[
\mathcal D(\mathcal F)
=\operatorname{im}\left(\operatorname{Sym}_{\mathcal O_S}(\mathcal F)
\longrightarrow\mathcal C\right).
\]
It is quasi-coherent. Indeed, on any affine chart the symmetric algebra is the usual symmetric algebra of the module of sections, its formation commutes with localization, and its image is the sheaf associated to the image module. The degree-zero part supplies the identity. On an affine chart \(V=\operatorname{Spec}A\), choose module generators \(c_1,\ldots,c_m\) for \(\mathcal F(V)\). The sections of this image algebra are
\[
\mathcal D(\mathcal F)(V)=A[c_1,\ldots,c_m]\subset\mathcal C(V).
\]
Every \(c_i\) satisfies a monic equation over \(A\), because \(\mathcal C\) is integral. If the equation has degree \(e_i\geq1\), repeated replacement of \(c_i^{e_i}\) expresses every polynomial in the \(c_i\) as an \(A\)-linear combination of
\[
c_1^{a_1}\cdots c_m^{a_m},\qquad 0\leq a_i<e_i.
\]
There are finitely many such monomials. This proves finiteness on every affine chart, and therefore finiteness of \(\mathcal D(\mathcal F)\) as a sheaf of modules. When \(m=0\), the list consists of the identity alone; its image still generates the algebra.

The extension result applied to the underlying module of \(\mathcal C\) shows that every stalk element belongs to some \(\mathcal F\), hence to a finite subalgebra \(\mathcal D(\mathcal F)\). Therefore these finite subalgebras exhaust \(\mathcal C\).

The collection of all finite quasi-coherent subalgebras is directed too. Given two, \(\mathcal D_1\) and \(\mathcal D_2\), the image of multiplication
\[
\mathcal D_1\otimes_{\mathcal O_S}\mathcal D_2\longrightarrow\mathcal C
\]
is a subalgebra containing both: the tensor product is an algebra, multiplication is an algebra homomorphism, and each subalgebra is recovered by multiplying by the other's identity. On affine charts its module is an image of a tensor product of two finite modules, so it is finite. It is quasi-coherent by the affine image calculation. This gives a common upper bound. The image of \(\mathcal O_S\) provides a first member, so the system is nonempty. Finally, directed sheaf colimits have the directed module colimit on affine charts, and equality on all stalks identifies this colimit with \(\mathcal C\). \(\square\)

This proves exactly the finite-subalgebra assertion in [Stacks Project, Tag 0817](https://stacks.math.columbia.edu/tag/0817), part (1). It does not assert that the finite subalgebras are finitely presented; that additional assertion is unnecessary for finite factorization.

### The finite-type closed-immersion step

**Lemma 4.1b.** Let \(Z=\varprojlim_i Z_i\) be a directed inverse limit of schemes over a scheme \(S\), with affine transition maps and quasi-compact stages. Suppose \(Y\to Z\) is a closed immersion over \(S\), and \(Y\to S\) is locally of finite type. Then \(Y\to Z_i\) is a closed immersion for all sufficiently large \(i\). No finite-presentation hypothesis is needed.

**Proof.** Fix a stage \(i_0\). Choose a finite affine cover \(W_1,\ldots,W_r\) of \(Z_{i_0}\) such that each \(W_a\) maps into an affine \(V_a=\operatorname{Spec}R_a\subset S\). Such a cover exists by continuity, the affine basis, and quasi-compactness. For \(i\geq i_0\), let \(W_{a,i}\subset Z_i\) be its inverse image. All are affine, since the transitions are affine. The inverse image \(W_a^\infty\subset Z\) is affine as well, and
\[
A_a:=\Gamma(W_a^\infty,\mathcal O_Z)
=\varinjlim_{i\geq i_0}A_{a,i},\qquad
A_{a,i}:=\Gamma(W_{a,i},\mathcal O_{Z_i}).
\]
These limit statements have a complete prerequisite programme proof in AG-MO-03, Theorem 1.1.

The inverse image \(Y_a\) of \(W_a^\infty\) in \(Y\) is a closed subscheme of this affine, hence affine; write \(Y_a=\operatorname{Spec}B_a\). The closed immersion gives a surjection \(A_a\twoheadrightarrow B_a\). Moreover \(B_a\) is a finite-type \(R_a\)-algebra, because \(Y\to S\) is locally of finite type. The statement on all compatible affine charts is proved in AG-MO-02, Theorem 3.1, from its localization and finite-cover patching argument in Lemma 2.1.

Choose finitely many \(R_a\)-algebra generators \(b_{a,1},\ldots,b_{a,n_a}\) of \(B_a\). Surjectivity supplies a preimage of each in \(A_a\), and every preimage is represented in some \(A_{a,i}\). At one common later stage all these representatives exist. Then \(A_{a,i}\to B_a\) contains the base image and every chosen algebra generator in its image, so it is surjective. There are finitely many \(a\), allowing one stage for all charts. The inverse image of \(W_{a,i}\) under \(Y\to Z_i\) is exactly \(Y_a\), by composition of the projection maps. Thus the morphism is a closed immersion on an affine cover of its target, and is a closed immersion globally. The same generators remain in the image at every later stage. \(\square\)

The precise freely accessible comparison is [Stacks Project, Tag 081B](https://stacks.math.columbia.edu/tag/081B), part (1). This argument descends surjectivity onto a fixed finite-type algebra; it does not descend an arbitrary map out of an algebra with infinitely many defining relations.


**Theorem 4.2 (finite factorization).** If \(f:X\to S\) is quasi-finite and separated and \(S\) is quasi-compact and quasi-separated, it factors as

\[
X\xrightarrow{j}T\xrightarrow{\pi}S,
\qquad j\text{ a quasi-compact open immersion},\quad\pi\text{ finite}.
\tag{4.2}
\]

**Proof.** Theorem 4.1 identifies \(X\) with a quasi-compact open of \(S'=\operatorname{Spec}_S\mathcal C\). By Lemma 4.1a write \(\mathcal C=\varinjlim_i\mathcal C_i\), where the \(\mathcal C_i\) are finite quasi-coherent subalgebras. Put \(T_i=\operatorname{Spec}_S\mathcal C_i\). Then \(T_i\to S\) is finite, its transition maps are affine, and their limit is \(S'\), by the affine-chart colimit calculation in the limits lesson. Each \(T_i\) is qcqs, since it is affine over the qcqs base.

Limits of schemes and Noetherian approximation, Lemma 2.1 descends the quasi-compact open \(X\subset S'\) to a quasi-compact open \(V_{i_0}\subset T_{i_0}\). At later stages use its inverse images \(V_i\). These have affine transition maps and limit \(X\). Apply Lemma 4.1b to the identity closed immersion \(X\to\varprojlim_iV_i=X\), using that \(X\to S\) is finite type. At a sufficiently large stage it gives a closed immersion \(X\to V_i\). Thus \(X\to T_i\) is a quasi-compact immersion. No finite-presentation assumption on \(X\to S\) has been used.

Take its scheme-theoretic closure \(T\subset T_i\). Explicitly, if \(a:X\to T_i\) denotes this immersion, the ideal
\[
\mathcal I=\ker(\mathcal O_{T_i}\longrightarrow a_*\mathcal O_X)
\]
is quasi-coherent: a quasi-compact immersion is separated and hence qcqs, so the finite-affine-equalizer direct-image calculation applies. Over \(V_i\), this kernel defines the closed subscheme \(X\), so \(T\cap V_i=X\). Consequently \(X\to T\) is an open immersion. It is quasi-compact, since inverse images of quasi-compact opens of \(T\) are the corresponding inverse images for the quasi-compact immersion into \(T_i\). The morphism \(T\to T_i\) is a closed immersion, hence finite even when its ideal is not finitely generated. Its composite with the finite map \(T_i\to S\) is finite. This proves (4.2). \(\square\)

This is [Stacks, Tag 05K0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-pass-through-finite). Theorem 4.1 also shows over an arbitrary base that a quasi-finite separated morphism is **quasi-affine**: over each affine base open its source is a quasi-compact open subscheme of the affine integral completion. See [Tag 02LR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-quasi-finite-separated-quasi-affine).

## 5. Properness and normality

**Theorem 5.1.** A proper quasi-finite morphism is finite, over an arbitrary base.

**Proof.** Finiteness is local on the target, so restrict to an affine base open and apply Theorem 4.2. In (4.2), \(j\) is proper: its graph is closed because \(T\to S\) is separated, and projection from \(X\times_S T\) is proper by base change of \(X\to S\). The proper open immersion has closed image, hence identifies \(X\) with an open and closed subscheme of \(T\). It is a closed immersion and therefore finite. Composing with \(T\to S\) proves finiteness. \(\square\)

No Noetherian or finite-presentation assumption is required. Equivalently a proper map with finite fibres is finite, by the finite-fibre quasi-finiteness test. This stronger version is [Stacks, Tag 02LS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-characterize-finite).

An integral scheme is **normal** if each local ring is integrally closed in its fraction field. A dominant morphism of integral schemes is **birational** here when it identifies their function fields.

**Theorem 5.2.** A quasi-finite separated birational morphism \(X\to S\) of integral schemes with normal target is an open immersion. In particular this holds for integral Noetherian schemes.

**Proof.** Identify both function fields with \(K\). On every nonempty target open, functions on its inverse image embed into \(K\), since that inverse image is a nonempty open of integral \(X\). Thus the stalks of \(f_*\mathcal O_X\) embed into \(K\). An element of its integral subalgebra \(\mathcal C_s\) is integral over \(\mathcal O_{S,s}\) and lies in \(K\), so normality puts it in \(\mathcal O_{S,s}\). The reverse inclusion is automatic. Therefore \(\mathcal C=\mathcal O_S\), and Theorem 4.1 identifies \(X\to S'=S\) with an open immersion. \(\square\)

For comparison, an integral birational morphism to an integral normal scheme is an isomorphism: on an affine chart its integral algebra is a subalgebra of the same fraction field and must equal the integrally closed base algebra. This is [Stacks, Tag 0AB1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-birational-over-normal). Separatedness in Theorem 5.2 cannot be discarded: the doubled affine line maps quasi-finitely and birationally to the affine line, but has two origins and is not an open immersion.

## 6. Open parts and a singular target

The inclusion \(\mathbb A^1\setminus\{0\}\to\mathbb A^1\) has (4.2) with \(T=\mathbb A^1\) and \(\pi\) the identity. Its fibres are finite, but its image is not closed, so it is not finite. This is the simplest distinction between a finite map and an open part of one.

For a less trivial example take \(\operatorname{char}k\ne2\) and the integral node

\[
N=\operatorname{Spec}k[x,y]/(y^2-x^2(x+1)).
\tag{6.1}
\]

The map from \(\mathbb A^1_t\) given by

\[
x=t^2-1,\qquad y=t(t^2-1)
\tag{6.2}
\]

is finite: \(t\) satisfies \(t^2=x+1\). It is birational because \(t=y/x\) off \(x=0\); there it is an isomorphism. The node has two inverse images, \(t=1\) and \(t=-1\). These formulas also identify \(k[t]\) as the integral closure: it is a polynomial normal domain with the same fraction field, integral over the nodal ring. Normalization is studied systematically in the next lesson.

Remove \(t=-1\). The remaining \(U=D(t+1)\) maps quasi-finitely, separatedly and birationally to \(N\), and is bijective on points: away from the node the original map is an isomorphism; over the node only \(t=1\) remains. It is not an open immersion. Such an immersion, being surjective, would be an isomorphism, but the source is normal and the target is not. Indeed \(t\) is integral and is not regular at the node. If \(t=r/s\) with \(r,s\) in the nodal ring and \(s\) nonvanishing there, then \(r(1)=r(-1)\) and \(s(1)=s(-1)\ne0\), whereas \(t(1)=1\) and \(t(-1)=-1\). This is impossible. The missing hypothesis of Theorem 5.2 is normality.

## 7. Exercises with solutions

**Exercise 7.1 (medium).** Deduce proper plus quasi-finite implies finite from the finite factorization, keeping track of why its open immersion becomes closed.

**Solution.** Work over an affine base so Theorem 4.2 applies. The graph factorization makes \(j:X\to T\) proper, since \(X\to S\) is proper and \(T\to S\) is separated. Properness makes its image closed; the open immersion already gives the open subscheme structure. Its image is therefore open and closed and its inclusion is a closed immersion. Both this map and \(T\to S\) are finite, so their composite is finite. The conclusion glues on the target.

**Exercise 7.2 (medium).** Verify the node example scheme-theoretically, and explain why deleting one inverse image does not restore the normal-target theorem.

**Solution.** The polynomial \(x+1\) is not a square in \(k(x)\), so \(y^2-x^2(x+1)\) is irreducible and the nodal coordinate ring is a domain. After inverting \(x\), substitution into (6.2) is an isomorphism, with inverse parameter \(t=y/x\). Its kernel before localization is therefore killed by a power of \(x\), and is zero because the nodal ring is a domain. Thus it identifies that ring with the indicated subring of \(k[t]\); both fraction fields are \(k(t)\). Its singular fibre algebra under normalization is \(k[t]/(t^2-1)\cong k\times k\). Localizing at \(t+1\) removes the \(-1\) factor and leaves one reduced point. The restriction of a finite map to this quasi-compact open is quasi-finite and separated. The target local ring still lacks the integral element \(t\), by the two-value argument in Section 6. Deleting a source point cannot make that target ring normal.

**Exercise 7.3 (medium).** Show a quasi-finite separated morphism is quasi-affine, without requiring the entire base to be quasi-compact.

**Solution.** On an arbitrary affine base open, the restricted source is quasi-compact, because the morphism is of finite type. Theorem 4.1 embeds it as a quasi-compact open of an affine integral completion. This is the target-local definition of a quasi-affine morphism. These local assertions suffice; no finite cover of the entire base was chosen.

**Exercise 7.4 (medium).** Prove that a bijective birational morphism of varieties onto a normal variety is an isomorphism. Varieties here are integral separated finite-type schemes over a field.

**Solution.** A morphism between these varieties is finite type: on affine charts its finitely many algebra generators over the field also generate over the target algebra, and the Noetherian source ensures quasi-compactness. It is separated, since both varieties are separated over the field and separatedness cancellation applies. Bijectivity gives fibres with one underlying point, hence finite fibres; the finite-type fibre test makes it quasi-finite. Theorem 5.2 makes it an open immersion. Its surjectivity then makes the image the whole target, proving it is an isomorphism. Bijectivity alone would not suffice: in positive characteristic a Frobenius map can be bijective on points without identifying function fields.

**Exercise 7.5 (hard).** Prove algebraic Zariski Main Theorem for an algebra generated by one element, explicitly treating the possibility that a leading coefficient vanishes at the chosen point.

**Solution.** Choose a polynomial relation having a coefficient outside the contracted base prime; otherwise the fibre is a polynomial line and has no quasi-finite point. Work in the integral closure \(C\). For a relation of degree \(m\), equation (1.3) puts the leading coefficient times the generator in \(C\). If that coefficient is outside the prime, invert it and obtain the whole algebra from \(C\). If it is inside the prime, absorb its product with the generator into the next coefficient. This reduces the degree and preserves the existence of a coefficient outside the prime, because the absorbed term is in the prime. Repeat; degree zero with a coefficient outside the prime is contradictory. The process must therefore terminate with the required invertible leading coefficient. Exactness of localization proves the equality of the two localized rings even when zero divisors or nilpotents are present.

## References and proof providers

The algebraic argument uses the conductor and induction approach of the freely accessible Stacks Project. Its conductor inputs are proved in The theorem on formal functions, Appendix Z, Lemmas Z.6 and Z.11; the monogenic calculation and finite-generator induction are proved in Sections 1–2 here. The nonaffine separated completion uses the complete prerequisite programme proof in Affine descent, Zariski Main and recognition of spaces, Theorem D5.2, with its preceding finite-piece, integral-closure base-change and descent proofs. The finite-subalgebra and finite-type closure arguments are proved here in Lemmas 4.1a–4.1b. Linked Stacks material retains GNU FDL 1.2; it is not reproduced here.

T. J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 7, Section 4, treats quasi-finite algebras and Zariski's Main Theorem by the algebraic conductor approach. Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), draft of 27 July 2024, §28.5, treats the proper-map and normal-target applications. Its alternative route through formal functions is not needed in the algebraic proof above.
