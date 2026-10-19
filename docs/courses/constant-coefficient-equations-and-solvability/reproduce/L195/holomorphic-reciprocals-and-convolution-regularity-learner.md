# Holomorphic reciprocals and convolution regularity

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Original exposition, examples and solutions: CC0.*

Convolution can erase singularities. A Gaussian turns a point mass into an analytic function. A primitive behaves differently: differentiating it recovers its input. A general microlocal version of this recovery is possible when the kernel's Fourier transform admits a holomorphic reciprocal with polynomial growth in a complex cone at infinity.

Read Pulling back and combining analytic singularities, Section 2, for analytic-wavefront localization; Analytic directions of holomorphic boundary values, Lemma 1.1, for controlled cutoffs; and [Schwartz functions and Fourier inversion](../../prerequisites/schwartz-fourier-foundations.html), Sections F1-F5, for the Fourier conventions. The [complete proof](holomorphic-reciprocals-and-convolution-regularity-formal.md) supplies the analytic multiplier estimate and the convolution theorem.

## 1. A reciprocal in the required frequency neighborhood

Let \(\mu\in\mathcal S'(\mathbb R^n)\). A nonzero real direction \(\xi_0\) is outside its convolution characteristic set if a holomorphic function \(\Phi\) exists on a complex conic neighborhood of that direction above some radius, with
\[
 |\Phi(\zeta)|\le C(1+|\zeta|)^m,\qquad
              \Phi\,\widehat\mu=1
              \quad\hbox{on the real high-frequency cone}.
 \tag{CL1}
\]
The product identity is distributional. The Fourier transform \(\widehat\mu\) need not be a function, and \(\Phi\) may vanish on real frequencies. What matters is the stated identity and the bound on a complex neighborhood. Denote the remaining nonzero directions by \(\operatorname{Char}\mu\).

For every compactly supported distribution \(v\), Theorem 4.1 of the full proof gives
\[
 \operatorname{WF}_A(v)
 \subset\operatorname{WF}_A(\mu*v)
       \cup(\mathbb R^n\times\operatorname{Char}\mu).
 \tag{CL2}
\]
Thus analyticity of the output at a point and an allowed direction forces analyticity of the input there in that direction. Theorem 2.1 establishes the analytic multiplier estimate used to prove this assertion.

The same inclusion holds for an arbitrary distribution \(v\) if addition is proper on the two supports. Properness means that the input pairs contributing to a compact output set form a compact set. The full proof, Corollary 4.2, then uses a compact input cutoff separately near each output neighborhood. It imposes no growth bound on \(v\).

## 2. The derivative budget behind analytic regularity

The reciprocal's holomorphic polynomial bound gives Cauchy estimates
\[
 \frac{|\partial^\alpha\Phi(\xi)|}{\alpha!}
     \le C^{|\alpha|+1}|\xi|^{m-|\alpha|}.
 \tag{CL3}
\]
A finite Taylor expansion separates the multiplier into local products with cutoff derivatives and a remainder. The local products use the analytic regularity of the output. The remainder is bounded in the fixed tempered seminorm of that output.

Choose the expansion index \(K=N+B\), where \(B\) is a fixed loss depending on the distributional order, symbol order and dimension. A cutoff with controlled derivatives through \(4K\) covers every derivative in the expansion and remainder. Its fixed low derivatives remain uniformly bounded, so the localized output distributions have a common order.

An apparently extra factor \(K^{|\alpha|}\) from a cutoff derivative is accompanied by \(|\xi|^{-|\alpha|}\) from the Taylor coefficient. In the region \(|\xi|\ge K\) this quotient is harmless. The remaining fixed shift satisfies
\[
 (N+B)^{N+B+c}\le C_{B,c}^{N+1}N^N.
 \tag{CL4}
\]
It therefore retains the single analytic factorial scale. Bounded frequencies use the common compact distributional estimate.

After multiplying the convolution equation by this localized reciprocal, the error has no Fourier transform in a smaller cone at infinity. Lemma 3.1 proves that such a Fourier gap is analytically regular in its interior directions, at every base point. This completes the recovery of the input's analytic regularity.

## 3. Four examples

### Example 1: a primitive with a noncompact kernel

Let \(\mu=H\), the Heaviside function on the line. With \(\widehat f(\xi)=\int e^{-ix\xi}f(x)\,dx\), its transform is
\[
 \widehat H=\pi\delta_0-i\,\operatorname{pv}(1/\xi),
 \qquad i\xi\,\widehat H=1.
 \tag{CL5}
\]
For a direct derivation, damp \(H\) by \(e^{-\epsilon x}\). Its transform is
\((\epsilon+i\xi)^{-1}=-i(\xi-i\epsilon)^{-1}\).
The lower boundary formula of Cauchy kernels and distributional boundary limits, Theorem 4.1, gives (CL5) as \(\epsilon\downarrow0\). The damping converges in tempered distributions by dominated convergence on Schwartz tests. Multiplication by \(\xi\) kills the point term and changes the principal value into one.

The reciprocal \(\Phi(\zeta)=i\zeta\) is entire and polynomially bounded. Both real rays are allowed, so \(\operatorname{Char}H=\varnothing\). For example, if
\[
 v=\delta_0-2\delta_1+\delta_3,
 \qquad g=H*v=H(x)-2H(x-1)+H(x-3),
 \tag{CL6}
\]
then \(g\) has values \(0,1,-1,0\) on the four intervals cut out by \(0,1,3\), and \(\partial_xg=v\). Both analytic covector signs occur at every jump. At the interior jump one may subtract its analytic constant value on the adjacent interval and apply the support-normal theorem locally. The kernel is noncompact, although this particular output is compactly supported.

### Example 2: a reciprocal that vanishes on an allowed direction

On the plane put
\[
 \mu(x_1,x_2)=H(x_1)\delta_0(x_2),\qquad
                   \Phi(\zeta)=i\zeta_1.
 \tag{CL7}
\]
Its transform is \((\pi\delta_0(\xi_1)-i\operatorname{pv}(1/\xi_1))\otimes1\). Multiplication gives \(\Phi\widehat\mu=1\) on the whole real frequency plane. Hence \(\operatorname{Char}\mu=\varnothing\), even in the directions \((0,\pm1)\), where \(\Phi\) itself is zero.

For \(v=\delta_{(0,0)}\), the output is \(\mu\). At the origin every nonzero covector belongs to \(\operatorname{WF}_A(v)\), by the support-normal theorem for an isolated support point. The convolution theorem therefore puts every one of them in \(\operatorname{WF}_A(\mu)\). At an interior point \((a,0)\), \(a>0\), the distribution is locally \(1\otimes\delta_0\), so the tensor rule and signed support normals give exactly
\[
 \operatorname{WF}_A(\mu)=
 \{(0,0;\xi_1,\xi_2):(\xi_1,\xi_2)\ne0\}
 \ \cup\
 \{(a,0;0,\xi_2):a>0,\ \xi_2\ne0\}.
 \tag{CL8}
\]
Outside this half-line support the kernel vanishes. This example requires the distributional product interpretation in (CL1).

![The half-line kernel and its complete unit covector directions at the endpoint and at an interior support point.](figures/primitive-kernel-and-covector-fibers.png)

*Figure 1.* Left: the exact spatial support \(\{x_1\ge0,x_2=0\}\) of \(H(x_1)\delta_0(x_2)\); the marked interior point is \((1,0)\). Middle: the full unit covector circle at the origin. Right: the two unit directions of the vertical covector line at \((1,0)\). The last two panels are cotangent fibers, with axes \((\xi_1,\xi_2)\), rather than spatial regions. The reciprocal \(i\zeta_1\) vanishes on both vertical directions, yet its distributional product with the kernel transform is one. Equation (CL8), the tensor rule and Theorem 4.1 prove the stated fibers.

### Example 3: a square-root reciprocal

Define a tempered kernel by
\[
 \widehat\mu(\xi)=(1+\xi^2)^{-1/2}.
 \tag{CL9}
\]
The bounded smooth function on the right defines a tempered distribution, so Fourier inversion defines \(\mu\). For \(|\zeta|>2\), set
\[
 S(\zeta)=\exp\!\left(\frac12\log(1+\zeta^{-2})\right),
 \qquad
 \Phi_+(\zeta)=\zeta S(\zeta),\quad
 \Phi_-(\zeta)=-\zeta S(\zeta).
 \tag{CL10}
\]
Here \(\log(1+w)=\sum_{k\ge1}(-1)^{k+1}w^k/k\) for \(|w|<1\). The convergent series gives \(S^2=1+\zeta^{-2}\). Choose the plus branch in the cone about the positive real ray and the minus branch about the negative ray. On each real ray the resulting value is the positive square root of \(1+\xi^2\), so (CL1) holds.

Since \(|\zeta^{-2}|<1/4\),
\[
 \frac{\sqrt3}{2}|\zeta|
       \le|\Phi_\pm(\zeta)|
       \le\frac{\sqrt5}{2}|\zeta|.
 \tag{CL11}
\]
Both rays are therefore outside \(\operatorname{Char}\mu\). These reciprocals are not polynomials: a polynomial whose square is \(1+\zeta^2\) would have degree one, but its leading, cross and constant coefficients cannot satisfy all three required identities.

The direct multiplier \((1+\xi^2)^{-1/2}\) also has a holomorphic polynomial bound in those cones. Its \(k\)-th real derivative has the form \(P_k(\xi)(1+\xi^2)^{-k-1/2}\), with \(\deg P_k\le k\): differentiation gives
\(P_{k+1}=(1+\xi^2)P_k'-(2k+1)\xi P_k\), starting from \(P_0=1\). Thus its fixed-order symbol estimates also hold. Theorem 2.1 applied to \(\delta_0\) gives \(\operatorname{WF}_A(\mu)\subset\operatorname{WF}_A(\delta_0)\). The reciprocal theorem with \(v=\delta_0\) gives the reverse inclusion. Thus its analytic wavefront is exactly both nonzero rays over the origin.

### Example 4: the Gaussian does erase the point singularity

Take
\[
 \mu(x)=(4\pi)^{-1/2}e^{-x^2/4},
 \qquad \widehat\mu(\xi)=e^{-\xi^2}.
 \tag{CL12}
\]
The Gaussian Fourier constant is proved in the linked Fourier foundation. Any holomorphic reciprocal near a real high-frequency ray must equal \(e^{\zeta^2}\) there: the product identity holds between functions, and the holomorphic identity theorem extends it locally. Already on the real ray its magnitude \(e^{\xi^2}\) exceeds every polynomial. Consequently every nonzero direction lies in \(\operatorname{Char}\mu\).

With \(v=\delta_0\), the output \(\mu*v=\mu\) is analytic everywhere while the input has both analytic singular directions at zero. The polynomial bound in (CL1) excludes precisely this attempted recovery.

![Complex frequency cones for the square-root reciprocal and real growth of that reciprocal compared with the Gaussian inverse.](figures/complex-cones-and-reciprocal-growth.png)

*Figure 2.* Left: the complex cones \(|\operatorname{Im}\zeta|<|\operatorname{Re}\zeta|/2\), outside the dashed circle \(|\zeta|=2\). The points \(\pm i\), marked by crosses, are the square-root branch points. The displayed Cauchy disks have centers \(\pm3,\pm6\) and radii \(3/4,3/2\), respectively; each lies inside the corresponding cone and outside the circle. Different signs in (CL10) give the positive real reciprocal on the two rays. Right: the exact logarithmic magnitudes \(\tfrac12\log(1+\xi^2)\) and \(\xi^2\) on the positive real axis. The dashed bound for \(\xi\ge2\) is \(\log(\sqrt5/2)+\log\xi\). Equations (CL10)–(CL12) prove the bounds and the failure for the Gaussian; the plotted interval illustrates those statements.

## 4. Exercises

1. **A causal primitive, 10 points.** Derive (CL5) with its signs and point term. Compute all four interval values and every jump of the output in (CL6).
2. **A distribution-valued transform, 12 points.** Prove that the kernel in (CL7) has empty convolution characteristic set, including the vertical frequency directions. Prove the exact analytic wavefront formula (CL8).
3. **Two square-root branches, 12 points.** Justify holomorphy, real-ray agreement and both bounds in (CL11). Prove that neither reciprocal is polynomial.
4. **The Gaussian obstruction, 12 points.** Prove \(\operatorname{Char}\mu=\mathbb R\setminus\{0\}\) for (CL12), and explain the convolution theorem at \(v=\delta_0\).
5. **Real-axis bounds are insufficient, 14 points.** Let \(\mu=\delta_h\) on the line, \(h\ne0\). Its real-axis reciprocal has magnitude one. Determine its convolution characteristic set under (CL1), and compare \(v=\delta_0\) with \(\mu*v\).
6. **The Taylor factor of \(i\), 12 points.** Verify (CE12) in one dimension. For \(a(\xi)=\xi^3\), express \(\widehat{\chi D^3f}\) in terms of the Fourier transforms of \(\chi f,\chi'f,\chi''f,\chi'''f\), with \(D=-i\partial\).
7. **One analytic scale, 14 points.** Track the largest cutoff derivative orders in the local products and the far Taylor polynomial terms when \(|\alpha|<K\). Explain why one fixed shift and \(J=4K\) suffice. Prove (CL4) for arbitrary fixed nonnegative integers \(B,c\).
8. **An input with arbitrary growth, 14 points.** Let \(\mu=H\) and \(v=H(x)e^{x^3}\). Prove properness, compute their convolution, and apply Corollary 4.2. Give the compact localization needed for outputs in \((-1,2)\), and prove that \(v\) is not tempered.

## 5. Complete solutions

### Solution 1

For \(\epsilon>0\), direct integration gives
\[
 \mathcal F(H e^{-\epsilon x})(\xi)
        =\int_0^\infty e^{-(\epsilon+i\xi)x}\,dx
        =-i(\xi-i\epsilon)^{-1}.
 \tag{CF1}
\]
The lower boundary formula is
\((\xi-i0)^{-1}=\operatorname{pv}(1/\xi)+i\pi\delta_0\).
Multiplication by \(-i\) gives (CL5). The convergence of \(H e^{-\epsilon x}\) to \(H\) on Schwartz tests follows from domination by the integrable absolute value of the test on the positive half-line. Fourier continuity passes this limit to the transforms. The identities \(\xi\delta_0=0\) and \(\xi\operatorname{pv}(1/\xi)=1\) give \(i\xi\widehat H=1\).

The intervals in (CL6) have values \(0\) for \(x<0\), \(1\) for \(0<x<1\), \(-1\) for \(1<x<3\), and \(0\) for \(x>3\). The jumps at \(0,1,3\) are \(1,-2,1\). The distributional derivative is therefore \(\delta_0-2\delta_1+\delta_3\). Values chosen exactly at the three endpoints do not change the associated distribution.

### Solution 2

The Fourier tensor identity gives
\[
 \widehat\mu=
  \bigl(\pi\delta_0(\xi_1)-i\operatorname{pv}(1/\xi_1)\bigr)
       \otimes1.
 \tag{CF2}
\]
Multiplication by \(i\xi_1\) gives \(1\otimes1\). The entire function \(i\zeta_1\) obeys \(|i\zeta_1|\le|\zeta|\) on every complex cone. The reciprocal criterion thus holds near every nonzero real frequency, including \(\xi_1=0\). A zero value of the multiplier on that hyperplane does not invalidate its product with the distributional principal value.

The point-mass input has every nonzero covector at the origin; Theorem 4.1 gives their presence in the output. For \(a>0\), the kernel is locally \(1\otimes\delta_0\). Analytic tensor estimates give only covectors \((0,\xi_2)\), and the supporting function \(x_2\), zero on its support, supplies both vertical signs. Off the half-line the kernel is zero. These three cases give (CL8).

### Solution 3

The logarithm series converges normally for \(|w|<1\), so its composition with \(\zeta^{-2}\), followed by the exponential, is holomorphic for \(|\zeta|>2\). Differentiating the logarithm series gives \((1+w)^{-1}\); hence \(\exp(\log(1+w))=1+w\), by differentiating their quotient and evaluating at zero. Thus \(S^2=1+\zeta^{-2}\). On the real rays the series is real and \(S\) is positive, giving the branch signs in (CL10).

For \(|\zeta|>2\), \(3/4<|1+\zeta^{-2}|<5/4\). Since \(|S|^2=|S^2|\), multiplication by \(|\zeta|\) gives (CL11). If a polynomial \(p=a\zeta+b\) had square \(1+\zeta^2\), coefficient comparison would require \(a^2=1\), \(2ab=0\), \(b^2=1\). The first and third make \(a,b\ne0\), contradicting the middle condition. Higher or lower polynomial degrees cannot have the required square degree. Agreement of a polynomial with either branch on an open set would force this same identity.

### Solution 4

On either real ray a reciprocal must satisfy \(\Phi(\xi)e^{-\xi^2}=1\). Both factors are analytic functions there, so \(\Phi(\xi)=e^{\xi^2}\). For every fixed \(m\), the positive exponential series gives \(e^{\xi^2}\ge|\xi|^{2k}/k!\) for any integer \(k\). Choose \(2k>m\); its ratio to \((1+|\xi|)^m\) is unbounded. No polynomial bound is possible on either ray, even before considering complex frequencies.

Therefore every nonzero direction is characteristic for this kernel. The output for a point mass is the analytic Gaussian, so its analytic wavefront is empty. Formula (CL2) places the point mass's singularities in the characteristic term, exactly as required.

### Solution 5

The transform of \(\delta_h\) is \(e^{-ih\xi}\). A reciprocal agreeing on a real interval must be \(e^{ih\zeta}\) on its local complex neighborhood, by the identity theorem. Every complex conic neighborhood of a real ray contains, for all sufficiently large real \(\xi\) in that ray, points
\[
 \zeta=\xi-i\,\operatorname{sgn}(h)d|\xi|
 \tag{CF3}
\]
with one fixed small \(d>0\). At these points \(|e^{ih\zeta}|=e^{|h|d|\xi|}\), which exceeds every polynomial. The real-axis bound of one therefore does not satisfy (CL1). Both rays are characteristic.

The point-mass input at zero is sent to the point mass at \(h\). The output is zero and hence analytic near zero, while the input is singular there. A rule using only a bounded real reciprocal would wrongly infer regularity at the unchanged base point. The complex polynomial condition correctly excludes this translation multiplier.

### Solution 6

The Fourier derivative rule gives
\(\widehat{\chi^{(\alpha)}}(\xi-\eta)
=i^\alpha(\xi-\eta)^\alpha\widehat\chi(\xi-\eta)\).
Since \((\eta-\xi)^\alpha=(-1)^\alpha(\xi-\eta)^\alpha\) and \((-1)/i=i\), the convolution pairing in (CE12) equals \(i^\alpha\widehat{\chi^{(\alpha)}f}(\xi)\).

The exact cubic Taylor formula now yields
\[
 \widehat{\chi D^3f}(\xi)
  =\xi^3\widehat{\chi f}(\xi)
    +3i\xi^2\widehat{\chi'f}(\xi)
    -3\xi\widehat{\chi''f}(\xi)
    -i\widehat{\chi'''f}(\xi).
 \tag{CF4}
\]
The coefficients are \(1,3,3,1\) before the successive powers \(1,i,-1,-i\). This identity can also be checked by the distributional product rule for \(D=-i\partial\).

### Solution 7

For a local product with \(|\alpha|<K\), its Fourier integration-by-parts order is \(s=K+q+n+1\), up to a fixed loss. The cutoff derivative order is \(|\alpha|+s\le2K+q+n\), up to that same fixed loss. In a far Taylor term the cutoff itself is undifferentiated before the Fourier moment estimate; its moment order is \(K+|\alpha|+q_1+c\le2K+q_1+c-1\). Derivatives from the fixed tempered seminorm add only fixed losses. A fixed shift makes \(K=N+B\) exceed all these losses, and \(4K\) then covers every required order. The high cutoff derivative contributes \(K^{|\alpha|}\), accompanied by \(|\xi|^{-|\alpha|}\); for \(|\xi|\ge K\) this creates no second analytic factorial scale.

For (CL4), divide the left side by \(N^N\):
\[
 \frac{(N+B)^{N+B+c}}{N^N}
   =(1+B/N)^N(N+B)^{B+c}
   \le e^B(N+B)^{B+c}.
 \tag{CF5}
\]
For \(N\ge1\), \(N+B\le(B+1)N\) and \(N\le2^N\). The last expression is at most
\(e^B(B+1)^{B+c}2^{(B+c)N}\), which is bounded by a fixed constant to the \(N+1\) power. This proves the estimate for all \(N\ge1\).

### Solution 8

Both supports are \([0,\infty)\). Pairs with sum in a compact output set satisfy \(0\le s,t\le\max(0,\sup O)\); the relevant closed subset of this bounded square is compact. Addition is proper.

For \(x>0\), the convolution is the ordinary finite integral, while for \(x<0\) it vanishes:
\[
 g(x)=H(x)\int_0^x e^{t^3}\,dt,\qquad
                 \partial_xg=H(x)e^{x^3}=v.
 \tag{CF6}
\]
There is no extra point mass in the derivative because the integral is zero at the origin. Both \(v\) and \(g\) are analytic off zero. They have support \([0,\infty)\); the signed support-normal theorem supplies both analytic rays at zero. Since \(\operatorname{Char}H=\varnothing\), Corollary 4.2 gives the asserted inclusion and, here, equality.

For outputs in \((-1,2)\), all contributing input times lie in \([0,2]\). Choose a smooth compact cutoff equal to one on a neighborhood of \([-1,2]\). Then \(v_c=\chi v\) agrees with \(v\) in that output interval and \(H*v_c=g\) there. This is the actual compact-input reduction.

To disprove temperedness of \(v\), take a fixed nonnegative compact bump \(\phi\) supported in \([0,1]\) with positive integral and translate it to \([R,R+1]\). Its pairing with \(v\) is at least \(e^{R^3}\int\phi\), while every fixed Schwartz seminorm of the translated bump grows at most polynomially in \(R\). No tempered distribution estimate can hold. The proper-support theorem nevertheless applies because it is local in the contributing input pairs.

## References

Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Theorem 8.6.15 and the proper-convolution remark, gives the classical context. The complete proof supplies the analytic multiplier estimate by finite Taylor expansion, Cauchy bounds and controlled cutoff moments. Its exact Fourier, cutoff and convolution dependencies are stated there; the examples and solutions above retain the same transform and derivative conventions.
