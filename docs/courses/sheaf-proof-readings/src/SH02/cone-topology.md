# SH02-GAM — Directional neighborhoods and a sheaf projector

Local unit: `SH02-GAM`. Original programme text: CC0 1.0 Universal. 

We keep the advanced course convention: $k$ is a commutative ring with identity and finite global dimension. Modules need not be flat, finite, or free. All derived categories in this unit are bounded below. No constructibility condition occurs. Let $V$ be a finite-dimensional real vector space and let $\gamma\subset V$ be a **closed convex cone containing $0$**. In particular, $\gamma$ may have lines, may have empty interior, and may be $\{0\}$ or $V$. Write $\gamma^a=-\gamma$. A superscript $a$ in this unit always means the antipodal image, never a polar cone.

The purpose of the topology below is to organize information that can be continued in the directions of $\gamma$. Convexity has two distinct roles: it connects alternative continuations, and it supplies a contraction for a correspondence of points. We separate these roles in the proofs.

The directional topology and continuation argument are compared with Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/), Section 1.5.2, printed pp. 33–36. That section assumes a closed convex cone containing zero; it does not require a pointed cone or nonempty interior. The kernel calculation below then supplies its own explicit comparison and contraction, with the support and sign checks kept separate.

## Directional open sets

### SH02-GAM-TOPO — Directional open sets
**Definition and elementary properties (`SH02-GAM-TOPO`).** Put a topology on the set $V$ by declaring $W$ open precisely when it is ordinarily open and $W+\gamma=W$. Denote the resulting space by $V_\gamma$. For any subset $X\subset V$, let $X_\gamma$ have the subspace topology from $V_\gamma$, and let

\[
\phi=\phi_\gamma^X:X\longrightarrow X_\gamma
\]

be the identity map of underlying sets, with the ordinary subspace topology on its domain. It is continuous. Arbitrary unions preserve both conditions defining directional openness. Finite intersections do as well: $(W_1\cap W_2)+\gamma\subset W_1\cap W_2$, and the opposite inclusion follows from $0\in\gamma$. Thus this is a topology.

If $\gamma_1\subset\gamma_2$, the identity $X_{\gamma_1}\to X_{\gamma_2}$ is continuous. For $\gamma=\{0\}$ the topology is the ordinary one. The sets

\[
B_\epsilon(x)+\gamma\qquad(\epsilon>0)
\]

form a convex directional neighborhood basis at $x$ in $V_\gamma$. Indeed, a directional open set containing $x$ contains some $B_\epsilon(x)$ and consequently its sum with $\gamma$. Here any fixed norm can be used. For a compact convex $K$ and a directional open $W$ containing $K$, compactness gives $\epsilon>0$ with

\[
(K+B_\epsilon(0))+\gamma\subset W.
\tag{G1}
\]

To verify this, choose a positive ordinary distance from $K$ to the complement of $W$; if the complement is empty any positive radius works. The left side is convex and directionally open.

The definition makes sense for arbitrary $X$. From now on, assertions about cohomology on $X_\gamma$ require **$X$ itself to be directionally open in $V$**, unless explicitly stated otherwise. This ensures $U+\gamma\subset X$ whenever $U\subset X$.

The directional topology need not be Hausdorff. If $v\in\gamma$ is nonzero, every directional neighborhood of $x$ contains $x+v$, so these distinct points have no disjoint neighborhoods. We therefore use the ordinary sheaf operations $\phi^{-1}$, $R\phi_*$ and $R\Gamma$ on arbitrary topological spaces. We do not apply a locally compact Hausdorff six-operation theorem to $X_\gamma$. The later uses of proper base change occur on ordinary locally compact Hausdorff spaces.

## Continuing sections across a cone

### SH02-GAM-SECTIONS — Continuing sections
**Section lemma (`SH02-GAM-SECTIONS`).** Suppose $X$ is directionally open, $A$ is a sheaf of $k$-modules on $X_\gamma$, and $H=\phi^{-1}A$. If $U\subset X$ is ordinarily open and convex, the pullback-and-restriction map

\[
\Gamma(U+\gamma;A)\longrightarrow\Gamma(U;H)
\tag{G2}
\]

is an isomorphism. The same statement holds for $U=\varnothing$, where both groups vanish.

*Proof.* Inverse image does not change the stalk at a point because $\phi$ is the identity of underlying sets. Equality of two germs of $A$ at $x$ therefore means equality on a directional neighborhood of $x$. It implies equality of their germs at every point of $x+\gamma$ at which the sections in question are defined.

For injectivity, let a section on $U+\gamma$ pull back to zero on $U$. For any $y=u+v$ with $u\in U$ and $v\in\gamma$, its zero germ at $u$ propagates to $y$. Every germ is zero, so the section is zero.

For surjectivity, represent a section $s$ of $H$ on an ordinary open cover $U=\bigcup_i U_i$ by sections $a_i$ of $A$ on $U_i+\gamma$. Such representatives exist: inverse-image sections are locally represented on directional neighborhoods; shrink the ordinary representing open $U_i$ inside that neighborhood and then restrict to $U_i+\gamma$.

Fix $y\in(U_i+\gamma)\cap(U_j+\gamma)$. Choose $u_i\in U_i\cap(y-\gamma)$ and $u_j\in U_j\cap(y-\gamma)$. The segment joining these two points lies in the convex set $U\cap(y-\gamma)$. At any point $u$ of the segment, and for any two charts $U_r,U_t$ containing $u$, the germs of $a_r,a_t$ at $u$ agree because both represent $s$. They agree on a directional neighborhood of $u$, which contains $y$. Consequently their germs at $y$ agree. Along a small subinterval of the segment a single chart can be used, so this common germ at $y$ is locally constant as a function of the segment parameter. Connectedness of the interval makes it constant. In particular, $(a_i)_y=(a_j)_y$. This argument for every $y$ proves equality on the overlaps of $U_i+\gamma$ and $U_j+\gamma$. Sheaf gluing gives a section on $U+\gamma$ whose pullback is $s$. The construction is inverse to (G2), hence canonical. $\square$

Applying (G2) to convex directional opens gives an isomorphism on a basis, and therefore gives the underived unit

\[
A\xrightarrow{\sim}\phi_*\phi^{-1}A.
\tag{G3}
\]

### SH02-GAM-COMPACT-SECTIONS — Compact convex tests
**Compact continuation (`SH02-GAM-COMPACT-SECTIONS`).** For a compact convex subset $K\subset X$, restriction induces

\[
\Gamma(K+\gamma;H)\xrightarrow{\sim}\Gamma(K;H).
\tag{G4}
\]

These are sections of the restrictions of the ordinary sheaf $H$ to the indicated subsets.

*Proof.* We use the elementary compact-neighborhood continuity of sections: for a compact subset $K$ of a Hausdorff space, sections of a restricted sheaf on $K$ are the filtered colimit of sections on its open neighborhoods. One can check it directly by representing a section near each point of $K$, taking a finite subcover, and shrinking the finitely many neighborhoods so that the representatives agree on their overlaps. Equality of two representatives is checked by the same finite-neighborhood shrinking argument. For compact convex $K$ in a finite-dimensional vector space, convex open neighborhoods are cofinal.

Using (G2), this continuity and (G1) give

\[
\Gamma(K;H)
\simeq\mathop{\mathrm{colim}}_{U\supset K\text{ convex open}}\Gamma(U+\gamma;A)
\simeq\mathop{\mathrm{colim}}_{W\supset K\text{ directionally open}}\Gamma(W;A).
\tag{G5}
\]

If $K\subset L\subset K+\gamma$ and $L$ is compact convex, a directional open set contains $K$ if and only if it contains $L$. Hence (G5) identifies the restriction $\Gamma(L;H)\to\Gamma(K;H)$ with an isomorphism.

The set $C=K+\gamma$ is closed: from a convergent sequence $k_n+v_n$ choose a convergent subsequence of $k_n\in K$, and then use closedness of $\gamma$ on $v_n$. Choose increasing radii $r_n\to\infty$, all large enough that $K\subset\overline B_{r_n}(0)$, and put $L_n=C\cap\overline B_{r_n}(0)$. These compact convex sets contain $K$, and their interiors $\operatorname{int}_C(L_n)$ in the topological space $C$ cover $C$. Therefore sections on $C$ are compatible sections on the $L_n$: these topological interiors give the required open cover for gluing; affine relative interiors are not being used. Every restriction $\Gamma(L_n;H)\to\Gamma(K;H)$ is the isomorphism just proved. Taking their inverse limit proves (G4). If $K$ is empty, so is $C$, and the assertion is immediate. $\square$

## Derived continuation

The ordinary-space acyclicity inputs are `SH02-OR-CONVEX-COMPACT` and `SH02-OR-CONVEX-EXHAUSTION` proved in [Extending sections on convex sets](convex-acyclicity.md). Their precise contract is this: for a nonempty locally closed convex subset $C$ of a finite-dimensional real vector space, a sheaf $H_C$ is acyclic for sections on $C$ if every restriction

\[
\Gamma(C;H_C)\longrightarrow\Gamma(L;H_C)
\]

is onto for compact convex $L\subset C$. Compact convex $C$ is the compact case of this criterion; the locally closed case uses a countable compact convex exhaustion with surjective transition maps. These are mathematical prerequisite proofs, not assertions that arbitrary sheaves on convex sets are acyclic. The topology in this criterion is the ordinary topology.

### SH02-GAM-FLABBY-ACYCLIC — Acyclicity after inverse image
**Acyclic resolution lemma (`SH02-GAM-FLABBY-ACYCLIC`).** If $A$ is flabby on $X_\gamma$, then $\phi^{-1}A$ is acyclic on every ordinary locally closed convex $C\subset X$.

*Proof.* Let $L\subset C$ be compact convex, and let $s\in\Gamma(L;\phi^{-1}A)$. Formula (G5) represents $s$ by a section of $A$ on a directional open neighborhood $W$ of $L$ in $X$. Flabbiness extends it to all of $X_\gamma$. Pull back that extension and restrict to $C$. It extends $s$, so the cited acyclicity criterion applies. Empty sets cause no exception. Notice that we proved convex-set acyclicity; we have not claimed that $\phi^{-1}A$ is flabby in the ordinary topology. $\square$

### SH02-GAM-COH-OPEN — Open convex cohomology
**Derived open continuation (`SH02-GAM-COH-OPEN`).** For $G\in D^+(k_{X_\gamma})$ and an ordinary convex open $U\subset X$, the canonical morphism is an isomorphism:

\[
R\Gamma(U+\gamma;G)\xrightarrow{\sim}
R\Gamma(U;\phi^{-1}G).
\tag{G6}
\]

### SH02-GAM-COH-COMPACT — Compact convex cohomology
**Derived compact continuation (`SH02-GAM-COH-COMPACT`).** For compact convex $K\subset X$ and the same $G$, restriction is an isomorphism:

\[
R\Gamma(K+\gamma;\phi^{-1}G)\xrightarrow{\sim}
R\Gamma(K;\phi^{-1}G).
\tag{G7}
\]

### SH02-GAM-UNIT — The derived adjunction unit
**Derived full faithfulness (`SH02-GAM-UNIT`).** The adjunction unit is an isomorphism on $D^+(k_{X_\gamma})$:

\[
G\xrightarrow{\sim}R\phi_*\phi^{-1}G.
\tag{G8}
\]

*Proof of the three assertions.* Resolve $G$ by a bounded-below complex $I^\bullet$ of injective sheaves on $X_\gamma$. The existence of injectives and exactness of inverse image hold on arbitrary topological spaces; see `SH02-IMP-INJECTIVE`, `SH02-IMP-INVERSE`, and `SH02-IMP-DERIVE` in [the prerequisite contracts](open-prerequisites.md). Injective sheaves are flabby, and flabby sheaves are acyclic on every open set, without a Hausdorff assumption.

The acyclic resolution lemma says that $\phi^{-1}I^\bullet$ computes derived sections on $U$, $K$, and $K+\gamma$. The latter is closed convex, even when it is unbounded. Applying (G2) and (G4) term by term gives (G6) and (G7). The maps are the indicated pullback or restriction maps because their underived versions are exactly the maps used in those lemmas.

For (G8), use convex directional open neighborhoods. On such a neighborhood $W$, $\phi^{-1}I^m$ has no higher ordinary cohomology, and $\Gamma(W;I^m)=\Gamma(W;\phi^{-1}I^m)$ by (G2). It follows that every $\phi^{-1}I^m$ is $\phi_*$-acyclic, and (G3) gives a termwise isomorphism $I^\bullet\to\phi_*\phi^{-1}I^\bullet$ computing the derived unit. A bounded-below complex of acyclic objects computes the right derived functor, so all three arguments apply in $D^+$, rather than only to a sheaf concentrated in degree zero. $\square$

In particular, $\phi^{-1}:D^+(k_{X_\gamma})\to D^+(k_X)$ is fully faithful: apply derived adjunction and (G8) to the target of a Hom group. Its right adjoint is $R\phi_*$. Thus $P_\gamma=\phi^{-1}R\phi_*$ is a projector on $D^+(k_X)$, with counit $P_\gamma F\to F$. The isomorphism $P_\gamma^2\simeq P_\gamma$ comes from (G8); it is compatible with the counit by the triangle identities of this same adjunction.

## A contraction with variable coefficients

The next lemma supplies the topological part of the kernel calculation. It does not identify the cohomology of an arbitrary nonproper map with the cohomology of its point fibers.

### SH02-GAM-RELATIVE-CONTRACTION — A contraction with variable coefficients
**Relative contraction lemma (`SH02-GAM-RELATIVE-CONTRACTION`).** Let $p:E\to B$ be a continuous map of ordinary locally compact Hausdorff spaces. Suppose there is a section $s:B\to E$ and a homotopy $h:E\times[0,1]\to E$ satisfying

\[
h_0=\mathrm{id}_E,\qquad h_1=s p,\qquad p h=p\pi,
\]

where $\pi:E\times[0,1]\to E$ is projection. Then, for every $F\in D^+(k_B)$, pullback gives a canonical isomorphism

\[
R\Gamma(B;F)\xrightarrow{\sim}R\Gamma(E;p^{-1}F).
\tag{G9}
\]

*Proof.* The projection $\pi$ is proper because $[0,1]$ is compact. Proper base change, in the arbitrary-module form `SH02-IMP-PROPER-BASECHANGE`, computes the stalks of its unit

\[
T\longrightarrow R\pi_*\pi^{-1}T
\]

as the maps $T_e\to R\Gamma([0,1];(T_e)_{[0,1]})$. These are isomorphisms. For a module $M$, the constant sheaf $M_{[0,1]}$ has global sections $M$, and its restrictions to nonempty compact convex subintervals are onto. The compact convex acyclicity criterion therefore gives zero higher cohomology. Applying this to the cohomology modules of a bounded-below complex, or using its truncation spectral sequence, gives the assertion for $T_e\in D^+(k)$. Thus $R\Gamma(E;T)\to R\Gamma(E\times[0,1];\pi^{-1}T)$ is an isomorphism.

Take $T=p^{-1}F$. The identity $ph=p\pi$ identifies $h^{-1}T$ with $\pi^{-1}T$. The two maps on cohomology induced by the endpoint inclusions into $E\times[0,1]$ are the same: both are inverses of pullback by $\pi$. Composing with pullback by $h$ shows $h_0^*=h_1^*$, that is, $\mathrm{id}=p^*s^*$ on $R\Gamma(E;p^{-1}F)$. On the other side $s^*p^*=\mathrm{id}$ because $ps=\mathrm{id}_B$. These identities are in $D^+(k)$ and prove (G9), with inverse $s^*$. The canonical isomorphism is $p^*$; a choice of contraction only proves its invertibility. $\square$

## The correspondence projector

### SH02-GAM-KERNEL — The correspondence projector
**Kernel theorem (`SH02-GAM-KERNEL`).** Set $X=V$ and let $q_1,q_2:V\times V\to V$ be the two ordinary projections. Put

\[
Z_\gamma=\{(x,y):y-x\in\gamma\}.
\]

For a closed subset $Z$, the notation $T_Z$ means restriction to $Z$ followed by its exact closed pushforward; equivalently $T\otimes^L k_Z$. No shift occurs. For every $F\in D^+(k_V)$ there is a canonical isomorphism

\[
\phi^{-1}R\phi_*F
\xrightarrow{\sim}
Rq_{1*}\bigl((q_2^{-1}F)_{Z_\gamma}\bigr).
\tag{G10}
\]

This is ordinary direct image, denoted $*$, not direct image with proper support.

*Construction of the comparison.* Write $p_i:Z_\gamma\to V$ for the restricted projections. If $W$ is directionally open, then $p_1^{-1}W\subset p_2^{-1}W$: $x\in W$ and $y-x\in\gamma$ imply $y\in W$. Restriction of sections therefore defines

\[
R(\phi p_2)_*T\longrightarrow R(\phi p_1)_*T
\]

on $D^+(k_{Z_\gamma})$. Apply it to $T=p_2^{-1}F$ and precede it by the derived unit for $p_2$. This gives

\[
R\phi_*F\longrightarrow R\phi_*Rp_{2*}p_2^{-1}F
\longrightarrow R\phi_*Rp_{1*}p_2^{-1}F.
\]

The direct-image composition identifications are valid here because inverse images are exact and hence their right adjoints preserve injectives. Derived adjunction for $\phi$ gives a map from the left side of (G10) to $Rp_{1*}p_2^{-1}F$, which equals its right side. This specifies the comparison, including its direction.

*Convex-neighborhood calculation.* For an ordinary nonempty convex open $U\subset V$, let

\[
E_U=\{(x,y):x\in U,\ y-x\in\gamma\},\qquad B=U+\gamma,
\]

and let $p:E_U\to B$ be projection to $y$. These are ordinary locally compact Hausdorff spaces: $E_U$ is closed in $U\times V$, and $B$ is open in $V$. The fiber over $y$ is $U\cap(y-\gamma)$, which is nonempty and convex. We need more than that assertion about fibers.

For $y_0\in B$, choose $x_0\in U$ with $y_0-x_0\in\gamma$. On a sufficiently small open neighborhood $B_0$ of $y_0$, the formula

\[
\sigma_0(y)=x_0+y-y_0
\]

lies in $U$ and satisfies $y-\sigma_0(y)=y_0-x_0\in\gamma$. It is a local section in the first coordinate. Choose a locally finite partition of unity on the ordinary open set $B$ subordinate to such neighborhoods and form the weighted sum $\sigma(y)$ of these local sections. Local finiteness makes the sum continuous. Convexity of $U$ gives $\sigma(y)\in U$, and convexity of $\gamma$ gives $y-\sigma(y)\in\gamma$. Thus $s(y)=(\sigma(y),y)$ is a global section.

The formula

\[
h_t(x,y)=((1-t)x+t\sigma(y),y)
\]

stays in $E_U$ and is a contraction over $B$ from the identity to $sp$. The relative contraction lemma gives the canonical pullback isomorphism

\[
R\Gamma(U+\gamma;F)\xrightarrow{\sim}
R\Gamma(E_U;p_2^{-1}F).
\tag{G11}
\]

*Stalk comparison.* For ordinary open $U$, the definition of derived direct image and open restriction give

\[
R\Gamma(U;Rp_{1*}p_2^{-1}F)
\simeq R\Gamma(E_U;p_2^{-1}F).
\]

Fix $x\in V$. Ordinary convex open neighborhoods $U$ of $x$ are cofinal among its ordinary neighborhoods; their directional enlargements $U+\gamma$ are cofinal among directional neighborhoods of $x$. Taking the filtered colimit of cohomology in (G11), and using exactness of filtered colimits, identifies the stalks of the two sides of (G10). Under these identifications, the constructed comparison is exactly the pullback in (G11): the unit pulls back sections and the subsequent map restricts them from $p_2^{-1}(U+\gamma)$ to $p_1^{-1}U$. Hence it is an isomorphism at every stalk in every degree. This proves (G10). $\square$

The proof also records why compact fibers alone would have been insufficient. The map $p:E_U\to U+\gamma$ need not be proper; its relative contraction is what gives (G11). By contrast, for compact $K$, the analogous map $\{(x,y):x\in K,y-x\in\gamma\}\to K+\gamma$ is proper: the inverse image of a compact $L$ is closed in the compact set $K\times L$. Its fibers are compact convex. That valid observation does not by itself justify base change for the different, generally nonproper, projection $p_1$ along a closed inclusion $K\hookrightarrow V$.

### SH02-GAM-SUPPORT — A supported projector
**Directional support compatibility (`SH02-GAM-SUPPORT`).** Let $X$ be directionally open, let $Z$ be locally closed in $X_\gamma$, and let $F\in D^+(k_X)$. Then

\[
R\phi_*R\Gamma_Z^{X}F\xrightarrow{\sim}
R\Gamma_Z^{X_\gamma}R\phi_*F.
\tag{G12}
\]

Here $R\Gamma_Z$ is the sheaf of derived sections with the indicated locally closed support convention, equivalently $R\mathcal Hom(k_Z,-)$; it is not global cohomology with support. The statement does not cover an arbitrary ordinarily locally closed set $Z$.

*Proof.* First take $Z=C$ closed in $X_\gamma$. Its complement $W$ is open in both topologies. The localization triangle on $X$ is

\[
R\Gamma_C^X F\longrightarrow F\longrightarrow Rj_*F|_W\longrightarrow.
\]

Apply $R\phi_*$. Direct-image composition and restriction to an open subset identify its third term with $Rj_{\gamma*}(R\phi_*F)|_{W_\gamma}$. This is the third term of the localization triangle for $C$ on $X_\gamma$, and the middle arrow is the same restriction map. The functorial fiber comparison is therefore an isomorphism. Only open restriction is used; no properness statement is needed.

For $Z=W\cap C$ with $W$ directionally open and $C$ directionally closed, use the locally closed support identity

\[
R\Gamma_Z^X F=Rj_*R\Gamma_{C\cap W}^{W}(F|_W).
\]

It follows either from the definition $R\mathcal Hom(k_Z,F)$ and the adjunction for extension by zero along $j$, or by composing the open and closed support functors. Apply the closed case on $W$, then compose direct images. This proves (G12) and fixes its canonical map independently of a chosen locally closed presentation. $\square$

## Worked calculations and problems

### SH02-GAM-EX-SKY — A skyscraper calculation
**A point becomes a reverse cone (`SH02-GAM-EX-SKY`).** Let $a\in V$ and let $M$ be any $k$-module. If $F=M_{\{a\}}$, then

\[
P_\gamma F\simeq M_{a-\gamma}
\]

in degree zero. Indeed $q_2^{-1}F$ is the constant $M$-sheaf on $V\times\{a\}$ extended by zero, and its restriction to $Z_\gamma$ is the same sheaf on $\{(x,a):a-x\in\gamma\}$. Projection to $x$ is a homeomorphism onto the closed subset $a-\gamma$, so its direct image is exact. This checks the sign in (G10). For instance, take $k=\mathbb Z$, $M=\mathbb Z/6\mathbb Z$, $V=\mathbb R^2$, and $\gamma=\{(r,s):r\geq|s|\}$. The result is supported on the closed cone with vertex $a$ opening in the negative first-coordinate direction. Neither flatness of $M$ nor smoothness of the cone boundary is used.

### SH02-GAM-EX-EXTREMES — Extreme cones
**Two extreme projectors (`SH02-GAM-EX-EXTREMES`).** For $\gamma=\{0\}$, $Z_\gamma$ is the diagonal and $P_\gamma=\mathrm{id}$. For $\gamma=V$, the directional topology is indiscrete. Its sheaves of modules are simply modules, and

\[
P_VF\simeq (R\Gamma(V;F))_V.
\]

Thus (G10) includes the pullback of global cohomology as well as the identity projector. If $V=0$, these descriptions coincide.

### SH02-GAM-EXERCISES — Exercises with solutions
**Exercises with solutions (`SH02-GAM-EXERCISES`).**

1. Let $L\subset V$ be a linear subspace and take $\gamma=L$. Identify $V_\gamma$ in terms of the quotient $q:V\to V/L$, and identify its category of sheaves.

   *Solution.* An ordinary open subset $W$ satisfies $W+L=W$ precisely when $W=q^{-1}(O)$ for a subset $O\subset V/L$. Since the quotient map is open, $O$ is open exactly when its inverse image is open. Hence the lattices of open sets of $V_L$ and $V/L$ are isomorphic, including their covers. Sheaves and their restriction maps are therefore the same data on these lattices, so $\mathrm{Sh}(V_L;k)\simeq\mathrm{Sh}(V/L;k)$. The underlying map need not be a homeomorphism: distinct points in a coset of $L$ remain distinct but topologically indistinguishable in $V_L$. This example explains why a Hausdorff assumption on $V_\gamma$ would exclude valid cases.

2. Replace $q_{1*}$ in (G10) by $q_{1!}$. Show that the resulting formula fails for $V=\mathbb R$, $\gamma=[0,\infty)$ and $F=k_V$, with $k\neq0$.

   *Solution.* The sheaf $k_V$ comes from the constant sheaf on $V_\gamma$, so (G8) gives $P_\gamma k_V\simeq k_V$. Proper-support base change for the ordinary projection identifies a stalk of the proposed replacement with $R\Gamma_c([0,\infty);k)$. This complex is zero: compactify the ray by one endpoint to a closed interval, and compute cohomology relative to that endpoint; restriction from the interval to the endpoint is the identity on $k$ and both have zero higher cohomology. Thus the replacement yields zero, not $k_V$. This problem uses the ordinary proper-support base-change theorem as a further course prerequisite; it is not supplied by `SH02-IMP-PROPER-BASECHANGE`, which concerns $R f_*$ for proper $f$.

3. For $V=\mathbb R^2$ and $\gamma=\mathbb R_{\geq0}(1,0)$, describe a directional neighborhood basis at the origin. Explain why replacing $\gamma$ by its ordinary interior would change the topology.

   *Solution.* The sets $B_\epsilon(0)+\mathbb R_{\geq0}(1,0)$ form a basis. They contain the entire nonnegative horizontal ray and a tubular neighborhood with a rounded left end. The ordinary interior of this cone in $\mathbb R^2$ is empty. The equation $W+\varnothing=W$ admits only $W=\varnothing$, so it does not even provide the same topology or a topology on nonempty $V$. Passing to the interior is not allowed in the hypotheses or definitions.

4. State the actual stalk formula obtained in the proof of (G10). Show that a single closed cone cannot replace the neighborhood colimit for arbitrary $F$, even when the cone is pointed and has nonempty interior.

   *Solution.* For every integer $j$,

   \[
   H^j(P_\gamma F)_x
   \simeq\mathop{\mathrm{colim}}_{U\ni x\text{ convex open}}
   H^jR\Gamma(U+\gamma;F).
   \]

   For a counterexample take $V=\mathbb R^2$, $\gamma=\mathbb R_{\geq0}^2$, $k\neq0$, and

   \[
   y_n=(-1/n,n),\qquad F=\bigoplus_{n\geq1}k_{\{y_n\}}.
   \]

   The set of $y_n$ is closed and discrete in $V$: any compact set meets only finitely many of its points. The sheaf direct sum is therefore the closed pushforward of the constant $k$-sheaf on this discrete set. Sections on any open set are a **product** over the points it contains; local finiteness permits arbitrary independently chosen values. The ordinary restriction $F|_\gamma$ is zero, so $R\Gamma(\gamma;F)=0$. On the other hand, $B_\epsilon(0)+\gamma$ contains exactly the $y_n$ with $1/n<\epsilon$. Consequently

   \[
   H^0(P_\gamma F)_0
   \simeq\mathop{\mathrm{colim}}_N\prod_{n>N}k
   \simeq\left(\prod_{n\geq1}k\right)\big/\left(\bigoplus_{n\geq1}k\right)\neq0.
   \]

   The last nonvanishing follows from the class of a constant sequence with nonzero value. Thus replacing the neighborhood colimit by $R\Gamma(x+\gamma;F)$ is false without extra hypotheses. Formula (G7) does not assert such a replacement: it concerns $\phi^{-1}G$, whereas the sheaf $F$ in this problem is arbitrary.

   The same construction diagnoses a closed-set base-change error for the correspondence itself. Let $K$ be the closed Euclidean unit disk and replace $y_n$ by $z_n=(-1-1/n,n)$. No $z_n$ belongs to $K+\gamma$, so $p_2^{-1}F$ restricts to zero on $p_1^{-1}K$. Yet every convex neighborhood $K+B_\epsilon(0)$ has a directional enlargement containing a tail of the $z_n$. Compact-neighborhood continuity of ordinary sections and (G11) therefore give

   \[
   \Gamma(K;p_{1*}p_2^{-1}F)
   \simeq(\prod k)/(\bigoplus k),\qquad
   \Gamma(p_1^{-1}K;p_2^{-1}F)=0.
   \]

   This explicitly rules out base change along $K\hookrightarrow V$ for this nonproper $p_1$. The properness of the *other* projection on a compact slice cannot repair that inference.

## Proof and release boundaries

The advanced statements have been drafted at the full cone generality above. Exercise 2 additionally imports proper-support base change and compact-support localization; it is marked dependency-pending until those course contracts are audited. The unit makes no claim about microsupport characterization, cutoff under proper cones, Fourier–Sato inversion, specialization, or involutivity.

Compare Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://www.numdam.org/item/AST_1985__128__1_0/). In the inspected Numdam scan, printed page numbers are three less than PDF page numbers. Section 1.5.2 defines the directional topology on printed p. 33; Lemma 1.5.4 proves section continuation on pp. 34–35; Lemma 1.5.5, Theorem 1.5.3 and Corollary 1.5.6 supply the underived unit, derived unit and convex-open cohomology comparison on pp. 34–36. These are the precise antecedents for (G2), (G3), (G6) and (G8).

The section proof here follows the same mathematical mechanism: equality of germs propagates along the cone, and a segment in the convex backward slice connects two possible representatives. The presentation makes the local inverse-image representatives and their overlap gluing explicit. Compact continuation (G4) then uses the cofinality in (G5) and a compact convex exhaustion whose interiors are taken in the topological space being exhausted. This is a claim about sheaves pulled back from the directional topology. It is not the false claim, tested in Exercise 4, that one closed cone computes a directional-neighborhood colimit for an arbitrary sheaf.

The source's Proposition 1.5.1 and Lemma 1.5.2, printed pp. 31–33, give the convex acyclicity and interval ingredients behind its derived argument. Here `SH02-GAM-FLABBY-ACYCLIC` invokes the exact compact and exhaustion contracts in [Extending sections on convex sets](convex-acyclicity.md), then the bounded-below acyclic-resolution argument computes the named maps term by term. No ordinary flabbiness of the inverse-image sheaf or Hausdorff property of the directional topology is asserted. The coefficient hypotheses and the zero, full, lower-dimensional and nonpointed cone cases stated at the start are retained.

The correspondence formula (G10) is justified by the additional proof in `SH02-GAM-KERNEL`. Its map is constructed from the derived unit and restriction on directional opens; local sections, a partition of unity and fibrewise convexity provide a contraction over the base for the ordinary projection. For the relative contraction lemma, [Stacks, Tag 09V6](https://stacks.math.columbia.edu/tag/09V6) was compared in the native chapter at [revision a04446e57ec1](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cohomology.tex), label `theorem-proper-base-change`. That theorem applies to the proper interval projection used in (G9); it does not justify base change for the generally nonproper correspondence projection. The actual contraction and neighborhood calculation supply (G11). The skyscraper and escaping-sequence calculations check, respectively, the sign and the failure of the tempting closed-set substitution.

The support comparison (G12) is supplied by open restriction, direct-image composition and the localization triangle for a directionally locally closed support. It neither enlarges that support class nor imports a microsupport characterization. The source's Proposition 3.2.2, printed pp. 58–60, is a later characterization involving microsupport; that separate theorem is not needed for the topology and kernel proofs here. The comparison distinguishes these arguments instead of assigning all of them to one source theorem.

Original programme expression and this source comparison are CC0 1.0 Universal. The cited Astérisque volume retains the Société mathématique de France's 1985 copyright and archive terms. The proper-base-change input retains the Stacks attribution and component terms recorded in [the prerequisite contracts](open-prerequisites.md). Reading access does not relicense either human source. Earlier source attributions remain in private history; no source text, figures or private comparison files are included in the reader.

