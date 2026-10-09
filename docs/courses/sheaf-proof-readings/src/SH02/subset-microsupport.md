# SH02-SUB-UNIT — Reading a subset through its sheaf

The arguments use the coefficient, geometric and derived-operation hypotheses listed below. Each estimate identifies the support or restriction map that supplies it.

A subset records where a coefficient can live. Microsupport records which directions make its local extension problem fail. The distinction between a closed restriction and extension by zero from an open set therefore matters even when their ordinary closures agree. We first establish a geometric estimate valid for arbitrary open and closed sets, and then use exact sequences to compute examples whose boundaries meet or disappear.

## SH02-SUB-CONVENTIONS — Coefficients, supports, and the imported tests

Let $k$ be a commutative unital ring of finite global dimension. Manifolds are finite dimensional, countable at infinity, and at least $C^1$ wherever differential tests are used. The derived category is $D^b(k_X)$. There is no field, constructibility, finite generation, or perfect-stalk assumption.

For a locally closed inclusion $i:S\hookrightarrow X$, write $k_S=i_!k$, with the closed part of the inclusion interpreted as ordinary closed pushforward. Thus $k_S$ has stalk $k$ on $S$ and zero elsewhere, with its canonical extension structure. Stalk descriptions alone do not characterize an arbitrary sheaf: the extension structure is part of this notation. For a closed $B\subset A$ with $A$ locally closed, localization supplies

$$
k_{A\setminus B}\longrightarrow k_A\longrightarrow k_B\xrightarrow{+1}.
\tag{S1}
$$

We use the following explicit dependencies.

- `SH02-MST-TEST` defines microsupport by the vanishing, uniformly on an open neighborhood of a covector, of $(R\Gamma_{\{f\ge f(x)\}}F)_x$ for every $C^1$ test function. `SH02-MST-FORMAL` proves locality, $C^1$ coordinate invariance, closed positive conicity, the triangle inequalities, and the identification of zero covectors with the **closed** support.
- `SH02-GAM-TOPO` defines the topology $E_C$ whose open sets are ordinary open sets stable under addition by a closed convex cone $C$. `SH02-GAM-UNIT` proves the derived unit for $q_C:E\to E_C$ and hence the projector $P_C=q_C^{-1}Rq_{C*}$.
- `SH02-MST-CUTOFF-FORWARD` proves, for arbitrary closed convex $C$ including cones containing lines,
  $$
  \operatorname{SS}(P_CF)\subset E\times(-C^\circ).
  \tag{S2}
  $$
  It also proves that $P_CF\to F$ is a microlocal isomorphism on $E\times\operatorname{Int}(-C^\circ)$. These statements apply to bounded complexes.
- `SH02-NG-CONE-SEQUENCES` identifies the pair normal cone $C(A,B)$ with limits $c_n(a_n-b_n)$, where $a_n\in A$, $b_n\in B$, both tend to the base point, and $c_n\to+\infty$. `SH02-NG-CONE-CONSEQUENCES` proves locality and $C(B,A)=-C(A,B)$.
- Localization, exactness of filtered colimits, closed pushforward, inverse image of constant sheaves, and proper base change have their usual derived sheaf meanings. The elementary convex acyclicity used in the crossing calculation is the constant-coefficient specialization of `SH02-CA-CONSTANT`, whose proof is not given in this lesson; its precise content needed here is $R\Gamma(D;k)\simeq k$ for a nonempty convex locally closed subset of a finite-dimensional real vector space, compatibly with restrictions between such sets.

The corresponding lessons are [directional tests](../../SH02-microsupport-tests.html), [directional topology](../../SH02-cone-topology.html), [normal geometry](../../SH02-normal-geometry.html), and [convex acyclicity](../../SH02-convex-acyclicity.html).

For $D\subset E$ the polar and antipode are

$$
D^\circ=\{\xi\in E^*: \langle v,\xi\rangle\ge0\text{ for all }v\in D\},
\qquad D^a=-D.
\tag{S3}
$$

A closed convex cone contains $0$. It is pointed when it contains no nonzero line. The polar of the empty set is all of $E^*$. A nonempty open cone need not contain $0$.

All assertions of an exact nonempty microsupport for $k_S$ use $k\ne0$. For the zero ring every coefficient sheaf is zero and its microsupport is empty. More generally the proofs for a cone vertex, a submanifold, and a regular boundary work with any nonzero coefficient module placed in degree zero; no flatness is required.

## SH02-SUB-STRICT-DEFINITION — Directions which cannot cross out of a set

For an arbitrary subset $S\subset X$, with no local-closedness assumption, define

$$
N_x(S)=T_xX\setminus C_x(X\setminus S,S),
\qquad
N_x^*(S)=N_x(S)^\circ.
\tag{S4}
$$

Write $N(S)$ and $N^*(S)$ for the unions over $x$. We call these the strict normal cone and its conormal cone. The first is a cone of tangent vectors; the second is a cone of cotangent vectors. Neither is obtained simply by taking the usual tangent cone of $S$ and inserting a minus sign.

Here is the operational meaning of a nonzero $v\in N_x(S)$. In some coordinate neighborhood there are an ordinary neighborhood $U$ of $x$ and an open cone $G$ containing $v$ such that

$$
U\cap\bigl((S\cap U)+G\bigr)\subset S.
\tag{S5}
$$

It says that a small displacement in any direction in $G$ cannot take a point of $S$ to its complement while both endpoints remain in $U$.

**Proof of equivalence.** If no such pair $U,G$ exists, take successively smaller coordinate balls about $x$ and successively smaller cones about the ray through $v$. We obtain $a_n\notin S$ and $b_n\in S$, both tending to $x$, with $a_n-b_n$ pointing increasingly closely in direction $v$. The difference is nonzero because its endpoints have different membership. Rescale it to have norm $|v|$. The rescaling constants tend to infinity, and the resulting vectors converge to $v$. This is precisely $v\in C_x(X\setminus S,S)$. Conversely, a sequence representing that membership has, for large $n$, both endpoints in $U$ and its difference in $G$, contradicting (S5). The sequence criterion also proves that the construction is intrinsic under coordinate changes. $\square$

## SH02-SUB-STRICT-GEOMETRY — Openness, convexity, complements, and zero vectors

The subset $N(S)\subset TX$ is open because the pair normal cone is closed. Its fibres are convex open cones. Here are the details of convexity, which also explain why a strict cone behaves better than a general normal cone.

Take $v,w\in N_x(S)$ and directional neighborhoods $G_v,G_w$ satisfying (S5). First consider a nonzero vector $d$ in $G_v+G_w$. Near a chosen decomposition $d=a+b$ with $a\in G_v$, $b\in G_w$, every nearby vector has a decomposition into points of these same two cones with both summands bounded in norm. By scaling, sufficiently short displacements in a cone about $d$ can therefore be performed in two steps whose intermediate point stays in the original neighborhood. Each step preserves membership in $S$. After shrinking the neighborhood, (S5) holds for that cone about $d$, so $d\in N_x(S)$.

If a convex combination of permitted vectors is zero, the same argument gives more. The open Minkowski sum of appropriate positive scalar multiples of their directional neighborhoods contains a ball about zero. Every sufficiently short displacement, in any direction, is consequently a bounded two-step permitted displacement. On a smaller ball, either there is no point of $S$, or every point belongs to $S$. Thus $0\in N_x(S)$ and in fact $N_x(S)=T_xX$. Positive scalar multiples and zero coefficients in a convex combination cause no further issue. This proves fibrewise convexity including the zero-vector case.

More explicitly,

$$
N_x(S)=T_xX
\quad\Longleftrightarrow\quad
x\notin\overline S\ \text{or}\ x\in\operatorname{Int}S.
\tag{S6}
$$

The forward implication follows because, when $x$ lies in both $\overline S$ and $\overline{X\setminus S}$, choose sequences from the two sets converging to $x$ and rescale their differences slowly enough to obtain the zero vector in the pair cone. For example, if the differences have norm $r_n\to0$, replace the scale by $(\sqrt{r_n}+1/n)^{-1}$ after passing to sufficiently close endpoints; the product with $r_n$ tends to zero. The reverse implication follows because one of the two sets is absent in a neighborhood. Equivalently, $0\in N_x(S)$ exactly in the cases in (S6).

The polar fibres $N_x^*(S)$ are closed convex cones containing zero. The union $N^*(S)$ is closed in $T^*X$: if $\xi(v)<0$ for some $v\in N_x(S)$, extend $v$ as a local vector field staying in the open set $N(S)$. The same strict inequality persists for nearby covectors and keeps them out of $N^*(S)$.

When $N_x(S)\ne\varnothing$, its polar is pointed. Indeed a functional and its negative can both be nonnegative on a nonempty open set only when that functional vanishes. In positive dimension the converse holds: if $N_x(S)=\varnothing$, its polar is the whole dual vector space, which is not pointed. The statement that an empty strict cone is equivalent to a full dual fibre must be handled separately in dimension zero: there the whole dual space is itself $\{0\}$. Every subset of a zero-dimensional manifold is open and closed, and (S6) gives $N_x(S)=T_xX=\{0\}$ at every point.

Exchanging the two sets in the pair cone proves

$$
N_x(X\setminus S)=-N_x(S),
\qquad
N_x^*(X\setminus S)=-N_x^*(S).
\tag{S7}
$$

Thus the conormal of a set and that of its complement have opposite signs even though both contain their zero covectors everywhere.

## SH02-SUB-CONE-TOPOLOGY — Recognizing directional open and closed sets locally

Let $E$ be a finite-dimensional real vector space, let $C\subset E$ be pointed, closed, convex, with nonempty interior, and fix $x\in E$. An ordinary open set $O$ is **locally $C$-open at $x$** if some neighborhood $U$ satisfies

$$
U\cap((O\cap U)+C)\subset O.
\tag{S8}
$$

A closed set is locally $C$-closed if its complement is locally $C$-open. These are local statements; neither requires that the original set be globally invariant under addition.

For an open $O$ and a closed $Z$ the implications are

$$
\begin{aligned}
N_x^*(O)\subset\operatorname{Int}C^\circ\cup\{0\}
&\Longrightarrow O\text{ is locally }C\text{-open at }x,\\
-N_x^*(Z)\subset\operatorname{Int}C^\circ\cup\{0\}
&\Longrightarrow Z\text{ is locally }C\text{-closed at }x.
\end{aligned}
\tag{S9}
$$

Conversely,

$$
\begin{aligned}
O\text{ locally }C\text{-open at }x&\Longrightarrow N_x^*(O)\subset C^\circ,\\
Z\text{ locally }C\text{-closed at }x&\Longrightarrow-N_x^*(Z)\subset C^\circ.
\end{aligned}
\tag{S10}
$$

**Proof.** Work first in positive dimension with $O$. Put $D=N_x^*(O)$. The assumption in (S9) implies $N_x(O)\ne\varnothing$; a full dual space cannot be contained in a pointed cone together with zero. For a nonempty open convex cone $G$, elementary separation gives $G=\operatorname{Int}((G^\circ)^\circ)$, unless $G=E$, where the same formula still holds. Hence $N_x(O)=\operatorname{Int}D^\circ$.

Every nonzero $c\in C$ pairs strictly positively with every nonzero $\xi\in D$, because $\xi$ is in the interior of $C^\circ$. Compactness of the unit slice of $D$ makes the positivity uniform when $c$ is fixed. Therefore $c\in\operatorname{Int}D^\circ=N_x(O)$. If $D=\{0\}$ this conclusion is immediate. For each direction of $C$, choose a cone of permitted displacements as in (S5). The compact set $C\cap S(E)$ has a finite subcover. Intersect the corresponding ordinary neighborhoods. Every nonzero displacement in $C$ is then permitted, and displacement zero is harmless. This proves (S8).

For the converse, every $v\in\operatorname{Int}C$ has an open cone neighborhood contained in $C$. Condition (S8) makes it a permitted direction, so $\operatorname{Int}C\subset N_x(O)$. Taking polars and using $C=\overline{\operatorname{Int}C}$ gives $D\subset C^\circ$. Complementation and (S7) prove the closed-set assertions. In dimension zero all statements are immediate from the discrete topology. $\square$

The gap between the interior in (S9) and the closed polar in (S10) is intentional. Inclusion on the boundary of a dual cone need not give the uniform room needed to choose one neighborhood for all directions of $C$.

For later use, a local $C$-open set can be replaced by a global one. If (S8) holds on $U$, choose a smaller ball $V\subset U$ and put

$$
\widetilde O=(O\cap V)+C.
\tag{S11}
$$

This is an ordinary open $C$-open subset of $E$, and $\widetilde O\cap V=O\cap V$. Both endpoints in this last equality lie in $U$, so (S8) applies directly; no properness of a projection is involved. The complementary construction treats a locally $C$-closed set.

## SH02-SUB-BOUND — A geometric upper bound for arbitrary open or closed sets

For every open $O\subset X$ and every closed $Z\subset X$,

$$
\operatorname{SS}(k_O)\subset -N^*(O),
\qquad
\operatorname{SS}(k_Z)\subset N^*(Z).
\tag{S12}
$$

The right sides are defined even at points outside the closed support. There they may contain a zero vector that is absent on the left; the assertion is an inclusion.

**Proof for open sets.** Suppose $\eta\notin-N_x^*(O)$. By the definition of the polar there is a vector $v\in N_x(O)$ with $\eta(v)>0$. In positive dimension choose a sufficiently narrow pointed closed convex cone $C$, with nonempty interior and $v$ in its interior, so that $C\setminus\{0\}$ lies in a permitted cone from (S5). Then $O$ is locally $C$-open. Replace it by $\widetilde O$ from (S11), which does not change its sheaf or microsupport near $x$.

As an open set of $E_C$, $\widetilde O$ carries its constant sheaf extended by zero to $E_C$. Its inverse image under $q_C$ is exactly $k_{\widetilde O}$: inverse image commutes with open extension by zero and carries the constant sheaf to the constant sheaf. The derived unit therefore gives

$$
P_Ck_{\widetilde O}\simeq k_{\widetilde O}.
\tag{S13}
$$

The cutoff inclusion (S2) now excludes every covector pairing positively with some vector of $C$, in particular $(x,\eta)$. This is an exclusion on an open neighborhood as required by the definition, not merely vanishing for one selected test function. In dimension zero the estimate follows directly from zero-section support.

For the closed assertion, apply the open estimate to $O=X\setminus Z$ and the triangle $k_O\to k_X\to k_Z\xrightarrow{+1}$. The constant sheaf has only zero covectors in its microsupport: this also follows from (S2) with $C=E$, since it is an inverse image from the indiscrete directional topology. By (S7), $-N^*(O)=N^*(Z)$, and every zero vector lies in $N^*(Z)$. The triangle inequality proves the result. $\square$

The estimate uses the pair cone of the complement against the set. Replacing that cone by a single tangent cone, or omitting the antipode for an open extension, changes the assertion.

## SH02-SUB-CONVEX-VERTEX — The vertex of a closed convex cone

Let $D\subset E$ be any closed convex cone. It may contain lines, have empty interior, equal $\{0\}$, or equal $E$. For $k\ne0$,

$$
\operatorname{SS}(k_D)\cap T_0^*E=D^\circ.
\tag{S14}
$$

**Upper inclusion.** The complement of $D$ is stable under addition by $-D$: if $a\notin D$ and $a-d\in D$ with $d\in D$, then $a=(a-d)+d\in D$, a contradiction. Thus $D$ is a closed subset of $E_{-D}$. The inverse image of its closed constant sheaf is $k_D$. One can verify this without any nonproper base-change assertion: the natural map of the two closed-constant sheaves has the identity on the stalks over $D$ and zero stalks elsewhere. The derived unit gives $P_{-D}k_D\simeq k_D$, and (S2) bounds its entire microsupport by $E\times D^\circ$.

**Lower inclusion at the vertex.** For $\xi\in D^\circ$, the linear function $f(y)=\langle y,\xi\rangle$ is nonnegative on $D$. The local section equal to $1$ on $D$ is supported in $\{f\ge0\}$ and has a nonzero germ at $0$. Hence

$$
H^0\bigl((R\Gamma_{\{f\ge0\}}k_D)_0\bigr)\ne0.
\tag{S15}
$$

One nonzero test at $(0,\xi)$ prevents the required neighborhood of uniformly vanishing tests. This proves the lower inclusion, including $\xi=0$. $\square$

This proof explains why pointedness and full dimension are unnecessary for the vertex formula. If $D$ is a vector subspace, $D^\circ$ is its annihilator, because both $v$ and $-v$ must pair nonnegatively. If $D=\{0\}$ the whole cotangent fibre occurs; if $D=E$ only the zero covector occurs.

## SH02-SUB-SMOOTH-MODELS — Submanifolds and regular boundaries

For a **closed embedded submanifold** $M\subset X$ and $k\ne0$,

$$
\operatorname{SS}(k_M)=T_M^*X.
\tag{S16}
$$

Indeed a local $C^1$ submanifold chart identifies $M$ with a vector subspace. Apply (S14) after translation to every point of that subspace, and use coordinate invariance. Outside $M$ the sheaf is locally zero. In particular $\operatorname{SS}(k_X)=T_X^*X$.

If $M$ is only locally closed, (S16) holds after restriction to an open ambient neighborhood in which $M$ is closed. It is not a global formula in the original ambient manifold: boundary points of $M$ outside $M$ can contribute microsupport.

Let $f:X\to\mathbb R$ be $C^1$, with $df\ne0$ on $f^{-1}(0)$. Set $Z=\{f\ge0\}$ and $O=\{f>0\}$. Then

$$
\begin{aligned}
\operatorname{SS}(k_Z)
={}&\{(x,0):f(x)\ge0\}\\
&\cup\{(x,\lambda df_x):f(x)=0,\ \lambda>0\},
\end{aligned}
\tag{S17}
$$

and

$$
\begin{aligned}
\operatorname{SS}(k_O)
={}&\{(x,0):f(x)\ge0\}\\
&\cup\{(x,\lambda df_x):f(x)=0,\ \lambda<0\}.
\end{aligned}
\tag{S18}
$$

**Proof.** At a boundary point the $C^1$ inverse function theorem makes $f$ one coordinate. A closed halfspace is a translated closed convex cone, so its polar is the nonnegative ray in the positive coordinate differential, proving (S17). Interior points carry the constant sheaf, and exterior points carry zero.

For (S18), use the triangle

$$
k_{\{f>0\}}\longrightarrow k_X\longrightarrow k_{\{f\le0\}}\xrightarrow{+1}.
\tag{S19}
$$

At a nonzero covector the middle term has no microsupport. The triangle inequalities then identify the microsupports of the other two terms there. Formula (S17), applied to $-f$, yields the negative ray. Zero covectors lie over $\overline O=\{f\ge0\}$, because the regularity assumption makes every boundary point a limit of points of $O$. This proves the complete formula, despite $(k_O)_x=0$ at its boundary. $\square$

For comparison, $N_x(Z)=N_x(O)=\{v:df_x(v)>0\}$ at a regular boundary point, so both conormal fibres are $\mathbb R_{\ge0}df_x$. The sign difference between (S17) and (S18) comes entirely from the two sheaf extension operations.

## SH02-SUB-TANGENTIAL-CHANNEL — Two faces meeting at an omitted point

A useful class of examples comes from two functions $b_-,b_+:\mathbb R\to\mathbb R$ of class $C^1$. Suppose

$$
b_-(u)=b_+(u)\quad(u\le0),\qquad
b_-(u)<b_+(u)\quad(u>0),
\tag{S20}
$$

and $b_-(0)=b_+(0)=0$. Their derivatives at zero necessarily agree; write the common derivative as $m$. Define the half-open channel

$$
A=\{(u,v):v\ge b_-(u)\},\qquad
B=\{(u,v):v\ge b_+(u)\},\qquad
S=A\setminus B.
\tag{S21}
$$

Since $B\subset A$ are closed, $S$ is locally closed. It consists of the points $u>0$ between the two graphs, with the lower face included and the upper face excluded. The origin is excluded as well.

For $k\ne0$, its full microsupport is the union of the following sets:

$$
\begin{gathered}
\{(z,0):z\in\overline S\},\\
\{((u,b_-(u)),\lambda(-b_-'(u),1)):u>0,\ \lambda>0\},\\
\{((u,b_+(u)),\lambda(-b_+'(u),1)):u>0,\ \lambda>0\},\\
\{((0,0),\lambda(-m,1)):\lambda>0\}.
\end{gathered}
\tag{S22}
$$

**Proof.** The triangle $k_S\to k_A\to k_B\xrightarrow{+1}$ bounds the microsupport of $k_S$ by the union of the two closed-superlevel microsupports. Both defining functions have $v$ derivative equal to one, so (S17) applies globally. At $(0,0)$ their nonzero conormals agree and equal the positive ray through $(-m,1)$. Away from $\overline S$, the sheaf is locally zero, even where the two larger epigraphs happen to have a common boundary.

At a lower face with $u>0$, the two graphs have positive separation, and a small neighborhood of that face meets no point of $B$. There $k_S=k_A$, proving equality with the first family of face covectors. At an upper face, a small neighborhood lies in the interior of $A$, and $S$ is locally the open sublevel $v<b_+(u)$. Formula (S18), applied to $b_+(u)-v$, gives the **same upward** sign shown in (S22). The face covectors approach every positive multiple of $(-m,1)$ at the origin, so closedness of microsupport supplies the last line. Zero covectors occur exactly over $\overline S$. These lower inclusions exhaust the upper estimate. $\square$

For a concrete calculation take

$$
b_-(u)=-2(u_+)^4,\qquad b_+(u)=5(u_+)^4,\qquad u_+=\max(u,0).
\tag{S23}
$$

The functions are $C^3$, which is more than needed. The two face directions are respectively

$$
\lambda(8u^3,1),\qquad \lambda(-20u^3,1),\qquad u>0,\ \lambda>0.
\tag{S24}
$$

At the missing tip the fibre is $\{(0,\beta):\beta\ge0\}$. Thus there is a nonzero directional obstruction at a point where the stalk of $k_S$ is zero. The two faces supply only one vertical ray there, even though one face is included and the other is excluded. Their boundary normals already have opposite geometric orientations, and changing the extension type reverses one of them a second time.

## SH02-SUB-CROSSING — A nonconvex cotangent fibre

Let $E$ have positive dimension, and let $D\subset E$ be a pointed closed convex cone with nonempty interior. Put

$$
Z=D\cup(-D).
\tag{S25}
$$

The two cones intersect only at zero. Then, for $k\ne0$,

$$
\operatorname{SS}(k_Z)\cap T_0^*E
=E^*\setminus\bigl(\operatorname{Int}D^\circ
\cup\operatorname{Int}(-D^\circ)\bigr).
\tag{S26}
$$

This formula is generally nonconvex. It is a calculation of the actual microsupport, rather than of the convex conormal bound.

**The algebra of the meeting point.** Closed-set restriction gives an exact sequence

$$
0\longrightarrow k_Z
\longrightarrow k_D\oplus k_{-D}
\xrightarrow{r_D-r_{-D}}k_{\{0\}}
\longrightarrow0.
\tag{S27}
$$

At zero this is the diagonal and difference sequence $0\to k\to k\oplus k\to k\to0$; at every other point it is plainly exact. No division or field assumption enters.

Apply $P_{-D}$. We have

$$
P_{-D}k_D\simeq k_D,\qquad
P_{-D}k_{\{0\}}\simeq k_D,\qquad
P_{-D}k_{-D}\simeq k_E.
\tag{S28}
$$

The first identity was proved for the vertex model. The second is the skyscraper calculation `SH02-GAM-EX-SKY`. To verify the third without substituting a nonproper closed fibre, compute the direct image on a basis of nonempty convex $(-D)$-open sets $U$. The intersection $U\cap(-D)$ is nonempty: choose $u\in U$ and $d\in\operatorname{Int}D$; for sufficiently large $t$, $u-td\in-D$, and it remains in $U$. The intersection is locally closed and convex, so its coefficient cohomology is canonically $k$ in degree zero, with identity restrictions. It follows on this basis that $Rq_{-D*}k_{-D}$ is the constant sheaf of $E_{-D}$. Pulling back proves the third identity.

Under the first two identities, the morphism $P_{-D}(r_D)$ is an isomorphism. Indeed on a convex directional neighborhood that contributes a stalk on $D$, restriction from its nonempty convex intersection with $D$ to zero is the identity on constants. The skyscraper calculation and fixedness show that both sides vanish off $D$. Thus (S27) becomes a triangle whose second arrow is a map

$$
k_D\oplus k_E\longrightarrow k_D
\tag{S29}
$$

with its first component invertible. Its fibre is $k_E$, by the elementary automorphism subtracting the second component from the first coordinate. Consequently $P_{-D}k_Z\simeq k_E$.

The cutoff counit is a microlocal isomorphism on $E\times\operatorname{Int}D^\circ$. This open cone contains no zero covector because $D$ has nonzero vectors. The constant sheaf has no microsupport there, and hence neither does $k_Z$. Replacing $D$ by $-D$ excludes the other open cone in (S26).

**The remaining directions.** If $\xi\notin D^\circ\cup(-D^\circ)$, neither of the two cone sheaves in (S27) has microsupport at $(0,\xi)$, by (S14). The skyscraper does have microsupport there. The triangle inequality forces $(0,\xi)\in\operatorname{SS}(k_Z)$. A nonzero boundary point of $D^\circ$ does not lie in $-D^\circ$, since $D^\circ$ is pointed. It is therefore a limit of points outside both closed cones; closedness of microsupport supplies every such boundary direction. The same argument applies to the opposite cone. Finally zero belongs because $k_Z$ is nonzero at zero. In dimension one the two open dual rays leave only zero, and this last argument gives the entire answer. This proves (S26). $\square$

For example, in coordinates $(u,v)$ let

$$
D=\{(u,v):u\ge2|v|\}.
\tag{S30}
$$

Pairing with the two edge directions $(2,1)$ and $(2,-1)$ gives

$$
D^\circ=\{(\alpha,\beta):2\alpha\ge|\beta|\}.
\tag{S31}
$$

The cotangent fibre of the double wedge is therefore

$$
\{(\alpha,\beta):|\beta|\ge2|\alpha|\}.
\tag{S32}
$$

The vectors $(1,2)$ and $(1,-2)$ belong to this fibre, but their midpoint $(1,0)$ does not. In contrast, every fibre $N_x^*(Z)$ is convex. A strict-conormal upper estimate can therefore lose information even for a union of two convex polyhedral sets.

The zero-dimensional case of (S25) is a single point. Its microsupport is the single zero covector when $k\ne0$. It is excluded from the hypothesis of (S26) because, in a zero-dimensional vector space, the interior of $\{0\}$ is $\{0\}$ itself.

## SH02-SUB-CONVEX-SETS — Supporting hyperplanes for arbitrary convex sets

The vertex calculation extends to every point of every closed convex set. If $Z\subset E$ is closed and convex and $x\in Z$, define

$$
T_xZ=\overline{\bigcup_{t>0}t(Z-x)}.
\tag{S34}
$$

The normal-cone sequence criterion identifies this with the normal cone of $Z$ along the one-point submanifold $\{x\}$. Indeed a scaled sequence from $Z-x$ lies in the displayed closed cone. Conversely, for a vector in its closure, approximate it by $t_n(z_n-x)$ and then move $z_n$ toward $x$ along its segment until the new point is within $1/n$ of $x$. Increasing the scale by the reciprocal segment factor preserves the approximating vector and makes the scales tend to infinity. Convexity is what keeps these new points in $Z$.

For $k\ne0$ the full formula is

$$
\operatorname{SS}(k_Z)
=\{(x,\xi):x\in Z,\ \langle z-x,\xi\rangle\ge0\text{ for every }z\in Z\}.
\tag{S35}
$$

Equivalently the fibre at $x$ is $(T_xZ)^\circ$.

**A convex displacement lemma.** Work first in the affine hull $L$ of $Z$, translated so that $x=0$. If $Z$ is not a point, it has nonempty relative interior and

$$
\operatorname{Int}_L T_xZ
=\bigcup_{t>0}t(\operatorname{Int}_LZ-x).
\tag{S36}
$$

To verify this, the right side is a nonempty open convex cone. Its closure is $T_xZ$: for any $z\in Z$ and a fixed relative interior point $a$, the points $(1-\varepsilon)z+\varepsilon a$ are relative interior points tending to $z$. The interior of the closure of a nonempty open convex set equals that set, by separation. This proves (S36).

For $v$ in the cone (S36), choose $t>0$ and a relative ball about $x+tv$ contained in $\operatorname{Int}_LZ$. There are a neighborhood $U$ of $x$ in $L$ and a narrow cone $G\subset L$ about $v$ such that sufficiently short displacements in $G$, starting in $Z\cap U$ and ending in $U$, preserve $Z$. Here is a quantitative way to see the point. For unit directions $e$ near $v/|v|$, choose $t_0>0$ so that $x+t_0e$ remains in that relative ball. If $b\in Z$ is close to $x$, then $b+t_0e$ remains in the same ball. For $0\le r\le t_0$,

$$
b+re=\left(1-\frac r{t_0}\right)b
+\frac r{t_0}(b+t_0e)\in Z.
\tag{S37}
$$

Shrinking $U$ makes every displacement with both endpoints in $U$ shorter than $t_0$. This proves the required uniform directional stability. The same argument preserves $\operatorname{Int}_LZ$ when the starting point lies there.

**Proof of (S35).** The lower inclusion is the supported-section argument (S15), now with the affine function $\langle y-x,\xi\rangle$. For the upper inclusion, suppose $\xi\notin(T_xZ)^\circ$. If $Z$ is a point, there is no such covector. Otherwise choose $v\in\operatorname{Int}_LT_xZ$ with $\xi(v)<0$, by perturbing a vector on which the pairing is negative. The displacement lemma supplies a narrow pointed closed convex cone $C\subset L$ around $v$ for which $Z$ is locally stable under addition by $C$. Considered in the full space $E$, $C$ may have empty interior; this is allowed in the cutoff theorem.

The complement of $Z$ is locally stable under addition by $-C$. For if $a\notin Z$ and $a-c\in Z$ with both points sufficiently close to $x$, stability of $Z$ would give $a\in Z$. A point outside $L$ remains outside $L$ after these displacements, so the same reasoning works in an ordinary ambient neighborhood in $E$. Thus $Z$ is locally a closed set for the $(-C)$-topology. The saturation construction (S11), applied to its complement, replaces it by a globally $(-C)$-closed set without changing it near $x$. Its coefficient sheaf is fixed by $P_{-C}$, whose microsupport lies in $E\times C^\circ$. Since $\xi(v)<0$, it cannot contain $(x,\xi)$. This proves the upper inclusion without imposing full dimension on $Z$ and without invoking a closed-embedding microsupport theorem. $\square$

Now let $O\subset E$ be open and convex. For $k\ne0$,

$$
\operatorname{SS}(k_O)
=\operatorname{SS}(k_{\overline O})^a.
\tag{S38}
$$

The empty set gives the empty microsupport on both sides. In dimension zero the assertion is immediate. For the remaining cases, the following proof has one additional, explicit dependency: the internal-Hom estimate in `SH02-MO-DIAGONAL`, with its second argument the constant sheaf. Its exact specialization is

$$
\operatorname{SS}(R\mathcal Hom(F,k_E))
\subset\operatorname{SS}(F)^a,\qquad F\in D^b(k_E),
\tag{S39}
$$

when the resulting Hom object is bounded; the usual microsupport transversality condition is automatic because $k_E$ has only zero covectors. The general functorial estimate uses the earlier strict-conormal bound, not (S38), so this is an item-level dependency in one direction. Its independent verification is not supplied by the present argument.

**Upper inclusion.** At a boundary point $x\in\partial O$, the displacement lemma gives

$$
N_x(O)=\operatorname{Int}T_x\overline O.
\tag{S40}
$$

For the remaining inclusion in this geometric identity, a permitted open cone of displacements sends points of $O$ approaching $x$ into $O$. Passing to the limit shows that every direction in that open cone lies in $T_x\overline O$; hence its original direction lies in the interior. Taking polars in (S40) and using (S12) proves that $\operatorname{SS}(k_O)$ at $x$ lies in $-(T_x\overline O)^\circ$. Interior and exterior points have already been computed. Formula (S35) proves the desired upper inclusion globally.

**Lower inclusion.** If $j:O\hookrightarrow E$, open adjunction gives

$$
R\mathcal Hom(k_O,k_E)\simeq Rj_*k_O\simeq k_{\overline O}.
\tag{S41}
$$

For the last isomorphism, on ordinary convex open neighborhoods $U$ the intersection $U\cap O$ is empty or convex and nonempty. Its constant coefficient cohomology is respectively zero or $k$ in degree zero. The map $k_E\to Rj_*k_O$ has stalk zero outside $\overline O$ and the identity on $k$ at every point of $\overline O$; it factors through $k_{\overline O}$ and gives the asserted isomorphism. This uses an open-neighborhood colimit, not a closed-fibre computation for a nonproper map. In particular the Hom object is bounded. Applying (S39) to (S41) yields

$$
\operatorname{SS}(k_{\overline O})
\subset\operatorname{SS}(k_O)^a,
\tag{S42}
$$

which is exactly the missing inclusion after applying the antipode. $\square$

For a worked application, let $Z=\{(u,v):u^2+4v^2\le9\}$. At an interior point the fibre is zero. At a boundary point the inward polar normal is the ray through $(-2u,-8v)$, so (S35) gives this nonnegative ray for $k_Z$. For the open ellipse, (S38) reverses it to the ray through $(2u,8v)$. The zero section over the closed ellipse occurs in both cases. The calculation uses a nonconstant curvature boundary, and the result allows every nonzero coefficient ring satisfying the course assumptions.

## SH02-SUB-PROBLEMS — Exercises with worked solutions

**1. An interval with one included endpoint.** Compute the microsupport of $M_{[2,7)}$ on $\mathbb R$, where $M$ is any nonzero $k$-module.

**Solution.** On $(2,7)$ only zero covectors occur. At $2$, the set is locally the closed superlevel $x-2\ge0$, so all nonnegative multiples of $dx$ occur. At $7$, it is locally the open superlevel $7-x>0$, whose negative multiples of $d(7-x)$ are again the nonnegative multiples of $dx$. Thus the result is the zero section over $[2,7]$, together with the strictly positive cotangent rays at both endpoints. All other fibres are empty. In particular $7$ contributes a zero covector despite its zero stalk. The proof of (S17)–(S18) uses the nonzero element of $M$ and exact diagonal maps only, so the calculation applies, for example, to $k=\mathbb Z$ and $M=\mathbb Z/8\mathbb Z$.

**2. A smooth submanifold that is not closed.** Regard $(2,7)$ as a one-dimensional submanifold of $\mathbb R$. Explain the failure of the global formula $\operatorname{SS}(k_M)=T_M^*\mathbb R$.

**Solution.** The right side is only the zero section over $(2,7)$. The open extension has, at $2$, the nonpositive ray in $dx$, and, at $7$, the nonnegative ray in $dx$, by applying (S18) to the two boundary coordinates. It also has zero covectors over both endpoints. Restriction to the ambient open manifold $(2,7)$ does satisfy the submanifold formula. The lost hypothesis in a global application is closedness in the ambient space.

**3. Compute the strict cone at the edge of a halfspace.** At $0\in\mathbb R^n$, take $S=\{x_1\ge0\}$ or $S=\{x_1>0\}$. Calculate the pair cone, strict cone, and conormal.

**Solution.** Every complement-minus-set difference has first coordinate at most zero. Every vector with first coordinate strictly negative is realized by choosing endpoints on opposite sides, and taking limits adds the vectors with first coordinate zero. Hence

$$
C_0(X\setminus S,S)=\{v:v_1\le0\},\quad
N_0(S)=\{v:v_1>0\},\quad
N_0^*(S)=\mathbb R_{\ge0}dx_1.
\tag{S33}
$$

These are the same for the open and closed halfspace. Their sheaf microsupport rays differ by the antipode, precisely as in (S12).

**4. A strict estimate with no nonzero information.** Let $S$ be dense in a positive-dimensional coordinate ball and suppose its complement is also dense. Compute $N_x(S)$ at a point in the ball.

**Solution.** For any vector $v$ choose target endpoints near $x+\varepsilon_nv/2$ in the complement and near $x-\varepsilon_nv/2$ in $S$, with errors $o(\varepsilon_n)$ and $\varepsilon_n\downarrow0$. Scaling by $\varepsilon_n^{-1}$ gives every $v$ in the pair cone. Thus $N_x(S)=\varnothing$ and $N_x^*(S)=T_x^*X$. This is a statement about arbitrary subsets and normal geometry. It does not introduce $k_S$ for a set that has not been shown locally closed.

**5. Change both extension choices in the channel.** In (S21), replace the half-open strip by $S'=\{u>0:b_-(u)<v\le b_+(u)\}$. Determine the nonzero cotangent fibre at the origin.

**Solution.** Negating the vertical coordinate sends the new strip to a channel of the already proved type, with lower function $-b_+$ and upper function $-b_-$. Formula (S22) gives the ray $\mathbb R_{>0}(m,-1)$ when transported back. Equivalently it is the negative ray through $(-m,1)$. The zero covector remains present. This checks the joint effect of changing the two extension choices without making an unjustified separate-face prediction at the missing tip.

## SH02-SUB-RESEARCH — What remains visible in these estimates

For a smooth boundary the strict conormal estimate is exact. For a double wedge the actual cotangent fibre is nonconvex, while the strict conormal is convex. Studying where information is lost in the polarity step gives a concrete route from elementary subset geometry to finer microlocal invariants. The half-open channel gives a second route: vary the order of tangency while tracking the same limiting cotangent ray, then compare sheaves that differ in their extension behavior but have the same closed ordinary support.

## SH02-SUB-SOURCES — Classical models, proof mechanisms, and remaining foundations

The strict normal cone is a classical construction. Kashiwara and Schapira's freely available [Microlocal study of sheaves, Astérisque 128 (1985), §1.2.3, printed pp. 20–21](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf) defines it by excluding complement-minus-set normal directions and then taking the positive polar. Section 3.1.3, printed p. 54, gives closed and open halfspaces, the polar at a closed-cone vertex, a crossing with a nonconvex cotangent fibre, and cusp models. These are mathematical antecedents for the examples here. Changing coordinates or numerical parameters would not make those classical patterns new.

**Strict directions and polar signs.** Section 1.2.3 states openness and convexity and describes permitted displacements. SH02-SUB-STRICT-DEFINITION and its following proofs derive the uniform displacement criterion from normal-cone sequences. They treat the zero vector and the zero-dimensional case explicitly before applying polarity.

**Closed and open extensions.** The source's §3.1.3 examples 2–4 distinguish the positive ray for a closed halfspace from the negative ray for an open halfspace. Here the directional projector first proves the general strict-conormal upper bounds. Local supported sections supply lower bounds, and localization changes the sign for open extension. Closed ordinary support includes boundary points whose stalks vanish.

**Cone vertices and intersecting boundaries.** Example 3 states the closed-cone vertex formula; example 5 gives a crossing whose cotangent fibre is nonconvex. Here the vertex argument permits cones containing lines. The double-cone calculation uses the diagonal-and-difference exact sequence and a projector comparison to prove the formula for an arbitrary pointed full-dimensional closed convex cone, with the one-dimensional and zero-dimensional cases separated.

**Tangent boundaries.** The cusp examples on p. 54 show that a singular tip can contribute a cotangent ray. The channel argument here treats two arbitrary stated once-differentiable boundary functions with a common tangent. It first identifies the exact extension sequence, then calculates the two face rays and proves their limiting contribution at the missing tip. The quartic instance tests that family; it is not the basis for an originality claim.

**Arbitrary convex sets.** The later convex-set argument proves its relative-interior displacement lemma and explicitly retains lower-dimensional affine hulls. The open-convex lower bound additionally uses the named MO-diagonal Hom estimate in (S39); it is not a consequence of convex geometry alone.

Pierre Schapira's [A short review on microlocal sheaf theory, 19 January 2016, pp. 6–9](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) provides a second comparison. Definition 2.3 uses one neighborhood of a covector for all support tests; Example 2.5(ii)–(iii) gives closed submanifolds and regular open and closed boundaries with the same sign conventions used here. Theorem 2.6 states the cap and directional-topology characterizations for bounded complexes. Those notes assume a commutative unital ring of finite global dimension and familiarity with derived sheaf operations. Their statements do not replace proofs of the programme's imported tests or projector.

The exposition here is organized around which extension sequence produces a boundary direction: establish the strict-cone estimate, prove equality in basic local models, resolve colliding boundaries, and then examine convex sets and five coefficient-sensitive or extension-sensitive exercises. The extended proofs, uniform displacement checks, parameter families and complete solutions give the teaching content. The named classical constructions retain the attribution above. No source diagram or source prose is reproduced in this reading.

The independently written programme text is CC0. The linked human works retain their own terms; access to the Astérisque volume does not relicense it. Full proof closure of derived localization and base change, convex acyclicity, the directional projector, the support-test equivalence, normal geometry, and the particular MO-diagonal estimate remains a separate prerequisite obligation.
