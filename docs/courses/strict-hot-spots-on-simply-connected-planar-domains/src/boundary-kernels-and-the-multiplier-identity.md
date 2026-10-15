# Boundary kernels and the multiplier identity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Through the conformal map \(\Phi\colon\mathbb D\to\Omega\), the nonnegative energy of [A variational principle for tangent vector fields](a-variational-principle-for-tangent-vector-fields.md) becomes a quadratic form \(E\) on vector data on the circle. This lesson writes \(E\) with two boundary kernels, built from the Green function of the disc and a nonnegative potential, and proves the multiplier identity: if \(g\) is the boundary gradient of a Neumann eigenfunction, then for every real Lipschitz function \(b\) on the circle
\[
\begin{aligned}
E(bg)&=\frac12\iint N(s,t)(b(s)-b(t))^2\\
&\qquad\cdot g(s)\cdot g(t)\,ds\,dt
\end{aligned}
\]
with a positive kernel \(N\). The kernel constructions in Sections 2–4 need only a bounded nonnegative potential satisfying a subcritical Dirichlet inequality.

- The Green function and Poisson kernel of the disc (Section 1).
- A subcritical potential and its Green operator (Section 2).
- The Dirichlet problem with the potential (Section 3).
- The kernels \(K\), \(R\), \(N\) and their estimates (Section 4).
- The boundary energy (Section 5).
- The multiplier identity (Section 6).

Notation is that of the earlier lessons: \(\Phi\) is the conformal map of Proposition 2.1 of [Conformal coordinates, Hopf's lemma and boundary signs](conformal-coordinates-hopfs-lemma-and-boundary-signs.md), and (SOB), (ER) apply to the disc as well as to \(\Omega\). The circle \(\mathbb S^1\) carries arclength \(ds\).

## 1. The Green function and Poisson kernel of the disc

For \(x,y\in\mathbb D\), \(x\ne y\), and \(s\in\mathbb S^1\) put
\[
\begin{gathered}
G(x,y)=\frac1{2\pi}\log\Bigl|\frac{1-x\bar y}{x-y}\Bigr|\\
=\frac1{4\pi}\log\Bigl(1+\frac{(1-|x|^2)(1-|y|^2)}{|x-y|^2}\Bigr),\\
P_s(x)=\frac{1-|x|^2}{2\pi|s-x|^2},
\end{gathered}
\]
and \(G(x,x)=+\infty\). The two expressions for \(G\) agree because \(|1-x\bar y|^2\) equals \(|x-y|^2+(1-|x|^2)(1-|y|^2)\). So \(G\) is symmetric and positive. Since \(|1-x\bar y|\le2\) and \(1-|x|^2\le2|s-x|\),
\[
\begin{gathered}
0<G(x,y)\le\tfrac1{2\pi}\log\tfrac2{|x-y|},\\
0<P_s(x)\le\tfrac1{\pi|s-x|}.
\end{gathered} \tag{1.1}
\]

**Lemma 1.1** (Poisson extension). For \(s=e^{i\varphi}\) and \(x=re^{i\theta}\in\mathbb D\),
\[
P_s(x)=\frac1{2\pi}\sum_{n\in\mathbb Z}r^{|n|}e^{in(\theta-\varphi)} .
\]
Hence \(P_s\) is harmonic and \(\int_{\mathbb S^1}P_s(x)\,ds=1\). For a Lipschitz function \(h\) on \(\mathbb S^1\) with Fourier coefficients \(\hat h_n\), the Poisson extension
\[
\begin{aligned}
Ah(x)&=\int_{\mathbb S^1}P_s(x)h(s)\,ds\\
&=\sum_n\hat h_nr^{|n|}e^{in\theta}
\end{aligned}
\]
is harmonic, continuous on \(\overline{\mathbb D}\) with boundary values \(h\), bounded by \(\max|h|\), and lies in \(H^1(\mathbb D)\) with
\[
\begin{aligned}
&\int_{\mathbb D}|\nabla Ah|^2\\
&\quad=2\pi\sum_n|n||\hat h_n|^2 .
\end{aligned} \tag{1.2}
\]
If \(h\in C^\infty(\mathbb S^1)\), then \(Ah\in C^\infty(\overline{\mathbb D})\).

*Proof.* With \(w=re^{i(\theta-\varphi)}\), the series equals \(\frac1{2\pi}\operatorname{Re}\frac{1+w}{1-w}=\frac{1-r^2}{2\pi|1-w|^2}\), and \(|1-w|=|s-x|\). Each term is harmonic, and the series converges with all derivatives uniformly on compact subsets of \(\mathbb D\); integrating over \(s\) keeps only the term \(n=0\). Since \(h\) is Lipschitz, \(\sum n^2|\hat h_n|^2<\infty\), so \(\sum|\hat h_n|<\infty\) and the series for \(Ah\) converges uniformly on \(\overline{\mathbb D}\) to a continuous function with boundary values \(h\). The bound follows from \(P_s>0\) and \(\int P_s\,ds=1\). For \(n\ne0\), \(\int_{\mathbb D}|\nabla(r^{|n|}e^{in\theta})|^2=2n^2\int_{\mathbb D}r^{2|n|-2}\), which is \(2\pi|n|\), and distinct \(n\) are orthogonal for the Dirichlet inner product by the angular integration; this gives (1.2) and convergence of the partial sums in \(H^1(\mathbb D)\). For smooth \(h\) the coefficients decrease faster than every power of \(|n|\), so every derivative of the series converges uniformly on \(\overline{\mathbb D}\). \(\square\)

**Lemma 1.2** (Green representation).

1. For \(\phi\in C^\infty_c(\mathbb D)\) and \(x\in\mathbb D\), \(\phi(x)=\int_{\mathbb D}G(x,y)(-\Delta\phi)(y)\,dy\).
2. For \(f\in L^2(\mathbb D)\), the function \(\mathcal Gf(x)=\int_{\mathbb D}G(x,y)f(y)\,dy\) is defined and continuous at every \(x\in\mathbb D\), and it is the unique \(\psi\in H^1_0(\mathbb D)\) with \(\int\nabla\psi\cdot\nabla\phi=\int f\phi\) for all \(\phi\in H^1_0(\mathbb D)\).

*Proof.* (1) For fixed \(x\), \(y\mapsto G(x,y)\) is \(-\frac1{2\pi}\log|x-y|\) plus \(\frac1{2\pi}\log|1-\bar xy|\), the real part of a holomorphic function of \(y\) on a neighbourhood of \(\overline{\mathbb D}\); so it is harmonic and smooth on \(\overline{\mathbb D}\setminus\{x\}\). Apply Green's second identity, from (SOB 1), on \(\mathbb D\setminus\overline{B(x,\varepsilon)}\). Only the small circle contributes, since \(\phi\) vanishes near \(\mathbb S^1\). On it the normal \(\nu\) points towards \(x\), \(G=-\frac1{2\pi}\log\varepsilon+O(1)\) and \(\partial_\nu G=\frac1{2\pi\varepsilon}+O(1)\). Hence \(\int_{\mathbb D}G\Delta\phi\) equals \(\lim_{\varepsilon\to0}\int(G\partial_\nu\phi-\phi\partial_\nu G)\,ds\), which is \(-\phi(x)\).

(2) By (1.1), \(G(x,\cdot)\in L^2(\mathbb D)\), and \(x\mapsto G(x,\cdot)\) is continuous into \(L^2(\mathbb D)\) by dominated convergence; so \(\mathcal Gf\) is defined and continuous, and \(\mathcal G\) is bounded on \(L^2(\mathbb D)\) because \(\iint G^2<\infty\). For \(f\in C^\infty_c(\mathbb D)\), \(\mathcal Gf\) is the convolution of \(-\frac1{2\pi}\log|\cdot|\) with \(f\) plus a function smooth on a neighbourhood of \(\overline{\mathbb D}\), so \(\mathcal Gf\in C^\infty(\overline{\mathbb D})\); it vanishes on \(\mathbb S^1\), where \(|1-x\bar y|=|x-y|\). Hence \(\mathcal Gf\in H^1_0(\mathbb D)\), and by Fubini, symmetry and (1), for \(\phi\in C^\infty_c(\mathbb D)\),
\[
\int\nabla\mathcal Gf\cdot\nabla\phi=\int\mathcal Gf\,(-\Delta\phi)=\int f\phi .
\]
By density this holds for \(\phi\in H^1_0(\mathbb D)\). The solution is unique by (B10) of [Boundary energy, local inverses, and harmonic data](course:elliptic-operators-and-boundary-problems/second-order-boundary), and the solution map is bounded from \(L^2\) into \(H^1_0\). Two bounded maps that agree on the dense subspace \(C^\infty_c(\mathbb D)\) agree on \(L^2(\mathbb D)\). \(\square\)

## 2. A subcritical potential and its Green operator

Let \(dq=a\,dx\) on \(\mathbb D\) with \(a\in L^\infty(\mathbb D)\), \(a\ge0\), and suppose that for some \(0<d<1\)
\[
\begin{gathered}
\int_{\mathbb D}|\psi|^2\,dq\le d\int_{\mathbb D}|\nabla\psi|^2\\
(\psi\in H^1_0(\mathbb D)).
\end{gathered} \tag{2.1}
\]
A subscript \(q\) on an inner product or norm refers to \(L^2(q)\). The zero measure satisfies (2.1) with any \(d\).

**Lemma 2.1** (the conformal potential). The measure \(dq=\mu|\Phi'|^2dx\) satisfies (2.1) with \(d=\mu/\lambda_D<1\).

*Proof.* For \(\psi\in C^\infty_c(\mathbb D)\), \(\psi\circ\Phi^{-1}\in C^\infty_c(\Omega)\). The Jacobian of \(\Phi\) is \(|\Phi'|^2\), and \(\nabla(f\circ\Phi)\cdot\nabla(k\circ\Phi)\) equals \(|\Phi'|^2(\nabla f\cdot\nabla k)\circ\Phi\) because \(D\Phi\) is \(|\Phi'|\) times a rotation. So \(\int_\Omega|\nabla(\psi\circ\Phi^{-1})|^2=\int_{\mathbb D}|\nabla\psi|^2\) and \(\int_\Omega|\psi\circ\Phi^{-1}|^2=\int_{\mathbb D}|\psi|^2|\Phi'|^2\). The definition of \(\lambda_D\) gives \(\int|\psi|^2dq\le(\mu/\lambda_D)\int|\nabla\psi|^2\), and density extends this to \(H^1_0(\mathbb D)\). \(\square\)

**Lemma 2.2** (the Green operator; [OpenAI-HS, Lemma 4.1]). The operator
\[
Tf(x)=\int_{\mathbb D}G(x,y)f(y)\,dq(y)
\]
is defined at every \(x\in\mathbb D\) for \(f\in L^2(q)\); \(Tf\) is the solution in \(H^1_0(\mathbb D)\) of \(-\Delta\psi=af\), with \(\int|\nabla Tf|^2=\langle Tf,f\rangle_q\), and \(T\) is a bounded self-adjoint operator on \(L^2(q)\) with \(\|T\|\le d\). The same holds with \(q\) replaced by any measure \(0\le\rho\le q\).

*Proof.* Since \(\int|af|^2\le\|a\|_\infty\|f\|_q^2\), Lemma 1.2 applies to \(af\), and \(\psi=Tf=\mathcal G(af)\) satisfies \(\int\nabla\psi\cdot\nabla\phi=\langle f,\phi\rangle_q\) for \(\phi\in H^1_0(\mathbb D)\). With \(\phi=\psi\) and (2.1),
\[
\begin{aligned}
\|\psi\|_q^2&\le d\int|\nabla\psi|^2=d\langle f,\psi\rangle_q\\
&\le d\|f\|_q\|\psi\|_q,
\end{aligned}
\]
so \(\|Tf\|_q\le d\|f\|_q\). Symmetry of \(G\) and Fubini give \(\langle Tf,g\rangle_q=\langle f,Tg\rangle_q\). A measure \(\rho\le q\) has a density \(0\le a_\rho\le a\) and satisfies (2.1) with the same \(d\). \(\square\)

## 3. The Dirichlet problem with the potential

**Lemma 3.1.** For a Lipschitz function \(h\) on \(\mathbb S^1\), the function
\[
\begin{aligned}
W_h&=Ah\\
&\quad+T(I-T)^{-1}Ah
\end{aligned} \tag{3.1}
\]
belongs to \(H^1(\mathbb D)\), has trace \(h\), and satisfies \(\int\nabla W_h\cdot\nabla\phi=\langle W_h,\phi\rangle_q\) for all \(\phi\in H^1_0(\mathbb D)\); it is the only function with these properties. In \(L^2(q)\), \(W_h=(I-T)^{-1}Ah\). If \(q\) has a density in \(C^\infty(\overline{\mathbb D})\) and \(h\in C^\infty(\mathbb S^1)\), then \(W_h\in C^\infty(\overline{\mathbb D})\).

*Proof.* \(Ah\) is bounded, hence in \(L^2(q)\), and \((I-T)^{-1}=\sum_{n\ge0}T^n\) converges in operator norm. Put \(F=(I-T)^{-1}Ah\) and \(\psi=TF\in H^1_0(\mathbb D)\). Then \(F=Ah+TF=W_h\) in \(L^2(q)\). Since \(Ah\) is harmonic and in \(H^1(\mathbb D)\), \(\int\nabla Ah\cdot\nabla\phi=0\) for \(\phi\in H^1_0(\mathbb D)\), and so
\[
\begin{aligned}
\int\nabla W_h\cdot\nabla\phi&=\int\nabla\psi\cdot\nabla\phi\\
&=\langle F,\phi\rangle_q=\langle W_h,\phi\rangle_q .
\end{aligned}
\]
The difference \(\delta\) of two solutions lies in \(H^1_0(\mathbb D)\) and satisfies \(\int|\nabla\delta|^2=\|\delta\|_q^2\le d\int|\nabla\delta|^2\), so \(\delta=0\). For smooth data, \(\psi=W_h-Ah\in H^1_0(\mathbb D)\) satisfies \(\int\nabla\psi\cdot\nabla\phi=\int a(Ah+\psi)\phi\), with \(a(Ah+\psi)\in H^1(\mathbb D)\); (ER D) on the disc, applied repeatedly with (SOB 4), gives \(\psi\in C^\infty(\overline{\mathbb D})\). \(\square\)

For vector data \(h\colon\mathbb S^1\to\mathbb R^2\), \(Ah\) and \(W_h\) are defined componentwise.

## 4. The kernels and their estimates

For a nonnegative function \(f\) on \(\mathbb D\) and \(n\ge1\), \(T^nf\) denotes the iterated integral \(T(T^{n-1}f)\) with values in \([0,\infty]\), and \(T^0f=f\). For \(p\in\mathbb D\) and distinct \(s,t\in\mathbb S^1\) define
\[
\begin{gathered}
K(p,s)=\sum_{n\ge0}(T^nP_s)(p),\\
R(s,t)=\sum_{n\ge0}\int_{\mathbb D}P_s\,T^nP_t\,dq,\\
N(s,t)=N_0(s,t)+R(s,t),\\
N_0(s,t)=\frac1{\pi|s-t|^2}.
\end{gathered}
\]
These are sums of nonnegative iterated integrals; the section \(P_s\) need not belong to \(L^2(q)\), and no operator is applied to it before the first smoothing.

**Lemma 4.1** ([OpenAI-HS, Lemma 4.2]).

1. \(\sup_{s}\sup_{x\in\mathbb D}TP_s(x)<\infty\), and \((T^nP_s)(p)\le Cd^{n-2}\) for \(n\ge2\), with \(C\) independent of \(p\) and \(s\).
2. For fixed \(p\), \(K(p,\cdot)\) is positive and bounded on \(\mathbb S^1\).
3. \(R\) is symmetric, nonnegative and finite off the diagonal, and its integral satisfies (4.1) below.
4. For Lipschitz data \(h\), \(k\) on \(\mathbb S^1\) and \(p\in\mathbb D\), the representations (4.2) below hold, with \(R=R(s,t)\) in the double integral.

\[
\iint R(s,t)\,ds\,dt\le\frac{q(\mathbb D)}{1-d}, \tag{4.1}
\]
\[
\begin{aligned}
&W_h(p)\\
&\ \ =\int_{\mathbb S^1}K(p,s)h(s)\,ds,\\
&\langle Ah,(I-T)^{-1}Ak\rangle_q\\
&\ \ =\iint R\,h(s)\cdot k(t)\,ds\,dt.
\end{aligned} \tag{4.2}
\]

The same statements hold with \(q\) replaced by a measure \(0\le\rho\le q\), for the kernels \(K^\rho\), \(R^\rho\), \(N^\rho\) built from \(\rho\).

*Proof.* (1) By (1.1), \(\int_{\mathbb D}P_s^{3/2}\le\pi^{-3/2}\int_{|y-s|<2}|y-s|^{-3/2}dy\) and \(\int_{\mathbb D}G(x,\cdot)^3\), which is at most \((2\pi)^{-3}\int_{|y-x|<2}\log^3\frac2{|x-y|}\,dy\), are bounded independently of \(s\) and \(x\). Hölder's inequality with exponents \(3\) and \(3/2\) gives \(TP_s(x)\le\|a\|_\infty\|G(x,\cdot)\|_{L^3}\|P_s\|_{L^{3/2}}\le C\). So \(F_s=TP_s\) is bounded, \(F_s\in L^2(q)\), and for \(n\ge2\)
\[
\begin{aligned}
(T^nP_s)(p)&=\langle G(p,\cdot),T^{n-2}F_s\rangle_q\\
&\le\|G(p,\cdot)\|_q\,d^{n-2}\|F_s\|_q\\
&\le Cd^{n-2},
\end{aligned}
\]
since \(\|G(p,\cdot)\|_q^2\le\|a\|_\infty\int G(p,\cdot)^2\) is bounded uniformly in \(p\).

(2) Positivity comes from the term \(P_s(p)>0\); boundedness from (1) and \(P_s(p)\le(1+|p|)/(2\pi(1-|p|))\).

(3) For \(s\ne t\), \(\int P_sP_t\,dq<\infty\): near each pole the other factor is bounded and \(|y-s|^{-1}\) is integrable in two dimensions. For \(n\ge1\), \(\int P_sT^nP_t\,dq\le\sup T^nP_t\cdot\|a\|_\infty\int P_s\,dy\), which is summable by (1). Reversing the chain of nonnegative integrals and using the symmetry of \(G\) shows \(R(s,t)=R(t,s)\). By Tonelli and \(\int P_s\,ds=1\),
\[
\begin{aligned}
\iint R\,ds\,dt&=\sum_{n\ge0}\langle\mathbf 1,T^n\mathbf 1\rangle_q\\
&\le\sum_{n\ge0}d^n\|\mathbf 1\|_q^2=\frac{q(\mathbb D)}{1-d}.
\end{aligned}
\]

(4) In \(L^2(q)\), \(T(I-T)^{-1}Ah=\sum_{n\ge1}T^nAh\), and evaluation at \(p\) of \(Tg=\langle G(p,\cdot),g\rangle_q\) is continuous on \(L^2(q)\); so \(W_h(p)=\sum_{n\ge0}(T^nAh)(p)\). By Fubini, \((T^nAh)(p)=\int(T^nP_s)(p)h(s)\,ds\), and the sum over \(n\) is dominated by \(\max|h|\sum_n(T^n\mathbf 1)(p)<\infty\). The second formula follows in the same way from \(\langle Ah,(I-T)^{-1}Ak\rangle_q=\sum_n\langle Ah,T^nAk\rangle_q\), with domination by \(\max|h|\max|k|\iint R\). \(\square\)

## 5. The boundary energy

From now on \(q\) is the conformal potential of Lemma 2.1. A vector function \(h\) on \(\mathbb S^1\) is *tangent* if \(h(s)\) is parallel to \(\tau(\Phi(s))\) for every \(s\). For tangent Lipschitz \(h\) put
\[
\begin{gathered}
X_h=W_h\circ\Phi^{-1},\\
E(h,k)=\mathcal E(X_h,X_k),\\
E(h)=E(h,h),
\end{gathered}
\]
where \(\mathcal E\) is the form of Corollary 1.2 of [A variational principle for tangent vector fields](a-variational-principle-for-tangent-vector-fields.md). The field \(X_h\in H^1(\Omega;\mathbb R^2)\) is tangent, with trace \(h\circ\Phi^{-1}\). By that corollary, with \(\nabla V=\{\nabla v:v\in V\}\),
\[
\begin{gathered}
E(h)\ge0,\\
E(h)=0\iff X_h\in\nabla V.
\end{gathered} \tag{5.1}
\]

**Lemma 5.1** (Douglas's identity). For Lipschitz \(h,k\colon\mathbb S^1\to\mathbb R^m\),
\[
\begin{aligned}
&\int_{\mathbb D}\nabla Ah:\nabla Ak\\
&\quad=\frac12\iint N_0(s,t)\,(h(s)-h(t))\\
&\qquad\cdot(k(s)-k(t))\,ds\,dt .
\end{aligned}
\]

*Proof.* By polarization and componentwise application it suffices to take \(h=k\) scalar. Both sides are Hermitian forms on the coefficient sequences that are diagonal in the Fourier modes: the left side by (1.2), the right side because \(N_0(s,t)\) depends only on \(s\bar t\). For \(h=s^n\), the left side is \(2\pi|n|\), and with \(w=t/s\),
\[
\begin{aligned}
&\iint\frac{|s^n-t^n|^2}{|s-t|^2}\,ds\,dt\\
&\quad=2\pi\int_{\mathbb S^1}\Bigl|\sum_{j=0}^{|n|-1}w^j\Bigr|^2dw=(2\pi)^2|n|,
\end{aligned}
\]
so the right side is also \(2\pi|n|\). This proves the identity for trigonometric polynomials. For a Lipschitz \(h\), the Fejér means \(h_N\) are trigonometric polynomials with coefficients \(\hat h_n(1-|n|/(N+1))\) for \(|n|\le N\); they converge uniformly to \(h\), and \(\operatorname{Lip}(h_N)\le\operatorname{Lip}(h)\) because the Fejér kernel is a positive kernel of total mass one. The left side for \(h_N\) converges to that for \(h\) by (1.2) and monotone convergence, and the right side by dominated convergence, since \(N_0(s,t)|h_N(s)-h_N(t)|^2\le\operatorname{Lip}(h)^2/\pi\). \(\square\)

**Lemma 5.2** (the boundary energy; [OpenAI-HS, Lemma 4.3]). For tangent Lipschitz \(h,k\), with \(\Delta h=h(s)-h(t)\), \(\Delta k=k(s)-k(t)\), \(N_0=N_0(s,t)\) and \(R=R(s,t)\),
\[
\begin{aligned}
&E(h,k)\\
&\ =\tfrac12\iint N_0\,\Delta h\cdot\Delta k\,ds\,dt\\
&\ \ -\iint R\,h(s)\cdot k(t)\,ds\,dt\\
&\ \ +\int_{\mathbb S^1}|\Phi'|(\kappa\circ\Phi)\,h\cdot k\,ds.
\end{aligned} \tag{5.2}
\]

*Proof.* *Smooth data.* Let \(h,k\) be tangent and smooth. By Lemma 3.1, \(W_h,W_k\in C^\infty(\overline{\mathbb D})\), so \(X_h,X_k\in C^\infty(\overline\Omega)\), and Lemma 2.1 of the previous lesson, polarized, gives
\[
\begin{aligned}
E(h,k)&=\int_\Omega\nabla X_h:\nabla X_k\\
&\quad+\int_{\partial\Omega}\kappa X_h\cdot X_k\,ds\\
&\quad-\mu\int_\Omega X_h\cdot X_k .
\end{aligned}
\]
By the conformal change of variables in the proof of Lemma 2.1, applied to each component, the first term is \(\int_{\mathbb D}\nabla W_h:\nabla W_k\) and the last is \(\langle W_h,W_k\rangle_q\); the boundary term is the last term of (5.2), since arclength on \(\partial\Omega\) is \(|\Phi'|\,ds\). Since \(W_h-Ah\in H^1_0(\mathbb D)\), the equation for \(W_k\) lets us replace \(W_h\) by \(Ah\) in \(\int\nabla W_h:\nabla W_k-\langle W_h,W_k\rangle_q\); then, \(Ah\) being harmonic, \(W_k\) may be replaced by \(Ak\) in the gradient term. Using \(W_k=(I-T)^{-1}Ak\) in \(L^2(q)\), we get
\[
\int\nabla Ah:\nabla Ak-\langle Ah,(I-T)^{-1}Ak\rangle_q,
\]
and Lemma 5.1 and (4.2) give the first two terms of (5.2).

*Lipschitz data.* Write \(h=c\,(\tau\circ\Phi)\) with a scalar Lipschitz function \(c\), and let \(h_n=c_n(\tau\circ\Phi)\), where \(c_n\) are smooth convolutions of \(c\) along the circle. Then \(h_n\to h\) uniformly, with uniformly bounded Lipschitz constants, so \(\int|\nabla A(h_n-h)|^2\to0\) by Lemma 5.1 and dominated convergence. Also \(A(h_n-h)\to0\) uniformly, hence in \(L^2(q)\). Since \(\int|\nabla TF|^2=\langle TF,F\rangle_q\le d\|F\|_q^2\), (3.1) gives \(W_{h_n}\to W_h\) in \(H^1(\mathbb D)\), so \(X_{h_n}\to X_h\) in \(H^1(\Omega)\) and \(E(h_n,k_n)\to E(h,k)\) for the corresponding approximations of \(k\). The right side of (5.2) converges by dominated convergence, using \(|h_n(s)-h_n(t)|\le C|s-t|\) and the integrability of \(R\). \(\square\)

## 6. The multiplier identity

Fix \(0\ne u\in V\) and put
\[
\begin{gathered}
g(s)=(\nabla u)(\Phi(s))\\
(s\in\mathbb S^1).
\end{gathered} \tag{6.1}
\]
It is smooth and, by the Neumann condition, tangent.

**Lemma 6.1.** \(W_g=(\nabla u)\circ\Phi\), and \(E(g)=0\).

*Proof.* Each \(\partial_iu\in C^\infty(\overline\Omega)\) satisfies \(\Delta\partial_iu+\mu\partial_iu=0\). Since \(\Delta(f\circ\Phi)=|\Phi'|^2(\Delta f)\circ\Phi\) for holomorphic \(\Phi\), the function \(w=(\partial_iu)\circ\Phi\in C^\infty(\overline{\mathbb D})\) satisfies \(-\Delta w=\mu|\Phi'|^2w=aw\), and its trace is \(g_i\). By the uniqueness in Lemma 3.1, \(w=W_{g_i}\). So \(X_g=\nabla u\), and \(E(g)=0\) by Proposition 1.1 of the previous lesson. \(\square\)

**Proposition 6.2** (the multiplier identity; [OpenAI-HS, Proposition 4.4]). For every real Lipschitz function \(b\) on \(\mathbb S^1\), with \(\Delta b=b(s)-b(t)\),
\[
\begin{aligned}
&E(bg)=\frac12\iint N(s,t)\\
&\quad\cdot(\Delta b)^2\,g(s)\cdot g(t)\,ds\,dt .
\end{aligned} \tag{6.2}
\]

*Proof.* By Lemma 6.1 and Corollary 1.2 of the previous lesson, \(E(g,b^2g)=0\). Subtract (5.2) for the pair \((g,b^2g)\) from (5.2) for \((bg,bg)\). The curvature terms cancel. In the first term, with \(b_s=b(s)\) and \(g_s=g(s)\),
\[
\begin{aligned}
&|b_sg_s-b_tg_t|^2\\
&\quad-(g_s-g_t)\cdot(b_s^2g_s-b_t^2g_t)\\
&\quad=(b_s-b_t)^2\,g_s\cdot g_t .
\end{aligned}
\]
In the second term the integrand is \(-R(s,t)(b_sb_t-b_t^2)g_s\cdot g_t\); symmetrizing in \(s,t\) with \(R(s,t)=R(t,s)\) replaces \(b_t^2\) by \(\frac12(b_s^2+b_t^2)\), which gives \(\frac12R(s,t)(b_s-b_t)^2g_s\cdot g_t\). Adding the two terms gives (6.2). All integrals converge absolutely: \(N_0(s,t)(b_s-b_t)^2\le\operatorname{Lip}(b)^2/\pi\), and \(R\) is integrable. \(\square\)

## 7. Exercises

**7.1.** Prove that \(|1-x\bar y|^2\) equals \(|x-y|^2+(1-|x|^2)(1-|y|^2)\), and deduce that \(G(x,y)=0\) when \(|x|=1\).

**7.2.** For \(q=0\), identify \(T\), \(K\), \(R\), \(N\) and \(W_h\).

**7.3.** Let \(b(e^{i\theta})=\cos\theta\). Show \(\iint N_0(s,t)(b(s)-b(t))^2\,ds\,dt=2\pi\), with Lemma 5.1 and directly.

**7.4.** Show that \(K(p,s)\ge P_s(p)\) and \(N(s,t)\ge N_0(s,t)\), and that for \(p=0\), \(K(0,s)\ge1/(2\pi)\).

**7.5.** Let \(q\) satisfy (2.1). Show that \(\iint R(s,t)\,ds\,dt\ge q(\mathbb D)\).

## 8. Solutions

**7.1.** Expand: \(|1-x\bar y|^2=1-2\operatorname{Re}(x\bar y)+|x|^2|y|^2\), while \(|x-y|^2=|x|^2+|y|^2-2\operatorname{Re}(x\bar y)\) and \((1-|x|^2)(1-|y|^2)\) equals \(1-|x|^2-|y|^2+|x|^2|y|^2\); add the last two. If \(|x|=1\), the second form of \(G\) has \(1-|x|^2=0\).

**7.2.** \(T=0\), \(K(p,s)=P_s(p)\), \(R=0\), \(N=N_0\) and \(W_h=Ah\).

**7.3.** \(\hat b_{\pm1}=\frac12\) and the other coefficients vanish, so (1.2) gives \(\int|\nabla Ab|^2=2\pi(\frac14+\frac14)=\pi\); indeed \(Ab=x_1\). By Lemma 5.1 the double integral is \(2\pi\). Directly, for \(s=e^{i\theta}\), \(t=e^{i\varphi}\): \(|s-t|^2=4\sin^2\frac{\theta-\varphi}2\) and \(\cos\theta-\cos\varphi=-2\sin\frac{\theta+\varphi}2\sin\frac{\theta-\varphi}2\), so the integrand is \(\frac1\pi\sin^2\frac{\theta+\varphi}2\), whose integral over \([0,2\pi]^2\) is \(\frac1\pi\cdot2\pi^2=2\pi\).

**7.4.** All terms of the series defining \(K\) and \(R\) are nonnegative; the term \(n=0\) of \(K\) is \(P_s(p)\), and \(P_s(0)=1/(2\pi)\).

**7.5.** The term \(n=0\) contributes \(\iint\int P_sP_t\,dq\,ds\,dt\), which equals \(\int(\int P_s\,ds)(\int P_t\,dt)\,dq=q(\mathbb D)\), and the other terms are nonnegative.

## References

- [OpenAI-HS] OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, OpenAI Math Release preprint, 24 September 2026, Section 4 (Lemmas 4.1–4.3, Proposition 4.4). https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
