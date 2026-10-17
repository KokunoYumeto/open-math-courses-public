# Ehrhard's inequality for convex sets

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson deduces Theorem A of [Gaussian heat semigroups and a gradient bound](gaussian-heat-semigroups-and-a-gradient-bound.md) from Theorem 2.1 of [A quantity monotone along the heat flow](a-quantity-monotone-along-the-heat-flow.md). Three limits are needed: the smoothing time \(\varepsilon\) tends to \(0\), which turns the hypothesis of Theorem 2.1 into a pointwise inequality between uniformly continuous functions (Proposition 3.1); Lipschitz functions approximate the indicator functions of convex sets (Proposition 3.3); and the correlation \(\rho\) tends to \(1\), so that \(\sigma\to1\). Corollary 3.4 records the concavity along translates in the form used in the course [The Gaussian propeller bound](course:the-gaussian-propeller-bound/gaussian-first-moments-of-partitions).

The notation \(\lambda\), \(\mu=1-\lambda\), \(\rho\), \(\sigma\), \(\Xi\) and \(\mathcal B_N\) is that of the previous lesson. The measure-theoretic results are cited by number from Fremlin's *Measure Theory* in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): B. Levi's theorem on monotone convergence (123A), dominated convergence (123C) and the linear change of variables (263A).

## 1. A pointwise hypothesis

**Proposition 3.1.** Let \(0<\lambda<1\), \(-1<\rho<1\), \(N>0\), \(\varepsilon_3>0\), and let \(f,g,h:\mathbf R^n\to[\Phi(-N),\Phi(N)]\) be uniformly continuous with, for all \(x,y\in\mathbf R^n\),
\[
\Xi\bigl(f(x),g(y),h(\lambda x+\mu y)\bigr)\le-\varepsilon_3 .
\]
Then \(\Xi\bigl(\int f\,d\gamma_n,\int g\,d\gamma_n,\int h(\sigma w)\,d\gamma_n(w)\bigr)<0\).

*Proof.* For a bounded uniformly continuous \(k\) with modulus of continuity \(\omega_k\), and \(t,R_1>0\),
\[
\begin{aligned}
&|Q_tk(x)-k(x)|\le\omega_k(\sqrt t\,R_1)\\
&\qquad+2\sup|k|\;\gamma_n(\{|w|>R_1\}),
\end{aligned}
\]
by splitting the integral of \(|k(x+\sqrt t\,w)-k(x)|\) at \(|w|=R_1\). Choosing \(R_1\) large and then \(t\) small shows that \(Q_tk\to k\) uniformly as \(t\to0\). \(\Xi\) is Lipschitz on \(\mathcal B_N\) (its partial derivatives are bounded by \(1/\varphi(N)\) there). So for \(\varepsilon>0\) small enough, the functions \(F_{i,0}\) of Theorem 2.1, namely \(Q_\varepsilon f(x)\), \(Q_\varepsilon g(y)\) and \(Q_{\sigma^2\varepsilon}h(\lambda x+\mu y)\), satisfy \(\Xi(F_0(x,y))\le-\varepsilon_3/2\) for all \((x,y)\). Theorem 2.1 with \(\varepsilon_1=\varepsilon_3/2\) gives the conclusion. \(\square\)

## 2. Convex sets

**Lemma 3.2.** Let \(S\subseteq\mathbf R^n\) be convex. If \(S\) has an interior point \(x_0\), then:

1. for \(0<t<1\), the map \(\eta_t(y)=x_0+t(y-x_0)\) sends \(\overline S\) into the interior of \(S\);
2. \(\overline S\) and \(S\) have the same interior, and the boundary of \(S\) is Lebesgue-null.

If \(S\) has no interior point, it lies in an affine hyperplane and is Lebesgue-null. In both cases \(S\) is Lebesgue measurable, and if \(S\) has an interior point, \(\gamma_n(S)=\gamma_n(\operatorname{int}S)=\gamma_n(\overline S)\).

*Proof.* (1) Let the open ball \(B(x_0,r_0)\) lie in \(S\), let \(y\in\overline S\) and \(z=\eta_t(y)\), and let \(|v|<(1-t)r_0\). Choose \(y'\in S\) so close to \(y\) that \(w=(v+t(y-y'))/(1-t)\) has \(|w|<r_0\). Then \(z+v=ty'+(1-t)(x_0+w)\) is a convex combination of points of \(S\), so the ball of radius \((1-t)r_0\) about \(z\) lies in \(S\).

(2) If \(y\ne x_0\) is an interior point of \(\overline S\), then \(y'=y+\tau(y-x_0)\in\overline S\) for some \(\tau>0\), and \(y=\eta_t(y')\) with \(t=1/(1+\tau)\), so \(y\) is interior to \(S\) by (1). For \(R>0\) let \(S_R=\overline S\cap\overline{B(x_0,R)}\), a compact convex set with \(x_0\) in its interior. By (1) applied to \(S_R\), \(\eta_t(S_R)\) lies in the interior of \(S_R\), so the boundary of \(S_R\) lies in \(S_R\setminus\eta_t(S_R)\), whose Lebesgue measure is \((1-t^n)\) times that of \(S_R\) (263A). Letting \(t\to1\), the boundary of \(S_R\) is null. A boundary point \(y\) of \(S\) with \(|y-x_0|<R\) lies in \(S_R\) and is not interior to \(\overline S\), hence not interior to \(S_R\); so the boundary of \(S\) is null.

If \(S\) contained \(n+1\) affinely independent points, it would contain the simplex they span, which has interior points; so a convex set without interior points lies in an affine hyperplane, which is null. Finally, \(S\) differs from its interior by a subset of its boundary. \(\square\)

**Proposition 3.3.** Let \(K,L\subseteq\mathbf R^n\) be compact convex sets with interior points and \(0<\lambda<1\). Then
\[
\begin{aligned}
&\Phi^{-1}\bigl(\gamma_n(\lambda K+\mu L)\bigr)\\
&\quad\ge\lambda\Phi^{-1}(\gamma_n(K))+\mu\Phi^{-1}(\gamma_n(L)).
\end{aligned}
\]

*Proof.* \(M=\lambda K+\mu L\) is compact and convex, as the image of \(K\times L\) under \((x,y)\mapsto\lambda x+\mu y\), and has interior points; all of \(\gamma_n(K)\), \(\gamma_n(L)\), \(\gamma_n(M)\) lie in \((0,1)\). Fix \(\rho\in(0,1)\), and numbers \(m,N'>0\) and \(N\) with
\[
\begin{aligned}
\lambda N&\ge\mu m+\sigma N'+1,\\
\mu N&\ge\lambda m+\sigma N'+1,
\end{aligned}
\]
and put \(T=(m+1)/\sigma\). For \(k\ge1\) let
\[
\begin{aligned}
a_k(x)&=\min\bigl(1,k\operatorname{dist}(x,\mathbf R^n\setminus\operatorname{int}K)\bigr),\\
b_k(y)&=\min\bigl(1,k\operatorname{dist}(y,\mathbf R^n\setminus\operatorname{int}L)\bigr),\\
c_k(z)&=\max\bigl(0,1-k\operatorname{dist}(z,M)\bigr).
\end{aligned}
\]
These are Lipschitz with values in \([0,1]\); \(a_k=0\) outside \(\operatorname{int}K\), \(b_k=0\) outside \(\operatorname{int}L\), \(c_k=1\) on \(M\); as \(k\to\infty\), \(a_k\uparrow\mathbf 1_{\operatorname{int}K}\), \(b_k\uparrow\mathbf 1_{\operatorname{int}L}\) and \(c_k\downarrow\mathbf 1_M\) pointwise. Put
\[
\begin{aligned}
\alpha_k&=-N+(N+m)a_k,\\
\beta_k&=-N+(N+m)b_k,\\
\chi_k&=-N'+(N'+T)c_k,
\end{aligned}
\]
and \(f=\Phi\circ\alpha_k\), \(g=\Phi\circ\beta_k\), \(h=\Phi\circ\chi_k\). They are uniformly continuous with values in \([\Phi(-N_1),\Phi(N_1)]\), \(N_1=\max(N,N',T)\). For all \(x,y\),
\[
\begin{aligned}
&\lambda\alpha_k(x)+\mu\beta_k(y)\\
&\quad-\sigma\chi_k(\lambda x+\mu y)\le-1 .
\end{aligned}
\]
Indeed, if \(a_k(x)>0\) and \(b_k(y)>0\), then \(x\in K\), \(y\in L\), \(\lambda x+\mu y\in M\) and \(\chi_k=T\), so the left side is at most \(\lambda m+\mu m-\sigma T=-1\); if \(a_k(x)=0\), it is at most \(-\lambda N+\mu m+\sigma N'\le-1\); and likewise if \(b_k(y)=0\). Put \(p_k=\int\Phi\circ\alpha_k\,d\gamma_n\), \(p'_k=\int\Phi\circ\beta_k\,d\gamma_n\) and \(q_k=\int\Phi(\chi_k(\sigma w))\,d\gamma_n(w)\). Proposition 3.1 with \(\varepsilon_3=1\) gives
\[
\lambda\Phi^{-1}(p_k)+\mu\Phi^{-1}(p'_k)<\sigma\Phi^{-1}(q_k).
\]
Let \(k\to\infty\), and write \(\kappa_K=\gamma_n(K)\), \(\kappa_L=\gamma_n(L)\) and \(s=\gamma_n(\sigma^{-1}M)\). By B. Levi's theorem (123A) and Lemma 3.2, \(p_k\to\bar p\) and \(p'_k\to\bar p'\), and by dominated convergence (123C), \(q_k\to\bar q\), where
\[
\begin{aligned}
\bar p&=\Phi(-N)(1-\kappa_K)+\Phi(m)\kappa_K,\\
\bar p'&=\Phi(-N)(1-\kappa_L)+\Phi(m)\kappa_L,\\
\bar q&=\Phi(-N')(1-s)+\Phi(T)s.
\end{aligned}
\]
These limits lie in \((0,1)\), where \(\Phi^{-1}\) is continuous, so
\[
\lambda\Phi^{-1}(\bar p)+\mu\Phi^{-1}(\bar p')\le\sigma\Phi^{-1}(\bar q).
\]
Let \(N\to\infty\), then \(N'\to\infty\) (with \(N\) still satisfying the two conditions), then \(m\to\infty\); the limits \(\Phi(m)\kappa_K\to\kappa_K\), \(\Phi(m)\kappa_L\to\kappa_L\) and \(\Phi(T)s\to s\) stay in \((0,1)\). So
\[
\lambda\Phi^{-1}(\kappa_K)+\mu\Phi^{-1}(\kappa_L)\le\sigma\Phi^{-1}(s).
\]
Finally let \(\rho\to1\), so that \(\sigma\to1\) (Exercise 2.1 of the previous lesson). For \(w\) in the interior of \(M\), \(\sigma w\in M\) for \(\sigma\) close to \(1\); for \(w\notin M\), \(\sigma w\notin M\) for \(\sigma\) close to \(1\), as \(M\) is closed. So \(\mathbf 1_M(\sigma w)\to\mathbf 1_M(w)\) off the boundary of \(M\), which is null by Lemma 3.2, and \(\gamma_n(\sigma^{-1}M)\to\gamma_n(M)\) by dominated convergence. \(\square\)

## 3. Proof of Theorem A

Let \(K,L\) be closed convex sets with \(\gamma_n(K),\gamma_n(L)\in(0,1)\), and \(0\le\lambda\le1\). For \(\lambda=0\) or \(1\) the two sides agree. Let \(0<\lambda<1\). The set \(M=\lambda K+\mu L\) is convex, hence measurable by Lemma 3.2 (it need not be closed, Exercise 3.3). If \(\gamma_n(M)=1\), the left side is \(+\infty\). By Lemma 3.2, \(K\) and \(L\) have interior points, so for large \(R\) the compact convex sets \(K_R=K\cap\overline{B(0,R)}\) and \(L_R=L\cap\overline{B(0,R)}\) have interior points; \(\gamma_n(K_R)\uparrow\gamma_n(K)\) and \(\gamma_n(L_R)\uparrow\gamma_n(L)\) as \(R\to\infty\) by monotone convergence. Since \(\lambda K_R+\mu L_R\subseteq M\), Proposition 3.3 gives
\[
\begin{aligned}
&\Phi^{-1}(\gamma_n(M))\\
&\quad\ge\Phi^{-1}\bigl(\gamma_n(\lambda K_R+\mu L_R)\bigr)\\
&\quad\ge\lambda\Phi^{-1}(\gamma_n(K_R))+\mu\Phi^{-1}(\gamma_n(L_R)),
\end{aligned}
\]
and the right side tends to \(\lambda\Phi^{-1}(\gamma_n(K))+\mu\Phi^{-1}(\gamma_n(L))\). \(\square\)

**Corollary 3.4** (concavity along translates). Let \(K\subseteq\mathbf R^n\) be closed and convex, \(v\in\mathbf R^n\), and suppose \(p(u)=\gamma_n(K+uv)\) lies in \((0,1)\) for every \(u\in\mathbf R\). Then \(u\mapsto\Phi^{-1}(p(u))\) is concave on \(\mathbf R\).

*Proof.* Let \(u_1,u_2\in\mathbf R\), \(0\le\lambda\le1\) and \(u=\lambda u_1+\mu u_2\). Since \(\lambda K+\mu K=K\) for the convex set \(K\),
\[
\lambda(K+u_1v)+\mu(K+u_2v)=K+uv .
\]
Theorem A for the closed convex sets \(K+u_1v\) and \(K+u_2v\) gives
\[
\begin{aligned}
\Phi^{-1}(p(u))&\ge\lambda\Phi^{-1}(p(u_1))\\
&\quad+\mu\Phi^{-1}(p(u_2)).
\end{aligned}
\]
\(\square\)

## 4. Exercises

**3.1** (easy). Show that Theorem A is an equality for \(K=L\), and for parallel half-spaces \(K=\{\langle e,x\rangle\le a\}\), \(L=\{\langle e,x\rangle\le b\}\) with \(|e|=1\).

**3.2** (medium). Show that \(\log\Phi\) is concave, using \(x\Phi(x)+\varphi(x)=\int_{-\infty}^x\Phi(s)\,ds>0\), and deduce from Theorem A that \(\gamma_n(\lambda K+\mu L)\ge\gamma_n(K)^\lambda\gamma_n(L)^\mu\).

**3.3** (medium). Show that \(K=\{(x_1,x_2):x_1>0,\ x_2\ge1/x_1\}\) and \(L=\{(x_1,0):x_1\le0\}\) are closed convex subsets of \(\mathbf R^2\) whose sum \(K+L\) is the open half-plane \(\{x_2>0\}\).

**3.4** (easy). Deduce from Theorem A in dimension one that \((a,b)\mapsto\Phi^{-1}(\Phi(b)-\Phi(a))\) is concave on \(\{(a,b):a<b\}\).

## 5. Solutions

**3.1.** For \(K=L\), \(\lambda K+\mu K=K\) and both sides equal \(\Phi^{-1}(\gamma_n(K))\). For the half-spaces, \(\gamma_n(K)=\Phi(a)\), \(\gamma_n(L)=\Phi(b)\), and \(\lambda K+\mu L=\{\langle e,x\rangle\le\lambda a+\mu b\}\) has measure \(\Phi(\lambda a+\mu b)\).

**3.2.** Since \(\varphi'(x)=-x\varphi(x)\),
\[
(\log\Phi)''=\frac{\varphi'\Phi-\varphi^2}{\Phi^2}=-\frac{\varphi\,(x\Phi+\varphi)}{\Phi^2}.
\] The function \(x\Phi(x)+\varphi(x)\) has derivative \(\Phi(x)>0\) and tends to \(0\) as \(x\to-\infty\), so it equals \(\int_{-\infty}^x\Phi\) and is positive. With \(a=\Phi^{-1}(\gamma_n(K))\) and \(b=\Phi^{-1}(\gamma_n(L))\), Theorem A gives \(\gamma_n(\lambda K+\mu L)\ge\Phi(\lambda a+\mu b)\), and this is at least \(\Phi(a)^\lambda\Phi(b)^\mu\) by the concavity of \(\log\Phi\).

**3.3.** \(K\) is the region above the graph of the convex function \(1/x_1\) on \((0,\infty)\); it is convex, and closed because a limit of points of \(K\) has \(x_1>0\) (as \(x_2\ge1/x_1\) stays bounded along a convergent sequence). \(L\) is a closed half-line. A point of \(K+L\) is \((x_1+t,x_2)\) with \(t\le0\) and \(x_2\ge1/x_1>0\). Conversely, for \(c\in\mathbf R\) and \(d>0\), choose \(x_1\ge\max(c,1/d)\) with \(x_1>0\); then \((c,d)=(x_1,d)+(c-x_1,0)\) with \((x_1,d)\in K\) and \((c-x_1,0)\in L\).

**3.4.** For \(a_i<b_i\), the intervals \(K=[a_1,b_1]\) and \(L=[a_2,b_2]\) have \(\lambda K+\mu L=[\lambda a_1+\mu a_2,\lambda b_1+\mu b_2]\), and \(\gamma_1([a,b])=\Phi(b)-\Phi(a)\in(0,1)\); Theorem A is the concavity inequality for \(\psi(a,b)=\Phi^{-1}(\Phi(b)-\Phi(a))\) at the two points.

## References

- [NP] J. Neeman and G. Paouris, *An interpolation proof of Ehrhard's inequality*, arXiv:1605.07233, Section 4. https://arxiv.org/abs/1605.07233
- [E] A. Ehrhard, *Symétrisation dans l'espace de Gauss*, Mathematica Scandinavica 53 (1983), 281–301. https://journals.msp.org/mscand/article/view/1636
- D. H. Fremlin, *Measure Theory*, volumes 1 and 2, in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10).
