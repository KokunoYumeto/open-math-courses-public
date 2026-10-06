# SH02-CHE-UNIT — Cotangent directions that survive a limiting operation

The bounded-complex results below have complete deductions from the explicit prerequisite contracts. The full bounded-below input range for the final tensor and Hom estimates is proved by the unbounded supplement linked in SH02-CHE-RANGE, relative to its named prerequisites.

The checked readable antecedent is Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorem 5.1.4, Theorems 5.2.1–5.2.2, Proposition 5.3.2 and Remark 5.3.3, with the graph Hom construction of §5.5. These are the actual specialization, Fourier, inverse-image, asymptotic tensor/Hom and graph-recovery mechanisms used here. The independent deductions below retain their maps, antipodes, orientation shifts and weighted escape conditions. Original expression is dedicated under CC0 1.0 Universal.

A restriction can create a singularity even when the covectors directly above the restricted submanifold do not predict it. Nearby covectors can become arbitrarily large while their tangential components remain finite. Normal deformation records this process. Applying the same construction to a graph gives inverse-image estimates, and applying it to a diagonal gives tensor and Hom estimates.

## SH02-CHE-SETUP — Categories, maps, and the proof dependencies

Let $k$ be a commutative ring of finite global dimension. All manifolds are finite dimensional, Hausdorff, and countable at infinity; maps are smooth. The real analytic case is included. Unless a different range is expressly discussed, complexes belong to $D^b(k_X)$. Their cohomology sheaves can be arbitrary. We assume neither a field of coefficients nor constructibility, perfect stalks, compact support, or orientability.

For $f:Y\to X$ write

$$
E_f=Y\times_XT^*X,\qquad
f_\pi(y,\xi)=(f(y),\xi),\qquad
f_d(y,\xi)=(y,df_y^t\xi),\qquad
q:E_f\to Y.
$$

The graph lies in $X\times Y$, in that order. Its conormal is identified with $E_f$ by $(y,\xi)\mapsto(f(y),y;\xi,-df_y^t\xi)$. The relative orientation complex is

$$
\omega_f=\omega_Y\otimes f^{-1}\omega_X^{\otimes-1},
\qquad \omega_X=\operatorname{or}_X[\dim X].
$$

The comparison $\vartheta_f:f^{-1}F\otimes\omega_f\to f^!F$ is the mate of the relative trace under $Rf_!\dashv f^!$. This fixes its direction and normalization. A morphism is a microlocal isomorphism on $V$ if the microsupport of its cone misses $V$.

Here is the exact dependency package used in the proofs.

| Contract | Required statement |
|---|---|
| SH02-MST-TEST and SH02-MST-EQUIVALENCE | The support-test definition of microsupport and its equivalent cone tests for bounded complexes; the triangle inequality; invariance under tensoring with an invertible locally constant complex. |
| SH02-AE-GRAPH, SH02-AE-SEQUENCES, SH02-AE-SUM, SH02-AE-NONCHAR | The normal-cone definitions and coordinate sequence descriptions of the operations recalled below, including their closedness and coordinate invariance in the smooth category. |
| SH02-AE-BOUNDARY | If $j:W\setminus M\hookrightarrow W$ is the complement of a closed submanifold, then $\operatorname{SS}(i^{-1}Rj_*K)\subset T^*M\cap C_{T^*_M W}(\operatorname{SS}(K))$ for bounded $K$. A sheaf on one open chamber is first extended by zero within $W\setminus M$. |
| SH02-MO-EXTERNAL-TENSOR and SH02-MO-EXTERNAL-HOM | $\operatorname{SS}(F\boxtimes^LG)\subset\operatorname{SS}(F)\times\operatorname{SS}(G)$ and $\operatorname{SS}(R\mathcal Hom(q_Y^{-1}G,q_X^!F))\subset\operatorname{SS}(F)\times\operatorname{SS}(G)^a$ for bounded inputs. The smooth inverse-image equality is also used. |
| SH02-MO-CONIC-PUSH | For a bounded conic $H$ on a vector bundle $\pi:E\to Y$, both $\operatorname{SS}(R\pi_*H)$ and $\operatorname{SS}(R\pi_!H)$ lie in $T^*Y\cap\operatorname{SS}(H)$; for the punctured projection, $\operatorname{SS}(R\dot\pi_*H)\subset\dot\pi_\pi\dot\pi_d^{-1}\operatorname{SS}(H)$. Here $T^*Y$ is inserted at the zero section with zero vertical cotangent component. The source theorem uses the biconicity of $\operatorname{SS}(H)$. |
| SH02-MO-FS-SS | For bounded conic $L$ on a vector bundle, the canonical map $(v,z;\alpha,\beta)\mapsto(\alpha,z;-v,\beta)$ takes $\operatorname{SS}(L)$ onto $\operatorname{SS}(L^\wedge)$. |
| SH02-SP-CONIC and SH02-MIC-DEFINITION | Bounded conic specialization $\nu_MF=s^{-1}Rj_*p_+^{-1}F$ and $\mu_MF=(\nu_MF)^\wedge$. |
| SH02-MH-HOM and SH02-MH-HOM-RECOVERY | The two graph Hom constructions, their ordinary and proper-support recoveries, and identification of the map between the recoveries with the canonical evaluation/trace map. Compact Hom recovery requires cohomological constructibility of the indicated first Hom input. |
| SH02-MIC-ZERO, SH02-MH-RECOVERY | The Sato recovery triangle with the explicitly trace-normalized compact recovery. REC8 compares the zero-cone FS14 map with original R4, REC18–REC19 prove equality of the recovery arrow and the relative trace, and the graph argument identifies it with $\vartheta_f$. These statements are used here without proof. |

The constructions are developed in normal geometry, specialization, microlocalization, microlocal Hom, and the [asymptotic cotangent estimates](asymptotic-estimates.md). The precise meaning of cohomological constructibility is the compatible local-system and perfectness condition in cohomological biduality, not an implicit condition on every sheaf in this lesson.

## SH02-CHE-OPERATIONS — Finite limits and escape directions

Let $A\subset T^*X$ and $B\subset T^*Y$ be closed conic sets. Their graph normal cone is

$$
C_f(A,B)=C_{T^*_{\Gamma_f}(X\times Y)}(A\times B^a),
\tag{CHE1}
$$

viewed as a subset of $T^*E_f$ through the normal-cone and Fourier identifications. This is the operation denoted $C_\mu$ in the asymptotic-estimates lesson. For a vector-bundle projection $q:E_f\to Y$, let $q_\pi:E_f\times_YT^*Y\to T^*Y$ be projection and $q_d:E_f\times_YT^*Y\to T^*E_f$ the transpose differential. Define

$$
f^\#(A,B)=q_\pi q_d^{-1}C_f(A,B),
\qquad
f^\#_\infty(A,B)=\dot q_\pi\dot q_d^{-1}C_f(A,B).
\tag{CHE2}
$$

Dots remove the zero section of $E_f$. The biconic normal-cone geometry also identifies the first set with $T^*Y\cap C_f(A,B)$. Put $f^\#A=f^\#(A,T^*_YY)$ and similarly for $f^\#_\infty A$.

In local coordinates, $(y_0;\eta_0)$ belongs to $f^\#(A,B)$ precisely when there are $(x_n;\xi_n)\in A$ and $(y_n;\eta_n)\in B$ with

$$
y_n\to y_0,\quad x_n\to f(y_0),\quad
df_{y_n}^t\xi_n-\eta_n\to\eta_0,\quad
|x_n-f(y_n)|\,|\xi_n|\to0.
\tag{CHE3}
$$

For $f^\#_\infty(A,B)$ require in addition $|\xi_n|\to\infty$. The norm can be any coordinate norm. The last condition controls the error from replacing a nearby point by a point on the graph. It must not be omitted.

For $A,B\subset T^*X$ put

$$
A\widehat+ B=(1_X)^\#(A,B^a),\qquad
A\widehat+_\infty B=(1_X)^\#_\infty(A,B^a).
\tag{CHE4}
$$

Thus the sum uses $\xi_n+\eta_n$, and permits different base points whose distance multiplied by $|\xi_n|$ tends to zero. Ordinary fibrewise addition uses the same base point and finite covectors. For closed conic $A$,

$$
f^\#A=f_df_\pi^{-1}A\ \cup\ f^\#_\infty A.
\tag{CHE5}
$$

Indeed, a sequence in (CHE3) with $B$ the zero section has either a bounded subsequence of $\xi_n$, producing the ordinary image by closedness, or a subsequence with norm tending to infinity. Conversely constant sequences give every point of the ordinary image. The same argument gives $A\widehat+B=(A+B)\cup(A\widehat+_\infty B)$.

We say $f$ is **noncharacteristic for $A$ on $V\subset T^*Y$** when

$$
f^\#_\infty A\cap V=\varnothing.
\tag{CHE6}
$$

The condition makes sense for an arbitrary subset $V$, not just an open or conic subset. It is a condition on escape directions over nearby points, and is stronger than properness of the ordinary cotangent correspondence over an open $V$.

## SH02-CHE-001 — What specialization can contribute

Let $M\hookrightarrow X$ be a closed submanifold and $F\in D^b(k_X)$. There are canonical identifications

$$
T^*N_MX\ \simeq\ T^*N_M^*X\ \simeq\ N_{N_M^*X}(T^*X).
\tag{CHE7}
$$

Under these identifications,

$$
\operatorname{SS}(\nu_MF)
\subset C_{N_M^*X}(\operatorname{SS}(F)),
\qquad
\operatorname{SS}(\mu_MF)=\operatorname{SS}(\nu_MF).
\tag{CHE8}
$$

The equality means transport by (CHE7), not literal equality of subsets of two different cotangent bundles.

**Proof.** Use adapted coordinates $(u,z)$ with $M=\{u=0\}$. The deformation has coordinates $(v,z,t)$ and $p(v,z,t)=(tv,z)$. Its central fibre is $N_MX$, and $p_+$ is a submersion on $t>0$. Write $(\alpha,\beta,\tau)$ for the covectors dual to $(v,z,t)$. The transpose differential gives

$$
(\alpha,\beta,\tau)
=(t\xi,\zeta,\langle v,\xi\rangle).
\tag{CHE9}
$$

Hence every point of $\operatorname{SS}(p_+^{-1}F)$ has

$$
(tv,z;t^{-1}\alpha,\beta)\in\operatorname{SS}(F),
\qquad t\tau=\langle v,\alpha\rangle.
\tag{CHE10}
$$

Apply the boundary contract to $s^{-1}Rj_*p_+^{-1}F$. If $(v_0,z_0;\alpha_0,\beta_0)$ belongs to its microsupport, that contract and the normal-cone sequence criterion yield points satisfying (CHE10) with

$$
t_n>0,\quad t_n\to0,\quad
(v_n,z_n;\alpha_n,\beta_n)\to(v_0,z_0;\alpha_0,\beta_0),
\qquad t_n|\tau_n|\to0.
\tag{CHE11}
$$

This use of the boundary theorem is legitimate even though only the positive chamber occurs: extend the sheaf by zero to the other component of the complement of $t=0$. No point from the empty negative component can enter the sequence.

Conicity allows multiplication of the covector in (CHE10) by $t_n$, so

$$
(t_nv_n,z_n;\alpha_n,t_n\beta_n)\in\operatorname{SS}(F).
\tag{CHE12}
$$

The conormal bundle $N_M^*X$ consists of $(0,z;\alpha,0)$. Relative to the point $(0,z_n;\alpha_n,0)$ on this bundle, the normal displacement of (CHE12), divided by $t_n$, is $(v_n,\beta_n)$. Its base tends to $(z_0,\alpha_0)$. This is exactly membership in the normal cone on the right of (CHE8).

For clarity, the identifications in these coordinates are

$$
(v,z;\alpha,\beta)
\longleftrightarrow(\alpha,z;-v,\beta)
\longleftrightarrow
\bigl((0,z;\alpha,0);\,v,\beta\bigr).
\tag{CHE13}
$$

The minus sign is in the cotangent component dual to the conormal-fibre coordinate. The second assertion of (CHE8) is now the Fourier microsupport transport theorem applied to the bounded conic object $\nu_MF$. This finishes both deductions. The construction is local, so a locally closed submanifold is handled in an open ambient neighborhood where it is closed. $\square$

There is useful extra information in the argument. Equations (CHE10)–(CHE11) imply $\langle v_0,\alpha_0\rangle=0$. Thus the microsupport of the specialized object annihilates the radial vector field of $N_MX$. This agrees with conicity and also checks that the positive deformation parameter did not introduce a spurious radial covector.

## SH02-CHE-002 — A single triangle controls a comparison defect

Let $H$ be a bounded conic sheaf on a vector bundle $q:E\to Y$. Let $C\subset T^*E$ be a closed biconic set containing $\operatorname{SS}(H)$. Write $a:Y\hookrightarrow E$ for the zero section and $j:\dot E\hookrightarrow E$ for its complement. Then

$$
Rq_!H\longrightarrow Rq_*H\longrightarrow
R\dot q_*(H|_{\dot E})\xrightarrow{+1}
\tag{CHE14}
$$

is the conic recovery triangle, and

$$
\begin{aligned}
\operatorname{SS}(Rq_!H),\ \operatorname{SS}(Rq_*H)
&\subset T^*Y\cap C,\\
\operatorname{SS}\bigl(\operatorname{Cone}(Rq_!H\to Rq_*H)\bigr)
&\subset\dot q_\pi\dot q_d^{-1}C.
\end{aligned}
\tag{CHE15}
$$

**Proof.** Apply $Rq_*$ to $a_*a^!H\to H\to Rj_*j^{-1}H\xrightarrow{+1}$. The left term is $a^!H$, which the proper conic contraction identifies with $Rq_!H$. Under this identification the map is the canonical comparison from proper to ordinary direct image. Composition of ordinary direct images identifies the third term with $R\dot q_*j^{-1}H$. This proves (CHE14) with its map, not merely with the three objects. Apply the full and punctured conic projection estimates to the three terms and enlarge $\operatorname{SS}(H)$ to $C$. These are precisely the inclusions in (CHE15). $\square$

Consequently the comparison is a microlocal isomorphism wherever the punctured image of $C$ is absent. There is no claim that $q$ is proper: the punctured term measures what ordinary direct image retains in the noncompact radial direction.

## SH02-CHE-003 — Hom along a graph

For $F\in D^b(k_X)$ and $G\in D^b(k_Y)$, set $A=\operatorname{SS}(F)$ and $B=\operatorname{SS}(G)$. With $p:X\times Y\to X$, $r:X\times Y\to Y$, define

$$
\begin{aligned}
\mathcal H_f^+(G,F)&=\mu_{\Gamma_f}
 R\mathcal Hom(r^{-1}G,p^!F),\\
\mathcal H_f^-(F,G)&=a_E^{-1}\mu_{\Gamma_f}
 R\mathcal Hom(p^{-1}F,r^!G),
\end{aligned}
\tag{CHE16}
$$

where $a_E(y,\xi)=(y,-\xi)$. These are sheaves on $E_f$. Let $b:T^*E_f\to T^*E_f$ be the **cotangent-fibre** antipodal map, $b(e;\theta)=(e;-\theta)$. Then

$$
\operatorname{SS}(\mathcal H_f^+(G,F))\subset C_f(A,B),
\qquad
\operatorname{SS}(\mathcal H_f^-(F,G))\subset b(C_f(A,B)).
\tag{CHE17}
$$

If $G$ is cohomologically constructible, the natural map

$$
D'_YG\otimes f^{-1}F\otimes\omega_f
\longrightarrow R\mathcal Hom(G,f^!F)
\tag{CHE18}
$$

is a microlocal isomorphism on $T^*Y\setminus f^\#_\infty(A,B)$.

**Proof.** The external Hom estimate puts the microsupport of the first kernel in $A\times B^a$. Apply SH02-CHE-001 with submanifold $\Gamma_f$ to obtain the first inclusion. The second kernel instead has microsupport in $A^a\times B$. This is the image of $A\times B^a$ under the antipodal map of $T^*(X\times Y)$. Its induced map on the normal-cone cotangent model is the cotangent lift of $a_E$, followed by $b$. One can verify this in (CHE13): negating an ambient covector negates $\alpha$ and $\beta$, keeps $v$ unchanged, and therefore sends $(\alpha,z;-v,\beta)$ to $(-\alpha,z;-v,-\beta)$. The cotangent lift of $a_E$ alone would send it to $(-\alpha,z;v,\beta)$; the additional map $b$ supplies the two remaining signs. Pullback by $a_E$ in (CHE16) cancels that cotangent lift, leaving $b(C_f(A,B))$. The maps $a_E$ and $b$ must not be conflated.

For the comparison, apply SH02-CHE-002 to $H=\mathcal H_f^+(G,F)$ and $C=C_f(A,B)$. Graph Hom recovery identifies the middle term with $R\mathcal Hom(G,f^!F)$. Under the additional constructibility assumption, it identifies the first term with the left side of (CHE18). The recovery contract identifies the arrow with evaluation followed by $\vartheta_f$ inside Hom. The cone bound in (CHE15) is, by definition, $f^\#_\infty(A,B)$. Its absence gives the asserted microlocal isomorphism. $\square$

## SH02-CHE-004 — The microsupport of microlocal Hom

For bounded $F,G$ on $X$, identify the diagonal conormal with $T^*X$ using the first covector. Then

$$
\operatorname{SS}(\mu hom(G,F))
\subset C(\operatorname{SS}(F),\operatorname{SS}(G))
\subset T^*T^*X.
\tag{CHE19}
$$

Here $C(A,B)$ is the normal cone of the pair of subsets of $T^*X$, with the canonical symplectic identification; equivalently it is $C_{1_X}(A,B)$ from (CHE1). This convention is the one used by the involutivity argument.

If $G$ is cohomologically constructible, the evaluation map

$$
D'_XG\otimes F\longrightarrow R\mathcal Hom(G,F)
\tag{CHE20}
$$

is a microlocal isomorphism on

$$
T^*X\setminus
\bigl(\operatorname{SS}(F)\widehat+_\infty
                  \operatorname{SS}(G)^a\bigr).
\tag{CHE21}
$$

**Proof.** Set $f=1_X$ in SH02-CHE-003. Its relative orientation is canonically $k_X$ with shift zero. Equation (CHE4) identifies the exceptional set, and the first kernel in (CHE16) is the definition of $\mu hom(G,F)$. No constructibility was used for (CHE19); it enters only to identify the first term of the comparison triangle. $\square$

## SH02-CHE-005 — Ordinary and exceptional inverse image

For every smooth $f:Y\to X$ and bounded $F$,

$$
\operatorname{SS}(f^{-1}F)\subset f^\#\operatorname{SS}(F),
\qquad
\operatorname{SS}(f^!F)\subset f^\#\operatorname{SS}(F).
\tag{CHE22}
$$

The cone of the canonical map has the stronger estimate

$$
\operatorname{SS}\bigl(\operatorname{Cone}(\vartheta_f)\bigr)
\subset f^\#_\infty\operatorname{SS}(F).
\tag{CHE23}
$$

Thus, if $f$ is noncharacteristic for $F$ on $V\subset T^*Y$, then $\vartheta_f$ is a microlocal isomorphism on $V$ and

$$
\operatorname{SS}(f^{-1}F)\cap V
\subset f_df_\pi^{-1}\operatorname{SS}(F).
\tag{CHE24}
$$

The same refined inclusion holds for $f^!F$ on $V$, since the two objects agree there up to the invertible orientation complex.

**Proof.** Apply microlocalization along the graph to $K=F\boxtimes\omega_Y$ and put $H=\mu_{\Gamma_f}K$. The external tensor estimate gives $\operatorname{SS}(K)\subset A\times T^*_YY$, where $A=\operatorname{SS}(F)$. SH02-CHE-001 then gives $\operatorname{SS}(H)\subset C_f(A,T^*_YY)$. The graph recovery identifications are

$$
Rq_!H\simeq f^{-1}F\otimes\omega_f,
\qquad Rq_*H\simeq f^!F.
\tag{CHE25}
$$

Their orientation cancellation can be checked before using them: restriction of $F\boxtimes\omega_Y$ to the graph is $f^{-1}F\otimes\omega_Y$, while the graph relative dualizing complex is $f^{-1}\omega_X^{\otimes-1}$. Their tensor product is precisely the first term of (CHE25). For the other term, $F\boxtimes\omega_Y=p^!F$ and exceptional composition gives $i_\Gamma^!p^!F=f^!F$. Use the trace-normalized compact recovery REC16, whose parity factor for this graph is $(-1)^{\dim X}$. REC18–REC19 identify the recovery arrow with the trace for the graph embedding. The graph argument following REC20 then identifies its composite with the smooth trace for $p$ with $\vartheta_f$: both exceptional adjuncts are projection formula followed by the graph counit and then the projection counit, exactly the composite counit for $f=p i_\Gamma$. This proves the map identity under the particular identifications in (CHE25), including their orientation permutations. The separate graph-Hom contracts used in (CHE18) and (CHE20) retain their own constructibility and proof obligations.

Apply (CHE15). The full projection image is $f^\#A$ and the punctured image is $f^\#_\infty A$, proving (CHE22) and (CHE23); tensoring with $\omega_f$ does not change microsupport. Finally remove the escape part in (CHE5) on $V$ to obtain (CHE24). $\square$

## SH02-CHE-PROPER — What the local hypothesis implies about properness

Suppose $A\subset T^*X$ is closed conic, $V\subset T^*Y$ is open, and $f^\#_\infty A\cap V=\varnothing$. Then

$$
f_d:f_\pi^{-1}A\cap f_d^{-1}V\longrightarrow V
\tag{CHE26}
$$

is proper.

**Proof.** Fix compact $K\subset V$ and consider a sequence $(y_n,\xi_n)$ in the inverse image of $K$. The points $y_n$ have a convergent subsequence, because they lie over the compact projection of $K$. A finite collection of bundle charts over that compact set reduces compactness to a bound on $|\xi_n|$. If no bound existed, pass to a subsequence on which the norms tend to infinity and $f_d(y_n,\xi_n)$ converges to a point of $K$. In (CHE3) take $x_n=f(y_n)$ and take the zero covector as the second input. The distance error is identically zero. This produces a point of $f^\#_\infty A\cap K$, a contradiction. The fibre coordinates are therefore bounded. The inverse image of $K$ is closed, since $A$ and $K$ are closed, so it is compact in a finite bundle-chart cover. This is properness. $\square$

The converse fails. SH02-CHE-EXAMPLES computes a case where (CHE26) has empty domain, hence is proper, but a tangential singularity is created by inverse image.

## SH02-CHE-DIAGONAL — Why a diagonal produces the asymptotic sum

Let $A,B\subset T^*X$ be closed conic and let $\delta:X\to X\times X$ be the diagonal. Then

$$
\delta^\#(A\times B)=A\widehat+B.
\tag{CHE27}
$$

**Proof.** The sequence criterion for the left side uses points $x_n,y_n,z_n\to x_0$ and covectors $(\xi_n,\eta_n)$ with

$$
\xi_n+\eta_n\to\zeta_0,
\qquad
\bigl|(x_n-z_n,y_n-z_n)\bigr|
\bigl|(\xi_n,\eta_n)\bigr|\to0.
\tag{CHE28}
$$

The triangle inequality gives $|x_n-y_n|\,|\xi_n|\to0$, so (CHE28) implies membership in the right side. Conversely suppose the asymptotic-sum criterion holds. Set $z_n=y_n$. Boundedness of $\xi_n+\eta_n$ gives $|\eta_n|\leq|\xi_n|+C$; therefore

$$
|x_n-y_n|\bigl|(\xi_n,\eta_n)\bigr|
\leq C'|x_n-y_n|(|\xi_n|+1)\to0.
$$

This is (CHE28). The argument uses neither compactness of the entire conic sets nor boundedness of the individual covectors. $\square$

## SH02-CHE-006 — Tensor and internal Hom without a transversality assumption

For $F,G\in D^b(k_X)$,

$$
\begin{aligned}
\operatorname{SS}(F\otimes^LG)
&\subset \operatorname{SS}(F)\widehat+\operatorname{SS}(G),\\
\operatorname{SS}(R\mathcal Hom(G,F))
&\subset \operatorname{SS}(F)\widehat+\operatorname{SS}(G)^a.
\end{aligned}
\tag{CHE29}
$$

There is no constructibility assumption in either estimate.

**Proof.** The exact inverse image of the diagonal gives $F\otimes^LG=\delta^{-1}(F\boxtimes^LG)$. Apply the external tensor bound, then (CHE22), then (CHE27). All three operations on conic sets are monotone, so enlarging the external microsupport preserves the inclusion.

For Hom use

$$
R\mathcal Hom(G,F)
\simeq\delta^!R\mathcal Hom(q_2^{-1}G,q_1^!F).
\tag{CHE30}
$$

This is exceptional inverse-image adjunction for internal Hom: $\delta^{-1}q_2^{-1}G=G$ and $\delta^!q_1^!F=F$ by composition. The external Hom bound places the kernel microsupport in $\operatorname{SS}(F)\times\operatorname{SS}(G)^a$. Apply the exceptional part of (CHE22), followed by (CHE27). This proves the second inclusion without replacing internal Hom by a tensor with a dual. $\square$

When the escape term is empty, (CHE5) recovers the usual estimate with ordinary fibrewise addition. In general that replacement is false, even for constant sheaves on smooth closed submanifolds.

## SH02-CHE-EXAMPLES — Tangency, escape, and a comparison that fails

Assume $k\ne0$. On $X=\mathbb R^2$ use coordinates $(s,t)$, with covectors $(\sigma,\tau)$. Let $Y=\{t=0\}$ and $Z=\{t=s^4\}$. Both are closed smooth submanifolds. Their constant sheaves, extended by zero to $X$, have conormal microsupports:

$$
\begin{aligned}
\operatorname{SS}(k_Y)&=\{(s,0;0,\lambda)\},\\
\operatorname{SS}(k_Z)&=\{(s,s^4;-4s^3\lambda,\lambda)\}.
\end{aligned}
\tag{CHE31}
$$

These equalities include zero covectors. They follow from the closed-embedding microsupport equality applied to a constant sheaf; alternatively adapted coordinates reduce the support tests to those for a point in the normal line.

First let $f:Y\hookrightarrow X$ and $F=k_Z$. Direct restriction gives $f^{-1}F=k_{\{0\}}$ on $Y$. Above $Y$, the conormal of $Z$ meets the correspondence only at $s=0$, and every such covector has tangential component zero. Thus the ordinary cotangent image misses $V=\{(s;\sigma):\sigma>0\}$. Its inverse-image map over $V$ has empty domain and is proper. But $\operatorname{SS}(f^{-1}F)$ contains every covector above $0$, including those in $V$.

The missing directions occur in $f^\#_\infty\operatorname{SS}(F)$. Given $c\ne0$, take $s_n>0$ with $s_n\to0$ and set $\lambda_n=-c/(4s_n^3)$. The source point and graph point are $(s_n,s_n^4)$ and $(s_n,0)$; the tangential covector is exactly $c$. Moreover

$$
s_n^4\,|(-4s_n^3\lambda_n,\lambda_n)|\to0,
\qquad |(-4s_n^3\lambda_n,\lambda_n)|\to\infty.
\tag{CHE32}
$$

This verifies every condition, including the weighted error, instead of inferring escape from a drawing.

Second, $k_Y\otimes^Lk_Z=k_{\{(0,0)\}}$. Stalkwise there is no higher Tor: the nonzero stalk modules of each factor are $k$. Its microsupport at the origin is all of $T^*_0X$. The ordinary sum of the two conormal bundles at their common point consists only of $(0,\tau)$. To obtain a missing vector $(c,d)$ asymptotically, use the point $(s_n,0)$ of $Y$ with covector $(0,d-\lambda_n)$ and the point $(s_n,s_n^4)$ of $Z$ with covector $(-4s_n^3\lambda_n,\lambda_n)$. Their sum is $(c,d)$ and the weighted base-point error tends to zero by (CHE32). Thus the asymptotic estimate records precisely the tangential directions absent from the ordinary sum.

Finally consider the closed line $Y\subset\mathbb R^2$ and $F=G=k_Y$. This $G$ is cohomologically constructible. The closed-submanifold duality calculation gives

$$
D'_Xk_Y\otimes k_Y\simeq k_Y[-1],
\qquad R\mathcal Hom(k_Y,k_Y)\simeq k_Y.
\tag{CHE33}
$$

Hence (CHE20) cannot be an isomorphism above $Y$. The shift is essential. More explicitly, $\operatorname{Hom}(k_Y[-1],k_Y)=H^1(Y;k)=0$ by closed-embedding adjunction and contractibility of the line. The comparison is zero, so its cone is the direct sum of two copies of $k_Y$. Its microsupport is $N_Y^*X$. The escape set contains this conormal bundle, since two conormal covectors may diverge while their difference remains any prescribed finite conormal covector. Constructibility licenses the tensor description of the first term; it does not eliminate the characteristic obstruction.

## SH02-CHE-PROBLEMS — Solved checks on the hypotheses

**Problem 1.** Let $f:Y\to X$ be a submersion. Show that $f^\#_\infty A$ is empty for every closed conic $A\subset T^*X$, and identify $f^\#A$.

**Solution.** Near a fixed point of $Y$, $df_y^t$ is injective and has a uniform lower norm bound $|df_y^t\xi|\geq c|\xi|$ after shrinking to a relatively compact coordinate neighborhood. In (CHE3), with zero second covector, convergence of $df_{y_n}^t\xi_n$ therefore bounds $|\xi_n|$. No escape sequence exists. Equation (CHE5) gives $f^\#A=f_df_\pi^{-1}A$. Consequently (CHE23) says the orientation comparison is an isomorphism everywhere; this agrees with the submersion formula $f^!F\simeq f^{-1}F\otimes\omega_f$.

**Problem 2.** Suppose $A,B$ are closed conic subsets of $T^*X$ with $A\cap B^a$ contained in the zero section. Prove $A\widehat+_\infty B=\varnothing$.

**Solution.** An escape sequence would have $\xi_n+\eta_n$ bounded and $|\xi_n|\to\infty$. Pass to a subsequence for which $\xi_n/|\xi_n|\to\xi_0$ of norm one. Then $\eta_n/|\xi_n|\to-\xi_0$. Conicity and closedness give $(x_0;\xi_0)\in A$ and $(x_0;-\xi_0)\in B$, contradicting the hypothesis. Thus the first estimate of (CHE29) reduces to ordinary addition in the usual noncharacteristic tensor situation. Replacing $B$ by $B^a$ gives the corresponding Hom condition $A\cap B\subset T^*_XX$.

**Problem 3.** In the tangency example, replace $s^4$ by $s^{2m}$ with $m\geq1$. Determine the required growth of the normal multiplier and check the weighted error.

**Solution.** A conormal covector is $(-2m s^{2m-1}\lambda,\lambda)$. To keep its tangential component equal to $c\ne0$, take $\lambda=-c/(2m s^{2m-1})$. Its norm is of order $|s|^{-(2m-1)}$, while the distance to the graph of the embedding is $|s|^{2m}$. Their product is of order $|s|$ and tends to zero. Every even tangency order therefore gives the same qualitative failure of the ordinary cotangent image, though the rate at which the normal covector diverges depends on the contact order.

**Problem 4.** Distinguish the two antipodes in (CHE17) in a one-dimensional fibre coordinate $e$.

**Solution.** In coordinates $(y,e;\eta,\epsilon)$, the cotangent lift of the bundle antipode is $(y,-e;\eta,-\epsilon)$. The cotangent-fibre antipode is $(y,e;-\eta,-\epsilon)$. They act on different base spaces. Their composite is $(y,-e;-\eta,\epsilon)$. Thus an estimate with the second antipode cannot be rewritten using only the first. The coordinate calculation in the proof of SH02-CHE-003 is exactly what cancels the first and retains the second.

## SH02-CHE-RANGE — The full input range and its unbounded proof

The full intended tensor and internal Hom estimate allows two inputs in $D^+(k_X)$. The deductions in SH02-CHE-006 establish the bounded-input theorem. SH02-UCE-SUM supplies both estimates for arbitrary inputs in the classical unbounded category, with the same coefficient ring and manifold assumptions. Its restriction to two bounded-below inputs proves the full printed range, including a possibly unbounded-below Hom output. The proof uses uniform local tests, raw specialization and radial recovery; it does not require the unresolved Fourier comparison.

The issue is substantial for internal Hom. Already at a point over a field, let $G=\bigoplus_{n\geq0}k[-n]$ and $F=k$. Both are bounded below, but

$$
R\operatorname{Hom}(G,F)\simeq\prod_{n\geq0}k[n]
\tag{CHE34}
$$

has nonzero cohomology in arbitrarily negative degrees. Thus membership of the two inputs in $D^+$ does not keep the Hom output in $D^+$. This calculation does not refute a correctly formulated unbounded microsupport estimate. It shows why a proof must specify that framework and justify the local tests and derived limit operations there. Degreewise truncation alone is insufficient: truncating a complex need not preserve its microsupport bound. Those steps are proved in SH02-UCE-WINDOWS, SH02-UCE-TESTS and the subsequent geometric arguments. The finite windows extend natural functor comparisons; the support tests themselves are applied to the original complex on neighborhoods chosen uniformly in degree.

## SH02-CHE-REGULARITY — A $C^1$ chart can change an asymptotic sum

The asymptotic operations above are invariant under smooth coordinate changes by their normal-cone construction. Their behavior under $C^1$ changes is different from the $C^1$ invariance of microsupport. Here is a direct calculation.

Fix $1<r<2$ and put $g(s)=|s|^r$, $Z=\{(s,g(s))\}\subset\mathbb R^2$, and

$$
A=N_Z^*\mathbb R^2
=\{(s,g(s);-g'(s)\lambda,\lambda):\lambda\in\mathbb R\}.
\tag{CHE35}
$$

The graph is a $C^1$ submanifold, and $A$ is a closed conic subset of the ordinary smooth cotangent bundle. We claim

$$
A\widehat+A=A\cup T^*_0\mathbb R^2.
\tag{CHE36}
$$

To create a prescribed covector $(c,d)$ at the origin, use graph points with parameters $s_n>0$ and $-s_n$, where $s_n\to0$. The derivatives there are $a_n=rs_n^{r-1}$ and $-a_n$. Choose

$$
\lambda_n=-\frac{c}{2a_n},\qquad \mu_n=d-\lambda_n.
$$

The covectors $(-a_n\lambda_n,\lambda_n)$ and $(a_n\mu_n,\mu_n)$ sum to $(c+a_nd,d)$, which tends to $(c,d)$. The graph points have distance $2s_n$, and the first covector has norm $O(s_n^{1-r})$ when $c\ne0$. Their weighted separation is therefore $O(s_n^{2-r})\to0$. If $c=0$, the same construction has first covector zero and still satisfies the criterion. Thus every covector over the origin lies in the asymptotic sum.

It remains to exclude other extra points. The base of any asymptotic limit belongs to the closed graph. Near a point with parameter $s_0\ne0$, the derivative $g'$ is Lipschitz. Suppose two conormal covectors at parameters $u_n,v_n\to s_0$ have a convergent sum. Write their normal coefficients as $\lambda_n,\mu_n$. Then $\lambda_n+\mu_n\to d$. The tangential component of their sum can be rewritten as

$$
-g'(v_n)(\lambda_n+\mu_n)
+(g'(v_n)-g'(u_n))\lambda_n.
$$

The second summand tends to zero: its norm is bounded by a constant times $|u_n-v_n|\,|\lambda_n|$, and this is bounded by the weighted separation in the definition of the asymptotic sum. The limit is therefore $(-g'(s_0)d,d)$, a conormal covector. This proves (CHE36).

Now use the $C^1$ diffeomorphism $\Phi(s,t)=(s,t-g(s))$. It sends $Z$ to the horizontal line, and its cotangent transport sends $A$ to that line's conormal bundle $B$. Since every covector in $B$ has tangential component zero, $B\widehat+B=B$. But (CHE36) transports to $B\cup T^*_0\mathbb R^2$, which is strictly larger. The operation $\widehat+$ is therefore not invariant under all $C^1$ coordinate changes.

The same calculation also exhibits failure of $C^1$ invariance for the generalized inverse-image operation. Indeed (CHE27) writes $A\widehat+A$ as the generalized inverse image of $A\times A$ by the diagonal. The pair of coordinate changes $\Phi$ and $\Phi\times\Phi$ preserves the diagonal map and sends $A\times A$ to $B\times B$. If generalized inverse image were invariant under these $C^1$ coordinate changes, (CHE27) would force the false equality just obtained. No claim of this invariance is needed by the smooth-manifold estimates.

## Exact range of the readable comparison

In [Astérisque 128](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorem 5.2.2 allows bounded-below tensor inputs under finite weak global dimension, but its internal-Hom assertion additionally requires the first Hom input to be bounded. This is an actual restriction of that edition. Schapira’s [2016 review](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), Corollary 2.12, is a noncharacteristic estimate and cannot replace the full asymptotic-sum theorem used in CHE-006. Thus the bounded proof above is supported by the normal-deformation and graph argument, while the larger intended Hom range remains dependent on the explicitly linked unbounded supplement and its uniform tests. The point example in CHE-RANGE is retained because it shows exactly why bounded-below inputs do not make the Hom output bounded below. No source citation discharges that extra proof obligation.
