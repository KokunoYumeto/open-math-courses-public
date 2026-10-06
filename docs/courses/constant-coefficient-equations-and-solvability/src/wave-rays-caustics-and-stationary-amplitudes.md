# Wave rays, caustics, and stationary amplitudes

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

An oscillatory initial velocity launches two oppositely directed families of wave rays. Their projection can fold, so several initial points can contribute to one observation. Away from these caustics, each ray has a complete oscillatory expansion. The leading amplitude measures the spreading of the ray bundle, while its phase records the curvature centers that the ray has passed.

We use the Fourier convention stated below and the Cauchy uniqueness and finite propagation proved in [The wave Cauchy problem and Kirchhoff’s formula](flat-wave-cauchy-and-kirchhoff.md). The compact stationary-phase theorem and its symbol-amplitude corollary in [Stationary phase and critical manifolds][stationary] supply the analytic expansion for a nondegenerate critical point. We prove the compact frequency reduction, ray geometry, full coefficient normalization, and all-order realization needed to apply that theorem.

Throughout, \(O(\omega^{-\infty})\) means decay faster than every power as \(\omega\to+\infty\), locally with every prescribed derivative in the observation parameters. A classical order-zero amplitude has an expansion in nonnegative integer powers of \(\omega^{-1}\), with the corresponding differentiated symbol estimates after each finite truncation.

## Initial velocity and the two Fourier branches

Let \(n\geq2\), \(a\in C^\infty_c(\mathbb R^n)\), and let \(\phi\) be real and smooth on \(\mathbb R^n\), with \(\nabla\phi\ne0\). Put \(f_\omega=a e^{i\omega\phi}\), \(\omega\geq1\), and use
\[
\begin{gathered}
\widehat f(\xi)=\int e^{-iy\cdot\xi}f(y)\,dy,\\
f(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}\widehat f(\xi)\,d\xi .
\end{gathered}
\]
The solution with initial displacement zero and initial velocity \(f_\omega\) is
\[
u_\omega(t,x)=(2\pi)^{-n}
\int e^{ix\cdot\xi}\frac{\sin(t|\xi|)}{|\xi|}
\widehat f_\omega(\xi)\,d\xi .
\]
The quotient at zero is its smooth radial extension. Rapid decrease of \(\widehat f_\omega\), for each fixed \(\omega\), permits all \(t,x\) derivatives under the integral. Differentiation gives the wave equation and both initial traces. The full no-growth uniqueness proof in [The wave Cauchy problem and Kirchhoff’s formula](flat-wave-cauchy-and-kirchhoff.md) identifies this with the Cauchy solution. Forward and backward causal kernels in that lesson give
\(\operatorname{supp}u_\omega(t,\cdot)\subset K+\overline B(0,|t|)\), \(K=\operatorname{supp}a\).

For \(\sigma\in\{+1,-1\}\), define the two separate oscillatory integrals
\[
u^\sigma_\omega=(2\pi)^{-n}\iint
e^{i[(x-y)\cdot\xi+\sigma t|\xi|+\omega\phi(y)]}
\frac{a(y)}{2i|\xi|}\,dy\,d\xi .
\]
Their meaning is obtained by first integrating in \(y\), or equivalently by a frequency cutoff and its limit. At zero, \(|\xi|^{-1}\) is locally integrable exactly as needed for \(n\geq2\). At infinity the \(y\) integral is \(\widehat f_\omega\). Thus each branch is smooth and \(u_\omega=u^+_\omega-u^-_\omega\). The factor \(1/(2i)\) is the same in both branch integrals; the minus sign belongs to the final difference.

## Ray maps and eikonal phases

Set \(k(y)=\nabla\phi(y)\), \(\kappa(y)=|k(y)|\), \(v(y)=k(y)/\kappa(y)\). On making \(\xi=\omega\eta\), the phase is
\[
\Psi_\sigma(t,x,\eta,y)=(x-y)\cdot\eta+\sigma t|\eta|+\phi(y)
\]
and the prefactor is \(\omega^{n-1}(2\pi)^{-n}\). Critical points satisfy
\[
\eta=k(y),\qquad x=F^\sigma_t(y):=y-\sigma t v(y).
\]
For fixed \(t\), \(F^\sigma_t\) is proper: \(|F^\sigma_t(y)-y|=|t|\), so inverse images of bounded sets are bounded and inverse images of closed sets are closed. The full map
\(\mathcal F_\sigma(t,y)=(t,F^\sigma_t(y))\) is proper as well: on a compact target set both \(t\) and \(F^\sigma_t(y)\) are bounded, hence \(y\) is bounded. Its critical set is the closed set where
\[
J_\sigma(t,y)=\det(I-\sigma t Dv(y))=0 .
\]
The caustic \(\mathcal C_\sigma\) is its image. A proper map between these Euclidean spaces maps closed sets to closed sets: if image points converge, properness on their union with the limit gives a convergent preimage subsequence. Hence \(\mathcal C_\sigma\) is closed.

Off the caustic, a fiber of \(F^\sigma_t\) is compact and consists of isolated regular points. It is finite: otherwise compactness gives an accumulation point in the fiber, contrary to local injectivity at that point. The implicit function theorem gives one smooth inverse branch near each of these points. No additional branch can appear on shrinking the parameter neighborhood. Indeed, an extra sequence of solutions would have a bounded preimage subsequence by properness; its limit is one of the original regular points, where the existing inverse branch is unique. Thus the fiber cardinality is locally constant and hence constant on each connected component of the complement. On the connected slice \(t=0\), \(F^\sigma_0\) is the identity, so the component containing that entire slice has just one branch. For each fixed \(t\), the critical-image lemma below also shows that the caustic section has measure zero.

On a regular inverse branch \(y=y(t,x)\), define
\(\phi_\sigma(t,x)=\phi(y(t,x))\). Differentiating \(v\cdot v=1\) gives \(k^T Dv=0\). Therefore
\[
\begin{gathered}
dx=(I-\sigma tDv)\,dy-\sigma v\,dt,\\
d\phi=k\cdot dx+\sigma\kappa\,dt.
\end{gathered}
\]
In particular
\[
\nabla_x\phi_\sigma=k(y),\qquad
\partial_t\phi_\sigma=\sigma|\nabla_x\phi_\sigma|.
\]
Along a ray \(t\mapsto(t,y-\sigma t v(y))\), its phase is the constant \(\phi(y)\). These formulas include the orientation: the ray velocity is \(-\sigma v(y)\).

## A critical image has measure zero

Let \(g\) be \(C^1\) on a neighborhood of a compact set \(K\subset\mathbb R^n\), with values in \(\mathbb R^n\). Write \(C=\{z\in K:\det Dg(z)=0\}\). This is compact. Choose a fixed compact neighborhood of \(K\) still within the domain; there \(Dg\) is bounded by \(M\) and has a modulus of continuity \(m(\varepsilon)\to0\). Cover \(C\) by grid cubes of side \(\varepsilon\) meeting it. Their number is at most \(C_K\varepsilon^{-n}\). In each selected cube choose \(z_j\in C\).

For \(z\) in that cube and in \(C\), the line from \(z_j\) to \(z\) stays in the fixed neighborhood when \(\varepsilon\) is small. The fundamental theorem of calculus gives
\[
\begin{gathered}
g(z)=g(z_j)+Dg(z_j)(z-z_j)+r_j(z),\\
|r_j(z)|\leq\sqrt n\,\varepsilon\,m(\sqrt n\,\varepsilon).
\end{gathered}
\]
The linear image lies in a hyperplane, since \(Dg(z_j)\) has rank at most \(n-1\), and has diameter at most \(2\sqrt n M\varepsilon\). With orthogonal coordinates having that hyperplane as the first \(n-1\) directions, the image of the critical portion of the cube lies in a box with those side lengths bounded by \(C\varepsilon\) and last side length bounded by \(C\varepsilon m(\sqrt n\varepsilon)\). The \(n=1\) interpretation has zero tangential directions and the same bound. Its volume is at most \(C\varepsilon^n m(\sqrt n\varepsilon)\), with constants independent of the cube.

Summing the outer volumes bounds the outer measure of \(g(C)\) by \(C' m(\sqrt n\varepsilon)\), which tends to zero. The image is compact and measurable, so its Lebesgue measure is zero. For a noncompact domain apply this argument on a countable compact exhaustion. This is the equal-dimensional \(C^1\) result; it asserts no general low-regularity Sard theorem in different dimensions. Applied to \(F^\sigma_t\) it proves the fixed-time assertion used in the ray-map argument.

## A compact frequency reduction

Choose \(\chi\in C^\infty_c(\mathbb R^n\setminus\{0\})\), equal to one on a neighborhood of \(k(K)\). Such a cutoff exists because \(k(K)\) is compact and avoids zero. On \(y\in K\), \(\eta\in\operatorname{supp}(1-\chi)\), there is \(\delta>0\) with
\[
|k(y)-\eta|\geq\delta(1+|\eta|).
\]
For bounded \(\eta\) this follows by compactness and the excluded neighborhood; for large \(\eta\) it follows from boundedness of \(k(K)\). Consequently, on the excluded frequencies \(\xi/\omega\),
\[
|\omega k(y)-\xi|\geq\delta(\omega+|\xi|).
\]
For the \(y\)-phase \(\omega\phi(y)-y\cdot\xi\), set
\[
b(y,\omega,\xi)=\frac{\omega k(y)-\xi}{|\omega k(y)-\xi|^2},\qquad
L=\frac1i b\cdot\nabla_y .
\]
Then \(Le^{i(\omega\phi-y\cdot\xi)}=e^{i(\omega\phi-y\cdot\xi)}\). Every fixed number of \(y\) derivatives of \(b\) is \(O((\omega+|\xi|)^{-1})\), uniformly on the compact data support. To verify this, differentiate the rational expression: each differentiated \(k\) supplies \(\omega\), bounded by \(\omega+|\xi|\), and every denominator is bounded below by a fixed multiple of that quantity. Repeated formal transposition of \(L\), with compact support in \(y\), therefore gives
\[
\left|\int e^{i(\omega\phi-y\cdot\xi)}a(y)\,dy\right|
\leq C_N(\omega+|\xi|)^{-N}
\]
on the excluded region, for every \(N\). Boundary terms vanish.

Each fixed \(r\)-th derivative in \(t,x\) of the remaining unit-modulus factor is bounded by \(C_r|\xi|^r\). Thus the excluded part is bounded by a constant times
\[
\int_{\mathbb R^n}|\xi|^{-1}(\omega+|\xi|)^{-N+r}\,d\xi
=C_{N,r,n}\omega^{n-1-N+r}
\]
when \(N>n-1+r\). The integral at zero is finite because \(n\geq2\); polar coordinates and \(\xi=\omega\zeta\) prove the displayed identity. Increasing \(N\) proves rapid decrease in \(\omega\) with every prescribed \(t,x\) derivative. The bounds are uniform in all \(t,x\).

The retained branch is now an ordinary compact oscillatory integral:
\[
\begin{aligned}
u^\sigma_\omega
&=\omega^{n-1}(2\pi)^{-n}\iint
e^{i\omega\Psi_\sigma}\frac{a(y)\chi(\eta)}{2i|\eta|}\,d\eta\,dy\\
&\quad+R^\sigma_\omega,\\
R^\sigma_\omega&=O(\omega^{-\infty}).
\end{aligned}
\]
in every local \(C^r\) parameter norm. This handles both small and large excluded frequencies, rather than merely a bounded nonstationary region.

## The ray Hessian and curvature centers

At a critical point put \(B=\phi''(y)\), \(\Pi=I-vv^T\). In the ordered variables \((\eta,y)\) the Hessian is
\[
H_\sigma=
\begin{pmatrix}\sigma t\Pi/\kappa&-I\\-I&B\end{pmatrix}.
\]
For arbitrary square matrices \(A,B\),
\(\det\left(\begin{smallmatrix}A&-I\\-I&B\end{smallmatrix}\right)=\det(AB-I)\).
When \(A\) is invertible this follows by a Schur complement:
\(\det A\det(B-A^{-1})=\det(AB-I)\).
The polynomial identity extends to singular \(A\) by continuity, because invertible matrices are dense. Also \(Dv=\Pi B/\kappa\). Hence
\[
\begin{aligned}
\det H_\sigma&=(-1)^n\det(I-\sigma t\Pi B/\kappa)\\
&=(-1)^nJ_\sigma(t,y).
\end{aligned}
\]
Thus the full \(2n\)-variable critical point is nondegenerate precisely off the ray caustic.

Rotate coordinates so \(k=\kappa e_1\). Diagonalize the symmetric restriction of \(B\) to \(e_1^\perp\), with eigenvalues \(b_2,\ldots,b_n\). Its quadratic form, divided by two in the Taylor convention, is
\[
\frac12\left[\frac{\sigma t}{\kappa}|\delta\eta'|^2
-2\delta\eta\cdot\delta y+\delta y^T B\delta y\right].
\]
Replacing
\(\delta\eta_1\) by
\(\delta\eta_1-B_{11}\delta y_1/2-B_{1'}\cdot\delta y'\)
separates the normal pair \(-\delta\eta_1^{\rm new}\delta y_1\), which has one positive and one negative eigenvalue. Each tangential pair has symmetric matrix
\[
\begin{pmatrix}\sigma t/\kappa&-1\\-1&b_j\end{pmatrix}.
\]
If its determinant \(\sigma t b_j/\kappa-1\) is negative, its signature is zero. If positive, \(\sigma t/\kappa\) and \(b_j\) have the same sign, and the trace has that sign; both eigenvalues therefore have sign \(\operatorname{sgn}(\sigma t)\). At a regular point, defining
\[
N_\sigma(t,y)=\#\{j\geq2:\sigma t b_j/\kappa>1\}
\]
with multiplicity gives
\(\operatorname{sgn}H_\sigma=2N_\sigma\operatorname{sgn}(\sigma t)\).
At \(t=0\) the signature is zero and \(N_\sigma=0\).

To interpret this count geometrically, translate \(y\) to zero. The level surface \(\phi=\phi(0)\) is a graph
\[
y_1=-\sum_{j=2}^n\frac{b_j}{2\kappa}y_j^2+O(|y'|^3).
\]
With unit normal \(v\) and Weingarten map \(-d v\), its signed principal curvature in direction \(e_j\) is \(-b_j/\kappa\). If \(b_j\ne0\), the signed radius is \(-\kappa/b_j\) and the curvature center is \(y-\kappa v/b_j\). The ray \(y-\sigma t v\) reaches it at \(t_j=\sigma\kappa/b_j\). The inequality in the definition of \(N_\sigma\) is exactly that this \(t_j\) lies strictly between \(0\) and \(t\), including negative \(t\). Directions with \(b_j=0\) have infinite radius and contribute nothing. Repeated eigenvalues count their multiplicity.

## The complete expansion and beam conservation

Work on a sufficiently small compact parameter neighborhood avoiding \(\mathcal C_\sigma\). The ray-map argument gives finitely many smooth inverse branches; properness excludes new ones. Choose disjoint cutoffs around their critical points, fixed in smooth branch coordinates. Any critical branch lying outside \(K\) has zero amplitude. The compact integration region away from all these neighborhoods has phase gradient bounded below uniformly, hence integration by parts gives \(O(\omega^{-\infty})\) there. All finite parameter derivatives have the same assertion after increasing the number of integrations.

Apply the compact stationary-phase theorem in [Stationary phase and critical manifolds][stationary] to each compact critical neighborhood in dimension \(2n\). Its hypotheses hold: the Hessian is invertible by the Hessian calculation, varies smoothly, and has bounded inverse on the compact parameter neighborhood; the support is compact and the other-region gradient bound was just proved. Its critical value is
\[
\Psi_\sigma(t,x,k(y),y)=\phi(y),
\]
since \((x-y)\cdot k+\sigma t\kappa=0\). The stationary prefactor \((2\pi/\omega)^n\), multiplied by the prefactor in the frequency-cutoff argument, is exactly \(\omega^{-1}\). For this display put \(\Phi_\ell=\phi_{\sigma,\ell}(t,x)\). Thus, for each \(M\),
\[
\begin{gathered}
S_{\ell,M}=\sum_{j<M}\omega^{-j}A_{\sigma,\ell,j}(t,x),\\
B_{\ell,M}=S_{\ell,M}+\mathcal R_{\sigma,\ell,M}(t,x,\omega),\\
u^\sigma_\omega(t,x)=
\omega^{-1}\sum_\ell e^{i\omega\Phi_\ell}B_{\ell,M}
+O(\omega^{-\infty}).
\end{gathered}
\]
After the displayed critical oscillation is removed, every prescribed parameter derivative of \(\mathcal R_{\sigma,\ell,M}\) is \(O(\omega^{-M})\). The symbol-amplitude corollary supplies the normalized \(\omega\)-symbol derivatives and the corresponding statement for classical input symbols. We do not differentiate a removed oscillatory factor as if it were bounded in all parameter derivatives.

The leading coefficient is
\[
\begin{aligned}
A_{\sigma,\ell,0}
&=\frac{a(y)}{2i\kappa(y)}
|J_\sigma(t,y)|^{-1/2}e^{i\pi\operatorname{sgn}H_\sigma/4}\\
&=\frac{a(y)}{2i\kappa(y)}
|J_\sigma(t,y)|^{-1/2}
i^{\,N_\sigma(t,y)\operatorname{sgn}(\sigma t)} .
\end{aligned}
\]
There is no additional \(\sigma\) multiplying this amplitude: \(u^+-u^-\) already records the original sine split. At \(t=0\), both branches have the same leading coefficient and cancel, as the exact initial displacement requires.

For completeness, the formal coefficient series can be realized by actual order-zero symbols locally in the parameters. Let \(K_\ell\) be a compact exhaustion of the parameter neighborhood and let \(\theta\) be smooth, zero for arguments at most one and one for arguments at least two. Choose numbers \(R_j\to\infty\) so fast that all seminorms involving \(K_\ell\), parameter derivative order \(r\), \(\omega\) derivative order \(k\), and target order \(-N\), for \(\ell,r,k,N\leq j/2\), of
\[
\omega^{-j}\theta(\omega/R_j)A_j
\]
are at most \(2^{-j}\). This is possible: on its support \(\omega\geq R_j\), differentiated terms are bounded by constants times \(\omega^{-j-k}\); the target weight \(\omega^{N+k}\) leaves a factor \(R_j^{N-j}\to0\) since \(N\leq j/2\). Define \(A_\omega\) as the sum of these terms, treating \(j=0\) separately as \(A_0\). On each bounded \(\omega\) interval only finitely many summands are nonzero. Thus the sum is smooth.

For any fixed \(N,k,r,K_\ell\), the tail with sufficiently large \(j\) is bounded by the geometric majorant in order \(-N-k\); the finitely many terms with \(j\geq N\) left over have that same order directly. For the first \(N\) terms, each cutoff differs from one only on a bounded \(\omega\) interval. Therefore
\[
A_\omega-\sum_{j<N}\omega^{-j}A_j\in S^{-N}
\]
with all local parameter seminorms. This proves the asserted full classical realization, rather than assuming convergence of a formal series.

Replace each finite expansion by its realization. To estimate \(r\) derivatives of the full, unnormalized remainder to order \(\omega^{-L}\), choose the stationary expansion with \(M>L+r+1\); the derivatives of \(e^{i\omega\phi_{\sigma,\ell}}\) cost at most \(\omega^r\). Hence
\[
u^\sigma_\omega=\omega^{-1}\sum_\ell
e^{i\omega\phi_{\sigma,\ell}}A_{\sigma,\ell,\omega}
+O(\omega^{-\infty})
\]
in every local \(C^r\) norm away from the caustic.

The geometric conservation law follows without a separate transport argument:
\[
|A_{\sigma,\ell,0}(t,x)|^2|J_\sigma(t,y)|
=\frac{|a(y)|^2}{4\kappa(y)^2}.
\]
Along the ray, the right side is constant. The absolute Jacobian measures the cross section of the infinitesimal ray bundle. When a simple curvature center is crossed in the oriented direction along the ray, the signature factor changes by \(i\) or \(-i\), a phase change of magnitude \(\pi/2\). The divergence of this formula as \(J_\sigma\to0\) is failure of the nondegenerate expansion, not a blowup claim for the exact smooth wave solution.

## Exercises with complete solutions

**Exercise 1 (introductory: keep the sine sign).** Let \(k_0\ne0\). Solve the wave Cauchy problem with zero initial displacement and initial velocity \(e^{i\omega k_0\cdot x}\). This datum is not compactly supported, so check the solution directly. Write it as the difference of two branches and identify their two amplitudes.

**Solution.** Direct differentiation gives
\[
u_\omega(t,x)=e^{i\omega k_0\cdot x}
\frac{\sin(\omega t|k_0|)}{\omega|k_0|}.
\]
It solves \(\partial_t^2u-\Delta u=0\), is zero at \(t=0\), and has the prescribed first derivative. Uniqueness without a growth condition makes it the solution. Its two terms are
\[
\frac{e^{i\omega(k_0\cdot x+t|k_0|)}}{2i\omega|k_0|}
-\frac{e^{i\omega(k_0\cdot x-t|k_0|)}}{2i\omega|k_0|}.
\]
Both branch amplitudes are \(1/(2i|k_0|)\); their difference gives the sine. Putting an additional minus sign into the second amplitude would give a cosine and violate the zero displacement.

**Exercise 2 (introductory: a parallel ray family).** Take \(\phi(y)=k_0\cdot y+d\) and compact smooth \(a\). Find both ray maps, their phases and Jacobians. Give the leading oscillatory solution.

**Solution.** Put \(v_0=k_0/|k_0|\). Since \(Dv_0=0\),
\[
\begin{gathered}
F^\sigma_t(y)=y-\sigma t v_0,\\
y=x+\sigma t v_0,\qquad J_\sigma=1 .
\end{gathered}
\]
There are no caustics. The phase is
\(\phi_\sigma=k_0\cdot x+d+\sigma t|k_0|\), and the curvature count is zero. Hence
\[
\begin{gathered}
T_\sigma=a(x+\sigma tv_0)e^{i\omega\phi_\sigma(t,x)},\\
u_\omega(t,x)=\frac{T_+-T_-}{2i\omega|k_0|}
+O(\omega^{-2}).
\end{gathered}
\]
locally. The error displayed is the undifferentiated first-truncation error; the full theorem gives complete classical amplitudes and the normalized derivative estimates. For general \(a\), the displayed leading terms alone are not the exact solution.

**Exercise 3 (intermediate: a critical image and two sheets).** For \(g(s,r)=(s,r^2)\), compute the critical set and its image. Count the fibers above points \((S,R)\) on each side of the critical image. Explain why a null critical image does not imply uniqueness of the regular fiber.

**Solution.** The derivative is \(\operatorname{diag}(1,2r)\), so the critical set is \(r=0\), with image the line \(R=0\). That line has two-dimensional measure zero. For \(R>0\), the two preimages are \((S,\sqrt R)\) and \((S,-\sqrt R)\); for \(R<0\), there are none. At \(R=0\) there is one critical preimage. Each regular complementary component has a fixed fiber count, but the count need not be one. For the wave ray map the identity at \(t=0\), rather than the measure-zero statement alone, supplies the one-branch component.

**Exercise 4 (intermediate: the normal block does not change the signature).** At a stationary point in dimension three, let \(\kappa=2\), \(\sigma=+1\), and
\[
B=\begin{pmatrix}7&2&-1\\2&-4&0\\-1&0&1\end{pmatrix}.
\]
For \(t=3\) and \(t=-3\), find the curvature count, full Hessian signature, and ray Jacobian. Explain the role of the mixed entries \(2,-1\).

**Solution.** The tangent eigenvalues are \(-4,1\). For \(t=3\), the two ratios \(tb_j/\kappa\) are \(-6,3/2\), so \(N=1\), the signature is \(2\), and
\[
J=(1+6)(1-3/2)=-7/2.
\]
For \(t=-3\), the ratios are \(6,-3/2\), so again \(N=1\), but the signature is \(-2\), and
\[
J=(1-6)(1+3/2)=-25/2.
\]
The normal-pair change of variables removes the mixed entries from the quadratic signature calculation. That pair has signature zero. Thus these entries affect the full Hessian matrix but neither this determinant factorization nor its signature count. They will matter in the cubic contact at a fold.

**Exercise 5 (advanced: regularity of an oscillatory remainder).** Suppose one normalized amplitude remainder and all its parameter derivatives through order \(r\) are \(O(\omega^{-M})\), and its contribution to the solution is
\(\omega^{-1}e^{i\omega\Phi(p)}R_M(p,\omega)\). Find a sufficient relation between \(M,r,L\) to make its full \(C^r\) norm \(O(\omega^{-L})\). Apply it with \(r=2,L=5\).

**Solution.** Each derivative of the oscillatory factor costs at most one power of \(\omega\), on a compact parameter set. The product rule therefore bounds the full \(C^r\) norm by
\[
C\omega^{-M-1+r}.
\]
It is sufficient that \(M\geq L+r-1\). For \(r=2,L=5\), take \(M\geq6\). Bounds for the normalized amplitude do not justify ignoring these phase derivatives. Increasing the truncation order gives rapid decay with any fixed number of derivatives.

**Exercise 6 (advanced: separate a simple center from a fold).** In two dimensions take
\(\phi(y_1,y_2)=y_1+\beta y_2^2/2\), \(\beta>0\). At \(y=0\), find the first positive-time curvature center for the \(+\) branch. Show that its Hessian has a one-dimensional kernel but its kernel cubic vanishes. Expand the second component of the ray map at that time.

**Solution.** At zero, \(\kappa=1\), the tangent Hessian is \(\beta\), and the center is \(x=(-1/\beta,0)\) at \(t=1/\beta\). There is exactly one vanishing tangential Hessian block, so the full Hessian has corank one. But the mixed normal derivative and the pure tangent third derivative both vanish, so the kernel cubic is zero. Writing \(s=y_2\),
\[
F^+_{1/\beta,2}(y)
=s-\frac{s}{\sqrt{1+\beta^2s^2}}
=\frac{\beta^2}{2}s^3+O(s^5).
\]
There is no nonzero quadratic folding term. The simple curvature-center condition by itself does not justify a cubic Airy approximation; the next lesson requires the additional nonzero kernel cubic.

## References

[stationary]: ../prerequisites/stationary-phase-and-critical-manifolds.html

[stationary] *Stationary phase and critical manifolds*, Theorem 5.1 and Corollary 6.1: compact stationary phase with smooth parameters and symbol amplitudes.

M. Riesz, *L'intégrale de Riemann-Liouville et le problème de Cauchy pour l'équation des ondes*, Bulletin de la Société Mathématique de France 67 (1939), 153–170, [primary paper](https://www.numdam.org/article/BSMF_1939__67__S153_0.pdf), for the wave Cauchy integral underlying the preceding lesson.
