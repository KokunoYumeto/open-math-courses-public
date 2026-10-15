# Optimal maps of finite affine maxima

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(K\subset\mathbb R^d\), \(d\ge2\), be a compact convex set with nonempty interior, and \(\rho\) the uniform probability measure on \(K\). For a probability measure \(\mu\) with compact support, a *quadratic optimal map* from \(\rho\) to \(\mu\) is a Borel map \(T\) with \(T_\#\rho=\mu\) that minimizes \(\int_K|x-T(x)|^2\,d\rho(x)\) among all such maps. This course proves the theorem of [OpenAI-BS]: optimal maps exist, are unique up to null sets, and depend on the target in a Hölder way with exponent \(\frac13\) for the quadratic Wasserstein distance, with one constant for all targets supported in a fixed compact set. The exponent \(\frac13\) is optimal, already on a cube with three-atom targets.

This lesson introduces the objects that the whole proof uses: maxima of finitely many affine functions, whose gradients are optimal maps to finite targets. It states the theorem and proves its sharpness.

- Convex bodies: null boundaries and sections (Lemma 1.1).
- Finite affine maxima and their optimality (Lemma 2.1).
- The theorem (Theorem 3.1).
- The exponent cannot be improved (Proposition 4.1).

The lesson follows [OpenAI-BS, Sections 1 and 2]. Measure theory is that of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fremlin, *Measure Theory*, Volumes 1 and 2): Lebesgue measure, image measures, Fubini's and Tonelli's theorems, dominated convergence.

## 1. Convex bodies

Write \(|E|\) for Lebesgue measure, \(\operatorname{int}\) for the interior, and \(\operatorname{relint}\) for the interior relative to the affine span.

**Lemma 1.1.** Let \(K\subset\mathbb R^d\) be compact and convex with nonempty interior.

1. If \(p\in\operatorname{int}K\) and \(z\in K\), the half-open segment \([p,z)\) lies in \(\operatorname{int}K\).
2. The boundary of \(K\) has measure zero.
3. If an affine subspace \(E\) meets \(\operatorname{int}K\), then \(\operatorname{relint}(K\cap E)=\operatorname{int}K\cap E\), and \(\partial K\cap E\) has zero measure in \(E\).

*Proof.* (1) Let \(B(p,\varepsilon)\subseteq K\). For \(w=(1-t)p+tz\) with \(0\le t<1\), convexity gives \(B(w,(1-t)\varepsilon)\subseteq K\), since this ball equals \((1-t)B(p,\varepsilon)+tz\).

(2) For \(0<s<1\), the contraction \(K_s=p+s(K-p)\) lies in \(\operatorname{int}K\) by (1), and \(|K_s|=s^d|K|\). So \(|\operatorname{int}K|\ge s^d|K|\) for every \(s<1\), hence \(|\partial K|=|K|-|\operatorname{int}K|=0\).

(3) Let \(p\in\operatorname{int}K\cap E\). A ball about a point of \(\operatorname{int}K\cap E\) meets \(E\) in a relative neighbourhood inside \(K\cap E\), so \(\operatorname{int}K\cap E\subseteq\operatorname{relint}(K\cap E)\). Conversely, let \(z\ne p\) be in \(\operatorname{relint}(K\cap E)\). For small \(t>0\) the point \(z'=z+t(z-p)\) lies in \(K\cap E\), and \(z\) lies on the half-open segment \([p,z')\), hence in \(\operatorname{int}K\) by (1). Now \(K\cap E\) is a compact convex set with nonempty relative interior in \(E\), so by (2) applied inside \(E\) its relative boundary is null in \(E\); and \(\partial K\cap E\) lies in that relative boundary. \(\blacksquare\)

## 2. Finite affine maxima

Let \(y_1,\dots,y_N\in\mathbb R^d\) (the *sites*) and \(c_1,\dots,c_N\in\mathbb R\) (the *intercepts*), and put
\[
u(x)=\max_{1\le i\le N}\bigl(x\cdot y_i+c_i\bigr) .
\]
It is convex, and Lipschitz with constant \(\max_i|y_i|\). Two indices with different slopes \(y_i\ne y_j\) tie on the hyperplane \(\{x\cdot(y_i-y_j)+c_i-c_j=0\}\), so the *tie set*, where two maximizing indices have different slopes, is contained in finitely many hyperplanes and has measure zero. Let \(T(x)=y_i\) for the smallest maximizing index \(i\). Its level sets are given by finitely many strict and non-strict affine inequalities, so \(T\) is Borel. Off the tie set, the maximizing slope is strictly larger than the others in a neighbourhood, so \(u\) is differentiable with \(\nabla u=T\) there.

**Lemma 2.1** (optimality of a finite affine maximum; [OpenAI-BS, Lemma 2.1]). Let \(\lambda=T_\#\rho\). Then \(T\) is a quadratic optimal map from \(\rho\) to \(\lambda\). Every transport plan from \(\rho\) to \(\lambda\) whose quadratic cost is minimal is concentrated on the graph of \(T\); in particular every quadratic optimal map from \(\rho\) to \(\lambda\) equals \(T\) almost everywhere.

*Proof.* Merge repeated slopes: for a site value \(y\) let \(c(y)\) be the largest intercept among the indices with slope \(y\). Then \(x\cdot y+c(y)\le u(x)\) for all \(x\) and all site values \(y\), and a maximizing index \(i\) has \(c_i=c(y_i)\). For a transport plan \(\pi\) from \(\rho\) to \(\lambda\), that is a probability measure on \(K\times\{y_1,\dots,y_N\}\) with marginals \(\rho\) and \(\lambda\), integration gives
\[
\int x\cdot y\,d\pi(x,y)\le\int_Ku\,d\rho-\int c\,d\lambda ,
\]
with equality for the plan \((\mathrm{id},T)_\#\rho\), since \(x\cdot T(x)+c(T(x))=u(x)\) off the tie set. As
\[
\begin{aligned}
\int|x-y|^2\,d\pi&=\int|x|^2\,d\rho+\int|y|^2\,d\lambda\\
&\quad-2\int x\cdot y\,d\pi ,
\end{aligned}
\]
minimizing the cost is the same as maximizing \(\int x\cdot y\,d\pi\), and \((\mathrm{id},T)_\#\rho\) does so. If \(\pi\) is optimal too, equality holds, so the nonnegative function \(u(x)-c(y)-x\cdot y\) vanishes \(\pi\)-almost everywhere: \(\pi\) lives on pairs where \(y\) is a maximizing slope at \(x\). Off the tie set that slope is \(T(x)\). A map \(S\) with \(S_\#\rho=\lambda\) and minimal cost gives the optimal plan \((\mathrm{id},S)_\#\rho\), so \(S=T\) almost everywhere. \(\blacksquare\)

The gradient of every finite affine maximum is therefore optimal for its own target. The cells
\[
P_i=\{x\in K:\ u(x)=x\cdot y_i+c_i\}
\]
are closed convex sets that cover \(K\), overlap only in the tie set when the sites are distinct, and carry the slope \(y_i\). They are the *Laguerre cells* of the next lesson.

## 3. The theorem

For a compact set \(Y\subset\mathbb R^d\), let \(\operatorname{Prob}(Y)\) be the Borel probability measures on \(Y\). For probability measures \(\mu,\nu\) with compact support,
\[
W_2(\mu,\nu)=\inf_{\pi}\Bigl(\int|y-z|^2\,d\pi(y,z)\Bigr)^{1/2},
\]
the infimum over couplings \(\pi\), that is probability measures on \(\mathbb R^d\times\mathbb R^d\) with marginals \(\mu\) and \(\nu\).

**Theorem 3.1** ([OpenAI-BS, Theorem 1.1]). Let \(K\subset\mathbb R^d\), \(d\ge2\), be compact and convex with nonempty interior, \(\rho\) the uniform probability measure on \(K\), and \(Y\subset\mathbb R^d\) compact and nonempty. Every \(\mu\in\operatorname{Prob}(Y)\) has a quadratic optimal map \(T_\mu\) from \(\rho\), unique up to null sets, and there is a constant \(C(K,Y)\) with
\[
\|T_\mu-T_\nu\|_{L^2(\rho)}\le C(K,Y)\,W_2(\mu,\nu)^{1/3}
\]
for all \(\mu,\nu\in\operatorname{Prob}(Y)\). The exponent \(\frac13\) cannot be replaced by a larger one, even for \(K=Y=[-1,1]^d\) and targets with exactly three atoms.

The constant does not depend on the number of atoms, their masses, their separation or any density bound, and neither smoothness nor strict convexity of \(K\), nor convexity of \(Y\), is required. The last lesson gives the explicit constant
\[
\begin{aligned}
C_*&=\Bigl(12dR^2(1+\sqrt{162})^2\\
&\qquad+\frac{28L^2P_K}{|K|}\Bigr)^{1/2} ,
\end{aligned}
\]
where \(K\subseteq B(0,R)\), \(Y\subseteq B(0,L)\), and \(P_K\) is the sum of the \((d-1)\)-dimensional volumes of the projections of \(K\) on the coordinate hyperplanes.

Letrouit conjectured that for a uniform convex source the square-root exponent holds uniformly [Letrouit, Conjecture 3]; Proposition 4.1 below disproves this. Earlier results with smaller exponents, or with constants that depend on the number and the masses of the atoms, are surveyed in [OpenAI-BS, Section 1]; they are not used here. Later work treats other sources. S. Wang and X. Wang consider a source with an \(L^p\) density, \(1<p\le\infty\), relative to a probability measure with a density of bounded variation, possibly with unbounded support; when one target lies in a fixed ball and the other is arbitrary, they prove stability of the maps in \(L^2\) with the Hölder exponent \(\frac{p-1}{4p-2}\) of \(W_2\), which is \(\frac14\) for \(p=\infty\), and a fixed source in the plane shows that this exponent cannot be improved in their class [WW, Theorem 1 and Section 1]. The uniform measure on a convex body is such a source with \(p=\infty\); for it, with both targets in a fixed compact set, Theorem 3.1 gives the exponent \(\frac13\). Ruan determined the sharp modulus with which the excess transport cost of a feasible plan controls its distance to the optimal map, under density and moment conditions that allow unbounded supports, and derived stability estimates for maps with a common source [Ruan]. Ford proved quantitative stability of optimal plans under perturbation of both marginals when one of them is upper Ahlfors regular with an exponent larger than \(d-1\), with sharp exponents [Ford]. Han and Zhu proved the sharp analogue for \(W_1\) on complete Riemannian manifolds and on fat sub-Riemannian manifolds: for a source with bounded support and bounded density and targets in a fixed compact set, the optimal maps satisfy \(\|\operatorname{dist}(T_\mu,T_\nu)\|_{L^2(\rho)}\le C\,W_1(\mu,\nu)^{1/4}\), where \(\operatorname{dist}\) is the Riemannian or the Carnot–Carathéodory distance, and targets with three atoms show that no exponent of \(W_1\) larger than \(\frac14\) works on any smooth sub-Riemannian manifold of horizontal rank at least two [HZ, Corollary 1.2 and Theorem 1.4]. They also observe that in the example of Proposition 4.1 below \(W_1\) is of order \(a^2\), \(W_2\) of order \(a^{3/2}\) and the distance of the maps of order \(a^{1/2}\), so that this example excludes exponents of \(W_1\) above \(\frac14\) as well [HZ, Section 1.2].

The proof of the upper bound has four steps, one per remaining lesson. The second lesson computes the derivatives of the masses and first moments of Laguerre cells, and constructs intercepts that keep prescribed masses as the sites move. The third proves the key estimate: when the intercepts move with fixed sites, the change of the first moments is controlled by the change of the masses, with an absolute constant. The fourth moves the sites of one finite target to those of another along an optimal coupling, keeping the masses fixed, and shows that the potentials move by at most \(C\,W_2\) in \(L^2(\rho)\). The fifth turns a bound on potentials into a bound on gradients at the cost of the exponent \(\frac13\), and passes from finite to arbitrary targets.

## 4. The exponent cannot be improved

**Proposition 4.1** (optimality of the exponent; [OpenAI-BS, Proposition 2.2]). Let \(K=Y=[-1,1]^d\) and \(\rho=2^{-d}\mathbf 1_K\,dx\). For every \(\alpha>\frac13\),
\[
\sup_{\mu\ne\nu}\frac{\|T_\mu-T_\nu\|_{L^2(\rho)}}{W_2(\mu,\nu)^\alpha}=+\infty ,
\]
where \(\mu\) and \(\nu\) range over the probability measures on \(Y\) with exactly three atoms.

*Proof.* For \(0<a<\frac12\) put \(b=a/2\) and
\[
\begin{gathered}
u_a(x)=\max\{-x_1,\ x_1,\ a\},\\
\tilde u_a(x)=\max\{-x_1,\ x_1,\ a+bx_2\} .
\end{gathered}
\]
Their slopes are \(-e_1,e_1,0\) and \(-e_1,e_1,be_2\), all in \(Y\). Let \(\mu_a\) and \(\nu_a\) be the images of \(\rho\) under \(\nabla u_a\) and \(\nabla\tilde u_a\); by Lemma 2.1 these gradients are the optimal maps \(T_{\mu_a}\) and \(T_{\nu_a}\).

Under \(\rho\) the coordinates are independent and uniform on \([-1,1]\). Since \(\frac a2\le a+bx_2\le\frac{3a}2<1\), the central cells are, up to null sets,
\[
\begin{gathered}
A_a=\{|x_1|<a\},\\
B_a=\{|x_1|<a+bx_2\} .
\end{gathered}
\]
On the slice \(x_2=t\), the second central interval has probability \(a+bt\) and each outer interval \((1-a-bt)/2\). Averaging over \(t\),
\[
\begin{aligned}
\mu_a&=\tfrac{1-a}2(\delta_{-e_1}+\delta_{e_1})+a\,\delta_0,\\
\nu_a&=\tfrac{1-a}2(\delta_{-e_1}+\delta_{e_1})+a\,\delta_{be_2} .
\end{aligned}
\]

*The targets are close.* The coupling that fixes the outer atoms and moves the central atom from \(0\) to \(be_2\) costs \(ab^2\). Conversely, every point of the support of \(\mu_a\) has second coordinate \(0\), so every coupling \(\pi\) has \(\int|y-z|^2\,d\pi\ge\int z_2^2\,d\nu_a(z)=ab^2\). Hence \(W_2(\mu_a,\nu_a)^2=ab^2\).

*The maps are far.* On the slice \(x_2=t\) the two central intervals are nested, and their symmetric difference has probability \(b|t|\); so \(\rho(A_a\triangle B_a)=\frac12\int_{-1}^1b|t|\,dt=\frac b2\). On \(A_a\cap B_a\) the maps are \(0\) and \(be_2\); on \(A_a\setminus B_a\) they are \(0\) and \(\pm e_1\); on \(B_a\setminus A_a\) they are \(\pm e_1\) and \(be_2\); elsewhere they agree. Hence, almost everywhere,
\[
|T_{\mu_a}-T_{\nu_a}|^2=\mathbf 1_{A_a\triangle B_a}+b^2\,\mathbf 1_{B_a} ,
\]
and since \(\rho(B_a)=a\),
\[
\|T_{\mu_a}-T_{\nu_a}\|_{L^2(\rho)}^2=\frac b2+ab^2 .
\]

With \(b=a/2\), \(W_2(\mu_a,\nu_a)=\frac12a^{3/2}\) and \(\|T_{\mu_a}-T_{\nu_a}\|_{L^2(\rho)}=\frac12a^{1/2}(1+a^2)^{1/2}\). The ratio in the proposition is
\[
2^{\alpha-1}(1+a^2)^{1/2}\,a^{(1-3\alpha)/2} ,
\]
which tends to \(\infty\) as \(a\to0\), since \(\alpha>\frac13\). The remaining \(d-2\) coordinates play no role. \(\blacksquare\)

The mechanism is visible in the formulas. Tilting the central affine function by an amount \(b\) keeps the central mass fixed but reassigns a set of mass \(b/2\) between slopes at distance about one, while the targets move only by \(b\) on a mass \(a\). With \(b=a/2\), the map distance is of order \(a^{1/2}\) and \(W_2\) of order \(a^{3/2}\).

## 5. Exercises

**5.1.** Compute \(W_1(\mu_a,\nu_a)\), where \(W_1\) is defined like \(W_2\) with \(|y-z|\) in place of \(|y-z|^2\) and without the square root, and show that \(\|T_{\mu_a}-T_{\nu_a}\|_{L^2(\rho)}\) is of order \(W_1(\mu_a,\nu_a)^{1/4}\) as \(a\to0\).

**5.2.** Show that the closed segment \([p,z]\) in Lemma 1.1(1) need not lie in \(\operatorname{int}K\).

**5.3.** For \(N=2\) sites \(y_1\ne y_2\) on \(K=[-1,1]^d\), show that the cell \(P_1\) is the intersection of \(K\) with a half-space, and that its mass is a continuous nonincreasing function of \(c_2-c_1\) that takes every value in \((0,1)\).

**5.4.** Let \(u\) be a convex function on \(K\) and \(T\) a Borel map with values in a compact set, such that \(u(z)\ge u(x)+T(x)\cdot(z-x)\) for all \(z\in K\) and almost every \(x\in K\). Show that \(T\) is a quadratic optimal map from \(\rho\) to \(T_\#\rho\).

**5.5.** In the proof of Proposition 4.1, check that \(\mu_a\) and \(\nu_a\) have the same atom masses and that the second coordinate of every point in the support of \(\nu_a\) is \(0\) or \(b\).

## 6. Solutions

**5.1.** The coupling that moves the central atom costs \(ab\), and every coupling has \(\int|y-z|\,d\pi\ge\int|z_2|\,d\nu_a=ab\). So \(W_1=ab=a^2/2\). The map distance is \(\frac12a^{1/2}(1+a^2)^{1/2}\), of order \(a^{1/2}=(2W_1)^{1/4}\).

**5.2.** Take \(K=[-1,1]^2\), \(p=0\) and \(z=(1,0)\); then \(z\in[p,z]\) lies on the boundary.

**5.3.** \(P_1=\{x\in K:x\cdot(y_1-y_2)\ge c_2-c_1\}\). As \(c_2-c_1\) increases, the half-space shrinks, and its mass is continuous by dominated convergence, because the bounding hyperplanes are null. It is \(1\) when \(c_2-c_1\le\min_K x\cdot(y_1-y_2)\) and \(0\) beyond the maximum; between these values it takes every value in \((0,1)\) by continuity.

**5.4.** Put \(u^*(y)=\max_{z\in K}(z\cdot y-u(z))\), and \(\lambda=T_\#\rho\). Then \(x\cdot y\le u(x)+u^*(y)\) for \(x\in K\), and the supporting inequality gives \(z\cdot T(x)-u(z)\le x\cdot T(x)-u(x)\) for all \(z\), that is \(x\cdot T(x)=u(x)+u^*(T(x))\) for almost every \(x\). For a plan \(\pi\) from \(\rho\) to \(\lambda\), \(\int x\cdot y\,d\pi\le\int u\,d\rho+\int u^*\,d\lambda\), and the right side equals \(\int x\cdot T(x)\,d\rho\), so the plan of \(T\) maximizes \(\int x\cdot y\,d\pi\) and minimizes the quadratic cost, as in the proof of Lemma 2.1. (The last lesson uses this argument for limits of finite affine maxima.)

**5.5.** Both have masses \(\frac{1-a}2,\frac{1-a}2,a\). The support of \(\nu_a\) is \(\{-e_1,e_1,be_2\}\), with second coordinates \(0,0,b\).

## References

- [OpenAI-BS] OpenAI, *Sharp one-third stability of Brenier maps*, OpenAI Math Release preprint, 25 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026
- [Letrouit] C. Letrouit, *Unstable optimal transport maps*, Comptes Rendus. Mathématique (2026), Theorem 2 and Conjecture 3. https://doi.org/10.5802/crmath.834
- [WW] S. Wang and X. Wang, *Quantitative stability of optimal transport via regularization*, arXiv:2610.09640 (October 2026). https://arxiv.org/abs/2610.09640
- [Ruan] Y. Ruan, *Sharp conditioning and quantitative stability of optimal transport*, arXiv:2610.07577 (October 2026). https://arxiv.org/abs/2610.07577
- [Ford] W. Ford, *Quantitative stability, coercivity and uniqueness of optimal transport plans*, arXiv:2609.35574 (September 2026). https://arxiv.org/abs/2609.35574
- [HZ] B.-X. Han and Z.-N. Zhu, *Stability of optimal transport on sub-Riemannian manifolds*, arXiv:2610.09688 (October 2026), Corollary 1.2 and Theorem 1.4. https://arxiv.org/abs/2610.09688
