# Directional neighborhoods and the compact-cap test

A compact cap detects a directional obstruction only if its cohomology comparison can be converted back into a local support test. The missing link is a sheaf that remembers continuation along a cone. We construct it, identify its actual counit, and use it to prove the converse compact-cap implication.

This is a prerequisite reading for the constructibility course. It uses the compact-support and injective constructions and the uniform forward compact-cap proof. The latter uses deformation and compact continuity proved earlier in that same lesson; it does not use this reading. These arguments in turn support the limiting boundary estimates. The companion limiting tensor proof treats arbitrary bounded coefficients over a ring of finite global dimension. The remaining geometric foundations are separate prerequisites.

*Independently written programme exposition, GPT-6 Astra (OpenAI), Ultra, October 2026; original expression is CC0. The human mathematical source is Kashiwara–Schapira, the freely accessible 1985 Astérisque volume, with exact scope described at the end.*

Let \(E\) be a finite-dimensional real vector space and \(k\) a commutative ring. The proofs here work for arbitrary \(k\)-modules; finite global dimension is not needed. Derived objects are bounded below, with no constructibility or finite-generation hypothesis. All subsets carry their ordinary subspace topology unless a directional topology is expressly specified.

## From compact extensions to acyclicity {#convex-extension-criterion}

We first prove the acyclicity statement used in passing from ordinary sections to derived sections. If \(C\subset E\) is locally closed and convex and a sheaf \(A\) on \(C\) satisfies

\[
\Gamma(C;A)\longrightarrow\Gamma(K;A|_K)
\quad\text{surjective for every compact convex }K\subset C,
\tag{D1}
\]

then \(H^q(C;A)=0\) for \(q>0\). Convexity alone is not the assertion: (D1) controls the gluing of local sections.

For a finite closed cover \(Y=Y_1\cup Y_2\), the sequence

\[
0\longrightarrow A\longrightarrow
i_{1*}(A|_{Y_1})\oplus i_{2*}(A|_{Y_2})
\longrightarrow i_{12*}(A|_{Y_1\cap Y_2})\longrightarrow0
\tag{D2}
\]

is exact. The maps are diagonal and difference of restrictions. At an intersection point this is \(0\to A_y\to A_y^2\to A_y\to0\); elsewhere only the appropriate identity remains. Closed pushforward is exact and preserves injectives, so derived sections give the associated Mayer–Vietoris sequence on this closed cover.

For a compact interval \(I\), assume first that every map \(\Gamma(I;A)\to A_t\) is onto. A positive-degree cohomology class is locally zero: represent it by an injective-resolution cocycle, which locally has a primitive by exactness of the resolution. Partition \(I\) into finitely many successive closed subintervals inside those vanishing neighborhoods. When two successive pieces are joined, their intersection is a point. In degree greater than one its preceding cohomology vanishes. In degree one the preceding difference map onto that point's stalk is surjective, because a global section realizing any prescribed germ can be restricted to the first piece and paired with zero. Thus (D2) makes restriction to the two pieces injective in every positive degree. Induction over the partition proves acyclicity of \(A\) on \(I\).

Now let \(K\) be compact convex and assume (D1) on \(K\). Induct on its affine dimension. A point is immediate. Otherwise choose an affine function \(p:K\to I=p(K)\) nonconstant on \(K\). The interval \(I\) is compact and \(p\) is proper. Every fibre is compact convex of smaller affine dimension. Its restricted sheaf satisfies (D1): extend a section on a smaller convex compact set to \(K\), then restrict to the fibre. By induction the higher fibre cohomology vanishes. The already proved compact-fibre formula therefore gives

\[
(R^q p_*A)_t=H^q(p^{-1}(t);A),\qquad
Rp_*A\simeq p_*A.
\tag{D3}
\]

The global-section evaluation of \(p_*A\) at \(t\) is the actual restriction to the fibre and is surjective by (D1). The interval argument gives \(H^{>0}(I;p_*A)=0\). Ordinary direct-image composition, computed with one injective resolution, identifies this with \(H^{>0}(K;A)\). This proves the compact case, including lower-dimensional compact sets. The fibre formula is used only for the proper map \(p\).

For completeness a locally closed convex \(C\) has a compact convex exhaustion \(K_n\subset\operatorname{int}_C K_{n+1}\) whose interiors cover \(C\). Here is a construction that also permits partially retained boundary faces. The set \(D=\overline C\setminus C\) is closed in \(E\). The compact sets

\[
A_m=\{x\in\overline C:|x|\leq m,
               \operatorname{dist}(x,D)\geq1/m\},\qquad
B_m=\operatorname{conv}(A_m)
\tag{D4}
\]

lie in \(C\), increase, and their interiors in \(C\) cover \(C\); omit the distance condition if \(D\) is empty. Their hulls are compact. Indeed a convex combination of more than \(\dim E+1\) points has an affine dependence; varying its coefficients along that dependence until one becomes zero preserves its barycenter and nonnegativity. Repetition bounds the number of points. The hull of a compact set is consequently a continuous image of its \((\dim E+1)\)-fold product times a compact simplex. Choose a subsequence of \(B_m\) such that each lies in the interior in \(C\) of its successor. Compactness and the increasing interior cover permit each choice. These are the required \(K_n\).

Every restricted sheaf \(A|_K\) on a compact convex \(K\subset C\) is acyclic by the compact case. Embed \(A\) into an injective sheaf \(J\), with quotient \(Q\). A section of \(Q\) on \(C\) lifts on each \(K_n\), since \(H^1(K_n;A)=0\). Make the lifts compatible: the difference of a new lift and the previous lift on \(K_n\) is a section of \(A\), which (D1) extends to \(C\); subtract that extension from the new lift. Compatible lifts glue on the open cover \(\operatorname{int}_C K_n\) and give a global lift. Hence \(H^1(C;A)=0\).

The quotient \(Q\) also satisfies (D1). A section of \(Q\) on compact convex \(K\) first lifts to \(J|_K\). Compact-neighborhood continuity for sections extends this lift to an open neighborhood of \(K\), and flabbiness of \(J\) extends it to \(C\). Its image is the required extension in \(Q\). Repeating this argument on successive injective-resolution quotients, and using dimension shifting, proves every positive-degree vanishing claimed in (D1). Empty sets give zero groups throughout. This proof uses actual compatible lifts, without an unproved interchange of cohomology and inverse limits.

## Sections that continue in every cone direction {#directional-sections}

Let \(\gamma\subset E\) be any closed convex cone containing zero. It may contain lines or have empty interior. Define \(E_\gamma\) by the open sets

\[
W\subset E\text{ ordinarily open},\qquad W+\gamma=W,
\qquad q:E\longrightarrow E_\gamma.
\tag{D5}
\]

The map \(q\) is the identity on points and is continuous. Arbitrary unions and finite intersections satisfy the two displayed conditions. Convex sets \(B_\epsilon(x)+\gamma\) form a neighborhood basis at \(x\). This topology is generally not Hausdorff: if \(v\in\gamma\), every directional neighborhood of \(x\) contains \(x+v\). We use ordinary inverse image, direct image and sheaf cohomology on this space. All proper-fibre arguments below take place on ordinary locally compact Hausdorff spaces.

Let \(G\) be a sheaf on \(E_\gamma\), and put \(H=q^{-1}G\). For every convex ordinary open \(U\), the natural map is an isomorphism:

\[
\Gamma(U+\gamma;G)\xrightarrow{\sim}\Gamma(U;H).
\tag{D6}
\]

Its injectivity expresses continuation of a zero germ: equality at \(u\) holds on a directional neighborhood and hence at all points of \(u+\gamma\). For surjectivity, represent a section on \(U\) on an ordinary open cover \(U_i\) by sections \(s_i\) of \(G\) on \(U_i+\gamma\). Such representatives exist by the definition of inverse image and by shrinking within a directional representing neighborhood. If \(y\) lies in two enlargements, choose originating points \(u_i,u_j\in U\cap(y-\gamma)\). Join them by a segment in that convex set. At a point on the segment any two representatives agree as germs there, and therefore also as germs at \(y\). A representing chart works on a small interval of segment parameters, so the germ at \(y\) is locally constant along the segment and hence constant. Thus \(s_i,s_j\) agree at \(y\), and all the representatives glue on \(U+\gamma\). The construction proves exactly the stated restriction map.

For compact convex \(K\), compact-neighborhood continuity and (D6) imply

\[
\Gamma(K;H)=
\operatorname*{colim}_{W\supset K\text{ directional open}}
\Gamma(W;G).
\tag{D7}
\]

To justify the indexing, convex ordinary neighborhoods are cofinal around \(K\). If a directional open \(W\) contains \(K\), compactness gives \(\epsilon>0\) with \(K+B_\epsilon\subset W\), and directional invariance gives \((K+B_\epsilon)+\gamma\subset W\). If \(K\subset L\subset K+\gamma\) and \(L\) is compact convex, a directional open contains \(K\) exactly when it contains \(L\). Hence restriction \(\Gamma(L;H)\to\Gamma(K;H)\) is an isomorphism.

The set \(K+\gamma\) is closed: in a convergent sequence of sums one first passes to a convergent subsequence of the compact summands. Exhaust this closed convex set by its intersections with closed balls large enough to contain \(K\). Their interiors in \(K+\gamma\) cover it. Gluing on those interiors and using the preceding restriction isomorphisms proves

\[
\Gamma(K+\gamma;H)\xrightarrow{\sim}\Gamma(K;H).
\tag{D8}
\]

## The derived unit and the projector {#directional-derived-unit}

If \(G\) is flabby on \(E_\gamma\), every section of \(q^{-1}G\) on a compact convex set extends to \(E\): use (D7) to represent it on a directional open, extend by flabbiness, and pull back. Restricting that global extension to any locally closed convex \(C\) proves (D1) for \((q^{-1}G)|_C\). The convex criterion gives its acyclicity on \(C\). This does not assert that \(q^{-1}G\) is flabby in the ordinary topology.

Resolve \(G\in D^+(k_{E_\gamma})\) by a bounded-below injective complex \(I\). Enough injectives and exact inverse image hold on any topological space, by the module/skyscraper and stalk constructions in the duality foundations. Each \(I^m\) is flabby. The preceding argument makes \(q^{-1}I^m\) acyclic on all ordinary locally closed convex sets. Thus (D6) and (D8), applied termwise, give the actual maps

\[
R\Gamma(U+\gamma;G)\xrightarrow{\sim}R\Gamma(U;q^{-1}G),
\qquad
R\Gamma(K+\gamma;q^{-1}G)\xrightarrow{\sim}R\Gamma(K;q^{-1}G).
\tag{D9}
\]

On a convex directional open \(W\), (D6) gives \(\Gamma(W;I^m)=\Gamma(W;q^{-1}I^m)\), and the latter sheaf has no higher cohomology there. These opens are a basis. It follows, by the stalk formula for a derived direct image, that every \(q^{-1}I^m\) is \(q_*\)-acyclic. The termwise unit is an isomorphism, again by (D6). Consequently

\[
G\xrightarrow{\sim}Rq_*q^{-1}G,
\qquad P_\gamma=q^{-1}Rq_*,\qquad P_\gamma^2\simeq P_\gamma.
\tag{D10}
\]

Derived adjunction and its unit identify Hom groups between inverse images with the original Hom groups, so \(q^{-1}\) is fully faithful. The projector has the counit \(P_\gamma F\to F\) of this same adjunction. Its idempotence and compatibility with that counit follow from the unit isomorphism and the adjunction triangle identities. These constructions work in \(D^+\), without a claim about arbitrary products or a finite cohomological bound on the non-Hausdorff directional space.

## A correspondence on ordinary spaces {#directional-kernel}

We identify \(P_\gamma\) by a kernel on ordinary spaces. First we need a variable-coefficient version of interval homotopy. For an ordinary locally compact Hausdorff \(T\), projection \(\pi:T\times[0,1]\to T\), and any \(A\in D^+(k_T)\),

\[
A\xrightarrow{\sim}R\pi_*\pi^{-1}A.
\tag{D11}
\]

The proper-fibre proof on bounded-below injectives identifies its stalk with the constant-section map \(A_t\to R\Gamma([0,1];(A_t)_{[0,1]})\). The constant-module interval calculation and finite truncation give this isomorphism for bounded coefficient complexes. For a bounded-below complex and a specified degree \(q\), truncate above degree \(q\). The removed tail begins in degree \(q+1\); ordinary derived sections are left t-exact, as seen from a bounded-below injective resolution. This tail changes neither side in degrees at most \(q\). The bounded result therefore proves every degree of (D11). Both endpoint restrictions are inverses of this actual unit.

Suppose \(p:Y\to B\) is a continuous map between ordinary locally compact Hausdorff spaces, has a continuous section \(s\), and has a homotopy from \(\mathrm{id}_Y\) to \(sp\) which preserves the map to \(B\). For \(F\in D^+(k_B)\), apply (D11) to \(p^{-1}F\) on \(Y\). Pullback by the homotopy, followed by its two endpoint restrictions, gives the same map in both cases. Hence \(\mathrm{id}=p^*s^*\) on derived sections, while \(s^*p^*=\mathrm{id}\) follows from \(ps=\mathrm{id}\). We have proved the canonical isomorphism

\[
R\Gamma(B;F)\xrightarrow{p^*}\ R\Gamma(Y;p^{-1}F).
\tag{D12}
\]

No properness of \(p\) or of this homotopy is required. Properness was used only for the interval projection in (D11).

Set \(Z_\gamma=\{(x,y):y-x\in\gamma\}\), and let \(p_1,p_2:Z_\gamma\to E\) be its projections. For \(F\in D^+(k_E)\),

\[
P_\gamma F\simeq Rp_{1*}p_2^{-1}F.
\tag{D13}
\]

Equivalently, on \(E\times E\) the kernel is the restriction of the second-factor inverse image to the closed set \(Z_\gamma\), followed by its exact closed pushforward. Thus (D13) uses ordinary direct image and has no orientation shift.

To construct its map, a directional open \(W\) satisfies \(p_1^{-1}W\subset p_2^{-1}W\). Pullback by \(p_2\), followed by this restriction on directional opens, gives a natural map \(Rq_*F\to Rq_*Rp_{1*}p_2^{-1}F\). Adjunction gives (D13) in the displayed direction. Ordinary direct images compose here because their left adjoints are exact and their right adjoints preserve injectives.

We check the map on stalks by computing on convex ordinary opens \(U\). Put \(B=U+\gamma\) and \(Y_U=p_1^{-1}U\), and project \(Y_U\to B\) by \(y\). This is a map between ordinary locally compact Hausdorff spaces. It has local sections: for \(y_0=x_0+v_0\), with \(x_0\in U\), \(v_0\in\gamma\), use \(y\mapsto(x_0+y-y_0,y)\) near \(y_0\). A locally finite continuous partition of unity on \(B\), subordinate to such neighborhoods, averages their first coordinates to a continuous \(\sigma(y)\in U\) with \(y-\sigma(y)\in\gamma\). Convexity of both sets verifies the two inclusions. The partition can be constructed by a locally finite relatively compact ball refinement, continuous bump functions positive on a shrinking cover, and division by their positive locally finite sum. Thus no directional-space partition theorem is being assumed.

The segment \(((1-t)x+t\sigma(y),y)\) remains in \(Y_U\), fixes its second projection and contracts to the section. Equation (D12) gives

\[
R\Gamma(U+\gamma;F)\xrightarrow{\sim}
R\Gamma(Y_U;p_2^{-1}F).
\tag{D14}
\]

Ordinary convex neighborhoods \(U\) are cofinal at \(x\), and \(U+\gamma\) are cofinal in its directional neighborhoods. Taking filtered colimits of cohomology in (D14) proves (D13) on all stalks. The constructed comparison is exactly this pullback map. Restriction to the diagonal section \(x\mapsto(x,x)\) identifies its subsequent map to \(F\) with the counit: on a directional open it restricts a section at \(y\) to its value at \(y=x\), the ordinary adjunction restriction. Equality can also be checked on the injective representatives used to construct the maps. This fixes the comparison, rather than merely giving an abstract isomorphism of its two objects.

## Localizing inside a directional lens {#directional-support-compatibility}

For \(S\) locally closed in \(E_\gamma\), write \(\mathcal L_S\) for the sheaf operation \(R\mathcal Hom(k_S,-)\). For a closed \(S\) it is the derived sheaf of sections with support in \(S\). Then

\[
Rq_*\mathcal L_S^{E}F\simeq
\mathcal L_S^{E_\gamma}Rq_*F.
\tag{D15}
\]

For directional closed \(S\), its complement is open in both topologies. Apply \(Rq_*\) to the usual localization triangle. Direct-image composition and restriction to this open identify its third term with the third term of the directional localization triangle, with the same restriction map. Their fibres are therefore isomorphic. For \(S=O\cap D\) with \(O\) directional open and \(D\) directional closed, let \(j:O\hookrightarrow E\). The locally closed support identity is \(\mathcal L_SF=Rj_*\mathcal L_{D\cap O}(F|_O)\). It follows by adjunction for open extension by zero followed by closed support. Apply the closed case on \(O\) and compose direct images. This proves (D15). It is not a formula for an arbitrary ordinarily locally closed subset.

## From the cap comparison back to all local tests {#compact-cap-converse}

Let \(F\in D^+(k_X)\), \(X\subset E\) open, and \((x_0,\xi_0)\) a nonzero covector. Suppose there are a closed convex cone \(C\), a vertex neighborhood \(V\), and \(h>0\) such that

\[
\langle c,\xi_0\rangle<0\ (c\in C\setminus\{0\}),\quad
H=\{y:\langle y-x_0,\xi_0\rangle\geq-h\},\quad L=\partial H,
\tag{D16}
\]

every \((x+C)\cap H\), \(x\in V\), lies in \(X\), and the actual restriction from this cap to \((x+C)\cap L\) is an isomorphism. We prove \((x_0,\xi_0)\notin\operatorname{SS}(F)\), including every nearby \(C^1\) test, rather than only linear tests.

Extend \(F\) by zero from \(X\) to \(E\), and put \(B=F_{H\setminus L}\), where the subscript denotes restriction followed by extension by zero. The exact coefficient-set sequence gives the triangle \(B\to F_H\to F_L\to\). By (D13) and properness on the support of this particular kernel,

\[
(P_C B)_x\simeq R\Gamma(x+C;B)
\simeq\operatorname{fib}\bigl(R\Gamma((x+C)\cap H;F)
                         \to R\Gamma((x+C)\cap L;F)\bigr)=0
\tag{D17}
\]

for \(x\in V\). Here is the properness check. Compactness of the unit section of \(C\) gives \(\langle c,\xi_0\rangle\leq-a|c|\) for some \(a>0\). If \(x\) ranges in a compact set, \(y-x\in C\) and \(y\in H\) bound \(|y-x|\) uniformly. The resulting correspondence is closed and bounded, hence compact. The closed support of the kernel is contained in it. The proper-fibre formula consequently applies; no fibre computation for an unrestricted nonproper projection was used. For \(C=\{0\}\) the same assertion is immediate from the diagonal kernel.

We turn this local vanishing of \(P_C B\) into a globally killed representative of \(F\). Shrink \(V\) into the interior of \(H\). Write \(\ell(y)=\langle y-x_0,\xi_0\rangle\) and take

\[
O_1=B_r(x_0)+C,\quad O_0=O_1\cap\{\ell<-b\},\quad
S=O_1\setminus O_0,\quad A=\mathcal L_S B,
\tag{D18}
\]

with \(r,b>0\) small. These two opens are directional. If \(y=x_0+u+c\in S\), then \(|u|<r\) and \(a|c|\leq b+|\xi_0|r\). Thus \(\overline S\subset V\) for sufficiently small choices, and \(x_0\in\operatorname{Int}S\). Since \(P_C B\) vanishes on \(V\), \(\mathcal L_S P_C B=0\). Formula (D15) and the unit isomorphism (D10) give

\[
Rq_*A\simeq\mathcal L_S Rq_*B
\simeq Rq_*\mathcal L_S P_C B=0.
\tag{D19}
\]

Near \(x_0\), \(A\) agrees with \(B\) and hence with \(F\). All these objects are in \(D^+\); no finite bound for the directional projector is needed.

If the original \(F\) is bounded, so is this representative \(A\). Indeed, for \(j_i:O_i\hookrightarrow E\), localization identifies \(A\) with the fibre of \(Rj_{1*}(B|_{O_1})\to Rj_{0*}(B|_{O_0})\). If \(F\) has degrees \([a,b]\) and \(\dim E=N\), the ordinary-image dimension bound puts both images in \([a,b+N]\). Their fibre lies in \([a,b+N+1]\). The intermediate projector may remain in \(D^+\); it does not impose a new boundedness assumption on this argument.

It remains to show that any such representative \(A\), killed by \(Rq_*\), passes all local tests with differential near \(\xi_0\). Strict negativity on the compact unit directions of \(C\) persists on one covector neighborhood of \(\xi_0\). Fix a point \(x\) near \(x_0\) and a \(C^1\) function \(f\) whose differential there is in that neighborhood. On a sufficiently small convex ball its derivative in every unit direction of \(C\) is at most \(-c<0\). Form a directional open \(O\) by adding \(C\) to the negative sublevel patch \(\{f<f(x)\}\) in a smaller ball. Near \(x\), this agrees with the original sublevel: along a cone segment inside the larger ball the function decreases. Both endpoints of any segment needed to check this germ lie in that convex ball.

Put \(N_\epsilon=B_\epsilon(x)+C\). There is \(M\) bounding \(|df|\) on the ball. A starting point in \(B_\epsilon(x)\) has value at most \(f(x)+M\epsilon\). After advancing a distance \((M/c+1)\epsilon\) in a cone direction it enters the negative patch, while still in the chosen small ball for sufficiently small \(\epsilon\). Every later point on that ray lies in \(O\). It follows that

\[
N_\epsilon\setminus O\subset B_{K\epsilon}(x)
\quad\text{for one }K>0\text{ and all small }\epsilon.
\tag{D20}
\]

These sets are relative open neighborhoods of \(x\) in \(Z=E\setminus O\) and form a neighborhood basis there. Because \(Z\) is directional closed, (D15) gives \(Rq_*\mathcal L_Z A=0\). Its derived sections on every directional open \(N_\epsilon\) vanish. Equivalently these are the derived sections on \(N_\epsilon\cap Z\) of the restricted supported object \(i^!A\), with \(i:Z\hookrightarrow E\). Taking the filtered colimit over this ordinary relative neighborhood basis gives \((\mathcal L_Z A)_x=0\). Since the germ of \(Z\) is \(\{f\geq f(x)\}\), this is exactly the desired local support test. The covector neighborhood was chosen before \(x,f\); the auxiliary ball may depend on the test, as its definition permits. If \(C=\{0\}\), \(Rq_*A=A=0\) directly. This proves the converse.

Combining it with (U1)–(U10) proves equivalence of the local support-test condition, the compact-cap condition, and existence of a locally agreeing representative killed by a strictly negative cone's directional direct image. The forward proof used analytic boundary functions in linear coordinates; the reverse allows all \(C^1\) functions. Thus testing analytic functions, smooth functions, or \(C^r\) functions for any \(r\geq1\) gives the same exclusion on an analytic coordinate chart. At the zero covector, constant-function tests force local vanishing of \(F\); the cone \(\{0\}\), whose projector is the identity, gives the same condition. This completes that edge case too.

## Propagation for a prescribed cone {#directional-propagation}

The cap converse lets us choose a cone around a single testing direction. A boundary problem often gives the cone in advance, through the directions that enter the open set. We now prove the propagation statement needed in that situation, and then use it for both kinds of open extension.

Write

\[
C^- =\{\eta\in E^*: \langle v,\eta\rangle\leq0\text{ for every }v\in C\}.
\tag{P1}
\]

Let \(C\) be closed, convex and pointed, meaning \(C\cap(-C)=\{0\}\). It need not have interior. Let \(F\in D^+(k_E)\), let \(U\) be ordinary open, and let \(O_0\subset O_1\) be \(C\)-open. Assume

\[
\operatorname{SS}(F)\cap(U\times\operatorname{Int}C^-)=\varnothing,
\qquad O_1\setminus O_0\subset U,
\qquad (x+C)\setminus O_0\text{ compact for every }x\in O_1.
\tag{P2}
\]

Then the following are the actual support and restriction comparisons:

\[
(Rq_{C*}\mathcal L_{E\setminus O_0}F)|_{O_1}=0,
\qquad R\Gamma(O_1;F)\xrightarrow{\sim}R\Gamma(O_0;F).
\tag{P3}
\]

For \(F\) originally defined on an open \(X\subset E\) and \(U\subset X\), apply this statement to \(Rj_*F\), \(j:X\hookrightarrow E\). Its microsupport agrees with that of \(F\) inside \(X\), and its sections on an open \(O\) are the sections of \(F\) on \(O\cap X\). Thus (P3) gives the same restriction comparison with those intersections. No hypothesis is imposed on the extension outside \(U\).

### A rounded front that retains a strict direction {#rounded-cone-fronts}

First suppose \(C\ne\{0\}\) and \(O_0=\{\ell<0\}\), where \(\ell(y)=\langle y,\eta\rangle-c\) and \(\eta\in\operatorname{Int}C^-\). Compactness of the unit directions gives \(\langle v,\eta\rangle\leq-a|v|\) on \(C\), for some \(a>0\). Put \(H=\{\ell\geq0\}\), \(B=\mathcal L_HF\), and let \(d_x(y)\) be distance to \(x+C\).

Here are the differentiability facts about distance that we need. A nonempty closed convex set has a unique closest point \(p(y)\): existence follows from a compact minimizing ball, and uniqueness from strict convexity of squared norm at a midpoint. Minimality gives \(\langle y-p(y),z-p(y)\rangle\leq0\) for all \(z\) in the set. Adding the two inequalities for \(y,y'\) proves \(|p(y)-p(y')|\leq|y-y'|\). Comparison with these two minimizers then bounds the error in the linear expansion of squared distance by a constant times \(|y-y'|^2\). Its derivative is therefore \(2(y-p(y))\), continuously. Away from the set,

\[
dd_x(y)=\frac{y-p(y)}{|y-p(y)|}\in C^-.
\tag{P4}
\]

The inclusion follows by using \(p(y)+tv\) in the minimizing inequality for \(v\in C\).

For \(t>0\), define the open set

\[
N_t(x)=\{\ell<0\}\ \cup\
\{d_x<2t,\ (d_x-t)_+\ell<(2t-d_x)^2\},
\qquad r_+=\max(r,0).
\tag{P5}
\]

It contains \(\{d_x\leq t\}\). For \(t<r<2t\), its curved boundary is the graph of

\[
b_t(r)=\frac{(2t-r)^2}{r-t},\qquad
b_t'(r)=-\frac{(2t-r)r}{(r-t)^2}\leq0.
\tag{P6}
\]

Set \(b_t(r)=0\) for \(r\geq2t\). The join is \(C^1\), with derivative zero. At \(r\downarrow t\) its height tends to infinity, so there is no finite boundary on that seam. Every finite boundary point is locally defined by \(\ell-b_t(d_x)<0\), with outward differential

\[
d(\ell-b_t(d_x))=\eta-b_t'(d_x)\,dd_x
\in\operatorname{Int}C^-\setminus\{0\}.
\tag{P7}
\]

An interior point of a convex cone plus a point of the cone stays interior, and evaluation on any nonzero vector of \(C\) proves that this differential is nonzero. The retained \(\eta\) term matters: avoidance is required only in the interior of the polar.

The sets \(N_t(x)\) increase and are left continuous in \(t\). On a curved piece this follows either from (P5), or from the fact that increasing \(t\) increases the numerator and decreases the positive denominator in (P6). The far flat boundary is stationary; only the limiting moving front enters every later set, as checked below. For \(r\geq0\), the set

\[
K_x(r)=\{y:\ell(y)\geq0,\ d_x(y)\leq r\}
\tag{P8}
\]

is compact. Write \(y=x+v+e\), \(v\in C\), \(|e|\leq r\). Then \(a|v|\leq\ell(x)+|\eta|r\), so it is bounded as well as closed. The sets \(K_x(r)\) decrease to the compact truncated cone \((x+C)\cap H\), which lies in \(U\cap O_1\). For some small \(\epsilon>0\), therefore, \(K_x(2\epsilon)\) is compactly contained in \(U\cap O_1\).

Apply the compact-front deformation theorem to \(B\) and \(N_t(x)\), with \(0<t<\epsilon\). Its supported increments lie in the corresponding compact set (P8). For a parameter \(s\), the limiting front, with closure taken before intersection, is contained in \(\partial N_s(x)\cap H\cap\{d_x\leq2s\}\). Interior points are excluded by openness, and strict exterior points by continuity of (P5). A flat boundary point with \(d_x>2s\) is excluded by choosing \(s<t<d_x/2\); near that point both opens are the same lower halfspace, so it is outside the increment closure. Every remaining front point enters each later set, by the strict increase of the curved graph and by (P5) at \(d_x=2s\). At the endpoint parameter, the complement of \(N_s(x)\) is contained in \(H\); consequently

\[
\mathcal L_{E\setminus N_s(x)}B
\simeq\mathcal L_{E\setminus N_s(x)}F.
\tag{P9}
\]

Its stalk vanishes by (P7) and (P2). This checks the endpoint as well as every later front condition. All restriction maps between sufficiently small \(N_t(x)\) are isomorphisms on derived sections of \(B\).

The intersections \(N_t(x)\cap H\) are cofinal ordinary neighborhoods in \(H\) of \((x+C)\cap H\): they contain this compact set and are contained in \(K_x(2t)\). The compact-continuity result (N1), applied on the closed support \(H\), now identifies the actual restriction

\[
R\Gamma(N_t(x);B)\xrightarrow{\sim}R\Gamma(x+C;B)
\quad\text{for all sufficiently small }t>0.
\tag{P10}
\]

### Following a ray to a region where the support is empty {#ray-propagation}

Fix any \(v\in C\setminus\{0\}\) and set \(x_b=x+bv\), \(b\geq0\). The vertices stay in \(O_1\). For large \(b\), \(\ell(x_b)<0\), and the whole cone \(x_b+C\) misses \(H\). Thus \(Q_b=R\Gamma(x_b+C;B)\) is zero there.

Near any fixed \(b\), choose \(\epsilon>0\) with \(K_{x_b}(6\epsilon)\) compactly inside \(U\cap O_1\). Distances to translated cones differ by at most the distance between the vertices. If \(|x_b-x_{b'}|<\epsilon\), then \(K_{x_{b'}}(5\epsilon)\subset K_{x_b}(6\epsilon)\). The deformation ranges may therefore be chosen as \((0,3\epsilon)\) and \((0,5\epsilon/2)\), respectively; both contain \(\epsilon\) and \(2\epsilon\). There is also a useful inclusion: if \(|d-d'|\leq\delta\) and \(t'\geq t+\delta\), the inequality defining (P5) for \((d,t)\) implies the one for \((d',t')\). In the curved part its positive left factor decreases and its right side increases; the tube and lower-halfspace cases follow directly. Hence, when \(|b-b'|\,|v|<\epsilon\),

\[
x_{b'}+C\subset N_\epsilon(x_b)\subset N_{2\epsilon}(x_{b'}),
\tag{P11}
\]

with both parameters inside the ranges of (P10) for both centers. The restriction isomorphism from the largest to the smallest set factors through \(R\Gamma(N_\epsilon(x_b);B)\). If \(Q_b=0\), this middle term is zero, and the factorization forces \(Q_{b'}=0\). Interchanging the centers proves the converse. The set of zero parameters and its complement are both open in \([0,\infty)\); connectedness and the large-parameter vanishing give \(Q_0=0\).

The directional neighborhoods \(B_\delta(x)+C\), intersected with \(H\), form another cofinal neighborhood system of the same compact truncated cone, by (P8). Compact continuity therefore makes the stalk of \(Rq_{C*}B\) zero at \(x\). This proves the first assertion of (P3) for a lower halfspace. No vector in \(\operatorname{Int}C\) was needed, so rays and other cones of empty interior are included.

### Compact localization for an arbitrary directional open {#general-directional-open}

Now let \(O_0\) be arbitrary as in (P2). For \(x\in O_1\setminus O_0\) and any prescribed directional neighborhood \(A\subset O_1\), we can choose

\[
V=B_\delta(x)+C\subset A,
\qquad \overline{V\setminus O_0}\text{ compactly contained in }U.
\tag{P12}
\]

Indeed, compactness of \((x+C)\setminus O_0\) gives \(R\) such that all cone points beyond length \(R\) lie in \(O_0\). The compact section at length \(R\) has a uniform ball neighborhood in \(O_0\). Adding the remaining positive multiple of a cone vector puts the same-radius ball around every longer point inside \(O_0\). Thus \((B_\delta(x)+C)\setminus O_0\) is uniformly bounded for small \(\delta\). Any limit as \(\delta\downarrow0\) lies in \((x+C)\setminus O_0\subset U\). Compactness then puts the whole closure inside \(U\). Finally choose the starting ball in \(A\).

Put \(D=V\setminus O_0\) and \(G=\mathcal L_DF\). Its closed support is compactly contained in \(U\), and localization gives

\[
R\Gamma(E;G)\simeq\operatorname{fib}
\bigl(R\Gamma(V;F)\longrightarrow R\Gamma(V\cap O_0;F)\bigr).
\tag{P13}
\]

Choose \(\eta\in\operatorname{Int}C^-\). We show that the support test of \(G\) on every affine halfspace \(H_c=\{\langle -,\eta\rangle\geq c\}\) vanishes at its boundary. Only boundary points \(z\in U\) matter. A small directional neighborhood \(W=B_\delta(z)+C\) has \(W\cap H_c\) compactly contained in \(U\): the preceding estimate gives \(|y-z|\leq(1+|\eta|/a)\delta\) there. The halfspace case, applied to \(\{\langle -,\eta\rangle<c\}\) and its union with \(W\), makes the directional image of \(B_c=\mathcal L_{H_c}F\) vanish over \(W\).

Closed support commutes with the locally closed operation \(\mathcal L_D\). This can be seen by writing \(D=V\cap(E\setminus O_0)\), composing the two closed-support functors on \(V\), and using open direct-image adjunction; it is also the tensor–Hom identity for \(k_{H_c}\otimes k_D=k_{H_c\cap D}\). For any \(C\)-open \(W'\subset W\), the resulting derived section complex is

\[
R\Gamma(W';\mathcal L_{H_c}G)\simeq
\operatorname{fib}\bigl(R\Gamma(W'\cap V;B_c)
\longrightarrow R\Gamma(W'\cap V\cap O_0;B_c)\bigr)=0.
\tag{P14}
\]

Both domains are directional opens in the vanishing region. The sets \(W'\cap H_c\) give a cofinal ordinary relative-neighborhood basis at \(z\), using the same radius bound as for \(W\). The object is supported on \(H_c\), so its ordinary stalk is the filtered colimit of these zero complexes in each cohomology degree. This proves the required halfspace support test on \(G\).

Apply deformation to \(G\) and the increasing opens \(\{\langle -,\eta\rangle<t\}\), \(t\in\mathbb R\). Compact support gives compact increments. The limiting fronts are the level hyperplanes; (P14) gives their endpoint tests, and later fronts already lie inside. Below the minimum on the support, sections vanish. Deformation therefore gives \(R\Gamma(E;G)=0\). By (P13), this is \(R\Gamma(V;\mathcal L_{E\setminus O_0}F)=0\). Such \(V\) are cofinal at every \(x\in O_1\setminus O_0\); on \(O_0\) the supported object already vanishes. This proves the directional vanishing in (P3). Taking its derived sections on \(O_1\) and applying localization proves the restriction assertion.

If \(C=\{0\}\), then \(\operatorname{Int}C^-=E^*\), including the zero covectors. Constant-function tests in (P2) force \(F|_U=0\), so (P3) follows directly. This exceptional case requires the zero covectors in (P2).

## One localization for an entire family {#uniform-directional-localization}

Suppose all \(F_i\in D^+(k_E)\) satisfy the same avoidance in (P2) on \(U\), with a fixed nonzero pointed cone \(C\). Fix \(x\in U\) and \(\eta\in\operatorname{Int}C^-\). For small \(r,b>0\), take

\[
O_1=B_r(x)+C,\quad O_0=O_1\cap\{\langle y-x,\eta\rangle<-b\},
\quad S=O_1\setminus O_0.
\tag{P15}
\]

The estimate from (D18) puts \(\overline S\) compactly inside \(U\) and \(x\) in its interior. Every forward slice outside \(O_0\) is a compact truncated cone. Propagation and (D15), followed by the open direct image from \(O_1\), give

\[
Rq_{C*}\mathcal L_SF_i=0\quad\text{for every }i,
\qquad (\mathcal L_SF_i)|_{\operatorname{Int}S}
\simeq F_i|_{\operatorname{Int}S}.
\tag{P16}
\]

All choices depend only on \(U,C,x,\eta\). They are made before \(i\), and no common degree bound is needed for this family statement.

For a countable tower with a common lower degree bound, this supplies the limit step used by ordinary open extension. The functor \(T=Rq_{C*}\mathcal L_S\) preserves its homotopy inverse limit. Here is a resolution-level justification. Tensoring with \(k_S\) is exact because its stalks are \(k\) or zero; therefore \(\mathcal Hom(k_S,-)\) preserves injectives. So does \(q_{C*}\), whose left adjoint is exact. Both are right adjoints and commute with products. Represent a tower by injective complexes bounded below in a common degree; the homotopy limit is the fibre of \(1-\mathrm{shift}\) on their product. Products of injectives are injective, and their complexes are homotopically injective: mapping an acyclic complex into a product gives the product of acyclic Hom complexes, which is acyclic because products of modules are exact. These models compute both operations and prove

\[
T(\operatorname{holim}_n F_n)\simeq
\operatorname{holim}_n T(F_n)=0.
\tag{P17}
\]

The limit agrees with its localized representative near \(x\). The cone-to-test argument therefore excludes every nearby covector in \(\operatorname{Int}C^-\). This calculation takes the limit after an entire supported object is killed; it makes no assertion that an ordinary stalk commutes with an infinite product. The common lower bound is explicitly needed for the bounded-below product model used here.

## Extension by zero in the opposite direction {#opposite-open-extension}

Let \(H\in D^+(k_E)\) satisfy \(Rq_{C*}H=0\). Let \(\Omega\) be ordinary open and invariant under \(-C\), and assume \(\Omega\cap(K+C)\) is relatively compact for each compact \(K\subset E\). Then

\[
Rq_{C*}(H_\Omega)=0,
\qquad H_\Omega=j_!j^{-1}H.
\tag{E1}
\]

Fix \(U=B_\epsilon(x)+C\); its intersection with \(\Omega\) has compact closure. For every integer \(q\),

\[
H^q(U;H_\Omega)=
\mathop{\mathrm{colim}}_{K\text{ closed in }U,\ K\subset\Omega}
H^q_K(U;H).
\tag{E2}
\]

To prove this derived identity, take a bounded-below injective resolution \(I\) of \(H\). Its restrictions are c-soft. The open-extension and compact lifting constructions make \(j_!(I|_\Omega)\), and their restrictions to \(U\), c-soft. The compact-exhaustion proof of ordinary acyclicity, formula (B1), makes these terms acyclic for ordinary sections on the open Euclidean set \(U\). Thus their section complex computes the left side. Term by term it is the union of sections of \(I|_U\) with closed support \(K\subset\Omega\), by the definition of extension by zero. The complex \(I|_U\) is injective and computes each supported term. Exact filtered colimits commute with cohomology, proving (E2) with its natural maps. We used c-soft acyclicity, not a claim that \(j_!I\) is injective.

Each such \(K\) has compact closure in \(E\). Set \(D=\overline K-C\). This is closed: a convergent sequence of sums has a convergent subsequence in its compact first factor. It is \(C\)-closed. Moreover

\[
K\subset D\cap U\subset\Omega.
\tag{E3}
\]

For if \(z=w-v\in U\), \(w\in\overline K\), \(v\in C\), then \(w=z+v\in U\), and hence \(w\in\overline K\cap U=K\). Invariance under \(-C\) gives \(z\in\Omega\). These enlarged supports are cofinal among the supports in (E2). Directional support compatibility (D15) identifies their cohomology with supported cohomology of the zero object \(Rq_{C*}H\) on \(U\). All terms therefore vanish. These \(U\) form a directional basis, proving (E1).

## The two noncharacteristic open-boundary estimates {#noncharacteristic-open-boundaries}

We specify the normal convention before giving the bounds. At a boundary point \(x\) of an open \(\Omega\), a strict inward direction is a vector \(v\) with a neighborhood of directions which translate all sufficiently nearby points of \(\Omega\) into \(\Omega\) for sufficiently short positive times. Let \(D_x(\Omega)\) be this open cone and let

\[
N_x^*(\Omega)=D_x(\Omega)^\circ,
\qquad D^\circ=\{\eta:\langle v,\eta\rangle\geq0\ (v\in D)\}.
\tag{E4}
\]

This is the polar of strict inward directions, not the whole conormal bundle. The cone of strict directions is convex: after shrinking the testing neighborhood, compose a short translation in one allowed direction with one in another, keeping the intermediate point in the same chart. A positive combination is realized by these two translations; the same argument for nearby directions proves the strict condition. Positive rescaling preserves it. If nonempty, this open convex cone equals the interior of its closed bipolar; finite-dimensional separation of a point from an open convex cone proves that assertion. Its polar is then pointed, because a linear functional and its negative cannot both be nonnegative on a nonempty open set unless they are zero. If the strict cone is empty, its polar is the whole dual space.

For comparison with the normal-cone definition, a direction fails to be strict precisely when there are \(y_n\in\Omega\), \(z_n\notin\Omega\), both tending to \(x\), and \(t_n\downarrow0\), with \((z_n-y_n)/t_n\to v\). Failure of a uniform translating neighborhood gives these witnesses; conversely a strict neighborhood excludes them. Thus this definition is the complement of the usual difference normal cone \(C_x(E\setminus\Omega,\Omega)\), with the sign convention fixed by the displayed difference.

Let \(F\in D^+(k_X)\), \(j:\Omega\hookrightarrow X\), and \(x\in\partial\Omega\). Set \(A=\operatorname{SS}(F)_x\) and \(N=N_x^*(\Omega)\). The pointwise estimates are

\[
\begin{aligned}
A\cap(-N)\subset\{0\}
&\ \Longrightarrow\ \operatorname{SS}(Rj_*j^{-1}F)_x\subset A+N,\\
A\cap N\subset\{0\}
&\ \Longrightarrow\ \operatorname{SS}(j_!j^{-1}F)_x\subset A-N.
\end{aligned}
\tag{E5}
\]

They require an ambient \(F\). The limiting estimates remove that requirement when a complex is given only on \(\Omega\). If the indicated condition holds at every boundary point, the bounds hold fibrewise everywhere, with the usual interior restriction and exterior vanishing. These are ordinary sums at the same point. Under the respective no-cancellation condition each sum is closed: an unbounded convergent sum of terms in the two closed cones, divided by the larger norm and passed to a subsequence, would yield nonzero opposite limiting terms. Thus terms of a convergent sum are bounded and have convergent subsequences in their respective cones.

### Choosing a cone with a strict angular margin

Outside the closed support of \(F\) both operations vanish near \(x\); otherwise \(0\in A\). If \(N=E^*\), the right sides are the whole fibre, so there is nothing to exclude. For the first line, fix \(\xi\notin A+N\). The closed convex cone \(L=N+\mathbb R_{\geq0}(-\xi)\) is pointed: \(N\) is pointed and \(\xi\notin N\), so adding the ray introduces no line. The same bounded-sum argument proves closedness. Also \(L\cap(-A)=\{0\}\): an equality \(n-t\xi=-a\) with \(t>0\) would put \(\xi\) in \(A+N\), while \(t=0\) is excluded by the hypothesis.

A pointed closed cone admits a linear functional strictly positive on its unit directions. One finite-dimensional proof takes the compact convex hull of those directions. It misses zero, since a positive combination summing to zero would give a nonzero vector in both signs of the cone. The closest point of that convex hull to zero supplies a separating functional with a positive lower bound. Its affine level-one slice of \(L\) is compact. Enlarge that slice by a sufficiently small closed ball within the affine hyperplane and take its positive hull. Compact angular separation from the closed set \(-A\) ensures that the resulting full-dimensional pointed closed cone \(K\) satisfies

\[
L\setminus\{0\}\subset\operatorname{Int}K,
\quad K\cap(-A)=\{0\},
\quad C=K^\circ,
\quad \langle v,\xi\rangle<0\ (v\in C\setminus\{0\}).
\tag{E6}
\]

In dimension one the affine slice is a point and the same assertion is read directly for the ray. The cone \(C\) is pointed with nonempty interior. Because every nonzero element of \(N\) lies in \(\operatorname{Int}K\), every nonzero vector of \(C\) lies in the strict inward cone. Compactness of its unit section supplies one translating neighborhood valid for all of them. Thus \(\Omega\) has, near \(x\), a globally \(C\)-open representative: take \((\Omega\cap B_\delta(x))+C\). It agrees with \(\Omega\) on a smaller ball, since the segment between an originating point and an endpoint in that smaller ball stays in the translating chart, where it can be subdivided into allowed short translations.

Closedness and conicity of microsupport, with \(K\cap(-A)=\{0\}\), give a neighborhood \(U\) on which \(\operatorname{SS}(F)\) avoids every nonzero direction of \(-K=C^-\). This follows by taking a convergent subsequence of any proposed unit-covector counterexamples at points tending to \(x\). We may extend \(F\) outside the chart and use the global representative of \(\Omega\), since only their common germ is relevant.

### Ordinary image and extension by zero

Choose the compact lens \(S\) from (P15) inside \(U\), with \(x\) in its interior, and write \(H=\mathcal L_SF\). Equation (P16) gives \(Rq_{C*}H=0\). For the ordinary image, \(\Omega\) is \(C\)-open. Open restriction, direct-image composition and the same locally closed support maps give

\[
Rq_{C*}\mathcal L_S(Rj_*j^{-1}F)
\simeq Rj_{C*}\bigl((Rq_{C*}\mathcal L_SF)|_{\Omega_C}\bigr)=0.
\tag{E7}
\]

Here \(j_C\) is the directional open inclusion. This comparison follows by writing \(S\) as the difference of two directional opens and comparing their identical restriction maps; no arbitrary closed base change is involved. Near \(x\), the localized complex agrees with \(Rj_*j^{-1}F\). Since \(\xi\) is strictly negative on \(C\setminus\{0\}\), the cone-to-test implication excludes \((x,\xi)\). This proves the first line of (E5).

For the second line replace \(N\) by \(-N\) in the separation argument. It gives a detecting cone \(C\) for which \(-C\) consists of strict inward directions. Use the globally \((-C)\)-open representative \(\Omega'=(\Omega\cap B_\delta(x))-C\). It agrees with \(\Omega\) near \(x\). It also meets every \(K_0+C\), \(K_0\) compact, in a relatively compact set. Indeed \(y=a-v=b+w\), with \(a\) in the bounded starting ball, \(b\in K_0\), \(v,w\in C\), implies \(v+w=a-b\) bounded. A functional strictly positive on the unit directions of \(C\) bounds both \(|v|\) and \(|w|\), hence \(|y|\). Apply (E1) to the same compactly localized \(H\):

\[
Rq_{C*}(H_{\Omega'})=0.
\tag{E8}
\]

Near \(x\), this is the extension by zero of \(F|_\Omega\). The cone-to-test implication proves the second line. Both arguments work in \(D^+\), including infinite modules. When \(F\) is bounded, the ordinary-image bound and the lens bound after (D19) keep the required actual extension and localized representatives bounded; no bounded-projector theorem is substituted.

## Four checks on propagation and boundary signs

### A ray in a plane

Take \(C=\{(t,0):t\geq0\}\) in \(\mathbb R^2\), \(F=M_{\mathbb R^2}\) for a module \(M\), \(O_1=\mathbb R^2\), and \(O_0=\{u>0\}\). Verify propagation and identify which directions must be excluded.

**Solution.** The negative polar is \(\{(\alpha,\beta):\alpha\leq0\}\), whose interior is \(\alpha<0\). A constant sheaf has only zero-section microsupport, so the avoidance holds. Each forward ray outside \(O_0\) is a compact interval or the empty set. Both opens are \(C\)-open. Thus (P3) gives the actual restriction isomorphism from the plane to the half-plane. Its map is the identity on \(M\), and higher cohomology vanishes by convex acyclicity. The cone has empty interior in the plane, showing why the ray step must not assume an interior vector.

### Why the compact-slice condition is necessary

Keep the preceding \(C\) and nonzero constant coefficients, but take \(O_0=\varnothing\). What fails?

**Solution.** The microsupport avoidance and directional openness still hold, but every forward ray is noncompact. Restriction from the plane has source \(M\) and target zero, so it is not an isomorphism. In the proof, no translation of the vertex reaches a region where the truncated supported cone is empty. This isolates the compact-slice hypothesis.

### The two signs at an endpoint

For \(\Omega=(0,\infty)\subset\mathbb R\) and a nonzero module \(M\), compute the boundary directions allowed by (E5), and check they are attained.

**Solution.** The inward vectors are positive and \(N_0^*(\Omega)=\mathbb R_{\geq0}\,dx\). For ambient \(M_\mathbb R\), the ordinary extension is \(M_{[0,\infty)}\). Its support test with \(f(x)=x\) has stalk \(M\), since all nearby support is already in \(\{x\geq0\}\). Thus the nonnegative ray in the first bound occurs. The zero extension is \(M_{(0,\infty)}\). Its ordinary stalk at zero is zero, while its derived sections on the positive part of a small neighborhood are \(M\). The localization triangle for \(\{x\leq0\}\) therefore gives \(M[-1]\) at zero, nonzero, so its negative covector is detected. Scaling gives the full negative ray in the second bound. Both calculations apply to infinite \(M\).

### What survives an inverse limit

Suppose a countable tower \(F_n\) has a common lower bound and the same exclusion on \(U\times\operatorname{Int}C^-\). Which object should be made zero before taking its homotopy inverse limit?

**Solution.** Choose the one compact lens \(S\) in (P15). Each entire object \(Rq_{C*}\mathcal L_SF_n\) is zero. The injective product-and-fibre model in (P17) then makes \(Rq_{C*}\mathcal L_S\operatorname{holim}_nF_n\) zero. The localized limit agrees with the limit near the lens center, so all corresponding local support tests vanish. Separate zero stalks, with neighborhoods depending on \(n\), would not supply this calculation; (P16) supplies one localization before the limit is formed.

## Four checks with solutions

### A point spreads against the cone

For \(F=M_{\{a\}}\) and arbitrary \(M\), compute \(P_\gamma F\), including its support and shift.

**Solution.** In the kernel, the second coordinate is \(a\) and the condition is \(a-x\in\gamma\). Projection from \(\{(x,a):x\in a-\gamma\}\) to the closed set \(a-\gamma\) is a homeomorphism. Therefore \(P_\gamma F=M_{a-\gamma}\) in degree zero. The counit restricts it to the vertex. For \(E=\mathbb R\), \(\gamma=[0,\infty)\), \(a=0\), this is \(M_{(-\infty,0]}\), not the positive half-line. No flatness or finite rank of \(M\) was used.

### The zero cone and a cone containing every direction

Compute \(P_{\{0\}}F\) and \(P_EF\). Explain why the second extreme does not supply a nonzero strictly negative testing direction.

**Solution.** The zero-cone topology is ordinary and the kernel is the diagonal, so its projector and counit are the identity. The topology \(E_E\) has only the empty set and \(E\) as opens. Its sheaves are modules, its inverse image is the constant-sheaf functor, and \(P_EF=(R\Gamma(E;F))_E\). Its counit is the actual constant-section evaluation. If \(E\ne0\), no covector is strictly negative on both a nonzero vector and its negative, so condition (D16) cannot hold for \(C=E\).

### A fibre calculation that is not available

Let \(j:(0,\infty)\hookrightarrow\mathbb R\) and take the constant sheaf \(k\). Compare \((Rj_*k)_0\) with cohomology of the inverse-image fibre over zero.

**Solution.** Small neighborhoods of zero meet the open half-line in a nonempty interval. Constant interval acyclicity makes their derived sections \(k\), with identity restriction maps. Thus \((Rj_*k)_0=k\) in degree zero. The inverse-image fibre is empty and has zero cohomology. This is why (D14) used an explicit relative contraction and (D17) separately verified properness on its particular support.

### Infinite coefficients in the cap comparison

Let \(M=\bigoplus_{n\geq0}k\), take a nonzero covector on \(E\), and let \(F=M_E\). Identify the natural compact-cap comparison and explain its consequence.

**Solution.** Choose a nonzero closed convex cone strictly negative for the chosen covector, for example a ray in a strictly negative direction, and take every vertex in \(\operatorname{Int}H\). Both the cap and its base are then nonempty compact convex sets: each such ray reaches the base, and strict negativity bounds the cap. Sections of the constant sheaf are the constant functions with value in \(M\), and their restrictions to nonempty convex compact subsets are onto. Criterion (D1) gives no higher cohomology. Restriction from the cap to the base is the identity on \(M\), so the converse excludes the chosen nonzero covector. This proves the expected zero-section bound with infinite coefficients and does not assert that \(M\) is perfect. The zero cone would instead have empty base and would not give this identity comparison.

## Sources and scope {#sources-and-scope}

Masaki Kashiwara and Pierre Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), develops the convex-extension criterion, directional continuation, the derived unit, equivalent microlocal tests, propagation and noncharacteristic open-boundary estimates.

Compact extension and compatible lifts establish the required acyclicity; continuation gives the unit; a variable-coefficient contraction proves the ordinary correspondence; directional support and a compact lens then convert the actual cap map into all local tests. The kernel construction identifies the actual counit and checks the support conditions needed for fibre calculations.

This reading proves the directional projector, compact-cap equivalence, propagation for a prescribed pointed cone, and both noncharacteristic open-boundary estimates, relative to the stated sheaf foundations. Propagation includes cones with empty interior and arbitrary commutative coefficients. The family localization precedes any homotopy inverse limit. The limiting-boundary reading proves the arbitrary-open estimates and the missing-submanifold trace. The companion limiting tensor proof supplies the bounded tensor estimate without constructibility, perfectness or a noncharacteristic assumption. Subanalytic foundations remain separate.
