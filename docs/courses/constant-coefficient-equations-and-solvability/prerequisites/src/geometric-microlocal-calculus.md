# Detecting regularity without choosing coordinates

**AN-03 · Unit AN03-U012 · Independent English AI draft, not admitted.**

An operator has two kinds of locality. Its kernel determines which input points can influence an output point. Its symbol determines which cotangent directions can carry an irregularity. We construct these two structures together, then use them to measure regularity of sections of arbitrary finite-rank complex bundles. All manifolds below are Hausdorff, second countable, smooth, and without boundary; compactness is imposed only where stated.

The analytic inputs are [AN03-U010](euclidean-symbol-calculus.md), especially AN03-EUC-002–005 and AN03-EUC-008–009, and the quadratic multiplier theorem AN03-GAU-007–008 of [AN03-U002](gauss-transform-estimates.md). The convention is \(D=-i\partial\), with inverse Fourier factor \((2\pi)^{-n}\). Local symbols have estimates on each compact base set, with no uniformity across a noncompact manifold. Unless parameters are displayed, \(S^m=S^m_{1,0}\) and \(\Psi^m=\Psi^m_{1,0}\).

We retain precise foundational contracts. **AN03-DEP-GEO-DIST** supplies distributions as continuous functionals on compact smooth densities, their restriction and multiplication by smooth functions, tensor products, Fourier transformation, the finite-order estimate on compact supports, and the scalar Schwartz kernel theorem for continuous \(C_c^\infty(U)\to\mathcal D'(V)\) maps on Euclidean open sets. The kernel theorem includes its identification with separately continuous bilinear test pairings, jointly continuous on every pair of fixed compact-support test spaces; it is a prerequisite, not proved from functional-analysis axioms here. The test spaces carry their usual smooth Fréchet topologies at fixed support and their inductive-limit topology over supports; distributions carry the strong dual topology. **AN03-BASE-GEO-MANIFOLD** supplies smooth atlases, the chain rule, inverse function theorem, locally finite smooth partitions of unity with compact supports subordinate to open covers, and finite-rank bundle gluing. **AN03-DEP-GEO-UB** supplies uniform boundedness for test-function Fréchet spaces and the closed graph theorem from a Banach space to a Fréchet space. Lebesgue change of variables, Fubini, dominated convergence, and Fourier inversion/Plancherel have the same exact entry contracts as U010. We prove the geometric kernel adapter and the wavefront results used below; no general theorem about multiplying arbitrary distributions is assumed.

## AN03-GEO-001 — Local estimates and amplitude reduction

For an open set \(U\subset\mathbb R^n\), \(a\in S^m_{\rho,\delta}(U\times\mathbb R^n)\) means that
\[
\sup_{x\in K,\xi}\langle\xi\rangle^{-m+\rho|\alpha|-\delta|\beta|}
|\partial_\xi^\alpha\partial_x^\beta a(x,\xi)|<\infty
\quad(K\Subset U),
\qquad 0<\rho\leq1,\quad0\leq\delta<1.
\tag{G1}
\]
These seminorms define the local Fréchet topology, using a compact exhaustion. On an open conic set \(\mathcal C\subset U\times(\mathbb R^n\setminus0)\), the same estimates are required along \((x,t\xi)\), \(t\geq1\), for every compact subset of \(\mathcal C\). They make no assertion about approaching the zero section outside such compact sets. A symbol defined at all frequencies must also be smooth there.

Local asymptotic summation follows with support control. Given \(a_j\) of orders \(m_j\to-\infty\), take a locally finite partition \(\theta_l\) of the base, or of a relatively compact angular/base cover in the conic case. Apply AN03-EUC-002 to each compactly supported piece \(\theta_l a_j\), extended into its coordinate product by zero, obtaining \(b_l\) with support contained in \(\bigcup_j\operatorname{supp}(\theta_l a_j)\). Then \(b=\sum_l b_l\) is locally finite. On each fixed compact set only finitely many \(l\) occur, so every remainder satisfies (G1) of order \(M_k=\max_{j\geq k}m_j\). The support assertion survives the locally finite sum. On a conic cover the cutoffs are homogeneous of degree zero above a fixed frequency; the bounded-frequency discrepancy is smooth and irrelevant to asymptotic orders. Differences of two sums are of every negative order. This also proves continuity of restrictions and the local form of the symbol recognition statement in AN03-EUC-002.

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

Here are the estimates behind this adapter. For fixed \(z\), apply AN03-GAU-008 with the metric
\(g_{(w,\eta)}(v,\nu)=\langle\eta\rangle^{2d}|v|^2+\langle\eta\rangle^{-2\rho}|\nu|^2\)
and weight \(\langle\eta\rangle^m\). Its slow variation and temperateness are exactly the parameter verification in AN03-EUC-004, with \(\delta\) there replaced by \(d\); its quadratic parameter is \(\frac12\langle\eta\rangle^{d-\rho}\). The theorem gives (G4) before restricting \(w=z\). Differentiate in \(z\) first, using the modified weight \(\langle\eta\rangle^{m+\delta|\beta|}\), and in \(w,\eta\) using their exact modified weights. Differentiation after the diagonal restriction is a sum of these derivatives. Since \(d\leq\delta\), each total base derivative costs at most \(\delta\). This proves all of (G1), including the remainder, rather than just a bound for values. Regularize \(c\) in all variables by cutoffs tending to one. Formula (G3) for the regularized kernels follows by Fourier inversion: the multiplier \(e^{i\omega\cdot\theta}\) becomes the kernel \((2\pi)^{-n}e^{-i(w-z)\cdot(\eta-\xi)}\). The Gauss bounds and distributional continuity identify the limits. They also justify all parameter derivatives. Thus no stationary phase theorem is hidden in (G3).

## AN03-GEO-002 — Kernels, exponential tests, and coordinate transport

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
The first identity follows by the Fourier translation rule on \(\mathcal S\), then on \(\mathcal S'\) by the continuous extensions in AN03-EUC-005. For the second, choose \(v\in\mathcal S\) with \(\widehat v\in C_c^\infty\) and \(v(0)=1\). The functions \(v(\varepsilon x)\) tend to one in \(\mathcal S'\): multiply a Schwartz test function by their bounded pointwise differences and use dominated convergence. The right side of the first identity is the integral of \(a(x,\xi+\varepsilon\theta)e^{i\varepsilon x\theta}\widehat v(\theta)\); every derivative converges on compact sets to \(a(x,\xi)\). This proves (G6) with its distributional meaning.

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

## AN03-GEO-003 — The second symbol term and the density it measures

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
Indeed AN03-EUC-005 applied to multiplication by \(J^z\) gives \(J^{-z}(aJ^z+\sum_j\partial_{\xi_j}a D_jJ^z)\) through the first correction; all higher frequency derivatives have order at most \(m-2\). The identity \(D_jJ^z=zJ^zD_jJ/J\) proves (G13). At \(z=\frac12\) it cancels (G12).

There is a version without homogeneity. For scalar half-density operators, the local quantity
\[
\sigma_{[2]}(A)=a+\frac i2\sum_j\partial_{x_j}\partial_{\xi_j}a
\pmod {S^{m-2}}
\tag{G14}
\]
agrees on overlaps as a scalar symbol class on \(T^*X\). Repeat the preceding calculation with \(a\) in place of \(a_m\): omitted terms contain at least two net frequency losses, so they are of order \(m-2\). A partition of unity patches the local quantities to a global symbol, and any two patches differ by \(S^{m-2}\) because they agree in each chart modulo that space. Its homogeneous term of degree \(m-1\), when present, is (G11). Formula (G12) also shows invariance for function operators at double zeros of \(a_m\), and under transformations with locally constant Jacobian. The refined assertion (G14) is specifically for scalar half-densities; a varying vector-bundle frame introduces its own first-order correction.

## AN03-GEO-004 — Assembling an operator and its principal symbol

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

The fiber-linear pullback proved in AN03-GEO-002 defines \(S^m(T^*X)\) independently of charts. Local principal symbols patch and give
\[
\Psi^m(X)/\Psi^{m-1}(X)
\simeq S^m(T^*X)/S^{m-1}(T^*X).
\tag{G16}
\]
For existence, take real compact smooth \(\theta_j\) subordinate to charts with \(\sum_j\theta_j^2=1\), and a cutoff \(\psi_j=1\) near \(\operatorname{supp}\theta_j\). Quantize a given cotangent symbol in each chart as \(A_j=\theta_j\operatorname{Op}(\psi_j a_j)\theta_j\), transporting back and extending by zero. The sum is locally finite and properly supported: over a fixed compact set only finitely many \(\operatorname{supp}\theta_j\) occur in either projection. Its principal symbol is \(\sum_j\theta_j^2a=a\). A square partition exists by dividing any nonnegative partition \(\chi_j\) by \((\sum_l\chi_l^2)^{1/2}\). On overlaps (G10) identifies principal classes. Their vanishing is equivalent in each local representation to order \(m-1\), proving the kernel of (G16) and injectivity. This also proves that \(\Psi^{-\infty}(X)\) is exactly the smooth-kernel class, by applying (G15) at every order and the integrability threshold of (G5).

## AN03-GEO-005 — Properness, products, and global summation

Write \(S=\operatorname{supp}K_A\subset X\times X\). The operator is **properly supported** if both projections \(S\to X\) are proper. For each compact \(K\subset X\), this says that there is a compact \(K'\) such that
\[
\operatorname{supp}u\subset K\ \Longrightarrow\ \operatorname{supp}Au\subset K',
\qquad
u=0\text{ near }K'\ \Longrightarrow\ Au=0\text{ near }K.
\tag{G17}
\]
The implications initially apply to test functions and then to the distributional extensions on their domains. Properness gives (G17) by the two kernel projections, enlarging the resulting compact sets to compact neighborhoods. Conversely, apply the support bounds to all test functions supported in a compact neighborhood of \(K\). If the kernel were nonzero outside the corresponding product set, its restriction to a small product of coordinate neighborhoods would pair nontrivially with some product of test functions, contradicting a support bound. Product test functions detect kernels by the scalar kernel theorem. Thus each projection has compact inverse images. This proves the equivalence, including the distinction between vanishing on a set and on a neighborhood used for distributions.

An arbitrary \(A\in\Psi^m\) extends continuously \(\mathcal E'(X)\to\mathcal D'(X)\): on each compact output set the local expression (G15) acts on compactly supported distributions by U010 and by pairing the smooth remainder. For a properly supported operator and arbitrary \(u\in\mathcal D'(X)\), define its output near a compact set \(K\) using \(A(\chi u)\), where \(\chi=1\) near the corresponding input compact set \(K'\). Formula (G17) proves independence of \(\chi\), and compatibility on overlapping output sets patches the result. Each output seminorm is controlled by finitely many input seminorms after this localization, proving continuity. Proper operators likewise map \(C^\infty\to C^\infty\), \(C_c^\infty\to C_c^\infty\), and \(\mathcal E'\to\mathcal E'\).

Every \(A\in\Psi^m\) is a properly supported operator plus a smooth-kernel operator. In the proof of (G15), retain only the intersecting partition pairs as an operator sum, now working intrinsically. The union of their compact kernel support rectangles has both projections proper, since each compact base set meets only finitely many partition supports and each such support has finitely many neighbors. The omitted terms are a locally finite smooth kernel. Equivalently this construction gives a smooth properly supported function on \(X\times X\), equal to one near the diagonal, by summing the retained products \(\theta_j(x)\theta_k(y)\). Multiplying any kernel by that function gives a common properness convention.

If \(A\in\Psi^m\) and \(B\in\Psi^{m'}\) are proper, then \(AB\in\Psi^{m+m'}\) is proper, and its principal symbol is \(\sigma_m(A)\sigma_{m'}(B)\), with the displayed order of factors. The relation \(S_A\circ S_B\) containing the product kernel support is closed and proper in both projections: above a compact output set the possible intermediate points lie in a compact set by properness of \(A\), and the possible input points then lie in a compact set by properness of \(B\). The same reasoning with the projections reversed proves the other direction, and these compactness statements prove closure by convergent subsequences.

For the local analytic assertion choose compact cutoffs \(\phi,\psi\) in a chart and \(\chi=1\) near both supports. Then
\(\phi AB\psi=(\phi A\chi)(\chi B\psi)+\phi A(1-\chi^2)B\psi\).
The first term is given by AN03-EUC-005. The second has a smooth kernel: properness confines its intermediate variable to a compact set, and the separated cutoffs make both factors smooth in the relevant external-variable neighborhoods. Differentiation under the compact integral, or action of a localized operator on a smooth kernel in one variable, proves every derivative. The same argument shows that smooth proper kernels form a two-sided ideal among proper pseudodifferential operators. It also covers products where the same support conditions make composition meaningful; we do not compose arbitrary nonproper operators on all distributions.

Finally let \(A_j\in\Psi^{m_j}(X)\), with \(m_j\) decreasing to \(-\infty\). There exists a proper \(A\in\Psi^{m_0}\) such that
\[
A-\sum_{j<k}A_j\in\Psi^{m_k}(X)\quad(k\geq0).
\tag{G18}
\]
First replace every \(A_j\) by a representative using the same proper kernel cutoff just constructed; this changes only smooth remainders. Choose a locally finite partition of a neighborhood of the diagonal by compact chart-product pieces. For each such piece, its localized kernel has a symbol of order \(m_j\) by (G3). Sum these symbols over \(j\) using AN03-GEO-001, then quantize and multiply by a cutoff equal to one near the corresponding diagonal piece. The difference introduced by that last cutoff is smooth. Summing the pieces gives (G18), since any compact product meets finitely many pieces and hence every remainder is a finite sum of symbols of order \(m_k\) and smooth kernels. Apply the common proper cutoff once more. It does not change any quotient by smoothing, proving properness and all remainder claims. This argument uses local finiteness, not a finite atlas or a uniform geometry assumption.

## AN03-GEO-006 — Inverses with global and conic error control

A scalar \(A\in\Psi^m(X)\) is elliptic when its principal class in (G16) has an inverse of order \(-m\). In coordinates this is equivalent to a lower bound
\[
|a(x,\xi)|\geq c_K\langle\xi\rangle^m
\quad(x\in K,\ |\xi|\geq R_K)
\tag{G19}
\]
on each compact set. For a square matrix symbol, use its smallest singular value, or equivalently \(\|a^{-1}\|\leq C_K\langle\xi\rangle^{-m}\). The reciprocal estimates of AN03-EUC-009 prove the implication from (G19) to an inverse class by taking local frequency cutoffs and patching. Conversely \(ab=1+r\), \(r\in S^{-1}\), gives \(|ab|\geq1/2\) above a compact-dependent radius and hence (G19). The same argument for square matrices uses the convergent finite-dimensional matrix Neumann series for \(I+r\).

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

We record the conic form of the calculus used here. If symbols \(a,b\) are prescribed on a cone and the usual composition is formed after extending them with cutoffs, its differential expansion is the usual one on every smaller cone; changes of extension have smoothing effects there. To prove it, choose a classical degree-zero cutoff \(q\) equal to one on the smaller cone, supported in the larger one, and a second cutoff equal to one near its support. In the oscillatory formula for composition, terms away from those supports have either separated base points, handled by frequency integration by parts, or separated frequency directions. In the latter case \(|\eta-\xi|\geq c(|\eta|+|\xi|)\); integration by parts in the intermediate base variable supplies arbitrarily many factors of this denominator, while its derivatives increase a symbol order by strictly less than one. Split into dyadic frequency shells to sum the resulting estimates. Derivatives of any fixed order are handled by performing more integrations. In the remaining region the global remainder theorem of U010 applies. This proves all differentiated conic estimates, including changes of cutoffs. It also shows that rapidly decreasing conic symbols form a two-sided microlocal ideal.

At a noncharacteristic point construct a local right inverse as follows. Choose \(b_0\), supported in the elliptic cone, equal there on a smaller cone to the reciprocal of \(a\), with a high-frequency cutoff. Extend \(r=1-a\circ b_0\), restricted to that smaller cone, to a global symbol of order \(-1\), using a further cone cutoff. The formal sum \(\sum b_0\circ r^{\circ j}\), made by local summation, gives an inverse modulo smoothing on a still smaller cone by (G20). The same construction on the left gives \(b_L\); the identity comparing the two inverses shows they agree modulo smoothing on their common cone. Proper quantization yields a single \(B\in\Psi^{-m}\) with both errors microlocally smoothing at the original point. Either such one-sided condition for a given \(B\) implies noncharacteristicity by the first remainder of the composition formula, hence implies the other condition by comparison with the inverse just constructed.

For \(1-\rho\leq\delta<\rho\), all constructions in this item hold with gain \(\varepsilon=\rho-\delta>0\), with \(S^{m-\varepsilon}\) in the principal quotient and \(S^{-\varepsilon}\) in the inverse-class condition. The coordinate error from AN03-GEO-002 has order at most \(m-(2\rho-1)\leq m-\varepsilon\), so these quotient symbols are intrinsic. Replace powers of order \(-j\) by order \(-j\varepsilon\) in (G20). At \(\delta=\rho\), closure and coordinate invariance survive; the zero gain does not furnish this principal quotient, conic inverse argument, or elliptic regularity assertion.

## AN03-GEO-007 — Fourier directions and the precise kernel relation

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

## AN03-GEO-008 — What every input can detect

For proper \(A\), and also for arbitrary \(A\in\Psi^m\) on compactly supported inputs,
\[
\operatorname{WF}(Au)\subset\operatorname{WF}(A)\cap\operatorname{WF}(u).
\tag{G24}
\]
We give a proof using cutoffs, so no unstated general kernel-composition theorem is needed. If a direction is absent from \(\operatorname{WF}(A)\), choose a classical conic cutoff \(Q\) supported in that regular symbol cone, elliptic at the point. Then \(QA\) is smoothing there, and by restricting the support of \(Q\) it is smoothing everywhere on the output neighborhood. The symbol estimates of AN03-GEO-006 prove this. If instead the direction is absent from \(\operatorname{WF}(u)\), choose compact spatial cutoffs and a smooth frequency cutoff \(q\), homogeneous above a ball and equal to one in a smaller cone, such that \(q(D)(\chi u)\) is smooth. Choose a proper \(Q\) equal to \(q(D)\chi\) near the point and a smaller conic cutoff \(P\). The full symbol of \(PA(I-Q)\) is smoothing by the separated-support estimates. Thus \(PAu=PAQu+PA(I-Q)u\) is smooth. Since \(P\) is a product of a spatial cutoff and an angular Fourier cutoff, this says directly that \(Au\) is Fourier-regular at the point. For an arbitrary distribution under a proper operator, (G17) reduces this argument to a compact input. For a global symbol and \(u\in\mathcal S'\), the separated spatial remainder \(\phi A(1-\chi)u\) is smooth: its kernel, after each output derivative, is Schwartz in the input variable, as repeated frequency integrations in (G5) show. This also proves global tempered pseudolocality and shrinkage of singular support.

The cutoff proof works for \(1-\rho\leq\delta\leq\rho\), including equality. One does not need an asymptotic expansion of two general equality-class symbols to separate a classical cutoff from a symbol. In \(a\circ q\) the differentiated terms gain \(\rho\) per paired derivative, since base derivatives of \(q\) cost zero; in \(q\circ a\) they gain \(1-\delta\). Both are positive. The same mixed-metric Gauss argument as AN03-EUC-004 proves the remainders with these respective gains. It follows, by inserting nested classical cutoffs, that the microsupport of a defined product satisfies
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

Localize both variables in compact coordinate sets. For a fixed input compact set \(K\), let \(E'_{K,N}\) be the Banach space of distributions supported in \(K\) with norm the dual norm of \(C^N\) test functions on a fixed compact neighborhood. The restricted map \(AQ:E'_{K,N}\to C^\infty\) has closed graph: convergence in that Banach norm implies distributional convergence, the original operator is continuous into distributions, and a smooth limit has the same distributional limit. The declared closed graph theorem therefore makes this map continuous. For input points in the interior of \(K\), the map \(y\mapsto\delta_y\) is \(C^r\) into \(E'_{K,N}\) when \(N\geq r+1\). Taylor's formula, with one extra uniformly bounded derivative on the unit ball of \(C^N\), proves this assertion and its difference-quotient derivatives. Consequently \((x,y)\mapsto (AQ\delta_y)(x)\) has every prescribed mixed derivative: choose \(r,N\) sufficiently large and use continuity into every output \(C^k\) seminorm. It is the kernel, since integration of \(\delta_y f(y)\) reproduces a test function and the operator is continuous. Hence that kernel is smooth.

Its symbol is therefore smoothing after compact localization. The conic cutoff calculus gives \(a\circ q-a\in S^{-\infty}\) near the selected covector, since \(q=1\) there to all orders. Thus \(a\) is smoothing there. This proves the converse and the minimality of \(\operatorname{WF}(A)\) among all sets allowed in (G24).

## AN03-GEO-009 — Elliptic tests and intrinsic wavefront

For every fixed real \(m\) and \(u\in\mathcal D'(X)\),
\[
\operatorname{WF}(u)=
\bigcap_{\substack{A\in\Psi^m(X)\ \mathrm{proper}\\Au\in C^\infty(X)}}
\operatorname{Char}_m(A).
\tag{G26}
\]
If a direction is Fourier-regular, choose an order-\(m\) conic symbol supported in a regular neighborhood and elliptic at the direction, for instance a degree-zero cutoff times \(\langle\xi\rangle^m\), with compact base support. Proper quantization and (G24) make \(Au\) smooth globally. Conversely, if \(Au\) is smooth and \(A\) is noncharacteristic at the direction, its conic inverse from AN03-GEO-006 gives
\(u=BAu+(I-BA)u\). The first term is smooth because \(B\) is proper, and the second is regular at the direction by (G24). This proves (G26) for the specified fixed order, not just for order zero.

Conjugating the test operators in (G26) by a diffeomorphism preserves properness, their order, their action on smooth functions, and their noncharacteristic set under the cotangent map, by AN03-GEO-002 and AN03-GEO-006. Distributions themselves pull back by the change-of-variables formula
\((\kappa^*u)(f|dx|)=u((f\circ\kappa^{-1})|\det(\kappa^{-1})'|\,|dz|)\);
it is continuous because composition and multiplication are continuous on compact test-function spaces. Thus (G26) proves that the Fourier definition transforms by the cotangent map. This establishes its intrinsic meaning on \(X\), and also that of (G23), without assuming a general pullback theorem for distributions with wavefront constraints. Smooth changes of bundle frame preserve it componentwise, by (G24) for multiplication and by the inverse frame transformation.

For a proper \(A\in\Psi^m\),
\[
\operatorname{WF}(u)\subset\operatorname{WF}(Au)\cup\operatorname{Char}_m(A).
\tag{G27}
\]
At a point outside the right side, choose a proper order-zero cutoff \(C\) elliptic there with \(CAu\) smooth, using (G26). The product \(CA\) is noncharacteristic there, and (G26) applied to it proves regularity of \(u\). Equivalently use its conic inverse. Together (G24) and (G27) say that a noncharacteristic operator neither creates nor removes a smoothness defect at that direction. The same proof applies in the strict coordinate-invariant \((\rho,\delta)\) range using the positive-gain conic inverse from AN03-GEO-006.

## AN03-GEO-010 — Convergence when singular directions are fixed

Let \(\Gamma\) be closed and conic off zero. Set \(\mathcal D'_\Gamma(X)=\{u:\operatorname{WF}(u)\subset\Gamma\}\). We use the following sequential convergence convention, the one specified in Hörmander I, Definition 8.2.2. In each chart, \(u_j\to u\) means weak distributional convergence and
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

We first isolate a uniformity fact. A weakly convergent sequence of distributions has, on each fixed compact input set, a common finite-order bound by uniform boundedness on the test-function Fréchet space. Moreover it converges uniformly on compact families of test functions in that space: cover the family by finitely many small neighborhoods in the controlling seminorm, and combine the common bound with convergence at the finitely many centers. In particular a fixed smooth proper kernel sends weakly convergent sequences to \(C^\infty\)-convergent sequences, since its differentiated input test functions over a compact output set form compact families.

Assume (G28) and fix an output compact set for \(A\). Properness restricts the input to a fixed compact set. Up to a smooth kernel, split the symbol into finitely many pieces whose angular/base supports have closures disjoint from \(\Gamma\); this is possible by compactness of the cosphere over the output compact set. Use a spatial cutoff \(\phi\) and a slightly larger good frequency cone for each piece. In the Fourier formula for its action on \(\phi(u_j-u)\), the part in that cone is bounded, after \(k\) output derivatives, by a constant times the seminorm (G28) with \(N>m+k+n+1\). It therefore tends to zero. The complementary frequency part has separated angular supports and is a smooth kernel after the conic integration-by-parts argument in AN03-GEO-006. The uniformity fact handles that part, as well as the initial smooth remainder. Finitely many such bounds prove every output \(C^k\) seminorm in (G29).

Conversely fix \(\phi,V\) in (G28). Enlarge its spatial support slightly and its angular cone slightly while remaining disjoint from \(\Gamma\); if necessary a finite partition in the spatial variable achieves such an enlargement. Choose \(\chi=1\) near the enlarged spatial support and a classical angular cutoff \(q=1\) near \(V\), supported in the enlarged cone above frequency one. Make \(A=\chi q(D)\phi\) proper by the common near-diagonal kernel cutoff. Its microsupport avoids \(\Gamma\), so (G29) gives convergence of its compactly supported outputs in every smooth norm. The properness correction is a smooth kernel on the fixed input support and tends to zero in the same norms. Thus \(\chi q(D)\phi(u_j-u)\to0\) in \(C_c^\infty\). The omitted output tail \((1-\chi)q(D)\phi(u_j-u)\) has a Schwartz kernel in the output variable and compact support in the input variable: repeated frequency integration by parts gives arbitrary spatial decay, uniformly with derivatives and input derivatives, because the two spatial supports are separated. The uniformity fact therefore makes this tail tend to zero in \(\mathcal S\). We conclude \(q(D)\phi(u_j-u)\to0\) in \(\mathcal S\). Taking its Fourier transform and restricting to \(V\) above frequency one gives (G28). Bounded frequencies were already controlled by weak convergence. This proves the equivalence and, by its intrinsic operator formulation, its coordinate independence.

One may replace convergence in (G28) by uniform boundedness of those seminorms for all \(N\), retaining weak distributional convergence. To see this, control a desired order \(N\) tail by the uniform order-\(N+1\) bound divided by the frequency radius; on a bounded frequency set use uniform convergence. This is a statement about the entire sequence, including its limit, and does not weaken the requirement that every \(u_j\) and \(u\) lie in \(\mathcal D'_\Gamma\).

## AN03-GEO-011 — Sobolev and Besov spaces in a moving chart

Let \(\mathcal B^s_p=B^s_{2,p}\), \(1\leq p\leq\infty\), be the dyadic Hilbert-based Besov space of AN03-EUC-008. Explicitly, with sharp annular Fourier projections \(\Pi_j\),
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

Choose integers \(k_-<s<k_+\). The annular two-endpoint argument (E39) of AN03-EUC-008, with order shift zero, now yields
\[
T:\mathcal B^s_p\longrightarrow\mathcal B^s_p
\quad\text{continuously},\qquad1\leq p\leq\infty.
\tag{G31}
\]
Its proof uses a summable convolution sequence in the dyadic indices and consistency of \(T\) on the two Sobolev endpoints. Distributional pullback supplies that consistency. At \(p=\infty\) the input annular sums are taken in the lower Sobolev space, not incorrectly asserted to converge in the Besov norm. Applying (G31) to the inverse diffeomorphism proves equivalence of chart norms. Thus this argument also proves real-order Sobolev coordinate invariance, without importing it as an extra theorem.

Define \(\mathcal B^{s,\mathrm{loc}}_p(X)\) by requiring every compact coordinate cutoff of a distribution, expressed in that chart and extended by zero, to have finite norm (G30). Its topology consists of those seminorms. Define \(\mathcal B^{s,\mathrm{comp}}_p(X)\) by adding compact support, with the inductive-limit topology over compact supports. Formula (G31), multiplication boundedness from U010, and finite partitions on each compact set show independence of coordinates and cutoff families. The same definitions apply to finitely many components of a vector bundle; changing frame multiplies by a smooth invertible matrix, bounded on every compact set together with its derivatives, and hence preserves these local spaces. No globally chosen bundle norm or volume form is required.

If \(A\in\Psi^m\) is proper, then
\[
A:\mathcal B^{s,\mathrm{loc}}_p(X)\to\mathcal B^{s-m,\mathrm{loc}}_p(X),
\qquad
A:\mathcal B^{s,\mathrm{comp}}_p(X)\to\mathcal B^{s-m,\mathrm{comp}}_p(X)
\tag{G32}
\]
continuously. Fix an output compact set and use properness to choose an input cutoff. A finite chart partition and (G15) express the localized map as finitely many global symbols of order \(m\), plus a compactly localized smooth kernel. U010 proves the desired bound for each symbol. A compact smooth kernel maps any fixed lower Sobolev space into any higher one: its Fourier transform decreases rapidly in both variables, and Cauchy–Schwarz with weights proves this bound. Applying the same dyadic endpoint argument proves its Besov bound. This handles every summand and every local output seminorm. Properness also bounds output support on each fixed input support, which proves the compact-space continuity. Without properness, the same proof gives the meaningful map \(\mathcal B^{s,\mathrm{comp}}_p\to\mathcal B^{s-m,\mathrm{loc}}_p\), and a local symbol on \(U\) maps \(\mathcal S'(\mathbb R^n)\to\mathcal D'(U)\), as follows by multiplying each output by a compact cutoff and using U010.

For proper elliptic \(A\), its parametrix gives the converse regularity implication in (G32). For example if \(u\in\mathcal D'(X)\) and \(Au\in\mathcal B^{s-m,\mathrm{loc}}_p\), write \(u=BAu+Ru\) with \(R\) a smooth proper kernel. The first term belongs to \(\mathcal B^{s,\mathrm{loc}}_p\) by (G32), and the second is smooth. If the input \(u\) is already compactly supported, this gives the corresponding compact-space regularity assertion. It does not infer compact support of \(u\) from compact support of \(Au\). For Sobolev spaces, one can equivalently test \(H^{s,\mathrm{loc}}\) by a proper elliptic operator of order \(s\) mapping to \(L^2_{\mathrm{loc}}\). Existence follows by quantizing a positive cotangent weight of order \(s\), constructed in charts and patched; any such operator gives the equivalence by (G32) and its parametrix. With general coordinate-invariant parameters (G32) is valid through equality, while its elliptic converse uses \(\delta<\rho\).

## AN03-GEO-012 — Microlocal scales and their unattained thresholds

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
\(\sum_j|a_j(x,\xi)|^2\geq c>0\) in a neighborhood of that cosphere, above a common radius: shrink finitely many neighborhoods and use compactness once more. Choose proper order-zero \(C_j\) with principal symbol \(\overline{a_j}\), and set \(P=\sum_j C_jA_j\). Then \(Pu\in\mathcal B^{s,\mathrm{loc}}_p\) and \(P\) is elliptic over a neighborhood of \(x_0\). Its conic inverse can be chosen uniformly over that compact cosphere, or constructed from a local reciprocal there by AN03-GEO-006. Thus \(BP-I\) is smoothing over that whole spatial neighborhood. Multiplying by a smaller spatial cutoff yields local regularity of \(u\). The reverse implication follows at once from the definition. No summation over infinitely many directions, nor reflexivity of the Besov space, occurs.

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
The equality follows by applying the inverse regularity implication at every real order; subtraction of a finite \(m\) from \(+\infty\) is interpreted as \(+\infty\). Identical definitions and proofs give thresholds for each fixed Besov exponent \(p\), but equality of thresholds never identifies endpoint membership for different \(p\). Equations (G30)–(G37) supply the microlocal continuation of the global and local-cutoff Besov assertions established in U010.

## AN03-GEO-013 — Bundles, anti-duals, and kernels between different manifolds

Let \(E,F\to X\) be smooth complex vector bundles of finite ranks \(e,f\), which need not be equal. An operator \(A\in\Psi^m(X;E,F)\) is represented in local frames by an \(f\times e\) matrix of operators in \(\Psi^m\), with smooth kernel off the diagonal. A new pair of frames changes that matrix by \(G_F A G_E^{-1}\); multiplication by these smooth matrix functions and AN03-EUC-005 preserve its class. Coordinate changes are handled by AN03-GEO-002 componentwise. Its principal symbol therefore is a section class
\[
\sigma_m(A)\in
S^m(T^*X;\operatorname{Hom}(\pi^*E,\pi^*F))
\big/S^{m-1}(T^*X;\operatorname{Hom}(\pi^*E,\pi^*F)).
\tag{G38}
\]
The leading transformation is \(a\mapsto G_FaG_E^{-1}\), since differentiated transition matrices occur only in lower orders. The construction proving (G16), performed in local frames, proves surjectivity onto these symbol classes and identifies the lower-order kernel. Matrix products keep their order, so \(\sigma(BA)=\sigma(B)\sigma(A)\) for compatible bundles. Properness, summation, (G32), and (G34) all apply componentwise and patch by local finiteness. Two-sided ellipticity means that (G38) is fiberwise invertible; that condition forces equal ranks, but it was not imposed on the definition, mapping, composition, or adjoint theorems. The same constructions define \(\Psi^m_{\rho,\delta}(X;E,F)\) in the entire coordinate-invariant range, with the positive-gain principal quotient as described in AN03-GEO-006 when \(\delta<\rho\).

Half-densities provide an intrinsic pairing. For scalar half-densities \(u,v\) with compact overlap of supports, set \((u,v)=\int_Xu\overline v\); the product is a density, so change of variables makes the integral independent of coordinates and of orientation. Every scalar \(A\in\Psi^m(X;\Omega^{1/2},\Omega^{1/2})\) has an adjoint \(A^*\) in the same class satisfying
\[
(Au,v)=(u,A^*v),\qquad u,v\in C_c^\infty(X;\Omega^{1/2}).
\tag{G39}
\]
Its kernel is \(\overline{K_A(y,x)}\), with the half-density factors interchanged. Locally U010 gives the adjoint symbol
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
To prove the adapter, trivialize both bundles and density lines on relatively compact charts. Each component of (G42) is a continuous scalar test-to-distribution map and has a unique scalar kernel by AN03-DEP-GEO-DIST. Under new frames that kernel is multiplied by \(G_F(y)\) on the left and \(G_E(x)^{-1}\) on the right. Under new coordinates the scalar kernel density factor in the input variable combines with the two half-density component laws to give one half-density in each variable. These are exactly the transition functions of (G43), since \(\Omega_{Y\times X}^{1/2}\simeq\Omega_Y^{1/2}\boxtimes\Omega_X^{1/2}\). Uniqueness of the scalar kernel makes the local distributions agree, so they glue to one global kernel.

Conversely take a kernel as in (G43). Pair its input half-density factor with the input half-density and its \(\operatorname{Hom}\) factor with the input section; this leaves a distributional target half-density. More concretely, to pair the result with a compact target dual test section, localize the product of the two compact supports into finitely many chart products and use the scalar kernel pairing there. The transformation rules prove independence of the localization. The scalar kernel theorem supplies continuity on each test-function support space, and the inductive-limit definition of \(C_c^\infty\) supplies global continuity. The two constructions are inverse because they agree on all pairs of scalar test functions in every chart. For topology, this is the same kernel identification with continuous bilinear test pairings as the declared scalar theorem, transported by finite local matrices and locally finite gluing; we do not replace it by an unspecified operator-norm topology. Thus the proof closes the geometric and bundle content of (G42)–(G43), while the scalar kernel theorem remains its explicit foundation.

## AN03-GEO-EX-001 — Four calculations that separate the assertions

**A density correction in one dimension.** Work on \(x>0\) with \(z=\log x\) and \(A=D_x\). On functions, (G7) gives \(A_\kappa=e^{-z}D_z\). Its leading symbol is \(e^{-z}\eta\), so its subprincipal symbol is \(-\frac i2e^{-z}\). Here \(J=x^{-1}\), and (G12) gives the same value: \(-\frac12D_x\log J=-\frac i{2x}\). On half-densities, (G13) adds \(+\frac i{2x}\), giving
\(A^{(1/2)}_\kappa=e^{-z}D_z+\frac i2e^{-z}\).
Its subprincipal symbol is zero, agreeing with \(D_x\). These calculations can be localized by compact cutoffs equal to one on the interval under discussion.

**One smoothing kernel, two support failures.** On \(\mathbb R\), the smooth kernel \(K(x,y)=1\) sends a compact distribution \(u\) to the constant \(u(1)\). It is smoothing and belongs locally to every \(\Psi^m\), but neither kernel projection is proper. It does not send general distributions to distributions by this integral formula: the proposed value on the constant input one would require integrating over the whole line. Multiplying the kernel by a compact smooth function of \(x-y\) makes it proper and still smooth; its integral then acts on every distribution. This distinguishes smoothness from support control without confusing either with symbol order.

**The same threshold, different endpoint membership.** For the point mass \(\delta_0\) in \(\mathbb R^n\), \(\widehat{\delta_0}=1\) and \(\|\Pi_j\delta_0\|_2\asymp2^{jn/2}\) for \(j\geq1\). Consequently \(\delta_0\in H^s\) exactly when \(s<-n/2\), while \(\delta_0\in B^{-n/2}_{2,\infty}\) and \(\delta_0\notin B^{-n/2}_{2,p}\) for finite \(p\). Each nonzero direction at the origin has Sobolev threshold \(-n/2\), because restricting the constant Fourier transform to any cone of positive angle gives the same divergence. The thresholds in (G36) coincide, and the endpoint still has to be checked separately. This is a standard diagnostic example.

**A characteristic operator can improve the threshold.** Let \(u=\delta_0(x_1)\otimes f(x')\) in a coordinate product, with smooth nonzero \(f\). Multiplication by \(x_1\) is an order-zero proper operator and sends \(u\) to zero. It is characteristic over \(x_1=0\), so the strict improvement from finite input regularity to smooth output is consistent with (G37). In contrast an elliptic order-zero matrix acting between equal-rank bundles preserves the threshold at every point of its elliptic set, regardless of the local frame.

## AN03-GEO-PS-001 — Exercises with complete solutions

**1. A complex density cocycle.** Let three charts have positive transition Jacobians \(J_{12},J_{23}\). For \(z=\frac12+i\tau\), verify the density transition law on a triple overlap. Determine the modulus of a local transition factor and explain why a complex logarithm branch is unnecessary.

**Solution.** The chain rule gives \(J_{13}=J_{23}J_{12}\), with the factors evaluated at the appropriate common point. All numbers are positive, so \(\log J_{13}=\log J_{23}+\log J_{12}\) in the real logarithm. Exponentiating after multiplication by \(-z\) gives \(J_{13}^{-z}=J_{23}^{-z}J_{12}^{-z}\), exactly the component cocycle. Its modulus is \(J_{13}^{-1/2}\), because \(|e^{-i\tau\log J_{13}}|=1\). The positivity supplied by the absolute Jacobian makes the real logarithm single valued even on orientation-reversing overlaps.

**2. Proper representatives need not preserve an exact operator.** For the kernel \(K(x,y)=1\) on \(\mathbb R\), choose \(h\in C_c^\infty(\mathbb R)\), equal to one near zero, and replace \(K\) by \(h(x-y)K\). Prove properness and identify the exact type of error. Does this authorize replacing the original operator on a fixed compact input without recording an error?

**Solution.** If \(\operatorname{supp}h\subset[-R,R]\), the new kernel support satisfies \(|x-y|\leq R\). Above a compact set in either variable, the other variable lies in its closed \(R\)-neighborhood, which is compact. Thus both projections are proper. The difference kernel \(1-h(x-y)\) is smooth, so the error is smoothing, but is generally nonzero. For a smooth input of nonzero integral supported far from a chosen output point, the proper replacement vanishes there while the original output is its nonzero integral. Hence the replacement is an identity modulo smoothing, not an exact operator identity.

**3. Recover the endpoint obstruction with a logarithmic sequence.** Let \(v_j\) be \(L^2\) Fourier functions on disjoint dyadic annuli with \(\|v_j\|_2=2^{-js_0}(1+j)^{-\beta}\), and let \(u\) be the tempered distribution with Fourier transform \(\sum_{j\geq1}v_j\). Determine its global \(B^{s_0}_{2,p}\) membership and its supremum of global Sobolev orders.

**Solution.** Polynomial growth of the annular \(L^2\) norms makes the sum a tempered distribution: pairing each annulus with a Schwartz function and applying Cauchy–Schwarz yields a summable geometric majorant. With the sharp annular projections in (G30), its order-\(s_0\) Besov sequence is \((2\pi)^{-n/2}(1+j)^{-\beta}\), by Plancherel in the stated Fourier convention. For finite \(p\), membership holds exactly when \(\beta p>1\); for \(p=\infty\), exactly when \(\beta\geq0\). The squared \(H^s\) norm is comparable to the sum of \(2^{2j(s-s_0)}(1+j)^{-2\beta}\), by disjoint Fourier supports and comparability of \(\langle\xi\rangle\) with \(2^j\) on each annulus. This series is summable for every \(s<s_0\), and not summable for any \(s>s_0\), since its terms then fail to tend to zero. Thus the supremum is \(s_0\) for every real \(\beta\), while endpoint Hilbert membership holds precisely when \(\beta>1/2\). This is a global calculation and makes no unsupported claim about the spatial location of its wavefront.

**4. Why a compact output does not imply a compact input.** Give a proper elliptic operator on a noncompact manifold and a noncompactly supported smooth input whose output is compactly supported. Locate the hypothesis that prevents this from contradicting the compact-space converse in (G32).

**Solution.** On \(\mathbb R\), take \(A=D_x\), a proper elliptic differential operator of order one, and \(u=1\). Its output is zero, whose support is empty and hence compact, while \(u\) has support all of \(\mathbb R\). The converse in (G32) asserts input regularity from output regularity; its compact-space version assumes at the outset that the input distribution has compact support. A parametrix leaves a smooth remainder, which can carry a noncompact smooth solution such as this one.

**5. An unequal-rank symbol.** Let \(E\) and \(F\) have local ranks two and three, and let a principal symbol be \(a(x,\xi)=\langle\xi\rangle^m\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}\). Compute the symbol of the half-density adjoint and explain which statements of AN03-GEO-013 apply without modification, and which two-sided assertion cannot hold.

**Solution.** In dual frames the adjoint symbol is \(\langle\xi\rangle^m\begin{pmatrix}1&0&0\\0&1&0\end{pmatrix}\), since the order \(m\) is real and the displayed matrix has real entries. The local class, its patching law, Sobolev/Besov mapping, proper-support extension, compatible composition, and the adjoint theorem all allow these ranks. Multiplying the adjoint symbol by the original gives \(\langle\xi\rangle^{2m}I_2\), whereas the reverse product is \(\langle\xi\rangle^{2m}\operatorname{diag}(1,1,0)\). Thus there cannot be a two-sided inverse from a three-dimensional fiber to a two-dimensional fiber. The failure is finite-dimensional algebra, not a regularity defect.

**6. The boundary of coordinate invariance.** For a symbol \(a(\xi)\in S^0_{\rho,0}\), consider \(b(x,\xi)=a(M(x)\xi)\) with smooth invertible nonconstant \(M\). Derive the order cost of one base derivative. Then classify \((\rho,\delta)=(2/5,1/5),(3/4,1/4),(1/2,1/2)\) with respect to the coordinate theorem and the inverse construction in this unit.

**Solution.** The chain rule gives \(\partial_{x_j}b=\sum_k(\partial_{\xi_k}a)(M(x)\xi)(\partial_{x_j}M(x)\xi)_k\). On a compact base set, the first factor costs \(-\rho\) and the second costs one, so the bound is of order \(1-\rho\). This estimate is the reason for the requirement \(\delta\geq1-\rho\); the calculation is not by itself an assertion that every particular symbol fails below that bound. For \((2/5,1/5)\), this condition fails because \(1/5<3/5\), so the general coordinate theorem does not apply, even though the Euclidean symbol class is defined. For \((3/4,1/4)\), both \(1-\rho\leq\delta\leq\rho\) and \(\delta<\rho\) hold, giving coordinate invariance and an inverse gain \(\rho-\delta=1/2\). For \((1/2,1/2)\), coordinate invariance holds through the amplitude estimate, but the inverse gain is zero. No decreasing-order parametrix construction follows there.

The proofs suggest two further research directions. Quantizing bundle-valued principal symbols with extra geometric structure requires tracking the frame correction omitted by the scalar half-density refinement. Studying propagation beyond elliptic directions requires information about the characteristic symbol that is absent from the inequality (G27). Those are separate problems; neither is inferred from elliptic inversion alone.

Mathematical antecedents include Hörmander, *The Analysis of Linear Partial Differential Operators III*, §18.1, and Volume I, §8.2. The coordinate amplitude construction is the Kuranishi change of phase variables discussed in [Grubb's author-hosted Chapter 8](https://web.math.ku.dk/~grubb/dist8n.pdf); the separate roles of operator microsupport and manifold assembly can also be compared in [Melrose's microlocalization chapter](https://math.mit.edu/~rbm/iml/Chapter5.pdf) and [manifold chapter](https://math.mit.edu/~rbm/iml/Chapter6.pdf). These are comparison readings. The present proofs, organization, examples, and solutions are independently written; no expression from those readings is imported under the course license, and no claim of novelty is made for standard mathematical constructions.
