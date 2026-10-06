# Constructibility through smooth cutoffs and microlocal properness

A nonproper image can become constructible when its relevant part is confined to a bounded region. There are two useful forms of confinement. A real $C^1$ function can stabilize the image along its sublevels. Alternatively, a compact set of base covectors can force every contributing fibre point into one compact set. We give proofs that retain perfect coefficients in both situations, including when the smooth sublevels themselves have no subanalytic description.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Use [Constructibility from microsupport and perfect stalks](../../sheaf-proof-readings/SH03-constructibility-from-microsupport-and-perfect-stalks.html), [Perfect coefficients on compact fibres](../../sheaf-proof-readings/SH03-perfect-coefficients-on-compact-fibres.html), and [Perfect operations and finite microlocal coefficients](../../sheaf-proof-readings/SH03-perfect-operations-and-finite-microlocal-coefficients.html). The exact current microlocal prerequisites are the bounded relative cutoff theorem, the full limiting tensor estimate, microlocally proper projection, and the cone criterion for localized isomorphisms. Their statements are specified below; their lower and transitive proofs remain explicit dependencies. The references give the classical results of Masaki Kashiwara and Pierre Schapira and freely readable accounts with their precise scopes. We prove the forward local geometric criterion here. Constructible models in one cotangent direction supplies its converse and the contact-equivalence application.

## Coefficients and closure under retracts

Let $k$ be a commutative ring of finite global dimension. Manifolds and maps used for constructibility are real analytic, Hausdorff, countable at infinity, with finite uniform dimension bounds. Complexes lie in the globally bounded derived categories $D^b(k_X)$. The exhaustion function below is only $C^1$. Tensor products are derived. Write $G_Z=G\otimes^L k_Z$ for restriction followed by extension by zero and $R\Gamma_ZG=R\mathcal Hom(k_Z,G)$ for local cohomology with support. Even for closed $Z$, these two objects are different.

An object $A$ is a **retract** of $E$ if there are arrows $i:A\to E$ and $r:E\to A$ with $ri=1_A$. If $E$ is weakly R-constructible, so is $A$. Indeed, every local-cohomology test of $A$ is a retract of the same test of $E$, hence

\[
 \operatorname{SS}(A)\subset\operatorname{SS}(E).
 \tag{1}
\]

The geometric constructibility criterion supplies the same closed subanalytic isotropic bound for $A$. If $E$ is R-constructible, $A$ also has perfect stalks. A split triangle gives $E_x\simeq A_x\oplus B_x$ in $D(k)$; perfection passes to either summand. We use precisely [Stacks Project, Lemma 15.76.5, Tag 066S](https://stacks.math.columbia.edu/tag/066S) for this algebraic fact. Its pseudo-coherence and Tor-amplitude dependencies remain foundation imports. No Noetherian hypothesis or replacement of perfection by finite-dimensional cohomology is needed.

The following simple device produces a retract. If $u:A\to E$, $v:E\to B$, and $vu$ is an isomorphism, then

\[
 i=u(vu)^{-1}:B\to E,\qquad r=v:E\to B,
 \qquad ri=1_B.
 \tag{2}
\]

The objects $A$ and $B$ can be different representatives of one stabilized image. Neither $u$ nor $v$ has to be invertible.

## The exact signed cutoff input

Let $f:Y\to X$ be analytic, $G\in D^b(k_Y)$, and $\varphi:Y\to\mathbb R$ be $C^1$. Put

\[
 Z_t=\{\varphi\leq t\},\qquad U_t=\{\varphi<t\},
 \qquad V_{f,y}=\operatorname{im}(d f_y^t).
 \tag{3}
\]

Assume that $\operatorname{supp}(G)\cap Z_t\to X$ is proper for **every real $t$**. Fix $t_0\in\mathbb R$. If $d\varphi_y\notin\operatorname{SS}(G)_y+V_{f,y}$ for $\varphi(y)>t_0$, the relative cutoff prerequisite gives

\[
 Rf_*G\xrightarrow{\sim}Rf_*(G_{Z_t})\qquad(t\geq t_0).
 \tag{4+}
\]

If instead $-d\varphi_y\notin\operatorname{SS}(G)_y+V_{f,y}$ for $\varphi(y)>t_0$, it gives

\[
 Rf_!R\Gamma_{Z_t}G\xrightarrow{\sim}Rf_!G\qquad(t\geq t_0).
 \tag{4−}
\]

These are respectively the actual restriction and supported counit maps. On the cutoffs, closed support properness permits $Rf_!$ to be replaced by $Rf_*$. The open analogues use $t>t_0$: ordinary restriction is $Rf_*G\to R(f|_{U_t})_*(G|_{U_t})$, while the proper-support arrow runs from $R(f|_{U_t})_!(G|_{U_t})$ to $Rf_!G$. We will use the closed formulas, choosing two levels strictly larger than $t_0$.

No subanalyticity of $Z_t$ occurs in this input. The signed conditions are independent: the positive one proves the ordinary-image assertion, the negative one proves the proper-support assertion. If both hold, both conclusions below follow. The valid threshold microsupport inclusion can also be retained from the cutoff theorem. This proof does not use the additional equality between geometric images printed in the general-real source statement; the earlier cutoff lesson keeps that equality as a typed source comparison.

## A compact subanalytic set between two smooth cutoffs

**Theorem.** Under the all-level properness assumption and the positive condition in (4), if $G$ is R-constructible, then $Rf_*G$ is R-constructible. Under the negative condition, $Rf_!G$ is R-constructible.

**Proof.** Work locally over a relatively compact subanalytic coordinate ball $B\subset X$, with compact closure. Write $V=f^{-1}B$ and $f_B:V\to B$. Choose

\[
 t_0<t_1<t_2,
 \qquad
 C=\operatorname{supp}(G)\cap f^{-1}(\overline B)\cap Z_{t_1}.
 \tag{5}
\]

All-level support properness makes $C$ compact. Every point of $C$ has a small analytic coordinate ball with compact closure inside $\{\varphi<t_2\}$. A finite subcover gives a compact subanalytic union $K$ of closed coordinate balls such that

\[
 C\subset\operatorname{Int}K,\qquad K\subset\{\varphi<t_2\}.
 \tag{6}
\]

Finite unions of these balls are locally subanalytic, even when $\varphi$ is not analytic. If $C$ is empty take $K=\varnothing$. Restrict $G$ to the analytic open manifold $V$ and call that restriction $H$. For readability, all sets in the next two displays mean their intersection with $V$. The bounds on closed supports are

\[
 \operatorname{supp}(H_{Z_{t_1}}),\ 
 \operatorname{supp}(R\Gamma_{Z_{t_1}}H)
 \subset C\cap V\subset\operatorname{Int}K.
 \tag{7}
\]

For the ordinary image, closed restriction gives the factorization

\[
 H_{Z_{t_2}}\longrightarrow H_K
 \longrightarrow H_{Z_{t_1}\cap K}
 \xrightarrow{\sim}H_{Z_{t_1}}.
 \tag{8}
\]

The first arrow uses $K\subset Z_{t_2}$. The last arrow is the inverse of the restriction isomorphism supplied by (7). The composite is the usual $Z_{t_2}$-to-$Z_{t_1}$ restriction, as may be checked before tensoring by $H$ and then on its support. Its image under $Rf_{B*}$ is an isomorphism: both outer objects are canonically isomorphic to $(Rf_*G)|_B$ by (4), and those canonical restriction maps commute with the level restriction. Formula (2) exhibits $(Rf_*G)|_B$ as a retract of

\[
 E=Rf_{B*}(H_K).
 \tag{9}
\]

The object $H_K$ is R-constructible by analytic inverse image, tensor closure and subanalyticity of $K$. Its closed support lies in the compact set $K$, viewed relatively over $B$. For every compact $T\subset B$, the support lying over $T$ is closed in $K\cap f^{-1}T$, hence compact. Thus $f_B$ is proper on this support. The perfect proper-image theorem makes $E$ R-constructible, including its perfect stalks. Retract closure proves the ordinary assertion on $B$.

For the proper-support image, the factorization goes in the opposite direction:

\[
 R\Gamma_{Z_{t_1}}H
 \xrightarrow{\sim}R\Gamma_{Z_{t_1}\cap K}H
 \longrightarrow R\Gamma_KH
 \longrightarrow R\Gamma_{Z_{t_2}}H.
 \tag{10}
\]

The first isomorphism follows from (7) and closed-support localization, or by applying $R\Gamma_K$ to $R\Gamma_{Z_{t_1}}H$. The two subsequent arrows are inclusions of support conditions. Composing gives the canonical $Z_{t_1}$-to-$Z_{t_2}$ supported map: the intersection and nested-support maps are compatible with their counits to $H$. After $Rf_{B!}$ this composite is invertible by the negative condition in (4). Therefore $(Rf_!G)|_B$ is a retract of

\[
 E'=Rf_{B!}R\Gamma_KH
   =Rf_{B*}R\mathcal Hom(k_K,H).
 \tag{11}
\]

Internal-Hom closure makes the coefficient in (11) R-constructible; its closed support is again inside $K$, so the same proper perfect-image theorem applies. Retract closure proves the second assertion on $B$. Real constructibility is local on the target; the globally bounded image supplied by the six-operation dimension bounds is therefore R-constructible on $X$. $\square$

The proof factors derived objects and actual comparison maps. Merely proving that each image stalk has finite cohomology would leave the geometric constructibility assertion unproved. We imposed subanalyticity on $K$, where the operation theorem needs it, while retaining the original smooth sublevels in the stabilization theorem.

## Pointwise constructible representatives

For any subset $\Omega\subset T^*X$, the localized category is

\[
 D^b(k_X;\Omega)=D^b(k_X)/\mathcal N_\Omega,
 \qquad
 \mathcal N_\Omega=\{A:\operatorname{SS}(A)\cap\Omega=\varnothing\}.
 \tag{12}
\]

An arrow becomes invertible exactly when the microsupport of its cone misses $\Omega$. This is the precise current localization prerequisite. At a point $p$, a **weakly constructible representative** of $F$ means a globally weakly R-constructible $F_p\in D^b(k_X)$ together with an isomorphism $F\simeq F_p$ in $D^b(k_X;p)$. A constructible representative requires $F_p$ to be globally R-constructible, including perfect stalks. The full localized subcategories consisting of objects with these representatives at every $p\in\Omega$ are denoted

\[
 D^b_{\mathrm{w\text{-}R\text{-}c}}(k_X;\Omega),
 \qquad D^b_{\mathrm{R\text{-}c}}(k_X;\Omega).
 \tag{13}
\]

The representative may depend on $p$. No single globally constructible model over all of $\Omega$ is part of this definition. Membership is invariant under localized isomorphism, since localization at $\Omega$ maps to localization at any of its points.

**Forward geometric criterion.** If $F$ belongs to the weak subcategory in (13), there is an open neighborhood $U$ of $\Omega$ such that $\operatorname{SS}(F)\cap U$ is contained in a relatively closed subanalytic isotropic subset of $U$. In fact $\operatorname{SS}(F)\cap U$ itself has these properties.

**Proof.** At each $p\in\Omega$, represent the isomorphism by a fraction

\[
 F\xleftarrow{s}H\xrightarrow{v}F_p.
 \tag{14}
\]

The fraction calculus makes $s$ a $p$-denominator. Since the fraction is invertible, $v$ is also invertible after localization; the saturated cone criterion makes it a $p$-denominator as well. The two cones have closed microsupport avoiding $p$. Hence a common open neighborhood $W_p$ of $p$ avoids both cones. The triangle estimate in both directions gives

\[
 \operatorname{SS}(F)\cap W_p
 =\operatorname{SS}(H)\cap W_p
 =\operatorname{SS}(F_p)\cap W_p.
 \tag{15}
\]

The global weak constructibility theorem makes $\operatorname{SS}(F_p)$ subanalytic Lagrangian. Set $U=\bigcup_{p\in\Omega}W_p$. Subanalyticity and isotropy of $\operatorname{SS}(F)\cap U$ follow locally from (15). This set is relatively closed in $U$, because the original microsupport is closed. An arbitrary union of the neighborhoods is allowed: there is no need to glue the sheaf representatives or to find one finite family over a noncompact $\Omega$. If $\Omega$ is empty, take $U=\varnothing$. $\square$

This proves the forward local geometric criterion, with $\Omega$ arbitrary, possibly nonopen and nonconic. The converse requires construction of a global weakly constructible model from local isotropic control. The next lesson gives that construction using a cone, a flat cap and an outer compact supported localization. In particular a geometric bound alone supplies no perfect-coefficient assertion.

## The projection retains the fibre point

Let $q:X\times Y\to X$ be projection and let $\Omega\subset T^*X$ now be **open**. For $F\in D^b(k_{X\times Y})$ write $A=\operatorname{SS}(F)$ and

\[
 p:T^*(X\times Y)\longrightarrow T^*X\times Y,
 \qquad p(x,y;\xi,\eta)=(x;\xi,y).
 \tag{16}
\]

The map forgets the fibre covector $\eta$ and retains its base point $y$. For the constructibility argument below, it is enough to assume properness of

\[
 p(A)\cap(\Omega\times Y)\longrightarrow\Omega.
 \tag{17}
\]

It implies the following useful quantified condition: for every compact $T\subset\Omega$ there is a compact $L_T\subset Y$ such that

\[
 (x,y;\xi,\eta)\in A,\quad(x;\xi)\in T
 \quad\Longrightarrow\quad y\in L_T,
 \quad\text{for every }\eta.
 \tag{18}
\]

Indeed, project the compact inverse image of $T$ in (17) to $Y$. The exact current projection prerequisite uses $\overline{p(A)}$ in (17), as does Kashiwara and Schapira's freely readable [Theorem 4.4.2, printed 75–76](https://www.numdam.org/item/AST_1985__128__1_0/). Condition (18) supplies this closure version too. Given compact $T\subset\Omega$, choose a compact neighborhood $T'\subset\Omega$ of $T$. Points of $p(A)$ tending to a point over $T$ eventually have first coordinate in $T'$, so their fibre base points lie in $L_{T'}$. The inverse image of $T$ in $\overline{p(A)}$ is consequently a closed subset of $T\times L_{T'}$, hence compact. Thus assumption (17) implies the exact imported closure hypothesis.

Under that closure hypothesis the projection theorem gives

\[
 \begin{aligned}
 \operatorname{SS}(Rq_*F)\cap\Omega
 &\subset\{(x;\xi):\text{some }y\text{ has }(x,y;\xi,0)\in A\},\\
 \operatorname{SS}(Rq_!F)\cap\Omega
 &\subset\{(x;\xi):\text{some }y\text{ has }(x,y;\xi,0)\in A\},
 \end{aligned}
 \tag{19}
\]

and the canonical $Rq_!F\to Rq_*F$ is invertible in $D^b(k_X;\Omega)$. This is an antecedent microlocal estimate, with its full boundary and boundedness dependencies. We next establish the additional constructibility conclusion by an explicit compact fibre cutoff.

## One compact fibre cutoff gives both representatives

**Theorem.** Assume (17) and let $F$ be R-constructible. Then both $Rq_!F$ and $Rq_*F$ belong to $D^b_{\mathrm{R\text{-}c}}(k_X;\Omega)$.

**Proof.** Fix $p_0\in\Omega$. Choose an open neighborhood $W$ of $p_0$ with compact closure in $\Omega$. Apply (18) to $\overline W$ to obtain a compact $L\subset Y$. A finite union of relatively compact analytic coordinate balls gives a relatively compact subanalytic open set $D\subset Y$ such that

\[
 L\subset D,\qquad\overline D\text{ is compact}.
 \tag{20}
\]

No smooth boundary or transversality condition on $D$ is required. With $q_2:X\times Y\to Y$, form the ordinary open/closed localization triangle

\[
 F_D:=F\otimes^L q_2^{-1}k_D
 \longrightarrow F
 \longrightarrow C:=F\otimes^L q_2^{-1}k_{Y\setminus D}
 \xrightarrow{+1}.
 \tag{21}
\]

All three coefficients are R-constructible by analytic inverse image and tensor closure. In particular $F_D$ has closed support in $X\times\overline D$, so $q$ is proper on its support. The perfect proper-image theorem makes

\[
 H_D=Rq_!F_D\xrightarrow{\sim}Rq_*F_D
 \tag{22}
\]

a globally R-constructible object on $X$, with the displayed canonical comparison invertible globally.

We claim that

\[
 p(\operatorname{SS}(C))\cap(W\times Y)=\varnothing.
 \tag{23}
\]

Inside $X\times D$, $C$ is zero. At a base point $(x_0,y_0)$ outside that open set, apply the bounded full tensor estimate SH02-CHE-006:

\[
 \operatorname{SS}(C)
 \subset A\widehat+\operatorname{SS}(q_2^{-1}k_{Y\setminus D}).
 \tag{24}
\]

Submersion pullback says that every covector of the second set has **zero $X$ component**. If (24) had a witness with limiting $X$ covector $(x_0;\xi_0)\in W$, write the first witness as $(x_j,y_j;\xi_j,\eta_j)\in A$. Since the other summand's $X$ component is zero, $(x_j;\xi_j)\to(x_0;\xi_0)$, also when the fibre covectors diverge and cancel. All sufficiently late first covectors lie in $\overline W$; (18) then gives $y_j\in L$. Their limiting base point $y_0$ lies in the compact closed set $L\subset D$, a contradiction. The weighted base-separation condition of SH02-AE-SUM remains part of the full limiting-sum witness. The contradiction already follows from its base-point control and does not discard escaping covectors. This proves (23), including at zero base covectors when these lie in $W$.

Because $W$ is open, (23) also excludes $\overline{p(\operatorname{SS}(C))}$ over $W$. Its projection is the empty proper map. Apply (19) to $C$ over $W$ to obtain

\[
 \operatorname{SS}(Rq_!C)\cap W
 =\operatorname{SS}(Rq_*C)\cap W=\varnothing.
 \tag{25}
\]

The two images of (21) therefore give actual isomorphisms

\[
 Rq_!F_D\longrightarrow Rq_!F,
 \qquad Rq_*F_D\longrightarrow Rq_*F
 \quad\text{in }D^b(k_X;W).
 \tag{26}
\]

By (22), one globally R-constructible $H_D$ represents both images at $p_0$. Since $p_0$ was arbitrary, definition (13) proves the theorem. If $Y$ is empty the two images are zero and the statement is immediate. The construction gives a separate $D$ near each point, without assuming a uniform compact cutoff for all of $\Omega$. $\square$

Naturality places (26) in a commutative square with the canonical comparisons $Rq_!\to Rq_*$. The left comparison is the isomorphism (22), and both horizontal arrows are invertible over $W$. Thus the original canonical comparison is invertible there as well. The pointwise perfect representatives are obtained before this inference; they are not deduced from equality of the two microsupport bounds.

## Examples and exercises with complete solutions

### An invertible composite produces a constructible retract

*Difficulty: Introductory.*

Suppose $A\xrightarrow{u}E\xrightarrow{v}B$ has invertible composite and $E$ is R-constructible. Prove that $B$ is R-constructible. Give an example over a point in which neither arrow is invertible, although the composite is.

**Solution.** Define $i=u(vu)^{-1}$ and $r=v$. Then $ri=1_B$. Each local-cohomology test of $B$ is a retract of the corresponding test of $E$, so $\operatorname{SS}(B)\subset\operatorname{SS}(E)$ and the same isotropic bound proves weak constructibility. On each stalk, the split triangle identifies $E_x$ with $B_x\oplus C_x$; perfect-summand closure proves perfection of $B_x$. For a nonzero coefficient ring take $A=B=k$, $E=k\oplus k[-1]$, $u$ the first-summand inclusion and $v$ its projection. Their composite is $1_k$. The nonzero degree-one summand of $E$ prevents either arrow from being invertible. In the cutoff argument it is the composite, rather than either intermediate restriction or support map, that is known to stabilize.

### A continuously differentiable exhaustion can have a non-subanalytic level

*Difficulty: Intermediate.*

Choose a smooth function $\chi:\mathbb R\to[0,1]$ equal to one on $[-1,1]$ and zero outside $(-2,2)$. Set

\[
 h(y)=\begin{cases}y^6\sin(1/y),&y\ne0,\\0,&y=0,\end{cases}
 \qquad \varphi(y)=\chi(y)h(y)+(1-\chi(y))y^2.
 \tag{27}
\]

Verify the $C^1$ and proper-sublevel assertions for the map $f:\mathbb R\to\mathrm{pt}$. Show that $Z_0$ is not locally subanalytic at zero, while both signed cutoff conditions hold for $G=k_{\mathbb R}$ with $t_0=65$. Compute the two full images.

**Solution.** For $y\ne0$,

\[
 h'(y)=6y^5\sin(1/y)-y^4\cos(1/y).
\]

The difference quotient at zero tends to zero, and the displayed derivative tends to zero, so $h$ and $\varphi$ are $C^1$. Outside $[-2,2]$, $\varphi=y^2$; every closed sublevel is therefore closed and bounded, hence compact. Near zero, $Z_0$ is given by $y^6\sin(1/y)\leq0$. Infinitely many negative-sine intervals separated by positive-sine intervals accumulate at zero on the positive side. A locally subanalytic subset of a line has only finitely many components in a sufficiently small compact neighborhood; hence $Z_0$ is not locally subanalytic there.

For $|y|\leq2$, the convex combination in (27) is at most $64$. Thus $\varphi>65$ implies $|y|>2$ and $d\varphi=2y\,dy\ne0$. Here $V_f=0$ and $\operatorname{SS}(k_{\mathbb R})$ is contained in the zero section; both signs satisfy the exclusion. The ordinary full image is $k$ and the proper-support full image is $k[-1]$, using the increasing orientation of the line. Both are perfect. This example explains why smooth-cutoff constructibility cannot be justified by asserting subanalyticity of every smooth sublevel.

### The closed ordinary and supported cutoffs have different degrees

*Difficulty: Intermediate.*

Let $G=k_{\mathbb R}$, $f:\mathbb R\to\mathrm{pt}$ and $\varphi(y)=y^2$. Use $t_0=0$. For $t>0$, put $a=\sqrt t>0$. Compute the ordinary closed cutoff and the supported closed cutoff, and check their stabilization degrees. When $k\ne0$, explain why the open endpoint cannot be included at $t=0$.

**Solution.** The two signs of $2y\,dy$ are nonzero for $y^2>0$, so both exclusions hold. The ordinary closed cutoff has

\[
 R\Gamma(\mathbb R;k_{[-a,a]})=k.
\]

For the supported cutoff use the localization triangle with the two complementary open rays. Their ordinary cohomology is $k\oplus k$, and the restriction from the full line is diagonal:

\[
 R\Gamma_{[-a,a]}(\mathbb R;k)
 \longrightarrow k\xrightarrow{(1,1)}k^2\xrightarrow{+1}.
\]

The cokernel, identified with $k$ by $(b_-,b_+)\mapsto b_+-b_-$, lies in degree one. Consequently $R\Gamma_{[-a,a]}(\mathbb R;k)=k[-1]$. Its coefficient sheaf has closed support in $[-a,a]$, so its ordinary ambient image equals its proper-support image. These are the stabilized full images $Rf_*G=k$ and $Rf_!G=k[-1]$, respectively. At $t=0$ the closed ordinary point still gives $k$ and point support still gives $k[-1]$. The open sublevel is empty, giving zero in both cases. When $k\ne0$, the empty open sublevel does not give the stabilized full images at $t=0$. The calculations retain the strict open and nonstrict closed endpoint rules and keep restriction separate from support.

### Weak coefficients do not become perfect through exhaustion

*Difficulty: Intermediate.*

Let $k$ be a field and $M=\bigoplus_{n\geq0}k$. For the constant sheaf $G=M_{\mathbb R}$ and the previous quadratic exhaustion, check the properness and signed exclusions. Determine both images and identify the hypothesis of the constructibility theorem that fails.

**Solution.** The support is the whole line, whose closed quadratic sublevels are compact. A constant sheaf of any coefficient module has zero-section microsupport, so the signed exclusions hold outside $y=0$. Ordinary line cohomology is $M$ and compact line cohomology is $M[-1]$. One may compute the latter from a finite interval and its two-endpoint localization, retaining the full module in the diagonal and difference maps. The source is weakly R-constructible but is not R-constructible: its stalk $M$ is an infinite-dimensional vector space and is not perfect. The same is true of either image. The cutoff theorem preserves its geometric stabilization; the perfect-image argument requires perfect source coefficients.

### Nonproper support can still have a compact directional cutoff

*Difficulty: Advanced.*

Assume $k\ne0$. On $\mathbb R_x\times\mathbb R_y$ let

\[
 F=k_{[0,\infty)\times[-1,1]}\oplus k_{\mathbb R^2},
 \qquad q(x,y)=x.
 \tag{28}
\]

Take an open neighborhood $\Omega$ of $(0;dx)$ with $1/2<\xi<3/2$. Check (17), although $q$ is not proper on the full support. Compute both images and exhibit one globally constructible model obtained by $D=(-2,2)$.

**Solution.** The constant summand has only zero $X$ covectors and contributes nothing over this $\Omega$. For the rectangle summand, every fibre base point lies in $[-1,1]$; its microsupport is closed and has the product boundary description. After forgetting the $Y$ covector its part over $\Omega$ is relatively closed with fibre base in $[-1,1]$, so compact inverse images prove (17). The full support contains $\mathbb R^2$, and the inverse image of the compact base point $\{0\}$ in that support is noncompact.

The compact closed interval has ordinary cohomology $k$ with no shift. The full open line has ordinary cohomology $k$ and compact cohomology $k[-1]$. Thus

\[
 Rq_*F=k_{[0,\infty)}\oplus k_{\mathbb R},
 \qquad
 Rq_!F=k_{[0,\infty)}\oplus k_{\mathbb R}[-1].
 \tag{29}
\]

The cutoff leaves the rectangle summand unchanged and replaces the constant summand by $k_{\mathbb R\times(-2,2)}$. Its proper-support image is

\[
 H_D=k_{[0,\infty)}\oplus k_{\mathbb R}[-1].
\]

This is globally R-constructible and has proper coefficient support in the fibre direction before applying $q$. The cutoff maps identify it with both images at every point of $\Omega$: their complementary terms are locally constant on the base and have no nonzero $X$ covector. The globally constructible $k_{[0,\infty)}$ is also a common localized model, but $H_D$ is the model furnished by the explicit compact-cutoff construction.

### A noncompact fibre can obstruct the image comparison

*Difficulty: Advanced.*

Assume $k$ is a nonzero field. Replace (28) by $F=k_{[0,\infty)\times\mathbb R}$ and keep $p_0=(0;dx)$. Compute the images, show that (17) fails, and determine whether the canonical image comparison is invertible at $p_0$.

**Solution.** For every $y\in\mathbb R$, $(0,y;dx,0)$ belongs to the source microsupport. The inverse image of $\{p_0\}$ under the projection in (17) contains the whole fibre line, so it is noncompact. The images are

\[
 Rq_*F=k_{[0,\infty)},\qquad
 Rq_!F=k_{[0,\infty)}[-1].
\]

The fibre comparison $R\Gamma_c(\mathbb R;k)\to R\Gamma(\mathbb R;k)$ is a map $k[-1]\to k$. Its degree-zero derived morphism group is $\operatorname{Ext}^1_k(k,k)=0$, so it is zero. Tensoring gives the zero image comparison. At $p_0$, the halfline local-cohomology test has coefficient $k$; for the shifted object it has $k[-1]$. The zero map between these nonzero tests cannot be invertible. Both images happen to be globally constructible here, but their directional comparison fails exactly where no compact fibre control is available.

### Compactness of only the critical fibre image is insufficient

*Difficulty: Advanced.*

Assume $k\ne0$. Let $Z=\{(x,y):xy=1,\ y>0\}\subset\mathbb R^2$ and $F=k_Z$, extended by its closed embedding. Near $p_0=(0;dx)$, show that there are no source microsupport covectors with $\eta=0$ and nonzero $\xi$. Nevertheless compute a nonzero ordinary image at $p_0$. Find the escaping covectors responsible for the failure of (17).

**Solution.** The positive hyperbola branch is closed: a finite limit of its points still has $xy=1$ and positive $y$. It is a smooth semialgebraic submanifold, so $F$ is R-constructible with perfect stalk $k$. Along $Z$ its microsupport is its full conormal. For $x=1/y$ this has covectors

\[
 (x,y;\xi,\eta)=(1/y,y;\xi,\xi/y^2).
 \tag{30}
\]

For nonzero $\xi$, the fibre component is nonzero. Thus the ordinary critical image in (19) is empty in a positive-covector neighborhood of $p_0$. Projection identifies $Z$ analytically with $(0,\infty)$, so

\[
 Rq_*F=k_{[0,\infty)},\qquad Rq_!F=k_{(0,\infty)}.
 \tag{31}
\]

The first assertion uses the actual ordinary open-extension stalk: a small positive interval has coefficient $k$ and no higher cohomology; restriction to zero therefore has stalk $k$. The positive conormal $dx$ belongs to its microsupport at zero, whereas the open extension has the negative boundary ray. Hence the ordinary image is nonzero at $p_0$, despite the empty critical source image there.

Take $y_j=j$, $x_j=1/j$, $\xi_j=1$ and $\eta_j=1/j^2$. Their $X$ covectors lie in one compact subset of $\Omega$ after discarding finitely many terms, while $y_j\to\infty$. The retained fibre points escape, contradicting (18) and therefore (17). A condition controlling only source covectors with $\eta=0$ would be vacuous in this example and would wrongly predict the ordinary-image bound. The all-$\eta$ control is essential.

## References and proof boundaries

The proof is organized around an actual factorization through a compact subanalytic neighbourhood and a retract of a perfect object. The same results are treated in Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorems 4.4.1–4.4.2, Remark 8.3.2, and Proposition 8.6.1. These sources were checked with their signed hypotheses. The relative smooth closed-sublevel cutoff used in this lesson has additional scope. Its exact closed-endpoint maps are supplied by [SH02-MO-RELATIVE-CUTOFF and its proof](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-RELATIVE-CUTOFF), using compact-neighbourhood continuity for ordinary restriction and a supported localization argument for the opposite sign. That proof depends on the foundations named in its lesson; its theorem is not inferred from the 1985 result about nested open sets. The sandwich proof explicitly avoids treating a merely smooth sublevel as subanalytic.

A freely readable human source is Kashiwara and Schapira, [*Microlocal study of sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/) ([author-hosted PDF](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf)). Theorem 4.4.1 gives signed stabilization for nested open exhaustions with proper closed-support truncations and a closure condition on the cotangent sum. Theorem 4.4.2 uses the closure of the projection retaining the fibre point and gives both microsupport bounds and the canonical proper-to-ordinary image comparison. Remark 8.3.2 relates the first theorem to real constructibility. Our smooth-sublevel sandwich and retract argument uses the separately stated $C^1$ cutoff input, including its closed endpoint maps. Proposition 8.6.1 concerns holomorphic maps and subanalytic exhausting opens; it does not supply the extra scope of arbitrary real $C^1$ non-subanalytic sublevels.

Pierre Schapira, [*Constructible sheaves and functions up to infinity*, Lemma 2.7](https://arxiv.org/html/2012.09652v5#S2.Thmtheorem7), gives related ambient-extension criteria. It assumes a relatively compact subanalytic open embedding and a Noetherian coefficient ring of finite global dimension. This supplies context for constructible extensions; it is narrower than the arbitrary-$\Omega$ pointwise representatives used here.

The exact bounded full tensor estimate is SH02-CHE-006, and its limiting-sum witness convention is SH02-AE-SUM. The signed cutoff input is [SH02-MO-RELATIVE-CUTOFF](../../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-RELATIVE-CUTOFF), including its one-sided/full-map proof; the projection input is SH02-AE-MICROPROPER, including closure and all-fibre-covector compact control; localization uses [SH02-MC-LOCAL](../../sheaf-proof-readings/SH02-microlocal-categories.html#SH02-MC-LOCAL), including saturated denominators. Their lower proof dependencies remain imports. The source statements and map directions are preserved; no text from the provider lessons is reproduced here.

The direct-summand argument uses [Stacks Project, Lemma 15.76.5, Tag 066S](https://stacks.math.columbia.edu/tag/066S), perfect direct-summand closure, GFDL 1.2 or later. Its pseudo-coherence and Tor-amplitude foundations are imported rather than proved here.

The general-real cutoff image-equality comparison is recorded in the earlier cutoff lesson. The next lesson proves the reverse local isotropic criterion and the contact-equivalence application relative to their stated prerequisites. The seven solutions above are complete relative to the prerequisites specified here. The microlocal, six-operation, geometric constructibility, perfect-coefficient and localization foundations retain their own proof scopes.

The compactness step in the projection argument retains the fibre base point while discarding only its covector. The closure in the free source’s Theorem 4.4.2 is essential: enlarging a compact target set to a compact neighbourhood controls limit points as well. That control is precisely what prevents nonzero fibre covectors from escaping to a boundary in the comparison-cone argument. The all-covector hypothesis, the open target neighbourhood and both signs of the cutoff are retained. The statement for arbitrary pointwise cotangent subsets is a separate local-model statement, with no unstated openness hypothesis.
