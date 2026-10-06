# Cosine crossings and spectral-gap bounds

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); linked prerequisites retain their stated licences.*

A real function bounded strictly below one cannot disturb the pattern of cosine crossings if its spectrum lies in the cosine band. Every half-period retains one simple zero, and the entire extension has no additional complex zeros. A spectral gap gives a different sharp result: a bounded weak derivative forces the function itself to be bounded by Bohr's constant. A periodic sign-change argument and positive periodization prove both conclusions without an initial boundedness assumption in the gap case.

Use \(Fu(\xi)=\int e^{-ix\xi}u(x)dx\), \(D=-i\partial\), bilinear distributional pairings and the canonical smooth or Lipschitz representative. [Sharp bounds for compact spectra](sharp-bounds-for-compact-spectra.md), Lemma0.1 and Theorems2.1–3.1, supplies the full identity and maximum principles, derivative contractions and entire extension. [Resolvent sampling and positive periodization](resolvent-sampling-and-positive-periodization.md), Theorem4.1 and Solution8, supplies positive periodization, its whole Fourier support and the exact finite degree. [Periodic Green functions and boundary spectra](periodic-green-functions-and-boundary-spectra.md), Theorem4.1's proof of(4.2), gives the complete weak primitive argument, including local absolute continuity and uniqueness of the representative. [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, supplies continuous periodic Fourier uniqueness. [Tempered growth and spectral cutoffs](tempered-growth-and-spectral-cutoffs.md), Lemma2.1 and Theorem3.1, proves full Schwartz convolution and spectral cutoffs. The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and16, prove the elementary calculus, algebraic operations, convergence and integration used below. The finite polynomial division argument is included where needed.

## Every cosine crossing is simple, and every complex zero is real

**Theorem 1.1.** Let \(\lambda>0\), and let \(u\) be real and bounded with \(\operatorname{supp}Fu\subset[-\lambda,\lambda]\). Use its canonical entire extension and put \(q=\|u\|_\infty<1\). Then
\[
\begin{gathered}
\frac{|u'(x)|^2}{\lambda^2}+|u(x)|^2\le q^2,\\
x\in\mathbb R.
\end{gathered}
\tag{1.1}
\]
The entire function \(g(z)=u(z)-\cos(\lambda z)\) has precisely one zero in each open interval
\((n\pi/\lambda,(n+1)\pi/\lambda)\), each zero is simple, and these are all its complex zeros. At each real zero the derivative \(g'\) has the sign of \(\sin(\lambda x)\).

**Pointwise estimate and real zeros.** [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Theorem 2.1 gives, with its full finite-measure proof at \(p=\infty\),
\[
\bigl|\sin\alpha\,u'(x)/\lambda+\cos\alpha\,u(x)\bigr|\le q
\]
for every real \(\alpha\), at every point of the continuous representative. For the real vector \((u'(x)/\lambda,u(x))\), choosing the unit vector in its direction proves (1.1); the zero vector is immediate. No restriction to a countable set of parameters is required, because the proof of [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Theorem 2.1 gives the everywhere assertion separately for every fixed parameter.

At \(x=n\pi/\lambda\), \(g(x)\) is strictly negative for even \(n\) and strictly positive for odd \(n\). The intermediate value theorem therefore gives a zero in each open interval. At such a zero \(u(x)=\cos(\lambda x)\); (1.1) implies
\[
|u'(x)|/\lambda
\le\sqrt{q^2-\cos^2(\lambda x)}
<|\sin(\lambda x)|.
\]
The square root is defined there because its argument is nonnegative by (1.1). Hence \(g'(x)=u'(x)+\lambda\sin(\lambda x)\) is nonzero and has the sign of the sine. It has the same strict crossing orientation at every zero in a given interval.

The entire \(g\) is not identically zero, by its grid values. Its zeros are isolated by the Taylor argument in [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Lemma0.1. There are finitely many in each closed grid interval: otherwise compactness would give a limit zero there, including at the endpoints, which were excluded. Two consecutive simple zeros must have opposite crossing orientations, since the sign between them is constant. The orientation just calculated is the same for all zeros in that open interval. Consequently there can be only one. This proves the complete real assertion and the precise derivative sign.

**Finite periodic approximants.** For integers \(j\ge2\), set
\[
\begin{gathered}
t_j=1-j^{-1},\quad N_j=j^2,\\
\epsilon_j=\lambda/(2N_j),\\
v_j(x)=u(t_jx).
\end{gathered}
\]
The spectrum of \(v_j\) lies in \([-t_j\lambda,t_j\lambda]\), by the full Fourier scaling identity, and its real bound is \(q\). Apply [*Resolvent sampling and positive periodization*](resolvent-sampling-and-positive-periodization.md)'s positive periodization to \(v_j\), and call the result \(p_j\). It is real, bounded by \(q\), and has period \(2\pi N_j/\lambda\). Its complete finite-degree conclusion, including the vanishing triangular-spectrum endpoints, gives
\[
\begin{gathered}
p_j(x)=V_j(\lambda x/N_j),\\
\deg V_j\le\lceil t_jN_j\rceil\\
=N_j-j\le N_j-1.
\end{gathered}
\tag{1.2}
\]
Here \(V_j\) is a real trigonometric polynomial. The coefficients supply its entire extension.

For any real trigonometric polynomial \(V\) of degree at most \(N-1\) with \(\sup_{\mathbb R}|V|<1\), the function \(V(\theta)-\cos(N\theta)\) has alternating strict signs at \(\theta=k\pi/N\). There are consequently \(2N\) distinct real roots in the \(2N\) open intervals of one period. With \(w=e^{i\theta}\), the Laurent polynomial becomes
\[
Q(w)=w^N\left(V(\theta)-\frac{w^N+w^{-N}}2\right).
\]
It is a polynomial of degree \(2N\), with leading and constant coefficients both \(-1/2\). Its \(2N\) known roots are distinct points on the unit circle. For completeness, if \(P(w)=\sum_{k=0}^d a_kw^k\) and \(P(r)=0\), the finite identity
\[
 P(w)=(w-r)\sum_{k=1}^d a_k
                  \sum_{j=0}^{k-1}w^{k-1-j}r^j
\]
follows by telescoping each \(w^k-r^k\). At every other distinct root the extracted factor is nonzero, so that root remains a root of the quotient. Applying this identity successively to the \(2N\) distinct known roots exhausts the degree; the remaining factor is the nonzero leading constant. Thus these roots are simple, and there are no others. For complex \(\theta\), \(w=e^{i\theta}\ne0\); if it is a root of \(Q\), its modulus is one, so \(\operatorname{Im}\theta=0\). This proves that the entire difference has no nonreal zero, without importing a root theorem to locate its roots. Apply this argument to (1.2). Each
\[
g_j(z)=p_j(z)-\cos(\lambda z)
\]
is zero-free off the real axis.

**Convergence on the entire complex plane.** On every fixed real compact set, [*Resolvent sampling and positive periodization*](resolvent-sampling-and-positive-periodization.md)'s exact error gives
\[
|p_j(x)-v_j(x)|
\le2q(1-\varphi(\epsilon_jx))\longrightarrow0
\]
uniformly, where \(\varphi(s)=(\sin s/s)^2\), \(\varphi(0)=1\). Continuity of \(u\) also gives \(v_j\to u\) uniformly there. All \(p_j\) have spectrum in \([-\lambda,\lambda]\), by (1.2), and have the same global real bound \(q\).

Choose a single \(\eta\in C_c^\infty(\mathbb R)\) equal to one near that closed band, and put \(f(z)=(2\pi)^{-1}\int e^{iz\xi}\eta(\xi)d\xi\). The entire construction in [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Theorem 3.1 applies to \(f\). Integration by parts in \(\xi\), any number of times, gives, on each complex compact set \(Z\),
\[
\begin{gathered}
\sup_{z\in Z}|f(z-s)|\\
\le C_{Z,L}(1+|s|)^{-L},\qquad s\in\mathbb R.
\end{gathered}
\tag{1.3}
\]
for every integer \(L\ge0\). The compact support of \(\eta\) eliminates all boundary terms; differentiating \(\eta(\xi)e^{iz\xi}\) gives bounded coefficients uniformly for \(z\in Z\).

The integrals \(\int p_j(s)f(z-s)ds\) and \(\int u(s)f(z-s)ds\) are entire by (1.3) and its derivative versions. They equal \(p_j(z)\) and \(u(z)\), respectively: on the real line this is [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md)'s fixed-point identity, and the one-variable identity theorem extends it everywhere. Split their difference into a fixed bounded real interval and its complement. On the first part local uniform real convergence applies; on the second (1.3), with \(L>1\), and the bound \(2q\) make the tail uniformly small on \(Z\). Thus \(p_j\to u\), and \(g_j\to g\), locally uniformly throughout \(\mathbb C\).

If \(g\) had a nonreal zero \(z_0\), choose a small closed disk about it avoiding the real axis, with \(g\) nonzero on its boundary; isolation of zeros permits this choice. Put \(m=\min_{\partial B}|g|>0\). For large \(j\), \(|g_j|\ge m/2\) on the boundary. Since \(g_j\) is zero-free on that whole disk, \(1/g_j\) is holomorphic there. [Sharp bounds for compact spectra](sharp-bounds-for-compact-spectra.md), Lemma0.1, gives the complete maximum principle: a continuous modulus attains a maximum on the compact disk, and an interior maximum forces constancy, so the boundary controls every interior value. Hence \(|1/g_j|\le2/m\) inside, so \(|g_j(z_0)|\ge m/2\). This contradicts \(g_j(z_0)\to g(z_0)=0\). There are therefore no nonreal zeros. All claims, including the full pointwise Bernstein bound, are proved. \(\square\)

## The sharp Bohr bound from a spectral gap

**Theorem 2.1.** Let \(\lambda>0\), let \(u\) be a real distribution on \(\mathbb R\) with distributional derivative \(u'\in L^\infty\), and suppose
\(\operatorname{supp}Fu\cap(-\lambda,\lambda)=\varnothing\).
The bounded derivative makes \(u\) tempered by the primitive argument below, so its Fourier transform is well defined. Set \(M=\|u'\|_\infty\). Its unique continuous representative is bounded and satisfies
\[
\|u\|_\infty\le\frac{\pi}{2\lambda}M.
\tag{2.1}
\]
In particular if \(M<1\), the inequality is strictly below \(\pi/(2\lambda)\). For
\[
h(x)=\min_{k\in\mathbb Z}|x-2\pi k/\lambda|
                   -\frac{\pi}{2\lambda},
\]
if \(M<1\), \(h-u\) has the same strict sign as \(h\) at every maximum and minimum point of \(h\). The constant in (2.1) is sharp.

**The representative and its boundedness.** A bounded weak derivative gives the locally absolutely continuous primitive
\(G(x)=\int_0^xu'(t)dt\). The distribution \(u-G\) has derivative zero. Every integral-zero compact smooth test is the derivative of its compact smooth primitive; hence a distribution with zero derivative depends only on the integral of its test, and is constant. This is the complete zero-derivative argument in [Periodic Green functions and boundary spectra](periodic-green-functions-and-boundary-spectra.md), Theorem4.1's proof of(4.2), and it also applies when the original \(u\) was merely a distribution. Thus \(u=G+c\), with \(c\) real, and its canonical representative is globally \(M\)-Lipschitz. It has at most linear growth and is tempered. Continuity makes that representative unique.

Choose \(\chi\in C_c^\infty((-\lambda,\lambda))\) equal to one near zero, and let \(\psi=G\chi\) under Fourier inversion. This \(\psi\) is Schwartz and \(\int\psi=\chi(0)=1\). [*Tempered growth and spectral cutoffs*](tempered-growth-and-spectral-cutoffs.md)'s complete global convolution identity gives \(F(u*\psi)=\chi Fu=0\), so the smooth convolution is zero. Its integral is absolutely convergent, because \(u\) has at most linear growth. Consequently, everywhere,
\[
\begin{gathered}
u(x)=\int\psi(t)\\
{}\times\bigl(u(x)-u(x-t)\bigr)\,dt,\\
|u(x)|\le M\int|t\psi(t)|\,dt.
\end{gathered}
\tag{2.2}
\]
The right side is finite and uniform in \(x\). This proves boundedness without adding it to the hypotheses. Write \(B=\|u\|_\infty<\infty\). If \(M=0\), (2.2) already gives \(u=0\).

**A finite periodic sign-change argument.** Fix \(\mu>0\) and an integer \(N\ge1\), and let \(v\) be real and periodic with period \(T=2\pi N/\mu\), satisfying \(|v(x)-v(y)|\le L|x-y|\). Suppose its Fourier coefficients at the frequencies \(2\pi k/T\), \(|k|<N\), all vanish. We prove
\[
\|v\|_\infty\le\frac{\pi}{2\mu}L.
\tag{2.3}
\]
Whenever \(v'\in L^\infty\) as a distribution, the proved weak primitive theorem supplies this increment bound with \(L=\|v'\|_\infty\). Thus the same statement gives exactly the weak-derivative norm estimate needed below, without assuming pointwise derivatives of a general Lipschitz function.

First suppose \(q=L<1\). Let \(h_\mu\) be the displayed triangle with \(\lambda\) replaced by \(\mu\), and translate it by an arbitrary \(s\). Its period \(T/N\) implies that every \(T\)-periodic coefficient is zero unless its index is a multiple of \(N\): translate the coefficient integral by \(T/N\) and compare its phase. Its zero coefficient is zero by integrating the two linear pieces of a triangle period. Thus
\(G_s(x)=h_\mu(x-s)-v(x)\) is orthogonal, by ordinary integration, to every trigonometric polynomial of degree at most \(N-1\) on this circle.

The triangle has \(2N\) monotone cells in one period, each of length \(\pi/\mu\). For \(x<y\) in an increasing cell, the increment of the difference is at least \((1-q)(y-x)>0\); in a decreasing cell it is at most \(-(1-q)(y-x)<0\). These follow directly from the triangle's slopes and the Lipschitz increment bound. Thus the difference is strictly monotone on each whole cell. It has at most one zero in the interior of each cell. A zero at a corner is a strict local minimum or maximum and is not a sign change. All zeros are finite in number, and all sign changes occur in the cell interiors.

A continuous periodic real function with finitely many zeros has an even number \(2r\) of sign changes. If \(2r<2N\), list their points \(x_1,\ldots,x_{2r}\) in cyclic order and form
\[
Q(x)=c\prod_{\ell=1}^{2r}
       \sin\!\left(\frac{\pi(x-x_\ell)}T\right).
\tag{2.4}
\]
When \(r=0\), take \(Q=c\). Because the number of factors is even, this is \(T\)-periodic; expanding the finite product of exponentials shows that its degree is at most \(r<N\). Its signs change precisely at the listed points. Choose \(c=1\) or \(-1\) so that \(G_sQ\ge0\) on the whole circle. Tangential zeros of \(G_s\) do not change its sign and introduce no difficulty. The product is positive on a nonempty open interval, since neither function vanishes on an interval. Therefore \(\int_0^T G_sQ>0\), contradicting the stated orthogonality. This proves that \(G_s\) has at least \(2N\) sign changes.

There are at most \(2N\) available cell interiors, each allowing at most one. Thus every cell has exactly one interior crossing, and no corner can be zero. Strict monotonicity then gives \(G_s<0\) at each minimum corner and \(G_s>0\) at each maximum corner. This proves the full periodic comparison, for every translate \(s\).

For general \(L\ge0\), put \(M_v=L\) and apply this comparison to \(v/c\) for every \(c>M_v\). Given any real \(x\), choose \(s\) first to make \(x\) a triangle maximum, then to make it a minimum. The two strict comparisons give
\(-c\pi/(2\mu)<v(x)<c\pi/(2\mu)\).
Let \(c\downarrow M_v\) and then take the supremum. This proves (2.3), including \(M_v=0\). Only the finite low-frequency orthogonality and the stated Lipschitz increment bound were used; the weak primitive proof supplies that bound for every input with a bounded weak derivative.

**Periodizing a bounded Lipschitz input preserves the derivative bound in the limit.** Let \(u_\epsilon\) be [*Resolvent sampling and positive periodization*](resolvent-sampling-and-positive-periodization.md)'s positive periodization, of period \(a=\pi/\epsilon\). Its complete support conclusion says that its spectrum avoids
\((-\lambda+2\epsilon,\lambda-2\epsilon)\), when \(2\epsilon<\lambda\); its continuity follows from the locally uniform sum of continuous summands.

There is a finite uniform constant
\[
C_\varphi=\sup_{s\in\mathbb R}
                \sum_{k\in\mathbb Z}|\varphi'(s+\pi k)|<\infty.
\]
Here is an explicit bound. The finite triangular integral for \(\varphi\) gives \(|\varphi'|\le2/3\) everywhere. Its explicit derivative for \(|s|\ge1\) gives \(|\varphi'(s)|\le3|s|^{-2}\). Reduce \(s\) to \([-\pi/2,\pi/2]\); for \(k\ne0\), \(|s+\pi k|\ge\pi|k|/2>1\). The reciprocal-square comparison \(\sum_{k\ge1}k^{-2}\le1+\int_1^\infty t^{-2}dt=2\) then gives
\[
C_\varphi\le\frac23+\frac{48}{\pi^2}.
\tag{2.5}
\]
Each summand in [*Resolvent sampling and positive periodization*](resolvent-sampling-and-positive-periodization.md)'s formula is locally absolutely continuous. Its weak derivative is represented by
\[
\begin{gathered}
u'(x+ak)\varphi(\epsilon x+\pi k)\\
{}+\epsilon u(x+ak)\varphi'(\epsilon x+\pi k)
\end{gathered}
\]
almost everywhere. On every compact interval the function tails converge uniformly, and the derivative tails converge in the essential supremum norm, by the reciprocal-square bounds and \(|u'|\le M\), \(|u|\le B\). The product formula follows directly by applying the distributional product rule to the smooth weight. Uniform convergence of functions and convergence of the derivative tails in essential supremum give the corresponding weak derivative for the sum, by pairing with compact tests. The proved weak primitive theorem then gives its locally absolutely continuous representative; continuity identifies it with the displayed sum. The positive partition sums to one, and (2.5) bounds the second term of the derivative. Hence
\[
\|u_\epsilon'\|_\infty\le M+\epsilon B C_\varphi.
\tag{2.6}
\]
This is a global estimate; no continuity of \(u'\) was assumed.

Take integers \(N\ge2\), put \(\epsilon_N=\lambda/(2N)\) and \(\mu_N=\lambda(1-1/N)\). Then \(u_{\epsilon_N}\) has period
\[
\frac{2\pi N}{\lambda}
=\frac{2\pi(N-1)}{\mu_N}
\]
and has zero coefficients at every index \(|k|<N-1\), by the full support gap. Apply (2.3) with order \(N-1\), then (2.6):
\[
\|u_{\epsilon_N}\|_\infty
\le\frac{\pi}{2\mu_N}
          (M+\epsilon_N B C_\varphi).
\]
[*Resolvent sampling and positive periodization*](resolvent-sampling-and-positive-periodization.md)'s exact positive-periodization error tends to zero uniformly on every real compact set. Thus \(u_{\epsilon_N}(x)\to u(x)\) at every real \(x\). Let \(N\to\infty\) in the last everywhere bound and take the supremum. This proves precisely (2.1).

If \(M<1\), the uniform strict bound \(|u(x)|<\pi/(2\lambda)\) makes \(h-u\) positive at every maximum \(h=\pi/(2\lambda)\), and negative at every minimum \(h=-\pi/(2\lambda)\), as asserted. Sharpness of the non-strict norm inequality is witnessed by \(u=h\) itself: it is real Lipschitz, has derivative of magnitude one almost everywhere, supremum \(\pi/(2\lambda)\), zero mean and period \(2\pi/\lambda\). Its whole periodic Fourier support is on the nonzero integer multiples of \(\lambda\), by the complete absolute coefficient and whole-transform computation in Solution5 below; hence it has the required open spectral gap. All endpoint and representative claims are retained. \(\square\)

## Exercises

**Exercise 1 (foundation: every zero for a constant input).** For real \(|c|<1\), find every complex zero of \(c-\cos(\lambda z)\), its location in each grid interval and its derivative sign. Explain the zero multiplicities at \(c=1\) and \(c=-1\).

**Exercise 2 (foundation: reality is essential).** Give a bounded complex constant of modulus less than one whose spectrum is in the cosine band, but whose difference from the cosine has a nonreal zero. Locate such a zero explicitly.

**Exercise 3 (intermediate: a uniform location and slope bound).** Under Theorem 1.1's hypotheses with \(q=\|u\|_\infty<1\), show that the zero in each grid interval is at least \(\arccos(q)/\lambda\) from either endpoint and satisfies \(|(u-\cos\lambda x)'|\ge\lambda(1-q)\). Give an input attaining the slope constant.

**Exercise 4 (advanced: stability as an amplitude varies).** Let \(f\) be real, bounded by one and band limited to \([-\lambda,\lambda]\). For \(0\le q<1\) and \(|a|\le q\), let \(r_n(a)\) be the zero of \(af(x)-\cos(\lambda x)\) in the \(n\)-th grid interval. Prove continuity, derive \(r_n'(a)\), and show
\[
|r_n(a)-r_n(b)|\le\frac{|a-b|}{\lambda(1-q)}.
\]
Do not assume an implicit-function theorem without justifying the derivative.

**Exercise 5 (intermediate: the full sharp triangle spectrum).** For \(0\le M<1\), \(s\in\mathbb R\), compute the full Fourier series and whole Fourier transform of \(u(x)=M h_\lambda(x-s)\). Verify its derivative norm, spectral gap and exact Bohr norm.

**Exercise 6 (foundation: the missing gap).** Show that a bounded derivative of norm less than one alone does not imply boundedness of the function, nor Bohr's uniform bound. Give the full Fourier distributions of your constant and affine counterexamples.

**Exercise 7 (intermediate: count every periodic triangle crossing).** Let \(N\ge1\), \(\mu>0\), and
\[
\begin{gathered}
v(x)=A\sin((N+1)\mu x/N)\\
{}+B\cos(2\mu x),\qquad A,B\in\mathbb R.
\end{gathered}
\]
Assume \(\mu((N+1)|A|/N+2|B|)<1\). For any translate of \(h_\mu\), determine all signs of \(h_\mu-v\) at its corners and the exact number of its crossings in a period \(2\pi N/\mu\). Give the Bohr norm estimate for \(v\).

**Exercise 8 (advanced: a smooth cutoff cannot attain the Bohr constant).** Let \(\chi\in C_c^\infty((-\lambda,\lambda))\) satisfy \(\chi(0)=1\), and set \(\psi=G\chi\). Prove
\[
\int_{\mathbb R}|t\psi(t)|dt>\frac{\pi}{2\lambda}.
\]
Explain why the preliminary cutoff estimate for a gap input is strictly weaker than the sharp Bohr constant.

## Solutions

**Solution 1.** Put \(\theta=\arccos c\in(0,\pi)\). Theorem 1.1 applies to the constant input, whose spectrum is contained in \(\{0\}\), and proves that all zeros are real and simple. They are exactly
\[
\begin{gathered}
x=(2k\pi\pm\theta)/\lambda,\\
k\in\mathbb Z.
\end{gathered}
\]
In an even cell \(n=2k\), choose \((2k\pi+\theta)/\lambda\); in an odd cell \(n=2k+1\), choose \((2k\pi+2\pi-\theta)/\lambda\). The derivative is \(\lambda\sin(\lambda x)\), positive in even cells and negative in odd ones. At \(c=1\), the zeros \(2k\pi/\lambda\) lie at grid points, and the local expansion \(1-\cos(\lambda x)=\lambda^2(x-x_0)^2/2+\cdots\) makes them double. At \(c=-1\), the odd grid points are double, with the negative quadratic coefficient. The identity \(\cos z=(e^{iz}+e^{-iz})/2\) makes these the whole complex zero sets in the endpoint cases too.

**Solution 2.** Take \(u=i a\), \(0<a<1\), and set \(t=\log(a+\sqrt{1+a^2})>0\), so \(\sinh t=a\). Its modulus is \(a\) and \(Fu=2\pi ia\delta_0\). At
\[
z=(\pi/2-it)/\lambda
\]
the cosine is \(\cos(\pi/2-it)=i\sinh t=ia\). Thus the difference has this nonreal zero despite its strict norm and correct band. The example violates precisely the real-input hypothesis.

**Solution 3.** At a zero \(r\), \(|\cos(\lambda r)|=|u(r)|\le q\). In every half-period this places the angle at least \(\arccos q\) from both grid endpoints. Put \(t=\cos^2(\lambda r)\in[0,q^2]\). The pointwise derivative estimate gives
\[
|g'(r)|\ge\lambda\bigl(\sqrt{1-t}-\sqrt{q^2-t}\bigr)
\ge\lambda(1-q).
\]
For \(q>0\), the parenthesized expression increases with \(t\), by differentiating on \([0,q^2)\) and taking the endpoint limit, so its minimum is its value at zero. If \(q=0\), the only possible \(t\) is zero and the same conclusion holds directly. The input \(u=q\cos(\lambda x)\) has zeros at the midpoints of every cell and slope magnitude \(\lambda(1-q)\) there. This proves sharpness of the slope bound, not just nonvanishing.

**Solution 4.** The roots exist for the whole open parameter interval \(|a|<1\), by Theorem 1.1. Work in that interval first, and then restrict to \([-q,q]\); this also defines the derivative at zero when \(q=0\). On every smaller closed parameter interval Exercise 3 places all roots in one fixed closed subinterval strictly inside the cell. For any \(a_j\to a\), a subsequence of \(r_n(a_j)\) converges; continuity of the equation identifies its limit with the unique root \(r_n(a)\). If the full sequence failed to converge, apply this argument to a subsequence separated from that root, a contradiction. Thus \(r_n\) is continuous.

Write \(g_a(x)=af(x)-\cos(\lambda x)\), \(r_a=r_n(a)\). Subtract the two equations at \(a,b\) and use the real integral fundamental theorem:
\[
\begin{gathered}
0=(b-a)f(r_b)\\
{}+(r_b-r_a)\int_0^1\\
g_a'(r_a+t(r_b-r_a))dt.
\end{gathered}
\]
The last integral tends to \(g_a'(r_a)\ne0\) as \(b\to a\). It is consequently nonzero for all nearby \(b\), and the displayed equation, even when \(r_b=r_a\), gives
\[
r_n'(a)=
-\frac{f(r_a)}{a f'(r_a)+\lambda\sin(\lambda r_a)}.
\]
The root slope bound gives magnitude at most \(1/(\lambda(1-q))\). The expression is continuous in \(a\); integration over the parameter interval gives the required Lipschitz estimate. At its endpoints the same argument gives the appropriate one-sided derivative, which suffices for the integral estimate.

**Solution 5.** The computation below is valid for every \(M\ge0\), including \(M=1\) used for sharpness in Theorem2.1. The unshifted triangle has zero mean by integrating its two linear pieces. Its first derivative has jump \(+2\) at each minimum and \(-2\) at each maximum. Two integrations by parts on those pieces therefore give, for its period-\(2\pi/\lambda\) coefficient \(d_k\), \(k\ne0\),
\[
 \begin{gathered}
 -(k\lambda)^2d_k=\frac\lambda\pi(1-(-1)^k),\\
 d_k=-\frac{1-(-1)^k}{\pi\lambda k^2}.
 \end{gathered}
\]
Thus even coefficients vanish and nonzero odd coefficients equal \(-2/(\pi\lambda k^2)\). The absolute Fourier series is therefore
\[
u(x)=-\frac{4M}{\pi\lambda}
\sum_{\substack{k\ge1\\ k\ {\rm odd}}}
 \frac{\cos(k\lambda(x-s))}{k^2}.
\]
[Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1, identifies this uniformly convergent series everywhere with the continuous triangle. Its bounded tail tends to zero strongly in \(\mathcal S'\): pairing it with a Schwartz test is bounded by its supremum times the test's \(L^1\) norm, uniformly on a bounded test set. The continuous Fourier transform and the supplied plane-wave normalization therefore give
\[
Fu=-\frac{4M}{\lambda}
\sum_{\substack{k\in\mathbb Z\\ k\ {\rm odd}}}
 \frac{e^{-ik\lambda s}}{k^2}\delta_{k\lambda}.
\]
This is a locally finite tempered atom series, and includes no zero term. The triangle derivative is \(+M\) or \(-M\) almost everywhere, so its norm is \(M\). Its supremum is \(M\pi/(2\lambda)\), attaining the sharp non-strict Bohr inequality while being strictly below \(\pi/(2\lambda)\) for \(M<1\). If \(M=0\), the transform and function are both zero; the empty spectrum still avoids the gap.

**Solution 6.** A constant \(c>\pi/(2\lambda)\) has derivative zero but violates the asserted uniform value bound; \(Fc=2\pi c\delta_0\). The affine function \(u(x)=a x+b\), \(0<|a|<1\), has bounded derivative of norm \(|a|\) and is unbounded. Its whole transform is
\[
Fu=2\pi i a\delta_0'+2\pi b\delta_0.
\]
Both spectra meet zero, so neither has the required gap. These are tempered distributions; no Fourier-integrability assumption was used.

**Solution 7.** On the indicated period the two harmonic indices are \(N+1\) and \(2N\), both outside \(|k|<N\), also when \(N=1\). The low coefficients, including the mean, vanish. Its weak derivative norm is at most
\[
L=\mu\bigl((N+1)|A|/N+2|B|\bigr)<1.
\]
Theorem 2.1's full periodic sign-change proof therefore applies to every translate of the triangle: the difference is negative at each minimum, positive at each maximum, and strictly monotone on each of its \(2N\) cells. It has exactly one crossing in every cell, hence exactly \(2N\) per full period. Theorem 2.1's periodic norm bound gives
\(\|v\|_\infty\le\pi L/(2\mu)\). This uses an upper derivative bound; it does not assert that the two derivative summands attain their maxima simultaneously.

**Solution 8.** The triangle \(h_\lambda\) has the required gap and derivative norm one. Since \(F\psi=\chi\), the complete Schwartz multiplier theorem gives \(h_\lambda*\psi=0\), while \(\int\psi=1\). Put \(a=\pi/\lambda\) and evaluate at its minimum \(x=0\):
\[
\frac a2=|h_\lambda(0)|
\le\int|\psi(t)|\,|h_\lambda(0)-h_\lambda(-t)|dt.
\]
The difference has modulus at most \(|t|\) by the Lipschitz bound, and at most \(a\) by the triangle's full range. For \(|t|>a\) this is strictly below \(|t|\). The Schwartz \(\psi\) extends to an entire function by [*Sharp bounds for compact spectra*](sharp-bounds-for-compact-spectra.md), Theorem 3.1, and is not zero because its integral is one. It cannot vanish on both exterior real intervals: the one-variable identity theorem would then make it zero everywhere. Thus \(|\psi|>0\) on an open interval with \(|t|>a\). The weighted difference is strictly positive on that interval and integrable everywhere. Hence the last integral is strictly smaller than \(\int |t\psi(t)|dt\), proving the claimed strict inequality. Theorem 2.1's preliminary bound uses precisely this larger weighted moment; the periodic comparison was necessary to obtain the sharp constant.

## References

- [Sharp bounds for compact spectra](sharp-bounds-for-compact-spectra.md), Lemma0.1 and Theorems2.1–3.1: full maximum principle, derivative contraction and entire extension. [Resolvent sampling and positive periodization](resolvent-sampling-and-positive-periodization.md), Theorem4.1 and Solution8: complete positive approximation, whole Fourier support and finite-degree conclusion.
- [Periodic Green functions and boundary spectra](periodic-green-functions-and-boundary-spectra.md), Theorem4.1's proof of(4.2): weak primitives and continuous representatives. [Bernoulli series and Poisson summation](bernoulli-series-and-poisson-summation.md), Lemma0.1: continuous periodic Fourier uniqueness. [Tempered growth and spectral cutoffs](tempered-growth-and-spectral-cutoffs.md), Lemma2.1 and Theorem3.1: whole Schwartz convolution and spectral cutoffs. Supplied scalar, Fourier and integration foundations retain their stated licences.
- A. Eremenko and D. Novikov, [*Oscillation of Fourier Integrals with a spectral gap*](https://arxiv.org/abs/math/0301060), arXiv:math/0301060v1 (2003), Introduction, page1: the finite periodic sign-change/orthogonality mechanism. The finite product and every step used here are proved above. The paper's broader nonperiodic sign-change-density theorem is a different result and is not used as a premise.
- Isaac Pesenson, [*Bernstein-Nikolskii inequalities and Riesz interpolation formula on compact homogeneous manifolds*](https://arxiv.org/abs/1403.4561), arXiv:1403.4561v2 (2014), Introduction, formulas(1.1)–(1.4), for the classical derivative-bound setting. The exact phase contraction used here has its full earlier programme proof in U059.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises7.2.10–7.2.11, printed pages389–390, and answers on page414. The complete real and complex comparison proofs, all representative and endpoint arguments, stability estimates and graded problems above are independently expressed.
