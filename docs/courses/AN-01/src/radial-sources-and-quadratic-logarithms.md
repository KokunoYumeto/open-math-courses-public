# Radial sources and quadratic logarithms

*Reconstructed by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The equation away from a singular point does not determine the source at that point. We calculate that source by integrating over a small surrounding sphere. This produces complex quadratic logarithms, inverses of the squared Laplacian, entire families of radial exponentials, and the point term in their second derivatives.

Throughout, \(\Delta=\sum_j\partial_j^2\), distributions act complex-linearly on \(C_c^\infty\), and integration uses ordinary Lebesgue density. Set \(r=|x|\) and \(\sigma_{n-1}=|\mathbb S^{n-1}|\). The earlier programme proofs used below, including the foundations of integration and matrix algebra, are identified at the end. Every additional identity needed here is proved below.

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods.

## A logarithm for a complex quadratic form

Write a complex symmetric two by two matrix as \(A=P+iQ\), where \(P,Q\) are real symmetric. Our hypotheses are

\[
\begin{aligned}
P&\geq0,\qquad q_A(x)=x^TAx,\\
q_A(x)&\ne0\quad(x\in\mathbb R^2\setminus\{0\}).
\end{aligned}
\tag{1.1}
\]

The logarithm is the branch on \(\mathbb C\setminus(-\infty,0]\) with \(\log1=0\). To obtain it from the fully constructed slit logarithm \(\operatorname{Log}\) preceding Theorem 4.1 in [Causal integration of complex order](causal-integration-of-complex-order.md), put \(\log z=\operatorname{Log}(-z)-i\pi\). That construction uses arguments in \((0,2\pi)\); the present branch therefore uses \((-\pi,\pi)\), has derivative \(1/z\), and satisfies \(\log(sz)=\log s+\log z\) for \(s>0\). Its arguments on the nonzero closed right half-plane lie in \([-\pi/2,\pi/2]\), so it is defined on every value \(q_A(x)\) in (1.1).

The determinant root \(g(A)\) is the matrix function of [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Lemma 2.1. It is positive on real positive definite matrices, has square \(\det A\), and extends continuously to invertible matrices with nonnegative real part. Choosing a scalar square root of \(\det A\) afresh need not give this function.

**Theorem 1.1 (the complex quadratic source).** Under (1.1), \(A\) is invertible. With the preceding choices,

\[
\begin{aligned}
L_A&=a_{22}\partial_1^2-2a_{12}\partial_1\partial_2
       +a_{11}\partial_2^2,\\
E_A(x)&=\frac{\log q_A(x)}{4\pi g(A)},\\
L_AE_A&=\delta_0.
\end{aligned}
\tag{1.2}
\]

The logarithm belongs to \(L^1_{\mathrm{loc}}\), as does its classical gradient away from zero. That gradient is also its full weak gradient.

**Proof.** If \(Az=0\), then \(0=\operatorname{Re}(z^*Az)=z^*Pz\). Orthogonal diagonalization of \(P\), proved in U020, Lemma 2.1, implies \(Pz=0\); hence \(Qz=0\). For \(z\ne0\), at least one of its real and imaginary parts would be a nonzero real common null vector \(w\) of \(P,Q\). This would give \(q_A(w)=0\), contradicting (1.1). Therefore \(\det A\ne0\), and the stated matrix-root lemma applies.

Compactness of the unit circle gives \(m=\min_{|\omega|=1}|q_A(\omega)|>0\). The selected logarithm satisfies

\[
\log q_A(r\omega)=2\log r+\log q_A(\omega).
\tag{1.3}
\]

The second summand is bounded. Since \(\int_0^1r|\log r|\,dr<\infty\), this defines a locally integrable function. The chain rule gives, off zero,

\[
\nabla\log q_A(x)=\frac{2Ax}{q_A(x)}=O(r^{-1}).
\tag{1.4}
\]

This gradient is locally integrable in two dimensions. Apply integration by parts on the complement of a radius-\(\varepsilon\) disk, inside a larger disk where the test vanishes. The boundary error for the first derivative is at most \(C\varepsilon(1+|\log\varepsilon|)\|\phi\|_\infty\). It tends to zero, proving the weak-gradient assertion.

Multiply that gradient by the adjugate:

\[
\begin{aligned}
J(x)&=\operatorname{adj}(A)\nabla\log q_A(x)
       =\frac{2\det(A)x}{q_A(x)},\\
\operatorname{div}J(x)&=0\quad(x\ne0).
\end{aligned}
\tag{1.5}
\]

Indeed \(\operatorname{adj}(A)A=\det(A)I\), while
\(\operatorname{div}(x/q_A)=2/q_A-(x\cdot\nabla q_A)/q_A^2=0\).
The distribution \(L_A\log q_A\) is \(\operatorname{div}J\). Green's formula, proved in Boundary flux and weak identities, Corollary 2.2, gives
\[
-\int_{r>\varepsilon}J\cdot\nabla\phi\,dx
=2\det(A)\int_0^{2\pi}
       \frac{\phi(\varepsilon\omega_\theta)}{q_A(\omega_\theta)}\,d\theta.
\]
Here \(\omega_\theta=(\cos\theta,\sin\theta)\); the normal of the punctured domain is \(-\omega_\theta\), accounting for the positive sign. The difference between the last integral and its value with \(\phi(0)\) is bounded by \(C\varepsilon\|\nabla\phi\|_\infty/m\). Thus

\[
\begin{aligned}
L_A\log q_A&=2\det(A)I_A\delta_0,\\
I_A&=\int_0^{2\pi}\frac{d\theta}{q_A(\omega_\theta)}.
\end{aligned}
\tag{1.6}
\]

For \(P>0\), the fully proved complex Gaussian formula in U020, Theorem 3.1, at dimension two, zero frequency and time one, is

\[
\int_{\mathbb R^2}e^{-q_A(x)}\,dx=\frac{\pi}{g(A)}.
\tag{1.7}
\]

The integrand is absolutely integrable, so polar Fubini applies. For \(\operatorname{Re}q>0\),
\(\int_0^\infty e^{-qr^2}r\,dr=1/(2q)\), by the antiderivative and exponential decay. Hence (1.7) is \(I_A/2=\pi/g(A)\). For a matrix on the semidefinite boundary use \(A+\eta I\), \(\eta>0\). On the circle \(q_{A+\eta I}=q_A+\eta\), so for \(0<\eta<m/2\) the denominators have absolute value at least \(m/2\). Dominated convergence and continuity of \(g\) give \(I_A=2\pi/g(A)\) also there. Inserting \(g(A)^2=\det A\) in (1.6) proves (1.2). \(\square\)

For real positive definite \(A\), writing \(\rho(x)=\sqrt{x^TAx}\) changes the logarithm to \(2\log\rho\). The coefficient of this radial logarithm is \(1/(2\pi\sqrt{\det A})\).

**Example 1.2 (a coupled boundary matrix).** Consider

\[
A=\begin{pmatrix}2&i\\i&i\end{pmatrix},
\qquad \det A=1+2i.
\tag{1.8}
\]

Here \(q_A=2x_1^2+2ix_1x_2+ix_2^2\). A zero has real part \(2x_1^2=0\), and then imaginary part \(x_2^2=0\), so (1.1) holds. To specify the root, calculate
\(\det(A+\eta I)=(1+\eta)^2+i(2+\eta)\), always in the first quadrant for \(\eta\geq0\).
The canonical root has \(g(A+\eta I)/\eta\to1\) as \(\eta\to\infty\): positive scaling and continuity give
\(g(A+\eta I)=\eta g(I+A/\eta)\). Positive scaling itself follows because \(g(sM)/(s\,g(M))\) has square one, depends continuously on \(s>0\), and equals one at \(s=1\). The continuous root on this path therefore has positive real part for all \(\eta\geq0\). Consequently

\[
E_A(x)=\frac{\log q_A(x)}{4\pi\sqrt{1+2i}},
\qquad \operatorname{Re}\sqrt{1+2i}>0,
\tag{1.9}
\]

has unit source for \(i\partial_1^2-2i\partial_1\partial_2+2\partial_2^2\).

## Integrate the Newton source once more

Theorem 1.1 of U020 proves, with the present sign convention, that for every \(n>2\)

\[
\Phi_n(r)=\frac{r^{2-n}}{(2-n)\sigma_{n-1}},
\qquad \Delta\Phi_n=\delta_0.
\tag{2.1}
\]

It also proves the planar identity \(\Delta(\log r/(2\pi))=\delta_0\). These are global distribution identities.

**Theorem 2.1 (the fourth-order radial source).** In dimension \(n>2\), define

\[
\begin{aligned}
B_n(r)&=\frac{r^{4-n}}{2(4-n)(2-n)\sigma_{n-1}}
            &&(n\ne4),\\
B_4(r)&=-\frac{\log r}{8\pi^2}.
\end{aligned}
\tag{2.2}
\]

Then

\[
\Delta B_n=\Phi_n,\qquad \Delta^2B_n=\delta_0.
\tag{2.3}
\]

**Proof.** The identities \(\partial_jr=x_j/r\) and
\(\partial_j^2r=1/r-x_j^2/r^3\) imply
\(\Delta f(r)=f''(r)+(n-1)f'(r)/r\) for \(r>0\). In particular,

\[
\Delta r^\alpha=\alpha(\alpha+n-2)r^{\alpha-2}.
\tag{2.4}
\]

When \(n\ne4\), substitution into (2.2) gives \(\Delta B_n=\Phi_n\) off zero. Polar integration bounds the absolute radial integrals of \(B_n,\nabla B_n,\Phi_n\) near zero respectively by constants times
\(\int_0^1r^3\,dr,\int_0^1r^2\,dr,\int_0^1r\,dr\).
For a compactly supported test, the two boundary terms in Green's formula are

\[
\begin{aligned}
\int_{r>\varepsilon}(B_n\Delta\phi-\phi\Delta B_n)\,dx
&=-\int_{r=\varepsilon}B_n\,\partial_r\phi\,dS\\
&\quad+\int_{r=\varepsilon}\phi\,\partial_rB_n\,dS.
\end{aligned}
\tag{2.5}
\]

Their absolute values are \(O(\varepsilon^3)\|\nabla\phi\|_\infty\) and
\(O(\varepsilon^2)\|\phi\|_\infty\). Both vanish, proving the global first equality.

For \(n=4\), the sphere formula proved in [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A5, gives \(\sigma_3=2\pi^2\), and the radial derivative gives \(\Delta\log r=2/r^2\) off zero. Thus (2.2) again differentiates to \(\Phi_4=-1/(4\pi^2r^2)\). Its local integrability is immediate from \(r^3|\log r|\,dr\). The two terms in (2.5) now have bounds \(C\varepsilon^3|\log\varepsilon|\) and \(C\varepsilon^2\). This proves the first equality also in dimension four. Applying the already global identity (2.1) proves the second equality in every case. \(\square\)

**Example 2.2 (opposite signs in dimensions three and five).** The sphere areas are
\(\sigma_2=4\pi\) and \(\sigma_4=8\pi^2/3\), by A5. Consequently

\[
B_3(r)=-\frac{r}{8\pi},\qquad
B_5(r)=\frac{1}{16\pi^2r}.
\tag{2.6}
\]

In dimension three, \(\Delta r=2/r\), so \(\Delta B_3=-1/(4\pi r)=\Phi_3\).
In dimension five, \(\Delta r^{-1}=-2r^{-3}\), so
\(\Delta B_5=-1/(8\pi^2r^3)=\Phi_5\).
Both second Laplacians are exactly \(\delta_0\). The factor \(4-n\) in (2.2) accounts for the change of sign.

The planar analogue is

\[
B_2(r)=\frac{r^2\log r-r^2}{8\pi},
\qquad \Delta B_2=\frac{\log r}{2\pi}.
\tag{2.7}
\]

Indeed \(B_2'=(2r\log r-r)/(8\pi)\) and
\(B_2''=(2\log r+1)/(8\pi)\), giving (2.7) off zero. The boundary terms of (2.5) are now bounded by
\(C\varepsilon^3(1+|\log\varepsilon|)\) and
\(C\varepsilon^2(1+|\log\varepsilon|)\). They tend to zero, while the bulk terms are locally integrable. Therefore (2.7) holds globally and the planar Newton identity gives \(\Delta^2B_2=\delta_0\).

## A radial exponential retains the same source

We now work in \(\mathbb R^3\). Compact tests allow arbitrary complex exponential parameters without a growth condition at infinity.

**Theorem 3.1 (every complex radial parameter).** The locally integrable family

\[
u_a(x)=\frac{e^{a|x|}}{|x|},\qquad a\in\mathbb C,
\tag{3.1}
\]

is weakly entire, meaning that \(\langle u_a,\phi\rangle\) is entire for every compact test \(\phi\). Its full Laplacian is

\[
\Delta u_a=a^2u_a-4\pi\delta_0.
\tag{3.2}
\]

**Proof.** If \(|a|\leq M\) and the test is supported in \(r\leq R\), the \(k\)-th parameter derivative of the integrand is bounded by
\(e^{MR}r^{k-1}|\phi(x)|\). The polar measure \(r^2\,dr\,d\omega\) makes this integrable for every \(k\geq0\). Difference quotients are dominated by the same bound with \(M\) slightly enlarged: use
\((e^{hr}-1)/h=r\int_0^1e^{thr}\,dt\).
Dominated convergence proves complex differentiability and every higher derivative, uniformly on compact parameter sets.

For \(r>0\), direct differentiation gives
\(u_a'=e^{ar}(a/r-1/r^2)\) and
\(u_a''=e^{ar}(a^2/r-2a/r^2+2/r^3)\).
Hence \(\Delta u_a=u_a''+2u_a'/r=a^2u_a\) there.
Use (2.5) with \(u_a\) in place of \(B_n\). The first boundary integral is \(O(\varepsilon)\|\nabla\phi\|_\infty\). In the second one,
\(\varepsilon^2u_a'(\varepsilon)=e^{a\varepsilon}(a\varepsilon-1)\to-1\), uniformly for \(a\) in compact sets. Its limit is
\(-\int_{\mathbb S^2}\phi(0)\,d\omega=-4\pi\phi(0)\).
The two bulk terms converge by local integrability. This proves (3.2) directly for every complex \(a\). \(\square\)

The spatial scaling provides a separate check on the source coefficient. Define dilation on tests by

\[
\begin{aligned}
\langle T(s\,\cdot),\phi\rangle
   &=s^{-3}\langle T,\phi(\,\cdot/s)\rangle,\\
\delta_0(s\,\cdot)&=s^{-3}\delta_0\qquad(s>0).
\end{aligned}
\tag{3.3}
\]

Applying the chain rule to the test proves
\(\partial_j[T(s\,\cdot)]=s(\partial_jT)(s\,\cdot)\).
Since \(u_{-s}=s\,u_{-1}(s\,\cdot)\), (3.2) at \(a=-1\) gives

\[
\Delta u_{-s}
=s^3(\Delta u_{-1})(s\,\cdot)
=s^2u_{-s}-4\pi\delta_0.
\tag{3.4}
\]

For completeness, the entire scalar function

\[
F_\phi(a)=\langle u_a,\Delta\phi\rangle
       -a^2\langle u_a,\phi\rangle+4\pi\phi(0)
\tag{3.5}
\]

vanishes identically by the direct proof. One could also deduce this from (3.4) and the proved identity principle in [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2. The boundary limit responsible for the coefficient in either argument is

\[
\varepsilon^2u_a'(\varepsilon)
=e^{a\varepsilon}(a\varepsilon-1)\longrightarrow-1.
\tag{3.6}
\]

## Cancel and shift the radial source

**Corollary 4.1 (the removable oscillatory profile).** Extending \(\sin r/r\) to value one at the origin gives a smooth function on \(\mathbb R^3\) with

\[
\Delta\left(\frac{\sin r}{r}\right)=-\frac{\sin r}{r}.
\tag{4.1}
\]

**Proof.** Off zero this function is \((u_i-u_{-i})/(2i)\). The equality also holds between the associated locally integrable distributions. The two point masses in (3.2) cancel, and \(i^2=(-i)^2=-1\), proving the weak equation.
The exponential series gives

\[
\frac{\sin r}{r}
=\sum_{k=0}^\infty\frac{(-1)^k(|x|^2)^k}{(2k+1)!}.
\tag{4.2}
\]

Here convergence holds with every spatial derivative on compact sets. To check this explicitly, expand
\((x_1^2+x_2^2+x_3^2)^k\) by the multinomial formula; the sum of its nonnegative coefficients is \(3^k\). On \(|x_j|\leq R\), a derivative of order \(m\) is bounded by
\(3^k(2k)^m\max(1,R)^{2k}\) for \(k\geq1\), and is zero if its order exceeds the degree. After division by \((2k+1)!\) these bounds sum, by the ratio test. Repeated fundamental theorems of calculus identify the differentiated sum with the derivatives. Thus the extension is smooth. Equality of its weak and classical derivatives proves (4.1) also at zero. \(\square\)

**Theorem 4.2 (two entire Helmholtz sources).** For \(a\in\mathbb C\), set

\[
E_a^\pm(x)=-\frac{e^{\pm ia|x|}}{4\pi|x|}.
\tag{4.3}
\]

Both are weakly entire fundamental families for \(Q_a=\Delta+a^2\):

\[
Q_aE_a^\pm=\delta_0.
\tag{4.4}
\]

Their difference is the smooth homogeneous solution

\[
E_a^+-E_a^-=-\frac{i}{2\pi}\frac{\sin(a|x|)}{|x|}.
\tag{4.5}
\]

**Proof.** Substitute \(ia\) and \(-ia\) in Theorem 3.1 and multiply by \(-1/(4\pi)\). This proves (4.4) and entire dependence. Subtraction gives (4.5) and its homogeneous equation. The series for \(\sin(ar)/r\) has terms
\((-1)^ka^{2k+1}(|x|^2)^k/(2k+1)!\).
The derivative estimate in Corollary 4.1, multiplied by powers of a bound for \(|a|\), proves uniform convergence with all spatial and parameter derivatives on compact sets. Its value at zero is \(a\). Therefore (4.5) has value \(-ia/(2\pi)\) there and is smooth everywhere. \(\square\)

At \(a=0\) both kernels equal \(\Phi_3=-1/(4\pi r)\). At \(a=i\), the plus kernel is \(-e^{-r}/(4\pi r)\) and solves \((\Delta-1)E_i^+=\delta_0\). These are identities including the origin. They impose no radiation condition or uniqueness requirement at infinity.

## Exercises

**Exercise 1 (basic).** *An off-diagonal real source.*

Find a logarithmic fundamental solution of \(3\partial_1^2-2\partial_1\partial_2+2\partial_2^2\). Explain the factor of two between quadratic and radial logarithms.

**Solution 1.** Choose \(A=\left(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\right)\).
The quadratic form is \(q(x)=2(x_1+x_2/2)^2+(5/2)x_2^2>0\) for \(x\ne0\). Thus \(A\) is positive definite, \(\det A=5\), and \(g(A)=\sqrt5\). The adjugate produces the stated operator, so Theorem 1.1 gives

\[
E(x)=\frac{\log(2x_1^2+2x_1x_2+3x_2^2)}{4\pi\sqrt5}.
\tag{5.1}
\]

The full distributional source is \(\delta_0\). Since \(\rho=\sqrt{q}\) is positive off zero and \(\log q=2\log\rho\), the coefficient of \(\log\rho\) is \(1/(2\pi\sqrt5)\). \(\square\)

**Exercise 2 (basic).** *A square root that reverses the source.*

For \(A=-iI_2\), determine the correct source kernel and the error caused by using the principal scalar square root of \(\det A\).

**Solution 2.** U020, Lemma 2.1, proves
\(g(iH)=|\det H|^{1/2}e^{i\pi\operatorname{sgn}(H)/4}\) for invertible real symmetric \(H\).
For \(H=-I_2\), this gives \(g(A)=-i\). In contrast, \(\det A=-1\) has principal scalar root \(i\).
The chosen logarithm is \(\log(-ir^2)=2\log r-i\pi/2\); hence

\[
E(x)=\frac{i}{2\pi}\log r+\frac18,\qquad L_A=-i\Delta.
\tag{5.2}
\]

The planar Newton identity gives \(L_AE=\delta_0\). Replacing the denominator root \(-i\) by \(i\) changes \(E\) to \(-E\), including its constant, and changes the source to \(-\delta_0\). Both functions still satisfy the homogeneous equation away from zero. \(\square\)

**Exercise 3 (intermediate).** *A neutral pair for a fourth-order operator.*

For fixed \(h\in\mathbb R^3\setminus\{0\}\), solve \(\Delta^2U=\delta_h-\delta_{-h}\) using a radial kernel. Determine the limit of \(U(R\omega)\) as \(R\to\infty\), \(|\omega|=1\).

**Solution 3.** For a distribution \(T\), define its translate by
\((\tau_hT)(\phi)=T(\phi(\,\cdot+h))\). Differentiating this test identity shows that translation commutes with every constant-coefficient derivative, and \(\tau_h\delta_0=\delta_h\). Therefore

\[
U(x)=-\frac{|x-h|-|x+h|}{8\pi}
\tag{5.3}
\]

has the requested source by (2.6). This is locally integrable at both centers.
For sufficiently large \(R\),
\[
|R\omega\mp h|
=R\sqrt{1\mp2\omega\cdot h/R+|h|^2/R^2}
=R\mp\omega\cdot h+O(R^{-1}).
\]
The remainder is uniform in \(\omega\), since the second derivative of the square root is bounded on a fixed interval about one. Subtracting gives

\[
\lim_{R\to\infty}U(R\omega)=\frac{\omega\cdot h}{4\pi}.
\tag{5.4}
\]

Thus a neutral pair can have a nonzero direction-dependent limit. \(\square\)

**Exercise 4 (intermediate).** *Length scale at the logarithmic dimension.*

For \(\rho>0\), let \(B_{4,\rho}(x)=-\log(|x|/\rho)/(8\pi^2)\). Find its source and dilation law. Can a rotation-invariant locally integrable function homogeneous of degree zero be a fundamental solution of \(\Delta^2\) in \(\mathbb R^4\)?

**Solution 4.** The difference \(B_{4,\rho}-B_4\) is the constant
\(\log\rho/(8\pi^2)\). Thus \(\Delta B_{4,\rho}=\Phi_4\) and
\(\Delta^2B_{4,\rho}=\delta_0\). For \(s>0\),

\[
B_{4,\rho}(sx)=B_{4,\rho}(x)-\frac{\log s}{8\pi^2}.
\tag{5.5}
\]

We prove the claimed obstruction at the level of distributions, so that no simultaneous choice of almost-everywhere representatives is assumed. Let \(T\) be rotation invariant and homogeneous of degree zero. The Euler criterion in [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), Lemma 1.1, gives
\(\mathcal ET=0\), where \(\mathcal E=\sum_i x_i\partial_i\).
Differentiating a rotation in the \((i,j)\)-plane gives
\((x_i\partial_j-x_j\partial_i)T=0\).
This differentiation is legitimate directly on tests: the rotated tests have common compact support for small angles; the chain rule and Taylor's formula give convergence of their difference quotients in every derivative seminorm. Transposing gives the stated generator equation; the generator has zero divergence.

The following identity uses multiplication of distributional derivatives, so involves no regularity assumption on \(T\):
\[
|x|^2\partial_jT
=x_j\mathcal ET+\sum_i x_i(x_i\partial_j-x_j\partial_i)T=0.
\]
It follows that all derivatives \(\partial_jT\) vanish on \(\mathbb R^4\setminus\{0\}\), where division by the smooth nonzero function \(|x|^2\) is allowed.

Here are the details that zero derivatives force a constant. Fix a ball whose closure avoids zero and choose a slightly larger such ball. Local convolution with a smooth unit-integral mollifier, justified in [Convolution as addition of supports](convolution-as-addition-of-supports.md), Proposition 5.1 and Theorem 5.2, produces smooth functions \(T_\varepsilon\) on the smaller ball, with zero gradient. Integrating their derivative on line segments shows \(T_\varepsilon=c_\varepsilon\) there. For a fixed test \(\psi\) in that ball with integral one, distributional convergence gives
\(c_\varepsilon=\langle T_\varepsilon,\psi\rangle\to\langle T,\psi\rangle=c\).
Consequently \(T(\phi)=c\int\phi\) for every test in the ball. Constants on intersecting balls agree, by a unit-integral test in their intersection.

Any two nonzero points in \(\mathbb R^4\) can be joined by two line segments avoiding zero: choose an intermediate point outside the two lines through the origin and those points. Cover this compact path by finitely many intersecting balls avoiding zero. The preceding agreement proves that \(T\) is one constant on the punctured space. If \(T\) comes from an \(L^1_{\mathrm{loc}}\) function, uniqueness of that representation, also proved by local mollification in U021, makes the function equal to this constant almost everywhere off zero. A point has Lebesgue measure zero, so \(T\) is that same constant globally. Hence \(\Delta^2T=0\), which cannot equal \(\delta_0\). The logarithmic dilation term in (5.5) cannot be removed within this radial function class. \(\square\)

**Exercise 5 (intermediate).** *Compact forcing without a global growth restriction.*

For \(f\in C_c^\infty(\mathbb R^3)\), prove that \(v_a=E_a^+*f\) is smooth, solves \(Q_av_a=f\), and depends entirely on \(a\) with all spatial derivatives locally uniform. Give a nonzero smooth homogeneous solution for every \(a\).

**Solution 5.** Write \(v_a(x)=\int E_a^+(y)f(x-y)\,dy\). For \(x\) in a compact set \(K\), the integrand vanishes unless \(y\in K-\operatorname{supp}f\), another compact set. For \(|a|\leq M\), its kernel is bounded by \(e^{M|y|}/(4\pi|y|)\), integrable on that set. Every spatial derivative can therefore be put on \(f\), giving

\[
\partial^\alpha v_a=E_a^+*(\partial^\alpha f).
\tag{5.6}
\]

Every parameter derivative adds a power of \(|y|\), still with an integrable common bound. The integral difference-quotient argument in Theorem 3.1 proves entire dependence and locally uniform convergence with every spatial derivative. The proper-support convolution and differentiation theorem, U021, Theorem 1.1, gives
\(Q_av_a=(Q_aE_a^+)*f=\delta_0*f=f\).

Define

\[
S_a(x)=
\begin{cases}
\displaystyle\frac{\sin(a|x|)}{a|x|},&a\ne0,\\
1,&a=0.
\end{cases}
\tag{5.7}
\]

Its series \(\sum_{k\geq0}(-1)^ka^{2k}(|x|^2)^k/(2k+1)!\) and the estimates of Corollary 4.1 prove smoothness, entire dependence and \(S_a(0)=1\). For \(a\ne0\), (4.5) gives \(Q_aS_a=0\); at \(a=0\) this is simply \(\Delta1=0\). Thus every \(v_a+cS_a\) solves the same inhomogeneous equation. \(\square\)

**Exercise 6 (advanced).** *An ellipsoid with a negative determinant.*

For every \(a\in\mathbb C\), find a fundamental solution of \(G:D^2+a^2\), where

\[
B=\begin{pmatrix}1&1&0\\0&2&0\\0&0&-3\end{pmatrix},
\qquad G=BB^T.
\tag{5.8}
\]

Use ordinary Lebesgue density and give the source Jacobian.

**Solution 6.** Matrix multiplication gives
\(G=\left(\begin{smallmatrix}2&2&0\\2&4&0\\0&0&9\end{smallmatrix}\right)\), so the operator is
\(2\partial_1^2+4\partial_1\partial_2+4\partial_2^2+9\partial_3^2+a^2\).
The inverse substitution \(x=By\) gives

\[
\rho_B(x)^2=|B^{-1}x|^2
=(x_1-x_2/2)^2+x_2^2/4+x_3^2/9.
\tag{5.9}
\]

For clarity, define the pullback of any distribution \(T\) by
\(\langle T(B^{-1}\,\cdot),\phi\rangle
=|\det B|\langle T,\phi(B\,\cdot)\rangle\).
This is a distribution, since test composition preserves compact supports and bounds every derivative seminorm by a fixed finite sum of seminorms. For a locally integrable function it agrees with ordinary substitution by the proved linear change-of-variables formula.
On smooth tests,
\[
\Delta_y[\phi(By)]
=\sum_{j,k}(BB^T)_{jk}(\partial_j\partial_k\phi)(By).
\]
Transposing this exact identity proves
\((G:D_x^2)[T(B^{-1}\,\cdot)]=(\Delta_yT)(B^{-1}\,\cdot)\).
In particular,

\[
\delta_0(B^{-1}\,\cdot)=|\det B|\delta_0=6\delta_0.
\tag{5.10}
\]

Indeed its test pairing is \(6\phi(0)\). Apply the identity to \(T=E_a^+\) and divide by six:

\[
E_{B,a}(x)=-\frac{e^{ia\rho_B(x)}}{24\pi\rho_B(x)}.
\tag{5.11}
\]

Theorem 4.2 now gives exactly \((G:D^2+a^2)E_{B,a}=\delta_0\). The linear substitution proves local integrability as well. The negative determinant \(\det B=-6\) does not change the sign of Lebesgue density. \(\square\)

**Exercise 7 (advanced).** *Remove a parameter pole in a squared operator.*

Construct a weakly entire fundamental family for \(Q_a^2=(\Delta+a^2)^2\) in \(\mathbb R^3\), with value \(-|x|/(8\pi)\) at \(a=0\). Start by differentiating \(Q_aE_a^+=\delta_0\) for \(a\ne0\), and remove the resulting pole using a homogeneous solution.

**Solution 7.** Entire dependence permits parameter differentiation on each test:
\(Q_a\partial_aE_a^+=-2aE_a^+\). Apply \(Q_a\) once more to obtain
\(Q_a^2\partial_aE_a^+=-2a\delta_0\). Thus for \(a\ne0\),

\[
F_a^{\mathrm{raw}}
=-\frac{\partial_aE_a^+}{2a}
=\frac{i e^{iar}}{8\pi a}
\tag{5.12}
\]

has unit source for \(Q_a^2\).
The cosine series \(\sum_{k\geq0}(-1)^ka^{2k}(r^2)^k/(2k)!\) converges with all spatial derivatives by the same polynomial estimate as (4.2). Its sum is smooth at zero. Direct radial differentiation off zero, followed by continuity at zero, gives

\[
Q_a\cos(ar)=-2a\frac{\sin(ar)}r,\qquad
Q_a^2\cos(ar)=0.
\tag{5.13}
\]

The second identity follows from the global homogeneous equation for the sine quotient in Theorem 4.2.
Subtract \(i\cos(ar)/(8\pi a)\) from (5.12). The source is unchanged, and the result extends to

\[
\begin{aligned}
F_a(x)&=-\frac{\sin(ar)}{8\pi a}&&(a\ne0),\\
F_0(x)&=-\frac r{8\pi}.
\end{aligned}
\tag{5.14}
\]

To verify entire dependence at the apparent singularity, use the series
\(-\sum_{k\geq0}(-1)^ka^{2k}r^{2k+1}/(8\pi(2k+1)!)\).
On bounded spatial and parameter sets its terms, and every parameter derivative, are bounded by summable multiples of \(r\): powers \(r^{2k}\) are bounded by a geometric factor, and differentiating in \(a\) introduces only a polynomial in \(k\) and another geometric factor. These are integrable compact-test majorants. The sum is therefore weakly entire and has the indicated value at zero. For each test,
\(\langle Q_a^2F_a-\delta_0,\phi\rangle\) is continuous in \(a\) and zero for \(a\ne0\), so it is zero also at zero, agreeing with (2.6).
Subtracting only \(i/(8\pi a)\) would fail: \(Q_a^2\) sends that constant function to the nonzero constant \(ia^3/(8\pi)\). The cosine term in (5.13) supplies the necessary homogeneous correction. \(\square\)

**Exercise 8 (advanced).** *The contact term of a second derivative.*

Determine the point-supported term of \(\partial_j\partial_kE_a^+\) for every \(a\in\mathbb C\), using spherical excision to specify the remaining principal value. Give its source under \(Q_a\).

**Solution 8.** First separate the Newton singularity:

\[
\begin{aligned}
E_a^+&=\Phi_3+R_a,\\
R_a(r)&=-\frac{e^{iar}-1}{4\pi r}
       =-\frac{ia}{4\pi}+\frac{a^2r}{8\pi}+O(r^2).
\end{aligned}
\tag{5.15}
\]

The convergent exponential series, differentiated with respect to the scalar \(r\), proves \(R_a'=O(1)\) and \(R_a''=O(1)\) near zero. Away from zero its Hessian is
\[
\partial_j\partial_kR_a
=\delta_{jk}\frac{R_a'}r
  +\frac{x_jx_k}{r^2}\left(R_a''-\frac{R_a'}r\right)=O(r^{-1}),
\]
which is locally integrable. Integration by parts outside a small ball proves that these are the full weak derivatives. For the first derivative the error is bounded by the area \(4\pi\varepsilon^2\) times bounded \(R_a\) and the test; for the second it is bounded by the same area times the bounded gradient and test. Both errors tend to zero. Thus this remainder contributes no point term.

We now prove the Newton Hessian explicitly. The weak first derivative, already established in U020, Theorem 1.1, is
\(v_j=\partial_j\Phi_3=x_j/(4\pi r^3)\), a locally integrable function. Its classical \(k\)-derivative away from zero is
\(H_{jk}=(\delta_{jk}r^2-3x_jx_k)/(4\pi r^5)\).
Sphere symmetries give
\(\int_{\mathbb S^2}\omega_j\omega_k\,d\omega=(4\pi/3)\delta_{jk}\):
reflection reverses an off-diagonal integrand, permutation makes the three diagonal integrals equal, and their sum is \(\int_{\mathbb S^2}|\omega|^2\,d\omega=4\pi\).
These symmetries preserve surface measure by the Gram surface formula proved in U011, or by its orthogonal parameter changes. Hence \(H_{jk}\) has zero spherical mean at every radius.

It follows that the spherical principal value exists on every compact test. On \(0<r<1\), subtract \(\phi(0)\) from the test without changing the integral, by the zero angular mean. The difference is bounded by \(r\|\nabla\phi\|_\infty\), so the absolute radial bound is \(C\|\nabla\phi\|_\infty\,dr\). On \(1\leq r\leq R\) the bound is \(C\|\phi\|_\infty\,dr/r\). This also proves continuity in a fixed-support first-derivative test seminorm, so the limit is a distribution.

The integration-by-parts identity on \(r>\varepsilon\) is
\[
-\int_{r>\varepsilon}v_j\,\partial_k\phi\,dx
=\int_{r>\varepsilon}H_{jk}\phi\,dx
 +\frac1{4\pi}\int_{\mathbb S^2}\omega_j\omega_k
                    \phi(\varepsilon\omega)\,d\omega .
\]
The last sign is positive because the inner normal is \(-\omega\). As \(\varepsilon\downarrow0\), the left side tends to \(\langle\partial_kv_j,\phi\rangle\), the first right side to the spherical principal value, and the second to \((\delta_{jk}/3)\phi(0)\). Therefore

\[
\begin{aligned}
\partial_j\partial_kE_a^+
  &=\operatorname{pv}H_{jk}
       +\frac{\delta_{jk}}3\delta_0+\partial_j\partial_kR_a,\\
H_{jk}(x)&=\frac{\delta_{jk}r^2-3x_jx_k}{4\pi r^5}.
\end{aligned}
\tag{5.16}
\]

Here \(\operatorname{pv}\) means exactly the limit over \(|x|>\varepsilon\). The decomposition depends on that specified excision, and the coefficient of its point term is independent of \(a\).
Tracing checks the normalization: \(\sum_jH_{jj}=0\), the three point terms sum to \(\delta_0\), and (4.4) gives
\(\Delta R_a=-a^2E_a^+\) as locally integrable distributions. Finally, derivatives of distributions commute because derivatives of their tests commute. Applying \(\partial_j\partial_k\) to (4.4) gives

\[
Q_a(\partial_j\partial_kE_a^+)=\partial_j\partial_k\delta_0.
\tag{5.17}
\]

All three terms of (5.16) are needed for this identity. \(\square\)

## Programme proof locations and freely accessible sources

The following are exact earlier programme proofs used in this lesson. The supplied foundation files retain their own license notices.

- Boundary flux and weak identities, Theorem 2.1 and Corollary 2.2: surface measure, divergence and Green identities on the punctured regions used here.
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Theorem 1.1, Lemma 2.1 and Theorem 3.1: full Newton sources and first weak gradients, real symmetric diagonalization, the matrix determinant branch and its semidefinite extension, and the complex Gaussian mass.
- [Homogeneous extensions and angular moments](homogeneous-extensions-and-angular-moments.md), Lemma 1.1: the Euler characterization of homogeneity. The rotation-to-constant argument needed here is proved in Solution 4 above.
- [Convolution as addition of supports](convolution-as-addition-of-supports.md), Theorem 1.1, Proposition 5.1 and Theorem 5.2: compact-support convolution, differentiation, local smoothing and convergence.
- [Gluing holomorphic sides](gluing-holomorphic-sides.md), Lemma 3.2: the scalar identity principle for the optional continuation check after (3.5).
- [Causal integration of complex order](causal-integration-of-complex-order.md), scalar logarithm construction immediately before Theorem 4.1: local logarithmic series and slit-plane branch. The branch change used here is specified before Theorem 1.1.
- [Scalar and metric foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13: compactness, calculus, exponential and trigonometric series, and smooth cutoffs.
- [Finite-dimensional foundations](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §10: matrix inverses, adjugates, determinants and Gram surface density.
- [Integration foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.1–15.4: convergence, Fubini, linear substitutions, \(L^1\) approximation and mollification.
- [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4–A5: polar integration and sphere areas, including \(\sigma_4=8\pi^2/3\).

Freely accessible human-written mathematical sources:

- Semyon Dyatlov, [*Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDE*](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf), October 2, 2026 version, Proposition 9.6 and its punctured-domain proof on pp. 99–100. The Newton proof and the additional radial calculations required here are given in the linked programme lesson and above.
- V. Hnizdo, [*Generalized second-order partial derivatives of \(1/r\)*](https://arxiv.org/pdf/1009.2480), arXiv:1009.2480v2, December 1, 2010, formulas (2), (4) and (10) on pp. 1–3: spherical-excision normalization of the Hessian. Solution 8 proves that normalization directly by integration by parts, including existence of the principal value and the contact term.
