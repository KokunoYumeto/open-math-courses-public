# Quadratic mass growth

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(P\) be the separating current of [Taming, compatibility and a separating current](taming-compatibility-and-a-separating-current.md) (Proposition 5.1 there), with trace measure \(\mu\) and fiber measure \(\lambda\) on the bundle \(\mathscr C\) of unit complex-line bivectors. This lesson proves that \(\mu\) of a geodesic ball of radius \(s\) is at most \(Cs^2\), uniformly in the centre: the trace measure is at most two-dimensional, as for the area measure of a surface. The proof tests \(P\) against closed invariant forms built from two radial functions, \(\log\sqrt{s^2+t^2}\) and \(\sqrt{s^2+t^2}\), where \(t\) is the distance to the centre. The closed lift \(B\) of the first lesson makes these forms invariant, and the main work is to show that the correction \(B\) adds only errors of lower order near the centre.

- The kernel of an operator of order zero, and its action on inputs concentrated at a small scale (Lemmas 1.1 and 1.2).
- The test forms (Lemma 2.1).
- Radial functions: derivative bounds, complex-line traces, and the size of the correction (Lemmas 3.1, 3.2 and 3.3).
- Quadratic mass growth (Proposition 4.1).

The lesson follows [OpenAI-TC, Section 3]. Throughout, \(C\) and \(c\) denote positive constants that depend only on \(X\), \(J\), \(g\) and the fixed choices below, not on centres or small scales; they may change from line to line.

## 1. Operators of order zero

We use the symbol classes and quantization of [Symbols, operators and Sobolev scales](course:elliptic-boundary-reduction/euclidean-symbol-calculus) (course *Elliptic boundary reduction*): \(b\in S^0\) means \(|\partial_x^\beta\partial_\xi^\alpha b(x,\xi)|\le C_{\alpha\beta}\langle\xi\rangle^{-|\alpha|}\), and \(\operatorname{Op}(b)u(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}b(x,\xi)\hat u(\xi)\,d\xi\), with kernel \(K_b(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}b(x,\xi)\,d\xi\) in the sense of (E12) there. Matrix-valued symbols are treated componentwise.

**Lemma 1.1** (the kernel off the diagonal). Let \(b\in S^0(\mathbb R^n\times\mathbb R^n)\). Off the diagonal, \(K_b\) is a continuous function with
\[
|K_b(x,y)|\le C|x-y|^{-n}\qquad(x\ne y),
\]
where \(C\) depends on finitely many seminorms of \(b\).

*Proof.* Let \(\phi_0\in C^\infty_c\) be one for \(|\xi|\le1\) and zero for \(|\xi|\ge2\), and \(\phi_k(\xi)=\phi_0(2^{-k}\xi)-\phi_0(2^{1-k}\xi)\) for \(k\ge1\), so that \(\sum_k\phi_k=1\) and \(\phi_k\) lives where \(2^{k-1}\le|\xi|\le2^{k+1}\). Put \(b_k=b\phi_k\) and \(K_k(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}b_k(x,\xi)\,d\xi\), an absolutely convergent integral. The symbol estimates give \(|\partial_\xi^\alpha b_k|\le C_\alpha2^{-k|\alpha|}\) on a set of volume \(C2^{kn}\). Hence \(|K_k|\le C2^{kn}\), and, writing \(w=x-y\) and integrating by parts \(N\) times with \(|w|^{2N}e^{iw\cdot\xi}=(-\Delta_\xi)^Ne^{iw\cdot\xi}\),
\[
|K_k(x,y)|\le C_N2^{kn}\,(2^k|w|)^{-2N} .
\]
Choose \(2N>n\). Summing \(C2^{kn}\) over \(2^k\le|w|^{-1}\) and the second bound over \(2^k>|w|^{-1}\) gives \(C|w|^{-n}\) for both geometric sums. The series converges uniformly on \(\{|x-y|\ge\delta\}\) for every \(\delta>0\). Moreover \(\sum_{k\le K}b_k\to b\) in \(S^\varepsilon\) for every \(\varepsilon>0\), so the partial kernels converge to \(K_b\) as tempered distributions by the continuity of (E12); hence the sum is \(K_b\) off the diagonal. \(\blacksquare\)

We fix the geometry once. By Theorem B.1 of [Geodesics, normal coordinates and curvature](course:DG-FND/geodesics-normal-coordinates-and-curvature) and Theorems B.3 and B.5 of [Riemannian connections and convex neighbourhoods](course:DG-FND/riemannian-connections-and-convex-neighbourhoods) (course *Bundles, curvature and holonomy*), applied to the smooth map \((x,v)\mapsto\exp_xv\), and by compactness, there is \(\rho_0>0\) such that for every \(x\in X\) the map \(\exp_x\) is a diffeomorphism from the ball of radius \(4\rho_0\) in \(T_xX\) onto the geodesic ball \(B_{4\rho_0}(x)\), with \(d(x,\exp_xv)=|v|\). Choosing an orthonormal basis of \(T_xX\) gives *normal coordinates* \(z\) at \(x\), with \(t=d(x,\cdot)=|z|\). In normal coordinates the coefficients of \(g\), \(g^{-1}\) and \(J\), with their derivatives up to any fixed order, are bounded uniformly in \(x\) and \(|z|\le3\rho_0\); in particular Euclidean and \(g\)-lengths of vectors are comparable, \(g_{ij}(0)=\delta_{ij}\), and \(J_0=J(x)\) is an orthogonal matrix.

**Lemma 1.2** (order zero on concentrated inputs). Let \(B\) be an operator of order zero between bundles of forms on \(X\). Then:

1. its kernel is continuous off the diagonal and \(|K_B(y,z)|\le C\,d(y,z)^{-4}\);
2. if \(0<a\le\rho_0\), \(M\ge0\), and \(f\) is a smooth form supported in a geodesic ball \(B_a(y_0)\) whose components in normal coordinates at \(y_0\) satisfy \(|\partial^\gamma f|\le Ma^{-|\gamma|}\) for \(|\gamma|\le6\), then \(|Bf(y)|\le CM\) for every \(y\in X\).

*Proof.* By the definition of operators of order zero on manifolds (Sections 4, 5 and 13 of [Detecting regularity without choosing coordinates](course:elliptic-boundary-reduction/geometric-microlocal-calculus)), the kernel is smooth off the diagonal, and for cutoffs \(\phi,\psi\) supported in a chart with frames, \(\phi B\psi=\operatorname{Op}(b)+S\) in the chart, with \(b\in S^0\) and \(S\) with smooth kernel. Cover \(X\) by finitely many balls \(B_{\rho_0}(y_i)\) and take \(\phi_i=\psi_i\) equal to one on \(B_{3\rho_0}(y_i)\) with support in \(B_{4\rho_0}(y_i)\), which lies in one chart.

(1) If \(d(y,z)\ge\rho_0\), the kernel is bounded on this compact set. If \(d(y,z)<\rho_0\) and \(y\in B_{\rho_0}(y_i)\), then \(K_B(y,z)=K_{\phi_iB\psi_i}(y,z)\), and Lemma 1.1, the smooth remainder and the smooth comparison of chart coordinates with distance give the bound.

(2) If \(d(y,B_a(y_0))\ge\rho_0\), then \(|Bf(y)|\le C\|f\|_{L^1}\le CMa^4\). Otherwise \(y\) and \(B_a(y_0)\) lie in some \(B_{3\rho_0}(y_i)\), and \(Bf(y)=\operatorname{Op}(b_i)\tilde f(\tilde y)+S_if(y)\), where \(\tilde f\) is \(f\) in the chart and frame. A smooth change of coordinates and frame keeps the derivative bounds, up to constants, since \(a\le1\). Then \(|S_if(y)|\le C\|f\|_{L^1}\le CM\), and
\[
|\operatorname{Op}(b_i)\tilde f(\tilde y)|\le(2\pi)^{-4}\sup|b_i|\,\|\hat{\tilde f}\|_{L^1} .
\]
Write \(\tilde f(w)=M\,h((w-w_0)/a)\), so that \(h\) is supported in a fixed ball and has bounded derivatives of order at most six. Then \(\hat{\tilde f}(\xi)=Ma^4\hat h(a\xi)\), so \(\|\hat{\tilde f}\|_{L^1}=M\|\hat h\|_{L^1}\). Since \((1+|\eta|^2)^3\hat h(\eta)\) is the Fourier transform of \((1-\Delta)^3h\), \(|\hat h(\eta)|\le C(1+|\eta|^2)^{-3}\), which is integrable on \(\mathbb R^4\). \(\blacksquare\)

## 2. The test forms

For a smooth function \(u\) put \(d^c_Ju=-du\circ J\), and
\[
Du=(1-BR)\,dd^c_Ju ,
\]
with the closed lift \(B\) of Lemma 3.4 of the first lesson.

**Lemma 2.1.** (1) \(Du\) is a smooth closed invariant two-form, so \(P(Du)=0\). (2) In local coordinates, with \(H\) the Hessian matrix of \(u\) and \(J\) the matrix of \(J\) at a point,
\[
\begin{gathered}
dd^c_Ju=h_u+e_u,\\
h_u(a,b)=\langle HJa,b\rangle-\langle HJb,a\rangle ,
\end{gathered}
\]
where \(\langle\cdot,\cdot\rangle\) is the coordinate dot product and \(e_u=-\sum_{i,j,k}\partial_ku\,\partial_iJ^k_j\,dz^i\wedge dz^j\). The form \(h_u\) is invariant. Consequently \(R\,dd^c_Ju=Re_u\): \(R\,dd^c_J\) is a first-order differential operator with smooth coefficients and no term of order zero. (3) If \(J\) is constant, \(dd^c_Ju(v,Jv)=H(v,v)+H(Jv,Jv)\).

*Proof.* (1) \(dd^c_Ju\) is exact, hence closed; \(d(BR\beta)=0\) since \(dB=0\); and \(R(1-BR)\beta=R\beta-R\beta=0\) since \(RB=\mathrm{id}\). Proposition 5.1 of the first lesson gives \(P(Du)=0\).

(2) With \(J\partial_j=\sum_kJ^k_j\partial_k\), \(d^c_Ju=-\sum_{j,k}\partial_ku\,J^k_j\,dz^j\). Differentiating gives \(e_u\) and the form \(-\sum\partial_i\partial_ku\,J^k_j\,dz^i\wedge dz^j\), whose value on \((a,b)\) is \(h_u(a,b)\). Since \(J^2=-1\) and \(H\) is symmetric,
\[
\begin{aligned}
h_u(Ja,Jb)&=-\langle Ha,Jb\rangle+\langle Hb,Ja\rangle\\
&=\langle HJa,b\rangle-\langle HJb,a\rangle .
\end{aligned}
\]
So \(Rh_u=0\).

(3) With \(e_u=0\), \(h_u(v,Jv)=\langle HJv,Jv\rangle-\langle HJ^2v,v\rangle\). \(\blacksquare\)

## 3. Radial functions

Fix \(x\in X\), normal coordinates \(z\) at \(x\), and a smooth function \(\chi\) of \(t=|z|\), equal to one for \(t\le\rho_0\) and zero for \(t\ge2\rho_0\). For \(0<s\le\rho_0\) put
\[
\begin{gathered}
u_s=\chi\log\sqrt{s^2+t^2},\\
h_s=\chi\sqrt{s^2+t^2} ,
\end{gathered}
\]
extended by zero outside \(B_{2\rho_0}(x)\).

**Lemma 3.1** (derivative bounds). For every multi-index \(\gamma\ne0\), in normal coordinates,
\[
\begin{gathered}
|\partial^\gamma u_s|\le C_\gamma(s+t)^{-|\gamma|},\\
|\partial^\gamma h_s|\le C_\gamma(s+t)^{1-|\gamma|} .
\end{gathered}
\]

*Proof.* Where \(\chi=1\), \(\log\sqrt{s^2+t^2}=\log s+G(z/s)\) with \(G(w)=\frac12\log(1+|w|^2)\), and \(\sqrt{s^2+t^2}=sG_2(z/s)\) with \(G_2(w)=(1+|w|^2)^{1/2}\). Each derivative of \(G\) of order \(m\ge1\) is \(O((1+|w|)^{-m})\), and each derivative of \(G_2\) of order \(m\) is \(O((1+|w|)^{1-m})\). The chain rule gives \(s^{-m}(1+t/s)^{-m}=(s+t)^{-m}\) and \(s^{1-m}(1+t/s)^{1-m}=(s+t)^{1-m}\). Where \(\chi\ne1\), \(t\ge\rho_0\), and all derivatives are bounded. \(\blacksquare\)

**Lemma 3.2** (complex-line traces). Let \(J_0=J(x)\), constant in the normal coordinates, and let \(v\in\mathbb R^4\). Where \(t<\rho_0\),
\[
\begin{gathered}
dd^c_{J_0}u_s(v,J_0v)\ge\frac{2s^2|v|^2}{(s^2+t^2)^2},\\
dd^c_{J_0}h_s(v,J_0v)\ge\frac{|v|^2}{\sqrt{s^2+t^2}} ,
\end{gathered}
\]
with Euclidean lengths.

*Proof.* The Hessians are
\[
\begin{gathered}
\frac{I}{s^2+t^2}-\frac{2zz^\top}{(s^2+t^2)^2},\\
\frac{I}{\sqrt{s^2+t^2}}-\frac{zz^\top}{(s^2+t^2)^{3/2}} .
\end{gathered}
\]
\(J_0\) is orthogonal and skew, so \(v\) and \(J_0v\) are orthogonal of equal length, and \((z\cdot v)^2+(z\cdot J_0v)^2\le t^2|v|^2\). By Lemma 2.1(3),
\[
dd^c_{J_0}u_s(v,J_0v)\ge\frac{2|v|^2}{s^2+t^2}-\frac{2t^2|v|^2}{(s^2+t^2)^2} ,
\]
which is the first bound; the second is \(\ge\frac{2|v|^2}{\sqrt{s^2+t^2}}-\frac{t^2|v|^2}{(s^2+t^2)^{3/2}}\), and \(t^2\le s^2+t^2\). \(\blacksquare\)

The first trace is positive everywhere and at least \(c/s^2\) where \(t<s\), for unit \(v\). It concentrates the test on the ball \(B_s(x)\). The second is a weaker but everywhere positive term that absorbs errors.

**Lemma 3.3** (the correction; [OpenAI-TC, Lemma 3.2]). For \(y\in X\) let \(t=d(x,y)\). Then
\[
\begin{gathered}
\bigl|BR\,dd^c_Ju_s(y)\bigr|\le\frac{C}{s+t},\\
\bigl|BR\,dd^c_Jh_s(y)\bigr|\le C\bigl(1+|\log(s+t)|\bigr) .
\end{gathered}
\]

*Proof.* Let \(f=R\,dd^c_Ju_s\) and \(k=R\,dd^c_Jh_s\). By Lemma 2.1(2) and Lemma 3.1, \(f\) and \(k\) vanish outside \(B_{2\rho_0}(x)\) and, in normal coordinates at \(x\),
\[
\begin{gathered}
|\partial^\gamma f|\le C_\gamma(s+t)^{-1-|\gamma|},\\
|\partial^\gamma k|\le C_\gamma(s+t)^{-|\gamma|} .
\end{gathered}
\]
Put \(a=s+t(y)\), and first suppose \(a\le\rho_0/8\). Split the input with a smooth partition into three parts.

*Near \(y\).* On the ball of radius \(a/4\) about \(y\), \(s+t\) lies between \(\frac34a\) and \(\frac54a\) by the triangle inequality. A cutoff equal to one on the ball of radius \(a/8\) about \(y\), supported in the ball of radius \(a/4\), with derivatives \(O(a^{-|\gamma|})\), gives a piece satisfying the hypothesis of Lemma 1.2(2) with \(M=C/a\) for \(f\) and \(M=C\) for \(k\). Its contribution at \(y\) is at most \(C/a\), respectively \(C\).

*Near \(x\).* On the rest of the ball \(\{t\le2a\}\), the distance to \(y\) is at least \(a/8\), so the kernel is at most \(Ca^{-4}\) by Lemma 1.2(1). The input has \(L^1\) norm at most \(C\int_0^{2a}\rho^3(s+\rho)^{-1}d\rho\le Ca^3\) for \(f\), and \(Ca^4\) for \(k\). The contributions are again \(C/a\) and \(C\).

*Dyadic shells.* On \(\{2^ja\le t<2^{j+1}a\}\), \(j\ge1\), the distance to \(y\) is at least \(2^{j-1}a\), the kernel is \(O((2^ja)^{-4})\), the input is \(O((2^ja)^{-1})\) for \(f\) and \(O(1)\) for \(k\), and the shell has volume \(O((2^ja)^4)\). The shell contributes \(O((2^ja)^{-1})\) for \(f\), whose sum over \(j\) is \(O(a^{-1})\), and \(O(1)\) for \(k\), with \(O(1+|\log a|)\) shells before \(t\) reaches \(2\rho_0\).

If \(a>\rho_0/8\), then either \(s>\rho_0/16\) or \(t>\rho_0/16\). In both cases split the input into the part within distance \(\rho_0/64\) of \(y\), where \(s+t\ge\rho_0/64\) and Lemma 1.2(2) applies with bounded \(M\), and the rest, where the kernel is bounded and the input has bounded \(L^1\) norm. Both bounds then hold with a larger constant. The constants are uniform in \(x\), by the uniform bounds in normal coordinates. \(\blacksquare\)

## 4. Quadratic mass growth

**Proposition 4.1** ([OpenAI-TC, Proposition 3.1]). There is a constant \(C\) such that
\[
\mu(B_s(x))\le Cs^2
\]
for every \(x\in X\) and every \(s>0\).

*Proof.* Fix \(x\), normal coordinates, \(0<s\le\rho_0\), and a point \(y\) with \(t=d(x,y)<\rho_0\). Let \(v\) be a \(g\)-unit vector at \(y\) and \(J=J(y)\). We compare \(dd^c_J\) at \(y\) with \(dd^c_{J_0}\). By Lemma 2.1(2), the Hessian parts differ on \((v,Jv)\) and \((v,J_0v)\) by
\[
H(Jv,Jv)-H(J_0v,J_0v) ,
\]
which is at most \(C|H|\,|J-J_0|\le C|H|t\), since \(J\) is smooth in the normal coordinates. The first-order part \(e_u\) is at most \(C|\nabla u|\). By Lemma 3.1, for \(u_s\) the two errors are \(Ct(s+t)^{-2}\) and \(C(s+t)^{-1}\), and for \(h_s\) they are bounded. Together with Lemmas 3.2 and 3.3, and with \(|v|\) comparable to one in Euclidean length,
\[
\begin{aligned}
Du_s(v,Jv)&\ge\frac{c}{s^2}\mathbf 1_{\{t<s\}}-\frac{C}{s+t},\\
Dh_s(v,Jv)&\ge\frac{c'}{s+t}\\
&\quad-C\bigl(1+|\log(s+t)|\bigr).
\end{aligned}
\]
For the first line we used \(2s^2/(s^2+t^2)^2\ge1/(2s^2)\) when \(t<s\). Since \((s+t)|\log(s+t)|\to0\), there is \(a_1>0\) such that the second line is at least \(c'/(2(s+t))\) when \(s+t\le a_1\). Fix \(A=2C/c'\). Then, when \(s+t\le a_1\),
\[
D(u_s+Ah_s)(v,Jv)\ge\frac{c}{s^2}\mathbf 1_{B_s(x)}(y) .
\]
When \(s\le a_1/2\) and \(s+t>a_1\), then \(t>a_1/2\), so \(y\notin B_s(x)\), and all terms are bounded: \(u_s\), \(h_s\) and their first and second derivatives are bounded there uniformly in \(s\), and the corrections are bounded by Lemma 3.3. Hence, for \(s\le a_1/2\), every \(y\in X\) and every unit \(v\) at \(y\),
\[
\begin{aligned}
&D(u_s+Ah_s)(v,Jv)\\
&\quad\ge\frac{c}{s^2}\mathbf 1_{B_s(x)}(y)-C' .
\end{aligned}
\]
Every \(\ell\in\mathscr C_y\) is \(v\wedge Jv\) for a unit \(v\). By Lemma 2.1(1) and the integral formula for \(P\),
\[
\begin{aligned}
0&=P\bigl(D(u_s+Ah_s)\bigr)\\
&=\int_{\mathscr C}D(u_s+Ah_s)_y(\ell)\,d\lambda(y,\ell) .
\end{aligned}
\]
The right side is at least \(\frac{c}{s^2}\mu(B_s(x))-C'\), because \(\lambda\) is a probability measure with projection \(\mu\). Thus \(\mu(B_s(x))\le(C'/c)s^2\) for \(s\le a_1/2\). For larger \(s\), \(\mu(B_s(x))\le1\le(2/a_1)^2s^2\). \(\blacksquare\)

Two features of the proof matter later. The bound is uniform in the centre, and it uses only that \(P\) annihilates the closed invariant forms \(Du\). The next lessons use it in the form of dyadic sums: for every \(y\) and \(r>0\),
\[
\int_X\Bigl(1+\frac{d(x,y)}{r}\Bigr)^{-6}d\mu(x)\le Cr^2 ,
\]
because the ball \(B_r(y)\) has mass at most \(Cr^2\) and the shell where \(2^jr\le d<2^{j+1}r\) has mass \(O(4^jr^2)\) and weight at most \(2^{-6j}\) (Exercise 5.4).

## 5. Exercises

**5.1.** Show that \(\mu\) has no atoms, and more generally that \(\mu(E)=0\) for every Borel set \(E\) that can be covered, for each \(\varepsilon>0\), by countably many balls \(B_{s_k}(x_k)\) with \(\sum_ks_k^2<\varepsilon\).

**5.2.** For constant \(J_0\) orthogonal on \(\mathbb R^4\), show that \(dd^c_{J_0}(|z|^2/2)=2F_0\), where \(F_0(a,b)=\langle J_0a,b\rangle\).

**5.3.** Show that for \(0<r\le1\) and \(2N>n\), \(\sum_{k\ge0}2^{kn}\min\bigl(1,(2^kr)^{-2N}\bigr)\le C_{n,N}r^{-n}\).

**5.4.** Prove the dyadic bound \(\int_X(1+d(x,y)/r)^{-6}\,d\mu(x)\le Cr^2\) stated after Proposition 4.1.

**5.5.** Using only \(u_s\), the proof gives \(\frac{c}{s^2}\mu(B_s(x))\le C\int_X\frac{d\mu(y)}{s+d(x,y)}\). Explain why this alone does not bound \(\mu(B_s(x))\) by \(Cs^2\), and how the term \(Ah_s\) removes the difficulty.

## 6. Solutions

**5.1.** If \(E\subseteq\bigcup_kB_{s_k}(x_k)\), Proposition 4.1 gives \(\mu(E)\le C\sum_ks_k^2<C\varepsilon\). A point is covered by one ball of any radius \(s\), so it has measure at most \(Cs^2\) for every \(s\).

**5.2.** The Hessian of \(|z|^2/2\) is the identity, so by Lemma 2.1(2), \(dd^c_{J_0}(|z|^2/2)(a,b)=\langle J_0a,b\rangle-\langle J_0b,a\rangle\). Since \(J_0\) is orthogonal with \(J_0^2=-1\), it is skew, so this is \(2\langle J_0a,b\rangle\).

**5.3.** Let \(2^{k_0}\le r^{-1}<2^{k_0+1}\). The terms with \(k\le k_0\) sum to at most \(2^{(k_0+1)n}\le2^nr^{-n}\). For \(k>k_0\) the terms are \(2^{kn}(2^kr)^{-2N}=r^{-2N}2^{-k(2N-n)}\), a geometric series bounded by \(Cr^{-2N}2^{-k_0(2N-n)}\le Cr^{-n}\).

**5.4.** The ball \(B_r(y)\) contributes at most \(\mu(B_r(y))\le Cr^2\). The shell where \(2^jr\le d(x,y)<2^{j+1}r\) has mass at most \(C4^{j+1}r^2\), and there the integrand is at most \((1+2^j)^{-6}\le2^{-6j}\). The sum \(\sum_j4^{j+1}2^{-6j}\) converges.

**5.5.** The right side \(\int(s+d(x,y))^{-1}d\mu(y)\) can be as large as \(\mu(B_s(x))/s\) when the mass sits near \(x\), and bounding it already requires control of \(\mu\) on small balls. The function \(h_s\) contributes \(Ac'/(2(s+t))\), which dominates the negative term \(C/(s+t)\) pointwise, so no integral of \((s+t)^{-1}\) against \(\mu\) needs to be estimated.

## References

- [OpenAI-TC] OpenAI, *Taming implies compatibility on four-manifolds*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026
