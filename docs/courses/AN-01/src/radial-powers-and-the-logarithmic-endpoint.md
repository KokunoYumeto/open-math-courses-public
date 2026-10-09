# Radial powers and the logarithmic endpoint

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

The Fourier transform of a radial power has an exact Gamma coefficient. At the limiting exponent its pole is a point mass in the physical variable, while its constant Laurent coefficient transforms into a logarithm. We derive these identities on all Schwartz tests, then calculate the point masses in the second derivatives of that logarithm.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz estimates, Gaussian integral, inversion and transpose rules. The [Gamma foundation](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), G0–G2 and W4a–W4e, proves the complex Euler integral, its nonvanishing, recurrence and residue. [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5, proves polar integration and sphere areas in every dimension, including dimension one. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 13.1–13.5 and 13.7–13.10, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.1 and 16.1–16.2, supply calculus, exponential series, cutoffs, convergence, Fubini and substitution. The local Hessian proof uses Boundary flux and weak identities, Theorem 2.1 and Corollary 2.2, on punctured disks. No external reference stands in for any of these proofs.

## Gaussians determine the radial power

Our convention is
\[
 F\phi(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}\phi(x)\,dx,
 \qquad (Fu)(\phi)=u(F\phi).
\]
Pairings are complex bilinear. Write \(r^z=\exp(z\log r)\) for \(r>0\), using the real logarithm. Let
\(\sigma_{n-1}=2\pi^{n/2}/\Gamma(n/2)\).
For estimates we use
\[
 p_{N,k}(\phi)=\max_{|\beta|\le k}
       \sup_x(1+|x|)^N|\partial^\beta\phi(x)|.
\]
Fourier foundation F1 proves equivalence with its monomial seminorms.

**Theorem 1.1 (the whole radial transform).** For \(n\ge1\) and \(0<\operatorname{Re}a<n\), both sides of
\[
 F(|x|^{-a})=C_{n,a}|\xi|^{a-n},
 \qquad
 C_{n,a}=2^{n-a}\pi^{n/2}
          \frac{\Gamma((n-a)/2)}{\Gamma(a/2)}
 \tag{1.1}
\]
are regular tempered distributions, and the equality holds on all of \(\mathbb R^n\).

**Proof: represent the physical power.** Set \(A=\operatorname{Re}a\). Polar integration bounds the integral of \(|x|^{-A}|\phi(x)|\) on \(r<1\) by \(\sigma_{n-1}p_{0,0}(\phi)/(n-A)\). For \(r\ge1\), use \(p_{N,0}(\phi)r^{-N}\) with \(N>n-A\). This proves absolute convergence and a finite seminorm bound. The frequency power has the same properties: its radial exponent at zero is \(A-1>-1\), and a sufficiently large \(N\) controls infinity.

Substitution \(s=t|x|^2\) in the convergent Euler integral gives
\[
 |x|^{-a}
 =\frac1{\Gamma(a/2)}
       \int_0^\infty t^{a/2-1}e^{-t|x|^2}\,dt
 \quad(x\ne0).
 \tag{1.2}
\]
The denominator is nonzero by W4a–W4d. The modulus of the integrand uses \(t^{A/2-1}\). Inserting a Schwartz test after Fourier transposition is legitimate because Tonelli gives
\[
 \begin{aligned}
 &\int_0^\infty\int_{\mathbb R^n}
       t^{A/2-1}e^{-t|x|^2}|F\phi(x)|\,dx\,dt\\
 &\hspace{8mm}=\Gamma(A/2)
       \int_{\mathbb R^n}|x|^{-A}|F\phi(x)|\,dx<\infty .
 \end{aligned}
 \tag{1.3}
\]
Here \(F\phi\) is Schwartz by F2, and the preceding radial bounds apply. Absolute Fubini now proves
\[
 (F|x|^{-a})(\phi)
 =\frac1{\Gamma(a/2)}\int_0^\infty t^{a/2-1}
        \left(\int e^{-t|x|^2}F\phi(x)\,dx\right)dt.
 \tag{1.4}
\]

**Proof: transform and integrate the Gaussian.** Fourier foundation F3 proves directly, by its scalar differential equation and product integration,
\[
 F(e^{-t|x|^2})(\xi)
       =(\pi/t)^{n/2}e^{-|\xi|^2/(4t)}.
 \tag{1.5}
\]
At each fixed \(t>0\), Fubini transposes this ordinary integrable Gaussian; the absolute bound is \(\|e^{-t|x|^2}\|_1\|\phi\|_1\).
To exchange the remaining \(t,\xi\) integrals, check their absolute integral:
\[
 \pi^{n/2}\int_{\mathbb R^n}|\phi(\xi)|
     \int_0^\infty
        t^{(A-n)/2-1}e^{-|\xi|^2/(4t)}\,dt\,d\xi .
 \tag{1.6}
\]
For \(\xi\ne0\), put \(s=|\xi|^2/(4t)\); the inner integral becomes
\(2^{n-A}|\xi|^{A-n}\Gamma((n-A)/2)\).
This is integrable against \(|\phi|\) by the frequency bound already proved. A possibly infinite value at the single point \(\xi=0\) changes no Lebesgue integral. Tonelli proves finiteness of (1.6), so complex Fubini applies.

The same substitution, now retaining the complex powers, gives
\[
 \int_0^\infty t^{(a-n)/2-1}e^{-|\xi|^2/(4t)}\,dt
 =2^{n-a}|\xi|^{a-n}\Gamma((n-a)/2)
 \quad(\xi\ne0).
 \tag{1.7}
\]
Combining (1.4)–(1.7) proves (1.1) on every test. In particular the computation leaves no undetermined point distribution. \(\square\)

The Gamma integral gives \(\Gamma(1)=1\); the substitution \(s=r^2\) and Gaussian mass give \(\Gamma(1/2)=\sqrt\pi\). Thus in dimension three,
\[
 F(|x|^{-1})=4\pi|\xi|^{-2},\qquad
 F(|x|^{-2})=2\pi^2|\xi|^{-1}.
\]
The distinction between these constants will matter in the exercises.

## Translation gives the exact phase

**Corollary 2.1.** On the whole real line,
\[
 F(|x+1|^{-1/2})
       =e^{i\xi}\sqrt{2\pi}\,|\xi|^{-1/2}.
 \tag{2.1}
\]

**Proof.** Apply (1.1) with \(n=1,a=1/2\). The two Gamma factors cancel, giving \(Fg=\sqrt{2\pi}|\xi|^{-1/2}\) for \(g(x)=|x|^{-1/2}\). For any Schwartz \(\phi\), affine substitution gives
\[
 (F[g(\cdot+1)])(\phi)
   =\int g(y)F\phi(y-1)\,dy
   =g\bigl(F[e^{i(\cdot)}\phi]\bigr).
\]
The exponential multiplier preserves Schwartz seminorms by its bounded derivatives. The last expression is \((Fg)(e^{i(\cdot)}\phi)\), giving the asserted phase on every test. All integrals are absolute by the power bounds. \(\square\)

More generally, the same test computation proves
\[
 F[g(\cdot-b)]=e^{-ib\xi}Fg,\qquad
 F[e^{icx}g(x)]=(Fg)(\xi-c).
\]
For the second identity use \(e^{icx}F\phi(x)=F[\phi(\cdot+c)](x)\), followed by the frequency substitution. These formulas hold for every tempered distribution by the same transposes, whose test maps are continuous.

## The critical exponent gives a logarithm

**Theorem 3.1 (all nonzero monomials).** If \(\alpha\) is a multiindex with \(|\alpha|\ge1\), then \(x^\alpha|x|^{-n}\) is locally integrable and tempered, and
\[
 F(x^\alpha|x|^{-n})
        =-\sigma_{n-1}(i\partial_\xi)^\alpha\log|\xi|.
 \tag{3.1}
\]
Every derivative here is a derivative of the whole regular logarithm distribution.

**Proof: fix the finite part.** Choose \(0<d<\min(1,n)\). For \(|\operatorname{Re}z|<d\), define
\[
 \begin{aligned}
 H(z)(\phi)
 &=\int_{S^{n-1}}\int_0^1
       r^{z-1}\,[\phi(r\omega)-\phi(0)]\,dr\,d\sigma(\omega)\\
 &\quad+\int_{S^{n-1}}\int_1^\infty
       r^{z-1}\phi(r\omega)\,dr\,d\sigma(\omega).
 \end{aligned}
 \tag{3.2}
\]
FTC bounds the bracket by \(\sqrt n\,r p_{0,1}(\phi)\), since \(\sum_j|\omega_j|\le\sqrt n\). The first absolute radial bound is \(\sqrt n\,r^{-d}p_{0,1}(\phi)\); the second is \(r^{d-1-N}p_{N,0}(\phi)\) with \(N>d\). Both are integrable. This defines a tempered distribution, with one fixed finite bound on each smaller closed parameter region.

Parameter derivatives insert powers of \(\log r\). Gamma foundation G1, with \(r=e^{-s}\) at zero and \(r=e^s\) at infinity, proves integrability of every such power under the same strict exponent margins. For precision, the exponential series or twice integrated FTC gives
\[
 \left|e^{h\log r}-1-h\log r\right|
       \le \tfrac12|h|^2|\log r|^2 e^{|h||\log r|}.
\]
On a smaller parameter region choose \(|h|\) below half its distance from the two limiting exponents. The displayed bounds then dominate the divided Taylor remainder, uniformly when \(\phi\) ranges over any family bounded in all Schwartz seminorms. Repeating after multiplication by \((\log r)^j\) proves all complex derivatives. Thus \(H\) is holomorphic even in the strong dual sense: all its differentiation limits are uniform on such bounded families.

For \(0<\operatorname{Re}z<d\), polar integration splits the absolutely convergent integral at one and gives
\[
 |x|^{-n+z}=\frac{\sigma_{n-1}}z\delta_0+H(z).
 \tag{3.3}
\]
The identity \(\int_0^1r^{z-1}\,dr=1/z\) follows from its primitive and \(\operatorname{Re}z>0\). Put \(H_0=H(0)\).

**Proof: take the Fourier constant term.** In that same strip, Theorem 1.1 says
\[
 F(|x|^{-n+z})=c(z)|\xi|^{-z},\qquad
 c(z)=2^z\pi^{n/2}\frac{\Gamma(z/2)}{\Gamma((n-z)/2)}.
 \tag{3.4}
\]
The Gamma recurrence yields
\[
 c(z)=\frac{\sigma_{n-1}}z A(z),\qquad
 A(z)=2^z\frac{\Gamma(1+z/2)\Gamma(n/2)}
                       {\Gamma((n-z)/2)},\qquad A(0)=1.
\]
The nonvanishing Gamma proof makes \(A\) holomorphic near zero. Its convergent scalar Taylor expansion therefore gives
\[
 c(z)=\frac{\sigma_{n-1}}z+\kappa_n+O(z),
 \quad
 \kappa_n=\sigma_{n-1}
   \left(\log2+\tfrac12\psi(1)+\tfrac12\psi(n/2)\right),
 \tag{3.5}
\]
where \(\psi=\Gamma'/\Gamma\); the numerical value is not needed.

In frequency variables \(|\xi|^{-z}\) is a regular tempered family for \(|\operatorname{Re}z|<d<n\). At zero its radial majorant is \(r^{n-1-d}\), and at infinity one uses \(r^{n-1+d-N}\) with \(N>n+d\). The logarithmic and remainder bounds just proved apply with these exponents. Hence, uniformly on bounded Schwartz families,
\[
 |\xi|^{-z}=1-z\log|\xi|+O(z^2).
 \tag{3.6}
\]
In particular \(\log|\xi|\) is locally integrable in every positive dimension and tempered at infinity.

Fourier transformation preserves these strong limits. Indeed for a bounded family \(B\subset\mathcal S\), continuity of \(F:\mathcal S\to\mathcal S\) makes \(FB\) bounded, and
\(\sup_{\phi\in B}|Fu(\phi)|=\sup_{\phi\in B}|u(F\phi)|\).
Transform (3.3), use \(F\delta_0=1\), subtract \(\sigma_{n-1}/z\), and let positive real \(z\) tend to zero in (3.4). Equations (3.5)–(3.6) give
\[
 FH_0=\kappa_n-\sigma_{n-1}\log|\xi|.
 \tag{3.7}
\]
This limit argument needs no assertion based only on punctured frequency space and no continuation of an unchecked identity.

**Proof: remove the subtraction by multiplication.** The test \(x^\alpha\phi\) vanishes at zero, so substitution into (3.2) gives
\[
 x^\alpha H_0=x^\alpha|x|^{-n}.
 \tag{3.8}
\]
Its absolute radial bound at zero is \(r^{|\alpha|-1}\) times a test supremum; infinity is controlled by a polynomial weight. Apply F5's coordinate rule repeatedly to (3.7). Since a nonzero derivative kills the ordinary constant \(\kappa_n\), (3.1) follows, with all contact terms intact. \(\square\)

**Lemma 3.2 (the one-dimensional logarithmic derivative).** On the line,
\[
 (\log|t|)'=P,\qquad
 P(\phi)=\int_0^\infty\frac{\phi(t)-\phi(-t)}t\,dt.
\]
**Proof.** Near zero FTC bounds the numerator by \(2t p_{0,1}(\phi)\); the tail uses a Schwartz weight. Thus \(P\) is tempered. Integrate \(-\log|t|\phi'(t)\) on the two intervals with \(|t|>\varepsilon\). Their inner endpoint term is
\(\log\varepsilon[\phi(\varepsilon)-\phi(-\varepsilon)]\), which tends to zero by the same bound. The remaining integral tends to \(P(\phi)\). The omitted logarithmic integral over \(|t|<\varepsilon\) tends to zero by local integrability. The endpoints at infinity vanish by Schwartz decay. This proves the full derivative. Taking \(n=1,\alpha=1\) in (3.1) gives \(F(\operatorname{sgn}x)=-2iP\). \(\square\)

**Lemma 3.3 (the full planar Hessian).** With spherical deletion,
\[
 \partial_j\partial_k\log|\xi|
 =\operatorname{pv}
     \frac{\delta_{jk}|\xi|^2-2\xi_j\xi_k}{|\xi|^4}
       +\pi\delta_{jk}\delta_0
 \quad(j,k\in\{1,2\}).
\]
**Proof.** First \(\log r\) and \(\xi_k/r^2\) are locally integrable in two dimensions. Integrate \(-\log r\,\partial_k\phi\) on a punctured disk containing the support of a compact smooth test. The inward boundary of this region has normal \(-\omega\). Its boundary error is bounded by \(C\varepsilon|\log\varepsilon|\|\phi\|_\infty\), which tends to zero. U011's boundary formula therefore gives the entire weak gradient \(\partial_k\log r=\xi_k/r^2\).

Set \(K_{jk}(\xi)=(\delta_{jk}r^2-2\xi_j\xi_k)/r^4\). Angular foundation A5 gives
\(\int_{S^1}\omega_j\omega_k\,d\sigma=\pi\delta_{jk}\): the first square is A5, the other is \(2\pi-\pi\), and the mixed integral vanishes by the reflection \(\theta\mapsto2\pi-\theta\). Consequently the angular mean of \(K_{jk}\) is zero. In its deleted integral on \(r<1\) one can replace \(\phi(r\omega)\) by \(\phi(r\omega)-\phi(0)\). The resulting absolute radial bound is constant times \(p_{0,1}(\phi)\,dr\). This proves existence of the spherical principal value, and the tail bound proves temperedness.

One more integration by parts, now on the weak gradient, gives
\[
 -\int_{r>\varepsilon}\frac{\xi_k}{r^2}\partial_j\phi\,d\xi
 =\int_{r>\varepsilon}K_{jk}(\xi)\phi(\xi)\,d\xi
       +\int_{S^1}\omega_j\omega_k\phi(\varepsilon\omega)\,d\sigma.
\]
The positive sign is the negative of the inward normal in the integration-by-parts boundary term. The last integral tends to \(\pi\delta_{jk}\phi(0)\), with error at most \(C\varepsilon p_{0,1}(\phi)\). The omitted integral of \((\xi_k/r^2)\partial_j\phi\) tends to zero. This proves the formula on compact tests. Both sides are tempered; compact-test density in Fourier F1 extends equality to every Schwartz test. Summing \(j=k=1,2\) cancels the kernels and gives \(\Delta\log r=2\pi\delta_0\). \(\square\)

## Exercises

**Exercise 1 (foundation).** Transform \(2/|x|-3/|x|^2\) on \(\mathbb R^3\). Establish local integrability in both variables and specify why the complete answer has no point mass.

**Exercise 2 (intermediate).** Locate the frequency singularity and compute the exact phase and coefficient for \(e^{-4ix}|2x-3|^{-1/2}\) on the line.

**Exercise 3 (advanced).** For complex \(a\) in the strict strip of Theorem 1.1, find \(F(|x|^{-a}\log|x|)\). Justify the parameter derivative in the strong Schwartz dual and express the coefficient using \(\psi=\Gamma'/\Gamma\).

**Exercise 4 (intermediate).** For \(b>0\), evaluate \((F|x|^{-a})(e^{-b|\xi|^2})\) twice: through the physical transpose and through the frequency formula. Check every normalization.

**Exercise 5 (intermediate).** Determine \(F(x^2\operatorname{sgn}x)\). Give both a derivative definition and a deleted-integral definition of the cubic finite part, and prove that they agree.

**Exercise 6 (advanced).** In two dimensions transform \(x_1^2/|x|^2\) and \(x_1x_2/|x|^2\), including all contact terms. Check the sum of the two diagonal transforms.

**Exercise 7 (advanced).** Replace the split radius one in \(H_0\) by \(R>0\):
\[
 H_R(\phi)=\int_{S^{n-1}}\left[
 \int_0^R\frac{\phi(r\omega)-\phi(0)}r\,dr
       +\int_R^\infty\frac{\phi(r\omega)}r\,dr\right]d\sigma.
\]
Compute \(H_R-H_S\), \(FH_R\), and \(x^\alpha H_R\) for \(|\alpha|\ge1\).

**Exercise 8 (foundation).** Calculate the complete planar transform of
\((2x_1^2+2x_1x_2-3x_2^2)/|x|^2\).
Check the angular cancellation of the resulting principal-value numerator and the coefficient of its point mass.

## Solutions

**Solution 1.** In physical dimension three the radial densities at zero are \(r\,dr\) and \(dr\); in frequency they are \(dr\) and \(r\,dr\). They are integrable, and polynomial weights control all tails. Theorem 1.1 and the two Gamma values computed after its proof give
\[
 F(2/|x|-3/|x|^2)
       =8\pi|\xi|^{-2}-6\pi^2|\xi|^{-1}.
\]
Each summand is already identified on every Schwartz test, so linearity determines the entire distribution and permits no extra point term.

**Solution 2.** Write the function as
\(2^{-1/2}e^{-4ix}g(x-3/2)\), with \(g(x)=|x|^{-1/2}\).
Translation contributes \(e^{-3i\xi/2}\); modulation replaces every occurrence of \(\xi\) by \(\xi+4\). Thus
\[
 F(e^{-4ix}|2x-3|^{-1/2})
    =\sqrt\pi\,e^{-3i(\xi+4)/2}|\xi+4|^{-1/2}.
\]
The sole singularity is at \(-4\); the function is locally integrable there. The transpose proofs following Corollary 2.1 ensure this is the whole distribution, with no additional mass.

**Solution 3.** On a compact parameter set choose \(0<A_0\le\operatorname{Re}a\le A_1<n\). The physical integrals at zero are bounded by constants times
\(\int_0^1r^{n-1-A_1}|\log r|^j\,dr\), and the frequency integrals by
\(\int_0^1r^{A_0-1}|\log r|^j\,dr\).
Both converge for every fixed \(j\). At infinity choose a fixed Schwartz weight sufficiently large for both families and their logarithmic factors. The exponential Taylor remainder estimate in Theorem 3.1, with a smaller parameter margin, proves differentiation uniformly on bounded tests. Hence differentiation of (1.1) gives
\[
 F(|x|^{-a}\log|x|)
    =-C'_{n,a}|\xi|^{a-n}
       -C_{n,a}|\xi|^{a-n}\log|\xi|.
\]
Taking the derivative of the explicit nonzero Gamma quotient yields
\[
 \frac{C'_{n,a}}{C_{n,a}}
 =-\log2-\tfrac12\psi((n-a)/2)-\tfrac12\psi(a/2).
\]
The answer is therefore
\[
 C_{n,a}|\xi|^{a-n}
 \left[\log2+\tfrac12\psi((n-a)/2)
       +\tfrac12\psi(a/2)-\log|\xi|\right].
\]
This is a regular locally integrable function with a tempered tail. The derivative was taken in the whole dual space, fixing all terms at zero.

**Solution 4.** Polar integration and \(s=tr^2\) give the absolute complex integral
\[
 \int_{\mathbb R^n}|x|^{-a}e^{-t|x|^2}\,dx
 =\frac{\sigma_{n-1}}2\,t^{-(n-a)/2}
                       \Gamma((n-a)/2).
\]
Indeed the radial factor is \(r^{n-a-1}\), and its substituted differential is
\(\tfrac12t^{-(n-a)/2}s^{(n-a)/2-1}\,ds\).
By (1.5) the physical pairing equals
\[
 (\pi/b)^{n/2}\frac{\sigma_{n-1}}2
       (4b)^{(n-a)/2}\Gamma((n-a)/2)
 =2^{n-a-1}\sigma_{n-1}\pi^{n/2}
       b^{-a/2}\Gamma((n-a)/2).
\]
The frequency calculation gives
\[
 C_{n,a}\frac{\sigma_{n-1}}2
       b^{-a/2}\Gamma(a/2).
\]
Substitution of \(C_{n,a}\) cancels \(\Gamma(a/2)\) and gives the same value. The strict strip ensures every displayed pairing is absolutely convergent.

**Solution 5.** Define \(T=\tfrac12P''\), where \(P\) is Lemma 3.2. This tempered distribution agrees with \(1/\xi^3\) off zero. To determine its normalization, twice integrate \(\phi''(\xi)/\xi\) on the deleted half-lines:
\[
 \begin{aligned}
 \int_{|\xi|>\varepsilon}\frac{\phi''(\xi)}{\xi}\,d\xi
 &=2\int_{|\xi|>\varepsilon}\frac{\phi(\xi)}{\xi^3}\,d\xi\\
 &\quad-\frac{\phi'(\varepsilon)+\phi'(-\varepsilon)}{\varepsilon}
       +\frac{\phi(-\varepsilon)-\phi(\varepsilon)}{\varepsilon^2}.
 \end{aligned}
\]
The endpoints at infinity vanish. Taylor's formula makes the last two terms
\(-4\phi'(0)/\varepsilon+O(\varepsilon)\).
Since the left side tends to \(P(\phi'')=P''(\phi)\), this proves
\[
 \operatorname{pf}(1/\xi^3):=T,\qquad
 T(\phi)=\lim_{\varepsilon\downarrow0}
 \left[\int_{|\xi|>\varepsilon}\frac{\phi(\xi)}{\xi^3}\,d\xi
                -\frac{2\phi'(0)}{\varepsilon}\right].
\]
Existence also follows directly: subtract the Taylor polynomial through degree two on a symmetric unit interval; the cubic remainder divided by \(\xi^3\) is bounded, while the odd constant and quadratic contributions cancel and the linear term has exactly the stated divergence.
Lemma 3.2 and the coordinate rule give
\[
 F(x^2\operatorname{sgn}x)
       =i^2\partial_\xi^2(-2iP)=4i\,\operatorname{pf}(1/\xi^3).
\]
This also follows from (3.1) at \(n=1,\alpha=3\). The ordinary function \(1/\xi^3\) is not locally integrable; its values off zero alone leave the distribution at zero unspecified.

**Solution 6.** In (3.1), \(n=2\) and \(|\alpha|=2\) give the coefficient \(-2\pi i^2=2\pi\). Lemma 3.3 therefore yields
\[
 F(x_1^2/|x|^2)
   =2\pi\,\operatorname{pv}
       \frac{|\xi|^2-2\xi_1^2}{|\xi|^4}
       +2\pi^2\delta_0,
\]
\[
 F(x_1x_2/|x|^2)
    =-4\pi\,\operatorname{pv}\frac{\xi_1\xi_2}{|\xi|^4}.
\]
Interchanging coordinates gives the second diagonal. Its principal-value kernel is the negative of the first, whereas its point mass has the same sign. Their sum is \(4\pi^2\delta_0=F1\), as required by Fourier inversion. The boundary integral in Lemma 3.3, rather than an off-origin differentiation, fixes these masses.

**Solution 7.** FTC controls the subtracted integral at zero, and a Schwartz weight controls infinity. For \(R<S\), only \(R<r<S\) differs: \(H_R\) retains \(\phi\), while \(H_S\) subtracts \(\phi(0)\). Integration of \(dr/r\) gives
\[
 H_R-H_S=\sigma_{n-1}\log(S/R)\delta_0.
\]
Reversing \(R,S\) proves the same formula for every pair. At \(S=1\), the radius-one distribution is precisely \(H_0\) in Theorem 3.1, so
\[
 FH_R=\kappa_n-\sigma_{n-1}\log R
                    -\sigma_{n-1}\log|\xi|.
\]
Here a physical delta transforms to an ordinary constant. For \(|\alpha|\ge1\), \(x^\alpha\delta_0=0\) directly by evaluation of the test at zero, and hence
\(x^\alpha H_R=x^\alpha|x|^{-n}\), independently of \(R\). Its transform is (3.1).

**Solution 8.** Write the numerator as \(x^TMx\), where
\(M=\begin{pmatrix}2&1\\1&-3\end{pmatrix}\).
Linearity of Lemma 3.3 and (3.1) gives, for any symmetric two-by-two matrix,
\[
 F(x^TMx/|x|^2)
 =2\pi\,\operatorname{pv}
       \frac{\operatorname{tr}M\,|\xi|^2-2\xi^TM\xi}{|\xi|^4}
       +2\pi^2\operatorname{tr}M\,\delta_0.
\]
The mixed matrix entry occurs twice. In this instance \(\operatorname{tr}M=-1\), so
\[
 F\left(\frac{2x_1^2+2x_1x_2-3x_2^2}{|x|^2}\right)
 =2\pi\,\operatorname{pv}
     \frac{-5\xi_1^2-4\xi_1\xi_2+5\xi_2^2}{|\xi|^4}
       -2\pi^2\delta_0.
\]
The circle integrals of the two squares are \(\pi\), and that of the mixed product is zero. The numerator has integral \(-5\pi+5\pi=0\), which is the cancellation required by the spherical principal value. The physical angular mean is \(-1/2\); its constant component has transform \(-2\pi^2\delta_0\), agreeing with the result.

## References

- [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [Gamma foundation](../prerequisites/U011-free-foundations/gamma-foundations-U016.md), G0–G2 and W4a–W4e; [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5: the complete local proofs of all transform, parameter, polar and normalization inputs.
- Boundary flux and weak identities, Theorem 2.1 and Corollary 2.2: the punctured-domain boundary identity used to prove Lemma 3.3. The remaining scalar and integration proof locations are specified at the start of this lesson.
- Michael E. Taylor, [*Fourier Analysis, Distributions, and Constant-Coefficient Linear PDE*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fourier.pdf), freely accessible author text, Section 8, pp. 77–80: angular cancellation, finite-part subtraction and radial Fourier coefficients. Its unitary Fourier convention differs by \((2\pi)^{-n/2}\). The logarithmic sign is derived here in (3.4)–(3.7); the plus sign printed in its (8.30)–(8.31) does not agree with that limit. Every result used in this lesson is proved here or in the supplied programme proofs.
