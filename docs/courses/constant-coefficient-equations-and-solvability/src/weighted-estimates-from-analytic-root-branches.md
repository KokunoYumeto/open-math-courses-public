# Weighted estimates from analytic root branches

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

We now assemble the half-line inverse, algebraic branch bounds and plurisubharmonic propagation into the characteristic Cauchy estimate. The roots can move between the upper and lower half-planes. We first shift each root upward, then remove those shifts one at a time on small regions where the original root has positive imaginary part. The norm used in that analytic propagation is fixed throughout each local argument.

Read [Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md), [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md), [Uniform bounds for algebraic analytic branches](uniform-bounds-for-algebraic-analytic-branches.md), [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## Statement and the fixed time norms

Write the coordinates as \((x,t)\in\mathbb R^d\times\mathbb R\), with \(d\ge1\). Let \(P(z,s)\) be irreducible over \(\mathbb C\), nonconstant, and let its total degree be \(M_P\). Its degree in the time frequency \(s\) is \(q\), with leading coefficient \(a(z)\). Assume that for some \(A\ge1\), every analytic function \(\tau\) on a complex ball \(B(\eta,A)\) with real center \(\eta\) which satisfies \(P(z,\tau(z))=0\) obeys
\[
 \sup_{|z-\eta|<A}\operatorname{Im}\tau(z)\ge A+1.
 \tag{1}
\]
When \(q=0\), there is no such analytic root on an open ball and this condition is vacuous.

For a positive moderate time-frequency weight \(k\), use the exact norms([equation 1 in Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md))–([equation 3 in Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md)). If \(v\in C_c^\infty(\mathbb R^{d+1})\), set \(g=P(D)v\), and let \(\widehat v(z,t)\), \(\widehat g(z,t)\) denote the tangential transforms with phase \(e^{-ix\cdot z}\). Use the derivative norm \(S_P\) from([equation 2 in Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md)), evaluated also at complex tangential frequencies.

**Theorem.** There are constants \(C,\kappa,R>0\), depending on \(P,A,d\), such that whenever
\(|x|\le L\) on \(\operatorname{supp}v\cap\{t<0\}\), \(L\ge0\), one has, for every \(1\le p\le\infty\) and every such \(k\),
\[
\begin{gathered}
\sup_{\xi\in\mathbb R^d}
      \|\widehat v(\xi,\cdot)\|^-_{p,k}
 \\
\le C e^{\kappa L}
       \sup_{\substack{z\in\mathbb C^d\\|\operatorname{Im}z|<R}}
       \|\widehat g(z,\cdot)\|^-_{p,k/S_P(z,\cdot)}.
\end{gathered}
\tag{2}
\]
Replacing \(\kappa=0\), when obtained below, by any positive constant keeps this statement valid.

The derivative norm is positive everywhere: one highest nonzero polynomial derivative is a nonzero constant. Its time shifts obey the same moderate bound as in the polynomial-jet proof. Indeed collect all derivatives of \(P\) in a finite vector; shifting by \(h\) is a finite exponential of its fixed commuting nilpotent derivative matrices. That proof works with complex polynomial coefficients and with complex base points as well. Thus the weights in(2) are positive moderate weights on the real time frequency. It also gives, for each fixed \(B<\infty\), a constant \(J_B\) such that
\[
\begin{gathered}
J_B^{-1}S_P(z,s)\\
\le S_P(z+h,s)\\
\le J_B S_P(z,s),
              \\|h|\le B,\\s\in\mathbb R.
\end{gathered}
\tag{3}
\]
Both directions follow by shifting by \(h\) and then by \(-h\).

Put
\[
\begin{gathered}
V(z)=\|\widehat v(z,\cdot)\|^-_{p,k},\\
\quad
 V_*=\sup_{\mathbb R^d}V,\\
\quad
 G=\sup_{|\operatorname{Im}z|<R}
          \|\widehat g(z,\cdot)\|^-_{p,k/S_P(z,\cdot)}.
\end{gathered}
\tag{4}
\]
The [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md) theorem proves that \(V_*<\infty\), \(\log V\) is plurisubharmonic and \(V(z)\le V_*e^{L|\operatorname{Im}z|}\). If \(G=\infty\), the estimate is immediate. We may therefore assume \(G<\infty\).

## Interpolation between a whole ball and a smaller ball

We use this consequence of the proved [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md) ball lemma. Let an analytic norm \(W(z)\) satisfy \(W\le H\) on \(B(c,T)\), with \(H>0\), and \(W\le S\) on a ball of radius \(r>0\) contained there. For a point with \(|z-c|\le T-\lambda\), \(\lambda>0\), its bound is
\[
\begin{gathered}
W(z)\le H^{1-\theta}S^\theta,\\
\qquad
 \theta=\delta(T,r)\lambda/T,
 \\
\quad 0<\theta\le1.
\end{gathered}
\tag{5}
\]
If \(0<S<H\), apply the [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md) lemma to
\((\log W-\log H)/\log(H/S)\). The pointwise propagation coefficient is at least the displayed \(\theta\); replacing it by \(\theta\) weakens the bound because \(S/H<1\). If \(S\ge H\), the same inequality follows from \(W\le H\). For \(S=0\), use every positive smaller-ball bound and let it tend to zero. This covers zeros of the norm without taking an undefined logarithm. At the center of the larger ball, take \(\lambda=T\).

## One uniformly sized regular region near each real frequency

Fix a real \(\xi\in\mathbb R^d\). If \(q\ge1\), irreducibility and characteristic zero imply that \(P\) and its last-variable derivative are coprime over the tangential fraction field: the derivative has smaller last-variable degree, and Gauss's lemma preserves irreducibility there. The written full-degree Sylvester calculation therefore gives a nonzero tangential polynomial \(Q\) whose nonvanishing ensures a nonzero leading coefficient and a simple full-degree fiber. For \(q=0\), use \(Q=P\).

The [Regular balls, moving roots and complex gauges](regular-balls-moving-roots-and-complex-gauges.md) zero-free-ball lemma supplies a fixed \(0<\gamma\le1/4\) for this polynomial's degree and dimension. Set \(R=(A+3)/\gamma\). Its translated and dilated version gives a real center \(\eta\) with
\[
\begin{gathered}
|\eta-\xi|\le R/2,\\
\qquad
 Q(z)\ne0\text{ on }B(\eta,A+3),\\
\qquad
 B(\eta,A+3)\subset B(\xi,R).
\end{gathered}
\tag{6}
\]
The constants are independent of \(\xi\), even if \(Q(\xi)=0\). For \(q\ge1\), all roots therefore have analytic labels \(\tau_1,\ldots,\tau_q\) on this entire ball.

Write \(H=V_*e^{RL}\). Throughout \(B(\xi,R)\), \(V\le H\). The positive-ball propagation gives, with \(\theta_0=\delta(R,A)>0\),
\[
 V(\xi)\le H^{1-\theta_0}
                 \left(\sup_{B(\eta,A)}V\right)^{\theta_0}.
 \tag{7}
\]
For \(V_*=0\) the theorem is already true, so assume \(H>0\).

Hereafter freeze the time weight
\[
 \rho(s)=\frac{|a(\eta)|\,k(s)}{S_P(\xi,s)},\qquad s\in\mathbb R.
 \tag{8}
\]
It is a positive moderate weight and does not change as \(z\) moves in the regular ball. Scalar norm homogeneity, the jet shift and coefficient comparisons will relate it to the moving weight in \(G\). Fixing it is essential for applying the analytic norm lemma.

## Shift every root upward

Suppose \(q\ge1\), and put
\[
\begin{gathered}
T_j=\sup_{B(\eta,A)}|\nabla\tau_j|,\\
\qquad
 \beta_j=3A T_j,\\
\qquad
 q_+(z,s)=\prod_{j=1}^q(s-\tau_j(z)-i\beta_j).
\end{gathered}
\tag{9}
\]
The symbol \(q_+\) is a local polynomial in \(s\), with analytic tangential coefficients; it is not the original global polynomial.

By(1), each root has imaginary part greater than one at some point of \(B(\eta,A)\). Integrating its gradient on the straight segment between that point and any other point of the ball gives
\[
\begin{gathered}
\operatorname{Im}\tau_j(z)\ge1-2A T_j,\\
\qquad
 \operatorname{Im}(\tau_j(z)+i\beta_j)\ge1+A T_j,
                       \\
\quad z\in B(\eta,A).
\end{gathered}
\tag{10}
\]
All roots of \(q_+(z,\cdot)\) lie strictly in the upper half-plane there.

For real \(s\), its \(j\)-th factor has modulus at least \(1+A T_j\). Also
\[
\begin{gathered}
|s-\tau_j(\eta)|\\
\le |s-\tau_j(z)-i\beta_j|+4A T_j\\
\le5|s-\tau_j(z)-i\beta_j|
\end{gathered}
\]

Because \(A\ge1\), the extra unit and the gradient on the unit ball together contribute at most twice that factor. The [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md) left-hand comparison and(3) consequently give
\[
\begin{gathered}
S_P(\xi,s)\le C_1 |a(\eta)|\,|q_+(z,s)|,
                         \\
\quad z\in B(\eta,A),\ s\in\mathbb R.
\end{gathered}
\tag{11}
\]
The resulting pointwise weight inequality \(k\le C_1|q_+|\rho\) passes to extension infima. The half-line theorem, applied with the fixed \(\rho\), now gives
\[
\begin{gathered}
V(z)\le C_1
            \|q_+(z,D_t)\widehat v(z,\cdot)\|^-_{p,\rho},
                               \\
\quad z\in B(\eta,A).
\end{gathered}
\tag{12}
\]

## Remove the shifts on positive balls

For \(0\le j\le q\), define actual Schwartz functions of time
\[
\begin{gathered}
g_j(z,t)=
   \prod_{\nu\le j}(D_t-\tau_\nu(z))
   \\
\prod_{\nu>j}(D_t-\tau_\nu(z)-i\beta_\nu)
                  \\
\widehat v(z,t),\\N_j=\sup_{B(\eta,A+1)}\|g_j(z,\cdot)\|^-_{p,\rho}.
\end{gathered}
\tag{13}
\]
Each time function has the same fixed compact support as the tangential transform of \(v\). Its coefficients are analytic in \(z\), and every fixed time derivative has a locally uniformly convergent analytic expansion. Hence the map into the fixed restriction space with norm \(\rho\) is analytic, and its logarithmic norm is plurisubharmonic by [Analytic norms and propagation on complex balls](analytic-norms-and-complex-ball-propagation.md) Lemma1.

There are uniform constants controlling the last member:
\[
 N_q\le C_2 G.
 \tag{14}
\]
In fact \(g_q=\widehat g/a(z)\). On \(B(\eta,A+1)\), the ratio \(|a(\eta)/a(z)|\) is bounded independently of \(\eta\). To see this, apply the line factorization from([equation 5 in Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md)), now with zero-free radius \(A+3\) and inner radius \(A+1\): every line-root factor has modulus at least \(1-(A+1)/(A+3)>0\). There are at most \(M_P\) factors. The jet norm ratio \(S_P(z,s)/S_P(\xi,s)\) is uniformly bounded by(3), since \(|z-\xi|<R\). These two pointwise comparisons give(14) after the extension infimum; scalar multiplication of a restriction norm is exact.

For later interpolation, every member also has a whole-ball bound
\[
\begin{gathered}
\|g_j(z,\cdot)\|^-_{p,\rho}\le C_3 V(z)\le C_3 H,
                    \\
\qquad |z-\eta|<A+2.
\end{gathered}
\tag{15}
\]
Here is the required multiplier estimate, with its uniformity explicit. Apply the [Uniform bounds for algebraic analytic branches](uniform-bounds-for-algebraic-analytic-branches.md) uniform comparison to
\(\tau_\nu(z)-\tau_\nu(\eta)\), on the domain \(B(\eta,A+3)\), using an inner ball of radius \(1/2\) and an outer ball of radius \(A+5/2\). The graph relation still has total degree at most \(M_P\); translation of the domain and subtraction of a constant preserve that class. On the inner ball its supremum is bounded by half the gradient supremum on the unit ball. Cauchy bounds on coordinate disks of radius \(1/4\) in the outer ball therefore give
\(T_\nu\le C\sup_{B(\eta,1)}|\nabla\tau_\nu|\).
The same [Uniform bounds for algebraic analytic branches](uniform-bounds-for-algebraic-analytic-branches.md) comparison, now from the ball of radius \(A\) to that of radius \(A+2\), gives
\(\sup_{B(\eta,A+2)}|\tau_\nu(z)-\tau_\nu(\eta)|\le C A T_\nu\).

Thus every shifted or unshifted multiplier factor in(13) is at most a constant times
\(|s-\tau_\nu(\eta)|+1+\sup_{B(\eta,1)}|\nabla\tau_\nu|\).
The [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md) right-hand comparison bounds their product by \(C S_P(\eta,s)/|a(\eta)|\), and(3) replaces that norm by \(C S_P(\xi,s)/|a(\eta)|\). Multiplication by \(\rho\) proves the full-line norm bound by \(C k\). For any Schwartz extension of \(\widehat v\)'s negative-time restriction, the local time differential operator produces an extension of \(g_j\)'s restriction. Taking infima proves(15). An inverse or an attained infimum is not needed for this direction.

The [Uniform bounds for algebraic analytic branches](uniform-bounds-for-algebraic-analytic-branches.md) imaginary-part theorem, with \(Z_0=B(\eta,A)\), \(Z_1=B(\eta,A+1)\), \(Z_2=B(\eta,A)\), supplies a radius \(r>0\) and \(C_4\), fixed for the whole graph family, such that each root has a ball \(B_j\subset B(\eta,A+1)\) of radius \(r\) with
\[
\begin{gathered}
\operatorname{Im}\tau_j(z)>0,\\
\qquad
 T_j\le C_4\operatorname{Im}\tau_j(z),
                                    \\
\quad z\in B_j.
\end{gathered}
\tag{16}
\]
Its derivative estimates give the second inequality, using the Euclidean gradient norm and the positive-ball lower bound. Condition(1) ensures a strictly positive imaginary supremum. Decrease \(r\), if needed, so it is at most \(1/2\).

Let \(h_j\) be the expression in(13) with the \(j\)-th factor omitted. Then \(g_j=(D_t-\tau_j)h_j\) and \(g_{j-1}=g_j-i\beta_j h_j\). On \(B_j\), the half-line lower bound gives
\(\operatorname{Im}\tau_j\,\|h_j\|^-_{p,\rho}\le\|g_j\|^-_{p,\rho}\).
Using(16) and the triangle inequality yields
\[
\begin{gathered}
\|g_{j-1}(z,\cdot)\|^-_{p,\rho}
                 \le(1+3A C_4)N_j,\\
\qquad z\in B_j.
\end{gathered}
\tag{17}
\]
This remains true for \(T_j=0\); its shift is then zero.

Apply(5) to this norm on the ball \(B(\eta,A+2)\), with whole-ball bound(15), small-ball bound(17), and inner target ball \(B(\eta,A+1)\). For the fixed
\(\varepsilon=\delta(A+2,r)/(A+2)>0\), we get
\[
 N_{j-1}\le C_5 N_j^\varepsilon H^{1-\varepsilon},
                                      \quad 1\le j\le q.
 \tag{18}
\]
The proof of(5) covers either ordering of the two bounds and a zero small-ball norm. All norms in this interpolation use the single fixed \(\rho\).

## Iterate and cancel the global supremum

Iterating(18), then using(14) and(12), gives
\[
\begin{gathered}
N_0\le
 C_5^{1+\varepsilon+\cdots+\varepsilon^{q-1}}
 N_q^{\varepsilon^q}H^{1-\varepsilon^q},\\
\qquad
 \sup_{B(\eta,A)}V
                   \le C_6 G^{\varepsilon^q}H^{1-\varepsilon^q}.
\end{gathered}
\tag{19}
\]
Combine this with(7). With \(a_*=\theta_0\varepsilon^q>0\), independent of \(\xi,p,k,L\), the result is
\[
 V(\xi)\le C_7 G^{a_*}(V_*e^{RL})^{1-a_*}.
 \tag{20}
\]
Take the real-frequency supremum. If \(G=0\), this says every \(V(\xi)=0\). If \(V_*=0\), the desired bound is immediate. Otherwise divide the finite inequality by \(V_*^{1-a_*}\) and take its positive \(a_*\)-th root:
\[
 V_*\le C_7^{1/a_*}G
                 e^{\,R(1/a_*-1)L}.
 \tag{21}
\]
This proves(2), with \(\kappa=R(1/a_*-1)\ge0\). Every constant introduced by the pointwise weight comparisons and norm interpolations is independent of the specific weight and of the norm exponent. Allowing them to depend on those choices would give the same stated conclusion.

If \(q=0\), there are no root shifts. On the regular ball, \(P(z,D_t)\widehat v=a(z)\widehat v=\widehat g\). The [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md) degree-zero comparison and(3) show that \(S_P(\xi,s)\le C|a(\eta)|\), while the coefficient ratio on \(B(\eta,A)\) is bounded below. Hence \(\sup_{B(\eta,A)}V\le C G\) directly. Use(7) with \(a_*=\theta_0\) and repeat the same cancellation. This proves the vacuous-root case as well.

In tangential dimension zero, each analytic root is a constant with imaginary part at least \(A+1\). The [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md) comparison gives \(S_P(s)\le C|P(s)|\) on the real time axis, since every root distance is at least one. Apply the half-line identity to \(P\), with weight \(k/S_P\), to obtain \(\|v\|^-_{p,k}\le C\|P(D_t)v\|^-_{p,k/S_P}\) directly. Constants give equality. Thus no complex-ball argument is needed in that dimension.

## Exercises with complete solutions

**Exercise 1 — basic: a fully upper-half-plane symbol.** Suppose all roots of a one-variable \(P\) have imaginary part at least one. Prove the negative-time estimate with \(\kappa=0\), and explain why root crossings force the more elaborate argument above.

**Solution.** Each real-axis root distance \(d_j=|s-\lambda_j|\) is at least one, so \(d_j+1\le2d_j\). The [Root factors and the full symbol norm](root-factors-and-the-full-symbol-norm.md) comparison with zero tangential dimension gives \(S_P(s)\le C|a|\prod_j(d_j+1)\le C2^q|P(s)|\). Therefore \(k\le C2^q|P|k/S_P\). Take extension infima and apply the exact half-line identity with weight \(k/S_P\). The result is \(\|v\|^-_{p,k}\le C2^q\|P(D_t)v\|^-_{p,k/S_P}\), with no spatial support exponential. If a root has negative imaginary part at a tangential frequency, its full-line inverse need not preserve the negative-time restriction, as the [Weighted inversion on a half-line](weighted-inversion-on-a-half-line.md) counterexample proves. Condition(1) only finds positive imaginary part somewhere on each analytic branch; the shifts and the successive small-ball interpolations transfer that information to the required uniform estimate.

**Exercise 2 — intermediate: why the propagation weight is fixed.** Let \(h\) have nonzero negative-time restriction, and for a complex parameter \(z\) define a constant-in-frequency weight \(k_z(s)=e^{-|z|^2}\). Compute \(\log\|h\|^-_{p,k_z}\). Is it subharmonic in \(z\)?

**Solution.** Each weight separately is positive and moderate, with exponent zero. Scalar homogeneity of the extension infimum gives
\[
\begin{gathered}
\log\|h\|^-_{p,k_z}
                   =-|z|^2+\log\|h\|^-_{p,1},\\
\qquad
 \Delta_z\log\|h\|^-_{p,k_z}=-4.
\end{gathered}
\tag{22}
\]
It is not subharmonic: the circle mean about any point is smaller than its center value by the squared circle radius. The function \(h\) is a constant analytic vector, but its target norm is being changed nonholomorphically. The analytic norm lemma concerns one fixed normed space. Equation(8) freezes the real target frequency and its time weight before applying that lemma, while pointwise weight comparisons handle the other frequencies.

**Exercise 3 — advanced: track the powers and the zero case.** Starting from \(N_{j-1}\le C N_j^\varepsilon H^{1-\varepsilon}\), prove the exponent and constant in(19) by induction. Then solve \(U\le B G^a(Ue^{RL})^{1-a}\) for finite \(U\ge0\), \(G\ge0\), \(0<a\le1\).

**Solution.** After one step the powers are \(\varepsilon\) on \(N_q\) and \(1-\varepsilon\) on \(H\), with constant \(C\). If after \(k\) steps they are \(\varepsilon^k\), \(1-\varepsilon^k\), and constant \(C^{1+\cdots+\varepsilon^{k-1}}\), insert that bound into the next recurrence. Raising it to \(\varepsilon\) changes the constant exponent to \(\varepsilon+\cdots+\varepsilon^k\), while the new outside \(C\) adds one. The \(H\) exponent becomes \(\varepsilon(1-\varepsilon^k)+(1-\varepsilon)=1-\varepsilon^{k+1}\). This is exactly the claimed induction.

If \(U=0\), every asserted conclusion holds. If \(G=0\), the right side is zero when \(U>0\), which contradicts the inequality; hence again \(U=0\). For \(U,G>0\), divide by \(U^{1-a}\), preserving the inequality, and obtain
\[
\begin{gathered}
U^a\le B G^a e^{RL(1-a)},\\
\qquad
 U\le B^{1/a}G e^{RL(1/a-1)}.
\end{gathered}
\tag{23}
\]
For \(a=1\), this gives \(U\le BG\) with no exponential cost. A small interpolation power yields a larger valid constant and exponential coefficient; it does not justify dropping that power before the cancellation.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, Springer, 1983.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
