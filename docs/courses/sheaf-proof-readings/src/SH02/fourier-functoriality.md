# Moving Fourier kernels across maps and products

Course SH-02. Unit SH02-FF. Original programme text: CC0 1.0 Universal.

The classical bundle-map and base-change statements are compared with Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985), §2.1, Propositions 2.1.5–2.1.6, p. 41](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=44). That section expressly omits proofs. Here one pairing identity constructs the primitive exchange; adjoint mates and ordered orientation evaluation give the remaining maps. The two inverse relative factors are checked by integral rank-one degree tests. Those tests check the displayed inverse factors in rank one and refute the stated alternatives; the general formulas are proved below. They are not claims about an unverified printed formula. The source account at the end compares the actual proof mechanisms and their domains.

## SH02-FF-DOMAINS. Objects, maps, and admissible operations

Fix a commutative unital ring \(k\) of finite global dimension \(g\). Work with all sheaves of \(k\)-modules: stalks may be infinitely generated or have torsion. A bounded-below complex has a single global lower cohomological bound; there is no upper bound unless stated. Our shift convention is \(H^j(K[r])=H^{j+r}(K)\).

A base \(B\) is locally compact Hausdorff. A bundle \(E\to B\) is a real vector bundle of constant finite rank \(n_E\). Statements are local on the base and also apply on components of locally constant rank whenever the resulting functors preserve the asserted global bounds. No finite dimension, manifold structure, compactness, or countability assumption is imposed on \(B\). In particular a theorem below concerning a continuous base map is not restricted to a map of manifolds.

Write \(\mathcal D_E=D^+_{\mathbb R_{>0}}(E;k)\). Conicity means locally constant cohomology along positive scalar orbits, including the fixed zero orbit. We use its proved equivalent, the natural scalar-transport isomorphism on \(E\times\mathbb R_{>0}\), normalized to be the identity at scalar one. See SH02-CON-COMPARISON and SH02-CON-COCYCLE in [Conic descent](conic-descent.md). Pointwise invariance under each fixed dilation, without the parameter-space isomorphism, is not used as a substitute.

All maps are continuous. The symbols \(Rf_!\) and \(Rf_*\) denote different direct images. The former uses sections whose support is proper over the target; none of the arguments replaces it by the latter merely because a fiber is contractible. On locally compact Hausdorff spaces we use proper-support base change, proper-support projection formula, their composition isomorphisms, and \(f^{-1}\dashv Rf_*\).

Whenever \(f^!\) occurs, the proper-support functor \(f_!\) on **sheaves of abelian groups** must have finite cohomological dimension. This is the domain condition for the exceptional inverse image in the imported formalism. It is not inferred just from a chosen coefficient ring. The adjunction is \(Rf_!\dashv f^!\) on \(D^+\). If that condition is absent, identities involving only \(f^{-1},Rf_!,Rf_*\) still apply in their stated domains; an expression containing an unavailable \(f^!\) is not asserted.

For a vector-bundle morphism over the identity of \(B\), this dimension condition is automatic. Its nonempty fibers are affine spaces of dimension at most the source rank. Compact-support cohomology of an arbitrary abelian sheaf on \(\mathbb R^d\) vanishes in degrees greater than \(d\). The proper-support stalk formula therefore bounds the cohomological dimension of the bundle map by its source rank, even if its rank jumps with the base point. The same observation applies to its transpose. For a base-change map, its fibers agree with those of the underlying map of bases, so a finite abelian-sheaf dimension bound for that map supplies the required bound. Alternatively one can impose the bound directly on each exceptional map that occurs.

The foundational imports are SH02-IMP-INVERSE, SH02-IMP-ADJUNCTION, SH02-IMP-TENSOR and the localization imports in [Open prerequisites](open-prerequisites.md). We use the dimension-bounded projection-formula and exceptional-adjunction contracts SH02-KER-IMP-BCPF and SH02-KER-IMP-DUAL in [Kernel calculus](kernel-calculus.md) only within their specified map bounds. Their full base-space hypotheses are not an exact import for the more general ambient spaces here. The following separately typed dependencies therefore remain open at the generality required in this lesson:

### SH02-FF-IMP-BC-LCH — Proper-support base-change contract

Proper-support base change for any cartesian square of locally compact Hausdorff spaces, on \(D^+(k)\), including its stalk formula and naturality, without a finite cohomological-dimension requirement on the map.

### SH02-FF-IMP-COMPOSE-LCH — Proper-support composition contract

The composition isomorphism for proper-support images of arbitrary continuous maps of locally compact Hausdorff spaces on \(D^+\), and its compatibility with base-change pasting.

### SH02-FF-IMP-PF-LCH — Projection-formula contract

The bounded-factor proper-support projection formula over locally compact Hausdorff spaces with finite cohomological dimension of the map, retaining the finite-global-dimension coefficient condition.

### SH02-FF-IMP-EXCEPTIONAL-LCH — Exceptional-adjunction contract

Exceptional adjunction and its transitivity for maps of locally compact Hausdorff spaces whose proper-support functors have finite cohomological dimension on abelian sheaves; the vector-bundle projection formula for its relative orientation object.

The finite-dimensional affine-fiber cohomology bound and the interval-cohomology import SH02-IMPORT-INTERVAL from [Conic descent](conic-descent.md) are also explicit dependencies. These contracts specify what must be proved or matched; the narrower kernel-calculus setting does not close them.

Conic preservation by the four operations is SH02-CON-FUNCTORS. Its proofs for inverse image and both direct images use scalar transport and product-interval base change; those proofs do not use the dimension assumption reserved for exceptional inverse image. Hence they apply also when the underlying base map has no finite dimension bound. In particular no general nonproper base-change theorem for \(Rf_*\) is being inserted.

## SH02-FF-CUT-TRANSPORT. Closed cuts through an arbitrary proper-support image

**Lemma.** For a continuous map \(r:X\to Y\) of locally compact Hausdorff spaces, a closed \(C\subset Y\), and \(A\in D^+(k_X)\), there is a natural isomorphism
\[
(Rr_!A)_C\simeq Rr_!(A_{r^{-1}C}).
\tag{FF0}
\]
It does not require a finite cohomological-dimension bound for \(r_!\).

**Proof.** Let \(i:C\hookrightarrow Y\), \(j:r^{-1}C\hookrightarrow X\), and \(r_C:r^{-1}C\to C\). Closed tensor cutoff is \(i_*i^{-1}\), not local cohomology. Proper-support base change and composition give
\[
i_*i^{-1}Rr_!A
 \simeq i_*R(r_C)_!j^{-1}A
 \simeq Rr_!j_*j^{-1}A.
\]
The first and last expressions are the two sides of FF0. Closed direct images are exact and proper, so these are operations on \(D^+\) with the claimed scope. The maps are the indicated base-change and composition maps. Their naturality also shows that for closed \(D\subset C\) they intertwine the cut restriction \(k_C\to k_D\). \(\square\)

## SH02-FF-BOUNDS. Tensor products of two bounded-below objects

We will need the proper-support projection formula with both inputs in \(D^+\), without assuming either has bounded or finite-rank cohomology. Here is the extension from the bounded-factor version in the prerequisite contract.

**Lemma.** For a map \(r\) with finite proper-support cohomological dimension and \(A,C\in D^+\), the natural comparison
\[
C\otimes^L Rr_!A
 \longrightarrow Rr_!(r^{-1}C\otimes^L A)
\tag{FF1}
\]
is an isomorphism.

**Proof.** Choose lower bounds \(a,c\). Finite global dimension gives
\(A\otimes^L C\in D^{\geq a+c-g}\), as is checked by the stalkwise hyper-Tor spectral sequence. Its finite Tor range also shows that replacing \(A\) by \(\tau_{\leq N}A\) changes either tensor expression only in degrees at least \(N+1+c-g\). Proper-support direct image preserves lower bounds, so this is still true after applying \(Rr_!\). Replacing \(C\) by \(\tau_{\leq N'}C\) similarly changes either side only in degrees at least \(N'+1+a-g\): on the left \(Rr_!A\) has lower bound \(a\).

For any fixed degree \(j\), choose \(N,N'\) so that both bounds exceed \(j+1\). The comparisons between the original morphism FF1 and the doubly truncated morphism induce isomorphisms on cohomology in degrees \(j,j+1\). The truncated inputs are bounded, and the imported projection formula applies. Therefore FF1 induces an isomorphism in degree \(j\). Since \(j\) was arbitrary, its cone is zero. The morphism is the original projection comparison, not a family of unrelated truncation isomorphisms. \(\square\)

The same proof applies to proper-support Künneth maps obtained by combining base change, projection formula, and composition. A pair with lower bounds \(a_1,a_2\) has derived external product bounded below by \(a_1+a_2-g\). This is the only tensor estimate needed for the product theorem.

## SH02-FF-CONVENTIONS. The inverse transform and orientation lines

Let \(\tau_E:E\to B\) and \(\pi_E:E^*\to B\). Denote the relative orientation local system on \(B\) by \(O_E\), and put
\[
W_E=O_E[n_E]\quad\text{on }B.
\]
Its pullback to \(E\) is \(\tau_E^!k_B\). We suppress a base pullback on \(W_E\) only when the ambient space is specified. The dual \(W_E^{-1}=R\mathcal Hom(W_E,k_B)\) is \(O_E^\vee[-n_E]\). This is a tensor inverse, including its shift, not just an ungraded orientation sheaf.

We use the positive dual-orientation identification \(O_{E^*}\simeq O_E\): an oriented basis and its dual basis are both positive. All tensor permutations use the usual Koszul symmetry. In particular interchanging the two pure graded lines \(W_{E_1}^{\pm1}\) and \(W_{E_2}^{\pm1}\) contributes \((-1)^{n_1n_2}\). Evaluation and coevaluation are the tensor–Hom counit and unit. Adjacent inverse factors are contracted by those maps, after the necessary Koszul permutation. This convention specifies maps; it does not declare every permutation of shifted orientation factors to have sign \(+1\).

On \(E\times_BE^*\) write \(p,q\) for the projections and
\[
N_E=\{(x,\xi):\langle x,\xi\rangle\leq0\},
\qquad
C_E=\{(x,\xi):\langle x,\xi\rangle\geq0\}.
\]
For a locally closed subset \(A\), \(H_A=H\otimes k_A\) is restriction with extension by zero. It is different from \(R\Gamma_AH=R\mathcal Hom(k_A,H)\).

The two functors used here are
\[
\begin{aligned}
T_EF&=Rq_!((p^{-1}F)_{N_E}),\\
V_EF&=a_{E^*}^{-1}(T_EF)\otimes\pi_E^{-1}W_E
      \simeq Rq_!((p^{-1}F)_{C_E})\otimes\pi_E^{-1}W_E ,
\end{aligned}
\tag{FF2}
\]
where \(a\) is the antipodal involution. Both go from \(\mathcal D_E\) to \(\mathcal D_{E^*}\). Thus \(V_E\) and \(T_E\) have the same direction, but are not each other's inverses.

The Fourier equivalence in [Fourier kernels](fourier-sato.md), SH02-FS-INVERSION, identifies \(V_E\) with the inverse, and right adjoint, of \(T_{E^*}\); likewise \(V_{E^*}\) is the inverse and right adjoint of \(T_E\). We use the adjunction obtained from the kernel tensor–Hom adjunction in SH02-FS-SETUP. Once a right adjoint is identified with FF2, its unit and counit are transported along that specified identification. All mates below use that adjunction.

The separately prescribed negatively normalized halfspace adjunction is treated in *The geometric normalization of Fourier adjunctions*, SH02-NDF-SOURCE-MAPS; SH02-FS-NORM-OPEN is its historical cross-reference. That theorem proves the paired inverse identities for its specified comparisons. The present identities use the positive dual orientation, the antipode in FF2, the tensor symmetry, and the raw kernel adjunction just fixed. They do not acquire a different adjunction from that later normalization result.

For a bundle map \(f:E_1\to E_2\) over \(B\), let
\[
t={}^{t}f:E_2^*\longrightarrow E_1^*
\]
be its transpose. Define the relative objects, on the indicated source spaces, by
\[
\begin{aligned}
\omega_f=f^!k_{E_2}
 &\simeq \tau_1^{-1}(W_1\otimes W_2^{-1}),\\
\omega_t=t^!k_{E_1^*}
 &\simeq \pi_2^{-1}(W_{2^*}\otimes W_{1^*}^{-1}).
\end{aligned}
\tag{FF3}
\]
In particular their shifts are \(n_1-n_2\) and \(n_2-n_1\), respectively. Their ungraded orientation lines may be identified with their own inverses; their graded dualizing objects usually may not.

Here is a proof of FF3 that also fixes its orientation identification. The equality \(\tau_1=\tau_2f\), exceptional-functor transitivity, and extraction of a base-pulled invertible line give a specified composite
\[
\omega_f\otimes\tau_1^{-1}W_2
 \simeq f^!(\tau_2^{-1}W_2)
 \simeq f^!\tau_2^!k_B
 \simeq\tau_1^!k_B
 \simeq\tau_1^{-1}W_1.
\tag{FF3a}
\]
Define the first identification in FF3 as the unique one which, after tensoring on the right by \(W_2\) and evaluating the adjacent inverse pair, gives FF3a. Tensoring by \(W_2\) is an equivalence, so this both exists and is unique. Apply the same construction to the dual projections and \(t\) for the second identification. This proof does not require a constant-rank kernel, a graph normal-coordinate convention, or a manifold base. It also specifies the maps of relative lines by transitivity, instead of selecting an unsigned isomorphism between their underlying rank-one sheaves.

A formula for \(f^!k\) does **not** assert \(f^!G=f^{-1}G\otimes\omega_f\) for arbitrary \(G\). That latter comparison can fail. The formulas below keep \(f^!\) intact.

## SH02-FF-LINEAR-KERNEL. A single pairing identity supplies the main map

**Theorem.** For \(F\in\mathcal D_{E_1}\), there is a natural isomorphism
\[
A_f(F):t^{-1}T_1F\xrightarrow{\sim}T_2Rf_!F.
\tag{FF4}
\]

**Proof and construction of the map.** Set \(X_i=E_i\times_BE_i^*\), with projections \(p_i,q_i\), and set \(Y=E_1\times_BE_2^*\). Define
\[
u(x,\eta)=(x,t\eta)\in X_1,\qquad
v(x,\eta)=(fx,\eta)\in X_2,
\]
and write \(r:Y\to E_2^*\), \(s:Y\to E_1\). The square \((u,r,q_1,t)\) is cartesian: its fiber product merely chooses \(x\) over the base of \(\eta\). The square \((v,s,p_2,f)\) is also cartesian. Most importantly,
\[
u^{-1}N_1=v^{-1}N_2
 =\{(x,\eta):\langle x,t\eta\rangle=\langle fx,\eta\rangle\leq0\}.
\tag{FF5}
\]
Thus proper-support base change in the first square gives the first isomorphism below; projection formula and base change in the second square give the remaining ones:
\[
\begin{aligned}
t^{-1}T_1F
&\simeq Rr_!\bigl(s^{-1}F\otimes k_{u^{-1}N_1}\bigr)\\
&\simeq Rq_{2!}Rv_!\bigl(s^{-1}F\otimes v^{-1}k_{N_2}\bigr)\\
&\simeq Rq_{2!}\bigl((Rv_!s^{-1}F)\otimes k_{N_2}\bigr)\\
&\simeq Rq_{2!}\bigl(p_2^{-1}Rf_!F\otimes k_{N_2}\bigr).
\end{aligned}
\tag{FF6}
\]
The final term is \(T_2Rf_!F\). Each restriction kernel is a flat degree-zero sheaf; the bounded-factor projection formula already suffices. No properness of \(v,f,q_i\) is asserted. All integrations explicitly use proper supports. This chain defines \(A_f\), and every arrow in it has been identified. \(\square\)

For composable bundle maps \(E_1\xrightarrow{f}E_2\xrightarrow{h}E_3\), \(A_{hf}\) agrees with the successive use of \(A_f,A_h\), under the functor-composition identifications and \({}^{t}(hf)=({}^{t}f)({}^{t}h)\). Indeed both chains expand to proper-support integration on \(E_1\times_BE_3^*\) with the identical restriction
\(\langle hf(x),\zeta\rangle\leq0\). Pasting the two cartesian squares in FF6 gives the square for the composite. The section-level pullback and tensor maps commute under this pasting; their derived maps are the proper-support base-change and projection-formula composition maps in the prerequisite contract. Hence the two maps agree, not just the two resulting objects. For the identity bundle map every square is an identity square, and \(A_{\mathrm{id}}\) is the identity.

## SH02-FF-MATES. The complete bundle-map identities

Here and below all displayed functor identities are on the conic \(D^+\) categories just specified. For \(F\in\mathcal D_{E_1}\), the four identities are
\[
\begin{aligned}
t^{-1}(T_1F)&\simeq T_2(Rf_!F), &(L1)\\
t^!(V_1F)&\simeq V_2(Rf_*F), &(L2)\\
t^!(T_1F)&\simeq T_2(Rf_*F)\otimes\omega_t, &(L3)\\
t^{-1}(V_1F)&\simeq V_2(Rf_!F)\otimes\omega_t^{-1}. &(L4)
\end{aligned}
\tag{FF7}
\]
For \(G\in\mathcal D_{E_2}\), the corresponding four identities are
\[
\begin{aligned}
V_1(f^{-1}G)&\simeq Rt_!(V_2G), &(R1)\\
T_1(f^!G)&\simeq Rt_*(T_2G), &(R2)\\
V_1(\omega_f^{-1}\otimes f^!G)&\simeq Rt_*(V_2G), &(R3)\\
T_1(\omega_f\otimes f^{-1}G)&\simeq Rt_!(T_2G). &(R4)
\end{aligned}
\tag{FF8}
\]
The order of a coefficient twist is part of the displayed formula; moving it past a complex uses tensor symmetry. All twists inside a transform are on its input bundle, and those outside are on its output bundle.

**Proof of the four untwisted identities.** L1 is FF4. Apply FF4 to the transposed map \(t:E_2^*\to E_1^*\). Since the double transpose is \(f\), this gives
\[
f^{-1}T_{2^*}\simeq T_{1^*}Rt_!.
\tag{FF9}
\]
Compose on the right by \(V_2\) and on the left by \(V_1\), and use the specified units and counits of the inverse equivalences. The result is R1.

Take right adjoints of the isomorphism \(T_2Rf_!\simeq t^{-1}T_1\). The right adjoints are, respectively,
\(f^!V_{2^*}\) and \(V_{1^*}Rt_*\). Thus
\[
f^!V_{2^*}\simeq V_{1^*}Rt_*.
\]
Compose on the right by \(T_2\) and on the left by \(T_1\), then use the inverse equivalences. This is R2. Finally the right adjoints of the two sides of FF9 are \(V_2Rf_*\) and \(t^!V_1\). Their mate is L2.

These operations determine actual morphisms. More explicitly, if \(\lambda:P\to Q\) is an isomorphism between left adjoints, its right mate \(Q^R\to P^R\) is the composite
\[
Q^R\longrightarrow P^RPQ^R
 \xrightarrow{P^R\lambda Q^R}P^RQQ^R
 \longrightarrow P^R ,
\tag{FF10}
\]
using the unit for \(P\) and the counit for \(Q\). The mate of \(\lambda^{-1}\) is its inverse by the triangle identities. Formula FF10, together with the named Fourier units and counits, is the convention used in the preceding paragraph. The ordinary and exceptional adjunctions restrict to conic objects because the corresponding functors preserve them. No Verdier biduality or finite-stalk dualization is used.

**Proof of the four orientation rewrites.** Fourier transformation commutes with tensoring by a base-pulled invertible graded line, by projection formula. Ordinary image commutes with that tensor because the line is locally free of rank one in a single degree. Exceptional inverse image commutes with it by adjunction and the same projection formula. All bundle maps commute with antipodes.

Insert \(V_iH=a^{-1}T_iH\otimes W_i\) into L2 and cancel the antipode. This gives
\[
t^!T_1F\otimes W_1\simeq T_2Rf_*F\otimes W_2.
\tag{FF11}
\]
Here is the explicit right-tensor-equivalence extraction defining L3. Denote the map FF11 by \(\widetilde\ell_f\), put \(D_1=R\mathcal Hom(W_1,k)\), and let \(d:\omega_t\otimes W_1\to W_2\) be FF3a for \(t\). Define
\[
j:\omega_t\longrightarrow W_2\otimes D_1,
\qquad
j=(d\otimes1_{D_1})(1_{\omega_t}\otimes\operatorname{coev}_{W_1}).
\tag{FF11a}
\]
Then L3 is the natural map
\[
\ell_f=(1\otimes j^{-1})
(\widetilde\ell_f\otimes1_{D_1})
(1\otimes\operatorname{coev}_{W_1}).
\tag{FF11b}
\]
Tensoring by the invertible line \(W_1\) is an equivalence, and FF11b is exactly its inverse on the displayed map. In particular the initial insertion in FF11b is coevaluation. A later cancellation of the output relative line is a separate map and must specify its order. [The graded support comparison](fourier-graded-comparison.md), SH02-FGC-EXTRACTION, proves that this L3 is \((-1)^{n_2-n_1}\) times the direct LFT17 kernel comparison. SH02-FGC-SUPPORT states the complete support equation with the final braided evaluation explicitly written. This paragraph completes the earlier suppressed line operation; it does not identify a separately implicit antecedent map without a correspondence check.

Likewise L1, with the antipode and then the line \(W_1\) applied, gives
\[
t^{-1}V_1F\simeq a^{-1}T_2Rf_!F\otimes W_1.
\]
Replace \(W_1\) by \(W_2\otimes\omega_t^{-1}\) using the inverse of the same evaluation identification. This is L4. The inverse on \(\omega_t\) is forced.

In R2, apply the antipode and then tensor on the output by \(W_2\), moving that locally free base line through \(Rt_*\). Its other side is
\(a^{-1}T_1f^!G\otimes W_2\).
On the other hand FF2 and FF3 identify
\[
V_1(\omega_f^{-1}\otimes f^!G)
 \simeq a^{-1}T_1f^!G\otimes W_2.
\]
This proves R3. Here the identifications permute the shifted lines as necessary and then evaluate \(W_1^{-1}\otimes W_1\); they include the Koszul signs declared in SH02-FF-CONVENTIONS.

Finally apply FF2 to R1:
\[
a^{-1}T_1f^{-1}G\otimes W_1
 \simeq a^{-1}Rt_!T_2G\otimes W_2.
\]
Cancel antipodes and the line \(W_2\). The remaining input twist is \(W_1\otimes W_2^{-1}=\omega_f\), yielding R4. Thus all eight identities have been constructed and proved. \(\square\)

All eight maps respect composition. For L1 this was checked after FF6. Taking adjoint mates respects pasting: substituting FF10 for two successive transformations cancels the intervening unit–counit pairs by the triangle identities, leaving FF10 for the composite. Conjugating by inverse equivalences has the same property. Finally for \(E_1\xrightarrow{f}E_2\xrightarrow{h}E_3\) the relative lines compose by
\[
(W_1\otimes W_2^{-1})\otimes(W_2\otimes W_3^{-1})
 \longrightarrow W_1\otimes W_3^{-1};
\tag{FF12}
\]
it contracts the middle factors and is associative by the duality triangle identities. The tensor permutations in other orders are the declared Koszul permutations. This proves composition compatibility of the orientation rewrites as well. It makes no claim that an independently normalized Fourier adjunction has already been compared with this one.

## SH02-FF-BASE. Changing the locally compact base

Let \(b:B'\to B\) be any continuous map of locally compact Hausdorff spaces. Form \(E'=B'\times_BE\) and \(E'^*=B'\times_BE^*\), with induced maps
\[
b_E:E'\to E,\qquad b_{E^*}:E'^*\to E^*.
\]
Write \(T'\) for \(T_{E'}\). The four base-change identities are
\[
\begin{aligned}
T'b_E^{-1}F&\simeq b_{E^*}^{-1}T_EF,\\
T_E R(b_E)_!G&\simeq R(b_{E^*})_!T'G,\\
T_E R(b_E)_*G&\simeq R(b_{E^*})_*T'G,\\
T'b_E^!F&\simeq b_{E^*}^!T_EF.
\end{aligned}
\tag{FF13}
\]
Here \(F\in\mathcal D_E\), \(G\in\mathcal D_{E'}\). The final line is asserted when the exceptional inverse images exist in the dimension-bounded formalism of SH02-FF-DOMAINS. A sufficient hypothesis is finite cohomological dimension of \(b_!\) on abelian sheaves.

**Proof.** Set \(X=E\times_BE^*\), \(X'=B'\times_BX\) and \(b_X:X'\to X\), with projections \(p,q,p',q'\). The pairing cut pulls back exactly:
\(N_{E'}=b_X^{-1}N_E\). Both squares formed with \(p,p'\), and with \(q,q'\), are cartesian. Therefore proper-support base change for \(q\), followed by exact inverse image and pullback of the cut, gives
\[
b_{E^*}^{-1}T_EF
 \simeq Rq'_!((p'^{-1}b_E^{-1}F)_{N_{E'}}).
\tag{FF14}
\]
This is the first map of FF13, with its direction reversed.

For the second map, composition of proper-support images gives
\[
\begin{aligned}
R(b_{E^*})_!T'G
&\simeq Rq_!R(b_X)_!
       (p'^{-1}G\otimes b_X^{-1}k_{N_E})\\
&\simeq Rq_!\bigl(R(b_X)_!p'^{-1}G\otimes k_{N_E}\bigr)\\
&\simeq Rq_!\bigl(p^{-1}R(b_E)_!G\otimes k_{N_E}\bigr)
 =T_E R(b_E)_!G.
\end{aligned}
\tag{FF15}
\]
The middle steps use FF0 for the closed cut \(N_E\), and proper-support base change for the square with \(p\). In particular they do not invoke a finite-map-dimension projection formula for \(b_X\). Neither \(b\) nor \(b_E\) needs to be proper.

Take right adjoints of the first identity of FF13. With \(S=V_{E^*}\) and \(S'=V_{E'^*}\), the result is
\[
R(b_E)_*S'\simeq S R(b_{E^*})_*.
\]
Compose with the Fourier equivalences and their specified units and counits. This gives the third identity of FF13. Taking right adjoints of the second identity similarly gives
\(b_E^!S\simeq S'b_{E^*}^!\), and conjugation by the equivalences gives the fourth identity. The maps are FF10 applied to FF14 and FF15. In particular the proof has not used a nonexistent unrestricted ordinary base-change isomorphism for \(Rb_*\).

These operations preserve conicity by the scalar-transport arguments recorded above. Moreover \(W_{E'}=b^{-1}W_E\) under its positive orientation identification. Thus no relative base orientation or rank difference appears in FF13. A general base map may have no invertible relative dualizing complex at all; no such invertibility was assumed. \(\square\)

These maps respect identity and successive base changes: pullback of a pairing inequality is literally successive pullback of the same subset; proper-support base change, tensor, and composition respect cartesian pasting. This proves compatibility first for FF14–FF15 and then for their mates by FF10. The same verification gives compatibility between FF4 and base pullback: the equality \(\langle fx,\eta\rangle=\langle x,t\eta\rangle\) survives base pullback, and both constructions use the resulting identical cartesian diagram.

## SH02-FF-BICONIC. Why two separate cuts can replace one sum cut

This compact-support lemma is the geometric input to the tensor-product theorem.

**Lemma.** Let \(H\in D^+(k_{\mathbb R^2})\) be biconic: each of the two independent positive dilations has the natural scalar-transport isomorphism. Set
\[
C=\{(s,t):s+t\leq0\},\qquad
D=\{(s,t):s\leq0,\ t\leq0\}.
\]
The restriction \(k_C\to k_D\) induces an isomorphism
\[
R\Gamma_c(\mathbb R^2;H_C)
 \xrightarrow{\sim}R\Gamma_c(\mathbb R^2;H_D).
\tag{FF16}
\]
No hypothesis is imposed on \(H\) along the axes or at the origin.

**Proof.** The set \(D\) is closed in \(C\), and \(U=C\setminus D\) is its relatively open complement. The restriction map is part of the canonical localization triangle
\[
H_U\longrightarrow H_C\longrightarrow H_D\longrightarrow H_U[1].
\tag{FF17}
\]
This is the tensor-cut triangle, not the local-cohomology triangle. Stalkwise the underlying sheaf sequence is \(0\to k_U\to k_C\to k_D\to0\).

The complement is the disjoint union of two relatively open-and-closed pieces
\[
U_1=\{0<s\leq-t\},\qquad U_2=\{0<t\leq-s\}.
\]
They lie in the two mixed-sign open quadrants. Biconic transport identifies the restriction of every cohomology sheaf of \(H\) to either quadrant with a constant sheaf: the orbit map of \(\mathbb R_{>0}^2\) through a chosen point is a homeomorphism onto that quadrant, and composing the two parameter-transport isomorphisms trivializes its pullback. This uses parameter transport, not just isomorphic stalks. Each constant coefficient module is arbitrary.

We show \(R\Gamma_c(U_1;M)=0\) for every constant \(k\)-module \(M\). The coordinates
\[
r=s>0,\qquad v=-t/s-1\geq0
\]
identify \(U_1\) with \((0,\infty)\times[0,\infty)\), hence with
\(W=(0,1)\times[0,1)\). Put \(K=[0,1]^2\). Its closed complement
\(A=K\setminus W\) consists of the left, top, and right edges; it is a closed interval, including its corners. The localization sequence on \(K\) is
\[
0\longrightarrow j_!M_W\longrightarrow M_K
 \longrightarrow i_*M_A\longrightarrow0 .
\tag{FF18}
\]
The interval-cohomology theorem gives \(R\Gamma(A;M)=M[0]\). It also gives \(R\Gamma(K;M)=M[0]\): project the square properly onto an interval, apply proper base change and interval acyclicity to the fibers, and then apply interval acyclicity on the base. The restriction map from \(K\) to \(A\) is the identity on constant sections. Taking derived sections in FF18 therefore gives \(R\Gamma_c(W;M)=0\). This holds for all modules, with no finite-generation or flatness assumption. Interchanging the coordinates proves the same assertion for \(U_2\).

Apply the bounded-below compact-support hypercohomology spectral sequence to \(H|_{U_i}\). Every term
\(H_c^p(U_i;H^q(H)|_{U_i})\) is zero by the preceding calculation. It converges in the asserted range: \(q\) has a global lower bound and \(p\geq0\), so only finitely many indices can contribute to each total degree. Thus \(R\Gamma_c(U_i;H|_{U_i})=0\), and the finite disjoint union gives \(R\Gamma_c(U;H|_U)=0\). Now FF17 proves that the actual restriction map FF16 is an isomorphism. \(\square\)

The non-strict diagonal in \(U_1,U_2\) matters. Replacing \(0<s\leq-t\) by \(0<s<-t\) produces an open quadrant in the displayed \((r,v)\) coordinates, with generally nonzero top compact-support cohomology. Axes and the origin lie in both cuts wherever they occur, so their possibly singular coefficient data cancel through the same localization triangle; they were never discarded.

The same compactification proves vanishing for a constant coefficient sheaf on the reflected wedge \(\{0<s\leq t\}\); biconicity supplies constancy on that positive quadrant as well. This reflected wedge is not the first component of \(C\setminus D\). For the particular cut morphism FF16, the minus sign in \(U_1=\{0<s\leq-t\}\) is essential. Thus both the reflected-wedge vanishing and the correct localization complement are accounted for.

There is also a parameter version. If \(P\) is any locally compact Hausdorff space, \(\alpha:P\times\mathbb R^2\to P\), and \(H\in D^+\) is biconic in the two real coordinates, the corresponding restriction
\[
R\alpha_!(H_{\{s+t\leq0\}})
 \longrightarrow R\alpha_!(H_{\{s\leq0,t\leq0\}})
\tag{FF19}
\]
is an isomorphism. Proper-support base change identifies its stalk at every \(p\) with FF16 for \(H|_{\{p\}\times\mathbb R^2}\). Inverse image preserves biconic transport, so the lemma applies. Since the morphism was constructed before taking stalks, stalk detection proves the sheaf isomorphism and includes its gluing over \(P\).

## SH02-FF-PRODUCT. Tensoring before or after transformation

For bundles \(E_1,E_2\) over the same \(B\), let \(E=E_1\oplus E_2=E_1\times_BE_2\). The dual is \(E_1^*\oplus E_2^*\) with pairing the sum of the two pairings. Define
\(F_1\boxtimes_B^L F_2=\operatorname{pr}_1^{-1}F_1\otimes^L\operatorname{pr}_2^{-1}F_2\).

**Theorem.** For arbitrary \(F_i\in\mathcal D_{E_i}\), the natural cut comparison gives
\[
T_E(F_1\boxtimes_B^L F_2)
 \xrightarrow{\sim}
 T_1F_1\boxtimes_B^L T_2F_2.
\tag{FF20}
\]

**Proof.** On
\[
X=(E_1\oplus E_2)\times_B(E_1^*\oplus E_2^*)
\]
write \(Q:X\to E_1^*\oplus E_2^*\), and let \(L\) be the inverse image of \(F_1\boxtimes_B^L F_2\). Put
\(s(x_1,x_2,\xi_1,\xi_2)=\langle x_1,\xi_1\rangle\) and
\(t(x_1,x_2,\xi_1,\xi_2)=\langle x_2,\xi_2\rangle\).
The left side is \(RQ_!L_{\{s+t\leq0\}}\).

The right side is \(RQ_!L_{\{s\leq0,t\leq0\}}\). To check this identification rather than assume it, pull the two transforms to \(E_1^*\times_BE_2^*\) by proper-support base change. Multiply them there. Apply FF1 to move the second factor under the first proper-support image, apply base change to pull the second image to that integration space, and apply FF1 again to combine the integrands. Composition of proper-support images then gives \(RQ_!\) of the tensor of the two input pullbacks and the two flat cut kernels. Their kernel tensor is exactly \(k_{\{s\leq0,t\leq0\}}\), and their coefficient tensor is \(L\). This is the proper-support Künneth map, specified as the composite of those three operations. The lower-bound estimate in SH02-FF-BOUNDS makes every tensor and image an object of \(D^+\), even if both inputs are unbounded above.

Now factor \(Q=\alpha\beta\), where
\[
\begin{aligned}
\beta:X&\longrightarrow
 (E_1^*\oplus E_2^*)\times\mathbb R^2,\\
(x_1,x_2,\xi_1,\xi_2)&\longmapsto(\xi_1,\xi_2,s,t),
\end{aligned}
\]
and \(\alpha\) forgets the last two coordinates. The coefficient object \(L\) is conic separately in \(x_1,x_2\), by the external-product transport in SH02-CON-FUNCTORS. The map \(\beta\) intertwines these scalings with independent scalings of \(s,t\). Proper-support scalar base change therefore makes \(H=R\beta_!L\) biconic in \(s,t\). It is bounded below; \(\beta_!\) is a left exact functor and its right derived functor preserves a lower bound.

Closed-cut transport FF0 gives
\[
\begin{aligned}
RQ_!L_{\{s+t\leq0\}}&\simeq
 R\alpha_!H_{\{s+t\leq0\}},\\
RQ_!L_{\{s\leq0,t\leq0\}}&\simeq
 R\alpha_!H_{\{s\leq0,t\leq0\}} .
\end{aligned}
\]
Their comparison is FF19. Consequently it is an isomorphism, proving FF20 with its actual restriction map. \(\square\)

For three factors, both iterated maps FF20 are restriction from
\(\{s_1+s_2+s_3\leq0\}\) to \(\{s_1\leq0,s_2\leq0,s_3\leq0\}\), with the intermediate block inequalities imposed in the two possible orders. Restriction maps compose transitively, and the proper-support Künneth maps respect associativity of tensor and composition. Thus the two maps agree under the associators. Interchanging two bundles interchanges the two inequalities; the resulting square commutes with the usual tensor symmetry, including the Koszul signs of the input complexes. No orientation twist is added to FF20. For a rank-zero factor the transform is the identity on \(D^+(B;k)\); both cuts impose the same inequality and FF20 reduces to projection formula. These verifications provide the unit, associativity, and symmetry compatibilities of this product comparison.

## SH02-FF-CORRECTIONS. Two degree tests for inverse relative factors

Take any nonzero commutative ring of finite global dimension, for example \(k=\mathbb Z\). Let \(f:0\to\mathbb R\) be the zero-section inclusion over a point, and let \(t:\mathbb R^*\to0\). Give \(\mathbb R\) its usual orientation. The definitions or the rank-one cone computation give
\[
V_0k=k,\qquad
V_{\mathbb R}k_{\{0\}}=k_{\mathbb R^*}[1],\qquad
V_{\mathbb R}k_{\mathbb R}=k_{\{0\}},\qquad
\omega_f=k[-1],\quad \omega_t=k_{\mathbb R^*}[1].
\tag{FF21}
\]

First take \(F=k\) on the zero bundle. The left side of L4 is \(k_{\mathbb R^*}\). Its corrected right side is
\(k_{\mathbb R^*}[1]\otimes k_{\mathbb R^*}[-1]=k_{\mathbb R^*}\).
Using \(\omega_t\) in place of \(\omega_t^{-1}\) would give
\(k_{\mathbb R^*}[2]\), which is not isomorphic to \(k_{\mathbb R^*}\).

Next take \(G=k_{\mathbb R}\). Then \(f^!G=k[-1]\), while
\(Rt_*V_{\mathbb R}G=k\). The corrected left side of R3 is
\(V_0(k[1]\otimes k[-1])=k\).
Using \(\omega_f\) in place of \(\omega_f^{-1}\) would give \(k[-2]\). This is a second failure, in the opposite shift direction. Over the zero ring all these objects vanish, so that ring cannot detect the error; the identities themselves still make sense there.

These tests concern the explicit alternatives just written: replacing an inverse relative factor by the relative factor itself changes the cohomological degree. They retain their force independently of any printed convention elsewhere.

## SH02-FF-EXAMPLES. Uses that retain the general hypotheses

**A rank-jumping family.** Let \(B=\mathbb R\), \(E_1=E_2=B\times\mathbb R\), and \(f(b,x)=(b,bx)\). This is a bundle morphism whose kernel rank jumps at \(b=0\); there is no kernel subbundle near that point. For any \(M\in D^+(B;k)\), let \(i:B\to E_1\) be the zero section and \(F=i_*M\). Since \(f\circ i\) is the target zero section \(i'\), one has \(Rf_!F=i'_*M\). Therefore L1 identifies
\[
t^{-1}T_1(i_*M)=\pi_2^{-1}M
 =T_2(i'_*M).
\]
This follows directly from \(T(i_*M)=\pi^{-1}M\). It verifies that the theorem applies through the rank jump with arbitrary base coefficient data.

**Orientation on a nontrivial line bundle.** Let \(L\to S^1\) be the Möbius line bundle, \(i:S^1\to L\), and \(p:L^*\to S^1\). For \(M\in D^+(S^1;\mathbb Z)\),
\[
V_L(i_*M)=p^{-1}(M\otimes O_L)[1],\qquad
\omega_p=p^{-1}O_L[1].
\]
In L4 the inverse relative factor cancels both the orientation and the shift, giving \(p^{-1}M\). With \(M=\mathbb Z/6\), the orientation monodromy is multiplication by \(-1\), which is not trivial modulo six. Thus the cancellation must be done with an actual local system and not just an integer degree.

**A derived external product with torsion.** Over a point, take \(k=\mathbb Z\),
\(F_1=(\mathbb Z/3)_{[0,\infty)}\) on the first real line and
\(F_2=(\mathbb Z/6)_{[0,\infty)}\) on the second. The integral coefficient ring satisfies the standing hypothesis. The external product has both tensor and Tor coefficient contributions: its coefficient complex has \(\mathbb Z/3\) in degrees \(0\) and \(-1\). The rank-one closed-ray transform changes each closed positive ray to the open positive ray. Consequently FF20 gives the derived coefficient complex on the open positive quadrant. The Tor contribution survives in degree \(-1\); replacing the external product by an underived tensor would lose it.

## SH02-FF-PROBLEMS. Problems and complete solutions

**Problem 1.** For a projection \(f:L\oplus M\to M\) of real vector spaces of dimensions \(\ell,m\), compute both sides of L1 for the constant sheaf \(k_{L\oplus M}\), retaining orientation lines.

**Solution.** Proper-support integration along \(L\) gives
\(Rf_!k_{L\oplus M}=k_M\otimes O_L[-\ell]\).
Transforming the constant sheaf on \(M\) gives
\(k_{\{0\}\subset M^*}\otimes O_M[-m]\), so the right side is
\(k_{\{0\}\subset M^*}\otimes O_L\otimes O_M[-\ell-m]\), with the product order fixed as \(L\) followed by \(M\).
The transpose \(t:M^*\hookrightarrow L^*\oplus M^*\) has inverse image of the zero-supported transform of \(k_{L\oplus M}\) equal to exactly this object. It is the restriction of a zero-supported sheaf, so no costalk or additional codimension shift appears on the left. The order \(O_L\otimes O_M\) agrees with the product orientation of \(L\oplus M\).

**Problem 2.** Show that diagonal conicity alone cannot replace biconicity in FF16.

**Solution.** Let \(H=k_{\{s>0,t=-2s\}}\), with extension by zero from that locally closed ray in \(\mathbb R^2\). It is conic for simultaneous positive scaling. Its support lies entirely in \(\{s+t\leq0\}\) and misses \(\{s\leq0,t\leq0\}\). Hence the first term of FF16 is \(k[-1]\), by compact-support integration on an open ray, while the second is zero. Independent scaling moves the supporting ray, so \(H\) is not biconic. This counterexample identifies exactly the extra invariance used in the mixed-quadrant argument.

**Problem 3.** Let \(b:B'\hookrightarrow B\) be an open inclusion with both spaces locally compact Hausdorff, and \(G\in\mathcal D_{E'}\). Interpret the second and third lines of FF13 and explain why they can give different answers.

**Solution.** The second line says that Fourier transformation commutes with extension by zero in the base, since \((b_E)_!\) is exact for an open inclusion. The third says that it commutes with the derived ordinary direct image from that open base. Those direct images have different boundary behavior. For instance take \(B=\mathbb R\), \(B'=(0,\infty)\), a rank-zero bundle, and \(G=k_{B'}\). Its extension by zero has stalk zero at the origin. Its ordinary derived direct image has stalk \(k\) there: sections on sufficiently small positive intervals are \(k\) and higher interval cohomology vanishes. Rank zero makes Fourier transformation the identity, so FF13 preserves this distinction visibly.

**Problem 4.** Verify the correction shifts without choosing an orientation of the target line.

**Solution.** For a one-dimensional vector space \(L\), the formulas become
\(V_Lk_{\{0\}}=k_{L^*}\otimes O_L[1]\),
\(\omega_{L^*\to0}=O_{L^*}[1]\),
and \(\omega_{0\to L}=O_L^\vee[-1]\).
Positive dual orientation identifies \(O_{L^*}\) with \(O_L\), and evaluation contracts an orientation line with its dual. L4 therefore requires a shift \([-1]\) to cancel \([1]\), independently of a generator. R3 likewise requires \([1]\) to cancel the costalk shift \([-1]\). Replacing an orientation generator by its negative affects both paired factors, so the evaluation and the conclusion are unchanged. This shows that the two-degree defects are not removable by changing orientation signs.

## SH02-FF-SOURCES. Statement comparison and the constructed exchange maps

Astérisque 128, §2.1, begins on p. 39 by stating that its Fourier results are recalled without proofs. Proposition 2.1.5(i), p. 41, is the proper-support/transpose-inverse-image identity underlying FF4; part (ii) is the extraordinary-inverse-image/transpose-ordinary-image identity underlying R2. Proposition 2.1.6 states the four base-map identities. These are precise comparisons for the classical statements. They do not supply the maps, composition checks, tensor estimates or orientation cancellations proved in this reading, and they are not evidence for an erratum about either inverse factor.

The foundational comparison is with Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §§4.4–4.6, pp. 90–96](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=90). Theorem 4.5.3 proves proper-support base change on the bounded-below category using sheaves soft along fibers. Theorem 4.4.7 proves projection formula with bounded source input, using a bounded proper-image-acyclic resolution and an almost-free resolution of the other factor. Proposition 4.5.6 obtains bounded Künneth by base change, projection formula and composition. Theorem 4.6.1 and Corollary 4.6.2 give exceptional adjunction and transitivity under finite cohomological dimension; their proof uses a separate representability theorem. These passages specify meaningful operation comparisons, while the exact contracts SH02-FF-IMP-BC-LCH through SH02-FF-IMP-EXCEPTIONAL-LCH retain their own programme closure obligations.

FF0 transports the closed pairing cut through proper-support image using its closed inclusion and base change. This is why the unrestricted base-map argument does not require an unavailable dimension-bounded projection formula. FF1 then gives the degreewise two-truncation argument needed when both coefficient objects are bounded below but unbounded above. The two cartesian squares in FF6 identify one literal pairing cut; FF10 takes its specified adjoint mates. FF3a and FF11a–FF11b determine the orientation-line maps by transitivity and coevaluation. Object-level Fourier equivalence alone does not determine those arrows.

Schapira's [§4.9, pp. 100–101](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=100), gives the proper kernel transform, its tensor–Hom right adjoint and graph-kernel descriptions of the four sheaf operations. That section works with bounded kernels on spaces of finite soft dimension. It is a comparison for the adjunction mechanism, not an import of every formula here at the more general base and coefficient bounds. Its associativity discussion leaves details and higher compatibility checks to the reader; FF6, FF10 and FF12 retain the actual pasting and ordered evaluation checks used here.

The product argument has an additional geometric step. FF16 separates the two mixed-sign wedges, compactifies each by three edges of a square, and computes the restriction map with arbitrary coefficient modules. FF19 constructs the parameterized map before testing stalks. FF20 combines that cut comparison with the bounded-below Künneth construction, then checks the associator, symmetry and rank-zero unit. Neither the statement-only Astérisque passage nor the bounded sphere-bundle inversion proof in Schapira's §5.4 substitutes for this biconic argument. The rank-jumping, nonorientable, torsion and diagonal-conic counterexamples test the hypotheses and ordered factors used in these proofs.

The teaching order follows those local tasks: operation bounds, primitive exchange, adjoint mates, base change, biconic geometry, degree tests and solved problems. The cited passages share standard mathematical constructions, but they do not present this sequence of complete course-map comparisons. Independently expressed programme text is CC0; genuine human components retain their recorded terms.

## SH02-FF-BOUNDARY. Verified content and remaining dependencies

This draft supplies the four continuous-base-map identities, all eight linear-bundle-map identities with the two inverse relative factors checked by degree tests, their specified base-change and adjoint-mate morphisms, their composition compatibilities, the biconic cut lemma including its boundary and arbitrary coefficient cases, and the derived external-product theorem with unit, associativity, and symmetry checks.

Proof closure remains relative to the named proper-support, exceptional-adjunction/transitivity, bundle-orientation, interval-cohomology, conic-transport, and Fourier-equivalence dependencies. In particular the separately proved Fourier adjunction-normalization comparison does not replace the raw adjunction or any operation contract used here. This unit makes no completion claim for specialization, microlocal Hom, microsupport, involutivity, or the complete course.
