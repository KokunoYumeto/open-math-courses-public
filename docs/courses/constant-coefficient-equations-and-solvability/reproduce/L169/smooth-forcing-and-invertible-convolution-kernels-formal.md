# Smooth forcing, invertible kernels and support confinement

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Solvability for analytic forcing holds for every nonzero compact kernel. Solvability for every compact smooth forcing requires an invertible kernel. Solvability for every smooth forcing also confines transpose-test supports whenever their convolutions stay in a fixed compact set. We prove both necessary conditions on arbitrary compatible open domains. One complete-space argument supplies their common bilinear estimate.

Basic references are [Grubb's Fourier-distribution notes](https://web.math.ku.dk/~grubb/dist5.pdf), [Melrose's tempered-distribution notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf), and Hörmander's *The Analysis of Linear Partial Differential Operators*, volumes I and II. The exact earlier mathematical inputs are Theorem 1.1 of Frequency-selective singularities and smooth convolutions, including its prescribed center and arbitrarily small support radius, and Theorem 1.1 and Definition 6.1 of Slow decrease and entire Fourier division. The complete-metric Baire theorem and completeness of both fixed-support tests and \(C^\infty(X_2)\) are proved in Sections 6 and 14.2 of Banach estimates, quotient spaces and compact parameter arguments. The exact Fourier inversion on Schwartz tests is Theorem 1.1 of Fourier transforms, finite spectra and convex separation. Smooth cutoffs are supplied by Section 13.10 of Metric and topological foundations.

## 1. Compatible domains and the necessary condition

Let \(\mu\in\mathcal E'(\mathbb R^n)\), \(n\ge1\), and let \(X_1,X_2\) be nonempty open sets satisfying
\[
 X_2-\operatorname{supp}\mu\subset X_1.
 \tag{1.1}
\]
Then \(\mu*u\) is defined as a distribution on \(X_2\) for every \(u\in\mathcal D'(X_1)\). Write \(\check\mu(\phi)=\mu(\phi(-\,\cdot))\). The transpose identity is
\[
 \langle\mu*u,\phi\rangle=\langle u,\check\mu*\phi\rangle,
 \qquad \phi\in C_c^\infty(X_2).
 \tag{1.2}
\]
Indeed the support of \(\check\mu*\phi\) is contained in the compact set
\(\operatorname{supp}\phi-\operatorname{supp}\mu\subset X_1\). Changing \(x-y\) to a new variable gives (1.2) for smooth \(u\); the same finite-order compact-kernel transpose defines the convolution for a distribution \(u\). It needs no convexity of either domain.

**Theorem 1.1.** Suppose that for every \(f\in C_c^\infty(X_2)\), there is a \(u_f\in\mathcal D'(X_1)\) with
\[
 \mu*u_f=f\quad\hbox{in }X_2 .
 \tag{1.3}
\]
Then \(\mu\) is invertible. Equivalently, its Fourier transform \(F_\mu\) obeys, for some \(A>0\),
\[
 \sup_{\substack{\zeta\in\mathbb C^n\\
       |\zeta-c|<A\log(2+|c|)}}|F_\mu(\zeta)|>(A+|c|)^{-A}
            \quad(c\in\mathbb R^n).
 \tag{1.4}
\]
This necessity does not assert that invertibility alone suffices on every compatible domain. It uses only compact smooth forcing, and allows arbitrary distributional solutions.

The hypothesis implies \(\mu\ne0\): if \(\mu=0\), its convolution is zero, whereas the nonempty open set \(X_2\) has a nonzero smooth compact bump. We assume \(\mu\ne0\) below.

## 2. A common bilinear estimate

We first isolate the complete-space argument.

**Lemma 2.1 (one complete variable).** Let \(F\) be a Fréchet space with increasing defining seminorms \(q_N\), and let \(V\) be a vector space with increasing seminorms \(p_M\). Suppose \(B:F\times V\to\mathbb C\) is bilinear, continuous in \(f\) for every fixed \(v\), and for every fixed \(f\) has a bound
\(|B(f,v)|\le C_f p_{M_f}(v)\). Then for some \(C,N,M\),
\[
 |B(f,v)|\le C q_N(f)p_M(v).
 \tag{2.0}
\]
Completeness of \(V\), or even separation by its seminorms, is unnecessary.

*Proof.* For integers \(m\ge1\), define \(E_m\) by \(|B(f,v)|\le m p_m(v)\) for every \(v\). Each is closed in \(F\), by the assumed continuity in \(f\), and they cover \(F\) by increasing \(m\) to dominate \(C_f,M_f\). Baire gives some \(E_m\) with interior. A finite-seminorm neighborhood in that interior contains \(f_0+\{h:q_N(h)<\delta\}\), since the seminorms increase. Subtract the inequalities at \(f_0+h\) and \(f_0\) to get \(|B(h,v)|\le2m p_m(v)\) for \(q_N(h)<\delta\). Rescale \(h=\delta f/(2q_N(f))\) when \(q_N(f)>0\). When \(q_N(f)=0\), apply the bound to arbitrarily large multiples of \(f\), obtaining \(B(f,v)=0\). This proves (2.0) with \(C=4m/\delta\), \(M=m\). The zero first space is immediate. \(\square\)

For a compact \(K\subset X_2\), let
\[
 \mathcal D_K=\{\phi\in C^\infty(\mathbb R^n):
                \operatorname{supp}\phi\subset K\},\qquad
 q_N(f)=\max_{|\alpha|\le N}\sup_{\mathbb R^n}|\partial^\alpha f|,
 \quad
 p_M(v)=\max_{|\beta|\le M}\sup_{\mathbb R^n}
                       |\partial^\beta(\check\mu*v)|.
 \tag{2.1}
\]
The \(q_N\) are increasing and define the complete fixed-support Fréchet topology. The \(p_M\) are finite increasing seminorms on the second copy of \(\mathcal D_K\). Completeness in that second topology will not be used.

**Corollary 2.2 (fixed-support test estimate).** Under (1.3), there are \(C<\infty\) and integers \(N,M\ge0\), depending on \(K\), such that
\[
 \left|\int f(x)v(x)\,dx\right|\le C q_N(f)p_M(v)
                  \quad(f,v\in\mathcal D_K).
 \tag{2.2}
\]

*Proof.* Put \(B(f,v)=\int fv\). For fixed \(v\), this is continuous in the \(q_N\) topology on the first variable: \(|B(f,v)|\le q_0(f)\|v\|_1\).

For fixed \(f\), choose the solution \(u_f\). Formula (1.2) gives
\[
 B(f,v)=u_f(\check\mu*v).
 \tag{2.3}
\]
All its tests have support in the single compact set \(K-\operatorname{supp}\mu\subset X_1\). Distributional continuity on a fixed compact set bounds (2.3) by \(C_f p_{M_f}(v)\) for some finite \(C_f\) and \(M_f\). Constants and orders may initially depend on \(f\); the next step removes that dependence.

Lemma 2.1 now applies with the complete first copy of \(\mathcal D_K\) and the indicated seminorms on the second copy. It gives (2.2). No linear choice or continuous dependence of the solutions \(u_f\) has been assumed. \(\square\)

## 3. Smooth outputs force a common distributional order

**Lemma 3.1.** Let \(w\) be a compact distribution whose support lies in the interior of \(K\), and suppose \(\check\mu*w\) is smooth. Under the estimate (2.2), \(w\) is smooth.

*Proof.* Choose a nonnegative \(\chi\in C_c^\infty(\mathbb R^n)\) supported in the unit ball, with integral one, and put
\(\chi_\varepsilon(x)=\varepsilon^{-n}\chi(x/\varepsilon)\). For sufficiently small \(\varepsilon>0\), \(w_\varepsilon=w*\chi_\varepsilon\) belongs to \(\mathcal D_K\). Compactness of \(\operatorname{supp}w\) inside \(\operatorname{int}K\) supplies the required fixed gap.

Set \(g=\check\mu*w\). This is compactly supported and smooth. For every multi-index \(\gamma\),
\[
 \check\mu*\partial^\gamma w_\varepsilon
       =(\partial^\gamma g)*\chi_\varepsilon,\qquad
 p_M(\partial^\gamma w_\varepsilon)
       \le \max_{|\beta|\le M}\|\partial^{\beta+\gamma}g\|_\infty
       =:C_\gamma<\infty .
 \tag{3.1}
\]
The positive mollifier has \(L^1\) norm one, which proves the estimate. Compact convolution and differentiation commute by the finite-order pairing and ordinary differentiation of its test.

Apply (2.2) with \(v=\partial^\gamma w_\varepsilon\):
\[
 \left|\int f\,\partial^\gamma w_\varepsilon\right|
       \le C C_\gamma q_N(f)\quad(f\in\mathcal D_K).
 \tag{3.2}
\]
Mollifiers converge to the identity on every compact-distribution test pairing: the convolved test and its derivatives converge uniformly on a fixed compact neighborhood of \(\operatorname{supp}w\). Hence \(\partial^\gamma w_\varepsilon\to\partial^\gamma w\) distributionally. Taking the limit in (3.2) gives the same bound for \((\partial^\gamma w)(f)\). Its order \(N\) is independent of \(\gamma\).

Choose \(\eta\in C_c^\infty(\operatorname{int}K)\) equal to one near \(\operatorname{supp}w\). All distributional derivatives of \(w\) have support there. The Leibniz rule bounds
\[
 q_N(\eta f)\le C_\eta\max_{|\alpha|\le N}
                       \sup_{\operatorname{supp}\eta}|\partial^\alpha f|.
 \tag{3.3}
\]
Thus the derivative distribution can be tested on an arbitrary smooth \(f\) by inserting \(\eta\), with a bound of the same order \(N\).

Use \(f(x)=e^{-ix\cdot\xi}\), \(\xi\in\mathbb R^n\). Fourier differentiation and (3.3) give
\[
 |\xi^\gamma F_w(\xi)|=|F_{\partial^\gamma w}(\xi)|
       \le C'_\gamma(1+|\xi|)^N .
 \tag{3.4}
\]
For any integer \(r\ge0\), take \(\gamma=(N+r)e_k\), \(k=1,\ldots,n\). At every \(|\xi|\ge1\), choose \(k\) with \(|\xi_k|\ge|\xi|/\sqrt n\). The finite maximum of the corresponding constants then yields
\[
 |F_w(\xi)|\le C_r(1+|\xi|)^{-r}.
 \tag{3.5}
\]
Bounded frequencies are included by increasing \(C_r\), since \(F_w\) is continuous. The order \(N\) remains fixed while \(\gamma\) becomes arbitrarily large.

For every multi-index \(\alpha\), choose \(r>n+|\alpha|\) in (3.5). Then \(\xi^\alpha F_w(\xi)\) is integrable. Fourier inversion defines
\[
 W(x)=(2\pi)^{-n}\int_{\mathbb R^n}
                     e^{ix\cdot\xi}F_w(\xi)\,d\xi ,
 \tag{3.6}
\]
with every derivative obtained by an absolutely convergent integral. Dominated convergence makes these derivatives continuous, so \(W\) is smooth. To identify it with \(w\), take a compact smooth test \(\phi\). The linked Schwartz inversion theorem writes
\[
 \phi(x)=(2\pi)^{-n}\int e^{-ix\cdot\xi}F_\phi(-\xi)\,d\xi.
 \tag{3.7}
\]
Its integral and every finite number of spatial derivatives converge uniformly near the support of \(w\), because \(F_\phi\) decays rapidly. Finite-order continuity therefore permits applying \(w\) inside that integral, yielding
\[
 w(\phi)=(2\pi)^{-n}\int F_w(\xi)F_\phi(-\xi)\,d\xi
                         =\int W(x)\phi(x)\,dx.
 \tag{3.8}
\]
The last equality follows from integrability and Fubini in (3.6). Thus \(w=W\) distributionally and is smooth. The argument does not require an additional negative-Sobolev regularity theorem. \(\square\)

## 4. Excluding a localized smoothing factor

*Proof of Theorem 1.1.* Reflection preserves slow decrease: \(F_{\check\mu}(\zeta)=F_\mu(-\zeta)\), and the map \((c,\zeta)\mapsto(-c,-\zeta)\) preserves the radius and lower bound in (1.4). Thus \(\mu\) is invertible exactly when \(\check\mu\) is invertible.

Suppose \(\mu\) were not invertible. The full equivalence in Theorem 1.1 of Slow decrease and entire Fourier division supplies a collapsed profile for \(\check\mu\). Theorem 1.1 of Frequency-selective singularities and smooth convolutions then gives the following at any chosen \(x_0\in X_2\) and any sufficiently small \(a>0\): a compact continuous \(w\), supported in \(\overline B_a(x_0)\), singular only at \(x_0\), not of class \(C^1\), with
\[
 \check\mu*w\in C^\infty(\mathbb R^n).
 \tag{4.1}
\]
Choose \(a\) so \(\overline B_{2a}(x_0)\subset X_2\), and take \(K=\overline B_{2a}(x_0)\). The support of \(w\) lies in its interior. Corollary 2.2 supplies the common test estimate on this exact \(K\), and Lemma 3.1 applied to (4.1) makes \(w\) smooth. This contradicts its failure to be \(C^1\).

Consequently \(\check\mu\), and hence \(\mu\), is invertible. The slow-decrease equivalence gives (1.4). This proves the full necessity theorem for every compatible pair of nonempty open domains. \(\square\)

## 5. Support confinement for arbitrary smooth forcing

**Theorem 5.1.** Strengthen the solvability hypothesis to every \(f\in C^\infty(X_2)\). Then for every compact \(K_1\subset X_1\), there is a compact \(K_2\subset X_2\) such that
\[
 v\in C_c^\infty(X_2),\quad
       \operatorname{supp}(\check\mu*v)\subset K_1
       \quad\Longrightarrow\quad
       \operatorname{supp}v\subset K_2.
 \tag{5.1}
\]
The conclusion concerns smooth compact tests. It is not an assertion that the same solution estimates hold for arbitrary distributional tests.

*Proof.* Take \(F=C^\infty(X_2)\) with increasing compact derivative seminorms from a compact exhaustion, and take
\[
 V=\{v\in C_c^\infty(X_2):
                  \operatorname{supp}(\check\mu*v)\subset K_1\},\qquad
 p_M(v)=\max_{|\beta|\le M}\sup_{\mathbb R^n}
                         |\partial^\beta(\check\mu*v)|.
 \tag{5.2}
\]
This is a vector space with increasing seminorms. Its completeness is not needed. For fixed \(v\), the map \(f\mapsto\int fv\) is continuous on \(C^\infty(X_2)\), bounded by a supremum on the compact support of \(v\). For fixed \(f\), its solution \(u_f\) and the transpose identity give
\[
 \int fv=u_f(\check\mu*v),\qquad
                  \left|\int fv\right|\le C_f p_{M_f}(v).
 \tag{5.3}
\]
Here all tests for \(u_f\) have support in the fixed \(K_1\). Apply Lemma 2.1 to the complete first space. One resulting seminorm has the form
\[
 q_N(f)=\max_{|\alpha|\le N}\sup_{K_2}|\partial^\alpha f|,
 \quad\hbox{for one compact }K_2\subset X_2,
 \qquad
 \left|\int fv\right|\le Cq_N(f)p_M(v).
 \tag{5.4}
\]
Finite unions of the compact sets in finitely many initial seminorms give such a compact \(K_2\); increasing the order gives the stated maximum.

If an admissible \(v\) were nonzero at some \(x_0\in X_2\setminus K_2\), choose a nonnegative smooth bump \(\theta\) supported in a small ball there, with \(\theta(x_0)>0\). The smooth compact function \(f=\theta\overline v\) has \(q_N(f)=0\), but
\[
 \int fv=\int\theta|v|^2>0,
 \tag{5.5}
\]
contradicting (5.4). Thus \(v\) is zero off \(K_2\), and its support is contained in the closed set \(K_2\). This proves (5.1), including \(V=\{0\}\) and empty \(K_1\). \(\square\)

Compact smooth forcing sufficed for Theorem 1.1. The complete space \(C^\infty(X_2)\) in Theorem 5.1 requires solvability for every smooth forcing. A function that grows without bound near the boundary can detect a domain obstruction that compact forcing misses.

## References

- Gerd Grubb, *Distributions and Operators*, Chapter 5, “Fourier transformation of distributions,” freely readable [lecture notes](https://web.math.ku.dk/~grubb/dist5.pdf).
- Richard B. Melrose, *Introduction to Microlocal Analysis*, MIT, 2007, Chapter 1, “Tempered distributions and the Fourier transform,” freely readable [notes](https://math.mit.edu/~rbm/iml/Chapter1.pdf).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, second edition, Springer, 1990.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983.
- The exact previously proved isolated-smoothing-factor and slow-decrease equivalences are linked in the introduction. The Baire level-set argument, common-order regularization and rapid Fourier decay are proved here.
