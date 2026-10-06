# Positive kernels and spectral measures

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

A continuous positive convolution kernel is the Fourier transform of a finite positive measure. A positive distributional kernel can have an infinite spectral mass, but some polynomial weight makes that mass finite. We prove both statements, including the automatic temperedness of a distribution that initially has only local bounds.

Pairings are complex bilinear, with
\[
Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,\qquad
\widetilde f(x)=f(-x),\qquad
Gf(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}f(\xi)\,d\xi.
\]
Reflection here includes no conjugation. Write
\(\langle x\rangle=(1+|x|^2)^{1/2}\) and
\(P_N(f)=\max_{|\alpha|\le N}\sup_x\langle x\rangle^N|\partial^\alpha f(x)|\).
The [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves its seminorms, cutoff density, both inverse identities, Gaussian normalization and all transposed identities. [U008](order-positivity-and-limits.md), Proposition 1.2, Theorem 4.1 and Corollary 3.3, supplies finite-regularity extension, positive-distribution representation and measure uniqueness. Its [positive-measure foundation](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), Theorem M, includes the complete Radon construction. [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorems 1.1–2.1 and 3.1, supplies compact smoothing and proper convolution associativity. [U041](separated-frequencies-and-distributional-order.md), Theorem 3.1, supplies the separated-series order bound used in Solution 3.

The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), Sections 15.0–15.1 and 15.3–15.4, proves monotone and dominated convergence, product integration, affine substitution and mollification. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), Sections 12.4–12.9, 13.1–13.5 and 13.7–13.10, supplies compactness, calculus, exponentials and cutoffs. All additional representation arguments are proved below.

## From finite Gram matrices to a finite measure

For continuous \(K:\mathbb R^n\to\mathbb C\), define, initially for \(\phi\in\mathcal D\),
\[
Q_K(\phi)=\int(K*\phi)(x)\overline{\phi(x)}\,dx
=\iint K(x-y)\phi(y)\overline{\phi(x)}\,dy\,dx.
\]
This is a compact integral even if \(K\) is unbounded.
Changing variables \(z=x-y\) also writes it as \(K(\widetilde\phi*\overline\phi)\), where \(K\) acts by integration: the test at \(z\) is \(\int\phi(y)\overline{\phi(y+z)}\,dy\).

**Theorem 1.1 (Bochner representation).** The following three conditions are equivalent:

1. \(Q_K(\phi)\) is real and nonnegative for every compact smooth \(\phi\).
2. For every finite set of points and complex coefficients,
\(\sum_{j,k}K(x_j-x_k)t_j\overline{t_k}\ge0\).
3. \(K=F\mu\) for a unique positive finite Radon measure.

In the third condition \(\mu(\mathbb R^n)=K(0)\). There is no initial boundedness assumption on \(K\).

**Proof: compact tests and finite matrices.** Choose a real nonnegative compact smooth \(\rho\) of integral one and set
\[
\phi_\varepsilon(x)=\sum_j\overline{t_j}
\varepsilon^{-n}\rho((x-x_j)/\varepsilon).
\]
For small \(\varepsilon\), every term in the double integral averages \(K\) on a fixed compact neighborhood of one difference \(x_k-x_j\). Uniform continuity there makes the averages tend to \(K(x_k-x_j)\). Thus
\[
Q_K(\phi_\varepsilon)\longrightarrow
\sum_{j,k}\overline{t_j}t_kK(x_k-x_j)
=\sum_{j,k}K(x_j-x_k)t_j\overline{t_k}.
\]
This proves condition 2 from condition 1 with the exact coefficient orientation.

Condition 2 gives \(d=K(0)\ge0\) by a single point. For two points, evaluation at coefficient pairs \((1,1)\) and \((1,i)\) shows \(K(-x)=\overline{K(x)}\): if the two off-diagonal entries are \(z,w\), reality says \(\operatorname{Im}(z+w)=0\) and \(\operatorname{Re}(w-z)=0\). The form on \((s,1)\) is therefore
\[
d(|s|^2+1)+2\operatorname{Re}(sK(x)).
\]
If \(d>0\), take \(s=-\overline{K(x)}/d\), obtaining \(|K(x)|\le d\). If \(d=0\), take \(s=-\overline{K(x)}\), forcing \(K(x)=0\). Hence in every case \(K\) is bounded by \(K(0)\).

Conversely, for a fixed compact support of \(\phi\), divide a bounding cube into finitely many measurable grid cells \(C_j\) of small diameter and choose \(x_j\in C_j\). Put \(c_j=\int_{C_j}\phi\). Replacing \(K(x-y)\) by \(K(x_j-x_k)\) on \(C_j\times C_k\) changes the integral by at most
\[
\sup_{j,k;\ x\in C_j,y\in C_k}
|K(x-y)-K(x_j-x_k)|\,\|\phi\|_1^2.
\]
Uniform continuity on the compact difference cube makes this tend to zero with the grid size. The replaced integral is
\(\sum_{j,k}K(x_j-x_k)c_k\overline{c_j}\), the nonnegative Gram form for \(t_j=\overline{c_j}\). This proves condition 1. The finite-partition argument also appears in the freely accessible proof of [Bell, Theorem 3](https://jordanbell.info/LaTeX/mathematics/bochnertheorem/bochnertheorem.pdf); the present calculation specifies all conjugations.

To construct the spectral measure, we first prove two local tools.

**Lemma 1.2 (positive tempered measures).** If a tempered functional \(v\) is nonnegative on nonnegative compact smooth tests, it is integration against a unique positive Radon measure \(\mu\). For some integer \(L\ge0\),
\(\int\langle\xi\rangle^{-L}\,d\mu<\infty\), and the integration formula holds for every Schwartz test.

**Proof.** U008, Theorem 4.1, with its supplied Theorem M, gives the measure on compact tests. By the finite-seminorm characterization of \(\mathcal S'\), fix \(C,N\) such that \(|v(\eta)|\le CP_N(\eta)\). Take a smooth cutoff \(0\le\chi\le1\), one on the unit ball and supported in a fixed larger ball, and let \(\chi_R(\xi)=\chi(\xi/R)\), \(R\ge1\). Differentiation gives
\(\partial^\alpha\chi_R=R^{-|\alpha|}(\partial^\alpha\chi)(\xi/R)\), so \(P_N(\chi_R)\le C_\chi R^N\). Positivity gives
\[
\mu(B_R)\le\int\chi_R\,d\mu=v(\chi_R)\le C'R^N.
\]
With \(L=N+1\), the shell \(2^j\le|\xi|<2^{j+1}\) contributes at most \(C''2^{-j}\) to \(\int\langle\xi\rangle^{-L}\,d\mu\). Summing the geometric series and adding the finite unit-ball mass proves the weighted bound.

For \(\eta\in\mathcal S\),
\(\int|\eta|\,d\mu\le P_L(\eta)\int\langle\xi\rangle^{-L}\,d\mu\).
The cutoff sequence \(\chi_R\eta\) converges to \(\eta\) in \(\mathcal S\) by F1 and is bounded in absolute value by \(|\eta|\). Dominated convergence and continuity of \(v\) therefore identify its pairing with the full integral. U008's measure uniqueness completes the claim. \(\square\)

**Lemma 1.3 (a tempered positive convolution form).** Suppose \(K\in\mathcal S'\) and \(K(\widetilde\phi*\overline\phi)\ge0\) for every \(\phi\in\mathcal D\). Then \(GK\) is a positive tempered measure as in Lemma 1.2.

**Proof: extend the quadratic form.** For Schwartz \(f,g\),
\[
P_N(f*g)\le 2^N\pi^n P_N(f)P_{N+2n}(g).
\]
Indeed \(\langle x\rangle\le2\langle x-y\rangle\langle y\rangle\), and after differentiating \(f\) the weighted integrand is bounded by
\(2^NP_N(f)P_{N+2n}(g)\langle y\rangle^{-2n}\).
Its integral is at most \(\pi^n\), since
\[
\langle y\rangle^{-2n}
\le\prod_{\nu=1}^n(1+y_\nu^2)^{-1}
\quad\text{and}\quad
\int_{\mathbb R}(1+t^2)^{-1}\,dt=\pi.
\]
Dominated difference quotients give the convolution derivatives used here. This bound, bilinearity, reflection and conjugation show that \(\phi_j\to\phi\) in \(\mathcal S\) implies convergence of their autocorrelations in \(\mathcal S\). Take compact-cutoff approximants to obtain positivity for every \(\phi\in\mathcal S\).

**Proof: from squares to all positive tests.** Set \(v=GK\), so \(K=Fv\). Absolute Fubini gives
\[
F(\widetilde\phi*\overline\phi)(\xi)
=F\phi(-\xi)\overline{F\phi(-\xi)}.
\]
For any \(h\in\mathcal S\), choose \(\phi=G(\widetilde h)\); then \(F\phi(-\xi)=h(\xi)\). It follows that \(v(|h|^2)\ge0\).

Given \(0\le\eta\in\mathcal D\), choose \(0\le\chi\in\mathcal D\) equal to one near \(\operatorname{supp}\eta\). For \(\epsilon>0\), \(h_\epsilon=\chi\sqrt{\eta+\epsilon}\) is compact smooth; the square root is smooth on the positive real axis by scalar calculus. Its square is exactly \(\eta+\epsilon\chi^2\). Thus \(v(\eta)+\epsilon v(\chi^2)\ge0\). Letting \(\epsilon\downarrow0\) gives a real nonnegative \(v(\eta)\). Lemma 1.2 applies. \(\square\)

**Proof of Theorem 1.1: representation and total mass.** Under conditions 1–2, the bound \(|K|\le K(0)\) makes its regular distribution tempered: F1's \(L^1\) bound controls \(|\int K\eta|\) by a Schwartz seminorm. Lemma 1.3 gives a positive weighted measure \(\mu=GK\) and \(K=F\mu\).

For \(t>0\), F3's exact Gaussian transform yields
\[
\begin{aligned}
\int e^{-t|\xi|^2}\,d\mu(\xi)
&=\mu(e^{-t|\cdot|^2})=K(G(e^{-t|\cdot|^2}))\\
&=\int K(x)(4\pi t)^{-n/2}e^{-|x|^2/(4t)}\,dx\\
&=\pi^{-n/2}\int K(2\sqrt t\,y)e^{-|y|^2}\,dy.
\end{aligned}
\]
The right side tends to \(K(0)\) by boundedness, continuity at zero and dominated convergence; the Gaussian mass is \(\pi^{n/2}\). Along \(t\downarrow0\), monotone convergence on the left gives \(\mu(\mathbb R^n)=K(0)<\infty\).

The finite measure's ordinary Fourier integral is continuous by dominated convergence, and Fubini identifies its distribution with \(F\mu=K\). Two continuous functions with the same distribution agree pointwise: if their difference is nonzero at a point, rotate its value to have positive real part and use a nonnegative bump on a neighborhood where that real part stays positive. Their difference would then have a nonzero test pairing. This proves the required pointwise equality.

Conversely, a finite positive measure gives a continuous \(F\mu\), and finite expansion under its integral gives
\[
\sum_{j,k}F\mu(x_j-x_k)t_j\overline{t_k}
=\int\left|\sum_jt_je^{-ix_j\cdot\xi}\right|^2d\mu(\xi)\ge0.
\]
Its value at zero is its mass. If two finite positive measures represent \(K\), they are tempered, Fourier inversion identifies their distributions, and measure uniqueness identifies the measures. The zero case is included throughout. \(\square\)

A single positive atom gives \(K(x)=c e^{-ix\cdot b}\), \(c\ge0\). Such a kernel can oscillate; its positivity is positivity of the tested form.

## Local positivity forces a polynomial spectral bound

For \(K\in\mathcal D'(\mathbb R^n)\), define
\[
Q_K(\phi)=K(\widetilde\phi*\overline\phi),\qquad\phi\in\mathcal D.
\tag{2.1}
\]
For continuous \(K\), substitution \(z=x-y\) in the compact double integral identifies this with the preceding quadratic form.

**Theorem 2.1 (Bochner–Schwartz representation).** Such a \(K\) satisfies \(Q_K(\phi)\ge0\) for all compact smooth \(\phi\) if and only if
\[
K=F\mu,\qquad \mu\ge0,\qquad
\int\langle\xi\rangle^{-M}\,d\mu(\xi)<\infty
\]
for a positive Radon measure and some finite \(M\ge0\). The measure is unique. In particular, positivity implies temperedness without any initial growth hypothesis.

**Proof: positive compact smoothing.** Choose a real nonnegative \(\rho\in\mathcal D(B(0,1))\) of integral one. For \(0<\varepsilon\le1/2\), put
\[
\rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon),\qquad
q_\varepsilon=\rho_\varepsilon*\widetilde\rho_\varepsilon,\qquad
K_\varepsilon=K*q_\varepsilon.
\]
The function \(q_\varepsilon\) is real, nonnegative, even, of mass one, and supported in \(B(0,2\varepsilon)\). Evenness follows by changing the variable in its autocorrelation; mass follows from Fubini. U021's compact smoothing proof makes \(K_\varepsilon\) smooth. Explicitly, on each compact set of \(x\)'s, the tests \(q_\varepsilon(x-\cdot)\) have common compact support and all their difference quotients converge in the fixed-support test topology.

The compact-factor test-pairing identity and associativity give
\[
\begin{aligned}
Q_{K_\varepsilon}(\phi)
&=K(q_\varepsilon*\widetilde\phi*\overline\phi)\\
&=Q_K(\rho_\varepsilon*\phi)\ge0.
\end{aligned}
\tag{2.2}
\]
Here \(\widetilde{\rho_\varepsilon*\phi}=\widetilde\rho_\varepsilon*\widetilde\phi\) and \(\overline{\rho_\varepsilon*\phi}=\rho_\varepsilon*\overline\phi\). All test factors are compact. The needed associativity is U021, **Theorem 3.1**, whose nonempty compact envelopes may be chosen even for a zero factor. Theorem 1.1 gives \(K_\varepsilon=F\mu_\varepsilon\) with \(\mu_\varepsilon\) positive and finite. Their unweighted masses may diverge.

**Proof: one support and one finite order.** Fix \(H=[-3,3]^n\) before choosing any other parameter. Local continuity gives integers \(N\ge0\) and \(C\) with
\[
|K(\theta)|\le C
\max_{|\alpha|\le N}\|\partial^\alpha\theta\|_\infty,
\qquad \theta\in\mathcal D_H.
\tag{2.3}
\]
U008, Proposition 1.2, extends this same bound to compact \(C^N\) tests supported inside the interior of \(H\), by smooth mollification with common support. We now construct such a test whose Fourier transform has a positive polynomial lower bound.

Let \(a(t)=e^{-t}1_{[0,1]}(t)\). For \(m\ge2\),
\[
a^{*m}(t)=\frac{e^{-t}}{(m-1)!}
\sum_{j=0}^m(-1)^j\binom mj(t-j)_+^{m-1}.
\tag{2.4}
\]
For the initial step, \(a\) is almost everywhere \(e^{-t}\) times the difference of the indicators of \([0,\infty)\) and \([1,\infty)\). Convolution with \(a\) integrates each corresponding truncated power over an interval of length one. More generally,
\[
\int_0^1(t-j-s)_+^{m-1}\,ds
=\frac{(t-j)_+^m-(t-j-1)_+^m}{m}.
\]
Multiplying the exponential factors gives \(e^{-t}\); Pascal's identity then proves (2.4) inductively, starting at \(m=2\). The original convolutions have support in \([0,m]\). Each truncated power in (2.4) is \(C^{m-2}\): derivatives through that order are continuous and vanish at its threshold. Thus the same formula proves this regularity at every junction and endpoint.

Take \(m=N+2\), and define
\[
b_m(t)=m\,a^{*m}(mt),\qquad
v(x)=\prod_{\nu=1}^n b_m(x_\nu),\qquad
\psi=v*\widetilde v.
\tag{2.5}
\]
Then \(b_m\in C_c^N([0,1])\), \(v\in C_c^N([0,1]^n)\) and \(\psi\in C_c^N([-1,1]^n)\). Finite product differentiation and differentiation under the compact convolution integral prove these statements. The autocorrelation \(\psi\) is real and even. The support remains fixed as \(m\) grows; the earlier choice of \(N\) is not circular.

The scalar exponential primitive gives
\[
Fa(s)=\frac{1-e^{-1}e^{-is}}{1+is},\qquad
Fb_m(s)=\left(\frac{1-e^{-1}e^{-is/m}}{1+is/m}\right)^m.
\]
The second identity uses ordinary \(L^1\) convolution Fubini and affine substitution. The triangle inequality gives \(|1-e^{-1}e^{-iu}|\ge1-e^{-1}\). Therefore, using Fubini again for the product and autocorrelation,
\[
\begin{aligned}
F\psi(\xi)=|Fv(\xi)|^2
&\ge(1-e^{-1})^{2mn}\prod_{\nu=1}^n(1+\xi_\nu^2)^{-m}\\
&\ge c\langle\xi\rangle^{-2mn},
\qquad c=(1-e^{-1})^{2mn}>0.
\end{aligned}
\tag{2.6}
\]
Indeed \(1+s^2/m^2\le1+s^2\) and
\(\prod_\nu(1+\xi_\nu^2)\le(1+|\xi|^2)^n\).

**Proof: the uniform weighted bound.** Finite-measure Fubini first gives
\[
\int F\psi(\xi)\,d\mu_\varepsilon(\xi)
=\int K_\varepsilon(x)\psi(x)\,dx
=K(q_\varepsilon*\psi).
\tag{2.7}
\]
For the second equality, approximate \(\psi\) in \(C^N\) by smooth functions supported in \([-3/2,3/2]^n\), using U008. Pairing them with \(K_\varepsilon\), bounded on that cube, converges by uniform approximation. On the other side, convolution with the fixed \(q_\varepsilon\) preserves the \(C^N\) convergence, and the resulting supports lie in \([-5/2,5/2]^n\), inside \(H\). Thus (2.3) passes the smooth-test identity to \(\psi\). Evenness of \(q_\varepsilon\) accounts for the test reflection. The first equality is absolutely justified by the finite mass of \(\mu_\varepsilon\) and the integrability of \(\psi\).

For \(|\alpha|\le N\),
\[
\|\partial^\alpha(q_\varepsilon*\psi)\|_\infty
\le\|q_\varepsilon\|_1\|\partial^\alpha\psi\|_\infty
=\|\partial^\alpha\psi\|_\infty.
\]
Combining (2.3), (2.6) and (2.7) gives a constant \(A\), independent of \(\varepsilon\), with
\[
\sup_{0<\varepsilon\le1/2}
\int\langle\xi\rangle^{-M}\,d\mu_\varepsilon(\xi)
\le A<\infty,\qquad M=2mn.
\tag{2.8}
\]
Only compact tests have been applied to the original \(K\).

**Proof: construct the tempered extension directly.** For \(\theta\in\mathcal D\),
\[
|K_\varepsilon(\theta)|
\le A\sup_\xi\langle\xi\rangle^M|F\theta(\xi)|
\le B P_L(\theta)
\]
for one finite \(L\) and \(B\), by F2's Fourier seminorm estimates. Meanwhile
\(K_\varepsilon(\theta)=K(q_\varepsilon*\theta)\to K(\theta)\).
Every derivative of the compact convolution tends uniformly to the corresponding derivative of \(\theta\): its difference is an average of translation differences of that derivative over \(|y|\le2\varepsilon\). Uniform continuity gives convergence, and all supports stay in one compact set.

Consequently \(|K(\theta)|\le BP_L(\theta)\) on \(\mathcal D\). For \(\eta\in\mathcal S\), define its extension as the limit of \(K(\chi_R\eta)\), where F1 supplies \(\chi_R\eta\to\eta\) in \(\mathcal S\). The estimate makes these complex numbers Cauchy, makes the result independent of approximants, and passes the same bound to the limit. Density proves uniqueness. Each \(K_\varepsilon\) satisfies the same global bound. For any fixed cutoff radius \(R\),
\[
|(K_\varepsilon-K)(\eta)|
\le2BP_L(\eta-\chi_R\eta)
  +|(K_\varepsilon-K)(\chi_R\eta)|.
\]
First make the first term small with \(R\), then the second with \(\varepsilon\). Thus \(K_\varepsilon\to K\) on every Schwartz test.

Lemma 1.3 applies to this tempered extension. It gives the positive Radon measure \(\mu=GK\), with \(K=F\mu\), and now for every \(\theta\in\mathcal S\),
\[
K_\varepsilon(\theta)
=\int F\theta\,d\mu_\varepsilon
\longrightarrow K(\theta)
=\int F\theta\,d\mu.
\tag{2.9}
\]
In particular \(\mu_\varepsilon(\eta)\to\mu(\eta)\) for each \(\eta\in\mathcal S\), by applying the preceding convergence to \(G\eta\). The weight in (2.8) can be retained exactly: for \(0\le\chi_R\le1\) equal to one on the radius-\(R\) ball,
\[
\int \chi_R(\xi)\langle\xi\rangle^{-M}\,d\mu
=\lim_{\varepsilon\downarrow0}
\int\chi_R(\xi)\langle\xi\rangle^{-M}\,d\mu_\varepsilon
\le A.
\]
Hence the integral over each radius-\(R\) ball is at most \(A\). Continuity from below of a positive measure gives the full weighted bound at the same \(M\). This proves both the representation and automatic temperedness.

**Proof: converse and uniqueness.** If \(\mu\ge0\) has a finite indicated weighted integral, then
\[
\left|\int\eta\,d\mu\right|
\le\left(\int\langle\xi\rangle^{-M}\,d\mu\right)
\sup_\xi\langle\xi\rangle^M|\eta(\xi)|
\]
makes it tempered; increase \(M\) to an integer if needed. Fourier transposition and the autocorrelation identity in Lemma 1.3 give
\[
Q_{F\mu}(\phi)
=\int|F\phi(-\xi)|^2\,d\mu(\xi)\ge0.
\]
The integrand has all polynomial decay, so it is integrable against this measure. If two such measures represent \(K\) on compact tests, density identifies the tempered transforms, inversion identifies their distributions, and U008 identifies the measures. Finally
\(\langle\xi\rangle\le1+|\xi|\le\sqrt2\langle\xi\rangle\), so either usual polynomial weight gives the same finiteness condition for a fixed exponent. \(\square\)

The distinction between mass and weighted mass is real: \(\delta_0\) is a positive kernel, with spectral measure \((2\pi)^{-n}d\xi\), of infinite total mass. In dimension one its weighted mass is finite exactly for exponents greater than one.

## Exercises

**Exercise 1 (foundation).** Determine when \(ce^{-ix\cdot b}\), \(b\in\mathbb R^n\), is positive, and find its spectral measure and mass.

**Exercise 2 (intermediate).** For \(a>0\) and real \(b\), find the positive spectral measure of \(e^{-a|x|}e^{-ibx}\). Prove its mass is one and compute its convolution quadratic form.

**Exercise 3 (advanced).** For \(\mu=\sum_{j\in\mathbb Z}(1+j^2)\delta_j\), determine every real \(M\) giving finite \(\int\langle\xi\rangle^{-M}\,d\mu\). Construct \(F\mu\) as a strongly convergent tempered exponential series, prove local order at most three and exclude a continuous representative.

**Exercise 4 (intermediate).** Find the spectral measure of \(\delta_0\) on the line and prove positivity directly. Give an explicit compact smooth family on which \(i\delta'_0\) has negative quadratic form.

**Exercise 5 (intermediate).** Prove that \(-\Delta K\) is positive whenever \(K\) is a positive convolution kernel. Find its spectral measure, a valid weight, and the quadratic form of \(-\delta''_0\).

**Exercise 6 (intermediate).** Prove that the pointwise product of two continuous positive kernels is positive. Determine its spectral measure and mass, including the zero cases.

**Exercise 7 (foundation).** Classify polynomial positive kernels. Give a negative two-point Gram form for \(K(x)=-x^2\).

**Exercise 8 (advanced).** For \(\mu_R=(2\pi)^{-1}1_{[-R,R]}d\xi\), compute \(K_R=F\mu_R\) and \(K_R(0)\). Prove weak tempered convergence to \(\delta_0\), and determine exactly which real weights give uniform weighted masses.

## Solutions

**Solution 1.** The bound at zero requires \(c=K(0)\) to be real and nonnegative. Conversely \(c\delta_b\) is positive for exactly such \(c\), and its Fourier transform is the required function. Its mass is \(c\), including zero. The finite form is \(c|\sum_jt_je^{-ix_j\cdot b}|^2\); uniqueness follows from Theorem 1.1.

**Solution 2.** Put \(f(x)=e^{-a|x|}\). Direct integration over the two half-lines gives
\[
Ff(\xi)=\frac1{a+i\xi}+\frac1{a-i\xi}
=\frac{2a}{a^2+\xi^2}.
\]
Both \(f\) and this density are integrable. The measure
\(\lambda(d\xi)=a[\pi(a^2+\xi^2)]^{-1}d\xi\) has mass
\(\pi^{-1}\int(1+t^2)^{-1}dt=1\) by \(\xi=at\) and the proved arctangent primitive. F5 agrees with the ordinary \(L^1\) Fourier transform, so
\(F\lambda=(2\pi)^{-1}F^2f=\widetilde f=f\) as distributions. Both sides are continuous, hence equal pointwise by the bump argument in Theorem 1.1. Translation of \(\lambda\) by \(b\) gives
\[
d\mu(\xi)=\frac{a\,d\xi}{\pi(a^2+(\xi-b)^2)},\qquad
F\mu(x)=e^{-ibx}e^{-a|x|}.
\]
The translation preserves mass and positivity. The complete quadratic form is
\[
Q_K(\phi)=\int_{\mathbb R}
\frac{a\,|F\phi(-\xi)|^2}{\pi(a^2+(\xi-b)^2)}\,d\xi\ge0.
\]
The reflected Fourier argument follows from the established bilinear convention, and rapid decrease makes the integral finite.

**Solution 3.** The weighted mass is
\(\sum_{j\in\mathbb Z}(1+j^2)^{1-M/2}\).
For \(|j|\ge1\), comparison \(j^2\le1+j^2\le2j^2\), with the inequalities reversed when raising to a negative power, makes these terms comparable to \(|j|^{2-M}\). To check the convergence criterion without an unproved series test, group the positive indices into \(2^r\le j<2^{r+1}\). Their sum is bounded above and below by fixed positive multiples of \(2^{r(3-M)}\). These block sums are summable exactly when \(M>3\); at \(M=3\) each is bounded below by a positive constant.

Apply U041, Theorem 3.1, to frequencies \(-j\), coefficients \(1+j^2\), and \(m=3\). They are separated by one, and
\[
\sum_j |1+j^2|^2\langle j\rangle^{-6}
=\sum_j(1+j^2)^{-1}<\infty.
\]
It follows that \(K=\sum_j(1+j^2)e^{-ijx}\) converges strongly in \(\mathcal S'\), independently of enumeration, and has local order at most three. On a test,
\[
K(\theta)=\sum_j(1+j^2)F\theta(j)=F\mu(\theta),
\qquad
Q_K(\phi)=\sum_j(1+j^2)|F\phi(-j)|^2\ge0.
\]
Every displayed scalar sum converges by rapid decrease or the cited proved square-sum estimate. A continuous representative would, by Theorem 1.1, have a finite positive spectral measure. Theorem 2.1 would identify it with \(\mu\), whose mass is infinite, a contradiction. The upper order bound three is not asserted to be sharp.

**Solution 4.** Since \(\delta_0*\phi=\phi\), \(Q_{\delta_0}(\phi)=\int|\phi|^2\ge0\). The identity \(F1=2\pi\delta_0\) gives the spectral measure \((2\pi)^{-1}d\xi\), with finite weighted mass exactly for \(M>1\), by comparison on dyadic intervals. For any nonzero real \(\rho\in\mathcal D\), put \(\phi_b(x)=e^{ibx}\rho(x)\), \(b>0\). The compact convolution derivative identity gives
\[
Q_{i\delta'_0}(\phi_b)
=i\int\phi_b'\overline{\phi_b}
=-b\int\rho^2+i\int\rho'\rho
=-b\int\rho^2<0.
\]
The last derivative integral is \(\frac12\int(\rho^2)'=0\) by compact support. Thus convolution-form positivity differs from positivity on nonnegative scalar tests.

**Solution 5.** If \(K=F\mu\), transposed differentiation gives
\(-\Delta K=F(|\xi|^2\mu)\). This measure is positive and obeys
\[
\int\langle\xi\rangle^{-M-2}|\xi|^2\,d\mu
\le\int\langle\xi\rangle^{-M}\,d\mu<\infty.
\]
Theorem 2.1 proves positivity. For \(K=\delta_0\) on the line, the new measure is \(\xi^2d\xi/(2\pi)\). Direct integration by parts also gives
\[
Q_{-\delta''_0}(\phi)=-\int\phi''\overline\phi
=\int|\phi'|^2.
\]
There are no boundary terms because \(\phi\) is compactly supported.

**Solution 6.** Write \(K_r=F\mu_r\) for finite positive measures. On real compact continuous \(h\), define
\[
I(h)=\iint h(\xi+\eta)\,d\mu_1(\xi)d\mu_2(\eta).
\]
This is positive and linear, with bound
\(|I(h)|\le\mu_1(\mathbb R^n)\mu_2(\mathbb R^n)\|h\|_\infty\).
The supplied Theorem M gives a positive Radon measure \(\lambda\) representing \(I\), of total mass at most that product. Compact cutoffs increasing to one, as constructed in M3, and monotone convergence in both measures give equality of the masses. They also identify \(\lambda\) with the addition pushforward of \(\mu_1\otimes\mu_2\): first test increasing cutoffs for each open set, then use the finite-measure generating-class uniqueness proved in the integration foundation. Thus \(\lambda=\mu_1*\mu_2\).

Apply the integral identity to a compact cutoff times \(h(s)=e^{-ix\cdot s}\). Bounded dominated convergence, using finite masses, removes the cutoff and gives
\[
F\lambda(x)=\iint e^{-ix\cdot(\xi+\eta)}
\,d\mu_1(\xi)d\mu_2(\eta)=K_1(x)K_2(x).
\]
Theorem 1.1 proves positivity. The mass is
\(\mu_1(\mathbb R^n)\mu_2(\mathbb R^n)=K_1(0)K_2(0)\).
If either kernel is zero, its measure is zero by that mass identity, so \(\lambda\) and the product kernel are zero as well.

**Solution 7.** Theorem 1.1 bounds any positive continuous kernel by \(K(0)\). A nonconstant complex polynomial cannot be bounded on \(\mathbb R^n\). To verify this, its top homogeneous part \(p_d\), \(d>0\), is nonzero at some real \(v\). A polynomial vanishing at all real points has all coefficients zero: in one variable, division by \(t-r\) at each distinct root proves by degree induction that a nonzero degree-\(d\) polynomial has at most \(d\) roots; in several variables, regard it as a polynomial in the last coordinate and apply this fact to each coefficient, inducting on the number of coordinates. Thus such \(v\) exists.

Now \(t^{-d}p(tv)\to p_d(v)\ne0\) as positive \(t\to\infty\), so \(|p(tv)|\to\infty\). The only positive polynomial kernels are therefore real nonnegative constants, all supplied by Solution 1. For \(-x^2\), choose points zero and one and both coefficients one. The diagonal entries are zero and each off-diagonal entry is \(-1\), giving the negative Gram sum \(-2\).

**Solution 8.** The elementary exponential integral on \([-R,R]\) gives
\[
K_R(x)=\frac{\sin(Rx)}{\pi x}\quad(x\ne0),\qquad
K_R(0)=\frac R\pi.
\]
The zero value follows either from the original integral or from \(\sin t/t\to1\), proved by the scalar derivative of sine at zero. The finite positive measure gives positivity and the stated mass. For \(\theta\in\mathcal S\), Fubini and F4 give
\[
K_R(\theta)=\frac1{2\pi}\int_{-R}^R F\theta(\xi)\,d\xi
\longrightarrow\frac1{2\pi}\int_{\mathbb R}F\theta(\xi)\,d\xi
=\theta(0).
\]
The limit uses the integrability of \(F\theta\), so this is weak convergence in \(\mathcal S'\). Weighted masses increase to
\((2\pi)^{-1}\int_{\mathbb R}\langle\xi\rangle^{-M}d\xi\).
For \(|\xi|\ge1\), the integrand is comparable to \(|\xi|^{-M}\). Its integrals on \(2^r\le|\xi|<2^{r+1}\) are comparable to \(2^{r(1-M)}\), proving finiteness and uniform boundedness exactly when \(M>1\). The unweighted masses \(R/\pi\) diverge.

## References

- Jordan Bell, [*Gaussian measures and Bochner's theorem*](https://jordanbell.info/LaTeX/mathematics/bochnertheorem/bochnertheorem.pdf), free author notes dated 30 April 2015, Section 3, Theorem 3 and Corollary 4, PDF pages 4–7. These give the finite-matrix and integral-form comparison. The spectral construction, Gaussian mass limit and automatic-temperedness argument needed in this lesson are fully supplied above.
- [U008](order-positivity-and-limits.md), Proposition 1.2, Theorem 4.1 and Corollary 3.3; [positive-measure foundation](../prerequisites/U011-free-foundations/positive-measure-foundations-U008.md), M1–M9 and Theorem M; [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5; [U021](convolution-as-addition-of-supports.md), Theorems 1.1–2.1 and 3.1; and [U041](separated-frequencies-and-distributional-order.md), Theorem 3.1. These exact programme proofs are supplied with this edition and retain their stated component licences.
