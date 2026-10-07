# Short-time reduction of the curved Dirichlet remainder

*Written by GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

<a id="curved-boundary-spectral-reduction"></a>

This reading proves the uniform curved Dirichlet spectral remainder in the full scalar scope below. Sections 1–4 give positive unsmoothing and the exact cosine formula. Sections 5–30 retain detailed near-normal and complementary frozen-model arguments. Sections 31–38 give a complete second construction: a finite reflected wave expansion with its actual smooth error, coarse temporal Fourier bounds, and the uniform no-return kernel estimate. Together they prove (B16) and both bounds in (B138), including the wall and the interior. 

The operator has the full scope used in [Generalized rays and the Dirichlet Weyl law](../../src/generalized-rays-and-the-dirichlet-weyl-law.md): a scalar formally self-adjoint second-order elliptic differential operator on half densities on a compact smooth manifold of dimension \(n\geq2\), with smooth boundary, no corners, and strictly positive Dirichlet realization. All smooth lower-order terms are retained. Its principal symbol defines the metric \(g\); \(d=d(x)\) is inward metric distance in a fixed collar. Every diagonal density below is relative to \(dV_g\).

Read [Smooth Dirichlet regularity, power domains, and projector growth](smooth-dirichlet-powers.md), Sections 4–6, first. It proves the exact spectral realization, smooth eigenfunctions, and the uniform diagonal bound used here. The positive-measure argument develops the cumulative version of [Return times and spectral counting](../../src/return-times-and-spectral-counting.md), Lemma 1.1. Section 5 uses the already proved [parameter Morse lemma](phase-geometry-and-stationary-phase.md#parameter-morse) and [stationary phase with parameter remainders](phase-geometry-and-stationary-phase.md#stationary-phase), equations (P1)–(P10). None of these inputs requires the curved estimate being reduced.

<a id="positive-reflected-measure"></a>
## 1. The positive measure and the reflected model

Write the orthonormal eigensections as \(u_j(dV_g)^{1/2}\), with eigenvalues \(\lambda_j>0\), and put \(\kappa_j=\sqrt{\lambda_j}\). At each point define
\[
 \begin{gathered}
 \mu_x=\sum_j|u_j(x)|^2\delta_{\kappa_j},\\
 E_x(k)=\mu_x([0,k])\quad(k\geq0),\\
 E_x(k)=0\quad(k<0),\\
 0\leq E_x(k)\leq C(1+k)^n\quad(k\geq0).
 \end{gathered}
 \tag{B1}
\]
The last bound is the cited programme proof, equation (26), with spectral parameter \(k^2\); the bounded interval \(0\leq k\leq1\) is absorbed using monotonicity. Its constant is independent of \(x\), including the wall. One may instead use \([0,k)\) throughout.

The model cumulative function, extended by zero to negative arguments, is
\[
 \begin{gathered}
 M_d(k)=(2\pi)^{-n}\int_{|\xi|\leq k}
 [1-\cos(2d\xi_n)]\,d\xi,\\
 k\geq0,\\
 M_d(k)=k^n[W_n(0)-W_n(2kd)],\\
 W_n(s)=(2\pi)^{-n}\int_{|\eta|\leq1}\cos(s\eta_n)\,d\eta.
 \end{gathered}
 \tag{B2}
\]
This is the exact flat Dirichlet density proved in [Reflection and the Dirichlet boundary coefficient](../../src/reflection-and-the-dirichlet-boundary-coefficient.md), Proposition 1.1. Radial integration, rather than differentiation of the rescaled profile, gives the useful uniform estimate
\[
 \begin{gathered}
 M_d'(k)\\
 =(2\pi)^{-n}k^{n-1}\int_{S^{n-1}}
 [1-\cos(2dk\theta_n)]\,d\theta,\\
 0\leq M_d'(k)\leq C_n k^{n-1},\qquad k>0.
 \end{gathered}
 \tag{B3}
\]
The polar integration formula is proved in the [coordinate and surface-measure reading](coordinate-inverses-and-integration.md). The integrand in (B3) lies between zero and two. Thus \(M_d\) is nondecreasing, is locally absolutely continuous across zero, and obeys \(0\leq M_d(k)\leq C_n k^n\), uniformly for every \(d\geq0\). The bounds involve no derivative in \(d\).

## 2. Fixed positive smoothing and a moderate weight

Fix any sufficiently small time \(T>0\). Choose an even nonnegative nonzero smooth function \(b\) supported in \((-T/2,T/2)\), and let \(v\) be its inverse Fourier transform with convention
\(\widehat f(t)=\int e^{-its}f(s)\,ds\). Integration by parts shows that \(v\) is Schwartz; it is real and even, and \(v(0)>0\). Put \(\rho=v^2/\int v^2\). The Fourier product formula, proved by Fourier inversion and absolutely convergent integration for Schwartz functions in the [Fourier reading](finite-derivative-l2.md#fourier-normalization), gives
\[
 \begin{gathered}
 \rho\geq0,\quad \rho(-s)=\rho(s),\\
 \int\rho(s)\,ds=1,\quad
 \operatorname{supp}\widehat\rho\subset(-T,T),\\
 c_a:=\int_{-a}^{a}\rho(s)\,ds>0.
 \end{gathered}
 \tag{B4}
\]
for some fixed \(a>0\). All constants may depend on this fixed kernel and on the operator and collar. They will not depend on \(x,d,k\).

Set \(S_x=\rho*E_x\) and \(S_d^0=\rho*M_d\). Their integrals converge by (B1)–(B3). For \(d>0\) define a weight on the whole real line by
\[
 \begin{gathered}
 B_d(k)=(1+|k|)(1+|k|+d^{-1})^{n-2},\\
 (1+|k|)^{n-1}\leq B_d(k),\\
 B_d(k+s)\leq B_d(k)(1+|s|)^{n-1}.
 \end{gathered}
 \tag{B5}
\]
Indeed \(1+|k+s|\leq(1+|k|)(1+|s|)\) and
\(1+|k+s|+d^{-1}\leq(1+|k|+d^{-1})(1+|s|)\). Multiplying proves the last line, with constant one. For \(k\geq2\), \(B_d(k)\) is comparable to \(k(k+d^{-1})^{n-2}\), with constants depending only on \(n\).

The derivative estimate (B3), including the zero extension, implies
\[
 \begin{gathered}
 |M_d(k)-M_d(k-s)|\\
 \leq C|s|(1+|k|+|s|)^{n-1},\\
 |S_d^0(k)-M_d(k)|\leq C(1+|k|)^{n-1}.
 \end{gathered}
 \tag{B6}
\]
For the first line integrate (B3) over the interval between the two arguments, intersected with the positive axis. For the second line integrate against \(\rho(s)\) and use its finite moments. These bounds are uniform even when \(d\) tends to zero.

<a id="uniform-cumulative-tauberian"></a>
## 3. Removing smoothing without assuming a cluster bound

**Theorem 3.1 (uniform cumulative Tauberian reduction).** Suppose that for every point in the collar with \(d>0\),
\[
 |S_x(k)-S_d^0(k)|\leq C B_d(k),\qquad k\geq2,
 \tag{B7}
\]
with one constant independent of the point. Then for either spectral endpoint convention,
\[
 \begin{gathered}
 |E_x(k)-M_d(k)|\leq C' B_d(k),\qquad k\geq2,\\
 |E_x(k)-M_d(k)|\leq C'' k^n,\qquad k\geq2.
 \end{gathered}
 \tag{B8}
\]
At \(d=0\) both functions vanish. Conversely, the first estimate in (B8), uniformly for \(d>0\), implies (B7). Consequently the two-bound curved remainder is equivalent to (B7), given the already proved rough growth (B1).

**Proof: low and negative frequencies.** For any real \(k\leq2\), (B1) bounds \(S_x(k)\) uniformly: the integrand is zero unless \(s\leq k\), and then \(1+k-s\leq3+|s|\). Integrate \(C\rho(s)(3+|s|)^n\). The same argument applies to \(S_d^0\). Since \(B_d\geq1\), (B7) therefore holds on the whole real line after enlarging its constant. No uniform small-distance estimate is being assumed at low frequency.

**A local mass estimate from cumulative differences.** Put \(A=a+2\), where \(a\) is from (B4). Positivity gives, for any real \(r\),
\[
 \begin{gathered}
 c_a\mu_x([r-1,r+1])\\
 \leq S_x(r+A)-S_x(r-A)\\
 \leq C B_d(r).
 \end{gathered}
 \tag{B9}
\]
For the first inequality, write the difference as the integral of
\(E_x(r+A-s)-E_x(r-A-s)\) against \(\rho(s)\). When \(|s|\leq a\), its lower endpoint is strictly below \(r-1\) and its upper endpoint strictly above \(r+1\). It therefore includes every atom in that closed interval for either convention. For other \(s\) the difference is nonnegative. For the upper inequality replace both smoothed cumulative values by \(S_d^0\), using (B7) and (B5). The model difference is bounded by \(C(1+|r|)^{n-1}\): integrate (B3) over an interval of length \(2A\), then against \(\rho\). This is bounded by \(C B_d(r)\) by (B5). Thus (B9) is derived, not an extra spectral-cluster hypothesis.

Cover the interval between \(k\) and \(k-s\) by at most \(C(1+|s|)\) closed intervals of radius one, whose centers lie within \(|s|+1\) of \(k\). The variation of either cumulative convention between the two endpoints is bounded by the measure of that closed interval. Equations (B9) and (B5) give
\[
 \begin{gathered}
 |E_x(k)-E_x(k-s)|
       \leq C B_d(k)(1+|s|)^n,\\
 |E_x(k)-S_x(k)|\leq C B_d(k).
 \end{gathered}
 \tag{B10}
\]
The second line follows by integration against the positive Schwartz kernel. It also controls an atom exactly at \(k\), so no continuity of the spectral staircase was assumed. Combining (B10), (B7) and (B6) proves the first part of (B8). The second part follows directly from (B1) and (B3), since \(k\geq2\). Every Dirichlet eigenfunction is smooth and zero at the wall, so \(E_x=0\) there; (B2) gives \(M_0=0\).

For the converse, extend the assumed bound for \(E_x-M_d\) to all real arguments: both vanish at negative arguments, and their difference is uniformly bounded on \([0,2]\) by (B1) and (B3). Convolve this bound and use (B5) and the finite \((n-1)\)-st moment of \(\rho\). This proves (B7). \(\square\)

<a id="short-time-cosine-comparison"></a>
## 4. The exact short-time quantity to estimate

The uniform growth permits us to define the diagonal cosine distribution directly by
\[
 \begin{gathered}
 C_x(t)=\int_0^\infty\cos(t\kappa)\,d\mu_x(\kappa),\\
 C_d^0(t)=\int_0^\infty\cos(t\kappa)\,dM_d(\kappa).
 \end{gathered}
 \tag{B11}
\]
These are distributional integrals. Pairing with a Schwartz test function gives rapidly decreasing Fourier transforms in \(\kappa\). Splitting the positive axis into unit intervals and using (B1) or (B3) proves absolute convergence, bounded by finitely many Schwartz seminorms uniformly in \(x,d\). Thus (B11) defines tempered distributions without requiring an unproved pullback of a singular kernel to the diagonal. It is the time-tested spectral definition of the diagonal of \(\cos(t\sqrt P)\). The pairing below is linear, without complex conjugation on the test function.

Let \(F(z)=\int_{-\infty}^z\rho(s)\,ds\). Positivity and interchange of the two integrals give
\[
 S_x(k)=\int_0^\infty F(k-\kappa)\,d\mu_x(\kappa).
 \tag{B12}
\]
The strict and closed conventions have the same convolution: for each fixed atom the excluded endpoint is a single integration value, of Lebesgue measure zero. The same formula holds for \(S_d^0\), with \(dM_d\).

**Theorem 4.1 (cosine formula and uniform tail).** For \(k\geq2\),
\[
 \begin{gathered}
 S_x(k)=\frac1\pi
     \left\langle C_x(t),\widehat\rho(t)\frac{\sin(kt)}t\right\rangle
     +T_x(k),\\
 T_x(k)=\int_0^\infty[1-F(k+\kappa)]\,d\mu_x(\kappa),\\
 0\leq T_x(k)\leq C_N k^{-N}\quad\text{for every }N.
 \end{gathered}
 \tag{B13}
\]
The constants are uniform up to the boundary. There is an identical formula and estimate for \(S_d^0,C_d^0,T_d^0\), uniform in \(d\geq0\).

**Proof.** Fourier inversion and evenness of \(\rho\) give, for one frequency \(\kappa\geq0\),
\[
 \begin{gathered}
 \frac1\pi\int\cos(t\kappa)\widehat\rho(t)
                  \frac{\sin(kt)}t\,dt\\
 =\int_0^k[\rho(s-\kappa)+\rho(s+\kappa)]\,ds\\
 =F(k-\kappa)+F(k+\kappa)-1.
 \end{gathered}
 \tag{B14}
\]
Here \(\sin(kt)/t=\int_0^k\cos(st)\,ds\), with value \(k\) at zero. The factor \(1/\pi\) follows from the inverse Fourier factor \(1/(2\pi)\) and the sum of the two even frequencies. The identity \(F(-\kappa)+F(\kappa)=1\) gives the final constant.

The test function \(\widehat\rho(t)\sin(kt)/t\) is smooth and supported in \((-T,T)\). For fixed \(k\), its cosine transform decays faster than any inverse power of \(\kappa\); hence (B11) allows its termwise pairing. Alternatively both expressions on the last line of (B14), after writing it as \(F(k-\kappa)-[1-F(k+\kappa)]\), are absolutely integrable against the polynomially growing positive measure. Integration of (B14) therefore proves (B13).

For the tail, \(1-F(z)\leq C_L(1+z)^{-L}\) for \(z\geq0\). The mass of \([m,m+1]\) is at most \(C(m+2)^n\), uniformly in the point, by (B1). Counting shared endpoints twice only enlarges the positive bound. Consequently
\[
 \begin{gathered}
 T_x(k)\leq C_L\sum_{m=0}^\infty
               (m+2)^n(k+m)^{-L}\\
 \leq C_L' k^{n+1-L},\qquad L>n+1.
 \end{gathered}
 \tag{B15}
\]
For the last inequality split at \(m\leq k\); the first sum has at most \(k+1\) terms bounded by \(C k^{n-L}\), and the remaining power sum is bounded by its convergent integral. Choose \(L\geq N+n+1\), increasing it strictly above \(n+1\) if needed. Equation (B3) gives the same interval-mass bound for the model. \(\square\)

Combining the two theorems yields an exact reduction of the required curved estimate. It suffices, and is necessary up to a change of constant, to prove
\[
 \begin{gathered}
 \left|\frac1\pi\left\langle C_x-C_d^0,
 \widehat\rho(t)\frac{\sin(kt)}t\right\rangle\right|\\
 \leq C B_d(k),\qquad k\geq2,\ d>0.
 \end{gathered}
 \tag{B16}
\]
The rapid tails in (B13) are absorbed because \(B_d\geq1\). With \(h=k^{-1}\), the size required on the right is comparable to
\[
 h^{1-n}(1+h/d)^{n-2}.
 \tag{B17}
\]
This reduction retains the metric-volume normalization and the full operator scope. Knowledge of the wavefront relation alone does not estimate (B16).

<a id="uniform-reflected-freezing"></a>
## 5. A quantitative reflected-phase freezing lemma

Here the distance \(d\) is a smooth parameter; this section is an oscillatory-integral lemma, with no assumed representation of the actual kernel. Fix \(0<E_0<1\). Let \(y\) range over a compact parameter set, let \(0\leq d\leq d_0\), and let \(\zeta\in\mathbb R^{n-1}\). Suppose the real phase \(\phi(d,y,\zeta,E)\) and amplitude \(A(d,y,\zeta,E)\) are smooth for \(E\in[E_0,1]\). The amplitude has uniformly compact \(\zeta\)-support and vanishes in a fixed neighborhood of \(E_0\). On a fixed neighborhood of its support suppose there is a smooth single critical branch \(\zeta_c(d,y,E)\), with uniformly invertible \(\zeta\)-Hessian. Away from a fixed neighborhood of this branch, assume \(|\partial_\zeta\phi|\) has a positive uniform lower bound on the support. Assume, crucially,
\[
 \begin{gathered}
 \phi(d,y,\zeta_c(d,y,E),E)=\Phi(y,E),\\
 |\partial_E\Phi(y,E)|\geq c>0.
 \end{gathered}
 \tag{B18}
\]
Thus the critical action is independent of \(d\). All necessary finite derivatives and inverse-Hessian bounds are uniform on the compact parameter set. Finitely many branches can be treated by a fixed partition and addition. Uniform extra parameters in the amplitudes are allowed with the same bounds.

Define, for \(r>0\),
\[
 \begin{gathered}
 J(d,y,r)=\int_{E_0}^1 I(d,y,E,r)\,dE,\\
 I(d,y,E,r)\\
 =\int_{\mathbb R^{n-1}}e^{ir\phi(d,y,\zeta,E)}
 A(d,y,\zeta,E)\,d\zeta.
 \end{gathered}
 \tag{B19}
\]

**Lemma 5.1 (fixed-action freezing).** Under these hypotheses,
\[
 \begin{gathered}
 |J(d,y,r)-J(0,y,r)|\\
 \leq C d\min\{1,r^{-(n+1)/2}\}.
 \end{gathered}
 \tag{B20}
\]
In particular, for \(0<h\leq1\), uniformly in \(0<d\leq d_0\),
\[
 h^{-n}|J(d,y,d/h)-J(0,y,d/h)|\leq C h^{1-n}.
 \tag{B21}
\]

**Proof.** For \(0<r\leq1\), differentiate the integrand in \(d\). The derivative is
\(e^{ir\phi}(\partial_d A+irA\partial_d\phi)\), whose integral is uniformly bounded because the integration region is fixed and compact. The fundamental theorem of calculus on \([0,d]\) proves (B20) in this range.

For \(r\geq1\), apply the parameter Morse and stationary-phase proof cited above, in \(m=n-1\) variables, with parameters \((d,y,E)\). After removing the critical exponential it gives an exact representation
\[
 \begin{gathered}
 I(d,y,E,r)=e^{ir\Phi(y,E)}b(d,y,E,r),\\
 |\partial_d^a\partial_E^j b(d,y,E,r)|
 \leq C_{a,j}r^{-(n-1)/2},\\
 a,j\in\{0,1\}.
 \end{gathered}
 \tag{B22}
\]
These bounds include the mixed derivative. To see explicitly why the remainder has this property, use the smooth Morse coordinates of (P1) to replace the phase near the branch by its critical value plus a fixed nondegenerate quadratic form. The Jacobian and transformed amplitude have uniform parameter derivatives. Equations (P4)–(P8) give the asserted bounds for this quadratic integral. On the complement, repeated integration by parts using (P10) gives arbitrary decay even after differentiating in \(d,E\) and removing \(e^{ir\Phi}\); any finitely many extra powers of \(r\) are absorbed by additional integrations. A finite parameter cover gives the uniform constants. This also shows that \(b\) vanishes near \(E_0\). No derivative of a moving critical exponential is hidden in (B22).

Put \(D(E)=b(d,y,E,r)-b(0,y,E,r)\). Integration of the \(d\)-derivative in (B22) gives
\(|D|+|\partial_E D|\leq C d r^{-(n-1)/2}\). Because the same \(\Phi\) occurs at both distances, integration by parts in energy gives
\[
 \begin{gathered}
 J(d,y,r)-J(0,y,r)\\
 =\left[\frac{e^{ir\Phi}D}{ir\partial_E\Phi}\right]_{E_0}^1\\
 -\frac1{ir}\int_{E_0}^1 e^{ir\Phi}
 \partial_E\!\left(\frac D{\partial_E\Phi}\right)dE.
 \end{gathered}
 \tag{B23}
\]
The lower endpoint is zero; the upper endpoint is retained. The lower bound in (B18) and bounded second energy derivative of \(\Phi\) prove the remaining part of (B20).

For (B21), if \(d\leq h\), use \(h^{-n}d\leq h^{1-n}\). If \(d\geq h\), the other part of (B20) gives
\[
 \begin{gathered}
 h^{-n}d(h/d)^{(n+1)/2}\\
 =h^{1-n}(h/d)^{(n-1)/2}\leq h^{1-n}.
 \end{gathered}
 \tag{B24}
\]
The comparison is zero at \(d=0\) by its definition before substitution. This completes the proof. \(\square\)

The fixed-action assumption is substantial. Even a difference of order \(d\) between critical values can produce an additional factor \(rd\) when exponentials are subtracted. Smooth coefficients alone therefore do not justify (B20). For the actual boundary kernel one must construct the relevant phase patches, identify the common critical action, verify the parameter bounds, handle all other patches, and control the exact operator remainder in (B16). A formal frozen amplitude is not that construction.

<a id="actual-near-normal-phase"></a>
## 6. Constructing the two phases from the metric

Write a boundary normal chart as \((a,z)\), where \(a\geq0\) is distance and \(z\in\mathbb R^{n-1}\). Reserve \((d,y)\) for the source point. On a compact chart inside a larger one the actual principal symbol is
\[
 \begin{gathered}
 p(a,z,s,\zeta)=s^2+r(a,z,\zeta),\\
 r(a,z,\zeta)=\zeta^{\mathsf T}G(a,z)\zeta,\\
 \lambda_\sigma(a,z,\zeta,E)\\
 =\sigma\sqrt{E-r(a,z,\zeta)},\qquad\sigma=\pm1.
 \end{gathered}
 \tag{B25}
\]
Here \(G\) is real symmetric and uniformly positive. Fix \(0<E_0<1\). For \(E\in[E_0,1]\), choose a small tangential frequency ball and a short fixed collar so that \(E-r\geq E_0/2\) on a slightly larger region. Every derivative of both roots is bounded there, uniformly in all parameters. Smoothness up to the wall permits an auxiliary smooth extension for local inverse arguments at zero; none of the asserted equations uses a physical point outside the collar.

We construct an incident phase \(S^i_\sigma\) from the source normal slice, and a reflected phase \(S^r_\sigma\) from the wall:
\[
 \begin{gathered}
 \partial_a S^i_\sigma
       =\lambda_\sigma(a,z,\partial_z S^i_\sigma,E),\\
 S^i_\sigma(d,z;d,y,\eta,E)=(z-y)\cdot\eta,\\
 \partial_a S^r_\sigma
       =\lambda_\sigma(a,z,\partial_z S^r_\sigma,E),\\
 S^r_\sigma(0,z;d,y,\eta,E)
       =S^i_{-\sigma}(0,z;d,y,\eta,E).
 \end{gathered}
 \tag{B26}
\]
Both phases are real and smooth jointly in all variables for \(0\leq a,d\leq d_0\), \(y,z\) in retained chart neighborhoods, small \(\eta\), and \(E\in[E_0,1]\). The same neighborhood works at \(d=0\). The matching phases at the wall are equal; Dirichlet cancellation will put a minus sign in the amplitudes.

Here is the construction and its uniformity. For any smooth initial function \(f(w)\) on the slice \(a=a_0\), solve
\[
 \begin{gathered}
 Z'=-\partial_\zeta\lambda_\sigma(a,Z,\Xi,E),\\
 \Xi'=\partial_z\lambda_\sigma(a,Z,\Xi,E),\\
 Z(a_0)=w,\qquad \Xi(a_0)=df(w),\\
 s(a)=f(w)+\int_{a_0}^{a}\Xi(v)\cdot Z'(v)\,dv\\
 +\int_{a_0}^{a}\lambda_\sigma(v,Z(v),\Xi(v),E)\,dv.
 \end{gathered}
 \tag{B27}
\]
The contraction and differentiated integral-equation proof in [Existence and compactness of generalized reflected curves](generalized-reflected-curves.md#generalized-reflected-curves), equation (G13), supplies this smooth flow with smooth dependence on the initial slice and every displayed parameter. Its constants are uniform on the larger compact region. At \(a=a_0\), the derivative \(Z_w\) is the identity. Bounded differentiated flow equations therefore give \(Z_w=I+O(|a-a_0|)\) for the bounded initial families used here. Choose the collar once so that this matrix stays invertible. The [parameter inverse proof](coordinate-inverses-and-integration.md) then solves \(Z(a,w)=z\) smoothly for \(w\).

Define \(S(a,z)=s(a,w(a,z))\). Varying \(w\) under the action integral shows \(d_ws(a)=\Xi(a)d_wZ(a)\): the variation of its integrand is the derivative of \(\Xi\cdot\delta Z\), because \(Z'=-\lambda_\zeta\) and \(\Xi'=\lambda_z\); its initial endpoint cancels \(df=\Xi(a_0)dw\). It follows that
\[
 \begin{gathered}
 \partial_zS=\Xi(a,w(a,z)),\\
 \partial_aS=\lambda_\sigma(a,z,\partial_zS,E).
 \end{gathered}
 \tag{B28}
\]
The second identity follows by differentiating \(Z(a,w(a,z))=z\) at fixed \(z\), so the action's \(\Xi\cdot Z'\) term cancels. Conversely, the gradient of any solution of this initial problem follows (B27), by differentiating its equation. Flow uniqueness and the initial value give uniqueness of \(S\).

First apply this construction to \(f(w)=(w-y)\cdot\eta\) and \(a_0=d\). Its parameter derivatives are bounded. Then take the resulting smooth boundary value \(f(w)=S^i_{-\sigma}(0,w;d,y,\eta,E)\) and \(a_0=0\). Its first two spatial derivatives are uniformly bounded and its gradient stays in the larger root region after reducing the collar. The construction applies again. Finite covers of a compact boundary chart give one common collar and frequency radius. This proves (B26), including all parameter derivatives and the normal-root gap; no formal eikonal solution is being assumed.

## 7. The exact critical action and Hessian on the diagonal

Put \(\Theta_\sigma(d,y,\eta,E)=S^r_\sigma(d,y;d,y,\eta,E)\). Since \(\Theta_\sigma(0,y,\eta,E)=0\), its normalized phase extends smoothly through zero:
\[
 \begin{gathered}
 \psi_\sigma(d,y,\eta,E)
       =\int_0^1\partial_d\Theta_\sigma(vd,y,\eta,E)\,dv,\\
 \Theta_\sigma=d\psi_\sigma,\\
 \psi_\sigma(0,y,\eta,E)
       =2\sigma\sqrt{E-\eta^{\mathsf T}G(0,y)\eta}.
 \end{gathered}
 \tag{B29}
\]
The last equality follows by differentiating (B26) when both normal slices are zero. The target-slice derivative contributes \(\lambda_\sigma\). The derivative of the incident initial slice contributes \(-\lambda_{-\sigma}\), because differentiation of \(S^i_{-\sigma}(d,z;d,y,\eta,E)=(z-y)\cdot\eta\) gives \(\partial_d S^i_{-\sigma}=-\partial_a S^i_{-\sigma}\) there. Their sum is \(2\lambda_\sigma\). The first formula in (B29), which is Taylor's integral identity in the single distance variable, also proves every uniform derivative bound after division by \(d\).

At \(\eta=0\), the incident and reflected solutions and their first frequency derivatives are particularly simple:
\[
 \begin{gathered}
 S^i_\sigma(a,z;d,y,0,E)=\sigma(a-d)\sqrt E,\\
 S^r_\sigma(a,z;d,y,0,E)=\sigma(a+d)\sqrt E,\\
 \left.\partial_\eta S^i_\sigma\right|_{\eta=0}=z-y,
 \qquad
 \left.\partial_\eta S^r_\sigma\right|_{\eta=0}=z-y.
 \end{gathered}
 \tag{B30}
\]
Indeed the first two expressions solve (B26), since the root at zero tangential momentum is \(\sigma\sqrt E\), independent of \(a,z\). Uniqueness proves them. Differentiating the eikonal equation once in \(\eta\) gives \(\partial_a S_\eta=\lambda_\zeta S_{z\eta}\). At \(\eta=0\) its right side vanishes, so its prescribed initial value \(z-y\) remains unchanged on each leg. Thus
\[
 \begin{gathered}
 \psi_\sigma(d,y,0,E)=2\sigma\sqrt E,\\
 \partial_\eta\psi_\sigma(d,y,0,E)=0,\\
 \partial_E\psi_\sigma(d,y,0,E)=\sigma/\sqrt E.
 \end{gathered}
 \tag{B31}
\]
These identities include \(d=0\) by (B29). In particular the critical action is exactly independent of distance, rather than just constant to first order.

The Hessian is also explicit. Define the positive matrix
\(\overline G(d,y)=\int_0^1G(vd,y)\,dv\). Differentiating the eikonal equation twice and using \(S_{z\eta}=I\) from (B30) gives
\(\partial_a S_{\eta\eta}=\lambda_{\zeta\zeta}(a,z,0,E)=-\sigma G(a,z)/\sqrt E\) on the \(\sigma\) leg. The incident \(-\sigma\) leg starts with zero Hessian on \(a=d\); its backward integral from \(d\) to zero is \(-\sigma E^{-1/2}\int_0^dG(v,z)\,dv\). The reflected \(\sigma\) leg adds the same integral on its forward journey to \(a=d\). Consequently
\[
 \begin{gathered}
 \partial_\eta^2\psi_\sigma(d,y,0,E)
       =-\frac{2\sigma}{\sqrt E}\,\overline G(d,y),\\
 \overline G(0,y)=G(0,y),\qquad
 \overline G(d,y)\geq c_G I.
 \end{gathered}
 \tag{B32}
\]
This calculation differentiates at fixed target coordinate \(z\) before setting \(z=y\); it does not identify a moving coordinate with that fixed derivative.

Smoothness of \(\psi_\sigma\), compactness of the parameter range and (B32) give, on one sufficiently small frequency ball,
\[
 \begin{gathered}
 -\sigma\partial_\eta^2\psi_\sigma\geq cI,\\
 |\partial_\eta\psi_\sigma(d,y,\eta,E)|\geq c|\eta|.
 \end{gathered}
 \tag{B33}
\]
For the second inequality, integrate the Hessian on the segment from zero to \(\eta\), pair with \(-\sigma\eta\), and use (B31) and Cauchy–Schwarz. Hence zero is the unique critical point in that ball, the Hessian has signature \(-\sigma(n-1)\), and the phase is uniformly nonstationary outside any smaller ball. Since \(|\sigma/\sqrt E|\geq1\) on the chosen energy interval, all hypotheses (B18) of the fixed-action freezing lemma are now verified for these actual metric phases. This assertion concerns these near-normal phases, not a representation of every part of the spectral kernel.

<a id="reflected-dirichlet-transport"></a>
## 8. Transport with the actual lower-order terms

Represent a half density by its scalar coefficient relative to \(|da\,dz|^{1/2}\). In this representation the actual differential expression has the form
\[
 \begin{gathered}
 P=\sum_{j,k=1}^n g^{jk}(a,z)D_jD_k\\
 +\sum_{j=1}^n b_j(a,z)D_j+c(a,z),\\
 D_j=-i\partial_j,\qquad
 (g^{jk})=\begin{pmatrix}1&0\\0&G\end{pmatrix}.
 \end{gathered}
 \tag{B34}
\]
The smooth coefficients \(b_j,c\) include all ordering and lower-order terms; they need not be real in left quantization. Nothing in the following construction discards them or assumes a Laplace operator.

For any one of the phases in (B26), direct differentiation of the degree-two differential expression gives the exact identity
\[
 \begin{gathered}
 e^{-iS/h}(h^2P-E)(e^{iS/h}A)\\
 =h\mathcal T_S A+h^2PA.
 \end{gathered}
 \tag{B35}
\]
where
\[
 \begin{aligned}
 \mathcal T_S A={}&\frac2i\sum_{j,k}g^{jk}S_j\partial_kA\\
 &+\frac1i\sum_{j,k}g^{jk}S_{jk}A\\
 &+\left(\sum_j b_jS_j\right)A.
 \end{aligned}
 \tag{B36}
\]
The eikonal equation cancels \((p(dS)-E)A\). The coefficient of \(\partial_a A\) in \(\mathcal T_S\) is \(2S_a/i\), uniformly separated from zero. After division by that coefficient, the transport equation is an ordinary scalar equation along the base characteristics with velocity \(G S_z/S_a=-\partial_\zeta\lambda_\sigma(a,z,S_z,E)\). These are precisely the projected characteristics used above.

For every integer \(L\geq0\), choose smooth bounded initial coefficient functions \(g_{\sigma,j}(z;d,y,\eta,E)\), \(0\leq j\leq L\), supported in the retained frequency and energy region. Prescribe incident coefficients on \(a=d\), and reflected coefficients on \(a=0\), by
\[
 \begin{gathered}
 \mathcal T_S a_0=0,\\
 \mathcal T_S a_j=-P a_{j-1}\quad(1\leq j\leq L),\\
 a^i_{\sigma,j}(d,z;d,y,\eta,E)\\
 =g_{\sigma,j}(z;d,y,\eta,E),\\
 a^r_{\sigma,j}(0,z;d,y,\eta,E)\\
 =-a^i_{-\sigma,j}(0,z;d,y,\eta,E).
 \end{gathered}
 \tag{B37}
\]
Solve the incident recursion first and then the reflected one. To justify every step, write its divided equation along a characteristic as \(u'+q u=f\). Multiplication by \(e^{\int q}\) gives
\(u(a)=e^{-\int_{a_0}^a q}[u(a_0)+\int_{a_0}^a e^{\int_{a_0}^v q}f(v)\,dv]\).
Differentiation verifies the equation and initial value, with oriented integrals for a backward incident leg. The intervals are uniformly bounded, their coefficients and all parameter derivatives are bounded, and the flow inverse is uniformly smooth. Differentiating this formula proves all parameter bounds. At each recursion step \(P a_{j-1}\) uses only the already obtained smooth derivatives. This proves existence, uniqueness and uniform bounds for all finite coefficient families, including mixed derivatives in the source distance \(d\) through zero. No expansion or division in that distance is used in the transport equations.

Set \(A^i_{\sigma,L}=\sum_{j=0}^Lh^j a^i_{\sigma,j}\), and define \(A^r_{\sigma,L}\) in the same way. Equations (B35)–(B37) telescope to
\[
 \begin{gathered}
 (h^2P-E)(e^{iS/h}A_L)
       =h^{L+2}e^{iS/h}P a_L,\\
 \left.e^{iS^i_{-\sigma}/h}A^i_{-\sigma,L}
       +e^{iS^r_\sigma/h}A^r_{\sigma,L}\right|_{a=0}=0.
 \end{gathered}
 \tag{B38}
\]
The boundary cancellation is exact for every \(h>0\). In the frozen flat case the phases are
\((z-y)\eta-\sigma(a-d)\sqrt{E-r_0(\eta)}\) and
\((z-y)\eta+\sigma(a+d)\sqrt{E-r_0(\eta)}\); they agree at \(a=0\). This also checks the reflection sign directly.

Frequency and energy supports of the coefficients are retained by the recursion: its differentiations are in \((a,z)\), and the characteristic parameter \((\eta,E)\) is fixed. A fixed energy cutoff vanishing near \(E_0\) can therefore be built into the initial coefficients. Initial base supports can be chosen strictly inside the chart so that their two transported supports stay inside the larger chart. Alternatively every estimate can be restricted to a compact subchart where an auxiliary base cutoff is one. Derivatives of a subsequently imposed base cutoff are separate commutator errors on its transition region; (B38) does not call those errors small.

## 9. Quantitative residuals and the frozen diagonal family

For a fixed choice \(\varepsilon=\pm1\), form the finite wave-phase integral
\[
 \begin{gathered}
 \mathcal V_{\sigma,L}=e^{iS^i_{-\sigma}/h}A^i_{-\sigma,L}
 +e^{iS^r_\sigma/h}A^r_{\sigma,L},\\
 K_{h,L}(t,a,z;d,y)\\
 =(2\pi h)^{-n}\sum_{\sigma=\pm1}\int_{E_0}^1\int
  e^{it\varepsilon\sqrt E/h}\mathcal V_{\sigma,L}\,d\eta\,dE.
 \end{gathered}
 \tag{B39}
\]
The amplitudes have uniformly compact \(\eta\)-support. They may be nonzero at the upper energy endpoint. This causes no problem when applying a differential operator or taking a fixed ordinary parameter derivative under the finite integral. With \(Q_h=(hD_t)^2-h^2P\), (B38) gives, on the retained compact charts and any fixed bounded time interval,
\[
 \begin{gathered}
 K_{h,L}|_{a=0}=0,\\
 |\partial^\alpha Q_h K_{h,L}|
       \leq C_{L,\alpha}h^{L+2-n-|\alpha|}.
 \end{gathered}
 \tag{B40}
\]
Here \(\partial^\alpha\) may differentiate time, target coordinates or source coordinates. Each derivative of an exponential costs at most one power of \(h^{-1}\); all phase derivatives and amplitude derivatives are uniformly bounded. The un-differentiated residual is exactly the integral of \(-h^{L+2}e^{i(t\varepsilon\sqrt E+S)/h}Pa_L\). Its absolute integral, and the same calculation after differentiating, prove (B40). Thus any prescribed finite number of derivatives and any prescribed residual power can be attained by increasing \(L\). The construction has not yet imposed the physical Cauchy data that identify this family with the actual cosine kernel.

For density normalization write
\[
 \begin{gathered}
 dV_g=\gamma(a,z)\,da\,dz,\\
 \gamma(a,z)=(\det G(a,z))^{-1/2}.
 \end{gathered}
 \tag{B41}
\]
A coordinate half-density kernel has scalar diagonal relative to \(dV_g\) equal to its coordinate diagonal divided by \(\gamma\). Indeed \(v|da\,dz|^{1/2}=u(dV_g)^{1/2}\) means \(u=\gamma^{-1/2}v\); apply this to both kernel factors. The smooth positive factors \(\gamma^{\pm1}\) and all their derivatives are bounded on the retained collar.

Consider the reflected diagonal family
\[
 \begin{gathered}
 a^{\rm diag}_{\sigma,L}(d,y,\eta,E)\\
 =\gamma(d,y)^{-1}A^r_{\sigma,L}(d,y;d,y,\eta,E),\\
 F_{h,L}(d,y)\\
 =(2\pi h)^{-n}\sum_\sigma\int_{E_0}^1\int
  e^{id\psi_\sigma/h}a^{\rm diag}_{\sigma,L}\,d\eta\,dE.
 \end{gathered}
 \tag{B42}
\]
Let \(F_h^0(d,y)\) be the same expression keeping only \(j=0\), and replacing the smooth distance parameters in \(\psi,\gamma,a^r_0\) by zero, while retaining \(d/h\) in the exponential. Then
\[
 \begin{gathered}
 |F_{h,L}(d,y)-F_h^0(d,y)|\\
 \leq C_Lh^{1-n},\qquad 0\leq d\leq d_0.
 \end{gathered}
 \tag{B43}
\]
To prove this, apply Lemma 5.1 to each actual metric phase \(\psi_\sigma\). Its hypotheses were verified in (B29)–(B33), and (B37) supplies all required distance and energy derivatives of the amplitude, including the factor \(\gamma^{-1}\). The lower energy cutoff makes that amplitude vanish near \(E_0\). This gives the claimed bound for the leading term. Every higher term is bounded directly by \(C_jh^{j-n}\), using its compact integration region, so their finite sum is \(O(h^{1-n})\). At \(d=0\) the leading difference vanishes and the same estimate for the higher terms applies. This proves a uniform coefficient-freezing bound for the constructed family, including arbitrary smooth lower-order coefficients.

Its frozen normalization can be fixed explicitly. Suppose the leading incident seeds on the zero source slice satisfy, at \(z=y\),
\[
 g_{\sigma,0}(y;0,y,\eta,E)
       =\frac{\chi(E)\beta(y,\eta,E)}
                    {2\sqrt{E-r(0,y,\eta)}}.
 \tag{B44}
\]
Here \(\chi\) vanishes near \(E_0\), and \(\beta\) is supported in the small near-normal frequency ball. Smooth such seed families exist because the denominator is separated from zero; multiply by an initial base cutoff equal to one near \(z=y\) and extend in \(d\) using the same positive root. By (B37), the reflected leading coefficient at zero is the negative of (B44). Thus
\[
 \begin{gathered}
 \lambda_0(y,\eta,E)=\sqrt{E-r(0,y,\eta)},\\
 F_h^0(d,y)=-\frac{(2\pi h)^{-n}}{\gamma(0,y)}
 \sum_{\sigma=\pm1}\int_{E_0}^1\int\\
 \quad e^{2i\sigma d\lambda_0/h}
 \frac{\chi(E)\beta(y,\eta,E)}{2\lambda_0}\,d\eta\,dE.
 \end{gathered}
 \tag{B45}
\]
This is precisely the corresponding part of the frozen reflected phase-volume integral. For each fixed \(\eta\), use the two branches \(s=\sigma\sqrt{E-r(0,y,\eta)}\); the positive Jacobian is \(|ds/dE|=1/(2\sqrt{E-r})\). This proves (B45)'s normalization and its negative Dirichlet sign without assigning the spectral interpretation to an arbitrary initial seed.

For the complete frozen phase-volume model, with its full ball instead of these cutoffs, the same image calculation in the reflection lesson gives
\[
 \begin{gathered}
 -\frac{(2\pi h)^{-n}}{\gamma(0,y)}
   \int_{s^2+\eta^{\mathsf T}G(0,y)\eta\leq1}
             e^{2ids/h}\,d\eta\,ds\\
 =-h^{-n}W_n(2d/h).
 \end{gathered}
 \tag{B46}
\]
The change \(\theta=G(0,y)^{1/2}\eta\) has Jacobian \(d\eta=\gamma(0,y)d\theta\); it cancels the density factor. Symmetry in \(s\) turns the exponential into the cosine defining \(W_n\). Removing the near-normal cutoff in the actual variable-coefficient problem is a separate estimate, not a consequence of this frozen identity.

<a id="normal-green-family"></a>
## 10. An exact normal jump and boundary coupling

The preceding scalar transports also have an operator counterpart which fixes the normal source jump. We record it because an arbitrary choice of incident coefficients in (B37) is not yet a fundamental solution.

After the actual normal gauge already proved in [Dirichlet commutators and a local diffraction estimate](dirichlet-commutator-and-diffraction.md#dirichlet-commutator), localize to the same separated-root region, retain the energy \(E\in[E_0,1]\) as a parameter, and extend its tangential symbol as in Sections 41–42 of [Incoming phase neighborhoods for Dirichlet waves](diffractive-phase-neighborhoods.md#separated-normal-roots-and-reflection). The resulting bounded tangential family has normal expression
\(L_h(E)=(hD_a)^2+R_h(a,E)\). It agrees with the gauged differential expression on the retained phase region, not globally. For any finite accuracy \(N\), the proved Riccati construction gives roots and their exact difference inverse:
\[
 \begin{gathered}
 \mathcal R_\sigma=B_\sigma^2-ih\partial_aB_\sigma+R_h,\\
 \|\mathcal R_\sigma\|\leq C_Nh^N,\\
 \|B_\sigma-B_\sigma^*\|\leq Ch,\\
 A_h=(B_+-B_-)^{-1},\quad\|A_h\|\leq C.
 \end{gathered}
 \tag{B47}
\]
Norms are on tangential \(L^2\). These statements hold after any fixed number of parameter derivatives, with the appropriate finite accuracy. Energy derivatives are ordinary compact-parameter derivatives in the same symbol recursion. The principal roots are \(\pm\sqrt{E-r}\); all actual lower terms are included in the finite roots.

For fixed \(h>0\), the bounded-operator integral equation constructs the evolution \(U_\sigma(a,b)\) satisfying
\[
 \begin{gathered}
 (hD_a-B_\sigma(a))U_\sigma(a,b)=0,\\
 U_\sigma(b,b)=I,\\
 \|U_\sigma(a,b)\|\leq e^{C|a-b|}.
 \end{gathered}
 \tag{B48}
\]
For existence, successive substitution in the integral equation has its \(j\)-th norm bounded by \((C_h|a-b|)^j/j!\); the series and its differentiated integral converge uniformly for each fixed \(h\). The same series proves uniqueness. The bound independent of \(h\) is stronger than this existence estimate: apply the squared-norm identity and \(\|B_\sigma-B_\sigma^*\|\leq Ch\), exactly as in (T110), to each evolved vector, in either direction. Smooth parameter dependence follows by differentiating the integral equation; each fixed derivative has at worst a fixed power of \(h^{-1}\), because its inhomogeneous terms are bounded by the differentiated coefficient norms and the energy estimate. The group identity follows from uniqueness. In particular \(\partial_bU_\sigma(a,b)=-U_\sigma(a,b)(i/h)B_\sigma(b)\), by differentiating that identity.

For an interior source distance \(0<d<d_0\), put \(M_h(d)=(ih)^{-1}A_h(d)\) and define
\[
 \begin{gathered}
 G_h^i(a,d)=
 \begin{cases}
 U_-(a,d)M_h(d),&a\geq d,\\
 U_+(a,d)M_h(d),&a\leq d,
 \end{cases}\\
 G_h^r(a,d)=-U_-(a,0)U_+(0,d)M_h(d),\\
 G_h^D=G_h^i+G_h^r.
 \end{gathered}
 \tag{B49}
\]
This is an operator-valued distribution in the normal variable. The two incident values agree at \(a=d\), and their ordinary derivative jump is
\[
 \begin{gathered}
 [G_h^i]_{a=d}=0,\\
 [\partial_aG_h^i]_{a=d}
       =\frac ih(B_--B_+)M_h=-h^{-2}I.
 \end{gathered}
 \tag{B50}
\]
For a continuous piecewise smooth function the second distributional derivative is its piecewise second derivative plus this first-derivative jump times \(\delta(a-d)\). This identity follows by integration by parts on the two intervals against a scalar test function, and also holds after pairing an operator with any two Hilbert-space vectors. Since \((hD_a)^2=-h^2\partial_a^2\), the singular term in \(L_hG_h^D\) is exactly \(\delta(a-d)I\); there is no derivative of a delta.

On each ordinary leg, \(L_hU_\sigma=\mathcal R_\sigma U_\sigma\), by differentiating (B48) once more in the correct operator order. The reflected term has the same identity with \(\mathcal R_-\) at its target end. Equations (B47)–(B49) therefore give
\[
 \begin{gathered}
 L_hG_h^D=\delta(a-d)I+\mathcal E_h(a,d),\\
 G_h^D(0,d)=0,\qquad
 \|\mathcal E_h(a,d)\|\leq C_Nh^{N-1},\\
 \|G_h^i(a,d)\|+\|G_h^r(a,d)\|\leq Ch^{-1}.
 \end{gathered}
 \tag{B51}
\]
The error bound is for the ordinary piecewise remainder; the singular term has already been identified exactly. The boundary value cancels because \(U_-(0,0)=I\). All constants are uniform as the interior source approaches the wall. On each open side of \(a=d\), fixed parameter derivatives of the remainder lose only finitely many powers of \(h\); increasing the Riccati accuracy beforehand gives any prescribed differentiated error bound there. Across the source slice, derivatives in \(a,d\) are distributional and may also differentiate its step functions. Their delta coefficients are differences of the same arbitrarily small differentiated remainder values; no pointwise bound for a delta is asserted. No global resolvent bound at an eigenvalue has been assumed.

The normal source jump and Dirichlet cancellation in (B51) hold for the extended separated-root operator. Sections 22–27 compare its localized wave with the physical wave, including the extension and position-cutoff errors.

<a id="compact-frequency-phase-action"></a>
## 11. Phase action when the tangential frequency can be zero

Put \(m=n-1\). The normal roots in (B47) are bounded tangential operators of the form \(B_h=\operatorname{Op}_h(b_h)\), where \(b_h=b_0+h c_h\), \(b_0\) is real, and each symbol is a constant plus a smooth symbol supported in a fixed compact part of \((z,\zeta)\). All needed derivatives are bounded, uniformly in the compact energy and normal parameters. Derivatives in \(h\) will not be required. The actual leading symbol on the retained region is \(b_0=\lambda_\sigma\).

We need phase action at \(\eta=0\), where the tangential phase gradient can vanish. The homogeneous formula in the [scalar phase-action reading](scalar-transport-and-phase-action.md#finite-phase-action) assumes a nonzero normalized phase gradient. Here a compact-frequency proof removes that assumption.

Let \(S(z,\eta)\) be a real smooth phase and let \(a(z,\eta;h)\) have fixed compact support in \((z,\eta)\), with uniform derivatives. All other variables are smooth compact parameters. Extend \(S\) smoothly across the compact region needed below, with bounded derivatives there, and put
\[
 \begin{gathered}
 F(z,w,\eta)=\int_0^1 S_z(z+vw,\eta)\,dv,\\
 S(z+w,\eta)-S(z,\eta)=w\cdot F(z,w,\eta).
 \end{gathered}
 \tag{B52}
\]
For each positive integer \(J\), direct insertion of the left-quantized kernel gives
\[
 \begin{gathered}
 \mathcal B_Sa=e^{-iS/h}B_h(e^{iS/h}a),\\
 \mathcal B_Sa=\sum_{|\alpha|<J}\frac{(h/i)^{|\alpha|}}{\alpha!}
       C_\alpha+h^Jr_J,\\
 C_\alpha=(\partial_w^\alpha\partial_\rho^\alpha G)(0,0),\\
 G(w,\rho)=b_h(z,\rho+F(z,w,\eta))\\
 \qquad\cdot a(z+w,\eta;h).
 \end{gathered}
 \tag{B53}
\]
Every fixed derivative of \(r_J\) in \(z,\eta\) and the compact parameters is bounded. Its \(\eta\)-support stays in the fixed support of the amplitude, and its \(z\)-support stays in a fixed compact set. No lower bound for \(|S_z|\) appears.

To prove this, separate the constant part of \(b_h\); its action is exactly that constant times \(a\), with zero positive-order coefficients. For the compact part the conjugated integral has phase
\(S(z+w,\eta)-S(z,\eta)-w\zeta\). The change \(\rho=\zeta-F(z,w,\eta)\) has Jacobian one and makes this phase exactly \(-w\rho\). Its amplitude is smooth and compact in \((w,\rho)\), uniformly in all retained parameters: \(z\) is in the compact base support of the symbol, \(z+w\) in that of \(a\), and \(\zeta\) in the compact frequency support of the symbol. The quadratic stationary-phase proof (P4)–(P8) in [Phase geometry and stationary phase](phase-geometry-and-stationary-phase.md#quadratic-stationary-phase), applied with parameter \(h^{-1}\), has Hessian \(\left(\begin{smallmatrix}0&-I\\-I&0\end{smallmatrix}\right)\). Its determinant has absolute value one and its signature is zero. Its factor \((2\pi h)^m\) cancels the quantization prefactor; its differential operator is \(-2\partial_w\cdot\partial_\rho\). These facts give precisely (B53), including its differentiated finite remainder. Outside the union of the two compact base supports the action and every term vanish. If the amplitude vanishes for a parameter frequency \(\eta\), the action does too. This proves the support and parameter assertions for the actual remainder, not just its formal coefficients.

In particular the first two terms, with \(b_h=b_0+h c_h\), are
\[
 \begin{aligned}
 \mathcal B_Sa={}&b_0a+h c_ha\\
 &+\frac hi\sum_j(b_0)_{\zeta_j}\partial_ja\\
 &+\frac h{2i}\sum_{j,k}(b_0)_{\zeta_j\zeta_k}S_{jk}a\\
 &+O(h^2).
 \end{aligned}
 \tag{B54}
\]
All symbol factors and their frequency derivatives in (B54) are evaluated at \((z,S_z)\). The remainder has the same smooth parameter meaning as (B53), after the critical exponential has been removed. This formula is valid at the normal ray itself.

<a id="normal-evolution-kernel-bounds"></a>
## 12. Norms that turn an operator error into a kernel error

For an integer \(s\geq0\), use the semiclassical Sobolev norm with Fourier weight \(\langle h\xi\rangle^s\), denoted \(H_h^s(\mathbb R^m)\); negative orders are its dual norms. For positive integers this norm is uniformly equivalent to the sum of \(\|(hD)^\alpha u\|_2\), \(|\alpha|\leq s\), by comparison of the corresponding polynomials in Fourier space. The Fourier normalization and dual pairing are those of the [Fourier reading](finite-derivative-l2.md#fourier-normalization).

The exact normal evolutions and difference inverse from (B47)–(B48) obey
\[
 \begin{gathered}
 \|U_\sigma(a,b)\|_{H_h^{\pm s}\to H_h^{\pm s}}
       \leq C_s,\\
 \|A_h(a)\|_{H_h^{\pm s}\to H_h^{\pm s}}
       \leq C_s.
 \end{gathered}
 \tag{B55}
\]
The first estimate has an energy proof, not an exponential bound of size \(e^{C/h}\). The exact identity
\[
 [hD_j,\operatorname{Op}_h(b_h)]
       =-ih\operatorname{Op}_h(\partial_{z_j}b_h)
 \tag{B56}
\]
follows by differentiating the kernel and integrating the input derivative by parts. The finite-derivative operator bound (N17) bounds each coefficient uniformly. Iterating (B56) expresses \([(hD)^\alpha,B_h]u\) as terms of norm at most \(C_sh\|u\|_{H_h^s}\). Apply the squared-norm argument of (B48) to every \((hD)^\alpha u\), retain these commutators divided by \(h\), sum and integrate. This proves the first bound for smooth inputs. Existence in \(H_h^s\) also follows first from the bounded-operator integral equation there, since (B56) makes \(B_h\) bounded on that space for each fixed \(h\); uniqueness identifies it with the \(L^2\) evolution. Density extends the uniform energy estimate. The adjoint evolution with reversed normal endpoints has the same skew-part and commutator bounds, giving the negative-order statement by duality.

For the inverse, write \(B_+-B_-=2k_0I+K_h\), with \(k_0>0\) constant and \(K_h\) a compact-frequency operator. Differentiating its kernel shows \(K_h:L^2\to H_h^s\) bounded uniformly: every output \(hD\) produces either a bounded frequency factor or \(h\) times a symbol derivative, and (N17) applies. If \(u\in H_h^s\) and \(v=A_hu\), its already established \(L^2\) identity gives \(v=(2k_0)^{-1}(u-K_hv)\). This first proves \(v\in H_h^s\), then bounds that norm using the \(L^2\) inverse bound. The adjoint compact-frequency kernel has the same output-derivative estimate, so the same argument and duality prove the negative-order bound. Parameter differentiation of the inverse identity preserves these bounds. Differentiating the evolution equation or its integral formula costs at most a finite power of \(h^{-1}\) for each fixed number of parameter derivatives, by the same inhomogeneous energy estimate.

There is a direct quantitative kernel consequence. If \(R_h:H_h^{-s}\to H_h^s\), and \(s>m/2+j\), Fourier integration gives the following bounds for \(|\alpha|,|\beta|\leq j\):
\[
 \begin{gathered}
 \|\partial_y^\beta\delta_y\|_{H_h^{-s}}
       \leq C_{s,\beta}h^{-m/2-|\beta|},\\
 |\partial_z^\alpha\partial_y^\beta K_{R_h}(z,y)|\\
 \leq C h^{-m-|\alpha|-|\beta|}
          \|R_h\|_{H_h^{-s}\to H_h^s}.
 \end{gathered}
 \tag{B57}
\]
For the first bound, substitute \(\theta=h\xi\) in the squared Fourier norm of the differentiated delta. The remaining integral of \(|\theta|^{2|\beta|}\langle\theta\rangle^{-2s}\) is finite. The same estimate is the norm of derivative evaluation on \(H_h^s\). Pair that evaluation with \(R_h\partial_y^\beta\delta_y\) to obtain the second bound. Taking \(s\) slightly larger, dominated convergence of these Fourier integrals proves continuous differentiability in \(z,y\); integration against compact smooth inputs identifies this function with the distribution kernel. Thus arbitrary finite weighted Sobolev accuracy implies arbitrary finite ordinary kernel accuracy, with the displayed powers of \(h\) retained.

We will also use a finite local symbol for \(A_hQ_h\), where \(Q_h=\operatorname{Op}_h(q)\) is a smooth compact phase cutoff. For any chosen accuracy and any fixed \(s\),
\[
 \begin{gathered}
 A_hQ_h=\operatorname{Op}_h(q_{A,h})+R_{A,h},\\
 q_{A,h}(z,\eta)=\frac{q(z,\eta)}{2\sqrt{E-r(a,z,\eta)}}\\
 \qquad+h q_{1,h}(z,\eta),\\
 \|R_{A,h}\|_{H_h^{-s}\to H_h^s}=O(h^N).
 \end{gathered}
 \tag{B58}
\]
Here and below an arbitrary prescribed \(N\) is obtained by choosing a sufficiently long finite expansion; the constants may depend on that choice. All symbol derivatives are bounded, and \(q_{A,h}\) has fixed compact support inside the retained phase region after allowing fixed margins. The finite inverse recursion of (T104) starts with \((2\sqrt{E-r})^{-1}\) and cancels the actual left product residual successively. Its symbols are a constant plus compact terms. The exact product formula (N19) and its Taylor remainder (N20) show that the inverse residual is \(h^N\operatorname{Op}_h(r_N)\), with all derivatives bounded and compact frequency support: expand products into their constant and compact parts and apply (N19) to each compact right factor. Constant right factors leave the compact left symbol itself. Such remainders map \(H_h^{-s}\) to \(H_h^s\) uniformly after removal of \(h^N\). Indeed right multiplication by the Fourier weight is exact multiplication of the left symbol by \(\langle\eta\rangle^s\); output \(hD\) derivatives again give bounded compact-frequency symbols. Multiplication by the exact inverse, using (B55), proves the claimed error for the finite inverse. A further application of (N19)–(N20) to its product with \(Q_h\) proves (B58). Parameter derivatives are included by increasing the finite accuracy. This argument does not give actual operator remainders the supports of formal coefficients.

<a id="exact-normal-evolution-phase-kernel"></a>
## 13. A phase kernel for the exact normal evolution

Choose a compact initial phase patch whose two normal flows stay in the region of (B25) for all retained normal endpoints. Let \(q_h\) be a symbol supported in this patch with uniformly bounded derivatives. It may depend on \(h\) and on the compact parameters. Write \(\Phi_\sigma(a,z;b,\eta,E)\) for the phase constructed in Section 6 with initial value \(z\cdot\eta\) at \(a=b\). Thus \(S^i_\sigma(a,z;b,y,\eta,E)=\Phi_\sigma-y\cdot\eta\), and \(\Phi_{z\eta}=I+O(|a-b|)\) is uniformly invertible on a sufficiently short fixed collar.

For every requested finite kernel accuracy, construct
\[
 \begin{gathered}
 V_\sigma(a,b)f(z)\\
 =(2\pi h)^{-m}\iint e^{i(\Phi_\sigma-y\eta)/h}
       v_\sigma f(y)\,d\eta\,dy,\\
 V_\sigma(b,b)=\operatorname{Op}_h(q_h).
 \end{gathered}
 \tag{B59}
\]
In (B59), the suppressed arguments are \(\Phi_\sigma=\Phi_\sigma(a,z;b,\eta,E)\) and \(v_\sigma=v_\sigma(a,z;b,\eta,E,h)\). The amplitude is smooth, has fixed compact support in its phase patch, and has uniform derivatives in all displayed variables except that no \(h\)-derivatives are asserted. It is a finite sum of powers of \(h\) with bounded smooth coefficients, allowed to depend uniformly on \(h\).

For clarity the first transport equation follows from (B54), with \(B_\sigma=\operatorname{Op}_h(\lambda_\sigma+h c_{\sigma,h})\). Its order-\(h\) operator is
\[
 \begin{aligned}
 \mathscr T_{\sigma,h}v={}&\frac1i
    (\partial_a-\lambda_{\sigma,\zeta}\cdot\partial_z)v\\
 &-c_{\sigma,h}(a,z,\Phi_z,E)v\\
 &-\frac1{2i}\sum_{j,k}
    \lambda_{\sigma,\zeta_j\zeta_k}(a,z,\Phi_z,E)
                         \Phi_{z_jz_k}v.
 \end{aligned}
 \tag{B60}
\]
All coefficients here are evaluated on the phase, and the leading order vanishes by \(\Phi_a=\lambda_\sigma(a,z,\Phi_z,E)\). Set the leading amplitude's initial value equal to \(q_h\), and solve \(\mathscr T_{\sigma,h}v_0=0\). At each subsequent order, solve the same inhomogeneous scalar transport equation with the negative of the actual remaining coefficient from (B53), and with zero initial value. The integrating-factor proof in Section 8 applies because its base vector field is the same smooth characteristic flow. It gives every uniform parameter derivative. All coefficients remain supported in the transported initial support: finite differential operators do not enlarge support, and their inhomogeneous transport has zero initial value. The phase can be smoothly extended beyond a slightly larger patch; the amplitudes vanish wherever that extension need not satisfy the eikonal equation. The actual off-support action errors are covered by the remainder in (B53).

Here are operator, not just formal, error bounds for this construction. After cancellation through order \(h^J\), its first-order residual kernel has the form \(h^{J+1}(2\pi h)^{-m}\int e^{i(\Phi-y\eta)/h}r_J\,d\eta\), with all relevant amplitude derivatives bounded and compact \((z,\eta)\)-support. For bounded \(y\), its absolute value is at most \(C h^{J+1-m}\). For large \(|y|\), the phase derivative \(\Phi_\eta-y\) is bounded below by a constant times \(1+|y|\). Repeated integration by parts in \(\eta\) gives any desired integrable decay in \(y\), with additional factors of \(h\). The same bounds hold after any fixed output and input semiclassical derivatives \(hD_z,hD_y\), since they produce bounded phase derivatives and bounded amplitude derivatives. Schur's integral inequality therefore gives, for every fixed even integer \(s\geq0\),
\[
 \|(hD_a-B_\sigma)V_\sigma\|_{H_h^{-s}\to H_h^s}
       \leq C_{J,s}h^{J+1-m}.
 \tag{B61}
\]
One can verify this norm assertion directly by writing a negative-order input as \((1-h^2\Delta_y)^{s/2}f\) with \(f\in L^2\), integrating those finitely many derivatives onto the kernel, and then applying output derivatives and Schur. The even integer restriction is sufficient for every desired kernel derivative in (B57). Schur's inequality itself is the two weighted Cauchy–Schwarz integrations in the [finite-derivative operator proof](finite-derivative-l2.md); it requires both integrable kernel bounds, supplied here by compact \(z\)-support and the preceding \(y\)-decay.

The initial identity in (B59) is exact, because every positive-order transport correction starts at zero. Variation of constants for the actual evolution, using (B55), now gives
\[
 \begin{gathered}
 \mathcal E_\sigma(a,b)
       =U_\sigma(a,b)\operatorname{Op}_h(q_h)-V_\sigma(a,b),\\
 \mathcal F_\sigma(v,b)
       =(hD_v-B_\sigma(v))V_\sigma(v,b),\\
 \mathcal E_\sigma(a,b)
       =-\frac ih\int_b^a U_\sigma(a,v)\mathcal F_\sigma(v,b)\,dv,\\
 \|\mathcal E_\sigma(a,b)\|_{H_h^{-s}\to H_h^s}
       \leq C h^{J-m}.
 \end{gathered}
 \tag{B62}
\]
The sign follows by differentiating the right side; the oriented integral handles either ordering of the endpoints. In particular the forcing loses one power of \(h\), which has been retained. Differentiate this actual integral identity to obtain normal-endpoint and energy derivatives. The differentiated evolution contributes only fixed powers of \(h^{-1}\), as proved after (B55); differentiated residual phases contribute one such power per ordinary parameter derivative. Endpoint terms are the same residuals or their derivatives at an endpoint. There are finitely many terms for any prescribed derivative order, so increasing \(J\) gives arbitrary accuracy for them as well.

Finally apply (B57), with an even \(s\) larger than all desired derivative orders. We have proved that, for any fixed finite collection of derivatives and any prescribed \(N\),
\
 \begin{gathered}
 [U_\sigma(a,b)\operatorname{Op}_h(q_h)\\
       =V_\sigma(a,b)+R_h,\\
 |\partial^\alpha R_h|\leq C_{N,\alpha}h^N.
 \end{gathered}
 \tag{B63}
\]
The estimates include both normal endpoints through zero and through equality, and the compact energy parameter. This identifies a finite phase kernel for the exact normal operator; it is stronger than a wavefront assertion. Zero tangential frequency has not been removed.

<a id="exact-reflected-normal-kernel"></a>
## 14. The reflected normal operator and its source coefficient

Let \(Q_h(d,E)=\operatorname{Op}_h(q(d,z,\eta,E))\), with smooth bounded compact support as above, and define the two normalized reflected operators
\[
 \begin{gathered}
 H_{\sigma,h}(a,d;E)\\
       =-U_\sigma(a,0;E)U_{-\sigma}(0,d;E)\\
 \qquad\cdot A_h(d,E)Q_h(d,E).
 \end{gathered}
 \tag{B64}
\]
For \(\sigma=-1\), this is exactly \(ihG_h^rQ_h\) from (B49). The other orientation has the same source-jump construction after interchanging the roots and reversing the sign of its initial jump factor. More explicitly its incident factor is \(-\sigma(ih)^{-1}A_h\), so its reflected part satisfies \((-\sigma ih)G^r_{\sigma,h}Q_h=H_{\sigma,h}\). Substitution in (B50) proves that both unnormalized Green families have the source \(\delta(a-d)I\); after the right cutoff this source is \(\delta(a-d)Q_h\).

For every finite requested kernel accuracy, these exact operators have the representation
\[
 \begin{gathered}
 H_{\sigma,h}(a,d;E)(z,y)\\
 =(2\pi h)^{-m}\int e^{iS^r_\sigma/h}
       c_\sigma\,d\eta+R_{\sigma,h},\\
 |\partial^\alpha R_{\sigma,h}|\leq C_{N,\alpha}h^N.
 \end{gathered}
 \tag{B65}
\]
In (B65), \(S^r_\sigma=S^r_\sigma(a,z;d,y,\eta,E)\) and \(c_\sigma=c_\sigma(a,z;d,\eta,E,h)\). All derivatives of the compactly supported amplitude \(c_\sigma\) in its ordinary parameters are uniformly bounded. At the common zero normal slice it obeys
\[
 \begin{gathered}
 c_\sigma(0,z;0,\eta,E,h)\\
       =-\frac{q(0,z,\eta,E)}{2\sqrt{E-r(0,z,\eta)}}
         +h r_{\sigma,h}(z,\eta,E).
 \end{gathered}
 \tag{B66}
\]
where \(r_{\sigma,h}\) and all required derivatives are bounded. Thus the leading frozen coefficient is fixed by the exact inverse difference and source jump, rather than chosen as independent data.

To prove these assertions without assuming a composition theorem at zero distance, first use (B58) for \(A_hQ_h\). Apply the single-leg construction of Section 13 to \(U_{-\sigma}(a,d)\operatorname{Op}_h(q_{A,h})\) and restrict its target normal variable to zero. The phase is \(S^i_{-\sigma}(0,z;d,y,\eta,E)\); its amplitude has all the uniform source-distance and energy derivatives just proved. Start a new phase transport on the \(\sigma\) leg at \(a=0\), with the negative of this incident amplitude as initial value. Its phase is exactly \(S^r_\sigma\) by (B26). The same compact phase-action expansion and scalar recursion work for this initial phase: its mixed derivative in \((z,\eta)\) is still \(I+O(d)\), and its phase and amplitude derivatives are uniformly bounded. Its initial kernel is the negative of the incident approximate kernel exactly, not merely to leading order.

Apply the inhomogeneous estimate (B62) to this second leg. The errors in the initial incident kernel and in (B58) are propagated by the bounded operators (B55); the new forcing has the bounds (B61). Parameter derivatives lose only fixed powers as before. Equation (B57) turns the resulting weighted Sobolev error into (B65). This proof does not multiply two oscillatory integrals and assume their remainders retain compact supports. At \(a=d=0\), both phase transports have length zero, all their correction integrals vanish, and the chosen amplitude is exactly \(-q_{A,h}\). Its expansion (B58) proves (B66).

## 15. Uniform freezing for the exact normal family

Let \(\chi(E)\) be smooth on the energy interval and zero near \(E_0\). Define a quantity from the exact normal operators, with diagonal density relative to \(dV_g\), by
\[
 \begin{gathered}
 \mathcal N_h^r(d,y)\\
       =\frac{1}{2\pi h\,\gamma(d,y)}
         \sum_{\sigma=\pm1}\int_{E_0}^1\chi(E)\\
 \qquad\cdot H_{\sigma,h}(d,d;E)(y,y)\,dE.
 \end{gathered}
 \tag{B67}
\]
The symbol \(\mathcal N_h^r\) denotes this normal-operator quantity, not the spectral counting function or the actual spectral projector. Equations (B65)–(B66) and the now verified metric-phase hypotheses imply
\[
 \begin{gathered}
 \mathcal N_h^r(d,y)-\mathcal N_{h,0}^r(d,y)=O(h^{1-n}),\\
 \mathcal N_{h,0}^r(d,y)
 =-\frac{(2\pi h)^{-n}}{\gamma(0,y)}\\
 \quad\cdot\sum_\sigma\int_{E_0}^1\int
       e^{2i\sigma d\lambda_0/h}\\
 \qquad\cdot\frac{\chi(E)q(0,y,\eta,E)}{2\lambda_0}
                        \,d\eta\,dE,\\
 \lambda_0=\sqrt{E-r(0,y,\eta)}.
 \end{gathered}
 \tag{B68}
\]
The error is uniform for \(0\leq d\leq d_0\) and all retained \(y\). Indeed, insert (B65) with arbitrary kernel accuracy, so its energy integral contributes \(O(h^{N-1})\). The remaining prefactors multiply to \((2\pi h)^{-n}\), because \(m=n-1\). On the diagonal the phase is \(d\psi_\sigma\). The amplitude \(\chi(E)\gamma(d,y)^{-1}c_\sigma(d,y;d,\eta,E,h)\) has uniform distance and energy derivatives and vanishes near \(E_0\). Apply Lemma 5.1 with \(h\) as an additional uniformly bounded-amplitude parameter. Equations (B29)–(B33) verify all phase hypotheses. This replaces its smooth distance arguments by zero with error \(O(h^{1-n})\). At zero, (B66) fixes the leading coefficient in (B68); the remaining amplitude has an explicit factor \(h\), so its absolute integral is also \(O(h^{1-n})\). Choose the initial kernel accuracy large enough to absorb its tail. This proves (B68) for the exact normal evolution and inverse operators, including the wall limit.

The multiplicative normal gauge used in (B47) does not alter this diagonal normalization on the retained region. If \(\widetilde P=\kappa P\kappa^{-1}\), restoring a kernel multiplies its coordinate coefficient by \(\kappa(a,z)^{-1}\kappa(d,y)\). On the diagonal this factor is exactly one. Its off-diagonal derivatives are bounded on the compact collar and therefore preserve every finite remainder estimate above. The volume factor \(\gamma^{-1}\) remains exactly the one proved in (B41).

The normalization and error in (B68) concern the exact normal family. Sections 18–27 supply the physical-time normalization and the quantitative comparison with the actual near-normal spectral contribution.

<a id="exact-second-order-normal-evolution"></a>
## 16. An extension compatible with physical time

The small residual in (B51) is sufficient for the reflected estimates already proved. It is not an exact wave equation: normal differentiation across its incident source slice can produce small delta terms. We now remove that residual. We also choose the extension so that its energy dependence is exactly subtraction of \(E\); otherwise a temporal Fourier inversion need not yield a second-order equation in physical time.

All preceding root and transport arguments work on any compact positive energy interval. Choose \(J=[E_*,E^*]\), with \(0<E_*<E_0<1<E^*\), and reduce the retained tangential ball if necessary. Extend the actual tangential cometric smoothly across a larger compact chart. Choose a smooth phase cutoff equal to one on both retained flow tubes, supported where \(r\leq E_*/2\), and between zero and one. Multiplying \(r\) by this cutoff gives a real smooth compact symbol \(r_e\), with \(0\leq r_e\leq E_*/2\). Extend every actual gauged lower-order tangential coefficient with a cutoff equal to one on the same tubes. Its left symbol has the form \(h\rho_1(a,z,\zeta;h)\), with bounded derivatives and compact phase support. Thus we may and do use
\[
 \begin{gathered}
 T_h(a)=\operatorname{Op}_h(r_e+h\rho_1),\\
 R_h(a,E)=T_h(a)-EI,\\
 L_h(E)=(hD_a)^2+T_h(a)-EI.
 \end{gathered}
 \tag{B69}
\]
Here \(T_h\) is independent of \(E\). The leading roots are \(\sigma\sqrt{E-r_e}\), equal to \(\sigma\sqrt E\) outside a compact phase set. Their gap has a uniform positive lower bound. The proofs in Sections 10–15 apply verbatim with the exterior constant \(k_0=\sqrt E\); its energy derivatives are bounded on \(J\). On the retained tubes the expression still includes all actual gauged lower terms. The choice (B69) is a particular admissible extension, not an assertion that it equals the actual differential operator everywhere.

The finite Riccati residual can be estimated more strongly than in (B47). Given a finite accuracy \(L\), it is a finite sum of \(h^L\) times bounded symbols with fixed compact frequency support. This follows from the exact product formula (N19), as in the inverse proof (B58): the constant terms cancel, and every other product has a compact factor; constant right factors leave the compact left factor. Consequently, for every fixed integer \(s\geq0\) and any fixed number of ordinary parameters derivatives,
\[
 \|\partial^\alpha\mathcal R_\sigma\|
       _{H_h^{-s}\to H_h^s}\leq C_{L,s,\alpha}h^L.
 \tag{B70}
\]
Choose the finite recursion long enough for the stated \(L\). The compact-frequency smoothing proof following (B58) proves (B70), including normal and energy derivatives. There is no assertion about differentiation in \(h\).

For a pair \((w,v)\), put \(d_a=hD_a\) and use the invertible change
\[
 \begin{gathered}
 w=V_++V_-,\qquad v=B_+V_++B_-V_-,\\
 V_+=A_h(v-B_-w),\qquad V_-=w-V_+.
 \end{gathered}
 \tag{B71}
\]
The change and its inverse are uniformly bounded on \(H_h^{\pm s}\oplus H_h^{\pm s}\), by (B55), the commutator proof there for the roots, and the same bounds for their parameter derivatives. The exact equation \(L_h(E)w=F\), with \(v=d_aw\), becomes
\[
 \begin{gathered}
 \widetilde F=F-\mathcal R_+V_+-\mathcal R_-V_-,\\
 (d_a-B_+)V_+=A_h\widetilde F,\\
 (d_a-B_-)V_-=-A_h\widetilde F.
 \end{gathered}
 \tag{B72}
\]
This is the direct differentiation used in (T107); it preserves every operator order. In particular its coupling has norm \(O(h^L)\) on each of these spaces. One way to verify existence and the uniform bound is to apply variation of constants with the block diagonal evolution \(\operatorname{diag}(U_+,U_-)\). The successive iterates of the coupling integral have norm at most \(C(C h^{L-1}|a-b|)^j/j!\). The series converges, is unique by the same estimate for a difference, and is bounded uniformly for \(L\geq1\) on the fixed collar. With forcing it gives
\[
 \begin{gathered}
 \|(w,d_aw)(a)\|_{H_h^{\pm s}\oplus H_h^{\pm s}}\\
 \leq C_s\|(w,d_aw)(b)\|_{H_h^{\pm s}\oplus H_h^{\pm s}}\\
 \quad+\frac{C_s}{h}\int_{[a,b]}\|F(v)\|_{H_h^{\pm s}}\,|dv|.
 \end{gathered}
 \tag{B73}
\]
For the forcing term use the uniform boundedness of \(A_h\) and sum the same iterates; either ordering of the endpoints is allowed. This proves stability for the exact second-order equation, without an exponential of order \(e^{C/h}\). Ordinary parameter derivatives of its integral identity lose at most finitely many powers of \(h^{-1}\). To see this explicitly, each normal derivative uses \(d_a(w,v)=(v,-R_hw+F)\); each energy or initial-slice derivative differentiates a bounded coefficient, initial datum or forcing and then uses (B73). Induction gives a finite loss for each fixed number of derivatives.

## 17. Exact normal Green families

Let \(F_\sigma(a,b;E)\) be the first component of the exact second-order solution with data \(w(b)=I\), \(d_aw(b)=B_\sigma(b)\). It satisfies
\[
 \begin{gathered}
 L_h(E)F_\sigma(a,b;E)=0,\\
 F_\sigma(b,b;E)=I,\qquad
 d_aF_\sigma(b,b;E)=B_\sigma(b),\\
 \|F_\sigma-U_\sigma\|_{H_h^{-s}\to H_h^s}
       \leq C_s h^{L-1}.
 \end{gathered}
 \tag{B74}
\]
Indeed their difference has zero value and zero first normal datum at \(a=b\), and forcing \(-\mathcal R_\sigma U_\sigma\). Use (B70), the negative-order bound for \(U_\sigma\), and (B73) with output \(H_h^s\). This also bounds its first semiclassical normal derivative. Differentiating this identity proves every fixed endpoint and energy derivative with a finite further power loss. Thus, by increasing \(L\), all these differences have any prescribed finite ordinary kernel accuracy, by (B57). This is a quantitative comparison with an exact solution, not a formal factorization.

For either \(\sigma=\pm1\), define \(M_\sigma(d)=-\sigma(ih)^{-1}A_h(d)\) and, for an interior source \(0<d<d_0\), set
\[
 \begin{gathered}
 \widehat G^i_\sigma(a,d)=
 \begin{cases}
 F_\sigma(a,d)M_\sigma(d),&a\geq d,\\
 F_{-\sigma}(a,d)M_\sigma(d),&a\leq d,
 \end{cases}\\
 \widehat G^r_\sigma(a,d)
       =-F_\sigma(a,0)F_{-\sigma}(0,d)M_\sigma(d),\\
 \widehat G^D_\sigma=\widehat G^i_\sigma+\widehat G^r_\sigma.
 \end{gathered}
 \tag{B75}
\]
The two incident values agree at the source. Their derivative jump is
\((i/h)(B_\sigma-B_{-\sigma})M_\sigma=-h^{-2}I\), since \(B_\sigma-B_{-\sigma}=\sigma(B_+-B_-)\). Every ordinary leg solves the exact second-order equation. The integration-by-parts jump proof of (B50) now gives the exact identities
\[
 \begin{gathered}
 L_h(E)\widehat G^D_\sigma=\delta(a-d)I,\\
 \widehat G^D_\sigma(0,d)=0,\\
 L_h(E)(\widehat G^D_- -\widehat G^D_+)=0.
 \end{gathered}
 \tag{B76}
\]
No ordinary residual remains. Moreover the difference in the last line is smooth across \(a=d\): its value jump and first-derivative jump both vanish. On the two sides it solves the same smooth bounded-operator Cauchy equation. Uniqueness identifies both sides with the solution from their common Cauchy data at \(a=d\). Those data depend smoothly on \(d,E\), so the difference is smooth jointly in both normal variables and energy. This justifies all higher derivatives without assigning a pointwise bound to a delta. Individual incident families still have their required first-derivative jump. At \(d=0\) only the uniform limiting estimates are asserted, not an interior delta source on the boundary.

For the same retained right cutoff \(Q_h(d,E)\), put
\[
 \begin{gathered}
 \widehat H_{\sigma,h}
       =-F_\sigma(a,0)F_{-\sigma}(0,d)A_h(d)Q_h(d,E),\\
 \widehat H_{\sigma,h}
       =(-\sigma ih)\widehat G^r_\sigma Q_h,\\
 \partial^\alpha(\widehat H_{\sigma,h}-H_{\sigma,h})(z,y)
       =O(h^N).
 \end{gathered}
 \tag{B77}
\]
For any prescribed \(N,\alpha\), choose \(L\) large first. Subtract the two ordered products, replacing one factor at a time. Equation (B74) supplies arbitrary weighted smoothing accuracy for the difference factor; all remaining factors are bounded on both weighted spaces. The inverse and cutoff obey (B55) and (B58). The same argument after differentiation and (B57) proves the last line. It also applies to either ordinary incident leg. Hence (B65)–(B68), including the leading coefficient and uniform frozen estimate, hold for these exact second-order reflected families as well. We have removed the equation residual without altering the finite leading coefficient or the earlier estimate.

<a id="normal-time-source-and-causality"></a>
## 18. Temporal orientation and the exact source prefactor

Take temporal frequencies with \(\tau^2\in J\), separated from zero, and set \(E=\tau^2\). Choose \(\sigma=-\operatorname{sgn}\tau\) for the outgoing incident leg \(a\geq d\) and for the reflected leg; the incident leg \(a\leq d\) has the opposite root. This orientation has a precise travel-time inequality.

Differentiate the action (B27) in \(\tau\) at fixed target position. Its endpoint variations cancel by the same variational identity that proved (B28). Along an incident characteristic this leaves the integral of \(\partial_\tau\lambda_\sigma=\sigma\tau/\sqrt{\tau^2-r}\). On the two reflected legs the intermediate endpoint variations cancel against each other, since their phase gradients match at the wall. Therefore
\[
 \begin{gathered}
 \partial_\tau S^i_\sigma
       =\int_d^a\frac{\sigma\tau}{\sqrt{\tau^2-r(v,Z,\Xi)}}\,dv,\\
 \partial_\tau S^r_\sigma
       =\int_d^0\frac{-\sigma\tau}{\sqrt{\tau^2-r(v,Z_i,\Xi_i)}}\,dv\\
 \qquad+\int_0^a\frac{\sigma\tau}{\sqrt{\tau^2-r(v,Z_r,\Xi_r)}}\,dv,\\
 \partial_\tau S^i_{\mathrm{oriented}}\leq-|a-d|,\\
 \partial_\tau S^r_\sigma\leq-(a+d).
 \end{gathered}
 \tag{B78}
\]
The last line uses \(r\geq0\) along the retained real metric flows, so \(|\tau|/\sqrt{\tau^2-r}\geq1\). On the lower incident leg reverse both the integration direction and the root sign. The initial plane phase is independent of \(\tau\). These arguments also prove all smooth parameter derivatives on each incident side and on the reflected family.

Let \(\theta\in C_c^\infty(\{\tau:\tau^2\in J^\circ\})\). At this point \(\theta\) need not be even. The cutoff \(Q_h(d,\tau^2)\) is the one used above. Define the tangential-operator-valued source and normal kernel by
\[
 \begin{gathered}
 \mathcal Q_h(t;d)
       =(2\pi h)^{-1}\int e^{it\tau/h}\\
 \qquad\cdot\theta(\tau)Q_h(d,\tau^2)\,d\tau,\\
 K_h^D(t;a,d)
       =\frac{h^2}{2\pi h}\int e^{it\tau/h}\theta(\tau)\\
 \qquad\cdot\widehat G^D_\sigma(a,d;\tau^2)
                       Q_h(d,\tau^2)\,d\tau,\\
 \sigma=-\operatorname{sgn}\tau.
 \end{gathered}
 \tag{B79}
\]
These compact-frequency integrals define ordinary smooth time families of the normal operator kernels, with the previously specified source-slice distributional meaning. Put \(\mathscr P_h=(hD_a)^2+T_h(a)\). Since the extension in (B69) is independent of energy except for \(-E\), (B76) gives
\[
 \begin{gathered}
 (\partial_t^2+h^{-2}\mathscr P_h)K_h^D
       =\delta(a-d)\mathcal Q_h(t;d),\\
 K_h^D(t;0,d)=0.
 \end{gathered}
 \tag{B80}
\]
Indeed applying \(\partial_t^2+h^{-2}\mathscr P_h\) under the integral yields \(h^{-2}L_h(\tau^2)\); its \(h^{-2}\) cancels precisely the \(h^2\) in (B79). This proves the physical-time source prefactor. It is an equation for the chosen extended normal expression, not yet the actual global Dirichlet operator.

For every fixed \(\varepsilon>0\), bounded time interval with \(t\leq-\varepsilon\), and every prescribed finite derivative collection, the reflected kernel and each ordinary incident side satisfy
\[
 |\partial^\alpha K_h^r|+
       |\partial^\alpha K_h^i|\leq C_{N,\alpha,\varepsilon}h^N.
 \tag{B81}
\]
To prove it, replace the exact operators by their phase kernels to a sufficiently high finite accuracy using (B63), (B74) and (B77). Their inverse factors carry the explicit \(h^{-1}\), while (B79) carries the other fixed powers; increasing the accuracy absorbs all of them and all chosen derivatives. For a phase term, (B78) gives \(|\partial_\tau(t\tau+S)|\geq\varepsilon\). Integrate repeatedly in \(\tau\) with \((h/i)(t+\partial_\tau S)^{-1}\partial_\tau\). All amplitudes have smooth compact temporal support, so there are no endpoint terms. The coefficient and its derivatives are uniformly bounded on the compact parameters. Each integration supplies \(h\); each preassigned ordinary derivative loses only a fixed power. This proves (B81), uniformly as either normal distance tends to zero. Across \(a=d\), derivatives are distributions; their jump coefficients have the same rapid bounds by the same compact temporal integration. The reflected kernel itself is smooth through that slice. This is rapid decay before negative times separated from zero, not exact causal support for a temporally band-limited function.

<a id="actual-retarded-spectral-family"></a>
## 19. The actual retarded spectral family with a smooth temporal cutoff

We now give the corresponding exact identity for the actual compact Dirichlet operator \(P\). This fixes what the normal construction must match. Let \(Pe_j=\lambda_je_j\), \(\kappa_j=\sqrt{\lambda_j}>0\), and \(\Pi_j f=(f,e_j)e_j\), with the eigenbasis and exact domains proved in [Compact positive inverses and diagonal domains](compact-spectrum-domains.md#compact-inverse-domains), equations (1)–(2), and applied to this realization in [Dirichlet wave regularization](dirichlet-wave-regularization.md#dirichlet-wave-regularization), equations (W1)–(W8). Let \(Q_h(E)\) be any smooth operator family on \(L^2(X)\), supported in the fixed energy interval after multiplication by the cutoff below, with uniform operator bounds for every required energy derivative. The local tangential cutoffs used here have those bounds after fixed coordinate and density cutoffs: apply (N17) on each normal slice and integrate its squared estimate in the normal variable. Smooth density multipliers on the compact chart only change its constant.

Assume now that \(\theta\) is even, and write \(\Theta(E)=\theta(\sqrt E)\). In this section \(\mathcal Q_h(t)\) is the full spatial operator defined by the first integral in (B79), with this \(Q_h(E)\). Define
\[
 \begin{gathered}
 S(u)=\frac{\sin(u\sqrt P)}{\sqrt P},\\
 K_h^P(t)=\int_0^\infty S(u)\mathcal Q_h(t-u)\,du.
 \end{gathered}
 \tag{B82}
\]
These are actual operators, not resolvents evaluated at an eigenvalue. By the eigenbasis, \(\|S(u)\|\leq\lambda_{\min}^{-1/2}\) and \(\|S'(u)\|\leq1\). Integration by parts in the compact \(\tau\) integral gives, for all fixed \(k,A\),
\(\|\partial_t^k\mathcal Q_h(t)\|\leq C_{k,A}h^{-1-k}(1+|t|/h)^{-A}\).
For \(|t|\leq h\) use the absolute integral; for \(|t|>h\) integrate \(A\) times and use the bounded energy derivatives. Thus (B82) and every fixed time derivative converge in operator norm. Moving one derivative from \(\mathcal Q_h\) onto \(S\), with \(S(0)=0\), gives \(K_h^{P\prime}(t)=\int_0^\infty\cos(u\sqrt P)\mathcal Q_h(t-u)\,du\). Interpret this last integral strongly on each input vector; its tails converge in operator norm by the integrable bound. No operator-norm continuity of the cosine group is assumed. The original integral and its derivatives defined with \(S(u)\partial_t^k\mathcal Q_h\) converge in operator norm because \(S\) is norm continuous, by \(\|S(u)-S(v)\|\leq|u-v|\).

For a finite eigenfunction projection, two scalar integrations by parts give \((\partial_t^2+\lambda_j)\Pi_j K_h^P=\Pi_j\mathcal Q_h\). Both \(K_h^{P\prime\prime}\) and \(\mathcal Q_h\) are bounded \(L^2\)-valued operators by the preceding estimates. The exact weighted-sum characterization of \(D(P)\) therefore shows, for every input, \(K_h^P(t)f\in D(P)\) and
\[
 \begin{gathered}
 (\partial_t^2+P)K_h^P=\mathcal Q_h,\\
 K_h^P(t)f|_{\partial X}=0,\\
 \|\partial_t^kK_h^P(t)\|_{2\to2}=O(h^N)
       \quad(t\leq-\varepsilon).
 \end{gathered}
 \tag{B83}
\]
For the last bound, \(u\geq0\) implies \(|t-u|\geq\varepsilon+u\). Integrating the preceding rapid bound for \(\mathcal Q_h\) against the bounded sine operator proves any power by choosing \(A\) large. The estimate is uniform on fixed negative time sets. The boundary condition follows from the proved domain of the original Dirichlet realization. The operator \(P\) was not replaced by the normal extension.

## 20. The factor of two and the spectral band

Evenness in \(\tau\) makes \(\mathcal Q_h\) even in time. Oddness of \(S\) then gives the exact identity
\[
 \begin{gathered}
 K_h^P(t)-K_h^P(-t)
       =\int_{\mathbb R}S(u)\mathcal Q_h(t-u)\,du\\
       =\sum_j\Theta(h^2\lambda_j)
          \frac{\sin(t\kappa_j)}{\kappa_j}
                         \Pi_jQ_h(h^2\lambda_j).
 \end{gathered}
 \tag{B84}
\]
The first equality follows by changing \(u\) to \(-u\) in the negative half of the absolutely convergent integral. For the second, project onto \(e_j\) and write the sine as its two exponentials. Fourier inversion for the smooth compact operator-valued function \(\theta(\tau)Q_h(\tau^2)\), tested against any two \(L^2\) vectors, evaluates it at \(\tau=\pm h\kappa_j\). Evenness makes both values equal. The ordinary Fourier inversion proof already used in the programme applies to these scalar smooth compact functions. Their derivative bounds justify the integrals. Only finitely many eigenvalues lie in the fixed scaled band for each \(h>0\), so the resulting sum is finite. Equality of every eigencomponent proves the operator identity. No commutation of \(Q_h(E)\) with \(P\) has been made: the projection is on the left in the displayed order.

Differentiating the finite sum gives
\[
 \begin{gathered}
 K_h^{P\prime}(t)+K_h^{P\prime}(-t)\\
       =\sum_j\Theta(h^2\lambda_j)\cos(t\kappa_j)
                         \Pi_jQ_h(h^2\lambda_j),\\
 2K_h^{P\prime}(0)
       =\sum_j\Theta(h^2\lambda_j)\Pi_jQ_h(h^2\lambda_j).
 \end{gathered}
 \tag{B85}
\]
In particular a smooth temporal cutoff of the retarded sine family contributes one half of this band operator at the zero-time derivative. Omitting that factor would give the wrong spectral coefficient. With \(Q_h=I\), the right side is precisely the smooth spectral band multiplier; with a varying \(Q_h(E)\), (B85) specifies the exact ordered band operator that must be matched locally.

The normal reflected family has the same prefactor. Define \(\widehat{\mathcal N}_{h,\Theta}^r\) by the right side below, with \(\widehat H\) from (B77). Differentiating the reflected part of (B79), using \(\sigma=-\operatorname{sgn}\tau\), and then changing \(E=\tau^2\) on each half-axis gives
\[
 \begin{gathered}
 \frac{2}{\gamma(d,y)}\partial_tK_h^r(0;d,y;d,y)
       =\widehat{\mathcal N}_{h,\Theta}^r(d,y),\\
 \widehat{\mathcal N}_{h,\Theta}^r(d,y)
       =\frac{1}{2\pi h\,\gamma(d,y)}\\
 \qquad\cdot\sum_\sigma\int_J\Theta(E)
                       \widehat H_{\sigma,h}(d,d;E)(y,y)\,dE.
 \end{gathered}
 \tag{B86}
\]
For the sign and constant, (B77) says \(\widehat G_\sigma^rQ_h=-\sigma(ih)^{-1}\widehat H_{\sigma,h}\). The time derivative in (B79) therefore has coefficient \(-\sigma\tau/(2\pi h)=|\tau|/(2\pi h)\). On each half-axis \(|\tau|\,|d\tau|=dE/2\). The additional factor two on the left of (B86) gives exactly the displayed \(1/(2\pi h)\). The diagonal gauge factors cancel as in Section 15, and division by \(\gamma\) is the same metric-volume conversion. Thus the normal source jump and the actual retarded spectral identity give consistent coefficients.

The smooth temporal cutoff in Sections 18–20 is essential to their rapid negative-time bounds. A sharp upper energy endpoint cannot be substituted into their integration-by-parts proof: it would add endpoint terms. Equation (B86) fixes the local energy-density normalization for smooth tests. The sharp cumulative endpoint in (B67)–(B68) retains its separate energy-endpoint analysis from Lemma 5.1. Neither calculation alone identifies the normal extension with the actual spectral projector.

## 21. Comparing the normal and physical waves

Equations (B76)–(B86) fix the normal Green equation, its phase representation, temporal orientation and source normalization. To identify this family with the physical wave, replace \(\mathscr P_h\) in (B80) by the actual gauged \(h^2P\) and estimate the extension and position-cutoff errors. Sections 22–27 perform this comparison in energy norms and then control the diagonal uniformly at the wall. Sections 28–30 treat the complementary frozen model. The full-frequency argument in Sections 31–38 proves (B16), including the regions not covered by the near-normal cutoff.

<a id="actual-near-normal-wave-comparison"></a>
## 22. Source columns with uniform energy norms at the wall

We now compare the normal construction with the actual wave for a retained near-normal right cutoff. The estimates will hold for every fixed target and time derivative, uniformly in the source point \((d,y)\), including its limit at the wall. No estimate for arbitrary normal derivatives of a point source is assumed. Reduce the retained collar and patches once so that all larger cutoffs fit inside the phase-construction region of Sections 6–20; write \(d_0\) for this smaller retained collar width.

First identify the energy space of the original positive Dirichlet operator. Use its Hermitian form \(q\) and the Gårding bound (10)–(11) in [Smooth Dirichlet regularity](smooth-dirichlet-powers.md), together with the actual eigenbasis \(Pe_j=\lambda_je_j\). For a large fixed \(C\), the inner product \(q+C(\cdot,\cdot)\) is equivalent to \(H_0^1\). Finite eigenfunction sums are dense in this inner product: a vector orthogonal to every \(e_j\) has \((\lambda_j+C)(u,e_j)=0\), by the weak form identity, and is zero by completeness of the \(L^2\) basis. The Hilbert projection argument then makes their closed span the whole energy space. On those sums \(q(u,u)=\sum_j\lambda_j|u_j|^2\). Passage in the form norm and strict positivity \(\lambda_j\geq\lambda_{\min}>0\) show that this is an equivalent complete norm on \(H_0^1\). Write \(\mathcal E_D^1\) for this normed energy space and \(\mathcal E_D^{-1}\) for its anti-dual. This notation leaves the shifted \(\mathcal H_D^s\) norms of (W3) unchanged. With the anti-dual convention of (W4), the exact coefficient norms are
\[
 \begin{gathered}
 \|u\|_{\mathcal E_D^1}^2=\sum_j\lambda_j|u_j|^2
       \asymp\|u\|_{H^1}^2,\quad u\in H_0^1,\\
 \|f\|_{\mathcal E_D^{-1}}^2=\sum_j\lambda_j^{-1}|f_j|^2,\\
 \|P^{-1}f\|_{\mathcal E_D^1}
       =\|f\|_{\mathcal E_D^{-1}}.
 \end{gathered}
 \tag{B87}
\]
For the dual formula, first test on finite eigenfunction sums and use weighted Cauchy–Schwarz. Conversely the finite choices \(u_j=\lambda_j^{-1}f_j\), with the anti-dual convention, recover every finite partial sum of the norm; density just proved extends the functional to all of \(H_0^1\). This proves the identification, rather than presuming a fractional-domain theorem. The cosine multipliers have norm at most one on this dual space.

Write \(q_h(d,z,y,E)\) for the kernel of \(Q_h(d,E)\) in Section 14; its symbol is fixed smooth compact tangential phase data, with uniformly bounded parameter derivatives. In a fixed coordinate strip, the elementary slice trace bound and the kernel estimate give
\[
 \begin{gathered}
 \|v(d,\cdot)\|_{L^2_z}\leq C\|v\|_{H^1},
       \quad 0\leq d\leq d_0,\\
 \|\partial_E^j q_h(d,\cdot,y,E)\|_{L^2_z}
       \leq C_jh^{-m/2},\\
 m=n-1,\\
 \|f_{h,E,d,y}\|_{\mathcal E_D^{-1}}
       \leq C h^{-m/2}.
 \end{gathered}
 \tag{B88}
\]
Here, in coordinate half-density coefficients, the source in the last line is
\(f_{h,E,d,y}(a,z)=\delta(a-d)\kappa(d,y)\kappa(d,z)^{-1}q_h(d,z,y,E)\), extended by zero past the artificial chart edges. The smooth nonvanishing normal gauge \(\kappa\) and its inverse have bounded derivatives on the larger chart. A fixed input cutoff, equal to one on all retained \((d,y)\), defines the corresponding global source operator; it is suppressed in this formula. The last estimate also holds after every fixed energy derivative.

For the first line of (B88), apply the fundamental theorem to \(v(d,z)-v(s,z)\), use Cauchy–Schwarz on the fixed strip, and average \(s\) over that strip. The resulting constant is independent of \(d\). Smooth approximation up to the wall, proved in Section 1 of the smooth Dirichlet reading, extends it to \(H^1\). For the second line, integration by parts in the compact symbol frequency gives \(|\partial_E^j q_h|\leq C_{j,A}h^{-m}(1+|z-y|/h)^{-A}\). Squaring and substituting \(z-y=hw\) proves the bound. Pairing this \(L^2_z\) kernel with the slice trace, and then using (B87), proves the final assertion. Smooth gauge factors change only constants. Thus the estimate is uniform as an interior source approaches the wall. At the wall its functional on \(H_0^1\) is zero; we do not insert an interior delta source at a boundary point.

## 23. Retarded columns in the energy space

Use a fixed even \(\theta\) as in Section 19 and set \(\Theta(E)=\theta(\sqrt E)\). For each retained source define
\[
 \begin{gathered}
 f_h(t)=(2\pi h)^{-1}\int e^{it\tau/h}\\
 \qquad\cdot\theta(\tau)f_{h,\tau^2,d,y}\,d\tau,\\
 \|\partial_t^k f_h(t)\|_{\mathcal E_D^{-1}}\\
       \leq C_{k,A}h^{-m/2-1-k}(1+|t|/h)^{-A}.
 \end{gathered}
 \tag{B89}
\]
Absolute integration for \(|t|\leq h\) and repeated integration by parts for \(|t|>h\), using (B88), prove the estimate. All constants are uniform in the source. These are strong Hilbert-space integrals of smooth compact-parameter families.

The actual retarded column is the sine convolution of (B82), now in this energy dual. It has the more regular representation
\[
 \begin{gathered}
 u_h^P(t)=\int_0^\infty S(v)f_h(t-v)\,dv,\\
 u_h^P(t)=P^{-1}f_h(t)\\
       -P^{-1}\int_0^\infty\cos(v\sqrt P)f_h'(t-v)\,dv,\\
 u_h^P\in C^\infty(\mathbb R;H_0^1),\\
 \|\partial_t^k u_h^P(t)\|_{H^1}=O(h^N),
       \quad t\leq-\varepsilon.
 \end{gathered}
 \tag{B90}
\]
The first integral converges in \(L^2\), since \(S(v):\mathcal E_D^{-1}\to L^2\) is bounded by one in the coefficient norms. The second follows by one scalar integration by parts on each eigencomponent, using \(S(v)=-P^{-1}\partial_v\cos(v\sqrt P)\); its boundary term is \(P^{-1}f_h(t)\). The cosine is strongly continuous and bounded on the energy dual, so the second integral converges there by (B89). Equation (B87) makes the displayed equality an \(H_0^1\) identity. The same argument for every time derivative proves the stated regularity and a fixed polynomial bound in \(h^{-1}\) on bounded time intervals. For \(t\leq-\varepsilon\), use \(|t-v|\geq\varepsilon+v\) in (B89) and choose \(A\) arbitrarily large. This proves its last line for every prescribed \(N,k\).

Eigencomponent testing gives \((\partial_t^2+P)u_h^P=f_h\) in the energy dual and the actual homogeneous Dirichlet condition. The even-source identities (B84)–(B85) remain valid columnwise: their scalar Fourier calculations apply to each eigencomponent, and only finitely many components survive the scaled band. In particular their right side is the actual kernel column of
\(\sum_j\Theta(h^2\lambda_j)\cos(t\kappa_j)\Pi_jQ_h^\kappa(h^2\lambda_j)\), where \(Q_h^\kappa\) denotes the embedded family \(\kappa^{-1}Q_h\kappa\). This preserves the operator order.

## 24. The actual extension error and its odd part

Keep the particular extension (B69). On the larger chart the difference from the actual gauged operator is tangential:
\[
 \begin{gathered}
 \Delta_h(a)=h^2\kappa P\kappa^{-1}\\
                 -\bigl((hD_a)^2+T_h(a)\bigr),\\
 Z_{\sigma,h}(a,d;E)=\Delta_h(a)
       \widehat G^D_\sigma(a,d;E)Q_h(d,E),\\
 \partial^\alpha Z_{\sigma,h}(a,d;E)(z,y)=O(h^N).
 \end{gathered}
 \tag{B91}
\]
The kernel estimate holds for any prescribed finite derivatives on either closed incident side separately and for the reflected part smoothly; \(L\) in the finite root construction is chosen sufficiently large. The source point and all retained parameters have uniform constants. In particular its value is continuous across \(a=d\). Higher normal derivatives across that slice are not asserted to be ordinary functions.

Here is the operator error proof. The left symbol of \(\Delta_h\) is a degree-two polynomial tangential differential symbol minus a compact symbol. It and all its derivatives vanish on a neighborhood of the retained phase tubes. Apply the exact finite differential phase action to the polynomial part and (B53) to the compact part. Their coefficients cancel to every chosen finite order because they are evaluated at the actual phase gradient in that neighborhood. The differential action has no terms past its degree; the compact part has the bounded differentiated remainder of (B53). Thus their action on every incident-side or reflected phase kernel is arbitrarily small with all prescribed ordinary derivatives. The true kernel differs by arbitrarily accurate weighted smoothing remainders, by (B74)–(B77). Allow two extra semiclassical Sobolev derivatives before applying \(\Delta_h\), and use its degree-two differential bound and the bounded-symbol estimate. Equation (B57) converts the resulting weighted norm into the same ordinary kernel bounds. Increasing the accuracy absorbs the Green factor \(h^{-1}\) and every fixed parameter loss. This proves (B91) for the actual operators, including their tangential frequency tails.

The energy independence of \(\Delta_h\) is useful here. Since \(\theta\) is even, the odd time part of \(\Delta_h K_h^D\) involves the orientation difference \(\widehat G^D_- -\widehat G^D_+\). By (B76) that difference is jointly smooth in both normal variables. It follows that
\[
 \begin{gathered}
 \mathcal D_h(t)=\Delta_hK_h^D(t),\\
 \partial^\alpha_{a,z,t}
       \{\mathcal D_h(t)-\mathcal D_h(-t)\}\\
                 =O(h^N).
 \end{gathered}
 \tag{B92}
\]
for the kernel coefficients at \((a,z;d,y)\) on the entire retained normal rectangle, including \(a=d\) and its wall limit. To verify its size, integrate (B91) on each side with the compact temporal profile, retaining the fixed powers of \(h\). The derivatives of the two side formulas match, by the exact Cauchy uniqueness in (B76); their bounds therefore extend across the slice. This proves the asserted ordinary derivative bounds for the odd part without treating small delta coefficients as pointwise-small functions.

## 25. A forced local energy comparison

Choose a smooth position cutoff \(\beta(a,z)\) supported inside the larger chart, equal to one on a neighborhood of all source output supports in (B88) and on the retained target patch. All phase tubes through its support remain inside the root agreement region. Its derivatives are supported outside a fixed smaller neighborhood \(U\) of the target patch. Restore the normal gauge and define
\[
 \begin{gathered}
 u_h^N(t;a,z)=\beta(a,z)\kappa(a,z)^{-1}\\
 \qquad\cdot K_h^D(t;a,z;d,y)\kappa(d,y),\\
 D_h=u_h^P-u_h^N,\\
 (\partial_t^2+P)D_h=F_h^{\rm small}+F_h^{\rm edge},\\
 F_h^{\rm small}=-\beta\kappa^{-1}h^{-2}
                    \Delta_hK_h^D\,\kappa(d,y),\\
 F_h^{\rm edge}=-[P,\beta]\kappa^{-1}
                    K_h^D\,\kappa(d,y).
 \end{gathered}
 \tag{B93}
\]
The source cancels exactly: the normal equation has the source \(\delta(a-d)\mathcal Q_h\), and \(\beta=1\) on its compact output support. Coordinate half-density identifications introduce precisely the displayed gauge factors; fixed smooth trivializations give equivalent norms. The formula has no source truncation remainder.

Both columns are \(C^\infty\) in time with values in \(H_0^1\), with polynomial bounds in \(h^{-1}\). For the normal column this follows from its continuous incident values, bounded piecewise first normal derivatives, tangential smoothing and exact zero wall value; its position support is compact. The zero-trace characterization in the smooth Dirichlet reading then gives \(H_0^1\). For the actual column use (B90). Their negative-time data have arbitrarily small energy norms, by (B81) and (B90). From (B91) and the compact position support,
\[
 \begin{gathered}
 \|\partial_t^k F_h^{\rm small}(t)\|_{L^2}=O(h^N),\\
 \operatorname{supp}F_h^{\rm edge}
       \subseteq\operatorname{supp}_{\rm coeff}[P,\beta],\\
 \|\partial_t^k D_h(-2T)\|_{H^1}\\
       +\|\partial_t^{k+1}D_h(-2T)\|_2=O(h^N).
 \end{gathered}
 \tag{B94}
\]
Here \(\operatorname{supp}_{\rm coeff}[P,\beta]\) is the union of the supports of its differentiated-cutoff coefficients; it is disjoint from \(U\). All bounds hold for every finite \(k,N\), after increasing the construction accuracy. The edge term need only have a polynomial norm bound. Each forcing is \(C^\infty\) in time with values in \(L^2\). Equation (B93), \(D_h\in C^\infty H_0^1\), and the actual Dirichlet \(H^2\) estimate therefore give \(D_h\in C^\infty(H^2\cap H_0^1)\). This justifies the strong energy test below.

For completeness the local estimate permits this forcing and a general chart neighborhood. Choose a smooth real function \(b(x)\), positive on a compact smaller target patch \(K\), with its positive set contained in \(U\). Choose \(V\geq\sup\sqrt{p(x,db)}\), and take \(T>0\) so small that \(4VT<\frac12\inf_K b\). With the increasing smooth function \(\chi\) from (T159), put \(\varphi(t,x)=\chi(b(x)-V(t+2T))\), for \(-2T\leq t\leq2T\). The energy identity (T158), now with the additional term \(\operatorname{Re}(\varphi F\overline{D_{h,t}})\), gives
\[
 \begin{gathered}
 E_\varphi'(t)\leq C E_\varphi(t)\\
                +C\|\sqrt\varphi F_h^{\rm small}(t)\|_2^2,\\
 \|\partial_t^k D_h(t)\|_{H^1(K)}\\
       +\|\partial_t^{k+1}D_h(t)\|_{L^2(K)}=O(h^N),\\
 |t|\leq T.
 \end{gathered}
 \tag{B95}
\]
Indeed \(\varphi_t=-V\chi'\), \(d\varphi=\chi'db\), so the time-weight and flux terms have nonpositive sum by the same positive-form Cauchy–Schwarz argument as (T159). The lower coefficients contribute at most \(CE_\varphi\). Bound the forcing product by a constant times \(\varphi(|F|^2+|D_{h,t}|^2)\). The edge forcing vanishes on this weight's support. Integrate the resulting inequality from \(-2T\), using (B94). The weight has a fixed positive lower bound on \(K\), giving the second line. Apply this same argument to each time derivative of (B93), since \(P\) is time independent. No propagation-of-wavefront assertion is used as a quantitative bound.

## 26. From energy to the boundary diagonal

Put \(W_h(t)=D_h(t)-D_h(-t)\). On \(U\), where \(\beta=1\), its equation and boundary value are
\[
 \begin{gathered}
 (\partial_t^2+P)W_h
       =F_h^{\rm small}(t)-F_h^{\rm small}(-t),\\
 W_h|_{\partial X}=0,\\
 \|\partial_t^kW_h(t)\|_{H^s(K')}=O(h^N)
       \quad(|t|\leq T)
 \end{gathered}
 \tag{B96}
\]
for every fixed \(k,s,N\), on any fixed target patch \(K'\) compactly inside \(K\) relative to the manifold with boundary. The source remains uniform in the full retained collar.

Here are the regularity and size arguments for the last line. The odd forcing has all target spatial and time derivatives \(O(h^N)\), by (B92), including the smooth gauge and position factors on \(U\). Equation (B95) supplies the initial \(H^1\) bounds for every fixed number of time derivatives. On finitely many nested interior or boundary half-patches, apply the local estimates of Sections 2–3 of [Smooth Dirichlet regularity](smooth-dirichlet-powers.md) to
\(P\partial_t^kW_h=\partial_t^k F_{\rm odd}-\partial_t^{k+2}W_h\).
Their first step gives \(H^2\) from the \(L^2\) right side and the controlled local \(H^1\) norm. The higher steps give \(H^{r+2}\) from an \(H^r\) right side and the lower local norms. Induct simultaneously on spatial order for the finitely many needed time derivatives; start with enough of those derivatives in (B95). Every cutoff commutator is one order lower and is controlled on the preceding larger patch. The number of patches and derivatives is finite for a prescribed \(s,k\), so the constants do not depend on \(h,d,y\). All traces remain zero and every membership assertion is obtained before applying the next estimate. This proves (B96).

Use the bounded half-space extensions in Lemma 1.3 of that reading and Fourier Cauchy–Schwarz with \(s>n/2+j\). They bound the first \(j\) pointwise target derivatives by the \(H^s\) norm, uniformly up to the wall. Since \(\partial_tW_h=D_h'(t)+D_h'(-t)\), the actual cosine band and the normal one satisfy
\[
 \begin{gathered}
 C_{h,\Theta,Q}^P(t)
       =\sum_j\Theta(h^2\lambda_j)\cos(t\kappa_j)\\
 \qquad\cdot\Pi_jQ_h^\kappa(h^2\lambda_j),\\
 C_{h,\Theta,Q}^N(t)=
              \partial_tu_h^N(t)+\partial_tu_h^N(-t),\\
 |\partial_{x,t}^{\alpha}
       (C_{h,\Theta,Q}^P-C_{h,\Theta,Q}^N)|\\
                          \leq C_{\alpha,N}h^N,\quad |t|\leq T.
 \end{gathered}
 \tag{B97}
\]
The kernels in the last line of (B97) are evaluated at \((t,x;d,y)\). This is the required actual near-normal short-time comparison for a fixed smooth energy band and right cutoff. It includes pointwise diagonal evaluation and the wall limit. It does not assert a comparable theorem for the complementary phase regions. Source normal derivatives, which were not used, are not inferred from the target estimates.

<a id="sharp-near-normal-endpoint"></a>
## 27. The normal contribution with a sharp upper endpoint

We now apply the comparison without replacing a smooth temporal cutoff by a discontinuous one. On the diagonal \(x=(d,y)\) in \(K'\), set
\
 \begin{gathered}
 \mathcal H_h(E;d,y)=2[A_h(d,E)Q_h(d,E)\\
             +\sum_\sigma\widehat H_{\sigma,h}(d,d;E),\\
 C_{h,\Theta,Q}^N(t;x,x)
       =\frac{1}{2\pi h\,\gamma(d,y)}\\
 \quad\cdot\int_J\Theta(E)\cos(t\sqrt E/h)
                      \mathcal H_h(E;d,y)\,dE,\\
 |\mathcal H_h(E;d,y)|\leq C h^{-m}.
 \end{gathered}
 \tag{B98}
\]
For the formula, the normalization \((-\sigma ih)\widehat G_\sigma^DQ_h\) gives \(A_hQ_h\) for each incident branch at \(a=d\), and \(\widehat H_{\sigma,h}\) for its reflection. Adding the derivatives at \(t,-t\) in (B79) gives the cosine and the factor \(1/(2\pi h)\), exactly as in (B86). The two gauge factors cancel on the diagonal; \(\gamma^{-1}\) changes the coordinate half-density coefficient to density relative to \(dV_g\). The bound follows from (B58) and the compact-frequency phase kernel (B65), transferred by (B77). Their arbitrary small exact-kernel errors can be absorbed. The constants are uniform in distance.

Choose the nonnegative Schwartz smoothing function \(\rho\) from (B4), with \(\widehat\rho\) supported in the time interval where (B97) holds. Let \(F_\rho(s)=\int_{-\infty}^s\rho(v)\,dv\), and define the actual short-time band contribution
\[
 \begin{gathered}
 \mathscr A_h(x)=\frac1\pi\int
       \widehat\rho(t)\frac{\sin(t/h)}{t}\\
 \qquad\cdot C_{h,\Theta,Q}^P(t;x,x)\,dt,\\
 a_h(E)=F_\rho((1-\sqrt E)/h)\\
                  +F_\rho((1+\sqrt E)/h)-1.
 \end{gathered}
 \tag{B99}
\]
The quotient has its continuous value at zero. Equation (B97) permits replacing \(P\) by \(N\), with any prescribed power of \(h\) error: the time test costs at most \(C/h\), which is absorbed by increasing the kernel accuracy. Formula (B14) then identifies the resulting energy factor as \(a_h(E)\).

On the fixed compact positive interval \(J\),
\[
 \int_J|a_h(E)-1_{\{E\leq1\}}|\,dE\leq C h.
 \tag{B100}
\]
The second \(F_\rho\) term differs from one by arbitrarily high powers of \(h\), uniformly on \(J\). For the first put \(u=\sqrt E\), whose Jacobian \(2u\) is bounded there, and then \(v=(1-u)/h\). Its integral is bounded by
\(Ch\int_{\mathbb R}|F_\rho(v)-1_{\{v\geq0\}}|\,dv\).
Fubini for the nonnegative \(\rho\) identifies this last integral with \(\int|s|\rho(s)\,ds<\infty\). Values at a single endpoint do not change these Lebesgue integrals. Combining (B98)–(B100) gives the actual-kernel formula
\[
 \begin{gathered}
 \mathscr A_h(x)=\frac{1}{2\pi h\,\gamma(d,y)}\\
 \quad\cdot\int_{J\cap(-\infty,1]}\Theta(E)\mathcal H_h(E;d,y)\,dE\\
                 +O(h^{1-n}).
 \end{gathered}
 \tag{B101}
\]
The error is \(h^{-1}\cdot O(h^{-m})\cdot O(h)=O(h^{-m})\). This retains the sharp upper endpoint while using only the fixed smooth \(\theta\) in the wave comparison.

For example choose \(\Theta\) supported above \(E_0\), zero near \(E_0\), and equal to one near \(1\). The incident principal term and the reflected frozen term in (B101) are
\[
 \begin{gathered}
 I_h(x)=\frac{(2\pi h)^{-n}}{\gamma(d,y)}\\
 \quad\cdot\int_{E_0}^1\int
         \frac{\Theta(E)q(d,y,\eta,E)}{\lambda_d}\,d\eta\,dE,\\
 R_{h,0}(x)=-\frac{(2\pi h)^{-n}}{\gamma(0,y)}\\
 \quad\cdot\sum_\sigma\int_{E_0}^1\int
          e^{2i\sigma d\lambda_0/h}\\
 \qquad\cdot\frac{\Theta(E)q(0,y,\eta,E)}{2\lambda_0}\,d\eta\,dE,\\
 \lambda_d=\sqrt{E-r(d,y,\eta)},\\
 \lambda_0=\sqrt{E-r(0,y,\eta)}.
 \end{gathered}
 \tag{B102}
\]
Equation (B58) gives the incident formula, with its \(h\) amplitude correction bounded absolutely by \(O(h^{1-n})\). For the reflected part use (B68) for the exact second-order family, as justified in (B77), with the smooth lower energy cutoff \(\Theta\) and the actual upper endpoint \(1\). Thus
\[
 \begin{gathered}
 \mathscr A_h(x)=I_h(x)+R_{h,0}(x)\\
          +O(h^{1-n}),\quad 0\leq d\leq d_0.
 \end{gathered}
 \tag{B103}
\]
Thus (B103) gives the actual contribution of the specified smooth lower energy band and near-normal right cutoff, with all lower-order terms, density factors and the sharp upper endpoint retained. The full-frequency estimate is proved in Sections 31–38.

<a id="complementary-frozen-boundary-model"></a>
## 28. Tangential energy coordinates through glancing

The roots used in Sections 6–27 stay separated. For the complementary region, the normal roots may merge. We first prove the exact frozen scalar model and its uniform estimates there. This is a necessary model calculation, not yet a comparison with the variable-coefficient wave.

Keep a compact positive energy interval \(J\), and use \(\alpha\) for the distance at which the coefficients are frozen. The observation distance \(d\) will remain a separate variable. Put
\[
 \begin{gathered}
 r_\alpha(y,\eta)=\eta^TG(\alpha,y)\eta,\quad m=n-1,\\
 q=q(\alpha,y,\eta,E),\\
       \operatorname{supp}_\eta q\subseteq
                     \{\epsilon\leq|\eta|\leq R\},\\
 \eta\cdot\partial_\eta r_\alpha=2r_\alpha
                \geq c|\eta|^2 .
 \end{gathered}
 \tag{B104}
\]
Here \(0<\epsilon<R\) are fixed, \(q\) is smooth with uniform derivatives, and all ordinary parameters range over compact sets. An additional parameter \(h\) is allowed with the same bounds; its derivatives are not required. The last identity proves a quantitative tangential energy direction on the entire support, including the normal glancing set \(E=r_\alpha\). In particular at least one component of \(\partial_\eta r_\alpha\) has a fixed positive absolute lower bound on each member of a finite cover.

We give the integration argument rather than assuming a coarea formula at a merging normal root. On each smaller member of that cover, choose the component \(\eta_j\) with nonzero derivative. The change of coordinates
\((\eta_j,\widehat\eta)\mapsto(v=r_\alpha(y,\eta),\widehat\eta)\)
is a smooth diffeomorphism there, by the parameter inverse theorem in [Coordinate inverses and integration](coordinate-inverses-and-integration.md). Choose a smooth partition with support compactly inside these charts. A chart contribution to \(q\,d\eta\) becomes
\(b_j(\alpha,y,v,\widehat\eta,E)\,dv\,d\widehat\eta\), where the Jacobian factor is \(1/|\partial_{\eta_j}r_\alpha|\). Extend \(b_j\) by zero outside its chart. All derivatives are uniformly bounded and its support is compact. The ordinary change-of-variables proof in that reading applies without an orientation sign because this is a density.

Define
\[
 \begin{gathered}
 A_q(s,E;\alpha,y)\\
    =\sum_j\int
       b_j(\alpha,y,E-s^2,\widehat\eta,E)\,d\widehat\eta,\\
 A_q(-s,E;\alpha,y)=A_q(s,E;\alpha,y),\\
 |\partial_{s,E,\alpha,y}^{\beta}A_q|\leq C_\beta,\\
       \operatorname{supp}_s A_q\subseteq[-C,C].
 \end{gathered}
 \tag{B105}
\]
The bounds follow by differentiation under an integral on one fixed compact set. They hold through \(s=0\). In dimension \(n=2\), the \(\widehat\eta\) integral is an integral over zero variables, so it is simply evaluation and the same proof applies.

For fixed \(s\), this is precisely the density obtained by integrating \(q\) on the tangential energy level \(r_\alpha=E-s^2\). More explicitly, if \(\varphi\) is a compactly supported smooth test in \(E\), change variables \(E=s^2+v\) in each chart to obtain
\[
 \begin{gathered}
 \int\varphi(E)A_q(s,E;\alpha,y)\,dE\\
   =\int\varphi(s^2+r_\alpha)\\
 \qquad\cdot q(\alpha,y,\eta,s^2+r_\alpha)\,d\eta .
 \end{gathered}
\]
This identity defines any delta notation for the energy level used below. It proves smoothness by the tangential variable, with no division by the vanishing normal root.

## 29. The exact frozen Dirichlet resolvent and density

For fixed \(\eta,\alpha,y\), consider
\(H_\eta=-h^2\partial_a^2+r_\alpha(y,\eta)\) on the half-line \(a>0\), with the Dirichlet domain. Its realization is the odd restriction of the whole-line Fourier multiplier, as proved for the half-space in Section 1 of [Reflection and the Dirichlet boundary coefficient](../../src/reflection-and-the-dirichlet-boundary-coefficient.md). The same odd unitary map and the substitution of \(hD_a\) give that proof for every constant \(r_\alpha\).

For \(\operatorname{Im}z>0\), let \(\kappa=(z-r_\alpha)^{1/2}\) be the root with positive imaginary part. The inverse of \(H_\eta-z\) has kernel
\[
 \begin{gathered}
 F_\kappa(v)=e^{i\kappa v/h},\\
 G_\eta(z;a,b)=\frac{i}{2h\kappa}\\
 \qquad\cdot\left(F_\kappa(|a-b|)-F_\kappa(a+b)\right),\\
 G_\eta(z;0,b)=0,\\
 [\partial_aG_\eta]_{a=b}=-h^{-2},\\
 \|(H_\eta-z)^{-1}\|_{L^2\to L^2}
                           \leq(\operatorname{Im}z)^{-1}.
 \end{gathered}
 \tag{B106}
\]
Indeed both exponentials solve the homogeneous ordinary differential equation off \(a=b\); their values are continuous and the displayed derivative jump gives a unit delta after multiplication by \(-h^2\). The image term enforces the zero boundary value. For compactly supported input the formula and its derivative decay at infinity and give the inverse equation. The odd Fourier multiplier has inverse symbol \((s^2+r_\alpha-z)^{-1}\), bounded by \((\operatorname{Im}z)^{-1}\), which proves existence and that norm bound. Uniqueness follows either from this multiplier or by taking the imaginary part of the Dirichlet energy identity. Thus the kernel formula is the actual inverse of the frozen operator.

At glancing the quotient in this formula has a finite limit for fixed \(a,b\). Its first exponential difference is
\(i\kappa(|a-b|-a-b)/h+O(\kappa^2)\). Consequently
\[
 \begin{gathered}
 \lim_{\substack{z\to r_\alpha\\ \operatorname{Im}z>0}}
          G_\eta(z;a,b)\\
 \qquad=h^{-2}\min(a,b),\\
 \frac1\pi\operatorname{Im}G_\eta(E+i0;d,d)\\
   =\frac{1-\cos(2d\sqrt{E-r_\alpha}/h)}
               {2\pi h\sqrt{E-r_\alpha}},
                \quad E>r_\alpha.
 \end{gathered}
 \tag{B107}
\]
For \(E<r_\alpha\) the boundary value is real, so its imaginary part is zero. At \(E=r_\alpha\) the second expression extends by zero, since its numerator is \(O(E-r_\alpha)\). This limit does not assert bounded derivatives of the separate normal roots.

For clarity the spectral-density interpretation does not rely on an unproved boundary-value theorem. The odd Fourier representation gives the diagonal normal spectral projector
\((2\pi h)^{-1}\int_{s^2+r_\alpha\leq E}(1-\cos(2ds/h))\,ds\).
For \(E>r_\alpha\), differentiation of its two endpoints gives exactly (B107). Below the threshold it is zero. The continuous cumulative function has no jump at the threshold and hence no atom there. This proves the asserted density directly from the unitary multiplier representation.

Restore the tangential Fourier factor \((2\pi h)^{-m}\) and the constant frozen volume density \(\gamma(\alpha,y)\). Multiplying the spectral density at energy \(E\) by \(q(\alpha,y,\eta,E)\), and then integrating in \(\eta\), yields
\[
 \begin{gathered}
 D^0_{h,q}(d,E;\alpha,y)\\
    =\frac{(2\pi h)^{-n}}{\gamma(\alpha,y)}\\
 \qquad\cdot\int_{\mathbb R}
       (1-\cos(2ds/h))\\
 \qquad\cdot A_q(s,E;\alpha,y)\,ds .
 \end{gathered}
 \tag{B108}
\]
One can verify the equality by testing in \(E\) and using the identity after (B105), followed by the odd Fourier formula. Every integral then has compact frequency support. The energy dependence of \(q\) weights the spectral measure; it is not differentiated as if this were the derivative of a cumulative expression already containing \(q(E)\). This also fixes the factor of two from the two normal signs. The result is smooth in \(E\), with uniform tangential and coefficient-parameter derivatives, despite the possible glancing in its individual \(\eta\) contributions.

## 30. A sharp energy endpoint and rapid decay of the complementary image

Let \(\Theta\) be a fixed smooth lower energy cutoff on \(J\), zero near a fixed \(E_0>0\). For an upper endpoint \(e\) in a fixed smaller positive interval in \(J\), define
\[
 \begin{gathered}
 Z_q(s,e;\alpha,y)\\
       =\int_{E_0}^{e}\Theta(E)A_q(s,E;\alpha,y)\,dE,\\
 \mathcal I^0_{h,q}(\alpha,y,e)
       =\frac{(2\pi h)^{-n}}{\gamma(\alpha,y)}\\
 \qquad\cdot\int Z_q(s,e;\alpha,y)\,ds,\\
 \mathcal R^0_{h,q}(d;\alpha,y,e)
       =-\frac{(2\pi h)^{-n}}{\gamma(\alpha,y)}\\
 \qquad\cdot\int\cos(2ds/h)Z_q(s,e;\alpha,y)\,ds .
 \end{gathered}
 \tag{B109}
\]
The exact frozen weighted cumulative contribution is
\(\mathcal I^0_{h,q}+\mathcal R^0_{h,q}\). Equation (B105) proves that \(Z_q\) is smooth and compactly supported in \(s\), with every derivative in \(s,e,\alpha,y\) uniformly bounded. Differentiation in \(e\) evaluates a smooth integrand at that endpoint. Thus the sharp upper endpoint does not destroy smoothness in \(s\); that conclusion uses the tangential energy coordinate and the exclusion of \(\eta=0\).

For \(D=d/h\), repeated integration by parts in \(s\) now gives
\[
 \begin{gathered}
 \mathcal F_q(D;\alpha,y,e)
       =h^n\mathcal R^0_{h,q}(hD;\alpha,y,e),\\
 |\partial_{D,e,\alpha,y}^{\beta}\mathcal F_q|
           \leq C_{\beta,N}(1+D)^{-N},\\
 D\geq0,\\
 \left|\begin{gathered}
 \mathcal R^0_{h,q}(d;d,y,e)\\
       -\mathcal R^0_{h,q}(d;0,y,e)
 \end{gathered}\right|
                  \leq C h^{1-n},\\
 0\leq d\leq d_0 .
 \end{gathered}
 \tag{B110}
\]
For the first line, \(D\) derivatives multiply the compact amplitude by powers of \(s\). If \(D\geq1\), write the cosine as two exponentials and integrate \(N\) times; the boundary terms vanish because the amplitude is smooth and compactly supported. For \(D\leq1\), use its bounded \(L^1\) norm. Parameter derivatives of \(\gamma^{-1}\) are bounded and cause no change in this argument.

For the second line keep \(D=d/h\) fixed while integrating the coefficient derivative in \(\alpha\) from zero to \(d\). The first line bounds the difference by
\(C_N d h^{-n}(1+d/h)^{-N}\).
For \(N\geq1\), this is at most \(C h^{1-n}\). This estimate includes the glancing frequencies in (B104). It freezes all smooth coefficient and cutoff factors while retaining the observation distance in the oscillation.

Here is the exact model partition that connects this calculation to the earlier normal one. Choose a tangential cutoff \(q_0\) equal to one on a sufficiently small neighborhood of \(\eta=0\), supported where the roots stay separated for \(E\geq E_0\). Choose a compact tangential cutoff \(\chi\) equal to one wherever \(r_\alpha\leq\sup J\), on all retained coefficient parameters, and equal to one on the support of \(q_0\). Set \(q_1=\chi-q_0\). Then \(q_1\) has the support required in (B104), and \(q_0+q_1=1\) on every frozen energy shell in \(J\).

For \(q_0\), define \(D^0_{h,q_0}\) by the exact odd Fourier spectral density preceding (B108), with \(q_0\) inserted. Its separated roots give the ordinary formula
\((2\pi h)^{-n}\gamma^{-1}\int q_0(1-\cos(2d\sqrt{E-r_\alpha}/h))/\sqrt{E-r_\alpha}\,d\eta\).
Thus this use of \(D^0_{h,q_0}\) does not assume that the tangential energy coordinates in (B105) exist at \(\eta=0\). Linearity of the exact odd Fourier formula gives
\[
 \begin{gathered}
 \sum_{j=0}^1\int_{E_0}^{1}
                  \Theta(E)D^0_{h,q_j}(d,E;\alpha,y)\,dE\\
 \quad=\frac{(2\pi h)^{-n}}{\gamma(\alpha,y)}\\
 \qquad\cdot\int_{\{s^2+r_\alpha\leq1\}}
             \Theta(s^2+r_\alpha)\\
 \qquad\cdot(1-\cos(2ds/h))\,ds\,d\eta .
 \end{gathered}
 \tag{B111}
\]
Here \(\Theta\) is extended by zero below \(E_0\). The same partition may be made smoothly in the coefficient parameters by fixed slightly larger frequency cutoffs. No high-frequency remainder appears in this **frozen** identity because the spectral support itself bounds \(r_\alpha\).

Equations (B104)–(B111) describe the complementary frozen contribution through glancing, its coefficient-freezing error and the complete frozen band partition. They do not compare the variable-coefficient complementary family or frequencies outside that band. Sections 31–38 instead estimate the entire cosine distribution directly.

<a id="scaled-reflected-parametrix"></a>
## 31. A fixed spatial region after dilation

We prove (B16) using a finite reflected wave construction with its actual smooth error and the [joint no-return kernel estimate](diffractive-phase-neighborhoods.md#joint-kernel-parameters), equation (T194). All constants may depend on the fixed operator, dimension and finitely many coefficient bounds.

Use boundary normal coordinates, and represent half densities by their coefficients relative to the coordinate half density. After a constant tangential linear change at a boundary point \(y_0\), the principal matrix at that point is the identity. These changes can be chosen smoothly on finitely many boundary patches: the positive matrix square root follows, for example, by the uniformly convergent power series for \((I-B)^{1/2}\), after a fixed positive scalar rescaling makes \(\|B\|<1\). Its differentiated series converge on the same compact spectral interval. Put \(z=(z',z_n)\), with wall \(z_n=0\), and dilate the original coordinates about \(y_0\) by \(\varepsilon\). The resulting differential operator, multiplied by \(\varepsilon^2\), has the form
\[
 \begin{gathered}
 P_\varepsilon
 =-\partial_i(A_\varepsilon^{ij}\partial_j)
       +b_\varepsilon^i\partial_i+c_\varepsilon,\\
 A_\varepsilon^{nn}=1,\quad A_\varepsilon^{in}=0\ (i<n),\\
 A_0=I,\quad b_0=0,\quad c_0=0,\\
 \gamma_\varepsilon(z)=(\det A_\varepsilon(z))^{-1/2}.
 \end{gathered}
 \tag{B112}
\]
Here \(b_\varepsilon=O(\varepsilon)\), \(c_\varepsilon=O(\varepsilon^2)\), and \(A_\varepsilon-I=O(\varepsilon)\) on every fixed bounded \(z\)-region, in every fixed derivative norm. The divergence rewriting includes derivatives of the original principal coefficients; no lower-order term is discarded. Parameters \(y_0\) are retained throughout.

Fix a scaled time bound \(T_*=33\). Take a much larger fixed coordinate ball, with radius exceeding \(100(T_*+1)\), and then reduce the permitted \(\varepsilon\). The compact extension in (T174)–(T175) works with this radius: increase the tangential periods and normal interval before choosing \(\varepsilon\), keep the operator unchanged on that ball, and make it flat outside a slightly larger ball. The same form absorption and fixed-interval Poincaré argument give a common positive Dirichlet realization. All finite elliptic and energy estimates used in (T176) remain uniform. Finite propagation (T157)–(T160), first for smooth data and then for the source limits in (T182)–(T186), identifies its kernel with the physical scaled kernel for the times and points considered here.

Let \(\Pi=(0,1)\). We need ordinary and once-reflected geodesic coordinates about \(\Pi\), also for sources \(y\) in a small fixed neighborhood of \(\Pi\). The metric is \(A_\varepsilon^{-1}\). Its geodesic equations are the Hamilton equations already constructed by the integral equation in (G13); differentiating that integral equation and applying the elementary integral inequality used there proves smooth dependence on all initial data and parameters on this fixed interval. At \(\varepsilon=0\), the two endpoint maps, with initial tangent vector \(S\), are
\[
 \begin{gathered}
 \mathcal E_0(S)=\Pi+S,\\
 \mathcal E_0^{\,r}(S)=(S',-1-S_n),\qquad S_n<0.
 \end{gathered}
 \tag{B113}
\]
The second map continues the incoming ray to the wall and then reverses its normal velocity.

Here are uniform domains for this construction. Take a large fixed \(R>4(T_*+3)\). On \(|S|<R,\ S_n<-1/2\), the flat wall-hit parameter is \(-1/S_n\); the angle of incidence is bounded below by \(1/(2R)\). Extend the metric smoothly across the wall for this calculation. The equation for the hit has a uniformly nonzero time derivative, so the proved coordinate inverse lemma gives a smooth hit time for small \(\varepsilon\). Reflect the velocity using the metric normal and continue the flow, allowing a negative remaining time when defining the extended endpoint map. Flow estimates make this map and its first derivative uniformly close to (B113). Its derivative stays invertible. More strongly, on this convex \(S\)-domain the fundamental theorem of calculus gives
\[
 |\mathcal E_\varepsilon^{\,r}(S)
       -\mathcal E_\varepsilon^{\,r}(\widetilde S)|
 \geq \tfrac12|S-\widetilde S|.
 \tag{B114}
\]
Indeed subtract the fixed flat orthogonal linear part and bound the derivative of the difference by \(1/2\). Thus the map is one-to-one. Every retained physical point with \(|z-\Pi|\leq 2T_*+3,\ z_n\geq0\) lies in its image: its flat inverse stays a fixed distance from the domain boundary; the map which subtracts the small nonlinear error from this flat inverse is a contraction on a fixed small closed ball. The convergent iteration proves existence, and the inverse lemma proves smoothness. The same argument applies to the ordinary endpoint map on \(|S|<R\), and uniformly when \(y\) moves slightly.

All reflected physical segments so obtained occur after the first wall hit. They have no second wall hit in the retained time interval. At the first hit their outward-to-inward reflected normal speed has a fixed positive lower bound; the acceleration is \(O(\varepsilon)\) on this bounded region. Its total change is smaller than half that bound when \(\varepsilon\) is small. This argument also shows that no grazing ray is being omitted from the causal region issuing from a source at height near one: any ray reaching the wall within the fixed time has initial normal speed bounded away from zero.

Write \(G_y=A_\varepsilon(y)^{-1}\) and \(r=|S|_{G_y}\). The ordinary and broken geodesic lengths are \(r\). Both coordinate pullbacks of the metric have the radial identity
\[
 A(S)G_y S=S.
 \tag{B115}
\]
For completeness, differentiate the length of a unit-speed geodesic variation. Integration of the derivative of its kinetic energy leaves only the endpoint scalar products, because the geodesic equation cancels the interior term. For a broken geodesic there is an additional wall term: the difference of the incoming and outgoing momenta paired with the moving wall point. It is zero because that motion is tangent to the wall and the two tangential momenta agree. Consequently the endpoint radial velocity has scalar product with an arbitrary endpoint variation equal to \(G_y S\cdot dS/r\). This is the metric identity dual to (B115). It proves that identity for both coordinate systems without a separate geometric comparison theorem. At \(z=y=\Pi\), the reflected length is exactly two: the boundary normal line goes down a unit distance and back a unit distance for every \(\varepsilon\), and uniqueness in (B114) identifies it with the reflected inverse just constructed.

<a id="flat-causal-distributions"></a>
## 32. Flat causal distributions from Fourier multipliers

Let \(L_0=\partial_t^2-\Delta_z\). Define distributions \(E_\nu\), \(\nu=0,1,\ldots\), by their spatial Fourier transforms
\[
 \widehat E_\nu(t,\xi)
 =(-\partial_\lambda)^\nu
   \left[H(t)\frac{\sin(t\sqrt\lambda)}{\sqrt\lambda}\right]
       _{\lambda=|\xi|^2}.
 \tag{B116}
\]
The quotient is defined at zero by its power series. The derivatives in (B116) have polynomial bounds in \(t,\xi\) on compact time intervals, so integration against Schwartz functions defines distributions. Differentiation of the scalar equation gives
\[
 \begin{gathered}
 L_0E_0=\delta_{(0,0)},\\
 L_0E_\nu=\nu E_{\nu-1}\quad(\nu\geq1),\\
 -2\partial_{z_i}E_\nu=z_iE_{\nu-1}\quad(\nu\geq1).
\end{gathered}
 \tag{B117}
\]
For the second identity differentiate the spatial Fourier transform in \(\xi_i\); the factor is \(2\xi_i\partial_\lambda\), with the sign supplied by the alternating derivative. These operations are valid on Schwartz tests. Rotation invariance follows from the same definition.

Each \(E_\nu\) is supported in \(t\geq |z|\). For \(E_0\), approximate the initial delta by smooth data supported in a ball of radius tending to zero. The constant-coefficient energy identity (T158), applied on growing bounded balls and with the exterior cone weight, gives support in \(t\geq |z|-\eta\). The Fourier formula gives distributional convergence to \(E_0\), proving its asserted support. For the induction, convolution of two distributions supported in the forward cone is well-defined: over the inverse image of a compact set under addition, their two time coordinates are nonnegative and bounded, hence both spatial coordinates are bounded. Insert a compact cutoff equal to one there into the tensor-product pairing. Its value is independent of the cutoff; smoothing both factors gives the usual convolution identities in the limit. Then
\(E_\nu=\nu E_0*E_{\nu-1}\): both sides solve the same forced equation with zero past, as is verified either by (B116) or by the scalar Fourier ordinary differential equation. This proves support by induction.

With \(s=1+i\tau\), the joint Fourier transform of \(e^{-t}E_\nu\) is
\[
 \frac{\nu!}{(|\xi|^2+s^2)^{\nu+1}}.
 \tag{B118}
\]
This follows by integrating the elementary damped sine transform and differentiating in \(\lambda\). There is a constant \(c>0\) such that
\(\big||\xi|^2+(1+i\tau)^2\big|\geq c\langle(\tau,\xi)\rangle\).
If \(|\xi|\leq2(1+|\tau|)\), use its imaginary part \(2\tau\) for large \(|\tau|\) and compactness for bounded \(\tau\); if \(|\xi|>2(1+|\tau|)\), use its positive real part. Thus for \(\nu>n+q\), multiplying (B118) by any polynomial of degree at most \(q\) gives an integrable function on \(\mathbb R^{1+n}\). Fourier inversion proves \(E_\nu\in C^q\) on compact time regions. In particular its derivatives through order \(q\) vanish at \(t=0\), since it vanishes for negative time. Taking \(\nu\) larger allows any specified finite number of coordinate and parameter derivatives after a smooth pullback.

The even full-time distributions needed for cosine kernels are
\[
 \begin{gathered}
 C_\nu(t,z)=\partial_t[E_\nu(t,z)-E_\nu(-t,z)],\\
 \widehat C_\nu(t,\xi)
   =(-\partial_\lambda)^\nu\cos(t\sqrt\lambda)
       \big|_{\lambda=|\xi|^2}.
 \end{gathered}
 \tag{B119}
\]
They have a well-defined restriction to every fixed \(z\), including zero. Indeed time testing of the second formula produces a smooth function of \(\xi\) decreasing faster than every power, also after multiplication by any fixed power of \(\xi\). At \(\xi=0\), smoothness follows from the even Taylor expansion of the cosine transform. Spatial Fourier inversion therefore defines a smooth function of \(z\) with values in time distributions. We write \(C_\nu(t,r)\) for its value at any vector of length \(r\). For \(r>0\), cone support gives
\[
 \operatorname{supp} C_\nu(\,\cdot\,,r)
       \subset\{|t|\geq r\}.
 \tag{B120}
\]
This definition avoids restricting the individual retarded fundamental solution to its singular vertex.

<a id="full-radial-transport"></a>
## 33. Transport with the complete differential operator

Pull \(P_\varepsilon\) back by either endpoint map. Rewrite it as
\(P=-\operatorname{div}(A\nabla)+b\cdot\nabla+c\)
in the \(S\)-coordinates. The transformed first-order coefficient includes the coordinate Jacobian terms. The matrix identity (B115) gives
\(\operatorname{div}(A\nabla f(r))=\operatorname{div}(G_y^{-1}\nabla f(r))\).
This follows by substituting \(\nabla f=G_y S f'(r)/r\); both vector fields equal \(S f'(r)/r\). It remains valid for radial distributions by smoothing radially and taking limits.

Put \(h(S)=b(S)\cdot G_y S\). The product rule and (B117) show that the coefficient of \(E_{\nu-1}(t,r)\) in \(L(u_\nu E_\nu)\), for \(\nu\geq1\), is
\(\nu u_\nu+S\cdot\nabla u_\nu-hu_\nu/2\).
The remaining term is \((Pu_\nu)E_\nu\). Choose
\[
 \begin{gathered}
 2S\cdot\nabla u_0-hu_0=0,\quad u_0(0)=1,\\
 (\nu+S\cdot\nabla-h/2)u_\nu=-Pu_{\nu-1},\\
 u_0(S)=\exp\!\left(\frac12\int_0^1
                         \frac{h(aS)}a\,da\right),\\
 u_\nu(S)=-u_0(S)\int_0^1
       a^{\nu-1}\frac{(Pu_{\nu-1})(aS)}{u_0(aS)}\,da.
 \end{gathered}
 \tag{B121}
\]
Since \(h(0)=0\), every integrand is smooth at the lower endpoint; the formula for \(u_0\) can equally be written using the integral of \(dh\) along the segment. The displayed integrals and differentiation under them prove smoothness and all finite uniform parameter bounds. Differentiating along a ray verifies the equations. A bounded homogeneous solution of the equation for \(u_\nu/u_0\), \(\nu>0\), is a multiple of \(r^{-\nu}\), so regularity at the origin gives uniqueness.

There is no unaccounted vertex term for \(\nu=0\). Its cross term is
\(V\cdot\nabla E_0\), where \(V=u_0b-2A\nabla u_0\); transport says \(V\cdot G_yS=0\). After a constant linear change making \(G_y=I\), a smooth tangent vector field satisfies \(V(0)=0\) and can be written
\[
 \begin{gathered}
 V_i(S)=\sum_j a_{ij}(S)S_j,\\
 a_{ij}=\int_0^1 a
       (\partial_jV_i-\partial_iV_j)(aS)\,da.
\end{gathered}
 \tag{B122}
\]
To verify this, differentiate \(S\cdot V(S)=0\), sum over \(j\), and integrate
\(d[aV_i(aS)]/da\). The matrix \(a_{ij}\) is skew. Every resulting angular derivative annihilates the radial distribution \(E_0\). This proves the cancellation at the vertex as well as away from it.

For the reflected coefficients \(v_\nu\), solve the same transport equations in the reflected coordinates, now prescribing their values on the wall to be the incident coefficients at that same physical point. The wall in each radial direction is \(r=r_b>0\), with \(r_b\) smooth and uniformly separated from zero on the retained domain. The equation \(r v_0'-h v_0/2=0\) is solved by its integrating factor with the specified boundary value; for \(\nu>0\), multiply the equation for \(v_\nu/v_0\) by \(r^\nu\) and integrate its known right side from \(r_b\) to \(r\). Equivalently one can use the nonvanishing homogeneous integrating factor even when the prescribed \(v_0\) is not used as a divisor. Here \(v_0\) is nonzero after shrinking \(\varepsilon\), since its flat value is one. These explicit one-dimensional integrations prove smoothness, uniqueness and all finite uniform bounds, including the source and \(\varepsilon\) parameters.

At a wall point the ordinary and reflected lengths agree, and the coefficients were chosen equal. Their difference therefore has zero Dirichlet trace term by term. Telescoping (B121) gives the following finite retarded kernel, relative to Lebesgue measure in the original scaled coordinates:
\[
 \begin{gathered}
 K_N(t,z,y)=\gamma_\varepsilon(y)
                    \sum_{\nu=0}^N(I_\nu-J_\nu),\\
 I_\nu=u_\nu E_\nu(t,r_i),\quad
 J_\nu=v_\nu E_\nu(t,r_r),\\
 (\partial_t^2+P_{\varepsilon,z})K_N\\
       =\delta(t)\delta_y(z)+F_N(t,z,y).
\end{gathered}
 \tag{B123}
\]
In (B123), the coefficients and lengths in \(I_\nu,J_\nu\) are evaluated at \((z,y)\). Here \(F_N/\gamma_\varepsilon(y)\) is
\((P_\varepsilon u_N)E_N(t,r_i)
 -(P_\varepsilon v_N)E_N(t,r_r)\).
The factor \(\gamma_\varepsilon(y)\) is essential: the constant-metric radial fundamental solution has source
\((\det A_\varepsilon(y))^{1/2}\delta_y\).
This follows by the linear substitution \(S=A_\varepsilon(y)^{1/2}w\); the ordinary endpoint map has derivative the identity at the source. Multiplication by \(\gamma_\varepsilon(y)\) gives exactly the unit delta in (B123).

For \(\varepsilon=0\), both pulled-back operators are \(-\Delta\). Consequently \(u_0=v_0=1\) and \(u_\nu=v_\nu=0\) for \(\nu\geq1\). Smooth dependence and the fundamental theorem of calculus give, at the diagonal \(z=y=\Pi\),
\[
 \begin{gathered}
 u_0(\Pi,\Pi)=1,\quad r_i(\Pi,\Pi)=0,\\
 r_r(\Pi,\Pi)=2,\quad |v_0(\Pi,\Pi)-1|\leq C\varepsilon,\\
 |u_\nu(\Pi,\Pi)|+|v_\nu(\Pi,\Pi)|
       \leq C_\nu\varepsilon\quad(\nu\geq1).
 \end{gathered}
 \tag{B124}
\]
These bounds retain every lower-order coefficient.

<a id="actual-reflected-kernel-error"></a>
## 34. The smooth error is an error for the actual kernel

Choose a spatial cutoff equal to one on the entire causal region from the source neighborhood for \(0\leq t\leq T_*\), supported inside the larger region of Section 31. Such a cutoff can be chosen independently of the parameters. Indeed the metric is uniformly close to the identity, so a path of length at most \(T_*+1\) stays in \(|z-\Pi|<2T_*+3\). Put the cutoff transition farther away. On its transition, both terms of (B123) vanish by cone support throughout the retained time interval. Multiplying the parametrix by this cutoff introduces no forcing there. It also preserves the exact wall cancellation. The construction now extends by zero to the fixed compact extension.

For any prescribed finite integer \(q\), choose \(N\) sufficiently large in (B118). The residual is jointly \(C^q\) in time, target, source and the retained parameters, vanishes to as many prescribed orders at \(t=0\) as needed, and obeys
\[
 \|F_N\|_{C^q([0,T_*]\times X\times Y)}
       \leq C_q\varepsilon.
 \tag{B125}
\]
The same statement holds with any specified finite list of derivatives in \(y_0\) and one derivative in \(\varepsilon\) before taking the final \(O(\varepsilon)\) difference. To justify it at the incident vertex, work in the smooth vector coordinate \(S\), where \(E_N(t,|S|_{G_y})\) is a \(C^{q'}\) function for a larger chosen \(q'\). The radial square root need not be differentiated at \(S=0\). Every coefficient and map is smooth on the fixed compact region. At \(\varepsilon=0\), \(F_N=0\); integrate its uniformly bounded \(\varepsilon\)-derivative.

We give the finite regularity estimate that turns (B125) into an actual kernel error. If
\[
 \begin{gathered}
 (\partial_t^2+P_\varepsilon)V=F,\\
 V|_{\partial X}=0,\quad V(0)=V_t(0)=0.
\end{gathered}
 \tag{B126}
\]
then a sufficiently large finite collection of ordinary derivatives of a smooth \(F\), vanishing to sufficiently high time order at zero, bounds any specified \(C^r\) norm of \(V\). All constants are uniform in this compact coefficient family.

Here are the details of the estimate. The full-coefficient energy inequality (T158), or its unweighted case integrated in time, bounds
\(\|V_t(t)\|_2+\|V(t)\|_{H^1}\)
by \(C\int_0^t\|F(s)\|_2\,ds\). Apply it to \(\partial_t^jV\). Differentiating the equation at zero shows that its two initial values are zero as long as the corresponding derivatives of \(F\) vanish there. Thus any specified finite number of time derivatives is bounded in \(H^1\). The [smooth Dirichlet reading](smooth-dirichlet-powers.md), Theorem 3.1, equation (16), with the uniform-constant argument in (T176), gives, for integers \(a\geq0\),
\[
 \begin{gathered}
 \|\partial_t^jV\|_{H^{a+2}}\\
 \leq C_a\bigl(
  \|\partial_t^jF\|_{H^a}
  +\|\partial_t^{j+2}V\|_{H^a}\\
 \qquad{}+\|\partial_t^jV\|_2\bigr).
\end{gathered}
 \tag{B127}
\]
Starting with the time-energy bounds and descending through a sufficiently long finite list of time derivatives proves this estimate successively for every needed spatial order. Smooth approximation of \(F\), the energy difference estimate and the elliptic estimate justify the induction for the solution defined by the spectral sine propagator. Sobolev embedding, proved by the Fourier extension argument in the same reading, then bounds the requested ordinary derivatives up to the wall.

Source derivatives commute with (B126) and differentiate \(F\) only. A coefficient-parameter derivative satisfies the same equation with forcing
\(\partial_\omega F-(\partial_\omega P_\varepsilon)V\).
The second term uses at most two additional spatial derivatives of the already bounded \(V\). Induction on the desired finite number of parameter derivatives, choosing two more spatial orders at each such step, proves the claimed uniform estimate. This argument uses only the common first Dirichlet domain and ordinary boundary elliptic estimates; it does not differentiate a parameter-dependent higher power domain. In particular (B125) bounds the solution and its first time derivative, jointly at target and source, by \(C\varepsilon\).

The actual retarded sine kernel minus \(K_N\) is the solution of (B126) with forcing \(-F_N\). One can verify the identification without assuming pointwise convergence of a wave series. Test first against a smooth source function supported near \(\Pi\). The source and boundary terms in (B123) are exact, so subtraction has zero past and the smooth forcing just described. Uniqueness follows by testing the homogeneous difference against Dirichlet eigensections: its scalar coefficients solve \(v_j''+\lambda_jv_j=0\) with zero past and hence vanish. Distributional testing is legitimate after time smoothing; the zero boundary trace removes the boundary term, and the resulting finite-order distributions are recovered by removing the smoothing. Completeness of the smooth spectral tests, equivalently inverse-power regularization (W9)–(W12), gives zero difference. Differentiation in the smooth source parameter followed by testing identifies the jointly smooth error kernel. Thus this is an equality of the actual kernels.

Write \(a_\nu=u_\nu(\Pi,\Pi)\) and \(b_\nu=v_\nu(\Pi,\Pi)\). Taking the odd-time difference and one time derivative, and converting the diagonal from Lebesgue measure to metric volume, gives
\[
 \begin{gathered}
 \mathcal C_\varepsilon(t)
 :=\gamma_\varepsilon(\Pi)^{-1}
          C_{P_\varepsilon}(t,\Pi,\Pi),\\
 \mathcal C_\varepsilon(t)=C_0(t,0)-b_0 C_0(t,2)\\
 \quad+\sum_{\nu=1}^N a_\nu C_\nu(t,0)\\
 \quad-\sum_{\nu=1}^N b_\nu C_\nu(t,2)+R_\varepsilon(t),\\
 \|R_\varepsilon\|_{C^0([-32,32])}\leq C\varepsilon.
\end{gathered}
 \tag{B128}
\]
For any fixed greater regularity of the remainder, increase \(N\). The \(\gamma_\varepsilon(y)\) in (B123) cancels exactly with the diagonal conversion \(1/\gamma_\varepsilon(\Pi)\). The coefficient of \(C_0(t,0)\) is exactly one. Restrictions at that term are the time-tested restrictions from (B119); the smooth remainder supplies the same restriction for the actual kernel. This proves both the normalization and the actual finite remainder.

<a id="temporal-distribution-bounds"></a>
## 35. Coarse temporal estimates, including the singular vertex

We require only polynomial bounds, not a stationary-phase expansion. Introduce the mass parameter \(m\geq0\):
\[
 \begin{gathered}
 C^{[m]}(t,z)\\
 =(2\pi)^{-n}\int e^{iz\cdot\xi}
                    \cos(t\sqrt{|\xi|^2+m})\,d\xi .
\end{gathered}
 \tag{B129}
\]
All integrals here are time-tested distributions. The even Taylor expansion at frequency zero and rapid decay at infinity justify every right derivative at \(m=0\), giving
\(C_\nu=(-\partial_m)^\nu C^{[m]}|_{m=0}\).
For \(|\tau|\geq1\) and \(0\leq m<1/4\), polar integration gives its time Fourier transform:
\[
 \begin{gathered}
 \mathcal F_t C^{[m]}(\tau,z)
 =\pi(2\pi)^{-n}|\tau|(\tau^2-m)^{(n-2)/2}\\
 \qquad\cdot\int_{S^{n-1}}
       e^{i\sqrt{\tau^2-m}\,z\cdot\omega}\,d\omega .
 \end{gathered}
 \tag{B130}
\]
Indeed the transform of the cosine is
\(\pi[\delta(\tau-\sqrt{r^2+m})+\delta(\tau+\sqrt{r^2+m})]\).
The radial Jacobian is \(|\tau|/r\), which, multiplied by \(r^{n-1}\), gives the displayed power. This proves every constant in (B130).

At \(|z|=2\), differentiating the amplitude and exponential any fixed number of times in \(m\) gives the bound \(C_\nu\langle\tau\rangle^{n-1}\); each derivative of the square root introduces a bounded inverse power when \(|\tau|\geq1\). At \(z=0\) and \(\nu\geq1\), the sphere integral is constant and the bound improves to
\(C_\nu\langle\tau\rangle^{n-1-2\nu}\), hence to \(C_\nu\langle\tau\rangle^{n-2}\). The part in \(|\tau|\leq2\) is a compactly supported distribution of finite order by (B119). Convolution with the Fourier transform of a compact smooth time cutoff makes that part rapidly decreasing: apply its finite-order test bound to the translated Schwartz function. Convolution of the high-frequency part with a Schwartz function preserves either of the nonnegative power bounds just given, by
\(\langle\tau-\sigma\rangle^a\leq C_a\langle\tau\rangle^a\langle\sigma\rangle^a\).

Let \(\psi\) range over a bounded set in \(C_c^\infty((-32,32))\). We obtain, for \(\kappa\geq0\),
\[
 \begin{gathered}
 \left|\left\langle C_\nu(t,2),
            \psi(t)\frac{\sin(\kappa t)}t\right\rangle\right|\\
       \leq C_\nu\kappa(1+\kappa)^{n-2},\\
 \left|\left\langle C_\nu(t,0),
            \psi(t)\frac{\sin(\kappa t)}t\right\rangle\right|\\
       \leq C_\nu\kappa(1+\kappa)^{n-2},
       \quad \nu\geq1.
\end{gathered}
 \tag{B131}
\]
For the first line insert a smooth cutoff vanishing near zero and equal to one on \(|t|\geq2\); (B120) allows this without change. Then \(\psi(t)/t\) is an ordinary compact smooth test coefficient. Its Fourier convolution is bounded by \(C(1+\kappa)^{n-1}\) for \(\kappa\geq1\), which is comparable to the stated bound. For \(0\leq\kappa\leq1\), the test function and all needed derivatives are \(O(\kappa)\); use the finite distribution order.

For the second line denote the pairing by \(J_\nu(\kappa)\). It is zero at \(\kappa=0\), and differentiation under distributional pairing gives
\(J_\nu'(\kappa)=\langle C_\nu(t,0),\psi(t)\cos(\kappa t)\rangle\).
The improved high-frequency bound just proved and its low-frequency part bound this derivative by \(C(1+\kappa)^{n-2}\). Integration from zero proves (B131). This argument works also when \(n=2\), including any point-supported terms at zero temporal frequency.

For a bounded ordinary function \(R\) on this fixed interval,
\[
 \left|\int R(t)\psi(t)
             \frac{\sin(\kappa t)}t\,dt\right|
       \leq C\|R\|_\infty\kappa.
 \tag{B132}
\]
This is simply \(|\sin(\kappa t)/t|\leq\kappa\) and the finite interval length.

<a id="reflected-arrival-comparison"></a>
## 36. The reflected-arrival part of the actual comparison

Choose an even smooth \(\chi\), equal to one on \([-16,16]\) and supported in \((-32,32)\). The physical diagonal is at distance \(d\); set \(\varepsilon=d\), \(t=du\), and \(\kappa=kd\). Unitary spatial dilation of the coordinate half densities multiplies a kernel by \(d^{-n}\). Conversion to metric volume then gives the exact distributional identity
\[
 \begin{gathered}
 C_x(du)=d^{-n}\mathcal C_d(u),\\
 C_d^0(du)=d^{-n}[C_0(u,0)-C_0(u,2)].
 \end{gathered}
 \tag{B133}
\]
These identities mean pullback under the nonzero linear time dilation; on pairing, the time Jacobian \(d\) is retained. It cancels the factor \(d\) in the denominator of \(\sin(kt)/t\).

The test coefficients \(\psi_d(u)=\chi(u)\widehat\rho(du)\) form a bounded set of compact smooth functions. Subtract the two identities in (B133), insert (B128), and use (B124), (B131), (B132). The direct leading term cancels exactly. The reflected leading coefficient differs by \(O(d)\), and all higher coefficients and the smooth error are \(O(d)\). Therefore
\[
 \begin{gathered}
 \left|\left\langle C_x-C_d^0,
       \chi(t/d)\widehat\rho(t)\frac{\sin(kt)}t
                                      \right\rangle\right|\\
 \leq C d^{1-n}\kappa(1+\kappa)^{n-2}
       =C k(k+d^{-1})^{n-2}.
 \end{gathered}
 \tag{B134}
\]
There is no lower-energy cutoff in this calculation; it bounds the complete short-time cosine distribution.

<a id="curved-remainder-comparison"></a>
## 37. The part with time much larger than distance

For \(16d\leq |t|\leq T\), put \(\varepsilon=|t|\) and \(\theta=d/|t|\leq1/16\). Let \(z_\theta=(0,\theta)\). The coordinate and density scaling used in (B133), now at time scale \(\varepsilon\), gives
\[
 C_x(t)=|t|^{-n}
    \gamma_\varepsilon(z_\theta)^{-1}
    C_{P_\varepsilon}(1,z_\theta,z_\theta).
 \tag{B135}
\]
Evenness of the cosine kernel handles negative time. Choose the physical \(T\) small enough that these scaled families fall within (T174)–(T194). The latter theorem says that the right-hand kernel at time one is smooth with every parameter, source and target derivative, uniformly for \(0\leq\theta\leq1/16\) and \(0\leq\varepsilon\leq T\).

Denote the normalized kernel in (B135) by \(F(\varepsilon,y_0,\theta)\). At \(\varepsilon=0\), the operator is the flat half-space operator throughout the domain of dependence, so the odd Fourier calculation gives
\(F(0,y_0,\theta)=C_0(1,0)-C_0(1,2\theta)\).
These are smooth values since \(1>2\theta\). At \(\theta=0\), both source and target are at the Dirichlet wall, so \(F(\varepsilon,y_0,0)=0\). The limiting source assertion follows explicitly from the boundary source limits in (T182)–(T186). Set
\(G=F-[C_0(1,0)-C_0(1,2\theta)]\).
It vanishes on both parameter axes. The twice iterated fundamental theorem of calculus gives
\[
 \begin{gathered}
 G(\varepsilon,y_0,\theta)\\
 =\int_0^\varepsilon\int_0^\theta
           \partial_a\partial_bG(a,y_0,b)\,db\,da,\\
 |C_x(t)-C_d^0(t)|\leq C d\,|t|^{-n},\\
 16d\leq|t|\leq T.
\end{gathered}
 \tag{B136}
\]
The mixed derivative is bounded by the actual kernel theorem (T194), including the zero scaling endpoint; this is where its parameter assertion is used.

Pair this smooth function with the complementary time cutoff. The two elementary inequalities \(|\sin(kt)|\leq k|t|\) and \(|\sin(kt)|\leq1\) give
\[
 \begin{gathered}
 \left|\left\langle C_x-C_d^0,
  [1-\chi(t/d)]\widehat\rho(t)\frac{\sin(kt)}t
                                      \right\rangle\right|\\
 \leq C\min\{k d^{2-n},\,d^{1-n}\}\\
 =C d^{1-n}\min\{kd,1\}\\
 \leq C k(k+d^{-1})^{n-2}.
 \end{gathered}
 \tag{B137}
\]
For example the first bound is \(Ckd\int_{16d}^T t^{-n}\,dt\), and the second is \(Cd\int_{16d}^T t^{-n-1}\,dt\). Both integrals have the stated bounds for \(n\geq2\). If \(16d\geq T\), this part is empty. Thus no small-distance or energy range is left out.

<a id="curved-spectral-estimate"></a>
## 38. Completion of the curved spectral estimate

Adding (B134) and (B137), and reinstating the harmless factor \(1/\pi\), proves (B16) for a fixed collar \(0<d\leq d_0\). The two tails in (B13) then prove (B7). The positive unsmoothing proof in Section 3 gives, for \(k\geq2\),
\[
 \begin{gathered}
 e_P(x,x;k^2)\\
       =k^n[W_n(0)-W_n(2kd(x))]+R(x,k),\\
 |R(x,k)|\leq C k^n,\\
 |R(x,k)|\leq C k(k+d(x)^{-1})^{n-2},\\
 d(x)>0.
\end{gathered}
 \tag{B138}
\]
Here the spectral density is relative to \(dV_g\), and either strict or closed endpoint convention is allowed. At the wall the density, the model and the remainder are all zero.

For use beyond the small collar, the same proof also supplies the requisite interior estimate. On the compact region \(d(x)\geq d_0\), take one fixed time smaller than the boundary distance and a uniform geodesic coordinate radius. Repeat Sections 31–34 with the ordinary endpoint map alone, without dilation. The coefficients \(u_\nu(x,x)\) and the smooth error are uniformly bounded, and \(u_0(x,x)=1\). The same source normalization cancels against metric volume. Applying the second line of (B131) and (B132) therefore bounds the smoothed difference from the bulk model \((2\pi)^{-n}\omega_n k^n\) by \(Ck^{n-1}\). The positive argument of Section 3, now with weight \((1+|k|)^{n-1}\), gives
\[
 \begin{gathered}
 \left|e_P(x,x;k^2)-W_n(0)k^n\right|
       \leq C k^{n-1},\\
 d(x)\geq d_0.
\end{gathered}
 \tag{B139}
\]
All steps in that argument remain unchanged: the bulk model has positive derivative bounded by \(Ck^{n-1}\), the fixed smoothing is positive, and the actual rough growth is (B1).

Finally \(|W_n(s)|\leq C/(1+s)\) for \(s\geq0\). For \(s\geq1\), slice the unit ball in its last coordinate. The remaining amplitude is a constant times \((1-a^2)^{(n-1)/2}\) on \([-1,1]\); it is zero at the endpoints and has integrable derivative for every \(n\geq2\). One integration by parts bounds its Fourier integral by \(C/s\). For \(s\leq1\), use the volume bound. Hence
\(k^n|W_n(2kd)|\leq C_{d_0}k^{n-1}\) when \(d\geq d_0\). Combining this with (B139) proves (B138) throughout \(X\), without assuming that the distance function is smooth outside the collar.

Estimate (B138) holds for the full scalar, smooth, formally self-adjoint, strictly positive Dirichlet operator stated at the start, including all lower-order terms. It supplies the two bounds in [the integrated remainder transfer theorem](../../src/reflection-and-the-dirichlet-boundary-coefficient.md#reflection-remainder-transfer) and the pointwise input in [Generalized rays and the Dirichlet Weyl law](../../src/generalized-rays-and-the-dirichlet-weyl-law.md).

<a id="39-source-comparison-and-proof-scope"></a>

## 39. Related spectral estimates

Victor Ivrii's freely readable [author monograph, *Microlocal Analysis, Sharp Spectral Asymptotics and Applications*](https://www.math.toronto.edu/ivrii/monsterbook.pdf), July 9, 2023 version, Section 8.1.2, printed pp. 741–749, distinguishes boundary parametrices, Tauberian comparison and coefficient freezing. Propositions 8.1.3–8.1.5 lead to Theorem 8.1.6. Section 8.1.1 identifies a tangential energy direction away from normal incidence; the pointwise complementary route uses Theorem 7.3.2 with Remark 7.3.3(v), supported by Theorem 7.2.17(i). Sections 5–30 above develop the near-normal and frozen parts of that route explicitly.

For the construction in Sections 31–38, see also Lars Hörmander, [*The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*](https://doi.org/10.1007/978-3-540-49938-1), the 2007 electronic edition. Section 17.4, printed pp. 32–40, constructs ordinary and reflected radial wave parametrices; Proposition 17.4.4 identifies their finite residual. Theorem 17.5.10, printed p. 52, is the corresponding curved spectral estimate.

The two-scale comparison uses the [joint parameter kernel theorem](diffractive-phase-neighborhoods.md#joint-kernel-parameters), including boundary source limits. The Fourier distributions and radial transports in Sections 32–34 control the reflected arrival; the uniform kernel theorem controls later times. Section 3 then removes the positive smoothing.

The near-normal and complementary frozen calculations in Sections 5–30 provide more detailed descriptions of the corresponding localized models.
