# Counting zeros and the explicit formula for character sums over prime powers

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Original material is public domain (CC0).*

The logarithmic derivative of an L-function turns its Euler product into a sum over prime powers. Perron's kernel turns that Dirichlet series into a sharp partial sum. Moving the integral across the zeros then gives the explicit formula. There are two details that must survive the calculation: complex characters require counting zeros above and below the real axis, and even nonprincipal characters have a zero at the origin which produces a double pole in the integrand.

We use the functional equation, Gamma formulas and genus-one product from the preceding lessons. The local zero count and logarithmic-derivative expansion were proved in *Zero-free regions and the exceptional zero*. The only Perron input is the scalar truncated kernel in the planned zeta-course lesson *Perron's formula and the explicit formula for ψ(x)*: with \(c>0\),

\[
\frac1{2\pi i}\int_{c-iT}^{c+iT}\frac{y^s}s\,ds
=\delta(y)+O\left(y^c\min\left\{1,\frac1{T|\log y|}\right\}\right)
\quad(y\ne1),
\tag{0.1}
\]

where \(\delta(y)=0,1/2,1\) according as \(y<1,y=1,y>1\); at \(y=1\) the error is \(O(c/T)\). We use \(1<c<2\). This precise generic kernel has an existing internal proof assignment. The character-specific contour estimates and residues are supplied here.

Write

\[
\psi(x,\chi)=\sum_{n\le x}\chi(n)\Lambda(n),
\qquad
\psi_0(x,\chi)=\sum_{n<x}\chi(n)\Lambda(n)
+\frac12\chi(x)\Lambda(x),
\tag{0.2}
\]

where the last term is zero unless \(x\) is an integral prime power. Nontrivial zeros always refer to the inducing primitive function; they are repeated with multiplicity. For a primitive nonprincipal character, they lie strictly in \(0<\Re s<1\).

## 1. Counting both halves of the strip

Let \(N(T,\chi)\) count the nontrivial zeros with \(|\Im\rho|\le T\). Unlike the ordinary zeta convention of counting positive ordinates, this counts both signs. Real zeros are included. A complex character need not have conjugate zeros within its own L-function.

**Theorem 1.1.** For a primitive character of conductor \(q\), uniformly for \(T\ge2\),

\[
\boxed{N(T,\chi)=\frac T\pi\log\frac{qT}{2\pi e}
+O(\log(qT)).}
\tag{1.1}
\]

**Proof.** Begin with a nonprincipal primitive character and a height \(T\) which is not a zero ordinate in absolute value. Apply the argument principle to the entire function \(\xi(s,\chi)\) on the rectangle
\(-1-iT,2-iT,2+iT,-1+iT\), traversed counterclockwise. All its zeros are nontrivial and inside \(0<\Re s<1\).

The reflection identity
\(\xi(s,\chi)=\varepsilon(\chi)\overline{\xi(1-\overline s,\chi)}\)
reflects the left half of the boundary to the right half. Reflection reverses boundary orientation; complex conjugation reverses variation of argument. The two reversals cancel, and the constant \(\varepsilon\) contributes no variation. Thus

\[
\pi N(T,\chi)=\Delta_R\arg\xi(s,\chi),
\tag{1.2}
\]

where \(R\) is the path
\(1/2-iT\to2-iT\to2+iT\to1/2+iT\).

On \(\Re s=2\), the Euler-product logarithm of \(L\) is bounded uniformly, so its argument variation is \(O(1)\). On each horizontal part the local expansion from the preceding lesson gives

\[
\frac{L'}L(s,\chi)
=\sum_{|\gamma\mp T|\le1}\frac1{s-\rho}
+O(\log(qT)).
\]

Its nearby zeros number \(O(\log(qT))\). For one zero, the imaginary part of the integral of \(1/(s-\rho)\) along a horizontal segment is a change in \(\arg(s-\rho)\), whose absolute value is at most \(\pi\). The error integrates over a segment of bounded length. Therefore
\(\Delta_R\arg L=O(\log(qT))\), without requiring separation between \(T\) and the ordinates.

The Gamma factor has an analytic logarithm on the right half of the rectangle. With
\(z_T=1/4+a/2+iT/2\), its variation is
\(2\Im\log\Gamma(z_T)\). Vertical Stirling gives

\[
2\Im\log\Gamma(z_T)
=T\log(T/2)-T+O(1),
\]

uniformly for \(a=0,1\) and \(T\ge2\). The conductor factor contributes \(T\log(q/\pi)\). Insert these in (1.2) to obtain (1.1).

If \(T\) is an ordinate, take nearby non-ordinate heights. The local zero-count bound controls the number on the two edges by \(O(\log(qT))\); hence either inclusion convention has the same stated error. For the primitive principal character, of conductor 1, the zeta-course *Riemann–von Mangoldt formula* supplies the positive-ordinate count; doubling it yields (1.1). This is an exact existing internal prerequisite, with its own argument-principle and Gamma proof. \(\square\)

The already-proved local estimate is

\[
\#\{\rho:|\gamma-t|\le1\}\ll\log(q(|t|+2)).
\tag{1.3}
\]

Its two useful consequences, by division into unit intervals, are

\[
\sum_{1<|\gamma|\le T}\frac1{|\gamma|}
\ll\log(q(T+2))\log(T+2),
\qquad
\sum_{|\gamma|>T}\frac1{\gamma^2}
\ll\frac{\log(q(T+2))}{T}\quad(T\ge2).
\tag{1.4}
\]

For the second, sum \(\log(q(k+2))/k^2\) from \(k\asymp T\), or integrate it; the integral is \(O(\log(q(T+2))/T)\). The first follows from the analogous harmonic sum. These estimates do not presume GRH.

## 2. The constant at the origin

For a primitive nonprincipal character put

\[
b(\chi)=
\begin{cases}
L'(0,\chi)/L(0,\chi),&a=1,\\
\displaystyle\lim_{s\to0}\left(\frac{L'}L(s,\chi)-\frac1s\right),&a=0.
\end{cases}
\tag{2.1}
\]

Both quantities are finite. For odd characters \(L(0,\chi)\ne0\); for even ones \(L\) has a simple zero at 0. Let \(B(\chi)=\xi'(0,\chi)/\xi(0,\chi)\), as in the functional-equation lesson. Its logarithmic derivative gives the exact relations

\[
b(\chi)=B(\chi)-\frac12\log(q/\pi)
-\frac12\frac{\Gamma'}\Gamma(1/2)\quad(a=1),
\tag{2.2}
\]

\[
b(\chi)=B(\chi)-\frac12\log(q/\pi)+\frac{\gamma_E}2
\quad(a=0).
\tag{2.3}
\]

The second uses \(\Gamma'/\Gamma(s/2)=-2/s-\gamma_E+O(s)\). The zero summands \(1/(s-\rho)+1/\rho\) vanish at \(s=0\); their normally convergent sum therefore adds no constant there.

**Proposition 2.1.** Uniformly in primitive nonprincipal \(\chi\),

\[
\boxed{b(\chi)=-\sum_{|\gamma|\le1}\frac1\rho+O(\log q).}
\tag{2.4}
\]

In particular, if every zero with \(|\gamma|\le1\) satisfies \(|\rho|\ge\eta>0\), then
\(|b(\chi)|\ll(1+\eta^{-1})\log q\).

**Proof.** Subtract the genus-one logarithmic derivative at 2 from the derivative at \(s\):

\[
\frac{L'}L(s,\chi)=\frac{L'}L(2,\chi)
-\frac12\left(
\frac{\Gamma'}\Gamma((s+a)/2)
-\frac{\Gamma'}\Gamma((2+a)/2)\right)
+\sum_\rho\left(\frac1{s-\rho}-\frac1{2-\rho}\right).
\]

The first term is \(O(1)\) by absolute Euler convergence. Take the constant term at zero, removing \(1/s\) in the even case. The Gamma constant is \(O(1)\), so

\[
b(\chi)=O(1)-\sum_\rho
\left(\frac1\rho+\frac1{2-\rho}\right).
\tag{2.5}
\]

For \(|\gamma|>1\), the paired summand is
\(2/(\rho(2-\rho))=O(\gamma^{-2})\); (1.3) bounds their sum by \(O(\log q)\). For \(|\gamma|\le1\), the base-point denominator satisfies \(|2-\rho|\ge1\), and there are \(O(\log q)\) terms. This proves (2.4). The additional bound follows by taking absolute values in the finite remaining sum. \(\square\)

Thus a large constant can only come from zeros close to the origin. A zero near 1 for a real character has a reflected zero near 0, so omitting this constant would conceal a potentially large contribution. The cancellation in Section 5 will make that contribution explicit and stable.

## 3. Perron's integral and its endpoint error

Let \(\langle x\rangle\) be the distance from \(x\) to the nearest integral prime power other than \(x\) itself if \(x\) is a prime power. For \(x\ge2\) this distance is positive. Define

\[
E(x,T)=\frac xT\log^2(2x)
+\log(2x)\min\left\{1,\frac{x}{T\langle x\rangle}\right\}.
\tag{3.1}
\]

**Lemma 3.1.** With \(c=1+1/\log(2x)\), uniformly for \(x,T\ge2\),

\[
\psi_0(x,\chi)
=-\frac1{2\pi i}\int_{c-iT}^{c+iT}
\frac{L'}L(s,\chi)\frac{x^s}s\,ds+O(E(x,T)).
\tag{3.2}
\]

**Proof.** On this line the logarithmic derivative has its absolutely convergent series
\(-L'/L(s,\chi)=\sum_n\Lambda(n)\chi(n)n^{-s}\).
Interchange it with the finite integral and apply (0.1) term by term. Since \(|\chi(n)|\le1\), the error is bounded by

\[
\sum_{n\ne x}\Lambda(n)(x/n)^c
\min\left\{1,\frac1{T|\log(x/n)|}\right\}
+O(\log(2x)/T).
\tag{3.3}
\]

The last term covers the possible prime power \(n=x\) with its half weight. For \(n\le x/2\) or \(n\ge2x\), \(|\log(x/n)|\ge\log2\). The Chebyshev bound \(\sum_{n\le u}\Lambda(n)\ll u\), proved in the Dirichlet-theorem lesson, and partial summation give
\(\sum_n\Lambda(n)n^{-c}\ll1/(c-1)\ll\log(2x)\).
As \(x^c\le ex\), these outer ranges contribute \(O(x\log(2x)/T)\).

In \(x/2<n<2x\), the power factor is bounded and
\(|\log(x/n)|\gg|x-n|/x\). Also \(\Lambda(n)\le\log(2x)\). Keep the nearest prime power on each side of \(x\) separately, giving at most a constant times the second term of (3.1). The remaining integers can be ordered by distance; their distances are bounded below by a constant times their index, after these nearest terms are removed. Hence their contribution is
\(O((x/T)\log(2x)\sum_{k\le3x}1/k)
=O(x\log^2(2x)/T)\).
This bounds (3.3) by (3.1). \(\square\)

No factor depending on the character entered this endpoint estimate. If \(x\) is an integer, then \(\langle x\rangle\ge1\) and the whole error is
\(O(x\log^2(2x)/T)\). Near a nonintegral prime-power endpoint, the second term is needed.

## 4. Shifting the contour and taking every residue

**Theorem 4.1 (sharp truncated explicit formula).** For a primitive nonprincipal character of conductor \(q\), \(x,T\ge2\),

\[
\boxed{\begin{aligned}
\psi_0(x,\chi)={}&-\sum_{|\gamma|<T}\frac{x^\rho}{\rho}
-(1-a)\log x-b(\chi)\\
&+\sum_{m\ge1}\frac{x^{a-2m}}{2m-a}+R(x,T;\chi),
\end{aligned}}
\tag{4.1}
\]

where

\[
\boxed{R(x,T;\chi)\ll
\frac xT\log^2(qxT)
+\log(2x)\min\left\{1,\frac{x}{T\langle x\rangle}\right\}.}
\tag{4.2}
\]

The implied constant is absolute. For integral \(x\), this simplifies to
\(R\ll x\log^2(qxT)/T\).

**Proof.** First choose a good height \(U\in[T,T+1]\) whose distance from every ordinate of either sign is at least
\(\kappa/\log(q(T+2))\), with an absolute \(\kappa>0\). Such a height exists: (1.3) bounds the zeros in the two relevant unit intervals by \(C\log(q(T+2))\). Excluding intervals of radius \(\kappa/\log(q(T+2))\) around their absolute ordinates removes less than half of \([T,T+1]\) if \(\kappa\) is sufficiently small. Ordinates outside a slightly larger interval are already separated by an absolute distance.

On the horizontal segments with \(-1\le\sigma\le c\), the local logarithmic-derivative expansion gives

\[
\left|\frac{L'}L(\sigma\pm iU,\chi)\right|
\ll\log^2(q(T+2)).
\tag{4.3}
\]

Here is the extension to the left of the strip used earlier. Subtract the Hadamard derivative at \(2\pm iU\) exactly as in the local-expansion proof. The far zero terms are still \(O(\log(q(T+2)))\), since the real-part interval has bounded length. Each nearby denominator is at least the chosen separation, and there are \(O(\log(q(T+2)))\) such terms. The Gamma term is \(O(\log(U+2))\) on this horizontal interval: use its recurrence to move its real part to a positive bounded interval; \(|U|\ge2\) bounds each removed reciprocal. This proves (4.3).

For \(\sigma\le-1\), logarithmically differentiate the functional equation. The right-hand L-function at \(1-s\) has real part at least 2, so its logarithmic derivative is bounded by an absolute constant. Gamma reflection and vertical Stirling then show

\[
\frac{L'}L(s,\chi)\ll\log(q(|s|+2))
\tag{4.4}
\]

away from fixed-radius discs about the trivial zeros. At height \(\pm U\) there is no such restriction: the cotangent in Gamma reflection is bounded because \(|\Im s|\ge2\). On the left line \(\sigma=-V\), choose \(V=k+1/2\), \(k\) an integer tending to infinity; its distance from every trivial-zero abscissa is at least \(1/2\). Thus (4.4) applies throughout that line too. The Gamma estimates are the exact reflection/Stirling inputs already used in the functional-equation lesson.

Shift the integral in (3.2) to \(-V\). Its left vertical integral is
\(O(x^{-V}U\log(q(V+U+2))/V)\), which tends to zero as \(V\to\infty\) for fixed \(x,U\). On the horizontal portions between \(-1\) and \(c\), (4.3) bounds the integrals by

\[
\ll\frac{\log^2(q(T+2))}{T}
\int_{-1}^c x^\sigma\,d\sigma
\ll\frac{x\log^2(q(T+2))}{T\log x}.
\]

The remaining portions to the left are, by (4.4),

\[
\ll\frac1T\int_{-\infty}^{-1}
x^\sigma\log(q(T+|\sigma|+2))\,d\sigma
\ll\frac{x^{-1}\log(q(T+2))}{T\log x}.
\]

The last bound follows on writing \(\sigma=-1-v\), using
\(\log(q(T+v+3))\le\log(q(T+3))+\log(v+1)\), and integrating the exponentially decaying factor \(x^{-v}\); \(\log x\ge\log2\). Both horizontal bounds are covered by the first term of (4.2).

It remains to compute the residues of
\(-L'/L(s,\chi)x^s/s\). At a nontrivial zero \(\rho\) of multiplicity \(m\), the residue is \(-m x^\rho/\rho\). At a trivial zero \(a-2m\), \(m\ge1\), it is
\(x^{a-2m}/(2m-a)\). These trivial-zero residues converge absolutely as the left boundary recedes.

For odd characters the origin is regular for \(L'/L\), so its residue is \(-b(\chi)\). For even characters,

\[
\frac{L'}L(s,\chi)=\frac1s+b(\chi)+O(s),
\qquad
\frac{x^s}s=\frac1s+\log x+O(s).
\]

The integrand has a double pole whose coefficient of \(1/s\) is
\(-\log x-b(\chi)\). This is exactly the extra term in (4.1). There is no principal pole because the character is nonprincipal.

We have proved (4.1) at the good height \(U\), including its Perron error. Replacing \(U\) by \(T\) changes the zero sum by
\(O(\log(q(T+2)))\) terms, each of magnitude at most \(x/T\). This change is covered by (4.2). The endpoint term at \(U\ge T\) is no larger than its stated bound at \(T\). This also permits either convention at a zero exactly on the chosen height, within the same error. The integer simplification follows from \(\langle x\rangle\ge1\). \(\square\)

The trivial-zero series is especially transparent:

\[
\sum_{m\ge1}\frac{x^{-2m}}{2m}
=-\frac12\log(1-x^{-2})\quad(a=0),
\]

\[
\sum_{m\ge1}\frac{x^{1-2m}}{2m-1}
=\operatorname{arctanh}(1/x)
=\frac12\log\frac{1+x^{-1}}{1-x^{-1}}\quad(a=1).
\tag{4.5}
\]

For the primitive principal character, of conductor 1, the exact internal zeta explicit formula adds the pole residue \(x\), uses \(b=\zeta'(0)/\zeta(0)=\log(2\pi)\), and has no zero at the origin. Its trivial-zero series is the even series in (4.5). This precise case is supplied by the zeta-course lesson named above; it must not be obtained by inserting the principal character into the nonprincipal even-origin calculation.

For fixed \(x>1\), letting \(T\to\infty\) gives the symmetric limit form of (4.1). The same contour proof applies on \(1<x<2\) with constants depending on a positive lower bound for \(x-1\). The convergence is uniform on compact intervals free of prime powers, because \(\langle x\rangle\) has a positive lower bound there. The zero series is understood by this symmetric limiting procedure, not as an absolutely convergent sum.

## 5. A uniform formula without a large hidden constant

The function

\[
\frac{x^\rho-1}{\rho}=\int_1^x u^{\rho-1}\,du
\tag{5.1}
\]

has the removable value \(\log x\) at \(\rho=0\). This is the stable way to keep a zero very close to the origin in a uniform formula.

**Theorem 5.1.** For every Dirichlet character modulo \(q\), uniformly for \(x\ge T\ge2\),

\[
\boxed{\psi(x,\chi)=\mathbf1_{\chi=\chi_0}x
-\sum_{|\gamma|<T}\frac{x^\rho-1}{\rho}
+O\left(\frac xT\log^2(qx)\right).}
\tag{5.2}
\]

The zeros in this formula belong to the primitive inducing function. The implied constant is absolute; no lower bound for \(|\rho|\) is assumed.

**Proof.** For a primitive nonprincipal character, use (2.4) in (4.1). It replaces \(-b\) by \(\sum_{|\gamma|\le1}1/\rho+O(\log q)\). The difference from using \(\sum_{|\gamma|<T}1/\rho\) is bounded by (1.4):
\(O(\log(q(T+2))\log(T+2))\).
Thus each zero term becomes the quotient in (5.1), and the remaining constant is \(O(\log^2(qx))\) when \(T\le x\).

The logarithmic origin term, the trivial-zero series and the difference between \(\psi_0\) and \(\psi\) are \(O(\log(2x))\), since \(x\ge2\) and the series in (4.5) are bounded. The nearest-endpoint term in (4.2) is at most \(\log(2x)\), and the first error is \(O(x\log^2(qx)/T)\). Since \(x/T\ge1\), all these contributions are absorbed in the error of (5.2).

For the primitive principal character use the zeta formula in Section 4. The same far-zero reciprocal estimate applies. Its finitely many zeros with \(|\gamma|\le1\), if present, have reciprocals bounded by an absolute constant from the internal zeta zero-free-region and functional-equation results: neither 0 nor 1 is a zero of the completed zeta function. Compactness for this single fixed function suffices. Its fixed origin constant and trivial-zero series are likewise absorbed. This yields the additional \(x\) term in (5.2).

Finally, if \(\chi\) is induced by \(\chi^*\) of conductor \(d\mid q\), the two prime-power sums differ only at prime powers with prime dividing \(q\):

\[
|\psi(x,\chi)-\psi(x,\chi^*)|
\le\sum_{p\mid q}\sum_{p^k\le x}\log p
\le\omega(q)\log x\ll\log q\log x.
\tag{5.3}
\]

This is absorbed in the stated error. The nontrivial zeros are unchanged, and the principal indicator is unchanged as well: conductor 1 is exactly the principal case. Replace \(d\) by the larger \(q\) in the logarithmic bound. \(\square\)

It would be incorrect to suppress \(b(\chi)\) separately in (4.1) by a blanket \(O(\log q)\) claim. Formula (2.4) specifies the cancellation that makes (5.2) valid.

For progressions, finite character orthogonality gives

\[
\psi(x;q,b)=\frac1{\varphi(q)}\sum_{\chi\bmod q}
\overline{\chi(b)}\,\psi(x,\chi),\qquad(b,q)=1.
\tag{5.4}
\]

This average has just one principal contribution. It will be used both conditionally below and unconditionally in the next lesson.

## 6. What GRH gives for prime powers and progressions

Here GRH means that every nontrivial zero of every primitive Dirichlet L-function involved, including the Riemann zeta function, has real part \(1/2\). We use it as a clearly stated hypothesis, not as a theorem.

**Theorem 6.1.** Under GRH, uniformly for \(x\ge2\) and characters modulo \(q\),

\[
\psi(x,\chi)=\mathbf1_{\chi=\chi_0}x
+O(\sqrt x\log^2(qx)).
\tag{6.1}
\]

Consequently, for \((b,q)=1\),

\[
\psi(x;q,b)=\frac x{\varphi(q)}
+O(\sqrt x\log^2(qx)).
\tag{6.2}
\]

In particular the error is \(O(\sqrt x\log^2 x)\) when \(q\le x\).

**Proof.** Choose \(T=x\) in (5.2). Under GRH, \(|\rho|\ge1/2\) and \(|x^\rho|=\sqrt x\). By (1.3) for \(|\gamma|\le1\) and by (1.4) for the others,

\[
\sum_{|\gamma|<x}\frac1{|\rho|}
\ll\log(q(x+2))\log(x+2)\ll\log^2(qx).
\]

The absolute value of the zero sum in (5.2) is therefore
\(O((\sqrt x+1)\log^2(qx))\), proving (6.1). Average it in (5.4). The \(\varphi(q)\) errors are divided by \(\varphi(q)\), so their bound stays of the same size; the principal main term becomes \(x/\varphi(q)\). Finally \(q\le x\) gives \(\log(qx)\le2\log x\). \(\square\)

Prime powers with exponent at least 2 contribute at most \(O(\sqrt x\log^2 x)\) by the elementary bound that there are \(O(\log x)\) exponents and at most \(\sqrt x\) possible primes for each. Thus the same GRH error holds for \(\theta(x;q,b)\). Partial summation then gives a corresponding prime-counting estimate; its precise unconditional form, including an exceptional-zero term, is developed in the next lesson.

## 7. A computed example for the character modulo 4

For \(\chi_{-4}\), the root number is 1, so its critical-line Hardy function

\[
Z_{-4}(t)=
(4/\pi)^{it/2}
\frac{\Gamma(3/4+it/2)}{|\Gamma(3/4+it/2)|}
L(1/2+it,\chi_{-4})
\tag{7.1}
\]

is real. Its sign changes give numerical roots. Computation at 32-digit precision gives these ten positive ordinates below 30, rounded here:

| Number | Ordinate |
|---:|---:|
| 1 | 6.020948904698 |
| 2 | 10.243770304167 |
| 3 | 12.988098012312 |
| 4 | 16.342607104587 |
| 5 | 18.291993196124 |
| 6 | 21.450611343983 |
| 7 | 23.278376520460 |
| 8 | 25.728756425089 |
| 9 | 28.359634343025 |
| 10 | 29.656384014593 |

The negative ordinates are their negatives because this character is real. Substitution into \(L\) gives residuals below \(3\cdot10^{-32}\). A numerical argument-principle calculation on the rectangle with real sides \(-1,2\) and heights \(\pm30\), at two successively halved sampling spacings, gives winding number 20 in both cases. This is a numerical consistency check for the list, not a certified zero-isolation calculation or a proof of GRH.

For this odd character,
\(b=L'(0,\chi_{-4})/L(0,\chi_{-4})\approx0.783188785414\).
Using the ten pairs of zeros with \(T=30\), formula (4.1) becomes the finite approximation

\[
-2\sum_{0<\gamma<30}
\Re\frac{x^{1/2+i\gamma}}{1/2+i\gamma}
-b+\operatorname{arctanh}(1/x).
\tag{7.2}
\]

Direct prime-power sums and this approximation give:

| \(x\) | Direct \(\psi_0(x,\chi_{-4})\) | Approximation (7.2) | Direct minus approximation |
|---:|---:|---:|---:|
| 10 | −0.336472237 | −0.067027458 | −0.269444779 |
| 25 | −2.611419047 | −3.231561623 | 0.620142576 |
| 50 | −1.312951343 | −1.472559540 | 0.159608197 |
| 100 | −0.112564888 | 0.271039275 | −0.383604162 |

At \(x=25\), the prime-power endpoint contributes half of \(\chi_{-4}(25)\log5\), exactly as in (0.2). The remaining zeros account for the truncation error. Neither these approximate values nor the low-height list replaces the contour proof.

![The character-weighted prime-power step function and the explicit-formula approximation from ten zero pairs.](assets/beta-explicit-formula.png)

*Figure 1. The dark step curve is the right-continuous \(\psi(x,\chi_{-4})\); the smooth curve is (7.2), with the recomputed zero ordinates, the constant and the odd trivial-zero tail. At an isolated prime-power jump, \(\psi_0\) takes the midpoint rather than the right endpoint of the step. The approximation is a numerical truncation at \(T=30\), not a bound; the proved error is (4.2). The reproducible original diagram uses no source figure.*

## 8. Exercises

1. **Easy.** Derive the main term of \(N(T,\chi)\) from vertical Stirling, explaining the factor of two compared with the positive-ordinate zeta count.
2. **Medium.** Express \(b(\chi)\) in terms of \(B(\chi)\), and prove that it can be large only when zeros lie close to the origin.
3. **Medium.** Under GRH, prove \(\psi(x;q,b)=x/\varphi(q)+O(\sqrt x\log^2 x)\) uniformly for \(q\le x\).
4. **Hard.** Carry out the contour argument for an even primitive nonprincipal character, including the double pole at 0 and the exact prime-power endpoint convention.

## 9. Solutions

**1.** The right-half contour has imaginary endpoint difference \(2T\). Thus the conductor factor contributes \(T\log(q/\pi)\), and Gamma contributes
\(2\Im\log\Gamma(1/4+a/2+iT/2)
=T\log(T/2)-T+O(1)\).
The L-factor argument contributes \(O(\log(qT))\) by the local kernel argument. Reflection doubles this half-boundary variation, and the argument principle divides the full variation by \(2\pi\). Equivalently divide the half variation by \(\pi\), giving
\(T\pi^{-1}\log(qT/(2\pi e))+O(\log(qT))\).
The zeta count usually includes only positive ordinates; this character count includes both signs, even when the character is complex and those signs are not paired.

**2.** Evaluate the genus-one logarithmic derivative at zero. For odd characters the Gamma term is regular, giving (2.2). For even characters remove the simple pole \(1/s\) from \(L'/L\), and use
\(\Gamma'/\Gamma(s/2)=-2/s-\gamma_E+O(s)\), giving (2.3). To see what controls the size, subtract the derivative at 2 first. This produces (2.5). The far terms are \(O(\gamma^{-2})\), summable to \(O(\log q)\) by the local zero count. The nearby base-point terms \(1/(2-\rho)\) are likewise \(O(\log q)\). Hence (2.4). If every nearby zero has \(|\rho|\ge\eta\), then \(|b|\ll(1+\eta^{-1})\log q\). This is the required one-way assertion: it does not say that every individual nearby zero forces a large uncancelled complex constant.

**3.** Apply (5.2) with \(T=x\). GRH gives \(|\rho|\ge1/2\) and \(|x^\rho|=\sqrt x\). The local count for heights at most 1 and the harmonic bound (1.4) above height 1 give
\(\sum_{|\gamma|<x}1/|\rho|\ll\log^2(qx)\).
Thus each character sum differs from its principal main term by
\(O(\sqrt x\log^2(qx))\). Character orthogonality averages these bounds with coefficients of modulus 1. The error remains of that size and the principal term is \(x/\varphi(q)\). Since \(q\le x\), replace \(\log(qx)\) by at most \(2\log x\).

**4.** Use the half-weighted Perron formula (3.2). Choose the separated height \(U\in[T,T+1]\) by the local zero count and shift to \(\Re s=-k-1/2\). The bounds (4.3)–(4.4) control both horizontal pieces and send the left vertical integral to zero; the prime-power endpoint error remains (3.1). Nontrivial zeros contribute \(-x^\rho/\rho\), with multiplicity. Negative even trivial zeros \(-2m\), \(m\ge1\), contribute \(x^{-2m}/(2m)\), whose sum is \(-\tfrac12\log(1-x^{-2})\). At 0 the two expansions displayed in the proof of Theorem 4.1 give
\(-L'/L(s)x^s/s=-s^{-2}-(\log x+b)s^{-1}+O(1)\).
Its residue is therefore \(-\log x-b\). There is no residue at 1 because the character is nonprincipal and is nonzero there. Replacing \(U\) by \(T\) adds \(O(x\log(qT)/T)\), giving (4.1)–(4.2). At an integral prime power \(x\), the Perron kernel contributes exactly half of \(\chi(x)\Lambda(x)\); no alteration of the origin residue is made to compensate for this independent endpoint convention.

## References

D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 11.3 and Lemma 11.4, emphasizes the stable quotient \((x^\rho-1)/\rho\) and uniform character estimates. The contour estimates and residues are proved here rather than left as a character adaptation exercise. The generic Perron kernel, the principal zeta explicit formula and the principal zero count have the exact existing internal proof providers identified in the introduction and Section 1; their assigned status is planned where no completed text has been verified.
