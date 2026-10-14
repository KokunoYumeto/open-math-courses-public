# Densities and planar tangent measures

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lessons produced a positive current \(P\) and a square integrable anti-invariant correction \(Q\) with \(P+Q\) closed, together with two estimates: quadratic growth of the trace measure ([Quadratic mass growth](quadratic-mass-growth.md)) and the angular bound ([Regularization and angular control](regularization-and-angular-control.md)). The decisive step of the proof is that the part of \(P\) carried by points of positive two-dimensional density is closed by itself. This lesson states that theorem in a general form and proves its two geometric ingredients: the density exists at every point, and at almost every point of positive density the current looks, at small scales, like a constant multiple of a complex line. The last lesson deduces the theorem from these two facts.

- The closedness theorem (Theorem 1.1), and the polarization of a measure on complex lines.
- Existence of the density (Proposition 2.1).
- Translation-invariant measures, closed constant currents and vague limits (Lemmas 3.1, 3.2 and 3.3).
- The vanishing transverse moment (Proposition 4.1).

The lesson follows [OpenAI-TC, Section 5]. Notation is that of [Taming, compatibility and a separating current](taming-compatibility-and-a-separating-current.md); \(\rho_0\) and normal coordinates are as in [Quadratic mass growth](quadratic-mass-growth.md), and \(z_x(y)=\exp_x^{-1}(y)\in T_xX\) for \(d(x,y)<4\rho_0\).

## 1. The closedness theorem

Let \(\lambda\) be a finite positive Borel measure on the bundle \(\mathscr C\) of unit complex-line bivectors, with projection \(\mu\) to \(X\). In a local orthonormal frame of bivectors over an open set \(U\), the six measures \(E\mapsto\int_{\pi^{-1}E}\ell_k\,d\lambda(x,\ell)\) given by the coordinates \(\ell_k\) of \(\ell\) are dominated by \(\mu\), since \(|\ell_k|\le1\). By the Radon–Nikodym theorem ([Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, Measure Theory, Volume 2, Section 232](https://www1.essex.ac.uk/maths/people/fremlin/cont23.htm)) they have densities, which define a Borel bivector field \(A\), unique \(\mu\)-almost everywhere, with \(|A|\le1\) and
\[
\int\langle\beta_x,\ell\rangle\,d\lambda(x,\ell)=\int\langle\beta,A\rangle\,d\mu
\]
for every bounded Borel field of two-forms \(\beta\) (first for \(\beta=\mathbf 1_E\) times a frame form, then by linearity and uniform approximation by simple fields). We call \(A\) the *polarization* of \(\lambda\). Testing with \(\beta=F\), with \(R\beta\), and with semidefinite invariant forms of constant matrix in a unitary frame shows that \(A(x)\) lies in the convex hull \(\mathscr K_x\) of \(\mathscr C_x\) for \(\mu\)-almost every \(x\) (Exercise 5.4). For the measure of Proposition 4.1 of the first lesson this is the field \(A\) constructed there.

**Theorem 1.1** (closedness of the positive-density part; [OpenAI-TC, Theorem 5.1]). Let \(\lambda\) be a finite positive Borel measure on \(\mathscr C\) with projection \(\mu\), and \(P(\alpha)=\int\alpha_x(\ell)\,d\lambda(x,\ell)\). Let \(Q\) be a square integrable anti-invariant two-form such that \(T=P+Q\) is a closed current. Suppose that, for \(0<r\le r_1\) and all \(x\), \(\mu(B_r(x))\le Cr^2\) and \(\mathcal I_r\le Cr^4\), where
\[
\mathcal I_r=\iint_{d(x,y)<r}|\ell-\tau_{yx}m|^2\,d\lambda\,d\lambda ,
\]
with \((x,\ell)\) and \((y,m)\) both distributed by \(\lambda\). Then the limit
\[
\theta(x)=\lim_{r\to0}r^{-2}\mu(B_r(x))
\]
exists at every point. If \(E=\{x:\theta(x)>0\}\), the current \(P_E=\mathbf 1_EP\), given by \(P_E(\alpha)=\int_{\pi^{-1}E}\alpha_x(\ell)\,d\lambda\), is closed.

The hypotheses do not require \(P\) to annihilate closed invariant forms. For the current of the first lesson they hold: quadratic growth is Proposition 4.1 of [Quadratic mass growth](quadratic-mass-growth.md), and \(Q\in L^2\) and the angular bound are Proposition 6.1 of [Regularization and angular control](regularization-and-angular-control.md), under the hypothesis (HK) stated there.

Throughout this lesson and the next, the hypotheses of Theorem 1.1 are in force, \(T=P+Q\), and \(\sigma=\mu+|Q|\,dV\). By Cauchy–Schwarz, \(\int_{B_s(x)}|Q|\,dV\le\|Q\|\,\mathrm{vol}(B_s(x))^{1/2}\), which is at most \(Cs^2\), so
\[
\sigma(B_s(x))\le Cs^2\qquad(0<s\le r_1) .
\]
The current \(T\) extends to bounded Borel forms \(\beta\) by \(T(\beta)=\int\langle\beta,A\rangle\,d\mu+\int\langle\beta,Q\rangle\,dV\), and \(|T(\beta)|\le\int|\beta|\,d\sigma\).

## 2. The density exists

**Proposition 2.1** ([OpenAI-TC, Lemma 5.2]). The limit \(\theta(p)=\lim_{r\to0}r^{-2}\mu(B_r(p))\) exists and is finite at every \(p\in X\).

*Proof.* Fix \(p\) and normal coordinates \(z\) at \(p\), \(t=|z|\). Let \(J_0=J(p)\) and \(F_0=F_p\), viewed as constant-coefficient objects in these coordinates; by Exercise 5.2 of the second lesson, \(dd^c_{J_0}(t^2/2)=2F_0\). Call a radius \(r<\rho_0\) *good* if the sphere \(\{t=r\}\) is \(\sigma\)-null. Only countably many spheres about \(p\) have positive \(\sigma\)-mass, since they are disjoint and \(\sigma\) is finite. For good \(r\) put
\[
b(r)=r^{-2}\,T(\mathbf 1_{B_r(p)}F_0) .
\]

*An exact identity.* For \(a>0\) let
\[
\varphi_a(t)=\begin{cases}\log a+\dfrac{t^2-a^2}{2a^2},&t<a,\\ \log t,&t\ge a.\end{cases}
\]
At \(t=a\) both pieces have value \(\log a\) and slope \(1/a\), so \(\varphi_a\) is \(C^{1,1}\). For good \(0<r<s\), the function \(\psi=\varphi_r-\varphi_s\) of \(z\) vanishes for \(t\ge s\). Its form \(dd^c_{J_0}\psi\) is \(2(r^{-2}-s^{-2})F_0\) on \(B_r\), equals \(dd^c_{J_0}\log t-2s^{-2}F_0\) where \(r<t<s\), and is zero outside \(B_s\). Euclidean mollifications \(\psi_k\) of \(\psi\) are smooth with support in the chart, have uniformly bounded second derivatives, and converge with their second derivatives off the two spheres. Since \(J_0\) is constant, \(dd^c_{J_0}\psi_k=d(d^c_{J_0}\psi_k)\) is exact, so \(T(dd^c_{J_0}\psi_k)=0\); dominated convergence against \(\sigma\), for which the spheres are null, gives \(T(dd^c_{J_0}\psi)=0\). Since \(\mathbf 1_{B_r}+\mathbf 1_{\{r<t<s\}}=\mathbf 1_{B_s}\) off a \(\sigma\)-null sphere, this reads
\[
b(s)-b(r)=\tfrac12\,T\bigl(\mathbf 1_{\{r<t<s\}}\,dd^c_{J_0}\log t\bigr) .
\]

*Almost monotonicity.* The form \(\beta=dd^c_{J_0}\log t\) is \(J_0\)-invariant (Lemma 2.1 of the second lesson) and semipositive for \(J_0\): with \(H=t^{-2}I-2t^{-4}zz^\top\),
\[
\begin{aligned}
&\beta(v,J_0v)=2t^{-2}|v|^2\\
&\quad-2t^{-4}\bigl((z\cdot v)^2+(z\cdot J_0v)^2\bigr)\ge0 .
\end{aligned}
\]
Its size is \(O(t^{-2})\). At a point \(y\) with \(t=t(y)\), \(|J(y)-J_0|\le Ct\). Hence, for a unit \(v\), \(\beta(v,J(y)v)\ge\beta(v,J_0v)-Ct^{-2}t\), which is at least \(-C/t\), and by convexity \(\langle\beta,A(y)\rangle\ge-C/t\) for \(A(y)\in\mathscr K_y\). Also the \(J(y)\)-anti-invariant part of \(\beta\) is \(\frac12(\beta(J_0\cdot,J_0\cdot)-\beta(J(y)\cdot,J(y)\cdot))\), of size at most \(C/t\), so \(|\langle\beta,Q\rangle|\le C|Q|/t\) since \(Q\) is anti-invariant. Splitting \(\{0<t<s\}\) into the shells \(2^{-k-1}s\le t<2^{-k}s\),
\[
\begin{aligned}
\int_{\{0<t<s\}}t^{-1}\,d\sigma&\le\sum_{k\ge0}\frac{2^{k+1}}s\,C(2^{-k}s)^2\\
&\le Cs .
\end{aligned}
\]
Therefore
\[
b(s)-b(r)\ge-Cs\qquad(r<s\text{ good}) .
\]

*Comparison with \(\mu\).* \(T(\mathbf 1_{B_r}F)=\mu(B_r)\), since \(\langle F,A\rangle=1\) \(\mu\)-almost everywhere and \(\langle F,Q\rangle=0\). As \(|F-F_0|\le Ct\),
\[
\begin{aligned}
\bigl|b(r)-r^{-2}\mu(B_r(p))\bigr|&\le r^{-2}\,Cr\,\sigma(B_r(p))\\
&\le Cr .
\end{aligned}
\]
In particular \(b\) is bounded.

*The limit.* Fix a good \(s\) and let \(r\to0\) through good radii: \(\limsup_{r}b(r)\le b(s)+Cs\). Letting \(s\to0\) along good radii with \(b(s)\to\liminf b\) gives \(\limsup b\le\liminf b\). So \(b\), and by the comparison \(r^{-2}\mu(B_r(p))\), converge along good radii. For an arbitrary small \(r\) and \(\varepsilon>0\), choose good radii \(r_1\in((1-\varepsilon)r,r)\) and \(r_2\in(r,(1+\varepsilon)r)\); monotonicity of \(\mu(B_r(p))\) in \(r\) traps \(r^{-2}\mu(B_r(p))\) between \((1-\varepsilon)^2\) and \((1+\varepsilon)^2\) times the values at \(r_1\) and \(r_2\). Letting \(r\to0\) and then \(\varepsilon\to0\) gives the limit along all radii. Finiteness follows from quadratic growth. \(\blacksquare\)

This is an almost monotonicity formula of Lelong type: \(r^{-2}\) times the mass of a ball, corrected by \(F_0\), can decrease only by \(O(r)\) as the radius shrinks.

## 3. Three tools

**Lemma 3.1** (translation-invariant measures). Let \(\nu\) be a positive Radon measure on \(\mathbb R^k\) and \(L\subseteq\mathbb R^k\) a linear subspace such that \(\nu\) is invariant under translation by every vector of \(L\). Then there is a positive Radon measure \(\gamma\) on \(L^\perp\) with
\[
\int f\,d\nu=\int_{L^\perp}\int_Lf(a+b)\,da\,d\gamma(b)
\]
for \(f\in C_c(\mathbb R^k)\), where \(da\) is Lebesgue measure on \(L\). If \(L=\mathbb R^k\), then \(\nu\) is a constant multiple of Lebesgue measure.

*Proof.* First let \(L=\mathbb R^k\) and \(c=\nu([0,1)^k)\). Invariance and additivity give \(\nu(Q)=c\,2^{-jk}\) for every half-open dyadic cube \(Q\) of side \(2^{-j}\). Every open set is a countable disjoint union of such cubes, so \(\nu\) and \(c\) times Lebesgue measure agree on open sets, hence as Radon measures. In general, for \(\psi\ge0\) in \(C_c(L^\perp)\), the measure \(\varphi\mapsto\int\varphi(\pi_Lw)\psi(\pi_{L^\perp}w)\,d\nu(w)\) on \(L\) is translation invariant, hence equals \(c(\psi)\) times Lebesgue measure. The map \(\psi\mapsto c(\psi)\) is a positive linear form, hence a positive Radon measure \(\gamma\) on \(L^\perp\) (Theorem 4.1 of [Order, positivity and distributional limits](course:AN-01/reader/AN01-U008), course *Distributions, kernels and analytic singularities*). The two sides of the formula agree on products \(\varphi\otimes\psi\), whose linear combinations are dense in \(C_c(\mathbb R^k)\) in the inductive-limit sense. \(\blacksquare\)

**Lemma 3.2** (closed constant currents). Let \(A=\sum_{i<j}A^{ij}e_i\wedge e_j\) be a constant bivector on \(\mathbb R^k\), extend \(A^{ij}\) to a skew matrix, and let \(\nu\) be a positive Radon measure such that the current \(S(\beta)=\int\langle\beta,A\rangle\,d\nu\) is closed. Then \(\nu\) is invariant under translation by every vector in the column space of \((A^{ij})\).

*Proof.* For a compactly supported smooth one-form \(\gamma=\sum_j\gamma_j\,dz^j\), \(d\gamma=\sum_{i<j}(\partial_i\gamma_j-\partial_j\gamma_i)\,dz^i\wedge dz^j\), and skew-symmetry gives
\[
0=S(d\gamma)=\sum_{i,j}\int\partial_i\gamma_j\,A^{ij}\,d\nu .
\]
Taking \(\gamma\) with one nonzero component, \(\sum_iA^{ij}\partial_i\nu=0\) as a distribution for each \(j\). So \(\partial_v\nu=0\) for \(v\) in the column space. For \(\varphi\in C^\infty_c\), the derivative of \(\tau\mapsto\int\varphi(w+\tau v)\,d\nu(w)\) is \(\int\partial_v\varphi(w+\tau v)\,d\nu(w)=0\), and translation invariance follows for continuous compactly supported functions, hence for \(\nu\). \(\blacksquare\)

**Lemma 3.3** (vague limits). Let \(\nu_k\) be positive Radon measures on \(\mathbb R^k\) with \(\sup_k\nu_k(B_m(0))<\infty\) for every \(m\). Then a subsequence converges vaguely, that is \(\int f\,d\nu_{k'}\to\int f\,d\nu\) for all \(f\in C_c(\mathbb R^k)\), to a positive Radon measure \(\nu\). If moreover \(\nu(\partial B_D(0))=0\), then \(\nu_{k'}(B_D(0))\to\nu(B_D(0))\).

*Proof.* For each \(m\), the restrictions of \(\nu_k\) to the open ball \(B_m\) are bounded functionals on the separable space \(C_0(B_m)\). By the Banach–Alaoglu theorem and the metrizability of the weak\(^*\) topology on bounded sets (Theorem 3.1 and Proposition 3.2 of [Weak topologies: Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian)), a subsequence converges weak\(^*\); a diagonal subsequence works for all \(m\). The limit is positive, and by Lemma 3.1 of the lesson on order and positivity cited above it is a positive Radon measure, consistently in \(m\). For the last claim, choose continuous compactly supported \(f_-\le\mathbf 1_{B_D}\le f_+\) with \(\int(f_+-f_-)\,d\nu<\varepsilon\), which is possible since \(\nu(\partial B_D)=0\). \(\blacksquare\)

## 4. The vanishing transverse moment

For \((x,\ell)\in\mathscr C\) let \(\mathrm{pr}_{L_\ell^\perp}\) be the orthogonal projection of \(T_xX\) onto the orthogonal complement of the plane \(L_\ell\).

**Proposition 4.1** ([OpenAI-TC, Lemma 5.3]). For \((x,\ell)\in\mathscr C\) and \(0<r<\rho_0\) put
\[
n_r(x,\ell)=\int_{B_r(x)}\Bigl|\mathrm{pr}_{L_\ell^\perp}\frac{z_x(y)}r\Bigr|^2d\mu(y) .
\]
Then, as \(r\to0\),
\[
\mathcal N_r=\int_{\mathscr C}n_r\,d\lambda=o(r^2) .
\]

*Proof.* *Step 1: Lebesgue points of the polarization.* Fix a finite atlas of charts with orthonormal frames of bivectors. By Theorem 5.1 of [Besicovitch's covering theorem and the differentiation of Radon measures](course:measurable-fields-and-direct-integrals/besicovitch-s-covering-theorem-and-the-differentiation-of-radon-measures) (course *Measurable fields and direct integrals*), applied in each chart to the components of \(A\), for \(\mu\)-almost every \(p\) the mean of \(|A(y)-A(p)|\) over coordinate balls \(B^{\mathrm E}_\delta(p)\) with respect to \(\mu\) tends to zero as \(\delta\to0\). A geodesic ball \(B_{Dr}(p)\) lies in a coordinate ball of radius \(CDr\), whose \(\mu\)-mass is at most \(CD^2r^2\) by quadratic growth. Hence, for every fixed \(D\),
\[
r^{-2}\int_{B_{Dr}(p)}|A(y)-A(p)|\,d\mu(y)\longrightarrow0 ,
\]
and the same holds for the components in the coordinate frame of normal coordinates at \(p\), because changing to this smoothly varying frame adds \(O(r^{-2}\cdot Dr\cdot D^2r^2)=O(r)\). Call such \(p\) *Lebesgue points*. Also \(A(p)\in\mathscr K_p\) for \(\mu\)-almost every \(p\).

*Step 2: tangent measures.* Fix a Lebesgue point \(p\) with \(A(p)\in\mathscr K_p\) and \(\theta(p)>0\), and identify \(T_pX\) with \(\mathbb R^4\) by an orthonormal basis. Let \(\nu_r\) be the measure on \(\mathbb R^4\) given by \(\int f\,d\nu_r=r^{-2}\int_{B_{\rho_0}(p)}f(z_p(y)/r)\,d\mu(y)\). Then \(\nu_r(B_D(0))=r^{-2}\mu(B_{Dr}(p))\le CD^2\). By Lemma 3.3 every sequence \(r_k\to0\) has a subsequence along which \(\nu_r\) converges vaguely to some \(\nu\). For \(D\) with \(\nu(\partial B_D)=0\),
\[
\begin{aligned}
\nu(B_D(0))&=\lim r^{-2}\mu(B_{Dr}(p))\\
&=\theta(p)D^2 .
\end{aligned}
\]
All but countably many \(D\) qualify. Increasing and decreasing sequences of such \(D\) give \(\nu(B_D(0))=\nu(\overline{B_D(0)})=\theta(p)D^2\) for every \(D>0\).

*Step 3: the limit current is closed.* For a compactly supported smooth two-form \(\beta=\sum_{i<j}\beta_{ij}\,dw^i\wedge dw^j\) on \(\mathbb R^4\), the dilation \(D_r=z_p/r\) pulls back to \(D_r^*\beta=r^{-2}\sum\beta_{ij}(z/r)\,dz^i\wedge dz^j\), supported in the chart for small \(r\). The rescaled current \(T_r(\beta)=T(D_r^*\beta)\) is closed, since \(D_r^*\) commutes with \(d\). Its parts are
\[
\begin{gathered}
P(D_r^*\beta)=\int\textstyle\sum_{i<j}\beta_{ij}A_r^{ij}\,d\nu_r ,\\
|Q(D_r^*\beta)|\\
\le C\|\beta\|_\infty\,r^{-2}\int_{B_{Dr}(p)}|Q|\,dV ,
\end{gathered}
\]
where \(A^{ij}\) are the components of \(A\) in the coordinate frame, \(A_r^{ij}(w)=A^{ij}(z_p^{-1}(rw))\), and \(\beta\) is supported in \(B_D(0)\). By Step 1 the first expression differs by \(o(1)\) from \(\int\sum\beta_{ij}A^{ij}(p)\,d\nu_r\), which tends to \(\int\langle\beta,A(p)\rangle\,d\nu\) along the subsequence. The second is at most \(C_D\|\beta\|_\infty\|Q\|_{L^2(B_{Dr}(p))}\) by Cauchy–Schwarz, which tends to zero by absolute continuity of the integral of \(|Q|^2\). Therefore the constant current \(\beta\mapsto\int\langle\beta,A(p)\rangle\,d\nu\) is closed.

*Step 4: the polarization is a complex line.* By Lemma 3.2, \(\nu\) is invariant under translation by the column space of the skew matrix of \(A(p)\). By Lemma 1.2(4) of the first lesson this space has dimension two or four, and \(A(p)\ne0\) since \(\langle F,A(p)\rangle=1\). Dimension four would make \(\nu\) a multiple of Lebesgue measure (Lemma 3.1), with \(\nu(B_D)\) proportional to \(D^4\), contradicting \(\nu(B_D)=\theta(p)D^2\) with \(\theta(p)>0\). So the dimension is two, and by Lemma 1.2(4) of the first lesson \(A(p)\) is a unit complex-line bivector, \(|A(p)|=1\), whose plane \(L\) is the column space.

*Step 5: the tangent measure is planar.* By Lemma 3.1, \(\nu=(\text{area on }L)\otimes\gamma\) for a positive Radon measure \(\gamma\) on \(L^\perp\). The ball \(B_D(0)\) meets the plane \(b+L\) in a disc of area \(\pi(D^2-|b|^2)_+\), so
\[
\begin{aligned}
\theta(p)&=\frac{\nu(B_D(0))}{D^2}\\
&=\pi\int_{L^\perp}\Bigl(1-\frac{|b|^2}{D^2}\Bigr)_+d\gamma(b)
\end{aligned}
\]
for every \(D>0\). For \(D_2>D_1\) the difference of the integrands is nonnegative, and positive at every \(b\) with \(0<|b|<D_2\). Since the integrals are equal, \(\gamma\) has no mass on \(\{0<|b|<D_2\}\) for any \(D_2\): \(\gamma=(\theta(p)/\pi)\,\delta_0\). Every vague limit is therefore \((\theta(p)/\pi)\) times area measure on \(L\), so \(\nu_r\) converges vaguely to it as \(r\to0\).

*Step 6: the moment.* Let \(\psi\) be continuous, equal to one on \(B_1(0)\), with support in \(B_2(0)\). Then
\[
\begin{aligned}
&r^{-2}n_r(p,A(p))\\
&\quad\le\int\psi(w)|\mathrm{pr}_{L^\perp}w|^2\,d\nu_r(w)\longrightarrow0 ,
\end{aligned}
\]
since the limit measure lives on \(L\), where the integrand vanishes.

*Step 7: integration.* Let \(S\) be the Borel set of Lebesgue points \(p\) with \(A(p)\in\mathscr K_p\) and \(\theta(p)>0\); there \(|A(p)|=1\) by Step 4. By the defining property of the polarization,
\[
\begin{aligned}
&\int_{\pi^{-1}S}|\ell-A(x)|^2\,d\lambda(x,\ell)\\
&\quad=\int_S\bigl(1-2|A|^2+|A|^2\bigr)d\mu=0 ,
\end{aligned}
\]
so \(\ell=A(x)\), and \(L_\ell\) is the plane of Step 4, for \(\lambda\)-almost every \((x,\ell)\) with \(x\in S\). For such \((x,\ell)\) the normalized inner integral \(r^{-2}n_r(x,\ell)\) tends to zero by Step 6. If \(\theta(x)=0\), it is at most \(r^{-2}\mu(B_r(x))\to0\). The remaining points form a \(\mu\)-null set. The normalized inner integrals are bounded by \(C\) by quadratic growth, and \(\lambda\) is finite, so dominated convergence gives \(r^{-2}\mathcal N_r\to0\). \(\blacksquare\)

Proposition 4.1 gives smallness without a rate: the mass near a typical point lies close to the complex line of the current there, in the mean-square sense, by \(o(r)\) at scale \(r\). The next lesson combines this with the angular bound, which is quantitative, to prove Theorem 1.1.

## 5. Exercises

**5.1.** Let \(\Sigma\subset X\) be a compact embedded surface and \(\mu\) its area measure. Show that \(\theta=\pi\) on \(\Sigma\) and \(\theta=0\) off \(\Sigma\), and that at every \(p\in\Sigma\) the rescaled measures \(\nu_r\) converge vaguely to area measure on \(T_p\Sigma\).

**5.2.** Show that \(\theta=0\) everywhere if \(\mu\) has a bounded density with respect to the volume.

**5.3.** In the notation of Proposition 2.1, show that \(dd^c_{J_0}\log t\) vanishes on every complex line through the origin: \(\beta(v,J_0v)=0\) when \(v\in\operatorname{span}(z,J_0z)\).

**5.4.** Prove that the polarization \(A\) of a finite measure \(\lambda\) on \(\mathscr C\) satisfies \(A(x)\in\mathscr K_x\) for \(\mu\)-almost every \(x\).

**5.5.** Show the converse of Lemma 3.2: if \(\nu\) is invariant under translation by the column space of \((A^{ij})\), then the current \(S\) is closed.

## 6. Solutions

**5.1.** At \(p\in\Sigma\), in normal coordinates \(\Sigma\) is a graph over \(T_p\Sigma\) with vanishing first derivatives at \(0\), so \(\mu(B_r(p))=\pi r^2(1+O(r))\) and \(\theta(p)=\pi\). For \(p\notin\Sigma\), \(\mu(B_r(p))=0\) for small \(r\). The measures \(\nu_r\) are the area measures of \(r^{-1}z_p(\Sigma)\), which converge smoothly to \(T_p\Sigma\) on compact sets.

**5.2.** If \(\mu\le c\,dV\), then \(\mu(B_r(p))\le Cr^4\), and \(r^{-2}\mu(B_r(p))\to0\).

**5.3.** By Lemma 2.1(3) of the second lesson, \(\beta(v,J_0v)=H(v,v)+H(J_0v,J_0v)\) with \(H=t^{-2}I-2t^{-4}zz^\top\). For \(v=az+bJ_0z\), \(z\cdot v=at^2\), \(z\cdot J_0v=-bt^2\) (as \(J_0\) is skew with \(J_0^2=-1\)), and \(|v|^2=(a^2+b^2)t^2\). Then \(\beta(v,J_0v)=2t^{-2}|v|^2-2t^{-4}(a^2+b^2)t^4\), which is \(0\). The restriction of \(\log t\) to a complex line through \(0\) is \(\log|\zeta|\) in a complex coordinate, which is harmonic off the origin.

**5.4.** For a continuous \(\beta\) and a bounded Borel \(f\ge0\), \(\int f\langle\beta,A\rangle d\mu=\int f\langle\beta,\ell\rangle d\lambda\). With \(\beta=F\) this gives \(\langle F,A\rangle=1\) almost everywhere; with \(\beta=R\beta'\) it gives \(\langle R\beta',A\rangle=0\), so \(A\) is invariant; with \(\beta\) of constant matrix \(\zeta\zeta^*\) in a local unitary frame it gives \(\zeta^*M(A)\zeta\ge0\) almost everywhere. Using a countable dense set of \(\zeta\) and finitely many frames, \(M(A)\ge0\) and \(\operatorname{tr}M(A)=1\) almost everywhere, which is \(A\in\mathscr K\) by Lemma 1.2 of the first lesson.

**5.5.** By the computation in the proof of Lemma 3.2, \(S(d\gamma)=-\sum_j\bigl(\sum_iA^{ij}\partial_i\nu\bigr)(\gamma_j)\), and translation invariance along \(v_j=\sum_iA^{ij}e_i\) gives \(\partial_{v_j}\nu=0\).

## References

- [OpenAI-TC] OpenAI, *Taming implies compatibility on four-manifolds*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Taming-implies-compatibility-on-four-manifolds-September-23-2026
