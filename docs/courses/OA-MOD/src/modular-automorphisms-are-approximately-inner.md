# Modular automorphisms are approximately inner

The modular group of an approximately finite-dimensional factor of type III₁ can be approximated by inner automorphisms. The approximation is in the pointwise norm topology of the predual. Its proof joins two constructions: the covariant C*-algebra of modular integrals, and the criterion that turns local vector intertwiners into implementing unitaries.

The spectral argument below retains the domain of the modular square root. It also treats finite families whose sum state is not faithful; adding an extra vector would change the relative error being estimated.

## 1. Statement and exact inputs

**Theorem 1.1.** Let \(M\) be an approximately finite-dimensional factor of type III₁ with separable predual. For every faithful normal state \(\psi\) and every \(\tau\in\mathbb R\), the automorphism \(\sigma_\tau^\psi\) is approximately inner. More generally, the conclusion holds for a semidiscrete factor of type III₁ with separable predual.

Here approximately finite-dimensional means that an increasing directed family of finite-dimensional unital subalgebras generates \(M\) as a von Neumann algebra. The separable-predual hypothesis is retained throughout. Approximate innerness means that there are unitaries \(u_n\in M\) such that

\[
 \|\omega\circ\operatorname{Ad}(u_n)^{-1}
       -\omega\circ(\sigma_\tau^\psi)^{-1}\|\longrightarrow0
 \qquad(\omega\in M_*).
 \tag{1}
\]

The sequence may depend on \(\psi\) and \(\tau\).

We use the following earlier proofs at their stated generalities.

- QV01 supplies the minimal-tensor multiplication bound for semidiscrete algebras, including the approximately finite-dimensional case.
- The bicentralizer theorem, Theorem 6.1 proves \(\mathrm B(M,\varphi)=\mathbb C1\) for **every** faithful normal state on a type III₁ factor with separable predual. Its proof passes through the eight lessons of that course; it is not an additional assumption on \(\varphi\).
- CV05–CV08 construct the coefficient and integrated C*-algebras and their modular covariance under those two hypotheses.
- IU06 proves the local criterion for approximate innerness on a type III factor with separable predual.

We work in a standard form \((M,H,J,P)\). Write \(\zeta a=Ja^*J\zeta\) for the right action. For an automorphism \(\theta\), write \(\theta\zeta\) for its canonical action on the cone. The criterion in IU06 asks: for every finite family \(\xi_1,\ldots,\xi_m\in P\) and every \(\varepsilon>0\), find a nonzero \(x\in M\) such that

\[
 \left(\sum_j\|x\xi_j-(\theta\xi_j)x\|^2\right)^{1/2}
 \leq\varepsilon\left(\sum_j\|x\xi_j\|^2\right)^{1/2}.
 \tag{2}
\]

Sections 2–6 establish (2) for \(\theta=\sigma_\tau^\psi\).

## 2. The state supplied by the test family

Put \(\Phi=\sum_j\omega_{\xi_j}\), and let \(p\) be its support, as constructed in CP12.

If \(p<1\), both \(r=1-p\) and \(s=1-\theta(p)\) are nonzero. The factor-corner argument in GI06 proves \(sMr\ne0\). Take \(0\ne x\in sMr\). Since

\[
 (1-p)\xi_j=0=\xi_j(1-p),
\]

and the transported vector has support \(\theta(p)\) on both sides, we have \(x\xi_j=0=(\theta\xi_j)x\). Thus (2) holds exactly. This includes an empty or entirely zero family.

Suppose henceforth that \(p=1\). Multiply all the \(\xi_j\) by the same positive constant so that \(\sum_j\|\xi_j\|^2=1\). Both sides of (2) are multiplied by that constant. Now \(\varphi=\Phi\) is a faithful normal state. Let \(\xi\in P\) be its representing unit vector; \(\xi\) is cyclic and separating. These standard-form facts are proved in SF10–SF12.

For \(a\in M\),

\[
 \|a\xi_j\|^2\leq\sum_k\|a\xi_k\|^2=\|a\xi\|^2.
 \tag{3}
\]

Therefore \(a\xi\mapsto a\xi_j\) extends from the dense space \(M\xi\) to a contraction \(T_j\in M'\). Indeed it commutes with each left multiplier on that dense space, hence on \(H\). Set \(b_j=JT_j^*J\in M\). Since \(J\xi=\xi\) and \(J\xi_j=\xi_j\),

\[
 \begin{gathered}
 \|b_j\|\leq1,\\
 \xi_j=\xi b_j=b_j^*\xi.
 \end{gathered}
 \tag{4}
\]

In particular, for every \(y\in M\),

\[
 \sum_j\|y\xi_j\|^2=\varphi(y^*y)=\|y\xi\|^2.
 \tag{5}
\]


The cocycle identity SI14, equation (SI.61) gives a unitary \(w=[D\psi:D\varphi]_\tau\in M\) with

\[
 \sigma_\tau^\psi=\operatorname{Ad}(w)\circ\sigma_\tau^\varphi.
 \tag{6}
\]

Write \(\gamma=\sigma_\tau^\varphi\). If \(y\ne0\) satisfies (2) with \(\gamma\), then \(x=wy\) satisfies it with \(\theta\): LC06 proves the exact identities

\[
 (wy)\xi_j-(\theta\xi_j)(wy)
 =w\bigl(y\xi_j-(\gamma\xi_j)y\bigr),
 \qquad \|wy\xi_j\|=\|y\xi_j\|.
 \tag{7}
\]

It remains to produce \(y\) for the state \(\varphi\) just constructed. This is why the bicentralizer input must hold for every faithful normal state.

## 3. A positive operator and a spectral cutoff

Let \(\Delta=\Delta_\varphi\), \(U_t=\Delta^{it}\) and \(\alpha_t=\operatorname{Ad}(U_t)\). By FS01,

\[
 \begin{gathered}
 U_t\xi=\xi,\\
 \Delta^{1/2}y\xi=\xi y\quad(y\in M),\\
 M\xi\text{ is a core for }\Delta^{1/2}.
 \end{gathered}
 \tag{8}
\]

The core assertion follows because the Tomita operator is the closure of \(y\xi\mapsto y^*\xi\), and multiplication by the antiunitary \(J\) preserves graph norms.

Put \(R_b=Jb^*J\), and define

\[
 X=\sum_{j=1}^m(R_{b_j}-b_j^*)^*(R_{b_j}-b_j^*).
 \tag{9}
\]

Then \(X\in C^*(M,M')\), \(X\xi=0\), and \(0\leq X\leq4mI\). The first equality on \(\xi\) is (4); the bound follows from \(\|R_{b_j}-b_j^*\|\leq2\).

Let \(\mathcal C\) be the coefficient algebra of CV02–CV05, which contains \(C^*(M,M')\). Its isometric automorphism \(\bar\gamma\), supplied by CV05, acts by \(\gamma\) on \(M\) and fixes \(M'\). Consequently

\[
 \begin{gathered}
 \bar\gamma(X)=\sum_j A_j^*A_j,\\
 A_j=R_{b_j}-\gamma(b_j^*),\\
 \|A_j\|\leq2.
 \end{gathered}
 \tag{10}
\]

It also commutes with \(\alpha\) and its scalar averages.

Fix \(0<\kappa\leq1/4\). Choose \(f\in C_c^\infty((0,\infty))\) such that

\[
 \begin{gathered}
 0\leq f\leq1,\\
 f(1)=1,\\
 \sup_{\lambda>0}|(\sqrt\lambda-1)f(\lambda)|\leq\kappa.
 \end{gathered}
 \tag{11}
\]

For example, choose its support inside a neighborhood of 1 where \(|\sqrt\lambda-1|<\kappa\), using the smooth cutoffs proved in BI03.

Set \(r=f(\Delta)-I\) and \(C=4m+1\). Spectral calculus gives

\[
 \begin{gathered}
 r=r^*,\\
 \|r\|\leq1,\\
 r\xi=0,\\
 0\leq X+r^2\leq CI.
 \end{gathered}
 \tag{12}
\]

The operator \(CI-X-r^2\) is positive and has norm exactly \(C\), since it sends \(\xi\) to \(C\xi\). The same upper bound and positivity hold with \(X\) replaced by \(\bar\gamma(X)\); equality of that latter norm is the point of the next section.

## 4. Transporting the norm through the integral algebra

Let \(\mathcal A\subset\mathcal C\) be the norm-continuous coefficient algebra of CV05. Write \(\mathcal B\) for the norm closure of

\[
 \int_{\mathbb R}y(t)U_t\,dt,\qquad
 y\in C_c(\mathbb R,\mathcal A).
 \tag{13}
\]

By CV08 there is an isometric automorphism \(\beta\) of \(\mathcal B\) taking (13) to the same integral with coefficient \(\bar\gamma(y(t))\). In particular it fixes every scalar integral \(\int k(t)U_t\,dt\) with \(k\in C_c(\mathbb R)\), and by the bound \(\|\int k(t)U_tdt\|\leq\|k\|_1\), every such integral with \(k\in L^1\).

Here is the required membership for the spectral cutoff. The function \(F(s)=f(e^s)\) lies in \(C_c^\infty(\mathbb R)\). Fourier inversion in BI03 gives an integrable inverse kernel \(k\) with

\[
 \begin{gathered}
 F(s)=\int k(t)e^{its}\,dt,\\
 f(\Delta)=F(\log\Delta)=\int k(t)U_t\,dt.
 \end{gathered}
 \tag{14}
\]

The last equality follows by scalar spectral integration and Fubini, tested on matrix coefficients; SK04–SK08 supply that calculus. Approximation of \(k\) in \(L^1\) by compact continuous kernels puts (14) in \(\mathcal B\). Thus \(\beta\) fixes \(f(\Delta)\). We do not need to assert that \(I\) or \(r\) itself lies in \(\mathcal B\).

Choose \(h\in C_c^\infty(\mathbb R)\), \(h\geq0\), \(\int h=1\). Put

\[
 \begin{gathered}
 G=\int h(t)U_t\,dt,\\
 X_h=\int h(t)\alpha_t(X)\,dt.
 \end{gathered}
 \tag{15}
\]

Then \(\|G\|\leq1\), \(G\xi=\xi\), \(X_h\in\mathcal A\), \(X_h\xi=0\), and \(0\leq X_h\leq4mI\). CV05 proves the membership of the strong operator average \(X_h\) in \(\mathcal A\), and proves that \(\bar\gamma(X_h)=\alpha_h(\bar\gamma(X))\).

Consider

\[
 Y=(CI-X_h-r^2)G.
 \tag{16}
\]

It belongs to \(\mathcal B\). Indeed, \(X_hG\) is (13) with coefficient \(h(t)X_h\), while

\[
 (CI-r^2)G=(C-1)G+2f(\Delta)G-f(\Delta)^2G
\]

is in \(\mathcal B\) by (14) and its algebra property. Positivity of \(CI-X_h-r^2\) and its upper bound \(CI\) give \(\|Y\|\leq C\), whereas \(Y\xi=C\xi\). Hence \(\|Y\|=C\).

The covariance formula and the fixed scalar integrals give

\[
 \beta(Y)=\bigl(CI-\alpha_h(\bar\gamma(X))-r^2\bigr)G.
 \tag{17}
\]

Since \(r\) commutes with \(U_t\), the first factor in (17) is the average \(\alpha_h(CI-\bar\gamma(X)-r^2)\). This average is contractive, so

\[
 \begin{gathered}
 C=\|\beta(Y)\|,\\
 \|\beta(Y)\|\leq\|CI-\bar\gamma(X)-r^2\|,\\
 \|CI-\bar\gamma(X)-r^2\|\leq C.
 \end{gathered}
 \tag{18}
\]

Let \(Q=\bar\gamma(X)+r^2\). We have \(0\leq Q\leq CI\) and \(\|CI-Q\|=C\). It follows that

\[
 \inf_{\|\eta\|=1}\langle Q\eta,\eta\rangle=0.
 \tag{19}
\]

For if all these quadratic values were at least \(d>0\), then \(dI\leq Q\leq CI\), whence \(0\leq CI-Q\leq(C-d)I\), contradicting (18).

## 5. Returning to the Tomita core

Choose a unit vector \(\eta\) using (19) with

\[
 \sum_j\|A_j\eta\|^2+\|r\eta\|^2<\kappa^2.
 \tag{20}
\]

The squared tolerance is explicit. In particular, each \(\|A_j\eta\|<\kappa\) and \(\|r\eta\|<\kappa\).

Set \(\zeta=f(\Delta)\eta=\eta+r\eta\). It belongs to \(D(\Delta^{1/2})\), since \(f\) has compact support in \((0,\infty)\). Equations (10)–(11) and (20) give

\[
 \begin{gathered}
 \|\zeta\|>1-\kappa,\\
 \|A_j\zeta\|<3\kappa,\\
 \|(\Delta^{1/2}-I)\zeta\|\leq\kappa.
 \end{gathered}
 \tag{21}
\]

The middle inequality uses \(A_j\zeta=A_j\eta+A_jr\eta\); it does not require \(A_j\) to commute with the cutoff.

The core statement (8) supplies \(y\in M\) such that

\[
 \begin{gathered}
 \|y\xi-\zeta\|<\kappa/2,\\
 \|\Delta^{1/2}y\xi-\Delta^{1/2}\zeta\|<\kappa/2.
 \end{gathered}
 \tag{22}
\]

Consequently

\[
 \begin{gathered}
 \|y\xi\|>1-2\kappa,\\
 \|y\xi-\xi y\|<2\kappa,\\
 \|A_jy\xi\|<4\kappa.
 \end{gathered}
 \tag{23}
\]

The first inequality shows \(y\ne0\). The second is obtained by adding the two graph errors in (22) to the last bound in (21); norm approximation alone would not prove it.

## 6. The local error and implementing unitaries

The canonical implementation of \(\gamma=\sigma_\tau^\varphi\) is \(U_\tau\); it preserves the cone and fixes \(\xi\). Therefore (4) implies

\[
 \gamma\xi_j=\gamma(b_j^*)\xi.
 \tag{24}
\]

Left and right actions commute. Using (10) and (24),

\[
 \begin{aligned}
 y\xi_j-(\gamma\xi_j)y
 &=A_jy\xi+\gamma(b_j^*)(y\xi-\xi y),\\
 \|y\xi_j-(\gamma\xi_j)y\|&<6\kappa.
 \end{aligned}
 \tag{25}
\]

Together with (5) and (23), this gives

\[
 \begin{gathered}
 \left(\sum_j\|y\xi_j-(\gamma\xi_j)y\|^2\right)^{1/2}
 <6\sqrt m\,\kappa,\\
 \left(\sum_j\|y\xi_j\|^2\right)^{1/2}>1-2\kappa.
 \end{gathered}
 \tag{26}
\]

Choose

\[
 0<\kappa\leq\min\{1/4,\varepsilon/(12\sqrt m)\}.
 \tag{27}
\]

The first bound in (26) is then at most \(\varepsilon/2\), strictly before the comparison, while the second is greater than \(1/2\). This proves (2) for \(\gamma\); (7) proves it for \(\theta\). Undoing the common normalization preserves that inequality. The proper-support case was already settled in Section 2.

Thus every finite test family satisfies the local criterion. IU06 applies because \(M\) is a type III factor with separable predual, and supplies the unitaries in (1). This proves Theorem 1.1. No sign restriction was placed on \(\tau\). \(\square\)

The argument has a useful intermediate form: a type III factor with separable predual satisfies the same conclusion if it has the multiplication bound and scalar bicentralizer for every faithful normal state. Theorem 1.1 verifies both inputs for the stated class through the earlier programme proofs.

## 7. Faithful semifinite weights and finite families of times

**Corollary 7.1.** Under the hypotheses of Theorem 1.1, every modular automorphism of a faithful normal semifinite weight is approximately inner.

**Proof.** Choose a faithful normal state \(\varphi\), which exists because the predual is separable, as proved in IU01. If \(\chi\) is the weight, SI14 gives

\[
 \sigma_\tau^\chi
 =\operatorname{Ad}([D\chi:D\varphi]_\tau)\circ\sigma_\tau^\varphi.
 \tag{28}
\]

Let \(u_n\) implement the approximation for \(\sigma_\tau^\varphi\), and put \(w=[D\chi:D\varphi]_\tau\). Then \(wu_n\) implements the approximation for (28): for every \(\omega\in M_*\), the norm of the difference of the two predual values is unchanged by their final composition with the isometry \(\operatorname{Ad}(w)^{-1}\). \(\square\)

For a fixed \(\chi\), a finite set of times \(\tau_1,\ldots,\tau_q\), a finite set of normal functionals, and a positive tolerance, (1) supplies one unitary for each time satisfying all those functional tests. No compatibility between these finitely many chosen unitaries has been proved. In particular, pointwise approximate innerness does not by this argument give a single one-parameter unitary group or convergence uniform in time.

## 8. Checks on support, cutoffs, and normalization

**Why retain the original family?** If a new faithful cone vector were appended, the new right side in (2) would contain its extra positive squared norm. An estimate relative to that larger denominator need not imply the required estimate for the original family. The complementary corner in Section 2 resolves this case with no change of denominator.

**Why use a squared tolerance?** Equation (20) bounds squared errors by \(\kappa^2\). This gives the linear estimates \(3\kappa,2\kappa,6\kappa\) in (21), (23), and (25). A bound by \(\kappa\) in (20) would instead give errors of order \(\sqrt\kappa\), requiring a different choice in (27).

**Why include the scalar integral factor?** The positive operator \(CI-X-r^2\) is not asserted to lie in \(\mathcal B\). Smoothing \(X\), then multiplying by \(G\), produces the actual element (16). The identity \(G\xi=\xi\) retains its full norm, while \(\|G\|\leq1\) permits the comparison after applying \(\beta\).

**Finite matrix check.** In the Hilbert–Schmidt standard form of \(M_n(\mathbb C)\), let \(\varphi\) be the normalized trace and \(\xi=n^{-1/2}I\). Then \(\Delta=I\), \(\gamma=\mathrm{id}\), \(r=0\), and \(\eta=\xi\) makes (20) exact. Taking \(y=1\) makes every error zero. For another faithful state with density \(d>0\), its modular automorphism is already \(\operatorname{Ad}(d^{i\tau})\), in agreement with the cocycle transport. This checks the formulas, without applying the type III criterion to a finite algebra.

**Reference.** M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, Theorem 4.12, printed p.381 and proof on pp.387–389. The covariant-algebra preparation is proved in CV; the bicentralizer input is the earlier programme theorem linked in Section 1. The proof above states the separable-predual scope explicitly and includes the support reduction, the integral-algebra membership, the squared-error choice, and the Tomita graph approximation.
