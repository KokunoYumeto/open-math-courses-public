# Smooth convex neighbourhoods

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The numerical range in Theorem A of [The numerical range and the Crouzeix inequality](the-numerical-range-and-the-crouzeix-inequality.md) is an arbitrary compact convex set; it can be a point or a segment. The proof works on convex domains with smooth boundaries that contain the numerical range and then shrinks them. This lesson constructs such domains, following OpenAI [OpenAI-DC, Lemma 4.1]: for a compact convex set \(K\) and \(0<\delta<1\), a bounded convex domain \(\Omega_\delta\supset K\) within distance of order \(\delta\) of \(K\), defined by a convex sum of exponentials. It also proves that the boundary of \(\Omega_\delta\) has a polar parametrization that extends holomorphically to a strip, the form in which the next lesson uses the smoothness of the boundary.

Complex numbers are identified with vectors of \(\mathbf R^2\), so that \(\operatorname{Re}(\bar\nu z)\) is the Euclidean inner product of \(\nu\) and \(z\).

## 1. The domains

Let \(K\subset\mathbf C\) be nonempty, compact and convex, with support function
\[
s_K(\nu)=\max_{z\in K}\operatorname{Re}(\bar\nu z)\qquad(|\nu|=1).
\]
Fix \(0<\delta<1\). Choose a finite set \(D_\delta\) of unit vectors that contains \(1,-1,i,-i\) and such that every unit vector lies within distance \(\delta\) of some element of \(D_\delta\). Choose \(t_\delta>0\) with \(|D_\delta|e^{-t_\delta\delta}<1\), and put
\[
\begin{aligned}
\Phi_\delta(z)&=\sum_{\nu\in D_\delta}e^{t_\delta(\operatorname{Re}(\bar\nu z)-s_K(\nu)-\delta)},\\
\Omega_\delta&=\{z\in\mathbf C:\Phi_\delta(z)<1\}.
\end{aligned}
\]

**Lemma 2.1** (OpenAI). Write \(\Phi=\Phi_\delta\) and \(\Omega=\Omega_\delta\).

1. \(K\subset\Omega\), and \(\Omega\) is open, convex and contained in the closed rectangle obtained from the smallest closed rectangle with sides parallel to the axes that contains \(K\) by moving each side outwards by \(\delta\).
2. \(\Phi\) is convex, its Hessian is positive definite everywhere, and \(\nabla\Phi\ne0\) on \(\{\Phi=1\}\).
3. \(\overline\Omega=\{\Phi\le1\}\) and \(\partial\Omega=\{\Phi=1\}\).
4. For every \(z\in\overline\Omega\), \(\operatorname{dist}(z,K)\le\varepsilon_\delta\), where \(\varepsilon_\delta=\delta(1+\operatorname{diam}K)/(1-\delta)\).

*Proof.* (1) For \(z\in K\), every exponent is at most \(-t_\delta\delta\), so \(\Phi(z)\le|D_\delta|e^{-t_\delta\delta}<1\). The set \(\Omega\) is open because \(\Phi\) is continuous, and convex because \(\Phi\) is convex (part 2). If \(\Phi(z)\le1\), every term is at most \(1\), so \(\operatorname{Re}(\bar\nu z)\le s_K(\nu)+\delta\) for all \(\nu\in D_\delta\); for \(\nu=\pm1,\pm i\) these say that \(z\) lies in that rectangle.

(2) Each term is the exponential of a real-affine function, hence convex, with Hessian \(t_\delta^2e^{(\cdot)}\nu\nu^{\mathsf T}\). The sum of these positive semidefinite matrices is positive definite, because the terms for \(\nu=1\) and \(\nu=i\) contribute positive multiples of the two coordinate projections. If \(\nabla\Phi(z)=0\), then \(z\) minimizes the convex function \(\Phi\), so \(\Phi(z)\le\Phi(k)<1\) for \(k\in K\); hence \(\nabla\Phi\ne0\) where \(\Phi=1\).

(3) \(\{\Phi\le1\}\) is closed and contains \(\Omega\). If \(\Phi(z)=1\) and \(k\in K\), convexity gives \(\Phi((1-s)z+sk)\le(1-s)+s\Phi(k)<1\) for \(0<s\le1\), so \(z\) is a limit of points of \(\Omega\) and not a point of the open set \(\Omega\). Hence \(\overline\Omega=\{\Phi\le1\}\) and \(\partial\Omega=\{\Phi=1\}\).

(4) Let \(z\in\overline\Omega\setminus K\), let \(w\in K\) be the point of \(K\) nearest to \(z\), \(d=|z-w|\) and \(\nu=(z-w)/d\). Choose \(\mu\in D_\delta\) with \(|\mu-\nu|\le\delta\), and \(v\in K\) with \(\operatorname{Re}(\bar\mu v)=s_K(\mu)\). Since \(w\) is nearest to \(z\) and the segment from \(w\) to \(v\) lies in \(K\), \(\operatorname{Re}(\bar\nu(v-w))\le0\). Then
\[
\begin{aligned}
(1-\delta)d&\le\operatorname{Re}\bigl(\bar\mu(z-w)\bigr)\\
&\le\operatorname{Re}\bigl(\bar\mu(v-w)\bigr)+\delta\\
&\le\delta|v-w|+\delta\\
&\le\delta(1+\operatorname{diam}K).
\end{aligned}
\]
The first and third inequalities use \(|\mu-\nu|\le\delta\) and \(\operatorname{Re}(\bar\nu(z-w))=d\), \(\operatorname{Re}(\bar\nu(v-w))\le0\); the second uses \(\operatorname{Re}(\bar\mu z)\le s_K(\mu)+\delta=\operatorname{Re}(\bar\mu v)+\delta\), from part 1; the last uses \(|v-w|\le\operatorname{diam}K\). \(\square\)

For example, \(\delta_j=1/(j+1)\) gives domains \(\Omega_{\delta_j}\supset K\) whose closures converge to \(K\) in the sense that \(\sup_{z\in\overline\Omega_{\delta_j}}\operatorname{dist}(z,K)\to0\).

**Lemma 2.2** (support inequality). For \(p\in\partial\Omega_\delta\) and \(z\in\overline\Omega_\delta\), \(\nabla\Phi_\delta(p)\cdot(z-p)\le0\).

*Proof.* By convexity, \(\Phi(z)\ge\Phi(p)+\nabla\Phi(p)\cdot(z-p)\), and \(\Phi(z)\le1=\Phi(p)\). \(\square\)

## 2. A polar parametrization of the boundary

Fix \(z_*\in\Omega_\delta\). For a real angle \(\theta\), the function \(r\mapsto\Phi(z_*+re^{i\theta})\) on \([0,\infty)\) is convex, less than \(1\) at \(r=0\), and larger than \(1\) for large \(r\), because \(\Omega_\delta\) is bounded. So it takes the value \(1\) at exactly one \(r=\rho(\theta)>0\): if it took it at \(r_1<r_2\), convexity would give \(\Phi(z_*+r_1e^{i\theta})\le\frac{r_2-r_1}{r_2}\Phi(z_*)+\frac{r_1}{r_2}<1\). By Lemma 2.1(3),
\[
\begin{aligned}
\Omega_\delta&=\{z_*+re^{i\theta}:0\le r<\rho(\theta)\},\\
\partial\Omega_\delta&=\{z_*+\rho(\theta)e^{i\theta}\}.
\end{aligned}
\]

We say that a bounded domain \(\Omega\) is *star-shaped with analytic polar boundary* about \(z_*\) if \(\Omega=\{z_*+re^{i\theta}:0\le r<\rho(\theta)\}\) for a positive \(2\pi\)-periodic function \(\rho\) on \(\mathbf R\) that extends to a holomorphic function on a strip \(\{|\operatorname{Im}\theta|<\eta\}\), \(\eta>0\). A *smooth convex domain* is a bounded convex domain that is star-shaped with analytic polar boundary about one of its points.

For such \(\Omega\),
\[
\begin{aligned}
\overline\Omega&=\{z_*+re^{i\theta}:0\le r\le\rho(\theta)\},\\
\partial\Omega&=\{z_*+\rho(\theta)e^{i\theta}:\theta\in\mathbf R\}.
\end{aligned}
\]
Indeed, \(f(z)=|z-z_*|-\rho(\arg(z-z_*))\) is well defined and continuous on \(\mathbf C\setminus\{z_*\}\), because \(\rho\) is continuous and \(2\pi\)-periodic, and \(\Omega\) consists of \(z_*\) and the points with \(f<0\). A point with \(f(z)=0\) is the limit of the points \(z_*+(1-1/k)(z-z_*)\) of \(\Omega\), and the points with \(f>0\) form an open set disjoint from \(\Omega\). The boundary map
\[
\gamma(\theta)=z_*+\rho(\theta)e^{i\theta}
\]
is holomorphic on the strip, with \(\gamma'(\theta)=e^{i\theta}(\rho'(\theta)+i\rho(\theta))\ne0\) for real \(\theta\).

**Proposition 2.3.** \(\Omega_\delta\) is star-shaped with analytic polar boundary about every \(z_*\in\Omega_\delta\). In particular, \(\Omega_\delta\) is a smooth convex domain.

*Proof.* Write \(\nu=e^{i\theta_\nu}\) for \(\nu\in D_\delta\). Since \(\operatorname{Re}(\bar\nu e^{i\theta})=\cos(\theta-\theta_\nu)\), the formula
\[
F(r,\theta)=\sum_{\nu\in D_\delta}e^{t_\delta(a_\nu+r\cos(\theta-\theta_\nu))}-1,
\]
with \(a_\nu=\operatorname{Re}(\bar\nu z_*)-s_K(\nu)-\delta\),
gives \(F(r,\theta)=\Phi(z_*+re^{i\theta})-1\) for real \(r,\theta\) and defines, for complex \(r\) and \(\theta\), a function that is holomorphic in each variable and continuous in both. Fix a real \(\theta_0\) and put \(\rho_0=\rho(\theta_0)\). By convexity in \(r\),
\[
\begin{aligned}
\partial_rF(\rho_0,\theta_0)&\ge\frac{F(\rho_0,\theta_0)-F(0,\theta_0)}{\rho_0}\\
&=\frac{1-\Phi(z_*)}{\rho_0}>0,
\end{aligned}
\]
so \(\rho_0\) is a simple zero of the entire function \(F(\cdot,\theta_0)\). Choose \(0<\varepsilon<\rho_0\) such that \(F(\cdot,\theta_0)\) has no other zero in \(|r-\rho_0|\le\varepsilon\). On the circle \(|r-\rho_0|=\varepsilon\), \(|F(\cdot,\theta_0)|\) has a positive minimum, and \(F\) is uniformly continuous on compact sets; so there is \(\eta_0>0\) such that for \(|\theta-\theta_0|<\eta_0\) the inequality \(|F(r,\theta)-F(r,\theta_0)|<|F(r,\theta_0)|\) holds on the circle. By Rouché's theorem, Corollary 5.4.3 of Lebl's guide in the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50), \(F(\cdot,\theta)\) then has exactly one zero \(R(\theta)\) in \(|r-\rho_0|<\varepsilon\), and by the residue theorem (Theorem 5.3.2 there)
\[
R(\theta)=\frac1{2\pi i}\oint_{|r-\rho_0|=\varepsilon}\frac{r\,\partial_rF(r,\theta)}{F(r,\theta)}\,dr .
\]
The integrand is continuous in \((r,\theta)\) and holomorphic in \(\theta\). So \(R\) is continuous, and for every closed triangle \(T\) in the disc \(|\theta-\theta_0|<\eta_0\), exchanging the order of integration and applying the Cauchy–Goursat theorem (Theorem 3.2.9 there) in \(\theta\) gives \(\oint_{\partial T}R(\theta)\,d\theta=0\); by Morera's theorem (Theorem 3.3.5 there), \(R\) is holomorphic on \(|\theta-\theta_0|<\eta_0\). For real \(\theta\), \(F(\cdot,\theta)\) is real on the real axis, so \(\overline{R(\theta)}\) is also a zero in the disc, which is symmetric about the real axis; hence \(R(\theta)\) is real and positive, and it is the unique positive zero \(\rho(\theta)\). So \(\rho\) extends holomorphically to a disc about every real point. Two such extensions agree on the intersection of their discs, which is connected and meets the real axis, by the identity theorem (Theorem 2.4.7 there). By periodicity, finitely many discs \(\{|\theta-\theta_i|<\eta_i\}\) cover \([0,2\pi]\); with a Lebesgue number \(\eta\) of this cover, the extensions combine to a holomorphic function on the strip \(\{|\operatorname{Im}\theta|<\eta\}\), which is \(2\pi\)-periodic because \(\rho\) is. \(\square\)

At \(p=\gamma(\theta)\), \(\theta\) real, differentiating \(\Phi(\gamma(\theta))=1\) gives \(\nabla\Phi(p)\cdot\gamma'(\theta)=0\): the gradient is normal to the boundary, and by Lemma 2.2 it points away from \(\overline\Omega_\delta\).

## 3. Exercises

**2.1** (easy). Show that every \(z\in\partial\Omega_\delta\) satisfies \(\operatorname{dist}(z,K)\ge\delta-(\log|D_\delta|)/t_\delta>0\).

**2.2** (easy). For the closed unit disc \(\overline{\mathbf D}\) and \(z_*=a\) with \(|a|<1\), show that, with \(\alpha(\theta)=\operatorname{Re}(\bar ae^{i\theta})\), \(\rho(\theta)=-\alpha(\theta)+\sqrt{1-|a|^2+\alpha(\theta)^2}\), and that \(\rho\) extends holomorphically to a strip.

**2.3** (medium). Let \(K=\{0\}\) and \(D_\delta\supseteq\{1,-1,i,-i\}\). Show that \(\Omega_\delta\) is symmetric under \(z\mapsto iz\) when \(D_\delta\) is, and that \(\Omega_\delta\) lies in the disc of radius \(\delta/(1-\delta)\).

**2.4** (medium). A function \(\rho\) on the real line that extends holomorphically to a strip is real-analytic. Conversely, show that a positive \(2\pi\)-periodic function given by a convergent Fourier series \(\sum_kc_ke^{ik\theta}\) with \(|c_k|\le Ce^{-\eta_1|k|}\) extends holomorphically to \(\{|\operatorname{Im}\theta|<\eta_1\}\).

## 4. Solutions

**2.1.** If \(\Phi(z)=1\), some term is at least \(1/|D_\delta|\), so for that \(\nu\), \(\operatorname{Re}(\bar\nu z)-s_K(\nu)\ge\delta-(\log|D_\delta|)/t_\delta\), which is positive by the choice of \(t_\delta\). For \(w\in K\), \(|z-w|\ge\operatorname{Re}(\bar\nu(z-w))\), and this is at least \(\operatorname{Re}(\bar\nu z)-s_K(\nu)\).

**2.2.** \(|a+re^{i\theta}|^2=1\) is the quadratic \(r^2+2r\alpha(\theta)+|a|^2-1=0\), whose positive root is the formula. The expression under the root is at least \(1-|a|^2>0\) for real \(\theta\), so it stays away from \((-\infty,0]\) on a strip, where the principal square root is holomorphic.

**2.3.** If \(iD_\delta=D_\delta\), the substitution \(\nu\mapsto i\nu\) permutes the terms of \(\Phi_\delta(iz)\), because \(s_K=0\) for \(K=\{0\}\). By Lemma 2.1(4) with \(\operatorname{diam}K=0\), \(|z|\le\delta/(1-\delta)\) on \(\overline\Omega_\delta\).

**2.4.** On \(|\operatorname{Im}\theta|\le\eta_2<\eta_1\), \(|c_ke^{ik\theta}|\le Ce^{-(\eta_1-\eta_2)|k|}\), so the series converges uniformly there, and a uniform limit of holomorphic functions is holomorphic.

## References

- [OpenAI-DC] OpenAI, *A direct proof of the complete Crouzeix inequality*, OpenAI Math Release preprint, 26 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026
