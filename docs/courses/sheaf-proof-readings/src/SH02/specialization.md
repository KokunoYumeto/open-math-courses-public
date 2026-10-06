# Reading a sheaf at the normal scale

The proofs in this unit use the explicit
prerequisite contracts below; using a contract does not close its proof
obligation. Kashiwara and Schapira's *Microlocal Study of Sheaves*, §2.2,
provides the classical specialization construction and its functorial
comparisons. Its positive-chamber construction is the starting point for
the map and support calculations below. The source account at the end
identifies its mechanisms and the additional arguments written
out here. No constructibility or finite-generation assumption is made.

The route through the proofs starts with a normalization problem: which
boundary map fixes the shift? The neighborhood and support formulas then
show what normal data can detect. Ordinary restriction and the exceptional
costalk are checked separately, with their actual unit and counit, before
the punctured recovery is deduced. Agreement of the objects alone would not
identify the arrow in that recovery triangle.

Next follow the directions of the direct and inverse comparison maps before
asking when they are isomorphisms. The compactness proof separates escape
in the original manifold from escape in normal velocity; the orientation
calculation keeps the relative shifts visible. Finally, homogeneous sheaves
calibrate the construction, and two arcs that have the same tangent ray
show why tensor comparison need not be invertible. The four solved problems
test the zero-rank, endpoint, properness and orientation mechanisms.

## SH02-SP-CONVENTIONS — The object being constructed

Let $k$ be a commutative ring of finite global dimension. All manifolds are
finite-dimensional, Hausdorff and countable at infinity, and maps are
$C^\infty$; the real analytic setting is also allowed. In the comparison
theorems, a map called **smooth** means a submersion, not merely a
$C^\infty$ map. Let $i:M\hookrightarrow X$
be a closed embedded submanifold. A locally closed embedding is treated in
an open neighborhood in which it is closed; every construction below is
compatible with that restriction. Write

$$
E=T_MX,\quad \tau:E\longrightarrow M,\quad e:M\longrightarrow E,
\quad D=D_MX,\quad p:D\longrightarrow X,\quad t:D\longrightarrow\mathbb R.
$$

Here $D$ is the deformation to the normal bundle. Its central fibre is $E$,
embedded by $s:E\hookrightarrow D$. Its positive chamber is
$\Omega=\{t>0\}$, embedded by $j$, with
$r=p|_\Omega:\Omega\simeq X\times\mathbb R_{>0}\to X$. In coordinates
$x=(a,b)$ with $M=\{a=0\}$, the deformation coordinates are $(v,b,t)$
and $p(v,b,t)=(tv,b)$. The positive parameter is oriented by increasing $t$.
The scaling action is $(v,b,t)\mapsto(\lambda v,b,t/\lambda)$ for
$\lambda>0$; it fixes $p$ and restricts to ordinary dilation on $E$.

All input complexes belong to $D^b(k_X)$ or the corresponding bounded
category on another manifold. The notation does not mean perfect or
constructible. A shift satisfies $H^a(K[n])=H^{a+n}(K)$. Thus a module with
its only cohomology in degree one is written $L[-1]$. Tensor products are
derived unless a displayed factor is an invertible orientation complex.
The support of a complex means the closed support: the closure of the union
of the supports of its cohomology stalks.

The proof dependencies are as follows. The identifiers are contracts, not
claims of an already admitted proof.

| Contract | Exact input used here |
|---|---|
| SH02-NG-CONSTRUCTION | The deformation charts, their gluing, the maps $p,t,s,j,r$, and the scaling action |
| SH02-NG-CONE-SEQUENCES | The normal cone $C_M(S)=E\cap\overline{r^{-1}S}$; its sequence criterion, closedness, conicity, finite-union property and locality |
| SH02-NG-CONE-AVOIDANCE | For open $U\subset X$ and open conic $V\subset E$, avoidance $C_M(X\setminus U)\cap V=\varnothing$ is equivalent to $V\cup r^{-1}U$ being a neighborhood of $V$ in $D_{\ge0}=\{t\ge0\}$ |
| SH02-NG-INTERVAL-NEIGHBORHOODS | Such neighborhoods have a cofinal refinement whose positive projection onto its open image has nonempty interval fibres, including neighborhoods of zero vectors |
| SH02-NG-FUNCTORIALITY | Maps of pairs induce maps of deformations and normal bundles; the positive and central squares are Cartesian |
| SH02-CON-INTERVAL-FIBRES | If an open subset of $B\times\mathbb R$ projects onto $B$ with nonempty interval fibres, then $A\to R\pi_*\pi^{-1}A$ is an isomorphism for $A\in D^+(k_B)$ |
| SH02-CON-FUNCTORS | Conicity is preserved by the indicated equivariant inverse and direct image operations |
| SH02-CON-RADIAL-STAR, SH02-CON-RADIAL-SUPPORT | For a conic bounded-below complex on a vector bundle, $R\tau_*K\simeq e^{-1}K$ and $R\tau_!K\simeq e^!K$ |

### SH02-IMPORT-TAUTNESS — Tautness (SH-01 import contract)

Derived cohomology of a locally closed subspace of a metrizable manifold is the filtered colimit over its neighborhoods, in every degree; the same holds for restriction to a closed submanifold.

### SH02-OPS-SIX — Six-operation prerequisite contract

Exact inverse image, derived direct images, their units/counits, localization, $Rf_!\dashv f^!$, proper-support base change, projection formula, smooth base change, and trace-compatible pasting of these maps.

### SH02-OPS-BOUNDS — Boundedness prerequisite contract

The preceding operations on finite-dimensional manifolds have the finite cohomological amplitudes needed to carry bounded inputs to the bounded outputs displayed below.

### SH02-OPS-ORIENTATION — Orientation prerequisite contract

$\omega_{Y/X}=\operatorname{or}_Y\otimes f^{-1}\operatorname{or}_X^{-1}[\dim Y-\dim X]$, its trace, and the smooth formula $f^!A\simeq f^{-1}A\otimes\omega_{Y/X}$.

Tautness here includes a noncompact locally closed subset; replacing it by a
compact-set version would leave the section theorem below unproved. The
interval condition concerns fibres of the projection, not merely the image
of a scaling orbit. No nonproper closed-base-change assertion is used.

## SH02-SP-BOUNDARY — Fixing the boundary shift

Let $H=r^{-1}F$. The localization triangle for the open inclusion $j$,
applied to $j_!H$, is

$$
R\Gamma_{D\setminus\Omega}(j_!H)\longrightarrow j_!H
\longrightarrow Rj_*H\xrightarrow{+1}.
$$

The first term is supported on $E$: it vanishes on both $\Omega$ and
$\{t<0\}$. It is consequently $s_*s^!j_!H$. Restriction by $s^{-1}$
kills the middle term and gives a natural isomorphism

$$
s^{-1}Rj_*r^{-1}F\simeq s^!j_!r^{-1}F[1].
$$

The orientation of the positive parameter identifies
$r^!F\simeq r^{-1}F[1]$. We therefore obtain

$$
s^{-1}Rj_*r^{-1}F\simeq s^!j_!r^!F. \tag{SH02-SP-BOUNDARY-EQ}
$$

This isomorphism is the connecting isomorphism in the displayed triangle,
followed by the oriented smooth-pullback isomorphism. That specification fixes
the map and its sign; an unspecified equivalence of the two objects would
not suffice when traces are used later.

Define the specialization by

$$
\nu_MF=s^{-1}Rj_*r^{-1}F\in D^b(k_E).
\tag{SH02-SP-DEFINITION-EQ}
$$

The boundedness assertion follows from SH02-OPS-BOUNDS. The second expression
in SH02-SP-BOUNDARY-EQ is an alternative formula for this same functor,
with its stated natural identification.

## SH02-SP-CONIC — Directions and support

The complex $r^{-1}F$ is invariant under the scaling action on $\Omega$:
its pullback from $X$ is unchanged because $r$ is unchanged. The inclusions
$j$ and $s$ are equivariant. SH02-CON-FUNCTORS therefore gives

$$
\nu_MF\in D^b_{\mathbb R_{>0}}(k_E).
$$

Put $Z=\operatorname{supp}F$. Outside the closure of $r^{-1}Z$, the complex
$Rj_*r^{-1}F$ vanishes: each point has an open neighborhood whose intersection
with $\Omega$ misses that closed support. Restriction to $E$ gives

$$
\operatorname{supp}(\nu_MF)\subset C_M(Z).
\tag{SH02-SP-SUPPORT-BOUND}
$$

This argument proves containment. It does not assert equality; derived
sections in a direction can vanish even when the geometric support approaches
that direction.

## SH02-SP-SECTIONS — A neighborhood test in the original manifold

For an open conic subset $V\subset E$, let $\mathcal U(V)$ consist of open
subsets $U\subset X$ satisfying

$$
C_M(X\setminus U)\cap V=\varnothing.
$$

The transition map for $U'\subset U$ is restriction from $U$ to $U'$.
The family is filtered in that direction: $U\cap U'$ is again admissible,
because normal cones commute with finite unions. For every integer $a$,

$$
H^a(V;\nu_MF)\simeq
\underset{U\in\mathcal U(V)}{\operatorname{colim}}H^a(U;F).
\tag{SH02-SP-SECTIONS-EQ}
$$

We first specify the map. Pull a section complex on $U$ back to $r^{-1}U$.
Cone avoidance says that $V\cup r^{-1}U$ is a neighborhood of $V$ in
$D_{\ge0}$. Extend that neighborhood to an open subset of $D$ and restrict
$Rj_*r^{-1}F$ to $V$. The resulting map
$R\Gamma(U;F)\to R\Gamma(V;\nu_MF)$ is independent of the extension:
two choices agree after their common refinement. These maps respect
restriction in $U$.

For the proof, tautness and the definition of $Rj_*$ give

$$
H^a(V;\nu_MF)
\simeq\underset{W\supset V}{\operatorname{colim}}
H^a(W\cap\Omega;r^{-1}F),
$$

where $W$ runs through open neighborhoods in $D$. The interval-neighborhood
contract permits a cofinal choice for which
$r:W\cap\Omega\to U_W=r(W\cap\Omega)$ has nonempty interval fibres.
The positive chamber is the product $X\times\mathbb R_{>0}$, so the interval
descent theorem identifies the last group with $H^a(U_W;F)$.

The images $U_W$ are admissible. Indeed, a smaller open neighborhood of $V$
contained in $W$ has its positive part in $r^{-1}U_W$, so cone avoidance
applies. Conversely, given $U\in\mathcal U(V)$, apply the same cofinal
refinement inside a neighborhood whose positive part is contained in
$r^{-1}U$. Its image $U_W$ lies in $U$. Thus these images are cofinal in
$\mathcal U(V)$, and their descent identifications give precisely the
previously specified map. This proves the formula in every degree.

For a vector $v\in E$, this becomes the stalk formula

$$
H^a(\nu_MF)_v\simeq
\underset{v\notin C_M(X\setminus U)}{\operatorname{colim}}H^a(U;F).
\tag{SH02-SP-STALK-EQ}
$$

To justify using conic neighborhoods for this stalk, first take a small
product chart in the quotient of $E\setminus M$ by positive dilation. Its
inverse image is a conic neighborhood with a radial interval factor; conic
descent computes the stalk by these charts. At the zero section, intersect
with fibrewise balls and use radial contraction before taking the base
neighborhood colimit. Finally, if $v$ is outside a closed conic set, the
complement itself is an open conic neighborhood of $v$. These observations
identify the two filtered systems and prove the displayed formula, including
zero vectors.

## SH02-SP-SUPPORTS — Keeping track of closed supports

Let $A\subset E$ be closed and conic. Consider pairs $(U,Z)$ with $U$ an
open neighborhood of $M$ in $X$, $Z$ closed in $X$, and $C_M(Z)\subset A$.
Restriction to a smaller $U$ and enlargement to a larger $Z$ give the
transition maps. Intersecting the neighborhoods and taking the union of two
supports shows that this system is filtered. There are natural isomorphisms

$$
H_A^a(E;\nu_MF)\simeq
\underset{(U,Z)}{\operatorname{colim}}H^a_{Z\cap U}(U;F).
\tag{SH02-SP-SUPPORTS-EQ}
$$

Here is the map and the proof. A supported section on $U$ pulls back to a
section supported on $r^{-1}(Z\cap U)$. Its closure in $p^{-1}U\cap D_{\ge0}$
meets $E$ only in $C_M(Z)\subset A$. Restriction to the central fibre
therefore gives a section with support in $A$. The localization triangles
for $Z\cap U\subset U$ and $A\subset E$ give a morphism of long exact
cohomology sequences after taking this filtered colimit.

Two of its three terms are already known. For the term without supports,
an open set has $C_M(X\setminus U)=\varnothing$ exactly when it contains
$M$. Formula SH02-SP-SECTIONS-EQ with $V=E$ applies. For the complement term,
the sets $U\setminus Z$ lie in $\mathcal U(E\setminus A)$ because

$$
C_M\bigl(X\setminus(U\setminus Z)\bigr)
\subset C_M(X\setminus U)\cup C_M(Z)\subset A.
$$

They give the full admissible system: any admissible open $W$ is represented
by $U=X$ and $Z=X\setminus W$. Common refinements preserve that representation
at the level of the colimit. Hence the complement maps are isomorphisms by
the section theorem as well. Exactness of filtered colimits of $k$-modules
and the five lemma give the supported isomorphism. This proof also establishes
compatibility with the maps in the localization triangles.

## SH02-SP-ZERO — What survives when the direction is forgotten

There are canonical identifications

$$
e^{-1}\nu_MF\simeq R\tau_*\nu_MF\simeq i^{-1}F,
\qquad
e^!\nu_MF\simeq R\tau_!\nu_MF\simeq i^!F.
\tag{SH02-SP-ZERO-EQ}
$$

We describe the maps rather than choosing isomorphisms after the fact. The
unit $p^{-1}F\to Rj_*j^{-1}p^{-1}F$, restricted to $s\circ e$, gives
$i^{-1}F\to e^{-1}\nu_MF$. For the second identification, the boundary
formula and the counit $j_!j^!p^!F\to p^!F$ give

$$
e^!\nu_MF\simeq e^!s^!j_!r^!F
\longrightarrow e^!s^!p^!F\simeq i^!F.
$$

To prove the first map invertible, work over each open subset of $M$ and
use the section formula with the entire normal bundle over that subset.
Its admissible sets are just neighborhoods of that part of $M$; tautness
identifies the colimit with the cohomology of $i^{-1}F$. The conic ordinary
contraction identifies the other side with $e^{-1}\nu_MF$. The described
unit induces exactly these restriction maps, so it is the isomorphism
just computed.

For the second map, apply the support formula with $A=e(M)$. We need a
small geometric fact. If $Z$ is closed and $C_M(Z)$ is contained in the zero
section, then there is a neighborhood $U_0$ of $M$ such that
$Z\cap U_0\subset M$. Otherwise some $m\in M$ is approached by points of
$Z\setminus M$. In a normal chart write them as $(a_n,b_n)$ with $a_n\ne0$,
divide the normal coordinate by $\lVert a_n\rVert$, and pass to a subsequence
of the unit sphere. The sequence criterion puts a nonzero normal vector in
$C_M(Z)$, a contradiction. Taking the union of the resulting neighborhoods
over $m$ gives $U_0$. Thus the supported colimit reduces to
$H^a_M(U;F)$ over neighborhoods of $M$, which is the cohomology of $i^!F$.
Localizing on $M$ gives the corresponding isomorphism of cohomology sheaves.
It remains to check the particular counit map displayed above, rather than
an unspecified object-level isomorphism.

Set $F_M=i_*i^!F$ and use the support counit $F_M\to F$. The support formula
shows that $e^!\nu_MF_M\to e^!\nu_MF$ is an isomorphism: in its colimit,
$R\Gamma_M(U;F_M)\to R\Gamma_M(U;F)$ is an isomorphism by idempotence of
sections with support. Naturality therefore reduces the required counit
calculation to $F=i_*L$, for $L\in D^b(k_M)$.

Let $h:M\times\mathbb R\hookrightarrow D$ be the zero-normal-coordinate
axis in the deformation, and let $z:M\hookrightarrow M\times\mathbb R$
be time zero. The positive pullback of $i_*L$ is supported on this axis.
The oriented product formula and proper base change for its closed
embedding identify

$$
j_!r^!i_*L\simeq h_*(L\boxtimes k_{(0,\infty)}[1]),
\qquad
\nu_Mi_*L\simeq e_*z^!(L\boxtimes k_{(0,\infty)}[1])\simeq e_*L.
$$

To identify the map, put $\pi:M\times\mathbb R\to M$. Composition of
exceptional inverse images gives

$$
h^!p^!i_*L\simeq(p\circ h)^!i_*L
\simeq\pi^!i^!i_*L\simeq\pi^!L.
$$

Under $h_*\dashv h^!$, the counit from
$h_*(L\boxtimes k_{(0,\infty)}[1])$ to $p^!i_*L$ therefore becomes
the open-extension counit on the axis with target $\pi^!L$. There is no
claim that $p^!i_*L$ itself is supported on that axis. Applying $z^!$
shows that the counit $e^!\nu_Mi_*L\to i^!i_*L=L$ is the oriented
endpoint boundary map tensored with $L$. The endpoint costalk
of $k_{(0,\infty)}$ is $k[-1]$, its projection orientation contributes
$[1]$, and the connecting map used in SH02-SP-BOUNDARY-EQ identifies their
composite with the identity of $k$. This follows also by writing the
localization triangle for the half-line: the restriction map from the
constant sheaf on the closed half-line to its endpoint is the identity on
sections. Hence the counit is the identity of $L$. The naturality square
for $F_M\to F$, whose other vertical arrows are isomorphisms, proves that
the original counit is an isomorphism. Proper-support contraction supplies
$R\tau_!\nu_MF\simeq e^!\nu_MF$.

Let $a:X\setminus M\hookrightarrow X$, $b:E\setminus M\hookrightarrow E$,
and $\tau^\circ=\tau|_{E\setminus M}$. The two zero-section identifications
fit into the localization triangles and imply

$$
R\tau^\circ_*b^{-1}\nu_MF\simeq i^{-1}Ra_*a^{-1}F.
\tag{SH02-SP-PUNCTURE-EQ}
$$

Indeed, compare the triangles

$$
i^!F\longrightarrow i^{-1}F\longrightarrow i^{-1}Ra_*a^{-1}F\xrightarrow{+1}
$$

and

$$
e^!\nu_MF\longrightarrow R\tau_*\nu_MF
\longrightarrow R\tau^\circ_*b^{-1}\nu_MF\xrightarrow{+1}.
$$

Here is the first-arrow compatibility with the specified maps. Specialize
the support counit $i_*i^!F\to F$ and use
$\nu_Mi_*i^!F\simeq e_*i^!F$. Its adjoint is a map
$\sigma:i^!F\to e^!\nu_MF$. Naturality of the exceptional counit and its
endpoint identity give $c_F\sigma=\operatorname{id}$, where
$c_F:e^!\nu_MF\to i^!F$ is the isomorphism just proved. Thus
$\sigma=c_F^{-1}$. Naturality of the ordinary restriction unit, applied to
the same support counit, identifies the maps from supported to ordinary
restriction. The first two vertical maps are therefore compatible
isomorphisms, so the induced map of the third
terms is an isomorphism. This statement retains the whole punctured normal
bundle, rather than choosing a sphere or a metric.

## SH02-SP-DIRECT — Sending normal data through a map

Consider a map of pairs $f:(Y,N)\to(X,M)$, where $N$ and $M$ are closed
embedded submanifolds and $f(N)\subset M$. Write $E_Y=T_NY$, $E_X=T_MX$,
$q=T_Nf:E_Y\to E_X$, and $g:D_NY\to D_MX$ for the induced maps.
Decorate $s,j,r,p,t$ by $X$ or $Y$ when necessary, and put
$g_+=g|_{\Omega_Y}=f\times\operatorname{id}_{\mathbb R_{>0}}$.
The central and positive squares are Cartesian. No assertion is made that
the square involving $p_Y,p_X,f,g$ is Cartesian at time zero.

For $G\in D^b(k_Y)$ there is a commuting square, with both vertical arrows
forgetting proper supports:

$$
\begin{array}{ccc}
Rq_!\nu_NG&\xrightarrow{c_!}&\nu_M Rf_!G\\
\downarrow&&\downarrow\\
Rq_*\nu_NG&\xleftarrow{c_*}&\nu_M Rf_*G.
\end{array}
\tag{SH02-SP-DIRECT-SQUARE}
$$

Here are definitions that determine all four maps. Set $K=Rj_{Y*}r_Y^{-1}G$.
Proper-support base change at the central fibre gives
$Rq_!s_Y^{-1}K\simeq s_X^{-1}Rg_!K$. The comparison

$$
Rg_!Rj_{Y*}A\longrightarrow Rj_{X*}Rg_{+!}A
$$

is the adjoint, under $j_X^{-1}\dashv Rj_{X*}$, of proper-support base
change followed by the restriction counit
$j_Y^{-1}Rj_{Y*}A\to A$. Apply it with $A=r_Y^{-1}G$. Base change in
the positive product square gives
$Rg_{+!}r_Y^{-1}G\simeq r_X^{-1}Rf_!G$. Restriction by $s_X^{-1}$
defines $c_!$.

For the other arrow, smooth base change along the projection $r_X$ gives

$$
\nu_M Rf_*G\simeq s_X^{-1}Rg_*Rj_{Y*}r_Y^{-1}G.
$$

Compose this with the ordinary base-change map
$s_X^{-1}Rg_*K\to Rq_*s_Y^{-1}K$ to define $c_*$. This last map is
a comparison, not an assumed isomorphism.

For completeness, the square's commutativity is a statement about these
maps. In the first construction, replace $Rg_!$ and $Rg_{+!}$ by their
maps to ordinary direct image; naturality of restriction identifies the
result with the composition map for $Rg_*Rj_{Y*}$. Then restrict to the
central fibre and apply the ordinary base-change map. The result is the
map $Rq_!s_Y^{-1}K\to Rq_*s_Y^{-1}K$: the intermediate unit and counit
cancel by their triangle identity. This verifies that going across the top,
down, and back along the bottom equals the left vertical arrow. It also
shows why the arrow on the bottom points in the opposite direction.

## SH02-SP-PROPER-GEOMETRY — The extra compactness condition

Let $Z\subset Y$ be closed. Suppose that

1. $f|_Z:Z\to X$ is proper;
2. $q|_{C_NZ}:C_NZ\to E_X$ is proper;
3. $Z\cap f^{-1}(M)\subset N$.

The conditions rule out three different failures. Properness on the
original support keeps the underlying points from escaping. The
support-intersection condition places a limit over the target submanifold
on the chosen source submanifold. Properness on the normal cone then keeps
rescaled normal vectors from escaping while their images converge. Each
condition is used separately in the proof, so ordinary properness alone
cannot replace this list.

Then the closed subset

$$
D_Z=\overline{r_Y^{-1}Z}\subset D_NY
$$

is proper over $D_MX$ under $g$. Its central fibre is $C_NZ$ and it has
no negative-time points.

We prove compactness over a compact set $K\subset D_MX$. These spaces are
metrizable, so it suffices to take a sequence $u_n\in D_Z\cap g^{-1}K$
and find a convergent subsequence. Pass first to a subsequence for which
$g(u_n)$ converges to $v$.

If infinitely many $u_n$ have time zero, properness in condition 2 gives
the required subsequence. We may otherwise assume $t_n=t(u_n)>0$.
The points $y_n=p_Y(u_n)$ belong to $Z$, and
$f(y_n)=p_Xg(u_n)$ stays in a compact subset of $X$. Condition 1 permits
passing to $y_n\to y\in Z$. If $t(v)>0$, the positive product chart gives
$u_n\to(y,t(v))$, as required.

It remains to consider $t_n\to0$. Now $f(y)\in M$, so condition 3 is
needed to conclude $y\in N$. Choose coordinates $y_n=(a_n,b_n)$ with
$N=\{a=0\}$ and $y=(0,b)$. Then

$$
u_n=(w_n,b_n,t_n),\qquad w_n=a_n/t_n.
$$

Write the normal component of $f$ in compatible target coordinates as
$F(a,b)$, with $F(0,b)=0$. Convergence of $g(u_n)$ says that
$F(a_n,b_n)/t_n$ is bounded. Suppose that $w_n$ is unbounded; pass to a
subsequence with $\lVert w_n\rVert\to\infty$ and
$w_n/\lVert w_n\rVert\to w$, where $\lVert w\rVert=1$. Define

$$
\sigma_n=t_n\lVert w_n\rVert=\lVert a_n\rVert\longrightarrow0.
$$

The points $(w_n/\lVert w_n\rVert,b_n,\sigma_n)$ are positive lifts of
the same $y_n\in Z$. Their limit $(w,b,0)$ belongs to $C_NZ$.
Their target normal coordinates are

$$
\frac{F(a_n,b_n)}{\sigma_n}
=\frac{F(a_n,b_n)/t_n}{\lVert w_n\rVert}\longrightarrow0.
$$

Thus $q(w,b)$ is the zero vector over $f(y)$. Since $C_NZ$ is closed and
conic, its entire closed ray through $(w,b)$ lies in that single fibre of
$q$. A nonzero closed ray is not compact, contradicting condition 2.
Therefore $(w_n)$ is bounded. A final subsequence converges in the
deformation chart to a point of the closed set $D_Z$. This proves the
properness assertion in all cases.

## SH02-SP-PROPER — When both direct comparisons are isomorphisms

Apply the preceding lemma to $Z=\operatorname{supp}G$. Under its three
hypotheses, every arrow in SH02-SP-DIRECT-SQUARE is an isomorphism.

Indeed, $K=Rj_{Y*}r_Y^{-1}G$ is supported on $D_Z$, so $Rg_!K\to Rg_*K$
is an isomorphism. Proper base change on this closed support makes the
central ordinary base-change map an isomorphism. On the positive chamber,
$g_+$ is proper on the support of $r_Y^{-1}G$ by condition 1, so its
proper and ordinary direct images agree as well. The comparison used in
$c_!$ is now the usual composition isomorphism of ordinary direct images.
Finally, $\operatorname{supp}\nu_NG\subset C_NZ$, so condition 2 makes
$Rq_!\nu_NG\to Rq_*\nu_NG$ an isomorphism. These observations prove the
claim for the specified maps, not merely for the resulting objects.

A useful sufficient condition is that $N=f^{-1}M$, that $f$ is clean with
respect to $M$, and that $f$ is proper on $\operatorname{supp}G$. Clean
means that the induced linear map on each normal fibre is injective.
Condition 3 is then automatic. To verify condition 2, let $K\subset E_X$
be compact. The base points of $q^{-1}K\cap C_NZ$ lie in the compact set

$$
L=Z\cap N\cap f^{-1}(\tau_XK).
$$

Choose bundle metrics. Fibrewise injectivity of $q$, over the compact set
$L$, gives a uniform lower bound $\lVert q_yv\rVert\ge c\lVert v\rVert$
with $c>0$: take the positive minimum over the unit sphere bundle above
$L$. Thus $q^{-1}K\cap C_NZ$ is a closed subset of a bounded disk bundle
over a compact base and is compact. The three hypotheses now apply.

The use of metrics in this last proof is only a compactness test. The
comparison maps and their isomorphism statement contain no metric choice.

## SH02-SP-ORIENTATIONS — The determinant calculation

For a map $h:P\to Q$ of manifolds, write

$$
\omega_h=\operatorname{or}_P\otimes h^{-1}\operatorname{or}_Q^{-1}
[\dim P-\dim Q].
$$

It is an invertible complex, whether or not $h$ is smooth. We write its
tensor inverse as $\omega_h^{\otimes-1}$; this is not Verdier duality of an
arbitrary sheaf. The comparison

$$
\theta_h(A):\omega_h\otimes h^{-1}A\longrightarrow h^!A
\tag{SH02-SP-THETA-EQ}
$$

is adjoint to the projection formula followed by the relative trace
$Rh_!\omega_h\to k_Q$. This fixes its direction and normalization.

For the normal bundle projection followed by the inclusion
$p_E=i\tau:E\to X$, the exact normal sequence gives a canonical
orientation identification

$$
p_E^!k_X\simeq k_E=p_E^{-1}k_X.
\tag{SH02-SP-NORMAL-ORIENTATION}
$$

Indeed, along the zero section the tangent orientation of $E$ is the product
of the orientation of $M$ and that of its normal bundle. The same product
is the orientation of $X|_M$, by the exact sequence
$0\to TM\to TX|_M\to E\to0$. Also $\dim E=\dim X$, so the degree
shift cancels. A choice of splitting proves the identification; the space
of splittings is affine, so the identification does not depend on it. Fibre
contraction extends the orientation identification over $E$.

Applying this calculation on $Y$ and $X$ gives

$$
\omega_q\simeq\tau_Y^{-1}(\omega_f|_N).
\tag{SH02-SP-ORIENTATION-Q}
$$

The restriction symbol includes the map $N\to Y$. To record both factors,
let $h=f|_N:N\to M$ and factor the normal map as

$$
E_Y\xrightarrow{u}N\times_M E_X\xrightarrow{v}E_X.
$$

With pullbacks to the displayed source understood explicitly, one has

$$
\omega_u\simeq\tau_Y^{-1}
\bigl((\omega_f|_N)\otimes\omega_h^{\otimes-1}\bigr).
\tag{SH02-SP-ORIENTATION-LINEAR}
$$

For the fibrewise transpose $u^t:N\times_M E_X^*\to E_Y^*$,

$$
\omega_{u^t}\simeq\pi^{-1}
\bigl(\omega_h\otimes(\omega_f|_N)^{\otimes-1}\bigr),
\tag{SH02-SP-ORIENTATION-TRANSPOSE}
$$

where $\pi:N\times_M E_X^*\to N$. To check the shifts, set
$r_Y=\dim Y-\dim N$ and $r_X=\dim X-\dim M$. The first linear map
has relative shift $r_Y-r_X$ and the transpose has $r_X-r_Y$. Their
orientation lines are inverse to one another because a real vector space
and its dual have canonically identified orientation lines. This proves
both formulas with their stated inverses. All reordering of shifted
factors uses the Koszul symmetry; the normal exact sequence is ordered
with tangent-to-base before normal directions.

## SH02-SP-TWISTS — Moving a locally constant factor through the limit

If $L$ is a locally constant invertible complex on $Y$, there is a natural
isomorphism

$$
\nu_N(L\otimes G)\simeq
\tau_Y^{-1}(L|_N)\otimes\nu_NG.
\tag{SH02-SP-TWIST-EQ}
$$

Pull $L$ to the deformation by $p_Y$. Tensoring by this invertible locally
constant complex commutes with $Rj_{Y*}$: tensoring with it and with its
inverse are mutually inverse equivalences. Move the inverse tensor factor
across a derived Hom, use $j_Y^{-1}\dashv Rj_{Y*}$, and move the factor
back on $\Omega_Y$. Yoneda then gives the required projection isomorphism.
This argument does not assert that an arbitrary invertible $k$-module is
free. Restriction to
$E_Y$ gives $s_Y^{-1}p_Y^{-1}L=\tau_Y^{-1}(L|_N)$ and proves the formula.
The same argument allows a locally constant finite projective coefficient
factor. Mere flatness does not assert commutation with an arbitrary
ordinary direct image.

## SH02-SP-INVERSE — Pullback and exceptional pullback

An invertible relative orientation complex does not by itself identify
exceptional inverse image with twisted ordinary inverse image. The
comparison map is available for a general map of manifolds; smoothness
makes the general isomorphism theorem used here applicable. Keep this
distinction between a determinant identification and an isomorphism theorem
when reading the next square.

For $F\in D^b(k_X)$ there are natural comparison maps

$$
\alpha:q^{-1}\nu_MF\longrightarrow\nu_N f^{-1}F,
\qquad
\beta:\nu_N f^!F\longrightarrow q^!\nu_MF.
\tag{SH02-SP-INVERSE-MAPS}
$$

They form the commuting orientation square

$$
\begin{array}{ccc}
\omega_q\otimes q^{-1}\nu_MF
&\xrightarrow{\ \omega_q\otimes\alpha\ }&
\nu_N(\omega_f\otimes f^{-1}F)\\
\theta_q\downarrow&&\downarrow\nu_N(\theta_f)\\
q^!\nu_MF&\xleftarrow{\ \beta\ }&\nu_N f^!F.
\end{array}
\tag{SH02-SP-INVERSE-SQUARE}
$$

The top arrow incorporates SH02-SP-ORIENTATION-Q and SH02-SP-TWIST-EQ.
Thus its right-hand orientation factor lives on $Y$, and its left-hand
factor lives on $E_Y$; the notation does not confuse these spaces.

We first construct $\alpha$. Write $A=r_X^{-1}F$. The ordinary base-change
map for the positive square gives

$$
q^{-1}s_X^{-1}Rj_{X*}A
\simeq s_Y^{-1}g^{-1}Rj_{X*}A
\longrightarrow s_Y^{-1}Rj_{Y*}g_+^{-1}A
\simeq\nu_N f^{-1}F.
$$

To construct $\beta$, orient both positive projections by the same increasing
parameter. Smooth pullback and composition give

$$
r_Y^{-1}f^!F\simeq g_+^!r_X^{-1}F.
$$

Explicitly, $r_Y^{-1}f^!F\simeq r_Y^!f^!F[-1]
\simeq g_+^!r_X^!F[-1]\simeq g_+^!r_X^{-1}F$; the two parameter shifts
cancel in the displayed order. Proper-support base change for the positive
square, by taking right adjoints, gives

$$
Rj_{Y*}g_+^!A\simeq g^!Rj_{X*}A.
$$

Finally, the central square has the exceptional base-change comparison

$$
s_Y^{-1}g^!B\longrightarrow q^!s_X^{-1}B.
$$

Its adjoint is
$Rq_!s_Y^{-1}g^!B\simeq s_X^{-1}Rg_!g^!B\to s_X^{-1}B$,
using the counit of $Rg_!\dashv g^!$. Composing these three maps with
$B=Rj_{X*}A$ defines $\beta$.

Here is a check of the square at the level of maps. On the deformation,
the orientation line $\omega_g$ restricts on the positive chamber to
$r_Y^{-1}\omega_f$ and on the central fibre to $\omega_q$. The determinant
identifications agree with SH02-SP-ORIENTATION-Q: both cancel the same
positively oriented parameter factor. Tensor the ordinary positive
base-change map by $\omega_g$, then apply the trace comparisons for $g_+$
and $g$. These two routes agree. To verify this equality, take the adjoint
under $Rg_!\dashv g^!$, and then under $j_X^{-1}\dashv Rj_{X*}$.
Both routes become the projection formula followed by the trace of $g_+$
on $\Omega_X$; the inserted restriction unit and counit cancel.

Now restrict that equality to $E_Y$. Composing with exceptional central
base change sends $s_Y^{-1}\theta_g$ to $\theta_q$. Taking its adjoint
under $Rq_!\dashv q^!$ checks this assertion: proper-support base change
identifies the adjoint with the restriction of the trace of $g$, which
is the trace of $q$. This is exactly the trace-compatible base-change
identity in SH02-OPS-SIX. Together with the twist identification, the
equality is SH02-SP-INVERSE-SQUARE. The proof uses one fixed trace and the
units/counits, so it introduces neither an arbitrary scalar nor an
unrecorded orientation sign.

All four maps in SH02-SP-INVERSE-SQUARE are isomorphisms on the open subset
of $E_Y$ where $q$ is smooth, meaning a submersion. To see the relevant
geometry, at a central point the deformation derivative is block triangular:
on the tangent space of $E_Y$ it is $dq$, and on the final time coordinate
it is the identity. Surjectivity of $dq$ makes $g$ a submersion near that
point. Smooth base change therefore makes $\alpha$ and the exceptional
central comparison defining $\beta$ isomorphisms there; all other arrows
used to construct $\beta$ are already isomorphisms. The comparison
$\theta_q$ is an isomorphism on this locus. The commuting square now also
makes its right vertical arrow an isomorphism on the same locus, regardless
of its behavior elsewhere.

In particular, if both $f:Y\to X$ and $h:N\to M$ are smooth, then $q$ is
smooth everywhere. Indeed, surjectivity of $df$ implies surjectivity on
the normal quotients, and the base map $h$ is a submersion. In bundle
coordinates these two statements give surjectivity of the derivative of
$q$. Thus all comparisons in the square are isomorphisms globally under
these two hypotheses.

## SH02-SP-ADJUNCTION — The direct and inverse maps are mates

The previous constructions obey two identities useful when another functor
is applied to the normal bundle. The map $\beta_F$ is exactly

$$
\nu_N f^!F\longrightarrow q^!Rq_!\nu_Nf^!F
\xrightarrow{q^!c_!}q^!\nu_M Rf_!f^!F
\longrightarrow q^!\nu_MF,
\tag{SH02-SP-SHRIEK-MATE}
$$

where the first arrow is the unit for $Rq_!\dashv q^!$ and the last uses
the counit for $Rf_!\dashv f^!$. Likewise, $\alpha_F$ is exactly

$$
q^{-1}\nu_MF\longrightarrow q^{-1}\nu_M Rf_*f^{-1}F
\xrightarrow{q^{-1}c_*}q^{-1}Rq_*\nu_Nf^{-1}F
\longrightarrow\nu_Nf^{-1}F,
\tag{SH02-SP-STAR-MATE}
$$

using the unit for $f^{-1}\dashv Rf_*$ and the counit for
$q^{-1}\dashv Rq_*$. To prove these identities, substitute the definitions
of $c_!$ and $c_*$ from SH02-SP-DIRECT. Move their positive-square
base-change maps across the displayed adjunctions. In the proper-support
case this gives $Rj_{Y*}g_+^!\simeq g^!Rj_{X*}$; in the ordinary case
it gives $g^{-1}Rj_{X*}\to Rj_{Y*}g_+^{-1}$. Moving the central-square
map gives respectively $s_Y^{-1}g^!\to q^!s_X^{-1}$ and
$q^{-1}s_X^{-1}=s_Y^{-1}g^{-1}$. The product-projection comparison moves
to the positive-parameter identification used in defining $\beta$, and
to the evident inverse-image identification used in defining $\alpha$.
All remaining inserted units and counits cancel by their triangle
identities. The resulting composites are precisely the definitions in
SH02-SP-INVERSE, which proves the two formulas with their fixed maps.

## SH02-SP-EXTERNAL — Synchronizing the deformation parameter

Let $M\subset X$ and $N\subset Y$ be closed embedded submanifolds, and
let $F\in D^b(k_X)$ and $G\in D^b(k_Y)$. There is a natural morphism

$$
\nu_MF\boxtimes^L\nu_NG\longrightarrow
\nu_{M\times N}(F\boxtimes^L G)
\quad\hbox{on }T_MX\times T_NY.
\tag{SH02-SP-EXTERNAL-EQ}
$$

The reason for a comparison rather than an equality in its definition is
that the product of two deformations has two time coordinates, while the
deformation of the product has one. In charts there is a closed embedding

$$
d:D_{M\times N}(X\times Y)\hookrightarrow D_MX\times D_NY,
\qquad (v,w,t)\longmapsto((v,t),(w,t)).
$$

It is the equal-time locus. Its central map is the identity under the
canonical normal-bundle identification. Its positive restriction is the
equal-time embedding $d_+$ in $\Omega_X\times\Omega_Y$, and the square
with the positive inclusions is Cartesian.

Write $A=r_X^{-1}F$ and $B=r_Y^{-1}G$. The external-product comparison

$$
Rj_{X*}A\boxtimes^L Rj_{Y*}B
\longrightarrow R(j_X\times j_Y)_*(A\boxtimes^L B)
$$

is adjoint to its restriction on $\Omega_X\times\Omega_Y$, where the
counits give the identity on $A\boxtimes^L B$. Pull it back along $d$
and use ordinary base change

$$
d^{-1}R(j_X\times j_Y)_*(A\boxtimes^L B)
\longrightarrow Rj_*d_+^{-1}(A\boxtimes^L B).
$$

The last inverse image is $r^{-1}(F\boxtimes^L G)$. Restricting the
composite to the central fibre gives SH02-SP-EXTERNAL-EQ. Finite global
dimension of $k$ ensures the tensor products of bounded inputs remain in
the bounded categories being used. No Künneth isomorphism for a nonproper
map, and no general isomorphism assertion for this comparison, is assumed.

## SH02-SP-TENSOR — Multiplication on one normal bundle

For $F,G\in D^b(k_X)$, pull the external comparison back by the normal
diagonal $\delta_E:E\to E\times E$. The map of pairs
$\delta_X:(X,M)\to(X\times X,M\times M)$ has normal map $\delta_E$.
Its comparison $\alpha$ gives the composite

$$
\begin{aligned}
\nu_MF\otimes^L\nu_MG
&\simeq\delta_E^{-1}(\nu_MF\boxtimes^L\nu_MG)\\
&\longrightarrow\delta_E^{-1}\nu_{M\times M}(F\boxtimes^L G)\\
&\longrightarrow\nu_M\delta_X^{-1}(F\boxtimes^L G)
\simeq\nu_M(F\otimes^L G).
\end{aligned}
\tag{SH02-SP-TENSOR-EQ}
$$

Naturality follows from that of the two comparisons. Their associativity
and symmetry follow by using a product of three deformation spaces and
restricting to the locus where all time coordinates agree: both composites
are adjoint to the same tensor product of restriction counits. The tensor
symmetry is the usual Koszul symmetry. The constant sheaf gives the unit,
since locally the positive half of a deformation chart is a product
half-neighborhood and $\nu_Mk_X\simeq k_E$. The displayed morphism need
not be an isomorphism; the example below exhibits a failure with elementary
closed supports.

## SH02-SP-HOMOGENEOUS — A calibration on a vector space

Let $V$ be a finite-dimensional real vector space, specialized along its
origin. Identify $T_{\{0\}}V$ with $V$. If $F\in D^b(k_V)$ is conic, then
there is a canonical identification

$$
\nu_{\{0\}}F\simeq F. \tag{SH02-SP-HOMOGENEOUS-EQ}
$$

In the deformation chart $p(v,t)=tv$, the positive pullback is canonically
identified with the pullback of $F$ under $(v,t)\mapsto v$, by normalized
conic transport. The stalk of its direct image at $(v,0)$ is computed on
products $U\times(0,\epsilon)$; interval descent gives $R\Gamma(U;F)$.
Passing to the stalk colimit gives $F_v$. These maps are the restrictions
of the conic transport map and hence glue and are natural. This proves the
claim without a finiteness hypothesis on the stalk modules.

One consequence is that specialization is not a tangent approximation of
supports alone. It retains the sheaf maps between angular pieces and the
zero section, as well as every cohomological shift.

## SH02-SP-EXAMPLE-SEPARATING-ARCS — Tensor products can lose a direction

In $X=\mathbb R^2$, specialize at the origin. Let

$$
A_+=\{(x,x^3):x\ge0\},\qquad
A_-=\{(x,-x^3):x\ge0\},
\qquad L=\{(u,0):u\ge0\}.
$$

Write $k_A$ for the constant sheaf on a closed subset $A$, extended by zero.
The maps $f_\pm:\mathbb R\to\mathbb R^2$ defined by
$f_\pm(x)=(x,\pm x^3)$ are proper closed embeddings, are clean with respect
to the origin, and induce the same normal map $x\mapsto(x,0)$.
The homogeneous calibration gives
$\nu_{\{0\}}k_{[0,\infty)}\simeq k_{[0,\infty)}$ on the line.
The proper direct-image theorem therefore gives

$$
\nu_{\{0\}}k_{A_+}\simeq k_L,
\qquad \nu_{\{0\}}k_{A_-}\simeq k_L.
$$

These sheaves are flat over $k$ stalkwise. Their derived tensor product
before specialization is $k_{A_+\cap A_-}=k_{\{0\}}$. Consequently the
tensor comparison has the form

$$
k_L\longrightarrow k_{\{0\}}.
$$

At a nonzero point of $L$, its source stalk is $k$ and its target stalk is
zero. For any nonzero coefficient ring, it is not an isomorphism. At the
origin the map is the identity under the zero-section identifications,
because the comparisons are made from the restriction counits. Thus the
map is the ordinary restriction from the closed ray to its endpoint.
The failure has a geometric explanation: the two curved supports meet only
at the origin, while their normal directions agree along the whole ray.

## SH02-SP-EXERCISE-ZERO-RANK — Specializing along the whole space

**Problem.** Compute specialization when $M=X$. Verify both formulas in
SH02-SP-ZERO-EQ and the boundary shift directly, for an arbitrary bounded
complex $F$.

**Solution.** The normal bundle has rank zero and equals $X$; the deformation
is $X\times\mathbb R$, and $p$ is projection. Restriction of
$Rj_*p^{-1}F|_{t>0}$ to $t=0$ is $F$ by interval descent. Thus $\nu_XF=F$,
and $e,\tau,i$ are all identities. For the exceptional expression, the
costalk at the endpoint of extension by zero from $(0,\infty)$ has the
parameter contribution $k[-1]$. The smooth projection contributes $[1]$.
Their composite is $F$, agreeing with the defining expression. This test
would detect a missing parameter shift in the boundary formula.

## SH02-SP-EXERCISE-OPEN-RAY — A nonzero costalk with zero stalk

**Problem.** Let $X=\mathbb R$, $M=\{0\}$ and
$F=k_{(0,\infty)}$, using extension by zero for the open inclusion.
Compute the specialization, its zero stalk, its zero costalk, and the
punctured direct image. Check the localization triangle and its shift.

**Solution.** The sheaf is conic, so the calibration gives $\nu_MF=F$ on
the normal line. Its stalk at zero is zero. On a small interval around zero,
the ordinary derived sections of $F$ vanish: in the triangle
$k_{(0,\infty)}\to k_{[0,\infty)}\to k_{\{0\}}\xrightarrow{+1}$,
the latter two section complexes are $k$ and the map is the identity.
On the punctured interval the section complex is $k$. The local-support
triangle is therefore

$$
k[-1]\longrightarrow0\longrightarrow k\xrightarrow{+1}.
$$

It proves $i^!F=k[-1]$. Equivalently, the normal proper direct image is
$R\Gamma_c((0,\infty);k)=k[-1]$, while the ordinary direct image from
the punctured normal line is $k$. All identifications agree with
SH02-SP-ZERO-EQ and SH02-SP-PUNCTURE-EQ. Zero ordinary stalk does not imply
zero costalk.

## SH02-SP-EXERCISE-PROPERNESS — Proper on the original support is insufficient

**Problem.** Let $f:\mathbb R\to\mathbb R$ be $f(y)=y^2$, and let
$N=M=\{0\}$ and $G=k_{\mathbb R}$, with $k\ne0$. Determine why the direct comparison
theorem cannot use only properness of $f$ on $\operatorname{supp}G$.

**Solution.** The map $f$ is proper, and
$\operatorname{supp}G\cap f^{-1}M=N$. Its normal map is the zero linear
map $q:\mathbb R\to\mathbb R$, since $df_0=0$. The normal cone of the
support is the whole line, on which $q$ is not proper.

The sheaf $Rf_*G=f_*G$ has stalk $k\oplus k$ at every positive point,
stalk $k$ at zero, and zero at negative points. There is no higher direct
image: inverse images of sufficiently small intervals are unions of
intervals, each acyclic for the constant sheaf. Positive scaling of the
target lifts to scaling by the positive square root on the source, so this
sheaf is conic. Its specialization is itself by the homogeneous calibration.
On the other hand,

$$
Rq_*\nu_NG=k_{\{0\}},\qquad
Rq_!\nu_NG=k_{\{0\}}[-1].
$$

The first formula uses $R\Gamma(\mathbb R;k)=k$, the second uses
$R\Gamma_c(\mathbb R;k)=k[-1]$. At a positive normal vector, either
direct image under $q$ has zero stalk, whereas $\nu_MRf_*G$ has stalk
$k\oplus k$. Thus $c_*$ is not an isomorphism; the analogous positive-stalk
test shows the failure of $c_!$ as well. The missing hypothesis is precisely
properness on the normal cone. In the deformation, points can run to infinity
in the rescaled normal coordinate while their target deformation points
remain bounded.

## SH02-SP-EXERCISE-ORIENTATION — Test a smooth projection

**Problem.** Let $Y=X\times\mathbb R^d$, let
$N=M\times\mathbb R^d$, and let $f$ be projection. Compute the normal map
and the relative complexes in SH02-SP-INVERSE-SQUARE. Does the calculation
require orientability of $M$ or $X$?

**Solution.** There are canonical identifications
$E_Y=E_X\times\mathbb R^d$ and $q$ is projection. Both $f$ and $f|_N$
are smooth, so $\alpha$ and $\beta$ are isomorphisms. The standard
orientation of $\mathbb R^d$ gives

$$
\omega_f=k_Y[d],\qquad\omega_q=k_{E_Y}[d].
$$

Thus $f^!F=f^{-1}F[d]$, and the square identifies
$\nu_Nf^{-1}F[d]$ with $q^{-1}\nu_MF[d]$ by the same normalized
pullback comparison. The orientation of $X$ cancels against its inverse,
as does the orientation of $M$ in the normal determinant calculation.
Neither manifold is required to be orientable. With a nontrivial vector
bundle in place of $\mathbb R^d$, keep its orientation local system instead
of replacing it by $k$; the shift is unchanged.

## SH02-SP-DEPENDENCY-BOUNDARY — What the arguments establish

The construction, neighborhood and support formulas, zero and punctured
recoveries, direct and inverse comparison maps, the three-hypothesis
properness result, the orientation square, and both tensor comparisons
have proofs in this unit relative to the contracts in SH02-SP-CONVENTIONS.
The properness argument and the solved comparisons also test the exceptional
cases that a support-only or unshifted account would miss.

This lesson uses deformation geometry, noncompact tautness, the bounded six-operation package with trace-compatible base change, the orientation trace and conic contraction as prerequisites; their full proofs are not given here. A next mathematical use is to apply Fourier--Sato transform in the normal fibres; that step belongs to the microlocalization unit and requires its separately audited sign and orientation conventions.

## SH02-SP-SOURCE-ACCOUNT — Sources and proof mechanisms

Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128
(1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf),
§2.2, supplies the deformation construction used here. Definition 2.2.1
takes ordinary derived direct image from the positive chamber and restricts
it to the normal bundle. Proposition 2.2.1 then records conicity, ordinary
and supported recovery on the zero section, and the neighborhood and
supported-section formulas. The present proof makes the passage from a
deformation neighborhood to sections explicit: cone avoidance chooses the
neighborhood system, interval-fibre descent removes the positive parameter,
and tautness passes to the central fibre. Localization supplies the
supported formula. The endpoint calculation fixes the particular
exceptional counit and its compatibility with the ordinary restriction
map; these checks cannot be replaced by a comparison of supports.

Propositions 2.2.2 and 2.2.3 of that work construct the direct and inverse
comparison maps by the positive and central Cartesian squares. Their
mechanism is retained here: use base change where its hypotheses hold,
and otherwise retain the natural comparison arrow. The source's short
proper-direct-image statement uses transversality and properness on the
support. For the arbitrary map of pairs used in this lesson, the explicit
support-intersection and normal-cone properness conditions in
SH02-SP-PROPER-GEOMETRY must still be checked. The rescaling argument there
is the proof of compactness needed by SH02-SP-PROPER, rather than an appeal
to a shorter criterion. For inverse image, the source also gives the
orientation square and the isomorphism result when the map and its
restriction to the submanifold are submersions. Here the determinant
calculation, the common oriented parameter, and the adjunction-mate checks
specify the maps and their shifts.

The coefficient and range conventions must be compared separately.
*Microlocal Study of Sheaves*, §1.3.1, starts with a unital coefficient ring
and assumes finite weak global dimension when forming the derived tensor
product. Its specialization definition and the three propositions above
use bounded-below complexes. This lesson deliberately fixes a commutative
ring of finite global dimension and bounded inputs, and lists the finite
cohomological amplitudes it needs as a prerequisite. It neither imports a
constructibility restriction nor establishes an unbounded version.

Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*
(1 August 2026)](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf)
provides a second view of the six-operation mechanisms. Theorem 4.5.3
proves proper-support base change by fibrewise acyclicity. Theorem 4.6.1
constructs exceptional inverse image as a right adjoint under a finite
cohomological-dimension hypothesis; Proposition 4.6.4 constructs its tensor
comparison from projection formula and adjunction. Definitions 5.1.4 and
5.1.6 record the orientation and relative orientation complexes, and
Proposition 5.1.9 proves the submersion formula by reduction to a product,
compactly supported cohomology of a convex fibre, and adjunction. These
are the operations used in the boundary, twist and inverse-comparison
arguments here, rather than a reason to assume all comparison arrows are
invertible.

Those notes do not discharge every prerequisite in this lesson: the
existence argument for the right adjoint invokes representability, the
identification with the classical differentiable orientation in
Proposition 5.1.5(d) refers elsewhere, and the final product step in the
submersion proof invokes Exercise 3.18. In particular, a source reference
does not close the noncompact tautness, interval-neighborhood, conic
contraction or trace-compatible orientation obligations listed above.
The common-time external comparison, homogeneous calibration, separating
arcs and solved problems remain part of this lesson's argument; no
general tensor isomorphism is inferred from the cited specialization
statements.

The independently written explanations in this lesson are offered under
CC0. This dedication does not change the terms of the cited human-authored
works or of any separately licensed reader components.
