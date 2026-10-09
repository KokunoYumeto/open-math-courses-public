# SH02-DA-UNIT — Supports, characteristic classes, and finite duality

Status: independently authored English draft. Every result below is conditional on the precise sheaf-operation contracts cited in its proof.

The map that forgets a support condition can carry useful geometric information even when its source and target have very simple cohomology. This lesson studies that map for vector bundles, sphere bundles, quadratic regions, and accumulating supports. It also explains why the finiteness condition in sheaf biduality produces finite-dimensional global duality on a compact manifold.

## SH02-DA-CONVENTIONS — Coefficients and imported results

Unless a paragraph explicitly assumes a field, let $k$ be a commutative unital ring of finite global dimension. Spaces are locally compact Hausdorff. Manifolds have finite dimension, are countable at infinity, and have no boundary; a submanifold is locally a standard coordinate subspace. A vector-bundle base is a manifold, or more generally a locally compact Hausdorff space for which the finite-dimensional relative operation contracts below hold. No orientability or finiteness of coefficient modules is implicit. The zero ring makes every sheaf zero, so assertions about sharp dimensions assume $k\ne0$.

We use cohomological grading, so $k[-r]$ is in degree $r$. For a locally closed subset $S\subset X$, $k_S$ means the constant sheaf on $S$ extended by zero to $X$. In particular, an open inclusion uses $j_!$, and it must not be replaced by $j_*$. Write

$$
D_XF=R\mathcal Hom(F,\omega_X),\qquad
D'_XF=R\mathcal Hom(F,k_X).
$$

The manifold-duality lesson supplies the dimension bounds `SH02-MD-DIMENSION`, the oriented Euclidean calculation `SH02-MD-EUCLIDEAN`, the submersion formula `SH02-MD-SUBMERSION`, the closed-submanifold formula `SH02-MD-CLOSED`, and trace compatibility `SH02-MD-TRACE`. The sign line $o(E)$ of a real bundle is obtained from its integral orientation line by extension of coefficients; its canonical square pairing identifies $o(E)^{\otimes2}$ with $k$.

The [exceptional-operation lesson](../../sheaf-proof-readings/SH02-exceptional-operations.html) supplies projection, composition, proper-support base change, localization, and the actual dual-sections adjunction in `SH02-EX-DUAL-SECTIONS`. Its support-forgetting map is the natural transformation `SH02-EX-SUPPORT-ERASURE`. The [local-finiteness lesson](../../sheaf-proof-readings/SH02-cohomological-biduality.html) supplies `SH02-CB-SYSTEMS`, `SH02-CB-BIDUALITY`, and `SH02-CB-EXTERNAL-HOM`. The words *cohomologically constructible* below mean that precise local ind/pro representability and perfectness condition; they do not mean that a finite stratification has been supplied.

The remaining sheaf foundations are exact filtered stalk colimits, closed direct image, injective resolutions, acyclicity of soft sheaves on paracompact Hausdorff spaces, and the localization sequence. The smooth part identifies its additional analytic foundation explicitly.

## SH02-DA-COUNITS — A trace equivalence with variable coefficients

Let $f:Y\to X$ be a topological submersion of fixed finite fiber dimension. Suppose its integral trace is an isomorphism

$$
Rf_!\omega_f^{\mathbb Z}\longrightarrow\mathbb Z_X.
$$

Equivalently, by `SH02-MD-ACYCLIC-SUBMERSION`, every fiber has constant-section unit $\mathbb Z\to R\Gamma(Y_x;\mathbb Z)$ an isomorphism. Then for every $F\in D^+(k_X)$ the exceptional counit is an isomorphism

$$
\epsilon_F:Rf_!f^!F\xrightarrow{\sim}F.
$$

**Proof.** Coefficient change for submersions and projection identify the trace with $Rf_!\omega_f\to k_X$. The submersion tensor map and the projection map give

$$
Rf_!f^!F
\simeq Rf_!(\omega_f\otimes^Lf^{-1}F)
\simeq (Rf_!\omega_f)\otimes^LF.
$$

Under these identifications, $\epsilon_F$ is $\epsilon_k\otimes\mathrm{id}_F$. Indeed, the submersion tensor map is defined as the mate of projection followed by $\epsilon_k$; applying the adjunction counit returns that defining map. Thus this is the actual counit, with its shift and orientation factor, and it is invertible. The finite fiber dimension and finite global dimension retain the stated $D^+$ range. No reflexivity of $F$ is used. $\square$

## SH02-DA-THOM — The supported generator of a vector bundle

Let $\pi:E\to B$ have rank $r$, with zero section $i:B\hookrightarrow E$. Choose an orientation $o(E)\simeq k_B$. The relative formulas give

$$
i^!k_E\simeq k_B[-r],\qquad
R\pi_!k_E\simeq k_B[-r],\qquad
k_B\xrightarrow{\sim}R\pi_*k_E.
$$

The first two identifications use the same ordered local orientation. The third is the ordinary adjunction unit: vector-space fibers satisfy the acyclicity condition of `SH02-MD-ACYCLIC-SUBMERSION`.

There is consequently a canonical, orientation-dependent isomorphism

$$
H^a(B;k)\xrightarrow{\sim}H_B^{a+r}(E;k).
$$

Let $u_E\in H_B^r(E;k)$ be the image of the constant section $1$. This definition works componentwise when $B$ is disconnected. It also includes rank zero, where $i$ is the identity and $u_E=1$.

**Proof and normalization.** Closed-support adjunction identifies

$$
R\Gamma_B(E;k_E)=R\Gamma(B;i^!k_E)
\simeq R\Gamma(B;k_B)[-r].
$$

Locally on $B$, the comparison from point support in a fiber to compact support in that fiber is the isomorphism in `SH02-MD-EUCLIDEAN`. Both generators are the ordered product of the one-dimensional endpoint-difference generators. Thus the map

$$
R\pi_!R\Gamma_B k_E\longrightarrow R\pi_!k_E
$$

is the identity on $k_B[-r]$ under the displayed identifications. This checks the map, not merely its one-dimensional stalks up to an unspecified unit. Compatibility of the closed and submersion traces makes these local identifications glue. $\square$

Without an orientation the corresponding statement has $o(E)$ in place of $k_B$ on the right-hand base complex. An untwisted generator $1$ then requires an orientation choice.

## SH02-DA-EULER — What remains after support is forgotten

Apply the natural transformation $R\pi_!\to R\pi_*$ to $k_E$. With the identifications just fixed it is a morphism

$$
e_E:k_B[-r]\longrightarrow k_B.
$$

Its class in $\operatorname{Hom}(k_B,k_B[r])=H^r(B;k)$ is the Euler class. For every $a$, the induced map $H^a(B;k)\to H^{a+r}(B;k)$ is multiplication by this class. The equality follows from the projection formula: the supported generator with coefficients in a class $v$ is $\pi^{-1}v\smile u_E$, and forgetting supports respects that product.

The map $e_E$ is also obtained by forgetting the support of $u_E$ and restricting to the zero section:

$$
H_B^r(E;k)\longrightarrow H^r(E;k)
\xrightarrow{i^*}H^r(B;k),\qquad u_E\longmapsto e(E).
$$

**Proof.** The complex $R\Gamma_Bk_E=i_*i^!k_E$ has support proper over $B$. For this complex, $R\pi_!\to R\pi_*$ is the identity after both sides are identified with $i^!k_E$. Naturality of support-forgetting gives the commutative square

$$
\begin{array}{ccc}
R\pi_!R\Gamma_Bk_E&\longrightarrow&R\pi_!k_E\\
\downarrow\wr&&\downarrow\\
R\pi_*R\Gamma_Bk_E&\longrightarrow&R\pi_*k_E.
\end{array}
$$

The top arrow is the identity on the oriented $k_B[-r]$ by `SH02-DA-THOM`. The bottom arrow forgets support. Finally $i^*$ is inverse to the ordinary unit for $\pi$, since $\pi i=\mathrm{id}_B$. This proves the asserted identification of classes and maps. $\square$

**Vanishing criterion.** If $E$ admits a continuous section $s$ whose value is never zero, then $e(E)=0$.

**Proof.** The ordinary image of $u_E$ restricts to zero on $E\setminus i(B)$ by the localization triangle. Hence its pullback along $s$ is zero. The maps $s$ and $i$ are homotopic through $s_t(b)=t s(b)$. Constant-sheaf cohomology is homotopy invariant for this homotopy: projection $B\times[0,1]\to B$ is proper with contractible compact fibers, so its ordinary unit is an isomorphism by proper base change; both endpoint pullbacks are its inverse. Thus $s^*=i^*$ on ordinary cohomology. The preceding formula gives $e(E)=0$. $\square$

For rank zero over a nonempty base, a nowhere-zero section does not exist, consistently with $e(E)=1\in H^0(B;k)$.

## SH02-DA-GYSIN — Removing a closed submanifold

Let $i:M\hookrightarrow X$ be a closed submanifold of codimension $c$. Choose a trivialization of the normal orientation line, so $i^!k_X\simeq k_M[-c]$. Put $j:X\setminus M\hookrightarrow X$. There is a distinguished triangle

$$
i_*k_M[-c]\longrightarrow k_X\longrightarrow Rj_*k_{X\setminus M}
\longrightarrow i_*k_M[1-c].
$$

It gives, for every integer $a$, the exact sequence

$$
\cdots\to H^a(M;k)\xrightarrow{i_!}
H^{a+c}(X;k)\longrightarrow H^{a+c}(X\setminus M;k)
\longrightarrow H^{a+1}(M;k)\to\cdots.
$$

Here $i_!$ denotes this cohomological Gysin map. Its definition is the supported adjunction map $i_*i^!k_X\to k_X$, so it is available without compactness of $M$ or orientability of $X$. The image of $1$ is the ambient cohomology class of the oriented normal cycle. Its pullback to $M$ is a different class; when the embedding is the zero section of an oriented vector bundle, that pullback is precisely `SH02-DA-EULER`.

**Proof.** For an injective resolution of $k_X$, sections supported on $M$ form the kernel of restriction to the complementary open set. Deriving gives the closed-support localization triangle. Closed adjunction identifies its first term with $i_*i^!k_X$, and the normal orientation formula identifies this with $i_*k_M[-c]$. Apply derived global sections and its long exact cohomology sequence. All arrows are therefore the stated natural arrows. $\square$

Without a normal orientation, replace $k_M$ in the first and last terms by the normal orientation line. For $c=0$, $M$ is both open and closed and the triangle is the direct decomposition by its two components.

## SH02-DA-SPHERES — The two cohomology layers of a sphere bundle

Let $f:Y\to X$ be a locally trivial sphere bundle with fiber $S^m$, where $m\ge1$. Write $L$ for the rank-one sign local system whose transition on an overlap is the degree of the corresponding sphere homeomorphism. There is a canonical distinguished triangle

$$
k_X\xrightarrow{\eta}Rf_*k_Y\longrightarrow L[-m]
\xrightarrow{\delta}k_X[1].
$$

Moreover $L\simeq f_*o_f$. Thus the third term can be written $f_*o_f[-m]$. The map $\eta$ is the constant-section unit, and $\delta$ is an extension class. The triangle does not assert that this class vanishes.

**Proof.** The bundle is proper. On a trivializing open set, proper base change and the constant-coefficient sphere calculation give $R^0f_*k_Y=k_X$, $R^mf_*k_Y=L$, and zero in all other degrees. The degree-zero assertion uses connectedness of $S^m$. The identification of $R^m$ is fixed by the compact-support generator and changes by the degree sign on a transition homeomorphism. The canonical truncation triangle for a complex with cohomology only in degrees $0,m$ gives the displayed triangle. Its first arrow agrees with $\eta$ because both induce the identity in degree zero.

For the orientation statement, the relative orientation line is constant along each sphere fiber and has transition equal to the same degree sign. Hence evaluation gives $f^{-1}L\simeq o_f$; applying $f_*$ and using connected fibers gives $L\simeq f_*o_f$. This also identifies the top cohomology map using the relative trace pairing. $\square$

The sphere cohomology calculation used here follows from the decomposition into two balls with an annular overlap, or from the boundary of the oriented Euclidean ball; its degree-zero generator is the constant section and its top generator is the boundary orientation. For $S^0$, the degree-zero sheaf has rank two, so the connected-fiber triangle above is not its formula.

**Relation to Euler classes.** Suppose $Y=S(E)$ is the sphere bundle of a metrized oriented bundle $E\to X$ of rank $m+1$. Then $L=k_X$. Identify the top layer by the boundary connecting map of the disk bundle. With the standard rotation convention for distinguished triangles, the last morphism is then $\delta=-e_E[1]$. Reversing the identification of the top layer changes this sign as well.

Indeed, for the disk bundle $D(E)$, the open interior inclusion and boundary restriction give the relative triangle. Proper pushforward along the disk projection identifies its middle term with $k_X$, its first term with $k_X[-m-1]$ by the fiber compact-support generator, and its third term with $Rf_*k_{S(E)}$. The first map is the support-forgetting map defining $e_E$: fiberwise radial identification of the disk interior with $E$ carries the ordered compact-support class to the Thom class. A triangle $A\xrightarrow{e_E}B\to C\to A[1]$ rotates to $B\to C\to A[1]\xrightarrow{-e_E[1]}B[1]$. This gives both the sphere triangle and the stated sign. Its vanishing is independent of that orientation convention.

## SH02-DA-QUADRATIC — Closed quadratic regions, including null directions

Let $V=P\oplus N\oplus K$ be an orthogonal decomposition of a real vector space, and let

$$
q(u,v,w)=\lVert u\rVert^2-\lVert v\rVert^2.
$$

Every real quadratic form has this form after a linear change of variables, with $K$ its kernel. Set $p=\dim P$, $e=\dim N+\dim K$, $n=p+e$, and $C_t=\{q\le t\}$. Denote by $o_{N\oplus K}$ and $o_P$ the orientation lines of the indicated vector spaces. There are isomorphisms

$$
R\Gamma_c(V;k_{C_t})\simeq
\begin{cases}
o_{N\oplus K}[-e],&t\ge0,\\
0,&t<0,
\end{cases}
$$

and

$$
R\Gamma_{C_t}(V;k_V)\simeq
\begin{cases}
o_P[-p],&t\ge0,\\
0,&t<0.
\end{cases}
$$

Orientations identify the displayed lines with $k$. Retaining the lines records how these choices change. Notice that null directions contribute to $e$, and the threshold $t=0$ belongs to the nonzero case.

**Proof.** Projection $h:C_t\to N\oplus K$ is proper onto

$$
B_t=\{(v,w):\lVert v\rVert^2+t\ge0\}.
$$

For a compact subset of $B_t$, the coordinates $v,w$ are bounded and $\lVert u\rVert^2\le\lVert v\rVert^2+t$ bounds $u$ as well; closedness then proves properness. Every nonempty fiber is a closed ball in $P$, possibly a point. Its ordinary cohomology is $k$ in degree zero by the compact-convex calculation. Proper base change therefore identifies the actual constant-section map $k_{B_t}\to Rh_*k_{C_t}$ with an isomorphism. Composition gives

$$
R\Gamma_c(C_t;k)\simeq R\Gamma_c(B_t;k).
$$

If $t\ge0$, $B_t=N\oplus K$, so the Euclidean compact-support calculation gives the first formula. If $t<0$ and $N=0$, then $B_t$ is empty. Otherwise

$$
B_t\simeq S(N)\times[\sqrt{-t},\infty)\times K.
$$

The compact-support cohomology of a closed ray is zero. To check the endpoint, compactify it to a closed interval; its constant sheaf and the sheaf of its added endpoint both have ordinary cohomology $k$, and restriction is the identity. Localization thus makes the compact-support cohomology of the remaining half-open interval zero. The product projection formula now gives $R\Gamma_c(B_t;k)=0$ without a field assumption.

For the supported formula, dual sections give

$$
R\Gamma_{C_t}(V;\omega_V)
\simeq R\operatorname{Hom}_k(R\Gamma_c(C_t;k),k).
$$

Use $\omega_V=o_V[n]$, the canonical square pairing for orientation lines, and the ordered identification $o_V=o_P\otimes o_{N\oplus K}$. The nonzero answer becomes $o_P[e-n]=o_P[-p]$; the zero answer stays zero. No biduality theorem for $k_{C_t}$ is needed. $\square$

For example, take $q$ on $\mathbb R^6$ with two positive, one negative, and three null directions. Every nonnegative closed sublevel has compact-support cohomology concentrated in degree four and supported cohomology of the ambient constant sheaf concentrated in degree two. Negative closed sublevels have neither. Replacing the closed inequality by an open inequality changes the boundary calculation and is not covered by this formula.

## SH02-DA-COMPACT-IMAGES — Finite information passes through a compact subset

Let $k$ be a field, let $X$ be a manifold, and let $F\in D^b(k_X)$ have the ordinary local stabilization and perfect-stalk properties in `SH02-CB-SYSTEMS`. The compact-support stabilization property is not needed for this result. For a compact subset $K\subset X$ and an open neighborhood $U$ of $K$, every restriction

$$
H^j(U;F)\longrightarrow H^j(K;F|_K)
$$

has finite-dimensional image. Neither of the two groups has to be finite-dimensional.

**Proof.** First record what local stabilization supplies. If $x\in V$ with $V$ open, the isomorphism of the neighborhood ind-system with the constant perfect object $F_x$ implies that there is a smaller open neighborhood $W$ of $x$ for which

$$
R\Gamma(V;F)\longrightarrow R\Gamma(W;F)
$$

factors through $F_x$ in $D(k)$. Indeed, the inverse map from the constant ind-object is represented at one neighborhood; the equality of its composite with the identity holds after passing to a sufficiently small further neighborhood. This is the defining equality of morphisms in an ind-category. In particular, the restriction has finite-dimensional image in every cohomological degree. Finitely many prescribed neighborhoods $V$ can be handled at once by shrinking $W$ again.

We next show that any finite open cover $(U_i)$ of $K$ admits a finite refinement $(V_a)$, still covering $K$, whose Čech refinement maps have finite-dimensional image on the cohomology of each intersection. All open sets here are open in $X$; a cover of $K$ therefore covers an open neighborhood of $K$ as well.

Choose compact subsets $K_i\subset K\cap U_i$ with $\bigcup_iK_i=K$. Such a closed shrinking exists by compactness and normality of the compact Hausdorff space $K$. For $x\in K$, set $I_x=\{i:x\in K_i\}$. It is nonempty. Choose an open neighborhood $W_x$ contained in every $U_i$ with $i\in I_x$, disjoint from every $K_i$ with $i\notin I_x$, and sufficiently small that

$$
H^q(U_{i_0}\cap\cdots\cap U_{i_p};F)
\longrightarrow H^q(W_x;F)
$$

has finite-dimensional image for each nonempty list of indices in $I_x$ and every $q$. The first paragraph supplies the last requirement for this finite family.

Take a finite cover $(V_a)$ of $K$ such that each $V_a$ meets a chosen $K_{r(a)}$, is contained in $U_{r(a)}$, and the union of any intersecting family of the $V_a$ lies inside some $W_x$. Here is the elementary refinement construction being used. A manifold has a compatible metric. On a fixed neighborhood of the compact set, the finite cover by selected $W_x$ has a positive Lebesgue radius near $K$. Choose uniformly smaller metric balls centered on $K$, each contained in an eligible $U_i$ with its center in $K_i$, and pass to a finite subcover. Their radii can be decreased uniformly because the compact sets $K_i$ lie inside their respective open sets. Two such balls which meet have their centers and their union within the chosen Lebesgue radius; the same estimate applies to the union of a family with nonempty common intersection. This gives the required property.

For an intersection $V_{a_0}\cap\cdots\cap V_{a_p}\ne\varnothing$, let $W_x$ contain the union of its members. Since $V_{a_l}$ meets $K_{r(a_l)}$ and $W_x$ is disjoint from the other $K_i$, every $r(a_l)$ belongs to $I_x$. The restriction from the corresponding old intersection therefore factors as

$$
H^q(U_{r(a_0)}\cap\cdots\cap U_{r(a_p)};F)
\longrightarrow H^q(W_x;F)
\longrightarrow H^q(V_{a_0}\cap\cdots\cap V_{a_p};F).
$$

Its image is finite-dimensional. Finite direct sums show the same for the entire refinement map in every bidegree of the Čech cohomology array.

For completeness, that array has a convergent spectral sequence

$$
E_1^{p,q}=\bigoplus_{i_0<\cdots<i_p}
H^q(U_{i_0}\cap\cdots\cap U_{i_p};F)
\ \Longrightarrow\ H^{p+q}\!\left(\bigcup_iU_i;F\right).
$$

Choose a bounded-below injective resolution of $F$ and form its Čech double complex. The augmented Čech resolution of each injective sheaf is exact locally, by contraction using an index of an open member containing the point. Its terms are injective: open restriction preserves injectives because extension by zero is exact, and open direct image preserves injectives because inverse image is exact. Hence each such augmented resolution splits successively and stays exact on global sections. The double complex consequently computes the displayed derived sections. Taking vertical cohomology gives the $E_1$ page above. Refinement induces the usual restriction map on the abutment, with components the intersection restrictions just examined; repeated indices contribute zero in the alternating complex.

Choose an integer $b$ such that $H^q(F)=0$ for $q<b$. On total degree $j\ge b$, the induced Čech filtration has at most $L=j-b+1$ nonzero layers, since $p\ge0$ and $q\ge b$. A refinement of the kind just constructed induces a finite-dimensional image on each associated graded piece: finite-dimensionality of the image passes from one spectral-sequence page to the next, and hence to $E_\infty$.

One must not infer finite-dimensionality of the whole image from this single associated-graded assertion. Instead perform $L$ successive refinements. The following linear-algebra observation applies to the resulting maps on $H^j$. For vector spaces with decreasing filtrations of length $L$, a filtration-preserving map with finite-dimensional image on every associated graded piece sends each filtration step into the next step plus a finite-dimensional subspace of the target; choose finitely many lifts of a basis for each graded image. Composing $L$ such maps sends the whole source into a finite sum of images of these finite-dimensional subspaces, because the residual term has descended through all $L$ steps and is zero. The composite therefore has finite-dimensional image.

Start with the one-member cover $(U)$. The final refined cover has union $W$, where $K\subset W\subset U$. The preceding argument proves that $H^j(U;F)\to H^j(W;F)$ has finite-dimensional image. The restriction to $K$ factors through it, proving the assertion. For $j<b$ both relevant derived-section groups vanish and no refinement is needed. $\square$

This result measures the information which survives restriction. A neighborhood may have many classes created near its boundary, while only finitely many can persist on a prescribed compact subset.

## SH02-DA-COMPACT-FINITE — Compactness turns the local duality condition into finiteness

Let $k$ be a field, let $X$ be a compact $n$-manifold, and let $F\in D^b(k_X)$ be cohomologically constructible in the sense of `SH02-CB-SYSTEMS`. Then all $H^a(X;F)$ are finite-dimensional and vanish outside a finite interval. The pairing induced by evaluation and trace is perfect:

$$
H^a(X;F)\times H^{-a}(X;D_XF)\longrightarrow k.
$$

In particular, since $D_XF=D'_XF\otimes o_X[n]$, the second group is $H^{n-a}(X;D'_XF\otimes o_X)$. Orientability is not assumed.

**Proof.** Put $A=R\Gamma(X;F)$ and $B=R\Gamma(X;D_XF)$. Finite cohomological dimension makes $A$ bounded. The dual-sections adjunction and compactness identify

$$
B\simeq R\operatorname{Hom}_k(A,k).
$$

This identification holds before finite-dimensionality is known. We must still prove that this dual has finite-dimensional cohomology.

On $X\times X$, the exterior-Hom theorem gives the evaluation isomorphism

$$
D_XF\boxtimes^LF
\xrightarrow{\sim}
R\mathcal Hom(q_1^{-1}F,q_2^!F).
$$

Apply derived global sections. Proper-support base change and projection, with $X$ compact, identify the left side with $B\otimes_k^LA$. The rectangle adjunction `SH02-EX-RECTANGLE` identifies the right side with $R\operatorname{Hom}_k(A,A)$. The resulting isomorphism is

$$
B\otimes_k^LA\longrightarrow R\operatorname{Hom}_k(A,A),
\qquad b\otimes a\longmapsto\bigl(v\mapsto b(v)a\bigr),
$$

with the graded signs prescribed by the tensor symmetry. To check its normalization, start with the exterior evaluation pairing, integrate its first variable, and apply the projection formula. This is exactly the adjunction defining $B=R\operatorname{Hom}(A,k)$; its value on a decomposable tensor is the displayed rank-one operator. Thus it is the canonical tensor-to-Hom map, not an unrelated vector-space isomorphism.

Over a field a bounded complex is isomorphic in its derived category to its graded cohomology: split boundaries inside cycles and cycles inside each term. The degree-zero part of $B\otimes^LA$ is a direct sum of tensor products of the graded cohomology spaces. Every tensor is a finite sum of elementary tensors. Since the identity of $A$ lies in the image of the preceding isomorphism, its action on each $H^a(A)$ is a finite sum of rank-one linear maps. The identity of an infinite-dimensional vector space cannot have finite-dimensional image. Hence every $H^a(A)$ is finite-dimensional. Boundedness leaves only finitely many nonzero groups.

Finally, exactness of algebraic duality over a field identifies $H^{-a}(B)$ with $\operatorname{Hom}_k(H^a(A),k)$. The identification is induced by evaluation and the same trace; finite-dimensionality makes it a perfect pairing in both variables. $\square$

This argument uses the local constructibility condition through the exterior-Hom theorem. Finite stalk dimensions alone do not supply that theorem.

## SH02-DA-FORMS — Smooth forms and distributional representatives

Now let $k=\mathbb R$ and let $X$ be a compact oriented smooth $n$-manifold. Write $\mathcal A^p$ for smooth real $p$-forms and $\mathcal T^p$ for differential $p$-forms with distribution coefficients. The latter are also called currents with complementary test-form degree. Locally, $T=\sum_I T_I\,dx_I$, where each $T_I$ is a distribution. Both differentials are the exterior derivative, with distributional derivatives in $\mathcal T^\bullet$.

The exact analytic foundation used here is the existence of smooth locally finite partitions of unity on a countable-at-infinity smooth manifold. A sheaf of modules over smooth functions is fine, and a fine sheaf is acyclic for ordinary sections on this paracompact space. In the usual Čech proof the homotopy on a locally finite cover is $(hc)_{i_0\ldots i_{p-1}}=\sum_j\rho_j c_{j i_0\ldots i_{p-1}}$, so $dh+hd=1$ in positive Čech degrees. The local finiteness makes the sum meaningful for distributions as well. This is the precise acyclic-resolution foundation imported from the ordinary-sheaf prerequisite theory.

Both complexes resolve the constant sheaf, and inclusion of smooth forms into distributional forms is a quasi-isomorphism:

$$
\mathbb R_X\xrightarrow{\sim}\mathcal A^\bullet
\longrightarrow\mathcal T^\bullet.
$$

Here is a local verification, including the distributional part. For smooth forms on a star-shaped ball, the radial homotopy operator, obtained by integrating contraction along $x\mapsto tx$, satisfies $dH+Hd=1-\mathrm{ev}_0$; on degree zero $\mathrm{ev}_0$ is the constant value and in positive degree its pullback is zero. This follows by integrating Cartan's formula for the radial homotopy. It proves the smooth Poincaré lemma.

For a distributional form $T$ on a ball, work on a smaller concentric ball and choose a smooth kernel $\rho_\varepsilon$ of integral $1$, supported in translations small enough to remain in the original ball. Translation averaging $R_\varepsilon T=\int\rho_\varepsilon(v)\tau_v^*T\,dv$ is smooth and commutes with $d$. Define

$$
A_\varepsilon T=
\int\rho_\varepsilon(v)\int_0^1
\tau_{tv}^*(\iota_vT)\,dt\,dv.
$$

These integrals are defined by evaluation on compactly supported test forms; all translated tests stay in a fixed compact subset. Differentiating translation on tests proves Cartan's identity for distributions and hence

$$
R_\varepsilon T-T=dA_\varepsilon T+A_\varepsilon dT.
$$

If $dT=0$ and $\deg T>0$, the smooth Poincaré lemma gives $R_\varepsilon T=dH(R_\varepsilon T)$ on a further smaller ball. Therefore $T=d(HR_\varepsilon T-A_\varepsilon T)$. In degree zero, contraction is zero; a closed distribution equals its regularization and is a constant function locally. This proves the distributional Poincaré lemma and the stated quasi-isomorphism. Acyclicity of the terms now identifies the cohomology of the global smooth and distributional complexes with $H^*(X;\mathbb R)$.

For a closed smooth $a$-form $\alpha$ and a closed distributional $(n-a)$-form $T$, the duality pairing is

$$
([\alpha],[T])\longmapsto\int_X\alpha\wedge T.
$$

The integral means evaluation of the resulting top-degree distributional form on the constant function $1$. Compactness makes this legitimate without an added support condition. Multiplication of a distribution by a smooth form is defined; no multiplication of two arbitrary distributions is asserted. For a smooth $a$-form $\alpha$ and a distributional $(n-a-1)$-form $S$, distributional Stokes gives

$$
\int_X d\alpha\wedge S=(-1)^{a+1}\int_X\alpha\wedge dS,
$$

so replacing $T$ by $T+dS$ does not change its pairing with a closed $\alpha$. Applying the same identity to a smooth $(a-1)$-form and the closed form $T$ proves independence under replacing $\alpha$ by an exact perturbation. The inclusion of smooth forms into currents takes a smooth form $\beta$ to the same pairing $\int_X\alpha\wedge\beta$. The coordinate calculation in `SH02-MD-DENSITIES` identifies integration with the orientation-normalized sheaf trace; the same calculation over $\mathbb R$ uses the identical endpoint-difference generator and integral $1$. Thus this is precisely `SH02-DA-COMPACT-FINITE` for $F=\mathbb R_X$, and the pairing is perfect. This proves the smooth/distributional comparison as well as the numerical cohomological duality.

## SH02-DA-ACCUMULATION — A general support defect at a limit point

Let $S=D\cup\{\infty\}$ be the one-point compactification of a countably infinite discrete set. Embed $S$ as a compact subset of a real line $L$, writing $p$ for the image of $\infty$. The embedding may approach $p$ from either side. Let $G=k_S$, and let $F$ be the extension by zero of $k_D$ to $L$. Define

$$
V=\prod_{d\in D}k,\qquad
V_{\mathrm{fin}}=\bigoplus_{d\in D}k,\qquad
V_{\mathrm{ec}}=k\mathbf 1+V_{\mathrm{fin}}.
$$

Thus $V_{\mathrm{ec}}$ consists of sequences that are constant off a finite set. Directly from the sheaf definitions,

$$
\Gamma(L;F)=V_{\mathrm{fin}},\qquad
\Gamma(L;G)=V_{\mathrm{ec}},\qquad
\Gamma(L\setminus\{p\};G)=V.
$$

The distinction between $F$ and direct image from $D$ matters: a section of $F$ has zero germ at $p$ and must vanish on a neighborhood of $p$. Arbitrary sequences fail this condition.

The sheaf $G$ is soft, but

$$
R\Gamma_{\{p\}}(L;G)\simeq
(V/V_{\mathrm{ec}})[-1].
$$

**Proof.** The compact space $S$ has a basis of clopen subsets. A section on a closed subset $A\subset S$ is a locally constant function to the discrete module $k$ and has finite image by compactness. Its finitely many level sets are disjoint closed subsets of $S$. Clopen neighborhoods separate them: for each pair use the clopen basis and compactness to separate the two compact sets, then take finite intersections. Thus there are disjoint clopen neighborhoods of all level sets, on which the function extends constantly; set it to zero on the remaining clopen set. This proves extension to $S$. Closed direct image then proves softness of $G$ on $L$.

Soft acyclicity gives $R\Gamma(L;G)=V_{\mathrm{ec}}$ in degree zero. On $L\setminus\{p\}$ the support $D$ is closed and discrete, so its ordinary cohomology is $V$ in degree zero: sections are products of the exact stalk section functors on a discrete space, and products of module surjections are surjective. Localization therefore gives the asserted cokernel in degree one; its degree-zero kernel is zero. $\square$

For a field $k$, the quotient $V/V_{\mathrm{ec}}$ is infinite-dimensional. Partition $D$ into countably many infinite sets $D_j$. Any finite linear combination of their indicator functions that is eventually constant must have constant value zero on an unused infinite block, and then every coefficient is zero on its own infinite block. Their classes are linearly independent.

## SH02-DA-BIDUAL-DEFECT — Computing both duals without a finiteness assumption

Assume in this paragraph that $k$ is a field and orient $L$, so $\omega_L=k_L[1]$. Put

$$
P=\prod_{d\in D}k_{\{d\}}.
$$

This is the direct image of $k_D$; its sections on an open set are arbitrary families indexed by the points of $D$ in that open set. There are explicit identifications

$$
D'_LF\simeq P[-1],\qquad
D'_LD'_LF\simeq Q:=D_LP.
$$

The second object is a sheaf in degree zero. It is characterized on every open $U\subset L$ by

$$
\Gamma(U;Q)=\operatorname{Hom}_k(\Gamma_c(U;P),k).
$$

At each isolated point of $D$ its stalk is $k$. At $p$ its stalk is

$$
Q_p\simeq
V^*/V_{\mathrm{coord}}^*,
$$

where $V^*=\operatorname{Hom}_k(V,k)$ is the algebraic dual and $V_{\mathrm{coord}}^*$ is the span of the coordinate evaluation functionals. On global sections, the evaluation $F\to D'_LD'_LF$ is the usual inclusion of finite coordinate functionals. The same description holds on compact-tail neighborhoods of $p$; on opens avoiding $p$, locally finite coordinate families instead give an isomorphism of sheaves. The nonzero stalk quotient at $p$ shows that the global sheaf morphism is not an isomorphism.

**Proof.** Since compact subsets of the discrete space $D$ are finite, $\Gamma_c(U;F)=\bigoplus_{d\in U\cap D}k$. The sheaf $F$ is c-soft, as is a direct sum of the compactly supported point sheaves. Its compact-support derived sections are therefore concentrated in degree zero. Dual sections identify $D_LF$ with the product sheaf $P$, with its ordinary evaluation pairing. Tensoring by $\omega_L^{-1}=k_L[-1]$ gives $D'_LF=P[-1]$.

Restriction maps of $P$ are coordinate projections and are surjective, so $P$ is flabby and hence c-soft. The same dual-sections argument makes $D_LP=Q$ a sheaf in degree zero and gives its displayed section formula. Dualizing the shift in $D'_LF$ gives $D'_L(P[-1])=D_LP$, proving the second formula.

Choose decreasing neighborhoods of $p$ that remove successively finite subsets of $D$ and have boundary disjoint from $S$. The support of $P$ in each such neighborhood is compact there, so its compact sections form the product over the remaining tail. Extension to a larger neighborhood is the inclusion that inserts zero in the missing finitely many coordinates. Dual restriction thus removes the corresponding finite coordinate functionals. The filtered colimit is exactly $V^*/V_{\mathrm{coord}}^*$.

This quotient is nonzero. The nonzero vector space $V/V_{\mathrm{fin}}$ admits a nonzero linear functional; pulled back to $V$, it vanishes on every finitely supported sequence. No nonzero finite sum of coordinate evaluations has that property. Hence its class in $Q_p$ is nonzero, whereas $F_p=0$. The evaluation map is therefore not invertible. $\square$

This calculation concerns algebraic duals, not continuous duals of any chosen topology on $V$.

## SH02-DA-FLABBY — The sharp positive-dimensional flabby bound

For every nonzero coefficient ring covered by the conventions and every $n\ge1$, the soft and c-soft dimensions of $\mathbb R^n$ are $n$, and its flabby dimension is $n+1$. In dimension zero all three dimensions are zero.

The soft and c-soft assertions, and the flabby upper bound, are proved in `SH02-MD-DIMENSION` and `SH02-MD-EXERCISES`. We prove the remaining lower bound.

Choose the compactification embedding in `SH02-DA-ACCUMULATION` so that $D$ lies on just one side of $p$. Let $H=k_{L\setminus S}$. The exact sequence

$$
0\longrightarrow H\longrightarrow k_L\longrightarrow G\longrightarrow0
$$

and local cohomology at $p$ give

$$
H^2_{\{p\}}(L;H)\simeq V/V_{\mathrm{ec}}\ne0.
$$

To check the possible incoming map, $R\Gamma_{\{p\}}(L;k_L)=k[-1]$. Its degree-one class is the difference of the constant values on the two components of $L\setminus\{p\}$. Restriction to $D$, lying on one component, is a constant sequence, and its class in $V/V_{\mathrm{ec}}$ is zero. Thus the map from $k$ into $H^1_{\{p\}}(L;G)$ is zero, giving exactly the displayed isomorphism. The quotient is nonzero for every nonzero ring: a sequence taking values $0$ and $1$ on two infinite parts is not eventually constant.

Now let $\rho:L\times\mathbb R^{n-1}\to L$ and let $a$ include $(p,0)$. Write $b:\{p\}\hookrightarrow L$. The oriented submersion formula and exceptional composition give

$$
a^!\rho^{-1}H
\simeq a^!\rho^!H[-(n-1)]
\simeq b^!H[-(n-1)].
$$

Consequently $\rho^{-1}H$ has nonzero point-supported cohomology in degree $n+1$. Every flabby sheaf is acyclic for sections with a fixed closed support; this follows from the localization sequence and surjectivity of restriction to the complementary open set. A flabby resolution of length at most $n$ would force that degree-$n+1$ group to vanish. This contradiction proves the lower bound. Together with the upper bound it proves equality. For $n=0$ the space is a point and every sheaf is already flabby and soft. $\square$

## SH02-DA-PROBLEMS — Further calculations with complete solutions

**Problem: a bundle with a distinguished direction.** Let $E=E_0\oplus\mathbb R$ be an oriented real bundle of positive rank over a manifold. Compute its Euler class, and describe the effect on the sphere-bundle triangle when its rank is at least two.

*Solution.* The unit vector in the last summand is a nowhere-zero section, so `SH02-DA-EULER` gives $e(E)=0$. The connecting morphism of the sphere triangle is therefore zero. A triangle with zero connecting morphism is split, so $R f_*k_{S(E)}\simeq k\oplus k[-(\operatorname{rank}E-1)]$ as an object. A splitting is a further choice; the theorem supplies the canonical triangle and its zero extension class.

**Problem: a normal cycle that is zero globally.** In an oriented rank-$r$ vector bundle, restrict the Thom class to the complement of the zero section and then pull back to any nowhere-zero section. Explain why this does not force the Thom class itself to be zero.

*Solution.* Localization makes both stated images zero. The Thom class lies in supported cohomology, whose map to ordinary cohomology need not be injective. For a trivial positive-rank bundle over a point, the Thom group is $k$ whereas the ordinary group in degree $r$ of the total vector space is zero. The supported class is the nonzero orientation generator despite its zero ordinary image.

**Problem: adding neutral parameters.** Suppose a closed quadratic sublevel for a form on $W$ has $s$ null directions. Add an additional null vector space of dimension $d$. Determine the changes in compact-support and supported cohomology.

*Solution.* The enlarged sublevel is the original one times $\mathbb R^d$. In the nonzero threshold range, compact-support cohomology acquires the orientation line and shift $[-d]$. Both the total dimension and the non-positive count increase by $d$, so their difference, the supported-cohomology degree, stays fixed. For a negative threshold both complexes remain zero. This is also immediate from the proper projection proof in `SH02-DA-QUADRATIC`.

**Problem: why soft is not flabby.** In `SH02-DA-ACCUMULATION`, give a section on $L\setminus\{p\}$ which cannot extend globally, despite softness of $G$.

*Solution.* Partition $D$ into two infinite sets and use their indicator function with values $0,1\in k$. This is a section on the punctured line, but it is not eventually constant, so it is not in $\Gamma(L;G)$. Flabbiness asks for extension from an arbitrary open subset; softness asks for extension from a closed subset. The two requirements differ exactly at this accumulation point.

**Problem: distributional representatives.** Let $\alpha$ be a closed smooth $a$-form and let $T,T'$ be closed distributional $(n-a)$-forms on a compact oriented smooth manifold, with $T'-T=dS$. Show that their pairings with $\alpha$ agree, and explain why every distributional cohomology class can be compared to a smooth one.

*Solution.* Distributional Stokes gives $\int\alpha\wedge dS=(-1)^{a+1}\int d\alpha\wedge S=0$. The two fine resolutions in `SH02-DA-FORMS` are quasi-isomorphic, so their global cohomologies are isomorphic. Thus the class of $T$ is represented by a smooth form; changing the representative does not change the integral. No global smoothing that commutes strictly with every coordinate change is needed.

## SH02-DA-ANTECEDENTS — Mathematical correspondence and remaining boundaries

These applications develop support phenomena, characteristic classes and compact duality in the microlocal theory of sheaves of M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985). Their proofs use the operation, orientation and local-finiteness lessons linked above. The integral rank-one local-system pairing is proved in `SH02-MD-ORIENTATION-LINE` and `SH02-MD-EXERCISES`; the local-cohomological boundary criterion and convex cases are in `SH02-CB-BOUNDARY-CRITERION` and `SH02-CB-CONVEX`.

The support-comparison diagrams belong to `SH02-EX-SUPPORT-ERASURE`, `SH02-EX-HOM-SUPPORT-COMPATIBILITY`, and `SH02-EX-COEFFICIENT-ACTION`. Those proofs retain their stated input and output ranges, including the supported unbounded Hom comparison. Here the support-erasure argument uses the $D^+$ counit result actually proved here.
