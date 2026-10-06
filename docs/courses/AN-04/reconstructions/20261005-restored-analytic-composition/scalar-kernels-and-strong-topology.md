# Scalar kernels and strong distribution topology

This companion retains the complete scalar kernel proof, Sections 13.1–13.6, equations GK1–GK26, and the bundle adapter G42–G43 from AN03-U012, *Detecting regularity without choosing coordinates*, in *Elliptic Operators & Boundary Problems: Renewed 2026 Course Draft*. Both imported mathematical blocks are unchanged. Entry E0 supplies the compact exhaustion referred to in Section 13.1. Entry E1 makes the compact-distribution strong topology and its smooth approximation explicit. Entry E2 gives the same topology conventions on manifolds.

Original principal author and publisher: AN-03 course-writing task / AN-03 local course project. Copyright © 2026 AN-03 course project contributors. Earlier modification: AN-03 course-writing task and OpenAI Codex. This selection, exact prerequisite bindings and added entries: GPT-6 Astra (OpenAI), Ultra, 5 October 2026; publisher: AN-04 local course project.

Permission is granted to copy, distribute and modify this component under the GNU Free Documentation License, Version 1.2 only, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The [licence](notices/COPYING), [title page](notices/TITLE_PAGE.md), [history](notices/HISTORY.md) and [rights notice](notices/RIGHTS.md) accompany it. Its combined text retains that licence.

The earlier programme proofs used here are:

- [Complete fixed-support test spaces](../20261004-free-tangent-zoom/prerequisites/complete-test-spaces.md): Section 14.1 proves the countable-seminorm metric, Section 14.2 proves completeness of the exact spaces used below, and Sections 6 and 19 prove Baire's theorem with its declared logical inputs. These are the particular Banach-foundation sections named in the retained text.
- [Finite calculus and compactness](../20261004-free-stationary-phase/prerequisite-completions.md), [exponential and trigonometric series, P13–P16](../20261004-free-stationary-phase/exponential-prerequisite-completions.md), and compact parameter integration and Fourier bounds. P16 proves the periods and trigonometric identities used in the Fejér calculation; the Fourier expansion below is proved here.
- [Compact bumps and densities, Appendix A.4–A.6](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md), [product integration, M4](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md), and [base exhaustion and partitions, PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md).

The [proof map](proof-map.json) binds the precise dependencies. For primary-source comparison, the approved purchased reprint of Hörmander I, second edition (1990), Sections 5.1–5.2 was read. The retained programme proof constructs its kernel by periodic Fourier series and includes a full Baire argument and strong-dual estimates; the book's existence proof uses regularized kernels and a parameter Taylor argument. The book is cited as a mathematical source and comparison, and none of its text is included.

## E0. Compact exhaustion and the topology conventions

For a nonempty proper open set \(U\subset\mathbb R^p\), put \(d(x)=\operatorname{dist}(x,\mathbb R^p\setminus U)\). The triangle inequality, followed by taking the infimum over the nonempty complement, gives \(|d(x)-d(y)|\leq|x-y|\). The infimum exists because these distances are bounded below. For positive integers \(j\), set \(K_j=\{x:|x|\leq j,\ d(x)\geq1/j\}\). This is closed and bounded, hence compact, and lies in \(U\). Both inequalities become strict for \(j+1\) at every point of \(K_j\), so \(K_j\subset\operatorname{int}K_{j+1}\). Every point of \(U\) has positive distance from the complement and lies in one of these interiors. Their nested interiors cover each compact subset by a finite subcover. If \(U=\mathbb R^p\), take the closed balls of radius \(j\); if \(U\) is empty all spaces are zero. This also covers dimension zero with its one-point topology.

A locally convex topology is specified here by its continuous seminorms. A set is bounded when each such seminorm has finite supremum on it. A linear map between two such spaces is continuous exactly when each target seminorm is bounded by a constant times a finite maximum of source seminorms: continuity gives a basic neighborhood on which the target seminorm is less than one; rescaling gives the inequality, and arbitrary rescaling handles a zero maximum. The converse follows directly from that inequality. Thus a continuous linear map carries bounded sets to bounded sets. These elementary facts justify every use of that implication below.

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

## E1. Compact distributions, strong approximation and bounded smooth families

Give \(C^\infty(U)\) the seminorms \(p_{K,N}(f)=\max_{|\alpha|\leq N}\sup_K|\partial^\alpha f|\), over compact subsets \(K\subset U\). A continuous linear functional on this space satisfies a finite-order estimate on one compact: take a finite union of the compacts in the continuity estimate and the largest derivative order. It therefore vanishes on tests supported outside that compact and restricts to a compactly supported distribution. Conversely Section 13.6, equation (GK24), extends every compactly supported distribution to a continuous functional on \(C^\infty(U)\), independently of its cutoff. Thus these spaces are exactly dual; write the dual as \(\mathcal E'(U)\).

The strong topology on \(\mathcal E'(U)\) has seminorms \(q_B(u)=\sup_{f\in B}|u(f)|\), where \(B\) is bounded in \(C^\infty(U)\). Such a set has uniformly bounded derivatives of each fixed order on each compact, by the definition of boundedness and the seminorm comparison in E0. The inclusion \(\mathcal E'\to\mathcal D'\) is continuous: a bounded test set has a common compact support and bounded derivatives by (GK2), hence is a bounded subset of \(C^\infty\), and its strong-dual seminorm is one of the \(q_B\).

Here is the smooth approximation with all uniform bounds. First let \(u\) be supported in a compact \(K\subset\mathbb R^p\). Choose \(r\in C_c^\infty(\mathbb R^p)\) with \(\int r=1\), obtained by normalizing a nonnegative bump. For \(0<\varepsilon\leq1\) put \(r_\varepsilon(x)=\varepsilon^{-p}r(x/\varepsilon)\) and \(u_\varepsilon(x)=u_y(r_\varepsilon(x-y))\). This is smooth: on every compact parameter set, the finite-order estimate for \(u\), applied to the Taylor remainder in \(x\), permits every derivative to pass under the pairing. Its support is contained in \(K+\varepsilon\operatorname{supp}r\), since the paired function vanishes near \(K\) outside that sum. All these supports lie in one compact set.

For \(f\in C^\infty(\mathbb R^p)\), a cutoff in the common compact support and the iterated pairing (GK25) give \(u_\varepsilon(f)=u_y(\int r(z)f(y+\varepsilon z)\,dz)\). The substitution has used both the factor \(\varepsilon^{-p}\) and its Jacobian. The segment fundamental theorem gives, for each multi-index \(\alpha\),
\[
\sup_{y\in L}\left|\partial_y^\alpha\int r(z)
 [f(y+\varepsilon z)-f(y)]\,dz\right|
\leq \varepsilon\sum_{j=1}^p\left(\int|r(z)|\,|z_j|\,dz\right)
\sup_{y\in L+[0,1]\operatorname{supp}r}
 |\partial^{\alpha+e_j}f(y)|.
\tag{KE1}
\]
Here \(L\) is a fixed compact neighborhood used in the finite-order bound for \(u\), and \([0,1]\operatorname{supp}r=\{tz:0\leq t\leq1,z\in\operatorname{supp}r\}\). Apply that bound, including the derivatives of its cutoff, to (KE1). For a bounded smooth family \(B\), every derivative on the right is uniformly bounded on the displayed compact. It follows that \(q_B(u_\varepsilon-u)\leq C_B\varepsilon\to0\). Thus compact smooth functions are dense in \(\mathcal E'\) for its strong topology, with a common compact support for each approximated distribution. In dimension zero this is the identity approximation.

The same finite-order estimate gives a common polynomial Fourier bound. The exact pairing and substitution above yield \(\widehat u_\varepsilon(\eta)=\widehat u(\eta)\widehat r(\varepsilon\eta)\); since \(|\widehat r|\leq\int|r|\), the polynomial exponent and bound for \(\widehat u\) also bound all the approximants. The factors \(\widehat r(\varepsilon\eta)\) tend to one for each \(\eta\), by compact parameter integration. This supplies the approximation used in the kernel Fourier formula.

For a compactly supported distribution in a general open set, choose finitely many relatively compact coordinate boxes and a smooth partition equal to one near its support. Each localized piece has positive distance from its chart boundary. Apply the preceding construction there with sufficiently small \(\varepsilon\), extend by zero and sum. The supports stay in one compact subset of the original open set. The finite product and coordinate-derivative rules carry each bounded smooth family to a bounded family on the finitely many chart compacts; hence the same strong convergence holds. This also proves the statement for finite-rank bundle-valued distributions and half-densities on a manifold, using the local frames described in E2.

Finally let \(T\) be a continuous linear map between the smooth or test spaces just defined, with transpose \(T^t\) on the appropriate duals. For every bounded set \(B\) in the domain of \(T\), E0 makes \(T(B)\) bounded and the exact identity \(q_B(T^tu)=q_{T(B)}(u)\) proves strong-dual continuity. Proper support is what supplies a common compact support when \(T(B)\) must be a bounded test family, rather than merely a bounded smooth family. This proves the transposition assertion without a separate functional-analytic extension theorem.

## E2. Manifold topologies and the finite bundle adapter

On a Hausdorff second-countable smooth manifold, use the precompact base exhaustion and locally finite chart partitions constructed in PS5. For one fixed compact support, finitely many coordinate charts and bundle frames give the derivative seminorms; transition matrices and coordinate maps, with all needed derivatives, are bounded on the corresponding compact overlaps. The finite chain and product rules prove continuity of these changes and the equivalence of the resulting fixed-support topologies. Define the global test topology as the finest locally convex topology of their compact-support union, exactly as in Section 13.1, and the smooth topology by the compact derivative seminorms.

The bounded-support proof of (GK3) works on this exhaustion as well. If a test family escapes every compact, select a nonzero component at a point escaping the \(j\)-th compact, in one local frame at that point. Weighted component evaluation defines a seminorm: on each fixed compact only finitely many of these evaluations remain, and each is continuous there. Choosing the weights to make the \(j\)-th selected value at least \(j\) contradicts boundedness. Once supports are in one compact, finitely many chart seminorms give exactly (GK2). Conversely their boundedness implies boundedness in the fixed-support space and then in the global test space. The same finite-chart construction proves the compact-support characterization of the dual of \(C^\infty\) and the strong-seminorm assertions of E1.

The following original adapter now applies with these specified topologies. Its uniqueness and finite local estimates give a global distribution on the product manifold; independence of each finite partition follows by the common refinement argument of Section 13.5.

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
