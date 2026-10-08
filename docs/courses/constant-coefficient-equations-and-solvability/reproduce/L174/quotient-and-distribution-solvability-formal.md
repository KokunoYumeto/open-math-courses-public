# Solving convolution equations for arbitrary distribution data

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Singular-support confinement can solve an equation modulo smooth functions even when the full kernel cannot be sampled on the unknown domain. To obtain the full result, we construct a proper local adjoint and prove its estimates on two separate exhaustions. A smooth correction then gives ordinary distributional solutions. We also distinguish arbitrary data from data of one fixed finite order, for which a global extension modulo smooth functions is available.

Basic references are [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's differential-analysis course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. Convolution modulo smooth functions and compact singularity bounds, Lemma 1.1 and Theorem 1.2, constructs compactly supported partitions and the canonical quotient operation. Its Theorems 2.1 and 4.1 prove invertibility and singularity confinement are necessary for quotient surjectivity. Recovering singularities from convolution profiles, Corollary 6.1 including its empty-image case, proves that an invertible compact kernel cannot smooth a nonsmooth compact input.

The same-domain polynomial exhaustion method is written in Singular supports and arbitrary distribution data, Lemmas 4.1–5.1 and Theorem 5.2. We prove the nonlocal, two-domain version here. Countable test families, compact smooth subsequences and complex seminorm Hahn–Banach are proved in Continuous functionals, test families and compact limits, Sections 1–3. The Fréchet closed graph theorem is Section 14.5 of Banach estimates, quotient spaces and compact parameter arguments. Finally, Fréchet duality and smooth convolution solvability, Theorem 8.1, proves the exact smooth-forcing equivalence used for our final corrections.

## 1. A global finite-order representative

Work in \(\mathbb R^n\), \(n\ge1\), and let \(m\) be a nonnegative integer. Write \(\mathcal D^{\prime m}(X)\) for the distributions having order at most \(m\) on every compact subset of \(X\), with constants allowed to depend on that compact set. The same \(m\) must work throughout \(X\). Put
\[
 p_r(\varphi)=\max_{|\alpha|\le r}
                 \sup_{\mathbb R^n}|D^\alpha\varphi|.
 \tag{1.1}
\]
These are global suprema for compactly supported smooth tests; their values are finite.

**Lemma 1.1 (one-derivative global extension modulo smooth functions).** If \(f\in\mathcal D^{\prime m}(X)\), there is \(g\in\mathcal D^{\prime\,m+1}(\mathbb R^n)\) such that \(f-g|_X\) is smooth.

*Proof.* Choose a countable locally finite smooth partition \(\sum_j\chi_j=1\) on \(X\), with each support \(L_j\Subset X\), as constructed in the linked quotient-convolution lemma. Omit identically zero partition members. The compact distributions \(f_j=\chi_j f\), extended globally, obey
\[
 |f_j(\varphi)|\le A_jp_m(\varphi)
              \quad(\varphi\in\mathcal D(\mathbb R^n)).
 \tag{1.2}
\]
Indeed apply the order-\(m\) bound for \(f\) on a compact neighborhood of \(L_j\) to \(\chi_j\varphi\), and use the finite Leibniz formula. The constants \(A_j\) may grow arbitrarily.

Choose a nonnegative even smooth bump \(\rho\), supported in the unit ball, with integral one, using the explicit bump construction and positive normalization in that same lemma. Set \(\rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon)\). For every \(|\alpha|\le m\), the line-segment mean-value formula gives
\[
 \sup|D^\alpha(\varphi-\rho_\varepsilon*\varphi)|
 \le\sqrt n\,\varepsilon\,p_{m+1}(\varphi).
 \tag{1.3}
\]
To see the constant, write the difference as the integral of
\(D^\alpha\varphi(x)-D^\alpha\varphi(x-y)\); the gradient has Euclidean norm at most \(\sqrt n\,p_{m+1}(\varphi)\), and \(|y|\le\varepsilon\) on the bump support.

The bilinear convolution transpose and evenness of the bump give
\[
 \begin{split}
 |(f_j-f_j*\rho_\varepsilon)(\varphi)|
 &=|f_j(\varphi-\rho_\varepsilon*\varphi)|\\
 &\le\sqrt n\,A_j\varepsilon\,p_{m+1}(\varphi).
 \end{split}
 \tag{1.4}
\]
Choose \(0<\varepsilon_j<1/j\) so small that \(L_j+\overline B_{\varepsilon_j}\Subset X\) and
\(\sqrt n\,A_j\varepsilon_j\le2^{-j}\). Then
\[
 g=\sum_{j\ge1}(f_j-f_j*\rho_{\varepsilon_j})
 \tag{1.5}
\]
converges absolutely on every test and satisfies \(|g(\varphi)|\le p_{m+1}(\varphi)\). Its restrictions to fixed compact test spaces are continuous, so it is a global distribution of order at most \(m+1\).

The expanded supports \(L_j+\overline B_{\varepsilon_j}\) remain locally finite in \(X\). Given compact \(C\Subset X\), choose \(r>0\) with \(C+\overline B_r\Subset X\). For all sufficiently large \(j\), \(\varepsilon_j<r\). An expanded support meeting \(C\) then forces \(L_j\) to meet the fixed compact \(C+\overline B_r\), which happens for only finitely many \(j\). The remaining finitely many indices cause no problem.

Each \(f_j*\rho_{\varepsilon_j}\) is smooth, since every derivative passes to the compact smooth bump in the distribution pairing. Thus
\[
 h=\sum_j f_j*\rho_{\varepsilon_j}\in C^\infty(X).
 \tag{1.6}
\]
On a test compactly supported in \(X\), both local sums are finite, and \(\sum_j f_j=f\). Equations (1.5)–(1.6) therefore give \(f=g|_X+h\). This proves the lemma without a uniform bound on the original constants \(A_j\). \(\square\)

## 2. A proper test-function adjoint under singular sampling

Let \(\mu\) be compact and invertible, and let \(X_1,X_2\) be nonempty open sets satisfying
\[
 X_2-\operatorname{sing\,supp}\mu\subset X_1.
 \tag{2.1}
\]
Convexity is not assumed. Define \(Q(X)=\mathcal D'(X)/C^\infty(X)\).

Choose a compactly supported locally finite partition \(\sum_i\lambda_i=1\) on \(X_2\), and write \(L_i=\operatorname{supp}\lambda_i\). Each compact \(L_i-\operatorname{sing\,supp}\mu\) lies inside \(X_1\). A cutoff \(\theta_i\) equal to one near the singular support can therefore be chosen so that
\[
 \mu_i=\theta_i\mu,\qquad
 \mu_i-\mu\in C_c^\infty(\mathbb R^n),\qquad
 L_i-\operatorname{supp}\mu_i\Subset X_1.
 \tag{2.2}
\]
The compact cutoff construction is Lemma 1.1 of the preceding quotient-convolution chapter: choose its support in a sufficiently small neighborhood of the singular set. The removed compact distribution is smooth because it vanishes near all singularities.

Define
\[
 T:\mathcal D(X_2)\longrightarrow\mathcal D(X_1),
 \qquad T\varphi=\sum_i\check\mu_i*(\lambda_i\varphi).
 \tag{2.3}
\]
The sum is finite for a compactly supported \(\varphi\).

**Lemma 2.1 (properness and the quotient transpose).** The map \(T\) is LF continuous. For continuous global \(v\) supported in a fixed compact \(B\Subset X_2\), the same finite formula is continuous from the supremum norm into global distributions with support in one fixed compact subset of \(X_1\). Moreover
\[
 Tv-\check\mu*v\in C_c^\infty(\mathbb R^n),
 \qquad
 \operatorname{sing\,supp}Tv
     =\operatorname{sing\,supp}(\check\mu*v).
 \tag{2.4}
\]
The distributional transpose \(T'u\) induces the canonical map
\(\mu_*:Q(X_1)\to Q(X_2)\).

*Proof.* Only finitely many \(L_i\) meet \(B\). All corresponding image supports lie in the finite union of the compact sets in (2.2), hence in a fixed compact \(H_B\Subset X_1\).

A compact kernel \(\mu\) has one finite global distributional order \(r\). Multiplication by each \(\theta_i\) keeps this order, while changing the bounding constant. For smooth \(\varphi\) supported in \(B\), differentiating (2.3) and applying the compact kernel bound gives, for every derivative order \(a\),
\[
 p_a(T\varphi)\le C_{B,a}p_{a+r}(\varphi).
 \tag{2.5}
\]
Derivatives of the finitely many \(\lambda_i\) are absorbed into the constant. This proves continuity from each \(\mathcal D_B(X_2)\) into \(\mathcal D_{H_B}(X_1)\), and thus LF continuity.

For continuous \(v\) supported in \(B\) and a smooth test \(\psi\), the bilinear pairing is
\[
 (Tv)(\psi)=\sum_i\int \lambda_i(x)v(x)(\mu_i*\psi)(x)\,dx.
 \tag{2.6}
\]
The same finite kernel order bounds its absolute value by a constant times \(\|v\|_\infty p_r(\psi)\). Together with the fixed image support, this proves the asserted distributional continuity.

Since \(\sum_i\lambda_iv=v\), subtraction in the global compact formula gives
\[
 Tv-\check\mu*v
   =\sum_i(\check\mu_i-\check\mu)*(\lambda_iv).
 \tag{2.7}
\]
Each first factor is smooth and compact, so convolution with the second compact factor is smooth and compact. This proves (2.4).

On a compact part of \(X_2\), transposing the finite sum in (2.3) gives
\[
 T'u=\sum_i\lambda_i(\mu_i*u).
 \tag{2.8}
\]
Each local convolution has proper sampling inside \(X_1\) by (2.2). Theorem 1.2 of the preceding quotient-convolution chapter proves that these local representatives differ smoothly and patch to the canonical class \(\mu_*[u]\). Their partition-weighted sum is precisely that class. The identity is complex linear; coefficients are not conjugated. \(\square\)

## 3. Two exhaustions and one global estimate

Assume compact singularity confinement:
\[
 \begin{gathered}
 \text{for every compact }A\Subset X_1
 \text{ there is compact }B'\Subset X_2,\\
 v\in\mathcal E'(X_2),\quad
 \operatorname{sing\,supp}(\check\mu*v)\subset A
 \quad\Longrightarrow\quad
 \operatorname{sing\,supp}v\subset B'.
 \end{gathered}
 \tag{3.1}
\]
For empty image singular support, invertibility makes the input smooth by the exact empty-image case of the linked singular-hull subtraction theorem.

Choose compact exhaustions \(A_j\) of \(X_1\) and \(B_j\) of \(X_2\), with \(A_{j-1}\subset\operatorname{int}A_j\), \(B_{j-1}\subset\operatorname{int}B_j\), such that \(B_j\) contains a receiver from (3.1) for \(A_j\). This is possible by enlarging each input compact to include both the receiver and a prescribed ordinary exhaustion, while keeping the preceding compact in its interior. Put
\[
 A_{-1}=A_0=B_{-1}=B_0=\varnothing.
 \tag{3.2}
\]
The empty-image property justifies these initial receiver choices. The two exhaustions need not be related by a full-kernel Minkowski inclusion.

**Lemma 3.1 (compact regularity outside the input receiver).** For \(j\ge0\), let \(V_j\) consist of continuous global functions supported in \(B_{j+1}\) such that \(Tv\) is smooth on \(X_1\setminus A_{j-1}\). The supremum norm of \(v\), together with all compact derivative seminorms of that image, makes \(V_j\) Fréchet. Restriction is a continuous map
\[
 V_j\longrightarrow C^\infty(X_2\setminus B_{j-1}).
 \tag{3.3}
\]
A bounded sequence has a subsequence converging smoothly on every compact subset of this latter open set.

*Proof.* Both open smooth-function spaces have countable compact exhaustions and derivative seminorms. A Cauchy sequence in \(V_j\) converges uniformly to a continuous supported \(v\), and its images converge smoothly on \(X_1\setminus A_{j-1}\). Lemma 2.1 identifies the image limit distributionally with \(Tv\), proving completeness. The topology is Hausdorff and countably seminormed, hence is Fréchet.

The global compact \(Tv\) is supported strictly inside \(X_1\), so its singular support is contained in \(A_{j-1}\). Equation (2.4) and confinement place the singular support of \(v\) in \(B_{j-1}\); the empty case follows from invertibility. Thus the restriction (3.3) is smooth.

Its graph is closed: uniform convergence of \(v\) identifies any smooth limit of its restrictions on the indicated open set. The linked Fréchet closed graph theorem therefore proves continuity. A bounded sequence then has every derivative bounded on each target compact. The exact compact smooth subsequence theorem in Sections 2–3 of the linked test-family lesson, applied to a countable exhaustion, gives the last assertion. \(\square\)

**Lemma 3.2 (global estimate with locally finite smooth tests).** Given \(f\in\mathcal D'(X_2)\), there are a continuous LF seminorm \(q\) on \(\mathcal D(X_1)\), a constant \(M\), and smooth tests \(\psi_\ell\in\mathcal D(X_2)\) with locally finite supports, such that every \(\varphi\in\mathcal D(X_2)\) satisfies
\[
 |f(\varphi)|+\|\varphi\|_\infty
 \le M\left(q(T\varphi)+
                 \sum_\ell\left|\int\varphi\psi_\ell\right|\right).
 \tag{3.4}
\]
The sum is finite on each test.

*Proof.* Write \(F(\varphi)=|f(\varphi)|+\|\varphi\|_\infty\). Inductively suppose
\[
 F(\varphi)\le M_j\left(q_j(T\varphi)+
             \sum_{\ell\le b_j}\left|\int\varphi\psi_\ell\right|\right)
                  \quad(\operatorname{supp}\varphi\subset B_j).
 \tag{3.5}
\]
For \(j=0\), start with \(M_0=1,q_0=0,b_0=0\); only the zero test has support in \(B_0\).

Fix \(\varepsilon>0\). We show that (3.5) extends to support \(B_{j+1}\) with constant \(M_j(1+\varepsilon)\), after adding finitely many compact derivative seminorms on \(X_1\setminus A_{j-1}\) to \(q_j\), and finitely many tests supported in \(X_2\setminus B_{j-1}\).

Choose a countable defining sequence \(p_a\) for \(C^\infty(X_1\setminus A_{j-1})\), and a countable dense sequence \(\eta_a\) in \(\mathcal D(X_2\setminus B_{j-1})\), using the proved test-family construction. If no extension were possible, for every integer \(N\ge1\) there would be \(\varphi_N\in\mathcal D_{B_{j+1}}(X_2)\) with
\[
 \begin{gathered}
 F(\varphi_N)=M_j(1+\varepsilon),\\
 q_j(T\varphi_N)+\sum_{\ell\le b_j}
             \left|\int\varphi_N\psi_\ell\right|
 +N\sum_{a\le N}p_a(T\varphi_N)
 +N\sum_{a\le N}\left|\int\varphi_N\eta_a\right|<1.
 \end{gathered}
 \tag{3.6}
\]
Indeed these are allowed finite additions; rescale a counterexample to the proposed estimate. The normalization gives a uniform supremum bound.

The images \(T\varphi_N\) tend to zero smoothly outside \(A_{j-1}\), so this sequence is bounded in \(V_j\). By Lemma 3.1 its restrictions outside \(B_{j-1}\) are smoothly precompact. For each fixed \(\eta_a\), the integrals in (3.6) tend to zero. Uniform boundedness of \(\varphi_N\) extends this convergence to every test on that open set: integration against a fixed bounded function is bounded by its supremum times the \(L^1\) norm of the test, and the dense sequence approximates any test in that norm. Every smooth subsequential limit is therefore zero. Precompactness shows the entire restriction sequence tends smoothly to zero; otherwise a subsequence separated from zero in one seminorm would have a convergent further subsequence.

Choose \(0\le\chi\le1\), supported in \(\operatorname{int}B_j\) and equal to one near \(B_{j-1}\). When \(j=0\), choose \(\chi=0\). The sequence
\[
 (1-\chi)\varphi_N\longrightarrow0
                         \quad\text{in }\mathcal D(X_2)
 \tag{3.7}
\]
has fixed support in \(B_{j+1}\). All its derivatives converge to zero: the factor vanishes near \(B_{j-1}\), and the remaining part of the fixed compact is covered by the smooth convergence outside it.

Continuity of \(f\), of \(T\) from Lemma 2.1, of \(q_j\), and of the finitely many old pairings gives
\[
 \begin{split}
 F(\chi\varphi_N)&\ge M_j(1+\varepsilon)-o(1),\\
 q_j(T(\chi\varphi_N))+
       \sum_{\ell\le b_j}\left|\int\chi\varphi_N\psi_\ell\right|
       &\le1+o(1).
 \end{split}
 \tag{3.8}
\]
But \(\chi\varphi_N\) has support in \(B_j\), so (3.5) contradicts (3.8) for large \(N\). The extension claim follows.

Iterate with positive \(\varepsilon_j\) having finite sum. The product \(\prod_j(1+\varepsilon_j)\) is bounded by \(\exp(\sum_j\varepsilon_j)\), so the constants have a common upper bound \(M\).

The accumulated seminorm \(q\) is LF continuous on \(\mathcal D(X_1)\). On any fixed compact output support space, all sufficiently late additions vanish, because their derivative seminorms are located outside the exhausting \(A_{j-1}\). The remaining finite sum is continuous there. This is the defining LF seminorm criterion proved in the test-family lesson.

The accumulated tests have locally finite supports in \(X_2\): at stage \(j\) only finitely many are added, outside \(B_{j-1}\), and these compacts exhaust the input domain with nested interiors. Every fixed compact input support is reached by (3.5). Passing to the accumulated estimate proves (3.4). \(\square\)

## 4. Every distribution class has a solution

**Theorem 4.1 (full quotient sufficiency).** Under (2.1), invertibility and compact singularity confinement (3.1) imply
\[
 \mu_*Q(X_1)=Q(X_2).
 \tag{4.1}
\]
The data are arbitrary distributions, with no one global order assumed.

*Proof.* For \(f\in\mathcal D'(X_2)\), use Lemma 3.2 and consider
\[
 \varphi\longmapsto
 \left(T\varphi,\left(\int\varphi\psi_\ell\right)_\ell\right)
       \in\mathcal D(X_1)\oplus\ell^1.
 \tag{4.2}
\]
The sequence has finite support for each \(\varphi\). On this range define the linear functional sending the displayed pair to \(f(\varphi)\). Estimate (3.4) proves it is well defined, even if (4.2) has a kernel, and bounds it by
\(M(q(w)+\|a\|_1)\).

Apply the proved complex seminorm Hahn–Banach theorem in Proposition 1.1 of the test-family lesson. Its restriction to the first summand is a distribution \(u\) on \(X_1\), bounded by \(Mq\). On the second summand, let \(c_\ell\) be its value at the \(\ell\)-th unit vector. The bound gives \(|c_\ell|\le M\); linearity gives the sum \(\sum_\ell c_\ell a_\ell\) on finite sequences, and their norm-density gives it on all of \(\ell^1\). Consequently
\[
 f(\varphi)=u(T\varphi)+
                     \sum_\ell c_\ell\int\varphi\psi_\ell.
 \tag{4.3}
\]
The locally finite sum \(h=\sum_\ell c_\ell\psi_\ell\) is smooth on \(X_2\). Thus \(f=T'u+h\), and Lemma 2.1 identifies \([T'u]=\mu_*[u]\). This proves (4.1). No continuous linear choice of \(u\) is asserted. \(\square\)

Together with the exact necessity theorems in the preceding quotient-convolution chapter, this gives the equivalence between quotient surjectivity and invertibility with compact singularity confinement on singular-support-compatible open domains.

## 5. Ordinary solvability for every distribution

For the ordinary operation assume the stronger sampling condition
\[
 X_2-\operatorname{supp}\mu\subset X_1.
 \tag{5.1}
\]
The pair is **convex for supports** when every compact image-support bound in \(X_1\) has a compact input-support receiver in \(X_2\) for \(\check\mu*v\), \(v\in\mathcal E'(X_2)\). The full equivalence with the ordinary support-distance condition is proved in Support distances and admissible convolution domains. Singular-support convexity uses (3.1).

**Theorem 5.1 (ordinary distributional criterion).** For a compact kernel and nonempty open domains satisfying (5.1), the map
\[
 \mu*:\mathcal D'(X_1)\longrightarrow\mathcal D'(X_2)
 \tag{5.2}
\]
is surjective if and only if the kernel is invertible and the pair is convex both for supports and for singular supports.

*Proof of necessity.* Full distributional solvability includes a distributional solution for every smooth datum. Theorem 8.1 of the linked smooth-convolution lesson gives invertibility and support convexity. It also implies quotient surjectivity, because (5.1) makes the ordinary operation a representative of the canonical quotient map. Theorems 2.1 and 4.1 of the preceding quotient-convolution chapter give compact singularity confinement.

*Proof of sufficiency.* Theorem 4.1 supplies \(u_0\in\mathcal D'(X_1)\) with
\[
 r=\mu*u_0-f\in C^\infty(X_2).
 \tag{5.3}
\]
Invertibility and support convexity let Theorem 8.1 give a smooth \(w\) on \(X_1\) with \(\mu*w=-r\). Then \(u=u_0+w\) satisfies \(\mu*u=f\). This removes the entire smooth error on \(X_2\). \(\square\)

## 6. Finite-order forcing needs only support geometry

**Theorem 6.1.** Suppose (5.1) holds, the kernel is invertible, and the pair is convex for supports. Every finite-order \(f\in\bigcup_m\mathcal D^{\prime m}(X_2)\) has a solution \(u\in\mathcal D'(X_1)\). That solution has finite order on every bounded open subset of \(X_1\). If \(X_1\) is bounded, it has one finite order on all of \(X_1\).

*Proof.* Lemma 1.1 supplies a global distribution \(g\) with \(f-g|_{X_2}\) smooth. The whole-space pair for this invertible kernel is convex for singular supports. Indeed Theorem 4.1 of Singular Fourier profiles and convex equation domains gives its full family criterion, and every nonempty carrier has \(E_K(\mathbb R^n)=\mathbb R^n\).

Apply Theorem 4.1 here on the two whole spaces. There is a global \(u_0\in\mathcal D'(\mathbb R^n)\) with \(\mu*u_0-g\) globally smooth. Ordinary sampling (5.1) identifies the convolution of \(u_0|_{X_1}\) with that global convolution on \(X_2\). Hence
\[
 h=f-\mu*(u_0|_{X_1})\in C^\infty(X_2).
 \tag{6.1}
\]
The smooth-forcing Theorem 8.1 gives \(w\in C^\infty(X_1)\) with \(\mu*w=h\). Then \(u=u_0|_{X_1}+w\) solves the equation.

For a bounded open \(Y\subset X_1\), enclose \(\overline Y\) in a compact ball of \(\mathbb R^n\). The global distribution \(u_0\) has some finite order \(N_Y\) on that ball, and so its restriction has order at most \(N_Y\) on \(Y\). The smooth function \(w\) defines a distribution of order zero: on each compact \(C\Subset Y\), its action is bounded by \(\int_C|w|\) times the test supremum. Thus \(u|_Y\) has finite order. If \(X_1\) itself is bounded, use it as \(Y\). For unbounded \(X_1\), the allowed order may depend on the bounded region. \(\square\)

This result addresses finite-order forcing under support geometry. The criterion in Theorem 5.1 covers all distributional forcing, including orders that increase without bound along an exhaustion.

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, freely readable [course materials](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The linked course chapters supply the canonical quotient operation, exact necessity, compact singular-hull facts, full smooth-forcing equivalence and functional-analysis prerequisites. The finite-order extension and the complete nonlocal two-domain exhaustion proof are given here.
