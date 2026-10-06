# Resolvent sampling and positive periodization

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); linked prerequisites retain their stated licences.*

A positive partition can turn any bounded measurable function into a periodic approximation while controlling both its values and its spectrum. We build that partition from the squared sinc function, then prove the full support bound, the rectangular extension and the sharp approximation and degree estimates. A second use of the same sampling machinery turns a resolvent's exponential spectrum into a cotangent sum and an exact Cauchy-grid error. Both inversion and Gaussian regularization are retained as routes to the Cauchy Fourier pair. Section and result numbers remain stable for subsequent lessons that cite them.

Use \(Ff(\xi)=\int e^{-ix\xi}f(x)\,dx\), with complex bilinear distribution pairings. [Periodic Green functions and boundary spectra](periodic-green-functions-and-boundary-spectra.md), Theorems4.1–4.2, supplies complete integrable sampling and its continuous-representative proof; Theorem2.1 supplies one-dimensional periodic-distribution uniqueness. [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, proves finite positive-kernel uniqueness and smooth periodic expansion. The multidimensional version needed here is proved next. [Spectral gaps and explicit Fourier distributions](spectral-gaps-and-explicit-fourier-distributions.md), Sections2 and4, supplies the Cauchy pair and finite sinc integral; its current Cauchy proof uses elementary half-line Laplace integration and Fourier inversion. [Tempered growth and spectral cutoffs](tempered-growth-and-spectral-cutoffs.md), Lemma2.1 and Theorem3.1, supplies the full Schwartz convolution and compact-spectrum fixed-point theorem. [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Theorem3.1, proves strong exponential series and their whole atomic transforms in every dimension. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16, supply all inversion, Gaussian, calculus, convergence and integration inputs. Each supplied prerequisite retains its stated attribution and licence.

## Periodic uniqueness in every dimension

**Lemma0.1.** Let \(d\ge1\) and \(L>0\). A continuous function on \(\mathbb R^d\), periodic with period \(L\) in every coordinate, is determined by its Fourier coefficients
\[
 c_k(v)=L^{-d}\int_{[0,L]^d}v(x)e^{-2\pi i k\cdot x/L}dx,
 \qquad k\in\mathbb Z^d.
\]
A smooth such function has an absolutely convergent Fourier expansion with uniform convergence of every derivative. An arbitrary distribution periodic in these coordinates is determined by its periodic exponential pairings.

**Proof for functions.** Let \(K_N\) be the one-periodic finite kernel proved in Bernoulli Lemma0.1. The product kernel
\[
 H_N(t)=L^{-d}\prod_{j=1}^d K_N(t_j/L)
\]
is nonnegative and has integral one on \([0,L]^d\), by finite product integration. Outside a fixed small coordinate neighborhood of \(L\mathbb Z^d\), at least one coordinate is away from \(L\mathbb Z\). The integral there is at most the sum of \(d\) one-dimensional kernel tails; each tends to zero by the proved one-dimensional estimate. Uniform continuity of periodic \(v\) therefore gives \(H_N*v\to v\) uniformly, by splitting its difference integral into that neighborhood and its complement. Expanding the finite product kernel shows that its convolution is the finite Fourier polynomial
\[
 \sum_{|k_j|\le N}
 \left[\prod_{j=1}^d\left(1-\frac{|k_j|}{N+1}\right)\right]
 c_k(v)e^{2\pi i k\cdot x/L}.
\]
If all coefficients vanish, every polynomial vanishes and so does \(v\).

For smooth \(v\), repeated integration by parts on the periodic cube gives, with \(\Delta=\sum_j\partial_j^2\),
\[
 |c_k(v)|\le
 (1+4\pi^2|k|^2/L^2)^{-M}
 \|(1-\Delta)^M v\|_\infty.
\]
All boundary terms cancel because opposite face derivatives agree. A dyadic shell \(2^j\le|k|<2^{j+1}\) contains at most \(C_d2^{jd}\) lattice points, as its integer coordinates lie in a cube with that many points. Thus the differentiated Fourier series of order \(r\) converges absolutely and uniformly if \(2M>r+d\). The scalar fundamental theorem in each coordinate identifies all successive derivatives of the sum. Termwise integration and exponential orthogonality show that the sum has the coefficients of \(v\); the preceding uniqueness proof identifies it with \(v\).

**Proof for distributions.** Rescale the one-dimensional compact smooth periodizing cutoff constructed in U057 Theorem2.1 from period \(2\pi\) to period \(L\); its translates still sum to one. Take its product in all \(d\) coordinates, obtaining \(\chi\) with \(\sum_{k\in\mathbb Z^d}\chi(x+Lk)=1\). Define \(T_{\rm per}(\psi)=T(\chi\psi)\) for smooth periodic \(\psi\). Multiplication by this fixed compact cutoff is continuous from the periodic smooth seminorms to the compact-test topology, so this pairing is continuous. It is independent of the cutoff: if a compact smooth \(h\) has zero periodization, insert the partition into \(T(h\psi)\), shift each term using periodicity, and obtain
\[
 T(h\psi)=T\!\left(\chi\psi\sum_k h(\cdot-Lk)\right)=0.
\]
Only finitely many compact supports intersect before this shift. For every compact smooth \(\theta\), the same finite partition and shifts give
\[
 T(\theta)=T_{\rm per}(P\theta),\qquad
 P\theta(x)=\sum_k\theta(x+Lk).
\]
The latter is smooth periodic; its sum is locally finite. If every periodic exponential pairing is zero, the smooth expansion just proved and continuity of \(T_{\rm per}\) give \(T_{\rm per}(\psi)=0\) for every smooth periodic \(\psi\). The displayed identity then gives \(T=0\). Apply this to the difference of two distributions to obtain uniqueness. \(\square\)

## 3. Squared sinc has a triangular spectrum and a positive partition

Let \(\varphi(x)=(\sin x/x)^2\), with \(\varphi(0)=1\).

**Theorem 3.1.** The function is nonnegative and smooth, \(\varphi,\varphi',\varphi''\in L^1\), and
\[
\begin{gathered}
F\varphi(\xi)=\pi(1-|\xi|/2)_+,\\
\sum_{k\in\mathbb Z}\varphi(x+\pi k)=1
\end{gathered}
\tag{3.1}
\]
for every real \(x\). The second series is absolute and locally uniformly convergent, and includes every endpoint and every zero of sine.

**Proof.** The complete finite sinc integral and its whole transform in [*Spectral gaps and explicit Fourier distributions*](spectral-gaps-and-explicit-fourier-distributions.md), Section 4 give
\(\sin x/x=\tfrac12\int_{-1}^{1}e^{itx}dt\).
Multiply two such finite integrals. Fubini on the square of integration, followed by the elementary convolution length of two unit-interval indicators, gives
\[
\varphi(x)=\frac14\int_{-2}^{2}(2-|t|)e^{itx}dt.
\]
Pairing with \(F\theta\), \(\theta\in\mathcal S\), is absolute because the finite weight is integrable and \(F\theta\in L^1\). The already proved whole plane-wave normalization gives
\(F\varphi(\theta)=(\pi/2)\int_{-2}^2(2-|t|)\theta(t)dt\).
This is exactly the entire triangular density in (3.1), with its endpoint values fixed by continuity. Smoothness at zero follows either from the finite integral or the sine power series. For \(|x|\ge1\),
\[
\begin{gathered}
\varphi(x)=\frac{1-\cos2x}{2x^2},\\
\varphi'(x)=\frac{\sin2x}{x^2}-\frac{1-\cos2x}{x^3},
\end{gathered}
\]
\[
\begin{gathered}
\varphi''(x)=\frac{2\cos2x}{x^2}
-\frac{4\sin2x}{x^3}\\
{}+\frac{3(1-\cos2x)}{x^4}.
\end{gathered}
\]
They are bounded by \(C|x|^{-2}\), and hence integrable. The same tail proves local uniform absolute convergence of the shifted series, including the continuous origin term.

Apply [*Periodic Green functions and boundary spectra*](periodic-green-functions-and-boundary-spectra.md), formula (4.2) to \(g(t)=\varphi(x+t/2)\). Its transform is \(Fg(n)=2e^{2inx}F\varphi(2n)\). Thus
\[
\sum_k\varphi(x+\pi k)=\frac1\pi\sum_n e^{2inx}F\varphi(2n).
\]
The only nonzero coefficient is \(F\varphi(0)=\pi\); the two boundary coefficients at \(n=\pm1\) vanish, as do all the exterior ones. The sum is exactly one for every \(x\), proving (3.1). \(\square\)

## 4. Positive periodization of every bounded measurable input

**Theorem 4.1.** Fix \(\epsilon>0\), set \(a=\pi/\epsilon\), and let \(u\) be a bounded measurable complex-valued representative on \(\mathbb R\), with \(M=\sup_x|u(x)|<\infty\). Then
\[
\begin{gathered}
u_\epsilon(x)=\sum_{k\in\mathbb Z}
u(x+ak)\\
{}\times\varphi(\epsilon x+\pi k)
\end{gathered}
\tag{4.1}
\]
converges absolutely, uniformly on compact sets in the sense of its uniformly vanishing tails. It is bounded by \(M\), measurable and \(a\)-periodic. Its range lies in the closed convex hull of the range of \(u\). Its whole tempered Fourier support and exact pointwise error satisfy
\[
\begin{gathered}
\operatorname{supp}Fu_\epsilon\\
\subset\operatorname{supp}Fu+[-2\epsilon,2\epsilon],
\end{gathered}
\tag{4.2}
\]
\[
\begin{gathered}
|u(x)-u_\epsilon(x)|\\
\le2M\bigl(1-\varphi(\epsilon x)\bigr).
\end{gathered}
\tag{4.3}
\]
For an \(L^\infty\) equivalence class these assertions hold almost everywhere with its essential bound and essential closed convex range. One may choose a representative taking all its values in the essential range and bounded by the essential supremum; then the literal pointwise assertions above hold. The resulting distribution \(u_\epsilon\) is independent of changes to \(u\) on a null set. No continuity of \(u\) is assumed.

**Proof of convergence, range and error.** On a fixed compact \(x\)-set the nonzero-index weights have a summable uniform \(C(1+|k|)^{-2}\) bound, by the explicit tail of \(\varphi\). Thus the series in (4.1) has uniformly small absolute tails. Reindexing \(k\mapsto k+1\) proves periodicity. The weights are nonnegative and sum to one by Theorem 3.1. Any finite partial weighted sum, completed with its omitted weight at one fixed value in the range of \(u\), belongs to that convex hull; the omitted weight tends to zero and its values are bounded. Passing to the limit proves the closed-convex-hull assertion and the bound \(M\).

The zeroth weight is \(\varphi(\epsilon x)\). Subtracting (4.1) from \(u(x)\), using the sum of all weights equal to one, gives
\[
\begin{gathered}
u(x)-u_\epsilon(x)\\
=\sum_{k\ne0}\bigl(u(x)-u(x+ak)\bigr)\\
{}\times\varphi(\epsilon x+\pi k).
\end{gathered}
\]
Its absolute value is bounded by \(2M\) times the omitted weights, which is exactly (4.3). For equivalence classes a common null exceptional set and its countably many translates suffice; outside their union every sampled value has the essential bound. Changes on a null set likewise change (4.1) only on such a countable translated union. The essential range is closed and lies in the bounded complex disk. All values belong to it off a null set: its open complement is a countable union of basis balls whose inverse images have measure zero. That exceptional union cannot cover a real interval, which also proves nonemptiness. Changing exceptional values to one fixed essential-range value supplies the stated bounded representative.

**Proof of the full support assertion.** Put \(\varphi_\epsilon(x)=\varphi(\epsilon x)\), \(w=u\varphi_\epsilon\), and
\[
K(\xi)=F\varphi_\epsilon(\xi)
=\frac\pi\epsilon\left(1-\frac{|\xi|}{2\epsilon}\right)_+.
\]
Then \(w\in L^1\) and \(Fw\) is continuous. We prove the entire identity
\[
Fw=\frac1{2\pi}(Fu)*K,
\tag{4.4}
\]
including its compact nonsmooth frequency factor. For a Schwartz test \(\theta\), define the compact-factor convolution by
\[
((Fu)*K)(\theta)
=Fu_\xi\left(\int K(\eta)\theta(\xi+\eta)d\eta\right).
\]
The inner function is Schwartz. Its every seminorm is bounded by \(\|K\|_1\) times a fixed finite sum of seminorms of \(\theta\), because \(\eta\) lies in one compact interval. This defines the tempered convolution on all tests.

Choose nonnegative compact smooth approximate identities \(\rho_\delta\), supported in \([-\delta,\delta]\), with integral one, and set \(K_\delta=K*\rho_\delta\). Then \(K_\delta\) is compact smooth and tends to \(K\) in \(L^1\), with one fixed compact support for \(\delta\le1\). Explicitly, the triangular \(K\) is globally Lipschitz; averaging its translate differences gives \(\|K_\delta-K\|_\infty\le C\delta\), and the common finite support gives the L1 convergence. Its inverse transform is
\(\psi_\delta(x)=\varphi_\epsilon(x)F\rho_\delta(-x)\).
This follows directly by absolute convolution Fubini and the inverse factor \((2\pi)^{-1}\). Also \(\psi_\delta=GK_\delta\) is Schwartz, \(|F\rho_\delta|\le1\), and \(F\rho_\delta(-x)\to1\) pointwise.

The complete global Schwartz convolution lemma in [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1, Fourier-dualized with \(F^2=2\pi R\), gives
\(F(u\psi_\delta)=(2\pi)^{-1}(Fu)*K_\delta\).
To verify its constant, apply \(F\) to the right numerator: the lemma gives \(F((Fu)*K_\delta)=(2\pi Ru)(2\pi R\psi_\delta)\). Inversion therefore leaves exactly the factor \(2\pi\) relating that numerator to \(F(u\psi_\delta)\).

Now \(u\psi_\delta\to u\varphi_\epsilon=w\) strongly in \(\mathcal S'\). Indeed bounded \(u\), the bound one on \(F\rho_\delta\), and an integrable Schwartz weight give dominated convergence, uniformly on each bounded test family. On the other side the convolution test difference tends to zero in every Schwartz seminorm, at most \(C\|K_\delta-K\|_1\) times a finite test seminorm. The finite-order Schwartz bound for \(Fu\) then proves strong convergence of its convolution, uniformly on bounded tests. Passing to the limit proves (4.4).

Let \(S=\operatorname{supp}Fu\). The sum \(S+[-2\epsilon,2\epsilon]\) is closed: for any convergent sequence of sums, a subsequence of the compact-interval components converges; the other components then converge into the closed set \(S\). The support of \((Fu)*K\) is contained in this sum: if a compact test is supported outside it, its convolution test in (4.4) is compact smooth and supported away from \(S\). Hence its \(Fu\) pairing is zero. Consequently \(Fw\), a continuous function, vanishes pointwise outside that set.

Finally (4.1) is precisely the \(a\)-periodization of \(w\). Absolute unfolding gives its coefficients
\[
c_n=\frac1a Fw(2\pi n/a).
\]
They are bounded by \(\|w\|_1/a\). The complete tempered exponential-series theorem [*Separated frequencies and distributional order*](separated-frequencies-and-distributional-order.md), Theorem 3.1, applied to the integer lattice with \(m=1\) and then scaled by \(x\mapsto2\pi x/a\), supplies the strongly convergent whole series and exact atomic transform. The series equals the periodization: their periodic pairings have the same coefficients, and the smooth periodic test expansion and partition argument proved in [*Periodic Green functions and boundary spectra*](periodic-green-functions-and-boundary-spectra.md), Theorem 2.1, show uniqueness. Thus
\[
\begin{gathered}
Fu_\epsilon=\frac{2\pi}{a}\sum_{n\in\mathbb Z}\\
Fw(2\pi n/a)\delta_{2\pi n/a}.
\end{gathered}
\tag{4.5}
\]
Every atom outside \(S+[-2\epsilon,2\epsilon]\) has zero coefficient. The locally finite lattice has no other support points; alternatively pair any compact test in the complement with the entire atom series. This proves (4.2) for the whole Fourier distribution. All approximation and series passages above hold uniformly on bounded Schwartz test sets. \(\square\)

## 1. A whole resolvent transform and cotangent sum

**Theorem 1.1.** For every \(z\in\mathbb C\) with \(\operatorname{Im}z>0\), the function \(f_z(x)=(x^2-z^2)^{-1}\) and its first two derivatives belong to \(L^1(\mathbb R)\). Its whole transform and whole integer sample sum are
\[
\begin{gathered}
Ff_z(\xi)=\frac{\pi i}{z}e^{iz|\xi|},\\
\sum_{k\in\mathbb Z}\frac1{k^2-z^2}
=-\frac\pi z\cot(\pi z).
\end{gathered}
\tag{1.1}
\]
Both the physical and transformed sampling series are absolutely convergent, locally uniformly in the entire upper half-plane. These identities are holomorphic there, including all their parameter derivatives.

**Proof.** There is no real pole, and \(z\ne0\). On a compact parameter set in the upper half-plane the denominator is bounded away from zero on each fixed real compact interval. At infinity the function and its first two derivatives have uniform bounds \(C|x|^{-2}\), \(C|x|^{-3}\), \(C|x|^{-4}\), respectively. This proves the claimed integrability, also uniformly on compact parameter sets.

Put \(q_z(\xi)=\pi i e^{iz|\xi|}/z\). It is continuous and integrable, since \(|e^{iz|\xi|}|=e^{-\operatorname{Im}z|\xi|}\). Absolute integration of its two half-lines gives
\[
\begin{gathered}
Fq_z(x)\\
=\frac{\pi i}{z}
\left(\frac{i}{z-x}+\frac{i}{z+x}\right)\\
=\frac{2\pi}{x^2-z^2}.
\end{gathered}
\tag{1.2}
\]
The elementary half-line integral here is \(\int_0^\infty e^{i(z\pm x)t}dt=i/(z\pm x)\), obtained by evaluating its exponentially decaying primitive. Thus (1.2) is an identity of ordinary integrable functions and of their whole tempered distributions. The complete Schwartz inversion used in [*Bernoulli series and Poisson summation*](bernoulli-series-and-poisson-summation.md) gives \(F^2=2\pi R\) on \(\mathcal S'\), where \(R\) is reflection. Both \(f_z\) and \(q_z\) are even. Applying inversion to (1.2) proves the first identity in (1.1) on the entire frequency line; it supplies the continuous value at zero and leaves no possible extra point distribution.

Apply [*Periodic Green functions and boundary spectra*](periodic-green-functions-and-boundary-spectra.md), Theorem 4.1, formula (4.2) to \(g(t)=f_z(t/(2\pi))\). Its transformed samples satisfy \(Fg(n)=2\pi Ff_z(2\pi n)\) by substitution, so its formula (4.2) gives
\[
\begin{gathered}
\sum_k f_z(k)=\sum_n Ff_z(2\pi n)\\
=\frac{\pi i}{z}\left(1+2\sum_{n\ge1}e^{2\pi izn}\right).
\end{gathered}
\]
With \(q=e^{2\pi iz}\), \(|q|<1\), the bracket is \((1+q)/(1-q)\). Since \(\cot(\pi z)=-i(1+q)/(1-q)\), this is exactly the second identity in (1.1). The physical tail is bounded uniformly on compact parameter sets by \(C\sum_{|k|>N}k^{-2}\). The frequency tail is geometric with ratio at most \(e^{-2\pi b}\), where \(b>0\) is a lower bound for \(\operatorname{Im}z\) on that set. Every parameter derivative has the same type of physical bound and a polynomial factor times that geometric frequency bound. These estimates justify termwise parameter differentiation and holomorphy of all the stated whole identities. \(\square\)

## 2. The exact exponential Cauchy sampling error

**Theorem 2.1.** The whole Cauchy transform is \(F(1+x^2)^{-1}=\pi e^{-|\xi|}\), and for every \(\epsilon>0\),
\[
\begin{gathered}
\epsilon\sum_{k\in\mathbb Z}\frac1{1+\epsilon^2k^2}\\
=\pi\coth(\pi/\epsilon)\\
=\pi+\frac{2\pi}{e^{2\pi/\epsilon}-1}.
\end{gathered}
\tag{2.1}
\]
Consequently
\[
\begin{gathered}
E_\epsilon=\epsilon\sum_k\frac1{1+\epsilon^2k^2}-\pi,\\
\lim_{\epsilon\downarrow0}e^{2\pi/\epsilon}E_\epsilon=2\pi.
\end{gathered}
\tag{2.2}
\]

**Proof by the existing inversion route.** [Spectral gaps and explicit Fourier distributions](spectral-gaps-and-explicit-fourier-distributions.md), Section2, proves the whole Cauchy pair by the two half-line Laplace integrals and Fourier inversion. It agrees with Theorem1.1 at \(z=i\), including the continuous frequency origin and equality on all Schwartz tests.

The density and its first two derivatives are integrable; this also follows from Theorem 1.1 at \(z=i\). Apply [*Periodic Green functions and boundary spectra*](periodic-green-functions-and-boundary-spectra.md), formula (4.2) with \(g(t)=(1+(\epsilon t/(2\pi))^2)^{-1}\). Substitution gives \(Fg(n)=2\pi\pi\epsilon^{-1}e^{-2\pi|n|/\epsilon}\). Therefore
\[
\epsilon\sum_k\frac1{1+\epsilon^2k^2}
=\pi\sum_n e^{-2\pi|n|/\epsilon}.
\]
All sums are absolute. Summing the two geometric tails gives (2.1). Multiplication of its exact error by \(e^{2\pi/\epsilon}\) gives \(2\pi/(1-e^{-2\pi/\epsilon})\), which tends to \(2\pi\). This is the asserted entire rescaled error, not an uncontrolled subtraction of two approximate infinite sums. \(\square\)

**A second proof of the Cauchy pair by Gaussian regularization.** This retains the argument in the earlier programme's Bochner's theorem, Example5.1, written by GPT-6.1 Sol (OpenAI), CC0, with the present Fourier normalization and all inputs supplied here. Put \(h(t)=e^{-|t|}\). Direct evaluation of the two half-line integrals gives
\[
 q(\xi)=\int e^{-it\xi}h(t)dt
 =\frac1{1+i\xi}+\frac1{1-i\xi}
 =\frac2{1+\xi^2}.
\]
For \(\delta>0\), the Gaussian transform and its mass in Fourier foundation F3 give
\[
\begin{aligned}
 J_\delta(x)
 &=\frac1{2\pi}\int e^{ix\xi}q(\xi)e^{-\delta\xi^2}d\xi\\
 &=\int h(t)\frac{e^{-(x-t)^2/(4\delta)}}{\sqrt{4\pi\delta}}dt\\
 &=\frac1{\sqrt\pi}\int h(x-2\sqrt\delta\,v)e^{-v^2}dv.
\end{aligned}
\]
The first interchange is absolute, bounded by \(\|h\|_1\int e^{-\delta\xi^2}d\xi/(2\pi)<\infty\). In the first line, dominated convergence uses the integrable \(q\). In the last line, continuity and boundedness of \(h\), dominated by \(e^{-v^2}/\sqrt\pi\), give the limit \(h(x)\), since that Gaussian has mass one. Consequently
\[
 \frac1\pi\int\frac{e^{ix\xi}}{1+\xi^2}d\xi=e^{-|x|}.
\]
Reflection of the integration variable changes the Fourier sign, so this is exactly \(F(1+x^2)^{-1}=\pi e^{-|x|}\). Every integral is absolute. This route uses the proved Gaussian identity, without assuming general Fourier inversion for the Cauchy density. \(\square\)

## Exercises

### Positive approximation and spectral bounds

**Exercise 4 (foundation: a plane wave becomes two neighboring frequencies).** For real \(c\), compute the entire periodization from Theorem 4.1 of \(u(x)=e^{icx}\). Write it using the two neighboring frequencies on the \(2\epsilon\) grid, including the integer case.

**Exercise 6 (advanced: a rectangular two-dimensional version).** For bounded measurable \(u\) on \(\mathbb R^2\), replace Theorem 4.1's weight by \(\varphi(\epsilon x_1)\varphi(\epsilon x_2)\) and sum over the square lattice with spacing \(a=\pi/\epsilon\). Prove convergence, convex range, the full Fourier support bound and the corresponding error estimate.

**Exercise 7 (intermediate: quantitative convergence without input continuity).** Prove uniform convergence \(u_\epsilon\to u\) on each fixed compact set for every bounded representative, with a quadratic bound. Show that Theorem 4.1's coefficient 2 is sharp even for continuous inputs at a prescribed \(\epsilon,x_0\) with \(\varphi(\epsilon x_0)<1\).

**Exercise 8 (advanced: the exact finite degree of a band-limited approximation).** If \(\operatorname{supp}Fu\subset[-\Lambda,\Lambda]\), \(\Lambda\ge0\), prove that Theorem 4.1's periodization is a trigonometric polynomial of degree at most \(\lceil\Lambda/(2\epsilon)\rceil\), with coefficients bounded by \(M\). Show the degree bound is sharp.

**Exercise 5 (intermediate: compact spectrum does not imply finite density moments).** Show that \(\varphi/\pi\) is a probability density with compactly supported Fourier transform, but has infinite first absolute and second moments.

### Resolvents and shifted sampling errors

**Exercise 1 (intermediate: shift and scale the resolvent samples).** For \(a>0\), real \(x\), and \(\operatorname{Im}z>0\), find \(\sum_k((x+ak)^2-z^2)^{-1}\), including a cotangent closed form.

**Exercise 2 (advanced: a double resolvent).** Find the whole transform and integer sample sum of \((x^2-z^2)^{-2}\), \(\operatorname{Im}z>0\), justifying parameter differentiation.

**Exercise 3 (advanced: a shifted Cauchy grid changes the leading error).** For \(b>0\) let \(p_b(x)=b/(\pi(b^2+x^2))\). Determine \(\epsilon\sum_kp_b(\epsilon(k+\theta))\), its leading rescaled error, and the next rescaled error when \(\theta=1/4\).

## Solutions

### Positive approximation and spectral bounds

**Solution 4.** Modulation shifts Theorem 3.1's triangle, so for \(w=e^{icx}\varphi_\epsilon\), \(Fw(\xi)=K(\xi-c)\). Theorem 4.1's coefficient formula gives
\[
c_n=\left(1-\left|n-\frac c{2\epsilon}\right|\right)_+.
\]
Set \(c/(2\epsilon)=m+\vartheta\), \(m\in\mathbb Z\), \(0\le\vartheta<1\). All coefficients vanish except \(c_m=1-\vartheta\), \(c_{m+1}=\vartheta\). Thus
\[
u_\epsilon(x)=(1-\vartheta)e^{2i\epsilon mx}
+\vartheta e^{2i\epsilon(m+1)x}.
\]
For \(\vartheta=0\) the second term vanishes. The triangle's two boundary values are zero, so no further endpoint atoms appear. These coefficients identify the entire distribution; both sides are continuous, as the original uniformly convergent bounded continuous-input series shows, so equality holds at every point. The expression is a convex combination of two unit-modulus values and hence has modulus at most one.

**Solution 6.** The weights are the products of two nonnegative one-dimensional weights. Their sum is one by absolute Fubini and Theorem 3.1; their tails converge uniformly on compact rectangles because each one-dimensional tail does. Bounded \(u\) supplies an absolute dominating product. Reindexing each coordinate proves separate \(a\)-periodicity. Completing finite convex sums with their omitted total weight proves the same closed-convex-range bound as in Theorem 4.1. Separating the zero lattice term gives
\[
|u(x)-u_\epsilon(x)|
\le2M\left(1-\varphi(\epsilon x_1)\varphi(\epsilon x_2)\right).
\]
Put \(w(x)=u(x)\varphi_\epsilon(x_1)\varphi_\epsilon(x_2)\); it is L1 by the product integrability. Its multiplier transform is \(K(\xi_1)K(\xi_2)\), with support the box \([-2\epsilon,2\epsilon]^2\). To retain the full distribution identity, convolve this compact L1 factor with a nonnegative smooth product approximate identity. The factors converge in L1 with common compact support; their inverse transforms are the original multiplier times a product of Fourier approximate-identity factors of modulus at most one. The same dominated bounded-test convergence and compact-translate Schwartz estimates as in Theorem 4.1 prove
\[
Fw=(2\pi)^{-2}Fu*(K\otimes K).
\]
Testing outside the Minkowski sum gives zero by the compact convolution support argument in Theorem 4.1, now with a compact box. Absolute unfolding in the two coordinates gives periodization coefficients \(a^{-2}Fw(2\pi n/a)\). They are bounded, so Lemma0.1's complete multidimensional smooth periodic test expansion and uniqueness, together with the tempered lattice-series theorem, give
\[
Fu_\epsilon=\frac{(2\pi)^2}{a^2}
\sum_{n\in\mathbb Z^2}Fw(2\pi n/a)\delta_{2\pi n/a}.
\]
The atom coefficients outside \(\operatorname{supp}Fu+[-2\epsilon,2\epsilon]^2\) vanish, proving the whole support inclusion. For the lattice-series theorem one can take \(m=2\), since bounded coefficients satisfy \(\sum_{\mathbb Z^2}\langle n\rangle^{-4}<\infty\); positive dilation normalizes the separation. All representative statements are interpreted as in Theorem 4.1, since the exceptional translated union is still countable.

**Solution 7.** The sine Taylor formula gives \(\varphi(t)=1-t^2/3+O(t^4)\), with the remainder bounded uniformly near zero. Thus for \(|x|\le R\), (4.3) gives
\[
\sup_{|x|\le R}|u(x)-u_\epsilon(x)|
\le\frac{2M}{3}\epsilon^2R^2+C_RM\epsilon^4
\]
for small \(\epsilon\). No continuity of \(u\) appears in this estimate. For sharpness at fixed \(\epsilon,x_0\), take a continuous compact bump \(0\le\chi\le1\), equal one at \(x_0\), supported in \((x_0-a/2,x_0+a/2)\), and set \(u=2\chi-1\). Then \(M=1\), \(u(x_0)=1\), and \(u(x_0+ak)=-1\) for every nonzero integer \(k\). Consequently \(u_\epsilon(x_0)=2\varphi(\epsilon x_0)-1\) and the exact error is \(2(1-\varphi(\epsilon x_0))\). Since that quantity is positive under the stated condition, no smaller universal coefficient can replace 2, even within bounded continuous inputs.

**Solution 8.** (4.4) makes the continuous function \(Fw\) supported in \([-\Lambda-2\epsilon,\Lambda+2\epsilon]\). A continuous function supported in a closed finite interval is zero at both boundary points, by continuity from the exterior. Therefore its nonzero lattice coefficients require
\(|2\epsilon n|<\Lambda+2\epsilon\), or \(|n|<\Lambda/(2\epsilon)+1\).
The largest permitted integer absolute index is \(\lceil\Lambda/(2\epsilon)\rceil\). (4.5) is consequently a finite atom sum and its inverse is the corresponding trigonometric polynomial. Its coefficient bound is
\[
|c_n|\le\frac{\|w\|_1}{a}
\le\frac{M\|\varphi_\epsilon\|_1}{a}=M,
\]
because \(\|\varphi_\epsilon\|_1=\pi/\epsilon=a\). If \(\Lambda>0\), choose \(u(x)=e^{i\Lambda x}\). Solution 4 has a nonzero coefficient at its upper neighboring index \(\lceil\Lambda/(2\epsilon)\rceil\), whether the ratio is integral or not. This gives sharpness with \(M=1\). For \(\Lambda=0\), the constant input has degree zero and attains the bound. For an L-infinity input the identity is an almost-everywhere identity, or a pointwise identity after selecting its continuous band-limited representative through the exact spectral cutoff theorem [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md), Theorem 3.1. Its full support, smoothness and fixed-point proof are the stated internal prerequisite; no extra regularity has been assumed from a bare bounded equivalence class.

**Solution 5.** Nonnegativity follows from the square. Theorem 3.1 proves integrability and \(F\varphi(0)=\pi\); since the transform of an L1 function at zero is its integral, \(\int\varphi/\pi=1\). Its characteristic transform is exactly \((1-|\xi|/2)_+\), compactly supported. On the intervals \([\pi k+\pi/4,\pi k+3\pi/4]\), \(k\ge1\), one has \(\sin^2x\ge1/2\). The first absolute moment integrand is \(\sin^2x/(\pi x)\); its integral on each interval is at least \(C/(k+1)\). Their harmonic sum diverges. The second moment integrand is \(\sin^2x/\pi\), with a fixed positive integral lower bound on every such interval; its sum also diverges. These lower bounds prove both infinities. The kink of the compact triangle is consistent with this lack of absolute moment regularity.

### Resolvents and shifted sampling errors

**Solution 1.** Scale and translate the sampling argument in [*Periodic Green functions and boundary spectra*](periodic-green-functions-and-boundary-spectra.md), formula (4.2), or substitute \(g(t)=f_z(x+at/(2\pi))\). Its transform is \((2\pi/a)e^{2\pi ix\xi/a}Ff_z(2\pi\xi/a)\). Theorem 1.1 therefore gives
\[
\begin{gathered}
\sum_k f_z(x+ak)\\
=\frac{\pi i}{az}
\left(1+2\sum_{m\ge1}q^m\cos(2\pi mx/a)\right),\\
q=e^{2\pi iz/a}.
\end{gathered}
\]
The physical sum is absolute and locally uniform in \(x\), and the frequency sum is uniformly geometric since \(|q|<1\). Adding the two geometric series gives \((1-q^2)/(1-2q\cos(2\pi x/a)+q^2)\). The denominators \(1-qe^{\pm2\pi ix/a}\) do not vanish. The identity \(\cot t=-i(1+e^{2it})/(1-e^{2it})\) then gives
\[
\begin{gathered}
\sum_k\frac1{(x+ak)^2-z^2}\\
=-\frac\pi{2az}\left[
\cot\frac{\pi(z+x)}a+\cot\frac{\pi(z-x)}a\right].
\end{gathered}
\]
This is a closed form of the whole absolutely convergent sum, with no separate interpretation of conditionally convergent simple-pole series.

**Solution 2.** Since \(\partial_zf_z=2z(x^2-z^2)^{-2}\), the locally uniform parameter-derivative bounds in Theorem 1.1 allow division by \(2z\) and differentiation of both whole identities. With \(\rho=|\xi|\), this gives
\
F[(x^2-z^2)^{-2}
=\left(-\frac{\pi i}{2z^3}-\frac{\pi\rho}{2z^2}\right)e^{iz\rho},
\]
\[
\begin{gathered}
\sum_k\frac1{(k^2-z^2)^2}\\
=\frac\pi{2z^3}\cot(\pi z)
+\frac{\pi^2}{2z^2}\csc^2(\pi z).
\end{gathered}
\]
On each compact upper-half-plane parameter set the physical derivatives are bounded by a uniform integrable tail and the frequency derivatives by \(C(1+\rho)^j e^{-b\rho}\). The sample derivatives have uniform summable bounds, so every differentiated pairing and sum is legitimate. Differentiation is in the parameter, not in frequency; the displayed regular continuous spectrum has no added frequency-origin contact.

**Solution 3.** Scaling the complete Cauchy transform gives \(Fp_b(\xi)=e^{-b|\xi|}\). The density and its first two derivatives are integrable. The translated sampling argument from [*Periodic Green functions and boundary spectra*](periodic-green-functions-and-boundary-spectra.md), formula (4.2), gives, with \(q=e^{-2\pi b/\epsilon}\),
\[
\begin{gathered}
\epsilon\sum_kp_b(\epsilon(k+\theta))\\
=1+2\sum_{m\ge1}q^m\cos(2\pi m\theta)\\
=\frac{1-q^2}{1-2q\cos(2\pi\theta)+q^2}.
\end{gathered}
\]
All sums are absolute. The terms with \(m\ge2\) have bound \(2q^2/(1-q)\). After multiplication by \(q^{-1}\) they tend to zero; the error limit is therefore \(2\cos(2\pi\theta)\). At \(\theta=1/4\), the rational expression becomes \((1-q^2)/(1+q^2)\). Its error is exactly \(-2q^2/(1+q^2)\), so multiplication by \(e^{4\pi b/\epsilon}\) gives limit \(-2\). The quarter-cell shift cancels the first exponential term and reverses the next one's sign.

## References

- [Periodic Green functions and boundary spectra](periodic-green-functions-and-boundary-spectra.md), Theorems4.1–4.2 and2.1; [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1: complete sampling, representative, periodic uniqueness and finite-kernel proofs.
- [Spectral gaps and explicit Fourier distributions](spectral-gaps-and-explicit-fourier-distributions.md), Sections2 and4; [Tempered growth and spectral cutoffs](tempered-growth-and-spectral-cutoffs.md), Lemma2.1 and Theorem3.1; [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Theorem3.1. The supplied Fourier, scalar and integration foundations retain their stated licences.
- Bochner's theorem, HA-LCA, Example5.1, GPT-6.1 Sol (OpenAI), CC0: earlier Gaussian-regularization argument, fully included here in the present normalization. The general locally compact group theorems in that lesson are not premises of this proof.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises7.2.6–7.2.9, printed page389, with answers on page413; §7.2 supplies the broader periodic Fourier setting. The complete proofs, extensions, quantitative bounds and thematic exercise organization here are independently expressed.
