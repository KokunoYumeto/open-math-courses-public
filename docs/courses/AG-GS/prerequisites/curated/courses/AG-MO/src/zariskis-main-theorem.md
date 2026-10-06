# Zariski's Main Theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A quasi-finite map has finite fibres, but it can omit points that would be present in a finite map. Zariski's Main Theorem makes this precise: with separatedness and a suitable base, it is an open part of a finite map. The algebraic theorem first finds that open part inside an integral closure. Finite generation then lets us replace the possibly infinite integral closure by a finite algebra.

We use the fibre tests of Quasi-finite morphisms and Chevalley's theorem, the local dimension convention of Dimension of fibres, Affine, integral and finite morphisms, and the integral-extension results of Integral extensions: lying over, going up and going down. A quasi-finite morphism is of finite type and is quasi-finite at every point. Locally quasi-finite means locally of finite type with every point isolated in its fibre. An integral closure in an algebra refers to elements integral over the image of the base ring; the base map need not be injective.

## 1. The algebraic neighbourhood

**Theorem 1.1 (algebraic Zariski Main Theorem).** Let \(R\to B\) be finite type and let \(C\subset B\) consist of the elements integral over \(R\). If \(\mathfrak q\in\operatorname{Spec}B\) is a quasi-finite point over \(R\), there is \(g\in C\setminus\mathfrak q\) such that

\[
C_g=B_g.
\tag{1.1}
\]

Equality means equality through the natural localization map. In particular a neighbourhood of \(\mathfrak q\) maps isomorphically to an open of \(\operatorname{Spec}C\). We will prove this by induction, first explaining the one-variable calculation. The two technical conductor facts needed for a finite extension of that calculation have exact complete open proofs identified in Section 2.

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

Here are the two open algebraic proof ingredients we use. Suppose \(A\subset B\), \(A\) is integrally closed in \(B\), and \(B\) is finite over \(A[b]\). Let \(J\) be the conductor from \(B\) to \(A[b]\).

* If \(u\sum_i a_i b^i\in\sqrt J\), with \(u\in B\) and \(a_i\in A\), then every \(ua_i\in\sqrt J\). The full proof is Stacks, Tag 00PY, including its leading-coefficient argument.
* If reduced rings \(A_0\subset B_0\) contain an element \(b_0\) such that \(u\sum_i a_i b_0^i=0\) always implies every \(ua_i=0\), and \(B_0\) is finite over \(A_0[b_0]\), then \(B_0/A_0\) is quasi-finite at no point. This is the strongly transcendental case; its complete proof is Stacks, Tag 00Q2. That proof passes to a minimal component and uses the integral polynomial-algebra case.

These are exact supporting proof providers, valid over arbitrary rings under the conditions just stated. Their open source retains GNU FDL 1.2; no source expression is reproduced here. They are the technical part of the conductor step, rather than a reference to a book for the main theorem.

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

**Theorem 4.1 (relative integral completion).** For a separated finite-type \(f:X\to S\), there is an open \(V\subset S'\) whose inverse image is exactly the quasi-finite locus of \(f\), and this inverse image maps isomorphically to \(V\). In particular, if \(f\) is quasi-finite, \(X\to S'\) is a quasi-compact open immersion.

The exact complete open proof, including the nonaffine gluing, is [Stacks, Tag 03GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-finite-type-separated). It supplies this general scheme theorem. Its crucial separation step is the full [finite-piece lemma, Tag 02LN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-splits-off-quasi-finite-part-technical): near a chosen isolated fibre point, an elementary étale neighbourhood of the base makes a finite piece of the source open and closed. Such a neighbourhood is an étale map with a distinguished point having the original base residue field. The finite piece is closed because it is proper inside a separated scheme; this is where separatedness enters. Integral closure commutes with these étale base changes. On the finite piece normalization is the identity, and the resulting local isomorphism descends to the original base. The proof at Tag 03GW includes this base-change and descent argument, so ordinary affine chart gluing is not being asserted as a substitute for it. The linked proof and its supporting treatment are openly licensed under GNU FDL 1.2.

The affine version also follows directly from Theorem 1.1: union the opens \(D_C(g)\). Their inverse images are the corresponding isomorphic opens in \(X\). Conversely a point in this inverse image is quasi-finite, since its local fibre agrees with a fibre of an integral morphism, whose points have no proper generalizations. This is [Stacks, Tag 03GT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-theorem-main-theorem).

**Theorem 4.2 (finite factorization).** If \(f:X\to S\) is quasi-finite and separated and \(S\) is quasi-compact and quasi-separated, it factors as

\[
X\xrightarrow{j}T\xrightarrow{\pi}S,
\qquad j\text{ a quasi-compact open immersion},\quad\pi\text{ finite}.
\tag{4.2}
\]

**Proof.** By Theorem 4.1, \(X\) is a quasi-compact open of \(S'\). The integral algebra \(\mathcal C\) is a directed union of finite quasi-coherent subalgebras \(\mathcal C_i\), by the complete open subalgebra theorem [Stacks, Tag 0817](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-integral-algebra-directed-colimit-finite). Its hypotheses are precisely the qcqs base and integral quasi-coherent algebra here. Put \(T_i=\operatorname{Spec}_S\mathcal C_i\). These are finite over \(S\), and \(S'=\varprojlim T_i\).

The open-descent theorem of Limits and Noetherian approximation descends \(X\subset S'\) to a quasi-compact open \(V_i\subset T_i\). At later stages take its inverse image. Their limit is \(X\). At a sufficiently late stage, \(X\to V_i\) is a closed immersion. The finite-type mechanism for this assertion is explicit: cover a fixed stage by finitely many affines mapping to affine opens of \(S\); their inverse images in \(X\) are affine. On each chart the limit ring maps onto the source ring, which is a finite-type algebra over the base. Finitely many algebra generators therefore already occur at one stage, making that stage's map surjective. One common late stage works on all charts. No finite-presentation hypothesis on \(X\) is needed. This is also the complete proof at [Stacks, Tag 081B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-finite-type-eventually-closed).

Thus \(X\to T_i\) is a quasi-compact immersion. Take its scheme-theoretic closure \(T\) in \(T_i\). On \(V_i\) the closure equals the already closed \(X\), so \(X\) is an open subscheme of \(T\). The closure is a closed subscheme of \(T_i\), hence finite over \(S\). Its open immersion is quasi-compact: \(X\to S\) is quasi-compact and \(T\to S\) is separated, so quasi-compactness cancellation applies. This gives (4.2). \(\square\)

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

The algebraic proof follows the conductor and induction route of the Stacks project, read in the AI Integrated Stacks Project edition, with exact full open supporting proofs at Tags 00PY and 00Q2. The nonaffine separated completion has the complete open provider at Tag 03GW, including its finite-piece and descent argument; the finite subalgebra theorem is at Tag 0817. These precise providers, with their hypotheses and use, are integrated above. Linked Stacks material retains GNU FDL 1.2; it is not reproduced here.

T. J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 7, Section 4, treats quasi-finite algebras and Zariski's Main Theorem by the algebraic conductor approach. Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), draft of 27 July 2024, §28.5, treats the proper-map and normal-target applications. Its alternative route through formal functions is not needed in the algebraic proof above.
