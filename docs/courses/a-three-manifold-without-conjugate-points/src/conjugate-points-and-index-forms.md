# Conjugate points and index forms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Riemannian metric has *no conjugate points* if no nonzero Jacobi field along a geodesic vanishes at two different times. Nonpositive sectional curvature implies this, and on closed surfaces the two conditions describe the same manifolds. This course proves the theorem of [OpenAI-NC] that in dimension three they do not: there is a closed three-manifold that carries a metric without conjugate points but no metric of nonpositive sectional curvature.

This lesson fixes the conventions, recalls the question, and proves the two general facts on index forms that the construction rests on: nonnegativity of the index form of compactly supported fields along every complete geodesic excludes conjugate points, and this nonnegativity may be checked separately on each visit of a geodesic to a region where the curvature may be positive.

- Jacobi fields, conjugate points and the question (Section 1).
- Index forms along complete geodesics (Section 2).
- The theorem and the plan of the course (Section 3).

## 1. Jacobi fields, conjugate points and the question

Manifolds are smooth, Hausdorff and second countable, and Riemannian metrics are smooth. We use the Levi-Civita connection, write \(D_s\) for covariant differentiation along a curve, and use the curvature convention of [Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem):
\[
\begin{aligned}
R(X,Y)Z&=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ\\
&\quad-\nabla_{[X,Y]}Z .
\end{aligned}
\]
With this convention the sectional curvature of the plane spanned by orthonormal vectors \(X,Y\) is \(\langle R(X,Y)Y,X\rangle\), and for every vector \(V\) and unit vector \(T\), with \(V^\perp=V-\langle V,T\rangle T\),
\[
\begin{aligned}
&\langle R(V,T)T,V\rangle\\
&\quad=K(V,T)\,|V^\perp|^2
\end{aligned} \tag{1.1}
\]
when \(V\) is not a multiple of \(T\), where \(K(V,T)\) is the sectional curvature of the plane they span; the left side is \(0\) when \(V\) is a multiple of \(T\). In particular \(\langle R(V,T)T,V\rangle\le0\) wherever the sectional curvatures are nonpositive.

Let \(\gamma\) be a geodesic and \(T=\dot\gamma\). A *Jacobi field* along \(\gamma\) is a smooth field \(J\) with
\[
D_s^2J+R(J,T)T=0 . \tag{1.2}
\]
It is determined by \(J(s_0)\) and \(D_sJ(s_0)\) at any one time ([Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem), Theorem A.1).

**Definition 1.1.** A Riemannian manifold has *no conjugate points* if, for every geodesic \(\gamma\colon I\to M\) and every Jacobi field \(J\ne0\) along \(\gamma\), there is at most one \(s\in I\) with \(J(s)=0\).

Along a constant geodesic the Jacobi equation reads \(D_s^2J=0\), whose nonzero solutions vanish at most once; for a geodesic with constant speed \(c>0\), the reparametrization \(s\mapsto\gamma(s/c)\) has unit speed and the same Jacobi fields up to the same change of variable. So it suffices to consider unit-speed geodesics. On a complete manifold every geodesic extends to all of \(\mathbb R\).

If every sectional curvature is nonpositive, there are no conjugate points ([Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem), Corollary F.3). The converse fails for individual metrics: local modifications of negatively curved metrics can create positive curvature without creating conjugate points (Gulliver's examples, recalled in [IK, Section 1]). The question is therefore about manifolds, not metrics.

**Question 1.2** ([IK, Questions 1.1 and 8.1], [BM, Section 4.1]). Does every closed manifold that carries a metric without conjugate points also carry a metric of nonpositive sectional curvature?

On a closed surface the answer is affirmative by the uniformization theorem [BM, Section 4.1]. Ivanov and Kapovitch single out graph manifolds as the test case in dimension three and ask in particular about two copies of a punctured torus times a circle glued along their boundary tori [IK, Section 8]. The theorem of this course answers the question negatively with a manifold of exactly this kind.

## 2. Index forms along complete geodesics

Let \(\gamma\colon\mathbb R\to M\) be a unit-speed geodesic and \(T=\dot\gamma\). For smooth fields \(V,W\) along \(\gamma\) and an interval \(J\subseteq\mathbb R\) put
\[
\begin{aligned}
&B_J(V,W)\\
&\quad=\int_J\bigl(\langle D_sV,D_sW\rangle\\
&\qquad-\langle R(V,T)T,W\rangle\bigr)\,ds,\\
&I_J(V)=B_J(V,V),
\end{aligned} \tag{2.1}
\]
whenever the integrand is integrable, for example when \(J\) is bounded or one of the fields vanishes outside a compact set. The form \(B_J\) is symmetric, because \(\langle R(V,T)T,W\rangle=\langle R(W,T)T,V\rangle\). We write \(I=I_{\mathbb R}\) and \(B=B_{\mathbb R}\). For a variation of \(\gamma|_{[a,b]}\) with field \(V\), the second derivative of the energy is \(I_{[a,b]}(V)\) plus an endpoint term ([Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem), Theorem A.4); the index form will be used through the two results below.

A *compactly supported \(H^1\) field* along \(\gamma\) is a field \(V\) vanishing outside a compact interval whose coefficients in a parallel orthonormal frame are absolutely continuous with square-integrable derivatives. Parallel orthonormal frames along \(\gamma\) exist, and in such a frame \(D_s\) is ordinary differentiation of the coefficient vector. Continuous fields that are smooth on each interval of a finite subdivision, and vanish outside a compact set, are compactly supported \(H^1\) fields.

**Lemma 2.1.** Suppose \(I(W)\ge0\) for every smooth field \(W\) along \(\gamma\) that vanishes outside a compact set. Then \(I(V)\ge0\) for every compactly supported \(H^1\) field \(V\) along \(\gamma\).

*Proof.* Fix a parallel orthonormal frame \(E_1,\dots,E_n\) and write \(V=\sum_iv_iE_i\). Then \(I(V)=\int(|v'|^2-v^{\mathsf T}K(s)v)\,ds\), where \(K(s)\) is the symmetric matrix with entries \(\langle R(E_i,T)T,E_j\rangle\), continuous in \(s\). Let \(v\) vanish outside \([\alpha,\beta]\), let \(\rho_\varepsilon\) be a smooth nonnegative mollifier of integral \(1\) supported in \([-\varepsilon,\varepsilon]\), and \(v^\varepsilon=\rho_\varepsilon*v\). Then \(v^\varepsilon\) is smooth and vanishes outside \([\alpha-\varepsilon,\beta+\varepsilon]\). Since \(v\) is continuous with compact support, \(v^\varepsilon\to v\) uniformly; since \(v'\) is square integrable, \((v^\varepsilon)'=\rho_\varepsilon*v'\to v'\) in \(L^2\). On the compact interval \([\alpha-1,\beta+1]\) the matrix \(K\) is bounded, so \(I(\sum_iv^\varepsilon_iE_i)\to I(V)\) as \(\varepsilon\to0\). The approximating fields are smooth and compactly supported, so their index forms are nonnegative, and so is the limit. \(\square\)

**Lemma 2.2** (the index criterion; [OpenAI-NC, Lemma 6.2]). Let \((M,g)\) be complete. If \(I(V)\ge0\) for every smooth field \(V\) vanishing outside a compact set, along every unit-speed geodesic \(\gamma\colon\mathbb R\to M\), then \(g\) has no conjugate points.

*Proof.* By the remarks after Definition 1.1 it suffices to consider unit-speed geodesics, which are defined on \(\mathbb R\). Suppose a Jacobi field \(J\ne0\) along \(\gamma\) vanishes at times \(a<b\). Let \(\widehat J\) equal \(J\) on \([a,b]\) and \(0\) elsewhere; it is continuous and piecewise smooth, so it is a compactly supported \(H^1\) field. Integration by parts and (1.2) give
\[
\begin{aligned}
&I(\widehat J)=\bigl[\langle D_sJ,J\rangle\bigr]_a^b\\
&\quad-\int_a^b\langle D_s^2J+R(J,T)T,J\rangle\,ds\\
&\quad=0 .
\end{aligned}
\]
For every smooth compactly supported \(W\) and every real \(t\), Lemma 2.1 applied to the \(H^1\) field \(\widehat J+tW\) gives
\[
0\le I(\widehat J+tW)=2t\,B(\widehat J,W)+t^2I(W),
\]
and letting \(t\) tend to \(0\) from both sides shows \(B(\widehat J,W)=0\). A second integration by parts on \([a,b]\) gives
\[
\begin{aligned}
&B(\widehat J,W)\\
&\quad=\langle D_sJ(b),W(b)\rangle\\
&\qquad-\langle D_sJ(a),W(a)\rangle .
\end{aligned} \tag{2.2}
\]
Now \(D_sJ(a)\ne0\): otherwise \(J(a)=D_sJ(a)=0\) and \(J=0\) by uniqueness. Let \(P\) be the parallel field with \(P(a)=D_sJ(a)\) and \(\varphi\) a smooth function with \(\varphi(a)=1\) that vanishes outside an interval around \(a\) not containing \(b\). For \(W=\varphi P\), (2.2) gives \(B(\widehat J,W)=-|D_sJ(a)|^2<0\), a contradiction. \(\square\)

The criterion is also necessary: if there are no conjugate points, the index form of every compact segment is positive definite on fields vanishing at its endpoints (Exercise 4.4). We use only the sufficiency.

**Proposition 2.3** (assembly of visits; [OpenAI-NC, Proposition 6.1]). Let \((M,g)\) be complete and \(U\subseteq M\) open, and suppose that every sectional curvature at every point of \(M\setminus U\) is nonpositive. Assume that for every unit-speed geodesic \(\gamma\colon\mathbb R\to M\), every connected component \(J\) of \(\gamma^{-1}(U)\) and every smooth field \(V\) along \(\gamma\) vanishing outside a compact set,
\[
I_J(V)\ge0 . \tag{2.3}
\]
Then \(I(V)\ge0\) for all such \(\gamma\) and \(V\), and therefore \(g\) has no conjugate points.

*Proof.* Put \(i_V(s)=|D_sV|^2-\langle R(V,T)T,V\rangle\). It is continuous and vanishes outside a compact set, hence integrable over \(\mathbb R\). The open set \(\gamma^{-1}(U)\subseteq\mathbb R\) is the disjoint union of its connected components, which are open intervals \(J_j\), countably many because each contains a rational number; its complement \(E\) is closed. By countable additivity of the integral of an integrable function,
\[
\begin{aligned}
I(V)&=\sum_jI_{J_j}(V)+\int_Ei_V(s)\,ds,\\
\sum_j|I_{J_j}(V)|&\le\int_{\mathbb R}|i_V|\,ds<\infty .
\end{aligned}
\]
Each \(I_{J_j}(V)\) is nonnegative by (2.3). For \(s\in E\) the point \(\gamma(s)\) lies outside \(U\), so \(\langle R(V,T)T,V\rangle\le0\) there by (1.1), and \(i_V(s)\ge0\). Hence \(I(V)\ge0\), and Lemma 2.2 applies. \(\square\)

The proof allows infinitely many visits, visits accumulating at a time, a visit equal to all of \(\mathbb R\), and visits with one infinite end; the set \(E\) may have positive measure. The hypothesis (2.3) concerns the restriction of one and the same field to each visit, with whatever values it has at the finite ends of the visit. Any auxiliary changes of the field used to verify (2.3) are made visit by visit and need not fit together, since only the intrinsic integrals \(I_{J_j}(V)\) of the original field are added.

## 3. The theorem and the plan of the course

**Theorem 3.1** ([OpenAI-NC, Theorem 1.1]). There is a closed connected orientable smooth three-manifold \(M\) with a \(C^\infty\) Riemannian metric without conjugate points, such that \(M\) admits no \(C^\infty\) Riemannian metric whose sectional curvature is everywhere at most zero.

The manifold is built from two copies of \(\Sigma\times S^1\), where \(\Sigma\) is a torus with an open disc removed. Write \(h_i\) for the boundary circle of the surface and \(f_i\) for the circle factor in the boundary torus of the \(i\)th copy. The two copies are joined through a collar \([0,1]\times T^2\) so that, in the first homology of the common torus,
\[
h_2=h_1+f_1,\quad f_2=h_1 . \tag{3.1}
\]
The obstruction is stronger than the Riemannian assertion: the fundamental group of \(M\) admits no proper cocompact isometric action on a proper CAT(0) space. It is an instance of Leeb's obstruction for graph manifolds [Leeb, Section 4.1].

The proof has two independent halves.

1. *The topology.* [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md) builds \(M\), checks that it is closed and orientable, and computes enough of its fundamental group: each circle factor commutes with the group of its piece, each surface boundary is a commutator there, the gluing gives (3.1), and the relevant elements have infinite order. [Spaces with the CN inequality](spaces-with-the-cn-inequality.md) develops the geometry of complete geodesic spaces satisfying the inequality of Bruhat and Tits, which includes CAT(0) spaces and Hadamard manifolds. [Axes, shifts and the two-piece obstruction](axes-shifts-and-the-two-piece-obstruction.md) studies isometries of such spaces and proves that, for an action of the fundamental group, (3.1) forces two incompatible orthogonality relations; this excludes metrics of nonpositive curvature.
2. *The metric.* [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md) constructs the metric. Outside the open collar \(U=(0,1)\times T^2\) it is a product of a nonpositively curved surface and a circle. On the collar it is \(dt^2+dx^{\mathsf T}P(t)^{-1}dx\), where \(P\) is a concave path of positive definite matrices. [Neck passages and the index form](neck-passages-and-the-index-form.md) classifies the visits of a geodesic to \(U\) and proves (2.3) for all visits except those that return to the boundary torus they entered through; [Returning passages and the main theorem](returning-passages-and-the-main-theorem.md) proves (2.3) for those, uniformly over all such visits, and concludes with Proposition 2.3.

## 4. Exercises

**4.1.** Let \(J\) be a Jacobi field along a unit-speed geodesic. Show that \(\langle J,T\rangle\) is an affine function of \(s\), and deduce that a Jacobi field vanishing at two times is everywhere orthogonal to \(T\).

**4.2.** On the unit sphere \(S^2\), let \(\gamma\) be a great circle and \(E\) the unit normal parallel field along it. Show that \(J(s)=\sin(s)E(s)\) is a Jacobi field vanishing at \(0\) and \(\pi\), and find an explicit compactly supported field \(W=\varphi E\) with \(I(W)<0\).

**4.3.** Show that if every sectional curvature of \(M\) is nonpositive, then \(I(V)\ge\int|D_sV|^2\,ds\) for every compactly supported field along a unit-speed geodesic, so that Lemma 2.2 gives another proof that there are no conjugate points.

**4.4.** Let \(g\) have no conjugate points and let \(V\) vanish outside \([a,b]\). Using the Morse index theorem ([Jacobi fields, conjugate points and the Morse index theorem](course:DG-FND/jacobi-fields-conjugate-points-and-the-morse-index-theorem), Theorem D.1), show that \(I(V)\ge0\), with equality only for \(V=0\).

**4.5.** Show that a function \(V\) on \(\mathbb R\) with values in \(\mathbb R^n\) that is continuous, vanishes outside a compact interval and is smooth on each interval of a finite subdivision has a square-integrable weak derivative, equal to its piecewise derivative.

## 5. Solutions

**4.1.** Since \(D_sT=0\), \(\frac{d^2}{ds^2}\langle J,T\rangle=\langle D_s^2J,T\rangle\), which equals \(-\langle R(J,T)T,T\rangle=0\) by antisymmetry of \(\langle R(X,Y)Z,W\rangle\) in \(Z,W\). An affine function with two zeros vanishes identically.

**4.2.** The curvature is \(1\), so \(R(J,T)T=J\) for normal \(J\), and \(J''+J=(-\sin s+\sin s)E=0\). For \(W=\varphi E\), \(I(W)=\int(\varphi'^2-\varphi^2)\,ds\). Take \(\varphi(s)=\sin(\pi s/L)\) on \([0,L]\) and \(0\) elsewhere (an \(H^1\) field, which suffices by Lemma 2.1, or smooth it): \(I(W)=\frac L2(\pi^2/L^2-1)<0\) for \(L>\pi\).

**4.3.** By (1.1), \(-\langle R(V,T)T,V\rangle\ge0\) pointwise, so \(I(V)\ge\int|D_sV|^2\ge0\), and Lemma 2.2 applies.

**4.4.** Theorem D.1 there identifies the index of \(I_{[a,b]}\) on fields vanishing at \(a,b\) with the number of conjugate times in \((a,b)\), counted with multiplicity, and its nullity with the multiplicity of \(b\). Both are \(0\), so the form is positive definite on such fields, and \(I(V)=I_{[a,b]}(V)\).

**4.5.** On each interval of the subdivision, \(\int Vw'=-\int V'w\) plus boundary terms for test functions \(w\); the boundary terms of adjacent intervals cancel because \(V\) is continuous, and those at the ends vanish because \(V\) does. The piecewise derivative is bounded with compact support, hence square integrable.

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Theorem 1.1, Proposition 6.1, Lemma 6.2. https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
- [IK] S. Ivanov and V. Kapovitch, *Manifolds without conjugate points and their fundamental groups*, arXiv:1205.4455, Sections 1 and 8. https://arxiv.org/abs/1205.4455
- [BM] K. Burns and V. S. Matveev, *Open problems and questions about geodesics*, arXiv:1308.5417, Section 4.1. https://arxiv.org/abs/1308.5417
- [Leeb] B. Leeb, *3-manifolds with(out) metrics of nonpositive curvature*, arXiv:dg-ga/9410002, Section 4.1. https://arxiv.org/abs/dg-ga/9410002
