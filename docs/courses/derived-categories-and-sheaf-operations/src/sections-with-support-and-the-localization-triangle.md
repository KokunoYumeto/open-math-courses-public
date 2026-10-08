# Sections with support and the localization triangle

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original text: public domain (CC0). Authorship and sources are listed in the [course notice](../LICENCE.md).*

A section can vanish away from a closed subset while carrying information on that subset. Derived sections with support also detect classes which cannot be represented by a degree-zero section. Localization compares this information with what remains on the open complement. The point of the triangle is to include the boundary map: it measures the obstruction to extending a class across the missing subset.

The prerequisites are [Sheaves of modules on a ringed space](sheaves-of-modules-on-a-ringed-space.md), Theorems 2.1 and 4.4; [Injective modules and bounded-below derived functors](injective-modules-and-bounded-below-derived-functors.md), Lemma 1.1, Proposition 1.3 and Theorem 4.1(4), for injective flasqueness and acyclic resolutions; [K-injective resolutions in Grothendieck categories](k-injective-resolutions-in-grothendieck-categories.md), Theorems 4.1 and 5.1; and [Derived pullback and pushforward](derived-pullback-and-pushforward.md), Proposition 3.2 and Theorem 4.1. The cone construction and exact-sequence triangle are Theorem 3.1 and Proposition 5.2 of the common reading. For cup products we use the tensor lesson's Theorem 2.2 and the internal-Hom lesson's Theorem 3.1.

Sections 1–3 work for any sheaf of unital rings, including noncommutative rings, and unbounded complexes of left modules. Section 5's tensor and cup products assume commutativity. For a closed inclusion \(i:Z\hookrightarrow X\), use the unchanged coefficient sheaf \(\mathcal O_Z=i^{-1}\mathcal O_X\); this is distinct from taking a quotient coefficient ring on a closed geometric subspace. Put \(j:U=X\setminus Z\hookrightarrow X\).

The construction follows the Stacks project authors’ *Cohomology of Sheaves*, “Cohomology with support in a closed subset, II”, Tags 0G6Z–0G79, and *Sheaves of Modules*, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). We develop the support adjunction, localization triangle and canonical product and pullback maps. The Euclidean example includes the singular-cochain comparison it uses. Source attribution appears in the [course notice](../LICENCE.md).
## 1. Closed supports and their adjunction

The support of a section \(s\in F(V)\) is the set of points where its germ is nonzero. It is closed in \(V\): a zero germ means the section vanishes on a neighborhood. Define the ambient support subsheaf by

\[
\mathcal S_Z^0F=\ker(F\longrightarrow j_*F|_U).
\tag{1.1}
\]

Its sections are exactly those supported in \(Z\cap V\). It is a module subsheaf, since scalar multiplication cannot create a nonzero germ where the section vanished. Kernels show that this additive functor is left exact. Its stalks vanish off \(Z\).

A sheaf with zero stalks off a closed set is canonically the direct image of its restriction to that set. Indeed \(i_*G\) has stalk \(G_z\) at \(z\in Z\) and zero off \(Z\): neighborhoods intersected with \(Z\) are cofinal neighborhoods in \(Z\), and a point outside \(Z\) has a neighborhood disjoint from it. Thus the unit \(F\to i_*i^{-1}F\) is an isomorphism for such \(F\). The same stalk description proves that \(i_*\) is exact, \(i^{-1}i_*\) is the identity, and \(i_*\) is fully faithful. Set

\[
\begin{gathered}
\mathcal H_ZF=i^{-1}\mathcal S_Z^0F,\\
i_*\mathcal H_ZF=\mathcal S_Z^0F.
\end{gathered}
\tag{1.2}
\]

**Proposition 1.1.** The functor \(\mathcal H_Z\) is right adjoint to the exact functor \(i_*\). It preserves injective objects and K-injective complexes. There is a derived adjunction
\(i_*\dashv R\mathcal H_Z\), and \(R\mathcal H_Z(i_*N)=N\).

**Proof.** A map \(i_*G\to F\) has image with zero stalks off \(Z\), so it factors uniquely through (1.1). Full faithfulness of \(i_*\) then identifies it with a unique map \(G\to\mathcal H_ZF\). Conversely such a map pushes forward and includes into \(F\); these operations are inverse and natural. Since \(i_*\) is exact, Hom into \(\mathcal H_ZI\) is exact if Hom into \(I\) is exact, proving injectivity preservation. If \(A\) is an acyclic complex on \(Z\), chain adjunction identifies maps and homotopies
\(A\to\mathcal H_ZI\) with those \(i_*A\to I\). The latter source is acyclic, so these maps are null-homotopic for K-injective \(I\).

Choose K-injective models in this same adjunction. The map test into K-injectives gives the derived adjunction. Also \(i_*\) preserves K-injectives, because its left adjoint \(i^{-1}\) is exact; the identical acyclic-source argument proves this. Resolving \(N\) by \(J\) therefore computes \(R\mathcal H_Z(i_*N)\) by \(\mathcal H_Z(i_*J)=J\), proving the final assertion. All arguments use left module maps only. \(\square\)

Write \(D_Z(\mathcal O_X)\) for objects whose cohomology sheaves vanish off \(Z\). Exact restriction shows this condition is equivalent to \(K|_U=0\); cone long exact sequences show it defines a triangulated subcategory. The stalk argument for the unit applies to every cohomology sheaf, so
\(i_*:D(\mathcal O_Z)\to D_Z(\mathcal O_X)\) is an equivalence with inverse \(i^{-1}\). Proposition 1.1 then says

\[
\mathcal S_ZK:=i_*R\mathcal H_ZK
\tag{1.3}
\]

is right adjoint to the inclusion of \(D_Z\). Its counit \(\mathcal S_ZK\to K\) is universal among maps from objects supported on \(Z\). In particular it is an isomorphism if \(K\in D_Z\).

Define \(\Gamma_Z(X,F)=\Gamma(X,\mathcal S_Z^0F)\) and derive it with K-injectives. Because \(\mathcal H_ZI\) is K-injective, (1.2) gives the full local-to-global identity

\[
R\Gamma_Z(X,K)=R\Gamma(Z,R\mathcal H_ZK).
\tag{1.4}
\]

On the right we restrict the scalar action from \(\Gamma(Z,\mathcal O_Z)\) through the map from \(\Gamma(X,\mathcal O_X)\). This also proves that taking derived sections of (1.3) gives the left side. These identities hold for all unbounded complexes.

### Derived costalks and changes of closed coefficients

The costalk adjunction in Proposition 5.3 of the first lesson extends to all unbounded complexes:
\[
x_*:D(\mathcal O_x)\rightleftarrows D(\mathcal O_X):Rc_x,
\qquad Rc_xF=c_xI
\]
for a K-injective resolution \(F\to I\). Indeed \(x_*\) is exact, and the complex adjunction identifies \(\operatorname{Hom}^\bullet(A,c_xI)\) with \(\operatorname{Hom}^\bullet(x_*A,I)\). Thus \(c_xI\) is K-injective and the Hom comparison proves the derived adjunction. For a closed point, uniqueness of right adjoints and Proposition 1.1 identify \(Rc_x\) with \(R\mathcal H_{\{x\}}\). The Euclidean calculation in Section 4 consequently says that, for a field \(k\) and \(n>0\),
\[
(k_{\mathbb R^n})_0=k,
\qquad Rc_0(k_{\mathbb R^n})=k[-n].
\]
The ordinary costalk is zero here; the degree-\(n\) derived costalk detects the class surrounding the missing point.

**Proposition 1.2 (closed embeddings with changed coefficients).** Let \(i:(Z,\mathcal B)\to(X,\mathcal O)\) be a morphism of commutative ringed spaces whose underlying map is a closed embedding. Its exact direct image has a left-exact right adjoint
\[
i_0^!F=i^{-1}\mathcal Hom_{\mathcal O}(i_*\mathcal B,F),
\]
where \(\mathcal B\) acts by precomposition with multiplication on \(i_*\mathcal B\). Its derived functor is right adjoint to \(i_*\) on unbounded derived categories. If \(\mathcal B=i^{-1}\mathcal O\), this is \(R\mathcal H_Z\). In general it also includes derived coinduction of coefficients.

**Proof.** The sheaf \(H=\mathcal Hom_{\mathcal O}(i_*\mathcal B,F)\) vanishes off \(Z\), since its source does, so the supported-sheaf argument above gives \(i_*i^{-1}H=H\). A sheaf map \(v:i_*M\to F\) determines a \(\mathcal B\)-linear map \(M\to i_0^!F\): a local element \(m\) defines the map \(b\mapsto v(bm)\). Conversely a map \(M\to i_0^!F\) is pushed forward to \(i_*M\to H\) and followed by evaluation at \(1\) to \(F\). Evaluation is compatible with restrictions; on an open disjoint from \(Z\), the source and \(H\) are both zero. The two constructions are inverse because \(\mathcal B\)-linearity gives \(a(bm)(1)=a(m)(b)\). This proves the adjunction and left exactness. Exactness of \(i_*\) follows from its closed-embedding stalk formula, irrespective of the coefficient map. The complex adjunction now shows that \(i_0^!\) preserves K-injectives, exactly as for the costalk. Apply the K-injective Hom comparison to obtain \(i_*\dashv Ri_0^!\). With unchanged coefficients both functors are right adjoints of the same \(i_*\), so they agree naturally. \(\square\)

This construction is discussed by Daniel Murfet in [*Modules over a Ringed Space*, §1.13, Propositions 96–97](https://therisingsea.org/notes/RingedSpaceModules.pdf); the proof here includes its unbounded derived extension. Even at a one-point space, a coefficient map \(R\to S\) has right adjoint \(\operatorname{Hom}_R(S,-)\), derived to \(\operatorname{RHom}_R(S,-)\). For \(\mathbb Z\to\mathbb F_p\), the free resolution \(\mathbb Z\xrightarrow{p}\mathbb Z\) in degrees \(-1,0\) gives
\[
\operatorname{Hom}_{\mathbb Z}(\mathbb F_p,\mathbb Z)=0,
\qquad \operatorname{RHom}_{\mathbb Z}(\mathbb F_p,\mathbb Z)
\simeq\mathbb F_p[-1].
\]
Support in the whole one-point space would instead return \(\mathbb Z\). Thus a closed geometric subspace with quotient coefficients requires the coefficient adjoint as well as support.

## 2. Localization and its connecting sign

**Theorem 2.1.** There are triangles natural in \(K\):

\[
\begin{gathered}
\mathcal S_ZK\longrightarrow K\longrightarrow Rj_*(K|_U)\\
\longrightarrow\mathcal S_ZK[1],
\end{gathered}
\tag{2.1}
\]

and

\[
\begin{gathered}
R\Gamma_Z(X,K)\longrightarrow R\Gamma(X,K)\\
\longrightarrow R\Gamma(U,K|_U)\\
\longrightarrow R\Gamma_Z(X,K)[1].
\end{gathered}
\tag{2.2}
\]

**Proof.** Choose \(K\to I\) K-injective with injective terms. Every term is flasque, and its restriction to \(U\) is K-injective. On every open \(V\), flasqueness makes \(I^n(V)\to I^n(V\cap U)\) surjective. The kernel is precisely supported sections. Thus there are termwise short exact sequences

\[
\begin{gathered}
0\to i_*\mathcal H_ZI\to I\\
\to j_*(I|_U)\to0,\\[4pt]
0\to\Gamma_Z(X,I)\to\Gamma(X,I)\\
\to\Gamma(U,I)\to0.
\end{gathered}
\tag{2.3}
\]

Each term is the indicated derived-functor model by Proposition 1.1 and open restriction. The common reading's exact-sequence triangle proves (2.1) and (2.2). A derived map is a unique homotopy class between the K-injective models. Applying the functors gives a map of exact sequences; the cone and quotient construction is natural for that map. Homotopic maps give homotopic maps on each term and identical maps of derived triangles. Resolution comparisons are homotopy equivalences, proving natural independence of the models. \(\square\)

The sign calculation is as follows. For \(0\to A\xrightarrow{a}B\xrightarrow{b}C\to0\), the cone has differential \(d(y,x)=(dy+a(x),-dx)\), projection \(p(y,x)=x\), and quasi-isomorphism \(q(y,x)=b(y)\) to \(C\). A cycle \(z\in C^n\) lifts to \(y\in B^n\); write \(dy=a(x)\). Injectivity of \(a\) gives \(dx=0\). The cone cycle \((y,-x)\) maps to \(z\), so

\[
H^n(p)H^n(q)^{-1}[z]=-[x].
\tag{2.4}
\]

Our triangle's last map is \(-p q^{-1}\), hence induces the positive lift boundary \([z]\mapsto[x]\). A convention using the positive cone projection has the opposite boundary. Negating two arrows gives an isomorphic triangle: multiply one of its three objects by minus one. Thus one must track the third-arrow convention when transporting a formula from another source, rather than change one boundary informally.

**Proposition 2.2.** If an open \(V\) is disjoint from \(Z\), then
\(R\mathcal H_Z(Rv_*N)=0\) for \(v:V\hookrightarrow X\). Module and underlying-abelian supported cohomology agree canonically, both globally and as support sheaves.

**Proof.** A K-injective \(J\) on \(V\) has K-injective \(v_*J\), since restriction is exact. Its sections over \(W\) and \(W\setminus Z\) are both \(J(W\cap V)\), so its support kernel is zero. This proves the first assertion. For coefficient comparison, resolve a module complex by \(I\), and its underlying abelian complex further by an abelian K-injective \(J\). Their support kernels and restrictions give a map of the exact-sequence triangles (2.3), with injective terms used for both resolutions. The middle and open-complement maps on derived global sections are isomorphisms by Theorem 4.1 of the preceding lesson. The long exact sequences, or the Five Lemma on consecutive five terms, make the support map an isomorphism. Apply this argument on every open and sheafify to obtain the local support comparison; restriction of both coefficient models to opens is K-injective. Finally restrict the ambient comparison to \(Z\) to get \(R\mathcal H_Z\). This supplies the source's omitted local verification. \(\square\)

## 3. Locally closed pairs

The construction also applies to a locally closed \(W\). Choose an open \(V\) in which \(W\) is closed, and define the ambient support functor by direct image from \(V\) of its closed-support subsheaf. It is independent of this choice. For another such open \(V'\subset V\), a supported section on \(T\cap V'\) glues with zero on \(T\cap(V\setminus W)\): their overlap is outside its support, and these two opens cover \(T\cap V\). This is the inverse to restriction of supported sections. Compare arbitrary choices through their intersection. These inverse maps commute with restrictions, differentials and scalars. For an open \(W\), this functor is \(w_*F|_W\), not a subsheaf of sections of \(F\) extended by zero.

**Proposition 3.1.** If \(W\) is locally closed and \(W'\) is closed in \(W\), there is a natural triangle

\[
\begin{gathered}
R\Gamma_{W'}^{\mathrm{sh}}K\longrightarrow R\Gamma_W^{\mathrm{sh}}K\\
\longrightarrow R\Gamma_{W\setminus W'}^{\mathrm{sh}}K
\longrightarrow R\Gamma_{W'}^{\mathrm{sh}}K[1].
\end{gathered}
\tag{3.1}
\]

Here the superscript distinguishes these ambient sheaf functors from global sections.

**Proof.** Choose \(V\) with \(W\) closed in \(V\); then \(W'\) is also closed in \(V\), and \(W\setminus W'\) is closed in \(V\setminus W'\). For a flasque \(F\), a supported section on \((T\cap V)\setminus W'\) extends to \(T\cap V\). Outside \(W\) the extension is still zero, since that open subset lies inside its original domain. The extension therefore has support in \(W\). Its kernel under restriction consists exactly of sections supported in \(W'\). This proves a short exact sequence of the three support sheaves on every open \(T\), even though direct image from \(V\) need not generally be exact. Apply it termwise to a K-injective resolution with injective, hence flasque, terms. The cone argument of Theorem 2.1 proves the triangle and its functoriality, with the same positive lift boundary. \(\square\)

## 4. Integer coefficients near a Euclidean point

We prove the comparison needed for this example, rather than assume homotopy invariance for arbitrary sheaf cohomology. Let \(V\) be any open subset of \(\mathbb R^n\) and \(A\) any abelian group. Let \(S_q(V)\) be the free abelian group on continuous singular simplices \(\Delta^q\to V\), with boundary the alternating sum of faces. Its cochains are \(C^q(V;A)=\operatorname{Hom}_{\mathbb Z}(S_q(V),A)\), with differential \(c\mapsto c\partial\). Let \(\mathcal C^q\) be the sheafification of this cochain presheaf.

**Lemma 4.1 (cochain comparison).** The augmented complex \(A_V\to\mathcal C^\bullet\) is a flasque resolution, and

\[
H^q(V,A_V)=H^q(C^\bullet(V;A)).
\tag{4.1}
\]

The comparison is natural under restrictions to smaller opens.

**Proof.** We supply the three required steps. First, a cover of an open Euclidean set has a locally finite open refinement \((V_a)\) whose closures lie in members of the original cover. Here is an explicit compactness argument. Exhaust the open set by compact sets
\(K_m=\{x:|x|\leq m,\ \operatorname{dist}(x,\mathbb R^n\setminus V)\geq1/m\}\) for \(m\geq1\); omit the distance condition when the complement is empty. They satisfy \(K_m\subset\operatorname{int}K_{m+1}\) and exhaust \(V\). Cover each compact layer \(K_m\setminus\operatorname{int}K_{m-1}\) by finitely many balls with closures in cover members and in \(\operatorname{int}K_{m+1}\setminus K_{m-2}\). Set \(K_m=\varnothing\) for every \(m\leq0\). The balls cover \(V\); every point has a neighborhood in some \(K_m\), which meets only finitely many subsequent layers, so they are locally finite.

A section of \(\mathcal C^q\) is represented by cochains \(c_a\) on cover members. Using this refinement, assign to each singular simplex contained in some \(V_a\) the value given by one such \(c_a\); assign zero if it is contained in none. This is a global cochain representing the section. To verify the assertion, fix a point \(x\). Only finitely many refinement members meet a sufficiently small neighborhood. Remove those whose closures do not contain \(x\). For the remaining finite list, their representing cochains are defined near \(x\), and their germs agree. Shrink the neighborhood so all these cochains agree on every simplex in it, and so it is contained in one refinement member containing \(x\). The global assignment then agrees with that representative there, irrespective of the choices for simplices. This proves surjectivity of \(C^q(V;A)\to\Gamma(V,\mathcal C^q)\). The same proof works on every smaller open. Extend a representing cochain by zero on simplices not contained in that smaller open; this proves flasqueness of \(\mathcal C^q\).

Second, on a convex ball straight-line contraction proves that singular cohomology is \(A\) in degree zero and zero in positive degrees. The chain verification is the prism identity: a homotopy \(H\) from \(f\) to \(g\) assigns to a \(q\)-simplex the alternating sum, with signs \((-1)^i\), of the \(q+1\) simplices with vertices
\((v_0,0),\ldots,(v_i,0),(v_i,1),\ldots,(v_q,1)\) in \(\Delta^q\times[0,1]\), followed by \(H\). Interior faces cancel in pairs, the two horizontal faces give \(g-f\), and the other faces give the negative prism of the boundary. Thus \(\partial P+P\partial=g_*-f_*\). A constant map factors through the point's chain complex; its augmented homology contracts (insert the unique vertex), and dually its cohomology is as stated. Taking the exact filtered colimit over convex-ball neighborhoods proves that \(A_V\to\mathcal C^\bullet\) is exact on stalks.

Third, the kernel of global cochains mapping to sheaf sections is the complex \(N^\bullet\) of cochains locally zero: each point has a neighborhood on all of whose singular simplices the cochain vanishes. We prove that this kernel is acyclic. For an open cover \(\mathcal U\), let \(S_*^{\mathcal U}\) be the subcomplex generated by simplices contained in one cover member, and let \(N_{\mathcal U}^\bullet\) be its annihilator. The small-chain inclusion has a retraction \(r\) and homotopy \(h\) satisfying

\[
\begin{gathered}
1-jr=\partial h+h\partial,\\
rj=1,\qquad hj=0.
\end{gathered}
\tag{4.2}
\]

Here is the full construction. Barycentric subdivision \(s\) replaces a simplex by its oriented barycentric triangulation. Internal faces cancel, and boundary faces are subdivided faces, so it is a chain map. There is a homotopy \(T\) with \(s-1=\partial T+T\partial\), supported inside each simplex image. To construct it without another theorem, work first in the standard simplex. In dimension zero take \(T=0\). In dimension \(q\), subtract the already constructed homotopies on its faces from \(s\iota_q-\iota_q\). The result is a cycle by the lower-dimensional identity. Cone that cycle to the barycenter inside the convex simplex, then push it forward by the singular simplex. The cone boundary formula \(\partial(b*c)=c-b*\partial c\) proves the identity. Write \(T_m\) for the sum of iterated homotopies, so \(s^m-1=\partial T_m+T_m\partial\); it has the same support control.

Induct on simplex dimension to construct (4.2). Once \(r,h\) are constructed on faces of \(\sigma\), put \(z=\sigma-h\partial\sigma\). The induction identity gives \(\partial z=jr\partial\sigma\). Choose \(m\) so that every simplex in \(s^m z\) is small, and define

\[
\begin{aligned}
jr\sigma&=s^mz-T_mjr\partial\sigma,\\
h\sigma&=-T_mz.
\end{aligned}
\tag{4.3}
\]

The correction is small: \(r\partial\sigma\) is small, and \(T_m\) keeps each simplex inside its image. The boundary of the first line is \(jr\partial\sigma\); subtracting it from \(z\) gives \(-\partial T_mz\), proving the homotopy identity. For a small \(\sigma\), its faces have \(h=0\); choose \(m=0\), obtaining \(r\sigma=\sigma\) and \(h\sigma=0\). The required \(m\) always exists: barycentric subdivision reduces mesh in dimension \(q>0\) by at most \(q/(q+1)\). Indeed two vertices of a subdivided simplex are barycenters of nested faces, and their distance is bounded by that fraction of the original diameter. Uniform continuity on the compact standard simplex and a finite subcover of its inverse-image cover then make repeated subdivisions small. The finitely many simplices in \(z\) can use a common \(m\).

Dualizing (4.2) contracts \(N_{\mathcal U}^\bullet\): \(cjr=0\), and \(ch\) still vanishes on small chains because \(hj=0\). Every locally zero cochain belongs to some \(N_{\mathcal U}\), and common refinement orders these complexes as a filtered union. Exact filtered colimits make \(N^\bullet\) acyclic. Our first step identifies the section complex of \(\mathcal C^\bullet\) with \(C^\bullet/N^\bullet\); the quotient is therefore quasi-isomorphic to singular cochains. Finally flasque acyclicity and the bounded-below acyclic-resolution theorem from the bounded-derived lesson compute sheaf cohomology by this section complex. All maps used in the quotient comparison are restriction maps, giving its naturality. \(\square\)

**Proposition 4.2.** For \(n\geq0\),

\[
R\Gamma_{\{0\}}(\mathbb R^n,\mathbb Z)
\cong\mathbb Z[-n].
\tag{4.4}
\]

**Proof.** The comparison proves \(H^q(\mathbb R^n,\mathbb Z)=\mathbb Z\) for \(q=0\) and zero otherwise, by straight-line contraction. For \(n>0\), the punctured space deformation retracts onto \(S^{n-1}\) by radial rescaling; the prism identity proves invariance of singular cohomology under this homotopy.

We recall and prove the sphere calculation needed here. For a cover by two opens, its small-chain complex is the sum of the two singular chain subcomplexes; their intersection is the chain complex of their intersection. Cochains therefore have the short exact sequence with middle term \(C^\bullet(U;\mathbb Z)\oplus C^\bullet(V;\mathbb Z)\), last term \(C^\bullet(U\cap V;\mathbb Z)\), and map the difference of restrictions. Surjectivity follows by extending any cochain on the intersection by zero to either open. The small-chain equivalence just proved gives the usual long exact Mayer–Vietoris sequence, with no sheaf comparison required on the sphere itself. Cover \(S^m\) by complements of its two poles. Each is homeomorphic to \(\mathbb R^m\), and their intersection retracts to \(S^{m-1}\). Starting with \(S^0\), whose two points have \(H^0=\mathbb Z^2\), the sequence proves inductively that the reduced cohomology of \(S^m\) is \(\mathbb Z\) in degree \(m\) and zero elsewhere.

For \(n=1\), the restriction from the line to its two complementary rays is the diagonal \(\mathbb Z\to\mathbb Z^2\). Its cokernel is \(\mathbb Z\). For \(n>1\) the degree-zero restriction is an isomorphism, and the sole reduced punctured-space class has degree \(n-1\). The long exact sequence of (2.2) puts the sole supported class in degree \(n\). For \(n=0\), the support is the entire one-point space and the result is immediate. A complex with just this cohomology is isomorphic to that cohomology module in its degree: the good-truncation inclusion and quotient give the requisite quasi-isomorphisms, as in the common reading's Proposition 5.2. This proves (4.4). \(\square\)

The same computation on balls centered at zero gives \(\mathcal S_{\{0\}}\mathbb Z=\mathbb Z_{\{0\}}[-n]\). The transition isomorphisms follow from the natural comparison and radial rescaling of punctured balls. This is supported cohomology, rather than ordinary sections of the constant sheaf supported at the point; those ordinary sections are zero when \(n>0\).

## 5. Cup products and support pullback

Assume commutative coefficients in this section. Tensoring an object supported on \(Z\) with any derived object keeps that support: a K-flat model makes its restriction to the complement acyclic. The universal counit in (1.3) therefore gives a unique factorization of
\(K\otimes^{\mathbf L}\mathcal S_ZM\to K\otimes^{\mathbf L}M\) through \(\mathcal S_Z(K\otimes^{\mathbf L}M)\). On closed-set coefficients it is the canonical map

\[
\begin{gathered}
i^{-1}K\otimes^{\mathbf L}R\mathcal H_ZM\\
\longrightarrow R\mathcal H_Z(K\otimes^{\mathbf L}M).
\end{gathered}
\tag{5.1}
\]

Indeed \(K\otimes^{\mathbf L}i_*N=i_*(i^{-1}K\otimes^{\mathbf L}N)\): take a K-flat model for \(K\), and check the ordinary tensor comparison on stalks, identical over \(\mathcal O_z\) on \(Z\) and zero off it. This proves the identity without a projection-formula assumption. The universal factorization proves naturality and coherence under successive tensor products, because the composites have the same image under the counit.

The internal-Hom lesson identifies cohomology classes with maps from \(\mathcal O\) to shifted objects. Tensoring such maps defines cup products. Apply the factorization above to get

\[
\begin{gathered}
H^p(X,K)\times H_Z^q(X,M)\\
\longrightarrow H_Z^{p+q}(X,K\otimes^{\mathbf L}M).
\end{gathered}
\tag{5.2}
\]

Forgetting supports commutes with cup product, since composing the factorization with its counit is precisely the ordinary tensor map. This proves the omitted compatibility in Tag 0G77. On homogeneous cycles the product is their tensor, whose differential is \(da\otimes b+(-1)^pa\otimes db\); changing either cycle by a boundary changes it by a boundary. The coherent shift identification gives exactly these signs.

For a morphism \(f:X'\to X\), set \(Z'=f^{-1}Z\). Derived pullback carries supported objects to objects supported on \(Z'\): off that set, a K-flat acyclic stalk remains acyclic after arbitrary scalar extension, by the tensor lesson's Lemma 1.1. Pulling back the support counit therefore factors uniquely through

\[
Lf^*\mathcal S_ZK\longrightarrow\mathcal S_{Z'}Lf^*K.
\tag{5.3}
\]

For \(g:Z'\to Z\) it equivalently gives \(Lg^*R\mathcal H_ZK\to R\mathcal H_{Z'}Lf^*K\). To justify the equivalence directly, a K-flat model \(P\) on \(Z\) has K-flat \(i_*P\) on \(X\), by the stalk test. The canonical ordinary closed-set comparison \(f^*i_*P\to i'_*g^*P\) is an isomorphism on each stalk, proving the derived identity. Universal uniqueness proves that (5.3) commutes with forgetting supports and composes for two pullbacks. On cohomology, pullback uses the unit of \(Lf^*\dashv Rf_*\) and the global Leray identity from lesson six; its naturality and the counit factorization prove the supported/ordinary pullback square commutes. This is a canonical map, without a general assertion that it is invertible.

## 6. A two-point calculation and exercises

Let \(X=\{c,\eta\}\) have opens \(\varnothing,\{\eta\},X\); its closed point is \(c\). With a constant ring sheaf, a module sheaf is exactly an arrow \(r:M\to N\). Its global sections are \(M\), its sections on the open point are \(N\), and exactness is exactness at both entries. Thus global sections on this space and on its open point are exact functors. Also \(j_*N=(N\xrightarrow{1}N)\) is exact. The localization triangle gives

\[
\begin{aligned}
H^0_c(X,F)&=\ker r,\\
H^1_c(X,F)&=\operatorname{coker}r,\\
H^q_c(X,F)&=0\quad(q\ne0,1).
\end{aligned}
\tag{6.1}
\]

The corresponding ambient cohomology sheaves are these modules at \(c\), zero at \(\eta\). Ordinary supported sections only see the kernel, while the degree-one group measures the failed extension of a section from \(\eta\). The first exercise shows that failure before any resolutions are chosen.

**Exercise 1 (easy: left exactness and its limit).** Prove left exactness of closed supported sections directly from their definition. On the two-point space give an exact sequence for which they fail to be right exact.

**Solution.** In an exact sequence \(0\to F\to G\to H\), a supported section of \(G\) mapping to zero in \(H\) lifts uniquely to \(F\), by left exactness of ordinary sections. Its restriction off the closed set vanishes because its image in \(G\) does, and \(F\to G\) is injective. Thus it is supported. This proves exactness at the first two terms, globally and on every open. On the two-point space the exact sequence of arrows
\(0\to(0\to k)\to(k\xrightarrow{1}k)\to(k\to0)\to0\)
is exact at each entry. Its closed supported sections are respectively \(0,0,k\), so the last map is not surjective. All the maps used are module maps over the same ring, and the counterexample works with noncommutative coefficients too.

**Exercise 2 (medium: the localization fibre).** For an arrow \(r:M\to N\), give a complex computing the global supported object, including the connecting map \(N\to H^1_c(X,F)\).

**Solution.** Since the other two global terms are \(M[0]\) and \(N[0]\), the supported object is the shifted cone \(C(r)[-1]\). It has \(M\) in degree zero, \(N\) in degree one, and differential \(-r\). Its map to \(M[0]\) is the identity in degree zero. Rotating the cone triangle with last map \(-p\) gives the next map \(r\) and the final map \(N[0]\to C(r)\) as the positive cone inclusion. Thus its boundary on cohomology is the positive quotient \(N\to N/r(M)\). The degree-minus-one shift is why the fibre differential is \(-r\). Replacing it by \(+r\) by negating its \(N\) term would also negate the coordinate description of the boundary; one cannot make that replacement while leaving the boundary description unchanged. This proves (6.1) and checks the sign convention in a fully explicit sheaf model.

**Exercise 3 (medium: the Euclidean group and its sign).** Compute all \(H^q_{\{0\}}(\mathbb R^n,\mathbb Z)\). For \(n=1\), label the complementary rays in negative, positive order and determine the boundary of their locally constant section \((a,b)\).

**Solution.** Proposition 4.2 gives \(\mathbb Z\) in degree \(n\) and zero in all other degrees, including the whole-support case \(n=0\). In dimension one the degree-zero restriction is diagonal, so the boundary factors through \(\mathbb Z^2/\mathbb Z(1,1)\). Its positive coordinate is \(b-a\). To check the sign with actual cochains, extend the function on the two rays arbitrarily to a zero-cochain on the line. Its differential on an oriented interval crossing zero is its value at the positive endpoint minus its value at the negative endpoint, namely \(b-a\). This differential vanishes on chains contained in either ray and represents the relative degree-one class.

The flasque resolution in Lemma 4.1 also computes supported cohomology: each of its terms is acyclic for sections on the line and on the complement, and its restriction is onto, so Theorem 2.1 makes it acyclic for supported sections. The bounded-below acyclic-term theorem therefore applies. Naturality of the singular comparison identifies its cone with the relative cochain cone. Equation (2.4) says the triangle's negative projection gives precisely this positive lift differential. Thus the increasing orientation of the real line gives \(\delta(a,b)=b-a\), rather than its negative. In higher dimensions the boundary takes a chosen linking-sphere class to the corresponding supported class with this same positive lift convention; changing the orientation negates both chosen generators.

**Exercise 4 (hard: cup products with support).** Prove that forgetting supports in (5.2) gives the ordinary cup product. Prove also that first multiplying two ordinary classes and then a supported class agrees, after association, with the successive supported cup products.

**Solution.** Let \(S=\mathcal S_ZM\). The source \(K\otimes^{\mathbf L}S\) lies in \(D_Z\), so the right adjunction identifies maps from it to \(\mathcal S_Z(K\otimes^{\mathbf L}M)\) with maps from it to \(K\otimes^{\mathbf L}M\). The defining transpose is \(1_K\) tensor the support counit. Composing the supported map with the new counit therefore gives exactly that tensor map. A class is a map from the tensor unit to a shifted object; tensoring the two class maps and composing these equal morphisms proves compatibility with forgetting supports on cohomology, in every pair of degrees.

For objects \(K,L,M\), both successive support products are maps from \(K\otimes^{\mathbf L}L\otimes^{\mathbf L}\mathcal S_ZM\), an object of \(D_Z\), to \(\mathcal S_Z(K\otimes^{\mathbf L}L\otimes^{\mathbf L}M)\). Under the adjunction both are \(1_K\otimes1_L\) tensor the counit. Its uniqueness proves equality; the tensor associator identifies their sources and targets. Applying this to shifted class maps proves the assertion for classes. No exactness of global sections, flatness of the classes' sheaves, or finiteness of their degrees is used. K-flat models and the proved tensor coherence justify the entire construction.

**Exercise 5 (hard: pullback is a map, not always an isomorphism).** Explain why (5.3) composes for two ringed-space morphisms and give a case where it is not an isomorphism.

**Solution.** Pulling back the original counit through two maps gives the same morphism as pulling it back through their composite, by lesson six's coherent pullback composition. Every source involved is supported on the inverse-image closed subset. The universal factorization into its support right adjoint is unique, so the two resulting maps agree after the canonical composition identification.

For failure, take \(X=\mathbb R\), \(Z=\{0\}\), constant coefficients \(\mathbb Z\), and \(f\) the inclusion of that point with the unchanged stalk coefficient ring. Pullback is the exact stalk functor. Proposition 4.2 and its ball calculation give \(Lf^*\mathcal S_Z\mathbb Z=\mathbb Z[-1]\). The inverse-image support is the entire point, so \(\mathcal S_{Z'}Lf^*\mathbb Z=\mathbb Z[0]\). Their cohomology groups occur in different degrees, and the canonical map cannot be an isomorphism. All coefficient maps are identity maps; this failure concerns the support operation, not nonflat change of coefficient rings.
