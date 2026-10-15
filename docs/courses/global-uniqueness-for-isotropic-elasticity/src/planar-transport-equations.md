# Planar transport equations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a complex vector \(\theta=\alpha+i\beta\) with \(\theta\cdot\theta=0\), the derivative \(D_\theta=\theta\cdot\nabla\) acts only in the plane spanned by \(\alpha\) and \(\beta\), where it is a multiple of the Cauchy–Riemann operator \(\partial_{\bar z}\). The leading terms of the solutions built in [Exact solutions with prescribed leading terms](exact-solutions-with-prescribed-leading-terms.md) satisfy first-order systems \(D_\theta V=MV\), and their comparison in [Matching the transports](matching-the-transports.md) needs two facts about such planar systems: invertible solutions exist over a whole disk, and a solution with compact support in a disk is determined by its equation [OpenAI-EL, Lemmas 4.1 and 5.2]. This lesson proves both, the first from a named hypothesis on holomorphic frames.

- The Cauchy transform and regularity for \(\partial_{\bar z}\) (Section 1).
- Frames and inhomogeneous equations (Section 2).
- Supported solutions (Section 3).

We use from the core course [Complex Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C50) (Lebl, *Guide to Cultivating Complex Analysis*, [Theorems 2.4.7 and 4.6.3](https://www.jirka.org/ca/ca.pdf)) the identity theorem and the Cauchy–Pompeiu formula; Plancherel's identity and the Sobolev norms \(\|F\|_{H^k}^2=(2\pi)^{-2}\int(1+|\xi|^2)^k|\widehat F|^2d\xi\) on \(\mathbb R^2\), which for integers \(k\ge0\) are equivalent to the sums of the \(L^2\) norms of the derivatives of order at most \(k\), from Sections 2 and 7 of [Fourier transforms, finite spectra and convex separation](course:elliptic-operators-and-boundary-problems/prerequisite-bridges); and from Section 1 of [Symbols, finite defects, and the index on a closed manifold](course:elliptic-operators-and-boundary-problems/global-elliptic-symbol-index) the compactness (I2), in its local form for functions supported in one fixed compact set, and the embedding of \(\bigcap_kH^k\) into smooth functions (I1).

## 1. The Cauchy transform and regularity for ∂/∂z̄

Write points of \(\mathbb R^2=\mathbb C\) as \(y=(y_1,y_2)\) or \(z=y_1+iy_2\), let \(dA\) be the area measure, \(\partial_{\bar z}=\frac12(\partial_{y_1}+i\partial_{y_2})\), and \(D^2_R=\{|y|<R\}\). For a bounded measurable function \(f\) with bounded support, matrix-valued or vector-valued, the *Cauchy transform* is
\[
(\mathcal Tf)(z)=\frac1\pi\int_{\mathbb C}\frac{f(w)}{z-w}\,dA(w).
\]

**Lemma 1.1.** Let \(f\) be bounded and measurable with support in a disk of radius \(\delta\).

1. \(|\mathcal Tf(z)|\le2\delta\sup|f|\) for every \(z\).
2. \(\mathcal Tf\) is continuous.
3. \(\partial_{\bar z}\mathcal Tf=f\) in the sense of distributions.

*Proof.* (1) Let \(D\) be the support disk and \(B=B(z,\delta)\), of the same area. As \(|z-w|^{-1}\ge\delta^{-1}\) on \(B\) and \(\le\delta^{-1}\) off \(B\), 
\[
\begin{aligned}&\int_{D\setminus B}|z-w|^{-1}\le\operatorname{area}(D\setminus B)/\delta\\&\quad=\operatorname{area}(B\setminus D)/\delta\le\int_{B\setminus D}|z-w|^{-1}.\end{aligned}
\]
So \(\int_D|z-w|^{-1}dA\le\int_B|z-w|^{-1}dA\), and the latter equals \(2\pi\delta\).

(2) After the substitution \(w\mapsto z-w\),
\[
\begin{aligned}&\mathcal Tf(z)-\mathcal Tf(z')\\&\quad=\frac1\pi\int\bigl(f(z-w)-f(z'-w)\bigr)\\&\qquad\qquad\times w^{-1}\,dA(w).\end{aligned}
\]
The part with \(|w|<\eta\) is at most \(4\eta\sup|f|\), and the rest at most \(\eta^{-1}\pi^{-1}\int|f(z-w)-f(z'-w)|\,dA(w)\), which tends to zero as \(z'\to z\) by continuity of translation in \(L^1\).

(3) For a test function \(\varphi\), the Cauchy–Pompeiu formula on a large circle gives \(\varphi(w)=-\frac1\pi\int\frac{\partial_{\bar z}\varphi(z)}{z-w}\,dA(z)\). By Fubini's theorem, which applies because \(|z-w|^{-1}\) is locally integrable,
\[
\begin{aligned}&-\int\mathcal Tf\,\partial_{\bar z}\varphi\,dA\\&\quad=-\frac1\pi\int f(w)\\&\qquad\times\int\frac{\partial_{\bar z}\varphi(z)}{z-w}\,dA(z)\,dA(w)\\&\quad=\int f\varphi\,dA .\qquad\square\end{aligned}
\]

**Lemma 1.2** (regularity). Let \(U\subset\mathbb C\) be open, \(b\in C^\infty(U;\mathbb C^{n\times n})\), \(g\in C^\infty(U;\mathbb C^n)\), and let \(W\in L^2_{\mathrm{loc}}(U;\mathbb C^n)\) satisfy \(\partial_{\bar z}W=bW+g\) in the sense of distributions. Then \(W\in C^\infty(U)\).

*Proof.* For \(F\in L^2(\mathbb R^2)\) with compact support, \(\widehat{\partial_{\bar z}F}(\xi)=\frac i2(\xi_1+i\xi_2)\widehat F(\xi)\), of modulus \(\frac12|\xi||\widehat F|\). Hence
\[
\begin{aligned}(1+|\xi|^2)^{k+1}|\widehat F|^2&=(1+|\xi|^2)^k|\widehat F|^2\\&\quad+4(1+|\xi|^2)^k\bigl|\widehat{\partial_{\bar z}F}\bigr|^2,\end{aligned}
\]
so \(F\in H^k\) and \(\partial_{\bar z}F\in H^k\) give \(F\in H^{k+1}\). Suppose \(W\in H^k_{\mathrm{loc}}(U)\) for some integer \(k\ge0\), and let \(\chi\in C^\infty_c(U)\). Then \(F=\chi W\in H^k\), and \(\partial_{\bar z}F=\chi(bW+g)+(\partial_{\bar z}\chi)W\in H^k\) by the product rule for weak derivatives. So \(\chi W\in H^{k+1}\), and \(W\in H^{k+1}_{\mathrm{loc}}(U)\). By induction \(W\in H^k_{\mathrm{loc}}\) for every \(k\), and by (I1) \(W\) is smooth. \(\square\)

**Corollary 1.3.** If \(w\in L^2_{\mathrm{loc}}(U)\) and \(\partial_{\bar z}w=0\) in the sense of distributions, then \(w\) is holomorphic. \(\square\)

## 2. Frames and inhomogeneous equations

A *frame* of the equation \(\partial_{\bar z}V=AV\), for a smooth \(A\) with values in \(\mathbb C^{n\times n}\), is a smooth solution \(V\) with values in invertible \(n\times n\) matrices. Its columns are \(n\) solutions that are linearly independent at every point.

**Lemma 2.1** (local frames). Let \(A\in C^\infty(U;\mathbb C^{n\times n})\) on an open set \(U\subset\mathbb C\). Every \(z_0\in U\) has a disk \(D(z_0,\delta)\subset U\) on which \(\partial_{\bar z}V=AV\) has a frame \(V\) with \(|V-\mathrm{Id}|\le\frac12\) in operator norm.

*Proof.* Choose \(\delta_0\) with \(\overline{D(z_0,2\delta_0)}\subset U\), let \(M=\max|A|\) on that closed disk, and take \(\delta\le\delta_0\) with \(4\delta M\le\frac13\). Let \(\chi\in C^\infty_c(D(z_0,2\delta))\) with \(0\le\chi\le1\) and \(\chi=1\) on \(D(z_0,\delta)\). On bounded measurable matrix functions with the supremum norm, \(KV=\mathcal T(\chi AV)\) has norm at most \(\frac13\) by Lemma 1.1(1). The Neumann series \(V=\sum_{j\ge0}K^j\mathrm{Id}\) solves \(V=\mathrm{Id}+KV\) and satisfies \(\sup|V-\mathrm{Id}|\le\frac{1/3}{1-1/3}=\frac12\), so \(V(z)\) is invertible for every \(z\). By Lemma 1.1(3), \(\partial_{\bar z}V=\chi AV\), which is \(AV\) on \(D(z_0,\delta)\). As \(V\) is bounded, Lemma 1.2 makes it smooth there. \(\square\)

If \(V_1,V_2\) are frames on overlapping disks, then on the overlap
\[
\begin{aligned}\partial_{\bar z}(V_1^{-1}V_2)&=-V_1^{-1}(\partial_{\bar z}V_1)V_1^{-1}V_2\\&\quad+V_1^{-1}AV_2=0 ,\end{aligned}
\]
so the transition matrices are holomorphic. Frames over a whole disk are given by the following hypothesis.

**Hypothesis (HF)** (frames over a disk; [Forstnerič 2009, Theorem 1.1]). Let \(R>0\) and \(A\in C^\infty(D^2_R;\mathbb C^{n\times n})\). Then \(\partial_{\bar z}V=AV\) has a frame on all of \(D^2_R\).

The local frames of Lemma 2.1 and their holomorphic transition matrices define a holomorphic vector bundle over the disk, and the frames identify its underlying smooth bundle with the trivial bundle; so its holomorphic frame bundle, a holomorphic fiber bundle with fiber the complex Lie group \(\mathrm{GL}_n(\mathbb C)\), has a continuous section. The disk is a Stein manifold and \(\mathrm{GL}_n(\mathbb C)\) is a complex homogeneous manifold, and the Oka principle for sections of such bundles [Forstnerič 2009, Theorem 1.1], which in the homogeneous case goes back to Grauert, gives a holomorphic section: a holomorphic frame of the bundle, which in the smooth trivialization is a frame as stated.

**Lemma 2.2** (frames depending on a parameter; [OpenAI-EL, Lemma 4.1]). Let \(I\subset\mathbb R\) be an open interval and \(A\in C^\infty(D^2_R\times I;\mathbb C^{n\times n})\). For every \(R'<R\) and \(t_0\in I\) there are an open interval \(I_0\ni t_0\) and a smooth function \(V\) on \(D^2_{R'}\times I_0\), with invertible values, such that \(\partial_{\bar z}V=AV\) for each \(t\in I_0\).

*Proof.* Let \(V_0\) be a frame of \(\partial_{\bar z}V=A(\cdot,t_0)V\) on \(D^2_R\), by Hypothesis (HF). Writing \(V=V_0W\), the equation becomes
\[
\begin{aligned}\partial_{\bar z}W&=B(z,t)W,\qquad\text{where}\\ B(z,t)&=V_0(z)^{-1}\bigl(A(z,t)\\&\qquad-A(z,t_0)\bigr)V_0(z).\end{aligned}
\]
Choose \(\chi\in C^\infty_c(D^2_R)\) with \(0\le\chi\le1\), equal to one near \(\overline{D^2_{R'}}\). On the compact set \(\operatorname{supp}\chi\), \(B(\cdot,t)\to0\) uniformly as \(t\to t_0\); choose a compact interval \(I_1\ni t_0\) in \(I\) with \(2R\sup_{\operatorname{supp}\chi\times I_1}|B|\le\frac13\), and let \(I_0\) be its interior. The operators \(K_t:W\mapsto\mathcal T(\chi B(\cdot,t)W)\) on bounded measurable matrix functions then have norm at most \(\frac13\), and \(W_t=(I-K_t)^{-1}\mathrm{Id}\) satisfies \(\sup|W_t-\mathrm{Id}|\le\frac12\) and \(\partial_{\bar z}W_t=B(\cdot,t)W_t\) on \(D^2_{R'}\).

*Smoothness.* By Lemma 1.1(1), \(\|K_t-K_s\|\) is at most \(2R\sup|\chi(B(\cdot,t)-B(\cdot,s))|\), and the same bound for the difference quotients shows that \(t\mapsto K_t\) is \(C^\infty\) in operator norm, with derivatives \(W\mapsto\mathcal T(\chi\,\partial_t^kB\,W)\); hence so is \(t\mapsto(I-K_t)^{-1}\), and \(t\mapsto W_t\) is \(C^\infty\) as a map into bounded functions, with derivatives \(\partial_t^kW_t\) satisfying \(\partial_{\bar z}(\partial_t^kW_t)=\sum_{j\le k}\binom kj(\partial_t^jB)(\partial_t^{k-j}W_t)\) on \(D^2_{R'}\). The proof of Lemma 1.2 is quantitative: for \(F=\chi'W\) it gives \(\|F\|_{H^{q+1}}^2=\|F\|_{H^q}^2+4\|\partial_{\bar z}F\|_{H^q}^2\), so on a smaller disk the \(H^{q+1}\) norm of a solution of \(\partial_{\bar z}W=bW+g\) is bounded by its \(H^q\) norm and that of \(g\) on a larger disk, linearly. Applied to \(\partial_t^kW_t-\partial_t^kW_s\), whose equation has the right side \(B(\cdot,t)(\partial_t^kW_t-\partial_t^kW_s)\) plus terms that tend to zero in every \(H^q\) as \(s\to t\), and to the difference quotients of \(\partial_t^kW_t\), this shows that \(t\mapsto\partial_t^kW_t\) is continuous into \(H^m\) of every smaller disk, for every \(k\) and \(m\), and is the \(k\)-th derivative there. By (I1) the same holds with \(C^m\) in place of \(H^m\). Hence all mixed derivatives of \(W\) in \((z,t)\) exist and are continuous on \(D^2_{R''}\times I_0\) for every \(R''<R'\). Replacing \(R'\) by a number between \(R'\) and \(R\) at the start gives the statement on \(D^2_{R'}\times I_0\), and \(V=V_0W\). \(\square\)

**Lemma 2.3** (inhomogeneous equations; [OpenAI-EL, Lemma 4.1]). Let \(V\) be as in Lemma 2.2 on \(D^2_{R'}\times I_0\), let \(R''<R'\), and let \(F\in C^\infty(D^2_{R'}\times I_0;\mathbb C^n)\). Then \(\partial_{\bar z}v=Av+F\) has a smooth solution on \(D^2_{R''}\times I_0\). If \(F(\cdot,t)=0\) for \(t\) outside a compact set \(K\subset I_0\), the solution can be chosen with \(v(\cdot,t)=0\) for \(t\notin K\).

*Proof.* Choose \(\chi\in C^\infty_c(D^2_{R'})\) equal to one near \(\overline{D^2_{R''}}\), and put \(v=V\,\mathcal T(\chi V^{-1}F)\), the transform acting in \(z\) for each \(t\). Writing \(\mathcal Tg(z)=\frac1\pi\int g(z-w)\,w^{-1}dA(w)\), derivatives of a smooth \(g\) with support in a fixed compact set can be taken under the integral, so \(v\) is smooth. By Lemma 1.1(3), \(\partial_{\bar z}v=AV\mathcal T(\chi V^{-1}F)+V\chi V^{-1}F\), which is \(Av+F\) on \(D^2_{R''}\). If \(F(\cdot,t)=0\), then \(v(\cdot,t)=0\). \(\square\)

The same statements hold for \(c\,\partial_{\bar z}\) with a nonzero constant \(c\), and for systems \(Q\,\partial_{\bar z}v=Av+F\) with a smooth invertible matrix \(Q\), after dividing by \(c\) or multiplying by \(Q^{-1}\).

## 3. Supported solutions

**Lemma 3.1** (supported planar transport; [OpenAI-EL, Lemma 5.2]). Let \(r>0\), let \(\mathcal U\subset\mathbb R^d\) be open, \(n\ge1\), and
\[
\begin{gathered}\mathcal P_\rho=\gamma(\rho)(\partial_{y_1}+i\partial_{y_2})+A(y,\rho),\\ \rho\in\mathcal U,\end{gathered}
\]
with \(\gamma\) smooth and nonzero and \(A\) a smooth complex \(n\times n\) matrix on a neighbourhood of \(\overline{D^2_{2r}}\times\mathcal U\).

1. If \(W\in L^2(D^2_{2r};\mathbb C^n)\) has compact support in \(D^2_{2r}\) and \(\mathcal P_\rho W=0\) in the sense of distributions, then \(W=0\).
2. For every integer \(j\ge0\) there is \(C_j\), locally uniform in \(\rho\), such that every \(W\in H^{j+1}(\mathbb R^2;\mathbb C^n)\) with \(\operatorname{supp}W\subset\overline{D^2_r}\) satisfies
\[
\begin{aligned}&\|W\|_{H^{j+1}}\\&\quad\le C_j\|\mathcal P_\rho W\|_{H^j}.\end{aligned}\tag{3.1}
\]
3. Let \(f\) be smooth on a neighbourhood of \(\overline{D^2_{2r}}\times\mathcal U\). If \(\mathcal P_\rho W=f(\cdot,\rho)\) has a solution \(W\in L^2\) with support in \(\overline{D^2_r}\) for a dense set of \(\rho\), then it has one for every \(\rho\). These solutions are unique and form a smooth function of \((y,\rho)\).

The same holds for matrix-valued unknowns, whose entries are regarded as a vector.

*Proof.* Note that \(\mathcal P_\rho W=0\) means \(\partial_{\bar z}W=-(2\gamma)^{-1}AW\), and \(\mathcal P_\rho W=f\) means \(\partial_{\bar z}W=-(2\gamma)^{-1}AW+(2\gamma)^{-1}f\), at fixed \(\rho\).

(1) By Lemma 1.2, \(W\) is smooth. Let \(O\) be the set of points of \(D^2_{2r}\) near which \(W\) vanishes; it is open, and nonempty because the support of \(W\) is compact. Let \(z\in D^2_{2r}\) be a limit of points of \(O\), and let \(F\) be a frame of \(\partial_{\bar z}F=-(2\gamma)^{-1}AF\) on a disk \(D\ni z\) (Lemma 2.1). Then \(\partial_{\bar z}(F^{-1}W)=0\) on \(D\), so \(F^{-1}W\) is holomorphic, and it vanishes on the open set \(O\cap D\), which is nonempty. By the identity theorem \(F^{-1}W=0\) on \(D\), so \(z\in O\). Thus \(O\) is open and closed in the connected disk, and \(W=0\).

(2) Extend \(W\) by zero to \(\mathbb R^2\), and cut \(A\) off outside a neighbourhood of \(\overline{D^2_r}\); this changes nothing on the support of \(W\). The Fourier transform of \(\gamma(\partial_{y_1}+i\partial_{y_2})W\) is \(i\gamma(\xi_1+i\xi_2)\widehat W\), of modulus \(|\gamma||\xi||\widehat W|\), and \((1+|\xi|^2)^{j+1}\) is \((1+|\xi|^2)^j+(1+|\xi|^2)^j|\xi|^2\); so
\[
\begin{aligned}&\|W\|_{H^{j+1}}\\&\quad\le\|W\|_{H^j}\\&\qquad+|\gamma|^{-1}\|\gamma(\partial_{y_1}+i\partial_{y_2})W\|_{H^j}\\&\quad\le\|W\|_{H^j}\\&\qquad+|\gamma|^{-1}\bigl(\|\mathcal P_\rho W\|_{H^j}+\|AW\|_{H^j}\bigr).\end{aligned}
\]
By the product rule \(\|AW\|_{H^j}\le C\|W\|_{H^j}\), and \(\|W\|_{H^j}\le\varepsilon\|W\|_{H^{j+1}}+C_\varepsilon\|W\|_{L^2}\), because \((1+|\xi|^2)^j\le\varepsilon^2(1+|\xi|^2)^{j+1}+C_\varepsilon^2\). Absorbing,
\[
\begin{aligned}&\|W\|_{H^{j+1}}\le C\bigl(\|\mathcal P_\rho W\|_{H^j}\\&\qquad+\|W\|_{L^2}\bigr).\end{aligned}\tag{3.2}
\]
If (3.1) failed at a fixed \(\rho\), there would be \(W_\nu\) supported in \(\overline{D^2_r}\) with \(\|W_\nu\|_{H^{j+1}}=1\) and \(\|\mathcal P_\rho W_\nu\|_{H^j}\to0\). By (I2) a subsequence converges in \(L^2\) to some \(W\), supported in \(\overline{D^2_r}\), with \(\mathcal P_\rho W=0\) in the sense of distributions. By (1), \(W=0\), and then (3.2) contradicts \(\|W_\nu\|_{H^{j+1}}=1\). So (3.1) holds at each \(\rho_0\). For \(\rho\) near \(\rho_0\), \(\|(\mathcal P_\rho-\mathcal P_{\rho_0})W\|_{H^j}\le\eta(\rho)\|W\|_{H^{j+1}}\) with \(\eta(\rho)\to0\), since the coefficients depend smoothly on \(\rho\); absorbing this term gives (3.1) near \(\rho_0\) with twice the constant.

(3) Let \(X_j\) be the closed subspace of \(H^{j+1}(\mathbb R^2;\mathbb C^n)\) of the functions with support in \(\overline{D^2_r}\), and \(Z_j=H^j(\mathbb R^2;\mathbb C^n)\), with their Hermitian inner products. The map \(\rho\mapsto\mathcal P_\rho\in\mathcal L(X_j,Z_j)\) is \(C^\infty\) in operator norm, because its \(\rho\)-derivatives are differential operators of order at most one with coefficients smooth in \(\rho\). By (3.1), \((\mathcal P_\rho^*\mathcal P_\rho W,W)=\|\mathcal P_\rho W\|^2\ge C_j^{-2}\|W\|^2\), where \(\mathcal P_\rho^*\) is the Hilbert space adjoint; so the self-adjoint operator \(\mathcal P_\rho^*\mathcal P_\rho\) on \(X_j\) is injective with closed range, its range is dense because its orthogonal complement is its kernel, and it is invertible. Thus
\[
T_{\rho,j}=(\mathcal P_\rho^*\mathcal P_\rho)^{-1}\mathcal P_\rho^*:Z_j\to X_j
\]
is a bounded left inverse of \(\mathcal P_\rho\), and \(\rho\mapsto T_{\rho,j}\) is \(C^\infty\) in operator norm, as adjoints and inverses of bounded invertible operators depend smoothly on the operator. An \(L^2\) solution of \(\mathcal P_\rho W=f(\cdot,\rho)\) supported in \(\overline{D^2_r}\) is smooth by Lemma 1.2, hence lies in every \(X_j\), and equals \(T_{\rho,j}f(\cdot,\rho)\). Put \(W_j(\rho)=T_{\rho,j}f(\cdot,\rho)\), a \(C^\infty\) map into \(X_j\). The residual \(\mathcal P_\rho W_j(\rho)-f(\cdot,\rho)\) is continuous in \(\rho\) with values in \(Z_j\) and vanishes on a dense set, hence everywhere: a supported solution exists for every \(\rho\). It is unique by (1), so it does not depend on \(j\). As \(\rho\mapsto W(\rho)\) is \(C^\infty\) into every \(H^{j+1}\), (I1) shows that all mixed derivatives in \((y,\rho)\) exist and are continuous. \(\square\)

## 4. Exercises

**4.1.** Show that \(\mathcal T\) applied to the indicator function of the unit disk is \(\bar z\) for \(|z|\le1\) and \(1/z\) for \(|z|\ge1\), and check Lemma 1.1(1) for it.

**4.2.** Let \(\theta=\alpha+i\beta\) with \(|\alpha|=|\beta|=\rho_0>0\) and \(\alpha\perp\beta\), and coordinates \(y_1,y_2\) along \(\alpha/\rho_0\) and \(\beta/\rho_0\). Show that \(D_\theta=\rho_0(\partial_{y_1}+i\partial_{y_2})=2\rho_0\partial_{\bar z}\).

**4.3.** For \(n=1\) and a smooth scalar \(a\) on a neighbourhood of \(\overline{D^2_R}\), show that \(V=\exp(\mathcal T(\chi a))\), with \(\chi\in C^\infty_c\) equal to one near \(\overline{D^2_R}\), is a frame of \(\partial_{\bar z}V=aV\) on \(D^2_R\). Why does this argument not work for matrices?

**4.4.** Show that Lemma 3.1(1) fails without the support condition: find a nonzero \(W\) on \(D^2_{2r}\) with \((\partial_{y_1}+i\partial_{y_2})W=0\).

**4.5.** In the proof of Lemma 3.1(3), why is the left inverse \(T_{\rho,j}\) used instead of an inverse of \(\mathcal P_\rho\)?

## 5. Solutions

**4.1.** For \(|z|>1\), \(w\mapsto(z-w)^{-1}\) is holomorphic near the closed unit disk, and by the mean value property its average over the disk is \(z^{-1}\); so \(\mathcal T\mathbf 1(z)=1/z\), also for \(|z|=1\) by continuity (Lemma 1.1(2)). Let \(u=\bar z\) for \(|z|\le1\) and \(u=1/z\) for \(|z|\ge1\). It is continuous, as \(\bar z=1/z\) on the circle, and the divergence theorem on the disk and on its complement, whose boundary terms cancel by continuity, gives \(\partial_{\bar z}u=\mathbf 1\) in the sense of distributions. So \(\mathcal T\mathbf 1-u\) is continuous with \(\partial_{\bar z}(\mathcal T\mathbf 1-u)=0\), hence entire by Corollary 1.3, and it tends to zero at infinity; by Liouville's theorem it is zero. Thus \(\mathcal T\mathbf 1(z)=\bar z\) for \(|z|\le1\), and \(|\mathcal T\mathbf 1|\le1\le2\), as Lemma 1.1(1) with \(\delta=1\) requires.

**4.2.** \(\theta\cdot\nabla=\alpha\cdot\nabla+i\beta\cdot\nabla=\rho_0\partial_{y_1}+i\rho_0\partial_{y_2}\), and \(\partial_{y_1}+i\partial_{y_2}=2\partial_{\bar z}\).

**4.3.** \(\mathcal T(\chi a)\) is smooth, as in the proof of Lemma 2.3, and \(\partial_{\bar z}\exp(\mathcal T(\chi a))=\exp(\mathcal T(\chi a))\,\partial_{\bar z}\mathcal T(\chi a)\), which is \(aV\) on \(D^2_R\) by Lemma 1.1(3); \(V\) never vanishes. For matrices, \(\partial_{\bar z}e^{M(z)}\ne(\partial_{\bar z}M)e^{M(z)}\) unless \(M\) commutes with its derivative, so the exponential does not solve the equation.

**4.4.** Any holomorphic function, for example \(W=1\) or \(W=z\).

**4.5.** \(\mathcal P_\rho\) is injective on \(X_j\) but need not be surjective onto \(Z_j\): for most right sides there is no solution supported in \(\overline{D^2_r}\). The left inverse exists without surjectivity, and its smoothness in \(\rho\) is what transfers smoothness to the solutions on the set of parameters where they exist.

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
- [Forstnerič 2009] F. Forstnerič, *Oka manifolds*, C. R. Math. Acad. Sci. Paris 347 (2009), no. 17–18, 1017–1020. https://arxiv.org/abs/0906.2421
