# Smooth fibres, comparison for a given triangulation, and lens spaces

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0. No independent AI review is recorded.*

A regular smooth fibre has a trivial normal bundle, and its signature is a cup-product evaluation of the ambient L-class. We prove that formula, including a product over a ball of regular values. We then compare the combinatorial and smooth classes for each **given finite smooth-compatible triangulation**, using controlled affine interpolation, an explicit PL retraction onto a polyhedral sphere, and a normal-graph contraction. Finally we compute lens-space tangent classes and exhibit nonzero integral torsion that rational coefficient change loses. Six original graded exercises have complete solutions.

This is a continuation of assigned lesson15. The comparison includes all degrees and descent for an unoriented smooth manifold, but it retains its given-triangulation hypothesis. Existence and compact boundary-relative compatibility, together with the separate integral-refinement obstruction, are proved in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md).

SectionsA–H referenced below belong to [Combinatorial L-classes and PL fibres](combinatorial-l-classes-and-piecewise-linear-fibres.md), where the full cohomotopy, rational homology duality, PL approximation, fibre-signature and stabilization proofs are given. Other exact prerequisites are [Vector bundles](vector-bundles-and-their-constructions.md), [Classifying maps and coverings](grassmannians-and-classifying-maps.md), [Thom and Euler classes](thom-classes-and-euler-classes.md), [Gysin and projective splitting](gysin-sequence-and-projective-splitting.md), [Chern classes](chern-classes-and-the-integral-universal-ring.md), [Pontryagin classes](pontryagin-classes-and-oriented-universal-cohomology.md), [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), [Thom spaces and transversality](thom-spaces-and-the-pontryagin-thom-construction.md), and [The signature theorem](multiplicative-sequences-and-the-signature-theorem.md). All coefficients, orientations, dimensional ranges and used proof locators were checked.

## I. Smooth regular fibres and their signature

This section proves the differentiable fibre formula, including the product neighbourhood used in comparison. Let \(M^n\) be a smooth closed oriented manifold, let \(k\geq1\), and suppose \(n-k=4i\), with \(i\geq0\). A regular value of a smooth map \(f:M\to S^k\) may have an empty inverse image; its signature is then zero. Orient a nonempty fibre by putting its tangent orientation first and the positive target orientation second.

The complete analytic prerequisites are [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), Lemma3.1, for local inverses and flows, and [Thom spaces](thom-spaces-and-the-pontryagin-thom-construction.md), TheoremA.2 and LemmaG.1, for Sard and inverse-image normal bundles. The Thom class, right-cap convention and dual-submanifold evaluation are proved in the Thom/Euler chapter and manifold-duality Section4. We use the full signature theorem proved in signature TheoremE.3, rather than assuming a signature formula as an additional input.

### I.1. A product over a ball of regular values

**Lemma I.1 — Compact regular fibres.** The regular values of \(f\) form a dense open subset of \(S^k\). At every such value \(y\), its fibre \(F_y=f^{-1}(y)\) is a smooth closed \((n-k)\)-manifold, or is empty, and
\[
TM|_{F_y}/TF_y\cong F_y\times T_yS^k.
\tag{I.1}
\]
In particular its normal bundle is trivial.

**Proof.** Failure of surjectivity of a derivative is a closed condition: in coordinate frames it is the simultaneous vanishing of all maximal minors. The critical set is therefore closed in compact \(M\); its image is compact and hence closed in the Hausdorff sphere. Its complement, the regular-value set, is open. The proved manifold Sard theorem says its complement has measure zero in each target chart, and thus contains no nonempty open subset. This proves density. At a fibre point, complete the \(k\) target coordinate functions with \(n-k\) source coordinates to obtain an invertible derivative. The local inverse theorem makes them a coordinate system; the fibre is the zero level of the last \(k\) coordinates. Its tangent space is \(\ker Df\), so the induced quotient map to \(T_yS^k\) is an isomorphism, and these maps glue smoothly. This also follows from the complete inverse-image proof in Thom LemmaG.1. The fibre is closed in compact \(M\) and has no boundary. A metric identifies its normal quotient with its orthogonal normal bundle. If it is empty all assertions are interpreted on the empty space. ∎

**Lemma I.2 — The proper regular-ball product.** If \(y_0\) is a regular value, there is a positively oriented target coordinate ball \(B\), centred at \(y_0\), and a diffeomorphism
\[
\Psi:F_{y_0}\times B\longrightarrow f^{-1}(B),
\qquad f\Psi(x,z)=z,
\tag{I.2}
\]
where target coordinates identify \(y_0\) with zero. It sends \((x,0)\) to \(x\) and preserves the fibre-first product orientation.

**Proof.** Choose a coordinate ball of radius \(3r\) whose closure is inside the regular-value set and inside a target chart. Write \(q\) for the coordinate form of \(f\) on its inverse image \(U\). A smooth metric on \(M\) and the Euclidean target metric give the adjoint of its surjective derivative. The bundle map
\[
A_p=Dq_p^*\bigl(Dq_pDq_p^*\bigr)^{-1}:
\mathbb R^k\longrightarrow T_pM
\tag{I.3}
\]
is smooth, since its positive definite \(k\)-by-\(k\) Gram matrix is invertible, and \(Dq_p A_p=1\). For \(z\in B_r(0)\) define the smooth field \(V_z(p)=A_pz\). The local flow lemma, with its proved parameter dependence, applies to this field. Along an integral curve,
\[
\frac d{dt}q(p(t))=z.
\tag{I.4}
\]
Starting at \(x\in F_{y_0}\), a curve for \(0\leq t\leq1\) therefore stays over the segment \(tz\). Its image stays in the compact subset \(q^{-1}(\overline B_r)\) of \(U\), so it exists for the whole interval. Here is the continuation detail. On a compact subset inside a smooth field's domain, finitely many coordinate balls provide a positive common existence time for initial points in smaller balls, by the bounds in the local-flow proof. A finite-time trajectory confined to this subset can consequently be extended past every proposed finite terminal time. This rules out termination before time one. The same argument applies to the backward curve starting at any \(p\) with \(q(p)=z\): for \(-1\leq t\leq0\), its target coordinate is \((1+t)z\), and it stays in the same compact subset.

Set \(\Psi(x,z)=\operatorname{Fl}^{V_z}_1(x)\). Its inverse is
\[
p\longmapsto\bigl(\operatorname{Fl}^{V_{q(p)}}_{-1}(p),q(p)\bigr).
\tag{I.5}
\]
Flow uniqueness proves that these maps are inverse. The local parameter-dependence proof, continued over the compact time interval, proves both are smooth. At \((x,0)\) the derivative is the identity on \(TF_{y_0}\), followed in the target directions by the positive normal lifts \(A_x\). This is precisely the fibre-first orientation. The determinant sign of a diffeomorphism is locally constant and stays the same along the path \((x,tz)\); thus it is positive throughout the product. If the initial fibre is empty, first shrink the ball to miss the compact image \(f(M)\), and both sides are empty. ∎

The proof uses properness through compactness, rather than assuming that an arbitrary submersion is globally a product over a ball.

### I.2. The smooth fibre formula

Write \(L_i(TM)=L_i(p_1(TM),\ldots,p_i(TM))\), using rational coefficients, and let \(u\in H^k(S^k;\mathbb Z)\) be its positive generator.

**Theorem I.3 — Signature of a regular inverse image.** For every regular value \(y\),
\[
\sigma(F_y)=
\left\langle L_i(TM)\smile f^*u,[M]\right\rangle.
\tag{I.6}
\]
Thus the signature is independent of the regular value, even when the regular-value set has several components. It also depends only on the homotopy class of the map.

**Proof.** Let \(j:F_y\hookrightarrow M\). The quotient (I.1), split by a metric, gives
\[
j^*TM\cong TF_y\oplus\varepsilon^k.
\tag{I.7}
\]
Naturality, the rational Whitney formula and normalization on a trivial bundle give \(j^*L_i(TM)=L_i(TF_y)\). The full signature theorem therefore says
\[
\sigma(F_y)=\left\langle j^*L_i(TM),[F_y]\right\rangle.
\tag{I.8}
\]
We identify the dual class with the actual pulled-back sphere generator, including its orientation. Let \(u_y\in H^k(S^k,S^k-\{y\};\mathbb Z)\) be the positive point-local class, whose image is \(u\). Pullback along the map of pairs
\[
(M,M-F_y)\longrightarrow(S^k,S^k-\{y\})
\]
gives a relative class. In the product (I.2) it is the positive generator in the normal ball factor. Equivalently, in any local inverse-image chart its normal-coordinate derivative is the oriented identity. Thom-class uniqueness therefore identifies this pullback with the Thom class of the oriented normal bundle of \(F_y\). Its absolute image is exactly the dual submanifold class \(f^*u\).

The proved right-cap calculation in manifold Section4 now gives
\[
j_*[F_y]=R_{f^*u}[M],
\qquad
\langle a\smile f^*u,[M]\rangle=
\langle j^*a,[F_y]\rangle
\tag{I.9}
\]
for every \(a\in H^{n-k}(M;\mathbb Q)\). The order in (I.9) is fibre class first, target class last; no unrecorded cap sign is used. Substitute \(a=L_i(TM)\) in (I.8). If the fibre is empty, the map factors through \(S^k-\{y\}\), which is contractible, so \(f^*u=0\) and both sides of (I.6) vanish. This proves the formula in all cases. Its right side has no dependence on \(y\), and homotopic maps give the same cohomology pullback. ∎


### I.3. A divisibility constraint on projective-space sphere maps

Let \(x=c_1(\gamma^*)\) be the positive generator on \(\mathbb {CP}^m\), with its complex orientation. For \(m\geq5\), let \(f:\mathbb {CP}^m\to S^{2m-8}\) be continuous and write
\[
f^*u=a x^{m-4},\qquad a\in\mathbb Z.
\tag{I.10}
\]
Then
\[
D_m\mid a,\qquad
D_m=\frac{90}{\gcd(90,5m^2+3m-2)}.
\tag{I.11}
\]
In particular, \(9\mid a\) when \(m\geq6\) is divisible by three. This is a necessary condition on the image of sphere pullback; it does not assert realization of every permitted multiple.

**Proof.** The integral projective-space ring makes (I.10) the unique possible form of the pullback. The smooth sphere approximation proved in the strict-range proof of TheoremJ.6 applies to any continuous sphere map on a compact smooth manifold, independent of that theorem's dimension inequality: a smooth partition of unity averages nearby unit-vector sample values, and normalization of the average and straight homotopy gives a homotopic smooth map. Thus replace \(f\) by such a smooth map without changing \(a\).

The stable complex tangent identity in Chern Section5 gives
\[
p(T\mathbb {CP}^m)=(1+x^2)^{m+1},\qquad
p_1=(m+1)x^2,\quad p_2=\binom{m+1}{2}x^4.
\tag{I.12}
\]
The already proved signature polynomial \(L_2=(7p_2-p_1^2)/45\) consequently gives
\[
L_2(T\mathbb {CP}^m)=\frac{5m^2+3m-2}{90}\,x^4.
\tag{I.13}
\]
Sard provides a regular value, possibly with empty fibre. Its fibre is an oriented eight-manifold, and TheoremI.3 says its integer signature is
\[
\sigma(F)=\frac{a(5m^2+3m-2)}{90}.
\tag{I.14}
\]
Here \(\langle x^m,[\mathbb {CP}^m]\rangle=1\); this is the proved projective normalization. Therefore \(90\mid a(5m^2+3m-2)\). Divide both factors by their common positive greatest common divisor. The remaining factor of \(5m^2+3m-2\) is relatively prime to \(D_m\), so the integer Bézout identity implies \(D_m\mid a\), proving (I.11).

If \(3\mid m\), the numerator \(5m^2+3m-2\) is congruent to one modulo three. It is therefore relatively prime to nine, and \(90\mid a(5m^2+3m-2)\) forces \(9\mid a\). For example \(D_{12}=45\), so in that case the same calculation gives the stronger necessary condition \(45\mid a\). The target dimension and \(m\geq5\) ensure a sphere of dimension at least two; no unstable rational cohomotopy assertion is used in this integrality argument.

For \(5\leq m\leq8\), an elementary cup-product obstruction is stronger still: \(a=0\). Indeed the sphere generator has square zero, so
\[
0=f^*(u^2)=a^2x^{2m-8}.
\tag{I.15}
\]
In this range \(0<2m-8\leq m\); the displayed projective power generates a torsion-free integer cohomology group. Thus \(a^2=0\) as an integer and \(a=0\). For larger \(m\) this power is zero by dimension, which removes this particular obstruction without asserting any realization result. ∎

**Exercise I.4 — Easy: disconnected regular-value sets.** Suppose two regular values lie in different components of the regular-value set, and no path between them avoids critical values. Prove their fibre signatures are equal. Also determine the consequence of one fibre being empty.

**Solution.** Apply (I.6) to both values; both signatures equal its same cup-product evaluation. This argument requires neither a regular-value path nor a trivialization across the critical values. If one fibre is empty the proof shows \(f^*u=0\), and the common evaluation is zero. Hence every regular fibre has signature zero, though other fibres may be nonempty. ∎

**Exercise I.5 — Medium: a normal bundle and an L-class.** Prove that the normal quotient of a regular fibre is canonically trivial, identify the induced tangent orientation, and show \(L(TF)=j^*L(TM)\) in every degree. Explain the coefficient restriction.

**Solution.** The derivative induces the smooth quotient isomorphism \(TM|_F/TF\to F\times T_yS^k\); choose a positive basis of \(T_yS^k\) to trivialize it. Its inverse lifts through a metric complement, producing (I.7). Define the tangent orientation by requiring this ordered sum, tangent first and chosen normal basis last, to give the ambient orientation. The rational Pontryagin Whitney formula and the multiplicative-sequence theorem give \(j^*L(TM)=L(TF)L(\varepsilon^k)=L(TF)\). Rational coefficients remove the integral two-torsion discrepancy in the general real Pontryagin Whitney formula, and the L-polynomials themselves have rational coefficients. No integral characteristic-class equality is inferred from this L-class identity. ∎


## J. Comparison for a given smooth-compatible triangulation

We prove a precise conditional comparison: **given** a finite smooth-compatible triangulation \(t:K\to M\) of a smooth closed oriented manifold, the combinatorial classes of Sections F–G pull back the smooth Hirzebruch L-classes. A smooth-compatible triangulation means that the restriction of \(t\) to every closed simplex extends smoothly to a neighbourhood in its affine hull and has full rank there along the simplex. The map \(t\) is a homeomorphism. We do not assume it is globally smooth across its faces.

This proof supplies the comparison without using uniqueness or relative extension of smooth triangulations. Existence is a separate prerequisite, supplied in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md); no existence claim follows merely by fixing \(t\).

### J.1. A PL retraction onto the polyhedral sphere

Realize the boundary \(Q\) of a \((k+1)\)-simplex in \(\mathbb R^{k+1}\), with the origin in the simplex interior. Its radial homeomorphism
\[
s:Q\longrightarrow S^k,\qquad s(x)=x/\|x\|
\tag{J.1}
\]
is smooth and of maximal rank on every closed facet and its faces. Indeed a facet lies in a hyperplane \(\ell(x)=1\). The derivative of radial projection has radial kernel; this kernel has zero intersection with the tangent hyperplane \(\ell(v)=0\). The same argument applies to lower-dimensional faces. Choose the orientation of \(Q\) to make \(s\) positive.

**Lemma J.1 — PL annular retraction.** For \(0<a<1<b\) there is a finite PL retraction
\[
r:\mathcal A_{a,b}\longrightarrow Q,
\qquad \mathcal A_{a,b}=\{\lambda x:x\in Q,\ a\leq\lambda\leq b\},
\tag{J.2}
\]
which fixes every point of \(Q\). If \(R=\max_{v\text{ a vertex of }Q}\|v\|\), then
\[
\|r(x)-x\|\leq R\max(1-a,b-1).
\tag{J.3}
\]

**Proof.** Over each simplex \(T\) of \(Q\), the region between \(aT\) and \(bT\) is its straight convex frustum. Triangulate it compatibly using the ordered prism triangulation already proved in LemmaE.2. Here is the explicit verification that its images really are straight simplices. If \(T\subset\{\ell=1\}\), the map
\[
(u,\tau)\longmapsto\frac{ab}{b-(b-a)\tau}\,u
\quad(u\in T,\ 0\leq\tau\leq1)
\tag{J.4}
\]
is a projective homeomorphism from \(T\times I\) to the frustum. Its inverse sends \(x\) to
\[
u=x/\ell(x),\qquad
\tau=\frac{b-ab/\ell(x)}{b-a}.
\]
The denominator in (J.4) is positive. A projective map with such a denominator sends every convex simplex exactly to the convex hull of its vertex images: for a convex combination of vertices, the image is their image combination with weights multiplied by the positive vertex denominators and then normalized. Applying the inverse proves equality, rather than just inclusion. Thus the prism simplices become a genuine straight triangulation, and the constructions agree on shared faces. Make this construction separately between \(aQ,Q\) and between \(Q,bQ\), using identical triangulations on their common middle layer.

Send the three vertices \(av,v,bv\) to \(v\), and extend affinely on each frustum simplex. Each image lies in its original face of \(Q\), so these maps glue, and their restriction to \(Q\) is the identity. For a point written as a convex combination of frustum vertices \(\lambda_jv_j\), its displacement under this affine map is \(\sum_j c_j(1-\lambda_j)v_j\). The coefficients are nonnegative and sum to one, and \(\lambda_j\) is one of \(a,1,b\). The triangle inequality proves (J.3). ∎

Write the defining facet forms of the full simplex as \(\ell_\nu(x)\leq1\) and put \(\mu(x)=\max_\nu\ell_\nu(x)\). Its boundedness and the origin-interior condition imply \(\mu(x)>0\) for \(x\ne0\), and \(Q=\{\mu=1\}\). The annulus in (J.2) is \(a\leq\mu\leq b\). The function \(\mu\) is Lipschitz with constant \(C=\max_\nu\|\ell_\nu\|\).

Consequently, if \(h:K\to Q\) is continuous and \(H:K\to\mathbb R^{k+1}\) is PL with \(\sup\|H-h\|<\eta\), choose \(a=1-2C\eta\), \(b=1+2C\eta\), with \(2C\eta<1\). The whole straight homotopy from \(h\) to \(H\) lies in that annulus. Its composition with \(r\) gives a homotopy from \(h\) to the PL map \(g=rH\), and
\[
\sup\|g-h\|\leq\eta+2RC\eta.
\tag{J.5}
\]
Where \(H\) already takes values in \(Q\), this construction preserves it exactly.

### J.2. Subdivisions with controlled shapes

An arbitrarily fine subdivision need not have controlled shapes. We provide the required family, rather than assuming a derivative estimate from small diameters alone.

**Lemma J.2 — Compatible shape control and affine interpolation.** Give the vertices of a finite complex one order. There are face-compatible subdivisions \(K_N\), \(N=1,2,\ldots\), whose simplex diameters are at most \(C_0/N\). In each original top simplex, the inverse of the edge-coordinate matrix of any subdivided top simplex has norm at most \(C_1N\), with constants independent of \(N\). If a map is smooth on the closed original simplex, its affine vertex interpolants converge to it in first derivatives, uniformly on the subdivided simplices. They also converge uniformly in values.

**Proof.** In the ordered standard simplex with coordinates \(\lambda_0,\ldots,\lambda_p\), use cumulative coordinates
\[
y_j=\lambda_j+\cdots+\lambda_p\quad(1\leq j\leq p).
\]
Its image is \(1\geq y_1\geq\cdots\geq y_p\geq0\). Divide the ambient \(y\)-space into cubes of side \(1/N\). Triangulate each cube by the staircase simplices whose vertices start at its lower corner and add the coordinate unit increments in a permutation order. These simplices tile the cube: order the fractional coordinates of a point, and their consecutive differences give its nonnegative barycentric coefficients in the corresponding staircase. Equal fractions give shared faces, so neighbouring cubes have the same induced face triangulations.

The hyperplanes \(y_j=y_{j+1}\), \(y_1=1\), and \(y_p=0\) are subcomplexes. For the equality hyperplane, if the two grid indices agree it is the equality of two fractional coordinates and hence a staircase face; if they differ, a cube either stays on one side or meets the hyperplane only on its boundary. The constant-coordinate cases are grid faces. Thus the ordered simplex is a union of these staircase simplices. On a face \(\lambda_j=0\), two successive cumulative coordinates merge; on the end faces a coordinate is deleted. The induced staircase triangulation, with the merged coordinates tied, is exactly the same construction in the surviving ordered vertices. This proves compatibility on all source faces.

Every full-dimensional small simplex in the cumulative coordinates is \(1/N\) times a translate of one of finitely many permutation staircase shapes. The fixed linear change back to barycentric coordinates preserves finiteness of this shape list and its nonsingularity. This proves the diameter and inverse-edge bounds. There are finitely many original simplices, so take common constants after their affine identifications.

For the derivative assertion let \(E=[v_1-v_0,\ldots,v_p-v_0]\) be the small simplex's edge matrix, and let \(A\) be the derivative of the affine interpolant. The fundamental theorem of calculus along each edge gives
\[
\bigl\|A E-Dh(v_0)E\bigr\|
\leq C_2\operatorname{diam}(\sigma)\,\omega(\operatorname{diam}(\sigma)),
\tag{J.6}
\]
where \(\omega(d)\to0\) is a common modulus of continuity of \(Dh\) on the original closed simplex. Multiplication by \(E^{-1}\) bounds \(\|A-Dh(v_0)\|\) by \(C_3\omega(C_0/N)\). At any other point in the small simplex the derivative differs from \(Dh(v_0)\) by at most this same modulus. This proves uniform derivative convergence. The value estimate follows either by integrating these derivatives or directly because interpolation is a convex combination of vertex values whose oscillation tends to zero. Apply the argument to each original closed simplex and its smooth extension. ∎

### J.3. Fibre stability for a continuous map with smooth pieces

We need stability of the whole fibre, not only surjectivity on the interiors of the small simplices.

**Lemma J.3 — A finite-piece Lipschitz bound.** Suppose a continuous function on a convex ball agrees, on finitely many relatively closed sets covering that ball, with smooth functions defined on neighbourhoods of those sets. If each such local extension has derivative norm at most \(L\) near every point of its assigned set, then the function is \(L\)-Lipschitz. The same assertion applies to a segment covered by these sets and their local extensions.

**Proof.** At a point \(x\), discard the finitely many closed sets not containing \(x\), by shrinking its neighbourhood to miss them. Every remaining extension has the common value of the continuous function at \(x\). Its derivative bound and a smaller convex neighbourhood give
\(\|h(y)-h(x)\|\leq L\|y-x\|\) for \(y\) sufficiently near \(x\), whichever remaining piece contains \(y\). This is a centred local bound at each point, with one constant \(L\).

To pass to the whole segment, project onto any fixed unit vector in the target. Parametrize the segment at constant speed and call this scalar projection \(v(t)\). For any \(\varepsilon>0\), the continuous function \(v(t)-(L+\varepsilon)\|y-x\|t\) cannot have a maximum greater than its value at zero. Such a maximum would occur at some \(t_*>0\); the local bound comparing \(t_*\) to a slightly smaller parameter makes the value at \(t_*\) strictly smaller than there, a contradiction. Thus \(v(1)-v(0)\leq(L+\varepsilon)\|y-x\|\). Let \(\varepsilon\) decrease to zero and choose the unit vector in the direction of \(h(y)-h(x)\), unless that difference is zero. This gives the claimed norm bound. ∎

**Lemma J.4 — A normal graph with its orientation.** Let \(F\) be a smooth compact manifold. On \(F\times\overline B_{2r}\) let \(e(x,z)\) be continuous, satisfy \(\|e\|<r/4\), and have Lipschitz constant \(\theta<1/2\) in its \(z\)-coordinate, uniformly in \(x\). Set \(G(x,z)=z+e(x,z)\). For every \(y\in B_r\), its inverse image is the graph of a unique continuous function \(\zeta_y:F\to B_{2r}\), hence is homeomorphic to \(F\). In an oriented fibre-first product, the induced fibre orientation is that of \(F\).

**Proof.** For each fixed \(x,y\), the map \(z\mapsto y-e(x,z)\) preserves the closed ball of radius \(2r\), since its norm is less than \(5r/4\), and is a contraction of ratio \(\theta\). Its iterates converge by the geometric-series estimate in the local-inverse proof, giving a unique solution \(\zeta(x,y)\). Continuity in \(x,y\) follows directly from
\[
(1-\theta)\|\zeta(x,y)-\zeta(x',y')\|
\leq\|y-y'\|+
\|e(x,\zeta(x',y'))-e(x',\zeta(x',y'))\|.
\tag{J.7}
\]
The second term tends to zero by uniform continuity on the compact product. The projection of this graph to \(F\) and its displayed continuous inverse are homeomorphisms.

For the orientation use the same construction with \(e\) replaced by \(se\), \(0\leq s\leq1\). The maps
\[
(x,z)\longmapsto(x,z+se(x,z))
\tag{J.8}
\]
are local homeomorphisms on the open product \(F\times B_{2r}\): near any interior point, solve the second coordinate in a small closed ball wholly inside the domain about its existing solution; the uniform contraction and continuity in \(x\) give a continuous inverse and an open image there. They are one-to-one on each full fibre because
\(\|G_s(x,z)-G_s(x,z')\|\geq(1-s\theta)\|z-z'\|\).
Each map is continuous and injective on the compact closed product, so its inverse on its image is continuous: images of closed subsets are compact and hence closed in the Hausdorff target. Thus these maps form a continuous family of embeddings of the closed product, starting at its identity; their restrictions to its interior are local homeomorphisms, and their inverse graphs vary continuously with \(s\).

Such a family preserves the ambient local orientation. To check this with local homology, take a small closed oriented coordinate ball about one point. Its image boundary misses the image centre. For nearby parameters these compact boundary images still miss that centre, transported continuously, and the maps of the corresponding punctured pairs are homotopic. Their local degrees are equal. The sign is therefore locally constant in \(s\), hence constantly \(+1\) from \(s=0\). In the product identification (J.8), target coordinates are still the last coordinates. Removing their positive local generator leaves precisely the positive \(F\)-generator. This proves the fibre-first orientation assertion, also when the graph is only a topological manifold. ∎

### J.4. A PL approximation that preserves the fibre signature

**Theorem J.5 — Comparing one smooth map.** Let \(t:K\to M^n\) be a finite smooth-compatible triangulation, with \(M\) closed oriented, and let \(f:M\to S^k\) be smooth, \(k\geq1\). There is a PL map \(g:K\to Q\), homotopic to \(s^{-1}ft\), such that its generic oriented fibres have the signature of a smooth regular fibre of \(f\), when \(n-k\) is divisible by four.

**Proof: local interpolation.** Choose a regular value \(y_0\) in the image under \(s\) of a facet interior. This is possible because both the regular-value set and the union of those interiors are dense open subsets. Fix positive affine coordinates \(\kappa\) on that facet with \(\kappa(s^{-1}(y_0))=0\); only these local coordinates are translated, while the global simplex stays centred as in LemmaJ.1. Choose the coordinate ball \(B_{3r}\) with closure inside the facet interior and consisting of regular values for \(q=\kappa s^{-1}f\). Shrink \(r\), if necessary, to obtain the product \(\Psi:F\times B_{3r}\to f^{-1}(s\kappa^{-1}B_{3r})\) from LemmaI.2, with \(q\Psi(x,z)=z\). In the rest of this proof, a target ball in \(Q\) means its image under \(\kappa^{-1}\); expressions such as \(sB_{3r}\) use this convention.

Let \(h=s^{-1}ft:K\to Q\). On the face-compatible subdivisions of LemmaJ.2, define \(H_N:K\to\mathbb R^{k+1}\) by taking the actual values \(h(v)\) at every vertex and interpolating affinely. Uniform continuity makes the positive bound \(\eta_N=1/N+\sup\|H_N-h\|\) tend to zero. Apply the annular retraction of LemmaJ.1 to obtain a PL map \(g_N\) homotopic to \(h\), converging to it uniformly by (J.5). No affine interpolation across different sphere facets was declared to take values in the sphere; the annular retraction is the step that ensures this globally.

For large \(N\), every closed source simplex of \(K_N\) meeting \(t^{-1}f^{-1}(s\overline B_{2r})\) is mapped by \(h\) entirely into the facet interior over \(B_{3r}\). This follows from compactness and uniform continuity, since the smaller closed target ball has positive distance from the complement of the larger open ball. Their union, with all faces, is a subcomplex \(A_N\), and the smaller inverse image lies in its relative interior in \(K\): all closed simplices incident to each of its points meet that inverse image and are included. On each simplex of \(A_N\), interpolation of the vertex images remains in the one convex target facet. Hence \(H_N\) takes values in \(Q\) there and the retraction fixes it exactly. Thus \(g_N=H_N\) on \(A_N\).

**Proof: uniform normal control.** The coordinate map \(h\) is smooth on the closed portions of each original simplex over a slightly larger compact target ball inside the facet. Its derivatives there have a common modulus of continuity. LemmaJ.2 therefore gives uniform first-derivative convergence of \(H_N\) to \(h\) on the small source simplices meeting this region. One can apply its edge estimate locally: every such small simplex is entirely in this coordinate region, and the finitely many original smooth extensions give common bounds and moduli on a compact neighbourhood of the smaller region.

In full-dimensional original simplices, the derivative of \(t\) is invertible as a map to a manifold chart, including along closed faces. Its inverse norms are bounded on these finitely many compact sets. Local inverse extensions of each such piece transfer the preceding derivative errors to the smooth \(M\)-coordinates, with one common multiplicative bound. Compose with the fixed product diffeomorphism \(\Psi\); its derivatives in the ball directions are bounded on \(F\times\overline B_{2r}\). Consequently the continuous error
\[
e_N(x,z)=\kappa\!\left(g_N\bigl(t^{-1}\Psi(x,z)\bigr)\right)-z
\tag{J.9}
\]
has, on each closed smooth piece, extensions with ball-direction derivative norm tending uniformly to zero. Here we use affine coordinates on the fixed facet, and their centre is zero. The finitely many pieces come from the small simplices of \(K_N\); at their boundaries the extensions need not have identical derivatives, but their values agree. Choose \(N\) so large that their derivative norms on sufficiently small extension neighbourhoods are all less than \(1/3\). LemmaJ.3 applied on each straight ball-coordinate segment then gives a common Lipschitz constant \(\theta\leq1/3\), for each fixed \(x\). Uniform convergence also gives \(\sup\|e_N\|<r/4\). The finite-piece lemma, rather than an assertion of global smoothness of \(g_Nt^{-1}\), supplies this crucial bound.

**Proof: the complete fibre.** Uniform convergence further ensures that every inverse image under \(g_Nt^{-1}\) of a point in \(B_r\) lies in \(f^{-1}(sB_{2r})\). To see this, the two disjoint compact subsets \(s\overline B_r\) and \(S^k-sB_{2r}\) have positive distance; compose the uniform convergence with the uniformly continuous \(s\). Taking the resulting error smaller than that distance rules out any other inverse-image points.

LemmaJ.4 now identifies the whole inverse image over every point of \(B_r\) with a graph over \(F\), preserving orientation. If \(F\) is empty, first choose the ball to miss \(f(M)\); uniform convergence makes the corresponding \(g_N\)-fibres empty too, so the same conclusion holds. Make \(g_N\) simplicial using LemmaE.1 and choose a generic target point in \(B_r\) outside the finitely many lower-dimensional target faces. Such a point exists because their finite union has empty interior. Its fibre is the finite rational homology manifold of SectionA and is also homeomorphic, with its induced orientation, to the smooth \(F\). Its rational middle cup form and hence its signature coincide with those of \(F\). SectionF proves that the generic signature has this same value at every generic target point. The map \(g=g_N\) has the required homotopy and signature. ∎

### J.5. The classes in every degree

**Theorem J.6 — Conditional smooth comparison.** For every finite smooth-compatible triangulation \(t:K\to M^n\) of a smooth closed oriented manifold,
\[
\ell_i(K)=t^*L_i(TM),\qquad
\mathcal P_i(K)=t^*p_i(TM)_{\mathbb Q}
\quad(i\geq0).
\tag{J.10}
\]
Here \(\mathcal P_i\) is the recursive rational Pontryagin recovery of CorollaryG.4. The equality gives the same class on \(M\) for every such given triangulation. It does not assert existence of those triangulations or an integral extension of the Pontryagin classes.

**Proof: the strict range.** First suppose \(4i<(n-1)/2\), with \(k=n-4i\geq2\). For every smooth \(f:M\to S^k\), TheoremJ.5, the defining property of \(\ell_i\), and TheoremI.3 give
\[
\left\langle \ell_i(K)\smile t^*f^*u,[K]\right\rangle
=\sigma(F_y)
=\left\langle t^*L_i(TM)\smile t^*f^*u,[K]\right\rangle.
\tag{J.11}
\]
Orient \(K\) by \(t\), so its fundamental class maps to \([M]\); the chosen positive \(s\) identifies the sphere generators in this formula.

These pulled-back classes span all \(H^k(K;\mathbb Q)\). By TheoremC.3, that cohomology is spanned by the pullbacks of a sphere generator under continuous maps \(K\to S^k\). Compose such a map with \(t^{-1}\) to get a continuous map on \(M\). Every continuous map from compact smooth \(M\) to the unit sphere is homotopic to a smooth one: choose a finite open cover on which its oscillation is less than \(\varepsilon<1/2\), a smooth partition of unity \(\theta_j\) subordinate to it, and sample values \(v_j\) from its members. The smooth vector map \(v=\sum_j\theta_jv_j\) is within \(\varepsilon\) of the original unit vector at each point. It is never zero, and \(v/\|v\|\) is smooth. Normalizing the straight homotopy between the original vector and \(v\) gives the desired homotopy, since each vector stays within \(\varepsilon\) of the original unit vector. The smooth subordinate partition construction was proved in Vector bundles, Section5, in the smooth-metric argument following the tangent/normal splitting. Thus the smooth maps used in (J.11) suffice. Rational perfect duality in SectionD makes equality of all these pairings imply \(\ell_i(K)=t^*L_i(TM)\) in the strict range.

**Proof: stabilization.** For an arbitrary positive \(i\), choose \(m>4i\) and \(n+m>8i+1\). There is a smooth-compatible product triangulation of \(M\times S^m\) from the given \(t\) and the explicit radial sphere triangulation (J.1). Indeed triangulate every convex product cell \(\sigma\times\tau\) by its face-chain coning, making the same choices on shared faces as in LemmaA.3. Each resulting simplex is affine in a product of original simplex affine hulls. The smooth extensions of \(t\) and \(s\) have injective product derivative; its restriction to every such simplex is injective. Thus the product homeomorphism is smooth and full rank on every closed simplex, exactly the asserted compatibility. No general existence theorem is used for this particular product.

The strict-range result on that product yields
\[
\ell_i(K\times Q_m)=(t\times s_m)^*L_i\bigl(T(M\times S^m)\bigr).
\tag{J.12}
\]
The sphere's tangent bundle plus its outward normal line is the trivial \((m+1)\)-plane bundle, by the map sending tangent and normal vectors to their sum in \(\mathbb R^{m+1}\). Hence its rational Pontryagin and L-classes in positive degrees vanish. The product tangent splitting and rational multiplicativity give \(L_i(T(M\times S^m))=\operatorname{pr}_M^*L_i(TM)\). The proved stabilization in TheoremG.3 gives \(\ell_i(K\times Q_m)=\operatorname{pr}_K^*\ell_i(K)\). Restrict (J.12) to a sphere-point slice to obtain the first equality of (J.10). For \(i=0\) both classes are the unit; degrees above \(n\) vanish on both sides.

Finally the positive all-degree coefficients in LemmaB.1 give a unique recursive solution of \(\ell_i=L_i(\mathcal P_1,\ldots,\mathcal P_i)\). The actual smooth rational Pontryagin classes satisfy these same equations by the first equality. Induction therefore gives the second equality in (J.10). Transporting by either of two given triangulations identifies their combinatorial classes on \(M\) with these same smooth classes, proving the stated independence. Every conclusion has exactly the given-triangulation hypothesis. ∎

**Corollary J.7 — Descent for an unoriented smooth manifold.** Let \(t:K\to M\) be a given finite smooth-compatible triangulation of a smooth closed manifold, with no orientation assumed. The rational combinatorial classes descend uniquely from its orientation cover and satisfy (J.10). They are natural under PL homeomorphisms of these triangulated manifolds.

**Proof.** In dimension zero the conclusion is the unit in degree zero and vanishing in positive degrees, so assume positive dimension. In smooth charts the two orientation choices are exchanged precisely when the determinant of a chart transition is negative. These locally constant signs give a two-sheeted orientation cover \(\widetilde M\to M\), whose total space is canonically oriented. Equivalently its sheets are the two generators of the integer point-local top homology; the equality with the determinant convention was proved in manifold Section3. This description makes the cover natural under every homeomorphism, not only a smooth one: transport a relative fundamental class on a small coordinate ball, and its coherent local restrictions give the transported generator throughout that neighbourhood. Thus the induced action on its two locally constant sheets is continuous. If a component is already oriented, its cover is the disjoint union of its two orientation choices.

Pull this cover back along \(t\). Each closed simplex lifts once for each selected vertex lift, by the full contractible-disk lifting proof; the lifts agree on a face when their chosen sheets agree. They form a finite covering complex \(\widetilde K\to K\), with two affine copies of every simplex. The lifted \(\widetilde t:\widetilde K\to\widetilde M\) is a smooth-compatible triangulation, since the covering charts on \(\widetilde M\) are local diffeomorphisms. It inherits the canonical orientation.

The deck transformation reverses that orientation. SectionF proves that reversing orientation does not change the class \(\ell_i\): it changes both the fibre signature and the fundamental-class evaluation sign, so the uniquely defined class stays fixed, and the same holds after stabilization. Its PL naturality therefore makes \(\ell_i(\widetilde K)\) deck invariant. The transfer identities (K.2), or the complete double-cover proof in Pontryagin Exercise6.5, identify the image of
\[
q^*:H^*(K;\mathbb Q)\longrightarrow H^*(\widetilde K;\mathbb Q)
\]
with the deck invariants and make this map injective. Define \(\ell_i(K)\) as the unique class whose pullback is \(\ell_i(\widetilde K)\). This agrees with the oriented definition when an orientation was already available, because the two cover components have the same orientation-independent class.

The oriented comparison gives
\(\ell_i(\widetilde K)=\widetilde t^*L_i(T\widetilde M)=q^*t^*L_i(TM)\), since a local diffeomorphism identifies the lifted tangent bundle with the pulled-back one. Injectivity of \(q^*\) proves the first equality of (J.10), and recursive recovery proves the Pontryagin equality. A PL homeomorphism lifts to the orientation covers by its action on the local generators. The lift is PL: refine the base map to affine simplex pieces and lift each such piece into an affine covering simplex; uniqueness makes the face restrictions agree. Naturality of the oriented classes upstairs and injectivity downstairs prove the assertion. The argument concerns characteristic classes; it asserts no unoriented bordism-detection theorem. ∎

The comparison above proves an equality for each given triangulation. [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md) independently constructs such triangulations and proves the needed relative boundary extension.


## K. Lens spaces and the rational/integral distinction

We derive these examples from the full [covering](grassmannians-and-classifying-maps.md), [Chern](chern-classes-and-the-integral-universal-ring.md), [Pontryagin](pontryagin-classes-and-oriented-universal-cohomology.md) and [Gysin](gysin-sequence-and-projective-splitting.md) proofs already in the course. They illustrate what rational invariance retains and what rational coefficient change discards. The torsion calculation is not, by itself, a counterexample to an integral PL-invariance theorem.

### K.1. The finite quotient and its tangent bundle

Let \(r\geq2\), let \(d\geq1\), and choose integers \(q_1,\ldots,q_d\) each relatively prime to \(r\). With \(\zeta=\exp(2\pi i/r)\), let its cyclic group act on the unit sphere in \(\mathbb C^d\) by
\[
(z_1,\ldots,z_d)\longmapsto
(\zeta^{q_1}z_1,\ldots,\zeta^{q_d}z_d).
\tag{K.1}
\]
Write \(L=L^{2d-1}(r;q_1,\ldots,q_d)\) for the quotient.

**Proposition K.1 — Lens-space quotient and rational cohomology.** The quotient is a smooth closed oriented manifold, and its covering sphere has \(r\) sheets. Its rational cohomology is \(\mathbb Q\) in degrees zero and \(2d-1\), and zero in all other degrees.

**Proof.** If a group element fixes a sphere point, at least one coordinate is nonzero. On that coordinate \(\zeta^{a q_j}=1\); relative primeness forces \(r\mid a\). Thus the action is free. Around any point choose a sufficiently small sphere coordinate neighbourhood whose finitely many translates are disjoint: the point and its distinct translates have positive pairwise distances, and shrinking its neighbourhood preserves that separation. Projection maps each such neighbourhood diffeomorphically onto its quotient image. These charts give the smooth manifold structure and the \(r\)-sheeted covering. A finite group quotient of a compact Hausdorff space is compact Hausdorff: distinct finite orbits have disjoint invariant neighbourhoods obtained by finite intersections and unions of separating neighbourhoods. The chart cover also gives second countability, by projecting a countable basis from the sphere. Each complex rotation preserves the real ambient orientation and the outward normal, so its restriction preserves the boundary sphere orientation; the charts therefore give a consistent quotient orientation. There is no boundary.

For completeness, define the chain transfer \(T\) on a singular simplex of \(L\) to be the sum of its \(r\) lifts to the sphere. A simplex has one unique lift for each selected vertex lift: the complete covering homotopy proof in the classifying-maps chapter applies to its contractible parameter simplex. Restricting all these lifts to any face enumerates exactly the lifts of that face, so \(T\partial=\partial T\). Projection followed after transfer is \(r\) times the identity on chains, and transfer after projection is the sum of the \(r\) deck maps. Dualizing gives a cohomology transfer \(\tau\) with
\[
\tau p^*=r\,1,\qquad
p^*\tau=\sum_{a=0}^{r-1}(\zeta^a)^*.
\tag{K.2}
\]
These are the same proved lift-and-face identities as the double-cover calculation in Pontryagin Exercise6.5, now with all \(r\) sheets. Over \(\mathbb Q\), the first identity makes \(p^*\) injective, and the second identifies its image with the deck invariants: an invariant class \(b\) equals \(p^*(\tau b/r)\). The sphere has cohomology only in degree zero and its top degree. Every deck map acts as the identity there, since it is positive. This proves the assertion, including \(d=1\), where the sphere and quotient are circles. ∎

Define the complex line
\[
\eta=(S^{2d-1}\times\mathbb C)/
\bigl((z,w)\sim(\zeta\cdot z,\zeta w)\bigr),
\qquad t=c_1(\eta)\in H^2(L;\mathbb Z).
\tag{K.3}
\]
Its local bundle charts are obtained by choosing one covering sheet over each quotient chart. Tensor powers have the corresponding power character, and \(\eta^{\otimes r}\) is canonically trivial. First-Chern tensor additivity, proved in the Chern chapter from the full line-bundle normalization, gives \(rt=0\).

**Proposition K.2 — Integral tangent Pontryagin formula.** The stable tangent bundle satisfies
\[
TL\oplus\varepsilon^1_{\mathbb R}
\cong\left(\bigoplus_{j=1}^d\eta^{\otimes q_j}\right)_{\mathbb R},
\qquad
p(TL)=\prod_{j=1}^d(1+q_j^2t^2).
\tag{K.4}
\]
The formula is integral, with terms above the manifold dimension omitted. In particular every positive-degree rational Pontryagin class is zero.

**Proof.** On the sphere the tangent bundle plus its radial line is the trivial real ambient bundle \(S^{2d-1}\times\mathbb C^d\), by the map \((v,a)\mapsto v+az\). This map is equivariant for (K.1), acting on the ambient fibre by its same complex rotations. The radial section \(z\) is also equivariant, and gives a nowhere-zero section of the quotient radial line, so that line is trivial. Dividing the ambient bundle by the group identifies its \(j\)-th complex coordinate with the line of character \(\zeta^{q_j}\), namely \(\eta^{\otimes q_j}\), also for negative \(q_j\) by dual tensor powers. This proves the stable splitting.

Its complex summands have first classes \(q_jt\), by tensor additivity and the dual rule. The exact underlying-complex formula in Pontryagin Section2, (2.3), gives the product in (K.4). There is no two-torsion qualification here: it is the complex-bundle identity obtained by complexifying to \(V\oplus\overline V\), applying the integral Chern Whitney formula, and pairing the roots \(q_jt,-q_jt\). Adding a trivial real line does not change Pontryagin classes by their definition and stability. Since \(rt=0\), its image in rational cohomology is zero, proving the final assertion. This also agrees with PropositionK.1: no positive degree divisible by four is the odd top degree. ∎

For a given smooth-compatible triangulation of \(L\), TheoremJ.6 therefore gives \(\mathcal P_i=0\) for every \(i>0\). Any PL homeomorphism between such triangulated lens spaces preserves these zero rational classes by SectionG. They supply no distinction between their PL types. In dimension three \(p_1\) is already zero integrally by dimension; even integral Pontryagin classes cannot distinguish three-dimensional lens spaces. No classification of lens spaces is asserted here.


### K.1a. An explicit compatible triangulation of every weighted lens space

The lens spaces in PropositionK.1 possess a finite smooth-compatible triangulation. Here is a construction that also handles \(r=2\), without invoking general smooth triangulation.

In each coordinate complex plane choose the regular \(2r\)-gon \(P_j\) with vertices \(\exp(\pi i b/r)e_j\), \(0\leq b<2r\), and let \(P\) be the convex hull of all these vertices in \(\mathbb R^{2d}\). If \(\mu_j\) is the positive homogeneous gauge of \(P_j\), then
\[
P=\{(v_1,\ldots,v_d):\ \sum_j\mu_j(v_j)\leq1\}.
\tag{K.10}
\]
Indeed a convex combination of points from the coordinate polygons satisfies this inequality by convexity. Conversely, take the weights \(\mu_j(v_j)\), write each nonzero coordinate as that weight times a boundary point of its polygon, and put the remaining weight at the origin, which belongs to every polygon. This proves equality. The origin is interior, since the polygons contain disks of positive radius in every coordinate plane.

Choose one edge of each polygon. Their join is a facet of \(P\): add their positive supporting linear functionals, each normalized to equal one on its chosen edge. Equality in the resulting support inequality holds precisely on that join. Every facet arises this way, as can also be seen by writing each gauge as the maximum of its finitely many edge functionals in (K.10). Its \(2d\) vertices are affinely independent. In each coordinate plane the two edge endpoints are linearly independent, because an edge of a regular \(2r\)-gon does not lie on a line through the origin. A linear relation among the vertices therefore vanishes separately in each coordinate plane. Thus \(\partial P\) is a finite simplicial sphere. The rotations (K.1) act simplicially, sending a vertex index \(b\) to \(b+2q_j\) in its coordinate plane.

Radial projection \(\rho:\partial P\to S^{2d-1}\) is an equivariant homeomorphism. Each ray meets the boundary once by (K.10), which also gives a continuous radial inverse. On a facet in a support hyperplane \(\ell(v)=1\), the radial derivative has kernel \(\mathbb Rv\); that line meets the tangent hyperplane \(\ell(w)=0\) only at zero. Hence \(\rho\) is smooth and full rank on each closed facet and all its faces, with a smooth extension to a neighbourhood in its affine hull. The action on \(\partial P\) is free, because its equivariant radial image is the free sphere action.

We verify that a finite invariant subdivision has a genuine simplicial quotient. In the Euclidean metric let
\[
\delta=\min_{\substack{v\in\partial P\\1\leq a<r}}
 \|v-\zeta^a v\|>0.
\tag{K.11}
\]
Positivity follows from freeness and compactness; the action is by isometries. Barycentric subdivision is equivariant. Its simplex mesh tends to zero: the diameter of each barycentric simplex in a simplex of dimension \(b\leq2d-1\) is at most \(b/(b+1)\) times the original diameter, by comparing the barycentres of nested faces; iteration gives a uniform geometric bound. Choose a finite iterate with mesh less than \(\delta/3\). Every closed vertex star then has diameter less than \(2\delta/3\).

No closed vertex star meets a nonidentity translate of itself. Otherwise \(v\) and \(\zeta^a v\) would both lie in that star, contradicting (K.11). In particular the vertices of a simplex have distinct group orbits. Make the quotient complex's vertices those orbits and its simplices the orbit sets of simplex vertices. Suppose two simplices have the same orbit set, or compare their vertices belonging to common quotient faces. Align one common vertex by a group element. The aligned simplices both lie in its closed star; two vertices there in the same orbit must be identical, again by (K.11). Thus all shared quotient vertices align simultaneously, and simplices with identical orbit sets are translates. Barycentric coordinates consequently give a continuous bijection from the finite orbit realization onto the quotient polyhedron, with inverse on each quotient simplex. It is a homeomorphism by compactness and the Hausdorff quotient property proved in PropositionK.1.

Finally the descended map \(\rho\) gives a homeomorphism from this quotient complex to \(L\). On a closed quotient simplex choose its lifted simplex. The radial extension on that simplex's affine hull, followed by the smooth covering projection \(S^{2d-1}\to L\), is a smooth extension of its map to \(L\). The covering projection is a local diffeomorphism, so this extension has the full rank just checked. The disjoint-star property ensures that these lifted simplex maps give exactly the quotient realization. This is a finite smooth-compatible triangulation of \(L\). Therefore the rational combinatorial Pontryagin classes of these explicit triangulations are zero by TheoremJ.6 and (K.4). The construction proves existence for these examples, while TheoremJ.6 keeps its precise given-triangulation scope for a general smooth manifold. ∎

### K.2. A nonzero torsion class that rationalization loses

For equal weights write \(L_r^{2d-1}=L^{2d-1}(r;1,\ldots,1)\). The map
\[
\pi:L_r^{2d-1}\longrightarrow\mathbb {CP}^{d-1},
\qquad [z]\longmapsto\mathbb Cz
\tag{K.5}
\]
is well defined. Let \(\gamma\) be the tautological complex line and \(u=c_1(\gamma^*)\).

**Proposition K.3 — Even integral cohomology and the basic line.** For \(d\geq2\) and \(1\leq j\leq d-1\),
\[
H^{2j}(L_r^{2d-1};\mathbb Z)=
(\mathbb Z/r)\,\pi^*u^j,
\qquad
\eta\cong\pi^*\gamma^*,\quad t=\pi^*u.
\tag{K.6}
\]
In particular, on \(L_5^5\),
\[
p_1(TL_5^5)=3t^2\ne0
\quad\text{in }H^4(L_5^5;\mathbb Z)\cong\mathbb Z/5,
\qquad p_1(TL_5^5)_{\mathbb Q}=0.
\tag{K.7}
\]

**Proof.** The unit sphere bundle of \(\gamma\) is the Hopf sphere, as proved in the Gysin chapter. The map \(z\mapsto z^{\otimes r}\) in its tautological line identifies its quotient by the scalar \(r\)-th roots with the unit sphere bundle of \(\gamma^{\otimes r}\). It is bijective over every projective line: its unit circle power map is onto and has exactly those \(r\) roots in each fibre. It is a continuous bijection from a compact space to a Hausdorff bundle total space, hence a homeomorphism. Local unit frames also show it is the usual smooth circle-bundle identification. Thus (K.5) is this circle bundle, whose oriented Euler class is \(c_1(\gamma^{\otimes r})=-ru\), using the complex orientation. Its sign will not affect the quotient group.

The projective-space theorem gives \(H^*(\mathbb {CP}^{d-1};\mathbb Z)=\mathbb Z[u]/(u^d)\). In the integral rank-two Gysin sequence, the segment ending in an even degree is
\[
\mathbb Z u^{j-1}\xrightarrow{\,-ru\,}
\mathbb Z u^j\xrightarrow{\pi^*}
H^{2j}(L_r^{2d-1};\mathbb Z)
\longrightarrow H^{2j-1}(\mathbb {CP}^{d-1};\mathbb Z)=0.
\tag{K.8}
\]
Exactness identifies the last nonzero group with the indicated cyclic quotient, and identifies its generator as the pullback of \(u^j\).

Identify the associated line in (K.3) with \(\pi^*\gamma^*\) as follows. To \([z,w]\) assign the linear functional on \(\mathbb Cz\) sending \(cz\) to \(cw\). Replacing \((z,w)\) by \((\zeta z,\zeta w)\) replaces \(c\) by \(c/\zeta\), and leaves its value unchanged. This is a well-defined complex-linear fibre isomorphism; local unit frames give smooth bundle charts and its inverse. Thus \(t=\pi^*u\). With \(d=3\) and \(r=5\), (K.4) gives \(p_1=3t^2\). Formula (K.6) makes \(t^2\) a generator of \(\mathbb Z/5\), so its multiple by three is nonzero. Rational coefficient change kills it. ∎

### K.3. Four further graded exercises

**Exercise K.4 — Easy: the three-dimensional example.** Explain why rational \(p_1\) is combinatorially invariant for a smooth-compatible triangulation of a three-dimensional lens space, and why that example cannot detect a difference of PL types.

**Solution.** There is no cohomology in degree four on a closed three-manifold, by the proved manifold dimension bound. Therefore both integral \(p_1\) and its rational image are zero. The conditional comparison identifies the combinatorial rational class with that zero class; PL naturality preserves it. Since the invariant has the same value for all these lens spaces, it cannot distinguish any pair of their PL types. This is a statement about the information in this invariant, not a classification result. ∎

**Exercise K.5 — Medium: weighted tangent classes.** Compute \(p_1,p_2\) for \(L^{2d-1}(r;q_1,\ldots,q_d)\) in terms of the class \(t\) of (K.3), retaining the dimension restrictions.

**Solution.** Expand (K.4):
\[
p_1=\left(\sum_jq_j^2\right)t^2,
\qquad
p_2=\left(\sum_{a<b}q_a^2q_b^2\right)t^4.
\tag{K.9}
\]
The first class vanishes by dimension if \(2d-1<4\), and the second if \(2d-1<8\). Each expression is \(r\)-torsion because \(rt=0\), and each becomes zero over \(\mathbb Q\). There is no assertion that \(t\) is a generator for arbitrary weights; only the equal-weight case was proved to have that description in PropositionK.3. ∎

**Exercise K.6 — Medium: what a rational theorem cannot decide.** For a finite CW complex, describe the information lost by passing from integral degree-four cohomology to rational cohomology. Use \(L_5^5\) to show that rational vanishing does not imply integral vanishing. Does this example prove that integral \(p_1\) fails to be a PL invariant?

**Solution.** The finite free cellular cochain complex and flatness of \(\mathbb Q\) give \(H^4(X;\mathbb Z)\otimes\mathbb Q\cong H^4(X;\mathbb Q)\), by the full comparison in SectionC. The kernel of coefficient change is precisely the torsion subgroup: an element is zero in the localization exactly when a nonzero integer kills it. Equation (K.7) is a nonzero integral torsion Pontryagin class with zero rational image. It disproves the implication from rational vanishing to integral vanishing. It does not compare two PL-equivalent smooth manifolds with unequal integral classes, and so supplies no counterexample to integral PL invariance. Such a stronger claim requires its own theorem or counterexample, with its precise scope. ∎

**Exercise K.7 — Hard: audit the conditional smooth comparison.** Explain why the proof of TheoremJ.6 does not require a PL equivalence between two smooth-compatible triangulations. Identify the prerequisite it still does not prove.

**Solution.** For each given triangulation separately, controlled interpolation near a regular fibre and a PL annular retraction produce a homotopic PL sphere map with the same oriented fibre signature. Rational cohomotopy spanning and perfect duality then give \(\ell_i(K)=t^*L_i(TM)\) in the strict range. A product with an explicitly triangulated sphere and the proved stabilization give the equality in every degree. Recursive inversion gives rational Pontryagin equality. Transporting either triangulation's classes to \(M\) therefore gives the same smooth class, without constructing a PL homeomorphism between their complexes. The argument begins with a given smooth-compatible triangulation. It still does not prove that every smooth manifold possesses one. That separate original15 prerequisite is proved in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md). ∎

The separate eight-dimensional obstruction to integral refinement of the canonical rational PL classes is proved in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md). The torsion calculation above is not used to replace that obligation. Nor do denominators in rational L-polynomials alone prove that no integral extension exists.


## Sources and proved scope

The freely readable classical source is John Milnor, with notes by James Stasheff, [*Lectures on Characteristic Classes* (1957)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf), ChapterXVI, Sections1–3. Its differentiable-fibre construction, combinatorial construction and smooth comparison provide the historical mathematical treatment; the cited triangulation theorem is proved in the course's triangulation companion. The normal-graph and controlled interpolation details above are independent complete reconstructions. The degree-eight projective divisibility calculation expands that source's Corollary2 using the Hirzebruch signature polynomial already proved in the course.

Bernard Morin’s [*Un contre-exemple de Milnor à la Hauptvermutung* (1962)](https://www.numdam.org/item/SB_1961-1962__7__41_0.pdf), §5, pp.53–55, presents weighted cyclic sphere quotients, their cell decomposition, integral cohomology groups and an invariant triangulation. The explicit construction above instead uses \(2r\)-gons in every coordinate plane, including the order-two case, and proves the subdivision and smooth quotient details. The stable tangent splitting, Pontryagin product, canonical cohomology generators and associated-line identification are proved here from the earlier covering, Chern, Pontryagin and Gysin results; these refinements are not attributed to Morin’s §5. Milnor’s counterexample involving \(L(7,1)\) and \(L(7,2)\) requires additional homotopy, torsion and embedding premises and is not asserted as a consequence of the tangent-class calculation.

The tangent and torsion calculations use the complete covering, Chern, Pontryagin and Gysin proofs identified above. General smooth triangulation and the integral-refinement obstruction are supplied in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md). The [curvature chapter](connections-curvature-and-characteristic-forms.md) and exotic-sphere chapter continue the course.
