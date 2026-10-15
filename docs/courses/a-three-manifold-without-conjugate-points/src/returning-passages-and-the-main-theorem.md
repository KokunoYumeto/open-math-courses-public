# Returning passages and the main theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The last lesson reduced the absence of conjugate points to the returning passages: geodesics that enter the neck through a boundary torus, turn, and leave through the same torus. For these, Lemma 5.2 of [Neck passages and the index form](neck-passages-and-the-index-form.md) bounds the normal index form below by the coordinate energy, plus a boundary term controlling one component of the change \(X\) of the torus part of the field, minus a tangential term \((p^{\mathsf T}X)^2/L\). This lesson shows that the first two terms dominate the third, uniformly over all returning passages, once the parameter \(\delta\) is small. The tool is the Cauchy–Schwarz inequality in a Hilbert space adapted to the coordinate energy, combined with a quadratic minimization; a timing estimate for passages that leave the end portion supplies the margin. The lesson then assembles the estimates and proves the main theorem.

- The duration of a returning passage (Section 1).
- Duality (Section 2).
- Bounds on the dual form (Section 3).
- The returning estimate (Section 4).
- All passages and the proof of the main theorem (Section 5).

Throughout, we use the coordinates of the boundary torus through which the passage enters, with inward coordinate \(\tau\), written \(t\) below; so \(P(0)=\operatorname{diag}(1,b)\), \(P'(0)=\kappa ee^{\mathsf T}\), \(e=(1,0)^{\mathsf T}\), \(\kappa=\delta a(0)\). The returning passage occupies \([0,L]\) with the data (4.1) of [Neck passages and the index form](neck-passages-and-the-index-form.md): \(t(0)=t(L)=0\), turn at \(L/2\) with \(t_*=t(L/2)\in(0,1)\), \(v=\dot t\), \(v(0)=-v(L)=v_0>0\), \(p=Q\dot x\) constant, \(F=p^{\mathsf T}Pp\), and
\[
\begin{aligned}
&0<F'\le\kappa p_1^2\ \text{ on }[0,t_*],\\
&v_0^2=F(t_*)-F(0)\le\kappa p_1^2 .
\end{aligned} \tag{0.1}
\]
Let \(C_0\) be the constant of Lemma 2.1 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md); in these coordinates \(\|P\|\le C_0\), \(\|P'\|\le C_0\delta\) and \(|P'p|^2\le C_0\delta\,(-F'')\) on \([0,1]\).

## 1. The duration of a returning passage

**Lemma 1.1** ([OpenAI-NC, Lemma 5.2]). For every returning passage,
\[
\int_0^Lv(s)^2\,ds\le\frac{Lv_0^2}3 . \tag{1.1}
\]
If \(t_*>\frac14\), then
\[
\begin{aligned}
&4v_0\le\beta\,\kappa p_1^2L,\\
&\beta=\frac{1+e^{-9/26}}2<1 .
\end{aligned} \tag{1.2}
\]

*Proof.* On \([0,\frac L2]\), \(v\ge0\) and \(\ddot v=-\frac12F''(t)\,v\ge0\), so \(v\) is convex and lies below the chord from \(v_0\) to \(0\): \(0\le v(s)\le v_0(1-2s/L)\). Squaring and integrating gives \(\int_0^{L/2}v^2\le Lv_0^2/6\), and \(v(L-s)=-v(s)\) gives (1.1).

On the same half, \(\ddot t=-\frac12F'(t)<0\), so \(t\) is concave and \(t(s)\ge2st_*/L\). If \(t_*>\frac14\), then \(t\ge\frac18\) on \([\frac L4,\frac L2]\), and by symmetry on \([\frac L4,\frac{3L}4]\). By (0.1) of the previous lesson, \(F'(\frac18)=\delta a(\frac18)p_1^2\), and \(F'\) is nonincreasing because \(F\) is concave; so \(F'(t(s))\le\delta a(\frac18)p_1^2\) for \(\frac L4\le s\le\frac{3L}4\), and \(F'(t(s))\le F'(0)=\kappa p_1^2\) for all \(s\). Since \(\dot v=-\frac12F'(t)\) and \(v(L)-v(0)=-2v_0\),
\[
\begin{aligned}
4v_0&=\int_0^LF'(t(s))\,ds\\
&\le\frac{\delta Lp_1^2}2\bigl(a(0)+a(\tfrac18)\bigr)\\
&=\frac{\kappa p_1^2L}2\bigl(1+e^{-9/26}\bigr),
\end{aligned}
\]
using \(a(\frac18)/a(0)=e^{-9/26}\) (Exercise 5.1 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md)). \(\square\)

## 2. Duality

Apply the gauge of Lemma 5.2 of [Neck passages and the index form](neck-passages-and-the-index-form.md) and write the resulting field as \(V=(w,z)\), so \(w(0)=w(L)=0\). Put
\[
\begin{aligned}
X&=z(L)-z(0),\qquad\mu=\frac{\kappa v_0}4>0,\\
\xi&=\dot z-P'(t)p\,w .
\end{aligned}
\]
The coordinate energy and the bound (5.1) of that lesson read
\[
\begin{aligned}
&E=\int_0^L\Bigl(|\xi|_Q^2+\dot w^2\\
&\qquad-\tfrac12F''(t)w^2\Bigr)ds,\\
&I^\perp(V)\ge E+\mu\,(e^{\mathsf T}X)^2\\
&\qquad-\frac{(p^{\mathsf T}X)^2}L ,
\end{aligned} \tag{2.1}
\]
so it suffices to show
\[
\begin{aligned}
&(p^{\mathsf T}X)^2\\
&\quad\le L\bigl(E+\mu\,(e^{\mathsf T}X)^2\bigr).
\end{aligned} \tag{2.2}
\]
The boundary term controls only one component of \(X\), so the size of \(p_1\) matters.

For a constant covector \(q\in\mathbb R^2\), integrating \(\dot z=\xi+P'(t)p\,w\) gives
\[
\begin{aligned}
&q^{\mathsf T}X\\
&\quad=\int_0^Lq^{\mathsf T}\xi\,ds+\Phi_q(w),\\
&\Phi_q(w)\\
&\quad=\int_0^Lq^{\mathsf T}P'(t)p\,w\,ds .
\end{aligned} \tag{2.3}
\]
Let \(\mathcal H\) be \(L^2([0,L];\mathbb R^2)\) with the inner product \(\langle\xi_1,\xi_2\rangle_Q=\int_0^L\xi_1^{\mathsf T}Q(t(s))\xi_2\,ds\), and \(\mathcal D\) the space of absolutely continuous \(w\) on \([0,L]\) with \(w(0)=w(L)=0\) and \(\dot w\in L^2\), with
\[
\begin{aligned}
&(w_1,w_2)_{\mathcal D}\\
&\quad=\int_0^L\Bigl(\dot w_1\dot w_2-\tfrac12F''(t)\,w_1w_2\Bigr)ds .
\end{aligned}
\]
Since \(0\le-F''\) is bounded on the passage, and \(\int w^2\le L^2\int\dot w^2\) for such \(w\), this inner product is equivalent to \(\int\dot w_1\dot w_2\); so \(\mathcal D\) is a Hilbert space and \(\Phi_q\) is a bounded linear functional on it. No constant uniform in \(L\) is claimed or needed. Put
\[
\begin{aligned}
&S(q,r)\\
&\quad=\int_0^Lq^{\mathsf T}P(t(s))\,r\,ds\\
&\qquad+(\Phi_q,\Phi_r)_{\mathcal D^*},
\end{aligned} \tag{2.4}
\]
where \((\cdot,\cdot)_{\mathcal D^*}\) is the inner product of the dual space, that of the Riesz representatives. \(S\) is a symmetric bilinear form on \(\mathbb R^2\), positive definite because its first term is.

**Lemma 2.1** ([OpenAI-NC, Lemma 5.3]). For every constant covector \(q\) and every gauged field,
\[
(q^{\mathsf T}X)^2\le S(q,q)\,E . \tag{2.5}
\]
For every real \(\alpha\), with \(p_\alpha=p-\alpha e\),
\[
\begin{aligned}
&(p^{\mathsf T}X)^2\\
&\quad\le\Bigl(S(p_\alpha,p_\alpha)+\frac{\alpha^2}\mu\Bigr)\\
&\qquad\cdot\Bigl(E+\mu\,(e^{\mathsf T}X)^2\Bigr),
\end{aligned} \tag{2.6}
\]
and the smallest value of the first factor over \(\alpha\) is
\[
S(p,p)-\frac{S(p,e)^2}{S(e,e)+\mu^{-1}} . \tag{2.7}
\]

*Proof.* The pair \((\xi,w)\) lies in \(\mathcal H\oplus\mathcal D\), and its squared norm is \(E\). By (2.3), \(q^{\mathsf T}X\) is the value at \((\xi,w)\) of the functional \((\xi,w)\mapsto\int q^{\mathsf T}\xi+\Phi_q(w)\). Since \(\int q^{\mathsf T}\xi=\langle Pq,\xi\rangle_Q\), the squared norm of this functional is \(\int q^{\mathsf T}PQPq+\|\Phi_q\|_{\mathcal D^*}^2=S(q,q)\), and the Cauchy–Schwarz inequality gives (2.5). For (2.6), write \(p^{\mathsf T}X=p_\alpha^{\mathsf T}X+\alpha\,e^{\mathsf T}X\), bound the first term by (2.5), and apply the Cauchy–Schwarz inequality in \(\mathbb R^2\) to the vectors \(\bigl(\sqrt{S(p_\alpha,p_\alpha)},\,|\alpha|/\sqrt\mu\bigr)\) and \(\bigl(\sqrt E,\,\sqrt\mu\,|e^{\mathsf T}X|\bigr)\). The first factor of (2.6) is the quadratic \(S(p,p)-2\alpha S(p,e)+\alpha^2\bigl(S(e,e)+\mu^{-1}\bigr)\), whose minimum, at \(\alpha=S(p,e)/(S(e,e)+\mu^{-1})\), is (2.7). \(\square\)

So (2.2) follows once (2.7) is at most \(L\).

## 3. Bounds on the dual form

The next lemma allows an excess \(Lv_0^2\) in \(S(p,p)\); the subtracted term in (2.7) will recover at least that much. For this, \(S(e,e)\) needs only a bound proportional to \(L\), but \(S(p,e)\) must be close to \(Lp_1\) with an error proportional to \(|p_1|\): an error proportional to \(|p|\) would not suffice when \(p_1\) is small.

**Lemma 3.1** ([OpenAI-NC, Lemma 5.4]). Let \(C_e=3C_0\) and
\[
\begin{aligned}
C_m&=a(0)+\sqrt{2C_0a(0)}\\
&\quad+2\sqrt{2C_0a(0)/3} .
\end{aligned}
\]
Every returning passage satisfies
\[
\begin{aligned}
&S(p,p)\le L(1+v_0^2),\\
&S(e,e)\le C_eL,\\
&|S(p,e)-Lp_1|\\
&\quad\le C_m\,\delta L|p_1| .
\end{aligned} \tag{3.1}
\]

*Proof.* *\(S(p,p)\).* For \(w\in\mathcal D\), \(p^{\mathsf T}P'p=F'(t)=-2\dot v\), and integration by parts gives \(\Phi_p(w)=-2\int\dot vw=2\int v\dot w\). Hence \(|\Phi_p(w)|\le2\|v\|_{L^2}\|\dot w\|_{L^2}\le2\|v\|_{L^2}\|w\|_{\mathcal D}\), and \(\|\Phi_p\|_{\mathcal D^*}^2\le4\int v^2\). Since \(p^{\mathsf T}Pp=F=1-v^2\), (1.1) gives
\[
\begin{aligned}
S(p,p)&\le\int_0^L(1-v^2)+4\int_0^Lv^2\\
&=L+3\int_0^Lv^2\le L(1+v_0^2).
\end{aligned}
\]

*\(S(e,e)\).* By \(|P'p|\le\sqrt{C_0\delta(-F'')}\) and the Cauchy–Schwarz inequality in \(s\),
\[
\begin{aligned}
|\Phi_e(w)|&\le\sqrt{C_0\delta}\int_0^L\sqrt{-F''}\,|w|\,ds\\
&\le\sqrt{C_0\delta L}\Bigl(\int_0^L(-F'')w^2\Bigr)^{1/2}\\
&\le\sqrt{2C_0\delta L}\,\|w\|_{\mathcal D};
\end{aligned}
\]
this does not divide by \(-F''\) and holds where it vanishes. So \(\|\Phi_e\|_{\mathcal D^*}^2\le2C_0\delta L\), and with \(\|P\|\le C_0\) and \(\delta\le1\), \(S(e,e)\le C_0L+2C_0\delta L\le3C_0L\).

*\(S(p,e)\).* The dual term satisfies, by the two bounds just proved and (0.1),
\[
\begin{aligned}
&|(\Phi_p,\Phi_e)_{\mathcal D^*}|\\
&\quad\le2\sqrt{Lv_0^2/3}\,\sqrt{2C_0\delta L}\\
&\quad\le2\sqrt{2C_0a(0)/3}\;\delta L|p_1| ,
\end{aligned}
\]
since \(v_0^2\le\kappa p_1^2=\delta a(0)p_1^2\). For the other term, fix \(t\in[0,t_*]\) and put \(D(t)=P'(0)-P'(t)\). Concavity of \(P\) gives \(D(t)\succeq0\), and \(\|D(t)\|\le2C_0\delta\); by (0.1), \(0\le p^{\mathsf T}D(t)p=\kappa p_1^2-F'(t)\le\kappa p_1^2\). The Cauchy–Schwarz inequality for the positive semidefinite form \(D(t)\) gives
\[
\begin{aligned}
|e^{\mathsf T}D(t)p|^2&\le(e^{\mathsf T}D(t)e)(p^{\mathsf T}D(t)p)\\
&\le2C_0a(0)\,\delta^2p_1^2 ,
\end{aligned}
\]
also when \(D(t)\) is singular. Since \(e^{\mathsf T}P'(0)p=\kappa p_1\), \(|e^{\mathsf T}P'(t)p|\le(a(0)+\sqrt{2C_0a(0)})\delta|p_1|\). Integrating from \(0\) to \(t\le t_*<1\), and using \(e^{\mathsf T}P(0)p=(P(0)e)^{\mathsf T}p=p_1\), gives the same bound for \(|e^{\mathsf T}P(t)p-p_1|\). Integrating over \(s\in[0,L]\) and adding the dual term proves the third bound. \(\square\)

All constants depend only on the fixed cutoff \(\chi\); they do not depend on \(p\), \(L\), \(v_0\), \(t_*\) or on the boundary torus.

## 4. The returning estimate

Fix \(\delta\) with
\[
\begin{aligned}
&0<\delta\le\delta_0,\qquad\delta\le\frac1{2C_m},\\
&\delta\le\frac{1-\beta}{2C_m+C_ea(0)},
\end{aligned} \tag{4.1}
\]
where \(\delta_0\) is the constant of Lemma 2.1 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md).

**Proposition 4.1** ([OpenAI-NC, Proposition 5.1]). With \(\delta\) as in (4.1), every returning passage of the neck satisfies \(I^\perp_{[0,L]}(V)\ge0\) for every smooth field \(V\) along its closure, with no condition on the values of \(V\) at \(0\) and \(L\). The same \(\delta\) serves both boundary tori and all unit-speed returning geodesics.

*Proof.* If \(t_*\le\frac14\), this is Lemma 5.1 of [Neck passages and the index form](neck-passages-and-the-index-form.md). Let \(t_*>\frac14\) and apply the gauge; by Lemma 2.1 and (2.1) it suffices to show that (2.7) is at most \(L\), and by the first bound of (3.1) it suffices that the subtracted term in (2.7) is at least \(Lv_0^2\).

Put \(r=v_0^2/p_1^2>0\). By (0.1), \(r\le\kappa=a(0)\delta\). By (1.2) and \(\mu=\kappa v_0/4\), \(L\mu=\frac{\kappa Lv_0}4\ge\frac{v_0^2}{\beta p_1^2}=\frac r\beta\). Since \(C_m\delta\le\frac12\), the third bound of (3.1) gives \(|S(p,e)|\ge L|p_1|(1-C_m\delta)\ge0\). Using the second bound and the fact that \(x\mapsto x/(1+C_ex)\) is increasing for \(x\ge0\),
\[
\begin{aligned}
&\frac{S(p,e)^2}{S(e,e)+\mu^{-1}}\\
&\quad\ge Lp_1^2(1-C_m\delta)^2\,\frac{L\mu}{1+C_eL\mu}\\
&\quad\ge Lp_1^2(1-C_m\delta)^2\,\frac{r/\beta}{1+C_er/\beta}\\
&\quad=Lv_0^2\,\frac{(1-C_m\delta)^2}{\beta+C_er}\\
&\quad\ge Lv_0^2\,\frac{(1-C_m\delta)^2}{\beta+C_ea(0)\delta}.
\end{aligned}
\]
By (4.1), \((1-C_m\delta)^2\ge1-2C_m\delta\ge\beta+C_ea(0)\delta\), so the last expression is at least \(Lv_0^2\). Hence (2.7) is at most \(L(1+v_0^2)-Lv_0^2=L\), (2.6) gives (2.2), and (2.1) gives \(I^\perp(V)\ge0\) for the gauged field, hence for the original field by tangential invariance. All denominators are positive on an actual returning passage (\(L>0\), \(v_0>0\), \(p_1\ne0\)), and (4.1) involves none of these quantities. So the estimate holds for arbitrarily shallow and arbitrarily long excursions, with no limiting argument. \(\square\)

## 5. All passages and the proof of the main theorem

**Proposition 5.1** ([OpenAI-NC, Proposition 5.5]). Fix \(\delta\) as in (4.1) and periods as in Section 4 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md). Let \(\gamma\) be a unit-speed geodesic of the resulting closed manifold \(M\). For every neck passage \(J\) of \(\gamma\) and every smooth field \(V\) along \(\gamma\) vanishing outside a compact set,
\[
I_J^\perp(V)\ge0,\qquad I_J(V)\ge0 .
\]

*Proof.* Lemma 4.1 of [Neck passages and the index form](neck-passages-and-the-index-form.md) lists every possible passage. Lemma 5.1 there handles the passage \(\mathbb R\), the passages on which \(v\) never vanishes, and the returning passages with \(t_*\le\frac14\); Proposition 4.1 handles the remaining returning passages. These results apply to the restriction of \(V\), with arbitrary values at finite end points and zero values far out at infinite ends, and they use the same \(\delta\) in both end frames. Finally \(I_J(V)=I_J^\perp(V)+\int_J\dot q_V^2\,ds\ge0\). \(\square\)

**Theorem 5.2** ([OpenAI-NC, Theorem 1.1]; Theorem 3.1 of [Conjugate points and index forms](conjugate-points-and-index-forms.md)). There is a closed connected orientable smooth three-manifold \(M\) with a \(C^\infty\) Riemannian metric without conjugate points, such that \(M\) admits no \(C^\infty\) Riemannian metric whose sectional curvature is everywhere at most zero.

*Proof.* Let \(M\) be the manifold of [The manifold and its fundamental group](the-manifold-and-its-fundamental-group.md), built with the cores of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md) for \(\delta\) as in (4.1), some \(B_2\in(0,1]\) and \(B_1=\delta^2B_2\); it is closed, connected and orientable. By Proposition 4.1 of the latter lesson it carries a smooth metric, complete because \(M\) is compact, whose sectional curvatures are nonpositive at every point outside the open neck \(U\). By Proposition 5.1, every visit of every unit-speed geodesic to \(U\) satisfies the hypothesis (2.3) of Proposition 2.3 of [Conjugate points and index forms](conjugate-points-and-index-forms.md), which therefore shows that the metric has no conjugate points. By Corollary 4.2 of [Axes, shifts and the two-piece obstruction](axes-shifts-and-the-two-piece-obstruction.md), \(M\) admits no metric of nonpositive sectional curvature. \(\square\)

The metric of Theorem 5.2 must have a positive sectional curvature somewhere, since otherwise it would be a metric of nonpositive curvature on \(M\); by Proposition 4.1 of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md), every such point lies in the middle part \(\frac14<t<\frac34\) of the neck. There the absence of conjugate points comes from the concavity of the cometric, through the coordinate second variation and the boundary terms, and not from a sign of the curvature.

## 6. Exercises

**6.1.** Show that \(\int_0^{L/2}v_0^2(1-2s/L)^2\,ds=Lv_0^2/6\).

**6.2.** Show that \(\int_0^Lw^2\le L^2\int_0^L\dot w^2\) for absolutely continuous \(w\) with \(w(0)=0\) and \(\dot w\in L^2\), and deduce that \((\cdot,\cdot)_{\mathcal D}\) is an inner product equivalent to \(\int\dot w_1\dot w_2\).

**6.3.** Show that \(x\mapsto x/(1+C_ex)\) is increasing on \([0,\infty)\) for \(C_e>0\), and that \(1-2C_m\delta\ge\beta+C_ea(0)\delta\) is equivalent to \(\delta\le(1-\beta)/(2C_m+C_ea(0))\).

**6.4.** Show that, without the boundary term (\(\mu=0\)), Lemma 2.1 would only give \((p^{\mathsf T}X)^2\le S(p,p)E\le L(1+v_0^2)E\), which does not imply (2.2). Which feature of the boundary term makes up the difference?

**6.5.** Check Proposition 4.1 in a returning passage for which the field is \(V=(0,z)\) with \(z\) constant: compute \(E\), \(X\) and \(I^\perp(V)\) directly.

## 7. Solutions

**6.1.** With \(u=1-2s/L\), \(ds=-\frac L2du\), the integral is \(v_0^2\frac L2\int_0^1u^2\,du=\frac{Lv_0^2}6\).

**6.2.** \(w(s)=\int_0^s\dot w\), so \(w(s)^2\le s\int_0^L\dot w^2\le L\int_0^L\dot w^2\); integrate over \([0,L]\). Then \(\int\dot w^2\le(w,w)_{\mathcal D}\), and \((w,w)_{\mathcal D}\le(1+\frac12L^2\sup|F''|)\int\dot w^2\).

**6.3.** The derivative is \(1/(1+C_ex)^2>0\). The second claim is a rearrangement.

**6.4.** \(S(p,p)\) may exceed \(L\) by \(Lv_0^2\); the bound (2.2) needs the factor \(L\) itself. The boundary term \(\mu(e^{\mathsf T}X)^2\) with \(\mu=\kappa v_0/4\) and the timing margin \(\beta<1\) recover the excess, because the component of \(p\) along \(e\) dominates \(S(p,e)\) up to an error \(C_m\delta L|p_1|\).

**6.5.** For \(V=(0,z)\) with \(z\) constant, \(w=0\), \(\xi=0\), \(E=0\), \(X=0\); the gauge leaves \(V\) unchanged except for a tangential term, \(\langle V,T\rangle=p^{\mathsf T}z\) is constant, and the identity in (5.1) of [Neck passages and the index form](neck-passages-and-the-index-form.md) gives \(I^\perp(V)=\frac{\kappa v_0}2\cdot2z_1^2=\kappa v_0z_1^2\ge0\).

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Section 5 (Proposition 5.1, Lemmas 5.2–5.4, Proposition 5.5) and Section 6 (proof of Theorem 1.1). https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
