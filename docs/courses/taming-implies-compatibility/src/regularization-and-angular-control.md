# Regularization and angular control

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(P\), \(Q\), \(T=P+Q\), \(\lambda\) and \(\mu\) be as in Proposition 5.1 of [Taming, compatibility and a separating current](taming-compatibility-and-a-separating-current.md). This lesson proves that the correction \(Q\) is square integrable, and that nearby complex lines of \(P\) are close on average: the *angular integral*
\[
\mathcal I_r=\iint_{d(x,y)<r}|\ell-\tau_{yx}m|^2\,d\lambda\,d\lambda
\]
is at most \(Cr^4\); here \((x,\ell)\) and \((y,m)\) both range over \(\mathscr C\) with the measure \(\lambda\), and \(\tau_{yx}\) is parallel transport along the shortest geodesic from \(y\) to \(x\). Both statements come from one identity. A closed current paired with the Hodge star of a regularization of another closed current gives zero; for \(T\) paired with itself, the positive part \(P\) contributes the angular integral with a positive weight, up to an error that quadratic mass growth controls.

- The Hodge Laplacian, its resolvent powers \(S_r=(1+r^2\Delta)^{-3}\), and their mapping properties (Lemmas 1.1 and 1.2).
- The zero pairing of closed currents (Lemma 2.1).
- A named hypothesis on the heat kernel, and the kernel of \(S_r^2\) (Lemma 3.1).
- The angular identity and a lower bound for the pairing (Lemmas 4.1 and 4.2).
- Mixing of invariant and anti-invariant parts (Lemma 5.1).
- Square integrability of \(Q\), the angular bound, and vanishing cross terms (Proposition 6.1).

The lesson follows [OpenAI-TC, Section 4]. Elliptic operators are those of [Symbols, finite defects, and the index on a closed manifold](course:elliptic-boundary-reduction/global-elliptic-symbol-index) (course *Elliptic boundary reduction*), and \(\rho_0\) and normal coordinates are as in [Quadratic mass growth](quadratic-mass-growth.md). All forms are real, \(\langle\cdot,\cdot\rangle\) and \(\|\cdot\|\) denote the \(L^2\) product and norm unless a point is indicated, and \(0<r\le1\).

## 1. The Hodge Laplacian and its resolvent powers

Let \(\Delta=dd^*+d^*d\) act on forms of every degree.

**Lemma 1.1.** (1) \(\Delta\) is formally self-adjoint, \(\langle\Delta\alpha,\alpha\rangle=\|d\alpha\|^2+\|d^*\alpha\|^2\), and \(\Delta\) is elliptic of order two with principal symbol \(|\xi|^2\). It commutes with \(d\) and \(d^*\), and with \(*\) on two-forms. (2) The square integrable two-forms have an orthonormal basis of smooth eigenforms, \(\Delta\varphi_j=\lambda_j\varphi_j\), with \(\lambda_j\ge0\) and \(\lambda_j\to\infty\). (3) For every integer \(k\ge0\), \(\|u\|_{H^{2k}}\) and \(\|(1+\Delta)^ku\|\) are equivalent norms on \(H^{2k}\). (4) For every real \(s\) and every \(v\in H^{s+1}\), \(\|v\|_{H^s}^2\le C_s\|v\|_{H^{s-1}}\|v\|_{H^{s+1}}\).

*Proof.* (1) The first two claims are integration by parts. The symbols of \(d\) and \(d^*\) are \(i\xi\wedge\) and \(-i\iota_\xi\), and \(\xi\wedge\iota_\xi+\iota_\xi\,\xi\wedge=|\xi|^2\). Next, \(d\Delta=dd^*d=\Delta d\), and likewise for \(d^*\). In dimension four \(d^*=-*d*\) in every degree, and a direct expansion, using \(**=1\) on two-forms and \(**=-1\) on one- and three-forms, gives \(*\Delta=\Delta*\) on two-forms.

(2) By (1), \(1+\Delta\) is elliptic, and it is injective on every Sobolev space: by (I5) of the lesson cited above a solution of \((1+\Delta)u=0\) is smooth, and then \(\|u\|^2+\|du\|^2+\|d^*u\|^2=0\). Being formally self-adjoint, it is surjective by (I7). So \(K=(1+\Delta)^{-1}\) maps \(L^2\) into \(H^2\); it is compact on \(L^2\) by (I2), self-adjoint, positive and injective. By Theorem 6.2 of [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators) (course *Foundations of von Neumann algebras*), \(L^2\) has an orthonormal basis of eigenvectors of \(K\) with eigenvalues \(\kappa_j\to0\), \(\kappa_j>0\). Then \(\varphi_j\) is smooth by elliptic regularity, and \(\lambda_j=\kappa_j^{-1}-1\ge0\).

(3) \((1+\Delta)^k\) is elliptic of order \(2k\) and injective as in (2), hence an isomorphism \(H^{2k}\to L^2\) with bounded inverse.

(4) On \(\mathbb R^4\), Cauchy–Schwarz gives
\[
\begin{aligned}
\int\langle\xi\rangle^{2s}|\hat v|^2&\le\Bigl(\int\langle\xi\rangle^{2s-2}|\hat v|^2\Bigr)^{1/2}\\
&\quad\times\Bigl(\int\langle\xi\rangle^{2s+2}|\hat v|^2\Bigr)^{1/2} .
\end{aligned}
\] The norm of \(H^s(X)\) is equivalent to the square root of the sum of the squared local norms of \(\chi_iv\) for a fixed partition (Section 1 of the lesson on the index on a closed manifold), and Cauchy–Schwarz for the finite sum gives the claim. \(\blacksquare\)

For a bounded Borel function \(f\) on \([0,\infty)\) put \(f(\Delta)u=\sum_jf(\lambda_j)\langle u,\varphi_j\rangle\varphi_j\) on square integrable two-forms. In particular
\[
S_r=(1+r^2\Delta)^{-3},\qquad e^{-\varepsilon\Delta}\quad(\varepsilon>0) .
\]

**Lemma 1.2** (resolvent powers). For \(0<r\le1\):

1. \(S_r\) is self-adjoint on \(L^2\), \(\|S_r\|\le1\), \(S_r*=*S_r\), and \(dS_r=S_rd\) and \(d^*S_r=S_rd^*\) on smooth forms of all degrees.
2. \(A_r=(1+r^2\Delta)^3\) is an isomorphism \(H^{s}\to H^{s-6}\) for every \(s\), and \(S_r\) is the restriction of its inverse to \(L^2\). In particular \(S_r\) extends to a continuous map \(H^{-4}\to H^2\), self-adjoint for the duality, with \((S_rW)(\alpha)=W(S_r\alpha)\).
3. \(\|S_ru\|_{H^k}\le C_kr^{-k}\|u\|\) for \(u\in L^2\) and \(0\le k\le6\).
4. For smooth \(\alpha\), \(S_r\alpha\to\alpha\) in every \(H^s\) as \(r\to0\); for \(u\in L^2\), \(S_ru\to u\) in \(L^2\).
5. \(e^{-\varepsilon\Delta}\) maps \(L^2\) into smooth forms, \(e^{-\varepsilon\Delta}u\to u\) in \(L^2\) as \(\varepsilon\to0\), and \(\langle e^{-\varepsilon\Delta}u,d\gamma\rangle=\langle u,d\,e^{-\varepsilon\Delta}\gamma\rangle\) for smooth one-forms \(\gamma\).

*Proof.* (1) The operator \(f(\Delta)\) is self-adjoint with norm \(\sup|f|\le1\). Since \(*\) maps eigenforms to eigenforms with the same eigenvalue, it commutes with \(f(\Delta)\). For smooth \(\alpha\), the expansion \(\sum\langle\alpha,\varphi_j\rangle\varphi_j\) converges in every \(H^{2k}\) by Lemma 1.1(3), and \(d\varphi_j\) is either zero or an eigenform with eigenvalue \(\lambda_j\); this gives \(dS_r=S_rd\), and similarly for \(d^*\).

(2) \(A_r\) is elliptic of order six and injective, so it is an isomorphism on the Sobolev scale. On \(L^2\) it acts diagonally, so \(A_r^{-1}=S_r\) there, and the duality statement follows from the formal self-adjointness of \(A_r\).

(3) For \(k=2i\), Lemma 1.1(3) and \(\sup_{\lambda\ge0}\lambda^j(1+r^2\lambda)^{-3}\le r^{-2j}\) for \(j\le3\) give
\[
\begin{aligned}
\|S_ru\|_{H^{2i}}&\le C\sum_{j\le i}\binom ij\|\Delta^jS_ru\|\\
&\le Cr^{-2i}\|u\| .
\end{aligned}
\]
For odd \(k=2i-1\), Lemma 1.1(4) interpolates between \(2i-2\) and \(2i\).

(4) By dominated convergence in the expansion, since \(\|(S_r-1)\alpha\|_{H^{2k}}\) is at most \(C\|(S_r-1)(1+\Delta)^k\alpha\|\).

(5) \(\Delta^ke^{-\varepsilon\Delta}u\in L^2\) for all \(k\), so \(e^{-\varepsilon\Delta}u\) lies in every \(H^{2k}\), and is smooth by (I1). Convergence is dominated convergence. The last identity holds because \(e^{-\varepsilon\Delta}\) is self-adjoint and commutes with \(d\) on smooth forms. \(\blacksquare\)

The currents \(P\), \(Q\), \(T\) lie in \(H^{-3}\subseteq H^{-4}\), so \(S_rP\), \(S_rQ\), \(S_rT\) are square integrable forms. The same holds for every *subcurrent*
\[
P'(\alpha)=\int_{\mathscr C}\alpha_y(m)\,d\lambda'(y,m),
\]
where \(\lambda'\le\lambda\) is a Borel measure on \(\mathscr C\); its projection \(\mu'\) satisfies \(\mu'\le\mu\), and \(|P'(\alpha)|\le\|\alpha\|_\infty\).

## 2. The zero pairing

**Lemma 2.1** ([OpenAI-TC, Lemma 4.1]). If \(T'\) is a closed current in \(H^{-4}\), then
\[
\langle S_rT,\,*S_rT'\rangle=0 .
\]

*Proof.* \(S_rT\) annihilates every smooth closed two-form \(\alpha\): \(S_r\alpha\) is smooth and closed by Lemma 1.2(1), and \((S_rT)(\alpha)=T(S_r\alpha)=0\). Let \(w=S_rT'\in L^2\). For a smooth one-form \(\gamma\), \(\langle w,d\gamma\rangle=T'(S_rd\gamma)=T'(dS_r\gamma)=0\). By Lemma 1.2(5), \(w_\varepsilon=e^{-\varepsilon\Delta}w\) is smooth with \(\langle w_\varepsilon,d\gamma\rangle=0\) for all \(\gamma\), so \(d^*w_\varepsilon=0\). In dimension four \(*d^*=d*\) on two-forms, so \(*w_\varepsilon\) is a smooth closed form. Hence \(\langle S_rT,*w_\varepsilon\rangle=0\), and \(*w_\varepsilon\to*w\) in \(L^2\). \(\blacksquare\)

## 3. A heat kernel hypothesis and the kernel of the squared resolvent power

We use one fact about the heat kernel that the programme does not prove. Let \(\chi_1\) be a fixed smooth function on \([0,\infty)\), equal to one on \([0,\rho_0]\) and zero on \([2\rho_0,\infty)\).

**Hypothesis (HK).** For \(t>0\) the operator \(e^{-t\Delta}\) on two-forms has a kernel \(k_t(x,y)\colon\Lambda^2_y\to\Lambda^2_x\), continuous in \((t,x,y)\). There are \(t_0>0\), \(c_0>0\), \(C\), and a smooth positive function \(a\) on \(\{d(x,y)<2\rho_0\}\), such that, with \(\tau_{yx}\colon\Lambda^2_y\to\Lambda^2_x\) the parallel transport of the Levi-Civita connection along the shortest geodesic, for \(0<t<t_0\) and every integer \(M\ge0\),
\[
\begin{aligned}
&\Bigl|k_t(x,y)-\chi_1(d)\frac{e^{-d^2/(4t)}}{(4\pi t)^2}a(x,y)\tau_{yx}\Bigr|\\
&\qquad\le Ct^{-1}e^{-c_0d^2/t}+C_Mt^M ,
\end{aligned}
\]
where \(d=d(x,y)\); and \(|k_t(x,y)|\le C\) for \(t\ge t_0\).

This is the leading term of the short-time expansion of the heat kernel of a Laplace-type operator, with the strong remainder estimate of Ludewig [Ludewig 2019, Theorem 1.1] near the diagonal and his Gaussian upper bound [Ludewig 2019, Theorem 3.5] away from it; the leading coefficient is parallel transport times \(J(x,y)^{-1/2}\), with \(J\) the Jacobian of the exponential map [Ludewig 2018, Section 3, (3.4)]. Ludewig's transport is that of the connection for which the operator is the connection Laplacian plus an endomorphism; for the Hodge Laplacian this is the Levi-Civita connection, by the Weitzenböck formula. Neither the expansion nor the Weitzenböck formula is proved in the programme, so (HK) is a named hypothesis of this course. The rest of the argument is proved here.

**Lemma 3.1** (the kernel of \(S_r^2\); [OpenAI-TC, Lemma 4.2]). Assume (HK). There is \(r_0\in(0,1]\) such that for \(0<r\le r_0\) the operator \(S_r^2\) has a continuous kernel
\[
K_r(x,y)=p_r(x,y)\tau_{yx}+E_r(x,y) ,
\]
where \(p_r\ge0\) vanishes where \(d(x,y)\ge2\rho_0\) (and \(p_r\tau_{yx}\) is read as zero there), and for every integer \(N\ge0\), with \(d=d(x,y)\),
\[
\begin{gathered}
p_r\le C_Nr^{-4}(1+d/r)^{-N},\\
p_r\ge cr^{-4}\quad\text{where }d<r,\\
|E_r|\le C_Nr^{-2}(1+d/r)^{-N} .
\end{gathered}
\]

*Proof.* For \(\lambda\ge0\), \(\int_0^\infty s^5e^{-s(1+r^2\lambda)}\,ds=\Gamma(6)(1+r^2\lambda)^{-6}\). Since \(\|e^{-t\Delta}\|\le1\), this gives
\[
S_r^2=\frac1{\Gamma(6)}\int_0^\infty e^{-s}s^5e^{-r^2s\Delta}\,ds
\]
as a norm-convergent integral of operators. The bounds of (HK) make \(\int_0^\infty e^{-s}s^5k_{r^2s}(x,y)\,ds\) absolutely and locally uniformly convergent, and testing against smooth forms with Fubini's theorem shows that it is \(\Gamma(6)K_r\).

Let \(r_0^2\le t_0/2\) and \(r_0\le\rho_0\). Define \(p_r\) as \(\Gamma(6)^{-1}\) times the integral of the leading term over \(r^2s<t_0\):
\[
\begin{aligned}
p_r&=\frac{\chi_1(d)a}{\Gamma(6)(4\pi r^2)^2}\\
&\quad\times\int_0^{t_0/r^2}e^{-s}s^3e^{-d^2/(4r^2s)}\,ds .
\end{aligned}
\]
It is nonnegative. For every \(N\), \(e^{-d^2/(4r^2s)}\le C_N(1+\sqrt s)^N(1+d/r)^{-N}\). Indeed, if \(d/r\le\sqrt s\) the right side is at least \(C_N\ge1\); otherwise, with \(w=d/(r\sqrt s)>1\), \((1+d/r)\le(1+\sqrt s)(1+w)\) and \(e^{-w^2/4}\le C_N(1+w)^{-N}\). Since \(\int_0^\infty s^3(1+\sqrt s)^Ne^{-s}\,ds<\infty\), the upper bound for \(p_r\) follows. If \(d<r\), the part \(1\le s\le2\) of the integral (inside the range, as \(2r^2\le t_0\)) has \(e^{-d^2/(4r^2s)}\ge e^{-1/4}\) and \(\chi_1(d)=1\), and \(a\) is bounded below; this gives \(p_r\ge cr^{-4}\).

The rest of \(K_r\) is \(E_r\). For \(r^2s<t_0\), the remainder in (HK) contributes \(\Gamma(6)^{-1}\) times the integral of \(e^{-s}s^5\) against \(C(r^2s)^{-1}e^{-c_0d^2/(r^2s)}+C_M(r^2s)^M\). The first term is at most \(C_Nr^{-2}(1+d/r)^{-N}\) by the same inequality, with \(c_0\) in place of \(\frac14\). The second is \(O(r^{2M})\); as \(d\) is at most the diameter \(D\) of \(X\), \(r^{2M}\le C r^{-2}(1+d/r)^{-N}\) once \(2M\ge N-2\). For \(s\ge t_0/r^2\), the kernel is bounded and \(\int_{t_0/r^2}^\infty e^{-s}s^5\,ds\le Ce^{-t_0/(2r^2)}\), again \(O(r^{-2}(1+d/r)^{-N})\). \(\blacksquare\)

## 4. The angular identity and the positive pairing

**Lemma 4.1** (the angular identity; [OpenAI-TC, (4.5)]). Let \(d(x,y)<2\rho_0\), \(\ell\in\mathscr C_x\) and \(m\in\mathscr C_y\). Then
\[
\begin{aligned}
&\langle\ell,*\tau_{yx}m\rangle\\
&\quad=\tfrac12\langle F_x,\tau_{yx}F_y\rangle-\langle\ell,\tau_{yx}m\rangle\\
&\quad=\tfrac12|\ell-\tau_{yx}m|^2-\tfrac14|F_x-\tau_{yx}F_y|^2 ,
\end{aligned}
\]
and \(|F_x-\tau_{yx}F_y|\le C\,d(x,y)\).

*Proof.* Levi-Civita parallel transport is an orientation-preserving isometry, so on two-forms it is an isometry commuting with \(*\). By Lemma 1.1(3) of the first lesson, \(*\ell=F_x-\ell\), and \(m^+=F_y/2\), so \(\tau_{yx}m^+=\frac12\tau_{yx}F_y\) is self-dual while \(\tau_{yx}m^-\) is anti-self-dual. Hence
\[
\begin{aligned}
&\langle\ell,*\tau_{yx}m\rangle=\langle F_x-\ell,\tau_{yx}m\rangle\\
&\quad=\tfrac12\langle F_x,\tau_{yx}F_y\rangle-\langle\ell,\tau_{yx}m\rangle .
\end{aligned}
\]
The second form follows from \(|\ell|=|m|=1\) and \(|F|^2=2\). The map \((x,y)\mapsto\tau_{yx}F_y-F_x\) is smooth on \(\{d<2\rho_0\}\), by smooth dependence of geodesics and of parallel transport on parameters ([Connections and parallel transport](course:DG-FND/connections-and-parallel-transport); Theorem B.5 of [Riemannian connections and convex neighbourhoods](course:DG-FND/riemannian-connections-and-convex-neighbourhoods)), and vanishes on the diagonal. \(\blacksquare\)

The identity is the heart of the method. Pairing \(P\) with the Hodge star of its own regularization does not measure mass; it measures how far apart nearby complex lines are, up to the drift of \(F\) under transport, which is of second order in the distance.

**Lemma 4.2** (the positive pairing; [OpenAI-TC, Lemma 4.4]). Assume (HK) and \(0<r\le r_0\). Let \(P'\) be a subcurrent with measure \(\lambda'\le\lambda\) and projection \(\mu'\). (1) For every \(y\in X\), \(r^{-2}\int_X(1+d(x,y)/r)^{-6}\,d\mu(x)\le C\). (2) \(\|S_rP'\|\le Cr^{-1}\). (3) With \(d=d(x,y)\), and with \((x,\ell)\) distributed by \(\lambda\) and \((y,m)\) by \(\lambda'\),
\[
\begin{aligned}
&\langle S_rP,*S_rP'\rangle\\
&\quad\ge cr^{-4}\iint_{d<r}|\ell-\tau_{yx}m|^2\,d\lambda\,d\lambda'\\
&\qquad-Cr^{-2}\iint(1+d/r)^{-6}\,d\mu\,d\mu' .
\end{aligned}
\]

*Proof.* (1) is the dyadic bound after Proposition 4.1 of [Quadratic mass growth](quadratic-mass-growth.md).

For the pairings, \(S_r^2\) maps \(H^{-4}\) into \(H^8\), which consists of continuous forms, and testing against smooth forms shows \((S_r^2P')(x)=\int K_r(x,y)m\,d\lambda'(y,m)\), using \(K_r(x,y)^*=K_r(y,x)\). Hence, since \(S_r\) is self-adjoint and commutes with \(*\),
\[
\begin{aligned}
&\langle S_rP,*S_rP'\rangle=P(*S_r^2P')\\
&\quad=\iint\langle\ell,*K_r(x,y)m\rangle\,d\lambda\,d\lambda' .
\end{aligned}
\]
Insert \(K_r=p_r\tau_{yx}+E_r\) and Lemma 4.1. The term \(\frac12p_r|\ell-\tau_{yx}m|^2\) is nonnegative; keep it only where \(d<r\), where \(p_r\ge cr^{-4}\). The term \(-\frac14p_r|F_x-\tau_{yx}F_y|^2\) is at least \(-C_Nr^{-4}(1+d/r)^{-N}d^2\), which for \(N=8\) is at least \(-Cr^{-2}(1+d/r)^{-6}\). The error \(\langle\ell,*E_rm\rangle\) is at least \(-|E_r|\ge-Cr^{-2}(1+d/r)^{-6}\). Integrating over the fibers, whose measures project to \(\mu\) and \(\mu'\), gives (3).

For (2), with \((x,m')\) and \((y,m)\) distributed by \(\lambda'\),
\[
\begin{aligned}
\|S_rP'\|^2&=P'(S_r^2P')\\
&=\iint\langle m',K_r(x,y)m\rangle\,d\lambda'\,d\lambda' ,
\end{aligned}
\]
and \(|K_r|\le Cr^{-4}(1+d/r)^{-6}\). With \(g_r(y)=r^{-2}\int(1+d(x,y)/r)^{-6}d\mu'(x)\), which is at most \(C\) by (1) and \(\mu'\le\mu\),
\[
\|S_rP'\|^2\le Cr^{-2}\int g_r\,d\mu'\le Cr^{-2} .
\] \(\blacksquare\)

## 5. Mixing of invariant and anti-invariant parts

**Lemma 5.1** (relative projection estimate; [OpenAI-TC, Lemma 4.5]). Let \(\Pi\) be a smooth field of orthogonal projections on \(\Lambda^2T^*X\). If \(W\in H^{-4}\) satisfies \(\Pi W=0\), then
\[
\|\Pi S_rW\|\le Cr\,\|S_rW\| ,
\]
with \(C\) depending on \(\Pi\) but not on \(r\) or \(W\).

*Proof.* Let \(U=S_rW\in H^2\). By Lemma 1.2(2), \(A_rU=W\) and \(\Pi U=S_rA_r\Pi U\). Since \(\Pi W=0\),
\[
A_r\Pi U=\Pi A_rU+[A_r,\Pi]U=[A_r,\Pi]U ,
\]
so \(\Pi U=S_r[A_r,\Pi]U\). Expanding, \([A_r,\Pi]=\sum_{j=1}^3\binom3jr^{2j}[\Delta^j,\Pi]\). The principal symbol of \(\Delta^j\) is the scalar \(|\xi|^{2j}\), so \([\Delta^j,\Pi]\) is a differential operator of order at most \(2j-1\), bounded \(H^{2j-1}\to L^2\). By Lemma 1.2(3), for the operator norm on \(L^2\),
\[
\|r^{2j}[\Delta^j,\Pi]S_r\|\le Cr^{2j}r^{-(2j-1)}=Cr .
\]
For smooth \(u\) and \(v\), \(\langle S_r[A_r,\Pi]u,v\rangle=-\langle u,[A_r,\Pi]S_rv\rangle\), because \(A_r\), \(\Pi\) and \(S_r\) are formally self-adjoint. So \(S_r[A_r,\Pi]\) extends from smooth forms to a bounded operator on \(L^2\) of norm at most \(Cr\), and the extension agrees with its action on \(U\), as both are continuous from \(L^2\) to \(H^{-6}\). Hence \(\|\Pi U\|\le Cr\|U\|\). \(\blacksquare\)

Thus regularization at scale \(r\) can create only an \(O(r)\) fraction of a component that the current did not have. For \(\Pi=R\) and \(W=P'\) (note \(RP'=0\), since every \(m\in\mathscr C\) is invariant), and for \(\Pi=1-R\) and an anti-invariant \(W\), this controls the cross terms between \(P\) and \(Q\).

## 6. The correction is square integrable

**Proposition 6.1** ([OpenAI-TC, Proposition 4.6]). Assume (HK). Then \(Q\in L^2\), and
\[
\mathcal I_r\le Cr^4
\]
for \(0<r\le r_0\). For every subcurrent \(P'\),
\[
\lim_{r\to0}\langle S_rP',\,*S_rQ\rangle=0 .
\]

*Proof.* *Cross terms.* Let \(V\in H^{-4}\) be anti-invariant, that is \((1-R)V=0\). Since \(R\) is a pointwise orthogonal projection and \(RP'=0\),
\[
\begin{aligned}
\langle S_rP',S_rV\rangle&=\langle RS_rP',S_rV\rangle\\
&\quad+\langle S_rP',(1-R)S_rV\rangle .
\end{aligned}
\]
Lemma 5.1, applied twice, and Lemma 4.2(2) give
\[
\begin{aligned}
|\langle S_rP',S_rV\rangle|&\le Cr\|S_rP'\|\,\|S_rV\|\\
&\le C\|S_rV\| .
\end{aligned}
\]

*Energy.* \(Q\) is self-dual, so \(*S_rQ=S_rQ\), and Lemma 2.1 with \(T'=T\) gives
\[
\begin{aligned}
0&=\langle S_rP,*S_rP\rangle\\
&\quad+2\langle S_rP,S_rQ\rangle+\|S_rQ\|^2 .
\end{aligned}
\]
By Lemma 4.2(3) and (1), the first term is at least \(cr^{-4}\mathcal I_r-C\); by the cross-term bound the second is at least \(-C\|S_rQ\|\). Hence
\[
cr^{-4}\mathcal I_r+\|S_rQ\|^2\le C+C\|S_rQ\| .
\]
So \(\|S_rQ\|\) is bounded as \(r\to0\), and \(\mathcal I_r\le Cr^4\). A sequence \(r_k\to0\) has \(S_{r_k}Q\) converging weakly in \(L^2\) to some \(q\): bounded sequences in a Hilbert space have weakly convergent subsequences (Exercise 4 of [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian), with its solution; Hilbert spaces are reflexive by Theorem 2.3 of the lesson on Hilbert spaces cited above). For smooth \(\alpha\), \(\langle S_rQ,\alpha\rangle=Q(S_r\alpha)\to Q(\alpha)\) by Lemma 1.2(4), so \(Q(\alpha)=\langle q,\alpha\rangle\): \(Q=q\in L^2\).

*Vanishing cross terms.* For anti-invariant \(V\in L^2\) the cross-term bound and \(\|S_r\|\le1\) give \(|\langle S_rP',S_rV\rangle|\le C\|V\|\), uniformly in \(r\). If \(V\) is smooth and anti-invariant, then \(\langle S_rP',S_rV\rangle=P'(S_r^2V)\to P'(V)\) by Lemma 1.2(4), and \(P'(V)=\int\langle V_y,m\rangle\,d\lambda'=0\) since \(V\) is anti-invariant and \(m\) invariant. Smooth anti-invariant forms are dense among square integrable anti-invariant forms (approximate by smooth forms, then apply \(R\)). Approximating \(Q\) in \(L^2\) by such \(V\) gives \(\langle S_rP',S_rQ\rangle\to0\), and \(*S_rQ=S_rQ\). \(\blacksquare\)

Two consequences are used in the last lesson: \(S_rQ\to Q\) in \(L^2\) (Lemma 1.2(4)), and the pairing of \(P\) with a subcurrent \(P'\) has the lower bound of Lemma 4.2(3), whose negative term will be shown to vanish when \(\mu'\) lives on points of zero density.

## 7. Exercises

**7.1.** Show that \(\sup_{\lambda\ge0}\lambda^j(1+r^2\lambda)^{-3}\) equals \(\bigl(\frac{j}{3-j}\bigr)^j\frac{(3-j)^3}{27}\,r^{-2j}\) for \(j=1,2\), and that it is at most \(r^{-2j}\) for \(0\le j\le3\).

**7.2.** Let \(\ell\) and \(m\) be unit complex-line bivectors at the same point with \(F\) the same. Show that \(\langle\ell,*m\rangle=\frac12|\ell-m|^2\ge0\), with equality only for \(\ell=m\).

**7.3.** On \(\mathbb R^4\) with the Euclidean metric, the heat kernel on functions is \((4\pi t)^{-2}e^{-|x-y|^2/(4t)}\). Show that the kernel of \((1-r^2\Delta_0)^{-6}\), with \(\Delta_0=\sum_i\partial_i^2\), is \(r^{-4}\Phi(|x-y|/r)\) for a positive function \(\Phi\), and give \(\Phi\) as an integral.

**7.4.** On the flat torus \(\mathbb R^4/\mathbb Z^4\), write two-forms in the constant frame \(dx^i\wedge dx^j\), and let \(\Pi\) be a constant orthogonal projection in this frame. Show that \(\Pi S_r=S_r\Pi\), so that Lemma 5.1 holds with \(C=0\).

**7.5.** Show that \(\langle\alpha,*\beta\rangle=\int_X\alpha\wedge\beta\) for square integrable two-forms. On the flat torus \(\mathbb R^4/\mathbb Z^4\), let \(T\) and \(T'\) be the currents given by the constant forms \(dx^1\wedge dx^2\) and \(dx^3\wedge dx^4\). Show that both are closed and that \(\langle S_rT,*S_rT'\rangle=1\). Which hypothesis of Lemma 2.1 fails?

## 8. Solutions

**7.1.** For \(f(\lambda)=\lambda^j(1+r^2\lambda)^{-3}\), \(f'=0\) when \(j(1+r^2\lambda)=3r^2\lambda\), that is \(r^2\lambda=j/(3-j)\). Then \(1+r^2\lambda=3/(3-j)\), and \(f=r^{-2j}(j/(3-j))^j((3-j)/3)^3\). For \(j=1\) this is \(\frac4{27}r^{-2}\), for \(j=2\) it is \(\frac4{27}r^{-4}\). For \(j=3\), \(\lambda^3(1+r^2\lambda)^{-3}<r^{-6}\), and for \(j=0\) the supremum is \(1\).

**7.2.** With \(x=y\) and \(\tau\) the identity, Lemma 4.1 gives \(\langle\ell,*m\rangle=\frac12|\ell-m|^2-\frac14|F-F|^2\).

**7.3.** The integral formula of the proof of Lemma 3.1, with \(e^{t\Delta_0}\) in place of \(e^{-t\Delta}\), gives the kernel
\[
\frac1{\Gamma(6)}\int_0^\infty e^{-s}s^5\frac{e^{-|x-y|^2/(4r^2s)}}{(4\pi r^2s)^2}\,ds ,
\]
which is \(r^{-4}\Phi(|x-y|/r)\) with \(\Phi(\rho)=\frac{1}{16\pi^2\Gamma(6)}\int_0^\infty e^{-s}s^3e^{-\rho^2/(4s)}\,ds>0\).

**7.4.** On the flat torus, \(\Delta\) acts componentwise as \(-\sum_i\partial_i^2\) in the constant frame, and a constant \(\Pi\) commutes with it, hence with \(S_r\). Then \(\Pi W=0\) gives \(\Pi S_rW=S_r\Pi W=0\).

**7.5.** Since \(\alpha\wedge*\gamma=\langle\alpha,\gamma\rangle\,dV\) and \(**=1\) on two-forms, \(\langle\alpha,*\beta\rangle=\int\alpha\wedge**\beta=\int\alpha\wedge\beta\). Constant forms on the flat torus satisfy \(d^*=0\), so \(T(d\gamma)=\langle d^*dx^{12},\gamma\rangle=0\): both currents are closed. Constant forms are harmonic, so \(S_r\) fixes them, and \(\langle S_rT,*S_rT'\rangle=\int dx^1\wedge dx^2\wedge dx^3\wedge dx^4\), which is \(1\). Lemma 2.1 needs \(T\) to annihilate every closed form, and \(T(dx^1\wedge dx^2)=1\). In this language the lemma says that the intersection pairing \(\int S_rT\wedge S_rT'\) vanishes when \(T\) annihilates all closed forms.

## References

- [OpenAI-TC] OpenAI, *Taming implies compatibility on four-manifolds*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026
- [Ludewig 2019] M. Ludewig, *Strong short-time asymptotics and convolution approximation of the heat kernel*, Ann. Global Anal. Geom. 55 (2019); Theorems 1.1 and 3.5. https://arxiv.org/abs/1607.05152
- [Ludewig 2018] M. Ludewig, *Heat kernel asymptotics, path integrals and infinite-dimensional determinants*, J. Geom. Phys. 131 (2018); Section 3, (3.4). https://arxiv.org/abs/1607.05891
