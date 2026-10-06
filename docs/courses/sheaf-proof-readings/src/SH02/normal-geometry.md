# SH02-NG-UNIT — Normal geometry as a family with a central fibre

The geometric arguments use the differential-topology prerequisites stated below. This lesson develops the geometric input to specialization; it does not establish the sheaf-theoretic specialization theorems.

The purpose of the deformation parameter is to put two kinds of observation in one space. Away from parameter zero we see the original manifold. At parameter zero we see displacement vectors normal to a submanifold. A subset of the original manifold then determines a closed set of possible limiting displacements. The topology of this family, particularly at zero normal vectors, controls the neighborhoods used by specialization.

The geometric starting points are [Kashiwara and Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), §1.2.1 (printed p. 15) and §2.2.1 (printed pp. 41–43), and [Schapira, *A short review on microlocal sheaf theory*, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §2.1, equations (2.5)–(2.6), and §4.2. The first gives the scaled-difference definition of a pair cone and the gluing construction of the deformation. The review compares those coordinates with the closure in the positive chamber. We prove their equivalence here, then supply the clean-map estimate, signed relative orientation, and neighborhood refinements needed by the later sheaf arguments.

## SH02-NG-PREREQUISITES — Prerequisites and notation

Local identifier: `SH02-NG-PREREQUISITES`

All manifolds are finite dimensional and countable at infinity. Maps and submanifolds are either smooth or real analytic. We initially take an embedded **closed** submanifold $i:M\hookrightarrow X$. For a locally closed submanifold, choose an open ambient neighborhood in which it is closed; the constructions involving the normal bundle agree after restriction to smaller such neighborhoods. A global deformation of all of $X$ below uses closedness.

The arguments use the following differential-topology inputs: adapted coordinate charts for embedded submanifolds; the inverse and constant-rank theorems; smooth partitions of unity and bundle metrics; and a smooth tubular neighborhood of a closed embedded submanifold. These are explicit prerequisite contracts, not claims that the sheaf-theoretic open-foundation imports already prove them. In the real analytic case the deformation and its functorial maps are real analytic; the auxiliary neighborhood proof is a topological proof and may use a smooth tubular neighborhood of the underlying smooth manifolds.

The normal bundle is

$$
E=N_MX=(TX|_M)/TM,
\qquad \tau:E\longrightarrow M.
$$

No coefficient ring is needed for the geometric results. When orientation sheaves are mentioned, use the course's commutative coefficient ring $k$ of finite global dimension; neither orientability nor constructibility is assumed. For a vector bundle, “conic” means invariant under multiplication by every positive real number, including invariance in both directions.

## SH02-NG-CONSTRUCTION — The deformation manifold and its maps

Local identifier: `SH02-NG-CONSTRUCTION`

As a set put

$$
\mathcal D_MX=(X\times\mathbb R^\times)\sqcup E.
$$

The two pieces are not given their disjoint-union topology. Write $n=\dim X$ and $r=\operatorname{codim}M$. Let $(u,z)$ be an adapted coordinate chart on $X$, with $u\in\mathbb R^r$ and $M=\{u=0\}$. The deformation chart is the open set

$$
\widetilde U=\{(v,z,t):(tv,z)\in U\}
\subset\mathbb R^{r}\times\mathbb R^{\dim M}\times\mathbb R.
$$

For $t\ne0$, its point $(v,z,t)$ represents $((tv,z),t)$. For $t=0$, it represents the normal vector $v$ based at $(0,z)$. Charts disjoint from $M$ have no central points and describe the usual product with $\mathbb R^\times$.

To verify that this prescription defines a manifold, write a change of adapted coordinates as

$$
(u,z)\longmapsto (a(u,z),b(u,z)),\qquad a(0,z)=0.
$$

Its deformation is

$$
(v,z,t)\longmapsto
\begin{cases}
\bigl(t^{-1}a(tv,z),b(tv,z),t\bigr),&t\ne0,\\
\bigl(D_u a(0,z)v,b(0,z),0\bigr),&t=0.
\end{cases}
$$

The first component extends smoothly because locally

$$
\frac{a(tv,z)}{t}
=\int_0^1D_u a(stv,z)v\,ds.
$$

The formula is needed only near $t=0$, where the intervening segment lies in the coordinate domain. For analytic coordinates, divisibility of the analytic function $a(tv,z)$ by $t$ gives an analytic extension. Applying the same construction to the inverse coordinate change proves that the extended maps are diffeomorphisms. Composition agrees for $t\ne0$ and hence, by continuity, at $t=0$. Thus the cocycle identities hold.

This also proves independence of the chosen adapted atlas. Take the union of two adapted atlases: every mixed transition has the same extension just constructed, and the cocycle identity holds on each mixed overlap. The identity map on the set underlying the deformation is consequently a diffeomorphism between the two resulting structures. Its central restriction is the identity on the normal quotient, rather than an unspecified bundle isomorphism.

Here are the separation and countability details. The functions

$$
p:\mathcal D_MX\longrightarrow X,
\qquad t:\mathcal D_MX\longrightarrow\mathbb R
$$

are given by $p(v,z,t)=(tv,z)$ and the last coordinate. Points with different $p$-values or different $t$-values can be separated using these continuous maps. Distinct remaining central points lie over one point of $M$ and are separated in one deformation chart. A central point and a noncentral point have different $t$-values. This proves Hausdorffness. A countable adapted atlas and the ordinary product charts yield a countable atlas for the deformation. The central coordinate transitions are precisely those of $(TX|_M)/TM$, so the identification of the central fibre with $E$ is intrinsic.

The map $t$ is a submersion. For every $c\ne0$, $p:t^{-1}(c)\to X$ is a diffeomorphism. Also,

$$
p^{-1}(X\setminus M)=(X\setminus M)\times\mathbb R^\times,
\qquad t^{-1}(0)=E.
$$

There is a canonical embedded copy of $M\times\mathbb R$: its point $(m,t)$ has zero normal coordinate in every adapted chart. In particular,

$$
p^{-1}(M)=E\cup(M\times\mathbb R),
\qquad E\cap(M\times\mathbb R)=M\times\{0\}.
$$

The map $p$ on the entire deformation need not be a submersion. On the positive chamber

$$
\Omega=t^{-1}(0,\infty),\qquad
j:\Omega\hookrightarrow\mathcal D_MX,
\qquad p_+=p\circ j,
$$

it is the product projection $X\times(0,\infty)\to X$ under the diffeomorphism $(p,t)$. Let $s:E\hookrightarrow\mathcal D_MX$ be the central embedding. Then $p\circ s=i\circ\tau$.

### SH02-NG-ACTION — Positive scaling and geometric fibres

There is a signed scaling action

$$
c\cdot(v,z,t)=(cv,z,t/c),\qquad c\in\mathbb R^\times.
$$

On $X\times\mathbb R^\times$ this fixes the $X$ coordinate and rescales the parameter. Consequently it is coordinate independent there and, by continuity, everywhere. It restricts on $E$ to ordinary scalar multiplication. Positive scalars preserve $\Omega$. This action keeps the entire zero-vector axis $M\times\mathbb R$; passing only to nonzero normal rays discards that axis and cannot describe neighborhoods of zero normal vectors.

### SH02-NG-PUNCTURED-QUOTIENT — A direction space with a signed radial coordinate

Let $M\subset X$ be a closed embedded submanifold of fixed codimension $r$.
Remove the zero-normal-vector axis from the deformation and form the positive
scaling quotient:

$$
P=\mathcal D_MX\setminus(M\times\mathbb R),\qquad
Q=P/\mathbb R_{>0},\qquad \alpha:P\longrightarrow Q.
$$

The quotient has a canonical smooth manifold structure, and the corresponding
structure is real analytic when the deformation is real analytic. The map
$\alpha$ is a principal $\mathbb R_{>0}$-bundle. The deformation projection
descends to a proper map $b:Q\to X$. Its fibre over $x\notin M$ has two
points, distinguished by the sign of the parameter. Its fibre over $m\in M$
is the positive-ray sphere $S(N_mX)$.

The central quotient $A=(N_MX\setminus M)/\mathbb R_{>0}$ is a closed
embedded hypersurface of $Q$ when $r>0$. Every prescribed smooth section
of $\alpha$ over $A$ extends to a smooth section over $Q$. In particular,
a bundle metric on $N_MX$ gives such a section over $A$ by taking the vector
of norm one on each positive ray. These section assertions concern smooth
maps on the underlying smooth manifolds; they require no real analytic
partition of unity.

**Proof.** On an adapted coordinate neighborhood $U\subset X$, write the
original coordinates as $(u,z)$ and the deformation coordinates as $(v,z,t)$,
where $u=tv$ and $u,v\in\mathbb R^r$. On the part of $P$ above $U$ we have
$v\ne0$. Set

$$
\theta=\frac{v}{\|v\|},\qquad
\rho=t\|v\|,\qquad a=\|v\|.
$$

This gives a diffeomorphism

$$
P\cap p^{-1}U\simeq
Q_U\times\mathbb R_{>0},\qquad
Q_U=\{(\theta,z,\rho):\theta\in S^{r-1},\ (\rho\theta,z)\in U\}.
$$

The inverse is $v=a\theta$ and $t=\rho/a$. In these coordinates positive
scaling fixes $(\theta,z,\rho)$ and sends $a$ to $ca$. Thus the quotient
on this saturated open subset is precisely the open manifold $Q_U$.
The same formulas are analytic: the norm of a nonzero vector is an analytic
positive function. Over an open subset of $X\setminus M$, ordinary product
coordinates identify the quotient with two copies of that subset.

These quotient charts cover $Q$. Their transition maps are obtained by
applying a deformation coordinate change to the representative with $a=1$
and then taking $(\theta,z,\rho)$ in the other chart. They are smooth,
or analytic, with inverses obtained in the same manner. The transition
identities follow from those for deformation coordinates. Their topology
is the quotient topology: the quotient map is open, since the saturation
of an open set is a union of its open translates, and each displayed chart
is the ordinary projection of a product.

To check Hausdorffness, points of $Q$ with different images in $X$ can be
separated using the descended map $b$. Two points above the same $x$ lie
in one of the quotient neighborhoods just described, where they can be
separated. A countable adapted atlas, together with countable sphere atlases
and the two charts away from $M$, gives second countability. The product
descriptions prove the principal-bundle assertion. They also show that
$A$ is the locus $\rho=0$. Its complement is open, because its inverse
image is the invariant open subset of $P$ with $t\ne0$. Hence $A$ is
closed, as well as an embedded hypersurface.

In the adapted quotient chart the descended map is

$$
b(\theta,z,\rho)=(\rho\theta,z).
$$

For compact $K\subset U$, its inverse image is closed in the product
of the compact sphere, the compact set of $z$-coordinates of $K$, and
a bounded closed interval for $\rho$: one may use
$|\rho|=\|u\|\le\max_K\|u\|$. It is therefore compact. Over a
coordinate neighborhood disjoint from $M$ the map is the proper projection
from two copies. These local compactness statements imply global
properness. Explicitly, cover an arbitrary compact $K\subset X$ by
finitely many open sets whose closures are compact and contained in such
coordinate neighborhoods. Intersect those closures with $K$. Their inverse
images are compact by the local calculation and cover $b^{-1}K$; since
$b^{-1}K$ is closed in that finite union, it is compact. The same formula
for $b$ gives the asserted fibres, including the two choices
$(\theta,\rho)=(\pm u/\|u\|,\pm\|u\|)$ when $u\ne0$.

Here are also explicit reasons that sections exist and extend. Choose a
locally finite smooth partition of unity $\chi_i$ on $Q$ subordinate to
principal-bundle charts. In chart $i$, let $a_i:P|_{Q_i}\to\mathbb R_{>0}$
be the fibre coordinate, so $a_i(cx)=c a_i(x)$. The sum

$$
h(x)=\sum_i\chi_i(\alpha(x))a_i(x)
$$

is a smooth positive function with $h(cx)=c h(x)$. Each summand extends
by zero where its partition function vanishes. Normalizing any
representative $x$ to $h(x)^{-1}\cdot x$ consequently defines a smooth
section $\sigma$ of $\alpha$ over all of $Q$.

If $\sigma_0$ is a prescribed smooth section over $A$, there is a unique
smooth function $\lambda:A\to\mathbb R_{>0}$ with
$\sigma_0=\lambda\cdot\sigma|_A$. To extend it, take a smooth tubular
neighborhood of the closed embedded submanifold $A$, compose $\log\lambda$
with its retraction onto $A$, and multiply by a smooth cutoff equal to one
on a neighborhood of $A$ and supported in the tubular neighborhood. Extend
the resulting function by zero outside that neighborhood. This gives a
smooth function $g$ on $Q$ with $g|_A=\log\lambda$, so
$e^g\cdot\sigma$ is the required extension. Tubular neighborhoods and
cutoffs are the differential-topology prerequisites already listed in
SH02-NG-PREREQUISITES.

If $r=0$, then $M$ is open and closed in $X$ and
$P=(X\setminus M)\times\mathbb R^\times$. The quotient is two copies
of the closed submanifold $X\setminus M$, its projection is proper, and
the central subset $A$ is empty. The fibre-coordinate construction still
gives a global section; there is no central extension condition.
$\square$

The quotient describes the punctured deformation. The removed axis is
still present in the original deformation and must be treated separately
when a neighborhood contains a zero normal vector. Thus this auxiliary
construction does not replace the four openness checks in
SH02-NG-INTERVAL-NEIGHBORHOODS.

## SH02-NG-FUNCTORIALITY — Maps of pairs

Local identifier: `SH02-NG-FUNCTORIALITY`

Let $f:Y\to X$ be a map and let $N\subset Y$ and $M\subset X$ be closed embedded submanifolds such that $f(N)\subset M$. Write $f_N:N\to M$ for its restriction. The tangent map induces a fibrewise linear map

$$
\overline{d f}:N_NY\longrightarrow f_N^*N_MX,
$$

and, after the projection to $N_MX$, a normal map $q:N_NY\to N_MX$.

There is a unique smooth, or real analytic, deformation map

$$
\widetilde f:\mathcal D_NY\longrightarrow\mathcal D_MX
$$

that is $(y,t)\mapsto(f(y),t)$ for $t\ne0$ and $q$ on the central fibre. To prove existence, choose adapted source coordinates $(w,z)$ and write $f=(a,b)$ in adapted target coordinates. Since $a(0,z)=0$, the formula

$$
\widetilde f(v,z,t)=
\begin{cases}
\bigl(t^{-1}a(tv,z),b(tv,z),t\bigr),&t\ne0,\\
\bigl(D_w a(0,z)v,b(0,z),0\bigr),&t=0
\end{cases}
$$

extends by the same integral or analytic-divisibility argument used for coordinate changes. It agrees on overlaps by density of $t\ne0$, which also proves uniqueness. Applying uniqueness to compositions and identities proves functoriality.

The equations $t_Y=t_X\circ\widetilde f$ and $p_X\circ\widetilde f=f\circ p_Y$ show that the following three squares are Cartesian:

1. The central-fibre square with horizontal maps $s_Y,s_X$ and vertical maps $q,\widetilde f$.
2. The positive-chamber square with horizontal maps $j_Y,j_X$ and vertical maps $f\times\mathrm{id}_{(0,\infty)},\widetilde f$.
3. The square of product projections $Y\times(0,\infty)\to Y$ and $X\times(0,\infty)\to X$, with vertical maps $f\times\mathrm{id}$ and $f$.

For the first two, taking a fibre or an open inverse image under the common parameter function gives the claimed fibre product, including its topology and smooth structure. The third is the defining Cartesian square for a product projection. The square formed instead by $p_Y,p_X,f,\widetilde f$ need not be Cartesian.

## SH02-NG-CLEAN-DEFINITION — Clean maps, transversality, and closedness

Local identifier: `SH02-NG-CLEAN-DEFINITION`

The conormal bundle is the annihilator

$$
N_M^*X=\{(m;\xi)\in T^*X|_M:\xi|_{T_mM}=0\}.
$$

A map $f:Y\to X$ is **clean with respect to $M$** when $N=f^{-1}(M)$ is an embedded submanifold and the normal differential

$$
\overline{d f}:N_NY\longrightarrow f_N^*N_MX
$$

is injective on every fibre. Equivalently, its dual map $f_N^*N_M^*X\to N_N^*Y$ is surjective. Equivalently,

$$
T_yN=\{v\in T_yY:d f_y(v)\in T_{f(y)}M\}
\qquad(y\in N).
$$

These equivalences are finite-dimensional linear algebra: the kernel of the induced map on normal quotients is the right-hand side of the last formula modulo $T_yN$, and a linear map is injective exactly when its dual is surjective.

A map is **transverse to $M$** when, for every $y\in f^{-1}(M)$,

$$
d f_y(T_yY)+T_{f(y)}M=T_{f(y)}X.
$$

Equivalently, the map from the pulled-back target conormal space to $T_y^*Y$ is injective. In adapted target coordinates $(u,z)$, transversality says that $u\circ f$ is a submersion at its zeros. The submersion theorem then makes $N=f^{-1}(M)$ a submanifold and identifies its tangent space with $\ker d(u\circ f)$. Thus a transverse map is clean and its normal differential is an isomorphism. None of these assertions supposes that $f$ is itself a submersion.

### SH02-NG-CLEAN-EMBEDDING — Clean embedding estimates

**Deformation embedding theorem.** If $f$ is clean with respect to $M$, the natural map

$$
\Phi=(p_Y,\widetilde f):\mathcal D_NY
\longrightarrow Y\times_X\mathcal D_MX
$$

is a closed embedding. If $f$ is transverse to $M$, it is an isomorphism, so the square formed by the two $p$ maps is Cartesian.

**Proof.** Away from $t=0$, $\Phi$ is the obvious identification of both spaces with $Y\times\mathbb R^\times$. At the central fibre it is the fibrewise injective normal differential, so it is injective everywhere. A proof of closedness must also prevent normal vectors from escaping to infinity while their images converge.

Fix $y_0\in N$. In adapted source and target coordinates write $f=(a,b)$ with $N=\{w=0\}$ and $M=\{u=0\}$. Locally there is a smooth matrix $A(w,z)$ such that

$$
a(w,z)=A(w,z)w,
\qquad A(0,z)=D_w a(0,z).
$$

The integral formula constructs $A$. Cleanliness makes $A(0,z_0)$ injective. After shrinking the chart it has a smooth left inverse $B(w,z)$; a bundle metric gives the explicit choice $B=(A^*A)^{-1}A^*$. In analytic charts, choosing an invertible minor instead gives an analytic left inverse.

Write a point of the target fibre product locally as $(y;v_X,z_X,t)$, so

$$
a(y)=t v_X,\qquad b(y)=z_X.
$$

If it comes from a noncentral point of the source deformation, its source normal coordinate is forced to be

$$
v_Y=\frac{w(y)}{t}=B(y)v_X.
$$

The right-hand side is defined even at $t=0$. On the image of the central fibre it recovers the source vector because $B(0,z)A(0,z)=1$. Together with the tangential coordinate $z(y)$ and $t$, it supplies a smooth inverse on the image, and a smooth left inverse from an ambient coordinate neighborhood. Thus $\Phi$ is an embedding locally near every central source point.

Now suppose a sequence in the image converges in the fibre product to $(y;v_X,z_X,0)$. Necessarily $f(y)\in M$, hence $y\in N$. Choose the preceding charts at $y$. The corresponding source vectors are $B(y_n)v_{X,n}$, including for central members of the sequence, so they converge. Their source tangential coordinates and parameters also converge. Continuity of $\Phi$ identifies the limit's image with the prescribed target limit. Therefore the image is sequentially closed. The fibre product is a subspace of a manifold and is first countable, so the image is closed. This proves the first assertion without a hidden properness assumption on $f$.

The left inverse provides the exact control needed in this limit argument: shrink to a relatively compact source coordinate neighborhood of the limiting base point. The operator norm of the matrix defining the left inverse is bounded there, so bounded target normal coordinates force bounded source normal coordinates. The displayed inverse formula then gives convergence, not merely a convergent subsequence. Thus cleanliness controls the normal directions even though the map on base manifolds need not be proper.

If $f$ is transverse, $A$ is square and invertible near $N$. Every central point of the fibre product is then in the image, and all noncentral points already were. The same local formula with $B=A^{-1}$ is a smooth or analytic inverse. This proves the Cartesian assertion. $\square$

As a consequence, if $f$ is clean and proper, $\widetilde f$ is proper: factor it as the closed embedding $\Phi$ followed by the base change of the proper map $f$. More generally, this implication can be applied on suitable closed support sets once the relevant normal-cone properness hypotheses are verified; those support hypotheses are part of the specialization unit and are not omitted here.

### SH02-NG-CLEAN-PAIRS — Clean pairs and zero completion

For maps $f_1:Y_1\to X$ and $f_2:Y_2\to X$, define cleanliness or transversality by applying the preceding definitions to $(f_1,f_2):Y_1\times Y_2\to X\times X$ and its diagonal. With $Q=Y_1\times_XY_2$, the clean condition says that $Q$ is a submanifold and

$$
T_{(y_1,y_2)}Q
=\ker\bigl(d f_1-d f_2:T_{y_1}Y_1\oplus T_{y_2}Y_2\to T_xX\bigr).
$$

The transverse condition says that this difference map is surjective. These descriptions follow from the normal identification $[(a,b)]\mapsto a-b$ for the diagonal, so they also record the sign convention.

If $f_2$ is the inclusion of an embedded submanifold $Y_2\subset X$, projection to $Y_1$ identifies $Q$ with $f_1^{-1}(Y_2)$. Quotienting the difference map by $TY_2$ gives $d f_1$ modulo $TY_2$. Its kernel equality, or its surjectivity, is precisely the corresponding condition for $f_1$ with respect to $Y_2$. Thus the pair definitions recover the earlier ones.

## SH02-NG-PARAMETER-ORIENTATION — The parameter determines a relative orientation

Local identifier: `SH02-NG-PARAMETER-ORIENTATION`

The map $p$ can be singular, but its relative determinant line still makes sense:

$$
\mathcal L_p=\det T^*\mathcal D_MX\otimes p^*(\det T^*X)^{-1}.
$$

It has rank one. With the convention that the base volume precedes the relative factor, the expression $t^{-r}dt$ on $t\ne0$ defines a nowhere-zero smooth section of $\mathcal L_p$ that extends uniquely across $t=0$.

To see this, in the deformation coordinates use the generator

$$
\eta_U=
(dv_1\wedge\cdots\wedge dv_r\wedge dz_1\wedge\cdots\wedge dz_{n-r}\wedge dt)
\otimes
(du_1\wedge\cdots\wedge du_r\wedge dz_1\wedge\cdots\wedge dz_{n-r})^{-1}.
$$

On $t\ne0$, wedging the pulled-back base volume with $dt/t^r$ gives the numerator, because all terms containing an extra $dt$ vanish and the remaining Jacobian factor is $t^r$. Hence $\eta_U$ is the desired extension. On overlap, both such generators equal the same intrinsic expression $dt/t^r$ on the dense noncentral set, so they agree everywhere. Each is nonzero at the central fibre as well.

Passing from a nonzero real determinant section to its orientation gives a canonical trivialization

$$
\operatorname{or}_{\mathcal D_MX}\otimes
p^{-1}\operatorname{or}_X^{-1}\simeq k_{\mathcal D_MX}.
$$

Thus the relative orientation of the whole deformation map is canonically trivial, even when $X$ and $M$ are not oriented. On $t>0$, this agrees with the orientation of increasing $t$, since $t^r>0$. On $t<0$, the factor $t^{-r}$ records the parity that an unqualified use of $dt$ would lose.

The sheaf-theoretic consequence requires the manifold duality formula for **arbitrary** smooth maps, including singular maps:

$$
p^!k_X\simeq
\operatorname{or}_{\mathcal D_MX}\otimes p^{-1}\operatorname{or}_X^{-1}
[\dim\mathcal D_MX-\dim X].
$$

With that explicit import the relative dualizing complex is $k_{\mathcal D_MX}[1]$. The import follows from $p^!\omega_X\simeq\omega_{\mathcal D_MX}$ and compatibility with tensoring by invertible local systems; a submersion-only formula would not suffice for $p$. The determinant proof above is independent of this sheaf-theoretic import.

For the sheaf comparison, the general manifold formula is recorded in [Schapira, *A short review on microlocal sheaf theory*, 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §2.2, pp. 6–7. Here is the reduction that transfers it to a possibly singular map. On a target chart trivializing its orientation local system, the target dualizing complex is the constant coefficient sheaf shifted by the target dimension. Composition of extraordinary inverse images carries this dualizing complex to the dualizing complex of the source. Commutation with shifts gives the required dimension difference. On the overlap of two such charts, changing the orientation generator multiplies it by the orientation transition sign. The extraordinary inverse image is linear over the coefficient ring, so it carries that transition to its pullback on the source. The local identifications therefore glue with the inverse target orientation twist in the displayed formula. The global determinant section fixes the remaining sign by the prescribed base-before-parameter convention. This reduction uses the declared duality and composition imports; it does not require the deformation projection to be a submersion.

## SH02-NG-CONE-DEFINITION — Limits of subsets and the sign of a pair cone

Local identifier: `SH02-NG-CONE-DEFINITION`

For an arbitrary subset $S\subset X$, define

$$
C_M(S)=E\cap\overline{p_+^{-1}(S)},
$$

where the closure is in $\mathcal D_MX$. This is the normal cone of $S$ along $M$. It is a closed positive-conic subset of $E$: positive scaling preserves the positive lift of $S$ and hence its closure. No closedness, local closedness, or regularity assumption on $S$ is used.

For two arbitrary subsets $S_1,S_2\subset X$, use the diagonal $\Delta\subset X\times X$ and set

$$
C(S_1,S_2)=C_\Delta(S_1\times S_2)\subset TX.
$$

The normal bundle of the diagonal is identified with $TX$ by

$$
[(a,b)]\longmapsto a-b.
$$

Equivalently, first use the representative $(a-b,0)$ and then project to the first tangent factor. The difference, rather than the sum or the opposite difference, fixes the sign convention throughout this unit.

### SH02-NG-CONE-SEQUENCES — Sequential tests for normal cones

**Sequence criterion.** In adapted coordinates $(u,z)$ at $m=(0,z_0)$, a vector $(m;v)$ belongs to $C_M(S)$ exactly when there are $x_n=(u_n,z_n)\in S$ and $c_n>0$ such that

$$
x_n\longrightarrow m,
\qquad c_nu_n\longrightarrow v.
$$

It is equivalent to require in addition that $c_n\to\infty$. In arbitrary local coordinates on $X$,

$$
(x;v)\in C(S_1,S_2)
$$

exactly when there are $x_n\in S_1$, $y_n\in S_2$, and $c_n>0$ with

$$
x_n\longrightarrow x,\qquad y_n\longrightarrow x,
\qquad c_n(x_n-y_n)\longrightarrow v.
$$

Again one may require $c_n\to\infty$.

**Proof.** A manifold is first countable, so membership in the defining closure is detected by a sequence $(v_n,z_n,t_n)$ with $t_n>0$ converging to $(v,z_0,0)$. Its image $x_n=(t_nv_n,z_n)$ lies in $S$, and $c_n=t_n^{-1}$ gives the criterion with $c_n\to\infty$.

Conversely, if $v\ne0$, convergence of $u_n$ to zero and of $c_nu_n$ to $v$ forces $c_n\to\infty$. Thus $(c_nu_n,z_n,c_n^{-1})$ is a convergent sequence in the positive lift. If $v=0$, it is enough to retain $x_n\to m$ and replace the scales by

$$
t_n=\sqrt{\lVert u_n\rVert}+1/n,
\qquad c'_n=t_n^{-1}.
$$

Then $t_n\to0$ and $\lVert u_n/t_n\rVert\le\sqrt{\lVert u_n\rVert}\to0$. This proves the equivalence, including bounded original scales. Apply it to the diagonal in the coordinates $(x-y,y)$ to obtain the pair criterion. Under a coordinate change $h$, the integral formula for $h(x_n)-h(y_n)$ shows that its scaled limit is $D h_x(v)$; hence the criterion has the asserted intrinsic meaning. $\square$

### SH02-NG-CONE-CONSEQUENCES — Consequences of normal-cone geometry

The sequence criterion gives the following useful identities:

$$
\tau(C_M(S))=M\cap\overline S,
\qquad C_M(S)=C_M(\overline S),
$$

$$
C_M(S\cup T)=C_M(S)\cup C_M(T),
\qquad C(S_2,S_1)=-C(S_1,S_2).
$$

For the first equality, one inclusion follows from continuity of $p$. In the other direction, take a sequence in $S$ converging to $m\in M$ and use the zero-vector construction in the proof above. Thus every point of $M\cap\overline S$ actually contributes its zero vector. For closure invariance, $p_+$ is open, so

$$
\overline{p_+^{-1}(S)}\cap\Omega
=p_+^{-1}(\overline S).
$$

Taking the closure in the whole deformation proves the identity. The finite-union formula follows because closure commutes with finite unions, and exchange of the pair factors negates the difference in the sequence criterion. The finite-union qualification matters: a countable union may have new limiting directions.

If $O\subset X$ is open, deformation charts identify $p^{-1}(O)$ with $\mathcal D_{M\cap O}O$. It follows that

$$
C_M(S)|_{M\cap O}=C_{M\cap O}(S\cap O).
$$

This is the precise locality that permits the locally closed version of the construction. For the quotient map $q:TX|_M\to N_MX$ one also has

$$
C(S,M)=q^{-1}C_M(S).
$$

Indeed, the normal component of a scaled difference from a point of $M$ gives one inclusion. For the reverse inclusion, represent $(m;a)$ in the normal cone by $x_n=(u_n,z_n)$ and $c_n\to\infty$. Given any tangential component $b$, put $y_n=(0,z_n-b/c_n)\in M$ for sufficiently large $n$. Then $c_n(x_n-y_n)\to(a,b)$. This also shows why the pair cone contains every tangential lift of an allowed normal vector.

The comparison with the sources preserves a useful difference in scope. The normal-cone definition in the 2016 review initially assumes a locally closed subset, whereas the pair-cone definition in Astérisque §1.2.1 is given for arbitrary subsets. The arguments here need only closure of the positive lift and sequential convergence in a manifold. Closure invariance and the zero-vector rescaling above therefore prove the asserted arbitrary-subset version directly. No stratification or regularity of the subset has been inserted.

## SH02-NG-CONE-AVOIDANCE — Neighborhoods seen from the positive side

Local identifier: `SH02-NG-CONE-AVOIDANCE`

Write $\mathcal D^{\ge0}_MX=E\cup\Omega$, with its subspace topology. Let $V\subset E$ be an open positive-conic subset.

**Neighborhood criterion.** If $W$ is an open neighborhood of $V$ in the deformation and $U=p_+(W\cap\Omega)$, then $U$ is open in $X$ and

$$
V\cap C_M(X\setminus U)=\varnothing.
$$

Conversely, for an open $U\subset X$ with this avoidance property,

$$
p_+^{-1}(U)\cup V
$$

is an open neighborhood of $V$ in $\mathcal D^{\ge0}_MX$.

**Proof.** The product projection $p_+$ is open. By definition, $W$ does not meet the positive lift of $X\setminus U$. Since $W$ is open, it also does not meet the closure of that lift at a point of $V\subset W$. This proves the first assertion.

For the converse, the positive lift of $X\setminus U$ is closed inside $\Omega$. Its closure inside $E\cup\Omega$ adds exactly $C_M(X\setminus U)$ at the central fibre. The set $E\setminus V$ is closed in $E\cup\Omega$, and by assumption it contains this added boundary. Therefore

$$
(E\setminus V)\cup p_+^{-1}(X\setminus U)
$$

is closed in $E\cup\Omega$. Its complement is the asserted neighborhood. $\square$

### SH02-NG-INTERVAL-NEIGHBORHOODS — Neighborhoods along positive rays

**Connected-fibre refinement.** Every open neighborhood $W$ of $V$ in $\mathcal D_MX$ contains an open neighborhood $W_0$ of $V$ such that each fibre of

$$
p_+:W_0\cap\Omega\longrightarrow X
$$

is either empty or an interval in its natural positive-parameter coordinate. In particular all its nonempty fibres are contractible.

**Proof.** Choose a smooth tubular neighborhood $T$ of $M$ and identify it with a disk neighborhood $D$ of the zero section in $E$, using a bundle metric. The normal differential of this identification is the identity. Its deformation identifies $p^{-1}(T)$ with

$$
Q=\{(m,v,t):tv\in D_m\},
\qquad p(m,v,t)=(m,tv).
$$

This can also be read directly in deformation charts; functoriality of the deformation justifies its compatibility on overlaps. Replace $W$ by $W\cap p^{-1}(T)$, which is still an open neighborhood of all of $V$. A fibre over $x\notin T$ will be empty. We now work entirely in $Q$.

Put

$$
A=\{m\in M:0_m\in V\}.
$$

This is open, and $E|_A\subset V$. Indeed, an open neighborhood of $0_m$ contains a ball in $E_m$; positive conicity dilates that ball to every vector in the fibre. The same argument near $0_m$ also shows directly that the relevant bases form an open set. This full-fibre observation is what makes the zero-vector case possible.

For $x=(m,w)\in D$, let

$$
I_x=\{a>0:(m,w/a,a)\in W\}.
$$

For $w\ne0$ write $r=\lVert w\rVert$. If $r\in I_x$, select the connected component $J_x$ of $I_x$ containing $r$; otherwise put $J_x=\varnothing$. The point at time $r$ is the radial anchor

$$
\sigma(x)=(m,w/\lVert w\rVert,\lVert w\rVert).
$$

For $w=0$ and $m\in A$, select instead the initial component of the positive axis:

$$
J_{(m,0)}=\{a>0:(m,0,b)\in W\text{ for every }0\le b\le a\}.
$$

Since $W$ is open and contains $(m,0,0)$, this is a nonempty open interval beginning at zero. If $w=0$ and $m\notin A$, select the empty set. Let

$$
W_+=\{(m,w/a,a):a\in J_{(m,w)}\},
\qquad
W_0=(W\cap\{t<0\})\cup V\cup W_+.
$$

Every selected positive fibre is an open interval or empty, and $V\subset W_0\subset W$. We prove that $W_0$ is open, with all four locations addressed explicitly.

First suppose $t>0$ and $w\ne0$. A selected point at time $t$ is joined to its anchor at time $r$ by the compact time segment between $t$ and $r$ inside $I_x$. The anchor depends continuously on $x$ near a nonzero $w$. Parametrize this segment linearly on $[0,1]$. Openness of $W$ and compactness of $[0,1]$ ensure that the whole segment remains in $W$ for nearby $x$ and nearby endpoint time. Thus $W_+$ is open at such a point.

Second consider $(m_0,0,t_0)\in W_+$ with $t_0>0$. There is a $t_1>t_0$ for which the whole axis segment $\{(m_0,0,a):0\le a\le t_1\}$ lies in $W$. The full closed unit disk in the central fibre over $m_0$ also lies in $V\subset W$. In a local bundle trivialization, compactness of these two sets and openness of $W$ give a neighborhood $B\subset A$ of $m_0$, numbers $0<\delta<t_0$ and $\varepsilon>0$, and the inclusions

$$
\{(m,v,a):m\in B,\ \lVert v\rVert\le1,\ 0\le a\le\delta\}\subset W,
$$

$$
\{(m,v,a):m\in B,\ \lVert v\rVert<\varepsilon,\ \delta\le a\le t_1\}\subset W.
$$

Shrinking the bounds ensures these sets lie in $Q$. For $m\in B$ and sufficiently small nonzero $w$, the path

$$
a\longmapsto(m,w/a,a),
\qquad \lVert w\rVert\le a\le t,
$$

joins the anchor to any point with $t$ near $t_0$ inside $W$. On $a\le\delta$, its normal norm is at most one, so the first inclusion applies. On $a\ge\delta$, choose $\lVert w\rVert<\delta\varepsilon$, so the second inclusion applies. We also choose $\lVert w\rVert<\delta$ and $t<t_1$. Nearby points with $w=0$ belong to their initial components by the same two inclusions. This proves openness at positive zero-axis points.

Third, let $(m_0,v_0,0)\in V$ with $v_0\ne0$. Near that point define, for $0\le s\le1$,

$$
d_s(v)=(1-s)+s\lVert v\rVert,
\qquad
H_s(m,v,t)=\bigl(m,v/d_s(v),t\,d_s(v)\bigr).
$$

It preserves $p(m,v,t)$ and joins a positive point to its radial anchor. At the given central point the path is a compact radial segment in $V$, since $V$ is conic. Compactness again gives a neighborhood of $(m_0,v_0,0)$ in which every $H_s$ lies in $W$. Every positive point of that neighborhood is therefore selected. Shrink the neighborhood so that its central slice lies in $V$ and the whole neighborhood lies in $W$; its negative part was included by definition. Thus it lies in $W_0$.

Finally let $(m_0,0,0)\in V$. By the full-fibre observation, the central closed unit disk over $m_0$ lies in $W$. Compactness gives $B\subset A$ and $\delta>0$ for which the first disk inclusion above holds. If $m\in B$, $\lVert v\rVert<1$, and $0<t<\delta$, the point $(m,v,t)$ has $w=tv$. When $v\ne0$, its anchor time is $r=t\lVert v\rVert$, and the time segment $[r,t]$ stays in that disk box. When $v=0$, it belongs to the initial axis component. Together with a sufficiently small central slice in $V$ and a negative slice in $W$, these points form an open neighborhood of $(m_0,0,0)$ contained in $W_0$.

These arguments prove openness everywhere. If the normal bundle has rank zero, the nonzero-ray cases are absent and the initial-axis construction alone proves the result. No assumption that $V$ avoids the zero section has entered the proof. $\square$

The refinement gives a cofinal supply of neighborhoods with connected **parameter fibres**, rather than just connected images in a space of rays. The interval selected at $w=0$ is necessary: a construction performed only on the complement of $M\times\mathbb R$ cannot by itself produce an open neighborhood of a zero normal vector.

## SH02-NG-EXAMPLES — Worked checks and exercises

Local identifier: `SH02-NG-EXAMPLES`

**An asymmetric limiting set.** In $X=\mathbb R^2$, deform along the horizontal axis $M=\{y=0\}$. Let

$$
S=\{(x,y):y=x^4,\ x\ne0\}.
$$

At the origin the normal cone is the nonnegative vertical half-line. Positivity follows because every scaled normal coordinate is $c_nx_n^4\ge0$. Given $a>0$, take any sequence $x_n\to0$, $x_n\ne0$, and set $c_n=a/x_n^4$; the resulting normal limit is $a$. The zero vector occurs by slower rescaling. At a nonzero point of the horizontal axis there is no cone fibre because that point is not in $\overline S$. This illustrates why the cone's base is $M\cap\overline S$, rather than an assumed constant base.

**A proper map whose deformation is not proper.** Let $f:\mathbb R\to\mathbb R$ be $f(y)=y^3$, and take $N=M=\{0\}$. The map $f$ is proper. In deformation coordinates,

$$
\widetilde f(v,t)=(t^2v^3,t).
$$

The inverse image of the single central point $(0,0)$ contains all $(v,0)$, so it is noncompact. The map is not clean: its normal differential at zero vanishes. Moreover the target fibre product contains central pairs $(0;u,0)$ for every $u$, whereas $\Phi$ hits only $u=0$. This tests both the properness warning and the failure of the ambient square to be Cartesian.

**A clean map that is not transverse.** Let $X=\mathbb R^3$, $M$ the $x$-axis, and let $Y$ be the $xy$-plane with its inclusion into $X$. The inverse image of $M$ is that axis. Its normal line in $Y$ maps injectively to the two-dimensional normal space of $M$ in $X$, so the inclusion is clean. It is not transverse because the image normal space misses the $z$ direction. The deformation embedding identifies a proper normal subbundle on the central fibre.

### SH02-NG-SOLVED-EXERCISES — Solved geometric checks

**Exercise A: extreme cones.** Determine $C_M(M)$ and $C_M(X)$, and determine $C(S_2,S_1)$ from $C(S_1,S_2)$.

**Solution.** The positive lift of $M$ has $v=0$ in every deformation chart, so its central closure is the zero section. Every central vector is the limit of $(v,z,t_n)$ with $t_n>0$, so $C_M(X)=E$. Exchanging the sequences in the pair criterion negates their scaled differences. Therefore $C(S_2,S_1)$ is the antipodal image of $C(S_1,S_2)$.

**Exercise B: clean intersections.** Suppose $S\subset X$ is a closed embedded submanifold clean with respect to $M$, and put $N=S\cap M$. Show that $C_M(S)$ is the image of $N_NS\to N_MX$.

**Solution.** Apply the clean deformation embedding theorem to $S\hookrightarrow X$. Since the inclusion is closed, the induced map of deformations is also closed: its factorization is a closed embedding followed by the base change of that closed inclusion. Its image contains the positive lift of $S$. Conversely every central source point is approached by positive source points, so the image of its central fibre lies in the closure of the positive lift. Any point in that closure lies in the closed image; if its parameter is zero, its preimage has parameter zero. The two inclusions give the result. The image is a vector subbundle over $N$, which explains the linearity in the clean case; arbitrary normal cones need not be linear or convex.

**Exercise C: the order of a pair matters.** At zero in $\mathbb R$, compute $C([0,\infty),\{0\})$ and $C(\{0\},[0,\infty))$.

**Solution.** In the first pair every difference is nonnegative, and every nonnegative vector is attained by choosing a positive point of size $v/c_n$ with $c_n\to\infty$. Thus the first cone is $[0,\infty)$ at the base zero; exchange gives $(-\infty,0]$. The zero vector belongs to both. This sign check is useful before translating any pair-cone statement into a conormal statement.

**Exercise D: orientation across the central fibre.** For $M=\{0\}\subset\mathbb R$, explain how $dt/t$ can extend as a relative determinant section although it does not extend as an ordinary one-form.

**Solution.** The deformation is $\mathbb R_v\times\mathbb R_t$ with $p(v,t)=tv$. The section is $(dv\wedge dt)\otimes(dx)^{-1}$ in the determinant ratio. On $t\ne0$, the equation $dp\wedge(dt/t)=dv\wedge dt$ identifies it with $dt/t$ along the fibres of $p$. The ratio section remains nonzero at $t=0$; there is no assertion that the ordinary differential form $dt/t$ extends on the total space. Replacing it by $dt$ in the ratio would introduce the vanishing factor $t$.

## SH02-NG-RESEARCH-ROUTES — Where this geometry is used

Local identifier: `SH02-NG-RESEARCH-ROUTES`

Specialization uses the positive chamber, central restriction, and the connected-fibre neighborhood refinement to turn sections near normal directions into sections on suitable open subsets of $X$. Its proper direct-image theorem also needs control of normal cones of supports; properness of $f$ alone fails, as the cubic example shows. Microlocalization then applies the Fourier–Sato transform to the normal bundle, so the signed difference convention and positive rather than signed conicity must remain consistent.

For further geometric work, compare a deformation retaining all of $E$ with a sphere or projective modification retaining only directions. The zero-vector neighborhood argument identifies exactly the information such a directional quotient omits. Another useful route is to study families of clean intersections and track the normal differential as its rank drops; the loss of injectivity gives an explicit place where deformation properness can fail.

The source comparison is mathematical as well as notational. Astérisque §2.2.1 supplies the coordinate gluing, scaling action, and normal-cone avoidance neighborhoods; its sheaf section formula is not used as a proof of the geometric neighborhood refinement. The four openness checks in `SH02-NG-INTERVAL-NEIGHBORHOODS` supply that refinement, including zero normal vectors. The punctured quotient and the clean-map left-inverse argument remain separate complete geometric arguments under the differential-topology prerequisites. The arbitrary-map duality formula remains a sheaf-theoretic import, explicitly separated from the determinant computation.

This independently authored exposition, including its proofs and exercises, is dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). The cited works retain their own terms; no source text or figures are incorporated. Differential-topology and sheaf-theoretic prerequisites still require their exact programme proof providers.
