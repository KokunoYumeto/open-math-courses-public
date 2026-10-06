# Reflection-compatible changes of quantization

This companion retains the reflection-compatible conversion from AN03-U009 Section 7. The all-parameter proof below replaces its reference to a larger-parameter Gaussian extension by a complete finite-step argument on the original metric.

This is a modified selection of AN03-U009, *From Weyl symbols to operators and changes of coordinates*, from *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Original principal author: AN-03 course-writing task. Original publisher: AN-03 local course project. Copyright © 2026 AN-03 course project contributors. The AN-03 course-writing task and OpenAI Codex are responsible for the renewed edition. Selection, exact prerequisite connections and identified additions: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The [complete licence](notices/COPYING), [title information](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and [rights notice](notices/RIGHTS.md) accompany it.

The [metric Weyl product](metric-weyl-products.md) proves the dual metric and weight comparisons; the [action companion](weyl-action-and-covariance.md) proves polynomial growth, Schwartz action, distribution action and their precise topologies. The [included Gaussian remainder theorem, Section 8](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md) applies directly to phases whose actual parameter is at most one. The [proof map](proof-map.json) gives all exact earlier proofs used here.

## 7. Reflection and changes of quantization

Assume now that \(g\) is symplectically temperate, \(g\le g^\sigma\), \(m\) is a temperate weight, and
\[
g_{(x,\xi)}(t,\tau)=g_{(x,\xi)}(t,-\tau).
\tag{A33}
\]
This reflection condition says that the position and frequency directions are orthogonal for \(g\) at each point. It is needed here to keep the same metric class under all quantization changes; it was not needed for (A21).

For every fixed \(k\in\mathbb R\), the distributional Fourier multiplier
\[
T_k=\exp(i k\langle D_x,D_\xi\rangle)
\tag{A34}
\]
is a continuous automorphism of \(S(m,g)\), weakly continuous on bounded symbol sets, with inverse \(T_{-k}\). If \(h^2=\sup g/g^\sigma\), then for every integer \(N\ge0\),
\[
T_k a-\sum_{j<N}\frac{(ik\langle D_x,D_\xi\rangle)^j}{j!}a
\in S(h^Nm,g),
\tag{A35}
\]
with finite source-seminorm estimates for all output derivatives and the same bounded-set continuity.

To check the normalization, the doubled auxiliary phase \(2p\cdot q\) has symmetric representing map \((p,q)\mapsto(q,p)\). Its phase dual at \((t,\tau)\) is \(g^\sigma(t,-\tau)\), which equals \(g^\sigma(t,\tau)\) by (A33) and quadratic inversion. The actual phase \(k p\cdot q\), for \(k\ne0\), therefore has dual
\(4k^{-2}g^\sigma\) and parameter \(|k|h/2\) in the convention of [Quadratic Fourier multipliers at a moving scale](../20261004-free-intrinsic-graph/prerequisites/gauss-transform-estimates.md). First suppose \(0<|k|\le2\). The actual parameter is at most one, and
\[
1+q_Y(X-Y)\le\max(1,k^2/4)
 \bigl(1+4k^{-2}q_Y(X-Y)\bigr).
\tag{A35a}
\]
This verifies the Gaussian metric and weight hypotheses at the original distance base; scalar multiplication of the dual form cancels on the two sides of its form comparisons. The included Gaussian Theorems 7.1 and 8.1 therefore give A34–A35, with every differentiated remainder and bounded-set continuity, for this range. For \(k=0\) the map is the identity; the remainder is zero for \(N\ge1\), and is \(a\) for \(N=0\).

**The derivative weight used in finite steps.** Put \(L=i\langle D_x,D_\xi\rangle\). For every integer \(j,l\ge0\),
\[
p_l(L^ja;h^jm,g)\le C_{n,j}p_{l+2j}(a;m,g).
\tag{WC2}
\]
Here is the full contraction estimate. At a fixed point, reflection makes the metric block diagonal, \(g=\operatorname{diag}(A,B)\) with \(A,B\) positive definite. The real spectral theorem constructs the positive square roots. In the \(g\)-orthonormal position and frequency frames given by \(A^{-1/2}\) and \(B^{-1/2}\), the coefficient matrix of the contraction \(\sum_r\partial_{x_r}\partial_{\xi_r}\) is \(A^{1/2}B^{1/2}\). Its singular values are at most \(h\), because their squares are the eigenvalues of \(B^{1/2}AB^{1/2}\), whose largest eigenvalue equals \(\sup g/g^\sigma\). To justify the singular frames explicitly, diagonalize \(C^tC\) for \(C=A^{1/2}B^{1/2}\); if \(v_r\) is a unit eigenvector with eigenvalue \(s_r^2>0\), then \(Cv_r/s_r\) are an orthonormal basis. Thus the contraction is a sum of \(n\) pairs of \(g\)-unit directions with coefficients at most \(h\). Its \(j\)-th power has at most \(n^j\) terms and coefficients at most \(h^j\). Since the differential operator has constant coordinate coefficients, its \(l\) output derivatives are simply the corresponding contractions of \(D^{l+2j}a\). No derivative of a chosen frame or of \(g\) is taken. This proves WC2. The weight \(h\) and all its real powers are legitimate temperate weights by the metric-product proof following W34.

**Every real parameter on the same metric.** Given \(k\ne0\), choose the integer \(M=\max(1,\lceil |k|/2\rceil)\) and set \(q=k/M\). Let
\[
P_q=\sum_{j<N}\frac{q^jL^j}{j!},\qquad T_k=T_q^M.
\tag{WC3}
\]
Initially these are the distributional Fourier multipliers, so the equality in WC3 is exact. The small-parameter argument proves that \(T_q\) preserves each \(S(h^rm,g)\), while \(T_q-P_q\) sends \(S(m,g)\) to \(S(h^Nm,g)\). WC2 and \(h\le1\) show that \(P_q\) also preserves each of those spaces. The finite telescoping identity
\[
T_q^M-P_q^M=
\sum_{\ell=0}^{M-1}T_q^{M-1-\ell}(T_q-P_q)P_q^\ell
\tag{WC4}
\]
therefore has values in \(S(h^Nm,g)\). Each composition has a finite source-seminorm bound; chaining the finitely many bounds gives such a bound for the sum, for every output derivative. All maps retain continuity on bounded sets with their local smooth topology.

In the polynomial \(P_q^M\), the coefficients of degrees below \(N\) equal those in \(\exp(MqL)\). Indeed the coefficient of degree \(j<N\) is the finite sum over \(j_1+\cdots+j_M=j\) of \(q^j/(j_1!\cdots j_M!)= (Mq)^j/j!\), by the multinomial theorem; none of the truncations remove a summand. Each remaining term has degree at least \(N\) and therefore lies in \(S(h^Nm,g)\) by WC2. This proves A35 for every real \(k\). For \(N=0\), the assertion is simply preservation of \(S(m,g)\) by \(T_q^M\), already proved. Every constant depends on the specified \(k,N,l\) and structural data; no bound uniform in unbounded \(k\) is asserted.

For each small step the Gauss extension agrees with the stated distributional multiplier. Indeed bounded compact approximants converge in \(\mathcal S'\) by (A3); their Gauss images are bounded in the asserted polynomially growing target class and converge locally smoothly. Thus both definitions are limits of the same sequence in distributional pairings. Multiplication of the Fourier multipliers now proves \(T_kT_l=T_{k+l}\), hence the automorphism assertion. No uniform estimate for unbounded \(k\) is claimed.

Let \(\operatorname{Op}_\tau\) have the kernel base point
\((1-\tau)x+\tau y\), as in Section 4 of [Two measuring scales, one Weyl product](metric-weyl-products.md). Here is the kernel coordinate calculation for every tempered symbol. For a plane wave \(a(z,\xi)=e^{i(p\cdot z+q\cdot\xi)}\), use the kernel coordinates \(z=(1-s)x+sy,\ t=x-y\). The old base point is \(z+(s-\tau)t\); partial inverse Fourier transformation sets \(t=-q\), leaving the factor \(e^{i(\tau-s)p\cdot q}\). This is exactly the multiplier \(T_{\tau-s}\) on the symbol Fourier variables. Fourier inversion proves the identity for Schwartz symbols. The two kernel constructions, the multiplier and the affine pullback are continuous in tempered-distribution pairings; the explicit cutoff-and-mollifier density proof after A25 extends the equality to all tempered symbols. Thus
\[
\operatorname{Op}_s(T_{\tau-s}a)=\operatorname{Op}_\tau(a).
\tag{A36}
\]
Uniqueness of the symbol follows by inverse partial Fourier transformation of the kernel. In particular, if \(a,c\) are left and right symbols and \(b\) is their Weyl symbol, then
\[
\begin{gathered}
b=T_{-1/2}a=T_{1/2}c,\qquad
a=T_{1/2}b=T_1c,\\
c=T_{-1}a=T_{-1/2}b.
\end{gathered}
\tag{A37}
\]
All these symbols lie in the same \(S(m,g)\). Combining (A36) with (A21) proves their Schwartz and distribution actions, with precisely the topologies stated in Section 4.

There is an elementary action proof under the additional vertical bound
\[
g_{(x,\xi)}(0,\tau)\le|\tau|^2.
\tag{A38}
\]
It is useful to see exactly what this stronger hypothesis buys. For each fixed \(\beta\), directional symbol estimates and (A3) give
\[
|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|
\le C_{\alpha,\beta}p_{\le|\alpha|+|\beta|}(a;m,g)
(1+|x|+|\xi|)^{K_\beta},
\tag{A39}
\]
where \(K_\beta\) is independent of \(\alpha\). The vertical factor contributes at most one to each coordinate frequency derivative; the factors from the fixed position derivatives have a polynomial bound. The left operator is
\((2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi\).
After any fixed output derivatives, multiplication by \((1+|x|^2)^M\) transfers \((1-\Delta_\xi)^M\) onto the amplitude. Formula (A39) leaves only a fixed power of \(1+|x|\), independent of \(M\), and the Schwartz decay of \(\widehat u\) makes the frequency integrals finite. Choosing \(M\) large proves every desired output seminorm with finitely many source seminorms. Adjoint transposition and the quantization changes give the other actions. The more general proof of (A21) removes (A38) entirely, while the reflection condition remains in the same-class quantization theorem.

## Q8. The ordinary real order-two receiver

For the ordinary metric \(g=|dx|^2+\langle\xi\rangle^{-2}|d\xi|^2\), the [included ordinary-metric proof O2](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) verifies every metric and weight hypothesis. Reflection is immediate and \(h=\langle\xi\rangle^{-1}\). If a real left symbol \(a\) has order two, A37 and A35 with \(k=-1/2,N=2\) give its Weyl symbol
\[
b=a+\frac{i}{2}\sum_j\partial_{x_j}\partial_{\xi_j}a+r,
\qquad r\in S^0_{1,0}.
\tag{WC5}
\]
The first correction is purely imaginary. Hence the symmetric part of \(\operatorname{Op}_0(a)\) has Weyl symbol \(2a+2\operatorname{Re}r\). For any \(r_0\in S^0_{1,0}\), the inverse conversion \(T_{1/2}r_0\) remains in \(S^0_{1,0}\), and the [complete global scalar bound G1](../20261005-cauchy-foundations/sharp-lower-bound.md) shows \(r_0^w\) is bounded on \(L^2\). This proves that any established lower bound for \(a^w\) transfers to the real part of the left quantization with only a bounded error. The scalar Fefferman–Phong lower bound itself remains a separate theorem.

As a sign check the left symbol \(x\xi\) in one dimension has Weyl symbol \(x\xi+i/2\): its left operator is \(xD\), while \((x\xi)^w=(xD+Dx)/2=xD-i/2\). All higher corrections vanish because the polynomial has degree two.

The retained AN03-U009 reflection and conversion results are modified by the explicit finite-step proof WC2–WC4 and the complete plane-wave kernel calculation. Their mathematical antecedent is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, 2007 edition, Theorem 18.5.10, printed 159 (PDF 174). No source access restriction is imposed on that book. The extended calculus, unrestricted cross parameter, metric operator bound and Fefferman–Phong induction are separate from this component.
