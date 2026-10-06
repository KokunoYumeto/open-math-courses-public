# Quotient stacks and Deligne–Mumford stacks

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

## Introduction

A smooth atlas permits parameters to move in families. An étale atlas has no infinitesimal motion relative to the stack. The distinction is controlled by the diagonal: its fibres are spaces of isomorphisms, so its infinitesimal directions are infinitesimal symmetries.

We prove this criterion for arbitrary algebraic stacks, without a Noetherian or separation assumption. The difficult implication constructs an étale atlas from an unramified diagonal. We first replace a field presentation by one whose identity relation is reduced, and then cut a transverse slice in a smooth atlas. Quotients and elliptic curves make the criterion concrete.

We use the full presentation and Weierstrass theorems of *Algebraic stacks*, the finite flat affine quotient and division proofs of *The bootstrap theorem*, and the scheme theory of unramified morphisms. All stacks are stacks in groupoids for the fppf topology. An atlas is representable by algebraic spaces. All products of stacks are 2-fibre products.

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

**Lemma 1.3 (field groupoids with unramified stabilizer).** Let \(R\rightrightarrows u=\operatorname{Spec}K\) be a groupoid in algebraic spaces over a scheme \(S\), whose projections \(s,t\) are locally of finite type. Suppose its stabilizer

\[
G=R\times_{u\times_Su,\Delta}u
\]

is unramified over \(u\). Then \(R\) has dimension zero.

*Proof.* Choose a connected affine étale chart \(V\to R\) at the identity, with a point \(v\) mapping to it. This is possible after taking the connected component of an affine chart: the chart is Noetherian because it is of finite type over \(K\). Set \(D=\Gamma(V_{\mathrm{red}},\mathcal O)\). The two field structures \(s,t:K\to D\) are locally of finite type.

We use the constant-field theorem already isolated as a scheme prerequisite in Lesson 2, §3.3: on a reduced connected scheme locally of finite type over two fields, their integral closures in its ring of functions are the same field [Stacks, Tags 04MI, 04MK]. Write this common field as \(K_c\subset D\). Evaluation at \(v\) is injective on \(K_c\). The two maps \(K\to\kappa(v)\) agree, because \(v\) maps to the identity. They must therefore agree in \(D\). Thus \(V_{\mathrm{red}}\to R\) factors through \(G\).

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

### 6.1. The finite-inertia existence theorem

Recall that \(\mathcal I_{\mathcal X}\to\mathcal X\) has fibre \(\operatorname{Aut}_T(x)\) at an object \(x/T\).

**Keel–Mori theorem, stated.** If an algebraic stack \(\mathcal X\) has finite inertia \(\mathcal I_{\mathcal X}\to\mathcal X\), there is an algebraic space \(M\) and a uniform categorical moduli space

\[
f:\mathcal X\longrightarrow M
\]

such that \(f\) is separated, quasi-compact and a universal homeomorphism [Stacks, Tag 0DUT; proof in Tag 0DUK].

No scheme target is asserted. Separatedness here means that the relative diagonal of \(f\) is proper. Universal homeomorphism means that the map on underlying topological spaces is a homeomorphism after every algebraic-space base change to \(M\). It does not say that \(f\) is representable by spaces, or that it retains automorphism groups.

For example, \(BG\to S\) for a nontrivial finite flat group forgets its stabilizers. The map is not representable: its functor on a trivial torsor kills the nontrivial automorphism sheaf \(G\), contrary to Lesson 5's faithfulness criterion. This is compatible with the conclusion of the stated theorem.

The hypothesis is finiteness of the entire inertia morphism. An arbitrary Deligne–Mumford stack need not satisfy it; its unramified stabilizers may fail to be finite, or the inertia may lack global finiteness. Conversely \(B\mu_p\) has finite inertia and admits the theorem's conclusion despite failing the Deligne–Mumford condition.

### 6.2. The \(j\)-line

**Elliptic coarse-space theorem, stated.** Over \(\mathbf Z\), the invariant

\[
j:\mathcal M_{1,1}\longrightarrow
\mathbf A^1_{\mathbf Z}=\operatorname{Spec}\mathbf Z[j]
\tag{6.3}
\]

is a coarse moduli space in Deligne–Rapoport's sense. Thus it is initial among maps to algebraic spaces over \(\mathbf Z\), and for each algebraically closed field \(k\) its value induces a bijection between pointed elliptic curves up to isomorphism and \(\mathbf A^1(k)\).

The source is Deligne–Rapoport, Chapter VI, Theorem 1.1 and §1.3, with the definition I.8.1 and the flat open restriction in I.8.2.3. Theorem VI.1.1 identifies the **compactified** coarse space of generalized elliptic curves with \(\mathbf P^1_{\mathbf Z}\). Section VI.1.3 normalizes its coordinate as the classical invariant and takes the singular generalized curve to \(\infty\). Removing that point gives exactly (6.3); the smooth open is their notation in III.0.3(b). We state this theorem and do not replace its characteristic-two and characteristic-three argument by the short-equation calculation.

The equality of \(j\)'s concerns geometric isomorphism classes, and does not classify families over every field or ring. For a concrete example over \(\mathbf Q\), compare

\[
E:y^2=x^3+x+1,\qquad
E':y^2=x^3+4x+8.
\]

Both are smooth and have \(j=1728\cdot4/31\). Their short coefficients are related by \(u=\sqrt2\), so they are isomorphic over \(\mathbf Q(\sqrt2)\). An isomorphism over \(\mathbf Q\) would, by the unique short-coordinate calculation, require \(u^4=4\) and \(u^6=8\), hence \(u^2=2\), impossible for a rational \(u\). They define distinct objects over \(\mathbf Q\) with the same coarse point.

Even over an algebraically closed field, the coarse point does not retain the automorphism group. Equations (5.5)–(5.7) display groups \(\mu_2,\mu_4,\mu_6\) over \(\mathbf Z[1/6]\), whereas the target of (6.3) has discrete fibres.

Deligne–Rapoport's Chapter III provides a broader representability context: III.0.2 restricts generalized elliptic curves by requiring the residue characteristic not to divide their number of geometric components, and Theorem III.2.5 constructs the resulting smooth algebraic stack. Its §2 is headed *Construction de \(\mathfrak M^*\)*. Those generalized and level-structure moduli problems are beyond the smooth pointed curves proved algebraic in Lesson 5.

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

## What this lesson does not prove

The three main results—the diagonal criterion, the classifying-stack criterion and finite étale quotient result, and the elliptic presentation with its Deligne–Mumford property—are proved above, using the full Weierstrass theorem already proved in Lesson 5.

The following inputs and stated results are kept separate:

- Scheme theory of unramified morphisms: the diagonal and differential criteria, the pointwise local-ring criterion [Stacks, Tag 02GF], an unramified universally injective morphism is a monomorphism [Stacks, Tag 05VH], and a flat locally finitely presented unramified map is étale. Stability, target descent, the fibre criterion and the open étale locus are used on scheme charts. These are the prerequisites from *Unramified morphisms*.
- The scheme slicing theorem [Stacks, Tag 06LI], applied to a regular sequence in a flat locally finitely presented fibre; fppf source locality of local finite presentation and local finite type [Stacks, Tags 036N, 036O]. Their passage to stack charts is proved in Lemma 2.1 and Lemma 1.4.
- The constant-field theorem [Stacks, Tags 04MI, 04MK], already isolated in Lesson 2; regular local rings and systems of parameters, and the existence of a closed separable point on a nonempty smooth scheme over a field [Stacks, Tag 056U]. The Euler sequence [Stacks, Tag 0FMH] and the conormal sequence for a closed immersion between smooth schemes [Stacks, Tag 06AA] are ordinary scheme prerequisites.
- The flat groupoid algebraicity theorem [Stacks, Tag 06FI], stated in §3 and proved in the next lesson. The proof of Theorem 2.2 does not use it.
- The finite-inertia moduli-space theorem [Stacks, Tag 0DUT, proof section 0DUK], stated in §6.1. Its conclusion is an algebraic space, with the stated uniform property.
- The all-characteristic elliptic coarse-space theorem, Deligne–Rapoport I.8.1–8.2.3, VI.1.1 and VI.1.3, restricted from the compactified projective \(j\)-line to the smooth affine open. The broader generalized-curve representability theorem III.2.5 is cited only as historical context.

## References

[The Stacks project](https://stacks.math.columbia.edu/), *Morphisms of Algebraic Stacks*, Tags 06N3 and 0CIA; *Examples of Stacks*, Tags 04UV and 04WM; *Introducing Algebraic Stacks*, Tags 072K, 072T and 072U; *More on Morphisms of Stacks*, Tags 0DUF, 0DUK and 0DUT; and *Criteria for Representability*, Tag 06FI. Auxiliary field and slice locators are Tags 06FF, 06LZ, 06N0, 06LI, 036N and 036O. AI Integrated Stacks Project retains these tags.

K. Behrend, *Introduction to Algebraic Stacks* (2012), §2.5, §3.4, Definitions 3.39 and 3.45, and the orbifold/root-stack discussion in §3.6. [Author's lecture notes](https://personal.math.ubc.ca/~behrend/math615A/stacksintro.pdf).

P. Deligne and D. Mumford, [*The irreducibility of the space of curves of a given genus*](https://www.numdam.org/item/PMIHES_1969__36__75_0/), *Publications mathématiques de l'IHÉS* 36 (1969), 75–109, §4, Example (4.8).

P. Deligne and M. Rapoport, [*Les schémas de modules de courbes elliptiques*](https://publications.ias.edu/sites/default/files/Number22.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349 (1973): I.8; III.0–2, especially Theorem III.2.5; VI.1, especially Theorem VI.1.1 and VI.1.3.
