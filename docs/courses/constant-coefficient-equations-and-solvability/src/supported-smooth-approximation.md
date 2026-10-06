# Supported smooth approximation

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Local supported solutions can be corrected on overlapping regions only if homogeneous differences can be approximated on the smaller region. We prove the needed density theorem using the compact local fundamental solution already constructed. The geometry concerns the positive-time part of compact distributions under the transposed operator. Compact containment at the conclusion is essential: it provides a cutoff strictly inside the smaller region, including every limit point on the time boundary.

Read [Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md), [Continuous functionals, test families and compact limits](continuous-functionals-and-test-families.md). [Fourier transforms, finite spectra and convex separation](../prerequisites/prerequisite-bridges.html) supplies Schwartz Fourier inversion; [Metric and topological foundations](../prerequisites/metric-foundation-bridges.html) supplies finite coordinates, scalar calculus and compact cutoffs; [Banach estimates, quotient spaces and compact parameter arguments](../prerequisites/banach-foundation-bridges.html) supplies the norm, extension and integration estimates. [Tensor products and smooth parameters](../prerequisites/tensor-products-and-parameters.html) and [Convolution as addition of supports](../prerequisites/convolution-as-addition-of-supports.html) supply parameter pairings and compact convolution.

Basic references are Grubb's *Distributions and Operators* ([author's lecture notes](https://web.math.ku.dk/~grubb/distribution.htm)), Melrose's *Differential Analysis* and Hörmander's *The Analysis of Linear Partial Differential Operators*. The proofs use the linked prerequisite lessons and any stated planned theorem.

## The support condition and the topology

Let \(X_1\subset X_2\subset\mathbb R^n\) be bounded open sets, and let \(P\ne0\) satisfy the analytic-root hypothesis([equation 1 in Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md)). Write \(H=\{t\ge0\}\), \(H^\circ=\{t>0\}\), and
\[
\begin{gathered}
\mathcal N_j\\
=\{u\in C^\infty(X_j):
       P(D)u\\
=0,\ u\\
=0\text{ on }X_j\cap\{t<0\}\}.
\end{gathered}
\tag{1}
\]
The support condition on \(u\) is relative to \(X_j\); no compact support of \(u\) is required. Give \(\mathcal N_j\) its topology inherited from \(C^\infty(X_j)\), namely uniform convergence of every derivative on every compact subset. Restrictions from \(\mathcal N_2\) lie in \(\mathcal N_1\).

For any set \(A\), write \(A\Subset X_1\) if its closure is a compact subset of \(X_1\). Assume the following statement about all global compactly supported distributions:
\[
\begin{gathered}
\mu\in\mathcal E'(\mathbb R^n),\qquad
                 \\
H^\circ\cap\operatorname{supp}\mu
                                      \subset\overline{X_2},\\
H^\circ\cap\operatorname{supp}P(-D)\mu\Subset X_1
       \quad\\
\Longrightarrow\quad
               \\
H^\circ\cap\operatorname{supp}\mu\Subset X_1.
\end{gathered}
\tag{2}
\]
The closed set \(\overline{X_2}\) in the first line and the two compact-containment conditions in the second line are retained exactly. The positive-time portion need not be a closed set before its closure is taken.

**Theorem.** Under(2), the restrictions to \(X_1\) of \(\mathcal N_2\) are dense in \(\mathcal N_1\). Consequently a smooth supported homogeneous solution on \(X_1\) can be approximated by such solutions on \(X_2\), simultaneously in any finite collection of derivative or weighted cutoff seminorms on \(X_1\).

If \(X_1=\varnothing\), its smooth space is the zero space and the assertion is immediate. We henceforth assume \(X_1\ne\varnothing\), so \(X_2\ne\varnothing\).

## A separating functional has compact distribution support

Let \(L\) be a continuous complex-linear functional on \(\mathcal N_1\) which annihilates all the indicated restrictions. Continuity bounds it by a finite list of smooth seminorms. Increasing their derivative order and taking the finite union of their compact sets gives a compact \(K\subset X_1\), an integer \(m\), and \(C\) with
\[
 |L(u)|\le C\max_{|\alpha|\le m}\sup_K|\partial^\alpha u|.
 \tag{3}
\]
Seminorm Hahn–Banach extends it to \(L_1\) on \(C^\infty(X_1)\) with the same bound. Its restriction to global test functions is a distribution \(\nu\) with support in \(K\): the fixed-stage bound proves distributional continuity, and a test vanishing near \(K\) has zero bound.

To specify its action on every \(u\in C^\infty(X_1)\), choose \(\rho\in C_c^\infty(X_1)\) equal to one near \(K\). The bound kills \(L_1((1-\rho)u)\). Extend \(\rho u\) smoothly by zero outside \(X_1\); then
\[
               L_1(u)=\nu(\rho u)=:\nu(u).
 \tag{4}
\]
This notation is independent of the chosen cutoff. It identifies precisely the smooth functional with an element of \(\mathcal E'(X_1)\); no dual representation theorem is left implicit. In particular \(\nu\) annihilates the restrictions of \(\mathcal N_2\).

## A local fundamental solution on all relevant differences

Choose a bounded open \(\Omega\) containing the compact set
\(\overline{X_2}-\overline{X_2}\).
The [Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md) consequence supplies a compactly supported \(E\), supported in \(H\), with
\[
 P(D)E=\delta_0+r,\qquad r=0\text{ on }\Omega.
 \tag{5}
\]
Both \(r\) and \(E\) are compact distributions. Put
\[
                 Y=\{y:\overline{X_2}-\{y\}\subset\Omega\}.
 \tag{6}
\]
It is open: for any \(y\in Y\), the compact set \(\overline{X_2}-y\) has positive distance from the closed complement of \(\Omega\); sufficiently small changes in \(y\) preserve its inclusion. It contains \(\overline{X_2}\) by the choice of \(\Omega\).

For \(\phi\in C_c^\infty(H^\circ\cap(Y\setminus\overline{X_2}))\), the global smooth compact function \(E*\phi\) has support in \(H\), because both factors have nonnegative time support. Also
\[
              P(D)(E*\phi)=\phi+r*\phi=0\text{ on }X_2.
 \tag{7}
\]
The first term vanishes there. For the second, if \(x\in X_2\) and \(y\in\operatorname{supp}\phi\subset Y\), then \(x-y\in\Omega\), where \(r\) vanishes. Equivalently no point of \(X_2\) is in \(\operatorname{supp}r+\operatorname{supp}\phi\), by(6). The compact-factor convolution support theorem proves the claim, including distributions. Thus the restriction of \(E*\phi\) belongs to \(\mathcal N_2\).

Set \(\mu=\check E*\nu\), a compact distribution. The exact bilinear convolution identity is
\[
                    \mu(\phi)=\nu(E*\phi).
 \tag{8}
\]
Indeed, compact tensor pairing writes its left side as
\(E_z\nu_a(\phi(a-z))\), which is the right side. There is reflection and no conjugation. The tensor/convolution definition permits the two compact distribution pairings in either order, as in the named compact-factor theorem. By annihilation and(7)–(8), \(\mu\) vanishes on \(H^\circ\cap(Y\setminus\overline{X_2})\). Moreover
\[
\begin{gathered}
P(-D)\mu=\nu+\check r*\nu,\\
\qquad
                         P(-D)\mu=\nu\text{ on }Y.
\end{gathered}
\tag{9}
\]
To see the second equality, a support point of \(\check r*\nu\) has the form \(a-z\), \(a\in\operatorname{supp}\nu\subset X_1\), \(z\in\operatorname{supp}r\). If \(y=a-z\) were in \(Y\), then \(z=a-y\in\overline{X_2}-y\subset\Omega\), contradicting(5). Support addition gives the stated vanishing. The first equality is the reflection of(5), followed by compact convolution differentiation.

## Two localizations and the boundary

Choose \(\chi\in C_c^\infty(Y)\) equal to one near \(\overline{X_2}\), and put \(\mu_1=\chi\mu\). The just established positive-time vanishing gives
\[
\begin{gathered}
H^\circ\cap\operatorname{supp}\mu_1\subset\overline{X_2},
       \\
\qquad
          P(-D)\mu_1-\nu=0\text{ on }H^\circ.
\end{gathered}
\tag{10}
\]
For the second assertion, the term \(\chi P(-D)\mu\) is \(\chi\nu=\nu\), since \(\chi\)'s support is inside \(Y\) and it equals one near \(\operatorname{supp}\nu\). Every remaining product-rule term contains a positive-order derivative of \(\chi\) multiplied by a derivative of \(\mu\). Such derivatives of \(\chi\) are zero near \(\overline{X_2}\), while in the remaining positive-time part of \(Y\), \(\mu\) and all its derivatives vanish. Outside \(\operatorname{supp}\chi\), those terms vanish as well. Thus all those terms vanish on \(H^\circ\). This explicitly controls the commutator without an equation on the time boundary.

The positive-time support of \(P(-D)\mu_1\) lies in the fixed compact \(\operatorname{supp}\nu\subset X_1\). Apply(2) to \(\mu_1\): the closure of \(H^\circ\cap\operatorname{supp}\mu_1\) is a compact subset of \(X_1\). We may therefore choose \(\theta\in C_c^\infty(X_1)\) equal to one near that closure and near \(\operatorname{supp}\nu\). Put \(\mu_2=\theta\mu_1\). It belongs to \(\mathcal E'(X_1)\) and equals \(\mu_1\) on \(H^\circ\): near its positive-time support the multiplier is one, and elsewhere that distribution is zero. Consequently
\[
\begin{gathered}
\nu_2=P(-D)\mu_2\in\mathcal E'(X_1),\\
\qquad
                  \operatorname{supp}(\nu-\nu_2)\subset\{t\le0\}.
\end{gathered}
\tag{11}
\]
For \(u\in\mathcal N_1\), compact distributional transposition inside \(X_1\) gives \(\nu_2(u)=\mu_2(P(D)u)=0\). The other compact distribution \(\nu-\nu_2\) is supported in nonpositive time. Multiply \(u\) by a compact cutoff inside \(X_1\) equal to one near this distribution's support, and extend by zero. The resulting smooth global test vanishes for \(t<0\), hence is flat at \(t=0\). The actual [Local supported solutions with the exact symbol gain](local-supported-solutions-with-exact-symbol-gain.md) flat-test proof gives \((\nu-\nu_2)(u)=0\). Thus \(\nu(u)=0\), and(4) gives \(L(u)=0\) for every \(u\in\mathcal N_1\).

If the restriction subspace were not dense, apply locally convex separation to its closure in \(\mathcal N_1\) and a point outside. It would give a continuous \(L\) annihilating the subspace but not that point, contrary to what we proved. This completes the density theorem. The space \(\mathcal N_1\) is Hausdorff with its inherited locally convex topology; completeness is not needed by the separation theorem.

## The weighted seminorm consequence

Fix \(\psi\in C_c^\infty(X_1)\), a moderate weight \(k\), and \(1\le p\le\infty\). Polynomial growth gives \(k(\xi)\le C(1+|\xi|)^N\). Choose an integer \(a\) with \(2a>N+n+1\). Repeated integration by parts using \((1-\Delta)^a\) gives
\[
\begin{gathered}
|\widehat{\psi u}(\xi)|
       \\
\le C_\psi(1+|\xi|^2)^{-a}
          \\
\max_{|\alpha|\le2a}
                       \sup_{\operatorname{supp}\psi}|\partial^\alpha u|,
 \\\|\psi u\|_{p,k}\le C_{\psi,k,p}
          \\
\max_{|\alpha|\le2a}
                       \sup_{\operatorname{supp}\psi}|\partial^\alpha u|.
\end{gathered}
\tag{12}
\]
The \(L^p\) integral of the weighted decay is finite for every finite \(p\); the supremum is finite for \(p=\infty\). The product-rule derivatives of \(\psi u\) have been absorbed in the fixed constant. A smooth approximation in the finite set of derivative seminorms implied by(12) is therefore an approximation in any prescribed finite list of weighted cutoff norms. This consequence includes the infinity norm for smooth solutions, and does not assert mollifier density for arbitrary \(B_{\infty,k}\) distributions.

## Exercises with complete solutions

**Exercise 1 (entry).** In one time variable let \(P(s)=s-i\), \(E(t)=iH(t)e^{-t}\), and \(\nu=\delta_a\), \(a>0\). Compute \(\mu=\check E*\nu\) and verify the transpose identity. This example may use the global kernel; it is a sign check rather than the compact parametrix construction.

**Solution.** Since convolution with \(\delta_a\) translates by \(a\), \(\mu(t)=E(a-t)=iH(a-t)e^{t-a}\). Its support is \(t\le a\). Distributional differentiation gives
\(\mu'=-i\delta_a+iH(a-t)e^{t-a}\).
The transposed operator is \(P(-D_t)=-D_t-i=i\partial_t-i\). Therefore \(i\mu'-i\mu=\delta_a-H(a-t)e^{t-a}+H(a-t)e^{t-a}=\delta_a\), as required. The pairing \[
\begin{gathered}
\mu(\phi)\\
=\int iH(a-t)e^{t-a}\phi(t)\,dt\\
=(E*\phi)(a)\\
=\nu(E*\phi)
\end{gathered}
\] verifies(8) directly. No coefficient conjugation occurs. The kernel is not compact, but the compact factor \(\nu\) makes this illustrative convolution defined.

**Exercise 2 (intermediate).** Let \(A=\{1/j:j\ge1\}\) and \(X_1=(0,2)\). Explain why \(A\subset X_1\) does not supply a cutoff \(\theta\in C_c^\infty(X_1)\) equal to one near \(A\). Relate this to the exact containment in(2).

**Solution.** The closure of \(A\) contains zero, which is outside \(X_1\). A compact subset of \((0,2)\) has positive distance from zero. Thus any compactly supported \(\theta\) in this interval is zero at \(1/j\) for all sufficiently large \(j\), and cannot be one near all of \(A\). The failure persists for the positive-time support of a compact distribution: \(\sum_{j\ge1}2^{-j}\delta_{1/j}\) is a compact finite measure with that positive-time support and with zero as a support limit point. In(2) the conclusion is \(H^\circ\cap\operatorname{supp}\mu\Subset X_1\); its closure is compact inside \(X_1\), so the required cutoff exists. This example diagnoses the invalid cutoff inference after weakening the condition; it does not claim the density theorem itself fails for every weaker hypothesis.

**Exercise 3 (advanced).** For a compact \(K\subset X_1\), a finite family of cutoffs \(\psi_j\in C_c^\infty(X_1)\), weights \(k_j\), and exponents \(1\le p_j\le\infty\), show how the density theorem supplies one \(h\in\mathcal N_2\) with prescribed simultaneous derivative and weighted errors for a given \(u\in\mathcal N_1\). Identify why this does not use general infinity-endpoint density.

**Solution.** For each weighted error select the derivative order \(2a_j\) and constant \(C_j\) in(12). Combine \(K\) and all \(\operatorname{supp}\psi_j\) into one compact subset of \(X_1\), and take the largest of the desired derivative order and the \(2a_j\). The theorem approximates \(u\) by a restriction \(h|_{X_1}\) within any positive tolerance in that single smooth seminorm. Choose the tolerance below the specified derivative error and below every weighted tolerance divided by \(C_j\). Then(12) bounds every \(\|\psi_j(u-h)\|_{p_j,k_j}\) by its tolerance, including \(p_j=\infty\). Both approximated functions are smooth. No claim that arbitrary infinity-norm distributions can be approximated by smooth functions is involved.

## References

- Gerd Grubb, *Distributions and Operators*, lecture-note versions, 2007–2008. [Lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition (1990), reprinted in Classics in Mathematics, Springer, 2003, e-ISBN 978-3-642-61497-2.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
