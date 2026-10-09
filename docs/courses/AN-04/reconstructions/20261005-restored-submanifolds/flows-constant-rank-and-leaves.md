# Flows, constant-rank bundles and characteristic leaves

This companion supplies the elementary smooth-geometric steps used in [Homogeneous submanifold normal forms](homogeneous-submanifold-normal-forms.md). Its flow inputs are the complete [finite-coordinate flow proofs, Sections 17.1–17.7](../20261005-restored-phase-space/finite-coordinate-flows.md): existence and uniqueness, smooth dependence, the variational equation, continuation and the flow law. The forms companion F0–F2 proves exterior differentiation, Cartan's formula and pullback differentiation. The inverse theorem and finite-dimensional linear algebra are proved in the [stationary-phase prerequisites](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md). The [proof map](proof-map.json) gives the exact earlier proof locators.

## F0. Tangency and transverse flow coordinates

Let a smooth vector field \(X\) on a manifold be tangent to an embedded submanifold \(V\). In submanifold coordinates \((y,z)\), with \(V=\{z=0\}\), tangency says \(X_z(y,0)=0\). Solve the tangential equation \(y'=X_y(y,0)\). The curve \((y(t),0)\) then solves the full ambient equation with the prescribed initial point of \(V\). Uniqueness identifies it with the ambient flow. Thus the local flow preserves \(V\); applying the inverse flow gives equality wherever both maps are defined. Cover a longer trajectory by finitely many such charts to obtain the same assertion on each compact part of its existence interval. This is a local statement and assumes no completeness.

If \(X(c)\ne0\), choose a coordinate hypersurface \(W\) through \(c\) transverse to \(X(c)\). The derivative of \((t,z)\mapsto\phi_t(z)\), at \((0,c)\), sends the time direction to \(X(c)\) and the slice directions identically to \(T_cW\). It is invertible. The inverse theorem gives a local coordinate chart, and the flow law gives \(X=\partial_t\) in it. If \(X\) is tangent to \(V\), choose the slice so its restriction to \(V\) is transverse there. The same argument on \(V\), together with preservation just proved, identifies \(V\) locally with the product of the time interval and \(V\cap W\).

## F1. Commuting flows and homogeneous weights

Write \(\phi_s\) for the flow of \(X\), and \(J_s(z)=D_z\phi_s(z)\). The variational equation is \(\partial_sJ_s=DX(\phi_s)J_s\). The inverse flow makes \(J_s\) invertible. For another smooth field \(Y\), the chain and product rules give
\[
 \frac{d}{ds}\big[J_s(z)^{-1}Y(\phi_s(z))\big]
 =J_s(z)^{-1}\big(DY\,X-DX\,Y\big)(\phi_s(z))
 =J_s(z)^{-1}[X,Y](\phi_s(z)).
\]
All statements hold on one sufficiently small common flow domain. If \([X,Y]=0\), this proves \(D\phi_s\,Y=Y\circ\phi_s\). Consequently the two curves \(t\mapsto\phi_s\psi_t(z)\) and \(t\mapsto\psi_t\phi_s(z)\) solve the same \(Y\) equation and have the same initial value. Uniqueness proves that the flows commute.

For independent pairwise commuting fields \(X_1,\ldots,X_j\), choose a transverse codimension-\(j\) slice. Compose their flows with times \(t_1,\ldots,t_j\) starting on that slice. The derivative at zero is invertible because the slice tangent and the given field vectors are complementary. Inverse coordinates therefore exist. Flow commutation shows that differentiating in \(t_i\) gives \(X_i\), so these are joint flow coordinates. This proves the precise two-field construction used for the homogeneous canonical pair.

More generally, if \([X,Y]=aY\) for a constant \(a\), the displayed equation and the scalar linear ODE give
\[
 J_s^{-1}Y(\phi_s(z))=e^{as}Y(z),\qquad
 (\phi_s)_*Y=e^{-as}Y.
\]
For the radial field \(R\), its time-\(s\) flow is dilation \(M_{e^s}\). Thus \([R,Y]=-Y\) gives \((M_t)_*Y=tY\), while \([R,Y]=0\) gives \((M_t)_*Y=Y\). The signs follow from the displayed derivative, without identifying pullback and pushforward.

Finally, if \(\iota_{H_f}\omega=-df\) and \(d\omega=0\), Cartan's formula gives \(\mathcal L_{H_f}\omega=-d^2f=0\). Pullback differentiation then gives \(\phi_s^*\omega=\omega\). This proves the form preservation used in the canonical product construction. These identities first hold near a chosen radial slice; the dilation identities extend them to its conic saturation. Their validity does not require a Hamilton field to have a globally complete flow.

## F2. Constant rank gives smooth kernels, images and quotients

Consider a smooth matrix \(A(x)\) with constant rank \(r\). For \(r>0\), permute rows and columns so an \(r\)-by-\(r\) block \(B\) is invertible at the marked point, and restrict to a neighborhood on which it stays invertible. Write
\[
 A=\begin{pmatrix}B&E\\ C&D\end{pmatrix}.
\]
Multiplication by invertible block triangular matrices reduces this to diagonal blocks \(B\) and \(D-CB^{-1}E\). Constant rank forces the second block to be zero. Hence the kernel consists exactly of vectors \((-B^{-1}Ew,w)\), with \(w\) free. They give a smooth frame of the kernel. The first \(r\) columns of \(A\) give a smooth frame of the image. Matrix inversion is smooth by the cofactor formula and the nonzero determinant. For \(r=0\), the matrix is identically zero and the conclusion is immediate. Applying these computations in bundle frames proves the same claims for smooth bundle maps of constant rank.

A smooth subbundle frame can be completed locally to an ambient frame: choose complementary vectors at one point and keep their coordinate coefficients constant; the resulting determinant stays nonzero nearby. This supplies local complements and quotient frames. On overlaps, their transition functions are the corresponding smooth matrices of basis changes, using the same inverse formula. Thus quotients are smooth vector bundles, without any claim that they are globally trivial. Constant-rank sums of subbundles are images of their addition map; intersections are identified with kernels of their difference map. The preceding matrix argument applies to both.

For a submanifold \(V\) of a symplectic manifold, the map \(TS|_V\to T^*V\), sending \(u\) to \(\omega(u,\cdot)|_{TV}\), is surjective: extend any covector from \(TV\) to the ambient tangent and use the nondegenerate ambient form. Its kernel is \((TV)^\omega\), so this orthogonal bundle is smooth. If the restricted form has constant rank, its bundle-map kernel \(\mathcal Z=TV\cap(TV)^\omega\) is smooth as well. The rank formula for the sum then makes \(TV+(TV)^\omega\) smooth.

A smooth bilinear form whose radical is a smooth subbundle descends to a smooth nondegenerate form on the quotient: evaluate it on any local smooth representatives in a complementary frame. Changing a representative by a radical vector changes no value, and nondegeneracy is precisely the definition of the radical. In particular the fiberwise symplectic quotient and its orthogonal splitting in the lesson assemble into smooth symplectic bundles. If symplectic frames are desired, choose at a point a pair with nonzero pairing, retain that pair nearby, divide by its smooth nonzero pairing and subtract its two components from the remaining vectors. Repeat on the symplectic orthogonal complement. This finite construction is smooth and produces the required local symplectic frames.

## F3. From local plaques to maximal connected leaves

Suppose a smooth rank-\(k\) distribution already has an atlas of product charts \((q,z)\) in which it is spanned by \(\partial_{q_1},\ldots,\partial_{q_k}\). A plaque is a connected coordinate slice with \(z\) fixed. This assumption is supplied by the ordinary submanifold normal form in the lesson; no general integrability theorem is being invoked here.

On an overlap, the transverse coordinates of the second chart have zero derivative in every \(q\) direction of the first. The fundamental theorem along coordinate segments makes them constant on each connected overlap component of a plaque. The two plaques through an overlap point therefore agree locally. Define two points to be equivalent when a finite chain of intersecting plaques joins them. The equivalence class has the topology and smooth charts generated by those plaque patches. On overlaps the transition maps are restrictions of ambient smooth coordinate maps and have smooth inverses. Its inclusion into the ambient manifold is an injective immersion with tangent equal to the given distribution. It need not be an embedding with the ambient subspace topology.

Here are the needed topological details. The ambient manifold is Hausdorff and second countable, as in the programme's manifold convention. Distinct leaf points can be separated by ambient open sets, whose intersections with every plaque are open; hence the leaf topology is Hausdorff. Take a countable product-chart cover, obtained by choosing from a countable ambient basis a subcover of the product neighborhoods. For any one plaque, its intersection with another chart is an open subset of its coordinate \(\mathbb R^k\), with at most countably many connected components: each component contains a different member of a countable basis. Each component lies in one plaque of the other chart. Starting with a plaque through the marked point, passage through countably many charts and then through finite chains consequently reaches only countably many plaques. They cover its entire equivalence class. Their countable coordinate bases give a countable basis for the leaf topology. When \(k=0\), the leaf is a single point and the same conclusions hold directly. The class is connected because every reached plaque is connected to the first by such a finite chain.

Any connected immersed integral manifold is contained in one such leaf. Locally its transverse coordinate derivatives vanish, so its image lies in one plaque. A connected manifold is path connected here: the points reachable by piecewise coordinate paths form open equivalence classes, so connectedness leaves only one class. A path has compact parameter interval; subdividing into finitely many chart intervals gives a finite plaque chain. This also proves that every piecewise smooth curve tangent to the distribution stays in one leaf on each connected parameter interval, by applying the same finite subdivision on compact subintervals. The leaves are therefore the unique maximal connected integral manifolds, with the specified immersed smooth structure.

A diffeomorphism preserving the distribution sends plaques locally into plaques and hence sends a leaf into a leaf. Its inverse gives equality and the inverse smooth map on the leaf structures. It therefore permutes the maximal leaves. This is the exact patching and maximality assertion used in the lesson's radial dichotomy. It makes no assertion that the global space of leaves is Hausdorff.

## Source and authorship

The characteristic-foliation application is credited in the main lesson to the edition of Lars Hörmander's *The Analysis of Linear Partial Differential Operators III*, §21.2. The elementary arguments here are written out independently from the earlier programme's complete flow, calculus and linear-algebra proofs. No source citation replaces one of those proofs, and no book text or figure is reproduced.

*Written by GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Original exposition: public domain (CC0). Linked programme components retain their own notices.*
