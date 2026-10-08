# Why complex Fourier weights need a construction

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

The closing notes of Hörmander's Chapter15 explain why the complex weights were constructed, which broader settings motivate the method, and why the chapter proves the scalar constant-coefficient case. We give the exact negative-curvature calculation and topology comparison, and identify the limits of the current theorems. These are treatments of the three source notes, not assertions that their externally referenced theories have been proved here.

The human source is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, printed pp.300–301. The approved current-edition native pages313–314 were read privately. The mathematical providers are the full [L149 four-condition compact-weight construction](../../AN02-L149.html#complete-proof), [L153 smooth-test neighborhood construction](../../AN02-L153.html#tp5-a-single-strict-psh-weighted-neighborhood), [L144 weighted Cauchy–Riemann proof](../../AN02-L144.html#complete-proof), and [L155 arbitrary-distribution representations](../../AN02-L155.html#ar3-the-full-characteristic-surface-formula). None of the protected source body or source images is included.

## NW1. The naive support weight has actual negative curvature

In one complex dimension, put \(z=\xi+i\eta\), \(r=|z|\), and take the full-dimensional compact real interval \(K=[-R,R]\), \(R>0\). Its support function is \(H_K(\eta)=R|\eta|\). For \(\kappa>0\), consider the exact naive expression
\[
\psi(z)=H_K(\eta)-\kappa\log(1+|z|).
\tag{NW1}
\]
On either open half-plane \(\eta>0\) or \(\eta<0\), the support function is affine and has zero ordinary Laplacian. There \(r>0\), so the real radial Laplacian gives
\[
\Delta\log(1+r)
=-\frac1{(1+r)^2}+\frac1{r(1+r)}
=\frac1{r(1+r)^2}.
\tag{NW2}
\]
With \(\partial_z=(\partial_\xi-i\partial_\eta)/2\), the one-dimensional Levi coefficient is one quarter of the Laplacian. Consequently
\[
\partial_z\partial_{\bar z}\psi
=-\frac{\kappa}{4r(1+r)^2}<0
\quad(\eta\ne0).
\tag{NW3}
\]
This proves that \(\psi\) is not PSH. The positive distributional curvature of \(R|\eta|\) on the real axis cannot repair a negative coefficient on either open half-plane. To see this in the distributional definition, choose any nonzero nonnegative smooth test compactly supported inside such a half-plane; the integral of the smooth NW3 coefficient against it is strictly negative. Thus the failure does not depend on the nonsmooth axis or on a degenerate carrier.

There is also a completely smooth variant when \(K=\{0\}\):
\[
\widetilde\psi(z)=-\frac{\kappa}{2}\log(1+|z|^2),\qquad
\partial_z\partial_{\bar z}\widetilde\psi
=-\frac{\kappa}{2(1+|z|^2)^2}<0.
\tag{NW4}
\]
Direct Wirtinger differentiation proves NW4. It is another counterexample, distinct from the exact NW1 calculation.

## NW2. The strict seed supplies the missing curvature

Let \(t\ge1\), \(a>0\), and \(\sqrt t\ge32a\). In any complex dimension set
\[
\begin{aligned}
s&=t^2+|\eta|^2,\qquad q=t^2/s,\\
p_t(\eta)&=t^{-1/2}s^{1/2}-s^{1/4},\\
\Psi(z)&=H_K(\eta)-a\log(t^2+|z|^2)+p_t(\eta).
\end{aligned}
\tag{NW5}
\]
The full convex-support proof in L153 makes \(H_K\) PSH distributionally. The logarithm's ordinary Levi matrix is
\(I/(t^2+|z|^2)-\overline z z^{\mathsf T}/(t^2+|z|^2)^2\), between zero and \(I/(t^2+|z|^2)\). Its negative contribution therefore has magnitude at most \(a/s\).

For completeness, the radial real Hessian eigenvalues of \(p_t\), after division by \(s^{-3/4}\), are
\[
t^{-1/2}s^{1/4}-\tfrac12\ge\tfrac12
\quad\text{transversely},\qquad
q^{3/4}+\tfrac14-\tfrac34q\ge\tfrac14
\quad\text{radially}.
\tag{NW6}
\]
These follow from two ordinary derivatives of \(t^{-1/2}s^{1/2}-s^{1/4}\). The second lower bound uses \(q^{3/4}\ge q\) for \(0<q\le1\). At \(\eta=0\) their limits agree; in dimension one only the radial eigenvalue is needed. Dividing by four for the complex Hessian gives \(\mathcal L_{p_t}\ge s^{-3/4}I/16\). Also
\(a/s\le a\,t^{-1/2}s^{-3/4}\le s^{-3/4}/32\).
Thus
\[
\mathcal L_\Psi\ge\frac1{32}(t^2+|\eta|^2)^{-3/4}I
\ge\frac{t^{-3/2}}{32}(1+|\eta|^2)^{-3/4}I.
\tag{NW7}
\]
Every inequality is distributional if the support function is nonsmooth. Positivity of \(p_t\) follows from \(s^{1/2}\ge t\), and its gradient norm is at most \(t^{-1/2}\). The logarithmic gradient norm is at most \(a/t\).

The added curvature has a support-growth cost. If \(K+t^{-1/2}\overline B\subset L\), then
\[
H_K(\eta)+t^{-1/2}|\eta|\le H_L(\eta),\qquad
p_t(\eta)\le t^{-1/2}|\eta|+\sqrt t.
\tag{NW8}
\]
The latter follows from \(s^{1/2}\le t+|\eta|\) and discarding the nonpositive term \(-s^{1/4}\). Therefore the seed uses a controlled enlargement of the carrier. It is not obtained by merely smoothing a real-frequency moderate weight.

## NW3. Equivalent neighborhoods, not identical weight functions

Let \(\mathcal D(X)\) have its compact smooth support-stage inductive topology on an open convex \(X\). For every weight with the three L153 conditions, define
\[
q_\phi(v)=\left(\int_{\mathbb C^n}|F_v(z)|^2e^{-2\phi(z)}\,dV(z)\right)^{1/2}.
\tag{NW9}
\]
Each \(q_\phi\) is continuous in that topology: on a fixed support \(S\), the full smooth Fourier estimate of L153 TP11 and \(e^{-\phi}\le C_S(1+|z|)^{N_S}e^{-H_S(\eta)}\) bound the integrand by a finite derivative seminorm squared times \((1+|z|)^{-2(L-N_S)}\); choose \(L>N_S+n\). The \(L^2\) triangle inequality makes it a seminorm, and its restrictions to all stages are continuous.

Let \(\mathcal F\) be the family of all these seminorms, allowing the constants and weights to depend on the neighborhood. Its generated topology is at most the smooth-test topology, by that continuity. Conversely every smooth-test zero-neighborhood contains a convex balanced zero-neighborhood \(V\), and the fully proved L153 TP5 produces one such \(\phi\) with \(\{q_\phi<1\}\subset V\). Thus every original zero-neighborhood contains a zero-neighborhood generated by \(\mathcal F\). The two topologies coincide.

This is the precise equivalence needed in the note. It does not assert a single fixed \(\phi\) gives the entire LF topology, or pointwise comparability of the naive weight and one strict weight. The distinct L149 theorem gives the corresponding four-condition construction on \(B_{2,k}\cap\mathcal E'(X)\), with the actual support stages and a fixed moderate \(k\). L153 gives the smooth-test topology, whose required derivative orders can vary with stage. The full L155 proof uses this latter topology to represent distributions with unbounded local orders. These two completed constructions meet the two different test-space requirements.

## NW4. Coordinate covariance and the broader-domain note

For a holomorphic map \(h:\Omega\to\Omega'\) and a smooth real function \(\varphi\), the chain rule gives the exact Levi pullback
\[
\mathcal L_{\varphi\circ h}(z)[w]
=\mathcal L_\varphi(h(z))[Dh(z)w].
\tag{NW10}
\]
Indeed a mixed \(z,\bar z\) derivative of \(h\) or \(\overline h\) is zero; only the product of a holomorphic first derivative, the mixed Hessian of \(\varphi\), and its conjugate derivative remains. With the Hermitian matrix convention \(w^*\mathcal L_\varphi w\), the matrix is \(Dh(z)^*\mathcal L_\varphi(h(z))Dh(z)\).

For a proper PSH target without smoothness, positive local radial convolution preserves PSH and recovers its value at every point, as proved in [L143 HC6](../../AN02-L143.html#HC6) with its explicit radial-recovery provider. On a neighborhood of the compact image of any closed source complex disc, these smoothings have a common finite upper bound. Their pullbacks satisfy the line submean inequality by NW10. Apply Fatou to that upper bound minus the circle integrands and use pointwise recovery to pass the inequality to the pullback. Upper semicontinuity follows from upper semicontinuity of the target and continuity of \(h\). The pullback is therefore PSH, with an identically \(-\infty\) component permitted; if the target itself is identically \(-\infty\), that case is immediate. No monotonicity of the smoothing family is needed. If \(h\) is biholomorphic and \(\varphi\) has a strict smooth Levi bound, the smallest singular value of \(Dh\) has a positive minimum on each compact subset; NW10 retains a positive local bound there.

The model \(h(z)=z^2\), \(\varphi(w)=|w|^2\), gives
\[
\varphi\circ h=|z|^4,\qquad
\partial_z\partial_{\bar z}|z|^4=4|z|^2.
\tag{NW11}
\]
Thus positivity pulls back, but strict positivity is lost at the critical point \(z=0\). Away from zero, a chosen local inverse chart restores the strictly positive local bound.

This local coordinate fact is not the global \(L^2\) solvability theorem on arbitrary pseudoconvex domains or Stein manifolds mentioned in the source note. Our [L144 proof](../../AN02-L144.html#complete-proof) establishes its stated Euclidean-domain weighted estimate; the compact Fourier constructions above use the vector space \(\mathbb C^n\), its translations, support functions and whole-space transforms. The broader geometric theory cited in the note would require its own domain, metric, bundle, completeness and boundary hypotheses and a proof of the corresponding global estimate. We neither import nor silently infer that theorem from a change of coordinates.

## NW5. The scalar and systems boundary

The completed L150/L152/L155 representation theorems concern one scalar polynomial operator. They retain every factor and multiplicity of that polynomial, but this does not constitute the general systems fundamental principle. For several polynomial equations, common characteristic sets and algebraic relations among the equations must be handled together; separate scalar representations do not by themselves impose those relations on their densities.

The source's closing note explicitly points to additional local algebraic geometry and bounded cohomology for higher-degree forms when describing the full systems theory, and explains why the chapter restricts its proof to one operator. We retain that boundary. The three notes are accounted for as: broader-domain reference with its actual scope; proved strict-weight and topology constructions above and in the exact providers; and an explicit scalar/systems boundary. No externally cited systems theorem is marked proved, no new systems assignment is inferred, and no unrelated source is required for these scalar results.

## Source locators and course obligations

The note records are N15-dbar-domains on printedp300 and N15-equivalent-weights/N15-system-boundary on printedp301 of Hörmander II. The actual native pages are313/314. Original calculations NW1–NW11 and the full topology argument give the mathematical clarification; the linked original lessons give the full weighted estimates and representation providers.

This notes treatment does not claim the entire assigned course is complete. Chapter15 passage coverage, all78 Chapter16 exact targets, every assigned residual in Chapters10–13 and recursive prerequisite closure remain separate explicit obligations.
