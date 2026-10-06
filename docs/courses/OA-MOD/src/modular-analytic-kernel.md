# Analytic kernels for unbounded modular operators

**Self-checked by the writing AI.**

An unbounded power need not commute with a bounded operator or preserve its range. We formulate the required equation as a pairing on its exact common domain. A strip integral then solves it through bounded operators. The same analytic tools construct entire vectors and identify their actual power domains.

The free human references are Rieffel and Van Daele, [*A bounded operator approach to Tomita–Takesaki theory*, Lemmas 4.6–4.8](https://msp.org/pjm/1977/69-1/pjm-v69-n1-p17-s.pdf), and Brent Nelson, [*Tomita–Takesaki Theory*, Definition 2.1, Lemmas 2.3–2.4 and the proof of Theorem 2.2](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf). The written strip formula used below is IK1. The arguments here include the domain, convergence and completeness steps needed for their stated conclusions; the references do not stand in for those proofs.

## Conventions and exact analytic inputs

The inner product is linear in its first variable. Hilbert spaces need not be separable. Throughout the spectral statements, \(A\) is positive, injective and self-adjoint; its inverse may be unbounded. Powers use the real logarithm of a positive scalar. Write

\[
P_n=1_{[1/n,n]}(A),\qquad n\geq1.
\tag{MA.1}
\]

The written spectral-domain and multiplication proofs SK-05, SK-07 and SK-09 give \(P_n\to I\) strongly and, for every \(\xi\in D(f(A))\),

\[
P_n\xi\to\xi,\qquad f(A)P_n\xi\to f(A)\xi.
\tag{MA.2}
\]

They also construct the strongly continuous unitaries \(A^{it}\). A spectral band has bounded spectral range; no finite-dimensionality is assumed.

The scalar prerequisites are written in complex analysis, closed-boundary formulas SC1–SC5, scalar integration, and products and substitutions PI1–PI7. In particular PI6 proves Gaussian normalization, PI3 proves the absolutely integrable Fubini theorem, and PI7 proves the integration-by-parts formula with its endpoint conditions. These supply the interfaces named MA-DEP-SCALAR-COMPLEX and MA-DEP-SCALAR-INTEGRATION. We only use the explicitly proved rectangle, disc and simple-pole forms of complex integration.

Complete normed spaces, scalar completeness and the usual set-theoretic maximal principle are foundational conventions. MA-02 proves the separation statements needed for general Banach and locally convex spaces. For Hilbert representation in MA-14, the earlier real projection and Riesz proof supplies the real theorem, and MA-14 gives its complex conversion. The spectral and bounded-operator prerequisites remain separately identified; this chapter does not by itself certify the whole programme's transitive proof closure.

## Which integrals take values in which space

**Separation used in this chapter.** Let \(p\) be a finite sublinear function on a real vector space, and \(f\leq p\) a linear functional on a subspace \(D\). For \(x\notin D\), an extension with value \(a\) at \(x\) is dominated by \(p\) exactly when

\[
\sup_{d\in D}\{f(d)-p(d-x)\}\leq a
\leq\inf_{e\in D}\{p(e+x)-f(e)\}.
\]

Every left expression is at most every right expression: use
\(f(d+e)\leq p(d+e)\leq p(d-x)+p(e+x)\).
The bounds are finite on the required side by taking \(d=0\) or \(e=0\). A real \(a\) between them therefore exists. Positive and negative scalar multiples of \(x\) reduce the domination check to these two inequalities. Order all dominated extensions by inclusion. A chain has its union as a dominated extension, so the maximal principle gives an extension to the whole space; otherwise the one-dimensional construction would enlarge it.

In particular, for a seminorm \(p\) and a vector \(v\), start on \(\mathbb Rv\) with \(f(tv)=t p(v)\). The extension satisfies \(|f|\leq p\) and \(f(v)=p(v)\). If \(p\) is continuous, this functional is continuous. It follows that continuous real functionals recover every continuous seminorm and separate points in a Hausdorff locally convex space. On a complex normed space, extend a real functional \(f\) and set \(L(x)=f(x)-if(ix)\). Direct substitution proves complex linearity and \(\operatorname{Re}L=f\). If \(|f(x)|\leq\|x\|\), rotate \(x\) by a scalar of modulus one so that \(L\) has nonnegative real value; then \(|L(x)|\leq\|x\|\). Starting with \(f(v)=\|v\|\) gives \(L(v)=\|v\|\). Thus complex continuous functionals of norm at most one recover the norm as well. These are the separation and norming statements used below.

Let \(f:[a,b]\to B\) be continuous, with \(B\) Banach. For two sufficiently fine tagged partitions, compare their sums on the common refinement. The norm of the difference is at most \((b-a)\) times the sum of the two continuity moduli. Uniform continuity and completeness give the Riemann integral. Comparing sums with sums of scalar norms proves

\[
\left\|\int_a^b f(t)\,dt\right\|\leq\int_a^b\|f(t)\|\,dt.
\tag{MA.3}
\]

If \(f:\mathbb R\to B\) is norm-continuous and \(\|f(t)\|\leq m(t)\) for an integrable scalar \(m\), the compact-interval integrals form a Cauchy family: each omitted tail has norm at most its scalar \(m\)-integral. Their limit defines the improper norm integral. This is the Bochner integral in the present continuous setting. Bounded linear maps pass through it, first on finite sums and then on limits.

For a strongly continuous operator family with \(\sup_t\|T(t)\|\leq C\) and continuous \(k\in L^1(\mathbb R)\), define instead

\[
T_k\xi=\int_{\mathbb R}k(t)T(t)\xi\,dt.
\tag{MA.4}
\]

Each integral is in \(H\); linearity and (MA.3) give

\[
\|T_k\|\leq C\|k\|_1.
\tag{MA.5}
\]

This is a vectorwise strong integral, without an operator-norm continuity assumption. If \(T_j(t)\to T(t)\) strongly pointwise along a sequence, with the same bound \(C\), scalar dominated convergence gives, for every \(\xi\),

\[
\left\|\int k(t)(T_j(t)-T(t))\xi\,dt\right\|
\leq\int |k(t)|\,\|(T_j(t)-T(t))\xi\|\,dt\longrightarrow0.
\tag{MA.6}
\]

All vector functions being integrated here are continuous. This sequential integration statement places no countability restriction on the Hilbert space.

Parametrizing a finite piecewise smooth path gives its Banach-valued integral and the path-length norm estimate. Scalar Cauchy formulas, SC1's rectangle identity and SC5's one-pole identity pass to Banach-valued holomorphic functions by testing with the separating functionals just proved. A locally uniform limit is holomorphic too: pass its circle Cauchy formula to the limit, expand the Cauchy kernel on a smaller disc, and use its geometric majorant to obtain a norm-convergent power series with termwise derivative. Each passage is controlled by (MA.3).

## Gaussian normalization and its Fourier transform

Set

\[
g_r(t)=\sqrt{r/\pi}\,e^{-rt^2},\qquad r>0,
\tag{MA.7}
\]

and use the Fourier convention

\[
\widehat f(s)=\int_{\mathbb R}e^{-ist}f(t)\,dt.
\tag{MA.8}
\]

PI6.6 proves \(\int e^{-t^2}dt=\sqrt\pi\) by the proved product and polar formulas; the absolute-value dilation formula PI5.1 gives \(\int g_r=1\).

For \(G(s)=\int e^{-t^2}e^{-ist}dt\), difference quotients are dominated near each real \(s\) by \(|t|e^{-t^2}\). Thus \(G'(s)=-i\int t e^{-t^2}e^{-ist}dt\). Apply PI7.2 to \(e^{-t^2}\) and \(e^{-ist}\). Both product-derivative terms are integrable and their endpoint product is zero. It yields
\(\int t e^{-t^2}e^{-ist}dt=-isG(s)/2\), so \(G'=-sG/2\). The derivative of \(e^{s^2/4}G(s)\) vanishes; finite-interval calculus and its value at zero give

\[
G(s)=\sqrt\pi e^{-s^2/4}.
\tag{MA.9}
\]

Changing scale in this identity proves directly

\[
g_r(v)=\frac1{2\pi}\int_{\mathbb R}e^{-s^2/(4r)}e^{isv}\,ds.
\tag{MA.10}
\]

All these integrals are absolutely convergent. Formula (MA.10) is a calculation for this kernel, not an invocation of general Fourier inversion.

## Fourier uniqueness from Gaussian approximation

**Theorem.** A continuous integrable scalar function whose Fourier transform vanishes everywhere is zero everywhere.

Insert (MA.10) into the convolution with \(g_r\). The absolute double integral is at most \(\|f\|_1\int e^{-s^2/(4r)}ds/(2\pi)\), so PI3 permits the interchange:

\[
(f*g_r)(t)=\frac1{2\pi}\int e^{-s^2/(4r)}e^{ist}\widehat f(s)\,ds=0.
\tag{MA.11}
\]

To identify its pointwise limit, fix \(t\) and \(\varepsilon>0\). On \(|v|<\delta\), continuity makes \(|f(t-v)-f(t)|<\varepsilon\), and the contribution is at most \(\varepsilon\). The remaining \(f(t-v)\) contribution is at most \(\|f\|_1\sqrt{r/\pi}e^{-r\delta^2}\). The remaining constant contribution is at most \(|f(t)|\pi^{-1/2}\int_{|u|\geq\delta\sqrt r}e^{-u^2}du\). Both tend to zero, so \(f*g_r(t)\to f(t)\). This also proves the theorem for continuous integrable functions that are not globally bounded.

For a uniformly bounded weak-operator-continuous family \(T(t)\), suppose

\[
\int_{\mathbb R}\frac{e^{-ist}}{2\cosh(\pi t)}
\langle T(t)\xi,\eta\rangle\,dt=0
\quad(s\in\mathbb R,\ \xi,\eta\in H).
\tag{MA.12}
\]

Apply the theorem to \(\langle T(t)\xi,\eta\rangle/(2\cosh\pi t)\), which is continuous and integrable. Its positive denominator never vanishes, so every coefficient of \(T(t)\) is zero for every \(t\). Hence \(T(t)=0\). The same proof, with Hilbert pairings, applies to a bounded weakly continuous vector function. A countable separating family is unnecessary.

## An inverse in a Banach algebra

Let \(B\) be a unital complex Banach algebra. Suppose \(u:\mathbb C\to\mathrm{GL}(B)\) is norm-entire and

\[
u(z+w)=u(z)u(w),\qquad M=\sup_{t\in\mathbb R}\|u(t)\|<\infty.
\tag{MA.13}
\]

For real \(s\), put

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

is the two-sided inverse of \(D_s\), and

\[
I_s=e^{s/2}u(-i/2)(u(-i)+e^s1_B)^{-1}.
\tag{MA.16}
\]

Use the already proved strip formula IK1.3 at \(\phi=0\). Its Banach-valued version follows by MA-02: boundary integrals converge in norm, scalar testing gives IK1.3, and functionals separate the values. Apply it to

\[
f(\zeta)=e^{-s\zeta}u(-i\zeta),\qquad |\operatorname{Re}\zeta|\leq\tfrac12.
\tag{MA.17}
\]

Writing \(\zeta=a+it\), the group law gives

\[
\|f(a+it)\|\leq M e^{|s|/2}
\max_{|b|\leq1/2}\|u(-ib)\|.
\tag{MA.18}
\]

The maximum is finite by continuity. Also \(u(0)=1_B\), since it is invertible and idempotent. At the right boundary the strip integrand is \(e^{-s/2}k_s(t)u(-i/2)u(t)\), and at the left it is \(e^{s/2}k_s(t)u(i/2)u(t)\). Therefore IK1 gives \(1_B=D_sI_s\). The group law makes all values of \(u\) commute; passing commutation through the integral gives \(I_sD_s=1_B\). Finally
\(D_s=e^{-s/2}u(i/2)(u(-i)+e^s1_B)\); inversion of this product proves (MA.16).

The scalar specialization \(u(z)=e^{i\beta z}\) yields

\[
\int k_s(t)e^{i\beta t}dt=\frac1{2\cosh((\beta-s)/2)}.
\tag{MA.19}
\]

In particular \(\|k_s\|_1=1/2\), and \(\|I_s\|\leq M/2\). The integral existence used above follows already from \(|k_s(t)|\leq e^{-\pi|t|}\) and MA-02.

## A spectral resolvent as a strong integral

For every real \(s\),

\[
\int_{\mathbb R}k_s(t)A^{it}dt
=e^{s/2}A^{1/2}(A+e^sI)^{-1}.
\tag{MA.20}
\]

The integral is vectorwise strong. The scalar function on the right is

\[
h_s(\lambda)=\frac{e^{s/2}\sqrt\lambda}{\lambda+e^s},\qquad
0\leq h_s(\lambda)\leq\tfrac12.
\tag{MA.21}
\]

The bound follows from \((\sqrt\lambda-e^{s/2})^2\geq0\).

To prove the formula, set \(\beta=\log\lambda\) in (MA.19). On each compact interval \([1/n,n]\), the functions \((t,\lambda)\mapsto k_s(t)\lambda^{it}\) are jointly continuous for bounded \(t\). Uniform Riemann approximation and the bounded continuous-calculus norm estimate commute each finite integral with the calculus on \(P_nH\). The tail is uniformly at most \(\int_{|t|>L}|k_s(t)|dt\), so the same equality holds for the whole integral on this band. Now \(P_n\to I\), the multipliers (MA.21) are uniformly bounded, and (MA.6) passes the identity to all of \(H\). The actual resolvent has range \(D(A)\); spectral multiplication and \(D(A)\subset D(A^{1/2})\) identify its displayed composition with \(h_s(A)\). Thus no merely formal unbounded product has been used.

## Solving an equation expressed through unbounded pairings

Let

\[
\mathcal V=D(A^{1/2})\cap D(A^{-1/2}),
\tag{MA.22}
\]

and, for \(X\in B(H)\), define

\[
\mathcal R_s(X)=\int_{\mathbb R}k_s(t)A^{it}XA^{-it}dt.
\tag{MA.23}
\]

The orbit is strongly continuous: insert and subtract \(A^{it}XA^{-iu}\xi\) to estimate its difference at \(t,u\). Each integrand has norm at most \(\|X\|\), so MA-02 constructs the integral.

**Theorem.** There is exactly one bounded \(Y\) for which

\[
\langle X\xi,\eta\rangle
=\langle YA^{-1/2}\xi,A^{1/2}\eta\rangle
+e^s\langle YA^{1/2}\xi,A^{-1/2}\eta\rangle
\quad(\xi,\eta\in\mathcal V).
\tag{MA.24}
\]

It is

\[
Y=e^{-s/2}\mathcal R_s(X),\qquad
\|Y\|\leq\tfrac12e^{-s/2}\|X\|.
\tag{MA.25}
\]

Here is a bounded proof of both existence and uniqueness. Set
\(R=2(I+A)^{-1}\), \(C=R^{1/2}\), \(D=(2I-R)^{1/2}\), and \(T=CD\). The spectral domain formulas give

\[
\mathcal V=\operatorname{ran}T,\qquad
A^{1/2}T=D^2,\qquad A^{-1/2}T=C^2.
\tag{MA.26}
\]

For the converse inclusion in the range assertion, if \(\xi\in\mathcal V\), put \(u=(A^{1/2}+A^{-1/2})\xi/2\). The bounded scalar multiplier \(T(\lambda)=2\sqrt\lambda/(1+\lambda)\) gives \(Tu=\xi\). The other inclusion and the two equalities follow from the same scalar products with their actual domains. The operator \(T\) is injective with dense range, since its scalar function is strictly positive and \(A\) is injective.

Substitute \(\xi=Tu\), \(\eta=Tv\) into the pairings. Equation (MA.24) is exactly

\[
TXT=D^2YC^2+e^sC^2YD^2.
\tag{MA.27}
\]

To invert this bounded equation, let
\(B_\zeta=R^{1/2-\zeta}(2I-R)^{1/2+\zeta}\)
on \(|\operatorname{Re}\zeta|\leq1/2\). The bounded functions defining these operators have norm at most two. They are strongly continuous up to the boundary and norm-holomorphic inside. The proof is the scalar estimate of IK2: after multiplying by \(R(2I-R)\), endpoint values vanish uniformly on compact parameter sets, and this operator has dense range; inside, the exponential Taylor remainder is bounded by a constant times \(|h|^2 r^{\delta/2}(1+|\log r|^2)\) near an endpoint. The latter is bounded and tends to zero. The bounded calculus passes both estimates to operators. These arguments use only \(0\leq R\leq2I\) and injectivity of \(R,2I-R\), which hold here.

One has \(B_0=T\), \(B_{1/2+it}=D^2A^{it}\) and \(B_{-1/2+it}=C^2A^{it}\). Apply IK1 to each scalar pairing of \(e^{-s\zeta}B_\zeta W B_{-\zeta}\), for any bounded \(W\). The family is bounded on the vertical strip and has the continuity just proved. Its boundary terms give

\[
TWT=e^{-s/2}D^2\mathcal R_s(W)C^2
       +e^{s/2}C^2\mathcal R_s(W)D^2.
\tag{MA.28}
\]

Taking \(W=X\) proves that (MA.25) satisfies (MA.27), hence (MA.24) on the whole stated domain. Conversely, if \(Y\) satisfies (MA.27), the same strip formula with \(W=Y\) has the boundary sum
\(e^{-s/2}k_s(t)A^{it}(TXT)A^{-it}\).
It follows that \(TYT=e^{-s/2}T\mathcal R_s(X)T\). Density of \(\operatorname{ran}T\) identifies the bounded operators, giving (MA.25). Its norm bound is (MA.5). No inverse of \(T\) is moved through an operator and no invariance of an unbounded domain under \(Y\) is asserted.

Taking scalar adjoints of the integral also gives

\[
\mathcal R_s(X)^*=\mathcal R_{-s}(X^*).
\tag{MA.29}
\]

For \(s=0\) the kernel is positive, so the map preserves positivity. A nonzero phase parameter does not supply that positivity conclusion.

![Bounded coordinates for the weak equation and its strip-integral solution.](../../audit/real-coercivity/figures/analytic-weak-equation.svg)

**Figure.** Every vector in the common domain is represented as \(Tu\). Its two half-power images are the bounded coordinates \(D^2u\) and \(C^2u\). Substituting both test vectors gives (MA.27); the strip argument (MA.28) supplies both existence and uniqueness, without commuting an unbounded operator through \(Y\). Reproducible figure source.

## Two facts about closed strips

Let \(S_a=\{z:-a\leq\operatorname{Im}z\leq0\}\), \(a>0\). A Banach-valued function continuous on \(S_a\), holomorphic inside and zero on the real boundary is zero everywhere on the strip. To prove this, test with a continuous linear functional and extend the resulting scalar function by zero just above the boundary. Every small rectangle crossing the boundary has zero contour integral: split it there, use the continuous-boundary Cauchy formula SC1 on the lower part, and note that the upper part is zero. The shared edges cancel. Rectangle Morera SC3 makes the extension holomorphic. The identity theorem applies to its open set of zeros above the boundary and then to the connected strip interior. Continuity includes its lower boundary. MA-02's separation gives the vector assertion.

If a continuous holomorphic \(F\) on this closed strip is globally bounded, and \(\|F\|\leq M\) on both boundary lines, then \(\|F\|\leq M\) throughout. For a scalar test \(f\) of norm at most one, write \(|f|\leq C\). On the rectangle \([-L,L]+i[-a,0]\), apply SC4 to \(f(z)e^{-\varepsilon z^2}\). The horizontal bound is \(Me^{\varepsilon a^2}\); the vertical bound is \(Ce^{-\varepsilon L^2+\varepsilon a^2}\). First let \(L\to\infty\) with an interior point fixed, and then let \(\varepsilon\downarrow0\). The resulting scalar bound is \(|f(z)|\leq M\), also when \(M=0\). Norming functionals from MA-02 prove the claimed Banach norm bound. The change of variable \(z\mapsto-z\) gives the corresponding upper-strip results.

## A spectral domain is a strip-extension condition

For real \(\alpha\), set

\[
S_\alpha=\{z:\min(0,-\alpha)\leq\operatorname{Im}z\leq\max(0,-\alpha)\}.
\tag{MA.30}
\]

**Theorem.** For \(\alpha\ne0\), a vector \(\xi\) belongs to \(D(A^\alpha)\) if and only if its real orbit \(A^{it}\xi\) extends to a bounded norm-continuous function on \(S_\alpha\), norm-holomorphic inside. The extension is unique and

\[
F(z)=A^{iz}\xi,\qquad F(t-i\alpha)=A^{it}A^\alpha\xi.
\tag{MA.31}
\]

For \(\alpha=0\), the domain is all of \(H\) and the assertion is just the bounded continuous real orbit; there is no strip interior.

First let \(\alpha>0\). If \(\xi\in D(A^\alpha)\), its scalar spectral measure satisfies \(\int(1+\lambda^{2\alpha})d\mu_\xi<\infty\). For \(z=t-iu\), \(0\leq u\leq\alpha\), one has \(\lambda^{2u}\leq1+\lambda^{2\alpha}\). Thus the bandwise entire functions \(A^{iz}P_n\xi\) obey

\[
\sup_{z\in S_\alpha}\|A^{iz}(I-P_n)\xi\|^2
\leq\int_{(0,\infty)\setminus[1/n,n]}(1+\lambda^{2\alpha})d\mu_\xi
\longrightarrow0.
\tag{MA.32}
\]

Their uniform limit is bounded and continuous on the entire strip and holomorphic inside by MA-02. Multiplication of the spectral functions gives (MA.31).

Conversely, for an extension \(F\), the two functions \(P_nF(z)\) and \(A^{iz}P_n\xi\) agree on the real boundary. MA-08's uniqueness gives equality throughout, hence

\[
P_nF(-i\alpha)=A^\alpha P_n\xi.
\tag{MA.33}
\]

Now \(P_n\xi\to\xi\) and the right side converges to \(F(-i\alpha)\). Closedness of the spectral power, already proved in SK-05, gives \(\xi\in D(A^\alpha)\) and identifies its image. Uniqueness on the rest of the strip is again MA-08. This converse needs no unjustified passage of a power through a boundary limit. For \(\alpha<0\), apply the positive case to \(A^{-1}\), exponent \(-\alpha\), and the function \(F(-z)\); all domains are transported, and no bounded inverse is assumed.

## Gaussian averages in compact convex sets

Let \(E\) be a real or complex locally convex space, \(K\subset E\) compact and convex, and \(x:\mathbb R\to K\) continuous. Completeness and Hausdorffness are not required for existence. For \(r>0\) there is \(x_r\in K\) such that

\[
\ell(x_r)=\int g_r(t)\ell(x(t))dt
\quad\text{for every continuous real linear functional }\ell.
\tag{MA.34}
\]

Every such choice tends to \(x(0)\) as \(r\to\infty\). In a Hausdorff space it is unique, and in a Banach space it equals the norm integral.

For a direct construction, partition \([-n,n)\) into intervals of length \(1/n\). Assign to the left endpoint of each interval its scalar Gaussian mass, and assign the remaining mass to \(x(0)\). The resulting finite convex combination \(y_n\) belongs to \(K\). For every continuous real \(\ell\), its integrand is \(\ell(x(\lfloor nt\rfloor/n))\) on \([-n,n)\) and \(\ell(x(0))\) outside. It converges pointwise to \(\ell(x(t))\) and is bounded by the maximum of \(|\ell|\) on \(K\). Scalar dominated convergence proves that \(\ell(y_n)\) tends to the right side of (MA.34). The closed subsets \(\overline{\{y_n:n\geq N\}}^{K}\) of the compact space \(K\) have the finite intersection property. Any point in their intersection satisfies all these scalar limits: every closed scalar interval about a limit contains a sufficiently late tail and hence its closure. This proves existence even if compactness is not sequential compactness.

For every continuous seminorm \(p\), the norming real functionals proved in MA-02 give

\[
p(x_r-x(0))\leq\int g_r(t)p(x(t)-x(0))dt.
\tag{MA.35}
\]

Indeed (MA.34) bounds each functional dominated by \(p\), and their supremum is the seminorm. The scalar function on the right is bounded because \(K\) is compact. It is small near zero by continuity, while the Gaussian mass outside any fixed neighbourhood tends to zero by (MA.7). This proves convergence in every continuous seminorm. Those same functionals show uniqueness in the Hausdorff case and uniqueness in the Hausdorff quotient otherwise. In a Banach space, MA-02's norm integral satisfies (MA.34), so uniqueness identifies it with \(x_r\).

## Models that distinguish the domains and topologies

**Sharp constant.** On \(\mathbb C^2\), take \(A=\operatorname{diag}(e^s,1)\), \(X=E_{12}\). Multiplication gives \(A^{it}XA^{-it}=e^{ist}X\). Formula (MA.19) therefore gives \(\mathcal R_s(X)=X/2\), and (MA.25) attains \(e^{-s/2}/2\). The norm of \(E_{12}\) is one: its action preserves the norm on the second coordinate and cannot increase any norm.

**Strong and norm continuity differ.** On \(L^2(\mathbb R)\), let \(A\) be multiplication by \(e^q\) on its maximal domain. The spectral multiplier construction gives positivity, injectivity and self-adjointness. Its unitary group is multiplication by \(e^{itq}\); dominated convergence against \(|f(q)|^2dq\) proves strong continuity. If \(t\ne0\), every neighbourhood of a point with \(tq\) an odd multiple of \(\pi\) has positive measure. Testing unit vectors supported in such bounded neighbourhoods makes \(\|(A^{it}-I)f\|\) arbitrarily close to two. The reverse inequality is the unitary triangle bound, so \(\|A^{it}-I\|=2\). Reflection \(Vf(q)=f(-q)\) is unitary by the proved change of variable and satisfies \(A^{it}VA^{-it}=M_{e^{2itq}}V\). This orbit too is norm-discontinuous at zero. The vectorwise integrals in MA-06–07 apply to it.

**An endpoint domain is an additional condition.** In \(\ell^2(\mathbb N)\), let \(Ae_n=ne_n\) and \(\xi_n=1/n\). The series of squared coordinates converges, since \(n^{-2}\leq1/(n(n-1))\) for \(n\geq2\) and the latter telescopes. But \(\sum n|\xi_n|^2=\sum1/n\) diverges: each dyadic block from \(2^k\) to \(2^{k+1}-1\) contributes at least \(1/2\). Hence \(\xi\notin D(A^{1/2})\). Its bounded continuous real orbit cannot have the bounded continuous extension to the closed half-strip of MA-09.

## Problems with worked solutions

**1. Check all signs in a matrix entry.** Suppose \(Ae_j=\lambda_j e_j\), with \(\lambda_j>0\), in finite dimension. Find the solution of (MA.24) for \(X=E_{jk}\).

Conjugation multiplies this matrix entry by \(e^{it\log(\lambda_j/\lambda_k)}\). Thus (MA.19) and (MA.25) give

\[
\mathcal R_s(E_{jk})=\frac{E_{jk}}{2\cosh((\log(\lambda_j/\lambda_k)-s)/2)},
\qquad
Y=\frac{E_{jk}}{\sqrt{\lambda_j/\lambda_k}+e^s\sqrt{\lambda_k/\lambda_j}}.
\]

Direct multiplication in (MA.24) gives precisely the two denominator factors, checking both half-power signs and the Fourier phase.

**2. Is a boundary bound enough?** On \(S_a\), the entire function
\(F(z)=\exp(i e^{\pi z/a})\)
has modulus one on both boundary lines, because the inner exponential is real there. At \(z=t-ia/2\), however, its modulus is \(\exp(e^{\pi t/a})\), which is unbounded. This verifies the need for global boundedness in MA-08's maximum statement.

**3. Does Fourier uniqueness identify every representative?** The indicator of \(\{0\}\) is nonzero at zero and has every Fourier integral zero, since it vanishes almost everywhere. It fails MA-04's continuity hypothesis. The proof there identifies pointwise values only through that hypothesis and Gaussian convergence.

**4. An average inside an incomplete space.** Let \(E=c_{00}(\mathbb N)\) with its \(\ell^2\) norm, choose \(v,w\in E\), and put \(x(t)=(1-h(t))v+h(t)w\) for continuous \(h:\mathbb R\to[0,1]\). Its range is in the compact segment joining \(v,w\). For \(c_r=\int g_rh\), the vector \(x_r=(1-c_r)v+c_rw\) remains in that segment and satisfies (MA.34). The scalar Gaussian estimate gives \(c_r\to h(0)\). Thus the integral stays in this incomplete space because its compact convex range supplies existence, as proved in MA-10.

## Exported contracts and remaining analytic boundaries

MA-05 supplies a Banach-algebra inverse. MA-06 gives the actual bounded spectral resolvent, and MA-07 solves the weak equation on the full intersection of the half-power domains, with its sharp norm constant. MA-09 identifies domains with closed-strip extensions for both signs of the exponent, including the zero case separately. MA-10 constructs compact-convex Gaussian averages without a completeness assumption. MA-03–04 prove the Gaussian identity and pointwise Fourier uniqueness. MA-08 distinguishes boundary uniqueness from the bounded-strip maximum principle.

The scalar programme proofs linked in MA-01 are actual inputs to these arguments. The spectral, Hilbert-space and other course prerequisites are not proved in this chapter. The following three results address a complex group initially given only on a dense algebraic domain. None of the results in this chapter assumes a modular commutant theorem.

## Dense scalar tests determine norm holomorphy

**Theorem.** Let \(D\subset H\) be dense, \(\Omega\subset\mathbb C\) open and \(F:\Omega\to H\) locally bounded. If \(\langle F(z),\eta\rangle\) is holomorphic for every \(\eta\in D\), then \(F\) is norm-holomorphic.

Approximate each \(\eta\in H\) by vectors of \(D\). Local boundedness gives locally uniform convergence of their scalar tests; the scalar Cauchy theorem then proves holomorphy for every test vector. On a closed disc of radius \(R\) about \(z_0\), let \(\|F\|\leq C\). For each \(n\geq0\), define

\[
\langle c_n,\eta\rangle=\frac1{2\pi i}\oint_{|\zeta-z_0|=R}
\frac{\langle F(\zeta),\eta\rangle}{(\zeta-z_0)^{n+1}}d\zeta.
\tag{MA.36}
\]

The scalar right side is conjugate-linear in \(\eta\) and bounded by \(CR^{-n}\|\eta\|\). For completeness, its representing vector follows from the written real Riesz theorem: represent its real part by \(\operatorname{Re}\langle c_n,\eta\rangle\); evaluating at \(i\eta\) identifies the imaginary part because both functionals are conjugate-linear. Thus \(c_n\) exists and \(\|c_n\|\leq CR^{-n}\). The series \(\sum c_n(z-z_0)^n\) converges in norm for \(|z-z_0|<R\); scalar Cauchy expansions identify all its pairings with those of \(F\). Hence it equals \(F\). On each smaller disc, the geometric bounds also give uniform convergence of the derivative series, proving norm holomorphy. No vector contour integral of an as-yet unproved continuous \(F\) was assumed.

## A contour identity on an invariant dense domain

Let \(D\subset H\) be dense and complex linear. Suppose \(U(z):D\to D\) is linear, every vector orbit is norm-entire, and

\[
U(0)=I_D,\qquad U(z+w)=U(z)U(w).
\tag{MA.37}
\]

Suppose the real values extend to bounded operators with

\[
\sup_{t\in\mathbb R}\|U(t)\|\leq M<\infty.
\tag{MA.38}
\]

Their real group law holds by density. If \(\xi\in H\) and \(\eta\in D\), the inequality
\(\|(U(t)-U(t_0))\xi\|\leq2M\|\xi-\eta\|+\|(U(t)-U(t_0))\eta\|\)
proves strong continuity. Consequently

\[
T_s=\int k_s(t)U(t)dt,\qquad
D_s\xi=e^{-s/2}U(-i/2)\xi+e^{s/2}U(i/2)\xi
\tag{MA.39}
\]

are respectively a bounded vectorwise integral and an operator on \(D\).

**Theorem.** One has

\[
T_sD_s\xi=\xi\quad(\xi\in D),\qquad
\overline{\operatorname{ran}D_s}=H,
\tag{MA.40}
\]

and, for every real \(a\),

\[
\overline{\operatorname{ran}(I_D+U(-ia))}=H.
\tag{MA.41}
\]

Apply the vector strip formula as in MA-05 to \(e^{-s\zeta}U(-i\zeta)\xi\). Its vertical-strip bound is \(M e^{|s|/2}\max_{|b|\leq1/2}\|U(-ib)\xi\|\). Its boundary identity is

\[
\xi=\int k_s(t)[e^{-s/2}U(t-i/2)\xi+e^{s/2}U(t+i/2)\xi]dt
=T_sD_s\xi.
\tag{MA.42}
\]

The bracket equals \(D_sU(t)\xi\). Finite Riemann sums therefore belong to \(\operatorname{ran}D_s\). Their norm limit is \(\xi\), since the two boundary orbits are continuous and bounded and \(k_s\) is integrable. Hence the range is dense. This conclusion does not move a possibly unclosed \(D_s\) through an integral.

Apply the same identity to \(z\mapsto U(az)\), with \(s=0\). It becomes

\[
\xi=\int k_0(t)(I_D+U(-ia))U(at+ia/2)\xi\,dt.
\tag{MA.43}
\]

Its finite sums belong to the stated range and converge in norm by the same two bounded-orbit estimates. This proves (MA.41), including \(a=0\).

If \(K=U(-ia)\) is positive symmetric on \(D\), it is essentially self-adjoint. Indeed, symmetry on a dense domain proves closability: if \(\xi_n\to0\) and \(K\xi_n\to y\), then \(\langle y,\eta\rangle=\lim\langle\xi_n,K\eta\rangle=0\) for \(\eta\in D\), so \(y=0\). Its closure remains positive symmetric and satisfies \(\|(I+\overline K)\xi\|\geq\|\xi\|\). This bound and closedness make its range closed: a convergent image sequence gives convergent first coordinates and then graph convergence. Equation (MA.41) makes the range all of \(H\). For \(\eta\in D(K^*)\), solve \((I+\overline K)\xi=(I+K^*)\eta\). The difference \(\eta-\xi\) is in the kernel of \(I+K^*\), which is the orthogonal complement of the range of \(I+\overline K\). It is zero. Thus \(D(K^*)\subset D(\overline K)\), proving self-adjointness of the closure. This argument proves the needed core conclusion directly.

## Gaussian continuation of bounded real orbits

Let \(U(t)\) be a strongly continuous group on \(H\) with \(\sup_t\|U(t)\|\leq M\). For \(r>0\), \(\xi\in H\), define

\[
F_r(z)=\int_{\mathbb R}g_r(t-z)U(t)\xi\,dt,\qquad
g_r(w)=\sqrt{r/\pi}e^{-rw^2}.
\tag{MA.44}
\]

This norm integral is entire and obeys

\[
\|F_r(z)\|\leq M e^{r(\operatorname{Im}z)^2}\|\xi\|,\qquad
U(s)F_r(z)=F_r(z+s)\quad(s\in\mathbb R).
\tag{MA.45}
\]

Moreover \(F_r(0)\to\xi\). For the spectral group \(U(t)=A^{it}\),

\[
F_r(0)\in\bigcap_{\alpha\in\mathbb R}D(A^\alpha),\qquad
A^{iz}F_r(0)=F_r(z)\quad(z\in\mathbb C).
\tag{MA.46}
\]

To verify every passage, write \(z=x+iy\). Then \(|g_r(t-z)|=e^{ry^2}g_r(t-x)\), which gives existence and the norm bound. On a fixed compact parameter set, the kernel and its complex derivative are bounded by a constant times \((1+|t|)e^{-rt^2/2}\). This follows from \(2|tx|\leq t^2/2+2x^2\) and the derivative factor \(2r(t-z)\). Finite-segment calculus expresses a difference quotient as the average of those derivatives along the segment. Dominated convergence and (MA.3) then prove convergence in norm of the difference quotient to the derivative integral. This proves entire dependence. Passing the bounded \(U(s)\) through the integral and substituting \(v=t+s\) proves covariance. For convergence at zero, integrate \(U(t)\xi-\xi\): continuity controls a fixed neighbourhood, and its complement is bounded by \((M+1)\|\xi\|\) times the Gaussian tail. Finally (MA.45) supplies a bounded extension on every closed strip with the correct real orbit, so MA-09 gives every actual domain and identity in (MA.46).

If \(X(t)\) is strongly continuous in a von Neumann algebra \(N\subset B(H)\), with \(\sup_t\|X(t)\|\leq C\), then

\[
X_r(z)=\int g_r(t-z)X(t)dt
\tag{MA.47}
\]

is a vectorwise strong integral in \(N\), satisfies \(\|X_r(z)\|\leq Ce^{r(\operatorname{Im}z)^2}\), and is operator-norm entire. Finite sums lie in \(N\), and their strong limits commute with every member of \(N'\): pass each fixed bounded operator through the vector limits. Since \(N=N''\), those limits stay in \(N\). The uniform tail bound handles the infinite interval. The derivative majorant above also proves convergence of the scalar kernel difference quotients in \(L^1\); multiplying that difference by \(C\) through (MA.5) proves operator-norm differentiability. For \(X(t)=V(t)XV(-t)\), where a unitary group normalizes \(N\), the same substitution proves real covariance. These results do not assign an undefined imaginary conjugation to an unsmoothed operator.
