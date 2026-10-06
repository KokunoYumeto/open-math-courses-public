# Hölder Gaussian bounds and operator remainders

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

A Gaussian peak decreases under quadratic evolution, while carefully phased annuli can accumulate at one point. We measure both effects and the exact cancellation of time filters. The full fractional bound and factorial remainder retain every degenerate matrix and iterated-operator hypothesis; three further proofs determine the sharp Hölder-gap loss, all order filters, and anisotropic Gaussian peaks without matrix commutation assumptions.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves all Schwartz seminorm estimates, polynomial-growth multipliers, compact-test density, Gaussian mass, inverse transforms and distributional transposes. [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Lemma 0.1 and the integrable-weight proof immediately following it, supplies Schwartz Plancherel with all weight coefficients. The [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16, proves dominated convergence, absolute Fubini, real linear Jacobians and Cauchy–Schwarz. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the norm comparison, cutoffs and algebra. Supplied prerequisites retain their stated licences.

[Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and the transform part of Theorem 3.1, proves real symmetric diagonalization, determinant differentiation, the holomorphic determinant branch and the complex Gaussian transform. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1 and calculation G, supplies the partial Fourier transposes and the signed scalar and product Fresnel identities.

Write \(D=-i\partial\), \(Q_A(D)=\sum_{k,l}A_{kl}D_kD_l\), and
\[
T_A=e^{-Q_A(D)},\qquad
\mathcal F(T_Au)(\xi)=e^{-\xi^TA\xi}\widehat u(\xi).
\]
All matrices are complex symmetric and \(n\ge1\). The real and imaginary parts are real symmetric matrices. The multiplier and all its derivatives have polynomial growth when \(\operatorname{Re}A\ge0\); it consequently acts continuously on \(\mathcal S'\). The notation \(A(D)\) for a Gaussian exponent means the quadratic \(Q_A(D)\).

The complete [integral Taylor proof](when-a-kernel-is-smooth.md#taylor-estimates-on-compact-neighborhoods) supplies the finite-order remainders used here, including signed increments, complex-valued functions, directional derivatives and uniform bounds for all required derivatives on compact neighborhoods. The same formula holds when derivatives are continuous up to the endpoints of a closed interval: the induction uses only the fundamental theorem and integration by parts on that interval. This covers the one-sided time derivatives in the operator remainder below.

## Convolution with kernels and Gaussian measures

**Lemma 0.1.** Let \(\nu\) be a finite positive measure with every polynomial moment finite, or a density \(q(y)\,dy\) with \(q\in\mathcal S\). Write \(d|\nu|\) for \(d\nu\) in the first case and \(|q(y)|dy\) in the second. Then convolution by \(\nu\) maps \(\mathcal S\) continuously into itself. For bounded continuous \(v\), its ordinary convolution is bounded continuous, and
\[
 \begin{gathered}
 \|\nu*v\|_\infty\le |\nu|(\mathbb R^n)\|v\|_\infty,\\
 \mathcal F(\nu*v)=\widehat\nu\,\widehat v
 \quad\text{in }\mathcal S'.
 \end{gathered}
\]
Here \(\widehat\nu(\xi)=\int e^{-iy\cdot\xi}\,d\nu(y)\); each of its derivatives is bounded by the corresponding absolute moment.

**Proof.** Since \(1+|x|\le(1+|x-y|)(1+|y|)\), differentiation under the convolution integral gives
\[
 \begin{gathered}
 \sup_x(1+|x|)^N
       |\partial^\beta(\nu*\phi)(x)|\\
 \le \left(\int(1+|y|)^N\,d|\nu|(y)\right)
       \sup_z(1+|z|)^N|\partial^\beta\phi(z)|.
 \end{gathered}
\]
Difference quotients are dominated by the next bounded derivative of \(\phi\) times this finite measure; iteration justifies every derivative. These estimates and F1 prove Schwartz continuity. The same dominated-difference argument proves the assertion about derivatives of \(\widehat\nu\), so it is a permitted multiplier by F1. For bounded continuous \(v\), dominated convergence proves continuity of \(\nu*v\), and its norm estimate is immediate. For \(\phi\in\mathcal S\), Fubini gives
\[
 \begin{gathered}
 \langle\mathcal F(\nu*v),\phi\rangle\\
 =\int v(z)\left(\int\widehat\phi(z+y)
                     \,d\nu(y)\right)dz\\
 =\langle v,\mathcal F(\widehat\nu\,\phi)\rangle
 =\langle\widehat v,\widehat\nu\,\phi\rangle.
 \end{gathered}
\]
The first double integral is absolutely bounded by
\(\|v\|_\infty|\nu|(\mathbb R^n)\|\widehat\phi\|_1\).
For each fixed \(z\), inserting the Fourier integral in the inner integral is justified by \(|\nu|(\mathbb R^n)\|\phi\|_1\), and gives its displayed value. This also fixes the Fourier sign and inverse normalization. \(\square\)

## Measure a Gaussian peak and an accumulated annulus

Begin with one Gaussian, \(u_b(x)=e^{-b|x|^2}\), where \(b>0\). For the purely imaginary matrix \(A=icI\), \(c\in\mathbb R\), the Gaussian calculation in Solution 5 gives
\[
\begin{gathered}
T_{ticI}u_b(x)\\
=(1+4itbc)^{-n/2}\\
{}\cdot\exp\!\left(-\frac{b|x|^2}{1+4itbc}\right),\\
\|T_{ticI}u_b\|_\infty\\
=(1+16t^2b^2c^2)^{-n/4}.
\end{gathered}
\tag{J1}
\]
The power is continued from \(t=0\). Taking the real part of the exponent measures the spatial width: the modulus falls to its peak divided by \(e\) at radius
\[
W_b(t)=b^{-1/2}\sqrt{1+16t^2b^2c^2}.
\tag{J2}
\]
For \(c\ne0\), this Gaussian spreads while its peak decreases; for \(c=0\), it remains fixed. Solution 11 will retain this exact measurement for anisotropic input and matrices whose real and imaginary parts do not commute.

The uniform bound for every input requires a second measurement. Let \(1\le r\le n\), write \(x=(y,z)\in\mathbb R^r\times\mathbb R^{n-r}\), and put \(C_r=\operatorname{diag}(I_r,0)\). Choose a nonnegative, nonzero \(a\in C_c^\infty(\mathbb R^r)\) supported in \(1<|y|<2\). When \(r<n\), choose \(b\in C_c^\infty(\mathbb R^{n-r})\) with \(b(0)=1\); when \(r=n\), omit this factor. For \(R_k=4^k\), define the finite smooth input
\[
\begin{gathered}
u_{\alpha,N}(y,z)\\
=\sum_{k=1}^N R_k^{-r-\alpha}a(y/R_k)\\
{}\qquad\cdot e^{-i|y|^2/4}b(z),\\
0<\alpha<1.
\end{gathered}
\tag{J3}
\]
Its disjoint annuli have small height and rapidly changing phase. The exact oscillatory kernel cancels that phase at the origin. With
\[
\begin{gathered}
\kappa_r=(4\pi)^{-r/2}e^{-ir\pi/4},\\
I_a=\int_{\mathbb R^r}a(y)\,dy>0,\\
T_{iC_r}u_{\alpha,N}(0)\\
=\kappa_r I_a\frac{1-4^{-N\alpha}}{4^\alpha-1}.
\end{gathered}
\tag{J4}
\]
each annulus contributes with the same complex phase. Solution 9 proves that the exact order-\(r+\alpha\) Hölder norm of these inputs stays bounded independently of \(N\) and \(\alpha\). Taking \(N=\lceil1/\alpha\rceil\) then gives
\[
\begin{gathered}
\frac{1-4^{-N\alpha}}{4^\alpha-1}
\ge\frac1{4\alpha},\\
\lim_{\alpha\downarrow0}
\alpha\frac{1-4^{-\lceil1/\alpha\rceil\alpha}}
{4^\alpha-1}
=\frac{3}{4\log4}.
\end{gathered}
\tag{J5}
\]
For full rank \(r=n\), this measures the sharp order of the \(1/\alpha\) constant in Theorem C. For smaller rank, it measures the sharp loss at order \(r+\alpha\), as in Solution 4. The original order-\(n+\alpha\) estimate can remain bounded as \(\alpha\downarrow0\) when \(r<n\), because it assumes more derivatives.

## C. The full fractional estimate, including every degenerate matrix

Put \(\mu=n+\alpha,\ 0<\alpha<1\), and, for \(u\in C^n(\mathbb R^n)\), use the reduced norm
\[
\begin{gathered}
|u|_\mu=\sum_{|\beta|<n}\|\partial^\beta u\|_\infty
\\ {}+\sum_{|\beta|=n}[\partial^\beta u]_\alpha,
\\ [v]_\alpha=\sup_{x\ne y}
\frac{|v(x)-v(y)|}{|x-y|^\alpha}.
\end{gathered} \tag{C1}
\]
There is no additional supremum norm of the derivatives of order \(n\) in (C1). The cited exercise uses the larger norm
\[
 \|u\|_{\mu,\mathrm{full}}
 =|u|_\mu+\sum_{|\beta|=n}\|\partial^\beta u\|_\infty.
\]
Solution 2 proves \(|u|_\mu\le\|u\|_{\mu,\mathrm{full}}\le C_n|u|_\mu\), with \(C_n\) independent of \(\alpha\). Our estimate with the reduced right side therefore implies the source's full-norm estimate and preserves its finite-norm hypothesis. The proof below establishes the stronger reduced-norm bound directly.

**Theorem C (uniform fractional Gaussian bound).** If \(\operatorname{Re}A\ge0\), \(\|\operatorname{Im}A\|_{\mathrm{op}}\le1\), and \(|u|_\mu<\infty\), then the tempered distribution \(T_Au\) has a bounded continuous representative, and
\[
\|T_Au\|_\infty\le \frac{C_n}{\mu-n}|u|_\mu.
\tag{C2}
\]
The constant is independent of \(A,u,\alpha\). Neither strict positive definiteness nor simultaneous diagonalization of the real and imaginary parts is assumed. More generally the proof gives \(C_n(1+M)^{n/2}/\alpha\) when \(\|\operatorname{Im}A\|_{\mathrm{op}}\le M\).

The estimate also retains the literal source norm hypothesis if its fixed matrix norm is given in another convention. The complete finite-norm comparison in §12.9 of the linked metric-foundations proof gives \(c_b|x|_2\le N(J_bx)\) for the original norm \(N\) and its actual matrix-entry coordinates, with \(c_b>0\). The Euclidean operator norm is at most the full matrix-entry Euclidean norm, by coordinate Cauchy--Schwarz. Hence \(N(C)\le1\) implies \(\|C\|_{\mathrm{op}}\le c_b^{-1}\). Apply the general estimate with this fixed \(M_n=c_b^{-1}\); its changed constant remains independent of \(A,u,\mu\). This is an exact norm adapter for any fixed source convention, with all its coordinate factors retained. No smallness of \(\operatorname{Re}A\) is introduced.

**Proof: the frequency bands retain the exact Hölder norm.** Fix a real smooth cutoff \(\varphi\) equal to one for \(|\xi|\le1\), zero for \(|\xi|\ge2\). Let
\[
\begin{gathered}
\chi_0(\xi)=\varphi(\xi),
\\ \chi_j(\xi)=\varphi(2^{-j}\xi)-\varphi(2^{-j+1}\xi),
\\ j\ge1.
\end{gathered}
\]
and \(u_j=\mathcal F^{-1}(\chi_j\widehat u)\). These are convolutions of the bounded function \(u\) with Schwartz kernels, hence smooth bounded functions by Lemma 0.1 and differentiation of those kernels. Put \(\psi(\eta)=\varphi(\eta)-\varphi(2\eta)\) and \(k=\mathcal F^{-1}\psi\). As \(\psi\) vanishes near zero, every moment of \(k\) is zero, by the Fourier derivative formula. For \(j\ge1\),
\[
\begin{gathered}
u_j(x)=
\\ \int 2^{jn}k(2^jy)u(x-y)\,dy.
\end{gathered} \tag{C3}
\]

For each \(x,y\), apply the one-variable Taylor formula to \(t\mapsto u(x-ty)\) through order \(n\). Its remainder, after subtracting the degree-\(n\) polynomial evaluated at \(x\), is
\[
\begin{gathered}
\frac1{(n-1)!}\int_0^1(1-t)^{n-1}
\\ {}\cdot\bigl(g^{(n)}(t)-g^{(n)}(0)\bigr)\,dt,
\\ g(t)=u(x-ty).
\end{gathered} \tag{C4}
\]
Indeed the integral Taylor formula through degree \(n-1\), with \(g^{(n)}(0)\) separated, adds the degree-\(n\) term \(g^{(n)}(0)/n!\). The directional derivative expansion gives
\[
|g^{(n)}(t)-g^{(n)}(0)|
\le C_n |y|^{n+\alpha}t^\alpha
\sum_{|\beta|=n}[\partial^\beta u]_\alpha.
\]
The integral factor in (C4) is at most \(1/n!\), uniformly for \(0<\alpha<1\). Integrating this remainder against (C3) cancels the entire degree-\(n\) Taylor polynomial by the moment identities. The Schwartz moments with exponents between \(n\) and \(n+1\) are bounded by one fixed sum of the two endpoint moments. Thus
\[
\begin{gathered}
\|u_j\|_\infty\le C_n2^{-j(n+\alpha)}|u|_\mu,
\\ j\ge1,
\\ \|u_0\|_\infty\le C_n\|u\|_\infty.
\end{gathered} \tag{C5}
\]
This argument uses only the difference seminorms at order \(n\), exactly as required by the reduced norm (C1). The individual pointwise values of the \(n\)th derivatives occur in the cancelled Taylor polynomial and are never estimated by an unprovided supremum.

The partial sum \(\sum_{j=0}^Ju_j\) has multiplier \(\varphi(2^{-J}\xi)\), which tends to one on Schwartz tests in their full topology: on the growing central ball the difference vanishes, and outside it arbitrary Schwartz polynomial decay controls every differentiated cutoff product. Hence the partial sums tend to \(u\) in \(\mathcal S'\). By (C5) the sum also converges uniformly to a bounded continuous function. The two limits agree as distributions, so the continuous original \(u\) equals this uniform sum.

**Proof: an \(L^1\) bound for each oscillatory kernel.** First take \(A=iC\) with \(C\) real symmetric. Choose a fixed smooth \(\eta\) equal to one on \(|\xi|\le2\) and zero outside \(|\xi|<4\). For \(j\ge0\), put
\[
\begin{gathered}
b_j(\zeta)=\eta(\zeta)\exp(-i2^{2j}\zeta^TC\zeta),
\\ K_j=\mathcal F^{-1}b_j,
\\ R_j=1+2^{2j}\|C\|_{\mathrm{op}}.
\end{gathered}
\]
For any fixed integer \(s>n/2\) and every multi-index \(|\beta|\le s\), the finite product rule on the fixed support gives
\[
\|\partial^\beta b_j\|_2\le C_{n,s}R_j^{|\beta|}.
\tag{C6}
\]
Each derivative of the exponential contributes factors bounded by a constant times \(2^{2j}\|C\|_{\mathrm{op}}\), and the exponential has modulus one. Consequently every derivative term of degree at most \(|\beta|\) is bounded by \(C R_j^{|\beta|}\); the support volume is fixed.

U041, Lemma 0.1, is the full Schwartz Plancherel proof. Together with F2 and the inverse factor \((2\pi)^{-n}\), it gives
\[
\|z^\beta K_j\|_2=(2\pi)^{-n/2}
\|\partial^\beta b_j\|_2.
\tag{C7}
\]
Put \(W_j(z)=1+|z|^2/R_j^2\). Use Cauchy--Schwarz with the weight \(W_j^s\). Its inverse has integral \(R_j^n\int(1+|w|^2)^{-s}dw<\infty\), since \(2s>n\). The exact tail proof after U041, Lemma 0.1, bounds each shell \(2^k\le|w|<2^{k+1}\) by \(2^{2n}2^{k(n-2s)}\), a convergent geometric series, and bounds the unit ball by a cube. Expanding the positive integer power and using (C6)--(C7) yields
\[
\begin{gathered}
\|K_j\|_1\le
\\ \left(\int W_j(z)^{-s}dz\right)^{1/2}
\\ {}\cdot\left(\int W_j(z)^s|K_j(z)|^2dz\right)^{1/2}
\\ \le C_nR_j^{n/2}.
\end{gathered} \tag{C8}
\]
All multinomial coefficients in the second integral are fixed nonnegative numbers; the factors \(R_j^{-2|\beta|}\) cancel the derivative growth in (C6). This scaling is essential: keeping a fixed spatial weight would lose the required fractional endpoint.

The convolution kernel \(q_j\) of
\[
e^{-i\xi^TC\xi}\eta(2^{-j}\xi)
\]
is \(q_j(x)=2^{jn}K_j(2^jx)\), by an actual real change of variables with its Fourier inverse Jacobian. Hence its \(L^1\) norm is \(\|K_j\|_1\). The cutoff \(\eta(2^{-j}\xi)\) is one on the support of \(\chi_j\), including \(j=0\). Therefore
\[
\begin{gathered}
T_{iC}u_j=q_j*u_j,
\\ \|T_{iC}u_j\|_\infty
\\ \le C_n(1+2^{2j}\|C\|_{\mathrm{op}})^{n/2}
\\ {}\cdot\|u_j\|_\infty.
\end{gathered} \tag{C9}
\]
The identity on bounded smooth functions follows also by testing and Fubini: \(q_j\) is Schwartz, \(u_j\) bounded, and the absolute test integral is bounded by \(\|q_j\|_1\|u_j\|_\infty\|\phi\|_1\). The Fourier multiplication identity then has exactly the displayed inverse factor.

For \(\|C\|_{\mathrm{op}}\le M\) and \(j\ge1\), (C5) and (C9) imply
\[
\begin{gathered}
\|T_{iC}u_j\|_\infty
\\ \le C_n(1+M)^{n/2}2^{-j\alpha}|u|_\mu.
\end{gathered} \tag{C10}
\]
The \(j=0\) bound has the same constant without \(2^{-j\alpha}\). Each term is continuous because it is a convolution with an integrable smooth kernel; dominated convergence or translation continuity of that kernel suffices. The series converges uniformly, and
\[
\begin{gathered}
\sum_{j\ge1}2^{-j\alpha}
\\ =\frac1{2^\alpha-1}
\\ \le\frac1{\alpha\log2}.
\end{gathered} \tag{C11}
\]
Continuity of \(T_{iC}\) on \(\mathcal S'\) identifies this uniform sum with its action on \(u\). This proves the estimate for every real symmetric \(C\), including zero and singular \(C\); no inverse matrix or lower eigenvalue bound appeared.

**Proof: arbitrary nonnegative real part.** Write \(A=R+iC\), \(R\ge0\). Orthogonally diagonalize the real symmetric \(R\). In an eigen-direction of eigenvalue \(r>0\), let \(\gamma_r\) have density \((4\pi r)^{-1/2}e^{-x^2/(4r)}\); in a zero eigen-direction use the point probability \(\delta_0\). The product, carried back by the orthogonal map, is a probability measure \(\gamma_R\), with Fourier transform \(e^{-\xi^TR\xi}\). The scalar Gaussian mass and transform prove every normalization; zero eigenvalues create genuine point factors, not undefined determinants. All moments of this probability are finite.

For bounded continuous \(v\), \(\gamma_R*v\) is bounded continuous by dominated convergence and
\[
\|\gamma_R*v\|_\infty\le\|v\|_\infty.
\tag{C12}
\]
Lemma 0.1 proves that this convolution represents \(T_Rv\) on tempered tests, supplies every Schwartz seminorm estimate and identifies the transpose operation. Quadratic multipliers commute exactly, even when \(R\) and \(C\) do not commute as matrices:
\[
\begin{gathered}
e^{-\xi^TA\xi}=e^{-\xi^TR\xi}e^{-i\xi^TC\xi},
\\ T_Au=T_R(T_{iC}u).
\end{gathered}
\]
Apply (C12) to the continuous bounded representative just constructed for \(T_{iC}u\). Equations (C10)--(C12), and \(0<\alpha<1\), prove (C2) and its more general \(M\)-version. The conclusion retains every semidefinite boundary case and arbitrary size of the real part. \(\square\)

## D. The complete remainder with its factorial

**Theorem D (the factorial operator remainder).** Under the matrix and exponent assumptions of Theorem C, suppose, for an integer \(N\ge0\), that every distribution \(Q_A(D)^ju,\ 0\le j\le N\), has a \(C^n\) representative with finite norm (C1). Then
\[
\begin{gathered}
\left\|T_Au-\sum_{j=0}^{N-1}\frac{(-Q_A(D))^ju}{j!}\right\|_\infty
\\ \le \frac{C_n}{(\mu-n)N!}|Q_A(D)^Nu|_\mu.
\end{gathered} \tag{D1}
\]
The empty sum at \(N=0\) is zero. The constant is the same dimension-dependent bound as in Theorem C, independent of \(A,u,N,\mu\). Every object on the left has a bounded continuous representative.

The original fixed matrix-norm version follows from the same exact adapter in C: \(N(t\,\operatorname{Im}A)=tN(\operatorname{Im}A)\le1\) for \(0\le t\le1\), so one fixed operator-norm bound \(M_n\) applies on the whole time interval. The unchanged time integral supplies the same \(N!\); no iterate hypothesis or dimensional constant is suppressed.

**Proof: continuity of the time-dependent representative.** For a function \(v\) with finite \(|v|_\mu\), put \(V(t)=T_{tA}v,\ 0\le t\le1\). Theorem C applies throughout, because \(\operatorname{Re}(tA)\ge0\) and \(\|\operatorname{Im}(tA)\|_{\mathrm{op}}\le1\). Thus
\[
\|V(t)\|_\infty\le C_n(\mu-n)^{-1}|v|_\mu.
\tag{D2}
\]
In fact \(V(t)\) is continuous as a map into the normed space \(C_b(\mathbb R^n)\). To prove this rather than assume distributional convergence implies uniform convergence, use the same frequency bands \(v_j\) as in the proof of C. For a fixed \(j\), the compactly supported smooth multiplier
\[
\eta(2^{-j}\xi)e^{-t\xi^TA\xi}
\]
depends continuously on \(t\) in every smooth derivative norm. Its support is fixed, so its inverse kernels depend continuously on \(t\) in the Schwartz topology and therefore in \(L^1\). Convolution with bounded \(v_j\) gives continuity of \(t\mapsto T_{tA}v_j\) in supremum norm. Constants for this fixed-band assertion may depend on \(A,j\), which causes no problem.

For the tail, the imaginary-kernel estimate and the real Gaussian contraction give uniformly in \(t\in[0,1]\)
\[
\begin{gathered}
\|T_{tA}v_j\|_\infty
\\ \le C_n2^{-j(\mu-n)}|v|_\mu,\qquad j\ge1.
\end{gathered} \tag{D3}
\]
The uniform series of these continuous \(C_b\)-valued maps is continuous, and by the exact distributional band identity is \(V(t)\). At \(t=0\) it is the uniformly reconstructed original \(v\). This proves the assertion at both endpoints and for all semidefinite matrices.

**Proof: the scalar Taylor identity represents an actual bounded function.** On Schwartz tests the multipliers \(e^{-t\xi^TA\xi}\) have continuous derivatives of every order in \(t\in[0,1]\), including one-sided endpoint derivatives:
\[
\begin{gathered}
\frac{d^k}{dt^k}e^{-t\xi^TA\xi}
\\ =(-\xi^TA\xi)^k e^{-t\xi^TA\xi}.
\end{gathered} \tag{D4}
\]
For each fixed matrix \(A\), all mixed \(\xi,t\) derivatives are bounded by polynomials uniformly on this time interval, because the exponential has modulus at most one. Taylor differences or the fundamental theorem, multiplied by arbitrary Schwartz weights, justify (D4) in the full Schwartz topology. Transposition and commutation of polynomial multipliers then give, for any Schwartz test \(\phi\),
\[
\begin{gathered}
\frac{d^k}{dt^k}\langle T_{tA}u,\phi\rangle
\\ =\langle T_{tA}(-Q_A(D))^ku,\phi\rangle.
\end{gathered} \tag{D5}
\]
This is an actual scalar smooth function of \(t\); no unproved norm derivative of a bounded function is used.

For \(N\ge1\), put \(v=Q_A(D)^Nu\). Taylor's integral formula at \(t=0\) applied to (D5) yields the distributional equality
\[
\begin{gathered}
T_Au-\sum_{j<N}\frac{(-Q_A(D))^ju}{j!}
\\ =\frac{(-1)^N}{(N-1)!}
\\ {}\cdot\int_0^1(1-t)^{N-1}T_{tA}v\,dt.
\end{gathered} \tag{D6}
\]
The last integral has a bounded continuous representative obtained by integrating the continuous \(C_b\)-valued map proved above, with \(v=Q_A(D)^Nu\). Equivalently define it pointwise: the supremum bound (D2) makes the integral absolutely convergent; continuity in the \(C_b\) norm proves its continuity in \(x\). Fubini against any Schwartz test is justified by the bound \(C_n(\mu-n)^{-1}|v|_\mu\|\phi\|_1\), and recovers exactly (D6).

The norm of this representative is at most
\[
\begin{gathered}
\frac{C_n|Q_A(D)^Nu|_\mu}{(\mu-n)(N-1)!}
\\ {}\cdot\int_0^1(1-t)^{N-1}\,dt
\\ =\frac{C_n|Q_A(D)^Nu|_\mu}{(\mu-n)N!}.
\end{gathered}
\]
The lower Taylor terms are continuous bounded functions by their assumed norms, and \(T_Au\) is so by C; hence the equality of distributions is an equality of the indicated continuous functions. This proves (D1). For \(N=0\) it is precisely (C2), with \(0!=1\). The argument retains every intermediate operator hypothesis \(0\le j\le N\) and the exact factorial, including \(A=0\), singular imaginary part and unbounded nonnegative real part. \(\square\)

## Measure cancellation across any number of times

For \(m\ge1\), sample the evolution at the equally spaced times \(0,t,\ldots,mt\), and form
\[
\begin{gathered}
L_{m,t}u\\
=\sum_{j=0}^m(-1)^j\binom mj T_{jtA}u\\
=(I-T_{tA})^m u,\\
0<t\le1/m.
\end{gathered}
\tag{J6}
\]
For a plane wave \(u(x)=e^{ix\cdot\xi}\), put \(q=\xi^TA\xi\). The measured scalar factor is exactly
\[
\begin{gathered}
L_{m,t}u=(1-e^{-tq})^m u,\\
t^{-m}(1-e^{-tq})^m\longrightarrow q^m.
\end{gathered}
\tag{J7}
\]
Every lower power of \(t\) cancels. The full operator identity in Solution 10 turns this into an integral of \(T_{sA}Q_A^m u\), with \(0\le s\le mt\), over an \(m\)-dimensional cube. Under the exact iterated Hölder hypotheses of Theorem D, it gives
\[
\begin{gathered}
\|L_{m,t}u\|_\infty
\le\frac{C_n}{\alpha}t^m|Q_A^m u|_{n+\alpha},\\
t^{-m}L_{m,t}u\longrightarrow Q_A^m u
\quad\text{uniformly}.
\end{gathered}
\tag{J8}
\]
For \(m=2\) and \(m=3\), the filters in Solution 6 are respectively \(-L_{2,t}\) and \(-L_{3,t}\). Their negative limiting signs come directly from their displayed coefficients. The complete proofs C–D above supply the uniform bound and the time continuity used in every order of this calculation.

## Exercises

**Exercise 1 (foundation: plane waves and exact remainders).** In dimension one, take \(A=r+ic\), \(r\ge0\), \(|c|\le1\), and \(u(x)=e^{ikx}\). Compute \(T_Au,Q_A^ju\), a bound for \(|u|_{1+\alpha}\), and the exact order-\(N\) Taylor remainder. Give a scalar bound that also covers arbitrarily large \(r\).

**Exercise 2 (foundation: the missing highest supremum).** For \(u\in C^n(\mathbb R^n)\) with \(|u|_{n+\alpha}<\infty\), prove that its derivatives of order \(n\) are actually bounded. Derive this from lower supremum norms and highest difference seminorms, and explain why the original proof of Theorem C does not need to add those supremum norms as assumptions.

**Exercise 3 (intermediate: dilation and the quadratic scale).** Let \(u_L(x)=u(Lx)\), \(L>0\). Compute its exact Hölder norm and prove the scaling identity for \(T_Au_L\). Apply the general imaginary-matrix bound to obtain an estimate in terms of \(|u|_\mu\). Also examine \(L^{-\mu}u(Lx)\) when \(L\ge1\).

**Exercise 4 (advanced: rank of the oscillatory part).** Suppose \(r=\operatorname{rank}C\). Improve the band-kernel estimate in Theorem C to growth \(2^{jr}\), using a cutoff that factors in eigenvector coordinates. Show that when \(1\le r<n\) its estimate for the original \(|u|_{n+\alpha}\) stays bounded as \(\alpha\downarrow0\). Prove that the order-\(r\) norm \(|u|_{r+\alpha}\) also suffices, and treat \(r=0\).

**Exercise 5 (intermediate: a Gaussian with noncommuting matrices).** In dimension two put
\[
A=\begin{pmatrix}2+i&1\\1&1-i\end{pmatrix},
\qquad u(x)=e^{-|x|^2}.
\]
Verify all matrix hypotheses and the failure of commutation of \(R,C\). Compute \(T_Au\), including the correct determinant root, and evaluate it at \((1,-1)\).

**Exercise 6 (advanced: cancellation across time scales).** If \(Q_A^ju\) has finite \(|\cdot|_\mu\) for \(0\le j\le2\), bound \(2T_{tA}u-T_{2tA}u-u\) for \(0<t\le1/2\) and find its uniform limit after division by \(t^2\). Under the corresponding hypotheses through order three, do the same for \(3T_{tA}u-3T_{2tA}u+T_{3tA}u-u\), \(0<t\le1/3\).

**Exercise 7 (advanced: failure at the integer dimension).** Choose a nonnegative nonzero smooth function \(a\) compactly supported in \(1<|y|<2\), and let \(R_k=4^k\). Set
\[
u_N(x)=\sum_{k=1}^N R_k^{-n}a(x/R_k)e^{-i|x|^2/4}.
\]
Show that all derivative supremum norms through order \(n\) are bounded independently of \(N\), while \(|(T_{iI}u_N)(0)|\to\infty\). Keep the kernel phase and normalization exact.

**Exercise 8 (advanced: the rank endpoint).** Let \(1\le r<n\), \(C=\operatorname{diag}(I_r,0)\), and write \(x=(y,z)\in\mathbb R^r\times\mathbb R^{n-r}\). Adapt the previous construction, using a fixed compactly supported smooth function \(b(z)\) with \(b(0)=1\), to obtain bounded derivative supremum norms through order \(r\) and unbounded output at the origin. Explain what this says about Solution 4's strict fractional threshold.

**Exercise 9 (advanced: sharp inverse Hölder gap).** For every \(1\le r\le n\), use the finite inputs (J3) to prove a uniform bound for their exact order-\(r+\alpha\) norm, with no highest derivative supremum added. Compute \(T_{iC_r}u_{\alpha,N}(0)\) and prove both statements in (J5). Deduce that the \(1/\alpha\) loss in the rank-\(r\) estimate is optimal in order, and explain precisely how the full-rank case applies to Theorem C.

**Exercise 10 (advanced: all order time filters).** Let \(m\ge1\), \(A=R+iC\), \(R\ge0\), and \(\|C\|_{\mathrm{op}}\le1\). Suppose every \(Q_A^j u\), \(0\le j\le m\), has finite norm (C1). Prove (J6)–(J8) as identities and limits of bounded continuous representatives. If \(Q_A^{m+1}u\) has the same regularity, prove an error bound with coefficient \(m/2\) after division by \(t^m\). When \(C=0\), derive the corresponding bounds using the supremum norms of the final iterates, for every \(t>0\).

**Exercise 11 (advanced: anisotropic Gaussian peak).** Let \(B\) be real symmetric positive definite and \(u_B(x)=e^{-x^TBx}\). For any complex symmetric \(A=R+iC\) with \(R\ge0\) and any \(t\ge0\), compute \(T_{tA}u_B\) with the determinant branch continued from \(t=0\). Prove that its exact supremum norm is at most one and decreases strictly for positive time if \(A\ne0\). No commutation of \(R,C,B\) may be assumed. For \(R=0\), compute the exact peak and its large-time constant in terms of all nonzero eigenvalues of \(B^{1/2}CB^{1/2}\).

## Solutions

**Solution 1.** With \(q=(r+ic)k^2\), the Fourier transform of the plane wave is \(2\pi\delta_k\), so multiplication by the Gaussian symbol and the quadratic symbol gives
\[
\begin{gathered}
T_Au=e^{-q}u,\qquad Q_A^ju=q^ju,
\\ \|T_Au\|_\infty=e^{-rk^2}\le1.
\end{gathered} \tag{H1}
\]
These formulas include \(k=0\), \(r=0\) and \(c=0,\pm1\). The bound
\[
|e^{ikh}-1|\le\min(2,|k||h|)
\le 2^{1-\alpha}|k|^\alpha|h|^\alpha
\]
follows by splitting at \(|k||h|=2\). Thus
\[
|u|_{1+\alpha}=\|u\|_\infty+[u']_\alpha
\le1+2^{1-\alpha}|k|^{1+\alpha}.
\]
For \(N\ge1\) the exact remainder is
\[
\left(e^{-q}-\sum_{j=0}^{N-1}\frac{(-q)^j}{j!}\right)e^{ikx}.
\]
The scalar integral Taylor formula gives its coefficient as
\[
\frac{(-q)^N}{(N-1)!}\int_0^1(1-s)^{N-1}e^{-sq}\,ds.
\]
Since \(\operatorname{Re}q\ge0\), its modulus is at most \(|q|^N/N!\), independent of the size of \(r\). For \(N=0\) the empty polynomial leaves \(e^{-q}u\), bounded by one. The general Hölder bound applies as well but is less sharp for this particular eigenfunction.

**Solution 2.** Let \(|\beta|=n\), choose \(j\) with \(\beta_j>0\), and put \(\gamma=\beta-e_j\). For \(v=\partial^\gamma u\), the fundamental theorem of calculus on the unit segment gives
\[
v(x+e_j)-v(x)=\int_0^1\partial^\beta u(x+te_j)\,dt.
\]
Subtracting \(\partial^\beta u(x)\) from the integral and applying the Hölder seminorm yields
\[
\begin{gathered}
|\partial^\beta u(x)|
\\ \le2\|\partial^\gamma u\|_\infty
+\frac{[\partial^\beta u]_\alpha}{1+\alpha}.
\end{gathered} \tag{H2}
\]
Both quantities on the right belong to the original norm. Summing the finitely many multiindices shows that the norm formed by adding all order-\(n\) supremum norms is bounded by \(C_n|u|_{n+\alpha}\), uniformly in \(\alpha\); the reverse comparison is immediate. Thus the two finite-norm conditions are equivalent here. This is a derived estimate, not an extra hypothesis. Theorem C's moment-cancellation argument already subtracts the whole degree-\(n\) Taylor polynomial and bounds only the order-\(n\) differences, so its proof works directly with the original norm.

**Solution 3.** The chain rule and the change of variables in the difference quotient give the exact equality
\[
\begin{gathered}
|u_L|_\mu
\\ =\sum_{|\beta|<n}L^{|\beta|}\|\partial^\beta u\|_\infty
\\ {}+L^\mu\sum_{|\beta|=n}[\partial^\beta u]_\alpha.
\end{gathered} \tag{H3}
\]
The Fourier scaling formula is \(\widehat{u_L}(\xi)=L^{-n}\widehat u(\xi/L)\), understood by duality for tempered distributions. Substitute \(\xi=L\eta\) into the inverse transform to obtain
\[
T_Au_L(x)=(T_{L^2A}u)(Lx).
\tag{H4}
\]
This equality is distributional first, and equality of the continuous representatives follows from Theorem C. Its general bound, with \(M=L^2\|C\|_{\mathrm{op}}\), gives
\[
\begin{gathered}
\|T_Au_L\|_\infty
\\ \le\frac{C_n(1+L^2\|C\|_{\mathrm{op}})^{n/2}}{\alpha}|u|_\mu.
\end{gathered} \tag{H5}
\]
If \(\|C\|_{\mathrm{op}}\le1\), applying the original estimate directly to \(u_L\) gives the further bound \(C_n|u_L|_\mu/\alpha\); both are valid. For \(L\ge1\), every exponent \(|\beta|-\mu\) below order \(n\) is negative, while the highest seminorm scales by exactly \(L^0\). Therefore \(|L^{-\mu}u(L\cdot)|_\mu\le|u|_\mu\). This normalization concerns the input norm; (H4) still retains the quadratic scale \(L^2A\).

**Solution 4.** Diagonalize \(C\) by an orthogonal real coordinate change, with eigenvalues \(\lambda_1,\ldots,\lambda_r\ne0\) and the others zero. The radial band cutoffs can be chosen unchanged by that change. Choose a one-dimensional smooth cutoff \(\eta_1\) equal to one on \([-2,2]\), supported in \([-4,4]\), and use
\[
\eta(\zeta)=\prod_{l=1}^n\eta_1(\zeta_l).
\]
It equals one on the support of every rescaled band cutoff. The compact symbol
\(\eta(\zeta)\exp(-i2^{2j}\sum_l\lambda_l\zeta_l^2)\)
factors into \(n\) one-dimensional symbols. The weighted Plancherel estimate in Theorem C, applied in dimension one, gives the \(L^1\) norm of each inverse kernel at most \(C(1+2^{2j}|\lambda_l|)^{1/2}\). One can take the spatial weight exponent \(s=1>1/2\), so only a fixed finite number of derivatives is used. The factors with \(\lambda_l=0\) have one fixed \(L^1\) norm. Fubini, the orthogonal Jacobian one and the band dilation therefore give
\[
\begin{gathered}
\|q_j\|_1
\\ \le C_n\prod_{l=1}^r(1+2^{2j}|\lambda_l|)^{1/2}
\\ \le C_n2^{jr},\qquad j\ge1.
\end{gathered} \tag{H6}
\]
Changing coordinates in derivative tensors alters the summed seminorms by at most a dimension-dependent constant: each coordinate derivative is a finite sum with coefficients from an orthogonal matrix, and Euclidean distances are preserved.

The original band amplitude is \(C_n2^{-j\mu}|u|_\mu\). Its product with (H6) is summable and yields
\[
\begin{gathered}
\|T_Au\|_\infty
\\ \le C_n\left(1+\frac1{2^{\mu-r}-1}\right)|u|_\mu,
\\ \mu=n+\alpha.
\end{gathered} \tag{H7}
\]
The real part is still a probability-measure convolution and cannot increase the supremum. No commutation of \(R,C\) as matrices is needed. If \(r<n\), \(\mu-r\ge n-r>0\), so the displayed factor is uniformly bounded as \(\alpha\downarrow0\).

For \(1\le r\le n\), define instead
\[
|u|_{r+\alpha}
=\sum_{|\beta|<r}\|\partial^\beta u\|_\infty
+\sum_{|\beta|=r}[\partial^\beta u]_\alpha.
\]
The exact order-\(r\) Taylor difference formula and cancellation of the entire degree-\(r\) polynomial give band amplitudes \(C_{n,r}2^{-j(r+\alpha)}|u|_{r+\alpha}\). Repeat the preceding kernel and reconstruction proof; \(\sum_{j\ge1}2^{-j\alpha}=(2^\alpha-1)^{-1}\le(\alpha\log2)^{-1}\). Thus the lower-order norm suffices, with bound \(C_{n,r}|u|_{r+\alpha}/\alpha\). All distributional identifications and uniform convergence follow exactly as in Theorem C. When \(r=0\), \(C=0\) and \(T_A=T_R\) is the positive-real heat convolution, including its point-mass factors. It satisfies \(\|T_Ru\|_\infty\le\|u\|_\infty\) for bounded continuous \(u\), with no fractional derivative condition.

**Solution 5.** The real part is \(R=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)\), positive definite because its first leading minor is two and its determinant is one. The imaginary part \(C=\operatorname{diag}(1,-1)\) has operator norm one. Both are symmetric. Their products are
\[
RC=\begin{pmatrix}2&-1\\1&-1\end{pmatrix},
\qquad CR=\begin{pmatrix}2&1\\-1&-1\end{pmatrix},
\]
which differ. Thus the example does not allow simultaneous diagonalization of \(R,C\).

More generally, for \(b>0\), the transform of \(e^{-b|x|^2}\) is \((\pi/b)^{n/2}e^{-|\xi|^2/(4b)}\). Multiply by \(e^{-\xi^TA\xi}\) and apply the positive-real complex Gaussian formula to \(A+(4b)^{-1}I\). Including its inverse Fourier factor gives
\[
\begin{gathered}
T_A(e^{-b|x|^2})=g(I+4bA)^{-1}
\\ {}\cdot\exp\bigl(-b\,x^T(I+4bA)^{-1}x\bigr).
\end{gathered} \tag{H8}
\]
where \(g(J)\) is the determinant square root normalized on positive real matrices, as in the full Gaussian proof. Its real part is positive definite, so that branch is defined.

In the question \(b=1\), and
\[
\begin{gathered}
J=I+4A=\begin{pmatrix}9+4i&4\\4&5-4i\end{pmatrix},
\\ \det J=45-16i.
\end{gathered}
\]
\[
\begin{gathered}
J^{-1}=\frac1{45-16i}
\\ {}\cdot\begin{pmatrix}5-4i&-4\\-4&9+4i\end{pmatrix}.
\end{gathered} \tag{H9}
\]
To specify the root without a phase guess, turn on \(C\) along \(J(t)=I+4R+4itC\), \(0\le t\le1\). Its determinant is \(29+16t^2-16it\), always in the right half-plane. At \(t=0\), the Gaussian branch is the positive root \(\sqrt{29}\). Along this path it is consequently the right-half-plane continuation, namely the principal root of \(45-16i\) at \(t=1\). Formula (H8) with (H9) is the desired full function. For \(x=(1,-1)\), its quadratic numerator is \(5-4i+8+9+4i=22\), so
\[
\begin{gathered}
(T_Au)(1,-1)
\\ =\frac{\exp(-22/(45-16i))}{\sqrt{45-16i}}.
\end{gathered} \tag{H10}
\]
with precisely that root.

**Solution 6.** Use Theorem D for \(sA\), \(0\le s\le1\); its bound can equivalently be written with \(s^N|Q_A^Nu|_\mu\). For \(N=2\),
\[
\begin{gathered}
T_{sA}u=u-sQ_Au+E_2(s),
\\ \|E_2(s)\|_\infty
\\ \le\frac{C_n}{2\alpha}s^2|Q_A^2u|_\mu.
\end{gathered}
\]
The coefficients \(2,-1\) at \(s=t,2t\) preserve the constant term and cancel the linear term. Hence
\[
\begin{gathered}
\|2T_{tA}u-T_{2tA}u-u\|_\infty
\\ \le\frac{3C_n}{\alpha}t^2|Q_A^2u|_\mu.
\end{gathered} \tag{H11}
\]
Theorem D's uniform time continuity at zero gives
\[
\begin{gathered}
\frac{E_2(s)}{s^2}
\\ =\int_0^1(1-v)T_{vsA}Q_A^2u\,dv
\\ \longrightarrow\frac12Q_A^2u
\\ \text{in the supremum norm}.
\end{gathered}
\]
Combining the limits with the coefficients yields
\[
\begin{gathered}
t^{-2}(2T_{tA}u-T_{2tA}u-u)
\\ \longrightarrow-Q_A^2u.
\end{gathered} \tag{H12}
\]

Through order three, write
\[
\begin{gathered}
T_{sA}u=u-sQ_Au+\frac{s^2}{2}Q_A^2u+E_3(s),
\\ \|E_3(s)\|_\infty
\\ \le\frac{C_n}{6\alpha}s^3|Q_A^3u|_\mu.
\end{gathered}
\]
The coefficients \(3,-3,1\) at \(s=t,2t,3t\) have sums \(1,0,0\) after multiplication by \(1,s,s^2\), respectively. The absolute cubic remainder weights are \(3+24+27=54\). Therefore
\[
\begin{gathered}
\left\|\begin{gathered}
3T_{tA}u-3T_{2tA}u
\\ {}+T_{3tA}u-u
\end{gathered}\right\|_\infty
\\ \le\frac{9C_n}{\alpha}t^3|Q_A^3u|_\mu.
\end{gathered} \tag{H13}
\]
The integral remainder divided by \(s^3\) tends uniformly to \(-Q_A^3u/6\). Its signed cubic weights are \(3-24+27=6\), giving the uniform limit
\[
\begin{gathered}
t^{-3}\left(\begin{gathered}
3T_{tA}u-3T_{2tA}u
\\ {}+T_{3tA}u-u
\end{gathered}\right)
\\ \longrightarrow-Q_A^3u.
\end{gathered} \tag{H14}
\]
The restrictions \(2t\le1\), \(3t\le1\) ensure the imaginary-matrix hypotheses for every time used. All intermediate iterates required by Theorem D have been retained.

**Solution 7.** Every \(u_N\) is smooth and compactly supported. Its summands have disjoint supports because the annuli \(R_k<|x|<2R_k\) are separated by \(R_{k+1}=4R_k\). For a derivative of order \(l\le n\), split \(q\) derivatives onto the rescaled amplitude and \(l-q\) onto the exponential. The amplitude contributes \(R_k^{-n-q}\). Derivatives of \(e^{-i|x|^2/4}\) are that exponential times a polynomial of degree at most \(l-q\); on the support their modulus is at most \(C_lR_k^{l-q}\). Thus every product term is bounded by
\[
C_{a,n}R_k^{l-n-2q}\le C_{a,n},
\tag{H15}
\]
since \(R_k\ge1\). At any point at most one summand is nonzero. The finitely many derivative terms and multiindices give
\(\sup_N\sum_{|\beta|\le n}\|\partial^\beta u_N\|_\infty<\infty\).

The signed Fresnel kernel, with the inverse factor \((2\pi)^{-n}\), is
\[
\begin{gathered}
K_n(x)=\mathcal F^{-1}(e^{-i|\xi|^2})(x)
\\ =(4\pi)^{-n/2}e^{-in\pi/4}e^{i|x|^2/4}.
\end{gathered} \tag{H16}
\]
It follows either from the full boundary Gaussian formula or its products in the coordinates. Convolution with the compactly supported input is an ordinary finite absolutely convergent integral, and represents the full distributional multiplier. At the origin the two chirp phases cancel:
\[
\begin{gathered}
(T_{iI}u_N)(0)
\\ =(4\pi)^{-n/2}e^{-in\pi/4}
\\ {}\cdot\sum_{k=1}^N R_k^{-n}\int a(x/R_k)\,dx
\\ =(4\pi)^{-n/2}e^{-in\pi/4}N
\\ {}\cdot\int a(y)\,dy.
\end{gathered} \tag{H17}
\]
The last integral is positive. The outputs are unbounded although the integer \(C^n\) supremum norms are uniformly bounded. This rules out a uniform estimate with those integer norms in place of the strict fractional norm. It does not assert a common compact support for the sequence: the supports expand with \(N\).

**Solution 8.** Choose the annular function \(a\) now in \(\mathbb R^r\) and set
\[
\begin{gathered}
u_N(y,z)=\sum_{k=1}^N R_k^{-r}a(y/R_k)
\\ {}\cdot e^{-i|y|^2/4}b(z).
\end{gathered} \tag{H18}
\]
For derivatives of total order at most \(r\), put \(l\) derivatives in \(y\) and the remaining ones in \(z\). The latter give a fixed bounded derivative of \(b\), and the former obey (H15) with \(n\) replaced by \(r\). The \(y\)-annuli are disjoint, so all these supremum norms are bounded independently of \(N\). Each function is smooth and compactly supported, although there is again no common compact support as \(N\) grows.

The multiplier \(e^{-i|\xi_y|^2}\) is independent of \(\xi_z\), so its inverse kernel is \(K_r(y)\otimes\delta_0(z)\), with the exact \(K_r\) in (H16). The ordinary compact-support convolution in \(y\) and evaluation \(b(0)=1\) give
\[
\begin{gathered}
(T_{iC}u_N)(0,0)
\\ =(4\pi)^{-r/2}e^{-ir\pi/4}N
\\ {}\cdot\int_{\mathbb R^r}a(y)\,dy.
\end{gathered} \tag{H19}
\]
Its modulus diverges. Thus even with additional nonoscillatory coordinates the rank-\(r\) integer norm cannot give a uniform bound. The fractional condition \(r+\alpha\), \(\alpha>0\), in Solution 4 avoids exactly this endpoint obstruction. The construction makes no claim that these integer-norm-bounded functions have uniformly bounded fractional norms.

**Solution 9.** Define the required norm explicitly by
\[
\begin{gathered}
|v|_{r+\alpha}\\
=\sum_{|\beta|<r}\|\partial^\beta v\|_\infty\\
{}+\sum_{|\beta|=r}[\partial^\beta v]_\alpha.
\end{gathered}
\tag{J9}
\]
The derivatives and the distances in its seminorms use all \(n\) physical coordinates. Let \(f_k\) be the \(k\)th summand in (J3). Each is smooth and compactly supported, and the supports in the \(y\) variables are disjoint. Consequently the finite sum is a Schwartz function.

On the support of \(a(y/R_k)\), one has \(R_k<|y|<2R_k\). A derivative of order \(l_y\) in \(y\) of the quadratic exponential is a polynomial of degree at most \(l_y\), multiplied by the exponential. A term with \(q\) derivatives on the amplitude has the extra factor \(R_k^{-q}\), while the remaining phase polynomial has degree at most \(l_y-q\). Derivatives in \(z\) affect only the fixed \(b\). The finite product rule therefore gives, for every multi-index \(\beta\) of total order \(l\le r+1\),
\[
\|\partial^\beta f_k\|_\infty
\le C R_k^{l-r-\alpha}.
\tag{J10}
\]
Here and below constants depend on \(a,b,n,r\), and remain independent of \(k,N,\alpha\). The bound follows term by term from the exponent \(l_y-r-\alpha-2q\le l-r-\alpha\); all fixed amplitude derivatives are bounded. It holds globally because the smooth amplitude is zero off its annulus.

For \(|\beta|<r\), disjointness at every point bounds the supremum norm of the sum by one constant. For \(|\beta|=r\), put \(v_k=\partial^\beta f_k\). Equation (J10), followed by the fundamental theorem of calculus along the segment between two points \(p,q\in\mathbb R^n\), yields, with \(d=|p-q|\),
\[
\begin{gathered}
|v_k(p)-v_k(q)|\\
\le C\min(2R_k^{-\alpha},R_k^{1-\alpha}d)\\
\le 2C d^\alpha.
\end{gathered}
\tag{J11}
\]
For \(R_kd\le1\), divide the second term by \(d^\alpha\) to get \((R_kd)^{1-\alpha}\le1\). For \(R_kd\ge1\), the first term gives \(2(R_kd)^{-\alpha}\le2\). This proves the stated constant uniformly for all \(0<\alpha<1\), without estimating a supremum for the entire highest derivative separately in the input norm.

At the two endpoints \(p,q\), at most two summands can be nonzero, including their derivatives. Every other summand has zero difference there. Summing (J11) for those at most two indices proves \([\partial^\beta u_{\alpha,N}]_\alpha\le4C\). The finite number of derivatives in (J9) thus gives a constant \(C_0\) such that
\[
\begin{gathered}
|u_{\alpha,N}|_{r+\alpha}\le C_0\\
\text{for every }N\ge1,\ 0<\alpha<1.
\end{gathered}
\tag{J12}
\]

The signed Fresnel calculation G and Solution 8 give the exact kernel \(\kappa_r e^{i|y|^2/4}\otimes\delta_0(z)\) of \(T_{iC_r}\). Since our input is compactly supported, its value at the origin is an ordinary finite integral. The phase cancels, \(b(0)=1\), and the real substitution \(y=R_k w\) contributes the Jacobian \(R_k^r\). Thus each summand contributes precisely \(\kappa_r I_a R_k^{-\alpha}\). Summing the geometric progression proves (J4).

For \(N=\lceil1/\alpha\rceil\), the numerator \(1-4^{-N\alpha}\) is at least \(3/4\). Convexity of \(4^s\) on \([0,1]\) bounds it above by its chord, so \(4^\alpha-1\le3\alpha\). This proves the lower bound in (J5). Also \(1\le\alpha\lceil1/\alpha\rceil<1+\alpha\), so the numerator tends to \(3/4\). The elementary exponential difference quotient gives \((4^\alpha-1)/\alpha\to\log4\), proving the exact limit.

It follows from (J12) that the best constant in a bound \(\|T_{iC_r}v\|_\infty\le K_r(\alpha)|v|_{r+\alpha}\) must satisfy \(K_r(\alpha)\ge |\kappa_r|I_a/(4C_0\alpha)\). The upper bound \(C_{n,r}/\alpha\) is proved in Solution 4 by the full rank-specific band and product-kernel argument. Hence the order \(1/\alpha\) is optimal for every positive rank. For \(r=n\), (J9) is exactly (C1), and \(\|C_r\|_{\mathrm{op}}=1\); Theorem C has a sharp order of dependence on its Hölder gap. For \(r<n\), the separate order-\(n+\alpha\) conclusion in Solution 4 uses additional derivatives and remains consistent with its bounded constant. \(\square\)

**Solution 10.** Write \(Q=Q_A(D)\). Scalar multiplier multiplication gives the semigroup identity \(T_{sA}T_{vA}=T_{(s+v)A}\) on \(\mathcal S'\). The binomial identity consequently proves (J6). For \(q=\xi^TA\xi\), the scalar fundamental theorem gives
\[
\begin{gathered}
1-e^{-tq}=q\int_0^t e^{-sq}\,ds,\\
(1-e^{-tq})^m\\
=q^m\int_{[0,t]^m}e^{-(s_1+\cdots+s_m)q}\,ds.
\end{gathered}
\tag{J13}
\]
Every frequency derivative of these multipliers has polynomial growth, uniformly when \(s_j\in[0,t]\): the real part of \(q\) is nonnegative, and a differentiated exponential contributes only polynomial factors. Pairing with a Schwartz test therefore allows differentiation and parameter integration in the Schwartz topology. Applying (J13) to the tempered input proves the distributional identity
\[
\begin{gathered}
L_{m,t}u\\
=\int_{[0,t]^m}T_{(s_1+\cdots+s_m)A}\\
{}\qquad\cdot Q^m u\,ds.
\end{gathered}
\tag{J14}
\]
The final iterate has exactly the regularity required by Theorem C. The time-continuity proof in Theorem D applies to that iterate and makes the integrand a continuous function into \(C_b(\mathbb R^n)\) for \(0\le s_1+\cdots+s_m\le mt\le1\). Its cube integral is an actual limit of Riemann sums in the supremum norm. Testing those sums identifies it with the distributional integral just proved. Thus (J14) holds for the bounded continuous representatives themselves.

Theorem C bounds each integrand by \(C_n|Q^m u|_{n+\alpha}/\alpha\), proving (J8) after multiplying by the cube volume \(t^m\). The substitution \(s_j=tv_j\) expresses \(t^{-m}L_{m,t}u\) as the average of \(T_{t(v_1+\cdots+v_m)A}Q^m u\) over the unit cube. Uniform time continuity at zero proves its uniform limit \(Q^m u\).

If the next iterate has the same regularity, Theorem D with order one, applied to \(Q^m u\) and matrix \(sA\), gives \(\|T_{sA}Q^m u-Q^m u\|_\infty\le C_n s|Q^{m+1}u|_{n+\alpha}/\alpha\) for \(0\le s\le1\). Integrating the sum of the \(m\) unit-cube coordinates gives \(m/2\), and hence
\[
\begin{gathered}
\|t^{-m}L_{m,t}u-Q^m u\|_\infty\\
\le\frac{C_n m t}{2\alpha}|Q^{m+1}u|_{n+\alpha}.
\end{gathered}
\tag{J15}
\]
For \(C=0\), every \(T_{sR}\) is convolution with the probability measure in (C12), so (J14) gives \(\|L_{m,t}u\|_\infty\le t^m\|Q^m u\|_\infty\). For the error, the scalar order-one identity gives \(T_{sR}Q^m u-Q^m u=-\int_0^s T_{vR}Q^{m+1}u\,dv\), whose norm is at most \(s\|Q^{m+1}u\|_\infty\). Cube averaging now bounds the error by \((m/2)t\|Q^{m+1}u\|_\infty\). These statements hold for every \(t>0\): on each finite time interval the same multiplier argument applies, and time continuity follows from the earlier proof with the rescaled real matrix. The stated iterated regularity hypotheses ensure that all participating functions are bounded and continuous. \(\square\)

**Solution 11.** Let \(g(S)\) denote the square root of \(\det S\) on the complex symmetric domain \(\operatorname{Re}S>0\), normalized positively on real positive definite matrices, as fully constructed in Sections 2–3 of the Gaussian-kernel lesson. The Gaussian transform is \(\widehat u_B(\xi)=\pi^{n/2}g(B)^{-1}\exp(-\xi^TB^{-1}\xi/4)\). Multiplying by \(e^{-t\xi^TA\xi}\) leaves an absolutely integrable Gaussian with matrix \(J/4\), where
\[
\begin{gathered}
J=B^{-1}+4tA,\\
\operatorname{Re}J>0,\\
T_{tA}u_B(x)\\
=\frac{\exp(-x^TJ^{-1}x)}{g(B)g(J)}.
\end{gathered}
\tag{J16}
\]
Indeed the inverse integral has factor \((2\pi)^{-n}\pi^{n/2}/g(B)\), and its Gaussian integral contributes \(\pi^{n/2}/g(J/4)\), with \(g(J/4)=2^{-n}g(J)\). These constants give exactly (J16). Its branch equals the original input at \(t=0\).

U020's proved real spectral theorem writes \(B=O\operatorname{diag}(b_j)O^T\), with \(b_j>0\). Thus \(B^{1/2}=O\operatorname{diag}(\sqrt{b_j})O^T\) is symmetric positive definite and has square \(B\); replacing the roots by their reciprocals gives \(B^{-1/2}\). Set \(Z=4B^{1/2}AB^{1/2}\) and \(M=I+tZ=B^{1/2}JB^{1/2}\). Then \(\operatorname{Re}M\ge I\), so \(M\) is invertible. The determinant identity and continuity along \(t\ge0\) show that \(g(M)=g(B)g(J)\): both squares equal \(\det M\), and both values at zero are one. Also \(J^{-1}=B^{1/2}M^{-1}B^{1/2}\). Thus the exponent retains all anisotropic factors.

The elementary identity \(\operatorname{Re}J^{-1}=J^{-*}(\operatorname{Re}J)J^{-1}>0\), proved in the Gaussian-kernel lesson, shows that the modulus of the exponential is at most one for real \(x\), with equality exactly at \(x=0\). Consequently the measured peak is
\[
\begin{gathered}
P_B(t)=\|T_{tA}u_B\|_\infty\\
=|\det(I+tZ)|^{-1/2}\\
=|g(M)|^{-1}.
\end{gathered}
\tag{J17}
\]
To bound it without a commutation hypothesis, write \(H=\operatorname{Re}M\ge I\), \(K=\operatorname{Im}M\), and \(E=H^{-1/2}KH^{-1/2}\). This \(E\) is real symmetric. Orthogonally diagonalizing it with eigenvalues \(\eta_1,\ldots,\eta_n\) in the factorization \(M=H^{1/2}(I+iE)H^{1/2}\) gives
\[
\begin{gathered}
|\det M|\\
=\det H\prod_{j=1}^n\sqrt{1+\eta_j^2}\\
\ge\det H\ge1,\\
P_B(t)\le(\det H)^{-1/2}\le1.
\end{gathered}
\tag{J18}
\]
This argument diagonalizes a real symmetric auxiliary matrix and never assumes that \(R,C,B\) share eigenvectors.

For the monotonicity, differentiating the nonvanishing determinant along this path gives \((\log P_B)'=-\tfrac12\operatorname{Re}\operatorname{tr}(ZM^{-1})\). Multiplication on the left by \(M^*\) and on the right by \(M\) proves the full matrix identity
\[
\begin{gathered}
\operatorname{Re}(ZM^{-1})\\
=M^{-*}(\operatorname{Re}Z+tZ^*Z)M^{-1}.
\end{gathered}
\tag{J19}
\]
Here \(\operatorname{Re}\) of a general matrix means its Hermitian part. The identity follows because \(M^*Z+Z^*M=Z+Z^*+2tZ^*Z\). Its right side is positive semidefinite, since \(\operatorname{Re}Z=4B^{1/2}RB^{1/2}\ge0\). Its trace is at least \(t\|ZM^{-1}\|_{\mathrm{HS}}^2\), where the squared Hilbert–Schmidt norm is the sum of the squared moduli of the matrix entries. If \(A\ne0\), then \(Z\ne0\) and this last quantity is strictly positive for \(t>0\). Hence \(P_B\) decreases strictly on positive times. At zero a purely imaginary evolution can have derivative zero; that does not affect the strict decrease between distinct nonnegative times.

Finally take \(R=0\), and let \(\kappa_1,\ldots,\kappa_r\) be all the nonzero real eigenvalues of \(B^{1/2}CB^{1/2}\), with multiplicity. The remaining \(n-r\) eigenvalues vanish. Real orthogonal diagonalization now gives the exact profile and constant
\[
\begin{gathered}
P_B(t)\\
=\prod_{j=1}^r(1+16t^2\kappa_j^2)^{-1/4},\\
\lim_{t\to\infty}(4t)^{r/2}P_B(t)\\
=\left(\prod_{j=1}^r|\kappa_j|\right)^{-1/2}.
\end{gathered}
\tag{J20}
\]
For \(r=0\), both products are empty and equal one; the evolution leaves the Gaussian fixed. Taking \(B=bI\) and \(C=cI\) recovers (J1), and taking the real part of its exponent gives (J2). No bound on the size of \(C\) was required for these Gaussian identities. \(\square\)

## References

- The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, and [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.1 and 16: exact Schwartz operations, multipliers, inversion, convergence, Fubini and Jacobians.
- [Separated frequencies and distributional order](separated-frequencies-and-distributional-order.md), Lemma 0.1 and its following integrable-weight proof: complete Schwartz Plancherel with all weight coefficients. [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Section 2 and the transform part of Theorem 3.1: diagonalization, determinant differentiation, branch and complex Gaussian transform. [Quadratic phases and curved spectra](quadratic-phases-and-curved-spectra.md), Lemma 0.1 and calculation G: partial transforms and signed Fresnel identities.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercises 7.6.9–7.6.10, p. 393, and answers, p. 417. The source includes highest derivative supremum norms; Solution 2 proves their uniform equivalence with the reduced norm used here. The lesson gives independent frequency-band and operator-remainder proofs, original measurements and eleven graded problems with complete solutions.
