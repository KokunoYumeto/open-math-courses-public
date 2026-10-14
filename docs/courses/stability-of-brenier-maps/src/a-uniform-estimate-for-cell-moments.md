# A uniform estimate for cell moments

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the central estimate of the course. Fix distinct sites and intercepts whose Laguerre cells, as in [Laguerre cells and prescribed masses](laguerre-cells-and-prescribed-masses.md), all have positive mass. When the intercepts move in a direction \(q\) and the sites stay fixed, the first moments of the cells change by at most a constant multiple of the change of their masses, in the weighted quadratic norm:
\[
\begin{aligned}
&\sum_{i=1}^N\frac{|DB_i[q,0]|^2}{M_i}\\
&\qquad\le162\,R^2\sum_{i=1}^N\frac{|DM_i[q,0]|^2}{M_i},
\end{aligned}
\]
where \(K\subseteq B(0,R)\). The constant does not depend on the number of cells, their masses, or the geometry of the faces. The proof couples the cells for two opposite perturbations of the intercepts, observes that the midpoints lie in the unperturbed cell, and bounds the density of the midpoints by Knothe's triangular rearrangement.

- A midpoint coupling of two uniform laws (Lemma 1.1).
- The moment estimate (Proposition 2.1).

The lesson follows [OpenAI-BS, Section 4]. The density bound of Lemma 1.1 also follows from McCann's displacement concavity; the direct proof below uses the conditional-quantile construction of Knothe [Knothe].

## 1. A midpoint coupling

**Lemma 1.1** (midpoint coupling; [OpenAI-BS, Lemma 4.2]). Let \(U,V\subset\mathbb R^d\) be compact convex sets of positive volume. There are random vectors \(X\) and \(Z\), defined on one probability space, with uniform laws on \(U\) and on \(V\), such that
\[
\operatorname{Law}\Bigl(\frac{X+Z}2\Bigr)\le\frac{dx}{\sqrt{|U|\,|V|}}
\]
as measures on \(\mathbb R^d\).

*Proof.* *Slice functions.* For \(0\le k<d\) and \(\xi\in\mathbb R^k\) put
\[
p_k(\xi)=\int_{\mathbb R^{d-k}}\mathbf 1_{\operatorname{int}U}(\xi,\eta)\,d\eta ,
\]
and \(p_d=\mathbf 1_{\operatorname{int}U}\). Then \(p_0=|\operatorname{int}U|=|U|\) by Lemma 1.1(2) of [Optimal maps of finite affine maxima](optimal-maps-of-finite-affine-maxima.md). Let \(D_k\) be the projection of \(\operatorname{int}U\) to the first \(k\) coordinates, an open convex set. On \(D_k\), \(p_k\) is positive, since the fiber is a nonempty open set, and continuous: as \(\xi\to\xi_0\in D_k\), \(\mathbf 1_{\operatorname{int}U}(\xi,\eta)\to\mathbf 1_{\operatorname{int}U}(\xi_0,\eta)\) unless \((\xi_0,\eta)\in\partial U\), and the slice \(\{\xi_0\}\times\mathbb R^{d-k}\) meets \(\operatorname{int}U\), so its intersection with \(\partial U\) is null by Lemma 1.1(3) of that lesson; dominated convergence applies, as \(U\) is bounded. By Fubini's theorem, \(\int p_k(\xi,t)\,dt=p_{k-1}(\xi)\).

*Conditional quantiles.* For \(s=(s_1,\dots,s_d)\in(0,1)^d\) define \(X(s)\) coordinate by coordinate. Given \(\xi=(X_1,\dots,X_{k-1})\in D_{k-1}\), the function \(t\mapsto p_k(\xi,t)/p_{k-1}(\xi)\) is a probability density, positive and continuous on the bounded open interval \(\{t:(\xi,t)\in D_k\}\) and zero outside. Its distribution function is continuously differentiable and strictly increasing from \(0\) to \(1\) on that interval, so it has a unique quantile at level \(s_k\); let \(X_k\) be this quantile. Then \((\xi,X_k)\in D_k\), and
\[
\partial_{s_k}X_k=\frac{p_{k-1}(X_1,\dots,X_{k-1})}{p_k(X_1,\dots,X_k)}>0 .
\]
For fixed \(s_1,\dots,s_{k-1}\), \(X_k\) is continuously differentiable in \(s_k\). The distribution functions are Borel in all their arguments, so comparing them at rational levels shows that the quantiles are Borel: \(X\) is a Borel map. If \(s\) is uniform on \((0,1)^d\), successive conditioning shows that \(X(s)\) has the density \(\prod_kp_k/p_{k-1}=p_d/p_0\), the uniform law on \(U\). The diagonal derivatives telescope:
\[
\prod_{k=1}^d\partial_{s_k}X_k=\frac{p_0}{p_d}=|U| .
\]

*The midpoint.* Construct \(Z(s)\) in the same way for \(V\), with the same \(s\), and let \(H=(X+Z)/2\). Each \(H_k\) depends only on \(s_1,\dots,s_k\) and increases in \(s_k\), and by the inequality between the arithmetic and geometric means,
\[
\begin{aligned}
\prod_{k=1}^d\partial_{s_k}H_k&\ge\prod_{k=1}^d\sqrt{\partial_{s_k}X_k\,\partial_{s_k}Z_k}\\
&=\sqrt{|U|\,|V|} .
\end{aligned}
\]

*Substitution.* Let \(g\ge0\) be Borel on \(\mathbb R^d\). Fix \(a=(s_1,\dots,s_{d-1})\) and write \(H'(a)=(H_1(a),\dots,H_{d-1}(a))\), where \(H_k(a)\) uses the first \(k\) entries of \(a\). The one-dimensional substitution \(z=H_d(a,t)\), for the strictly increasing continuously differentiable function \(t\mapsto H_d(a,t)\), followed by enlarging its image interval to \(\mathbb R\), gives
\[
\begin{aligned}
&\int_0^1g\bigl(H'(a),H_d(a,t)\bigr)\,\partial_tH_d(a,t)\,dt\\
&\quad\le\int_{\mathbb R}g\bigl(H'(a),z\bigr)\,dz .
\end{aligned}
\]
The right side is a nonnegative Borel function of \(H'(a)\), and the remaining factors \(\partial_{s_k}H_k\), \(k<d\), depend only on earlier parameters. By Tonelli's theorem we may multiply by them and integrate in \(a\), and repeating the argument backwards gives
\[
\begin{aligned}
&\int_{(0,1)^d}g(H(s))\prod_{k=1}^d\partial_{s_k}H_k(s)\,ds\\
&\qquad\le\int_{\mathbb R^d}g(x)\,dx .
\end{aligned}
\]
Combined with the lower bound for the product,
\[
\begin{aligned}
\mathbb E\,g\Bigl(\frac{X+Z}2\Bigr)&=\int_{(0,1)^d}g(H(s))\,ds\\
&\le\frac1{\sqrt{|U|\,|V|}}\int_{\mathbb R^d}g(x)\,dx ,
\end{aligned}
\]
which is the asserted inequality of measures. \(\blacksquare\)

No differentiability in the earlier parameters, and no bound on the derivatives near the boundary of the cube, was needed: only monotone continuously differentiable dependence on the last parameter at each stage.

## 2. The moment estimate

**Proposition 2.1** (stationary-site moment estimate; [OpenAI-BS, Lemma 4.1]). Let \(K\subseteq B(0,R)\), and fix distinct sites and intercepts whose cells have positive masses \(M_i\). For every intercept direction \(q\in\mathbb R^N\), with \(C_0=162\),
\[
\begin{aligned}
&\sum_{i=1}^N\frac{|DB_i[q,0]|^2}{M_i}\\
&\qquad\le C_0R^2\sum_{i=1}^N\frac{|DM_i[q,0]|^2}{M_i} .
\end{aligned}
\]

*Proof.* *Opposite perturbations.* For small \(s>0\), let \(P_i^-\) and \(P_i^+\) be the cells at the intercepts \(c-sq\) and \(c+sq\), with the sites fixed, and
\[
\begin{gathered}
\alpha_i=\rho(P_i^-),\qquad\beta_i=\rho(P_i^+),\\
\gamma_i=\sqrt{\alpha_i\beta_i} .
\end{gathered}
\]
By continuity of the masses (Proposition 1.1 of the previous lesson) we may take \(s\) so small that \(\alpha_i\), \(\beta_i\) and \(\gamma_i\) lie between \(M_i/2\) and \(2M_i\) for every \(i\). Couple the uniform laws on \(P_i^-\) and \(P_i^+\) by Lemma 1.1, giving \(X_i\in P_i^-\) and \(Z_i\in P_i^+\), and let \(D_i=\mathbb E|X_i-Z_i|^2\). For each \(j\ne i\),
\[
\begin{aligned}
X_i\cdot(y_i-y_j)+c_i-c_j-s(q_i-q_j)&\ge0,\\
Z_i\cdot(y_i-y_j)+c_i-c_j+s(q_i-q_j)&\ge0 .
\end{aligned}
\]
Averaging, the midpoint \((X_i+Z_i)/2\) satisfies the inequalities of the cell \(P_i\) at \(c\), and it lies in \(K\) by convexity. Since \(|P_i^-|=|K|\alpha_i\) and \(|P_i^+|=|K|\beta_i\), Lemma 1.1 gives
\[
\gamma_i\operatorname{Law}\Bigl(\frac{X_i+Z_i}2\Bigr)\le\frac{\mathbf 1_{P_i}\,dx}{|K|}=\rho|_{P_i} .
\]

*Testing with a concave function.* Let \(\Phi(x)=R^2-|x|^2\), nonnegative on \(K\), and \(A_i^-=\mathbb E\Phi(X_i)\), \(A_i^+=\mathbb E\Phi(Z_i)\). The identity
\[
\begin{aligned}
\Phi\Bigl(\frac{X+Z}2\Bigr)&=\frac{\Phi(X)+\Phi(Z)}2\\
&\quad+\frac{|X-Z|^2}4
\end{aligned}
\]
and the domination give, since the cells at \(c\) cover \(K\) up to a null set,
\[
\begin{aligned}
&\sum_i\gamma_i\Bigl(\frac{A_i^-+A_i^+}2+\frac{D_i}4\Bigr)\le\int_K\Phi\,d\rho\\
&\qquad=\frac12\sum_i\bigl(\alpha_iA_i^-+\beta_iA_i^+\bigr) ;
\end{aligned}
\]
the last equality uses the two partitions at \(c\mp sq\). Put \(\delta_i=\alpha_i-\beta_i\),
\[
\mathcal A=\sum_i\gamma_iD_i,\qquad\mathcal B=\sum_i\frac{\delta_i^2}{\gamma_i} .
\]
Since \(\frac12(\alpha_iA_i^-+\beta_iA_i^+)\) equals \(\frac{\alpha_i+\beta_i}2\cdot\frac{A_i^-+A_i^+}2+\frac{\delta_i}2\cdot\frac{A_i^--A_i^+}2\), subtraction gives
\[
\begin{aligned}
\frac{\mathcal A}4\le\sum_i\Bigl[&\Bigl(\frac{\alpha_i+\beta_i}2-\gamma_i\Bigr)\frac{A_i^-+A_i^+}2\\
&+\frac{\delta_i}4\bigl(A_i^--A_i^+\bigr)\Bigr] .
\end{aligned}
\]
Here \(0\le A_i^\pm\le R^2\);
\[
\begin{aligned}
\frac{\alpha_i+\beta_i}2-\gamma_i&=\frac{\delta_i^2}{2(\sqrt{\alpha_i}+\sqrt{\beta_i})^2}\\
&\le\frac{\delta_i^2}{8\gamma_i} ,
\end{aligned}
\]
because \((\sqrt{\alpha_i}+\sqrt{\beta_i})^2\ge4\gamma_i\); and since \(|X_i|,|Z_i|\le R\), \(|A_i^--A_i^+|\le2R\,\mathbb E|X_i-Z_i|\le2R\sqrt{D_i}\). By Cauchy–Schwarz,
\[
\frac{\mathcal A}4\le\frac{R^2\mathcal B}8+\frac R2\sqrt{\mathcal A\mathcal B} .
\]
With \(\frac R2\sqrt{\mathcal A\mathcal B}\le\frac{\mathcal A}8+\frac{R^2\mathcal B}2\), this gives
\[
\mathcal A\le5R^2\mathcal B ,
\]
including the cases where either side vanishes.

*Moments.* The difference of the cell moments is
\[
\begin{aligned}
\Delta B_i&=B_i(c-sq)-B_i(c+sq)\\
&=\alpha_i\mathbb EX_i-\beta_i\mathbb EZ_i ,
\end{aligned}
\]
so
\[
\begin{aligned}
|\Delta B_i|&\le|\delta_i|\,|\mathbb EZ_i|+\alpha_i|\mathbb E(X_i-Z_i)|\\
&\le R|\delta_i|+\alpha_i\sqrt{D_i} .
\end{aligned}
\]
Let \(\mathcal E=\sum_i\delta_i^2/M_i\). The comparisons with \(M_i\) give \(\alpha_i^2/M_i\le4M_i\le8\gamma_i\) and \(\mathcal B\le2\mathcal E\). Therefore
\[
\begin{aligned}
\sum_i\frac{|\Delta B_i|^2}{M_i}&\le2R^2\mathcal E+2\sum_i\frac{\alpha_i^2}{M_i}D_i\\
&\le2R^2\mathcal E+16\mathcal A\le162R^2\mathcal E .
\end{aligned}
\]
Divide by \((2s)^2\) and let \(s\to0\). By Proposition 1.1 of the previous lesson, \(\Delta B_i/(2s)\to-DB_i[q,0]\) and \(\delta_i/(2s)\to-DM_i[q,0]\), which proves the estimate. \(\blacksquare\)

The admissible range of \(s\) depends on the configuration, the direction and the smallest mass; only the constant \(162\) survives the limit. This is why the estimate holds uniformly as masses or faces degenerate.

## 3. Exercises

**3.1.** For \(d=1\), \(U=[0,1]\) and \(V=[0,2]\), compute the coupling of Lemma 1.1 and the law of \((X+Z)/2\), and check the density bound \(1/\sqrt2\).

**3.2.** Show that for \(U=V\) the coupling of Lemma 1.1 is \(X=Z\), and that the bound is then an equality.

**3.3.** Verify the identity \(\Phi\bigl(\frac{X+Z}2\bigr)=\frac{\Phi(X)+\Phi(Z)}2+\frac{|X-Z|^2}4\) for \(\Phi(x)=R^2-|x|^2\).

**3.4.** Check \(\frac{\alpha+\beta}2-\sqrt{\alpha\beta}=\frac{(\alpha-\beta)^2}{2(\sqrt\alpha+\sqrt\beta)^2}\) for \(\alpha,\beta>0\).

**3.5.** Show that \(\frac{\mathcal A}4\le\frac{R^2\mathcal B}8+\frac R2\sqrt{\mathcal A\mathcal B}\) implies \(\mathcal A\le5R^2\mathcal B\), and find the best constant \(c\) with \(\mathcal A\le cR^2\mathcal B\) that this inequality alone yields.

## 4. Solutions

**3.1.** \(X=s\) and \(Z=2s\) for \(s\in(0,1)\), so \((X+Z)/2=\frac32s\), uniform on \([0,\frac32]\) with density \(\frac23\le\frac1{\sqrt2}\approx0.707\).

**3.2.** The construction depends only on the set, so \(Z(s)=X(s)\), and \(H=X\) has density \(1/|U|=1/\sqrt{|U||U|}\).

**3.3.** Both sides equal \(R^2-\frac14(|X|^2+|Z|^2)-\frac12X\cdot Z\).

**3.4.** \(\frac{\alpha+\beta}2-\sqrt{\alpha\beta}=\frac12(\sqrt\alpha-\sqrt\beta)^2\), and \(\sqrt\alpha-\sqrt\beta=(\alpha-\beta)/(\sqrt\alpha+\sqrt\beta)\).

**3.5.** With \(x=\sqrt{\mathcal A}\) and \(y=R\sqrt{\mathcal B}\), the inequality is \(x^2/4\le y^2/8+xy/2\), that is \(2x^2-4xy-y^2\le0\), so \(x\le\frac{4+\sqrt{24}}4\,y\) and \(\mathcal A\le\bigl(1+\sqrt{3/2}\bigr)^2R^2\mathcal B\approx4.95\,R^2\mathcal B\). The constant \(5\) is a convenient rounding.

## References

- [OpenAI-BS] OpenAI, *Sharp one-third stability of Brenier maps*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026
- [Knothe] H. Knothe, *Contributions to the theory of convex bodies*, Michigan Math. J. 4 (1957), 39–52. https://doi.org/10.1307/mmj/1028990175
