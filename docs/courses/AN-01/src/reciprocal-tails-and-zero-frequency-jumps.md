# Reciprocal tails and zero-frequency jumps

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

The Fourier transform records a reciprocal tail as a jump. If the two tail coefficients differ, a logarithm appears as well. We calculate the complete distributions, then recover every derivative jump associated with a finite signed-power expansion. Compact corrections change smooth terms, while a constant in physical space contributes a separate point mass.

Use \(Ff(\xi)=\int_{\mathbb R}e^{-ix\xi}f(x)\,dx\), \(G=(2\pi)^{-1}RF\) and \(R\phi(x)=\phi(-x)\), with complex bilinear pairings. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz estimates, inversion, compact-test density and the transposed identities \(F(u')=i\xi Fu\), \(F(xu)=i(Fu)'\). Write
\[
 p_N(\theta)=\max_{0\le r\le N}\sup_x(1+|x|)^N|\theta^{(r)}(x)|.
\]
Every tempered functional is bounded by one such seminorm. Strong convergence in \(\mathcal S'\) means uniform convergence on sets on which every \(p_N\) is bounded. A continuous linear test map sends such sets to bounded sets by its seminorm estimates. Its transpose is therefore strongly continuous; in particular this applies to \(F,G\), derivatives and fixed polynomial multipliers.

The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12 and 13.1–13.5, 13.7–13.10, supplies the calculus, exponential, logarithm, trigonometry, arctangent and smooth cutoffs. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16, supplies convergence, absolute Fubini and substitution. [U021](convolution-as-addition-of-supports.md), B0–B1, proves localization, compact-distribution pairing and its parameter estimates. [U046](spectral-gaps-and-explicit-fourier-distributions.md), §§1–3, supplies the whole constant, principal-value, sign and Cauchy transforms. The further arguments are given here.

## Integrable remainders and compact corrections

Let \(P=\operatorname{pv}(1/x)\). U046 defines it on Schwartz tests by the convergent integral \(\int_0^\infty[\theta(t)-\theta(-t)]\,dt/t\) and proves \(F(\operatorname{sgn})=-2iP\). Applying \(F\) and \(F^2=2\pi R\) gives
\[
 FP=-i\pi\operatorname{sgn}\xi.
 \tag{1.1}
\]
Indeed \(-2iFP=2\pi R(\operatorname{sgn})=-2\pi\operatorname{sgn}\). The same exact normalization gives \(F1=2\pi\delta_0\).

**Lemma 1.1 (integrable transforms and moments).** If \(h\in L^1(\mathbb R)\), its integral transform is bounded, continuous, and represents its entire distributional Fourier transform. If \(x^rh\in L^1\) for \(0\le r\le m\), then \(Fh\in C^m(\mathbb R)\), with
\[
 (Fh)^{(r)}(\xi)=\int_{\mathbb R}(-ix)^re^{-ix\xi}h(x)\,dx,
 \qquad 0\le r\le m.
 \tag{1.2}
\]
The inverse assertion holds with the positive phase and factor \(1/(2\pi)\).

**Proof.** Absolute integration gives \(|Fh|\le\|h\|_1\). For \(\xi_j\to\xi\), the integrands converge pointwise and are dominated by \(|h|\), so dominated convergence proves continuity. Against \(\theta\in\mathcal S\), the double absolute integral is at most \(\|h\|_1\|\theta\|_1\). Fubini therefore identifies the integral function with the transpose \(h(F\theta)\) on every Schwartz test.

The fundamental theorem gives \(|(e^{-ixt}-1)/t|\le |x|\) for \(t\ne0\). Thus a difference quotient of the order-\(r\) integral is dominated by \(|x|^{r+1}|h(x)|\). Induction and dominated convergence give every derivative in (1.2); continuity of each uses \(|x|^r|h|\) as its majorant. Replacing the phase by its conjugate and retaining the scalar factor proves the inverse statement. \(\square\)

**Proposition 1.2 (the full transform of a compact correction).** A compactly supported distribution \(V\) is tempered. Its entire Fourier transform is the smooth function
\[
 b_V(\xi)=V_x(e^{-ix\xi}),\qquad
 b_V^{(r)}(\xi)=V_x((-ix)^re^{-ix\xi}),
 \tag{1.3}
\]
where the pairing uses any compact cutoff equal to one near its support. For one integer \(N\), \(|b_V^{(r)}(\xi)|\le C_r(1+|\xi|)^N\) for every \(r\).

**Proof.** Choose that cutoff \(\eta\). U021 B0 proves that \(V(h)=V(\eta h)\) is independent of the cutoff and obeys a finite derivative estimate on its fixed compact support:
\[
 |V(h)|\le C\max_{j\le N}\sup_{x\in K}|(\eta h)^{(j)}(x)|.
\]
For \(h\in\mathcal S\), this is bounded by \(C'p_N(h)\), proving temperedness. A Taylor remainder in the parameter \(\xi\), after each of the finitely many required \(x\)-derivatives on \(K\), proves differentiation of \(V(\eta e^{-ix\xi})\). Equivalently this is the fully proved parameter rule in U021 B1. Repeating it gives (1.3). In a derivative of \(\eta(x)(-ix)^re^{-ix\xi}\), at most \(N\) derivatives hit the exponential; all other factors are bounded on \(K\). This gives the displayed growth bound, with the same \(N\) for all \(r\).

For \(\theta\in\mathcal S\), integrate first over \(|\xi|\le A\). Riemann sums for
\(\eta(x)\int_{-A}^Ae^{-ix\xi}\theta(\xi)\,d\xi\)
converge in every \(C^N(K)\) seminorm: differentiate in \(x\) and use uniform continuity on the compact \(x,\xi\) rectangle. Applying \(V\) commutes with those sums and their limits. The tails in each required seminorm are bounded by
\[
 C\int_{|\xi|>A}(1+|\xi|)^N|\theta(\xi)|\,d\xi\longrightarrow0.
\]
Thus the whole integral also passes through \(V\), and
\[
 V(F\theta)=\int_{\mathbb R}V(e^{-ix\xi})\theta(\xi)\,d\xi
           =\int_{\mathbb R}b_V(\xi)\theta(\xi)\,d\xi.
\]
This identifies the entire Fourier distribution, including at zero. \(\square\)

## A reciprocal tail leaves a jump

**Theorem 2.1.** Suppose \(f\in C(\mathbb R)\) and \(f(x)=a/x+O(|x|^{-2})\) as \(|x|\to\infty\), with the same signed reciprocal coefficient on both tails. Then \(Ff\) is a regular distribution represented by a function continuous off zero, with finite one-sided limits satisfying
\[
 Ff(+0)-Ff(-0)=-2\pi i a.
 \tag{2.1}
\]
More precisely, for \(h(x)=f(x)-ax/(1+x^2)\),
\[
 \begin{gathered}
 Ff(\xi)=-i\pi a\operatorname{sgn}\xi\,e^{-|\xi|}+Fh(\xi),\\
 Ff(\pm0)=\int_{\mathbb R}h(x)\,dx\mp i\pi a.
 \end{gathered}
 \tag{2.2}
\]

**Proof.** The identity \(x/(1+x^2)=x^{-1}-[x(1+x^2)]^{-1}\) gives an error \(O(|x|^{-3})\). Hence \(h=O(|x|^{-2})\) on both tails, and continuity makes it integrable on compact intervals. It is therefore in \(L^1\). The original \(f\) is bounded and defines a tempered regular distribution. U046 §2 proves the complete transform \(F[x/(1+x^2)]=-i\pi\operatorname{sgn}\xi\,e^{-|\xi|}\). Add the whole \(L^1\) transform from Lemma 1.1. Its value at zero is \(\int h\), so the two limits in (2.2) and their difference follow. Since both summands have been identified on all Schwartz tests, there is no additional point mass. \(\square\)

The two-sided assumption is essential. A prescribed positive reciprocal tail alone allows arbitrarily fast growth on the other half-line, as Solution 8 shows.

## Unequal tails leave a logarithm

Use the real half-line model \(q(x)=1_{[1,\infty)}(x)/x\). It is locally integrable and bounded, so tempered. Define the finite real constant
\[
 c_*=\int_0^1\frac{\cos t-1}{t}\,dt
          +\int_1^\infty\frac{\cos t}{t}\,dt.
 \tag{3.1}
\]
The first integrand is bounded in absolute value by \(t/2\), by two applications of the fundamental theorem. Integration by parts against the bounded primitive \(\sin t\) bounds the second integral's tail from \(A\ge1\) by \(2/A\).

**Lemma 3.1 (the whole one-sided reciprocal transform).** For \(\xi\ne0\), put
\[
 Q(\xi)=\lim_{A\to\infty}\int_1^A e^{-ix\xi}\frac{dx}{x}.
\]
It is continuous on each open half-line and locally integrable through zero. It represents the entire distribution \(Fq\), and
\[
 \lim_{s\downarrow0}\bigl(Q(\pm s)+\log s\bigr)
       =c_*\mp\frac{\pi i}{2}.
 \tag{3.2}
\]

**Proof: uniform tails and the distributional limit.** For \(\varepsilon>0\), let \(q_\varepsilon(x)=e^{-\varepsilon x}q(x)\). It is in \(L^1\), so its whole transform is the ordinary integral
\[
 Q_\varepsilon(\xi)=\int_1^\infty e^{-(\varepsilon+i\xi)x}\frac{dx}{x}.
\]
For a Schwartz test,
\[
 |(q_\varepsilon-q)(\theta)|
 \le p_2(\theta)\int_1^\infty
      \frac{|e^{-\varepsilon x}-1|}{x(1+x)^2}\,dx.
\]
The last integral tends to zero by dominated convergence. This proves strong convergence on every bounded Schwartz test set.

For \(z=\varepsilon+i\xi\), \(\xi\ne0\), integration by parts on a finite interval, followed by its upper-end limit, gives
\[
 \int_A^\infty\frac{e^{-zx}}x\,dx
 =\frac{e^{-zA}}{zA}
       -\frac1z\int_A^\infty\frac{e^{-zx}}{x^2}\,dx.
\]
This remains valid when \(\varepsilon=0\), since the omitted endpoint is \(O(1/A')\) at upper endpoint \(A'\). Consequently
\[
 \left|\int_A^\infty e^{-(\varepsilon+i\xi)x}\frac{dx}{x}\right|
       \le\frac{2}{|\xi|A},\qquad \varepsilon\ge0.
 \tag{3.3}
\]
For \(\varepsilon=0\) it proves existence of the oscillatory integral. On any compact set separated from \(\xi=0\), it controls tails uniformly, while the finite-interval integrals are continuous. It follows that \(Q\) is continuous there and \(Q_\varepsilon\to Q\) uniformly there.

If \(0<|\xi|\le1\), split at \(A=1/|\xi|\). The first integral is bounded by \(\log(1/|\xi|)\) and the tail by \(2\). If \(|\xi|\ge1\), use (3.3) at \(A=1\). Thus all \(Q_\varepsilon\) and \(Q\), except for their immaterial values at zero, obey
\[
 |Q_\varepsilon(\xi)|,\ |Q(\xi)|
 \le M(\xi):=
 \begin{cases}
 2+|\log|\xi||,&0<|\xi|\le1,\\
 2/|\xi|,&|\xi|\ge1.
 \end{cases}
\]
This is locally integrable: \(\int_0^1|\log s|\,ds=1\), by the primitive \(s\log s-s\) and its zero endpoint limit. Also \(M(\xi)(1+|\xi|)^{-2}\) is integrable on the whole line. Dominated convergence gives
\[
 \int_{\mathbb R}|Q_\varepsilon-Q|(1+|\xi|)^{-2}\,d\xi\longrightarrow0.
\]
This bounds the difference of the corresponding distribution pairings by that integral times \(p_2(\theta)\), so the convergence is strong in \(\mathcal S'\). Strong Fourier continuity also gives \(Fq_\varepsilon\to Fq\). Uniqueness of evaluations on each test proves \(Fq=Q\) as the full regular distribution.

**Proof: the exact endpoint constants.** For \(s>0\), substitute \(t=sx\). Then
\[
 \begin{aligned}
 \operatorname{Re}Q(\pm s)+\log s
 &=\int_s^1\frac{\cos t-1}{t}\,dt
       +\int_1^\infty\frac{\cos t}{t}\,dt,\\
 \operatorname{Im}Q(\pm s)
 &=\mp\int_s^\infty\frac{\sin t}{t}\,dt.
 \end{aligned}
\]
The first tends to \(c_*\). To compute the second limit without an external integral formula, use \(\sin t/t=\int_0^1\cos(\lambda t)\,d\lambda\). For \(\varepsilon>0\), the double absolute integral after multiplication by \(e^{-\varepsilon t}\) is at most \(1/\varepsilon\). Fubini and the elementary exponential primitive therefore give
\[
 \begin{aligned}
 \int_0^\infty e^{-\varepsilon t}\frac{\sin t}{t}\,dt
 &=\int_0^1\operatorname{Re}\frac1{\varepsilon-i\lambda}\,d\lambda\\
 &=\int_0^1\frac{\varepsilon}{\varepsilon^2+\lambda^2}\,d\lambda
 =\arctan(1/\varepsilon).
 \end{aligned}
\]
For \(a(t)=e^{-\varepsilon t}/t\), or \(a(t)=1/t\), the amplitude is decreasing to zero, and integration by parts against \(-\cos t\) gives
\[
 \left|\int_A^\infty a(t)\sin t\,dt\right|
 \le a(A)+\int_A^\infty|a'(t)|\,dt=2a(A)\le2/A.
\]
This tail estimate is uniform for \(\varepsilon\ge0\). On a finite interval the continuous extension of \(\sin t/t\) at zero gives dominated convergence. Taking first \(\varepsilon\downarrow0\), then \(A\to\infty\), proves the full integral equals \(\pi/2\). Its integral on \([0,s]\) tends to zero. Equation (3.2) follows, with both signs. \(\square\)

For comparison with the usual real sine and cosine integrals, define
\(\operatorname{Si}(s)=\int_0^s\sin t\,dt/t\) and
\(\operatorname{Ci}(s)=-\int_s^\infty\cos t\,dt/t\), \(s>0\).
The proof gives \(Q(\pm s)=-\operatorname{Ci}(s)\mp i[\pi/2-\operatorname{Si}(s)]\).
These definitions and normalization agree with [NIST DLMF §6.2(ii)](https://dlmf.nist.gov/6.2#ii), formulas 6.2.9–6.2.11 and 6.2.14. The convergence and \(\pi/2\) value required here have been proved above.

**Theorem 3.2 (different coefficients on the two tails).** Suppose \(f\in C(\mathbb R)\) satisfies \(f(x)=a_+/x+O(|x|^{-2})\) as \(x\to+\infty\) and \(f(x)=a_-/x+O(|x|^{-2})\) as \(x\to-\infty\). Put \(d=a_+-a_-\) and \(h=f-a_+q+a_-q(-\,\cdot\,)\). Then \(h\in L^1\), and
\[
 Ff(\xi)=a_+Q(\xi)-a_-Q(-\xi)+Fh(\xi)
 \tag{3.4}
\]
is the whole regular Fourier distribution. Its renormalized function \(g(\xi)=Ff(\xi)+d\log|\xi|\), \(\xi\ne0\), has the limits
\[
 \begin{gathered}
 g(\pm0)=dc_*+\int_{\mathbb R}h(x)\,dx
                    \mp\frac{\pi i}{2}(a_++a_-),\\
 g(+0)-g(-0)=-\pi i(a_++a_-).
 \end{gathered}
 \tag{3.5}
\]

**Proof.** On the positive tail the subtracted model is \(a_+/x\); on the negative tail the term \(-a_-q(-x)\) equals \(a_-/x\). Thus the remainder is \(O(|x|^{-2})\) on both ends, and is bounded on compact intervals except for harmless finite jumps at \(1,-1\). It is integrable. Fourier reflection, Lemma 3.1 and Lemma 1.1 give (3.4) on every Schwartz test. For \(\xi=\pm s\), Lemma 3.1 says \(Q(\pm s)=-\log s+c_*\mp\pi i/2+o(1)\). Substitute both signs into (3.4), and use \(Fh(0)=\int h\). This proves (3.5), including the logarithmic coefficient. No point-supported term can be appended to an identity already established on all tests. \(\square\)

Thus the difference of the physical coefficients controls the logarithm, while their sum controls the jump left after its subtraction. Equal coefficients give a jump without a logarithm; opposite coefficients give a logarithm without that residual jump.

## Higher powers determine derivative jumps

**Theorem 4.1 (every jump from a finite signed-power expansion).** For an integer \(k\ge1\), suppose \(f\in C(\mathbb R)\) has the same coefficients on both tails in
\[
 f(x)=a_0+\sum_{j=1}^k a_jx^{-j}+O(|x|^{-k-1}),
 \qquad |x|\to\infty.
 \tag{4.1}
\]
There is \(R\in C^{k-1}(\mathbb R)\) such that the whole transform is
\[
 Ff=2\pi a_0\delta_0+R(\xi)
     +\sum_{j=1}^k\frac{\pi i^{-j}a_j}{(j-1)!}
                       \xi^{j-1}\operatorname{sgn}\xi.
 \tag{4.2}
\]
After removing the displayed contact term, its regular part \(g\) has ordinary derivatives through order \(k-1\) on each open half-line, extending continuously to that side of zero, and
\[
 g^{(r)}(+0)-g^{(r)}(-0)=2\pi i^{-r-1}a_{r+1},
 \qquad 0\le r\le k-1.
 \tag{4.3}
\]

**Proof: construct exact models for all powers.** Define tempered distributions
\[
 P_j=\frac{(-1)^{j-1}}{(j-1)!}\partial_x^{j-1}P,\qquad j\ge1.
\]
On any open interval not containing zero, \(P\) equals the ordinary function \(1/x\). Integration by parts against a test supported in that interval shows that \(P_j\) equals \(x^{-j}\) there: induction differentiates \(1/x\) to \((-1)^{j-1}(j-1)!x^{-j}\). Using (1.1) and the full derivative transform identity gives
\[
 FP_j=\frac{\pi i^{-j}}{(j-1)!}
                    \xi^{j-1}\operatorname{sgn}\xi.
\]
The coefficient identity is
\((-1)^{j-1}i^{j-1}(-i)=i^{-j}\).
It follows directly from \(i^2=-1\), or by multiplying both sides by \(i^j\). These are entire regular Fourier distributions; multiplication by a polynomial preserves their meaning.

Choose a smooth even cutoff \(\chi\) equal to zero for \(|x|\le1\) and one for \(|x|\ge2\), and let \(q_j(x)=\chi(x)x^{-j}\), extended smoothly by zero near zero. The difference \(V_j=q_j-P_j\) vanishes on tests outside \([-2,2]\), so is compactly supported. Proposition 1.2 gives a globally smooth Fourier function \(b_j=FV_j\). Consequently
\[
 Fq_j=\frac{\pi i^{-j}}{(j-1)!}
                    \xi^{j-1}\operatorname{sgn}\xi+b_j.
\]
The remainder \(h=f-a_0-\sum_{j=1}^k a_jq_j\) is continuous and \(O(|x|^{-k-1})\) on both tails. For \(0\le r\le k-1\), \(x^rh\) is integrable, since the slowest resulting decay is \(|x|^{-2}\). Lemma 1.1 yields \(Fh\in C^{k-1}\). Define \(R=Fh+\sum_{j=1}^k a_jb_j\) and use \(F1=2\pi\delta_0\). This proves (4.2).

**Proof: read the endpoint derivatives.** On either half-line the sign is constant. The \(r\)-th derivative of \(\xi^{j-1}\) is zero if \(r>j-1\), and its endpoint limit is zero if \(r<j-1\). Only \(j=r+1\) remains, with right value \(r!\) and left value \(-r!\) after the sign is included. The \(C^{k-1}\) function \(R\) has identical derivative limits on both sides. Substitution of the coefficient in (4.2) therefore gives (4.3). This concerns ordinary derivatives on the half-lines. Distributional derivatives also retain the deltas induced by jumps. \(\square\)

If \(a_0\ne0\), the whole transform cannot itself be a locally integrable function. To check this last assertion, a hypothetical such representation, after subtracting the regular part of (4.2), would represent a nonzero multiple of \(\delta_0\) by \(w\in L^1_{\mathrm{loc}}\). Take a smooth compact \(\rho\) with \(\rho(0)=1\), and test with \(\rho(\xi/\varepsilon)\). Its delta pairing is one, whereas \(\int w(\xi)\rho(\xi/\varepsilon)\,d\xi\to0\) by integrability on shrinking neighborhoods. This is a contradiction.

## Exercises

**Exercise 1 (intermediate).** For \(f(x)=3+(2x+5)/(1+x^2)\), find the signed tail expansion through degree \(-3\) and the whole Fourier transform. After separating its point mass, calculate the first three derivative jumps, counting the function itself as order zero.

**Exercise 2 (intermediate).** Put \(v=x/(1+x^2)\). Compute \(F(xv)\) by distributionally differentiating \(Fv\), and verify every term using an algebraic identity for \(xv\).

**Exercise 3 (foundation).** Let \(h(x)=2(1-x^2)_+\), \(f(x)=2x/(1+x^2)+h(x)\). Give the entire regular transform and both endpoint limits at zero, including the continuous compact correction.

**Exercise 4 (advanced).** For \(f(x)=3x/(1+x^2)+2/\sqrt{1+x^2}\), calculate \(a_+,a_-\), the two limits of \(Ff(\xi)+4\log|\xi|\), and the exact integral of the remainder in Theorem 3.2.

**Exercise 5 (foundation).** Show with \(h=(1+x^2)^{-1}\) why \(O(|x|^{-2})\) decay alone does not imply \(Fh\in C^1\). Check the first absolute moment.

**Exercise 6 (advanced).** If \(f\) satisfies Theorem 3.2, calculate the full transform of \(v(x)=\lambda f(bx-c)+d_0\), for \(b>0\), \(c\in\mathbb R\), \(\lambda,d_0\in\mathbb C\). Find the renormalized limits of its regular part and their jump.

**Exercise 7 (intermediate).** For \(0<R<S\), put \(q_R(x)=1_{[R,\infty)}(x)/x\). Compute its whole transform and renormalized endpoint limits. Show that \(F(q_R-q_S)\) is continuous at zero and find its value.

**Exercise 8 (advanced).** Construct a smooth function equal to \(2/x\) for all sufficiently large positive \(x\), whose compact-test distribution has no tempered extension. Prove this using translates of one nonnegative test.

## Solutions

**Solution 1.** The finite geometric identity with its remainder gives
\[
 f(x)=3+2x^{-1}+5x^{-2}-2x^{-3}+O(|x|^{-4}).
\]
Thus \((a_0,a_1,a_2,a_3)=(3,2,5,-2)\). U046's full Cauchy and constant identities give
\[
 Ff=6\pi\delta_0+\pi(5-2i\operatorname{sgn}\xi)e^{-|\xi|}.
\]
Write the regular part as \(g\). On the right its \(r\)-th derivative at zero is \(\pi(5-2i)(-1)^r\); on the left it is \(\pi(5+2i)\). At orders \(0,1,2\) their differences are respectively \(-4\pi i,-10\pi,-4\pi i\). Substitution into (4.3) gives the same three values, including \(i^{-3}=i\) at the last one.

**Solution 2.** The regular function \(Fv=-i\pi\operatorname{sgn}\xi\,e^{-|\xi|}\) has ordinary derivative \(i\pi e^{-|\xi|}\) away from zero and jump \(-2\pi i\) at zero. For a compact test, integration by parts on the two half-lines produces the boundary contribution equal to the jump times \(\theta(0)\). Thus
\[
 (Fv)'=i\pi e^{-|\xi|}-2\pi i\delta_0,\qquad
 F(xv)=i(Fv)'=-\pi e^{-|\xi|}+2\pi\delta_0.
\]
The identity \(xv=1-(1+x^2)^{-1}\) confirms both terms. In particular differentiating only the ordinary half-line values would lose the physical constant one.

**Solution 3.** Let \(J(\xi)=\int_{-1}^1e^{-ix\xi}\,dx=2\sin\xi/\xi\), with its integral value at zero. Differentiation under this compact integral gives \(Fh=2(J+J'')\). For \(\xi\ne0\), direct differentiation yields
\[
 J''=2\left(-\frac{\sin\xi}{\xi}
            -\frac{2\cos\xi}{\xi^2}
            +\frac{2\sin\xi}{\xi^3}\right),
\]
so \(Fh=8(\sin\xi-\xi\cos\xi)/\xi^3\). At zero its compact integral gives \(Fh(0)=2\int_{-1}^1(1-x^2)\,dx=8/3\), establishing the removable value independently of this quotient. Therefore
\[
 Ff(\xi)=-2\pi i\operatorname{sgn}\xi\,e^{-|\xi|}
                 +8\frac{\sin\xi-\xi\cos\xi}{\xi^3}.
\]
Its right and left limits are \(8/3-2\pi i\) and \(8/3+2\pi i\); the jump is \(-4\pi i\). Both summands are the full regular distributions.

**Solution 4.** Since \((1+x^2)^{-1/2}=|x|^{-1}+O(|x|^{-3})\), the signed coefficients are \(a_+=5\), \(a_-=1\). Thus \(d=4\) and \(a_++a_-=6\). The remainder in Theorem 3.2 decomposes as
\[
 \begin{aligned}
 h={}&3\left(\frac{x}{1+x^2}-q(x)+q(-x)\right)\\
 &+2\left(\frac1{\sqrt{1+x^2}}-q(x)-q(-x)\right).
 \end{aligned}
\]
Both brackets are integrable, with \(O(|x|^{-3})\) tails. The first is odd and has integral zero. The second is even. The chain rule verifies that \(A(x)=\log(x+\sqrt{1+x^2})\), \(x\ge0\), has derivative \(1/\sqrt{1+x^2}\), with \(A(0)=0\). Also \(A(x)-\log x=\log(1+\sqrt{1+x^{-2}})\to\log2\). Hence
\[
 \int_{\mathbb R}h
 =4\lim_{M\to\infty}\left(\int_0^M\frac{dx}{\sqrt{1+x^2}}
                             -\int_1^M\frac{dx}{x}\right)
 =4\log2.
\]
The whole transform is \(5Q(\xi)-Q(-\xi)+Fh(\xi)\). Its renormalized limits are \(4c_*+4\log2\mp3\pi i\); their difference is \(-6\pi i\).

**Solution 5.** Here \(Fh=\pi e^{-|\xi|}\). It is continuous, but its right derivative at zero is \(-\pi\), its left derivative is \(\pi\), so it is not \(C^1\). Meanwhile
\[
 \int_{\mathbb R}|x|h(x)\,dx
 =2\int_0^\infty\frac{x}{1+x^2}\,dx=\infty,
\]
as follows from the primitive \(\tfrac12\log(1+x^2)\). The weighted hypothesis needed for one absolutely justified Fourier derivative fails.

**Solution 6.** Set \(d=a_+-a_-\), \(s=a_++a_-\) and \(L_\pm=dc_*+\int h\mp\pi i s/2\). Affine substitution in the Fourier test identity, with positive Jacobian \(b^{-1}\), gives
\[
 Fv(\xi)=\frac{\lambda}{b}e^{-ic\xi/b}Ff(\xi/b)
                         +2\pi d_0\delta_0.
\]
This is a whole distributional equality by transposition, even though \(f\) need not be integrable. Denote its regular summand by \(w\). Formula (3.5) says
\[
 Ff(\xi/b)=-d\log|\xi|+d\log b+L_\pm+o(1)
 \quad(\xi\to\pm0).
\]
The exponential difference \(e^{-ic\xi/b}-1\) is \(O(|\xi|)\) by the fundamental theorem. Also \(\tau|\log\tau|\to0\) as \(\tau\downarrow0\): for \(0<\tau\le1\), the integral bound \(\log(1/\tau)\le2\tau^{-1/2}\) gives \(\tau|\log\tau|\le2\sqrt\tau\). Thus the phase affects neither limit, and
\[
 \lim_{\xi\to\pm0}\left(w(\xi)+\frac{\lambda d}{b}\log|\xi|\right)
       =\frac{\lambda}{b}(L_\pm+d\log b).
\]
Their difference is \(-\lambda\pi i s/b\). The regular part has physical reciprocal coefficients \(\lambda a_\pm/b\), consistent with this compensating logarithm. If \(\lambda=0\), both limits are zero and the contact term \(2\pi d_0\delta_0\) remains.

**Solution 7.** Since \(q_R(x)=R^{-1}q(x/R)\), positive scaling in the transposed Fourier identity gives \(Fq_R(\xi)=Q(R\xi)\) on all tests. Therefore
\[
 \lim_{\xi\to\pm0}\bigl(Fq_R(\xi)+\log|\xi|\bigr)
       =c_*-\log R\mp\pi i/2.
\]
The difference \(q_R-q_S\) equals \(1_{[R,S)}(x)/x\) almost everywhere. It is integrable, so its entire transform is the continuous function \(\int_R^S e^{-ix\xi}\,dx/x\), whose value at zero is \(\log(S/R)\). Subtracting the two endpoint formulas gives the same value; both singular terms cancel.

**Solution 8.** Choose smooth \(0\le\chi_\pm\le1\), with \(\chi_-=1\) on \(x\le-2\), \(\chi_-=0\) on \(x\ge-1\), and \(\chi_+=0\) on \(x\le1\), \(\chi_+=1\) on \(x\ge2\). Set
\[
 f(x)=\chi_-(x)e^{-x}+2\chi_+(x)/x,
\]
extending the last term by zero for \(x\le1\). It is smooth since that term vanishes on a neighborhood of zero and the cutoff is smooth across \(1\). It is nonnegative and equals \(2/x\) for \(x\ge2\).

Fix a nonnegative nonzero \(\rho\in C_c^\infty((-1/10,1/10))\) and let \(\theta_A(x)=\rho(x+A)\), \(A>3\). Its support lies in the region where \(f=e^{-x}\), so
\[
 f(\theta_A)\ge e^{A-1/10}\int\rho.
\]
For each fixed \(N\), \(p_N(\theta_A)\le C_N(1+A)^N\), since all derivatives of the bump are fixed and only its location changes. A tempered extension would bound the displayed pairings by \(Cp_N(\theta_A)\) for some fixed \(N\). This is impossible: the exponential series, using a term of degree greater than \(N\), proves \(e^A/(1+A)^N\to\infty\). Thus the compact-test distribution has no tempered extension.

## References

- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), author-hosted edition dated 2 October 2026, §11.2.3, Proposition 11.26. Its complete compact-distribution Fourier proof was read and compared; Proposition 1.2 above supplies the finite-order bounds, parameter derivatives and the full integral-pairing argument locally.
- [NIST Digital Library of Mathematical Functions, §6.2(ii)](https://dlmf.nist.gov/6.2#ii), real sine and cosine integral definitions and normalization. Lemma 3.1 proves all convergence, endpoint constants and distributional identification used here directly; no complex branch formula or identification of \(c_*\) with another constant is required.
- U021 B0–B1, U046 §§1–3 and the supplied foundations are linked at their points of use. The scalar and integration foundations retain their CC0 1.0 notices. The reconstructed exposition, local proofs and solutions are CC0.
