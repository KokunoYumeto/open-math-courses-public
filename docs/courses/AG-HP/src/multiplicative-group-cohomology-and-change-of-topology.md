# Multiplicative group cohomology and change of topology

*Mathematical exposition by GPT-6 Astra (OpenAI), Ultra, October 2026. Original exposition dedicated to CC0. Mathematical sources and earlier proof providers are identified below.*

For a scheme \(Y\), the sheaf \(\mathbf G_m\) assigns to a \(Y\)-scheme \(U\) the group \(\Gamma(U,\mathcal O_U)^\times\). Passing from étale covers to flat covers does not change its cohomology. The result holds in every degree, including over nonreduced and non-Noetherian schemes.

**Theorem 1.** For every scheme \(Y\) and integer \(n\geq0\), the canonical comparison is an isomorphism

\[
H^n(Y_{\mathrm{\acute et}},\mathbf G_m)
\longrightarrow H^n((\mathrm{Sch}/Y)_{\mathrm{fppf}},\mathbf G_m).
\tag{1}
\]

These maps commute with pullback along every morphism of schemes.

The coefficient on the right is the **represented** multiplicative group. It is not generally the inverse image of the small étale sheaf on the left. For example, over an algebraically closed field \(k\), the small étale sheaf corresponds to the group \(k^\times\); its inverse image gives locally constant \(k^\times\)-valued sections. The represented group on \(\operatorname{Spec}k[t,t^{-1}]\) also contains the nonconstant unit \(t\). The proof keeps these coefficients distinct.

We use the programme's universe convention for sites. Cohomology means the right derived functors of sections of abelian sheaves. Empty schemes have zero abelian cohomology. Exact earlier arguments are linked in the final section; each invocation below identifies the result needed, rather than referring to an entire course.

## Smooth lifting and finite covers

**Lemma 2.** Let \((A,\mathfrak m,k)\) be henselian local. If \(X\to\operatorname{Spec}A\) is smooth, every specified \(k\)-point of \(X_k\) lifts to an \(A\)-point. If \(k\) is separably closed, every nonempty smooth \(k\)-scheme has a \(k\)-point.

**Proof.** By the smooth-coordinate theorem [P1], an affine neighbourhood \(U\) of the specified point \(x\) admits an étale map \(U\to\mathbb A_A^d\). Lift the coordinates of its image from \(k\) to \(A\), obtaining a section \(a:\operatorname{Spec}A\to\mathbb A_A^d\). The pullback

\[
W=U\times_{\mathbb A_A^d,a}\operatorname{Spec}A
\longrightarrow\operatorname{Spec}A
\]

is affine and étale and has the specified residue point. The henselian section criterion [P2, Theorem 1.2] supplies a section through that point. Its composite with \(W\to U\to X\) is the required lift. There is no assertion of uniqueness for a smooth lift.

For the second assertion choose a nonempty étale coordinate chart \(U\to\mathbb A_k^d\). Its image is nonempty open by openness of flat locally finitely presented maps [P3]. It contains a nonempty principal open \(D(f)\). A separably closed field is infinite: every finite field has a proper finite separable extension. Induction on the number of variables, using the root bound in one variable, shows that a nonzero polynomial over an infinite field does not vanish on every tuple. Hence \(D(f)\) has a \(k\)-point. The nonempty fibre of \(U\) there is affine étale of finite type over \(k\), so its algebra is a nonzero finite product of finite separable field extensions. These extensions equal \(k\), giving a point of \(U\). The case \(d=0\) is included. \(\square\)

**Lemma 3.** Every fppf cover of the spectrum of a henselian local ring \(A\) has a refinement by a surjective finite locally free morphism \(\operatorname{Spec}B\to\operatorname{Spec}A\).

**Proof.** Let \(s\) be the closed point. The flat quasi-finite refinement theorem [P4] gives a flat, locally finitely presented, locally quasi-finite map \(T\to\operatorname{Spec}A\), with a point over \(s\), which factors through one member of the cover. The elementary étale neighbourhood theorem [P5, Theorem 4.2] gives an étale neighbourhood \((U,u)\to(\operatorname{Spec}A,s)\), with \(k(u)=k(s)\), and an open \(V\subset T\times_AU\) finite over \(U\) and meeting the fibre over \(u\).

The map \(V\to U\) remains flat and locally finitely presented. A finite flat morphism of finite presentation is finite locally free. Its image is open and contains \(u\). Restrict \(U\) to this image and then to an affine neighbourhood of \(u\). The resulting finite locally free morphism is surjective. By [P2, Theorem 1.2], the marked residue point gives a section \(\sigma:\operatorname{Spec}A\to U\). Then

\[
V\times_{U,\sigma}\operatorname{Spec}A\longrightarrow\operatorname{Spec}A
\]

is the required finite locally free surjection and still factors through the selected cover member. Both the residue-field equality and the marked point are needed for the section. \(\square\)

## The schemes of cochains and cocycles

Let \(R\) be local and \(B\) a faithfully flat finite free \(R\)-algebra. For \(n\geq0\) put

\[
D_n=B^{\otimes_R(n+1)},\qquad
C^n(A)=(A\otimes_RD_n)^\times
\]

for every \(R\)-algebra \(A\). If \(\partial_i:D_n\to D_{n+1}\) inserts \(1\) in position \(i\), define

\[
\delta_n(u)=\prod_{i=0}^{n+1}\partial_i(u)^{(-1)^i},
\qquad Z^n=\ker(\delta_n).
\tag{2}
\]

The insertions commute in the cosimplicial order, so consecutive coboundaries have value \(1\).

**Lemma 4.** For \(n\geq1\), the map

\[
\delta_{n-1}:C^{n-1}\longrightarrow Z^n
\tag{3}
\]

is a smooth surjective morphism of finitely presented affine \(R\)-schemes.

**Proof.** Choose a basis of the finite free algebra \(D_n\). For an element \(x\) let \(m_x\) denote its multiplication matrix. The element is a unit exactly when \(\det(m_x)\) is a unit: if the matrix is invertible, its inverse applied to \(1\) is an inverse of \(x\); the converse follows by multiplying by \(x^{-1}\). Thus \(C^n\) is the principal open defined by this determinant in affine space. The inverse coordinates are given by the adjugate matrix. All insertions, inverses and products in (2) are morphisms. Consequently \(Z^n\) is the affine fibre over the identity, cut out by finitely many equations. The map (3) is finitely presented: a finite presentation for its source over \(R\), together with equations specifying the images of finitely many generators of its target algebra, gives a finite presentation over that algebra.

To prove formal smoothness, let \(A\) be an \(R\)-algebra and \(J\subset A\) satisfy \(J^2=0\). Suppose

\[
z\in Z^n(A),\qquad
\bar v\in C^{n-1}(A/J),\qquad
\delta(\bar v)=\bar z.
\]

Units lift across a square-zero ideal. Indeed, lift a unit and its inverse; their product is \(1+j\), whose inverse is \(1-j\). Choose a lift \(v_0\in C^{n-1}(A)\). Write \(D_i(A)=A\otimes_RD_i\). Since this is flat over \(A\), the kernel of its reduction modulo \(J\) is

\[
J\otimes_AD_i(A)=JD_i(A).
\]

Hence \(z/\delta(v_0)=1+w\) for a unique \(w\in JD_n(A)\). In a square-zero ideal multiplication of such units is addition, and inversion is negation. The equation \(\delta(1+w)=1\) therefore says that \(w\) is an additive Amitsur cocycle with coefficient module \(J\).

The additive Amitsur complex is exact for every module under a faithfully flat map [P6, Lemma 4.1]. Apply it to \(A\to A\otimes_RB\) and \(J\). There is \(t\in JD_{n-1}(A)\) with \(d(t)=w\). Then

\[
v=v_0(1+t),\qquad
\delta(v)=\delta(v_0)(1+d(t))=z.
\tag{4}
\]

This proves the square-zero lifting property. Finite presentation and formal smoothness give smoothness [P1]. Notice that the coefficient ideal \(J\) has remained in every tensor term.

For surjectivity take a geometric point \(z:\operatorname{Spec}K\to Z^n\), where \(K\) is algebraically closed. The finite \(K\)-algebra \(B_K\) is nonzero by faithful flatness. A maximal ideal has residue field finite over \(K\), hence equal to \(K\); this gives an augmentation \(\varepsilon:B_K\to K\). Applying it to the first tensor factor defines \(h_i:C^i(K)\to C^{i-1}(K)\). The insertion identities give

\[
h_{i+1}(\delta_i(u))\,\delta_{i-1}(h_i(u))=u.
\tag{5}
\]

The first insertion gives \(u\); each other insertion pairs with the corresponding insertion after \(h_i\), with opposite exponent. This verifies (5), including its signs. Since \(\delta_n(z)=1\), equation (5) gives \(\delta_{n-1}(h_n(z))=z\). Every geometric fibre of (3) is nonempty. Thus the map is surjective. \(\square\)

## Vanishing over a strictly henselian local ring

**Proposition 5.** For every strictly henselian local ring \(R\) and every \(q>0\),

\[
H^q((\mathrm{Sch}/\operatorname{Spec}R)_{\mathrm{fppf}},\mathbf G_m)=0.
\tag{6}
\]

**Proof.** First take a finite locally free surjective cover \(\operatorname{Spec}B\to\operatorname{Spec}R\). Over a local ring its algebra is finite free. For any positive-degree cocycle \(z\in Z^n(R)\), the fibre

\[
X_z=C^{n-1}\times_{Z^n,z}\operatorname{Spec}R
\]

is smooth and surjective by Lemma 4. Its closed fibre is nonempty smooth over the separably closed residue field. Lemma 2 gives a residue point and then lifts it to an \(R\)-point. Such a point is exactly a cochain \(v\) with \(\delta(v)=z\). Thus all positive Čech groups of every such cover vanish.

To pass to derived cohomology, consider simultaneously all schemes finite over \(\operatorname{Spec}R\). A finite algebra over a henselian local ring is a finite product of henselian local rings [P2, Theorem 2.2 and Proposition 3.1]. Each factor's residue field is finite over the separably closed residue field \(k\) of \(R\), and is again separably closed. Here is the field argument. In characteristic \(p\), remove the largest common \(p\)-power from the exponents of an irreducible polynomial over \(k\); its remaining polynomial is separable, so is linear. Every algebraic element over \(k\) therefore has a \(p\)-power in \(k\). An algebraic closure of a finite extension \(L/k\) is consequently purely inseparable over \(L\), excluding nontrivial finite separable extensions of \(L\). In characteristic zero the assertion is immediate.

Every factor is therefore strictly henselian. By Lemma 3, any fppf cover of a finite \(R\)-scheme refines factor by factor to finite locally free surjections. Their finite disjoint union gives a refining family. Different members may map to different members of the original cover; a single-member factorization over a disconnected base is not required. Its positive Čech groups vanish by the preceding argument on each factor. Units on a finite disjoint union form the product of the unit groups, so finite products preserve this exactness.

Every member of these families and every iterated overlap is finite over \(R\). The simultaneous Čech-to-derived criterion [P7, Theorem 4.1] therefore applies to this class of objects and its cofinal class of covers. Its proof uses local effacement and the Čech spectral sequence, inducting simultaneously on all objects and degrees. In particular it does not assume that one chosen covering object is already derived-acyclic. Taking the object \(\operatorname{Spec}R\) gives (6). \(\square\)

## Continuity with the represented coefficient

**Proposition 6.** If \(A=\operatorname{colim}_i A_i\) is a filtered colimit of rings, then for every \(q\geq0\) the canonical map is an isomorphism

\[
\operatorname{colim}_i H^q_{\mathrm{fppf}}(\operatorname{Spec}A_i,\mathbf G_m)
\longrightarrow H^q_{\mathrm{fppf}}(\operatorname{Spec}A,\mathbf G_m).
\tag{7}
\]

**Proof.** Let \(\mathcal C_A\) have all affine schemes finitely presented over \(A\) as objects, all \(A\)-morphisms as arrows, and finite jointly surjective flat finitely presented families as covers. Its objects need not themselves be flat over \(A\). Products are given by tensor products. If two maps to \(\operatorname{Spec}C\) are compared, choose finitely many algebra generators \(c_r\) of \(C\); their equalizer is cut out by the finitely many differences of their images. Thus finite limits remain in \(\mathcal C_A\).

Any fppf cover of an object of \(\mathcal C_A\) has a finite affine refinement there: take affine opens in the covering schemes and use openness [P3] and quasi-compactness of the target to select finitely many images covering it. This assertion concerns covers of objects of \(\mathcal C_A\), not every object of the big site.

The inclusion of \(\mathcal C_A\) into the big fppf site preserves covers and finite limits. By [P8, Theorem 2.1], restriction of sheaves has an exact left adjoint, and therefore preserves injectives. Restriction is also exact: kernels are computed on sections, and an epimorphism lifts a section locally; the preceding finite refinement puts that lifting cover in \(\mathcal C_A\). Restrict an injective resolution and evaluate at the common terminal object. It follows that

\[
H^q_{\mathrm{fppf}}(\operatorname{Spec}A,F)=H^q(\mathcal C_A,F|_{\mathcal C_A})
\tag{8}
\]

canonically. No equivalence of the two whole topoi is asserted.

Suppose first the index set is directed. Base change gives the compatible sites \(\mathcal C_{A_i}\). A finitely presented algebra over \(A\) descends because it has finitely many coefficients and relations. A map descends by choosing the images of its finitely many generators, and its relation equations hold at a sufficiently late stage. Equality of two maps is tested on those same generators and also holds eventually. This proves the equivalence of the colimit category with \(\mathcal C_A\).

A finite fppf cover descends as a finite family of finitely presented algebras. Finite-presentation flatness descent [P9, the flatness lemma] makes its members flat at one later stage. Their image is then a quasi-compact open union

\[
D(g_1)\cup\cdots\cup D(g_r)\subseteq\operatorname{Spec}B_i.
\]

Its base change to \(B=B_i\otimes_{A_i}A\) is surjective, so \(1=\sum_r b_rg_r\) for finitely many \(b_r\in B\). This equation and its coefficients hold at a later stage. The descended family is therefore surjective there. Morphisms of finite covering families and their equalities descend by the generator argument. These statements verify the site-limit hypotheses in [P10], not just the underlying-category identification.

On \(\mathcal C_{A_i}\), the coefficient \(\mathbf G_m\) is represented by \(\operatorname{Spec}A_i[x,y]/(xy-1)\). Its sheaf condition follows by applying additive faithfully flat descent [P6] both to a unit and to its inverse. The canonical inverse-image functor carries this representing object to its base change: adjunction and Yoneda identify maps out of the pullback with evaluation on the base-changed object; multiplication and inversion are respected. Explicitly, on a descended algebra \(B_i\), the limit coefficient has sections

\[
\operatorname{colim}_{j\geq i}(B_i\otimes_{A_i}A_j)^\times
=(B_i\otimes_{A_i}A)^\times.
\tag{9}
\]

A unit and its inverse descend together and their product becomes \(1\) at a finite stage; equality also becomes true at a finite stage. This proves both directions of (9) and identifies the actual unit maps, rather than choosing abstract group isomorphisms.

The cohomology theorem for limits of these sites [P11] now gives (7), using (8) at each stage and (9) for its coefficient. For completeness, the transition in its compatible-injective construction is the adjunction counit

\[
f_a^{-1}f_{a\circ b,*}I
=f_a^{-1}f_{a,*}f_{b,*}I
\longrightarrow f_{b,*}I
\tag{10}
\]

for arrows \(a:j\to i\) and \(b:k\to j\) and a sheaf \(I\) on the site at \(k\). Both sides are on the site at \(j\). The inverse-image prefix is \(f_a^{-1}\), not \(f_b^{-1}\).

For a general small filtered category, the cofinal directed-set theorem [P12] supplies one directed system preserving colimits of every diagram on that category. Apply it to both the ring diagram and its cohomology groups. A skeleton alone would not give this directed-set reduction. \(\square\)

## Pointed neighbourhoods and strict localization

**Lemma 7.** Let \(R\) be any ring, \(\mathfrak p\) a prime, and \(k(\mathfrak p)\subseteq K\) a chosen separable algebraic closure. Index étale \(R\)-algebras \(S\) by compatible evaluations \(e:S\to K\), with arrows preserving the evaluations. With \(\mathfrak q=\ker e\), this category is filtered and

\[
L=\operatorname{colim}_{(S,e)}S
\cong(R_{\mathfrak p})^{sh}
\cong\operatorname{colim}_{(S,e)}S_{\mathfrak q}
\tag{11}
\]

canonically with the specified residue field.

**Proof.** Evaluation extends to \(S\otimes_Rk(\mathfrak p)\), a finite product of finite separable fields. It selects a factor with an embedding into \(K\), equivalently a prime over \(\mathfrak p\) and an embedding of its residue field. The image \(e(S)\) need not itself be a field when \(R\) is not local.

The category contains \(R\to K\). Tensor products, evaluated by multiplication in \(K\), give common targets. For parallel pointed maps \(u,v:S\to T\), put \(D=S\otimes_RS\) and

\[
W=T\otimes_D S,
\quad D\to T:\ s\otimes t\longmapsto u(s)v(t),
\quad D\to S:\ s\otimes t\longmapsto st.
\]

The last map is étale, by the maps-between-étale-algebras result specified in [P2]. Hence \(T\to W\) and \(R\to W\) are étale. The evaluations agree on \(D\), so induce \(W\to K\). The relations in \(W\) identify \(u(s)\) with \(v(s)\), giving an equalizing arrow. This proves filteredness.

The induced evaluation \(L\to K\) is onto. For \(\alpha\in K\), lift the coefficients of its monic separable minimal polynomial to \(R_t\) for one \(t\notin\mathfrak p\), obtained by clearing their finitely many denominators. If \(f\) is the lifted polynomial, then

\[
(R_t[T]/(f))_{f'}\longrightarrow K,\qquad T\longmapsto\alpha
\]

is a pointed étale algebra representing \(\alpha\). Every element of \(L\) with nonzero evaluation becomes a unit: represent it by \(s\in S\) and use the pointed principal localization \(S_s\). No element of the evaluation kernel is a unit. The kernel is therefore the unique maximal ideal, and the residue field is \(K\). Every \(t\in R\setminus\mathfrak p\) becomes a unit, giving a local map \(R_{\mathfrak p}\to L\).

Let \(P\in L[T]\) be monic with simple residue root \(\alpha\in K\). Represent its coefficients at one stage \((S,e)\) by a monic \(Q\). The pointed algebra \((S[T]/(Q))_{Q'}\), evaluated at \(\alpha\), gives a root in \(L\) with that residue. This construction does not require \(\alpha\) to lie in the previous stage's residue field. Thus \(L\) is strictly henselian.

Let \(H=(R_{\mathfrak p})^{sh}\) be the construction in [P2, Theorem 5.1]. For every \((S,e)\), the section criterion applied to the étale \(R_{\mathfrak p}\)-algebra \(S\otimes_RR_{\mathfrak p}\) gives a unique map to \(H\) with the specified residue evaluation. These maps are compatible by uniqueness and induce a local map \(f:L\to H\). Conversely the strict-henselization universal property gives a local map \(g:H\to L\) inducing the identity of \(K\). The same property gives \(fg=\mathrm{id}_H\). The maps \(gf\) and \(\mathrm{id}_L\) agree on every \(S\): after localizing the base they are two lifts of the same evaluation to the henselian ring \(L\), so the section criterion makes them equal. Hence \(gf=\mathrm{id}_L\).

Finally, every pointed arrow \(S\to T\) pulls back the marked prime of \(T\) to that of \(S\), so induces a map of their localizations. The maps \(S\to L\) invert all elements outside \(\mathfrak q\), giving compatible maps \(S_{\mathfrak q}\to L\). They induce an inverse to \(\operatorname{colim}S\to\operatorname{colim}S_{\mathfrak q}\): one composite fixes every element from \(S\), and the other fixes such elements and their inverted denominators. This proves (11). \(\square\)

## The comparison and its naturality

**Proof of Theorem 1.** Viewing an étale \(Y\)-scheme as a \(Y\)-scheme preserves covers and finite limits and defines a morphism of topoi

\[
\epsilon_Y:(\mathrm{Sch}/Y)_{\mathrm{fppf}}
\longrightarrow Y_{\mathrm{\acute et}}.
\]

Its direct image of the represented \(\mathbf G_m\) is the small étale unit sheaf, by evaluation on each étale object. By the higher-direct-image calculation [P11], \(R^q\epsilon_{Y,*}\mathbf G_m\) is the sheafification of

\[
U\longmapsto H^q_{\mathrm{fppf}}(U,\mathbf G_m).
\]

Sheafification does not change stalks [P8]. Fix a geometric point \(\bar y\) of \(Y\). Affine pointed étale neighbourhoods inside a fixed affine neighbourhood of its underlying point are cofinal: restrict to that affine base, then choose an affine open containing the marked point; do the same after fibre products to refine finite sets of arrows. Their coordinate rings have colimit \(\mathcal O_{Y,\bar y}^{sh}\) by Lemma 7. If the geometric point has values in a larger algebraically closed field, its finite étale residue extensions land in the separable algebraic closure of \(k(y)\) inside that field; this is the chosen residue field used in Lemma 7.

Proposition 6 now identifies the stalk canonically as

\[
(R^q\epsilon_{Y,*}\mathbf G_m)_{\bar y}
=H^q_{\mathrm{fppf}}(\operatorname{Spec}\mathcal O_{Y,\bar y}^{sh},\mathbf G_m).
\tag{12}
\]

For \(q>0\) it is zero by Proposition 5. To make the detection step explicit, a section whose every geometric germ is zero vanishes on an étale neighbourhood of every point. These neighbourhoods cover its domain, so the sheaf separatedness axiom makes the section zero. Thus every positive higher direct image vanishes. In degree zero the direct image is exactly \(\mathbf G_m\). The canonical map

\[
\mathbf G_m\longrightarrow R\epsilon_{Y,*}\mathbf G_m
\]

is therefore a quasi-isomorphism. Leray [P7, Theorem 8.1] identifies derived sections on the right with the fppf derived sections on \(Y\). Taking degree \(n\) proves (1), without a global affineness or quasi-compactness assumption on \(Y\).

For naturality, if \(g:X\to Y\), an étale object \(U\) pulls back to \(U\times_YX\) whether it is first viewed in the small étale or the big fppf site. These identical object maps give the square of geometric morphisms. Its coefficient maps are induced by ring pullback:

\[
g_{\mathrm{\acute et}}^{-1}\mathbf G_{m,Y}\longrightarrow\mathbf G_{m,X},
\qquad
g_{\mathrm{fppf}}^{-1}\mathbf G_{m,Y}\longrightarrow\mathbf G_{m,X}.
\]

The latter is the represented base-change identification; the former is not asserted to be an isomorphism. The derived base-change map is constructed from the square and the adjunction counit [P7, Section 9]. Its compatibility with the identity \(\epsilon_*\mathbf G_m=\mathbf G_m\) says that both composites send a unit on \(U\) to its image on \(U\times_YX\). The unit and counit identities consequently give the same derived comparison map. Taking cohomology yields the commuting square

\[
\begin{array}{ccc}
H^n_{\mathrm{\acute et}}(Y,\mathbf G_m)&\longrightarrow&H^n_{\mathrm{fppf}}(Y,\mathbf G_m)\\
\downarrow g^*&&\downarrow g^*\\
H^n_{\mathrm{\acute et}}(X,\mathbf G_m)&\longrightarrow&H^n_{\mathrm{fppf}}(X,\mathbf G_m).
\end{array}
\tag{13}
\]

This uses the canonical maps of the square, not a separate assertion that all base-change morphisms are invertible. \(\square\)

## The relative Picard comparison

**Corollary 8.** Let \(f:X\to S\) satisfy the universal condition
\(\mathcal O_T\xrightarrow{\sim}(f_T)_*\mathcal O_{X_T}\) for every \(T\to S\). The étale and fppf relative Picard sheaves agree, and their obstruction sequences agree naturally:

\[
0\longrightarrow\operatorname{Pic}(T)
\longrightarrow\operatorname{Pic}(X_T)
\longrightarrow\operatorname{Pic}_{X/S}(T)
\longrightarrow H^2_{\mathrm{\acute et}}(T,\mathbf G_m)
\longrightarrow H^2_{\mathrm{\acute et}}(X_T,\mathbf G_m).
\tag{14}
\]

**Proof.** The line-bundle/torsor correspondence and the two Leray five-term rows are proved in [P13, Theorem 3.1]. The morphism from the étale relative Picard sheaf to its fppf sheafification gives a map of these rows. The four terms other than the relative Picard term have canonical isomorphisms: the two Picard groups use the same line bundles, and the two degree-two terms use Theorem 1. Theorem 1 also gives compatibility with the pullbacks in these rows.

Here is the middle-term argument. If an étale relative class maps to zero, its boundary is zero; it is therefore the image of \(b\in\operatorname{Pic}(X_T)\). Below, \(b\) comes from \(\operatorname{Pic}(T)\), so it does above as well, and the original class is zero. Conversely lift the boundary of an fppf relative class through the isomorphism on \(H^2(T,\mathbf G_m)\). Its image in \(H^2(X_T,\mathbf G_m)\) is zero, so exactness gives an étale relative class with that boundary. The difference downstairs has zero boundary and comes from \(\operatorname{Pic}(X_T)\); that same line bundle corrects the lift. Thus the relative map is bijective for every \(T\), naturally. This proves the sheaf comparison and (14). The argument uses Theorem 1 first; it is not a proof of Theorem 1 from a Picard comparison. \(\square\)

## Sources and exact earlier proofs

The comparison is Grothendieck's theorem. The proof uses his strict-local method, specialized to the represented multiplicative group: [*Le groupe de Brauer III*, Appendix 11, printed pages 171–183, especially Theorem 11.7](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/DixExp.pdf#page=145). The following links identify the exact earlier programme and fork arguments used here.

- **[P1] Smooth coordinates and the lifting criterion.** *Smooth morphisms*, definition, Theorem 4.1 and Theorem 5.2.
- **[P2] Henselian sections and strict henselization.** *Henselian local rings and henselization*, Theorem 1.2, Theorem 2.2, Proposition 3.1 and Theorem 5.1. The opening prerequisite paragraph identifies the earlier étale-algebra results used in the diagonal and root-algebra constructions.
- **[P3] Flatness and openness.** *Flat morphisms*, Proposition 2.1, Lemma 3.1 and Theorem 3.2.
- **[P4] Flat quasi-finite refinements.** [AI Integrated Stacks, `more-morphisms.tex`, the two flat quasi-finite domination lemmas](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/more-morphisms.tex#L6588), following the explicit Cohen–Macaulay slicing argument at lines 6317–6586.
- **[P5] The finite neighbourhood.** *Étale neighbourhoods, henselization and quasi-finite morphisms*, Lemma 4.1 and Theorem 4.2.
- **[P6] Additive faithfully flat exactness.** *Topologies on schemes*, Lemma 4.1.
- **[P7] Derived cohomology on sites.** *Cohomology on sites*, Proposition 2.1, Theorem 3.2, Theorem 4.1, Theorem 8.1 and Section 9.
- **[P8] Site morphisms and stalks.** *Topoi, morphisms and points*, Theorem 2.1 and the stalk/sheafification argument.
- **[P9] Eventual flatness.** [AI Integrated Stacks, `algebra.tex`, finite-presentation flatness descent](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex#L48990). Its local model, eventual Tor vanishing and open-flat-locus arguments are at lines 33804–33859, 34105–34145 and 34801–34905 respectively.
- **[P10] Limits of sites and coefficients.** [AI Integrated Stacks, `sites.tex`, site construction, inverse images and compatible coefficients](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/sites.tex#L3767), through line 3994.
- **[P11] Higher direct images and continuity.** [AI Integrated Stacks, `sites-cohomology.tex`, higher direct images](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/sites-cohomology.tex#L746) and [the compatible-system and cohomology-limit proofs](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/sites-cohomology.tex#L2854). Formula (10) specifies the counit used in that construction.
- **[P12] A cofinal directed set.** [AI Integrated Stacks, `categories.tex`, the directed-category-system lemma](https://github.com/KokunoYumeto/unofficial-ai-integrated-stacks-project/blob/565b10e987aba5969b21145a0833f42d69f96790/categories.tex#L2711), through line 2848.
- **[P13] Picard sheaves and their Leray rows.** *The Picard functor and the Picard scheme of a curve*, Section 3. Only its line-bundle interpretation and construction of the two rows enter Corollary 8; its use of the topology comparison is supplied by Theorem 1 here, not imported as a premise.
