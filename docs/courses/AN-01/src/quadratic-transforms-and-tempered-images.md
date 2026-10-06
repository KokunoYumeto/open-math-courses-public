# Quadratic transforms and tempered images

*Original edition by GPT-6.1 Sol (OpenAI), Ultra reasoning effort. Repaired and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Original exposition: public domain (CC0); supplied prerequisites retain their stated licences.*

A unit Gaussian becomes a constant entire function with finite weighted energy. Moving its position and frequency moves that energy center, while changing its width stretches the output in two different directions. An impulse or a plane wave instead leaves one whole direction without decay. We use these measurements to distinguish the square-integrable, Schwartz and tempered images of a quadratic transform, then prove the full arbitrary-matrix theorem and every converse. Finite Gaussian levels, interference and point jets supply further tests of the exact normalization and reconstruction formulas.

We use \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)dx\), inverse factor \((2\pi)^{-n}\), \(D=-i\partial\), and complex bilinear distributional pairings.

The supplied [Fourier foundation](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, proves the Schwartz seminorm operations, compact-test density, Gaussian mass, both inverse transforms and bilinear distributional transposes. [Fourier–Laplace slices and boundary poles](fourier-laplace-slices-and-boundary-poles.md), Lemma 0.1 and Lemma L, proves the completed square-integral maps and the analytic-slice representation. The supplied [integration foundation](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, proves convergence, product integration, real linear Jacobians, norm inequalities, completeness and density. The [scalar foundation](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, and [finite algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, supply the elementary calculus and matrix operations.

The exact Gaussian norm and its full converse are [Gaussian norms and entire uncertainty](gaussian-norms-and-entire-uncertainty.md), Theorem D; its Lemma 0.1 supplies positive matrix roots and the entire-frequency real Gaussian formula. The holomorphic determinant branch and complex matrix transform are [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Lemma 2.1 and Theorem 3.1. The coordinate Cauchy formulas are [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2, and the full polydisk power-series and identity proofs are [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section 3 and Lemma 3.1. The [angular foundation](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4 and formula (A16), proves the polar integral used for the finite Hermite levels.

## A complex Gaussian at every complex frequency

**Lemma 0.1.** Let \(Z\) be complex symmetric with \(\operatorname{Re}Z>0\), and let \(g(Z)\) be the holomorphic determinant root from U020, Lemma 2.1, positive on real positive definite matrices. For every \(w\in\mathbb C^n\),
\[
 \begin{gathered}
 \int_{\mathbb R^n}e^{-y^TZy/2+iw\cdot y}\,dy\\
 =\frac{(2\pi)^{n/2}}{g(Z)}
       e^{-w^TZ^{-1}w/2}.
 \end{gathered}
\]
The integral and all of its complex-frequency derivatives converge absolutely, locally uniformly in \(w\).

**Proof.** The real symmetric matrix \(\operatorname{Re}Z\) has a positive lower eigenvalue by U020's proved diagonalization. On each compact complex set of \(w\), every derivative of the integrand is dominated by a constant times a polynomial in \(|y|\) times \(e^{-c|y|^2+C|y|}\), with \(c>0\). Completing scalar squares and the Gaussian estimates in the Fourier foundation make these bounds integrable. Dominated difference quotients and U015's polydisk proof show that the integral is entire in \(w\). U020, Theorem 3.1, with matrix \(Z\), time parameter \(t=2\) and real frequency \(-w\), gives the formula for real \(w\). The right side is entire as well. Hold all but one coordinate real: the difference and all its real derivatives vanish on the real axis. Cauchy–Riemann makes all complex Taylor coefficients zero there; the convergent power series and the connected identity principle extend zero to the whole coordinate plane. Repeat for each coordinate, allowing the preceding ones to be complex. This proves the displayed identity everywhere, with the same determinant branch. \(\square\)

## Measure the unit Gaussian and move its center

**Worked measurement B1.** First take one real variable and the phase matrices
\[
\begin{gathered}
A=i,\qquad B=-i\sqrt2,\\
C=i,\qquad c=\pi^{-3/4},\\
\Phi(z)=|z|^2/2.
\end{gathered}
\tag{B1}
\]
Indeed, if \(z=x+i\eta\), then \(Bz=\sqrt2\eta-i\sqrt2 x\). The maximizing input point is \(q=\sqrt2 x\). Completing the real square gives
\[
\begin{gathered}
(\mathcal Bu)(z)=\pi^{-3/4}\\
{}\cdot\int_{\mathbb R}
e^{-z^2/2+\sqrt2zy-y^2/2}u(y)\,dy,\\
\Phi(z)+\operatorname{Im}\phi(z,y)\\
=\tfrac12(y-\sqrt2 x)^2.
\end{gathered}
\tag{B2}
\]
We call this instance \(\mathcal B\) to distinguish it from the arbitrary matrices below. Its weighted squared energy density is
\(\rho_U(z)=|U(z)|^2e^{-|z|^2}\), with respect to ordinary area \(dx\,d\eta\). Its normalized modulus is \(m_U(z)=|U(z)|e^{-|z|^2/2}\).

The unit input \(g_0(y)=\pi^{-1/4}e^{-y^2/2}\) has squared integral one. Lemma 0.1 gives the full complex Gaussian integral
\[
\begin{gathered}
\int e^{-y^2+\sqrt2zy}\,dy
=\sqrt\pi e^{z^2/2},\\
\mathcal B g_0=\pi^{-1/2},\\
\rho_{\mathcal B g_0}(z)=\pi^{-1}e^{-|z|^2},\\
\int_{\mathbb C}\rho_{\mathcal B g_0}\,dx\,d\eta=1.
\end{gathered}
\tag{B3}
\]
The constant output has the factor \(\pi^{-1/2}\) because our output measure is area itself. This is the simplest direct check on the normalization in Theorem E.

Now move the input and add a real oscillation:
\(g_{a,p}(y)=\pi^{-1/4}e^{-(y-a)^2/2+ipy}\), where \(a,p\in\mathbb R\). It still has norm one. Combining the two real Gaussian factors inside (B2) gives
\[
\begin{gathered}
\mathcal B g_{a,p}(z)\\
=\pi^{-1/2}
e^{\frac{(a+ip)z}{\sqrt2}-\frac{a^2+p^2}4+\frac{iap}2},\\
\rho_{\mathcal B g_{a,p}}(x+i\eta)\\
=\pi^{-1}
e^{-(x-\frac a{\sqrt2})^2-(\eta+\frac p{\sqrt2})^2}.
\end{gathered}
\tag{B4}
\]
For the first formula, the remaining integral is
\(\int e^{-y^2+(\sqrt2z+a+ip)y}\,dy
=\sqrt\pi e^{(\sqrt2z+a+ip)^2/4}\); expanding that square proves every phase and constant displayed. The second formula follows by taking its real part and completing two real squares. The output energy is centered at \((a/\sqrt2,-p/\sqrt2)\). In particular the imaginary center has the opposite sign to the input frequency for the chosen kernel. Each density integrates to one by two real Gaussian integrals. The exact complex phase \(iap/2\) will matter when two such states are added.

There is also a useful pointwise measurement for every \(u\in L^2\). The squared input-kernel norm in (B2) is
\(\pi^{-3/2}\int e^{-\operatorname{Re}(z^2)+2\sqrt2xy-y^2}dy
=\pi^{-1}e^{|z|^2}\). Cauchy--Schwarz therefore proves
\[
|\mathcal Bu(z)|e^{-|z|^2/2}
\leq\pi^{-1/2}\|u\|_2.
\tag{B5}
\]
The translated and modulated Gaussians attain this bound at their energy centers. Each displayed Gaussian output has rapid normalized decay, so Theorem E will also recognize each as Schwartz data. The general proof below explains why the same three image tests remain valid for every admissible coupled phase.

All vector products in the phase are bilinear. Let \(n\geq1\), let \(A,C\) be complex symmetric \(n\)-by-\(n\) matrices, let \(B\) be an invertible complex matrix, and let

\[
\begin{gathered}
Q=\operatorname{Im}C>0,\\
R=\operatorname{Re}C,\\
\phi(z,y)\\
=\tfrac12z^TAz+(Bz)\cdot y\\
+\tfrac12y^TCy,\\
c=2^{-n/2}\pi^{-3n/4}\\
(\det Q)^{-1/4}|\det B|.
\end{gathered}
\tag{E1}
\]

Entrywise real and imaginary parts of \(C\) are real symmetric; positivity of \(Q\) is strict on real vectors. Define

\[
\begin{gathered}
(Tu)(z)=c\int_{\mathbb R^n}e^{i\phi(z,y)}u(y)\,dy,\\
\Phi(z)=\max_{y\in\mathbb R^n}[-\operatorname{Im}\phi(z,y)].
\end{gathered}
\tag{E2}
\]

For tempered inputs the integral means the complex bilinear action of the distribution on the indicated Schwartz function. No complex conjugation is inserted into that action.

## E. The full isometry and all three image classes

**Theorem E.** The map \(T\) is a unitary bijection from \(L^2(\mathbb R^n)\) onto the space of entire functions with norm

\[
\begin{gathered}
\|U\|_\Phi^2\\
=\int_{\mathbb C^n}|U(z)|^2e^{-2\Phi(z)}dL(z).
\end{gathered}
\tag{E3}
\]

Its Schwartz image consists exactly of the entire functions satisfying

\[
\begin{gathered}
\sup_z(1+|z|)^N|U(z)|e^{-\Phi(z)}<\infty\\
\text{for every integer }N\geq0.
\end{gathered}
\tag{E4}
\]

Its tempered-distribution image consists exactly of the entire functions satisfying

\[
\begin{gathered}
|U(z)|e^{-\Phi(z)}\leq C_N(1+|z|)^N\\
\text{for some integer }N\geq0.
\end{gathered}
\tag{E5}
\]

Both maps are injective. For the Schwartz image the inverse is the absolutely convergent formula, with all derivatives and weighted real seminorms obtained by differentiating under it,

\[
\begin{gathered}
u(y)=c\int_{\mathbb C^n}\\
e^{-i\overline{\phi(z,y)}}U(z)e^{-2\Phi(z)}dL(z).
\end{gathered}
\tag{E6}
\]

For a general image in (E5), the inverse is instead defined on each \(\psi\in\mathcal S\) by

\[
\begin{gathered}
\langle u,\psi\rangle\\
=\int_{\mathbb C^n}U(z)\overline{T(\overline\psi)(z)}\\
e^{-2\Phi(z)}dL(z).
\end{gathered}
\tag{E7}
\]

Formula (E7) is absolutely convergent and complex linear in \(\psi\). The pointwise absolute integral (E6) is not asserted for arbitrary \(L^2\) or tempered input.

The weighted seminorms in (E4) also identify the Schwartz topology: the forward bounds (E16) and inverse bounds from (E13)–(E17) make both maps continuous. For each fixed polynomial-growth bound (E5), (E7) bounds the inverse by a finite sum of original Schwartz test seminorms. No different unspecified topology on the full union of growth classes is assumed.

### The actual maximizing point and Gaussian weight

Put \(\beta=\operatorname{Im}(Bz)\) and \(p=\operatorname{Re}(Bz)\). These are coordinates of the given cross term \((Bz)\cdot y\). Define the real center

\[
\begin{gathered}
q=-Q^{-1}\beta.
\end{gathered}
\tag{E8}
\]

Completing the real square in \(y\) gives

\[
\begin{gathered}
-\operatorname{Im}\phi(z,y)\\
=-\tfrac12\operatorname{Im}(z^TAz)-\beta\cdot y\\
-\tfrac12y^TQy,\\
\Phi(z)=-\tfrac12\operatorname{Im}(z^TAz)\\
+\tfrac12\beta^TQ^{-1}\beta,\\
K_z(y)=e^{i\phi(z,y)-\Phi(z)}\\
=e^{i\operatorname{Re}(z^TAz)/2}\\
e^{ip\cdot y+i y^TRy/2}\\
e^{-(y-q)^TQ(y-q)/2}.
\end{gathered}
\tag{E9}
\]

The maximizing point is exactly (E8) and is unique because \(Q>0\). The map \(z\mapsto(p,q)\) is an invertible real linear map: first multiply by the complex invertible \(B\), then keep its real part and apply \(-Q^{-1}\) to its imaginary part. Thus its Euclidean norm is equivalent to \(|z|\), with constants determined by the given matrices. Its actual real Jacobian is also determined, rather than presumed one. For any complex invertible \(M\), the real matrix of \(z\mapsto Mz\) has blocks \(\bigl(\begin{smallmatrix}\operatorname{Re}M&-\operatorname{Im}M\\\operatorname{Im}M&\operatorname{Re}M\end{smallmatrix}\bigr)\). Complexifying and changing coordinates from \((x,y)\) to \((z,\overline z)\) conjugates it to \(\operatorname{diag}(M,\overline M)\); hence its real determinant is \(\det M\det\overline M=|\det M|^2>0\). The supplied integration foundation, §16, therefore applies with this exact real Jacobian.

### The whole \(L^2\) map and its converse

For \(u\in L^2\), set \(f(y)=e^{iy^TCy/2}u(y)\). Then \(|f(y)|^2e^{y^TQy}=|u(y)|^2\). Theorem D applies to \(f\) with its actual matrix \(Q\). If \(F=\mathcal Ff\) denotes the entire extension, the cross-term convention gives

\[
\begin{gathered}
Tu(z)=c e^{iz^TAz/2}F(w),\\
w=-Bz.
\end{gathered}
\tag{E10}
\]

Every such transform is entire. Equations (E9)–(E10) give

\[
\begin{gathered}
|Tu(z)|^2e^{-2\Phi(z)}\\
=c^2|F(-Bz)|^2e^{-\beta^TQ^{-1}\beta}.
\end{gathered}
\tag{E11}
\]

Changing from \(z\) to \(w=-Bz\) contributes \(|\det B|^{-2}\), and \(\operatorname{Im}w=-\beta\). Theorem D and the displayed value of \(c\) therefore give

\[
\begin{gathered}
\|Tu\|_\Phi^2\\
=c^2|\det B|^{-2}\\
\pi^{n/2}(2\pi)^n\sqrt{\det Q}\\
\int|f(y)|^2e^{y^TQy}dy\\
=2^{-n}\pi^{-3n/2}(\det Q)^{-1/2}\\
\pi^{n/2}(2\pi)^n\\
\sqrt{\det Q}\,\|u\|_2^2\\
=\|u\|_2^2.
\end{gathered}
\tag{E12}
\]

The cancellation retains the actual cross term, both Jacobians, every power of two and pi, and the positive determinant of \(Q\). For the converse, given an entire \(U\) with finite norm (E3), put \(z=-(B)^{-1}w\) and
\(F(w)=c^{-1}e^{-iz^TAz/2}U(z)\).
It is entire. Equation (E11) and the same Jacobian show that it has finite Gaussian norm in Theorem D. That theorem supplies the unique \(f\) with \(|f|^2e^{y^TQy}\) integrable. Then \(u=e^{-iy^TCy/2}f\in L^2\), since its squared modulus is exactly that weighted modulus. Equation (E10) gives \(Tu=U\). This proves bijection and equality of norms. The corresponding inner-product identity follows by polarization, with the inner product linear in its first variable.

### Direct seminorm bounds for the normalized Gaussian kernels

At each \(z\), both \(K_z\) and \(e^{i\phi(z,\cdot)}\) are Schwartz functions. For every pair of multiindices \(\alpha,\gamma\), differentiating (E9) gives the bound

\[
\begin{gathered}
\sup_y|y^\alpha\partial_y^\gamma K_z(y)|\\
\leq C_{\alpha,\gamma}(1+|p|+|q|)^{|\alpha|+|\gamma|}.
\end{gathered}
\tag{E13}
\]

Indeed the first derivative multiplies the unchanged Gaussian and phase by \(i(p+Ry)-Q(y-q)\). Iteration gives a polynomial in \(p,q,y-q\) of degree at most \(|\gamma|\), with fixed coefficients from \(Q,R\); multiplication by \(y^\alpha=(q+(y-q))^\alpha\) adds at most \(|\alpha|\). Every polynomial in \(y-q\) times this strictly positive Gaussian has a finite translation-independent supremum. This proves every term in (E13), including the zero derivative and weight.

For a tempered \(u\), its continuity is a bound by a finite sum of the original Schwartz seminorms. Equation (E13), real linear norm equivalence and \(e^{-\Phi}Tu=c\langle u,K_z\rangle\) therefore give (E5). Its transform is entire: on any compact complex set the original \(e^{i\phi(z,y)}\), all its complex derivatives and the difference-quotient remainders have uniformly bounded Schwartz seminorms. The derivatives are explicit polynomial factors times a Gaussian with bounded real center. Taylor's integral remainder in each complex coordinate shows convergence of the difference quotient in every seminorm. Iterated Cauchy formulas on a fixed coordinate polydisk bound each Taylor coefficient in any given seminorm by \(C_r r^{-|\alpha|}\). The resulting geometric product makes the power series converge in that seminorm on every smaller polydisk. Applying the continuous functional \(u\) therefore gives the whole local holomorphic power expansion. Thus no tempered input is silently restricted to an ordinary function.

For \(u\in\mathcal S\), put \(v(y)=e^{iy^TRy/2}u(y)\). The chirp multiplication and its inverse preserve \(\mathcal S\), since every derivative of either multiplier is a polynomial times a function of modulus one. From (E9), apart from its explicit unit phase and factor \(c\), the normalized transform is

\[
\begin{gathered}
W_v(q,p)\\
=\int e^{ip\cdot y}v(y)g(y-q)dy,\\
g(r)=e^{-r^TQr/2}.
\end{gathered}
\tag{E14}
\]

Integration by parts gives the exact identity

\[
\begin{gathered}
p^\gamma W_v(q,p)=i^{|\gamma|}\\
\int e^{ip\cdot y}\partial_y^\gamma[v(y)g(y-q)]dy.
\end{gathered}
\tag{E15}
\]

There are no end terms, because both factors and their derivatives decay. To bound this expression use the full Leibniz sum, and
\((1+|q|)^M\leq C_M(1+|y|)^M(1+|y-q|)^M\).
For each summand, the weighted derivative of \(v\) is bounded by a Schwartz seminorm, while the polynomially weighted derivative of \(g(y-q)\) has a finite integral independent of \(q\). Thus for all integers \(M,L\geq0\),

\[
\begin{gathered}
(1+|q|)^M(1+|p|)^L\\
|W_v(q,p)|\\
\leq C_{M,L}\sum_{\substack{\alpha,\gamma\\\text{in a finite set}}}\\
\sup_y|y^\alpha\partial^\gamma v(y)|.
\end{gathered}
\tag{E16}
\]

The passage from monomials \(p^\gamma\) to \((1+|p|)^L\) uses only the finite scalar polynomial bound. Norm equivalence proves (E4), with each output seminorm bounded by finitely many original input seminorms. It also proves rapid decay for \(T(\overline\psi)\), needed in (E7).

### Schwartz reconstruction, with convergence in every seminorm

For \(\psi\in\mathcal S\), define

\[
\begin{gathered}
R\psi(y)=c\int \overline{K_z(y)}\\
e^{-\Phi(z)}T\psi(z)\,dL(z).
\end{gathered}
\tag{E17}
\]

This is an actual absolutely convergent function integral. By (E13) and (E16), each differentiated integrand, multiplied by any \(y^\alpha\), is bounded in supremum over \(y\) by an integrable function of \(z\). Taking sufficiently many rapid-decay powers makes it integrable in the real dimension \(2n\). Explicitly, in real dimension \(d\), the shell \(2^k\le |z|<2^{k+1}\) lies in a cube of volume at most \(C_d2^{kd}\). A bound \((1+|z|)^{-d-\epsilon}\), \(\epsilon>0\), therefore has shell integral at most \(C_d2^{-k\epsilon}\); the geometric sum and the bounded central cube prove integrability. Differentiation under the integral is legitimate on every compact set of \(y\), and these same bounds prove that \(R\psi\in\mathcal S\). Truncating the \(z\) integral to balls converges in every original Schwartz seminorm, since each discarded seminorm is bounded by the tail of its integrable majorant.

For any \(h\in\mathcal S\), absolute Fubini and (E12) give
\(\int R\psi\,\overline h\,dy=\int T\psi\,\overline{Th}\,e^{-2\Phi}dL=\int\psi\,\overline h\,dy\).
Absolute Fubini follows, for example, by \(|K_z(y)|\leq1\), \(\|h\|_1<\infty\), and the integrable rapid decay of \(e^{-\Phi}T\psi\). Thus \(R\psi=\psi\) as a distribution and, since both are smooth, pointwise. This proves (E6) for Schwartz input.

Taking the complex conjugate of (E17) applied to \(\overline\psi\) gives the actual Schwartz identity

\[
\begin{gathered}
\psi(y)=c\int K_z(y)\\
\overline{e^{-\Phi(z)}T(\overline\psi)(z)}dL(z),
\end{gathered}
\tag{E18}
\]

with convergence in every seminorm just established. To justify applying a tempered functional to this integral, first insert a smooth compact cutoff in the real \(z\) variables. On a box containing its support, the integrand is continuous in every Schwartz seminorm. This follows directly from the compact-parameter Gaussian bounds for its first real \(z\) derivatives and the scalar fundamental theorem. In each seminorm, the difference between a Riemann sum and the scalar integral is at most the box volume times the largest seminorm oscillation on a mesh cell. It tends to zero as the mesh shrinks. Thus the finite-seminorm bound of \(u\in\mathcal S'\) passes its action through the compact integral. Choose cutoffs equal to one on expanding balls and bounded by one; the integrable seminorm majorants proved for (E17) make the omitted tails tend to zero in each seminorm. The scalar functional tails obey the same finite sum of bounds. Passing to the limit proves the interchange for (E18). The result is exactly (E7) with \(U=Tu\). This proves injectivity on all tempered inputs as well as the actual distributional reconstruction formula.

Conversely suppose an entire \(U\) obeys (E4). Define \(u\) by (E6), rewritten as \(c\int\overline{K_z(y)}e^{-\Phi}U(z)dL\). Equations (E13) and (E4), exactly as in (E17), prove absolute convergence, smoothness, every weighted derivative bound and hence \(u\in\mathcal S\). Since (E4) implies finite norm (E3), the \(L^2\) converse already supplies an input \(u_0\). For every Schwartz test, its unitary pairing with that test equals the integral (E7), which also equals the pairing of the constructed \(u\) by absolute Fubini. Therefore \(u=u_0\) as distributions. In particular \(Tu=U\). This proves both directions of the full Schwartz characterization from the stated modulus bounds alone.

### Every entire polynomially weighted function comes from a tempered input

Now suppose \(U\) obeys (E5). Formula (E7) converges absolutely: its two normalized factors have polynomial growth and rapid decay respectively. Choose in (E16) an output decay order greater than \(N+2n\). It bounds (E7) by a fixed finite sum of Schwartz seminorms of \(\psi\), and proves that it defines a tempered distribution \(u\). It remains to show \(Tu=U\); that step cannot be replaced by a formal adjoint identity for an input not yet known to exist.

Use the positive real square root \(S=Q^{1/2}\). U063, Lemma 0.1, proves the existence and uniqueness of this positive symmetric invertible matrix by exact orthogonal diagonalization. Let

\[
\begin{gathered}
w=-Bz=\sqrt2 S Z,\\
H(Z)=c^{-1}\\
e^{-iz^TAz/2+Z\cdot Z/2}U(z).
\end{gathered}
\tag{E19}
\]

This is an entire function, because \(z=-(B)^{-1}\sqrt2 S Z\) is a complex linear bijection. Since \(\operatorname{Im}w=\sqrt2 S\operatorname{Im}Z\), direct cancellation of the real parts in (E19) gives

\[
\begin{gathered}
|H(Z)|e^{-|Z|^2/2}\\
=c^{-1}|U(z)|e^{-\Phi(z)}.
\end{gathered}
\tag{E20}
\]

Indeed \(\operatorname{Re}(Z\cdot Z)-|Z|^2=-2|\operatorname{Im}Z|^2\), and \(\beta^TQ^{-1}\beta=2|\operatorname{Im}Z|^2\). All these are identities for the given coupled matrices, not a diagonal restriction of the original theorem.

For \(0<r<1\), set \(H_r(Z)=H(rZ)\), and use the inverse holomorphic factor in (E19) to define an entire \(U_r\). From (E5), norm equivalence and (E20),

\[
\begin{gathered}
|H_r(Z)|e^{-|Z|^2/2}\\
\leq C(1+|Z|)^N e^{-(1-r^2)|Z|^2/2}.
\end{gathered}
\tag{E21}
\]

Thus every \(U_r\) has finite norm (E3), after the fixed linear Jacobian. Also the normalized functions \(e^{-\Phi}U_r\) have one uniform polynomial bound independent of \(r\), and \(U_r\to U\) pointwise and locally uniformly as \(r\uparrow1\).

The \(L^2\) converse gives \(u_r\in L^2\) with \(Tu_r=U_r\). Its inner-product identity with \(\overline\psi\) gives formula (E7) for each \(u_r\). The uniform polynomial bound in (E21) and the rapid normalized decay of \(T\overline\psi\) allow dominated convergence in that formula. Consequently \(u_r\to u\) on every Schwartz test. For each fixed complex \(z\), the function \(e^{i\phi(z,\cdot)}\) is one such test, so
\(Tu_r(z)\to Tu(z)\). The left side is \(U_r(z)\to U(z)\). Hence \(Tu=U\) everywhere. Reconstruction (E18) proves uniqueness. This completes the converse for every tempered growth order, and therefore the entire theorem. \(\square\)

## Change a width and inspect the two output axes

**Worked measurement B2.** Keep (B1)--(B2), but take the unit input
\(g_s(y)=(s/\pi)^{1/4}e^{-sy^2/2}\), with \(s>0\). Combining its exponent with the kernel and applying the real-positive Gaussian formula gives
\[
\begin{gathered}
\mathcal Bg_s(z)
=k_s e^{(1-s)z^2/[2(1+s)]},\\
k_s=\frac{\sqrt2\,s^{1/4}}{\sqrt\pi\sqrt{1+s}},\\
\rho_{\mathcal Bg_s}(x+i\eta)\\
=k_s^2 e^{-2s x^2/(1+s)-2\eta^2/(1+s)}.
\end{gathered}
\tag{B6}
\]
Both precision coefficients are strictly positive. Their product is \(4s/(1+s)^2\), so the output squared norm is exactly
\[
\begin{gathered}
k_s^2\sqrt{\frac{\pi(1+s)}{2s}}\\
{}\cdot\sqrt{\frac{\pi(1+s)}2}=1,\\
k_s\leq\pi^{-1/2},\\
k_s=\pi^{-1/2}\ \Longleftrightarrow\ s=1.
\end{gathered}
\tag{B7}
\]
The last assertion uses \(1+s\geq2\sqrt s\), with equality precisely at one. Every fixed \(s>0\) gives a Schwartz image, yet the rate of rapid decay changes with \(s\). As \(s\) tends to zero, the real precision tends to zero and energy spreads along the real axis. As \(s\) tends to infinity, the imaginary precision tends to zero and energy spreads along the imaginary axis. The fixed norm stays one throughout; no single positive Gaussian decay rate works uniformly over all widths.

**Worked measurement B3.** An impulse and a plane wave expose what happens when one axis has no decay. Acting on the kernel by the point mass at real \(a\) gives
\[
\begin{gathered}
\mathcal B\delta_a(z)\\
=\pi^{-3/4}e^{-z^2/2+\sqrt2az-a^2/2},\\
m_{\mathcal B\delta_a}(x+i\eta)\\
=\pi^{-3/4}e^{-(\sqrt2x-a)^2/2}.
\end{gathered}
\tag{B8}
\]
There is Gaussian decay transverse to the line \(x=a/\sqrt2\), and constant modulus along that line. The normalized modulus is bounded, but its squared integral over the \(\eta\) axis is infinite. It also fails rapid decay on the line. Theorem E classifies this entire function as a tempered image belonging to neither the Hilbert nor the Schwartz image.

The regular tempered input \(e^{ipy}\), with real \(p\), yields another exact Gaussian integral:
\[
\begin{gathered}
\mathcal B(e^{ipy})(z)\\
=\sqrt2\,\pi^{-1/4}
e^{z^2/2+i\sqrt2pz-p^2/2},\\
m_{\mathcal B(e^{ipy})}(x+i\eta)\\
=\sqrt2\,\pi^{-1/4}e^{-(\eta+p/\sqrt2)^2}.
\end{gathered}
\tag{B9}
\]
Its defining distribution is continuous on Schwartz tests, since their absolute integral is bounded by an integrable polynomial weight times a Schwartz seminorm. The kernel integral converges absolutely because of its Gaussian factor. Completing its square proves (B9). Now the normalized modulus is constant along the real direction. Its classification is the same as the impulse's, with the two axes exchanged.

For the first derivative of the impulse, the sign in distributional differentiation gives
\[
\begin{gathered}
\mathcal B(\partial_y\delta_a)(z)\\
=\pi^{-3/4}(a-\sqrt2z)\\
{}\cdot e^{-z^2/2+\sqrt2az-a^2/2},\\
m_{\mathcal B(\partial_y\delta_a)}(a/\sqrt2+i\eta)\\
=\pi^{-3/4}\sqrt2\,|\eta|.
\end{gathered}
\tag{B10}
\]
Thus even bounded normalized modulus is stronger than the full tempered-image condition: this output needs a linear growth allowance. Solution 11 determines the sharp allowance for every finite jet. Solutions 9--10 explain polynomial Gaussian levels and cancellation between two nearby Gaussian states. These cases give concrete tests for all the general bounds and reconstruction formulas proved above.

## Exercises

**Exercise 1 (foundation: retain the actual coupled phase).** In dimension two take
\[
\begin{gathered}
Q=\begin{pmatrix}2&1\\1&3\end{pmatrix},\\
R=\begin{pmatrix}0&1\\1&0\end{pmatrix},\\
C=R+iQ,\\
B=\begin{pmatrix}1&i\\0&2-i\end{pmatrix},\\
A=\begin{pmatrix}i&1\\1&-i/2\end{pmatrix}.
\end{gathered}
\]
At \(z=(1+i,-i)\), compute \(p,\beta,q,\Phi,c\) and the normalized kernel at its maximizing point. Verify the whole Gaussian defect for arbitrary real \(y\). Keep \((Bz)\cdot y\) rather than replacing it by another cross term.

**Exercise 2 (intermediate: exact translation and modulation).** For real vectors \(a,\xi\), put \(u_{a,\xi}(y)=e^{i\xi\cdot y}u(y-a)\). Derive its transformed function in terms of \(Tu\), including the whole quadratic multiplier and the complex translated argument. Prove that the resulting map on the entire Hilbert image is unitary, and explain its validity on \(\mathcal S\) and \(\mathcal S'\).

**Exercise 3 (intermediate: point masses and two full jet orders).** Compute \(T\delta_a\), \(T\partial_j\delta_a\), and \(T\partial_j\partial_k\delta_a\) for real \(a\). Determine their normalized growth orders and show why \(T\delta_a\) is tempered-image data but not Schwartz-image data.

**Exercise 4 (advanced: the exact operator correspondence).** Derive the output operators corresponding to multiplication by \(y_j\) and to \(D_{y_j}\). Check their commutator against \([y_j,D_{y_k}]=i\delta_{jk}\). Prove the needed commutation of the output multiplication operators rather than discarding matrix order.

**Exercise 5 (advanced: an independent Gaussian isometry calculation).** For an arbitrary real symmetric \(H>0\), compute \(T(e^{-y^THy/2})\) with the actual complex determinant branch. Independently integrate its output norm using a real positive block matrix in \((p,\beta)\). Prove its Schur complement and determinant formulas without assuming that \(H,Q,R\) commute.

**Exercise 6 (intermediate: an explicit tempered regularization).** Take \(Q=I,B=I,A=0,C=iI\). Apply the proof's radial entire regularization to \(T\delta_0\), and compute the corresponding \(L^2\) inputs \(u_r\), \(0<r<1\). Prove \(u_r\to\delta_0\) in \(\mathcal S'\), compute their squared \(L^2\) norms, and classify the limiting output among the three image classes.

**Exercise 7 (foundation: the entire condition cannot be omitted).** In the canonical one-dimensional case, show that \(U(x+iy)=e^{-x^2-y^2/2}\) has every rapid normalized modulus bound and finite weighted square-integral norm. Prove that it nevertheless belongs to none of the three transform images.

**Exercise 8 (advanced: topology and weak tempered recovery).** Derive a quantitative inverse bound for each Schwartz seminorm from rapid normalized output bounds. Then prove the following sequential assertion in both directions: under one uniform polynomial normalized bound, weak convergence of the inverse tempered distributions is equivalent to locally uniform convergence of the entire outputs. State the limit's bound and keep the uniform-growth hypothesis in the proof.

**Exercise 9 (intermediate: finite Hermite levels and their norms).** Use the transform \(\mathcal B\) in (B2). Define the real polynomials \(H_m\) by
\(e^{2ty-t^2}=\sum_{m\geq0}H_m(y)t^m/m!\), and put
\(g_m=H_m g_0/\sqrt{2^m m!}\). Derive \(\mathcal B g_m\) from the generating function, with justified differentiation under the integral. Compute all pairwise weighted inner products of these outputs by polar integration and hence the exact norm of any finite linear combination of the inputs. Also derive the output actions of \((y+\partial_y)/\sqrt2\) and \((y-\partial_y)/\sqrt2\). A completeness assertion for the infinite family is not required.

**Exercise 10 (advanced: phase-sensitive interference and a normalized collision).** Compute the full complex inner product of \(g_{a,p}\) and \(g_{b,q}\), with the inner product linear in its first variable. Obtain the squared norm of \(\alpha g_{a,p}+\beta g_{b,q}\). For \(a>0\), normalize \(g_{a,0}-g_{-a,0}\), compute its entire transform, and prove that these unit vectors tend in \(L^2\) to \(g_1\) as \(a\downarrow0\). Prove locally uniform convergence of their outputs using (B5), including the limiting output constant.

**Exercise 11 (advanced: every finite point jet and its exact growth order).** Fix real \(a\), an integer \(M\geq0\), and complex numbers \(d_0,\ldots,d_M\) with \(d_M\ne0\). For
\(u=\sum_{m=0}^M d_m\partial_y^m\delta_a\), compute \(\mathcal Bu\) using the polynomials \(\mathrm{He}_m\) defined by
\(e^{tw-t^2/2}=\sum_{m\geq0}\mathrm{He}_m(w)t^m/m!\). Prove that its smallest nonnegative integer normalized growth order is exactly \(M\). Prove directly that its output energy is infinite and that it fails rapid normalized decay. Classify the image without replacing the original distribution by an ordinary function.

## Solutions

**Solution 1.** Direct multiplication with the nonsymmetric \(B\) gives
\[
\begin{gathered}
Bz=(2+i,-1-2i),\\
p=(2,-1),\\
\beta=(1,-2),\\
Q^{-1}\beta=(1,-1),\\
q=(-1,1).
\end{gathered}
\]
Here \(\det Q=5\), \(\det B=2-i\), and \(z^TAz=-3i/2\). Thus
\[
\begin{gathered}
\Phi=-\tfrac12\operatorname{Im}(z^TAz)\\
+\tfrac12\beta^TQ^{-1}\beta=\frac94,\\
c=\frac{5^{1/4}}{2\pi^{3/2}}.
\end{gathered}
\]
At \(q\), \(q^TRq=-2\), \(q^TQq=3\), and \((Bz)\cdot q=-3-3i\). Consequently \(\phi(z,q)=-4-9i/4\) and \(K_z(q)=e^{-4i}\). For any real \(y\), completing the same real square gives
\(\Phi+\operatorname{Im}\phi(z,y)=\tfrac12(y-q)^TQ(y-q)\).
The right side is strictly positive away from \(q\), proving the unique maximizer and the normalized modulus everywhere, not only at the computed point. Inserting \(B^Tz\) would change the displayed \(p,\beta,q\) and solve a different problem.

**Solution 2.** Substitute \(y=t+a\). The coefficient of \(t\) in \(\phi(z,t+a)+\xi\cdot(t+a)\) is \(Bz+Ca+\xi\). Let
\[
\begin{gathered}
z'=z+B^{-1}(Ca+\xi),\\
d(z)= (Bz)\cdot a+\tfrac12a^TCa+\xi\cdot a\\
+\tfrac12z^TAz-\tfrac12z'^TAz'.
\end{gathered}
\]
Then the full identity of phases is \(\phi(z,t+a)+\xi\cdot(t+a)=\phi(z',t)+d(z)\), so
\(Tu_{a,\xi}(z)=e^{id(z)}Tu(z')\).
For \(L^2\) input, the substitution is justified by the Gaussian test kernel and Cauchy–Schwarz. Translation and real modulation preserve the input norm and have inverses, so Theorem E's unitary bijection makes this explicit output operator unitary on the entire weighted Hilbert space. On \(\mathcal S\), the product and chain rules show directly that these two input operations and their inverses preserve every seminorm up to finitely many others. Their transpose operations preserve \(\mathcal S'\). Applying the same exact test-kernel identity to a distribution proves the displayed formula there as well. The multiplier supplies the weight correction for the complex output translation.

**Solution 3.** Put \(\ell(z,a)=Bz+Ca\). Distributional differentiation, with its actual sign, gives
\[
\begin{gathered}
T\delta_a(z)=c e^{i\phi(z,a)},\\
T\partial_j\delta_a(z)=-ic\ell_j(z,a)e^{i\phi(z,a)},\\
T\partial_j\partial_k\delta_a(z)\\
=c\,[iC_{jk}-\ell_j(z,a)\ell_k(z,a)]e^{i\phi(z,a)}.
\end{gathered}
\]
The normalized point-mass modulus is exactly
\(c e^{-(a-q)^TQ(a-q)/2}\), and is bounded. Because \((p,q)\) are real linear coordinates, the first and second formulas have polynomial normalized bounds of orders one and two. These orders cannot be lowered: on \(q=a\), \(\beta=-Qa\), so \(\ell=p+Ra\) is real. Sending \(p_j\) to infinity makes the first order grow linearly; sending both relevant components to infinity makes the second order grow quadratically, including \(j=k\). The constant term \(iC_{jk}\) cannot cancel that leading growth. On the same center plane the point-mass normalized modulus stays equal to \(c\) while \(|p|\to\infty\). It therefore fails rapid decay already for weight one. The tempered and Schwartz characterizations in Theorem E give precisely the claimed distinction.

**Solution 4.** Differentiate the phase in \(z\). Since \(A\) is symmetric, in vector notation
\(D_z(Tu)=Az\,Tu+B^T T(yu)\). Define operators acting on entire outputs by
\[
\begin{gathered}
M=B^{-T}(D_z-Az),\\
N=-Bz-CM.
\end{gathered}
\]
Then \(T(y_j u)=M_jTu\). Integration by parts on the input gives
\[
\begin{gathered}
T(D_{y_j}u)\\
=-[(Bz)_jTu+(C T(yu))_j]\\
=N_jTu.
\end{gathered}
\]
For Schwartz inputs all integrals and derivatives are absolutely justified. For tempered inputs these identities follow by differentiating their Schwartz kernels and using the definition of distributional derivatives.

The components \(L_j=D_{z_j}-(Az)_j\) obey
\([L_j,L_k]=iA_{kj}-iA_{jk}=0\), so the constant linear combinations \(M_j\) commute. Also
\([M_j,z_l]=-i(B^{-T})_{jl}\). Hence
\[
\begin{gathered}
[M_j,N_k]=-[M_j,(Bz)_k]\\
=i\sum_l(B^{-T})_{jl}B_{kl}=i\delta_{jk}.
\end{gathered}
\]
The final sum is \((B^{-T}B^T)_{jk}\). The term \(CM\) contributes zero because the components of \(M\) commute; symmetry of \(A\) is the reason for that step. This reproduces the input commutator exactly.

**Solution 5.** Set \(W=H+Q>0\) and \(Z=W-iR\), a complex symmetric matrix with positive real part. Let \(g(Z)\) be the holomorphic determinant root in U020, Lemma 2.1, positive on real positive matrices. Lemma 0.1 of this lesson, with complex frequency \(w=Bz\), gives
\[
\begin{gathered}
U(z)=c e^{iz^TAz/2}\frac{(2\pi)^{n/2}}{g(Z)}\\
\exp\!\left[-\tfrac12(Bz)^TZ^{-1}(Bz)\right].
\end{gathered}
\]
Write \(Z^{-1}=P+iJ\), with real symmetric \(P,J\). The identity
\(P=Z^{-*}WZ^{-1}\) follows by multiplying out the Hermitian part of \(Z^{-1}\), so \(P>0\) and \(\det P=\det W/|\det Z|^2\). The real and imaginary parts of \(Z(P+iJ)=I\) give \(WP+RJ=I\) and \(WJ-RP=0\). Substituting \(R=WJP^{-1}\) into the first yields
\(P+JP^{-1}J=W^{-1}\), with the indicated order of factors.

The normalized squared output modulus, apart from its constant, is the real Gaussian in \((p,\beta)=(\operatorname{Re}Bz,\operatorname{Im}Bz)\) with precision
\[
\begin{gathered}
G=\begin{pmatrix}P&-J\\-J&Q^{-1}-P\end{pmatrix}.
\end{gathered}
\]
Its Schur complement is
\(Q^{-1}-P-JP^{-1}J=Q^{-1}-W^{-1}>0\), since \(W-Q=H>0\) and the inverse-order argument in the Gaussian lesson applies. The real block elimination identity therefore gives
\[
\begin{gathered}
\det G=\det P\det(Q^{-1}-W^{-1})\\
=\frac{\det H}{\det Q\,|\det Z|^2}.
\end{gathered}
\]
To verify that elimination directly, put \(D=Q^{-1}-W^{-1}\). The exact quadratic identity is
\[
\begin{gathered}
(p,\beta)^TG(p,\beta)\\
=(p-P^{-1}J\beta)^TP(p-P^{-1}J\beta)+\beta^TD\beta.
\end{gathered}
\]
The triangular real change \((p,\beta)\mapsto(p-P^{-1}J\beta,\beta)\) has determinant one. It proves positivity of \(G\), its determinant \(\det P\det D\), and the factorized Gaussian integral. Thus the Schur step includes its proof.

The intermediate determinant is \(\det H/(\det Q\det W)\), by the exact product \(Q^{-1}HW^{-1}=Q^{-1}-W^{-1}\). Now \(|g(Z)|^2=|\det Z|\), the real complex-linear Jacobian is \(|\det B|^2\), and the Gaussian in real dimension \(2n\) has mass \(\pi^n/\sqrt{\det G}\). Thus
\[
\begin{gathered}
\|U\|_\Phi^2=\\
\frac{c^2(2\pi)^n\pi^n}{|\det B|^2|\det Z|\sqrt{\det G}}\\
=\frac{\pi^{n/2}}{\sqrt{\det H}}=\|u\|_2^2.
\end{gathered}
\]
This independent calculation retains all matrix couplings and the determinant branch. The \(A\) factor cancels against its exact contribution to \(\Phi\), as the original modulus formula requires.

**Solution 6.** Here \(c=2^{-n/2}\pi^{-3n/4}\), \(\Phi(z)=|\operatorname{Im}z|^2/2\), and \(T\delta_0=c\). In the proof's gauge, \(z=-\sqrt2 Z\), the corresponding function is \(H(Z)=e^{Z\cdot Z/2}\). Radial regularization gives \(H_r=e^{r^2Z\cdot Z/2}\) and therefore
\[
\begin{gathered}
U_r(z)=c e^{-(1-r^2)z\cdot z/4},\\
u_r(y)=[\pi(1-r^2)]^{-n/2}e^{-h_r|y|^2/2},\\
h_r=\frac{1+r^2}{1-r^2}.
\end{gathered}
\]
Indeed the canonical transform of \(u_r\) is the Gaussian transform of \(e^{-|y|^2/2}u_r\), with \(h_r+1=2/(1-r^2)\); its mass factor cancels exactly to give \(U_r\). The input mass is \([2/(1+r^2)]^{n/2}\to1\). Dividing by this mass gives a probability Gaussian of variance \(h_r^{-1}\to0\). For any Schwartz test, boundedness and continuity at zero, followed by the change of variable \(t=\sqrt{h_r}y\) and dominated convergence against the fixed Gaussian, prove \(\langle u_r,\psi\rangle\to\psi(0)\).

Direct integration of its squared modulus gives
\[
\begin{gathered}
\|u_r\|_2^2=\pi^{-n/2}(1-r^4)^{-n/2}\longrightarrow\infty.
\end{gathered}
\]
Every \(r<1\) input is in \(L^2\), and \(U_r\to c\) locally uniformly. The constant limit has normalized modulus \(c e^{-|\operatorname{Im}z|^2/2}\), which is bounded but fails rapid decay along the real directions. Its weighted squared modulus is independent of \(\operatorname{Re}z\) and has infinite integral. It belongs to the tempered image and belongs to neither the Hilbert nor the Schwartz image. Diverging input norms are consistent with that conclusion.

**Solution 7.** Use the one-dimensional data \(Q=B=1,A=0,C=i\) from Exercise 6. Then \(\Phi(x+iy)=y^2/2\), so
\(e^{-\Phi}U=e^{-x^2-y^2}\). Multiplication by every power of \(1+|z|\) stays bounded, and \(|U|^2e^{-2\Phi}=e^{-2x^2-2y^2}\) is integrable. Nevertheless \(U\) is real valued and nonconstant. More explicitly,
\(\partial_{\bar z}U=\tfrac12(\partial_x+i\partial_y)U=(-x-iy/2)U\), which is nonzero at \(z=1\). It is not entire. Every transform in Theorem E is entire, including tempered inputs, so none of the three image characterizations can omit that hypothesis.

**Solution 8.** Define
\(A_N(U)=\sup_z(1+|z|)^N|U(z)|e^{-\Phi(z)}\)
and \(p_{\alpha,\gamma}(u)=\sup_y|y^\alpha\partial_y^\gamma u(y)|\).
The absolute inverse formula and the kernel estimate (E13), with the real linear norm equivalence, give
\[
\begin{gathered}
p_{\alpha,\gamma}(u)\\
\leq C_{\alpha,\gamma}A_N(U)\\
\int_{\mathbb C^n}(1+|z|)^{|\alpha|+|\gamma|-N}dL(z).
\end{gathered}
\]
The integral is finite for any integer \(N>|\alpha|+|\gamma|+2n\). This proves the quantitative inverse bound; the forward finite-seminorm estimates (E16) prove continuity in the other direction.

Now suppose all entire \(U_j\) satisfy
\(|U_j(z)|e^{-\Phi(z)}\leq C(1+|z|)^M\), with one \(C,M\). If \(U_j\to U\) locally uniformly, the iterated Cauchy formula proves that \(U\) is entire, and the same bound passes pointwise to \(U\). Formula (E7) and the rapid normalized decay of \(T\overline\psi\) give an integrable majorant independent of \(j\) for every Schwartz test. Dominated convergence proves \(u_j\to u\) weakly in \(\mathcal S'\), where \(Tu=U\).

Conversely assume \(u_j\to u\) weakly, retaining the same uniform output-growth bound. Each fixed original Gaussian kernel is a Schwartz test, so \(U_j(z)\to Tu(z)\) pointwise. Formula (E7), bounded by the common polynomial majorant and (E16), also supplies one fixed finite sum of test seminorms controlling every \(u_j\). On a compact complex set, the first complex derivatives of the original kernel have uniformly bounded values in those seminorms. Differentiating the kernel action therefore bounds every first derivative of \(U_j\) uniformly there. On a slightly larger compact polydisk neighborhood these derivative bounds imply a common modulus of continuity on the initial compact set by line segments in finitely many covering disks. The continuous limit \(Tu\) has such a modulus too. A finite sufficiently fine net, pointwise convergence at its points and these two moduli prove uniform convergence on that compact set. Hence \(U_j\to Tu\) locally uniformly, and the common growth bound passes to \(Tu\). The conclusion concerns sequences under the explicit uniform-growth condition; it makes no unrestricted assertion about an unspecified topology on all growth classes.

**Solution 9.** On any bounded complex set of \(t,z\), every differentiated generating integrand is bounded by a constant times a polynomial in \(|y|\) times \(e^{-y^2+C|y|}\), which is integrable. Differentiation under the integral is therefore valid for every order. Using the whole complex Gaussian integral gives
\[
\begin{gathered}
\mathcal B(g_0e^{2ty-t^2})(z)\\
=\pi^{-1}e^{-z^2/2-t^2}\\
{}\cdot\int e^{-y^2+(\sqrt2z+2t)y}dy\\
=\pi^{-1/2}e^{\sqrt2zt},\\
\mathcal B g_m(z)=\frac{z^m}{\sqrt\pi\sqrt{m!}}.
\end{gathered}
\tag{B11}
\]
Taking the \(m\)-th derivative at \(t=0\) yields
\(\mathcal B(H_mg_0)=\pi^{-1/2}(\sqrt2z)^m\), proving the last formula. Each input is a real polynomial times a Gaussian, hence Schwartz; the same conclusion follows from the output's rapid normalized modulus.

Put \(e_m(z)=z^m/(\sqrt\pi\sqrt{m!})\). The angular foundation, A4 and (A16), gives the exact polar measure \(r\,dr\,d\theta\) for \(z=re^{i\theta}\). Its use here is legitimate: the absolute integrand is a fixed polynomial in \(r\) times \(e^{-r^2}\), hence integrable by the Gaussian estimates. For \(m\ne k\), angular integration of \(e^{i(m-k)\theta}\) is zero by its antiderivative and the period \(2\pi\). For \(m=k\) its value is \(2\pi\), and
\(\int_0^\infty r^{2m+1}e^{-r^2}dr=m!/2\): set \(v=r^2\) and integrate \(\int_0^\infty v^m e^{-v}dv\) by parts \(m\) times, with vanishing endpoints. Thus
\[
\begin{gathered}
\int_{\mathbb C}e_m(z)\overline{e_k(z)}e^{-|z|^2}dx\,d\eta\\
=\delta_{mk},\\
\left\|\sum_{m=0}^L b_m g_m\right\|_2^2
=\sum_{m=0}^L|b_m|^2.
\end{gathered}
\tag{B12}
\]
The norm conclusion uses the already proved unitary map in Theorem E. This establishes the whole finite orthogonality claim without an infinite basis assumption.

For Schwartz input, differentiating (B2) gives
\(\partial_z\mathcal Bu=-z\mathcal Bu+\sqrt2\mathcal B(yu)\). Integration by parts in the real variable gives
\(\mathcal B(\partial_yu)=\mathcal B(yu)-\sqrt2z\mathcal Bu\), since the kernel's derivative is \((\sqrt2z-y)\) times itself. Every boundary term vanishes by Gaussian decay and the Schwartz bounds. Combining these two identities proves
\[
\begin{gathered}
\mathcal B\bigl((y+\partial_y)u/\sqrt2\bigr)
=\partial_z\mathcal Bu,\\
\mathcal B\bigl((y-\partial_y)u/\sqrt2\bigr)
=z\mathcal Bu.
\end{gathered}
\tag{B13}
\]
They hold on tempered inputs as well, by the same identities of Schwartz kernels and the definition of distributional differentiation. In particular, differentiating \(e_m\) gives \(\sqrt m\,e_{m-1}\), with zero at \(m=0\), and multiplying it by \(z\) gives \(\sqrt{m+1}\,e_{m+1}\). Injectivity gives the corresponding input relations. Both signs follow from the actual positive cross term \(\sqrt2zy\).

**Solution 10.** Completing the real square in the product of the two inputs gives
\[
\begin{gathered}
\langle g_{a,p},g_{b,q}\rangle\\
=e^{-\frac{(a-b)^2}4-\frac{(p-q)^2}4}
e^{\frac{i(p-q)(a+b)}2},\\
\|\alpha g_{a,p}+\beta g_{b,q}\|_2^2\\
=|\alpha|^2+|\beta|^2\\
{}+2\operatorname{Re}
\bigl(\alpha\overline\beta\langle g_{a,p},g_{b,q}\rangle\bigr).
\end{gathered}
\tag{B14}
\]
Indeed the combined real exponent is
\(-(y-(a+b)/2)^2-(a-b)^2/4\). The remaining Gaussian Fourier integral at frequency \(p-q\) contributes
\(e^{-(p-q)^2/4+i(p-q)(a+b)/2}\). This also computes the output weighted inner product by Theorem E. The interference term depends on the full complex phase, so the two energy densities by themselves do not determine the norm of the superposition.

For \(a>0\) the overlap of \(g_{a,0}\) and \(g_{-a,0}\) is \(e^{-a^2}\). Consequently the unit vector and its transform are
\[
\begin{gathered}
v_a=\frac{g_{a,0}-g_{-a,0}}
{\sqrt{2(1-e^{-a^2})}},\\
\mathcal Bv_a(z)\\
=\frac{\sqrt2\,e^{-a^2/4}}
{\sqrt\pi\sqrt{1-e^{-a^2}}}\\
{}\cdot\sinh(az/\sqrt2).
\end{gathered}
\tag{B15}
\]
The denominator is positive. From Solution 9, \(g_1=\sqrt2y g_0\) has norm one. The same Gaussian square gives
\(\langle g_{a,0},g_1\rangle=(a/\sqrt2)e^{-a^2/4}\), by integrating the Gaussian's mean \(a/2\). The overlap for \(-a\) changes sign, hence
\[
\begin{gathered}
\langle v_a,g_1\rangle\\
=\frac{a e^{-a^2/4}}{\sqrt{1-e^{-a^2}}}
\longrightarrow1,\\
\|v_a-g_1\|_2^2\\
=2-2\langle v_a,g_1\rangle
\longrightarrow0.
\end{gathered}
\tag{B16}
\]
The scalar limit uses \((1-e^{-a^2})/a^2\to1\). It proves convergence in the full input norm, rather than only pointwise after dividing by a small denominator. Unitarity also gives convergence in the output norm. Finally, for any compact \(K\subset\mathbb C\), (B5) gives
\[
\begin{gathered}
\sup_{z\in K}|\mathcal Bv_a(z)-z/\sqrt\pi|\\
\leq\pi^{-1/2}e^{\max_K|z|^2/2}\|v_a-g_1\|_2\\
\longrightarrow0.
\end{gathered}
\tag{B17}
\]
This proves the requested locally uniform convergence with the exact limiting output. The zero unnormalized difference at \(a=0\) becomes a nonzero first Gaussian level after the stated normalization and limit.

**Solution 11.** Let
\(F_z(y)=e^{-z^2/2+\sqrt2zy-y^2/2}\). Its translation quotient is the entire identity
\[
\frac{F_z(y+t)}{F_z(y)}
=e^{t(\sqrt2z-y)-t^2/2}.
\tag{B18}
\]
The generating function therefore gives
\(\partial_y^mF_z(y)=\mathrm{He}_m(\sqrt2z-y)F_z(y)\).
It also gives
\(\mathrm{He}_m(-w)=(-1)^m\mathrm{He}_m(w)\) by replacing \(t\) with \(-t\). The sign \((-1)^m\) in the action of \(\partial_y^m\delta_a\) then cancels this parity sign. Thus, with the whole polynomial
\(P(w)=\sum_{m=0}^M d_m\mathrm{He}_m(w)\),
\[
\begin{gathered}
\mathcal Bu(z)\\
=\pi^{-3/4}P(a-\sqrt2z)\\
{}\cdot e^{-z^2/2+\sqrt2az-a^2/2},\\
m_{\mathcal Bu}(x+i\eta)\\
=\pi^{-3/4}|P(a-\sqrt2z)|\\
{}\cdot e^{-(\sqrt2x-a)^2/2}.
\end{gathered}
\tag{B19}
\]
The generating function shows that \(\mathrm{He}_m\) is monic of degree \(m\). Hence \(P\) has degree exactly \(M\), leading coefficient \(d_M\), and
\(|P(a-\sqrt2z)|\leq C(1+|z|)^M\). Since the Gaussian factor is at most one, this proves normalized growth order at most \(M\).

On \(x=a/\sqrt2\), the polynomial argument is \(-i\sqrt2\eta\). Its nonzero leading coefficient gives
\[
\begin{gathered}
\lim_{|\eta|\to\infty}
\frac{m_{\mathcal Bu}(a/\sqrt2+i\eta)}{|\eta|^M}\\
=\pi^{-3/4}|d_M|2^{M/2}>0.
\end{gathered}
\tag{B20}
\]
For \(M=0\), the denominator is one. Thus no smaller nonnegative integer growth allowance works when \(M>0\), and bounded order zero is exact when \(M=0\). The same line disproves rapid decay in every case: the modulus stays nonzero or grows there as \(|z|\) tends to infinity.

To prove infinite energy one needs a strip, not merely a line of area zero. On \(|x-a/\sqrt2|\leq1\), the coefficients below the \(\eta^M\) term in \(P(a-\sqrt2x-i\sqrt2\eta)\) are bounded uniformly in \(x\). The leading term is always \(d_M(-i\sqrt2\eta)^M\). For a sufficiently large fixed \(L\), it follows that
\(|P(a-\sqrt2z)|\geq c_0(1+|\eta|)^M\) throughout that strip with \(|\eta|\geq L\), for some \(c_0>0\). This statement also holds for the nonzero constant polynomial when \(M=0\). The Gaussian squared factor on the strip is at least \(e^{-2}\). Therefore
\[
\begin{gathered}
\int_{\mathbb C}|\mathcal Bu(z)|^2e^{-|z|^2}dx\,d\eta\\
\geq2\pi^{-3/2}e^{-2}c_0^2\\
{}\cdot\int_{|\eta|\geq L}(1+|\eta|)^{2M}d\eta
=\infty.
\end{gathered}
\tag{B21}
\]
Each derivative of a point mass is a continuous Schwartz functional because evaluation of the indicated derivative at \(a\) is bounded by a Schwartz seminorm. Their finite sum is therefore tempered. The output is entire, has the exact polynomial normalized order proved above, and belongs to neither the Hilbert nor the Schwartz image. All conclusions follow from actual distributional kernel actions and from the full image theorem.

## References

- [Gaussian norms and entire uncertainty](gaussian-norms-and-entire-uncertainty.md), Lemma 0.1, Theorem D and Solution 1: positive roots, the full arbitrary-positive-matrix norm converse and inverse-order comparison. [Fourier–Laplace slices and boundary poles](fourier-laplace-slices-and-boundary-poles.md), Lemma 0.1 and Lemma L, supplies the completed Fourier and slice inputs.
- [Point sources and complex Gaussian kernels](point-sources-and-complex-gaussian-kernels.md), Lemma 2.1 and Theorem 3.1: the actual determinant branch and complex-matrix transform. Lemma 0.1 here extends the formula to every complex frequency with explicit convergence bounds.
- Supplied [Fourier](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F1–F5, [integration](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.0–15.4 and 16, [scalar](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13, [finite-algebra](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §§10.1–10.6, and [angular](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A4 and (A16), foundations. These supplied proofs retain their stated licences. The reconstruction proof above supplies its own passage through a tempered functional by compact Riemann sums and seminorm tail bounds.
- [Cauchy kernels and distributional boundary limits](cauchy-kernels-and-boundary-limits.md), Corollary 2.2, and [Holomorphic boundaries in convex cones](holomorphic-boundaries-in-convex-cones.md), Section 3 and Lemma 3.1: the exact Cauchy, power-series and identity arguments used here.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, reprint of the second edition (1990), Exercise 7.4.5 and its answer on page 415, including the Schwartz and tempered image assertions. The full reconstruction, topology, regularization and eleven graded problems here are independently expressed and proved.
- Michael Hitrik and Johannes Sjöstrand, [*Two minicourses on analytic microlocal analysis*](https://arxiv.org/abs/1508.00649v1), Chapter 1, §1.3, Definition 1.3.1, Theorem 1.3.3 and Proposition 1.3.4. The quadratic phase conditions, maximizing weight and unitary normalization give a freely accessible comparison. In their reduced phase, their cross-term matrix \(A\) is our \(B\), their positive matrix \(B\) is our \(Q\), and we set \(h=1\). The complete Schwartz and tempered characterizations, reconstruction arguments and worked measurements are proved in this lesson.
