# Fourier transforms, finite spectra and convex separation

The Gaussian estimates in [Quantitative estimates for quadratic Fourier multipliers](gauss-transform-estimates.md) use a precise Fourier convention, a real spectral theorem, and finite-dimensional convex separation. This chapter proves those facts with their constants and endpoint cases. [Metric and topological foundations](metric-foundation-bridges.md) supplies the measure and compactness background. Basic references are [Melrose] for Fourier analysis and [Beezer] for finite-dimensional linear algebra, but the arguments below do not require either book.

Section 13 of [Metric and topological foundations](metric-foundation-bridges.md#original-scalar-calculus-and-its-finite-coordinate-receivers) proves the full original scalar and finite-coordinate calculus. Its Section 13.12 gives the exact Gaussian, Rayleigh, logarithmic-contour, matrix and half-line receiving maps, retaining every original factor, endpoint and norm.

The complete original real-number, compactness, extrema and finite-norm proofs are in Section 12 of [Metric and topological foundations](metric-foundation-bridges.md#real-numbers-and-finite-dimensional-topology). Its Section 12.10 gives the exact receiving minimum and spectral-contour maps; the original coordinates, norms and constants are retained.

We assume multivariable differentiation and Taylor's formula, smooth compact cutoffs, change of variables and Fubini for absolutely integrable functions, dominated convergence and differentiation, Cauchy–Schwarz, finite-dimensional compactness, and completeness of the real numbers. We also use elementary matrix algebra, determinants, Gram–Schmidt, and the usual monomial Schwartz seminorms. The complete finite basis, Gram, matrix and adjoint proofs are given in Section 10 of [Polynomial and contour interfaces for stable boundary models](stable-prerequisite-bridges.md#full-finite-linear-algebra-foundations). Each further step is proved here.

## 1. Fourier inversion on the Schwartz space

For \(d\geq1\), let \(\mathcal S(\mathbb R^d)\) have the seminorms
\[
p_{\alpha,\beta}(f)=\sup_x|x^\alpha\partial^\beta f(x)|.
\]
Use \(D_j=-i\partial_j\) and
\[
Ff(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx,
\qquad
Gv(x)=(2\pi)^{-d}\int e^{ix\cdot\xi}v(\xi)\,d\xi.
\]
**Theorem 1.1 (Fourier inversion).** The map \(F\) is a continuous automorphism of the Schwartz space with inverse \(G\), and
\[
F(D_jf)=\xi_jFf,\qquad F(x_jf)=i\partial_{\xi_j}Ff.
\]
For the complex-linear distribution convention, \(\langle Fu,\phi\rangle=\langle u,F\phi\rangle\); transposition of the continuous Schwartz maps supplies the transform on \(\mathcal S'\), its inverse with the corresponding factor, and the differentiated identities. This convention agrees with the integral for regular distributions induced by Schwartz functions, by Fubini.

**Proof of Theorem 1.1.** Differentiation under the integral and integration by parts give the displayed identities. More precisely, \(\xi^\alpha\partial_\xi^\beta Ff(\xi)=F[D^\alpha((-ix)^\beta f)](\xi)\). By the finite Leibniz rule, \(D^\alpha((-ix)^\beta f)\) is a finite linear combination of derivatives of \(x^\beta f(x)\), with each coefficient fixed by \(\alpha,\beta\). Its Fourier transform is bounded in supremum norm by the \(L^1\) norm of that full expression. If \(N>d\), then
\[
\|h\|_1\leq\left(\int_{\mathbb R^d}\langle x\rangle^{-N}\,dx\right)
\sup_x\langle x\rangle^N|h(x)|,
\]
so finitely many Schwartz seminorms bound each output seminorm. Thus \(F:\mathcal S\to\mathcal S\) is continuous.

For \(\varepsilon>0\), put
\[
k_\varepsilon(x)=(4\pi\varepsilon)^{-d/2}e^{-|x|^2/(4\varepsilon)}.
\]
The one-dimensional Gaussian integral is \(\int_{\mathbb R}e^{-t^2}\,dt=\sqrt{\pi}\): square the integral, use Fubini, and in \(\mathbb R^2\) make the polar change of variables with Jacobian \(r\), obtaining \(2\pi\int_0^\infty e^{-r^2}r\,dr=\pi\). Hence \(\int k_\varepsilon=1\). Let
\[
I_\varepsilon(x)=\int_{\mathbb R^d}e^{ix\cdot\xi}e^{-\varepsilon|\xi|^2}\,d\xi.
\]
Integration of a total \(\xi_j\)-derivative gives
\[
0=ix_jI_\varepsilon(x)-2\varepsilon
\int_{\mathbb R^d}\xi_j e^{ix\cdot\xi}e^{-\varepsilon|\xi|^2}\,d\xi,
\qquad
\partial_{x_j}I_\varepsilon(x)=-\frac{x_j}{2\varepsilon}I_\varepsilon(x).
\]
Its value at zero is \((\pi/\varepsilon)^{d/2}\). Solving these coordinate equations yields the exact inverse-Gaussian identity
\[
(2\pi)^{-d}I_\varepsilon(x)=k_\varepsilon(x).
\]

For \(f\in\mathcal S\), Fubini is legitimate after inserting \(e^{-\varepsilon|\xi|^2}\). It gives
\[
(2\pi)^{-d}\int e^{ix\cdot\xi}e^{-\varepsilon|\xi|^2}Ff(\xi)\,d\xi
=\int_{\mathbb R^d}k_\varepsilon(x-y)f(y)\,dy.
\]
On the left, dominated convergence gives \(GFf(x)\), since \(Ff\in L^1\). On the right, write the difference from \(f(x)\) as \(\int k_\varepsilon(y)(f(x-y)-f(x))\,dy\). On \(|y|<\delta\), the mean-value formula bounds the difference by \(\|\nabla f\|_\infty\delta\). On its complement, boundedness of \(f\) gives at most \(2\|f\|_\infty\) times the Gaussian mass \(\int_{|y|\geq\delta}k_\varepsilon(y)\,dy=\pi^{-d/2}\int_{|z|\geq\delta/(2\sqrt{\varepsilon})}e^{-|z|^2}\,dz\), which tends to zero for fixed \(\delta>0\). First let \(\varepsilon\downarrow0\), then \(\delta\downarrow0\). Thus the right side tends to \(f(x)\), uniformly in \(x\). Hence \(GF=I\) on \(\mathcal S\). The calculation of the other inverse follows below without changing any Fourier factor. ∎

Here is the two-sided inverse bridge. Define \(Rf(x)=f(-x)\) and \(a=(2\pi)^{-d}\). A change of variables gives \(FR=RF\), and the candidate inverse is \(G=aRF\). The proof above gives \(GF=I\). Therefore
\[
FG=aFRF=aRF^2=GF=I.
\]
Reflection preserves the monomial seminorms, so \(G\) is continuous. No equivalence with an unstated alternative topology is required. In dimension zero the integral convention is the identity on \(\mathbb C\); this includes that harmless endpoint whenever a zero-dimensional factor occurs.

## 2. Plancherel and integer Sobolev weights

**Theorem 2.1 (Plancherel on Schwartz functions).** For \(u\in\mathcal S(\mathbb R^d)\),
\[
\|Fu\|_2^2=(2\pi)^d\|u\|_2^2.
\]
For \(f,g\in\mathcal S\), substitute \(g=GFg\) from Theorem 1.1 into \(\int f\overline g\). Fubini is valid because \(f\) and \(Fg\) are integrable. The inner integral is \(Ff\), so \(\int f\overline g=(2\pi)^{-d}\int Ff\,\overline{Fg}\). Taking \(g=f\) proves the displayed identity, including its full factor. No extension to arbitrary \(L^2\) functions is needed here.

For every integer \(s\geq0\), the multinomial identity and differentiation under \(F\) give the more precise formula
\[
\|\langle\xi\rangle^s Fu\|_2^2
=(2\pi)^d\sum_{|\alpha|\leq s}
\frac{s!}{(s-|\alpha|)!\,\alpha!}\|D^\alpha u\|_2^2.
\]
Indeed expand \((1+\xi_1^2+\cdots+\xi_d^2)^s\), multiply by \(|Fu|^2\), integrate the finite sum and apply Theorem 2.1 to each derivative. All coefficients are positive, so this also proves both norm comparisons, with constants depending only on \(d,s\). For \(s=0\) the sum has one term.

When \(s>d/2\), Cauchy–Schwarz yields
\[
\|Fu\|_1\leq
\|\langle\xi\rangle^{-s}\|_2
\|\langle\xi\rangle^sFu\|_2.
\]
The first norm is finite: the integral inside the unit ball is bounded; the annulus \(2^k\leq|\xi|<2^{k+1}\) contributes at most a constant times \(2^{k(d-2s)}\), whose sum converges. This is the precise integer-derivative control used in the local multiplier estimate.

## 3. Real spectral decomposition

**Theorem 3.1 (Real spectral decomposition).** Every self-adjoint endomorphism of a finite-dimensional real inner-product space has a real orthonormal eigenbasis, including repeated and zero eigenvalues.

**Proof.** In dimension zero the empty basis suffices. Otherwise maximize \(\langle Av,v\rangle\) over the compact unit sphere, and call a maximizer \(v\). For each \(w\perp v\), differentiate \(\langle A(v+tw),v+tw\rangle/\langle v+tw,v+tw\rangle\) at \(t=0\). Its derivative vanishes, so \(\langle Av,w\rangle=0\); hence \(Av=\lambda v\) for \(\lambda=\langle Av,v\rangle\). Self-adjointness makes \(v^\perp\) invariant, since \(\langle Aw,v\rangle=\langle w,Av\rangle=0\) for \(w\perp v\). Induction on dimension gives an orthonormal eigenbasis of \(v^\perp\). Together with \(v\) it gives the asserted basis, with no distinct-eigenvalue assumption. ∎

The complexification gives a second check of the real eigenspaces.

In dimension zero take the empty basis. Otherwise use Gram–Schmidt to choose real orthonormal coordinates. The real symmetric matrix \(A\), regarded as a complex matrix, is Hermitian. The real basis just proved complexifies to an eigenbasis of \(\mathbb C^d\), and every eigenvalue remains real. For real \(\lambda\), taking real and imaginary parts proves
\[
\ker_{\mathbb C}(A-\lambda I)
=\ker_{\mathbb R}(A-\lambda I)
 +i\ker_{\mathbb R}(A-\lambda I).
\]
Decompose a real vector into complex eigenvectors and take real parts. Thus the real eigenspaces span \(\mathbb R^d\). If \(Av=\lambda v\) and \(Aw=\mu w\), symmetry gives
\[
(\lambda-\mu)\langle v,w\rangle
=\langle Av,w\rangle-\langle v,Aw\rangle=0.
\]
Distinct eigenspaces are orthogonal. Choosing an orthonormal basis in each gives the required real basis, with all multiplicities retained.

The following triangular-matrix facts retain the zero-dimensional case and the order of multiplication. Its induction includes dimension zero with the empty matrix. Products of upper triangular matrices are upper triangular: when \(i>j\), in each term \(a_{ik}b_{kj}\), either \(k<i\) or \(k\geq i>j\), so one factor vanishes. An invertible upper triangular matrix preserves every coordinate flag space \(E_j\); its restriction to that finite-dimensional space is injective and therefore onto. Its inverse preserves the same flag and is upper triangular. The diagonal equation in \(AA^{-1}=I\) gives \((A^{-1})_{jj}=a_{jj}^{-1}\).

## 4. Strict separation of an open convex set

**Theorem 4.1 (Strict separation).** Let \(V\) be a finite-dimensional real vector space, let \(C\subset V\) be nonempty, open and convex, and let \(x\notin C\). There is a nonzero real covector \(\eta\) such that
\[
\eta(y)<\eta(x)\quad(y\in C),
\qquad \sup_{y\in C}\eta(y)\leq\eta(x).
\]
The second inequality includes \(x\) on the boundary. The supremum need not be attained. The proof uses only finite-dimensional compactness and the inner product.

Choose an auxiliary Euclidean norm, put \(K=\overline C\), and fix \(c\in C\) with \(B(c,r)\subset C\), \(r>0\). First, if \(z\in K\) and \(0\leq t<1\), then
\[
(1-t)c+tz\in C.
\]
For \(t=0\) this is immediate. For \(0<t<1\), choose \(z_j\in C\) tending to \(z\). Convexity gives a ball of radius \((1-t)r\) centered at \((1-t)c+tz_j\) inside \(C\). For sufficiently large \(j\), this ball contains \((1-t)c+tz\), proving the assertion.

For \(\varepsilon>0\), put \(z_\varepsilon=x+\varepsilon(x-c)\). This point lies outside \(K\): if it lay in \(K\), then
\[
x=\frac{\varepsilon}{1+\varepsilon}c
 +\frac{1}{1+\varepsilon}z_\varepsilon
\]
would lie in \(C\) by the preceding assertion. The nonempty closed set \(K\) has a point \(q_\varepsilon\) nearest to \(z_\varepsilon\). To see existence without a compactness assumption on \(K\), take a minimizing sequence. Its distance to \(z_\varepsilon\) is bounded, so it has a convergent subsequence in finite dimensions; closedness places its limit in \(K\).

Write \(v_\varepsilon=z_\varepsilon-q_\varepsilon\ne0\). For \(y\in K\), the segment \(q_\varepsilon+t(y-q_\varepsilon)\), \(0\leq t\leq1\), lies in \(K\). Differentiating the squared distance at its minimum \(t=0\) gives
\[
\langle v_\varepsilon,y-q_\varepsilon\rangle\leq0.
\]
Consequently, for \(u_\varepsilon=v_\varepsilon/|v_\varepsilon|\),
\[
\langle u_\varepsilon,y\rangle
\leq\langle u_\varepsilon,z_\varepsilon\rangle
-|v_\varepsilon|
\leq\langle u_\varepsilon,z_\varepsilon\rangle.
\]
Choose \(\varepsilon=1/k\) and a convergent subsequence of the unit vectors, with limit \(u\), \(|u|=1\). Since \(z_\varepsilon\to x\), the last inequality implies \(\langle u,y\rangle\leq\langle u,x\rangle\) for every \(y\in K\). The same subsequence works for every \(y\): it was selected using only the unit vectors, and the inequality holds for every \(y\) at every index.

Set \(\eta(y)=\langle u,y\rangle\). It is nonzero. For \(y\in C\), openness gives \(y+\delta u\in C\) for some \(\delta>0\), whence
\[
\eta(y)+\delta\leq\eta(x).
\]
This proves strict pointwise separation. The supremum statement follows because \(\eta(C)\) is nonempty and bounded above. In dimension zero the hypotheses cannot occur, since the only nonempty open set is all of \(V\).

## 5. Support functions of Minkowski sums

**Proposition 5.1.** For nonempty \(A,B\subset V\), put
\[
h_A(\eta)=\sup_{a\in A}\eta(a)\in\mathbb R\cup\{+\infty\}.
\]
Then \(h_{A+B}(\eta)=h_A(\eta)+h_B(\eta)\), where \(A+B=\{a+b:a\in A,b\in B\}\). Nonemptiness excludes \(-\infty\), so the right side is unambiguous.

Linearity first gives the inequality \(\leq\). If both right-hand suprema are finite, choose \(a,b\) within \(\varepsilon/2\) of the two suprema. Their sum gives the reverse inequality up to \(\varepsilon\); let \(\varepsilon\downarrow0\). If \(h_A(\eta)=+\infty\), fix \(b_0\in B\). The values \(\eta(a+b_0)\) are unbounded above, so \(h_{A+B}(\eta)=+\infty\). Interchange \(A,B\) for the other case. No boundedness, compactness or convexity is needed for this identity.

## 6. Phase checks and exercises

The exact Fourier phases used above can be checked without changing conventions: the segment integral in the fundamental theorem runs from \(0\) to \(1\); frequency continuity compares \(e^{-ix\cdot\xi}-e^{-ix\cdot\xi'}\); the squared one-dimensional Gaussian integral is an integral over \(\mathbb R^2\); Parseval uses the conjugate transform of \(\psi\) as its second factor; and an \(H^m\) condition uses \(\langle\xi\rangle^{m}Fu\in L^2\). These checks preserve the signs and the factor \((2\pi)^{-d}\) in Theorems 1.1 and 2.1.

Exercise. For the open strip \(C=\{(a,b)\in\mathbb R^2:|a|<2\}\) and boundary point \(x=(2,7)\), determine all separating covectors satisfying the strict inequality in Theorem 4.1. Explain why the support value need not be attained and why its finiteness constrains the covector.

Solution. Write \(\eta(a,b)=\alpha a+\beta b\). Since \(b\) is unrestricted, finite upper support forces \(\beta=0\). Nonzero separation at the right boundary then forces \(\alpha>0\), and every such \(\alpha\) works: \(\alpha a<2\alpha=\eta(x)\). The support equals \(2\alpha\) but is not attained because \(a=2\) is excluded. This distinguishes strict pointwise separation from a positive uniform gap at a boundary point.

**Exercise 6.2 (A Gaussian transform).** For \(t>0\) and \(f_t(x)=e^{-t|x|^2}\) on \(\mathbb R^d\), compute \(Ff_t(\xi)\) with the exact convention of Section 1.

**Solution.** Apply the Gaussian identity from the proof of Theorem 1.1 after exchanging the roles of \(x\) and \(\xi\). Equivalently, the same integration-by-parts equation gives \(\partial_{\xi_j}Ff_t=-\xi_jFf_t/(2t)\), while \(Ff_t(0)=(\pi/t)^{d/2}\). Hence
\[
Ff_t(\xi)=(\pi/t)^{d/2}e^{-|\xi|^2/(4t)}.
\]
The positive value at zero fixes the constant and the negative exponent fixes the phase.

The polar and Gaussian integrations in Section 1 are proved in Sections 15.6–15.7 of [Banach estimates, quotient spaces and compact parameter arguments](banach-foundation-bridges.md#the-full-polar-formula-on-the-original-plane). These proofs include completed measurability, both determinant terms, the radial endpoints and the full Fourier heat-kernel factors.

## 7. Fourier transforms on the complete \(L^2\) space

The Schwartz identities above extend to the original completed Lebesgue \(L^2(\mathbb R^d)\), with both Fourier factors unchanged. The measure, density, translation and completeness proofs used here are Sections 15.0–15.4 of [Banach estimates, quotient spaces and compact parameter arguments](banach-foundation-bridges.md). We use their original measure and scalar field.

### 7.1. Constructing both inverse maps

Suppose first that \(d\geq1\). Compact smooth functions are dense in \(L^2\), by the truncation and mollification proof there, and belong to the Schwartz space. For \(f\in L^2\), choose Schwartz \(f_j\to f\) in \(L^2\). Theorem 2.1 gives the exact difference identity
\[
 \|Ff_j-Ff_k\|_2=(2\pi)^{d/2}\|f_j-f_k\|_2.
                                                               \tag{FL1}
\]
Completeness makes this a convergent sequence. If \(\widetilde f_j\to f\) is another such sequence, its difference from \(f_j\) tends to zero in \(L^2\), so (FL1) gives the same output. Define \(Ff\) as that limit. Linearity follows by approximating each summand and taking limits; the norm identity follows from continuity of the norm.

For Schwartz \(h\), Theorem 1.1 gives \(F(Gh)=h\), and Theorem 2.1 applied to \(Gh\) gives \(\|Gh\|_2=(2\pi)^{-d/2}\|h\|_2\). Thus the same construction extends \(G\) to \(L^2\). Applying continuity to \(GFf_j=f_j\) and \(FGh_j=h_j\) proves, on the original entire spaces,
\[
 \begin{split}
 F,G&:L^2(\mathbb R^d)\longrightarrow L^2(\mathbb R^d),\\
 GF&=I,\qquad FG=I,\\
 \|Ff\|_2&=(2\pi)^{d/2}\|f\|_2,\qquad
 \|Gh\|_2=(2\pi)^{-d/2}\|h\|_2 .
 \end{split}                                                   \tag{FL2}
\]
These are bijections with their original norms. In dimension zero the measure is the point mass on the one point \(\mathbb R^0\), the space is \(\mathbb C\), and both maps are the identity with \((2\pi)^0=1\). No assertion that this point is null is used in that case.

### 7.2. Ordinary integrals and simultaneous approximation

For any finite exponents \(a,c\geq1\) and \(f\in L^a\cap L^c\), put
\(f_j=1_{\{|x|_\infty\leq j,\ |f(x)|\leq j\}}f\).
Dominated convergence of \(|f|^a\) and \(|f|^c\) proves convergence in both original norms. Each \(f_j\) is bounded and supported in its displayed coordinate cube. Fix the compact smooth nonnegative approximate identity \(\rho\), with \(\int\rho=1\), from Section 15.4 of the linked chapter. For
\(\rho_\varepsilon(x)=\varepsilon^{-d}\rho(x/\varepsilon)\), the following norm-integral estimate follows from the scalar proof below:
\[
 \|\rho_\varepsilon*f_j-f_j\|_t
 \leq\int|\rho(z)|\,\|f_j(\,\cdot-\varepsilon z)-f_j\|_t\,dz
 \longrightarrow0,\qquad t=a,c.                                \tag{FL3}
\]
The completed-measure substitutions and Tonelli argument are proved in [Section 15.1](../banach-foundation-bridges.html#convergence-product-integration-and-the-full-linear-jacobian), the scalar Hölder inequality in [Section 15.2](../banach-foundation-bridges.html#holder-minkowski-and-all-young-endpoints), and translation continuity in [Section 15.3](../banach-foundation-bridges.html#completeness-and-compact-smooth-density). The original scaling identity is (LP13) in [Section 15.4](../banach-foundation-bridges.html#the-original-scaled-approximate-identity).

**The full integral triangle estimate in (FL3).** Fix an original finite exponent \(t\geq1\), the actual \(f_j\), and \(\varepsilon>0\). Put \(h_z(x)=f_j(x-\varepsilon z)-f_j(x)\) and \(M_\varepsilon(x)=\int|\rho(z)||h_z(x)|\,dz\). These are the original translated differences and their nonnegative integral envelope. The joint integrand is measurable for completed Lebesgue measure: first take a Borel representative of the given \(f_j\) class. Its coordinate compositions are Borel. Changing that representative on a null set \(N\) changes the composed functions only on the inverse images of \(N\times\mathbb R^d\) under the identity product map and the invertible shear \((x,z)\mapsto(x-\varepsilon z,z)\). Its inverse is \((w,z)\mapsto(w+\varepsilon z,z)\), its full block determinant is one, and completed product integration and affine substitution make both inverse images null. Thus the calculation respects the original completed classes. For each fixed \(x\), the section in \(z\) is also measurable by the invertible affine substitution \(z\mapsto x-\varepsilon z\).

The original truncation gives \(|f_j|\leq j\) and support in \(Q_j=[-j,j]^d\). Consequently \(0\leq M_\varepsilon\leq2j\|\rho\|_1\), with support contained in the actual compact set \(Q_j\cup(Q_j+\varepsilon\operatorname{supp}\rho)\). It follows that \(M_\varepsilon\in L^t\). At \(t=1\), nonnegative Tonelli gives \(\|M_\varepsilon\|_1=\int|\rho(z)|\|h_z\|_1\,dz\). If \(t>1\), apply the proved scalar Hölder inequality with its actual conjugate exponent \(t'=t/(t-1)\). The full power satisfies \(\|M_\varepsilon^{t-1}\|_{t'}=\|M_\varepsilon\|_t^{t-1}\), since \((t-1)t'=t\). Nonnegative Tonelli then gives
\[
 \begin{aligned}
 \|M_\varepsilon\|_t^t
 &=\int M_\varepsilon(x)^{t-1}
              \left(\int|\rho(z)||h_z(x)|\,dz\right)dx\\
 &=\int|\rho(z)|
              \left(\int M_\varepsilon(x)^{t-1}|h_z(x)|\,dx\right)dz\\
 &\leq\|M_\varepsilon\|_t^{t-1}
                 \int|\rho(z)|\|h_z\|_t\,dz.
 \end{aligned}\tag{FL3a}
\]
The last integral is finite, because translation is an isometry and \(\|h_z\|_t\leq2\|f_j\|_t\). If \(\|M_\varepsilon\|_t>0\), division by its displayed positive power proves the integral triangle bound. If that norm is zero, the same bound is immediate without division. The exact difference formula (LP13), with both original scaling Jacobians retained, gives \(|\rho_\varepsilon*f_j-f_j|\leq M_\varepsilon\). Combining these two inequalities proves exactly (FL3), rather than replacing it by the weaker power-integral bound (LP14). Translation continuity makes \(\|h_z\|_t\to0\) for each fixed \(z\), and its original bound \(2|\rho(z)|\|f_j\|_t\) is integrable. Its dependence on \(z\) is continuous by that same translation theorem and the reverse norm inequality. Dominated convergence therefore proves the limit in (FL3) for each of the original exponents \(a,c\), without an infinite-dimensional integration theorem.

Its bound \(2|\rho(z)|\|f_j\|_t\) is integrable. Choose a positive \(\varepsilon_j<1/j\) making both errors at most \(1/j\). Then \(v_j=\rho_{\varepsilon_j}*f_j\) is compact smooth and tends to \(f\) in both norms. Differentiating this absolutely convergent convolution proves smoothness, and its support is contained in the sum of the two original compact supports. This constructs a single approximation, rather than assuming that two independently chosen approximations coincide.

Apply this with \(a=1,c=2\). The ordinary Fourier and inverse integrals satisfy
\[
 \begin{split}
 \sup_\xi|Fv_j(\xi)-Ff(\xi)|&\leq\|v_j-f\|_1,\\
 \sup_x|Gv_j(x)-Gf(x)|&\leq(2\pi)^{-d}\|v_j-f\|_1 .
 \end{split}                                                   \tag{FL4}
\]
Here the symbols on the right side of each difference denote their ordinary absolutely defined integrals. Their uniform limits therefore agree almost everywhere with the \(L^2\) limits in (FL2). Indeed, the summable-difference argument in the completeness proof supplies an almost-everywhere convergent subsequence of either \(L^2\) sequence. The uniform and almost-everywhere limits of that subsequence are equal. Thus the constructed \(L^2\) classes coincide with the original integrals on \(L^1\cap L^2\), with the exact inverse factor retained.

The same simultaneous approximation identifies any two finite-exponent continuous extensions of an operator from Schwartz functions when both original norm bounds are available. For completeness, if functions converge in \(L^a\) and \(L^c\) to two limits, select a common subsequence with summable \(a\)-th and \(c\)-th powers of its errors. Chebyshev's integral inequality and the measure of the countable tail unions make both errors tend to zero almost everywhere; the limits must agree. This is the identification used for the multiplier below.

### 7.3. Parseval pairing, multiplication and the actual adjoint

Approximating both inputs by Schwartz functions in \(L^2\), Theorem 2.1 and Cauchy–Schwarz prove
\[
 \langle u,v\rangle
   =(2\pi)^{-d}\int_{\mathbb R^d}
                     Fu(\xi)\overline{Fv(\xi)}\,d\xi .
                                                               \tag{FL5}
\]
The inner product is linear in the first variable. Each pairing difference tends to zero by the sum of the two Cauchy–Schwarz bounds, so the original factor persists.

If \(b\) is a measurable scalar frequency function with
\(\|b\|_\infty\leq B\), multiplication by \(b\) respects the completed null classes and maps \(L^2\) to itself with norm at most \(B\). Hence
\[
 \begin{split}
 T_b&=G\,M_b\,F,\qquad M_bh=bh,\\
 \|T_bf\|_2
 &\leq(2\pi)^{-d/2}B(2\pi)^{d/2}\|f\|_2=B\|f\|_2,\\
 \langle T_bu,v\rangle
 &=(2\pi)^{-d}\int b(\xi)Fu(\xi)\overline{Fv(\xi)}\,d\xi
   =\langle u,T_{\overline b}v\rangle .
 \end{split}                                                   \tag{FL6}
\]
This proves the actual adjoint \(T_b^*=T_{\overline b}\). It uses the constructed inverse maps, not an assumed representation of an \(L^p\) dual space. For Schwartz \(f\), \(bFf\in L^1\cap L^2\), so \(T_bf\) is exactly the original inverse integral. These statements apply in the elliptic chapter with \(d=n\geq1\); its arbitrary value of the symbol at zero changes no frequency integral.

## References

- [Melrose] Richard Melrose, *Differential Analysis*, MIT 18.155 lecture notes, 2004, [MIT OpenCourseWare lecture notes](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/pages/lecture-notes/).
- [Beezer] Robert Beezer, *A First Course in Linear Algebra*, [author's source repository](https://github.com/rbeezer/fcla).

*Scalar integral-bound proof integrated from the existing AN-03 programme proof by GPT-6 Astra (OpenAI), Ultra, October 2026. CC0-1.0.*
