# Intersections of supported subanalytic cycles

An intersection starts as a cup product with support. Its degree measures codimension, its coefficient carries an orientation twist, and its support is the actual intersection of the two closed carriers. A dimension bound turns this class into a literal cycle. A different condition, compactness, permits its integration to a scalar.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

Use Subanalytic chains and closed cycle supports, Supports, products and proper images of chains and The dualizing resolution by subanalytic chains for the supported-cycle identity, product signs, proper traces and coefficient resolution. The finite filtered reconstruction in The dualizing complex from oriented simplices will also identify the reverse trace map. The exact current SH-02 prerequisites are closed support as internal Hom, exceptional composition, compact-convex constant acyclicity, the integral orientation-square pairing and normalized trace.

This lesson treats intersections of supported subanalytic cycles, in the framework of subanalytic chains of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §1.

## Put the input classes in codimension degrees

Let \(A\) be a commutative ring of finite global dimension. Let \(X\) be a real analytic \(n\)-manifold, Hausdorff and countable at infinity, with uniformly bounded dimension. Let \(S_j\) be closed subanalytic sets of dimension at most \(p_j\), and \(L_j\) locally free sheaves of finite rank, for \(j=1,2\). Put

\[
 K=S_1\cap S_2,\qquad q_j=n-p_j,\qquad d=p_1+p_2-n.
 \qquad\text{(1)}
\]

Here \(H^r_S(X;E)\) means global cohomology with the indicated closed support. The closed-cycle identity gives

\[
 C_j\in H^{-p_j}_{S_j}(X;\omega_X\otimes_A L_j)
    \simeq \Gamma_{S_j}(X;\mathcal Z_{p_j}(L_j)).
 \qquad\text{(2)}
\]

This uses the dimension bound on \(S_j\) and finite local freeness of \(L_j\). The sheaf-kernel result for arbitrary coefficients alone would not justify every support identification in (2).

Write \(o=\operatorname{or}_X\), with its integral sign structure. Since
\(\omega_X=o[n]\), the same classes have codimension degrees

\[
 C_j\in H^{q_j}_{S_j}(X;o\otimes_A L_j).
 \qquad\text{(3)}
\]

The orientation square has a canonical identification

\[
 o\otimes_A o\simeq A_X.
 \qquad\text{(4)}
\]

Indeed an integral local orientation generator \(e\) gives
\(e\otimes e\mapsto1\). On an overlap it changes to \(-e\), whose square has the same image. Tensoring this integral pairing with \(A\) supplies (4), including in characteristic two. An arbitrary invertible local system need not have this canonical square pairing.

## The actual cup product retains both supports

We specify the supported product rather than choosing an unspecified bilinear map between its endpoint groups. For closed \(S\), let \(A_S\) be the constant sheaf on \(S\), extended by the closed inclusion. The exceptional-support prerequisite gives

\[
 R\Gamma_S E=R\mathcal Hom(A_S,E).
 \qquad\text{(5)}
\]

The left side here is a sheaf object. On stalks \(A_S\) is \(A\) or zero, so it is flat. Restriction and multiplication of constant coefficients give a canonical isomorphism
\(A_{S_1}\otimes_A A_{S_2}\simeq A_K\).

Tensor the two evaluation maps, keeping their displayed order, and curry. This constructs

\[
 R\Gamma_{S_1}E_1\otimes_A^L R\Gamma_{S_2}E_2
       \longrightarrow R\Gamma_K(E_1\otimes_A^L E_2).
 \qquad\text{(6)}
\]

For ordinary sections its evaluation sends the pair of supported homomorphisms to
\((a_1\otimes a_2)\mapsto u_1(a_1)\otimes u_2(a_2)\).
Derived evaluation gives the same map with the Koszul symmetry needed to place each argument next to its homomorphism. Tensoring the global-section evaluation maps and applying (6) gives the global supported cup product. Flat resolutions compute the tensors, injective resolutions compute internal Hom and sections, and boundedness with finite global dimension keeps these operations in the stated derived categories. These constructions commute with restriction and enlargement of closed supports.

Apply (6) to \(E_j=o\otimes L_j\). Their local freeness identifies derived and ordinary coefficient tensor. Using (4), and then reintroducing the dualizing shift, gives

\[
 \begin{aligned}
 &H^{q_1}_{S_1}(X;o\otimes L_1)
       \otimes_A H^{q_2}_{S_2}(X;o\otimes L_2)\\
 &\qquad\longrightarrow
 H^{q_1+q_2}_K(X;o\otimes o\otimes L_1\otimes L_2)\\
 &\qquad\simeq
 H^{-d}_K(X;\omega_X\otimes L_1\otimes L_2\otimes o).
 \end{aligned}
 \qquad\text{(7)}
\]

In the last line,
\(-d+n=2n-p_1-p_2=q_1+q_2\), and the unshifted coefficient is
\(o\otimes L_1\otimes L_2\otimes o\).
All these coefficient factors have degree zero; moving them into the displayed order introduces no extra graded sign.

The image of \(C_1\otimes C_2\) in (7) is
\(C_1\cap C_2\). This is the intersection class with its orientation coefficient and support intact.

## Exchange uses codimensions

The symmetry in a tensor complex sends homogeneous degrees \(q_1,q_2\) to their reversed order with factor \((-1)^{q_1q_2}\). Naturality of the two evaluations in (6) makes the supported cup diagram commute with precisely that factor. Consequently, under the coefficient flip \(L_1\otimes L_2\to L_2\otimes L_1\),

\[
 C_1\cap C_2
   =(-1)^{(n-p_1)(n-p_2)}
            \operatorname{flip}^{-1}(C_2\cap C_1).
 \qquad\text{(8)}
\]

For untwisted inputs, the flip leaves the common output coefficient \(o\) unchanged. This is the source's exchange formula.

This sign differs from the external-product chain sign
\((-1)^{p_1p_2}\). For example two surface cycles in a three-manifold have odd codimension, so intersection changes sign, although swapping their two-dimensional chain factors has sign plus.

If a class of odd codimension is intersected with itself and its coefficient flip is the identity, (8) says \(2(C\cap C)=0\). It forces the self-intersection to vanish when that output group has no \(2\)-torsion. One cannot draw that conclusion in an arbitrary coefficient ring merely from antisymmetry.

## When the class is an actual cycle

Suppose

\[
 d\geq0,\qquad \dim K\leq d.
 \qquad\text{(9)}
\]

The coefficient \(L=L_1\otimes L_2\otimes o\) is still locally free of finite rank. The earlier lowest-dualizing closed-support calculation now applies to \(K\):

\[
 H^{-d}_K(X;\omega_X\otimes L)
       \simeq H^{-d}(K;\omega_K\otimes L|_K)
       \simeq\Gamma_K(X;\mathcal Z_d(L)).
 \qquad\text{(10)}
\]

Thus (7) defines an actual supported cycle intersection

\[
 \Gamma_{S_1}\mathcal Z_{p_1}(L_1)
       \otimes_A\Gamma_{S_2}\mathcal Z_{p_2}(L_2)
 \longrightarrow
 \Gamma_K\mathcal Z_d(L_1\otimes L_2\otimes o).
 \qquad\text{(11)}
\]

**Why the dimension matters.** Exceptional composition for the closed inclusion of \(K\) gives the first equality in (10). If \(\dim K\leq d\), its dualizing complex has no cohomology below degree \(-d\). The lowest global cohomology therefore consists of sections of the lowest cohomology sheaf, which the closed-cycle theorem identifies with supported \(d\)-cycles. This proves the second equality, rather than commuting global sections with a chain colimit.

If \(\dim K<d\), the dualizing bound is stronger and the group in (10) is zero. Equivalently a nonzero pure \(d\)-cycle cannot have smaller-dimensional support. If \(d<0\), the dimension condition \(\dim K\leq d\) forces \(K\) to be empty and the product is zero.

Without (9), (7) still defines a supported cohomology class. Its interpretation as a literal \(d\)-cycle by the lowest-degree argument is unavailable. Exercise 5 gives a nonzero excess-intersection example.

## A scalar needs compact support and a coefficient pairing

Assume \(p_1+p_2=n\), so \(d=0\), and assume \(K\) is compact. Choose an isomorphism

\[
 \lambda:L_1\otimes_A L_2\xrightarrow{\sim}o.
 \qquad\text{(12)}
\]

Combining it with (4) turns the output coefficient of (7) into \(A_X\). A closed compact support has a canonical support-forgetting map into compactly supported cohomology. Define the intersection number by

\[
 \#_\lambda(C_1,C_2)=
 \int_X\!\left(
 H^0_K(X;\omega_X)\longrightarrow H_c^0(X;\omega_X)
 \right)\lambda_*(C_1\cap C_2).
 \qquad\text{(13)}
\]

The integration here is the actual counit
\(Ra_{X!}\omega_X\to A\), where \(a_X:X\to\{\mathrm{pt}\}\).
Under the orientation formula it is
\(H_c^n(X;o)\to A\). It requires no global orientation of \(X\).

The chosen pairing is part of the numerical data. Replacing it by \(u\lambda\), for a unit \(u\in A\), multiplies the number by \(u\). If \(K\) is noncompact there is no corresponding canonical map from all its supported classes to compact cohomology. A finite or compactly supported particular output can still be integrated after its support is checked. None of these statements supplies an unrestricted integral of ordinary global cohomology.

The input carriers themselves need not be compact. Transverse coordinate lines in the plane have noncompact carriers and a single compact intersection point.

## The trace map is the inverse chain comparison

The proper chain map to a point, together with c-softness of the chain terms, gives a morphism

\[
 \varepsilon:Ra_{X!}\mathcal C\simeq a_{X!}\mathcal C
          \longrightarrow A.
 \qquad\text{(14)}
\]

In degree zero it adds the weights of a compact zero-chain. Its other components are zero, because a point has no positive-dimensional chains. Boundary compatibility makes it a chain map. Adjunction gives

\[
 \psi:\mathcal C\longrightarrow a_X^!A=\omega_X.
 \qquad\text{(15)}
\]

Let \(\phi:\omega_X\to\mathcal C\) be the canonical map proved to be an isomorphism in the preceding lesson. We check its actual normalization:

\[
 \varepsilon\circ Ra_{X!}\phi=\operatorname{tr}_{a_X},
 \qquad
 \psi\circ\phi=\operatorname{id}_{\omega_X}.
 \qquad\text{(16)}
\]

The source states the reverse comparison up to sign. In this exposition all cell-incidence maps and traces use the same localization triangles, terminal-minus-initial interval boundary and positive-interval trace. Equation (16) fixes the comparison in these coherent conventions.

**Proof of (16).** First work on a coordinate open set \(U\), with a compatible locally finite subanalytic triangulation of dimension at most \(n\). The pure-layer construction of the cellular dualizing lesson gives a complex

\[
 B^{-r}=\bigoplus_{\dim\sigma=r}
          A_{\overline\sigma}\otimes o_\sigma,\qquad
 \omega_U\simeq B.
 \qquad\text{(17)}
\]

The differential is the oriented closed-face restriction. Each summand maps to its oriented simplex chain in \(\mathcal C_r\). The boundary computations make these maps a chain map \(B\to\mathcal C|_U\). In top degree its cycles identify with \(H^{-n}\omega_U=o_U\), by the same support maps defining \(\phi\). Hence the composite
\(\omega_U\simeq B\to\mathcal C|_U\) is \(\phi|_U\).
To justify the last statement at the derived level, both complexes are quasi-isomorphic to \(o_U[n]\); a degree-zero map between them is determined by its map on this sole cohomology sheaf.

We now keep trace through this reconstruction. Use the finite decreasing skeleton filtration
\(U_k=\{\text{cells of dimension }\leq-k\}\), with \(U_k=U\) below its range and \(U_k=\varnothing\) above zero. For an injective complex \(I\) representing \(\omega_U\), put

\[
 P^k I=\Gamma_{U_k}I,\qquad Q^k=P^kI/P^{k+1}I.
 \qquad\text{(18)}
\]

Every \(P^kI^j\) is injective: closed-support inclusion and its right adjoint preserve injectives under the exact closed-embedding functors. Its inclusion \(P^{k+1}I^j\hookrightarrow P^kI^j\) splits as a sheaf map because the subobject is injective. Thus the quotient terms are also injective, and compact sections preserve these degreewise exact sequences.

The layer \(Q^k\), for \(r=-k\), is quasi-isomorphic to
\(\bigoplus_{\dim\sigma=r}(A_{\overline\sigma}\otimes o_\sigma)[r]\).
Each closed simplex is compact and contractible; the constant-convex acyclicity prerequisite gives compact cohomology \(o_\sigma\) in degree zero and zero otherwise. A compact set meets only finitely many closed cells, so compact sections of the locally finite sum give a direct sum. Consequently

\[
 H^j(\Gamma_c Q^k)=0\ (j\ne k),\qquad
 H^k(\Gamma_c Q^k)=\bigoplus_{\dim\sigma=-k}o_\sigma.
 \qquad\text{(19)}
\]

Apply the same finite pure-filtration reconstruction to the complex
\(\Gamma_c I\). Its pure complex is \(\Gamma_c B\), with the same incidence differential. This computes \(R\Gamma_c(U;\omega_U)\), including the reconstruction map: the construction uses
\(G^k=P^kI^k\cap d^{-1}P^{k+1}I^{k+1}\) and the roofs
\(I\leftarrow G\to B\). Compact sections preserve this intersection. The lowest layer edge maps identify the compact classes in (19) with \(\Gamma_c B^k\); the finite lifting proof then makes both compact-section arrows quasi-isomorphisms. Each \(B^k\) is compact-section acyclic by the closed-simplex calculation, so these are also the derived compact-section comparisons.

This reconstruction is natural for a filtered chain map. Such a map sends each intersection defining \(G^k\) into its target intersection, and sends a layer cycle class to the induced layer cycle class. Its two reconstruction roofs therefore commute. This verifies naturality at the level needed here, rather than relying only on a collapsed spectral sequence.

Represent trace \(\Gamma_c I\to A\) by a map to an injective resolution of \(A\) on the point. Filter that target as the whole resolution for \(k\leq0\) and zero for \(k\geq1\). The trace map is filtered, since the source also has zero filtration above zero. The target's only pure term is \(A\) in degree zero. On the source's zero-dimensional skeleton, exceptional composition identifies its restriction with trace on the discrete vertex set. Trace on each point is the identity, and compact sections have finitely many nonzero vertex weights. Hence the induced pure map is

\[
 \Gamma_c B^0=\bigoplus_{\text{vertices }v}A[v]
       \longrightarrow A,\qquad \sum_v a_v[v]\longmapsto\sum_v a_v.
 \qquad\text{(20)}
\]

In every negative degree it is zero. Naturality of the reconstruction shows that this is exactly trace on \(\omega_U\) under (17), with no additional sign. It is also the composite
\(\Gamma_c B\to\Gamma_c\mathcal C|_U\xrightarrow{\varepsilon}A\).
This proves the first equality of (16) on \(U\).

Adjunction sends \(\operatorname{tr}_{a_U}\) to
\(\operatorname{id}_{\omega_U}\); thus it gives the second equality there. Open extension of compact supports and the normalized trace composition show that \(\psi,\phi\) restrict to these same local maps. They agree on every coordinate neighborhood, so the second equality holds globally. Since \(\phi\) is an isomorphism, \(\psi=\phi^{-1}\), and its global adjoint gives the first equality as well. \(\square\)

This argument uses the actual finite filtered roofs and the vertex trace. It applies directly over the standing ring \(A\), without a comparison through differential forms or an unproved change-of-coefficients sign rule.

## Exercises with complete solutions

### Two planes expose the codimension sign

*Difficulty: Intermediate.*

Orient \(\mathbb R^3\) by \(dx\wedge dy\wedge dz\). Let
\(S_1=\{x=0\}\) have tangent orientation \(dy\wedge dz\), and
\(S_2=\{y=0\}\) have tangent orientation \(dz\wedge dx\).
Compute their intersection as an oriented cycle. Compare the intersection exchange sign with the external-product exchange sign.

**Solution.** With normal coordinate first, \(dx\) is the positive Thom generator for \(S_1\), since
\(dx\wedge dy\wedge dz\) is the ambient orientation. The positive normal generator for \(S_2\) is \(dy\), since
\(dy\wedge dz\wedge dx\) has that same orientation. Their supported cup is the ordered normal generator \(dx\wedge dy\), leaving tangent orientation \(dz\) on the \(z\)-axis. Thus
\[
 C_1\cap C_2=[\{x=y=0\}]_{\text{increasing }z}.
 \qquad\text{(21)}
\]
Here \(p_1=p_2=2\), \(n=3\), \(d=1\), and the intersection has dimension one, so (11) applies. Reversing the cup gives
\(dy\wedge dx=-dx\wedge dy\), the negative of this line. Equation (8) gives the same sign because both codimensions are one. The external product of two surface chains instead exchanges with \((-1)^{2\cdot2}=+1\). These are two distinct operations.

The normal generators can be read as supported cohomology generators rather than differential forms: each coordinate line's degree-one class is the endpoint-difference generator, and their ordered compact product changes by minus when its two factors are exchanged.

### Weighted crossings and coefficient orientation

*Difficulty: Intermediate.*

In the plane oriented by \(dx\wedge dy\), let the horizontal line be oriented by increasing \(x\), with weight \(a\in A\). Orient the vertical lines at \(x=-1,1\) by increasing \(y\), with weights \(b,c\). Compute both orders of the intersection number with the coefficient pairing specified by this plane orientation. What happens over \(\mathbb Z/2\), or if the coefficient pairing is negated?

**Solution.** For the horizontal line, the positive normal-first generator is \(-dy\), because
\((-dy)\wedge dx=dx\wedge dy\). For a vertical line it is \(dx\), because \(dx\wedge dy\) is positive. Thus the horizontal-first cup is
\((-dy)\wedge dx=dx\wedge dy\), positive at each crossing.
Both crossings are isolated and compact, and
\[
 C_H\cap C_V=ab[(-1,0)]+ac[(1,0)],\qquad
 \#(C_H,C_V)=ab+ac.
 \qquad\text{(22)}
\]
Vertical first gives \(dx\wedge(-dy)=-dx\wedge dy\), so its number is
\(-ab-ac\), in agreement with odd codimensions.

Over \(\mathbb Z/2\), minus equals plus. The two orders give the same number; two unit crossings have total \(1+1=0\). This is coefficient arithmetic, not a reason to drop the integral orientation conventions before reducing them. Negating the chosen pairing negates every scalar number by (13). The inputs are noncompact, but the two-point intersection is compact.

### Strict dimension forces the product to vanish

*Difficulty: Intermediate.*

Suppose two three-cycle carriers in a real four-manifold have intersection of dimension at most one. Determine the expected cycle dimension and the product. Contrast this with two coordinate hypersurfaces whose intersection has dimension two. Explain the case \(p_1+p_2<n\) under the dimension condition.

**Solution.** For \(n=4\), \(p_1=p_2=3\), the expected dimension is
\(d=3+3-4=2\). If \(\dim K\leq1\), then the supported degree-\(-2\) dualizing group in (10) is zero. Thus the intersection is zero, even if the two inputs themselves are nonzero. This is the lowest-degree bound, equivalently the impossibility of a nonzero pure two-cycle supported on a set of dimension at most one.

For coordinate hypersurfaces \(x_1=0,x_2=0\) in \(\mathbb R^4\), their intersection is the two-plane \(x_1=x_2=0\). Its dimension equals \(d\), and the two ordered normal degree-one generators cup to its oriented two-cycle, with the sign changed when they are exchanged.

If \(p_1+p_2<n\), then \(d<0\). A nonempty subanalytic set has nonnegative dimension. Hence \(\dim K\leq d\) forces \(K=\varnothing\), so the supported product is zero. This conclusion uses the stated dimension condition; it is not a general replacement for the supported-cohomology construction.

### Compact integration has a domain

*Difficulty: Advanced.*

Let \(X=\mathbb R\) with its positive orientation. Intersect its whole-line orientation cycle with the zero-cycle having weight \(a_m\) at each integer \(m\), where the family is locally finite. Describe the intersection class, when a scalar integral is available, and why merely choosing \(a_m=(-1)^m\) does not create an unrestricted scalar intersection number.

**Solution.** Here \(n=1\), \(p_1=1\), \(p_2=0\), so \(d=0\).
The whole-line class is degree zero after the orientation shift, and acts as the unit in the supported cup. The intersection is the same zero-cycle
\[
 \sum_{m\in\mathbb Z}a_m[m].
 \qquad\text{(23)}
\]
Its closed carrier is a closed locally finite zero-dimensional subanalytic set, so the cycle interpretation is valid. An orientation trivializes the coefficient pairing required by (12).

If only finitely many \(a_m\) are nonzero, the actual output support is compact and its integral is their finite sum. If infinitely many are nonzero, its support is noncompact. The chain sheaf admits these locally finite weights, but the map to the point in (14) is defined on compact sections. It cannot collapse this infinite carrier properly. Alternating weights supply no algebraic convergence or compact-support map; neither an infinite sum in \(A\) nor a summation prescription is part of (13). Thus they do not define that scalar intersection number.

On a nonorientable manifold, two constant input coefficient lines do not by themselves give the global pairing \(A\otimes A\simeq o\). Compactness alone would not supply the missing coefficient identification.

### An excess self-intersection can be nonzero

*Difficulty: Advanced.*

Take \(X=\mathbb{CP}^2\), with its complex orientation and integral coefficients. Let
\(L=\{z_2=0\}\) be its complex projective line, oriented complexly. Explain why its supported self-intersection has a well-defined scalar number even though the dimension bound for a literal zero-cycle fails. Compute that number using a compact motion to
\(L'=\{z_1=0\}\).

**Solution.** The real dimensions are \(n=4\), \(p_1=p_2=2\), so \(d=0\).
The self-intersection carrier is \(L\), of real dimension two; therefore (9) fails. Nevertheless (7) defines a supported degree-zero dualizing class on this compact carrier. The complex orientation supplies \(A\otimes A\simeq o_X\), so (13) defines its scalar number. This does not identify the supported class canonically with a literal point chain by (10).

Rotate the two coordinates \(z_1,z_2\) through angle \(\theta\in[0,\pi/2]\). These complex linear invertible maps induce an analytic motion of \(L\) to \(L'\). The carrier of the parameterized projective line is compact, so the chain strip and its image are properly supported. Its boundary is the difference of the endpoint line cycles, with the ordered strip sign fixed in the chain-operation lesson. Thus the two cycles have the same ordinary dualizing cohomology class by the resolution theorem. Forgetting support in (7) is compatible with cup, and \(X\) is compact, so
\(\#(L,L)=\#(L,L')\).

The distinct lines meet only at \([1:0:0]\). In coordinates
\(u=z_1/z_0,\ v=z_2/z_0\) there, \(L\) is \(v=0\) and \(L'\) is \(u=0\).
Their normal generators are the positive real two-plane generators of \(v\) and \(u\), respectively. Exchanging these degree-two generators has sign \((-1)^{2\cdot2}=+1\), so their product is the positive four-dimensional local generator in the complex \((u,v)\)-orientation. The compact point trace is \(+1\). Hence
\[
 \#(L,L)=\#(L,L')=1.
 \qquad\text{(24)}
\]
This uses the explicit motion and the one transverse coordinate calculation, without assuming a presentation of the cohomology ring of \(\mathbb{CP}^2\). It shows why an excess supported class cannot simply be declared zero or automatically read as a lowest-dimensional supported cycle.

### Collapse and the actual reverse comparison

*Difficulty: Advanced.*

On an analytic star-shaped open ball \(U\subset\mathbb R^n\), let \(I=(0,1)\) have positive orientation and define
\(F(x,t)=(1-t)x\), with centre \(0\in U\).
For a compact \(p\)-chain \(\alpha\), compute
\[
 H_p(\alpha)=(-1)^{p+1}F_*(\alpha\boxtimes[I]).
 \qquad\text{(25)}
\]
Check properness and the chain-homotopy equation. Then explain which step in (17)–(20) identifies augmentation with the actual dualizing trace, rather than merely proving both are nonzero.

**Solution.** The closed carrier
\(\operatorname{supp}(\alpha)\times[0,1]\) is compact, and \(F\) maps it into \(U\), since \(U\) is star-shaped. The map is proper on this carrier, so the pushforward is valid. It produces a compact chain. There is no claim of properness on all \(U\times\mathbb R\).

With the \(U\)-factor first,
\[
 \partial(\alpha\boxtimes[I])
   =(\partial\alpha)\boxtimes[I]
           +(-1)^p\alpha\boxtimes([1]-[0]).
 \qquad\text{(26)}
\]
Multiplication by \((-1)^{p+1}\) makes the endpoint part
\(\alpha\boxtimes[0]-\alpha\boxtimes[1]\).
The other part cancels \(H_{p-1}(\partial\alpha)\), whose coefficient is \((-1)^p\). Boundary compatibility of \(F_*\) yields
\[
 \partial H_p+H_{p-1}\partial
       =\operatorname{id}-i_*\varepsilon,\qquad
       i:\{0\}\hookrightarrow U.
 \qquad\text{(27)}
\]
For \(p>0\) the endpoint collapse has zero image by target dimension. For \(p=0\) it is the point chain with total input weight. Thus the compact chain complex has cohomology \(A\) in degree zero via augmentation and zero in all negative degrees. This remains true at the top degree: its purported compact cycle must be zero because its endpoint difference is the boundary of a degree-\((n+1)\) image, which the target cannot carry.

This contraction alone would show augmentation is an isomorphism on a ball. It would leave a possible scalar ambiguity in its comparison with trace. The finite pure-filtration reconstruction resolves that ambiguity: trace is a filtered map, its induced zero-layer map is the identity trace on each vertex, and naturality of the actual reconstruction roofs identifies it with the sum-of-weights map (20). The canonical oriented-cell map to \(\mathcal C\) has the same top-cycle map as \(\phi\). These two facts give (16) and therefore \(\psi=\phi^{-1}\) in the stated conventions. A separately chosen scalar isomorphism or an unspecified quasi-isomorphism would not prove this conclusion.
