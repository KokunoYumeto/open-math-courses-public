# Sharp bounds for compact spectra

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); linked prerequisites retain their stated licences.*

A compact Fourier band controls derivatives with sharp norm constants. We construct the finite signed measures with explicitly summable atoms that realize a derivative and every sine-cosine combination, including the closed band endpoints. In several dimensions, a compact spectrum also gives an entire extension whose complex-translation norm is controlled by its actual support function. That support function can be negative in a direction, and no polynomial loss is needed.

We use \(Fu(\xi)=\int e^{-ix\cdot\xi}u(x)dx\), \(D=-i\partial\), and bilinear distributional pairings. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves inversion and the coordinate rules; the [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16, prove the calculus, convergence, norms and absolute integration inputs. [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B1, supplies compact-distribution pairing, finite order and smooth parameter interchange. [Tempered growth and spectral cutoffs](tempered-growth-and-spectral-cutoffs.md), Lemma2.1 and Theorem3.1, proves full Schwartz convolution and compact-spectrum fixed points. [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, proves smooth periodic expansion and continuous Fourier uniqueness at every period. [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary2.2 and formulas(2.3)–(2.4), supplies Cauchy's formula, Taylor expansion and coefficient bounds. We prove the identity and maximum principles from those formulas below. No external proof citation is an input in place of a programme proof.

## The local complex-variable input

**Lemma 0.1 (identity and maximum principles).** On a connected open subset of \(\mathbb C\), a holomorphic function with a limit point of distinct zeros in that open set is identically zero. If its modulus has a local maximum at an interior point, it is constant.

**Proof.** Use the full Taylor formula of [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary2.2. If the first nonzero coefficient at a zero has index \(m\), factor the local series as \((z-a)^m(c_m+O(z-a))\). Continuity and \(c_m\ne0\) show that this zero is isolated. A limit point of zeros therefore forces every Taylor coefficient to vanish, so the function is zero on a neighborhood. The set of points near which it is zero is open. It is also relatively closed: at a limit point, all derivatives vanish by continuity, hence the Taylor series is zero nearby. Connectedness makes this nonempty set the entire domain.

Now suppose \(|f(z)|\le |f(a)|\) near \(a\). If \(f(a)=0\), then \(f=0\) there and the preceding conclusion applies. Otherwise put \(h=f/f(a)\). On a sufficiently small closed disk around \(a\), \(|h|\le1\) and \(h(a)=1\). Cauchy's formula at the center gives
\[
 1=\frac1{2\pi}\int_0^{2\pi}h(a+re^{it})\,dt.
\]
The continuous function \(1-\operatorname{Re}h\) on this circle is nonnegative and has integral zero; if it were positive at one point, continuity would make its integral positive on a short interval. Thus \(\operatorname{Re}h=1\) everywhere on the circle. Together with \(|h|\le1\) this forces \(h=1\) there. Cauchy's formula inside that circle, applied to \(h-1\), makes \(h=1\) throughout the disk. Apply the identity conclusion to \(f-f(a)\). \(\square\)

## A derivative as an exact finite signed measure

**Theorem 1.1.** Define a continuous four-periodic function \(b\) by \(b(\xi)=i\xi\) for \(-1\le\xi\le1\) and \(b(\xi)=i(2-\xi)\) for \(1\le\xi\le3\). Then the full inverse Fourier distribution is the finite signed measure
\[
\begin{gathered}
K=\frac4{\pi^2}\sum_{k\in\mathbb Z}\\
{}\times\frac{(-1)^k}{(2k-1)^2}\delta_{(2k-1)\pi/2},\\
FK=b,\qquad\|K\|_{\rm TV}=1.
\end{gathered}
\tag{1.1}
\]
For every bounded input with Fourier support contained in \([-1,1]\), use its canonical smooth representative. Its ordinary derivative satisfies \(u'=K*u\) at every point, with absolute uniform convergence of this atom convolution and \(\|u'\|_\infty\le\|u\|_\infty\). This includes the original open support condition. The constant one is sharp; every nonzero \(u(x)=a e^{ix}+c e^{-ix}\) attains equality of the two supremum norms.

**Proof of the full multiplier and measure.** The values at \(-1,3\) agree and the values at \(1\) agree. Its ordinary derivative is \(+i\) on \((-1,1)\) and \(-i\) on \((1,3)\). At \(1+4j\) this derivative has jump \(-2i\), and at \(-1+4j\) jump \(+2i\). Periodwise integration by parts therefore gives the complete periodic second derivative
\[
b''=2iC_{-1+4\mathbb Z}-2iC_{1+4\mathbb Z}.
\]
For the periodic Fourier coefficient
\(d_n=\frac14\int_{-1}^3 b(\xi)e^{-i\pi n\xi/2}d\xi\),
the two source coefficients are \(i(e^{i\pi n/2}-e^{-i\pi n/2})/2=-\sin(\pi n/2)\).
Thus for \(n\ne0\),
\[
\begin{gathered}
-\frac{\pi^2n^2}{4}d_n=-\sin(\pi n/2),\\
d_n=\frac4{\pi^2n^2}\sin(\pi n/2).
\end{gathered}
\]
The zero coefficient is zero by direct integration of the two linear pieces. All even coefficients vanish. The coefficients are absolutely summable, so their series is uniformly convergent to a continuous periodic function. Its coefficients agree with those of \(b\); the full continuous Fourier uniqueness proof in [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, at period4, identifies the sum at every point.

The Fourier transform of a point mass at \(s\) is \(e^{-is\xi}\) on the whole tempered space. In (1.1) put \(n=1-2k\); then
\(\sin(\pi n/2)=(-1)^k\) and \(e^{i\pi n\xi/2}=e^{-i(2k-1)\pi\xi/2}\).
The stated measure therefore has transform exactly \(b\), including all corners and zero. Its total variation is finite by the summable reciprocal squares. To compute it without importing a separate zeta identity, evaluate this absolute transform series at \(\xi=1\). Each term has the same phase \(i\), since
\[
(-1)^ke^{-i(2k-1)\pi/2}=i.
\]
As \(b(1)=i\), the sum of the positive absolute weights is one. Hence \(\|K\|_{\rm TV}=1\) exactly. Fourier inversion on \(\mathcal S'\) identifies the inverse distribution uniquely.

**Proof of the whole derivative identity.** First suppose \(S=\operatorname{supp}Fu\) is compactly contained in \((-1,1)\). The full spectral cutoff theorem [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md), Theorem 3.1 chooses \(\eta\in C_c^\infty((-1,1))\), equal one near \(S\), and \(f=G\eta\in\mathcal S\), such that \(u=u*f\). It also supplies the canonical smooth representative. Since \(u\) is bounded, its representative has supremum equal to its essential bound: a continuous value above that bound would persist on an interval of positive measure.

The function \(K*f\) belongs to \(L^1\), with norm at most \(\|K\|_{\rm TV}\|f\|_1\), by absolute Fubini. Its ordinary Fourier transform is \(b\eta=i\xi\eta=Ff'\), again by absolute Fubini. Whole Fourier inversion gives \(K*f=f'\). Both sides are continuous: the atom sum converges uniformly by the bound \(\|f\|_\infty\|K\|_{\rm TV}\), and each summand is continuous. Thus equality holds everywhere.

Absolute double integration, with bound \(\|u\|_\infty\|K\|_{\rm TV}\|f\|_1\), now gives
\[
\begin{gathered}
K*u=K*(u*f)\\
=u*(K*f)=u*f'=u'.
\end{gathered}
\tag{1.2}
\]
The last differentiation and its full distributional interpretation are the complete global Schwartz convolution lemma [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1. The sum defining \(K*u\) has tails uniformly bounded on the whole line by \(\|u\|_\infty\) times the omitted total variation. It is consequently an absolutely uniformly convergent continuous series.

For the closed-band endpoint \(S\subset[-1,1]\), let \(u_t(x)=u(tx)\), \(0<t<1\). Positive dilation sends its Fourier support to \(tS\subset(-1,1)\), and its bound is the same as that of \(u\). Therefore \(u_t'=K*u_t\). As \(t\uparrow1\), the left side \(t u'(tx)\) tends locally uniformly to \(u'(x)\). Each fixed summand on the right tends locally uniformly to the corresponding \(u(x-s)\), by continuity on compact intervals. The uniform tail bound independent of \(t\) then proves locally uniform convergence to \(K*u\). This proves (1.2) on the whole closed band. Taking absolute values and using total variation one proves the derivative inequality.

For \(u=a e^{ix}+c e^{-ix}\), both its norm and its derivative norm equal \(|a|+|c|\): the varying relative phase \(e^{2ix}\) aligns the two complex terms for the supremum; after differentiation the relative phase still runs through the full unit circle. This includes a single nonzero term and proves sharpness. \(\square\)

## Every sine-cosine derivative combination contracts every norm

**Theorem 2.1.** For every \(1\le p\le\infty\), \(\lambda>0\), real \(\alpha\), and \(u\in L^p(\mathbb R)\) with Fourier support in \([-\lambda,\lambda]\), its canonical smooth representative satisfies
\[
\left\|\frac{\sin\alpha}{\lambda}u'+\cos\alpha\,u\right\|_p
\le\|u\|_p.
\tag{2.1}
\]
At \(\lambda=1\), a complete convolution formula is
\[
\sin\alpha\,u'+\cos\alpha\,u=K_\alpha*u,
\tag{2.2}
\]
where, if \(\alpha\notin\pi\mathbb Z\),
\[
\begin{gathered}
K_\alpha=\sum_{k\in\mathbb Z}\\
{}\times\frac{(-1)^k\sin^2\alpha}{(\pi k-\alpha)^2}\delta_{\pi k-\alpha},\\
\|K_\alpha\|_{\rm TV}=1.
\end{gathered}
\tag{2.3}
\]
If \(\alpha=\pi m\), set \(K_\alpha=(-1)^m\delta_0\). All measure series and convolution claims are absolute in their stated norms. No pointwise interpretation of a bare \(L^p\) equivalence class is assumed.

**Proof of the full finite measure.** On \([-1,1]\) put
\[
\Phi_\alpha(\xi)=(\cos\alpha+i\xi\sin\alpha)e^{-i\alpha\xi}
\]
and extend with period 2. Both endpoint values are one, so this extension is continuous. For its coefficient of \(e^{i\pi n\xi}\), let \(\beta=\alpha+\pi n\). Direct finite integration gives
\[
c_n=\cos\alpha\,\frac{\sin\beta}{\beta}
-\sin\alpha\,\left(\frac{\sin\beta}{\beta}\right)'.
\]
The two integral values and their derivative are legitimate also at zero, with their removable limits. For \(\alpha\notin\pi\mathbb Z\), no \(\beta\) vanishes, and
\(\sin\beta=(-1)^n\sin\alpha\), \(\cos\beta=(-1)^n\cos\alpha\).
The linear numerator terms cancel, leaving
\[
c_n=\frac{(-1)^n\sin^2\alpha}{(\alpha+\pi n)^2}.
\]
They are absolutely summable. The same full Fejér uniqueness argument as in Theorem 1.1 identifies their uniformly convergent series with the full continuous periodic \(\Phi_\alpha\). Multiply by \(e^{i\alpha\xi}\) and set \(k=-n\). The absolute atom series (2.3) has full transform \(e^{i\alpha\xi}\Phi_\alpha(\xi)\); in particular on the whole closed interval \([-1,1]\) it equals \(\cos\alpha+i\xi\sin\alpha\).

At \(\xi=1\), each transformed measure term has phase \(e^{i\alpha}\) times its positive absolute weight, since
\((-1)^ke^{-i(\pi k-\alpha)}=e^{i\alpha}\).
Its full transform there is \(e^{i\alpha}\). Thus the sum of its absolute weights is one. If \(\alpha=\pi m\), the displayed trigonometric combination is simply \((-1)^m u\), and the prescribed single point mass gives precisely that multiplier and the same norm. This handles every apparent zero denominator without assigning an undefined series value.

**Proof of the full convolution identity.** Every compact-band \(L^p\) input is tempered by Hölder against a Schwartz test. The complete [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md) spectral cutoff theorem supplies \(u=u*f\), \(f\in\mathcal S\), and its smooth representative. For every derivative the absolutely convergent convolution bound
\(|u*f^{(j)}(x)|\le\|u\|_p\|f^{(j)}\|_{p'}\)
is uniform in \(x\); it includes \(p=1,\infty\). In particular this representative is bounded.

If the support is compactly contained in \((-1,1)\), choose \(f=G\eta\) with \(\eta\) compactly supported in that open interval and equal one near the support. The same absolute \(L^1\) Fourier calculation as in Theorem 1.1 gives
\[
K_\alpha*f=\sin\alpha\,f'+\cos\alpha\,f
\]
on the whole line, since its transformed identity is the smooth compact function
\(\eta(\xi)(\cos\alpha+i\xi\sin\alpha)\).
Using the bounded representative, the same double absolute integration proves (2.2). It is simultaneously a whole distribution identity and an everywhere identity of continuous functions.

The finite measure has an \(L^p\) contraction bound on arbitrary inputs: for a finite atom sum, the triangle inequality in \(L^p\) and translation invariance give a norm at most the sum of absolute weights times \(\|u\|_p\). For \(p<\infty\), omitted tails have norm at most their omitted total variation times \(\|u\|_p\), so the series converges in the complete \(L^p\) space. For bounded inputs it converges uniformly by the supremum bound, including \(p=\infty\). The finite-sum bound passes to the limit. This proves (2.1) on the open band, including both norm endpoints; the norm triangle, completeness and integral convergence are proved in the supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4.

For the closed band take \(u_t(x)=u(tx)\), \(0<t<1\). It has open-band support, and \(\|u_t\|_p=t^{-1/p}\|u\|_p\), with \(t^{-1/\infty}=1\). Its combination converges pointwise to \(\sin\alpha\,u'(x)+\cos\alpha\,u(x)\) by smoothness. For finite \(p\), Fatou gives the integral inequality with limit \(t^{-1}\|u\|_p^p\to\|u\|_p^p\). At \(p=\infty\), pass to the limit in the everywhere bound \(|\sin\alpha\,u_t'(x)+\cos\alpha\,u_t(x)|\le\|u\|_\infty\); the smooth representatives have that bound everywhere. The uniform finite-measure tail argument in Theorem 1.1 also passes (2.2) itself to the closed band.

Finally reduce arbitrary \(\lambda>0\) to one by \(v(t)=u(t/\lambda)\). Its Fourier support lies in \([-1,1]\), its derivative is \(\lambda^{-1}u'(t/\lambda)\), and its norm is \(\lambda^{1/p}\|u\|_p\). The same norm factor occurs on both sides, proving exactly (2.1). Equivalently push every atom of \(K_\alpha\) to its location divided by \(\lambda\); the total variation remains one and its multiplier is the stated sine-cosine combination on the full closed band. Zero inputs and \(\alpha\in\pi\mathbb Z\) are included. \(\square\)

**Corollary 2.2 (directional bounds from the projected spectrum).** Let \(u\in L^p(\mathbb R^n)\), \(1\le p\le\infty\), have nonempty compact spectrum \(S\). For \(a\in\mathbb R^n\), set \(R_a=\max_{\xi\in S}|a\cdot\xi|\). If \(R_a>0\), then for every real \(\alpha\),
\[
 \left\|\frac{\sin\alpha}{R_a}(a\cdot\nabla)u+\cos\alpha\,u\right\|_p
 \le\|u\|_p.
\]
For every integer \(m\ge1\),
\[
 \|(a\cdot\nabla)^m u\|_p\le R_a^m\|u\|_p.
\]
If \(R_a=0\), every positive directional derivative is zero.

**Proof.** For any \(\rho>0\), push the scale-\(\rho\) measure in Theorem2.1 along \(s\mapsto sa\). It has total variation at most one, and its full Fourier transform at \(\xi\) is that measure's one-dimensional transform at \(a\cdot\xi\). On \(|a\cdot\xi|\le\rho\) it equals \(\cos\alpha+i(a\cdot\xi)\sin\alpha/\rho\). If \(S\) lies in the open slab, choose a compact cutoff there equal to one near \(S\). Theorem2.1's argument now works with its inverse transform \(f\in\mathcal S(\mathbb R^n)\): absolute integration gives the whole transform identity for the pushed measure convolved with \(f\), Fourier injectivity identifies it with \(\cos\alpha f+\sin\alpha(a\cdot\nabla)f/\rho\), and boundedness of the canonical representative justifies the associativity with \(u\). The bound \(\|u*f\|_\infty\le\|u\|_p\|f\|_{p'}\) is valid in every dimension. Each translated atom has the same \(L^p\) norm as the input; the absolute tails and completeness give the contraction at all \(p\).

For a closed slab, use \(u_t(x)=u(tx)\), \(0<t<1\). Its spectrum is \(tS\); its norm is \(t^{-n/p}\|u\|_p\), and its directional derivative is \(t(a\cdot\nabla)u(tx)\). The pointwise limit and Fatou give the finite-\(p\) inequality; for \(p=\infty\), use the everywhere smooth-representative bound. Uniform atom tails also give the convolution identity in the limit. Take \(\rho=R_a>0\), then \(\alpha=\pi/2\). Each derivative remains in the same spectral slab since its transform is multiplied by \(i(a\cdot\xi)\); iteration proves every order. If \(R_a=0\), apply the first derivative estimate at every \(\rho>0\) and let \(\rho\downarrow0\). The continuous derivative of norm zero vanishes everywhere; all its further derivatives vanish. \(\square\)

## Entire extensions and sharp complex-translation norms

**Theorem 3.1.** Let \(1\le p\le\infty\), \(u\in L^p(\mathbb R^n)\), and \(S=\operatorname{supp}Fu\) be compact. If \(S\ne\varnothing\), define its actual support function
\[
H(\eta)=\sup_{\xi\in S}\eta\cdot\xi.
\]
The canonical smooth representative of \(u\) extends uniquely to an entire function on \(\mathbb C^n\), and, for every \(y\in\mathbb R^n\),
\[
\|u(\,\cdot+iy)\|_p
\le e^{H(-y)}\|u\|_p.
\tag{3.1}
\]
The norm on the left uses the original Lebesgue measure in the original real coordinates. There is no polynomial prefactor. If \(S=\varnothing\), then \(u=0\) and every complex translate is zero.

**Construction and the precise preliminary growth bound.** Hölder against Schwartz tests makes \(u\) tempered, including both norm endpoints. Put \(T=Fu\). [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0, gives its canonical continuous action on smooth functions, with a finite-order bound after one compact cutoff. Define
\[
U(z)=(2\pi)^{-n}\langle T(\xi),e^{iz\cdot\xi}\rangle.
\tag{3.2}
\]
The action includes any compact cutoff equal to one near \(S\), and is independent of that cutoff. On fixed compact sets in both \(z\) and \(\xi\), the exponential series and each of its finitely many \(\xi\)-derivatives converge uniformly: a derivative of order at most \(N\) of its \(k\)-th term is bounded by a fixed geometric power times a polynomial in \(k\), divided by \(k!\). The compact finite-order bound therefore permits applying \(T\) term by term. The same estimates after \(z\)-differentiation show local uniform convergence of all resulting derivatives. This proves that (3.2) is entire, in the full \(n\)-variable power-series sense.

For every \(\delta>0\), choose a compact smooth cutoff \(\chi_\delta\) equal to one near \(S\), with support in the closed \(\delta\)-neighbourhood of \(S\). The common finite-order estimate on this fixed compact support yields constants \(C_\delta,N_\delta\) such that
\[
\begin{gathered}
|U(z)|\le C_\delta(1+|z|)^{N_\delta}\\
{}\times\exp\!\bigl(H(-\operatorname{Im}z)\\
{}+\delta|\operatorname{Im}z|\bigr).
\end{gathered}
\tag{3.3}
\]
Indeed each derivative of \(\chi_\delta(\xi)e^{iz\cdot\xi}\) has at most a polynomial factor in \(z\), and its exponential modulus is \(e^{-\operatorname{Im}z\cdot\xi}\). The maximum of that exponent on the stated neighbourhood is at most \(H(-\operatorname{Im}z)+\delta|\operatorname{Im}z|\). No sign or positivity assumption on \(H\) has entered.

On the real subspace (3.3) has polynomial growth. For a Schwartz test \(\theta\), the finite-order bound justifies interchanging the compact-distribution action with its absolutely convergent real integral, including all required \(\xi\)-derivatives. This gives
\[
\begin{gathered}
\int U(x)\theta(x)\,dx\\
=(2\pi)^{-n}\langle T(\xi),F\theta(-\xi)\rangle\\
=\langle GT,\theta\rangle=\langle u,\theta\rangle.
\end{gathered}
\]
Whole Fourier inversion proves the second-to-last identification. Hence \(U\) agrees with the [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md) smooth representative. For that representative, a continuous value above an essential supremum would persist on a set of positive measure, so in the bounded case the essential and pointwise bounds agree.

Uniqueness follows by iterating Lemma0.1's one-variable identity principle. An entire function zero on \(\mathbb R^n\) is zero everywhere: fix all but its first coordinate real, use that principle, then allow the first coordinate to be arbitrarily complex and continue through the remaining coordinates. We henceforth write \(u(z)\) for \(U(z)\).

**A half-plane bound with polynomial growth.** We use the following consequence of Lemma0.1. Suppose \(g\) is holomorphic above the real axis, continuous on its closure, satisfies \(|g(s)|\le M\) for real \(s\), and
\[
|g(w)|\le C(1+|w|)^N\qquad(\operatorname{Im}w\ge0).
\]
Then \(|g(w)|\le M\) throughout that half-plane.

To prove this, fix \(0<\beta<1\), \(a>0\), and set
\[
g_a(w)=g(w)\exp\!\bigl(-a(1-iw)^\beta\bigr).
\]
The power uses the logarithm on the right half-plane. Explicitly, there it is \(\log|v|+i\arctan(\operatorname{Im}v/\operatorname{Re}v)\); differentiating the real coordinates gives the Cauchy–Riemann equations and derivative \(1/v\), so this is a holomorphic branch. When \(\operatorname{Im}w\ge0\), the number \(v=1-iw\) has real part at least one, and
\[
\operatorname{Re}v^\beta
\ge\cos(\beta\pi/2)|v|^\beta>0.
\]
Thus \(|g_a|\le M\) on the real boundary. On the upper semicircle \(|w|=R\), its modulus is at most
\[
C(1+R)^N
\exp\!\bigl(-a\cos(\beta\pi/2)(R-1)^\beta\bigr),
\]
which tends to zero as \(R\to\infty\). On each closed half-disk the maximum occurs on the boundary: compactness produces a maximum, and if one occurs inside, the local maximum principle makes the function constant on the connected half-disk, in which case its boundary has the same maximum. This establishes the required boundary maximum bound on each finite half-disk. Letting \(R\to\infty\) gives \(|g_a(w)|\le M\) at every fixed upper point; then \(a\downarrow0\) gives the asserted bound. This argument includes \(M=0\).

**The bounded-input estimate.** Assume \(p=\infty\), set \(M=\|u\|_\infty\), fix real \(x,y\), and let
\[
f(w)=u(x+wy),\qquad
b_\delta=H(-y)+\delta|y|.
\]
For \(t=\operatorname{Im}w\ge0\), the homogeneity of the actual support function gives \(H(-ty)=tH(-y)\). Formula (3.3) therefore bounds \(f(w)\) by a polynomial in \(|w|\) times \(e^{b_\delta t}\). On the real axis \(x+sy\) is real and \(|f(s)|\le M\). The function
\[
g_\delta(w)=e^{ib_\delta w}f(w)
\]
has polynomial growth throughout the upper half-plane, since
\(|e^{ib_\delta w}|=e^{-b_\delta t}\). The preceding bound implies \(|g_\delta(i)|\le M\), or
\[
|u(x+iy)|\le M e^{H(-y)+\delta|y|}.
\]
Let \(\delta\downarrow0\). This proves (3.1) at the bounded endpoint, in fact at every point of every complex translate. The calculation remains valid if \(H(-y)<0\), or \(y=0\).

**All finite norm endpoints.** Let \(1\le p<\infty\), and let \(v\) be an arbitrary bounded measurable function of compact support, with \(\|v\|_{p'}\le1\). Here \(p'=\infty\) when \(p=1\). Define
\[
f_v(z)=\int u(z+t)v(t)\,dt.
\]
The compact integration set and local uniform bounds on the entire integrand and all its derivatives prove that this is entire. The same compact integration preserves (3.3), with changed constants and the *same* support function and \(\delta\): translating \(z\) by a real \(t\) changes only the polynomial estimate. Hölder on the real subspace gives \(|f_v(x)|\le\|u\|_p\). Apply exactly the bounded half-plane argument to \(f_v\); it needed this growth estimate and the real bound, and did not require any further Fourier-support assertion for \(f_v\). At \(x=0\) it yields
\[
\begin{gathered}
\left|\int u(t+iy)v(t)\,dt\right|\\
\le e^{H(-y)}\|u\|_p.
\end{gathered}
\tag{3.4}
\]
To extract the full norm without assuming it is finite in advance, put \(g(t)=u(t+iy)\) and \(E_R=\{|t|\le R\}\). It is bounded on each \(E_R\) by continuity. At \(p=1\), use \(v=\boldsymbol1_{E_R}\overline g/|g|\), setting its value zero where \(g=0\). Its infinity norm is at most one, and the integral in (3.4) is \(\int_{E_R}|g|\). At \(1<p<\infty\), put \(A_R=(\int_{E_R}|g|^p)^{1/p}\). If \(A_R>0\), use
\[
v=\boldsymbol1_{E_R}
   \frac{\overline g\,|g|^{p-2}}{A_R^{p-1}},
\]
again setting the zero value to zero. Its modulus is \(|g|^{p-1}/A_R^{p-1}\), so it is bounded and compactly supported, has \(p'\)-norm one, and its pairing is \(A_R\). The case \(A_R=0\) already satisfies the desired bound. Let \(R\to\infty\) by monotone convergence in each case. This proves all finite-\(p\) assertions, including \(p=1\). If \(S\) is empty, [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md)'s empty-support conclusion and Fourier injectivity give \(u=0\); no support function of the empty set is needed. \(\square\)

## Exercises

**Exercise 1 (foundation: the atoms at an arbitrary bandwidth).** For \(\lambda>0\), compute a finite signed measure \(K_\lambda\) such that \(u'=K_\lambda*u\) for every bounded \(u\) with spectrum in \([-\lambda,\lambda]\). Give its total variation, its whole Fourier transform and its action on every plane wave \(e^{i\xi x}\) with \(|\xi|\le\lambda\).

**Exercise 2 (intermediate: every derivative order).** Prove \(\|u^{(m)}\|_p\le\lambda^m\|u\|_p\) for every integer \(m\ge0\), \(1\le p\le\infty\), and \(L^p\) input with spectrum in \([-\lambda,\lambda]\). Describe the finite convolution measure for \(u^{(m)}\) and prove that the constant is attained at the bounded endpoint for every \(m\).

**Exercise 3 (foundation: a support function can be negative).** Let \(0<c_1<c_2\), and let \(u(x)=a e^{ic_1x}+b e^{ic_2x}\), where \(a,b\ne0\). Compute the exact original and complex-translate infinity norms and \(H(-y)\). Determine when the complex-translation inequality is strict, including the direction \(y>0\).

**Exercise 4 (advanced: the exact tensor squared-sinc norm).** For \(a_j>0\), \(c_j\in\mathbb R\), set
\[
u(z)=\prod_{j=1}^n e^{ic_jz_j}
                  \left(\frac{\sin(a_jz_j)}{a_jz_j}\right)^2.
\]
Compute its actual Fourier support and its exact \(L^1\) norm on every translate \(\mathbb R^n+iy\), including zero components of \(y\). Verify the support-function estimate directly.

**Exercise 5 (intermediate: all phase contractions attain equality).** For \(u(x)=a e^{i\lambda x}+b e^{-i\lambda x}\), \(a,b\in\mathbb C\), not both zero, compute the exact infinity norm of
\(\sin\alpha\,u'/\lambda+\cos\alpha\,u\) for every real \(\alpha\). For a real single sinusoid, determine the pointwise Bernstein expression at every real point.

**Exercise 6 (advanced: sharpness at every finite norm endpoint).** Show that the derivative constant \(\lambda\) cannot be decreased for any fixed \(1\le p<\infty\). Use \(f(x)=(\sin(x/2)/(x/2))^2\) and a family whose whole Fourier support remains inside \([-\lambda,\lambda]\); justify all norm and derivative limits.

**Exercise 7 (advanced: complex Cauchy bounds in a real direction).** Let \(u\in L^p(\mathbb R^n)\) have nonempty compact spectrum \(S\), and let \(a\in\mathbb R^n\). Set \(R_a=\max_{\xi\in S}|a\cdot\xi|\). Prove, for \(m\ge1\) and every \(r>0\),
\[
\|(a\cdot\nabla)^m u\|_p
\le m!r^{-m}e^{rR_a}\|u\|_p.
\]
Optimize this bound when \(R_a>0\), and determine the derivatives when \(R_a=0\). Keep both norm endpoints.

**Exercise 8 (intermediate: a centred covariant derivative).** Suppose the spectrum of \(u\in L^p(\mathbb R)\) lies in \([c-\lambda,c+\lambda]\), \(c\in\mathbb R\), \(\lambda>0\). Prove the sine-cosine contraction with \(u'\) replaced by \(u'-icu\). Describe its atom measure and total variation explicitly from Theorem 2.1's measure.

## Solutions

**Solution 1.** Push Theorem 1.1's \(K\) by \(s\mapsto s/\lambda\) and multiply it by \(\lambda\). The full measure is
\[
K_\lambda=\frac{4\lambda}{\pi^2}
\sum_{k\in\mathbb Z}\frac{(-1)^k}{(2k-1)^2}
           \delta_{(2k-1)\pi/(2\lambda)}.
\]
Its atoms are distinct, so its total variation is \(\lambda\). Its whole transform is \(\lambda b(\xi/\lambda)\), with \(b\) the complete four-periodic triangular multiplier in Theorem 1.1. In particular it equals \(i\xi\) on the entire closed band. Scaling the proved closed-band convolution identity gives \(u'=K_\lambda*u\). Every atom sum is absolutely uniformly convergent for bounded inputs. On a plane wave it is \(e^{i\xi x}FK_\lambda(\xi)=i\xi e^{i\xi x}\), including both endpoints and zero.

**Solution 2.** Theorem 2.1 at \(\alpha=\pi/2\) gives the first derivative bound at all \(p\), and proves that the derivative belongs to the same \(L^p\) space. Its spectrum stays in the band because its transform is \(i\xi Fu\). Iterate this conclusion \(m\) times; \(m=0\) is the identity. The measure is \(K_\lambda^{*m}\), with the zeroth power \(\delta_0\). Its total variation is at most \(\lambda^m\), since absolute convolution of finite measures multiplies the two total-variation bounds; this also follows by summing the absolute products of their atoms. Iterated convolution gives the whole derivative identity. For \(u=e^{i\lambda x}\), the input infinity norm is one and the \(m\)-th derivative infinity norm is exactly \(\lambda^m\). Thus the constant is attained, including order zero; no finite-\(p\) membership is claimed for that plane wave.

**Solution 3.** The actual spectrum is \(\{c_1,c_2\}\). The relative phase \((c_2-c_1)x\) ranges through a full circle, so the two terms can be aligned; the triangle bound is attained. Therefore
\[
\begin{gathered}
\|u\|_\infty=|a|+|b|,\\
\|u(\cdot+iy)\|_\infty\\
=|a|e^{-c_1y}+|b|e^{-c_2y}.
\end{gathered}
\]
The same relative-phase argument works after translation. Here \(H(-y)=\max(-c_1y,-c_2y)\). For \(y>0\) it is \(-c_1y<0\), so the bound decays; the second term has a strictly smaller exponential factor, making the inequality strict. For \(y<0\), the maximum is \(-c_2y\), and the first term is strictly smaller. At \(y=0\) there is equality. Nonzero amplitudes and distinct frequencies were needed for both strict assertions.

**Solution 4.** Each one-dimensional real factor is integrable and has the full triangular transform
\((\pi/a_j)(1-|\xi_j-c_j|/(2a_j))_+\). Absolute Fubini gives the tensor product transform. It is nonzero throughout the interior of the product box and zero outside it, so the actual support is
\[
\begin{gathered}
S=\prod_j[c_j-2a_j,c_j+2a_j],\\
H(-y)=\sum_j(-c_jy_j+2a_j|y_j|).
\end{gathered}
\]
Put \(r=a_jy_j\), \(s=a_jx_j\). For \(r\ne0\),
\[
\left|\frac{\sin(s+ir)}{s+ir}\right|^2
=\frac{\cosh(2r)-\cos(2s)}{2(s^2+r^2)}.
\]
The full Cauchy transform gives the integral of this expression as
\[
\begin{gathered}
\pi[\cosh(2r)-e^{-2|r|}]/(2|r|)\\
=\pi\sinh(2|r|)/(2|r|).
\end{gathered}
\]
At \(r=0\) the squared-sinc integral is \(\pi\), from its transform at zero; the ratio has removable value one. Tonelli for the nonnegative product now gives
\[
\|u(\cdot+iy)\|_1
=\prod_j\frac{\pi}{a_j}e^{-c_jy_j}
   \frac{\sinh(2a_j|y_j|)}{2a_j|y_j|}.
\]
Every zero denominator denotes that removable value. Finally \(\sinh t/t=\frac12\int_{-1}^1e^{ts}ds\le e^t\) for \(t\ge0\), with value one at zero. Multiplying these bounds proves exactly \(e^{H(-y)}\|u\|_1\), and \(\|u\|_1=\prod_j\pi/a_j\).

**Solution 5.** The two endpoint multipliers are \(e^{i\alpha}\) and \(e^{-i\alpha}\), so the output is
\(a e^{i\alpha}e^{i\lambda x}+b e^{-i\alpha}e^{-i\lambda x}\).
Its infinity norm is \(|a|+|b|\), by relative-phase alignment, also when one coefficient is zero. This equals the input norm for every \(\alpha\). For the real sinusoid \(u=q\cos(\lambda x+\theta)\), its derivative is \(-q\lambda\sin(\lambda x+\theta)\), and
\(|u'|^2/\lambda^2+|u|^2=q^2\) at every point. These calculations include \(q=0\); the nonzero condition was needed only for a nonzero equality example.

**Solution 6.** The smooth \(f,f'\) are bounded and have \(O(|x|^{-2})\) tails, so both belong to every finite \(L^p\), and \(\|f\|_p>0\). Its actual spectrum is \([-1,1]\). For \(0<\delta<\lambda/2\), set
\[
u_\delta(x)=e^{i(\lambda-\delta)x}f(\delta x).
\]
Its spectrum is \([\lambda-2\delta,\lambda]\), inside the required band. Its norm is \(\delta^{-1/p}\|f\|_p\), while
\[
u_\delta'=i(\lambda-\delta)u_\delta
+\delta e^{i(\lambda-\delta)x}f'(\delta x).
\]
The reverse norm triangle gives
\[
\frac{\|u_\delta'\|_p}{\|u_\delta\|_p}
\ge\lambda-\delta
-\delta\frac{\|f'\|_p}{\|f\|_p}.
\]
The derivative theorem gives the upper bound \(\lambda\). The two bounds tend to \(\lambda\) as \(\delta\downarrow0\), so any smaller proposed constant fails for sufficiently small \(\delta\). This proves sharpness separately for each finite \(p\), including \(p=1\).

**Solution 7.** Corollary2.2 also supplies the sharper directional estimate with constant \(R_a^m\). We retain the following independent Cauchy-contour bound, which exhibits the complex-translation mechanism requested here. Apply the one-variable Cauchy coefficient formula to \(w\mapsto u(x+wa)\):
\[
\begin{gathered}
(a\cdot\nabla)^m u(x)=\frac{m!}{2\pi r^m}\\
{}\times\int_0^{2\pi}u(x+r e^{i\theta}a)e^{-im\theta}d\theta.
\end{gathered}
\]
Its complex translate has imaginary part \(r\sin\theta\,a\). Real translation by \(r\cos\theta\,a\) does not change the \(L^p\) norm, and the exact support-function bound gives a norm at most \(e^{rR_a}\|u\|_p\). For finite \(p\), Hölder on the probability measure \(d\theta/(2\pi)\) bounds the \(p\)-th power of the pointwise average by the average of the \(p\)-th powers; at \(p=1\) use the ordinary integral triangle. Tonelli then integrates that bound over \(x\), proving the displayed inequality. At \(p=\infty\) the pointwise integral bound proves it directly. This also proves the derivative belongs to \(L^p\), without assuming that beforehand. For \(R_a>0\), minimize \(r^{-m}e^{rR_a}\) at \(r=m/R_a\), obtaining \(m!(eR_a/m)^m\|u\|_p\). For \(R_a=0\), let \(r\to\infty\); the derivative norm is zero. Its smooth representative is therefore zero everywhere.

**Solution 8.** Put \(v=e^{-icx}u\). Its spectrum is in \([-\lambda,\lambda]\), its norm equals that of \(u\), and
\(v'=e^{-icx}(u'-icu)\). Apply Theorem 2.1 to \(v\) and multiply back by \(e^{icx}\), whose modulus is one. If Theorem 2.1's unit-variation measure at scale \(\lambda\) is
\(\sum_j w_j\delta_{s_j}\), the output on \(u\) is convolution by
\(\sum_j w_j e^{ics_j}\delta_{s_j}\).
For \(\alpha\notin\pi\mathbb Z\), its atoms have
\[
s_k=(\pi k-\alpha)/\lambda,\qquad
w_k=\frac{(-1)^k\sin^2\alpha}{(\pi k-\alpha)^2}.
\]
The added phase leaves total variation one. Its multiplier on the actual band is
\(\cos\alpha+i(\xi-c)\sin\alpha/\lambda\).
For \(\alpha=\pi m\), it is simply \((-1)^m\delta_0\), also of variation one. This supplies the whole contraction and every exceptional parameter.

## References

- [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B1: complete compact-support pairing and parameter estimates. [Tempered growth and spectral cutoffs](tempered-growth-and-spectral-cutoffs.md), Lemma2.1 and Theorem3.1: full Schwartz convolution and compact-spectrum fixed points. [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1: periodic expansion and continuous Fourier uniqueness.
- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary2.2 and(2.3)–(2.4): Cauchy and Taylor formulas. Lemma0.1 above supplies the identity and maximum principles. [Spectral gaps and explicit Fourier distributions](spectral-gaps-and-explicit-fourier-distributions.md), Section2, and [Resolvent sampling and positive periodization](resolvent-sampling-and-positive-periodization.md), Section3, provide the full Cauchy-density and squared-sinc transforms used in Solutions4 and6. The supplied Fourier, scalar and integration foundations retain their stated licences.
- Isaac Pesenson, [*Bernstein-Nikolskii inequalities and Riesz interpolation formula on compact homogeneous manifolds*](https://arxiv.org/abs/1403.4561), arXiv:1403.4561v2 (2014), Introduction, formulas(1.1)–(1.4), and §2, Lemma2.1: classical derivative interpolation and its isometric-orbit formulation. Corollary2.2 proves the Euclidean directional consequence directly; it does not assume the paper's general group or compact-manifold theorems.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises7.3.2–7.3.4, printed page390, and answers on pages414–415. The closed-band endpoint proofs, exact norm calculations, directional extension and graded applications here have their own full exposition.
