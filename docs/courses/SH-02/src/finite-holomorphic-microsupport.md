# SH02-FH-UNIT — Directional information under a finite holomorphic map

<a id="SH02-FH-WEAK-EXTENSION"></a>

[The arbitrary weak-coefficient theorem](../weak-coefficients.html#WC0) proves the same finite holomorphic equality for every bounded weakly complex-constructible complex over every commutative ring. Its [direct original-ring proof](../weak-coefficients.html#WC6) includes infinitely generated and nonperfect stalks. The perfect-stalk proofs and scalar-change statements below remain useful at their specified scope.

Self-checked by the writing AI. The finite-map proof below works at the full coefficient-ring and constructibility scope of FH1. It uses an explicit finite conormal-image argument, actual supported tests, the integer Morse filtration and residue-field detection. The analytic, normal-Morse, field-perverse and controlled-Morse inputs are stated in [the geometric prerequisites](#SH02-FH-INPUTS) and developed in the four lessons linked there, relative to their exact external theorem statements. This supplies the primary finite-map argument for `SH02-MO-HOLOMORPHIC-IMPORT` in microsupport operations.

Let $k$ be a commutative ring with identity and finite global dimension. A complex-constructible complex means a bounded complex whose cohomology is locally constant on a locally finite complex analytic stratification and whose stalks are perfect over $k$. Perfection means representability by a bounded complex of finite projective modules. It does not mean that those modules are free, or that their cohomology is a vector space. Complex manifolds have finite dimension and are Hausdorff and countable at infinity.

For a complex $A$, write $s(A)=\{z:A_z\not\simeq0\}$ and $\operatorname{Supp}(A)=\overline{s(A)}$. Keeping these two sets distinct matters in the argument. A nonzero vanishing-cycle germ need not occur at every point of its closed support.

The target is the equality

$$
\operatorname{SS}(Rf_*G)=f_\pi f_d^{-1}\operatorname{SS}(G)
\tag{FH1}
$$

for a finite holomorphic map $f:Y\to X$ and a complex-constructible $G$. Here finite means proper with finite fibres, including maps whose image has positive codimension. On underlying real cotangent bundles,

$$
f_d(y,\eta)=(y,df_y^t\eta),\qquad
f_\pi(y,\eta)=(f(y),\eta).
$$

The general proper-image theorem proves the inclusion from left to right. Finiteness prevents cancellation between different points of a fibre. Holomorphic geometry is needed to detect a covector when its pullback lies at a branch point.

## SH02-FH-FIBRE — Separating the sheets near one fibre

Let $f:Y\to X$ be a proper continuous map of locally compact Hausdorff spaces with finite fibres. Fix $x\in X$ and write $f^{-1}(x)=\{y_1,\ldots,y_r\}$. Given pairwise disjoint open neighborhoods $W_i$ of these points, there is an open neighborhood $U$ of $x$ such that

$$
f^{-1}(U)\subset\bigcup_i W_i.
\tag{FH2}
$$

Consequently the sets $W_i\cap f^{-1}(U)$ are both open and closed in $f^{-1}(U)$. For an empty fibre one can choose $U$ with empty inverse image.

**Proof.** A proper map between these spaces is closed. The closed set $C=Y\setminus\bigcup_iW_i$ misses the fibre, so $U=X\setminus f(C)$ has the required property. For each $i$, the complement of $W_i\cap f^{-1}(U)$ in $f^{-1}(U)$ is the union of the other pieces. For an empty fibre take $C=Y$. $\square$

This conclusion says nothing about unramifiedness. A piece can contain several points of a nearby fibre that merge at $y_i$.

## SH02-FH-STALKS — Exactness and the actual base-change map

Under the preceding hypotheses, for any sheaf $A$ of $k$-modules the germ restriction map is an isomorphism

$$
(f_*A)_x\xrightarrow{\sim}\bigoplus_{y\in f^{-1}(x)}A_y.
\tag{FH3}
$$

In particular $f_*$ is exact, $Rf_*=f_*$ on bounded complexes, and

$$
(Rf_*A)_x\simeq\bigoplus_{y\in f^{-1}(x)}A_y,
\qquad
\operatorname{Supp}(Rf_*A)=f\bigl(\operatorname{Supp}(A)\bigr).
\tag{FH4}
$$

These assertions require no finiteness assumption on the modules and no finite global dimension assumption on $k$.

**Proof.** Represent a tuple of germs by sections on disjoint neighborhoods of the finitely many $y_i$. Apply FH2 and restrict these sections to its pieces. They glue to a section over $f^{-1}(U)$, proving surjectivity of FH3. If a section over $f^{-1}(U)$ has zero germ at every $y_i$, choose smaller disjoint neighborhoods on which it is zero and apply FH2 again. Its germ at $x$ is zero, proving injectivity. A stalkwise short exact sequence stays exact after a finite direct sum, so $f_*$ is exact. Applying the resulting natural isomorphism term by term gives the derived assertion; no splitting of a cohomology spectral sequence is involved.

A finite direct sum of complexes is zero exactly when every summand is zero. Thus $s(Rf_*A)=f(s(A))$. For every subset $S\subset Y$, continuity gives $f(\overline S)\subset\overline{f(S)}$, and closedness of $f$ gives the reverse inclusion. Apply this to $S=s(A)$ to obtain the support equality. $\square$

For a cartesian square

$$
\begin{array}{ccc}
Y'&\xrightarrow{g'}&Y\\
\scriptstyle f'\downarrow&&\downarrow\scriptstyle f\\
X'&\xrightarrow{g}&X,
\end{array}
$$

with locally compact Hausdorff spaces, properness and finite fibres pass to $f'$. The adjunction base-change map

$$
g^{-1}Rf_*A\longrightarrow Rf'_*g'^{-1}A
\tag{FH5}
$$

is an isomorphism. Indeed, at $x'$, FH3 identifies both sides with $\bigoplus_{f(y)=g(x')}A_y$. The map restricts a representative germ to that same tuple and is the identity under these identifications. This also proves its compatibility with successive changes of base and with identity squares. Exactness of inverse image to constant-ring spaces is the coefficient convention in the prerequisite proofs.

## SH02-FH-LOCAL-SUPPORT — A support test splits over the fibre

Let $Z\subset X$ be closed, $j:X\setminus Z\hookrightarrow X$, and $j':Y\setminus f^{-1}(Z)\hookrightarrow Y$. There is a natural isomorphism

$$
R\Gamma_Z Rf_*A\simeq Rf_*R\Gamma_{f^{-1}(Z)}A.
\tag{FH6}
$$

Its stalk at $x$ is the finite direct sum of the supported stalks on the right.

**Proof.** Restriction to $X\setminus Z$ is an instance of FH5. Direct images compose, giving

$$
Rj_*j^{-1}Rf_*A\simeq Rf_*Rj'_*j'^{-1}A.
$$

The maps from $Rf_*A$ to these objects correspond: both restrict a section to the inverse image of $X\setminus Z$. Taking fibres in the two localization triangles proves FH6. Its stalk form is FH4. This argument compares the actual restriction maps, not just the outer objects of the triangles. $\square$

For a real test function $u$ on $X$, take $Z=\{u\geq u(x)\}$. FH6 becomes

$$
\bigl(R\Gamma_{\{u\geq u(x)\}}Rf_*A\bigr)_x
\simeq
\bigoplus_{f(y)=x}
\bigl(R\Gamma_{\{u\circ f\geq u(x)\}}A\bigr)_y.
\tag{FH7}
$$

One cannot infer FH1 from FH7 alone. The functions pulled back from the target may fail to detect a covector in the source microsupport.

## SH02-FH-CYCLES — Nearby and vanishing cycles also split

Here is a definition and comparison that fix all maps and shifts used below. For a continuous $h:X\to\mathbb C$, let $X_0=h^{-1}(0)$ with inclusion $i$, and put

$$
\widetilde X^*=X\times_{\mathbb C}\widetilde{\mathbb C^*},
\qquad q:\widetilde X^*\longrightarrow X,
$$

where $\widetilde{\mathbb C^*}\to\mathbb C^*\hookrightarrow\mathbb C$ is a universal covering followed by the open inclusion. Define

$$
\psi_hA=i^{-1}Rq_*q^{-1}A,
\qquad
\Phi_hA=\operatorname{Cone}\bigl(i^{-1}A\longrightarrow\psi_hA\bigr).
\tag{FH8}
$$

The arrow is induced by the unit $A\to Rq_*q^{-1}A$. We use this unshifted cone throughout; replacing every $\Phi$ by $\Phi[-1]$ would leave all support assertions unchanged. These constructions and the following comparison can be performed in the bounded-below derived category. Boundedness and perfect local data in the constructible analytic situation are included in the explicit geometric contract below.

Let $f:Y\to X$ be as in FH2 and let $f_0:(h\circ f)^{-1}(0)\to h^{-1}(0)$ be the induced finite proper map. Then

$$
\psi_h Rf_*A\simeq Rf_{0*}\psi_{h\circ f}A,
\qquad
\Phi_h Rf_*A\simeq Rf_{0*}\Phi_{h\circ f}A.
\tag{FH9}
$$

**Proof.** The space $\widetilde Y^*$ obtained from $h\circ f$ is $Y\times_X\widetilde X^*$. Write $\widetilde f:\widetilde Y^*\to\widetilde X^*$ and $q_Y:\widetilde Y^*\to Y$. Both $\widetilde f$ and $f_0$ are proper with finite fibres. Applying FH5 first over $\widetilde X^*$ and then over $X_0$, and composing direct images, gives

$$
\begin{aligned}
i^{-1}Rq_*q^{-1}Rf_*A
&\simeq i^{-1}Rq_*R\widetilde f_*q_Y^{-1}A\\
&\simeq i^{-1}Rf_*Rq_{Y*}q_Y^{-1}A\\
&\simeq Rf_{0*}i_Y^{-1}Rq_{Y*}q_Y^{-1}A.
\end{aligned}
$$

This is the nearby-cycle comparison. To check the specialization arrow, start with the unit $A\to Rq_{Y*}q_Y^{-1}A$ and use the same two cartesian squares. The mate description of FH5, or its germ description in FH3, identifies its image with the unit for $q$. The specialization arrows therefore form a commutative square. Taking its cones in the derived enhancement proves the second comparison. This construction commutes with the deck transformation as well, since all base-change maps are natural. $\square$

In particular

$$
\operatorname{Supp}\bigl(\Phi_hRf_*A\bigr)
=f_0\operatorname{Supp}\bigl(\Phi_{h\circ f}A\bigr).
\tag{FH10}
$$

There is no decomposition-theorem or semisimplicity argument here: FH10 follows from the exact finite direct sum on stalks and closedness of $f_0$.

## SH02-FH-PERFECT-DETECTION — Residue fields detect a perfect complex

For any commutative ring $k$ and any perfect complex $P$,

$$
P\simeq0\quad\Longleftrightarrow\quad
P\otimes_k^L\kappa(\mathfrak p)\simeq0
\text{ for every prime }\mathfrak p\subset k.
\tag{FH11}
$$

**Proof.** Only the reverse implication needs proof. Localize a bounded finite-projective representative at a maximal ideal $\mathfrak m$. Finite projective modules over a local ring are finite free. If an entry of a differential is a unit, row and column operations isolate a two-term summand $k_{\mathfrak m}\xrightarrow{1}k_{\mathfrak m}$. The identities $d^2=0$ make the adjacent maps into and out of this summand zero. Remove this contractible summand. The total number of basis vectors is finite, so the process stops with every differential entry in $\mathfrak m k_{\mathfrak m}$. After tensoring with $\kappa(\mathfrak m)$, the remaining differentials are zero. Acyclicity over that field forces every remaining term to be zero. Thus $P_{\mathfrak m}$ is contractible for every maximal ideal.

If a cohomology module of $P$ contained a nonzero element $a$, choose a maximal ideal containing its annihilator. No element outside that ideal kills $a$, so $a$ survives localization, a contradiction. Hence $P$ is acyclic. No noetherian hypothesis was used. The statement also covers the zero ring, when every module is zero. $\square$

A second elementary fact controls change of coefficients. Suppose a local cohomology datum is expressed by a finite diagram of perfect complexes using finite sums, shifts, cones and direct summands. Its value is perfect, and its construction commutes with $-\otimes_k^L L$ for every $k$-complex $L$. Each operation in this list has that property, so induction on the finite construction proves the assertion. Finite homotopy limits are included, since in a stable category they are made from finite sums and fibres.

## SH02-FH-FINITE-PAIR — Coefficients in an actual finite local model

Let $(K,L)$ be a compact pair with a finite triangulation in which $L$ is a subcomplex. Suppose a bounded complex $A$ restricts on every open simplex to a constant perfect complex. Then $R\Gamma(K,L;A)$ is perfect and the natural comparison

$$
R\Gamma(K,L;A)\otimes_k^L B
\longrightarrow R\Gamma(K,L;A\otimes_k^L B)
\tag{FH16}
$$

is an isomorphism for every coefficient $k$-algebra $B$.

**Proof.** Filter $K$ by its closed skeleta. The difference between consecutive skeleta is a finite disjoint union of open simplices. After orienting a $d$-simplex $\sigma$, compactly supported cohomology of its constant complex $P$ is

$$
R\Gamma_c(\sigma;P)\simeq P[-d].
$$

This is the compactly supported orientation calculation for $\mathbb R^d$ in manifold duality; its comparison with coefficients is induced by tensoring the same orientation generator. Thus the assertion holds on each open simplex. The open-closed localization triangle at every skeletal step gives a triangle of compactly supported cohomology complexes. The projection comparison with coefficients is natural for its three maps. Finite sums and cones preserve perfection, and derived tensor preserves these triangles, so induction proves perfection and the comparison for $R\Gamma_c(K;A)$. Compactness identifies this with ordinary cohomology. Repeat the argument for $L$ and take the fibre of the restriction $R\Gamma(K;A)\to R\Gamma(L;A)$. This gives FH16 with its actual restriction map. $\square$

No triangulation-existence theorem is hidden in this lemma: the compatible finite triangulation is a hypothesis. Applying it to a normal slice or a Milnor pair still requires that such a pair exists and computes the desired sheaf-theoretic datum. In particular it does not justify interchanging tensor with an arbitrary infinite nearby-cycle limit.

## SH02-FH-INPUTS — The geometric prerequisites of the finite-map proof

The main proof below uses supported real tests and finite sums. The stronger critical-support argument later in the lesson is retained as an alternative; its full vanishing-cycle comparison and nonisolated analytic theorem are not prerequisites of the main proof. The four inputs below are supplied by these lessons, with their exact external theorem statements and coefficient ranges kept visible:

- Analytic geometry for finite maps supplies compatible strata, finite analytic images and closed conormals.
- Normal Morse data and change of coefficients supplies the finite normal pairs, their stabilization and the coefficient comparison.
- [Perverse degrees and normal Morse complexes](perverse-normal-morse-inputs.md#SH02-PNM-UNIT) supplies the field-perverse degree and normal-Morse exactness.
- [An isolated holomorphic test and its Morse filtration](isolated-holomorphic-morse-tests.md#SH02-IHM-UNIT) supplies the controlled cluster, actual relative filtration and positive integer count.

For the primary proof, use these inputs with the [finite conormal-image argument](#SH02-FH-CONORMAL-IMAGE), [quadratic test construction](#SH02-FH-HOLOMORPHIC-TEST), [field argument](#SH02-FH-FIELD-FINITE) and [coefficient recovery](#SH02-FH-RING-FINITE). The [full critical-support route](#SH02-FH-GEOMETRIC-CONTRACT) is a separate, stronger direction; The [general nearby-cycle proof](../general-nearby-cycle-models.html) supplies FH13; The [critical-support proof](../general-critical-support.html) supplies FH14 separately. Neither is needed for FH30.

### SH02-FH-ANALYTIC-INPUT — Analytic sets and adapted finite maps

The required analytic facts are the local dimension bound for finitely many holomorphic equations, analyticity and dimension preservation under a finite proper holomorphic map, dense smooth loci and compatible Whitney stratifications. Locally near a finite fibre, the source stratification may be chosen adapted to the sheaf and compatible with a target stratification so that each source stratum maps locally biholomorphically to its target stratum. Conormal closures for this complex stratification are complex analytic. The strata and their refinements are geometric and independent of the coefficient ring. Only locally finite stratifications are assumed globally. Their local finite form, not a global finite decomposition, is used below.

### SH02-FH-NORMAL-MORSE-INPUT — Coefficient-compatible visible conormals

The normal Morse part of FH12 is required: every generic connected conormal component has a normal Morse object, the microsupport is the union of closures of the components with nonzero objects, and these objects are computed by actual finite normal pairs compatible with the coefficient stratification. FH16 then proves perfection and derived change of coefficients for these models. This input includes the existence and stabilization of the normal pairs and the assertion that they compute microsupport. It does not assert that all nearby-cycle limits commute with tensor.

### SH02-FH-PERVERSE-INPUT — Field coefficients and normal Morse degree

Over every field, bounded complex-constructible complexes have the bounded middle-perverse t-structure described by the stalk/costalk conditions FH17. With the dimension normalization in the Morse argument below, the normal Morse functors are t-exact. These are the only perverse inputs. Finite direct-image t-exactness and the microsupport union over perverse cohomology are deduced below, and no perverse construction is applied over the original ring.

### SH02-FH-CONTROLLED-MORSE-INPUT — An isolated cluster and its finite filtration

For a holomorphic germ with an isolated critical point for a finite adapted complex Whitney stratification, a sufficiently small relative pair computes its supported local test. A small generic holomorphic perturbation can be chosen with controlled noncharacteristic boundary, finitely many stratified Morse points, and distinct critical values. The relative complex remains identified with the original local test while those points are separated by a finite Morse filtration. At a point on a stratum of complex dimension $d$, the quotient is its normal Morse object shifted by $[-d]$. The number of points on each generic conormal is the local complex analytic intersection number; these numbers are positive at a nonempty isolated intersection and are preserved by this perturbation. The boundary control, relative-pair continuation and local analytic intersection theorem are substantive geometric inputs. The integer index and nonvanishing consequence are proved from them below.

<a id="SH02-FH-FULL-ISOLATED-PROOF"></a>

The complete [original isolated pair and whole-cluster construction IH0–IH22](../isolated-holomorphic-pair-and-cluster.html#IH0) proves this controlled isolated geometric input at its [exact retained provider floor](../isolated-holomorphic-pair-and-cluster.html#IH-PROVIDERS). It identifies the original relative restrictions, keeps the entire perturbation cluster inside the prescribed radial boundary, and gives the actual finite filtration with its orientation and every-field integer count. The [IHA1–IHA3 multiplicity bridge](../isolated-holomorphic-pair-and-cluster.html#IHA1) identifies both the oriented-cycle and Samuel conventions without a Cohen–Macaulay assumption. The original perfect-coefficient and residue-field steps below retain their own hypotheses.

The linked lessons give the four prerequisite deductions relative to their exact external theorem statements. The cited analytic and constructible foundations retain their other-course owners.

## SH02-FH-CONSTRUCTIBLE-IMAGE — Constructibility from an adapted finite covering

Use a compatible pair of complex analytic stratifications $\mathcal S$ of $Y$ and $\mathcal T$ of $X$ for the finite holomorphic map $f$, adapted to $G$, such that every $f^{-1}(T)$ is a disjoint union of source strata and each source stratum maps locally biholomorphically to $T$. Such compatible analytic stratifications are the exact geometric input here. We prove the sheaf consequence, rather than invoke a general proper-image constructibility theorem in addition.

For any $T\in\mathcal T$, all the source strata in $f^{-1}(T)$ have dimension $\dim T$. The frontier condition and local finiteness imply that each is open and closed in $f^{-1}(T)$: an incident distinct boundary stratum would have smaller dimension. Thus $f_T:f^{-1}(T)\to T$ is a local homeomorphism. It is proper with finite fibres, by change of base from $f$.

A proper local homeomorphism with finite fibres is a finite covering. Indeed choose disjoint neighborhoods of the finitely many points of a fibre on which the map is a homeomorphism to an open target neighborhood. Intersect those target neighborhoods and then use FH2 to ensure that their inverse images exhaust the inverse image of a still smaller neighborhood. These are precisely its sheets. An empty fibre gives the empty covering on a neighborhood.

The restriction of $R f_*G$ to $T$ is $f_{T*}(G|_{f^{-1}(T)})$ by FH5. On a sufficiently small open set in $T$, the covering is a finite disjoint union of copies of that set. Consequently its cohomology sheaves are finite direct sums of the local systems obtained from the cohomology sheaves of $G$ on those sheets. They are locally constant. This proves weak complex constructibility of $Rf_*G$. Boundedness and perfection of its stalks follow separately from the actual finite sum FH4. The proof holds for the original ring $k$; it uses no field condition or finite-rank replacement for perfect stalks.

The same argument applies after extending coefficients to a residue field, since scalar extension preserves local constancy on the fixed source strata. Hence one compatible geometric stratification works for every coefficient change needed in FH28.

## SH02-FH-CONORMAL-IMAGE — The geometry of a finite cotangent image

Here is the geometric reason isolated tests suffice for a finite map. We use three local facts about complex analytic sets: the dimension bound for the zero set of a finite list of holomorphic functions; the analyticity and dimension preservation of a finite holomorphic image; and compatible locally finite analytic stratifications with dense smooth strata. These are analytic prerequisites. The argument below does not deduce them from the sheaf statement being proved.

Let $Y$ and $X$ have complex dimensions $d$ and $n$, and let $f:Y\to X$ be finite holomorphic. On complex cotangent bundles put

$$
E=Y\times_XT^*X,\qquad
a(y,\eta)=(y,df_y^t\eta),\qquad
b(y,\eta)=(f(y),\eta).
\tag{FH40}
$$

Thus $a=f_d$, $b=f_\pi$, and $E$ is a vector bundle of rank $n$ over $Y$. The map $b$ is the base change of $f$, so it is proper and finite.

Suppose $\Lambda\subset T^*Y$ is a closed complex analytic conic set, empty or pure of dimension $d$. Assume there is a locally finite complex analytic Whitney stratification of $Y$ such that

$$
\Lambda_y\subset\operatorname{Ann}(T_yS)
\quad\text{whenever }y\in S.
\tag{FH41}
$$

The union of closed conormals occurring in the normal-Morse description of a complex-constructible sheaf satisfies FH41. To see the point at a boundary stratum, take covectors based on the original stratum that converge to a covector at the boundary. Pass to a convergent subsequence of tangent spaces in a Grassmannian. Whitney condition (a) places the tangent of the boundary stratum inside their limit. The limiting covector annihilates that limit and hence the boundary tangent. This proves FH41 for every closed conormal in the union.

Define the reduced analytic set $B$ and its image $A$ by

$$
B=a^{-1}(\Lambda),\qquad A=b(B).
\tag{FH42}
$$

If nonempty, both $B$ and $A$ are pure of complex dimension $n$. The set $A$ is closed, analytic and conic, and its smooth tangent spaces are Lagrangian in $T^*X$.

**Proof.** First observe that a holomorphic map with finite fibres from a smooth complex manifold of dimension $s$ has differential rank $s$ on a dense open subset. On an open set of maximum rank $t$, the holomorphic constant-rank theorem gives local fibres of dimension $s-t$. Finiteness forces $t=s$. The rank-drop locus is a proper analytic subset. This observation applies to any local smooth piece of the source; it makes no claim of immersion at every point.

For the lower dimension bound on $B$, work in coordinates on $Y$. The product $E\times\Lambda$ is pure of dimension $2d+n$. Inside $E\times T^*Y$, the graph of $a$ is given by $2d$ holomorphic equations, matching the base and covector coordinates of the second factor with those of $a$. Its intersection with $E\times\Lambda$ is $B$. Thus the analytic dimension bound gives

$$
\dim C\geq n
\tag{FH43}
$$

for every local irreducible component $C$ of $B$. Neither smoothness of $\Lambda$ nor transversality of $a$ is assumed.

For the upper bound, let $e=\dim C$. Let $r:E\to Y$ be the bundle projection. Choose a dense smooth piece of $C$ on which $r$ has constant rank $s$ and whose image lies in one stratum $S$ of FH41. A compatible analytic stratification of $C$, the map $r$, and the finitely many source strata near the point supplies such a piece of full dimension. The constant-rank theorem identifies the local image with a smooth complex submanifold $V\subset S$ of dimension $s$. By the finite-fibre observation, we may choose the point and shrink this piece so that $df$ is injective on $TV$.

For a fixed such $y$, the fibre $B_y$ lies in the linear subspace of $T^*_{f(y)}X$ that annihilates $df_y(T_yS)$. This subspace has dimension at most $n-s$, since it also annihilates the $s$-dimensional space $df_y(T_yV)$. The local fibre of $C\to V$ has dimension $e-s$. Consequently

$$
e-s\leq n-s,
\tag{FH44}
$$

which gives $e\leq n$. Together with FH43 this proves purity of $B$.

The restriction of $b$ to $B$ is finite and proper. Its image is therefore closed and analytic, and the image of each irreducible component has the same dimension $n$. Locally these images form a finite union, so $A$ is pure of dimension $n$. Scalar multiplication commutes with $a$ and $b$, giving conicity.

Write $\theta_Y$ and $\theta_X$ for the tautological one-forms. Their pullbacks satisfy

$$
b^*\theta_X=a^*\theta_Y.
\tag{FH45}
$$

Indeed both sides, evaluated on a tangent vector $v$ at $(y,\eta)$, are $\eta(df_y(dr(v)))$. On a dense smooth piece of an irreducible component $C\subset B$, tangent vectors project into the tangent of a single stratum $S$. The covector $df_y^t\eta$ annihilates that tangent by FH41. Hence FH45 vanishes on that piece. Its restriction to the smooth locus of $C$ is a holomorphic form and therefore vanishes everywhere there.

Choose an irreducible component $A_0$ of $A$ and a component $C$ mapping onto it. On dense smooth open subsets the finite map $C\to A_0$ has full rank $n$: a smaller maximum rank would give a positive-dimensional local fibre. At such points its tangent map is an isomorphism, so the vanishing of $b^*\theta_X$ gives $\theta_X|_{T A_0}=0$. Holomorphic continuation extends this to the smooth locus of $A_0$. Differentiating gives $d\theta_X|_{T A_0}=0$. Since its dimension is half the ambient symplectic dimension, this tangent space is Lagrangian. The same conclusion holds at every smooth point of the full reduced set $A$. $\square$

This proof includes components over branch loci and lower-dimensional support strata. It allows $d<n$, and it also allows $df_y=0$ at an individual point. A source stratum consisting of a point can contribute an entire target cotangent fibre of dimension $n$.

## SH02-FH-HOLOMORPHIC-TEST — Choosing a test and isolating its source points

Let $A\subset T^*X$ be a complex analytic Lagrangian set and let $q=(x,\eta)$ be a smooth point. In holomorphic coordinates centered at $x$, there is a quadratic polynomial $h$ such that

$$
h(x)=0,\qquad dh_x=\eta,\qquad
T_q\operatorname{graph}(dh)\cap T_qA=0.
\tag{FH46}
$$

**Proof.** Set $V=T_xX$. Coordinates identify $T_q(T^*X)$ with $V\oplus V^*$. Let $L=T_qA$ and let $W\subset V$ be its projected image. The vertical subspace of $L$ equals $\operatorname{Ann}(W)$: isotropy gives containment, and both have dimension $n-\dim W$. Thus for $w\in W$, the restriction to $W$ of a covector component of any lift of $w$ to $L$ is well-defined. It gives a linear map $C:W\to W^*$. The Lagrangian condition says that $C$ is symmetric.

Choose a nondegenerate complex symmetric form $D$ on $W$ and extend $C+D$ to a symmetric form $H$ on $V$. A vector $(v,Hv)$ in $L$ must have $v\in W$ and satisfy $D(v)=0$, so $v=0$. Hence $\operatorname{graph}(H)$ is transverse to $L$. The polynomial

$$
h(z)=\eta(z)+\tfrac12 H(z,z)
\tag{FH47}
$$

has the requested first derivative and Hessian. Its differential graph has tangent space $\operatorname{graph}(H)$ at $q$, proving FH46. The inverse-function theorem then shows that the graph and $A$ intersect locally only at the reduced point $q$. $\square$

This construction works when $\eta=0$. For a zero-section component of $A$, take a nondegenerate Hessian. If $W=0$, every Hessian is transverse to $L$; the form on the zero vector space is nondegenerate in the usual convention.

Now take $A$ and $B$ from FH42 and choose such an $h$ at a smooth point $q\in A$. Shrink the target neighborhood $U$ of $x$ so that

$$
\operatorname{graph}(dh)\cap A\cap T^*U=\{q\}.
\tag{FH48}
$$

This is possible because $dh$ is continuous: after taking a cotangent neighborhood where the intersection is isolated, the whole graph over a sufficiently small $U$ lies in that neighborhood. For $z\in f^{-1}(U)$ the chain rule gives

$$
(z,d(h\circ f)_z)\in\Lambda
\quad\Longleftrightarrow\quad
(z,dh_{f(z)})\in B.
\tag{FH49}
$$

The image of such a point under $b$ lies in the intersection FH48. Therefore all source points in FH49 lie in the finite set

$$
C_q=\{y\in f^{-1}(x):(y,df_y^t\eta)\in\Lambda\}.
\tag{FH50}
$$

This set is nonempty because $q\in A$. The graph of $d(h\circ f)$ consequently has an isolated intersection with $\Lambda$ at every corresponding source cotangent point. No nonzero condition on $df_y^t\eta$ is imposed. These intersections may have multiplicity greater than one; the argument does not require source transversality.

Small disjoint neighborhoods separate the finitely many points of the fibre. By the finite-fibre neighborhood lemma, the target can be shrunk again so that its full inverse image is contained in those neighborhoods. Thus the local tests obtained here apply to the same finite direct-sum comparison FH7, with no missing branch.

Finally, the smooth locus of every irreducible component of $A$ is dense. Once a sheaf's closed microsupport contains all these smooth points, it contains all of $A$. Singular points of the cotangent image therefore follow by closure after using these isolated tests. In target dimension zero all spaces and tangent spaces in this argument have their zero-dimensional meanings; the empty and zero-section cases remain valid.

For the sheaf argument one may strengthen the choice so that every source stratum has isolated critical points. Fix a locally finite complex analytic Whitney stratification adapted to the sheaf and put

$$
\Sigma=\bigcup_S\overline{T^*_SY},\qquad
A_{\mathrm{all}}=b\bigl(a^{-1}(\Sigma)\bigr).
\tag{FH51}
$$

The union here includes every stratum, including those with zero normal-Morse complex. Locally it is a finite union of closed analytic conormals, each pure of dimension $d$. The Whitney argument preceding FH42 proves FH41 for $\Sigma$. Thus $A_{\mathrm{all}}$ is a closed analytic Lagrangian set, pure of dimension $n$. If $\Lambda\subset\Sigma$ is the microsupport, then $A\subset A_{\mathrm{all}}$. Both are pure of dimension $n$, and $A$ is closed analytic. It follows that every local irreducible component of $A$ is a component of $A_{\mathrm{all}}$: a proper analytic subset of an irreducible component of dimension $n$ has smaller dimension. Conversely $A$ is the union of the components so obtained.

In a dense open subset of each such component choose $q$ smooth in the full set $A_{\mathrm{all}}$, excluding its intersections with other components. Apply FH46 to $A_{\mathrm{all}}$ at $q$. After shrinking $U$, this gives

$$
\operatorname{graph}(dh)\cap A_{\mathrm{all}}\cap T^*U=\{q\}.
\tag{FH52}
$$

If $z\in S\cap f^{-1}(U)$ is a critical point of $(h\circ f)|_S$, then

$$
d(h\circ f)_z\in T^*_SY\subset\Sigma,
\tag{FH53}
$$

where the first membership means the covector based at $z$. The argument of FH49 now places $z$ in $f^{-1}(x)$. Thus the critical points on all source strata form a finite set, and each is isolated locally. At every point of $C_q$ in FH50, the Whitney tangency property makes the covector annihilate the tangent of its actual stratum, so it is one of these stratified critical points. This permits the local stratified Morse calculation to use the full adapted stratification. It needs no assertion that strata with zero normal-Morse data can be discarded before choosing a neighborhood or perturbing the test.

## SH02-FH-PERVERSE-FINITE — Finite direct image and the perverse degree

This section uses the bounded middle-perverse t-structure on complex-constructible sheaves over a field $K$. Its existence, and the normal Morse description below, are geometric prerequisites from the constructible and perverse course. No perverse truncation over the original coefficient ring $k$ is used.

Locally, fix a finite complex stratification on which all the sheaves in question are constructible. For a stratum $S$ of complex dimension $d$, the middle-perverse conditions on a complex $P$ are

$$
P_y\in D^{\leq-d}(K),\qquad
(i_y^!P)\in D^{\geq d}(K)\quad(y\in S).
\tag{FH17}
$$

The first condition describes the nonpositive half of the t-structure and the second the nonnegative half. Here $i_y$ is the inclusion of a point; its exceptional inverse image is a complex of $K$-vector spaces. A common refinement does not change these conditions: they express the intrinsic stalk-support and costalk-support dimension conditions.

**Finite perverse exactness.** If $f:Y\to X$ is finite holomorphic, then $Rf_*$ preserves both halves of this t-structure. Consequently it commutes with all perverse cohomology functors.

**Proof.** Choose compatible complex stratifications for $f$ and $P$ such that every source stratum $S$ maps to a target stratum $T$ by a local biholomorphism. Some target strata have empty inverse image; on them the direct image is zero. Finiteness makes the dimensions of nonempty corresponding strata equal. The existence of this compatible analytic refinement is the same finite-map stratification input used below, and is not a consequence of the stalk calculation alone.

For $x\in T$, FH4 gives

$$
(Rf_*P)_x\simeq\bigoplus_{f(y)=x}P_y.
\tag{FH18}
$$

All source strata through these points have complex dimension $\dim T$. Thus the nonpositive condition in FH17 is preserved. To check the other half, apply FH6 to the closed subset $\{x\}$ and then take its stalk. On a neighborhood of any $y\in f^{-1}(x)$ disjoint from the other points, support in the finite fibre is support at $y$. Therefore the actual localization comparison gives

$$
i_x^!Rf_*P\simeq\bigoplus_{f(y)=x}i_y^!P.
\tag{FH19}
$$

This proves the required nonnegative bound. Both sums are finite and exact, so no spectral-sequence degeneration is being asserted. The preceding adapted-covering proof supplies membership in the constructible category; its boundedness and finite-dimensional stalks already follow from FH18.

An exact functor preserving the two halves carries the defining truncation triangle to a truncation triangle. Uniqueness of that triangle gives natural comparisons with perverse truncation and hence

$$
{}^pH^j(Rf_*P)\simeq Rf_*\,{}^pH^j(P).
\tag{FH20}
$$

This proves the last assertion. $\square$

For later use record precisely the Morse input to perverse support. At a generic point of each connected conormal component, let $\mu_\alpha$ be the normal Morse functor with the perverse normalization. The input says that $\mu_\alpha$ is exact for the perverse and ordinary t-structures, and that a component belongs to the microsupport exactly when its Morse complex is nonzero. It follows that

$$
\operatorname{SS}(B)=\bigcup_j\operatorname{SS}({}^pH^jB)
\tag{FH21}
$$

for every bounded complex-constructible $B$ over $K$. Indeed exactness gives $\mu_\alpha({}^pH^jB)\simeq H^j(\mu_\alpha B)$; a bounded complex of vector spaces is zero if and only if all its cohomology groups vanish. Apply the conormal description to each side. The bounded perverse t-structure makes the union finite locally. This argument neither splits $B$ into its perverse cohomology objects nor assumes that the perverse category is semisimple.

## SH02-FH-POSITIVE-INDEX — What isolated holomorphic detection requires

For a perverse sheaf $P$ over an arbitrary field $K$, use integer multiplicities

$$
\operatorname{CC}(P)=\sum_\alpha
\dim_K\mu_\alpha(P)\,[\Lambda_\alpha].
\tag{FH22}
$$

The complex conormal components carry their complex orientations. The nonzero coefficients are positive integers, and the support of this cycle is $\operatorname{SS}(P)$ by the normal Morse description. The integers in FH22 are not reduced modulo the characteristic of $K$.

For a holomorphic $g$, denote its supported local test by

$$
M_g(P)_y=
\bigl(R\Gamma_{\{\operatorname{Re}g\geq\operatorname{Re}g(y)\}}P\bigr)_y.
$$

Let $\Lambda_{\mathcal S}$ be the union of all closed conormals of a finite local adapted complex Whitney stratification, including invisible strata. We need the following specialization of the isolated local index theorem. If $dg$ meets $\Lambda_{\mathcal S}$ only at an isolated point over $y$ after shrinking, then

$$
\chi_K(M_g(P)_y)
=\sum_\alpha \dim_K\mu_\alpha(P)\,
I_{(y,dg_y)}(\Lambda_\alpha,\operatorname{graph}(dg)).
\tag{FH23}
$$

Here $\chi_K$ is the alternating sum of finite vector-space dimensions, with value in $\mathbb Z$. Each local intersection multiplicity on the right is a strictly positive integer when that component passes through the isolated intersection. Consequently

$$
(y,dg_y)\in\operatorname{SS}(P),\quad
\operatorname{graph}(dg)\cap\Lambda_{\mathcal S}
\text{ isolated at }(y,dg_y)
\quad\Longrightarrow\quad
M_g(P)_y\not\simeq0.
\tag{FH24}
$$

The implication is proved by FH22--FH23: at least one positive term occurs and no negative term occurs. A zero complex has zero integer Euler characteristic. This also covers $dg_y=0$. If $g$ is locally constant on the support, isolation forces that support to be zero-dimensional near $y$, and its supported local test is $P_y$, which gives the same conclusion.

Equation FH23 is a geometric input, not proved by positivity alone. It is the integer-dimensional local-supported index formula. Its scope is substantially smaller than FH14: only an isolated intersection is required, but it must hold over every field. The local-supported index belongs to the index theory of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), whose coefficient-valued trace must be strengthened to this integer formula by the Morse filtration argument. A related all-field integer antecedent is Massey's *A Little Microlocal Morse Theory*, Theorem 2.1 and Remark 2.2. Reducing a positive integer modulo the characteristic would destroy the argument. The following finite filtration explains exactly which geometric content makes the integer refinement valid.

### SH02-FH-MORSE-FILTRATION — The integer index from the actual filtration

Here is the deduction from the controlled Morse input, including its degree and integer normalization. Work near a point $y$ with no other stratified critical point of $g$. For a stratum $S_\alpha$ of complex dimension $d_\alpha$, write $N_\alpha(P)$ for its normal Morse complex and

$$
\mu_\alpha(P)=N_\alpha(P)[-d_\alpha].
\tag{FH54}
$$

It is a finite-dimensional vector space in degree zero by the perverse normal-Morse input. At a stratified holomorphic Morse point on a stratum of dimension $d$, holomorphic Morse coordinates express the tangential function as a nondegenerate sum of complex squares. Its real part has $d$ negative and $d$ positive real squares. The tangential relative handle therefore shifts the normal complex by $[-d]$, exactly as in FH54; there is no further shift depending on the ambient dimension.

Choose the controlled perturbation and its relative pair. The pair includes the whole small cluster of perturbed critical points, between regular levels below and above their critical values. Its complex is identified with the original $M_g(P)_y$ by the stipulated boundary continuation; it is not the stalk of the perturbed test at the old point. The finite relative Morse filtration supplies distinguished triangles

$$
F_{r-1}\longrightarrow F_r\longrightarrow V_r
\longrightarrow F_{r-1}[1],
\qquad F_0=0,\quad F_N=M_g(P)_y,
\tag{FH55}
$$

where $V_r$ is the normalized Morse vector space at the $r$th point. The cohomology long exact sequence proves by induction that every $F_r$ is concentrated in degree zero, and gives

$$
0\longrightarrow H^0(F_{r-1})\longrightarrow H^0(F_r)
\longrightarrow V_r\longrightarrow0.
\tag{FH56}
$$

Taking dimensions gives $\dim_K H^0(M_g(P)_y)=\sum_r\dim_KV_r$. The local analytic conservation of intersection number groups these points by their conormal components. If $n_\alpha$ is their number on the generic conormal of $S_\alpha$, the result is

$$
\dim_K H^0(M_g(P)_y)
=\sum_\alpha n_\alpha\dim_K\mu_\alpha(P)
=\sum_\alpha I_{(y,dg_y)}
 (\Lambda_\alpha,\operatorname{graph}(dg))\,
 \dim_K\mu_\alpha(P).
$$

This is FH23 with values in $\mathbb Z$, and proves more than its Euler-characteristic version. No splitting of FH56 is chosen. An invisible stratum has $V_r=0$ and contributes zero. If a visible conormal passes through the isolated intersection, both its Morse dimension and its intersection multiplicity are positive, so the local test is nonzero in every characteristic.

For a sign check take $P=K_{\mathbb C}[1]$ and $g(z)=z^2$. The negative region of $\operatorname{Re}g$ has two local components. Its relative complex with the disc is $K[-1]$, and the shift $[1]$ gives the local test $K$ in degree zero. The complex intersection with the zero section has multiplicity one. A point sheaf with a constant test also gives a degree-zero vector space and intersection multiplicity one. These checks include a zero pulled-back covector and agree with the stated normalization.

The construction of the controlled pair and perturbation is supplied by [the isolated-test lesson](isolated-holomorphic-morse-tests.md#SH02-IHM-BOUNDARY) at the precise scope stated above. A genericity statement alone would not prove FH55, and a field-valued trace would not prove the integer equality. This deduction explicitly records both distinctions.

## SH02-FH-FIELD-FINITE — Reverse inclusion from isolated source tests

Assume the explicit normal Morse and isolated index inputs above, together with the analytic stratification input in the finite conormal-image lemma. Then FH1 holds for every field $K$ and every bounded complex-constructible $B$ of $K$-sheaves.

**Proof for a perverse sheaf.** Put $\Lambda=\operatorname{SS}(P)$ and

$$
A=f_\pi f_d^{-1}\Lambda.
\tag{FH25}
$$

The geometric lemma makes $A$ a closed complex analytic conic Lagrangian subset of $T^*X$. For a finite adapted complex Whitney stratification $\mathcal S$ of the source neighborhood, also put

$$
\Lambda_{\mathcal S}=\bigcup_{S\in\mathcal S}\overline{T^*_S Y},
\qquad A_{\mathcal S}=f_\pi f_d^{-1}\Lambda_{\mathcal S}.
$$

Apply the same geometric lemma to $\Lambda_{\mathcal S}$. Thus $A_{\mathcal S}$ is a finite union of complex Lagrangian components and contains $A$. Since both sets are pure of the target dimension, every local irreducible component of $A$ is an irreducible component of $A_{\mathcal S}$. Indeed a proper analytic subset of an irreducible analytic set has smaller dimension. It is enough to prove the desired inclusion on a dense subset of each component of $A$, because microsupport is closed.

Choose $a=(x,\eta)$ on such a component, smooth on $A_{\mathcal S}$ and disjoint from its other local components. The holomorphic-test lemma supplies a holomorphic quadratic germ $h$ at $x$ with $dh_x=\eta$ and with its differential graph meeting $A_{\mathcal S}$ only at $a$ on a sufficiently small cotangent neighborhood. This stronger choice will make the source critical points isolated for the entire adapted stratification, including its invisible strata.

There is a useful further shrinking here. A covector $dh_z$ tends to $\eta$ as $z$ tends to $x$. Thus, after shrinking the base, its graph stays in the chosen cotangent neighborhood. FH2 separates the finitely many points over $x$, and properness ensures that the inverse image of the smaller base is contained in their union. For any such point $y$, a source stratified critical point of $h\circ f$ in its neighborhood maps to an intersection of $\operatorname{graph}(dh)$ with $A_{\mathcal S}$. The target intersection is only $a$; the finite fibre has no accumulation points. Hence every source stratified critical point over $x$ is isolated, and there are finitely many of them. At least one is characteristic for $P$ because $a\in A$.

Choose one such $y$. FH24 gives a nonzero supported local test $M_{h\circ f}(P)_y$. The actual localization comparison FH7 identifies

$$
\bigl(R\Gamma_{\{\operatorname{Re}h\geq\operatorname{Re}h(x)\}}Rf_*P\bigr)_x
\simeq\bigoplus_{f(y')=x}M_{h\circ f}(P)_{y'}.
\tag{FH26}
$$

Its summand at $y$ is nonzero, so the left side is nonzero. This is one of the actual real tests in the definition of microsupport, with differential $\operatorname{Re}\eta$ at $x$. Consequently $(x,\operatorname{Re}\eta)\in\operatorname{SS}(Rf_*P)$. The real-part identification is FH15 and commutes with $df$. No nearby-cycle or vanishing-cycle comparison is used in this step.

This proves the reverse inclusion on the stated dense subset. Closedness extends it to all of $A$. The other inclusion is the proper direct-image estimate. Empty microsupport gives the zero object and no components. Zero covectors also follow immediately from the support equality FH4, independently of the generic argument.

**Passage to a bounded complex.** By FH20--FH21,

$$
\begin{aligned}
\operatorname{SS}(Rf_*B)
&=\bigcup_j\operatorname{SS}(Rf_*\,{}^pH^jB)\\
&=\bigcup_j f_\pi f_d^{-1}\operatorname{SS}({}^pH^jB)\\
&=f_\pi f_d^{-1}\operatorname{SS}(B).
\end{aligned}
\tag{FH27}
$$

Images and inverse images commute with these unions. There is no cancellation between degrees in this argument, because FH21 detects the individual normal Morse cohomology groups before the image is taken. $\square$

## SH02-FH-RING-FINITE — Recovering every original coefficient ring

We can now prove the original-ring statement using only the normal Morse part of FH12; the coefficient comparison for arbitrary vanishing-cycle limits in FH13 is unnecessary for this route.

First, for every bounded complex-constructible $G$, the finite normal Morse models and FH11 give the pointwise equality

$$
\operatorname{SS}_k(G)=\bigcup_{\mathfrak p\in\operatorname{Spec}k}
\operatorname{SS}_{\kappa(\mathfrak p)}
\bigl(G\otimes_k^L\kappa(\mathfrak p)\bigr).
\tag{FH28}
$$

To prove it, choose a local finite adapted stratification. A covector in the left side belongs to the closure of one visible conormal component. Its perfect Morse object is detected by one residue field, by FH11, and the finite model from FH16 identifies the resulting Morse object with the coefficient-changed one. That same entire conormal closure therefore occurs on the right. Conversely tensoring a zero Morse object gives zero, so no new component is introduced. This proves equality at boundary covectors as well as generic ones. It does not take the closure of an infinite union.

Second, the natural projection comparison is an isomorphism

$$
(Rf_*G)\otimes_k^L L\xrightarrow{\sim}
Rf_*(G\otimes_k^L L)
\tag{FH29}
$$

for a finite proper $f$ and a coefficient complex $L$. On a stalk it is the canonical map

$$
\left(\bigoplus_{f(y)=x}G_y\right)\otimes_k^L L
\longrightarrow\bigoplus_{f(y)=x}(G_y\otimes_k^L L),
$$

which is an isomorphism. This identifies the actual comparison: the adjunction map restricts a section to each germ and then tensors it, exactly as FH3 does. A K-flat coefficient resolution computes the displayed map if a complex representative is desired. Thus FH29 uses a finite sum, and no general commutation of tensor with an infinite direct image is needed.

**Proof of FH1 over $k$.** Write $G_{\mathfrak p}=G\otimes_k^L\kappa(\mathfrak p)$. Its stalks are bounded finite-dimensional complexes over the residue field. The finite global dimension of $k$ keeps the sheaf complex bounded. Apply FH28 on $X$, then FH29, the field theorem FH27, and FH28 on $Y$:

$$
\begin{aligned}
\operatorname{SS}_k(Rf_*G)
&=\bigcup_{\mathfrak p}
\operatorname{SS}_{\kappa(\mathfrak p)}(Rf_*G_{\mathfrak p})\\
&=\bigcup_{\mathfrak p}
 f_\pi f_d^{-1}\operatorname{SS}_{\kappa(\mathfrak p)}(G_{\mathfrak p})\\
&=f_\pi f_d^{-1}\operatorname{SS}_k(G).
\end{aligned}
\tag{FH30}
$$

Finite direct image is bounded and has perfect stalks by FH4; weak complex constructibility is proved in `SH02-FH-CONSTRUCTIBLE-IMAGE` from the same compatible analytic stratification input already used for FH17. Thus every application of FH28 is legitimate. The zero ring gives empty microsupports on both sides. There is no original-ring perverse t-structure, rank cancellation, division by the finite degree, flatness assumption on $f$, or characteristic-zero coefficient assumption in the proof. $\square$

This route uses the four prerequisite lessons linked in [the geometric inputs](#SH02-FH-INPUTS), with their exact external theorem statements retained. It does not require the full critical-support equivalence FH14, the general Milnor coefficient comparison FH13, or any nearby-cycle/vanishing-cycle comparison. The general nearby-cycle proof supplies the Milnor coefficient comparison. The critical-support theorem is proved in [its own lesson](../general-critical-support.html) and remains separate from the dependency chain of FH30.

## SH02-FH-MONOMIAL-CURVE — A full cotangent fibre created by a finite parametrization

Take relatively prime integers $2\leq a<b$ and the map

$$
f:\mathbb C\longrightarrow\mathbb C^2,\qquad
f(t)=(t^a,t^b).
\tag{FH31}
$$

It is proper because a bound on $|t^a|$ bounds $|t|$. It is injective: if two nonzero parameters have the same image, their quotient is both an $a$th and a $b$th root of unity, and hence is one; the fibre over zero is also a singleton. Thus $f$ is finite. Away from zero it is an immersion and gives a smooth embedded curve locally. Denote its image by $C$ and its smooth part by $C^\circ$.

For any nonzero commutative coefficient ring $k$, put $A=f_*k_{\mathbb C}$. Then

$$
\operatorname{SS}(A)=
\overline{T^*_{C^\circ}\mathbb C^2}\ \cup\ T^*_{\{0\}}\mathbb C^2.
\tag{FH32}
$$

The real and complex conormals are identified by FH15. This example has an original direct proof using supported tests, without invoking the general finite holomorphic equality.

**Proof.** Away from zero the closed-embedding formula computes microsupport as the conormal of the smooth image; outside $C$ the sheaf vanishes. Its microsupport is closed, so it contains the conormal closure. It remains to show that every nonzero covector at the origin occurs. Write its holomorphic representative as $\eta=\alpha\,dz_1+\beta\,dz_2$ and test with the real part of $h(z_1,z_2)=\alpha z_1+\beta z_2$.

The pullback is $g(t)=\alpha t^a+\beta t^b$. If $\alpha\ne0$, its vanishing order is $a$; if $\alpha=0$, then $\beta\ne0$ and the order is $b$. Write that order as $m\geq2$. A holomorphic unit has a holomorphic $m$th root on a sufficiently small disc. The resulting coordinate $s=t\,u(t)^{1/m}$ is a local biholomorphism and changes $g$ into $s^m$.

In a sufficiently small round $s$-disc, the open set $\operatorname{Re}(s^m)<0$ consists of $m$ disjoint contractible sectors. The restriction map on cohomology from the disc to that set is the diagonal $k\to k^m$. The support triangle therefore gives

$$
\bigl(R\Gamma_{\{\operatorname{Re}g\geq0\}}k_{\mathbb C}\bigr)_0
\simeq\operatorname{Cone}(k\xrightarrow{\mathrm{diag}}k^m)[-1]
\simeq k^{m-1}[-1].
\tag{FH33}
$$

The isomorphism is stable under smaller such discs, so it computes the stated stalk. The last complex is nonzero over every nonzero $k$. FH7, whose proof used finite properness and localization alone, identifies it with the test complex for $A$ and $\operatorname{Re}h$ at zero. Thus this actual test does not vanish, and the defining microsupport criterion puts $\operatorname{Re}\eta$ in $\operatorname{SS}(A)$. The zero covector belongs by the nonzero stalk. This proves the reverse containment in FH32. The forward containment follows from the already computed smooth points and the fact that the only point of $C\setminus C^\circ$ is zero. $\square$

For comparison the cotangent correspondence of the source zero section is given before projection by

$$
t^{a-1}\bigl(a\eta_1+b\eta_2t^{b-a}\bigr)=0.
\tag{FH34}
$$

Its component at $t=0$ is the whole target covector plane. Its other component closes the conormal relation along the smooth image. Thus the two components in FH32 are also exactly what the finite conormal-image construction predicts. The point component cannot be dropped by computing only at unramified parameters.

**Exercise.** At $\eta=dz_2$, compare the rank of the supported test in FH33 with its rank at $\eta=dz_1$. Does the larger rank force an additional irreducible component of the set in FH32?

**Solution.** The ranks are respectively $b-1$ and $a-1$. Both covectors already lie in the same full cotangent fibre at zero. Microsupport records nonvanishing and its closed set of directions, so a change in the dimension of a particular test does not itself force a new set component. The calculation also shows why an integer multiplicity contains more information than the underlying microsupport set.

## SH02-FH-GEOMETRIC-CONTRACT — An alternative through full critical support

[Holomorphic critical support and graph covectors](../general-critical-support.html) proves the full critical-support equivalence FH14 at the original coefficient scope. It includes singular and nonisolated critical loci, closed support on the fixed level, visible normal slicing, a direct radial-boundary proof and the actual finite Morse filtration and scalar maps.

[Finite nearby-cycle models for an arbitrary holomorphic function](../general-nearby-cycle-models.html) proves the full finite-model and coefficient contract FH13, including singular and nonisolated critical loci. Its cofinal restrictions compute the actual specialization unit, its unshifted cone and the original deck action. The [critical-support proof](../general-critical-support.html) supplies FH14 for the original coefficient ring by its actual residue-field comparison.

This alternative route uses stronger analytic inputs than FH30. They are retained as precise dependency contracts for the critical-support theorem itself. They are not required by the finite-map proof above and are not established by its algebraic lemmas.

**Finite local data.** A complex-constructible $A$ has, locally, a finite complex Whitney stratification with connected strata $S_\alpha$ and normal Morse complexes $M_\alpha(A)$. These complexes are perfect and have finite cellular models compatible with derived change of coefficients. They give the precise description

$$
\operatorname{SS}(A)=
\bigcup_{M_\alpha(A)\not\simeq0}\overline{T^*_{S_\alpha}X}.
\tag{FH12}
$$

Here the conormals are identified with real covectors as below. For each fixed local holomorphic function $h$, its vanishing cycles are constructible with perfect stalks and finite local models satisfying

$$
\Phi_h(A)\otimes_k^L L\simeq\Phi_h(A\otimes_k^L L)
\tag{FH13}
$$

for $L=\kappa(\mathfrak p)$. The models must compute the specialization morphism as well as its source and target. The comparison must be local on the zero fibre. Proper holomorphic direct image preserves weak complex constructibility; in the finite case perfection of its stalks is already proved by FH4. These are exact constructible-geometry prerequisites, not consequences of properness alone.

**Field critical support.** For every field $K$, every bounded complex-constructible complex $B$ of $K$-sheaves, every holomorphic function $h$ on a complex manifold, and every $z$,

$$
(z,d\operatorname{Re}h_z)\in\operatorname{SS}(B)
\quad\Longleftrightarrow\quad
z\in\operatorname{Supp}\bigl(\Phi_{h-h(z)}B\bigr).
\tag{FH14}
$$

This assertion concerns closed support. It includes singular critical loci, nonisolated critical points, and functions constant on a component. It cannot be replaced by an isolated Morse-point calculation or by vanishing of the single stalk at $z$.

The exact field statement is available as a mathematical antecedent in Massey's Corollary 4.15; its proof passes through the critical-support theorem for perverse sheaves and a description by visible conormals. Those results use characteristic-cycle positivity and the vanishing-cycle cycle formula. Establishing their required scope and proof is still necessary; a generic reference to perverse sheaves does not supply that verification.

## SH02-FH-RING-EXTENSION — Why the field criterion suffices for the source ring

Assuming FH12–FH14 at their exact stated scopes, FH14 holds with the original ring $k$ in place of $K$.

**Proof.** Work in a neighborhood having the finite stratification in FH12. Suppose $(z,d\operatorname{Re}h_z)\in\operatorname{SS}(A)$. Some stratum $S_\alpha$ has this covector in its closed conormal and has $M_\alpha(A)\not\simeq0$. By FH11 choose one prime $\mathfrak p$ for which

$$
M_\alpha(A)\otimes_k^L\kappa(\mathfrak p)\not\simeq0.
$$

The coefficient-compatible normal model and FH12 over $\kappa(\mathfrak p)$ put that same covector in $\operatorname{SS}(A\otimes_k^L\kappa(\mathfrak p))$. FH14 over this single field puts $z$ in the closed support of its vanishing cycles. By FH13 this closed support is contained in $\operatorname{Supp}(\Phi_{h-h(z)}A)$: a zero stalk remains zero on tensoring, and taking closures preserves containment.

Conversely, suppose $z\in\operatorname{Supp}(\Phi_{h-h(z)}A)$. Choose points $z_n\to z$ where these vanishing cycles have nonzero stalks. Their stalks are perfect by the finite local-data contract. FH11 gives primes $\mathfrak p_n$ detecting them. FH13 and the field implication in FH14 show

$$
(z_n,d\operatorname{Re}h_{z_n})\in
\operatorname{SS}(A\otimes_k^L\kappa(\mathfrak p_n))
\subset\operatorname{SS}(A).
$$

The last inclusion follows from FH12: a normal Morse complex that was zero stays zero after tensoring. Closedness of microsupport and continuity of $dh$ give the required covector at $z$. If $z$ itself has a nonzero stalk, one may take the constant sequence. No single prime is chosen uniformly over all points or all tests, and no interchange of an infinite union with closure is used. $\square$

The role of perfection is explicit. Neither ranks nor Euler characteristics detect an arbitrary torsion complex, whereas FH11 does. Finite global dimension keeps $A\otimes_k^L\kappa(\mathfrak p)$ bounded uniformly; its stalks become bounded finite-dimensional vector-space complexes because the original stalks are perfect.

## SH02-FH-EQUALITY — The finite-map argument

Assume the analytic contracts in `SH02-FH-GEOMETRIC-CONTRACT`. Then FH1 holds at the full coefficient and constructibility generality stated at the beginning.

**Proof.** Identify a holomorphic covector $\theta$ with the real covector $\operatorname{Re}\theta$. The inverse identification sends a real covector $\eta$ to

$$
\theta(v)=\eta(v)-i\eta(Jv),
\tag{FH15}
$$

where $J$ is the complex structure. This is complex linear, has real part $\eta$, and commutes with pullback by a holomorphic differential. There is no sign reversal in this identification.

The proper-image estimate in microsupport operations gives the inclusion from left to right in FH1. For the other inclusion take $(x,\eta)$ on its right side and choose $y\in f^{-1}(x)$ with $(y,df_y^t\eta)\in\operatorname{SS}(G)$. Choose holomorphic coordinates near $x$ and the affine holomorphic function $\ell$ with $d\ell_x=\theta$ from FH15. Shrink the target neighborhood and restrict $f$ to its full inverse image; this is still finite and proper.

The ring version of FH14 applied to $\ell\circ f$ gives

$$
y\in\operatorname{Supp}\bigl(\Phi_{\ell\circ f-\ell(x)}G\bigr).
$$

Equation FH10 therefore gives

$$
x\in\operatorname{Supp}\bigl(\Phi_{\ell-\ell(x)}Rf_*G\bigr).
$$

The weak constructibility part of the geometric contract and the perfect-stalk formula FH4 show that $Rf_*G$ is complex-constructible. Apply the converse direction of the ring criterion to obtain $(x,\eta)\in\operatorname{SS}(Rf_*G)$.

The argument also permits $df_y^t\eta=0$. If $\eta=0$, the result follows even without the analytic criterion: the zero section of microsupport is closed support, and FH4 identifies those supports. The empty fibre contributes nothing. No hypothesis that $f$ is a covering, flat, surjective, or equidimensional was imposed. $\square$

## SH02-FH-CHECKS — Examples and exercises

**Branching over arbitrary coefficients.** Let $f:\mathbb C\to\mathbb C$ be $z\mapsto z^m$, $m\geq2$, and take $G=k_{\mathbb C}$. At zero the source stalk is $k$ and a nearby fibre has $m$ points, so the specialization map for the target coordinate is the diagonal

$$
k\longrightarrow k^m.
$$

Its cone is $k^{m-1}$ in degree zero with the convention FH8: subtract the first coordinate from the others to identify its cokernel, and note that its kernel is zero. For $k\neq0$ this detects every nonzero target direction at zero by rotating the coordinate. Away from zero the pushforward is a local system. The resulting microsupport is the zero section together with the full cotangent fibre at zero. This calculation works in characteristics dividing $m$ and does not use the trace divided by $m$.

**Why the real calculation differs.** For the proper homeomorphism $t\mapsto t^3$ of the real line and $G=k_{\mathbb R}$, the pushforward is constant. At zero the differential vanishes, so the right side of FH1 would contain the full cotangent fibre, while the left side is only the zero section for $k\neq0$. FH7 still holds; the analytic critical-support theorem is the step unavailable in this example.

**Exercise 1.** Show that a finite proper map detects zero objects: $Rf_*A\simeq0$ implies $A\simeq0$. Explain why this statement for an arbitrary proper map fails.

**Solution.** Each $A_y$ is a direct summand of $(Rf_*A)_{f(y)}$ by FH4, so every stalk is zero. A proper projection can instead have nonzero fibre sheaves with zero total cohomology. For example, on a circle a rank-one local system over a field with monodromy $a\neq1$ has cochain complex $K\xrightarrow{a-1}K$, which is acyclic; push it to a point.

**Exercise 2.** If $h$ is constant, compute $\psi_{h-h(z)}A$ and $\Phi_{h-h(z)}A$. What does FH14 say in this case?

**Solution.** The punctured inverse image is empty, so nearby cycles are zero and FH8 gives $\Phi_{h-h(z)}A=A[1]$. Its closed support is $\operatorname{Supp}(A)$. Since $dh=0$, the criterion reduces to the zero-section support identity. This case must be treated directly if one proves the analytic criterion using projectivized characteristic cycles: projectivization discards the zero section.

**Exercise 3.** In FH11, why does checking only the fraction field of an integral domain fail?

**Solution.** The perfect complex $[\mathbb Z\xrightarrow{2}\mathbb Z]$ is nonzero, while its tensor with $\mathbb Q$ is acyclic. Tensoring with $\mathbb F_2$ detects it. The argument uses residue fields at all primes, with a prime chosen for the particular perfect datum.

## SH02-FH-ANTECEDENTS — Attribution and unresolved proof boundary

The finite holomorphic equality goes back to Kashiwara's work on systems of microdifferential equations; the micro-support form used here belongs to the theory of M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985). The finite-fibre, localization, cycle-comparison and coefficient-reduction arguments are proved here.

The analytic antecedent used to locate the remaining precise theorem is David B. Massey, [*A Little Microlocal Morse Theory*, arXiv:math/0006185v2](https://arxiv.org/abs/math/0006185v2), Corollary 4.15. It is stated over a principal ideal domain, so its field specialization has the required coefficient scope for FH14. Its proof depends on a perverse critical-support theorem and a visible-conormal description.

The primary finite-map proof is FH30. Its analytic, normal-Morse, field-perverse and controlled stratified Morse inputs are supplied by the four lessons linked in [the geometric prerequisites](#SH02-FH-INPUTS), relative to their exact external theorem statements. The finite image geometry, symmetric-Hessian test, finite constructibility and perverse exactness, integer filtration deduction, direct support comparison and residue-field recovery are supplied explicitly. The earlier FH14 route remains an alternative using the [proved critical-support theorem](../general-critical-support.html). The [general nearby-cycle proof](../general-nearby-cycle-models.html) supplies FH13 independently; FH13–FH14 do not lie on the primary proof chain.
