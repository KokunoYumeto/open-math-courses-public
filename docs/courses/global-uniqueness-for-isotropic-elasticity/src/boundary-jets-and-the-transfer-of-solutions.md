# Boundary jets and the transfer of solutions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two pairs of moduli with the same displacement-to-traction map, as in The displacement-to-traction map, cannot differ to any finite order at the boundary. This lesson uses that fact, quoted from the literature, to extend both pairs to all of \(\mathbb R^3\) so that they coincide outside \(\Omega\). Then every elastic displacement for the first pair near \(\overline\Omega\) has a displacement for the second pair that agrees with it outside \(\Omega\): the two are glued along \(\partial\Omega\), where their boundary values and their tractions agree [OpenAI-EL, Section 2]. The difference of the two is supported in \(\overline\Omega\), and this is the only way in which equality of the boundary maps enters the rest of the proof.

- Boundary determination (Section 1).
- Gluing functions with equal jets (Section 2).
- A common extension of the moduli (Section 3).
- Interior regularity and the transfer of solutions (Section 4).

We keep the notation of the previous lesson. The divergence theorem for a bounded domain with smooth boundary is used as in the core course [Vector Calculus](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B60) (CLP-4, [Theorem 4.2.2](https://personal.math.ubc.ca/~CLP/CLP4/clp_4_vc_text.pdf)). Throughout, the two pairs \((\lambda_j,\mu_j)\), \(j=1,2\), satisfy the hypotheses of Theorem 4.1 of the previous lesson, and \(\Lambda_{\lambda_1,\mu_1}=\Lambda_{\lambda_2,\mu_2}\).

## 1. Boundary determination

For \(f\in C^\infty(\overline\Omega)\) and a point \(y\in\partial\Omega\), the derivative \(\partial^\alpha f(y)\) is the limit of \(\partial^\alpha f(x)\) as \(x\to y\) in \(\Omega\); it agrees with the derivative of every smooth function on \(\mathbb R^3\) that restricts to \(f\).

**Hypothesis (BD)** (boundary determination; [Tan–Liu 2023, Theorem 1.2]). Let \(\lambda_j,\mu_j\in C^\infty(\overline\Omega)\), \(j=1,2\), be real with \(\mu_j>0\) and \(\lambda_j+\mu_j\ge0\) on \(\overline\Omega\). If \(\Lambda_{\lambda_1,\mu_1}=\Lambda_{\lambda_2,\mu_2}\), then \(\partial^\alpha\lambda_1=\partial^\alpha\lambda_2\) and \(\partial^\alpha\mu_1=\partial^\alpha\mu_2\) on \(\partial\Omega\) for every multi-index \(\alpha\).

Tan and Liu prove this on a compact Riemannian manifold with smooth boundary, for the map that sends smooth boundary values \(v\) to the traction \(\lambda(\operatorname{div}u)n+\mu(\nabla u+(\nabla u)^{\mathsf T})n=\sigma(u)n\) of the solution \(u\) with these boundary values, by computing its full symbol as a pseudodifferential operator on the boundary. For \(\Omega\subset\mathbb R^3\) with the Euclidean metric this is our map: the solution with smooth boundary values is smooth up to the boundary, by boundary regularity for the Lamé system (part of the setting of [Tan–Liu 2023], not proved in this course), and then the divergence theorem identifies the traction with the functional of Definition 3.1 of the previous lesson. Under the conditions of Theorem 4.1 we have \(\lambda_j+\mu_j>\mu_j/3>0\), so the hypothesis applies. The determination of the full Taylor series of the moduli at the boundary of a Euclidean domain is due to Nakamura and Uhlmann (see the introduction of [Tan–Liu 2023]).

## 2. Gluing functions with equal jets

**Lemma 2.1.** Let \(F,G_1,\ldots,G_n\) be continuous on an open set \(U\subset\mathbb R^n\) with \(\int F\,\partial_i\varphi\,dx=-\int G_i\varphi\,dx\) for all \(\varphi\in C^\infty_c(U)\) and all \(i\). Then \(F\in C^1(U)\) and \(\partial_iF=G_i\).

*Proof.* Let \(\rho_\varepsilon\) be a standard mollifier and \(F_\varepsilon=F*\rho_\varepsilon\), defined on the points of \(U\) at distance more than \(\varepsilon\) from the complement. Applying the hypothesis to \(\varphi=\rho_\varepsilon(x-\cdot)\) gives \(\partial_iF_\varepsilon=G_i*\rho_\varepsilon\). As \(\varepsilon\to0\), \(F_\varepsilon\to F\) and \(G_i*\rho_\varepsilon\to G_i\) uniformly on compact subsets, by uniform continuity. Passing to the limit in
\[
\begin{aligned}&F_\varepsilon(x+te_i)-F_\varepsilon(x)\\&\quad=\int_0^t\partial_iF_\varepsilon(x+se_i)\,ds\end{aligned}
\]
gives \(F(x+te_i)-F(x)=\int_0^tG_i(x+se_i)\,ds\) for small \(t\). So \(\partial_iF=G_i\), and continuous partial derivatives make \(F\) of class \(C^1\). \(\square\)

**Lemma 2.2** (gluing). Let \(H\in C^\infty(\mathbb R^3)\) have \(\partial^\alpha H=0\) on \(\partial\Omega\) for every \(\alpha\), and let \(\tilde h=H\) on \(\overline\Omega\) and \(\tilde h=0\) on \(\mathbb R^3\setminus\overline\Omega\). Then \(\tilde h\in C^\infty(\mathbb R^3)\), with \(\partial^\alpha\tilde h=\partial^\alpha H\) on \(\overline\Omega\) and \(\partial^\alpha\tilde h=0\) outside.

*Proof.* For a multi-index \(\alpha\), let \(g_\alpha=\partial^\alpha H\) on \(\overline\Omega\) and \(g_\alpha=0\) outside. It is continuous: on \(\partial\Omega\) the values from inside tend to \(\partial^\alpha H=0\). For \(\varphi\in C^\infty_c(\mathbb R^3)\), the divergence theorem for the field \(g_\alpha\varphi e_i\) on \(\Omega\) gives
\[
\begin{aligned}\int_\Omega\partial^\alpha H\,\partial_i\varphi\,dx&=\int_{\partial\Omega}\partial^\alpha H\,\varphi\,n_i\,dS\\&\quad-\int_\Omega\partial_i\partial^\alpha H\,\varphi\,dx ,\end{aligned}
\]
and the boundary integral vanishes. So \(\int g_\alpha\partial_i\varphi=-\int g_{\alpha+e_i}\varphi\). By Lemma 2.1 and induction on \(|\alpha|\), every \(g_\alpha\) is \(C^1\) with \(\partial_ig_\alpha=g_{\alpha+e_i}\); as \(g_0=\tilde h\), \(\tilde h\) is \(C^\infty\). \(\square\)

## 3. A common extension of the moduli

**Lemma 3.1** (common exterior extension; [OpenAI-EL, Lemma 2.1]). The two pairs have real \(C^\infty\) extensions \(\lambda_j,\mu_j\) to \(\mathbb R^3\) such that \(\mu_j>0\) and \(3\lambda_j+2\mu_j>0\) on \(\mathbb R^3\), \(\lambda_1=\lambda_2\) and \(\mu_1=\mu_2\) on \(\mathbb R^3\setminus\Omega\), and both pairs equal one constant pair outside a ball.

*Proof.* The set \(\mathcal A\) of the pairs \((\lambda,\mu)\in\mathbb R^2\) with \(\mu>0\) and \(3\lambda+2\mu>0\) is an intersection of two open half-planes, so it is open and convex; it contains \((0,1)\).

*The first pair.* Let \(\hat\lambda_1,\hat\mu_1\in C^\infty(\mathbb R^3)\) restrict to \(\lambda_1,\mu_1\). The set \(V=\{x:(\hat\lambda_1(x),\hat\mu_1(x))\in\mathcal A\}\) is open and contains the compact set \(\overline\Omega\). Choose \(\chi\in C^\infty_c(V)\) with \(0\le\chi\le1\) and \(\chi=1\) on a neighbourhood of \(\overline\Omega\), and put \((\tilde\lambda_1,\tilde\mu_1)=\chi(\hat\lambda_1,\hat\mu_1)+(1-\chi)(0,1)\). At each point this is a convex combination of points of \(\mathcal A\), or equals \((0,1)\) where \(\chi=0\); so it lies in \(\mathcal A\). It is smooth, equals \((\lambda_1,\mu_1)\) on \(\overline\Omega\), and equals \((0,1)\) outside the compact set \(\operatorname{supp}\chi\).

*The second pair.* Let \(\hat\lambda_2\in C^\infty(\mathbb R^3)\) restrict to \(\lambda_2\), and put \(H=\hat\lambda_2-\tilde\lambda_1\). Near \(\overline\Omega\), \(\tilde\lambda_1=\hat\lambda_1\), so on \(\partial\Omega\), \(\partial^\alpha H=\partial^\alpha\lambda_2-\partial^\alpha\lambda_1=0\) for every \(\alpha\) by Hypothesis (BD). With \(\tilde h\) from Lemma 2.2, \(\tilde\lambda_2=\tilde\lambda_1+\tilde h\) is smooth, equals \(\lambda_2\) on \(\overline\Omega\) and \(\tilde\lambda_1\) outside. The same construction gives \(\tilde\mu_2\). The pair \((\tilde\lambda_2,\tilde\mu_2)\) lies in \(\mathcal A\) on \(\overline\Omega\) by assumption and outside \(\overline\Omega\) because it equals the first extension there. \(\square\)

From now on \(\lambda_j,\mu_j\) denote these extensions, \(L_j\) the Lamé operator of the \(j\)-th pair on \(\mathbb R^3\), and we fix \(r>0\) such that \(\overline\Omega\subset B_r\) and both extensions are constant outside \(B_r\). Here \(B_R\) is the open ball of radius \(R\) about the origin.

## 4. Interior regularity and the transfer of solutions

The Lamé operator is elliptic: its principal symbol at \(\xi\in\mathbb R^3\) is \(v\mapsto-\bigl(\mu|\xi|^2v+(\lambda+\mu)(\xi\cdot v)\xi\bigr)\), with the eigenvalue \(-\mu|\xi|^2\) on vectors orthogonal to \(\xi\) and \(-(\lambda+2\mu)|\xi|^2\) on \(\xi\), and \(\lambda+2\mu>0\) under (1.2) of the previous lesson. We use interior regularity for elliptic systems in the following form.

**Hypothesis (ER)** (interior elliptic regularity; [Dyatlov, Theorem 15.1, Remark 15.2 and Proposition 15.6]). Let \(U\subset\mathbb R^n\) be open and \(P=\sum_{|\beta|\le2}A_\beta(x)\partial^\beta\) with \(A_\beta\in C^\infty(U;\mathbb C^{N\times N})\), where the principal symbol \(\sum_{|\beta|=2}A_\beta(x)\xi^\beta\) is invertible for all \(x\in U\) and \(\xi\in\mathbb R^n\setminus\{0\}\).

1. If \(z\in L^2_{\mathrm{loc}}(U;\mathbb C^N)\) and the distribution \(Pz\) belongs to \(L^2_{\mathrm{loc}}\), then \(z\in H^2_{\mathrm{loc}}(U)\). If \(Pz\in C^\infty(U)\), then \(z\in C^\infty(U)\).
2. Let \(P_\kappa\), \(\kappa\in K\) with \(K\) compact, be such operators on the ball \(B(0,2)\subset\mathbb R^n\) whose coefficients, with all their derivatives in \(y\), are continuous in \((y,\kappa)\) on \(\overline{B(0,2)}\times K\). Then there is \(C\) such that \(\|z\|_{H^2(B(0,1))}\) is at most \(C\) times \(\|z\|_{L^2(B(0,2))}+\|P_\kappa z\|_{L^2(B(0,2))}\) for every \(\kappa\in K\) and every \(z\in L^2(B(0,2))\) with \(P_\kappa z\in L^2(B(0,2))\).

Part 1 is the cited regularity theorem for operators on vector bundles. Part 2 is the cited local elliptic estimate together with the uniformity of its constant over a compact smooth family of operators, which follows by carrying the coefficients through the construction of the parametrix; it is used only in the next lesson.

**Proposition 4.1** (transfer of physical solutions; [OpenAI-EL, Proposition 2.2]). Let \(B\) be an open ball containing \(\overline{B_r}\). Every \(u_1\in C^\infty(B;\mathbb C^3)\) with \(L_1u_1=0\) on \(B\) has a counterpart \(u_2\in C^\infty(B;\mathbb C^3)\) with \(L_2u_2=0\) on \(B\) and \(u_2=u_1\) on \(B\setminus\overline\Omega\). In particular \(u_2-u_1\) and \(\operatorname{div}u_2-\operatorname{div}u_1\) are smooth with support in \(\overline\Omega\).

*Proof.* The operators have real coefficients, so we may treat the real and imaginary parts of \(u_1\) separately and assume \(u_1\) real. Write \(B_j^D\) for the form (2.1) of the previous lesson for the \(j\)-th pair on a region \(D\).

*The interior solution.* The restriction of \(u_1\) to \(\Omega\) lies in \(H^1(\Omega;\mathbb R^3)\), and by (2.2) of the previous lesson it is a weak solution of \(L_1u=0\) in \(\Omega\). With \(f=[u_1|_\Omega]\in\mathcal T\), it is therefore the solution \(u_f\) of the Dirichlet problem for the first pair. Let \(v\) be the weak solution of \(L_2v=0\) in \(\Omega\) with \(v-u_1\in H^1_0(\Omega)\), given by Proposition 2.3 of the previous lesson.

*Gluing.* The field \(w=v-u_1\in H^1_0(\Omega)\) is an \(H^1\) limit of fields in \(C^\infty_c(\Omega)\); extending these by zero shows that the extension \(\tilde w\) of \(w\) by zero lies in \(H^1(\mathbb R^3)\), with derivatives the extensions of those of \(w\). Put \(u_2=u_1+\tilde w\) on \(B\). Then \(u_2\in H^1_{\mathrm{loc}}(B)\), \(u_2=v\) in \(\Omega\) and \(u_2=u_1\) on \(B\setminus\overline\Omega\).

*The weak equation.* Let \(\varphi\in C^\infty_c(B;\mathbb R^3)\). The boundary \(\partial\Omega\) has measure zero, and the two pairs coincide on \(B\setminus\overline\Omega\), where \(u_2=u_1\). By the definition of \(\Lambda\) and the equality of the two maps,
\[
\begin{aligned}&B_2^B(u_2,\varphi)=B_2^\Omega(v,\varphi)+B_1^{B\setminus\overline\Omega}(u_1,\varphi)\\&\quad=\langle\Lambda_{\lambda_2,\mu_2}f,[\varphi|_\Omega]\rangle+B_1^{B\setminus\overline\Omega}(u_1,\varphi)\\&\quad=\langle\Lambda_{\lambda_1,\mu_1}f,[\varphi|_\Omega]\rangle+B_1^{B\setminus\overline\Omega}(u_1,\varphi)\\&\quad=B_1^\Omega(u_1,\varphi)+B_1^{B\setminus\overline\Omega}(u_1,\varphi)\\&\quad=B_1^B(u_1,\varphi),\end{aligned}
\]
which is \(-\int_B(L_1u_1)\cdot\varphi\,dx=0\) by (2.2) of the previous lesson on \(B\). So \(L_2u_2=0\) in the sense of distributions on \(B\), because \(\langle L_2u_2,\varphi\rangle=-B_2^B(u_2,\varphi)\) for \(u_2\in H^1_{\mathrm{loc}}\).

*Smoothness.* \(L_2\) has smooth coefficients on \(B\) and invertible principal symbol, and \(L_2u_2=0\). By Hypothesis (ER)(1), \(u_2\in C^\infty(B)\). Then \(u_2-u_1=\tilde w\) is smooth and zero on \(B\setminus\overline\Omega\), so it and all its derivatives, in particular its divergence, vanish there; their supports lie in \(\overline\Omega\subset B_r\). \(\square\)

## 5. Exercises

**5.1.** Show that \(\mathcal A=\{(\lambda,\mu):\mu>0,\ 3\lambda+2\mu>0\}\) is convex, and that it does not contain \((-1,1)\).

**5.2.** Compute the principal symbol of the Lamé operator with constant moduli, and its eigenvalues and eigenvectors.

**5.3.** In one dimension, let \(H(x)=x\) and glue \(H\) on \((-\infty,0]\) with \(0\) on \((0,\infty)\). Show that the glued function is continuous but not differentiable at \(0\). Which hypothesis of Lemma 2.2 fails?

**5.4.** Let \(u_1(x)=Mx+b\) with \(M\) antisymmetric. Show that \(L_1u_1=0\), and that the construction in the proof of Proposition 4.1 gives \(u_2=u_1\).

**5.5.** The proof of Proposition 4.1 uses that \(\partial\Omega\) has Lebesgue measure zero. Prove this from the definition of a \(C^\infty\) boundary in the previous lesson.

## 6. Solutions

**5.1.** If \((\lambda,\mu)\) and \((\lambda',\mu')\) satisfy the two strict linear inequalities, so does every convex combination, because the inequalities are linear. For \((-1,1)\), \(3\lambda+2\mu=-1<0\).

**5.2.** For \(u=e^{ix\cdot\xi}v\), \(Lu=-e^{ix\cdot\xi}\bigl(\mu|\xi|^2v+(\lambda+\mu)(\xi\cdot v)\xi\bigr)\). The vector \(\xi\) is an eigenvector with eigenvalue \(-(\lambda+2\mu)|\xi|^2\), and every \(v\perp\xi\) is an eigenvector with eigenvalue \(-\mu|\xi|^2\).

**5.3.** The glued function is \(x\) for \(x\le0\) and \(0\) for \(x>0\); it is continuous, but its left derivative at \(0\) is \(1\) and its right derivative is \(0\). The first derivative of \(H\) does not vanish at the gluing point.

**5.4.** \(e(u_1)=0\) and \(\operatorname{div}u_1=0\), so \(\sigma(u_1)=0\) for every pair of moduli and \(L_1u_1=0\). As \(u_1\) is a weak solution for the second pair as well, the solution \(v\) of the second Dirichlet problem with \(v-u_1\in H^1_0\) is \(u_1\) itself, so \(\tilde w=0\) and \(u_2=u_1\).

**5.5.** Each point of \(\partial\Omega\) has a neighbourhood in which, after a rotation, \(\partial\Omega\) is the graph \(x_3=g(x_1,x_2)\) of a smooth function. A graph over a bounded set has measure zero: each vertical line meets it in one point, so its measure is zero by Fubini's theorem. Finitely many such neighbourhoods cover the compact set \(\partial\Omega\).

## References

- [OpenAI-EL] OpenAI, *Global uniqueness for the smooth isotropic elasticity inverse problem*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026
- [Tan–Liu 2023] X. Tan, G. Liu, *Determining Lamé coefficients by elastic Dirichlet-to-Neumann map on a Riemannian manifold*, Inverse Problems 39 (2023), no. 9, 095004. https://arxiv.org/abs/2211.06650
- [Dyatlov] S. Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity, and applications to PDEs*, MIT, version of 2 October 2026, Section 15.1. https://math.mit.edu/~dyatlov/18.155/155-notes.pdf
