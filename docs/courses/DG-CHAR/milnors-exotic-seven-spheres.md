# Milnor's exotic seven-spheres

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0. No independent AI review is recorded.*

We construct smooth oriented four-plane bundles over \(S^4\), compute their integral Euler and Pontryagin classes, and prove that Euler number \(\pm1\) makes their sphere total spaces homeomorphic to \(S^7\). The homeomorphism comes from a checked smooth function with two nondegenerate critical points. A filling-independent invariant modulo seven then distinguishes one of these smooth manifolds from the standard sphere. Every sign is fixed by a single quaternionic-line normalization, and six graded exercises have complete solutions.

These proofs cover assigned lesson16. They use the full [bundle](vector-bundles-and-their-constructions.md), [classification and covering](grassmannians-and-classifying-maps.md), [Thom/Euler](thom-classes-and-euler-classes.md), [Gysin](gysin-sequence-and-projective-splitting.md), [sphere-degree](frame-fields-and-primary-obstructions.md), [Chern](chern-classes-and-the-integral-universal-ring.md), [Pontryagin](pontryagin-classes-and-oriented-universal-cohomology.md), [manifold](manifold-duality-the-diagonal-and-wu-classes.md), [collar/gluing](the-oriented-cobordism-ring.md), and [signature](multiplicative-sequences-and-the-signature-theorem.md) proofs already supplied in this course. The compact-band flow argument is also given in [smooth fibres](smooth-fibres-triangulation-comparison-and-lens-spaces.md), SectionI.1. The exact uses are identified below. No general smooth-triangulation existence theorem or general theorem that all seven-manifolds bound is assumed: the examples have their explicit disk-bundle fillings.

The distinction matters. The smooth total space is a sphere topologically, while its smooth structure is detected by a characteristic-number calculation on an eight-dimensional filling. The separate integral PL-refinement obstruction and its compatible relative triangulation prerequisites are proved in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md).

## A. Four-plane bundles with prescribed Euler and Pontryagin classes

We use the bundle \(\xi_{h,j}\) with transition (C.6). The base and fibre orientations must be fixed before an Euler number is assigned. Give \(\mathbb H\) the complex structure \(v\mapsto vi\), and give its underlying real four-space the resulting complex orientation. Left multiplication by a quaternion commutes with this complex structure. This fixes the fibre orientation for every \(\xi_{h,j}\).

### A.1. The quaternionic line and its integral normalization

**Lemma A.1 — The basic bundle.** The bundle \(\xi_{1,0}\) is the underlying real bundle of a complex two-plane bundle \(V\), and its unit sphere bundle is diffeomorphic to \(S^7\). Orient the base \(S^4\) so that \(u=e(\xi_{1,0})\) evaluates to one. Then
\[
 e(\xi_{1,0})=u,\qquad p_1(\xi_{1,0})=-2u.
\tag{A.1}
\]

**Proof.** The transition is left multiplication by \(q\), which is complex linear for right multiplication by \(i\). Thus it defines \(V\), with the stated real complex orientation. There is an explicit identification of its sphere total space with the unit sphere in \(\mathbb H^2\). In the first and second charts it is respectively
\[
 (u,v)\longmapsto\frac{(v,uv)}{\sqrt{1+|u|^2}},
 \qquad
 (u',v')\longmapsto\frac{(\bar u'v',v')}{\sqrt{1+|u'|^2}}.
\tag{A.2}
\]
On the overlap \(u'=q/|u|\), \(v'=qv\); substitution shows the expressions agree. Both are smooth. For a sphere point \((a,b)\), when \(a\ne0\) their inverse is
\(v=a/|a|\), \(u=ba^{-1}\). When \(b\ne0\) it is
\(v'=b/|b|\), \(u'=\overline{ab^{-1}}\). These inverses are smooth and agree on the overlap. Since at least one of \(a,b\) is nonzero, they prove the diffeomorphism. The quaternionic line itself is the right line through \((a,b)\); the two displayed coordinate frames are \((1,u)\) and \((\bar u',1)\), normalized to unit length. Thus this is also the usual tautological quaternionic line over its projective line, with the second base chart conjugated to give (C.5).

The integral rank-four Gysin sequence has the segment
\[
 H^3(S^7;\mathbb Z)=0\longrightarrow H^0(S^4;\mathbb Z)
 \xrightarrow{\smile e(\xi_{1,0})}H^4(S^4;\mathbb Z)
 \longrightarrow H^4(S^7;\mathbb Z)=0.
\tag{A.3}
\]
Both middle groups are \(\mathbb Z\), so exactness makes the Euler class a primitive generator. There is therefore a unique base orientation for which it evaluates to one; call this generator \(u\). This specifies the sign rather than assuming it from a clutching convention.

The Chern chapter defines the top class of a complex bundle as the Euler class of its real complex orientation. Hence \(c_2(V)=u\). Also \(c_1(V)=0\) because \(H^2(S^4;\mathbb Z)=0\). The integral underlying-complex formula from Pontryagin Section 2 gives
\(p_1(V_{\mathbb R})=c_1(V)^2-2c_2(V)=-2u\). This proves (A.1) and the assigned quaternionic-line example without invoking a quaternionic projective-space characteristic-class formula. ∎

### A.2. Additivity for clutching, with an explicit classifying map

**Lemma A.2 — Characteristic numbers of a clutching map.** Let \(g:S^3\to SO(4)\) be based at the identity. For every \(c\in H^4(BSO(4);\mathbb Z)\), the number
\(\langle c(\xi_g),[S^4]\rangle\) is additive under pointwise multiplication of based clutching maps and changes sign under pointwise inversion. Here \(\xi_g\) is formed using the same ordered base charts as (C.5).

**Proof.** Represent \(S^4\) as the unreduced suspension of \(S^3\). If its latitude parameter is \(t\in[0,1]\), put \(\alpha=\pi t/2\). A finite-dimensional classifying map is the oriented plane
\[
 E_g(q,t)=\{(\cos\alpha\,v,\sin\alpha\,g(q)v):v\in\mathbb R^4\}
                  \subset\mathbb R^4\oplus\mathbb R^4.
\tag{A.4}
\]
The plane at either endpoint is independent of \(q\), so the map is continuous on the suspension. Projection to the first coordinate block, divided by the positive factor \(\cos\alpha\), trivializes the bundle away from the second endpoint. Projection to the second, divided by \(\sin\alpha\), trivializes it away from the first. These normalized fibre coordinates satisfy \(w=g(q)v\) on the overlap. Thus its pulled-back tautological oriented bundle is exactly \(\xi_g\); the positive normalization factors preserve its orientation.

To obtain a based cube representative, rotate the ambient coordinate blocks by
\[
 T_t(x,y)=(\cos\alpha\,x+\sin\alpha\,y,
                  -\sin\alpha\,x+\cos\alpha\,y).
\tag{A.5}
\]
This is an orthogonal bundle isomorphism carrying (A.4) to another oriented plane map \(\widehat E_g\). Both its endpoint planes are the first coordinate plane. At the basepoint \(q\), where \(g(q)=I\), that plane is also constant for every \(t\). The isomorphism transports the plane orientation, and at the second endpoint the first-block parametrization is \(g(q)v\), with positive determinant. Therefore \(\widehat E_g\) is constant, with the same oriented value, on the entire basepoint arc.

Represent \(S^3\) by \(I^3/\partial I^3\), with this arc as its basepoint times \(I\). Collapsing the arc and the two suspension tips makes the reduced suspension \(I^4/\partial I^4\). The quotient from the unreduced to the reduced suspension has degree \(+1\) with the corresponding cube orientation: at an interior point away from the arc it is an orientation-preserving identification, so the point-local fundamental-class test gives degree one. Reversing both sphere orientations, if required to match \(u\) of (A.1), keeps that assertion. Consequently \(\widehat E_g\), viewed as a map on the based four-cube, has the same characteristic number as (A.4).

First use concatenation of two based maps \(g_0,g_1\) in the first coordinate of \(I^3\). Formula (A.4), followed by (A.5), then concatenates their four-cube representatives in that same coordinate. Cutting the oriented four-cube into its two halves gives the sum of their pushed-forward fundamental classes. The shared face cancels and all remaining boundary faces map to the common basepoint. Equivalently this is the singular-chain representative for the sphere pinch map; triangulating the two halves gives the same chain identity. Evaluating \(c\) proves additivity for concatenation.

Pointwise multiplication is homotopic to that concatenation. To see it directly, write the first coordinate as \(s\). For \(0\leq r\leq1\) define
\[
 A_r(s)=\min\{s/(1-r/2),1\},\qquad
 B_r(s)=\max\{(s-r/2)/(1-r/2),0\}.
\tag{A.6}
\]
Replace the first input coordinate of \(g_0\) by \(A_r\) and of \(g_1\) by \(B_r\), and multiply their values in \(SO(4)\). Every boundary value stays the identity. At \(r=0\) this is their pointwise product. At \(r=1\), the first map is the identity on the second half and the second is the identity on the first half, so it is precisely their concatenation. This is a continuous based homotopy. The associated plane maps (A.4) give a homotopy of characteristic numbers by cohomological homotopy invariance. A pointwise map times its inverse is constant, whose positive-degree class is zero. Hence inversion changes the number's sign as well. ∎

### A.3. The right factor and all prescribed pairs

Let \(L_q(v)=qv\), \(R_q(v)=vq\), and let \(r:S^4\to S^4\) be the reflection \(u\mapsto\bar u\), \(u'\mapsto\bar u'\). It has degree \(-1\): in its first real coordinate chart conjugation has determinant \(-1\), which gives its action on the local and hence global oriented fundamental class. The fibre map \(C(v)=\bar v\) also reverses orientation. Its identity
\[
 R_q=C L_{\bar q}C
\tag{A.7}
\]
gives a fibre-orientation-reversing isomorphism
\(\xi_{0,1}\cong r^*\xi_{1,0}\). The Euler class changes sign under this isomorphism, whereas the Pontryagin class does not. Naturality and (A.1) therefore give
\[
 e(\xi_{0,1})=-r^*u=u,\qquad
 p_1(\xi_{0,1})=r^*(-2u)=2u.
\tag{A.8}
\]

Since left and right multiplication commute, the transition of \(\xi_{h,j}\) is the pointwise product \(L_q^hR_q^j\). Apply Lemma A.2 to the universal Euler and first Pontryagin classes. Cohomology in degree four is cyclic and evaluation is an isomorphism, so equality of their numbers proves equality of their classes:
\[
 e(\xi_{h,j})=(h+j)u,\qquad
 p_1(\xi_{h,j})=2(j-h)u.
\tag{A.9}
\]
All signs refer to the single normalization (A.1).

**Theorem A.3 — Prescribed four-plane classes.** Given integers \(e,k\) with \(k\equiv2e\pmod4\), there is a smooth oriented four-plane bundle on \(S^4\) with Euler class \(eu\) and first Pontryagin class \(ku\).

**Proof.** Choose
\[
 h=(2e-k)/4,\qquad j=(2e+k)/4.
\tag{A.10}
\]
These are integers: the first numerator is divisible by four by the hypothesis, and the second differs from it by \(2k\), divisible by four since \(k\) is even. They have \(h+j=e\) and \(2(j-h)=k\). Use (A.9). The bundle is smooth by its explicit transition functions. ∎

### A.4. Why this family includes every oriented four-plane bundle

**Proposition A.4 — Classification in this dimension.** Every smooth oriented four-plane bundle over the oriented \(S^4\) is smoothly isomorphic, preserving fibre orientation, to exactly one \(\xi_{h,j}\). Thus its Euler and first Pontryagin classes determine its isomorphism class, and their integer coefficients satisfy \(k\equiv2e\pmod4\).

**Proof.** A bundle on either closed hemisphere is continuously trivial by the proved homotopy-invariance theorem for bundles on a contractible compact base. Choose oriented orthonormal trivializations using its metric and Gram–Schmidt. They give an \(SO(4)\)-valued transition on the equator. Conversely such a transition glues two trivial bundles, as already used here. A homotopy of transitions gives a bundle on \(S^4\times I\); the explicit bundle homotopy-invariance proof in classification Lemma4.2 identifies its endpoint bundles.

An isomorphism between two glued bundles gives matrices on the two hemispheres with
\(g'=b_S g b_N^{-1}\) on the equator. Each \(b\) extends over its disk, so its boundary map is homotopic to a constant matrix in \(GL^+(4,\mathbb R)\). Gram–Schmidt writes a positive invertible matrix as \(QR\), with \(Q\in SO(4)\) and \(R\) upper triangular with positive diagonal. Replacing \(R\) by \((1-t)R+tI\) is a deformation retraction onto \(SO(4)\), fixed on that subgroup. Applying it to these homotopies shows that the two clutch maps are homotopic in \(SO(4)\) up to constant factors. Normalize a clutch map to be the identity at one chosen equator point by changing a hemisphere frame. Constant conjugation is homotopic to the identity conjugation along a path in the connected group \(SO(4)\). Finally an unbased homotopy between normalized maps can be based by multiplying its values on the right by the inverse of its value at the chosen point. Hence bundle classes are precisely based classes in \(\pi_3(SO(4))\).

Here is the required group computation. Define
\[
 \varphi:S^3\times S^3\longrightarrow SO(4),\qquad
 \varphi(a,b)(v)=avb^{-1}.
\tag{A.11}
\]
It is onto. For \(T\in SO(4)\), put \(w=T(1)\); the map \(L_{w^{-1}}T\) fixes \(1\) and restricts to a positive orthogonal map of the imaginary three-space. Such a map has an axis: its real eigenvalues are \(\pm1\), and odd dimension and determinant one guarantee an eigenvalue \(+1\). On the perpendicular two-plane it is a rotation of some angle \(\theta\). If \(n\) is the unit imaginary quaternion on the oriented axis, direct multiplication shows that conjugation by \(a=\cos(\theta/2)+n\sin(\theta/2)\) gives this rotation, fixing the axis. Thus \(T=L_w L_aR_{a^{-1}}=\varphi(wa,a)\). This also shows that \(SO(4)\) is connected, as it is the image of the connected \(S^3\times S^3\).

The kernel is \(\{(1,1),(-1,-1)\}\). Indeed evaluating an identity action at \(1\) gives \(a=b\), and commuting with every quaternion then makes \(a\) real, hence \(\pm1\). The map is a smooth local diffeomorphism. Both manifolds have dimension six: for \(SO(4)\), local coordinates are obtained by choosing the first unit column, then a unit column in its three-dimensional complement, then one in the remaining two-dimensional complement; the last positive column is determined. Projection and Gram–Schmidt give smooth complement frames, so this description provides actual local coordinates of dimensions three, two and one. At the identity, differentiating (A.11) gives \((A,B)\mapsto(v\mapsto Av-vB)\) for imaginary \(A,B\). Its kernel is zero by the same evaluation and commutation calculation. The inverse function theorem applies in these six-dimensional charts; translating in the two groups proves the assertion everywhere. A sufficiently small identity neighbourhood and its translate by \((-1,-1)\) are disjoint, and their common image is evenly covered, since every preimage differs by an element of the kernel. Translating proves that (A.11) is a two-sheeted covering.

The full cube and homotopy lifting proof for coverings in classification Section8b gives
\(\pi_3(SO(4))\cong\pi_3(S^3\times S^3)\): a based cube lifts from \((1,1)\), its connected boundary stays at that lift, and its based homotopies lift with the same boundary. Coordinate projections identify the latter group with \(\pi_3(S^3)\oplus\pi_3(S^3)\). The complete sphere-degree proof in frame-obstruction LemmaB.1 gives \(\pi_3(S^3)=\mathbb Z\), generated by the identity. Pointwise multiplication and concatenation agree by (A.6), now in the unit quaternion group. Therefore the two components of \(q\mapsto(q^h,q^{-j})\) have degrees \(h,-j\), and (A.11) takes them to the transition of \(\xi_{h,j}\). Every clutch class has a unique such pair. Formula (A.9) and its inverse (A.10) prove the assertions about characteristic classes.

Finally the continuous bundle isomorphisms just obtained can be made smooth. In smooth local frames for their Hom bundle, approximate each continuous matrix by a constant sampled matrix on a sufficiently small chart, and combine these smooth local sections with a finite smooth partition. Local uniform continuity and bounded frame changes on compact pieces give any prescribed uniform approximation in bundle metrics. The original isomorphism has a positive minimum singular value on the compact base. Choose the approximation error smaller than half that value; the approximating smooth bundle map and the straight path from the original are invertible in every fibre. The path retains the positive determinant sign. Thus the approximation is a smooth oriented bundle isomorphism. On unit sphere bundles its normalization \(v\mapsto Av/|Av|\) is a diffeomorphism, with inverse given by the similarly normalized inverse linear map. This completes the smooth classification, without a triangulation theorem. ∎

### A.5. Two elementary exercises with solutions

**Exercise A.5 — Easy: compute the two classes.** With the normalization (A.1), compute the Euler and first Pontryagin classes for \((h,j)=(1,0),(0,1),(-1,2)\). Construct the bundle with any allowed pair \((e,k)\).

**Solution.** Formula (A.9) gives respectively \((u,-2u)\), \((u,2u)\) and \((u,6u)\). For arbitrary \(k\equiv2e\pmod4\), the integers (A.10) give exactly \(e=h+j\) and \(k=2(j-h)\); the explicit smooth transition constructs that bundle. Conversely Proposition A.4 and (A.9) force that congruence for every oriented four-plane bundle over the chosen sphere.

**Exercise A.6 — Medium: Euler number minus one.** Explain why the unit sphere total space of every oriented four-plane bundle over \(S^4\) with Euler number \(-1\) is homeomorphic to \(S^7\).

**Solution.** Proposition A.4 identifies the bundle smoothly with a unique \(\xi_{h,j}\); (A.9) makes \(h+j=-1\). Pullback by the base reflection \(u\mapsto\bar u\) changes the transition to that of \(\xi_{-h,-j}\), whose exponent sum is one. The induced total-space map is a diffeomorphism over the base reflection; the normalized sphere maps of the smooth bundle isomorphism are also diffeomorphisms. Section C's explicitly checked two-critical-point function and full sphere criterion therefore give the required homeomorphism. No assertion that a homology sphere is automatically a sphere is used.

## B. The disk bundle and its relative square

Let \(W=D(\xi_{h,j})\), \(M=S(\xi_{h,j})=\partial W\), and \(\pi:W\to S^4\). Orient \(W\) by base first and fibre last, and \(M\) by its outward-normal-first boundary orientation. Transition maps preserve both choices. In bundle charts the norm-one boundary is the usual smooth disk boundary; thus \(W\) is a compact smooth eight-manifold with boundary.

The vertical tangent of the full vector-bundle total space is canonically \(\pi^*\xi_{h,j}\): differentiation of translation in a fibre gives the identification. Its projection derivative has kernel this vertical tangent and quotient \(\pi^*TS^4\). A smooth metric splits the quotient, giving
\[
 TW\cong\pi^*(TS^4\oplus\xi_{h,j}).
\tag{B.1}
\]
This also holds at the disk boundary, since its tangent bundle is the restriction of the tangent bundle of the full total space. The sphere tangent plus its normal line is trivial, so \(p_1(TS^4)=0\). The Pontryagin Whitney identity is exact here: its possible two-torsion discrepancy lies in \(H^4(W;\mathbb Z)\cong\mathbb Z\), which has no two-torsion. If \(x=\pi^*u\), then
\[
 H^*(W;\mathbb Z)\cong H^*(S^4;\mathbb Z),\qquad
 p_1(TW)=2(j-h)x=kx.
\tag{B.2}
\]
The cohomology assertion follows from the fibrewise radial contraction to the zero section.

Write \(U\in H^4(W,M;\mathbb Z)\) for the positive Thom class. The disk/sphere pair has the usual Thom cohomology, as follows directly on pairs. Put \(W_0=W\setminus S^4\), removing the zero section. The radial deformation \(v\mapsto((1-t)+t/|v|)v\) retracts \(W_0\) onto \(M\). The exact pair sequences consequently identify \(H^*(W,M)\) with \(H^*(W,W_0)\), compatibly with products and forgetful maps. If \(E\) is the full bundle total space, \(v\mapsto v/\max\{1,|v|\}\) retracts \((E,E_0)\) onto \((W,W_0)\); its straight radial homotopy stays nonzero on \(E_0\). Thus the ordinary Thom theorem applies to this pair. Its Thom isomorphism and forgetful map are
\[
 H^4(W,M)=\mathbb Z U,\qquad
 J(U)=\pi^*e(\xi_{h,j})=e x,
 \quad e=h+j.
\tag{B.3}
\]
The absolute image of the first relative cup factor can be used when multiplying two relative classes. Therefore
\[
 U\smile U=J(U)\smile U=e\,x\smile U,
 \qquad
 \langle x\smile U,[W,M]\rangle=1.
\tag{B.4}
\]
Here the second identity includes its sign. Represent the positive base generator by the point-local class in an oriented base disk and restrict the Thom class to its trivial bundle chart. Excision reduces the evaluation to a positive base four-disk crossed with a positive fibre four-disk, relative to the base-disk boundary and fibre-sphere boundary. The proved cross-product/cup evaluation makes this value the product of their values, namely one. Its product orientation is exactly base first, fibre last; switching four-dimensional factors introduces no sign. The relative fundamental class has this local product value by the integer local-orientation construction. This proves the evaluation without choosing an unspecified sign for the intersection form.

When \(e=1\), (B.3) is an isomorphism in degree four. The relative intersection pairing has matrix \((1)\) in the Thom basis by (B.4). Consequently
\[
 \sigma(W)=1,\qquad
 \widetilde p_1=J^{-1}p_1(TW)=kU,
 \qquad
 \langle\widetilde p_1^2,[W,M]\rangle=k^2.
\tag{B.5}
\]
The integral Gysin sequence also gives \(H^*(M;\mathbb Z)=\mathbb Z\) in degrees zero and seven and zero elsewhere: multiplication by \(u\) identifies base degrees zero and four, and the top connecting map identifies degree seven with \(H^4(S^4)\). The complete sequence supplies vanishing in every other degree. Section C gives the stronger sphere homeomorphism from the explicit smooth function; it does not infer that homeomorphism from these groups.

## C. Two critical points and an explicit sphere homeomorphism

This section proves the differential-topological mechanism used for the sphere-bundle examples. A homology computation alone does not produce their homeomorphism to a sphere.

### C.1. The local normal form at an extremum

**Lemma C.1.** Suppose a smooth real function has a nondegenerate minimum at a point of an \(n\)-manifold. There are smooth coordinates \(y\) centred there in which the function is its minimum value plus \(|y|^2\). At a nondegenerate maximum the analogous expression is its maximum value minus \(|y|^2\).

**Proof.** Choose initial coordinates \(x\), with the point at zero, and subtract the critical value. Taylor's formula with integral remainder gives
\[
 f(x)=x^TA(x)x,\qquad
 A(x)=\int_0^1(1-t)D^2f(tx)\,dt.
\tag{C.1}
\]
The matrix \(A\) is smooth and symmetric. At a minimum its value at zero is positive definite: the Hessian is nonnegative by the one-variable second derivative test in every direction, and nondegeneracy excludes a zero eigenvalue. It remains positive definite after shrinking the chart.

For completeness the required smooth matrix factorization is elementary. A positive definite symmetric matrix has a unique upper triangular factor \(B\) with positive diagonal and \(A=B^TB\). Construct its entries successively: take the positive square root of the first diagonal entry, divide the first row entries by it, and repeat on the remaining Schur complement. The complement is positive definite because its quadratic form is the minimum over the eliminated coordinate of the old positive quadratic form. All square roots have positive arguments and all denominators are nonzero; consequently the recursion gives a smooth \(B(x)\).

Set \(y=B(x)x\). Its derivative at zero is the invertible matrix \(B(0)\). The proved smooth inverse function theorem therefore makes \(y\) a coordinate system on a smaller neighbourhood, and (C.1) becomes \(f=|y|^2\). Apply this argument to the negative of the function at a maximum. ∎

### C.2. The sphere criterion, including the missing endpoint

**Theorem C.2.** Let \(M\) be a closed connected smooth \(n\)-manifold, \(n\geq1\), admitting a smooth function with exactly two critical points, both nondegenerate. Then \(M\) is homeomorphic to \(S^n\). Moreover \(M\) is obtained by gluing two smooth closed \(n\)-disks along a boundary diffeomorphism, and it admits a sphere homeomorphism that is a diffeomorphism away from one point.

**Proof.** Compactness gives a minimum and maximum, and these are the two critical points. They are distinct: otherwise the function is constant and every point is critical. Rescale the function to \(f:M\to[0,1]\), with minimum \(p_-\) and maximum \(p_+\). Its extreme level sets consist of their respective points, since any other extreme point would also be critical.

Lemma C.1 supplies a minimum chart in which \(f=|y|^2\), and a maximum chart in which \(f=1-|z|^2\). Choose a smooth Riemannian metric equal to the Euclidean metric in a smaller minimum chart, using the finite smooth partition construction from the bundle chapter. On \(M\setminus\{p_-,p_+\}\) put
\[
 V=\frac{\operatorname{grad}f}{|\operatorname{grad}f|^2},
 \qquad df(V)=1.
\tag{C.2}
\]
This is a smooth vector field on that open set. For any \(0<a<b<1\), the band \(f^{-1}([a,b])\) is compact and misses the critical points. A trajectory of \(V\) has \(f\)-value increasing at unit speed. The local flow existence theorem and a finite coordinate cover of the compact band give a common positive continuation time; repeating it proves that a trajectory can be continued for every finite interval for which its \(f\)-value stays in \([a,b]\). The same reasoning applies backwards. This is the compact-band continuation argument proved in the smooth regular-fibre section; it does not presume completeness on the punctured manifold.

Choose \(\delta>0\) small enough that the entire sublevel \(f^{-1}([0,2\delta])\) lies in the Euclidean minimum chart and that this chart contains the coordinate ball of radius \(\sqrt{2\delta}\). Such a choice exists: on the compact complement of any smaller minimum neighbourhood the function has a positive minimum. In the chart,
\(V(y)=y/(2|y|^2)\). Its flow sends \(\sqrt\delta\,a\) to \(\sqrt t\,a\) when the new \(f\)-value is \(t\), for every unit vector \(a\) and sufficiently small positive \(t\).

Let \(\Phi_s\) denote this flow, continued on compact bands, and define
\[
 P(ra)=\Phi_{r^2-\delta}(\sqrt\delta\,a)
 \quad(0<r<1,\ a\in S^{n-1}),
 \qquad P(0)=p_-.
\tag{C.3}
\]
Near zero this is exactly the minimum coordinate map \(ra\mapsto y=ra\), so it is smooth there. Elsewhere smooth dependence of the flow on initial conditions and time makes it smooth. It has \(f(P(ra))=r^2\).

Every \(x\ne p_-,p_+\) flows uniquely back to the level \(\delta\), even if \(f(x)<\delta\): use the compact band between these two positive levels. The resulting point has unique coordinates \(\sqrt\delta\,a\). Thus (C.3) is a bijection from the open unit ball onto \(M\setminus\{p_+\}\), with inverse given by radius \(\sqrt{f(x)}\) and that flow direction. This inverse is smooth off \(p_-\), and is the chart inverse near \(p_-\). Therefore \(P\) is a diffeomorphism.

The behaviour as \(r\to1\) must also be checked. For every neighbourhood \(U\) of \(p_+\), compactness of \(M\setminus U\) and uniqueness of the maximum give
\(\max_{M\setminus U}f<1\). Hence \(P(ra)\to p_+\) uniformly in \(a\) as \(r\to1\). Define \(P\) on the boundary of the closed unit ball to be \(p_+\). This extension is continuous and induces a continuous bijection
\[
 \overline D^n/\partial D^n\longrightarrow M.
\tag{C.4}
\]
Its domain is compact and its target is Hausdorff, so it is a homeomorphism. The quotient is \(S^n\): for example the radial diffeomorphism \(x\mapsto x/(1-|x|^2)\) identifies the open ball with \(\mathbb R^n\), and its norm tends uniformly to infinity on approaching the boundary. It therefore identifies the quotient with the one-point compactification of \(\mathbb R^n\), which inverse stereographic projection identifies with the sphere. This also proves the asserted smoothness off the single collapsed point.

Finally restrict (C.3) to the closed ball of radius \(\sqrt c\), for any \(0<c<1\). The inverse remains smooth at its boundary, since the flow gives coordinates transverse to the regular level \(c\). Thus \(f^{-1}([0,c])\) is a smooth closed disk. Apply the same argument to \(1-f\), choosing a metric Euclidean near its minimum \(p_+\); then \(f^{-1}([c,1])\) is another smooth closed disk. Their boundary identifications with the common level \(c\) are diffeomorphisms. They give the stated two-disk decomposition of \(M\). No smooth extension of its gluing diffeomorphism over the disks has been asserted. ∎

### C.3. Quaternionic clutching and the global function

Write \(\mathbb H\) for the quaternions, with norm \(|\cdot|\), conjugation \(\bar v\), and real part \(\operatorname{Re}v\). Identify the base sphere with two quaternionic coordinate charts \(u,u'\in\mathbb H\), related on their overlap by
\[
 u'=u/|u|^2.
\tag{C.5}
\]
This atlas is smooth: it is the usual two stereographic charts with a fixed orthogonal choice of axes, and their transition and its inverse are smooth away from zero.

For integers \(h,j\), glue two trivial real four-plane bundles by the orthogonal map
\[
 v'=q^h vq^j,
 \qquad q=u/|u|.
\tag{C.6}
\]
Integer powers of a unit quaternion are smooth, including negative powers, so these transition functions define a smooth bundle \(\xi_{h,j}\). Left and right unit multiplication preserve the real inner product and have determinant \(+1\): their determinants are continuously valued in \(\{\pm1\}\), the unit quaternion sphere is connected, and the identity has determinant one. Thus the norm and an orientation give a global unit sphere bundle \(M_{h,j}=S(\xi_{h,j})\). It is a closed connected smooth seven-manifold. Compactness follows from finitely many compact base pieces with bundle trivializations and compact fibre \(S^3\); connectedness follows by lifting successive subintervals of a base path in bundle charts and then joining within a fibre.

Assume \(h+j=1\). On the first chart define
\[
 F(u,v)=\frac{\operatorname{Re}v}{\sqrt{1+|u|^2}},
 \qquad |v|=1.
\tag{C.7}
\]
The extension across the missing base point is not obtained by a limit argument alone. On the second chart replace its coordinates \((u',v')\) by
\[
 a=u'(v')^{-1},\quad v';\qquad u'=av'.
\tag{C.8}
\]
These are smooth coordinates on the whole \(\mathbb H\times S^3\). Put \(\rho=|u|\). On the overlap (C.5)–(C.6) give
\[
 a=\rho^{-1}q^{1-j}v^{-1}q^{-h}
   =\rho^{-1}q^h v^{-1}q^{-h}.
\tag{C.9}
\]
Conjugation by a unit quaternion preserves the real part, and
\(\operatorname{Re}(v^{-1})=\operatorname{Re}v\) for unit \(v\). Also \(|a|=\rho^{-1}\). Consequently (C.7) is exactly the expression
\[
 F(a,v')=\frac{\operatorname{Re}a}{\sqrt{1+|a|^2}}
\tag{C.10}
\]
on the overlap. Formula (C.10) is smooth even at \(a=0\), proving that the two expressions define a global smooth function.

In the second chart write \(a=a_0+a_1i+a_2j+a_3k\). Then
\[
 \frac{\partial F}{\partial a_0}
 =\frac{1+a_1^2+a_2^2+a_3^2}{(1+|a|^2)^{3/2}}>0.
\tag{C.11}
\]
There are no critical points anywhere in this chart. In the first chart the fibre derivative vanishes only when \(v=\pm1\), since the height function on \(S^3\) has exactly those two critical points. At either such point the base derivative of (C.7) vanishes exactly when \(u=0\). Hence the global critical points are precisely \((0,1)\) and \((0,-1)\).

Their Hessians can be calculated in genuine seven-dimensional coordinates. Near each pole of the fibre write
\(v=(\pm\sqrt{1-|w|^2},w)\), with \(w\in\mathbb R^3\). Formula (C.7) becomes
\[
 F(u,w)=\pm\left(1-\tfrac12(|u|^2+|w|^2)
                      +O((|u|+|w|)^4)\right).
\tag{C.12}
\]
The Hessian is \(-I_7\) at the plus pole and \(+I_7\) at the minus pole. Both points are nondegenerate. Theorem C.2 proves
\[
 M_{h,j}\cong S^7\quad\text{as topological manifolds whenever }h+j=1.
\tag{C.13}
\]

The same conclusion holds when \(h+j=-1\). The base map defined by \(u\mapsto\bar u\), \(u'\mapsto\bar u'\) is a smooth reflection of the base sphere, since it commutes with (C.5). Pulling the transition (C.6) back by it replaces \(q\) with \(q^{-1}\), giving \(\xi_{-h,-j}\). The resulting total-space bundle map is a diffeomorphism, and \((-h)+(-j)=1\), so (C.13) applies to that bundle. ∎

### C.4. Two exercises with solutions

**Exercise C.4 — Medium: the endpoint of the flow.** In Theorem C.2, explain why following individual trajectories towards the maximum is insufficient by itself to prove continuity of (C.4). Give the needed estimate and prove that each regular level is a sphere.

**Solution.** Continuity at the collapsed boundary requires a bound uniform in the direction \(a\). Given a neighbourhood \(U\) of the unique maximum, the compact complement has maximum \(b<1\). Every point of every level with value greater than \(b\) lies in \(U\). This gives the uniform bound for (C.3). For each \(0<t<1\), continuation along the compact band between \(t\) and \(\delta\) is a diffeomorphism from level \(\delta\) to level \(t\), with inverse the backward flow. Level \(\delta\) is the coordinate sphere of radius \(\sqrt\delta\), so every regular level is diffeomorphic to \(S^{n-1}\).

**Exercise C.5 — Medium: finding all seven-dimensional critical points.** For \(h+j=1\), verify the coordinate identity for the global function and determine the critical points, their values and their indices.

**Solution.** From \(u'=q/\rho\) and \((v')^{-1}=q^{-j}v^{-1}q^{-h}\), multiplication gives (C.9). The relation \(1-j=h\) makes its quaternionic part a conjugate of \(v^{-1}\); its real part is \(\rho^{-1}\operatorname{Re}v\), and its norm is \(\rho^{-1}\). Dividing by \(\sqrt{1+\rho^{-2}}\) yields (C.7), proving the overlap identity. The strictly positive derivative (C.11) excludes every critical point on the second chart. On the first, vanishing of the fibre derivative forces \(v=\pm1\), and vanishing of the base derivative then forces \(u=0\). The critical values are \(-1\) and \(+1\). By (C.12) their Hessians are respectively positive and negative definite, so their Morse indices are \(0\) and \(7\). There are exactly two, and Theorem C.2 yields the sphere homeomorphism.


### C.5. The converse two-disk construction

Every smooth boundary gluing of two closed \(n\)-disks, \(n\geq1\), admits a smooth function with exactly two nondegenerate critical points. Thus the two-disk statement in TheoremC.2 is an equivalence.

**Proof.** Let the gluing map be \(g:S^{n-1}\to S^{n-1}\). There is a convenient equivalent smooth atlas with two copies of \(\mathbb R^n\), whose nonzero points are identified by
\[
v=\frac{1}{|u|}\,g\!\left(\frac{u}{|u|}\right).
\tag{C.14}
\]
The inverse is the same expression with \(g^{-1}\) and \(v\); both are smooth away from zero. The two radius-one closed disks form the compact gluing, with the specified boundary map \(g\). On the punctured charts the smooth collar coordinate can be taken as \(\log|u|\) and \(-\log|v|\), respectively. Their equality in (C.14), together with the angular map \(g\), shows that this atlas has precisely the smooth structure of the collar gluing. At each origin the respective Euclidean chart applies. These charts also verify the Hausdorff property: the two origins have disjoint small balls because their overlap radii are reciprocal; all other separation questions are in these open coordinate charts, shrinking across the smooth transition when needed.

Define
\[
\phi(u)=\frac{|u|^2}{1+|u|^2},\qquad
\phi(v)=\frac{1}{1+|v|^2}.
\tag{C.15}
\]
The reciprocal radii make the formulas agree on the overlap. They are smooth at both origins. Away from either origin the radial derivative is nonzero. At the first origin the Hessian is \(2I_n\); at the second it is \(-2I_n\). Thus the critical points are exactly those origins, with indices zero and \(n\). TheoremC.2 supplies the sphere homeomorphism and its smoothness off one point. Conversely that theorem constructs the two disks from any such function, proving the equivalence. This construction allows an arbitrary boundary diffeomorphism; it does not require its extension over a disk. ∎

## D. A filling-independent invariant modulo seven

Let \(M\) be a closed oriented seven-manifold satisfying
\[
 H^3(M;\mathbb Z)=H^4(M;\mathbb Z)=0.
\tag{D.1}
\]
Suppose a compact oriented smooth eight-manifold \(W\) is given with outward boundary identified orientation-preservingly with \(M\). We prove independence of the chosen filling when such a filling exists. The sphere-bundle examples have the explicit disk-bundle filling of Section B; no general theorem that every seven-manifold bounds is needed or assumed.



The [general seven-dimensional bounding theorem](oriented-seven-manifold-bounding.md#DG-CHAR-13F.proof) proves that every closed smooth oriented seven-manifold has an oriented smooth filling. Thus, in dimension seven, existence need not be an extra hypothesis in the construction below. The explicit disk-bundle fillings used here remain useful because their characteristic numbers can be computed directly. This does not remove the filling hypothesis in the higher-dimensional generalization.

### D.1. The relative square and its nondegenerate pairing

The pair sequence and (D.1) make the forgetful map an integral isomorphism
\[
 J:H^4(W,M;\mathbb Z)\xrightarrow{\cong}H^4(W;\mathbb Z).
\tag{D.2}
\]
Let \([W,M]\) be the integer relative fundamental class with the fixed ambient orientation. The signed local-boundary construction in Chern Lemma5.1 proves its existence and \(\partial[W,M]=[M]\). Define
\[
 Q_W(a,b)=\langle a\smile b,[W,M]\rangle,
 \qquad
 q(W)=\left\langle\bigl(J^{-1}p_1(TW)\bigr)^2,[W,M]\right\rangle.
\tag{D.3}
\]
The latter number is an integer. Torsion classes pair trivially with everything because their products have finite order, while evaluation takes values in \(\mathbb Z\). Cup commutativity in degree four makes the pairing symmetric.

We supply the nondegeneracy needed to define its signature, rather than invoke an unproved boundary-duality theorem. Form the smooth oriented double \(D(W)=W\cup_M(-W)\) using the full collar and gluing proofs in cobordism Theorem1.1 and Lemma2.1. Choose open neighbourhoods \(A,B\) of its two halves which include small collars on the other side. They retract to the respective halves; their intersection retracts to \(M\). Mayer–Vietoris and (D.1) give
\[
 H^4(D(W);\mathbb Z)\xrightarrow{\cong}
 H^4(W;\mathbb Z)\oplus H^4(W;\mathbb Z).
\tag{D.4}
\]

Here are the product and evaluation details of this splitting. Excision identifies a class in \(H^4(W,M)\) with a class in \(H^4(D(W),B)\) supported in the first half, and with one in \(H^4(D(W),A)\) when supported in the second half. One can obtain these identifications by removing the interiors of the opposite half beyond its collar and then contracting the remaining collar to the boundary. The relative cup of the two extended classes belongs to
\(H^8(D(W),A\cup B)=H^8(D(W),D(W))=0\). This relative-product assertion uses the small-chain model of the open cover \(A,B\): on each small simplex one relative factor vanishes on its corresponding member, and the cup formula descends to the union-relative complex. The small-chain equivalence identifies it with ordinary cohomology. Thus the two summands are orthogonal.

For two classes supported in the same half, naturality of the relative cup and evaluation gives exactly their pairing on \([W,M]\). In the second half the sign is negative, since the double gives that copy the reversed ambient orientation. More explicitly the image of the double's fundamental class in its first-half relative group is \([W,M]\), and in its second-half group is \(-[W,M]\). The integer local-orientation construction proves this by restriction at every interior point; the boundary pieces are forgotten. Consequently the middle-dimensional form of the double is
\[
 Q_{D(W)}=Q_W\oplus(-Q_W).
\tag{D.5}
\]

The closed double and its closed boundary have finite integer homology by manifold Theorem2.2 and Corollary2.3, whose full proofs were supplied earlier. In homological Mayer–Vietoris the two adjacent maps are
\[
H_i(M)\xrightarrow{\alpha}H_i(W)\oplus H_i(W)
 \xrightarrow{\beta}H_i(D(W)).
\]
Exactness gives a short exact sequence with kernel \(\operatorname{im}\alpha\), a quotient of \(H_i(M)\), and quotient \(\operatorname{im}\beta\), a subgroup of \(H_i(D(W))\). Both are finitely generated, so \(H_i(W)\oplus H_i(W)\), and hence every \(H_i(W)\), is finitely generated. The next term \(H_{i-1}(M)\) contains the image measuring the cokernel of the map to \(H_i(D(W))\). The integer coefficient theorem now gives finite generation of cohomology, also for the pair by its exact sequence. In its natural comparison with rational coefficients, the Ext terms become zero and \(\operatorname{Hom}(H_i,\mathbb Z)\otimes\mathbb Q\to\operatorname{Hom}(H_i,\mathbb Q)\) is an isomorphism for these finitely generated homology groups. Thus coefficient change has its claimed effect; no tensor operation on infinite cochain products is presumed. In particular (D.1) holds rationally and (D.2)–(D.5) hold over \(\mathbb Q\). The perfect rational cup form of the closed double and (D.5) force \(Q_W\) to be nondegenerate. Define \(\sigma(W)\) as its number of positive eigenvalues minus its number of negative eigenvalues. The torsion-free integral group supplies its rational lattice; no determinant normalization is needed for the signature.

### D.2. Gluing two different fillings

**Lemma D.1 — Additivity across this boundary.** Let \(W_0,W_1\) be two such fillings of the same \(M\), and give
\(C=W_0\cup_M(-W_1)\) the smooth closed orientation agreeing with \(W_0\). Then
\[
 \sigma(C)=\sigma(W_0)-\sigma(W_1),\qquad
 \langle p_1(TC)^2,[C]\rangle=q(W_0)-q(W_1).
\tag{D.6}
\]

**Proof.** The signed collar coordinate gives a smooth manifold across the identified boundary; its tangent bundle restricts to the original tangent bundles of each half, including their boundary points. In particular its first Pontryagin restrictions are those of \(TW_0\) and \(TW_1\), because Pontryagin classes disregard orientation. Choose the same open collar neighbourhoods \(A,B\) as in D.1. The absolute Mayer–Vietoris sequence again gives an isomorphism
\[
 H^4(C;\mathbb Z)\cong H^4(W_0;\mathbb Z)\oplus H^4(W_1;\mathbb Z).
\tag{D.7}
\]
The relative extension argument of D.1 shows that the two summands are orthogonal, with forms \(Q_{W_0}\) and \(-Q_{W_1}\). Signatures of finite nondegenerate real forms add under orthogonal direct sum, proving the first identity of (D.6).

Under (D.7), the class \(p_1(TC)\) has components \(p_1(TW_0),p_1(TW_1)\). By (D.2), these have the unique relative representatives used in (D.3). Extend those representatives to \(C\) from their respective halves. Their sum has the specified restrictions, so equals \(p_1(TC)\) by injectivity of (D.7). Its squared evaluation is the sum of their squared evaluations, since the cross product is zero. The first is \(q(W_0)\); the second is \(-q(W_1)\) by its ambient orientation. This proves the second identity, over the integers. ∎

The hypotheses (D.1) have a precise role: they make every absolute degree-four class have a unique relative representative, and make (D.7) an isomorphism. No arbitrary-boundary signature-additivity theorem has been substituted for this argument.

### D.3. The congruence and the exotic sphere

**Theorem D.2 — The invariant.** Under (D.1), when a smooth oriented filling exists, the residue
\[
 \lambda(M)=2q(W)-\sigma(W)\pmod7
\tag{D.8}
\]
is independent of the filling. It is preserved by orientation-preserving diffeomorphisms and changes sign when the orientation is reversed. The standard sphere has \(\lambda(S^7)=0\), with either orientation.

**Proof.** For every closed oriented smooth eight-manifold the already proved signature theorem, with its explicit second L-polynomial, gives
\[
 45\sigma(C)=\langle7p_2(TC)-p_1(TC)^2,[C]\rangle.
\tag{D.9}
\]
Both Pontryagin numbers are integers. Multiply the rearranged equality by two and reduce modulo seven. Since \(90\equiv-1\pmod7\), it becomes
\[
 2\langle p_1(TC)^2,[C]\rangle-\sigma(C)\equiv0\pmod7.
\tag{D.10}
\]
Apply Lemma D.1 to the two fillings. Equation (D.10) states exactly that their expressions in (D.8) agree.

Changing the orientation of \(W\) changes its boundary to \(-M\), negates its relative fundamental class, and negates its intersection-form signature. Its Pontryagin class is unchanged. Thus both terms in (D.8) change sign. An orientation-preserving diffeomorphism of boundaries simply gives another boundary identification of a filling; independence proves diffeomorphism invariance. Finally the standard sphere bounds its standard disk, whose degree-four groups vanish. Its relative square and signature are zero, so its invariant is zero. The opposite disk orientation proves the same for the opposite sphere orientation. ∎

**Theorem D.3 — An explicit exotic seven-sphere.** Take \(h=-1,j=2\), and give \(M=S(\xi_{-1,2})\) the boundary orientation of its disk bundle. Then \(M\) is homeomorphic to \(S^7\) and has \(\lambda(M)=1\). In particular it is not diffeomorphic to the standard sphere, even if a diffeomorphism is allowed to reverse orientation.

**Proof.** By (A.9), its Euler class is \(u\) and its first Pontryagin class is \(6u\). Section C proves the homeomorphism from the actual global function with two nondegenerate critical points. Its degree-three and degree-four cohomology vanish, either from that homeomorphism or from the exact Gysin computation in Section B. Thus (D.8) applies. For its disk bundle (B.5) gives
\[
 \lambda(M)=2\cdot6^2-1=71\equiv1\pmod7.
\tag{D.11}
\]
The standard sphere has invariant zero with both orientations by Theorem D.2. Every orientation-preserving or reversing diffeomorphism to it would therefore force this value to be zero or the negative of zero, a contradiction. ∎

More generally the bundles with \(h+j=1\) have \(k=2(j-h)\equiv2\pmod4\) and
\[
 \lambda(S(\xi_{h,j}))=2k^2-1\pmod7.
\tag{D.12}
\]
This construction supplies infinitely many parameter choices, but (D.12) alone is a finite-valued invariant; it does not assert infinitely many distinct diffeomorphism types. Its PL-sphere and coned-filling applications use the complete relative triangulation and disk-comparison proofs supplied in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md).

### D.4. Two exercises with complete solutions

**Exercise D.4 — Medium: why the residue is well defined.** Reconstruct the filling-independence proof, explaining why an ordinary square on \(W\) cannot replace the relative square. Determine the effect of reversing the orientation.

**Solution.** The number must be evaluated on \([W,M]\), a relative fundamental class. Its compatible degree-eight cohomology class is the square of the unique degree-four relative lift of \(p_1(TW)\), obtained from (D.2). An absolute degree-eight class alone does not supply this relative lift; in the disk-bundle example the absolute cohomology in degree eight is zero while its relative squared evaluation is \(k^2\). Glue \(W_0\) to \(-W_1\) by the collar construction. The two relative degree-four extensions are orthogonal because their mixed cup lies in the union-relative group of the full closed manifold, which is zero. Their self-evaluations have opposite signs, so the closed signature and Pontryagin square are their differences. The closed signature identity gives (D.10), making those differences zero modulo seven. Reversal negates the relative fundamental class and the signature, so \(\lambda(-M)=-\lambda(M)\).

**Exercise D.5 — Hard: distinguish a smooth structure without changing the topology.** For the sphere bundles with \(h+j=1\), give a parameter pair for which the mod-seven obstruction is nonzero. Prove both the sphere homeomorphism and the failure of every diffeomorphism to the standard sphere.

**Solution.** Choose \((h,j)=(-1,2)\). The transition gives a smooth sphere bundle. Its global function is (C.7) in the first chart and (C.10) in the second; (C.9) verifies equality. The second-chart real derivative is strictly positive, while the first chart has precisely two critical points with Hessians \(\pm I_7\). The full compact-band flow and uniform endpoint proof in Theorem C.2 therefore identify its total space homeomorphically with \(S^7\). Formula (A.9) gives \(e=u,p_1=6u\). The disk bundle has relative Thom generator mapping to the base generator, relative squared evaluation \(36\) and signature one. Thus its invariant is \(71\equiv1\). The sphere bounds a disk with invariant zero. Filling independence and the sign rule exclude a diffeomorphism with either orientation behaviour. The nonzero residue distinguishes smooth structures on the same topological manifold.


### D.5. Filling restrictions and orientation reversal

Under the hypotheses of TheoremD.2, if \(\lambda(M)\ne0\), every smooth oriented filling of \(M\) has positive fourth Betti number. Moreover \(M\) has no orientation-reversing self-diffeomorphism.

**Proof.** If a filling \(W\) had \(H^4(W;\mathbb Q)=0\), the finite-generation and coefficient comparison in D.1 would make its integral degree-four group torsion. Its unique relative Pontryagin lift would then be torsion as well. Its squared evaluation is zero in \(\mathbb Z\), and its rational middle form has dimension zero, so \(q(W)=\sigma(W)=0\). Equation (D.8) would give \(\lambda(M)=0\), a contradiction. The field coefficient theorem identifies the fourth Betti number with this rational cohomology dimension. If a self-diffeomorphism reversed orientation, the invariant would equal its own negative by TheoremD.2. This would give \(2\lambda(M)=0\) in \(\mathbb Z/7\). Multiplication by two is invertible in that group, again a contradiction. In particular both assertions apply to \(S(\xi_{-1,2})\), whose residue is one. ∎

### D.6. The same residue mechanism in dimension \(4k-1\)

The relative gluing argument also gives a higher-dimensional residue. Fix \(k\geq2\), and choose a positive integer \(d_k\) clearing the denominators of the proved Hirzebruch polynomial \(L_k\). Write
\[
d_k L_k=a_kp_k+R_k(p_1,\ldots,p_{k-1}),
\qquad a_k>0,
\tag{D.13}
\]
where \(a_k\) and the coefficients of \(R_k\) are integers. The strict positivity of the indecomposable coefficient was proved in combinatorial LemmaB.1, so this choice has \(a_k\ne0\). Every monomial in \(R_k\) has total weight \(k\) and at least two factors.

Let \(N\) be a smooth closed oriented \((4k-1)\)-manifold satisfying
\[
H^{2k-1}(N;\mathbb Z)=H^{2k}(N;\mathbb Z)=0,\qquad
H^{4j-1}(N;\mathbb Z)=H^{4j}(N;\mathbb Z)=0
\quad(1\leq j<k).
\tag{D.14}
\]
Assume a compact smooth oriented filling \(V\) is given. The relative maps in degrees \(4j\) are isomorphisms by the pair sequence. Write \(\widetilde p_j\) for the unique relative lift of \(p_j(TV)\), and put
\[
q_R(V)=\left\langle R_k(\widetilde p_1,\ldots,\widetilde p_{k-1}),
 [V,N]\right\rangle,\qquad
\Lambda_k(N)=d_k\sigma(V)-q_R(V)\pmod {a_k}.
\tag{D.15}
\]
Then \(\Lambda_k(N)\) is independent of the filling, is invariant under orientation-preserving diffeomorphisms, changes sign under orientation reversal, and is zero on the standard sphere.

**Proof.** All relative lifts and evaluations in (D.15) are integral. The middle-dimensional relative map is an isomorphism by the first part of (D.14). The double argument in D.1 works in degree \(2k\): the Mayer–Vietoris map from the double to the two halves is an isomorphism; opposite supported relative classes have zero mixed cup; and their same-half evaluations have opposite ambient signs. The perfect closed middle form consequently makes the filling's rational form nondegenerate. The corrected finite-generation argument in D.1 applies in every degree, so rational coefficient comparison and the signature are defined exactly as there.

For two fillings form \(C=V_0\cup_N(-V_1)\). Applying the same Mayer–Vietoris and supported relative-extension argument in each degree \(4j\) identifies \(p_j(TC)\) with the sum of the two extended relative lifts. On expanding a monomial of \(R_k\), every mixed-half term vanishes: at least two factors belong to opposite relative supports, whose cup lies in the zero cohomology of the union-relative pair. A same-half term evaluates on that half's relative fundamental class, positively for \(V_0\) and negatively for \(V_1\). Therefore
\[
\langle R_k(p_1(TC),\ldots,p_{k-1}(TC)),[C]\rangle
 =q_R(V_0)-q_R(V_1),\qquad
\sigma(C)=\sigma(V_0)-\sigma(V_1).
\tag{D.16}
\]
The second identity follows from the orthogonal middle-form splitting, not from an unrestricted signature-additivity assertion.

The closed signature theorem and (D.13) give
\[
d_k\sigma(C)-\langle R_k(p_1(TC),\ldots,p_{k-1}(TC)),[C]\rangle
 =a_k\langle p_k(TC),[C]\rangle.
\tag{D.17}
\]
The last evaluation is an integer. Reducing modulo \(a_k\) and using (D.16) proves filling independence. Reversal negates all evaluations and the signature while leaving Pontryagin classes unchanged, and boundary reidentification by a positive diffeomorphism does not change the filling numbers. Finally the standard disk has zero positive-degree classes and a zero-dimensional middle form; it gives residue zero for the standard sphere. This proves every assertion without a general bounding theorem. ∎

For example \(d_2=45\), \(a_2=7\), \(R_2=-p_1^2\). Hence \(\Lambda_2=45\sigma+q\) modulo seven, and \(2\Lambda_2=2q-\sigma=\lambda\). The next signature polynomial gives \(d_3=945\), \(a_3=62\), \(R_3=2p_1^3-13p_1p_2\); (D.14) and a given filling therefore supply the analogous integral residue modulo62 for eleven-manifolds. An integral homology sphere satisfies all the stated cohomology vanishings, but existence of a smooth filling remains an explicit hypothesis.

### D.7. A positive sphere diffeomorphism outside the identity isotopy class

There is a degree-one diffeomorphism of \(S^6\) which is not smoothly isotopic to the identity.

**Proof.** TheoremC.2 writes the explicit exotic manifold of TheoremD.3 as two smooth seven-disks. Choose disk parametrizations. Their boundary diffeomorphism is \(g:S^6\to S^6\); composing one parametrization with a linear disk reflection if necessary makes \(g\) have degree \(+1\). This changes only the parametrization of the same smooth gluing.

Suppose there were a smooth isotopy \(g_t\), \(0\leq t\leq1\), from the identity to \(g\). Choose a smooth function \(\chi:[0,1]\to[0,1]\) equal to zero near zero and one near one. The map
\[
G(ra)=r g_{\chi(r)}(a)\quad(0<r\leq1),\qquad G(0)=0
\tag{D.18}
\]
is the identity near the disk centre and is a smooth collar product near its boundary. It is a diffeomorphism: it preserves the radius, and its inverse uses the smooth family \(g_{\chi(r)}^{-1}\). Smoothness of that inverse family follows from the local inverse theorem applied to \((a,t)\mapsto(g_t(a),t)\). Thus \(G\) extends \(g\) over the disk.

Applying \(G^{-1}\) on the second disk and the identity on the first changes the gluing by \(g\) to the identity gluing. The maps fit smoothly across the collars since (D.18) is a collar product there. The identity double is the standard smooth sphere: parametrizations of its two hemispheres are
\[
ra\longmapsto
\bigl(\sin(\pi r/2)a,\ \pm\cos(\pi r/2)\bigr).
\tag{D.19}
\]
They are smooth and full rank at the centres and boundary, and their signed collar parameters agree on the double. This would give a diffeomorphism from the exotic manifold to the standard sphere, contrary to TheoremD.3. Hence \(g\) has no such isotopy. Its degree is one by construction. This proves a distinction between degree and smooth isotopy without claiming an isotopy classification. ∎

## E. What the example changes

Theorem C.2 gives two smooth disks and a boundary diffeomorphism for every sphere bundle in this construction with Euler number one. Theorem D.3 proves that at least one such gluing produces a smooth manifold that is homeomorphic to a sphere and admits no diffeomorphism to the standard sphere. Thus the topology of the total space and the smooth structure of its disk gluing contain different information. The proof detects that difference through the relative square on a filling, rather than through the cohomology groups of the seven-manifold itself.

Two further questions are how smooth sphere structures vary, and which tangent characteristic classes survive passage between smooth, PL and topological categories. The finite-valued residue proved here does not classify all smooth sphere structures. The previous chapter proves its stated rational comparison for each given compatible triangulation. A stronger topological-invariance theorem requires additional arguments. Neither broader question is a premise of this lesson.

The curvature chapter expresses the already defined characteristic classes by differential forms and connects Euler-class evaluation with the Pfaffian form and Gauss–Bonnet. The present construction already fixes the integral normalization that such representatives must respect.

## Sources and proof scope

Nikhil Sahoo, [*An Exotic Sphere*](https://e.math.cornell.edu/people/Nikhil_Sahoo/files/notes/exotic-7-spheres.pdf), treats Milnor’s quaternionic sphere bundles, their characteristic classes and the obstruction to a standard smooth sphere. The local normal form used here is the extremum case of the Morse lemma; the two-critical-point criterion is Reeb’s sphere theorem. Sections C.1–C.3 give their proofs and the explicit function, while Section D develops the filling invariant from the signature theorem and relative gluing.

John Milnor, with notes by James Stasheff, [*Lectures on Characteristic Classes* (1957)](https://math.mit.edu/~hrm/manuscripts/milnor-characteristic-classes.pdf), treats prescribed four-plane characteristic classes and the coned-filling obstruction. The integral PL obstruction is proved in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md). Every residue in this lesson assumes a given smooth oriented filling; the sphere-bundle examples use their explicit disk bundles.
