# Boundary adjoints, complete composition and distributional action

These connected components retain AN03-U032, *Totally characteristic operators on the half space*, Sections 2–5, Section 6 through Example 6.7, and Sections 7–13. Original author: Claude Opus 5.5 (Anthropic), September 2026; editorial additions: Codex, September 2026. Both were dedicated to the public domain (CC0). Current prerequisite connections and proof clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, also CC0. The selected components retain every mathematical display, the full scalar and finite-matrix hypotheses, and all five original solved exercises.

The approved mathematical antecedent is Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid. Complete proofs are supplied in the components and the exact earlier programme proofs. The earlier linked components retain their individual licences.

The four components, in proof order, are [Boundary tests, lacunary symbols and all normal jets](boundary-tests-and-lacunary-symbols.md), [Resolved corner kernels and their exact inverse](resolved-corner-kernels.md), [Boundary adjoints, complete composition and distributional action](boundary-adjoints-composition-and-distributions.md), [Boundary operator bounds, conormal action and the residual obstruction](boundary-bounds-and-conormal-action.md). Original section and equation numbers are retained across them. Sections 6.8 (polyhomogeneous corner characterization) and 14 (arbitrary positive-order Sobolev loss) are separate unadopted obligations; the theorems below do not substitute for those results or for the global compressed wave-front calculus.

Use the exact [test and symbol calculus](boundary-tests-and-lacunary-symbols.md) and [resolved kernel theorem](resolved-corner-kernels.md). All adjoints use the Hilbert convention, and every transpose of a matrix reverses its source and target. The distribution actions retain the actual supported representatives and the separate restriction quotient.

## 7. Adjoints

The adjoint of \(T_a\) with respect to \((u,v)=\int u\overline v\) is again an operator of the class. We first compute it for strongly lacunary residual symbols, where the transposed kernel can be read off from Theorem 6.2. Then we extend the formula by an adjoint transform defined on all of \(S^m_+\).

### The adjoint of a strongly lacunary residual operator

**Proposition 7.1** (A residual adjoint formula). Let \(a\in S^{-\infty}_{\mathrm{la}}\) be strongly lacunary, and let \(\chi\in C_0^\infty((0,\infty))\) equal 1 on \((\tfrac12,2)\). There is exactly one \(b\in S^{-\infty}_{\mathrm{la}}\) with
\[
(T_au,v)=(u,T_bv)\qquad(u,v\in\mathcal S(\mathbb R^n)),
\tag{7.1}
\]
and for \(x_n>0\), with the inner integral taken first,
\[
b(x,\xi)=(2\pi)^{-n}\int\!\Big(\int e^{-i\langle y,\eta\rangle}\,\overline a\big(x'-y',\,x_n(1-y_n),\,\xi'-\eta',\,(1-y_n)(\xi_n-\eta_n)\big)\chi(1-y_n)\,d\eta\Big)dy
\tag{7.2}
\]
\[
=\Big[e^{i\langle D_y,D_\eta\rangle}\big(\overline a(y',x_ny_n,\eta',y_n\eta_n)\chi(y_n)\big)\Big]_{y=(x',1),\ \eta=\xi}.
\tag{7.3}
\]

**Proof.** *Existence and uniqueness.* The transposed kernel \(K^*(x,y)=\overline{K_a(y,x)}\) is locally integrable and supported in \(Q\), and its resolved form is \(F^*(x',y',t,r)=\overline{F(y',x',t,-r)}\), which has all the properties in Theorem 6.2(c). By Theorem 6.2(d), \(K^*=K_b\) for a unique \(b\in S^{-\infty}_{\mathrm{la}}\), and Fubini's theorem, justified by the bounds of Theorem 6.2(b), gives (7.1). An operator determines its symbol (by the explicit Fourier-kernel construction in Section 1.2), so \(b\) is unique.

*The formula.* By the inversion formula for kernels in Section 1, for \(x_n>0\), \(b^\flat(x,\xi)=\int e^{-iz\cdot\xi}\,\overline{K_a(x-z,x)}\,dz\), an absolutely convergent integral. Strong lacunarity says that \(A\) vanishes unless \(z_n\in[-1,\tfrac12]\); in \(K_a(y,x)\) the normal argument is \((y_n-x_n)/y_n\), so \(K_a(y,x)=0\) unless \(x_n/y_n\in[\tfrac12,2]\). So we may insert \(\chi((x_n-z_n)/x_n)\), since it equals 1 almost everywhere on the support. Writing \(\overline{K_a(x-z,x)}=(2\pi)^{-n}\int e^{i\langle z,\eta\rangle}\overline{a^\flat(x-z,\eta)}\,d\eta\) and substituting \(\eta\mapsto\xi-\eta\), we get
\[
b^\flat(x,\xi)=(2\pi)^{-n}\int\!\Big(\int e^{-i\langle z,\eta\rangle}\overline a\big(x-z,\xi'-\eta',(x_n-z_n)(\xi_n-\eta_n)\big)\chi\Big(\frac{x_n-z_n}{x_n}\Big)d\eta\Big)dz .
\]
Now \(b(x,\xi)=b^\flat(x,\xi',\xi_n/x_n)\). Substitute \(z_n=x_ny_n\), \(\eta_n\mapsto\eta_n/x_n\), \(z'=y'\): then \((x_n-z_n)(\xi_n/x_n-\eta_n/x_n)=(1-y_n)(\xi_n-\eta_n)\), \(z_n\eta_n\) becomes \(y_n\eta_n\), and \(dz_n\,d\eta_n=dy_n\,d\eta_n\). This is (7.2). Finally, for a function \(c(y,\eta)\) that is a residual symbol, \(e^{i\langle D_y,D_\eta\rangle}c(y,\eta)=(2\pi)^{-n}\iint e^{-i\langle w,\theta\rangle}c(y-w,\eta-\theta)\,d\theta\,dw\) (the complete Fourier multiplier identity O4 in the earlier ordinary calculus proves this formula on Schwartz inputs; bounded compact approximation and the O8 seminorm estimates extend it to residual symbols, with the inner Fourier integral first). With \(c(y,\eta)=\overline a(y',x_ny_n,\eta',y_n\eta_n)\chi(y_n)\), a residual symbol for fixed \(x_n>0\), and \((y,\eta)=((x',1),\xi)\), this is (7.2). \(\square\)

### The adjoint transform

**Lemma 7.2** (The adjoint transform). Let \(\chi\in C_0^\infty((0,\infty))\) equal 1 near 1, with \(\operatorname{supp}\chi\subset(M^{-1},M)\), \(M>1\). For \(a\in S^m_+\) put
\[
L_\chi a(x,\xi)=\Big[e^{i\langle D_y,D_\eta\rangle}c_{x_n}\Big]\big((x',1),\xi\big),\qquad c_{x_n}(y,\eta)=\overline a(y',x_ny_n,\eta',y_n\eta_n)\chi(y_n).
\tag{7.4}
\]

(a) \(L_\chi\) is a continuous conjugate-linear map \(S^m_+\to S^m_{\mathrm{la}}\).

(b) In \(S^m_+\),
\[
L_\chi a\sim\sum_{j\geq0}\frac1{j!}\langle D_y,iD_\eta\rangle^j\,\overline a(y',x_ny_n,\eta',y_n\eta_n)\Big|_{y=(x',1),\,\eta=\xi},
\tag{7.5}
\]
the \(j\)-th term lying in \(S^{m-j}_+\), with the remainder after \(N\) terms in \(S^{m-N}_+\) and controlled by finitely many seminorms of \(a\). For \(x_n>0\) the \(j\)-th term equals \(\frac1{j!}\langle D_y,iD_\eta\rangle^j\overline a(y,\eta',y_n\eta_n)\) at \(y=x\), \(\eta'=\xi'\), \(\eta_n=\xi_n/x_n\).

(c) If \(a\in S^{-\infty}_+\), then \(\operatorname{supp}\mathcal F_n(L_\chi a)(x,\xi',\cdot)\subset[M^{-1}-1,\,M-1]\), and \(T_{L_\chi a}\) has the kernel \(\chi(y_n/x_n)\overline{K_a(y,x)}\) for \(x_n,y_n>0\) (and 0 elsewhere).

**Proof.** (a), (b) On \(\operatorname{supp}\chi\) we have \(M^{-1}\leq y_n\leq M\), hence \((1+|\eta|)/M\leq1+|(\eta',y_n\eta_n)|\leq M(1+|\eta|)\) and \(1+x_ny_n\geq(1+x_n)/M\). A \(y_n\)-derivative of \(\overline a(y',x_ny_n,\eta',y_n\eta_n)\) produces \(x_n\partial_{x_n}\overline a\) (the factor \(x_n\) is absorbed by the decay in \(x_ny_n\)) or \(\eta_n\partial_{\xi_n}\overline a\) (the factor \(\eta_n\) is paid for by the lower order); an \(\eta_n\)-derivative produces \(y_n\partial_{\xi_n}\overline a\). Hence \((1+x_n)^\nu c_{x_n}\) is bounded in the classical class \(S^m(\mathbb R^n_y\times\mathbb R^n_\eta)\), uniformly in \(x_n\geq0\), for every \(\nu\), and so is every \(\partial_{x_n}^kc_{x_n}\) (it has the same form, with \(y_n^k\partial_{x_n}^k\overline a\)).

By the complete ordinary quadratic multiplier estimate O8 and parameter proof in Section 1, \(e^{i\langle D_y,D_\eta\rangle}\) is continuous on \(S^m\), with the expansion \(\sum_{|\alpha|<N}\frac1{\alpha!}\partial_\eta^\alpha D_y^\alpha c\) and remainder in \(S^{m-N}\). The map \(x_n\mapsto c_{x_n}\) is \(C^\infty\) into \(S^m\) (difference quotients converge, by the mean value theorem and the bounds on the next derivative), so \(C(y,\eta;x_n)=e^{i\langle D_y,D_\eta\rangle}c_{x_n}\) is smooth in all variables, with \(|\partial^k_{x_n}\partial^\alpha_\eta\partial^\beta_yC|\leq C(1+|\eta|)^{m-|\alpha|}(1+x_n)^{-\nu}\). Evaluating at \(y=(x',1)\), \(\eta=\xi\) (so \(x'\)-derivatives are \(y'\)-derivatives) gives \(L_\chi a\in S^m_+\), continuously in \(a\).

Since \(\chi=1\) near \(y_n=1\), the expansion terms at \(y_n=1\) are those of (7.5). The \(j\)-th term is in \(S^{m-j}_+\): the operators \(x_n\partial_{x_n}\) and \(\eta_n\partial_{\xi_n}\) produced by \(D_{y_n}\) preserve \(S^m_+\), and each \(\partial_\eta\) lowers the order by one (also when it hits a factor \(\eta_n\), since \([\partial_{\eta_n},\eta_n\partial_{\xi_n}]=\partial_{\xi_n}\)). The second form of the terms follows from \(\overline a(y',x_ny_n,\eta',y_n\eta_n)=\overline a(Y,H',Y_nH_n)\) with \(Y=(y',x_ny_n)\), \(H=(\eta',\eta_n/x_n)\), under which \(D_{y_n}D_{\eta_n}=D_{Y_n}D_{H_n}\).

Lacunarity. First let \(a\in S^{-\infty}_+\). Then \(c_{x_n}\) is a residual symbol and \(L_\chi a\) is given by the integral (7.2) with this \(\chi\). Substitute \(\theta=\xi_n-\eta_n\) in the inner integral: \(L_\chi a(x,\xi',\cdot)\) is the Fourier transform, in \(y_n\), of
\[
G(y_n)=(2\pi)^{-n}\iiint e^{-i\langle y',\eta'\rangle+iy_n\theta}\,\overline a\big(x'-y',x_n(1-y_n),\xi'-\eta',(1-y_n)\theta\big)\chi(1-y_n)\,d\theta\,d\eta'\,dy' .
\]
So \(\mathcal F_n(L_\chi a)(x,\xi',t)=2\pi G(-t)\), which vanishes unless \(1+t\in\operatorname{supp}\chi\), that is \(t\in[M^{-1}-1,M-1]\subset(-1,\infty)\). For general \(a\in S^m_+\), take \(a_k=a\,\psi(\xi/k)\in S^{-\infty}_+\) with \(\psi\in C_0^\infty\) equal to 1 near 0; then \(a_k\to a\) in \(S^{m+1}_+\), so \(L_\chi a_k\to L_\chi a\) in \(S^{m+1}_+\) by (a), and \(L_\chi a\) is lacunary because \(S^{m+1}_{\mathrm{la}}\) is closed.

(c) The support statement was just proved. For the kernel, the computation in the proof of Proposition 7.1 applies to any \(a\in S^{-\infty}_+\) and shows that \((L_\chi a)^\flat(x,\cdot)\) is the transform \(\int e^{-iz\cdot\xi}k(x,x-z)dz\) of \(k(x,y)=\chi(y_n/x_n)\overline{K_a(y,x)}\). \(\square\)

The kernel statement in (c) explains the construction: the cutoff multiplies the transposed kernel by a function of the ratio of the normal variables, and that makes the result lacunary.

### Adjoints of lacunary operators

**Theorem 7.3** (Adjoints).

(a) For every \(a\in S^m_{\mathrm{la}}\) there is exactly one \(a^\dagger\in S^m_{\mathrm{la}}\) with
\[
(T_au,v)=(u,T_{a^\dagger}v)\qquad(u,v\in\mathcal S(\mathbb R^n)).
\tag{7.6}
\]
The map \(a\mapsto a^\dagger\) is conjugate-linear and continuous \(S^m_{\mathrm{la}}\to S^m_{\mathrm{la}}\), \((a^\dagger)^\dagger=a\), and \(a^\dagger-\overline a\in S^{m-1}_+\).

(b) If \(a\) is strongly lacunary and \(\chi\in C_0^\infty((0,\infty))\) equals 1 on \((\tfrac12,2)\), then \(a^\dagger=L_\chi a\); in particular \(a^\dagger\) has the expansion (7.5).

(c) Since \(T_au=0\) on \(\mathbb R^n_-\), (7.6) says \((T_au,v)_{L^2(\mathbb R^n_+)}=(u,T_{a^\dagger}v)_{L^2(\mathbb R^n_+)}\) for \(u,v\in\overline{\mathcal S}(\mathbb R^n_+)\).

**Proof.** (b) For residual \(a\) this is Proposition 7.1. Let \(a\in S^m_{\mathrm{la}}\) be strongly lacunary, and let \(\rho\) be as in Lemma 4.4. Take \(a_k=a\,\psi(\xi/k)\in S^{-\infty}_+\), so that \(a_k\to a\) in \(S^{m+1}_+\) (the error \((1-\psi(\xi/k))a\) has \(S^{m+1}\) seminorms \(O(k^{-1})\)). Then \((a_k)_\rho\in S^{-\infty}_+\) is strongly lacunary, and \((a_k)_\rho\to a_\rho\) in \(S^{m+1}_+\). By the residual case, \((T_{(a_k)_\rho}u,v)=(u,T_{L_\chi(a_k)_\rho}v)\). Let \(k\to\infty\): \(L_\chi(a_k)_\rho\to L_\chi a_\rho\) in \(S^{m+1}_{\mathrm{la}}\) by Lemma 7.2, and Theorem 5.1(a) lets us pass to the limit on both sides. So the formula holds for \(a_\rho\). The difference \(a-a_\rho\) is residual and strongly lacunary (Lemma 4.4(b),(c)), so the formula holds for it too, and \(L_\chi\) is additive and conjugate-linear.

(a) Write \(a=a_\rho+(a-a_\rho)\). The first term is strongly lacunary, so it has the adjoint symbol \(L_\chi a_\rho\) by (b). The second is in \(S^{-\infty}_{\mathrm{la}}\); by Theorem 6.2 its transposed kernel is the kernel of \(T_{b'}\) for some \(b'\in S^{-\infty}_{\mathrm{la}}\), as in the proof of Proposition 7.1. Put \(a^\dagger=L_\chi a_\rho+b'\). Uniqueness follows because \(T_c\) determines \(c^\flat\) (an operator determines its symbol), hence \(c\) on \(x_n>0\), hence \(c\) by continuity. Additivity, conjugate-linearity and \((a^\dagger)^\dagger=a\) follow from uniqueness. Indeed \(T_{\lambda a+\mu b}=\lambda T_a+\mu T_b\) and the inner product is linear in its first argument, so the unique adjoint symbol is \(\overline\lambda a^\dagger+\overline\mu b^\dagger\). For continuity, each step is continuous: \(a\mapsto a_\rho\) and \(a\mapsto a-a_\rho\) by Lemma 4.4, \(L_\chi\) by Lemma 7.2, and the residual adjoint by the explicit formulas of Theorem 6.2 (\(a\mapsto A\mapsto F\mapsto F^*\mapsto A^*\mapsto b'\), each with seminorm bounds). Finally \(L_\chi a_\rho=\overline{a_\rho}+S^{m-1}_+\) by (7.5), and \(\overline{a_\rho}-\overline a\in S^{-\infty}_+\).

(c) is immediate. \(\square\)

## 8. Composition

The composition of two operators of the class is again in the class. Its symbol is the sum of a near part, given by a Gauss transform as in the ordinary calculus, and a residual far part.

**Theorem 8.1** (Composition). Let \(a_j\in S^{m_j}_{\mathrm{la}}\), \(j=1,2\), and let \(\chi\in C_0^\infty((0,\infty))\) equal 1 near 1, with \(\operatorname{supp}\chi\subset(M^{-1},M)\). Put
\[
b_1(x,\xi)=\Big[e^{i\langle D_y,D_\eta\rangle}\big(a_1(x,\eta)\,a_2(y',x_ny_n,\xi',\xi_ny_n)\,\chi(y_n)\big)\Big]_{y=(x',1),\ \eta=\xi},
\tag{8.1}
\]
where the Gauss transform acts in \((y,\eta)\) with \((x,\xi)\) as parameters, and
\[
b_2(x,\xi)=\int e^{-i\langle x'-y',\xi'\rangle-i(1-y_n)\xi_n}A_1(x,x'-y',1-y_n)\,a_2(y',x_ny_n,\xi',\xi_ny_n)\,dy,\quad
A_1(x,z)=\big(1-\chi(1-z_n)\big)(2\pi)^{-n}\!\int e^{iz\cdot\xi}a_1(x,\xi)d\xi,
\tag{8.2}
\]
with the integrand taken to be 0 for \(y_n\leq0\). Then \(b=b_1+b_2\in S^{m_1+m_2}_{\mathrm{la}}\); \(b_2\in S^{-\infty}_+\); the map \((a_1,a_2)\mapsto b\) is continuous and bilinear; \(b\) does not depend on \(\chi\); and
\[
T_{a_1}T_{a_2}=T_b\quad\text{on }\overline{\mathcal S}(\mathbb R^n_+),\qquad
b\sim\sum_\alpha\frac1{\alpha!}\,\partial_\xi^\alpha a_1(x,\xi)\,D_{x'}^{\alpha'}D_s^{\alpha_n}\big[a_2(x',sx_n,\xi',s\xi_n)\big]_{s=1},
\tag{8.3}
\]
the \(\alpha\)-term having order \(m_1+m_2-|\alpha|\). If \(a_1\in S^{-\infty}_{\mathrm{la}}\) and \(a_2\) vanishes for large \(|x|\), then for \(x_n>0\)
\[
b(x,\xi)=(2\pi)^{-n}\iint_{y_n>0}e^{-i\langle x'-y',\xi'-\eta'\rangle-i(1-y_n)(\xi_n-\eta_n)}a_1(x,\eta)\,a_2(y',x_ny_n,\xi',\xi_ny_n)\,dy\,d\eta,
\tag{8.4}
\]
an absolutely convergent integral. Formally, \(b=e^{i\langle D_y,D_\eta\rangle}a_1(x,\eta)a_2(y',x_ny_n,\xi',\xi_ny_n)\) at \(y=(x',1)\), \(\eta=\xi\); the sum (8.1)+(8.2) is the precise meaning of this formula.

*Reference:* [Hörmander III, Theorem 18.3.11] treats composition. The truncation used below needs boundedness and pointwise convergence; its lack of convergence in the full symbol topology is proved in Remark 8.2.

**Proof.** *Step 1: the near part.* Put \(g(y,\xi)=a_2(y',x_ny_n,\xi',\xi_ny_n)\chi(y_n)\), with \(x_n\geq0\) a parameter. On \(\operatorname{supp}\chi\), \(M^{-1}\leq y_n\leq M\), so \(1+|(\xi',y_n\xi_n)|\) is comparable to \(1+|\xi|\). A \(y_n\)-derivative produces \(x_n\partial_{x_n}a_2\) (the factor \(x_n\) is absorbed by the decay of \(a_2\) in \(x_ny_n\)) or \(\xi_n\partial_{\xi_n}a_2\), and \(|\xi_n|(1+|(\xi',y_n\xi_n)|)^{m_2-1}\leq M(1+|(\xi',y_n\xi_n)|)^{m_2}\). A \(\xi\)-derivative lowers the order by one. So \(g\) is a classical symbol of order \(m_2\) in \((y,\xi)\), uniformly in \(x_n\), and so are its \(x_n\)-derivatives. Likewise \((1+x_n)^\nu a_1(x,\eta)\) is a symbol of order \(m_1\) in \((x,\eta)\) for every \(\nu\). We apply the full pre-diagonal estimate O9, including every parameter derivative, identified in Section 1 to the product \((1+x_n)^\nu a_1(x,\eta)\,g(y,\xi)\), with the multiplier acting in \((y,\eta)\) and \(x_n\) a passive parameter. That estimate holds at every \((y,\eta)\); at \(y=(x',1)\), \(\eta=\xi\) it gives
\[
\Big|\partial^\alpha_\xi\partial^\beta_x\Big(b_1-\sum_{|\gamma|<N}\frac1{\gamma!}\partial^\gamma_\eta a_1(x,\xi)D_y^\gamma g\big((x',1),\xi\big)\Big)\Big|\leq C(1+x_n)^{-\nu}(1+|\xi|)^{m_1+m_2-N-|\alpha|},
\]
with \(C\) controlled by finitely many seminorms of \(a_1\) and \(a_2\) (differentiation in \(x\) commutes with the multiplier, and a derivative of the evaluation at \(y=(x',1)\), \(\eta=\xi\) is a sum of derivatives in the two sets of variables, each controlled by the estimate). Since \(\chi=1\) near 1, \(D_y^\gamma g((x',1),\xi)=D^{\gamma'}_{x'}D^{\gamma_n}_s[a_2(x',sx_n,\xi',s\xi_n)]_{s=1}\). So \(b_1\in S^{m_1+m_2}_+\) with the expansion (8.3), continuously in \((a_1,a_2)\).

*Step 2: the far part is residual.* The factor \(1-\chi(1-z_n)\) vanishes near \(z_n=0\). Off \(z=0\) the inverse transform of \(a_1(x,\cdot)\) is smooth, and for \(|z|\) bounded below its derivatives are bounded by \(C_N(1+|z|)^{-N}(1+x_n)^{-N}\) (integrate by parts in \(\xi\)). So \(A_1\) satisfies (6.2). By lacunarity \(A_1=0\) for \(z_n\geq1\), and Taylor's formula at \(z_n=1\) gives
\[
|\partial_x^\alpha\partial_z^\beta A_1(x,z)|\leq C|1-z_n|^N(1+|z|)^{-2N}(1+x_n)^{-N}\qquad(z_n\leq1).
\tag{8.5}
\]
Let \(G(x,y,\xi)\) be the integrand of (8.2) without the exponential. For \(y_n>0\) we have \(\min(1,y_n)(1+|\xi|)\leq1+|\xi'|+y_n|\xi_n|\leq(1+y_n)(1+|\xi|)\). So a derivative of \(a_2(y',x_ny_n,\xi',\xi_ny_n)\) of order \(\gamma\) in \(\xi\) is bounded by \((1+|\xi|)^{m_2-|\gamma|}\) times a factor \((1+x_n)^K(y_n+y_n^{-1})^K\); the powers of \(x_n\) come from \(y_n\)-derivatives falling on the second argument. The factor \(A_1\) absorbs all of this. Near \(y_n=0\) the factor \(y_n^{-K}\) is paid for by \(y_n^N=|1-z_n|^N\) in (8.5). For large \(y_n\) the growth is paid for by the decay in \(z_n=1-y_n\). The powers of \(1+x_n\) are paid for by the decay of \(A_1\) in \(x_n\). Hence \(G\) is smooth across \(y_n=0\), and
\[
|\partial_x^\alpha\partial_y^\beta\partial_\xi^\gamma G|\leq C_N(1+|x'-y'|+|1-y_n|)^{-N}(1+x_n)^{-N}(1+|\xi|)^{m_2-|\gamma|}.
\]
The phase is \(e^{-i\langle x',\xi'\rangle-i\xi_n}e^{i\langle y,\xi\rangle}\), so \(\xi^\kappa b_2=\int e^{-i\langle x'-y',\xi'\rangle-i(1-y_n)\xi_n}(-D_y)^\kappa G\,dy\). Derivatives of \(b_2\) in \(x\) and \(\xi\) bring factors \(\xi'\) (treated the same way) or \(x'-y'\), \(1-y_n\) (absorbed by the decay of \(G\)). So \(b_2\in S^{-\infty}_+\), continuously in \((a_1,a_2)\).

*Step 3: the product formula for residual \(a_1\) and compactly supported \(a_2\).* Let \(a_1\in S^{-\infty}_{\mathrm{la}}\), \(a_2\in S^{m_2}_{\mathrm{la}}\) with \(a_2=0\) for \(|x|\geq R\), and \(u\in\mathcal S\). Then \(w=T_{a_2}u\) is a bounded function with compact support, zero for \(x_n<0\). For \(x_n>0\) the kernel \(K_{a_1}(x,\cdot)\) is a Schwartz function vanishing for \(y_n\leq0\) (Theorem 6.2), so for every Schwartz extension \(W\) of \(w|_{\mathbb R^n_+}\), \(T_{a_1}W(x)=\int K_{a_1}(x,y)w(y)dy=(2\pi)^{-n}\int e^{i\langle x,\eta\rangle}a_1^\flat(x,\eta)\widehat w(\eta)d\eta\). Here \(\widehat w(\eta)=(2\pi)^{-n}\iint e^{i\langle y,\xi-\eta\rangle}a_2^\flat(y,\xi)\widehat u(\xi)\,d\xi\,dy\), absolutely convergent. Combining the integrals (absolutely convergent for fixed \(x\)),
\[
T_{a_1}T_{a_2}u(x)=(2\pi)^{-n}\int e^{i\langle x,\xi\rangle}c(x,\xi)\widehat u(\xi)d\xi,\qquad c(x,\xi)=(2\pi)^{-n}\iint e^{-i\langle x-y,\xi-\eta\rangle}a_1^\flat(x,\eta)a_2^\flat(y,\xi)\,dy\,d\eta .
\]
Put \(b(x,\xi)=c(x,\xi',\xi_n/x_n)\), so \(c=b^\flat\). The substitutions \(\xi_n\mapsto\xi_n/x_n\), \(\eta_n\mapsto\eta_n/x_n\), \(y_n\mapsto x_ny_n\) turn \(c\) into (8.4); the double integral converges absolutely because \(a_1\) is residual and \(y\) stays in a compact set. Now insert \(1=\chi(y_n)+(1-\chi(y_n))\). The first part is the Gauss transform (8.1) of a residual symbol with compact \(y\)-support, written as an absolutely convergent integral (as in Proposition 7.1). In the second part, integrate in \(\eta\) first: \((2\pi)^{-n}\int e^{i\langle x'-y',\eta'\rangle+i(1-y_n)\eta_n}a_1(x,\eta)d\eta\), multiplied by \(1-\chi(y_n)=1-\chi(1-z_n)\) with \(z_n=1-y_n\), is \(A_1(x,x'-y',1-y_n)\); what remains is (8.2). So \(T_{a_1}T_{a_2}=T_{b_1+b_2}\) on \(\mathcal S\), in \(\mathbb R^n_+\).

*Step 4: general \(a_2\).* Let \(\vartheta\in C_0^\infty(\mathbb R^n)\) equal 1 near 0 and \(a_{2,k}=\vartheta(x/k)a_2\). These are lacunary, bounded in \(S^{m_2}_+\), and converge to \(a_2\) locally uniformly with all derivatives. Since functions of \(x\) stand on the left, \(T_{a_{2,k}}u=\vartheta(\cdot/k)T_{a_2}u\to T_{a_2}u\) in \(\overline{\mathcal S}(\mathbb R^n_+)\); so \(T_{a_1}T_{a_{2,k}}u\to T_{a_1}T_{a_2}u\) by Theorem 5.1. On the other side, \(b_{2,k}\to b_2\) pointwise by dominated convergence. The near parts \(b_{1,k}\) are Gauss transforms of symbols in \((y,\eta)\) that stay bounded in \(S^{m_1}\) and converge locally smoothly; by the complete ordinary quadratic multiplier estimate O8 and parameter proof in Section 1, the transforms converge locally uniformly with all derivatives, so \(b_{1,k}\to b_1\) pointwise. All \(b_k=b_{1,k}+b_{2,k}\) are bounded in \(S^{m_1+m_2}_+\) (here \(m_1\) is any real number, since \(a_1\) is residual), so \(T_{b_k}u(x)\to T_bu(x)\) for each \(x\in\mathbb R^n_+\) by dominated convergence. Hence \(T_{a_1}T_{a_2}u=T_bu\).

*Step 5: general \(a_1\).* Write \(a_1=(a_1)_\rho+r\) with \(r=a_1-(a_1)_\rho\in S^{-\infty}_{\mathrm{la}}\) (Lemma 4.4); Step 4 applies to \(r\). Let \(a_{1,k}=a_1\psi(\xi/k)\in S^{-\infty}_+\), \(\psi\in C_0^\infty\) equal to 1 near 0. Then \((a_{1,k})_\rho\in S^{-\infty}_{\mathrm{la}}\) and \((a_{1,k})_\rho\to(a_1)_\rho\) in \(S^{m_1+1}_+\). By Step 4, \(T_{(a_{1,k})_\rho}T_{a_2}u=T_{b^{(k)}}u\), where \(b^{(k)}\) is built from \((a_{1,k})_\rho\) and \(a_2\). As \(k\to\infty\), the left side converges to \(T_{(a_1)_\rho}T_{a_2}u\) (Theorem 5.1, continuity in the symbol), and \(b^{(k)}\) converges in \(S^{m_1+1+m_2}_+\) by Steps 1–2, so the right side converges to \(T_bu\) with \(b\) built from \((a_1)_\rho\). Bilinearity gives the formula for \(a_1\).

*Step 6: conclusions.* \(T_bu=T_{a_1}T_{a_2}u\) depends only on \(u|_{\mathbb R^n_+}\), so \(b\) is lacunary by Proposition 4.3. The operator determines the symbol, so \(b\) does not depend on \(\chi\). Continuity and the expansion come from Steps 1–2. \(\square\)

**Remark 8.2** (The truncated symbols do not converge in the symbol topology). For the tangential-translation example in this paragraph assume \(n\ge2\). In Step 4 the symbols \(b_k\) are bounded and converge pointwise, but they need not converge to \(b\) in the Fréchet topology of \(S^{-\infty}_+\), even when \(a_1\) is residual. Take \(a_2=\theta(x_n)\), with \(\theta\in C_0^\infty(\mathbb R)\) equal to 1 on \([0,1]\), and \(a_1=e^{-x_n}\widehat h(\xi)\) with \(0\leq h\in C_0^\infty(\{|z|<\tfrac12\})\), \(h\neq0\). Both are lacunary, \(T_{a_2}\) is multiplication by \(\theta(x_n)\), and \(T_{a_1}\) commutes with translations in \(x'\). If \(b_k\to b\) in \(S^{-\infty}_+\), then \(T_{b_k}\to T_b\) in the operator norm on \(L^2(\mathbb R^n_+)\), by the Schur bound of Proposition 6.4, which is linear in a seminorm of the symbol. But let \(u_0\geq0\) be a bump near \((0,\tfrac12)\), and let \(u\) be a translate of \(u_0\) in \(x'\) far outside the support of \(\vartheta(\cdot/k)\). Then \(\|(T_{b_k}-T_b)u\|=\|T_{a_1}(\theta u_0)\|>0\), independently of \(k\). So only boundedness together with pointwise convergence is available, and that is what Step 4 uses.

**Example 8.3** (A totally characteristic differential operator: product, adjoint, jets). Let \(\theta\in C_0^\infty(\mathbb R)\) equal 1 on \([-1,2]\) and \(a(x,\xi)=\theta(x_n)\xi_n\). It lies in \(S^1_{\mathrm{la}}\) (strongly lacunary, since \(\mathcal F_na\) is supported at \(t=0\)), and \(T_a=\theta(x_n)x_nD_n\).

*Product.* In (8.3) only \(\alpha=0\) and \(\alpha=e_n\) contribute: \(a\,a=\theta^2\xi_n^2\), and \(\partial_{\xi_n}a\cdot D_s[\theta(sx_n)s\xi_n]_{s=1}=-i\theta(\theta+x_n\theta')\xi_n\). Directly, \(\theta x_nD_n(\theta x_nD_nu)=\theta^2x_n^2D_n^2u-i\theta(\theta+x_n\theta')x_nD_nu\), whose compressed symbol is the same. Where \(\theta=1\) this is \((x_nD_n)^2=x_n^2D_n^2-ix_nD_n\), in agreement with (2.1).

*Adjoint.* By (7.5), the term \(j=0\) is \(\theta\xi_n\), the term \(j=1\) is \(\partial_{\eta_n}D_{y_n}[\theta(x_ny_n)y_n\eta_n]_{y_n=1}=-i(\theta+x_n\theta')\), and all later terms vanish. Directly, \((\theta x_nD_n)^*=D_n\,x_n\theta=\theta x_nD_n-i(\theta+x_n\theta')\). The expansion is exact here: the difference is a differential operator with symbol in \(S^{-\infty}_+\), hence 0.

*Jets.* In (5.2) only \(a_{kk}=\binom k1(-i)\theta(0)=-ik\) is nonzero near the boundary, so \(D_n^k(x_nD_nu)(x',0)=-ik\,D_n^ku(x',0)\); this is Leibniz' rule for \(D_n^k(x_nw)\) at \(x_n=0\).

## 9. Extension to distributions

By duality with the adjoints of Section 7, the operators act on supported and on restricted tempered distributions.

### Supported and restricted distributions

**Theorem 9.1** (Extension to distributions). Let \(a\in S^m_{\mathrm{la}}\).

(a) For \(U\in\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\) and \(v\in\overline{\mathcal S}(\mathbb R^n_+)\) the pairing \((U,v)=U(\overline V)\), \(V\) any Schwartz extension of \(v\), is well defined, and it identifies \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\) with the space of continuous antilinear functionals on \(\overline{\mathcal S}(\mathbb R^n_+)\).

(b) The formula
\[
(T_aU,v)=(U,T_{a^\dagger}v)\qquad(v\in\overline{\mathcal S}(\mathbb R^n_+))
\tag{9.1}
\]
defines a continuous map \(T_a:\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\to\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\). For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\) with zero extension \(u_0\), \(T_au_0\) is the zero extension of the function \(T_au\).

(c) The restriction map \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\to\overline{\mathcal S'}(\mathbb R^n_+)\) is surjective, and its kernel is
\[
\{U\in\mathcal S':\operatorname{supp}U\subset\partial\mathbb R^n_+\}=\bigcup_{k\geq0}\dot{\mathcal S}'_k,\qquad \dot{\mathcal S}'_k=\{U\in\mathcal S'(\mathbb R^n):x_n^kU=0\}.
\tag{9.2}
\]

(d) \(T_a\dot{\mathcal S}'_k\subset\dot{\mathcal S}'_k\) for every \(k\). Hence \(T_a\) induces a map \(\overline{\mathcal S'}(\mathbb R^n_+)\to\overline{\mathcal S'}(\mathbb R^n_+)\). Identifying \(\overline{\mathcal S'}(\mathbb R^n_+)\) with the antidual of \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\), this map is again given by (9.1), now with \(v\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\).

(e) Every element of \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\), and every element of \(\overline{\mathcal S'}(\mathbb R^n_+)\), is a weak limit of a sequence in \(C_0^\infty(\mathbb R^n_+)\). So the action of \(T_a\) on either space is determined by its action on \(C_0^\infty(\mathbb R^n_+)\).

**Proof.** (a) If two extensions differ by \(\varphi\), then \(\varphi=0\) in \(\mathbb R^n_+\), and \(U(\overline\varphi)=0\) by Lemma 3.1. Since \(|U(\overline V)|\leq Cp(V)\) for a Schwartz seminorm \(p\) and every extension \(V\), \(|(U,v)|\leq C\bar p(v)\) with the quotient seminorm, so the functional is continuous. Conversely, a continuous antilinear \(\lambda\) on \(\overline{\mathcal S}(\mathbb R^n_+)\) gives \(U(\varphi)=\lambda(\overline\varphi|_{\mathbb R^n_+})\), which is linear and continuous on \(\mathcal S\), vanishes on \(C_0^\infty(\mathbb R^n_-)\) (so \(\operatorname{supp}U\subset\overline{\mathbb R}{}^n_+\)), and satisfies \((U,v)=\lambda(v)\).

(b) \(T_{a^\dagger}\) is continuous on \(\overline{\mathcal S}(\mathbb R^n_+)\) (Theorem 5.1), so (9.1) defines a continuous map by (a). For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\), \((T_au_0,v)=\int_{\mathbb R^n_+}u\,\overline{T_{a^\dagger}v}=(T_au,v)_{L^2(\mathbb R^n_+)}\) by Theorem 7.3(c).

(c) Surjectivity. Let \(w=U|_{\mathbb R^n_+}\), \(U\in\mathcal S'\). There is a Schwartz seminorm \(p\) with \(|U(\varphi)|\leq p(\varphi)\). On the subspace \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\subset\overline{\mathcal S}(\mathbb R^n_+)\) (restriction is injective on it), \(p(v)\) equals the corresponding sum of suprema over \(\mathbb R^n_+\), a continuous seminorm \(\bar p\) of \(\overline{\mathcal S}(\mathbb R^n_+)\) by Lemma 3.2(a). The antilinear functional \(v\mapsto U(\overline v)\) on this subspace is bounded by \(\bar p\). By the complete Hahn–Banach theorem in seminorm form linked in Section 1, applied to the linear functional \(v\mapsto\overline{U(\overline v)}\), it extends to \(\overline{\mathcal S}(\mathbb R^n_+)\) with the same bound. By (a) the extension is some \(\tilde U\in\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\), and \(\tilde U=U\) on \(C_0^\infty(\mathbb R^n_+)\). So \(\tilde U|_{\mathbb R^n_+}=w\).

Kernel. An element of \(\dot{\mathcal S}'\) that vanishes in \(\mathbb R^n_+\) has support in \(\partial\mathbb R^n_+\); conversely \(x_n^kU=0\) forces \(U=0\) on \(x_n\neq0\). Let \(\operatorname{supp}U\subset\{x_n=0\}\). Being tempered, \(U\) satisfies \(|U(\varphi)|\leq C\sum_{|\alpha|,|\beta|\leq\mu}\sup|x^\alpha D^\beta\varphi|\) for some \(\mu\). Let \(\theta\in C_0^\infty(\mathbb R)\) equal 1 on \([-1,1]\) and vanish outside \([-2,2]\), and \(\theta_\varepsilon(x)=\theta(x_n/\varepsilon)\). For \(\varphi\in\mathcal S\), \((1-\theta_\varepsilon)x_n^{\mu+1}\varphi\) vanishes near \(\operatorname{supp}U\), so \(U(x_n^{\mu+1}\varphi)=U(\theta_\varepsilon x_n^{\mu+1}\varphi)\). A derivative of order \(|\beta|\leq\mu\) of \(\theta_\varepsilon x_n^{\mu+1}\varphi\) is a sum of terms of size \(\varepsilon^{-i}\,\varepsilon^{\mu+1-j}\,|D^\gamma\varphi|\), \(i+j+|\gamma|=|\beta|\), on \(|x_n|\leq2\varepsilon\); each is \(O(\varepsilon)\), with the weights \(x^\alpha\) carried by \(\varphi\). So \(U(x_n^{\mu+1}\varphi)=0\), that is, \(U\in\dot{\mathcal S}'_{\mu+1}\).

(d) Let \(U\in\dot{\mathcal S}'_k\) and \(v\in\overline{\mathcal S}(\mathbb R^n_+)\). Then \((x_n^kT_aU,v)=(U,T_{a^\dagger}(x_n^kv))\). The jets of \(x_n^kv\) of order \(<k\) vanish, so by Theorem 5.1(d) those of \(T_{a^\dagger}(x_n^kv)\) do too, and Lemma 3.2(d) writes it as \(x_n^kh\), \(h\in\overline{\mathcal S}(\mathbb R^n_+)\). So \((x_n^kT_aU,v)=(x_n^kU,h)=0\). For the last assertion: \(\overline{\mathcal S'}(\mathbb R^n_+)\) is \(\mathcal S'\) modulo the distributions vanishing in \(\mathbb R^n_+\), and these are exactly the tempered distributions that annihilate the closed subspace \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\) (one inclusion is Lemma 3.1 with the half spaces exchanged, the other holds because \(C_0^\infty(\mathbb R^n_+)\subset\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\)). With the Hahn–Banach theorem this identifies \(\overline{\mathcal S'}(\mathbb R^n_+)\) with the antidual of \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\). If \(U\in\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\) restricts to \(u\) and \(v\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\), then \(T_{a^\dagger}v\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\) (Theorem 5.1(d)) and \((T_aU,v)=(U,T_{a^\dagger}v)=(u,T_{a^\dagger}v)\).

(e) Let \(U\in\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\). Choose \(\phi\in C_0^\infty(\mathbb R^n_+)\) with \(\int\phi=1\) and \(\theta\in C_0^\infty(\mathbb R^n)\) equal to 1 near 0, and put \(U_\varepsilon=\theta(\varepsilon x)\,(\phi_\varepsilon*U)\), \(\phi_\varepsilon=\varepsilon^{-n}\phi(\cdot/\varepsilon)\). Then \(U_\varepsilon\in C_0^\infty(\mathbb R^n_+)\), since \(\operatorname{supp}(\phi_\varepsilon*U)\subset\overline{\mathbb R}{}^n_++\operatorname{supp}\phi_\varepsilon\subset\mathbb R^n_+\). For \(\varphi\in\mathcal S\), \(U_\varepsilon(\varphi)=U(\check\phi_\varepsilon*(\theta(\varepsilon\cdot)\varphi))\), and \(\check\phi_\varepsilon*(\theta(\varepsilon\cdot)\varphi)\to\varphi\) in \(\mathcal S\). So \(U_\varepsilon\to U\) weakly. Restricting gives the statement for \(\overline{\mathcal S'}(\mathbb R^n_+)\). Both actions of \(T_a\) are weakly continuous, being transposes of continuous maps. \(\square\)

In the ordinary calculus one works modulo smooth functions, the range of operators of order \(-\infty\). Here one also loses the distributions supported on the boundary when passing to \(\overline{\mathcal S'}(\mathbb R^n_+)\): they are the kernel (9.2).

By (e), the composition formula \(T_{a_1}T_{a_2}=T_b\) of Theorem 8.1 holds on \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\) and on \(\overline{\mathcal S'}(\mathbb R^n_+)\) as well. Indeed, both sides are weakly continuous, and by (b) they agree on \(C_0^\infty(\mathbb R^n_+)\).

### Residual operators produce conormal distributions

**Lemma 9.2** (Bounded order implies conormality). Let \(W\in\mathcal D'(\mathbb R^n)\). Suppose there is \(\mu\) such that every \(D'^{\alpha'}(x_nD_n)^{\alpha_n}W\) has order at most \(\mu\) on every compact set (the constants may depend on \(\alpha\) and the set). Then \(W\in I^{\mu+n/4}(\mathbb R^n,\partial\mathbb R^n_+)\).

**Proof.** If \(w\) has order \(\leq\mu\) near the support of \(\phi\in C_0^\infty\), then \(|\widehat{\phi w}(\xi)|=|w(\phi e^{-ix\cdot\xi})|\leq C(1+|\xi|)^\mu\), so \(\|\Pi_j(\phi w)\|_{L^2}^2\leq C2^{2j\mu}2^{jn}\) and \(\phi w\in B^{-\mu-n/2}_{2,\infty}\). Products of first-order operators whose principal symbols vanish on \(N^*(\partial\mathbb R^n_+)\) are, by Hadamard's lemma and the commutation argument of Proposition 2.1(c), finite sums of smooth functions times \(D'^{\alpha'}(x_nD_n)^{\alpha_n}\); multiplication by smooth functions preserves the local order. So all these products map \(W\) into \(B^{-\mu-n/2}_{2,\infty,\mathrm{loc}}\). By the definition of conormal distributions in Section 1, this says that \(W\in I^{\mu+n/4}\), since \(-(\mu+n/4)-n/4=-\mu-n/2\). \(\square\)

**Theorem 9.3** (Conormal outputs). Let \(a\in S^{-\infty}_{\mathrm{la}}\) and \(U\in\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\). Then \(\operatorname{supp}T_aU\subset\overline{\mathbb R}{}^n_+\) and \(T_aU\in I^k(\mathbb R^n,\partial\mathbb R^n_+)\) for some \(k\). More precisely, if \(|(U,v)|\leq C\sum_{|\beta|+|\gamma|\leq\mu}q_{\beta,\gamma}(v)\), then there is \(\mu'\), depending only on \(\mu\) and \(n\), such that every \(D'^{\alpha'}(x_nD_n)^{\alpha_n}T_aU\) has order at most \(\mu'\) on every compact set, and \(T_aU\in I^{\mu'+n/4}\).

**Proof.** The support statement is part of Theorem 9.1. Since \(U\) is continuous on \(\overline{\mathcal S}(\mathbb R^n_+)\), a bound of the stated form holds by Lemma 3.2(a). For \(\varphi\in C_0^\infty(\mathbb R^n)\), using the formal adjoints \((x_nD_n)^*=D_nx_n\) and (5.4),
\[
\big(D'^{\alpha'}(x_nD_n)^{\alpha_n}T_aU,\varphi\big)=\big(U,T_{a^\dagger}D'^{\alpha'}(D_nx_n)^{\alpha_n}\varphi\big)=(U,T_{b_\alpha}\varphi),\qquad
b_\alpha=\xi'^{\alpha'}\big(\xi_n-i-i\xi_n\partial_{\xi_n}\big)^{\alpha_n}a^\dagger\in S^{-\infty}_{\mathrm{la}} .
\]
By Theorem 5.1(a), applied in the fixed class \(S^0_{\mathrm{la}}\supset S^{-\infty}_{\mathrm{la}}\), there are \(\mu'\) (depending only on \(\mu\) and \(n\)) and a seminorm \(p\) with \(\sum_{|\beta|+|\gamma|\leq\mu}q_{\beta,\gamma}(T_{b_\alpha}\varphi)\leq p(b_\alpha)\sum_{|\beta|+|\gamma|\leq\mu'}q_{\beta,\gamma}(\varphi)\). For \(\varphi\) supported in a fixed compact set the right side is at most \(C\,p(b_\alpha)\sum_{|\gamma|\leq\mu'}\sup|D^\gamma\varphi|\). So the order is at most \(\mu'\), with constants depending on \(\alpha\) only through \(p(b_\alpha)\). Lemma 9.2 finishes the proof. \(\square\)

In particular the wave front set of \(T_aU\) lies in the conormal bundle of the boundary, since this holds for every element of \(I^k(\mathbb R^n,\partial\mathbb R^n_+)\) (Section 1).

