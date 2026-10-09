# SH02-SA — What a normal limit preserves

The specialization theory used here goes back to M. Kashiwara and P. Schapira,
[*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf),
Astérisque 128 (1985), §2.2. This lesson proves removal, homogeneous
recovery, and three comparison constructions. It also gives an explicit
counterexample to an unrestricted support equality and states the valid
closed-set version. Public domain (CC0).

## SH02-SA-SETUP — Coefficients, supports, and the available maps

Let $k$ be a commutative unital ring of finite global dimension. Manifolds
are finite dimensional, Hausdorff, and countable at infinity; maps and
embedded submanifolds are $C^\infty$. Real analytic manifolds are included.
No constructibility, finite rank, field, orientability, or compactness
hypothesis is imposed on the sheaves in the general statements. All inputs
are bounded complexes of sheaves of $k$-modules. Write

$$
i:M\hookrightarrow X,\qquad E=N_MX,
\qquad \nu=\nu_M:D^b(k_X)\longrightarrow D^b(k_E)
$$

for a closed embedded submanifold and its specialization. For a locally
closed submanifold, use an open ambient neighborhood in which it is closed;
the constructions below respect subsequent restriction.

For a locally closed subset $S$, $k_S$ denotes its constant sheaf extended
by zero, using open extension inside its closure followed by closed direct
image. It has stalk $k$ on $S$ and zero stalk off $S$. The support used in
normal-cone estimates is the **closed support**, the closure of the union
of the nonzero cohomology stalks. Thus, when $k\ne0$,
$\operatorname{supp}k_S=\overline S$, including points where the stalk
itself is zero. We use $H^a(A[n])=H^{a+n}(A)$ and derived tensor products.
In particular, $k[-1]$ has its nonzero cohomology in degree one.

The proofs use these precise contracts:

| Dependency | Input needed in this lesson |
|---|---|
| SH02-NG-CONSTRUCTION, SH02-NG-CONE-SEQUENCES, SH02-NG-CONE-CONSEQUENCES | Deformation charts, the sequence criterion, closure invariance and finite-union behavior of normal cones |
| SH02-SP-BOUNDARY, SH02-SP-CONIC | The definition $\nu F=s^{-1}Rj_*r^{-1}F$, its boundedness, conicity, and the closed-support upper bound |
| SH02-SP-PROPER-GEOMETRY, SH02-SP-PROPER | Proper direct-image comparison with all three support and normal-cone conditions |
| SH02-SP-TENSOR | The unital, natural tensor comparison $\nu A\otimes^L\nu B\to\nu(A\otimes^L B)$ |
| SH02-CON-COMPARISON, SH02-CON-CYLINDER | Normalized transport for an arbitrary bounded conic complex and descent along an interval |
| SH02-MIC-DEFINITION | Microlocalization is the negative-pairing Fourier transform of specialization |
| SH02-MD-BOUNDED-HOM | Internal derived Hom of arbitrary bounded sheaves is bounded on a finite-dimensional manifold |
| SH02-IMP-OPEN-ZERO, SH02-IMP-LOCALIZATION | Exact open extension and the closed-support localization triangle |
| SH02-IMP-ADJUNCTION, SH02-IMP-RHOM, SH02-EX-EMBEDDING | Ordinary and supported adjunctions, tensor-Hom adjunction, and the identification of closed-support sections with internal Hom from the constant sheaf of that closed subset |
| SH02-IMP-PROPER-BASECHANGE | Ordinary base change for proper maps, applied on each closed support |
| SH02-MD-DIMENSION | Finite cohomological amplitude of ordinary direct image and closed-support sections on finite-dimensional manifolds |
| SH02-CA-INTERVAL | Ordinary cohomology of a constant sheaf with arbitrary coefficient module on a nonempty compact interval |

These are linked through [specialization](../../sheaf-proof-readings/SH02-specialization.html),
[normal geometry](../../sheaf-proof-readings/SH02-normal-geometry.html), [conic transport](../../sheaf-proof-readings/SH02-conic-descent.html),
[microlocalization](../../sheaf-proof-readings/SH02-microlocalization.html),
manifold duality,
open prerequisite contracts,
[exceptional adjunctions](../../sheaf-proof-readings/SH02-exceptional-operations.html), and
convex cohomology. The Hom bound is needed: boundedness
of the two arguments alone is not a formal reason for their derived Hom
to be bounded in an arbitrary sheaf category.

## SH02-SA-REMOVAL — Removing a closed set removes its normal cone

Let $S\subset X$ be closed, and put

$$
U=X\setminus S,\quad j_U:U\hookrightarrow X,
\qquad V=E\setminus C_M(S),\quad a:V\hookrightarrow E.
$$

There is a natural exact functor

$$
\nu^{\mathrm{away}\,S}:D^b(k_U)\longrightarrow D^b(k_V),
\qquad
\nu^{\mathrm{away}\,S}(G)=a^{-1}\nu(j_{U!}G),
\tag{SA1}
$$

and a natural isomorphism of functors on $D^b(k_X)$,

$$
\nu^{\mathrm{away}\,S}\,j_U^{-1}\simeq a^{-1}\nu.
\tag{SA2}
$$

The functor can equally be computed as $a^{-1}\nu Rj_{U*}$.

**Proof.** Open extension by zero is exact, so SA1 preserves boundedness;
specialization and inverse image also do so. Consider the open/closed
localization triangle, with $h:S\hookrightarrow X$,

$$
j_{U!}j_U^{-1}F\longrightarrow F\longrightarrow h_*h^{-1}F
\xrightarrow{+1}.
$$

The third object has closed support in $S$. Its specialization is therefore
supported in $C_M(S)$ by SH02-SP-CONIC. Apply $a^{-1}\nu$ to this triangle.
The third term vanishes, and its first arrow is the natural isomorphism
in SA2. This specifies the isomorphism by a restriction counit, without
choosing an extension of $j_U^{-1}F$ separately for each $F$.

The other localization triangle is

$$
R\Gamma_S F\longrightarrow F\longrightarrow Rj_{U*}j_U^{-1}F
\xrightarrow{+1}.
$$

Its first term is supported in $S$, so it gives the natural isomorphism
$a^{-1}\nu F\simeq a^{-1}\nu Rj_{U*}j_U^{-1}F$. The comparison
$j_{U!}G\to Rj_{U*}G$ restricts to the identity on $U$; its cone is supported
in $S$. Its specialization consequently becomes an isomorphism on $V$.
This identifies the two formulas for the functor and their comparison
maps. The direct-image boundedness here uses the finite-dimensional
manifold bound, not properness of $j_U$.

One can also express this construction as descent through a derived
quotient. Let $D^b_S(k_X)$ be the full subcategory of complexes supported
in $S$. Restriction kills exactly that subcategory, and $j_{U!}$ is an
exact section of restriction. The first localization triangle makes
$j_{U!}j_U^{-1}F\to F$ an isomorphism after quotienting by $D^b_S(k_X)$.
These facts prove the equivalence

$$
D^b(k_X)/D^b_S(k_X)\simeq D^b(k_U).
$$

Since $a^{-1}\nu$ kills $D^b_S(k_X)$, it descends through this quotient,
and the explicit representative of the descended functor is SA1.
This proves both the existence and the compatible restriction diagram.
$\square$

Directions over a removed point may remain. For instance, take
$X=\mathbb R$, $M=S=\{0\}$. Then $V$ is the punctured normal line.
The constant sheaf on the positive component of $U$ is sent to the
constant sheaf on the positive component of $V$. This follows from the
conic recovery theorem below applied to its open extension. Thus SA1
contains boundary-direction information even though $M\cap U$ is empty.

## SH02-SA-CONIC-BUNDLE — A homogeneous object already is its normal limit

Let $p:E\to Z$ be any finite-rank real vector bundle, and identify $Z$ with
its zero section. The normal bundle $N_ZE$ has the canonical identification
with $E$ given by the vertical tangent vector. For every
$F\in D^b_{\mathbb R_{>0}}(k_E)$ there are canonical natural isomorphisms

$$
\nu_Z F\simeq F,\qquad \mu_ZF\simeq F^\wedge.
\tag{SA3}
$$

The second identification is on $E^*$. Our convention is

$$
F^\wedge=Rq_!\left(\operatorname{pr}_E^{-1}F
\otimes^L k_{\{\langle v,\xi\rangle\le0\}}\right),
\qquad q:E\times_ZE^*\to E^*.
\tag{SA4}
$$

There is no orientation tensor, degree shift, or antipodal map in SA3.

**Proof.** The deformation along the zero section is globally
$E\times\mathbb R$, with projection to $E$ given by $(v,t)\mapsto tv$.
This follows directly from a bundle trivialization, and the formulas agree
on overlaps because the transition functions are fibrewise linear. The
central identification is the vertical-tangent identification just specified.

Write $b:E\times\mathbb R\to E$ for the first projection and
$j:E\times\mathbb R_{>0}\hookrightarrow E\times\mathbb R$ for the
positive inclusion. On the positive chamber, normalized conic transport
gives a natural isomorphism

$$
(bj)^{-1}F\xrightarrow{\ \theta_F\ }[(v,t)\mapsto tv]^{-1}F.
$$

It is normalized to the identity at $t=1$ by SH02-CON-COMPARISON.
Use it to identify the specialization with
$s^{-1}Rj_*j^{-1}b^{-1}F$. The open adjunction unit gives the natural map

$$
F=s^{-1}b^{-1}F\longrightarrow s^{-1}Rj_*j^{-1}b^{-1}F.
\tag{SA5}
$$

It is an isomorphism. Indeed, product neighborhoods of $(v,0)$ have positive
part $W\times(0,\epsilon)$, and interval descent identifies their derived
sections of $b^{-1}F$ with $R\Gamma(W;F)$. In each degree, the filtered
colimit over neighborhoods $W$ is $H^a(F)_v$. This last assertion is the
usual stalk computation using an injective resolution and exact filtered
colimits; it does not require acyclicity of $F$ on every neighborhood.
The unit in SA5 induces precisely these identifications. Thus it is an
isomorphism on all cohomology stalks. Invert it after using $\theta_F$ to
obtain the first isomorphism in SA3. Every map is global and natural, so
this argument covers a nontrivial bundle as well as a trivial one.

Microlocalization is defined as Fourier transformation after specialization.
Applying SA4 to the first isomorphism gives the second. The normal and
conormal identifications are $E$ and $E^*$ with their evaluation pairing;
no dualizing functor is inserted. This proves the absence of additional
twists or signs. Rank zero gives $\nu_ZF=\mu_ZF=F$ with the same unit map.
$\square$

## SH02-SA-CLOSED-SUPPORT — Closed subsets retain every normal direction

For a closed subset $A\subset X$, there is a natural morphism

$$
c_A:k_{C_M(A)}\longrightarrow\nu_M k_A.
\tag{SA6}
$$

If $k\ne0$, then

$$
\operatorname{supp}\nu_Mk_A=C_M(A).
\tag{SA7}
$$

In fact $H^0(\nu_Mk_A)_v$ contains a canonical copy of $k$ for every
$v\in C_M(A)$, supplied by SA6. Equality of supports does not say that
SA6 is an isomorphism.

**Construction of the map.** The constant unit in SH02-SP-TENSOR gives
$\nu_Mk_X\simeq k_E$. Specializing the restriction $k_X\to k_A$ gives
$k_E\to\nu_Mk_A$. The target is supported in the closed subset
$C=C_M(A)$. For its closed inclusion $h:C\hookrightarrow E$, the
adjunction with ordinary restriction identifies that target with
$h_*h^{-1}\nu_Mk_A$. The adjunction therefore uniquely factors the map
as $k_E\to k_C\xrightarrow{c_A}\nu_Mk_A$.

**Proof of the support statement.** Recall the deformation notation
$\nu_Mk_A=s^{-1}Rj_*r^{-1}k_A$. The subset $r^{-1}A$ is closed in the
positive chamber, and $r^{-1}k_A=k_{r^{-1}A}$. As the input is in degree
zero and both $s^{-1}$ and $r^{-1}$ are exact, the degree-zero stalk at
$v\in E$ is

$$
H^0(\nu_Mk_A)_v
=\varinjlim_{W\ni v}\Gamma(W\cap\Omega;k_{r^{-1}A}).
\tag{SA8}
$$

Here $W$ ranges over open deformation neighborhoods of $v$. Since
$r^{-1}A$ is closed in $\Omega$, the displayed sections are ordinary
sections of the constant sheaf on $W\cap r^{-1}A$. If $v\in C_M(A)$,
every such intersection is nonempty. A coefficient $a\in k$ determines
the constant section with value $a$ there. A nonzero $a$ remains nonzero
after every neighborhood restriction, because every smaller intersection
remains nonempty. Hence these constant sections give an injection
$k\hookrightarrow H^0(\nu_Mk_A)_v$. This is the stalk map induced by
the construction of $c_A$.

The support upper bound gives the opposite containment, so SA7 follows.
No local contractibility of $A$ is needed. Higher cohomology and additional
degree-zero sections are allowed. For the zero ring all these complexes
vanish; the support-equality assertion consequently requires the stated
$k\ne0$ qualification. $\square$

For a locally closed subset $S$, the universally valid conclusion from
the support theorem is

$$
\operatorname{supp}\nu_Mk_S
\subset C_M(\overline S)=C_M(S).
\tag{SA9}
$$

The proof of SA8 cannot be reused to prove equality: an open extension
inside $\overline S$ need not admit the constant section one across its
missing boundary. The next example shows that this is an actual failure,
even for a set given by polynomial inequalities.

## SH02-SA-COLLAPSING-STRIP — A nonempty cone with zero specialization

Assume $k\ne0$, let $X=\mathbb R^2$, and specialize at the origin. Set

$$
\begin{aligned}
D&=\{(x,y):x\ge0,\ 0\le y\le x^4\},\\
B&=\{(x,0):x\ge0\},\qquad S=D\setminus B,\\
L&=\{(u,0):u\ge0\}\subset T_0X.
\end{aligned}
\tag{SA10}
$$

The set $S=D\cap\{y>0\}$ is locally closed, its closure is $D$, and

$$
C_0(S)=C_0(D)=C_0(B)=L,
\qquad \nu_0k_S=0.
\tag{SA11}
$$

Thus SA9 can be a strict inclusion with its left side empty. This refutes
the unqualified equality for an arbitrary locally closed set; no published
erratum is being claimed here.

**The cone calculation.** Suppose $(x_n,y_n)\in D$ tends to zero,
$c_n>0$, and $(c_nx_n,c_ny_n)$ has a finite limit. Since $0\le y_n\le x_n^4$,

$$
0\le c_ny_n\le(c_nx_n)x_n^3\longrightarrow0.
$$

Its limiting first component is nonnegative, proving $C_0(D)\subset L$.
For $u>0$, take $x_n=u/n$, $y_n=x_n^4/2$, and $c_n=n$ to obtain
$(u,0)$ as a normal limit from $S$. For the zero vector use
$x_n=n^{-2}$, $y_n=x_n^4/2$, and $c_n=n$. Hence $L\subset C_0(S)$.
Inclusion and closure invariance prove the first two equalities in SA11;
the cone of the closed ray $B$ is $L$ directly.

**A proper-map calculation of the sheaf.** Let $\pi:X\to\mathbb R$
be $(x,y)\mapsto x$. It is proper on $D$: the inverse image in $D$ of
a compact subset of the line is closed and bounded. It is also proper
on $B$. The fibres in $D$ are empty for $x<0$ and the compact intervals
$[0,x^4]$ for $x\ge0$, including the one-point fibre at zero. The fibres
in $B$ are the corresponding endpoints $\{0\}$. Proper base change and
constant-coefficient interval cohomology therefore give

$$
R\pi_*k_D\longrightarrow R\pi_*k_B
\quad\text{an isomorphism}.
\tag{SA12}
$$

This is the actual map obtained by restricting from $D$ to $B$. At every
nonempty fibre it is evaluation of a constant section on a connected
interval at its endpoint, hence the identity of $k$ in degree zero; all
higher fibre groups vanish. On empty fibres both sides vanish. Equivalently,
both objects and the map identify with $k_{[0,\infty)}$ and its identity.
The open/closed triangle

$$
k_S\longrightarrow k_D\longrightarrow k_B\xrightarrow{+1}
$$

now gives $R\pi_*k_S=0$.

We must justify passing this calculation through specialization. Use the
map of pairs $(X,\{0\})\to(\mathbb R,\{0\})$. Its normal map is
$\pi_N:T_0X\to\mathbb R$, $(u,v)\mapsto u$. The three hypotheses of
SH02-SP-PROPER, for the closed support $D$ of $k_S$, are all satisfied:
$\pi|_D$ is proper as just proved; $\pi_N|_{C_0(D)}=\pi_N|_L$ is a
homeomorphism to a closed ray and is proper; and
$D\cap\pi^{-1}(0)=\{0\}$. The resulting comparison gives

$$
R\pi_{N*}\nu_0k_S\simeq\nu_0 R\pi_*k_S=0.
\tag{SA13}
$$

Finally, $K=\nu_0k_S$ is supported in $L$ by the support upper bound.
If $h:L\hookrightarrow T_0X$, then $K\simeq h_*h^{-1}K$. The composite
$\pi_Nh$ is a homeomorphism of $L$ onto the closed ray in the line,
followed by its closed inclusion. Its direct image is exact and fully
faithful. Thus $R\pi_{N*}K=0$ implies $K=0$. This proves SA11 in all
cohomological degrees. In particular, no interchange with an infinite
product, approximation by constructible inputs, or nonproper ordinary
base change occurs in this argument. $\square$

## SH02-SA-HOM-COMPARISON — Specializing an evaluation map

For arbitrary $F,G\in D^b(k_X)$, there is a natural morphism

$$
b_{G,F}:\nu_MR\mathcal Hom(G,F)
\longrightarrow R\mathcal Hom(\nu_MG,\nu_MF).
\tag{SA14}
$$

It is covariant in $F$ and contravariant in $G$.

**Construction and proof.** Set $A=R\mathcal Hom(G,F)$, which is bounded
by SH02-MD-BOUNDED-HOM. Apply the specialization tensor comparison to
$A,G$, followed by specialization of evaluation:

$$
\nu_MA\otimes^L\nu_MG
\longrightarrow\nu_M(A\otimes^LG)
\xrightarrow{\ \nu_M(\mathrm{ev})\ }\nu_MF.
\tag{SA15}
$$

Tensor-Hom adjunction turns this specified composite into SA14. The
boundedness theorem also bounds the target. Naturality follows from
naturality of evaluation and of the tensor comparison. The construction
does not exchange specialization with an internal Hom by an assumed
isomorphism, nor does it require $G$ to be perfect. The tensor symmetry
is the usual Koszul symmetry when factors are reordered; the displayed
order needs no reordering or extra sign. $\square$

## SH02-SA-SUPPORT-COMPARISON — Taking supported sections before a limit

For a closed subset $A\subset X$ and $F\in D^b(k_X)$, there is a natural
morphism

$$
d_{A,F}:\nu_MR\Gamma_A F
\longrightarrow R\Gamma_{C_M(A)}\nu_MF.
\tag{SA16}
$$

**Construction.** The support counit $R\Gamma_A F\to F$ specializes to
a map $K\to\nu_MF$, where $K=\nu_MR\Gamma_A F$. The complex
$R\Gamma_A F$ has closed support in $A$, so $K$ has closed support in
$C=C_M(A)$. The inclusion of the category of complexes supported in $C$
has right adjoint $R\Gamma_C$. Therefore

$$
\operatorname{Hom}(K,R\Gamma_C\nu_MF)
\simeq\operatorname{Hom}(K,\nu_MF).
$$

The map corresponding to the specialized support counit is SA16. This
defines a canonical morphism in the derived category and proves its
naturality. The boundedness of local cohomology and of the other operations
is covered by the explicit finite-dimensional bounds in the setup.

This map is also obtained by combining SA6 and SA14. For a closed subset,
the canonical identification
$R\mathcal Hom(k_A,F)=R\Gamma_A F$ follows from the adjunction for its
closed inclusion. Use it in the following composite:

$$
\begin{aligned}
\nu_MR\Gamma_A F
&\xrightarrow{b_{k_A,F}}
R\mathcal Hom(\nu_Mk_A,\nu_MF)\\
&\xrightarrow{c_A^*}
R\mathcal Hom(k_C,\nu_MF)
\simeq R\Gamma_C\nu_MF.
\end{aligned}
\tag{SA17}
$$

To check that this is the same map, compose it with the support counit
to $\nu_MF$. Under tensor-Hom adjunction, that composition is evaluation
after precomposition with $k_E\to k_C\to\nu_Mk_A$. By the construction
of $c_A$, the latter map is specialization of $k_X\to k_A$, with the
constant-unit identification. Naturality and the unit property of the
specialization tensor comparison reduce SA15 to specialization of
$R\mathcal Hom(k_A,F)\to R\mathcal Hom(k_X,F)=F$. This is precisely the
support counit used to define SA16. The supported adjunction then proves
equality of the two maps. $\square$

## SH02-SA-TANGENT-CIRCLES — A compact model retaining two approaching pieces

Let $X=\mathbb R^2$, $M=\{0\}$, and $k\ne0$. Consider the two circles

$$
P=\{x^2+(y-2)^2=4\},\qquad
Q=\{x^2+(y+3)^2=9\},
\qquad L=\{(u,0):u\in\mathbb R\}\subset T_0X.
\tag{SA18}
$$

They meet only at the origin. Indeed, their equations say
$x^2+y^2=4y=-6y$, forcing $x=y=0$. Each is a compact smooth curve with
tangent line $L$ at zero. The normal cones along the point are thus

$$
C_0(P)=C_0(Q)=C_0(P\cup Q)=L.
$$

There are natural identifications

$$
\nu_0k_P\simeq k_L,
\qquad \nu_0k_Q\simeq k_L,
\qquad \nu_0k_{\{0\}}\simeq k_{\{0\}}.
\tag{SA19}
$$

**Proof with the properness conditions.** For the inclusion of $P$ into
$X$, specialize the constant sheaf on the manifold $P$ along its point
zero. In a local coordinate at that point the constant sheaf specializes
to the constant sheaf on $T_0P$: the positive deformation chart is a
product and interval descent computes the limit. This is also the unit
case $\nu k_P=k_{T_0P}$ in the specialization tensor theorem. The original
inclusion is proper because $P$ is closed, its normal derivative is the
closed linear embedding $T_0P\hookrightarrow T_0X$ and is proper, and
the preimage of the target center is exactly the source center. The
proper comparison consequently identifies specialization of its closed
direct image with $k_L$. The argument for $Q$ is identical with its own
derivative. The point calculation uses the same theorem for the inclusion
of a point, or the supported-object computation in SH02-SP-ZERO.

In all three cases the identification is compatible with restriction to
the origin: it is built from the same units and restriction maps in the
proper comparison. Hence specializing $k_P\to k_{\{0\}}$ or
$k_Q\to k_{\{0\}}$ gives the usual $k_L\to k_{\{0\}}$.
No orientation shift occurs in SA19 because these are ordinary direct
images and constant-unit specialization. $\square$

## SH02-SA-CLOSED-MAP-FAILURE — One normal direction need not mean one section

Put $A=P\cup Q$ in the circle model. Its constant sheaf fits into the
short exact sequence

$$
0\longrightarrow k_A\longrightarrow k_P\oplus k_Q
\xrightarrow{\mathrm{res}_P-\mathrm{res}_Q}k_{\{0\}}
\longrightarrow0.
\tag{SA20}
$$

Exactness can be checked on stalks: off the intersection the surviving
summand is the identity, and at the origin the sequence is
$0\to k\xrightarrow{(1,1)}k^2\xrightarrow{(1,-1)}k\to0$.
Specialize this sequence and use SA19. It follows that $\nu_0k_A$ is a
sheaf in degree zero, with stalk

$$
(\nu_0k_A)_v\simeq
\begin{cases}
k^2,&v\in L\setminus\{0\},\\
k,&v=0,\\
0,&v\notin L.
\end{cases}
\tag{SA21}
$$

There is no additional cohomology: the difference map from $k_L^2$ to
$k_{\{0\}}$ is surjective on every stalk. Its kernel is the displayed
specialization sheaf. At a nonzero $v\in L$, the map

$$
c_A:k_L\longrightarrow\nu_0k_A
$$

has stalk $k\to k^2$, $a\mapsto(a,a)$. This follows by composing the
constant restriction map with the two restrictions in SA20, which both
send the constant value $a$ to $a$. Its cokernel is a copy of $k$, so it
is not an isomorphism for any nonzero $k$. At zero it is the identity.
Thus the full support equality SA7 holds while its natural coefficient
comparison fails. The normal cone records the common direction, whereas
the specialization retains two independent local sections away from zero.

## SH02-SA-HOM-AND-SUPPORT-FAILURE — Coincident directions enlarge both targets

Keep the same circles and take $G=k_P$, $F=k_Q$, and the closed support
set $A=P$. Then

$$
R\mathcal Hom(k_P,k_Q)=R\Gamma_Pk_Q
\simeq k_{\{0\}}[-1].
\tag{SA22}
$$

To verify the degree and coefficient, let $q:Q\hookrightarrow X$ and
$z:\{0\}\hookrightarrow Q$. Closed direct image identifies the support
functor with support in the intersection, so
$R\Gamma_Pk_Q=q_*R\Gamma_{\{0\}}k_Q$ with the constant sheaf on $Q$
understood on the right. The costalk of this constant sheaf at zero is
$z^!k_Q=k[-1]$, after orienting a local coordinate on $Q$ by increasing
$x$. Directly, a small interval in $Q$ is cut into two intervals by zero;
the localization map on constant sections is $k\to k\oplus k$,
$a\mapsto(a,a)$. Its kernel is zero and its cokernel is $k$, so the
supported cohomology is $k$ in degree one only. This also derives SA22
without suppressing the degree shift. A different orientation changes
the chosen generator, not the following nonisomorphism assertion.

By SA19 and exactness of specialization,

$$
\nu_0R\mathcal Hom(k_P,k_Q)
\simeq\nu_0R\Gamma_Pk_Q
\simeq k_{\{0\}}[-1].
\tag{SA23}
$$

The two comparison targets, however, are

$$
R\mathcal Hom(\nu_0k_P,\nu_0k_Q)
\simeq R\mathcal Hom(k_L,k_L)\simeq k_L,
\qquad
R\Gamma_{C_0(P)}\nu_0k_Q\simeq R\Gamma_Lk_L\simeq k_L.
\tag{SA24}
$$

For the Hom identification, closed adjunction reduces both arguments to
the constant sheaf on $L$, and the internal Hom from the tensor unit to
itself is $k_L$. For the support identification, $k_L$ already has support
in $L$, so the support counit is an isomorphism. At every nonzero point
of $L$, the source in SA23 has zero stalk and each target in SA24 has
stalk $k$. Thus both SA14 and SA16 fail to be isomorphisms. These are
failures for compact, smooth individual supports and bounded sheaves with
free rank-one coefficients; no pathological space or infinite family is
needed. The actual maps remain the adjunction morphisms constructed above.

## SH02-SA-PROBLEMS — Exercises with complete solutions

**Problem 1: independence of an extension.** Let $S\subset X$ be closed,
and suppose $F_1,F_2\in D^b(k_X)$ are joined by a morphism that becomes an
isomorphism on $X\setminus S$. Show that their specializations become
isomorphic on $E\setminus C_M(S)$. Explain why the specified morphism,
rather than just the two restricted objects, matters.

**Solution.** The cone of the morphism restricts to zero on $X\setminus S$,
so its cohomology sheaves have support in $S$. The specialization support
bound places the support of its specialization in $C_M(S)$. Apply
specialization to the triangle and then restrict to the complementary
open set. The cone vanishes there, so the specialized morphism is an
isomorphism. If only an isomorphism between the two restrictions is given,
SA1 applies functorially to that isomorphism and SA2 identifies the
result with the two restricted specializations. Without choosing such
an isomorphism, one obtains no preferred identification of the outputs.

**Problem 2: do the bundle identifications remember orientability?** Let
$E\to S^1$ be a nonorientable real line bundle and let $A$ be any bounded
complex of $k$-modules. Put $F=A_E$, the constant complex on the total
space. Determine $\nu_{S^1}F$, and specify $\mu_{S^1}F$ without choosing
an orientation of $E$.

**Solution.** The constant complex is conic, so SA3 gives
$\nu_{S^1}F=A_E$. The second output is the globally defined Fourier
transform in SA4, with $F=A_E$. This is a complete orientation-independent
specification of its canonical identification with $\mu_{S^1}F$: the
pairing $E\times_{S^1}E^*\to\mathbb R$ is intrinsic. If one subsequently
computes the Fourier transform of a fibrewise constant object as an object
on the zero section of the dual bundle, the usual orientation complex of
the fibre appears in that Fourier calculation. It is not an extra twist
in the equality between microlocalization and that transform. No
trivialization of the nonorientable line is needed for either statement.

**Problem 3: a coefficient module in the collapsing strip.** In SA10,
replace $k_S$ by $A_S$ for an arbitrary nonzero $k$-module $A$. Prove the
same vanishing of specialization without assuming $A$ flat or finite.

**Solution.** There is a short exact sequence
$0\to A_S\to A_D\to A_B\to0$, as its stalk sequences show. A constant
sheaf with coefficient $A$ on a compact interval has ordinary sections
$A$ and no positive cohomology; the constant-endpoint restriction is the
identity of $A$. Proper base change therefore makes
$R\pi_*A_D\to R\pi_*A_B$ an isomorphism, giving $R\pi_*A_S=0$.
The closed support of $A_S$ is $D$, and the three proper-specialization
conditions are exactly the geometric conditions checked after SA12.
Consequently $R\pi_{N*}\nu_0A_S=0$, and the same fully faithful closed-ray
argument gives $\nu_0A_S=0$. This proof uses no derived tensoring with a
nonflat module and no finite-generation assertion.

**Problem 4: locate the two different failures.** In the circle model,
compare the stalks at zero and at a nonzero $v\in L$ of SA6 for $A=P\cup Q$
and of SA16 for $A=P$, $F=k_Q$.

**Solution.** For SA6 the source and target at zero are both $k$, and the
map is the identity; at $v\ne0$ it is the diagonal $k\to k^2$. For SA16
the zero-stalk source is $k[-1]$ and the zero-stalk target is $k$; they
have nonzero cohomology in different degrees. At $v\ne0$ its source is
zero and its target is $k$. Thus the first comparison fails through extra
independent sections in a shared direction, while the second fails
through local cohomology concentrated before specialization at the
intersection point. Both calculations distinguish a closed support from
the subset of directions where a particular degree has a nonzero stalk.

## SH02-SA-BOUNDARY — Statements proved and the remaining audit boundary

Removal has a functorial quotient construction, and conic recovery holds
on arbitrary vector bundles with all bounded coefficient complexes allowed.
The three comparison maps are defined by their units, tensor evaluation,
and supported adjunction, with their compatibility verified. The compact
circle model gives an explicit failure for each comparison. For set
coefficients, equality of normal cone and specialization support is proved
for closed subsets and nonzero coefficients. For arbitrary locally closed
subsets only SA9 holds in general, as the fully computed strip example
demonstrates. That discrepancy remains visible in the source correspondence;
it is not silently counted as a proof of the stronger assertion.

These results suggest two concrete further questions. One can seek geometric
conditions on a locally closed subset that exclude the half-open collapsing
fibres of SA10 and restore support equality. One can also seek hypotheses
on two sheaves that make their tensor evaluation commute with the normal
limit, thereby turning SA14 into an isomorphism. Neither property follows
from the boundedness or compactness conditions used in this lesson.

All proofs remain relative to the exact prerequisite contracts above.
