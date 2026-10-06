# Convolution equations and logarithmic tails

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

Fourier multiplication gives a precise criterion for solving a Schwartz convolution equation. Gaussian convolution powers make the solution and its critical peak explicit, but their series has a smaller parameter domain than the equation itself. A separate support estimate permits convolution of two tempered distributions on the positive half-line. Finally, an endpoint with logarithmic decay gives a Fourier tail whose leading coefficient is exactly \(-i\).

We use the complex bilinear transform \(Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), with inverse \(G\) carrying the factor \((2\pi)^{-n}\), and the seminorms
\[
P_N(\phi)=\max_{|\alpha|\le N}\sup_x
\langle x\rangle^N|\partial^\alpha\phi(x)|,\qquad
\langle x\rangle=(1+|x|^2)^{1/2}.
\tag{0.1}
\]
The [Schwartz and Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves Gaussian mass, the exact Gaussian transform, inversion, compact-cutoff density and all transposed identities. [U040](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1, supplies the smooth Schwartz-factor convolution adapter and its multiplication formula. [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorems 1.1–2.1, supplies tensor pairings, proper convolution and all compact smoothing and derivative identities.

The [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4, prove Tonelli, absolute Fubini, affine substitution, dominated and monotone convergence, all Young endpoints and \(L^1\) mollifier convergence. The [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, prove compactness, the intermediate value and fundamental theorems, exponential and logarithmic differentiation, smooth cutoffs and integration by parts. The real symmetric diagonalization proof at the beginning of §2 of [U020](point-sources-and-complex-gaussian-kernels.md) and the [finite algebra foundation](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the matrix operations used in Solution 10.

Two elementary consequences will be used explicitly. First, a locally integrable function whose compact-test distribution is zero is zero almost everywhere. Multiply it by a compact smooth cutoff to obtain an \(L^1\) function. Each compact mollification is zero by the defining test pairing; the proved \(L^1\) convergence of mollifiers makes the cutoff function zero almost everywhere. An exhaustion by cutoffs equal to one on expanding balls proves the assertion.

Second, for \(s>n\),
\[
\int_{\mathbb R^n}\langle x\rangle^{-s}\,dx<\infty.
\]
The unit ball lies in a finite cube; the shell \(2^j\le|x|<2^{j+1}\) lies in a cube of volume \(2^{n(j+2)}\) and its integrand is at most \(2^{-js}\). Sum the convergent geometric series. Thus every function of polynomial growth defines a tempered distribution with an explicit sufficiently large Schwartz weight.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## An integrable convolution idempotent vanishes

**Theorem 1.1.** If \(n\ge1\) and \(f\in L^1(\mathbb R^n)\) satisfies \(f*f=f\), then \(f=0\) almost everywhere.

**Proof.** The \(L^1\) Young estimate makes \(f*f\) integrable. Its transform is
\[
F(f*f)(\xi)=Ff(\xi)^2.
\]
Indeed, the double integral has absolute integral \(\|f\|_1^2\), so Fubini and \(x=y+z\) give this formula with no normalization factor. The function \(h=Ff\) is continuous: for \(\xi_j\to\xi\), the exponential integrands converge pointwise and are dominated by \(|f|\). It also satisfies \(|h|\le\|f\|_1\). The equation gives \(h^2=h\), hence \(h\) takes only the values zero and one. If both occurred, restriction to a segment joining two such points and the intermediate value theorem would give a value strictly between them. Therefore \(h\) is constant.

The ordinary transform agrees with the transposed distributional transform, because the corresponding absolute double integral against a Schwartz test \(\psi\) is bounded by \(\|f\|_1\|\psi\|_1\). If \(h=0\), the supplied Fourier inversion makes the distribution \(f\) zero, and the mollifier argument above makes its density zero almost everywhere.

If \(h=1\), then \(F\delta_0=1\) and inversion would identify \(f\) with \(\delta_0\). Choose \(\psi\in C_c^\infty\) with \(\psi(0)=1\). For \(\varepsilon\downarrow0\), the functions \(\psi(x/\varepsilon)\) converge to zero at every \(x\ne0\), and are bounded by \(\|\psi\|_\infty\). The point zero has measure zero, since it lies in cubes of arbitrarily small positive volume. Dominated convergence against \(|f|\) gives
\[
\int f(x)\psi(x/\varepsilon)\,dx\longrightarrow0.
\]
The corresponding delta pairing is always one, a contradiction. The zero function does satisfy the equation. ∎

## A denominator decides a Schwartz convolution equation

**Theorem 2.1 (Schwartz resolvent).** For \(f\in\mathcal S(\mathbb R^n)\), the equation
\[
u-u*f=f
\tag{2.1}
\]
has a Schwartz solution if and only if \(Ff(\xi)\ne1\) at every real frequency. That solution is unique and equals
\[
u=G\!\left(\frac{Ff}{1-Ff}\right).
\tag{2.2}
\]

**Proof.** Put \(h=Ff\in\mathcal S\). The complete convolution identity gives \((1-h)Fu=h\). If \(h(\xi_0)=1\), evaluation of this equality of continuous functions gives \(0=1\), so a solution is impossible.

Suppose \(h\ne1\) everywhere. Since \(h\to0\) at infinity, \(|1-h|\ge1/2\) outside a ball. On the remaining compact ball, its positive continuous modulus has a positive minimum. Hence \(|1-h|\ge c>0\) globally.

Let \(r=(1-h)^{-1}\). Its first derivative is \(\partial_jr=(\partial_jh)/(1-h)^2\). Induction by product and quotient differentiation expresses each positive-order derivative of \(r\) as a finite linear combination of
\[
\frac{\prod_{\nu=1}^\ell\partial^{\gamma_\nu}h}
 {(1-h)^{\ell+1}},\qquad
|\gamma_\nu|\ge1,\quad\sum_{\nu=1}^\ell\gamma_\nu=\alpha.
\]
Differentiating a numerator increases one \(\gamma_\nu\); differentiating the denominator appends a first derivative of \(h\) and raises its power. This proves the induction, including finiteness of the coefficients. All these derivatives are bounded, since the derivatives of \(h\) are bounded and the denominator is bounded below.

For \(g=hr\), Leibniz gives the explicit seminorm control
\[
\sup_x\langle x\rangle^N|\partial^\alpha g(x)|
\le\sum_{\beta\le\alpha}\binom{\alpha}{\beta}
\sup_x\langle x\rangle^N|\partial^\beta h(x)|
\|\partial^{\alpha-\beta}r\|_\infty<\infty.
\]
Thus \(g\in\mathcal S\). Applying \(G\) gives (2.2), and the supplied convolution identity and inversion verify (2.1). The transform of the difference of two solutions is killed by the nowhere-zero \(1-h\); pointwise division and inversion make that difference zero. ∎

## Gaussian powers make the resolvent visible

**Theorem 2.2 (Gaussian power series and critical peak).** For \(n\ge1\), set
\[
q_k(x)=(4\pi k)^{-n/2}e^{-|x|^2/(4k)},\qquad
f_\rho=\rho q_1,\qquad |\rho|<1.
\tag{G1}
\]
Then \(q_j*q_k=q_{j+k}\), and the unique Schwartz solution for \(f_\rho\) is
\[
\begin{gathered}
u_\rho=\sum_{k=1}^\infty\rho^kq_k,\\
P_N\!\left(u_\rho-\sum_{k=1}^K\rho^kq_k\right)
\le C_N\sum_{k>K}|\rho|^k k^{N/2}.
\end{gathered}
\tag{G2}
\]
The constant is independent of \(K,\rho\). For real \(0<\rho<1\), this solution is positive and
\[
\begin{gathered}
\|u_\rho\|_1=\frac{\rho}{1-\rho},\\
\|u_\rho\|_\infty=u_\rho(0)
=(4\pi)^{-n/2}\sum_{k\ge1}\rho^k k^{-n/2}.
\end{gathered}
\tag{G3}
\]
As \(\rho\uparrow1\), the peak satisfies
\[
\begin{aligned}
n=1:&\quad \sqrt{1-\rho}\,u_\rho(0)\longrightarrow\tfrac12,\\
n=2:&\quad u_\rho(0)=-\frac{\log(1-\rho)}{4\pi},\\
n\ge3:&\quad u_\rho(0)\longrightarrow
(4\pi)^{-n/2}\sum_{k\ge1}k^{-n/2}<\infty.
\end{aligned}
\tag{G4}
\]
Nevertheless \(f_1=q_1\) has no Schwartz resolvent in any dimension.

**Proof: normalization and the Schwartz series.** The complete Gaussian calculation in the supplied Fourier foundation F3, followed by affine scaling, gives
\[
Fq_k(\xi)=e^{-k|\xi|^2},\qquad \int q_k(x)\,dx=1.
\]
These are the stated convention's exact constants. The Schwartz convolution formula and inversion prove \(q_j*q_k=q_{j+k}\).

Every derivative of \(q_1\) is a polynomial times its Gaussian. The elementary bound \(e^s\ge s^L/L!\), with sufficiently large integer \(L\), proves rapid decay of every such derivative. The exact scaling gives
\[
\begin{gathered}
q_k(x)=k^{-n/2}q_1(x/\sqrt{k}),\\
\partial^\alpha q_k(x)
=k^{-(n+|\alpha|)/2}(\partial^\alpha q_1)(x/\sqrt{k}).
\end{gathered}
\tag{G5}
\]
For \(k\ge1\), \(\langle x\rangle\le\sqrt{k}\langle x/\sqrt{k}\rangle\). Therefore \(P_N(q_k)\le P_N(q_1)k^{N/2}\). For fixed \(0<r<1\), the ratio of consecutive terms of \(r^k k^{N/2}\) tends to \(r\); eventually it is at most some \(s<1\), which bounds its tail by a geometric series. The case \(r=0\) is immediate.

Consequently each weighted derivative series converges uniformly and absolutely. On any compact line segment the fundamental theorem passes through the uniformly convergent function and first-derivative series, proving that the latter are the derivatives of the sum. Repeating this argument proves all derivative identities. The resulting smooth sum has every Schwartz seminorm finite, and the same estimates on tails give (G2) with \(C_N=P_N(q_1)\). No completeness assertion about an unconstructed pointwise sum is required.

Fourier continuity permits termwise transformation. The geometric identity gives
\[
Fu_\rho(\xi)=
\frac{\rho e^{-|\xi|^2}}{1-\rho e^{-|\xi|^2}}.
\tag{G6}
\]
Since the denominator is nonzero for \(|\rho|<1\), Theorem 2.1 verifies the equation and uniqueness.

**Proof: mass, maximum and critical peak.** For \(0<\rho<1\), monotone convergence of the positive partial sums and unit Gaussian mass give \(\|u_\rho\|_1=\sum_{k\ge1}\rho^k=\rho/(1-\rho)\). Each Gaussian is positive and has its maximum at zero, so their sum does too, giving (G3). Continuity identifies the pointwise and essential suprema by the positive-volume-ball argument.

For \(n=1\), put \(\tau=-\log\rho>0\) and \(b(t)=t^{-1/2}e^{-t}\). This function is positive decreasing. The substitution \(t=y^2\), first on finite positive intervals and then by monotone convergence at both ends, and the Gaussian mass identity give \(\int_0^\infty b(t)\,dt=\sqrt\pi\). Comparison of the decreasing rectangles with adjacent integrals yields
\[
\begin{gathered}
\int_\tau^\infty b(t)\,dt
\le \tau\sum_{k\ge1}b(k\tau)
\le \int_0^\infty b(t)\,dt,\\
0\le\sqrt\pi-\tau\sum_{k\ge1}b(k\tau)
\le\int_0^\tau t^{-1/2}\,dt=2\sqrt\tau .
\end{gathered}
\tag{G7}
\]
The middle sum equals \(\sqrt\tau\sum_{k\ge1}\rho^k k^{-1/2}\). Moreover
\[
1-\rho\le \tau=\int_\rho^1\frac{dt}{t}\le\frac{1-\rho}{\rho},
\]
so \(\tau/(1-\rho)\to1\). Multiplying by \((4\pi)^{-1/2}\) proves the limit \(1/2\).

For \(n=2\), monotone integration of \(\sum_{j\ge0}t^j=(1-t)^{-1}\) on \([0,\rho]\) gives \(\sum_{k\ge1}\rho^k/k=-\log(1-\rho)\). For \(n\ge3\), the series \(\sum k^{-n/2}\) converges: on \(2^j\le k<2^{j+1}\) its sum is at most \(2^{j(1-n/2)}\), a convergent geometric series. Dominated convergence for counting measure proves the last limit in (G4). Finally \(Fq_1(0)=1\), so Theorem 2.1 forbids a Schwartz solution at \(\rho=1\), including when the limiting peak is finite. ∎

## Positive support controls the full Schwartz pairing

**Theorem 3.1 (tempered causal convolution).** If \(u,v\in\mathcal S'(\mathbb R)\) are supported in \([0,\infty)\), their proper distributional convolution belongs to \(\mathcal S'\).

**Proof: define the global pairing.** Addition is proper on the support product: when \(x,y\ge0\) and \(x+y\) belongs to a compact set, both variables lie in a bounded interval. Its closed preimage is compact. U021 therefore defines the convolution on compact tests.

Choose a smooth \(\theta\) equal to zero for \(x\le-1\) and to one for \(x\ge-1/2\); the scalar cutoff construction supplies it with all derivatives bounded. Leibniz shows that multiplication by \(\theta\) is continuous on \(\mathcal S\). Localization gives \(\theta u=u\) and \(\theta v=v\) on compact tests and then, by compact-cutoff density, on Schwartz tests.

Choose integers \(N,M\) and constants with \(|u(\phi)|\le CP_N(\phi)\), \(|v(\phi)|\le C'P_M(\phi)\). For \(\psi\in\mathcal S\), define
\[
\begin{gathered}
V_\psi(x)=v_y\bigl(\theta(y)\psi(x+y)\bigr),\\
\Phi_\psi(x)=\theta(x)V_\psi(x),\qquad
W(\psi)=u(\Phi_\psi).
\end{gathered}
\tag{3.1}
\]
For fixed \(x\) the inner test is Schwartz. The translation and difference-quotient bounds proved in U040, Lemma 2.1, show smooth dependence on \(x\) in every Schwartz seminorm; multiplication by the fixed \(\theta(y)\) preserves those bounds. Applying \(v\) therefore commutes with each \(x\) derivative.

**Proof: the full seminorm estimate.** If \(x,y\ge-1\), then
\[
\begin{gathered}
|x|+|y|\le|x+y|+4,\\
\langle x\rangle^a\langle y\rangle^M
\le C_{a,M}\langle x+y\rangle^{a+M}.
\end{gathered}
\tag{3.2}
\]
For the first inequality, each variable's absolute value exceeds its signed value by at most two. It follows that each of \(1+|x|,1+|y|\) is at most \(5+|x+y|\), proving the second inequality after comparison with brackets.

For \(0\le r\le a\), the outer derivative is exactly
\[
\partial_x^r\Phi_\psi(x)=
\sum_{\ell=0}^r\binom r\ell\theta^{(\ell)}(x)
v_y\bigl(\theta(y)\psi^{(r-\ell)}(x+y)\bigr).
\]
Its inner derivatives through order \(M\) are
\[
\partial_y^j\bigl(\theta(y)\psi^{(r-\ell)}(x+y)\bigr)
=\sum_{m=0}^j\binom jm
\theta^{(m)}(y)\psi^{(r-\ell+j-m)}(x+y).
\]
Every nonzero cutoff term has \(x,y\ge-1\). All its cutoff derivatives are bounded, its test derivative has order at most \(a+M\), and (3.2) bounds its product weight. Applying the \(P_M\) bound for \(v\), summing these finitely many terms and taking the \(P_a\) supremum gives
\[
P_a(\Phi_\psi)\le C_{a,M}P_{a+M}(\psi),\qquad
|W(\psi)|\le C''P_{N+M}(\psi).
\tag{3.3}
\]
The first estimate holds for every \(a\), so \(\Phi_\psi\in\mathcal S\). The second proves that the linear functional \(W\) is tempered.

For compactly supported \(\psi\), the function \(\theta(x)\theta(y)\psi(x+y)\) has compact support: both variables are at least \(-1\), and a bounded sum bounds both above. It agrees with the uncut convolution test near the tensor support because both cutoffs are one near \([0,\infty)\). The iterated-pairing and localization statements of U021, Theorem 1.1, identify (3.1) with the actual proper convolution. Schwartz density proves uniqueness of its tempered extension and independence of the auxiliary cutoff. ∎

## A logarithmic endpoint has an exact Fourier coefficient

**Theorem 4.1 (logarithmic tail).** Let \(a>0\). Suppose \(u\) vanishes for \(x<0\) and \(x>1\), is smooth for \(x>0\), and equals \((\log(1/x))^{-a}\) on \(0<x<1/2\). Every such continuation satisfies
\[
\lim_{\xi\to+\infty}
\xi(\log\xi)^a\widehat u(\xi)=-i.
\tag{4.1}
\]

**Proof: reduce to the derivative integral.** Choose the irrelevant point value \(u(0)=0\), and write \(g(x)=(\log(1/x))^{-a}\) near zero. Scalar differentiation and a finite-interval substitution, followed by its zero-endpoint limit, give
\[
g'(x)=\frac{a}{x(\log(1/x))^{a+1}},\qquad
\int_0^b g'(x)\,dx=(\log(1/b))^{-a}.
\tag{4.2}
\]
Thus \(u'\) is integrable at zero; it is smooth on each remaining compact interval. Since \(u\) is smooth across \(1\) and vanishes to its right, its value and all derivatives vanish at \(1\). Integrate by parts on \([\delta,1]\). The boundary value at \(\delta\) tends to zero with \(u(\delta)\), and the derivative integral converges absolutely as \(\delta\downarrow0\). Hence
\[
\widehat u(\xi)=\frac{1}{i\xi}
\int_0^1u'(x)e^{-i\xi x}\,dx.
\tag{4.3}
\]

**Proof: keep the leading term and bound both tails.** Fix \(0<b<\min(1/2,e^{-a-2})\), let \(L=\log\xi\), and assume \(\xi>1/b\). The unoscillated integral of \(g'\) over \((0,1/\xi)\) is \(L^{-a}\). The error satisfies
\[
\left|\int_0^{1/\xi}g'(x)(e^{-i\xi x}-1)\,dx\right|
\le\xi\int_0^{1/\xi}xg'(x)\,dx
\le aL^{-a-1}.
\tag{4.4}
\]
The exponential difference bound follows by integrating its derivative on a real interval; the last bound uses \(\log(1/x)\ge L\) and the interval's length \(1/\xi\).

On \([1/\xi,b]\), direct differentiation gives
\[
g''(x)=
\frac{a(a+1-\log(1/x))}
 {x^2(\log(1/x))^{a+2}}<0.
\]
An integration by parts bounds this middle oscillatory integral by
\[
\frac{g'(1/\xi)+g'(b)}{\xi}
+\frac{1}{\xi}\int_{1/\xi}^b|g''(x)|\,dx
=\frac{2g'(1/\xi)}{\xi}=2aL^{-a-1}.
\]
The equality uses monotonicity, so every boundary magnitude is accounted for. On \([b,1]\), one more integration by parts gives a bound
\[
\frac{|u'(b)|+|u'(1)|+\int_b^1|u''(x)|\,dx}{\xi}.
\]
These finite constants depend on the continuation and on the fixed \(b\). Combining the three regions gives
\[
\int_0^1u'(x)e^{-i\xi x}\,dx
=L^{-a}+O_a(L^{-a-1})+O_u(\xi^{-1}).
\tag{4.5}
\]
Choose an integer \(m>a\). Since \(e^L\ge L^m/m!\), one has \(L^a/\xi\to0\). Multiplication of (4.3) by \(\xi L^a\) therefore leaves the coefficient \(1/i=-i\). The continuation enters only a vanishing error, proving the claimed independence. ∎

## Exercises

**Exercise 1 (basic).** Determine all \(f\in L^1(\mathbb R^n)\) with \(f*f=3f\).

**Exercise 2 (intermediate).** Let \(f=G(\rho e^{-|\xi|^2})\), \(\rho\in\mathbb R\). Determine exactly when the Schwartz resolvent exists and give it.

**Exercise 3 (intermediate).** For \(f=G(ie^{-\xi^2})\) on the line, compute the solution's transform and a global lower bound for its denominator.

**Exercise 4 (foundation).** For the positive-half-line indicator \(H\), compute \(H*H\) and \(H*H*H\), and prove temperateness.

**Exercise 5 (intermediate).** Compute \(\delta'_0*H\), explaining every derivative sign.

**Exercise 6 (foundation).** Explain why addition is not proper on the support product of \(H(x)\) and \(H(-x)\), and why their ordinary convolution integral diverges at every output.

**Exercise 7 (intermediate).** For \(u\) in Theorem 4.1 and \(b>0\), determine the logarithmic tail coefficient of \(v(x)=7u(bx)\).

**Exercise 8 (advanced).** For the same \(u\), prove \(\widehat{xu}(\xi)=O(\xi^{-2})\) as \(\xi\to+\infty\), and determine its limit under the normalization in (4.1).

**Exercise 9 (advanced).** For complex \(\rho\), determine the full Schwartz-resolvent parameter set for \(f_\rho=\rho q_1\). Compute
\[
c_\rho=\inf_{\xi\in\mathbb R^n}|1-\rho e^{-|\xi|^2}|
\tag{G8}
\]
piecewise in \(\operatorname{Re}\rho\) and \(|\rho|\), including finite-frequency attainment. Treat \(-2,1+i,2\), and find the exact parameter set for convergence of (G2) in Schwartz space.

**Exercise 10 (advanced).** For real symmetric positive definite \(B\) and \(0<\rho<1\), put
\[
q_{k,B}(x)=\frac{e^{-x^TB^{-1}x/(4k)}}
 {(4\pi k)^{n/2}\sqrt{\det B}},\qquad
f_{\rho,B}=\rho q_{1,B}.
\tag{G9}
\]
Find the unique Schwartz resolvent, justify all weighted mixed-derivative limits, and determine its mass, maximum and exact critical peak in every dimension, retaining the complete determinant factor. Decide whether dimension three allows a Schwartz solution at \(\rho=1\).

## Solutions

**Solution 1.** With \(g=f/3\), bilinearity gives \(g*g=(f*f)/9=f/3=g\). Theorem 1.1 gives \(g=0\), so \(f=0\). This function indeed satisfies the equation.

**Solution 2.** For \(n\ge1\), the range of \(e^{-|\xi|^2}\) is \((0,1]\). If \(\rho=1\), the transform is one at zero; if \(\rho>1\), it is one at any frequency with \(|\xi|=\sqrt{\log\rho}\). If \(0<\rho<1\), it is strictly less than one; if \(\rho\le0\), it is nonpositive. Thus precisely \(\rho<1\) is allowed. The solution is
\[
u=G\!\left(\frac{\rho e^{-|\xi|^2}}
 {1-\rho e^{-|\xi|^2}}\right).
\]
Theorem 2.1 supplies all Schwartz estimates, including for arbitrarily large negative \(\rho\) and for \(\rho=0\).

**Solution 3.** Put \(r=e^{-\xi^2}\). Then \(|1-ir|=\sqrt{1+r^2}\ge1\), and multiplication of numerator and denominator by \(1+ir\) gives
\[
Fu=\frac{ir}{1-ir}=\frac{-r^2+ir}{1+r^2}.
\]
Its inverse is the unique Schwartz solution by Theorem 2.1. The signs of both parts follow from this explicit multiplication.

**Solution 4.** On \(x>0\), the integral for \(H*H\) is the length of \((0,x)\), while on \(x<0\) it is zero. Thus \(H*H=xH(x)\). A second integral gives
\[
((xH)*H)(x)=H(x)\int_0^x y\,dy=\tfrac12x^2H(x).
\]
These are proper convolutions, identified with the ordinary integrals by compact-test Fubini on each bounded triangle. Proper associativity follows from U021, Theorem 3.1, applied to the proper addition map on the nonnegative triple product. Both answers have polynomial growth and are tempered by the weighted integrability estimate at the start; Theorem 3.1 also gives temperateness at each convolution step.

**Solution 5.** U021's compact-factor formula gives \(\delta_0*H=H\). Its derivative rule gives \(\delta'_0*H=H'\). On every compact test,
\[
H'(\psi)=-\int_0^\infty\psi'(x)\,dx=\psi(0),
\]
where the leading minus is the distributional derivative and the second minus is the lower-endpoint term of the fundamental theorem. Hence \(\delta'_0*H=\delta_0\).

**Solution 6.** The support product contains \((j,-j)\) for all positive integers \(j\). These points escape every bounded set and all map to zero under addition, so the preimage of the compact set \(\{0\}\) is not compact. At any output \(x\), the proposed ordinary integral is
\[
\int_{\mathbb R}H(y)H(y-x)\,dy
=\int_{\max(0,x)}^\infty1\,dy=\infty.
\]
Thus that ordinary integral does not define a finite convolution.

**Solution 7.** Affine substitution gives \(\widehat v(\xi)=7b^{-1}\widehat u(\xi/b)\). Set \(r=\xi/b\). Then
\[
\xi(\log\xi)^a\widehat v(\xi)
=7r(\log r)^a\widehat u(r)
\left(\frac{\log\xi}{\log r}\right)^a.
\]
The ratio tends to one because \(\log r=\log\xi-\log b\). Theorem 4.1 therefore gives the coefficient \(-7i\), for every \(b>0\), without requiring the dilated support to keep its old endpoints.

**Solution 8.** Set \(v=xu\). Near zero,
\[
v'=u+xu'\longrightarrow0,\qquad
v''(x)=\frac{a}{x(\log(1/x))^{a+1}}
+\frac{a(a+1)}{x(\log(1/x))^{a+2}}.
\]
Each displayed term is integrable by the substitution used in (4.2). The remaining portion is smooth, and \(v,v'\) vanish at \(1\). Two integrations by parts on \([\delta,1]\), followed by \(\delta\downarrow0\), have zero boundary limits at both ends: \(v(\delta),v'(\delta)\to0\). Thus
\[
\widehat v(\xi)=(i\xi)^{-2}\widehat{v''}(\xi),\qquad
|\widehat v(\xi)|\le\frac{\|v''\|_1}{\xi^2}.
\]
Consequently \(\xi(\log\xi)^a\widehat v(\xi)\to0\), by the logarithm-versus-exponential bound at the end of Theorem 4.1. No asymptotic remainder was differentiated.

**Solution 9.** The equality \(\rho r=1\) for some \(r\in(0,1]\) occurs exactly for \(\rho\in[1,\infty)\). Hence the allowed set is \(\mathbb C\setminus[1,\infty)\), and the solution is \(G\) applied to (G6), regardless of \(|\rho|\).

For \(\rho\ne0\), write \(a=\operatorname{Re}\rho\), \(b=|\rho|^2>0\). The squared modulus is
\[
d(r)=|1-\rho r|^2=1-2ar+br^2.
\]
Its derivative \(2(br-a)\) changes sign at \(r=a/b\). Restricting to the closed segment \([0,1]\), whose infimum equals that on \((0,1]\) by continuity, gives
\[
\begin{gathered}
c_0=1,\\
a\le0:\quad c_\rho=1,\\
a\ge b:\quad c_\rho=|1-\rho|,\\
0<a<b:\quad c_\rho=\sqrt{1-a^2/b}.
\end{gathered}
\tag{G10}
\]
The last radicand is nonnegative because it is the actual squared modulus at \(a/b\). At either boundary the adjacent formulas agree.

For \(\rho=0\), every finite frequency attains the minimum. For nonzero \(\rho\) with \(a\le0\), \(d(r)>1\) for \(r>0\), so the infimum is approached only as \(|\xi|\to\infty\). If \(a\ge b\), the minimum occurs at \(r=1\), or \(\xi=0\). If \(0<a<b\), the minimizing frequencies form the sphere \(|\xi|=\sqrt{-\log(a/b)}\). These alternatives include a zero minimum at every forbidden parameter.

At \(\rho=-2\), \(c_\rho=1\) and the resolvent exists. At \(\rho=1+i\), the minimizing \(r\) is \(1/2\), \(c_\rho=1/\sqrt2\), and the resolvent exists. At \(\rho=2\), the same \(r=1/2\) makes the denominator zero, so no Schwartz resolvent exists.

Theorem 2.2 proves convergence of the series precisely inside the unit disk. To exclude every \(|\rho|\ge1\), choose an integer \(N>n\) and evaluate its \(k\)-th term at \(x=\sqrt{k}e_1\):
\[
P_N(\rho^kq_k)\ge
(4\pi)^{-n/2}e^{-1/4}|\rho|^k k^{(N-n)/2}.
\tag{G11}
\]
This does not tend to zero. If the partial sums converged in every Schwartz seminorm, consecutive differences would tend to zero in each by the triangle inequality, a contradiction. This also excludes all unit-circle parameters whose resolvent nevertheless exists.

**Solution 10.** First retain the matrix and its full Jacobian. U020's complete real symmetric diagonalization gives \(B=O\Lambda O^T\), with \(O^TO=I\) and all diagonal entries \(\lambda_j>0\). Define
\[
A=O\operatorname{diag}(\sqrt{\lambda_j})O^T,\qquad
C=A^{-1}=B^{-1/2},\qquad D=\det A=\sqrt{\det B}>0.
\]
Finite matrix multiplication gives \(A^2=B\) and \(C^TC=B^{-1}\); the determinant formulas follow by multiplicativity and \((\det O)^2=1\). Thus, with \(y=Cx\),
\[
\begin{gathered}
q_{k,B}(x)=D^{-1}q_k(B^{-1/2}x),\qquad dx=D\,dy,\\
Fq_{k,B}(\xi)=e^{-k\xi^TB\xi}.
\end{gathered}
\tag{G12}
\]
The last equality follows by substituting \(x=Ay\): the transform becomes \(Fq_k(A^T\xi)\), and \(|A^T\xi|^2=\xi^TB\xi\).

**All mixed derivatives.** The chain rule is \(\partial_{x_i}=\sum_j C_{ji}\partial_{y_j}\). Expanding each power by the finite multinomial formula gives, for every smooth \(\phi\),
\[
\partial_x^\alpha\phi(Cx)
=\sum_m
\left(\prod_i\frac{\alpha_i!}{\prod_jm_{ij}!}\right)
\left(\prod_{i,j}C_{ji}^{m_{ij}}\right)
(\partial_y^{\beta(m)}\phi)(Cx).
\]
The finite sum runs over \(m_{ij}\ge0\) with \(\sum_jm_{ij}=\alpha_i\), and \(\beta_j(m)=\sum_i m_{ij}\). In particular \(|\beta(m)|=|\alpha|\), and every coefficient is retained. The finite operator bound for \(A\) gives
\(\langle Ay\rangle\le\max(1,\|A\|)\langle y\rangle\).
Taking absolute values in the displayed finite sum therefore proves
\[
P_N(D^{-1}\phi(C\,\cdot))\le C_{N,B}P_N(\phi)
\]
with a finite constant depending only on \(N,B\). Applying this inequality to the exact tails in (G2) proves every weighted mixed-derivative convergence and yields
\[
u_{\rho,B}(x)=\sum_{k\ge1}\rho^kq_{k,B}(x)
=D^{-1}u_\rho(B^{-1/2}x).
\tag{G13}
\]
Its transform is \(\rho e^{-\xi^TB\xi}/(1-\rho e^{-\xi^TB\xi})\). The denominator is nonzero for \(0<\rho<1\), so Theorem 2.1 verifies the equation and uniqueness.

**Mass and peak.** The full Jacobian and unit scalar Gaussian mass give \(\int q_{k,B}=1\). Positivity and monotone convergence give \(\|u_{\rho,B}\|_1=\rho/(1-\rho)\). The positive quadratic form in each exponent vanishes only at zero, so the maximum is at zero and equals \(D^{-1}u_\rho(0)\). Consequently
\[
\begin{aligned}
n=1:&\quad \sqrt{1-\rho}\,u_{\rho,B}(0)\longrightarrow\frac{1}{2D},\\
n=2:&\quad u_{\rho,B}(0)=-\frac{\log(1-\rho)}{4\pi D},\\
n\ge3:&\quad u_{\rho,B}(0)\longrightarrow
\frac{(4\pi)^{-n/2}}{D}\sum_{k\ge1}k^{-n/2}.
\end{aligned}
\tag{G14}
\]
At \(\rho=1\), the Fourier denominator still vanishes at zero. No Schwartz resolvent exists, including in dimension three; the bounded local peak does not alter the equation at that frequency.

## Free sources and exact proof dependencies

- Michael E. Taylor, [*Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*, author-hosted free text](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), §3, formulas (3.11)–(3.24), and §5, formulas (5.7)–(5.11): Gaussian normalization and the heat convolution kernel. The supplied Fourier foundation F3 proves the scalar Gaussian calculation in our exact convention without relying on an external analytic-continuation or polar-coordinate proof.
- The supplied scalar and integration foundations, with the exact F1–F5, U020, U021 and U040 locators given above, provide the earlier programme proofs. The reciprocal estimates, Gaussian series and critical limits, causal global seminorm bound, and logarithmic endpoint argument are proved in full here from those tools. An external reference supplies no omitted step.
- Original exposition is CC0. Supplied foundation components keep their stated CC0 terms and accompanying human attribution; the free research PDF is cited, not redistributed.
