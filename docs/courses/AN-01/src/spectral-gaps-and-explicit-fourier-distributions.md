# Spectral gaps and explicit Fourier distributions

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

A Fourier derivative equation can lose a point mass at zero. We calculate complete distributions, keeping the masses, their derivatives and the precise finite parts. We then prove the norm identities used in the examples and construct the unique bounded primitive with no frequency near zero.

Use \(Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\), \(G=(2\pi)^{-n}RF\), and \(Rf(x)=f(-x)\). Pairings are bilinear. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves every Schwartz estimate, inversion, coordinate identity and transpose convention. [U041](separated-frequencies-and-distributional-order.md), Lemma 0.1, proves Schwartz Parseval from absolute Fubini and that inversion. [U040](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1, proves the global convolution multiplier identity. [U045](positive-kernels-and-spectral-measures.md), Solution 2, proves the Cauchy Fourier pair by elementary Laplace integration and Fourier inversion.

The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12.4–12.9, 13.1–13.5 and 13.7–13.10, supplies compactness, FTC, trigonometry and cutoffs. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.4 and 16.1–16.2, supplies convergence, Fubini, Cauchy–Schwarz, \(L^2\) completeness and mollification. We prove the pole limits and the classification of all primitives here.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## Plane waves fix the normalization

**Proposition 1.1 (plane-wave normalization).** In \(\mathcal S'(\mathbb R^n)\),
\[
F(e^{ix\cdot b})=(2\pi)^n\delta_b.
\tag{1.1}
\]
**Proof.** For \(\theta\in\mathcal S\), the defining transpose pairing is the absolutely convergent integral \(\int e^{ix\cdot b}F\theta(x)\,dx\). Fourier inversion makes this \((2\pi)^n\theta(b)\). Thus the statement includes its complete value at the supporting point. On the line the coordinate identity \(F(xu)=i(Fu)'\) gives
\[
F1=2\pi\delta_0,\qquad Fx=2\pi i\delta'_0,\qquad
Fx^2=-2\pi\delta''_0.
\]
For completeness, the translation, modulation and positive-dilation rules are
\[
\begin{aligned}
F[u(\cdot-b)]&=e^{-ib\xi}Fu,\\
F[e^{ibx}u]&=(Fu)(\cdot-b),\\
F[u(\cdot/a)]&=a(Fu)(a\cdot)\quad(a>0).
\end{aligned}
\]
For functions these follow by affine substitution in the integral. For distributions the same identities follow by applying that substitution to the Schwartz test in the transpose definition; the maps preserve Schwartz seminorms by the chain rule and fixed affine weight comparisons. In particular \(T(a\cdot)(\theta)=a^{-1}T(\theta(\cdot/a))\) on the line. \(\square\)

## Rational tails and an odd antiderivative

We will prove the following identities, with \(a=1/\sqrt2\):
\[
\begin{gathered}
F((1+x^2)^{-1})=\pi e^{-|\xi|},\\
F(x/(1+x^2))=-i\pi\operatorname{sgn}(\xi)e^{-|\xi|},\\
F(x^3/(1+x^2))=2\pi i\delta'_0
 +i\pi\operatorname{sgn}(\xi)e^{-|\xi|},\\
F(\arctan x)=-i\pi\operatorname{pv}\frac{e^{-|\xi|}}{\xi},\\
F(x^3/(1+x^4))=-i\pi\operatorname{sgn}(\xi)
 e^{-a|\xi|}\cos(a|\xi|).
\end{gathered}
\tag{2.1}
\]
The weighted principal value is defined as one symmetric integral below; no nonsmooth multiplier is applied to a distribution.

**Proof: the Cauchy pair.** U045, Solution 2, proves
\(F(e^{-|x|})=2/(1+\xi^2)\) by integration on the two half-lines. Applying \(F\) again and using \(F^2=2\pi R\) gives the first identity. The inverse exponential is even. Its weak first derivative is \(-\operatorname{sgn}(\xi)e^{-|\xi|}\): split the integral against a compact test at zero and integrate by parts on both halves; the two boundary values cancel because the function is continuous. The Schwartz tails also vanish. The coordinate identity then proves the second formula. The decomposition \(x^3/(1+x^2)=x-x/(1+x^2)\) proves the third, including its point derivative.

**Proof: the entire arctangent transform.** Define
\[
A(\theta)=\int_0^\infty e^{-t}
 \frac{\theta(t)-\theta(-t)}t\,dt.
\]
For \(0<t<1\), FTC bounds the quotient by \(2\|\theta'\|_\infty\); for \(t\ge1\), the exponential gives a bound by \(2e^{-t}\|\theta\|_\infty/t\). Hence \(A\) is tempered. Its definition equals symmetric deletion of \(e^{-|\xi|}\theta(\xi)/\xi\), and direct substitution shows \(\xi A=e^{-|\xi|}\). It is odd.

The derivative \((\arctan x)'=(1+x^2)^{-1}\) therefore shows that both \(F(\arctan)\) and \(-i\pi A\) solve \(i\xi T=\pi e^{-|\xi|}\). Their difference is killed by \(\xi\). Such a tempered distribution \(V\) is \(c\delta_0\): choose \(\zeta\in\mathcal D\) with \(\zeta(0)=1\), and write
\[
\theta(\xi)=\theta(0)\zeta(\xi)+\xi r(\xi).
\]
Near zero, the numerator of \(r\) vanishes and FTC writes its quotient as the integral of its derivative along the segment from zero to \(\xi\). Repeated differentiation of this integral makes \(r\) smooth there. Outside a fixed neighborhood, the derivatives of \(1/\xi\) have polynomial bounds and \(\theta\) is Schwartz; the compact term causes no tail. Thus \(r\in\mathcal S\), and \(V(\theta)=V(\zeta)\theta(0)\). Both transforms in question are odd, since Fourier transformation commutes with reflection; \(\delta_0\) is even. Their difference must be zero.

**Proof: the quartic denominator.** Define the integrable even function
\[
w(\xi)=\pi a e^{-a|\xi|}
 \bigl(\cos(a|\xi|)+\sin(a|\xi|)\bigr),
\qquad a=1/\sqrt2.
\tag{2.2}
\]
Integration of \(e^{(-a+ib)t}\) on \(t\ge0\) gives the cosine and sine integrals \(a/(a^2+b^2)\) and \(b/(a^2+b^2)\). Product-to-sum, obtained by multiplying the exponential formulas for sine and cosine, then yields
\[
\begin{aligned}
Fw(x)&=\pi a\left[
 \frac{2a+x}{a^2+(a+x)^2}
 +\frac{2a-x}{a^2+(a-x)^2}\right]\\
&=\frac{2\pi}{1+x^4}.
\end{aligned}
\tag{2.3}
\]
Indeed the product denominator is
\((x^2+2ax+2a^2)(x^2-2ax+2a^2)=x^4+4a^4\), and the combined numerator in the brackets is \(8a^3\). Since \(8\pi a^4=2\pi\), every constant in (2.3) follows. Inversion and evenness give \(F[(1+x^4)^{-1}]=w\).

On the positive half-line,
\[
\begin{aligned}
w'&=-2\pi a^2e^{-a\xi}\sin(a\xi),\\
w''&=-2\pi a^3e^{-a\xi}(\cos(a\xi)-\sin(a\xi)),\\
w'''&=4\pi a^4e^{-a\xi}\cos(a\xi).
\end{aligned}
\]
The values of \(w,w',w''\) match their left limits at zero: evenness gives this for \(w,w''\), and \(w'(0+)=0\). Three integrations by parts on the two halves consequently have cancelling boundary terms through order two. The weak third derivative is the displayed ordinary derivative on each half, with no point term. It is
\(\pi\operatorname{sgn}(\xi)e^{-a|\xi|}\cos(a|\xi|)\). Multiplication by \(x^3\) corresponds to \(i^3\partial_\xi^3\), proving the final formula in (2.1).

## Jumps, ramps and shifted principal values

Define the symmetric principal value on Schwartz tests by
\[
P(\theta)=\int_0^\infty\frac{\theta(t)-\theta(-t)}t\,dt,
\qquad \operatorname{pf}(1/\xi^2)=-P'.
\]
The integral near zero is bounded by \(2\|\theta'\|_\infty\). On \(t\ge1\), the Schwartz estimate \(|\theta(\pm t)|\le C(1+t^2)^{-1}\) gives an integrable bound. Thus \(P\) and its derivative are tempered.

**Pole limit.** On every Schwartz test,
\[
(\xi-i\varepsilon)^{-1}
 \longrightarrow P+i\pi\delta_0\quad(\varepsilon\downarrow0).
\]
To prove it, split the kernel into \(\xi/(\xi^2+\varepsilon^2)\) and \(i\varepsilon/(\xi^2+\varepsilon^2)\). The odd first part pairs as
\(\int_0^\infty t[\theta(t)-\theta(-t)]/(t^2+\varepsilon^2)\,dt\). Its near-zero integrand is bounded by \(2\|\theta'\|_\infty\), and its tail by \((|\theta(t)|+|\theta(-t)|)/t\). Dominated convergence gives \(P(\theta)\). In the second part set \(\xi=\varepsilon s\); dominated convergence gives
\[
\int_{\mathbb R}\frac{\theta(\varepsilon s)}{1+s^2}\,ds
\longrightarrow\pi\theta(0).
\]
The mass \(\pi\) is the arctangent primitive from the scalar foundation. This proves the entire pole limit with its sign.

Let \(H=1_{(0,\infty)}\); its value at zero does not affect its distribution. The functions \(e^{-\varepsilon x}H(x)\) converge to \(H\) on Schwartz tests by dominated convergence, and their integrable Fourier transforms are
\((\varepsilon+i\xi)^{-1}=-i(\xi-i\varepsilon)^{-1}\). Fourier continuity and the preceding limit give
\[
FH=\pi\delta_0-iP.
\tag{3.1}
\]
In particular,
\[
\begin{gathered}
F(xH)=i\pi\delta'_0-\operatorname{pf}(1/\xi^2),\\
F(H(1+x)+H(1-x))=2\pi\delta_0+2\sin\xi/\xi,\\
F(\operatorname{sgn}x)=-2iP,\\
F(\sin|x|)=\operatorname{pv}\frac1{\xi+1}
 -\operatorname{pv}\frac1{\xi-1}.
\end{gathered}
\tag{3.2}
\]
Here the first formula is \(i(FH)'\). The second uses the almost-everywhere identity \(H(1+x)+H(1-x)=1+1_{[-1,1]}\) and integration of the interval exponential. The third follows from \(\operatorname{sgn}=2H-1\), with cancellation of the point masses. For the last, write
\(\sin|x|=\operatorname{sgn}(x)(e^{ix}-e^{-ix})/(2i)\) and use modulation on \(-2iP\). It gives \(-P(\xi-1)+P(\xi+1)\). Each shifted principal value is the translated distribution with symmetric deletion at its own pole; no additional mass is present.

## Finite profiles and polynomial contact terms

The finite exponential expansion of sine and (1.1) prove
\[
\begin{aligned}
F(\sin x)&=\frac\pi i(\delta_1-\delta_{-1}),\\
F(\sin^2x)&=\pi\delta_0-\frac\pi2(\delta_2+\delta_{-2}),\\
F((\sin x)^k)&=\frac{2\pi}{(2i)^k}
 \sum_{j=0}^k(-1)^j\binom kj\delta_{k-2j}
 \quad(k\ge1).
\end{aligned}
\]
These are finite sums; the binomial formula follows by choosing which of the \(k\) factors supply \(e^{-ix}\). In particular an even power retains a zero-frequency term.

The ordinary identity
\(\sin x/x=\frac12\int_{-1}^1e^{itx}\,dt\), including the value one at zero, gives
\[
F(\sin x/x)=\pi1_{[-1,1]}.
\]
Indeed pairing against \(F\theta\) permits Fubini with absolute bound \(\|F\theta\|_1\); (1.1) then gives \(\pi\int_{-1}^1\theta(t)\,dt\). This calculation proves equality on every Schwartz test.

**Proposition 4.1 (the absolute quadratic).** The pointwise decomposition
\[
|x^2-1|=x^2-1+2(1-x^2)_+
\tag{4.1}
\]
gives the whole transform
\[
F|x^2-1|=-2\pi\delta''_0-2\pi\delta_0
 +8\frac{\sin\xi-\xi\cos\xi}{\xi^3}.
\tag{4.2}
\]
**Proof.** The decomposition is checked separately on \(|x|\le1\) and \(|x|\ge1\). To compute the compact term, let \(J(\xi)=\int_{-1}^1e^{-ix\xi}dx=2\sin\xi/\xi\). Differentiation under this finite integral twice is justified by domination by \(x^2\), and
\[
F[(1-x^2)_+](\xi)=J(\xi)+J''(\xi)
=4\frac{\sin\xi-\xi\cos\xi}{\xi^3}\quad(\xi\ne0).
\]
The derivative calculation is
\(J''=2[-\sin\xi/\xi-2\cos\xi/\xi^2+2\sin\xi/\xi^3]\).
At zero, the original integral is \(\int_{-1}^1(1-x^2)dx=4/3\). All higher derivatives of the finite integral exist by the same domination, so its extension is smooth. Twice this term has value \(8/3\); the only point terms come from \(x^2-1\) through (1.1). \(\square\)

## Parseval keeps its factor through a norm limit

**Lemma 5.1 (cutoff passage in Parseval).** Suppose a smooth \(f\in L^2(\mathbb R)\) has tempered Fourier transform equal to a regular \(v\in L^2(\mathbb R)\). Then
\(\|v\|_2^2=2\pi\|f\|_2^2\).

**Proof.** Choose \(0\le\eta\le1\) compact smooth and equal to one near zero. The functions \(f_R=\eta(\cdot/R)f\) are compact smooth, hence Schwartz, and tend to \(f\) in \(L^2\) by dominated convergence. The exact Schwartz identity from U041, Lemma 0.1, gives
\(\|Ff_R-Ff_S\|_2^2=2\pi\|f_R-f_S\|_2^2\).
The supplied \(L^2\) completeness proof gives a limit \(w\in L^2\). For \(\theta\in\mathcal S\), Cauchy–Schwarz gives
\[
\int (Ff_R)\theta\longrightarrow\int w\theta,\qquad
\int f_R F\theta\longrightarrow\int fF\theta.
\]
The two integrals before the limits are equal by transposition. Thus \(w=v\) as distributions and almost everywhere. To justify the last implication, on each compact set the locally integrable difference has zero smooth-test integrals; the mollification and local \(L^1\) approximation proof in the integration foundation makes that difference zero in \(L^1\) on every smaller compact set. Exhaustion gives the almost-everywhere claim. Taking limits of norms, using \(|\|u\|_2-\|z\|_2|\le\|u-z\|_2\), proves the lemma. \(\square\)

Apply it to \(f_0=(1+x^2)^{-1}\) and \(f_1=x/(1+x^2)\). Their squared tails are bounded by \(x^{-4}\) and \(x^{-2}\); the transforms from (2.1) have square \(\pi^2e^{-2|\xi|}\). All four functions therefore lie in \(L^2\), and
\[
\begin{aligned}
\int\frac{dx}{(1+x^2)^2}
 &=\frac1{2\pi}\int\pi^2e^{-2|\xi|}d\xi=\frac\pi2,\\
\int\frac{x^2\,dx}{(1+x^2)^2}
 &=\frac1{2\pi}\int\pi^2e^{-2|\xi|}d\xi=\frac\pi2.
\end{aligned}
\tag{5.1}
\]
The exponential integral is \(2\int_0^\infty e^{-2t}dt=1\). No factor changes in the norm limit.

## A spectral gap removes the unbounded primitive

**Theorem 6.1 (bounded primitives from a spectral gap).** If \(f\in C_b(\mathbb R)\) and \(Ff\) vanishes on a neighborhood of zero, every distributional primitive is a bounded classical \(C^1\) function. There is exactly one primitive \(u_0\) whose Fourier transform vanishes near zero. Its Fourier support equals \(\operatorname{supp}Ff\). All other primitives are \(u_0+C\).

**Proof: an integrable inverse derivative.** Choose \(\chi\in\mathcal D\), supported inside the gap and equal to one near zero, and put \(h=G\chi\). Then \(h\in\mathcal S\), \(\int h=Fh(0)=1\), and U040, Lemma 2.1, gives \(h*f=0\), because its Fourier transform is \(\chi Ff=0\). Define
\[
k(x)=H(x)-\int_{-\infty}^x h(t)\,dt.
\tag{6.1}
\]
For \(x<0\) this is minus the left tail integral; for \(x>0\) it is the right tail integral. For each integer \(L>1\), the Schwartz bound \(|h(t)|\le C_L(1+|t|)^{-L}\) gives \(|k(x)|\le C'_L(1+|x|)^{1-L}\) on both tails by direct integration. It is bounded on finite intervals. Thus \(k\in L^1\), and \(\int\langle x\rangle^r|k(x)|dx<\infty\) for every \(r\ge0\).

Integration by parts on each half-line proves \(H'=\delta_0\). FTC gives the derivative of the integral in (6.1), so \(k'=\delta_0-h\). Consequently \(i\xi Fk=1-\chi\). The ordinary \(L^1\) transform \(Fk\) is continuous, by dominated convergence. Away from zero it is therefore the smooth function
\[
Fk(\xi)=m(\xi)=\frac{1-\chi(\xi)}{i\xi},
\tag{6.2}
\]
and near zero it extends as zero. Indeed division of the distributional identity gives equality off zero; two continuous functions with equal distributions on an open set agree there by a nonnegative bump test after rotating a nonzero difference. Continuity at zero completes (6.2). In particular \(\int k=m(0)=0\). The derivatives of \(m\) are bounded: outside a compact interval they are constant multiples of inverse powers of \(\xi\); on the remaining compact transition region they are smooth, and near zero they vanish.

**Proof: construct and classify the primitives.** Set \(u_0=k*f\). The integral converges absolutely with
\(\|u_0\|_\infty\le\|k\|_1\|f\|_\infty\), and dominated convergence makes it continuous. Its distributional derivative is \(f-h*f=f\). In detail, for a compact test \(\theta\), Fubini rewrites
\[
-\int u_0(x)\theta'(x)dx
=\int f(y)\left[-\int k(z)\theta'(z+y)dz\right]dy.
\]
The inner bracket is \(\theta(y)-\int h(z)\theta(z+y)dz\), by \(k'=\delta_0-h\). Both uses of Fubini are absolutely justified, respectively by
\(\|f\|_\infty\|k\|_1\|\theta'\|_1\) and
\(\|f\|_\infty(1+\|h\|_1)\|\theta\|_1\).
The resulting pairing is exactly that of \(f-h*f\).

Here are the required classical and distributional uniqueness facts. If \(T'=0\) on the line, every compact smooth test \(\theta\) of integral zero has compact smooth primitive \(\Theta(x)=\int_{-\infty}^x\theta(t)dt\). Thus \(T(\theta)=T(\Theta')=0\). For a fixed compact smooth \(\rho\) of integral one, apply this to \(\theta-\rho\int\theta\), obtaining \(T(\theta)=T(\rho)\int\theta\). Hence \(T\) is a constant distribution. The classical function \(J(x)=\int_0^x f(t)dt\) has derivative \(f\) by FTC; therefore \(u_0-J\) is constant as a distribution. Since both are continuous, the bump-test argument makes the equality pointwise. This proves \(u_0\in C^1\), and every distributional primitive equals \(u_0+C\). Each is bounded.

**Proof: exact Fourier support.** Choose another compact smooth \(\eta\), equal to one near zero and supported in the gap, and put \(r=G\eta\). U040 gives \(r*f=0\). Associating the two integrable kernels with bounded \(f\) is permitted by the bound \(\|r\|_1\|k\|_1\|f\|_\infty\); hence
\[
r*u_0=r*(k*f)=k*(r*f)=0.
\]
U040 again gives \(\eta Fu_0=0\), so \(Fu_0\) vanishes near zero. The smooth bounded-derivative multiplier \(m\) acts on \(\mathcal S'\) by the product rule. Since \(i\xi Fu_0=Ff\) and \(i\xi mFf=(1-\chi)Ff=Ff\), their difference is supported at zero and is killed by \(\xi\). The coordinate-division proof in Section 2 makes it \(c\delta_0\); both terms vanish near zero, so \(c=0\). Thus
\[
Fu_0=mFf,\qquad
\operatorname{supp}Fu_0=\operatorname{supp}Ff.
\tag{6.3}
\]
Multiplication cannot enlarge support. Near each point of \(\operatorname{supp}Ff\), \(\chi=0\), the point is nonzero, and \(m=1/(i\xi)\) has a smooth nonvanishing reciprocal; multiplication by that reciprocal gives the reverse support inclusion. Here \(\chi=0\) near the support because its compact support lies inside the open gap. Finally
\[
\begin{gathered}
Fu=mFf+2\pi C\delta_0,\\
\operatorname{supp}Fu=
\begin{cases}
\operatorname{supp}Ff,&C=0,\\
\operatorname{supp}Ff\cup\{0\},&C\ne0.
\end{cases}
\end{gathered}
\tag{6.4}
\]
The supports are separated near zero, so they cannot cancel. This proves uniqueness of the primitive avoiding zero and includes \(f=0\). \(\square\)

## Exercises

**Exercise 1 (foundation).** For \(a>0\), \(b\in\mathbb R\), find the complete transform and exact support of \(e^{ibx}\sin(ax)/x\), including its value at the physical origin.

**Exercise 2 (intermediate).** Classify the primitives of \(\cos(3x)+2\sin(5x)\). Find the one with a spectral gap, its exact support and a uniform bound.

**Exercise 3 (foundation).** Find the primitive of \(e^{iax}\), \(a\ne0\), with spectrum avoiding zero. Compute its norm, and show why a spectral gap and dependence on its size are necessary.

**Exercise 4 (intermediate).** Transform \((x-b)H(x-b)\), displaying both point terms separately from the smoothly modulated finite part.

**Exercise 5 (advanced).** For \(a>0\) and real \(b,c\), transform \(\arctan((x-b)/a)+c\). Define its weighted principal value and check the derivative equation with the zero-frequency term retained.

**Exercise 6 (advanced).** Derive the triangular transform of \((\sin x/x)^2\) by a finite frequency integral. Compute \(\int(\sin x/x)^2dx\) and \(\int(\sin x/x)^4dx\).

**Exercise 7 (intermediate).** Use Parseval to compute \(\int(a^2+x^2)^{-2}dx\) and \(\int x^2(a^2+x^2)^{-2}dx\), for \(a>0\).

**Exercise 8 (advanced).** Compute the complete transform of \(|x^2-a^2|\), including its two point terms and compact-correction value at zero. Prove its weak tempered limit as \(a\downarrow0\).

## Solutions

**Solution 1.** The identity \(\sin(ax)/x=\frac12\int_{-a}^ae^{itx}dt\) gives value \(a\) at zero. Pairing with \(F\theta\), the absolute bound is \(a\|F\theta\|_1\); Fubini and (1.1) give \(\pi1_{[-a,a]}\). Modulation translates it to \(\pi1_{[b-a,b+a]}\). This distribution vanishes outside the closed interval and is nonzero on every neighborhood of every point in it: such a neighborhood meets its interior in an open interval, where a nonnegative nonzero bump has positive pairing. Its exact support is therefore \([b-a,b+a]\).

**Solution 2.** Take \(u_0=\frac13\sin(3x)-\frac25\cos(5x)\). Its derivative is the prescribed function and
\[
Fu_0=\frac{\pi}{3i}(\delta_3-\delta_{-3})
 -\frac{2\pi}{5}(\delta_5+\delta_{-5}).
\]
All coefficients are nonzero; bumps separating the four points prove exact support \(\{-5,-3,3,5\}\). There is a gap at zero. Theorem 6.1 makes every primitive \(u_0+C\), with support enlarged by zero precisely when \(C\ne0\). The triangle inequality gives \(\|u_0\|_\infty\le1/3+2/5=11/15\); this is an upper bound, without a claim of simultaneous extrema.

**Solution 3.** The required primitive is \(u_0=e^{iax}/(ia)\), with transform \(2\pi\delta_a/(ia)\) and exact norm \(1/|a|\). Theorem 6.1 proves uniqueness. These right sides all have norm one, while the primitive norms diverge as \(a\to0\); a uniform bound independent of gap size is impossible. For \(f=1\), the spectrum is \(2\pi\delta_0\), and all primitives \(x+C\) are unbounded. Thus boundedness of the right side alone does not imply boundedness of its primitive.

**Solution 4.** Translation multiplies (3.2)'s ramp transform by \(g(\xi)=e^{-ib\xi}\). Direct testing gives \(g\delta'_0=g(0)\delta'_0-g'(0)\delta_0=\delta'_0+ib\delta_0\). Hence
\[
F[(x-b)H(x-b)]
=i\pi\delta'_0-\pi b\delta_0
 -e^{-ib\xi}\operatorname{pf}(1/\xi^2).
\]
The multiplier is smooth with bounded derivatives, so its product with the finite part is well defined. Its derivative normalization remains the one fixed in Section 3. The additional mass \(-\pi b\delta_0\) is part of the whole transform.

**Solution 5.** Put
\[
A_a(\theta)=\int_0^\infty e^{-at}
 \frac{\theta(t)-\theta(-t)}t\,dt .
\]
FTC bounds the near-zero quotient, and the exponential bounds the tail; this is a tempered odd symmetric principal value. Multiplication gives \(\xi A_a=e^{-a|\xi|}\). The dilation rule applied to the whole arctangent transform replaces \(A\) by \(A_a\): in its test pairing substitute \(t=a\xi\), including the test-scaling factor. Translation and the added constant then give
\[
F[\arctan((x-b)/a)+c]
=-i\pi e^{-ib\xi}A_a+2\pi c\delta_0.
\]
Multiplication by \(i\xi\) gives \(\pi e^{-ib\xi-a|\xi|}\). Independently the physical derivative is \(a/(a^2+(x-b)^2)\), whose Cauchy transform is this same expression by dilation and translation. The constant mass is retained even though differentiation kills it.

**Solution 6.** Multiplying two ordinary finite integrals gives
\[
(\sin x/x)^2=\frac14\int_{[-1,1]^2}e^{i(s+t)x}\,ds\,dt.
\]
Against a Schwartz Fourier test, the absolute integral is at most \(\|F\theta\|_1\). Fubini and (1.1) give \(\frac\pi2\int_{[-1,1]^2}\theta(s+t)dsdt\). Set \(\xi=s+t\); for fixed \(\xi\), the allowed \(s\) interval is \([-1,1]\cap[\xi-1,\xi+1]\), of length \((2-|\xi|)_+\). Thus the whole transform is
\[
F[(\sin x/x)^2](\xi)=\frac\pi2(2-|\xi|)_+.
\]
The physical square is integrable, being bounded near zero and at most \(x^{-2}\) on the tails. Its ordinary transform is continuous and agrees with the displayed continuous triangle as a distribution, hence pointwise by the bump argument. Evaluation at zero gives \(\int(\sin x/x)^2dx=\pi\).

The physical square is also smooth and in \(L^2\), and the triangle is in \(L^2\). Smoothness at zero follows by differentiating the finite exponential integral. Lemma 5.1 therefore gives
\[
\int(\sin x/x)^4dx
=\frac1{2\pi}\frac{\pi^2}{4}
 \int_{-2}^{2}(2-|\xi|)^2d\xi
=\frac\pi8\frac{16}3=\frac{2\pi}3.
\]
Every quotient has its continuous value at zero.

**Solution 7.** Dilation and the coordinate identity give
\[
F[(a^2+x^2)^{-1}]=\frac\pi a e^{-a|\xi|},\qquad
F[x/(a^2+x^2)]=-i\pi\operatorname{sgn}(\xi)e^{-a|\xi|}.
\]
There is no delta in the derivative of the continuous exponential, by the half-line boundary cancellation already proved. All four functions lie in \(L^2\) by their explicit tails. Lemma 5.1 and \(\int e^{-2a|\xi|}d\xi=1/a\) yield, respectively,
\[
\int\frac{dx}{(a^2+x^2)^2}=\frac{\pi}{2a^3},
\qquad
\int\frac{x^2\,dx}{(a^2+x^2)^2}=\frac{\pi}{2a}.
\]

**Solution 8.** The physical function is \(a^2|(x/a)^2-1|\), so its transform is \(a^3F|x^2-1|(a\xi)\). The distributional scaling definition gives \(\delta_0(a\cdot)=a^{-1}\delta_0\) and \(\delta''_0(a\cdot)=a^{-3}\delta''_0\), by testing the value and second derivative of \(\theta(\cdot/a)\). Therefore
\[
F|x^2-a^2|
=-2\pi\delta''_0-2\pi a^2\delta_0
 +8\frac{\sin(a\xi)-a\xi\cos(a\xi)}{\xi^3}.
\]
The compact correction's value at zero is \(8a^3/3\), either by scaling the original compact integral or Taylor's formula. The inequality
\(\big||x^2-a^2|-x^2\big|\le a^2\) bounds each physical Schwartz pairing difference by \(a^2\|\theta\|_1\). Thus the physical distributions converge weakly to \(x^2\); Fourier continuity gives the whole limit \(-2\pi\delta''_0\). The vanishing mass term and compact correction can also be checked separately: \(2(a^2-x^2)_+\) has integral \(8a^3/3\), so its Fourier pairing is bounded by that number times \(\|F\theta\|_\infty\).

## References

- Terence Tao, [*Lecture Notes 2, Math 247A*](https://www.math.ucla.edu/~tao/247a.1.06f/notes2.pdf), Fall 2006, PDF pages 19–20, Fourier symmetries and Schwartz Parseval. The source uses \(2\pi\) in the phase; the exact convention conversion is proved through the supplied inversion and U041, Lemma 0.1. The source's polynomial-Gaussian density assertion and interpolation results are not assumed here.
- [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [U040](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1; [U041](separated-frequencies-and-distributional-order.md), Lemma 0.1; [U045](positive-kernels-and-spectral-measures.md), Solution 2; and the supplied scalar and integration foundations at the exact sections listed above. The pole limits, zero-derivative classification, compact quadratic transform and spectral primitive are proved in this lesson. Component licences are retained.
