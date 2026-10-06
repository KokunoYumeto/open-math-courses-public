# Hyperbolicity and lower order terms

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A root barrier constrains an entire polynomial. Its principal part must have real roots on real time lines, and its lower order components must be weaker than that principal part. The difficult implication is uniform: a bounded imaginary strip for the roots forces a single comparison constant valid at every real frequency. We prove that implication with an analytic rescaling argument, then connect it to eight equivalent algebraic tests.

Read [Causal solvability forces hyperbolicity](causal-solvability-forces-hyperbolicity.md), [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md), [Symbols at infinity](symbols-at-infinity.md), and [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md). We use their fixed-shift, window-norm, product, domination, semialgebraic projection, Puiseux selection and complex-zero distance results. The exact two additional analytic inputs are these.

- **Homogeneous cone entry.** For a positive-degree homogeneous \(F\), if \(F(N)\ne0\) and \(F(\xi+zN)\) has only real roots for every real \(\xi\), the component \(\Gamma(F,N)\) of \(N\) in \(\{F\ne0\}\subset\mathbb R^n\) is an open convex cone. Every \(\theta\in\Gamma\) is a hyperbolic direction, \(F/F(N)\) has real coefficients, and the roots of \(F(x+z\theta)\) are strictly negative exactly when \(x\in\Gamma\). Also \(F(x+iy)\ne0\) for real \(x\), \(y\in\Gamma\).
- **Analytic order entry.** If a germ \(g(z,\lambda)\) is holomorphic at zero, \(g(z,0)\) has exact order \(d\), and every local zero with real \(\lambda\) satisfies \(\operatorname{Im}z\le C|\lambda|\), the total Taylor order of \(g\) is at least \(d\). The assertion permits complex coefficients and uses both signs of the real parameter.

We also use polynomial factorization and Vieta, Rouché's theorem, the maximum principle and convergent power series. Continuity of polynomial roots with their multiplicities follows by small disjoint circles and Rouché when the degree is fixed and the leading coefficient remains nonzero.

Write \(P=\sum_{j=0}^mP_j\), with \(P_j\) homogeneous of degree \(j\), and retain arbitrary complex coefficients. For nonzero real \(N\), hyperbolicity means \(P_m(N)\ne0\) and \(P(\xi+i\tau N)\ne0\) for every real \(\xi\) and every real \(\tau<\tau_0\), for one fixed \(\tau_0\). No assumption of real lower order coefficients is introduced.

[Cauchy bounds, root counts and analytic extensions](cauchy-bounds-and-root-counts.md), Sections 1–2, proves the Cauchy estimates, maximum modulus and persistent root counts. The homogeneous cone theorem and analytic zero-strip order theorem specified below are planned prerequisites of [Distributions, kernels and analytic singularities](../prerequisites/planned-foundation-proofs.html).

## A barrier in both directions

For \(m=0\), a nonzero constant has no roots and every assertion is immediate. Assume \(m\ge 1\). For fixed real \(\xi\), consider \(z\mapsto P(\xi+izN)\). Its degree is exactly \(m\), with leading coefficient \(i^m P_m(N)\), independent of \(\xi\). If \(z=a+ib\) is a root, it is also the vector root \((\xi-bN)+iaN\); hence every root has \(\operatorname{Re}z\ge\tau_0\).

The coefficient of \(z^{m-1}\) is affine in \(\xi\): it receives a term linear in \(\xi\) from \(P_m\), a constant term from \(P_{m-1}\), and nothing from smaller degrees. Vieta therefore makes the sum of the real parts of the \(m\) roots a real affine function of \(\xi\). This function is at least \(m\tau_0\) on all of \(\mathbb R^n\); a nonconstant affine function is unbounded below along a line. The sum is consequently one constant \(c\). Each root then satisfies
\[
\tau_0\le\operatorname{Re}z\le c-(m-1)\tau_0.
\]
Changing \(N\) to \(-N\) changes \(z\) to \(-z\), so a negative barrier for \(-N\) follows, and \(P_m(-N)=(-1)^mP_m(N)\ne0\). Equivalently there is \(C>0\) such that every root of \(P(\xi+zN)\), \(\xi\) real, has \(|\operatorname{Im}z|\le C\). Neither distinct roots nor real coefficients were used.

## The homogeneous principal part

For fixed real \(\xi\), the polynomials
\[
R^{-m}P(R\xi+iRzN),\qquad R\to+\infty,
\]
converge coefficientwise to \(P_m(\xi+izN)\), with the same nonzero leading coefficient \(i^mP_m(N)\). Their roots have real part at least \(\tau_0/R\). Rouché/root continuity implies that every root of the limit has real part at least zero. Thus \(P_m(\xi+i\tau N)\ne0\) for \(\tau<0\).

If \(F\) is homogeneous and hyperbolic and \(F(\xi+zN)=0\), homogeneity gives \(F(\lambda\xi+\lambda zN)=0\) for every nonzero real \(\lambda\). The negative-imaginary barrier applied after absorbing the real part of \(\lambda z\) implies \(\lambda\operatorname{Im}z\ge\tau_0\) for every such \(\lambda\). This forces \(\operatorname{Im}z=0\). Conversely, if \(F(N)\ne0\) and all roots on every real affine \(N\)-line are real, \(F(\xi+i\tau N)\ne0\) for every real \(\tau\ne0\); a barrier at zero suffices. Constants are covered by the empty-root convention. 

For \(m\ge 1\), apply the homogeneous cone entry to \(F=P_m\). We henceforth write \(\Gamma=\Gamma(P_m,N)\). In particular \(\Gamma\) is open and convex and does not contain zero, and \(P_m(N+u\theta)\) has only strictly negative roots when \(\theta\in\Gamma\), since both \(N,\theta\) lie in \(\Gamma\). The degree is \(m\), with leading coefficient \(P_m(\theta)\ne0\). Nonzero constants are hyperbolic along every nonzero real direction and need no cone argument.

## Transport the full barrier through a cone

Assume \(m\ge 1\) and retain a barrier \(\tau_0\) for \(P\). We prove
\[
\begin{gathered}
P(\xi+i\tau N+i\sigma\theta)\ne0,\\
\xi\in\mathbb R^n,\quad \theta\in\Gamma,\\
\operatorname{Re}\tau<\tau_0,\quad
\operatorname{Re}\sigma\le0.
\end{gathered}
\]
Fix \(\xi,\theta\). As a polynomial in \(\sigma\), the displayed expression has degree \(m\) and fixed leading coefficient \(i^mP_m(\theta)\ne0\). If \(\operatorname{Re}\sigma=0\), the term \(i\sigma\theta\) is real. Absorb it and the real vector \(-\operatorname{Im}\tau N\) into \(\xi\); the barrier precludes a zero. The number of roots in \(\operatorname{Re}\sigma<0\), counted with multiplicity, is locally constant as \(\tau\) varies in the connected halfplane \(\operatorname{Re}\tau<\tau_0\). Root continuity proves this locally; fixed degree prevents roots escaping at finite parameter values.

Take \(\tau=T\) real and let \(T\to-\infty\). Setting \(\sigma=uT\) and dividing by \((iT)^m\), the root polynomial tends coefficientwise to \(P_m(N+u\theta)\). All its roots are strictly negative real numbers by the homogeneous cone entry. For sufficiently negative \(T\), all roots \(u\) have negative real part, so all corresponding roots \(\sigma=uT\) have positive real part. The count in the negative halfplane is zero there, and therefore zero for all permitted \(\tau\). The imaginary boundary was already excluded. This proves the zero-free cone assertion, including complex \(\tau,\sigma\).

For \(\varepsilon>0\), put \(\tau=\varepsilon\sigma\) with \(\sigma\) real and sufficiently negative. The result supplies a barrier along \(\theta+\varepsilon N\). For a given \(\theta\in\Gamma\), openness permits a small \(\varepsilon>0\) with \(\theta-\varepsilon N\in\Gamma\). Apply the preceding conclusion to that vector: \((\theta-\varepsilon N)+\varepsilon N=\theta\). Also \(P_m(\theta)\ne0\). Thus \(P\) is hyperbolic in every direction of \(\Gamma\). The conclusion uses the principal cone but applies to the full polynomial.

## An analytic strip comparison

Let \(h(z,r,s)\) be holomorphic at \(0\in\mathbb C^3\). Suppose that in a fixed sufficiently small neighborhood,
\[
\begin{gathered}
h(z,r,s)=0,\quad r,s\in\mathbb R\\
\Longrightarrow\quad |\operatorname{Im}z|\le C|s|.
\end{gathered}
\tag{1}
\]
Then there is \(C'>0\) such that
\[
\begin{gathered}
|h(it,r,t)|\le C'|h(it,r,0)|,\\
t,r\in\mathbb R\text{ small}.
\end{gathered}
\tag{2}
\]
The function \(h\) need not be a polynomial.

First, \(h(z,0,0)\) cannot be identically zero: a small nonreal \(z\) would violate (1). Let its order at zero be \(d\). If \(d=0\), the denominator is nonzero near zero, so continuity proves (2). We induct on \(d\).

We prove the total-order adapter required for the rescaling. For any real \(a,b\), set \(g(z,\lambda)=h(z,a\lambda,b\lambda)\). Its \(z\)-axis order is \(d\), and (1) implies \(\operatorname{Im}z\le C|b||\lambda|\) at every local zero with real \(\lambda\). The analytic order entry says that \(g\) has total Taylor order at least \(d\). If a homogeneous Taylor component of \(h\) of degree less than \(d\) were nonzero, its substitution \(r=a\lambda,s=b\lambda\) would therefore vanish for every real \(a,b\). Comparing powers of \(z,\lambda\), its coefficient polynomials in \(a,b\) vanish on all real pairs and hence identically. Thus every such component is zero. We have
\[
h(z,r,s)=h_d(z,r,s)+O((|z|+|r|+|s|)^{d+1}),
\]
where \(h_d\) is homogeneous of degree \(d\) and its coefficient of \(z^d\) is nonzero.

Next establish a uniform denominator bound
\[
\begin{gathered}
|h(it,r,0)|\ge c|t|^d,\\
t,r\in\mathbb R\text{ small}.
\end{gathered}
\tag{3}
\]
Choose a disk \(|z|<\rho\) on which \(h(z,0,0)\) has exactly its \(d\) zeros at zero and none on the boundary. For all small real \(r\), Rouché gives exactly \(d\) zeros in this disk, all lying in \(|z|<\rho/2\). By (1) with \(s=0\), these roots \(\lambda_1(r),\ldots,\lambda_d(r)\) are real. Divide \(h(z,r,0)\) by \(\prod_j(z-\lambda_j(r))\); removable singularities give a zero-free holomorphic quotient \(q_r\) in the disk. On \(|z|=\rho\), the numerator is uniformly bounded below by a positive number, whereas the product is at most \((2\rho)^d\). The maximum principle applied to \(1/q_r\) gives a uniform positive lower bound for \(|q_r|\) throughout the disk. Finally \(|it-\lambda_j(r)|\ge|t|\), proving (3). This argument does not require roots labeled analytically in \(r\).

The total-order statement makes
\[
h_1(z,r,s)=r^{-d}h(rz,r,rs)
\tag{4}
\]
holomorphic at zero: every Taylor monomial acquires a nonnegative power of \(r\). At \(r=0\), \(h_1(z,0,s)=h_d(z, 1,s)\), which has nonzero \(z^d\) coefficient. Its \(z\)-axis order is at most \(d\). For real nonzero \(r\), its zeros satisfy (1) after division of \(|\operatorname{Im}(rz)|\le C|rs|\) by \(|r|\). The same implication holds at \(r=0\). Indeed \(h_1(z,0,s)\) is not identically zero for any fixed small real \(s\), because its \(z^d\) coefficient persists. A hypothetical root outside the strip has an isolating disk outside the strip; Rouché would produce nearby roots for small real nonzero \(r\), a contradiction.

If (2) is known for \(h_1\), it proves (2) for \(h\) when \(|t|\le\eta|r|\), for some sufficiently small \(\eta>0\): substitute \(z=i(t/r)\), parameter \(s=t/r\) into that comparison and cancel \(|r|^d\). In the complementary region \(|t|>\eta|r|\), the total-order estimate bounds \(|h(it,r,t)|\) by \(C_\eta|t|^d\), while (3) bounds the denominator below. The case \(r=0\) is in this complementary region for \(t\ne0\), and \(t=0\) is immediate. Thus a comparison for the rescaled germ lifts to one for the original germ.

If the axis order of \(h_1\) drops below \(d\), the induction hypothesis proves its comparison and the lifting finishes the proof. If it remains \(d\), repeat (4). After \(k\) steps in which the order has not dropped, write the original convergent series as
\[
h(z,r,s)=\sum_{\alpha,\beta,\gamma\ge0}a_{\alpha\beta\gamma}z^\alpha r^\beta s^\gamma.
\]
The rescaled series is
\[
\sum a_{\alpha\beta\gamma}z^\alpha
r^{\beta+k(\alpha+\gamma-d)}s^\gamma.
\tag{5}
\]
Analyticity at every stage forces each exponent of \(r\) in a nonzero term to be nonnegative. There is no cancellation between different triples: for fixed \(\alpha,\gamma\) the map from \(\beta\) to the displayed exponent is injective. If any nonzero coefficient has \(\alpha+\gamma<d\), choosing \(k>\beta/(d-\alpha-\gamma)\) is impossible. Hence the axis order must drop after finitely many steps, and the finite chain of lifting arguments applies.

The only remaining case has \(a_{\alpha\beta\gamma}=0\) whenever \(\alpha+\gamma<d\). Absolute convergence of the original power series then directly gives \(|h(it,r,t)|\le C|t|^d\) on a small bidisk of real \((t,r)\). Combine this with (3). This completes the induction and proves (2), with all termination and uniformity steps explicit.

## From a root strip to bounded ratios

Homogenize without any division at zero:
\[
p(\zeta,s)=\sum_{j=0}^m s^{m-j}P_j(\zeta).
\]
Thus \(p(\zeta,0)=P_m(\zeta)\), \(p(\zeta, 1)=P(\zeta)\), and \(p\) is homogeneous of total degree \(m\). The two-sided barrier proof and the principal-part proof imply the full strip
\[
\begin{gathered}
p(\xi+zN,s)=0,\quad \xi,s\text{ real}\\
\Longrightarrow\quad |\operatorname{Im}z|\le C|s|.
\end{gathered}
\tag{6}
\]
For \(s\ne0\), divide by \(s\) inside \(P\) and use the two-sided strip from the two-sided barrier proof, including negative \(s\). At \(s=0\), use the principal-part proof and the real-root characterization. We claim
\[
\begin{gathered}
|p(\xi+itN,t)|\le C_1|p(\xi+itN,0)|,\\
\xi,t\text{ real}.
\end{gathered}
\tag{7}
\]
Constants \(m=0\) are immediate. The case \(\xi=0\), \(t\ne0\), is immediate by total homogeneity and \(P_m(N)\ne0\); the case \((\xi,t)=(0,0)\) is immediate too. For \(\xi\ne0\), total homogeneity reduces to \(|\xi|=1\).

The factorization
\[
\begin{gathered}
P_m(\xi+zN)=P_m(N)\prod_{j=1}^m(z-\lambda_j(\xi)),\\
\lambda_j(\xi)\in\mathbb R.
\end{gathered}
\]
gives \(|p(\xi+itN,0)|\ge |P_m(N)|\,|t|^m\). The numerator is uniformly \(O((1+|t|)^m)\) on the unit sphere, so large \(|t|\) cause no problem. On every compact interval bounded away from \(t=0\), continuity and this denominator bound prove (7). At \(t=0\), numerator and denominator are identical. Only a possible failure as \(t\to0\), \(t\ne0\), remains.

For each such \(t\), maximize the ratio in (7) on the compact unit sphere. Its square is a quotient of real polynomials with strictly positive denominator there, so the maximum function and the compact set of maximizers are semialgebraic by the projection and Puiseux lemmas. If the maxima were unbounded as \(t\to0\), choose a sign \(\varepsilon\in\{1,-1\}\) with unbounded maxima for \(t=\varepsilon u\), \(u\downarrow0\). The Puiseux expansion implies that on a final sufficiently small interval these maxima tend to infinity. Select a maximizing point \(\xi(u)\) using the projection and Puiseux lemmas. Its bounded coordinates have convergent Puiseux series with no negative powers. Clear their finitely many denominators by \(u=r^q\). The resulting vector \(\Xi(r)=\xi(r^q)\) extends holomorphically to zero, has real coefficients, and is real for real \(r\). The identity \(|\Xi(r)|=1\) for \(r>0\) extends as a real analytic identity for all small real \(r\).

Set \(h(z,r,s)=p(\Xi(r)+zN,s)\). It satisfies (1) by (6). The analytic comparison lemma gives
\[
|p(\Xi(r)+itN,t)|\le C'|p(\Xi(r)+itN,0)|
\]
for all small real \(t,r\). Taking \(t=\varepsilon r^q\), \(r>0\), contradicts the chosen diverging maxima. This proves (7). In particular, \(t=1\) gives
\[
\begin{gathered}
|P(\xi+iN)|\le C_1|P_m(\xi+iN)|,\\
\xi\in\mathbb R^n.
\end{gathered}
\tag{8}
\]
The compact selection and Puiseux lemmas provide the analytic maximizing curve needed for the proof.

## Eight equivalent criteria

Assume \(P_m\) is hyperbolic with respect to \(N\). The following eight conditions are equivalent, and each is equivalent to hyperbolicity of the full \(P\):

1. \(P(\xi+iN)/P_m(\xi+iN)\) is uniformly bounded for real \(\xi\).
2. Every \(P_j(\xi+iN)/P_m(\xi+iN)\), \(0\le j\le m\), is uniformly bounded.
3. \(P\prec P_m\).
4. \(P_j\prec P_m\) for every \(0\le j\le m\).
5. \(P-P_m\ll P_m\).
6. \(P_j\ll P_m\) for every \(0\le j<m\).
7. \(P\) and \(P_m\) have equal strength.
8. There is \(R>0\) with \(P(\sigma(\xi+iN))\ne0\) for every real \(\xi\) and every complex \(\sigma\) with \(|\sigma|>R\).

The bounds in 2 can be combined because there are finitely many \(j\)'s.

First, 1 implies 3. Put \(A(w)=P(w+iN)\), \(B(w)=P_m(w+iN)\). The pointwise inequality \(|A(\eta)|\le C|B(\eta)|\) holds at every real \(\eta\). Taking supremum on each real unit ball and applying finite-dimensional window norm equivalence gives \(S_A(\xi, 1)\le C' S_B(\xi, 1)\). Fixed complex shifts have bounded invertible Taylor matrices on the derivative vectors. Applying these matrices in both directions converts this to \(S_P(\xi, 1)\le C''S_{P_m}(\xi, 1)\).

Next, 3 implies 4. For each fixed nonzero real \(a\), the chain rule gives
\[
S_{P(a\cdot)}(\xi, 1)=S_P(a\xi,|a|).
\]
Rescaling the finitely many derivative weights compares this with \(S_P(a\xi, 1)\). Homogeneity of \(P_m\) likewise compares \(S_{P_m}(a\xi, 1)\) with \(S_{P_m}(\xi, 1)\), with constants depending on \(a\). Thus \(P(a\cdot)\prec P_m\). Choose \(m+1\) distinct nonzero real \(a\)'s. The Vandermonde system \(P(a\xi)=\sum_j a^jP_j(\xi)\) is invertible; every \(P_j\) is a fixed linear combination of these weaker polynomials. Hence 4.

To prove 4 implies 2, take a small complex ball about \(iN\) whose imaginary vectors lie in \(\Gamma(P_m,N)\). The homogeneous cone entry gives \(P_m(\xi+iN+z)\ne0\) there for every real \(\xi\). Apply the complex-zero distance lemma to \(B(w)=P_m(w+iN)\): its zero distance at every real \(\xi\) is uniformly positive. Therefore every derivative ratio \(\partial^\alpha B(\xi)/B(\xi)\), \(|\alpha|\le m\), is uniformly bounded, and
\[
S_{P_m(\cdot+iN)}(\xi, 1)\le C|P_m(\xi+iN)|.
\tag{9}
\]
The fixed-shift derivative-vector comparison and 4 now imply
\[
\begin{aligned}
|P_j(\xi+iN)|&\le S_{P_j(\cdot+iN)}(\xi,1)\\
&\le C_jS_{P_m(\cdot+iN)}(\xi,1)\\
&\le C'_j|P_m(\xi+iN)|.
\end{aligned}
\]
Finally 2 implies 1 by summing. This proves equivalence of 1–4.

For each homogeneous \(P_j\),
\[
S_{P_j}(\xi,t)=t^j S_{P_j}(\xi/t, 1)\qquad(t>0).
\]
Thus 4 yields \(S_{P_j}(\xi,t)\le C_j t^{j-m}S_{P_m}(\xi,t)\). For \(j<m\), this tends uniformly to zero in the ratio, proving 6 by Proposition 3.2 in *Rescaled symbols and stable strength*. Finite summation gives 5. Lemma 3.3 in *Rescaled symbols and stable strength* gives 5 implies 7, and 7 implies 3 immediately. Therefore 1–7 are equivalent. Notice that the limit is an enlarged-window limit, not the generally false assertion of a small ratio at every frequency tending to infinity.

Since \(P_m(\xi+iN)\ne0\), divide the polynomial in 8 by this leading coefficient. Its monic coefficients are exactly the ratios in 2. Uniformly bounded coefficients give a uniform root bound: if every coefficient has absolute value at most \(M\), a root cannot have \(|\sigma|>1+M\), by comparison of the leading power with the geometric sum of lower powers. Conversely, if all \(m\) roots have \(|\sigma|\le R\), Vieta bounds each coefficient by \(\binom{m}{k}R^k\). This proves 2 equivalent to 8 with full complex \(\sigma\).

Condition 8 implies hyperbolicity: for any negative real \(T\) with \(|T|>R\), take \(\xi=\eta/T\); then \(P(\eta+iTN)\ne0\) for all real \(\eta\). The nonzero principal value is part of the assumed hyperbolicity of \(P_m\). Conversely, full hyperbolicity gives 1 by the bounded-ratio proof.  For \(m=0\), all lower parts are empty, all norms are constant, and 8 says the nonzero constant is nonzero; all eight conventions agree.

## Exercises with complete solutions

**Exercise 1 (introductory).** Check that \(P(z)=z^m+\sum_{j<m}a_jz^j\), with arbitrary complex \(a_j\), is hyperbolic in both directions in one real variable, and identify its inactive space.

**Solution.** Its finitely many roots have a minimum and maximum imaginary part. Choose a barrier below the minimum for \(N=1\), and below the minimum of their negatives for \(N=-1\). The principal value in either direction is nonzero. For \(m\ge 1\), the principal monomial depends on the coordinate, so \(A(P_m)=\{0\}\) and the inactive-space result gives \(A(P)=\{0\}\). For a nonzero constant, both inactive spaces are all of \(\mathbb R\). No claim that the roots themselves are real is made for the nonhomogeneous completion.

**Exercise 2 (introductory).** For \(F=x^2-y^2-z^2\) and \(N=e_x\), determine \(\Gamma(F,N)\) and the roots of \(F(v+tN)\) for \(v\in\Gamma\).

**Solution.** The component containing \((1,0,0)\) is \(\{x>\sqrt{y^2+z^2}\}\). It is a convex open cone by the triangle inequality. The roots are \(-x\pm\sqrt{y^2+z^2}\), both strictly negative precisely on this component. The other component gives both positive roots. At the boundary at least one root is zero, so strict negativity does not extend to the closed cone.

**Exercise 3 (intermediate).** If a homogeneous \(Q\) of degree \(j<m\) is weaker than a homogeneous \(F\) of degree \(m\), obtain a uniform rate for the enlarged-window comparison, and explain why \(F+Q\) has equal strength.

**Solution.** Homogeneity gives \(S_Q(\xi,t)=t^j S_Q(\xi/t, 1)\) and the analogous identity for \(F\). Therefore \(S_Q(\xi,t)/S_F(\xi,t)\le Ct^{j-m}\), uniformly in \(\xi\). This tends to zero, so \(Q\ll F\). Lemma 3.3 in *Rescaled symbols and stable strength* supplies equal strength of \(F+Q\) and \(F\). The estimate makes no assertion that the scale-one ratio tends to zero on all escaping rays.

**Exercise 4 (advanced).** For \(h(z,r,s)=(z-r)^2+s^2\), verify the strip hypothesis of the analytic comparison lemma and find the optimal constant in its comparison.

**Solution.** For real \(r,s\), the roots are \(r\pm is\), so \(|\operatorname{Im}z|=|s|\). Also
\[
h(it,r,t)=r^2-2irt,\qquad
|h(it,r,0)|=r^2+t^2.
\]
At \(r=0\), the numerator is zero. For \(r\ne0\), put \(q=t^2/r^2\ge0\). The square of the ratio is \((1+4q)/(1+q)^2\), whose derivative has the sign of \(2-4q\). Its maximum occurs at \(q=1/2\) and equals \(4/3\). Thus the optimal constant is \(2/\sqrt 3\), attained arbitrarily close to the origin along \(t=\pm r/\sqrt 2\). At \((t,r)=(0,0)\), both sides are zero, so the inequality remains valid without defining a quotient.

## References

The strength comparisons used here are proved in [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). The projection, convergent Puiseux and compact selection lemmas are proved in [Symbols at infinity](symbols-at-infinity.md), Lemmas 2.1 and 3.1 and Corollary 3.3. The uniform shifted derivative estimate uses [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md), Lemma 1.1. The two additional analytic entries are stated with their precise hypotheses at the start of the first lesson.
