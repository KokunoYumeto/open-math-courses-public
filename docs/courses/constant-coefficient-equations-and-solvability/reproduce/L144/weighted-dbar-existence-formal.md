# Weighted existence for the inhomogeneous Cauchy–Riemann equations

*Original proof exposition by GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0.*

Positive complex curvature supplies an estimate for an adjoint equation. Orthogonal projection removes the part of a test form that cannot pair with a closed right-hand side. Hilbert representation then turns that estimate into an actual solution. We prove the operator-domain approximation and the limiting arguments, including the case where the data have only the curvature-weighted norm required by the theorem.

Write \(z_j=x_j+iy_j\), \(\partial_j=(\partial_{x_j}-i\partial_{y_j})/2\), \(\bar\partial_j=(\partial_{x_j}+i\partial_{y_j})/2\), and \(dV=dx\,dy\) on \(\mathbb C^n\), \(n\ge1\). Inner products are linear in the first entry. For a real \(C^2\) weight \(\phi\), put

\[
(a,b)_\phi=\int a\overline b\,e^{-\phi}dV,\qquad
\kappa_\phi(z)=\min_{|\xi|=1}\sum_{j,k}\phi_{j\bar k}(z)\xi_j\overline{\xi_k}.
\tag{W1}
\]

For vectors sum the coefficient inner products. For antisymmetric two-forms use the sum over \(j<k\); in dimension one that space is zero. The Levi matrix convention is \(\phi_{j\bar k}=\partial_j\bar\partial_k\phi\).

<a id="strict-weighted-existence"></a>

**Theorem W1.** Suppose \(\phi\in C^2(\mathbb C^n;\mathbb R)\) and \(\kappa_\phi(z)>0\) everywhere. Let \(f=(f_1,\ldots,f_n)\) be measurable with

\[
B=\int |f|^2e^{-\phi}\kappa_\phi^{-1}dV<\infty,
\qquad \bar\partial_k f_j=\bar\partial_j f_k
\quad\text{as distributions}.
\tag{W2}
\]

Then there is \(u\in L^2(e^{-\phi}dV)\) such that

\[
\bar\partial_j u=f_j\quad(1\le j\le n),\qquad
\int |u|^2e^{-\phi}dV\le B.
\tag{W3}
\]

No global unweighted-in-curvature norm \(\int|f|^2e^{-\phi}\) is assumed. The hypothesis does imply \(f\in L^2_{\rm loc}\), since the continuous positive weight \(e^{-\phi}/\kappa_\phi\) has a positive lower bound on every compact set.

<a id="general-psh-weighted-existence"></a>

**Theorem W2.** Let \(\phi\) be a nontrivial global PSH function, possibly nonsmooth or minus infinite at some points. If \(f\) is distributionally closed as in (W2) and

\[
B_0=\int |f|^2e^{-\phi}dV<\infty,
\tag{W4}
\]

there is a distributional solution with

\[
2\int |u|^2e^{-\phi}(1+|z|^2)^{-2}dV\le B_0.
\tag{W5}
\]

Weights use their ordinary extended Lebesgue integrals; a null singular set does not change them. If \(\phi\equiv-\infty\), finite weighted data must be zero almost everywhere and the zero solution gives the immediate extended case.

The exact Hilbert input is [L043, Lemma 1.1](../../AN02-L043.html#a-representing-vector-in-hilbert-space): every continuous linear functional on a complex Hilbert space is an inner product with a unique representing vector of the same norm. Its full parallelogram/projection argument was read. The integration/completeness input is [the written Lebesgue foundations](../../prerequisites/banach-foundation-bridges.html), §§15.0–15.3 and §16.4. The [local PSH smoothing argument, L140 UE2](../../AN02-L140.html#UE2), proves that positive radial convolutions are smooth PSH functions, recover the actual upper semicontinuous values, and converge in local integral norm. We prove the needed monotonicity, weak extraction and differential-operator estimates below.

## W3. The weighted identity on compact smooth forms

Let \(H_0=L^2(e^{-\phi}dV)\), \(H_1=H_0^n\), and \(H_2=H_0^{\binom n2}\). Formally set

\[
Ta=(\bar\partial_j a)_j,\qquad
(Sg)_{jk}=\bar\partial_k g_j-\bar\partial_j g_k\quad(j<k),
\qquad T^*g=-\sum_j\delta_jg_j,
\quad\delta_j=\partial_j-\phi_j.
\tag{W6}
\]

The stars here agree with the weighted integration-by-parts adjoint: for compactly supported smooth coefficients,

\[
(\bar\partial_j a,b)_\phi=-(a,\delta_jb)_\phi.
\tag{W7}
\]

The real weight and the two conjugate Wirtinger operators account for the displayed sign. Mixed derivatives commute and

\[
[\delta_j,\bar\partial_k]=\phi_{j\bar k}.
\tag{W8}
\]

For \(g\in C_c^\infty(\mathbb C^n)^n\), expansion gives the exact identity

\[
\|T^*g\|_\phi^2+\|Sg\|_\phi^2
=\sum_{j,k}\|\bar\partial_k g_j\|_\phi^2
 +\int\sum_{j,k}\phi_{j\bar k}g_j\overline{g_k}\,e^{-\phi}dV.
\tag{W9}
\]

Here are the cross-term details. Summing both orientations in the square of each antisymmetric coefficient gives

\[
\|Sg\|_\phi^2
=\sum_{j,k}\|\bar\partial_k g_j\|_\phi^2
 -\sum_{j,k}(\bar\partial_k g_j,\bar\partial_j g_k)_\phi.
\tag{W10}
\]

The last sum is real: swapping \(j,k\) conjugates each term. On the other hand,

\[
\begin{aligned}
\sum_{j,k}(\delta_jg_j,\delta_kg_k)_\phi
&=-\sum_{j,k}(\bar\partial_k\delta_jg_j,g_k)_\phi\\
&=\sum_{j,k}(\bar\partial_k g_j,\bar\partial_j g_k)_\phi
  +\sum_{j,k}(\phi_{j\bar k}g_j,g_k)_\phi.
\end{aligned}
\tag{W11}
\]

The first equality uses (W7) with the adjoint of \(\delta_k\); the second uses (W8) and then (W7) again. Adding (W10) cancels the cross terms and proves (W9). Positivity of the Levi matrix now gives

\[
\int\kappa_\phi|g|^2e^{-\phi}dV
\le\|T^*g\|_\phi^2+\|Sg\|_\phi^2.
\tag{W12}
\]

The factor for two-form coefficients is exactly one over unordered pairs, or one-half over all ordered pairs. This convention keeps the sharp constant in (W3).

<a id="joint-graph-domain-approximation"></a>

## W4. Passing the estimate to the joint graph domain

Use the maximal distributional domains

\[
\mathcal D=\{g\in H_1:T^*g\in H_0,\ Sg\in H_2\}.
\tag{W13}
\]

Multiplication by the continuous coefficients of \(\delta_j\) and differentiation make sense in distributions, because weighted square-integrable functions are locally square integrable. We prove that every \(g\in\mathcal D\) is approximated by compactly supported smooth forms in the three norms \(\|g\|_\phi,\|T^*g\|_\phi,\|Sg\|_\phi\).

First choose a smooth real cutoff \(\chi\), equal to one near the origin, zero outside a fixed ball, and bounded by one, and set \(\chi_R(z)=\chi(z/R)\). Products obey

\[
T^*(\chi_Rg)=\chi_RT^*g-\sum_j(\partial_j\chi_R)g_j,
\quad
S(\chi_Rg)=\chi_RSg+(\bar\partial_k\chi_R)g_j-(\bar\partial_j\chi_R)g_k.
\tag{W14}
\]

The new coefficient derivatives have sup norm \(O(R^{-1})\). Their weighted \(L^2\) norms are thus at most \(O(R^{-1})\|g\|_\phi\), with constants depending only on the fixed cutoff and dimension. Dominated convergence handles the terms multiplied by \(\chi_R\). Consequently \(\chi_Rg\to g\) in the three graph norms.

Next take a compactly supported member \(g\) of \(\mathcal D\), and a nonnegative smooth convolution kernel \(\rho_\varepsilon\) of integral one and radius \(\varepsilon\). All supports stay in one fixed compact neighborhood. The weight is bounded above and below there by positive constants. Ordinary local \(L^2\) convolution convergence therefore gives weighted convergence of \(g*\rho_\varepsilon\) to \(g\). The constant-coefficient operator \(S\) commutes with convolution, so its convergence is identical. For the variable-coefficient adjoint,

\[
T^*(g*\rho_\varepsilon)
=(T^*g)*\rho_\varepsilon
 +\sum_j\left[\phi_j(g_j*\rho_\varepsilon)
                    -(\phi_jg_j)*\rho_\varepsilon\right].
\tag{W15}
\]

For a continuous coefficient \(a\), the bracket at \(z\) is the integral of \((a(z)-a(z-h))g(z-h)\rho_\varepsilon(h)\). On the common compact neighborhood its \(L^2\) norm is at most \(\omega_a(\varepsilon)\|g\|_2\), by the integral triangle inequality and translation invariance; \(\omega_a\) is its modulus of continuity there. This tends to zero. Weighted convergence follows from compact comparability. Each approximant is smooth with compact support, and the three graph convergences are proved. Taking a diagonal choice after the cutoff step gives the stated approximation for general \(g\).

Apply (W12) to those approximants. On each compact set, the continuous factor \(\kappa_\phi\) is bounded, and local strong \(L^2\) convergence passes its integral to the limit. The graph-norm right sides converge globally. Enlarge the compact sets and use monotone convergence to obtain (W12) for every \(g\in\mathcal D\), even if its curvature-weighted norm was not known finite beforehand. This proves the actual joint-domain estimate, not only its formal compact-support version.

## W5. Remove the orthogonal test component and represent the functional

For this step assume additionally \(f\in H_1\). Let

\[
N=\{g\in H_1:Sg=0\text{ distributionally}\}.
\tag{W16}
\]

It is closed: convergence in \(H_1\) gives local square convergence, hence distributional convergence of each tested derivative. The data lie in \(N\). A closed subspace of a Hilbert space has an orthogonal projection. To justify it at exactly the used generality, minimize the distance from a vector to that subspace. The parallelogram calculation in L043 Lemma 1.1 makes every minimizing sequence Cauchy; completeness and closedness give the minimizing vector. Varying it by real and imaginary multiples of any subspace vector proves orthogonality. This gives the unique decomposition and a projection of norm at most one.

Take a compactly supported smooth test form \(g\), and write \(g=G+J\), with \(G\in N\), \(J\in N^\perp\). For every smooth compact scalar \(\psi\), the form \(T\psi\) lies in \(N\), since mixed Wirtinger derivatives commute. Orthogonality gives \((J,T\psi)_\phi=0\), hence \(T^*J=0\) as a distribution. To justify this statement in ordinary distributional tests when the weight is only \(C^2\), first extend these compact scalar tests to \(C^1\) by local convolution convergence. For a smooth ordinary test \(\eta\), use \(\psi=e^\phi\eta\), which is compactly supported \(C^2\). Weighted integration by parts cancels \(e^\phi\), giving the ordinary test for \(-\sum_j\partial_jJ_j+\phi_jJ_j\). Thus the asserted distribution really vanishes. Thus \(T^*G=T^*g\in H_0\) and \(SG=0\); in particular \(G\in\mathcal D\). The extended estimate gives

\[
\int\kappa_\phi|G|^2e^{-\phi}dV\le\|T^*g\|_\phi^2.
\tag{W17}
\]

Since \(f\in N\), \((f,g)_\phi=(f,G)_\phi\). Weighted Cauchy–Schwarz using (W2) and (W17) yields

\[
|(f,g)_\phi|^2\le B\|T^*g\|_\phi^2.
\tag{W18}
\]

Define a linear functional on the range of these adjoint tests by

\[
\Lambda(T^*g)=(g,f)_\phi.
\tag{W19}
\]

If two tests have the same adjoint image, (W18) makes their difference's pairing zero, so the definition is independent of the chosen test. Its norm is at most \(\sqrt B\). Extend it by continuity to the closure of this range, and then to \(H_0\) by its orthogonal projection, just constructed. The norm bound is retained. L043 Lemma 1.1 gives \(u\in H_0\) with \(\Lambda(h)=(h,u)_\phi\), \(\|u\|_\phi\le\sqrt B\). Conjugating (W19) gives

\[
(f,g)_\phi=(u,T^*g)_\phi.
\tag{W20}
\]

This is exactly the weak equation \(Tu=f\). To recover ordinary distributional tests despite only \(C^2\) regularity of the weight, extend (W20) to compact \(C^1\) coefficient tests by convolution convergence on a fixed compact set. For any ordinary smooth test \(\eta\), select the single coefficient \(g_j=e^\phi\eta\), which is compactly supported \(C^2\). Its weighted pairing cancels \(e^\phi\); the adjoint expression is \(-\partial_j(e^\phi\eta)+\phi_j e^\phi\eta=-e^\phi\partial_j\eta\). Thus (W20) states the distributional derivative equation with the correct conjugate Wirtinger operator. All other coefficients are zero. This proves (W3) under the temporary extra assumption \(f\in H_1\).

<a id="local-weak-extraction"></a>

## W6. A precise local weak-limit construction

We will use the following elementary Hilbert consequence. If \(u_m\) has uniformly bounded ordinary \(L^2\) norms on every fixed ball, there is a subsequence converging weakly in \(L^2\) on every fixed ball to one \(u\in L^2_{\rm loc}\). Here is a proof. On a ball choose a countable dense set of finite-grid step functions on rational rectangles, restricted to the ball. Density follows by approximating measurable sets in measure by finite unions of rectangles, then truncating and rounding real and imaginary values; these are the ordinary Lebesgue approximation facts in the linked foundations. Take the pairings \((h,u_m)\), linear in the test \(h\) under our convention. Each is bounded. Successive subsequences and a diagonal selection make all these pairings converge. The common norm bound and density extend their limits uniquely to a bounded linear functional on that ball's Hilbert space. L043 Lemma 1.1 represents it by a vector, giving weak convergence against every \(L^2\) test. Repeat on nested integer-radius balls and diagonalize once more. Pairings on their overlaps coincide, so their representing functions agree almost everywhere and define one local function.

Weak convergence makes the norm lower semicontinuous. Indeed for a unit vector \(h\), \(|(u,h)|=\lim|(u_m,h)|\le\liminf\|u_m\|\); take the supremum over unit vectors, using \(h=u/\|u\|\) when \(u\ne0\). The same conclusion applies to a bounded continuous nonnegative weight on a fixed ball: multiplication by its square root preserves weak convergence, because its adjoint is the same bounded multiplication. Finally, the weak local limit passes distributional first derivatives to the limit by pairing with compactly supported smooth derivative tests. These facts provide every weak-limit step used below.

## W7. The data need only the stated curvature weight

We construct a nonnegative smooth convex \(\Phi\) growing quickly enough that \(\kappa_\phi e^{-\varepsilon\Phi}\) is bounded for every \(\varepsilon>0\). Let

\[
L_m=\max_{|z|\le m+1}\log^+\kappa_\phi(z),\qquad
Q_m=m(1+L_m)\quad(m=1,2,\ldots).
\tag{W21}
\]

These finite nondecreasing numbers use continuity and strict positivity of \(\kappa_\phi\). Choose a smooth nonnegative convex increasing function \(b\) on \(\mathbb R\), zero on \(( -\infty,0]\), with \(b(1)=1\). For an explicit construction integrate twice a nonnegative smooth function supported in \((0,1)\), and divide by its value at 1; its second derivative is nonnegative, and it is affine beyond 1. Define, for \(s\ge0\),

\[
P(s)=Q_1+\sum_{m\ge1}Q_m b(s-(m-1)),\qquad
\Phi(z)=P(1+|z|^2).
\tag{W22}
\]

On each bounded interval only finitely many nonzero summands occur. The endpoint flatness of \(b\) makes \(P\) smooth. It is nonnegative, increasing and convex. Its composition with \(1+|z|^2\) is smooth convex on real space, and its Levi form is nonnegative, as follows by differentiating. If \(m\le|z|\le m+1\), then \(1+|z|^2-(m-1)\ge1\), so \(\Phi(z)\ge Q_m\ge mL_m\). For any fixed \(\varepsilon>0\) and all \(m\ge1/\varepsilon\),

\[
\log\kappa_\phi(z)-\varepsilon\Phi(z)\le L_m-\varepsilon mL_m\le0.
\tag{W23}
\]

The remaining bounded ball supplies a finite bound by continuity. Thus the asserted boundedness holds globally. Set \(\phi_\varepsilon=\phi+\varepsilon\Phi\), so its least Levi eigenvalue \(\kappa_\varepsilon\ge\kappa_\phi\). We have

\[
\int|f|^2e^{-\phi_\varepsilon}dV
\le\sup_z(\kappa_\phi e^{-\varepsilon\Phi})\,B<\infty,
\qquad
\int |f|^2e^{-\phi_\varepsilon}\kappa_\varepsilon^{-1}dV\le B.
\tag{W24}
\]

The already proved case supplies \(u_\varepsilon\) with the same equations and \(\int|u_\varepsilon|^2e^{-\phi-\varepsilon\Phi}\le B\). For \(0<\varepsilon\le1\), the continuous weight \(e^{-\phi-\Phi}\) has a positive lower bound on any fixed ball. The solutions are therefore locally uniformly bounded in ordinary \(L^2\). Use W6 along \(\varepsilon=1/m\) to obtain a weak local limit \(u\), with \(Tu=f\).

For fixed \(\delta>0\), eventually \(\varepsilon\le\delta\), and nonnegativity of \(\Phi\) gives \(e^{-\phi-\delta\Phi}\le e^{-\phi-\varepsilon\Phi}\). Weighted weak lower semicontinuity on each ball gives the same bound \(B\) for its \(u\) integral. Enlarge the balls to all space, then let \(\delta\downarrow0\). Monotone convergence gives \(\int|u|^2e^{-\phi}\le B\). This proves Theorem W1 with exactly its stated hypotheses.

<a id="psh-weight-regularization"></a>

## W8. General PSH weights and the exact factor two

First let \(\phi\) be smooth PSH. Direct Wirtinger differentiation gives, with \(r^2=|z|^2\),

\[
\partial_j\bar\partial_k\log(1+r^2)
=\frac{\delta_{jk}}{1+r^2}-\frac{\overline z_j z_k}{(1+r^2)^2},
\qquad
\sum_{j,k}\partial_j\bar\partial_k\log(1+r^2)\xi_j\overline{\xi_k}
\ge\frac{|\xi|^2}{(1+r^2)^2}.
\tag{W25}
\]

The final inequality is Cauchy–Schwarz applied to the rank-one term. The weight \(\psi=\phi+2\log(1+r^2)\) is strictly PSH with least Levi eigenvalue at least \(2(1+r^2)^{-2}\). Theorem W1 therefore solves the equation and gives (W5), since

\[
e^{-\psi}\kappa_\psi^{-1}
\le\tfrac12 e^{-\phi},\qquad
e^{-\psi}=e^{-\phi}(1+r^2)^{-2}.
\tag{W26}
\]

Now let \(\phi\) be an arbitrary nontrivial global PSH function. UE2 makes it real subharmonic and locally integrable. Choose a smooth nonnegative normalized radial kernel and set \(\phi_\varepsilon=\phi*\rho_\varepsilon\). UE2 proves smoothness and PSH. We use a decreasing radial kernel expressed as positive ball averages; ball-mean monotonicity and the passage between two fixed ball radii by local \(L^1\) approximation are proved in [L141 D5](../../AN02-L141.html). Choose a normalized \(\exp(-1/(1-|a|^2))\) on \(|a|<1\), zero outside. If its radial density is \(q(r)\), then \(q(s)=\int_s^1[-q'(r)]dr\); multiplying by the ball volume shows that convolution is the average of normalized ball means with positive weights \([-q'(r)]|B(0,r)|dr\) of total one. Thus \(\phi_\varepsilon\) is nondecreasing with \(\varepsilon\), and \(\phi_\varepsilon\ge\phi\). Upper semicontinuity at the center and the ball-mean inequality show

\[
\phi_\varepsilon\downarrow\phi\quad(\varepsilon\downarrow0)
\quad\text{at every point, including values }-\infty.
\tag{W27}
\]

For example, at a minus-infinite center all nearby values are below any given finite bound once the neighborhood is small, which gives the required upper limit for the convolution. The mean inequality supplies the lower bound at a finite center.

The smooth case gives solutions \(u_\varepsilon\) with

\[
2\int |u_\varepsilon|^2e^{-\phi_\varepsilon}(1+r^2)^{-2}dV
\le\int|f|^2e^{-\phi_\varepsilon}dV\le B_0.
\tag{W28}
\]

For \(\varepsilon\le1\), \(\phi_\varepsilon\le\phi_1\), whose finite continuous values give positive lower bounds for the left weight on compact sets. Thus W6 supplies a weak local \(L^2\) limit \(u\) along a decreasing sequence of radii, with \(Tu=f\). Fix \(\delta>0\), compare the estimate with the continuous smaller weight \(e^{-\phi_\delta}(1+r^2)^{-2}\), pass by weighted weak lower semicontinuity on balls, and then enlarge the balls. Finally (W27) and monotone convergence let \(\delta\downarrow0\), proving (W5). This proves Theorem W2 without smoothness, strictness, or an unmentioned finite-value assumption on \(\phi\).

## Source credit and current scope

Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (1983 edition; second revised printing 1990; reprint 2005), §15.1, Theorems 15.1.1–15.1.2, printed pp. 271–274 (PDF pp.284–287), supplies these weighted existence targets. The proofs here are original. The operator-domain approximation, explicit auxiliary convex function and local weak-limit construction are written in full. The exact earlier Hilbert/integration/PSH inputs are linked at the beginning. Further learner examples, complete exercises and original illustrations accompany the completed lesson packet; this formal source does not claim the whole course or all downstream proofs are complete.
