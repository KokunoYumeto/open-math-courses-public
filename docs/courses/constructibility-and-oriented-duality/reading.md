# Constructibility and oriented duality

Three lessons prove constructibility through smooth cutoffs, build constructible models in a cotangent direction, and reconstruct dualizing complexes from oriented simplices. Twenty-two exercises have complete solutions.

- [Constructibility through smooth cutoffs and microlocal properness](constructibility-through-smooth-cutoffs-and-microlocal-properness.html) · [editable source](src/constructibility-through-smooth-cutoffs-and-microlocal-properness.md)
- [Constructible models in one cotangent direction](constructible-models-in-one-cotangent-direction.html) · [editable source](src/constructible-models-in-one-cotangent-direction.md)
- [The dualizing complex from oriented simplices](the-dualizing-complex-from-oriented-simplices.html) · [editable source](src/the-dualizing-complex-from-oriented-simplices.md)

The proofs retain the stated sheaf-operation, microlocal localization, geometric constructibility, perfect-coefficient and finite-dimensional topology prerequisites. The general constructions allow every commutative coefficient ring of finite global dimension; nonvanishing examples specify nonzero coefficients.

The exact characteristic tensor proof, asymptotic-sum convention and microlocally proper projection proof are in these earlier lessons:

- [Characteristic estimates](providers/SH02-CHE.html#SH02-CHE-006)
- [Asymptotic sum](providers/SH02-AE.html#SH02-AE-SUM) and [projection](providers/SH02-AE.html#SH02-AE-MICROPROPER)

Download the readings, sources and build code · [Reuse terms](LICENSE.txt) · Provenance

[Further sheaf proof readings](../sheaf-proof-readings/index.html) include the linked constructibility and microlocal prerequisites with editable sources.

---

# Constructibility through smooth cutoffs and microlocal properness

A nonproper image can become constructible when its relevant part is confined to a bounded region. There are two useful forms of confinement. A real $C^1$ function can stabilize the image along its sublevels. Alternatively, a compact set of base covectors can force every contributing fibre point into one compact set. We give proofs that retain perfect coefficients in both situations, including when the smooth sublevels themselves have no subanalytic description.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Use [Constructibility from microsupport and perfect stalks](../sheaf-proof-readings/SH03-constructibility-from-microsupport-and-perfect-stalks.html), [Perfect coefficients on compact fibres](../sheaf-proof-readings/SH03-perfect-coefficients-on-compact-fibres.html), and [Perfect operations and finite microlocal coefficients](../sheaf-proof-readings/SH03-perfect-operations-and-finite-microlocal-coefficients.html). The exact current microlocal prerequisites are the bounded relative cutoff theorem, the full limiting tensor estimate, microlocally proper projection, and the cone criterion for localized isomorphisms. Their statements are specified below; their lower and transitive proofs remain explicit dependencies. The references give the classical results of Masaki Kashiwara and Pierre Schapira and freely readable accounts with their precise scopes. We prove the forward local geometric criterion here. [Constructible models in one cotangent direction](constructible-models-in-one-cotangent-direction.html) supplies its converse and the contact-equivalence application.

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

Inside $X\times D$, $C$ is zero. At a base point $(x_0,y_0)$ outside that open set, apply the bounded full tensor estimate [SH02-CHE-006](providers/SH02-CHE.html#SH02-CHE-006):

\[
 \operatorname{SS}(C)
 \subset A\widehat+\operatorname{SS}(q_2^{-1}k_{Y\setminus D}).
 \tag{24}
\]

Submersion pullback says that every covector of the second set has **zero $X$ component**. If (24) had a witness with limiting $X$ covector $(x_0;\xi_0)\in W$, write the first witness as $(x_j,y_j;\xi_j,\eta_j)\in A$. Since the other summand's $X$ component is zero, $(x_j;\xi_j)\to(x_0;\xi_0)$, also when the fibre covectors diverge and cancel. All sufficiently late first covectors lie in $\overline W$; (18) then gives $y_j\in L$. Their limiting base point $y_0$ lies in the compact closed set $L\subset D$, a contradiction. The weighted base-separation condition of [SH02-AE-SUM](providers/SH02-AE.html#SH02-AE-SUM) remains part of the full limiting-sum witness. The contradiction already follows from its base-point control and does not discard escaping covectors. This proves (23), including at zero base covectors when these lie in $W$.

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

The proof is organized around an actual factorization through a compact subanalytic neighbourhood and a retract of a perfect object. The same results are treated in Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorems 4.4.1–4.4.2, Remark 8.3.2, and Proposition 8.6.1. These sources were checked with their signed hypotheses. The relative smooth closed-sublevel cutoff used in this lesson has additional scope. Its exact closed-endpoint maps are supplied by [SH02-MO-RELATIVE-CUTOFF and its proof](../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-RELATIVE-CUTOFF), using compact-neighbourhood continuity for ordinary restriction and a supported localization argument for the opposite sign. That proof depends on the foundations named in its lesson; its theorem is not inferred from the 1985 result about nested open sets. The sandwich proof explicitly avoids treating a merely smooth sublevel as subanalytic.

A freely readable human source is Kashiwara and Schapira, [*Microlocal study of sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/) ([author-hosted PDF](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf)). Theorem 4.4.1 gives signed stabilization for nested open exhaustions with proper closed-support truncations and a closure condition on the cotangent sum. Theorem 4.4.2 uses the closure of the projection retaining the fibre point and gives both microsupport bounds and the canonical proper-to-ordinary image comparison. Remark 8.3.2 relates the first theorem to real constructibility. Our smooth-sublevel sandwich and retract argument uses the separately stated $C^1$ cutoff input, including its closed endpoint maps. Proposition 8.6.1 concerns holomorphic maps and subanalytic exhausting opens; it does not supply the extra scope of arbitrary real $C^1$ non-subanalytic sublevels.

Pierre Schapira, [*Constructible sheaves and functions up to infinity*, Lemma 2.7](https://arxiv.org/html/2012.09652v5#S2.Thmtheorem7), gives related ambient-extension criteria. It assumes a relatively compact subanalytic open embedding and a Noetherian coefficient ring of finite global dimension. This supplies context for constructible extensions; it is narrower than the arbitrary-$\Omega$ pointwise representatives used here.

The exact bounded full tensor estimate is [SH02-CHE-006](providers/SH02-CHE.html#SH02-CHE-006), and its limiting-sum witness convention is [SH02-AE-SUM](providers/SH02-AE.html#SH02-AE-SUM). The signed cutoff input is [SH02-MO-RELATIVE-CUTOFF](../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-RELATIVE-CUTOFF), including its one-sided/full-map proof; the projection input is [SH02-AE-MICROPROPER](providers/SH02-AE.html#SH02-AE-MICROPROPER), including closure and all-fibre-covector compact control; localization uses [SH02-MC-LOCAL](../sheaf-proof-readings/SH02-microlocal-categories.html#SH02-MC-LOCAL), including saturated denominators. Their lower proof dependencies remain imports. The source statements and map directions are preserved; no text from the provider lessons is reproduced here.

The direct-summand argument uses [Stacks Project, Lemma 15.76.5, Tag 066S](https://stacks.math.columbia.edu/tag/066S), perfect direct-summand closure, GFDL 1.2 or later. Its pseudo-coherence and Tor-amplitude foundations are imported rather than proved here.

The general-real cutoff image-equality comparison is recorded in the earlier cutoff lesson. The next lesson proves the reverse local isotropic criterion and the contact-equivalence application relative to their stated prerequisites. The seven solutions above are complete relative to the prerequisites specified here. The microlocal, six-operation, geometric constructibility, perfect-coefficient and localization foundations retain their own proof scopes.

The compactness step in the projection argument retains the fibre base point while discarding only its covector. The closure in the free source’s Theorem 4.4.2 is essential: enlarging a compact target set to a compact neighbourhood controls limit points as well. That control is precisely what prevents nonzero fibre covectors from escaping to a boundary in the comparison-cone argument. The all-covector hypothesis, the open target neighbourhood and both signs of the cutoff are retained. The statement for arbitrary pointwise cotangent subsets is a separate local-model statement, with no unstated openness hypothesis.

---

# Constructible models in one cotangent direction

Local isotropic control of microsupport produces a constructible model in the localized category, even when the original sheaf is arbitrary elsewhere. The construction must control every direction of its new model near the chosen base point, including directions created at a cutoff boundary. We use a polyhedral cone and a flat cap to achieve this, then extend a compactly supported model to the whole manifold. A second application shows that a constructible contact kernel preserves the pointwise perfect constructible categories in both directions.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Use [Constructibility through smooth cutoffs and microlocal properness](constructibility-through-smooth-cutoffs-and-microlocal-properness.html) for the pointwise category definition, the forward criterion and perfect microlocally proper images. The geometric operations used here are proved in [Conic subanalytic images and isotropic dimension](../sheaf-proof-readings/SH03-conic-subanalytic-images-and-isotropic-dimension.html), [Isotropic cotangent transport](../sheaf-proof-readings/SH03-isotropic-cotangent-transport-and-discrete-critical-values.html), and [Limiting cotangent sums and characteristic inverse images](../sheaf-proof-readings/SH03-limiting-cotangent-sums-and-characteristic-inverse-images.html). The contact equivalence and its actual unit/counit maps are those of [When a kernel quantizes a contact transformation](../sheaf-proof-readings/SH03-when-a-kernel-quantizes-a-contact-transformation.html).

The exact sheaf inputs are the cone projector's polar bound and counit, its ordinary kernel realization, the full bounded tensor/Hom limiting estimates, noncharacteristic tensor and proper-on-support image estimates, and saturated localized fractions. We assume these sheaf-operation and localization results. The local-model proof below uses radial saturation, a flat cap and a final compact supported localization. The contact application additionally needs the identity on microlocal endomorphisms and both actual adjunction maps; a graph-shaped correspondence alone is insufficient.

## The local criterion and its coefficient scope

Let $k$ be commutative of finite global dimension. Manifolds and maps in constructibility arguments are real analytic, Hausdorff, countable at infinity, with uniform finite dimension bounds. Inputs and all representatives are globally bounded derived objects. Tensor products are derived. Write $a(x;\xi)=(x;-\xi)$ for the antipode. Weak R-constructibility imposes the geometric condition; R-constructibility additionally requires perfect stalk complexes. No field, Noetherianity, finite-rank or orientation hypothesis is added.

For any subset $\Omega\subset T^*X$, the preceding lesson defined $D^b_{\mathrm{w\text{-}R\text{-}c}}(k_X;\Omega)$ by existence, at every $p\in\Omega$, of a globally weakly R-constructible representative isomorphic to $F$ in $D^b(k_X;p)$. It proved the forward implication of the following criterion.

**Local isotropic criterion.** An object $F\in D^b(k_X;\Omega)$ belongs to this weak constructible subcategory if and only if there is an open neighborhood $U$ of $\Omega$ with

\[
 \operatorname{SS}(F)\cap U\subset\Lambda,
 \qquad \Lambda\text{ relatively closed, subanalytic and isotropic in }U.
 \tag{1}
\]

The word isotropic on a region retains vanishing of the canonical one-form $\alpha=\sum\xi_i\,dx_i$ on the subanalytic set. This is the local restriction of the conic isotropy used by the source criterion. We now prove the converse by constructing an actual global weakly constructible model at each $p$. A geometric hypothesis alone does not imply perfect coefficients.

## A compact angular slice produces a global isotropic container

Work in analytic coordinates near $x_0$, identify $x_0=0$, and let $p_0=(0;\xi_0)$ be nonzero. Choose a small compact base ball $\overline B_1$ and a closed angular cone $C'$ around $\xi_0$ so that, with $r_0=|\xi_0|$,

\[
 \overline B_1\times\{\xi\in C':|\xi|=r_0\}\subset U.
 \tag{2}
\]

The compact slice

\[
 \Sigma=\Lambda\cap
 \bigl(\overline B_1\times C'\cap\{ |\xi|=r_0\}\bigr)
 \tag{3}
\]

is subanalytic and compact. Subanalytic subset calculus preserves $\alpha|_\Sigma=0$. Let $A$ be its nonnegative radial image together with the **whole** zero section of the coordinate vector space:

\[
 A=\{(x;s\xi):(x;\xi)\in\Sigma,\ s\geq0\}
       \ \cup\ T^*_{\mathbb R^n}\mathbb R^n.
 \tag{4}
\]

This is a closed conic subanalytic isotropic set. For closedness, a finite-covector limit of the first term has bounded $s$, since $|\xi|=r_0>0$, and compactness of $\Sigma$ provides a convergent preimage. For subanalyticity, restrict $s$ to a bounded interval over any bounded target covector neighborhood and use the proper subanalytic-image theorem. The radial map $m(s,x,\xi)=(x;s\xi)$ satisfies

\[
 m^*\alpha=s\alpha.
 \tag{5}
\]

There is no $ds$ term, since radial change leaves the base point fixed. Analytic detection of vanishing on images therefore proves isotropy of the first term. The zero section is isotropic; finite union preserves it. Adding that zero section is a deliberate containing-set enlargement, not an assertion that positive radial saturation supplies zero covectors over all base points.

Conicity of the original microsupport and (1)–(3) show that $A$ contains every original covector over $\overline B_1$ whose direction lies in $C'$. We need no initial subanalyticity of that original microsupport.

There is also a zero-covector version. If $p_0=(0;0)$, choose $r_0>0$ small and $\overline B_1$ so that the full radius-$r_0$ sphere over that base ball lies in $U$. Use all angular directions in (3). Then (4) contains the **entire** microsupport over $B_1$. The geometric criterion makes $F|_{B_1}$ weakly constructible. A compact supported localization inside $B_1$, described below, gives its global representative. In dimension zero every local bounded coefficient object is already weakly constructible; the same compact extension applies.

## A cone capped by one affine inequality

For the nonzero case choose linear coordinates $(z,t)$ with $\xi_0=-dt$. Choose full-dimensional proper closed polyhedral covector cones $C,C'$ such that

\[
 -dt\in\operatorname{Int}C,\qquad
 C\setminus0\subset\operatorname{Int}C',
 \tag{6}
\]

with the larger cone still satisfying (2). One can take the cones over two nested compact polytopes in the affine section $\xi(\partial_t)=-1$. Shrinking those polytopes around $-dt$ keeps their entire angular closures inside the available neighborhood. Put

\[
 \gamma=(C^a)^\circ,
 \qquad C=(\gamma^\circ)^a,
 \qquad Z=\{t\leq\varepsilon\},\quad\varepsilon>0.
 \tag{7}
\]

The polar is nonnegative: $v\in\gamma$ means $\xi(v)\leq0$ for every $\xi\in C$. The bipolar equality gives the middle identity. The cone $\gamma$ is closed, polyhedral and proper. Since $-dt$ lies in the interior of $C$, $t$ is strictly positive on $\gamma\setminus0$. Compactness of its unit section gives a constant $c>0$ with

\[
 |v|\leq c\,t(v)\qquad(v\in\gamma).
 \tag{8}
\]

Extend the original sheaf from its coordinate chart to $\mathbb R^n$ by ordinary open extension by zero, and continue to call that bounded object $F$. On the smaller ball in (2) it is the original sheaf and has the same controlled microsupport. With source point $x$ and output point $v$, set

\[
 G=R\Gamma_ZF,
 \qquad s(x,v)=x-v,
 \qquad
 T=Rr_{2*}\bigl(s^{-1}k_\gamma\otimes^L r_1^{-1}G\bigr).
 \tag{9}
\]

Here $r_1,r_2$ are the two projections of $\mathbb R^n\times\mathbb R^n$. The ordinary cone-kernel prerequisite identifies $T$ with the cone projector $\phi_\gamma^{-1}R\phi_{\gamma*}G$. It identifies restriction of the kernel to its vertex with the projector counit. Hence the natural arrow

\[
 T\longrightarrow R\Gamma_ZF\longrightarrow F
 \tag{10}
\]

is invertible at $p_0$: the first map is microlocally invertible in $\operatorname{Int}C$, and the second is an ordinary isomorphism near $0\in\operatorname{Int}Z$. The same prerequisite gives

\[
 \operatorname{SS}(T)\subset\mathbb R^n\times C.
 \tag{11}
\]

All objects are bounded by the stated internal-Hom and manifold-operation bounds. The coefficient in (9) has closed support inside

\[
 S=\{(x,v):x-v\in\gamma,\ t(x)\leq\varepsilon\}.
 \tag{12}
\]

Projection $S\to\mathbb R^n_v$ is proper. In fact for $v$ in a compact set, writing $x=v+w$ gives $w\in\gamma$ and $t(w)\leq\varepsilon-t(v)$; (8) bounds $w$ and therefore $x$. Closedness supplies compact inverse images. Furthermore choose $\varepsilon$ small, then an output neighborhood $O$ of zero small, so that

\[
 (x,v)\in S,\ v\in O\quad\Longrightarrow\quad x\in B_0,
 \qquad \overline B_0\subset B_1.
 \tag{13}
\]

Indeed $|x|\leq|v|+c(\varepsilon+|t(v)|)$. The strict margin between $B_0$ and $B_1$ will also contain the base points of every sufficiently late limiting witness.

## The flat boundary keeps all input directions controlled

Put $N=\operatorname{SS}(k_Z)^a$. In the interior of $Z$ it has only zero covectors; at its boundary its nonzero rays are $\lambda\,dt$ with $\lambda\geq0$. There are no covectors over the complement of $Z$. Thus the full internal-Hom estimate gives

\[
 \operatorname{SS}(G)\subset\operatorname{SS}(F)\widehat+N.
 \tag{14}
\]

We claim that, for $x\in B_0$ and nonzero $\xi\in C$,

\[
 (x;\xi)\in\operatorname{SS}(G)
 \quad\Longrightarrow\quad
 (x;\xi)\in A_Z:=A\widehat+N.
 \tag{15}
\]

In a witness for (14), write the source covector as $\sigma_j$ and the second covector as $\lambda_jdt$, permitting $\lambda_j=0$. Then

\[
 \beta_j:=\sigma_j+\lambda_jdt\longrightarrow\xi,
 \qquad
 \sigma_j=\beta_j-\lambda_jdt.
 \tag{16}
\]

Because $C\setminus0\subset\operatorname{Int}C'$, sufficiently late $\beta_j$ lie in $C'$. Both $\beta_j$ and $-dt$ lie in this convex cone, so $\sigma_j\in C'$ for every sufficiently late term, however large $\lambda_j$ becomes. The source base points tend to $x\in B_0$, and therefore lie in $B_1$ eventually. Container (4) contains these actual source covectors. The original base-separation–norm product still tends to zero; we have changed no term of that witness, only its containing set. It is consequently a witness for $A\widehat+N$, proving (15). This argument includes unbounded cancellation at the cap boundary. Inside $Z$ it reduces to the zero second covector.

The geometric limiting-sum theorem makes $A_Z$ closed, conic, subanalytic and isotropic. Introduce the global geometric sets

\[
 B_\gamma=\operatorname{SS}(s^{-1}k_\gamma),
 \qquad J=r_{1d}r_{1\pi}^{-1}A_Z,
 \qquad
 \Xi=(B_\gamma\widehat+J)\cap T^*(\mathbb R^{2n})|_S.
 \tag{17}
\]

The subanalytic polyhedron $\gamma$ has weakly constructible constant coefficients. Analytic submersion pullback makes $B_\gamma$ a closed conic subanalytic isotropic set. Ordinary inverse cotangent transport gives the same properties for $J$: its covectors have the form $(\beta,0)$ over $(x,v)$ with $(x;\beta)\in A_Z$. Limiting-sum isotropy and restriction to the closed subanalytic base set $S$ give these properties for $\Xi$ as well.

The proper direct cotangent image

\[
 L=r_{2\pi}r_{2d}^{-1}\Xi
 \tag{18}
\]

is closed, conic, subanalytic and isotropic. Here the required cotangent properness is checked on its actual incidence: a compact output set of $(v;\xi)$ determines the lifted covector $(x,v;0,\xi)$, while (12) and its properness bound $x$. The incidence is closed, so it is compact. No properness of an unconstrained projection has been assumed.

We now show that $L$ contains the nonzero microsupport of $T$ over $O$. The two factors in (9) are noncharacteristic for tensor product: a kernel covector has form $(\alpha,-\alpha)$, a source covector has form $(\beta,0)$, and their cancellation in both components forces $\alpha=\beta=0$. The noncharacteristic tensor estimate and proper-on-support image estimate therefore give, for a nonzero $(v;\xi)\in\operatorname{SS}(T)$, a common source point $x$ with

\[
 (x,v)\in S,\qquad
 (x;\xi)\in\operatorname{SS}(G),\qquad
 (x,v;-\xi,\xi)\in B_\gamma.
 \tag{19}
\]

By (11), $\xi\in C$, and by (13), $x\in B_0$ whenever $v\in O$. Formula (15) then puts $(x;\xi)$ in $A_Z$. The covector $(x,v;\xi,0)$ lies in $J$. Adding it to the final covector in (19) gives $(x,v;0,\xi)$ in the ordinary sum, hence in $\Xi$. Formula (18) gives $(v;\xi)\in L$. Zero covectors can be included by adjoining the whole output zero section. Thus

\[
 \operatorname{SS}(T|_O)\subset
 (L\cup T^*_{\mathbb R^n}\mathbb R^n)|_O.
 \tag{20}
\]

The right side is a relatively closed conic subanalytic isotropic set. The global geometric criterion on the open analytic manifold $O$ proves that $T|_O$ is weakly R-constructible.

Choose a small closed analytic ball $D_0$ with $0\in\operatorname{Int}D_0$ and $D_0\subset O$, and let $j:O\hookrightarrow X$ be the coordinate inclusion. Define

\[
 F'=j_!R\Gamma_{D_0}(T|_O).
 \tag{21}
\]

The inner object is weakly constructible by subanalytic cutoff and bounded internal-Hom closure. Its closed support is compact inside $O$, so $j$ is proper on that support. Proper weak-image closure makes $F'$ globally weakly R-constructible. The supported counit, restriction of (10), and the ordinary open-extension counit give an actual arrow $F'\to F$. Near zero, the extra supported localization is the identity, so that arrow is a $p_0$-denominator. It is the required global representative. For a zero covector use the weakly constructible restriction obtained after (5) in place of $T|_O$; its compact supported localization maps isomorphically to $F$ on an ordinary neighborhood. This finishes the converse of (1) at every point of an arbitrary $\Omega$.

The outer compact localization in (21) is essential to the global assertion. Local weak constructibility on an open set does not by itself guarantee that extension across its boundary is weakly constructible. Here the closed support lies strictly inside that open set, and the proper-image hypothesis is verified there.

## A constructible contact kernel preserves perfect local models

Let $q_1,q_2:X\times Y\to X,Y$. Retain all hypotheses of the contact-kernel equivalence theorem: a relatively closed conic graph $\Gamma$, its two homeomorphic projections, selected open regions $\Omega_X,\Omega_Y$, union containment of $\operatorname{SS}(K)$ in that graph, and the identity-induced self-microlocal-Hom isomorphism. Write the graph in physical kernel covectors as

\[
 \Gamma=\{(x,y;\xi,-\eta):(x;\xi)=\chi(y;\eta)\}.
 \tag{22}
\]

Assume additionally that $K$ is R-constructible. This implies the cohomological constructibility required by the original theorem, by the costalk/duality result. Its inverse equivalences are

\[
 \Phi_KG=Rq_{1!}(K\otimes^Lq_2^{-1}G),
 \qquad
 \Psi_KF=Rq_{2*}R\mathcal Hom(K,q_1^!F).
 \tag{23}
\]

The extraordinary inverse image in the right operator retains its orientation and dimension normalization. We do not replace it by an unshifted ordinary pullback.

First take a globally R-constructible $G$. The tensor coefficient

\[
 H=K\otimes^Lq_2^{-1}G
 \tag{24}
\]

is R-constructible. It satisfies the microlocally proper projection hypothesis over $\Omega_X$. To see this for a compact output set $T\subset\Omega_X$, choose a compact neighborhood $T'\subset\Omega_X$ of $T$. In a full tensor limiting witness for a covector of $H$ over $T$, the second factor has zero $X$ component. The kernel's $X$ covectors consequently converge to the chosen output covector and eventually lie in $T'$. The proper graph projection in (22) confines both their $Y$ base points and their complete $Y$ covectors to a compact set. In particular all limiting $Y$ base points lie in one compact set, regardless of the total $Y$ covector of $H$ or any cancellation with the second factor. This gives all-fibre-covector compact control; the compact-neighborhood argument from the previous lesson supplies the closure version of projection properness. Its perfect-image theorem makes $\Phi_KG$ pointwise R-constructible on $\Omega_X$.

Next take a globally R-constructible $F$. The coefficient

\[
 H'=R\mathcal Hom(K,q_1^!F)
 \tag{25}
\]

is R-constructible by perfect exceptional inverse image and internal-Hom closure. The full Hom estimate is

\[
 \operatorname{SS}(H')
 \subset \operatorname{SS}(K)^a\widehat+
          \operatorname{SS}(q_1^!F).
 \tag{26}
\]

The second set has zero $Y$ component, because $q_1$ is a submersion and its relative dualizing factor is invertible locally constant. Over a compact set of $Y$ output covectors, the first factor's $Y$ components therefore converge to that compact set. If the physical kernel covector is $(\xi,-\eta)$, its antipode has $Y$ component $\eta$, which is exactly the input coordinate of (22). Properness of the other graph projection confines the $X$ base points and kernel $X$ covectors. Thus (25) is microlocally proper for $q_2$ over $\Omega_Y$, for all total $X$ covectors. The ordinary-image clause of the same theorem proves pointwise perfect constructibility of $\Psi_KF$ there.

Now let $G$ have only the pointwise constructible property on $\Omega_Y$. Fix $p_X\in\Omega_X$ and set $p_Y=\chi^{-1}(p_X)$. Choose a globally R-constructible $G_{p_Y}$ isomorphic to $G$ at $p_Y$. A finite localized fraction representing this isomorphism has two denominator cones missing $p_Y$. Closedness of their microsupports gives an open neighborhood $V\subset\Omega_Y$ where both cones are invisible. The source roof therefore gives an isomorphism in $D^b(k_Y;V)$.

On $\chi(V)$ the kernel graph has no input outside $V$, and its projection is still proper. The already established kernel descent thus applies to these smaller regions. It sends both arrows of that roof to denominators and gives

\[
 \Phi_KG\simeq\Phi_KG_{p_Y}
 \quad\text{in }D^b(k_X;\chi(V)).
 \tag{27}
\]

The globally constructible-input argument after (24) supplies a global perfect constructible representative of the right side at $p_X$, through the compact fibre cutoff of the preceding lesson. Composing the two localized isomorphisms supplies such a representative for the left side. Applying the same roof argument to the inverse graph and (25) proves preservation by $\Psi_K$ for pointwise constructible inputs on $\Omega_X$.

We have proved

\[
 \Phi_K:
 D^b_{\mathrm{R\text{-}c}}(k_Y;\Omega_Y)
 \xrightarrow{\sim}
 D^b_{\mathrm{R\text{-}c}}(k_X;\Omega_X),
 \qquad\text{inverse }\Psi_K.
 \tag{28}
\]

These are full subcategories of the original localized categories. The original unit and counit are isomorphisms; after both preservation arguments their components lie in the two full subcategories and remain isomorphisms there. This proves full faithfulness and essential surjectivity, establishing the asserted restricted equivalence. Perfection came from actual constructible coefficients (24)–(25) and the compact fibre theorem, rather than from isotropy alone. All right-adjoint shifts and orientations remain in the original maps (23).

## Exercises with complete solutions

### Radial saturation retains the canonical-form equation

*Difficulty: Introductory.*

Let $\Sigma$ be a compact subanalytic subset of a radius-$r_0$ sphere bundle, with $r_0>0$ and $\alpha|_\Sigma=0$. Prove closedness and isotropy of its nonnegative radial image. Distinguish its zero section from the enlargement used in (4).

**Solution.** For $m(s,x,\xi)=(x;s\xi)$, the pullback is $m^*\alpha=s\alpha$: only the projected base differential enters, so varying $s$ adds no term. Vanishing pulls back to $[0,\infty)\times\Sigma$, and analytic image detection gives vanishing on its subanalytic image. Locally that image is subanalytic because bounded output norm bounds $s$ by the positive fixed norm $r_0$, making the relevant map proper. The same bound and compactness of $\Sigma$ give convergent preimages of every finite-covector limit; the image is closed. At $s=0$ it contains zero covectors only over the base projection of $\Sigma$. The full zero section in (4) includes the other base points deliberately; each added point has zero canonical form, and the union remains closed and isotropic.

### The cone projector replaces a point by a closed halfline

*Difficulty: Intermediate.*

Assume $k\ne0$. Take $X=\mathbb R$, $p_0=(0;-dt)$, $F=k_{\{0\}}$, $\gamma=[0,\infty)$ and $Z=(-\infty,\varepsilon]$, with $\varepsilon>0$. Compute $G,T$ in (9), the arrow (10) and its cone. Check the sign of its invisible direction.

**Solution.** The source point lies in the interior of $Z$, so $G=F$. In the kernel correspondence the source coordinate is $x=0$ and $x-v\in\gamma$ means $v\leq0$. Projection is a homeomorphism from this support to $(-\infty,0]$, so

\[
 T=k_{(-\infty,0]}.
\]

There is no fibre integration shift. Restriction to the kernel vertex is the closed-point restriction $k_{(-\infty,0]}\to k_{\{0\}}$. The open/closed triangle identifies its cone with $k_{(-\infty,0)}[1]$. The closed left halfline has negative conormal at zero; the open left halfline has positive conormal there. Consequently the cone misses $(0;-dt)$, as required. The projector has selected the negative direction of the point's full conormal. Both source and model are globally constructible in this example.

### An unbounded cap correction stays in the larger cone

*Difficulty: Intermediate.*

In covector coordinates $(a,b)$ for $(z,t)$, use

\[
 C=\{b\leq-2|a|\},\qquad C'=\{b\leq-|a|\},
 \quad \xi=(1,-2).
\]

If $\beta_j\to\xi$ and $\lambda_j\geq0$, prove that $\sigma_j=\beta_j-\lambda_jdt$ lies in $C'$ eventually. Give a genuinely divergent sequence whose base-separation–norm product tends to zero.

**Solution.** The nonzero $\xi$ belongs to the interior of $C'$, so $\beta_j=(a_j,b_j)$ eventually satisfies $b_j\leq-|a_j|$. Subtracting $\lambda_jdt$ replaces $b_j$ by $b_j-\lambda_j$, preserving that inequality for every nonnegative $\lambda_j$. Choose $\beta_j=(1+1/j,-2)$, $\lambda_j=j^2$, so

\[
 \sigma_j=(1+1/j,-2-j^2),\qquad
 \sigma_j+\lambda_jdt=\beta_j\to\xi.
\]

Place their base points at $x_j=(j^{-3},\varepsilon)$ and $z_j=(0,\varepsilon)$, respectively. The second is on the flat cap boundary. The norm of $\sigma_j$ diverges like $j^2$, while

\[
 |x_j-z_j|\,|\sigma_j|=O(j^{-1})\longrightarrow0.
\]

These are valid limiting-sum witness conditions and exhibit cancellation of unbounded covectors. This calculation is a cone/witness test; it does not assert that an arbitrary set of such first covectors is itself isotropic. In the theorem their isotropic container is constructed separately in (3)–(5).

### Zero-covector control proves weak constructibility without finiteness

*Difficulty: Intermediate.*

Over a field, let $M=\bigoplus_{j\geq0}k$ and $F=M_{\mathbb R^n}$. Verify the criterion near a zero covector and give a global weakly constructible representative. Does its geometric control force perfect coefficients?

**Solution.** The microsupport is the zero section, a closed subanalytic isotropic set, so (1) holds near any zero covector and every other covector. The original constant sheaf is already a global weakly constructible representative. Alternatively (21) applied to a compact ball gives a compactly supported weak representative mapping isomorphically to it near the chosen interior point. The stalk $M$ is infinite dimensional, so it is not perfect over the field. In particular at the zero covector no perfect model can be ordinarily locally isomorphic to this stalk. The reverse criterion asserts weak constructibility and supplies no coefficient finiteness. When $n=0$, the same example is simply a bounded coefficient module at a point, which is weakly constructible regardless of its rank.

Any denominator at a zero covector has cone vanishing on an ordinary neighborhood, because zero-section microsupport records closed support. A finite isomorphism roof at that covector therefore gives ordinary local isomorphisms. This justifies the obstruction to a perfect localized model in this example, rather than assuming that all nonzero-covector isomorphisms have that stronger ordinary meaning.

### The outer compact support avoids an accumulating boundary

*Difficulty: Advanced.*

Assume $k\ne0$. On $U=(0,1)$ take the locally finite sheaf $G=\bigoplus_{j\geq2}k_{\{1/j\}}$. Show that it is R-constructible on $U$, whereas its extension by zero to $\mathbb R$ is not weakly R-constructible. Explain the support properness gained by a cutoff inside $U$.

**Solution.** Every compact subset of $U$ contains only finitely many of the points $1/j$. They and the complementary intervals form a locally finite semianalytic stratification, with stalk $k$ at each included point and zero elsewhere. Thus $G$ is R-constructible. Its open extension still has nonzero stalks at all those points and zero stalk at zero. Its closed support is $\{0\}\cup\{1/j:j\geq2\}$, which is not locally subanalytic at zero: arbitrarily small neighborhoods contain infinitely many isolated components. The zero-section base of the microsupport of a weakly constructible sheaf is subanalytic, so this extension cannot be weakly constructible.

For the embedding $U\hookrightarrow\mathbb R$, that original coefficient support is nonproper: the inverse image of a compact interval around zero contains an accumulating sequence with no limit in $U$. A closed ball $D_0$ compactly contained in $U$ meets only finitely many points. Either its ordinary cutoff or supported cutoff has compact closed support inside $U$, and its image under the embedding is proper on that support and constructible. Formula (21) uses exactly this strict interior placement, rather than relying on unrestricted open extension of a local model.

### The identity kernel checks the adjoint orientation shift

*Difficulty: Advanced.*

On oriented lines $X=Y=\mathbb R$, let $K=k_\Delta$ for the diagonal. Compute both operators (23). Verify the physical covector sign and explain the cancellation of the exceptional shift in the right operator.

**Solution.** The diagonal conormal is $(x,x;\xi,-\xi)$, so (22) gives the identity contact map. The two graph projections are homeomorphisms. Tensoring the input pullback with $k_\Delta$ gives its closed pushforward along the diagonal; proper-support projection from that support is a homeomorphism, hence $\Phi_KG=G$.

The projection $q_1$ has an oriented one-dimensional fibre, so $q_1^!F=q_1^{-1}F[1]$. Internal Hom with $k_\Delta$ is $R\Gamma_\Delta(q_1^!F)$. The diagonal's codimension-one exceptional restriction of $q_1^{-1}F$ is $F[-1]$, with its normal orientation line; it is the noncharacteristic submanifold formula, since pullback covectors have zero second component. Its normal orientation cancels the projection's relative orientation under $q_1\Delta=\mathrm{id}$. The shift $[-1]$ cancels $[1]$, giving $R\Gamma_\Delta(q_1^!F)=\Delta_*F$. Ordinary projection then gives $\Psi_KF=F$. This uses the normalized exceptional composition; omitting the fibre shift would produce an incorrect inverse.

### A shifted identity kernel has the oppositely shifted inverse

*Difficulty: Intermediate.*

For any integer $s$, replace the identity kernel by $k_\Delta[s]$. Compute both operators, their unit/counit degrees and the effect on pointwise perfect constructibility.

**Solution.** The tensor kernel shifts the forward operator by $[s]$, so $\Phi G=G[s]$. Internal Hom is contravariant in its first argument, hence shifts the right operator by $[-s]$, giving $\Psi F=F[-s]$. Each composite has total shift zero. The actual adjunction units and counits are therefore the original identity maps under the normalized shifted identifications; there is no new degree in either composite. Both microsupport and perfect-stalk properties are invariant under shifts. A global perfect representative $G_p$ for $G$ becomes $G_p[s]$ for its forward image, and similarly with $[-s]$ for the inverse. The graph and identity-induced directional endomorphism remain unchanged.

### A constructible kernel alone need not preserve perfect local models

*Difficulty: Advanced.*

Let $k$ be a nonzero field, $X=Y=\mathbb R$, $K=k_{\{0\}\times\mathbb R}$ and $G=i_*k_{\mathbb Z}$ for the closed discrete integer inclusion $i:\mathbb Z\hookrightarrow\mathbb R$. Verify that both inputs are R-constructible. Compute $\Phi_KG$ and show that it has no perfect constructible representative at $(0;dx)$. Identify the failed contact hypothesis.

**Solution.** The kernel has constant perfect coefficient $k$ on a closed analytic submanifold. The integer support is locally finite, with perfect point stalks and zero elsewhere, so $G$ is R-constructible. Tensoring restricts the first factor to zero and leaves the discrete input in the second. Compact sections of the discrete set are finite-support tuples and have no higher cohomology. Therefore

\[
 \Phi_KG=k_{\{0\}}\otimes_k V,
 \qquad V=\bigoplus_{m\in\mathbb Z}k.
 \tag{29}
\]

This is weakly constructible, but its nonzero point coefficient is infinite dimensional. The submanifold microlocal-Hom formula gives

\[
 \bigl(\mu\operatorname{hom}(k_{\{0\}},\Phi_KG)\bigr)_{(0;dx)}=V.
\]

If a globally R-constructible representative were isomorphic there, microlocal Hom would invert that isomorphism. Its stalk would be perfect by the perfect microlocal-Hom theorem, since both inputs would be R-constructible. Over the field this contradicts infinite dimensionality of $V$ in degree zero. Hence there is no perfect constructible representative at this covector.

The kernel covectors over a nonzero $X$ normal have arbitrary $Y$ base point and zero $Y$ component. They cannot form the contact graph with proper homeomorphic projection required in (22). The inverse image of that one output covector contains the whole noncompact $Y$ line. Thus constructibility of $K$ and $G$ supplies the coefficient condition for (24), but the missing graph/properness condition prevents application of the perfect localized-image theorem. This is a failure of that hypothesis, not a counterexample to (28).

## References and proof boundaries

Masaki Kashiwara and Pierre Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985), §6.2, Proposition 6.2.2, p. 106, gives the local coefficient-object model when microsupport lies in a smooth conormal; [freely readable PDF](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf). Masaki Kashiwara, *Index theorem for constructible sheaves*, Astérisque 130 (1985), §3, Proposition 3.3, p. 198, gives the finite-dimensional field-coefficient version; [free article](https://www.numdam.org/item/AST_1985__130__193_0/). These conormal statements are useful antecedents; the general isotropic cutoff construction and perfect contact argument are supplied by the proof above and its named prerequisites.

For the contact theorem, Kashiwara and Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Theorem 6.3.4 and its proof, imposes the graph, union-of-cotangent-regions, cohomological-constructibility and identity conditions. Its Proposition 8.4.1 treats constructible contact transport. Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), §5, Theorem 5.11, is a readable statement of the contact equivalence, not a replacement for the full proof. The present proof keeps the two explicit functors, their unit and counit, and separately proves preservation of perfect coefficients by compact fibre control. The smooth-conormal models cited above alone do not prove the arbitrary isotropic local-model criterion: the complete cone-and-cap construction in this lesson is the additional argument.

The current foundation contracts are [SH02-MST-CUTOFF-FORWARD](../sheaf-proof-readings/SH02-microsupport-tests.html#SH02-MST-CUTOFF-FORWARD), [SH02-GAM-KERNEL](../sheaf-proof-readings/SH02-cone-topology.html#SH02-GAM-KERNEL), [SH02-MO-DIAGONAL](../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-DIAGONAL) and [SH02-MO-PROPER-PUSH](../sheaf-proof-readings/SH02-microsupport-operations.html#SH02-MO-PROPER-PUSH), [SH02-CHE-006](providers/SH02-CHE.html#SH02-CHE-006), [SH02-AE-MICROPROPER](providers/SH02-AE.html#SH02-AE-MICROPROPER) and its full sum witness criterion, and [SH02-MC-LOCAL](../sheaf-proof-readings/SH02-microlocal-categories.html#SH02-MC-LOCAL). The elementary projector statements include both its polar bound and its actual counit; the ordinary kernel realization includes its section/relative-contraction proof and has no arbitrary nonproper closed-fibre base-change assertion. We apply those results to the capped coefficient whose projection is proved proper in (12).

These arguments and eight solved exercises establish the local criterion and contact-preservation statements using the named prerequisites. Isotropic control yields weak constructible models; the perfect contact conclusion also uses perfect coefficient complexes and the stated graph and projection conditions. The sheaf-operation, localization and geometric prerequisites are assumed at their stated scopes.

---

# The dualizing complex from oriented simplices

The dualizing complex of a polyhedron can be written as a sheaf complex of oriented simplices. A $d$-simplex contributes in degree $-d$, with its coefficient extended to the **closed** simplex. The differential is its oriented boundary. This construction includes boundary points, branches, non-pure complexes and infinitely many locally finite simplices. Its stalks record local homology rather than merely the dimension of a simplex containing the point.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

Use [Constructible sheaves on a triangulation](../sheaf-proof-readings/SH03-constructible-sheaves-on-a-triangulation.html) for locally finite simplices, open stars, closed-simplex sheaves and the diagram/derived comparison. The exact current sheaf-operation prerequisites used here are locally closed support as internal Hom, exceptional composition, internal duality, oriented manifold dualizing objects, and constant-complex acyclicity on locally closed convex sets. The proof uses those results with their stated hypotheses. The simplicial construction is proved directly by a finite filtration of an injective complex. The two quasi-isomorphisms are constructed, rather than deduced from purity of the associated layers alone.

## The skeleton index and the support operation

Let $S$ be a locally finite simplicial complex with a uniform dimension bound $N<\infty$, and put $X=|S|$. The source's local finiteness means each vertex belongs to only finitely many simplices. No globally finite complex, pure dimension, orientability, field or Noetherian ring is assumed. Let $k$ be a commutative ring of finite global dimension. Write $\sigma^\circ$ for an open simplex, $\overline\sigma$ for its closed realization, and $d_\sigma=\#\sigma-1$.

Use the decreasing closed filtration

\[
 X_k=\bigcup_{d_\sigma\leq-k}\sigma^\circ,
 \qquad
 L_k=X_k\setminus X_{k+1}
     =\coprod_{d_\sigma=-k}\sigma^\circ.
 \tag{1}
\]

Thus $X_k=X$ for $k\leq-N$, $X_k=\varnothing$ for $k>0$, and $L_k$ is the union of the open $(-k)$-simplices. Each skeleton is closed: in a finite local subcomplex the union of the corresponding closed faces is closed, and local finiteness gives such neighborhoods everywhere. This also explains why a dimension bound, rather than a globally finite number of cells, makes the filtration finite.

For a locally closed subset $L$, use

\[
 R\Gamma_L F=R\mathcal Hom(k_L,F),
 \qquad k_L\text{ extended by zero from }L.
 \tag{2}
\]

This is a **sheaf** on $X$, not the single complex of global supported sections. A locally closed inclusion $j:L\to X$ gives
$R\Gamma_LF\simeq Rj_*j^!F$. In particular the ordinary direct image $Rj_*$ appears after exceptional restriction; replacing it by open extension by zero changes the boundary stalks.

The locally compact polyhedron has finite compact-support cohomological dimension. Indeed the finite skeleton filtration reduces compactly supported cohomology of an arbitrary sheaf to that on the disjoint open simplices; those are manifolds of dimension at most $N$. Compact support on a disjoint union gives direct sums, and local finiteness ensures each compact subset meets finitely many closed simplices. The manifold bound and the finite localization triangles give vanishing above $N$. Consequently $a_X^!k$ is defined under the existing exceptional-operation contract. Set

\[
 \omega_X=a_X^!k,\qquad D_XA=R\mathcal Hom(A,\omega_X).
 \tag{3}
\]

Initially the construction supplies a bounded-below object. The cellular model below will prove that $\omega_X$ is in fact bounded, in degrees $[-N,0]$.

## A supported layer is pure in its indexed degree

For an open $d$-simplex let $o_\sigma$ be its integral orientation line tensored with $k$. It is a constant free rank-one coefficient on that simplex, without choosing a generator. On its closed realization use the same constant line. Exceptional composition and internal duality give

\[
 D_X(k_{\sigma^\circ})
   \simeq Rj_{\sigma*}\omega_{\sigma^\circ}
   \simeq Rj_{\sigma*}(o_\sigma[d])
   \simeq k_{\overline\sigma}\otimes_k o_\sigma[d].
 \tag{4}
\]

The first identity applies internal duality with the bounded input $k_{\sigma^\circ}$ and the bounded-below target $\omega_X$; it requires no biduality assertion. The middle identity is the exact oriented manifold dualizing formula, with cohomological degree $-d$.

To verify the last identity, factor $j_\sigma$ through the closed embedding of $\overline\sigma$. A sufficiently small convex neighborhood in that closed simplex meets $\sigma^\circ$ in a nonempty locally closed convex set, at every point of $\overline\sigma$. Its constant-section map is an isomorphism on derived cohomology. The resulting ordinary image has the constant orientation line in degree zero at every such point and zero elsewhere; these identifications commute with restriction. This checks an actual natural ordinary-image map on a basis. No arbitrary nonproper fibre base change is used.

For $d=-k$, the family of closed $d$-simplices is locally finite. The extension-by-zero constant sheaf on $L_k$ is the locally finite direct sum of the $k_{\sigma^\circ}$. Internal Hom changes a direct sum to a product, but here every point has a neighborhood meeting only finitely many closed supports. On that neighborhood the product and direct sum coincide, so (2)–(4) give

\[
 R\Gamma_{L_k}\omega_X
 \simeq
 \left(\bigoplus_{d_\sigma=-k}
       k_{\overline\sigma}\otimes_k o_\sigma\right)[-k].
 \tag{5}
\]

It follows that

\[
 H^j_{L_k}(\omega_X)=0\quad(j\ne k),\qquad
 K^k:=H^k_{L_k}(\omega_X)
     =\bigoplus_{d_\sigma=-k}
        k_{\overline\sigma}\otimes_k o_\sigma.
 \tag{6}
\]

The shift $[-k]=[d]$ puts the unshifted sheaf in degree $k=-d$. This is the source purity assertion, with its supported operation and negative skeleton index retained.

## Reconstruct from a finite pure support filtration

We give the finite form of the filtered construction needed here. Let $(X_k)$ be a decreasing closed filtration equal to $X$ and to $\varnothing$ at its two ends. If a bounded-below object $F$ satisfies
$H^j_{X_k\setminus X_{k+1}}F=0$ for $j\ne k$, define $K^k$ by these degree-$k$ layer sheaves. The boundary morphisms of the localization triangles give

\[
 d_K^k:K^k\longrightarrow K^{k+1}.
 \tag{7}
\]

Then $K$ is a complex and $F\simeq K$ in the derived category. This assertion includes a reconstruction map, rather than only a collapsed spectral sequence.

**Construction and proof.** Choose a bounded-below injective resolution $I$ of $F$ and set

\[
 P^kI=\Gamma_{X_k}I,
 \qquad Q^k=P^kI/P^{k+1}I.
 \tag{8}
\]

The exact coefficient sequence
$0\to k_{L_k}\to k_{X_k}\to k_{X_{k+1}}\to0$ and injectivity show that $Q^k$ computes $R\Gamma_{L_k}F$. Thus its cohomology is concentrated in degree $k$. Every filtration is finite, including at each stalk.

Define an actual subcomplex of $I$ by

\[
 G^k=P^kI^k\cap d_I^{-1}(P^{k+1}I^{k+1}).
 \tag{9}
\]

If $x\in G^k$, then $d_Ix\in P^{k+1}I^{k+1}$ and its next differential is zero, so $d_Ix\in G^{k+1}$. The map $G\to I$ is inclusion. Send $x\in G^k$ to its cycle class in $H^k(Q^k)=K^k$ to obtain $G\to K$. In this description $d_K[x]$ is the class of $d_Ix$ in $H^{k+1}(Q^{k+1})$. Changing a lift by a boundary or an element of $P^{k+1}$ changes this class by a boundary. The same representative has $d_I^2x=0$, so $d_K^2=0$ and $G\to K$ is a chain map. This is the localization-triangle boundary (7), with the same differential convention.

Here is a direct check of both quasi-isomorphisms. All lifts may be taken at a stalk, where the cohomology of the finite filtered sheaf complexes is the cohomology of their stalk complexes. This suffices to check a sheaf quasi-isomorphism.

For $G\to I$, take a cocycle $z\in I^q$. Starting at the lowest filtration index $a<q$, if $z\in P^a$, its class in $Q^a$ is a degree-$q$ cycle. Since $H^q(Q^a)=0$, subtract a differential of an element of $P^aI^{q-1}$ to move $z$ into $P^{a+1}$. Repeat finitely to obtain a cohomologous cocycle in $P^qI^q$, hence in $G^q$. If a cocycle $z\in G^q$ is $d_Iy$ in $I$, the same argument in degree $q-1$, using $d_Iy\in P^q$, replaces $y$ by an element of $P^{q-1}I^{q-1}$ without changing its differential. That primitive is in $G^{q-1}$. These prove surjectivity and injectivity on cohomology.

For $G\to K$, lift a $K$-cycle $\alpha\in K^q$ to $x\in G^q$. The condition $d_K\alpha=0$ lets one subtract $u\in P^{q+1}I^q$ so that $d_I(x-u)\in P^{q+2}$. In all subsequent indices $a\geq q+2$, $H^{q+1}(Q^a)=0$ lets one subtract another element of $P^aI^q$ and move this differential into $P^{a+1}$. At the finite terminal index it is zero. None of these corrections changes $\alpha$, so a cocycle of $G$ lifts it.

If a cocycle $x\in G^q$ maps to a boundary $d_K\beta$, lift $\beta\in K^{q-1}$ to $y\in G^{q-1}$. The image of $x-d_Iy$ is zero in $H^q(Q^q)$, so write
$x-d_Iy=d_Iz+w$ with $z\in P^qI^{q-1}$ and $w\in P^{q+1}I^q$. Then $z\in G^{q-1}$ and $w$ is a cocycle. The vanishing $H^q(Q^a)=0$ for every $a\geq q+1$ successively makes $w$ a differential, with a primitive in $G^{q-1}$. Hence $x$ is a boundary in $G$. This proves injectivity. We obtain the explicit isomorphism roof

\[
 F\simeq I\ \longleftarrow^{\sim}\ G
                  \ \longrightarrow^{\sim}\ K.
 \tag{10}
\]

Every correction terminates because the filtration is finite. There is no infinite convergence, unbounded totalization or termwise splitting assumption. Applying this to (5) proves $\omega_X\simeq K$ and its bounded range $[-N,0]$. This completes the finite supported-filtration reconstruction. $\square$

## The differential is the oriented boundary

Choose an ordering of the vertices to name orientation generators. For
$\sigma=[v_0,\ldots,v_d]$ with $v_0<\cdots<v_d$, let
$\tau_i=[v_0,\ldots,\widehat v_i,\ldots,v_d]$. Under (6), the differential is

\[
 \partial_\sigma=
 \sum_{i=0}^d(-1)^i\,\rho_{\sigma\tau_i},
 \qquad
 \rho_{\sigma\tau_i}:
 k_{\overline\sigma}\otimes o_\sigma
       \longrightarrow
 k_{\overline{\tau_i}}\otimes o_{\tau_i}.
 \tag{11}
\]

Each $\rho_{\sigma\tau_i}$ is the closed-face restriction tensored with the unsigned identification of the ordered orientation generators. The incidence sign is the single external factor $(-1)^i$ in (11). Components to a simplex that is not a codimension-one face are zero. For $d=0$ the target degree $1$ is zero; there is no artificial empty-simplex augmentation.

To identify this with (7), localize near the interior of one codimension-one face. The open simplex is a half-collar of that face, and the connecting map is the dual of the compact-support localization boundary of this collar. In the oriented interval its generator was fixed by the difference of endpoint values $b-a$, so its dual sends the edge to terminal vertex minus initial vertex. Tensor this one-dimensional calculation with the face orientation, retaining the coordinate order. Boundary orientation is outward-normal-first; the orientation on the face opposite $v_i$ is $(-1)^i$ times its listed order. This gives exactly (11), with no additional fibre shift.

For completeness that sign is the ordinary determinant comparison: writing the simplex orientation with edge vectors based at $v_0$, the outward normal at the face opposite $v_i$ followed by that face's ordered tangent vectors has orientation $(-1)^i$ relative to the listed simplex orientation. Equivalently it is the sign in deleting the $i$th entry of the alternating ordered vertex generator. A neighborhood away from all faces has zero target; nonfaces have disjoint support there. These local identifications determine the sheaf component maps and prove (11) globally.

One can also check the complex identity directly. For a codimension-two face obtained by deleting entries $i<j$, the two routes have signs

\[
 (-1)^{i+j-1}\quad\text{and}\quad(-1)^{i+j},
 \tag{12}
\]

whose sum is zero in any coefficient ring. Their closed-face restrictions are the same map, so $\partial^2=0$. This agrees with the actual filtered proof; it is not its substitute.

Changing an orientation multiplies that simplex's generator by $-1$ and changes the adjacent incidence matrices by the corresponding basis changes. The resulting sheaf complexes are isomorphic. Keeping the lines $o_\sigma$ is an orientation-independent way to state the same object.

## Stalks are relative local chains

If $x\in\rho^\circ$, the summand $k_{\overline\sigma}\otimes_k o_\sigma$ has stalk $o_\sigma$ when $\rho\leq\sigma$ and zero otherwise. Thus the stalk complex is

\[
 K_x^{-d}=
 \bigoplus_{\substack{d_\sigma=d\\\rho\leq\sigma}}o_\sigma,
 \qquad
 \partial\text{ keeps only faces still containing }\rho.
 \tag{13}
\]

There are finitely many such cofaces. This is the relative simplicial chain complex of the closed star of $\rho$ modulo its faces not containing $\rho$, placed in negative chain degrees. It explains the local homology interpretation and works without purity. At a vertex $v$ of a cone on a finite complex $L$, it becomes the relative chain complex $(\operatorname{Cone}L,L)$, so

\[
 H^{-d}(\omega_X)_v\simeq
 \widetilde H_{d-1}(L;k),
 \tag{14}
\]

with augmented reduced-homology conventions, including an empty link at an isolated vertex. The formula follows directly by separating cone simplices from base simplices in (13): deleting the cone vertex is zero in the relative quotient; the other face maps are the link's augmented boundary maps, with a consistent shift of signs. No manifold assumption on the link is made.

## Exercises with complete solutions

### A closed interval has zero dualizing stalk at an endpoint

*Difficulty: Introductory.*

Order the vertices $v_0<v_1$ of one closed edge. Write the sheaf complex and compute all stalk cohomology groups. Compare ordinary restriction to the edge with the supported open-edge layer.

**Solution.** The complex is

\[
 k_{[v_0,v_1]}\quad\xrightarrow{\ (-\rho_0,\rho_1)\ }\quad
 k_{\{v_0\}}\oplus k_{\{v_1\}},
 \qquad\text{degrees }-1,0.
\]

At an interior point the target is zero and the source is $k$, so only $H^{-1}=k$ remains. At either endpoint the map is $-1$ or $+1$ from $k$ to $k$, hence the stalk complex is acyclic. Consequently $\omega_X$ is the open interval's orientation coefficient extended by zero and shifted by $[1]$.

Its ordinary restriction to the open edge has zero stalk at the endpoints after open extension. In contrast $R\Gamma_{(v_0,v_1)}\omega_X=k_{[v_0,v_1]}[1]$ by (5), with endpoint stalks $k$. These are the supported layer's ordinary-image boundary contributions; the next layer differential cancels them in the reconstructed object.

### A branching vertex detects the number of arms

*Difficulty: Intermediate.*

Take a finite star graph with central vertex $v$ and $m\geq1$ distinct edges to outer vertices. Orient every edge away from $v$. Compute $\omega_X$ at $v$, at the outer vertices and in edge interiors.

**Solution.** At $v$, all $m$ edge summands survive and the central vertex summand survives. The differential is
$k^m\to k$, $(a_1,\ldots,a_m)\mapsto-\sum_i a_i$. It is onto, so $H^0=0$ and
$H^{-1}=\ker(\sum)=k^{m-1}$, with an explicit basis $e_i-e_m$ for $i<m$. At an outer vertex only its one edge and that vertex remain; the map is $+1$, hence the stalk is acyclic. In an edge interior only the edge remains, giving $k$ in degree $-1$.

For $m=1$ even the central endpoint stalk vanishes. When $k\ne0$, the $m=2$ central coefficient is free of rank one, consistent with a line neighborhood, while $m=3$ gives a free rank-two coefficient that detects branching. The displayed stalk calculations hold also for the zero ring, where every coefficient vanishes.

### Non-pure complexes keep their separate degree-zero pieces

*Difficulty: Intermediate.*

Adjoin an isolated vertex $w$ disjoint from a star graph. Describe its dualizing stalk and compare it with a terminal vertex belonging to an edge. For the degree distinction assume $k\ne0$, and explain why a global shift by the maximum dimension does not describe the whole complex.

**Solution.** At $w$ there are no edge cofaces. Formula (13) leaves a single $k$ in degree zero with zero differential, so $H^0(\omega_X)_w=k$. At a terminal edge vertex there is also an edge summand in degree $-1$, and its incidence map to the vertex is an isomorphism, making that stalk zero. The same zero-dimensional simplex type therefore has different surrounding local chains.

The graph interiors have a degree-$-1$ coefficient, while the isolated point has degree zero. A single orientation local system shifted by $[1]$ would place the isolated point in the wrong degree. Formula (6) handles all dimensions together and does not assume the complex is pure.

### Triangle incidence signs cancel without dividing by two

*Difficulty: Intermediate.*

For vertices $0<1<2$, compute both differentials on the oriented triangle and show that their composite is zero. Repeat over a ring of characteristic two.

**Solution.** The first boundary is
$[12]-[02]+[01]$. Taking the next boundary gives

\[
 ([2]-[1])-([2]-[0])+([1]-[0])=0.
\]

Each vertex receives two opposite incidence routes, as in (12). The sheaf restrictions along the two routes agree. Over characteristic two the signs are both $+1$, but each repeated coefficient is $1+1=0$; the composite still vanishes. No step divides by two or uses characteristic zero. At vertex $0$, order the surviving edges as $[01],[02]$. The stalk complex is $k\to k^2\to k$ with maps $a\mapsto(a,-a)$ and $(b,c)\mapsto-b-c$. The first is injective, the second is onto, and its kernel is exactly the first image. Thus the dualizing stalk vanishes there. The other vertices give the same exact complex after changing basis, in agreement with the interval boundary mechanism.

### Local finiteness makes the infinite line a bounded sheaf complex

*Difficulty: Intermediate.*

Triangulate $\mathbb R$ with vertices $\mathbb Z$ and edges $[j,j+1]$, all oriented to the right. Explain why the infinite sums in (6) are legitimate, and compute the stalks at integer and noninteger points. Can an unrestricted product-to-stalk interchange replace local finiteness?

**Solution.** Each compact interval meets only finitely many closed edges and vertices. The sheaf complex has an infinite locally finite sum of edge coefficients in degree $-1$ and vertex coefficients in degree zero, with the usual terminal-minus-initial restrictions. At a noninteger point only one edge remains, giving $k$ in degree $-1$. At an integer $j$ the two incident edges remain; the map is $(a,b)\mapsto a-b$, which is onto with kernel the diagonal $k$. Again only degree $-1$ survives, and the diagonal identifications glue as the line orientation.

The global number of cells is infinite, but the number of terms near any point and the length of the degree interval are finite. This is exactly what makes the local product and direct sum agree in (5). General products of sheaves need not commute with stalks, so an unrestricted interchange supplies no replacement for this finite local-support argument.

### A torsion link gives torsion local dualizing cohomology

*Difficulty: Advanced.*

Let $L$ be a finite simplicial triangulation of $\mathbb RP^2$ and $X=\operatorname{Cone}L$. Compute the dualizing cohomology at its cone vertex over $\mathbb Z$ and over $\mathbb F_2$. Explain why a three-dimensional maximum does not force concentration in degree $-3$.

**Solution.** The projective plane has one cell in each dimension $0,1,2$. Its attaching loop for the two-cell traverses the one-cell twice, giving cellular differential $\mathbb Z\xrightarrow{2}\mathbb Z$ from degree two to one, and zero from degree one to zero. Thus its reduced homology over $\mathbb Z$ is $\mathbb Z/2$ in degree one and zero otherwise. Formula (14) gives
$H^{-2}(\omega_X)_v=\mathbb Z/2$, with all other groups zero.

Over $\mathbb F_2$, the multiplication-by-two boundary is zero, so the link has reduced homology $\mathbb F_2$ in degrees one and two. The cone vertex therefore has $\mathbb F_2$ in degrees $-2$ and $-3$. It is not a manifold point: its link does not have the homology of a two-sphere in either coefficient calculation. The finite cellular stalk complex has free terms over either ring, and its torsion cohomology over $\mathbb Z$ presents no failure of perfection. The geometry alone does not force local dualizing cohomology into a single maximum-dimensional degree.

### The filtered reconstruction needs a complex, not a direct sum of layers

*Difficulty: Advanced.*

Assume $k\ne0$. Use the closed interval to compare $\omega_X$ with the direct sum of its two pure layers, shifted into degrees $-1$ and zero but with zero differential. Identify the step in (9)–(10) that preserves the extension data.

**Solution.** With zero differential, the proposed direct sum has at an endpoint a $k$ in degree $-1$ and another $k$ in degree zero. The actual dualizing stalk is zero by the first solution, since the connecting incidence map is an isomorphism. Purity of the individual layers therefore does not permit splitting the filtered object.

The subcomplex $G^k$ in (9) retains representatives whose differential lands in the next support level. Their images under $d_I$ define the nonzero connecting differential on $K$. Both maps in the roof (10) preserve this differential and are proved quasi-isomorphisms by finite correction of cocycles and primitives. Dropping the differential discards the endpoint cancellation and the extension class; a collapsed collection of graded layer groups alone cannot reconstruct $F$.

## References and proof boundaries

Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), §§4.6–4.7 and §5.1, supplies the exceptional and dualizing framework and the orientation shift. The independent finite reconstruction above uses enough injectives and the stated supported-cohomology identities. Its incidence differential is checked by the outward-normal convention and the interval boundary; the two contributions at a codimension-two face cancel. The local star-and-link calculation includes singular polyhedra and integral torsion, so it cannot be replaced by an orientation-sheaf assertion valid only on manifolds.

For a freely readable antecedent, see Masaki Kashiwara, *Index theorem for constructible sheaves*, Astérisque 130 (1985), §1.3–1.5, pp. 195–196; [free article](https://www.numdam.org/item/AST_1985__130__193_0/). It constructs oriented subanalytic chain sheaves and a chain resolution of the orientation sheaf on a real analytic manifold. The arbitrary polyhedron's closed-simplex model and finite reconstruction are proved above; they are not inferred merely from that manifold statement.

The operation inputs are [SH02-EX-EMBEDDING](../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-EMBEDDING), [SH02-EX-INTERNAL](../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-INTERNAL), [SH02-EX-DUALIZING](../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-DUALIZING)/[SH02-EX-DUAL-SECTIONS](../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-DUAL-SECTIONS), [SH02-MD-EUCLIDEAN](../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-EUCLIDEAN)/[SH02-MD-ORIENTATION-LINE](../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-ORIENTATION-LINE)/[SH02-MD-SUBMERSION](../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-SUBMERSION), and [SH02-CA-CONSTANT](../sheaf-proof-readings/SH02-convex-acyclicity.html#SH02-CA-CONSTANT), with their stated coefficient and degree ranges. The sheaf model and seven solved exercises use these prerequisites. The argument requires neither unrestricted biduality nor nonproper fibre base change, arbitrary product-to-stalk interchange or reconstruction from an infinite filtration.

