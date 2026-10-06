# Analytic kernels for unbounded modular operators

**Draft. Self-checked by the writing AI.**

A bounded operator can satisfy an equation involving two unbounded powers without preserving either power's domain. The equation must then be stated through pairings. A decaying Fourier kernel solves the resulting equation and, at the same time, expresses a spectral resolvent through unitary operators. This unit proves those assertions, the strip criterion for spectral domains, and the Gaussian approximation results needed to pass from integral identities to pointwise identities.

The mathematical antecedents are Takesaki, *Theory of Operator Algebras II*, VI.1, Lemmas 1.20–1.22, and VI.2, Lemmas 2.3–2.4. The arguments below start with integral conventions and scalar kernels, then establish the operator and domain results. They do not use the modular fundamental theorem.

## Conventions and exact analytic inputs

Hilbert spaces are arbitrary, and their inner products are linear in the first variable. For a positive injective self-adjoint operator \(A\), the powers \(A^z\) use the real logarithm on \((0,\infty)\). Injectivity does not mean that \(A^{-1}\) is bounded. We use the common spectral bands

\[
P_n=1_{[1/n,n]}(A),\qquad n\geq1.
\tag{MA.1}
\]

They increase strongly to the identity. A band can be infinite dimensional or zero.

The exact spectral inputs are integral domains for Borel functions, spectral multiplication with its domain conditions, real change of variable, and dominated convergence for each vector's finite spectral measure. In particular, if \(f(A)\xi\) is defined, then

\[
P_n\xi\to\xi,\qquad f(A)P_n\xi\to f(A)\xi
\tag{MA.2}
\]

in norm. The spectral kernel supplies these contracts in **SK-05, SK-07 and SK-09**: measurable integral domains, powers and logarithms, and vectorwise dominated convergence and graph cutoffs. These items also give the strongly continuous unitary group \(A^{it}\).

We explicitly retain two elementary analysis contracts:

- **Scalar integration:** scalar Lebesgue integration on Euclidean spaces, dominated and monotone convergence, Fubini for absolutely integrable functions, the change-of-variable formula, and integration by parts for the integrable smooth functions used below.
- **Scalar complex analysis:** the scalar Cauchy integral and residue theorems, Morera's theorem, the identity theorem and the maximum-modulus principle. Holomorphic means complex differentiable on an open set.

These contracts are assumed inputs. The Gaussian normalization, Fourier uniqueness, strip-boundary argument, Banach-valued contour calculation and locally convex integration construction are proved below. Separation by bounded linear functionals and continuous seminorms uses **OA-MOD-OPEN-CONVEX-HB-NORM** and **OA-MOD-OPEN-CONVEX-HB-SEMINORM**, with their existing source and license records. Bounded square roots, continuous functional calculus, adjoints and operator norms use OA-MOD-BK and the Hilbert-space kernel.

## Which integrals take values in which space

Let \(B\) be a Banach space. A norm-continuous function \(f:\mathbb R\to B\) satisfying \(\|f(t)\|\leq m(t)\) for some integrable nonnegative scalar function has an improper norm integral whenever its integrals over compact intervals exist. In our applications the latter are Riemann integrals: continuity on a compact interval is uniform, so two sufficiently fine Riemann sums differ in norm by at most the interval length times the modulus of continuity. Completeness gives their common limit.

For compact intervals \(I\), these integrals satisfy

\[
\left\|\int_I f(t)\,dt\right\|\leq\int_I\|f(t)\|\,dt.
\tag{MA.3}
\]

The tail bound by \(\int_{|t|>R}m(t)\,dt\) makes the compact-interval integrals Cauchy as \(R\to\infty\). Thus the improper integral exists and retains (MA.3). It is the Bochner integral for these functions. Bounded linear maps pass through the integral because they pass through finite sums and norm limits.

We also need a different construction. Suppose \(T(t)\in B(H)\), the function \(t\mapsto T(t)\xi\) is norm-continuous for each \(\xi\in H\), and \(\|T(t)\|\leq C\). If the continuous scalar function \(k\) is integrable, define

\[
T_k\xi=\int_{\mathbb R}k(t)T(t)\xi\,dt.
\tag{MA.4}
\]

The preceding construction in \(H\) proves existence. Linearity and (MA.3) give a bounded operator with

\[
\|T_k\|\leq C\|k\|_1.
\tag{MA.5}
\]

We call (MA.4) a **vectorwise strong integral**. It is not an assertion that \(t\mapsto k(t)T(t)\) is Bochner integrable for the operator norm on \(B(H)\).

If \(T_j(t)\xi\to T(t)\xi\) for every \(t,\xi\), all the operator norms are bounded by the same \(C\), and all the relevant vector functions are continuous, then

\[
\left\|\int k(t)(T_j(t)-T(t))\xi\,dt\right\|
\leq\int |k(t)|\,\|(T_j(t)-T(t))\xi\|\,dt\longrightarrow0
\tag{MA.6}
\]

for a sequence \(j\), by scalar dominated convergence. All spectral cutoff passages below use this sequence. Global operator limits and strip domains impose no countability hypothesis on \(H\).

The same statements hold for integrals over piecewise smooth finite contours, using their parametrizations. A Banach-valued holomorphic function has the contour identities obtained by applying the scalar theorems to every bounded linear functional: (MA.3) permits scalarization, and Hahn–Banach separates two candidate Banach-space values. Similarly, a locally uniform limit of Banach-valued holomorphic functions is holomorphic. To see the latter assertion, take a circle lying inside the common open domain. The vector Cauchy formula passes to the uniform limit on that circle and in its interior. Expanding \((\zeta-z)^{-1}\) as a geometric series on a smaller concentric disc gives a norm-convergent power series for the limit, hence complex differentiability there.

## Gaussian normalization and its Fourier transform

For \(r>0\), put

\[
g_r(t)=\sqrt{\frac r\pi}\,e^{-rt^2}.
\tag{MA.7}
\]

These are probability densities. Indeed, if \(I=\int_{\mathbb R}e^{-t^2}\,dt\), positivity and Fubini give

\[
I^2=\int_{\mathbb R^2}e^{-(x^2+y^2)}\,dx\,dy
=2\pi\int_0^\infty e^{-u^2}u\,du=\pi.
\]

The polar-coordinate Jacobian is \(u\), and the last integral is \(1/2\) by the substitution \(v=u^2\). Thus \(I=\sqrt\pi\), and scaling proves \(\int g_r=1\).

Our Fourier convention is

\[
\widehat f(s)=\int_{\mathbb R}e^{-ist}f(t)\,dt.
\tag{MA.8}
\]

**Gaussian identity.** For every real \(s\),

\[
\int_{\mathbb R}e^{-t^2}e^{-ist}\,dt
=\sqrt\pi\,e^{-s^2/4}.
\tag{MA.9}
\]

**Proof.** Call the left side \(G(s)\). Since \(|t|e^{-t^2}\) is integrable, differentiation under the integral is justified by dominated convergence. Integration by parts, with vanishing boundary terms, gives

\[
\int t e^{-t^2}e^{-ist}\,dt=-\frac{is}{2}G(s),
\qquad G'(s)=-\frac s2G(s).
\]

Hence the derivative of \(e^{s^2/4}G(s)\) is zero. Its value at zero is \(\sqrt\pi\), proving (MA.9). \(\square\)

Scaling and replacing \(s\) by \(-s\) now give the exact inverse formula

\[
g_r(v)=\frac1{2\pi}\int_{\mathbb R}
e^{-s^2/(4r)}e^{isv}\,ds.
\tag{MA.10}
\]

No general Fourier inversion theorem was used to obtain it.

## Fourier uniqueness from Gaussian approximation

**Theorem.** If \(f:\mathbb R\to\mathbb C\) is continuous and integrable, and \(\widehat f(s)=0\) for all real \(s\), then \(f(t)=0\) for every \(t\).

**Proof.** Formula (MA.10) and Fubini give

\[
\begin{aligned}
(f*g_r)(t)
&=\int_{\mathbb R}f(u)g_r(t-u)\,du\\
&=\frac1{2\pi}\int_{\mathbb R}
e^{-s^2/(4r)}e^{ist}\widehat f(s)\,ds=0.
\end{aligned}
\tag{MA.11}
\]

Absolute integrability for the interchange follows from
\(\|f\|_1\int e^{-s^2/(4r)}ds<\infty\).

Fix \(t\) and \(\varepsilon>0\). Continuity supplies \(\delta>0\) such that \(|f(t-v)-f(t)|<\varepsilon\) for \(|v|<\delta\). The integral of this difference against \(g_r\) on that interval is at most \(\varepsilon\). Outside it, the contribution involving \(f(t-v)\) is bounded by

\[
\|f\|_1\sup_{|v|\geq\delta}g_r(v)
=\|f\|_1\sqrt{r/\pi}\,e^{-r\delta^2}\longrightarrow0.
\]

The contribution involving \(f(t)\) is bounded by

\[
\frac{|f(t)|}{\sqrt\pi}
\int_{|u|\geq\delta\sqrt r}e^{-u^2}\,du\longrightarrow0.
\]

Thus \((f*g_r)(t)\to f(t)\), proving the conclusion. The proof did not assume that a continuous integrable function is globally bounded. \(\square\)

**Operator and vector consequence.** Let \(T(t)\) be a uniformly bounded, weak-operator-continuous family in \(B(H)\). If

\[
\int_{\mathbb R}\frac{e^{-ist}}{2\cosh(\pi t)}
\langle T(t)\xi,\eta\rangle\,dt=0
\quad(s\in\mathbb R,\ \xi,\eta\in H),
\tag{MA.12}
\]

then \(T(t)=0\) for every \(t\). Each scalar function
\((2\cosh(\pi t))^{-1}\langle T(t)\xi,\eta\rangle\)
is continuous and integrable, so the theorem makes it identically zero. Its scalar prefactor is strictly positive. Varying \(\xi,\eta\) proves the assertion. The identical argument applies to a bounded weakly continuous Hilbert-space-valued function, by pairing it with arbitrary vectors. Only scalar integrals are needed for these consequences.

## An inverse in a Banach algebra

Let \(B\) be a unital complex Banach algebra, and let \(u:\mathbb C\to\mathrm{GL}(B)\) be entire in norm, with

\[
u(z+w)=u(z)u(w),\qquad
M:=\sup_{t\in\mathbb R}\|u(t)\|<\infty.
\tag{MA.13}
\]

For \(s\in\mathbb R\), define

\[
k_s(t)=\frac{e^{-ist}}{e^{\pi t}+e^{-\pi t}},\qquad
D_s=e^{-s/2}u(-i/2)+e^{s/2}u(i/2).
\tag{MA.14}
\]

**Theorem.** The norm integral

\[
I_s=\int_{\mathbb R}k_s(t)u(t)\,dt
\tag{MA.15}
\]

exists, and \(D_sI_s=I_sD_s=1_B\). Equivalently,

\[
I_s=e^{s/2}u(-i/2)\bigl(u(-i)+e^s1_B\bigr)^{-1}.
\tag{MA.16}
\]

**Proof.** The denominator in \(k_s\) makes it absolutely integrable, since
\((e^{\pi t}+e^{-\pi t})^{-1}\leq e^{-\pi|t|}\).
Norm continuity and (MA.13) therefore give (MA.15) by MA-02.

Consider the meromorphic Banach-valued function

\[
F(z)=\frac{e^{-isz}u(z)}{e^{\pi z}-e^{-\pi z}}.
\tag{MA.17}
\]

On the positively oriented rectangle with vertices \(\pm R\pm i/2\), its only pole inside is \(z=0\), with residue \(1_B/(2\pi)\). Indeed, \(u(0)=1_B\) by the group law and invertibility, and the denominator has derivative \(2\pi\) at zero. The Banach-valued residue identity of MA-02 gives contour integral \(i1_B\).

For \(z=t+ir\), with \(|r|\leq1/2\), the group law gives

\[
\|F(t+ir)\|
\leq\frac{M e^{sr}\|u(ir)\|}
{|e^{\pi(t+ir)}-e^{-\pi(t+ir)}|}.
\tag{MA.18}
\]

The numerator is uniformly bounded on these \(r\)'s. At \(t=\pm R\), the denominator is at least \(e^{\pi R}-e^{-\pi R}\). Thus both vertical contour integrals tend to zero. On the bottom and top edges respectively,

\[
F(t-i/2)=i e^{-s/2}u(-i/2)k_s(t)u(t),
\]

\[
F(t+i/2)=-i e^{s/2}u(i/2)k_s(t)u(t).
\]

The bottom edge runs to the right and the top edge to the left. Taking the limit of their integrals therefore gives \(iD_sI_s=i1_B\). Every value of \(u\) commutes with every other value, by (MA.13). Consequently \(D_s\) commutes with \(I_s\), and it has the asserted two-sided inverse.

Finally,

\[
D_s=e^{-s/2}u(i/2)\bigl(u(-i)+e^s1_B\bigr).
\]

Both \(D_s\) and \(u(i/2)\) are invertible. Inverting this factorization, and using commutation, proves (MA.16). \(\square\)

Taking \(u(z)=e^{i\beta z}\) in \(B=\mathbb C\) yields the scalar formula

\[
\int_{\mathbb R}k_s(t)e^{i\beta t}\,dt
=\frac1{2\cosh((\beta-s)/2)}.
\tag{MA.19}
\]

In particular, \(\int |k_s(t)|dt=\int k_0(t)dt=1/2\). Thus the general inverse satisfies \(\|I_s\|\leq M/2\).

## A spectral resolvent as a strong integral

Let \(A\) be positive, injective and self-adjoint on \(H\). No modular interpretation is required.

**Theorem.** For every real \(s\),

\[
\int_{\mathbb R}k_s(t)A^{it}\,dt
=e^{s/2}A^{1/2}(A+e^sI)^{-1}.
\tag{MA.20}
\]

The integral is vectorwise strong. The right side is the everywhere-defined bounded spectral multiplier

\[
h_s(\lambda)=\frac{e^{s/2}\sqrt\lambda}{\lambda+e^s},
\qquad 0\leq h_s(\lambda)\leq\frac12.
\tag{MA.21}
\]

The displayed composition is also legitimate as an operator product: the resolvent maps \(H\) into \(D(A)\), which is contained in \(D(A^{1/2})\).

**Proof.** Strong continuity of \(A^{it}\) and unitarity give existence of the integral by MA-02. On \(P_nH\), the restriction \(A_n\) is bounded and boundedly invertible. The zero band is trivial. Otherwise \(L_n=\log A_n\) is bounded self-adjoint, and
\(u_n(z)=\exp(izL_n)\)
is an entire group in \(B(P_nH)\), by its norm-convergent exponential series. Real values are unitary. MA-05 gives (MA.20) on this band.

The scalar inequality \(2e^{s/2}\sqrt\lambda\leq\lambda+e^s\) proves (MA.21). Hence the band multipliers converge strongly to \(h_s(A)\). On the integral side, \(A^{it}P_n\xi\to A^{it}\xi\) for every \(t\), and all norms are bounded by \(\|\xi\|\). Equation (MA.6) passes to the full strong integral. The product interpretation follows from the spectral domain criterion and the scalar bounds on \(\lambda/(\lambda+e^s)\) and \(\sqrt\lambda/(\lambda+e^s)\). \(\square\)

## Solving an equation expressed through unbounded pairings

Put

\[
\mathcal D=D(A^{1/2})\cap D(A^{-1/2}).
\tag{MA.22}
\]

This is dense, since it contains every \(P_nH\). For \(X\in B(H)\), define

\[
\mathcal R_s(X)=\int_{\mathbb R}
k_s(t)A^{it}XA^{-it}\,dt.
\tag{MA.23}
\]

The integral exists vectorwise strongly. Indeed, strong continuity of the two unitary groups makes \(t\mapsto A^{it}XA^{-it}\xi\) norm-continuous, and its norm is at most \(\|X\|\|\xi\|\).

**Theorem.** For every \(X\in B(H)\) there is exactly one bounded \(Y\) satisfying

\[
\langle X\xi,\eta\rangle
=\langle YA^{-1/2}\xi,A^{1/2}\eta\rangle
+e^s\langle YA^{1/2}\xi,A^{-1/2}\eta\rangle
\quad(\xi,\eta\in\mathcal D).
\tag{MA.24}
\]

It is

\[
Y=e^{-s/2}\mathcal R_s(X),\qquad
\|Y\|\leq\tfrac12 e^{-s/2}\|X\|.
\tag{MA.25}
\]

No assertion that \(Y\) preserves either unbounded domain is part of (MA.24).

**Proof of uniqueness and the formula.** Suppose (MA.24) holds. Write \(X_n=P_nX|_{P_nH}\), \(Y_n=P_nY|_{P_nH}\). In the Banach algebra of bounded linear maps on the Banach space \(B(P_nH)\), consider

\[
\sigma_z(T)=A_n^{iz}TA_n^{-iz}.
\tag{MA.26}
\]

This is an entire group; for real \(t\), its norm is one on a nonzero band, because conjugation by a unitary is an isometry. The boundedness of \(\log A_n\) justifies entire norm dependence. Restricting (MA.24) to vectors in the band gives

\[
X_n=(\sigma_{-i/2}+e^s\sigma_{i/2})(Y_n).
\tag{MA.27}
\]

For example, the first pairing is the pairing of \(A_n^{1/2}Y_nA_n^{-1/2}\), which is \(\sigma_{-i/2}(Y_n)\). This verifies the signs before applying the inverse formula.

MA-05 in this Banach algebra gives

\[
e^{s/2}Y_n=\int_{\mathbb R}k_s(t)A_n^{it}X_nA_n^{-it}\,dt.
\tag{MA.28}
\]

Extend the band operators by zero on \((I-P_n)H\). Their integrands are \(P_nA^{it}XA^{-it}P_n\), which converge strongly pointwise to \(A^{it}XA^{-it}\) and have norm at most \(\|X\|\). Equation (MA.6) and \(P_nYP_n\to Y\) strongly prove (MA.25). This proves uniqueness; the norm bound follows from \(\|k_s\|_1=1/2\).

**Proof of existence.** Define \(Y\) by (MA.25). Compression by \(P_n\) passes through the vector integrals and identifies \(P_nY|_{P_nH}\) with the right side of (MA.28). The inverse identity in MA-05 consequently proves (MA.27), and hence (MA.24) for pairs of vectors in \(P_nH\).

For general \(\xi,\eta\in\mathcal D\), use \(P_n\xi,P_n\eta\). Spectral convergence (MA.2) holds simultaneously for the constant function \(1\) and for both functions \(\lambda^{1/2}\) and \(\lambda^{-1/2}\). Thus all four unbounded-vector terms in the pairings converge in norm. Since \(X,Y\) are bounded, passing to the limit gives (MA.24) on precisely \(\mathcal D\times\mathcal D\). \(\square\)

This argument also shows

\[
\mathcal R_s(X)^*=\mathcal R_{-s}(X^*).
\tag{MA.29}
\]

It follows by scalarizing the integral and conjugating \(k_s\). For \(s=0\), averaging positive operators proves positivity of \(\mathcal R_0\). Such a positivity claim for general \(s\) would require more: the kernel then has a complex phase.

## Two facts about closed strips

Let \(a>0\), and let

\[
S_a=\{z\in\mathbb C:-a\leq\operatorname{Im}z\leq0\}.
\]

**Boundary uniqueness.** A Banach-valued function continuous on \(S_a\), holomorphic in its interior, and zero on the real boundary is zero on the whole strip.

**Proof.** Scalarize by any bounded linear functional. Near a real point, extend the scalar function by zero into the upper half-plane. The extension is continuous. To verify Morera's condition for a triangle crossing the real line, cut its interior into the portions above and below that line. Replace any segment on the line by a parallel segment at distance \(\varepsilon\) inside the corresponding half-plane. Cauchy's theorem gives zero integrals on the resulting polygonal contours; continuity on the compact triangle makes their boundary integrals converge as \(\varepsilon\downarrow0\). The contributions on the common line cancel. Thus the original triangle has zero integral. Triangles contained in one half-plane already satisfy the condition.

Morera makes the extension holomorphic near the boundary. It vanishes on an open upper half-disc, so the identity theorem makes it zero in that disc and then throughout the connected strip interior. Continuity includes the opposite boundary. Scalar functionals separate values, proving the Banach-valued conclusion. \(\square\)

**Bounded-strip maximum principle.** Suppose a Banach-valued \(F\) is bounded and continuous on \(S_a\), holomorphic inside, and has norm at most \(M\) on both boundary lines. Then \(\|F(z)\|\leq M\) throughout \(S_a\).

**Proof.** Scalarize with a functional of norm at most one, obtaining a bounded scalar function \(f\), say \(|f|\leq C\). Fix \(\varepsilon>0\) and apply the maximum-modulus principle on the rectangle \([-R,R]+i[-a,0]\) to
\(f(z)e^{-\varepsilon z^2}\).
On its horizontal edges the modulus is at most \(Me^{\varepsilon a^2}\). On its vertical edges it is at most \(Ce^{-\varepsilon R^2+\varepsilon a^2}\). If \(M>0\), sufficiently large \(R\) makes the latter bound no larger than the former. For each fixed interior \(z\), this gives

\[
|f(z)|e^{-\varepsilon\operatorname{Re}(z^2)}
\leq Me^{\varepsilon a^2}.
\]

Let \(\varepsilon\downarrow0\). If \(M=0\), apply the same argument with any positive bound \(\delta\) on the horizontal edges and then let \(\delta\downarrow0\). Hahn–Banach recovers the Banach norm from its scalar tests. \(\square\)

Reflecting the variable handles strips above the real line. The boundedness hypothesis in the second assertion cannot be discarded merely because the boundary values are bounded.

## A spectral domain is a strip-extension condition

For \(\alpha\in\mathbb R\), define the closed strip

\[
S_\alpha=\{z:\min(0,-\alpha)\leq\operatorname{Im}z
\leq\max(0,-\alpha)\}.
\tag{MA.30}
\]

**Theorem.** For \(\alpha\ne0\) and \(\xi\in H\), the following are equivalent:

1. \(\xi\in D(A^\alpha)\).
2. The orbit \(t\mapsto A^{it}\xi\) extends to a bounded norm-continuous function \(F:S_\alpha\to H\), norm-holomorphic in the interior.

The extension is unique, and its exact values are

\[
F(z)=A^{iz}\xi,\qquad
F(t-i\alpha)=A^{it}A^\alpha\xi.
\tag{MA.31}
\]

For \(\alpha=0\), the domain is all of \(H\), the strip is the real axis, and the bounded norm-continuous unitary orbit is the entire assertion; interior holomorphy is vacuous.

**Proof for \(\alpha>0\), starting with the domain.** Write \(z=t-iu\), where \(0\leq u\leq\alpha\). If \(\mu_\xi\) is the scalar spectral measure of \(\xi\), then

\[
|\lambda^{iz}|^2=\lambda^{2u}\leq1+\lambda^{2\alpha}.
\]

The right side is integrable by the domain hypothesis. Thus \(A^{iz}\xi\) is defined on the whole strip. On each band,

\[
F_n(z)=A^{iz}P_n\xi
\]

is entire, by the bounded logarithm and its exponential series. The uniform estimate

\[
\sup_{z\in S_\alpha}\|A^{iz}(I-P_n)\xi\|^2
\leq\int_{(0,\infty)\setminus[1/n,n]}
(1+\lambda^{2\alpha})\,d\mu_\xi(\lambda)
\longrightarrow0
\tag{MA.32}
\]

shows uniform convergence on the entire closed strip. Consequently its limit is continuous there, bounded by
\((\|\xi\|^2+\|A^\alpha\xi\|^2)^{1/2}\), and holomorphic inside by MA-02. Spectral multiplication gives the boundary identity in (MA.31).

**Proof starting with the extension.** For each \(n\), the function

\[
G_n(z)=P_nF(z)-A^{iz}P_n\xi
\]

is continuous on the strip, holomorphic inside, and zero on the real boundary. MA-08 gives \(G_n=0\). At the other boundary,

\[
P_nF(-i\alpha)=A^\alpha P_n\xi.
\tag{MA.33}
\]

It follows that

\[
\int_{[1/n,n]}\lambda^{2\alpha}\,d\mu_\xi(\lambda)
=\|A^\alpha P_n\xi\|^2
\leq\|F(-i\alpha)\|^2.
\]

Monotone convergence proves \(\xi\in D(A^\alpha)\). Now (MA.33) and strong convergence of \(P_n\) give \(A^\alpha\xi=F(-i\alpha)\). The first half of the proof supplies the spectral extension, and boundary uniqueness identifies it with \(F\). This also proves uniqueness directly.

For \(\alpha<0\), use the positive injective self-adjoint operator \(A^{-1}\), put \(\beta=-\alpha>0\), and replace \(F(z)\) by \(F(-z)\). Its real orbit is \((A^{-1})^{it}\xi\), and the lower-strip theorem gives the required domain and formulas. No bounded inverse or positive lower spectral bound is inserted. \(\square\)

## Gaussian averages in compact convex sets

Let \(E\) be a locally convex real or complex topological vector space, \(K\subseteq E\) compact and convex, and \(x:\mathbb R\to K\) continuous. For complex \(E\), use its underlying real space in the construction below.

**Theorem.** For every \(r>0\), there is \(x_r\in K\) satisfying

\[
\ell(x_r)=\int_{\mathbb R}g_r(t)\ell(x(t))\,dt
\quad\text{for every continuous real linear functional }\ell.
\tag{MA.34}
\]

Every such choice satisfies \(x_r\to x(0)\) as \(r\to\infty\). If \(E\) is Hausdorff, the choice is unique; it is the barycentric, or weak, integral \(\int g_r(t)x(t)dt\). In a Banach space this agrees with the usual Bochner integral. Completeness of a general locally convex \(E\) is not a hypothesis.

**Proof of existence.** Choose finitely many continuous real linear functionals \(\ell_1,\ldots,\ell_m\). Their joint image \(C\) of \(K\) is a compact convex subset of \(\mathbb R^m\). The vector

\[
v=\left(\int g_r(t)\ell_j(x(t))\,dt\right)_{j=1}^m
\]

belongs to \(C\). To prove this, suppose \(v\notin C\), and choose \(c_0\in C\) minimizing the Euclidean distance to \(v\), which exists by compactness. For \(c\in C\), differentiate the squared distance from \(v\) to \(c_0+t(c-c_0)\) at \(t=0\) from the right. Convexity and minimality give \(\langle v-c_0,c-c_0\rangle\leq0\). The real linear functional \(q(w)=\langle v-c_0,w\rangle\) therefore satisfies
\(q(v)=q(c_0)+\|v-c_0\|^2>\sup_{c\in C}q(c)\).
This contradicts the definition of \(v\) as the integral of points in \(C\) against the probability density \(g_r\).

Thus the closed subsets of \(K\) imposing any finite collection of the equalities (MA.34) have nonempty intersection. Compactness gives a point satisfying them all. In a Hausdorff locally convex space, continuous linear functionals separate points by the seminorm Hahn–Banach theorem, proving uniqueness. More generally any two such points differ by a vector annihilated by every continuous seminorm, so they have the same image in the Hausdorff quotient.

**Proof of convergence.** For every continuous seminorm \(p\), Hahn–Banach gives

\[
p(x_r-x(0))
\leq\int_{\mathbb R}g_r(t)p(x(t)-x(0))\,dt.
\tag{MA.35}
\]

Indeed, for a real linear \(\ell\) with \(|\ell|\leq p\), equation (MA.34) bounds \(|\ell(x_r-x(0))|\) by the right side. The supremum of these tests is \(p(x_r-x(0))\), by seminorm Hahn–Banach.

Compactness of \(K\) bounds the continuous function \(p(\,\cdot-x(0))\) there by some \(C_p\). Given \(\varepsilon>0\), continuity at zero supplies \(\delta>0\) such that \(p(x(t)-x(0))<\varepsilon\) for \(|t|<\delta\). Hence

\[
p(x_r-x(0))\leq\varepsilon+
\frac{C_p}{\sqrt\pi}
\int_{|u|\geq\delta\sqrt r}e^{-u^2}\,du.
\]

The tail tends to zero. Since this holds for every seminorm and every positive \(\varepsilon\), it proves convergence in \(E\), also without Hausdorffness.

If \(E\) is Banach, the compact range is norm bounded. MA-02 constructs the norm integral, which satisfies every scalar equality in (MA.34), and uniqueness identifies it with \(x_r\). \(\square\)

The construction specifies what the integral means in a locally convex space. Merely invoking a Banach-space integration theorem would not establish its existence in an incomplete locally convex space.

## Models that distinguish the domains and topologies

**A sharp two-dimensional bound.** Let \(A=\operatorname{diag}(e^s,1)\) on \(\mathbb C^2\), and take \(X=E_{12}\). Then

\[
A^{it}XA^{-it}=e^{ist}X,
\qquad \mathcal R_s(X)=\tfrac12X.
\]

Thus the solution in MA-07 has norm \(\tfrac12e^{-s/2}\|X\|\). The uniform bound there is sharp. This does not require \(X\) or \(Y\) to be positive.

**Strong continuity without norm continuity.** On \(L^2(\mathbb R)\), let \(A\) be multiplication by \(e^q\), with its maximal spectral domain. Then \(A\) is positive injective self-adjoint and

\[
(A^{it}f)(q)=e^{itq}f(q).
\]

Dominated convergence proves strong continuity. For every \(t\ne0\), however, the essential supremum of \(|e^{itq}-1|\) is two, so \(\|A^{it}-I\|=2\). If \(Rf(q)=f(-q)\), then

\[
A^{it}RA^{-it}=M_{e^{2itq}}R,
\]

which is also norm-discontinuous at zero. These examples explain why MA-06 and MA-07 use vectorwise strong integrals on the full space, even though their spectral-band proofs use norm integrals.

**A missing endpoint domain.** On \(\ell^2(\mathbb N)\), let \(Ae_n=ne_n\) and \(\xi_n=1/n\). Then \(\xi\in H\), but \(\xi\notin D(A^{1/2})\), since \(\sum n|\xi_n|^2=\sum1/n\) diverges. Its real unitary orbit is bounded and continuous. MA-09 nevertheless forbids a bounded continuous holomorphic extension to the closed strip down to \(-i/2\). Continuity of the real orbit alone supplies no nonzero strip width.

## Problems with worked solutions

**Problem 1: verify the conjugation sign in a diagonal model.** Let \(Ae_j=\lambda_j e_j\), with all \(\lambda_j>0\), on a finite-dimensional Hilbert space. Compute \(\mathcal R_s(E_{jk})\) and the corresponding solution of (MA.24).

**Solution.** Conjugation gives
\(A^{it}E_{jk}A^{-it}=e^{it\log(\lambda_j/\lambda_k)}E_{jk}\).
Equation (MA.19) therefore yields

\[
\mathcal R_s(E_{jk})=
\frac{E_{jk}}{2\cosh((\log(\lambda_j/\lambda_k)-s)/2)}.
\]

Multiplying by \(e^{-s/2}\) gives the solution coefficient

\[
\frac1{\sqrt{\lambda_j/\lambda_k}
+e^s\sqrt{\lambda_k/\lambda_j}}.
\]

The two terms of (MA.24) act on \(E_{jk}\) with exactly these two denominator factors. Thus the model independently checks the Fourier phase, the two unbounded-power signs, and the scalar prefactor.

**Problem 2: why the bounded-strip hypothesis matters.** For \(a>0\), construct a scalar function holomorphic on a neighborhood of \(S_a\), with modulus one on both boundary lines, but unbounded inside.

**Solution.** Take

\[
F(z)=\exp\bigl(i e^{\pi z/a}\bigr).
\]

For \(z=t\) and \(z=t-ia\), the inner exponential is real, so \(|F|=1\). On \(z=t-ia/2\), it is \(-i e^{\pi t/a}\), and hence \(|F|=\exp(e^{\pi t/a})\to\infty\). Thus boundary bounds alone do not give the bounded-strip maximum principle of MA-08.

**Problem 3: pointwise Fourier uniqueness needs a pointwise hypothesis.** Give a nonzero integrable function with every Fourier integral zero, and explain why it does not contradict MA-04.

**Solution.** The indicator of the singleton \(\{0\}\) is nonzero at zero but vanishes almost everywhere. Every Lebesgue integral of it, including its Fourier integrals, is zero. It is not continuous at zero. MA-04 uses continuity to turn Gaussian convolution convergence into equality at each point; it does not infer pointwise equality from an almost-everywhere representative without that condition.

**Problem 4: a compact convex average without completeness.** Let \(E=c_{00}(\mathbb N)\) with the norm inherited from \(\ell^2\), let \(v,w\in E\), and let \(h:\mathbb R\to[0,1]\) be continuous. Put \(x(t)=(1-h(t))v+h(t)w\). Construct its Gaussian average inside \(E\).

**Solution.** The segment \(K=\{(1-c)v+cw:0\leq c\leq1\}\) is compact and convex, since it is a continuous image of \([0,1]\). Set \(c_r=\int g_r(t)h(t)dt\in[0,1]\). Then
\(x_r=(1-c_r)v+c_rw\in K\subset E\)
satisfies every scalar average identity, so it is the barycenter of MA-10. The Gaussian tail argument gives \(c_r\to h(0)\), hence \(x_r\to x(0)\) in the inherited norm. The normed space \(c_{00}\) is incomplete, but this compact finite-dimensional range keeps the integral inside it.

## Exported contracts and remaining analytic boundaries

The Banach-algebra inverse is MA-05. Its spectral resolvent specialization is MA-06, and MA-07 gives existence and uniqueness of the bounded solution to the exact weak equation on \(D(A^{1/2})\cap D(A^{-1/2})\). MA-09 identifies spectral domains with closed-strip extensions, including both signs of the exponent and the zero case. MA-10 supplies compact-convex Gaussian averages without completeness. MA-03–04 provide the Gaussian identity and the Fourier uniqueness needed to recover pointwise operator identities from all their scalar Fourier integrals. MA-08 supplies the separate boundary-uniqueness and bounded-strip maximum arguments.

All operator statements preserve arbitrary Hilbert spaces and potentially unbounded inverses. Spectral bands impose bounded spectral ranges, not finite dimension. The exact scalar integration and complex-analysis contracts in MA-01 and the separate spectral kernel retain their own proof obligations. Nothing here proves that a modular unitary group preserves a von Neumann algebra or that modular conjugation exchanges the algebra and its commutant. The final three items give the vector contour and Gaussian continuation forms used when a complex group is initially defined only on a dense algebraic domain.

## Dense scalar tests determine norm holomorphy

**Theorem.** Let \(\Omega\subseteq\mathbb C\) be open, let \(D\subseteq H\) be dense, and let \(F:\Omega\to H\) be locally bounded in norm. If \(z\mapsto\langle F(z),\eta\rangle\) is holomorphic for every \(\eta\in D\), then \(F\) is norm-holomorphic.

**Proof.** Approximate any \(\eta\in H\) in norm by a sequence from \(D\). Local boundedness makes the corresponding scalar functions converge locally uniformly to \(\langle F(z),\eta\rangle\). The scalar Cauchy formula, or its power-series consequence, shows that this limit is holomorphic. Thus every Hilbert scalar test is holomorphic, and in particular continuous.

Fix a closed disc \(\{|z-z_0|\leq R\}\subseteq\Omega\), and bound \(\|F(z)\|\) there by \(C\). For \(n\geq0\), the formula

\[
\langle c_n,\eta\rangle
=\frac1{2\pi i}\oint_{|\zeta-z_0|=R}
\frac{\langle F(\zeta),\eta\rangle}
{(\zeta-z_0)^{n+1}}\,d\zeta
\tag{MA.36}
\]

defines a vector \(c_n\in H\), by the Hilbert Riesz theorem. Indeed the right side is conjugate-linear in \(\eta\), and its modulus is at most \(CR^{-n}\|\eta\|\). Consequently \(\|c_n\|\leq CR^{-n}\), and
\(\sum_{n\geq0}c_n(z-z_0)^n\)
converges in norm on the open disc. Its pairing with every \(\eta\) is the scalar Cauchy expansion of \(\langle F(z),\eta\rangle\); hence the sum equals \(F(z)\). A norm-convergent power series on smaller discs is complex differentiable term by term there, by the same geometric bounds. This proves norm holomorphy. \(\square\)

Here the contour in (MA.36) is initially a scalar integral. Thus the proof does not assume the norm continuity of \(F\) that it is establishing.

## A contour identity on an invariant dense domain

Let \(D\subseteq H\) be a dense complex linear subspace. Suppose maps \(U(z):D\to D\) are linear, satisfy

\[
U(0)=I_D,\qquad U(z+w)=U(z)U(w),
\tag{MA.37}
\]

and for each \(\xi\in D\), \(z\mapsto U(z)\xi\) is norm-entire. It suffices to verify the dense scalar tests and local bounds of MA-14. Assume also that each real \(U(t)\) extends to a bounded operator on \(H\), still denoted \(U(t)\), with

\[
\sup_{t\in\mathbb R}\|U(t)\|\leq M<\infty.
\tag{MA.38}
\]

No bounded operator on \(H\) at a nonreal parameter is assumed.

**Theorem.** The real extensions form a strongly continuous group. For

\[
T_s=\int_{\mathbb R}k_s(t)U(t)\,dt,
\qquad
D_s\xi=e^{-s/2}U(-i/2)\xi+e^{s/2}U(i/2)\xi\quad(\xi\in D),
\tag{MA.39}
\]

one has

\[
T_sD_s\xi=\xi\quad(\xi\in D),\qquad
\overline{\operatorname{ran}D_s}=H.
\tag{MA.40}
\]

For every real \(a\), there is also the density conclusion

\[
\overline{\operatorname{ran}(I_D+U(-ia))}=H.
\tag{MA.41}
\]

These statements do not assert closedness or self-adjointness of the operators initially defined on \(D\).

**Proof.** The group identities for real extensions hold by equality on the dense subspace. On \(D\) their orbits are norm-continuous. For \(\xi\in H\), approximate by \(\eta\in D\) and use

\[
\|(U(t)-U(t_0))\xi\|
\leq2M\|\xi-\eta\|+\|(U(t)-U(t_0))\eta\|.
\]

This proves strong continuity and therefore existence of \(T_s\) by MA-02.

For fixed \(\xi\in D\), apply the rectangle proof of MA-05 to the vector-valued function

\[
z\longmapsto\frac{e^{-isz}U(z)\xi}{e^{\pi z}-e^{-\pi z}}.
\]

Its residue at zero is \(\xi/(2\pi)\). The vertical estimates remain valid, because

\[
\|U(t+ir)\xi\|\leq M\|U(ir)\xi\|,
\]

and the latter vector norm is bounded for \(|r|\leq1/2\) by continuity. The two horizontal integrals give

\[
\xi=\int_{\mathbb R}k_s(t)
\bigl[e^{-s/2}U(t-i/2)\xi+e^{s/2}U(t+i/2)\xi\bigr]\,dt
=T_sD_s\xi.
\tag{MA.42}
\]

The group law on \(D\) also identifies the bracket with \(D_sU(t)\xi\). The vector function in brackets is continuous and uniformly bounded in \(t\), by (MA.38). Thus the integral is a norm limit of finite Riemann sums, each belonging to \(\operatorname{ran}D_s\): the preimage is the same finite linear combination of vectors \(U(t)\xi\in D\). Consequently every \(\xi\in D\) lies in the closure of that range. Density of \(D\) proves (MA.40). This argument does not move a possibly unclosed operator through an integral.

Finally replace the complex group by \(V(z)=U(az)\) and set \(s=0\). Formula (MA.42) becomes

\[
\xi=\int_{\mathbb R}k_0(t)
(I_D+U(-ia))U(at+ia/2)\xi\,dt.
\tag{MA.43}
\]

The two terms of this integrand are \(U(at+ia/2)\xi\) and \(U(at-ia/2)\xi\), so the same continuity and tail bounds apply, also when \(a=0\). Every finite Riemann sum is in \(\operatorname{ran}(I_D+U(-ia))\). Taking its norm limit and then using density proves (MA.41). \(\square\)

One useful consequence makes the range argument concrete. If \(K=U(-ia)\) is positive symmetric on \(D\), it is essentially self-adjoint. Indeed it is closable; its closure \(\overline K\) is positive symmetric and satisfies
\(\|(\overline K+I)\xi\|\geq\|\xi\|\).
If \((\overline K+I)\xi_n\) converges, this inequality makes \(\xi_n\) Cauchy, and closedness of \(\overline K\) identifies its graph limit. Hence the range is closed. Equation (MA.41) makes it all of \(H\). For \(\eta\in D(K^*)\), choose \(\xi\in D(\overline K)\) such that
\((\overline K+I)\xi=(K^*+I)\eta\).
Then \(\eta-\xi\in\ker(K^*+I)=\operatorname{ran}(\overline K+I)^\perp=\{0\}\). Thus \(D(K^*)\subseteq D(\overline K)\), proving self-adjointness. This uses the ordinary adjoint and graph criteria, not a theorem representing unitary groups by generators.

## Gaussian continuation of bounded real orbits

Let \(U(t)\), \(t\in\mathbb R\), be a strongly continuous group on \(H\), with \(\sup_t\|U(t)\|\leq M\). For \(\xi\in H\) and \(r>0\), define

\[
F_r(z)=\int_{\mathbb R}g_r(t-z)U(t)\xi\,dt,
\qquad
g_r(w)=\sqrt{r/\pi}\,e^{-rw^2},\quad z\in\mathbb C.
\tag{MA.44}
\]

**Theorem.** The integral exists in Hilbert norm, \(F_r\) is norm-entire, and

\[
\|F_r(z)\|\leq M e^{r(\operatorname{Im}z)^2}\|\xi\|,
\qquad
U(s)F_r(z)=F_r(z+s)\quad(s\in\mathbb R).
\tag{MA.45}
\]

Moreover \(F_r(0)\to\xi\) in norm as \(r\to\infty\). If \(U(t)=A^{it}\) for a positive injective self-adjoint \(A\), then

\[
F_r(0)\in\bigcap_{\alpha\in\mathbb R}D(A^\alpha),
\qquad A^{iz}F_r(0)=F_r(z)\quad(z\in\mathbb C).
\tag{MA.46}
\]

**Proof.** If \(z=x+iy\), then

\[
|g_r(t-z)|=e^{ry^2}g_r(t-x).
\]

This proves existence and the bound in (MA.45). On a compact set of \(z\)'s, both the kernel and its complex derivative are bounded in modulus by a constant times
\((1+|t|)e^{-rt^2/2}\).
Such a bound follows by expanding \((t-x)^2\) and using \(2|tx|\leq t^2/2+2x^2\). The derivative adds only the factor \(2r(t-z)\). The fundamental theorem of calculus on a small complex line segment and scalar dominated convergence therefore justify differentiating the norm integral. Thus \(F_r\) is entire.

Bounded \(U(s)\) passes through the integral. Substituting \(v=t+s\) and using the group law gives

\[
U(s)F_r(z)=\int g_r(v-(z+s))U(v)\xi\,dv=F_r(z+s).
\]

For convergence at zero, integrate \(U(t)\xi-\xi\) against \(g_r(t)\). Strong continuity makes its norm small near zero; away from zero it is bounded by \((M+1)\|\xi\|\), and the Gaussian tail tends to zero. This proves the norm limit.

For the spectral group, (MA.45) makes \(F_r\) a bounded continuous holomorphic extension on every closed horizontal strip, and its real restriction is \(A^{it}F_r(0)\). Apply MA-09 for each real \(\alpha\). It gives every domain in (MA.46) and identifies the extension at every \(z\). \(\square\)

There is a parallel operator statement useful for algebra-valued averages. If \(X(t)\in N\subseteq B(H)\) is strongly continuous, \(N\) is a von Neumann algebra, and \(\sup_t\|X(t)\|\leq C\), then

\[
X_r(z)=\int_{\mathbb R}g_r(t-z)X(t)\,dt
\tag{MA.47}
\]

is defined vectorwise strongly, belongs to \(N\), has norm at most \(Ce^{r(\operatorname{Im}z)^2}\), and is **operator-norm entire** in \(z\). Membership in \(N\) follows by approximating the integrals by their finite Riemann sums, which lie in \(N\), and taking strong limits; the uniform scalar tail bound handles the infinite interval. The kernel difference quotients converge in scalar \(L^1\) by the derivative bound just proved. The estimate (MA.5) then shows convergence of the corresponding operator difference quotients in norm, proving the holomorphy assertion despite the original family's merely strong continuity. If \(X(t)=V(t)XV(-t)\) for a unitary group normalizing \(N\), the change of variable above gives the same real covariance for \(X_r(z)\). These conclusions do not assert that arbitrary imaginary conjugations of the unsmoothed operator are defined.
