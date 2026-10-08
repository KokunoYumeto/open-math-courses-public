# Étale neighbourhoods, henselization and quasi-finite morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the subsections on henselian pairs and on universal homeomorphisms in Section 5 by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Original text: public domain (CC0). Sources are listed at the end.*

A Zariski neighbourhood may retain several algebraic branches that meet at a point. An étale neighbourhood permits a simple root to be chosen while preserving the local geometry. Taking all such choices produces the henselization. Allowing finite separable extensions of the residue field produces the strict henselization. These constructions also explain why a quasi-finite branch can be isolated as a finite scheme after an étale change of base. We then pass from a henselian local ring to a henselian pair and prove that every finite étale algebra, including all its morphisms, is determined by reduction along the pair ideal. Finally, integral descent extends the preceding thickening theorem to every universal homeomorphism.

We use **Étale morphisms and their local structure** and **Infinitesimal lifting and the invariance of étale morphisms under thickenings**. The algebraic prerequisites are **Henselian local rings and henselization** and **Completion**; the geometric prerequisite is **Zariski's Main Theorem**. We specify the imported statements below. No Noetherian, separatedness or finite-presentation hypothesis is imposed unless stated. A finite algebra means a finite module, whereas a finite type algebra means finitely many algebra generators.

## 1. Which neighbourhood categories are cofiltered?

Let \(s\in S\), and put \(k=\kappa(s)\). An **étale neighbourhood** is an étale morphism \(U\to S\) with a point \(u\) over \(s\). Morphisms of neighbourhoods are \(S\)-morphisms preserving the selected point. It is **elementary** if the canonical map \(k\to\kappa(u)\) is an isomorphism. Its residue extension is always finite separable [Stacks, Tag [02LE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-definition-etale-neighbourhood)].

Fix a geometric point \(\bar s:\operatorname{Spec}\Omega\to S\), with \(\Omega\) algebraically closed. A neighbourhood of \(\bar s\) carries a lift \(\bar u:\operatorname{Spec}\Omega\to U\); its morphisms preserve this lift. Write \(k^{\mathrm{sep}}\subset\Omega\) for the elements separable algebraic over \(k\). Equivalently the marking specifies an embedding \(\kappa(u)\hookrightarrow k^{\mathrm{sep}}\).

**Lemma 1.1 (prescribing the residue field).** Every finite separable extension \(L/k\) occurs as the residue field of an étale neighbourhood of \(s\).

**Proof.** Work in an affine neighbourhood \(\operatorname{Spec}R\) of \(s\), represented by \(\mathfrak p\). Choose a primitive element of \(L/k\), with monic minimal polynomial \(\bar f\in k[T]\). Its finitely many coefficients belong to a localization \((R/\mathfrak p)_r\), for some \(r\notin\mathfrak p\). Lift them to \(R_r\), retaining the leading coefficient 1, and let

\[
B=\bigl(R_r[T]/(f)\bigr)_{f'}.
\tag{1.1}
\]

This is standard étale. The fibre contains the point with field \(k[T]/(\bar f)=L\), since separability makes \(\bar f'\) nonzero there. Its spectrum, followed by the open immersion \(\operatorname{Spec}R_r\to S\), is the required neighbourhood. ∎ [Stacks, Tag [02LF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-realize-prescribed-residue-field-extension-etale)]

**Proposition 1.2.** The category of elementary étale neighbourhoods of \(s\), and the category of neighbourhoods of \(\bar s\), are cofiltered.

**Proof.** The identity neighbourhood makes both categories nonempty. For two elementary neighbourhoods, the product \(U_1\times_S U_2\) has a selected point corresponding to

\[
\kappa(u_1)\otimes_k\kappa(u_2)=k;
\]

it gives an elementary common refinement. For geometric neighbourhoods, the two lifts give a lift to the product, which is a common refinement with its marking.

Let \(a,b\colon U\rightrightarrows V\) be parallel arrows. Since \(V\to S\) is étale, its diagonal is an open immersion. The inverse image of that diagonal under \((a,b)\) is therefore an open subscheme \(E\subset U\), and on \(E\) the arrows agree as scheme morphisms. In the elementary case their residue-field maps are both the identity of \(k\), so \(u\in E\). In the geometric case they agree on the specified lift, so that lift factors through \(E\). The open inclusion \(E\to U\) equalizes the arrows and preserves the required marking. These are the three cofilteredness conditions. ∎ [Stacks, Tags [057A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-neighbourhoods-not-quite-filtered), [057B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-elementary-etale-neighbourhoods)]

The residue marking matters. General pointed neighbourhoods need not be cofiltered: over \(\operatorname{Spec}\mathbf F_q\), take \(U=\operatorname{Spec}\mathbf F_{q^2}\). Its identity and its \(q\)-power automorphism preserve its single point. An equalizing nonempty refinement would induce an embedding \(\mathbf F_{q^2}\hookrightarrow\kappa(v)\) that equates this automorphism with the identity, which injectivity forbids. General pointed neighbourhoods have common refinements, and parallel arrows with the same residue-field map can be equalized by the proof above.

We may always refine to an affine neighbourhood of the selected point lying over a fixed affine open of \(S\). An affine open inclusion preserves the marking. Thus these affine neighbourhoods suffice for all the colimits used below.

## 2. Henselian rings through their sections

A local ring \((A,\mathfrak m,k)\) is **henselian** if every simple root \(\alpha\in k\) of the reduction of a monic polynomial \(F\in A[T]\) lifts to a root in \(A\). It is **strictly henselian** if in addition \(k\) is separably closed [Stacks, Tags [03QF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-definition-henselian), [03QK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-definition-strictly-henselian)].

We import two equivalent algebraic descriptions from **Henselian local rings and henselization**. Henselianity is equivalent to lifting factorizations of monic polynomials into coprime monic factors, and to every finite \(A\)-algebra being a finite product of local rings. Each such local factor is henselian [Stacks, Tags [04GG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-henselian), [04GH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-over-henselian)]. Complete local rings are henselian, as proved in **Completion** [Stacks, Tags [04GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-complete-henselian), [03QG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-hensel)]. These algebraic results do not assert that a henselian ring is complete.

**Theorem 2.1 (geometric criterion).** The ring \(A\) is henselian if and only if every étale neighbourhood \((U,u)\) of its closed point with \(\kappa(u)=k\) has a section

\[
\sigma:\operatorname{Spec}A\longrightarrow U
\tag{2.1}
\]

through \(u\). The section through that specified point is unique. It is enough to test affine étale neighbourhoods.

**Proof.** Suppose first that \(A\) is henselian. The monic local structure theorem permits an affine open around \(u\) of the form

\[
\operatorname{Spec}\bigl(A[T]/(F)\bigr)_g,
\tag{2.2}
\]

with \(F\) monic and \(F'\) invertible. An open neighbourhood of the closed point of \(\operatorname{Spec}A\) is the entire spectrum, so no shrinking of this base is needed. The point \(u\) gives a simple root \(\alpha\in k\) of \(\bar F\), with \(\bar g(\alpha)\ne0\). A lifted root \(a\in A\) satisfies \(g(a)\notin\mathfrak m\), hence \(g(a)\) is a unit. Evaluation at \(a\) defines (2.1).

Two sections through \(u\) coincide on the closed point, including its residue-field map. Their equalizer is open because the diagonal of \(U/A\) is open. It contains the closed point, hence is all of \(\operatorname{Spec}A\). This proves uniqueness even when \(U\) is not separated.

Conversely, given monic \(F\) and a simple residue root \(\alpha\), the algebra \((A[T]/(F))_{F'}\) is étale and has the rational point specified by \(\alpha\). A section through it is an evaluation homomorphism whose value on \(T\) is the required lifted root. Thus \(A\) is henselian. ∎ [Stacks, Tags [03QH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-henselian), [04GG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-henselian)]

Sometimes the criterion says only that the étale algebra admits a section. Applied to every such algebra, this is equivalent: first localize to remove all the other points of its finite closed fibre. Any section then passes through the selected point. For an individual neighbourhood the chosen-point condition must still be kept.

For example, \(\mathbf Z_p\) is henselian. A simple root modulo \(p\) has a unique lift there. The algebraic criterion makes the same conclusion available over henselian rings that are not complete and over rings that are not Noetherian.

## 3. The two colimits of local choices

For a point \(s\) of an arbitrary scheme the colimit maps come from restriction of functions. Therefore they run over the **opposite** of the neighbourhood category:

\[
\mathcal O_{S,s}^{h}
\cong\underset{(U,u)\ \mathrm{elementary}}{\operatorname{colim}}
\Gamma(U,\mathcal O_U),
\qquad
\mathcal O_{S,s}^{sh}
\cong\underset{(U,\bar u)}{\operatorname{colim}}
\Gamma(U,\mathcal O_U).
\tag{3.1}
\]

In the second formula the separable closure is chosen as above. The algebraic local colimits and their universal properties are imported from Henselian local rings and henselization, Theorems 4.2 and 5.1. We state them with our markings and prove their comparison with geometric neighbourhoods.

**Theorem 3.1 (elementary colimit).** For a local ring \((A,\mathfrak m,k)\), the filtered colimit \(H\) of étale \(A\)-algebras \(B\) marked by a prime \(\mathfrak q\) over \(\mathfrak m\) with residue field \(k\) is local and henselian. Its maximal ideal is \(\mathfrak mH\), its residue field is \(k\), and every local map from \(A\) to a henselian local ring factors uniquely through a local map from \(H\). Consequently \(H=A^h\).

**Algebraic import.** A marking with residue field \(k\) is precisely the evaluation \(B\to k\) used in Henselian local rings and henselization, Theorem 4.2. That theorem proves locality, the maximal ideal and residue-field assertions, henselianity and the stated universal property over any local base ring. Thus its algebraic colimit is the \(H\) in this statement. The geometric identification remains to be proved below. [Stacks, Tags [04GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-henselization), [05KS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-describe-henselization)]

To pass from this local-ring result to the first formula in (3.1), put \(A=R_{\mathfrak p}=\mathcal O_{S,s}\) in an affine neighbourhood \(\operatorname{Spec}R\). After a principal refinement at its selected point, a marked étale algebra over \(A\) has a square Jacobian chart and spreads to an étale algebra over \(R_r\) for some \(r\notin\mathfrak p\): take a finite square Jacobian presentation from the preceding lesson, then clear the finitely many denominators in its equations and the identity expressing its determinant as a unit. Its marked fibre point spreads as well because the fibre remains over \(k\). Thus every local stage occurs geometrically. Conversely a geometric affine stage gives an étale algebra after tensoring with \(A\), and each denominator outside its selected prime can be inverted by a principal open refinement. Every function germ needed for the local construction occurs after such a refinement. The two systems therefore give inverse maps on their colimits. Affine refinements from Section 1 give the same answer if non-affine neighbourhoods are included.

**Theorem 3.2 (geometric colimit).** Using markings \(\kappa(\mathfrak q)\hookrightarrow k^{\mathrm{sep}}\) instead, the colimit \(H_{\mathrm{geom}}\) is \(A^{sh}\) with this chosen separable closure. It is henselian, local with maximal ideal \(\mathfrak mH_{\mathrm{geom}}\), and has residue field \(k^{\mathrm{sep}}\). A local map \(A\to C\) into a strictly henselian ring factors uniquely through it after a compatible embedding \(k^{\mathrm{sep}}\hookrightarrow\kappa(C)\) has been specified.

**Algebraic import and geometric comparison.** A prime together with a residue embedding into \(k^{\mathrm{sep}}\) is exactly an evaluation \(B\to k^{\mathrm{sep}}\). The algebraic colimit and all stated local-ring properties, including uniqueness with the specified embedding, are Henselian local rings and henselization, Theorem 5.1.

For the second formula in (3.1), work on an affine neighbourhood \(\operatorname{Spec}R\) of \(s\), with \(A=R_{\mathfrak p}\). After a principal refinement at its selected point, a marked étale \(A\)-algebra has a finite square Jacobian presentation and a finite identity certifying that its determinant is invertible. Clearing their denominators gives an étale algebra over some \(R_r\), \(r\notin\mathfrak p\). Base change back to \(A\) recovers the algebra, and its selected point and residue embedding determine a geometric marking on this neighbourhood. Conversely, tensoring the coordinate ring of a geometric affine neighbourhood with \(A\) gives an algebraic marked stage; each denominator outside its selected prime is supplied by a principal open refinement. Finitely many elements and algebra relations can be put at a common stage, by Proposition 1.2, and their finitely many denominators can be inverted together. These constructions therefore induce inverse maps on the colimits, respecting the residue embeddings. Affine cofinality from Section 1 permits non-affine neighbourhoods as well. This proves the second geometric identification in (3.1). ∎ [Stacks, Tags [04GP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-strict-henselization), [04GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-strict-henselization-different), [03QL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-henselization)]

If \(A=k\) is a field, a marked étale algebra is a product of finite separable fields and its selected field factor is a cofinal refinement. It follows directly that

\[
k^h=k,\qquad k^{sh}=k^{\mathrm{sep}}.
\tag{3.3}
\]

With a fixed marking the universal properties give canonical uniqueness. After the marking is forgotten, different identifications of a separable closure can give different isomorphisms. For a finite field these already include its nontrivial power automorphisms.

We import the remaining algebraic properties with their exact scope: \(A\to A^h\to A^{sh}\) are faithfully flat; \(A\) is Noetherian if and only if either henselization is Noetherian; and for Noetherian \(A\), the completion of \(A^h\) is canonically the completion of \(A\) [Stacks, Tags [07QM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dumb-properties-henselization), [06LJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-noetherian)]. The last statement concerns ordinary henselization. A strict henselization can enlarge the residue field and its completion accordingly.

Henselianity still does not imply completeness. For instance, \(\mathbf Q[x]_{(x)}^h\) is countable: up to isomorphism there are countably many finite presentations over the countable base and countably many marked stages, since each stage has finitely many closed-fibre points. Each stage is countable, so their colimit is countable. Its completion is \(\mathbf Q[[x]]\), which is uncountable by the binary coefficient sequences. Thus this henselian ring is not complete.

## 4. Extracting the finite branches

We use the algebraic statement of **Zariski's Main Theorem**. If \(A\to B\) is finite type, \(B'\subset B\) is the integral closure of \(A\) in \(B\), and \(\mathfrak q\) is a quasi-finite point, then there is \(g\in B'\setminus\mathfrak q\) such that \(B'_g=B_g\) [Stacks, Tag [00Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-main-theorem)]. This statement allows arbitrary rings and does not require finite presentation.

**Lemma 4.1 (finite part over a henselian base).** Let \(A\) be henselian local with residue field \(k\), and let \(B\) be a finite type \(A\)-algebra. Then

\[
B=B_1\times\cdots\times B_r\times C,
\tag{4.1}
\]

where each \(B_i\) is finite and local over \(A\), with a single point in its closed fibre, and \(C\) has no point in its closed fibre at which the morphism is quasi-finite. Equivalently every irreducible component of \(\operatorname{Spec}(C\otimes_A k)\) has positive dimension. The \(B_i\) correspond to all the isolated points of \(\operatorname{Spec}(B\otimes_A k)\).

**Proof.** The fibre is a finite type \(k\)-scheme, hence Noetherian, so it has only finitely many isolated points \(\mathfrak q_1,\ldots,\mathfrak q_r\). They are exactly its quasi-finite points. Algebraic Zariski's Main Theorem gives \(g_i\in B'\setminus\mathfrak q_i\) with \(B'_{g_i}=B_{g_i}\).

Choose algebra generators \(b_1,\ldots,b_n\) of \(B/A\). In \(B'_{g_i}\), each \(b_j\) can be written using a numerator in \(B'\) and a power of \(g_i\) as denominator. Let \(C\subset B'\) be the \(A\)-subalgebra generated by all the \(g_i\) and these finitely many numerators. These elements are integral over \(A\), so \(C\) is finite over \(A\). Since \(C_{g_i}\) contains all \(b_j\) and \(g_i^{-1}\), it equals \(B_{g_i}\).

The maximal ideals \(\mathfrak n_i=\mathfrak q_i\cap C\) are distinct. If \(\mathfrak n_i=\mathfrak n_j\), then \(g_i\) avoids both, so both points occur in \(B_{g_i}=C_{g_i}\) over that same prime and must be equal. Henselianity decomposes \(C\) into local factors. Let \(e_i\in C\) be the idempotent of the factor with maximal ideal \(\mathfrak n_i\). The element \(g_i\) is a unit in \(e_iC\), and hence in \(e_iB\). Consequently

\[
e_iB=(e_iB)_{g_i}=(e_iC)_{g_i}=e_iC.
\]

Thus these orthogonal idempotents give finite local factors \(B_i=e_iB\), each with its single closed-fibre point \(\mathfrak q_i\). The residual factor is \((1-\sum e_i)B\), and its closed fibre has no isolated point. If \(r=0\), simply take this residual factor to be \(B\). In a finite type scheme over a field, a zero-dimensional irreducible component is an isolated point: it is a closed point and cannot lie in a different maximal irreducible component. This gives the equivalent dimension statement. ∎ [Stacks, Tags [04GJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-mop-up), [03QE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-quasi-finite-etale-locally)]

**Theorem 4.2 (one quasi-finite point).** Let \(f:X\to S\) be locally of finite type and quasi-finite at \(x\), with image \(s\). There is an elementary étale neighbourhood \((U,u)\) of \(s\) and an open \(V\subset X_U\) finite over \(U\), whose fibre over \(u\) consists of a single point \(v\) above \(x\). Moreover \(\kappa(v)=\kappa(x)\) under the canonical identification \(\kappa(u)=\kappa(s)\).

**Proof.** Choose affine neighbourhoods \(\operatorname{Spec}R\subset S\) and \(Y=\operatorname{Spec}B\subset X\) around \(s,x\) with \(B\) finite type over \(R\). Put \(A=R_{\mathfrak p}\) and \(H=A^h\). The closed fibre after base change to \(H\) is unchanged. Lemma 4.1 provides a finite local factor of \(B\otimes_R H\) corresponding to \(x\). Thus an idempotent \(e\) defines this factor as \(e(B\otimes_R H)\).

Theorem 3.1 expresses \(H\) as the colimit of elementary affine étale neighbourhood algebras \(R_\lambda\) of \(s\). The element \(e\), and the equality \(e^2=e\), occur at some stage. Suppose \(b_1,\ldots,b_n\) generate \(B\) as an \(R\)-algebra. The finite \(H\)-algebra \(e(B\otimes_R H)\) has these \(eb_i\) as algebra generators, and each satisfies a monic integrality equation. Their finitely many coefficients occur at a later stage. Their equations also hold at a later stage: equality of two elements in a filtered colimit means they become equal in some stage. There are finitely many equations, so a common stage suffices. Constants in these equations are multiplied by the factor's unit \(e\).

At that stage, the factor

\[
C_\lambda=e(B\otimes_R R_\lambda)
\tag{4.2}
\]

is generated by finitely many integral elements. The monic equations bound the needed powers of each generator, proving directly that \(C_\lambda\) is a finite \(R_\lambda\)-module. Its spectrum is clopen in \(Y_{R_\lambda}\), hence open in \(X_{R_\lambda}\). Over the marked point \(u\), the fibre is the same selected factor as over \(H\), since its residue field is still \(\kappa(s)\). It has the required single point and unchanged residue field. Take \(U=\operatorname{Spec}R_\lambda\) and \(V=\operatorname{Spec}C_\lambda\). ∎ [Stacks, Tag [02LK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-makes-quasi-finite-finite-at-point)]

This descent used finite algebra generators and finitely many equations for their integrality. It did not assume that the relations defining \(B\) were finitely generated.

**Theorem 4.3 (several points and separatedness).** Given finitely many distinct quasi-finite points \(x_1,\ldots,x_n\) over \(s\), one elementary neighbourhood works simultaneously, with finite opens \(V_i\) and single fibre points \(v_i\) above \(x_i\). If \(f\) is separated, they can be chosen disjoint and clopen, giving

\[
X_U=V_1\amalg\cdots\amalg V_n\amalg W.
\tag{4.3}
\]

The fibre of \(W\) avoids the selected \(x_i\). It is empty if these are all the points of \(X_s\).

**Proof.** Apply Theorem 4.2 to each point and take a common elementary refinement. Base change preserves finiteness and the single selected fibre points. In the separated case each finite open is closed: its graph in \(V_i\times_U X_U\) is closed, and projection to \(X_U\) is proper as a base change of the finite map \(V_i\to U\). Thus \(V_i\to X_U\) is proper and has closed image. Each intersection \(V_i\cap V_j\) is therefore finite over \(U\), and its image is closed and misses \(u\), since its fibre there is empty. Shrink \(U\) away from these finitely many images. The remaining opens are disjoint and clopen. Their complement gives (4.3) and the asserted fibre statement. ∎ [Stacks, Tags [02LL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-makes-quasi-finite-finite-multiple-points), [02LN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-splits-off-quasi-finite-part-technical)]

Selecting only one point does not remove other fibre points. For the disjoint union of two identity maps \(S\amalg S\to S\), selecting the first point leaves the second point in \(W_s\).

There is also a residue-splitting version [Stacks, Tags [02LM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-makes-quasi-finite-finite-multiple-points-var), [02LO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-splits-off-quasi-finite-part-technical-variant), [02LP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-etale-splits-off-quasi-finite-part)]. After an étale neighbourhood that need not be elementary, the finite parts can be required to have purely inseparable residue extensions at their single selected fibre points. Here is the construction. For the finitely many selected finite residue extensions \(K_i/k\), let \(L_i\subset K_i\) be their maximal separable subextensions. The extensions \(K_i/L_i\) are purely inseparable. Choose a finite Galois extension \(L/k\) containing all embeddings of the \(L_i\), and realize it using Lemma 1.1. Each

\[
K_i\otimes_k L
\tag{4.4}
\]

is a product of fields purely inseparable over \(L\): split \(L_i\otimes_k L\) into its embedding factors, then extend the purely inseparable extension to each factor. Apply Theorem 4.3 to all these lifted points. The subsequent elementary refinement keeps their residue extensions unchanged. For an affine finite type \(X\), select every isolated fibre point; the remaining part has no quasi-finite point in the distinguished fibre. A finite field extension preserves positive-dimensional fibre components, so none are missed by this selection. This proves the finite type algebra variant as well as the selected-point scheme versions.

## 5. Splitting unramified schemes and étale coverings

**Theorem 5.1.** Let \(f:X\to S\) be finite and unramified. For every \(s\in S\), an étale neighbourhood \((U,u)\) makes \(X_U\) a finite disjoint union of closed subschemes of \(U\). If \(f\) is finite étale, this disjoint union consists of copies of \(U\).

**Proof.** Work over an affine neighbourhood of \(s\). The fibre algebra of a finite unramified morphism is a finite product of finite separable residue fields, by **Unramified morphisms**. Apply the residue-splitting version of Section 4 to all of its points. Its purely inseparable residue extensions are also separable, hence trivial. Since a finite morphism is separated, we obtain disjoint clopen finite parts \(V_i\), each with a single distinguished fibre point of residue \(\kappa(u)\), and a finite complement \(W\) with empty distinguished fibre. Its image is closed, so shrinking \(U\) removes \(W\).

Write \(U=\operatorname{Spec}R\) and \(V_i=\operatorname{Spec}C_i\). Unramifiedness says that the entire fibre algebra \(C_i\otimes_R\kappa(u)\), not just its residue field, equals \(\kappa(u)\). The cokernel of the map

\[
R\longrightarrow C_i,\qquad a\longmapsto a\cdot1,
\tag{5.1}
\]

is a finite \(R\)-module whose reduction at \(u\) is zero. Nakayama makes its localization at \(u\) zero. Finitely many generators then vanish on a common open neighbourhood of \(u\). Shrink to this open for every \(i\); (5.1) becomes surjective. Thus each \(V_i\to U\) is a closed immersion. This argument also covers finite unramified morphisms that are not finitely presented.

If \(f\) is étale, each closed immersion \(V_i\to U\) is also étale. By the open immersion criterion from **Étale morphisms and their local structure**, it is an open immersion. Its image is an open neighbourhood of \(u\). Shrink \(U\) to the intersection of these finitely many images. Each \(V_i\to U\) is now an isomorphism. The number of copies may be zero. ∎ [Stacks, Tags [04HJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-unramified-etale-local), [04HN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-finite-etale-etale-local)]

In particular an étale morphism is locally on its source an open piece of a finite étale morphism after a suitable étale neighbourhood of the base: apply Theorem 4.2 and retain its finite étale open. Theorem 5.1 then splits this piece into local copies of the base [Stacks, Tags [04HL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-etale-etale-local), [04HM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale.html#etale-lemma-etale-etale-local-technical)]. Finiteness is what allows a residual piece with empty fibre to be removed by deleting its closed image.

**Theorem 5.2 (henselian finite étale equivalence).** For henselian local \((A,\mathfrak m,k)\), reduction is an equivalence between finite étale \(A\)-algebras and finite étale \(k\)-algebras:

\[
B\longmapsto B/\mathfrak mB.
\tag{5.2}
\]

It preserves all morphisms and automorphisms. More generally, if \(B\) is finite étale and \(C\) is any finite \(A\)-algebra, then

\[
\operatorname{Hom}_A(B,C)
\xrightarrow{\ \sim\ }
\operatorname{Hom}_k(B/\mathfrak mB,C/\mathfrak mC).
\tag{5.3}
\]

**Proof.** A finite étale \(k\)-algebra is a product of finite separable fields. For a field factor choose a monic separable minimal polynomial \(\bar F\) and lift its coefficients to a monic \(F\in A[T]\). The algebra \(B=A[T]/(F)\) is finite free. The derivative is invertible in \(B/\mathfrak mB\). Every maximal ideal of the finite algebra \(B\) lies over \(\mathfrak m\), so \(F'\) is in no maximal ideal of \(B\) and is a unit. Thus \(B\) is étale and lifts the chosen field. Products prove essential surjectivity.

For (5.3), split \(C\) into its henselian local factors \(C_j\), using the imported finite-algebra criterion. A specified map on reductions gives, for each \(j\), a map

\[
B\longrightarrow C_j/\mathfrak mC_j
\longrightarrow\kappa(C_j).
\]

This selects a rational closed-fibre point of the étale \(C_j\)-algebra \(B\otimes_A C_j\). Theorem 2.1 gives its unique section, hence a map \(B\to C_j\). Its reduction is the prescribed map: the local finite \(k\)-algebra \(C_j/\mathfrak mC_j\) has nilpotent radical, and maps from the étale \(k\)-algebra \(B/\mathfrak mB\) agreeing after quotienting by that radical agree by infinitesimal uniqueness from the preceding lesson. The same section uniqueness shows that every lift is this one. Combining the factors proves (5.3). Taking \(C\) finite étale proves full faithfulness in (5.2), completing the equivalence. ∎ [Stacks, Tag [04GK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-henselian-cat-finite-etale)]

The uniqueness here is relative to a prescribed reduction map. A lifted finite separable field extension retains its field automorphisms; the theorem does not discard them. Over a strictly henselian ring the finite étale algebras are therefore exactly finite products of the base ring, with the maps corresponding to maps between the finite sets of components.

### Henselian pairs and finite étale algebras

Theorem 5.2 works modulo the maximal ideal of a local ring. To compare an affine scheme with a closed subscheme that need not be a point, we replace the maximal ideal by an arbitrary ideal \(I\) of a ring \(A\). The pair \((A,I)\) is a **henselian pair** if \(I\subset\operatorname{Jac}(A)\) and the following lifting property holds. Let \(f\in A[T]\) be monic, and suppose \(\bar f=g_0h_0\) in \((A/I)[T]\), with \(g_0,h_0\) monic and generating the unit ideal of \((A/I)[T]\). Then \(f=gh\) for monic \(g,h\in A[T]\) with \(\bar g=g_0\) and \(\bar h=h_0\). Nothing is assumed about Noetherianity or completeness. For a local ring and \(I=\mathfrak m\) this is the factorization form of henselianity recalled in Section 2. The results of this subsection are proved in the Stacks Project, *More on Algebra*, [Tags 09XI](https://stacks.math.columbia.edu/tag/09XI), [09XH](https://stacks.math.columbia.edu/tag/09XH) and [09ZL](https://stacks.math.columbia.edu/tag/09ZL).

Two elementary facts are used repeatedly. If \(D\) is integral over \(A\) and \(\mathfrak n\subset D\) is a maximal ideal, then the field \(D/\mathfrak n\) is integral over its subring \(A/(\mathfrak n\cap A)\), so that subring is a field and \(\mathfrak n\cap A\) is maximal. Hence \(I\subset\mathfrak n\) whenever \(I\subset\operatorname{Jac}(A)\), and

\[
ID\subset\operatorname{Jac}(D)\qquad(D\text{ integral over }A,\ I\subset\operatorname{Jac}(A)).
\]

Secondly, for a polynomial \(q\) and an idempotent \(\varepsilon\) of any ring, \(q(\varepsilon)=q(1)\varepsilon+q(0)(1-\varepsilon)\), since \(\varepsilon^j=\varepsilon\) for \(j\ge1\).

**Lemma 5.3 (idempotents lift in integral algebras).** Suppose \((A,I)\) is a henselian pair and \(D\) is an integral \(A\)-algebra. Then reduction modulo \(ID\) is a bijection

\[
\operatorname{Idem}(D)\longrightarrow\operatorname{Idem}(D/ID).
\tag{5.4}
\]

**Proof.** *Injectivity.* Let \(e,e'\) be idempotents and put \(x=e-e'\). Expanding gives \(x^2=e+e'-2ee'\) and then \(x^3=x\). If \(e\) and \(e'\) have the same reduction, then \(x\in ID\subset\operatorname{Jac}(D)\). So \(1-x^2\) is a unit, and \(x(1-x^2)=0\) forces \(x=0\).

*Surjectivity for finite \(D\).* Suppose first that \(D\) is a finite \(A\)-module. Write \(\bar D=D/ID\), let \(\bar e\in\bar D\) be idempotent, and choose \(b\in D\) with image \(\bar e\). The ring \(\bar D\) is the product of \(\bar e\bar D\) and \((1-\bar e)\bar D\). Lift finitely many \(A\)-module generators of the first factor to \(y_1,\ldots,y_r\in D\), and of the second to \(y_{r+1},\ldots,y_{r+s}\in D\). Let \(N\) be the \(A\)-span of all the \(y_k\). Then \(N+ID=D\), and Nakayama's lemma for the finite \(A\)-module \(D/N\) gives \(N=D\). In \(\bar D\), multiplication by \(\bar b=\bar e\) fixes the first \(r\) generators and kills the others. The differences therefore lie in \(ID=IN\), which consists of combinations of the \(y_k\) with coefficients in \(I\). So there is a square matrix \(M\) over \(A\) with

\[
by_k=\sum_lM_{kl}y_l\quad(1\le k\le r+s),
\qquad
M\equiv\operatorname{diag}(\underbrace{1,\ldots,1}_r,\underbrace{0,\ldots,0}_s)\pmod I .
\]

Multiplying the vector identity \((b\,\mathrm{Id}-M)y=0\) on the left by the adjugate of \(b\,\mathrm{Id}-M\) shows that \(\chi(b)\) annihilates every \(y_k\), hence annihilates \(1\in D\), where \(\chi(T)=\det(T\,\mathrm{Id}-M)\). So \(\chi(b)=0\), \(\chi\) is monic, and

\[
\bar\chi(T)=(T-1)^rT^s.
\tag{5.5}
\]

If \(r=0\) then \(\bar e=0\), and if \(s=0\) then \(\bar e=1\); in these cases \(0\) or \(1\) is the required lift. Let \(r,s\ge1\). The polynomials \((T-1)^r\) and \(T^s\) generate the unit ideal of \((A/I)[T]\), because \(T-(T-1)=1\). The pair condition gives \(\chi=gh\), with \(g,h\) monic, \(\bar g=(T-1)^r\) and \(\bar h=T^s\). These lifts again generate the unit ideal. Indeed, \(Q=A[T]/(g,h)\) is a finite \(A\)-module because \(g\) is monic, and \(Q/IQ=(A/I)[T]/(\bar g,\bar h)=0\); Nakayama's lemma gives \(Q=0\). By the Chinese remainder theorem, \(A[T]/(\chi)\cong A[T]/(g)\times A[T]/(h)\). Choose \(p\in A[T]\) with \(p\equiv1\) modulo \(g\) and \(p\equiv0\) modulo \(h\). Since \(\chi(b)=0\), the element \(e=p(b)\) of \(D\) satisfies \(e^2=e\), because \(p^2-p\) is divisible by \(gh=\chi\). Its reduction is \(\bar p(\bar e)=\bar p(1)\bar e+\bar p(0)(1-\bar e)\). Here \(\bar p(1)=1\) because \((T-1)^r\) divides \(\bar p-1\), and \(\bar p(0)=0\) because \(T^s\) divides \(\bar p\). So \(e\) reduces to \(\bar e\).

*Surjectivity in general.* Let \(D\) be integral, let \(\bar e\) be an idempotent of \(D/ID\), and let \(b\in D\) reduce to it. Write \(b^2-b=\sum_{j=1}^m\iota_jd_j\), with \(\iota_j\in I\) and \(d_j\in D\). The subalgebra \(D_0=A[b,d_1,\ldots,d_m]\) is generated by finitely many integral elements, so it is a finite \(A\)-module, and the class of \(b\) in \(D_0/ID_0\) is idempotent. The finite case gives an idempotent \(e\in D_0\) with \(e-b\in ID_0\subset ID\). ∎

The argument uses a finite generating set of \(D\), not a basis, and nowhere assumes that \(A\) or \(D\) is Noetherian. In particular it does not presuppose that finite \(A\)-algebras split into local factors.

**Lemma 5.4 (an étale lift before imposing finiteness).** For every ring \(A\) and ideal \(I\subset A\), each étale \(A/I\)-algebra \(C\) is the reduction of an étale \(A\)-algebra \(D\): there is an isomorphism of \(A/I\)-algebras \(D/ID\cong C\).

**Proof.** By Infinitesimal lifting and the invariance of étale morphisms under thickenings, Lemma 6.1, \(C\) has a presentation \((A/I)[x_1,\ldots,x_n]/(\bar f_1,\ldots,\bar f_n)\) whose Jacobian determinant \(\bar\Delta=\det(\partial\bar f_i/\partial x_j)\) is a unit of \(C\). Choose \(f_i\in A[x_1,\ldots,x_n]\) reducing to \(\bar f_i\), let \(\Delta\) be their Jacobian determinant, and put

\[
D=A[x_1,\ldots,x_n,z]/(f_1,\ldots,f_n,z\Delta-1).
\tag{5.6}
\]

Thus \(D=\bigl(A[x_1,\ldots,x_n]/(f_1,\ldots,f_n)\bigr)_\Delta\), which has the form (1.1) of Étale morphisms and their local structure and is therefore étale over \(A\). Modulo \(I\) it becomes \(C[z]/(z\bar\Delta-1)=C_{\bar\Delta}\), which is \(C\) because \(\bar\Delta\) is already a unit of \(C\). The determinant is inverted outright, so no nilpotence of \(I\) is needed. ∎ [Stacks, Tag 00U9.]

The algebra \(D\) need not be finite over \(A\). The next lemma isolates the part of \(D\) lying over a finite piece of its reduction, without knowing whether the elements of \(D\) integral over \(A\) form a finite \(A\)-module.

**Lemma 5.5 (the integral component around a finite fibre).** Consider an \(A\)-algebra \(D\) of finite type whose reduction splits as

\[
D/ID=C\times C_2,
\qquad C\text{ finite over }A/I.
\]

Write \(R\subset D\) for the subring of elements integral over \(A\). Then there is a decomposition

\[
R/IR=C'\times C_2'
\tag{5.7}
\]

such that \(R/IR\to D/ID\) maps \(C'\) isomorphically onto \(C\) and \(C_2'\) into \(C_2\), and there is \(g\in R\) with image \((1,0)\) in (5.7) such that \(R_g\to D_g\) is an isomorphism.

**Proof.** Write \(\phi:\operatorname{Spec}D\to\operatorname{Spec}R\) and \(T=\operatorname{Spec}C\), a subset of \(\operatorname{Spec}D\) that is open and closed in \(V(ID)\). Let \(\mathfrak q\in T\) lie over \(\mathfrak p\in\operatorname{Spec}A\). Then \(I\subset\mathfrak p\), so the fibre of \(\operatorname{Spec}D\) over \(\mathfrak p\) is the spectrum of \((C\otimes_A\kappa(\mathfrak p))\times(C_2\otimes_A\kappa(\mathfrak p))\). The first factor is a finite \(\kappa(\mathfrak p)\)-algebra, so its spectrum is a finite discrete open subset of the fibre containing \(\mathfrak q\). Thus \(\mathfrak q\) is isolated in its fibre, and \(A\to D\) is quasi-finite at \(\mathfrak q\). The algebraic Zariski Main Theorem in its arbitrary-base, finite type form (Zariski's Main Theorem, Theorem 1.1; recalled in Section 4) gives \(h_{\mathfrak q}\in R\setminus\mathfrak q\) with \(R_{h_{\mathfrak q}}\cong D_{h_{\mathfrak q}}\). Let \(U\subset\operatorname{Spec}R\) be the union of the opens \(D(h_{\mathfrak q})\). Over each of them \(\phi\) is an isomorphism, so \(\phi^{-1}(U)\to U\) is an isomorphism of schemes, and \(T\subset\phi^{-1}(U)\).

Put \(W=\phi(T)\). The \(A/I\)-algebra \(C\) is a finite \(R\)-module as well, so \(W\), the image of \(\operatorname{Spec}C\to\operatorname{Spec}R\), is closed. The isomorphism \(\phi^{-1}(U)\cong U\) carries \(\phi^{-1}(U)\cap V(ID)\) onto \(U\cap V(IR)\), because \(\phi^{-1}(V(IR))=V(ID)\). As \(T\) is open in \(V(ID)\) and contained in \(\phi^{-1}(U)\), its image \(W\) is open in \(U\cap V(IR)\), hence in \(V(IR)\). So \(W\) is open and closed in \(\operatorname{Spec}(R/IR)\), and gives the decomposition (5.7) with \(\operatorname{Spec}C'=W\). Over \(U\) the closed subschemes cut out by \(I\) correspond under \(\phi\), and \(T\) corresponds to \(W\). Since \(\phi\) is injective on \(\phi^{-1}(U)\), the points of \(V(ID)\) over \(W\) are exactly those of \(T\). Thus \(R/IR\to D/ID\) sends the idempotent of \(C'\) to that of \(C\), and the induced map \(C'\to C\) is an isomorphism, being the ring map of the isomorphism \(T\cong W\) of affine schemes. The other factor goes to the other factor.

It remains to choose \(g\). Let \(J\subset R\) be an ideal with \(V(J)=\operatorname{Spec}R\setminus U\). Since \(W\subset U\), the ideal generated by \(J\) in \(C'\) has no zeros, so it is the unit ideal. Multiplying a relation \(1=\sum_kj_kc_k\) in \(C'\) by the idempotent \((1,0)\) shows that \((1,0)\) lies in the image of \(J\) in \(R/IR\). Choose \(g\in J\) with image \((1,0)\). Then \(D(g)\subset U\), and the isomorphism over \(U\) restricts to \(R_g\cong D_g\). ∎ [Stacks, Tag 09XH.]

**Theorem 5.6 (finite étale equivalence for every henselian pair).** Let \((A,I)\) be a henselian pair. Then \(B\mapsto B/IB\) is an equivalence

\[
\operatorname{F\acute EtAlg}(A)
\xrightarrow{\ \sim\ }
\operatorname{F\acute EtAlg}(A/I),
\qquad B\longmapsto B/IB.
\tag{5.8}
\]

Every object and every morphism lifts, and a morphism is determined by its reduction. In geometric terms, pulling back to \(\operatorname{Spec}(A/I)\) identifies finite étale schemes over \(\operatorname{Spec}A\) with finite étale schemes over \(\operatorname{Spec}(A/I)\).

**Proof of full faithfulness.** Fix finite étale \(A\)-algebras \(B\) and \(B'\), and let \(E=B\otimes_AB'\), a finite étale \(B'\)-algebra by base change. Giving an \(A\)-algebra map \(u:B\to B'\) amounts to giving a \(B'\)-algebra map \(\sigma_u:E\to B'\), namely \(b\otimes b'\mapsto u(b)b'\). Such a \(\sigma\) is surjective, so \(\operatorname{Spec}\sigma\) is a closed immersion, in particular universally injective. It is étale by Étale morphisms and their local structure, Proposition 2.1, being a morphism of schemes étale over \(\operatorname{Spec}B'\). By Theorem 4.1 there, an étale universally injective morphism is an open immersion. Its image is therefore open and closed, so \(\ker\sigma=(1-e)E\) for an idempotent \(e\), and \(B'\to eE\) is an isomorphism. Conversely, an idempotent \(e\) for which \(B'\to eE\) is an isomorphism defines \(\sigma\) as the projection \(E\to eE\) followed by the inverse of that isomorphism. This gives a bijection between \(\operatorname{Hom}_A(B,B')\) and the set of such idempotents. The same holds over \(A/I\) for \(\bar B=B/IB\), \(\bar B'=B'/IB'\) and \(\bar E=E/IE=\bar B\otimes_{A/I}\bar B'\), and reduction is compatible with both bijections.

Let \(\bar u:\bar B\to\bar B'\) be given, with idempotent \(\bar e\in\bar E\). As \(E\) is finite over \(A\), Lemma 5.3 lifts \(\bar e\) to a unique idempotent \(e\in E\). The map \(B'\to eE\) is surjective: its cokernel is a finite \(B'\)-module with zero reduction, and \(IB'\subset\operatorname{Jac}(B')\) because \(B'\) is integral over \(A\). It is a surjective map of étale \(B'\)-algebras, so by the argument just given its kernel is \(fB'\) for an idempotent \(f\in B'\). The reduction \(\bar B'\to\bar e\bar E\) is injective, so \(\bar f=0\), and Lemma 5.3 for \(B'\) gives \(f=0\). Hence \(B'\to eE\) is an isomorphism, and \(e\) corresponds to a map \(u:B\to B'\) reducing to \(\bar u\). If two maps have the same reduction, their idempotents have the same reduction and coincide by Lemma 5.3, so the maps coincide.

**Proof of essential surjectivity.** Start with a finite étale \(A/I\)-algebra \(C\). Lemma 5.4 gives an étale \(A\)-algebra \(D\) with \(D/ID\cong C\). Apply Lemma 5.5 with \(C_2=0\): with \(R\) the integral closure of \(A\) in \(D\), we get \(R/IR=C'\times C_2'\) with \(C'\cong C\), and \(g\in R\) with image \((1,0)\) and \(R_g\cong D_g\). Lemma 5.3, applied to the integral \(A\)-algebra \(R\), lifts \((1,0)\) to an idempotent \(e\in R\). We obtain

\[
R=R_1\times R_2,
\qquad R_1=eR,\quad R_1/IR_1=C'\cong C.
\tag{5.9}
\]

The component \(eg\) of \(g\) in \(R_1\) is congruent to \(1\) modulo \(IR_1\subset\operatorname{Jac}(R_1)\), so it is a unit of \(R_1\). Hence \(D_g\cong R_g=R_1\times(R_2)_g\), and \(R_1\) is the localization of the étale \(A\)-algebra \(D_g\) at an idempotent. So \(R_1\) is étale over \(A\), in particular of finite type. Being integral over \(A\) as well, it is spanned as a module by finitely many monomials in finitely many algebra generators, each of which satisfies a monic equation. Hence \(R_1\) is finite étale over \(A\) with reduction \(C\). ∎ [Stacks, Tag 09ZL; Tag 09ZS states the version for schemes.]

At no point is \(I\) replaced by a maximal ideal, is the integral closure \(R\) shown to be finite, or is \(A\) assumed Noetherian. Taking \(A\) local and \(I=\mathfrak m\) recovers (5.2). The local statement (5.3) remains stronger in one respect: its target may be any finite algebra.

A product of two henselian local rings gives an example that is not local: take \(A=A_1\times A_2\) with \((A_i,\mathfrak m_i)\) henselian local, and \(I=\mathfrak m_1\times\mathfrak m_2\). Then \(I\) is the Jacobson radical of \(A\). A monic polynomial over \(A\) is a pair of monic polynomials of the same degree, and coprime monic factorizations modulo \(I\) lift componentwise. So \((A,I)\) is a henselian pair. By (5.8), a finite étale \(A\)-algebra amounts to two finite étale algebras, one over each residue field, and their ranks may differ. The theorem is not limited to such products: it holds for every ideal satisfying the pair conditions.


### Universal homeomorphisms preserve étale objects

By the preceding lesson, étale objects do not see nilpotent structure. Integral descent shows that they do not see purely inseparable identifications of points either. The order of the arguments matters. The descent proof uses the henselian-pair equivalence just established, while the proof of that equivalence used no descent.

From Descending properties of schemes and morphisms we use two results whose proofs are written there. Theorem 5.2: along a universally submersive morphism, pullback of étale schemes to descent data is fully faithful. Theorem 6.4: along a surjective integral morphism, every descent datum on a quasi-compact separated étale scheme is effective. Its finite étale input over henselian pairs is Theorem 5.6 above. An integral surjective morphism is universally closed and surjective, hence universally submersive: after any base change the target carries the quotient topology.

**Theorem 5.7 (topological invariance of étale objects).** Let \(p:S'\to S\) be integral, surjective and universally injective, that is, a universal homeomorphism. Then \(U\mapsto U\times_SS'\) is an equivalence

\[
\operatorname{\acute Et}(S)\xrightarrow{\ \sim\ }\operatorname{\acute Et}(S').
\tag{5.10}
\]

Here étale schemes need not be separated or quasi-compact. A family of étale maps is jointly surjective exactly when its pullback is, so (5.10) also identifies the small étale sites of \(S\) and \(S'\), and their topoi.

**Proof.** *Every étale \(S'\)-scheme carries exactly one descent datum restricting to the identity.* The morphism \(p\) is integral, hence affine and separated, so the diagonal \(\delta:S'\to S''=S'\times_SS'\) is a closed immersion. Universal injectivity makes \(\delta\) surjective. So \(\delta\) is a thickening, and so is the small diagonal of \(S'\) in \(S'''=S'\times_SS'\times_SS'\). Let \(U'\to S'\) be étale, and let \(U'_1,U'_2\) be its pullbacks to \(S''\) along the two projections. Both restrict along \(\delta\) to \(U'\). Theorem 5.3 of the preceding lesson, the equivalence along thickenings, gives a unique isomorphism \(\varphi:U'_1\to U'_2\) of étale \(S''\)-schemes whose restriction along \(\delta\) is \(\mathrm{id}_{U'}\). The cocycle identity on \(S'''\) compares two isomorphisms of étale \(S'''\)-schemes, and both become the identity on the small diagonal, so it holds by full faithfulness along that thickening. Conversely, any descent datum on \(U'\) restricts to the identity along \(\delta\): restricting its cocycle identity along the small diagonal shows that this restriction equals its own square, and an automorphism with that property is the identity. So \(\varphi\) is the only descent datum on \(U'\). For a morphism \(U'\to V'\) of étale \(S'\)-schemes, compatibility with the two data is an equation between morphisms over \(S''\). Along \(\delta\) both sides restrict to the given morphism, so the equation holds. Therefore forgetting the datum is an equivalence from étale descent data for \(S'/S\) to étale \(S'\)-schemes.

*Full faithfulness.* By Theorem 5.2 of the descent lesson, pullback from étale \(S\)-schemes to étale descent data is fully faithful, since \(p\) is universally submersive. Composing with the equivalence above proves that (5.10) is fully faithful.

*Essential surjectivity, affine case.* Let \(S\) and the étale \(S'\)-scheme \(U'\) be affine. Then \(S'\) is affine because \(p\) is integral, and \(U'\to S'\) is affine, hence quasi-compact and separated. By Theorem 6.4 of the descent lesson, the canonical datum of \(U'\) is effective. So there is a quasi-compact separated étale \(U\to S\) with \(U\times_SS'\cong U'\).

*Essential surjectivity in general.* Let \(U'\to S'\) be étale. Cover \(U'\) by affine opens \(U'_i\), each mapping into \(p^{-1}(S_i)\) for an affine open \(S_i\subset S\). The restriction \(p^{-1}(S_i)\to S_i\) is again a universal homeomorphism. The affine case gives étale \(U_i\to S_i\) with \(U_i\times_SS'\cong U'_i\). The projection \(U'_i\to U_i\) is a homeomorphism, so the open \(U'_i\cap U'_j\) of \(U'_i\) is the inverse image of a unique open \(U_{ij}\subset U_i\). Since restriction to an open subscheme commutes with base change, \(U_{ij}\times_SS'=U'_i\cap U'_j\). By full faithfulness, the identity of \(U'_i\cap U'_j\) comes from a unique isomorphism \(\theta_{ij}:U_{ij}\to U_{ji}\) over \(S\). The same uniqueness gives \(\theta_{ji}=\theta_{ij}^{-1}\) and the cocycle condition on triple overlaps. Gluing the \(U_i\) along the \(\theta_{ij}\) produces an étale \(S\)-scheme \(U\) with \(U\times_SS'\cong U'\). The glued scheme need not be separated or quasi-compact.

*Coverings.* A family of étale morphisms into an étale \(S\)-scheme \(V\) is jointly surjective exactly when the images cover \(V\). The projection \(V\times_SS'\to V\) is a homeomorphism, so this condition holds for the family over \(S\) if and only if it holds for its pullback. The equivalence therefore preserves and reflects coverings, which gives the statements about sites and topoi. ∎ [Stacks, Étale Cohomology, Tags 04DY–04DZ.]

In characteristic \(p>0\) the absolute Frobenius morphism is an example. Affine-locally it is \(a\mapsto a^p\). Every element of the ring is integral over the image, each prime has exactly one prime over it, and the residue field extensions are purely inseparable. Theorem 5.7 applies even when Frobenius is not finite. For the consequences in cohomology, see the étale-cohomology course, lesson 7 (**Pushforward, pullback and finite morphisms**), Theorem 6.2 in Section 6.


## 6. Roots, branches and a finite local piece

Assume \(\operatorname{char}k\ne2\) and put \(R=k[x]_{(x)}\). The polynomial \(T^2-(1+x)\) has the simple residue root 1. Hence \(R^h\) contains a root \(s\) with

\[
s^2=1+x,\qquad s\equiv1\pmod{xR^h}.
\tag{6.1}
\]

It is not a rational function in \(k(x)\): the valuation at the irreducible polynomial \(x+1\) of a square is even, whereas that of \(1+x\) is 1. In particular it is not in \(R\). The other root \(-s\) has residue \(-1\), so the marking distinguishes the two choices.

**Proposition 6.1 (the node).** The local ring at the origin of

\[
y^2=x^2(1+x)
\tag{6.2}
\]

is a domain, but its henselization is reduced with exactly two minimal primes. More precisely, with \(D=R^h\) and \(s\) as in (6.1), its henselization is

\[
D[y]/\bigl((y-xs)(y+xs)\bigr)
\cong
\{(u,v)\in D\times D:u\equiv v\pmod{xD}\}.
\tag{6.3}
\]

**Proof.** The polynomial \(y^2-x^2(1+x)\) is irreducible over \(k(x)\), by the preceding square obstruction, and the quotient embeds into that field extension because the polynomial is monic. Thus \(R[y]/(y^2-x^2(1+x))\) is a domain. It is finite over the local ring \(R\); its closed fibre is \(k[y]/(y^2)\), which has one maximal ideal. Hence this finite algebra is local and is exactly the local ring \(A\) of the node.

The imported Noetherian henselization and completion results identify \(\widehat D\) with \(k[[x]]\). The Noetherian local completion map is faithfully flat and therefore injective [Stacks, Tag [00MC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-faithfully-flat)]. Consequently \(D\) is a domain and \(x\ne0\) in \(D\).

Set \(C=A\otimes_R D\). It is finite over henselian \(D\), and its closed fibre is again \(k[y]/(y^2)\). It is therefore a local henselian ring. The local map \(A\to C\) induces \(A^h\to C\). Conversely the local map \(R\to A^h\) induces \(D\to A^h\), hence \(C\to A^h\). Their composite on \(A^h\) is the identity by its universal property. The other composite fixes \(A\), and fixes \(D\) by the uniqueness of the local map extending \(R\to C\); these generate \(C\). Thus \(C=A^h\). Equation (6.1) factors its defining polynomial as in (6.3).

Evaluation at \(y=xs\) and at \(y=-xs\) maps \(C\) to \(D\times D\). To check injectivity, work in \(D[Y]\). If a polynomial is divisible by both \(Y-xs\) and \(Y+xs\), write it as \((Y-xs)q(Y)\) and evaluate at \(-xs\). Then \(-2xs\,q(-xs)=0\). The domain property and \(2xs\ne0\) imply \(q(-xs)=0\), so monic division shows \(Y+xs\) divides \(q\). The intersection of the two linear ideals is therefore their product, the defining ideal of \(C\).

Every class has the form \(a+by\); its values are \((a+bxs,a-bxs)\). Their difference is in \(xD\). Conversely for \(u-v\in xD\), take

\[
a=\frac{u+v}{2},\qquad b=\frac{u-v}{2xs}\in D,
\]

since \(2s\) is a unit. This proves the pair-ring description. The ideals

\[
P_+=(y-xs),\qquad P_-=(y+xs)
\tag{6.4}
\]

have domain quotient \(D\), and are incomparable: the other linear factor maps to \(\pm2xs\ne0\). Their intersection is zero. Every prime contains one of them because their product is zero. Thus they are exactly the two minimal primes and the ring is reduced. ∎

The two branches in (6.3) meet at their common closed point: the pair coordinates have the same residue modulo \(x\). The henselization is local, so it is not the product \(D\times D\). Splitting local factors of finite algebras does not require each local factor to be a domain.

For the quasi-finite example, let

\[
X=\operatorname{Spec}k[x,(x-1)^{-1}],
\qquad X\longrightarrow\mathbf A^1_k,\quad t=x^2.
\tag{6.5}
\]

It is quasi-finite. It is not finite: \(1/(x-1)\) cannot be integral over \(k[t]\). The integrally closed discrete valuation ring \(k[x]_{(x-1)}\) contains \(k[t]\), so such integrality would put this element in the valuation ring, contradicting its negative valuation.

Near \(t=1\), use the elementary étale neighbourhood

\[
U=\operatorname{Spec}Q,
\quad Q=k[a,a^{-1},(a+1)^{-1}],
\quad t=a^2,\quad u=(a-1).
\tag{6.6}
\]

It is étale because \(2a\) is invertible, and \(\kappa(u)=k\). The two factors \(x-a\) and \(x+a\) are comaximal because \(2a\) is a unit. The Chinese remainder theorem and then inversion of \(x-1\) give

\[
Q[x,(x-1)^{-1}]/(x^2-a^2)
\cong Q[(a-1)^{-1}]\times Q.
\tag{6.7}
\]

The second factor is the finite branch \(x=-a\) through \(x=-1\), isomorphic to \(U\). The first is the positive branch \(x=a\), whose fibre over \(u\) is empty. Its image is the open \(D(a-1)\), which cannot be removed by shrinking around \(u\). This is why a finite branch and a residual branch are separate parts of the localization theorem.

## 7. Exercises

1. **Easy.** For \(\operatorname{char}k\ne2\), prove that the residue-1 root of \(T^2-(1+x)\) belongs to \(k[x]_{(x)}^h\) and does not belong to \(k[x]_{(x)}\).
2. **Medium.** Compute the henselization of the local node ring (6.2). Identify its minimal primes and explain why it is local although it has two branches.
3. **Medium.** Let \((A,\mathfrak m,k)\) be henselian. Prove that finite étale \(A\)-algebras, including their morphisms, are determined by their reductions modulo \(\mathfrak m\). Explain the meaning of uniqueness for a chosen lift.
4. **Medium.** Perform the étale localization of (6.5) at \(t=1\). Identify the finite branch and calculate the fibre of the other branch.
5. **Hard.** Prove the geometric section characterization of henselianity for arbitrary local rings. Include uniqueness through the specified rational point and explain why existence without specifying the point must be tested on every étale neighbourhood.

**Exercise 6 (medium — a finite cover which does not split globally).** Let \(k\) be a field of characteristic different from 2, \(A=k[t,t^{-1}]\), \(I=(t-1)\), and \(B=A[u]/(u^2-t)\). Prove that \(B\) is finite étale and connected, whereas \(B/IB\cong k\times k\). Show directly that an idempotent of the reduction does not lift and that the coprime residue factorization of \(T^2-t\) does not lift. Explain which henselian-pair conditions fail.

## 8. Solutions

**Solution 1.** The derivative at the residue root 1 is 2, which is nonzero. In the henselian local ring \(R^h\), Hensel's simple-root property gives \(s^2=1+x\) and \(s\equiv1\pmod{x}\). Equivalently, the marked étale algebra \((R[T]/(T^2-(1+x)))_{2T}\), with selected point \(x=0,T=1\), puts this element directly into the colimit. If \(s\) belonged to \(R\), it would belong to \(k(x)\). Taking the valuation at \(x+1\) in \(s^2=1+x\) would give an even integer equal to 1. This contradiction proves the claim.

**Solution 2.** Put \(R=k[x]_{(x)}\), \(D=R^h\), and let \(s\) be the root from Solution 1. The node ring is \(A=R[y]/(y^2-x^2(1+x))\): it is finite local over \(R\) because its closed fibre is the local algebra \(k[y]/(y^2)\). The finite algebra

\[
C=D[y]/((y-xs)(y+xs))
\]

has that same local closed fibre, so it is local henselian. The universal properties of \(R^h\) and \(A^h\) give inverse maps \(C\leftrightarrows A^h\): one extends \(A\to C\), the other combines \(A\to A^h\) and the unique extension \(D\to A^h\); uniqueness verifies both composites on the generators.

The map to \(D^2\) by the two evaluations is injective. Indeed, in the domain \(D\), a polynomial divisible by both linear factors is divisible by their product, as evaluation of the quotient at the other root and cancellation of \(2xs\) show. Its image is exactly the pairs with difference in \(xD\): the inverse formula is \(a=(u+v)/2\), \(b=(u-v)/(2xs)\), giving \(a+by\). The kernels of the two projections are the two ideals \((y-xs)\) and \((y+xs)\); their quotients are \(D\), their intersection is zero, and every prime contains one since their product is zero. They are distinct and incomparable, hence exactly the minimal primes. The pair ring has a single maximal ideal, consisting of pairs with common residue zero, because it is the finite local ring just constructed. The congruence condition joins the two branches at that closed point.

**Solution 3.** Every finite étale \(k\)-algebra is a product of finite separable fields \(k[T]/(\bar F_i)\). Lift each monic polynomial to \(F_i\in A[T]\). The finite free algebra \(A[T]/(F_i)\) has derivative invertible modulo \(\mathfrak m\); all its maximal ideals lie over \(\mathfrak m\), so the derivative is a unit everywhere. Its product with the other lifts is finite étale and has the desired reduction.

For a prescribed residue map \(B/\mathfrak mB\to C/\mathfrak mC\), decompose finite étale \(C\) into henselian local factors \(C_j\). Their reductions are fields. In each factor the map selects a rational point of \(\operatorname{Spec}(B\otimes_A C_j)\) over the closed point. Its unique section lifts the map to \(B\to C_j\). Combining the factors gives a lift to \(C\). Any other lift selects the same point in every factor and therefore is the same map by section uniqueness. This proves full faithfulness as well as existence of every object. Two lifts with a chosen identification of their reductions have one isomorphism respecting that identification. Without prescribing it, residue automorphisms lift to automorphisms and can give several isomorphisms.

**Solution 4.** Let \(Q=k[a,a^{-1},(a+1)^{-1}]\) and take \(t=a^2\) and \(u=(a-1)\). The derivative \(2a\) is a unit, and the residue map at \(u\) is the identity of \(k\), so this is an elementary étale neighbourhood of \(t=1\). Factoring \(x^2-a^2\), the difference of its roots is \(2a\), a unit, so the Chinese remainder theorem gives \(Q[x]/(x^2-a^2)=Q\times Q\), with evaluations at \(x=a\) and \(x=-a\). Inverting \(x-1\) inverts \(a-1\) in the first factor and \(-a-1\), already a unit, in the second. Hence (6.7) follows. The negative branch is \(\operatorname{Spec}Q\), finite and isomorphic to the base, with its selected point through \(-1\). The positive branch is \(\operatorname{Spec}Q[(a-1)^{-1}]\). Tensoring its ring with \(Q/(a-1)=k\) gives the zero ring, so its selected fibre is empty.

**Solution 5.** Suppose \(A\) henselian and take a rational selected point of an étale \(A\)-scheme. On a monic standard étale chart through it the point is a simple root \(\alpha\) of a monic \(F\), with the inverted chart element nonzero at \(\alpha\). Lift \(\alpha\) using Hensel's property. The inverted element evaluates to a unit of the local ring, so evaluation defines a section into the chart. The base need not shrink: every open containing its closed point is the entire local spectrum. Two sections through the point have an open equalizer because the étale diagonal is open; their equalizer contains the closed point, hence is the whole base.

Conversely, given a simple root \(\alpha\) of any monic residue polynomial, consider \((A[T]/(F))_{F'}\) and its rational point \(T=\alpha\). A section through this point sends \(T\) to a root of \(F\) reducing to \(\alpha\), proving henselianity. If only existence of some section is assumed for every étale algebra, first invert an element whose reduction is 1 at this selected fibre point and 0 at all other fibre points. The resulting étale algebra still has the chosen point, and any section must pass through it. Thus the universal existence condition also suffices. A section of just one unlocalized algebra might pass through a different root and would not establish the required lifting property.

**Solution 6.** The monic equation makes \(B\) free of rank two over \(A\). The element \(u\) is a unit since \(u^2=t\), and its derivative \(2u\) is a unit, so \(B\) is finite étale. Eliminating \(t\) identifies it with \(k[u,u^{-1}]\), a domain, hence a connected ring with only the idempotents 0 and 1. Reduction sends \(u^2-t\) to \(u^2-1\); its roots differ by the unit 2, so the Chinese remainder theorem gives \(B/IB=k\times k\). The idempotent \((1,0)\) cannot lift to \(B\).

The residue factorization is \((T-1)(T+1)\). A monic lift of these two degree-one factors would give a root of \(T^2-t\) in \(k[t,t^{-1}]\). Its units are \(ct^n\), with \(c\in k^*\) and \(n\in\mathbf Z\): compare the lowest and highest exponents of a Laurent polynomial and its inverse. A root would be a unit whose square is \(t\), requiring \(2n=1\), which is impossible. Thus the henselian factorization condition fails. The Jacobson-radical condition fails too: \((t+1)\) is a maximal ideal not containing \(t-1\), since 2 is nonzero in \(k\). The theorem's pair conditions are therefore substantive even though the covering is finite étale.

## What this lesson does not prove

The algebraic equivalences for henselian rings, the permanence of henselianity under finite local extensions, complete local rings being henselian, faithful flatness and Noetherianity of the two henselizations, and unchanged completion for ordinary henselization are imported from the named algebraic prerequisites [Stacks, Tags [04GG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-characterize-henselian), [04GH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-over-henselian), [04GM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-complete-henselian), [07QM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-dumb-properties-henselization), [06LJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-henselization-noetherian)]. Noetherian local completion is faithfully flat [Stacks, Tag [00MC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-completion-faithfully-flat)]. The algebraic Zariski's Main Theorem is imported in the form specified in Section 4 [Stacks, Tag [00Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-theorem-main-theorem)]. The algebraic local colimit constructions and their universal properties are imported from Henselian local rings and henselization, Theorems 4.2 and 5.1. Sections 1–5 prove geometric cofilteredness, affine cofinality, spreading, the neighbourhood colimit comparisons, and the section and localization applications.

Theorem 5.6 proves finite étale equivalence for every henselian pair, with the idempotent and integral-component steps in Lemmas 5.3–5.5. Its one-square-presentation prerequisite is Lemma 6.1 of the preceding infinitesimal-lifting lesson, which is already written. Algebraic Zariski's Main Theorem is used at its full arbitrary-base, finite-type generality: Zariski's Main Theorem, Theorem 1.1, is the internal provider. Its main induction is written in Sections 1–2, and its complete supporting proofs are in the programme’s AI Integrated Stacks Project algebra chapter: Coefficients in the radical of a conductor (Tag 00PY) and Strong transcendence excludes quasi-finite points (Tag 00Q2). The former includes the conductor setup and leading-coefficient argument; the latter retains reducedness and finiteness over the algebra generated by the strongly transcendental element. Both are also included in the portable programme reader, with their original Stacks Project attribution and GNU FDL 1.2 licence in the pinned edition identified below. This establishes the named proof-provider correspondence; it does not claim recursive prerequisite closure. Theorem 5.7 uses the written integral-descent proof of Descending properties of schemes and morphisms, Theorem 6.4, after the pair-equivalence input has been established above. These dependencies neither assume the pair equivalence nor use it to prove the local structure theorem. The interpretation of strict henselizations through sheaves on the étale site is taught in **The étale site and its points**, Section 4, Theorem 4.1 (the étale-cohomology course, lesson 6).

## Sources and licence

The statements of Lemmas 5.3–5.5 and Theorem 5.6 are proved in the Stacks Project, *More on Algebra*, Tags 09XI, 09XH and 09ZL; Tag 09ZS gives Theorem 5.6 for schemes. Theorem 5.7 is *Étale Cohomology*, Tags 04DY–04DZ. The programme's AI Integrated Stacks Project edition pins these chapters at commit `565b10e987aba5969b21145a0833f42d69f96790`: [More on Algebra](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/more-algebra.tex) and [Étale Cohomology](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/etale-cohomology.tex). The other Stacks tags cited in this lesson are references for statements proved in this lesson or in the prerequisite lessons named above.

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the subsections *Henselian pairs and finite étale algebras* and *Universal homeomorphisms preserve étale objects* by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. The lesson text is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
