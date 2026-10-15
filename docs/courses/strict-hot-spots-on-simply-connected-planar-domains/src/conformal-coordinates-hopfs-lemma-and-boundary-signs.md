# Conformal coordinates, Hopf's lemma and boundary signs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the hot-spots theorem works on the unit disc \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) with boundary circle \(\mathbb S^1\). This lesson constructs a conformal map from \(\mathbb D\) onto \(\Omega\) that is smooth up to the boundary, using Hopf's boundary point lemma and the argument principle. It then transfers the mean-zero condition of Neumann eigenfunctions to a weighted condition on the circle, shows that their sign sets are connected, and deduces that the first positive Neumann eigenvalue has multiplicity at most two.

- Interior discs and Hopf's lemma (Section 1).
- A conformal map that is smooth up to the boundary (Section 2).
- A positive boundary weight (Section 3).
- Two paths with alternating endpoints meet (Section 4).
- Sign sets and the multiplicity bound (Section 5).

Notation is that of [Neumann eigenfunctions and the hot-spots problem](neumann-eigenfunctions-and-the-hot-spots-problem.md): \(\Omega\) is a nonempty bounded simply connected open set with \(C^\infty\) boundary, \(\mu\) and \(V\) are the first positive Neumann eigenvalue and its eigenspace, \(\lambda_D\) is the first Dirichlet eigenvalue, and (SOB), (ER) are the named analytic facts. Proposition 3.1 there gives \(V\subseteq C^\infty(\overline\Omega)\), and Proposition 4.1 there gives \(\mu<\lambda_D\). The circle \(\mathbb S^1\) carries arclength \(ds\), of total mass \(2\pi\), and points \(s=e^{i\theta}\).

## 1. Interior discs and Hopf's lemma

**Lemma 1.1** (interior discs). For every \(x_0\in\partial\Omega\) and every sufficiently small \(\rho>0\), the disc \(B\) of radius \(\rho\) with centre \(x_0-\rho\nu(x_0)\) satisfies \(B\subseteq\Omega\); its outward normal at \(x_0\in\partial B\) is \(\nu(x_0)\).

*Proof.* In a boundary chart centred at \(x_0\) (Section 1 of the first lesson), \(\Omega\) is the region \(x_2>\gamma(x_1)\) in a rectangle \((-a,a)\times(-b,b)\), with \(\gamma(0)=\gamma'(0)=0\), and \(\nu(x_0)=(0,-1)\). Let \(c\ge0\) bound \(|\gamma''|/2\), so \(\gamma(x_1)\le cx_1^2\). Take \(\rho<\min(a,b/2)\) with \(2c\rho<1\). A point of the disc of radius \(\rho\) centred at \((0,\rho)\) satisfies \(|x_1|<\rho\), \(0<x_2<2\rho\) and
\[
\begin{aligned}
x_2&>\rho-\sqrt{\rho^2-x_1^2}\\
&=\frac{x_1^2}{\rho+\sqrt{\rho^2-x_1^2}}\\
&\ge\frac{x_1^2}{2\rho}\ge cx_1^2\ge\gamma(x_1)
\end{aligned}
\]
when \(x_1\ne0\), and \(x_2>0=\gamma(0)\) when \(x_1=0\). \(\square\)

**Lemma 1.2** (Hopf's boundary point lemma). Let \(B\) be an open disc with centre \(y\) and radius \(\rho\), let \(x_0\in\partial B\) and \(n=(x_0-y)/\rho\). Let \(w\in C^2(B)\cap C^1(\overline B)\) satisfy \(\Delta w\ge0\) in \(B\) and \(w(x)<w(x_0)\) for all \(x\in B\). Then \(\partial_nw(x_0)>0\).

*Proof.* Let \(A\) be the annulus \(\rho/2<|x-y|<\rho\), fix \(\alpha>4/\rho^2\), and put \(v(x)=e^{-\alpha|x-y|^2}-e^{-\alpha\rho^2}\). With \(r=|x-y|\), in two dimensions
\[
\begin{aligned}
\Delta v&=e^{-\alpha r^2}(4\alpha^2r^2-4\alpha)\\
&=4\alpha e^{-\alpha r^2}(\alpha r^2-1)>0\quad\text{on }A,
\end{aligned}
\]
since \(\alpha r^2>\alpha\rho^2/4>1\). On the inner circle, \(w-w(x_0)\le-\delta\) for some \(\delta>0\), by compactness. Choose \(\varepsilon>0\) with \(\varepsilon\le\delta\), and put \(z=w-w(x_0)+\varepsilon v\). Then \(\Delta z>0\) in \(A\), so \(z\) has no interior maximum in \(A\) (at an interior maximum the Hessian is negative semidefinite). On the inner circle \(z\le-\delta+\varepsilon\le0\); on the outer circle \(v=0\) and \(w\le w(x_0)\), so \(z\le0\). Hence \(z\le0\) on \(A\), while \(z(x_0)=0\). Approaching \(x_0\) along \(-n\) gives \(\partial_nz(x_0)\ge0\), that is,
\[
\begin{aligned}
\partial_nw(x_0)&\ge-\varepsilon\,\partial_nv(x_0)\\
&=2\varepsilon\alpha\rho e^{-\alpha\rho^2}>0.\qquad\square
\end{aligned}
\]

## 2. A conformal map that is smooth up to the boundary

We write \(z\) for the complex coordinate. For a bounded open set \(U\) with \(C^1\) boundary and a complex function \(F\in C^1(\overline U)\), (SOB 1) applied to the real and imaginary parts of \((F,0)\) and \((0,F)\) gives \(\int_{\partial U}F\nu\,ds=\int_U(\partial_xF+i\partial_yF)\), with \(\nu=\nu_1+i\nu_2\). Since \(\tau=i\nu\),
\[
\begin{gathered}
\int_{\partial U}F\,\tau\,ds=2i\int_U\partial_{\bar z}F,\\
\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y).
\end{gathered} \tag{2.1}
\]
In particular \(\int_{\partial U}F\tau\,ds=0\) if \(F\) is holomorphic in \(U\).

**Proposition 2.1** ([OpenAI-HS, Lemma 2.2]). There is a holomorphic bijection \(\Phi\colon\mathbb D\to\Omega\) that extends to a homeomorphism \(\overline{\mathbb D}\to\overline\Omega\), with \(\Phi\in C^\infty(\overline{\mathbb D})\), \(\Phi^{-1}\in C^\infty(\overline\Omega)\), and \(\Phi'\ne0\) on \(\overline{\mathbb D}\).

*Proof.* *Step 1: a harmonic function with logarithmic boundary values.* Fix \(a\in\Omega\) and a smooth \(\chi\) on \(\mathbb R^2\) that vanishes near \(a\) and equals \(1\) near \(\partial\Omega\). Then \(E=\chi\log|z-a|\) is smooth on \(\mathbb R^2\). By (B10) and (B29) of [Boundary energy, local inverses, and harmonic data](course:elliptic-operators-and-boundary-problems/second-order-boundary), there is \(w\in H^1_0(\Omega)\cap C^\infty(\overline\Omega)\) with \(-\Delta w=\Delta E\). The function \(l=E+w\in C^\infty(\overline\Omega)\) is harmonic in \(\Omega\), and \(l=\log|z-a|\) on \(\partial\Omega\), because \(w\) is continuous with zero trace.

*Step 2: a harmonic conjugate.* The function \(F=l_x-il_y\) is holomorphic in \(\Omega\) by the Cauchy–Riemann equations, which hold because \(l\) is harmonic. By Lemma A.2 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01), \(F\) has a primitive \(G\) in the simply connected domain \(\Omega\). Since \(\partial_x\operatorname{Re}G=\operatorname{Re}G'=l_x\) and \(\partial_y\operatorname{Re}G=-\operatorname{Im}G'=l_y\), adding a real constant to \(G\) gives \(G=l+i\tilde l\). All derivatives of \(\tilde l\) of positive order extend continuously to \(\overline\Omega\), because \(\nabla\tilde l=(-l_y,l_x)\). The function \(\tilde l\) itself extends continuously: in a boundary chart, two points \(p,q\) of \(\Omega\) near the boundary point can be joined inside \(\Omega\) by moving up a distance \(L|p-q|\), across, and down, where \(L=1+\sup|\gamma'|\); this path has length at most \((2L+1)|p-q|\), so \(\tilde l\) is Lipschitz there. Hence \(\tilde l\in C^\infty(\overline\Omega)\).

*Step 3: the candidate inverse.* Put \(m(z)=(z-a)e^{-G(z)}\). It is holomorphic in \(\Omega\), lies in \(C^\infty(\overline\Omega)\), and has exactly one zero, at \(a\), which is simple. The function \(\log|m|=\log|z-a|-l\) is harmonic in \(\Omega\setminus\{a\}\), continuous on \(\overline\Omega\setminus\{a\}\), zero on \(\partial\Omega\), and tends to \(-\infty\) at \(a\). We show \(|m|<1\) in \(\Omega\). Choose \(r>0\) with \(\overline{B(a,r)}\subseteq\Omega\) and \(\log|m|<-1\) on \(\overline{B(a,r)}\setminus\{a\}\), and let \(\Omega_r=\Omega\setminus\overline{B(a,r)}\). The maximum \(M\) of \(\log|m|\) over the compact set \(\overline{\Omega_r}\) is at least \(0\). If it is attained at a point of \(\Omega_r\), the harmonic maximum principle (Lemma A.3 of [Dirichlet series and Euler products](course:NT-ZETA/NT-ZETA-01)) makes \(\log|m|\) equal to \(M\) on the component \(C\) of \(\Omega_r\) containing that point. By continuity \(\log|m|=M\ge0\) on \(\partial C\), which is nonempty and contained in \(\partial\Omega\cup\partial B(a,r)\); since \(\log|m|<-1\) on \(\partial B(a,r)\), \(\partial C\subseteq\partial\Omega\). Then \(C\) is open and closed in \(\Omega\), so \(C=\Omega\), which is impossible because \(a\notin C\). Hence \(M\) is attained only on \(\partial\Omega_r\), and therefore only on \(\partial\Omega\), where \(\log|m|=0\). So \(M=0\), \(\log|m|<0\) on \(\Omega_r\), and \(|m|<1\) in \(\Omega\).

*Step 4: \(m'\ne0\) on \(\partial\Omega\).* Let \(x_0\in\partial\Omega\), and let \(B\) be an interior disc at \(x_0\) from Lemma 1.1, so small that \(a\notin\overline B\). The function \(\log|m|\) is \(C^1\) on \(\overline B\), harmonic in \(B\), negative in \(B\) and zero at \(x_0\). By Lemma 1.2, its normal derivative at \(x_0\) is positive. Near any point where \(m\ne0\), \(\log|m|\) is the real part of a local holomorphic logarithm of \(m\), so \(|\nabla\log|m||=|m'/m|\); by continuity this holds at \(x_0\), and \(m'(x_0)\ne0\).

*Step 5: \(m\) maps \(\Omega\) bijectively onto \(\mathbb D\).* Let \(w_0\in\mathbb D\). The zeros of \(m-w_0\) lie in the compact set \(\{|m|\le|w_0|\}\subseteq\Omega\); they are isolated (Lemma A.3 there), hence finitely many, say \(z_j\) with orders \(k_j\). Remove small closed discs \(\overline{B(z_j,\varepsilon)}\) from \(\Omega\) and apply (2.1) to \(F=m'/(m-w_0)\), which is \(C^1\) up to the boundary of the remaining set and holomorphic inside. On the circle around \(z_j\), oriented clockwise as part of that boundary, write \(m-w_0=(z-z_j)^{k_j}h\) with \(h\) zero-free near \(z_j\); then \(F=k_j/(z-z_j)+h'/h\), and the circle integral is \(-2\pi ik_j\), because \(h'/h\) has zero integral around the circle (Lemma A.2 there). Hence
\[
\begin{aligned}
N(w_0)&:=\sum_jk_j\\
&=\frac1{2\pi i}\int_{\partial\Omega}\frac{m'}{m-w_0}\,\tau\,ds .
\end{aligned}
\]
On \(\partial\Omega\), \(|m-w_0|\ge1-|w_0|>0\), so the right side is continuous in \(w_0\in\mathbb D\). Being integer-valued on the connected set \(\mathbb D\), it is constant, equal to \(N(0)=1\). So every \(w_0\in\mathbb D\) has exactly one preimage in \(\Omega\), of multiplicity one; in particular \(m'\ne0\) in \(\Omega\), and \(m\colon\Omega\to\mathbb D\) is a bijection.

*Step 6: the boundary.* Every \(\zeta\in\mathbb S^1\) is a limit of \(m(z_n)\) with \(z_n\in\Omega\); a limit point \(z\) of \((z_n)\) satisfies \(m(z)=\zeta\), so \(z\in\partial\Omega\). Hence \(m(\partial\Omega)=\mathbb S^1\). Near \(x_0\in\partial\Omega\), flatten the boundary in a boundary chart by \((x_1,x_2)\mapsto(y_1,y_2)=(x_1,x_2-\gamma(x_1))\), write \(f\) for \(m\) in the coordinates \(y\), and put \(\hat f(y_1,y_2)=3f(y_1,-y_2)-2f(y_1,-2y_2)\) for \(y_2<0\). Values and first derivatives match at \(y_2=0\), so this gives a \(C^1\) map \(\hat m\) on a neighbourhood \(N\) of \(x_0\) that equals \(m\) on \(N\cap\overline\Omega\). Its Jacobian at \(x_0\) is \(|m'(x_0)|^2\ne0\). Suppose \(m(x_1)=m(x_2)=\zeta\) with \(x_1\ne x_2\) on \(\partial\Omega\). By the inverse function theorem there are disjoint neighbourhoods \(N_1,N_2\) of \(x_1,x_2\) and a disc \(U\) around \(\zeta\) such that \(\hat m\) maps each \(N_i\) homeomorphically onto \(U\). The preimage in \(N_i\) of the connected set \(U\cap\mathbb D\) is connected and contained in \(N_i\setminus\partial\Omega=(N_i\cap\Omega)\cup(N_i\setminus\overline\Omega)\), since \(\hat m\) maps \(\partial\Omega\) into \(\mathbb S^1\); it meets \(N_i\cap\Omega\), whose image contains points of \(\mathbb D\) near \(\zeta\). So it lies in \(\Omega\), and points of \(U\cap\mathbb D\) have two preimages in \(\Omega\), contradicting Step 5. Hence \(m\colon\overline\Omega\to\overline{\mathbb D}\) is a continuous bijection of compact spaces, and its inverse \(\Phi\) is continuous.

*Step 7: smoothness of the inverse.* At \(\zeta=m(x_0)\in\mathbb S^1\), the local \(C^1\) inverse of \(\hat m\) agrees with \(\Phi\) on \(\overline{\mathbb D}\) near \(\zeta\), by continuity of \(\Phi\) and injectivity of \(m\). So \(\Phi\) is \(C^1\) up to the boundary, holomorphic in \(\mathbb D\), and \(\Phi'=1/(m'\circ\Phi)\) is continuous and nonzero on \(\overline{\mathbb D}\). If all derivatives of \(\Phi\) of order at most \(k\) extend continuously to \(\overline{\mathbb D}\), the chain rule shows the same for \(m'\circ\Phi\), hence for \(\Phi'=1/(m'\circ\Phi)\), and so for the derivatives of \(\Phi\) of order \(k+1\). Thus \(\Phi\in C^\infty(\overline{\mathbb D})\), and \(\Phi^{-1}=m\in C^\infty(\overline\Omega)\). \(\square\)

From now on \(\Phi\) is fixed. It maps \(\mathbb S^1\) onto \(\partial\Omega\), and the arclength of \(\partial\Omega\) at \(\Phi(s)\) is \(|\Phi'(s)|\,ds\). For \(v\in V\) put \(h_v=v\circ\Phi\) on \(\mathbb S^1\).

## 3. A positive boundary weight

**Lemma 3.1** ([OpenAI-HS, Lemma 2.3]). There is \(\beta\in C^\infty(\mathbb S^1)\) with \(\beta>0\) such that
\[
\int_{\mathbb S^1}\beta h_v\,ds=0\quad(v\in V). \tag{3.1}
\]
If \(v\ne0\), then \(h_v\ne0\), and \(h_v\) takes both signs.

*Proof.* By Proposition 4.1 of the first lesson and Lemma 2.3 there, \(\langle\phi,\psi\rangle_\mu=\int\nabla\phi\cdot\nabla\psi-\mu\int\phi\psi\) is an inner product on \(H^1_0(\Omega)\) equivalent to the \(H^1\) inner product: \(\langle\phi,\phi\rangle_\mu\ge(1-\mu/\lambda_D)\|\nabla\phi\|^2\). The Riesz–Fréchet theorem gives \(L\in H^1_0(\Omega)\) with \(\langle L,\phi\rangle_\mu=\int\phi\) for all \(\phi\in H^1_0(\Omega)\). Thus \(\int\nabla L\cdot\nabla\phi=\int(1+\mu L)\phi\), and (ER D) applied repeatedly, with (SOB 4), gives \(L\in C^\infty(\overline\Omega)\), \(-\Delta L-\mu L=1\) in \(\Omega\) and \(L=0\) on \(\partial\Omega\).

*\(L\ge0\).* Let \(L^-=\max(-L,0)\). Approximating \(t\mapsto\max(-t,0)\) by \(\frac12(\sqrt{t^2+\delta^2}-\delta-t)\) as in Lemma 3.2 of the first lesson shows \(L^-\in H^1_0(\Omega)\) with \(\nabla L^-=-\mathbf 1_{\{L<0\}}\nabla L\) almost everywhere (the set where \(L=0\) and \(\nabla L\ne0\) is locally a smooth curve, of measure zero). Testing with \(\phi=L^-\) gives
\[
-\int|\nabla L^-|^2+\mu\int(L^-)^2=\int L^-\ge0 .
\]
If \(L^-\ne0\), this gives \(\int|\nabla L^-|^2\le\mu\int(L^-)^2<\lambda_D\int(L^-)^2\), contradicting the definition of \(\lambda_D\). So \(L\ge0\).

*\(L>0\) in \(\Omega\) and \(-\partial_\nu L>0\) on \(\partial\Omega\).* At an interior zero of \(L\ge0\), \(L\) has a minimum and \(\Delta L\ge0\), whereas \(\Delta L=-1-\mu L=-1\) there. So \(L>0\) in \(\Omega\). At \(x_0\in\partial\Omega\) apply Lemma 1.2 to \(w=-L\) on an interior disc from Lemma 1.1: \(\Delta w=1+\mu L>0\) and \(w<0=w(x_0)\) in the disc. So \(-\partial_\nu L(x_0)>0\).

*The identity.* For \(v\in V\), Green's formula (2.2) of the first lesson applied twice gives
\[
\begin{aligned}
\int_\Omega v&=\int_\Omega v(-\Delta L-\mu L)\\
&=\int_\Omega(-\Delta v-\mu v)L\\
&\quad+\int_{\partial\Omega}(L\,\partial_\nu v-v\,\partial_\nu L)\,ds\\
&=-\int_{\partial\Omega}v\,\partial_\nu L\,ds,
\end{aligned}
\]
since \(\Delta v+\mu v=0\), \(\partial_\nu v=0\) and \(L=0\) on \(\partial\Omega\). As \(\int_\Omega v=0\), the change of variables \(x=\Phi(s)\) gives (3.1) with \(\beta=|\Phi'|\,(-\partial_\nu L)\circ\Phi\), which is smooth and positive.

If \(h_v=0\), then \(v\in C^\infty(\overline\Omega)\) vanishes on \(\partial\Omega\), so \(v\in H^1_0(\Omega)\) and \(\mu\|v\|^2=\|\nabla v\|^2\ge\lambda_D\|v\|^2\), which forces \(v=0\). If \(h_v\ne0\), (3.1) and \(\beta>0\) force both signs. \(\square\)

## 4. Two paths with alternating endpoints meet

**Lemma 4.1** (continuous logarithms). Let \(Q=[0,1]^2\) and let \(F\colon Q\to\mathbb C\setminus\{0\}\) be continuous. There is a continuous \(G\colon Q\to\mathbb C\) with \(e^G=F\).

*Proof.* Let \(m=\min_Q|F|>0\), and choose \(\delta>0\) with \(|F(x)-F(y)|<m\) whenever \(|x-y|\le\delta\). Fix an integer \(N>\sqrt2/\delta\) and a complex number \(g_0\) with \(e^{g_0}=F(0)\). For \(x\in Q\) put \(x_j=(j/N)x\), \(0\le j\le N\). Then \(|F(x_{j+1})/F(x_j)-1|<1\), so the principal logarithm \(\operatorname{Log}\) is defined and continuous at these quotients, and
\[
G(x)=g_0+\sum_{j=0}^{N-1}\operatorname{Log}\frac{F(x_{j+1})}{F(x_j)}
\]
is continuous with \(e^{G(x)}=F(0)\prod_jF(x_{j+1})/F(x_j)=F(x)\). \(\square\)

For \(p\in\mathbb S^1\) let \(H_p=\{w\in\mathbb C:\operatorname{Re}(w\bar p)>0\}\), fix a real \(\varphi_p\) with \(p=e^{i\varphi_p}\), and define the continuous argument \(\theta_p(w)=\varphi_p+\operatorname{Arg}(w/p)\) on \(H_p\), where \(\operatorname{Arg}\) takes values in \((-\pi/2,\pi/2)\) on the right half-plane. For \(z\in\overline{\mathbb D}\setminus\{p\}\), \(\operatorname{Re}((p-z)\bar p)=1-\operatorname{Re}(z\bar p)>0\), so \(p-z\in H_p\). For \(q=e^{i\kappa}\in\mathbb S^1\setminus\{p\}\), with \(\kappa\) chosen in \((\varphi_p-2\pi,\varphi_p)\),
\[
\begin{aligned}
&p-q=2\sin\bigl(\tfrac{\varphi_p-\kappa}2\bigr)\\
&\qquad\cdot e^{i((\varphi_p+\kappa)/2+\pi/2)},\\
&\theta_p(p-q)=\tfrac{\varphi_p+\kappa}2+\tfrac\pi2,
\end{aligned} \tag{4.1}
\]
because the sine is positive and \((\kappa-\varphi_p)/2+\pi/2\in(-\pi/2,\pi/2)\).

**Lemma 4.2** (planar separation). Let \(a,b,c,d\in\mathbb S^1\) be distinct and in this counterclockwise order. Let \(\gamma_1,\gamma_2\colon[0,1]\to\overline{\mathbb D}\) be continuous paths from \(a\) to \(c\) and from \(b\) to \(d\), with \(\gamma_1(s),\gamma_2(s)\in\mathbb D\) for \(0<s<1\). Then \(\gamma_1(s)=\gamma_2(t)\) for some \(s,t\in(0,1)\).

*Proof.* Suppose not. Then \(F(s,t)=\gamma_1(s)-\gamma_2(t)\) never vanishes on \(Q\): interior points of the paths lie in \(\mathbb D\), their endpoints lie on \(\mathbb S^1\), and the four endpoints are distinct. Let \(G\) be as in Lemma 4.1; \(\operatorname{Im}G\) is a continuous argument of \(F\). Along the side \(t=0\), \(F(s,0)=-(b-\gamma_1(s))\) with \(b-\gamma_1(s)\in H_b\), so \(\operatorname{Im}G(s,0)-\pi-\theta_b(b-\gamma_1(s))\) is a continuous function with values in \(2\pi\mathbb Z\), hence constant. The same reasoning on the four sides, traversed counterclockwise around \(Q\), gives
\[
\begin{aligned}
0&=[\theta_b(b-c)-\theta_b(b-a)]\\
&\quad+[\theta_c(c-d)-\theta_c(c-b)]\\
&\quad+[\theta_d(d-a)-\theta_d(d-c)]\\
&\quad+[\theta_a(a-b)-\theta_a(a-d)],
\end{aligned}
\]
using \(F(1,t)=c-\gamma_2(t)\), \(F(s,1)=-(d-\gamma_1(s))\) and \(F(0,t)=a-\gamma_2(t)\). Write \(a,b,c,d=e^{i\alpha},e^{i\beta},e^{i\gamma},e^{i\delta}\) with \(\alpha<\beta<\gamma<\delta<\alpha+2\pi\), and take \(\varphi_a,\varphi_b,\varphi_c,\varphi_d=\alpha,\beta,\gamma,\delta\). By (4.1) the four brackets are
\[
\begin{gathered}
\frac{(\gamma-2\pi)-\alpha}2,\qquad\frac{(\delta-2\pi)-\beta}2,\\
\frac{\alpha-\gamma}2,\qquad\frac{(\beta-2\pi)-(\delta-2\pi)}2,
\end{gathered}
\]
whose sum is \(-2\pi\ne0\). \(\square\)

## 5. Sign sets and the multiplicity bound

**Lemma 5.1** ([OpenAI-HS, Lemma 2.4]). Let \(0\ne v\in V\).

1. The sets \(\{v>0\}\) and \(\{v<0\}\) are nonempty and connected.
2. There are no points \(s_1,s_2,s_3,s_4\in\mathbb S^1\), in this counterclockwise order, with \(h_v(s_1)>0\), \(h_v(s_2)<0\), \(h_v(s_3)>0\), \(h_v(s_4)<0\).

*Proof.* (1) Both sets are nonempty because \(v\) has mean zero. Let \(U\) be a connected component of \(\{v>0\}\). At a point \(z\in\partial U\cap\Omega\), \(v(z)=0\): if \(v(z)>0\), a small disc around \(z\) lies in \(\{v>0\}\) and meets \(U\), so it lies in \(U\); if \(v(z)<0\), a small disc around \(z\) misses \(U\). Choose smooth nondecreasing \(g_\varepsilon\) with \(g_\varepsilon=0\) on \((-\infty,\varepsilon]\) and \(g_\varepsilon=1\) on \([2\varepsilon,\infty)\), let \(G_\varepsilon(t)=\int_0^tg_\varepsilon\), and put \(w_\varepsilon=G_\varepsilon(v)\mathbf 1_U\). Near each point of \(\overline\Omega\), \(w_\varepsilon\) equals \(0\) or \(G_\varepsilon(v)\). This is clear near points of \(U\) and of \(\Omega\setminus\overline U\); near points of \(\partial U\cap\Omega\), and near boundary points where \(v\le0\), it holds because \(v<\varepsilon\) there; near a point of \(\partial\Omega\setminus\overline U\), because \(U\) stays away from it. Finally, if \(x_0\in\partial\Omega\cap\overline U\) and \(v(x_0)>0\), then in a boundary chart at \(x_0\) the set \(\{|x_1|<a',\ \gamma(x_1)<x_2<b'\}\) is connected, and for small \(a',b'\) it lies in \(\{v>0\}\) and meets \(U\), so it lies in \(U\). Hence \(w_\varepsilon\in C^\infty(\overline\Omega)\) with \(\nabla w_\varepsilon=g_\varepsilon(v)\mathbf 1_U\nabla v\). As \(\varepsilon\to0\), \(w_\varepsilon\to v\mathbf 1_U\) uniformly and \(\nabla w_\varepsilon\to\mathbf 1_U\nabla v\) in \(L^2\). So \(v_U=v\mathbf 1_U\in H^1(\Omega)\) with \(\nabla v_U=\mathbf 1_U\nabla v\). The same holds for components of \(\{v<0\}\), applied to \(-v\). Testing (3.1) of the first lesson with \(\phi=v_U\) gives
\[
\begin{aligned}
\int|\nabla v_U|^2&=\int_U|\nabla v|^2\\
&=\mu\int_Uv^2=\mu\int v_U^2 .
\end{aligned}
\]
Suppose the two sign sets together have at least three components, among them \(U_1,U_2,U_3\). Choose \((c_1,c_2)\ne(0,0)\) with \(c_1\int v_{U_1}+c_2\int v_{U_2}=0\), and put \(w=c_1v_{U_1}+c_2v_{U_2}\). Since the supports are disjoint, \(\int|\nabla w|^2=\mu\int w^2\), and \(w\ne0\). By Proposition 3.1(2) of the first lesson \(w\in V\); it vanishes on the open set \(U_3\), so \(w=0\) by Proposition 3.1(4) there, a contradiction. Hence each sign set has exactly one component.

(2) Suppose such points exist, and let \(x_i=\Phi(s_i)\). By Lemma 1.1 and continuity of \(v\) on \(\overline\Omega\), there is a segment from \(x_1\) into \(\Omega\), along \(-\nu(x_1)\), on which \(v>0\); likewise at \(x_3\). Their inner endpoints lie in the open connected set \(\{v>0\}\), which is path-connected. This gives a path \(\sigma_1\) from \(x_1\) to \(x_3\), lying in \(\Omega\) except at its endpoints, with \(v>0\) on all of it. In the same way there is a path \(\sigma_2\) from \(x_2\) to \(x_4\) with \(v<0\) on all of it. The paths \(\Phi^{-1}\circ\sigma_1\) and \(\Phi^{-1}\circ\sigma_2\) satisfy the hypotheses of Lemma 4.2, so they meet, and so do \(\sigma_1\) and \(\sigma_2\), which is impossible. \(\square\)

**Proposition 5.2** ([OpenAI-HS, Proposition 2.5]; [Nad88, Theorem 3]). \(\dim V\le2\).

*Proof.* Suppose \(\dim V\ge3\). The linear map \(v\mapsto\bigl(\int\beta h_v\cos\theta\,ds,\int\beta h_v\sin\theta\,ds\bigr)\) from \(V\) to \(\mathbb R^2\) has a nonzero kernel element \(v\). By Lemma 3.1, \(h=h_v\) is nonzero, takes both signs, and is orthogonal to \(\beta\), \(\beta\cos\theta\) and \(\beta\sin\theta\).

Choose \(\theta_0\) with \(h(e^{i\theta_0})<0\) and regard \(h\) as a function of \(\theta\in(\theta_0,\theta_0+2\pi)\). The set \(P\) of angles there where \(h>0\) is open and nonempty, and \(h<0\) near both ends of the interval; let \(a=\inf P\) and \(b=\sup P\). Then \(\theta_0<a<b<\theta_0+2\pi\), and \(h\le0\) outside \([a,b]\). There is no \(\theta'\in(a,b)\) with \(h(\theta')<0\): otherwise \(P\) has points \(p_1\in(a,\theta')\) and \(p_2\in(\theta',b)\), and the points \(e^{ip_1},e^{i\theta'},e^{ip_2},e^{i\theta_0}\) lie in counterclockwise order with signs \(+,-,+,-\), contrary to Lemma 5.1. So \(h\ge0\) on \([a,b]\). Put \(w=(b-a)/2\in(0,\pi)\), \(m=(a+b)/2\), and
\[
F(\theta)=\cos(\theta-m)-\cos w .
\]
On \((a,b)\), \(|\theta-m|<w\) and \(F>0\). For \(\theta\) in \((\theta_0,a)\cup(b,\theta_0+2\pi)\), \(\theta-m\) lies in \((w-2\pi,-w)\cup(w,2\pi-w)\), where the cosine is less than \(\cos w\), so \(F<0\). Hence \(Fh\ge0\) everywhere and \(Fh>0\) on the nonempty open set \(P\). So \(\int\beta Fh\,ds>0\). But \(F=\cos m\cos\theta+\sin m\sin\theta-\cos w\) is a combination of \(1,\cos\theta,\sin\theta\), so this integral vanishes. \(\square\)

The bound is due to Nadirashvili [Nad88, Theorem 3], who proved it for the first positive Neumann eigenvalue of every two-dimensional Riemannian manifold diffeomorphic to a disc with nonpositive Gaussian curvature.

## 6. Exercises

**6.1.** Let \(\Omega=\mathbb D\) and \(\Phi(z)=z\). Show that the function \(L\) of the proof of Lemma 3.1 is radial, and deduce that \(\beta\) is constant.

**6.2.** Check (4.1) for \(p=1\) and \(q=i\).

**6.3.** Show that Lemma 4.2 fails when the endpoints do not alternate: give two disjoint chords of \(\overline{\mathbb D}\) joining \(1\) to \(i\) and \(-1\) to \(-i\).

**6.4.** In the proof of Proposition 5.2 take \(a=0\) and \(b=\pi\). Compute \(F\).

**6.5.** Let \(\Omega=\mathbb D\). Show that \(\dim V=2\).

## 7. Solutions

**6.1.** For a rotation \(R\), \(L\circ R\) solves the same problem, and the solution is unique (it is the Riesz–Fréchet representative). So \(L\) is radial, \(\partial_\nu L\) is constant on the circle, and \(\beta=|\Phi'|(-\partial_\nu L)\) is constant.

**6.2.** Here \(\varphi_p=0\) and \(q=e^{i\kappa}\) with \(\kappa=-3\pi/2\in(-2\pi,0)\). Formula (4.1) gives \(\theta_1(1-i)=-3\pi/4+\pi/2=-\pi/4\), the argument of \(1-i\).

**6.3.** The segments \([1,i]\) and \([-1,-i]\) lie in the half-planes \(x+y\ge1\) and \(x+y\le-1\), so they are disjoint. The points \(1,i,-1,-i\) are in counterclockwise order, and the paths join the first two and the last two, so the endpoints do not alternate.

**6.4.** \(m=\pi/2\), \(w=\pi/2\), and \(F(\theta)=\cos(\theta-\pi/2)=\sin\theta\).

**6.5.** Rotations \(R\) of the disc map \(V\) into itself, since (3.1) of the first lesson is rotation invariant. If \(V\) were spanned by one function \(v\), then \(v\circ R_\theta=c(\theta)v\) with \(c(\theta)=\pm1\) (the \(L^2\) norm is preserved) and \(c\) continuous with \(c(0)=1\), so \(c=1\) and \(v\) would be radial. Then \(h_v\) is constant, and (3.1) with constant \(\beta\) (Exercise 6.1) gives \(h_v=0\), so \(v=0\) by Lemma 3.1. Hence \(\dim V\ge2\), and Proposition 5.2 gives equality.

## References

- [OpenAI-HS] OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains*, OpenAI Math Release preprint, 24 September 2026, Lemmas 2.2–2.4, Proposition 2.5. https://github.com/openai/math/tree/main/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026
- [Nad88] N. S. Nadirashvili, *Multiple eigenvalues of the Laplace operator*, Math. USSR-Sb. 61 (1988), 225–238, Theorem 3. https://www.mathnet.ru/eng/sm2554
