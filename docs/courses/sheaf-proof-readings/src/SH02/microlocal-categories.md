# SH02-MC — Categories and operations in one cotangent direction

Local identifier: `SH02-MC`.
Independently authored programme expression: CC0 1.0 Universal. Formalization: absent. The human sources identified below retain their own terms.

Directional localization permits many representatives of a single object. Applying a sheaf operation to those representatives first gives a formal system. Replacing that system by one bounded sheaf requires control of its support and of the relevant cotangent incidence. We develop the formal operations first, construct that geometric control, and then prove the representation criteria. The final morphism calculation identifies the information carried by the resulting category.

All manifolds are finite-dimensional real smooth manifolds, Hausdorff and second countable. The coefficient ring $k$ is commutative and has finite global dimension. $D^b(k_X)$ means the bounded derived category of **all** sheaves of $k$-modules. No constructibility, finite-rank, field, orientability, or compactness condition is understood. A locally closed subspace has its subspace topology. A subscript $F_Z$ means extension by zero of the restriction, whereas $R\Gamma_ZF=R\mathcal Hom(k_Z,F)$ means local cohomology with support. These are different functors. Tensor products are derived. The antipodal map is $a(x;\xi)=(x;-\xi)$. Positive homogeneity always uses $\mathbb R_{>0}$.

For any $C^\infty$ map $f:Y\to X$, put
\[
 E_f=Y\times_XT^*X,\qquad
 f_\pi(y;\xi)=(f(y);\xi),\qquad
 f_d(y;\xi)=(y;d f_y^t\xi).
\]
The relative dualizing object is $\omega_{Y/X}=f^!k_X$. Locally it is the relative orientation line shifted by $[\dim Y-\dim X]$; thus the shift in $\omega_{Y/X}\otimes f^{-1}F\to f^!F$ is fixed by this definition. We never replace $f^!$ by a shifted $f^{-1}$ without a noncharacteristic hypothesis.

**Proof inputs and source roles.** The prerequisites are the named programme constructions in the supplier table at the end: bounded sheaf operations with their actual adjunction maps; the local support tests and directional projector; proper-image, noncharacteristic and boundary estimates; and the definition, recovery and cone-stalk calculation for microlocal Hom. Every sheaf-theoretic input retains the coefficient and manifold scope stated above. The construction uses no constructible biduality theorem. The lower proofs and the precise contracts they still import remain identified in those supplier units.

The directional quotient and its pointwise Hom comparison are classical constructions of Masaki Kashiwara and Pierre Schapira. Their [*Microlocal Study of Sheaves*, Astérisque 128 (1985), §6.1, Lemma 6.1.1 and Proposition 6.1.2, printed pp. 103–105](https://www.numdam.org/item/AST_1985__128__1_0/) give an openly accessible comparison for that part of the argument. Those pages do not supply the full four-operation representability theorem proved here. Its proof below uses the two explicitly constructed cutoff caps, the tilted boundary neighborhoods and the actual denominator comparison maps.

The categorical imports are the [Stacks Project authors' localization calculus, Tag 04VB](https://stacks.math.columbia.edu/tag/04VB), and [triangulated quotient construction, Tag 05RA](https://stacks.math.columbia.edu/tag/05RA). The reading edition is the official source revision `a04446e57ec1fbc252a871afcec7752fb2807b14`{style="overflow-wrap:anywhere"}, `categories.tex` and `derived.tex`. These supply the fraction and quotient arguments, under GFDL 1.2 or later. They do not supply the microlocal estimates. The Astérisque citation gives mathematical credit; its source expression and copyright terms are distinct from the programme's CC0 dedication.

## SH02-MC-LOCAL — A category that records specified directions

Fix **any** subset $\Omega\subset T^*X$. It need not be open or conic. Let
\[
 \mathcal N_\Omega=\{F\in D^b(k_X):\operatorname{SS}(F)\cap\Omega=\varnothing\},
 \qquad \mathcal D_X(\Omega)=D^b(k_X)/\mathcal N_\Omega.
\]
An arrow is an $\Omega$-denominator when the microsupport of its cone avoids $\Omega$.

**Proposition.** $\mathcal N_\Omega$ is a thick triangulated subcategory. Denominators form a saturated multiplicative system admitting both fraction calculi. An arrow is invertible in $\mathcal D_X(\Omega)$ precisely when it is a denominator. For $G,F\in D^b(k_X)$ there are natural identifications
\[
 \operatorname{Hom}_{\mathcal D_X(\Omega)}(G,F)
 =\underset{F\xrightarrow{s}F',\ s\text{ a denominator}}{\operatorname{colim}}
       \operatorname{Hom}_{D^b(k_X)}(G,F')
 =\underset{G'\xrightarrow{t}G,\ t\text{ a denominator}}{\operatorname{colim}}
       \operatorname{Hom}_{D^b(k_X)}(G',F).
 \tag{MC.1}
\]
In the second colimit arrows between denominators are reversed before applying $\operatorname{Hom}(-,F)$. These are colimits of abelian groups over denominator categories, not colimits over a chosen sequence of neighborhoods.

**Proof.** Shifting a complex preserves its microsupport. For a triangle $A\to B\to C\to A[1]$, microsupport of any one term is contained in the union of the other two. Finally $\operatorname{SS}(A\oplus B)=\operatorname{SS}(A)\cup\operatorname{SS}(B)$, since a local-cohomology test of a direct sum is the direct sum of the two tests. These facts prove thickness. The Stacks quotient theorem applies exactly to this thick subcategory. Its kernel is this subcategory, rather than a larger saturation, because thickness was checked. Thus an arrow becomes invertible precisely when its cone lies there. The two fraction descriptions give (MC.1): the first represents $G\to F$ by $G\to F'\leftarrow F$, the second by $G\leftarrow G'\to F$. A representative becomes zero precisely when a further denominator kills it. This last assertion is the criterion we shall actually use. $\square$

A triangle with an invisible third term gives equality of the first two microsupports on $\Omega$. Any localized isomorphism is represented by denominators, so $\operatorname{SS}(F)\cap\Omega$ depends only on the localized object. In particular,
\[
 F=0\text{ in }\mathcal D_X(\Omega)
 \quad\Longleftrightarrow\quad
 \operatorname{SS}(F)\cap\Omega=\varnothing.
 \tag{MC.2}
\]

The antecedent estimate
\[
 \operatorname{supp}\mu\mathcal Hom(G,F)
 \subset\operatorname{SS}(G)\cap\operatorname{SS}(F)
\]
and exactness in each variable show that restriction of $\mu\mathcal Hom$ to $\Omega$ inverts denominators in either argument. Hence it descends to
\[
 \mathcal D_X(\Omega)^{op}\times\mathcal D_X(\Omega)\longrightarrow D^b(k_\Omega).
\]
The identification
$\operatorname{Hom}_{D^b(k_X)}(G,F)=H^0R\Gamma(T^*X;\mu\mathcal Hom(G,F))$
then induces
\[
 \operatorname{Hom}_{\mathcal D_X(\Omega)}(G,F)
 \longrightarrow H^0R\Gamma(\Omega;\mu\mathcal Hom(G,F)).
 \tag{MC.3}
\]
For example, the right fraction $(v:G\to F',s:F\to F')$ maps to the restriction of $v$ followed by the inverse of $\mu\mathcal Hom(G,s)|_\Omega$. Common refinements prove independence of the fraction. Equation (MC.3) is a comparison, with no assertion that it is an isomorphism for an arbitrary $\Omega$.

## SH02-MC-FOUR — Four microlocal operations and their variance

The quotient tells us which changes of representative are invisible. We now apply each sheaf operation to every such representative, retaining the direction of its comparison arrows.

Choose $p\in E_f$, and write $p_X=f_\pi(p)$, $p_Y=f_d(p)$. For a category $\mathcal C$ we regard a pro-object $P=(P_i)$ as the functor $A\mapsto\operatorname{colim}_i\operatorname{Hom}(P_i,A)$, and an ind-object $I=(I_j)$ as $A\mapsto\operatorname{colim}_j\operatorname{Hom}(A,I_j)$. Quotation marks on a limit denote a formal pro/ind object, not a limit claimed to exist in $\mathcal C$.

Define
\[
 \begin{aligned}
 f_{\mu,p}^{-1}F&=``\!\lim_{F'\to F}\!''\ f^{-1}F'
       &&\text{in }\operatorname{Pro}(\mathcal D_Y(p_Y)),\\
 f_{\mu,p}^{!}F&=``\!\operatorname{colim}_{F\to F'}\!''\ f^!F'
       &&\text{in }\operatorname{Ind}(\mathcal D_Y(p_Y)),\\
 f_{!,p}^{\mu}G&=``\!\lim_{G'\to G}\!''\ Rf_!G'
       &&\text{in }\operatorname{Pro}(\mathcal D_X(p_X)),\\
 f_{*,p}^{\mu}G&=``\!\operatorname{colim}_{G\to G'}\!''\ Rf_*G'
       &&\text{in }\operatorname{Ind}(\mathcal D_X(p_X)).
 \end{aligned}
 \tag{MC.11}
\]
Every indexing arrow is a denominator at its indicated point. The fraction calculus proves independence of the chosen representative of $F$ or $G$: composing with a denominator gives a cofinal denominator category, and common refinements provide the inverse identification. These constructions are not, in general, endofunctors of ordinary bounded localized categories.

## SH02-MC-ADJUNCTION — The comparison maps before representability

With the pro/ind Hom conventions just specified, there are natural identifications
\[
 \operatorname{Hom}(f_{!,p}^{\mu}G,F)
 =\operatorname{Hom}(G,f_{\mu,p}^!F),\qquad
 \operatorname{Hom}(F,f_{*,p}^{\mu}G)
 =\operatorname{Hom}(f_{\mu,p}^{-1}F,G).
 \tag{MC.12}
\]
For the first, expand the left side by (MC.11), then expand the localized Hom by the first formula (MC.1). It becomes
\[
 \operatorname{colim}_{G'\to G}\operatorname{colim}_{F\to F'}
 \operatorname{Hom}(Rf_!G',F')
 =\operatorname{colim}_{G'\to G}\operatorname{colim}_{F\to F'}
 \operatorname{Hom}(G',f^!F').
\]
Colimits commute with colimits. Applying the second formula (MC.1) to the inner denominator colimit yields the right side of (MC.12). The other adjunction follows from
$\operatorname{Hom}(F',Rf_*G')=\operatorname{Hom}(f^{-1}F',G')$
with $F'\to F$ and $G\to G'$ denominators. This derivation specifies the variance of every indexing arrow.

There are canonical comparisons
\[
 f_{!,p}^{\mu}G\longrightarrow f_{*,p}^{\mu}G,
 \qquad
 \omega_{Y/X}\otimes f_{\mu,p}^{-1}F
       \longrightarrow f_{\mu,p}^!F.
 \tag{MC.13}
\]
Their precise meaning is the compatible pro-to-ind morphism represented by
\[
 Rf_!G'\to Rf_!G\to Rf_*G\to Rf_*G^{\prime\prime},
 \qquad
 \omega_{Y/X}\otimes f^{-1}F'
   \to\omega_{Y/X}\otimes f^{-1}F
   \to f^!F\to f^!F^{\prime\prime},
\]
for $G'\to G\to G^{\prime\prime}$ and $F'\to F\to F^{\prime\prime}$. The middle arrows are the usual sheaf comparisons. Common denominator refinements prove compatibility. Once the formal objects are represented by ordinary objects these become ordinary arrows; until then (MC.13) is not a claim of an arrow between two ordinary sheaves.

<a id="SH02-MC-AMBIENT"></a>

### A common category for the comparison arrows

All filtered and cofiltered diagrams here are small in a fixed universe. For any locally small \(\mathcal C\), write \(c:\mathcal C\to\operatorname{Pro}(\mathcal C)\) for the constant pro embedding and \(\iota:\operatorname{Pro}(\mathcal C)\to\operatorname{Ind}(\operatorname{Pro}(\mathcal C))\) for the constant ind embedding. There are fully faithful embeddings

\[
\operatorname{Pro}(\mathcal C)\xrightarrow{\ \iota\ }
\operatorname{Ind}(\operatorname{Pro}(\mathcal C)),
\qquad
\operatorname{Ind}(\mathcal C)\xrightarrow{\ \operatorname{Ind}(c)\ }
\operatorname{Ind}(\operatorname{Pro}(\mathcal C)).
\tag{MC.13a}
\]

The first is fully faithful by the constant-object Hom formula. The second is fully faithful because \(c\) is, and the ind Hom formula applies its bijections to each stage before taking the prescribed colimits and limits. Both send an ordinary object to the same twice-constant object.

If \(P=(P_i)_{i\in I}\) is a pro-object with \(I\) cofiltered and \(J=(J_j)_{j\in K}\) is an ind-object with \(K\) filtered, then

\[
\operatorname{Hom}_{\operatorname{Ind}(\operatorname{Pro}(\mathcal C))}
\bigl(\iota P,\operatorname{Ind}(c)J\bigr)
=\operatorname{colim}_{j\in K}\operatorname{colim}_{i\in I^{\mathrm{op}}}
\operatorname{Hom}_{\mathcal C}(P_i,J_j).
\tag{MC.13b}
\]

Indeed the outer source is constant, so the ind Hom formula gives \(\operatorname{colim}_j\operatorname{Hom}_{\operatorname{Pro}(\mathcal C)}(P,cJ_j)\). The target of each inner Hom is constant, so the pro formula gives the second colimit. A single stage map represents a morphism, and equality is equality after common refinements in these filtered categories. This is a double **colimit** calculation; there is no exchange of an infinite limit with a colimit. It also specifies the ambient category when neither formal object is represented by an ordinary object.

For the first arrow of (MC.13), take \(\mathcal C=\mathcal D_X(p_X)\). The incoming pro-object has its canonical projection to the identity stage \(Rf_!G\), the outgoing ind-object has its structural map from the identity stage \(Rf_*G\), and the ordinary comparison lies between these stages. Their composite in (MC.13a) is exactly the first displayed stage composite. Refining an incoming denominator precomposes it, and refining an outgoing one postcomposes it, leaving its class in (MC.13b) unchanged.

For the second arrow take \(\mathcal C=\mathcal D_Y(p_Y)\). Tensoring by \(\omega_{Y/X}\) is an ordinary functor on this localization: locally this object is an invertible orientation line with the stated shift, so tensoring preserves microsupport and hence denominators. Extend that functor termwise to the pro-category, and use the identity-stage projection, the ordinary noncharacteristic comparison map, and the outgoing structural map. This gives exactly the second stage composite. The middle map exists before imposing a noncharacteristic hypothesis; that hypothesis concerns its invertibility.

Both composites are natural on ordinary arrows, by the naturality of the usual comparisons and the structural maps. The formal incoming and outgoing functors invert denominators, so this naturality identity also holds for their inverses and consequently for every roof. Thus (MC.13) is canonical and natural on localized objects. If both formal values are represented by ordinary objects, full faithfulness of the twice-constant embedding identifies it with a unique ordinary morphism. Representability alone does not make that morphism invertible. The forthcoming geometric hypotheses prove invertibility where it is asserted. \(\square\)

## SH02-MC-CUTOFF — Representatives with a prescribed directional bound

To represent the formal operations, we need two kinds of control. The next two constructions constrain cotangent directions at a fixed basepoint; the boundary-control lemma then constrains support over the target.

Fix $x_0\in X$, a proper closed convex cone $K\subset T^*_{x_0}X$, an open cone $U\subset K$, and $F\in D^b(k_X)$. Here “open cone” is open in the cotangent fiber away from its origin; a vacuous empty cone causes no difficulty. Let $W$ be a conic neighborhood, in that fiber, of $(K\cap\operatorname{SS}(F))\setminus\{0\}$.

**Refined replacement theorem.** There are $F_- ,F_+\in D^b(k_X)$ and arrows
\[
 F_-\longrightarrow F\longrightarrow F_+
\]
which are isomorphisms at every point of $U$ in the corresponding localized category, and
\[
 \operatorname{SS}(F_\pm)\cap T^*_{x_0}X\subset W\cup\{0\}.
 \tag{MC.7}
\]
These are two separately constructed replacements, not a claim that they agree globally.

If $\dim X=0$, take $F_-=F_+=F$. If $U$ is empty, take $F_-=F_+=0$. In the remaining case $K$ has nonempty interior. We give the incoming construction first. Work in a vector-space chart with $x_0=0$. First enlarge $K$ to a proper closed convex cone $K_1$ such that $K\setminus\{0\}\subset\operatorname{Int}K_1$ and
$K_1\cap\operatorname{SS}(F)\cap(T^*_{0}X\setminus0)\subset W$.
Such an enlargement exists: otherwise compactness of the unit sphere would produce a limiting direction in $K\cap\operatorname{SS}(F)$ outside the open set $W$. A strictly positive linear functional on $K\setminus0$ realizes the enlargement by a small thickening of a compact convex section, keeping it proper. Choose a full-dimensional proper convex cone $\gamma$, with $C^1$ boundary away from its vertex, so that
\[
 K\setminus\{0\}\subset\operatorname{Int}C,
 \qquad C=(\gamma^\circ)^a\subset K_1.
\]
Here and below $\gamma^\circ$ denotes the nonnegative polar. To obtain the smooth cone, take a bounded section of the dual cone between the two strict inclusions, approximate its convex gauge uniformly by smoothing with a nonnegative mollifier, and add a small positive quadratic term on the section before taking its level set. Convexity and strict convexity are preserved; choosing both errors smaller than the gap preserves the inclusions. Homogenizing this section gives the required cone. In one dimension take a half-line directly. This construction uses the enlarged cone only inside the prescribed $W$-control; it does not presume a gap between $U$ and the boundary of the original $K$. Use coordinates $(z,t)$ with $\gamma=\{t\ge h(z)\}$, where $h$ is positive, homogeneous, convex, and $C^1$ away from $0$. The linear coordinate $-t$ is strictly negative on $\gamma\setminus\{0\}$.

Closedness of microsupport on a compact section of $C$ gives a neighborhood $B$ of $0$ such that every direction in that cone occurring in $\operatorname{SS}(F)$ over $B$ lies in $W$. To see this, a failure gives basepoints tending to $0$ and unit covectors outside $W$; a convergent unit-covector subsequence would lie in $K_1\cap\operatorname{SS}(F)$ outside $W$. Choose $\varepsilon>0$ so that $\gamma\cap\{t\le\varepsilon\}\subset B$.

**A smooth cap with tangential contact.** Choose $0<a<2\varepsilon/3$. There is a smooth positive bounded function $\theta:[0,\infty)\to(0,\varepsilon)$, constant near $0$, such that $\theta(s)=s$ only at $s=a$ and $\theta'(a)=1$. For completeness, away from a small interval near $0$ use
\[
 \theta(s)=a+\frac{a^2(s-a)}{a^2+(s-a)^2}.
\]
It lies between $a/2$ and $3a/2$, and $\theta(s)-s=-(s-a)^3/(a^2+(s-a)^2)$. Near $0$ splice it to a positive constant using a smooth cutoff supported where both functions are strictly greater than $s$; the splice introduces no further equality. Set
\[
 Z=\{(z,t):t\le\theta(h(z))\}.
\]
The function $\theta\circ h$ is smooth near $z=0$ because it is constant there, and is $C^1$ elsewhere. Thus $\partial Z$ is $C^1$, $0\in\operatorname{Int}Z$, and $Z\subset\{t\le\varepsilon\}$. At any intersection with $\partial\gamma$, $h(z)=a$ and $d(\theta\circ h)=dh$. The inward normal rays of $Z$ and $\gamma$ are opposite. This explicitly constructs the cap used below.

Define, with $s(x,y)=x-y$ and projections $q_i$,
\[
 F_-=R q_{2*}\bigl(s^{-1}k_\gamma\otimes q_1^{-1}R\Gamma_ZF\bigr).
 \tag{MC.8}
\]
The kernel is the ordinary cone cutoff $\phi_\gamma^{-1}R\phi_{\gamma*}$, so restriction of $k_\gamma$ to its vertex and $R\Gamma_ZF\to F$ give $F_-\to F$. The antecedent cutoff theorem says this is an isomorphism on $\operatorname{Int}Z\times\operatorname{Int}(\gamma^\circ)^a$ and gives
$\operatorname{SS}(F_-)\subset X\times(\gamma^\circ)^a$.

The projection $q_2$ is proper on the kernel support: if $y$ remains in a compact set, then $x-y\in\gamma$ and $x\in Z$ force an upper bound on the $t$-coordinate of $x-y$. Properness of $\gamma$ then bounds every coordinate of $x-y$, hence of $x$. The relevant set is closed, so it is compact over compact $y$-sets. Tensoring in (MC.8) causes no hidden transversality problem: a covector of $s^{-1}k_\gamma$ is of the form $(\alpha,-\alpha)$, while one of $q_1^{-1}R\Gamma_ZF$ is $(\beta,0)$. Cancellation of both components forces $\alpha=\beta=0$. Thus the noncharacteristic tensor estimate and proper direct-image estimate apply.

For a nonzero $\xi\in\partial(\gamma^\circ)^a$ with $(0;\xi)\in\operatorname{SS}(F_-)$ those estimates give $x$ with
\[
 (x;\xi)\in\operatorname{SS}(k_\gamma)^a\cap\operatorname{SS}(R\Gamma_ZF).
 \tag{MC.9}
\]
Here $x\in\gamma\cap Z\subset B$. If $x\in\operatorname{Int}Z$, the second complex agrees with $F$ near $x$. If $x\in\partial Z$, the inward conormal of $Z$ is the ray $\mathbb R_{\ge0}\xi$. Local support in this closed set adds its opposite ray. Suppose $(x;\xi)\notin\operatorname{SS}(F)$. This is precisely the noncharacteristic condition needed for the local-support estimate at that smooth boundary, and it yields
\[
 \operatorname{SS}(R\Gamma_ZF)\cap T_x^*X
 \subset \operatorname{SS}(F)\cap T_x^*X+\mathbb R_{\le0}\xi.
\]
Membership of $\xi$ would therefore imply $(1+c)\xi\in\operatorname{SS}(F)$ for some $c\ge0$, contradicting positive homogeneity. Hence (MC.9) implies $(x;\xi)\in\operatorname{SS}(F)$ and so $\xi\in W$. Interior directions of the polar cone are already controlled by the cutoff comparison, because at such directions $F_-$ agrees microlocally with $F$. This proves (MC.7) for $F_-$.

## SH02-MC-DUAL-CUTOFF — The outgoing replacement without a duality finiteness assumption

Let $\gamma$ be any closed proper convex cone with nonempty interior; no boundary regularity is required in this section. For compactly supported $H\in D^b(k_X)$ put
\[
 T_\gamma H
 =Rq_{2*}R\Gamma_{s^{-1}(\gamma^a)}(q_1^!H)
 =Rq_{2*}R\mathcal Hom(s^{-1}k_{\gamma^a},q_1^!H).
 \tag{MC.10}
\]
The diagonal kernel represents $H$. Restricting $k_{\gamma^a}$ to $k_{\{0\}}$ and applying contravariant internal Hom gives the natural arrow
\[
 H\simeq Rq_{2*}R\mathcal Hom(k_\Delta,q_1^!H)
 \longrightarrow T_\gamma H.
\]
Compactness of $\operatorname{supp}H$ makes $q_2$ proper on the support of this internal Hom. The ordinary cutoff applied to the vertex sheaf says that $\operatorname{SS}(k_{\gamma^a})\subset X\times(\gamma^\circ)^a$, and its restriction to the vertex is an isomorphism over $\operatorname{Int}(\gamma^\circ)^a$. In the internal-Hom estimate the first factor is antipodal. Since $s$ contributes $(\alpha,-\alpha)$ and the second factor contributes $(\beta,0)$, the same component argument excludes nonzero cancellation. It follows that
\[
 \operatorname{SS}(T_\gamma H)\subset X\times(\gamma^\circ)^a,
\]
and applying that argument to the cone of the kernel restriction shows that $H\to T_\gamma H$ is an isomorphism over the interior of this cone. This proves the dual cutoff lemma directly; no identification $H\simeq DDH$ is used.

### SH02-MC-DUAL-REFINED — Completing the outgoing construction

Choose a compact neighborhood $L$ of $0$ and replace $F$ by $F_L$ using $F\to F_L$. This arrow is an isomorphism on $\operatorname{Int}L$. Shrink the neighborhood $B$ used in the incoming proof inside $\operatorname{Int}L$, and henceforth write $H=F_L$. There will be no contribution from the artificial boundary of $L$ in the calculation at $0$.

With $\gamma=\{t\ge h(z)\}$ as above put $r(z)=h(-z)$. Then
\[
 \gamma^a=\{t\le-r(z)\},\qquad
 Z_+=\{t\ge-\theta(r(z))\},
 \qquad F_+=T_\gamma(H_{Z_+}).
\]
Use a sufficiently small cap parameter that $\gamma^a\cap Z_+\subset B$. The set $Z_+$ contains $0$ in its interior, and $H_{Z_+}$ has compact support. The natural composite
$F\to H\to H_{Z_+}\to F_+$ is an isomorphism at the directions in $U$ by the dual cutoff. Its global bound is $\operatorname{SS}(F_+)\subset X\times C$.

Here is the boundary calculation with all signs retained. The internal-Hom estimate applied to (MC.10), followed by the proper direct-image estimate, says that a nonzero $(0;\xi)\in\operatorname{SS}(F_+)$ has a witness $x\in\gamma^a\cap Z_+$ with
\[
 (x;\xi)\in\operatorname{SS}(k_{\gamma^a})
                 \cap\operatorname{SS}(H_{Z_+}).
 \tag{MC.10a}
\]
Indeed the kernel covector $s^{-1}k_{\gamma^a}$ is $(\alpha,-\alpha)$; internal Hom reverses it to $(-\alpha,\alpha)$. Adding $(\beta,0)$ and killing the first component gives $\beta=\alpha=\xi$. This also proves the required noncharacteristic condition for the two factors: cancellation before the estimate would force both components to vanish.

For $\xi$ on the boundary of $C$, if $x\in\operatorname{Int}Z_+$ then $H_{Z_+}=F$ near $x$. At a cap contact $r(z)=a$, the inward conormal of $\gamma^a$ is $-dt-dr$, and that of $Z_+$ is $dt+dr$. Thus the second is the ray $\mathbb R_{\le0}\xi$. If $\xi$ is absent from $\operatorname{SS}(F)_x$, extension by zero to this closed set is noncharacteristic for $F$ at $x$, and its boundary estimate yields
\[
 \operatorname{SS}(H_{Z_+})_x
 \subset\operatorname{SS}(F)_x+\mathbb R_{\le0}\xi.
\]
Equation (MC.10a) would then force $(1+c)\xi\in\operatorname{SS}(F)_x$ for some $c\ge0$, a contradiction. Hence $\xi$ belongs to $\operatorname{SS}(F)_x$, and the choice of $B$ puts it in $W$. In the interior of $C$, the dual cutoff already identifies the replacement with $F$ at the basepoint. This proves (MC.7) for $F_+$ without assuming that biduality is an isomorphism for arbitrary sheaves. $\square$

## SH02-MC-TILTED — Removing boundary contributions from a direct image

The following elementary construction is the geometric step behind the direct-image results. It is useful to state both boundary signs explicitly.

**Boundary-control lemma.** Let $H\in D^b(k_Y)$ and suppose
\[
 f_\pi^{-1}(p_X)\cap f_d^{-1}\operatorname{SS}(H)
                   \subset\{p\}\quad\text{near }p.
 \tag{MC.20}
\]
There are arbitrarily small open neighborhoods $V_-$ and $V_+$ of $y_0$, with closures proper over a sufficiently small neighborhood of $x_0$, such that
\[
 \begin{split}
 f_\pi^{-1}(p_X)\cap f_d^{-1}\operatorname{SS}(H_{V_-})&\subset\{p\},\\
 f_\pi^{-1}(p_X)\cap f_d^{-1}\operatorname{SS}(R\Gamma_{V_+}H)&\subset\{p\}.
 \end{split}
 \tag{MC.21}
\]
If the left side of (MC.20) is empty near $p$, both right sides in (MC.21) can be replaced by the empty set. Moreover the same boundary exclusion holds for the cones of $H_{V_-}\to H$ and $H\to R\Gamma_{V_+}H$, wherever the original incidence is absent outside these neighborhoods.

**Proof.** Use coordinates with $y_0=0$, $x_0=0$, $p_X=(0;\xi_0)$, and write $A_y=d f_y^t\xi_0$. Choose $r>0$ so small that
\[
 f(y)=0,\quad 0<|y|\le2r
       \quad\Longrightarrow\quad (y;A_y)\notin\operatorname{SS}(H).
 \tag{MC.22}
\]
This follows from (MC.20), because $y\mapsto(y;\xi_0)$ approaches $p$. On the compact intersection of $f^{-1}(0)$ with $|y|=r$, closedness gives $\delta>0$ such that
\[
 (y;A_y+\eta)\notin\operatorname{SS}(H)
       \quad\text{for }|\eta|\le2\delta.
 \tag{MC.23}
\]
If this sphere misses the fibre, the condition is vacuous. Set, within the coordinate chart,
\[
 \begin{aligned}
 \rho_-(y)&=\langle f(y),\xi_0\rangle+\delta r-\delta|y|,
 &V_-&=\{\rho_->0\},\\
 \rho_+(y)&=-\langle f(y),\xi_0\rangle+\delta r-\delta|y|,
 &V_+&=\{\rho_+>0\}.
 \end{aligned}
 \tag{MC.24}
\]
After restricting the target so that $|\langle f(y),\xi_0\rangle|<\delta r/2$, both closures lie inside $|y|\le3r/2$. They are closed there and hence proper over this smaller target. On $f^{-1}(0)$ their boundary is exactly $|y|=r$, and both contain $0$. Taking $r$ arbitrarily small gives neighborhood systems. The norm need not be smooth at $0$, which is an interior point. At a boundary point in $\operatorname{supp}(H)$, (MC.23) implies $d\rho_\pm\ne0$: otherwise $A_y$ differs from zero by a vector of length $\delta$, contradicting that the zero covector belongs to microsupport over the closed support. Thus the boundary is smooth wherever it matters. Outside this support the complex vanishes in a neighborhood.

At a fibre-boundary point write $n=y/|y|$. The inward normal of $V_-$ is $A_y-\delta n$. Equation (MC.23) excludes that entire positive ray from $\operatorname{SS}(H)$, by conicity. The noncharacteristic extension estimate applies and gives
\[
 \operatorname{SS}(H_{V_-})_y
       \subset\operatorname{SS}(H)_y
                    +\mathbb R_{\ge0}(-A_y+\delta n).
\]
If $A_y$ belonged to the left side, there would be $\eta\in\operatorname{SS}(H)_y$ and $c\ge0$ with
\[
 \eta=(1+c)A_y-c\delta n.
\]
Dividing by $1+c$ contradicts (MC.23). For $R\Gamma_{V_+}H$, local support in an open set adds its inward normal ray, which here is $-A_y-\delta n$. The noncharacteristic condition is the absence of its opposite ray, again supplied by (MC.23). The same calculation now gives
\[
 \eta=(1+c)A_y+c\delta n,
\]
and the same contradiction. On the interior of either neighborhood the complex is $H$, and outside its closure it is zero. This proves (MC.21), including the empty-incidence case.

For the incoming comparison its cone is $H_{Y\setminus V_-}$, where the complement is closed. Its boundary extension adds the inward normal of that closed complement, namely $-A_y+\delta n$, the ray already excluded. For the outgoing comparison the cone is $R\Gamma_{Y\setminus V_+}H[1]$. Local support in this closed complement adds the opposite of its inward normal, namely $-A_y-\delta n$. Thus both comparison cones have no new incidence at the boundary. Away from the boundary they either vanish or agree with $H$. This proves the last assertion. All these arguments remain valid when $\xi_0=0$; (MC.23) then says that the complex vanishes near the relevant boundary. $\square$

## SH02-MC-PULL-REP — When microlocal inverse images are ordinary objects

We can now apply the geometric constructions to the two cotangent maps. Inverse images require isolation in a fibre of the transpose differential; direct images require isolation over the target covector. The proofs keep these fibres separate.

Let $p=(y_0;\xi_0)\in E_f$, $p_X=f_\pi(p)$ and $p_Y=f_d(p)$. A condition stated “near $p$” concerns an actual neighborhood in $E_f$, not the entire fibre of either map.

**Theorem.** Suppose $F\in\mathcal D_X(p_X)$ has a representative satisfying
\[
 f_d^{-1}(p_Y)\cap f_\pi^{-1}\operatorname{SS}(F)
       \subset\{p\}\quad\text{near }p.
 \tag{MC.14}
\]
Then the pro-object $f_{\mu,p}^{-1}F$ and the ind-object $f_{\mu,p}^{!}F$ are represented by objects of $\mathcal D_Y(p_Y)$. Their canonical comparison is an isomorphism
\[
 \omega_{Y/X}\otimes f_{\mu,p}^{-1}F
             \xrightarrow{\sim} f_{\mu,p}^{!}F.
 \tag{MC.15}
\]
For every neighborhood $W$ of $p$, a representative of the microlocal inverse image can be chosen so that, near $p_Y$,
\[
 \operatorname{SS}(f_{\mu,p}^{-1}F)
 \subset f_d\bigl(W\cap f_\pi^{-1}\operatorname{SS}(F)\bigr).
 \tag{MC.16}
\]
This is an estimate of germs: an arbitrary global representative can acquire unrelated microsupport away from $p_Y$.

There is a useful sufficient condition for using the original sheaf itself. If $F\in D^b(k_X)$, $f$ is noncharacteristic for $F$, and
\[
 f_d^{-1}(p_Y)\cap f_\pi^{-1}\operatorname{SS}(F)\subset\{p\}
 \tag{MC.17}
\]
on the entire fibre, then
\[
 f_{\mu,p}^{-1}F\simeq f^{-1}F,\qquad
 f_{\mu,p}^{!}F\simeq f^!F
 \quad\text{in }\mathcal D_Y(p_Y).
 \tag{MC.18}
\]
Noncharacteristic means that $f_\pi^{-1}\operatorname{SS}(F)$ meets $\ker f_d$ only in zero covectors. The proof uses the antecedent noncharacteristic theorem in its full form: the canonical arrow $\omega_{Y/X}\otimes f^{-1}F\to f^!F$ is an isomorphism, and both microsupports lie in $f_df_\pi^{-1}\operatorname{SS}(F)$.

**Proof.** We may work in base charts about $y_0,x_0=f(y_0)$, since restriction to a smaller base neighborhood is a denominator at the specified covector. If $p_X\notin\operatorname{SS}(F)$, then $F=0$ in the source localization and all formal images are zero. If $p_X$ is zero and belongs to microsupport, (MC.14) excludes every nonzero characteristic covector at $y_0$: scaling it towards zero would contradict isolation. This exclusion persists near $y_0$. Otherwise a sequence of characteristic covectors at basepoints tending to $y_0$, normalized to length one in a chart, would have a characteristic limit at $y_0$ by closedness of microsupport and continuity of the transpose differential. Thus the original sheaf is noncharacteristic locally, and (MC.17) holds. This reduces the zero-covector case to the argument for good representatives below. If $p_X\ne0$ and lies in microsupport, (MC.14) implies $p_Y\ne0$, because otherwise positive multiples of $p$ would give distinct points of the same incidence fibre arbitrarily close to $p$.

Assume now both covectors are nonzero, and put $A=d f_{y_0}^t$. Choose a narrow proper closed convex cone $K$ around $\xi_0$ with $K\cap\ker A=\{0\}$. It can be chosen so that
\[
 K\cap A^{-1}(p_Y)\cap\operatorname{SS}(F)_{x_0}
                   \subset\{\xi_0\}.
 \tag{MC.19}
\]
Here $p_Y$ denotes its fibre coordinate. To justify the passage from local isolation to (MC.19), a compact unit section of a sufficiently narrow $K$ has $|A\xi|\ge c|\xi|$. Covectors in $K\cap A^{-1}(p_Y)$ are therefore bounded, while their direction approaches that of $\xi_0$ as the cone narrows. Their only possible limit is $\xi_0$, since $A\xi_0=p_Y\ne0$. The neighborhood in (MC.14) then excludes every other incidence.

Choose an open cone about $\xi_0$ inside $K$. The incoming refined replacement provides $F_-\to F$ with microsupport at $x_0$ contained in a sufficiently small conic neighborhood of $K\cap\operatorname{SS}(F)_{x_0}$. Choose this neighborhood to miss $\ker A\setminus0$ and to meet $A^{-1}(p_Y)$ only within the open cone on which the replacement agrees with $F$. Then $F_-$ is noncharacteristic near $y_0$ and satisfies (MC.17). These are open consequences of the fibre assertions: normalize a purported sequence of characteristic covectors, and use compactness of unit covectors to obtain a forbidden limit at $y_0$. The outgoing replacement produces $F\to F_+$ with the same two properties. Call such representatives good.

Good incoming representatives are cofinal among all incoming denominators. Indeed, apply the same construction to the domain of any denominator; microsupports coincide near $p_X$. Common refinements can in turn be made good by one more cutoff. The analogous statement holds for outgoing denominators. If $F^{\prime\prime}\to F'$ is a denominator between two good representatives, its cone $C$ is noncharacteristic and has
\[
 f_d^{-1}(p_Y)\cap f_\pi^{-1}\operatorname{SS}(C)=\varnothing.
\]
The triangle estimate gives noncharacteristicity, while the only possible incidence is $p$, which the denominator excludes. The noncharacteristic inverse-image estimate therefore makes $f^{-1}C$ and $f^!C$ zero at $p_Y$. Thus every transition between good representatives induces an isomorphism after either inverse operation. A filtered diagram whose transition arrows are all isomorphisms represents an ordinary object in the formal pro or ind category. This proves representability and (MC.18) whenever the original representative is good.

The composite $F_-\to F\to F_+$ is itself a denominator between good representatives. Apply the natural noncharacteristic comparison to its two ends. The resulting commutative square identifies (MC.13) with an isomorphism, proving (MC.15) for that canonical map, not merely an abstract isomorphism of objects.

Finally fix $W$. In the preceding construction choose the cone and its microsupport neighborhood sufficiently narrow that all covectors mapping near $p_Y$ lie in $W$ and in a region where the cutoff agrees with $F$. This is possible by the bound $|A\xi|\ge c|\xi|$ and (MC.19). After a base shrink the same bound holds for $d f_y^t$. Consequently its restriction to the relevant closed conic microsupport is proper over a small target cotangent neighborhood: a bounded output has bounded input, and the base is already in a compact chart. Any sequence violating the required confinement has a limit in the forbidden part of the incidence fibre. There the original and replacement microsupports agree, and the noncharacteristic inverse-image estimate gives (MC.16). In the zero-covector case the same normalization argument follows from noncharacteristicity, with the sole lift equal to zero. $\square$

## SH02-MC-DIRECT-GERMS — Direct images use the germ at the chosen basepoint

For any $G\in\mathcal D_Y(p_Y)$ there are canonical formal isomorphisms
\[
 \begin{split}
 f_{!,p}^{\mu}G
 &\simeq``\!\lim_{V\ni y_0}\!''\,Rf_!(G_V)
  \simeq``\!\lim_{K\ni y_0}\!''\,Rf_!R\Gamma_KG,\\
 f_{*,p}^{\mu}G
 &\simeq``\!\operatorname{colim}_{V\ni y_0}\!''\,Rf_*R\Gamma_VG
  \simeq``\!\operatorname{colim}_{K\ni y_0}\!''\,Rf_*(G_K).
 \end{split}
 \tag{MC.25}
\]
Here $V$ ranges over open neighborhoods and $K$ over closed neighborhoods. They can be taken relatively compact. No incidence or proper-support hypothesis on $G$ is imposed. The limits remain formal; (MC.25) does not take a sheaf-theoretic limit of these bounded complexes.

**Proof.** The arrows $G_V\to G$ are denominators at $p_Y$. If $G'\to G$ is any denominator with cone $C$, then $p_Y\notin\operatorname{SS}(C)$. By continuity of $f_d$ and closedness of microsupport, the incidence of $C$ is empty near $p$. The boundary-control lemma supplies arbitrarily small $V$ for which $Rf_!C_V$ is zero at $p_X$, by the proper direct-image estimate. Consequently
\[
 Rf_!(G'_V)\longrightarrow Rf_!(G_V)
\]
is an isomorphism in $\mathcal D_X(p_X)$. This proves formal cofinality after applying $Rf_!$: in the diagram indexed jointly by denominators and neighborhoods, the map which forgets the denominator is an isomorphism eventually for each denominator. Expanding Hom from the pro-object turns that assertion into equality of filtered colimits of abelian groups, with the zero criterion and common refinements from (MC.1). This establishes the first formula without falsely asserting that base-neighborhood restrictions are cofinal among all microlocal denominators before applying $Rf_!$.

For $G\to G'$ use its cone and the second construction of the boundary-control lemma. The maps
$Rf_*R\Gamma_VG\to Rf_*R\Gamma_VG'$ are eventually isomorphisms at $p_X$. Expanding Hom into the ind-object proves the third formula in (MC.25).

The closed-neighborhood versions are interleaved with the open ones. For $V\subset K$ there are natural arrows
\[
 G_V\to R\Gamma_KG,\qquad G_K\to R\Gamma_VG;
\]
for $K\subset V$ there are natural arrows
\[
 R\Gamma_KG\to G_V,\qquad R\Gamma_VG\to G_K.
\]
They are the localization and restriction maps, and their composites are the transition maps after choosing nested neighborhoods. A manifold has arbitrarily small closed neighborhoods inside any open neighborhood and open neighborhoods inside any closed neighborhood of the point. These interleavings induce the two remaining formal isomorphisms. $\square$

## SH02-MC-DIRECT-REP — Isolated incidence and proper support

**Theorem.** Suppose $G\in\mathcal D_Y(p_Y)$ satisfies
\[
 f_\pi^{-1}(p_X)\cap f_d^{-1}\operatorname{SS}(G)
                      \subset\{p\}\quad\text{near }p.
 \tag{MC.26}
\]
Then $f_{!,p}^{\mu}G$ and $f_{*,p}^{\mu}G$ are represented by objects of $\mathcal D_X(p_X)$, and their canonical comparison is an isomorphism. For every neighborhood $W$ of $p$, their common representative can be chosen with
\[
 \operatorname{SS}(f_{!,p}^{\mu}G)
 \subset f_\pi\bigl(W\cap f_d^{-1}\operatorname{SS}(G)\bigr)
                     \quad\text{near }p_X.
 \tag{MC.27}
\]
If the original sheaf $G\in D^b(k_Y)$ has support proper over $X$ and the incidence condition in (MC.26) holds on the entire fibre $f_\pi^{-1}(p_X)$, then the canonical identifications are
\[
 f_{!,p}^{\mu}G\simeq f_{*,p}^{\mu}G\simeq Rf_*G\simeq Rf_!G
                       \quad\text{in }\mathcal D_X(p_X).
 \tag{MC.28}
\]
Properness and the entire-fibre condition are separate hypotheses here.

**Proof.** First assume these latter two hypotheses. Choose $V_-$ from the boundary-control lemma. The cone of $G_{V_-}\to G$ has no incidence at $p_X$: inside $V_-$ it vanishes; outside its closure the entire-fibre hypothesis excludes incidence; and the lemma excludes its boundary contribution. Its support is contained in the proper support of $G$. Therefore the proper direct-image estimate makes
\[
 Rf_!(G_{V_-})\longrightarrow Rf_!G
\]
an isomorphism at $p_X$. Such neighborhoods are arbitrarily small, and the maps are the actual transition comparisons of (MC.25). They prove that its pro-object is represented by $Rf_!G$. Use $V_+$ and the outgoing comparison cone in the same way to show that
$Rf_*G\to Rf_*R\Gamma_{V_+}G$ is an isomorphism at $p_X$. This proves its ind-object is represented by $Rf_*G$. Properness makes $Rf_!G\to Rf_*G$ an isomorphism, and the constructions identify it with (MC.13). This proves (MC.28) with its claimed canonical maps.

Now assume only local isolation. Apply the lemma to choose $H=G_{V_-}$ with proper support over a target neighborhood and with the entire-fibre incidence reduced to $p$. Since $H\to G$ is an isomorphism near $y_0$, it is a denominator at $p_Y$. The invariance of all formal operations under such denominators identifies the operations on $G$ with those on $H$. The already proved case applies to $H$ and gives representability and the canonical comparison isomorphism. Notice that this argument also represents the ordinary microlocal direct image by the same incoming replacement; a separate reflexive-duality argument is unnecessary.

To obtain (MC.27), choose $V_-$ inside a prescribed base neighborhood so that the part of $E_f$ above it and near $p$ lies in $W$. The sheaf $H$ agrees with $G$ near $y_0$. On the complement of a smaller neighborhood of $y_0$, its microsupport has no incidence over $p_X$, by the boundary-control lemma. Properness excludes such incidences over a sufficiently small cotangent neighborhood of $p_X$ as well: a contrary sequence has convergent basepoints in the compact support and convergent target covectors, hence a forbidden limiting incidence. The proper direct-image estimate for $H$ then has all its witnesses inside $W$, where $\operatorname{SS}(H)=\operatorname{SS}(G)$. This is (MC.27). $\square$

## SH02-MC-POINT — The complete morphism group at one point

We finish by computing morphisms in the directional category. This calculation uses the cone-projector stalk formula and the fraction zero criterion; it is independent of the representability criteria above.

**Theorem.** For $p\in T^*X$ and arbitrary $G,F\in D^b(k_X)$,
\[
 \operatorname{Hom}_{\mathcal D_X(\{p\})}(G,F)
 \xrightarrow{\sim} H^0(\mu\mathcal Hom(G,F))_p.
 \tag{MC.4}
\]
The statement also applies after shifting either argument, so it determines every graded morphism group.

Here is the precise antecedent cutoff input used in the proof. In a vector-space chart at a nonzero covector $p=(x_0;\xi_0)$, let $U$ shrink to $x_0$ and let $\gamma$ run through closed proper convex cones with $\xi_0\in\operatorname{Int}(\gamma^\circ)^a$. The cone topology map is $\phi_\gamma$. Put
\[
 Q_{U,\gamma}G=(\phi_\gamma^{-1}R\phi_{\gamma*}G_U)_U.
\]
The cutoff theorem supplies an arrow $Q_{U,\gamma}G\to G$ that is a $p$-denominator for sufficiently small choices. The microlocal-Hom stalk formula is
\[
 H^0(\mu\mathcal Hom(G,F))_p
 =\operatorname{colim}_{U,\gamma}
       \operatorname{Hom}(Q_{U,\gamma}G,F).
 \tag{MC.5}
\]
The filtered category permits simultaneous shrinking and cone refinement. Formula (MC.5) is the actual local formula imported from the microlocal-Hom unit; an assertion that ordinary sheaf stalks alone compute this group would be false.

**Proof.** Any representative of the right side of (MC.4), using (MC.5), is an arrow $Q_{U,\gamma}G\to F$. Inverting $Q_{U,\gamma}G\to G$ produces a localized morphism with the requested image. This proves surjectivity. For injectivity, first represent a localized arrow by $G'\to G$, $G'\to F$, where the first arrow is a denominator. If its image vanishes, use the isomorphism induced by $G'\to G$ on microlocal Hom to reduce to the ordinary arrow $G'\to F$. The zero criterion for the filtered colimit (MC.5) gives a further cutoff $Q_{U,\gamma}G'\to G'$ on which that ordinary arrow is zero. This cutoff is another denominator. The fraction is therefore zero by (MC.1). This explicitly clears the initial denominator; injectivity is not being checked merely on ordinary arrows out of $G$.

At $p=(x,0)$, a conic closed microsupport misses $p$ precisely when the complex vanishes in some neighborhood of $x$: its intersection with the zero section is the closed support. The denominator localization consequently has morphisms $\operatorname{colim}_{U\ni x}\operatorname{Hom}(G|_U,F|_U)$. This equals $H^0(R\mathcal Hom(G,F))_x$. The zero-section identity for microlocal Hom identifies the latter with the right side of (MC.4). $\square$

## SH02-MC-IDENTITY — A sheaf detects its own microsupport

Let $e_F$ be the section of $H^0\mu\mathcal Hom(F,F)$ obtained from $\operatorname{id}_F$.

**Corollary.** As closed supports,
\[
 \operatorname{supp}(e_F)
 =\operatorname{supp}\mu\mathcal Hom(F,F)
 =\operatorname{SS}(F).
 \tag{MC.6}
\]
In particular $p\notin\operatorname{SS}(F)$ if and only if $\mu\mathcal Hom(F,F)_p=0$.

**Proof.** The first support is contained in the second, and the second in microsupport by the support estimate. If $(e_F)_p=0$, (MC.4) says that the identity of $F$ is zero in $\mathcal D_X(\{p\})$. An object in an additive category whose identity is zero is a zero object: every arrow to or from it factors through its zero identity and is zero. Equation (MC.2) now excludes $p$ from microsupport. This proves the reverse inclusion. $\square$

The proof uses the identity in a localized category and does not assume finite-dimensional endomorphism spaces. It therefore detects infinite-rank sheaves just as well as finite-rank ones.

## SH02-MC-EXTERNAL — Multiplying localized morphisms

Let $p_X\in T^*X$, $p_Y\in T^*Y$ and $p=(p_X,p_Y)\in T^*(X\times Y)$. External derived tensor product induces a bifunctor
\[
 \mathcal D_X(p_X)\times\mathcal D_Y(p_Y)
                         \longrightarrow\mathcal D_{X\times Y}(p).
 \tag{MC.29}
\]
In particular there is a canonical bilinear map
\[
 \operatorname{Hom}_{\mathcal D_X(p_X)}(F_1,F_2)
 \times\operatorname{Hom}_{\mathcal D_Y(p_Y)}(G_1,G_2)
 \longrightarrow
 \operatorname{Hom}_{\mathcal D_{X\times Y}(p)}
             (F_1\boxtimes G_1,F_2\boxtimes G_2).
 \tag{MC.30}
\]

**Proof.** If $s:F'\to F$ is a denominator at $p_X$ with cone $C$, the cone of $s\boxtimes\operatorname{id}_G$ is $C\boxtimes G$. The product estimate
$\operatorname{SS}(C\boxtimes G)\subset\operatorname{SS}(C)\times\operatorname{SS}(G)$ excludes $p$. Thus tensoring in either argument preserves the appropriate denominators. The two localization universal properties give (MC.29). Concretely, for left fractions represented by $F_1\leftarrow F_1'\to F_2$ and $G_1\leftarrow G_1'\to G_2$, tensor the arrows to get a fraction with denominator $F_1'\boxtimes G_1'\to F_1\boxtimes G_1$. Factor this denominator into one denominator in each variable to see that it is invertible. Common refinements and additivity give a well-defined bilinear map. Associativity, composition and identities follow from the corresponding tensor identities before localization. This proves (MC.30), without claiming it is an isomorphism or that all product morphisms are decomposable. $\square$

## SH02-MC-PROBLEMS — Examples and exercises with solutions

**1. A large stalk remains visible.** Let $M$ be a nonzero $k$-module, with no finite-generation assumption, and let $F=M_{[2,\infty)}$ on the real line. Show that the positive covector $p=(2;dx)$ detects $F$, whereas $q=(2;-dx)$ does not.

**Solution.** The test $\phi(x)=x$ has $R\Gamma_{\{x\ge2\}}F=F$ near $2$, so the test stalk is $M\ne0$. The closed-half-space calculation gives $\operatorname{SS}(F)_2=\mathbb R_{\ge0}dx$; the opposite direction has a vanishing test uniformly in a small negative cone. Hence $F$ is nonzero in $\mathcal D_{\mathbb R}(p)$ and zero in $\mathcal D_{\mathbb R}(q)$. The identity section of its self microlocal Hom is nonzero at $p$ by (MC.6). No count of stalk dimensions enters the argument.

**2. Representability alone does not identify the two direct images.** Let $k$ be a nonzero field, $f:\mathbb R\to\{*\}$, $G=k_{\mathbb R}$, and $p=(0;0)\in E_f$. Compute both microlocal direct images.

**Solution.** The open intervals $V=(-r,r)$ form a neighborhood basis. Their compact cohomology is $k[-1]$, with the transition maps identified by the positive orientation of the line. Thus (MC.25) gives $f_{!,p}^{\mu}G\simeq k[-1]$. On the other side,
$R\Gamma(\mathbb R;R\Gamma_VG)=R\Gamma(V;k)=k$, with identity transition maps, so $f_{*,p}^{\mu}G\simeq k$. Both formal objects are represented, but their canonical comparison is zero: $\operatorname{Hom}_{D(k)}(k[-1],k)=\operatorname{Ext}^1_k(k,k)=0$. The incidence is the entire zero section of $\mathbb R$, which is not isolated at $0$. The sufficient isolated-incidence theorem therefore makes no false identification in this example.

**3. Properness does not select a branch.** Let $Y$ be two disjoint copies of the real line and let $f:Y\to\mathbb R$ be the identity on each component. Take one skyscraper $k_{\{0\}}$ on each component and let $G$ be their direct sum. Choose a nonzero covector $p_X=(0;dx)$ and the lift $p$ on the first component. Compare the microlocal and ordinary direct images.

**Solution.** The map is proper, but the entire incidence fibre has two points. Near the chosen $p$ it has just one. A neighborhood of its basepoint contained in the first component removes the second skyscraper, so (MC.25) gives $f_{!,p}^{\mu}G=f_{*,p}^{\mu}G=k_{\{0\}}$ in the localization at $p_X$. The ordinary direct image is $k_{\{0\}}\oplus k_{\{0\}}$. Its second summand remains visible at $p_X$ by the closed-point microsupport calculation. In particular the canonical map from the first summand to the ordinary image has a nonzero localized cone. The entire-fibre hypothesis in (MC.28) cannot be replaced by its local version.

**4. Where the orientation shift goes.** For the projection $f:\mathbb R^m\times X\to X$, let $p$ be any lift of a covector $p_X$ and let $F\in D^b(k_X)$. Identify its two microlocal inverse images.

**Solution.** The transpose differential is injective and has at most one lift of a prescribed covector at the fixed basepoint. It has zero characteristic kernel, so (MC.18) applies. Hence $f_{\mu,p}^{-1}F=f^{-1}F$ and $f_{\mu,p}^{!}F=\omega_{Y/X}\otimes f^{-1}F$. With the standard orientation, $\omega_{Y/X}=k[m]$. The second object is therefore $f^{-1}F[m]$, in the cohomological convention $H^{-m}(k[m])=k$. The first object carries no such shift.

**5. Empty directions.** Compute $\mathcal D_X(\varnothing)$ and the corresponding comparison (MC.3).

**Solution.** Every bounded sheaf belongs to the null subcategory, so the quotient is the zero category. The sheaf on the empty space has zero derived sections, and (MC.3) is the unique map $0\to0$. This agrees with the arbitrary-subset definition and requires no nonempty or conic assumption.

## SH02-MC-DEPENDENCIES — Proof suppliers and their exact use

The following table identifies the actual proof inputs. It also distinguishes the estimates used here from stronger assertions whose additional hypotheses are unnecessary for this lesson.

| Input and scope | Programme proof or identified categorical source | Use in this lesson |
| --- | --- | --- |
| Thick quotient, saturated denominators, left and right fractions, filtered Hom formulas and their zero criterion | Official Stacks `categories.tex`, the two localization-morphism colimit remarks and `lemma-what-gets-inverted`; `derived.tex`, `lemma-construct-multiplicative-system` and `lemma-kernel-quotient`, at the revision identified above | `SH02-MC-LOCAL`; denominator refinements in all four formal operations |
| Proper supports, fibre calculation, composition and base change for arbitrary module sheaves on locally compact Hausdorff spaces, with bounded-below inputs | The compact-support and proper-image proofs, (C1)–(C7), (F2)–(F6) and (D1)–(D4); [Exceptional operations](exceptional-operations.md), `SH02-EX-FOUNDATIONS` and `SH02-EX-BASECHANGE-BRIDGE` | Properness on the actual kernel support and the boundary-control constructions |
| Exceptional adjunction, its unit and counit, internal adjunction and normalized tensor comparison | [Exceptional operations](exceptional-operations.md), `SH02-EX-ADJOINT`, `SH02-EX-INTERNAL`, `SH02-EX-TENSOR` and `SH02-EX-HOM` | The diagonal internal-Hom kernel, the two adjunctions and the canonical comparison arrows |
| Finite cohomological bounds, relative orientation and bounded internal Hom for arbitrary bounded inputs | [Manifold duality](manifold-duality.md), `SH02-MD-DIMENSION`, `SH02-MD-SUBMERSION`, `SH02-MD-RELATIVE` and `SH02-MD-BOUNDED-HOM`; the globally bounded operation proof | All displayed bounded categories; the relative dimension shift in the inverse-image comparison |
| Closed conicity, closed support on the zero section, shifts and the triangle inequality | [Microsupport tests](microsupport-tests.md), `SH02-MST-TEST` and `SH02-MST-FORMAL` | Thickness, zero objects and compactness arguments; no finite-stalk hypothesis |
| Ordinary directional projector, its polar bound and the counit isomorphism on the interior polar | [Cone topology](cone-topology.md), `SH02-GAM-UNIT` and `SH02-GAM-KERNEL`; [Microsupport tests](microsupport-tests.md), `SH02-MST-CUTOFF-FORWARD` | The incoming and outgoing cutoff constructions and the pointwise morphism calculation. The proper-support and ordinary projector models are compared only after checking the indicated support condition |
| Proper-on-support direct image and submersion pullback | [Microsupport operations](microsupport-operations.md), `SH02-MO-PROPER-PUSH` and `SH02-MO-SUBMERSION` | The kernel estimates and the inverse/direct incidence bounds. Properness is imposed on support, not inferred from the smoothness of the map |
| Noncharacteristic inverse image, including its specified orientation comparison; noncharacteristic tensor and internal-Hom bounds | [Microsupport operations](microsupport-operations.md), `SH02-MO-EMBEDDING`, `SH02-MO-PULLBACK` and `SH02-MO-DIAGONAL` | The good inverse-image representatives and the two cutoff kernels. The estimates MO21–MO22 require no constructibility; the additional evaluation isomorphism MO23 is not used |
| All four open/closed extension and local-support boundary signs, including those of $F_U$ and $R\Gamma_UF$ | [Microsupport operations](microsupport-operations.md), `SH02-MO-BOUNDARY`; [Subset microsupport](subset-microsupport.md), `SH02-SUB-SMOOTH-MODELS` | Tangential cap contact, tilted neighborhoods and their comparison cones; the proof retains each normal ray explicitly |
| Bounded microlocal Hom, ordinary and zero-section recovery, and the cone-projector stalk formula on $G_U$ with neighborhood refinements | [Microlocal Hom](microlocal-hom.md), `SH02-MH-HOM`, `SH02-MH-BOUNDED`, `SH02-MH-RECOVERY`, `SH02-MH-HOM-RECOVERY` and `SH02-MH-GAMMA-STALK`; [Microsupport operations](microsupport-operations.md), `SH02-MO-MICROLOCAL-SUPPORT` | The arbitrary-subset comparison, the complete pointwise morphism group and identity detection. Only the ordinary Hom recovery is used; its compact counterpart has separate constructibility hypotheses |
| External tensor estimate for arbitrary bounded inputs | [Microsupport operations](microsupport-operations.md), `SH02-MO-EXTERNAL-TENSOR` | Descent of external products and bilinear multiplication of localized morphisms |

The directional-test suppliers in turn use [noncharacteristic deformation](noncharacteristic-deformation.md), `SH02-NCD-COMPACT-CONTINUITY`, `SH02-NCD-OPEN-UNION` and `SH02-NCD-THEOREM`. The deformation theorem uses closures before intersecting the moving increments. The microlocal-Hom suppliers retain their normal-specialization, Fourier and exact recovery-map inputs; the noncharacteristic inverse-image theorem uses those specified recovery maps to identify the orientation comparison. These are named lower dependencies, not extra finiteness assumptions on the sheaves in this lesson.

The [six-operations comparison bridge](six-operations-import-bridge.md) retains a second route through Marco Volpe's published *The six operations in topology*, under CC BY 4.0, and its separately stated bounded-recognition and coefficient imports from Jacob Lurie. Its published and arXiv editions have different source roles and terms, as stated there. That route is a comparison with the classical construction; the support, finite-resolution and adjunction proofs used above are available in the named programme units. The independently authored programme dedication does not change the terms of any referenced human work or identified adaptation.

Two routes for further work are now visible. One can study how the represented operations glue as the covector varies; pointwise representability by itself does not supply that gluing data. One can also replace isolated incidence by a geometric correspondence with positive-dimensional fibres, where compactness, properness and possible nonrepresentability must be analyzed anew. Neither route licenses identifying localized Hom over an arbitrary set with the global sections of microlocal Hom there.
