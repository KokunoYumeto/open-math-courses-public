# Poincaré duality for smooth varieties

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026; the construction of the trace in Section 2 was written by GPT-6 Astra (OpenAI) in ChatGPT and checked by Claude Opus 5.5 (Anthropic) in a separate session. The supported Kummer and divisor-normalization argument is by GPT-6 Astra (OpenAI) in Codex, Ultra, October 2026. Self-checked by the contributing AIs. Original text released under CC0. The constructibility-hypothesis check is by GPT-6 Astra (OpenAI), October 2026.

The curve theorem gives a perfect pairing with a trace in degree two. A smooth variety has local coordinates, so one expects one such shift and twist for every coordinate. The difficulty is that a strict localization is an inverse limit of neighbourhoods, and compact support runs in the direction of trace. We first make that direction and the uniform local argument precise. Global duality and purity then follow from adjunction. This also explains why purity is a statement about local cohomology sheaves, rather than vanishing of every higher global group with support.

## 1. Coefficients, scope and exact prerequisites

Let \(\Lambda=\mathbf Z/n\), with \(n\geq2\). Every scheme carrying these coefficients has \(n\) invertible. Put \(\Lambda(1)=\mu_n\); its tensor powers and inverse powers define \(\Lambda(a)\). They are invertible rank-one local systems. We retain the twists without choosing roots of unity. Complexes have cohomological grading, so \(H^r(A[s])=H^{r+s}(A)\).

In the absolute theorem, \(k\) is algebraically closed and \(X/k\) is separated, smooth, finite type, and purely of dimension \(N\). In the relative theorem, \(f:X\to S\) is separated and smooth of finite presentation, \(S\) is quasi-compact and quasi-separated, and the relative dimension is the constant \(d\). A locally constant constructible \(\Lambda\)-sheaf has finite module fibres. Those fibres need not be free, and \(n\) need not be prime.

We use the following precise earlier results. Lesson 7 proves geometric-stalk formulas and the finite-data continuity of sections, and states cohomological continuity on inverse limits with affine transition maps; that theorem is proved in the Stacks project, [Tag 09YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-colimit). Lesson 10, Theorem 6.2, computes the degree of the Kummer class on a curve. Lesson 11 proves that constructible sheaves form a Serre category, descend with their finite presentations and approximate every sheaf as a filtered colimit, and it constructs extension by zero along étale maps. Lesson 13 proves the proper base change theorem. Lesson 14, Sections 5 and 7–12, constructs \(Rf_!\), its composition and base-change maps, its arbitrary-complex projection formula, its preservation of sums and its relative amplitude \([0,2d]\) when fibres have dimension at most \(d\). Its Section 12 gives the [general constructibility reduction](cohomology-with-compact-support.md#proof-of-general-constructibility) and the [finiteness proof](cohomology-with-compact-support.md#general-finiteness-over-an-algebraically-closed-field), using the exact affine-line provider linked there. The corresponding Stacks statements are [Tag 0GL0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-theorem-constructible-shriek) and [Tag 0GLH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-finiteness-compactly-supported). We use constructibility for finite-presentation morphisms over a coherent base, and finite compact cohomology over an algebraically closed field. Lesson 15, Theorem 9.1, proves universal local acyclicity of smooth morphisms. Lesson 16 proves affine vanishing and derived Künneth. Lesson 17 proves full curve duality, coefficient self-injectivity, and trace compatibility for finite maps and open extension.

For the construction of a general right adjoint we use Brown representability for the derived category of a Grothendieck abelian category, a categorical theorem proved in the Stacks project, [Tags 0F5X–0F5Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-proposition-brown). Section 8 applies it explicitly; neither a higher-dimensional duality theorem nor a purity theorem is included among the premises. Section 2 constructs the higher-dimensional trace from the curve trace. For \(n=1\), every coefficient object in this lesson is zero.

## 2. The trace and its derived comparison

This section constructs the top-degree trace of a smooth morphism and proves its compatibilities. It uses only the lessons listed in Section 1 and standard algebra; nothing from Sections 3–16 of this lesson enters.

**Theorem 2.1 (trace for smooth morphisms).** Let \(f:X\to S\) be separated, smooth and of finite presentation, of constant relative dimension \(d\), with \(S\) quasi-compact and quasi-separated. There is a canonical morphism

\[
\operatorname{Tr}_f:R^{2d}f_!\Lambda(d)\longrightarrow\Lambda_S
\tag{2.1}
\]

with the following properties.

**(T1) Base change.** For every morphism \(b:S'\to S\), the compact-support base-change isomorphism \(b^{-1}R^{2d}f_!\Lambda(d)\simeq R^{2d}f'_!\Lambda(d)\) identifies \(b^{-1}\operatorname{Tr}_f\) with \(\operatorname{Tr}_{f'}\).

**(T2) Étale localization.** For every separated étale \(j:U\to X\), let \(\varepsilon_j:j_!j^{-1}\Lambda(d)\to\Lambda(d)\) be the counit. Under the identification \(R^{2d}(fj)_!\Lambda(d)=R^{2d}f_!j_!\Lambda(d)\),

\[
\operatorname{Tr}_{fj}=\operatorname{Tr}_f\circ R^{2d}f_!(\varepsilon_j).
\]

**(T3) Composition.** If \(g:Y\to X\) is separated, smooth, of finite presentation and of constant relative dimension \(e\), then

\[
\operatorname{Tr}_{fg}=\operatorname{Tr}_f\circ R^{2d}f_!\bigl(\operatorname{Tr}_g(d)\bigr)\circ c_{f,g},
\]

where \(c_{f,g}:R^{2(d+e)}(fg)_!\Lambda(d+e)\xrightarrow{\sim}R^{2d}f_!\bigl((R^{2e}g_!\Lambda(e))(d)\bigr)\) is the top-degree composition isomorphism (2.5) below, followed by the projection formula for the twist.

**(T4) Normalization.** If \(d=0\), then \(f\) is étale and \(\operatorname{Tr}_f\) is the counit \(f_!\Lambda\to\Lambda\), given by summation. If \(d=1\) and \(S=\operatorname{Spec}k\) with \(k\) algebraically closed, \(\operatorname{Tr}_f\) is the compact-support trace of Lesson 17, Section 2. In particular, on a smooth projective curve \(C\), \(\operatorname{Tr}_C\bigl(c_1(\mathcal O_C(x))\bigr)=1\) for every closed point \(x\).

**(T5) Nondegeneracy.** If every geometric fibre of \(f\) is nonempty and connected, (2.1) is an isomorphism. For every separated smooth finite-type scheme \(X\) of pure dimension \(d\) over an algebraically closed field, possibly disconnected or empty, the traces of the connected components give a canonical isomorphism \(H^{2d}_c(X,\Lambda(d))\xrightarrow{\sim}\Lambda^{\pi_0(X)}\), under which \(\operatorname{Tr}_X\) is summation.

**(U) Uniqueness.** A family of morphisms (2.1) satisfying (T1)–(T4) is unique.

In (T1) the base \(S'\) is arbitrary, and in (T2) the étale map \(j\) need not be quasi-compact. Step 12 below gives the notation its meaning in these cases: over a base that is not quasi-compact and quasi-separated, the top direct image and its trace are defined locally on the base, and for a separated étale \(j\) that is not quasi-compact, \(R(fj)_!\) means \(Rf_!j_!\). For example, \(\coprod_{m\geq0}\operatorname{Spec}k\to\operatorname{Spec}k\) is separated and étale but not of finite presentation; its counit is the sum \(\bigoplus_{m\geq0}\Lambda\to\Lambda\). No finiteness hypothesis is added to \(j\) or to \(b\).

The bound from Lesson 14 gives \(Rf_!\Lambda(d)[2d]\in D^{\leq0}(S,\Lambda)\). Its canonical map to degree-zero cohomology followed by (2.1) gives a derived trace

\[
T_f:Rf_!\Lambda(d)[2d]\longrightarrow\Lambda_S.
\tag{2.2}
\]

For an object \(K\in D^{\leq0}\) and a sheaf \(B\), the truncation triangle and the vanishing of maps from \(D^{\leq-1}\) to \(D^{\geq0}\) give \(\operatorname{Hom}_D(K,B)=\operatorname{Hom}(H^0K,B)\). Thus (T1)–(T3) give the corresponding compatibilities of (2.2). The same notation will denote its extension to arbitrary coefficients pulled back from the base. The projection formula of Lesson 14 defines

\[
Rf_!\bigl(f^*A(d)[2d]\bigr)
\simeq A\otimes^L Rf_!\Lambda(d)[2d]
\xrightarrow{1\otimes T_f}A.
\tag{2.3}
\]

This construction works for arbitrary complexes \(A\). Derived tensors of bounded complexes over \(\mathbf Z/n\) need not be bounded; the arbitrary-complex projection formula is therefore necessary. Compatibility of (2.3) with composition follows by applying the composition and projection maps and then the two traces in order. Their composite is (2.1) in the top degree, and the canonical truncation to that degree makes it (2.2). Base change follows in the same way. All orientation shifts are even, so their exchange contributes no sign.

The rest of this section proves Theorem 2.1.

### Step 1. Signs and top-degree composition

Complexes have cohomological grading, \(K[r]^i=K^{i+r}\) and \(d_{K[r]}=(-1)^rd_K\). The tensor differential and symmetry are

\[
d(x\otimes y)=dx\otimes y+(-1)^{|x|}x\otimes dy,
\qquad
x\otimes y\longmapsto(-1)^{|x||y|}y\otimes x.
\tag{2.4}
\]

For \(x\in K^i\), the shift identification \(K[r]\otimes L[s]\to(K\otimes L)[r+s]\) sends \(x\otimes y\) to \((-1)^{si}x\otimes y\); substitution in (2.4) shows that this is a chain map. Twists are sheaves in degree zero, and their tensor identifications introduce no sign. Every orientation shift below is even, so exchanging two orientation factors of degrees \(2a\) and \(2b\) contributes \((-1)^{4ab}=+1\).

We use the composition, base-change, projection and amplitude results of Lesson 14, Theorems 8.1, 9.1, 10.3 and 12.1, with their canonical comparison maps. Suppose that \(h:Z\to T\) and \(q:T\to B\) have fibre dimensions at most \(b\) and \(a\), respectively. For a sheaf \(F\), the canonical truncation triangle is

\[
\tau_{\leq 2b-1}Rh_!F\longrightarrow Rh_!F\longrightarrow R^{2b}h_!F[-2b]\longrightarrow.
\]

After applying \(Rq_!\), the first term has cohomology only in degrees at most \(2a+2b-1\). The resulting map is therefore a canonical isomorphism

\[
c_{q,h,F}:R^{2(a+b)}(qh)_!F\xrightarrow{\sim}R^{2a}q_!R^{2b}h_!F.
\tag{2.5}
\]

It is natural in \(F\) and commutes with base change: inverse image is exact, hence commutes with good truncation, and the compact-support comparison maps commute with composition.

Here is the associativity check. For three direct images, first apply the truncation map of the innermost complex. Applying the middle direct image gives a morphism between two complexes with the same upper cohomological bound. The square formed by this morphism and the canonical maps to their top cohomology objects commutes by naturality of truncation. Apply the outer direct image and take the highest possible degree. The two sides of the square are the two iterated maps (2.5), so they are equal. The same argument allows coefficient morphisms to be inserted at any stage.

Given \(t_q:R^{2a}q_!\Lambda(a)\to\Lambda\) and \(t_h:R^{2b}h_!\Lambda(b)\to\Lambda\), put

\[
t_q\star t_h:=t_q\circ R^{2a}q_!\bigl(t_h(a)\bigr)\circ c_{q,h}.
\tag{2.6}
\]

The naturality square above, with the coefficient maps inserted, proves that \(\star\) is associative. The twists are moved by the projection formula without a sign. The comparison \(c_{f,g}\) of (T3) is (2.5) followed by these twist identifications.

### Step 2. Smooth coordinates

A smooth morphism of relative dimension \(d\) has, locally on its source, an étale morphism to \(\mathbf A^d_S\). We recall the algebra behind this assertion and the coordinate-change criterion used below.

Write a smooth finitely presented \(A\)-algebra as \(B=P/I\), with \(P=A[t_1,\ldots,t_m]\) and \(I\) finitely generated. The infinitesimal lifting property gives an \(A\)-algebra section \(s:B\to P/I^2\) of the quotient map. The difference between \(P\to P/I^2\) and its composite through \(s\) is an \(A\)-derivation with values in \(I/I^2\), whose restriction to \(I/I^2\) is the identity. Thus the conormal sequence

\[
0\longrightarrow I/I^2\longrightarrow B^m\longrightarrow\Omega_{B/A}\longrightarrow0
\]

is split exact, and locally its terms are finite free. Choose \(F_1,\ldots,F_r\in I\) whose images form a basis of \(I/I^2\) at the point under consideration. Their differentials are independent there, so some \(r\)-row Jacobian minor is invertible. These \(F_i\) generate \(I\) after a further localization: in the corresponding local ring of \(P\), the finite module \(I/(F_1,\ldots,F_r)\) equals its product with \(I\), and Nakayama's lemma makes it zero. After reordering the variables,

\[
B=\bigl(A[t_1,\ldots,t_m]/(F_1,\ldots,F_r)\bigr)_h,
\qquad
\det\Bigl(\frac{\partial F_i}{\partial t_j}\Bigr)_{1\leq i,j\leq r}\in B^\times.
\tag{2.7}
\]

The map from \(A[t_{r+1},\ldots,t_m]\) to this algebra is étale. To check the infinitesimal criterion, lift the \(t_i\) across a square-zero ideal; the errors in the equations \(F_i\) are corrected uniquely by solving the linear system with the invertible Jacobian matrix. Finite presentation is explicit. On a geometric fibre, at a closed point, the independent Jacobian rows make the \(F_i\) part of a regular system of parameters of the ambient polynomial local ring, so the quotient has dimension \(m-r\). Hence \(m-r=d\).

These presentations are flat. In the Noetherian case, use the local criterion of flatness in its fibrewise regular-sequence form: if a Noetherian local algebra is flat over its Noetherian local base, and elements of its maximal ideal form a regular sequence in the closed fibre, then their quotient is flat over the base. Apply this to the local polynomial algebra and the \(F_i\); the independent Jacobian rows give the required regular sequence after an algebraic closure of the residue field, as in the preceding paragraph, and faithful flatness of that field extension detects regular sequences. For arbitrary \(A\), the equations, the localization and a polynomial witness for the inverse of the Jacobian minor use only finitely many coefficients. They are defined over a finitely generated \(\mathbf Z\)-subalgebra \(A_0\subset A\). The resulting presentation over \(A_0\) has the same invertible minor and is flat by the Noetherian case; its base change is the original algebra, and flatness is preserved by base change.

The same calculation gives the following inverse-function criterion. If \(u_1,\ldots,u_d\) are functions on a smooth \(S\)-scheme \(X\) whose differentials form a basis of \(\Omega_{X/S}\) at a point, then \((u_1,\ldots,u_d):X\to\mathbf A^d_S\) is étale on a neighbourhood of that point. Indeed, in (2.7) lift the \(u_i\) to elements \(G_i\) of the localized polynomial algebra. As an algebra over \(A[z_1,\ldots,z_d]\), use the equations \(F_i\) and \(G_i-z_i\); their square Jacobian is invertible exactly when the indicated differentials form a basis, and the same square-zero calculation applies.

Over an algebraically closed field \(k\), a smooth finite-type \(k\)-scheme is regular: at a closed point the independent equations in (2.7) are part of a regular system of parameters of the local polynomial ring, and their quotient is regular; every prime lies in a maximal ideal, and localizations of regular local rings are regular. Regular local rings are domains. Consequently the finitely many irreducible components of a regular Noetherian scheme are pairwise disjoint, open and closed. In particular a connected smooth finite-type \(k\)-scheme is integral, and so is every connected affine étale scheme over it.

### Step 3. Descent along étale covers and removal of smaller-dimensional subsets

Fix \(f:X\to S\) with fibre dimensions at most \(d\), and put \(Q_f(F)=R^{2d}f_!F\). The amplitude bound makes \(Q_f\) right exact. The construction of compact supports and Lesson 14, Proposition 5.2, show that \(Rf_!\), hence \(Q_f\), preserves arbitrary direct sums. Therefore \(Q_f\) preserves all colimits, since a colimit in an abelian category is the cokernel of two relation maps between coproducts.

Let \(u_i:U_i\to X\) be a **jointly surjective** family of separated étale morphisms, initially of finite presentation. Set \(U_{ij}=U_i\times_XU_j\), with \(u_{ij}:U_{ij}\to X\). For every sheaf \(F\) there is an exact sequence

\[
\bigoplus_{i,j}u_{ij!}u_{ij}^{-1}F
\xrightarrow{\delta}
\bigoplus_iu_{i!}u_i^{-1}F
\xrightarrow{\varepsilon}F\longrightarrow0.
\tag{2.8}
\]

The map \(\delta\) is the first projection counit minus the second, and \(\varepsilon\) is the sum of the counits. At a geometric point \(\bar x\), the middle term is a direct sum of copies of \(F_{\bar x}\) indexed by the lifts of \(\bar x\). This index set is nonempty because the family is jointly surjective. The relations are exactly \(e_ua-e_va\), and their quotient is \(F_{\bar x}\), by summation. This proves (2.8). Applying the right exact functor \(Q_f\) gives

\[
\bigoplus_{i,j}R^{2d}(fu_{ij})_!u_{ij}^{-1}F
\longrightarrow
\bigoplus_iR^{2d}(fu_i)_!u_i^{-1}F
\longrightarrow R^{2d}f_!F\longrightarrow0.
\tag{2.9}
\]

Consequently a map out of \(R^{2d}f_!F\) is specified by compatible maps on an étale covering of the source. Geometric stalks detect the equalities and isomorphisms used here: if a section has zero germ at every geometric point, then at each point it vanishes on a pointed étale neighbourhood; these neighbourhoods cover, so the section is zero. Apply this to kernels, cokernels and differences of morphisms.

There is a second consequence of the amplitude bound. If \(j:V\hookrightarrow X\) has closed complement \(i:Z\hookrightarrow X\), and the fibres of \(Z\to S\) have dimension at most \(d-1\), then excision gives an isomorphism

\[
R^{2d}(fj)_!j^{-1}F\xrightarrow{\sim}R^{2d}f_!F.
\tag{2.10}
\]

Indeed, the terms next to this arrow in the excision sequence are the direct images of \(i^{-1}F\) in degrees \(2d-1\) and \(2d\), and both vanish. In particular, over a field, removing a proper closed subset of an integral \(d\)-dimensional scheme does not change its top compactly supported cohomology, for any sheaf.

### Step 4. Dimension zero

For a separated étale \(u:V\to W\), define

\[
\operatorname{Tr}_u=\varepsilon_u:u_!\Lambda_V\longrightarrow\Lambda_W.
\tag{2.11}
\]

Exactness, adjunction and base change for \(u_!\) are Lesson 11, Propositions 1.1 and 1.2. On a geometric stalk, (2.11) is \(\bigoplus_{v\in V_{\bar w}}\Lambda\to\Lambda\), \((a_v)_v\mapsto\sum_va_v\); the sums have finite support, and base change preserves this description. For composable étale maps, summing over the fibres successively is summing over the fibres of the composite, so

\[
\varepsilon_{uv}=\varepsilon_u\circ u_!(\varepsilon_v).
\tag{2.12}
\]

The same argument works with any coefficient sheaf pulled back from \(W\), including twists. This proves every dimension-zero compatibility used below.

### Step 5. The absolute curve trace under étale maps

Let \(k\) be algebraically closed, and write \(t_C\) for the trace of Lesson 17, Section 2, on a separated smooth finite-type curve \(C/k\). We need its compatibility with every separated étale map \(v:C'\to C\) of finite type:

\[
t_{C'}=t_C\circ H^2_c\bigl(\varepsilon_v(1)\bigr).
\tag{2.13}
\]

For an open immersion this is the definition of \(t_C\) through a smooth projective completion. For a finite étale map it is Proposition 2.1 of Lesson 17; its norm map is precisely the summation counit.

Here is the reduction of a general \(v\) to these cases. By finite disjoint unions, consider one connected component of \(C'\), whose image lies in one connected component of \(C\); both are integral. Choose a nonempty affine open \(\operatorname{Spec}A\) of the target and a nonempty affine open \(\operatorname{Spec}B\) of its inverse image. The extension \(\operatorname{Frac}A\subset\operatorname{Frac}B\) is finite and separable: the map is étale, both curves have dimension one, and it is dominant. Choose finitely many \(A\)-algebra generators of \(B\). Their monic equations over \(\operatorname{Frac}A\) have finitely many denominators; after inverting their product \(s\neq0\) in \(A\), all generators are integral. Hence \(B_s\) is finite over \(A_s\), and the induced morphism is finite étale. Both resulting opens are dense, and their complements in the original curves have dimension zero, so the extension maps on \(H^2_c(-,\mu_n)\) are isomorphisms by (2.10). Apply the finite case on these opens. Transitivity (2.12) makes its two extensions the two sides of (2.13), and the source extension is an isomorphism, proving (2.13). Summing over components completes the proof.

The sign is fixed by the Kummer connecting morphism and the convention \(t_C\bigl(c_1(\mathcal O_C(x))\bigr)=+1\). No degree factor enters (2.13): a finite étale transfer preserves the degree of a point divisor, whereas pullback multiplies the total degree.

### Step 6. Relative projective lines, affine lines and smooth curves

Let \(p:\mathbf P^1_S\to S\). The Kummer class of \(\mathcal O(1)\) defines a morphism

\[
\alpha_S:\Lambda_S\longrightarrow R^2p_*\mu_n,
\qquad 1\longmapsto c_1(\mathcal O(1)).
\tag{2.14}
\]

It is defined on every étale \(T\to S\) by the Kummer class of \(\mathcal O(1)\) on \(\mathbf P^1_T\), followed by sheafification. The Kummer sequence is exact because an invertible function acquires an \(n\)-th root on the étale cover defined by \(z^n-u\), whose derivative is invertible there. Thus (2.14) is natural under arbitrary base change. The proper base change theorem of Lesson 13 identifies the stalk of (2.14) with the degree-one Kummer class on a projective line over an algebraically closed field. Lesson 10, Theorem 6.2, and the normalization of the curve trace show that this stalk map is an isomorphism. Consequently \(\alpha_S\) is an isomorphism; define \(t_p=\alpha_S^{-1}\).

Let \(a:\mathbf A^1_S\to S\), with its open immersion into \(\mathbf P^1_S\). The complement is the section at infinity, of relative dimension zero. Excision gives a base-change-compatible isomorphism \(R^2a_!\mu_n\xrightarrow{\sim}R^2p_*\mu_n\). Its composite with \(t_p\) is denoted \(t_{a,S}\); it induces the absolute curve trace on each geometric fibre. Furthermore

\[
Ra_!\Lambda(1)\simeq\Lambda_S[-2],
\tag{2.15}
\]

with top map \(t_{a,S}\): the geometric fibre formula and Lesson 14, Example 13.1, give zero cohomology in all other degrees, and good truncation then gives (2.15).

Now let \(h:C\to S\) be any separated smooth curve of finite presentation. Choose a finite cover by quasi-compact open subsets \(C_i\) with étale coordinate maps \(u_i:C_i\to\mathbf A^1_S\). Define on each piece

\[
t_i=t_{a,S}\star\varepsilon_{u_i}.
\tag{2.16}
\]

After pullback to a geometric point of \(S\), (2.13) says that (2.16) is the absolute trace of \((C_i)_{\bar s}\). On a double overlap the two induced maps therefore agree on all geometric stalks, and the sequence (2.9) glues the \(t_i\) to

\[
\operatorname{Tr}_h:R^2h_!\Lambda(1)\longrightarrow\Lambda_S.
\tag{2.17}
\]

Its stalk at every geometric point is the absolute curve trace: the covering epimorphism on that fibre and (2.13) characterize the stalk map. This characterization proves independence of the cover, arbitrary base change and étale localization for relative curves; for the last assertion, the two maps in (T2) become (2.13) on every geometric fibre.

### Step 7. Affine spaces and permutations of coordinates

Let \(p_{r,S}:\mathbf A^r_S\to S\). Set \(t_{0,S}=\operatorname{id}\). For \(r>0\), factor \(p_{r,S}\) as the projection deleting the last coordinate followed by \(p_{r-1,S}\), and define \(t_{r,S}\) as the \(\star\)-composite of the corresponding traces. By (2.15), composition and the projection formula give

\[
Rp_{r,S!}\Lambda(r)\simeq\Lambda_S[-2r],
\qquad
t_{r,S}:R^{2r}p_{r,S!}\Lambda(r)\xrightarrow{\sim}\Lambda_S.
\tag{2.18}
\]

These identifications commute with base change, and associativity (Step 1) shows that grouping consecutive coordinates into blocks does not change the result.

We check the symmetry needed for nonconsecutive blocks. Over an algebraically closed field, let \(\eta\in H^2_c(\mathbf A^1,\Lambda(1))\) with \(t_{1,k}(\eta)=1\). The compactly supported exterior product gives

\[
\eta^{\boxtimes r}\in H^{2r}_c(\mathbf A^r,\Lambda(r)),
\qquad
t_{r,k}(\eta^{\boxtimes r})=1.
\tag{2.19}
\]

The product isomorphism comes from the available formalism. For structural maps \(a:V\to\operatorname{Spec}k\) and \(b:W\to\operatorname{Spec}k\), first push along \(V\times W\to V\); base change and the projection formula identify this pushforward of \(F\boxtimes G\) with \(F\otimes^La^*Rb_!G\). Applying \(Ra_!\) and the projection formula gives

\[
R\Gamma_c(V\times W,F\boxtimes G)\simeq R\Gamma_c(V,F)\otimes^LR\Gamma_c(W,G).
\tag{2.20}
\]

Its iterated form for affine lines identifies (2.18) with the tensor product of copies of (2.15), proving (2.19). The map in (2.20) is the external cup product, not merely an abstract isomorphism: after compactifying the factors, it is induced by the tensor of the two adjunction counits and by the tensor identification of the two extensions by zero, which is checked on stalks (it is the tensor of the coefficient stalks when both coordinates lie in the opens, and zero otherwise). Interchanging the factors interchanges the two counits and applies the symmetry (2.4). Thus the comparison intertwines a geometric permutation of factors with the graded tensor permutation.

An adjacent transposition acts on (2.19) by exchanging two factors of degree two, with sign \((-1)^4=+1\) by (2.4). It therefore fixes the generator (2.19) and preserves \(t_{r,k}\). Adjacent transpositions generate the symmetric group, and checking on geometric stalks proves that \(t_{r,S}\) is invariant under every permutation of coordinates over every \(S\).

### Step 8. A chain of one-coordinate changes

Let \(k\) be algebraically closed and let \(u,v:V\to\mathbf A^d_k\) be étale morphisms. For every closed point \(x\in V\) there are an open neighbourhood \(W\) and a finite sequence of étale maps

\[
u|_W=w_0,\ w_1,\ \ldots,\ w_N=v|_W
\tag{2.21}
\]

in which consecutive maps differ in only one coordinate function.

For \(d=0\) there is nothing to prove. Otherwise the differentials \(du_i(x)\) and \(dv_i(x)\) are bases of the same \(d\)-dimensional cotangent space. Let \(M\in\mathrm{GL}_d(k)\) carry the first basis to the second. Gaussian elimination writes \(M\) as a product of elementary row additions and nonzero row scalings; row swaps can be avoided, since on two rows the changes

\[
(a,b)\mapsto(a+b,b)\mapsto(a+b,-a)\mapsto(b,-a)\mapsto(b,a)
\]

perform a swap while changing one row at a time. Apply these row operations to the functions \(u_i\). Each intermediate tuple has a differential basis at \(x\). The final tuple \(z\) has \(dz_i(x)=dv_i(x)\); replace \(z_1\) by \(v_1\), then \(z_2\) by \(v_2\), and so on, and these tuples still have differential bases at \(x\). By the inverse-function criterion of Step 2, each tuple is étale near \(x\). Intersecting the finitely many neighbourhoods gives (2.21).

These neighbourhoods cover \(V\): a nonempty closed complement would have a closed \(k\)-point by the Nullstellensatz. Since \(V\) is of finite type, finitely many of them suffice.

### Step 9. Independence of coordinates and the construction in all dimensions

Suppose \(f:X\to S\) has an étale coordinate map \(u:X\to\mathbf A^d_S\), so that \(f=p_{d,S}u\). Define the candidate

\[
t(f,u)=t_{d,S}\star\varepsilon_u.
\tag{2.22}
\]

It commutes with base change. For a separated étale \(v:V\to X\) of finite presentation, (2.12) and the naturality of (2.5) give

\[
t(f,u)\circ R^{2d}f_!\bigl(\varepsilon_v(d)\bigr)=t(fv,uv).
\tag{2.23}
\]

We prove that (2.22) does not depend on \(u\). Equality can be checked after pullback to every geometric point of \(S\), so take \(S=\operatorname{Spec}k\) with \(k\) algebraically closed. By (2.9), (2.23) and Step 8, it suffices to compare two coordinate maps that differ in one coordinate. By the permutation invariance of Step 7, put that coordinate last. The common first \(d-1\) coordinates give \(h:X\to B=\mathbf A^{d-1}_k\), a smooth relative curve, and both maps are étale morphisms over \(B\) into \(\mathbf A^1_B\). The relative-curve localization property of Step 6 gives

\[
t_{1,B}\star\varepsilon_u=\operatorname{Tr}_h=t_{1,B}\star\varepsilon_v.
\]

Compose with \(t_{d-1,k}\) and use the associativity of \(\star\); the result is \(t(f,u)=t(f,v)\). For \(d=1\) this is already the relative-curve construction, and for \(d=0\) it is (2.11).

For general \(f\), choose a finite cover by quasi-compact coordinate opens \(j_i:X_i\hookrightarrow X\) and use (2.22) on each \(X_i\). On a double overlap, (2.23) and the independence of coordinates identify the two induced maps. The sequence (2.9) with \(F=\Lambda(d)\) gives a unique morphism

\[
\operatorname{Tr}_f:R^{2d}f_!\Lambda(d)\longrightarrow\Lambda_S,
\tag{2.24}
\]

and comparison on a common refinement proves independence of the cover. Pulling the covering epimorphism (2.9) back to another quasi-compact quasi-separated base gives the epimorphism for the pulled-back cover; each candidate (2.22) commutes with base change, hence so does (2.24). This proves (T1) in this scope.

For a separated étale \(j:U\to X\) of finite presentation, cover \(U\) by quasi-compact coordinate opens whose maps to \(X\) factor through coordinate opens of \(X\). On each piece the formula of (T2) is (2.23), and the covering epimorphism proves it globally. This proves (T2) for \(j\) of finite presentation. The construction agrees with Steps 4 and 6, which proves (T4).

### Step 10. Composition

We first check an interchange. Let \(u:X\to A\) be separated étale of finite presentation, and consider the cartesian square

\[
\begin{array}{ccc}
E=\mathbf A^e_X&\xrightarrow{\;u'\;}&\mathbf A^e_A=E_A\\
{\scriptstyle q}\downarrow\ &&\ \downarrow{\scriptstyle r}\\
X&\xrightarrow{\;u\;}&A.
\end{array}
\tag{2.25}
\]

Composition of compact supports and exactness of the two étale direct images give \(u_!R^{2e}q_!\Lambda(e)\simeq R^{2e}r_!u'_!\Lambda(e)\). Under this identification,

\[
\varepsilon_u\circ u_!(t_{e,X})=t_{e,A}\circ R^{2e}r_!\bigl(\varepsilon_{u'}(e)\bigr).
\tag{2.26}
\]

Indeed, at a geometric point \(\bar a\) of \(A\), both sides have source \(\bigoplus_{x\in X_{\bar a}}H^{2e}_c(\mathbf A^e_{\bar a},\Lambda(e))\), and both send \((z_x)_x\) to \(\sum_xt_{e,\bar a}(z_x)\). The identification of this source follows from the fibre formula, composition and the étale stalk formula, so it is the stalk of the canonical comparison above. Thus (2.26) holds as an identity of sheaf maps, and tensoring with a further twist preserves it.

Now let \(f:X\to S\) and \(g:Y\to X\) be as in (T3). The equality in (T3) can be checked after the covering epimorphism (2.9) for a coordinate cover of \(Y\). Choose one such piece lying above a coordinate open of \(X\), and write the coordinate maps as \(u:X\to A=\mathbf A^d_S\) and \(v:Y\to E=\mathbf A^e_X\), where \(X\) and \(Y\) now denote these pieces. Let \(p:A\to S\) and use (2.25). The composite chart \(w=u'v:Y\to E_A=\mathbf A^{d+e}_S\) is étale. The definitions give

\[
\begin{aligned}
\operatorname{Tr}_{fg}&=(t_{d,S}\star t_{e,A})\star\varepsilon_{u'}\star\varepsilon_v,\\
\operatorname{Tr}_f\star\operatorname{Tr}_g&=t_{d,S}\star\varepsilon_u\star t_{e,X}\star\varepsilon_v.
\end{aligned}
\tag{2.27}
\]

The two expressions are equal by (2.26) and the associativity of \(\star\).

To pass from these pieces to the original maps, let \(j:X_0\hookrightarrow X\) be a coordinate open and \(Y_0=Y\times_XX_0\). Base change identifies the restriction of \(\operatorname{Tr}_g\) with \(\operatorname{Tr}_{g_0}\). For a coordinate open \(V\subset Y_0\), (T2) identifies its transfer followed by \(\operatorname{Tr}_{g_0}\) with \(\operatorname{Tr}_{g_0|_V}\), and (T2) for \(j\) identifies the corresponding outer counit followed by \(\operatorname{Tr}_f\) with \(\operatorname{Tr}_{fj}\). The naturality of (2.5) makes these exactly the restriction of the right side of (T3) to the \(V\)-summand; the same assertion for its left side is (T2) for \(fg\). Hence (2.27) gives equality on every summand, and (2.9) gives it globally. The comparison used is precisely \(c_{f,g}\), by Step 1. All factors exchanged in (2.27) have even orientation degree and all counits have degree zero, so the sign in (T3) is \(+1\), with no factor depending on \(d\) or \(e\). This proves (T3).

### Step 11. Uniqueness

Let another family satisfy (T1)–(T4). Its relative-curve trace is determined on every geometric fibre by (T1) and the dimension-one clause of (T4), so geometric stalks force it to be (2.17). By (T3), its trace on \(\mathbf A^d_S\to S\) is the iterated composite of the relative affine-line traces, hence equals \(t_{d,S}\). On a coordinate chart \(f=p_{d,S}u\), apply (T3) to the étale morphism \(u\); its dimension-zero trace is forced by (T4), so its trace on the chart is (2.22). Finally (T2) specifies its restriction to every summand of the coordinate cover in (2.9). Those summands map epimorphically onto \(R^{2d}f_!\Lambda(d)\), so the family is (2.24). No nondegeneracy assertion is used.

### Step 12. Arbitrary bases and non-quasi-compact étale maps

First allow an arbitrary base \(S'\). On each affine open \(T\subset S'\), a separated smooth finite-presentation \(X'\to S'\) restricts to a morphism in the scope already treated, whose top compact-support sheaf and trace are constructed. On intersections, their restrictions agree; this can be checked on affine opens of the intersections using the base-change compatibility already proved, and the resulting cocycle identities are the composition identities of the canonical base-change maps. Gluing of sheaves and of sheaf morphisms therefore defines the top direct image and the trace over \(S'\), and checking on its affine opens proves (T1) for every \(S'\to S\).

Next let \(j:U\to X\) be any separated étale morphism. The exact functor \(j_!\) exists by Lesson 11, Proposition 1.1. Cover \(U\) by quasi-compact open subsets \(V_i\). The composite \(U\to S\) is separated, and \(S\) is quasi-separated, so \(U\) is quasi-separated and the overlaps \(V_i\cap V_j\) are quasi-compact. A morphism from a quasi-compact scheme to a quasi-separated scheme is quasi-compact: choose a finite affine cover of the source whose members map into affine opens of the target; intersect such an affine open with any other affine open of the target; the intersection is quasi-compact, and its inverse image in the corresponding affine piece of the source is quasi-compact because a morphism of affine schemes is affine. Consequently these opens and overlaps are quasi-compact and quasi-separated over \(S\), locally of finite presentation, hence of finite presentation over \(S\); they are separated and smooth, and their traces are already defined.

Apply the sheaf coequalizer (2.8) for this possibly infinite open cover, then the exact functor \(j_!\), and then the right exact, coproduct-preserving functor \(R^{2d}f_!\). It follows that \(R^{2d}f_!j_!\Lambda_U(d)\) is the cokernel of the overlap relations between the top direct images of the \(V_i\). Their traces agree on overlaps by the finite-presentation case of (T2), and so define a unique trace on this cokernel; a common refinement proves independence of the cover. Its restriction to each \(V_i\)-summand equals the restriction of \(\operatorname{Tr}_f\circ R^{2d}f_!\bigl(\varepsilon_j(d)\bigr)\), by the case already proved, and the covering epimorphism proves equality. Thus (T2) holds for every separated étale \(j\). The construction commutes with arbitrary base change: inverse image preserves coproducts and cokernels, and \(j_!\) and the finite-presentation compact-support comparisons commute with base change. This gives the meaning of the notation described after Theorem 2.1.

### Step 13. Constant targets on dense opens and generic fibres

Throughout this step \(k\) is algebraically closed and schemes are smooth of finite type over \(k\). If \(T\) is connected and \(j:V\hookrightarrow T\) is a nonempty open immersion, then

\[
\Lambda_T\xrightarrow{\sim}j_*\Lambda_V.
\tag{2.28}
\]

To prove this on an étale basis, take a connected affine étale \(W\to T\). By Step 2, \(T\) and \(W\) are integral. The map \(W\to T\) is dominant: on a nonempty affine piece over an affine open of \(T\), its ring map is a nonzero flat map from a domain, hence injective. Thus \(W\times_TV\) is nonempty and integral, both sides of (2.28) have sections \(\Lambda\) on \(W\), and the map is the identity. Disconnected objects of the basis are finite disjoint unions of connected ones. Here we have used that the sections of a finite constant étale sheaf on a scheme are its locally constant functions: the constant sheaf on a finite set is represented by the disjoint union of copies of the scheme indexed by that set, and a section is a clopen partition indexed by it. By adjunction, (2.28) gives, for every sheaf \(F\),

\[
\operatorname{Hom}_T(F,\Lambda_T)\xrightarrow{\sim}\operatorname{Hom}_V(F|_V,\Lambda_V).
\tag{2.29}
\]

There is no constructibility condition here.

We need a generic-fibre version. Let \(B=\mathbf A^m_k\), let \(K=k(B)\), and let \(h:U\to B\) be a nonempty smooth morphism with \(U\) connected. For \(\iota:U_K\to U\) and \(\eta:\operatorname{Spec}K\to B\),

\[
\Lambda_U\xrightarrow{\sim}\iota_*\Lambda_{U_K},
\qquad
\Lambda_B\xrightarrow{\sim}\eta_*\Lambda_K.
\tag{2.30}
\]

For a connected affine étale \(W\to U\), the ring \(\Gamma(W,\mathcal O_W)\) is a domain and is flat over \(k[B]\), so multiplication by every nonzero element of \(k[B]\) is injective; its localization at \(k[B]\setminus\{0\}\) is therefore a nonzero domain, and \(W_K\) is nonempty and integral. This proves the first identity on the same basis as above; the second is the case \(U=B\). Adjunction gives

\[
\operatorname{Hom}_U(F,\Lambda_U)\simeq\operatorname{Hom}_{U_K}(F_K,\Lambda_{U_K}),
\qquad
\operatorname{Hom}_B(E,\Lambda_B)\simeq\operatorname{Hom}_{K_{\mathrm{et}}}(E_K,\Lambda_K)
\tag{2.31}
\]

for arbitrary sheaves \(F\) and \(E\). These identities concern the direct image of a constant target only; no constructibility or base change for \(h_*\) is used.

### Step 14. The top-degree curve pairing over an arbitrary field

Let \(K\) be a field in which \(n\) is invertible, and let \(h:C\to\operatorname{Spec}K\) be a separated smooth finite-type curve. For every sheaf \(F\) on \(C\), the map

\[
\beta_{C,F}:\operatorname{Hom}_C(F,\Lambda_C)\longrightarrow\operatorname{Hom}_{K_{\mathrm{et}}}\bigl(R^2h_!F(1),\Lambda_K\bigr),
\qquad
a\longmapsto\operatorname{Tr}_h\circ R^2h_!\bigl(a(1)\bigr)
\tag{2.32}
\]

is an isomorphism.

First let \(K\) be algebraically closed and \(F\) constructible. Apply Lesson 17, Theorem 11.1, to \(F(1)\) and take degree \(-2\). Since \(R\mathcal Hom(F(1),\Lambda(1)[2])\simeq R\mathcal Hom(F,\Lambda)[2]\), the left side gives \(\operatorname{Hom}_C(F,\Lambda)\), and the right side gives \(\operatorname{Hom}_\Lambda(H^2_c(C,F(1)),\Lambda)\) by the self-injectivity of \(\Lambda\) (Lesson 17, Lemma 3.1). The evaluation-and-trace pairing identifies this map with (2.32); the evaluating morphism has degree zero, so the order of its product with the degree-two class introduces no sign.

Now let \(K\) be arbitrary. Fix a separable closure \(K^s\) inside an algebraic closure \(\Omega\), and put \(G=\operatorname{Gal}(K^s/K)\). A sheaf of \(\Lambda\)-modules on \(\operatorname{Spec}K\) is the same as a discrete \(\Lambda\)-module with continuous \(G\)-action. This follows from the finite étale site: a finite separable algebra splits over \(K^s\) into one factor for each embedding, by the Chinese remainder theorem, and a finite Galois cover has overlap algebra \(L\otimes_KL=\prod_{\sigma\in\operatorname{Gal}(L/K)}L\). The sheaf equalizer for this overlap says that the sections over a finite separable extension are the elements fixed by the corresponding subgroup; conversely these fixed modules form a sheaf, by the same equalizer. Taking the union over finite extensions recovers the module, and each element has open stabilizer. In particular

\[
\operatorname{Hom}_{K_{\mathrm{et}}}(E,\Lambda_K)=\operatorname{Hom}_\Lambda(E_\Omega,\Lambda)^G.
\tag{2.33}
\]

For constructible \(F\) we likewise have

\[
\operatorname{Hom}_C(F,\Lambda_C)=\operatorname{Hom}_{C_\Omega}(F_\Omega,\Lambda)^G.
\tag{2.34}
\]

To prove the descent assertion in (2.34), use Lesson 11, Lemma 5.2, to choose a finite presentation of \(F\) by finite sums of sheaves \(a_!\Lambda\), with \(a:V\to C\) affine étale of finite presentation. A map from this presentation to \(\Lambda\) is a finite collection of sections of \(\Lambda\) on the corresponding \(V\), subject to finitely many relations, and these sections are finite clopen partitions. A clopen partition of \(V_{K^s}\) descends to a finite separable extension of \(K\): on a finite affine cover it is given by finitely many idempotents, and their coefficients, the idempotent equations and the agreement on a finite affine cover of the overlaps all descend at a finite stage. The relations between the sections then also hold at a finite stage. Thus every morphism over \(K^s\) descends to a finite extension \(L/K\), which can be enlarged to a finite Galois extension. If the morphism is \(G\)-invariant, its two pullbacks to \(C_L\times_CC_L\) agree; this can be checked after pullback to \(K^s\), since the factors of \(L\otimes_KL\) are indexed by the automorphisms of \(L/K\) and each extends to \(K^s\). The gluing axiom for the finite étale cover \(C_L\to C\) then descends the morphism uniquely to \(C\). This proves (2.34) with \(K^s\) in place of \(\Omega\).

The extension \(\Omega/K^s\) is purely inseparable. For every \(K^s\)-scheme \(W\), the projection \(W_\Omega\to W\) is a homeomorphism: on affine rings the extension is integral, and every element has a power of the characteristic exponent in the original ring, so lying-over gives existence of primes and this power property gives uniqueness; these statements persist after any base change. Consequently clopen partitions are unchanged, and for \(\pi:C_\Omega\to C_{K^s}\) one has \(\pi_*\Lambda=\Lambda\); adjunction shows that pullback preserves the Hom groups in question. This finishes (2.34).

Compact-support base change identifies the stalk in (2.33), for \(E=R^2h_!F(1)\), with \(H^2_c(C_\Omega,F_\Omega(1))\). The isomorphism over the algebraically closed field is \(G\)-equivariant, since evaluation and the trace commute with pullback, the trace by (T1). Taking fixed elements and using (2.33) and (2.34) proves (2.32) for constructible \(F\) over \(K\).

Finally, every sheaf \(F\) is a filtered colimit of constructible sheaves, by Lesson 11, Theorem 5.1. The functor \(F\mapsto R^2h_!(F(1))\) preserves these colimits by Step 3, and both Hom functors in (2.32) turn colimits in the first variable into limits. Passing to these limits proves (2.32) for every \(F\). No constructibility of a higher direct image is needed.

### Step 15. A top-degree calculation in every dimension

Let \(X/k\) be separated, smooth and of finite type, of pure dimension \(d\), with \(k\) algebraically closed. For every sheaf \(F\) on \(X\), define

\[
\Phi_{X,F}:\operatorname{Hom}_X(F,\Lambda_X)\longrightarrow\operatorname{Hom}_\Lambda\bigl(H^{2d}_c(X,F(d)),\Lambda\bigr),
\qquad
a\longmapsto\operatorname{Tr}_X\circ H^{2d}_c\bigl(a(d)\bigr).
\tag{2.35}
\]

We prove by induction on \(d\) that (2.35) is an isomorphism; this concerns the top degree only. For \(d=0\), \(X\) is a finite disjoint union of \(k\)-points, compact cohomology is the direct sum of the stalks of \(F\), and (2.35) is the identity between their componentwise duals. For \(d=1\) it is Step 14.

Let \(d\geq2\). Finite disjoint unions reduce the assertion to connected \(X\), which is integral by Step 2. Choose a nonempty quasi-compact coordinate open \(j:U\hookrightarrow X\). Its complement has dimension at most \(d-1\), so (2.10) identifies the top compact groups of \(U\) and \(X\) for the respective restrictions of \(F\), and (2.29) identifies their Hom groups. The square with (2.35) commutes by (T2), so it suffices to treat \(U\). Project its étale coordinate map \(U\to\mathbf A^d_k\) onto the first \(d-1\) coordinates:

\[
h:U\longrightarrow B=\mathbf A^{d-1}_k,\qquad K=k(B).
\]

This is a smooth relative curve. Put \(E=R^2h_!F(1)\). The top-degree composition isomorphism and the projection formula give

\[
H^{2d}_c(U,F(d))\xrightarrow{\sim}H^{2d-2}_c(B,E(d-1)).
\tag{2.36}
\]

The induction hypothesis applies to \(E\), whether or not it is constructible, so the dual of the right side of (2.36) is canonically \(\operatorname{Hom}_B(E,\Lambda_B)\). Now consider

\[
\operatorname{Hom}_B(E,\Lambda_B)\xrightarrow{\sim}\operatorname{Hom}_{K_{\mathrm{et}}}(E_K,\Lambda_K)\xleftarrow{\sim}\operatorname{Hom}_{U_K}(F_K,\Lambda_{U_K})\xleftarrow{\sim}\operatorname{Hom}_U(F,\Lambda_U).
\tag{2.37}
\]

The first and last isomorphisms are (2.31). Compact-support base change identifies \(E_K=R^2h_{K!}F_K(1)\), and the middle arrow is (2.32). We check the map, not only the objects: the composite from the last group of (2.37) to the first sends \(a:F\to\Lambda_U\) to

\[
\operatorname{Tr}_h\circ R^2h_!\bigl(a(1)\bigr):E\longrightarrow\Lambda_B.
\tag{2.38}
\]

This holds after restriction to \(K\) by the definition (2.32), (T1) and compact-support base change, and restriction is injective on this Hom group by (2.31), so it holds over \(B\). Under the induction isomorphism for \(B\), (2.38) is followed by top compact cohomology and \(\operatorname{Tr}_B\). Naturality of (2.36) and (T3) identify the resulting functional with (2.35) for \(U\). Thus \(\Phi_{U,F}\), and hence \(\Phi_{X,F}\), is an isomorphism. The only duality input of the induction is the curve pairing.

### Step 16. Nondegeneracy and the component formula

The injective \(\Lambda\)-module \(\Lambda\) is a cogenerator for all \(\Lambda\)-modules, not only the finite ones. Indeed, let \(0\neq m\in M\) have order \(r\mid n\). The homomorphism \(\Lambda m\to\Lambda\), \(m\mapsto n/r\), is nonzero, and self-injectivity extends it to \(M\). Thus \(\operatorname{Hom}_\Lambda(M,\Lambda)=0\) implies \(M=0\).

For connected nonempty \(X/k\), take \(F=\Lambda_X\) in (2.35). Since \(H^0(X,\Lambda)=\Lambda\), the resulting isomorphism is the dual of the trace:

\[
\operatorname{Hom}_\Lambda(\Lambda,\Lambda)\xrightarrow{\sim}\operatorname{Hom}_\Lambda\bigl(H^{2d}_c(X,\Lambda(d)),\Lambda\bigr).
\tag{2.39}
\]

Let \(M=H^{2d}_c(X,\Lambda(d))\), and let \(A\) and \(C\) be the kernel and cokernel of \(\operatorname{Tr}_X:M\to\Lambda\). Exactness of Hom into \(\Lambda\) gives an exact sequence \(0\to C^\vee\to\Lambda^\vee\to M^\vee\to A^\vee\to0\), in which the middle map is the dual of the trace. By (2.39), \(A^\vee=C^\vee=0\), and the cogenerator property gives \(A=C=0\). So \(\operatorname{Tr}_X\) is an isomorphism; no higher-dimensional finiteness theorem has been used. For arbitrary \(X\), its finitely many connected components are open and closed; additivity of compact supports and (T2) identify its trace with the sum of their traces. This proves the component formula in (T5), including the empty case.

Finally, for general \(f:X\to S\), the compact-support fibre formula and (T1) identify the stalk of (2.1) at \(\bar s\) with \(\operatorname{Tr}_{X_{\bar s}}:H^{2d}_c(X_{\bar s},\Lambda(d))\to\Lambda\). If the fibre is nonempty and connected, this map is an isomorphism by what was just proved. If this holds for every geometric fibre, the sheaf map is an isomorphism. This proves (T5) and completes the proof of Theorem 2.1. \(\square\)

## 3. Compact support near a geometric point

Let \(\bar x\to X\) be a geometric point. Use affine pointed étale neighbourhoods \((U,\bar u)\); morphisms preserve the chosen point. Fibre products and further affine neighbourhoods give common refinements, and two parallel maps agree after a further refinement. This is a cofiltered category, and its inverse limit is \(X_{(\bar x)}\).

A refinement \(v:U'\to U\) is separated and étale of finite presentation. The counit \(v_!v^*\Lambda\to\Lambda\), given by summation, induces

\[
R\Gamma_c(U',\Lambda(a))\longrightarrow
R\Gamma_c(U,\Lambda(a)).
\tag{3.1}
\]

On ordinary cohomology the direction is reversed: there is pullback from \(U\) to \(U'\). These two directions are dual under the curve theorem when \(U\) has dimension one. For a general refinement of smooth curves, factor its quasi-finite map as an open immersion followed by a finite map using normalization. The finite trace and the open adjunction proved in Lesson 17 identify (3.1) with the transpose of ordinary pullback. Thus this compatibility includes affine neighbourhoods and not just finite étale covers.

Write

\[
\mathcal C^r_{\bar x}(\Lambda(a))
=\{H^r_c(U,\Lambda(a))\}_U,
\qquad
H^r_{c,\mathrm{germ}}(X_{(\bar x)},\Lambda(a))
=\varprojlim_U H^r_c(U,\Lambda(a)).
\tag{3.2}
\]

The first object is a pro-module: it retains the system, including maps that eventually become zero. It is this object that our proof computes. The second is its inverse limit. Neither is a filtered colimit of compact groups using ordinary pullback. For a strict germ not finite type, (3.2) is a definition and does not assert that a finite-type compactification of the germ has been chosen.

**Lemma 3.1 (finite systems).** Inverse limit is exact on cofiltered systems of finite modules. Such a system is pro-zero if and only if its inverse limit is zero.

*Proof.* A pro-zero system means that for each target stage some later transition into it is zero. Its limit is then zero. Conversely, fix a stage \(i\). The images of later groups in the finite group \(A_i\) form a filtered decreasing family of subgroups, so their intersection is achieved by a common refinement of finitely many stages. That intersection is the image of the inverse limit in \(A_i\): any value in it has a compatible lift. To prove the last assertion, put all possible lifts in a product of finite discrete sets. The compatibility conditions are closed, and every finite family of them is solvable at one common refinement. Compactness of the product supplies a simultaneous solution. If the limit is zero, the intersection is zero, so a later map into \(A_i\) is zero.

For a levelwise short exact sequence of finite systems, a compatible element of the quotient likewise has compatible lifts: impose the lifting equations and the transition equations in the product of the finite sets of lifts. Every finite set of equations is solvable at one common refinement, by levelwise surjectivity. Compactness gives all the equations at once. Limits already preserve kernels, so they are exact. Finite diagrams in a pro-category can be represented at common indices by taking refinements; this proves the same assertion for an exact sequence of pro-finite modules. \(\square\)

No assumption of a countable list of neighbourhoods, and no unproved interchange with an infinite product of cochain degrees, occurs in this argument.

## 4. From pointwise vanishing to a uniform derived limit

Two elementary lemmas make the local induction rigorous.

**Lemma 4.1 (uniform refinement).** Let \(B\) be quasi-compact and quasi-separated, and let \(\{E_i\}\) be a cofiltered system of constructible finite module sheaves on \(B\). If its stalk system is pro-zero at every geometric point, then the sheaf system is pro-zero.

*Proof.* Fix \(i\). For a later stage \(j\), the image of \(E_j\to E_i\) is constructible by the Serre property. Its nonzero-stalk locus is a constructible subset of \(B\). Its complement, where that map is zero, is therefore open in the constructible topology. These complements cover \(B\), by the hypothesis on stalks. The constructible topology of a quasi-compact, quasi-separated scheme is compact: on an affine this is the compact topology generated by quasi-compact opens and their complements, and a finite affine cover gives the assertion for \(B\). A finite number of the complements consequently cover \(B\). Choose a common later stage for their maps. Its map to \(E_i\) is zero at every stalk and hence zero as a sheaf map. \(\square\)

Apply the lemma to kernels, cokernels and cohomology sheaves when their finite presentation has been fixed. In particular, an isomorphism of stalk pro-systems gives a pro-isomorphism of constructible sheaf systems. Pointwise vanishing alone would not justify this conclusion without the constructibility and compactness argument.

**Lemma 4.2 (bounded ghosts).** Suppose all \(K_i\) lie in \(D^{[a,b]}\), and each map in a chain induces zero on every cohomology object. A composite of \(b-a+1\) such maps is zero. Consequently a uniformly bounded system with pro-zero cohomology has pro-zero objects in the derived category.

*Proof.* If \(u:A\to B\) kills \(H^b\), its composite with \(B\to H^b(B)[-b]\) is zero. Indeed any map from \(A\in D^{\leq b}\) to the last object is determined by \(H^b(A)\), by the truncation triangle and the vanishing of Hom from \(D^{\leq b-1}\) to \(D^{\geq b}\). Thus \(u\) factors through \(\tau_{\leq b-1}B\). The next ghost, restricted to that truncation, factors through \(\tau_{\leq b-2}\) of its target by the same argument. Repeating lowers the upper degree by one at each step, and after \(b-a+1\) steps the composite factors through zero. For a system, first refine to kill all its finitely many cohomology degrees, and repeat this finitely many times. \(\square\)

We also use finite-presentation descent explicitly. A constructible sheaf and its morphisms on a strict local base descend to an étale neighbourhood of that base point. Equality or zero of a descended morphism holds at some later neighbourhood. This is the finite-presentation/continuity assertion from Lessons 7 and 11: use finite presentations on the finite-presentation étale basis, and descend the finite generators and relations at a common stage. For a bounded derived diagram, make these descents in its finitely many cohomology degrees and use Lemma 4.2 to kill the remaining ghosts. Thus the computations below on a strict base give actual refined neighbourhood maps, rather than merely an equality of numerical fibre dimensions.

## 5. The relative-curve calculation

For a smooth \(f:X\to S\), fix \(\bar x\) over \(\bar s\). A neighbourhood diagram consists of an affine étale \(V\to S\), a pointed affine étale \(U\to X\times_S V\), and its smooth map \(g:U\to V\). Put \(j_V:V\to S\). Trace gives a morphism of inverse systems

\[
\{R(fj_U)_!\Lambda(d)\}_{{(U,V)}}
\longrightarrow
\{j_{V,!}\Lambda[-2d]\}_{{(U,V)}}.
\tag{5.1}
\]

On the left \(j_U:U\to X\); its map to the term on the right is \(j_{V,!}\operatorname{Tr}_g\). The transition maps on both sides are the étale counits. Property (T2) of Theorem 2.1 makes their squares commute.

**Proposition 5.1 (dimension one).** If \(d=1\), the cone system in (5.1) is pro-zero in the derived category. Equivalently, trace is an isomorphism of these bounded derived pro-systems.

*Proof.* Fix an original target diagram \((U_0,V_0)\). The chosen geometric point identifies \(B=(V_0)_{(\bar v_0)}\) with \(S_{(\bar s)}\), and selects the map \(B\to V_0\). First consider the relative trace cones on \(V_0\), before applying \(j_{V_0,!}\). Pullback along this selected map identifies their source terms with \(Rg_{U,!}\Lambda(1)\) on \(B\). Thus \(U_B\) means \(U\times_{V_0}B\), rather than the union of all sheets of \(U\times_SB\). They have degrees zero through two. The source neighbourhoods have smooth relative dimension one. Their images contain the closed point of \(B\), and a smooth map has open image; an open subset of a local scheme containing its closed point is the whole scheme. Thus every geometric fibre is nonempty.

For a geometric \(\bar t\to B\), compact base change gives the finite groups

\[
(R^qg_{U,!}\Lambda(1))_{\bar t}
=H^q_c(U_{\bar t},\Lambda(1)).
\tag{5.2}
\]

The inverse limit of the affine schemes \(U_{\bar t}\) is the local fibre
\(X_{(\bar x)}\times_B\bar t\). Continuity and smooth local acyclicity, already proved in Lesson 15, give

\[
\mathop{\mathrm{colim}}_U H^r(U_{\bar t},\Lambda)
=\begin{cases}\Lambda&r=0,\\0&r>0.\end{cases}
\tag{5.3}
\]

The map from \(\Lambda\) in degree zero is the constant-section map. These are smooth affine curves over a separably closed field; passage to its algebraic closure is an étale-topos equivalence, so the proved curve theorem applies. It identifies each group in (5.2) with the dual of \(H^{2-q}(U_{\bar t},\Lambda)\), and identifies the transition trace with the transpose of pullback, by Section 3.

For positive ordinary degree, a finite group's generators all become zero at a common later stage by (5.3). The corresponding compact transition is zero. In ordinary degree zero the constant-section inclusion is injective, because the fibre is nonempty. Its finite quotient becomes zero at a later stage, since (5.3) says the colimit is exactly the constants. Exact finite-module duality turns this into the statement that the kernel system of the top trace is pro-zero. That trace is surjective: on each fibre it sums the component traces, each normalized to one. Thus at every \(\bar t\) the compact pro-system is \(\Lambda[-2]\), via trace.

Each \(R^qg_{U,!}\Lambda(1)\), its trace kernel and the relevant images are constructible, by [Theorem 12.3 of Lesson 14](cohomology-with-compact-support.md#proof-of-general-constructibility), whose affine-line proof provider is linked there. Their images are again constructible: on a common finite stratification where the two sheaves are locally constant, a morphism is locally a fixed map of finite modules, whose kernel and image are locally constant. This also proves the needed Serre assertion over the coherent strict base. Lemma 4.1 now kills the finitely many cohomology sheaves of the trace cone by one uniform refinement on \(B\). The cones have a fixed finite range, so repeated refinement and Lemma 4.2 kill their maps in the derived category itself.

Finally descend the finite data to \(V\)'s. The schemes and coefficients have finite presentation; compact base change identifies their cohomology sheaves over \(B\), and zero of the finitely many descended sheaf maps holds at a later base neighbourhood. Repeat the bounded-ghost construction there. For the resulting \(v:V'\to V_0\), the refined relative cone map \(C_{U'}\to v^*C_{U_0}\) is zero on \(V'\). Its adjoint \(v_!C_{U'}\to C_{U_0}\) is therefore zero. Applying \(j_{V_0,!}\) gives the zero cone map on \(S\) required in (5.1). Since the original diagram was arbitrary, this proves pro-zero of that system, including the extension-by-zero maps between different base neighbourhoods. \(\square\)

The proof used local acyclicity of the strict fibre, not the false assertion that a whole smooth affine curve has zero degree-one cohomology. The finite cohomology of whole curves supplies the uniform generator argument; their degree-one groups are allowed to be large.

### Checking constructibility in the relative-curve argument

The morphism \(g_U:U_B\to B\) in Section 5 satisfies the full hypotheses of [Theorem 12.3 of Lesson 14](cohomology-with-compact-support.md#proof-of-general-constructibility). Here \(B\) is the spectrum of a strict henselization, hence affine and quasi-compact and quasi-separated; it need not be Noetherian. Before base change, \(U\) and \(V\) are affine, and \(g:U\to V\) is smooth, hence locally of finite presentation. An affine morphism is quasi-compact and separated, so \(g\) is separated and of finite presentation. These properties persist after base change to \(B\). The coefficient sheaf \(\Lambda(1)=\mu_n\) is finite locally constant because \(n\) is invertible on the base, and \(\Lambda=\mathbf Z/n\mathbf Z\) is a Noetherian torsion ring. Thus every \(R^qg_{U,!}\Lambda(1)\) is constructible. Its kernels and images are constructible by the Serre property, and all their stalks are finite because a finitely generated module over this finite ring is a finite set. This verifies the input to Lemma 4.1 without replacing its strict-local base by a Noetherian one.

For the algebraically closed field uses in Sections 7, 10 and 13, the schemes are separated of finite type over that field, and the coefficients lie in the specified constructible category. [Corollary 12.4 of Lesson 14](cohomology-with-compact-support.md#general-finiteness-over-an-algebraically-closed-field) gives finite compactly supported cohomology in every degree. Neither this corollary nor its proof uses the duality theorem being established here.

## 6. Induction in the relative dimension

**Theorem 6.1 (local trace system).** Proposition 5.1 holds for every \(d\geq0\).

*Proof.* For \(d=0\), \(f\) is étale. After taking \(V\) to be a pointed étale neighbourhood in its source, the base-changed map has the distinguished section through \(\bar x\). Its image is open, since it is a section of an étale map. Restrict the source neighbourhood to that section. The trace comparison there is the identity of \(j_{V,!}\Lambda\). Such restrictions refine every diagram, proving the result.

The case \(d=1\) is Proposition 5.1. Suppose \(d>1\), and assume the result in lower dimension. Étale locally at \(\bar x\), smooth coordinates factor \(f\) as

\[
X\xrightarrow{h}Y\xrightarrow{g}S,
\qquad \dim(h)=1,\quad\dim(g)=d-1.
\tag{6.1}
\]

Indeed take an étale coordinate map to \(\mathbf A^d_S\), and project onto \(\mathbf A^{d-1}_S\). After restriction to an affine chart both maps are separated and smooth of finite presentation. This restriction is cofinal in the source neighbourhood system, so suffices for the local assertion.

Use neighbourhood triples \(U\to X\), \(V\to Y\), \(W\to S\), with \(U\to V\to W\). Any finite list of such conditions can be achieved by taking fibre products and a further affine pointed chart. Conversely every source neighbourhood admits such a refinement. Thus the iterated system is the same local system, indexed cofinally, and no special chosen sequence is being substituted for it.

The dimension-one result for \(h\), in the derived pro-category on \(Y\), is

\[
\{R(hj_U)_!\Lambda(1)\}_{(U,V)}
\xrightarrow{\sim}
\{j_{V,!}\Lambda[-2]\}_{(U,V)}.
\tag{6.2}
\]

Apply \(Rg_!\), tensor with the additional twist \((d-1)\), and use composition. Zero derived maps remain zero under this exact functor, so a pro-zero cone remains pro-zero. The resulting source terms are \(R(fj_U)_!\Lambda(d)\); the target terms are
\(R(gj_V)_!\Lambda(d-1)[-2]\). The induction hypothesis for \(g\) identifies their pro-system with
\(j_{W,!}\Lambda[-2(d-1)][-2]\). The composite is exactly (5.1), by compatibility of trace with composition and base change. It therefore has pro-zero cone.

Here is the compact Leray content of this argument. At every finite neighbourhood diagram, composition has the good-truncation spectral sequence

\[
R^pg_!R^qh_!\Lambda(d)
\Longrightarrow R^{p+q}(gh)_!\Lambda(d).
\tag{6.3}
\]

There are only \(0\leq q\leq2\) and \(0\leq p\leq2(d-1)\). Proposition 5.1 kills the unwanted rows uniformly as pro-sheaves; the remaining row is \(\Lambda(d-1)\) in degree two, via the actual trace map. The finite filtration then reduces (6.3) to the induction hypothesis. More strongly, Lemma 4.2 gives (6.2) at the derived level before applying \(Rg_!\), so possible extension maps between rows are killed as well. This is the justification of the limit Leray step. It uses finitely many truncations and refinements, rather than an unjustified interchange of infinite cochain totals with inverse limit. \(\square\)

## 7. The absolute local statement

**Corollary 7.1.** If \(X/k\) is smooth of pure dimension \(N\) and \(x\) is a closed point, then

\[
\mathcal C^r_x(\Lambda)=0\quad(r\ne2N),
\qquad
\operatorname{Tr}:\mathcal C^{2N}_x(\Lambda(N))
\xrightarrow{\sim}\Lambda.
\tag{7.1}
\]

The same formulas hold for the inverse-limit groups in (3.2).

*Proof.* Apply Theorem 6.1 to \(X\to\operatorname{Spec}k\). Pointed étale base neighbourhoods of the algebraically closed field refine to its distinguished copy of \(\operatorname{Spec}k\). Hence its target system is the constant \(\Lambda[-2N]\). Taking cohomology gives (7.1). Compact cohomology at every source stage is finite by the general finiteness input of Lesson 14. Lemma 3.1 passes the pro-isomorphism to inverse limits and identifies vanishing with pro-zero. Removing the twist gives \(\Lambda(-N)\) in degree \(2N\). \(\square\)

Explicitly, coordinates give a smooth relative curve from the strict germ of \(X\) to the strict germ of a smooth \((N-1)\)-fold. Equations (5.2)–(5.3) identify its local-fibre compact row with \(\Lambda(-1)\) in degree two. The finite Leray filtration of Section 6 then gives

\[
H^r_{c,\mathrm{germ}}(X_{(x)},\Lambda(N))
=H^{r-2}_{c,\mathrm{germ}}(Y_{(y)},\Lambda(N-1)),
\tag{7.2}
\]

via trace. Iteration ends at a point. Thus the claimed local concentration was proved from the curve case and local acyclicity; it has not been deduced from the global theorem we are about to prove.

## 8. Exceptional inverse image and its local description

Let \(f\) be separated finite type between quasi-compact, quasi-separated schemes. The category of \(\Lambda\)-module sheaves is Grothendieck. Brown representability in its derived category says that a contravariant cohomological functor taking sums to products is represented by an object. For fixed \(A\), apply it to

\[
E\longmapsto\operatorname{Hom}_S(Rf_!E,A).
\]

It is cohomological because \(Rf_!\) is exact, and takes sums to products because \(Rf_!\) preserves sums. Representing objects and Yoneda give a right adjoint \(Rf^!\), with

\[
\operatorname{Hom}_X(E,Rf^!A)
=\operatorname{Hom}_S(Rf_!E,A).
\tag{8.1}
\]

Naturality determines its functoriality and counit; adjoints of exact triangulated functors are exact, as follows by applying (8.1) to a triangle and its shifts. This constructs the operation without assuming its smooth formula.

For an affine étale \(j:U\to X\), exact extension by zero and composition give

\[
H^r(U,Rf^!A)
=\operatorname{Hom}_X(j_!\Lambda,Rf^!A[r])
=\operatorname{Hom}_S(R(fj)_!\Lambda,A[r]).
\tag{8.2}
\]

Sheafifying this presheaf computes \(H^r(Rf^!A)\). In particular its stalk is the filtered colimit over pointed \(U\) of the last groups. To see that sheafification is valid even for an unbounded \(A\), use a K-injective representative for \(Rf^!A\). Its sections on \(U\) compute hypercohomology; the filtered colimit of those section complexes is its stalk complex. Exact filtered colimits commute with taking cohomology, giving the assertion.

Composition of lower shrieks transposes to
\(R(gh)^!=Rh^!Rg^!\). The counit is the composite of the two counits: testing Hom makes both maps the identity map in the two adjunctions, so uniqueness proves their agreement and the associativity condition. For an étale base change \(v:V\to S\), with source map \(v_X\), the corresponding comparison
\(v_X^*Rf^!A=Rf_V^!v^*A\) follows by testing a complex \(B\) on the base-changed source:

\[
\begin{aligned}
\operatorname{Hom}(B,v_X^*Rf^!A)
&=\operatorname{Hom}(v_{X,!}B,Rf^!A)\\
&=\operatorname{Hom}(v_!Rf_{V,!}B,A)\\
&=\operatorname{Hom}(Rf_{V,!}B,v^*A).
\end{aligned}
\tag{8.3}
\]

These equalities also prove compatibility of the counit with étale localization: each comparison is the mate of the lower-shriek comparison under the same adjunction, so composing it with the counit returns that comparison. The two triangle identities for units and counits verify this directly. This is the compatibility isolated in Deligne's “Dualité,” §4.

There is also an internal comparison, for arbitrary \(A,E\),

\[
Rf_*R\mathcal Hom_X(E,Rf^!A)
\xrightarrow{\sim}R\mathcal Hom_S(Rf_!E,A).
\tag{8.4}
\]

To prove it, test by Hom from an arbitrary \(M\) on \(S\). The left group is, in order,

\[
\begin{aligned}
\operatorname{Hom}_X(f^*M\otimes^LE,Rf^!A)
&=\operatorname{Hom}_S(Rf_!(f^*M\otimes^LE),A)\\
&=\operatorname{Hom}_S(M\otimes^LRf_!E,A)\\
&=\operatorname{Hom}_S(M,R\mathcal Hom_S(Rf_!E,A)).
\end{aligned}
\tag{8.5}
\]

The middle equality is the already proved arbitrary-complex projection formula. Yoneda gives (8.4). Its map is evaluation followed by the counit, because every equality used that adjunction. Taking derived global sections gives the corresponding isomorphism of global derived Hom complexes. \(\square\)

## 9. The relative smooth duality formula

Transpose (2.3) under (8.1). It gives a natural map

\[
t_{f,A}:f^*A(d)[2d]\longrightarrow Rf^!A.
\tag{9.1}
\]

**Theorem 9.1.** For every complex \(A\in D(S,\Lambda)\), (9.1) is an isomorphism. Under it the adjunction counit is precisely (2.3).

*Proof.* Fix \(\bar x\) over \(\bar s\). In the neighbourhood diagrams of Section 5, untwist (5.1) to obtain the derived pro-comparison

\[
\{R(fj_U)_!\Lambda\}\xrightarrow{\sim}
\{j_{V,!}\Lambda(-d)[-2d]\}.
\tag{9.2}
\]

Its cone is pro-zero by Theorem 6.1. Apply Hom into \(A[r]\). The long exact sequences of the cone triangles, followed by exact filtered colimit, show that (9.2) gives an isomorphism

\[
\begin{aligned}
\mathop{\mathrm{colim}}_{(U,V)}
\operatorname{Hom}_S(R(fj_U)_!\Lambda,A[r])
&=\mathop{\mathrm{colim}}_{(U,V)}
\operatorname{Hom}_S(j_{V,!}\Lambda(-d)[-2d],A[r])\\
&=\mathop{\mathrm{colim}}_V H^{r+2d}(V,A(d))\\
&=(H^{r+2d}(A(d)))_{\bar s}.
\end{aligned}
\tag{9.3}
\]

There is no boundedness restriction on \(A\): any element of Hom from a cone is killed by the later zero cone map itself. Forgetting the auxiliary neighbourhood in these colimits is cofinal. For a fixed source neighbourhood and a fixed base neighbourhood, their fibre product has a further pointed source neighbourhood; similarly every base neighbourhood has such a source neighbourhood. This verifies both cofinality assertions in (9.3).

By (8.2), the left group is \(H^r(Rf^!A)_{\bar x}\); the right group is \(H^r(f^*A(d)[2d])_{\bar x}\). The comparison is the map induced by (9.1): both are obtained by precomposing Hom with the trace of the same neighbourhood diagram. All geometric stalks and all cohomological degrees agree, proving the theorem. Finally (9.1) was the adjoint of (2.3), so the counit composed with \(Rf_!t_{f,A}\) is (2.3), by the adjunction triangle identity. \(\square\)

This proof also verifies composition of the smooth identifications. Transpose the two successive traces; their composite is the transpose of the composite trace and hence \(t_{gh,A}\). Their twists add and their shifts add. The identification commutes with base change because the trace, the lower-shriek base-change comparison and inverse image do. It can alternatively be used to define that smooth upper-shriek base-change isomorphism, with the same counit.

For completeness, the formula gives the amplitude

\[
Rf^!(D^{[a,b]})\subset D^{[a-2d,b-2d]}.
\tag{9.4}
\]

Before knowing the formula, adjunction gives the lower bound \(Rf^!D^{\geq a}\subset D^{\geq a-2d}\). Indeed test (8.1) on \(E=\tau_{\leq a-2d-1}Rf^!A\). The lower-shriek amplitude places \(Rf_!E\) in \(D^{\leq a-1}\), so its Hom into \(A\in D^{\geq a}\) is zero. The truncation inclusion is therefore zero, forcing its cohomology to vanish. This adjunction argument alone supplies no analogous upper bound. Equation (9.3) proves the arbitrary-complex smooth formula directly, and that formula supplies both bounds in (9.4).

## 10. Global Poincaré duality

Set \(p:X\to\operatorname{Spec}k\) and

\[
K_X=\Lambda_X(N)[2N],\qquad
D_XE=R\mathcal Hom_X(E,K_X).
\tag{10.1}
\]

**Theorem 10.1.** For every \(E\in D(X,\Lambda)\), evaluation and trace give a canonical isomorphism

\[
R\Gamma(X,D_XE)
\xrightarrow{\sim}
R\operatorname{Hom}_\Lambda(R\Gamma_c(X,E),\Lambda).
\tag{10.2}
\]

For a finite locally constant \(F\), it gives mutually perfect finite-group pairings

\[
H^i_c(X,F)\times H^{2N-i}(X,F^\vee(N))
\xrightarrow{\ \operatorname{Tr}_X(a\cup b)\ }\Lambda,
\qquad F^\vee=\mathcal Hom_\Lambda(F,\Lambda).
\tag{10.3}
\]

*Proof.* Theorem 9.1 identifies \(Rp^!\Lambda\) with \(K_X\), with counit the specified trace. Apply (8.4) to \(p\), \(A=\Lambda\) and \(E\). The small étale site of the algebraically closed field is the category of modules, with exact global sections. Thus (8.4) is exactly (10.2), with its evaluation-and-trace map.

Locally \(F\) is a constant finite module \(M\). Lesson 17, Lemma 3.1, proves that \(\Lambda\) is injective over itself, including composite \(n\); therefore \(R\operatorname{Hom}_\Lambda(M,\Lambda)=M^\vee\) in degree zero. Sheafifying a finite-free module resolution on a trivializing cover proves the same internal formula. The invertible twist is exact, so
\(D_XF=F^\vee(N)[2N]\).

The same self-injectivity identifies degree \(-i\) on the right of (10.2) with \(H^i_c(X,F)^\vee\): dualize cycles, boundaries and their quotient by the exact Hom functor. Degree \(-i\) on the left is \(H^{2N-i}(X,F^\vee(N))\). Compact groups are finite by the earlier stated finiteness input; the isomorphism proves finiteness of these ordinary groups as well. Finite-module evaluation is an isomorphism to the bidual, so each factor is the dual of the other. The pairing is (10.3) because (8.4) uses evaluation followed by the trace counit. \(\square\)

Invertibility of \(n\) is essential. In characteristic \(p\), Lesson 16's Artin–Schreier example gives an infinite \(H^1(\mathbf A^1,\mathbf Z/p)\); the finite prime-to-characteristic pairing proved here has no such conclusion for those coefficients.

For a general constructible complex, (10.2) still uses internal derived Hom. Replacing it by just the ordinary degree-zero dual sheaf would drop ramification or extension terms. For local systems (10.3) is ordinary cohomology and needs neither free fibres nor a finite projective resolution of \(F\). We order the compactly supported factor first; exchanging degree \(r\) and degree \(s\) contributes \((-1)^{rs}\).

**Corollary 10.2 (top compact degree).** For connected \(X\), trace is an isomorphism

\[
H^{2N}_c(X,\Lambda(N))\xrightarrow{\sim}\Lambda.
\tag{10.4}
\]

*Proof.* Apply (10.3) to \(F=\Lambda(N)\) in degree \(2N\). Its other factor is \(H^0(X,\Lambda)=\Lambda\), since \(X\) is connected. Pairing with its constant section \(1\) is exactly trace, proving (10.4). For a finite union of connected components the group is a copy of \(\Lambda\) for each component and trace is their sum. \(\square\)

## 11. Purity and the distinction between sheaves and groups

Let \(i:Z\hookrightarrow X\) be a closed immersion of smooth \(k\)-schemes, with \(X\) purely \(N\)-dimensional and \(Z\) purely \((N-c)\)-dimensional. Write \(j:X-Z\hookrightarrow X\). The right adjoint \(i^!\) of exact \(i_*\) is sections supported on \(Z\), regarded as a sheaf on \(Z\). Since \(i_*\) is exact, \(i^!\) sends injectives to injectives. An injective resolution therefore gives both

\[
i_*Ri^!E\longrightarrow E\longrightarrow Rj_*j^*E\longrightarrow i_*Ri^!E[1]
\tag{11.1}
\]

and \(R\Gamma_Z(X,E)=R\Gamma(Z,Ri^!E)\). Indeed restriction of an injective sheaf to an open is surjective on sections, with kernel the supported sections, so (11.1) comes from that short exact sequence of resolution complexes. This proves the support formalism used here.

**Theorem 11.1 (smooth-pair purity).** There is a canonical orientation isomorphism

\[
Ri^!\Lambda_X=\Lambda_Z(-c)[-2c].
\tag{11.2}
\]

Consequently

\[
R^qi^!\Lambda_X=0\ (q\ne2c),\qquad
R^{2c}i^!\Lambda_X=\Lambda_Z(-c),
\tag{11.3}
\]

whereas the global groups satisfy

\[
H^r_Z(X,\Lambda)=H^{r-2c}(Z,\Lambda(-c)).
\tag{11.4}
\]

*Proof.* The structure maps satisfy \(p_Z=p_Xi\). Composition of right adjoints gives

\[
Ri^!Rp_X^!\Lambda=Rp_Z^!\Lambda.
\tag{11.5}
\]

Substitute the two proved smooth formulas:
\(Ri^!(\Lambda_X(N)[2N])=\Lambda_Z(N-c)[2N-2c]\).
An invertible local system \(T\) commutes with \(Ri^!\). To verify this, test Hom from \(B\) on \(Z\), move \(T\) to its inverse twist on the other argument, use \(i_*B\otimes T^{-1}=i_*(B\otimes i^*T^{-1})\), and apply the adjunction. Yoneda identifies the resulting functors. Thus twist by \((-N)\) and shift by \([-2N]\) give (11.2). Its single cohomology degree gives (11.3). Applying \(R\Gamma(Z,-)\) to (11.2) gives (11.4). \(\square\)

In particular \(H^{2c}_Z(X,\Lambda)=H^0(Z,\Lambda(-c))\), and the groups below \(2c\) vanish. Higher global groups need not vanish. For example take the zero section
\(Z=\mathbf P^1\times\{0\}\subset X=\mathbf P^1\times\mathbf A^1\), with \(c=1\). Then

\[
H^4_Z(X,\Lambda)=H^2(\mathbf P^1,\Lambda(-1))
=\Lambda(-2)\ne0.
\tag{11.6}
\]

So the global cohomology with supports is not concentrated in one degree. The concentrated object is \(Ri^!\Lambda\); global support cohomology also includes the cohomology of \(Z\).

## 12. Gysin maps, orientation and point classes

Transpose the purity isomorphism by the closed adjunction. The counit supplies
\(i_*\Lambda_Z\to\Lambda_X(c)[2c]\). With a twist and either ordinary or compact global sections, it gives

\[
\begin{aligned}
i_* &:H^r(Z,\Lambda(a))\longrightarrow H^{r+2c}(X,\Lambda(a+c)),\\
i_* &:H^r_c(Z,\Lambda(a))\longrightarrow H^{r+2c}_c(X,\Lambda(a+c)).
\end{aligned}
\tag{12.1}
\]

In the second line, \(Rp_{X,!}i_*=Rp_{Z,!}\), since a closed immersion is proper. These are the Gysin maps. Their degrees and twists record the codimension, not the dimensions of the whole varieties.

**Proposition 12.1.** Gysin maps compose for a chain of smooth closed immersions. They satisfy the projection formula, and in the top compact degree preserve trace:

\[
i_*(u\cup i^*v)=i_*u\cup v,
\qquad
\operatorname{Tr}_X(i_*u)=\operatorname{Tr}_Z(u)
\quad(u\in H^{2(N-c)}_c(Z,\Lambda(N-c))).
\tag{12.2}
\]

*Proof.* Purity was defined by (11.5), so for two closed immersions its orientation is the composite right-adjoint identification. The counit for their composite is the composite of their counits, as proved in Section 8. This proves composition, with the twists and shifts added. The closed projection formula follows on sheaf stalks, on \(Z\) by the identity tensor formula and off \(Z\) by zero, and hence on K-flat complexes. Applying its adjunction and the counit gives the first equality of (12.2); the class \(u\) remains first in the coefficient tensor. For trace, compose the counit of \(i\) with the counit of \(p_X\). Their composite is the counit of \(p_Z\), which Theorem 9.1 identifies with its trace. This is the second equality. \(\square\)

A closed point \(x\) has \(c=N\). Its class is \(i_*1\) in compact degree \(2N\), or the image of the supported class in ordinary degree \(2N\). Equation (12.2) gives

\[
\operatorname{Tr}_X(\operatorname{cl}_c(x))=1.
\tag{12.3}
\]

This fixes its orientation without choosing a root. Even if its ordinary image vanishes, its compact image is the generator of (10.4).

**Lemma 12.2 (divisor normalization).** For a smooth divisor \(D\) in a smooth \(X\), the Gysin class of \(1\) is \(c_1^{(n)}\mathcal O_X(D)\) in \(H^2(X,\mu_n)\).

*Proof.* Near a point of \(D\), choose its smooth normal parameter \(t\). The map to \(\mathbf A^1\) given by \(t\) is smooth after shrinking. Pulling back the localization triangle along this smooth map is valid by smooth base change for the complementary open direct image, proved in Lesson 15. Write \(\lambda\) for its supported boundary. The trace-positive orientation is \(-\lambda\kappa(t)\), by Lesson 17, Lemmas 4.2–4.3. To compare this with (11.2), write \(i_0:\{0\}\hookrightarrow\mathbf A^1\) and \(h:D\to\{0\}\), so \(ti=i_0h\). Composition of exceptional inverse images gives \(Ri^!Rt^!=Rh^!Ri_0^!\). Both \(t\) and \(h\) are smooth of relative dimension \(N-1\). Substitute their already proved smooth formulas and cancel the common twist and shift. The result identifies the supported orientation on \(X\) with the pullback of the point orientation on \(\mathbf A^1\). The composite counits agree by Section 8, so this is the same comparison as in the localization triangle. Thus the negative raw boundary, not the raw boundary, is the specified purity generator.

On these charts the divisor valuation sequence is
\(0\to\mathbf G_m\to j_*\mathbf G_m\to i_*\mathbf Z\to0\).
A unit off \(D\) is locally a power of \(t\) times a unit, since its divisor can have support only on that smooth principal divisor. In the fixed Picard convention of Lesson 10, equation (5.4), the connecting line bundle of \(1\) in this sequence is \(\mathcal O_X(-D)\). We must retain both connecting-map signs to compare it with Gysin.

Here is a global comparison, so that equality is not inferred merely by restricting ordinary degree-two classes to charts. Let \(\sigma_D\in H^1_D(X,\mathbf G_m)\) be the relative line-bundle class of \(\mathcal O_X(D)\) with its canonical trivialization on \(X\setminus D\). Cohomology in this degree with supports classifies a line bundle with such a trivialization: the complex \(\operatorname{Cone}(R\Gamma(X,\mathbf G_m)\to R\Gamma(X\setminus D,\mathbf G_m))[-1]\) records its transition cocycle together with a trivializing zero-cochain on the complement. On a chart with equation \(t\), \(\sigma_D\) is \(\lambda_{\mathbf G_m}(t)\). One can verify this sign without a torsor convention implicit in the notation: use local equations \(t_i\), form the divisor coefficient cocycle from their differences, and use the support cone. Its ordinary cocycle is the negative of that divisor coefficient cocycle, hence represents \(\mathcal O_X(D)\), since the latter coefficient cocycle represents \(\mathcal O_X(-D)\). Equivalently, on a two-open cover the forgetting-support map sends \(\lambda_{\mathbf G_m}(t)\) to \(-m_{\mathbf G_m}(t)\), exactly the flasque-resolution calculation in Lesson 17, Lemma 4.3. These local equations and their unit ratios give the global relative cocycle just described.

Explicitly, write the abelian-group cochains additively, and put \(V=X\setminus D\). The relative complex has pairs \((a,b)\) of degrees \(r,r-1\), with differential \((da,a|_V-db)\). Its localization boundary sends a cocycle \(b\) on \(V\) to \((0,-b)\): if \(\widetilde b\) is a resolution lift, the supported cocycle \((d\widetilde b,0)\) differs from \((0,-b)\) by \(d(\widetilde b,0)\). For local equations \(t_i\), the coefficient cocycle is \(c=\delta t\), with multiplicative values \(t_j/t_i\), which are units on the overlaps. The relative pair \((-c,-t|_V)\) is closed, since \(\delta c=0\) and \(-c|_V+\delta(t|_V)=0\). Its first component is the negative divisor coefficient class; on each chart it is \((0,-t_i)\), hence \(\lambda_{\mathbf G_m}(t_i)\). Refining the cover or changing local equations by units gives a relative coboundary together with the usual change of trivialization of the same line bundle. This constructs \(\sigma_D\) and verifies both its ordinary image and its local boundary description with the same signs.

Apply the supported Kummer connecting map \(\kappa_D\) to \(\sigma_D\). Coefficient connecting maps and localization connecting maps anticommute:

\[
\kappa_D\lambda_{\mathbf G_m}(t)=-\lambda_{\mu_n}\kappa(t).
\tag{12.4}
\]

To check (12.4), take compatible split injective resolutions of the Kummer sequence and the three complexes of sections supported on \(D\), all sections, and sections on the complement. The lift calculation of Lesson 17, Lemma 4.3, applies to these exact rows as well: if \(d\widetilde y-r\widetilde z=i(v)\) and \(d\widetilde z=i(\beta)\), differentiation gives \(dv=-r\beta\). The two iterated boundaries are \([\beta]\) and \([-\beta]\). This proves the asserted anticommutation, including the sign.

Purity identifies \(H^2_D(X,\mu_n)\) with \(H^0(D,\Lambda)\). The class \(\kappa_D(\sigma_D)\) has local value \(1\) by (12.4) and the trace-positive orientation proved above; hence it is the global Gysin generator. Forgetting supports commutes with the coefficient connecting map. Its ordinary image is therefore \(\kappa_X([\mathcal O_X(D)])=c_1^{(n)}\mathcal O_X(D)\). This proves the equality globally. \(\square\)

The construction commutes with étale localization. In the normal coordinate calculation it also commutes with transverse pullback: both local classes are the negative boundary of the pulled-back normal parameter. These compatibilities are enough for the hyperplane and affine-space calculations below. No purity assertion for arbitrary singular closed subschemes has been used.

## 13. Perfect constant-coefficient complexes and products

One cannot in general replace the dual of a derived tensor by the tensor of its duals over \(\mathbf Z/n\). We prove the finite-projective property needed for constant coefficients.

**Lemma 13.1.** The complex \(A_X=R\Gamma_c(X,\Lambda)\) is perfect over \(\Lambda\): it has a bounded representative by finite projective modules, in degrees \([0,2N]\).

*Proof.* Its cohomology is finite and in that interval, by the earlier compact bound and finiteness input. For any module \(M\), the projection formula gives

\[
A_X\otimes^L_\Lambda M=R\Gamma_c(X,\underline M).
\tag{13.1}
\]

The right side has no negative cohomology and vanishes above \(2N\), since the compact bound applies to every \(\Lambda\)-sheaf. A bounded complex with finite cohomology over the Noetherian ring \(\Lambda\) admits a bounded-above resolution \(P\) by finite free modules: successively choose finite generators for the highest cohomology and the kernels of the maps already constructed. Noetherianity keeps each subsequent kernel finitely generated. We may take \(P^r=0\) for \(r>2N\).

Put \(Q=\operatorname{coker}(P^{-1}\to P^0)\). Since the negative cohomology of \(P\) vanishes, its nonpositive part is a free resolution of \(Q\). For every \(M\), (13.1) gives
\(\operatorname{Tor}_1^\Lambda(Q,M)=H^{-1}(P\otimes M)=0\).
Thus \(Q\) is flat, by the tensor criterion for flatness. It is finitely presented, so is projective. Replace the negative part of \(P\) by \(Q\) in degree zero. The resulting finite-projective complex, in degrees zero through \(2N\), is quasi-isomorphic to \(A_X\). \(\square\)

The same proof works for any separated finite-type variety when its constant coefficient is \(\Lambda\). It does not assert that \(R\Gamma_c(X,F)\) is perfect for a nonfree local system: already on a point, \(F=\mathbf Z/\ell\) over \(\mathbf Z/\ell^2\) is a counterexample.

**Lemma 13.2 (compact Künneth and trace).** For separated finite-type \(X,Y\),

\[
R\Gamma_c(X\times Y,\Lambda)
=A_X\otimes^L A_Y.
\tag{13.2}
\]

For smooth varieties of dimensions \(N,M\), the product trace is the tensor of their traces under the twisted version of (13.2).

*Proof.* Compact base change for \(\operatorname{pr}_1:X\times Y\to X\) identifies \(R\operatorname{pr}_{1,!}\Lambda\) with the constant complex \(\underline{R\Gamma_c(Y,\Lambda)}\). Apply composition and then the compact projection formula over the point to obtain (13.2). These maps are the external-product maps because both projection comparisons are defined by tensor and adjunction. For trace, factor the structure map of \(X\times Y\) as \(\operatorname{pr}_1\) followed by \(p_X\). The trace of \(\operatorname{pr}_1\) is the base change of the trace of \(p_Y\); composition compatibility gives the stated tensor trace. \(\square\)

Consequently duality for \(X\) and \(Y\), together with ordinary Künneth from Lesson 16, proves constant-coefficient duality for their product. Here are the actual derived identifications:

\[
\begin{aligned}
&R\Gamma(X\times Y,\Lambda(N+M)[2N+2M])\\
&\quad=R\Gamma(X,\Lambda(N)[2N])\otimes^L
R\Gamma(Y,\Lambda(M)[2M])\\
&\quad=A_X^\vee\otimes^L A_Y^\vee\\
&\quad=(A_X\otimes^LA_Y)^\vee.
\end{aligned}
\tag{13.3}
\]

The last equality is valid by Lemma 13.1: on bounded finite-projective representatives it is the ordinary Hom–tensor identity with the graded signs. The first two comparisons are the factor Künneth and factor duality maps, so by Lemma 13.2 their composite is the product evaluation-and-trace map. This argument does not assume duality for the product in advance.

For classes \(a,b\) in compact degrees \(i,j\), and \(\alpha,\beta\) in the complementary ordinary degrees, the resulting value is

\[
(-1)^{j(2N-i)}
\operatorname{Tr}_X(a\cup\alpha)
\operatorname{Tr}_Y(b\cup\beta).
\tag{13.4}
\]

The sign moves \(b\) past \(\alpha\) before pairing the factors. For a composite \(n\), Tor contributions can still enter the cohomology of (13.2). The proof concerns derived complexes, so does not discard those terms.

## 14. Three worked examples

**Example 14.1: affine space.** The curve calculation gives
\(R\Gamma(\mathbf A^1,\Lambda)=\Lambda\) and
\(R\Gamma_c(\mathbf A^1,\Lambda)=\Lambda(-1)[-2]\).
Ordinary Künneth and Lemma 13.2, applied repeatedly, give

\[
R\Gamma(\mathbf A^N,\Lambda)=\Lambda,
\qquad
R\Gamma_c(\mathbf A^N,\Lambda)=\Lambda(-N)[-2N].
\tag{14.1}
\]

All these tensor factors are rank-one free modules in one degree, so there are no Tor terms, even for composite \(n\). The trace on \(H^{2N}_c(\mathbf A^N,\Lambda(N))\) is the product of the curve traces and sends its coordinate orientation to one. The duality pairing is multiplication between that top group and the ordinary constants. Every other paired degree is zero.

**Example 14.2: projective space.** Use
\(\mathbf P^{N-1}\subset\mathbf P^N\), with complement \(\mathbf A^N\). The compact closed-open triangle, (14.1) and induction give

\[
H^{2i}(\mathbf P^N,\Lambda)=\Lambda(-i)\ (0\leq i\leq N),
\qquad H^{2i+1}(\mathbf P^N,\Lambda)=0.
\tag{14.2}
\]

In degrees below \(2N-1\) restriction to \(\mathbf P^{N-1}\) is an isomorphism; degree \(2N-1\) is zero and degree \(2N\) is the affine top compact group. This spells out every step of the additive computation, rather than assuming the projective bundle theorem.

Let \(h=c_1^{(n)}\mathcal O(1)\in H^2(\mathbf P^N,\Lambda(1))\). A hyperplane Gysin class is \(h\) by Lemma 12.2. Restriction sends it to the preceding hyperplane class. Induction shows \(h^i\) generates every twisted even group with \(i<N\). For the top class, the projection formula gives
\(i_*h_{\mathbf P^{N-1}}^{N-1}=h^N\), and trace compatibility gives \(\operatorname{Tr}(h^N)=1\). Hence it too generates. Thus the twisted even cohomology ring is \(\Lambda[h]/(h^{N+1})\), and the pairs \(h^i,h^{N-i}\) have value one. A root trivialization converts this to the familiar untwisted ring; (14.2) retains its canonical twists.

**Example 14.3: a point in the plane.** For \(i:\{0\}\hookrightarrow\mathbf A^2\), (11.2) gives

\[
Ri^!\Lambda=\Lambda(-2)[-4],
\qquad H^4_{\{0\}}(\mathbf A^2,\Lambda)=\Lambda(-2),
\tag{14.3}
\]

with all other supported degrees zero, because the support is an acyclic point. Its twisted generator maps to the generator of \(H^4_c(\mathbf A^2,\Lambda(2))\), with trace one. Its ordinary image is zero, since \(H^4(\mathbf A^2,\Lambda(2))=0\) by (14.1). Local support, compact support and ordinary cohomology are three different operations in this example.

## 15. Exercises

1. **Easy.** Compute all groups of \(\mathbf P^N\) from its affine-space stratification for every invertible \(n\), and check its duality pairings with twists retained.
2. **Medium.** Show \(H^{2N}(X,\Lambda)=0\) for smooth connected affine \(X\) of dimension \(N\geq1\), using duality and \(H^0_c=0\).
3. **Medium.** Derive smooth-pair purity from the relative smooth upper-shriek formula. State separately the local cohomology sheaves and the global groups with support.
4. **Medium.** Deduce constant-coefficient duality for \(X\times Y\) from duality for \(X,Y\) and Künneth. Justify the Hom–tensor step for composite \(n\), and compute its class-order sign.
5. **Hard.** Let \(X\) be smooth projective of dimension \(N\geq1\), and \(Y\) a smooth hyperplane section. Prove that restriction \(H^i(X,\Lambda)\to H^i(Y,\Lambda)\) is an isomorphism for \(i<N-1\) and injective for \(i=N-1\), using affine vanishing and duality.

## 16. Complete solutions

**Solution 1.** Start with \(\mathbf P^0\), whose only group is \(\Lambda\) in degree zero. The localization sequence for the complement \(\mathbf A^N\) is

\[
\cdots\to H^r_c(\mathbf A^N,\Lambda)
\to H^r(\mathbf P^N,\Lambda)
\to H^r(\mathbf P^{N-1},\Lambda)
\to H^{r+1}_c(\mathbf A^N,\Lambda)\to\cdots.
\tag{16.1}
\]

The affine groups vanish except in degree \(2N\), where the value is \(\Lambda(-N)\). For \(r<2N-1\), both end terms in (16.1) vanish, giving the restriction isomorphism. For \(r=2N-1\), the affine group and the odd group of the hyperplane vanish, so the middle odd group is zero. In top degree, the preceding hyperplane odd group and its degree-\(2N\) group are zero, so the affine top group maps isomorphically to \(H^{2N}(\mathbf P^N,\Lambda)\). Above it everything vanishes by the dimension bound. These statements inductively prove all of (14.2).

With \(h\) as in Example 14.2, the normal-parameter Kummer calculation identifies the hyperplane class with \(h\). Restriction and the projection formula give each \(h^i\) as its twisted degree-\(2i\) generator; successive hyperplane Gysin maps send \(1\) on a point to \(h^N\). Their trace is one by (12.2). Since \(h^ih^{N-i}=h^N\), duality for the coefficients \(F=\Lambda(i)\) in compact degree \(2i\) is multiplication of the two copies of \(\Lambda\), paired with \(F^\vee(N)=\Lambda(N-i)\). For untwisted \(F=\Lambda\), the groups have the twists \((-i)\) and \((i)\) in the two factors, which contract to \(\Lambda\). Odd and out-of-range degrees pair zero with zero. No field-coefficient assumption is involved. \(\square\)

**Solution 2.** A section of a local system has an open-and-closed nonzero locus: on a trivializing étale chart this is the nonzero locus of a locally constant module value, and vanishing descends to the base. On connected \(X\), a nonzero global section therefore has support all of \(X\). A compactly supported degree-zero section must have proper support. A positive-dimensional connected affine scheme of finite type cannot be proper over \(k\), since a proper affine morphism of finite type is finite and its fibre has dimension zero. Thus \(H^0_c(X,\Lambda(N))=0\). Apply (10.3) with \(F=\Lambda(N)\) and \(i=0\): its complementary factor is \(H^{2N}(X,\Lambda)\), the dual of zero, hence zero. The affine vanishing theorem of Lesson 16 also proves this, since \(2N>N\); the requested proof here uses duality. \(\square\)

**Solution 3.** Let \(p_X\) and \(p_Z\) be the two smooth structure maps. The identity \(p_Z=p_Xi\), transposed under the compact adjunctions, is
\(Ri^!Rp_X^!\Lambda=Rp_Z^!\Lambda\).
Their dimensions are \(N\) and \(N-c\). The smooth formula gives
\(Ri^!(\Lambda(N)[2N])=\Lambda(N-c)[2N-2c]\).
Move the invertible twist and the shift through \(Ri^!\), as justified by the closed projection formula, and cancel them. The result is \(Ri^!\Lambda=\Lambda(-c)[-2c]\). Its cohomology sheaves are zero except in degree \(2c\), with value \(\Lambda(-c)\).

Supported global sections are the composite \(R\Gamma(Z,-)Ri^!\). They give \(H^r_Z(X,\Lambda)=H^{r-2c}(Z,\Lambda(-c))\), so \(H^{2c}_Z=H^0(Z,\Lambda(-c))\), and lower degrees vanish. The zero-section example (11.6) has a nonzero higher group. This proves the entire smooth-pair conclusion at its correct scope, including its sheaf and global forms. \(\square\)

**Solution 4.** Put \(A=R\Gamma_c(X,\Lambda)\), \(B=R\Gamma_c(Y,\Lambda)\). Lemma 13.1 proves these are bounded finite-projective complexes, by the compact projection formula with every coefficient module, the degree bound and finite generation. Therefore \(A^\vee\otimes^LB^\vee=(A\otimes^LB)^\vee\), calculated on those projective representatives. This is a justification, rather than an assumption that arbitrary finite modules over \(\mathbf Z/n\) are projective.

The factor dualities give \(R\Gamma(X,\Lambda(N)[2N])=A^\vee\) and the analogous identity for \(Y\). Ordinary Künneth tensors these identities; compact Künneth identifies \(A\otimes^LB\) with the product's compact complex. The product trace is the tensor trace by composition and base change. Thus the resulting map is exactly the evaluation-and-trace duality map for the product, as in (13.3). Taking cohomology and using exact finite \(\Lambda\)-duality makes its group pairings mutually perfect. If compact classes have degrees \(i,j\), move the second compact class past the first ordinary class, whose degree is \(2N-i\). The sign is \((-1)^{j(2N-i)}\), giving (13.4). For composite \(n\) the argument retains the derived tensor and its possible Tor terms throughout. \(\square\)

**Solution 5 (weak Lefschetz).** Set \(U=X-Y\). In the projective embedding, the complement of the chosen hyperplane is affine space and \(U\) is closed in it, hence affine. It is smooth and purely \(N\)-dimensional. Affine vanishing from Lesson 16 gives
\(H^q(U,\Lambda(N))=0\) for \(q>N\).
Duality on \(U\) therefore gives

\[
H^r_c(U,\Lambda)
=H^{2N-r}(U,\Lambda(N))^\vee=0
\quad(r<N).
\tag{16.2}
\]

The exact closed-open sequence on the proper \(X\) contains

\[
H^i_c(U,\Lambda)\longrightarrow H^i(X,\Lambda)
\longrightarrow H^i(Y,\Lambda)
\longrightarrow H^{i+1}_c(U,\Lambda).
\tag{16.3}
\]

If \(i<N-1\), both outer groups vanish by (16.2), so the middle restriction is bijective. If \(i=N-1\), the first group still vanishes, proving injectivity; the last group may be nonzero. This proves precisely the claimed range, including \(N=1\), where the injective map is in degree zero and the isomorphism range is empty for nonnegative degrees. Twisting coefficients preserves the argument. It works for every invertible \(n\), with the same exact coefficient duality used in (16.2). \(\square\)

## 17. Sources and what was actually used

The main historical comparison is P. Deligne, [SGA 4½](https://publications.ias.edu/sites/default/files/Number32.pdf), “Cohomologie étale: les points de départ” [Arcata], VI.3–VI.4. Its formula 6.3.1.1 is an inverse limit under compact traces. Sections 3–7 above expand the local-fibre induction, including uniform refinement, bounded derived maps, and the compact Leray limit. “Dualité,” §4, addresses étale localization of the adjunction counit; Section 8 gives that compatibility directly.

[SGA 4](https://www.normalesup.org/~forgogozo/SGA4/), Exposé XVIII, treats the same material: §§2.9–2.14 for trace and the uniform local criterion, and §§3.1.12–3.2.6 for the adjunction, local presheaves and smooth duality. Section 2 constructs the higher trace by the coordinate method of its §2: curve traces glued along étale coordinates, independence of coordinates through chains of one-coordinate changes, and composition through an interchange square. Nondegeneracy is proved there directly from the curve pairing. Deligne and Boutot, Arcata, VI.2, describe the same normalization of the curve trace. The local criterion, relative identification and global theorem are proved here, rather than imported from the historical higher-dimensional theorem.

The modern construction and support formalism were checked at their full assigned sections and statements:

- [Derived upper shriek, Tags 0G2B–0G2C](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-derived-upper-shriek), and [its local presheaf description, Tag 0GLK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-describe-Rf-upper-shriek). Section 8 proves the construction and its Hom formulas using the categorical Brown foundation and the earlier projection formula.
- [Derived lower shriek by compactification, Tag 0F7H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-derived-lower-shriek-compactification). Its composition and base-change formalism was already proved in Lesson 14 and is used with the actual maps here.
- [Cohomology with support, Tags 09XP, 09XQ, 09XR and 0A45](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-section-cohomology-support). Section 11 constructs the supported triangle and distinguishes its cohomology sheaves from supported global groups.
- [Smooth local acyclicity, Tag 0GJQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-proposition-smooth-locally-acyclic). The exact prerequisite is the proved Theorem 9.1 of Lesson 15; no entire affine fibre is assumed acyclic.
- [Categorical Brown representability, Tags 0F5X–0F5Y](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/injectives.html#injectives-proposition-brown). It is proved there and applied explicitly to construct the adjoint. General constructibility and finiteness are stated in Lesson 14, Section 12, and proved in [Tag 0GL0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-theorem-constructible-shriek) and [Tag 0GLH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-lemma-finiteness-compactly-supported).
- [Weightings and trace maps for locally quasi-finite morphisms, Tag 0GKE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-etale.html#more-etale-section-weightings). Step 4 of Section 2 is its étale case with weighting one, proved there by summation on stalks.
- [Cohomology and limits, Tag 09YQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/etale-cohomology.html#etale-cohomology-theorem-colimit). This is the continuity theorem stated in Lesson 7.

J. S. Milne, [Lectures on Étale Cohomology, version 2.21](https://www.jmilne.org/math/CourseNotes/LEC.pdf), §24, was read in full as a comparison for duality, point normalization and Gysin maps; §§16.7–16.8 were read for the supported-sheaf formulation and normal coordinates. The general-duality proof in that edition is expressly omitted. It supplies comparison statements, not a missing trace construction or a proof substituted for Sections 5–10. Its smooth-pair support spectral sequence agrees with (11.4); its dated discussion of more general absolute purity is not a premise here.

Curve duality in Lesson 17, smooth base change in Lesson 15, and the affine bound and Künneth formula in Lesson 16 are the substantive proved imports. The global trace pairing supplies the duality input for the functional equation in AG-LTF-07. The weak Lefschetz solution provides the prerequisite used in AG-LTF-10. The next lesson compares the resulting étale cohomology with singular cohomology over the complex numbers. The linked AI Integrated Stacks Project reader contains AI-proposed additions and corrections and is not reviewed by the maintainers of the [official Stacks Project](https://stacks.math.columbia.edu/). Writing-AI self-check, source consultation and independent AI review are separate activities.
