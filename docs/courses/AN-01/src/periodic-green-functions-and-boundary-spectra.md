# Periodic Green functions and boundary spectra

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); linked prerequisites retain their stated licences.*

Sampling and solving a periodic differential equation use the same operation: recover a periodic object from all of its Fourier coefficients. We first establish sampling for integrable densities and finite complex measures, including the continuous representative forced by a measure second derivative. We then use coefficient uniqueness and derivative jumps to construct Green functions, remove their constant pole, and analyze resonances. Finally, tangent boundary values show how the same reconstruction works for a distribution whose spectrum occupies only one side. The exercises develop the full resolvent family, every polyharmonic order, shifted cusps and complex atomic examples.

Our convention is \(Ff(\xi)=\int e^{-ix\xi}f(x)\,dx\), with complex bilinear distribution pairings. The supplied [Schwartz Fourier foundations](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, prove the seminorm estimates, coordinate rules, Gaussian transform and whole tempered inversion. The [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16.1–16.2, prove integration, convergence, smooth approximation and the generating-class argument; [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, prove the calculus, exponential series and cutoffs used here. [Positive and complex measure foundations](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), (M10)–(M12), prove total variation and Radon regularity. These supplied texts carry their own attribution and licence notices. [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1 and Theorems1.1–1.2, supplies the complete positive-kernel uniqueness proof, smooth periodic test expansion, scaled comb and all Bernoulli identities. The result numbers below are stable citation labels, also used by later lessons.

## Measure integration and identification of regular distributions

**Lemma0.1.** Absolute integration may be interchanged between Lebesgue measure and a finite complex Radon measure. An \(L^1_{\rm loc}\) function whose regular distribution is zero vanishes almost everywhere. Every \(f\in L^1(\mathbb R)\) defines a finite complex Radon measure \(f\,dx\), with variation at most \(|f|\,dx\).

**Proof of the mixed integration assertion.** First take a finite positive measure \(\eta\) and restrict the Lebesgue variable to a bounded interval \(I\). Consider Borel sets \(A\subset I\times\mathbb R\) for which both section measures are measurable and
\[
 \int_I\eta(A_x)\,dx=\int_{\mathbb R}|A^y|\,d\eta(y).
\]
Rectangles satisfy this identity by multiplication of their two finite measures. The class contains the whole space and is closed under relative complement: both sides subtract from \(|I|\eta(\mathbb R)<\infty\). It is closed under countable disjoint unions by monotone convergence, which also proves measurability of the sums of section measures. The full generating-class proof in integration §16.2 therefore gives the identity for all Borel sets. Rectangles generate these Borel sets because the two Euclidean spaces have countable bases. Increasing nonnegative simple approximations give equality of both iterated integrals for every nonnegative Borel function. Exhaust \(\mathbb R\) by bounded intervals and use monotone convergence once more. Applying this result to the absolute value and then the four real and imaginary parts proves absolute Fubini.

For complex \(\nu\), its positive variation \(v=|\nu|\) is supplied by the measure foundations. The four measures
\[
 \tfrac12(v+\operatorname{Re}\nu),\quad
 \tfrac12(v-\operatorname{Re}\nu),\quad
 \tfrac12(v+\operatorname{Im}\nu),\quad
 \tfrac12(v-\operatorname{Im}\nu)
\]
are positive, at most \(v\), and their signed complex combination is \(\nu\). They are Radon because approximation of a Borel set from inside by compacts and outside by opens in \(v\)-measure also approximates each dominated measure. Apply the positive result to these four measures; integrability against \(dx\,dv\) justifies every subtraction. This proves the complex assertion and all its variation bounds. Lebesgue equivalence classes can be represented by Borel functions using the completion proved in integration §16.1; all kernels below are Borel and the iterated identities retain their almost-everywhere meanings.

**Proof of injectivity.** Let \(u\in L^1_{\rm loc}\) annihilate every compact smooth test. For a compact interval \(K\), choose a compact smooth cutoff \(\chi=1\) on a neighborhood of \(K\) and a compact smooth integral-one mollifier \(r_\varepsilon\). For sufficiently small \(\varepsilon\), at every \(x\in K\) the test \(r_\varepsilon(x-\cdot)\) is supported where \(\chi=1\). Thus \((\chi u)*r_\varepsilon(x)=0\). The exact \(L^1\) approximate-identity proof in integration §15.4 makes these convolutions tend to \(\chi u\) in \(L^1\); hence \(u=0\) almost everywhere on \(K\). Exhausting the line proves injectivity. A continuous function zero almost everywhere is zero everywhere: a nonzero value would give an interval on which its modulus is bounded below.

**Proof for integrable densities.** For a nonnegative integrable Borel function \(q\), truncate its values and restrict to a bounded interval. The resulting measure is bounded by a constant times Lebesgue measure there. Compact inner and open outer approximation for Lebesgue sets, as proved in integration §§15.0 and15.3, therefore proves its Radon regularity. The total mass of the discarded part tends to zero by dominated convergence, so these same approximations, with that mass added to the error, prove regularity of \(q\,dx\). Apply this to the positive and negative real and imaginary parts of \(f\). For every finite Borel partition of a set \(A\), the integral triangle inequality gives a sum of moduli at most \(\int_A|f|\). Taking the supremum defining variation proves the bound. \(\square\)

## Poisson sampling for integrable convolutions

**Theorem 4.1.** For every \(f\in L^1(\mathbb R)\) and \(\phi\in\mathcal S(\mathbb R)\),
\[
\begin{gathered}
2\pi\sum_{k\in\mathbb Z}(f*\phi)(2\pi k)\\
=\sum_{n\in\mathbb Z}Ff(n)F\phi(n),
\end{gathered}
\tag{4.1}
\]
with absolute convergence on both sides. If \(f,f',f''\in L^1\), with derivatives in the distributional sense and the unique continuous representative of \(f\), then
\[
2\pi\sum_{k\in\mathbb Z}f(2\pi k)
=\sum_{n\in\mathbb Z}Ff(n),
\tag{4.2}
\]
again with both sums absolutely convergent. The continuous representative is essential when one starts from L1 equivalence classes.

**Proof of (4.1).** Put \(g=f*\phi\). Dominated differentiation under its absolutely convergent integral proves \(g^{(j)}=f*\phi^{(j)}\), continuous for every \(j\): translations of a Schwartz function and each derivative converge uniformly, and are bounded. Also \(g^{(j)}\in L^1\), with norm at most \(\|f\|_1\|\phi^{(j)}\|_1\), by absolute Fubini.

For every derivative order \(j\),
\[
\begin{gathered}
\sup_{\substack{x\in[0,2\pi]\\y\in\mathbb R}}
\sum_{k\in\mathbb Z}|\phi^{(j)}(x+2\pi k-y)|\\
<\infty.
\end{gathered}
\tag{4.3}
\]
Indeed shift \(x-y\) into a fixed period interval, reindex \(k\), and apply a Schwartz bound with any exponent greater than one. Consequently the periodization
\(P_g(x)=\sum_kg(x+2\pi k)\) is absolutely convergent. Its differentiated series are locally uniformly convergent. To prove the latter assertion rather than merely pointwise domination, split the convolution integral into \(|y|\le A\) and its complement. On the bounded part, rapid decay gives a uniform tail for \(|k|>N\), uniformly in \(x\) on a period. On the complement use (4.3); its contribution is at most a fixed constant times \(\int_{|y|>A}|f(y)|dy\), tending to zero independently of \(N\). First choose \(A\), then \(N\). This proves local uniform convergence of every derivative and permits differentiation of the periodization. It is smooth and periodic.

Its coefficient is \(Fg(n)/(2\pi)\), by absolute unfolding over the periods. Absolute Fubini in the whole convolution integral gives \(Fg(n)=Ff(n)F\phi(n)\). The bound \(|Ff(n)|\le\|f\|_1\) and arbitrary Schwartz decay of \(F\phi\) show that these coefficients are absolutely summable with every frequency power. The [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, complete smooth periodic Fourier theorem identifies \(P_g\) with that expansion. Evaluation at zero gives (4.1), and both absolute-convergence assertions have already been proved. Notice that no Schwartz-decay assumption has been imposed on \(f\).

**Proof of (4.2), including all representative and limit bounds.** First recall the one-dimensional weak fundamental theorem in a form that supplies the needed representative. If \(h,g\in L^1_{\rm loc}\) and \(h'=g\), put \(G(x)=\int_0^xg(t)dt\). On a compact interval \(J\), choose \(M>0\) so that the integral of \(|g|\) over \(J\cap\{|g|>M\}\) is below \(\varepsilon/2\). On any finite disjoint family of intervals in \(J\) whose total length is below \(\varepsilon/(2M)\), the sum of the increments of \(G\) in modulus is below \(\varepsilon\). This proves local absolute continuity. For a test supported in \((a,b)\), write \(G(x)=G(a)+\int_a^x g(t)dt\); absolute Fubini gives \(-\int_a^bG(x)\psi'(x)dx=\int_a^b g(t)\psi(t)dt\). Thus its whole derivative is \(g\). Thus \(r=h-G\) has derivative zero. Every compact smooth test \(\psi\) with zero integral is the derivative of the compact smooth primitive \(\int_{-\infty}^x\psi(t)dt\); hence \(r(\psi)=0\). Fixing one compact test with integral one shows that \(r\) is a constant distribution. The injectivity in Lemma0.1 therefore makes \(h\) agree almost everywhere with \(G+c\), which is the unique continuous representative.

Apply this argument to \(f\) and \(f'\). Both representatives are locally absolutely continuous. Their derivatives are globally integrable, so each representative has finite limits at both infinities by the Cauchy criterion applied to its integral tails. Its L1 integrability forces each of these limits to be zero. Thus both integration-by-parts boundary terms vanish, and, for \(\xi\ne0\),
\[
\begin{gathered}
Ff''(\xi)=-\xi^2Ff(\xi),\\
|Ff(\xi)|\le|\xi|^{-2}\|f''\|_1.
\end{gathered}
\tag{4.4}
\]
The term at \(n=0\) is bounded by \(\|f\|_1\), so the frequency sum in (4.2) is absolute.

Physical samples require a separate bound. On \(I_k=[2\pi k-\pi,2\pi k+\pi]\), absolute continuity gives
\[
\begin{gathered}
\sup_{I_k}|f|\le\frac1{2\pi}\int_{I_k}|f(t)|dt\\
{}+\int_{I_k}|f'(t)|dt.
\end{gathered}
\tag{4.5}
\]
For any fixed point of the interval this follows by comparison with every other point and averaging; taking its supremum proves the bound. Summing over the intervals gives
\(\sum_k\sup_{I_k}|f|\le\|f\|_1/(2\pi)+\|f'\|_1\).
Thus the sample sum is absolute, and \(P_f(x)=\sum_kf(x+2\pi k)\) converges absolutely uniformly on \([-\pi,\pi]\). It is continuous and periodic, with the endpoint reindexing justified by absolute convergence.

Choose a nonnegative compact smooth approximate identity \(\phi_\epsilon\) with integral one. It is Schwartz; \(F\phi_\epsilon(n)\to1\) for each integer \(n\), and \(|F\phi_\epsilon(n)|\le1\). Formula (4.1) holds for each \(\epsilon>0\). Absolute physical Fubini, justified either by (4.3) or by the uniformly convergent periodization on the compact support of \(\phi_\epsilon\), gives
\[
\begin{gathered}
\sum_k(f*\phi_\epsilon)(2\pi k)\\
=\int\phi_\epsilon(y)P_f(-y)dy\\
\longrightarrow P_f(0).
\end{gathered}
\]
On the frequency side the already proved absolute sum and the bound one permit dominated convergence to \(\sum_nFf(n)\). Passing to the limit gives (4.2). Every physical point is evaluated on the proved continuous representative. This proves the entire delta specialization and both absolute sums. \(\square\)

## Sampling finite measures and functions with a measure second derivative

The convolution in (4.1) smooths an integrable density. It also smooths point masses and every finite complex measure. More surprisingly, the unsmoothed sampling formula needs only an integrable function with a finite-measure second derivative; its first derivative and continuous representative then follow from the equation.

For a finite complex Radon measure \(\nu\), write \(\|\nu\|_{\rm TV}=|\nu|(\mathbb R)\) and
\(F\nu(\xi)=\int e^{-ix\xi}d\nu(x)\).
The latter is continuous, by dominated convergence, and bounded by total variation. The measure is tempered because its test pairing is bounded by \(\|\nu\|_{\rm TV}\|\psi\|_\infty\). Mixed Fubini from Lemma0.1 identifies its distributional Fourier transform with the displayed continuous function: the absolute bound for interchanging the integrals against a Schwartz test is \(\|\nu\|_{\rm TV}\|\psi\|_1\).

**Theorem 4.2.** If \(\nu\) is a finite complex Radon measure, \(\phi\in\mathcal S(\mathbb R)\), \(L>0\) and \(h\in\mathbb R\), then
\[
\begin{gathered}
\omega_n=2\pi n/L,\\
L\sum_{k\in\mathbb Z}(\nu*\phi)(h+Lk)\\
=\sum_{n\in\mathbb Z}e^{i\omega_nh}
F\nu(\omega_n)F\phi(\omega_n).
\end{gathered}
\tag{M1}
\]
Both sums are absolute, and the periodized convolution is smooth with locally uniform convergence of every differentiated physical series.

Suppose instead that \(f\in L^1(\mathbb R)\) and its whole distributional derivative \(f''=\mu\) is a finite complex Radon measure. Then \(f\) has a unique continuous, locally absolutely continuous representative, its weak derivative belongs to \(L^1\), and
\[
\begin{gathered}
\|f'\|_1\le\|f\,dx-\mu\|_{\rm TV}\\
\le\|f\|_1+\|\mu\|_{\rm TV},\\
|Ff(\xi)|\le\|\mu\|_{\rm TV}/\xi^2,\\
\xi\ne0,\\
\sum_{n\ne0}|Ff(2\pi n/L)|\\
\le\frac{L^2}{12}\|\mu\|_{\rm TV}.
\end{gathered}
\tag{M2}
\]
On that representative, for every \(L>0\) and every \(h\),
\[
\begin{gathered}
L\sum_{k\in\mathbb Z}f(h+Lk)\\
=\sum_{n\in\mathbb Z}e^{2\pi inh/L}Ff(2\pi n/L).
\end{gathered}
\tag{M3}
\]
Both sums are absolute. The physical periodization and its frequency series converge uniformly in \(h\) on a period. This includes (4.2), and does not authorize sampling arbitrary representatives of an \(L^1\) class.

**Proof for the smoothed measure.** Set \(g(x)=\int\phi(x-y)d\nu(y)\). Uniform difference quotients of the bounded Schwartz derivatives and finite total variation give \(g^{(j)}=\nu*\phi^{(j)}\), continuously for every \(j\). Absolute Fubini gives
\[
\|g^{(j)}\|_1\le\|\nu\|_{\rm TV}\|\phi^{(j)}\|_1.
\tag{M4}
\]
The translate estimate (4.3), with period \(L\), is uniform in \(x\) on one period and in \(y\): shift \(x-y\) into that period and use any Schwartz decay exponent greater than one.

To prove uniform lattice tails, split \(\nu\) into \(|y|\le A\) and its complement. On the first part, \(|x+Lk-y|\) escapes uniformly as \(|k|\to\infty\), so each derivative has a uniformly vanishing summable tail. The other part is bounded by the translate constant times \(|\nu|(\{|y|>A\})\), which tends to zero. First choose \(A\), then the lattice tail. This proves absolute uniform convergence for every derivative of the periodization.

Unfolding over a period and then applying absolute convolution Fubini gives its normalized coefficient at \(n\) as
\[
\frac1L F\nu(2\pi n/L)F\phi(2\pi n/L).
\tag{M5}
\]
These coefficients are rapidly summable with every frequency power, since \(F\nu\) is bounded and \(F\phi\) is Schwartz. The full smooth periodic Fourier proof in Bernoulli Lemma0.1 identifies the series with the periodization. Evaluating at \(h\) proves (M1), including its phase and scale.

**Proof of the automatic representative.** Define
\[
\begin{gathered}
E(x)=\tfrac12e^{-|x|},\\
\nu=f(x)\,dx-\mu,\\
g=E*\nu,\\
FE(\xi)=\frac1{1+\xi^2}.
\end{gathered}
\tag{M6}
\]
The last formula follows by integrating the two absolutely convergent half-line exponentials. Also \(\|E\|_1=1\) and
\(E'(x)=-\tfrac12\operatorname{sgn}(x)e^{-|x|}\) almost everywhere, with \(\|E'\|_1=1\). Integration by parts separately on the two half-lines proves this whole first derivative; continuity of \(E\) contributes no atom.

Thus absolute Fubini makes \(g\) and its whole derivative \(g'=E'*\nu\) integrable, with both norms at most \(\|\nu\|_{\rm TV}\). The function \(E\) is bounded and uniformly continuous, so
\[
\begin{gathered}
|g(x+t)-g(x)|\\
\le\|\nu\|_{\rm TV}\\
{}\cdot\sup_s|E(s+t)-E(s)|.
\end{gathered}
\tag{M7}
\]
This tends uniformly to zero. In particular \(g\) is continuous.

The full distributional Fourier derivative identity \(f''=\mu\) gives
\(-\xi^2Ff=F\mu\). Both sides are continuous functions, hence their distributional equality holds pointwise: a nonzero continuous difference could be detected on a small compact test. Therefore
\[
\begin{gathered}
(1+\xi^2)Ff(\xi)=F\nu(\xi),\\
Fg(\xi)=FE(\xi)F\nu(\xi)\\
=Ff(\xi).
\end{gathered}
\tag{M8}
\]
The convolution identity here is absolute Fubini for \(E\in L^1\) and a finite measure. Whole tempered Fourier inversion makes their regular distributions equal; Lemma0.1 supplies injectivity, so \(f=g\) almost everywhere. Thus \(g\) is the unique continuous representative: two continuous functions equal almost everywhere agree everywhere.

Its integrable weak derivative supplies local absolute continuity by the complete weak fundamental theorem in the proof of (4.2). That proof uses a compact primitive for each zero-integral test to remove the constant remainder, so it also applies to the present complex-valued function. The derivative bound follows from the proved convolution norm. The identity \(-\xi^2Ff=F\mu\) gives the frequency estimate in (M2). Summing both signs of \(n\) and using the exact reciprocal-square sum in Bernoulli Solution 2 gives
\[
\begin{gathered}
\frac{L^2}{4\pi^2}\|\mu\|_{\rm TV}
\sum_{n\ne0}n^{-2}\\
=\frac{L^2}{12}\|\mu\|_{\rm TV}.
\end{gathered}
\tag{M9}
\]
The zero sample is bounded by \(\|f\|_1\).

**Proof of the unsmoothed sampling identity.** On \(I_k=[Lk-L/2,Lk+L/2]\), absolute continuity and averaging over the comparison point give
\[
\begin{gathered}
\sup_{I_k}|f|\\
\le L^{-1}\int_{I_k}|f|+\int_{I_k}|f'|.
\end{gathered}
\tag{M10}
\]
Summing yields a finite bound \(L^{-1}\|f\|_1+\|f'\|_1\). Consequently \(\sum_k f(h+Lk)\) converges absolutely uniformly for \(|h|\le L/2\), and is continuous and periodic. Its normalized Fourier coefficient is \(Ff(2\pi n/L)/L\), by absolute unfolding. By (M2) the corresponding frequency series is absolutely uniformly convergent. The complete Fejér uniqueness proof identifies these two continuous periodic functions. This proves (M3) at every \(h\), with its precise representative and all constants. \(\square\)

For comparison, [NIST DLMF §1.8(iv)](https://dlmf.nist.gov/1.8) states a classical shifted Poisson formula for a twice continuously differentiable function with \(f\) and \(|f''|\) integrable. [Terence Tao's complex and Fourier notes](https://terrytao.wordpress.com/2014/12/05/245a-supplement-2-a-little-bit-of-complex-and-fourier-analysis/), Theorem 34, give a compact \(C^2\) instance by Abel damping and residues, with the opposite Fourier sign. Its contour and inversion inputs are separate foundations. The proof above uses the supplied periodic Fourier argument and establishes the stated finite-measure hypotheses directly. These references do not assert the difference-primitive theorem or the present measure extension.

## The hyperbolic periodic Green function

**Theorem 2.1.** The absolutely uniformly convergent series
\[
S(x)=\sum_{n=1}^{\infty}\frac{\cos(nx)}{1+n^2}
\]
satisfies, for \(0\le x\le2\pi\),
\[
\begin{gathered}
S(x)=\frac{\pi\cosh(x-\pi)}{2\sinh\pi}-\frac12,
\end{gathered}
\tag{2.1}
\]
extended continuously with period \(2\pi\). Its whole equation is
\[
\begin{gathered}
S-S''=\pi C_{2\pi}-\frac12,\\
C_{2\pi}=\sum_{k\in\mathbb Z}\delta_{2\pi k}.
\end{gathered}
\tag{2.2}
\]

**Proof.** Absolute uniform convergence follows from \(\sum(1+n^2)^{-1}<\infty\), so \(S\) is continuous and periodic. Distributional differentiation of this series is legitimate strongly in \(\mathcal S'\): before or after either derivative, the Schwartz transform samples have arbitrarily fast decay, uniformly on bounded test sets. The [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md) full scaled comb identity gives
\[
\sum_{n=1}^{\infty}\cos(nx)=\pi C_{2\pi}-\frac12
\]
in the whole space. Therefore the exact coefficient multiplication proves (2.2).

Define \(H(x)=\pi\cosh(x-\pi)/(2\sinh\pi)\) on \([0,2\pi]\), extended continuously and periodically. Off the joining points, \(H''=H\). At zero the left derivative is \(+\pi/2\), while the right derivative is \(-\pi/2\). Its derivative jump is therefore \(-\pi\), so \(H''=H-\pi C_{2\pi}\), with no first-derivative point term because \(H\) is continuous. Indeed, integrate twice on each open period against a Schwartz test. The equal endpoint values cancel the test-derivative terms; the right-minus-left first derivative contributes the stated point mass. The remaining integrals and boundary sums converge absolutely by Schwartz decay. Thus \(H-1/2\) solves (2.2).

For completeness, the periodic homogeneous equation has only the zero distribution. A whole-line periodic distribution \(w\) defines a continuous pairing on smooth periodic functions by \(w_{\rm per}(\psi)=w(\chi\psi)\), where \(\chi\) is compact smooth and \(\sum_k\chi(x+2\pi k)=1\). Construct \(\chi\) by dividing a nonnegative compact smooth function whose translates cover the circle by its strictly positive periodic sum. This pairing is independent of the partition. Indeed, if compact smooth \(h\) has zero periodization, insert the locally finite partition into \(w(h\psi)\), shift each term using periodicity, and obtain \(w(\chi\psi\sum_kh(x+2\pi k))=0\). Only finitely many intersecting compact supports contribute to this argument. It also applies to \(h=\chi'\) and \(h=\chi''\), since their periodizations vanish. Therefore whole-line differentiation descends to the usual derivative on the periodic pairing, with no partition-derivative remainder.

Testing \((1-\partial_x^2)w=0\) against the periodic exponential now gives \((1+n^2)w_{\rm per}(e^{-inx})=0\) for every integer \(n\). The complete [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, smooth periodic Fourier expansion converges with every derivative. Continuity allows its pairing with \(w_{\rm per}\) term by term, so all vanishing coefficients imply \(w_{\rm per}=0\). To recover every compact-test pairing, periodize the compact test and use the same partition-shift argument; it gives \(w(\phi)=w_{\rm per}(\sum_k\phi(x+2\pi k))=0\). Thus \(w=0\) on the whole line. Both \(S\) and \(H-1/2\) are continuous functions, so their distributional equality gives equality at every point, including both endpoints. This proves (2.1). \(\square\)

## Subtract the constant pole before taking zero mass

The mean in Solution 3 identifies exactly which part of the massive Green function diverges. Removing it leaves a continuous profile with a finite massless limit.

**Theorem 2.2.** For \(\mu>0\), let \(G_\mu\) be the full Green function in Solution 3 and set
\[
\begin{gathered}
A_\mu=G_\mu-\frac1{2\pi\mu^2},\\
A_0(x)=\pi B_2(x/(2\pi))\\
=\frac{x^2}{4\pi}-\frac x2+\frac\pi6,\\
0\le x\le2\pi .
\end{gathered}
\tag{G1}
\]
extended continuously and periodically. Both profiles have mean zero. Their whole equations are
\[
\begin{gathered}
(\mu^2-D^2)A_\mu=C_{2\pi}-\frac1{2\pi},\\
-D^2A_0=C_{2\pi}-\frac1{2\pi}.
\end{gathered}
\tag{G2}
\]
The difference \(R_\mu=A_\mu-A_0\) is globally \(C^2\), with
\[
\begin{gathered}
R_\mu(x)=-\frac{\mu^2}{2\pi}\\
{}\times\sum_{n\ne0}\frac{e^{inx}}{n^2(\mu^2+n^2)},\\
\|R_\mu\|_\infty\le\frac{\mu^2\pi^3}{90},\\
\|R_\mu'\|_\infty\le
\frac{\mu^2}{\pi}\sum_{n=1}^{\infty}n^{-3},\\
\|R_\mu''\|_\infty\le\frac{\mu^2\pi}{6}.
\end{gathered}
\tag{G3}
\]
Thus \(R_\mu\to0\) uniformly with its first two derivatives. It is not globally \(C^3\) for any \(\mu>0\): its third piecewise derivative has jump \(-\mu^2\) at each joining point. Nevertheless every fixed whole distributional derivative of \(R_\mu\) tends strongly to zero in \(\mathcal S'\).

**Proof of the normalization and full equations.** Solution 3 has the exact coefficient series
\[
A_\mu=\frac1{2\pi}\sum_{n\ne0}
\frac{e^{inx}}{\mu^2+n^2}.
\tag{G4}
\]
Removing the zero coefficient removes exactly \(1/(2\pi\mu^2)\), so the mean is zero. Subtraction in the full massive equation gives the first line of (G2). By [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Solution 2, \(B_2(t)=\sum_{n\ne0}e^{2\pi int}/(2\pi^2n^2)\), absolutely uniformly. Substituting \(t=x/(2\pi)\) proves
\[
A_0=\frac1{2\pi}\sum_{n\ne0}\frac{e^{inx}}{n^2}
\]
and (G1). Its polynomial second derivative is \(1/(2\pi)\) off the joins. Its first derivative has left trace \(1/2\) and right trace \(-1/2\) at zero, hence jump \(-1\); periodwise integration by parts yields the second line of (G2). Both the constant term and the source lattice are retained.

**Proof of the differentiated estimates and their precise limit.** Subtract the two absolutely convergent coefficient series, using
\[
\frac1{\mu^2+n^2}-\frac1{n^2}
=-\frac{\mu^2}{n^2(\mu^2+n^2)}.
\]
This gives the first line of (G3). Since \(\mu^2+n^2\ge n^2\), the coefficient magnitudes of the zeroth, first and second derivatives are bounded respectively by \(\mu^2/(2\pi|n|^4)\), \(\mu^2/(2\pi|n|^3)\) and \(\mu^2/(2\pi|n|^2)\). All three majorants are summable. Uniform convergence of the series and its first two derivatives, with the ordinary fundamental theorem applied successively, proves \(R_\mu\in C^2\). Pair \(n\) and \(-n\), use the reciprocal-square sum proved in Bernoulli Solution 2 and the reciprocal-fourth sum proved in its Solution 9. The resulting bounds are exactly (G3).

Subtracting the whole equations (G2) also gives
\[
R_\mu''=\mu^2A_\mu .
\tag{G5}
\]
The right side is continuous. On each open period its derivative is \(\mu^2A_\mu'\). The derivative jump of \(A_\mu\) equals the jump of \(G_\mu\), namely \(-1\); a constant subtraction does not change it. Thus the piecewise third derivative of \(R_\mu\) has jump \(-\mu^2\), proving the failure of \(C^3\). This accounts for the exact regularity of the difference even though each separate profile has a corner.

Finally, for any fixed \(j\ge0\) and any Schwartz test \(\phi\),
\[
|(D^jR_\mu)(\phi)|
\le\frac{\mu^2\pi^3}{90}\|\phi^{(j)}\|_1 .
\tag{G6}
\]
A fixed weighted Schwartz supremum controls this \(L^1\) norm, uniformly on every bounded test set. Consequently all these whole derivatives converge strongly to zero, including those which cannot be represented by globally continuous ordinary derivatives. \(\square\)

## Every periodic cosine and its resonances

**Theorem 1.1.** For \(a\in\mathbb C\), let \(f_a\) be the continuous \(2\pi\)-periodic function equal to \(\cos(ax)\) on \([-\pi,\pi]\). Then, on the whole line,
\[
\begin{gathered}
f_a''+a^2f_a\\
=2a\sin(\pi a)\sum_{k\in\mathbb Z}\delta_{(2k+1)\pi}.
\end{gathered}
\tag{1.1}
\]
Its entire Fourier expansion is
\[
\begin{gathered}
f_a(x)=\sum_{n\in\mathbb Z}c_n(a)e^{inx},\\
c_n(a)=\frac{a\sin(\pi a)(-1)^n}{\pi(a^2-n^2)},
\end{gathered}
\tag{1.2}
\]
where every apparent singularity is filled by its actual integral value. Specifically \(c_0(0)=1\), \(c_n(0)=0\) for \(n\ne0\); if \(a=\pm m\), \(m\) a positive integer, the only nonzero coefficients are \(c_m=c_{-m}=1/2\). The expansion converges absolutely and uniformly in \(x\), uniformly also for \(a\) in any compact subset of \(\mathbb C\). It is an entire parameter family in the uniform periodic norm, and its differentiated series supplies (1.1) strongly in \(\mathcal S'\).

**Proof.** The endpoint values of \(\cos(ax)\) agree. Therefore the first derivative has no point mass. At \(b=(2k+1)\pi\), the left derivative is \(-a\sin(\pi a)\), and the right derivative, read at the next period's \(-\pi\), is \(+a\sin(\pi a)\). Integrating by parts on each period shows that the second derivative has a point mass with coefficient the right-minus-left jump, \(2a\sin(\pi a)\). The ordinary second derivative away from the endpoints is \(-a^2f_a\). The sum of boundary terms and integrals is absolute on a Schwartz test: the periodic function and both one-sided derivatives are bounded, while the test and its derivatives decay. The same bound is uniform for \(a\) in a compact set. This proves the whole identity (1.1).

The coefficient integral is
\[
c_n(a)=\frac1{2\pi}\int_{-\pi}^{\pi}\cos(ax)e^{-inx}dx.
\]
For \(a\ne\pm n\), splitting the cosine into two exponentials gives
\[
\begin{gathered}
c_n(a)=\frac{\sin(\pi(a-n))}{2\pi(a-n)}\\
{}+\frac{\sin(\pi(a+n))}{2\pi(a+n)}\\
=\frac{a\sin(\pi a)(-1)^n}{\pi(a^2-n^2)}.
\end{gathered}
\]
The integral is entire in \(a\), because all derivatives of its integrand are uniformly bounded on the finite integration interval and on compact parameter sets. Thus it fixes every removable value. Direct integration at integer \(a\) gives exactly the resonant coefficients stated above, including the constant case.

For a compact parameter set \(K\), choose \(M>2\sup_K|a|+1\). For \(|n|>M\), \(|a^2-n^2|\ge3n^2/4\), while \(|a\sin(\pi a)|\) is uniformly bounded. Hence \(|c_n(a)|\le C_Kn^{-2}\). Each of the finitely many remaining entire coefficients is bounded on \(K\). The series therefore converges absolutely and uniformly in \(x,a\in\mathbb R\times K\). Its continuous periodic sum has the same coefficients as \(f_a\). The complete smooth periodic test expansion and Fejér uniqueness proof in [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1 identify them. Equivalently, apply its positive Fejér convolution kernels to their continuous difference: every coefficient is zero, every such convolution is zero, and the kernels converge uniformly to that difference. No pointwise endpoint exception remains because \(f_a\) is continuous.

Entire dependence in the uniform norm can be proved directly without a norm-valued contour theorem. Let \(r(x)\in[-\pi,\pi]\) be a representative of \(x\) modulo \(2\pi\). Its even powers are continuous periodic functions, independent of the endpoint choice, and
\[
 f_a(x)=\sum_{k=0}^{\infty}\frac{(-1)^ka^{2k}r(x)^{2k}}{(2k)!}.
\]
On \(|a|\le R\), the norm of the \(k\)-th term is at most \((R\pi)^{2k}/(2k)!\). Every parameter derivative has the corresponding factorial majorant, with sum bounded by \(\pi^j e^{R\pi}\) for derivative order \(j\). The scalar fundamental theorem along a parameter segment therefore passes through the uniformly convergent derivative series: it proves complex differentiation in the uniform norm at every parameter. This proves the asserted entire family, including its actual integral values at every resonance.

Finally a uniformly vanishing bounded periodic tail vanishes strongly in \(\mathcal S'\), since its pairing is at most its supremum times \(\|\phi\|_1\), uniformly on a bounded set of Schwartz tests. Both distributional differentiations are continuous in that topology. One may also read the differentiated series directly: multiplication of the \(n\)-th coefficient by \(a^2-n^2\) gives \(a\sin(\pi a)(-1)^n/\pi\). The [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md) whole lattice identity, pulled back and shifted, gives
\[
\sum_{n\in\mathbb Z}(-1)^ne^{inx}
=2\pi\sum_{k\in\mathbb Z}\delta_{(2k+1)\pi}.
\]
Its Schwartz-test series has arbitrarily rapid tails. This recovers exactly (1.1) and confirms its constants and signs. \(\square\)

## Upper tangent boundaries have one-sided atomic spectra

**Theorem 3.1.** The limits as \(\epsilon\downarrow0\) of \(\tan(x+i\epsilon)\) and \(\tan^2(x+i\epsilon)\) exist strongly in \(\mathcal S'(\mathbb R)\). Write them \(T\) and \(Q\). Their exact whole spectra are
\[
\begin{gathered}
FT=2\pi i\delta_0\\
{}+4\pi i\sum_{m=1}^{\infty}(-1)^m\delta_{2m},
\end{gathered}
\tag{3.1}
\]
\[
\begin{gathered}
FQ=-2\pi\delta_0\\
{}-8\pi\sum_{m=1}^{\infty}(-1)^m m\delta_{2m}.
\end{gathered}
\tag{3.2}
\]
Both atom sums are strongly tempered, with polynomially bounded coefficients. In particular (3.2) includes its nonzero zero-frequency contact.

**Proof.** If \(z=x+i\epsilon\), then \(w=e^{2iz}\) has modulus \(e^{-2\epsilon}<1\), and algebra gives
\[
\begin{gathered}
\tan z=i\frac{1-w}{1+w}\\
=i+2i\sum_{m=1}^{\infty}
(-1)^m e^{2imx-2m\epsilon}.
\end{gathered}
\tag{3.3}
\]
The geometric series converges absolutely uniformly in \(x\) at every fixed positive \(\epsilon\), as do all its differentiated series. Thus it equals the smooth bounded periodic tangent on the whole real line.

Pair (3.3) with \(\phi\in\mathcal S\). Its \(m\)-th exponential pairing is \(F\phi(-2m)\). For any fixed \(M>1\), repeated integration by parts gives
\[
|F\phi(-2m)|\le C_Mp_M(\phi)(1+m)^{-M},
\]
where \(p_M\) may be a finite sum of weighted Schwartz derivative seminorms. On a bounded set of Schwartz tests its supremum is finite. The bound does not involve \(\epsilon\). The tail is uniformly summable; on the finite remaining terms \(e^{-2m\epsilon}\to1\). Consequently the exponential series with \(\epsilon=0\) defines a tempered distribution and the regularized distributions converge strongly to it. This proves the entire first limit without making a pointwise assertion at tangent poles.

The complete Fourier plane-wave normalization already used in [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md) gives \(F(e^{ibx})=2\pi\delta_b\) and \(F1=2\pi\delta_0\) in the whole tempered space. Apply its continuous transform to the strong series. This gives (3.1). Directly, its atom tail paired with a Schwartz test is bounded by \(Cp_M(\phi)\sum_{m>N}(1+m)^{-M}\); hence the sum itself is strongly tempered.

For every \(\epsilon>0\), the exact ordinary identity is
\[
\tan^2(x+i\epsilon)=\partial_x\tan(x+i\epsilon)-1.
\]
Distributional differentiation is continuous strongly in \(\mathcal S'\), because it sends a bounded test set to a bounded test set. It follows that the second limit exists and equals \(Q=T'-1\). Fourier transformation gives \(FQ=i\xi FT-2\pi\delta_0\). The multiplier kills the zero atom of \(FT\), and at \(\xi=2m\), \(i(2m)(4\pi i)(-1)^m=-8\pi m(-1)^m\). This is exactly (3.2). A Schwartz weight with exponent greater than two proves the uniform atom-tail bound for its linearly growing coefficients. All passages hold on every Schwartz test and leave no unspecified contact terms. \(\square\)

## Exercises

### Sampling densities and measures

**Exercise 7 (foundation: an interval convolved with a Gaussian).** For \(a,b>0\), evaluate the exact sampling identity for \(f=1_{[-a,a]}\), \(\phi(x)=e^{-bx^2}\), expressing both sides through convergent ordinary sums.

**Exercise 8 (advanced: a twice differentiable rational sample sum).** For \(a>0\), use \(f(x)=(1+a|x|)e^{-a|x|}\) to evaluate \(\sum_n(a^2+n^2)^{-2}\) by (4.2). Prove the needed derivative and transform facts.

**Exercise 11 (intermediate: a shifted exponential cusp is admissible).** Let \(a,L>0\), \(c,h\in\mathbb R\), and \(f(x)=e^{-a|x-c|}\). Find its whole second derivative and full Fourier transform, justify (M3), and evaluate the phase-weighted rational sum \(\sum_n e^{2\pi in(h-c)/L}/(a^2+(2\pi n/L)^2)\). Retain the point source at the cusp and the scale \(L\).

**Exercise 12 (advanced: atomic smoothing and the unsmoothed obstruction).** For \(b,L>0\) and distinct real \(c,d\), apply (M1) to \(\nu=\delta_c+i\delta_d\) and \(\phi(x)=e^{-bx^2}\), keeping every complex phase. Then determine why an interval indicator belongs to the original integrable-convolution theorem but fails the measure-second-derivative hypothesis of (M3). Prove the failure using fixed-support tests of supremum at most one.

### Periodic inverses and zero modes

**Exercise 3 (intermediate: a massive periodic Green function).** For \(\mu>0\), find the unique \(2\pi\)-periodic distribution \(G_\mu\) solving \((\mu^2-\partial_x^2)G_\mu=C_{2\pi}\). Determine its mean and full Fourier series.

**Exercise 4 (intermediate: a pair of opposite periodic sources).** For \(0<h<2\pi\), solve \((\mu^2-\partial_x^2)u=C_{2\pi}-C_{h+2\pi\mathbb Z}\). Give its coefficients, mean, value at zero and both derivative jumps.

**Exercise 9 (advanced: every complex periodic resolvent and its poles).** For \(\lambda\in\mathbb C\), determine exactly when \((\lambda-D^2)K=C_{2\pi}\) has a periodic distributional solution. On that parameter set find its full coefficient series and, for \(\lambda=-a^2\) with \(a\notin\mathbb Z\), its physical profile on \([0,2\pi]\). Prove the parameter holomorphy, every spectral residue and the equations of the finite parts at the poles, specifying their resonant coefficients.

**Exercise 10 (advanced: a polyharmonic source with arbitrary period).** For integers \(r\ge1\) and \(L>0\), construct the unique mean-zero \(L\)-periodic distribution \(P_{r,L}\) solving \((-D^2)^rP_{r,L}=C_L-1/L\). Give its Bernoulli profile, full Fourier series, exact ordinary regularity and highest derivative jump. Check the case \(r=1,L=2\pi\) against (G1).

### Resonant parameter families

**Exercise 1 (foundation: shift a periodic cosine).** For complex \(a\) and real \(h\), find the entire Fourier series and the exact distributional source of \(f_a(x-h)\), including all integer resonances.

**Exercise 2 (advanced: differentiate at a resonance).** For an integer \(m>0\), differentiate the entire periodic family \(f_a\) at \(a=m\). Find every coefficient of the resulting \(v_m\), its mean and its full equation.

### One-sided boundary spectra

**Exercise 5 (intermediate: approach tangent from below).** Find both whole transforms of the limits of \(\tan(x-i\epsilon)\) and \(\tan^2(x-i\epsilon)\). Include every atom and justify convergence.

**Exercise 6 (advanced: the cotangent upper boundary).** Determine both whole upper boundary transforms of \(\cot(x+i\epsilon)\) and its square, with strong convergence and exact zero terms.

## Solutions

### Sampling densities and measures

**Solution 7.** Direct finite integration gives \(Ff(n)=2\sin(an)/n\) for \(n\ne0\), with value \(2a\) at zero. The Gaussian transform is \(F\phi(n)=\sqrt{\pi/b}e^{-n^2/(4b)}\). Also
\[
\begin{gathered}
(f*\phi)(t)=\frac{\sqrt\pi}{2\sqrt b}\\
{}\times\left[\operatorname{erf}(\sqrt b(t+a))
-\operatorname{erf}(\sqrt b(t-a))\right],
\end{gathered}
\]
where \(\operatorname{erf}(s)=2\pi^{-1/2}\int_0^s e^{-r^2}dr\). Theorem 4.1, formula (4.1), gives
\[
\begin{gathered}
2\pi\sum_k(f*\phi)(2\pi k)\\
=\sqrt{\frac\pi b}\left(2a+4\sum_{n\ge1}
\frac{\sin(an)}n e^{-n^2/(4b)}\right).
\end{gathered}
\]
The physical sum is absolute by the uniform Gaussian translate bound in (4.3), or by the Gaussian tail of its finite convolution integral. The frequency sum has Gaussian decay. This application requires only \(f\in L^1\); its two discontinuities do not meet (4.2)'s weak-second-derivative hypothesis, and no delta-test specialization for this indicator has been assumed.

**Solution 8.** The first derivative is \(-a^2xe^{-a|x|}\), continuous at zero, and the second is \((-a^2+a^3|x|)e^{-a|x|}\). Thus \(f,f',f''\in L^1\), with no point mass in either weak derivative. The two absolute half-line Laplace integrals give \(F[e^{-a|x|}]=2a/(a^2+\xi^2)\). Since \(f=e^{-a|x|}-a\partial_ae^{-a|x|}\), dominated parameter differentiation yields
\[
Ff(\xi)=\frac{4a^3}{(a^2+\xi^2)^2}.
\]
The physical samples, with \(q=e^{-2\pi a}\), sum to
\[
\begin{gathered}
1+2\sum_{k\ge1}(1+2\pi ak)q^k\\
=\coth(\pi a)+\pi a\operatorname{csch}^2(\pi a).
\end{gathered}
\]
Both geometric sums and their first weighted sums are absolute. (4.2) therefore gives
\[
\begin{gathered}
\sum_{n\in\mathbb Z}\frac1{(a^2+n^2)^2}\\
=\frac\pi{2a^3}\coth(\pi a)
+\frac{\pi^2}{2a^2}\operatorname{csch}^2(\pi a).
\end{gathered}
\]
All normalizing factors follow from dividing \(2\pi\) times the physical sum by \(4a^3\).

**Solution 11.** The cusp is continuous. Its first derivative equals \(+af\) to the left of \(c\) and \(-af\) to the right. Integration by parts on both half-lines gives
\[
\begin{gathered}
f''=a^2f\,dx-2a\delta_c,\\
Ff(\xi)=e^{-ic\xi}\frac{2a}{a^2+\xi^2}.
\end{gathered}
\tag{M11}
\]
The jump in the first derivative is \(-2a\), fixing the negative atom. The ordinary density has mass \(2a\), and the atom has absolute mass \(2a\); their total variation is \(4a\). Also \(\|f\|_1=2/a\) and \(\|f'\|_1=2\). Theorem 4.2 therefore applies, although \(f''\) is not an \(L^1\) function. Its regular density and atom are both part of the hypothesis.

Choose \(t\in[0,L]\) representing \(h-c\) modulo \(L\). At the two endpoint choices the following values agree. Separating positive and negative translates and summing geometric series gives
\[
\begin{gathered}
\sum_k e^{-a|t+Lk|}\\
=\frac{e^{-at}+e^{-a(L-t)}}{1-e^{-aL}}\\
=\frac{\cosh(a(t-L/2))}{\sinh(aL/2)}.
\end{gathered}
\tag{M12}
\]
The first series is absolute, including at \(t=0,L\). Substituting (M11) in (M3) and dividing by \(2a\) now yields
\[
\begin{gathered}
\sum_{n\in\mathbb Z}
\frac{e^{2\pi in(h-c)/L}}{a^2+(2\pi n/L)^2}\\
=\frac{L}{2a}
\frac{\cosh(a(t-L/2))}{\sinh(aL/2)}.
\end{gathered}
\tag{M13}
\]
Its frequency sum is absolute. At \(L=2\pi\), \(h=c\), this gives \(\sum_n(a^2+n^2)^{-1}=(\pi/a)\coth(\pi a)\), consistently with the massive Green function evaluated at zero. The general formula retains the shift and period instead of suppressing their phases.

**Solution 12.** The measure has total variation two. Its convolution and transform are
\[
\begin{gathered}
g(x)=e^{-b(x-c)^2}\\
{}+i e^{-b(x-d)^2},\\
F\nu(\xi)=e^{-ic\xi}+i e^{-id\xi}.
\end{gathered}
\tag{M14}
\]
Put \(\omega_n=2\pi n/L\). The whole Gaussian transform and (M1) give
\[
\begin{gathered}
A_n=e^{i\omega_n(h-c)}\\
{}+i e^{i\omega_n(h-d)},\\
L\sum_k g(h+Lk)\\
=\sqrt{\pi/b}\sum_n e^{-\omega_n^2/(4b)}A_n.
\end{gathered}
\tag{M15}
\]
Both sides converge absolutely; Gaussian lattice tails justify every differentiated periodization too. The coefficient \(i\) remains inside the complex bilinear identity. There is no conjugation of the second phase.

For \(A>0\), let \(v=1_{[-A,A]}\). It is \(L^1\), so \(v*\phi\) meets the original theorem. But its whole derivatives are
\[
\begin{gathered}
v'=\delta_{-A}-\delta_A,\\
v''=\delta_{-A}'-\delta_A'.
\end{gathered}
\tag{M16}
\]
Choose a compact smooth \(0\le\chi\le1\), supported near \(A\) away from \(-A\), with \(\chi(A)=1\). Set \(\theta_N(x)=\chi(x)\sin(N(x-A))\). All these tests have one fixed compact support and supremum at most one. Their derivative at \(A\) is \(N\), and at \(-A\) it is zero. Thus \(v''(\theta_N)=N\).

A locally finite complex measure would bound these pairings by its total variation on that fixed compact set. Their unbounded values prove that \(v''\) is not such a measure, and in particular not a finite measure. Hence (M3)'s hypothesis does not admit the unsmoothed indicator. The valid Gaussian-convolution application in Solution 7 remains intact.

### Periodic inverses and zero modes

**Solution 3.** Set
\[
G_\mu(x)=\frac{\cosh(\mu(x-\pi))}{2\mu\sinh(\pi\mu)},
\qquad0\le x\le2\pi,
\]
and extend continuously. On each open period it solves \(G_\mu''=\mu^2G_\mu\). Its derivative immediately to the left of zero is \(+1/2\), and immediately to the right is \(-1/2\); the jump is \(-1\). Periodwise integration by parts proves \(G_\mu''=\mu^2G_\mu-C_{2\pi}\), with no delta derivative because the function is continuous. The periodic coefficient of the comb is \(1/(2\pi)\). The equation therefore fixes
\[
\begin{gathered}
G_\mu(x)=\frac1{2\pi}\sum_{n\in\mathbb Z}
\frac{e^{inx}}{\mu^2+n^2},\\
\operatorname{mean}G_\mu=\frac1{2\pi\mu^2}.
\end{gathered}
\]
The series is absolute and uniform; smooth periodic test uniqueness from Theorem 2.1 identifies it with the displayed continuous function. Every periodic homogeneous solution has coefficients killed by the strictly positive \(\mu^2+n^2\); the same full uniqueness proof makes it zero. This establishes uniqueness among all periodic distributions.

**Solution 4.** The unique solution is \(u(x)=G_\mu(x)-G_\mu(x-h)\), by Solution 3 and translation of its whole equation. Its entire series has coefficients
\[
\frac{1-e^{-inh}}{2\pi(\mu^2+n^2)},
\]
so its mean is zero. Absolute uniform convergence makes it a continuous periodic function. At zero, periodicity and the explicit even profile give
\[
u(0)=\frac{\cosh(\pi\mu)-\cosh(\mu(h-\pi))}
{2\mu\sinh(\pi\mu)}.
\]
The first Green term contributes derivative jump \(-1\) at zero, while the negative translated term contributes jump \(+1\) at \(h\). Their ordinary equations hold away from those two lattices, and these exact jumps give the two source signs. Subtracting two solutions leaves the zero homogeneous solution from Solution 3, proving uniqueness without an extra mean condition.

**Solution 9.** The periodic pairing and full coefficient uniqueness proof in Theorem 2.1 apply to every periodic distribution. Normalize coefficients by
\[
c_n(w)=\frac1{2\pi}w_{\rm per}(e^{-inx}).
\]
Since the comb has coefficient \(1/(2\pi)\), the equation forces \((\lambda+n^2)c_n(K)=1/(2\pi)\) for every integer \(n\). Therefore the exact permitted set and its unique solution are
\[
\begin{gathered}
\lambda\in\mathbb C\setminus\{-m^2:m=0,1,\ldots\},\\
K_\lambda(x)=\frac1{2\pi}
\sum_{n\in\mathbb Z}\frac{e^{inx}}{\lambda+n^2}.
\end{gathered}
\tag{G7}
\]
For a compact parameter set in this open domain, every finite denominator is bounded away from zero and, for all sufficiently large \(|n|\), \(|\lambda+n^2|\ge n^2/2\). The series is absolutely and uniformly convergent in the physical variable and locally uniformly in the parameter. Multiplying its coefficients by \(\lambda+n^2\) yields the whole comb identity, strongly on Schwartz tests by their rapidly decreasing Fourier samples. The series is therefore an actual solution. A homogeneous solution has every coefficient zero; the full periodic uniqueness proof makes it zero. At \(\lambda=-m^2\), the nonzero right side of the coefficient equation at \(n=m\) makes any solution impossible, also at \(m=0\).

For a noninteger complex \(a\), the denominator \(2a\sin(\pi a)\) is nonzero: the complex zeros of sine are precisely the integer multiples of \(\pi\), as its exponential formula shows. Set
\[
\begin{gathered}
K_{-a^2}(x)=-\frac{\cos(a(x-\pi))}{2a\sin(\pi a)},\\
0\le x\le2\pi .
\end{gathered}
\tag{G8}
\]
The endpoint values agree. Its derivative on the right of zero is \(-1/2\), and its derivative on the left is \(+1/2\), so its jump is \(-1\). Its ordinary equation is \(K''=-a^2K\) between the joins. The same complete periodwise integration by parts as in Theorem 1.1 therefore gives \((-a^2-D^2)K=C_{2\pi}\) with the correct positive source. Uniqueness identifies this profile with (G7). Changing \(a\) to \(-a\) leaves (G8) unchanged, so a choice of square root does not change it. At \(a=i\mu\), it becomes \(\cosh(\mu(x-\pi))/(2\mu\sinh(\pi\mu))\), agreeing with the original massive Green function.

Termwise parameter differentiation is justified locally uniformly. The \(j\)-th derivative of the \(n\)-th scalar coefficient is
\[
\frac{(-1)^j j!}{2\pi(\lambda+n^2)^{j+1}},
\]
whose tail has a summable uniform bound \(C_{j,K}|n|^{-2j-2}\) on a compact parameter set \(K\). The finitely many other terms and their derivatives are bounded there. Integrate the coefficient derivative along the straight parameter segment inside a disk avoiding the poles. Uniform convergence passes that identity through the series, and the uniform continuity of the derivative sum on a smaller disk gives the complex difference quotient in the uniform periodic norm. This proves holomorphy with all the stated derivatives.

To compute the poles, separate the resonant terms in a small parameter disk containing no other spectral value. For \(m=0\) there is the single term \(1/(2\pi\lambda)\). For \(m\ge1\) the two terms \(n=\pm m\) sum to \(\cos(mx)/(\pi(\lambda+m^2))\). The remaining series and all its parameter derivatives converge locally uniformly by the same finite-head and summable-tail bounds. Thus every pole is simple and its complete residue is
\[
\begin{gathered}
\mathop{\rm Res}_{\lambda=0}K_\lambda=\frac1{2\pi},\\
\mathop{\rm Res}_{\lambda=-m^2}K_\lambda\\
=\frac{\cos(mx)}{\pi},\qquad m\ge1.
\end{gathered}
\tag{G9}
\]
The finite part at zero is \(A_0\) from (G1), with zero constant coefficient and full equation \(-D^2A_0=C_{2\pi}-1/(2\pi)\). For \(m\ge1\) the finite part is
\[
\begin{gathered}
H_m=\frac1{2\pi}\sum_{n\ne\pm m}
\frac{e^{inx}}{n^2-m^2},\\
(-m^2-D^2)H_m\\
=C_{2\pi}-\frac{\cos(mx)}{\pi},\\
c_m(H_m)=c_{-m}(H_m)=0,\\
\operatorname{mean}H_m=-\frac1{2\pi m^2}.
\end{gathered}
\tag{G10}
\]
Its series is absolutely uniform: exclude the two zero denominators, bound the finite remaining head directly, and use \(O(n^{-2})\) for the tail. Coefficient multiplication gives the exact reduced source, whose two resonant coefficients vanish. If two solutions of this reduced equation have zero resonant coefficients, their difference has every coefficient zero by the multiplier equation, hence is zero by full periodic uniqueness. Without that condition the entire homogeneous ambiguity is the span of \(e^{imx}\) and \(e^{-imx}\), as follows by subtracting precisely those two coefficient modes and using uniqueness. At zero the corresponding ambiguity is the constants. These statements retain the removed modes and their exact source coefficients.

**Solution 10.** The required profile is
\[
\begin{gathered}
P_{r,L}(x)=
\frac{(-1)^{r+1}L^{2r-1}}{(2r)!}\\
{}\times B_{2r}(x/L),\\
P_{r,L}(x)=
\frac1L\sum_{n\ne0}\\
{}\times\frac{e^{2\pi inx/L}}{(2\pi n/L)^{2r}}.
\end{gathered}
\tag{G11}
\]
The first line uses the mean-zero polynomial and continuous periodic extension in Bernoulli Theorem 1.2. Substitute its full Fourier series (B2), use \(i^{2r}=(-1)^r\), and simplify the two signs and powers of \(L\). This gives exactly the second line, which is absolutely and uniformly convergent, with mean zero and the stated coefficients.

The full affine contact identity (B8), with \(m=2r,a=L,h=0\), gives
\[
\begin{gathered}
D^{2r}P_{r,L}\\
=(-1)^{r+1}(1/L-C_L),\\
(-D^2)^rP_{r,L}=C_L-1/L .
\end{gathered}
\tag{G12}
\]
All these identities hold on every Schwartz test. For uniqueness among periodic distributions, rescale the periodic pairing and smooth test expansion from Theorem 2.1 to period \(L\). At every nonzero frequency the multiplier \((2\pi n/L)^{2r}\) is nonzero. The equation fixes the coefficients in (G11), while the zero frequency is fixed to zero by the mean condition. The difference of two candidates has every coefficient zero and hence every smooth periodic pairing zero; the same partition argument recovers every compact-test pairing. It is therefore zero on the whole line.

Bernoulli regularity gives \(P_{r,L}\in C^{2r-2}\), and its next piecewise derivative is
\[
D^{2r-1}P_{r,L}=(-1)^{r+1}B_1(x/L)
\]
between the joining points. It has jump \((-1)^r\), the scalar times the sawtooth jump \(-1\). This jump is nonzero, so the function is not \(C^{2r-1}\). For \(r=1,L=2\pi\), its profile is \(\pi B_2(x/(2\pi))=A_0\). Its derivative jump is \(-1\) and its equation is exactly (G2), completing the normalization check.

### Resonant parameter families

**Solution 1.** Translation of Theorem 1.1's absolutely uniformly convergent series gives
\[
\begin{gathered}
f_a(x-h)=\sum_n c_n(a)e^{-inh}e^{inx},\\
c_n(a)=\frac{a\sin(\pi a)(-1)^n}{\pi(a^2-n^2)}.
\end{gathered}
\]
Every removable value is the original integral coefficient: at \(a=0\) only \(c_0=1\) remains, and at \(a=\pm m\), \(m>0\) integer, only \(c_{\pm m}=1/2\) remain. Translation sends \(\delta_b\) to \(\delta_{b+h}\), as follows by substituting in its test pairing. Hence
\[
\begin{gathered}
(\partial_x^2+a^2)f_a(x-h)\\
=2a\sin(\pi a)\sum_k\delta_{h+(2k+1)\pi}.
\end{gathered}
\]
The series remains absolute and uniform for every compact parameter set; its translated source is a strongly tempered atom sum because Schwartz values on this lattice are summable. At integer \(a\) the coefficient of that source is zero, giving the expected ordinary homogeneous cosine.

**Solution 2.** On the principal period, \(v_m(x)=-x\sin(mx)\), extended continuously and periodically. The endpoint values are both zero. The compact-parameter uniform holomorphy in Theorem 1.1 permits coefficient and distributional differentiation. For \(n\ne\pm m\), differentiating (1.2) at \(a=m\) gives
\[
d_n=\frac{m(-1)^{m+n}}{m^2-n^2}.
\]
At \(n=\pm m\) use the entire integral formula, written as the sum of \(\sin(\pi(a-m))/(2\pi(a-m))\) and \(\sin(\pi(a+m))/(2\pi(a+m))\). The first derivative is zero at \(a=m\); the second is \(1/(4m)\). Thus \(d_m=d_{-m}=1/(4m)\), and the mean is \(d_0=(-1)^m/m\). All coefficients are absolutely summable. Differentiating (1.1), including its multiplier, gives
\[
\begin{gathered}
v_m''+m^2v_m\\
=2\pi m(-1)^m\sum_k\delta_{(2k+1)\pi}\\
{}-2m\cos(mx).
\end{gathered}
\]
The derivative of \(2a\sin(\pi a)\) at \(m\) is \(2\pi m(-1)^m\). This proves the entire equation, including the forcing that would be lost by differentiating only the right side. Its resonant Fourier coefficients are consistent: the two cosine coefficients are canceled by the corresponding comb coefficients.

### One-sided boundary spectra

**Solution 5.** The regularized functions are the complex conjugates of Theorem 3.1's upper functions. Conjugation is continuous on the strong tempered topology, because it conjugates the test pairing and sends a bounded test set to a bounded set. For the first boundary value,
\[
T^-=-i\left(1+2\sum_{m\ge1}(-1)^me^{-2imx}\right).
\]
The coefficient series pairs absolutely with Schwartz tests, with tails bounded by an arbitrarily summable inverse power uniformly on bounded test sets; the regularized coefficients have the extra bounded factor \(e^{-2m\epsilon}\), which tends to one. Thus the whole limit is strong and
\[
FT^-=-2\pi i\delta_0-4\pi i\sum_{m\ge1}(-1)^m\delta_{-2m}.
\]
The exact identity \(\tan^2=\partial_x\tan-1\) passes through the strong limit. Multiplication of this transform by \(i\xi\), then subtraction of \(2\pi\delta_0\), gives
\[
FQ^-=-2\pi\delta_0-8\pi\sum_{m\ge1}(-1)^m m\delta_{-2m}.
\]
A Schwartz weight of exponent greater than two bounds its atom tails. Both zero contacts and the reflected side of the spectrum are therefore fixed.

**Solution 6.** For \(w=e^{2ix-2\epsilon}\), \(|w|<1\),
\[
\begin{gathered}
\cot(x+i\epsilon)=-i\frac{1+w}{1-w}\\
=-i\left(1+2\sum_{m\ge1}e^{2imx-2m\epsilon}\right).
\end{gathered}
\]
The geometric series and every derivative converge uniformly at fixed positive \(\epsilon\). Its test terms are \(F\theta(-2m)\), bounded by a fixed Schwartz seminorm times \((1+m)^{-M}\). Split into a uniformly small tail and a finite head to let \(\epsilon\downarrow0\); this proves strong convergence. Plane-wave normalization gives
\[
FC=-2\pi i\delta_0-4\pi i\sum_{m\ge1}\delta_{2m}.
\]
Here \(\cot'=-1-\cot^2\), so the square limit is \(Q=-C'-1\). Its transform is
\[
FQ
=-2\pi\delta_0-8\pi\sum_{m\ge1}m\delta_{2m}.
\]
The notation on the left denotes the limit of the regularized squares, not a product of two singular distributions. The linearly growing atom coefficients have uniformly summable Schwartz tails for \(M>2\). This proves every whole identity and convergence assertion.

## References

- [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, Theorems1.1–1.2 and Solutions2 and9: full periodic uniqueness, scaled comb, Bernoulli kernels and exact reciprocal-power sums.
- [Schwartz Fourier foundations](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16.1–16.2; [positive and complex measure foundations](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), (M10)–(M12). The linked programme proofs retain their stated licences.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), §7.2 and Exercises7.2.2–7.2.5, printed page389, with answers on page413. These give periodic Fourier examples, tangent boundary spectra and integrable sampling. The approved purchased edition is a research source. The arguments here include the complete convergence and representative proofs, finite-measure extension, parameter and zero-mode analysis, and independently organized exercises.
