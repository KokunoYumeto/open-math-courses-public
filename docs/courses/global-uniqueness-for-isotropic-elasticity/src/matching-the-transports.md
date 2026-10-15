# Matching the transports

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Each of the two media has its own transport equation for the leading pair of displacement and divergence. In suitable variables both equations have the form \(D_\theta(p,s)=M_{j,\theta}(p,s)\) on the same three-dimensional space \(\mathcal E_\theta\), and their upper rows coincide. This lesson compares them [OpenAI-EL, Section 5]. Exact solutions for the first medium, from [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md), are transferred to the second medium by [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md). The Carleman estimate keeps the transferred leading pairs bounded as \(\tau\to\infty\), and their weak limits are solutions of the second transport equation that agree with the first ones outside \(\Omega\). The result is a field \(G(x,[\theta])\) of endomorphisms of \(\mathcal E_\theta\) carrying solutions of the first equation to solutions of the second, equal to the identity outside a ball and holomorphic in the direction \([\theta]\). Cekić used complex parallel transport and holomorphic dependence on the direction in the same way for connection Laplacians on a trivial vector bundle, where the full Dirichlet-to-Neumann map of the system is given [Cekić 2025].

- The transport normal form (Section 1).
- The null conic and the bundles over it (Section 2).
- The comparison equation (Section 3).
- The matching theorem (Section 4).

We keep the notation of the earlier lessons of this course: the extended pairs of moduli \((\lambda_j,\mu_j)\), equal outside \(\Omega\) and constant outside \(B_r\), with \(m_j,k_j,\ell_j\); a nonzero null vector \(\theta\), \(D=D_\theta\), \(E_\tau=e^{\tau\theta\cdot x}\), \(h=\tau^{-1}\); the spaces \(H_\theta\), \(\mathcal E_\theta\) and the coordinates \((y,t)\) of Section 2 of [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md). Weak limits come from the fact that every bounded sequence in a Hilbert space has a weakly convergent subsequence, Lemma K.2 of [Complex manifolds and Kähler metrics](course:DG-FND/complex-manifolds-and-kahler-metrics). A dot between complex vectors is the complex bilinear product.

## 1. The transport normal form

**Lemma 1.1** (transport normal form; [OpenAI-EL, Lemma 5.1]). For one pair of moduli put \(g=\nabla\log m\). The change of variables
\[
\begin{gathered}p=\sqrt m\,a,\\ s=-\frac k{2\sqrt m}\,b-\frac12\,g\cdot p\end{gathered}\tag{1.1}
\]
is a smooth invertible map of \(\mathcal E_\theta\) to itself at each point, and it transforms the constrained transport equation (2.2) of [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md) into
\[
\begin{gathered}D\binom ps=M_\theta\binom ps,\\ M_\theta=\begin{pmatrix}0&\theta\\ Q_\theta\cdot&T_\theta\end{pmatrix}\\ \text{on }H_\theta\oplus\mathbb C,\end{gathered}\tag{1.2}
\]
where
\[
\begin{aligned}&T_\theta=D\log(k/\ell),\\&Q_\theta=\frac12\Bigl[\Bigl(\frac m\ell D\log k\\&\qquad-\frac12\,\theta\cdot g\Bigr)g-\frac m\ell\,Dg\Bigr].\end{aligned}\tag{1.3}
\]
The bottom-left entry is the linear form \(p\mapsto Q_\theta\cdot p\). For fixed \(x\), \(M_\theta\) is linear in \(\theta\).

*Proof.* The inverse map is \(a=m^{-1/2}p\), \(b=-\frac{2\sqrt m}k\bigl(s+\frac12g\cdot p\bigr)\), defined because \(m,k>0\); multiplication by \(\sqrt m\) preserves \(H_\theta\). Since \(D(\sqrt m\,a)=\sqrt m\,Da+\frac{Dm}{2\sqrt m}a\), division of the first equation of (2.2), \(2m\,Da+(Dm)a+\theta(kb+\nabla m\cdot a)=0\), by \(\sqrt m\) gives
\[
\begin{aligned}2\,Dp&=2\sqrt m\,Da+\frac{Dm}{\sqrt m}\,a\\&=-\frac1{\sqrt m}\,\theta\,(kb+\nabla m\cdot a)=2\theta s,\end{aligned}
\]
where the last step uses \(\nabla m\cdot a=m\,g\cdot a=\sqrt m\,g\cdot p\) and the definition of \(s\). So \(Dp=\theta s\).

Dividing the second equation of (2.2) by two and using \(\nabla m=mg\),
\[
\begin{aligned}0&=\ell\,Db+(Dk)b\\&\quad+2\nabla m\cdot Da+(D\nabla m)\cdot a .\end{aligned}
\]
Here \(2\nabla m\cdot Da\) is \(2\sqrt m\,g\cdot Dp-\sqrt m\,(D\log m)\,g\cdot p\), and \((D\nabla m)\cdot a=\sqrt m\bigl((D\log m)g+Dg\bigr)\cdot p\); the terms with \((D\log m)\,g\cdot p\) cancel, and with \(Dp=\theta s\),
\[
\begin{aligned}&\ell\,Db=-(Dk)\,b\\&\quad-2\sqrt m\,(\theta\cdot g)\,s\\&\quad-\sqrt m\,(Dg)\cdot p .\end{aligned}\tag{1.4}
\]
Put \(\gamma=D\log m=\theta\cdot g\). Differentiating the definition of \(s\), with \(D\bigl(\frac k{2\sqrt m}\bigr)=\frac k{2\sqrt m}\bigl(D\log k-\frac\gamma2\bigr)\), \(Dp=\theta s\) and \(-\frac k{2\sqrt m}\,b=s+\frac12g\cdot p\),
\[
\begin{aligned}Ds&=\Bigl(D\log k-\frac\gamma2\Bigr)\Bigl(s+\frac12g\cdot p\Bigr)\\&\quad-\frac k{2\sqrt m}\,Db-\frac12(Dg)\cdot p-\frac\gamma2\,s .\end{aligned}
\]
By (1.4) and the same expression for \(b\),
\[
\begin{aligned}&-\frac k{2\sqrt m}\,Db\\&\quad=-\frac k\ell(D\log k)\Bigl(s+\frac12g\cdot p\Bigr)\\&\qquad+\frac k\ell\,\gamma s+\frac k{2\ell}(Dg)\cdot p .\end{aligned}
\]
With \(c=m/\ell=1-k/\ell\), the sum is
\[
\begin{aligned}Ds&=c\,(D\log k-\gamma)\,s\\&\quad+\frac12\bigl[(c\,D\log k-\gamma/2)\,g\\&\qquad-c\,Dg\bigr]\cdot p .\end{aligned}
\]
Finally \(D\log(k/\ell)=D\log k-\frac{Dk+Dm}\ell\), which equals \(\frac m\ell(D\log k-D\log m)\) since \(\ell=k+m\); this gives (1.3). The top row takes values in \(H_\theta\) because \(\theta\cdot\theta=0\), and every entry is linear in \(\theta\). \(\square\)

For the two pairs we write \(M_{j,\theta}\), \(Q_{j,\theta}\), \(T_{j,\theta}\). The upper row \(Dp=\theta s\) is the same for both, and outside \(\overline\Omega\) the two normal forms, and the changes of variables (1.1), coincide.

## 2. The null conic and the bundles over it

Two nonzero null vectors define the same equations up to a factor: \(D_{c\theta}=cD_\theta\), \(M_{j,c\theta}=cM_{j,\theta}\) and \(\mathcal E_{c\theta}=\mathcal E_\theta\) for \(c\in\mathbb C\setminus\{0\}\). The directions form the *projective null conic*
\[
\mathcal C=\{[\theta]\in\mathbb C\mathrm P^2:\theta\cdot\theta=0\}.
\]

**Lemma 2.1** (a parametrization; [OpenAI-EL, Lemma 6.1]). The map \([z_0:z_1]\mapsto[\theta(z_0,z_1)]\), with
\[
\theta(z_0,z_1)=\begin{pmatrix}z_0^2-z_1^2\\ i(z_0^2+z_1^2)\\ 2z_0z_1\end{pmatrix},\tag{2.1}
\]
is a bijection of \(\mathbb C\mathrm P^1\) onto \(\mathcal C\). Its inverse is \([\theta]\mapsto[1:\theta_3/(\theta_1-i\theta_2)]\) where \(\theta_1-i\theta_2\ne0\), and \([\theta]\mapsto[\theta_3/(-\theta_1-i\theta_2):1]\) where \(-\theta_1-i\theta_2\ne0\); the two denominators do not vanish together on \(\mathcal C\).

*Proof.* The bilinear square \(\theta(z_0,z_1)\cdot\theta(z_0,z_1)\) is \((z_0^2-z_1^2)^2-(z_0^2+z_1^2)^2+4z_0^2z_1^2=0\), \(\theta\ne0\) for \((z_0,z_1)\ne0\), and \(\theta(cz)=c^2\theta(z)\); so the map is defined. Note \(\theta_1-i\theta_2=2z_0^2\), \(-\theta_1-i\theta_2=2z_1^2\) and \(\theta_3=2z_0z_1\) for \(\theta=\theta(z_0,z_1)\), which shows that the displayed formulas invert the map where they are defined. If both \(\theta_1-i\theta_2\) and \(-\theta_1-i\theta_2\) vanish, then \(\theta_1=\theta_2=0\), and \(\theta\cdot\theta=0\) gives \(\theta_3=0\). For surjectivity, let \(\theta\ne0\) be null with \(w=\theta_1-i\theta_2\ne0\), and put \(z_1=\theta_3/w\). From \(0=\theta\cdot\theta=w(\theta_1+i\theta_2)+\theta_3^2\) we get \(\theta_1+i\theta_2=-wz_1^2\), hence \(\theta_1=\frac w2(1-z_1^2)\), \(\theta_2=\frac{iw}2(1+z_1^2)\), \(\theta_3=\frac w2\cdot2z_1\): \(\theta=\frac w2\theta(1,z_1)\). The case \(-\theta_1-i\theta_2\ne0\) is symmetric. \(\square\)

Through this bijection, \(\mathcal C\) is a compact connected Riemann surface, with the two charts \(v=z_1/z_0\) and \(v=z_0/z_1\); on them, \(\theta(1,v)\) and \(\theta(v,1)\) are holomorphic nonzero representatives. A function on \(\mathcal C\) is holomorphic if it is holomorphic in both charts.

The spaces \(H_\theta\) and \(\mathcal E_\theta=H_\theta\oplus\mathbb C\) depend only on \([\theta]\). They form holomorphic vector bundles \(H\) and \(\mathcal E\) over \(\mathcal C\), subbundles of the trivial bundles with fibers \(\mathbb C^3\) and \(\mathbb C^4\): where \(\theta_i\ne0\), the vectors \(e_j-(\theta_j/\theta_i)e_i\), \(j\ne i\), form a basis of \(H_\theta\) depending holomorphically on the direction, and adjoining the scalar component gives a basis of \(\mathcal E_\theta\). A section of \(\mathcal E\), or an endomorphism field of \(\mathcal E\), is holomorphic if its components in these bases are holomorphic functions of the chart variable.

## 3. The comparison equation

Fix \(\theta\) and an open interval \(J\subset(-2r,2r)\), and suppose that \(Y_1\) is a smooth map on the cylinder \(D^2_{2r}\times J\), with values in invertible linear maps \(\mathbb C^3\to\mathcal E_\theta\), whose three columns solve \(DY_1=M_{1,\theta}Y_1\), and that \(Y_2\) is a locally square-integrable map on the cylinder with values in linear maps \(\mathbb C^3\to\mathcal E_\theta\) whose columns solve \(DY_2=M_{2,\theta}Y_2\) in the sense of distributions. If \(Y_2=Y_1\) almost everywhere outside \(\overline\Omega\), put
\[
G=Y_2Y_1^{-1},\qquad W=G-\mathrm{Id}.
\]
Multiplication of a distribution by the smooth \(Y_1^{-1}\) obeys the product rule, and \(D(Y_1^{-1})=-Y_1^{-1}(DY_1)Y_1^{-1}\), which is \(-Y_1^{-1}M_{1,\theta}\); so, with the first relation in the sense of distributions,
\[
\begin{gathered}DG=M_{2,\theta}G-GM_{1,\theta},\\ G=\mathrm{Id}\ \text{outside }\overline\Omega .\end{gathered}\tag{3.1}
\]
Only \(Y_1\) needs to be invertible. Using a basis of \(\mathcal E_\theta\), regard endomorphisms as \(3\times3\) matrices and these as vectors of nine entries. For a transverse coordinate \(t\), define the planar operator
\[
\begin{aligned}\mathcal P_{\theta,t}W&=D_\theta W-M_{2,\theta}W\\&\quad+WM_{1,\theta},\\ f_{\theta,t}&=M_{2,\theta}-M_{1,\theta},\end{aligned}\tag{3.2}
\]
with coefficients restricted to the plane of \(t\). Then (3.1) says \(\mathcal P_{\theta,t}W=f_{\theta,t}\), and \(f_{\theta,t}=0\) outside \(\overline\Omega\). In the coordinates \((y,t)\), \(D_\theta=\rho_0(\partial_{y_1}+i\partial_{y_2})\) with \(\rho_0=|\operatorname{Re}\theta|\), so \(\mathcal P_{\theta,t}\) has the form of Lemma 3.1 of [Planar transport equations](planar-transport-equations.md).

## 4. The matching theorem

**Proposition 4.1** (matching of the transports; [OpenAI-EL, Proposition 5.3]). There is a unique smooth field \(G(x,[\theta])\in\operatorname{End}(\mathcal E_\theta)\), for \((x,[\theta])\in\mathbb R^3\times\mathcal C\), such that for every nonzero representative \(\theta\)
\[
\begin{gathered}D_\theta G=M_{2,\theta}G-GM_{1,\theta},\\ G(x,[\theta])=\mathrm{Id}\ \text{for }|x|>2r .\end{gathered}\tag{4.1}
\]
For each fixed \(x\), \(G(x,\cdot)\) is a holomorphic section of the endomorphism bundle of \(\mathcal E\) over \(\mathcal C\). For each fixed direction, the first equation in (4.1) has at most one smooth solution \(G\) with \(G-\mathrm{Id}\) of compact support.

*Proof.* *Physical transfer and weak limits.* Fix \(\theta\) and \(t_0\in(-2r,2r)\). Proposition 3.1 of [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md), for the first pair, gives an interval \(J\ni t_0\), three solutions \((a_0^\nu,b_0^\nu)\) of the first transport equation forming a basis of \(\mathcal E_\theta\) on \(D^2_{2r}\times J\), and exact solutions \(u^\nu_{1,\tau}\) on \(B_{5r}\) with (3.1) of that lesson. We work with one column and omit \(\nu\). By Proposition 4.1 of [Boundary jets and the transfer of solutions](boundary-jets-and-the-transfer-of-solutions.md), \(u_{1,\tau}\) has a smooth counterpart \(u_{2,\tau}\) on \(B_{5r}\) with \(L_2u_{2,\tau}=0\) and \(u_{2,\tau}=u_{1,\tau}\) outside \(\overline\Omega\). Put \(V_{j,\tau}=(u_{j,\tau},\operatorname{div}u_{j,\tau})\). Then \(V_{2,\tau}-V_{1,\tau}\) is smooth with support in \(\overline\Omega\subset B_r\). By Lemma 1.1 of An augmented system and a Carleman estimate, \(R_j\) and \(S_j\) vanish at \(V_{j,\tau}\), so \(\mathcal L_jV_{j,\tau}=0\) by (1.3) of that lesson, and
\[
\mathcal L_2(V_{2,\tau}-V_{1,\tau})=(\mathcal L_1-\mathcal L_2)V_{1,\tau}.
\]
By Lemma 1.2 of that lesson, \(\mathcal L_1-\mathcal L_2\) has order at most one with coefficients supported in \(\overline\Omega\), so by (3.1) of [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md) the function \(F_\tau=E_\tau^{-1}(\mathcal L_1-\mathcal L_2)V_{1,\tau}\) satisfies
\[
\begin{aligned}\|F_\tau\|_{L^2}&\le C\bigl(\|E_\tau^{-1}V_{1,\tau}\|_{L^2(B_{4r})}\\&\quad+\|E_\tau^{-1}\nabla V_{1,\tau}\|_{L^2(B_{4r})}\bigr)=O(\tau).\end{aligned}
\]
Proposition 3.1 of An augmented system and a Carleman estimate, for the second pair on \(B_{5r}\), and Lemma 2.1(1) of that lesson give
\[
\begin{aligned}&\|E_\tau^{-1}(V_{2,\tau}-V_{1,\tau})\|_{H^1_h}\\&\quad\le Ch\,\|F_\tau\|_{L^2}\le C .\end{aligned}\tag{4.2}
\]
So \(E_\tau^{-1}V_{2,\tau}\) is bounded in \(L^2(B_{4r})\). Along a sequence \(\tau\to\infty\), chosen simultaneously for the three columns, it converges weakly in \(L^2(B_{4r})\) to some \((\tilde a,\tilde b)\). As \(E_\tau^{-1}V_{2,\tau}=E_\tau^{-1}V_{1,\tau}\) outside \(\overline\Omega\), and the latter converges strongly to \((a_0,b_0)\), the limit satisfies, almost everywhere on \(B_{4r}\setminus\overline\Omega\),
\[
(\tilde a,\tilde b)=(a_0,b_0) .\tag{4.3}
\]

*The limit equations.* Write \((a_\tau,b_\tau)=E_\tau^{-1}V_{2,\tau}\). Since \(R_2\) and \(S_2\) vanish at \(V_{2,\tau}=(u_{2,\tau},\operatorname{div}u_{2,\tau})\), Lemma 1.1 of [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md) gives
\[
\begin{gathered}R_2^\theta(a_\tau,b_\tau)+\tau^{-1}R_2(a_\tau,b_\tau)=0,\\ S_2^\theta(a_\tau,b_\tau)+\tau^{-1}S_2(a_\tau,b_\tau)=0 .\end{gathered}
\]
Against a fixed test function on \(B_{4r}\), all derivatives can be moved to the test function; the terms with \(\tau^{-1}\) then tend to zero because \((a_\tau,b_\tau)\) is bounded in \(L^2\), and the others converge by weak convergence. Also \(E_\tau^{-1}\operatorname{div}(E_\tau a_\tau)=b_\tau\), that is, \(\theta\cdot a_\tau=\tau^{-1}(b_\tau-\operatorname{div}a_\tau)\), so \(\theta\cdot\tilde a=0\) in the sense of distributions, hence almost everywhere. Thus \((\tilde a,\tilde b)\) takes values in \(\mathcal E_\theta\) and solves the second transport equation \(R_2^\theta=S_2^\theta=0\) in the sense of distributions on \(B_{4r}\). No derivative bound on the transferred pairs is needed for this.

*A comparison on almost every plane.* Apply the change of variables (1.1) of the first pair to the columns \((a_0^\nu,b_0^\nu)\), and that of the second pair to the limits \((\tilde a^\nu,\tilde b^\nu)\); by Lemma 1.1, valid for distributions since it uses only multiplications by smooth functions and the product rule, this gives \(Y_1\) and \(Y_2\) as in Section 3. Points with \(|y|<2r\) and \(|t|<2r\) satisfy \(|x|<\sqrt8\,r<4r\), so the cylinder \(D^2_{2r}\times J\) lies in \(B_{4r}\). The two changes of variables agree outside \(\overline\Omega\), so (4.3) gives \(Y_2=Y_1\) almost everywhere there, and \(G\) and \(W=G-\mathrm{Id}\) satisfy (3.1) on the cylinder. As \(\overline\Omega\subset B_r\), \(W=0\) where \(|y|>r\); on \(\{|y|\le r\}\times J'\), for compact \(J'\subset J\), \(Y_1^{-1}\) is bounded, so \(W\) is square integrable there. Testing (3.1) with products \(\varphi(y)\psi(t)\), and using a countable family of planar test functions \(\varphi\) dense in \(C^\infty_c(D^2_{2r})\), Fubini's theorem shows that for almost every \(t\in J\), \(W(\cdot,t)\in L^2(D^2_{2r})\) has support in \(\overline{D^2_r}\) and \(\mathcal P_{\theta,t}W(\cdot,t)=f_{\theta,t}\) in the sense of distributions.

*Existence on every plane.* The coefficients of \(\mathcal P_{\theta,t}\) and \(f_{\theta,t}\) are smooth in \((y,t)\). The parameters \(t\) with a supported solution have full measure in \(J\), hence are dense. By Lemma 3.1(3) of [Planar transport equations](planar-transport-equations.md), there is a supported solution for every \(t\in J\); it is unique and smooth in \((y,t)\). By uniqueness, the solutions obtained from different intervals \(J\) agree where they overlap, and since \(t_0\) was arbitrary this defines \(W\) for all \(|t|<2r\). Extend \(W\) by zero in \(y\) outside \(D^2_{2r}\); this is smooth, because \(W=0\) for \(r<|y|<2r\), and the equation holds there because \(f_{\theta,t}=0\). For \(r<|t|<2r\) the whole plane misses \(\overline\Omega\), so \(f_{\theta,t}=0\), and Lemma 3.1(1) of that lesson gives \(W=0\); extending by zero for \(|t|\ge2r\) is therefore smooth. For this direction we obtain a smooth global \(G\) with
\[
\begin{aligned}&\operatorname{supp}(G-\mathrm{Id})\\&\quad\subset\{|y|\le r,\ |t|\le r\}\\&\quad\subset\overline{B_{2r}} .\end{aligned}\tag{4.4}
\]
*Uniqueness.* If \(G,G'\) are two smooth solutions of the first equation of (4.1) with \(G-\mathrm{Id}\) and \(G'-\mathrm{Id}\) of compact support, their difference solves \(\mathcal P_{\theta,t}(G-G')=0\) on every plane with compact support, and Lemma 3.1(1) of [Planar transport equations](planar-transport-equations.md), applied with a radius \(R\) in place of \(r\) such that \(D^2_{2R}\) contains that support, gives \(G=G'\).

*Independence of the representative.* For \(c\ne0\) the equations for \(c\theta\) are those for \(\theta\) multiplied by \(c\), so uniqueness gives \(G(x,c\theta)=G(x,\theta)\): \(G\) is a function of \((x,[\theta])\).

*Smooth dependence on the direction.* Choose a local smooth representative \(\theta(v)\) of the directions, \(v\) in an open subset of \(\mathbb R^2\), and a smooth local basis of \(\mathcal E\). The vectors \(e_1(v)=\operatorname{Re}\theta(v)/|\operatorname{Re}\theta(v)|\), \(e_2(v)=\operatorname{Im}\theta(v)/|\operatorname{Im}\theta(v)|\) and \(e_3(v)=e_1(v)\times e_2(v)\) are orthonormal and smooth in \(v\). In the coordinates \(x=y_1e_1(v)+y_2e_2(v)+te_3(v)\), the comparison equation is a smooth family of operators as in Lemma 3.1 of [Planar transport equations](planar-transport-equations.md), with parameters \((t,v)\), on the fixed disk \(D^2_{2r}\), and for every parameter a supported solution has been constructed. By Lemma 3.1(3), the solution is smooth in \((y,t,v)\), and returning to the coordinates \(x\) gives smoothness in \((x,v)\). This uses only the existence for each fixed direction and uniqueness; no choice of subsequences depends on the direction.

*Holomorphic dependence.* Let \(v\) be a complex chart variable on \(\mathcal C\), with the holomorphic representative \(\theta(v)\) of Section 2 and a holomorphic basis of \(\mathcal E\) on the chart, which does not depend on \(x\). In this basis the matrices \(M_{j,\theta(v)}(x)\) are holomorphic in \(v\) for each \(x\), because the formulas (1.2) and (1.3) are linear in \(\theta\). Represent \(G\) in this basis and apply \(\partial_{\bar v}\) to the first equation of (4.1), holding \(x\) fixed; the joint smoothness just proved allows this. Since \(\partial_{\bar v}\theta(v)=0\) and \(\partial_{\bar v}M_{j,\theta(v)}=0\),
\[
\begin{aligned}&D_{\theta(v)}(\partial_{\bar v}G)-M_{2,\theta(v)}\,\partial_{\bar v}G\\&\quad+(\partial_{\bar v}G)\,M_{1,\theta(v)}=0 .\end{aligned}
\]
By (4.4), \(\partial_{\bar v}G=0\) for \(|x|>2r\), so \(\partial_{\bar v}G\) has compact support, and uniqueness on each plane gives \(\partial_{\bar v}G=0\). Thus \(G(x,\cdot)\) is holomorphic for every \(x\). \(\square\)

## 5. Exercises

**5.1.** For constant moduli, compute \(M_\theta\) in (1.2).

**5.2.** Check the formula \(D\log(k/\ell)=\frac m\ell\bigl(D\log k-D\log m\bigr)\).

**5.3.** Show that \(\theta(1,0)\), \(\theta(0,1)\) and \(\theta(1,1)\) span \(\mathbb C^3\). Conclude that null vectors span \(\mathbb C^3\).

**5.4.** Show that if \(G\) satisfies (4.1) for \(\theta\), it satisfies (4.1) for \(c\theta\), \(c\ne0\).

**5.5.** In the proof of Proposition 4.1, why does the Carleman estimate (4.2) give a bound independent of \(\tau\), although \(\|E_\tau^{-1}(\mathcal L_1-\mathcal L_2)V_{1,\tau}\|\) grows like \(\tau\)?

## 6. Solutions

**5.1.** All derivatives of the moduli vanish, so \(g=0\), \(T_\theta=0\) and \(Q_\theta=0\): \(M_\theta=\begin{pmatrix}0&\theta\\0&0\end{pmatrix}\), and the equations are \(Dp=\theta s\), \(Ds=0\).

**5.2.** Using \(\ell-k=m\),
\[
\begin{aligned}D\log(k/\ell)&=\frac{Dk}k-\frac{Dk+Dm}\ell\\&=\frac{(\ell-k)Dk-k\,Dm}{k\ell}\\&=\frac{m\,Dk-k\,Dm}{k\ell}\\&=\frac m\ell\Bigl(\frac{Dk}k-\frac{Dm}m\Bigr).\end{aligned}
\]

**5.3.** \(\theta(1,0)=(1,i,0)\), \(\theta(0,1)=(-1,i,0)\) and \(\theta(1,1)=(0,2i,2)\). Expanding along the last column, the determinant of the matrix with these rows is \(2\,(1\cdot i-i\cdot(-1))=4i\ne0\). So null vectors span \(\mathbb C^3\).

**5.4.** \(D_{c\theta}=cD_\theta\) and \(M_{j,c\theta}=cM_{j,\theta}\), so the equation for \(c\theta\) is \(c\) times the equation for \(\theta\); the condition for \(|x|>2r\) does not involve \(\theta\).

**5.5.** The estimate gains the factor \(h=\tau^{-1}\): \(\|E_\tau^{-1}U\|_{H^1_h}\le Ch\|E_\tau^{-1}\mathcal L_2U\|_{H^{-1}_h}\), and \(\|\cdot\|_{H^{-1}_h}\le\|\cdot\|_{L^2}\). The order-one forcing \((\mathcal L_1-\mathcal L_2)V_{1,\tau}\) is of size \(\tau\) after conjugation, so \(h\) times it is bounded. This is why the weighted derivative bound in (3.1) of [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md) is needed: the difference of the two operators has order one.

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Section 5 and Lemma 6.1. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
- [Cekić 2025] M. Cekić, *Calderón problem for systems via complex parallel transport*, SIAM J. Math. Anal. 57 (2025), no. 4, 3524–3560. https://arxiv.org/abs/2309.09348
