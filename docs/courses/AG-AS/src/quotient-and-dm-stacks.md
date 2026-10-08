# Quotient stacks and Deligne–Mumford stacks

*Written by GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026. Self-checked by the writing AI. Original text: public domain (CC0). Sections 1.1 and 6.1 follow arguments of the Stacks Project authors, cited at the end.*

## Introduction

A smooth atlas permits parameters to move in families. An étale atlas has no infinitesimal motion relative to the stack. The distinction is controlled by the diagonal: its fibres are spaces of isomorphisms, so its infinitesimal directions are infinitesimal symmetries.

We prove this criterion for arbitrary algebraic stacks, without a Noetherian or separation assumption. The difficult implication constructs an étale atlas from an unramified diagonal. We first replace a field presentation by one whose identity relation is reduced, and then cut a transverse slice in a smooth atlas. The constant-field proof supplies the field calculation; finite-inertia charts and their gluing then construct the coarse space. Quotients and elliptic curves make these distinctions concrete. The integral Weierstrass calculation proves finite isomorphism schemes and classifies geometric curves in every characteristic, then identifies their coarse space with the affine \(j\)-line among all algebraic-space targets.

We use the full presentation and Weierstrass theorems of [*Algebraic stacks*](algebraic-stacks.md), the finite flat affine quotient and division proofs of [*The bootstrap theorem*](bootstrap-theorem.md), and the scheme theory of unramified morphisms. All stacks are stacks in groupoids for the fppf topology. An atlas is representable by algebraic spaces. All products of stacks are 2-fibre products.

## 1. Unramified diagonals and a field presentation

For a representable morphism of stacks, “unramified” means that every scheme test gives an unramified morphism of algebraic spaces. Thus the condition

\[
\Delta_{\mathcal X/S}:\mathcal X\longrightarrow
\mathcal X\times_S\mathcal X
\quad\text{is unramified}
\tag{1.1}
\]

can be tested on the spaces \(\operatorname{Isom}_T(x,y)\to T\) for every scheme \(T/S\) and pair of objects \(x,y/T\). Here unramified includes local finite type; it does not require flatness. The scheme prerequisites identify it with local finite type and an open-immersion diagonal, or with local finite type and vanishing relative differentials.

Call a point of \(|\mathcal X|\) a **finite type point** if it is represented by a field map locally of finite type. This concerns the map into \(\mathcal X\), not finite generation of the field over a fixed ground field.

**Lemma 1.1.** Images of closed points of affine smooth charts are finite type points. Every nonempty closed subset of \(|\mathcal X|\) contains one.

*Proof.* If \(u\) is closed in an affine chart \(U\), then \(\operatorname{Spec}\kappa(u)\to U\) is a closed immersion and is of finite type, even when its ideal is not finitely generated. Its composite with the smooth map \(U\to\mathcal X\) is locally of finite type.

For a nonempty closed subset \(C\), choose an affine smooth chart meeting it. Its inverse image in \(U\) is a nonempty closed subset of an affine scheme, so it contains a point closed in \(U\). Its image lies in \(C\). In particular, an open subset containing all these points is all of \(|\mathcal X|\). \(\square\)

We need two elementary facts about spaces and groupoids over fields.

**Lemma 1.2 (zero-dimensional spaces over a field).** An algebraic space locally of finite type over a field \(K\), of dimension zero, is a disjoint union of spectra of finite local Artinian \(K\)-algebras. In particular it is a separated scheme, and its quasi-compact opens are affine.

*Proof.* Work first on a quasi-compact open \(X\). Choose a surjective étale map \(V\to X\) with \(V\) a finite disjoint union of affine schemes. The scheme \(V\) has dimension zero and is of finite type over \(K\), hence is finite over \(K\). The scheme

\[
E=V\times_XV
\]

is étale over \(V\), locally of finite type over \(K\), and zero-dimensional. It is therefore a disjoint union of spectra of finite local Artinian \(K\)-algebras. Its endpoint map \(E\to V\times_KV\) is a monomorphism. After extending \(K\) to an algebraic closure, each geometric point of the finite target has at most one inverse-image geometric point. Consequently there are only finitely many Artinian components of \(E\). Thus \(E\) is finite over \(K\), and its two étale projections to \(V\) are finite locally free.

The finite flat affine quotient proved in Lesson 2, Appendix A, represents \(V/E\) by an affine scheme. The first quotient theorem identifies this sheaf with \(X\). Hence \(X\) is affine.

Every point of the original space has such a quasi-compact open neighbourhood, which is a zero-dimensional finite type scheme over \(K\). Its points are open and closed. The singleton opens therefore cover the whole space and are spectra of finite local Artinian algebras. Their disjoint union is the space itself. A disjoint union of these affine schemes is separated over \(K\). \(\square\)

*Reference:* [Stacks, Tag 06LZ], field case. The finiteness of the étale relation above was proved rather than assumed.

### 1.1. The field of constants

The field-groupoid calculation needs uniqueness of the integral constants, including on a reduced connected scheme which is not quasi-compact. We prove it before using it. The argument below follows the Stacks Project authors' treatment of units and constants in *Varieties*, from the pinned AI Integrated Stacks Project edition cited at the end.

The normal-ring inputs are Theorems 1.2 and 3.3 of *Discrete valuation rings, normal rings and Serre's criterion*: height-one Noetherian normal local domains are DVRs, and a Noetherian normal domain is the intersection of its height-one localizations in its fraction field. Their current programme proofs are written. The normalization input is the genuine existing lesson *Normalization* in *Morphisms of schemes*: normalization of an integral scheme of finite type over a field is finite and restricts to normalization on each open. That finiteness proof is still planned in the selected programme edition. The following proof retains that precise prerequisite; it supplies the units and constant-field argument rather than treating its external reference as a proof.

#### Integral constants form a field

**Lemma 1.2a.** Let \(X\) be a nonempty reduced connected scheme over a field \(k\). The subring
\[
K=\{f\in\Gamma(X,\mathcal O_X):f\text{ is integral over }k\}
\tag{1.C1}
\]
is a field.

**Proof.** Integral elements form a subring: finitely many such elements generate a finite-dimensional \(k\)-algebra, since their monic equations bound the powers needed to span it. Every element of that finite algebra satisfies a monic equation by its multiplication operator. This proves closure under sums and products.

For \(f\in K\), the algebra \(k[f]\) is finite-dimensional and reduced, being a subring of the reduced ring \(\Gamma(X,\mathcal O_X)\). Its presentation is \(k[T]/(P)\) for a nonconstant monic polynomial \(P\). Reducedness makes \(P\) a product of distinct monic irreducibles. If it had two or more factors, the Chinese remainder theorem would give a nontrivial idempotent in \(k[f]\).

A global idempotent on a connected scheme is either zero or one: the loci where its germs are zero and one are disjoint open-and-closed subsets covering the scheme. Thus \(P\) has a single irreducible factor, and \(k[f]\) is a field. Every nonzero \(f\in K\) consequently has its inverse already in \(k[f]\). This proves the assertion. \(\square\)

The same argument shows that \(K\) is integrally closed inside \(\Gamma(X,\mathcal O_X)\). An element integral over \(K\) satisfies a monic equation involving only finitely many coefficients of \(K\). These coefficients lie in a finite integral \(k\)-algebra, so transitivity makes the element integral over \(k\), and it belongs to \(K\).

#### Units and the boundary of a proper model

We first establish the part of the units theorem used later. Its field \(k\) is arbitrary.

**Lemma 1.2b.** If \(Y\) is an integral proper scheme of finite type over \(k\), every element of \(\Gamma(Y,\mathcal O_Y)\) is algebraic over \(k\). This ring of global sections is a field.

**Proof.** A section \(f\) defines a morphism \(Y\to\mathbf A^1_k\), and hence a morphism \(Y\to\mathbf P^1_k\) whose image misses infinity. A morphism from a proper \(k\)-scheme to a separated \(k\)-scheme is proper: its graph is a closed immersion into the product, followed by the base change of the proper map \(Y\to\operatorname{Spec}k\). Its image in \(\mathbf P^1_k\) is therefore closed.

If \(f\) were transcendental over \(k\), the homomorphism \(k[T]\to k(Y)\), \(T\mapsto f\), would be injective. The generic point would map to the generic point of \(\mathbf A^1_k\), so that closed image in \(\mathbf P^1_k\) would be all of \(\mathbf P^1_k\). It would contain infinity, a contradiction. Thus \(f\) is algebraic.

The section ring embeds in \(k(Y)\). For a nonzero algebraic element, its minimal polynomial has nonzero constant coefficient; solving that equation for its inverse expresses the inverse as a polynomial in the element over \(k\). The inverse is again a global section. Thus the section ring is a field. \(\square\)

No theorem about coherent cohomology or finite-dimensional global sections is needed here.

**Lemma 1.2c.** Let \(A\) be a finitely generated integral \(k\)-algebra, and let \(F=\operatorname{Frac}A\). There are finitely many discrete valuations
\[
v_1,\ldots,v_r:F^*\longrightarrow\mathbf Z
\tag{1.C2}
\]
such that every \(a\in A^*\) with \(v_j(a)=0\) for all \(j\) is algebraic over \(k\).

**Proof.** Embed \(\operatorname{Spec}A\) in affine space, and take its reduced projective closure \(Z\). It is integral. Let \(Y\to Z\) be its normalization, finite by the normalization contract stated above. Then \(Y\) is normal, integral, proper and of finite type over \(k\), with function field \(F\). Let \(U\subset Y\) be the inverse image of \(\operatorname{Spec}A\).

The complement \(Y\setminus U\) has finitely many irreducible components, because \(Y\) is Noetherian. List the generic points of those components which have codimension one as \(\xi_1,\ldots,\xi_r\). Their local rings are DVRs by Theorem 1.2 of the normal-ring lesson, giving (1.C2).

A unit \(a\in A^*\) pulls back to a unit on \(U\). At each codimension-one point in \(U\), both \(a\) and \(a^{-1}\) belong to its local ring. Every codimension-one point outside \(U\) is one of the \(\xi_j\): the irreducible divisor it defines is contained in the complement, whose component containing it must also have codimension one. If all \(v_j(a)\) vanish, \(a\) and \(a^{-1}\) belong to those local rings as well.

On an affine open \(\operatorname{Spec}B\subset Y\), algebraic Hartogs, Theorem 3.3 of the normal-ring lesson, now puts both rational functions in \(B\): they belong to every height-one localization of the Noetherian normal domain \(B\). These sections agree on overlaps because they are the same rational functions. They therefore give a global unit of \(Y\), which is algebraic over \(k\) by Lemma 1.2b. \(\square\)

The list is allowed to be empty. In that case the argument says that all the units under discussion extend to the proper model.

**Proposition 1.2d (units modulo integral constants).** Suppose \(X\) is nonempty, reduced, connected and quasi-compact, and locally of finite type over \(k\). Let \(K\) be the field (1.C1). Then
\[
\Gamma(X,\mathcal O_X)^*/K^*
\quad\text{is a finitely generated abelian group.}
\tag{1.C3}
\]

**Proof.** The scheme is Noetherian and has finitely many irreducible components \(X_1,\ldots,X_m\), taken with their reduced structures. For each component choose a nonempty affine open \(U_i=\operatorname{Spec}A_i\) of \(X_i\). The algebra \(A_i\) is a finitely generated integral \(k\)-algebra. Restriction of a global section of \(X_i\) to \(U_i\) is injective: a regular function on an integral scheme is determined by its value at the generic point.

Apply Lemma 1.2c to these finitely many algebras. Restrict global units to them and combine all their valuations into a homomorphism
\[
v:\Gamma(X,\mathcal O_X)^*\longrightarrow\mathbf Z^N.
\tag{1.C4}
\]
If \(v(f)=0\), the restriction of \(f\) to each \(U_i\), and hence to the function field of \(X_i\), satisfies a monic polynomial \(P_i\in k[T]\). The monic product \(P=\prod_iP_i\) annihilates \(f\) at every generic point of \(X\). A section on a reduced scheme which vanishes at all generic points is zero: on each affine open this is the intersection-of-minimal-primes characterization of the nilradical. Thus \(P(f)=0\) globally. We get \(f\in K^*\).

Conversely, a nonzero element \(c\in K\) is a unit by Lemma 1.2a. Its image in each normal proper model is algebraic over \(k\), and it and its inverse are integral over every local ring of that model. Normality puts them in those rings. Each boundary valuation therefore vanishes on \(c\). We have proved
\[
\ker v=K^*.
\]
Consequently (1.C3) embeds in \(\mathbf Z^N\). Every subgroup of a finitely generated free abelian group is finitely generated. For completeness, induction on \(N\) proves this: project the subgroup to the last copy of \(\mathbf Z\), choose a lift of its positive generator if the image is nonzero, and combine that lift with a generating list for the kernel furnished by induction. This proves (1.C3). \(\square\)

This proof covers nonseparated \(X\). Only the chosen affine parts of its finitely many components were compactified; no separated compactification of the whole scheme was assumed.

#### Uniqueness of the field of integral constants

We include the algebra fact used to turn finite generation of units into an algebraic extension.

**Lemma 1.2e (Zariski's lemma).** A field \(L\) which is a finitely generated algebra over a field \(l\) is finite over \(l\).

**Proof.** Choose a maximal algebraically independent subset \(t_1,\ldots,t_d\) of a finite algebra generating list. The remaining generators \(a_1,\ldots,a_s\) are algebraic over \(l(t_1,\ldots,t_d)\). Their finitely many monic equations have coefficients in
\[
R=l[t_1,\ldots,t_d,1/g]
\]
for one nonzero polynomial \(g\). Thus \(L=R[a_1,\ldots,a_s]\) is integral over \(R\). The equality holds because \(L\) was generated as an \(l\)-algebra by the displayed list, and \(1/g\) already lies in the field \(L\).

A subring over which a field is integral is a field. Indeed for \(0\ne r\in R\), a monic equation for \(r^{-1}\) in \(L\), multiplied by \(r^{n-1}\), expresses \(r^{-1}\) as an element of \(R\).

If \(d>0\), choose a monic irreducible polynomial \(h(t_1)\in l[t_1]\) not dividing \(g\). There are infinitely many irreducibles in \(l[t_1]\): a finite purported list has a product whose product-plus-one has an irreducible factor outside that list. Only finitely many can divide \(g\). The prime \((h)\) of the polynomial ring in \(d\) variables survives in \(R\), so \(R\) is not a field. This contradiction gives \(d=0\). The finitely many remaining algebraic generators make \(L/l\) finite. \(\square\)

This is also the existing subject of *The Nullstellensatz and Jacobson rings*, Theorem 1.1.

**Theorem 1.2f (the constant-field theorem).** Let \(X\) be a nonempty reduced connected scheme with two morphisms
\[
a:X\to\operatorname{Spec}k_1,\qquad
b:X\to\operatorname{Spec}k_2,
\]
both locally of finite type. Identify \(k_1,k_2\) with their images in \(\Gamma(X,\mathcal O_X)\). Their integral closures there are the same field.

**Proof in the quasi-compact case.** Write \(K_i\) for those closures and \(G=\Gamma(X,\mathcal O_X)^*\). Lemma 1.2a makes \(K_i\) fields, and Proposition 1.2d makes both \(G/K_i^*\) finitely generated. Put \(L=K_1\cap K_2\). It is a field, and the homomorphism
\[
K_1^*/L^*\longrightarrow G/K_2^*
\tag{1.C5}
\]
is injective. Its source is therefore finitely generated. Choose multiplicative generators \(\alpha_1,\ldots,\alpha_r\) modulo \(L^*\). Every nonzero element of \(K_1\) is a product of their integer powers times an element of \(L^*\), so
\[
K_1=L[\alpha_1,\alpha_1^{-1},\ldots,\alpha_r,\alpha_r^{-1}].
\]
Lemma 1.2e shows that \(K_1/L\) is finite. Interchanging the fields proves that \(K_2/L\) is finite too.

Every element of \(K_1\) is now integral over \(L\), hence over \(K_2\). The latter field is integrally closed inside the global section ring by the observation following Lemma 1.2a, so \(K_1\subset K_2\). The symmetric inclusion proves equality. \(\square\)

**Proof without quasi-compactness.** The scheme is locally Noetherian. Cover it by connected affine opens \(U_i\): the finitely many connected components of a Noetherian affine open are open and closed, hence affine. On each \(U_i\), the quasi-compact case gives the common field
\[
K_i\subset\Gamma(U_i,\mathcal O_X)
\]
of integral constants for the two field structures.

An intersection \(U_i\cap U_j\) is a quasi-compact open subset of the Noetherian \(U_i\). Decompose it into its finitely many nonempty connected components \(W_{ij\ell}\). The quasi-compact case gives a common constant field \(K_{ij\ell}\) on each. Restriction embeds \(K_i\) and \(K_j\) into \(K_{ij\ell}\): elements remain integral over either ground field, and a unital map from a field to the section ring of a nonempty scheme is injective.

Let \(K_{\mathrm{glue}}\) be the tuples \((f_i)\in\prod_iK_i\) whose restrictions agree on every \(W_{ij\ell}\). The sheaf condition identifies such a tuple with a unique global section \(f\). Fix \(i_0\) and a monic \(P\in k_1[T]\) annihilating \(f_{i_0}\).

The overlap graph of the covering is connected. Otherwise the unions of the opens belonging to two graph components would be disjoint nonempty opens partitioning \(X\). Along any finite edge path from \(i_0\) to \(i\), the equalities of the restrictions in the fields \(K_{ij\ell}\), and the injectivity of restriction, propagate \(P(f_{i_0})=0\) to \(P(f_i)=0\). Thus \(P(f)=0\) on every open and hence globally. So \(f\) is integral over \(k_1\). The same argument with \(k_2\) proves that it is integral over \(k_2\).

Conversely a global element integral over either ground field restricts to \(K_i\) on each open and satisfies the overlap equalities. The two global integral closures therefore both equal \(K_{\mathrm{glue}}\), and Lemma 1.2a makes this a field. \(\square\)

The nonempty hypothesis is necessary when talking about subfields of a section ring. The empty scheme has zero section ring and admits both field structures without such embeddings.

### 1.2. Field groupoids

**Lemma 1.3 (field groupoids with unramified stabilizer).** Let \(R\rightrightarrows u=\operatorname{Spec}K\) be a groupoid in algebraic spaces over a scheme \(S\), whose projections \(s,t\) are locally of finite type. Suppose its stabilizer

\[
G=R\times_{u\times_Su,\Delta}u
\]

is unramified over \(u\). Then \(R\) has dimension zero.

*Proof.* Choose a connected affine étale chart \(V\to R\) at the identity, with a point \(v\) mapping to it. This is possible after taking the connected component of an affine chart: the chart is Noetherian because it is of finite type over \(K\). Set \(D=\Gamma(V_{\mathrm{red}},\mathcal O)\). The two field structures \(s,t:K\to D\) are locally of finite type.

Theorem 1.2f gives the constant-field theorem needed here: on a reduced connected scheme locally of finite type over two fields, their integral closures in its ring of functions are the same field [Stacks, Tags 04MI, 04MK]. Write this common field as \(K_c\subset D\). Evaluation at \(v\) is injective on \(K_c\). The two maps \(K\to\kappa(v)\) agree, because \(v\) maps to the identity. They must therefore agree in \(D\). Thus \(V_{\mathrm{red}}\to R\) factors through \(G\).

The group \(G\), locally of finite type and unramified over \(K\), has dimension zero. The pullback \(V\times_RG\) is étale over \(G\), and its underlying set is all of \(V\), since it contains \(V_{\mathrm{red}}\). Thus \(V\), and hence \(R\), has dimension zero near the identity.

For an arbitrary arrow \(r\) over a field extension \(L\), composition with \(r^{-1}\) identifies its source fibre with the source fibre at its target and carries \(r\) to the identity. Extension of the ground field preserves relative dimension. Thus every point of every source fibre has dimension zero. The source is a field, so \(\dim R=0\). \(\square\)

*Reference:* [Stacks, Tags 04MQ, 06FF]. This extends the trivial-stabilizer field argument in Lesson 2 to an unramified stabilizer.

**Lemma 1.4 (an étale field chart for the restricted quotient).** Suppose (1.1) holds. Let \(u=\operatorname{Spec}K\to\mathcal X\) be the image of a closed point of an affine smooth chart. Put \(R=u\times_{\mathcal X}u\). Then there are a field \(K_0\), an algebraic stack \(\mathcal Z\), and maps

\[
\operatorname{Spec}K_0\longrightarrow\mathcal Z
\longrightarrow\mathcal X
\tag{1.2}
\]

such that the first map is surjective and étale, the second is a representable monomorphism locally of finite type, and \(|\mathcal Z|\) consists of the point represented by \(u\).

*Proof.* The full Isom spaces define the groupoid \(R\rightrightarrows u\). Its projections are locally of finite type: each factors through \(u\times_{\mathcal X}U\), using the finite type closed immersion \(u\to U\) and the smooth atlas. Over a field they are flat and locally of finite presentation. Its stabilizer is a base change of (1.1), hence unramified. Lemmas 1.3 and 1.2 make \(R\) a disjoint union of finite local Artinian \(K\)-schemes.

Let \(P=\operatorname{Spec}A\) be the component containing the identity. Its residue field is \(K\), with both field structures giving the identity on that residue. Thus

\[
A/(s(a)-t(a):a\in K)
\tag{1.3}
\]

is a local Artinian algebra with residue \(K\). It is also the identity component of the unramified stabilizer, so it equals \(K\). The map \(P\to u\times_Su\) is of finite type and universally injective: it has one point and induces the identity residue field at its image. Its fibre there is the reduced field (1.3); the unramified fibre criterion makes this map unramified. An unramified universally injective morphism is a monomorphism.

The component \(P\) is a subgroupoid. Inversion preserves its single point. The scheme \(P\times_{s,u,t}P\) is Artinian local with residue \(K\), so composition maps its single point to the identity and factors through the open component \(P\). Units are already in \(P\). Its two projections are finite locally free over \(K\). Thus it is a finite flat equivalence relation.

Lesson 2's affine quotient gives

\[
\bar u=u/P=\operatorname{Spec}K_0,\qquad
P=u\times_{\bar u}u.
\tag{1.4}
\]

The invariant subring \(K_0\subset K\) for **\(P\)** is a field: if a nonzero element has equal images under \(s,t\), its inverse does too. The quotient map is finite faithfully flat.

We can divide the whole groupoid by \(P\), using Lesson 2, Lemma 3.2. Its endpoint map is separated and locally quasi-finite because \(R\) is a separated zero-dimensional scheme over either field structure. This gives a scheme groupoid \(\bar R\rightrightarrows\bar u\) with

\[
R=u\times_{\bar u,\bar t}\bar R
       \times_{\bar s,\bar u}u.
\tag{1.5}
\]

The division proof descends arrows by changing both endpoints, and supplies composition, units and inverses; it applies to groupoids with stabilizers as well as equivalence relations. The two projections of \(\bar R\) are flat and locally of finite presentation by fppf descent. The unit \(\bar u\to\bar R\) is open, since its pullback in (1.5) is the open component \(P\subset R\).

These projections are étale. Indeed, in a geometric source fibre, translation by any arrow carries that arrow to the identity in another source fibre. The open unit gives that identity the open neighbourhood \(\operatorname{Spec}\bar K\). Hence all geometric fibres are reduced and zero-dimensional. Flatness and local finite presentation now imply étaleness.

The étale groupoid theorem from Lesson 5 makes

\[
\mathcal Z=[\bar u/\bar R]\simeq[u/R]
\tag{1.6}
\]

algebraic, with a surjective étale atlas \(\bar u\). The equivalence in (1.6) can also be checked directly: an object locally lifts through the faithfully flat map \(u\to\bar u\), and (1.5) identifies all Isom arrows between its lifts. Stack descent then gives both full faithfulness and essential surjectivity.

The map \([u/R]\to\mathcal X\) is fully faithful, because \(R\) was defined by **all** isomorphisms between objects from \(u\); the statement is checked on local representatives and then on their Isom sheaves. Lesson 5's faithfulness criterion makes it representable, and full faithfulness makes it a monomorphism. It is locally of finite type: the cover \(u\to\mathcal Z\) is flat, surjective and locally finitely presented, and its composite into \(\mathcal X\) is locally of finite type. This property descends on the source for fppf covers [Stacks, Tag 036O], applied on scheme charts.

Finally \(u\to\mathcal Z\) is surjective and \(u\) has one point. Thus \(|\mathcal Z|\) is a singleton, with the indicated image. \(\square\)

This proof uses no theorem asserting algebraicity of arbitrary flat groupoid quotients. Its quotient becomes algebraic after the identity component has been divided out and the projections have been proved étale.

## 2. Cutting an étale atlas

We record exactly how scheme slicing passes to stacks.

**Lemma 2.1 (slicing and the étale locus).** Let \(p:U\to\mathcal X\) be representable, flat and locally of finite presentation, with \(U\) a scheme. Let \(x:\operatorname{Spec}L\to\mathcal X\), and put \(F=U\times_{\mathcal X}\operatorname{Spec}L\).

1. If functions \(f_1,\ldots,f_d\) from \(U\) give a regular sequence at a point of \(F\), then, after shrinking \(U\) around its image, \(V(f_1,\ldots,f_d)\to\mathcal X\) is flat and locally of finite presentation.
2. The étale locus of \(p\) is an open subset of \(U\). Its pullback to any such field test is the étale locus of \(F\to\operatorname{Spec}L\).

*Proof.* Choose a smooth scheme atlas \(B\to\mathcal X\). After extending \(L\), the object \(x\) lifts to \(B\). The field fibre of \(U\times_{\mathcal X}B\to B\) is then a field extension of \(F\). Flat extension preserves the regular sequence. Choose an étale scheme chart of \(U\times_{\mathcal X}B\) at a point over the chosen fibre point.

The scheme slicing theorem [Stacks, Tag 06LI] gives an open neighbourhood in this chart on which the zero scheme of the functions is flat and locally finitely presented over \(B\). Its map to \(U\) is smooth, hence open, with an image neighbourhood of the required point. On the zero schemes it is a smooth cover of that neighbourhood. Its composite to \(\mathcal X\) is flat and locally finitely presented. These two properties descend on the source of an fppf cover, as is seen after testing by a scheme atlas; local finite presentation uses [Stacks, Tag 036N]. Thus the zero scheme over the image neighbourhood has the asserted properties. Its presentation is finite because only finitely many equations were added. This proves 1.

For 2, on \(U_B=U\times_{\mathcal X}B\) use the ordinary étale locus of the flat locally finitely presented map \(U_B\to B\). For such a map, being étale at a point is equivalent to its geometric fibre being smooth of dimension zero there. This criterion shows both openness and compatibility of the locus with arbitrary base change. On the common refinement \(B\times_{\mathcal X}B\), the two pullbacks of \(U_B\) are canonically isomorphic over that refinement. Their étale loci therefore agree. Descent for opens under the smooth cover \(U_B\to U\) gives an open subset of \(U\). On this subset every atlas test is étale; outside it none of the tests at the corresponding geometric point is étale. Applying the same refinement argument with the field test proves the stated pullback equality. \(\square\)

**Theorem 2.2 (the Deligne–Mumford criterion).** For an algebraic stack \(\mathcal X/S\), the following are equivalent:

1. Its diagonal is unramified.
2. It is Deligne–Mumford.
3. A scheme \(W\) admits a representable, surjective étale morphism \(W\to\mathcal X\).

No separation or Noetherian hypothesis is imposed [Stacks, Tag 06N3].

*Proof.* Conditions 2 and 3 are the definition in Lesson 5. Suppose 3. Set \(E=W\times_{\mathcal X}W\). Its projections to \(W\) are étale. The endpoint morphism \(E\to W\times_SW\) is unramified: its composite with either projection to \(W\) is unramified, and the scheme permanence property for unramified maps gives the assertion, checked on étale charts. It is the base change of the diagonal by the fppf cover \(W\times_SW\to\mathcal X\times_S\mathcal X\). Unramifiedness descends, giving 1.

Assume 1. We construct an étale map whose image contains each finite type point from Lemma 1.1. For such a point, Lemma 1.4 gives an étale field cover \(\operatorname{Spec}L\to\mathcal Z\) of a representable monomorphism \(\mathcal Z\to\mathcal X\) locally of finite type. A representable monomorphism locally of finite type is unramified: its diagonal is an isomorphism. Hence the composite

\[
x:\operatorname{Spec}L\longrightarrow\mathcal X
\tag{2.1}
\]

is unramified and represents the required point.

Choose a smooth scheme atlas \(U\to\mathcal X\) meeting this point. The space \(F=U\times_{\mathcal X}\operatorname{Spec}L\) is nonempty, smooth over \(L\), and unramified over \(U\), the last assertion being a base change of (2.1). Choose a nonempty affine étale scheme chart \(V\to F\). Then \(V/L\) is smooth and \(V\to U\) is unramified. A nonempty smooth scheme over a field has a closed point \(v\) whose residue field is finite separable over that field. Choose one and write \(u\) for its image in \(U\).

The local ring \(\mathcal O_{V,v}\) is regular. Since \(V\to U\) is unramified, the local criterion gives

\[
\mathfrak m_u\mathcal O_{V,v}=\mathfrak m_v.
\]

Choose \(d=\dim\mathcal O_{V,v}\) elements \(f_1,\ldots,f_d\) in \(\mathfrak m_u\) whose images form a basis of \(\mathfrak m_v/\mathfrak m_v^2\). They are regular parameters of this regular local ring. After shrinking \(U\), they are functions on \(U\). Their pullbacks give a regular sequence at the corresponding point of \(F\), since \(V\to F\) is étale and this condition is faithfully flat local at the point.

Put \(U_0=V(f_1,\ldots,f_d)\). Lemma 2.1 lets us shrink around \(u\) so that \(U_0\to\mathcal X\) is flat and locally finitely presented. The pullback of its fibre to \(V\) has local ring

\[
\mathcal O_{V,v}/(f_1,\ldots,f_d)=\kappa(v),
\tag{2.2}
\]

a finite separable extension of \(L\). Thus this fibre is unramified at the point, and, being flat and locally finitely presented over a field, is étale there. Lemma 2.1's étale-locus assertion provides an open neighbourhood \(W_x\subset U_0\) which is étale over \(\mathcal X\). It contains \(u\), so its image contains the required point \(x\).

Take the disjoint union of these \(W_x\) for the finite type points supplied by affine smooth charts. Their images are open because their maps are étale. Their union contains all the points in Lemma 1.1, so its closed complement is empty. Consequently

\[
\coprod_x W_x\longrightarrow\mathcal X
\]

is a surjective étale scheme atlas. This proves 3. \(\square\)

For a relative version, call \(f:\mathcal X\to\mathcal Y\) **DM** when its relative diagonal is unramified. Base change preserves this condition. If \(\mathcal Y\) is Deligne–Mumford, then \(\mathcal X\) is Deligne–Mumford: its diagonal factors through the relative diagonal and a base change of \(\Delta_{\mathcal Y}\), so is unramified. In particular a DM morphism tested by an algebraic space has a Deligne–Mumford source and an étale scheme atlas [Stacks, Tag 0CIA].

An unramified diagonal need not be proper or separated. The doubled-origin classifying stack of Lesson 5, Exercise 8.3, already has an étale atlas and a nonseparated diagonal.

## 3. Classifying stacks and quotient stacks

Let \(G\to S\) be a group scheme, flat and locally of finite presentation. The stack \(BG\) classifies right fppf \(G\)-torsors. We use the following theorem here and prove it in the next lesson:

**Flat groupoid theorem, stated.** A groupoid in algebraic spaces whose source and target are flat and locally of finite presentation has an algebraic quotient stack [Stacks, Tag 06FI].

It applies to \(G\rightrightarrows S\), so \(BG\) is algebraic. It also makes \([X/G]\) algebraic for an action on any algebraic space \(X/S\) under the same hypotheses on \(G\). The quotient-torsor equivalence, including descent and all arrows, was proved in Lesson 4 [Stacks, Tags 04UV, 04WM].

**Proposition 3.1.** For \(G\) flat and locally of finite presentation over \(S\),

\[
BG\text{ is Deligne–Mumford}
\quad\Longleftrightarrow\quad
G\to S\text{ is unramified}.
\tag{3.1}
\]

If \(G\) is finite étale and acts on a scheme \(X/S\), then \([X/G]\) is Deligne–Mumford.

*Proof.* The base change of \(\Delta_{BG}\) by the pair of trivial torsors is

\[
\operatorname{Isom}_S(G,G)=G\longrightarrow S.
\]

The identification sends a group element to left translation of the right torsor. If \(BG\) is Deligne–Mumford, Theorem 2.2 makes this test unramified.

Conversely, flatness, local finite presentation and unramifiedness make \(G\to S\) étale. For a torsor \(P/T\), the base change of \(S\to BG\) is \(P\to T\): a point of \(P\) is a trivialization with its specified comparison. It is represented by an algebraic space by Lesson 4's torsor theorem. Locally it is \(G_T\to T\), hence étale and surjective. Therefore \(S\to BG\) is an étale scheme atlas.

For the action quotient, the base change of \(X\to[X/G]\) by an object \((P,\phi)/T\) is again \(P\to T\). If \(G\) is finite étale this is finite étale and surjective, so \(X\) is an étale atlas. \(\square\)

The last argument works for every étale group scheme, without finiteness or separation. The original Deligne–Mumford Example (4.8) assumes an étale, separated group scheme of finite type and a scheme \(X\). Its atlas is of the same torsor form; that example has a smaller range of hypotheses than (3.1).

### 3.1. A finite group with infinitesimal symmetry

Let \(k\) have characteristic \(p>0\). The scheme

\[
\mu_p=\operatorname{Spec}k[z]/(z^p-1)
      =\operatorname{Spec}k[\eta]/(\eta^p)
\]

is finite locally free of rank \(p\). Thus \(B\mu_p\) is algebraic by the stated flat groupoid theorem. It is not Deligne–Mumford.

Indeed, over \(D=k[\epsilon]/(\epsilon^2)\), the elements \(1\) and \(1+\epsilon\) give distinct \(D\)-points of \(\mu_p\) with the same reduction. The equality \((1+\epsilon)^p=1\) holds also for \(p=2\). This violates formal unramifiedness. Proposition 3.1 excludes a Deligne–Mumford atlas.

There is only one geometric point of \(\mu_p\). Counting geometric automorphism *points* would consequently miss the obstruction. The stabilizer group scheme, including its nilpotents, is what the diagonal detects.

### 3.2. A square-root quotient

Let \(\mu_2\) act on \(\mathbf A^1_S\) by scalar multiplication. The quotient \([\mathbf A^1/\mu_2]\) is algebraic over every \(S\); it is Deligne–Mumford when \(2\) is invertible on \(S\). Its objects can be described as

\[
(L,\alpha,s),\qquad
\alpha:L^{\otimes2}\xrightarrow{\sim}\mathcal O_T,\quad
s\in\Gamma(T,L).
\tag{3.2}
\]

A local frame satisfying \(\alpha(\ell^2)=1\) defines a point of \(\mathbf A^1\). Such frames form a \(\mu_2\)-torsor: a frame of an arbitrary line bundle can be normalized after adjoining a square root of a unit, a finite free fppf cover. Changes of normalized frame multiply its coordinate by \(\mu_2\). Conversely the associated line bundle of a torsor supplies (3.2). These constructions preserve sections and all isomorphisms and are inverse by descent.

The zero section has stabilizer \(\mu_2\). On the open where \(s\) is a frame, every stabilizer is trivial. More explicitly, the squaring map

\[
\mathbf G_m\longrightarrow\mathbf G_m,\qquad z\longmapsto z^2
\]

is an fppf \(\mu_2\)-torsor over every base. Lesson 2's free quotient gives \([\mathbf G_m/\mu_2]\simeq\mathbf G_m\). Thus the stack remembers a square-root symmetry along the origin and is a space away from it. On any characteristic-two fibre its origin stabilizer is nonunramified, so the whole quotient over such a field is not Deligne–Mumford.

This is the local model of a root stack along a divisor. If a divisor has local equation \(a\), its order-\(n\) root stack is

\[
\left[
\operatorname{Spec}A[z]/(z^n-a)\big/\mu_n
\right],
\tag{3.3}
\]

with \(\mu_n\) scaling \(z\). To see the description, use a root line bundle with section and an identification of its \(n\)-th power with the divisor line bundle, taking the \(n\)-th power of the section to the divisor section. Normalize a frame fppf locally; the coefficient then satisfies \(z^n=a\), and its remaining frame changes are \(\mu_n\). This proves the local quotient by the same descent argument as (3.2).

For \(n\) invertible, this chart has a finite étale group and is Deligne–Mumford. If the residue characteristic divides \(n\), its stabilizer along the divisor is nonunramified. This states the characteristic hypothesis omitted by an informal picture of “inserting a stacky point”; Behrend's orbifold discussion makes the characteristic-zero hypothesis at its beginning.

## 4. The weighted projective line

Put \(U=\mathbf A^2_S\setminus V(x,y)\), and let \(\mathbf G_m\) act by

\[
\lambda\cdot(x,y)=(\lambda x,\lambda^2y).
\]

The weighted projective line is

\[
\mathbf P_S(1,2)=[U/\mathbf G_m].
\tag{4.1}
\]

It is algebraic because the acting group is smooth. Its points over a scheme \(T\) are a line bundle \(L\), a section \(x\) of \(L\), and a section \(y\) of \(L^{\otimes2}\) which do not vanish together at any point. A frame turns them into the two coordinates in (4.1); frame changes give the action, with the right-torsor convention of Lesson 4.

For a geometric representative \((x,y)\), the stabilizer is defined scheme-theoretically by

\[
(\lambda-1)x=0,\qquad(\lambda^2-1)y=0.
\tag{4.2}
\]

If \(x\ne0\), it is the trivial group. If \(x=0\), then \(y\ne0\), and it is \(\mu_2\). These equations also describe stabilizers of nonconstant families; nilpotent \(x\) can impose an intermediate equation on \(\mu_2\), so the geometric list should not be substituted for the whole group scheme over \(T\).

There are two useful open charts. On \(D(x)\), setting \(x=1\) uses a unique scalar, and the invariant coordinate is \(y/x^2\). Hence

\[
[D(x)/\mathbf G_m]\simeq\mathbf A^1_S.
\tag{4.3}
\]

On \(D(y)\), choose a square root of the invertible coordinate \(y\) fppf locally and scale it to \(1\). The remaining choice is exactly \(\mu_2\), acting on the normalized coordinate \(x\). The same local full-faithfulness and effectivity argument as (3.2) gives

\[
[D(y)/\mathbf G_m]\simeq[\mathbf A^1_S/\mu_2].
\tag{4.4}
\]

The two descriptions agree on their common open, where \(x,y\) are invertible. Equations (4.3)–(4.4) prove that \(\mathbf P_S(1,2)\) is Deligne–Mumford when \(2\) is invertible. Over a field of characteristic two, its point represented by \((0,1)\) has stabilizer \(\mu_2\); pulling back the diagonal to that object and using Theorem 2.2 proves it is not Deligne–Mumford.

Over an algebraically closed field with \(2\ne0\), (4.4) describes one order-two stacky point. The graded scheme \(\operatorname{Proj}\mathcal O_S[x,y]\), with degrees \(1,2\), is \(\mathbf P^1_S\): taking the second Veronese ring gives the polynomial ring \(\mathcal O_S[x^2,y]\) with both generators in the same degree. Its coordinates are \(y/x^2\) on the first chart and \(x^2/y\) on the second. The stack chart above the second coordinate retains the square-root symmetry.

## 5. Elliptic curves are Deligne–Mumford in every characteristic

Write

\[
W=\operatorname{Spec}
\mathbf Z[a_1,a_2,a_3,a_4,a_6,\Delta^{-1}]
\]

for the general Weierstrass parameter space, and

\[
\Gamma=\operatorname{Spec}\mathbf Z[u,u^{-1},r,s,t]
\]

for its coordinate-change group. Lesson 5 proved, over arbitrary bases, that

\[
\mathcal M_{1,1}\simeq[W/\Gamma],
\qquad W\longrightarrow\mathcal M_{1,1}
\text{ is representable, smooth and surjective}.
\tag{5.1}
\]

In particular the atlas includes an identification of the parameterized equation with the given elliptic curve. The discriminant criterion and normal-form proof work in characteristics two and three as well. This supplies the smooth quotient and atlas parts of [Stacks, Tags 072T, 072U] with full proofs.

**Lemma 5.1.** For a smooth proper geometrically connected genus-one curve \(E/k\) with a marked point \(e\), over an algebraically closed field of any characteristic,

\[
H^0(E,T_E(-e))=0.
\tag{5.2}
\]

*Proof.* The Weierstrass normal form embeds \(E\) as a smooth plane cubic. Its conormal sequence is

\[
0\longrightarrow\mathcal O_E(-3)
\longrightarrow\Omega_{\mathbf P^2/k}|_E
\longrightarrow\Omega_{E/k}\longrightarrow0.
\]

Taking determinants and using the Euler sequence of projective space, whose rank-two cotangent determinant is \(\mathcal O_{\mathbf P^2}(-3)\), gives \(\Omega_{E/k}\simeq\mathcal O_E\). Thus \(T_E(-e)\simeq\mathcal O_E(-e)\). This is a submodule of \(\mathcal O_E\), and a global section would be a global regular function vanishing at \(e\). The genus-one cohomology in Lesson 5 gives \(H^0(E,\mathcal O_E)=k\). Only the zero constant vanishes there. \(\square\)

An automorphism of \(E_{k[\epsilon]/(\epsilon^2)}\) reducing to the identity acts locally on functions by

\[
f\longmapsto f+\epsilon D(f).
\]

The condition that it preserve products says that \(D\) is a \(k\)-derivation. Compatibility on overlaps gives a global tangent section. Preserving the marked section says that \(D\) vanishes at \(e\). Conversely any such derivation gives an infinitesimal pointed automorphism, with inverse \(1-\epsilon D\). Thus (5.2) is exactly the absence of infinitesimal pointed automorphisms, not merely a statement about the number of geometric automorphisms.

**Theorem 5.2.** The stack \(\mathcal M_{1,1}\) is Deligne–Mumford over \(\operatorname{Spec}\mathbf Z\).

*Proof.* By (5.1) it is algebraic. Test its diagonal on the smooth cover \(W\times W\). Its Isom space is the scheme

\[
R=\Gamma\times W,\qquad
R\longrightarrow W\times W,\quad
(\gamma,a)\longmapsto(a,\gamma a),
\tag{5.3}
\]

using the left-action convention of Lesson 5. This endpoint map is of finite presentation: the parameter schemes and coordinate formulas are of finite presentation over \(\mathbf Z\), and the equations for the two endpoints give a finite presentation over \(W\times W\).

At a geometric point of \(R\), the relative tangent space of (5.3) is the space of infinitesimal isomorphisms with both equations fixed. Compose with the inverse of the chosen isomorphism. This identifies it with infinitesimal pointed automorphisms of one elliptic curve, which vanish by Lemma 5.1.

The relative cotangent module is finite. Its fibre at every geometric point is zero, since its dual is this zero tangent space. Nakayama's lemma makes the module zero everywhere. The finite-presentation map (5.3) is therefore unramified. Unramifiedness is fppf local on the target, so the diagonal of \(\mathcal M_{1,1}\) is unramified. Theorem 2.2 supplies an étale scheme atlas. \(\square\)

The smooth atlas \(W\) has relative dimension four over the stack. The theorem produces a different, étale atlas; it does not assert that the five-parameter Weierstrass family is itself étale.

### 5.1. Short equations after inverting six

Over \(B=\operatorname{Spec}\mathbf Z[1/6]\), complete the square and translate \(x\) to obtain

\[
E_{a,b}: y^2=x^3+ax+b,\qquad
V=\operatorname{Spec}\mathbf Z[1/6][a,b,(4a^3+27b^2)^{-1}].
\tag{5.4}
\]

The discriminant is \(-16(4a^3+27b^2)\). The unique pointed coordinate changes from Lesson 5 have \(s=r=t=0\) between two short equations: the \(xy\) coefficient forces \(s=0\), the \(x^2\) coefficient then forces \(r=0\), and the \(y\) coefficient forces \(t=0\), using respectively the units \(2,3,2\). The remaining change is \(x=u^2x'\), \(y=u^3y'\).

Consequently, with the positive-weight left action,

\[
\mathcal M_{1,1}\times B\simeq[V/\mathbf G_m],
\qquad
u\cdot(a,b)=(u^4a,u^6b).
\tag{5.5}
\]

Local short equations give essential surjectivity; unique changes give full faithfulness of the action prestack, and its coordinate cocycles descend. This verifies the equivalence on objects and arrows, not just on isomorphism classes over fields.

The stabilizer of a geometric equation is

\[
u^4a=a,\qquad u^6b=b.
\tag{5.6}
\]

If \(a,b\ne0\), both conditions give \(\mu_2\), because \((u^6-1)-u^2(u^4-1)=u^2-1\). If \(b=0\), then \(a\ne0\) and the stabilizer is \(\mu_4\). If \(a=0\), then \(b\ne0\) and it is \(\mu_6\). These are group-scheme identifications. The discriminant excludes \(a=b=0\), and inverting six makes all three stabilizers étale.

The invariant from Lesson 5 specializes to

\[
j=1728\,\frac{4a^3}{4a^3+27b^2}.
\tag{5.7}
\]

Its numerator and denominator both have weight twelve, so it is invariant. The exceptional loci are \(a=0\), with \(j=0\), and \(b=0\), with \(j=1728\). The short presentation and this stabilizer list have only been used over \(B\); Theorem 5.2, with the general equation, treats the remaining characteristics.

## 6. What a moduli space forgets

An algebraic space has discrete point groupoids. A morphism from a stack to a space consequently sends every automorphism to the identity. A moduli space is a universal way of doing this within a specified class of targets.

**Definition 6.1.** A morphism \(f:\mathcal X\to M\) to an algebraic space is a **categorical moduli space** if, for every algebraic space \(N\), composition gives a bijection

\[
\operatorname{Mor}(M,N)\xrightarrow{\sim}
\{\text{morphisms }\mathcal X\to N\text{ up to 2-isomorphism}\}.
\tag{6.1}
\]

Here every Hom groupoid on the right is a setoid: a comparison, when it exists, is unique. The map is **uniform categorical** if the same property holds after every flat morphism \(M'\to M\) of algebraic spaces [Stacks, Tag 0DUF].

The adjective “uniform” concerns flat base changes. Universality under arbitrary base change is a stronger assertion and is not built into this definition. One can also restrict the test targets to a full subcategory, such as schemes or separated algebraic spaces. The chosen target category belongs to the definition.

A categorical moduli space is unique up to a unique isomorphism. Indeed its two universal properties give maps between any two candidates. Their composites induce the same maps from \(\mathcal X\) as the identity, so uniqueness forces both composites to be the identity.

**Proposition 6.2 (quotient comparison).** For an algebraic quotient \(\mathcal X=[U/R]\), with \(s,t\) flat and locally finitely presented, a morphism \(\mathcal X\to N\) to an algebraic space is equivalent to a morphism \(\phi:U\to N\) satisfying

\[
\phi s=\phi t.
\tag{6.2}
\]

Consequently \(\mathcal X\to M\) is categorical if and only if \(U\to M\) is a categorical quotient of the groupoid. The same equivalence holds for the uniform versions and for a specified full subcategory of targets.

*Proof.* Restriction of a map to the objects \(U\) gives \(\phi\). Every arrow in \(R\) gives the unique equality between its two images in the discrete target, so (6.2) holds.

Conversely, (6.2) defines a functor from the action prestack into the discrete stack \(N\): on objects use \(\phi\), on arrows use the identity at their common image. The composition and unit laws hold because there is only that one arrow. The stackification universal property proved in Lesson 4 extends this functor uniquely up to the unique comparison to \([U/R]\). Equivalently, local lifts of an object to \(U\) give maps to \(N\) which agree on overlaps by (6.2); the sheaf condition glues them. This description also verifies compatibility with pullback and all arrows.

Thus maps to every target space, and their factorization through \(M\), agree in the two formulations. After a morphism \(M'\to M\), put

\[
U'=M'\times_MU,\qquad R'=M'\times_MR.
\]

The pulled-back atlas is flat, surjective and locally finitely presented, and its full presentation is \([U'/R']\simeq M'\times_M\mathcal X\), by the flat-presentation argument of Lesson 5. The same correspondence applies. Applying it to each flat \(M'\to M\) proves the uniform assertion. Restricting the targets makes no change to the proof. \(\square\)

There are two conventions to distinguish in the named sources:

- Behrend's **coarse moduli scheme**, Definition 3.39, is a scheme target, initial among maps to schemes, and remains so after flat scheme maps to that target. His later Definition 3.45 uses separated algebraic spaces for a separated Deligne–Mumford stack. A geometric-point bijection is a conclusion in Proposition 3.46, rather than an extra condition in Definition 3.39.
- Deligne–Rapoport's **coarse moduli space**, I.8.1, is initial among maps to algebraic spaces over the base and induces a bijection on isomorphism classes over every algebraically closed field and the points of the space over that field. This point condition is included in their definition. Their I.8.2.3 discusses flat base change.

We use “categorical” and “uniform categorical” as in Definition 6.1, and specify the coarse convention when invoking the elliptic-curve theorem.

### 6.1. Finite inertia and the coarse space

Recall that the fibre of \(\mathcal I_{\mathcal X}\to\mathcal X\) at an object \(x/T\) is \(\operatorname{Aut}_T(x)\). We now construct its coarse space when this entire inertia morphism is finite. The construction preserves the full infinitesimal stabilizer in local charts before passing to invariant functions. It applies to \(B\mu_p\) as well as to Deligne–Mumford stacks. The following treatment follows the Stacks Project authors' finite-inertia proof, cited below.

#### Finite-flat charts and their invariant functions

Call a stack \(\mathcal Y\) a **finite-flat affine chart** when it has a representable, finite locally free, surjective map \(U\to\mathcal Y\) from an affine scheme. Then
\[
\mathcal Y=[U/R],\qquad R=U\times_{\mathcal Y}U,
\]
and \(U=\operatorname{Spec}A\), \(R=\operatorname{Spec}B\) are affine, with both source and target finite locally free. This follows from the flat presentation theorem in *Artin's axioms*, Theorem 6.6, and from descent of finiteness. Conversely such a presentation supplies a finite-flat affine chart.

Write
\[
C=\{a\in A:s^\sharp(a)=t^\sharp(a)\},\qquad M=\operatorname{Spec}C.
\tag{6.K1}
\]
The invariant map \(U\to M\) gives \(\pi:\mathcal Y\to M\) by Proposition 6.2 of *Quotient stacks and Deligne–Mumford stacks*.

**Lemma 6.3.** The inclusion \(C\subset A\) is integral. If \(D\) is a flat \(C\)-algebra, the invariant ring of the base-changed groupoid is \(D\).

**Proof.** The rank of \(s\) is constant along an orbit: composition by an arrow identifies the two source fibres after a common field extension. The rank strata are invariant open-and-closed subschemes; there are finitely many because \(U\) is affine. Their idempotents lie in \(C\), so work on one stratum of rank \(r>0\).

For \(a\in A\), multiplication by \(t^\sharp(a)\) on the finite locally free \(s^\sharp(A)\)-module \(B\) has a monic characteristic polynomial. Composition identifies its two pullbacks, preserving target functions. Its coefficients therefore lie in \(C\). Cayley–Hamilton and the identity arrow give a monic equation for \(a\) over \(C\). This proves integrality.

Finally,
\[
0\longrightarrow C\longrightarrow A
 \xrightarrow{\,s^\sharp-t^\sharp\,}B
\]
is exact as a sequence of \(C\)-modules. Flat tensoring preserves its kernel, proving the second assertion. These are the invariant-polynomial and flat-kernel arguments already proved in *The bootstrap theorem*, Appendix A; they use the groupoid laws, without the additional equivalence-relation hypothesis needed for that appendix's stronger effective fppf quotient conclusion. \(\square\)

An arbitrary base change need not preserve the invariant ring, but its discrepancy has no effect on points.

**Lemma 6.4.** For a \(C\)-algebra \(D\), let \(C_D\) be the invariant ring in \(A_D=A\otimes_C D\). Then \(\operatorname{Spec}C_D\to\operatorname{Spec}D\) is a universal homeomorphism. For every algebraically closed field \(k\),
\[
M(k)=U(k)/R(k).
\tag{6.K2}
\]

**Proof.** First suppose the rank is \(r\). Choose a polynomial \(C\)-algebra \(P\) mapping onto \(D\). For \(f\in C_D\), lift \(f\) to \(g\in A\otimes_C P\). The norm
\[
\operatorname{Norm}_{s}\bigl(X-t^\sharp(g)\bigr)
\]
has invariant coefficients, by the same composition calculation as in Lemma 6.3. Invariants commute with the flat extension \(C\to P\), so this polynomial belongs to \(P[X]\). Its image over \(D\) is \((X-f)^r\), because \(s^\sharp(f)=t^\sharp(f)\). Thus \((X-f)^r\) has all coefficients in the image of \(D\). With several rank strata, take a common positive multiple of their ranks and combine the polynomials along the corresponding idempotents.

It follows that \(C_D\) is integral over the image of \(D\). The map \(\operatorname{Spec}A_D\to\operatorname{Spec}D\) is surjective, since \(C\subset A\) is integral and lying over survives base change. Its factorization through \(\operatorname{Spec}C_D\) shows that every kernel element of \(D\to C_D\) is nilpotent and that the latter map is surjective on spectra.

If two maps from \(C_D\) into an algebraically closed field agree on \(D\), apply them to the polynomial \((X-f)^n\) with coefficients in \(D\). The resulting monic polynomials are equal and each has a single root, so the two values of \(f\) coincide. This proves universal injectivity. Integral, surjective, universally injective morphisms are universal homeomorphisms.

For (6.K2), surjectivity follows because \(A\otimes_C k\) is a nonzero integral \(k\)-algebra; its residue fields are \(k\). Suppose \(u_0,u_1\in U(k)\) have the same image in \(M(k)\). The orbit of \(u_1\) is finite, since the source fibre is finite. If it does not contain \(u_0\), choose \(f\in A\otimes_C k\) vanishing at \(u_0\) and nonvanishing at every point of that orbit, using the Chinese remainder theorem. The invariant norm \(N_s(t^\sharp f)\) vanishes at \(u_0\) and is nonzero at \(u_1\).

On the other hand the preceding polynomial conclusion for \(D=k\) says that every invariant element has a positive power in \(k\). In characteristic zero the coefficient of \(X^{n-1}\) gives \(nf\in k\), so \(f\in k\). In characteristic \(p\), write \(n=p^e m\) with \(p\nmid m\); the coefficient of \(X^{n-p^e}\) gives \(m f^{p^e}\in k\), since \((X-f)^n=(X^{p^e}-f^{p^e})^m\). Thus a positive power belongs to \(k\) in either case. Such an element is either nilpotent or a unit. It cannot have these two different vanishing behaviours. This contradiction shows that \(u_0,u_1\) are joined by an arrow. The reverse implication follows from the definition of \(C\). \(\square\)

**Proposition 6.5.** For a finite-flat affine chart, \(\pi:\mathcal Y\to M\) is separated, quasi-compact and a universal homeomorphism. It is a uniform categorical moduli space among affine targets.

**Proof.** The diagonal is tested by \(R\to U\times_M U\). This morphism is finite: factor it as the graph of one endpoint followed by a base change of the other finite endpoint, using that \(U\to M\) is affine and separated. Thus the relative diagonal of \(\pi\) is proper. The affine map \(U\to M\) and the surjectivity of \(U\to\mathcal Y\) give quasi-compactness.

The map \(U\to M\) is integral. Its universal closedness descends through the surjective atlas: for a closed subset of any base change of \(\mathcal Y\), its inverse image in the base-changed \(U\) is closed and has the same image in the base. Lemma 6.4 identifies the topological quotient with \(M\); after arbitrary affine base change, apply the same orbit calculation and then the universal homeomorphism of invariant spectra in Lemma 6.4. Hence \(\pi\) is universally bijective and universally closed, and therefore a universal homeomorphism.

For an affine target \(\operatorname{Spec}E\), invariant maps \(U\to\operatorname{Spec}E\) are exactly ring maps \(E\to C\). Proposition 6.2 identifies these with maps from \(\mathcal Y\). Flat base change preserves \(C\) by Lemma 6.3, so this categorical property holds after every flat affine base change. \(\square\)

#### Descending étale maps without changing stabilizers

The next step explains why retaining the stabilizers in a local chart matters.

**Lemma 6.6 (étale descent of charts).** Let \(h:\mathcal Y'\to\mathcal Y\) be representable, étale and stabilizer preserving. If both stacks have finite-flat affine charts and \(\pi,\pi'\) are their invariant quotients, there is a cartesian square
\[
\begin{array}{ccc}
\mathcal Y'&\xrightarrow{h}&\mathcal Y\\
\downarrow&&\downarrow\\
M'&\longrightarrow&M
\end{array}
\tag{6.K3}
\]
whose bottom morphism is étale.

The algebraic form is the following. If \(U'\to U\) is étale and the source, target and stabilizer squares of two finite locally free affine groupoids are cartesian, their invariant spectra satisfy \(M'\to M\) étale and
\[
U'=M'\times_M U,\qquad R'=M'\times_M R.
\tag{6.K4}
\]
The second equality has \(R\) on the right, because it describes the arrow space.

**Proof.** Choose \(U\to\mathcal Y\) finite locally free and affine. Its pullback \(U'\to\mathcal Y'\) is finite locally free. Choose a finite locally free affine atlas \(V\to\mathcal Y'\). The space \(U'\times_{\mathcal Y'}V\) is affine, being finite over \(V\), and is a finite faithfully flat cover of \(U'\). An algebraic space with such a cover is affine, by *The bootstrap theorem*, Appendix A applied to its presentation relation. Thus \(U'\) is affine. Set \(R'=U'\times_{\mathcal Y'}U'\). The source and target squares are cartesian by transitivity of fibre products; the stabilizer square is cartesian because \(h\) preserves inertia. It remains to prove the algebraic assertion (6.K4).

Write \(C,C'\) for the two invariant rings. Flat base change preserves both rings by Lemma 6.3. Fix \(p'\in\operatorname{Spec}C'\) above \(p\in\operatorname{Spec}C\), and pass to the strict henselization \(D\) of \(C_p\). After choosing a point above \(p'\), replace all rings by this flat base change. We may assume \(C\) strictly henselian local, with maximal ideal \(\mathfrak m\) and separably closed residue field \(k\).

The fibre \(U_p\) is a finite orbit by Lemma 6.4. Each residue field there is algebraic over \(k\), and therefore purely inseparable and separably closed. The same holds for the selected quotient fibre \(U'_{p'}\). An étale map gives equal residue fields at its points over \(U_p\). The cartesian source square shows that every point of \(U_p\) is reached from a chosen \(u'\in U'_{p'}\): translate along the source fibre to reach every point in its orbit.

There is no duplication. If \(u'_1,u'_2\) above the same \(u\) are joined by \(r'\), the two induced embeddings of the purely inseparable field \(\kappa(u)\) into \(\kappa(r')\) coincide. Thus \(r'\) maps to the stabilizer at \(u\). The stabilizer square is cartesian, so \(r'\) belongs to the stabilizer at \(u'_1\), and \(u'_1=u'_2\). Consequently the selected fibre maps bijectively to \(U_p\), with the same residue fields. With
\[
J=\sqrt{\mathfrak m A},\qquad
J'\subset A'\ \text{the radical ideal of }U'_{p'},
\]
this gives \(A/J\simeq A'/J'\). The fibres are finite sets of closed points; their reduced coordinate rings are the products of their residue fields.

Here is the henselian lifting used in this argument, with its full integral scope. A henselian local ring \(C\) has the idempotent-lifting property for every finite \(C\)-algebra, proved in *Henselian local rings and henselization*, Theorem 2.2. It has the same property for an integral \(C\)-algebra \(E\): an idempotent modulo \(\mathfrak m E\), together with its finite equation and the finitely many coefficients expressing that equation modulo \(\mathfrak m E\), lies in a finite \(C\)-subalgebra, where it lifts. Uniqueness follows because \(\mathfrak m E\) is in the Jacobson radical, by integrality. Every finite \(A\)-algebra is integral over \(C\). Since \(J=\sqrt{\mathfrak m A}\), the quotients modulo \(\mathfrak m\) and modulo \(J\) have the same idempotents: their intervening ideal is nil, and idempotents lift uniquely modulo nil ideals. Thus reduction modulo \(J\) preserves idempotents in every finite \(A\)-algebra.

Apply the affine finite factorization of *Zariski's Main Theorem*, Theorem 3.2, to the affine étale map \(\operatorname{Spec}A'\to\operatorname{Spec}A\). Write \(U'\) as an open of a finite affine \(A\)-scheme \(\overline U\). The selected reduced closed fibre is an open-and-closed component of \(\overline U_{A/J}\): it is open because its projection is an étale section, and closed because that section, isomorphic to \(\operatorname{Spec}(A/J)\), is proper in the separated finite fibre. Lift its idempotent to the finite algebra of \(\overline U\). The resulting finite component lies wholly in \(U'\), since its closed complement misses the fibre over \(J\), while every maximal ideal of its finite algebra lies over a maximal ideal containing \(J\). This component is finite étale over \(A\) and reduces to \(A/J\). A finite locally free algebra with this reduction has rank one at every maximal ideal; its unit is a basis by Nakayama, so it is \(A\). We obtain
\[
U'=U\amalg U''.
\]

This component is invariant. The source and target inverse images of it agree over the closed orbit \(U'_{p'}\). Each is finite over the component \(U\), hence integral over the local ring \(C\); any nonempty closed difference would have a point over the closed point of \(C\). There is no such point, because \(U'_{p'}\) is a whole orbit. The two inverse images therefore agree. The original cartesian source square identifies the restricted arrow scheme with \(R\). We get a decomposition of groupoids into \((U,R)\) and a complement, and hence \(M'=M\amalg M''\) on invariant spectra.

The component is cut out by an idempotent, and its isomorphism to \(U\) is between schemes of finite presentation over the relevant object scheme. Its finitely many defining equations, inverse equations and groupoid compatibilities descend to a finite stage of the filtered étale neighbourhoods defining \(D\). This is the finite-presentation limit result of *Properties and morphisms of algebraic spaces*, applied also to scheme maps. At that stage \(M'\to M\) has an open component isomorphic to the base near the selected point, so it is étale there. Descent of étaleness proves that \(M'\to M\) is étale at every point.

The map \(U'\to M'\times_M U\) is étale, since both schemes are étale over \(U\). The same strictly henselian orbit calculation says that every geometric fibre of this map has exactly one point with equal residue field. It is thus surjective and universally injective, hence an isomorphism. The cartesian source square gives \(R'=M'\times_M R\). Finally base change of quotient stacks proves (6.K3). \(\square\)

Two consequences complete the categorical assertion of Proposition 6.5.

**Proposition 6.7.** A finite-flat affine chart has a uniform categorical moduli space among all algebraic-space targets. If \(h:\mathcal Y'\to\mathcal Y\) is separated, étale and stabilizer preserving, then \(\mathcal Y'\) is obtained by base change from a separated étale scheme \(M'\to M\).

**Proof.** First prove the categorical assertion. Uniqueness can be checked before existence. For two factorizations \(M\rightrightarrows E\) of a map \(\mathcal Y\to E\), their equalizer \(Z\to M\) is a monomorphism of schemes: the diagonal of an algebraic space is representable by schemes. The map from \(\mathcal Y\) factors through \(Z\). The universal homeomorphism \(\mathcal Y\to M\) shows that \(Z\to M\) is a universal homeomorphism, and hence integral. Thus \(Z\) is affine. Initiality among affine targets forces \(Z=M\).

For existence, choose an affine étale chart \(V\to E\) at the image of a given point of \(M\). Put \(\mathcal Y'=\mathcal Y\times_E V\) and \(U'=U\times_E V\). The map \(U'\to U\) is separated and étale; hence \(U'\) is a scheme and each finite orbit lies in an affine open. Choose such an affine open \(W\). If \(R'\) is the pulled-back groupoid, remove from \(U'\) the closed set
\[
t\bigl(R'\setminus(s^{-1}W\cap t^{-1}W)\bigr).
\]
Its complement \(W_0\subset W\) is invariant and still contains the chosen orbit. Finite source and target maps make this saturation closed; composition shows that it is exactly the union of orbits meeting the complement of \(W\). Choose \(f\in\Gamma(W,\mathcal O_W)\) with the orbit contained in \(D_W(f)\subset W_0\), by prime avoidance against its finitely many points. On \(W_0\) define \(g=\operatorname{Norm}_s(t^*f)\), using \(t(s^{-1}W_0)\subset W\). Its nonvanishing locus consists exactly of the points at which \(f\) is nonzero on the entire orbit. It is invariant and contains the chosen orbit. The identity arrow gives \(D(g)\subset D_W(f)\). On this affine principal open, \(g\) is regular, and \(D(g)\) is its principal open. Thus \(D(g)\) is affine, rather than merely an open subset of an affine scheme. It gives the required open finite-flat affine subchart \(\mathcal Y''\subset\mathcal Y'\).

Lemma 6.6 descends \(\mathcal Y''\to\mathcal Y\) to an étale affine neighbourhood \(M''\to M\). The map \(\mathcal Y''\to V\) factors through \(M''\) by affine initiality. These neighbourhoods cover \(M\), and uniqueness makes the resulting maps to \(E\) agree on their étale overlaps. The sheaf condition for \(E\) glues them. Equality of the composites with the original map is also checked on this cover.

The argument survives every flat affine base change. For a flat algebraic-space base change, choose an affine étale cover of its target and apply the affine result there. On the affine covers of its pairwise overlaps, uniqueness identifies the local factorizations. Étale descent glues the unique factorization. This proves uniformity for all algebraic-space base changes.

For the second assertion, apply the invariant-affine-neighbourhood construction to the finite orbits in \(U'=\mathcal Y'\times_{\mathcal Y}U\). This covers \(\mathcal Y'\) by open finite-flat affine subcharts. Lemma 6.6 supplies étale affine quotient schemes for them. Their pairwise intersections correspond to open subsets of the quotient schemes, because each quotient is a universal homeomorphism. The categorical property just proved identifies the two quotients of an intersection uniquely. On a triple intersection, both composites are factorizations of the same map from that intersection, so uniqueness proves the cocycle identity. Glue the quotient schemes along these open isomorphisms to get \(M'\). The maps to \(M\) and from \(\mathcal Y'\) glue, and the cartesian squares hold locally on the open covers. Thus \(\mathcal Y'=M'\times_M\mathcal Y\) and \(M'\to M\) is étale.

Finally \(U'\to M'\) is universally closed and surjective: it is finite over \(\mathcal Y'\), followed locally by its quotient's universal homeomorphism. After pulling back the diagonal of \(M'\to M\) by \(U'\times_U U'\to M'\times_M M'\), its inverse image is the closed diagonal of \(U'\to U\). The latter covering morphism is universally closed and surjective, so that diagonal is closed. Since an étale diagonal is an open immersion, it is a closed immersion as well. Hence \(M'\to M\) is separated. \(\square\)

#### The local charts provided by finite inertia

**Lemma 6.8.** If \(\mathcal X\) has finite inertia, every point is in the image of a representable, separated, étale, stabilizer-preserving map
\[
g_i:\mathcal X_i\to\mathcal X
\]
from a finite-flat affine chart.

**Proof.** The diagonal is locally quasi-finite because on every geometric fibre its nonempty Isom space is a torsor under a finite stabilizer, and the diagonal is locally of finite type. Its diagonal is closed: on a smooth scheme chart it is the identity section of the finite inertia group. Thus the diagonal is separated.

We first produce a flat locally quasi-finite scheme atlas. The field-groupoid argument of Lemma 1.3 of *Quotient stacks and Deligne–Mumford stacks* works with any zero-dimensional stabilizer: its constant-field calculation identifies the reduced field groupoid near the identity with the reduced stabilizer. A finite stabilizer is zero-dimensional even when nonreduced. Translation gives the same dimension at every arrow.

At a finite-type point \(x\), choose a closed point \(u\) in a smooth affine atlas \(U\to\mathcal X\). Put \(F=U\times_{\mathcal X}\operatorname{Spec}\kappa(u)\), and let \(z\in F\) be the identity point. The closed subspace \(\operatorname{Spec}\kappa(u)\times_{\mathcal X}\operatorname{Spec}\kappa(u)\) has dimension zero by the field-groupoid argument. Therefore the image of the maximal ideal of \(\mathcal O_{U,u}\) in the regular local ring of the smooth fibre \(F\) is primary to its maximal ideal. Choose a regular sequence of length \(\dim_zF\) from that image. The flat slicing calculation in *The bootstrap theorem*, Section 3.3, applied on scheme charts, makes its zero locus flat and locally finitely presented over \(\mathcal X\) after shrinking; its fibre at \(z\) is zero-dimensional, so shrink further to its locally quasi-finite locus. These open images contain every finite-type point and cover \(\mathcal X\), by Lemma 1.1 of the present lesson. Their disjoint union is a flat locally quasi-finite scheme atlas.

Near any chosen point, take its affine piece \(U\). The arrow space \(R=U\times_{\mathcal X}U\) is separated and locally quasi-finite over \(U\), so it is a scheme by *The bootstrap theorem*, Appendix B. Its source and target are flat, locally finitely presented and separated.

The finite-part parameter construction in the proof of *The bootstrap theorem*, Lemma 3.5, used no monomorphism condition until it concluded that its new groupoid was an equivalence relation. Apply that parameter construction here, keeping its groupoid rather than imposing that conclusion. Explicitly let \(Y\to U\) parametrize finite open-and-closed parts \(Z\) of source fibres which contain the identity. Finite parts lift over a henselization by the finite-piece and idempotent argument in that proof. Equal finite parts are recognized by vanishing of the locally constant ranks of their two differences. These liftings and equality loci give étale charts with an étale scheme relation; *Algebraic spaces* constructs their quotient. Its diagonal is closed by the same rank comparison. Appendix B then makes it a scheme separated and étale over \(U\).

Its universal finite part has source
\[
(x,Z,r)\longmapsto(x,Z)
\]
and target
\[
(x,Z,r)\longmapsto\bigl(t(r),Zr^{-1}\bigr).
\]
Translation of a source fibre is an isomorphism, so the target part is still finite open-and-closed and contains its identity. Inversion is
\[
(x,Z,r)\longmapsto\bigl(t(r),Zr^{-1},r^{-1}\bigr).
\]
For a second arrow \(r'\) the translated part is \(Zr^{-1}(r')^{-1}=Z(r'r)^{-1}\); this proves closure under composition. Identities, associativity and the inverse laws follow from the original arrows. The source is finite locally free; inversion shows the same for the target. The resulting groupoid \(P\rightrightarrows Y\) is open in \(R_Y\): over its universal finite open, its target prescription is a section of the étale projection \(R_Y\to R\times_UY\), and such a section is an open immersion.

At the chosen \(u\), the source fibre is zero-dimensional and locally of finite type over \(\kappa(u)\). The finite stabilizer is supported on a finite collection of its open-and-closed Artinian components. Select exactly those components, including their complete scheme structures, to obtain a finite part \(Z_u\). This gives a point \(y=(u,Z_u)\) of \(Y\) with residue field \(\kappa(u)\). Right translation by a stabilizer arrow preserves the stabilizer support and therefore permutes precisely these complete components. This remains true after every base change: equality of open-and-closed parts is detected on their geometric points. Hence \(Z_ug^{-1}=Z_u\) for every stabilizer arrow \(g\), including arrows over nonreduced test schemes. Each such arrow lies in the selected part and its translated target is again \(y\). Thus \(P\) contains the entire stabilizer at this point, including its infinitesimal structure.

The finite orbit of \(y\) has an invariant affine neighbourhood in \(Y\), by the construction in Proposition 6.7; finite subsets lie in affine opens because \(Y\to U\) is separated and étale. Restrict to this affine neighbourhood \(V\), preserving finiteness of \(P\). Then
\[
\mathcal Y=[V/P]\longrightarrow[U/R]
\]
is representable, since the inclusion of arrows is injective. It is étale: over \(U\), its presentation relation is an open subrelation of the source-fibre equality relation, and the quotient by that open relation is étale over \(U\), as in the étale reduction of *The bootstrap theorem*, Section 2. Flat groupoid algebraicity is supplied by *Artin's axioms*, Theorem 6.6. Its inertia map is an isomorphism at the selected point because that map is an open immersion between stabilizer schemes and contains the entire target fibre there.

Shrink to the stabilizer-preserving locus. Pull the inertia map back to a scheme chart; it is an open immersion \(G\hookrightarrow H\), since the map of stacks is representable and unramified. Here \(H\) is finite over the chart. The image of the closed complement \(H\setminus G\) is closed; its complement is precisely the locus where every fibre has \(G=H\). An étale open immersion which is bijective on every fibre of this locus is an isomorphism there. This constructs the required open substack.

Refine it by invariant affine neighbourhoods for its finite atlas as in Proposition 6.7. The resulting \(\mathcal X_i\) have finite locally free affine covers and preserve stabilizers everywhere. They are separated over \(\mathcal X\): their absolute diagonals are proper, the diagonal of \(\mathcal X\) is separated, and the relative diagonal is proper by the graph/base-change factorization. The chosen point is retained. Taking the choices through all points proves the lemma. \(\square\)

The constant-field theorem is Theorem 1.2f above. Flat slicing and the finite-piece parameter construction have their preceding proofs in *The bootstrap theorem*, §3.3 and Lemma 3.5. The latter uses the existing nonaffine Zariski Main assignment for lifting a finite part; that programme dependency remains planned where its full proof is not yet supplied. This is distinct from the written affine Zariski Main factorization used in Lemma 6.6.

#### Gluing the coarse space

**Theorem 6.9 (Keel–Mori).** Let \(\mathcal X\) be an algebraic stack whose inertia morphism is finite. There is an algebraic space \(M\) and a uniform categorical moduli morphism
\[
f:\mathcal X\longrightarrow M.
\]
The morphism is separated, quasi-compact and a universal homeomorphism. For each algebraically closed field \(k\), it induces a bijection
\[
\{\text{objects of }\mathcal X(k)\text{ up to isomorphism}\}
 \xrightarrow{\sim}M(k).
\tag{6.K5}
\]

**Proof, given Lemmas 6.6 and 6.8.** Choose the charts \(g_i:\mathcal X_i\to\mathcal X\) of Lemma 6.8, and their affine invariant quotients \(M_i\). On an overlap
\[
\mathcal X_{ij}=\mathcal X_i\times_{\mathcal X}\mathcal X_j,
\]
both projections are separated, étale and stabilizer preserving. Proposition 6.7 gives a scheme \(M_{ij}\), separated and étale over \(M_i\), with
\[
\mathcal X_{ij}
 =M_{ij}\times_{M_i}\mathcal X_i.
\tag{6.K6}
\]
The quotient obtained from the other projection is canonically the same, by its categorical property.

Put \(V=\coprod_iM_i\) and \(Q=\coprod_{i,j}M_{ij}\). The projections \(Q\rightrightarrows V\) are étale. They carry composition, identities and inverse. For composition, the triple overlap has quotient
\[
M_{ijk}=M_{ij}\times_{M_j}M_{jk};
\]
the flat base-change property shows that this is its categorical quotient. Projection from the triple stack overlap to \(\mathcal X_{ik}\), followed by its quotient map, factors uniquely through \(M_{ijk}\to M_{ik}\). This defines composition. The diagonal and flip give identity and inverse by the same factorization. Each groupoid law follows from uniqueness: on the corresponding stack overlap, both composites are the same projection or composition map.

For any algebraically closed \(k\), finite-flat chart objects map bijectively on isomorphism classes to their quotient points. Since \(g_i\) preserves the full automorphism groups, passage to isomorphism classes commutes with the groupoid fibre product on each overlap. Explicitly, two choices of an isomorphism between the same pair of chart objects differ by an automorphism in \(\mathcal X\); preservation of automorphisms absorbs that difference on either chart. Thus
\[
Q(k)=V(k)\times_{\pi_0\mathcal X(k)}V(k).
\tag{6.K7}
\]
In particular \(Q(k)\to V(k)\times V(k)\) is injective and is an equivalence relation.

This point calculation is enough to establish the scheme-level relation. The endpoint map \(j:Q\to V\times V\) is unramified because one of its projections is étale. Its diagonal is an open immersion. Injectivity on all algebraically closed points makes that open immersion surjective, hence an isomorphism. Therefore \(j\) is a monomorphism. The identity, inverse and composition already constructed then make \(Q\) an equivalence relation on every test scheme. The quotient theorem of *Algebraic spaces* gives an algebraic space
\[
M=V/Q.
\tag{6.K8}
\]

The local maps \(\mathcal X_i\to M_i\to M\) agree on \(\mathcal X_{ij}\), because that overlap factors through \(M_{ij}\). For an object \(x/T\), pull the charts back to obtain an étale covering \(T_i=\mathcal X_i\times_{\mathcal X}T\). The local maps \(T_i\to M\) agree on \(T_i\times_TT_j\), so they glue uniquely to a map \(T\to M\). Pulling an object or an arrow back pulls these local maps back, and uniqueness of sheaf gluing gives compatibility with every pullback and every arrow. This constructs \(f\).

The squares
\[
\begin{array}{ccc}
\mathcal X_i&\longrightarrow&\mathcal X\\
\downarrow&&\downarrow f\\
M_i&\longrightarrow&M
\end{array}
\tag{6.K9}
\]
are cartesian. The comparison \(h_i:\mathcal X_i\to M_i\times_M\mathcal X\) is representable and étale: it is a morphism over \(\mathcal X\) between representable étale stacks. Equation (6.K7) and the quotient description (6.K8) show that on each algebraically closed field it is bijective on isomorphism classes. Its map on automorphism groups is an isomorphism because this holds for \(g_i\), and the algebraic-space factor \(M_i\) adds no automorphisms. Hence it is an equivalence on those fibres. A representable étale morphism with this property is surjective and universally injective; it is an open immersion and therefore an isomorphism. This proves (6.K9).

The étale surjection \(V\to M\) therefore pulls \(f\) back to the maps of Proposition 6.5. Properness of the relative diagonal, quasi-compactness and universal-homeomorphism descend along this covering, giving the asserted properties of \(f\). Equation (6.K7) also gives (6.K5).

Finally let \(M'\to M\) be any flat morphism of algebraic spaces and let \(\theta:\mathcal X\times_M M'\to E\) be a map to an algebraic space. The uniform property of each \(\mathcal X_i\to M_i\) gives a unique map
\[
\psi_i:M_i\times_M M'\to E.
\]
On the overlap \(M_{ij}\times_M M'\), both restrictions compose with the quotient of \(\mathcal X_{ij}\times_M M'\) to the same restriction of \(\theta\). Uniqueness for that overlap quotient forces the restrictions to agree. Étale descent then gives a unique \(\psi:M'\to E\). Its composite with the pulled-back \(f\) equals \(\theta\), since equality is checked after the étale covering by the pulled-back \(\mathcal X_i\). Any other factorization has the same restrictions \(\psi_i\) and hence equals \(\psi\). This proves uniform categorical initiality. \(\square\)

The map forgets automorphisms, even when it is a universal homeomorphism. For a nontrivial finite flat group \(G\), the example \(BG\to S\) has one geometric isomorphism class over each coarse point while retaining automorphism group \(G\) in the stack. The target is an algebraic space; the theorem supplies no scheme structure on the global gluing (6.K8).

### 6.2. The \(j\)-line

**Theorem 6.10 (integral elliptic coarse space).** For the stack of smooth proper genus-one curves with a specified section, the morphism
\[
j:\mathcal M_{1,1}\longrightarrow J=\mathbf A^1_{\mathbf Z},
\qquad j(E,e)=c_4^3/\Delta,
\tag{6.3}
\]
is initial among morphisms to **all algebraic spaces over \(\mathbf Z\)**. For every algebraically closed field \(k\), including characteristics \(2\) and \(3\), it induces a bijection
\[
\{\text{pointed elliptic curves over }k\}/\cong
\;\xrightarrow{\ \sim\ }\;J(k)=k.
\]
Thus it is a coarse moduli space. It also inherits the uniform property proved in §6.1: after a flat morphism of algebraic spaces \(J'\to J\), its base change is again categorical and has the geometric-point property. No assertion about arbitrary nonflat base changes is needed for the theorem.

We use the presentation already proved in Lesson 5:
\[
X=\mathcal M_{1,1}=[W/\Gamma],\qquad
W=\operatorname{Spec}A,\qquad
A=\mathbf Z[a_1,a_2,a_3,a_4,a_6,\Delta^{-1}],
\]
where \(\Gamma\) parametrizes the changes
\[
x=u^2x'+r,\qquad y=u^3y'+u^2sx'+t.
\]
Every pointed isomorphism is uniquely such a change. The invariant \(j\) is already a morphism of stacks over \(\mathbf Z\); the present task is its universal property. The proof has three substantive steps: finite isomorphism schemes, classification in every geometric fibre, and identification of the space supplied by §6.1.

#### Finite isomorphism schemes over the whole coefficient space

**Lemma 6.11.** The morphism
\[
\operatorname{Isom}(E_a,E_{a'})\longrightarrow W\times_{\mathbf Z}W
\]
is finite. Consequently \(X\) has finite diagonal, is separated over \(\mathbf Z\), and has finite inertia.

*Proof.* Write
\[
B=\mathbf Z[a_1,a_2,a_3,a_4,a_6,a'_1,a'_2,a'_3,a'_4,a'_6,
             \Delta(a)^{-1},\Delta(a')^{-1}].
\]
The scheme of isomorphisms from the primed curve to the unprimed curve is the closed subscheme of
\(\operatorname{Spec}B[u,u^{-1},r,s,t]\) defined by Lesson 5's coordinate-change equations:
\[
\begin{aligned}
ua'_1&=a_1+2s,\\
u^2a'_2&=a_2-sa_1+3r-s^2,\\
u^3a'_3&=a_3+ra_1+2t,\\
u^4a'_4&=a_4-sa_3+2ra_2-(t+rs)a_1+3r^2-2st,\\
u^6a'_6&=a_6+ra_4+r^2a_2+r^3-ta_3-rta_1-t^2.
\end{aligned}                                                    \tag{6.4}
\]
The discriminant transformation gives
\[
u^{12}\Delta(a')=\Delta(a).
\]
Thus \(u\) and \(u^{-1}\) lie in the finite \(B\)-algebra
\[
B_1=B[u]/(u^{12}-\Delta(a)/\Delta(a')).
\]
Indeed \(u^{-1}=u^{11}\Delta(a')/\Delta(a)\). It remains to prove that the isomorphism algebra is finite over \(B_1\).

Give \(s,r,t\) weights \(1,2,3\), and give \(B_1\) weight zero. The highest-weight parts of (6.4) imply that its associated graded algebra is a quotient of
\[
B_1[S,R,T]/(2S,\ 3R-S^2,\ 2T,\ 3R^2-2ST,\ R^3-T^2).             \tag{6.5}
\]
This assertion follows from the filtered polynomial presentation: the initial ideal of the defining ideal contains the initial forms of its five displayed generators.

In (6.5), \(2T=0\) and \(3R^2=2ST=0\). Therefore
\[
2T^2=0,\qquad 3T^2=3R^3=0,
\]
and \(T^2=0\), because \(3-2=1\) in every coefficient ring. Then \(R^3=0\), and
\(S^6=(3R)^3=27R^3=0\).
The graded algebra is consequently generated as a \(B_1\)-module by the 36 monomials
\[
S^iR^hT^\ell,\qquad 0\leq i<6,\quad 0\leq h<3,\quad 0\leq\ell<2.
\]
Their lifts generate the filtered algebra too: subtract a combination with the same highest-weight class and induct on the nonnegative weight. No division by \(2\) or \(3\) occurs. Hence the isomorphism algebra is finite over \(B_1\), and over \(B\).

The base change of \(\Delta_{X/\mathbf Z}\) by the smooth surjection
\(W\times_{\mathbf Z}W\to X\times_{\mathbf Z}X\) is this scheme of isomorphisms. Finiteness descends along the atlas cover: locally it is descent of the finite algebra and its multiplication, and the representing relative spectra agree on the cover and its overlaps. Thus the diagonal is finite. Finite morphisms are proper, so \(X/\mathbf Z\) is separated in the stack sense. The inertia is a base change of this diagonal, hence is finite as a morphism to \(X\). \(\square\)

This proves global finiteness, rather than only finiteness of the automorphism groups at geometric points. In particular, jumping automorphism groups at special \(j\)-values and small characteristics do not prevent applying §6.1.

#### The geometric classification, including characteristics \(2\) and \(3\)

**Lemma 6.12.** Over an algebraically closed field \(k\), two pointed elliptic curves are isomorphic if and only if their \(j\)-invariants agree, and every element of \(k\) occurs.

*Proof.* Lesson 5 gives a long Weierstrass equation over \(k\), all its pointed isomorphisms, and the discriminant criterion. We put these equations into explicit forms. Each coordinate change below is of that lesson's prescribed form and therefore preserves the section.

If \(\operatorname{char}k\ne2,3\), completion of the square and translation of \(x\) give
\[
y^2=x^3+Ax+B,\qquad
D=4A^3+27B^2\ne0,\qquad
j=1728\,\frac{4A^3}{D}.                                      \tag{6.6}
\]
Changes between short equations are precisely scalings, with
\(A=u^4A'\), \(B=u^6B'\). If \(j=0\), then \(A=0\), \(B\ne0\), and all such curves scale to \(y^2=x^3+1\). If \(j=1728\), then \(B=0\), \(A\ne0\), and all scale to \(y^2=x^3+x\).

For any other fixed \(j\), both \(A\) and \(B\) are nonzero. Equality of (6.6) gives
\(A^3B'^2=A'^3B^2\). Put
\(\alpha=A/A'\), \(\beta=B/B'\); then \(\alpha^3=\beta^2\).
Choose \(u\) with \(u^2=\beta/\alpha\). It satisfies \(u^4=\alpha\) and \(u^6=\beta\), giving the pointed isomorphism. To see existence for every such \(j\), take
\[
A=-\frac{3j}{j-1728},\qquad B=-\frac{2j}{j-1728}.
\]
Here \(D=-108\cdot1728\,j^2/(j-1728)^3\ne0\), and substitution in (6.6) gives the prescribed \(j\). This also proves uniqueness for the two exceptional values by the preceding scalings.

In characteristic \(3\), completion of the square is still allowed. Write
\[
y^2=x^3+A_2x^2+A_4x+A_6.
\]
Directly from the integral formulas,
\[
c_4=A_2^2,\qquad
\Delta=A_2^2A_4^2-A_2^3A_6-A_4^3.                             \tag{6.7}
\]
For \(j\ne0\), one has \(A_2\ne0\). Translation by \(r=A_4/A_2\) kills the \(x\)-coefficient, since its new value is \(A_4+2A_2r=A_4-A_2r\). The equation becomes
\(y^2=x^3+A_2x^2+B\), with
\(\Delta=-A_2^3B\) and \(j=-A_2^3/B\).
Choose \(u^2=A_2\). Scaling gives the unique displayed form
\[
y^2=x^3+x^2-\frac1j.                                        \tag{6.8}
\]
For \(j=0\), \(A_2=0\) and \(A_4\ne0\), by (6.7). Choose \(r\) solving
\(r^3+A_4r+A_6=0\), and then choose \(u^4=A_4\). Translation kills the constant and scaling gives
\[
y^2=x^3+x.                                                   \tag{6.9}
\]
The discriminants of (6.8) and (6.9) are respectively \(1/j\) and \(-1\). Their invariants are the indicated \(j\) and \(0\). Algebraic closedness supplies every root used here. These forms prove both existence and uniqueness in characteristic \(3\).

In characteristic \(2\), the integral formulas reduce to
\[
c_4=a_1^4,\qquad
\Delta=a_3^4\quad\text{if }a_1=0.                             \tag{6.10}
\]
For \(j\ne0\), \(a_1\ne0\). In (6.4) choose
\[
u=a_1,\qquad r=a_3/a_1,\qquad t=(a_4+r^2)/a_1.
\]
Then \(a'_1=1\), \(a'_3=0\). The two terms involving \(s\) in the fourth equation cancel because \(a_3+ra_1=0\), so \(a'_4=0\). Choose a root of
\[
s^2+a_1s+a_2+r=0;
\]
this makes \(a'_2=0\). The result is
\[
y^2+xy=x^3+B,\qquad \Delta=B,\quad c_4=1.
\]
Hence \(B=1/j\), and the normal form is
\[
y^2+xy=x^3+\frac1j.                                         \tag{6.11}
\]
It is smooth for every \(j\ne0\).

For \(j=0\), \(a_1=0\) and \(a_3\ne0\). Choose \(u^3=a_3\). Choose \(s\) solving
\[
s^4+a_3s+a_2^2+a_4=0,\qquad r=s^2+a_2.
\]
The second and fourth equations of (6.4) then give \(a'_2=a'_4=0\), and \(a'_3=1\). Finally choose \(t\) solving
\[
t^2+a_3t=a_6+ra_4+r^2a_2+r^3.
\]
This gives \(a'_6=0\), and therefore the normal form
\[
y^2+y=x^3,                                                   \tag{6.12}
\]
whose discriminant is \(1\) and invariant is \(0\).
All the displayed polynomial equations have roots in \(k\); their nonzero linear coefficients even make the two choices in the \(j=0\) construction separable. Forms (6.11) and (6.12) prove existence and uniqueness in the remaining characteristic.

Isomorphic curves have the same \(j\) by its integral transformation identity. Conversely, the constructions take any two equations with the same \(j\) to the same pointed normal form. Composing the resulting pointed isomorphisms proves the required converse. Every listed normal form is smooth by its nonzero discriminant, so it is an elliptic curve by Lesson 5. \(\square\)

The lemma classifies geometric isomorphism classes; it asserts neither uniqueness of an isomorphism nor classification over nonclosed fields.

#### The integral invariant functions

**Lemma 6.13.** For the action of \(\Gamma\) on \(A\),
\[
A^\Gamma=\mathbf Z[j].                                      \tag{6.13}
\]
The equality is inside \(A\), with the indicated integral invariant \(j=c_4^3/\Delta\).

*Proof.* The ring \(A\) is torsion-free over \(\mathbf Z\), so an invariant embeds into the invariant ring over \(\mathbf Q\). Lesson 5's short-equation presentation over \(\mathbf Z[1/6]\) identifies this latter ring with
\[
\mathbf Q[A,B,D^{-1}]^{\mathbf G_m},\qquad D=4A^3+27B^2.
\]
Here the symbols \(A,B\) are the short coefficients, not the original coefficient ring. Their weights are \(4,6\), and \(D\) has weight \(12\). After putting a common denominator \(D^n\), invariance says that its numerator has weight \(12n\). For each monomial \(A^aB^b\) in that numerator,
\[
4a+6b=12n.
\]
Thus \(a=3r\), \(b=2s\), \(r+s=n\). The invariant ring is generated by \(A^3/D\) and \(B^2/D\), which satisfy
\[
4(A^3/D)+27(B^2/D)=1.
\]
Since \(4,27\) are units in \(\mathbf Q\), it is precisely
\(\mathbf Q[A^3/D]=\mathbf Q[j]\). The use of weights can be read scheme-theoretically: equality after coaction into the Laurent polynomial ring forces every nonzero weight component to vanish.

We now prove the integral intersection
\[
\mathbf Q[j]\cap A=\mathbf Z[j],                             \tag{6.14}
\]
rather than assuming it from the rational calculation. For each prime \(p\), the homomorphism
\[
\mathbf F_p[z]\longrightarrow A/pA,\qquad z\longmapsto j
\]
is injective. Indeed a polynomial in its kernel vanishes on every Weierstrass equation over \(\overline{\mathbf F}_p\). Lemma 6.12 realizes every value of \(j\) over that infinite field. A polynomial vanishing on all those values is zero.

Suppose \(F(j)\in A\) with \(F(z)\in\mathbf Q[z]\), and some coefficient has a denominator divisible by \(p\). Take the least \(n>0\) such that
\[
H(z)=p^nF(z)\in\mathbf Z_{(p)}[z].
\]
Some coefficient of \(H\) is a \(p\)-adic unit. But
\(H(j)\in p^n(A\otimes\mathbf Z_{(p)})\), so reducing modulo \(p\) makes the nonzero polynomial \(\overline H\) vanish at \(j\), contradicting the injectivity just proved. Thus every coefficient of \(F\) is integral at every prime, and belongs to \(\mathbf Z\).

The rational calculation and (6.14) put every integral invariant in \(\mathbf Z[j]\). The reverse inclusion follows from the already proved integral invariance of \(j\). \(\square\)

Equality of global invariant functions alone would give a categorical statement only for affine targets. It does not imply that the coarse space is affine or provide initiality for arbitrary algebraic spaces. We establish those assertions next.

#### Identifying the Keel–Mori space

Apply the theorem of §6.1, using Lemma 6.11. It gives
\[
f:X\longrightarrow M
\]
with \(M\) an algebraic space, \(f\) a separated quasi-compact universal homeomorphism, geometric-point classification, and categorical initiality for arbitrary algebraic-space targets. Its uniform version gives the same properties after flat base change from \(M\). Since \(j:X\to J\) is a morphism to an algebraic space, there is a unique
\[
h:M\longrightarrow J,\qquad h\circ f=j.                       \tag{6.15}
\]
We prove \(h\) is an isomorphism. No separation, reducedness or birationality of \(M\) is assumed in this step.

**Finite type.** The stack \(X\) is of finite type over \(\mathbf Z\): its smooth atlas is the affine finite-type scheme \(W\). The construction in §6.1 supplies an étale cover \(M_i\to M\), with cartesian stacks \(X_i=X\times_M M_i\), each of the form
\[
X_i=[U_i/R_i],\quad U_i=\operatorname{Spec}A_i,\quad
M_i=\operatorname{Spec}C_i,\quad C_i=A_i^{R_i},
\]
where \(R_i\rightrightarrows U_i\) has finite locally free projections.
The atlas \(U_i\to X_i\) is finite locally free; \(X_i\to X\) is étale. Thus \(A_i\) is a finite-type \(\mathbf Z\)-algebra. The invariant-algebra proof in §6.1 makes \(A_i\) integral over \(C_i\). Since its finite set of \(\mathbf Z\)-algebra generators also generates it as a \(C_i\)-algebra, it is finite as a \(C_i\)-module.

Here is the precise finite-generation deduction. If a finite-type algebra \(D\) over a Noetherian ring \(R\) is finite as a module over an intermediate algebra \(C\), choose module generators \(v_1,\ldots,v_m\), including \(1\), and algebra generators \(d_1,\ldots,d_n\) over \(R\). Express each \(d_i\) and each \(v_jv_k\) as a \(C\)-linear combination of the \(v_\ell\). Let \(C_0\) be the \(R\)-algebra generated by the finitely many coefficients. The \(C_0\)-span of the \(v_\ell\) contains \(1,d_1,\ldots,d_n\) and is closed under products; hence it is all of \(D\). Thus \(D\) is a finite \(C_0\)-module. Because \(C_0\) is Noetherian, its submodule \(C\subset D\) is finite too. Therefore \(C\) is a finite-type \(R\)-algebra. Applying this with \(R=\mathbf Z\) proves that the \(M_i\), and hence \(M\), are locally of finite type over \(\mathbf Z\).

The continuous surjection \(W\to M\) makes \(M\) quasi-compact. Since its structure map has affine target, it follows that \(M\) is of finite type over \(\mathbf Z\). Its underlying topological space is Noetherian: finitely many affine Noetherian pieces of an étale atlas have open images covering it, and a finite union of Noetherian subspaces is Noetherian. The map \(h\) is locally of finite type: on these affine charts, the same generators over \(\mathbf Z\) generate over \(\mathbf Z[j]\). Inverse images of the principal-open basis of the affine scheme \(J\) are open subspaces of \(M\), hence quasi-compact. Thus \(h\) is quasi-compact and of finite type.

**Separatedness.** The relative diagonal \(\Delta_{X/\mathbf Z}\) is finite by Lemma 6.11. In the commuting diagram
\[
\begin{array}{ccc}
X&\xrightarrow{\Delta_{X/\mathbf Z}}&X\times_{\mathbf Z}X\\
\downarrow f&&\downarrow f\times f\\
M&\xrightarrow{\Delta_{M/\mathbf Z}}&M\times_{\mathbf Z}M ,
\end{array}
\]
the right vertical map is a universal homeomorphism: it is a composite of two base changes of \(f\).
After any base change of the bottom target, take a closed subset of the base change of \(M\). Its inverse image in the corresponding base change of \(X\) is closed and surjects onto it. The top diagonal sends that inverse image to a closed subset, since it is universally closed. The right vertical map sends that image to a closed subset too. The commuting diagram and the surjectivity just mentioned identify this last subset with the image under the bottom diagonal of the original closed subset. Thus \(\Delta_{M/\mathbf Z}\) is universally closed.

Quasi-compactness of this diagonal must also be checked after scheme target charts. For an affine scheme \(T\to M\times_{\mathbf Z}M\), put
\[
P=X\times_{M\times_{\mathbf Z}M}T,\qquad
Q=M\times_{M\times_{\mathbf Z}M}T.
\]
The map \(P\to T\) factors through
\((X\times_{\mathbf Z}X)\times_{M\times_{\mathbf Z}M}T\): its first map is a base change of the finite diagonal of \(X\), and its second is a base change of the quasi-compact map \(f\times f\). Thus \(P\) is quasi-compact. The surjection \(P\to Q\), which is a base change of \(f\), makes \(Q\) quasi-compact too. This proves quasi-compactness of \(\Delta_{M/\mathbf Z}\).

The diagonal is a separated monomorphism, locally of finite type. It is therefore proper and locally quasi-finite. The diagonal of an algebraic space is representable by schemes; the proper quasi-finite scheme theorem applies on scheme target charts and makes it finite. A finite monomorphism is a closed immersion. Indeed its finite algebra \(D\) over an affine target ring \(R\) has \(D\otimes_R D=D\). On every residue-field fibre the finite-dimensional algebra \(D_p\) consequently satisfies \((\dim D_p)^2=\dim D_p\), so it is zero or is the residue field. Thus \(1\) generates all the fibres. Nakayama applied to the finite cokernel of \(R\to D\) makes that map surjective. Hence \(M/\mathbf Z\) is separated. Finally \(\Delta_{M/J}\) is the base change of \(\Delta_{M/\mathbf Z}\) along \(M\times_J M\to M\times_{\mathbf Z}M\), so it is closed. This proves that \(h\) is separated.

**Reducedness and irreducibility.** Every \(X_i\) above is smooth over \(\mathbf Z\), since it is étale over the smooth stack \(X/\mathbf Z\). It is reduced. To check this on a smooth scheme atlas \(V\to X_i\), observe that \(V/\mathbf Z\) is smooth and flat. Its generic fibre is smooth over \(\mathbf Q\), hence reduced; a nilpotent local function on \(V\) therefore becomes zero after inverting an integer, and flatness over \(\mathbf Z\) makes that function zero already. This argument on the atlas proves reducedness of the stack and of its ring of global functions.

The categorical property for the cartesian \(X_i\to M_i\) identifies
\[
\Gamma(M_i,\mathcal O_{M_i})=\Gamma(X_i,\mathcal O_{X_i}):
\]
both sides represent morphisms to \(\mathbf A^1_{\mathbf Z}\), with addition and multiplication preserved by pullback. Consequently every \(C_i\) is reduced. Reducedness is étale local, so \(M\) is reduced. The surjection from irreducible \(W\) makes its underlying topological space irreducible. Thus \(M\) is integral.

**Quasi-finiteness and the function field.** For every algebraically closed field \(k\) and every \(j_0\in k\), Lemma 6.12 and the geometric-point property of \(f\) say that \(h^{-1}(j_0)\) has exactly one geometric point. Its fibres are finite-type algebraic spaces over fields, so this is the finite-fibre criterion for quasi-finiteness. Thus \(h\) is quasi-finite. It is surjective, since every geometric point of \(J\) is attained.

By Lesson 2, Theorem B.2, a separated locally quasi-finite algebraic space over a scheme is a scheme. Applying it to \(h\) represents \(M\) by an integral scheme. Dominance and quasi-finiteness make
\[
\mathbf Q(j)\subset k(M)
\]
a finite field extension. Over an algebraic closure of \(\mathbf Q(j)\), the generic fibre has exactly one point, again by Lemma 6.12. The number of its points is the separable degree of this finite field extension. In characteristic zero that degree is its full degree. It follows that \(k(M)=\mathbf Q(j)\), with the identification induced by \(h\); hence \(h\) is birational. Geometric injectivity in characteristic \(p\) alone would not justify this inference. It is the characteristic-zero generic field, not the small-characteristic fibres, which supplies birationality.

**The normal target and the final identification.** The ring \(\mathbf Z[j]\) is a UFD by Gauss's lemma, since \(\mathbf Z\) is a UFD. The polynomial-factorization proof is Proposition 2.3 of *Integral extensions, lying over, going up and going down*: contents multiply by reduction modulo each irreducible, and primitive polynomials factor uniquely by clearing denominators in \(\mathbf Q[j]\). Every UFD is integrally closed: if a reduced fraction satisfies a monic equation, its denominator divides a power of its numerator and must be a unit. Its localizations are integrally closed as well, by clearing denominators in a monic equation, as proved in that lesson's Theorems 2.1–2.2. Therefore \(J\) is an integral normal scheme.

For clarity, the precise Zariski Main consequence can be proved using only the affine completion theorem. Cover \(M\) by affine open subschemes \(V=\operatorname{Spec}D\). The morphism \(V\to J\) is quasi-finite and of finite type. Its function field is \(\mathbf Q(j)\), so
\[
\mathbf Z[j]\subset D\subset\mathbf Q(j).
\]
The affine completion theorem of *Zariski's Main Theorem* (AG-MO-12), Theorem 3.2, embeds \(V\) as an open subscheme of \(\operatorname{Spec}D_0\), where \(D_0\) is a finite \(\mathbf Z[j]\)-subalgebra of the integral closure of \(\mathbf Z[j]\) in \(D\). Normality says this integral closure is exactly \(\mathbf Z[j]\). Thus \(D_0=\mathbf Z[j]\), and each \(V\to J\) is an open immersion.

These open immersions identify \(h\) as a local isomorphism. There cannot be two points of \(M\) above the same point of \(J\): after extending their residue fields to a common algebraically closed extension, their two geometric lifts would violate the geometric-point bijection. If two affine opens have overlapping images in \(J\), their lifts of a point in that overlap therefore coincide and lie in their intersection. Their isomorphisms on this intersection both come from \(h\), so agree as morphisms. The open immersions glue to an open immersion \(M\hookrightarrow J\). Its already proved surjectivity makes it an isomorphism.

Notice exactly where normality entered: it was proved for the target \(J\), and was used with the actual common function field. We assumed neither normality of \(M\) nor a characteristic-\(2\) or characteristic-\(3\) field identification. Now that \(h\) is an isomorphism, \(M\) is normal as a consequence. Its normality was not used to prove the isomorphism.

Finally substitute \(M=J\) in (6.15). For every algebraic space \(Y/\mathbf Z\) and every morphism \(g:X\to Y\), the categorical property of \(f\) supplies a unique \(\bar g:M\to Y\). Transporting \(\bar g\) along the proved isomorphism \(h\) gives the unique morphism \(J\to Y\) with composite \(g\). This uses the full algebraic-space universal property of §6.1, rather than the invariant-ring calculation alone. Lemma 6.12 proves the geometric-point bijection. The flat base-change property also transports along \(h\). This proves Theorem 6.10. \(\square\)

As a useful consistency check, categorical maps to \(\mathbf A^1_{\mathbf Z}\) identify
\[
\Gamma(M,\mathcal O_M)=\Gamma(X,\mathcal O_X)=A^\Gamma
=\mathbf Z[j].
\]
The middle equality is descent of functions along the action groupoid; the last is Lemma 6.13. This agrees with the identified affine scheme, but it was not used to assume affineness.

#### What a coarse point forgets

The equality of \(j\)'s concerns geometric pointed isomorphism classes. It does not classify objects over every field or families over every ring. Over \(\mathbf Q\), for example,
\[
E:y^2=x^3+x+1,\qquad E':y^2=x^3+4x+8
\]
both have \(j=1728\cdot4/31\). They become pointed-isomorphic over \(\mathbf Q(\sqrt2)\). An isomorphism over \(\mathbf Q\) would require \(u^4=4\) and \(u^6=8\), hence \(u^2=2\), which is impossible for rational \(u\). They are distinct objects over \(\mathbf Q\) with the same coarse point.

The coarse point also forgets the automorphism group. On \(\mathbf Z[1/6]\), the short equations give \(\mu_2\) at the usual values, \(\mu_4\) at \(1728\), and \(\mu_6\) at \(0\), as proved in §5. These groups are not information carried by a point of the affine line. In characteristics \(2\) and \(3\), Lemma 6.11 retains all automorphisms in its integral isomorphism scheme while Lemma 6.12 classifies their objects; the coarse-space assertion does not identify those two kinds of data.

Deligne–Rapoport's compactification and generalized or level-structure elliptic curves give a broader historical setting for the \(j\)-line. They are not inputs into this proof for the smooth pointed-curve stack. The present argument establishes the full integral smooth theorem directly from the existing Weierstrass presentation and §6.1.

Deligne–Rapoport's Chapter VI, Theorem 1.1 and §1.3, identifies the compactified coarse space of generalized elliptic curves with \(\mathbf P^1_{\mathbf Z}\) and its smooth open with the affine \(j\)-line. Their coarse-space convention is I.8.1, with flat restriction in I.8.2.3. Their III.0.2 and Theorem III.2.5 concern the broader stack of generalized curves, with the residue-characteristic condition on the number of components. These precise human-source locators remain historical context for the direct smooth-curve proof above.

## 7. Exercises and solutions

### Exercise 7.1 — A finite étale classifying stack (easy)

Show that \(BG\) is Deligne–Mumford when \(G\to S\) is finite étale.

*Solution.* The stack of right torsors has a map \(S\to BG\) given by the trivial torsor. On a test object \(P/T\), its fibre is the space \(P\) of trivializations with a specified comparison. Fppf locally this is \(G_T\), so it is finite étale and surjective over \(T\); finite étaleness descends. Its diagonal is represented by Isom torsors, which are fppf locally \(G_T\). The étale scheme atlas therefore makes \(BG\) algebraic and Deligne–Mumford, by the étale quotient theorem of Lesson 5 or by Proposition 3.1. No assumption on the invertibility of the number of geometric elements is needed for a finite **étale** group. \(\square\)

### Exercise 7.2 — \(B\mu_p\) in characteristic \(p\) (medium)

Show that \(B\mu_p\) is not Deligne–Mumford over a field \(k\) of characteristic \(p>0\).

*Solution.* The group scheme is finite locally free, so its classifying stack is algebraic by the flat groupoid theorem stated in §3. Pull the diagonal back by the pair of trivial torsors; this gives \(\mu_p\to\operatorname{Spec}k\).

The two maps from the dual numbers \(k[\epsilon]/(\epsilon^2)\) specified by \(z=1\) and \(z=1+\epsilon\) are distinct. Both satisfy \(z^p=1\) and agree after reducing modulo \(\epsilon\). Hence this diagonal test is not formally unramified. Theorem 2.2 says that a Deligne–Mumford stack has an unramified diagonal, so \(B\mu_p\) cannot be Deligne–Mumford. This argument also applies when \(p=2\). \(\square\)

### Exercise 7.3 — Stabilizers of \(\mathbf P(1,2)\) (medium)

Compute the stabilizer group schemes of its geometric points. State the base-dependent Deligne–Mumford conclusion.

*Solution.* Represent a point by \((x,y)\ne(0,0)\) over an algebraically closed field. For every test algebra \(A\), an automorphism is a unit \(\lambda\in A^\times\) with \(\lambda x=x\) and \(\lambda^2y=y\).

If \(x\ne0\), it remains a unit after scalar extension, and the first equation forces \(\lambda=1\). Thus the stabilizer is trivial. If \(x=0\), then \(y\ne0\), and the sole condition is \(\lambda^2=1\); the stabilizer is \(\mu_2\), including its full scheme structure.

Over a base with \(2\) invertible, the charts (4.3) and (4.4) have étale atlases, so the weighted line is Deligne–Mumford. Over a field of characteristic two, the stabilizer at \((0,1)\) is the nonunramified group \(\mu_2\), making its diagonal nonunramified and excluding the Deligne–Mumford condition. Over a general scheme it is Deligne–Mumford precisely when all its residue characteristics differ from two, equivalently when \(2\) is a unit; the necessity follows by this base change to each characteristic-two point. \(\square\)

### Exercise 7.4 — Short Weierstrass equations and their symmetries (medium)

Over \(\mathbf Z[1/6]\), identify \(\mathcal M_{1,1}\) with the quotient of the discriminant open in the coefficient plane by weights \(4,6\), and compute its geometric stabilizers.

*Solution.* Complete the square using \(2^{-1}\) and translate \(x\) using \(3^{-1}\). The relative normal forms of Lesson 5 thus give short equations Zariski locally over every test scheme. The discriminant is a unit exactly on \(V\) of (5.4).

Between two short equations, the unique general change of coordinates must have \(s=0\), \(r=0\), \(t=0\), by comparing the \(xy,x^2,y\) coefficients in that order. Its remaining parameter \(u\) is a unit, and the positive-weight action is \((a,b)\mapsto(u^4a,u^6b)\). Thus the action prestack has exactly all pointed Isom arrows between the local equations. The local choices and their unique comparison parameters satisfy the cocycle. Effectivity of both the elliptic stack and the quotient stack gives the equivalence (5.5).

For a geometric equation the equations are \(a(u^4-1)=b(u^6-1)=0\). If both coefficients are nonzero, their ideal in \(k[u,u^{-1}]\) is \((u^2-1)\): subtracting \(u^2(u^4-1)\) from \(u^6-1\) gives \(u^2-1\), and the converse divisibilities are immediate. Hence the stabilizer is \(\mu_2\). If \(b=0\), smoothness forces \(a\ne0\) and gives \(\mu_4\). If \(a=0\), it forces \(b\ne0\) and gives \(\mu_6\). This computes the group schemes, not only their orders. \(\square\)

### Exercise 7.5 — The short family is a smooth surjection (hard)

Show directly that the morphism \(V\to\mathcal M_{1,1}\times\operatorname{Spec}\mathbf Z[1/6]\) defined by the family (5.4) is smooth and surjective.

*Solution.* Fix an elliptic curve \(E/T\) over this base. The fibre product \(P=T\times_{\mathcal M_{1,1}}V\) classifies a short equation over a test \(T'\to T\), together with a specified pointed isomorphism from its curve to \(E_{T'}\).

The Weierstrass normal-form theorem from Lesson 5, followed by completion of the square and translation of \(x\), supplies a short equation with its identification Zariski locally on \(T\). Thus \(P\to T\) has Zariski local sections. Relative to one such section, every other section is determined by exactly one invertible parameter \(u\), by the coefficient comparison in Exercise 7.4. For every test scheme on that open this gives

\[
P|_{T_i}\simeq\mathbf G_{m,T_i}.
\]

On an overlap the two identifications differ by multiplication by their unique comparison unit. These transition units satisfy the cocycle because the comparisons compose. Zariski scheme gluing therefore represents \(P\) by a \(\mathbf G_m\)-torsor over \(T\). It is locally the smooth surjection \(\mathbf G_{m,T_i}\to T_i\), so is smooth and surjective globally.

This proves representability, smoothness and surjectivity on every scheme test. The specified identification is essential: discarding it would replace this torsor calculation by a space of isomorphism classes and would lose the automorphisms. \(\square\)

## Prerequisites and sources

The three assigned main results—the diagonal criterion, the classifying-stack criterion and finite étale quotient result, and the elliptic presentation with its Deligne–Mumford property—are proved above, using the full Weierstrass theorem already proved in Lesson 5.

The following inputs and stated results are kept separate:

- Scheme theory of unramified morphisms: the diagonal and differential criteria, the pointwise local-ring criterion [Stacks, Tag 02GF], an unramified universally injective morphism is a monomorphism [Stacks, Tag 05VH], and a flat locally finitely presented unramified map is étale. Stability, target descent, the fibre criterion and the open étale locus are used on scheme charts. These are the prerequisites from *Unramified morphisms*.
- The scheme slicing theorem [Stacks, Tag 06LI], applied to a regular sequence in a flat locally finitely presented fibre; fppf source locality of local finite presentation and local finite type [Stacks, Tags 036N, 036O]. Their passage to stack charts is proved in Lemma 2.1 and Lemma 1.4.
- The constant-field theorem [Stacks, Tags 04MI, 04MK] is proved in §1.1, relative to the existing finite-normalization assignment. Its two normal-ring inputs are written as identified there. We also use regular local rings and systems of parameters, and the existence of a closed separable point on a nonempty smooth scheme over a field [Stacks, Tag 056U]. The Euler sequence [Stacks, Tag 0FMH] and the conormal sequence for a closed immersion between smooth schemes [Stacks, Tag 06AA] are ordinary scheme prerequisites.
- The flat groupoid algebraicity theorem [Stacks, Tag 06FI], stated in §3 and proved in the next lesson. The proof of Theorem 2.2 does not use it.
- The finite-inertia moduli-space theorem [Stacks, Tag 0DUT, proof section 0DUK] is proved in §6.1. Its conclusion is an algebraic space with the stated uniform property. Henselian idempotent lifting is the written Theorem 2.2 of *Henselian local rings and henselization*; affine finite factorization is the written Theorem 3.2 of *Zariski's Main Theorem* (AG-MO-12). The finite-piece lift in the bootstrap construction still retains the genuine existing nonaffine Zariski Main proof assignment, and finite normalization retains the existing *Normalization* assignment. The conductor and nonaffine completion foundations belong to AG-MO-12; finite normalization belongs to AG-MO-13. Their planned foundations are not claimed written by this lesson.
- The integral elliptic coarse-space theorem is proved in §6.2, including characteristics two and three, the integral invariant ring, finite type and separatedness of the coarse space, and initiality for every algebraic-space target. It uses Lesson 5's integral presentation, Theorem 6.9 above, the scheme-recognition Theorem B.2 of Lesson 2, and the affine completion Theorem 3.2 of *Zariski's Main Theorem* (AG-MO-12). That provider's conductor foundations and nonaffine completion remain its genuine existing proof assignments; they are not claimed supplied here. Deligne–Rapoport I.8.1–8.2.3, VI.1.1 and VI.1.3 give the broader compactified source perspective.

## Sources and history

Sections 1.1 and 6.1 follow the Stacks Project authors' treatment, as present in the **AI Integrated Stacks Project** source at revision `565b10e987aba5969b21145a0833f42d69f96790`; they are written in this lesson's own words and integrated by GPT-6.1 Sol (OpenAI), in Codex at Ultra. The pinned source credits its own AI changes separately. This lesson is not an official Stacks Project edition and asserts no human endorsement.

The sources followed are *Varieties*, the units and uniqueness-of-constant-field proofs; *Groupoids*, the finite locally free invariant, orbit and étale-descent arguments; *Morphisms of Stacks*, the finite-inertia local charts; and *More on Morphisms of Stacks*, its Keel–Mori section. The exact [source edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790), its [licensing notice](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/README.md#attribution-and-licensing), and its [licence copy](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/COPYING) identify the source's own terms.

The text of this lesson is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

**History.** The October 2026 course lesson supplied the diagonal criterion, examples and elliptic presentation in original AI writing. On 5 October 2026 the writing AI integrated the two Stacks-following treatments above, reorganized the units proof over arbitrary fields, supplied the non-quasi-compact gluing argument, explained the henselian and categorical gluing steps, and corrected the arrow-space base change to \(R'=M'\times_MR\). The same finite pass independently supplied §6.2’s integral finite-Isom calculation, small-characteristic normal forms, invariant ring and normal-target comparison. The lesson text is CC0. Exact source hashes and remaining programme prerequisites are kept in the accompanying correction record.

## References

The Stacks project, *Morphisms of Algebraic Stacks*, Tags 06N3 and 0CIA; *Examples of Stacks*, Tags 04UV and 04WM; *Introducing Algebraic Stacks*, Tags 072K, 072T and 072U; *More on Morphisms of Stacks*, Tags 0DUF, 0DUK and 0DUT; and *Criteria for Representability*, Tag 06FI. Auxiliary field and slice locators are Tags 06FF, 06LZ, 06N0, 06LI, 036N and 036O. AI Integrated Stacks Project retains these tags.

K. Behrend, [*Introduction to Algebraic Stacks*](https://personal.math.ubc.ca/~behrend/math615A/stacksintro.pdf) (17 December 2012), §2.5, §3.4, Definitions 3.39 and 3.45, and the orbifold/root-stack discussion in §3.6.

P. Deligne and D. Mumford, [*The irreducibility of the space of curves of a given genus*](https://www.numdam.org/item/PMIHES_1969__36__75_0/), *Publications mathématiques de l'IHÉS* 36 (1969), 75–109, §4, Example (4.8).

P. Deligne and M. Rapoport, [*Les schémas de modules de courbes elliptiques*](https://publications.ias.edu/sites/default/files/Number22.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349 (1973). Internal page locators: I.8, DeRa pp. 29–30; III.0–2, DeRa pp. 54–62, especially Theorem III.2.5; VI.1, DeRa pp. 125–129, especially Theorem VI.1.1 and VI.1.3.

## History

**Source edition.** *The Stacks Project*, by the Stacks Project authors (copyright 2005–2025 Johan de Jong), distributed in the *AI Integrated Stacks Project*, 2026 edition at revision `565b10e987aba5969b21145a0833f42d69f96790` (30 September 2026). The source publisher is the Stacks Project; the fork distribution and its separately credited AI changes are identified by the pinned repository and its [retained source provenance](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/PROVENANCE.md). The [source application notice](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/introduction.tex) supplies the source's licence grant (GNU FDL 1.2 or later), and [the pinned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790) preserves the source files and their prior network locations.

**Course edition.** *Algebraic spaces and stacks — Quotient stacks and Deligne–Mumford stacks*, October 2026, published by the Open Math Courses project, `KokunoYumeto/open-math-courses`. Written and integrated by GPT-6.1 Sol (OpenAI), Codex, Ultra, 5–6 October 2026: the units/constant-field and finite-inertia coarse-space treatments following the Stacks proofs, corrected base-change and gluing comparisons, and independently expressed integral Weierstrass and coarse-invariant proofs. No AI copyright holder or human endorsement is asserted. The detailed source loci, exact edition and concrete corrections remain in this chapter. The text is dedicated to the public domain under CC0 1.0.
