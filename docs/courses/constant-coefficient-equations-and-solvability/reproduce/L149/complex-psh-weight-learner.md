# Building a complex weight from compact Fourier tests

*Original learner material by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked; CC0.*

The [formal companion](complex-psh-weight-formal.md) proves the full variable-scale lemma and four-condition weight theorem. The scale smooths a possibly nonsmooth real frequency weight, a radial correction supplies curvature, and a stabilized maximum joins the supports in a compact exhaustion. A separate exterior-support estimate makes the resulting integral dominate any continuous seminorm of compact weighted tests.

Use the Fourier convention and complex estimates of [L148](../../AN02-L148.html). Write \(z=\xi+i\eta\), \(M=(t^2+|\eta|^2)^{1/2}\), and \(\partial_z=(\partial_\xi-i\partial_\eta)/2\). The coefficient one quarter in a one-dimensional Levi derivative matters in these examples.

## Worked example 1. Smooth a weight with a corner

In one dimension let
\[
k(\xi)=(1+\max(\xi,0))^2,\qquad
\ell(\xi)=2\log(1+\max(\xi,0)).
\tag{L149.1}
\]
The inequality
\(1+\max(\xi+h,0)\le(1+|h|)(1+\max(\xi,0))\)
shows that \(C=1,N=2\) are valid. This weight is not even, and its logarithm has a derivative jump at zero.

Choose the symmetric probability bump
\[
\chi(y)=a\exp[-1/(1-y^2)]\quad(|y|<1),\qquad
\chi(y)=0\quad(|y|\ge1),
\tag{L149.2}
\]
where \(a\) is the reciprocal of its positive finite integral. Repeated differentiation produces a rational function of \(1-y^2\) times the exponential; the exponential tends to zero faster than every reciprocal power at the endpoints. Thus the zero extension is smooth. The regularized logarithm is
\[
\ell_t(\xi,\eta)=2\int_{-1}^1
\chi(y)\log(1+\max(\xi+My,0))\,dy.
\tag{L149.3}
\]
At \(\xi=0\) it is \(2\int_0^1\chi(y)\log(1+My)\,dy>0\), so \(k_t(0,\eta)>1=k(0)\). Smoothing is not pointwise equality with the starting weight. VS5–VS6 give instead the exact useful comparison
\(M^{-4}\le k_t(\xi,\eta)/k(\xi)\le M^4\).

The distributional derivatives of the original logarithm are
\[
\ell'(\xi)=\frac{2\,1_{\{\xi>0\}}}{1+\xi},\qquad
\ell''=2\delta_0-\frac{2\,1_{\{\xi>0\}}}{(1+\xi)^2}.
\tag{L149.4}
\]
The jump of \(\ell'\) is two, giving the positive delta term. Convolution at a fixed \(M\) therefore gives
\[
\partial_\xi^2\ell_t
=\frac2M\chi(-\xi/M)
-2\int_{\xi+My>0}\frac{\chi(y)}{(1+\xi+My)^2}\,dy.
\tag{L149.5}
\]
Both terms can be substantial; their cancellation is part of the derivative-scale estimate. The full proof VS7–VS10 does not need to differentiate \(\ell\) at its corner: it differentiates the smooth kernel instead. Formula L149.5 supplies an independent check of that argument.

## Worked example 2. Exact radial curvature

Take \(k=1\). Then \(\ell_t=0\), and the correction itself is
\[
p_t(\eta)=t^{-1/2}M-M^{1/2}.
\tag{L149.6}
\]
Let \(r=|\eta|\). In complex dimension at least two the radial complex line is spanned by the real vector \(\eta\); a tangential complex direction has \(\sum_j\eta_jw_j=0\). The corresponding eigenvalues of the Levi form are
\[
\begin{aligned}
\lambda_\parallel&=
\frac{t^2}{4M^3}\left(t^{-1/2}-\frac1{2\sqrt M}\right)
+\frac{r^2}{16M^{7/2}},\\
\lambda_\perp&=
\frac1{4M}\left(t^{-1/2}-\frac1{2\sqrt M}\right).
\end{aligned}
\tag{L149.7}
\]
To derive them, differentiate \(p_t(r)\). Its first derivative is
\((r/M)(t^{-1/2}-1/(2\sqrt M))\), its second derivative is the first displayed eigenvalue multiplied by four, and its tangential real Hessian eigenvalue is \(p_t'(r)/r\). Divide each real Hessian eigenvalue by four. At \(r=0\) both limiting values are \(1/(8t^{3/2})\). In dimension one only the radial eigenvalue is present.
Formula VS14 gives \(f''(s)<0\) for \(s\ge t^2\), because \(t^{-1/2}s^{1/4}\ge1\). Thus the radial eigenvalue is the minimum; the tangential one is larger when \(r>0\).

The normalized radial eigenvalue has a particularly clear form. Put \(q=r/t\):
\[
\lambda_\parallel M^{3/2}
=\frac1{4(1+q^2)^{3/4}}+\frac{q^2-2}{16(1+q^2)}
\ge\frac1{16},\qquad
\lim_{q\to\infty}\lambda_\parallel M^{3/2}=\frac1{16}.
\tag{L149.8}
\]
The inequality follows from the full two-sign argument VS15–VS17. Equivalently, subtract \(1/16\); the result is
\((1+q^2)^{-1}[\, (1+q^2)^{1/4}/4-3/16\,]\ge(1+q^2)^{-1}/16>0\).
The limit at infinity gives the value shown. The general logarithmic smoothing can consume at most \(1/144\) of this normalized lower bound, leaving \(1/18\).

## Worked example 3. A stabilized finite maximum

Consider the first three centered compact intervals in \(X=(-3,3)\), with radii \(r_1=1/2,r_2=1,r_3=3/2\); take \(r_4=2\) and later radii increasing to three. For \(k=1\), choose
\[
(t_1,t_2,t_3)=(64,144,256),\qquad
(G_1,G_2,G_3)=(1,160,800),\qquad
\phi_3(i\eta)=\max_{j\le3}\{r_j|\eta|+p_{t_j}(\eta)-G_j\}.
\tag{L149.9}
\]
The gap to the next interval is \(1/2\) for these three stages, and
\(2/\sqrt{t_j}<1/2\), so the interior-support condition PW9 holds. Since \(M\ge t\),
\[
0\le p_t(\eta)\le t^{-1/2}(M-t)
=\frac{|\eta|^2}{\sqrt t(M+t)}
\le\frac{|\eta|^2}{2t^{3/2}}.
\tag{L149.10}
\]
The lower bound is \(M/\sqrt t\ge\sqrt M\); the upper bound follows because the derivative in \(M\) is at most \(t^{-1/2}\) and \(p_t=0\) at \(M=t\).

For \(|\eta|\le5\), the second seed minus the first, before vertical shifts, is at most \(5/2+25/(2\cdot144^{3/2})<3\), whereas \(G_2-G_1=159\). The corresponding third difference is at most \(5+25/(2\cdot256^{3/2})<6\), whereas \(G_3-G_1=799\). Hence \(\phi_3=\phi_1\) throughout this strip. This is an exact analytic stabilization statement, not a conclusion from sampled plots.

These constants also illustrate the wider inactivity regions in PW18. The second comparison on \(|\eta|\le161\) is bounded by \(161/2+161^2/(2\cdot144^{3/2})<89<159\). The third comparison on \(|\eta|\le301\) is bounded by \(301+301^2/(2\cdot256^{3/2})<313<799\). Thus \(B_2=160,B_3=300\) are compatible inactivity radii. Each new seed has gradient bound at most \(r_j+t_j^{-1/2}\), so the logarithmic gradient bound is certainly valid beyond those radii.

At larger imaginary frequencies the slopes of the later support functions let new branches become active. The resulting maximum has positive extra distributional curvature at a branch change, rather than a classical second derivative there. This is why PW4 is stated distributionally.

![The exact radial curvature margin and a finite maximum with a stabilized strip.](figures/curvature-and-stabilized-maxima.png)

The displayed maximum is the first three branches, with their exact parameters. The final theorem continues the exhaustion and chooses the remaining constants and strip radii using the seminorm induction. The normalized curvature plot is the exact \(k=1\) correction, not a numerically constructed general-weight solution.

## Worked example 4. The exterior-support sign

At one finite construction stage let \(K=[-1,1]\), and let a smooth cutoff \(\chi\) be supported in \(C=[2,3]\). These intervals are separated in the direction \(\theta=1\), with gap one. Their supporting functions give
\[
H_C(-\eta)+H_K(\eta)=
\begin{cases}
-\eta,&\eta\ge0,\\
-4\eta,&\eta<0.
\end{cases}
\tag{L149.11}
\]
The positive imaginary direction gives decay; reversing it gives growth. If the stage weight satisfies \(\phi_{j+1}\le H_K-\log k+D\), PW24 becomes
\[
\|\chi u\|_{2,k}^2\le C_\chi e^{-2\eta}
\int|F_u(\xi+i\eta)|^2e^{-2\phi_{j+1}(\xi+i\eta)}\,d\xi
\quad(\eta\ge0).
\tag{L149.12}
\]
Its plane integral still contains the Fourier transform of the whole test \(u\). It is not the transform of \(\chi u\) on the right.

For a physical model choose \(u=1_{[9/4,11/4]}\), \(k=1\), and a cutoff equal to one near that inner interval, supported in \(C\). Then \(\|\chi u\|_2^2=1/2\), and
\[
\int|F_u(\xi+i\eta)|^2\,d\xi
=\frac{\pi}{\eta}(e^{11\eta/2}-e^{9\eta/2})\quad(\eta\ne0),
\qquad I(0)=\pi.
\tag{L149.13}
\]
This is Plancherel applied to \(e^{\eta x}u\). The comparison energy weighted by \(H_K(\eta)=\eta\) is
\[
E_\eta=e^{-2\eta}I(\eta)
=\pi\frac{e^{7\eta/2}-e^{5\eta/2}}{\eta}\quad(\eta>0),
\qquad E_0=\pi.
\tag{L149.14}
\]
The small factor \(e^{-2\eta}\) in the exterior estimate multiplies a plane energy which can grow. Their product for this model is
\(\pi(e^{3\eta/2}-e^{\eta/2})/\eta\), also growing. The proof does not say that the entire transform decays on these planes. It enlarges the integral's imaginary domain to make that integral control the exterior norm with an arbitrarily small coefficient.

![Separated real supports and the small coefficient multiplying a potentially growing plane energy.](figures/exterior-supports-and-imaginary-shifts.png)

The factor comes from the exact support-function gap in L149.11. The energy curves use the explicit exterior interval in L149.13–L149.14; the finite-stage weight comparison remains the assumption displayed in L149.12.

## Exercises with complete solutions

**Exercise 1 — entry: why only positive derivatives?** For the weight in example 1 and fixed \(\eta,t\), show that a bound \(|\ell_t(\xi,\eta)|\le D\log M\) for all \(\xi\) cannot be correct.

**Solution 1.** If \(\xi>M\), every \(\xi+My\) in the bump support is at least \(\xi-M>0\). Thus the probability integral gives \(\ell_t(\xi,\eta)\ge2\log(1+\xi-M)\), which tends to infinity as \(\xi\to\infty\). Its proposed right side is fixed. The correct zero-order statement controls \(\ell_t-\ell\), as in VS5. The estimate VS10 uses a positive derivative, whose kernel integral is zero and permits that subtraction.

**Exercise 2 — intermediate: a rigorous large parameter.** Suppose the constant \(D\) in VS18 is one. Give an explicit \(t\) satisfying VS19 without relying on a decimal approximation to the logarithm.

**Solution 2.** Take \(t=10^8\). Since \(e^3>1+3+9/2+27/6=13>10\), \(\log10<3\). Hence \((\log t)/\sqrt t<24/10^4<1/144\), the last inequality being \(24\cdot144<10^4\). Also \(t>e^2\), for example from the elementary series bound \(e<3\). The monotonicity of \((\log r)/\sqrt r\) for \(r\ge e^2\) gives the required bound for every \(M\ge t\), not just at the chosen parameter.

**Exercise 3 — intermediate: complex directions.** In \(\mathbb C^2\), let \(\eta=(r,0)\), \(r>0\). Compare the correction's Levi form on \(w=(1,0)\), \(w=(i,0)\), and \(w=(0,1)\). Does a purely imaginary first component make the direction tangential?

**Solution 3.** Each vector has norm one. In VS16 the modulus of \(\sum\eta_jw_j\) is \(r,r,0\), respectively. The first two values are therefore both \(\lambda_\parallel\), and the last is \(\lambda_\perp\). Multiplying a complex direction by \(i\) preserves its Hermitian quadratic value. Tangency here means the complex equation \(\sum\eta_jw_j=0\), not a test of real orthogonality after discarding imaginary components.

**Exercise 4 — intermediate: closed compact-support stages.** Let \(u_m\in E_j\) converge in the global \(B_{2,k}\) norm. Prove that its limit remains in \(E_j\), and explain which support condition is used.

**Solution 4.** The weighted inclusion into \(\mathcal S'\) is continuous by CF1, so \(u_m\) converges to the same limit distribution there. For every smooth compact test supported outside the fixed closed \(K_j\), each \(u_m\) has zero pairing; continuity gives zero for the limit. The definition of distributional support therefore puts it inside \(K_j\). Global membership is already supplied by the weighted norm limit. Hence \(E_j\) is closed in a complete Hilbert space, so it is Banach. The fixed support set is essential; supports escaping to infinity would not prove the same fixed-stage assertion.

**Exercise 5 — intermediate: the partition seminorms.** For the partition \(\chi_j=\theta_j\prod_{l<j}(1-\theta_l)\) in PW1, prove both local finiteness and continuity of \(\sum a_j\|\chi_j u\|_{2,k}\), for arbitrary positive \(a_j\).

**Solution 5.** The finite sum telescopes to \(1-\prod_{l\le J}(1-\theta_l)\). Around any given compact set, some \(\theta_J=1\), so the product is zero there and every later \(\chi_j\) vanishes on a neighborhood. Thus the partition sums to one and only finitely many supports meet that compact set. On \(E_i\) the seminorm sum therefore has finitely many terms. Each term is at most \(a_jA_k(\chi_j)\|u\|_{2,k}\) by CF6. Summing those finite constants proves its norm-continuity on each stage, and PW3 proves continuity in the inductive topology. No boundedness of the sequence \(a_j\) is needed.

**Exercise 6 — advanced: curvature at a maximum.** For \(a>0\) in one complex variable, compute the distributional Levi derivative of \(\max(a\eta,-a\eta)\). Then add \(p_t(\eta)\).

**Solution 6.** The maximum is \(a|\eta|\). The real derivative of \(|\eta|\) is \(\operatorname{sgn}\eta\), whose distributional derivative is \(2\delta_{\eta=0}\). Because the function is independent of \(\xi\), its Levi derivative is one quarter of that second real derivative, hence \((a/2)\delta_{\eta=0}\). This is line measure, integrated in \(\xi\), in the complex plane. It is nonnegative and is not represented by the classical second derivative away from the line, which is zero. Adding \(p_t\) adds its smooth positive radial Levi value. The lower bound is retained, together with this extra positive singular curvature. This concrete case explains the distributional formulation in PW4.

**Exercise 7 — advanced: why fixed-stage integrals are finite.** Let \(u\) be supported in a compact convex \(K\Subset X\). Use PW5 for an enlarged set \(K+\rho\overline B\Subset X\) to prove the full complex norm is bounded by a constant times the real weighted norm.

**Solution 7.** The enlarged supporting function is \(H_K(\eta)+\rho|\eta|\). Squaring PW5 gives \(e^{-2\phi}\le C^2 e^{-2H_K}e^{-2\rho|\eta|}k(\xi)^2\). The supremum of \(e^{-2\rho r}(1+r^2)^{N+2n}\) is finite: continuity handles bounded \(r\), and exponential decay handles infinity. Bound the extra exponential by this supremum times \((1+r^2)^{-N-2n}\), then apply the full complex estimate CF17. Taking square roots gives PW32. The positive enlargement margin supplies the decay which the deduction needs. For a nonconvex compact support, first take its compact convex hull as in CF9.

**Exercise 8 — advanced: outside does not imply separated.** Let \(K=[-1,1]\) and \(S=\{-2,2\}\). Calculate \(H_S(-\theta)+H_K(\theta)\) for the two unit directions in \(\mathbb R\). Explain why exterior cutoffs need smaller separated convex supports.

**Solution 8.** For either \(\theta=1\) or \(\theta=-1\), \(H_S(-\theta)=2\) and \(H_K(\theta)=1\), giving three, not a negative gap. Although each point of \(S\) is outside \(K\), its convex hull contains \(K\). A single strict separating direction therefore does not exist. Splitting the exterior region into sufficiently small balls gives compact convex supports individually separated from \(K\); the ball near two uses direction \(1\), and the ball near minus two uses direction \(-1\). The finite partition PW21 uses exactly this stronger property.

**Exercise 9 — synthesis: turn a plane estimate into a strip estimate.** In example 4 let \(A>2\), and integrate L149.12 over \(A-2<\eta<A\). Find an explicit coefficient multiplying the square-root strip integral.

**Solution 9.** This interval is the real unit ball centered at \(A-1\), and has volume two. Throughout it \(e^{-2\eta}\le e^{-2A+4}\). Integrating the squared-norm inequality gives
\(2\|\chi u\|_{2,k}^2\le C_\chi e^{-2A+4}\int_{A-2<\eta<A}\int|F_u|^2e^{-2\phi_{j+1}}\,d\xi d\eta\).
The interval lies inside \(|\eta|<A\), so taking square roots gives a coefficient \(\sqrt{C_\chi/2}\,e^2 e^{-A}\) multiplying that full strip norm. The coefficient tends to zero with \(A\), independently of \(u\). For finitely many cutoff pieces choose one \(A\) making their coefficient sum at most the prescribed inductive margin.

**Exercise 10 — synthesis: pass to the weight and its weak density.** Explain why PW30 is monotone despite the increasing weights \(\phi_j\). Then, for a continuous linear form dominated by the resulting norm, recover the reflected weak density with its exact data norm.

**Solution 10.** Increasing \(\phi_j\) alone decreases \(e^{-2\phi_j}\), so expanding domains would not by themselves imply monotonicity. The stronger fact is exact stabilization: all future branches leave \(|\eta|<A_j\) unchanged. There \(\phi=\phi_j\), and \(P_j^2\) equals the integral of the single final nonnegative integrand over \(|\eta|<A_j\). These domains increase, so monotone convergence applies. Since \(\alpha_j=j/(j+1)\to1\), the stage inequality passes to the full seminorm bound.

For the density, take the closed image of \(u\mapsto F_u e^{-\phi}\) in \(L^2(\mathbb C^n)\). The dominated form has norm at most one there, so the actual Hilbert representation gives \(g\) of \(L^2\) norm at most one with \(L(u)=\int F_u e^{-\phi}\overline g\). Put
\[
V(z)=e^{-\phi(-z)}\overline{g(-z)}.
\tag{L149.15}
\]
Reflection preserves Lebesgue measure, so \(\int|V(z)|^2e^{2\phi(-z)}\,dV(z)=\|g\|_2^2\le1\), and changing \(z\) to \(-z\) gives \(L(u)=\int V(z)F_u(-z)\,dV(z)\). This is an absolute weak pairing by Cauchy–Schwarz. Its local distribution belongs to the reciprocal reflected space by L148 CF7–CF11. Neither the reflected transform nor the reflected data weight can be silently replaced.

## Reproducibility and source map

The editable figures and calculations accompany the complete formal proof. Independent checks evaluate the actual nonsmooth-weight convolution in two coordinates, kernel and distributional derivative formulas, physical radial Hessians, finite-branch comparisons and the exterior interval's physical Fourier integrals. They supplement the analytic proofs.

The exact source map is in the formal companion: VS1–VS20 reconstruct H-II Lemma 15.2.3, and PW1–PW35 with PW3a reconstruct Theorem 15.2.1 and the partition/duality and subsequent representation passages. The classical source is Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, §15.2, printed pp. 279–285. This packet contains original exposition, solutions and artwork with ordinary attribution.
