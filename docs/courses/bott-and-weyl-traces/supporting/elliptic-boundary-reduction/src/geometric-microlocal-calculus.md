# Detecting regularity without choosing coordinates

An operator has two kinds of locality. Its kernel determines which input points can influence an output point. Its symbol determines which cotangent directions can carry an irregularity. We construct these two structures together, then use them to measure regularity of sections of arbitrary finite-rank complex bundles. All manifolds below are Hausdorff, second countable, smooth, and without boundary; compactness is imposed only where stated.

The analytic inputs are [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), Sections2–5 and8–9, and [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md), Sections7–8. The convention is \(D=-i\partial\), with inverse Fourier factor \((2\pi)^{-n}\). Local symbols have estimates on each compact base set, with no uniformity across a noncompact manifold. Unless parameters are displayed, \(S^m=S^m_{1,0}\) and \(\Psi^m=\Psi^m_{1,0}\).

The geometric construction uses the following analytic facts. **Distributions and kernels** supplies distributions as continuous functionals on compact smooth densities, their restriction and multiplication by smooth functions, tensor products, Fourier transformation, the finite-order estimate on compact supports, and the scalar Schwartz kernel theorem for continuous \(C_c^\infty(U)\to\mathcal D'(V)\) maps on Euclidean open sets. The kernel theorem includes its identification with separately continuous bilinear test pairings, jointly continuous on every pair of fixed compact-support test spaces; Sections 13.1–13.6 prove this scalar theorem, its fixed-support joint estimates, and continuity into the strong distribution dual, together with the exact elementary distribution operations. The test spaces carry their usual smooth Fréchet topologies at fixed support and their inductive-limit topology over supports; distributions carry the strong dual topology. **Manifolds and bundles** supplies smooth atlases, the chain rule, inverse function theorem, locally finite smooth partitions of unity with compact supports subordinate to open covers, and finite-rank bundle gluing. **Uniform boundedness** and the closed graph theorem are proved in Sections 14.1–14.6 of [Banach estimates, quotient spaces and compact parameter arguments](banach-foundation-bridges.md). Those sections prove completeness of the exact fixed-support smooth test spaces and smooth output spaces, a common finite-order estimate for arbitrary pointwise bounded functional families, and the closed graph theorem between Fréchet spaces, including a Banach domain. Lebesgue change of variables, Fubini, dominated convergence, and Fourier inversion/Plancherel have the same exact entry contracts as [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md). We prove the geometric kernel adapter and the wavefront results used below; no general theorem about multiplying arbitrary distributions is assumed.

## 1. Local estimates and amplitude reduction

For an open set \(U\subset\mathbb R^n\), \(a\in S^m_{\rho,\delta}(U\times\mathbb R^n)\) means that
\[
\sup_{x\in K,\xi}\langle\xi\rangle^{-m+\rho|\alpha|-\delta|\beta|}
|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|<\infty
\quad(K\Subset U),
\qquad 0<\rho\leq1,\quad0\leq\delta<1.
\tag{G1}
\]
These seminorms define the local Fréchet topology, using a compact exhaustion. On an open conic set \(\mathcal C\subset U\times(\mathbb R^n\setminus0)\), the same estimates are required along \((x,t\xi)\), \(t\geq1\), for every compact subset of \(\mathcal C\). They make no assertion about approaching the zero section outside such compact sets. A symbol defined at all frequencies must also be smooth there.

Local asymptotic summation follows with support control. Given \(a_j\) of orders \(m_j\to-\infty\), take a locally finite partition \(\theta_l\) of the base, or of a relatively compact angular/base cover in the conic case. Apply Section 2 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) to each compactly supported piece \(\theta_l a_j\), extended into its coordinate product by zero, obtaining \(b_l\) with support contained in \(\bigcup_j\operatorname{supp}(\theta_l a_j)\). Then \(b=\sum_l b_l\) is locally finite. On each fixed compact set only finitely many \(l\) occur, so every remainder satisfies (G1) of order \(M_k=\max_{j\geq k}m_j\). The support assertion survives the locally finite sum. On a conic cover the cutoffs are homogeneous of degree zero above a fixed frequency; the bounded-frequency discrepancy is smooth and irrelevant to asymptotic orders. Differences of two sums are of every negative order. This also proves continuity of restrictions and the local form of the symbol recognition statement in Section 2 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md).

We need an amplitude version of the Euclidean calculus. Suppose \(c(z,w,\eta)\), compactly supported in \((z,w)\), has estimates
\[
|\partial_\eta^\alpha\partial_z^\beta\partial_w^\gamma c|
\leq C_{\alpha\beta\gamma}
\langle\eta\rangle^{m-\rho|\alpha|+\delta|\beta|+d|\gamma|},
\qquad 0\leq d\leq\rho,\quad d<1.
\tag{G2}
\]
The kernel \((2\pi)^{-n}\int e^{i(z-w)\cdot\eta}c(z,w,\eta)\,d\eta\) has a left symbol
\[
b(z,\xi)=\left[e^{iD_w\cdot D_\eta}c(z,w,\eta)\right]_{w=z,\eta=\xi}.
\tag{G3}
\]
When \(d\leq\delta\) and \(\delta\leq\rho\), it belongs to \(S^m_{\rho,\delta}\). More precisely its remainder after \(|\alpha|<N\) is
\[
b-\sum_{|\alpha|<N}\frac{\partial_\eta^\alpha D_w^\alpha c(z,z,\xi)}{\alpha!}
\in S^{m-N(\rho-d)}_{\rho,\delta}.
\tag{G4}
\]
Every seminorm uses finitely many constants in (G2), and the bound remains valid at \(d=\rho\), where it gives no order gain.

Here are the estimates behind this adapter. For fixed \(z\), apply Section 8 of [Quadratic Fourier multipliers at a moving scale](gauss-transform-estimates.md) with the metric
\(g_{(w,\eta)}(v,\nu)=\langle\eta\rangle^{2d}|v|^2+\langle\eta\rangle^{-2\rho}|\nu|^2\)
and weight \(\langle\eta\rangle^m\). Its slow variation and temperateness are exactly the parameter verification in Section 4 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), with \(\delta\) there replaced by \(d\); its quadratic parameter is \(\frac12\langle\eta\rangle^{d-\rho}\). The theorem gives (G4) before restricting \(w=z\). Differentiate in \(z\) first, using the modified weight \(\langle\eta\rangle^{m+\delta|\beta|}\), and in \(w,\eta\) using their exact modified weights. Differentiation after the diagonal restriction is a sum of these derivatives. Since \(d\leq\delta\), each total base derivative costs at most \(\delta\). This proves all of (G1), including the remainder, rather than just a bound for values. Regularize \(c\) in all variables by cutoffs tending to one. Formula (G3) for the regularized kernels follows by Fourier inversion: the multiplier \(e^{i\omega\cdot\theta}\) becomes the kernel \((2\pi)^{-n}e^{-i(w-z)\cdot(\eta-\xi)}\). The Gauss bounds and distributional continuity identify the limits. They also justify all parameter derivatives. Thus no stationary phase theorem is hidden in (G3).

## 2. Kernels, exponential tests, and coordinate transport

For a global symbol \(a\in S^m\), its kernel is
\[
K_a(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a(x,\xi)\,d\xi.
\tag{G5}
\]
It is \(C^j\) if \(m+j+n<0\). Indeed, differentiating a total of at most \(j\) times gives finitely many integrands bounded by \(C\langle\xi\rangle^{m+j}\); these are integrable under the strict inequality, uniformly on compact sets. Dominated convergence gives the claimed derivatives. Off the diagonal, apply
\(e^{i(x-y)\xi}=|x-y|^{-2L}(-\Delta_\xi)^L e^{i(x-y)\xi}\), integrate by parts in frequency, and take \(2L>m+j+n\). The coefficients and their derivatives are bounded on every compact set separated from the diagonal, giving smoothness there. For the parameters in (G1), frequency differentiation instead gains \(\rho\) per derivative; sufficiently many integrations still prove off-diagonal smoothness.

An order-minus-infinity symbol maps \(\mathcal S'\) into \(C^\infty\), although its output need not decrease at spatial infinity. At fixed \(x\), the differentiated expression \(\partial_x^\beta(e^{ix\cdot\xi}a(x,\xi))\) is a Schwartz function of \(\xi\), smoothly depending on \(x\) in that topology. Pair it with \(\widehat u\). The compact-uniform Schwartz seminorms justify all output derivatives and continuity. The same reasoning applies to local smoothing symbols on every compact output set.

Exponential functions recover a symbol without being test functions:
\[
\operatorname{Op}(a)(e^{ix\cdot\xi}u)
=e^{ix\cdot\xi}a(x,D+\xi)u,
\qquad
\operatorname{Op}(a)e^{ix\cdot\xi}=e^{ix\cdot\xi}a(x,\xi).
\tag{G6}
\]
The first identity follows by the Fourier translation rule on \(\mathcal S\), then on \(\mathcal S'\) by the continuous extensions in Section 5 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md). For the second, choose \(v\in\mathcal S\) with \(\widehat v\in C_c^\infty\) and \(v(0)=1\). The functions \(v(\varepsilon x)\) tend to one in \(\mathcal S'\): multiply a Schwartz test function by their bounded pointwise differences and use dominated convergence. The integrand \(a(x,\xi+\varepsilon\theta)e^{i\varepsilon x\theta}\widehat v(\theta)\) must retain the inverse Fourier factor. The exact identity is
\[
 e^{-ix\cdot\xi}\operatorname{Op}(a)
       (e^{i(\cdot)\cdot\xi}v(\varepsilon\cdot))(x)
 =(2\pi)^{-n}\int a(x,\xi+\varepsilon\theta)
                e^{i\varepsilon x\cdot\theta}\widehat v(\theta)\,d\theta
 \longrightarrow a(x,\xi),\qquad
 (2\pi)^{-n}\int\widehat v(\theta)\,d\theta=v(0)=1.
 \tag{G6a}
\]
Compact support of \(\widehat v\) permits every derivative limit on compact base sets. Derivatives falling on the exponential retain their powers of \(\varepsilon\theta\); the limit with no such derivative is the corresponding derivative of \(a(x,\xi)\) times the displayed mass one. Without the factor, even \(a=1\) would give the limit \((2\pi)^n\), not one. This proves (G6) with its distributional meaning.

Let \(\kappa:U\to V\) be a smooth diffeomorphism and suppose that \(\operatorname{Op}(a)\) has compact kernel support inside \(U\times U\). Define its transport on functions by
\[
A_\kappa f=(A(f\circ\kappa))\circ\kappa^{-1}.
\tag{G7}
\]
It has compact kernel support in \(V\times V\). For \(1-\rho\leq\delta\leq\rho\), \(a\in S^m_{\rho,\delta}\) implies \(A_\kappa=\operatorname{Op}(a_\kappa)\) with a global \(S^m_{\rho,\delta}\) symbol, zero outside a compact subset of \(V\) in its base variable. In particular the allowed range has \(\rho\geq\frac12\), and \(\rho=\frac12\) forces \(\delta=\frac12\).

**Proof with the Jacobians retained.** Cut the kernel into a part sufficiently close to the diagonal and a smooth compact remainder. The latter has a smoothing symbol by Fourier transformation in \(x-y\). For the first part use small convex coordinate neighborhoods and write
\[
\kappa(x)-\kappa(y)=L(x,y)(x-y),\qquad
L(x,y)=\int_0^1\kappa'(y+t(x-y))\,dt.
\tag{G8}
\]
After shrinking the neighborhoods, \(L\) is invertible with all derivatives bounded, as are those of its inverse. Put \(z=\kappa(x),w=\kappa(y)\), and change frequency by \(\xi=L(x,y)^T\eta\). The transported amplitude is
\[
c(z,w,\eta)=\chi(x,y)a(x,L(x,y)^T\eta)
\frac{|\det L(x,y)|}{|\det\kappa'(y)|},
\tag{G9}
\]
where \(\chi=1\) near the relevant diagonal. On that diagonal the determinant ratio is one. Differentiating a frequency-linear argument once in \(x\) or \(y\) introduces a factor \(O(|\eta|)\) and one frequency derivative of \(a\), hence costs \(1-\rho\). A direct base derivative of \(a\) costs \(\delta\). Repeated chain and product rules therefore give (G2) with \(d=1-\rho\) for the \(w\) derivatives and with \(\delta\) for the \(z\) derivatives, because \(1-\rho\leq\delta\). Ordinary derivatives of the cutoff and determinants cost zero. Compact-set norm comparability \(\langle L^T\eta\rangle\asymp\langle\eta\rangle\) controls every real order. Apply (G3). A finite cover of the compact diagonal part completes the proof, including \(\rho=\delta=\frac12\). ∎

This chain-rule argument also proves a useful symbol pullback statement. If \(F(x,\xi)=(f(x),M(x)\xi)\), with smooth \(f\), smooth invertible \(M\), and \(F(\mathcal C_1)\subset\mathcal C_2\), then \(F^*:S^m_{\rho,\delta}(\mathcal C_2)\to S^m_{\rho,\delta}(\mathcal C_1)\) is continuous when \(1-\rho\leq\delta\). For a compact ray generator its image is compact; the smallest and largest singular values of \(M\) have positive finite bounds. Every chain-rule term has the required derivative budget, exactly as in (G9). No assumption that \(f\) is a diffeomorphism is needed for this symbol statement.

For the classical class the full coordinate expansion is
\[
a_\kappa(\kappa(x),\eta)
\sim\sum_\alpha\frac{\partial_\xi^\alpha a(x,\kappa'(x)^T\eta)}{\alpha!}
\left.D_y^\alpha e^{i r_x(y)\cdot\eta}\right|_{y=x},
\quad
r_x(y)=\kappa(y)-\kappa(x)-\kappa'(x)(y-x).
\tag{G10}
\]
The exact value before expansion is \(e^{-i\kappa(x)\cdot\eta}A(e^{i\kappa(\cdot)\cdot\eta})(x)\); a cutoff equal to one near the compact kernel support makes this input unambiguous. In (G10) the second factor is a polynomial in \(\eta\) of degree at most \(\lfloor|\alpha|/2\rfloor\): every factor \(\eta\) comes with a derivative of \(r_x\), and its value survives at \(y=x\) only after at least two derivatives. The factors for \(|\alpha|=0,1\) are respectively one and zero. Consequently the term has order at most \(m-|\alpha|/2\).

For completeness, the coefficients and the remainder can be checked without assuming that the exponential has small derivatives. Expand (G3) to arbitrary order using (G4) applied to (G9). Each coefficient is a finite linear combination of frequency derivatives of \(a\), evaluated at \(\kappa'(x)^T\eta\), with polynomial coefficients in \(\eta\) and jets of \(\kappa\). To identify these finite-jet expressions, take \(a\) to be a polynomial in frequency with arbitrary coefficients at the fixed base point. Then \(A=a(x,D)\) is a differential operator and the product rule applied to
\(e^{i\kappa(y)\cdot\eta}=e^{i\kappa(x)\cdot\eta}e^{i(y-x)\cdot\kappa'(x)^T\eta}e^{ir_x(y)\cdot\eta}\)
gives precisely (G10). Polynomial jets span every finite jet space, so these identities identify the coefficients for an arbitrary smooth symbol as well. Sorting the finite expressions by the number of frequency derivatives minus their polynomial degree is legitimate: only finitely many terms have this number below any prescribed bound. The discarded amplitude remainder after sufficiently many terms of (G4) and the discarded coefficient terms both have arbitrarily low order. Thus truncating (G10) at \(|\alpha|<2N\) has remainder in \(S^{m-N}\); the same proof applies after any prescribed derivatives.

When \(1-\rho\leq\delta<\rho\), the same formula is an asymptotic series in \(S_{\rho,\delta}\). The term with index \(\alpha\) has order at most \(m-\rho|\alpha|+\lfloor|\alpha|/2\rfloor\). Using (G4) with \(d=1-\rho\), truncation at \(|\alpha|<2N\) has remainder in \(S^{m-N(2\rho-1)}_{\rho,\delta}\), hence also in \(S^{m-N(\rho-\delta)}_{\rho,\delta}\). The parameter \(2\rho-1\) is positive in this strict range. The equality-case invariance already proved uses (G3), and does not rely on a decreasing-order series or imply an elliptic inverse theorem at \(\delta=\rho\).

## 3. The second symbol term and the density it measures

Equation (G10) first gives
\(a_\kappa(\kappa(x),\eta)-a(x,\kappa'(x)^T\eta)\in S^{m-1}\).
Suppose that \(a\sim a_m+a_{m-1}+\cdots\) is classical with step one. Define
\[
s(a)=a_{m-1}+\frac{i}{2}\sum_j\partial_{x_j}\partial_{\xi_j}a_m.
\tag{G11}
\]
For operators on functions, this is generally not a scalar on the cotangent bundle. If \(J=|\det\kappa'|\), then
\[
s(a_\kappa)(\kappa(x),\eta)
=s(a)(x,\kappa'(x)^T\eta)
-\frac12\sum_j(\partial_{\xi_j}a_m)(x,\kappa'(x)^T\eta)
\frac{D_{x_j}J}{J}.
\tag{G12}
\]
Here is an index verification of the correction. Write \(M_{kj}=\partial_j\kappa_k\), \(N=M^{-1}\), and \(\xi=M^T\eta\). The order-\(m-1\) term added by (G10) is
\(-\frac i2\sum_{j,l,k}(\partial_{\xi_j}\partial_{\xi_l}a_m)\,\eta_k\partial_j\partial_l\kappa_k\).
In \(\sum_k\partial_{z_k}\partial_{\eta_k}[a_m(x,M^T\eta)]\), the chain rule produces \(\sum_j\partial_{x_j}\partial_{\xi_j}a_m\), the same Hessian term with coefficient \(+1\), and
\(\sum_{j,k,l}N_{lk}(\partial_lM_{kj})\partial_{\xi_j}a_m\).
The Hessian terms cancel after multiplication by \(i/2\). Since mixed derivatives commute,
\(\sum_{k,l}N_{lk}\partial_lM_{kj}=\sum_{k,l}N_{lk}\partial_jM_{kl}=\partial_j\log J\),
by the determinant derivative formula. The remainder is \((i/2)\sum_j\partial_{\xi_j}a_m\,\partial_j\log J\), which is (G12). Orientation reversal changes the sign of \(\det M\) only by a locally constant factor, so its logarithmic derivative is that of \(J\).

The density line bundle \(\Omega\) has local generator \(|dx|\). For any \(z\in\mathbb C\), define \(\Omega^z\) using positive Jacobians raised to \(z\): \(t^z=e^{z\log t}\) for \(t>0\). The real logarithm makes \((t_1t_2)^z=t_1^zt_2^z\), proving the cocycle relation, including complex exponents. Components transform by
\(u_\kappa(\kappa(x))=J(x)^{-z}u(x)\).
Thus an operator on \(z\)-densities is transported as the function operator conjugated in the old coordinates by \(J^{-z}AJ^z\). Its symbol differs from \(a\), modulo \(S^{m-2}\), by
\[
z\sum_j\partial_{\xi_j}a\,\frac{D_jJ}{J}.
\tag{G13}
\]
Indeed Section 5 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) applied to multiplication by \(J^z\) gives \(J^{-z}(aJ^z+\sum_j\partial_{\xi_j}a D_jJ^z)\) through the first correction; all higher frequency derivatives have order at most \(m-2\). The identity \(D_jJ^z=zJ^zD_jJ/J\) proves (G13). At \(z=\frac12\) it cancels (G12).

There is a version without homogeneity. For scalar half-density operators, the local quantity
\[
\sigma_{[2]}(A)=a+\frac i2\sum_j\partial_{x_j}\partial_{\xi_j}a
\pmod {S^{m-2}}
\tag{G14}
\]
agrees on overlaps as a scalar symbol class on \(T^*X\). Repeat the preceding calculation with \(a\) in place of \(a_m\): omitted terms contain at least two net frequency losses, so they are of order \(m-2\). A partition of unity patches the local quantities to a global symbol, and any two patches differ by \(S^{m-2}\) because they agree in each chart modulo that space. Its homogeneous term of degree \(m-1\), when present, is (G11). Formula (G12) also shows invariance for function operators at double zeros of \(a_m\), and under transformations with locally constant Jacobian. The refined assertion (G14) is specifically for scalar half-densities; a varying vector-bundle frame introduces its own first-order correction.

## 4. Assembling an operator and its principal symbol

Let \(A:C_c^\infty(U)\to C^\infty(U)\) be continuous. Suppose \(\phi A\psi\) is the global quantization of an \(S^m\) symbol for every \(\phi,\psi\in C_c^\infty(U)\). Then
\[
A=\operatorname{Op}(a)+R,\qquad a\in S^m(U\times\mathbb R^n),
\qquad K_R\in C^\infty(U\times U).
\tag{G15}
\]
The symbol is unique modulo local \(S^{-\infty}\).

To prove this, choose a locally finite smooth partition \(\theta_j\) with compact supports. Compactness and local finiteness imply that each support meets only finitely many others. Let \(a_{jk}\) be the symbol of \(\theta_jA\theta_k\). By (G6) it vanishes in the base variable outside \(\operatorname{supp}\theta_j\). Sum \(a_{jk}\) only for intersecting pairs of supports. The sum is locally finite in the base, and on a fixed compact set the finitely many symbols satisfy the required bounds. The kernel difference is the locally finite sum
\(\sum'\theta_j(x)K_A(x,y)\theta_k(y)\) over disjoint pairs. Each term is smooth by (G5); this proves (G15). If a compactly supported smooth kernel is given, its left symbol is its Fourier transform in \(y\) after multiplication by \(e^{-ix\cdot\xi}\). Integrating by parts in \(y\), and differentiating in \(x,\xi\), proves every smoothing seminorm. Apply this to \(\phi(A-\operatorname{Op}(a))\psi\), with \(\psi=1\) near \(\operatorname{supp}\phi\). The symbol of \(\phi\operatorname{Op}(a)(1-\psi)\) is smoothing by off-diagonal integration by parts; hence local uniqueness follows. Conversely the symbol and smooth kernel in (G15) clearly satisfy the localized hypothesis.

Define \(\Psi^m(X)\) by this localized condition in coordinate charts, together with smoothness of the kernel off the diagonal. Equivalently one can impose the localized condition in every chart and for every pair of compact cutoffs: that condition already implies off-diagonal smoothness. One atlas suffices if off-diagonal smoothness is included. To verify this, localize a kernel near any diagonal point and transport its compact localization by (G7)–(G10); the remainder in (G15) stays smooth under a diffeomorphism. Away from the diagonal the assumed smoothness handles pairs of different charts. The kernel is a distributional density in its input variable, so it is intrinsically a section with coefficients in \(1\boxtimes\Omega\), not a scalar function on \(X\times X\).

The fiber-linear pullback proved in Section 2 defines \(S^m(T^*X)\) independently of charts. Local principal symbols patch and give
\[
\Psi^m(X)/\Psi^{m-1}(X)
\simeq S^m(T^*X)/S^{m-1}(T^*X).
\tag{G16}
\]
For existence, take real compact smooth \(\theta_j\) subordinate to charts with \(\sum_j\theta_j^2=1\), and a cutoff \(\psi_j=1\) near \(\operatorname{supp}\theta_j\). Quantize a given cotangent symbol in each chart as \(A_j=\theta_j\operatorname{Op}(\psi_j a_j)\theta_j\), transporting back and extending by zero. The sum is locally finite and properly supported: over a fixed compact set only finitely many \(\operatorname{supp}\theta_j\) occur in either projection. Its principal symbol is \(\sum_j\theta_j^2a=a\). A square partition exists by dividing any nonnegative partition \(\chi_j\) by \((\sum_l\chi_l^2)^{1/2}\). On overlaps (G10) identifies principal classes. Their vanishing is equivalent in each local representation to order \(m-1\), proving the kernel of (G16) and injectivity. This also proves that \(\Psi^{-\infty}(X)\) is exactly the smooth-kernel class, by applying (G15) at every order and the integrability threshold of (G5).

## 5. Properness, products, and global summation

Write \(S=\operatorname{supp}K_A\subset X\times X\). The operator is **properly supported** if both projections \(S\to X\) are proper. For each compact \(K\subset X\), this says that there is a compact \(K'\) such that
\[
\operatorname{supp}u\subset K\ \Longrightarrow\ \operatorname{supp}Au\subset K',
\qquad
u=0\text{ near }K'\ \Longrightarrow\ Au=0\text{ near }K.
\tag{G17}
\]
The implications initially apply to test functions and then to the distributional extensions on their domains. Properness gives (G17) by the two kernel projections, enlarging the resulting compact sets to compact neighborhoods. Conversely, apply the support bounds to all test functions supported in a compact neighborhood of \(K\). If the kernel were nonzero outside the corresponding product set, its restriction to a small product of coordinate neighborhoods would pair nontrivially with some product of test functions, contradicting a support bound. Product test functions detect kernels by the scalar kernel theorem. Thus each projection has compact inverse images. This proves the equivalence, including the distinction between vanishing on a set and on a neighborhood used for distributions.

An arbitrary \(A\in\Psi^m\) extends continuously \(\mathcal E'(X)\to\mathcal D'(X)\): on each compact output set the local expression (G15) acts on compactly supported distributions by [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) and by pairing the smooth remainder. For a properly supported operator and arbitrary \(u\in\mathcal D'(X)\), define its output near a compact set \(K\) using \(A(\chi u)\), where \(\chi=1\) near the corresponding input compact set \(K'\). Formula (G17) proves independence of \(\chi\), and compatibility on overlapping output sets patches the result. Each output seminorm is controlled by finitely many input seminorms after this localization, proving continuity. Proper operators likewise map \(C^\infty\to C^\infty\), \(C_c^\infty\to C_c^\infty\), and \(\mathcal E'\to\mathcal E'\).

Every \(A\in\Psi^m\) is a properly supported operator plus a smooth-kernel operator. In the proof of (G15), retain only the intersecting partition pairs as an operator sum, now working intrinsically. The union of their compact kernel support rectangles has both projections proper, since each compact base set meets only finitely many partition supports and each such support has finitely many neighbors. The omitted terms are a locally finite smooth kernel. Equivalently this construction gives a smooth properly supported function on \(X\times X\), equal to one near the diagonal, by summing the retained products \(\theta_j(x)\theta_k(y)\). Multiplying any kernel by that function gives a common properness convention.

If \(A\in\Psi^m\) and \(B\in\Psi^{m'}\) are proper, then \(AB\in\Psi^{m+m'}\) is proper, and its principal symbol is \(\sigma_m(A)\sigma_{m'}(B)\), with the displayed order of factors. The relation \(S_A\circ S_B\) containing the product kernel support is closed and proper in both projections: above a compact output set the possible intermediate points lie in a compact set by properness of \(A\), and the possible input points then lie in a compact set by properness of \(B\). The same reasoning with the projections reversed proves the other direction, and these compactness statements prove closure by convergent subsequences.

For the local analytic assertion choose compact cutoffs \(\phi,\psi\) in a chart and \(\chi=1\) near both supports. Then
\(\phi AB\psi=(\phi A\chi)(\chi B\psi)+\phi A(1-\chi^2)B\psi\).
The first term is given by Section 5 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md). The second has a smooth kernel: properness confines its intermediate variable to a compact set, and the separated cutoffs make both factors smooth in the relevant external-variable neighborhoods. Differentiation under the compact integral, or action of a localized operator on a smooth kernel in one variable, proves every derivative. The same argument shows that smooth proper kernels form a two-sided ideal among proper pseudodifferential operators. It also covers products where the same support conditions make composition meaningful; we do not compose arbitrary nonproper operators on all distributions.

Finally let \(A_j\in\Psi^{m_j}(X)\), with \(m_j\) decreasing to \(-\infty\). There exists a proper \(A\in\Psi^{m_0}\) such that
\[
A-\sum_{j<k}A_j\in\Psi^{m_k}(X)\quad(k\geq0).
\tag{G18}
\]
First replace every \(A_j\) by a representative using the same proper kernel cutoff just constructed; this changes only smooth remainders. Choose a locally finite partition of a neighborhood of the diagonal by compact chart-product pieces. For each such piece, its localized kernel has a symbol of order \(m_j\) by (G3). Sum these symbols over \(j\) using Section 1, then quantize and multiply by a cutoff equal to one near the corresponding diagonal piece. The difference introduced by that last cutoff is smooth. Summing the pieces gives (G18), since any compact product meets finitely many pieces and hence every remainder is a finite sum of symbols of order \(m_k\) and smooth kernels. Apply the common proper cutoff once more. It does not change any quotient by smoothing, proving properness and all remainder claims. This argument uses local finiteness, not a finite atlas or a uniform geometry assumption.

## 6. Inverses with global and conic error control

A scalar \(A\in\Psi^m(X)\) is elliptic when its principal class in (G16) has an inverse of order \(-m\). In coordinates this is equivalent to a lower bound
\[
|a(x,\xi)|\geq c_K\langle\xi\rangle^m
\quad(x\in K,\ |\xi|\geq R_K)
\tag{G19}
\]
on each compact set. For a square matrix symbol, use its smallest singular value, or equivalently \(\|a^{-1}\|\leq C_K\langle\xi\rangle^{-m}\). The reciprocal estimates of Section 9 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) prove the implication from (G19) to an inverse class by taking local frequency cutoffs and patching. Conversely \(ab=1+r\), \(r\in S^{-1}\), gives \(|ab|\geq1/2\) above a compact-dependent radius and hence (G19). The same argument for square matrices uses the convergent finite-dimensional matrix Neumann series for \(I+r\).

For proper elliptic \(A\), choose a proper \(B_0\) quantizing the inverse class. Then \(R=I-AB_0\), \(L=I-B_0A\) have order \(-1\). Sum \(B_0R^j\) and \(L^jB_0\) by (G18), obtaining right and left parametrices \(B_R,B_L\). The finite identities
\[
A\sum_{j<N}B_0R^j=I-R^N,
\qquad
\left(\sum_{j<N}L^jB_0\right)A=I-L^N
\tag{G20}
\]
and the orders of their tails prove smoothing errors. Since smooth proper kernels form an ideal,
\(B_L-B_R=B_L(I-AB_R)+(B_LA-I)B_R\) is smoothing. Thus either is a proper two-sided parametrix, of order \(-m\). This proof requires no convergence of an operator Neumann series and no uniform ellipticity constant on a noncompact manifold.

A nonzero covector \(\gamma=(x_0,\xi_0)\) is noncharacteristic if (G19) holds in some open conic neighborhood of it, at sufficiently large frequency. Equivalently \(ab-1\in S^{-1}\) there for some conic \(b\in S^{-m}\). The reciprocal argument is local on a smaller conic neighborhood, so it proves this equivalence. Adding an order-\(m-1\) symbol cannot destroy the lower bound after shrinking and increasing the radius; coordinate changes preserve it by (G10). The complement \(\operatorname{Char}_m(A)\) is closed and conic. For a homogeneous leading symbol it is its zero set off the zero section. More generally the full local symbol has **microlocal order \(k\)** at a covector if it is in \(S^k\) on a conic neighborhood. Formula (G10), applied after a conic cutoff and with its separated remainder, and uniqueness in (G15), show that this notion is independent of chart and full-symbol representative. Order minus infinity means one neighborhood on which every negative-order estimate holds.

We record the conic form of the calculus used here. If symbols \(a,b\) are prescribed on a cone and the usual composition is formed after extending them with cutoffs, its differential expansion is the usual one on every smaller cone; changes of extension have smoothing effects there. To prove it, choose a classical degree-zero cutoff \(q\) equal to one on the smaller cone, supported in the larger one, and a second cutoff equal to one near its support. In the oscillatory formula for composition, terms away from those supports have either separated base points, handled by frequency integration by parts, or separated frequency directions. In the latter case \(|\eta-\xi|\geq c(|\eta|+|\xi|)\); integration by parts in the intermediate base variable supplies arbitrarily many factors of this denominator, while its derivatives increase a symbol order by strictly less than one. Split into dyadic frequency shells to sum the resulting estimates. Derivatives of any fixed order are handled by performing more integrations. In the remaining region the global remainder theorem of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) applies. This proves all differentiated conic estimates, including changes of cutoffs. It also shows that rapidly decreasing conic symbols form a two-sided microlocal ideal.

At a noncharacteristic point construct a local right inverse as follows. Choose \(b_0\), supported in the elliptic cone, equal there on a smaller cone to the reciprocal of \(a\), with a high-frequency cutoff. Extend \(r=1-a\circ b_0\), restricted to that smaller cone, to a global symbol of order \(-1\), using a further cone cutoff. The formal sum \(\sum b_0\circ r^{\circ j}\), made by local summation, gives an inverse modulo smoothing on a still smaller cone by (G20). The same construction on the left gives \(b_L\); the identity comparing the two inverses shows they agree modulo smoothing on their common cone. Proper quantization yields a single \(B\in\Psi^{-m}\) with both errors microlocally smoothing at the original point. Either such one-sided condition for a given \(B\) implies noncharacteristicity by the first remainder of the composition formula, hence implies the other condition by comparison with the inverse just constructed.

For \(1-\rho\leq\delta<\rho\), all constructions in this item hold with gain \(\varepsilon=\rho-\delta>0\), with \(S^{m-\varepsilon}\) in the principal quotient and \(S^{-\varepsilon}\) in the inverse-class condition. The coordinate error from Section 2 has order at most \(m-(2\rho-1)\leq m-\varepsilon\), so these quotient symbols are intrinsic. Replace powers of order \(-j\) by order \(-j\varepsilon\) in (G20). At \(\delta=\rho\), closure and coordinate invariance survive; the zero gain does not furnish this principal quotient, conic inverse argument, or elliptic regularity assertion.

## 7. Fourier directions and the precise kernel relation

On a coordinate open set, a nonzero covector \((x_0,\xi_0)\) is absent from \(\operatorname{WF}(u)\) if there is \(\chi\in C_c^\infty\), equal to one near \(x_0\), such that \(\widehat{\chi u}\) decreases faster than every inverse power in a cone about \(\xi_0\). A cutoff merely nonzero at \(x_0\) gives the same definition by multiplying with its smooth local reciprocal. The basic cutoff estimate is worth spelling out. If a compact distribution has polynomially bounded Fourier transform and that transform decreases rapidly in a cone \(V\), then multiplying by a compact smooth function preserves rapid decrease in every cone whose angular closure lies in \(V\). In the convolution formula split into \(\eta\in V\), where the input decreases rapidly, and its complement. For an output frequency in the smaller cone and a complementary \(\eta\),
\(|\xi-\eta|\geq c(|\xi|+|\eta|)\); rapid decay of the cutoff transform beats both the polynomial input bound and any desired output weight. Integrating these bounds proves the assertion. Spatial localization then proves that this definition is local, has a closed conic wavefront set, and gives smoothness exactly when every direction is regular: a finite angular cover of the unit sphere provides rapid Fourier decrease in all directions, followed by Fourier inversion.

For a compactly localized pseudodifferential kernel, use coordinates \((x,v)=(x,x-y)\). Before localizing in \(v\), its Fourier transform in \((x,v)\) is
\
\mathcal F_{x,v}\big[\phi(x)K_a(x,x-v)\big
=\mathcal F_x(\phi a)(\zeta,\eta).
\tag{G21}
\]
For classical symbols the right side is bounded by \(C_L\langle\zeta\rangle^{-L}\langle\eta\rangle^m\), after any fixed frequency derivatives. With general parameters the power in the last factor becomes \(m+\delta L\). Where \(|\zeta|\geq c|\eta|\), choose \(L\) large; the gain \(1-\delta>0\) gives rapid decay. Multiplication by a compact \(v\)-cutoff preserves that decay on smaller cones by the preceding convolution estimate. Together with off-diagonal smoothness this proves
\[
\operatorname{WF}(K_A)\subset
\{(x,x;\xi,-\xi):\xi\ne0\}.
\tag{G22}
\]
If \(a\) is smoothing on a conic neighborhood of \((x_0,\xi_0)\), the same calculation, splitting \(a\) with a conic cutoff, shows that the corresponding point is absent from (G22).

The converse also follows from (G21); here are the estimates needed for it. If the kernel is regular near \((x_0,v=0;0,\xi_0)\), choose compact cutoffs in \(x,v\), equal to one on smaller neighborhoods. Its full Fourier transform is rapidly decreasing when \(|\zeta|<c|\eta|\) and \(\eta\) is in a fixed smaller cone about \(\xi_0\). Recover the symbol of the cutoff kernel by inverse Fourier transformation in \(\zeta\). On that region rapid decrease gives every desired \(\eta\) bound, even after multiplying by a fixed power of \(\zeta\). On \(|\zeta|\geq c|\eta|\), the estimate following (G21) gives the same bound by increasing \(L\). Frequency derivatives can be taken before the estimates: they correspond to multiplying the compact kernel by powers of \(v\), which preserves its conic regularity. The recovered symbol therefore satisfies every negative-order estimate near \((x_0,\xi_0)\). Removing the \(v\)-cutoff changes the symbol by a smoothing symbol, by off-diagonal integration by parts and compact localization in both original variables. Thus (G22) is precisely the diagonal relation of the nonsmoothing directions of the full symbol.

Denote that closed conic subset of \(T^*X\setminus0\) by \(\operatorname{WF}(A)\). For the moment the assertion is local; coordinate invariance will follow below. The prime on a kernel relation reverses its input covector:
\[
\operatorname{WF}'(K_A)
=\{(x,\xi;y,-\eta):(x,y;\xi,\eta)\in\operatorname{WF}(K_A)\}
=\{(\gamma,\gamma):\gamma\in\operatorname{WF}(A)\}.
\tag{G23}
\]
This sign is essential: the identity operator has kernel \(\delta(x-y)\), whose untwisted covectors are \((\xi,-\xi)\).

## 8. What every input can detect

For proper \(A\), and also for arbitrary \(A\in\Psi^m\) on compactly supported inputs,
\[
\operatorname{WF}(Au)\subset\operatorname{WF}(A)\cap\operatorname{WF}(u).
\tag{G24}
\]
We give a proof using cutoffs, so no unstated general kernel-composition theorem is needed. If a direction is absent from \(\operatorname{WF}(A)\), choose a classical conic cutoff \(Q\) supported in that regular symbol cone, elliptic at the point. Then \(QA\) is smoothing there, and by restricting the support of \(Q\) it is smoothing everywhere on the output neighborhood. The symbol estimates of Section 6 prove this. If instead the direction is absent from \(\operatorname{WF}(u)\), choose compact spatial cutoffs and a smooth frequency cutoff \(q\), homogeneous above a ball and equal to one in a smaller cone, such that \(q(D)(\chi u)\) is smooth. Choose a proper \(Q\) equal to \(q(D)\chi\) near the point and a smaller conic cutoff \(P\). The full symbol of \(PA(I-Q)\) is smoothing by the separated-support estimates. Thus \(PAu=PAQu+PA(I-Q)u\) is smooth. Since \(P\) is a product of a spatial cutoff and an angular Fourier cutoff, this says directly that \(Au\) is Fourier-regular at the point. For an arbitrary distribution under a proper operator, (G17) reduces this argument to a compact input. For a global symbol and \(u\in\mathcal S'\), the separated spatial remainder \(\phi A(1-\chi)u\) is smooth: its kernel, after each output derivative, is Schwartz in the input variable, as repeated frequency integrations in (G5) show. This also proves global tempered pseudolocality and shrinkage of singular support.

The cutoff proof works for \(1-\rho\leq\delta\leq\rho\), including equality. One does not need an asymptotic expansion of two general equality-class symbols to separate a classical cutoff from a symbol. In \(a\circ q\) the differentiated terms gain \(\rho\) per paired derivative, since base derivatives of \(q\) cost zero; in \(q\circ a\) they gain \(1-\delta\). Both are positive. The same mixed-metric Gauss argument as Section 4 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) proves the remainders with these respective gains. It follows, by inserting nested classical cutoffs, that the microsupport of a defined product satisfies
\[
\operatorname{WF}(AB)\subset\operatorname{WF}(A)\cap\operatorname{WF}(B).
\tag{G25}
\]
For example if \(A\) is smoothing near a direction, insert \(Q=1\) on a smaller cone: \(QAB\) is smoothing because \(QA\) is smoothing. If \(B\) is smoothing there, insert a second cutoff \(Q_1=1\) near \(Q\); write \(QAB=QAQ_1B+QA(1-Q_1)B\), where the first term has a smoothing right factor in that cone and the second is separated. This proves the general equality-case assertion as well as the classical one.

There is an exact converse to (G24). For a closed conic \(\Gamma\subset T^*X\setminus0\), the following conditions are equivalent:

1. The full symbol of \(A\) is smoothing off \(\Gamma\).
2. \(\operatorname{WF}'(K_A)\subset\{(\gamma,\gamma):\gamma\in\Gamma\}\).
3. Every \(u\in\mathcal E'(X)\) satisfies \(\operatorname{WF}(Au)\subset\Gamma\cap\operatorname{WF}(u)\).

We proved the first equivalence in (G21)–(G23), and its implication to the third in (G24). Suppose the third holds and choose a compactly based classical cutoff \(Q\) whose microsupport lies in a small closed cone disjoint from \(\Gamma\), with symbol one near a chosen covector. For every compact distribution, \(AQ u\) has wavefront contained both in \(\Gamma\) and in \(\operatorname{WF}(Q)\), so it is smooth. We justify that its kernel is smooth, a fact stronger than smoothing individual test functions.

Localize both variables in compact coordinate sets. For a fixed input compact set \(K\), let \(E'_{K,N}\) be the Banach space of distributions supported in \(K\) with norm the dual norm of \(C^N\) test functions on a fixed compact neighborhood. The restricted map \(AQ:E'_{K,N}\to C^\infty\) has closed graph: convergence in that Banach norm implies distributional convergence, the original operator is continuous into distributions, and a smooth limit has the same distributional limit. Sections 14.5–14.6 of the Banach foundation lesson prove this closed graph step with the exact dual norm and every output seminorm, and therefore make this map continuous. For input points in the interior of \(K\), the map \(y\mapsto\delta_y\) is \(C^r\) into \(E'_{K,N}\) when \(N\geq r+1\). Taylor's formula, with one extra uniformly bounded derivative on the unit ball of \(C^N\), proves this assertion and its difference-quotient derivatives. Consequently \((x,y)\mapsto (AQ\delta_y)(x)\) has every prescribed mixed derivative: choose \(r,N\) sufficiently large and use continuity into every output \(C^k\) seminorm. It is the kernel, since integration of \(\delta_y f(y)\) reproduces a test function and the operator is continuous. Hence that kernel is smooth.

Its symbol is therefore smoothing after compact localization. The conic cutoff calculus gives \(a\circ q-a\in S^{-\infty}\) near the selected covector, since \(q=1\) there to all orders. Thus \(a\) is smoothing there. This proves the converse and the minimality of \(\operatorname{WF}(A)\) among all sets allowed in (G24).

## 9. Elliptic tests and intrinsic wavefront

For every fixed real \(m\) and \(u\in\mathcal D'(X)\),
\[
\operatorname{WF}(u)=
\bigcap_{\substack{A\in\Psi^m(X)\ \mathrm{proper}\\Au\in C^\infty(X)}}
\operatorname{Char}_m(A).
\tag{G26}
\]
If a direction is Fourier-regular, choose an order-\(m\) conic symbol supported in a regular neighborhood and elliptic at the direction, for instance a degree-zero cutoff times \(\langle\xi\rangle^m\), with compact base support. Proper quantization and (G24) make \(Au\) smooth globally. Conversely, if \(Au\) is smooth and \(A\) is noncharacteristic at the direction, its conic inverse from Section 6 gives
\(u=BAu+(I-BA)u\). The first term is smooth because \(B\) is proper, and the second is regular at the direction by (G24). This proves (G26) for the specified fixed order, not just for order zero.

Conjugating the test operators in (G26) by a diffeomorphism preserves properness, their order, their action on smooth functions, and their noncharacteristic set under the cotangent map, by Section 2 and Section 6. Distributions themselves pull back by the change-of-variables formula
\((\kappa^*u)(f|dx|)=u((f\circ\kappa^{-1})|\det(\kappa^{-1})'|\,|dz|)\);
it is continuous because composition and multiplication are continuous on compact test-function spaces. Thus (G26) proves that the Fourier definition transforms by the cotangent map. This establishes its intrinsic meaning on \(X\), and also that of (G23), without assuming a general pullback theorem for distributions with wavefront constraints. Smooth changes of bundle frame preserve it componentwise, by (G24) for multiplication and by the inverse frame transformation.

For a proper \(A\in\Psi^m\),
\[
\operatorname{WF}(u)\subset\operatorname{WF}(Au)\cup\operatorname{Char}_m(A).
\tag{G27}
\]
At a point outside the right side, choose a proper order-zero cutoff \(C\) elliptic there with \(CAu\) smooth, using (G26). The product \(CA\) is noncharacteristic there, and (G26) applied to it proves regularity of \(u\). Equivalently use its conic inverse. Together (G24) and (G27) say that a noncharacteristic operator neither creates nor removes a smoothness defect at that direction. The same proof applies in the strict coordinate-invariant \((\rho,\delta)\) range using the positive-gain conic inverse from Section 6.

## 10. Convergence when singular directions are fixed

Let \(\Gamma\) be closed and conic off zero. Set \(\mathcal D'_\Gamma(X)=\{u:\operatorname{WF}(u)\subset\Gamma\}\). We use the following sequential convergence convention, defined here as follows. In each chart, \(u_j\to u\) means weak distributional convergence and
\[
\sup_{\xi\in V}\langle\xi\rangle^N
|\widehat{\phi(u_j-u)}(\xi)|\longrightarrow0
\tag{G28}
\]
for every \(N\geq0\), compact smooth \(\phi\), and closed frequency cone \(V\) for which \((\operatorname{supp}\phi\times V)\cap\Gamma=\varnothing\) off zero. Replacing \(\langle\xi\rangle^N\) by \(|\xi|^N\), \(N\geq1\), gives the same convention: weak convergence and uniform boundedness imply uniform Fourier convergence on bounded frequency sets. We make a statement about sequences, not an identification of all locally convex topologies that share the same convergent sequences.

The equivalent operator test is
\[
u_j\longrightarrow u\text{ weakly in }\mathcal D',
\qquad
Au_j\longrightarrow Au\text{ in }C^\infty(X)
\tag{G29}
\]
for every proper pseudodifferential \(A\) with \(\operatorname{WF}(A)\cap\Gamma=\varnothing\).

We first isolate a uniformity fact. A weakly convergent sequence of distributions has, on each fixed compact input set, a common finite-order bound by (BF9) in Section 14.3 of the Banach foundation lesson, after the test-space completeness proof in Section 14.2. Moreover it converges uniformly on compact families of test functions in that space: cover the family by finitely many small neighborhoods in the controlling seminorm, and combine the common bound with convergence at the finitely many centers. In particular a fixed smooth proper kernel sends weakly convergent sequences to \(C^\infty\)-convergent sequences, since its differentiated input test functions over a compact output set form compact families.

Assume (G28) and fix an output compact set for \(A\). Properness restricts the input to a fixed compact set. Up to a smooth kernel, split the symbol into finitely many pieces whose angular/base supports have closures disjoint from \(\Gamma\); this is possible by compactness of the cosphere over the output compact set. Use a spatial cutoff \(\phi\) and a slightly larger good frequency cone for each piece. In the Fourier formula for its action on \(\phi(u_j-u)\), the part in that cone is bounded, after \(k\) output derivatives, by a constant times the seminorm (G28) with \(N>m+k+n+1\). It therefore tends to zero. The complementary frequency part has separated angular supports and is a smooth kernel after the conic integration-by-parts argument in Section 6. The uniformity fact handles that part, as well as the initial smooth remainder. Finitely many such bounds prove every output \(C^k\) seminorm in (G29).

Conversely fix \(\phi,V\) in (G28). Enlarge its spatial support slightly and its angular cone slightly while remaining disjoint from \(\Gamma\); if necessary a finite partition in the spatial variable achieves such an enlargement. Choose \(\chi=1\) near the enlarged spatial support and a classical angular cutoff \(q=1\) near \(V\), supported in the enlarged cone above frequency one. Make \(A=\chi q(D)\phi\) proper by the common near-diagonal kernel cutoff. Its microsupport avoids \(\Gamma\), so (G29) gives convergence of its compactly supported outputs in every smooth norm. The properness correction is a smooth kernel on the fixed input support and tends to zero in the same norms. Thus \(\chi q(D)\phi(u_j-u)\to0\) in \(C_c^\infty\). The omitted output tail \((1-\chi)q(D)\phi(u_j-u)\) has a Schwartz kernel in the output variable and compact support in the input variable: repeated frequency integration by parts gives arbitrary spatial decay, uniformly with derivatives and input derivatives, because the two spatial supports are separated. The uniformity fact therefore makes this tail tend to zero in \(\mathcal S\). We conclude \(q(D)\phi(u_j-u)\to0\) in \(\mathcal S\). Taking its Fourier transform and restricting to \(V\) above frequency one gives (G28). Bounded frequencies were already controlled by weak convergence. This proves the equivalence and, by its intrinsic operator formulation, its coordinate independence.

One may replace convergence in (G28) by uniform boundedness of those seminorms for all \(N\), retaining weak distributional convergence. To see this, control a desired order \(N\) tail by the uniform order-\(N+1\) bound divided by the frequency radius; on a bounded frequency set use uniform convergence. This is a statement about the entire sequence, including its limit, and does not weaken the requirement that every \(u_j\) and \(u\) lie in \(\mathcal D'_\Gamma\).

## 11. Sobolev and Besov spaces in a moving chart

Let \(\mathcal B^s_p=B^s_{2,p}\), \(1\leq p\leq\infty\), be the dyadic Hilbert-based Besov space of Section 8 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md). Explicitly, with sharp annular Fourier projections \(\Pi_j\),
\[
\|u\|_{\mathcal B^s_p}
=\left\|(2^{js}\|\Pi_j u\|_{L^2})_{j\geq0}\right\|_{\ell^p},
\qquad \mathcal B^s_2=H^s
\tag{G30}
\]
up to equivalent norms. At \(p=\infty\) the norm is a supremum. This is the scale also denoted \({}^pH_{(s)}\), and the exponent \(p\) is not a spatial \(L^p\) exponent.

We prove invariance under compactly localized coordinate changes for every real \(s\) and every displayed \(p\). Let
\(Tu(z)=\phi(z)\,u(\kappa^{-1}(z))\), with compact smooth \(\phi\) inside a coordinate image, inserting an input cutoff equal to one on its inverse image. For an integer \(k\geq0\), the chain rule and change of variables bound its \(H^k\) norm by the input \(H^k\) norm: by Plancherel, the sum of the \(L^2\) norms of derivatives of orders at most \(k\) is an equivalent norm. All coefficient functions and Jacobians are bounded on the fixed compact supports. The \(L^2\) transpose of \(T\) is the reverse coordinate pullback times the smooth density Jacobian and cutoffs, so it has the same positive-integer estimates. Duality gives the estimates on \(H^{-k}\). This duality follows directly from the weighted Fourier pairing:
\(\|u\|_{H^{-k}}=\sup_{\|v\|_{H^k}\leq1}|\langle u,v\rangle|\), first for Schwartz functions and then by completion.

Choose integers \(k_-<s<k_+\). The annular two-endpoint argument (E39) of Section 8 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), with order shift zero, now yields
\[
T:\mathcal B^s_p\longrightarrow\mathcal B^s_p
\quad\text{continuously},\qquad1\leq p\leq\infty.
\tag{G31}
\]
Its proof uses a summable convolution sequence in the dyadic indices and consistency of \(T\) on the two Sobolev endpoints. Distributional pullback supplies that consistency. At \(p=\infty\) the input annular sums are taken in the lower Sobolev space, not incorrectly asserted to converge in the Besov norm. Applying (G31) to the inverse diffeomorphism proves equivalence of chart norms. Thus this argument also proves real-order Sobolev coordinate invariance, without importing it as an extra theorem.

Define \(\mathcal B^{s,\mathrm{loc}}_p(X)\) by requiring every compact coordinate cutoff of a distribution, expressed in that chart and extended by zero, to have finite norm (G30). Its topology consists of those seminorms. Define \(\mathcal B^{s,\mathrm{comp}}_p(X)\) by adding compact support, with the inductive-limit topology over compact supports. Formula (G31), multiplication boundedness from [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md), and finite partitions on each compact set show independence of coordinates and cutoff families. The same definitions apply to finitely many components of a vector bundle; changing frame multiplies by a smooth invertible matrix, bounded on every compact set together with its derivatives, and hence preserves these local spaces. No globally chosen bundle norm or volume form is required.

If \(A\in\Psi^m\) is proper, then
\[
A:\mathcal B^{s,\mathrm{loc}}_p(X)\to\mathcal B^{s-m,\mathrm{loc}}_p(X),
\qquad
A:\mathcal B^{s,\mathrm{comp}}_p(X)\to\mathcal B^{s-m,\mathrm{comp}}_p(X)
\tag{G32}
\]
continuously. Fix an output compact set and use properness to choose an input cutoff. A finite chart partition and (G15) express the localized map as finitely many global symbols of order \(m\), plus a compactly localized smooth kernel. [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) proves the desired bound for each symbol. A compact smooth kernel maps any fixed lower Sobolev space into any higher one: its Fourier transform decreases rapidly in both variables, and Cauchy–Schwarz with weights proves this bound. Applying the same dyadic endpoint argument proves its Besov bound. This handles every summand and every local output seminorm. Properness also bounds output support on each fixed input support, which proves the compact-space continuity. Without properness, the same proof gives the meaningful map \(\mathcal B^{s,\mathrm{comp}}_p\to\mathcal B^{s-m,\mathrm{loc}}_p\), and a local symbol on \(U\) maps \(\mathcal S'(\mathbb R^n)\to\mathcal D'(U)\), as follows by multiplying each output by a compact cutoff and using [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md).

For proper elliptic \(A\), its parametrix gives the converse regularity implication in (G32). For example if \(u\in\mathcal D'(X)\) and \(Au\in\mathcal B^{s-m,\mathrm{loc}}_p\), write \(u=BAu+Ru\) with \(R\) a smooth proper kernel. The first term belongs to \(\mathcal B^{s,\mathrm{loc}}_p\) by (G32), and the second is smooth. If the input \(u\) is already compactly supported, this gives the corresponding compact-space regularity assertion. It does not infer compact support of \(u\) from compact support of \(Au\). For Sobolev spaces, one can equivalently test \(H^{s,\mathrm{loc}}\) by a proper elliptic operator of order \(s\) mapping to \(L^2_{\mathrm{loc}}\). Existence follows by quantizing a positive cotangent weight of order \(s\), constructed in charts and patched; any such operator gives the equivalence by (G32) and its parametrix. With general coordinate-invariant parameters (G32) is valid through equality, while its elliptic converse uses \(\delta<\rho\).

## 12. Microlocal scales and their unattained thresholds

Fix \(s\in\mathbb R\) and \(p\in[1,\infty]\). We say that \(u\) is \(\mathcal B^s_p\) at a base point \(x\) if
\(u=v+w\), with \(v\in\mathcal B^{s,\mathrm{loc}}_p\) and \(w\) smooth near \(x\). We say that it is \(\mathcal B^s_p\) at a nonzero covector \(\gamma\) if such a decomposition has \(\gamma\notin\operatorname{WF}(w)\). These are properties of \(u\): two possible decompositions need not have the same individual terms. At a base point the definition is equivalent to \(\phi u\in\mathcal B^{s,\mathrm{loc}}_p\) for some compact smooth \(\phi\) nonzero at that point. One implication follows by multiplying the decomposition with a cutoff supported where \(w\) is smooth; the other by setting \(v=\chi u\) with \(\chi=1\) near the point, using a local reciprocal of \(\phi\) and multiplication boundedness.

The equivalent covector test, for any fixed real \(m\), is that there exists a proper \(A\in\Psi^m\), noncharacteristic at \(\gamma\), with
\[
Au\in\mathcal B^{s-m,\mathrm{loc}}_p(X).
\tag{G33}
\]
Given the decomposition, take a compactly based conic operator of order \(m\), elliptic at \(\gamma\), whose microsupport avoids \(\operatorname{WF}(w)\). Then \(Av\) has the required regularity by (G32), and \(Aw\) is smooth by (G24). Conversely a conic parametrix gives \(u=BAu+(I-BA)u\), which is exactly a decomposition of the stipulated kind. Thus this test is independent of the chosen order and coordinates, and works at the Besov endpoints as well as in the Hilbert case.

For any proper \(A\in\Psi^m\),
\[
u\text{ is }\mathcal B^s_p\text{ at }\gamma
\ \Longrightarrow\ Au\text{ is }\mathcal B^{s-m}_p\text{ at }\gamma.
\tag{G34}
\]
Apply \(A\) to a defining decomposition. Equation (G32) handles its regular part, and (G24) handles its wavefront-regular remainder. If \(A\) is noncharacteristic at \(\gamma\), the converse follows by applying its conic parametrix and (G34), since the remaining error is regular at \(\gamma\). In the strict \((\rho,\delta)\) range the same argument works with its conic inverse; the forward implication uses only mapping and pseudolocality and therefore also holds at equality.

If \(u\) has \(\mathcal B^s_p\) regularity at every nonzero cotangent vector over \(x_0\), then it has that regularity at \(x_0\). To prove the nontrivial direction, use (G33) with \(m=0\). The elliptic sets of finitely many tests \(A_1,\ldots,A_N\) cover the cosphere over \(x_0\), by compactness. Their order-zero principal representatives \(a_j\) satisfy
\(\sum_j|a_j(x,\xi)|^2\geq c>0\) in a neighborhood of that cosphere, above a common radius: shrink finitely many neighborhoods and use compactness once more. Choose proper order-zero \(C_j\) with principal symbol \(\overline{a_j}\), and set \(P=\sum_j C_jA_j\). Then \(Pu\in\mathcal B^{s,\mathrm{loc}}_p\) and \(P\) is elliptic over a neighborhood of \(x_0\). Its conic inverse can be chosen uniformly over that compact cosphere, or constructed from a local reciprocal there by Section 6. Thus \(BP-I\) is smoothing over that whole spatial neighborhood. Multiplying by a smaller spatial cutoff yields local regularity of \(u\). The reverse implication follows at once from the definition. No summation over infinitely many directions, nor reflexivity of the Besov space, occurs.

Define the extended real Sobolev thresholds
\[
s_u(x)=\sup\{s:u\text{ is }H^s\text{ at }x\},\qquad
s_u^*(x,\xi)=\sup\{s:u\text{ is }H^s\text{ at }(x,\xi)\}.
\tag{G35}
\]
Each is lower semicontinuous: if its value exceeds \(t\), choose a regularity order \(s>t\) below that value and keep the corresponding cutoff or decomposition on its open regularity neighborhood. Thus the set where the threshold exceeds \(t\) is open. Both definitions allow \(+\infty\); finite-order compact distribution estimates imply some local negative Sobolev regularity, so the value is never \(-\infty\) at an ordinary base point or covector. Indeed a compactly localized distribution has \(|\widehat u(\xi)|\leq C\langle\xi\rangle^M\) for some \(M\); the defining Fourier integral for its squared \(H^s\) norm is finite whenever \(2s+2M+n<0\).

There is an exact relation
\[
s_u(x)=\inf_{\xi\ne0}s_u^*(x,\xi).
\tag{G36}
\]
Local membership implies membership in every direction, giving \(\leq\). If \(t\) is strictly below the infimum, for each direction choose an order strictly between \(t\) and its threshold. Sobolev monotonicity implies membership at order \(t\) in that direction. The finite-cosphere argument just proved gives local membership at order \(t\), hence \(s_u(x)\geq t\). Let \(t\) approach the infimum; this also handles an infinite infimum. This reasoning does not claim membership at the threshold itself.

For \(A\in\Psi^m\) proper, (G34) gives
\[
s_{Au}^*(x,\xi)\geq s_u^*(x,\xi)-m,
\qquad
s_{Au}^*(x,\xi)=s_u^*(x,\xi)-m
\quad\text{off }\operatorname{Char}_m(A).
\tag{G37}
\]
The equality follows by applying the inverse regularity implication at every real order; subtraction of a finite \(m\) from \(+\infty\) is interpreted as \(+\infty\). Identical definitions and proofs give thresholds for each fixed Besov exponent \(p\), but equality of thresholds never identifies endpoint membership for different \(p\). Equations (G30)–(G37) supply the microlocal continuation of the global and local-cutoff Besov assertions established in [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md).

### 12.1. Editorial extension: every positive sequence exponent and the same thresholds

The restrictions on the sequence exponent in (G30)--(G34) can be removed. The original statements remain above; this extension proves the actual coordinate, bundle and microlocal maps for \(0<p\le\infty\). It also proves that the supremum thresholds are independent of this sequence exponent, while keeping endpoint membership distinct.

Keep every original sharp annulus \(A_0=\{|\xi|<1\}\), \(A_j=\{2^{j-1}\le|\xi|<2^j\}\) for \(j\ge1\), and projection \(\Pi_j\). For a finite coordinate fiber \(H=\mathbb C^r\), with its original Euclidean Hilbert norm, put
\[
 N_{s,p,H}(u)=\left(\sum_{j\ge0}
       (2^{js}\|\Pi_j u\|_{L^2(H)})^p\right)^{1/p}
       \quad(0<p<\infty),\qquad
 N_{s,\infty,H}(u)=\sup_{j\ge0}2^{js}\|\Pi_j u\|_{L^2(H)}.
 \tag{GB1}
\]
The actual domain is the \(H\)-valued tempered distributions whose Fourier transforms are locally \(L^2(H)\) and have this finite quantity. For \(0<p<1\), its distance is \(N_{s,p,H}(u-v)^p\). The inequality \((a+b)^p\le a^p+b^p\), proved in BQ1--BQ2 of [the Euclidean chapter](euclidean-symbol-calculus.md), gives the metric triangle inequality.

The scalar reconstruction BQ3 applies to the finitely many original components, keeping their full vector:
\[
 u(\varphi)=(2\pi)^{-n}\sum_{j\ge0}
       \int_{A_j}F_j(\xi)\widehat\varphi(-\xi)\,d\xi,\qquad
 v_j=2^{js}(2\pi)^{-n/2}\|F_j\|_{L^2(H)}.
 \tag{GB2}
\]
For \(j\ge1\), its vector norm is bounded by
\((2\pi)^{-n/2}\omega_n^{1/2}2^L C_L
2^{j(n/2-s-L)}v_j\), where
\(C_L=\sup_\xi\langle\xi\rangle^L|\widehat\varphi(-\xi)|\) and an integer \(L>n/2-s\) is chosen. The low term is bounded by
\((2\pi)^{-n/2}v_0\|\widehat\varphi\|_{L^2(A_0)}\).
These are the same Cauchy--Schwarz bounds on the original vector-valued integrals. They prove absolute convergence, continuity into tempered distributions, and identification of the Fourier transform with the locally \(L^2\) function \(\sum F_j\). Plancherel retains \((2\pi)^{-n/2}\) in each piece. Component Hilbert limits and increasing finite sums give BQ4 with this vector norm; for infinity take the supremum of the component limits. Thus every domain in (GB1) is complete. BQ6's finite-overlap proof uses the Hilbert triangle inequality and the scalar \(p\)-power inequality, so its two displayed constants apply unchanged to these original vectors.

Here are the coordinate bounds, with the entire derivative and measure factors. Let \(\kappa:U\to V\) be the original smooth coordinate diffeomorphism, \(\psi=\kappa^{-1}\), \(\phi\in C_c^\infty(V)\), and \(\chi\in C_c^\infty(U)\) real and equal to one near \(\psi(\operatorname{supp}\phi)\). Let \(M(z)\) be an arbitrary smooth \(f\times e\) matrix on \(V\). Its localized map is
\[
 Tu(z)=A(z)u(\psi(z)),\qquad
 A(z)=\phi(z)M(z)\chi(\psi(z)),\qquad
 J_\kappa(x)=|\det D\kappa(x)|.
 \tag{GB3}
\]
It is extended by zero outside \(V\). This is the original pullback applied to \(\chi u\), followed by the displayed multiplication; its scalar distribution pairing includes the Jacobian in (GK26). Because \(\chi=1\) on a neighborhood of the relevant compact set, \(\chi(\psi(z))=1\) wherever \(\phi\) or any derivative of \(\phi\) is nonzero. Its derivative contributions there are exactly zero. This proves agreement with the original map (G31), rather than dropping an input cutoff without explanation.

For a multi-index \(\gamma\), retain a labeled list \(h_1,\ldots,h_k\), \(k=|\gamma|\), containing \(\gamma_i\) copies of the original coordinate direction \(e_i\). Let \(D_B\) mean differentiation in the directions with labels in \(B\), and \(\mathfrak P(S)\) all partitions of a label set \(S\) into nonempty blocks; the empty set has its one empty partition. For \(|\alpha|\le k\), the entire coefficient of \((\partial^\alpha u)(\psi(z))\) is
\[
 Q_{\gamma,\alpha}(z)=
 \sum_{J\subset\{1,\ldots,k\}}
 \sum_{\Pi\in\mathfrak P(J^c)}
 \sum_{\substack{\nu:\Pi\to\{1,\ldots,n\}\\
       \#\{B:\nu(B)=i\}=\alpha_i\ (\text{all }i)}}
       (D_J A)(z)\prod_{B\in\Pi}D_B\psi^{\nu(B)}(z).
 \tag{GB4}
\]
The sum over \(\nu\) is zero unless \(|\Pi|=|\alpha|\). In \(D_J A\) the full product rule is
\[
 D_J A=\sum_{J_1\sqcup J_2\sqcup J_3=J}
        (D_{J_1}\phi)(D_{J_2}M)D_{J_3}(\chi\circ\psi).
 \tag{GB5}
\]
For a nonempty \(J_3\), its last derivative is the full chain sum
\(\sum_{\Theta\in\mathfrak P(J_3)}
D^{|\Theta|}\chi(\psi)[D_B\psi:B\in\Theta]\);
for an empty \(J_3\) it is \(\chi(\psi)\).
The finite-coordinate chain and product rules, proved with these same labeled partitions in Sections16.1 and16.5, give exactly
\(\partial^\gamma Tu=\sum_{|\alpha|\le|\gamma|}
Q_{\gamma,\alpha}(\partial^\alpha u)\circ\psi\).
Repeated coordinate directions keep every multiplicity. The matrix coefficient acts on the left and is never commuted with another matrix.

For an integer \(N\ge0\), set
\[
 c_{N,\alpha}=\frac{N!}{(N-|\alpha|)!\alpha!},\qquad
 \|u\|_{H^N(H)}^2=(2\pi)^{-n}
       \int\langle\xi\rangle^{2N}\|\widehat u(\xi)\|_H^2\,d\xi
       =\sum_{|\alpha|\le N}c_{N,\alpha}
          \|\partial^\alpha u\|_{L^2(H)}^2.
 \tag{GB6}
\]
The last equality is the full multinomial expansion of \((1+\sum_i\xi_i^2)^N\) and Plancherel: the derivative transform is \((i\xi)^\alpha\widehat u\), whose squared norm keeps precisely \(\xi^{2\alpha}\).
If the coordinate opens are empty, or the localized coefficient is identically zero, the actual map is zero and every endpoint bound is zero. Otherwise choose a nonempty compact \(K\Subset U\) containing \(\psi(\operatorname{supp}\phi)\). Let \(J_*=\sup_K J_\kappa\) and \(t_\gamma=\#\{\alpha:|\alpha|\le|\gamma|\}=\binom{n+|\gamma|}{n}\). All norms of \(Q\) below are supremums on \(V\), finite by their compact support. Change of variables retains \(dz=J_\kappa(x)\,dx\); Cauchy--Schwarz in the finite \(\alpha\)-sum therefore gives
\[
 \begin{aligned}
 \|Tu\|_{H^N(\mathbb C^f)}&\le E_N(T)
                       \|u\|_{H^N(\mathbb C^e)},\\
 E_N(T)^2&=
 J_*\sum_{|\gamma|\le N}c_{N,\gamma}t_\gamma
      \sum_{|\alpha|\le|\gamma|}
        \frac{\|Q_{\gamma,\alpha}\|_\infty^2}{c_{N,\alpha}}.
 \end{aligned}
 \tag{GB7}
\]
To verify the bound, square the displayed derivative sum, bound it by
\(t_\gamma\sum_\alpha\|Q_{\gamma,\alpha}\|_\infty^2
\|(\partial^\alpha u)\circ\psi\|^2\), integrate with the original Jacobian, and use
\(\|\partial^\alpha u\|_2^2\le c_{N,\alpha}^{-1}\|u\|_{H^N}^2\)
for every retained \(\alpha\). This proves the full finite constant, including \(N=0\). A zero coefficient contributes zero to that sum.

The actual Hilbert adjoint on the original coordinate measures is
\[
 T^*v(x)=
 \chi(x)J_\kappa(x)\overline{\phi(\kappa(x))}
          M(\kappa(x))^*v(\kappa(x)).
 \tag{GB8}
\]
Substitution in the compact integral proves this identity, including its order and its whole positive Jacobian. Applying (GB4)--(GB7) to this reverse map, with \(\psi\) replaced by \(\kappa\) and with the entire coefficient in (GB8), gives its positive-integer constants \(E_N(T^*)\). Weighted Fourier duality retains
\((2\pi)^{-n}\int\widehat u\cdot\overline{\widehat v}\,d\xi\);
Cauchy--Schwarz and the inverse weights show
\(\|u\|_{H^{-N}}=\sup_{\|v\|_{H^N}\le1}|(u,v)|\).
The reverse inequality is obtained by the actual weighted Fourier vector, or its truncated \(L^2\) approximations. Thus
\(\|Tu\|_{H^{-N}}\le E_N(T^*)\|u\|_{H^{-N}}\).
The completions agree with the original distribution pullback, since all formulas agree on Schwartz functions and converge into distributions. These give consistent bounds at every integer endpoint, with no assumption of real-order coordinate invariance.

For any real \(s\), choose integers \(k_-<s<k_+\), and write \(M_-,M_+\) for these proved endpoint norms. Put
\[
 \begin{aligned}
 a_t&=\min(2^{-t},2^{t/2}),&
 b_t&=\max(2^{-t},2^{t/2}),\\
 C&=\max(M_-b_{k_-}/a_{k_-},
                  M_+b_{k_+}/a_{k_+}),&
 c_l&=\min(2^{l(s-k_-)},2^{l(s-k_+)}).
 \end{aligned}
 \tag{GB9}
\]
On every original annulus \(2^{-j}\langle\xi\rangle\in[1/2,\sqrt2]\), including \(j=0\). Applying both endpoint estimates to \(\Pi_j u\) gives
\[
 2^{ks}\|\Pi_kT\Pi_j u\|_2
       \le Cc_{k-j}\,2^{js}\|\Pi_j u\|_2.
 \tag{GB10}
\]
For finite annular sums apply the target Hilbert triangle inequality. For \(0<p<1\), take the \(p\)-th power, use its subadditivity, and sum over both nonnegative indices. For \(1\le p<\infty\), use the sequence triangle inequality on the translated sequences; for infinity use the supremum directly. The complete resulting constants are
\[
 \begin{aligned}
 N_{s,p,\mathbb C^f}(Tu)&\le CD_pN_{s,p,\mathbb C^e}(u),\\
 D_p^p&=1+\frac{2^{-p(s-k_-)}}{1-2^{-p(s-k_-)}}
             +\frac{2^{-p(k_+-s)}}{1-2^{-p(k_+-s)}}
                         &&(0<p<1),\\
 D_p&=1+\frac{2^{-(s-k_-)}}{1-2^{-(s-k_-)}}
             +\frac{2^{-(k_+-s)}}{1-2^{-(k_+-s)}}
                         &&(1\le p\le\infty).
 \end{aligned}
 \tag{GB11}
\]
Indeed the two tails are respectively \(l<0\) and \(l>0\), and the retained \(l=0\) term is one. For an arbitrary input in (GB1),
\[
 \|u\|_{H^{k_-}}^2\le
       \frac{b_{k_-}^2}{1-2^{-2(s-k_-)}}
          N_{s,p,H}(u)^2.
 \tag{GB12}
\]
Sum the disjoint original Fourier squares and bound each weighted annular norm by its sequence norm to obtain this inequality; the same geometric tail proves convergence of the input partial sums in \(H^{k_-}\). Hence \(Tu\) is the already defined endpoint distribution. Each fixed output projection converges in \(L^2\). Increasing finite sums, or a supremum, pass (GB11) to that actual limit. This proves all positive sequence exponents, including infinity, without claiming Besov-norm density at infinity. Applying the same proof to a localized inverse coordinate map and inverse frame matrix gives the actual inverse local maps and the equivalence of chart norms.

Consequently the local and compact spaces in Section11 extend to every \(0<p\le\infty\), on the same distributions and bundles. For \(p<1\), use the finite local quasi-norm conditions \(N_{s,p}(\phi u)\), rather than calling them locally convex seminorms. With \(q=\min(1,p)\) and \(q=1\) at infinity, finite sums satisfy
\[
 N_{s,p}\left(\sum_{\ell=1}^L u_\ell\right)^q
       \le\sum_{\ell=1}^L N_{s,p}(u_\ell)^q.
 \tag{GB13}
\]
For \(p<1\) this follows from the Hilbert triangle inequality on each annulus and scalar subadditivity; otherwise it is the norm triangle inequality. Compactness makes each local partition sum finite. Thus (GB11), its inverse and (GB13) prove independence of every chart, cutoff and smooth invertible finite-rank frame, preserving all transition matrices.

The mapping theorem (G32) and its elliptic converse hold for every such \(p\). For each localized symbol, apply the consistent Sobolev endpoints already proved in the Euclidean chapter, with shift \(m\); (GB9)--(GB12) then has \(a_{k_\pm-m}\) in its denominator and \(2^{k(s-m)}\) on its output. The geometric sums are unchanged. A compactly localized smooth kernel is bounded from every integer \(H^{k_\pm}\) to \(H^{k_\pm-m}\): its full two-variable Fourier transform decreases to every order, and weighted Cauchy--Schwarz retains the two original inverse factors. The same endpoint argument receives its actual distributional map. A finite chart partition and (GB13) combine these maps, with bound \((\sum_\ell C_\ell^q)^{1/q}\) when the individual bounds are \(C_\ell\). Properness gives the same input and output compact sets as (G17), and hence both local and compact maps. Without properness it gives exactly compact input to local output. The positive-gain parametrix gives \(u=BAu+Ru\) as before; multiplication by a local cutoff makes the smooth \(Ru\) belong to every space (GB1). This proves the converse, with compact support of the input still required for its compact-space version. In the coordinate-invariant range \(1-\rho\le\delta\le\rho\), \(\delta<1\), the forward mapping holds through equality; the inverse assertion still requires \(\delta<\rho\).

The decomposition, fixed-order test and both microlocal implications (G33)--(G34) also extend to every \(p\). Given \(u=v+w\), choose the same compact conic test of order \(m\), elliptic at the selected covector and supported away from \(\operatorname{WF}(w)\). The extended (G32) sends \(v\) into the stated order \(s-m\) space, and (G24) makes the image of \(w\) smooth. Conversely the same proper conic parametrix gives \(v=BAu\) and \(w=(I-BA)u\); the first has order \(s\) regularity and the second has no wavefront at that covector. Applying any proper operator to this decomposition proves the forward implication, and its conic inverse proves the noncharacteristic converse. No convexity or sequence reflexivity is used.

The finite-cosphere argument is valid for all these exponents too. In one fixed local frame, choose finitely many order-zero tests \(A_j\) whose elliptic sets cover the cosphere over the original point. Their principal matrices have
\(\sum_j a_j^*a_j\ge cI\) on a smaller base/cosphere neighborhood: at each direction at least one original smallest singular value is positive; the finite cover and compactness give the common \(c>0\). Quantize \(a_j^*\) in that same frame with the original compact cutoffs, obtaining \(C_j\), and use the actual ordered sum \(P=\sum_j C_jA_j\). By (GB13), \(Pu\) has the required local Besov regularity. Its displayed principal matrix is invertible there, so the proper local inverse yields base-point regularity. Thus regularity at all nonzero directions over a point is exactly regularity at that point, for arbitrary finite rank as well as for scalars.

Finally there is a stronger exact threshold statement. For any \(0<p,r\le\infty\) and \(\epsilon>0\), the same original annuli give
\[
 \begin{aligned}
 N_{s-\epsilon,r,H}(u)&\le
       (1-2^{-\epsilon r})^{-1/r}N_{s,p,H}(u)
                                  &&(0<r<\infty),\\
 N_{s-\epsilon,\infty,H}(u)&\le N_{s,p,H}(u).
 \end{aligned}
 \tag{GB14}
\]
Each \(v_j=2^{js}\|\Pi_j u\|_2\) is at most its sequence norm for every \(p\), and the entire \(r\)-power sum is bounded by
\(\sum_{j\ge0}2^{-j\epsilon r}\sup_jv_j^r\);
this is precisely the constant in (GB14), with its low term retained. Apply it to each compact cutoff for local membership and to the regular part of a microlocal decomposition for directional membership. If one exponent admits an order greater than \(t\), choose a loss \(\epsilon\) smaller than the difference from that order to \(t\). Every other exponent then admits order \(t\). Reversing the exponents proves that all supremum thresholds coincide, including \(+\infty\). In particular they are exactly the Sobolev thresholds (G35), since the \(p=2\) norm is equivalent to the original \(H^s\) norm. Their lower semicontinuity, base/cosphere infimum identity (G36), and the proper-operator inequality and elliptic equality (G37) therefore hold for every positive sequence exponent with these same thresholds. There is still no assertion of membership at the supremum.

The retained point-mass example makes the endpoint distinction exact. For \(n\ge1\), \(\widehat{\delta_0}=1\), so
\[
 \|\Pi_0\delta_0\|_2=(2\pi)^{-n/2}\omega_n^{1/2},\qquad
 \|\Pi_j\delta_0\|_2=(2\pi)^{-n/2}
       \bigl(\omega_n(1-2^{-n})\bigr)^{1/2}2^{jn/2}
       \quad(j\ge1).
 \tag{GB15}
\]
These are the original annular volumes and Plancherel factor. At \(s=-n/2\) the tail sequence is the same strictly positive constant, hence belongs to infinity and to no finite positive sequence exponent. At \(s<-n/2\), every finite \(p>0\) has the full norm
\[
 N_{s,p}(\delta_0)^p=(2\pi)^{-np/2}\omega_n^{p/2}
 \left(1+(1-2^{-n})^{p/2}
       \frac{2^{p(s+n/2)}}{1-2^{p(s+n/2)}}\right).
 \tag{GB16}
\]
At \(s>-n/2\) the annular sequence is unbounded. Thus every global supremum is \(-n/2\), although its endpoint depends on the exponent. Dimension zero has one Fourier piece with empty determinant and inverse factor one, and all finite-coordinate maps reduce to the actual matrix map at a point. The local discrete manifold statements follow on finite compact sets; wavefront sets are empty and the regularity thresholds are \(+\infty\). No sphere of negative dimension, zero denominator, infinite-rank bundle extension or assertion about spatial \(L^p\) exponents is introduced.

## 13. Bundles, anti-duals, and kernels between different manifolds

Let \(E,F\to X\) be smooth complex vector bundles of finite ranks \(e,f\), which need not be equal. An operator \(A\in\Psi^m(X;E,F)\) is represented in local frames by an \(f\times e\) matrix of operators in \(\Psi^m\), with smooth kernel off the diagonal. A new pair of frames changes that matrix by \(G_F A G_E^{-1}\); multiplication by these smooth matrix functions and Section 5 of [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) preserve its class. Coordinate changes are handled by Section 2 componentwise. Its principal symbol therefore is a section class
\[
\sigma_m(A)\in
S^m(T^*X;\operatorname{Hom}(\pi^*E,\pi^*F))
\big/S^{m-1}(T^*X;\operatorname{Hom}(\pi^*E,\pi^*F)).
\tag{G38}
\]
The leading transformation is \(a\mapsto G_FaG_E^{-1}\), since differentiated transition matrices occur only in lower orders. The construction proving (G16), performed in local frames, proves surjectivity onto these symbol classes and identifies the lower-order kernel. Matrix products keep their order, so \(\sigma(BA)=\sigma(B)\sigma(A)\) for compatible bundles. Properness, summation, (G32), and (G34) all apply componentwise and patch by local finiteness. Two-sided ellipticity means that (G38) is fiberwise invertible; that condition forces equal ranks, but it was not imposed on the definition, mapping, composition, or adjoint theorems. The same constructions define \(\Psi^m_{\rho,\delta}(X;E,F)\) in the entire coordinate-invariant range, with the positive-gain principal quotient as described in Section 6 when \(\delta<\rho\).

Half-densities provide an intrinsic pairing. For scalar half-densities \(u,v\) with compact overlap of supports, set \((u,v)=\int_Xu\overline v\); the product is a density, so change of variables makes the integral independent of coordinates and of orientation. Every scalar \(A\in\Psi^m(X;\Omega^{1/2},\Omega^{1/2})\) has an adjoint \(A^*\) in the same class satisfying
\[
(Au,v)=(u,A^*v),\qquad u,v\in C_c^\infty(X;\Omega^{1/2}).
\tag{G39}
\]
Its kernel is \(\overline{K_A(y,x)}\), with the half-density factors interchanged. Locally [From symbol estimates to operators on every Sobolev scale](euclidean-symbol-calculus.md) gives the adjoint symbol
\(a^\dagger=\overline a+\sum_j\partial_{\xi_j}D_{x_j}\overline a\pmod {S^{m-2}}\).
This is of order \(m\), proves the identity for compact tests by Fourier inversion, and defines the distributional adjoint by continuity. Transposing kernel support preserves properness if present; without properness the compact-test identity remains well-defined. The principal symbol is conjugated. For the refined class,
\[
a^\dagger+\frac i2\sum_j\partial_{x_j}\partial_{\xi_j}a^\dagger
=\overline a-\frac i2\sum_j\partial_{x_j}\partial_{\xi_j}\overline a
\pmod {S^{m-2}},
\tag{G40}
\]
which is exactly the complex conjugate of (G14).

For bundles, let \(E^*\) denote the **anti-dual**: its elements are conjugate-linear functionals on \(E\). Use \(\langle u,v\rangle=\overline{v(u)}\), linear in \(u\) and conjugate-linear in \(v\). In components, if vectors change by \(u'=G_Eu\), the anti-dual components change by \(v'=\overline{G_E}^{-T}v\), since \((v')^T\overline{u'}=v^T\overline u\). Thus
\[
A^*\in\Psi^m(X;F^*\otimes\Omega^{1/2},E^*\otimes\Omega^{1/2})
\quad\text{when}\quad
A\in\Psi^m(X;E\otimes\Omega^{1/2},F\otimes\Omega^{1/2}).
\tag{G41}
\]
The local kernel is the conjugate transpose with variables reversed. The anti-dual transformation law just computed makes these kernels agree on overlaps. The principal symbol is the fiberwise adjoint, characterized by the pairing, and (G39) holds for compact smooth \(E\)- and \(F^*\)-valued half-densities. No Hermitian metric identifying \(E\) with \(E^*\) has been silently chosen.

There is also a kernel statement with different source and target manifolds. For smooth finite-rank bundles \(E\to X\), \(F\to Y\), continuous linear maps
\[
C_c^\infty(X;E\otimes\Omega_X^{1/2})
\longrightarrow\mathcal D'(Y;F\otimes\Omega_Y^{1/2})
\tag{G42}
\]
correspond bijectively to distributions on \(Y\times X\) with coefficients in
\[
\operatorname{Hom}(E_x,F_y)\otimes\Omega_{Y\times X}^{1/2}.
\tag{G43}
\]
To prove the adapter, trivialize both bundles and density lines on relatively compact charts. Each component of (G42) is a continuous scalar test-to-distribution map and has a unique scalar kernel by the scalar kernel theorem proved in Sections 13.1–13.5. Under new frames that kernel is multiplied by \(G_F(y)\) on the left and \(G_E(x)^{-1}\) on the right. Under new coordinates the scalar kernel density factor in the input variable combines with the two half-density component laws to give one half-density in each variable. These are exactly the transition functions of (G43), since \(\Omega_{Y\times X}^{1/2}\simeq\Omega_Y^{1/2}\boxtimes\Omega_X^{1/2}\). Uniqueness of the scalar kernel makes the local distributions agree, so they glue to one global kernel.

Conversely take a kernel as in (G43). Pair its input half-density factor with the input half-density and its \(\operatorname{Hom}\) factor with the input section; this leaves a distributional target half-density. More concretely, to pair the result with a compact target dual test section, localize the product of the two compact supports into finitely many chart products and use the scalar kernel pairing there. The transformation rules prove independence of the localization. The scalar kernel theorem supplies continuity on each test-function support space, and the inductive-limit definition of \(C_c^\infty\) supplies global continuity. The two constructions are inverse because they agree on all pairs of scalar test functions in every chart. For topology, this is the same kernel identification with continuous bilinear test pairings as the declared scalar theorem, transported by finite local matrices and locally finite gluing; we do not replace it by an unspecified operator-norm topology. This proves the geometric and bundle content of (G42)–(G43); Sections 13.1–13.6 supply its scalar foundation with the actual support and strong-dual estimates.

### 13.1. Test spaces, bounded supports, and the strong dual

Let \(U\subset\mathbb R^p\) and \(V\subset\mathbb R^q\) be open. Scalar distributions are complex-linear functionals on scalar tests; the pairing in this proof is bilinear, without a complex conjugate. The Lebesgue coordinate density is included in each test pairing; we write only its coefficient. A scalar kernel pairs with \(\Phi(y,x)\,dy\,dx\). For a compact \(K\subset U\), retain the original spaces and seminorms
\[
 \mathcal D_K(U)=\{f\in C^\infty(U):\operatorname{supp}f\subset K\},
 \qquad p_N(f)=\max_{|\alpha|\leq N}\sup_U|\partial^\alpha f|.
 \tag{GK1}
\]
They are complete by Section 14.2 of the Banach foundation lesson. Choose a compact exhaustion \(K_j\subset\operatorname{int}K_{j+1}\) of \(U\), with interiors covering \(U\), as constructed there. Every compact subset lies in some \(K_j\): finitely many of these nested interiors cover it. Give \(\mathcal D(U)=\bigcup_j\mathcal D_{K_j}(U)\) the finest locally convex topology making every inclusion continuous. This is its test-function inductive-limit topology. A seminorm on this union is continuous exactly when its restriction to each \(\mathcal D_{K_j}\) is continuous. Indeed adding such a seminorm to the topology still leaves every inclusion continuous, so the defining finest topology already contains it. Likewise a linear map from this union to a locally convex space is continuous exactly when all its restrictions are continuous: apply the seminorm statement to the target's continuous seminorms. This specifies the topology used below, rather than using only the global derivative seminorms.

A subset \(H\) is bounded if every continuous seminorm has finite supremum on \(H\). It is bounded in \(\mathcal D(U)\) exactly when all its supports lie in one compact \(K\subset U\) and
\[
 \sup_{f\in H}p_N(f)<\infty \quad\text{for every }N.
 \tag{GK2}
\]
To prove the support assertion, suppose no \(K_j\) contains all the supports. Choose \(f_j\in H\) and \(x_j\in U\setminus K_j\) with \(f_j(x_j)\ne0\). Such a point exists because the nonzero set is dense in the support and the complement of \(K_j\) is open. The points eventually leave every compact subset. Set \(a_j=j/|f_j(x_j)|\) and
\[
 P(f)=\sup_j a_j|f(x_j)|.
 \tag{GK3}
\]
For each compactly supported \(f\) only finitely many terms can be nonzero. On each \(\mathcal D_K\) this is a finite maximum of continuous evaluations, bounded by a finite constant times \(p_0\); hence \(P\) is a continuous test-space seminorm. But \(P(f_j)\geq j\), contradicting boundedness. Each global \(p_N\) is also continuous by its restrictions, proving (GK2). Conversely (GK2) makes \(H\) bounded in the fixed-support Fréchet space: every neighborhood contains finitely many seminorm constraints, and a single sufficiently large dilation contains \(H\). Its continuous inclusion into \(\mathcal D(U)\) preserves boundedness. This proves both directions.

Define \(\mathcal D'(U)\) as the continuous dual and its strong topology by the seminorms
\[
 Q_H(u)=\sup_{f\in H}|\langle u,f\rangle|,
 \qquad H\subset\mathcal D(U)\text{ bounded}.
 \tag{GK4}
\]
A scalar functional is a distribution exactly when its restriction to every \(\mathcal D_K\) obeys \(|u(f)|\leq C_Kp_{N_K}(f)\) for some finite \(N_K,C_K\). Continuity gives finitely many seminorm constraints; their increasing order reduces them to one \(p_N\), and rescaling gives this inequality, including the zero-seminorm case. The inequality implies continuity in the reverse direction. Formula (GK2) makes every (GK4) finite. Singletons of tests are bounded, so their evaluations are continuous in the strong dual. The same definitions apply on \(V\) and \(V\times U\).

### 13.2. Product tests and a convergent Fourier expansion

We need a density statement with its support and all derivative orders retained. Let
\[
 I=\prod_{i=1}^p(a_i,b_i),\quad \ell_i=b_i-a_i>0,\qquad
 J=\prod_{j=1}^q(c_j,d_j),\quad s_j=d_j-c_j>0,
 \quad \overline I\subset U,\quad\overline J\subset V.
 \tag{GK5}
\]
Write \(x\in I\), \(y\in J\), and
\[
 e_k(x)=\exp\!\left(2\pi i\sum_i k_i(x_i-a_i)/\ell_i\right),\qquad
 e_l(y)=\exp\!\left(2\pi i\sum_j l_j(y_j-c_j)/s_j\right).
 \tag{GK6}
\]
For \(\Phi\in\mathcal D(J\times I)\), extend it periodically; it is smooth because it is zero near every face. Its coefficients, in output-then-input order, are
\[
 c_{l,k}(\Phi)=\frac1{|J||I|}
       \int_J\int_I\Phi(y,x)e_{-l}(y)e_{-k}(x)\,dx\,dy,
 \qquad |I|=\prod_i\ell_i,\quad |J|=\prod_j s_j.
 \tag{GK7}
\]
Let
\[
 L=1-\sum_i\left(\frac{\ell_i}{2\pi}\right)^2\partial_{x_i}^2
       -\sum_j\left(\frac{s_j}{2\pi}\right)^2\partial_{y_j}^2 .
 \tag{GK8}
\]
Integration by parts has no face terms. For every integer \(r\geq0\),
\[
 c_{l,k}(\Phi)=
  \frac{\int_J\int_I(L^r\Phi)(y,x)e_{-l}(y)e_{-k}(x)\,dx\,dy}
       {|J||I|(1+|k|^2+|l|^2)^r},
\]
\[
 L^r=\sum_{h+|\alpha|+|\beta|=r}
 \frac{r!(-1)^{|\alpha|+|\beta|}}{h!\alpha!\beta!}
 \prod_i\left(\frac{\ell_i}{2\pi}\right)^{2\alpha_i}
 \prod_j\left(\frac{s_j}{2\pi}\right)^{2\beta_j}
 \partial_x^{2\alpha}\partial_y^{2\beta}.
 \tag{GK9}
\]
Here the sum includes \(h=r,\alpha=\beta=0\); no constant term is suppressed. Taking the absolute value of the numerator yields the coefficient estimate with this entire finite differential operator. In particular the coefficients decay faster than every power of \((1+|k|^2+|l|^2)^{1/2}\).

We justify the periodic inversion needed here. On a circle of its actual length \(\ell\), the Fejér kernel is
\[
 F_N(t)=\frac1{N+1}\left|\sum_{\nu=0}^N e^{2\pi i\nu t/\ell}\right|^2
 =\sum_{|k|\leq N}\left(1-\frac{|k|}{N+1}\right)e^{2\pi ikt/\ell}.
 \tag{GK10}
\]
It is nonnegative and \(\ell^{-1}\int_0^\ell F_N=1\), by integrating the finite sum. Away from \(t=0\) modulo \(\ell\), the finite geometric sum gives
\(F_N(t)\leq[(N+1)\sin^2(\pi t/\ell)]^{-1}\). Thus the mass outside circular distance \(\delta\), \(0<\delta<\ell/2\), is at most \([(N+1)\sin^2(\pi\delta/\ell)]^{-1}\). The product kernels over all \(p+q\) circles, with their respective factors \(1/\ell_i\) and \(1/s_j\) in convolution, have total mass one. Their mass outside a product of small circular intervals is bounded by the sum of these one-coordinate tail bounds. Uniform continuity on the compact period box then proves uniform convergence of their convolutions to any continuous periodic function: inside the small intervals bound the difference by its modulus of continuity, and outside bound it by twice the supremum times that tail mass.

For a smooth function the same argument applies to each derivative, since differentiating the periodic convolution differentiates the smooth function under a finite integral. These convolutions are the finite Fourier sums with coefficient multiplier
\[
 \prod_i\left(1-\frac{|k_i|}{N+1}\right)_+
 \prod_j\left(1-\frac{|l_j|}{N+1}\right)_+ .
 \tag{GK11}
\]
On the other hand (GK9), with \(r\) as large as needed, makes the unweighted Fourier series and each of its differentiated series absolutely uniformly convergent. The convergence of the lattice sums follows directly by grouping vectors in shells \(2^h\leq|(k,l)|<2^{h+1}\): there are at most \((2^{h+2}+1)^{p+q}\) vectors, whereas a power of exponent exceeding \(p+q\) gives a summable geometric bound. Dominated convergence for these absolutely summable series makes the sums with (GK11) converge to the unweighted sum. The preceding convolution limit identifies that sum with \(\Phi\). Uniform convergence of all derivative series also verifies termwise differentiation, by the fundamental theorem of calculus on coordinate segments.

Choose \(\sigma\in\mathcal D(I)\), \(\tau\in\mathcal D(J)\), equal to one on neighborhoods of the respective projections of \(\operatorname{supp}\Phi\). Multiplication gives
\[
 \Phi(y,x)=\sum_{l\in\mathbb Z^q,\ k\in\mathbb Z^p}
       c_{l,k}(\Phi)\,\tau(y)e_l(y)\,\sigma(x)e_k(x).
 \tag{GK12}
\]
Its finite partial sums converge in every smooth seminorm with support in the fixed compact \(\operatorname{supp}\tau\times\operatorname{supp}\sigma\). This follows from the derivative convergence just proved and the full finite product rule for the two cutoffs. Therefore this is convergence in a fixed-support test space.

For an arbitrary compactly supported test on \(V\times U\), finitely many boxes \(I_i,J_j\) of the form (GK5) cover its compact projections. Choose bumps \(0\leq\beta_i\leq1\) supported in \(I_i\), each equal to one on a smaller set, with those smaller sets covering the input projection. Define
\[
 \chi_i=\beta_i\prod_{h<i}(1-\beta_h),\qquad
 \sum_i\chi_i=1-\prod_i(1-\beta_i).
 \tag{GK13}
\]
The last function is one near that projection; the identity follows by telescoping successive products. Construct \(\eta_j\) on the output projection in the same way. Then
\(\Phi=\sum_{j,i}\eta_j(y)\chi_i(x)\Phi(y,x)\), with each piece compactly supported in \(J_j\times I_i\). Apply (GK12) to every piece. Finite sums of product tests are consequently dense in \(\mathcal D(V\times U)\), with convergence in one fixed compact-support space for each given test. This proof uses only elementary smooth bumps on boxes, finite products, scalar integration and the displayed Fourier series; it does not assume a kernel theorem.

### 13.3. Separate continuity gives a fixed-support estimate

Let \(B:\mathcal D(U)\times\mathcal D(V)\to\mathbb C\) be bilinear and separately continuous. Fix compacts \(K\subset U\), \(H\subset V\). Write \(p_N,q_M\) for their increasing derivative seminorms. There are finite orders \(N,M\) and a constant \(C\) such that
\[
 |B(f,g)|\leq C p_N(f)q_M(g),
 \qquad f\in\mathcal D_K(U),\quad g\in\mathcal D_H(V).
 \tag{GK14}
\]
Here is the complete argument. For positive integers \(m\) and integers \(M\geq0\), put
\[
 E_{m,M}=\{f\in\mathcal D_K:|B(f,g)|\leq m q_M(g)
                                      \text{ for every }g\in\mathcal D_H\}.
 \tag{GK15}
\]
Every set is closed, by continuity in \(f\) for each \(g\). They cover \(\mathcal D_K\), because each continuous functional \(B(f,\cdot)\) has a finite-order bound. Completeness and the complete-metric Baire theorem proved in Section 6 of the Banach foundation lesson show that one \(E_{m,M}\) has interior. Choose \(f_0\) in that interior and \(r>0,N\) such that \(f_0+h\in E_{m,M}\) when \(p_N(h)<r\). Subtract the two inequalities for \(f_0+h\) and \(f_0\): \(|B(h,g)|\leq2m q_M(g)\). Rescaling \(h\ne0\) to \(r h/(2p_N(h))\) gives (GK14) with \(C=4m/r\). If the seminorm is zero, use arbitrary positive rescaling to obtain zero; on these test spaces \(p_N\) already separates points. This proves joint continuity on each pair of fixed supports, without claiming a single order works for every support.

In fact continuity on every pair of fixed supports is sufficient here in place of global separate continuity. For fixed \(g\), its support is contained in one \(H\), and (GK14) on each \(K\) makes \(f\mapsto B(f,g)\) continuous on the inductive limit. The reverse variable follows in the same way.

### 13.4. Construction of the local scalar kernel

Retain \(I,J\) and choose smaller boxes \(I_0,J_0\) with \(\overline I_0\subset I\), \(\overline J_0\subset J\). Fix cutoffs \(\sigma,\tau\) equal to one near these smaller closures and supported in \(I,J\). For \(\Phi\in\mathcal D(J_0\times I_0)\), define
\[
 T_{J_0,I_0}(\Phi)=\sum_{l,k}c_{l,k}(\Phi)
                          B(\sigma e_k,\tau e_l).
 \tag{GK16}
\]
The series is absolutely convergent. To verify this with all its constants, apply (GK14) to \(\operatorname{supp}\sigma,\operatorname{supp}\tau\). The product rule gives the bounds
\[
 p_N(\sigma e_k)\leq A_N(k):=
 \max_{|\gamma|\leq N}
 \sum_{\alpha\leq\gamma}\binom{\gamma}{\alpha}
 \|\partial^\alpha\sigma\|_\infty
 \prod_i\left(\frac{2\pi|k_i|}{\ell_i}\right)^{\gamma_i-\alpha_i},
\]
\[
 q_M(\tau e_l)\leq B_M(l):=
 \max_{|\delta|\leq M}
 \sum_{\beta\leq\delta}\binom{\delta}{\beta}
 \|\partial^\beta\tau\|_\infty
 \prod_j\left(\frac{2\pi|l_j|}{s_j}\right)^{\delta_j-\beta_j}.
 \tag{GK17}
\]
Zero powers are one, including a zero frequency. These are bounded by constants times \((1+|k|)^N,(1+|l|)^M\), respectively, as is seen by expanding the displayed finite sums. Combining (GK9), (GK14) and (GK17) yields
\[
 |T_{J_0,I_0}(\Phi)|
 \leq \frac{C}{|J||I|}
       \int_J\int_I|L^r\Phi(y,x)|\,dx\,dy
       \sum_{l,k}\frac{A_N(k)B_M(l)}
                         {(1+|k|^2+|l|^2)^r},
 \qquad 2r>N+M+p+q.
 \tag{GK18}
\]
The shell estimate in Section 13.2 proves the sum finite with precisely this strict inequality. The full expression for \(L^r\) in (GK9) bounds its integral by a finite sum of the original derivative supremums of order at most \(2r\), times \(|J||I|\). Thus (GK18) proves distributional continuity on every compact support in the smaller box.

For a product \(\Phi(y,x)=g(y)f(x)\), \(f\in\mathcal D(I_0)\), \(g\in\mathcal D(J_0)\), Fubini gives \(c_{l,k}(\Phi)=c_l(g)c_k(f)\), with their respective volume factors from (GK7). The cutoff Fourier sums for \(f,g\) converge in their fixed-support test spaces. Joint continuity (GK14) and the absolute convergence of (GK16) therefore give
\[
 T_{J_0,I_0}(g\otimes f)=B(f,g).
 \tag{GK19}
\]
If different boxes or cutoffs give two local kernels, both give this value on every product test in the intersection. Intersections of the smaller coordinate boxes are again products of boxes, possibly empty. The product-test density in Section 13.2 and distributional continuity prove equality on the entire intersection. This establishes independence of the construction.

### 13.5. The global kernel and continuity into the strong dual

The smaller boxes of Section 13.4 cover \(V\times U\). Their local kernels glue as follows. For a compactly supported \(\Phi\), choose finitely many input and output boxes and the functions \(\chi_i,\eta_j\) of (GK13), and put
\[
 T(\Phi)=\sum_{j,i}T_{J_j,I_i}(\eta_j(y)\chi_i(x)\Phi(y,x)).
 \tag{GK20}
\]
Here \(I_i,J_j\) denote smaller boxes, each equipped with its larger box and local kernel. For a second choice, insert both product partitions. Their sums are one near \(\operatorname{supp}\Phi\), so expanding gives the same finite double refinement. On each refined support the local distributions agree by Section 13.4. This proves independence, hence linearity by choosing one partition for the union of finitely many test supports. For any fixed compact support, choose one such finite partition once. The finitely many estimates (GK18), followed by the full product rule for \(\eta_j\chi_i\Phi\), give a finite-order bound there. Thus \(T\in\mathcal D'(V\times U)\). Partitioning \(f,g\) in (GK19) proves \(T(g\otimes f)=B(f,g)\) for arbitrary tests. Product-test density proves uniqueness.

Conversely, if \(T\in\mathcal D'(V\times U)\), define \(B(f,g)=T(g\otimes f)\). On a fixed product of supports, the distribution estimate of order \(R\) gives
\[
 |B(f,g)|\leq C
 \max_{|\alpha|+|\beta|\leq R}
       \|\partial_x^\alpha f\|_\infty
       \|\partial_y^\beta g\|_\infty
 \leq C p_R(f)q_R(g).
 \tag{GK21}
\]
This proves separate continuity on the inductive limits and joint continuity at fixed supports. It also defines a distribution \(Af\) by \(\langle Af,g\rangle=B(f,g)\). For a bounded set \(H\subset\mathcal D(V)\), Section 13.1 supplies a common compact output support and bounds for every \(q_R\). For a fixed input compact \(K\), (GK21) consequently gives
\[
 Q_H(Af)\leq C p_R(f)\sup_{g\in H}q_R(g),\qquad f\in\mathcal D_K(U).
 \tag{GK22}
\]
Thus \(A:\mathcal D_K(U)\to\mathcal D'(V)\) is continuous for every strong-dual seminorm. The inductive-limit criterion proves continuity of \(A:\mathcal D(U)\to\mathcal D'(V)\) in the strong topology.

If we start instead with such a continuous linear \(A\), then \(B(f,g)=\langle Af,g\rangle\) is separately continuous: for fixed \(g\), its evaluation is a continuous strong-dual seminorm; for fixed \(f\), \(Af\) is a distribution. Sections 13.3–13.5 give its unique kernel. These constructions are inverse by their values on every pair of tests. We have proved the exact bijection among scalar distributions on \(V\times U\), separately continuous bilinear test pairings, and continuous linear test-to-strong-distribution maps. We assert the displayed continuity statements, with their actual support-dependent orders; no extra topology on the space of all operators is being substituted.

If an open set is empty, its test and distribution spaces are zero and the assertion reduces to the unique zero map. If a coordinate dimension is zero, its nonempty Euclidean open set is the one-point space, its test space is \(\mathbb C\), and the sums, volume factors and products over its empty coordinate list are respectively one term, one and one. The same formulas give the asserted bijection.

### 13.6. The exact elementary distribution operations

Restriction from \(U\) to an open \(W\subset U\) is \(\langle u|_W,f\rangle=\langle u,\widetilde f\rangle\), with the compact test extended by zero. That extension is smooth and continuous on each fixed-support space, so restriction is well defined. Extension sends bounded test sets to bounded test sets by (GK2); hence restriction is also continuous between the strong distribution duals.

For \(a\in C^\infty(U)\), define \(\langle au,f\rangle=\langle u,af\rangle\), and define \(\langle\partial^\alpha u,f\rangle=(-1)^{|\alpha|}\langle u,\partial^\alpha f\rangle\). Both test operations preserve compact supports and bounded sets, by the complete finite product rule and the derivative seminorms. They therefore give continuous strong-dual operations. Differentiating once and using the test product rule gives \(\partial_j(au)=(\partial_j a)u+a\partial_j u\), including both signs from the pairing definition. Induction using Pascal's identity proves the complete multi-index formula
\[
 \partial^\alpha(au)=
   \sum_{\beta\leq\alpha}\binom{\alpha}{\beta}
                (\partial^\beta a)\partial^{\alpha-\beta}u.
 \tag{GK23}
\]

If \(\operatorname{supp}u\subset K\subset U\) is compact, choose \(\zeta\in\mathcal D(U)\) equal to one on a neighborhood of \(K\). Then \(u\) acts on every \(g\in C^\infty(U)\) by \(u(\zeta g)\). The value is independent of \(\zeta\). To see the locality being used, a compact test supported outside \(\operatorname{supp}u\) has a finite cover by boxes on which \(u\) vanishes. The finite bump construction (GK13) splits the test into tests on those boxes, proving its value zero. The difference of two cutoff products is supported outside a neighborhood of \(K\), so this locality proves independence. The distribution estimate on \(\operatorname{supp}\zeta\), with its finite order \(N\), gives the entire bound
\[
 |u(g)|\leq C
 \max_{|\gamma|\leq N}
 \sum_{\alpha\leq\gamma}\binom{\gamma}{\alpha}
       \|\partial^\alpha\zeta\|_\infty
       \sup_{\operatorname{supp}\zeta}
                    |\partial^{\gamma-\alpha}g|.
 \tag{GK24}
\]
For \(U=\mathbb R^p\) this is a bound by a finite collection of the original Schwartz seminorms, so the compactly supported distribution is tempered. For a general \(U\), \(f\mapsto u(\zeta f|_U)\) similarly gives its canonical compactly supported extension to \(\mathbb R^p\), independent of the chosen cutoff. Its support is exactly the original support: tests near that compact set recover \(u\), and tests away from it give zero. This proves the finite-order statement without replacing the original compact set or discarding the cutoff derivatives.

For \(u\in\mathcal D'(U)\), \(v\in\mathcal D'(V)\), the bilinear form \(B(f,g)=u(f)v(g)\) is separately continuous. Its kernel, just proved, is their product distribution, denoted \(v\otimes u\) in output-then-input order. There is also the exact iterated formula
\[
 \langle v\otimes u,\Phi\rangle
    =u\!\left(x\mapsto v(\Phi(\,\cdot\,,x))\right)
    =v\!\left(y\mapsto u(\Phi(y,\,\cdot\,))\right).
 \tag{GK25}
\]
Indeed the first inner pairing is a smooth compactly supported function of \(x\): on a fixed product support the finite-order bound for \(v\), applied to the Taylor remainder in each \(x\)-direction with all \(y\)-derivatives through that order, proves differentiation under the pairing of every order. Its support is in the input projection. The finite-order bounds of \(u,v\) make the resulting functional continuous on each product support. It agrees with \(u(f)v(g)\) on product tests, so density proves the first equality; reversing the roles proves the second. No interchange of undefined integrals is used.

Its support is exactly \(\operatorname{supp}v\times\operatorname{supp}u\). Outside this product, each point has a product neighborhood with one distribution zero, and (GK24), or product-test density, makes the product zero there. At a point in the product, every product neighborhood contains tests \(f,g\) with \(u(f)\ne0,v(g)\ne0\), by the definition of support. Their product test gives a nonzero value. Every neighborhood contains such a product neighborhood, proving the reverse inclusion, including zero distributions.

For a smooth diffeomorphism \(H:W\to U\), scalar pullback is
\[
 \langle H^*u,f\rangle
  =\left\langle u,(f\circ H^{-1})|\det DH^{-1}|\right\rangle .
 \tag{GK26}
\]
The transformed support is \(H(\operatorname{supp}f)\), a compact subset of \(U\). Every derivative of the transformed test is a finite sum of chain and product terms containing the derivatives of \(f,H^{-1}\) and the entire positive absolute Jacobian. On a fixed compact, all these latter coefficients are bounded. Thus this test map is continuous and carries bounded sets to bounded sets, proving strong-dual continuity of pullback. The full change-of-variables formula verifies (GK26) for a smooth scalar function; applying the determinant chain rule to two diffeomorphisms proves the composition law and that the inverse pullback is its inverse. Orientation reversal changes no absolute Jacobian. This is a diffeomorphic pullback; no pullback for arbitrary smooth maps or multiplication of two arbitrary distributions is asserted.

These arguments prove the scalar kernel, restriction, product and coordinate operations used in Section 13. Fourier operations still use their precise Schwartz or compact-support domains and the Fourier proofs named at the beginning of the lesson. The finite matrix and half-density adapter (G42)–(G43) retains those original factors and transition laws.

### 13.7. Convolution with its actual support and derivative bounds

We use scalar distributions paired with the original coordinate density \(dx\) on \(\mathbb R^n\), and \(D_j=-i\partial_j\). Let \(u\in\mathcal D'(\mathbb R^n)\), and let \(s\) have compact support \(K\). Fix \(\zeta\in\mathcal D\), equal to one near \(K\), and set \(L=\operatorname{supp}\zeta\). The constant \(C_s\) and order \(N_s\) below are those in the distribution estimate for \(s\) on \(L\). For \(\phi\in\mathcal D\) define
\[
 F_s\phi(x)=s_y\bigl(\phi(x+y)\bigr),\qquad
 (u*s)(\phi)=u_x(F_s\phi(x)).
 \tag{GC1}
\]
The inner pairing means \(s_y(\zeta(y)\phi(x+y))\). Its value is independent of the chosen cutoff by the locality proved in Section 13.6. Taylor's formula in an \(x_j\)-direction, with all \(y\)-derivatives through order \(N_s\), shows that it is smooth and that every \(x\)-derivative passes under the pairing. The remainder divided by the increment tends uniformly to zero on each compact parameter set and on \(L\), including those finitely many derivatives; the finite-order estimate therefore makes its paired remainder tend to zero.

If \(\operatorname{supp}\phi\subset P\) is compact, then \(\operatorname{supp}F_s\phi\subset P-K\subset P-L\). Indeed when \(x\notin P-K\), the function \(y\mapsto\phi(x+y)\) vanishes near \(K\). The same holds for all nearby \(x\), because the two compact sets are disjoint. Thus locality proves the support assertion. For every \(\alpha\), the entire finite-order estimate is
\[
 \sup_x|\partial_x^\alpha F_s\phi(x)|
 \leq C_s\max_{|\gamma|\leq N_s}
 \sum_{\eta\leq\gamma}\binom{\gamma}{\eta}
 \|\partial^\eta\zeta\|_\infty
 \sup_{z\in\mathbb R^n}|\partial^{\alpha+\gamma-\eta}\phi(z)|.
 \tag{GC2}
\]
No derivative of the cutoff is omitted. This proves that \(F_s:\mathcal D_P\to\mathcal D_{P-L}\) is continuous. Applying the finite-order bound for \(u\) on the fixed compact \(P-L\) proves that (GC1) is a distribution, with a bound using orders through \(N_u+N_s\). It also proves that \(u\mapsto u*s\) is continuous for the strong distribution topology: (GC2) sends every bounded test set to a bounded test set with common compact support, so the strong seminorm \(Q_H(u*s)\) is exactly \(Q_{F_sH}(u)\).

The set \(\operatorname{supp}u+K\) is closed. If \(x_j+y_j\) converges, with \(x_j\in\operatorname{supp}u\) and \(y_j\in K\), a subsequence of \(y_j\) converges in \(K\), and then \(x_j\) converges in the closed support of \(u\). If a test support avoids this sum, the inner function in (GC1) vanishes near \(\operatorname{supp}u\). Consequently
\[
 \operatorname{supp}(u*s)\subset\operatorname{supp}u+K.
 \tag{GC3}
\]
This is an inclusion; cancellation may make it strict.

Choose also \(\rho\in\mathcal D\) equal to one near \(P-L\). The smooth compact test \(\rho(x)\zeta(y)\phi(x+y)\) permits both iterated pairings in (GK25). Its value in the order \(u_xs_y\) is (GC1). In the reverse order, for every \(y\in L\) the support of \(x\mapsto\phi(x+y)\) lies in \(P-L\), so \(\rho\) can be removed. This proves commutativity and independence of both auxiliary cutoffs. Differentiating the output distribution and differentiating either factor give exactly
\[
 \partial^\alpha(u*s)
    =(\partial^\alpha u)*s=u*(\partial^\alpha s),\qquad
 D^\alpha(u*s)=(D^\alpha u)*s=u*(D^\alpha s).
 \tag{GC4}
\]
For the first equality, the factor \((-1)^{|\alpha|}\) in the test definition of \(\partial^\alpha u\) differentiates \(\phi(x+y)\) in \(x\). For the second, the same factor differentiates it in \(y\); those derivatives equal the output derivatives. The extension of \(\partial^\alpha s\) to smooth functions still satisfies that formula, since derivatives of its cutoff are supported away from \(K\) and pair to zero. Multiplying by the full constant \((-i)^{|\alpha|}\) gives the \(D\) identities. Taking \(s=\delta_0\) in (GC1) proves \(u*\delta_0=u\).

Let now \(t\) also have compact support, with cutoff support \(L_t\). For a test supported in \(P\), choose an \(x\)-cutoff equal to one near \(P-L-L_t\), and insert the two compact-factor cutoffs. Their product times \(\phi(x+y+z)\) is a compact smooth test on the full product. All its iterated pairings exist; the finite-order bounds justify parameter derivatives at every step. Repeated (GK25) identifies the different orders. More explicitly, the triple functionals are continuous on every fixed product support by the three finite-order estimates and agree on all products of three tests. Applying the product-test density of Section 13.2 first to two variables and then to the third proves their equality on every such test. Both definitions of iterated convolution therefore have the same value
\[
 ((u*s)*t)(\phi)=(u*(s*t))(\phi)
       =u_xs_yt_z\bigl(\phi(x+y+z)\bigr).
 \tag{GC5}
\]
Here \(s*t\) has compact support in \(K+\operatorname{supp}t\) by (GC3), so its pairing with a smooth function is already defined. Removal of each cutoff is valid on precisely the compact support just described. Commutativity then proves associativity for any ordering in which all but at most one factor have compact support. This argument does not assign a convolution to an arbitrary pair of noncompact distributions.

### 13.8. The full Schwartz estimate for a compact convolution factor

Use the original seminorms \(p_{\alpha,\beta}(\phi)=\sup_x|x^\alpha\partial^\beta\phi(x)|\), with every monomial and derivative retained. For the same compact factor \(s\), the function in (GC1) satisfies
\[
\begin{aligned}
 p_{\alpha,\beta}(F_s\phi)
 \leq{}&C_s\max_{|\gamma|\leq N_s}
 \sum_{\eta\leq\gamma}\binom{\gamma}{\eta}
          \|\partial^\eta\zeta\|_\infty\\
 &\times\sum_{\kappa\leq\alpha}\binom{\alpha}{\kappa}
    \sup_{y\in L}|y^{\alpha-\kappa}|
             p_{\kappa,\beta+\gamma-\eta}(\phi).
\end{aligned}
 \tag{GC6}
\]
To prove it, apply (GK24) in the \(y\)-variable to \(x^\alpha\partial_x^\beta\phi(x+y)\), treating \(x^\alpha\) as constant during those derivatives. Then use the full expansion
\[
 x^\alpha=\sum_{\kappa\leq\alpha}\binom{\alpha}{\kappa}
       (x+y)^\kappa(-y)^{\alpha-\kappa}.
 \tag{GC7}
\]
Taking absolute values and suprema gives (GC6). The parameter argument from Section 13.7 proves smoothness. The bound proves membership in \(\mathcal S\) and continuity of \(F_s:\mathcal S\to\mathcal S\), using a finite list of the original seminorms for each requested one. No weighted factor has been absorbed into a replacement seminorm.

For \(u\in\mathcal S'\), formula (GC1) now defines a continuous functional on \(\mathcal S\). On compact tests it is the convolution already constructed; hence
\[
 u\in\mathcal S',\quad s\text{ compactly supported}
       \quad\Longrightarrow\quad u*s\in\mathcal S'.
 \tag{GC8}
\]
It is continuous in \(u\) for the strong Schwartz dual: a bounded Schwartz set has a finite supremum for every original seminorm, and (GC6) carries it to another bounded set. The exact dual seminorm is again \(T_H(u*s)=T_{F_sH}(u)\). Completeness and this description of Schwartz boundedness were proved in Sections 4.1 and 4.5 of [Two measuring scales, one Weyl product](weyl-metric-products.md).

### 13.9. Smooth parameter pairings and distributional approximation

Let \(k(x,y)\) be smooth on an open set containing \(Y\times K\), where \(Y\subset\mathbb R^a\) is open and \(s\) has compact support \(K\). Near any fixed compact parameter neighborhood \(Y_0\Subset Y\), compactness gives a \(y\)-neighborhood of \(K\) and a slightly larger parameter neighborhood on whose product \(k\) is smooth. Choose \(\zeta\) supported in that \(y\)-neighborhood and equal to one near \(K\). The function
\[
 h(x)=s_y(k(x,y)),\qquad
 \partial_x^\alpha h(x)=s_y(\partial_x^\alpha k(x,y))
 \tag{GC9}
\]
is well defined and smooth on \(Y\). Independence of the cutoff follows from locality. For every \(\alpha\) its actual bound on \(Y_0\) is
\[
 \sup_{x\in Y_0}|\partial_x^\alpha h(x)|
 \leq C_s\max_{|\gamma|\leq N_s}
 \sum_{\eta\leq\gamma}\binom{\gamma}{\eta}
 \|\partial^\eta\zeta\|_\infty
 \sup_{\substack{x\in Y_0\\y\in L}}
        |\partial_x^\alpha\partial_y^{\gamma-\eta}k(x,y)|.
 \tag{GC10}
\]
For the derivative assertion, apply the fundamental theorem of calculus to the difference quotient in a parameter direction. The difference from \(\partial_{x_j}k\), and each \(y\)-derivative through order \(N_s\), tends uniformly to zero on the fixed product compact. Estimate (GC10) therefore proves differentiation under the pairing. Iterating proves every order. If the kernel has a singular set, the argument applies locally whenever this product neighborhood avoids that set; this is the precise hypothesis needed for off-singularity smoothness.

In particular, when \(v\) is compactly supported and a distribution \(f\) is represented by a smooth function near every difference \(x-y\), with \(x\in Y\) and \(y\in\operatorname{supp}v\), the restriction of \(f*v\) to \(Y\) is the smooth function \(v_y(f(x-y))\). To verify equality as distributions, take a test supported in a compact subset of \(Y\). All relevant differences form a compact set in the smooth region. Insert a cutoff in that region, use (GK25) to exchange the two finite-order pairings, and use the original Lebesgue substitution \(z=x+y\), with absolute Jacobian one. This gives exactly the integral of the stated smooth function against the test. The parts of \(f\) outside that region pair to zero because the inner test vanishes there. This proves the claimed representation, rather than merely the smoothness of a separately defined function.

For an arbitrary \(u\in\mathcal D'\) and \(r\in\mathcal D\), the convolution \(u*r\) is smooth. On a compact output neighborhood, all \(y\)-arguments in \(r(x-y)\) lie in one compact set. Insert a cutoff there into \(u\), making it a compact distribution, and apply (GC9). The same change of variables and iterated pairing identify the result with (GC1). Thus
\[
 (u*r)(x)=u_y(r(x-y)),\qquad
 \partial^\alpha(u*r)(x)=u_y(\partial^\alpha r(x-y)).
 \tag{GC11}
\]
For the useful approximation statement, let \(r\in\mathcal D\) have integral one, and retain the full scaled function \(r_\varepsilon(y)=\varepsilon^{-n}r(y/\varepsilon)\), \(0<\varepsilon\leq1\). For a bounded test set \(H\), Section 13.1 gives a common compact support \(P\) and finite bounds for every derivative. The tests \(F_{r_\varepsilon}\phi\) are supported in the common compact \(P-\{tz:0\leq t\leq1,\ z\in\operatorname{supp}r\}\). The substitution \(y=\varepsilon z\) retains both the scaled factor and the Jacobian, yielding
\[
 F_{r_\varepsilon}\phi(x)-\phi(x)
       =\int r(z)\bigl(\phi(x+\varepsilon z)-\phi(x)\bigr)\,dz.
 \tag{GC12}
\]
The fundamental theorem of calculus along the actual segment gives, for every \(\alpha\),
\[
 \sup_x|\partial^\alpha(F_{r_\varepsilon}\phi-\phi)(x)|
 \leq\varepsilon\sum_{j=1}^n
       \left(\int|r(z)|\,|z_j|\,dz\right)
       \sup_x|\partial^{\alpha+e_j}\phi(x)|.
 \tag{GC13}
\]
Apply the fixed finite-order estimate for \(u\) on that common compact and then take the supremum over \(\phi\in H\). Its right side tends to zero. Therefore the smooth distributions \(u*r_\varepsilon\) converge to \(u\) in the strong distribution topology. This proves a stronger statement than convergence on each individual test, with the same original smoothing functions and no positivity requirement on \(r\).

### 13.10. Compact Fourier pairings and the receiving inverse identities

Retain the original transform \(\widehat f(\xi)=\int e^{-ix\cdot\xi}f(x)\,dx\) and inverse factor \((2\pi)^{-n}\). For a compact distribution \(s\) in the frequency variable, (GC9) proves that
\[
 H(x)=(2\pi)^{-n}s_\xi(e^{ix\cdot\xi}),\qquad
 \partial_x^\alpha H(x)
        =(2\pi)^{-n}s_\xi((i\xi)^\alpha e^{ix\cdot\xi})
 \tag{GC14}
\]
is smooth. All pairings include the cutoff \(\zeta(\xi)\) used in (GK24). For clarity, every derivative entering that finite-order bound is the complete expression
\[
 \partial_\xi^\nu\bigl((i\xi)^\alpha e^{ix\cdot\xi}\bigr)
 =i^{|\alpha|}
   \sum_{\substack{\lambda\leq\nu\\\lambda\leq\alpha}}
   \binom{\nu}{\lambda}\frac{\alpha!}{(\alpha-\lambda)!}
   \xi^{\alpha-\lambda}(ix)^{\nu-\lambda}e^{ix\cdot\xi}.
 \tag{GC15}
\]
Combining (GC15) with (GK24), with \(\nu=\gamma-\eta\), gives
\[
\begin{aligned}
 |\partial_x^\alpha H(x)|\leq{}&(2\pi)^{-n}C_s
 \max_{|\gamma|\leq N_s}
 \sum_{\eta\leq\gamma}\binom{\gamma}{\eta}
       \|\partial^\eta\zeta\|_\infty\\
 &\times\sum_{\substack{\lambda\leq\gamma-\eta\\\lambda\leq\alpha}}
   \binom{\gamma-\eta}{\lambda}\frac{\alpha!}{(\alpha-\lambda)!}
   \sup_{\xi\in L}|\xi^{\alpha-\lambda}|
   |x^{\gamma-\eta-\lambda}|.
\end{aligned}
 \tag{GC16}
\]
Thus every derivative has polynomial growth of degree at most the original order \(N_s\), with its entire constant displayed. The powers of \(i\) in (GC15) have modulus one for real \(x,\xi\); no sign or power is lost from the identity.

The smooth function in (GC14) represents the inverse Fourier distribution. Indeed, for \(\phi\in\mathcal S\),
\[
 \int H(x)\phi(x)\,dx
  =(2\pi)^{-n}s_\xi\left(\int e^{ix\cdot\xi}\phi(x)\,dx\right)
  =(2\pi)^{-n}s_\xi\bigl(\widehat\phi(-\xi)\bigr)
  =\langle\mathcal F^{-1}s,\phi\rangle.
 \tag{GC17}
\]
To justify the first equality, truncate the \(x\)-integral to compact boxes and approximate there by Riemann sums in the smooth \(\xi\)-topology on \(L\). Uniform convergence of every derivative through order \(N_s\) permits the finite-order pairing. The tail of each such derivative is bounded by a constant times \(\int_{|x|>R}(1+|x|)^{N_s}|\phi(x)|\,dx\), which tends to zero by the original Schwartz decay. Bound (GC16) also gives convergence of the outer integral. The last expression is precisely the transpose definition of the inverse transform at the declared Fourier entry base. Hence (GC17) proves the asserted identification.

The same argument with \(e^{-iy\cdot\xi}\), without an inverse prefactor, proves that \(\widehat s(\xi)=s_y(e^{-iy\cdot\xi})\) is smooth. Every frequency derivative has polynomial growth of degree at most \(N_s\), by the full version of (GC15) with the negative phase. Multiplication by \(\widehat s\) consequently preserves \(\mathcal S\): the complete product rule for \(x^\alpha\partial^\beta(\widehat s\phi)\) is a sum over every \(\eta\leq\beta\), with coefficient \(\binom{\beta}{\eta}\); its polynomial growth is bounded by the finite multinomial expansion of \((1+\sum_j|x_j|)^{N_s}\) and the corresponding original monomial seminorms of \(\phi\).

For \(u\in\mathcal S'\) and compact \(s\), the exact transform identity is
\[
 \widehat{u*s}=\widehat s\,\widehat u.
 \tag{GC18}
\]
On a Schwartz test \(\psi\), its proof is the test identity
\[
 F_s(\widehat\psi)(x)
   =s_y\left(\int e^{-i(x+y)\cdot\xi}\psi(\xi)\,d\xi\right)
   =\int e^{-ix\cdot\xi}\widehat s(\xi)\psi(\xi)\,d\xi
   =\widehat{\widehat s\psi}(x).
 \tag{GC19}
\]
The compact-factor finite-order bound justifies passing its pairing through the integral, exactly as in (GC17); the additional \(x\)-derivatives require only further powers of \(\xi\), all integrable against the Schwartz test. Both sides are Schwartz functions by (GC6) and the multiplier bound just proved. Pairing (GC19) with \(u\), using the transpose definition \(\langle\widehat u,\psi\rangle=\langle u,\widehat\psi\rangle\), proves (GC18). No pairing of an arbitrary distribution against a non-Schwartz function is used.

The noncompact Schwartz input in (L14) also requires its actual convolution, which we now construct. If \(u\in\mathcal S'\) and \(r\in\mathcal S\), define
\[
 h(x)=u_y(r(x-y)),\qquad
 \partial_x^\eta h(x)=u_y(\partial^\eta r(x-y)).
 \tag{GC20}
\]
For each fixed \(x\) the argument is Schwartz. Its full bound in the original seminorms is
\[
 p_{\alpha,\beta}^{(y)}(\partial_x^\eta r(x-y))
 \leq\sum_{\kappa\leq\alpha}\binom{\alpha}{\kappa}
       |x^{\alpha-\kappa}|p_{\kappa,\beta+\eta}(r).
 \tag{GC21}
\]
This follows from \(y=x-(x-y)\) by the complete multinomial rule; \(\partial_y^\beta\) supplies the sign \((-1)^{|\beta|}\). Taylor's formula for a parameter increment, including each \(y\)-derivative and monomial weight in (GC21), bounds the difference-quotient remainder by the increment times a finite sum of the next derivative seminorms of \(r\), uniformly on each compact parameter set. Thus the map into \(\mathcal S\) is smooth in every original seminorm. Applying the continuous functional \(u\) proves (GC20), and its finite-seminorm estimate combined with (GC21) proves polynomial growth of every derivative. In particular \(h\) is a tempered distribution.

Its distributional formula is \((u*r)(\phi)=u(F_r\phi)\), where \(F_r\phi(x)=\int r(y)\phi(x+y)\,dy\) and
\[
 p_{\alpha,\beta}(F_r\phi)
 \leq\sum_{\kappa\leq\alpha}\binom{\alpha}{\kappa}
       \left(\int |r(y)|\,|y^{\alpha-\kappa}|\,dy\right)
                  p_{\kappa,\beta}(\phi).
 \tag{GC22}
\]
The same complete expansion as (GC7) proves the bound, and differentiation under this absolutely convergent integral proves smoothness. To identify this functional with the function \(h\), integrate \(\phi(x)r(x-y)\) first over a compact \(x\)-box. Riemann sums converge in every Schwartz seminorm in \(y\), by (GC21) and parameter continuity. The seminorm of the tail is bounded by a finite sum of \(p_{\kappa,\beta}(r)\int_{|x|>R}|\phi(x)|\,|x^{\alpha-\kappa}|\,dx\), tending to zero. Completeness of the Schwartz space, proved in Section 4.1 of the cited Weyl-product lesson, supplies the integral in that topology. The ordinary substitution in the scalar integral gives \(F_r\phi(y)=\int r(x-y)\phi(x)\,dx\). Applying \(u\) verifies the identification. Formula (GC22) proves continuity into the strong Schwartz dual for fixed \(r\).

For this Schwartz factor the same Fourier identity holds:
\[
 \widehat{u*r}=\widehat r\,\widehat u.
 \tag{GC23}
\]
Here \(\widehat r\) is Schwartz by the declared Fourier theorem, so its product with a Schwartz test is Schwartz by the entire finite product rule. Fubini in the two absolutely integrable functions \(r(y)\) and \(\psi(\xi)\) proves \(F_r\widehat\psi=\widehat{\widehat r\psi}\); both sides lie in \(\mathcal S\) by (GC22). Pairing with \(u\) proves (GC23), with no inverse factor introduced into a forward transform. If \(r\) is compact smooth, this definition agrees with (GC1). Thus its domains extend the earlier construction exactly.

Here are the exact receiving maps in [Local inverses and distance-weighted elliptic estimates](local-elliptic-coefficients.md). Its compact frequency distribution \(T-b_0\) gives the smooth correction \(G-F_0\) by (GC14)–(GC17), with the original inverse factor. Its zero extension of \(g\in L^p(V)\), for \(V\subset B_1\), is a compact distribution supported in \(\overline B_1\): Hölder on that bounded set bounds its test pairing, including when \(\overline V\) has irregular boundary. Thus \(G*g\) is defined by (GC1). Since \(q(D)G=\delta_0\), (GC4) and the delta identity give \(q(D)(G*g)=g\). For \(v\in C_c^\infty(V)\), they give \(G*q(D)v=(q(D)G)*v=v\). Restriction to \(V\) proves both original identities (L12), with their stated domains.

In its homogeneous-equation argument, \(q(D)F_0=\delta_0+\omega\) and compactness of \(\eta w\) give exactly
\[
 F_0*q(D)(\eta w)
       =\eta w+\omega*(\eta w).
 \tag{GC24}
\]
The commutator \([q(D),\eta]w\) has compact support outside the region where \(\eta=1\). The first kernel is smooth at every resulting nonzero difference, so (GC9)–(GC11) prove local smoothness there; the second kernel \(\omega\) is smooth everywhere. Rearranging (GC24) proves the original assertion that \(w\) is smooth, without imposing a homogeneity formula on the fundamental solution. For every original Schwartz input \(v\), (GC23) and \(q b_0=1+\widehat\omega\) prove the full formula \((D^\alpha F_0)*q(D)v=D^\alpha v+(D^\alpha\omega)*v\), hence (L14). Its later extension still uses the separately stated \(L^p\) multiplier and approximation bounds. These distribution proofs supply the declared distribution-calculus interface; they do not replace those other analytic estimates.

## 14. Four calculations that separate the assertions

**A density correction in one dimension.** Work on \(x>0\) with \(z=\log x\) and \(A=D_x\). On functions, (G7) gives \(A_\kappa=e^{-z}D_z\). Its leading symbol is \(e^{-z}\eta\), so its subprincipal symbol is \(-\frac i2e^{-z}\). Here \(J=x^{-1}\), and (G12) gives the same value: \(-\frac12D_x\log J=-\frac i{2x}\). On half-densities, (G13) adds \(+\frac i{2x}\), giving
\(A^{(1/2)}_\kappa=e^{-z}D_z+\frac i2e^{-z}\).
Its subprincipal symbol is zero, agreeing with \(D_x\). These calculations can be localized by compact cutoffs equal to one on the interval under discussion.

**One smoothing kernel, two support failures.** On \(\mathbb R\), the smooth kernel \(K(x,y)=1\) sends a compact distribution \(u\) to the constant \(u(1)\). It is smoothing and belongs locally to every \(\Psi^m\), but neither kernel projection is proper. It does not send general distributions to distributions by this integral formula: the proposed value on the constant input one would require integrating over the whole line. Multiplying the kernel by a compact smooth function of \(x-y\) makes it proper and still smooth; its integral then acts on every distribution. This distinguishes smoothness from support control without confusing either with symbol order.

**The same threshold, different endpoint membership.** For the point mass \(\delta_0\) in \(\mathbb R^n\), \(\widehat{\delta_0}=1\) and \(\|\Pi_j\delta_0\|_2\asymp2^{jn/2}\) for \(j\geq1\). Consequently \(\delta_0\in H^s\) exactly when \(s<-n/2\), while \(\delta_0\in B^{-n/2}_{2,\infty}\) and \(\delta_0\notin B^{-n/2}_{2,p}\) for finite \(p\). Each nonzero direction at the origin has Sobolev threshold \(-n/2\), because restricting the constant Fourier transform to any cone of positive angle gives the same divergence. The thresholds in (G36) coincide, and the endpoint still has to be checked separately. This is a standard diagnostic example, not a novelty claim.

**A characteristic operator can improve the threshold.** Let \(u=\delta_0(x_1)\otimes f(x')\) in a coordinate product, with smooth nonzero \(f\). Multiplication by \(x_1\) is an order-zero proper operator and sends \(u\) to zero. It is characteristic over \(x_1=0\), so the strict improvement from finite input regularity to smooth output is consistent with (G37). In contrast an elliptic order-zero matrix acting between equal-rank bundles preserves the threshold at every point of its elliptic set, regardless of the local frame.

## 15. Exercises with complete solutions

**1. A complex density cocycle.** Let three charts have positive transition Jacobians \(J_{12},J_{23}\). For \(z=\frac12+i\tau\), verify the density transition law on a triple overlap. Determine the modulus of a local transition factor and explain why a complex logarithm branch is unnecessary.

**Solution.** The chain rule gives \(J_{13}=J_{23}J_{12}\), with the factors evaluated at the appropriate common point. All numbers are positive, so \(\log J_{13}=\log J_{23}+\log J_{12}\) in the real logarithm. Exponentiating after multiplication by \(-z\) gives \(J_{13}^{-z}=J_{23}^{-z}J_{12}^{-z}\), exactly the component cocycle. Its modulus is \(J_{13}^{-1/2}\), because \(|e^{-i\tau\log J_{13}}|=1\). The positivity supplied by the absolute Jacobian makes the real logarithm single valued even on orientation-reversing overlaps.

**2. Proper representatives need not preserve an exact operator.** For the kernel \(K(x,y)=1\) on \(\mathbb R\), choose \(h\in C_c^\infty(\mathbb R)\), equal to one near zero, and replace \(K\) by \(h(x-y)K\). Prove properness and identify the exact type of error. Does this authorize replacing the original operator on a fixed compact input without recording an error?

**Solution.** If \(\operatorname{supp}h\subset[-R,R]\), the new kernel support satisfies \(|x-y|\leq R\). Above a compact set in either variable, the other variable lies in its closed \(R\)-neighborhood, which is compact. Thus both projections are proper. The difference kernel \(1-h(x-y)\) is smooth, so the error is smoothing, but is generally nonzero. For a smooth input of nonzero integral supported far from a chosen output point, the proper replacement vanishes there while the original output is its nonzero integral. Hence the replacement is an identity modulo smoothing, not an exact operator identity.

**3. Recover the endpoint obstruction with a logarithmic sequence.** Let \(v_j\) be \(L^2\) Fourier functions on disjoint dyadic annuli with \(\|v_j\|_2=2^{-js_0}(1+j)^{-\beta}\), and let \(u\) be the tempered distribution with Fourier transform \(\sum_{j\geq1}v_j\). Determine its global \(B^{s_0}_{2,p}\) membership and its supremum of global Sobolev orders.

**Solution.** Polynomial growth of the annular \(L^2\) norms makes the sum a tempered distribution: pairing each annulus with a Schwartz function and applying Cauchy–Schwarz yields a summable geometric majorant. With the sharp annular projections in (G30), its order-\(s_0\) Besov sequence is \((2\pi)^{-n/2}(1+j)^{-\beta}\), by Plancherel in the stated Fourier convention. For finite \(p\), membership holds exactly when \(\beta p>1\); for \(p=\infty\), exactly when \(\beta\geq0\). The squared \(H^s\) norm is comparable to the sum of \(2^{2j(s-s_0)}(1+j)^{-2\beta}\), by disjoint Fourier supports and comparability of \(\langle\xi\rangle\) with \(2^j\) on each annulus. This series is summable for every \(s<s_0\), and not summable for any \(s>s_0\), since its terms then fail to tend to zero. Thus the supremum is \(s_0\) for every real \(\beta\), while endpoint Hilbert membership holds precisely when \(\beta>1/2\). This is a global calculation and makes no unsupported claim about the spatial location of its wavefront.

**4. Why a compact output does not imply a compact input.** Give a proper elliptic operator on a noncompact manifold and a noncompactly supported smooth input whose output is compactly supported. Locate the hypothesis that prevents this from contradicting the compact-space converse in (G32).

**Solution.** On \(\mathbb R\), take \(A=D_x\), a proper elliptic differential operator of order one, and \(u=1\). Its output is zero, whose support is empty and hence compact, while \(u\) has support all of \(\mathbb R\). The converse in (G32) asserts input regularity from output regularity; its compact-space version assumes at the outset that the input distribution has compact support. A parametrix leaves a smooth remainder, which can carry a noncompact smooth solution such as this one.

**5. An unequal-rank symbol.** Let \(E\) and \(F\) have local ranks two and three, and let a principal symbol be \(a(x,\xi)=\langle\xi\rangle^m\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}\). Compute the symbol of the half-density adjoint and explain which statements of Section 13 apply without modification, and which two-sided assertion cannot hold.

**Solution.** In dual frames the adjoint symbol is \(\langle\xi\rangle^m\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}\), since the order \(m\) is real and the displayed matrix has real entries. The local class, its patching law, Sobolev/Besov mapping, proper-support extension, compatible composition, and the adjoint theorem all allow these ranks. Multiplying the adjoint symbol by the original gives \(\langle\xi\rangle^{2m}I_2\), whereas the reverse product is \(\langle\xi\rangle^{2m}\operatorname{diag}(1,1,0)\). Thus there cannot be a two-sided inverse from a three-dimensional fiber to a two-dimensional fiber. The failure is finite-dimensional algebra, not a regularity defect.

**6. The boundary of coordinate invariance.** For a symbol \(a(\xi)\in S^0_{\rho,0}\), consider \(b(x,\xi)=a(M(x)\xi)\) with smooth invertible nonconstant \(M\). Derive the order cost of one base derivative. Then classify \((\rho,\delta)=(2/5,1/5),(3/4,1/4),(1/2,1/2)\) with respect to the coordinate theorem and the inverse construction in this lesson.

**Solution.** The chain rule gives \(\partial_{x_j}b=\sum_k(\partial_{\xi_k}a)(M(x)\xi)(\partial_{x_j}M(x)\xi)_k\). On a compact base set, the first factor costs \(-\rho\) and the second costs one, so the bound is of order \(1-\rho\). This estimate is the reason for the requirement \(\delta\geq1-\rho\); the calculation is not by itself an assertion that every particular symbol fails below that bound. For \((2/5,1/5)\), this condition fails because \(1/5<3/5\), so the general coordinate theorem does not apply, even though the Euclidean symbol class is defined. For \((3/4,1/4)\), both \(1-\rho\leq\delta\leq\rho\) and \(\delta<\rho\) hold, giving coordinate invariance and an inverse gain \(\rho-\delta=1/2\). For \((1/2,1/2)\), coordinate invariance holds through the amplitude estimate, but the inverse gain is zero. No decreasing-order parametrix construction follows there.

## 16. Original chart, bundle and inverse maps

These are complete standard foundation proofs for the course's original smooth manifolds and finite-coordinate maps. No novelty is claimed. The original spaces, norms, coordinates, matrices and all transition factors remain. The independent inputs are the full finite linear algebra in Polynomial and contour tools Section 10, the original scalar and higher finite-coordinate calculus in Metric and topological foundations Section 13, the norm completeness proved there and in Banach estimates, and the full original chart construction MG1--MG9 in the divergence chapter. A manifold means its given Hausdorff, second-countable smooth atlas; a bundle means the finite-rank locally trivial complex vector space structure specified below. These definitions do not assume a missing inverse, gluing or partition theorem.

### 16.1. The actual smooth partition and every denominator derivative

The construction MG1--MG5 works in the original smooth atlas. Its coordinate bumps, including the full exponential and positive denominator in MG3 and the actual three radii and quadratic denominator in MG4, are smooth. Composition with the given smooth charts and extension by zero preserve every derivative order because each support is compact inside its chart. The original shell construction proves local finiteness independently of any bundle or inverse-function theorem. Consequently its actual functions are

\[
 S(x)=\sum_{i\in I}\beta_i(x),\qquad S(x)\geq1,\qquad
 \phi_i(x)=\frac{\beta_i(x)}{S(x)},\qquad
 \sum_{i\in I}\phi_i(x)=1 .
 \tag{BG1}
\]

Every sum is finite on a neighborhood of each point. The compact supports stay in their assigned original cover members. There is no global compactness or finite-atlas assumption.

Here is the full higher derivative formula, including every denominator contribution. For labeled coordinate directions \(h_1,\ldots,h_N\), let \(\mathfrak P(J)\) be the set of all partitions of the finite label set \(J\) into nonempty blocks. The empty set has its one empty partition. In a block \(B\), retain the directions with those actual labels, writing \(D_B S=D^{|B|}S[h_b:b\in B]\). Then

\[
 \begin{aligned}
 D^N\phi_i[h_1,\ldots,h_N]
 =\sum_{J\subset\{1,\ldots,N\}}
 &D^{|J|}\beta_i[h_j:j\in J]\\
 {}\times\sum_{\Pi\in\mathfrak P(J^c)}
 &(-1)^{|\Pi|}|\Pi|!\,S^{-|\Pi|-1}
       \prod_{B\in\Pi}D_BS .
 \end{aligned}
 \tag{BG2}
\]

For \(N=0\), this is exactly the original quotient in BG1. To prove the formula, differentiate the reciprocal once: \(D(S^{-1})[h]=-S^{-2}DS[h]\). At any following differentiation a new label either joins exactly one existing block by differentiating that derivative of \(S\), or forms a singleton by differentiating the reciprocal coefficient. The latter coefficient changes from \((-1)^k k!S^{-k-1}\) to \((-1)^{k+1}(k+1)!S^{-k-2}\). Every partition of the enlarged label set has exactly one predecessor of one of these two kinds, determined by the block containing the new label. This proves the reciprocal partition formula by induction. The complete product rule chooses the labels \(J\) assigned to \(\beta_i\), giving BG2. Repeated equal coordinate directions retain all their multiplicities because the labels remain distinct. On any compact subchart, finitely many original supports occur and all derivatives on the right have finite bounds; \(S\geq1\) keeps every original denominator away from zero.

The original compact cutoff MG5--MG7 is smooth by the same reasoning: its sum has finitely many selected original compact supports and equals one on a neighborhood of the compact set by the locally finite closed-support argument. The original locally positive radius minorant, original metric and absolute density MG7--MG9 are smooth at every order when the given atlas is smooth. Their original sums, metric matrices, square roots and absolute Jacobians remain those of MG7--MG9. On an empty manifold these assertions are vacuous with the empty functions; in dimension zero the given Hausdorff second-countable manifold is discrete and its countable singleton charts give the same construction with empty derivative lists.

### 16.2. Gluing the actual finite-rank bundle

Let \(\{U_i\}_{i\in I}\) be an open cover of the original smooth manifold \(X\). The original rank \(r\geq0\) is fixed on the component under discussion; a locally constant rank is treated component by component. Suppose given smooth matrices on every overlap, with exactly the convention

\[
 G_{ji}:U_i\cap U_j\longrightarrow {\rm GL}(r,\mathbb C),
 \qquad
 G_{ii}=I_r,\qquad
 G_{kj}(x)G_{ji}(x)=G_{ki}(x).
 \tag{BG3}
\]

These are the data to be glued, not an assumed gluing theorem. In particular \(G_{ij}G_{ji}=I_r=G_{ji}G_{ij}\); the actual inverses are given by the reversed transition matrices. Form the disjoint union of the original \(U_i\times\mathbb C^r\), and impose

\[
 (i,x,v_i)\sim(j,x,v_j)
 \quad\Longleftrightarrow\quad
 v_j=G_{ji}(x)v_i .
 \tag{BG4}
\]

BG3 proves reflexivity, symmetry and transitivity, with the displayed multiplication order. Let \(E\) be this quotient with its quotient topology, \(q\) the quotient map, and \(\pi[(i,x,v_i)]=x\). The last map is well defined and continuous: on each disjoint-union component its composition with \(q\) is the continuous projection, and the defining quotient criterion proves continuity.

For each original \(U_i\), define

\[
 \begin{aligned}
 \Phi_i:\pi^{-1}(U_i)&\longrightarrow U_i\times\mathbb C^r,\\
 \Phi_i[(j,x,v_j)]&=(x,G_{ij}(x)v_j),\\
 \Phi_i^{-1}(x,v_i)&=q(i,x,v_i).
 \end{aligned}
 \tag{BG5}
\]

The cocycle proves independence of the representative, and the two displayed maps are inverse. The set \(\pi^{-1}(U_i)\) is open. The restriction of a quotient to an open saturated preimage is a quotient map: the inverse image of an open subset of that restriction is open in the open preimage and therefore open in the whole disjoint union. On each component of this preimage, \(\Phi_iq\) is \((x,v_j)\mapsto(x,G_{ij}(x)v_j)\), continuous. Hence \(\Phi_i\) is continuous by this restricted quotient criterion. Its displayed inverse is the continuous inclusion followed by \(q\). Thus BG5 is a homeomorphism onto the entire original product, without a missing bijection-to-homeomorphism step.

If two points in \(E\) have different base points, disjoint original base neighborhoods separate them by \(\pi\). If their base points agree, one chart BG5 contains both; its Hausdorff product separates them by open subsets of that open chart. Thus \(E\) is Hausdorff. The original countable-base argument in MG1 selects a countable subcover of the \(U_i\). Each \(\pi^{-1}(U_i)\) in that subcover is second countable by BG5, since its base is an open subset of a second-countable manifold and its fiber is finite-dimensional. The union of those countably many open-chart bases is a countable base for \(E\).

Use the original base coordinates in BG5 and the original real and imaginary fiber coordinates. On an overlap its full change of coordinates is

\[
 (x_i,v_i)\longmapsto
       \bigl(\kappa_{ji}(x_i),G_{ji}(x)v_i\bigr).
 \tag{BG6}
\]

It and its inverse are smooth by the full coordinate product and chain rules; the inverse retains \(\kappa_{ij}\) and \(G_{ij}\). This supplies a smooth atlas on the quotient. Fiber addition and complex scalar multiplication are the original operations in each \(\mathbb C^r\). BG3 makes them independent of the chart, and BG6 proves their smoothness. We have constructed the complete smooth finite-rank vector bundle.

A section is equivalent to its actual smooth component functions \(v_i\) with \(v_j=G_{ji}v_i\). In one direction this follows from BG5--BG6. Conversely these functions define the same quotient point on every overlap by BG4; their local smoothness in the open charts gives a global smooth section. The same argument glues any family of compatible local sections over arbitrary open sets, uniquely. Compatible local fiber-linear maps glue too: with input transitions \(G^E\), output transitions \(G^F\) and local matrix \(A_i\), the exact condition is \(A_jG^E_{ji}=G^F_{ji}A_i\). It gives one well-defined smooth quotient map, and its local matrices recover the original family. If all local matrices are invertible, their actual inverses satisfy the reverse transition law and glue to the inverse map. Any other bundle with the same trivializations and transition data receives this map and its inverse, so the construction is unique up to the uniquely specified bundle isomorphism. This proves existence, gluing and the full inverse statement rather than assuming a bundle object from its cocycle.

For rank zero, every fiber is the singleton \(\mathbb C^0\), every matrix is \(I_0\), its determinant is one and every empty product has value one. BG4--BG6 give \(E=X\), with its zero-dimensional fibers and the unique zero sections. Empty base sets give the empty bundle.

### 16.3. Every tensor, dual, metric and density factor

The same construction applies to the actual derived transitions. For two bundles, the tensor transition has all of its original entries:

\[
 (v^E\otimes v^F)^{ab}_j
   =\sum_{c=1}^{r_E}\sum_{d=1}^{r_F}
       (G^E_{ji})_{ac}(G^F_{ji})_{bd}
       (v^E\otimes v^F)^{cd}_i .
 \tag{BG7}
\]

The tensor of the two cocycle identities, with both finite sums expanded, proves its cocycle in the same order. Direct sums use the full block-diagonal matrices. For a fiber-linear map from \(E\) to \(F\) and for the linear and conjugate-linear duals, respectively, the transitions are

\[
 A_j=G^F_{ji}A_iG^E_{ij},\qquad
 \ell_j=(G^E_{ij})^T\ell_i,\qquad
 m_j=\overline{G^E_{ij}}^{\,T}m_i .
 \tag{BG8}
\]

Indeed \(v_j=G^E_{ji}v_i\), so the first equation is exactly equality of the original map in both frames. A linear functional has value \(\ell_i^Tv_i\); a conjugate-linear functional has value \(m_i^T\overline{v_i}\). Substitution gives the last two equations including the full conjugation and transpose. Each pairwise composition keeps every matrix factor and proves the corresponding cocycle. These are exact maps to the actual Hom, dual and anti-dual fibers, not merely formally similar transition lists.

Take the smooth nonnegative partition BG1 subordinate to trivializations, retaining its actual partition index set I_phi and its assignment a(i) to the original trivialization U_a(i). This assignment may repeat a trivialization; no grouping changes the original compact supports. In each original frame choose its actual positive Hermitian matrix \(H_i(x)\), for example the identity in that particular original frame. In frame \(j\), the resulting global metric has the entire matrix

\[
 H_j(x)=\sum_{i\in I_\phi}\phi_i(x)\,
                  G_{a(i),j}(x)^*H_{a(i)}(x)G_{a(i),j}(x).
 \tag{BG9}
\]

Terms are defined on their original trivialization overlap and extended by zero where their compact base support permits it. Each such extension is smooth, and the sum is locally finite. Every term is nonnegative on the actual vector \(v_j\). At each point one \(\phi_i\) is positive; if \(v_j\ne0\), the inverse matrix \(G_{a(i),j}\) makes that term strictly positive. Thus the metric is positive. Its change of frame is \(H_k=G_{jk}^*H_jG_{jk}\): insert BG3 into every term in BG9, retaining both ordered outer factors. On a compact subchart the continuous value \(v^*H_j(x)v\) on the original unit sphere has a positive minimum and a finite maximum, so the original fiber norm has exact positive local comparison bounds. Rank-zero assertions are vacuous; no positive eigenvalue is asserted for an empty matrix.

For original smooth coordinates \(x_i\) and \(x_j=\kappa_{ji}(x_i)\), tangent components change by \(D\kappa_{ji}\); cotangent components change by \((D\kappa_{ij})^T\), from evaluation on the original tangent vector. The chain rule proves both inverse products. The actual scalar density and half-density coefficients have transitions

\[
 \rho_j(x_j)=\rho_i(x_i)|\det D\kappa_{ij}(x_j)|,\qquad
 h_j(x_j)=h_i(x_i)|\det D\kappa_{ij}(x_j)|^{1/2}.
 \tag{BG10}
\]

The full determinant chain rule proves both cocycles, including orientation reversal. The determinants never vanish because both actual inverse coordinate maps are given; their sign is locally constant, so the absolute determinant is smooth. Its positive square root is smooth by the already proved scalar calculus. Tensoring BG10 with BG3 gives the full section and kernel factors of the original bundle-valued density and half-density spaces. In particular a Hom-valued half-density kernel from \(X\) to \(Y\) keeps \(G_F(y)\) on the left, \(G_E(x)^{-1}\) on the right, and one positive half-density Jacobian in each original variable. Pairing the input half-density with a test half-density gives the complete input density. Their multiplication is exactly the product of the two original square roots, so no input Jacobian is dropped. This is the bundle gluing and pairing map required by the existing scalar kernel construction; it does not assume a new scalar kernel theorem.

### 16.4. Constructing the inverse without changing the map or norms

Let \(E,F\) be the original real finite-dimensional normed coordinate spaces of the same dimension \(n\geq1\), with their original norms \(\|\cdot\|_E,\|\cdot\|_F\). Let \(f:O\subset E\to F\) be \(C^r\), \(1\leq r\leq\infty\), on the original open set, and let \(a\in O\) have the actual invertible derivative \(A=Df(a):E\to F\). We keep \(f,A,a,f(a)\) and both norms, and never replace \(A\) by an identity or \(f\) by a changed coordinate expression.

Choose \(0<\theta<1\). Continuity of the actual derivative gives \(R>0\) such that the original closed ball \(\overline B_E(a,R)\) is inside \(O\) and

\[
 \sup_{x\in\overline B_E(a,R)}
       \|I_E-A^{-1}Df(x)\|_{E\to E}\leq\theta .
 \tag{IV1}
\]

The closed ball is complete in the original norm by the existing finite-coordinate completeness proof. For \(y\in F\), use the actual correction map

\[
 T_y(x)=x+A^{-1}(y-f(x)),\qquad
 \varepsilon=\frac{(1-\theta)R}{\|A^{-1}\|_{F\to E}},\qquad
 V=B_F(f(a),\varepsilon).
 \tag{IV2}
\]

The denominator is positive for \(n\geq1\). The full segment fundamental theorem gives
\(\|T_y(x)-T_y(z)\|_E\leq\theta\|x-z\|_E\) for \(x,z\) in the original closed ball. Also
\(\|T_y(x)-a\|_E\leq\theta R+\|A^{-1}\|_{F\to E}\|y-f(a)\|_F<R\) for \(y\in V\). Thus the whole original closed ball maps into itself.

Start \(x_0=a\), \(x_{m+1}=T_y(x_m)\). All iterates remain in that ball. The entire contraction estimate is

\[
 \begin{aligned}
 \|x_{m+1}-x_m\|_E
   &\leq\theta^m\|A^{-1}(y-f(a))\|_E,\\
 \|x_{m+k}-x_m\|_E
   &\leq\|A^{-1}(y-f(a))\|_E
                         \sum_{\nu=m}^{m+k-1}\theta^\nu .
 \end{aligned}
 \tag{IV3}
\]

The finite sum and its convergent geometric tail prove that the sequence is Cauchy. Completeness gives its limit \(h(y)\) in the original closed ball. Continuity gives \(T_y(h(y))=h(y)\), hence \(f(h(y))=y\). Letting \(k\) tend to infinity in IV3 retains the exact tail bound
\(\|h(y)-x_m\|_E\leq\theta^m(1-\theta)^{-1}\|A^{-1}(y-f(a))\|_E\).
At a fixed point,
\(\|h(y)-a\|_E\leq(1-\theta)^{-1}\|A^{-1}(y-f(a))\|_E<R\).
If two fixed points existed, their distance would be at most \(\theta\) times itself; since \(1-\theta>0\), they agree. These arguments prove every existence and uniqueness step of the contraction construction.

For any \(x,z\) in the original closed ball, the same full segment formula gives

\[
 \begin{aligned}
 A^{-1}(f(x)-f(z))
 &=x-z+\int_0^1
      A^{-1}\bigl(Df(z+t(x-z))-A\bigr)(x-z)\,dt,\\
 \|f(x)-f(z)\|_F
 &\geq\frac{1-\theta}{\|A^{-1}\|_{F\to E}}\|x-z\|_E .
 \end{aligned}
 \tag{IV4}
\]

Every ordered matrix factor and the entire integral remain. The reverse triangle inequality proves the second line. Put \(U=B_E(a,R)\cap f^{-1}(V)\), an original open neighborhood of \(a\). The map \(f:U\to V\) is injective by IV4 and surjective by the constructed interior fixed points. Thus \(h\) is its actual inverse, and IV4 gives its precise Lipschitz bound \(\|A^{-1}\|_{F\to E}/(1-\theta)\). In particular both maps are continuous.

For \(x\) in the ball set \(B_x=I_E-A^{-1}Df(x)\). Retain both finite product identities
\((I_E-B_x)\sum_{m=0}^N B_x^m=I_E-B_x^{N+1}
=\bigl(\sum_{m=0}^N B_x^m\bigr)(I_E-B_x)\).
The full operator-norm tail is at most \(\theta^{N+1}/(1-\theta)\). Operator completeness therefore gives both actual inverse products and

\[
 Df(x)^{-1}=\left(\sum_{m=0}^{\infty}B_x^m\right)A^{-1},
 \qquad
 \|Df(x)^{-1}\|_{F\to E}
       \leq\frac{\|A^{-1}\|_{F\to E}}{1-\theta}.
 \tag{IV5}
\]

The rightmost original inverse factor has not been absorbed into a changed derivative. The uniformly convergent series also proves continuous dependence on \(x\), since every finite matrix power is continuous.

For \(y,y+k\in V\), write \(x=h(y)\), \(v=h(y+k)-h(y)\). The original differentiability remainder gives

\[
 \begin{aligned}
 k&=Df(x)v+r_x(v),\qquad
          \frac{\|r_x(v)\|_F}{\|v\|_E}\longrightarrow0,\\
 v&=Df(x)^{-1}k-Df(x)^{-1}r_x(v).
 \end{aligned}
 \tag{IV6}
\]

The remainder is zero at \(v=0\). IV4 bounds \(\|v\|_E\) by
\(\|A^{-1}\|_{F\to E}(1-\theta)^{-1}\|k\|_F\);
IV5 then makes the last remainder \(o(\|k\|_F)\).
Consequently \(Dh(y)=Df(h(y))^{-1}\), and its continuity follows from IV5 and continuity of \(h\). This proves \(C^1\) regularity of the actual inverse before any higher smoothness is used.

### 16.5. Every higher inverse derivative and the implicit map

Matrix inversion is smooth on the original invertible matrices: the full cofactor inverse proved in Polynomial and contour tools Section10 is a matrix of polynomial entries divided by its actual nonzero determinant. The proved finite product, reciprocal and chain rules therefore apply at every available order. Differentiating both original inverse products gives \(D(M^{-1})[v]=-M^{-1}DM[v]M^{-1}\). For every integer \(N\geq1\), iteration retains every ordered factor:

\[
 D^N(M^{-1})[v_1,\ldots,v_N]
 =\sum_{k=1}^N(-1)^k
   \sum_{\substack{(I_1,\ldots,I_k)\ {\rm ordered}\\
                   I_j\ne\varnothing,\ 
                   I_1\sqcup\cdots\sqcup I_k=\{1,\ldots,N\}}}
 M^{-1}D_{I_1}M\,M^{-1}\cdots
             D_{I_k}M\,M^{-1}.
 \tag{IV7}
\]

Each differentiation either adds its label to one existing derivative block or inserts a singleton block at one of the inverse factors. The sign changes precisely in the latter case. Every ordered partition of the new label set has one such predecessor, proving IV7 by induction with no commutation of matrix factors. Repeated equal directions keep all labeled multiplicities.

Starting from the proved \(C^1\) inverse, the identity \(Dh=(Df\circ h)^{-1}\) and this smooth inversion map prove \(h\in C^r\) by induction. Precisely, if \(h\in C^s\) with \(s<r\), then \(Df\) is \(C^{r-1}\), so the right side is \(C^s\); hence \(Dh\) is \(C^s\) and \(h\) is \(C^{s+1}\). This covers every finite order and all orders when \(r=\infty\).

For \(2\leq N\leq r\), set \(D_Bh(y)=D^{|B|}h(y)[v_b:b\in B]\) with every original direction label retained, and differentiate the exact composition \(f(h(y))=y\) by the full higher chain rule. The partition with one block is \(Df(h(y))D^Nh\); all other partitions keep their original derivatives. Thus the complete inverse derivative is

\[
 D^Nh(y)[v_1,\ldots,v_N]
 =-Df(h(y))^{-1}
   \sum_{\substack{\Pi\in\mathfrak P(\{1,\ldots,N\})\\|\Pi|\geq2}}
 D^{|\Pi|}f(h(y))
       [D_Bh(y):B\in\Pi].
 \tag{IV8}
\]

The full higher chain rule itself follows by the same labeled-partition induction: differentiating a block derivative adds the new label to that block, while differentiating the outer derivative creates its singleton block. This accounts for every partition once. The derivatives of the outer map are symmetric multilinear maps, so the bracket order across blocks can be read in increasing least-label order without changing a matrix product. All lower inverse derivatives, repeated-direction multiplicities and the original left inverse matrix remain in IV8.

For the actual implicit problem \(f(s,x)=y\), where \(s\) lies in its original finite-coordinate parameter space and \(D_xf(s_0,x_0)=A\) is invertible, apply the just proved inverse construction to the unchanged augmented map \(L(s,x)=(s,f(s,x))\). At the original point its two block matrices are

\[
 DL=\begin{pmatrix}I&0\\ B&A\end{pmatrix},
 \qquad
 (DL)^{-1}=\begin{pmatrix}I&0\\-A^{-1}B&A^{-1}\end{pmatrix},
 \qquad B=D_sf(s_0,x_0).
 \tag{IV9}
\]

Multiplying in both orders proves the inverse, including the lower-left term. Use the original product norm and an open product contained in the constructed image neighborhood. The first component of \(L^{-1}(s,y)\) must be exactly \(s\), because \(L\)'s first component is \(s\). Its second component \(H(s,y)\) is therefore the unique local solution of the actual original implicit equation. It has the proved \(C^r\) regularity and

\[
 D_yH=(D_xf)^{-1},\qquad
 D_sH=-(D_xf)^{-1}D_sf,
 \tag{IV10}
\]

with every derivative of \(f\) evaluated at the original \((s,H(s,y))\). All higher derivatives are IV8 applied to the entire augmented map and then its second projection; this retains its full parameter blocks and ordered inverse factors. No implicit-function theorem was assumed in constructing this map.

If the solved coordinate dimension is zero, its original domain and range are the singleton spaces and the local inverse is the identity there; the implicit augmented map is exactly the identity on its parameter component. Its empty matrix determinant is one, and no division by the zero operator norm is made. Empty open domains have no base point and make no local assertion.

### 16.6. Exact receiving scope and remaining work

The original smooth atlas and finite-rank bundle clauses receive BG1--BG10 with their actual transition matrices, component maps, duals and density factors. The smooth inverse-function entry receives IV1--IV10 in the original finite-coordinate norms. The existing scalar distribution and kernel constructions then have the precise bundle gluing and half-density pairing map they require; their scalar proofs remain separate independent providers. Smooth coordinate charts already given by an atlas need no new inverse assumption, since both original coordinate maps are part of that atlas.

These proofs do not by themselves establish the nonlinear local flow construction, complete exponential-chart/minimizing-radius calculations, wavefront-qualified arbitrary-map pullback or submersion converse, or complex contour and Laplace/Euler interfaces. Those require their actual remaining calculations.

## 17. Original finite-coordinate flows and their geodesic receiving map

These are standard foundation proofs. Their inputs are the original finite norm completeness, compactness, scalar integration and full finite-coordinate calculus already proved in the course, and the actual inverse and implicit maps BG1--BG10/IV1--IV10 in geometry Section16. Every original state space, norm, time endpoint, parameter, vector field, matrix order and derivative contribution remains.

### 17.1. The original integral equation and its complete local solution

Let \(E,P\) be the original real finite-dimensional normed spaces, with their given norms. Let \(W\subset\mathbb R\times E\times P\) be open and let \(F:W\to E\) be \(C^r\), \(1\leq r\leq\infty\). Fix the original point \((t_0,a,p_0)\in W\). The equation and datum are

\[
 \partial_tu(t)=F(t,u(t),p),\qquad u(t_0)=x.
 \tag{NF1}
\]

Choose positive \(d,\rho,\delta\) such that the compact rectangle
\(K=[t_0-d,t_0+d]\times\overline B_E(a,\rho)\times\overline B_P(p_0,\delta)\)
lies in \(W\). An open neighborhood contains a sufficiently small product of balls; their closures are compact in the original norms and can still be chosen inside that neighborhood. Let the actual bounds be

\[
 M=\sup_K\|F\|_E,\qquad
 L=\sup_K\|D_xF\|_{E\to E},\qquad
 Q=\sup_K\|D_pF\|_{P\to E}.
 \tag{NF2}
\]

They are finite by continuity and compactness. Choose \(0<\theta<1\) and \(0<h<d\) with \(hM\leq\rho/4\) and \(hL\leq\theta\). Such an \(h\) exists also when either bound is zero; no division by a zero bound is used. Keep the original interval \(I=[t_0-h,t_0+h]\), the state ball, and \(x\in B_E(a,\rho/4)\), \(p\in B_P(p_0,\delta)\). On continuous paths in the original closed state ball set

\[
 (\Phi_{x,p}w)(t)=x+\int_{t_0}^{t}F(s,w(s),p)\,ds .
 \tag{NF3}
\]

All integrals retain their original oriented endpoints. A finite-coordinate continuous integral exists coordinatewise by the proved Riemann integral. Its norm is at most the integral of the norm: the finite tagged sums have this bound by the triangle inequality; their vector limits and the scalar integral limit preserve it. The continuous-path space is complete in \(\|w\|_\infty=\sup_{t\in I}\|w(t)\|_E\). Indeed a uniform Cauchy sequence converges pointwise by the original completeness of \(E\), its Cauchy estimates pass uniformly to the limit, and the triangle inequality with one continuous approximant proves continuity. The paths with values in the closed ball form a closed subset of that complete space.

NF2--NF3 show that \(\Phi_{x,p}w\) stays within distance \(\rho/2\) of \(a\). The full state-segment fundamental theorem gives
\(\|F(s,v,p)-F(s,w,p)\|_E\leq L\|v-w\|_E\) inside the original convex ball. Thus
\(\|\Phi_{x,p}v-\Phi_{x,p}w\|_\infty\leq hL\|v-w\|_\infty\leq\theta\|v-w\|_\infty\).
Starting with the actual constant path \(u_0(t)=x\), define \(u_{m+1}=\Phi_{x,p}u_m\). For every \(m\geq0\) and \(k\geq1\), retain

\[
 \begin{aligned}
 \|u_{m+1}-u_m\|_\infty
   &\leq\theta^m\|u_1-u_0\|_\infty,\qquad
       \|u_1-u_0\|_\infty\leq hM,\\
 \|u_{m+k}-u_m\|_\infty
   &\leq\|u_1-u_0\|_\infty
                         \sum_{\nu=m}^{m+k-1}\theta^\nu,\\
 \|u-u_m\|_\infty
   &\leq\frac{\theta^m}{1-\theta}\|u_1-u_0\|_\infty .
 \end{aligned}
 \tag{NF4}
\]

The finite sum proves the Cauchy property, completeness supplies \(u\), and continuity of \(\Phi\) gives NF3 with \(w=u\). The last line follows by taking the limit in the full finite-tail estimate. The fundamental theorem then proves NF1, including at \(t_0\). Two fixed points have distance at most \(\theta\) times that distance and therefore coincide.

For another \(C^1\) solution with the same datum, restrict to an interval on which both solutions lie in a common compact rectangle. On a sufficiently short subinterval beginning at any time at which they agree, the same contraction estimate forces agreement. Their equality set is closed by continuity and open by this two-sided local argument. On their connected common time interval containing the datum it is therefore the whole interval. This proves local uniqueness even for a solution not initially confined to the particular closed ball used to construct \(u\).

The original parameter differences satisfy

\[
 \|u(\,\cdot\,;x',p')-u(\,\cdot\,;x,p)\|_\infty
 \leq\frac{\|x'-x\|_E+hQ\|p'-p\|_P}{1-\theta}.
 \tag{NF5}
\]

To prove it, subtract the two full equations NF3, use the state and parameter segment formulas with their original derivative bounds, and bring the \(hL\) term to the left. Convexity of the original parameter ball keeps every intermediate point in \(K\). Continuity in time and this uniform estimate give joint continuity in \((t,x,p)\). The retained buffer \(\rho/2\) to the boundary of the larger state ball permits the full parameter Taylor comparisons below.

### 17.2. Ordered linear transport on the original two-sided interval

Let \(A:I\to\mathcal L(E,E)\) be continuous and \(B:I\to E\) be continuous. For the same original \(t_0\), define

\[
 (\mathcal V_Az)(t)=\int_{t_0}^t A(s)z(s)\,ds,\qquad
 z=B+\mathcal V_Az.
 \tag{NF6}
\]

For \(L_A=\sup_I\|A(s)\|\), nested integration proves
\(\|\mathcal V_A^m\|\leq(hL_A)^m/m!\). In detail the \(m\)-fold application has the full integral
\(\int_{t_0}^t ds_1\int_{t_0}^{s_1}ds_2\cdots\int_{t_0}^{s_{m-1}}ds_m\)
of \(A(s_1)\cdots A(s_m)z(s_m)\). Taking absolute values reverses the bounds when \(t<t_0\); the resulting scalar nested integral of one is \(|t-t_0|^m/m!\), by induction from the scalar power integral. Every oriented sign remains in the original operator integral. Norm completeness therefore supplies

\[
 \begin{aligned}
 \mathcal R_A&=\sum_{m=0}^{\infty}\mathcal V_A^m,&
 (I-\mathcal V_A)\mathcal R_A
   &=I=\mathcal R_A(I-\mathcal V_A),\\
 z&=\mathcal R_AB,&
 \|\mathcal R_A\|&\leq
        \sum_{m=0}^{\infty}\frac{(hL_A)^m}{m!}
        =\exp(hL_A).
 \end{aligned}
 \tag{NF7}
\]

The inverse products follow from both finite identities
\((I-\mathcal V_A)\sum_{m=0}^N\mathcal V_A^m
=I-\mathcal V_A^{N+1}
=(\sum_{m=0}^N\mathcal V_A^m)(I-\mathcal V_A)\)
and the factorial bound. This proves uniqueness as well as existence. When \(hL_A\leq\theta\), the additional geometric bounds
\(\|\mathcal R_A\|\leq(1-\theta)^{-1}\) and
\(\|\sum_{m>N}\mathcal V_A^m\|\leq\theta^{N+1}/(1-\theta)\)
hold with their complete factors. Neither estimate replaces the original operator or the factorial estimate.

For a matrix coefficient acting on a finite-dimensional original fiber, the fundamental matrix is

\[
 Y(t)=I_E+\sum_{m=1}^{\infty}
   \int_{t_0}^{t}ds_1\int_{t_0}^{s_1}ds_2
       \cdots\int_{t_0}^{s_{m-1}}ds_m\,
        A(s_1)A(s_2)\cdots A(s_m).
 \tag{NF8}
\]

The order is exactly the displayed one. Its factorial bound proves uniform convergence. Its integral equation and the fundamental theorem give \(Y'=AY\), \(Y(t_0)=I_E\). Construct \(Z'=-ZA\), \(Z(t_0)=I_E\), by the same integral argument, now on the original matrix space with right multiplication. Differentiating \(ZY\) gives zero with the two full terms \(-ZAY+ZAY\), so \(ZY=I_E\). Finite-dimensional injectivity and surjectivity imply \(YZ=I_E\) as well. Thus this constructed \(Z\) is the actual inverse at every original time.

For \(z'=Az+b\), \(z(t_0)=c\), both full maps are

\[
 z(t)=Y(t)\left(c+\int_{t_0}^{t}Y(s)^{-1}b(s)\,ds\right),
 \qquad
 Y(t)^{-1}z(t)=c+\int_{t_0}^{t}Y(s)^{-1}b(s)\,ds .
 \tag{NF9}
\]

The product rule and the proved inverse equation verify both identities, including their initial values and multiplication order. Uniqueness follows from NF7. Arbitrary complex matrices are handled on their original real and imaginary coordinates, with the same complex matrix products; no diagonalization, self-adjointness or commutation is used.

### 17.3. All parameter derivatives of the linear inverse

Let \(\eta\) range in an open finite-dimensional original normed parameter space. Suppose \(\eta\mapsto A_\eta\) is \(C^s\) into continuous matrix or operator paths in the original supremum norm. Integration in NF6 is a bounded linear map of \(A\), with norm at most \(h\), so \(\eta\mapsto\mathcal V_\eta\) is \(C^s\) and every derivative retains that integral. Locally bounded \(L_A\) gives locally bounded inverses by NF7. Their exact difference identity is

\[
 \mathcal R_{\eta'}-\mathcal R_\eta
   =\mathcal R_{\eta'}(\mathcal V_{\eta'}-\mathcal V_\eta)
                         \mathcal R_\eta.
 \tag{NF10}
\]

Multiplication on the left by \(I-\mathcal V_{\eta'}\) and on the right by \(I-\mathcal V_\eta\) verifies the identity directly. It proves norm continuity. Insert the full differentiability remainder of \(\mathcal V\) into NF10; continuity and the local inverse bound make its remaining error \(o(\|\eta'-\eta\|)\). Consequently
\(D\mathcal R[v]=\mathcal R(D\mathcal V[v])\mathcal R\).
This proof uses no Banach inverse-function theorem. Bounded operator multiplication has the required product rule: expand the actual two-factor increment, retaining the bilinear increment product whose norm is bounded by the product of its two increment norms. The remainder is therefore of second order. Induction gives its full higher product rule.

For every integer \(N\geq1\) allowed by the parameter differentiability, the entire inverse derivative is

\[
 D^N\mathcal R[v_1,\ldots,v_N]
 =\sum_{k=1}^N
   \sum_{\substack{(I_1,\ldots,I_k)\ {\rm ordered}\\
                   I_j\ne\varnothing,\ 
                   I_1\sqcup\cdots\sqcup I_k=\{1,\ldots,N\}}}
 \mathcal R D_{I_1}\mathcal V\,\mathcal R\cdots
                       D_{I_k}\mathcal V\,\mathcal R .
 \tag{NF11}
\]

Here \(D_I\) retains precisely the labeled directions in \(I\). A new differentiation either joins an existing derivative block or differentiates one inverse factor and inserts its new singleton block there. Every ordered partition of the enlarged label set has exactly one predecessor, determined by the new label's block. This proves NF11 and \(C^s\) regularity by induction, with all repeated-direction multiplicities and every noncommuting factor retained. For \(N=0\) the value is the full inverse \(\mathcal R\).

If \(B_\eta\) is \(C^s\) in the continuous-path norm, NF7 and the full product rule therefore make \(z_\eta=\mathcal R_\eta B_\eta\) \(C^s\) in that same norm. For coefficient paths of the form \(A_\eta(t)=A(t,\eta)\), whose finite-coordinate derivatives are jointly continuous, their path-valued derivatives exist uniformly on compact parameter neighborhoods. The segment Taylor remainder is bounded by the uniform oscillation of the next continuous derivative on the compact time/parameter product, which tends to zero. This proves the asserted path-valued regularity, rather than merely pointwise differentiability.

### 17.4. The first actual nonlinear parameter derivative

Write \(\eta=(x,p)\), retaining its given product-space norm and both coordinate projections. For a direction \(v=(v_x,v_p)\), the candidate derivative \(z_v\) solves

\[
 \begin{aligned}
 A_\eta(t)&=D_xF(t,u_\eta(t),p),\\
 B_{\eta,v}(t)&=v_x+
           \int_{t_0}^tD_pF(s,u_\eta(s),p)v_p\,ds,\\
 z_v&=B_{\eta,v}+\mathcal V_{A_\eta}z_v
       =\mathcal R_{A_\eta}B_{\eta,v}.
 \end{aligned}
 \tag{NF12}
\]

NF7 supplies this entire linear solution and uniqueness. It is linear in the original direction, and continuous as an operator from the original parameter norm to the path norm: keep the original projection norms \(c_x,c_p\), so
\(\|z_v\|_\infty\leq(1-\theta)^{-1}(c_x+hQc_p)\|v\|\).
No original norm is replaced by a coordinate norm in this estimate.

To prove that it is the derivative, let \(\Delta\eta=(\Delta x,\Delta p)\) and \(\Delta u=u_{\eta+\Delta\eta}-u_\eta\). The exact segment expansion of the original field is

\[
 \begin{aligned}
 &F(t,u_\eta+\Delta u,p+\Delta p)-F(t,u_\eta,p)\\
 &\quad=A_\eta(t)\Delta u+
               D_pF(t,u_\eta,p)\Delta p+\epsilon_\eta(t),\\
 &\|\epsilon_\eta\|_\infty
   \leq\omega_\eta\bigl(\|\Delta u\|_\infty+\|\Delta p\|_P\bigr)
             \bigl(\|\Delta u\|_\infty+\|\Delta p\|_P\bigr),
       \qquad \omega_\eta(q)\longrightarrow0\quad(q\downarrow0).
 \end{aligned}
 \tag{NF13}
\]

For the bound, subtract the derivatives at the start of each full state/parameter segment from their values along it and integrate. Uniform continuity on a compact rectangle containing these segments gives the displayed modulus. NF5, with both original projection factors, bounds the argument of the modulus by
\(((c_x+hQc_p)/(1-\theta)+c_p)\|\Delta\eta\|\).
Subtract NF12 for \(v=\Delta\eta\) from the exact difference of NF3. Its residual is
\(\Delta u-z_{\Delta\eta}=\mathcal V_{A_\eta}(\Delta u-z_{\Delta\eta})
+\int_{t_0}^{\,\cdot\,}\epsilon_\eta(s)\,ds\).
NF7 bounds it by \(h(1-\theta)^{-1}\|\epsilon_\eta\|_\infty=o(\|\Delta\eta\|)\). This proves the full path-valued Fréchet derivative. Joint continuity of the field derivatives, NF5 and NF10 give continuity of the derivative operator. Thus \(u_\eta\) is \(C^1\) into continuous paths before any higher dependence is used.

### 17.5. Every nonlinear parameter derivative, including its original blocks

Assume \(u_\eta\) is \(C^s\) in the path norm, with \(s<r\). The path-valued maps \(A_\eta=D_xF(\,\cdot\,,u_\eta,p)\) and \(B_{\eta,v}\) in NF12 are \(C^s\), because \(F\) is \(C^r\) and \(s\leq r-1\). To justify the composition statement in the path norm, apply the full finite-coordinate chain and product rules at each time. The derivatives are finite sums of continuous products of the original derivatives of \(F\) and those of \(u\). All their Taylor remainder bounds are uniform on the compact rectangle, by the same segment and uniform-continuity argument as NF13. The bound remains uniform for \(v\) in the unit ball of its original finite-dimensional direction space. NF10--NF11 then show that \(Du_\eta=\mathcal R_{A_\eta}B_{\eta,\cdot}\) is \(C^s\) as an operator-valued map. Hence \(u_\eta\) is \(C^{s+1}\). Induction proves the full \(C^r\) parameter theorem, and every order for \(r=\infty\).

Here is its exact higher equation. Retain labeled directions \(v_1,\ldots,v_N\) in the original parameter space, and put \(\zeta_\eta(t)=(u_\eta(t),p)\). For a nonempty block \(B\) of labels use

\[
 D_B\zeta_\eta(t)=
 \begin{cases}
 (D u_\eta(t)[v_b],(v_b)_p),&B=\{b\},\\
 (D^{|B|}u_\eta(t)[v_b:b\in B],0),&|B|\geq2.
 \end{cases}
 \tag{NF14}
\]

For \(2\leq N\leq r\), the whole \(N\)-th derivative equation is

\[
 \begin{aligned}
 D^Nu_\eta(t)[v_1,\ldots,v_N]
 &=\int_{t_0}^t A_\eta(s)
                  D^Nu_\eta(s)[v_1,\ldots,v_N]\,ds\\
 &\quad+\int_{t_0}^t
   \sum_{\substack{\Pi\in\mathfrak P(\{1,\ldots,N\})\\|\Pi|\geq2}}
   D_{(x,p)}^{|\Pi|}F(s,u_\eta(s),p)
                 [D_B\zeta_\eta(s):B\in\Pi]\,ds .
 \end{aligned}
 \tag{NF15}
\]

The initial \(N\)-th derivative is zero because the original datum \(x\) is linear in \(\eta\). The one-block term of the full chain rule is \(D_xF\,D^Nu\), since the parameter component of NF14 is zero for that block. Every other partition remains explicitly in NF15. Differentiating a block appends the new direction to that block; differentiating the outer derivative creates its singleton block. Every partition is obtained once, proving the full chain formula with no omitted multiplicity. The outer derivatives are symmetric multilinear maps on the original state/parameter product; the order of their arguments may be fixed by the least label in each block. Their values do not authorize commuting any linear transport factors. NF7 applied to the entire displayed inhomogeneous integral gives the actual unique derivative, including all pure-state, pure-parameter and mixed derivatives.

All derivatives just constructed are jointly continuous in time and parameters. NF1 gives the time derivative. More explicitly, the first time derivative of each parameter derivative of total order at most \(r-1\) is its full chain-rule derivative of \(F(t,u_\eta(t),p)\). Its right side is a finite continuous sum of the just proved parameter derivatives and the original field derivatives. Differentiating these identities in time gives all further mixed time/parameter derivatives of total order at most \(r\), inductively using the complete product and chain rules. At a given total order only field derivatives and solution derivatives of lower total order occur on the right of the time equation. Their continuity proves the next derivatives and permits equality of the mixed derivatives by the proved finite-coordinate calculus. The case of no time derivative and \(r\) parameter derivatives was already constructed in the path norm. Thus \(u(t;x,p)\) is jointly \(C^r\), not only separately differentiable.

### 17.6. Variable initial times without replacing the original time coordinate

Use the proved solution with the fixed original \(t_0\). Write \(U(t;t_0,y,p)\) for it. Near \((t_0,a,p_0)\), the actual finite map

\[
 \mathcal L(\tau,y,p)
   =(\tau,U(\tau;t_0,y,p),p)
 \tag{NF16}
\]

is \(C^r\). At \(\tau=t_0\) its state derivative is the original identity because \(U(t_0;t_0,y,p)=y\), its state derivative in \(p\) is zero, and its time derivative is \(F(t_0,y,p)\). Its full derivative is block triangular with diagonal identities; its inverse keeps the lower state/time block \(-F(t_0,y,p)\). The proved finite inverse/implicit theorem therefore constructs its actual local inverse, with second component \(Y(\tau,x,p)\). The unchanged original-time solution is

\[
 U(t;\tau,x,p)=U(t;t_0,Y(\tau,x,p),p),\qquad
 U(\tau;t_0,Y(\tau,x,p),p)=x .
 \tag{NF17}
\]

It is jointly \(C^r\), solves the original differential equation in the original \(t\), and has the original datum at the original time \(\tau\). Uniqueness was proved in Section17.1. Both maps in NF17 are explicit; no translated time equation or changed vector field is substituted for NF1.

Let \(M(t)=D_yU(t;t_0,y,p)\). Differentiating the already proved equation gives \(M'=D_xF(t,U,p)M\), \(M(t_0)=I_E\). NF8 proves that it is invertible with the constructed opposite-order inverse. Differentiate the second identity of NF17 and then its first identity to obtain the full initial-time derivative

\[
 \begin{aligned}
 D_\tau Y&=
  -D_yU(\tau;t_0,Y,p)^{-1}F(\tau,x,p),\\
 D_\tau U(t;\tau,x,p)&=
  -D_yU(t;t_0,Y,p)
   D_yU(\tau;t_0,Y,p)^{-1}F(\tau,x,p)\\
  &=-D_xU(t;\tau,x,p)F(\tau,x,p).
 \end{aligned}
 \tag{NF18}
\]

The last equality follows by differentiating NF17 in \(x\): \(D_xY=D_yU(\tau;t_0,Y,p)^{-1}\). All original inverse factors and endpoint evaluations appear before the comparison. Higher initial-time derivatives are the full finite composition and inverse partition formulas applied to NF16--NF17; they keep the entire time/state/parameter blocks.

### 17.7. Continuation, the exact composition law and coordinate transport

At every point of a solution, the local construction above applies with that original point and its original time as datum. Its local continuations agree by uniqueness. The union of all continuation intervals is an interval: each contains the original datum time, so two such intervals overlap; their agreeing solutions glue. This gives the unique maximal solution on that interval. If two overlapping continuations are first described through different chains of local rectangles, the same uniqueness argument on the connected time overlap makes them equal. No choice of a chart or of a time subdivision changes the solution.

The full admissible domain of \((t,\tau,x,p)\) is open and the solution is jointly \(C^r\) there. For an actual trajectory segment from \(\tau\) to \(t\), its compact graph is covered by finitely many construction rectangles with smaller time intervals. Subdivide that original time segment finely enough that each successive piece lies in one such rectangle: a Lebesgue number follows from compactness by taking finitely many smaller neighborhoods whose closures remain in the covering neighborhoods, or by the elementary compact interval subdivision argument. Each local solution map is defined on an open neighborhood of its intermediate datum. Continuity of the finite preceding composition lets one shrink the original data neighborhood so that all intermediate data stay in these open neighborhoods. The finite composition then exists near the given endpoint and is \(C^r\), and uniqueness identifies it with the maximal solution. Slightly moving both endpoint times uses the first and last rectangles. This proves openness and full local regularity throughout the actual domain.

Whenever all displayed solutions are defined along their connected common intervals,

\[
 U(t;s,U(s;\tau,x,p),p)=U(t;\tau,x,p),\qquad
 U(\tau;t,U(t;\tau,x,p),p)=x.
 \tag{NF19}
\]

Both sides of the first identity solve NF1 with the same datum at \(s\); uniqueness proves it, and the second is its endpoint case. For an autonomous field write \(\varphi_t(x,p)=U(t;0,x,p)\). NF19 gives the local flow law \(\varphi_t(\varphi_s(x,p),p)=\varphi_{t+s}(x,p)\), with their actual domains, and inverse \(\varphi_{-t}\). This is a local diffeomorphism, since both maps are the constructed smooth inverse maps on open sets. It is not an assertion that every field has a globally defined flow.

Under an original smooth coordinate diffeomorphism \(\kappa\), retain the transformed field
\(\widetilde F(t,\kappa(x),p)=D\kappa(x)F(t,x,p)\).
The chain rule proves that \(\kappa(U(t;\tau,x,p))\) solves its equation with datum \(\kappa(x)\). Applying uniqueness gives

\[
 \widetilde U(t;\tau,\kappa(x),p)
       =\kappa(U(t;\tau,x,p)).
 \tag{NF20}
\]

This is the exact map between coordinate presentations. For a smooth vector field on the given manifold, these transformations glue local chart solutions and all their parameter derivatives. Their domains are open by the finite-chain proof. For a manifold with boundary, the same assertion in boundary charts needs an actual smooth extension of the coefficients to an open coordinate neighborhood; no extension theorem is hidden in NF20. The collar lesson's stated coefficient extension or an explicitly given extension supplies that separate condition.

The determinant of the original state variation has all of its factors:

\[
 \det D_xU(t;\tau,x,p)
   =\exp\left(\int_\tau^t
             \operatorname{tr}D_xF(s,U(s;\tau,x,p),p)\,ds\right).
 \tag{NF21}
\]

Its derivative follows from the full cofactor determinant derivative and the two actual inverse products of NF8: for \(M'=AM\),
\((\det M)'=(\det M)\operatorname{tr}(M^{-1}AM)
=(\det M)\operatorname{tr}A\).
The trace equality is the finite sum
\(\sum_{i,j,k}(M^{-1})_{ij}A_{jk}M_{ki}
=\sum_{j,k}A_{jk}\sum_i M_{ki}(M^{-1})_{ij}
=\sum_jA_{jj}\).
The scalar integrating-factor proof and the initial determinant one give NF21. The original determinant, oriented time integral and original trace are all retained. Positivity of this determinant is the local orientation statement; no state norm or coordinate volume has been silently changed.

If the original state dimension is zero, the unique state is its zero vector, \(F\) is zero and the solution is constant. Every state inverse is the unique \(I_0\), every empty matrix determinant is one, and NF21 is \(1=\exp(0)\). No positive state comparison constant or division by a zero operator norm is needed. A zero-dimensional parameter space has no parameter directions; its derivative terms in the original formulas are zero. If \(W\) is empty there is no datum and no local assertion.

### 17.8. The actual geodesic vector field and smooth endpoint map

Return to the original positive metric \(H=(g_{ij})=G^{-1}\) and its original Christoffel coefficients HG2. On the original state space of coordinate positions and velocities its full vector field is

\[
 \mathcal F(x,v)=
 \left(v,\left(-\sum_{j,k=1}^n
                       \Gamma^i_{jk}(x)v^jv^k\right)_{i=1}^n\right).
 \tag{NG1}
\]

The given original \(G=(g^{ij})\) is real symmetric, smooth and positive definite, \(H=G^{-1}=(g_{ij})\), and the complete connection formula is

\[
 \Gamma^i_{jk}=\frac12\sum_l g^{il}
             (\partial_jg_{kl}+\partial_kg_{jl}-\partial_lg_{jk}).
                                                                    \tag{NG0}
\]

Use the given position and velocity norms with their complete product norm and projection constants. This is a smooth finite-coordinate field by the full inverse-matrix and calculus proofs; no initial metric is made into an identity. NF1--NF20 now construct and uniquely continue the actual geodesic \((x(t;v,y),\dot x(t;v,y))\), smoothly in all initial coordinates and times.

At \((y,0)\) the field vanishes, so the constant position and zero velocity solve the equation for every real time while remaining in the original chart. Openness of the full flow domain, over the compact time interval \([0,1]\) of this constant trajectory, gives one neighborhood of \((y,0)\) on which solutions exist throughout \([0,1]\). In detail use finitely many open product neighborhoods of its points; intersect their initial-data neighborhoods and use uniqueness to identify all overlapping local solutions. The endpoint
\(\gamma(v,y)=x(1;v,y)\) is therefore jointly smooth near each original zero velocity.

The exact initial-velocity variation at zero solves

\[
 \dot V=W,\qquad \dot W=0,\qquad
 V(0)=0,\quad W(0)=w,\qquad
 V(t)=tw,\quad W(t)=w .
 \tag{NG2}
\]

Every derivative in the quadratic velocity expression in NG1 vanishes at zero velocity; its position derivative also vanishes there. Thus NG2 is the actual NF12 variation equation. The initial-position variation is \((V,W)=(z,0)\). Consequently \(\gamma(0,y)=y\) and the actual original derivative \(D_v\gamma(0,y)=I\) is proved. Scaling the original curve's time by \(t\) gives a curve with initial velocity \(tv\) and the same complete quadratic equation; the chain rule contributes both factors of \(t\). Uniqueness gives \(x(t;v,y)=\gamma(tv,y)\) whenever those original curve segments are defined.

Under \(z=\kappa(x)\), the velocity changes by \(\dot z^a=\sum_i\partial_i\kappa^a\,v^i\). The second derivative retains both contributions. Hence the transformed Christoffel coefficients are precisely

\[
 \widetilde\Gamma^a_{bc}(\kappa(x))
 =\sum_{i,j}
  \left(\sum_k\partial_k\kappa^a(x)\Gamma^k_{ij}(x)
                  -\partial_{ij}\kappa^a(x)\right)
   \partial_b(\kappa^{-1})^i(\kappa(x))
   \partial_c(\kappa^{-1})^j(\kappa(x)).
 \tag{NG3}
\]

Both Hessian and original connection terms remain. They agree with HG2 for the actual transported metric
\(\widetilde g_{bc}=\sum_{i,j}g_{ij}\partial_b(\kappa^{-1})^i\partial_c(\kappa^{-1})^j\).
Here is a direct justification. HG2 is symmetric in its two lower indices and satisfies
\(\partial_k g_{ij}=\sum_\ell g_{\ell j}\Gamma^\ell_{ki}+\sum_\ell g_{i\ell}\Gamma^\ell_{kj}\);
substitution gives the full six-term right side
\(\frac12(\partial_kg_{ij}+\partial_ig_{kj}-\partial_jg_{ki}
+\partial_kg_{ji}+\partial_jg_{ki}-\partial_ig_{kj})\), which equals the original derivative. Apply the product and chain rules to the full displayed transported metric: its two differentiated coordinate factors yield the two Hessian contributions, and its differentiated \(g_{ij}\) yields the two original connection sums. The identity for the second derivative of \(\kappa\kappa^{-1}\) changes these Hessian contributions into the negative Hessian term in NG3. Thus NG3 is symmetric and has the same metric-compatibility identity for \(\widetilde g\). Conversely any symmetric compatible coefficients \(C^\ell_{jk}\) satisfy
\(2\sum_\ell g_{i\ell}C^\ell_{jk}
=\partial_jg_{ik}+\partial_kg_{ij}-\partial_ig_{jk}\),
by adding the first two compatibility identities and subtracting the third. Multiplication by the actual inverse \(G\) gives exactly HG2 and proves uniqueness. NG3 therefore has the required actual metric formula. NF20 now proves the coordinate-independent geodesic and endpoint maps on the actual tangent bundle.

For completeness the full differentiated metric and the inverse-coordinate Hessian comparison used above are, with \(K^i_b=\partial_b(\kappa^{-1})^i\),

\[
 \begin{aligned}
 \partial_d\widetilde g_{bc}
 &=\sum_{i,j,k}(\partial_kg_{ij})(\kappa^{-1}(z))
                           K^k_dK^i_bK^j_c\\
 &\quad+\sum_{i,j}g_{ij}(\kappa^{-1}(z))
       \left(\partial_{db}(\kappa^{-1})^iK^j_c
                        +K^i_b\partial_{dc}(\kappa^{-1})^j\right),\\
 \sum_k\partial_k\kappa^a(\kappa^{-1}(z))
                           \partial_{bc}(\kappa^{-1})^k
 &=-\sum_{i,j}\partial_{ij}\kappa^a(\kappa^{-1}(z))
                                             K^i_bK^j_c .
 \end{aligned}
 \tag{NG3a}
\]

The second line is the full second derivative of \(\kappa(\kappa^{-1}(z))=z\). Substitution of the six original compatibility terms into the first line retains the two connection products and both Hessian terms; substitution of the second line supplies precisely NG3. This explicitly gives every coordinate derivative contribution in the comparison.

### 17.9. The unaltered metric identity, all first jets and minimizing radius

The finite inverse theorem applies to \((v,y)\mapsto(\gamma(v,y),y)\) with its actual derivative. Near every \((0,y)\) it gives the full smooth inverse. In a local base neighborhood a positive velocity radius works uniformly after shrinking; all needed existence, injectivity and derivative bounds are open conditions on a compact smaller base neighborhood. Use the actual continuous metric norm \(r_y(v)=(v^tH(y)v)^{1/2}\) to choose the velocity balls. On the smaller base neighborhood its original coordinate norm comparison constants bound both inclusions, so a sufficiently small metric ball fits the original inverse neighborhood.

These local radii have a locally positive lower bound after taking a locally finite cover by smaller base neighborhoods and assigning each its positive radius. The original smooth positive-minorant proof MG7 gives a smaller smooth positive function \(R(y)\) below these allowed radii. Its support assignment and all original metric factors are retained. The map on \(r_y(v)<R(y)\) is injective in each fiber by its local inverse, and points over different centers have different second coordinates. It is a local diffeomorphism and injective, hence has an open image and a smooth inverse: its locally defined inverses agree on every overlap by injectivity. This supplies a neighborhood of the zero section and a neighborhood of the diagonal without assuming a uniform global injectivity radius. For compact centers the positive smooth radius has a positive minimum, and finitely many original chart bounds give the stated uniform constants.

Write \(\widetilde H(v,y)=(D_v\gamma)^tH(\gamma(v,y))D_v\gamma\). Its actual center value is \(H(y)\). Metric compatibility, proved above, gives constant geodesic energy; torsion freeness gives \(\nabla_t\partial_s q=\nabla_s\partial_tq\) for a velocity variation \(q(t,s)=x(t;v+sw,y)\). The two covariant derivatives have equal mixed-coordinate derivatives, and their original Christoffel sums agree because the lower indices are symmetric. Keeping both product terms therefore gives

\[
 \begin{aligned}
 \frac d{dt}\langle\dot q,\partial_s q\rangle_H
 &=\langle\nabla_t\dot q,\partial_s q\rangle_H
       +\langle\dot q,\nabla_t\partial_s q\rangle_H\\
 &=\tfrac12\partial_s\langle\dot q,\dot q\rangle_H
       =\langle v,w\rangle_{H(y)},\\
 \langle D_v\gamma(v,y)v,D_v\gamma(v,y)w\rangle_H
 &=\langle v,w\rangle_{H(y)},\\
 \sum_k\widetilde g_{jk}(v,y)v^k&=\sum_k g_{jk}(y)v^k.
 \end{aligned}
 \tag{NG4}
\]

The first term vanishes by the actual geodesic equation, the energy is the original initial energy \((v+sw)^tH(y)(v+sw)\), and the initial varied position is zero. Integration on the original time interval \([0,1]\) gives the second line. No orthonormal frame or rescaled velocity enters this identity.

Let \(A_{ijk}=\partial_k\widetilde g_{ij}(0,y)\). Symmetry and the quadratic terms of the last line in NG4 give \(A_{ijk}=A_{jik}\) and \(A_{ijk}=-A_{ikj}\). The full sequence
\(A_{ijk}=-A_{ikj}=-A_{kij}=A_{kji}=A_{jki}=-A_{jik}=-A_{ijk}\)
makes every coefficient zero. The complete integral Taylor formula is therefore

\[
 \begin{aligned}
 \widetilde g_{ij}(v,y)-g_{ij}(y)
 &=\sum_{k,l}v^kv^l\int_0^1
            (1-t)\partial_{kl}\widetilde g_{ij}(tv,y)\,dt,\\
 \widetilde G-G(y)
 &=-G(y)(\widetilde H-H(y))\widetilde G,\\
 r_y(v)^2&=v^tH(y)v,\qquad
 \operatorname{grad}_{\widetilde H}r_y(v)=v/r_y(v)
                         \quad(v\ne0).
 \end{aligned}
 \tag{NG5}
\]

The inverse comparison follows by multiplying both original inverse identities; its full left and right factors remain. Every finite collection of center derivatives of the first line has the same entire integral with its differentiated coefficients; compact-center bounds follow from smoothness on the actual compact charts. Its first velocity derivative is \(O(|v|)\), and the entire matrix differences are \(O(|v|^2)\), with the original norm comparison constants. The gradient identity follows by multiplying \(dr_y=H(y)v/r_y\) by the actual \(\widetilde G\) and using NG4. Its squared length is \(v^tH(y)v/r_y^2=1\).

Choose \(0<R_1<R_0<R_2\) whose closed original metric ball of radius \(R_2\) lies in the inverse neighborhood at the given center. Its closed image is compact and the image of \(r_y<R_0\) has boundary exactly the image of \(r_y=R_0\): the diffeomorphism on the larger ball preserves relative interiors and boundaries, and compactness excludes an extra boundary point outside that larger image. The radial curve from the center to \(v\) has length \(r_y(v)\). Any piecewise \(C^1\) curve remaining in this normal image and ending at \(v\) has length at least \(r_y(v)\), since away from zero \(|(r_y\circ c)'|\leq\|\dot c\|_H\). To handle the center without assuming differentiability of the radius there, fix \(0<\epsilon<r_y(v)\), take the last crossing of radius \(\epsilon\) before the endpoint, integrate the inequality on the following segment, and let \(\epsilon\) decrease to zero. If there are further zero-radius points, choose that last crossing; compactness of the time interval guarantees it. The inequality then holds on the whole remaining positive-radius segment.

If a curve to a point with \(r_y(v)<R_1\) leaves the outer image \(r_y<R_0\), its segment to its first boundary crossing has length at least \(R_0\), by approaching that crossing from inside and using the same radius argument. It is strictly longer than the retained radial curve. Thus curves which leave and return cannot lower the infimum. The actual Riemannian distance and square are

\[
 s(\gamma(v,y),y)=r_y(v),\qquad
 s(\gamma(v,y),y)^2=v^tH(y)v
                     \quad(r_y(v)<R_1).
 \tag{NG6}
\]

The radii can again be chosen locally uniformly in the center and reduced by MG7's positive minorant; compact-center subsets have uniform positive lower radii. The inverse endpoint map is jointly smooth, so the square is jointly smooth near the diagonal and the positive square root is smooth off the diagonal. No smoothness of the distance itself at the diagonal is claimed.

### 17.10. Every transformed divergence and density contribution

Keep the whole original coordinate operator and its distinct measure:

\[
 P=-\sum_{j,k=1}^n\partial_j\bigl(g^{jk}(x)\partial_k\bigr)I_r
       +\sum_{j=1}^n b^j(x)\partial_j+c(x).                    \tag{NG7a}
\]

\[
                   d\mu(x)=\rho(x)\,dx,
 \qquad \rho(x)=(\det G(x))^{-1/2}.                            \tag{NG7b}
\]

Here \(b^j,c\) are smooth complex matrices acting on the left. Their original rank and every original coordinate sum remain. These data define the receiving operator independently of an elliptic or geodesic conclusion.

For the actual original operator H1 keep \(x=\gamma(v,y)\), \(C=D_v\gamma\), \(J=|\det C|>0\). The original coordinate measure is \(dx=J\,dv\); the full Riemannian measure is \(\rho(\gamma(v,y))J\,dv\). Its density is not identified with coordinate measure or suppressed. The principal and lower-order coefficient transports are

\[
 \begin{aligned}
 \widetilde G&=C^{-1}G(\gamma(v,y))C^{-t},\\
 \widetilde b^{\,i}
 &=\sum_j(C^{-1})_{ij}b^j(\gamma(v,y))
      -\sum_k\widetilde g^{ik}J^{-1}\partial_kJ\,I_r,\\
 \widetilde c&=c(\gamma(v,y)).
 \end{aligned}
 \tag{NG7}
\]

To prove the divergence law, pair the original divergence against a smooth compact test and integrate by parts. The complete two gradient transforms are \(C^{-t}\partial_v\) and the full original substitution factor is \(J\). Their product gives
\(\int J\,(\partial_v\psi)^t\widetilde G\,\partial_v f\,dv\).
Integration by parts in \(v\) identifies the transported divergence as
\(J^{-1}\sum_{i,k}\partial_i(J\widetilde g^{ik}\partial_k f)\).
This equality of test integrals is equality of smooth coefficients, because a nonzero continuous difference has a compact test of the same sign or a complex component with nonzero pairing. Expanding the complete derivative retains both terms
\(\sum_{i,k}\partial_i(\widetilde g^{ik}\partial_kf)
+\sum_{i,k}J^{-1}\partial_iJ\,\widetilde g^{ik}\partial_kf\).
The original minus sign in H1 and symmetry of \(\widetilde G\) yield precisely the second line of NG7, with \(J^{-1}\partial_kJ=\partial_k\log J\). The first-order original matrices transform by the full state chain rule and continue to act on the left; the zeroth-order matrices are the stated compositions. Since the actual \(C(0,y)=I\), \(J(0,y)=1\). Smoothness and every compact parameter bound follow from the proved endpoint map, full inverse/cofactor formulas and the positive determinant. This proves HG10 with every Jacobian contribution, rather than identifying the original coordinate operator with a differently measured Laplacian.

### 17.11. Exact course use and its remaining interfaces

NF1--NF21 prove local existence, uniqueness, maximal continuation on its actual domain, jointly \(C^r\) parameter and initial-time dependence, every labeled higher variation, actual flow inverses, the ordered linear equation and full variation-of-constants maps. NG1--NG7 supply the original geodesic equation's dependence, endpoint derivative, unaltered normal-coordinate metric, first jets, true local minimizing radius and complete transformed drift and density. Their independently proved inverse and partition inputs are the actual earlier geometry/calculus providers.

The elementary scalar ray integral HS2--HS8 and matrix series HM2--HM7 remain their original proofs. Their center and parameter derivatives have the uniform compact bounds proved there; NF6--NF15 now give an additional general original-time linear provider. Bundle frame covariance of an amplitude requires the exact transformed operator and its normalized transport equation, not only existence of a smooth bundle or of a curve. Any remaining such receiving calculation must be checked in its actual matrix convention. The nonlinear flow entry also supplies the stated local base used by the collar construction; the collar's global injectivity, coefficient extension and boundary support arguments remain their own full assertions.

Complex Cauchy/residue/maximum principles, Laplace/Euler continuations, wavefront-qualified arbitrary-map pullbacks and source-formula comparisons are separate interfaces. This standard foundation proof makes no claim to establish those assertions.

## References

The coordinate amplitude construction is the Kuranishi change of phase variables discussed in [Grubb's author-hosted Chapter 8](https://web.math.ku.dk/~grubb/dist8n.pdf); the separate roles of operator microsupport and manifold assembly can also be compared in [Melrose's microlocalization chapter](https://math.mit.edu/~rbm/iml/Chapter5.pdf) and [manifold chapter](https://math.mit.edu/~rbm/iml/Chapter6.pdf).

## Further questions

The proofs suggest two further research directions. Quantizing bundle-valued principal symbols with extra geometric structure requires tracking the frame correction omitted by the scalar half-density refinement. Studying propagation beyond elliptic directions requires information about the characteristic symbol that is absent from the inequality (G27). Those are separate problems; neither is inferred from elliptic inversion alone.

## 18. Original wavefront and pullback foundations

This section proves the actual coordinate, product, qualified smooth-map and submersion pullbacks and their complete wavefront relations. It supplies strong smooth parameter dependence and differential elliptic regularity with the full original symbol, then compares the whole odd-wave kernel at nonzero cone points and its vertex. The test topology and scalar operations are proved in Sections13.1--13.6, [the original Fourier inverses](prerequisite-bridges.md) retain their factors, and [the nonlinear completed measure theorem](conormal-transmission.md) is proved in CX35a--c. The finite-symbol and conic operator proofs in Sections1/5/6/8 and [the Euclidean calculus](euclidean-symbol-calculus.md) are used on their stated domains. The exact original wave formulas are retained from [the wave kernel chapter](wave-hadamard-kernels.md).

### 18.1. The original Fourier estimate and every cutoff

Use the original convention

\[
\widehat f(\xi)=\int_{\mathbb R^d}e^{-ix\cdot\xi}f(x)\,dx,\qquad
f(x)=(2\pi)^{-d}\int_{\mathbb R^d}e^{ix\cdot\xi}\widehat f(\xi)\,d\xi.
\tag{WF1}
\]

For a compactly supported distribution \(v\), its Fourier transform is \(v(e^{-ix\cdot\xi})\), with a compact smooth cutoff equal to one on its support inserted in that pairing. The full finite-order test estimate and product rule give
\(|\widehat v(\xi)|\leq C(1+|\xi|)^m\) for some actual integer \(m\). Every frequency derivative has the same type of estimate, with its original multiplier \((-ix)^\alpha\) in the test. The estimate keeps the derivatives of the inserted support cutoff. A compact smooth test has rapidly decreasing transform by repeated integration by parts with \(1-\Delta_x\), whose full multiplier is \(1+|\xi|^2\). These facts follow on the original coordinates.

For \(b\in C_c^\infty\), inverse Fourier transformation of the test and the finite-order bound justify

\[
\widehat{bv}(\xi)=(2\pi)^{-d}
       \int_{\mathbb R^d}\widehat b(\xi-\eta)\widehat v(\eta)\,d\eta.
\tag{WF2}
\]

The integral is absolutely convergent: take the Schwartz decrease of \(\widehat b\) beyond the original polynomial order plus \(d\). It also converges in every test seminorm needed in the pairing, so the distribution can be passed through the integral. No Fourier multiplier constant is suppressed.

Suppose \(\widehat v\) decreases rapidly in an open cone \(V\), and the angular closure of a smaller cone \(W\) lies in \(V\). For \(\xi\in W,\eta\notin V\), angular separation gives
\(|\xi-\eta|\geq c(|\xi|+|\eta|)\) for some \(c>0\). To prove this, restrict to \(|\xi|+|\eta|=1\); the two closed angular sets are disjoint, so the continuous difference has a positive minimum. Scaling restores the original lengths. Split WF2 at \(\eta\in V\). On that region both original transforms decrease rapidly, and
\(1+|\xi|\leq(1+|\xi-\eta|)(1+|\eta|)\). Taking their exponents larger than \(N+d+1\) gives the requested output power \((1+|\xi|)^{-N}\) and an integrable residual power in \(\eta\). On the complement, take the cutoff exponent larger than \(N+m+d+1\); angular separation beats the full polynomial input bound. Thus multiplication preserves rapid decrease on \(W\).

Consequently the definition of \(\operatorname{WF}(u)\) using a cutoff equal to one near the original base point is unchanged if the cutoff is only nonzero there: multiply by its actual smooth reciprocal on a smaller neighborhood and use WF2. It is local. Its complement is open in the nonzero cotangent variables by the same smaller-neighborhood and smaller-cone construction, so the wavefront set is closed and conic. If all directions are regular over a compactly localized neighborhood, a finite cover of the original unit sphere and the cutoff estimate give rapid decrease everywhere. WF1 then proves smoothness with every derivative. Conversely compactly localized smooth functions have that decrease, so absence of all wavefront directions is exactly smoothness.

### 18.2. A full nonstationary integral bound

Let \(K\) be a fixed compact coordinate set and
\(I(\xi,\eta)=\int a(x)e^{i\Phi(x,\xi,\eta)}dx\), with \(a\) smooth and supported in \(K\). In each application below the original phase is linear in the frequency parameters, and its coordinate derivatives on \(K\) satisfy
\(|\partial_x^\alpha\Phi|\leq C_\alpha(|\xi|+|\eta|)\). Suppose its actual gradient satisfies
\(|\nabla_x\Phi|\geq c(|\xi|+|\eta|)\) on \(K\), for \(|\xi|+|\eta|\geq1\). Retain the entire operators

\[
\begin{aligned}
L&=\sum_j\frac{\partial_{x_j}\Phi}{i|\nabla_x\Phi|^2}\partial_{x_j},
&Le^{i\Phi}&=e^{i\Phi},\\
L^ta&=-\sum_j\partial_{x_j}
       \left(\frac{\partial_{x_j}\Phi}{i|\nabla_x\Phi|^2}a\right),
&I(\xi,\eta)&=\int (L^t)^Na(x)e^{i\Phi(x,\xi,\eta)}dx .
\end{aligned}
\tag{WF3}
\]

The superscript \(t\) denotes the bilinear integration transpose, not a conjugate adjoint. Boundary terms vanish because the original amplitude is compactly supported. Every derivative of each coefficient of \(L\) is bounded by \(C_\alpha(|\xi|+|\eta|)^{-1}\): the numerator has one frequency power, the denominator has two, and each differentiated quotient has the same net power, with the positive lower gradient bound retained. The full iterated product and chain rules in the calculus chapter give a finite sum at every \(N\), keeping every differentiated coefficient and amplitude. They therefore prove

\[
|I(\xi,\eta)|\leq C_N(1+|\xi|+|\eta|)^{-N}
                \max_{|\alpha|\leq N}\|\partial^\alpha a\|_\infty
\tag{WF4}
\]

on the separated region, enlarging \(C_N\) for bounded frequencies. Every fixed additional derivative of the amplitude or phase parameters has the corresponding estimate after increasing the number of integrations; its original polynomial frequency factors must be included before choosing \(N\). The constants depend on the actual compact set, gradient margin and finitely many original derivatives, rather than a replaced phase.

### 18.3. The exact diffeomorphism covector map

Let \(\kappa:X\to Y\) be a smooth diffeomorphism between coordinate opens of dimension \(d\), and put \(\phi=\kappa^{-1}\). The already constructed scalar pullback retains its full test Jacobian:

\[
\langle\kappa^*u,f\rangle
 =\langle u,(f\circ\phi)|\det D\phi|\rangle.
\tag{WF5}
\]

Fix \(x_0\), \(y_0=\kappa(x_0)\), and \(\xi_0\ne0\), and put
\(\eta_0=D\phi(y_0)^T\xi_0\). Suppose \((y_0,\eta_0)\) is regular for \(u\). Choose an original compact cutoff \(\chi\) equal to one on a neighborhood of \(y_0\) so that \(v=\chi u\) has rapidly decreasing transform on a cone \(V\) about \(\eta_0\). Shrink an \(x\)-cutoff \(b\) about \(x_0\) until its image lies in that neighborhood. Its transform after pullback is exactly

\[
\widehat{b\kappa^*u}(\xi)
=(2\pi)^{-d}\int\widehat v(\eta)I(\xi,\eta)\,d\eta,\qquad
I(\xi,\eta)=\int b(\phi(y))|\det D\phi(y)|
        e^{i(y\cdot\eta-\phi(y)\cdot\xi)}dy.
\tag{WF6}
\]

For each fixed \(\xi\), this is the Fourier inverse formula applied to a compact smooth test, and is absolutely convergent at large \(\eta\) by WF3. Its phase gradient is the original
\(\eta-D\phi(y)^T\xi\). On the compact support, both \(D\phi^T\) and its inverse have uniform finite norm bounds. Thus when \(|\eta|\) is below a sufficiently small multiple of \(|\xi|\), or above a sufficiently large multiple, the gradient is bounded below by \(c(|\xi|+|\eta|)\). For the remaining comparable lengths, continuity of \(D\phi\) and sufficiently small base/direction neighborhoods place \(D\phi(y)^T\xi\) in an angular cone whose closure lies in \(V\). If \(\eta\notin V\), compact angular separation gives the same lower bound. This compactness argument retains the full derivative matrix and its original covectors.

On those separated regions WF4 beats the polynomial bound for \(\widehat v\), with \(N\) larger than that order, the requested decay exponent and \(d\). On the remaining region \(\eta\in V\) and \(|\eta|\) comparable with \(|\xi|\), use the rapid input decrease and the original constant bound \(|I|\leq\int|b(\phi(y))||\det D\phi(y)|dy\). The integration volume is at most \(C(1+|\xi|)^d\); choosing the input decay exponent larger than that volume power and the requested output exponent proves rapid output decrease. Hence regularity at \((y_0,\eta_0)\) implies regularity at \((x_0,\xi_0)\). Applying this proved implication to the actual inverse diffeomorphism and using WF5's composition law proves both inclusions, giving the exact equality

\[
\operatorname{WF}(\kappa^*u)
 =\{(x,D\kappa(x)^T\eta):(\kappa(x),\eta)\in\operatorname{WF}(u)\}.
\tag{WF7}
\]

Invertibility keeps every displayed output covector nonzero. Both original Jacobians remain in WF5--WF6; they do not change the covector relation.

### 18.4. Products and the exact projection converse

For compact localizations \(v\) on \(\mathbb R^a\) and \(w\) on \(\mathbb R^b\), their already constructed tensor product has

\[
\widehat{v\otimes w}(\xi,\eta)=\widehat v(\xi)\widehat w(\eta).
\tag{WF8}
\]

Here the order of the two factors is input-coordinate order, as indicated by the variables; converting to the geometric chapter's output-then-input notation requires that actual permutation. The equality follows by its two original iterated test pairings and the factored exponential.

Write \(Z_u=\{(x,0):x\in\operatorname{supp}u\}\). Then

\[
\operatorname{WF}(u\otimes v)
\subset
\bigl((\operatorname{WF}(u)\cup Z_u)
      \times(\operatorname{WF}(v)\cup Z_v)\bigr)
          \setminus\{(\xi,\eta)=(0,0)\}.
\tag{WF9}
\]

Outside the product support the tensor distribution vanishes, by the proved exact support formula. At a point inside it but outside the displayed covector set, at least one nonzero component is a regular direction for its factor. Near that pair direction its length is at least a fixed positive fraction of the total frequency length. Its factor in WF8 decreases to every order, while the other has its original polynomial bound. Their product therefore decreases to every order in that product cone. Product spatial cutoffs are equal to one near the base point, so this proves the claimed inclusion with the correct original Fourier definition. WF2 then handles all smaller nonproduct cutoffs. No general equality for two arbitrary singular factors is asserted.

For the original projection \(\pi(x,y)=x\), define \(\pi^*u=u\otimes1\) by
\(\langle\pi^*u,f\rangle=\langle u,x\mapsto\int f(x,y)dy\rangle\). The integral test is smooth with compact support and every \(x\)-derivative is its actual integrated derivative, so this is a continuous distribution. The constant factor is smooth, and WF9 gives one inclusion in

\[
\operatorname{WF}(\pi^*u)
 =\{(x,y;\xi,0):(x,\xi)\in\operatorname{WF}(u)\}.
\tag{WF10}
\]

For the converse suppose \(\pi^*u\) is regular at \((x_0,y_0;\xi_0,0)\). By WF2 choose product cutoffs \(\alpha(x),\beta(y)\) supported in that regular base neighborhood, both equal to one near their respective points, with \(\beta\geq0\) and \(\int\beta>0\). Their full transform is
\(\widehat{\alpha u}(\xi)\widehat\beta(\eta)\). The regular cone contains \((\xi,0)\) for all \(\xi\) in a smaller cone about \(\xi_0\). Its restriction at \(\eta=0\) is the original nonzero scalar \((\int\beta)\widehat{\alpha u}(\xi)\). Division by that scalar proves rapid decrease of the original factor, contradicting singularity at \((x_0,\xi_0)\). This proves the exact converse, not only the forward inclusion.

### 18.5. Constructing the pullback for the original smooth map

Let \(F:X\subset\mathbb R^b\to Y\subset\mathbb R^a\) be smooth. Its precise normal set and the required condition are

\[
N_F=\{(F(x),\eta):\eta\ne0,\ DF(x)^T\eta=0\},
\qquad N_F\cap\operatorname{WF}(u)=\varnothing.
\tag{WF11}
\]

We construct the map under this original transversality condition; no pullback at a forbidden covector is assumed. Near any fixed \(x_0\), the unit directions in the kernel of \(DF(x_0)^T\) form a compact set, possibly empty. WF11 makes every such direction regular at \(F(x_0)\). A finite regular cone cover, a common sufficiently small target cutoff \(\chi\), and WF2 give an open cone \(V_{\rm reg}\) on which \(\widehat{\chi u}\) decreases to every order, containing an angular neighborhood of those kernel directions. On the compact complementary unit directions \(DF(x_0)^T\eta\) has a positive lower norm. Continuity allows a fixed original neighborhood \(U_0\) of \(x_0\) and a constant \(c>0\) with
\(|DF(x)^T\eta|\geq c|\eta|\) there for every complementary direction. Shrink \(U_0\) so its image lies in the region where \(\chi=1\).

For \(f\in C_c^\infty(U_0)\), put \(v=\chi u\) and define

\[
\langle F^*u,f\rangle
=(2\pi)^{-a}\int_{\mathbb R^a}\widehat v(\eta)
                   \left(\int_{U_0}f(x)e^{iF(x)\cdot\eta}dx\right)d\eta.
\tag{WF12}
\]

On \(V_{\rm reg}\), the rapid input decrease and \(\int|f|\) give an integrable bound. On its complement, the actual phase gradient is \(DF(x)^T\eta\), so WF4 gives a bound \(C_N(1+|\eta|)^{-N}\max_{|\alpha|\leq N}\|\partial^\alpha f\|_\infty\). Multiplying by the original polynomial bound for \(\widehat v\) and choosing \(N>m+a\) proves absolute convergence. It also proves a continuous finite-order distribution estimate on each original compact test support, with its complete coordinate and map derivative constants. For smooth \(u\), WF1 and absolute testing show that this is exactly the smooth scalar function \(u(F(x))\).

Here is the needed independence and locality, rather than an assumed gluing rule. Use the original Cartesian Gaussian regularization
\[
g_\epsilon(y)=(4\pi\epsilon)^{-a/2}
      e^{-|y|^2/(4\epsilon)},\qquad
v_\epsilon=g_\epsilon*v,\qquad
\widehat v_\epsilon(\eta)=e^{-\epsilon|\eta|^2}\widehat v(\eta).
\tag{WF13}
\]
Its full mass and Fourier identity are proved in the integration/Fourier chapters. The two absolute bounds for WF12 dominate uniformly for \(0<\epsilon\leq1\), since \(0<e^{-\epsilon|\eta|^2}\leq1\). Thus WF12 is the limit of the actual smooth pullbacks \(v_\epsilon\circ F\).

If two target cutoffs equal one near \(F(\operatorname{supp}f)\), their difference times \(u\) is a compact distribution \(w\) vanishing near that compact image. The distance between that image and \(\operatorname{supp}w\) is positive. Its original compact finite-order estimate, applied to every derivative of \(g_\epsilon(F(x)-y)\), shows uniform convergence to zero on that image, including every fixed \(x\)-derivative: the full differentiated Gaussian has finitely many polynomial factors in the original difference coordinates and inverse powers of \(\epsilon\), times the same exponential. For distance at least \(d>0\), each such factor is bounded by \(C\epsilon^{-M}e^{-d^2/(8\epsilon)}\), tending to zero. The inserted support cutoff derivatives also remain in this estimate. Consequently the two limits agree on \(f\).

The same argument handles restriction to smaller original neighborhoods. For a compact test crossing several \(U_0\)'s, choose a finite smooth partition subordinate to them and sum WF12. On an overlap the preceding common Gaussian comparison gives equality; refinements therefore have the same sum. This constructs a unique local distribution \(F^*u\) on all of \(X\) with these formulas, preserving the original map. It proves its locality and compatibility with restriction. At a diffeomorphism, the smooth Gaussian approximations and the full measure substitution show agreement with WF5, including its actual inverse Jacobian. At the projection the same approximations and the integrated test show agreement with WF10's construction.

Its precise wavefront bound is

\[
\operatorname{WF}(F^*u)
\subset\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}.
\tag{WF14}
\]

For completeness fix a nonzero \(\xi_0\) outside the displayed set over \(x_0\). The singular unit target directions over \(F(x_0)\) are compact. WF11 says their images under \(DF(x_0)^T\) never vanish, and the chosen output direction is different from every resulting direction. Compactness yields positive margins for both assertions. Choose a closed angular neighborhood \(\Gamma\) of that singular set retaining these margins. Its complementary directions have a finite regular cone cover; WF2 again chooses a common target cutoff so that \(\widehat v\) decreases to every order outside \(\Gamma\). Shrink both original base and output direction neighborhoods so the margins hold for all \(x\) in the support of a cutoff \(b\) and every allowed output \(\xi\). If the singular set is empty, local smoothness already proved in Section18.1 supplies the conclusion directly.

The localized output transform is WF12 with \(f(x)=b(x)e^{-ix\cdot\xi}\). Its inner phase is exactly \(F(x)\cdot\eta-x\cdot\xi\), with gradient \(DF(x)^T\eta-\xi\). For \(\eta\in\Gamma\), the two compact margins give
\(|DF(x)^T\eta-\xi|\geq c(|\eta|+|\xi|)\): normalize their combined lengths to one; if the continuous difference had zero minimum, the covectors would have the excluded common direction, or a nonzero singular target direction would map to zero. WF4 therefore beats the full polynomial input bound and gives every output inverse power after integration in \(\eta\).

For \(\eta\notin\Gamma\), use the rapidly decreasing input. Split at \(|\eta|\leq c_0|\xi|\), with \(c_0>0\) smaller than the reciprocal of twice the actual compact bound for \(\|DF^T\|\). On that region the gradient has norm at least \(|\xi|/2\), so WF4 and the rapid input bound give every output power. On the other region \(|\eta|>c_0|\xi|\), the original bound for the inner integral is \(\int|b|\); taking the input decay exponent larger than the requested output exponent plus \(a+1\) gives every output power after integrating the full tail. This proves WF14 with the original Fourier constant still present in WF12. It proves a bound, and does not claim a converse for an arbitrary smooth map.

For a submersion \(F\), the normal set is empty, so the construction applies to every \(u\). Retain a nonzero \(a\)-row derivative minor at \(x_0\) and complete \(F\)'s coordinates by the remaining original \(x\)-coordinates. The resulting map \(\kappa(x)=(F(x),x_J)\) has its actual nonzero determinant. The proved inverse/implicit theorem gives a local diffeomorphism; in these coordinates \(F=\pi\circ\kappa\). Gaussian comparison in WF12 proves \(F^*u=\kappa^*(\pi^*u)\). WF7 and the exact WF10 converse therefore give

\[
\operatorname{WF}(F^*u)
 =\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}
 \quad\text{for a submersion}.
\tag{WF15}
\]

The derivative identity is the original chain rule
\(DF^T=D\kappa^T D\pi^T\). Its injectivity on target covectors is precisely full row rank, so every right-hand covector is nonzero. Every dimension-zero case has its point mass and empty Fourier factor; when the target has dimension zero, its distributions are smooth constants and both wavefront sets are empty.

### 18.6. Absence of parameter-normal covectors gives the actual smooth family

Let \(u\) be a distribution on an open product in the original variables \((t,x)\in\mathbb R^p\times\mathbb R^q\), with no wavefront covector \((t,x;\tau,0)\), \(\tau\ne0\). Every slice embedding \(j_t(x)=(t,x)\) satisfies WF11, because its transpose sends \((\tau,\xi)\) to \(\xi\). Thus the already constructed restriction \(u_t=j_t^*u\) exists.

Fix compact spatial test support and a small compact parameter neighborhood. The compact base set and the compact unit sphere in the original \(\tau\)-coordinates have a finite regular cone/base cover. Use its finite spatial partition and common smaller parameter neighborhood. After each compact localization \(v\), WF2 gives a constant \(\delta>0\) such that \(\widehat v(\tau,\xi)\) decreases to every order when \(|\xi|\leq\delta|\tau|\); on the whole space it has the original polynomial bound \(C(1+|\tau|+|\xi|)^m\). Summing the finitely many localized formulas retains all their cutoff derivatives.

For a spatial test \(\psi\), the actual pairing on the neighborhood where the parameter cutoff is one is

\[
\langle u_t,\psi\rangle
=(2\pi)^{-(p+q)}
 \iint e^{it\cdot\tau}\widehat v(\tau,\xi)\widehat\psi(-\xi)
                           \,d\xi\,d\tau,\qquad
\partial_t^\alpha e^{it\cdot\tau}=(i\tau)^\alpha e^{it\cdot\tau}.
\tag{WF16}
\]

In \(|\xi|\leq\delta|\tau|\), the rapid decrease of \(\widehat v\) dominates every original factor \(\tau^\alpha\) and both integration dimensions, while \(|\widehat\psi|\leq\int|\psi|\). In the complementary region, \(|\tau|\leq|\xi|/\delta\). The polynomial bound for \(v\), multiplied by the Schwartz bound
\[
|\widehat\psi(\xi)|\leq
(1+|\xi|^2)^{-N}
\int |(1-\Delta_x)^N\psi(x)|dx,
\tag{WF17}
\]
is integrable after both integrations when \(2N>m+|\alpha|+p+q\). The integral in WF17 is bounded by finitely many original test derivative seminorms on the fixed support, with every binomial and derivative from \((1-\Delta)^N\) retained in that full operator. These bounds are uniform on bounded sets of tests. For each derivative order, take a corresponding \(N\); no one fixed finite test order for all parameter derivatives is inferred.

Dominated differentiation therefore gives every derivative in WF16. Taylor's remainder for \(e^{ih\cdot\tau}\), bounded by a constant times \(|h|^2|\tau|^2\), and the same bounds with two additional frequency powers prove convergence of difference quotients uniformly on every bounded set of spatial tests. Continuity uses the same dominated bounds. This is precisely smoothness into the strong distribution topology, whose seminorms are suprema of pairings over bounded test sets. It is stronger than only the smoothness of each single pairing.

To verify that WF16 is the original pullback, apply WF13 to \(v\), then restrict the smooth Gaussian approximations. Their transforms acquire the full factor \(e^{-\epsilon(|\tau|^2+|\xi|^2)}\), bounded by one. The just proved absolute envelopes allow its limit and every fixed parameter derivative in WF16, agreeing with WF12 for the slice map. Finally testing against any original compact smooth \(\varphi(t,x)\) and applying these absolute bounds permits integration in \(t\), and recovers the original distribution pairing by WF1. Thus the family reconstructs \(u\), rather than an unrelated family with the same notation. Finite localization and restriction compatibility paste these actual families on the whole parameter domain. For \(p=0\) there is no parameter derivative; for \(q=0\) the no-normal condition is absence of all nonzero covectors and Section18.1 proves the required scalar smoothness.

### 18.7. Differential elliptic regularity with the entire original symbol

The actual finite-symbol composition and its complete remainder are proved in the Euclidean chapter, E19--E22. Local support-controlled summation and conic separation are proved in the geometric chapter, Sections1/5/6, and its G24 proves that a proper operator has
\(\operatorname{WF}(Av)\subset\operatorname{WF}(A)\cap\operatorname{WF}(v)\).
We use these proved maps on their actual domains. In particular the composition product below is its full oscillatory product, rather than multiplication of a leading term. The positive remainder gain used here is one, for the original class \(S^m_{1,0}\).

In fixed original coordinates and frames let the actual differential operator between bundles of the same finite rank be

\[
\begin{aligned}
P(x,D)&=\sum_{|\alpha|\leq m}A_\alpha(x)D^\alpha,
&D_j&=-i\partial_{x_j},\\
a(x,\xi)&=\sum_{|\alpha|\leq m}A_\alpha(x)\xi^\alpha,
&p_m(x,\xi)&=\sum_{|\alpha|=m}A_\alpha(x)\xi^\alpha .
\end{aligned}
\tag{WF18}
\]

Here \(m\) is a nonnegative integer. Every coefficient and every lower-order term remains in \(a\), which is the working symbol throughout. In a scalar case the matrices are one by one. At a noncharacteristic original covector \((x_0,\xi_0)\), \(\xi_0\ne0\), the square matrix \(p_m(x_0,\xi_0)\) is invertible. Homogeneity, continuity of all its entries and finite-dimensional inverse continuity give a compact base neighborhood and a closed angular neighborhood of \(\xi_0/|\xi_0|\) on which
\(\|p_m(x,\xi)^{-1}\|\leq C|\xi|^{-m}\).
These are estimates of the original principal polynomial, with the original Euclidean matrix norms. For each lower coefficient the compact coefficient bounds retain
\(\|A_\alpha(x)\||\xi^\alpha|\), and their complete finite sum is at most
\(\sum_{|\alpha|<m}C_\alpha|\xi|^{|\alpha|}\).
For \(m\geq1\), choose the frequency radius so

\[
\left\|p_m(x,\xi)^{-1}
       \sum_{|\alpha|<m}A_\alpha(x)\xi^\alpha\right\|
\leq C\sum_{|\alpha|<m}C_\alpha|\xi|^{|\alpha|-m}
\leq\frac12 .
\tag{WF19}
\]

The ordered identity
\[
a^{-1}
=\left(I+p_m^{-1}\sum_{|\alpha|<m}A_\alpha\xi^\alpha\right)^{-1}
        p_m^{-1}
\tag{WF20}
\]
and the actual convergent finite-dimensional geometric series for the first inverse prove invertibility of the full \(a\) and
\(\|a^{-1}\|\leq2C|\xi|^{-m}\) there. The whole lower-term sum remains in WF19--WF20. For \(m=0\) the sum is empty and \(a=A_0\); its original inverse is bounded on that base neighborhood at all frequencies. Increasing the radius above one permits the usual symbol estimates with \(\langle\xi\rangle=(1+|\xi|^2)^{1/2}\), retaining the exact inequalities
\(|\xi|\leq\langle\xi\rangle\leq\sqrt2|\xi|\).
No rescaled replacement for \(a\) is introduced.

Every derivative of this original inverse is obtained from differentiating \(aa^{-1}=I\). Write a joint multi-index \(\gamma=(\beta,\alpha)\) for original base and frequency derivatives, and \(\nu=(\nu_x,\nu_\xi)\). The complete recurrence, with its actual matrix order, is

\[
\partial_x^\beta\partial_\xi^\alpha a^{-1}
=-a^{-1}
 \sum_{\substack{0<\nu\leq(\beta,\alpha)}}
  \binom{(\beta,\alpha)}{\nu}
  (\partial_x^{\nu_x}\partial_\xi^{\nu_\xi}a)
  (\partial_x^{\beta-\nu_x}
        \partial_\xi^{\alpha-\nu_\xi}a^{-1}) .
\tag{WF21}
\]

For derivative order zero use the just proved bound. In each summand at positive total order the final inverse derivative has smaller total order. Induction, the original polynomial derivative estimate
\(\|\partial_x^{\nu_x}\partial_\xi^{\nu_\xi}a\|
\leq C_\nu\langle\xi\rangle^{m-|\nu_\xi|}\),
and the exact three exponents in that ordered summand give
\[
\langle\xi\rangle^{-m}
\langle\xi\rangle^{m-|\nu_\xi|}
\langle\xi\rangle^{-m-|\alpha-\nu_\xi|}
=\langle\xi\rangle^{-m-|\alpha|}.
\tag{WF22}
\]
Every binomial, differentiated original coefficient and inverse factor is retained in WF21; the finite sum supplies its actual constant. Thus the full inverse is in \(S^{-m}_{1,0}\) on this cone.

Choose original base/angular/high-frequency cutoffs whose product \(\theta\) is supported strictly in that invertibility region and equals one on a smaller conic neighborhood for sufficiently large frequency. Extend
\(b_0=\theta a^{-1}\) by zero outside it. This is smooth across its support boundary because \(\theta\) vanishes on a neighborhood of that boundary. All its derivative estimates follow from the full sum
\[
\partial^{(\beta,\alpha)}b_0
 =\sum_{\nu\leq(\beta,\alpha)}
   \binom{(\beta,\alpha)}{\nu}
   (\partial^\nu\theta)
   (\partial^{(\beta,\alpha)-\nu}a^{-1}).
\tag{WF23}
\]
Above the cutoff radius \(ab_0=b_0a=I\) on the smaller cone. On that cone the actual full composition products have
\(\ell=I-b_0\circ a\) and \(r=I-a\circ b_0\) of order \(-1\).
This follows from E21 with \(N=1\), and includes the whole composition remainder. The entire higher expansion is
\[
b_0\circ a-
 \sum_{|\gamma|<N}
  \frac{(\partial_\xi^\gamma b_0)(D_x^\gamma a)}{\gamma!}
 \in S^{-N}_{1,0}
\tag{WF24}
\]
on that smaller cone; every original \(A_\alpha\) contributes through \(D_x^\gamma a\). Extend the restricted errors with further cutoffs equal to one on a still smaller cone, and form their powers there. The proved conic separated-support calculus makes every change of extension smoothing on the final cone. It does not set any nonzero off-cone remainder equal to zero.

The ordered finite inverse identities on that conic calculus are
\[
\left(\sum_{j=0}^{N-1}\ell^{\circ j}\circ b_0\right)\circ a
   =I-\ell^{\circ N},\qquad
a\circ\left(\sum_{j=0}^{N-1}b_0\circ r^{\circ j}\right)
   =I-r^{\circ N}.
\tag{WF25}
\]
The notation in this display denotes the original conic germs; after the cutoff extensions each equality has the corresponding conic smoothing discrepancy, already proved by the separation estimates. The finite identities themselves follow by associativity and telescoping, with the left powers on the left and the right powers on the right. Each \(j\)-term has order \(-m-j\). Support-controlled local summation gives \(b_L,b_R\) such that their differences from the first \(N\) terms have order \(-m-N\). Composing their actual tails with \(a\), and using WF25, proves both errors have order \(-N\) for every \(N\) on one fixed final cone. Hence their errors are smoothing there. The exact ordered comparison
\[
b_L-b_R=b_L\circ(I-a\circ b_R)
                 +(b_L\circ a-I)\circ b_R
\tag{WF26}
\]
and the conic smoothing ideal show that either sum is a two-sided inverse there. Proper quantization yields a proper \(B\) of order \(-m\) with \(I-BP\) and \(I-PB\) smoothing in that original covector neighborhood. A compact coordinate localization makes the original differential operator proper for this construction; the separated exterior-input kernel is smooth on the smaller output neighborhood, as proved in G5/G17. Thus this local construction applies to every distribution on the original open domain, without a support assumption on the whole input.

If \(Pu\) is regular at the original covector, the exact distribution identity
\[
u=B(Pu)+(I-BP)u
\tag{WF27}
\]
and G24 prove regularity of both terms there: the first because proper \(B\) does not enlarge the wavefront of its input, and the second because its operator symbol is smoothing on that cone. No smoothness of \(Pu\) away from the selected cone is assumed. Conversely G24 for the original differential operator gives \(\operatorname{WF}(Pu)\subset\operatorname{WF}(u)\). Consequently
\[
\operatorname{WF}(u)\subset
 \operatorname{WF}(Pu)\cup\operatorname{Char}_m(P),\qquad
\operatorname{WF}(Pu)\setminus\operatorname{Char}_m(P)
=\operatorname{WF}(u)\setminus\operatorname{Char}_m(P),
\tag{WF28}
\]
where
\(\operatorname{Char}_m(P)=\{(x,\xi):\xi\ne0,\ p_m(x,\xi)
\text{ is not invertible}\}\).
The latter set is the actual characteristic set for an order-\(m\) differential operator: an inverse principal matrix implies the full lower bound by WF19--WF20, while a singular principal matrix has a nonzero kernel vector whose full \(a(x,t\xi)\) norm is bounded by the retained lower sum \(O(t^{m-1})\), ruling out an order-\(m\) lower bound on that ray. For \(m=0\) singularity of \(A_0\) rules it out directly.

The construction uses the original coordinate and frame maps. The derivative transpose law in WF7 and the full bundle coefficient transport in the geometric chapter preserve the displayed regular directions; multiplication by an invertible smooth frame matrix and its inverse preserves componentwise wavefront by the cutoff lemma. Thus WF28 applies intrinsically to the differential bundle operator, with all its original coefficients. The argument supplies no zero-gain parametrix at the equality endpoint \(\delta=\rho\); the gain used in every tail estimate was exactly one.

For the original wave operator in the wave chapter, \(P=\partial_t^2-\sum_{j=1}^n\partial_{x_j}^2\), the convention \(D=-i\partial\) gives its entire symbol
\[
a(t,x;\tau,\xi)=-\tau^2+\sum_{j=1}^n\xi_j^2,\qquad
\operatorname{Char}_2(P)=
\{(t,x;\tau,\xi):(\tau,\xi)\ne(0,0),\quad
                        \tau^2=\sum_{j=1}^n\xi_j^2\}.
\tag{WF29}
\]
For \(n\geq1\), every characteristic covector has a nonzero spatial component when its time component is nonzero. A parameter-normal covector for the spatial slice parameter \(x\), namely \((\tau,\xi)=(0,\xi)\) with \(\xi\ne0\), is not characteristic: its original symbol value is \(\sum_j\xi_j^2>0\). The next section verifies the exact receiving recurrence before using this fact.

### 18.8. The entire original odd-wave receiving comparison

Retain \(n\geq1\), \(\nu\in\mathbb N_0\) and every original constant from W11/W14/W15/W17. Put \(L=\partial_t^2-\sum_j\partial_{x_j}^2\), and let \(\mathcal R(t,x)=(-t,x)\). The odd family is the actual distribution difference

\[
\begin{aligned}
E_\nu&=\nu!R_{\nu+1},&
A_\nu&=2^{-2\nu-1}\pi^{(1-n)/2},&
a_\nu&=\nu+(1-n)/2,\\
W_\nu&=E_\nu-\mathcal R^*E_\nu,&
q(t,x)&=t^2-\sum_{j=1}^n x_j^2,\\
LE_0&=\delta_{(0,0)},&
LE_\nu&=\nu E_{\nu-1}\quad(\nu\geq1),&
L^{\nu+1}E_\nu&=\nu!\delta_{(0,0)}.
\end{aligned}
\tag{WF30}
\]

These full distribution identities, including the point source, are proved in W5/W11/W17 by the original Fourier--Laplace transforms. The last equality follows by induction and retains each integer factor \(\nu(\nu-1)\cdots1=\nu!\); for \(\nu=0\) the empty product is one. The reflection has derivative \(\operatorname{diag}(-1,I_n)\) and absolute determinant one, so its pullback preserves the point mass and commutes with every term of \(L\). Thus
\[
L^{\nu+1}W_\nu
=\nu!\delta_{(0,0)}-\nu!\mathcal R^*\delta_{(0,0)}
=0 .
\tag{WF31}
\]
The two source terms are retained explicitly before their equality is used. Elliptic regularity WF28 for the actual operator \(L^{\nu+1}\), whose full constant symbol is
\((-\tau^2+\sum_j\xi_j^2)^{\nu+1}\), excludes every nonnull covector at the vertex. It does not assert that either retarded source term alone has that exclusion.

At a nonzero cone point \(q=0\), \(t\ne0\) and
\(dq=2(t,-x)\ne0\). The source gives the entire local expression
\(\operatorname{sgn}(t)A_\nu\chi_+^{a_\nu}(q)\), where the sign is constant on a sufficiently small neighborhood. The map \(q\) is a submersion there. The one-variable distribution \(\chi_+^{a_\nu}\) is nonzero, real, supported in the nonnegative half-line, and homogeneous of the original degree \(a_\nu\), as proved by its Euler integral and derivative continuation in the wave chapter. It cannot be smooth at zero: smoothness and vanishing on the negative half-line would make every derivative at zero vanish; the resulting Taylor estimate of any order, compared along positive dilations with its original homogeneity, would force it to vanish on the positive half-line. A distribution supported only at zero is a finite sum of delta derivatives by the compact finite-order/Taylor argument and is smooth only if zero; those nonzero continuation values are therefore singular as well. This contradicts nonzero \(\chi_+^{a_\nu}\). It has no other singular base point. For a real cutoff, its transform has equal magnitude in opposite directions, so failure of rapid decay in one of the two one-dimensional directions implies failure in both. The equivalence between smoothness and absence of every direction in Section18.1 proves
\[
\operatorname{WF}(\chi_+^{a_\nu})
=\{(0,\lambda):\lambda\ne0\}.
\tag{WF32}
\]

Here is the point-support assertion used in that argument. Let a one-variable distribution \(T\) be supported at zero and have finite order \(M\) on a fixed compact neighborhood. If every derivative of a test \(f\) through order \(M\) vanishes at zero, its Taylor remainders satisfy
\(f^{(j)}(s)=o(|s|^{M-j})\), \(0\leq j\leq M\).
Choose a fixed compact cutoff \(\zeta=1\) near zero and set
\(\zeta_\epsilon(s)=\zeta(s/\epsilon)\).
The full derivative product is
\((\zeta_\epsilon f)^{(k)}
=\sum_{j=0}^k\binom{k}{j}\epsilon^{-j}
\zeta^{(j)}(s/\epsilon)f^{(k-j)}(s)\).
On its support each summand is \(o(\epsilon^{M-k})\), hence tends to zero for every \(k\leq M\). Support locality gives
\(T(f)=T(\zeta_\epsilon f)\), and the actual order-\(M\) bound proves this value is zero. Subtracting the entire Taylor polynomial of an arbitrary test, with the fixed cutoff, therefore gives
\[
T(f)=\sum_{j=0}^M\frac{T(\zeta(s)s^j)}{j!}f^{(j)}(0),
\qquad
T=\sum_{j=0}^M
\frac{(-1)^jT(\zeta(s)s^j)}{j!}\delta_0^{(j)} .
\tag{WF32a}
\]
All signs and factorials follow from
\(\delta_0^{(j)}(f)=(-1)^jf^{(j)}(0)\).
A smooth function supported at a point is zero by continuity, so any nonzero point-supported continuation value is singular.

The exact submersion converse WF15 and the smooth nonzero factor and its inverse now give every and only nonzero multiple of \(dq\) over each nonzero cone point. In original coordinates these satisfy
\[
t^2=\sum_jx_j^2,\qquad
\tau^2=\sum_j\xi_j^2,\qquad
\tau x+t\xi=0,\qquad(\tau,\xi)\ne(0,0).
\tag{WF33}
\]
Indeed \((\tau,\xi)=2\lambda(t,-x)\) proves all three equations. Conversely \(t\ne0\) and the last vector equation give
\(\xi=-(\tau/t)x\); \(\tau=0\) would then force the excluded zero covector, and the multiple is the original \(\lambda=\tau/(2t)\).
Away from the cone the source's function or continued distribution expression is smooth, so these directions exhaust its nonvertex wavefront.

For any nonzero null covector \((\tau,\xi)\), the original base points
\((t_s,x_s)=s(\tau,-\xi)\), \(s>0\), are nonzero cone points with
\(dq(t_s,x_s)=2s(\tau,\xi)\). At each of them the same retained covector lies in the wavefront by the exact converse just proved. Closedness from Section18.1 as \(s\downarrow0\) includes it over the vertex. Together with WF31 and WF28 this proves the full original OE22 equality
\[
 \operatorname{WF}(W_\nu)=
 \{(t,x;\tau,\xi):
   (\tau,\xi)\ne0,\ t^2=|x|^2,
   \tau^2=|\xi|^2,\ \tau x+t\xi=0\}.
 \tag{WF34}
\]

In this exact set \(\tau=0\) forces \(\xi=0\), which is excluded. Thus the embedding \(j_x(t)=(t,x)\) has its entire normal set disjoint from the wavefront, including at \(x=0\). WF12 constructs every original time-distribution slice, and Section18.6 with parameter \(x\) proves a strong smooth map
\(x\mapsto W_\nu(\,\cdot\,,x)\).
Differentiation in time commutes with that map: its transposed test derivative preserves bounded test sets, as proved in GK23, so
\(x\mapsto\partial_tW_\nu(\,\cdot\,,x)\) is strong smooth as well. These slices agree with the explicit OE10--OE17 construction: for \(x\ne0\) both are the same source expression, and both are continuous into distributions at zero, so their difference at zero is the limit of their zero difference away from zero. Every factorial and finite-test-order bound in OE11/OE18 remains intact; the present argument never replaces those bounds by a negative derivative order or by one fixed finite order for all spatial derivatives.

All clauses of the original distribution foundation now have written proofs here or in the exact elementary distribution, finite-symbol and conic-calculus sections named above. Its original wave-kernel application has been compared in full, including both cancelling point sources and every nonvertex/vertex covector.
