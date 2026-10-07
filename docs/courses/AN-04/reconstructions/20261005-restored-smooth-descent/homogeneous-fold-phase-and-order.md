# The homogeneous fold phase and its amplitude order

This companion supplies the order calculation used in [Folds, reflections and uniform smooth descent](folds-reflections-and-uniform-descent.md). It reuses the explicit model already developed in the preserved course, proving the required part here so that the descent lesson does not depend on a later lesson. The earlier inputs are the nondegenerate-phase construction in [Phase space and generating families](../20261005-restored-phase-space/phase-space-and-generating-families.md), the normalized integral and order convention in Oscillatory distributions and their order, and its exact elementary calculus providers. The [proof map](proof-map.json) records those dependencies.

Write \(n\geq2\), \(\rho=\xi_n\), and work in \(\rho\geq1\), \(|\xi|\leq C\rho\). The degree-zero variable \(s\) lies in a fixed compact interval. Base variables are \((x,y)\in\mathbb R^{2n}\). Smooth cutoffs may restrict them to a compact set. All symbol estimates below are uniform in every \(s,x,y\) derivative; frequency derivatives lower the order by their total degree.

## P0. A nondegenerate homogeneous phase through the fold

Introduce \(\tau=\rho s\) and \(\theta=(\xi,\tau)\). The cubic expression and the homogeneous phase are
\[
\Phi=(x-y)\cdot\xi+s\xi_1-\frac{s^3\rho}{3},
\qquad
\phi=(x-y)\cdot\xi+\frac{\tau\xi_1}{\rho}
-\frac{\tau^3}{3\rho^2}.
\]
The change is smooth and invertible for \(\rho>0\). Scaling \(\theta\) by \(t>0\) scales \(\phi\) by \(t\). Its auxiliary derivatives are
\[
\begin{split}
\phi_{\xi_1}&=x_1-y_1+\tau/\rho,\\
\phi_{\xi_j}&=x_j-y_j\quad(1<j<n),\\
\phi_\rho&=x_n-y_n-\tau\xi_1/\rho^2+2\tau^3/(3\rho^3),\\
\phi_\tau&=\xi_1/\rho-\tau^2/\rho^2.
\end{split}
\]
Their \(n+1\) differentials are independent. In a vanishing linear combination, the \(dy_j\) coefficients first force the coefficients of the first \(n\) differentials to be zero. The remaining differential has nonzero \(\xi_1\) derivative \(1/\rho\), so its coefficient is also zero. This uses \(n\geq2\), which keeps \(\xi_1\) distinct from \(\rho\). The full phase differential is nonzero since \(\phi_y=-\xi\) and \(\rho>0\).

The critical equations, with \(s=\tau/\rho\), give
\[
\xi_1=s^2\rho,\qquad
y_1=x_1+s,\qquad y_j=x_j\ (1<j<n),\qquad
y_n=x_n-s^3/3.
\]
The output and input covectors are \(\phi_x=\xi\) and \(-\phi_y=\xi\). Thus \((x,s,\xi_2,\ldots,\xi_n)\) parametrize the resulting relation, smoothly and injectively: these variables are recovered from \(x,\xi_2,\ldots,\xi_n\) and \(s=y_1-x_1\). The same recovery shows that the parametrization is an immersion. The proved nondegenerate-phase theorem gives its Lagrangian property and dimension \(2n\). All these arguments hold at \(s=0\); none divides by \(s\).

## P1. The Jacobian changes the ordinary symbol order by one

Let \(a(x,y,s,\xi)\) have ordinary order \(\nu\), uniformly on the stated supports. Since \(d\tau=\rho\,ds\) at fixed \(\xi\), set
\[
\widetilde a(x,y,\xi,\tau)=\rho^{-1}a(x,y,\tau/\rho,\xi).
\]
On its support, \(|\theta|\asymp\rho\). The first derivatives, evaluated at \(s=\tau/\rho\), are
\[
\partial_\tau\widetilde a=\rho^{-2}a_s,\qquad
\partial_{\xi_j}\widetilde a=\rho^{-1}a_{\xi_j}\ (j\ne n),\qquad
\partial_\rho\widetilde a=-\rho^{-2}a+\rho^{-1}a_\rho-s\rho^{-2}a_s.
\]
Here the last derivative holds \(\tau\) fixed. These formulas prove every higher estimate by induction: differentiating a power of \(\rho\) loses one order; differentiating \(s=\tau/\rho\) contributes \(\rho^{-1}\) or \(-s/\rho\); and an external \(\xi\) derivative of \(a\) loses one order. Every \(s\) derivative of \(a\) has the same order as \(a\), and \(s\) remains bounded. Consequently each derivative of total auxiliary degree \(k\) is bounded by a constant times \(\rho^{\nu-1-k}\), using only finitely many original seminorms. Base differentiation commutes with these formulas. Thus \(\widetilde a\in S^{\nu-1}\).

Conversely \(a=\rho\,\widetilde a(x,y,\xi,\rho s)\). Each \(s\) derivative acts by \(\rho\partial_\tau\); each \(\rho\) derivative at fixed \(s\) acts by \(\partial_\rho+s\partial_\tau\), as well as differentiating the leading \(\rho\). Other frequency derivatives are unchanged. Repeated product and chain rules give order \(\nu\), with all \(s\) derivatives of that same order, from \(\widetilde a\in S^{\nu-1}\). This proves both implications and finite seminorm control. Smooth angular cutoffs satisfy these estimates by the same differentiation, on a slightly larger cone. A smooth cutoff at bounded frequency introduces only a smooth kernel.

## P2. The actual kernel and its normalized FIO order

The change of variables gives the same distributional kernel:
\[
(2\pi)^{-n-1/2}\iint e^{i\Phi}a\,ds\,d\xi
=(2\pi)^{-n-1/2}\int e^{i\phi}\widetilde a\,d\theta.
\]
Here is a direct justification of the cutoff limits in this identity. Pair with a compactly supported smooth test function \(h(x,y)\). Since \(-\Delta_y e^{i\Phi}=|\xi|^2e^{i\Phi}\), integrating by parts \(N\) times in \(y\) changes the amplitude in the paired integral to
\(|\xi|^{-2N}(-\Delta_y)^N(ah)\).
There are no boundary terms. This expression has absolute value at most \(C_N\rho^{\nu-2N}\), with fixed compact \(x,y,s\) support. Choose \(2N>\nu+n\). Its integral in \(\xi\) is finite: on the cone, polar coordinates bound it by a constant times \(\int_1^\infty r^{\nu-2N+n-1}\,dr\). The earlier calculus proofs provide this change of variables and the convergence of that power integral.

Frequency cutoffs, whether expressed in \(\xi\) or \(\theta\), have a common bound and converge to one. They commute with the \(y\) integration by parts. The just established integrable bound therefore gives both limits and their equality by dominated convergence. At each finite cutoff the ordinary Jacobian formula applies; \(ds\,d\xi=\rho^{-1}d\tau\,d\xi\). This proves equality for every \(h\), and hence equality as distributions. Compact parameter support is essential to this argument; no noncompact Airy tail is included.

The base dimension for this kernel is \(d=2n\), and the number of homogeneous auxiliary variables is \(N=n+1\). The earlier normalized FIO convention requires amplitude order \(m+(d-2N)/4=m-\tfrac12\) and prefactor \((2\pi)^{-(d+2N)/4}=(2\pi)^{-n-1/2}\). By P1 the amplitude order is \(\nu-1\). Therefore
\[
\nu-1=m-\tfrac12
\quad\Longleftrightarrow\quad
\nu=m+\tfrac12.
\]
Together with P0 and the proved phase-integral construction, this places the kernel in \(I^m\) on the displayed relation. Order here means class membership; a vanishing or lower-order amplitude may also belong to smaller classes. This proof establishes precisely the order conversion needed in Theorem 6.2 of the descent lesson. Intrinsic critical half-densities, full lower-order Airy realization and continuity estimates require their separate proofs.

The source for the model and its order is Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV*, reprint of the corrected second printing (1994), §25.3. The explicit phase and Jacobian calculation also occur in the preserved AN-04 lessons *Canonical relations with two folding projections*, §5, and *Fold amplitudes and critical densities*, §1; their required arguments are proved above rather than assumed as later prerequisites.

*Companion assembled and completed by GPT-6 Astra (OpenAI), Ultra, 5 October 2026, from the preserved GPT-6.1 Sol course model and independent supporting arguments. Original exposition: CC0.*
