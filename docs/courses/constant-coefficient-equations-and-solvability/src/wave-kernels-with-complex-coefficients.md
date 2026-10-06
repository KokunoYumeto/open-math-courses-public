# Wave kernels with complex coefficients

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

A constant potential can change the tail behind a wave front without changing its speed. First-order terms can also be removed by an exponential change of the unknown. We will make both observations precise for arbitrary complex coefficients, construct causal solutions, and prove that every point of the light cone belongs to the support of a suitable homogeneous solution. That last assertion will supply the witness in the next lesson on domain geometry.

Basic references are Bär, Ginoux and Pfäffle's book on wave equations and the flat-kernel construction in *Causal kernels, initial data, and short-time geometry*, cited below.

Write \(x=(t,z)\in\mathbb R\times\mathbb R^d\), where \(d\geq1\), and put
\[
\begin{aligned}
L_\kappa&=\partial_t^2-\Delta_z+\kappa,\quad \kappa\in\mathbb C,\\
C_+&=\{(t,z):t\geq|z|\},\\
C_-&=-C_+.
\end{aligned}
\tag{1}
\]
Our spatial Fourier transform has negative exponential and no prefactor; its inverse has prefactor \((2\pi)^{-d}\). Pairings of distributions with tests are complex bilinear. Smooth distribution-valued dependence below uses the strong topology, meaning uniform convergence on bounded families of tests.

## The flat kernels we use

The flat wave construction gives distributions \(R_j\), \(j\geq0\), with
\[
\begin{gathered}
R_0=\delta_{(0,0)},\qquad L_0R_{j+1}=R_j,\\
\operatorname{supp}R_j\subset C_+.
\end{gathered}
\tag{2}
\]
For \(t\geq0\), \(R_{j+1}\) is a smooth one-sided function with values in spatial distributions. Its spatial Fourier transform is
\[
g_j(t,\xi)=\underbrace{S_\omega*\cdots*S_\omega}_{j+1},
\qquad \omega=|\xi|,
\tag{3}
\]
where convolution here is in nonnegative time, and
\[
S_\omega(t)=\frac{\sin(t\omega)}{\omega},\qquad
S_0(t)=t.
\tag{4}
\]
In particular \(R_1(0+)=0\), \(\partial_tR_1(0+)=\delta_z\), and the corresponding two traces of \(R_{j+1}\) vanish for \(j\geq1\). These are exactly the normalization and Volterra formula from the cited flat-kernel lesson; its notation is \(E_j=j!R_{j+1}\).

We also use Fourier inversion on Schwartz functions and distributions, smooth multiplication and tensor products of distributions, and convolution when addition is proper on the two supports. The specific properness needed for causal data will be checked below. No wave evolution theorem is needed in addition to (2)–(4).

## Adding a complex potential

**Theorem 2.1.** The series
\[
E_\kappa^+=\sum_{j=0}^{\infty}(-\kappa)^jR_{j+1}
\tag{5}
\]
converges strongly in distributions, locally uniformly for \(\kappa\in\mathbb C\). Its restriction to nonnegative time converges with every time derivative in spatial tempered distributions on bounded time intervals. It is entire in \(\kappa\), is supported in \(C_+\), and satisfies
\[
\begin{gathered}
L_\kappa E_\kappa^+=\delta_{(0,0)},\\
E_\kappa^+(0+)=0,\qquad
\partial_tE_\kappa^+(0+)=\delta_z.
\end{gathered}
\tag{6}
\]

**Proof.** Change the time variables in (3) to \(tu_i\). On the simplex \(u_i\geq0\), \(\sum_{i=1}^{j+1}u_i=1\), this gives
\[
\begin{gathered}
g_j(t,\xi)\\
{}=t^{2j+1}\int_{\Sigma_j}
\prod_{i=1}^{j+1}u_i\operatorname{sinc}(t\omega u_i)\,du.
\end{gathered}
\tag{7}
\]
with the single-factor interpretation when \(j=0\). Here \(\operatorname{sinc}v=\sin v/v=\int_0^1\cos(sv)\,ds\), including at zero. The elementary simplex integral is
\[
\int_{\Sigma_j}\prod_{i=1}^{j+1}u_i\,du
=\frac1{(2j+1)!}.
\tag{8}
\]
Consequently \(|g_j(t,\xi)|\leq t^{2j+1}/(2j+1)!\) for real \(\xi\) and \(t\geq0\).

We need the same factorial for derivatives. Fix an integer \(k\geq0\) and \(0\leq t\leq T\), and set \(T_*=\max(1,T)\). A derivative of a sinc factor is bounded by \(\omega^\ell u_i^\ell\) at order \(\ell\), using its cosine integral. Differentiating \(t^{2j+1}\) costs at most \((2j+1)^kT_*^{2j+1}\); when a derivative order exceeds this integer power the term is zero. The product rule has at most a constant depending on \(k\) times \((j+1)^k\) choices of factors. Keeping the factors \(u_i\), and bounding all additional powers of them by one, proves
\[
\begin{gathered}
|\partial_t^kg_j(t,\xi)|\\
{}\leq\frac{C_k(j+1)^{2k}T_*^{2j+1}}
{(2j+1)!}(1+|\xi|)^k.
\end{gathered}
\tag{9}
\]
Increasing \(C_k\) handles \(j=0\). On a bounded family of Schwartz tests, their Fourier transforms have a common integrable bound after multiplication by \((1+|\xi|)^k\). Formula (9) therefore proves convergence of (5) after spatial inversion, uniformly on such families, with every time derivative and uniformly for \(|\kappa|\leq M\). The same factorial proves convergence after any fixed number of \(\kappa\) derivatives. Thus the sum is entire and has the asserted strong smoothness for \(t\geq0\).

To obtain a spacetime distribution, integrate these spatial pairings in \(t\geq0\). For a bounded family of spacetime tests on one compact support, the spatial Fourier decay estimates are uniform in \(t\); (9) proves strong convergence of that integral. Each summand has support in \(C_+\), so the limit has the same support inclusion.

For the finite sum \(E_{\kappa,N}^+\), the recursion (2) gives
\[
L_\kappa E_{\kappa,N}^+
=\delta+\kappa(-\kappa)^N R_{N+1}.
\tag{10}
\]
The remainder tends strongly to zero by the estimate just proved. Distributional differentiation is continuous, which proves the equation in (6). The convergent time-derivative series and the traces after (4) give its two initial data. \(\square\)

The spatial multiplier of the sum can now be written in a form that does not choose a square-root branch. Define the entire function of \(q\)
\[
s(t,q)=\sum_{\ell=0}^{\infty}
\frac{(-q)^\ell t^{2\ell+1}}{(2\ell+1)!}.
\tag{11}
\]
For fixed real \(\xi\), the convergent series in (5) solves the scalar equation \(v''+(|\xi|^2+\kappa)v=0\), \(v(0)=0\), \(v'(0)=1\). The power series (11) has those properties too. Uniqueness follows, for example, by writing the difference as a two-component first-order integral equation and iterating its zero-data estimate. Hence
\[
\begin{gathered}
\mathcal F_z E_\kappa^+(t,\xi)
=s(t,|\xi|^2+\kappa),\\
t\geq0.
\end{gathered}
\tag{12}
\]
If \(w^2=q\), this is \(\sin(tw)/w\), with its removable value at \(w=0\). Changing the sign of \(w\) makes no change.

## A homogeneous kernel and its exact light front

Reflect time and put
\[
\begin{gathered}
E_\kappa^-(t,z)=E_\kappa^+(-t,z),\\
F_\kappa=E_\kappa^+-E_\kappa^-.
\end{gathered}
\tag{13}
\]
Time reflection commutes with \(L_\kappa\); therefore both \(E_\kappa^\pm\) have image \(\delta\). The function of time underlying \(F_\kappa\) is the odd extension of the one-sided kernel. It is smooth with values in spatial tempered distributions across zero: the scalar equation and the initial data show that all even time derivatives at zero vanish. The bounds in (9), or the equation differentiated repeatedly, give this assertion in the strong topology.

**Theorem 3.1.** We have
\[
\begin{gathered}
L_\kappa F_\kappa=0,\\
\operatorname{supp}F_\kappa\subset C_+\cup C_-.
\end{gathered}
\tag{14}
\]
Every point of the light cone \(\{(t,z):t^2=|z|^2\}\), including its vertex, belongs to \(\operatorname{supp}F_\kappa\).

**Proof.** The equation and inclusion follow from (6) and (13). Write \(S_\kappa(t)\) for the spatial distribution at time \(t\). It is supported in the closed ball \(|z|\leq |t|\), and its Fourier transform is \(s(t,|\xi|^2+\kappa)\) for every real \(t\).

Fix \(t\ne0\). Spatial rotations preserve this multiplier, so Fourier injectivity makes \(S_\kappa(t)\), and hence its support, invariant under all orthogonal transformations. Suppose its support lay in a ball of radius \(r<|t|\). The elementary compact-distribution Fourier estimate would imply, for some \(N,C\) and \(r<r'<|t|\),
\[
\begin{gathered}
|\widehat{S_\kappa(t)}(i\rho e_1)|
\leq C(1+\rho)^N e^{r'\rho},\\
\rho\geq1.
\end{gathered}
\tag{15}
\]
To recall the estimate, choose a smooth cutoff equal to one near the support and supported in the ball of radius \(r'\). Apply the finite-order estimate for the compact distribution to that cutoff times \(e^{\rho z_1}\). Every derivative is bounded by a fixed polynomial in \(\rho\) times \(e^{r'\rho}\), which gives (15).

Its compactly supported Fourier transform is entire in the complex spatial frequency. The right side of (12) is entire there too, with \(|\xi|^2\) replaced by \(\xi\cdot\xi\). Equality on real frequency space extends by successive one-variable identity theorems. At \(\xi=i\rho e_1\), choose
\[
\begin{gathered}
a_\rho=(\rho^2-\kappa)^{1/2}
=\rho+O(\rho^{-1}),\\
\operatorname{Re}a_\rho>0.
\end{gathered}
\tag{16}
\]
The binomial series near one justifies this choice for large \(\rho\), even when \(\kappa\) is complex. Then
\[
\begin{aligned}
|s(t,-\rho^2+\kappa)|
&=\left|\frac{\sinh(ta_\rho)}{a_\rho}\right|\\
&\sim\frac{e^{|t|\rho}}{2\rho}.
\end{aligned}
\tag{17}
\]
Indeed the exponentially decreasing term in the hyperbolic sine is negligible, \(\operatorname{Re}a_\rho=\rho+O(\rho^{-1})\), and \(|a_\rho|/\rho\to1\). This contradicts (15).

The spatial support is compact. It therefore attains the maximal radius \(|t|\); if that radius were smaller, the preceding argument would apply. Rotation invariance now puts the entire sphere \(|z|=|t|\) in that support.

Finally suppose \(F_\kappa\) vanished in a spacetime neighborhood of \((t_0,z_0)\) with \(t_0\ne0\) and \(|z_0|=|t_0|\). For each spatial test supported in a sufficiently small neighborhood of \(z_0\), its smooth pairing with \(S_\kappa(t)\) would be zero on an interval about \(t_0\), by testing also in time. Its value at \(t_0\) would be zero, contradicting the sphere statement. The vertex belongs to the spacetime support by closure. \(\square\)

The theorem asserts nonvanishing at the front, not at every point of the cone's interior. For example, in three spatial dimensions the zero-potential kernel is supported only on the front.

## Removing first-order terms

Let \(D=-i\partial\), \(G=\operatorname{diag}(-1,1,\ldots,1)\), and
\[
\begin{gathered}
q(\zeta)=\zeta^TG\zeta,\\
P(\zeta)=q(\zeta)+b^T\zeta+c.
\end{gathered}
\tag{18}
\]
where \(b\in\mathbb C^{d+1}\), \(c\in\mathbb C\). The transpose is algebraic, with no complex conjugation. Thus \(q(D)=\partial_t^2-\Delta_z\).

**Theorem 4.1.** Set
\[
\alpha=-\tfrac12Gb,\qquad
\kappa=c-\tfrac14b^TGb.
\tag{19}
\]
Then
\[
E_P^\pm=e^{ix\cdot\alpha}E_\kappa^\pm,\qquad
F_P=e^{ix\cdot\alpha}F_\kappa
\tag{20}
\]
satisfy \(P(D)E_P^\pm=\delta\), \(P(D)F_P=0\). Their supports equal the respective supports before multiplication. In particular \(F_P\) is supported in the double cone and contains the entire light cone in its support.

**Proof.** Distributional differentiation obeys
\[
D(e^{ix\cdot\alpha}v)
=e^{ix\cdot\alpha}(D+\alpha)v.
\]
Expanding \(P(\zeta+\alpha)\), its linear term is \(2G\alpha+b=0\), and its constant term is precisely \(\kappa\). Therefore
\[
P(D)(e^{ix\cdot\alpha}v)
=e^{ix\cdot\alpha}L_\kappa v.
\tag{21}
\]
The multiplying function equals one at the origin and never vanishes anywhere. It preserves support, since its reciprocal is smooth. Equations (6), (14) and Theorem 3.1 prove all claims. Complex exponential growth causes no difficulty for distributions on compact test supports. \(\square\)

The formal transpose \(P^t=P(-D)\) has linear coefficient \(-b\), the same constant \(\kappa\), and gauge vector \(-\alpha\). Thus every assertion applies to the transpose as well.

## Causal distribution data

**Theorem 5.1.** For each \(f\in\mathcal D'(\mathbb R^{d+1})\) supported in \(H_+=\{t\geq0\}\), there is a unique solution \(u\) supported in \(H_+\) of \(P(D)u=f\). It is
\[
u=E_P^+*f.
\tag{22}
\]

**Proof.** Addition is proper on \(C_+\times H_+\). To check it, let the sum lie in a compact set whose time coordinate is at most \(T\). If the first point is \((s,y)\in C_+\), then \(0\leq s\leq T\), \(|y|\leq s\leq T\). The first point is bounded, and the second is bounded by subtracting it from the compact sum. The inverse image is closed, so it is compact. This proves that the convolution in (22) exists. Its support lies in \(H_+\), and differentiation under the distributional convolution gives \(P(D)u=f\).

If \(P(D)v=0\) and \(\operatorname{supp}v\subset H_+\), the same properness permits \(E_P^+*v\). Commuting a constant differential operator with this convolution gives
\[
\begin{aligned}
v&=(P(D)E_P^+)*v\\
&=E_P^+*(P(D)v)=0.
\end{aligned}
\tag{23}
\]
For clarity, this differentiation rule follows by applying the tensor product to a test of the sum variable, with a cutoff equal to one near the compact part of the two supports over that test. Integration by parts differentiates the test in either variable; derivatives of the cutoff are supported away from that part and pair to zero. This also shows why properness was essential. \(\square\)

This construction concerns the Lorentz quadratic principal symbol in (18). A lower order series for a general hyperbolic polynomial requires its own estimates; the factorial argument here uses the flat wave Volterra kernels.

## Exercises with solutions

**Exercise 1 — Elementary level: the one-dimensional constant.** For \(d=1\) and \(\kappa=0\), show that
\[
\begin{aligned}
E_0^+(t,z)&=\tfrac12\boldsymbol1_{\{t>|z|\}},\\
S_0(t,z)&=\tfrac12\operatorname{sgn}(t)
\boldsymbol1_{\{|z|<|t|\}}.
\end{aligned}
\tag{24}
\]
Check the point-source coefficient using characteristic coordinates.

**Solution.** At \(t>0\), the Fourier transform in \(z\) of \(\tfrac12\boldsymbol1_{(-t,t)}\) is \(\sin(t\xi)/\xi\), including its value \(t\) at zero. This identifies the positive-time kernel by (12); odd extension gives the second formula. Set \(r=t+z\), \(s=t-z\). Then \(L_0=4\partial_r\partial_s\), and the first kernel is \(\tfrac12H(r)H(s)\). Its image is \(2\delta(r)\delta(s)\). The Jacobian of \((t,z)\mapsto(r,s)\) has absolute determinant two, so \(\delta(r)\delta(s)=\tfrac12\delta(t,z)\). Thus the image is exactly \(\delta(t,z)\).

**Exercise 2 — Intermediate level: a complex gauge.** In two spacetime coordinates take \(b=(2i,2)\), \(c=3\) in (18). Compute the gauge and the potential. Determine what happens to the support.

**Solution.** We have \(Gb=(-2i,2)\), hence \(\alpha=(i,-1)\). Also \(b^TGb=-(2i)^2+2^2=8\), so \(\kappa=1\). The multiplier is \(e^{-t-iz}\). Thus \(E_P^+=e^{-t-iz}E_1^+\) and \(F_P=e^{-t-iz}F_1\). The smooth reciprocal \(e^{t+iz}\) exists everywhere, so both support sets are unchanged. Replacing the bilinear square by a Hermitian square would give the wrong potential.

**Exercise 3 — Intermediate level: which supports permit convolution?** Explain why addition is proper on \(C_+\times H_+\) but fails to be proper on \(H_+\times H_+\) when \(d\geq1\).

**Solution.** The proof of Theorem 5.1 bounds the first spatial coordinate by its time coordinate; that is the extra information in \(C_+\). In contrast the pairs \(((0,je_1),(0,-je_1))\) lie in \(H_+\times H_+\), all have sum zero, and escape every compact subset of the product. The inverse image of the compact singleton \(\{0\}\) is therefore not compact. Merely having nonnegative time support does not guarantee that two distributions can be convolved.

**Exercise 4 — Advanced level: support on the surface.** For \(d=3\), \(\kappa=0\), prove the spatial identity
\[
\langle S_0(t),\psi\rangle
=\frac{t}{4\pi}\int_{\mathbb S^2}\psi(t\omega)\,d\omega.
\tag{25}
\]
Identify the spacetime support of \(F_0\), and compare it with (24).

**Solution.** Rotation of \(\xi\) to the polar axis gives
\[
\begin{aligned}
\frac1{4\pi}\int_{\mathbb S^2}
e^{-it\omega\cdot\xi}\,d\omega
&=\frac12\int_{-1}^1e^{-it|\xi|s}\,ds\\
&=\operatorname{sinc}(t|\xi|).
\end{aligned}
\tag{26}
\]
The Fourier transform of (25) is consequently \(\sin(t|\xi|)/|\xi|\), so Fourier injectivity proves the identity. It is smooth in \(t\) as a spatial distribution, has value zero and first derivative \(\delta_z\) at zero, and is supported on the sphere at each nonzero time. Its spacetime support is exactly the light cone, including the vertex by closure. Theorem 3.1 proves that no front point is missing. In (24), by contrast, every interior point of either half cone is also in the support. These two dimensions show why front nonvanishing and interior nonvanishing are different assertions.

## References

- *Causal kernels, initial data, and short-time geometry*, [flat wave construction](../prerequisites/wave-hadamard-kernels.html), sections “A Laplace calculation that constructs the whole family” and “Initial traces from a Volterra problem”. These give (2)–(4), with \(E_j=j!R_{j+1}\). The present potential series and light-front argument use those results.
- Christian Bär, Nicolas Ginoux and Frank Pfäffle, [*Wave Equations on Lorentzian Manifolds and Quantization*](https://arxiv.org/abs/0806.1036), European Mathematical Society, 2007, §§1.2 and 2.1–2.4. Their Riesz parameter is twice the parameter used for the flat family above. Their discussion also treats geometric wave operators and vector bundles.
