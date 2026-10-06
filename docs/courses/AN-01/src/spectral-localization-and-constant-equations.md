# Spectral localization and constant equations

*Reconstructed and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Earlier edition: GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Original exposition: CC0. Supplied foundations retain their stated licences.*

A small Fourier support forces a small derivative. By cutting a bounded function down to a shrinking neighbourhood of one spectral point, translating to an almost maximal value and normalizing its phase, we obtain an actual plane wave limit. The same construction controls every mixed derivative. We then distinguish the zero sets relevant to distributional, tempered, rapidly decreasing and compactly supported solutions of a constant coefficient equation.

All distributional pairings are complex linear. We use
\[
\begin{gathered}
F\phi(\xi)=\int_{\mathbb R^n}e^{-ix\cdot\xi}\phi(x)\,dx,\qquad
D_j=\frac1i\partial_j,\\
G\psi(x)=(2\pi)^{-n}\int_{\mathbb R^n}e^{ix\cdot\xi}\psi(\xi)\,d\xi .
\end{gathered}
\tag{0.1}
\]
The [Schwartz and Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves both inversion identities, all coordinate differentiation identities, compact-cutoff density in \(\mathcal S\), and the Gaussian formula. [U040](tempered-growth-and-spectral-cutoffs.md), Lemma 2.1 and Theorem 3.1, proves the full convolution adapter
\[
u*f(x)=u_y(f(x-y)),\qquad F(u*f)=(Fu)(Ff),
\]
for \(u\in\mathcal S'\), \(f\in\mathcal S\), its smoothness and derivative rules, and the compact spectral cutoff criterion. [U021](convolution-as-addition-of-supports.md), B0–B2 and Theorems 1.1–2.1, supplies compact localization, proper convolution and compact smoothing. [U008](order-positivity-and-limits.md), Proposition 1.2, supplies the distributional seminorm criterion.

The [scalar foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12, 13.1–13.5 and 13.7–13.10, prove compactness, finite differentiation rules, the fundamental theorem of calculus, complex exponentials, their period \(2\pi\) and smooth cutoffs. The [integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4, prove completed Lebesgue measure, Tonelli, absolute Fubini, affine changes of variables, Hölder and Minkowski with their endpoints, and convergence of compact mollifiers in \(L^1\).

Write \(\langle x\rangle=(1+|x|^2)^{1/2}\) and
\[
P_N(\psi)=\max_{|\alpha|\le N}\sup_x
\langle x\rangle^N|\partial^\alpha\psi(x)|.
\]
These are the increasing Schwartz seminorms from U040. A family \(B\subset\mathcal S\) is bounded when \(\sup_{\psi\in B}P_N(\psi)<\infty\) for each \(N\); strong convergence in \(\mathcal S'\) means uniform convergence of pairings on each such family.

## A bandwidth controls every first derivative

**Lemma 1.0 (the convolution estimate used here).** For \(1\le p\le\infty\), \(u\in L^p(\mathbb R^n)\) and \(k\in\mathcal S(\mathbb R^n)\), the convolution is an absolutely convergent integral at every point and
\[
\|u*k\|_p\le\|u\|_p\|k\|_1.
\]

**Proof.** Every Schwartz function belongs to every \(L^q\), \(1\le q\le\infty\). Indeed, for \(a>n\), integration of \(\langle x\rangle^{-a}\) over the unit ball is bounded by its containing cube. The shell \(2^j\le|x|<2^{j+1}\) has volume at most \(2^{n(j+2)}\), and its integrand is at most \(2^{-ja}\). The resulting geometric series converges. A Schwartz seminorm therefore bounds each finite \(L^q\) norm, and the \(L^\infty\) assertion follows from its supremum seminorm.

Hölder applied to \(u(y)k(x-y)\) gives absolute convergence for each \(x\), including both endpoints. Put \(K=\|k\|_1\); if \(K=0\), then \(k=0\) and the conclusion holds. For \(1<p<\infty\), weighted Hölder gives
\[
\begin{aligned}
|u*k(x)|^p
&\le\left(\int |u(x-y)||k(y)|\,dy\right)^p\\
&\le K^{p-1}\int |u(x-y)|^p|k(y)|\,dy .
\end{aligned}
\]
One can apply Hölder first on finite sets and pass monotonically to the full nonnegative integrals; an infinite right side at an exceptional \(x\) does not invalidate the inequality. Tonelli and translation invariance now bound the integral over \(x\) by \(K^p\|u\|_p^p\). For \(p=1\), the integral triangle inequality and Tonelli give the same bound directly. For \(p=\infty\), the pointwise integral is at most \(\|u\|_\infty K\). ∎

**Theorem 1.1 (Bernstein bound).** Suppose \(1\le p\le\infty\), \(\lambda\ge0\), and \(u\in L^p(\mathbb R^n)\) satisfies
\[
\operatorname{supp}Fu\subset\{\xi:|\xi|\le\lambda\}.
\]
Then \(u\) has a smooth representative and, using the Euclidean norm on its gradient,
\[
\|\nabla u\|_p\le C_n\lambda\|u\|_p.
\tag{1.1}
\]
The constant depends only on \(n\), including at both endpoints. At bandwidth zero the representative is constant, and is zero when \(p<\infty\).

**Proof.** First, \(u\) defines a tempered distribution: Hölder bounds \(|u(\psi)|\) by \(\|u\|_p\|\psi\|_{p'}\), and the dyadic estimate in Lemma 1.0 bounds the latter norm by \(C_{n,p}P_{n+1}(\psi)\). For \(p=1\) use \(\|\psi\|_\infty\); for \(p=\infty\) use \(\|\psi\|_1\).

Fix a dimension-dependent \(\eta\in C_c^\infty(\mathbb R^n)\) equal to one on a neighbourhood of the closed unit ball, and set \(f=G\eta\in\mathcal S\). For \(\lambda>0\), put
\[
f_\lambda(x)=\lambda^nf(\lambda x),\qquad
Ff_\lambda(\xi)=\eta(\xi/\lambda).
\]
The transform formula follows by the affine change of variables in its absolutely convergent integral. Since \(1-\eta(\cdot/\lambda)\) vanishes near \(\operatorname{supp}Fu\), its product with \(Fu\) is zero on compact tests by support localization and then on Schwartz tests by compact-cutoff density. Fourier inversion and the U040 adapter give
\[
u=u*f_\lambda,\qquad \partial_j u=u*\partial_j f_\lambda.
\]
The adapter gives a smooth function. Its defining pairing is precisely the ordinary absolutely convergent integral of Lemma 1.0; no Fourier integral of \(u\) is assumed. It represents the original \(u\) almost everywhere: their difference \(g\) is locally integrable and zero on compact tests. For a compact smooth cutoff \(\chi\), the function \(\chi g\) is in \(L^1\) and zero on compact tests. Each of its convolutions with a compact smooth mollifier is zero, by the defining test pairing. Section 15.4 of the integration foundations proves that these convolutions tend to \(\chi g\) in \(L^1\), so \(\chi g=0\) almost everywhere. Choose cutoffs equal to one on successively larger balls to conclude \(g=0\) almost everywhere. Thus this smooth function is indeed an \(L^p\) representative with the original norm. Lemma 1.0 now gives
\[
\begin{gathered}
\|\partial_j u\|_p\le\|u\|_p\|\partial_j f_\lambda\|_1,\\
\|\partial_j f_\lambda\|_1
=\lambda\|\partial_j f\|_1 .
\end{gathered}
\tag{1.2}
\]
Here differentiation contributes \(\lambda^{n+1}\), while \(y=\lambda x\) contributes \(\lambda^{-n}\) to volume. Since
\[
|\nabla u|\le\sum_{j=1}^n|\partial_j u|,
\]
the proved finite Minkowski inequality gives (1.1) with
\[
C_n=\sum_{j=1}^n\|\partial_j f\|_1.
\]
Nothing in the choice of \(f\) depends on \(p,u,\lambda\).

If \(\lambda=0\), first obtain the smooth representative with the radius-one cutoff. Apply the positive-bandwidth result to every radius \(\varepsilon>0\). It gives \(\|\nabla u\|_p\le C_n\varepsilon\|u\|_p\), so that norm is zero. Each derivative is continuous and zero almost everywhere, hence zero everywhere: a nonzero continuous value would persist on a ball containing a positive-volume cube. The segment fundamental theorem makes \(u\) constant. A nonzero constant has infinite finite \(L^p\) norm, as seen on disjoint unit cubes. ∎

## A spectral point yields an actual plane wave limit

**Theorem 2.1 (normalized localization).** If \(u\in L^\infty(\mathbb R^n)\) and \(\xi_0\in\operatorname{supp}Fu\), there are actual tests \(\phi_j\in\mathcal S\) for \(j\ge1\) such that
\[
|u*\phi_j(x)|\le1\quad(x\in\mathbb R^n),\qquad
u*\phi_j\longrightarrow e^{ix\cdot\xi_0}
\]
uniformly on each compact set.

**Proof: normalization.** For \(0<\varepsilon<1\), choose \(\eta_\varepsilon\in C_c^\infty\), supported in \(B(\xi_0,\varepsilon)\), equal to one near \(\xi_0\). The supplied cutoff construction gives such a function by translating and rescaling a fixed bump. Set
\[
f_\varepsilon=G\eta_\varepsilon,\qquad
v_\varepsilon=u*f_\varepsilon .
\]
The function \(v_\varepsilon\) is smooth, bounded by Lemma 1.0, and has transform \(\eta_\varepsilon Fu\). It cannot be zero: on the neighbourhood where \(\eta_\varepsilon=1\), a zero product would make \(Fu\) vanish, contrary to \(\xi_0\in\operatorname{supp}Fu\). Consequently \(M_\varepsilon=\|v_\varepsilon\|_\infty>0\).

For a continuous function the essential and pointwise suprema agree. Any value strictly above an alleged essential bound persists on a ball of positive measure. Choose \(x_\varepsilon\) with \(|v_\varepsilon(x_\varepsilon)|\ge(1-\varepsilon)M_\varepsilon\), and define
\[
\begin{gathered}
c_\varepsilon=
\frac{\overline{v_\varepsilon(x_\varepsilon)}}
 {|v_\varepsilon(x_\varepsilon)|M_\varepsilon},\\
w_\varepsilon(x)=c_\varepsilon v_\varepsilon(x+x_\varepsilon).
\end{gathered}
\tag{2.1}
\]
Thus \(\|w_\varepsilon\|_\infty=1\) and \(w_\varepsilon(0)\) is real in \([1-\varepsilon,1]\).

**Proof: the Fourier signs and the limit.** For a bounded function \(v\), a real vector \(a\) and a Schwartz test \(\psi\), absolute integrability of \(vF\psi\) permits
\[
\begin{aligned}
F(v(\cdot+a))(\psi)
&=\int v(y)F\psi(y-a)\,dy\\
&=Fv(e^{ia\cdot\xi}\psi(\xi)).
\end{aligned}
\]
Here \(F(e^{ia\cdot\xi}\psi)(y)=F\psi(y-a)\) follows inside the Schwartz integral. Similarly, for real \(b\),
\[
F(e^{ib\cdot x}v)(\psi)=Fv(\psi(\cdot+b)),
\]
because \(e^{ib\cdot x}F\psi(x)=F(\psi(\cdot+b))(x)\). The last test formula shifts the support by \(b\): if a test is supported away from \(\operatorname{supp}Fv+b\), its translate in this formula is supported away from \(\operatorname{supp}Fv\). Applying the inverse shift proves equality of the supports. Translation only multiplies by a nowhere-zero smooth factor and preserves support by the same local division argument.

It follows that \(z_\varepsilon(x)=e^{-ix\cdot\xi_0}w_\varepsilon(x)\) has Fourier support in \(B(0,\varepsilon)\) and \(\|z_\varepsilon\|_\infty=1\). Theorem 1.1 and the segment fundamental theorem give
\[
\begin{aligned}
|z_\varepsilon(x)-1|
&\le |z_\varepsilon(0)-1|
 +\left|\int_0^1 x\cdot\nabla z_\varepsilon(tx)\,dt\right|\\
&\le\varepsilon+C_n\varepsilon|x|.
\end{aligned}
\tag{2.2}
\]
The first line uses the ordinary real-parameter fundamental theorem on real and imaginary parts. The gradient estimate uses the Euclidean Cauchy–Schwarz inequality.

Finally,
\[
\phi_\varepsilon(y)=c_\varepsilon f_\varepsilon(y+x_\varepsilon)\in\mathcal S
\]
is an actual convolution test: substitution into \(\int u(y)\phi_\varepsilon(x-y)\,dy\) gives \(u*\phi_\varepsilon=w_\varepsilon\). Take \(\varepsilon=1/(j+1)\). Since \(|w_\varepsilon-e^{ix\cdot\xi_0}|=|z_\varepsilon-1|\), (2.2) proves the assertion. ∎

## The same localization converges with every derivative

**Corollary 2.2 (full derivative and tempered convergence).** The same \(w_\varepsilon=u*\phi_\varepsilon\) converges to \(e^{ix\cdot\xi_0}\) in \(C^\infty\) on every compact set. Every derivative also converges strongly in \(\mathcal S'\). The errors on each compact set and each bounded Schwartz test family are \(O(\varepsilon)\). No uniform seminorm bound on the \(\phi_\varepsilon\) is required.

**Proof: every derivative.** Keep the fixed \(f=G\eta\) from Theorem 1.1. Define
\[
\begin{gathered}
B_\beta=\prod_{\nu=1}^n\|\partial_\nu f\|_1^{\beta_\nu},
\qquad B_0=1,\\
\|\partial^\beta z_\varepsilon\|_\infty
\le B_\beta\varepsilon^{|\beta|}\qquad(|\beta|>0).
\end{gathered}
\tag{J1}
\]
To prove the inequality, apply (1.2) in each coordinate in succession. After one step the derivative is bounded and its Fourier transform is \(i\xi_\nu Fz_\varepsilon\), so its support stays in the same ball. Thus the next application has the same bandwidth. Induction through all \(|\beta|\) steps yields exactly the displayed product.

For a multiindex \(\alpha\), set \(e_0(x)=e^{ix\cdot\xi_0}\). The finite Leibniz rule gives
\[
\begin{gathered}
R_{\alpha,\varepsilon}(x):=\partial^\alpha(w_\varepsilon-e_0)(x)
=e_0(x)\sum_{\beta\le\alpha}C_{\alpha,\beta}Z_{\beta,\varepsilon}(x),\\
C_{\alpha,\beta}=\binom{\alpha}{\beta}(i\xi_0)^{\alpha-\beta},
\qquad Z_{\beta,\varepsilon}=\partial^\beta(z_\varepsilon-1),\\
|R_{\alpha,\varepsilon}(x)|
\le \varepsilon|\xi_0^\alpha|(1+C_n|x|)
 +\sum_{0<\beta\le\alpha}\binom{\alpha}{\beta}
 |\xi_0^{\alpha-\beta}|B_\beta\varepsilon^{|\beta|}.
\end{gathered}
\tag{J2}
\]
The term \(\beta=0\) uses (2.2); every other derivative kills the subtracted constant and uses (J1). Products over zero exponents equal one, including for \(\alpha=0\). All mixed coefficients are retained. Since \(0<\varepsilon<1\), put
\[
\begin{gathered}
A_{\alpha,\xi_0}
=|\xi_0^\alpha|\max(1,C_n)
 +\sum_{0<\beta\le\alpha}\binom{\alpha}{\beta}
 |\xi_0^{\alpha-\beta}|B_\beta,\\
|R_{\alpha,\varepsilon}(x)|
\le A_{\alpha,\xi_0}\varepsilon(1+|x|).
\end{gathered}
\tag{J3}
\]
This proves the compact convergence of each derivative, including at zero coordinates of \(\xi_0\).

**Proof: the strong topology.** Choose an integer \(N>n+1\), and set
\[
I_N=\int_{\mathbb R^n}(1+|x|)\langle x\rangle^{-N}\,dx.
\]
On the unit ball the integrand is bounded. On \(2^j\le|x|<2^{j+1}\), it is at most \(3\cdot2^{j(1-N)}\), and the containing cube has volume \(2^{n(j+2)}\). Hence \(I_N<\infty\), by the geometric series with exponent \(n+1-N<0\). Equation (J3) gives the actual pairing estimate
\[
|R_{\alpha,\varepsilon}(\psi)|
\le A_{\alpha,\xi_0}\varepsilon I_N P_N(\psi).
\tag{J4}
\]
Taking the supremum over any bounded Schwartz family proves the strong convergence. Substituting \(\varepsilon=1/(j+1)\) gives the asserted rate for this very sequence. ∎

The weight \(1+|x|\) permits a global distributional estimate while allowing failure of global uniform convergence. Solution 9 shows that failure even for a bounded Schwartz input.

## The solution class changes the zero set that matters

**Lemma 3.0 (complex roots, with the needed proof).** Every nonconstant complex polynomial of one variable has a complex zero.

**Proof.** Suppose \(q(z)=\sum_{k=0}^d a_kz^k\), \(a_d\ne0\), has no zero. Set \(h(r,\theta)=q(re^{i\theta})\). Finite differentiation gives \(h_{r\theta}=h_{\theta r}\), and therefore
\[
\partial_r\!\left(\frac{h_\theta}{h}\right)
=\frac{h_{\theta r}h-h_\theta h_r}{h^2}
=\partial_\theta\!\left(\frac{h_r}{h}\right).
\]
These are continuous on each rectangle \([0,R]\times[0,2\pi]\), since its nonvanishing denominator has a positive minimum modulus. The functions are periodic in \(\theta\), and \(h_\theta(0,\theta)=0\). Absolute Fubini and the fundamental theorem, in the two orders, give
\[
\begin{aligned}
\int_0^{2\pi}\frac{h_\theta(R,\theta)}{h(R,\theta)}\,d\theta
&=\int_0^{2\pi}\int_0^R
 \partial_r(h_\theta/h)\,dr\,d\theta\\
&=\int_0^R
 \left[\frac{h_r(r,\theta)}{h(r,\theta)}\right]_{\theta=0}^{2\pi}\,dr=0.
\end{aligned}
\]
For \(R\ge1\), put
\[
\begin{gathered}
s_R(\theta)=\sum_{k<d}\frac{a_k}{a_d}R^{k-d}e^{i(k-d)\theta},\\
\|s_R\|_\infty\le\frac{1}{R}\sum_{k<d}|a_k/a_d|,
\qquad
\|\partial_\theta s_R\|_\infty
\le\frac{1}{R}\sum_{k<d}(d-k)|a_k/a_d|.
\end{gathered}
\]
Thus \(h(R,\theta)=a_dR^de^{id\theta}(1+s_R(\theta))\) and
\[
\frac{h_\theta}{h}=id+\frac{\partial_\theta s_R}{1+s_R}
\longrightarrow id
\]
uniformly, since eventually \(\|s_R\|_\infty\le1/2\). The preceding zero integral tends to \(2\pi id\), contradicting \(d\ge1\). ∎

**Theorem 3.1 (five solution classes).** Let \(P\) be a complex polynomial in \(n\ge1\) variables. The equation \(P(D)u=0\) has a nonzero solution exactly as follows:

| Required class | Necessary and sufficient condition |
| --- | --- |
| \(\mathcal D'(\mathbb R^n)\) | \(P=0\) or \(P\) has positive degree |
| \(\mathcal S'(\mathbb R^n)\) | \(P\) has a real zero, including \(P=0\) |
| \(\mathcal E'(\mathbb R^n)\) | \(P=0\) |
| \(C_c^\infty(\mathbb R^n)\) | \(P=0\) |
| \(\mathcal S(\mathbb R^n)\) | \(P=0\) |

Here \(\mathcal E'\) denotes compactly supported distributions.

**Proof: unrestricted distributions.** For \(P=0\), any nonzero compact smooth bump belongs to all five classes and solves the equation. For nonzero constant \(P\), multiplication by its reciprocal makes any solution zero.

Suppose \(P\) has positive degree \(d\), with leading homogeneous part \(H_d\ne0\). There exists \(v\in\mathbb R^n\) with \(H_d(v)\ne0\). Otherwise the real polynomial function \(H_d\) would vanish identically, and its derivatives at zero would give \(\partial^\alpha H_d(0)=\alpha!c_\alpha=0\) for every coefficient. The complex polynomial \(q(t)=P(tv)\) therefore has degree \(d\). Lemma 3.0 gives \(t_0\in\mathbb C\) with \(q(t_0)=0\). Let \(\zeta=t_0v\). The smooth nowhere-zero function \(e^{ix\cdot\zeta}\) is bounded on each compact set and defines a distribution; explicitly,
\[
\left|\int e^{ix\cdot\zeta}\psi(x)\,dx\right|
\le |K|\sup_K|e^{ix\cdot\zeta}|\sup_K|\psi|
\]
for tests supported in a compact \(K\). If \(K\) has zero volume the same estimate still applies. Finite differentiation gives
\[
P(D)e^{ix\cdot\zeta}=P(\zeta)e^{ix\cdot\zeta}=0.
\]
The associated distribution is nonzero, for example by testing against \(e^{-ix\cdot\zeta}\rho(x)\), where \(\rho\) is a nonnegative compact bump of positive integral.

**Proof: tempered solutions.** The supplied Fourier identities give
\[
F(P(D)u)=P(\xi)Fu.
\]
If \(P\) has no real zero, \(1/P=\overline P/|P|^2\) is smooth on \(\mathbb R^n\). For every \(\psi\in C_c^\infty\), the quotient \(\psi/P\) is a compact test, and
\[
Fu(\psi)=(P Fu)(\psi/P)=0.
\]
Compact-cutoff density in \(\mathcal S\) and continuity make \(Fu\) zero on every Schwartz test. Inversion gives \(u=0\). If \(P(\xi_0)=0\) for a real vector \(\xi_0\), the bounded plane wave \(e^{ix\cdot\xi_0}\) is a nonzero tempered solution, by the \(L^\infty\) embedding proved in Theorem 1.1.

**Proof: rapid decay and compact support.** A nonzero polynomial cannot vanish on an open real ball. If it did, every partial derivative at its centre would vanish, and the exact finite polynomial Taylor expansion there would make \(P\) identically zero. Hence \(\{P\ne0\}\) is dense. If \(u\in\mathcal S\) solves the equation, \(Fu\) is smooth and \(P Fu=0\) as a distribution. This continuous product is pointwise zero: a nonzero value can be rotated to have positive real part on a ball and paired with a nonnegative bump there. Therefore \(Fu=0\) on \(\{P\ne0\}\), and continuity gives zero everywhere. Inversion gives \(u=0\). This includes \(C_c^\infty\subset\mathcal S\).

If \(u\in\mathcal E'\) solves the equation, then \(u*\phi\) is compact smooth for each \(\phi\in C_c^\infty\) by U021, Theorem 2.1. Its derivative rule gives \(P(D)(u*\phi)=(P(D)u)*\phi=0\), so the preceding paragraph makes it zero.

Choose a nonnegative compact smooth \(\rho\) of integral one, put \(\rho_\varepsilon(y)=\varepsilon^{-n}\rho(y/\varepsilon)\), and let \(\widetilde\rho(y)=\rho(-y)\). The normalization exists because a nonzero nonnegative bump has positive finite integral. U021's test-pairing identity gives
\[
(u*\rho_\varepsilon)(\psi)
=u(\widetilde\rho_\varepsilon*\psi),\qquad
(\widetilde\rho_\varepsilon*\psi)(x)
=\int \rho(z)\psi(x+\varepsilon z)\,dz.
\]
For \(0<\varepsilon\le1\), these tests have support in the fixed compact set
\(\operatorname{supp}\psi-\{tz:z\in\operatorname{supp}\rho,\ 0\le t\le1\}\).
For every multiindex \(\alpha\), differentiation under this compact integral gives the same formula with \(\partial^\alpha\psi\). Uniform continuity of that compactly supported derivative makes its difference from \(\partial^\alpha\psi(x)\) uniformly tend to zero. Thus \(\widetilde\rho_\varepsilon*\psi\to\psi\) in one fixed compact test space, and continuity of \(u\) proves \(u*\rho_\varepsilon\to u\) in \(\mathcal D'\). All convolutions were zero, so \(u=0\). This completes every class in the table. ∎

## Exercises

**Exercise 1 (basic).** For \(b\in\mathbb R^n\), compute the \(L^\infty\) norm and Euclidean gradient norm of \(u(x)=4e^{ix\cdot b}\). Which finite \(L^p\) spaces contain it?

**Exercise 2 (foundation).** If \(u\in L^p\) has Fourier support in the radius-\(\lambda\) ball, find the support and norm of \(v(x)=u(3x)\) and its first derivative bound.

**Exercise 3 (intermediate).** Prove the all-multiindex bound \(\|\partial^\alpha u\|_p\le C_{n,\alpha}\lambda^{|\alpha|}\|u\|_p\), treating zero bandwidth and the zero multiindex explicitly.

**Exercise 4 (intermediate).** For \(u(x)=2e^{2ix}+3e^{-5ix}\), construct \(\phi\in\mathcal S\) with \(u*\phi=e^{2ix}\) exactly.

**Exercise 5 (foundation).** Determine the five nonzero-solution possibilities for \((D^2+1)u=0\) on the line and exhibit a distributional solution.

**Exercise 6 (intermediate).** Do the same for \((D_1D_2-2)u=0\), exhibiting a bounded solution.

**Exercise 7 (intermediate).** Give infinitely many linearly independent bounded solutions of \(D_1u=0\) on \(\mathbb R^2\). Decide whether a nonzero compactly supported distributional solution exists.

**Exercise 8 (advanced).** In Theorem 2.1, prescribe an error \(t>0\) on \(|x|\le R\). Give an explicit sufficient \(j\), and explain why no quantitative lower bound on \(M_\varepsilon\) is needed.

**Exercise 9 (advanced: the extent of the limit).** Take \(u(x)=e^{-x^2}\), \(\xi_0=0\). Prove that every actual \(w_\varepsilon\) of Theorem 2.1 is Schwartz, with every compact derivative limit and strong tempered derivative limit from Corollary 2.2, while \(\|w_\varepsilon-1\|_\infty\ge1\). Give the sharper global positive-derivative bounds.

## Solutions

**Solution 1.** Since \(|u|=4\) and \(\nabla u=ibu\),
\[
\|u\|_\infty=4,\qquad \|\nabla u\|_\infty=4|b|.
\]
The integral of \(|u|^p=4^p\) is infinite for every finite \(p\), by the disjoint unit cubes in \(\mathbb R^n\), so none of those spaces contains \(u\).

**Solution 2.** The exact transposed scaling formula is
\[
\begin{aligned}
Fv(\psi)
&=3^{-n}\int u(y)F\psi(y/3)\,dy\\
&=Fu(\psi(3\,\cdot)).
\end{aligned}
\]
The integrals converge by Hölder; the second equality uses
\(F(\psi(3\,\cdot))(y)=3^{-n}F\psi(y/3)\), proved by ordinary substitution. In function notation the result is \(Fv(\xi)=3^{-n}Fu(\xi/3)\); the displayed pairing specifies it even for a distribution. A test supported away from \(3\operatorname{supp}Fu\) pulls back to one away from \(\operatorname{supp}Fu\). Applying the inverse dilation gives exact equality of supports, hence the new bandwidth is at most \(3\lambda\).

Affine measure substitution, including preservation of null sets, gives
\[
\|v\|_p=3^{-n/p}\|u\|_p,\qquad
\|\nabla v\|_p=3^{1-n/p}\|\nabla u\|_p ,
\]
where \(1/p=0\) at infinity. The smooth representative and its chain rule come from Theorem 1.1. Either these formulas and (1.1), or direct application of that theorem at bandwidth \(3\lambda\), give \(\|\nabla v\|_p\le3C_n\lambda\|v\|_p\).

**Solution 3.** Apply (1.2) successively in the coordinates occurring in \(\alpha\). At each step the derivative remains in \(L^p\), and its Fourier support stays in the same ball by multiplication by the appropriate \(i\xi_j\). This proves the exact constant
\[
C_{n,\alpha}=\prod_{j=1}^n\|\partial_j f\|_1^{\alpha_j}.
\]
For \(\alpha=0\), the assertion is the identity with constant one. At \(\lambda=0\), Theorem 1.1 makes the function constant, so every positive derivative is zero. No value of \(0^0\) is needed.

**Solution 4.** Choose a compact smooth bump \(\chi\) supported in \((1,3)\) with \(\chi(2)=1\); the scalar cutoff construction supplies it. Put \(\eta=\chi/2\) and \(\phi=G\eta\). Direct absolute integration gives
\[
(e^{ib\,\cdot}*\phi)(x)
=e^{ibx}\int e^{-iby}\phi(y)\,dy
=e^{ibx}\eta(b).
\]
Thus \(2\eta(2)=1\), \(3\eta(-5)=0\), and the convolution is exactly \(e^{2ix}\) everywhere.

**Solution 5.** The polynomial \(\xi^2+1\) has positive degree and no real zero. Theorem 3.1 gives nonzero solutions in \(\mathcal D'\) and none in the other four classes. The smooth locally integrable function \(e^x\) is a nonzero distribution and satisfies \(D^2e^x=-e^x\). The tempered criterion proves that this distribution is not tempered.

**Solution 6.** The real zero set is \(\{(r,2/r):r\ne0\}\). Hence \(\mathcal D'\) and \(\mathcal S'\) contain nonzero solutions, whereas \(\mathcal E'\), \(C_c^\infty\) and \(\mathcal S\) do not. The bounded plane wave \(e^{i(x_1+2x_2)}\) works because \(D_1D_2\) multiplies it by \(1\cdot2\).

**Solution 7.** For \(m=0,1,2,\ldots\), the bounded function \(e^{imx_2}\) is independent of \(x_1\) and solves the equation. A finite linear relation, even initially distributional, is pointwise zero because its left side is continuous, by the detecting-bump argument in Theorem 3.1. Multiplication by \(e^{-i\ell x_2}\) and integration from \(0\) to \(2\pi\) isolates \(2\pi\) times the coefficient of index \(\ell\). Indeed, the constant exponential integrates to \(2\pi\), and for nonzero integer \(k\),
\[
\int_0^{2\pi}e^{ikt}\,dt
=\frac{e^{2\pi ik}-1}{ik}=0
\]
by the proved exponential period and fundamental theorem. Thus all coefficients vanish. The nonzero polynomial \(\xi_1\) admits no nonzero compactly supported distributional solution by Theorem 3.1.

**Solution 8.** Equation (2.2) bounds the error by \((1+C_nR)/(j+1)\). Choose any integer \(j\ge1\) with
\[
j+1\ge\frac{1+C_nR}{t}.
\]
The support condition proves \(M_\varepsilon>0\), which makes the actual division in (2.1) legitimate. It gives \(\|w_\varepsilon\|_\infty=1\) whatever the size of that positive number. A small \(M_\varepsilon\) can enlarge the scalar in \(\phi_\varepsilon\); the argument imposes no uniform bound on those test seminorms.

**Solution 9.** The Gaussian and all its derivatives are polynomial multiples of \(e^{-x^2}\), so the input is Schwartz. The decay follows, for any required power, from \(e^s\ge s^L/L!\) with \(s=x^2/2\) and sufficiently large \(L\). The exact transform, proved in the supplied Fourier foundation F3, is
\[
Fu(\xi)=\sqrt\pi e^{-\xi^2/4}.
\]
It is strictly positive, so every neighbourhood of zero detects a nonzero Fourier distribution by a nonnegative bump. Thus \(\xi_0=0\) is permitted. The localized transform \(\eta_\varepsilon Fu\) is compact smooth; its inverse \(v_\varepsilon\) is Schwartz by F1–F4. Translation preserves all Schwartz seminorm finiteness by the elementary polynomial weight inequality, and multiplication by the finite scalar \(c_\varepsilon\) preserves it. Hence every actual \(w_\varepsilon\) in Theorem 2.1 is Schwartz.

Corollary 2.2 applies to this same sequence, including every derivative and strong pairing limit. For each fixed \(\varepsilon\), Schwartz decay gives \(w_\varepsilon(x)\to0\) as \(|x|\to\infty\), so \(|w_\varepsilon(x)-1|\to1\) and the supremum norm is at least one. For a positive integer \(h\), the demodulated function equals \(w_\varepsilon\), and (J1) gives
\[
\|w_\varepsilon^{(h)}\|_\infty
\le \|f'\|_1^h\varepsilon^h.
\]
These positive-derivative errors converge uniformly on the whole line although the zero-order errors do not.

## Free sources and exact proof dependencies

- Terence Tao, [*Nonlinear dispersive equations: local and global analysis*, freely posted author excerpt](https://math.ucla.edu/~tao/preprints/chapter.pdf), Appendix A, printed pp. 332–334: smooth frequency cutoffs and the convolution route to Bernstein estimates. Lemma 1.0 and Theorem 1.1 supply the needed endpoint and derivative proofs here; no fractional multiplier or Littlewood–Paley theorem is assumed.
- Keith Conrad, [*The fundamental theorem of algebra via multivariable calculus*](https://kconrad.math.uconn.edu/blurbs/fundthmalg/fundthmalgcalculus.pdf), Theorem 1, pp. 1–3: the periodic rectangle-integration argument. Lemma 3.0 supplies the full complex-quotient calculation, its integral identity and the explicit uniform remainder bound. No logarithm branch, contour theorem or external proof is needed.
- The supplied scalar, integration and Fourier foundations and the exact U008, U021 and U040 results linked at the start provide the earlier programme proofs. Their licence notices remain attached. The lesson's original exposition is CC0.
