# The right adjoint of derived pushforward

*Written and mathematically self-checked by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. The scheme compact-generation, denominator, finite-factor, duality and Appendix N blowup and Nagata assembly constructions adapt the Stacks project authors’ proofs in the freely accessible Stacks project and its pinned AI Integrated edition, and retain GFDL-1.2-or-later. Independent explanations and computations are CC0. See the course notice for component authorship and terms.*

The trace in Serre duality sends top cohomology of a canonical sheaf to the ground field. Its derived formulation is a counit: a map from the pushforward of a distinguished complex to the original complex on the base. This viewpoint puts finite maps, closed immersions and projective space into one construction. It also explains why a singular scheme may need a complex with several nonzero cohomology sheaves.

We use cohomological grading: \(H^i(C[r])=H^{i+r}(C)\). Write \(D_{\mathrm{QCoh}}(X)\) for the full subcategory of \(D(\mathcal O_X)\) whose cohomology sheaves are quasi-coherent. A perfect complex is locally represented by a bounded complex of finite locally free sheaves. All schemes in Sections 1–2 are quasi-compact and quasi-separated. No separation assumption is silently added to that convention.

The bounded-below injective machinery is taught in Injective modules and bounded-below derived functors, Theorem 2.3, Lemma 1.1 and Theorem 4.1. The exact earlier programme providers for the unbounded operations are identified in Section 1 and at their uses below. Our two preceding lessons supply the classical projective duality proofs. Appendix N writes the Noetherian Nagata construction. Section 8 says which of its prerequisites are not proved in these lessons.

## 1. Representing maps out of pushforward

For a morphism \(f:X\to Y\), its derived pushforward has a right adjoint
\[
a_f:D_{\mathrm{QCoh}}(Y)\longrightarrow D_{\mathrm{QCoh}}(X),
\qquad
\operatorname{Hom}_X(L,a_fK)
 \simeq\operatorname{Hom}_Y(Rf_*L,K).
\tag{1}
\]
The bijection is natural in both variables. We prove existence before using it: the scheme arguments below construct a perfect compact generator, the exact earlier programme theorem supplies coproduct preservation by pushforward, and the categorical proof constructs the representing object.

### The scheme input, including quasi-separated schemes

We first prove the input needed for representability. The following earlier programme results are used at their full stated generality: Quasi-coherent sheaves and concentrated scheme maps, Theorem 4.2 (unbounded affine comparison, qcqs pushforward, coproducts and finite cohomological amplitude), Theorem 5.1 (unbounded quasi-coherent projection formula), and Lemma 1.4 (finite covers and quasi-separated intersections); Perfect complexes and duals, Propositions 2.1–2.2, Theorem 3.2, Corollary 3.3 and Theorem 4.1 (finite approximation, the Tor-amplitude criterion, permanence and perfect duality); and Sections with support and the localization triangle, Theorem 2.1. In particular, the scheme input is not replaced by a separated-scheme assertion.

**Lemma 1.A (compactness and a finite Hom window).** Every perfect object \(P\) on a qcqs scheme \(X\) is compact in \(D_{\mathrm{QCoh}}(X)\). If \(P^\vee\) has Tor amplitude \([a,b]\) and quasi-coherent cohomological dimension of \(X\) is at most \(d\), then
\[
\operatorname{Hom}(P,E)=0
\quad\text{if}\quad H^q(E)=0\quad(-b-d\leq q\leq-a).
\tag{1.A}
\]
In particular \(\operatorname{Ext}^q(P,F)=0\) for every quasi-coherent sheaf \(F\) and \(q>b+d\), uniformly in \(F\).

**Proof.** Perfect duality identifies the Hom group with \(H^0R\Gamma(X,P^\vee\otimes^{\mathbf L}E)\). Tensor preserves sums, and the earlier unbounded pushforward theorem says that derived sections preserve sums on quasi-coherent complexes. Exactness of sums then proves compactness. The same theorem says that degree zero of derived sections depends only on degrees \([-d,0]\) of its input. Tensoring by an object of amplitude \([a,b]\) makes those degrees depend only on degrees \([-b-d,-a]\) of \(E\). To see this without an unbounded spectral-sequence convergence assumption, truncate \(E\) above and below that interval: the omitted lower part tensors into degrees at most \(-d-1\), and the upper part into degrees at least 1. The finite-window pushforward bound kills both contributions to degree zero. The remaining finite truncation has zero cohomology under the hypothesis. For \(E=F[q]\), its only cohomology degree is \(-q\); if \(q>b+d\), it lies below that window. \(\square\)

**Lemma 1.B (affine denominators in derived maps).** Let \(V=\operatorname{Spec}A\), \(W=\bigcup_{i=1}^rD(f_i)\), and let \(P\) be perfect on \(V\). Every derived map \(P|_W\to E|_W\), with \(E\in D_{\mathrm{QCoh}}(V)\), is represented by
\[
P\xleftarrow{\beta}P\otimes^{\mathbf L}I\xrightarrow{\gamma}E,
\tag{1.B}
\]
where \(I\) is perfect, has a map \(I\to\mathcal O_V\), and this map, hence \(\beta\), is an isomorphism on \(W\).

**Proof.** Let \(K_e\) be the Koszul complex on \(f_1^e,\ldots,f_r^e\), in degrees \(-r,\ldots,0\), with degree-zero term \(A\), and put \(I_e=\operatorname{Cone}(A\to K_e)[-1]\). Thus \(I_e\to A\to K_e\) is a triangle; \(K_e|_W=0\) because one of its entries is a unit locally. The transition \(K_{e+1}\to K_e\) is the identity in degree zero and multiplies the exterior basis indexed by \(S\) by \(\prod_{i\in S}f_i\). It induces \(I_{e+1}\to I_e\).

For every module complex \(M\), there is a chain isomorphism
\[
\underset e{\operatorname{colim}}\operatorname{Hom}^{\bullet}_A(I_e,M)
\simeq\operatorname{Tot}\check C^{\bullet}(D(f_1),\ldots,D(f_r);\widetilde M).
\tag{1.C}
\]
Indeed, cancel the identity pair coming from \(A\to K_e\) in the cone. The remaining dual terms are indexed by nonempty subsets \(S\), in Čech degree \(|S|-1\). Their transition maps multiply by \(\prod_{i\in S}f_i\), so their direct limits are \(M_{\prod_{i\in S}f_i}\). The Koszul incidence differential becomes the alternating restriction differential; choose the usual increasing exterior order on both sides. There are only \(r\) columns, so this identification holds also for unbounded \(M\). Affine intersections and the earlier affine comparison identify this finite Čech total complex with \(R\Gamma(W,\widetilde M)\). Filtered module colimits are exact, hence
\[
\underset e{\operatorname{colim}}\operatorname{Hom}_{D(A)}(I_e,M)
=H^0(W,\widetilde M).
\tag{1.D}
\]
Use \(M=R\operatorname{Hom}_A(P,E)\). A bounded finite-projective model of \(P\) makes its internal Hom quasi-coherent. Tensor–Hom adjunction turns a representative \(I_e\to M\) of the specified class into \(P\otimes I_e\to E\), proving (1.B). The existence of the bounded finite-projective affine model is proved in the next paragraph, independently of this use of (1.B).

Here are the finite-model facts used here and below. If a quasi-coherent complex on an affine is pseudo-coherent, it has a bounded-above finite-free resolution. More generally, if \(E\) is pseudo-coherent on a quasi-compact open \(W\subset V\), such a complex on \(V\) can represent \(E\) after restriction. First extend \(E\) as \(Rj_*E\) and use the earlier affine equivalence to obtain an \(A\)-complex \(M\). Choose a finite principal cover of \(W\). Start above the common upper cohomology bound with the zero complex, and descend. If a finite-free tail \(F^{\ge n}\to M\) is an isomorphism above \(n\) and surjective in degree \(n\) on every member of the cover, its cone has finite top cohomology in degree \(n-1\) on every member, by the finite-approximation criterion. Choose finitely many generators there. Represent each by a localized cycle of the cone; multiply by a sufficiently high power of that principal denominator to obtain an actual global cycle. This is possible because a localized zero differential is killed by some power of the denominator. The finitely many resulting global cycles span each localized top-cohomology module: multiplication by the denominator is a unit on that member. Attach one free generator in degree \(n-1\) for each cycle. Its two components in \(M^{n-1}\oplus F^n\) specify the comparison and the differential, with the cone sign; the cycle equation proves both \(d^2=0\) and compatibility with \(M\). The new tail is an isomorphism above \(n-1\) and surjective there. Continuing downward gives the required bounded-above finite-free complex, since each fixed degree stops changing. On each principal open its map is a quasi-isomorphism in every degree. For \(W=V\), this is the asserted affine resolution.

If the complex is also perfect, its Tor amplitude has a common finite bound. Cut this free resolution sufficiently far below that bound. Its bottom syzygy is flat by the bottom-syzygy argument in the earlier perfectness theorem; two preceding free terms give a finite presentation of it. A flat finitely presented module is finite projective, as proved in that lesson, Lemma 1.2. Replacing the bottom of the resolution by that syzygy gives a bounded finite-projective model. This also establishes the fact used before (1.C), without circular reliance on the denominator lemma. \(\square\)

**Lemma 1.C (lifting a perfect object and its map).** Let \(U\subset X\) be quasi-compact open in a qcqs scheme. Given perfect \(P\) on \(U\), quasi-coherent \(E\) on \(X\), and \(\alpha:P\to E|_U\), there is perfect \(R\) on \(X\) and \(R\to E\) such that \(R|_U\) is a finite sum of shifts of \(P\), containing \(P\) as a summand on which the map is \(\alpha\). If \(P\) is supported on \(T\cap U\), where \(T\) is closed with quasi-compact complement, \(R\) can be chosen supported on \(T\).

**Proof.** First let \(X=\operatorname{Spec}A\). Apply the last paragraph of Lemma 1.B to represent \(P\) on \(U\) by a bounded-above finite-free complex \(F\) on \(X\). Cut it at degree \(s\) far below its Tor-amplitude bound. On \(U\), \(N=\ker(F^s\to F^{s+1})\) is finite locally free, by the same flat-syzygy and finite-presentation argument. The finite tail \(Q=F^{\ge s}\) has a triangle
\[
Q|_U\longrightarrow P\longrightarrow N[1-s]\longrightarrow Q|_U[1].
\]
For sufficiently negative \(s\), the middle arrow is zero by Lemma 1.A's uniform Ext bound, applied on \(U\). Thus \(Q|_U\simeq P\oplus N[-s]\). The endomorphism of this restriction which is zero on \(P\) and the identity on \(N[-s]\) lifts, by Lemma 1.B, to a map between perfect objects on \(X\), after replacing its domain by \(Q\otimes I\). Its cone restricts to \(P\oplus P[1]\). This proves affine extension up to a summand.

For the support assertion, write \(T=V(g_1,\ldots,g_l)\) on this affine. On the qcqs open \(U\), some power of each \(g_i\) acts by zero on \(P\) in the derived category. Indeed the perfect-Hom complex \(P^\vee\otimes P\) is quasi-coherent. The earlier concentrated-map Theorem 6.2, applied to the flat principal localization of \(A\), identifies its derived-section complex localized at \(g_i\) with its derived sections on \(U\cap D(g_i)\). There \(P=0\), so the identity class becomes zero after localization. A zero localized element of the Hom module is killed by some power of \(g_i\), which proves the assertion globally on \(U\). Tensor the affine extension with the Koszul complexes on those powers. It is then supported on \(T\); its restriction is a finite sum of positive shifts of \(P\), containing \(P\), since each cone of a zero multiplication splits as the object plus its shift. Lemma 1.B now lifts the map from that summand to \(E|_U\), using a further perfect factor \(I\) which is the unit on \(U\). This factor preserves the support. This proves the entire affine assertion, with or without \(T\).

For general \(X\), add one affine \(V\) at a time to \(U\). In the step \(X=U\cup V\), the intersection \(W\) is quasi-compact. The affine construction extends \(P|_W\) to perfect \(Q\) on \(V\), with \(Q|_W\) a finite sum \(P|_W\oplus\bigoplus_{t>0}P|_W[t]^{m_t}\), and lifts the map to \(E|_V\). On \(U\) take the same finite sum of shifts of \(P\), with map \(\alpha\) on its first summand and zero on the rest. These objects and maps agree on \(W\) and glue.

For completeness, this derived gluing has an explicit cone construction. With open direct-image functors denoted by \(j_*\), take the homotopy fibre of
\[
Rj_{U*}P_U\oplus Rj_{V*}Q
\longrightarrow Rj_{W*}(P_U|_W),
\]
whose components are restriction and negative restriction, the latter composed with the chosen identification. Its restriction to \(U\) is \(P_U\): the extra two copies coming from \(W\) cancel by the identity; likewise its restriction to \(V\) is \(Q\). The Mayer–Vietoris triangle for \(E\) gives the map of fibres to \(E\); at the complex level the chosen equality of derived maps is represented by a homotopy on \(W\), which supplies that fibre map. Thus its restrictions are the specified maps. The fibre has quasi-coherent cohomology by the earlier qcqs pushforward theorem and is perfect locally on this cover. If both local objects are supported on \(T\), so is the fibre. There are finitely many added affines; induction proves the assertion. \(\square\)

**Lemma 1.D (the affine support detector).** On \(V=\operatorname{Spec}A\), let \(Z=V(f_1,\ldots,f_r)\) and \(j:V\setminus Z\hookrightarrow V\). For the Koszul complex \(K=K(f_1,\ldots,f_r)\),
\[
\operatorname{Hom}(K,E[q])=0\ (q\in\mathbb Z)
\quad\Longrightarrow\quad E\simeq Rj_*(E|_{V\setminus Z}).
\tag{1.E}
\]
In particular \(K\) detects zero objects with cohomology supported on \(Z\).

**Proof.** Every \(K_e\) in Lemma 1.B is obtained by finite sums, cones and shifts from \(K\). For one entry, the cone triangles for the composable multiplications \(f^a,f^b\) give a triangle connecting \(K(f^a)\), \(K(f^{a+b})\) and \(K(f^b)\); the cone matrix or octahedral axiom gives this triangle. Tensor it with the remaining entries and induct on each exponent. Thus the asserted Hom vanishing holds for all \(K_e\) and shifts. The triangle \(I_e\to A\to K_e\) consequently identifies \(\operatorname{Hom}(A,E[q])\) with \(\operatorname{Hom}(I_e,E[q])\). Taking the direct limit and using (1.D) identifies the map with restriction \(H^q(V,E)\to H^q(V\setminus Z,E)\). These are isomorphisms in every degree. Affine unbounded comparison detects the cone of \(E\to Rj_*E|_{V\setminus Z}\), proving (1.E). If \(E\) is supported on \(Z\), its restriction is zero. \(\square\)

**Theorem 1.E (qcqs compact generation).** The category \(D_{\mathrm{QCoh}}(X)\) has a single perfect compact generator. More generally, if \(T\subset X\) is closed with quasi-compact complement, its full subcategory of supported objects has a perfect compact generator, which is compact also in the ambient category.

**Proof.** Induct on a finite affine cover. On an affine, the generator is \(\mathcal O_X\); for the supported category use Lemma 1.D's Koszul complex. Suppose \(X=U\cup V\), with \(U\) already covered and \(V\) affine. Lift a perfect generator \(P\) of \(U\) to \(Q\) on \(X\) by Lemma 1.C. Let \(Z=X\setminus U\), a closed subset contained in \(V\) whose complement in \(V\) is quasi-compact. Choose a Koszul detector \(K\) for \(Z\) on \(V\). Its extension \(K'\) to \(X\) is perfect: it is \(K\) on \(V\) and zero on \(X\setminus Z\). More explicitly, exact open extension by zero and derived open pushforward agree for this complex. Their natural comparison is an isomorphism on \(V\) and on \(X\setminus Z\), where both vanish, so it is an isomorphism globally. In particular
\[
\operatorname{Hom}_X(K',E[q])=\operatorname{Hom}_V(K,E|_V[q]).
\]
If all maps from shifts of \(Q\oplus K'\) to \(E\) vanish, Lemma 1.D on \(V\) says that the unit \(E\to Rj_{U*}E|_U\) is an isomorphism there. It is already an isomorphism on \(U\), so its cone vanishes on a cover and it is an isomorphism globally. Now
\[
\operatorname{Hom}_X(Q,E[q])=
\operatorname{Hom}_U(Q|_U,E|_U[q])
\]
contains the group with \(P\) as a summand. The generator on \(U\) forces \(E|_U=0\), whence \(E=0\).

For the supported category, lift its generator on \(U\) with support in \(T\) using Lemma 1.C, and take on \(V\) the Koszul complex for \(Z\cap T\). Its complement is the union of the two quasi-compact opens \(V\setminus Z\) and \(V\setminus T\), so such a finite Koszul complex exists. For \(E\) supported on \(T\), its restriction to \(V\setminus(Z\cap T)\) is supported on \(T\cap U\cap V\), a closed subset of that open contained in \(U\cap V\). The same extension-by-zero argument identifies its derived direct image from this larger open with its derived direct image from \(U\cap V\). Lemma 1.D therefore again says \(E\simeq Rj_{U*}E|_U\). The preceding argument with the supported generator proves detection. Every constructed generator is perfect, and Lemma 1.A proves compactness, both in the supported subcategory and in the ambient category. \(\square\)

### The representability argument

**Lemma 1.F (cellular generation).** Let \(\mathcal T\) be a locally small triangulated category with coproducts, and let a set \(\mathcal G\) of compact objects, closed under shifts, detect zero objects. Every object belongs to the smallest triangulated subcategory containing \(\mathcal G\) and closed under coproducts.

**Proof.** For \(Y\), take \(X_1=\bigoplus_{(G,u:G\to Y)}G\) with evaluation \(v_1:X_1\to Y\). Given \(v_n\), let \(B_n\) be the coproduct of all maps \(k:G\to X_n\) with \(v_nk=0\), and complete evaluation to a triangle \(B_n\to X_n\xrightarrow{a_n}X_{n+1}\to B_n[1]\). Exactness of \(\operatorname{Hom}(-,Y)\) gives \(v_{n+1}\) with \(v_{n+1}a_n=v_n\). Define \(X\) by the telescope triangle
\[
\bigoplus_nX_n\xrightarrow{1-a}\bigoplus_nX_n
\longrightarrow X\longrightarrow\bigoplus_nX_n[1].
\tag{1.F}
\]
The compatible \(v_n\)'s lift to \(v:X\to Y\). For compact \(G\),
\[
\operatorname{Hom}(G,X)=\underset n{\operatorname{colim}}\operatorname{Hom}(G,X_n).
\]
Apply \(\operatorname{Hom}(G,-)\) to (1.F): on the direct sums of these groups, \(1-a\) is injective, since its first coordinate in a kernel element vanishes, then its second, and so on; every element has finite support. Its cokernel is the defining direct-limit quotient. The same assertion holds after shifts. Surjectivity of \(\operatorname{Hom}(G,v)\) holds at stage 1. Every kernel element at any stage is killed at the next by the defining triangle. Hence these maps are bijective for all \(G\). The cone is undetected by \(\mathcal G\), so is zero. Every \(X_n\) and its telescope were built using the allowed operations, proving the lemma. \(\square\)

**Theorem 1.G (Brown representability and adjoints).** A contravariant cohomological functor \(H:\mathcal T\to\mathrm{Ab}\) which sends coproducts to products, with \(\mathcal T\) as in Lemma 1.F, is represented by an object of \(\mathcal T\). Consequently every coproduct-preserving exact functor from \(\mathcal T\) to a locally small triangulated category has a right adjoint.

**Proof.** Take \(X_1=\bigoplus_{(G,b\in H(G))}G\). The product property gives \(b_1\in H(X_1)\) with component \(b\) on its labelled summand. An element \(b_n\in H(X_n)\) defines \(\eta_n(u)=H(u)b_n\). Let \(B_n\) be the coproduct of all \(k:G\to X_n\) in this transformation's kernel and take the same triangle as in Lemma 1.F. Its restriction of \(b_n\) to \(H(B_n)\) is zero; the cohomological exact sequence therefore gives \(b_{n+1}\) restricting to \(b_n\). The telescope and product property give an exact sequence
\[
H(X)\longrightarrow\prod_nH(X_n)
\xrightarrow{1-a^*}\prod_nH(X_n).
\]
Choose \(b\in H(X)\) over the compatible family and define \(\eta_Y(u)=H(u)b\). For every \(G\), compactness and the telescope calculation show that \(\eta_G\) is surjective by stage 1 and injective because every zero class is killed at the next stage. The objects \(Y\) on which \(\eta_{Y[q]}\) is bijective for all \(q\) form a triangulated subcategory, by natural long exact sequences and the five lemma. It is closed under coproducts, since both functors send them to products. Lemma 1.F says this subcategory is all of \(\mathcal T\), proving representability.

For an exact coproduct-preserving \(F\), apply this to \(H_K(L)=\operatorname{Hom}(FL,K)\). A map \(K\to K'\) induces a unique map of representing objects; uniqueness preserves identities and compositions and makes the bijections natural in both variables. This is the required adjoint. \(\square\)

Apply Theorems 1.E and 1.G to \(F=Rf_*\), whose exactness and preservation of coproducts are the earlier concentrated-map Theorem 4.2. Every morphism between qcqs schemes is concentrated. Choose a finite affine cover of \(X\) whose members map into affine opens of \(Y\). For an affine open \(V\subset Y\), its intersection with each of those target affines is quasi-compact by quasi-separatedness and has a finite principal cover there. Its inverse image in the corresponding source affine is therefore a finite union of principal opens. The finite union over the source cover proves quasi-compactness of \(f^{-1}V\). Quasi-separatedness follows from quasi-compact intersections in \(X\), equivalently the affine-cover criterion in that earlier lesson, Lemma 1.4. This establishes (1) for arbitrary unbounded quasi-coherent complexes.

The same argument applied to the inclusion \(D_{\mathrm{QCoh}}(Y)\hookrightarrow D(\mathcal O_Y)\), which preserves coproducts since quasi-coherence and cohomology commute with sums, constructs \(DQ_Y\). Its counit is universal among maps from quasi-coherent complexes. This proves the coherator used below, in precisely the required unbounded category.

The **trace** is the counit
\[
\operatorname{Tr}_f(K):Rf_*a_fK\longrightarrow K,
\tag{2}
\]
corresponding to the identity of \(a_fK\). Thus the transpose of \(u:L\to a_fK\) is precisely \(\operatorname{Tr}_f(K)\circ Rf_*u\). This definition specifies the normalization of every computation below.

**Proposition 1.1.** The functor \(a_f\) is exact, commutes with shifts, and sends bounded-below objects to bounded-below objects. For composable morphisms \(X\xrightarrow fY\xrightarrow gZ\), there is a canonical isomorphism
\[
a_{gf}\simeq a_fa_g.
\tag{3}
\]
Under it, the composite trace is \(\operatorname{Tr}_g\circ Rg_*\operatorname{Tr}_f\).

**Proof.** Shifting both sides of (1) gives the shift isomorphism. Right adjoints of exact triangulated functors are exact: given a triangle on the target, transpose its first two maps, complete to a triangle, and test the third map by the adjunction and the long exact Hom sequences. The five lemma gives the required isomorphism with the third adjoint object. This is the usual derived adjunction construction, with its compatible shift maps.

Choose \(d\geq0\) such that \(Rf_*D^{\leq b}_{\mathrm{QCoh}}(X)\subset D^{\leq b+d}_{\mathrm{QCoh}}(Y)\) for every \(b\). The uniform bound, including for unbounded complexes, is proved in the earlier concentrated-map lesson, Proposition 3.3 and Theorem 4.2. On each member of a finite affine cover of \(Y\), use its finite-cover bound on the inverse image and take the maximum; thus a single \(d\) works on \(Y\). If \(K\in D^{\geq c}(Y)\), set \(T=\tau_{\leq c-d-1}a_fK\). Then \(Rf_*T\in D^{\leq c-1}(Y)\), so
\[
\operatorname{Hom}_X(T,a_fK)=\operatorname{Hom}_Y(Rf_*T,K)=0.
\]
In particular the truncation map \(T\to a_fK\) is zero. On every cohomology sheaf in degrees at most \(c-d-1\) that map is the identity identification, so those sheaves vanish. Hence \(a_fK\in D^{\geq c-d}(X)\).

Finally, transpose twice:
\[
\operatorname{Hom}_X(L,a_fa_gK)
 \simeq\operatorname{Hom}_Y(Rf_*L,a_gK)
 \simeq\operatorname{Hom}_Z(Rg_*Rf_*L,K).
\]
Using the canonical composition of derived pushforwards, Yoneda proves (3). The displayed rule for transposes proves the trace formula. Repeating the argument three times shows associativity: both comparison maps induce the same bijection on every Hom set. \(\square\)

The bound need not be zero. For projective \(n\)-space, the adjoint of the field occurs in degree \(-n\), as Section 4 will show.

There are now three different operations to keep track of. Pullback is the left adjoint of pushforward; it transports sections and tensors them with the structure sheaf upstairs. The functor \(a_f\) is its right adjoint and represents maps from a pushforward into a prescribed target. The compactification construction \(f^!\), introduced later, uses the right adjoint of a proper map followed by restriction. Finite maps make the second operation concrete as coinduction; open immersions will show why the second and third operations require separate names.

## 2. What sheafified duality says

Distinguish internal \(R\mathcal H om_X\), which is a complex of sheaves, from global \(R\operatorname{Hom}_X\). Evaluation and the counit give a canonical morphism
\[
Rf_*R\mathcal H om_X(L,a_fK)
 \longrightarrow R\mathcal H om_Y(Rf_*L,K).
\tag{4}
\]
One construction first maps into \(R\mathcal H om_Y(Rf_*L,Rf_*a_fK)\), using evaluation and the projection-formula comparison, and then applies (2). Internal Hom of arbitrary unbounded quasi-coherent complexes need not have quasi-coherent cohomology. This prevents us from treating (4) as an isomorphism merely by applying (1).

Let \(DQ_Y:D(\mathcal O_Y)\to D_{\mathrm{QCoh}}(Y)\) be the right adjoint of the inclusion, constructed after Theorem 1.G. This is the adjoint of the full quasi-coherent-cohomology subcategory in the unbounded category, not merely the derived sheaf-level coherator.

**Proposition 2.1.** Applying \(DQ_Y\) to (4) gives an isomorphism. Taking global sections of (4) gives
\[
R\operatorname{Hom}_X(L,a_fK)
 \simeq R\operatorname{Hom}_Y(Rf_*L,K).
\tag{5}
\]

**Proof.** Test (4) against \(M\in D_{\mathrm{QCoh}}(Y)\). The tensor–Hom and pullback–pushforward adjunctions identify its source Hom group with
\[
\operatorname{Hom}_X(Lf^*M\otimes^{\mathbf L}L,a_fK)
 \simeq
\operatorname{Hom}_Y(Rf_*(Lf^*M\otimes^{\mathbf L}L),K).
\]
The unbounded quasi-coherent projection formula identifies the last group with
\[
\operatorname{Hom}_Y(M\otimes^{\mathbf L}Rf_*L,K)
 \simeq
\operatorname{Hom}_Y(M,R\mathcal H om_Y(Rf_*L,K)).
\]
The projection formula holds for every qcqs morphism and both indicated quasi-coherent complexes, without a perfectness condition on \(M\); the exact earlier programme proof is the concentrated-map lesson, Theorem 5.1. The identifications just made are induced by evaluation and the counit, hence by (4). The defining adjunction of \(DQ_Y\) and Yoneda prove the first assertion. Testing with \(M=\mathcal O_Y[-r]\) proves that (4) induces an isomorphism on every global hypercohomology group. This gives (5), since global derived Hom is the derived global sections of internal Hom. \(\square\)

There is a second, distinct locality issue. If \(V\subset Y\) is quasi-compact open, \(U=f^{-1}(V)\), and \(f_V:U\to V\), there is a canonical comparison
\[
(a_fK)|_U\longrightarrow a_{f_V}(K|_V).
\tag{6}
\]
It comes from \(K\to Rj_*(K|_V)\) and the two open adjunctions. The following proof establishes it for proper maps over a Noetherian base and explains exactly what is additionally needed over an arbitrary base.

**Lemma 2.2 (finite factorization and killing a supported map).** If \(C\) is compact and \(E\) is built by the cellular construction of Lemma 1.F from compact objects \(G\), every map \(C\to E\) factors through a finite sequence of sums, shifts and cones of the \(G\)'s. Consequently, if \(T\subset Y\) is closed with quasi-compact complement \(V\), \(P\) is pseudo-coherent, and \(Q\in D^+_{\mathrm{QCoh}}(Y)\) is supported on \(T\), every map \(P\to Q\) is killed after precomposition with
\[
I\otimes^{\mathbf L}P\longrightarrow P,
\tag{2.A}
\]
where \(I\to\mathcal O_Y\) is a perfect map which restricts to the identity isomorphism on \(V\).

**Proof.** Compactness first factors a map to the telescope through some stage \(E_n\), by the calculation in Lemma 1.F. We prove the finite factorization for that stage by induction. Stage 1 is a coproduct, so compactness gives a finite subcoproduct. In the stage triangle \(B\to E_{n-1}\to E_n\to B[1]\), the composite \(C\to B[1]\) factors through a finite subcoproduct \(B_0[1]\). Complete it to \(B_0\to C'\to C\to B_0[1]\). The triangle axiom gives a compatible map to the stage triangle. The object \(C'\) is compact, because compact objects are closed under cones: apply the two Hom long exact sequences to a coproduct comparison and use the five lemma. By induction, \(C'\to E_{n-1}\) factors through a finite object \(A\). Take the cone of \(B_0\to C'\to A\); triangle morphisms give a factorization of the specified composite to \(B[1]\) through this finite cone. Its map to \(E_n\) may differ from the original by a map coming from \(E_{n-1}\). Apply the induction hypothesis once more to that difference, and add its finite factor as a summand. This gives the exact original map, not just its composite into \(B[1]\). It proves finite factorization.

Now put \(H=R\mathcal H om_Y(P,Q)\). It has quasi-coherent cohomology: on an affine, resolve \(P\) by a bounded-above finite-free complex using Lemma 1.B, and represent \(Q\) by a bounded-below module complex. In each fixed Hom degree only finitely many pairs of terms occur. Thus localization commutes with this Hom complex and its cohomology. It is supported on \(T\), since internal derived Hom restricts to the corresponding internal Hom and \(Q|_V=0\). The given map is a class \(\mathcal O_Y\to H\).

Use Theorem 1.E's supported perfect generator to build \(H\) cellularly within the supported category. That telescope is also a telescope in the ambient category, since the inclusion preserves coproducts and triangles. The ambient compact object \(\mathcal O_Y\) therefore factors its map through a perfect \(A\) supported on \(T\), by the finite argument just proved; its use does not require \(\mathcal O_Y\) to belong to the supported category. Complete \(\mathcal O_Y\to A\) to \(I\to\mathcal O_Y\to A\to I[1]\). Then \(I\) is perfect, is the unit on \(V\), and \(I\to\mathcal O_Y\to H\) is zero. Tensor–Hom adjunction says exactly that (2.A) kills the original map. \(\square\)

**Theorem 2.3 (proper restriction, with a verified Noetherian case).** If \(f\) is proper and \(Y\) is Noetherian, (6), for its quasi-compact open \(V\), is an isomorphism for every \(K\in D^+_{\mathrm{QCoh}}(Y)\). More generally, the same proof applies whenever \(Rf_*P\) is pseudo-coherent for every perfect \(P\) on \(X\).

**Proof.** First we show that \(a_f\) takes bounded-below objects supported on \(Y\setminus V\) to objects supported on \(X\setminus U\). Otherwise a perfect generator on \(U\) gives a nonzero map \(P_U\to(a_fQ)|_U\). Lift this map by Lemma 1.C to a map \(P\to a_fQ\), with \(P\) perfect on \(X\), whose restriction includes that nonzero map. Its transpose is \(Rf_*P\to Q\). The source is pseudo-coherent under the stated general hypothesis. In the Noetherian case this hypothesis follows from [Proper morphisms and coherent direct images](proper-morphisms-and-coherent-direct-images.md), Theorem 4.1: the finite truncation filtration of \(P\) has coherent cohomology sheaves, each with coherent higher direct images; the cohomological-dimension bound makes the output bounded. On a Noetherian affine, a bounded-above complex with finite cohomology has a bounded-above finite-free resolution by successively resolving its top cohomology and the next cone, so it is pseudo-coherent.

Lemma 2.2 supplies \(I\to\mathcal O_Y\), the unit on \(V\), killing the transpose after tensoring. The earlier unbounded projection formula identifies the new source with \(Rf_*(Lf^*I\otimes P)\). Transposing back shows that
\[
Lf^*I\otimes P\longrightarrow P\longrightarrow a_fQ
\]
is zero. On \(U\), its first arrow is an isomorphism, contradicting the chosen nonzero restriction. This proves the support assertion.

Let \(j:V\hookrightarrow Y\) and \(h:U\hookrightarrow X\). Usual pushforward restriction and two adjunctions give, naturally in \(L\) and \(N\),
\[
\begin{aligned}
\operatorname{Hom}_X(L,a_fRj_*N)
&=\operatorname{Hom}_Y(Rf_*L,Rj_*N)\\
&=\operatorname{Hom}_V(R(f_V)_*h^*L,N)\\
&=\operatorname{Hom}_X(L,Rh_*a_{f_V}N).
\end{aligned}
\]
Hence \(a_fRj_*\simeq Rh_*a_{f_V}\). Apply \(a_f\) to the localization triangle \(Q\to K\to Rj_*j^*K\), where \(Q\) is bounded below and supported outside \(V\). Restrict to \(U\). Its first term vanishes by the support assertion, and \(h^*Rh_*\) is the identity. The remaining arrow is exactly (6), proving the theorem. \(\square\)

**Lemma 2.4 (proper flat finite presentation).** If \(f:X\to Y\) is proper, flat and of finite presentation, with \(Y\) qcqs, then \(Rf_*P\) is perfect for every perfect \(P\) on \(X\). In particular it is pseudo-coherent, and Theorem 2.3 proves (6) for this case as well, for every quasi-compact open \(V\) and every bounded-below input.

**Proof: descending the finite data.** Work on an affine open \(\operatorname{Spec}A\) of \(Y\), and write \(A=\operatorname{colim}A_i\) as its finite-type \(\mathbb Z\)-subalgebras. [Semicontinuity and Grauert's theorem](semicontinuity-and-grauerts-theorem.md), Lemma 0.1, proves that a finite-presentation model of this proper flat \(X/A\) can be made proper and flat over a Noetherian \(A_i\): apply its scheme, properness and flatness descent with the sheaf \(\mathcal O_X\). We still have to descend the perfect complex, rather than treating it as one globally free complex on \(X\).

Choose a finite affine cover \(U_1,\ldots,U_m\) on which \(P\) is represented by bounded complexes \(P_a\) of finite projective modules, in a common interval \([s,t]\). Such models follow from Lemma 1.B's finite-model argument. The intersections \(U_I\) are affine, since \(X\) is separated over an affine base. They, their inclusions and their rings descend to a common stage by the finite-open and finite-presentation descent in the earlier limits lesson and the separated-diagonal descent used in Lemma 0.1. Each projective term is the image of a finite idempotent matrix. Its differential is a finite matrix between those images. Thus these terms and differentials are specified by finitely many entries and the equations \(e^2=e\), \(ed=d=de\) and \(d^2=0\).

The gluing also has finite chain data, including the necessary homotopies. On each affine intersection, choose chain maps between the restricted local models which represent their identification with \(P\), and homotopy inverses. A derived map between bounded projective complexes is represented by a chain map; equality is represented by a chain homotopy. Record the inverse identities up to homotopy. On triple intersections record the homotopy between the two compositions. Continue with higher intersections: for an increasing tuple of length \(q+1\), record the degree \(1-q\) map making the boundary of the previous homotopies vanish. These are precisely the finitely many equations which say that the sum of the local differential, the restriction differential and the higher homotopy maps in the ordered Čech total complex squares to zero.

Here is why these coherent choices exist, and not just the pairwise homotopies. Use a common resolution representing the original global \(P\) on each intersection. A quasi-isomorphism to that resolution induces a quasi-isomorphism on the Hom complex out of each bounded projective local model. Inductively, the boundary of the next desired homotopy is a cycle. Its image in the common resolution is a boundary: there all comparisons are the restrictions of the same global object, and the preceding chosen comparisons and homotopies have already been recorded. Injectivity on the cohomology of the Hom complex makes the cycle a boundary in the local model. Choose its preimage, adjusting by a cycle when necessary using surjectivity on that same cohomology. This supplies the next homotopy and the compatibility with the common resolution. Start with the chosen local quasi-isomorphisms and repeat on the increasing tuples. There are no tuples of length greater than \(m\); the finite interval of the models also kills sufficiently negative Hom degrees. Thus only finitely many finite matrices and finite equations are involved. This argument also records the augmentation which identifies the resulting total complex with the original \(P\).

Represent all these entries in a common stage. Every stated matrix equality holds there after moving to a sufficiently late stage, since a zero element in the filtered colimit is zero eventually. Descend the equations for the inverse homotopies as well. The finite cover remains a cover at a late stage. Its descended coherent chain data glue to an object \(P_i\) on \(X_i\): explicitly use the finite ordered Čech totalization, with the higher homotopies as its extra differential components. Restriction to each \(U_{a,i}\) is equivalent to the local bounded projective model. The contraction which inserts the index \(a\) cancels the Čech columns on that open; the recorded homotopy equations make this contraction compatible with the extra components. Equivalently, eliminate the pairs of columns containing and not containing \(a\), starting from the longest tuples; their diagonal map is the recorded homotopy equivalence and the higher components are exactly its successive corrections. There are finitely many columns, so elimination terminates and leaves \(P_{a,i}\). Therefore \(P_i\) is perfect, and its derived pullback to \(X\) is the given \(P\). This describes the descent of the actual local complexes, equivalences, homotopies and their finite compatibility equations; it does not assume a resolution property for \(X\).

**Proof: the finite projective image and arbitrary tensor.** Apply sections to this finite Čech model. It gives a bounded complex \(C_i\) of \(A_i\)-flat modules which computes \(R\Gamma(X_i,P_i)\). Each term is a finite sum of finite projective modules over an affine-intersection ring; that ring is \(A_i\)-flat because \(X_i\to\operatorname{Spec}A_i\) is flat. Direct summands of its finite free modules are consequently \(A_i\)-flat. The acyclic-affine Čech calculation applies to the total complex with its recorded homotopies, or to the finite filtration by its columns: on each column it is the earlier affine comparison, and finite induction proves the total assertion.

The cohomology modules of \(C_i\) are finite. Indeed \(P_i\) is bounded coherent over the Noetherian \(X_i\), and the finite cohomology-sheaf filtration together with [Proper morphisms and coherent direct images](proper-morphisms-and-coherent-direct-images.md), Theorem 4.1, makes its derived sections bounded with finite cohomology. [Base change and the Grothendieck complex](base-change-and-the-grothendieck-complex.md), Lemma 3.1, therefore replaces \(C_i\), after shifting its finite interval, by a bounded complex \(K_i\) of finite projective \(A_i\)-modules, with a quasi-isomorphism which stays one after tensoring with every \(A_i\)-module.

For any \(A_i\)-algebra \(B\), the cover, the idempotent matrices and every differential and homotopy in \(C_i\) base change termwise. The resulting total complex is \(C_i\otimes_{A_i}B\), and computes the derived pullback of \(P_i\) on \(X_{i,B}\). Its local terms are base-flat, so ordinary tensor here computes derived tensor. The same finite Čech calculation gives
\[
K_i\otimes_{A_i}B
\simeq R\Gamma(X_{i,B},LP_i|_{X_{i,B}}).
\tag{2.B}
\]
Take \(B=A\). It follows that \(R\Gamma(X,P)\) is represented by the bounded finite projective complex \(K_i\otimes_{A_i}A\). Affine comparison makes \(Rf_*P\) perfect on this affine open of \(Y\). These opens cover \(Y\), so it is perfect globally. Lemma 2.2 and Theorem 2.3 now give the claimed proper restriction. All support-generation steps use the quasi-compact \(V\) specified in (6); any further assertion of locality is checked on quasi-compact affine opens. \(\square\)

## 3. Finite maps and closed immersions

Let \(f:X\to Y\) be finite between Noetherian schemes, and put \(B=f_*\mathcal O_X\), a coherent sheaf of \(\mathcal O_Y\)-algebras. Quasi-coherent sheaves on \(X\) correspond to quasi-coherent \(B\)-modules on \(Y\). In the derived category this correspondence is given by exact affine pushforward; it preserves and detects quasi-isomorphisms.

**Theorem 3.1.** For \(K\in D^+_{\mathrm{QCoh}}(Y)\), the object \(a_fK\), expressed as a \(B\)-complex on \(Y\), is
\[
R\mathcal H om_{\mathcal O_Y}(B,K),
\qquad (b\varphi)(b')=\varphi(bb').
\tag{7}
\]
For a closed immersion \(i:Z\hookrightarrow Y\), this is the derived functor of the annihilator sheaf
\[
i^bK=\mathcal H om_Y(i_*\mathcal O_Z,K),
\]
regarded as a sheaf on \(Z\). Its derived value is often denoted \(Ri^bK\).

**Proof.** The sheaf-level coinduction identity is
\[
\operatorname{Hom}_B(M,\mathcal H om_Y(B,J))
 \simeq\operatorname{Hom}_{\mathcal O_Y}(M,J).
\tag{8}
\]
Evaluation at \(1\) gives the forward map; the inverse sends \(v\) to \(m\mapsto[b\mapsto v(bm)]\). This works on every open subset and glues. Restriction of scalars is exact, so its right adjoint sends injectives to injectives. Resolve \(K\) by a bounded-below injective complex \(J\). Formula (8), applied to complexes, identifies the derived adjunction with coinduction into \(\mathcal H om_Y(B,J)\).

This complex has quasi-coherent cohomology. Locally on the Noetherian base, resolve the finite module \(B\) by finite free modules in nonpositive degrees. The bounded-below hypothesis on \(K\) makes each fixed total degree involve only finitely many terms. Hom therefore commutes with localization and computes quasi-coherent Ext sheaves. The equivalence for affine pushforward now transports the complex back to \(X\). It represents exactly the Hom functor (1), proving (7). For \(B=\mathcal O_Y/\mathcal I\), its terms are annihilated by \(\mathcal I\), so they are the asserted sheaves on \(Z\). \(\square\)

The \(B\)-action in (7) is essential. An ambient internal Hom complex without its algebra action has not yet specified an object on \(X\). The trace in this model is evaluation at \(1\), not an unspecified ring trace.

**Example 3.2 (an effective Cartier divisor).** If \(Z=D\) is an effective Cartier divisor in \(Y\), resolve \(\mathcal O_D\) by
\[
0\longrightarrow\mathcal O_Y(-D)\longrightarrow\mathcal O_Y
 \longrightarrow\mathcal O_D\longrightarrow0.
\]
Applying Hom into \(\mathcal O_Y\) gives \(\mathcal O_Y\to\mathcal O_Y(D)\) in degrees 0 and 1. The map is injective, and its cokernel is the normal line \(N_{D/Y}=\mathcal O_D(D)\). Thus
\[
a_i(\mathcal O_Y)=N_{D/Y}[-1].
\tag{9}
\]
The minus sign in the shift places the normal line in cohomological degree 1.

## 4. Projective space and the classical trace

**Theorem 4.1.** For \(\pi:P=\mathbf P^n_k\to\operatorname{Spec}k\),
\[
a_\pi(k)\simeq\mathcal O_P(-n-1)[n]=\omega_P[n].
\tag{10}
\]
The counit is the trace whose ordered Čech representative extracts the coefficient of \(T_0^{-1}\cdots T_n^{-1}\).

**Proof.** The projective-space calculation gives \(R\Gamma(P,\omega_P[n])\simeq k\), with the specified trace. Transpose that map to obtain \(c:\omega_P[n]\to a_\pi(k)\). For a coherent sheaf \(F\), testing \(c\) against every shift of \(F\) gives the maps
\[
\operatorname{Ext}^{n+r}_P(F,\omega_P)
 \longrightarrow\operatorname{Hom}_{D(k)}(R\Gamma(P,F),k[r])
 \simeq H^{-r}(P,F)^\vee.
\]
These are precisely the Yoneda trace pairings proved in [Serre duality on projective space](ext-sheaves-and-serre-duality-on-projective-space.md), Theorem 5.1. They are isomorphisms for all \(r\), including the zero groups outside the cohomological range.

Finite truncation triangles extend this assertion from coherent sheaves to every bounded complex with coherent cohomology. In particular it holds for a perfect generator \(G\) of \(D_{\mathrm{QCoh}}(P)\), which is bounded coherent because \(P\) is Noetherian and quasi-compact. If \(C\) is the cone of \(c\), then \(\operatorname{Hom}(G,C[r])=0\) for every \(r\). The generator property forces \(C=0\). Thus the map is an isomorphism in the full unbounded category, not merely on coherent test objects. When \(n=0\), this is the identity adjunction on the field; every twist on the point is the same line. \(\square\)

**Theorem 4.2 (the relative projective bundle).** Let \(E\) be locally free of rank \(n+1\geq1\) on a qcqs scheme \(Y\), and use the quotient convention for \(\pi:\mathbf P(E)\to Y\). Then
\[
a_\pi(\mathcal O_Y)\simeq
\pi^*\det E\otimes\mathcal O_{\mathbf P(E)}(-n-1)[n].
\tag{11}
\]

**Proof of the trace.** On an affine free-frame open, [Cohomology of projective space](cohomology-of-projective-space.md), Theorem 2.2, gives just one nonzero cohomology module for \(\mathcal O(-n-1)\), in degree \(n\), generated by \([1/(T_0\cdots T_n)]\). Its ordered trace sends that generator to one. Under a change of frame by \(M\), the generator transforms by \(\det(M)^{-1}\). Here is a presentation-independent verification, valid over every ring: the Koszul resolution of the quotient of \(A[T_0,\ldots,T_n]\) by its variables has top exterior term \(\bigwedge^{n+1}A^{n+1}\). Its dual class maps, through the dual power-Koszul complexes, to the reciprocal-monomial class in top Čech degree. The direct-limit identification is the termwise localization calculation (1.C), now for the variables. Changing the variables multiplies the top exterior term by \(\det M\), hence its dual by the inverse determinant. The map into Čech cohomology is defined by the quotient and localization maps and respects a change of presentation. This proves the transformation law, including elementary changes with nondiagonal entries. Thus tensoring by \(\det E\) glues these local traces to a canonical isomorphism
\[
R\pi_*D\simeq\mathcal O_Y,
\qquad D=\pi^*\det E\otimes\mathcal O(-n-1)[n].
\tag{4.A}
\]
Transpose it to \(c:D\to a_\pi\mathcal O_Y\).

**Proof of detection on projective space.** On \(\mathbf P_A^n\), the objects \(\mathcal O,\ldots,\mathcal O(-n)\) detect zero unbounded quasi-coherent complexes. The sheafified Koszul complex of the homogeneous coordinates is exact, since at every point one coordinate is a unit and contracts it. Twisting this complex successively shows that all \(\mathcal O(-m)\), \(m\geq0\), are finite extensions of shifts of the displayed twists. If their Hom groups to a complex \(C\), in all degrees, vanish, then \(R\Gamma(\mathbf P_A^n,C(m))=0\) for every \(m\geq0\). On a standard chart \(D_+(T_i)\), localization is the telescope of multiplication by \(T_i\) on these twists. This assertion follows on every trivializing affine from the exact module localization \(\operatorname{colim}(M\xrightarrow{T_i}M\to\cdots)=M_{T_i}\), and the telescope is that colimit by its injective \(1-\mathrm{shift}\) map. Derived sections commute with these telescopes by the earlier coproduct theorem. Consequently derived sections of \(C\) on every standard chart vanish. Affine comparison gives \(C=0\). This proves detection for unbounded complexes over arbitrary \(A\), without invoking coherent resolutions over \(A\).

**Proof that the transpose is an isomorphism.** Take the perfect generator \(G\) on \(Y\) from Theorem 1.E. The objects
\[
L_i=\pi^*G\otimes\mathcal O(i),\qquad -n\leq i\leq0,
\]
detect zero on \(\mathbf P(E)\). Indeed, vanishing of their shifted Hom groups implies \(R\pi_*(C\otimes\mathcal O(-i))=0\), by adjunction and detection by \(G\). Restrict usual pushforward to an affine free-frame open on the base and use the projective-space detector just proved. This makes \(C\) vanish on an open cover.

For \(-n\leq i<0\), the earlier twist calculation gives both \(R\pi_*\mathcal O(i)=0\) and \(R\pi_*(D\otimes\mathcal O(-i))=0\). Perfect duality and the projection formula identify all Hom groups from \(L_i\) to both the source and target of \(c\) with zero groups. For \(i=0\), the groups on its source are
\[
\operatorname{Hom}_Y(G,R\pi_*D[q])
=\operatorname{Hom}_Y(G,\mathcal O_Y[q]),
\]
while its target groups, by the adjunction, are
\[
\operatorname{Hom}_Y(R\pi_*\pi^*G,\mathcal O_Y[q])
=\operatorname{Hom}_Y(G,\mathcal O_Y[q]).
\]
The map is the identity under these identifications because \(c\) was transposed from (4.A), and the projection comparison is defined by evaluation. Thus the cone of \(c\) is undetected by all the \(L_i\), and is zero. This proves (11). When \(n=0\), the only detector is \(\pi^*G\), \(\mathbf P(E)=Y\), and \(\mathcal O(1)=\pi^*E\); the two line factors cancel. No proper-locality theorem was used in this argument. \(\square\)

## 5. Proper duality over a field

Let \(p:X\to\operatorname{Spec}k\) be proper, and define
\[
\omega_X^\bullet=a_p(k).
\]

**Theorem 5.1.** For every \(K\in D_{\mathrm{QCoh}}(X)\) and every integer \(i\), the trace induces
\[
H^i(X,K)^\vee\simeq
\operatorname{Ext}^{-i}_X(K,\omega_X^\bullet).
\tag{12}
\]
If \(X\) is projective, Cohen–Macaulay and equidimensional of dimension \(n\), then
\[
\omega_X^\bullet\simeq\omega_X^\circ[n],
\]
where \(\omega_X^\circ\) is the dualizing sheaf of the preceding lesson.

**Proof.** Formula (1) gives
\[
\operatorname{Hom}_X(K,\omega_X^\bullet[-i])
 \simeq\operatorname{Hom}_{D(k)}(R\Gamma(X,K),k[-i]).
\]
Over a field, every complex splits into its cohomology complex and a contractible complex: choose complements to boundaries inside cycles and to cycles inside each term. Its maps to \(k[-i]\) in the derived category are consequently exactly the linear functionals on \(H^i\). This remains valid for unbounded complexes and infinite-dimensional cohomology; no finite-dimensional biduality has been used. It proves (12). For bounded coherent \(K\), proper coherence gives the familiar finite-dimensional interpretation.

For the last assertion embed \(i:X\hookrightarrow P=\mathbf P^N_k\). Composition and Theorems 3.1 and 4.1 identify
\[
\omega_X^\bullet=Ri^b(\omega_P[N]).
\]
The preceding lesson proves that \(Ri^b\omega_P\) has only one cohomology sheaf, in degree \(c=N-n\), and that this sheaf is \(\omega_X^\circ\). Thus it is \(\omega_X^\circ[-c]\); shifting by \(N\) gives \(\omega_X^\circ[n]\). The classical representing trace was defined from the same ambient pairing, so this identification respects traces. \(\square\)

**Theorem 5.2 (the complex on an arbitrary proper scheme).** For every proper \(k\)-scheme \(X\), the complex \(\omega_X^\bullet=a_p(k)\) is bounded coherent, is locally dualizing, and has cohomology only in \([-\dim X,0]\).

**Proof.** Fix an affine open \(U\subset X\). Embed \(U\) as a closed subscheme of \(\mathbf A_k^N\) using finite algebra generators, and let \(Z\) be its scheme-theoretic closure in \(\mathbf P_k^N\). It is projective, contains \(U\) as an open, and has dimension \(\dim U\): taking the closure introduces no new irreducible components unrelated to the dense open. The scheme-theoretic closure exists by taking on each affine the kernel of restriction to the prescribed open and gluing those quasi-coherent ideals; on a Noetherian scheme they are coherent.

Let \(W\) be the scheme-theoretic closure of the graph of the two inclusions of \(U\) in \(X\times_k Z\). Both projections \(h:W\to X\) and \(q:W\to Z\) are proper, because the product factors are proper and \(W\) is closed. Both inverse images of \(U\) are precisely this common \(U\). Indeed, above \(U\subset X\) the graph of \(U\to Z\) is already closed, since \(Z\) is separated; above \(U\subset Z\) the graph of \(U\to X\) is already closed, since \(X\) is separated. Formation of scheme-theoretic closure restricts to these opens, so there is no extra scheme structure there.

Composition of the adjoints and the Noetherian proper restriction theorem give
\[
\begin{aligned}
(a_p k)|_U
&\simeq(a_h a_p k)|_U\\
&\simeq a_{W\to\operatorname{Spec}k}(k)|_U\\
&\simeq(a_q a_{Z\to\operatorname{Spec}k}k)|_U\\
&\simeq a_{Z\to\operatorname{Spec}k}(k)|_U.
\end{aligned}
\tag{5.A}
\]
The local maps are isomorphisms because the restrictions of \(h\) and \(q\) over these opens are identity maps. This argument only constructs a common refinement of the two already existing proper schemes. It does not use a compactification theorem for arbitrary finite-type maps.

By the closed-immersion and projective-space computations, the last object is the restriction of
\[
C_Z=Ri^b\mathcal O_{\mathbf P^N}(-N-1)[N].
\]
The preceding lesson, [Dualizing sheaves and Serre duality for projective schemes](dualizing-sheaves-and-serre-duality-for-projective-schemes.md), Proposition 8.1, proves its local dualizing property by derived coinduction and finite regular-local resolutions. It also proves bounded coherence. Its Lemma 2.1 kills the ambient Ext sheaves below \(N-\dim Z\); the regular-local resolution bound kills them above \(N\). Thus its shifted cohomology lies in \([-\dim Z,0]\). For the latter bound, the exact earlier provider is Regular local rings, Theorem 2.2 and Proposition 3.3: polynomial ambient local rings are regular of dimension at most \(N\), and have that finite global dimension. No regularity of \(Z\) or \(X\) is asserted.

Equation (5.A) proves these properties on every affine open of \(X\). Bounded coherence and the dualizing condition are local; a finite affine cover supplies a common finite bound, and \(\dim U\leq\dim X\) supplies the stated uniform interval. This proves the theorem for proper schemes which are not projective and for schemes with nilpotents and embedded components. \(\square\)

The embedded-point example \(X=V(T_0^2,T_0T_1)\subset\mathbf P^2\) from the preceding lesson has \(H^{-1}(\omega_X^\bullet)=\mathcal O_{\mathbf P^1}(-2)\) and \(H^0(\omega_X^\bullet)=k_p\). Dropping its second cohomology sheaf was exactly what made the single-sheaf duality formula fail.

## 6. Coinduction versus restriction

For a finite \(k\)-algebra \(B\), Theorem 3.1 gives \(a_p(k)=\operatorname{Hom}_k(B,k)\) in degree zero. This is coinduction; \(k\) is injective as a vector space, so there is no higher cohomology.

Now take \(A=k[t]\), \(B=k[x]\), with \(t=x^2\). As an \(A\)-module, \(B=A\oplus Ax\) is free. Let \(\lambda:B\to A\) extract the coefficient of \(x\). The pairing \((b,b')\mapsto\lambda(bb')\) has matrix
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
in the basis \(1,x\), so \(B\to\operatorname{Hom}_A(B,A)\), \(b\mapsto b\lambda\), is a \(B\)-linear isomorphism in every characteristic. Hence \(a_f(\mathcal O_Y)\simeq\mathcal O_X\). Under this chosen trivialization the counit sends \(a+bx\) to \(b\). The algebraic trace of multiplication is a different functional: it sends \(1\) to \(2\), and in characteristic 2 it vanishes identically.

For an open immersion \(j:U\hookrightarrow X\), the compactification functor \(j^!\) discussed below is restriction, but the right adjoint \(a_j\) of \(Rj_*\) generally differs. An explicit affine example is
\[
j:\operatorname{Spec}A[t^{-1}]\hookrightarrow\operatorname{Spec}A,
\qquad A=k[t].
\]
Here \(a_j(A)=R\operatorname{Hom}_A(A[t^{-1}],A)\), with its \(A[t^{-1}]\)-action. In degree zero this is zero: the image of \(1\) under an \(A\)-linear map must lie in every \(t^mA\), whose intersection is zero; the same argument applies to each \(t^{-r}\). But \(j^!A=A[t^{-1}]\) has nonzero degree zero. Thus restriction cannot be the general right adjoint of pushforward.

More precisely, the free telescope resolution has map \(e_r\mapsto e_r-te_{r+1}\) on \(\bigoplus_{r\geq0}A\). Its cokernel is \(A[t^{-1}]\), with \(e_r\) mapping to \(t^{-r}\); its injectivity follows by examining the last nonzero coefficient in a finite sum. Dualizing computes \(a_j(A)\) by
\[
\prod_{r\geq0}A\longrightarrow\prod_{r\geq0}A,
\qquad (b_r)\longmapsto(b_r-tb_{r+1})
\tag{13}
\]
in degrees 0 and 1. Its cokernel is \(k[[t]]/k[t]\). Indeed, sending \((c_r)\) to \(\sum t^rc_r\) modulo \(A\) is surjective. A sequence is in its kernel exactly when that sum is a polynomial \(s\); then \(b_r=(s-\sum_{j<r}t^jc_j)/t^r\) is a polynomial and solves (13). This calculation makes the failure visible in both degrees.

For a separated finite-type map \(f:X\to Y\) of Noetherian schemes, the compactification assertion is that there is an open immersion \(j:X\hookrightarrow\overline X\) followed by a proper map \(\overline f:\overline X\to Y\), with \(f=\overline f j\). This is the Nagata theorem. Theorem N.E.1 in Appendix N proves this existence assertion from the exact earlier inputs listed there. Some prerequisites of those inputs are not proved in these lessons. The following arguments prove independence and composition for the compactifications so constructed.

Given such a compactification, put on bounded-below quasi-coherent complexes
\[
f^!K=j^*a_{\overline f}K.
\tag{14}
\]
Proposition 1.1 makes its value bounded below. We may replace \(\overline X\) by the scheme-theoretic closure of \(X\) in it, so that \(X\) is schematically dense; the proper comparison below identifies the two constructions.

**Proposition 6.1 (independence of compactification).** Formula (14) is independent of the compactification, with canonical comparisons satisfying the cocycle condition.

**Proof.** For two compactifications, take the scheme-theoretic closure \(Z\) of the diagonal copy of \(X\) in \(\overline X_1\times_Y\overline X_2\). It is proper over \(Y\). Its projections \(g_i:Z\to\overline X_i\) are proper and restrict to the identity of \(X\). Moreover \(g_i^{-1}(X)=X\): over that open in one factor, the graph of \(X\to\overline X_{3-i}\) is already closed because the second factor is separated over \(Y\). Thus restriction of its closure adds nothing there. This is also true scheme-theoretically. Adjoint composition identifies \(a_{\overline f_Z}=a_{g_i}a_{\overline f_i}\), and Theorem 2.3 restricted over \(X\) identifies
\[
j_Z^*a_{\overline f_Z}
\simeq j_i^*a_{\overline f_i}.
\tag{6.A}
\]
All maps used here are the transposes of the pushforward composition and open restriction maps. For two consecutive proper refinements, their comparison is the composite comparison: transposing either map gives the same pushforward counit, followed by ordinary restriction. Associativity of the pushforward comparisons and the adjunction triangle identities prove equality, rather than only existence of an isomorphism.

To check independence of the common refinement, take the closure of the diagonal \(X\) in the product of two proposed refinements. It dominates both, with the same inverse-image property. The preceding composition identity shows that their two comparisons agree after this further refinement; its comparison is an isomorphism, so they agree before it. Using the closure in a triple product proves the cocycle identity for three compactifications in exactly the same way. Thus (6.A) supplies canonical, compatible identifications. The scheme-theoretic-density replacement is the special case of a proper refinement which is the identity over \(X\). \(\square\)

**Proposition 6.2 (composition).** For composable separated finite-type maps of Noetherian schemes, there is a canonical isomorphism \((gf)^!\simeq f^!g^!\). These comparisons are associative.

**Proof.** Choose \(Y\hookrightarrow\overline Y\xrightarrow{\overline g}Z\), and compactify \(X\to\overline Y\) as \(X\hookrightarrow\overline X\xrightarrow{F}\overline Y\). Let \(U=F^{-1}Y\). Then \(X\hookrightarrow U\to Y\) is a compactification of \(f\), and \(X\hookrightarrow\overline X\to Z\) is a compactification of \(gf\). With \(A=a_F\), \(B=a_{\overline g}\), and \(A'=a_{U\to Y}\), adjoint composition gives
\[
(gf)^!K=(ABK)|_X.
\]
The proper restriction isomorphism for \(F\), followed by restriction from \(U\) to \(X\), gives
\[
(ABK)|_X\simeq (A'((BK)|_Y))|_X=f^!g^!K.
\]
If different choices are made, take common refinements for the two \(\overline Y\)'s and then common refinements for the resulting \(\overline X\)'s. The comparison squares commute because their transposes are the same composition and restriction maps; this is the composition identity proved in Proposition 6.1. Hence the isomorphism is choice-independent. For three maps use one nested system of compactifications. Both comparison routes are successive ordinary restrictions of the same triple right adjoint, with the same composite counit. They agree by Proposition 1.1's associativity and the restriction composition identity. Refinement-independence then proves associativity for every choice. \(\square\)

For an open immersion one can take the identity proper map after the given open embedding, so \(j^!=j^*\). For a proper map one can take the identity open embedding, so \(f^!=a_f\) on the stated bounded-below domain. Together with Theorem N.E.1, these identifications and Propositions 6.1–6.2 prove the stated functorial claims. The general unbounded adjoint has already been constructed independently of this existence theorem.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Compute the adjoint of \(k\) for \(B=k[\epsilon]/(\epsilon^2)\), its \(B\)-action and the counit.

**Solution.** Let \(\lambda\) extract the coefficient of \(\epsilon\). The two functionals \(\lambda,\epsilon\lambda\) form a basis of \(B^\vee\), because \(\epsilon\lambda\) extracts the constant coefficient. Thus \(B^\vee=B\lambda\), and \(\epsilon\) sends \(\lambda\) to \(\epsilon\lambda\) and the latter to zero. The counit is evaluation at \(1\): it sends \(a\lambda+b\epsilon\lambda\) to \(b\). This is a degree-zero complex.

**Exercise 7.2 (easy).** Derive the composite adjunction and verify its counit on a map \(u:L\to a_fa_gK\).

**Solution.** Its two transposes are \(Rf_*L\xrightarrow{Rf_*u}Rf_*a_fa_gK\xrightarrow{\operatorname{Tr}_f}a_gK\) and then \(Rg_*Rf_*L\to Rg_*a_gK\xrightarrow{\operatorname{Tr}_g}K\). This is the transpose under \(a_{gf}\), giving (3) and the asserted composite counit. Naturality in \(u\) proves equality of the transformations.

**Exercise 7.3 (medium).** For a closed immersion of Noetherian schemes, explain why ordinary annihilators do not generally compute the derived adjoint. Compute the example \(A=k[t]\), \(A\to k=A/(t)\), with input \(A\).

**Solution.** The ordinary annihilator is \(\operatorname{Hom}_A(k,A)=0\). The free resolution \(A\xrightarrow tA\) in degrees \(-1,0\) gives the dual complex \(A\xrightarrow tA\) in degrees \(0,1\). Its only cohomology is \(k\) in degree 1, so the adjoint is \(k[-1]\). The derived annihilator construction of Theorem 3.1 supplies the missing Ext term.

**Exercise 7.4 (medium).** Recover classical Serre duality for a coherent sheaf \(F\) on \(\mathbf P^n_k\) from (10) and the adjunction, including its signs.

**Solution.** Taking \(K=F\) in (12) gives
\[
H^i(F)^\vee=\operatorname{Hom}(F,\omega_P[n-i])
 =\operatorname{Ext}^{n-i}(F,\omega_P).
\]
The pairing sends a cohomology class and its Ext partner to their composite into \(\omega_P[n]\), followed by the trace. This agrees with the ordered Čech normalization in Theorem 4.1. For \(n=0\) it is the vector-space evaluation pairing.

**Exercise 7.5 (medium).** In the squaring map example, compute the action of \(x\) on the dual basis \(\lambda_0,\lambda_1\), which extracts the coefficients of \(1,x\). Identify a generator and its counit.

**Solution.** For \(a+bx\), multiplying by \(x\) gives \(bt+ax\), so \(x\lambda_0=t\lambda_1\) and \(x\lambda_1=\lambda_0\). Hence \(\lambda_1\) generates the dual as a free \(B\)-module; its two \(A\)-basis vectors are \(\lambda_1,x\lambda_1=\lambda_0\). Evaluation at \(1\) takes them to \(0,1\), respectively. This computation remains valid at the branch point and in characteristic 2.

**Exercise 7.6 (hard).** Verify that the degree-one module in the open-immersion calculation is nonzero, and that multiplication by \(t\) on \(k[[t]]/k[t]\) is invertible.

**Solution.** The series \(\sum_{r\geq1}t^{r!}\) is not a polynomial, so gives a nonzero class. If \(ts\) is a polynomial, then the formal series \(s\) is a polynomial, proving injectivity. For any series \(s\), remove its constant term; \((s-s(0))/t\) is a formal series whose class maps to \([s]\), proving surjectivity. Thus the module has the required \(A[t^{-1}]\)-action. Together with its zero degree-zero cohomology this explicitly distinguishes \(a_j(A)\) from \(j^!A\).

## 8. Construction sources and remaining proof obligations

The unbounded affine comparison, qcqs pushforward, its coproduct preservation and cohomological amplitude, and the unrestricted quasi-coherent projection formula are the exact earlier concentrated-map Theorems 4.2 and 5.1. Perfect duality, finite Tor-amplitude models and finite approximation are the exact earlier perfect-complex results listed in Section 1. Their uses here preserve the earlier hypotheses, including quasi-separated schemes and arbitrary unbounded inputs. Lemmas 1.A–1.D and Theorem 1.E prove the scheme compact-generation step in this lesson. Lemma 1.F and Theorem 1.G prove cellular generation, Brown representability, the right-adjoint consequence and the coherator. Lemma 2.2 and Theorem 2.3 prove the supported-map argument and proper restriction in the Noetherian case; Lemma 2.4 proves the proper flat finite-presentation case over an arbitrary qcqs base. Theorems 4.2 and 5.2 prove the relative projective-bundle computation and the bounded coherent locally dualizing complex on every proper field-scheme. The six solutions have been retained.

Appendix N writes the full Noetherian Nagata construction: coherent blowup charts and strict transforms, protected rational-section elimination, improvement near a closure, separated common enlargement, the dense-open valuative argument and the two-open compactification induction. Theorem N.E.1 includes nonreduced schemes and nonaffine bases. The exact earlier affineness-descent support used in Lemma N.A.3 is bound below and has a written proof. The finite-piece input to Lemma N.A.4 still has recursive algebraic audit boundaries recorded in the prerequisite record. This written construction does not certify all earlier programme proofs or their source lists.

The freely accessible construction source is the Stacks project authors’ *Derived Categories*, *Derived Categories of Schemes*, *Cohomology of Sheaves*, and *Duality for Schemes*, in the [pinned AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/tree/565b10e987aba5969b21145a0833f42d69f96790). Exact source components consulted for the new scheme and category arguments are `perfect.tex`, “Lifting complexes”, “Generating derived categories” and “The coherator revisited”; `derived.tex`, “Generators of triangulated categories” and “Brown representability”; and `duality.tex`, “Right adjoint of pushforward”, “Right adjoint of pushforward and restriction to opens”, “Upper shriek functors”, and “Duality for proper schemes over fields”. Adaptations of those proof constructions retain GFDL-1.2-or-later; the course notice records the component rights. These are construction and attribution links, not replacements for the programme proofs just identified.

Amnon Neeman, [*Grothendieck duality via homotopy theory*](https://arxiv.org/abs/alg-geom/9412022v1), 27 December 1994, Sections 3–4, is a freely accessible antecedent for the categorical construction. Its scheme example is separated. The lesson proves the qcqs scheme input above and does not use that example to assert the greater generality. No paid book is used or cited as a construction source, template or historical credit.

## Appendix N. Nagata compactification over a Noetherian base

We now prove compactification existence for every separated finite-type map of Noetherian schemes. The source and base may have nilpotents and embedded components, and separation is relative to the specified base. The construction preserves the entire open source as a scheme.

The exact earlier inputs are:

- Projective morphisms and Chow's lemma, Section 4 and Theorem 4.1: scheme-theoretic closure and the full Noetherian Chow construction, including the dense affine cover. Its general-base Theorem 5.1 is not used here.
- Proper morphisms and valuative criteria, Theorems 2.1, 3.1, 4.1–4.2 and Corollary 2.2: permanence, all-valuation-ring properness, projective spaces and graded Proj. Its discrete-valuation criterion is not used.
- Valuation rings and separatedness, Theorems 2.1 and 4.1: general valuation domination and specialization witnesses. Its discrete-domination Lemma 5.1 is not used.
- The diagonal and separated morphisms, Theorems 4.1 and 5.1: relative closed graphs, equalizers and separation permanence.
- Étale neighbourhoods, henselization and quasi-finite morphisms, Theorem 4.3 and its proof from Theorem 4.2 and Lemma 4.1: finite clopen pieces over elementary étale neighbourhoods. The polynomial-normality input to its algebraic support is proved in lesson 10, Lemma 0.1; the conductor and strong-transcendence support is written in lesson 10, Appendix Z. The remaining lower regular-local, dimension and flatness-slicing audit boundaries are recorded in the prerequisite record.
- Descending properties, Lemma 4.1 and the affineness part of Theorem 2.1: the finite affine equalizer for flat base change and descent of affineness. The exact supporting Faithfully flat descent, Theorems 1.3, 2.5, 6.2 and 7.1 and Lemma 6.1, writes the Amitsur contraction, invariant-module recovery, scheme-map descent and affine-algebra effectivity. These are the earlier proof inputs for the affineness part, with their current identities recorded in the prerequisite record.

The proofs below supply the Nagata construction from these written earlier results. The lower regular-local, dimension and flatness-slicing prerequisites named above are not proved in these lessons; external references do not replace their proofs.

### N.A. Blowups, closure, and two elementary descent facts

For a quasi-compact immersion \(D\to T\) between Noetherian schemes, write \([D]_T\) for its scheme-theoretic closure, defined by the coherent ideal
\[
\ker(\mathcal O_T\longrightarrow j_*\mathcal O_D).
\]
This ideal and its compatibility with open restriction are the written construction preceding the earlier Chow Theorem 4.1. In particular, \(D\) is an open subscheme of \([D]_T\), and restriction of functions on the latter to \(D\) is injective. We call this **schematic density**. A closed subscheme containing a schematically dense open is the whole scheme. Two morphisms into a separated target agreeing on a schematically dense open agree, since their closed equalizer's ideal restricts to zero.

A **\(D\)-admissible modification** in this proof is a finite sequence of blowups with coherent ideals whose zero loci avoid the successive copy of \(D\). Permitting sequences avoids any use of a theorem that a composite is a single blowup. Each step, and hence the sequence, is proper and an isomorphism over \(D\).

**Lemma N.A.1 (the blowup calculations).** Let \(T\) be Noetherian and \(I\subset\mathcal O_T\) coherent. The blowup \(b:T'\to T\) is proper. Its pulled-back ideal is invertible as an ideal; the complement of its zero locus is schematically dense in \(T'\). Over the locus where \(I=\mathcal O_T\), the map is an isomorphism. It has the following additional properties.

1. If \(D\subset T\) is schematically dense and \(I|_D=\mathcal O_D\), then \(D\) remains schematically dense in \(T'\). If \(D\) is merely topologically dense, it remains topologically dense.
2. If \(Z\to T\) has a schematically dense open \(D\), and \(I|_D=\mathcal O_D\), then the closure of \(D\) in \(Z\times_T T'\) is the blowup of \(Z\) in \(I\mathcal O_Z\). This is its strict transform. In particular, for a closed \(Z\subset T\), this blowup is closed in \(T'\).
3. If \(W\subset T\) is open and \(J\subset\mathcal O_W\) is coherent with zero locus avoiding \(D\cap W\), it extends to a coherent ideal on \(T\) whose zero locus avoids \(D\), and its blowup restricts to the prescribed blowup on \(W\).
4. Two finite \(D\)-admissible sequences over a scheme in which \(D\) is schematically dense have a common refinement which is a finite \(D\)-admissible sequence over each. Their strict transforms can consequently be used interchangeably after such a refinement.

**Proof.** On \(T=\operatorname{Spec}A\), form the Rees ring \(R(I)=\bigoplus_{n\geq0}I^n t^n\subset A[t]\). A finite generating list of \(I\) gives a homogeneous surjection from a polynomial ring, so \(\operatorname{Proj}R(I)\) is a closed subscheme of finite projective space. It is proper by the earlier properness theorem. Localization of the Rees ring gives compatible schemes on affine base opens, proving properness globally.

For \(a\in I\), its standard chart is
\[
\operatorname{Spec}A[I/a],\qquad
A[I/a]\subset A_a,
\tag{N.A.1}
\]
where the subalgebra is generated by the fractions \(x/a\), \(x\in I\). This equality follows by taking the degree-zero part of \(R(I)_{at}\): a degree-zero element has the form \(x/a^n\) with \(x\in I^n\). These charts cover. The ideal \(I\) on this chart is generated by \(a\), and \(a\) is a nonzerodivisor because this ring is a subring of \(A_a\). Thus the ideal is invertible and its complement is schematically dense. When \(I=A\), the Rees ring is \(A[t]\), whose Proj is \(\operatorname{Spec}A\). The same argument on an open proves the asserted isomorphism locus.

For (1), write the restriction map on an affine base as \(A\hookrightarrow\Gamma(D,\mathcal O_D)\). Localizing and using the finite affine equalizer calculation gives an injection \(A_a\hookrightarrow\Gamma(D\cap D(a),\mathcal O)\). The chart ring in (N.A.1) injects into this last ring. The copy of \(D\) on that chart contains \(D\cap D(a)\), so restriction to it is injective. For topological density, the complement of the exceptional divisor is dense in every chart; it identifies with the corresponding open of \(T\setminus V(I)\), in which \(D\) is dense. Therefore \(D\) is dense in \(T'\).

For (2), on an affine chart \(Z=\operatorname{Spec}B\), the degree-zero map onto \(B[IB/a]\subset B_a\) identifies this algebra with the image of
\[
B\otimes_A A[I/a]\longrightarrow B_a.
\]
Its kernel is exactly the ideal vanishing on \(D\cap D(a)\): \(D\) is schematically dense in \(Z\), so after localization vanishing there is vanishing in \(B_a\). The resulting charts are the scheme-theoretic closure of \(D\), and they are the blowup charts for (IB). They glue compatibly. The closed-immersion assertion also follows from the surjection of Rees rings \(R_A(I)\twoheadrightarrow R_{A/K}((I+K)/K)\) when \(Z=V(K)\).

For (3), glue \(J\) on \(W\) to the unit ideal on \(D\). They agree on \(D\cap W\). The closed subscheme of \(D\cup W\) thereby defined has a scheme-theoretic closure in \(T\). The ideal of that closure restricts to the prescribed ideal on \(D\cup W\), hence is coherent and is the unit ideal on \(D\). Rees rings commute with localization, giving the desired restriction. This works at every successive step of a finite sequence.

For (4), first consider two single blowups in ideals \(I,J\). The blowup in (IJ) dominates both: on a local ring upstairs, if \(IJ=(c)\) with \(c\) a nonzerodivisor, write \(c=\sum x_i y_i\), \(x_i\in I,y_i\in J\). Some \((x_i y_i)/c\) is a unit, since their sum is one. For that pair \((x,y)\), multiplication by \(y\) and cancellation show every element of \(I\) is a multiple of \(x\); similarly \(J=(y)\). Both are invertible ideals. The universal property of a blowup now gives the two maps. That universal property itself follows on (N.A.1): wherever \(a\) generates an invertible pulled-back ideal, the required ring map sends \(x/a\) to the unique quotient of \(x\) by \(a\), and the maps agree on overlaps.

For sequences, one can instead take successive strict transforms of the steps of the second sequence over the first. By (2) each such step is a blowup of the pulled-back ideal. The resulting scheme is the closure of \(D\) in the fibre product of the two modifications: each stage is schematically dense along \(D\), and the same chart-image calculation identifies that closure. Interchanging the two sequences identifies it with the corresponding sequence over the second modification. This proves (4). \(\square\)

If \(D\subset T\) is any open, blowing up an ideal with support \(T\setminus D\) makes \(D\) schematically dense: in (N.A.1), \(D\cap b^{-1}\operatorname{Spec}A\) contains \(D(a)\), and the chart embeds into \(A_a\). This remains true when the original \(D\) was not dense. Components disjoint from \(D\) are removed by the blowup. No reducedness assumption occurs.

**Lemma N.A.2 (separating closures).** If \(T_1,T_2\) are disjoint closed subsets of an open \(D\subset T\), there is a \(D\)-admissible blowup after which their closures are disjoint.

**Proof.** Give their closures \(Z_1,Z_2\subset T\) reduced closed subscheme structures, with ideals \(I_1,I_2\), and blow up \(I_1+I_2\). Its centre \(Z_1\cap Z_2\) misses \(D\). The strict transform of \(Z_i\) is empty on every standard chart with denominator in \(I_i\): after inverting that denominator the ideal of \(Z_i\) is the unit ideal. The charts with denominators in \(I_1\cup I_2\) cover the blowup. Thus the two strict transforms are disjoint. Each contains the closure of the unchanged \(T_i\), since \(T_i\) avoids the centre. \(\square\)

**Lemma N.A.3 (isomorphism descent used here).** If an existing map becomes an isomorphism under an étale covering of its target, it is an isomorphism.

**Proof.** Étale covering maps are open and flat, and every affine target open has a finite affine refinement which is faithfully flat. Affineness descends by the written affineness part of AG-DFG, Theorem 2.1. Thus over that affine target the original map is \(\operatorname{Spec}B\to\operatorname{Spec}A\). For its faithfully flat affine covering \(A\to A'\), the ring map becomes \(A'\to A'\otimes_A B\), an isomorphism. The kernel and cokernel of \(A\to B\) vanish because their flat base changes vanish. Therefore \(A\to B\) is an isomorphism. These conclusions agree on target overlaps and prove the assertion. \(\square\)

**Lemma N.A.4 (the quasi-affine input, proved without the nonaffine Zariski Main Theorem).** A separated quasi-finite finite-type morphism \(q:Z\to T\) of Noetherian schemes is quasi-affine.

**Proof.** Work first with \(T=\operatorname{Spec}A\), and set \(H=\operatorname{Spec}\Gamma(Z,\mathcal O_Z)\). The canonical map \(\alpha:Z\to H\) is compatible with flat base change by the earlier AG-DFG Lemma 4.1. For each \(z\in Z\), with image \(t\in T\), apply the written AG-FSE Theorem 4.3 to obtain an affine elementary étale neighbourhood \(T'\to T\) and a finite clopen \(P\subset Z_{T'}\) containing the selected lift of \(z\). Its complement \(Q\) is quasi-compact, and
\[
\Gamma(Z_{T'},\mathcal O)=\Gamma(P,\mathcal O)\times\Gamma(Q,\mathcal O).
\]
Since \(P\to T'\) is finite, it is affine. Hence \(H_{T'}\) has \(P\) as an open-and-closed component, and \(\alpha_{T'}^{-1}(P)=P\) with the map on this inverse image the identity. The maps \(P\subset H_{T'}\to H\) are étale and have open images. Let \(O\subset H\) be the union of these images over all the choices. They cover \(\alpha(Z)\), and each such image is contained in \(\alpha(Z)\), so \(O=\alpha(Z)\). The induced covering of \(O\) is étale; the pullback of \(Z\to O\) to every member is the isomorphism \(P\to P\). Lemma N.A.3 proves \(Z\simeq O\).

The image is quasi-compact because \(Z\) is, so this is a quasi-compact open embedding into an affine scheme over \(T\). Applying the same construction on affine opens of an arbitrary \(T\), localization compatibility gives the quasi-coherent algebra \(q_*\mathcal O_Z\), and the resulting embeddings glue into \(\underline{\operatorname{Spec}}_T(q_*\mathcal O_Z)\). This proves the relative assertion. \(\square\)

### N.B. The elimination construction

We prove the particular elimination theorem needed in the compactification construction, including its protection of a larger open.

**Theorem N.B.1.** Let \(T\) be Noetherian, let \(W\subset V\subset T\) be opens with \(W\) schematically dense in \(T\), and let \(p:Y\to T\) be separated and finite type. Let \(s:W\to Y\) be a section whose graph is closed in \(Y\times_T V\). There is a finite \(V\)-admissible sequence \(T'\to T\) for which the closure of the lifted \(s(W)\) in \(Y\times_T T'\) maps isomorphically to an open of \(T'\). This open contains \(W\).

**Proof, first case: \(W=V\), affine \(T\), and quasi-affine \(Y/T\).** A quasi-affine finite-type scheme over an affine base admits a finite-coordinate immersion into affine space. Here is the needed argument. Write \(Y\) as a quasi-compact open of \(\operatorname{Spec}B\); choose finitely many principal opens \(D_B(g_i)\) covering it and contained in it. Each \(B_{g_i}\) is finite type over the base ring \(A\). Choose finitely many algebra generators and express them as fractions with numerator in \(B\). The subalgebra \(C\subset B\) generated over \(A\) by these finitely many numerators and the \(g_i\) satisfies \(C_{g_i}=B_{g_i}\). Thus \(Y\) embeds as \(\bigcup D_C(g_i)\subset\operatorname{Spec}C\), and \(C\), being finite type, gives a closed embedding into some \(\mathbf A^n_T\).

It is enough first to extend the composite \(s:W\to\mathbf A^n_T\) to a map into \(\mathbf P^n_T\) after \(W\)-admissible blowups. Put \(A=\Gamma(T,\mathcal O_T)\), \(M=\Gamma(W,\mathcal O_W)\), and write \(f_1,\ldots,f_n\in M\) for its coordinate functions. Schematic density identifies \(A\subset M\). Define two finitely generated ideals of \(A\):
\[
I=\{a\in A:af_j\in A\text{ for every }j\},\qquad
J=I+If_1+\cdots+If_n\subset A.
\tag{N.B.1}
\]
Both restrict to the unit ideal on \(W\). To verify this, cover \(W\) by finitely many \(D(u)\subset T\). Localization of the finite affine equalizer gives \(M_u=A_u\). Each \(f_j\) therefore has a denominator which is a power of \(u\); clearing the resulting finitely many localization equalities gives \(u^Nf_j\in A\) for one \(N\). Hence \(u^N\in I\).

Blow up \(I\), then the pulled-back ideal \(J\). Both steps protect \(W\). Denote the resulting invertible ideals by \(I'\) and \(J'\). Multiplication by \(1,f_1,\ldots,f_n\) first defines \(A\)-linear maps \(I\to J\), because these products belong to \(A\subset M\). Pull them back and then map to the ideal \(J'\). They factor through the image ideal \(I'\): every section of the kernel of the pulled-back module map to \(I'\) has zero image in \(J'\) on \(W\), hence zero image everywhere, since \(J'\subset\mathcal O_{T'}\) and \(W\) is schematically dense. Thus they give maps \(I'\to J'\), and their images generate \(J'\), by the definition of \(J\). Therefore they give \(n+1\) generating sections of the invertible sheaf \(J'\otimes(I')^{-1}\), and hence a map
\[
T'\longrightarrow\mathbf P^n_T
\]
whose restriction to \(W\) is \([1:f_1:\cdots:f_n]\).

Choose an ambient open \(G\subset\mathbf A^n_T\) in which \(Y\) is closed. On the inverse image \(O\) of \(G\), its equations vanish on \(W\); schematic density from Lemma N.A.1 makes them vanish on \(O\). Thus the map factors through \(Y\) on \(O\). Its graph is closed in \(T'\times_T Y\), as the pullback of the closed graph of the map to \(\mathbf P^n_T\). The graph is the closure of \(s(W)\), since \(W\) is schematically dense in \(O\). This proves the case.

**Second case: \(W=V\), arbitrary \(T\), and quasi-affine \(Y/T\).** Apply the first case independently over a finite affine cover of \(T\). Extend the first local sequence's successive coherent centres to the whole scheme by Lemma N.A.1(3), protecting \(W\). For each next base open, take the common refinement, from Lemma N.A.1(4), of its prescribed local sequence and the restriction of the global sequence already performed. Extend the remaining refinement centres from that current open to the whole current scheme, again protecting \(W\). Once the graph closure is an open over a base open, further protected blowups retain that property: its strict transform is the pullback of that open, by schematic density and Lemma N.A.1(2). Thus processing the finitely many base opens gives one finite sequence for which the graph closure is locally an open everywhere. The local open immersions agree, being the projections of the same scheme-theoretic closure, and give an open immersion globally.

**Third case: general \(W\subset V\), still quasi-affine \(Y/T\).** Let \(H=[s(W)]_Y\). The hypothesis says \(H|_V=s(W)\). Put \(C=\overline{V\setminus W}\subset T\), with coherent ideal \(I\), and give \(T\setminus V\) coherent ideal \(K\). The closed subscheme \(H\cap V(I^2\mathcal O_Y)\) has support over \(T\setminus V\): over \(V\), the closure is the graph \(s(W)\), and \(C\cap W=\varnothing\). Noetherianity and quasi-compactness give an \(N\) such that
\[
K^N\mathcal O_H\subset I^2\mathcal O_H.
\tag{N.B.2}
\]
Indeed the coherent quotient \(\mathcal O_H/I^2\mathcal O_H\) is supported on \(V(K)\); on finitely many affine charts a power of every finite generator of \(K\) annihilates it, and a common larger power of \(K\) does so.

Set \(J=I^2+K^N\), and blow up \(I+J=I+K^N\). This centre misses \(V\). Write \(b:T_1\to T\), and let \(H_1\) be the closure of \(s(W)\) in \(Y\times_T T_1\). We claim
\[
H_1\cap p_1^{-1}\bigl(\overline{V\setminus W}^{\,T_1}\bigr)=\varnothing.
\tag{N.B.3}
\]
The strict transform of \(C=V(I)\) contains the indicated closure. Its standard charts have denominators in \(J\): on a chart with denominator in \(I\), the strict transform of \(V(I)\) is empty. On a chart with denominator \(a\in J\), equation (N.B.2) writes the image of \(a\) on \(H\) as
\[
a=\sum_\ell b_\ell c_\ell d_\ell,
\qquad c_\ell,d_\ell\in I.
\]
On the lifted graph \(s(W)\) in this chart, \(a\) is invertible, because the blowup is the identity over \(V\) and this chart there is \(D(a)\). Therefore the regular function
\[
\sum_\ell b_\ell(c_\ell/a)d_\ell
\]
is a regular function on the closed base change of \(H\) in the chart, which contains \(H_1\). It is one on the lifted graph, hence one on \(H_1\) by schematic density. It is zero on the inverse image of \(V(I)\). This proves (N.B.3).

Let \(T_0=T_1\setminus\overline{V\setminus W}^{\,T_1}\). The entire \(H_1\) lies over \(T_0\), and \(T_0\cap V=W\). The morphism \(H_1\to T_0\) is quasi-affine: it is a closed subscheme of the quasi-affine \(Y\times_T T_0\). Apply the second case there, protecting \(W\). Extend all its centres to \(T_1\), protecting \(V\), by gluing them to the unit ideal on \(V\) before taking closure. The extension is possible because their restrictions to \(T_0\cap V=W\) are the unit ideal. The final graph closure still lies over \(T_0\), is open there, and is consequently open in the entire modified base. This proves the third case.

**Last case: arbitrary separated finite-type \(Y/T\).** Choose a finite affine cover \(Y_i\) of \(Y\) and put \(W_i=s^{-1}(Y_i)\), \(T_i=[W_i]_T\), \(V_i=T_i\cap V\). Discard empty \(W_i\). Then \(W_i\) is schematically dense in \(T_i\). Each \(Y_i\times_T T_i\to T_i\) is quasi-affine: the inverse image of an affine base open is a quasi-compact open of the affine \(Y_i\), and these target-local embeddings are the definition of relative quasi-affineness. Its section on \(W_i\) has closed graph over \(V_i\), by restriction of the original closed graph.

Apply the third case on \(T_i\). A coherent centre on a closed subscheme extends by its inverse image under the quotient structure-sheaf map; since it is the unit ideal on \(V_i\), the extended ideal is the unit ideal on \(V\). Lemma N.A.1(2) identifies the closed strict transform with the prescribed blowup of \(T_i\). At each subsequent \(i\), use Lemma N.A.1(4) to refine both its prescribed sequence and the already performed sequence restricted to its closed strict transform. Extend the remaining refinement centres by the same quotient-ideal construction. Performing these finitely many sequences and retaining the previous properties under further strict transforms gives a \(V\)-admissible \(T_1\to T\) for which the closure of each \(s(W_i)\) over \(Y_i\) is the graph of an open subscheme of a closed strict transform of \(T_i\).

Let \(H_1\) be the full graph closure in \(T_1\times_T Y\). On \(T_1\times_T Y_i\), its underlying space is the closure of \(s(W_i)\), since closure restricts to opens. The preceding closed graph contains this closure and projects injectively to \(T_1\). Thus each fibre of \(H_1\to T_1\) has at most one point in each of the finitely many \(Y_i\), so all its fibres are finite. A finite-type scheme over a field with finitely many points is zero-dimensional and all its points are isolated; this proves quasi-finiteness. The morphism is separated because \(Y/T\) is. Lemma N.A.4 now makes \(H_1/T_1\) quasi-affine.

Finally apply the third case to \(H_1\to T_1\), the original \(W\subset V\), and its section. Its closure over \(V\) is still the original closed section, since every preceding centre avoided \(V\). The resulting open graph maps to \(Y\) and is precisely the closure of \(s(W)\) in the final \(T'\times_T Y\). This proves the theorem. \(\square\)

**Corollary N.B.2 (the elimination form).** Let \(p:Z\to T\) be separated and finite type between Noetherian schemes, and let \(D\subset T\) be open with \(p^{-1}D\to D\) an isomorphism. After a finite \(D\)-admissible sequence, the strict transform of \(Z\) is an open subscheme of the modified \(T\). If \(p\) is proper, that open is the whole modified \(T\).

**Proof.** First blow up an ideal with support \(T\setminus D\). This makes \(D\) schematically dense in the modified base and makes the strict transform of \(Z\) the closure of its copy of \(D\), by the chart calculation in Lemma N.A.1. Apply Theorem N.B.1 with \(W=V=D\) to the inverse section. The graph closure is the accumulated strict transform and becomes an open. If \(p\) is proper, its strict transform is proper over the modified base. The open image is therefore closed. It contains the schematically dense \(D\), so is the entire base. \(\square\)

### N.C. Three geometric assembly lemmas

**Lemma N.C.1 (improvement near a closure).** Let \(p:Z\to T\) be proper between Noetherian schemes, \(V\subset T\) open, and \(F\subset V\) closed. Suppose \(p\) is an isomorphism over an open neighbourhood of \(F\) in \(V\). There is a finite \(V\)-admissible sequence after which its strict transform is an isomorphism over a neighbourhood of the closure of \(F\).

**Proof.** Let \(B\subset V\) be the complement of the largest open on which \(p|_V\) is an isomorphism. This is closed and disjoint from \(F\). Lemma N.A.2 separates their closures by a \(V\)-admissible blowup. Set \(T_0=T\setminus\overline B\), \(V_0=V\setminus B=T_0\cap V\). The closure of \(F\) lies in \(T_0\), and \(p\) is an isomorphism on \(V_0\). Apply the proper part of Corollary N.B.2 over \(T_0\). Extend its centres to the whole scheme while protecting \(V\), using Lemma N.A.1(3). Over the inverse image of \(T_0\), the resulting strict transform is an isomorphism, and that open still contains the closure of \(F\). \(\square\)

**Lemma N.C.2 (separated common enlargement).** Let \(S\) be Noetherian, and let \(D\to T_1,T_2\) be open embeddings of separated finite-type \(S\)-schemes. Finite \(D\)-admissible modifications \(T_i'\to T_i\) can be embedded openly into one separated finite-type \(S\)-scheme, identifying their copies of \(D\).

**Proof.** Let \(Z=[D]_{T_1\times_S T_2}\). Over the copy of \(D\) in either target, its projection is exactly \(D\to D\): the other map's graph is already closed there, and closure restricts to opens. Apply Corollary N.B.2 to each projection, so that the strict transforms \(Z_i\) embed openly into modifications of \(T_i\). The induced \(Z_i\to Z\) are finite blowup sequences by Lemma N.A.1(2). Lemma N.A.1(4) gives a common finite refinement \(Z'\) over both. Extend these successive blowup centres from the open \(Z_i\) to the respective modifications of \(T_i\), protecting \(D\). Then \(Z'\) is open in each resulting \(T_i'\).

The map \(Z'\to T_1'\times_S T_2'\) is an immersion, since one projection is open and the other factor is separated. It is proper: \(Z'\to Z\subset T_1\times_S T_2\) is proper, and the product \(T_1'\times_S T_2'\to T_1\times_S T_2\) is separated, so the graph factorization proving properness cancellation applies. Thus this immersion is closed. Glue \(T_1'\) and \(T_2'\) along \(Z'\). On the four open pieces of its self-product over \(S\), the diagonal is either the closed diagonal of \(T_i'\) or the closed graph just proved. Hence the glued scheme is separated. Its two finite-type open pieces form a finite cover, so it is finite type. \(\square\)

**Lemma N.C.3 (valuative tests from a dense open suffice in this Noetherian setting).** Let \(M\to S\) be separated and finite type with \(S\) Noetherian. Let \(D\subset M\) be dense and open. If every valuation diagram whose generic map lands in \(D\) has an extension to \(M\), then \(M\to S\) is proper.

**Proof.** Apply the proved Noetherian Chow Theorem 4.1: there are a proper surjection \(q:M'\to M\), an immersion \(M'\to\mathbf P^N_S\), and an isomorphism over a dense open \(E\subset M\). Replace \(M'\) by the scheme-theoretic closure of \(q^{-1}E=E\) in it. The proper image is still all of \(M\), since it is closed and contains the dense \(E\). Thus \(E\) is schematically dense in \(M'\), and every generic point of \(M'\) lies in it and maps to a generic point of \(M\); the additional dense open \(D\) contains those points.

Let \(C\) be the scheme-theoretic closure of \(M'\) in \(\mathbf P^N_S\). If its boundary had a point \(c\notin M'\), choose an irreducible component through \(c\), give it its reduced structure, and let \(K\) be its function field. Its generic point lies in \(M'\), with its image in \(D\). The proved valuation-domination Theorem 2.1 gives a valuation ring \(R\subset K\) dominating the local domain at \(c\). Thus \(\operatorname{Spec}R\to C\) has that specified generic map and closed-point image \(c\). The hypothesis extends its generic map to \(M\). Properness of \(q\) then lifts that extension to \(M'\), since the generic map already lies in \(M'\). The two maps to the separated \(\mathbf P^N_S\) agree generically and hence agree on \(\operatorname{Spec}R\), whose structure ring injects into \(K\). The first sends the closed point to \(c\notin M'\), a contradiction.

Therefore the immersion \(M'\to\mathbf P^N_S\) has closed image, so is a closed immersion; \(M'\to S\) is proper. The earlier properness-surjection Corollary 2.2 makes \(M\to S\) universally closed, and its separatedness and finite type were assumed. It is proper. This proof uses all valuation rings and the proved general domination theorem, and needs no discrete-domination input. \(\square\)

### N.D. Combining two existing compactifications

**Theorem N.D.1.** Let \(X\to S\) be separated and finite type with \(S\) Noetherian. Suppose \(X=U_1\cup U_2\), the intersection \(D=U_1\cap U_2\) is dense in \(X\), and each \(U_i\) has a proper compactification over \(S\). Then \(X\) has a proper compactification over \(S\).

**Proof.** Choose compactifications \(U_i\subset P_i\), replacing \(P_i\) by the scheme-theoretic closure of \(U_i\). In \(P_i\times_S X\), take the graph closure of \(U_i\). Its projection to \(P_i\) is an isomorphism over \(U_i\). By Corollary N.B.2, modify \(P_i\) away from \(U_i\) so that this closure is an open \(V_i\subset P_i\). Its other projection
\[
\psi_i:V_i\longrightarrow X
\]
is proper: its graph is closed in \(P_i\times_S X\), and \(P_i/S\) is proper. It has \(\psi_i^{-1}(U_i)=U_i\) and is the identity there. The closed graph assertion, and schematic density of \(U_i\) in \(P_i\) and \(V_i\), are retained throughout the following modifications.

Let \(Z_i=X\setminus U_j\subset U_i\), where \(\{i,j\}=\{1,2\}\), and put
\[
F_{i,j}=\psi_i^{-1}(Z_j)\subset V_i.
\]
For each fixed \(i\), the sets \(F_{i,1}\) and \(F_{i,2}\) are disjoint and closed in \(V_i\). Apply Lemma N.A.2 to modify \(P_i\) away from \(V_i\) until their closures \(B_{i,1},B_{i,2}\subset P_i\) are disjoint. This remains true under further \(V_i\)-admissible modifications.

Set \(V_{12}=V_1\times_X V_2\), and let \(P_{12}\subset P_1\times_S P_2\) be its scheme-theoretic closure. Both projections \(p_i:P_{12}\to P_i\) are proper. Moreover \(p_i^{-1}(V_i)=V_{12}\): for instance \(V_{12}\to V_1\times_S P_2\) is the base change of the closed graph of \(\psi_2\), so is already closed on that open. The first projection is an isomorphism on a neighbourhood of \(F_{1,2}\), because \(\psi_2\) is an isomorphism over the open \(U_2\) containing \(Z_2\). Lemma N.C.1 modifies \(P_1\) away from \(V_1\) so that \(p_1\), after strict transform, is an isomorphism on a neighbourhood of \(B_{1,2}\). Replace \(P_1,P_{12}\) accordingly. Its scheme-theoretic closure description is retained by Lemma N.A.1(2).

We obtain
\[
P_{12}\cap(B_{1,2}\times_S B_{2,1})=\varnothing.
\tag{N.D.1}
\]
Indeed \(p_1^{-1}(B_{1,2})\to B_{1,2}\) is an isomorphism. The subset
\[
V_{12}\cap\psi^{-1}(Z_2),
\qquad \psi=\psi_1p_1=\psi_2p_2\text{ on }V_{12},
\]
maps isomorphically onto \(F_{1,2}\), which is dense in \(B_{1,2}\). Consequently it is dense in \(p_1^{-1}(B_{1,2})\). Its second image lies in \(F_{2,2}\), so the full second image lies in \(B_{2,2}\), disjoint from \(B_{2,1}\). This proves (N.D.1).

Define two schemes by open gluing:
\[
M_i=X\coprod_{U_i}(P_i\setminus B_{i,j}).
\tag{N.D.2}
\]
They are separated over \(S\). To prove this directly, the closure of the graph of \(U_i\to X\) in \(P_i\times_S X\) is the closed graph of \(\psi_i:V_i\to X\), since \(U_i\) is schematically dense in \(V_i\). Its intersection with \((P_i\setminus B_{i,j})\times_S X\) is exactly the graph of \(U_i\): a point in that intersection cannot map to \(Z_j\), because \(\psi_i^{-1}Z_j=F_{i,j}\subset B_{i,j}\). It therefore maps to \(U_i=X\setminus Z_j\), whose full inverse image is \(U_i\). The equality is scheme-theoretic, by restriction to that open. Thus the gluing graph is closed. The four-piece diagonal calculation from Lemma N.C.2 proves separatedness of (N.D.2). Each \(M_i\) is finite type, and contains \(X\) as an open.

For any valuation ring \(R\), with fraction field \(K\), and generic map \(\gamma:\operatorname{Spec}K\to D\) over \(S\), properness gives extensions \(g_i:\operatorname{Spec}R\to P_i\). The pair factors through \(P_{12}\): its generic map lies in \(V_{12}\), so every equation of that closed closure vanishes in \(K\), hence in \(R\subset K\). By (N.D.1) the two closed-point images cannot both lie in the removed sets \(B_{1,2}\) and \(B_{2,1}\). For some \(i\), the entire map \(g_i\) lands in \(P_i\setminus B_{i,j}\), since an open of a local spectrum containing its closed point is the whole spectrum. This gives an extension of \(\gamma\) to \(M_i\).

Apply Lemma N.C.2 to the two opens \(X\subset M_i\). It provides proper \(X\)-admissible modifications \(M_i'\to M_i\) which are open in one separated finite-type \(M\to S\). They identify the unchanged copy of \(X\). Every preceding extension to an \(M_i\) lifts to \(M_i'\) by properness, using the given generic map in \(D\subset X\). Hence every valuation diagram with generic point in \(D\) extends to \(M\).

The open \(D\) is dense in \(M\). Before modification it is dense in \(X\), and is dense in each \(P_i\), since \(U_i\) is dense there and \(D\) contains all its generic points; hence it is dense in both \(M_i\). Density is retained by their protected blowups, by Lemma N.A.1(1), and their open images cover \(M\). Lemma N.C.3 now proves \(M\to S\) proper. Thus \(X\subset M\to S\) is the required compactification. \(\square\)

### N.E. Nagata existence in the requested generality

**Theorem N.E.1.** Every separated finite-type morphism \(f:X\to S\) between Noetherian schemes factors as an open immersion \(X\hookrightarrow\overline X\) followed by a proper morphism \(\overline X\to S\).

**Proof.** The empty source has the empty compactification. Otherwise \(X\) has finitely many irreducible components. The finite affine-cover construction at the beginning of the proved Noetherian Chow Theorem 4.1 gives a cover \(X=\bigcup_{i=1}^n U_i\) in which every \(U_i\) contains every generic point of \(X\). Therefore their intersection is dense in \(X\). Here is the finite-coordinate construction for each affine \(U_i=\operatorname{Spec}B\), including a nonaffine base. Cover \(U_i\) by finitely many distinguished opens \(D_B(g_\alpha)\) whose images lie in affine base opens \(S_\alpha=\operatorname{Spec}A_\alpha\). Because the map is finite type, each \(B_{g_\alpha}\) has finitely many algebra generators over \(A_\alpha\). Express them as \(b/g_\alpha^m\). Collect their numerators and all \(g_\alpha\) as finitely many global functions on \(U_i\). They define an \(S\)-map to \(\mathbf A^N_S\). Let \(G\) be the union of the opens over \(S_\alpha\) where the coordinate corresponding to \(g_\alpha\) is invertible. The full inverse image of each such open is precisely \(D_B(g_\alpha)\), and the corresponding coordinate-ring map
\[
A_\alpha[t_1,\ldots,t_N]_{t_{g_\alpha}}
\longrightarrow B_{g_\alpha}
\]
is surjective by the selected generators. The map to \(G\) is therefore a closed immersion, since this property is local on the target. Hence \(U_i\to\mathbf A^N_S\to\mathbf P^N_S\) is an immersion. Its scheme-theoretic closure in \(\mathbf P^N_S\) is proper over \(S\) and contains the full original \(U_i\) as an open.

Inductively compactify \(U_1\cup\cdots\cup U_r\) by Theorem N.D.1. For the next step its intersection with \(U_{r+1}\) contains all generic points of \(X\), and is dense in that union. After \(n-1\) steps we have a compactification of \(X\). All constructions used coherent ideals and scheme-theoretic closures, and every modification protecting an open preserved its structure sheaf, including nilpotents. Thus the proof has retained the stated Noetherian, possibly nonreduced, relative generality. \(\square\)

This theorem supplies the existence input for lesson 16, Proposition 6.1, and for the successive compactifications in Proposition 6.2. It supplies precisely the requested hypothesis class; no projectivity assumption on \(X\to S\) has been added. Replacing any final compactification by the scheme-theoretic closure of \(X\) makes its open schematically dense, as required in the existing comparison proof.

### Construction sources and rights for Appendix N

The two-open assembly in Sections N.C–N.E follows the mathematical construction in the Stacks Project Authors, *More on Flatness*, “Nagata compactification”, [Section 38.33](https://stacks.math.columbia.edu/tag/0F3T), especially its improvement-near-a-closure, common-enlargement, and two-compactification arguments. The elementary admissible-blowup definitions and chart calculations are the Stacks Project Authors, *Divisors*, [Blowing up](https://stacks.math.columbia.edu/tag/01OF), [Strict transform](https://stacks.math.columbia.edu/tag/080C), and [Admissible blowups](https://stacks.math.columbia.edu/tag/080J). These adapted constructions retain GNU FDL 1.2 or later, with no invariant sections, no front-cover texts, and no back-cover texts, as specified in the [Stacks Project copying notice](https://github.com/stacks/stacks-project/blob/master/COPYING). The proofs are written above; the source links do not discharge their obligations.

Brian Conrad's freely author-posted [*Deligne's notes on Nagata compactifications*](https://math.stanford.edu/~conrad/papers/nagatafinal.pdf), Theorem 2.4, was consulted to identify the elementary rational-map route avoiding general flatification. No prose, diagram or extended excerpt from that author draft is reproduced. The conductor-ideal implementation in (N.B.1), the affine-hull proof in Lemma N.A.4, and the Chow proof of Lemma N.C.3 are written here to identify and close the otherwise hidden programme inputs. Mathematical assertions themselves are proved rather than accepted on the authority of that draft. No paid book, journal gateway, or inaccessible source is used as a proof provider.
