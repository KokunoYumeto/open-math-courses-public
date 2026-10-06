# Pushforward, pullback and finite morphisms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Links and citations revised by Claude Opus 5.5 (Anthropic), October 2026. Public domain (CC0).*

A pushforward records sections on the inverse image of a neighbourhood. Its geometric stalk therefore sees a scheme over a strict henselization, rather than just an ordinary fibre. For a finite morphism that scheme separates into finitely many strictly local pieces. The pushforward stalk is a product of their stalks, and its higher cohomology vanishes.

We develop this calculation before closed immersions and topological invariance. The same local argument proves that an integral universal homeomorphism, even one which is not finite, preserves all étale sheaves and their cohomology. At a node, however, normalization separates two branches; its pushforward need not be locally constant.

The prerequisites are [The étale site and its points](the-etale-site-and-its-points.md), the site morphisms and cohomology of lessons 2–3, and affine geometry: finite and integral algebras, lying over, Artinian algebras, finite projective modules and the square Jacobian criterion. We state the cohomological continuity theorem precisely where used. We retain the universe convention of lesson 5. Write \(f^{-1}\) for sheaves of sets or abelian groups; \(f^*\) denotes pullback of modules over a structure sheaf.

## 1. Pullback transports the selected geometric point

Let \(f:X\to Y\) be any scheme morphism. Base change defines

\[
u:Y_{\mathrm{ét}}\longrightarrow X_{\mathrm{ét}},
\qquad V\longmapsto X_V=X\times_Y V.
\tag{1.1}
\]

It takes the final object to the final object, preserves fibre products and preserves covers: an étale surjective family stays such after base change. Consequently

\[
(f_*F)(V)=F(X_V)
\tag{1.2}
\]

is a sheaf whenever \(F\) is a sheaf. Indeed its matching diagram is exactly the matching diagram on the base-changed covering. It is functorial in \(F\), and preserves all limits, since those are computed objectwise for sheaves.

The site-morphism construction of lesson 2 supplies its left adjoint. Explicitly \(f^{-1}G\) is the sheafification of

\[
U\longmapsto
\operatorname*{colim}_{(V,\ a:U\to X_V)}G(V).
\tag{1.3}
\]

In this colimit a map \(V'\to V\) whose base change carries \(a':U\to X_{V'}\) to \(a\) gives the restriction \(G(V)\to G(V')\). The indexing category with this orientation is filtered: use \(Y\) for nonemptiness, \(V\times_Y V'\) for two maps out of \(U\), and the open equalizer for two parallel compatible maps. An empty \(U\) causes no exception to these finite-limit constructions. Thus the presheaf functor in (1.3) preserves finite limits. Sheafification does too, and the universal property of the colimit and sheafification gives

\[
\operatorname{Hom}_X(f^{-1}G,F)
=\operatorname{Hom}_Y(G,f_*F).
\tag{1.4}
\]

As a left adjoint it also preserves colimits. It is exact on abelian sheaves, by the abelian inverse-image result of lesson 2. Its right adjoint \(f_*\) therefore preserves injectives: extending a map into \(f_*I\) across a monomorphism is, by (1.4), extending the corresponding map into \(I\) across the monomorphism obtained by exact \(f^{-1}\).

**Proposition 1.1.** For a geometric point \(\bar x\) of \(X\), put \(\bar y=f\bar x\). There is a natural identification

\[
(f^{-1}G)_{\bar x}=G_{\bar y}.
\tag{1.5}
\]

Also \(f^{-1}h_V=h_{X_V}\) for every étale \(V\to Y\).

**Proof.** Stalks ignore sheafification by lesson 6, so (1.3) represents the left side by a section \(s\in G(V)\), a pointed neighbourhood \((U,\bar u)\) of \(\bar x\), and a map \(a:U\to X_V\). Send this representative to the germ of \(s\) at the induced lift \(\bar v\) of \(\bar y\). This respects both types of refinement.

Conversely a germ represented on \((V,\bar v)\) is represented on the left by \(U=X_V\), its paired lift \((\bar x,\bar v)\), and the identity map. This proves surjectivity. Given an arbitrary left-side representative, the pointed arrow \(U\to X_V\) identifies it with this particular representative for \((V,\bar v)\). If two resulting \(Y\)-germs agree, realize their equality on a common pointed refinement \(V'\); its base change \(X_{V'}\) identifies the left-side germs as well. This proves injectivity and both inverse identities. The construction commutes with maps of \(G\).

Finally (1.4) and Yoneda give, naturally in \(F\),
\(\operatorname{Hom}(f^{-1}h_V,F)=F(X_V)=\operatorname{Hom}(h_{X_V},F)\).
Representables are sheaves by lesson 5, so Yoneda identifies these objects. \(\square\)

Base change associativity in (1.2) gives \((gf)_*=g_*f_*\); the adjunctions give \((gf)^{-1}=f^{-1}g^{-1}\). The identifications respect the units and counits. Formula (1.5) gives another proof of exactness using the geometric-stalk criterion of lesson 6.

## 2. A higher direct image sees a strict local base

For abelian \(F\), define \(R^qf_*F\) using an injective resolution. We first identify it without any quasi-compactness hypothesis.

**Lemma 2.1.** The sheaf \(R^qf_*F\) is the sheafification of

\[
V\longmapsto H^q((X_V)_{\mathrm{ét}},F|_{X_V}).
\tag{2.1}
\]

Hence for every geometric \(\bar y\),

\[
(R^qf_*F)_{\bar y}
=\operatorname*{colim}_{(V,\bar v)}
H^q((X_V)_{\mathrm{ét}},F|_{X_V}).
\tag{2.2}
\]

**Proof.** Restriction of an injective sheaf on \(X_{\mathrm{ét}}\) to the slice over the object \(X_V\) is sections-acyclic, by the exact slice adjunctions of lesson 3. Thus \(H^q\) of the section complex \(I^\bullet(X_V)\) computes the group on the right of (2.1). On the other hand \(f_*I^\bullet\) computes \(R^qf_*F\). Its cohomology sheaf is the sheafification of its presheaf cohomology, since associated abelian sheaves preserve kernels and cokernels. These are precisely the groups in (2.1), with their restriction maps. Taking a stalk and using the sheafification-stalk identification gives (2.2). \(\square\)

Here is the **continuity prerequisite** [Stacks, Tags 09YQ, 03Q5–03Q6]. If \(T=\varprojlim T_i\), with a directed system of quasi-compact quasi-separated schemes and affine transition maps, and \(F_i\) is a compatible system of abelian étale sheaves, then

\[
\operatorname*{colim}_i H^q((T_i)_{\mathrm{ét}},F_i)
=H^q(T_{\mathrm{ét}},\operatorname*{colim}_i p_i^{-1}F_i)
\quad(q\geq0).
\tag{2.3}
\]

In particular, for \(T_i=T_0\times_{\operatorname{Spec}A}\operatorname{Spec}B_i\), \(B=\operatorname{colim}B_i\), and \(F_i\) pulled back from \(F_0\), the last coefficient sheaf is the pullback of \(F_0\). Quasi-compactness and quasi-separatedness apply to the schemes in the system, not to the coefficient sheaf. No torsion or constructibility condition is imposed.

We also use the degree-zero sections version for sheaves of sets. Its finite-data argument is useful to spell out. On the affine étale basis, objects, morphisms and their equalities descend along a filtered ring limit by finite presentation. Finite covering families descend after increasing the index. These are the site-continuity facts in the proof of (2.3). Locally a section of a pullback sheaf has a representative from a stage, by the left Kan formula and sheafification. On a quasi-compact object select finitely many such charts. Quasi-separatedness permits finitely many quasi-compact charts on their overlaps. The finitely many matching equalities hold at a common later stage, where the charts cover; sheaf gluing gives a section there. Conversely, equality of two pulled-back sections is locally equality of their stage representatives; the same finite selection realizes it at a later stage. This proves the sections bijection for sets as well. In this argument a further finite cover is allowed to realize an equality introduced by sheafification; it too descends. The higher-cohomology assertion (2.3) is used as cited; it is not inferred from degree zero alone.

**Theorem 2.2.** Assume \(f\) is quasi-compact and quasi-separated. Let
\(R=\mathcal O_{Y,\bar y}\), the strict henselization identified in lesson 6, and let \(p:X_R=X\times_Y\operatorname{Spec}R\to X\). Then

\[
(R^qf_*F)_{\bar y}
=H^q((X_R)_{\mathrm{ét}},p^{-1}F)
\quad(q\geq0).
\tag{2.4}
\]

For sheaves of sets the degree-zero version holds as well.

**Proof.** Choose an affine open \(Y_0=\operatorname{Spec}A\) about the image of \(\bar y\), and use affine pointed étale neighbourhoods \(V=\operatorname{Spec}B_V\) over it. These suffice by lesson 6. Their ring colimit is \(R\), with the selected residue embedding. All transition maps between these affines are affine, and

\[
X_R=\varprojlim_V(X\times_Y V).
\tag{2.5}
\]

Every scheme on the right is quasi-compact and quasi-separated: it is the base change of the restricted \(f\) over a quasi-compact quasi-separated affine base. Its transition maps are affine by base change from the \(V\)'s. A filtered category may be replaced by a cofinal directed indexing set; this elementary filtered-category fact is part of the colimit convention. Apply (2.3) to (2.2). For sets apply its degree-zero finite-data argument. All comparison maps are restriction to the limit, so the resulting isomorphisms are natural and are the canonical stalk maps. \(\square\)

The scheme \(X_R\) in (2.4) is larger than the geometric fibre. A further restriction map to \(X_{\bar y}\) always exists, but an isomorphism requires another theorem or a special argument. We have not proved proper base change by writing a stalk formula.

**Lemma 2.3 (units on this limit).** For the projection \(p:X_R\to X\) of Theorem 2.2, the natural map \(p^{-1}\mathbf G_{m,X}\to\mathbf G_{m,X_R}\) is an isomorphism.

**Proof.** The projection is the limit of the étale maps \(X_V\to X\), on which inverse image is restriction and takes the units sheaf to the units sheaf. An affine étale chart \(W\to X_R\) descends to an affine étale chart \(W_V\to X_V\) by the finite-presentation limit facts used above. Degree-zero sections continuity on the schemes \(W_{V'}\) identifies the sections of \(p^{-1}\mathbf G_{m,X}\) on \(W\) with the colimit of their units. Their rings have colimit \(\Gamma(W,\mathcal O_W)\); units commute with this filtered colimit, since a unit, its inverse and the equation that their product is one are finite data. Equalities of units also hold at a later stage. Thus the comparison is bijective on every affine étale chart, a basis, proving the assertion. \(\square\)

The specific limit of étale maps matters in Lemma 2.3. Inverse image of \(\mathbf G_m\) along an arbitrary scheme morphism need not be the target's units sheaf.

The general Leray sequence from lesson 3 applies here:
\(H^a(Y_{\mathrm{ét}},R^bf_*F)\Rightarrow H^{a+b}(X_{\mathrm{ét}},F)\).
Its injective condition is especially transparent: exact \(f^{-1}\) makes \(f_*\) preserve injectives, and \(\Gamma_Yf_*=\Gamma_X\).

## 3. Why finite algebras split over a strict local ring

We give the algebra needed for finite pushforward, including henselianity of the factors. Let \((R,\mathfrak m,k)\) be strictly henselian. Finite means finite as a module; finite presentation is not assumed.

**Lemma 3.1 (coprime factor lifting).** If \(P\in R[T]\) is monic and
\(\bar P=g_0h_0\) with monic coprime factors in \(k[T]\), then \(P=gh\) for monic lifts of the same degrees.

**Proof.** Introduce variables for the coefficients of monic polynomials \(g,h\) of those degrees. The equations saying \(gh=P\) give a square system. At \((g_0,h_0)\) its derivative is the linear map

\[
(\delta g,\delta h)\longmapsto h_0\delta g+g_0\delta h,
\qquad \deg\delta g<\deg g_0,\quad
\deg\delta h<\deg h_0.
\tag{3.1}
\]

It is injective: coprimality makes \(g_0\) divide \(\delta g\) in a zero relation, hence \(\delta g=0\), and then \(\delta h=0\). Domain and target both have dimension \(\deg P\), so it is an isomorphism. Localize the coefficient scheme at this Jacobian determinant. The square Jacobian criterion makes it étale over \(R\), and the factorization gives a \(k\)-point of its closed fibre. The strictly local section theorem of lesson 6 gives an \(R\)-point lifting it, hence the desired factors. A constant factor needs no variables and is simply \(1\). Repeating the argument lifts a finite coprime factorization. \(\square\)

**Lemma 3.2.** Every idempotent in \(B/\mathfrak mB\), for a finite \(R\)-algebra \(B\), lifts uniquely to an idempotent in \(B\). Consequently

\[
B=B_1\times\cdots\times B_r
\tag{3.2}
\]

with finitely many nonzero local factors.

**Proof.** The ideal \(\mathfrak mB\) lies in the Jacobson radical: every maximal ideal of \(B\) lies over \(\mathfrak m\), by integrality. Choose \(b\in B\) representing a specified idempotent \(\bar e\). Integrality supplies a monic \(P\in R[T]\) with \(P(b)=0\). Factor \(\bar P\) into its powers of \(T\), its powers of \(T-1\), and the remaining factor coprime to both, omitting factors of degree zero. Lemma 3.1 lifts these factors.

They are pairwise comaximal in \(R[T]\). Indeed their reductions are coprime, and their resultants are therefore units; the resultant Bezout identity gives comaximality. Chinese remainders provide the idempotent in \(R[T]/P\) equal to \(1\) on the \(T-1\) factor and \(0\) on the other factors, interpreted as zero if that factor is absent. Its image in \(B\) reduces to \(\bar e\). To check this last claim, decompose \(B/\mathfrak mB\) by \(\bar e\): on one factor \(\bar b=1\), on the other \(\bar b=0\); the polynomial idempotent has those prescribed values. A missing factor can only occur when its corresponding component is zero, since \(P(\bar b)=0\).

Two idempotents \(e,e'\) with the same reduction satisfy \(e(1-e'),(1-e)e'\in\mathfrak mB\). These are idempotents in the Jacobson radical, hence zero: \(c(1-c)=0\) with \(1-c\) a unit implies \(c=0\). Thus \(e=e'\).

The finite-dimensional \(k\)-algebra \(B/\mathfrak mB\) is Artinian and has a finite decomposition into local factors. Lift its primitive idempotents successively, within the previously lifted complementary factor. This preserves orthogonality and makes their sum \(1\). The corresponding factors \(B_i\) each have exactly one maximal ideal, since maximal ideals correspond to those of the reduction and all lie over \(\mathfrak m\). They are local. Zero \(B\) gives the empty product. \(\square\)

**Theorem 3.3.** Each factor \(B_i\) in (3.2) is strictly henselian.

**Proof.** Put \(C=B_i\). Every finite \(C\)-algebra is finite over \(R\), so Lemma 3.2 decomposes it into finitely many local rings. Take a monic polynomial \(F\in C[T]\) with a specified simple root \(a\) in its residue field. The finite free algebra \(D=C[T]/F\) decomposes into local factors. Each factor has a nonzero local reduction modulo the maximal ideal of \(C\): integrality puts that ideal inside its maximal ideal, and Nakayama prevents a nonzero finite factor from having zero reduction. Thus reducing the product identifies its factors with the Artinian local factors of \(k_C[T]/\bar F\). The simple root gives exactly one factor equal to \(k_C\).

Let \(E\) be the corresponding factor of \(D\). It is a direct summand of a finite free \(C\)-module, hence finite projective, and \(E/\mathfrak m_CE=k_C\). The unit generates \(E\) by Nakayama, so \(C\to E\) is surjective. Projectivity splits it as a module map; its kernel is a finite direct summand of \(C\) with zero reduction, hence zero by Nakayama. Thus it is an isomorphism of rings. The coordinate \(T\) supplies the desired root in \(C\), with residue \(a\). This proves henselianity.

Finally \(k_C/k\) is finite algebraic. As \(k\) is separably closed, it is purely inseparable. Such an extension is again separably closed. In characteristic zero it is trivial. In characteristic \(p\), if \(\alpha\) is separable algebraic over \(k_C\), raise the coefficients of its separable polynomial to a common \(p^e\)-th power lying in \(k\). Then \(\alpha^{p^e}\) is separable algebraic over \(k\), so lies in \(k\). Consequently \(\alpha\) is both purely inseparable and separable over \(k_C\), and lies in \(k_C\). Thus \(C\) is strictly henselian. \(\square\)

The local factors are indexed by the closed points of \(\operatorname{Spec}B\) over the closed point of \(\operatorname{Spec}R\). With a fixed algebraically closed field containing \(k\), each purely inseparable residue extension has exactly one embedding there. This is the finite set of geometric lifts which will index the pushforward stalk.

## 4. Finite pushforward is a finite product on stalks

**Theorem 4.1.** Let \(f:X\to Y\) be finite and let \(\bar y:\operatorname{Spec}\Omega\to Y\) be geometric. For a sheaf of sets there is a canonical identification

\[
(f_*F)_{\bar y}=\prod_{\bar x\in X(\Omega),\ f\bar x=\bar y}F_{\bar x}.
\tag{4.1}
\]

For abelian sheaves this finite product is also the direct sum. The functor \(f_*\) is exact on abelian sheaves, \(R^qf_*F=0\) for \(q>0\), and naturally

\[
H^q(X_{\mathrm{ét}},F)=H^q(Y_{\mathrm{ét}},f_*F)
\quad(q\geq0).
\tag{4.2}
\]

**Proof.** A finite morphism is affine and quasi-compact quasi-separated. With \(R=\mathcal O_{Y,\bar y}\), write \(X_R=\operatorname{Spec}B\). Theorem 3.3 gives a finite disjoint union of strictly local spectra \(\operatorname{Spec}B_i\). The closed points of these factors correspond exactly to the \(\Omega\)-valued lifts of \(\bar y\): their residue fields are purely inseparable finite extensions of the separably closed residue field of \(R\), and have unique embeddings in \(\Omega\) extending its selected embedding. This also explains why the index is geometric lifts with this fixed \(\Omega\), rather than arbitrary choices of geometric points upstairs.

For every sheaf on a strictly local spectrum, global sections equal its closed-point stalk by lesson 6, Solution 5. That proof works for sets as well as abelian groups. Sections on a finite disjoint union are the product of the sections on its pieces. The degree-zero comparison of Theorem 2.2 and (1.5) therefore give (4.1). All maps are restrictions to the chosen closed geometric points, so the identification is canonical and natural.

In the abelian case the sections functor on each piece is exact. A finite product of exact functors is exact, so the sections functor on \(X_R\) is exact and its positive cohomology vanishes. Theorem 2.2 gives \((R^qf_*F)_{\bar y}=0\) for \(q>0\). Alternatively (4.1), the exactness of each stalk and finite-product exactness show directly that \(f_*\) is exact. Geometric stalks detect both conclusions. Since \(f_*\) also preserves injectives, applying it to an injective resolution and then taking sections proves (4.2), including its natural comparison map. \(\square\)

For sets, (4.1) also shows that \(f_*\) preserves epimorphisms: each component map of stalks is surjective and there are finitely many components. An empty fibre gives a singleton for sets and the zero group for abelian sheaves.

**Corollary 4.2 (finite base change).** In a Cartesian square

\[
\begin{array}{ccc}
X'=X\times_Y Y'&\xrightarrow{g'}&X\\
\downarrow f'&&\downarrow f\\
Y'&\xrightarrow{g}&Y
\end{array}
\]

with \(f\) finite, the canonical map

\[
g^{-1}f_*F\longrightarrow f'_*g'^{-1}F
\tag{4.3}
\]

is an isomorphism for sets and abelian sheaves. All positive higher direct images on either side vanish.

**Proof.** Construct (4.3) by adjunction from the counit: the Cartesian identification of inverse images takes \(f'^{-1}g^{-1}f_*F\) to \(g'^{-1}f^{-1}f_*F\), which maps to \(g'^{-1}F\). At \(\bar y':\operatorname{Spec}\Omega\to Y'\), the two sides of (4.3) are the products in (4.1). The lifts to \(X'\) are precisely pairs \((\bar x,\bar y')\) with \(f\bar x=g\bar y'\). Thus the indexing sets agree, and (1.5) identifies their components. The canonical map is the identity on these components because it was defined from restriction and the counit. It is an isomorphism on every stalk, hence an isomorphism of sheaves. Apply Theorem 4.1 to \(f\) and its finite base change \(f'\) for the last assertion. \(\square\)

For a finite étale cover of constant degree \(d\), pushing forward a constant coefficient sheaf \(\Lambda\) gives a locally constant sheaf with stalk \(\Lambda^d\). The permutations of the lifts supply its transition maps. There need not be a global ordering of those lifts: this sheaf need not be constant. Solution 1 makes the permutation action explicit for a Galois cover.

## 5. Closed immersions and extension by zero

Let \(i:Z\hookrightarrow X\) be a closed immersion and \(j:U=X\setminus Z\hookrightarrow X\) the complementary open immersion. A closed immersion is finite, even if its ideal is not finitely generated: a quotient algebra is generated by its unit as a module. Formula (4.1) specializes to

\[
(i_*G)_{\bar x}=\begin{cases}
G_{\bar z},&\bar x\text{ factors through }Z,\\
*,&\bar x\text{ does not, for sets},\\
0,&\bar x\text{ does not, for abelian groups}.
\end{cases}
\tag{5.1}
\]

In the first case the factorization \(\bar z\) is unique. In particular \(i_*\) is exact on abelian sheaves.

**Proposition 5.1.** The counit \(i^{-1}i_*G\to G\) is an isomorphism. Thus \(i_*\) is fully faithful. Its essential image on abelian sheaves consists of the sheaves whose stalks outside \(Z\) are zero. For sets replace “zero” by “a singleton.”

**Proof.** At \(\bar z\), (1.5) and (5.1) identify the counit with the identity on \(G_{\bar z}\). It is therefore an isomorphism. Adjunction then gives
\(\operatorname{Hom}_X(i_*G,i_*H)=\operatorname{Hom}_Z(i^{-1}i_*G,H)=\operatorname{Hom}_Z(G,H)\).
This proves full faithfulness.

For any \(F\) on \(X\), the unit \(F\to i_*i^{-1}F\) is the identity on stalks in \(Z\), and has target zero, or a singleton, outside. It is an isomorphism precisely under the stated stalk condition. Conversely (5.1) gives that condition for every \(i_*G\). This proves the essential-image assertion. \(\square\)

For abelian sheaves, saying \(\operatorname{Supp}F\subseteq Z\) means exactly this stalk condition, with the support convention of lesson 6. For sets a sheaf in the essential image is terminal outside \(Z\); requiring an empty stalk would give a different assertion.

We construct the extension-by-zero functor \(j_!\) explicitly. For an abelian sheaf \(G\) on \(U\), form the presheaf on \(X_{\mathrm{ét}}\)

\[
P_G(V)=\begin{cases}G(V),&V\to X\text{ factors through }U,\\
0,&\text{otherwise},\end{cases}
\qquad j_!G=P_G^{\#}.
\tag{5.2}
\]

Restriction from an object not contained in \(U\) is the zero map; restriction between objects contained in \(U\) is that of \(G\). For any arrow \(W\to V\), containment of \(V\) in \(U\) implies containment of \(W\), which is the compatibility needed for composition.

A natural map \(P_G\to F\) is exactly a map \(G\to j^{-1}F\): on objects outside \(U\) its component is forced to be zero, and all squares starting there commute because both routes are zero. Sheafification gives the adjunction \(j_!\dashv j^{-1}\). At a point in \(U\), neighbourhoods contained in \(U\) are cofinal; at a point outside \(U\), all terms in its stalk colimit for \(P_G\) are zero. Thus

\[
(j_!G)_{\bar x}=\begin{cases}G_{\bar x},&x\in U,\\0,&x\notin U.\end{cases}
\tag{5.3}
\]

This proves exactness of \(j_!\) and \(j^{-1}j_!G=G\). Sheafification in (5.2) matters: sections on a disconnected object may have a part supported inside \(U\) even when the whole object is not contained in it.

**Proposition 5.2.** For every abelian sheaf \(F\) on \(X\), the counit and unit give a natural exact sequence

\[
0\longrightarrow j_!j^{-1}F\longrightarrow F
\longrightarrow i_*i^{-1}F\longrightarrow0.
\tag{5.4}
\]

**Proof.** At a point of \(U\) the sequence is \(0\to F_{\bar x}\xrightarrow{1}F_{\bar x}\to0\to0\). At a point of \(Z\) it is \(0\to0\to F_{\bar x}\xrightarrow{1}F_{\bar x}\to0\). The composite is zero on all stalks, hence zero, and the stalk criterion gives every exact position. \(\square\)

## 6. Topological invariance, including nonfinite morphisms

A morphism is a **universal homeomorphism** if every base change is a homeomorphism on underlying spaces. We use the equivalent algebraic description: it is integral, universally injective and surjective ([Stacks, Tag 04DF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universal-homeomorphism)). Universally injective is also called radicial; its residue extensions are purely inseparable ([Stacks, Tag 01S4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universally-injective)). The criterion follows from the affine integral lying-over theorem and the geometric-fibre criterion for universal injectivity: an integral surjection stays surjective after base change and is closed; a universally injective such map is therefore a continuous closed bijection after every base change. Conversely the usual affine integral criterion gives the stated description of a universal homeomorphism. Only the displayed algebraic hypotheses are needed below.

Here is the extra ring argument which handles an integral morphism that is not finite.

**Lemma 6.1.** If \(R\) is strictly henselian local and \(\operatorname{Spec}B\to\operatorname{Spec}R\) is an integral universal homeomorphism, then \(B\) is strictly henselian local.

**Proof.** Write \(B\) as the filtered union of its finite \(R\)-subalgebras \(C\), containing the image of \(R\). Each is finite because finitely many integral generators generate a finite module. The inclusion \(C\subseteq B\) is integral, so \(\operatorname{Spec}B\to\operatorname{Spec}C\) is surjective by lying over; it stays surjective after every base change. Consequently \(\operatorname{Spec}C\to\operatorname{Spec}R\) is surjective and universally injective. For the latter assertion, two points upstairs after a base change can be lifted to \(\operatorname{Spec}B\) after that same base change and must coincide there, since its map to the base is injective. Their images in \(\operatorname{Spec}C\) coincide. Thus this finite intermediate morphism is also a universal homeomorphism.

Theorem 3.3 splits \(C\) into strictly local factors. Its closed fibre has just one point, so there is exactly one factor: \(C\) is strictly henselian local. For \(C\subseteq D\) the inclusion is local, since the unique maximal ideal of \(D\) contracts to the unique maximal ideal of \(C\). A filtered union of these local rings with local maps is local: an element is a unit exactly when it is a unit in a stage containing it. A nonunit cannot become a unit at a later stage under a local map, and the union of the maximal ideals is the unique maximal ideal of \(B\).

To prove henselianity, take a monic polynomial over \(B\) and a simple residue root. Its coefficients and a lift of the residue root lie in a common \(C\). Its value there lies in the maximal ideal and its derivative is a unit: both assertions follow by contraction of the maximal ideal of \(B\). Henselianity of \(C\) supplies a root with the specified residue, hence supplies one in \(B\). Finally the residue field of \(B\) is the filtered union of the residue fields of the \(C\)'s, whose transition maps are embeddings. A separable polynomial over this union has its coefficients at a stage; its nonzero discriminant remains nonzero there, and the separably closed stage supplies a root. Factoring off simple roots, or applying this to a minimal separable polynomial, shows that the union is separably closed. Thus \(B\) is strictly henselian local. \(\square\)

**Theorem 6.2 (topological invariance).** Let \(f:X\to Y\) be integral, universally injective and surjective. Then

\[
f^{-1}:\operatorname{Sh}(Y_{\mathrm{ét}})
\ \rightleftarrows\ \operatorname{Sh}(X_{\mathrm{ét}}):f_*
\tag{6.1}
\]

are inverse equivalences. They also give an exact equivalence on abelian sheaves and a natural isomorphism

\[
H^q(Y_{\mathrm{ét}},G)=H^q(X_{\mathrm{ét}},f^{-1}G)
\quad(q\geq0).
\tag{6.2}
\]

**Proof.** Integral morphisms are affine, hence quasi-compact quasi-separated. Fix \(\bar y:\operatorname{Spec}\Omega\to Y\) and its strict local ring \(R\). Its base change is \(\operatorname{Spec}B\) as in Lemma 6.1. The closed residue field of \(B\) is algebraic purely inseparable over that of \(R\), by integrality and universal injectivity, so it has exactly one compatible embedding in \(\Omega\). Equivalently there is a unique geometric lift \(\bar x\) of \(\bar y\) with this field. Surjectivity ensures existence; an algebraic purely inseparable extension embeds uniquely into an algebraically closed field with the given base embedding.

Theorem 2.2 in degree zero, Lemma 6.1, the strictly local sections theorem and (1.5) give a canonical natural equality

\[
(f_*F)_{\bar y}=F_{\bar x}.
\tag{6.3}
\]

The unit \(G\to f_*f^{-1}G\) is the identity on \(G_{\bar y}\) under (6.3) and (1.5). For every geometric \(\bar x\) of \(X\), the counit \(f^{-1}f_*F\to F\) is similarly the identity on \(F_{\bar x}\). Indeed these identifications are restriction to the unique lift and the inverse-image germ construction of Proposition 1.1; the unit and counit are precisely those restriction maps. All geometric stalks therefore make both maps isomorphisms. The stalk criterion proves the inverse equivalences, for sets and abelian sheaves, without imposing finite presentation or finiteness on \(f\).

An equivalence of abelian categories is exact and preserves injectives. The natural equality \(\Gamma_Yf_*=\Gamma_X\), followed by the unit isomorphism, identifies their injective section complexes and proves (6.2). The same local proof also gives \(R^qf_*F=0\) for \(q>0\). \(\square\)

For a closed immersion defined by a nil ideal, all primes contain that ideal, and after every base change the extended ideal is still nil: each element involves finitely many nilpotent generators, which generate a nilpotent ideal. Hence the immersion is a universal homeomorphism. The theorem applies to nilpotent thickenings and also to \(X_{\mathrm{red}}\hookrightarrow X\), even when the nilradical has no uniform nilpotence exponent.

For a scheme of characteristic \(p>0\), the absolute Frobenius is a universal homeomorphism. On an affine chart its ring map is \(a\mapsto a^p\). Every element in the target is integral over the image, being a root of \(T^p-a^p\). Every prime is its own inverse image under Frobenius, since \(a^p\) belongs to a prime exactly when \(a\) does. On residue fields the extension is purely inseparable; equivalently a geometric lift is determined by the unique \(p\)-th roots in an algebraically closed field. Thus the map is integral, surjective and universally injective. Theorem 6.2 applies even when Frobenius is not finite.

A homeomorphism of underlying spaces alone is insufficient. The finite map \(\operatorname{Spec}\mathbf C\to\operatorname{Spec}\mathbf R\) is a homeomorphism of one-point spaces. On the real étale site the representable \(h_{\operatorname{Spec}\mathbf C}\) has no global section: no \(\mathbf R\)-algebra map \(\mathbf C\to\mathbf R\) exists. After pullback to \(\mathbf C\), Proposition 1.1 identifies it with the representable of
\(\operatorname{Spec}(\mathbf C\otimes_{\mathbf R}\mathbf C)=\operatorname{Spec}(\mathbf C\times\mathbf C)\), which has two global sections. Pullback preserves the terminal object, so an equivalence would preserve maps from it. These different sets of maps show that this pullback is not an equivalence. The missing hypothesis is universal injectivity.

## 7. Galois fibres and the two branches of a node

**Example 7.1 (finite separable field extension).** Choose an algebraic closure \(\Omega\) of \(K\), its separable closure \(K^s\), and an embedding \(L\subset K^s\) of a finite separable extension of \(K\). Put \(G=\operatorname{Gal}(K^s/K)\) and \(H=\operatorname{Gal}(K^s/L)\), an open subgroup of index \([L:K]\). Every element of \(G\) extends uniquely to \(\Omega\), which is purely inseparable over \(K^s\). For an abelian sheaf \(F\) on \(\operatorname{Spec}L\), let \(M\) be its geometric stalk for this embedding in \(\Omega\), with the continuous \(H\)-action of lesson 6. The geometric stalk of \(f_*F\), with its \(G\)-action, is

\[
\operatorname{Coind}_H^G M
=\{b:G\to M\text{ continuous}:b(hg)=h b(g)\},
\qquad(a b)(g)=b(ga).
\tag{7.1}
\]

Here is a direct check from (4.1), without using the full field-topos equivalence to be proved in lesson 8. Denote the chosen embedding by \(\iota\). The lifts are the embeddings \(g^{-1}\iota\), indexed by \(H\backslash G\). Changing a residue embedding by \(a\) transports the corresponding stalk by a map \(t_a\), with \(t_at_b=t_{ab}\). This is the change-of-embedding action on pointed neighbourhoods from lesson 6. For an element \(n\) of the product of these stalks, define

\[
b_n(g)=t_g(n_{g^{-1}\iota}).
\tag{7.2}
\]

Since \(h\iota=\iota\), it satisfies \(b_n(hg)=h b_n(g)\). It is continuous: select finitely many coset representatives; on each open coset it is the orbit map of a fixed element of the continuous \(H\)-module \(M\). Conversely such a function supplies the component at \(g^{-1}\iota\) as \(t_{g^{-1}}b(g)\); its equivariance makes that component independent of the representative. These constructions are inverse. The action on the stalk product is \((a n)_\lambda=t_a(n_{a^{-1}\lambda})\); substituting in (7.2) gives \(b_{a n}(g)=b_n(ga)\), which proves (7.1) with the stated convention.

This finite-index coinduced module is also the induced module. An explicit identification uses the algebraic induced module \(\mathbf Z[G]\otimes_{\mathbf Z[H]}M\), with finite support on its \(G/H\) components. Send \(g\otimes m\) to the function supported on \(Hg^{-1}\) with value \(h m\) at \(h g^{-1}\). The relation \(gh\otimes m=g\otimes hm\) holds for these functions; left translation of the tensor agrees with right translation of the argument. Each function is the sum of these contributions on the finitely many cosets, so this map is bijective. The resulting action is continuous by (7.1), even though \(\mathbf Z[G]\) here is only an algebraic device. Thus the phrase “induced Galois module” is valid; pushforward, as a right adjoint, naturally has the coinduced description.

**Example 7.2 (a nodal cubic).** Let \(k\) be algebraically closed of characteristic different from two, and put

\[
C=\operatorname{Spec}A,\quad
A=k[x,y]/(y^2-x^2(x+1)),\qquad
\nu:\mathbf A^1_k=\operatorname{Spec}B\longrightarrow C,
\quad x=t^2-1,\quad y=t(t^2-1).
\tag{7.3}
\]

This is the normalization. Indeed \(x+1\) is not a square in \(k(x)\), by its valuation at \(x=-1\). Thus the polynomial in \(y\) in (7.3) is irreducible and \(A\) is a domain. The displayed map embeds \(A\) in \(k[t]\): its fraction field maps isomorphically to \(k(t)\), with inverse rational coordinate \(t=y/x\). Equivalently the kernel has height one, contains the displayed irreducible relation, and contains no larger prime since its image has transcendence degree one. Moreover \(B=A[t]\) and \(t^2=x+1\), so \(B\) is finite over \(A\). As \(k[t]\) is integrally closed, it is the entire integral closure: an element of \(k(t)\) integral over \(A\) is also integral over \(B\) and hence belongs to \(B\).

Away from the node \(z=(x,y)=(0,0)\), \(x\) is invertible and \(t=y/x\) gives \(A_x=B_x\). The only point with \(x=0\) is the node. Its preimages are \(t=1\) and \(t=-1\). Thus for the constant sheaf \(\Lambda=\mathbf Z/n\mathbf Z\), \(n\geq2\),

\[
(\nu_*\Lambda)_{\bar c}=\begin{cases}
\Lambda^2,&c=z,\\
\Lambda,&c\ne z.
\end{cases}
\tag{7.4}
\]

The two factors at the node are its two branches. They are stalks over the two strictly local factors of \(B\otimes_A\mathcal O_{C,\bar z}\), not two copies of the original local ring of the singular curve. This sheaf is not locally constant near the node. If it were constant on an étale neighbourhood of a lift of the node, its stalk there would have \(n^2\) elements. That neighbourhood has generizations mapping off the node: flatness gives generization lifting, or its open image contains the generic point of the irreducible curve and every open neighbourhood of its selected point still has such an image. The stalk at such a generization has \(n\) elements, a contradiction. More explicitly one may shrink to a constant open chart containing the selected point; the openness of that chart's map to \(C\) already supplies a point off the node. Formula (1.5) gives the contradiction on that chart.

We can compute the units pushforward as well. First observe the conductor description

\[
A=\{b\in k[t]:b(1)=b(-1)\}
=B\times_{k\times k}k,
\tag{7.5}
\]

where \(k\to k\times k\) is diagonal. To prove it, reduce \(b\) modulo \(t^2-1\), with remainder \(c+dt\). The two values coincide exactly when \(d=0\). Every polynomial \((t^2-1)q(t)\) lies in \(A\): its even-power terms are multiples of \(x\) times powers of \(x+1\), and its odd-power terms are multiples of \(y\) times those powers. Constants also belong to \(A\). This proves both inclusions in (7.5).

With \(i:\operatorname{Spec}k=\{z\}\hookrightarrow C\), there is an exact sequence of abelian multiplicative sheaves

\[
1\longrightarrow\mathbf G_{m,C}
\longrightarrow\nu_*\mathbf G_{m,\mathbf A^1}
\xrightarrow{\rho}i_*\mathbf G_{m,k}\longrightarrow1,
\qquad\rho(b)=b(1)/b(-1).
\tag{7.6}
\]

For an affine étale object \(V=\operatorname{Spec}E\to C\), the middle sheaf is precisely \((B\otimes_A E)^\times\), and the target is \((E\otimes_A k)^\times\). The ratio is defined by the two evaluations after base change; these formulas are compatible with restriction, hence define the map on all objects by gluing. Since \(E\) is flat over \(A\), tensoring the exact additive sequence \(0\to A\to B\to k\to0\), whose last arrow is the difference of the two evaluations, shows that equal evaluations characterize the image of \(E\) inside \(B\otimes_AE\). A unit with equal evaluations lies there together with its inverse, so the kernel of \(\rho\) is exactly \(E^\times\). This proves the first two exact positions.

Surjectivity is a stalk assertion. Away from the node the target is zero as an abelian group. At the node the middle stalk is \(R_+^\times\times R_-^\times\), for the two strictly local factors of \(B\otimes_A\mathcal O_{C,\bar z}\); Lemma 2.3 identifies the coefficient sheaf with their units. Both residue fields are \(k\). Their units surject onto \(k^\times\), so their ratio does also. This proves the final position of (7.6).

For the affine curve (7.3), (7.6) even computes \(\operatorname{Pic}(C)\). Global units of \(\mathbf A^1\) are \(k^\times\) and their ratio is \(1\). Theorem 4.1 and Hilbert 90 from lesson 5 give \(H^1(C,\nu_*\mathbf G_m)=\operatorname{Pic}(\mathbf A^1)=0\), since \(k[t]\) is a principal ideal domain. The exact sequence therefore gives \(\operatorname{Pic}(C)\simeq k^\times\). In particular exact pushforward does not erase the gluing datum between the two branches.

## 8. Exercises

1. **Easy.** Show that \(f_*\) is left exact for every morphism. For a finite étale Galois cover \(f:X\to Y\) with group \(G\), \(|G|=d\), compute \(f_*\Lambda\) and \(f^{-1}f_*\Lambda\), with their permutation action. Explain why local rank \(d\) does not imply global constancy.
2. **Medium.** Prove \(i^{-1}i_*G=G\) for a closed immersion by checking the actual counit on stalks. Deduce full faithfulness and characterize the essential image, for sets and abelian groups.
3. **Medium.** Prove that a semilocal ring has trivial Picard group. Use the strict-local stalk formula to show \(R^1f_*\mathbf G_m=0\) for finite \(f\), and compute \(\nu_*\mathbf G_m\) for the nodal cubic (7.3).
4. **Medium.** For every abelian sheaf \(F\) on \(X_{\mathrm{ét}}\), deduce naturally
\(H^q(X_{\mathrm{ét}},F)=H^q((X_{\mathrm{red}})_{\mathrm{ét}},F|_{X_{\mathrm{red}}})\).
Allow a nilradical with no uniform nilpotence bound.
5. **Hard.** Prove that a finite algebra over a strictly henselian local ring is a finite product of strictly henselian local rings. Identify the factors with the geometric lifts and deduce finite-pushforward exactness and all higher-direct-image vanishing.

## 9. Solutions

**Solution 1.** Limits of sheaves are computed objectwise, and \(f_*F(V)=F(X_V)\); hence \(f_*\) preserves all limits, in particular kernels and finite products. This is left exactness. Let a Galois cover mean a \(G\)-torsor: its deck transformations give an isomorphism

\[
\coprod_{g\in G}X\xrightarrow{\sim}X\times_YX,
\qquad(g,x)\longmapsto(x,gx).
\tag{9.1}
\]

The cover \(X\to Y\) trivializes \(f_*\Lambda\). In fact finite base change gives
\(f^{-1}f_*\Lambda=\prod_{g\in G}\Lambda_X\), by (9.1), since the pullback of the constant sheaf remains constant. Its stalk is the set or group of functions from the fibre torsor to \(\Lambda\). Deck transport permutes the arguments by the regular permutation action. On choosing a fibre point to identify that torsor with \(G\), one may write \((a b)(g)=b(ga)\), as in (7.1); changing the chosen point changes the identification, not the sheaf. The gluing across the two projections of \(X\times_YX\) uses these permutations. Thus \(f_*\Lambda\) is locally constant of rank \(d\) when \(\Lambda\) is a coefficient ring and is constant only when its permutation descent datum admits a trivialization.

For a concrete failure of constancy, take \(\operatorname{Spec}\mathbf C\to\operatorname{Spec}\mathbf R\) and \(\Lambda=\mathbf Z/n\mathbf Z\), \(n\geq2\). Its two geometric components are exchanged by complex conjugation. This action on \(\Lambda^2\) is nontrivial. A constant sheaf has trivial change-of-embedding action on its stalk, since its values arise from constant sections. Hence this locally constant pushforward is not constant.

**Solution 2.** Fix \(\bar z\) and let \(\bar x=i\bar z\). The inverse-image formula gives \((i^{-1}i_*G)_{\bar z}=(i_*G)_{\bar x}\). Since a geometric lift through a closed immersion is unique, the finite formula identifies the latter with \(G_{\bar z}\). The counit is restriction to that lift, so is the identity under these identifications. The geometric-stalk criterion proves it is an isomorphism of sheaves. Adjunction then identifies the Hom sets and proves full faithfulness. Finally \(F\to i_*i^{-1}F\) is the identity on stalks in \(Z\), with zero or singleton target outside \(Z\). Thus it is an isomorphism exactly for zero stalks outside \(Z\) in the abelian case, and singleton stalks there for sets. This proves the stated essential image as well as the counit assertion.

**Solution 3.** Let \(D\) be a semilocal ring with maximal ideals \(\mathfrak n_1,\ldots,\mathfrak n_r\), and let \(L\) be an invertible \(D\)-module. Chinese remainders for modules give a surjection \(L\to\prod_i L/\mathfrak n_iL\). One can see surjectivity by choosing scalar Chinese-remainder idempotents modulo \(\bigcap_i\mathfrak n_i\) and multiplying chosen lifts of the finitely many target components. Choose \(\ell\in L\) whose image is a nonzero generator in every one-dimensional residue space. Nakayama at each maximal ideal shows that \(\ell\) generates \(L_{\mathfrak n_i}\). The finite module \(L/D\ell\) is consequently zero at every maximal ideal, hence zero: a nonzero element of a module has an annihilator contained in some maximal ideal, where its localization is still nonzero. Thus \(D\to L\), \(1\mapsto\ell\), is surjective.

Projectivity of \(L\) splits this map. Its kernel is a finite direct summand of \(D\); after localization at each maximal ideal the map is an isomorphism between free rank-one modules, so the kernel is zero there and hence zero. Therefore \(L\simeq D\), proving \(\operatorname{Pic}(D)=0\). For the zero ring the assertion is immediate. No Noetherian hypothesis was used.

For finite \(f\), Theorem 2.2 and Lemma 2.3 identify a stalk of \(R^1f_*\mathbf G_m\) with \(H^1(\operatorname{Spec}B_{\mathrm{ét}},\mathbf G_m)\), where \(B\) is finite over a strict henselization. Theorem 3.3 makes \(B\) semilocal. Hilbert 90 identifies this \(H^1\) with \(\operatorname{Pic}(B)=0\). All stalks vanish, so \(R^1f_*\mathbf G_m=0\).

For (7.3) the direct image on an affine étale object is \((k[t]\otimes_AE)^\times\). At the node its stalk is \(R_+^\times\times R_-^\times\); off the node it is the usual units stalk of \(C\). Its relation to \(\mathbf G_{m,C}\) is the exact sequence (7.6). The difference-of-values conductor calculation (7.5), flat tensoring with \(E\), and equal evaluations of both a unit and its inverse prove its kernel. Lifting either residue unit in the two strict-local factors proves that the ratio is locally surjective. These steps determine the sheaf, not only the number of its stalk factors; they explain the branch-gluing quotient \(i_*k^\times\).

**Solution 4.** The reduction immersion is defined by the nilradical. After any base change the generated ideal is nil, because each of its elements is a finite sum involving nilpotent generators and a finitely generated nil ideal in a commutative ring is nilpotent. Thus every prime in the base change contains that ideal. The immersion is integral, universally injective and surjective, so Theorem 6.2 applies without a common exponent. Its inverse image is exactly the restriction \(F|_{X_{\mathrm{red}}}\). The exact inverse equivalence identifies global-section functors and preserves injective resolutions; taking their cohomology gives the asserted isomorphism for every \(q\), naturally in \(F\).

**Solution 5.** We spell out the dependence of the algebraic argument. A monic coprime factorization of a residue polynomial lifts by Lemma 3.1: the coefficient equations have invertible derivative \((\delta g,\delta h)\mapsto h\delta g+g\delta h\), so a closed point of their étale Jacobian locus lifts over the strictly local base. For a lift \(b\) of a residue idempotent, split its integral monic polynomial into the coprime factors supported at \(0\), at \(1\), and elsewhere. The lifted Chinese-remainder idempotent evaluates at \(b\) to the required idempotent of \(B\). Its uniqueness follows because an idempotent in \(\mathfrak mB\subseteq\operatorname{Jac}(B)\) is zero. Lifting the finitely many primitive residue idempotents inside successive complements gives the finite product of local rings in (3.2).

Every finite algebra over one such factor \(C\) is still finite over \(R\) and therefore also decomposes into local factors. For a simple residue root of a monic \(F\), the corresponding factor \(E\) of the finite free algebra \(C[T]/F\) has one-dimensional reduction. As a finite projective \(C\)-module it is generated by its unit, and its split kernel has zero reduction; Nakayama proves \(C\to E\) is an isomorphism. The coordinate gives the henselian root lift. The residue field of \(C\) is a finite purely inseparable extension of the separably closed residue field of \(R\), hence separably closed by the coefficient-power argument of Theorem 3.3. Thus all factors are strictly henselian. These arguments allow finite algebras which are not finitely presented.

Their closed points have unique compatible embeddings into the fixed algebraically closed field of the base geometric point, so they are precisely its geometric lifts. Global sections on each factor equal its exact closed stalk. Finite products of these functors are exact. Theorem 2.2 now gives (4.1), exact \(f_*\), and vanishing of every positive \(R^qf_*\). This last step uses vanishing for all abelian sheaves on a strictly local scheme, not only for units or constant coefficients.

## What this lesson does not prove

We use without proof the cohomological continuity theorem (2.3) for quasi-compact quasi-separated schemes ([Stacks, Tag 09YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-colimit)). The limit facts used in its degree-zero argument are proved in [Limits of schemes and Noetherian approximation](course:AG-MO/AG-MO-03), Theorems 3.2 and 4.1 (also [Stacks, Tag 01ZC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-proposition-characterize-locally-finite-presentation) and [Tag 01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation)); that étale and surjective morphisms descend to a finite stage is cited from [Stacks, Tag 07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale) and [Tag 07RR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-surjective). The facts from affine geometry used here are proved in earlier lessons: finite algebras are integral ([Integral extensions: lying over, going up and going down](course:AG-CA/AG-CA-05), Theorem 1.2), integral extensions satisfy lying over (the same lesson, Theorem 3.2), integral morphisms are universally closed ([Affine morphisms, relative Spec, and finite morphisms](course:AG-MO/AG-MO-05), Theorem 5.1), an Artinian ring is the finite product of its localizations at its maximal ideals ([Noetherian and Artinian rings](course:AG-CA/AG-CA-03), Theorem 4.2), and Nakayama's lemma ([Localization, local properties and support](course:AG-CA/AG-CA-02), Theorem 4.2). We cite from the Stacks project that the integral morphisms are exactly the affine universally closed morphisms ([Stacks, Tag 01WM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-integral-universally-closed)), that radicial means universally injective, with purely inseparable residue field extensions ([Stacks, Tag 01S4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universally-injective)), that the universal homeomorphisms are the integral, universally injective, surjective morphisms ([Stacks, Tag 04DF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universal-homeomorphism)), and the basic facts on finite projective modules ([Stacks, Tag 00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-projective)). A polynomial presentation with as many equations as variables, localized at its Jacobian determinant, is standard smooth with zero module of differentials ([Formally smooth, unramified and étale ring maps](course:AG-CA/AG-CA-17), Theorem 4.1), hence étale ([Étale morphisms and their local structure](course:AG-FSE/AG-FSE-04), Theorem 1.3; also [Stacks, Tag 00T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-smooth), [Tag 00T8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-example-make-standard-smooth) and [Tag 00U1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-etale)). The permanence properties of étale morphisms are proved in [Étale morphisms and their local structure](course:AG-FSE/AG-FSE-04), Section 2 and Proposition 2.1 (also [Stacks, Tag 02GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-etale), [Tag 02GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-etale) and [Tag 02GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-permanence)). Section 3 gives the complete argument for finite algebras over a strictly henselian ring.

Earlier lessons supply sheafification, stalk detection, slice adjunctions, derived functors, Leray, the strict-henselization ring and strictly local section theorem, and Hilbert 90. The equivalence with the Galois-module topos over a field will be proved in lesson 8; Example 7.1 computes the pushforward stalk and its action directly. Theorem 6.2 proves equivalence of the small étale topoi at the full stated generality. We do not assert a separate classification of all étale scheme objects over an integral universal homeomorphism from the stalk proof alone. The cohomological stalk comparison is with a strict-local base change; proper base change is still a later theorem.

## References

- **[Stacks, functoriality]** The Stacks Project Authors, *The Stacks Project*, [Tag 04I0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-functoriality), [Tags 03PV–03PY and 04I2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-direct-image), and [Tags 03PZ–03Q1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-inverse-image). These are the direct and inverse images and geometric pullback stalks of section 1.
- **[Stacks, continuity and higher images]** [Tags 03Q4–03Q6 and 09YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-colimit) for the continuity theorem; [Tags 03Q7 and 03Q9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-stalks-direct-image) for strict-local stalks; and [Tags 03QA and 03QC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-leray) for Leray. Section 2 proves the higher-image sheafification and the limit-to-stalk comparison from that theorem.
- **[Stacks, finite morphisms and closed immersions]** [Tags 03QN–03QP and 0959](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-vanishing-finite-morphism), [Tags 04E1 and 04CA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-closed-immersions), and the algebraic strict-local results [Tags 04GG–04GI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-section-henselian). Sections 3–5 provide the algebraic factor proof, canonical finite-product formula, finite base change, closed-immersion essential image and extension-by-zero exact sequence.
- **[Stacks, topological invariance]** [Tags 04DY–04DZ, 0BTY and 03SI](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-topological-invariance). Section 6 gives a strict-local proof of the topos equivalence, treating arbitrary integral morphisms by finite subalgebras, and proves its nil-thickening and Frobenius consequences.
- **[Milne, direct images]** J. S. Milne, *Lectures on Étale Cohomology*, version 2.21, 22 March 2013, [section 12, PDF pages 81–83](https://www.jmilne.org/math/CourseNotes/LEC.pdf#page=81). It treats direct images, stalks, finite vanishing, the Leray spectral sequence and nodal normalization. Example 7.2 proves finiteness for its explicit nodal cubic; it does not assume that normalization is finite for every integral scheme.
- **[Stacks, affine and étale morphisms]** [Tag 00GK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-is-integral), [Tag 00GQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-integral-overring-surjective), [Tag 01WM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-integral-universally-closed), [Tag 01S4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universally-injective), [Tag 04DF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-universal-homeomorphism), [Tag 00JB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-artinian-finite-length), [Tag 00KJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-dimension-zero-ring), [Tag 00NX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-finite-projective) and [Tag 00DV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-NAK) for the facts of affine geometry listed under *What this lesson does not prove*; [Tag 00T7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-smooth), [Tag 00T8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-example-make-standard-smooth) and [Tag 00U1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-definition-etale) for the Jacobian criterion; [Tag 02GN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-etale), [Tag 02GO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-etale), [Tag 02GW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-permanence) and [Tag 02GL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-etale-over-field) for permanence and field fibres; [Tag 01ZC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-proposition-characterize-locally-finite-presentation), [Tag 01ZM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-finite-presentation), [Tag 07RP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-etale) and [Tag 07RR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/limits.html#limits-lemma-descend-surjective) for limits of schemes of finite presentation.

The linked AI Integrated Stacks Project reader contains AI-proposed corrections and AI-written additions and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/).
