# Hörmander's L² estimates on pseudoconvex domains

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

To show that a \(\bar\partial\)-closed form is \(\bar\partial\)-exact on a whole domain, not only near each point, one needs a global method. L. Hörmander's method treats \(\bar\partial\) as a closed unbounded operator between weighted \(L^2\) spaces. An integration by parts shows that the weight \(e^{-\varphi}\) contributes the complex Hessian of \(\varphi\) to an a priori inequality; when \(\varphi\) is sufficiently strictly plurisubharmonic, the inequality gives existence of solutions with estimates, by the Riesz representation theorem. This lesson proves the resulting existence theorem on every open set of \(\mathbf C^n\) that has a smooth strictly plurisubharmonic exhaustion. The next lesson draws the consequences for holomorphic functions and coherent sheaves.

We use [Plurisubharmonic functions and Stein manifolds](plurisubharmonic-functions-and-stein-manifolds.md). From analysis we use Lebesgue integration, the space \(L^2\) and its completeness, convolution with mollifiers, and distributions on open subsets of \(\mathbf R^{2n}\), as in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), and the Riesz representation theorem for Hilbert spaces [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators).

Basic references are [Demailly] and [Hörmander 1965].

## 1. An abstract existence lemma

Let \(H_1,H_2,H_3\) be Hilbert spaces. A **densely defined operator** \(T:H_1\dashrightarrow H_2\) is a linear map defined on a dense subspace \(\operatorname{Dom}T\). Its **adjoint** \(T^*\) has as domain the set of \(f\in H_2\) for which \(x\mapsto\langle Tx,f\rangle\) is bounded on \(\operatorname{Dom}T\), and \(T^*f\) is the element with \(\langle Tx,f\rangle=\langle x,T^*f\rangle\) for all \(x\in\operatorname{Dom}T\). Directly from the definition, \(f\perp\operatorname{Im}T\) implies \(f\in\operatorname{Dom}T^*\) and \(T^*f=0\).

**Lemma 1.1.** Let \(T:H_1\dashrightarrow H_2\) and \(S:H_2\dashrightarrow H_3\) be densely defined, with \(\ker S\) closed and \(T(\operatorname{Dom}T)\subset\ker S\). Suppose that for some \(C>0\)

\[
\|T^*f\|^2+\|Sf\|^2\geq C\|f\|^2\qquad\text{for all } f\in\operatorname{Dom}T^*\cap\operatorname{Dom}S .
\tag{1.1}
\]

Then for every \(g\in\ker S\) there is \(u\in H_1\) with \(\|u\|^2\leq C^{-1}\|g\|^2\) and \(\langle u,T^*f\rangle=\langle g,f\rangle\) for all \(f\in\operatorname{Dom}T^*\).

**Proof.** Let \(f\in\operatorname{Dom}T^*\) and write \(f=f_1+f_2\) with \(f_1\in\ker S\) and \(f_2\perp\ker S\). As \(\operatorname{Im}T\subset\ker S\), \(f_2\perp\operatorname{Im}T\), so \(f_2\in\operatorname{Dom}T^*\) and \(T^*f_2=0\). Hence \(f_1\in\operatorname{Dom}T^*\cap\ker S\) and \(T^*f_1=T^*f\). Since \(g\in\ker S\perp f_2\), (1.1) applied to \(f_1\) gives

\[
|\langle g,f\rangle|=|\langle g,f_1\rangle|\leq\|g\|\,\|f_1\|\leq C^{-1/2}\|g\|\,\|T^*f_1\|=C^{-1/2}\|g\|\,\|T^*f\| .
\]

So \(T^*f\mapsto\langle f,g\rangle\) is a well-defined conjugate-linear functional on \(\operatorname{Im}T^*\) of norm at most \(C^{-1/2}\|g\|\). Extend it by continuity to the closure and by zero on the orthogonal complement; the Riesz representation theorem gives \(u\) with \(\langle T^*f,u\rangle=\langle f,g\rangle\) and \(\|u\|\leq C^{-1/2}\|g\|\). Conjugating gives the claim. \(\square\)

## 2. Weighted spaces and the operator \(\bar\partial\)

Let \(\Omega\subset\mathbf C^n\) be open and \(\varphi\) a real continuous function on \(\Omega\). Let \(L^2_{(0,q)}(\Omega,\varphi)\) be the Hilbert space of \((0,q)\)-forms \(f=\sum'_{|J|=q}f_J\,d\bar z_J\) with measurable coefficients and

\[
\|f\|_\varphi^2=\int_\Omega|f|^2e^{-\varphi}\,d\lambda,\qquad|f|^2={\sum_J}'|f_J|^2,
\]

where \(\sum'\) runs over increasing multi-indices and \(\lambda\) is Lebesgue measure. We extend the coefficients to all multi-indices so that they are alternating; then, for \(|K|=q-1\), \(f_{jK}\) is defined, and \(\sum'_J|f_J|^2=\frac1q\sum'_K\sum_j|f_{jK}|^2\).

Fix three continuous weights \(\varphi_1,\varphi_2,\varphi_3\). Let \(T:L^2_{(0,q-1)}(\Omega,\varphi_1)\dashrightarrow L^2_{(0,q)}(\Omega,\varphi_2)\) be \(\bar\partial\) in the sense of distributions, with domain the forms \(u\) for which \(\bar\partial u\) belongs to the target space, and let \(S:L^2_{(0,q)}(\Omega,\varphi_2)\dashrightarrow L^2_{(0,q+1)}(\Omega,\varphi_3)\) be defined in the same way. Both contain the smooth compactly supported forms \(\mathcal D_{(0,\bullet)}(\Omega)\) in their domains, so they are densely defined. \(\ker S\) is closed: if \(f_\nu\to f\) in \(L^2(\varphi_2)\) and \(\bar\partial f_\nu=0\), then \(\bar\partial f_\nu\to\bar\partial f\) as distributions, because \(L^2(\varphi_2)\)-convergence implies \(L^2\)-convergence on compact sets, where the weight is bounded. And \(S\circ T=0\) since \(\bar\partial^2=0\) for distributions.

Let now the weights be smooth. For \(u\in\mathcal D_{(0,q-1)}\) and \(f\in\mathcal D_{(0,q)}\), integration by parts gives \(\langle Tu,f\rangle_{\varphi_2}=\langle u,\vartheta f\rangle_{\varphi_1}\), where

\[
\vartheta f=-{\sum_K}'\sum_{j=1}^n e^{\varphi_1}\frac{\partial}{\partial z_j}\bigl(e^{-\varphi_2}f_{jK}\bigr)\,d\bar z_K .
\tag{2.1}
\]

Indeed, \(\langle\bar\partial u,f\rangle_{\varphi_2}=\sum'_K\sum_j\int(\partial u_K/\partial\bar z_j)\,\overline{f_{jK}}\,e^{-\varphi_2}d\lambda\) by expanding the coefficients of \(\bar\partial u\), and \(\int(\partial u_K/\partial\bar z_j)\,\overline F=-\int u_K\,\overline{\partial F/\partial z_j}\) for compactly supported smooth functions. Consequently \(\mathcal D_{(0,q)}\subset\operatorname{Dom}T^*\) with \(T^*f=\vartheta f\); and if \(f\in\operatorname{Dom}T^*\), then \(T^*f=\vartheta f\) in the sense of distributions, \(\vartheta\) being a first-order operator with smooth coefficients.

## 3. Density of compactly supported forms

Choose compact sets \(K_1\subset K_2\subset\cdots\) exhausting \(\Omega\), with \(K_\nu\) in the interior of \(K_{\nu+1}\), and smooth functions \(\eta_\nu\) with \(0\leq\eta_\nu\leq1\), \(\eta_\nu=1\) on \(K_\nu\) and support in the interior of \(K_{\nu+1}\). The support of \(\bar\partial\eta_\nu\) lies in \(K_{\nu+1}\setminus K_\nu\), and these sets are disjoint for different \(\nu\). Hence \(M=1+\sup_\nu\sum_k|\partial\eta_\nu/\partial\bar z_k|^2\) is locally bounded, and there is \(\psi\in\mathcal C^\infty(\Omega,\mathbf R)\) with \(e^\psi\geq M\): majorize the locally bounded function \(\log M\) by \(\sum_\alpha c_\alpha\chi_\alpha\) for a smooth partition of unity \((\chi_\alpha)\) with compact supports, with \(c_\alpha\) the supremum of \(\log M\) on the support of \(\chi_\alpha\). We fix \(\eta_\nu\) and \(\psi\), so that

\[
\sum_{k=1}^n\Bigl|\frac{\partial\eta_\nu}{\partial\bar z_k}\Bigr|^2\leq e^{\psi}\qquad\text{for all }\nu .
\tag{3.1}
\]

From now on, for a smooth real function \(\varphi\), the three weights are

\[
\varphi_1=\varphi-2\psi,\qquad\varphi_2=\varphi-\psi,\qquad\varphi_3=\varphi .
\tag{3.2}
\]

**Lemma 3.1 (Friedrichs).** Let \(P=\sum_ka_k\,\partial/\partial x_k+b\) be a first-order operator on an open set of \(\mathbf R^m\) with \(a_k\in\mathcal C^1\) and \(b\) continuous, let \(v\in L^2\) have compact support in it, and let \(\rho_\varepsilon(x)=\varepsilon^{-m}\rho(x/\varepsilon)\) be a mollifier. Then \(P(v*\rho_\varepsilon)-(Pv)*\rho_\varepsilon\to0\) in \(L^2\) as \(\varepsilon\to0\), where \(Pv\) is computed in the sense of distributions.

**Proof.** The term \(b\) causes no difficulty, since \(b(v*\rho_\varepsilon)\) and \((bv)*\rho_\varepsilon\) both tend to \(bv\). For \(P=a\,\partial/\partial x_k\), an integration by parts gives

\[
w_\varepsilon(x)=P(v*\rho_\varepsilon)(x)-(Pv)*\rho_\varepsilon(x)=\int\Bigl(\bigl(a(x)-a(x-\varepsilon y)\bigr)\,\varepsilon^{-1}\partial_k\rho(y)+\partial_ka(x-\varepsilon y)\,\rho(y)\Bigr)\,v(x-\varepsilon y)\,dy .
\]

With \(C\) a bound for \(|da|\) near the support of \(v\), \(|w_\varepsilon(x)|\leq C\int|v(x-\varepsilon y)|\,(|y|\,|\partial_k\rho(y)|+\rho(y))\,dy\), so \(\|w_\varepsilon\|_{L^2}\leq C'\|v\|_{L^2}\) uniformly in \(\varepsilon\). For smooth \(v\), \(w_\varepsilon\to0\) uniformly with supports in a fixed compact set. Since smooth compactly supported functions are dense in \(L^2\) and the operators \(v\mapsto w_\varepsilon\) are uniformly bounded, \(w_\varepsilon\to0\) for every \(v\). \(\square\)

**Lemma 3.2.** With the weights (3.2), \(\mathcal D_{(0,q)}(\Omega)\) is dense in \(\operatorname{Dom}T^*\cap\operatorname{Dom}S\) for the graph norm \(\|f\|_{\varphi_2}+\|T^*f\|_{\varphi_1}+\|Sf\|_{\varphi_3}\).

**Proof.** *Cut-off.* Let \(f\in\operatorname{Dom}T^*\cap\operatorname{Dom}S\). Then \(\eta_\nu f\to f\) in \(L^2(\varphi_2)\) by dominated convergence. In the sense of distributions \(S(\eta_\nu f)=\eta_\nu Sf+\bar\partial\eta_\nu\wedge f\), and by (3.1)

\[
\|\bar\partial\eta_\nu\wedge f\|^2_{\varphi_3}\leq\int_{\Omega\setminus K_\nu}|f|^2e^{\psi-\varphi}\,d\lambda=\int_{\Omega\setminus K_\nu}|f|^2e^{-\varphi_2}\,d\lambda\longrightarrow0 .
\]

For \(T^*\): for \(u\in\operatorname{Dom}T\), \(\eta_\nu u\in\operatorname{Dom}T\) and \(\langle Tu,\eta_\nu f\rangle_{\varphi_2}=\langle T(\eta_\nu u),f\rangle_{\varphi_2}-\langle\bar\partial\eta_\nu\wedge u,f\rangle_{\varphi_2}\), which is bounded in \(\|u\|_{\varphi_1}\); so \(\eta_\nu f\in\operatorname{Dom}T^*\) with

\[
T^*(\eta_\nu f)=\eta_\nu T^*f-e^{\varphi_1-\varphi_2}{\sum_K}'\sum_j\frac{\partial\eta_\nu}{\partial z_j}f_{jK}\,d\bar z_K ,
\]

and the last term has \(L^2(\varphi_1)\)-norm squared at most \(q\int_{\Omega\setminus K_\nu}|\partial\eta_\nu|^2|f|^2e^{-2\psi}e^{-\varphi+2\psi}\leq q\int_{\Omega\setminus K_\nu}|f|^2e^{-\varphi_2}\to0\), since \(|\partial\eta_\nu/\partial z_j|=|\partial\eta_\nu/\partial\bar z_j|\) for real \(\eta_\nu\), \(|\sum_j\alpha_jf_{jK}|^2\leq|\alpha|^2\sum_j|f_{jK}|^2\), and \(\sum'_K\sum_j|f_{jK}|^2=q|f|^2\). So we may assume \(f\) has compact support.

*Mollification.* For \(f\) with compact support, let \(f_\varepsilon=f*\rho_\varepsilon\), coefficientwise; for small \(\varepsilon\) these forms lie in \(\mathcal D_{(0,q)}\) with supports in a fixed compact set, on which all weights are bounded above and below, so all weighted norms are equivalent to unweighted ones there. Then \(f_\varepsilon\to f\), \(Sf_\varepsilon=(Sf)*\rho_\varepsilon\to Sf\) because \(\bar\partial\) has constant coefficients, and \(T^*f_\varepsilon=\vartheta f_\varepsilon\to\vartheta f=T^*f\) by Lemma 3.1 applied to the first-order operator \(\vartheta\). \(\square\)

## 4. The basic identity

For a smooth real function \(\varphi\) put \(\delta_jw=e^\varphi\,\partial(e^{-\varphi}w)/\partial z_j=\partial w/\partial z_j-(\partial\varphi/\partial z_j)\,w\), and write \(\varphi_{j\bar k}=\partial^2\varphi/\partial z_j\partial\bar z_k\).

**Lemma 4.1 (Morrey–Kohn–Hörmander identity).** For every \(f\in\mathcal D_{(0,q)}(\Omega)\),

\[
{\sum_K}'\int\Bigl|\sum_j\delta_jf_{jK}\Bigr|^2e^{-\varphi}+\int|\bar\partial f|^2e^{-\varphi}
={\sum_J}'\sum_k\int\Bigl|\frac{\partial f_J}{\partial\bar z_k}\Bigr|^2e^{-\varphi}+{\sum_K}'\sum_{j,k}\int\varphi_{j\bar k}\,f_{jK}\overline{f_{kK}}\,e^{-\varphi}.
\tag{4.1}
\]

**Proof.** Expanding the coefficients of \(\bar\partial f=\sum'_J\sum_j(\partial f_J/\partial\bar z_j)\,d\bar z_j\wedge d\bar z_J\) with the alternating convention, the terms with repeated indices cancel and one obtains the pointwise identity

\[
|\bar\partial f|^2={\sum_J}'\sum_j\Bigl|\frac{\partial f_J}{\partial\bar z_j}\Bigr|^2-{\sum_K}'\sum_{j,k}\frac{\partial f_{kK}}{\partial\bar z_j}\,\overline{\frac{\partial f_{jK}}{\partial\bar z_k}} .
\tag{4.2}
\]

For compactly supported smooth \(v,w\), \(\int(\partial w/\partial\bar z_k)\,\bar v\,e^{-\varphi}=-\int w\,\overline{\delta_kv}\,e^{-\varphi}\), and the commutator is \(\delta_k(\partial v/\partial\bar z_j)-\partial(\delta_kv)/\partial\bar z_j=\varphi_{k\bar j}v\). Hence

\[
\int\frac{\partial f_{jK}}{\partial\bar z_k}\,\overline{\frac{\partial f_{kK}}{\partial\bar z_j}}\,e^{-\varphi}
=-\int f_{jK}\,\overline{\frac{\partial(\delta_kf_{kK})}{\partial\bar z_j}+\varphi_{k\bar j}f_{kK}}\,e^{-\varphi}
=\int\delta_jf_{jK}\,\overline{\delta_kf_{kK}}\,e^{-\varphi}-\int\varphi_{j\bar k}f_{jK}\overline{f_{kK}}\,e^{-\varphi},
\]

using \(\int g\,\overline{\partial h/\partial\bar z_j}\,e^{-\varphi}=-\int\delta_jg\,\bar h\,e^{-\varphi}\) and \(\overline{\varphi_{k\bar j}}=\varphi_{j\bar k}\). The sum of the left side over all \(j,k\) is unchanged when the names \(j\) and \(k\) are exchanged, so summing over \(j,k\) and \(K\) computes the integral of the last term of (4.2); substituting into the integral of (4.2) gives (4.1). \(\square\)

The first term of (4.1) is \(\|\vartheta_\varphi f\|^2_\varphi\), where \(\vartheta_\varphi\) is (2.1) with \(\varphi_1=\varphi_2=\varphi\). With the weights (3.2), (2.1) becomes \(e^{\psi}T^*f=\vartheta_\varphi f-\sum'_K\sum_j(\partial\psi/\partial z_j)f_{jK}\,d\bar z_K\), so that, with \(|\partial\psi|^2=\sum_j|\partial\psi/\partial z_j|^2\),

\[
\|\vartheta_\varphi f\|^2_\varphi\leq2\int|e^{\psi}T^*f|^2e^{-\varphi}+2q\int|\partial\psi|^2|f|^2e^{-\varphi}=2\|T^*f\|^2_{\varphi_1}+2q\int|\partial\psi|^2|f|^2e^{-\varphi}.
\tag{4.3}
\]

## 5. The existence theorem

Write \(\lambda_\varphi(z)\) for the smallest eigenvalue of the complex Hessian of \(\varphi\) at \(z\).

**Theorem 5.1.** Let \(\Omega\subset\mathbf C^n\) be open, let \(\psi\) be as in (3.1), and let \(\varphi\in\mathcal C^\infty(\Omega,\mathbf R)\) satisfy

\[
\lambda_\varphi\geq2|\partial\psi|^2+2e^{\psi}\qquad\text{on }\Omega .
\tag{5.1}
\]

Let \(q\geq1\). For every \(g\in L^2_{(0,q)}(\Omega,\varphi-\psi)\) with \(\bar\partial g=0\) in the sense of distributions there is \(u\in L^2_{(0,q-1)}(\Omega,\varphi-2\psi)\) with \(\bar\partial u=g\) in the sense of distributions and

\[
\int_\Omega|u|^2e^{-\varphi+2\psi}\,d\lambda\leq\int_\Omega|g|^2e^{-\varphi+\psi}\,d\lambda .
\tag{5.2}
\]

**Proof.** For \(f\in\mathcal D_{(0,q)}\), the Hermitian form in the last term of (4.1) satisfies \(\sum'_K\sum_{j,k}\varphi_{j\bar k}f_{jK}\overline{f_{kK}}\geq\lambda_\varphi\sum'_K\sum_j|f_{jK}|^2=q\lambda_\varphi|f|^2\). Dropping the nonnegative first term on the right of (4.1) and using (4.3) and \(\|Sf\|_{\varphi_3}=\|\bar\partial f\|_\varphi\):

\[
2\|T^*f\|^2_{\varphi_1}+\|Sf\|^2_{\varphi_3}\geq q\int\bigl(\lambda_\varphi-2|\partial\psi|^2\bigr)|f|^2e^{-\varphi}\geq2q\int|f|^2e^{\psi-\varphi}\geq2\|f\|^2_{\varphi_2}
\]

by (5.1). Hence \(\|T^*f\|^2_{\varphi_1}+\|Sf\|^2_{\varphi_3}\geq\|f\|^2_{\varphi_2}\) on \(\mathcal D_{(0,q)}\), and by Lemma 3.2 on all of \(\operatorname{Dom}T^*\cap\operatorname{Dom}S\). Lemma 1.1 with \(C=1\) gives \(u\) with \(\|u\|_{\varphi_1}\leq\|g\|_{\varphi_2}\), which is (5.2), and \(\langle u,T^*f\rangle_{\varphi_1}=\langle g,f\rangle_{\varphi_2}\) for all \(f\in\operatorname{Dom}T^*\). Taking \(f\in\mathcal D_{(0,q)}\), where \(T^*f=\vartheta f\) is given by (2.1), this says that \(\bar\partial u=g\) in the sense of distributions. \(\square\)

**Corollary 5.2.** Let \(\Omega\subset\mathbf C^n\) have a smooth strictly plurisubharmonic exhaustion \(\psi_0\), and let \(\psi\) be as in (3.1).

1. For every continuous function \(m\) on \(\Omega\) there is a convex increasing smooth function \(\chi\) such that \(\varphi=\chi\circ\psi_0\) satisfies (5.1) and \(\varphi\geq m\). If \(\varphi\) satisfies (5.1), so does \(\varphi+\theta\circ\psi_0\) for every convex nondecreasing smooth \(\theta\).
2. (Hörmander) For \(q\geq1\), every \((0,q)\)-form \(g\) with locally square integrable coefficients and \(\bar\partial g=0\) in the sense of distributions is \(\bar\partial u\) for a \((0,q-1)\)-form \(u\) with locally square integrable coefficients.

**Proof.** (1) Let \(\mu(t)=\min\{\lambda_{\psi_0}(z):\ \psi_0(z)\leq t\}>0\) and \(M(t)=\max\{2|\partial\psi|^2+2e^\psi:\ \psi_0\leq t\}\), using compactness of the sublevel sets. Choose \(\chi\) smooth, convex and increasing with \(\chi'(t)\mu(t)\geq M(t)\) and \(\chi(\psi_0(z))\geq m(z)\); for instance \(\chi\) with \(\chi'\) increasing and larger than \(M/\mu\) and than the slopes needed to dominate \(\max\{m:\ \psi_0\leq t\}\). By Lemma 1.2 of the previous lesson, \(\lambda_{\chi\circ\psi_0}\geq\chi'(\psi_0)\lambda_{\psi_0}\geq M(\psi_0)\), which gives (5.1). Adding \(\theta\circ\psi_0\) adds a positive semidefinite form to the Hessian, by the same lemma.

(2) In (1), choose \(\chi\) so that in addition \(\chi(\nu-1)\geq\nu-1+\log\bigl(1+\int_{\{\psi_0\leq\nu\}}|g|^2e^{\psi}\,d\lambda\bigr)\) for every integer \(\nu\), which is a countable family of lower bounds on an increasing function. On the compact shell \(\{\nu-1\leq\psi_0<\nu\}\) we have \(e^{-\chi\circ\psi_0}\leq e^{-\chi(\nu-1)}\), so the integral of \(|g|^2e^{\psi-\varphi}\) over the shell is at most \(e^{-(\nu-1)}\), and \(g\in L^2(\varphi-\psi)\). Theorem 5.1 gives \(u\in L^2(\varphi-2\psi)\), which has locally square integrable coefficients. \(\square\)

*Reference:* [Hörmander 1965] introduced the method and the three weights (3.2); the presentation of Section 1 follows [Demailly].

## 6. Exercises

**Exercise 6.1.** Let \(T=d/dx\) on \(L^2(0,1)\) with domain the functions with square integrable derivative. Show that \(T^*=-d/dx\) with domain the functions in this space vanishing at \(0\) and \(1\), so that \(T^*\) is not the formal adjoint on its natural maximal domain.

*Solution.* For \(u\) in the domain of \(T\) and smooth \(f\) on \([0,1]\), \(\langle u',f\rangle=-\langle u,f'\rangle+u(1)\bar f(1)-u(0)\bar f(0)\). The functional \(u\mapsto\langle u',f\rangle\) is bounded in \(\|u\|\) exactly when the boundary terms vanish for all \(u\), that is, \(f(0)=f(1)=0\); by density this describes \(\operatorname{Dom}T^*\), and then \(T^*f=-f'\). The boundary conditions are the reason for the cut-offs of Lemma 3.2.

**Exercise 6.2.** In \(\mathbf C\) (so \(q=1\) is the only case), verify (4.1) for \(f=g\,d\bar z\) with \(g\in\mathcal D(\Omega)\).

*Solution.* Here \(K=\emptyset\), \(f_1=g\), \(\bar\partial f=0\), and (4.1) reads \(\int|\delta g|^2e^{-\varphi}=\int|\partial g/\partial\bar z|^2e^{-\varphi}+\int\varphi_{z\bar z}|g|^2e^{-\varphi}\) with \(\delta g=\partial g/\partial z-\varphi_zg\). This follows from \(\int(\partial g/\partial\bar z)\overline{(\partial g/\partial\bar z)}e^{-\varphi}=-\int g\,\overline{\delta(\partial g/\partial\bar z)}e^{-\varphi}=-\int g\,\overline{\partial(\delta g)/\partial\bar z+\varphi_{z\bar z}g}\,e^{-\varphi}=\int|\delta g|^2e^{-\varphi}-\int\varphi_{z\bar z}|g|^2e^{-\varphi}\), the computation of Lemma 4.1 with one index.

**Exercise 6.3.** Show that a weight is needed: there is a smooth compactly supported function \(g\) on \(\mathbf C\) for which \(\partial u/\partial\bar z=g\) has no solution \(u\in L^2(\mathbf C)\).

*Solution.* Let \(g\geq0\) be smooth with support in \(\{|z|<1\}\) and \(\int g\,d\lambda=1\), and suppose \(u\in L^2(\mathbf C)\) solves the equation. With \(v=-\frac1\pi\int g(\zeta)(\zeta-z)^{-1}d\lambda(\zeta)\), which is smooth with \(\partial v/\partial\bar z=g\) by [The Dolbeault complex, Lemma 2.1](the-dolbeault-complex.md#2-the-dolbeault-grothendieck-lemma), \(u-v\) satisfies \(\partial(u-v)/\partial\bar z=0\) in the sense of distributions, so it is holomorphic (next lesson, Lemma 1.2), and \(u\) is smooth. On \(\{|z|>1\}\), \(u\) is holomorphic with a Laurent expansion \(\sum_ka_kz^k\). By orthogonality of the powers on circles, \(\int_{|z|>1}|u|^2d\lambda=\sum_k|a_k|^2\int_{|z|>1}|z|^{2k}d\lambda\), and the integrals are infinite for \(k\geq-1\); so \(a_{-1}=0\). But by Green's formula, for \(R>1\), \(\int_{|z|=R}u\,dz=\int_{|z|<R}\frac{\partial u}{\partial\bar z}\,d\bar z\wedge dz=2i\int g\,d\lambda=2i\), so \(a_{-1}=\frac1{2\pi i}\int_{|z|=R}u\,dz=\frac1\pi\neq0\), a contradiction.

## References

- [Demailly] J.-P. Demailly, *Complex Analytic and Differential Geometry*, version of 21 June 2012, freely available from the author with permission to copy, modify and redistribute with credit. <https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf>
- [Hörmander 1965] L. Hörmander, \(L^2\) estimates and existence theorems for the \(\bar\partial\) operator, *Acta Mathematica* 113 (1965), 89–152. <https://doi.org/10.1007/BF02391775>
