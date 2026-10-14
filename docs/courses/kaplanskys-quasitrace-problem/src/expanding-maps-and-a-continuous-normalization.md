# Expanding maps and a continuous normalization

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The algebra of the course is built from maps \(X_1,\dots,X_n\) between Hermitian vector bundles that satisfy
\[
\sum_iX_i^*X_i=I,\qquad\sum_iX_iX_i^*\le\tfrac23\,I .
\]
This lesson proves two lemmas that produce such maps. The first, the *incidence lemma*, shows by a dimension count that generic families of bundle maps *expand* subspaces: the span of the images of every subspace of a given dimension is large. The second, the *normalization lemma*, turns a family that doubles the dimension of every subspace into a family with the two relations above. It minimizes a determinant potential in each fiber; the minimizer is unique, and therefore depends continuously on the point of the base, also when the bundles are not trivial.

- Bundles, bundle maps and the polar part of a map with a lower bound (Section 1).
- The facts on smooth manifolds that are used, as a named hypothesis (Section 2).
- Smooth images of smaller manifolds are null (Lemma 3.1).
- The incidence lemma (Lemma 4.1).
- Two facts of linear algebra (Section 5) and the normalization lemma (Lemma 6.1).

The lesson follows [OpenAI-QT, Sections 2 and 3]. It is independent of [Quasitraces and a uniform additivity defect](quasitraces-and-a-uniform-additivity-defect.md). It uses linear algebra (core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40)), Lebesgue measure on \(\mathbb R^n\) and compactness.

## 1. Bundles and bundle maps

All vector bundles are complex, of finite rank, over a compact Hausdorff space \(Y\), and carry a Hermitian metric: a continuous choice of inner products on the fibers. Around every point there are continuous orthonormal frames (apply the Gram–Schmidt process to a local frame), so locally a bundle of rank \(d\) is \(U\times\mathbb C^d\) with the standard inner product. A *bundle map* \(T\colon E\to F\) is a continuous family of linear maps \(T(y)\colon E_y\to F_y\). Its adjoint \(T^*\) is taken in each fiber; in local orthonormal frames \(T\) is a continuous matrix function and \(T^*\) its conjugate transpose. A bundle map is *positive* if each \(T(y)\) is positive, and \(T\ge c\,I\) means \(T(y)\ge c\,I\) for all \(y\).

A *subbundle* is a family of subspaces that is locally spanned by continuous sections; equivalently, the orthogonal projections onto the subspaces form a bundle map. A bundle is *trivial* if it is isomorphic, with a bundle map that is unitary in each fiber, to \(Y\times\mathbb C^d\).

**Lemma 1.1** (polar part). Let \(W\colon E\to F\) be a bundle map with \(W^*W\ge c\,I\) for a number \(c>0\). Then \(Q=W(W^*W)^{-1/2}\) is a bundle map with \(Q^*Q=I\). Its fiberwise image is a subbundle of \(F\), the image of \(W\), and \(Q\) is a unitary isomorphism from \(E\) onto it.

**Proof.** In local orthonormal frames \(W^*W\) is a continuous function with values in the Hermitian matrices with spectrum in \([c,\|W\|^2]\), and \(t\mapsto t^{-1/2}\) is continuous there; the continuous functional calculus of matrices depends continuously on the matrix. So \(Q\) is continuous, and with \(Z=(W^*W)^{-1/2}\) we get \(Q^*Q=ZW^*WZ=I\). The projection \(QQ^*\) onto the image is continuous, and the image of \(Q\) equals that of \(W\) because \((W^*W)^{-1/2}\) is invertible. \(\blacksquare\)

## 2. Facts on smooth manifolds

The incidence lemma uses smooth structures. The following facts are standard in differential topology and are used without proof.

**Hypothesis (SM).** Let \(Y\) be a compact smooth manifold of real dimension \(2h\), and \(E,F\) smooth Hermitian vector bundles over \(Y\) of ranks \(d,r\).

1. There are finitely many smooth local frames of \(\operatorname{Hom}(E,F)\) over open sets covering \(Y\), and a smooth partition of unity subordinate to this cover.
2. For integers \(1\le s\le d\) and \(0\le t\le r\), the set \(\mathcal G\) of the triples \((y,S,U)\) with \(y\in Y\), \(S\) a complex subspace of \(E_y\) of dimension \(s\) and \(U\) a complex subspace of \(F_y\) of dimension \(t\) is a compact smooth manifold of real dimension
\[
2h+2s(d-s)+2t(r-t) .
\]
Over \(\mathcal G\), the families \(S\), \(F_y\) and \(F_y/U\) form smooth vector bundles, and so does \(\operatorname{Hom}(S,F_y/U)\).
3. If \(\Psi\) is a smooth homomorphism from a smooth vector bundle onto another one over the same manifold, surjective in every fiber, then its kernel is a smooth vector bundle; its total space is a smooth manifold whose dimension is the dimension of the base plus twice the difference of the complex ranks.
4. A smooth manifold is a countable union of compact sets, each contained in the domain of a chart; a smooth map between manifolds, written in charts, is Lipschitz on compact subsets of the chart domains.

These facts are not proved in this course. They are used only in Section 4. For a point in place of \(Y\), with \(h=0\), part 2 concerns pairs of subspaces of \(\mathbb C^d\) and \(\mathbb C^r\); Exercise 7.4 explains the dimension \(2s(d-s)\) of the Grassmannian of \(s\)-dimensional subspaces of \(\mathbb C^d\).

## 3. Smooth images of smaller manifolds

**Lemma 3.1.** Let \(Z\) be a smooth manifold of real dimension \(a\), and \(f\colon Z\to\mathbb R^n\) a smooth map with \(a<n\). Then \(f(Z)\) has Lebesgue measure \(0\).

**Proof.** By part 4 of (SM) it suffices to treat the image of a compact set \(K\) contained in a chart domain, on which \(f\), written in the chart, is \(\Lambda\)-Lipschitz. In the chart, \(K\) lies in a closed cube of side \(\ell\) in \(\mathbb R^a\). Divide the cube into \(k^a\) cubes of side \(\ell/k\). The part of \(K\) in each small cube has diameter at most \(\sqrt a\,\ell/k\), so its image lies in a ball of radius \(\Lambda\sqrt a\,\ell/k\). The total volume of these balls is at most a constant times \(k^a\cdot k^{-n}\), which tends to \(0\) as \(k\to\infty\). A countable union of null sets is null. \(\blacksquare\)

## 4. The incidence lemma

For subspaces we write \(\sum_iT_iS\) for the span of the images \(T_i(S)\).

**Lemma 4.1** (incidence; [OpenAI-QT, Section 3]). Assume (SM). Let \(E,F\) be smooth Hermitian vector bundles of ranks \(d,r\) over a compact smooth manifold \(Y\) of real dimension \(2h\), let \(q\ge1\), and let \(\mathcal A\) be a finite set of pairs of integers \((s,t)\) with \(1\le s\le d\), \(0\le t\le r\), such that every pair in \(\mathcal A\) satisfies
\[
(qs-t)(r-t)-s(d-s)>h .
\]
Then there are smooth bundle maps \(T_1,\dots,T_q\colon E\to F\) such that for every \(y\in Y\), every \((s,t)\in\mathcal A\) and every subspace \(S\subseteq E_y\) of dimension \(s\),
\[
\dim\sum_{i=1}^qT_i(y)S>t .
\]
The same holds over a point, with \(h=0\).

**Proof.** *A space of maps.* Multiply each section of the finitely many local frames of \(\operatorname{Hom}(E,F)\) of part 1 of (SM) by the corresponding function of the partition of unity, and extend it by zero. The complex span \(V\) of these finitely many smooth bundle maps has finite dimension, and at every point \(y\) the evaluation \(V\to\operatorname{Hom}(E_y,F_y)\) is onto: some function of the partition of unity is nonzero at \(y\), and the multiplied frame still spans the fiber. Let \(\mathcal V=V^q\), the space of \(q\)-tuples, of complex dimension \(M\).

*The bad tuples for one pair.* Fix \((s,t)\in\mathcal A\) and let \(\mathcal G\) be the manifold of part 2 of (SM). Over \(\mathcal G\) consider the homomorphism from the trivial bundle with fiber \(\mathcal V\) to the bundle with fiber \(\operatorname{Hom}(S,F_y/U)^q\) that maps a tuple \((T_i)\) to the restrictions of the \(T_i(y)\) to \(S\), followed by the quotient map \(F_y\to F_y/U\). It is onto in every fiber: a linear map from \(S\) to \(F_y/U\) lifts to \(F_y\), extends from \(S\) to \(E_y\), and is the evaluation of an element of \(V\). The target has complex rank \(qs(r-t)\). By part 3 of (SM) the kernel is a smooth manifold \(\mathcal I\) of real dimension
\[
\begin{aligned}
&2M+2h+2s(d-s)\\
&\quad+2t(r-t)-2qs(r-t) ,
\end{aligned}
\]
which is less than \(2M\) by the assumption on \((s,t)\). The projection of \(\mathcal I\) to \(\mathcal V\) is smooth. Its image consists of the tuples for which some \(s\)-dimensional \(S\subseteq E_y\) has all images \(T_i(y)S\) inside some \(t\)-dimensional \(U\subseteq F_y\). By Lemma 3.1, applied with \(\mathcal V\cong\mathbb R^{2M}\), this image is a null set.

*Conclusion.* The finitely many null sets for the pairs in \(\mathcal A\) do not cover \(\mathcal V\). Take a tuple \((T_i)\) outside all of them. If for some \(y\), \((s,t)\in\mathcal A\) and \(S\) the span \(\sum_iT_i(y)S\) had dimension at most \(t\), it would lie in a subspace \(U\) of dimension exactly \(t\), since \(t\le r\); the tuple would be in the bad set. \(\blacksquare\)

The inequality of the lemma compares two dimensions. The family of the configurations \((y,S,U)\) has complex dimension \(h+s(d-s)+t(r-t)\). For a fixed configuration, the condition "all \(T_i(y)S\) lie in \(U\)" imposes \(qs(r-t)\) linear conditions on the tuple. If the conditions outnumber the configurations, a generic tuple satisfies the condition for no configuration.

## 5. Two facts of linear algebra

For a Hermitian matrix \(A\) of size \(n\) let \(\mu_1(A)\ge\dots\ge\mu_n(A)\) be its eigenvalues.

**Lemma 5.1** (min-max). \(\mu_k(A)\) is the largest number \(\mu\) for which there is a subspace \(V\) of dimension \(k\) with \(\langle Av,v\rangle\ge\mu\|v\|^2\) for all \(v\in V\). Consequently, if \(A\le B\), then \(\mu_k(A)\le\mu_k(B)\) for all \(k\); and \(|\mu_k(A)-\mu_k(B)|\le\|A-B\|\).

**Proof.** Let \(e_1,\dots,e_n\) be orthonormal eigenvectors with \(Ae_j=\mu_j(A)e_j\). The span of \(e_1,\dots,e_k\) has the property with \(\mu=\mu_k(A)\). Conversely, a subspace \(V\) of dimension \(k\) meets the span of \(e_k,\dots,e_n\), of dimension \(n-k+1\), in a unit vector \(v\), and \(\langle Av,v\rangle\le\mu_k(A)\). If \(A\le B\), every subspace that works for \(A\) and \(\mu\) works for \(B\) and \(\mu\). Finally \(A\le B+\|A-B\|\,I\), and the eigenvalues of \(B+c\,I\) are those of \(B\) plus \(c\). \(\blacksquare\)

**Lemma 5.2** (determinant expansion). Let \(C\) be a complex \(n\times N\) matrix with columns \(c_1,\dots,c_N\). Then
\[
\det(I_n+CC^*)=\sum_{J\subseteq\{1,\dots,N\}}\gamma_J ,
\]
where \(\gamma_J\ge0\) is the Gram determinant \(\det(\langle c_k,c_j\rangle)_{j,k\in J}\), and \(\gamma_\emptyset=1\).

**Proof.** \(\det(I_n+CC^*)=\det(I_N+C^*C)\) (Sylvester's identity, from the two factorizations of the block matrix with blocks \(I_n\), \(-C\), \(C^*\), \(I_N\)). Write the columns of \(I_N+G\), \(G=C^*C\), as \(e_j+g_j\) and expand the determinant by multilinearity in the columns: the term in which the columns with index in \(J\) are taken from \(G\) and the others from \(I_N\) is the principal minor \(\det(G_{JJ})\). The matrix \(G_{JJ}\) is the Gram matrix of the \(c_j\), \(j\in J\), which is positive. \(\blacksquare\)

## 6. The normalization lemma

**Lemma 6.1** (normalization; [OpenAI-QT, Section 3]). Let \(E,F\) be Hermitian vector bundles of positive ranks \(d,r\) over a compact Hausdorff space \(Y\), and let \(T_1,\dots,T_n\colon E\to F\) be bundle maps such that for all \(y\in Y\) and all subspaces \(S\subseteq E_y\)
\[
\dim\sum_{i=1}^nT_i(y)S\ge2\dim S .
\]
Then there are bundle maps \(X_1,\dots,X_n\colon E\to F\) with
\[
\sum_{i=1}^nX_i^*X_i=I_E,\qquad\sum_{i=1}^nX_iX_i^*\le\tfrac23\,I_F .
\]

**Proof.** For \(y\in Y\) and positive definite \(P\) on \(E_y\) put
\[
\begin{aligned}
D_y(P)&=\sum_iT_i(y)\,P\,T_i(y)^*,\\
g_y(P)&=\log\det\bigl(I+D_y(P)\bigr)\\
&\quad-\tfrac32\log\det P .
\end{aligned}
\]
Both determinants are taken on the fibers and do not depend on frames.

*Step 1: a uniform estimate.* For an orthogonal projection \(p\) of rank \(s\) on \(E_y\), the range of \(D_y(p)=\sum_i(T_ip)(T_ip)^*\) is \(\sum_iT_i(y)\operatorname{ran}p\), which has dimension at least \(2s\). So \(\mu_{2s}(D_y(p))>0\); in particular \(r\ge2d\). The pairs \((y,p)\) with \(p\) of rank \(s\) form a compact set (in local orthonormal frames, a finite union of compact sets of the form \(K\times\{\text{projections of rank }s\}\)), and \(\mu_{2s}\) is continuous by Lemma 5.1. So there is \(\varepsilon>0\) with \(\mu_{2s}(D_y(p))\ge\varepsilon\) for all \(y\), all \(1\le s\le d\) and all projections \(p\) of rank \(s\).

Let \(P\) have the eigenvalues \(\lambda_1\ge\dots\ge\lambda_d>0\), and let \(p_s\) be the projection onto eigenvectors of the \(s\) largest ones. Then \(P\ge\lambda_sp_s\), so \(D_y(P)\ge\lambda_sD_y(p_s)\) and, by Lemma 5.1, \(\mu_{2s}(D_y(P))\ge\varepsilon\lambda_s\). Since \(\mu_{2s-1}\ge\mu_{2s}\),
\[
\begin{aligned}
&\log\det(I+D_y(P))\\
&\quad\ge\sum_{s=1}^d\log\bigl((1+\mu_{2s-1})(1+\mu_{2s})\bigr)\\
&\quad\ge2\sum_{s=1}^d\log(1+\varepsilon\lambda_s) .
\end{aligned}
\]

*Step 2: compact sublevel sets.* Let \(f(\lambda)=2\log(1+\varepsilon\lambda)-\tfrac32\log\lambda\) for \(\lambda>0\). It tends to \(+\infty\) at \(0\) and at \(\infty\), so it has a minimum \(\beta\). By Step 1, \(g_y(P)\ge\sum_sf(\lambda_s)\). Let \(\Gamma\) be the maximum of \(g_y(I)\) over \(y\) (a continuous function on a compact space). If \(g_y(P)\le\Gamma\), then \(f(\lambda_j)\le\Gamma-(d-1)\beta\) for every \(j\). So there are \(0<\alpha\le\alpha'\) with \(\alpha\le\lambda_j\le\alpha'\) for all eigenvalues of every such \(P\), for all \(y\). On the compact set \(\alpha I\le P\le\alpha'I\), \(g_y\) has a minimum, and outside it \(g_y>\Gamma\ge g_y(I)\). So \(g_y\) has a global minimizer, with \(\alpha I\le P\le\alpha'I\).

*Step 3: strict convexity and uniqueness.* Let \(P_0>0\) and \(H\ne0\) Hermitian on \(E_y\), and \(P(u)=P_0^{1/2}e^{uH}P_0^{1/2}\) for \(u\in\mathbb R\). Let \(e_1,\dots,e_d\) be orthonormal eigenvectors of \(H\) with eigenvalues \(h_j\), and \(c_{ij}=T_i(y)P_0^{1/2}e_j\). Then
\[
D_y(P(u))=\sum_{i,j}e^{uh_j}c_{ij}c_{ij}^* .
\]
By Lemma 5.2 applied to the columns \(e^{uh_j/2}c_{ij}\), \(\det(I+D_y(P(u)))\) is a finite sum \(\sum_\alpha w_\alpha e^{u\alpha}\) with coefficients \(w_\alpha\ge0\): a set \(J\) of pairs \((i,j)\) contributes its Gram determinant at the exponent \(\sum_{(i,j)\in J}h_j\). The empty set contributes \(1\) at the exponent \(0\). For each \(j\) the singletons contribute \(\sum_i\|c_{ij}\|^2>0\) at the exponent \(h_j\); this is positive because the maps \(T_i(y)\) have no common nonzero kernel vector (apply the hypothesis to the line spanned by \(P_0^{1/2}e_j\)). Since \(H\ne0\), some \(h_j\ne0\), so at least two different exponents have positive coefficients. The second derivative of \(\log\sum_\alpha w_\alpha e^{u\alpha}\) is the variance of the exponents \(\alpha\) under the weights proportional to \(w_\alpha e^{u\alpha}\), which is positive. Further \(\log\det P(u)=\log\det P_0+u\operatorname{tr}H\) is affine in \(u\). So \(u\mapsto g_y(P(u))\) is strictly convex. Two different positive definite \(P_0,P_1\) lie on such a curve, with \(H=\log(P_0^{-1/2}P_1P_0^{-1/2})\ne0\) and \(u\in\{0,1\}\). A strictly convex function on \([0,1]\) cannot take its minimum at both ends, so the minimizer \(P_y\) of \(g_y\) is unique.

*Step 4: continuity.* In local orthonormal frames over an open set \(U\), \((y,P)\mapsto g_y(P)\) is continuous. Let \((y_k)\) be a net in \(U\) converging to \(y\in U\). The minimizers \(P_{y_k}\) lie in the compact set \(\alpha I\le P\le\alpha'I\), so every subnet has a further subnet that converges, to \(P'\) say. Passing to the limit in \(g_{y_k}(P_{y_k})\le g_{y_k}(P)\) along it gives \(g_y(P')\le g_y(P)\) for every \(P\), so \(P'=P_y\) by uniqueness. A net of which every subnet has a further subnet converging to \(P_y\) converges to \(P_y\); so \(y\mapsto P_y\) is continuous in the frame. A change of orthonormal frames conjugates \(P\) and \(I+D_y(P)\) by unitaries and does not change \(g_y\). So the minimizers do not depend on the frames and form a continuous positive bundle map \(P\) of \(E\).

*Step 5: the normalization.* Let \(Q=I+D(P)\). At the minimizer the derivative of \(g_y\) in every Hermitian direction \(K\) vanishes. Since the derivative of \(\log\det\) at an invertible \(Z\) in the direction \(Z'\) is \(\operatorname{tr}(Z^{-1}Z')\),
\[
0=\operatorname{tr}\Bigl(\Bigl(\sum_iT_i^*Q^{-1}T_i-\tfrac32P^{-1}\Bigr)K\Bigr)
\]
for all Hermitian \(K\). The trace pairing of Hermitian matrices is nondegenerate, so \(\sum_iT_i^*Q^{-1}T_i=\tfrac32P^{-1}\). Put
\[
X_i=\sqrt{\tfrac23}\,Q^{-1/2}\,T_i\,P^{1/2} .
\]
These are bundle maps, continuous by the functional calculus, and
\[
\begin{aligned}
\sum_iX_i^*X_i&=\tfrac23\,P^{1/2}\Bigl(\sum_iT_i^*Q^{-1}T_i\Bigr)P^{1/2}\\
&=\tfrac23\,P^{1/2}\bigl(\tfrac32P^{-1}\bigr)P^{1/2}=I,\\
\sum_iX_iX_i^*&=\tfrac23\,Q^{-1/2}D(P)\,Q^{-1/2}\\
&=\tfrac23\bigl(I-Q^{-1}\bigr)\le\tfrac23\,I .
\end{aligned}
\]
\(\blacksquare\)

The factor \(2\) in the hypothesis and the coefficient \(\tfrac32\) in \(g\) are related: in Step 1 the determinant grows like \(\lambda^2\) in each eigenvalue \(\lambda\) of \(P\), and \(\det P^{3/2}\) like \(\lambda^{3/2}\); the margin \(2>\tfrac32\) makes the sublevel sets compact. The coefficient \(\tfrac32\) becomes the bound \(\tfrac23\) in the end.

**Remark 6.2** (other bounds). The proof uses the coefficient \(\tfrac32\) only through \(0<\tfrac32<2\). Let \(0<\theta<2\) and replace \(\tfrac32\log\det P\) by \(\theta\log\det P\) in \(g_y\). In Step 2 the function \(2\log(1+\varepsilon\lambda)-\theta\log\lambda\) still tends to \(+\infty\) at \(0\) and at \(\infty\); Step 3 is unchanged, because \(\theta\log\det P(u)\) is affine in \(u\); and Step 5 gives \(\sum_iT_i^*Q^{-1}T_i=\theta P^{-1}\). With \(X_i=\theta^{-1/2}Q^{-1/2}T_iP^{1/2}\),
\[
\begin{gathered}
\sum_iX_i^*X_i=I,\\
\sum_iX_iX_i^*=\theta^{-1}\bigl(I-Q^{-1}\bigr)\le\theta^{-1}I .
\end{gathered}
\]
So for every \(c>\tfrac12\) there are maps with \(\sum_iX_i^*X_i=I\) and \(\sum_iX_iX_i^*\le c\,I\).

## 7. Exercises

**7.1.** Show that a single map (\(n=1\)) can never satisfy \(X^*X=I\) and \(XX^*\le\tfrac23I\).

**7.2.** Over a point, show that the two relations of Lemma 6.1 force \(r\ge\tfrac32d\), and that the hypothesis of Lemma 6.1 forces \(r\ge2d\).

**7.3.** Over a point, let \(d=1\), \(r=2\), \(n=2\) and \(T_1=e_1\), \(T_2=e_2\) as maps \(\mathbb C\to\mathbb C^2\). Compute the minimizer of \(g\) and the maps \(X_1,X_2\).

**7.4.** Show that the subspaces \(S\) of \(\mathbb C^d\) of dimension \(s\) that meet \(\{0\}\times\mathbb C^{d-s}\) only in \(0\) are exactly the graphs of the linear maps \(\mathbb C^s\to\mathbb C^{d-s}\), and conclude that the Grassmannian of these subspaces has complex dimension \(s(d-s)\) near such an \(S\).

**7.5.** In the proof of Lemma 4.1, why does the space \(V\) have to be built from several local frames, rather than from global frames of \(\operatorname{Hom}(E,F)\)?

## 8. Solutions

**7.1.** \(X^*X=I\) makes \(XX^*\) a projection, as in Exercise 7.3 of [Quasitraces and a uniform additivity defect](quasitraces-and-a-uniform-additivity-defect.md). It is not zero, since \(X^*(XX^*)X=I\), so its norm is \(1\), and \(XX^*\le\tfrac23I\) fails.

**7.2.** Taking traces, \(d=\operatorname{tr}\sum X_i^*X_i=\operatorname{tr}\sum X_iX_i^*\le\tfrac23r\). For the second statement apply the hypothesis to \(S=E_y\): the span lies in \(F_y\), of dimension \(r\).

**7.3.** \(P=\lambda>0\) and \(D(P)=\lambda I_2\), so \(g=2\log(1+\lambda)-\tfrac32\log\lambda\), with derivative \(\frac2{1+\lambda}-\frac3{2\lambda}\), which vanishes at \(\lambda=3\). Then \(Q=4I_2\) and \(X_i=\sqrt{2/3}\cdot\tfrac12\cdot\sqrt3\,e_i=e_i/\sqrt2\). Indeed \(\sum X_i^*X_i=\tfrac12+\tfrac12=1\) and \(\sum X_iX_i^*=\tfrac12I_2=\tfrac23(I-Q^{-1})\).

**7.4.** If \(S\cap(\{0\}\times\mathbb C^{d-s})=0\), the projection of \(S\) to the first \(s\) coordinates is injective, hence an isomorphism onto \(\mathbb C^s\), and \(S\) is the graph of the linear map that sends the first coordinates of a vector of \(S\) to its last ones. Conversely a graph meets \(\{0\}\times\mathbb C^{d-s}\) only in \(0\). The linear maps form \(\mathbb C^{s(d-s)}\), and every \(S\) is of this form after a permutation of the coordinates.

**7.5.** A nontrivial bundle has no global frame. The local frames, cut off by the partition of unity, give finitely many global smooth bundle maps whose values span every fiber.

## References

- [OpenAI-QT] OpenAI, *A counterexample to Kaplansky's quasitrace conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026
