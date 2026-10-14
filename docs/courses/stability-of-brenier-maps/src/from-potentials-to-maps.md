# From potentials to maps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson, [Moving sites with fixed masses](moving-sites-with-fixed-masses.md), bounds the distance of the affine potentials of two finite targets linearly by their Wasserstein distance. This lesson converts that bound into a bound on the gradients, which are the optimal maps, at the cost of the exponent \(\frac13\): an elementary interpolation inequality on coordinate slices controls the gradient difference of two convex functions by \(h^{-2}\) times their squared distance plus \(h\). Approximation by finite targets then gives existence and uniqueness of optimal maps for all targets, and the theorem of [Optimal maps of finite affine maxima](optimal-maps-of-finite-affine-maxima.md).

- Partial derivatives and gradients of convex functions (Lemma 1.1).
- Gradient interpolation (Lemma 1.2).
- Stability for finite targets (Corollary 1.3).
- Optimal maps for all targets, and the theorem (Proposition 2.1, Theorem 2.2).

The lesson follows [OpenAI-BS, Section 6]. The interpolation inequality is a coordinate-slice form of an inequality of Delalande and Mérigot [DM, Proposition 4.1]. Throughout, \(K\subseteq B(0,R)\) is a compact convex set with nonempty interior, \(\rho\) its uniform probability measure, \(Y\subseteq B(0,L)\) compact, and \(C_0=162\).

## 1. Gradient interpolation

**Lemma 1.1** (gradients of convex functions). Let \(u\) be convex and Lipschitz on \(K\). (1) For each \(j\), the partial derivative \(\partial_ju\) exists almost everywhere in \(K\), and on almost every line parallel to \(e_j\) it is nondecreasing where it exists. (2) If all partial derivatives exist at an interior point \(x\), then \(u\) is differentiable at \(x\) with gradient \(p=(\partial_1u(x),\dots,\partial_du(x))\). (3) At such a point, \(p\) is the only vector with \(u(z)\ge u(x)+p\cdot(z-x)\) for all \(z\in K\).

*Proof.* (1) On a line, a convex function has nondecreasing one-sided derivatives, which agree except at countably many points. The set where \(\partial_ju\) fails to exist is Borel, and by Fubini's theorem it is null.

(2) Let \(v\ne0\) be small and \(q=\|v\|_1=\sum_j|v_j|\). With \(\sigma_j=\operatorname{sign}(v_j)\), the point \(x+v\) is the convex combination of the points \(x+\sigma_jqe_j\) with weights \(|v_j|/q\), omitting zero weights, so convexity and the partial derivatives give
\[
\begin{aligned}
u(x+v)&\le\sum_j\frac{|v_j|}q\,u(x+\sigma_jqe_j)\\
&=u(x)+p\cdot v+o(q) .
\end{aligned}
\]
The same with \(-v\), and \(u(x)\le\frac12(u(x+v)+u(x-v))\), give \(u(x+v)\ge u(x)+p\cdot v-o(q)\). Since \(q\le\sqrt d\,|v|\), \(u\) is differentiable at \(x\) with gradient \(p\).

(3) A supporting vector \(p'\) satisfies \(u(x+te_j)-u(x)\ge tp'_j\) for small \(t\) of both signs, so \(p'_j\) lies between the left and right derivatives, which both equal \(\partial_ju(x)\). \(\blacksquare\)

By Lemma 1.1(2) and the null boundary of \(K\) (Lemma 1.1(2) of the first lesson), the gradient of a convex Lipschitz function on \(K\) exists almost everywhere and is the vector of its partial derivatives.

For a unit coordinate vector \(e_j\) let \(A_j\) be the \((d-1)\)-dimensional volume of the projection of \(K\) on \(e_j^\perp\), and \(P_K=\sum_jA_j\).

**Lemma 1.2** (gradient interpolation; [OpenAI-BS, Lemma 6.1]). Let \(u_0\) and \(u_1\) be convex and \(L\)-Lipschitz on \(K\), and \(f=u_0-u_1\). For every \(h>0\),
\[
\begin{aligned}
\|\nabla u_0-\nabla u_1\|_{L^2(\rho)}^2&\le\frac{12d}{h^2}\|f\|_{L^2(\rho)}^2\\
&\quad+\frac{28L^2P_K}{|K|}\,h .
\end{aligned}
\]

*Proof.* Fix \(j\), let \(K_{j,h}=\{x\in K:x+he_j\in K\}\), and for \(x\in K_{j,h}\) let
\[
D_{j,h}u(x)=\frac{u(x+he_j)-u(x)}h .
\]
Almost every nonempty slice of \(K\) parallel to \(e_j\) is an interval \([\alpha,\beta]\) on which each \(u_i\) is convex, \(L\)-Lipschitz, and has a nondecreasing derivative of absolute value at most \(L\) almost everywhere. For either \(u=u_i\), put \(\delta_u(x)=D_{j,h}u(x)-\partial_ju(x)\) at the points \(x\) where \(\partial_ju\) exists at \(x\) and at \(x+he_j\). Convexity gives \(\delta_u\ge0\) and
\[
\begin{aligned}
\delta_u(x)&\le\partial_ju(x+he_j)-\partial_ju(x)\\
&\le2L .
\end{aligned}
\]
If \(\beta-\alpha\ge h\), cancellation of translated integrals gives (suppressing the other coordinates)
\[
\begin{aligned}
&\int_\alpha^{\beta-h}\bigl(\partial_ju(t+h)-\partial_ju(t)\bigr)\,dt\\
&\quad=\int_{\beta-h}^\beta\partial_ju\,dt-\int_\alpha^{\alpha+h}\partial_ju\,dt\le2Lh ;
\end{aligned}
\]
if \(\beta-\alpha<h\), the allowed part of the slice is empty. Integrating \(\delta_u^2\le2L\delta_u\) over the slices and then over the projection,
\[
\int_{K_{j,h}}\delta_u^2\,d\rho\le\frac{4L^2hA_j}{|K|} .
\]
Each slice loses at most a length \(h\), so \(\rho(K\setminus K_{j,h})\le hA_j/|K|\); there we use \(|\partial_jf|\le2L\). On \(K_{j,h}\), both \(x\) and \(x+he_j\) lie in \(K\), and translation invariance of Lebesgue measure with \((a-b)^2\le2a^2+2b^2\) gives
\[
\int_{K_{j,h}}|D_{j,h}f|^2\,d\rho\le\frac4{h^2}\|f\|_{L^2(\rho)}^2 .
\]
Since \(\partial_jf=D_{j,h}f-\delta_{u_0}+\delta_{u_1}\), the inequality \((a+b+c)^2\le3(a^2+b^2+c^2)\) gives
\[
\begin{aligned}
\int_K|\partial_jf|^2\,d\rho&\le\frac{12}{h^2}\|f\|_{L^2(\rho)}^2\\
&\quad+\frac{(24+4)L^2hA_j}{|K|} .
\end{aligned}
\]
Summing over \(j\), with Lemma 1.1, proves the lemma; it holds for every \(h>0\), also when \(h\) exceeds some slice lengths. \(\blacksquare\)

**Corollary 1.3** (finite target stability; [OpenAI-BS, Corollary 6.2]). Let
\[
\begin{aligned}
C_*&=\Bigl(12dR^2(1+\sqrt{C_0})^2\\
&\qquad+\frac{28L^2P_K}{|K|}\Bigr)^{1/2} .
\end{aligned}
\]
For finitely supported probability measures \(\mu\) and \(\nu\) on \(Y\),
\[
\|T_\mu-T_\nu\|_{L^2(\rho)}\le C_*\,W_2(\mu,\nu)^{1/3} .
\]

*Proof.* Let \(w=W_2(\mu,\nu)\), and \(u_0\), \(u_1\) the potentials of Proposition 1.1 of the previous lesson, with \(\|u_0-u_1\|_{L^2(\rho)}\le(1+\sqrt{C_0})Rw\). If \(w>0\), Lemma 1.2 with \(h=w^{2/3}\) gives
\[
\begin{aligned}
&\|T_\mu-T_\nu\|_{L^2(\rho)}^2\\
&\quad\le12d(1+\sqrt{C_0})^2R^2w^{2/3}\\
&\qquad+\frac{28L^2P_K}{|K|}w^{2/3}=C_*^2w^{2/3} .
\end{aligned}
\]
If \(w=0\), the potentials agree in \(L^2(\rho)\), and letting \(h\to0\) in Lemma 1.2 gives \(T_\mu=T_\nu\). \(\blacksquare\)

## 2. All targets

**Proposition 2.1** (approximation and optimal maps; [OpenAI-BS, Proposition 6.3]). Every \(\lambda\in\operatorname{Prob}(Y)\) has a quadratic optimal map \(T_\lambda\) from \(\rho\), unique up to a null set, and every optimal transport plan from \(\rho\) to \(\lambda\) is concentrated on its graph. If \(F_n\subseteq Y\) are finite \(\varepsilon_n\)-nets with \(\varepsilon_n\to0\) and \(Q_n\colon Y\to F_n\) are Borel nearest-point selections, then \(T_{(Q_n)_\#\lambda}\to T_\lambda\) in \(L^2(\rho)\).

*Proof.* *A Cauchy sequence.* Compactness of \(Y\) gives the nets; enumerating each net and choosing the first nearest point gives a Borel selection with \(|Q_n(y)-y|\le\varepsilon_n\). Let \(\lambda_n=(Q_n)_\#\lambda\), discard its sites of zero mass, and let \(T_n=T_{\lambda_n}\), which exists by Proposition 2.1 of [Laguerre cells and prescribed masses](laguerre-cells-and-prescribed-masses.md) and Lemma 2.1 of the first lesson. The coupling \((Q_n,Q_m)_\#\lambda\) gives \(W_2(\lambda_n,\lambda_m)\le\varepsilon_n+\varepsilon_m\), so by Corollary 1.3 the sequence \((T_n)\) is Cauchy in \(L^2(\rho)\). Let \(S\) be its limit, and pass to a subsequence converging almost everywhere. The limit lies in the closed set \(Y\) almost everywhere; changing \(S\) on a null set, \(S\) is a Borel map into \(Y\).

*\(S\) transports \(\rho\) to \(\lambda\).* For continuous \(\varphi\) on \(Y\), bounded convergence and uniform continuity give
\[
\begin{aligned}
&\int_K\varphi(S)\,d\rho=\lim_n\int_K\varphi(T_n)\,d\rho\\
&\quad=\lim_n\int_Y\varphi(Q_n(y))\,d\lambda(y)\\
&\quad=\int_Y\varphi\,d\lambda .
\end{aligned}
\]

*A limit potential.* Let \(u_n\) be finite affine maxima with \(\nabla u_n=T_n\) almost everywhere, normalized by \(u_n(x_*)=0\) at a fixed \(x_*\in K\). Their slopes lie in \(Y\), so they are \(L\)-Lipschitz and \(|u_n|\le L\operatorname{diam}K\) on \(K\). By the Arzelà–Ascoli theorem ([Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20); [Lebl, Basic Analysis II, Theorem 11.6.9](https://www.jirka.org/ra/html/sec_arzelaascoli.html#thm_arzelaascoli)) a further subsequence converges uniformly on \(K\) to a convex \(L\)-Lipschitz function \(u\). For each \(n\), off a null set, \(T_n(x)\) is a maximizing slope of \(u_n\) at \(x\), so \(u_n(z)\ge u_n(x)+T_n(x)\cdot(z-x)\) for all \(z\in K\). Intersecting these countably many full-measure sets with the set where \(T_n\to S\), the limit gives
\[
u(z)\ge u(x)+S(x)\cdot(z-x)
\]
for all \(z\in K\) and almost every \(x\).

*Optimality.* Let \(u^*(y)=\max_{z\in K}(z\cdot y-u(z))\), finite and continuous. Then \(x\cdot y\le u(x)+u^*(y)\) for \(x\in K\) and all \(y\), with equality at \(y=S(x)\) for almost every \(x\) by the supporting inequality. For a plan \(\pi\) from \(\rho\) to \(\lambda\),
\[
\begin{aligned}
\int x\cdot y\,d\pi&\le\int u\,d\rho+\int u^*\,d\lambda\\
&=\int x\cdot S(x)\,d\rho .
\end{aligned}
\]
As in the proof of Lemma 2.1 of the first lesson, the plan of \(S\) has minimal quadratic cost.

*Uniqueness.* If a plan \(\pi\) is optimal, equality holds above, so the nonnegative gap \(u(x)+u^*(y)-x\cdot y\) vanishes \(\pi\)-almost everywhere; by the definition of \(u^*\), \(y\) is then a supporting slope of \(u\) at \(x\). By Lemma 1.1(3), at almost every \(x\) the only supporting slope is \(\nabla u(x)\), and \(S(x)\) is one, so \(y=S(x)\): \(\pi\) lives on the graph of \(S\). In particular every optimal map equals \(S\) almost everywhere. So \(S=T_\lambda\), and since the whole sequence \((T_n)\) is Cauchy, it converges to \(T_\lambda\). \(\blacksquare\)

**Theorem 2.2** (Theorem 3.1 of the first lesson; [OpenAI-BS, Theorem 1.1]). For all \(\mu,\nu\in\operatorname{Prob}(Y)\),
\[
\|T_\mu-T_\nu\|_{L^2(\rho)}\le C_*\,W_2(\mu,\nu)^{1/3} ,
\]
and the exponent \(\frac13\) cannot be increased.

*Proof.* Use the same nets and selections for \(\mu\) and \(\nu\), and let \(\mu_n=(Q_n)_\#\mu\), \(\nu_n=(Q_n)_\#\nu\). For a coupling \(\pi\) of \(\mu\) and \(\nu\), its image under \((Q_n,Q_n)\) couples \(\mu_n\) and \(\nu_n\), and \(|Q_n(y)-Q_n(z)|\le|y-z|+2\varepsilon_n\), so by the triangle inequality in \(L^2(\pi)\)
\[
W_2(\mu_n,\nu_n)\le\Bigl(\int|y-z|^2\,d\pi\Bigr)^{1/2}+2\varepsilon_n .
\]
Taking the infimum over \(\pi\), \(W_2(\mu_n,\nu_n)\le W_2(\mu,\nu)+2\varepsilon_n\). Corollary 1.3 bounds \(\|T_{\mu_n}-T_{\nu_n}\|_{L^2(\rho)}\) by \(C_*(W_2(\mu,\nu)+2\varepsilon_n)^{1/3}\), and Proposition 2.1 lets \(n\to\infty\). Sharpness is Proposition 4.1 of the first lesson. \(\blacksquare\)

The constant depends only on \(K\) and the radius \(L\). It does not see the number of atoms, their masses, their separation or any density of the targets, and \(Y\) need not be convex: the interpolated sites of the previous lesson stay in the ball \(B(0,L)\), and the discretizations take values in \(Y\).

## 3. Exercises

**3.1.** Show that the constant \(28\) in Lemma 1.2 is \(3\cdot2\cdot4+4\), and explain where each term comes from.

**3.2.** For \(d=1\), \(K=[0,1]\), \(u_0(x)=|x-\frac12|\) and \(u_1=0\), compare both sides of Lemma 1.2 for small \(h\).

**3.3.** Show that with \(h=W_2^{2/3}\) the two terms of Lemma 1.2 have the same order, and that no other choice of \(h\) gives a better exponent from Lemma 1.2 and the potential bound alone.

**3.4.** Show that a Borel nearest-point selection \(Q_n\) exists: enumerate \(F_n=\{f_1,\dots,f_k\}\) and let \(Q_n(y)\) be the first \(f_i\) at minimal distance from \(y\).

**3.5.** In the proof of Theorem 2.2, why is it enough to know \(W_2\) as an infimum, without an optimal coupling of \(\mu\) and \(\nu\)?

## 4. Solutions

**3.1.** On \(K_{j,h}\), the term \(3\bigl(\int\delta_{u_0}^2+\int\delta_{u_1}^2\bigr)\) is at most \(3\cdot2\cdot4L^2hA_j/|K|=24L^2hA_j/|K|\); on \(K\setminus K_{j,h}\), \(|\partial_jf|^2\le4L^2\) on a set of measure at most \(hA_j/|K|\), which gives the remaining \(4\).

**3.2.** \(\|\nabla u_0\|^2=1\), \(\|f\|^2=\int_0^1(x-\frac12)^2dx=\frac1{12}\), \(P_K=1\) (the projection of \([0,1]\) on the point \(e_1^\perp\) has measure one), \(L=1\). The right side is \(\frac1{h^2}+28h\), at least \(1\), with minimum about \(3\cdot(\frac{28}2)^{2/3}\approx17.4\) at \(h=(1/14)^{1/3}\).

**3.3.** With \(\|f\|\le Cw\), the bound is \(C(w^2/h^2+h)\); balancing \(w^2/h^2=h\) gives \(h=w^{2/3}\) and the value \(Cw^{2/3}\), so the map bound is \(Cw^{1/3}\). For \(h=w^\gamma\) the bound is \(C(w^{2-2\gamma}+w^\gamma)\), of order \(w^{\min(2-2\gamma,\gamma)}\), largest exponent \(\frac23\) at \(\gamma=\frac23\).

**3.4.** \(\{Q_n=f_i\}\) is the set of \(y\) with \(|y-f_i|<|y-f_l|\) for \(l<i\) and \(|y-f_i|\le|y-f_l|\) for \(l>i\), an intersection of open and closed sets.

**3.5.** The estimate \(W_2(\mu_n,\nu_n)\le(\int|y-z|^2d\pi)^{1/2}+2\varepsilon_n\) holds for every coupling, so its infimum over \(\pi\) bounds \(W_2(\mu_n,\nu_n)\) by \(W_2(\mu,\nu)+2\varepsilon_n\) whether or not the infimum is attained.

## References

- [OpenAI-BS] OpenAI, *Sharp one-third stability of Brenier maps*, OpenAI Math Release preprint, 25 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026
- [DM] A. Delalande and Q. Mérigot, *Quantitative stability of optimal transport maps under variations of the target measure*, Duke Math. J. 172 (2023), Proposition 4.1. https://arxiv.org/abs/2103.05934
