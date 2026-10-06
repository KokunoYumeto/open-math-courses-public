# Rational spectra and origin matching

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

Two exact calculations connect complex functions with distributions. An analytic function around a circle gives an integer spectrum, with geometric decay in both frequency directions. A bounded phase on the frequency line gives every tempered solution of an equation singular at the physical origin. In the second calculation, the behavior at both frequency endpoints determines the physical traces, while a point mass is needed even when those traces are finite.

We use \(Ff(\xi)=\int e^{-ix\xi}f(x)\,dx\), inverse \(G=(2\pi)^{-1}RF\), and reflection \(R\phi(x)=\phi(-x)\), with bilinear complex pairings. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves inversion, the transpose construction, compact-test density and
\[
 F(u')=i\xi Fu,\qquad F(xu)=i(Fu)',\qquad
 F\delta_0=1,\quad F1=2\pi\delta_0.
\]
The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12 and 13.1–13.5, 13.7–13.10, supplies compactness, calculus, smooth cutoffs, geometric and exponential series, trigonometry and arctangent. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, supplies convergence, absolute Fubini and convergence of mollifiers in \(L^1\). [U013](cauchy-kernels-and-boundary-limits.md), §1 and Theorem 1.1, supplies complex Green and the full Cauchy–Pompeiu formula. [U049](reciprocal-tails-and-zero-frequency-jumps.md), Lemma 1.1, supplies the whole inverse transform of an integrable function.

For estimates put
\[
 p_N(\theta)=\max_{0\le j\le N}
             \sup_x(1+|x|)^N|\theta^{(j)}(x)|.
\]
These seminorms define the Schwartz topology: expand the integer weight to compare it with monomial weights, and bound each monomial by that weight. Every continuous tempered functional has one bound \(Cp_N\). A bounded Schwartz test family has all \(p_N\) uniformly bounded. Strong dual convergence means uniform convergence on every such family. Test-map seminorm estimates show that continuous linear maps carry bounded families to bounded families; their transposes therefore preserve strong convergence.

## An analytic collar controls both frequency directions

Here analytic means locally represented by a convergent complex power series. Differentiating on smaller disks is justified by the differentiated geometric majorants; hence such functions are smooth and have \(\partial_{\bar z}f=0\).

**Theorem 1.1.** Suppose \(f\) is analytic on an open neighborhood of the unit circle. Choose \(0<r<1<R\) so that it is analytic on a neighborhood of the closed annulus \(r\le |z|\le R\). For each integer \(k\), define the counterclockwise contour integral
\[
 c_k=\frac1{2\pi i}\int_{|z|=\rho}f(z)z^{-k-1}\,dz,
 \qquad r\le\rho\le R.
 \tag{1.1}
\]
It is independent of \(\rho\). If \(v(x)=f(e^{ix})\), then
\[
 Fv=2\pi\sum_{k\in\mathbb Z}c_k\delta_k
 \tag{1.2}
\]
on the whole Schwartz space. The point series converges strongly, and its support is exactly \(\{k\in\mathbb Z:c_k\ne0\}\). The physical series \(v(x)=\sum_kc_ke^{ikx}\) converges uniformly together with every ordinary derivative. With \(M_\rho=\max_{|z|=\rho}|f(z)|\),
\[
 |c_k|\le M_RR^{-k}\quad(k\ge0),\qquad
 |c_{-\ell}|\le M_rr^\ell\quad(\ell\ge1).
 \tag{1.3}
\]

**Proof: the contour coefficients.** Compactness gives a uniform collar. Explicitly, finitely many disks whose doubled radii remain in the given open set cover the circle by their smaller disks; the minimum smaller radius gives a positive neighborhood of the circle still inside that set. For \(z\ne0\), its distance to the circle is \(||z|-1|\), by the triangle inequality and the point \(z/|z|\). Smaller positive inner and outer radii thus give the stated closed annulus.

Parameterize (1.1) by \(z=\rho e^{it}\), \(0\le t\le2\pi\):
\[
 c_k(\rho)=\frac1{2\pi}\int_0^{2\pi}
                  f(\rho e^{it})\rho^{-k}e^{-ikt}\,dt.
\]
The derivative of this integrand with respect to \(\rho\) is
\[
 \rho^{-k-1}\bigl(\rho e^{it}f'(\rho e^{it})-kf(\rho e^{it})\bigr)e^{-ikt}
 =\frac{\rho^{-k-1}}i
             \partial_t\bigl(f(\rho e^{it})e^{-ikt}\bigr).
\]
Differentiation passes through the compact integral by uniform continuity of the derivative. Its integral is zero because \(k\) is an integer and the endpoint values agree. The fundamental theorem proves radius independence. The parameterized formula bounds its modulus by \(M_\rho\rho^{-k}\), giving (1.3) at \(R\) and \(r\).

**Proof: recover the analytic function.** Choose a smooth radial cutoff equal to one near the closed annulus and supported in a slightly larger annulus where \(f\) is defined. Its product with \(f\), extended by zero, is an admissible compact smooth function for U013 Theorem 1.1. On \(r<|w|<R\) the \(\partial_{\bar w}\) term vanishes. The outer boundary has positive counterclockwise orientation and the inner boundary the opposite orientation. Consequently
\[
 f(z)=\frac1{2\pi i}\int_{|w|=R}\frac{f(w)}{w-z}\,dw
       -\frac1{2\pi i}\int_{|w|=r}\frac{f(w)}{w-z}\,dw,
 \quad r<|z|<R.
 \tag{1.4}
\]
On the outer circle expand \((w-z)^{-1}=\sum_{j\ge0}z^jw^{-j-1}\). On the inner circle it equals \(-\sum_{j\ge0}w^jz^{-j-1}\). The ratios \(|z|/R\) and \(r/|z|\) are strictly below one uniformly when \(z\) lies in a compact subannulus. Uniform geometric tails permit integration term by term. Radius independence identifies the outer terms with \(c_jz^j\) and the inner terms, including its preceding minus sign, with \(c_{-j-1}z^{-j-1}\). Thus \(f(z)=\sum_{k\in\mathbb Z}c_kz^k\).

For every integer \(p\ge0\), (1.3) makes \(\sum_k(1+|k|)^p|c_k|\) finite: for \(0<t<1\), the ratio of successive terms \(k^pt^k\) tends to \(t\), so a fixed geometric bound controls its tail. The physical series and each differentiated series therefore converge uniformly. To justify differentiation, apply the finite-sum fundamental theorem on any bounded interval and pass to both uniform limits. Induct on the derivative order. The zeroth limit is \(f(e^{ix})\) by the annular expansion.

**Proof: the whole spectrum and exact support.** Put \(v_N=\sum_{|k|\le N}c_ke^{ikx}\) and \(T_N=\sum_{|k|>N}|c_k|\). Uniform convergence gives
\[
 |(v-v_N)(\theta)|\le T_N\|\theta\|_1\le2T_Np_2(\theta).
\]
Hence \(v_N\to v\) strongly in \(\mathcal S'\). For each real \(k\), Fourier inversion on tests gives
\[
 F(e^{ikx})(\theta)=\int e^{ikx}F\theta(x)\,dx
                   =2\pi\theta(k).
\]
The series \(D(\theta)=2\pi\sum_kc_k\theta(k)\) is absolutely convergent, is bounded by \(2\pi p_0(\theta)\sum|c_k|\), and its tail is bounded by \(2\pi T_Np_0(\theta)\). It is therefore a tempered distribution and the finite point sums converge to it strongly. Strong Fourier continuity identifies \(Fv=D\), proving (1.2).

The nonzero-coefficient set is a closed subset of the integers: in every bounded interval it is finite. A compact test supported off that set pairs to zero with \(D\). If \(c_j\ne0\), choose, in any neighborhood of \(j\), a smooth test equal to one at \(j\) and supported within distance less than \(1/2\) of it. Its pairing is \(2\pi c_j\ne0\). This proves the exact support assertion. \(\square\)

For a concrete spectrum in both directions, consider
\[
 f(z)=\frac{z}{(2z-1)(z-2)}
     =-\frac1{3(2z-1)}+\frac2{3(z-2)}.
\]
On \(1/2<|z|<2\), the two geometric expansions are
\[
 \frac1{2z-1}=\sum_{\ell\ge1}2^{-\ell}z^{-\ell},
 \qquad
 \frac1{z-2}=-\frac12\sum_{j\ge0}2^{-j}z^j.
\]
They give \(c_k=-2^{-|k|}/3\), including \(k=0\), and hence
\[
 F[f(e^{ix})]=-\frac{2\pi}{3}
                \sum_{k\in\mathbb Z}2^{-|k|}\delta_k.
 \tag{1.5}
\]
Its support is all integers. At \(x=0\), the physical series is
\(-\tfrac13(1+2\sum_{j\ge1}2^{-j})=-1=f(1)\), checking the central coefficient as well as both tails.

## Frequency endpoints decide the origin traces

We first supply the distributional fact needed to solve the transformed equation.

**Lemma 2.0 (a zero derivative).** If \(T\in\mathcal D'(\mathbb R)\) and \(T'=0\), then \(T\) is a constant regular distribution.

**Proof.** Fix \(\rho\in C_c^\infty(\mathbb R)\) with \(\int\rho=1\). For any compact smooth test \(\phi\), put
\[
 \psi(x)=\int_{-\infty}^x
             \left(\phi(t)-\rho(t)\int\phi\right)\,dt.
\]
The integrand is smooth and compactly supported, and has total integral zero. Therefore \(\psi\) vanishes both below and above a compact interval containing those supports. It is a compact smooth test and \(\psi'=\phi-\rho\int\phi\). It follows that
\(T(\phi)-T(\rho)\int\phi=T(\psi')=-T'(\psi)=0\).
Thus \(T=T(\rho)\) as distributions. \(\square\)

For a smooth multiplier \(M\), the product rule also follows directly from tests:
\[
 (MT)'(\phi)=-T(M\phi'),\qquad
 (MT'+M'T)(\phi)=-T((M\phi)')+T(M'\phi).
\]
The right sides agree. These operations are defined in \(\mathcal D'\) without any growth assumption on \(M\).

**Theorem 2.1.** For every \(a\in\mathbb C\), all tempered solutions of
\[
 L_au:=xu''+2u'+(a-x)u=0
 \tag{2.1}
\]
are given by
\[
 Fu(\xi)=C e^{-ia\arctan\xi},\qquad C\in\mathbb C.
 \tag{2.2}
\]
This solution space is one dimensional. A nonzero solution has a finite trace on either open side of zero if and only if \(a\in2\mathbb Z\); in that case both traces exist.

For \(m\ge1\), define
\[
 p_m(x)=\sum_{j=1}^m{m\choose j}(-1)^{m-j}2^j
                         \frac{x^{j-1}}{(j-1)!}.
\]
The solutions normalized by \(Fu(0)=1\) are
\[
 \begin{aligned}
 u_{2m}&=(-1)^m\delta_0+H(x)e^{-x}p_m(x),\\
 u_{-2m}&=(-1)^m\delta_0+H(-x)e^xp_m(-x),\\
 u_0&=\delta_0.
 \end{aligned}
 \tag{2.3}
\]
Here \(H=1_{(0,\infty)}\), whose value at zero is immaterial. The finite traces of these normalized solutions are
\[
 \begin{aligned}
 u_{2m}(+0)&=2m(-1)^{m-1},&u_{2m}(-0)&=0,\\
 u_{-2m}(+0)&=0,&u_{-2m}(-0)&=2m(-1)^{m-1},\\
 u_0(+0)&=0,&u_0(-0)&=0.
 \end{aligned}
 \tag{2.4}
\]
Traces refer to the regular restrictions on the punctured half-lines; they do not discard the point masses in (2.3).

**Proof: solve the equation on the entire frequency line.** Write \(U=Fu\). The supplied Fourier rules and the distributional product rule give
\[
 F(xu'')=-i\xi^2U'-2i\xi U,\quad
 F(2u')=2i\xi U,\quad F((a-x)u)=aU-iU'.
\]
The two terms linear in \(\xi U\) cancel. Since \(1+\xi^2\) never vanishes, the equation in \(\mathcal D'\) is equivalent to
\[
 -i(1+\xi^2)U'+aU=0,\qquad
 U'=-\frac{ia}{1+\xi^2}U.
 \tag{2.5}
\]
Set \(A(\xi)=\arctan\xi\), \(M_a=e^{iaA}\), and \(W_a=M_a^{-1}\). Multiplication and the just-proved product rule show \((M_aU)'=0\). Lemma 2.0 implies \(M_aU=C\), hence \(U=CW_a\) on all compact tests.

This candidate is tempered. Indeed \(|W_a|,|M_a|\le e^{|\operatorname{Im}a|\pi/2}\). All their derivatives are bounded too. To see this explicitly, for \(j\ge1\) one has
\[
 A^{(j)}(\xi)=\frac{P_{j-1}(\xi)}{(1+\xi^2)^j},
 \qquad \deg P_{j-1}\le j-1.
\]
The assertion starts with \(A'=(1+\xi^2)^{-1}\); differentiating gives
\(P_j=(1+\xi^2)P_{j-1}'-2j\xi P_{j-1}\), proving it by induction. Each derivative is bounded, since its rational expression is continuous and bounded at infinity. Repeated product and chain rules express every derivative of \(W_a\) or \(M_a\) as the same bounded exponential times a finite sum of products of these derivatives. Leibniz thus gives \(p_N(M_a\theta),p_N(W_a\theta)\le C_{N,a}p_N(\theta)\).

In particular \(CW_a\) is a bounded regular tempered distribution and satisfies (2.5). Its inverse Fourier transform is a solution. Compact-test density in the Schwartz space identifies the original \(U\) with this tempered candidate on every Schwartz test. Fourier inversion gives uniqueness for each \(C\), and \(W_a(0)=1\) makes the parameter nondegenerate.

**Proof: determine when traces can be finite.** The ordinary derivative \(U'=-iaCW_a/(1+\xi^2)\) is integrable. U049 Lemma 1.1 gives a bounded continuous entire inverse transform \(b=GU'\). The inverse derivative identity gives \(b=-ixu\), and the fundamental theorem on finite intervals, followed by the integrable tails, gives
\[
 \begin{aligned}
 b(0)&=\frac1{2\pi}\int_{\mathbb R}U'(\xi)\,d\xi\\
 &=\frac C{2\pi}\left(e^{-ia\pi/2}-e^{ia\pi/2}\right)
 =-\frac{iC}{\pi}\sin(\pi a/2).
 \end{aligned}
 \tag{2.6}
\]
On either half-line, multiplication by \(1/x\) is smooth, so \(u=ib(x)/x\) there as a continuous regular distribution. If either trace is finite, \(b(x)=-ixu(x)\) tends to zero on that side; continuity forces \(b(0)=0\). For \(C\ne0\), (2.6) then gives \(\sin(\pi a/2)=0\). From the exponential definition, \(\sin z=0\) is equivalent to \(e^{2iz}=1\). Its modulus first implies \(\operatorname{Im}z=0\), and the real trigonometric periods then imply \(z\in\pi\mathbb Z\). Thus \(a\in2\mathbb Z\). Conversely, if \(a\notin2\mathbb Z\), the nonzero limit of \(xu(x)=ib(x)\) excludes each finite trace.

**Proof: invert every permitted rational phase.** For real \(\xi=\tan t\), \(-\pi/2<t<\pi/2\), the exponential formulas for sine and cosine give
\[
 e^{-2it}=\frac{\cos t-i\sin t}{\cos t+i\sin t}
         =\frac{1-i\xi}{1+i\xi}
         =-1+\frac2{1+i\xi}.
\]
The finite binomial formula consequently gives
\[
 W_{2m}(\xi)-(-1)^m
   =\sum_{j=1}^m{m\choose j}(-1)^{m-j}
                         \frac{2^j}{(1+i\xi)^j}.
 \tag{2.7}
\]
Let \(g_j(x)=H(x)e^{-x}x^{j-1}/(j-1)!\). It is integrable: each fixed polynomial times \(e^{-x/2}\) is bounded on the positive half-line, as follows from the exponential series, leaving an integrable \(e^{-x/2}\) majorant. Put \(z=1+i\xi\). The exponential primitive gives \(\int_0^\infty e^{-zx}\,dx=z^{-1}\). Integration by parts for \(j>1\), whose zero endpoint vanishes and whose infinite endpoint vanishes by the same majorant, gives the recurrence
\[
 \int_0^\infty e^{-zx}\frac{x^{j-1}}{(j-1)!}\,dx
 =z^{-1}\int_0^\infty e^{-zx}\frac{x^{j-2}}{(j-2)!}\,dx.
\]
Induction and the full integrable-transform identity yield
\[
 F\left(H(x)e^{-x}\frac{x^{j-1}}{(j-1)!}\right)
          =(1+i\xi)^{-j}.
 \tag{2.8}
\]
Combining (2.7), (2.8), \(G1=\delta_0\), and Fourier inversion proves the first whole-line formula (2.3). The identity \(W_{-2m}(\xi)=W_{2m}(-\xi)\) and Fourier reflection give the second; reflection leaves \(\delta_0\) unchanged. For \(a=0\), \(W_0=1\). Finally \(p_m(0)=2m(-1)^{m-1}\), since only \(j=1\) survives, so the explicit profiles give all limits in (2.4). \(\square\)

**The origin cancellation.** For a function \(v\) smooth on each closed half-line near zero, write \([v]=v(+0)-v(-0)\). Integration by parts on each side gives
\[
 v'=v'_{\rm sides}+[v]\delta_0,\qquad
 v''=v''_{\rm sides}+[v']\delta_0+[v]\delta'_0.
\]
For every \(j\ge1\), the test identity
\((x\delta_0^{(j)})(\theta)=(-1)^j(x\theta)^{(j)}(0)\)
gives \(x\delta_0^{(j)}=-j\delta_0^{(j-1)}\), and \(x\delta_0=0\). Therefore the contact contribution of \(xv''+2v'\) is \([v]\delta_0\), and
\[
 L_a\delta_0=a\delta_0.
\]
For the positive profile in (2.3), its jump is \(2m(-1)^{m-1}\), which cancels \(2m(-1)^m\) from the point mass. For the reflected profile the jump changes sign and \(a=-2m\), again giving cancellation. Fourier uniqueness already classified every tempered distribution, so it also excludes any omitted point derivatives. At parameter zero the pure point mass remains a nonzero solution.

## Exercises

**Exercise 1 (foundation).** On \(1/5<|z|<3\), take \(f(z)=(1-z/3)^{-1}+(1-(5z)^{-1})^{-1}-1\). Determine every coefficient, the full Fourier transform of \(f(e^{ix})\), its mean over a period, and its value at \(x=0\).

**Exercise 2 (intermediate).** Let \(v(x)=e^{2ix}+e^{-3ix}\) and \(w(x)=e^{7ix}v(2x-\pi/6)\). Find both entire spectra with their phase coefficients, and explain why no dilation factor remains on the final point masses.

**Exercise 3 (advanced).** In Theorem 1.1, show that the negative coefficients all vanish exactly when the annular function extends holomorphically to a neighborhood of the closed unit disk.

**Exercise 4 (intermediate).** For \(N\ge0\), give explicit uniform bounds on the error of the truncation \(\sum_{|k|\le N}c_ke^{ikx}\) and its first derivative. Deduce quantitative strong convergence of the physical distributions and their Fourier transforms.

**Exercise 5 (intermediate).** For \(a=6\), find the solution normalized by \(Fu(0)=1\), its two traces, and the complete cancellation at zero. Verify the ordinary equation on its nonzero half-line directly.

**Exercise 6 (intermediate).** Do the corresponding computation for \(a=-4\), retaining the sign of the reflected jump.

**Exercise 7 (advanced).** For \(a=2+i\) and \(Fu(0)=1\), compute the limit of \(xu(x)\) from both punctured sides and decide whether either trace of \(u\) can be finite.

**Exercise 8 (advanced).** Can a nonzero tempered solution of (2.1) be represented globally by a locally integrable function with finite traces? Decide also whether removing the trace requirement changes the answer. Explain the role of temperedness using \(v(x)=\sinh x/x\), with its removable value at zero.

## Solutions

**Solution 1.** Expanding the two geometric series gives
\[
 f(z)=1+\sum_{j\ge1}3^{-j}z^j+\sum_{\ell\ge1}5^{-\ell}z^{-\ell}.
\]
Thus \(c_0=1\), \(c_j=3^{-j}\) for \(j\ge1\), and \(c_{-\ell}=5^{-\ell}\) for \(\ell\ge1\). The complete transform is
\[
 2\pi\delta_0+2\pi\sum_{j\ge1}3^{-j}\delta_j
                  +2\pi\sum_{\ell\ge1}5^{-\ell}\delta_{-\ell},
\]
strongly convergent with support all integers. Uniform convergence permits integration over a period. The elementary exponential primitive makes every nonconstant integer wave have zero integral, so the mean is one. At zero, the series gives \(1+1/2+1/4=7/4\). Directly, \(f(1)=3/2+5/4-1=7/4\).

**Solution 2.** The plane-wave identity in Theorem 1.1 gives \(Fv=2\pi(\delta_2+\delta_{-3})\). Substitution before transforming gives
\[
 w(x)=e^{-i\pi/3}e^{11ix}+i e^{ix},\qquad
 Fw=2\pi(e^{-i\pi/3}\delta_{11}+i\delta_1).
\]
Indeed the second frequency is \(7-6=1\) and its phase is \(e^{i\pi/2}=i\). The distributional dilation formula agrees: against a test, \(\delta(\xi/2-k)\) has value \(2\theta(2k)\), by the positive substitution \(\xi=2t\). It therefore cancels the prefactor \(1/2\) in \(F[v(2x)]=\tfrac12(Fv)(\xi/2)\).

**Solution 3.** If the extension exists, then \(f(z)z^{\ell-1}\) is analytic near the closed unit disk for every \(\ell\ge1\). Multiply by a cutoff equal to one there and apply the complex Green identity from U013 §1 to the disk. The interior \(\partial_{\bar z}\) is zero, so its circle integral vanishes; (1.1) gives \(c_{-\ell}=0\).

Conversely, suppose those coefficients vanish. For \(0<t<R\), (1.3) gives absolute uniform convergence of \(\sum_{k\ge0}c_kz^k\) on \(|z|\le t\). Its derivatives of every order also converge uniformly there, using a slightly larger radius \(t<t'<R\) and the convergent polynomially weighted geometric majorant. Passing the finite-sum fundamental theorem along horizontal and vertical segments to these limits proves complex differentiability with the expected derivative. The resulting holomorphic function on \(|z|<R\) agrees with \(f\) on the annular overlap by (1.4) and its expansion. Since \(R>1\), this is the required extension.

**Solution 4.** For \(0<z<1\), put
\[
 A_N(z)=\frac{z^{N+1}}{1-z},\qquad
 B_N(z)=\frac{z^{N+1}((N+1)-Nz)}{(1-z)^2}.
\]
The geometric tail is \(\sum_{k>N}z^k=A_N(z)\). Differentiation, justified uniformly on smaller compact intervals as above, gives \(\sum_{k>N}kz^k=zA_N'(z)=B_N(z)\). With \(t=R^{-1}\), \(s=r\), and \(E_N=M_RA_N(t)+M_rA_N(s)\), (1.3) therefore yields
\[
 \|v-v_N\|_\infty\le E_N,\qquad
 \|v'-v_N'\|_\infty\le M_RB_N(t)+M_rB_N(s).
\]
Writing \(q=\max(t,s)<1\) bounds the first by a constant times \(q^{N+1}\), and the second by a constant times \((N+1)q^{N+1}\). The entire-distribution estimates are
\[
 |(v-v_N)(\theta)|\le E_N\|\theta\|_1\le2E_Np_2(\theta),
 \qquad
 |(Fv-Fv_N)(\theta)|\le2\pi E_Np_0(\theta).
\]
Both seminorms are bounded on every bounded Schwartz family, proving strong convergence with the explicit geometric rate.

**Solution 5.** At \(m=3\), the finite sum gives \(p_3(x)=6-12x+4x^2\). Hence
\[
 u=-\delta_0+H(x)e^{-x}(6-12x+4x^2),
\]
and its full transform is
\[
 -1+\frac6{1+i\xi}-\frac{12}{(1+i\xi)^2}
                    +\frac8{(1+i\xi)^3}
 =W_6(\xi).
\]
Its value at zero is \(-1+6-12+8=1\). Its traces are \(6\) on the right and \(0\) on the left. For \(v=e^{-x}p_3\) on \(x>0\),
\[
 L_6v=e^{-x}\bigl(xp_3''+(2-2x)p_3'+4p_3\bigr).
\]
The three polynomials are \(8x\), \(-24+40x-16x^2\), and \(24-48x+16x^2\), whose sum is zero. The zero-side profile solves the equation too. At the origin the regular step contributes \(6\delta_0\), and \(L_6(-\delta_0)=-6\delta_0\). They cancel exactly.

**Solution 6.** Here \(m=2\), \(p_2(y)=-4+4y\), and the point coefficient is \(1\). Thus
\[
 u=\delta_0+H(-x)e^x(-4-4x),\qquad Fu=W_{-4}.
\]
The left trace is \(-4\) and the right trace \(0\), so the jump is \(4\). Direct differentiation of a reflected function gives \(L_{-a}Rv=-R L_av\). The positive profile for \(a=4\) has \(p_2' =4\), \(p_2''=0\), and
\((2-2y)4+2(-4+4y)=0\), so reflection proves the ordinary equation on \(x<0\). Its step contribution is \(4\delta_0\), canceled by \(L_{-4}\delta_0=-4\delta_0\). Reflection preserves the point mass itself.

**Solution 7.** The normalization sets \(C=1\). The continuous function \(b\) in (2.6) gives, on either punctured side,
\[
 \lim_{x\to0}xu(x)=ib(0)=\frac{\sin(\pi(2+i)/2)}{\pi}
                   =-\frac{i}{\pi}\sinh(\pi/2).
\]
The last equality follows by substituting \(\pi+it\) in the exponential formula for sine, with \(\sinh t=(e^t-e^{-t})/2\). It is nonzero since \(t=\pi/2>0\). A finite trace on either side would make \(xu(x)\) tend to zero there, which is impossible.

**Solution 8.** First suppose the finite traces exist. Theorem 2.1 forces \(a=2m\), \(m\in\mathbb Z\). Each nonzero normalized solution has a nonzero point coefficient, including \(u_0=\delta_0\), and its remaining step profile is locally integrable. A nonzero point mass cannot equal a locally integrable regular distribution: take a bounded smooth compact \(\rho\) with \(\rho(0)=1\) and test with \(\rho(x/\varepsilon)\). Its delta pairing remains one, but pairing any locally integrable function tends to zero by dominated convergence on a fixed compact interval with shrinking support. Subtracting the regular profile proves the asserted impossibility.

In fact the same conclusion holds without finite traces. If \(a\notin2\mathbb Z\), then \(b(0)\ne0\) for \(C\ne0\). Continuity gives some \(\delta>0\) with \(|b(x)|\ge|b(0)|/2\) for \(|x|<\delta\). The actual punctured representative therefore satisfies
\[
 |u(x)|=\frac{|b(x)|}{|x|}
       \ge\frac{|b(0)|}{2|x|},\qquad 0<|x|<\delta.
 \tag{S1}
\]
The absolute integral diverges on each side, by the logarithmic primitive. Any global locally integrable representative would agree almost everywhere with this one on the punctured sides. Here is the full uniqueness argument for that step. If their difference \(w\in L^1_{\rm loc}\) defines the zero distribution on a half-line, fix a compact interval \(J\) inside it and a compact smooth cutoff \(\chi\) equal to one on a neighborhood of \(J\). The function \(\chi w\), extended by zero, belongs to \(L^1(\mathbb R)\). For a fixed compact smooth mollifier \(\rho\) of integral one and sufficiently small \(\varepsilon\), each test \(\rho_\varepsilon(x-\,\cdot\,)\), \(x\in J\), is supported where \(\chi=1\), so \((\rho_\varepsilon*(\chi w))(x)=0\). The supplied integration foundation §15.4, (LP13)–(LP14), proves convergence of this convolution to \(\chi w\) in \(L^1\). Consequently \(\int_J|w|=0\). Exhaust each punctured half-line by countably many such intervals to obtain the asserted almost-everywhere equality. This contradicts the divergent integral in (S1). For \(a\in2\mathbb Z\), the preceding point-mass obstruction applies. Thus every nonzero tempered solution fails to be globally locally integrable.

Temperedness is essential. At \(a=0\), define
\[
 v(x)=\frac{\sinh x}{x}\ (x\ne0),\qquad v(0)=1,\qquad
 v(x)=\sum_{j\ge0}\frac{x^{2j}}{(2j+1)!}.
 \tag{S2}
\]
On every bounded complex disk this series and each differentiated series converge uniformly: successive factorial denominators dominate every fixed power of the index and radius. The segment fundamental-theorem argument proves that \(v\) is entire. Since \(xv=\sinh x\), its second derivative is again \(\sinh x\), so \(L_0v=(xv)''-xv=0\) everywhere, with both traces equal to one.

Nevertheless its compact-test distribution has no tempered extension. Choose a fixed nonnegative nonzero \(\rho\in C_c^\infty((-1/10,1/10))\). On the support of \(\rho(x-A)\), \(A\ge2\), we have \(x\ge A-1/10\), \(x\le A+1/10\), and
\(\sinh x=\tfrac12e^x(1-e^{-2x})\ge\tfrac12(1-e^{-3})e^x\).
Thus the pairing is at least \(c e^A/(A+1)\) for a fixed \(c>0\). Every \(p_N(\rho(\,\cdot-A))\) is at most \(C_N(1+A)^N\). A putative tempered bound contradicts these estimates: a term of degree larger than \(N+1\) in the exponential series proves \(e^A/(A+1)^{N+1}\to\infty\). This verifies precisely why the smooth solution lies outside the theorem's class.

## References

- Jiří Lebl, [*Tasty Bits of Several Complex Variables*](https://www.jirka.org/scv/scv-3.4.pdf), version 3.4, 23 December 2020, §4.1, Theorem 4.1.1 and its full proof. The signed annular application here uses the exact supplied U013 Cauchy–Pompeiu proof, including its singular-area estimate; the Laurent construction and complete spectral proof are given in this lesson.
- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), author-hosted edition dated 2 October 2026, §3.1.3, Proposition 3.2, and §3.2.1, the direct proof of Proposition 3.4. The compact-primitive and product-rule proofs needed for the integrating factor are supplied in full above.
- The exact U013, U049 and Fourier proofs are linked at their points of use. Supplied scalar and integration foundations retain their CC0 1.0 notices. This reconstructed exposition and its solutions are CC0.
