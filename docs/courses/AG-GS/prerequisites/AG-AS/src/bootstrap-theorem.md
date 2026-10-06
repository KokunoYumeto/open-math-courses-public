# The bootstrap theorem

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

## Introduction

The first quotient theorem began with schemes and an étale relation. Geometry often presents us with less: the relation is already an algebraic space, or the available cover is flat rather than étale. The bootstrap theorems recover the missing scheme coordinates. They also explain why a free action of a flat group can have a geometric quotient even when the group is not smooth.

There are two distinct problems. An étale coordinate map can be turned into a scheme presentation by recognizing its relation as a scheme. A flat coordinate map first has to be replaced by coordinates transverse to the relation, and then the finite local part of the relation has to be removed. We will keep these tasks separate so that the geometric work behind the second theorem remains visible.

Read Algebraic spaces first. We use its quotient theorem, the description of a sheaf quotient by local coordinates, and scheme descent for separated locally quasi-finite morphisms. We also assume flatness, finite presentation, and the scheme form of Zariski's main theorem. The proof passes through the étale reduction, transverse slicing, finite-subgroupoid division, finite-part construction and final flat bootstrap. Appendix A proves the finite flat affine quotient theorem, and Appendix B then proves the separated locally quasi-finite recognition used in Section 2. Those two appendices can be read before the bootstrap proofs. The scheme prerequisites imported along the way are listed after the appendices.

## 1. Changing the meaning of representability

For a morphism of sheaves \(F\to H\), **representable by algebraic spaces** means that \(T\times_H F\) is an algebraic space for every scheme \(T\to H\). Properties of these maps are defined by the corresponding properties of the resulting morphisms of algebraic spaces.

**Proposition 1.1.** Base change and composition preserve representability by algebraic spaces. A representable-by-spaces morphism to an algebraic space has an algebraic space as its source.

**Proof.** Base change follows directly from the definition. For the last assertion, let \(F\to X\) be representable by spaces, with \(X\) algebraic. Choose a scheme presentation \(U\to X\). Its pullback \(V=U\times_X F\) is an algebraic space, and \(V\to F\) has the tested property étale and surjective. Choose a scheme presentation \(W\to V\); to conclude we must justify representability of \(W\to F\) and of the equality functors, rather than merely exhibit a map of sheaves.

For a scheme \(T\to F\), the sheaf \(T\times_F V\) is \(T\times_X U\), a scheme. The map \(W\to V\) is representable by schemes, so \(T\times_F W\) is a scheme, étale and surjective over \(T\). For two sections \(a,b\in F(T)\), the locus on which their images in \(X\) agree is the scheme \(E_X\) cut out by \(\Delta_X\). Over \(E_X\), they give two sections of the algebraic space \(E_X\times_X F\). Their equality is represented by its diagonal. Composing its equality scheme with \(E_X\to T\) represents their equality in \(F\). Thus \(F\) is algebraic.

Now let \(F\to G\to H\) be representable by spaces and \(T\to H\) a scheme point. The sheaf \(V=T\times_H G\) is an algebraic space. Its pullback \(T\times_H F\to V\) is representable by spaces: to test it, compose a scheme point of \(V\) with \(V\to G\). The assertion just proved shows that \(T\times_H F\) is an algebraic space. This proves composition. \(\square\)

The proof did not use the bootstrap theorem; the intermediate source was placed over an algebraic space whose diagonal was already representable by schemes.

**Lemma 1.2.** If an fppf sheaf \(H\) has diagonal representable by algebraic spaces, then every map from an algebraic space \(X\) to \(H\) is representable by algebraic spaces.

**Proof.** For a scheme \(T\to H\), choose \(U\to X\) a scheme presentation. The sheaf \(T\times_H U\) is an algebraic space by the hypothesis on \(\Delta_H\), since it is its base change by \(T\times_S U\). Its map to \(T\times_H X\) is representable by schemes and étale surjective: for a test scheme over \(T\times_H X\), it is the pullback of \(U\to X\).

To see directly that this produces an algebraic space, take a scheme presentation of \(T\times_H U\). The resulting scheme map to \(T\times_H X\) is representable by schemes and étale surjective. Its self-fibre product is a scheme étale equivalence relation, so the quotient theorem from the first lesson identifies the target with an algebraic space. The target is an fppf sheaf as a fibre product of sheaves, and the surjective scheme map is an epimorphism of sheaves, which justifies this quotient identification. \(\square\)

This lemma explains why the diagonal condition permits one to talk about an étale map from \(X\) in the next theorem. Without a representability condition, a geometric adjective attached to a morphism of arbitrary sheaves needs a definition.

## 2. Recovering a scheme relation

The geometric fact used in the étale bootstrap is the following:

**Separated quasi-finite recognition.** If \(Z\to T\) is a separated, locally quasi-finite morphism of algebraic spaces and \(T\) is a scheme, then \(Z\) is a scheme. No quasi-compactness of \(Z\) is required.

The exact statement is [Stacks, Tag 03XX], proved in Appendix B. It is used below with the target a product of two schemes. Its proof uses the independently established finite affine quotient theorem of Appendix A and the scheme descent input from the first lesson; it does not invoke either bootstrap theorem.

**Theorem 2.1 (étale bootstrap).** Let \(F\) be an fppf sheaf over \(S\). Suppose an algebraic space \(X\) admits a map \(X\to F\) representable by algebraic spaces, surjective and étale. Then \(F\) is an algebraic space. The conclusion also holds if \(\Delta_F\) is representable by algebraic spaces and \(X\to F\) is surjective and étale with that representability supplied by Lemma 1.2.

**Proof.** Choose a scheme presentation \(U\to X\). Proposition 1.1 and stability of étaleness and surjectivity under composition make \(U\to F\) representable by spaces, étale and surjective. Thus

\[
R=U\times_F U
\]

is an algebraic space, and each projection \(R\to U\) is étale. The map \(j:R\to U\times_S U\) is a monomorphism. Its diagonal is an isomorphism, so \(j\) is separated.

The projections \(R\to U\) are locally quasi-finite. The morphism \(j\) is locally quasi-finite as well: its fibres embed into fibres of a projection, and its local finite type property follows from that of the projection. These statements can be tested on scheme presentations, where they are the corresponding permanence statements for locally quasi-finite morphisms. Apply separated quasi-finite recognition to \(j\). It says that \(R\) is a scheme, even though representability by schemes was not one of the initial hypotheses.

The maps \(s,t:R\to U\) are now étale scheme morphisms, and \(j\) is an equivalence relation. The quotient theorem of the first lesson proves that \(U/R\) is an algebraic space. It remains to identify this quotient with \(F\).

For a scheme \(T\to F\), its pullback to \(U\) is an algebraic space étale surjective over \(T\). Choose a scheme presentation of that pullback. Its composition to \(T\) is a surjective étale scheme morphism, and on it the section of \(F(T)\) lifts to \(U\). Hence \(U\to F\) is an epimorphism of fppf sheaves. Its equality relation is exactly \(R\). As in Lemma 2.1 of the first lesson, two local coordinates give the same section of \(F\) exactly when their pair factors through \(R\), and fppf descent glues these sections. Therefore \(F=U/R\). This proves the assertion. The second formulation follows from Lemma 1.2. \(\square\)

*Reference:* [Stacks, Tag 03Y3].

Notice what was improved. The initial diagonal and cover were allowed to be represented by algebraic spaces. The conclusion has a diagonal represented by schemes and an étale scheme presentation. The scheme relation \(R\) is the bridge between the two definitions.

## 3. Restriction, open images, and division

Write an arrow of a groupoid as \(r:x\to y\), so \(s(r)=x\) and \(t(r)=y\). Given a map \(g:V\to U\), its **restricted groupoid** has objects \(V\) and arrows

\[
R_V=V\times_{g,U,t}R\times_{s,U,g}V.
\]

The two additional coordinates record the chosen lifts of the endpoints. Even when \(g\) is not a monomorphism, they belong in this formula. Composition forgets the common middle coordinate and composes the original arrows.

**Lemma 3.1 (restriction and open image).** Let \(R\rightrightarrows U\) be a scheme equivalence relation with flat, locally finitely presented projections. If \(g:V\to U\) is an open immersion or an étale morphism, then

\[
V/R_V\longrightarrow U/R
\]

is representable by open immersions. Its image consists of classes that locally have a representative in the image of \(g\). More generally, for any \(g\), it is an isomorphism whenever

\[
h:R\times_{t,U,g}V\longrightarrow U,
\qquad (r,v)\longmapsto s(r)
\tag{3.1}
\]

is an fppf covering.

**Proof.** Let \(W\) be the image of \(h\) when \(g\) is open or étale. The projection \(R\times_U V\to R\) is open or étale, respectively, and \(s\) is flat and locally finitely presented. Thus \(h\) is open and \(W\subset U\) is open. Composition and inversion show that \(W\) is saturated: if an arrow joins two objects, one endpoint belongs to \(W\) exactly when the other does. This remains true after a base change; the two pullbacks of \(W\) to \(R\) are the same open subscheme.

Every section of the sheaf quotient \(U/R\) locally lifts to \(U\). For a scheme \(T\to U/R\), choose such lifts on an fppf covering \(T_i\to T\). Pulling back \(W\) gives opens in \(T_i\). On an overlap, any two lifts are locally joined by an arrow of \(R\), so saturation makes these opens agree. Descent for open subschemes glues them to an open \(T_W\subset T\).

Over \(T_W\), a lift to \(U\) locally lifts through \(h\), hence is joined by an arrow to an object of \(V\). Conversely, every object of \(V\) gives a lift in \(W\). Two objects of \(V\) define the same quotient section exactly when their pair of endpoints and its arrow define a section of \(R_V\), after an fppf refinement. Therefore

\[
T\times_{U/R}(V/R_V)=T_W.
\]

This proves representability and the description of the image. If (3.1) is an fppf covering, the same local-lifting argument gives every section a representative in \(V\); the equality argument remains valid. Thus the quotient map is an isomorphism. \(\square\)

*Reference:* [Stacks, Tag 04S2]. This proof uses descent for open subschemes of schemes; it does not assume that the target quotient is already algebraic.

The next operation changes objects as well as arrows. A **subgroupoid** \(P\subset R\) has all the objects of \(R\), contains the identities, and is closed under inversion and composition. Its arrows specify which changes of coordinates will first be forgotten.

For this operation we use the following exact affine scheme theorem: if \(U\) is affine and \(P\rightrightarrows U\) is an equivalence relation with finite locally free projections, then the fppf quotient is an affine scheme \(\bar U\), the map \(q:U\to\bar U\) is finite locally free and surjective, and

\[
P=U\times_{\bar U}U.
\tag{3.2}
\]

This is the finite flat affine quotient theorem [Stacks, Tag 03BM], proved in Appendix A below. It is stronger than the finite constant-group quotient proved in the first lesson; that special case alone would lose the inseparable example.

**Lemma 3.2 (division by a finite subgroupoid).** Let \(U\) be affine, let \(R\rightrightarrows U\) be a scheme groupoid, and suppose \(j=(t,s):R\to U\times_S U\) is separated and locally quasi-finite. Let \(P\subset R\) be a subgroupoid which is an equivalence relation and has finite locally free projections. Then there is a scheme groupoid \(\bar R\rightrightarrows\bar U=U/P\) with

\[
R=U\times_{\bar U,\bar t}\bar R
  \times_{\bar s,\bar U}U,
\qquad U/R=\bar U/\bar R.
\tag{3.3}
\]

Here \(\bar R\) parametrizes arrows whose two endpoints have been taken modulo \(P\). This is a double quotient; forgetting changes at only one endpoint would give a different object. If \(R\) is an equivalence relation, then \(\bar R\) is also an equivalence relation.

**Proof.** Obtain \(\bar U\) and \(q\) from the affine theorem. The map

\[
d=q\times q:U\times_S U\longrightarrow
\bar U\times_S\bar U
\]

is finite locally free and surjective. Its self-overlap identifies with \(P\times_S P\) by (3.2). Give \(R\), viewed as a scheme over \(U\times_S U\), the following descent datum. If

\[
r:x\to y,\qquad p:a\to y,\qquad p':b\to x
\]

with \(p,p'\in P\), replace \(r\) by the arrow

\[
p^{-1}\circ r\circ p':b\longrightarrow a.
\tag{3.4}
\]

This rule is a morphism of schemes, because inversion and composition are morphisms in the groupoid. It is invertible: given the replacement arrow \(v\), recover \(r=p\circ v\circ(p')^{-1}\). For a second pair of endpoint changes, applying (3.4) twice equals applying it once with the composed changes. Explicitly,

\[
p_2^{-1}\circ(p_1^{-1}\circ r\circ p'_1)\circ p'_2
=(p_1\circ p_2)^{-1}\circ r\circ(p'_1\circ p'_2).
\]

Thus associativity gives the descent cocycle. Effective fppf descent for separated locally quasi-finite schemes, the same scheme theorem used in the first lesson, now gives \(\bar R\to\bar U\times_S\bar U\) and the first isomorphism in (3.3).

We must also descend composition. Locally lift two composable arrows of \(\bar R\) to arrows \(r:x\to y\) and \(v:z\to w\) of \(R\), where \(q(y)=q(z)\). Equation (3.2) gives a unique arrow \(a:y\to z\) of \(P\), after placing the endpoint sections on a common fppf cover. Define the composite by the class of \(v\circ a\circ r\). Changing an outer endpoint changes this expression by (3.4). Changing either lift at the middle endpoint cancels against the corresponding change of \(a\); uniqueness of arrows in \(P\) and associativity give the same class. Hence this prescription is independent of all lifts and glues to a morphism

\[
\bar R\times_{\bar s,\bar U,\bar t}\bar R\longrightarrow\bar R.
\]

Identities and inverses descend in the same way. All groupoid laws can be checked on the surjective fppf covers by the original objects and arrows, where they are the laws of \(R\). This constructs the asserted scheme groupoid. If the original endpoint map is a monomorphism, the descended endpoint map is one too: its pullback by \(q\times q\) is the original map by (3.3), and monomorphisms descend along an fppf cover. The descended groupoid is then an equivalence relation.

Finally \(q\) and \(R\to\bar R\) are fppf epimorphisms. Every section of \(\bar U/\bar R\) locally has an object representative in \(U\). Two representatives define the same class precisely when, after refining the cover and choosing lifts of their arrow, they are joined in \(R\). The quotient sheaves are therefore equal. \(\square\)

*Reference:* [Stacks, Tag 04S3]. The effective descent input is [Stacks, Tag 02W8].

### 3.3. Transverse coordinates for a flat relation

We first prove the field case needed for slicing. Its scheme prerequisite is the **uniqueness of the constant field**: if a reduced connected scheme is locally of finite type over two fields, the integral closures of those fields in its ring of global functions coincide [Stacks, Tag 04MK]. For an integral scheme, each such integral closure is a field [Stacks, Tag 04MI]. These are results about ordinary schemes, rather than quotient representability.

**Field relation lemma.** Suppose \(R\rightrightarrows\operatorname{Spec}K\) is a scheme equivalence relation and both projections are locally of finite type. Then \(R\) has dimension zero.

**Proof.** Choose an affine neighbourhood \(\operatorname{Spec}B\) of the identity arrow. It is of finite type over \(K\) through both ring maps \(s,t:K\to B\). The identity gives a homomorphism \(e^*:B\to K\), with \(e^*s=e^*t=\operatorname{id}_K\). For a minimal prime \(\mathfrak p\subset\ker(e^*)\), the domain \(D=B/\mathfrak p\) is of finite type over both copies of \(K\), and the identity still gives \(D\to K\).

Let \(K_s,K_t\subset D\) be the integral closures of \(s(K),t(K)\). They are fields, and the constant-field theorem gives \(K_s=K_t\). The map \(D\to K\) is injective on each of these fields. Its restriction to \(s(K)\) is already surjective onto \(K\), so \(K_s=s(K)\); otherwise subtracting the element of \(s(K)\) with the same image would contradict injectivity. Similarly \(K_t=t(K)\). Thus \(s(K)=t(K)\) in \(D\), and the identity map shows that \(s(a)=t(a)\) for every \(a\in K\).

Consequently \(\operatorname{Spec}D\to R\) factors through the stabilizer at the object \(\operatorname{Spec}K\). That stabilizer is exactly the identity scheme: the endpoint map is a monomorphism and the identity supplies its unique arrow with equal endpoints. Hence every irreducible component of \(\operatorname{Spec}B\) through the identity consists of that single point. The local ring of \(R\) there has dimension zero. Since the identity is a \(K\)-rational point, the relative dimension at that point is also zero.

Now take an arbitrary point of \(R\) and represent it by an arrow \(r\) over its residue field \(L\). Its source and target are two maps \(\alpha,\beta:K\to L\). Composition gives an isomorphism of \(L\)-schemes

\[
R\times_{s,K,\alpha}\operatorname{Spec}L
\longrightarrow
R\times_{s,K,\beta}\operatorname{Spec}L,
\qquad a\longmapsto a\circ r^{-1}.
\]

It carries the selected arrow to the identity at its target. Relative dimension at a point is unchanged by extension of the ground field [Stacks, Tag 02FY], so the relative dimension at the original point is zero as well. Thus both projections are locally quasi-finite, and \(R\), locally of finite type over \(K\), has dimension zero. \(\square\)

This is the trivial-stabilizer case of [Stacks, Tag 04MQ]. The finite type hypothesis matters: it excludes relations on a generic field obtained by restricting a positive-dimensional orbit without a finite type coordinate map.

We also use openness of the flat locus for a locally finitely presented morphism [Stacks, Tag 0399], its compatibility with flat base change [Stacks, Tag 047C], and openness and arbitrary base change compatibility of the Cohen–Macaulay locus for a flat, locally finitely presented map [Stacks, Tag 045U]. The relative dimension zero locus is open and commutes with base change [Stacks, Tags 02FZ, 02FY and 0397]. Finally, the local flatness criterion [Stacks, Tag 046Z] says that cutting a flat local algebra essentially of finite presentation by an element regular on its fibre preserves flatness at that point. A Cohen–Macaulay fibre stays Cohen–Macaulay after a regular cut. These are statements about schemes and local rings.

Here a Cohen–Macaulay morphism means a flat morphism with Cohen–Macaulay fibres. We will apply the good-locus construction also to locally finitely presented morphisms which are not initially flat; their Cohen–Macaulay locus is the corresponding open within the open flat locus.

**Lemma 3.3 (a good locus is determined by the object).** Suppose \(s,t:R\to U\) are flat and locally of finite presentation, and \(g:V\to U\) is locally of finite presentation. Set \(Z=R\times_{t,U,g}V\), with \(h:Z\to U\) given by \(s\). The largest open of \(Z\) on which \(h\) is Cohen–Macaulay is the inverse image of an open of \(V\). The same assertion holds for the locally quasi-finite locus.

**Proof.** A point of \(Z\times_V Z\) consists of \(v\in V\) and two arrows

\[
r_1:x_1\to g(v),\qquad r_2:x_2\to g(v).
\]

Send it to \(r_2^{-1}\circ r_1:x_1\to x_2\). Together with the two projections to \(Z\), this gives two Cartesian squares over \(h:Z\to U\), using respectively \(s:R\to U\) and \(t:R\to U\). For example, fixing \((v,r_2)\) and an arrow \(a:x_1\to x_2\) recovers \(r_1=r_2\circ a\); this explicitly verifies one square. The other is verified by inversion.

The Cohen–Macaulay good locus commutes with these flat, locally finitely presented base changes. The relative dimension zero locus commutes with base change as well, and for locally finite type maps it is exactly the locally quasi-finite locus. Hence the inverse images of either good open along the two projections \(Z\times_V Z\rightrightarrows Z\) agree.

There is a section \(\sigma:V\to Z\), \(v\mapsto(e(g(v)),v)\). If \(O\subset Z\) is either good open, define \(W=\sigma^{-1}(O)\). Comparing any point of \(Z\) with the identity arrow at its object in the self-overlap shows that it belongs to \(O\) precisely when its image in \(V\) belongs to \(W\). Thus \(O=Z\times_V W\), and \(W\) is open. \(\square\)

*Reference:* [Stacks, Tag 04LH]. The argument uses openness and the stated base change compatibilities, rather than assuming that every flat locus is open for an arbitrary morphism.

**Lemma 3.4 (slicing a flat equivalence relation).** Let \(R\rightrightarrows U\) be a scheme equivalence relation with flat, locally finitely presented projections. There is a morphism \(g:V\to U\) such that the restricted relation has flat, locally finitely presented, locally quasi-finite projections and

\[
V/R_V\simeq U/R.
\tag{3.5}
\]

**Proof.** First we may make the source and target Cohen–Macaulay. Apply Lemma 3.3 with \(V=U\) and \(g=\operatorname{id}\). It gives an open \(U_0\subset U\) whose inverse image under \(t\) is the Cohen–Macaulay locus of \(s\). Inversion gives the analogous statement with \(s\) and \(t\) exchanged. Every source fibre has a dense Cohen–Macaulay open: it is locally of finite type over a field, its generic local rings have dimension zero, and the Cohen–Macaulay locus is open. In particular, this open meets every nonempty source fibre. All source fibres are nonempty because of the identities. Therefore

\[
t^{-1}(U_0)\xrightarrow{s}U
\]

is flat, locally finitely presented and surjective. Lemma 3.1 identifies the quotient with the quotient of the restricted relation over \(U_0\). In that restriction both projections are Cohen–Macaulay. Replace the original groupoid by this restriction.

Fix a point \(u\) which is closed in some affine open \(\operatorname{Spec}A\subset U\). Such points are also called finite type points. Write \(\mathfrak m\subset A\) for its maximal ideal. Choose affine coordinates \(\operatorname{Spec}B\subset R\) around the identity \(e(u)\), with both endpoints in \(\operatorname{Spec}A\), and let \(\mathfrak q\subset B\) represent \(e(u)\). The local source fibre ring is

\[
D=B_{\mathfrak q}/s(\mathfrak m)B_{\mathfrak q}.
\]

It is a Noetherian Cohen–Macaulay local ring of some finite dimension \(d\). Restricting both endpoints to \(u\) gives at the identity the ring

\[
D/t(\mathfrak m)D.
\]

The resulting groupoid has object scheme \(\operatorname{Spec}\kappa(u)\), locally finite type projections, and trivial stabilizer. The field relation lemma says that this ring has dimension zero. Thus the ideal generated by \(t(\mathfrak m)\) is primary to the maximal ideal of \(D\).

Choose \(f_1,\ldots,f_d\in\mathfrak m\) whose images \(t(f_i)\) form a system of parameters of \(D\). Here is why the parameters can be chosen from this particular ideal. If the current quotient has positive dimension, its finitely many minimal primes cannot contain the whole image of \(t(\mathfrak m)\), since the quotient by that image has dimension zero. Prime avoidance chooses an element of \(\mathfrak m\) avoiding all their inverse images. In a Cohen–Macaulay local ring this image is regular, and its quotient is Cohen–Macaulay with dimension reduced by one. Repeating constructs the required regular sequence. If \(d=0\), the sequence is empty.

Put

\[
V_u=\operatorname{Spec}A/(f_1,\ldots,f_d).
\]

The map \(V_u\to U\) is an immersion of finite presentation near \(u\). For

\[
h_u:R\times_{t,U}V_u\longrightarrow U,
\]

the fibre ring at the identity is \(D/(t(f_1),\ldots,t(f_d))\). Successive applications of the fibrewise regular-cut flatness criterion show that \(h_u\) is Cohen–Macaulay at this point. Its fibre there has dimension zero, so \(h_u\) is also locally quasi-finite there.

Apply Lemma 3.3 to both good loci and shrink \(V_u\) around \(u\), choosing an affine open in their intersection. The complete map \(h_u\), over this smaller object scheme, is now flat, locally finitely presented and locally quasi-finite. The source projection of the restricted relation is a base change of \(h_u\), so it has these three properties. Inversion supplies them for the target projection as well. This constructs a transverse slice through each finite type point.

Take the disjoint union \(V=\coprod_u V_u\), indexed by the finite type points, and restrict \(R\) to \(V\). On the component with endpoints in \(V_u,V_v\), its source projection is a base change of \(h_u\) along \(V_v\to U\). Hence every source and target projection of \(R_V\) is flat, locally finitely presented and locally quasi-finite.

The map \(h=\coprod_u h_u\) is flat and locally finitely presented. Its image is open and contains every finite type point, since each slice contains its identity. To prove surjectivity, suppose its closed complement were nonempty. Intersect the complement with an affine open meeting it; this nonempty closed subset of an affine scheme contains a closed point. That point is closed in an affine open of \(U\), so it is a finite type point of \(U\), contradicting the construction. Thus \(h\) is surjective. This argument uses more than density of the chosen points: a dense subset of an open need not make that open the whole scheme.

Now \(h\) is an fppf covering. Lemma 3.1 gives (3.5), and the earlier restriction to \(U_0\) has already preserved the quotient. \(\square\)

*Reference:* [Stacks, Tag 0489], in the slicing section, Tag 046L. The geometric step is the regular system of parameters pulled from the target maximal ideal; no assumption of smoothness or separability is made.

### 3.4. Keeping a finite part of the relation

**Lemma 3.5 (a finite open subgroupoid after étale localization).** Suppose \(U\) is affine and \(R\rightrightarrows U\) is a scheme equivalence relation whose projections are flat, locally finitely presented and locally quasi-finite. For each \(u\in U\), there is an affine scheme \(V\), an étale morphism \(V\to U\) whose image contains \(u\), and an open subgroupoid \(P\subset R_V\) with finite locally free projections.

**Proof.** First observe that \(s,t\) are separated. The endpoint morphism to \(U\times_{\mathbf Z}U\) is a monomorphism and hence separated, and its compositions with the two separated projections are separated. This allows us to use the separated scheme form of Zariski's main theorem.

Consider the functor \(Y\) over \(U\) whose points over \(T\to U\) are open-and-closed subschemes

\[
Z\subset R\times_{s,U}T
\]

which are finite over \(T\) and contain the identity section. Since \(s\) is flat and locally finitely presented, such a finite part is finite locally free. These parts descend under fppf covers: finite locally free schemes descend as affine schemes, and their inclusions descend as open immersions. Thus this is a sheaf, with a universal finite part once representability is established.

We spell out why it is étale locally described by ordinary schemes. For a separated locally quasi-finite scheme morphism, any finite open-and-closed part of a fibre extends to a finite open-and-closed part after an étale localization of the base. Work over the henselization at the chosen base point. Choose a quasi-compact open containing the finitely many selected fibre points and use Zariski's main theorem to embed it as an open in a finite scheme. Idempotents in the finite fibre algebra lift over the henselian base. Select the factors belonging to the prescribed fibre part. Their whole closed fibre lies in the chosen open, so their whole finite scheme lies there: the finite image of a nonempty closed complement would contain the closed point of the local base. The selected factors are therefore finite and open in the original scheme; separatedness also makes them closed. They are flat as opens of the original flat morphism, hence finite locally free. The finite presentation limit theorem descends this part from the henselization to an étale neighbourhood. Uniqueness over a henselian local base follows because the difference of two candidate parts is finite locally free, with zero rank on the closed fibre, and therefore zero rank everywhere.

This construction also supplies charts for parts over field extensions. A finite selection of open-and-closed fibre components is defined after a finite separable residue extension: idempotents are unchanged by purely inseparable extension, and their finitely many defining data over a separable closure descend to a finite stage. Applying the preceding lifting construction at that stage gives the required étale charts. The requirement to contain the identity is open and closed in these charts.

On overlaps of two charts, equality of their finite parts is representable by an open-and-closed subscheme of the base overlap. Indeed, both parts are closed in the separated ambient scheme, and their two differences are open-and-closed subschemes of finite locally free schemes. Their ranks are locally constant; equality means that both ranks vanish. The chart relation is consequently a scheme étale equivalence relation. The quotient theorem of the first lesson constructs \(Y\) as an algebraic space, and the local lifting and equality descriptions identify this quotient with the stated functor. Its map \(Y\to U\) is étale, and the same equality calculation makes its diagonal closed. Separated locally quasi-finite recognition, as stated in Section 2, now shows that \(Y\) is a scheme separated and étale over \(U\). This uses that recognition input, rather than the flat bootstrap we are proving.

The universal finite part has a groupoid structure over \(Y\). An object is a pair \((x,Z)\), with \(Z\) a finite part of the source fibre at \(x\) containing the identity. For an arrow \(r:x\to y\) lying in \(Z\), prescribe its target object to be

\[
(y,Zr^{-1}),
\qquad Zr^{-1}=\{a\circ r^{-1}:a\in Z\}.
\tag{3.6}
\]

Composition is an isomorphism of the appropriate source fibres, so the translated finite part is open and closed and finite locally free. It contains the identity at \(y\) because \(r\in Z\). Formula (3.6) defines a morphism to the representing scheme \(Y\). Inversion sends \((x,Z,r)\) to \((y,Zr^{-1},r^{-1})\), and applying it twice recovers the original triple. Thus both source and target of this groupoid are finite locally free.

If \(r'\) is an arrow starting at \((y,Zr^{-1})\), then \(r'r\in Z\), and its target finite part is

\[
Z(r'r)^{-1}=Zr^{-1}(r')^{-1}.
\]

This verifies closure under composition. The identities, inverse law and associativity follow from the original groupoid. Call this finite groupoid \(P\rightrightarrows Y\).

It is an open subgroupoid of \(R_Y\). Its arrow scheme is the universal finite open inside \(R\times_{s,U}Y\); over that open, the target prescription is a section of the étale projection \(R_Y\to R\times_{s,U}Y\). A section of an étale morphism is an open immersion. Moreover \(P\) is an equivalence relation, since its endpoint map factors through that of the restricted equivalence relation.

The source fibre \(R_u\) is a zero-dimensional locally finite type scheme over \(\kappa(u)\). The connected component supported at its identity is an Artinian scheme finite over \(\kappa(u)\), open and closed in that fibre. Choosing this part gives a \(\kappa(u)\)-point \(y\in Y\) over \(u\).

It remains to obtain affine coordinates without destroying the finite subgroupoid. The finite \(P\)-orbit of \(y\) is contained in a quasi-compact open \(W\subset Y\). Its map to the affine \(U\) is separated, quasi-finite and of finite type, so Zariski's main theorem makes \(W\) quasi-affine. A finite subset of a quasi-affine scheme lies in an affine open, by the ample finite-set lemma used in the first lesson. Choose such an affine open \(A\subset Y\) containing the orbit.

There is a \(P\)-invariant open \(D\subset A\) containing that orbit: remove the finite closed image of all arrows with at least one endpoint outside \(A\). Inversion and composition make the remaining open invariant. Choose a function \(f\) on \(A\) whose principal open contains the orbit and is contained in \(D\); prime avoidance in the ideal of \(A\setminus D\) provides it. On \(D\), take the norm of the target pullback of \(f\) along the finite locally free source projection of \(P_D\). The invariant-norm argument of Appendix A works for finite locally free sheaves as well as modules on an affine scheme. It gives an invariant function \(N\) on \(D\).

The open \(D_D(N)\) contains the orbit, because \(f\) is invertible at every point of each finite source fibre there. It is contained in \(D_A(f)\): an invertible norm makes the target pullback of \(f\) invertible, and the identity section then makes \(f\) invertible. Consequently

\[
D_D(N)=D_{D_A(f)}(N),
\]

an affine principal open of the affine scheme \(D_A(f)\). Put \(V=D_D(N)\). It is invariant, so restricting \(P\) to \(V\) preserves its finite locally free projections. It is affine, maps étale to \(U\), and contains \(y\). Its image contains \(u\), proving the lemma. \(\square\)

*References:* [Stacks, Tags 04RI, 04RU and 04S0]. The finite-part parameter, translation of a selected part, and invariant affine refinement are the three separate constructions in this proof. The henselian lifting step uses only the scheme form of Zariski's main theorem, lifting of idempotents in finite algebras, and descent of finitely presented scheme data along the system of étale neighbourhoods.

## 4. The flat quotient theorem

The remaining theorem of this lesson must handle more than an étale presentation. Its statement is:

**Theorem 4.1 (flat quotient theorem).** Let \(R\rightrightarrows U\) be a groupoid in algebraic spaces over \(S\), with source and target flat and locally of finite presentation. Suppose the endpoint map \(R\to U\times_S U\) is a monomorphism giving an equivalence relation. Then the fppf quotient \(U/R\) is an algebraic space, and \(U\to U/R\) is flat, locally of finite presentation and surjective. Equivalently, an fppf sheaf admitting a representable-by-spaces, flat, locally finitely presented surjection from an algebraic space is algebraic.

**Proof.** Choose an étale scheme presentation of \(U\) and restrict the relation to it. All quotient sections locally lift to this presentation, and its equality relation is the restricted relation, so this preserves the quotient sheaf. The restricted arrow space is algebraic; its endpoint map to a product of schemes is a locally finite type monomorphism, hence separated and locally quasi-finite. The recognition input in Section 2 makes it a scheme. We have reduced to a scheme relation.

Lemma 3.4 preserves the quotient while making its projections flat, locally finitely presented and locally quasi-finite. Cover its object scheme by affine opens. Lemma 3.1 makes their quotients open subfunctors of the original quotient. It suffices to prove algebraicity on each of these opens and glue, using the gluing theorem from the first lesson.

Thus take \(U\) affine. Lemma 3.5 supplies étale affine coordinates through every point of \(U\), each with a finite locally free open subgroupoid \(P\). Again their quotients are open subfunctors by Lemma 3.1, and these opens cover the quotient. On one such coordinate scheme, Lemma 3.2 and Theorem A.1 construct

\[
q:U\to\bar U=U/P,
\qquad\bar R\rightrightarrows\bar U,
\qquad U/R=\bar U/\bar R.
\]

The descended source and target are flat and locally of finite presentation. Indeed, their pullbacks by the finite locally free covering \(q\) become the original projections after a further finite locally free source cover. Flatness and local finite presentation descend along these covers, first on the source and then on the target.

The unit \(\bar e:\bar U\to\bar R\) is an open immersion. Its pullback along the finite locally free cover \(R\to\bar R\) is exactly \(P=U\times_{\bar U}U\to R\), which is open. Descent of open immersions proves the assertion.

This open unit forces the descended projections to be étale. To check this, take a geometric arrow \(r:x\to y\) over an algebraically closed field. Translation \(a\mapsto a r^{-1}\) identifies the source fibre at \(x\) with the source fibre at \(y\), taking \(r\) to the identity at \(y\). The identity has an open neighbourhood in that fibre consisting of \(\operatorname{Spec}k\), because the unit is open. Thus the local ring at every geometric arrow in every source fibre is \(k\). The fibres have zero relative differentials, and the locally finitely presented source map is unramified. Its flatness makes it étale. Inversion gives the same result for the target. The first quotient theorem now makes \(\bar U/\bar R\), hence \(U/R\), algebraic. Gluing over all the open quotient coordinates completes this part of the proof.

Let \(Q=U/R\). Equality of two local object sections is locally an arrow of \(R\), and uniqueness of an arrow with given endpoints descends that arrow. Therefore \(R=U\times_Q U\). For a scheme \(T\to Q\), the quotient construction gives an fppf scheme covering \(T_i\to T\) on which the section lifts to \(U\). Over \(T_i\), the morphism \(T\times_Q U\to T\) is a base change of a projection of \(R\). Flatness and local finite presentation descend along this covering, proving those properties for \(U\to Q\). Local lifting also proves surjectivity.

Finally suppose instead that an algebraic space \(X\) has a representable-by-spaces, flat, locally finitely presented surjection to an fppf sheaf \(F\). After taking a scheme presentation of \(X\), its self-fibre product over \(F\) is an algebraic space relation with the required flat projections. The surjection is an epimorphism of fppf sheaves: on a scheme test of \(F\), take a scheme presentation of its surjective flat locally finitely presented pullback to \(X\). Such an fppf covering locally lifts the tested section. Hence \(F\) is the quotient of this relation, to which the preceding proof applies. Conversely every quotient in the theorem has the asserted flat cover. This proves the equivalent formulation. \(\square\)

*Reference:* [Stacks, Tag 04S6]. The separated locally quasi-finite recognition is proved in Appendix B, and the field relation lemma and all three geometric reductions are proved in Section 3.

The distinction between the two quotient theorems already has concrete consequences. A flat group may have no étale coordinate map given by the original torsor. The examples below compute this directly.

**Corollary 4.2 (free flat group actions).** Let \(G\) be a group algebraic space over an algebraic space \(B\), flat and locally of finite presentation. Suppose \(G\) acts on an algebraic space \(X\) over \(B\), freely in the sense that

\[
G\times_B X\longrightarrow X\times_B X,
\qquad(g,x)\longmapsto(gx,x)
\]

is a monomorphism. Then the sheaf quotient \(Q=X/G\) is an algebraic space, \(X\to Q\) is flat, locally of finite presentation and surjective, and \(X\) is an fppf \(G\)-torsor over \(Q\).

**Proof.** The action groupoid has objects \(X\) and arrows \(G\times_B X\), with source \(x\) and target \(gx\). The source projection is a base change of \(G\to B\). The isomorphism \((g,x)\mapsto(g,gx)\), with inverse \((g,y)\mapsto(g,g^{-1}y)\), shows that the target projection has the same flatness and finite presentation properties. Freeness makes the endpoint map a monomorphism, and the group law supplies an equivalence relation. Thus the flat quotient theorem applies.

The equality relation for the quotient is precisely the action relation. Indeed, two object sections with the same quotient class are locally joined by an action arrow; the uniqueness supplied by freeness glues the local arrows. Therefore

\[
G\times_B X\simeq X\times_Q X.
\tag{4.1}
\]

This is the torsor identity. To obtain a covering by schemes which trivializes the torsor, choose a scheme presentation of \(X\) and affine opens in that presentation. Their compositions to \(Q\) are flat and locally of finite presentation, and together are surjective. On a scheme which maps to \(X\), the resulting chosen object section and (4.1) identify the pulled-back torsor with \(G\) times that scheme. This gives an fppf local trivialization and proves all the assertions. \(\square\)

*Reference:* [Stacks, Tag 06PH]. Here freeness concerns all test schemes, including those with nilpotents. Triviality of stabilizers on algebraically closed field points alone would not suffice for a nonreduced group such as \(\mu_p\).

### A historical distinction

Grothendieck's *FGA*, Exposé 212, §8, Conjecture 8.1 concerns free projective-group actions in moduli problems. It asks for a scheme quotient and, when the action respects a relatively very ample line bundle, for the descended bundle to be relatively pre-ample. Here pre-ampleness means that a power comes from the hyperplane bundle under a quasi-finite map to projective space; the discussion relates it to ampleness when the quotient is separated. The erratum to that exposé and the addendum to Exposé 221 explicitly retract the conjecture, even for nonsingular varieties in characteristic zero and actions with closed graph. The flat bootstrap proves existence of an **algebraic space** quotient. It does not assert the stronger scheme or pre-ampleness conclusions of the retracted conjecture. See the [English FGA reading edition, Exposé 212, §8 and its erratum](https://github.com/KokunoYumeto/fga-en/blob/b987b99fbdaff80efb9f23815a3583fa0a52d284/releases/2026-08-30-r1/fga-en-canon-errata-0001-0017.pdf).

## 5. Examples with flat groups

### 5.1. Scalar multiplication and projective space

Let \(n\geq1\), and work over any base scheme \(S\). The group \(\mathbf G_m\) acts by scalar multiplication on \(\mathbf A^n_S\setminus\{0\}\), where the complement means the open on which the coordinate functions generate the unit ideal. This is a free action: a scalar fixing a unimodular vector has to be one.

The map to \(\mathbf P^{n-1}_S\) sends a vector to its generated line. Over the chart on which the \(i\)-th homogeneous coordinate is nonzero, a vector is uniquely a scalar times the vector whose \(i\)-th coordinate is one. Hence the map is locally the projection

\[
\mathbf G_m\times\mathbf A^{n-1}_S\longrightarrow\mathbf A^{n-1}_S.
\]

Two vectors give the same line precisely when one is the unique scalar multiple of the other. These chart calculations prove both the torsor identity and local sections, so the fppf quotient is \(\mathbf P^{n-1}_S\). The construction identifies the quotient sheaf, rather than only its points over algebraically closed fields.

### 5.2. A torsor with inseparable fibres

Let \(k\) have characteristic \(p>0\). On \(\mathbf G_m\), use the action of \(\mu_p\) by multiplication. The map

\[
q:\mathbf G_m\longrightarrow\mathbf G_m,
\qquad x\longmapsto x^p
\]

has coordinate algebra inclusion \(k[y,y^{-1}]\to k[x,x^{-1}]\), \(y\mapsto x^p\). The target algebra is free of rank \(p\) over the source, with basis \(1,x,\ldots,x^{p-1}\). Thus \(q\) is finite, faithfully flat and finitely presented.

Its fibre relation has coordinates \(x_1,x_2\) with \(x_1^p=x_2^p\). Since both coordinates are invertible, put \(u=x_2/x_1\). The relation is \(u^p=1\), giving the isomorphism

\[
\mathbf G_m\times\mu_p\simeq
\mathbf G_m\times_{q,\mathbf G_m,q}\mathbf G_m.
\]

The map \(q\) has sections fppf locally simply by pulling it back along itself. Therefore it is a \(\mu_p\)-torsor, and its quotient sheaf is the target \(\mathbf G_m\). It is not étale: the relative differential \(dx\) is nonzero, because the derivative of \(x^p-y\) with respect to \(x\) is zero. Equivalently, its geometric fibres are nonreduced of length \(p\).

This example works out the quotient directly. It shows why the flat quotient theorem cannot insist that the original cover be étale.

## 6. Exercises and solutions

**Exercise 6.1 (easy: successive base changes).** Suppose \(F\to H\to K\) are representable by algebraic spaces. Explain why a scheme test of \(F\to K\) can be carried out even though its intermediate fibre product is an algebraic space. Prove also that an arbitrary base change of \(F\to H\) is representable by algebraic spaces.

**Solution.** For a scheme \(T\to K\), the intermediate fibre product \(Y=T\times_K H\) is algebraic. The morphism \(T\times_K F\to Y\) is representable by spaces, as follows by testing it on scheme points of \(Y\) and using the hypothesis on \(F\to H\). Proposition 1.1, whose proof constructs an atlas and equality schemes for the source, then makes \(T\times_K F\) algebraic. This proves composition. If \(H'\to H\) is arbitrary and \(T\to H'\) is a scheme test, its pullback of \(F\times_H H'\) is \(T\times_H F\), which is algebraic by the original hypothesis. This proves base change.

**Exercise 6.2 (medium: freeness with infinitesimal points).** Using the final bootstrap theorem, prove the torsor assertion for a free action of a flat, locally finitely presented group algebraic space. Identify the place where scheme-theoretic freeness enters, and explain why the action of \(\mu_p\) on a point in characteristic \(p\) does not meet that hypothesis.

**Solution.** Source and target in the action groupoid are flat and locally finitely presented: one is the projection from \(G\times_B X\), and the other is obtained from it through the invertible change \((g,x)\mapsto(g,gx)\). Scheme-theoretic freeness makes the endpoint map a monomorphism, so the flat bootstrap gives an algebraic quotient. Equality of two quotient sections is locally an action arrow; freeness gives uniqueness, allowing these local arrows to descend. Hence the action relation is \(X\times_Q X\), as in (4.1). Scheme presentations of \(X\), followed by affine open coverings, give fppf covers of \(Q\) with a chosen lift to \(X\); translating that lift trivializes the torsor. This proves Corollary 4.2 from the final theorem.

On a point, every element of \(\mu_p(T)\) is a stabilizer. For \(T=\operatorname{Spec}k[\epsilon]/(\epsilon^2)\), the element \(1+\epsilon\) has \(p\)-th power one and is not the identity. Thus its endpoint map cannot be a monomorphism, although \(\mu_p\) has only the identity point over an algebraically closed field of characteristic \(p\).

**Exercise 6.3 (medium: starting in the étale topology).** Let \(F\) be a sheaf on the big étale site of \(S\), with diagonal representable by schemes. Suppose a scheme \(U\) maps to \(F\), representably, surjectively and étale. Prove that \(F\) is an algebraic space; in particular, prove the fppf sheaf condition instead of assuming it.

**Solution.** The diagonal makes \(R=U\times_F U\) a scheme, and the two projections are étale by base change of the cover. It is an equivalence relation. The first lesson constructs the algebraic space \(X\) which is its fppf quotient, with \(U\to X\) a representable surjective étale map and \(R=U\times_X U\).

The cover \(U\to X\) is also an epimorphism in the étale topology: every scheme point of \(X\) pulls it back to a surjective étale scheme cover and thus locally lifts to \(U\). Consequently \(X\), regarded as an étale sheaf, is the étale quotient of \(U\) by \(R\). The same is true of \(F\) by its assumed cover and equality relation. The two quotient identifications give \(F\simeq X\) as functors on schemes. Since \(X\) is an fppf sheaf, so is \(F\), and the asserted algebraic space conditions follow. No comparison theorem for arbitrary étale sheaves is being assumed. This is the recognition principle in [Stacks, Tag 076M].

**Exercise 6.4 (medium: a proper acting group).** Let a group scheme \(G\), proper, flat and locally of finite presentation over \(S\), act freely on a separated \(S\)-scheme \(X\). Prove that its algebraic-space quotient is separated over \(S\).

**Solution.** Apply Corollary 4.2 to obtain \(Q=X/G\) and its fppf torsor map. The endpoint morphism

\[
j:G\times_S X\longrightarrow X\times_S X
\]

is proper. To verify this without assuming that the action morphism itself is proper, factor \(j\) as the graph which remembers \((g,x,gx)\) in \(G\times_S X\times_S X\), followed by projection to \(X\times_S X\). The graph is closed because \(X\to S\) is separated; the projection is a base change of the proper map \(G\to S\). Freeness makes \(j\) a monomorphism. A proper monomorphism is a closed immersion, so the action relation is closed in \(X\times_S X\).

This morphism is the pullback of \(\Delta_{Q/S}\) along the fppf cover \(X\times_S X\to Q\times_S Q\). Closed immersions descend under fppf covers, checked after scheme presentations of the target. Thus \(\Delta_{Q/S}\) is a closed immersion and \(Q\to S\) is separated. The argument needs both properness of the group and separatedness of \(X\) at the indicated factorization.

**Exercise 6.5 (medium: a purely inseparable quotient).** In characteristic \(p\), use coordinate rings to compute the quotient for multiplication by \(\mu_p\) on \(\mathbf G_m\). Determine the degree of the quotient map, its relation, and why it is not étale.

**Solution.** Put \(A=k[x,x^{-1}]\) and \(C=k[y,y^{-1}]\), with \(y\mapsto x^p\). Every Laurent monomial has a unique exponent modulo \(p\), so \(A\) is free over \(C\) on \(1,x,\ldots,x^{p-1}\). The map is faithfully flat of degree \(p\). Its relation algebra is

\[
A\otimes_C A
\simeq k[x_1^{\pm1},x_2^{\pm1}]/(x_1^p-x_2^p).
\]

Putting \(u=x_2/x_1\) identifies this with \(k[x_1^{\pm1},u]/(u^p-1)\), the algebra of \(\mathbf G_m\times\mu_p\). Hence it is the action relation. Since the quotient map itself is an fppf cover and its fibres are precisely this relation, its quotient sheaf is \(\operatorname{Spec}C=\mathbf G_m\). The relation also proves scheme-theoretic freeness. The map is not étale: \(\Omega_{A/C}\) is generated by the nonzero element \(dx\), and the derivative of \(x^p-y\) provides no relation on it. Its geometric fibres are nonreduced of length \(p\). This computation proves the example without using the general bootstrap theorem.

## Appendix A. The finite flat affine quotient

**Theorem A.1.** Let \(P\rightrightarrows U\) be a scheme equivalence relation with \(U=\operatorname{Spec}A\) affine and with both projections finite locally free. Put \(P=\operatorname{Spec}B\), and write the two ring maps as \(s,t:A\to B\). Define

\[
C=\{a\in A:s(a)=t(a)\}.
\]

Then \(A\) is a faithfully flat finite locally free \(C\)-algebra, the endpoint map identifies

\[
B=A\otimes_C A,
\tag{A.1}
\]

and \(\operatorname{Spec}C\) represents the fppf quotient \(U/P\). The empty scheme is allowed, with the evident empty quotient.

**Proof.** We first make three algebraic observations, keeping the groupoid structure in view.

*Invariant characteristic polynomials.* The rank of \(B\) as an \(A\)-module through \(s\) is locally constant on \(U\), and it takes the same value at two objects joined by an arrow. Indeed, composition by that arrow identifies the two source fibres after the common field extension needed to represent the arrow. Finite locally free ranks are unchanged by field extension. The rank strata are therefore invariant open-and-closed subschemes of \(U\). Their idempotents belong to \(C\). There are finitely many strata because \(U\) is quasi-compact. We may treat them separately and assume that the rank is the positive integer \(r\).

For \(a\in A\), consider multiplication by \(t(a)\) on the finite locally free \(s(A)\)-module \(B\). Its characteristic polynomial has coefficients in \(A\). These coefficients lie in \(C\): over an arrow \(x\to y\), composition identifies the source fibre over \(y\) with the source fibre over \(x\), while preserving the target of each arrow in those fibres. Consequently the two pullbacks of the multiplication operator are conjugate. Characteristic polynomials commute with base change and conjugation, so the coefficients have equal \(s\)- and \(t\)-images. Applying the identity section to the Cayley–Hamilton equation shows that \(a\) satisfies this monic polynomial. Thus \(C\subset A\) is integral. In particular, \(\operatorname{Spec}A\to\operatorname{Spec}C\) is surjective by lying over. The same argument shows that

\[
N(a)=\det_s\bigl(\text{multiplication by }t(a)\text{ on }B\bigr)
\quad\text{belongs to }C.
\tag{A.2}
\]

*Generation of the relation algebra.* The morphism \(P\to U\times_{\mathbf Z}U\) is a finite monomorphism. To see finiteness, factor it as the graph of the second endpoint followed by a base change of the finite first projection; the graph is closed because the affine scheme \(U\) is separated over \(\mathbf Z\). A finite monomorphism of schemes is a closed immersion. Therefore \(A\otimes_{\mathbf Z}A\to B\) is surjective. Since \(s\) and \(t\) agree on \(C\), it factors through a surjection

\[
\theta:A\otimes_C A\longrightarrow B,
\qquad a\otimes a'\longmapsto s(a)t(a').
\tag{A.3}
\]

This argument works even when the original base \(S\) is not separated or affine.

*Flat extension of the invariant ring.* The sequence

\[
0\longrightarrow C\longrightarrow A
\xrightarrow{s-t}B
\]

is exact as a sequence of \(C\)-modules. Tensoring with a flat \(C\)-algebra \(D\) preserves the kernel. Hence the invariant ring after this base change is exactly \(D\). In particular, no assertion that invariants commute with arbitrary base change is needed.

We next prove the theorem after suitable faithfully flat local extensions of \(C\). Fix a prime \(\mathfrak p\subset C\). Starting with \(C_{\mathfrak p}\), localize the polynomial algebra \(C_{\mathfrak p}[z]\) at the prime \(\mathfrak p C_{\mathfrak p}[z]\). The resulting local ring \(D\) is faithfully flat over \(C_{\mathfrak p}\), and its residue field is \(\kappa(\mathfrak p)(z)\), which is infinite. By the preceding observation, we can replace \(C,A,B\) by \(D,A\otimes_C D,B\otimes_C D\). We now have a local invariant ring \(C\), with maximal ideal \(\mathfrak m\) and infinite residue field.

We claim that \(A\) is semilocal. Integrality shows that all its maximal ideals lie over \(\mathfrak m\). Each topological orbit in \(\operatorname{Spec}A\) is finite: it is the set of targets of points of the finite source fibre over any object in that orbit. Inversion and composition make this an equivalence relation on points. When two arrows share only an underlying endpoint, their composition exists after extending their residue fields to a common field; this suffices to establish transitivity on underlying points.

If there were two distinct orbits of maximal ideals, the Chinese remainder theorem would give \(f\in A\) which is zero at every maximal ideal of the first orbit and one at every maximal ideal of the second. Evaluate (A.2) at an object in the first orbit. On its finite Artinian source fibre, \(t(f)\) is nilpotent, so its determinant is zero. On a source fibre in the second orbit, \(t(f)-1\) is nilpotent, so its determinant is one. But \(N(f)\in C\), and these two values come from its single residue in \(C/\mathfrak m\). A residue cannot map to both zero and one in field extensions. Thus there is only one orbit of maximal ideals. It is finite, proving the claim.

The finite locally free \(s(A)\)-module \(B\) has constant rank \(r\). By (A.3), it is generated by elements of \(t(A)\); choose a finite list \(t(f_1),\ldots,t(f_m)\) of such generators. We can choose \(r\) linear combinations of this list, with coefficients in \(C\), which form a basis simultaneously at every maximal ideal of \(A\). Here are the details of this small generic-choice argument. At each of the finitely many maximal ideals, an \(r\)-by-\(r\) determinant in the coefficients is a nonzero polynomial over its residue field. The common subfield \(C/\mathfrak m\) is infinite. A nonzero polynomial over a field extension cannot vanish on every tuple from this subfield: expand its finitely many coefficients in a basis of their span over the subfield and retain a nonzero coordinate polynomial. Avoiding the finitely many resulting nonzero polynomials gives one tuple of coefficients good at all maximal ideals. Lift those coefficients to \(C\), and call the corresponding elements of \(A\)

\[
x_1,\ldots,x_r.
\]

Nakayama's lemma makes \(t(x_1),\ldots,t(x_r)\) generators of \(B\) over \(s(A)\). Since \(B\) is projective of constant rank \(r\), the surjection \(A^r\to B\) is an isomorphism: locally at each maximal ideal it is a surjection between free modules of the same rank. Thus

\[
B=\bigoplus_{i=1}^r s(A)t(x_i).
\tag{A.4}
\]

The groupoid laws now force the same elements to be a basis of \(A\) over \(C\). For \(a\in A\), write its unique expansion

\[
t(a)=\sum_i s(a_i)t(x_i).
\tag{A.5}
\]

Use the algebra of composable pairs

\[
E=B\otimes_{s,A,t}B.
\]

In this convention an arrow in the left factor follows an arrow in the right factor. Composition has ring map \(c^*:B\to E\), with

\[
c^*t(a)=t(a)\otimes1,
\qquad c^*s(a)=1\otimes s(a).
\]

Applying \(c^*\) to (A.5), and also applying the inclusion of the left tensor factor, gives two expansions of \(t(a)\otimes1\). By (A.4), the elements \(t(x_i)\otimes1\) form a basis of \(E\) as a module over its right factor. The tensor relation identifies \(s(a_i)\otimes1\) with \(1\otimes t(a_i)\). Comparing coefficients therefore yields

\[
t(a_i)=s(a_i)\qquad\text{for every }i.
\]

Thus every \(a_i\) lies in \(C\). The identity section makes \(t\) injective, so (A.5) implies \(a=\sum_i a_i x_i\). Applying \(t\) and using (A.4) also proves linear independence over \(C\). We obtain

\[
A=\bigoplus_{i=1}^r Cx_i.
\]

Consequently (A.3) is an isomorphism: it takes the \(A\)-basis \(1\otimes x_i\) to the basis (A.4). This proves the required finite freeness and relation identity after the faithfully flat local extension at every prime of the original \(C\).

Return to the original rings. Faithfully flat descent at each prime proves that \(\theta\) is an isomorphism and that \(A\) is flat over \(C\). Lying over makes this flat map faithfully flat. Now \(A\otimes_C A=B\) is a finite locally free module over \(A\), so descent of finite projective modules along the faithfully flat map \(C\to A\) proves that \(A\) itself is finite locally free over \(C\). These module-descent statements apply without a Noetherian hypothesis.

Finally \(\operatorname{Spec}A\to\operatorname{Spec}C\) is an fppf epimorphism and its fibre relation is \(P\) by (A.1). The local-coordinate description of a sheaf quotient therefore identifies \(U/P\) with \(\operatorname{Spec}C\). \(\square\)

*Reference:* [Stacks, Tag 03BM]. Scheme and algebra inputs used here are Cayley–Hamilton for finite locally free modules, lying over for integral extensions, the Chinese remainder theorem, finite monomorphisms being closed immersions, Nakayama's lemma, and faithfully flat descent of finite projective modules. The proof includes the invariant-polynomial and basis arguments rather than assuming that the affine quotient is effective.

## Appendix B. Separated quasi-finite spaces over schemes

The following descent argument explains why separatedness rules out the pathological quotients of the first lesson. It also closes the recognition step used in both bootstrap proofs.

**Lemma B.1 (descending an affine neighbourhood).** Let \(X\to T\) be separated and locally quasi-finite, with \(T\) affine. Let \(T'\to T\) be étale with \(T'\) affine, and suppose \(V'\subset X\times_T T'\) is an affine open subspace. Then the image \(W\subset X\) of \(V'\) is an open subspace represented by a scheme.

**Proof.** The map to \(X\) is étale, so its image is open. An étale map of affine schemes has a uniform finite bound \(n\) on the cardinalities of its geometric fibres. For instance, it is quasi-finite and separated, and the scheme form of Zariski's main theorem embeds its source in a finite scheme over \(T\); a finite list of module generators for that finite scheme bounds the dimensions of all its fibre algebras, hence the number of geometric points. We induct on such a bound.

When \(n\leq1\), the étale morphism is universally injective and therefore an open immersion. Thus \(X\times_T T'\) is an open subspace of \(X\), and \(W=V'\) is already a scheme. The empty case is included.

For \(n>1\), separate the diagonal in the affine self-overlap:

\[
T'\times_T T'=\Delta(T')\amalg T^*.
\]

The diagonal is open because the map is étale, and closed because it is separated. Hence \(T^*\) is affine. Each projection \(T^*\to T'\) is étale and has geometric fibre cardinality at most \(n-1\): one diagonal point has been removed from each fibre of the full base change.

Put \(X'=X\times_T T'\). In the corresponding self-overlap \(X'\times_X X'\), let \(p_0,p_1\) be the two projections, and let \(X^*\) be its part over \(T^*\). The open

\[
V^*=p_0^{-1}(V')\cap X^*
\]

is affine: it is the base change of the affine map \(V'\to T'\) along the first projection \(T^*\to T'\). Apply the induction hypothesis with base \(T'\), cover \(T^*\to T'\) given by the second projection, ambient space \(X'\), and affine open \(V^*\). Its image \(p_1(V^*)\) is a scheme open in \(X'\). The diagonal part of the overlap contributes \(V'\), so

\[
p_1(p_0^{-1}(V'))=V'\cup p_1(V^*)
\]

is a scheme, glued from two open subschemes. This saturated image is exactly \(X'\times_X W=T'\times_T W\). The identity is valid as an equality of open subspaces: over any test scheme an object lies in the saturation precisely when, after an étale refinement, it has a lift in \(V'\).

Let \(O\subset T\) be the open image of \(T'\to T\). The map \(W\to T\) factors through \(O\), and \(T'\to O\) is an fppf cover. We have just proved that its pullback \(T'\times_O W\) is a scheme. Its morphism to \(T'\) is separated and locally quasi-finite, by base change of \(X\to T\). Its canonical descent datum is effective by the scheme theorem [Stacks, Tag 02W8]. The descended scheme represents \(W\): both represent the sheaf obtained by descent from the same pullback and equality data. This completes the induction. \(\square\)

*Reference:* Compare [Stacks, Tag 03XW]. The last step here uses the separated locally quasi-finite scheme descent theorem already assumed in the first lesson.

**Theorem B.2 (separated locally quasi-finite recognition).** If \(X\to T\) is a separated locally quasi-finite morphism of algebraic spaces and \(T\) is a scheme, then \(X\) is a scheme.

**Proof.** The assertion is local on the target for open coverings. Replace \(T\) by an affine open and \(X\) by its inverse image. Choose a scheme presentation of \(X\) and cover its source by affine opens. Their images are open subspaces of \(X\). If each such image is a scheme, they glue to make \(X\) a scheme. We may therefore assume that an affine scheme \(U\) has an étale surjection to \(X\).

The composite \(U\to T\) is a quasi-finite separated scheme morphism: local quasi-finiteness is stable under the composition with an étale map, and a map of affine schemes is quasi-compact and separated. The relation

\[
R=U\times_X U
\]

is a closed subscheme of \(U\times_T U\), since \(X\to T\) is separated. Thus \(R\) is affine and its two projections to \(U\) are étale.

Fix \(u\in U\), with image \(p\in T\). We claim that, after an affine étale neighbourhood \(T'\to T\) of \(p\), the base change of \(U\) contains a finite open-and-closed subscheme \(U'\) with a point over \(u\). This is a scheme localization, which can be constructed explicitly from Zariski's main theorem. Embed \(U\) as an open in a finite scheme \(\widetilde U\) over \(T\). Over the henselization at \(p\), the finite algebra splits into the factors of its closed fibre. Select the factors whose closed fibre belongs to \(U_p\). Each selected factor lies wholly in the open \(U\), because its finite closed complement would otherwise have nonempty image containing the closed point. These factors are consequently finite and open and closed in the base change of \(U\), and they contain its whole fibre at \(p\). Their defining idempotents descend to an étale neighbourhood. If necessary, shrink that neighbourhood to avoid the finite closed image of the portions of the selected factors lying outside the open \(U\). This yields the asserted \(U'\). The neighbourhood may be chosen with its distinguished residue field equal to \(\kappa(p)\), so a point over \(u\) remains present. No flatness of \(U\to T\) is used in this construction.

Restrict the relation to \(U'\). Its endpoint map

\[
R'=U'\times_{X\times_T T'}U'
\longrightarrow U'\times_{T'}U'
\]

is closed. Since \(U'\) is finite over \(T'\), this makes both projections \(R'\to U'\) finite. They remain étale, because the restriction is by an open subscheme. Thus \(U'\) and \(R'\) are affine and the projections are finite locally free. Theorem A.1 gives an affine scheme quotient \(V'=U'/R'\).

The quotient \(V'\) is the open image of \(U'\) in \(X\times_T T'\), by the open-image result of Lemma 3.1 applied to this étale presentation. It contains the image of the selected point over \(u\). Lemma B.1 now makes its image \(W\subset X\) a scheme open containing the image of \(u\). This works for every point of the presentation and hence every point of \(X\). These scheme opens glue to represent \(X\). \(\square\)

*Reference:* [Stacks, Tag 03XX]. The proof has used only the first quotient theorem, the independently proved finite affine quotient of Appendix A, scheme Zariski main and henselian idempotent lifting, and effective scheme descent [Stacks, Tag 02W8]. Neither bootstrap theorem is used, so the dependency order is acyclic.

## What this lesson does not prove

The quotient, slicing, division, finite-part and recognition arguments have been proved above. Their inputs from scheme theory and commutative algebra are used as prerequisites:

- Effective fppf descent for separated locally quasi-finite schemes [Stacks, Tag 02W8], already stated in the first lesson; the scheme form of Zariski's main theorem for a quasi-finite separated map to a quasi-compact quasi-separated scheme [Stacks, Tag 05K0]; the decomposition of a finite algebra over a henselian local ring into local factors [Stacks, Tag 04GH]; and descent of finitely presented scheme data and finite local freeness along filtered limits with affine transition maps [Stacks, Tags 01ZM and 06AC].
- The uniqueness of the constant field for a reduced connected scheme locally of finite type over two fields [Stacks, Tag 04MK], and the integral-closure field fact [Stacks, Tag 04MI]. These supply the scheme-theoretic input to the field relation lemma.
- Openness of flatness [Stacks, Tag 0399], flat base change for that locus [Stacks, Tag 047C], the Cohen–Macaulay locus theorem [Stacks, Tag 045U], relative dimension and its base change properties [Stacks, Tags 02FZ, 02FY and 0397], and the regular-cut flatness criterion with the hypotheses stated in Section 3.3 [Stacks, Tag 046Z].
- Cayley–Hamilton, lying over, prime avoidance, the Chinese remainder theorem, Nakayama's lemma, and faithfully flat descent of finite projective modules [Stacks, Tags 03C4 and 00NX]. Their roles in the invariant-ring argument are identified in Appendix A.
- Descent of open and closed immersions and of flat, locally finitely presented morphisms; finite monomorphisms and proper monomorphisms being closed immersions; and the ample finite-set lemma for schemes, used in the first lesson.

## References

- **[Stacks]** The Stacks project, *Bootstrap*, Tags 03Y3, 04S2, 0489 (in Section 046L), 04S3, 04S6, 06PH and 076M. Read these in [AI Integrated Stacks Project, Bootstrap](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/bootstrap.html). The auxiliary references are *Groupoids*, Tag 03BM; *More on Groupoids*, Tags 04LH and 04MQ; *More on Groupoids in Algebraic Spaces*, Tags 04RI, 04RU and 04S0; *Morphisms of Algebraic Spaces*, Tags 03XW and 03XX; and *Varieties*, Tags 04MI and 04MK. AI Integrated Stacks Project retains the upstream tags; its additions and corrections are not reviewed by the Stacks project's maintainers.
- **Grothendieck, *FGA*.** Exposé 212, *Préschémas quotients*, §8, Conjecture 8.1 and its erratum; Exposé 221, addendum. Historical motivation and the explicit retraction, rather than a proof of the bootstrap theorem. [English reading edition](https://github.com/KokunoYumeto/fga-en).
