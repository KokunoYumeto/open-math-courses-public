# Measurable change of variables and finite-sheeted integration

*Written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, 11 October 2026. Original exposition: CC0-1.0. No separate review of this proof is recorded.*

The conjugation map in Weyl integration is locally invertible away from the singular set. Its integration formula needs substitution for nonnegative measurable functions, not just continuous functions on a box. We prove that version here, including the passage to manifold densities and finite coverings.

## Exact preceding proofs

- [Measure and Hilbert space tools for Haar integration](courses/harmonic-analysis-on-locally-compact-groups/measure-and-hilbert-space-tools.html): Section 1 constructs one-dimensional Lebesgue measure and proves its Radon properties; Theorem 2.1 proves monotone convergence; Lemma 6.1 in Section 6 proves one-variable substitution and identifies continuous Riemann and Lebesgue integrals.
- [Haar measure on locally compact groups](courses/harmonic-analysis-on-locally-compact-groups/haar-measure-on-locally-compact-groups.html): Theorem 2.2 proves uniqueness of a Radon measure from its integrals on continuous compactly supported functions; Proposition 3.1 proves transport by homeomorphisms and multiplication by positive continuous densities; Sections 4–5 construct Radon products and prove Tonelli and Fubini, in particular Theorem 5.1(4), (5), (7).
- Local tools for bundles and transport: Section 0 proves the real, linear and differential foundations; Theorem 1.2 proves the smooth inverse function theorem. The part of its proof before the higher-derivative induction establishes the continuously differentiable version used below.

All three readings are included in this selected course. No multidimensional substitution or area formula is assumed in them for the results just listed. Define \(\lambda_n\) to be the iterated Radon product of one-dimensional Lebesgue measure. Bounded boxes have their usual product volume by the rectangle theorem, and cover \(\mathbb R^n\) countably. Thus these measures are sigma-finite. The Borel sigma-algebra of a Euclidean product is its product sigma-algebra by Theorem 5.1(7), so Tonelli applies to every nonnegative Borel function used below. Restrictions to open sets use zero extension. We first work with Borel measures; completed measures are treated explicitly in Section 5. In dimension zero, a point has measure one and the empty determinant is one.

## 1. Substitution on an interval

**Lemma CV.1.** Let \(g:I\to J\) be a \(C^1\) diffeomorphism of nonempty open intervals. For every Borel \(h:J\to[0,\infty]\),
\[
\int_J h(y)\,d\lambda_1(y)
=\int_I h(g(t))|g'(t)|\,d\lambda_1(t).
\tag{CV.1}
\]

*Proof.* The chain rule for \(g^{-1}g\) gives \(g'(t)\ne0\). Continuity and the intermediate value theorem make its sign constant, and the mean value theorem makes \(g\) strictly monotone. If \(h\in C_c(J)\), its support and its inverse image are compact. Choose \(a<b\) in \(I\) whose interior contains that inverse image. Lemma 6.1 of the measure-tools reading gives
\(\int_{g(a)}^{g(b)}h=\int_a^b(h\circ g)g'\).
If \(g\) decreases, reversing the endpoints replaces \(g'\) by \(|g'|\); if it increases, no reversal is needed. Both integrands vanish outside the corresponding compact intervals. This proves (CV.1) for continuous compactly supported \(h\).

The measure \(|g'|\lambda_1\) on \(I\) is Radon by the positive-density assertion of Proposition 3.1. Its image \(g_*(|g'|\lambda_1)\) is Radon by the homeomorphism assertion there. The two Radon measures on \(J\) have the same integrals on \(C_c(J)\), so Theorem 2.2 makes them equal. Their equality first gives (CV.1) for indicators, then for nonnegative simple functions by additivity, then for arbitrary nonnegative Borel functions by monotone convergence. Infinite integrals are allowed. ∎

## 2. Changing a single coordinate

**Lemma CV.2.** Suppose \(S:V\to W\) is a \(C^1\) diffeomorphism between open subsets of \(\mathbb R^n\), and changes only coordinate \(k\). Write the other coordinates as \(z\) and that coordinate as \(t\); thus
\[
S(z,t)=(z,s(z,t)).
\]
For every nonnegative Borel \(h\) on \(W\),
\[
\int_W h(y)\,d\lambda_n(y)
=\int_V h(S(x))|\det DS(x)|\,d\lambda_n(x).
\tag{CV.2}
\]

*Proof.* The Jacobian matrix is the identity except for row \(k\). Expansion in that row gives \(\det DS=\partial_t s\), which is nonzero. For fixed \(z\), the open slice \(V_z\subseteq\mathbb R\) is a countable disjoint union of open intervals: each component is an interval, and distinct components contain distinct rational numbers. The same holds for \(W_z\). The map \(t\mapsto s(z,t)\) is a homeomorphism from \(V_z\) onto \(W_z\), since \(S\) and \(S^{-1}\) preserve the other coordinates. It therefore maps components bijectively onto components. Its restriction to each interval is a \(C^1\) diffeomorphism. Apply Lemma CV.1 and sum over those intervals by nonnegative countable additivity. This proves equality of the two slice integrals, including empty slices and infinite values.

The functions \(1_W h\) and \(1_V(h\circ S)|\partial_t s|\), extended by zero, are Borel. Tonelli identifies their total integrals with their slice integrals and proves (CV.2). Listing coordinate \(k\) last is legitimate because the two orders of iterated integration agree by the same Tonelli theorem; it is not an assumption of multidimensional substitution. For \(n=1\) there is no outer slice integral. ∎

**Lemma CV.3.** For an invertible real matrix \(A\) and \(b\in\mathbb R^n\), the affine map \(L(x)=Ax+b\) satisfies (CV.2), with \(|\det A|\) as its Jacobian.

*Proof.* A translation of one coordinate, a nonzero scaling of one coordinate, or addition of a multiple of a different coordinate to one coordinate is covered by Lemma CV.2. Its absolute determinant is respectively \(1\), the absolute value of the scale, or \(1\). Interchanging two coordinates preserves the integral by Tonelli and has absolute determinant one.

Gaussian elimination expresses every invertible matrix as a product of these elementary matrices. Indeed, its first column has a nonzero entry; interchange rows to put it first, scale the pivot to one, and subtract multiples of that row to clear the entries below it. The remaining lower-right block is invertible, since a nonzero vector in its kernel would give a vector in the kernel of the full matrix after solving the first coordinate. Induction reduces that block; clearing the remaining first-row entries finishes the reduction to the identity. Reversing the elementary operations gives the claimed factorization. Translations are products of coordinate translations.

Substitution is stable under composition. If it holds for \(P\) and \(Q\), apply the formula for \(P\) to the nonnegative function \((h\circ Q)|\det DQ|\), and the formula for \(Q\) to \(h\). The chain rule and multiplicativity of determinants identify the product of Jacobians with \(|\det D(QP)|\). Determinant multiplicativity follows directly from multilinearity and alternation in the columns: for fixed \(A\), the function \(B\mapsto\det(AB)\) is alternating multilinear in the columns of \(B\), hence equals its value at the identity, \(\det A\), times \(\det B\). This proves the affine formula. Restriction to an open subset follows by applying the whole-space formula to \(h\) extended by zero on the complement of that subset's image. ∎

## 3. A general local diffeomorphism

**Lemma CV.4.** If \(F:U\to V\) is a \(C^1\) diffeomorphism of open subsets of \(\mathbb R^n\), every point of \(U\) has an open neighbourhood \(O\) such that
\[
\int_{F(O)}h(y)\,d\lambda_n(y)
=\int_O h(F(x))|\det DF(x)|\,d\lambda_n(x)
\tag{CV.3}
\]
for all nonnegative Borel \(h\) on \(F(O)\).

*Proof.* Fix \(a\in U\), let \(A=DF(a)\), and set
\[
H(x)=a+A^{-1}(F(x)-F(a)),\qquad
P_k(x)=(H_1(x),\ldots,H_k(x),x_{k+1},\ldots,x_n).
\]
Here \(H_i\) denotes the \(i\)-th scalar component of \(H\), whereas \(P_k:U\to\mathbb R^n\) is the displayed partial-coordinate map. Set \(P_0(x)=x\), so \(P_n=H\). Because \(DH(a)=I\), every \(DP_k(a)=I\). The continuously differentiable part of the inverse-function proof gives a neighbourhood on which each \(P_k\) is a \(C^1\) diffeomorphism onto its open image. More precisely, that proof uses continuity of \(Df\) to make \(x\mapsto x-f(x)\) a contraction after affine normalization. Its fixed-point argument constructs a Lipschitz local inverse \(g\); the first-order remainder then gives \(Dg=(Df\circ g)^{-1}\), a continuous derivative. These steps require only \(C^1\), not the subsequent induction proving smoothness. Intersect the finitely many resulting neighbourhoods to obtain a common \(O\). A restriction of a diffeomorphism to an open subset is still a diffeomorphism onto its image.

The maps
\[
S_k=P_k\circ P_{k-1}^{-1}:P_{k-1}(O)\longrightarrow P_k(O)
\]
change only coordinate \(k\): the first \(k-1\) coordinates are already those of \(H\), and the coordinates after \(k\) are still those of \(x\). Lemma CV.2 applies to every \(S_k\). Their composition is \(H|_O\), so the composition calculation in Lemma CV.3 gives substitution for \(H|_O\). Finally
\(F(x)=F(a)+A(H(x)-a)\).
Apply the affine case and that composition calculation once more. The resulting determinant is exactly \(|\det DF(x)|\), proving (CV.3). No global triangular form of \(F\), and no positivity of its determinant, has been assumed. ∎

## 4. Global measurable substitution

**Theorem CV.5.** For every \(C^1\) diffeomorphism \(F:U\to V\) of open subsets of \(\mathbb R^n\), and every nonnegative Borel \(h:V\to[0,\infty]\),
\[
\int_Vh\,d\lambda_n
=\int_U(h\circ F)|\det DF|\,d\lambda_n.
\tag{CV.4}
\]
The same identity holds for a complex Borel \(h\) whenever either side for \(|h|\) is finite; finiteness on the other side then follows as well.

*Proof.* The neighbourhoods of Lemma CV.4 have a countable subcover \(O_1,O_2,\ldots\) of \(U\). To see this, use rational-centre rational-radius balls as a countable basis, and for every basic ball contained in a member of the cover choose one such member. These chosen members cover every point. Put
\[
E_1=O_1,\qquad E_j=O_j\setminus\bigcup_{i<j}O_i\quad(j>1).
\]
These Borel sets partition \(U\). Their images are Borel, since \(F\) is a homeomorphism, and they partition \(V\). Apply the local formula on \(O_j\) to \(h1_{F(E_j)}\), and sum. Monotone convergence for the partial sums proves (CV.4), even when its value is infinite. Apply this first to \(|h|\), and then to the positive and negative parts of its real and imaginary parts, to obtain the complex assertion without any undefined subtraction. The zero-dimensional and empty-domain cases are immediate. ∎

## 5. Completion, densities and manifolds

**Corollary CV.6.** Theorem CV.5 also holds for Lebesgue-measurable functions with respect to the completed measures. If \(M,N\) are second-countable \(n\)-dimensional \(C^1\) manifolds with positive continuous densities \(\mu_M,\mu_N\), and \(F:M\to N\) is a \(C^1\) diffeomorphism, then
\[
\int_N h\,d\mu_N=\int_M (h\circ F)J_F\,d\mu_M
\tag{CV.5}
\]
for nonnegative measurable \(h\), or for integrable complex \(h\). In coordinates where the density functions are \(r_M(x)>0\), \(r_N(y)>0\),
\[
J_F(x)=\frac{r_N(F(x))|\det DF(x)|}{r_M(x)}.
\tag{CV.6}
\]
For Riemannian densities, \(r=\sqrt{\det(g_{ij})}\), so this is the absolute determinant between orthonormal tangent frames. No orientation is required.

*Proof.* If \(B\subseteq V\) is Borel and null, apply Theorem CV.5 to \(1_B\). Its inverse image has zero integral against the strictly positive continuous function \(|\det DF|\), hence is Lebesgue-null: intersect it with the sets \(\{|\det DF|\geq1/m\}\), on each of which ordinary measure is at most \(m\) times the weighted integral, and take their union. Apply the theorem to \(F^{-1}\) as well to see that null Borel sets have null Borel images. A subset of such a null set therefore also has a null image or inverse image in the completed measures.

Every completed-measurable nonnegative function agrees with a Borel function off a Borel null set. For completeness, form its increasing dyadic simple approximants. Each of their finitely many level sets differs from a Borel set by a subset of a Borel null set, by the definition of completion. Replace those level sets by Borel sets and take the limsup of the resulting Borel simple functions. Off the countable union of the exceptional Borel null sets it is the original function. Apply Theorem CV.5 to that representative and use the null-set transport just proved. Treat complex functions by real and imaginary parts.

For densities in Euclidean charts, apply Theorem CV.5 to \(hr_N\), and divide the source density by the strictly positive \(r_M\), obtaining (CV.6). Densities in overlapping charts transform by exactly this absolute-determinant rule; Theorem CV.5 therefore makes their local integrals agree. The Riemannian transformation law follows from
\(g_x=(D y/D x)^Tg_y(D y/D x)\)
and the determinant identity. Thus the density measures are well defined, and (CV.6) is independent of charts. One can construct the global measure with any countable chart cover partitioned into Borel pieces as in Theorem CV.5; agreement on overlaps shows that this construction restricts to the prescribed measure on every chart and is independent of the partition.

Cover \(M\) by countably many open sets on which both the source and target have coordinates and \(F\) has a coordinate expression. Partition this cover into disjoint Borel pieces. The local density formula, applied to the indicator of each image piece, sums to (CV.5). This also proves the completed-measure and complex cases on manifolds, using countably many chartwise null sets. ∎

## 6. Counting sheets, not assuming their contribution

**Corollary CV.7.** Let \(p:M\to N\) be a \(C^1\) local diffeomorphism which is a covering with exactly \(d<\infty\) points in every fibre. Give \(M,N\) positive continuous densities as above. Then
\[
\int_M(h\circ p)J_p\,d\mu_M=d\int_Nh\,d\mu_N
\tag{CV.7}
\]
for all nonnegative measurable \(h\), and for all integrable complex \(h\).

*Proof.* Choose a countable cover of \(N\) by evenly covered open sets, and partition it into Borel sets \(E_j\), each contained in its corresponding open set. Over that open set the map has exactly \(d\) disjoint inverse sheets, each a diffeomorphism onto the open set. Apply Corollary CV.6 on each sheet to \(h1_{E_j}\). Summing the \(d\) equal target integrals gives \(d\int_{E_j}h\). Sum over \(j\) by monotone convergence. The inverse images of the \(E_j\) are disjoint and cover \(M\), so this is (CV.7). Applying it to \(|h|\) justifies the complex case. Null-set representatives are legitimate on all the sheets by Corollary CV.6. ∎

In [the Weyl integration lesson](courses/representations-of-compact-groups/the-weyl-integration-formula.html#result-theorem-3-1), take \(M=G/T\times T_{\mathrm{reg}}\), \(N=G_{\mathrm{reg}}\), and \(p(gT,t)=gtg^{-1}\). That lesson's Lemma 2.1 proves the covering and \(d=|W|\); Lemma 1.4 computes the absolute Jacobian; its volume identity (1.2) fixes the normalization. Corollary CV.7 supplies the precise measurable integration step. It does not assume a connected full centralizer, and it does not discard the singular-set argument needed to return to the whole group.
