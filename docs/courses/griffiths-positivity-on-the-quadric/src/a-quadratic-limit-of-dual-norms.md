# A quadratic limit of dual norms

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Suppose that the bundles \(E_m=f_m^*G\otimes P\) of Hermitian metrics and Griffiths positivity carry strictly Griffiths-positive metrics for infinitely many \(m\). This lesson extracts from them a single object on the total space of \(F=G^\vee\): a nonzero, nonnegative plurisubharmonic function that is a Hermitian quadratic form on every fiber. The power maps make the twist by \(P\) disappear in the limit: averaging the dual norms over the fibers of \(f_m\) produces functions on \(F\) that differ from quadratic forms on \(F\) only by a factor that tends to one.

The proof needs care at two places. The limit must not vanish, and it must remain quadratic and plurisubharmonic at every point of the base, not only almost everywhere; the next lesson evaluates it along the divisor \(D\), which has measure zero.

- A removable singularity lemma for continuous functions (Lemma 1.1).
- Traces of dual norms along the power maps (Section 2).
- Normalization and a measurable limit (Section 3).
- The limit does not vanish (Section 4).
- A plurisubharmonic representative that is quadratic on every fiber (Section 5, Proposition 5.1).

The lesson follows [OpenAI-GP, Section 4]. The facts on plurisubharmonic functions are those of the lesson [Compactness and complex-line positivity](course:AN-01/reader/AN01-U024) (course *Distributions, kernels and analytic singularities*): plurisubharmonic functions are locally integrable and satisfy the submean inequality on balls; a real distribution with nonnegative Levi forms has exactly one plurisubharmonic representative, and its averages with a fixed smooth radial kernel decrease to it as the radius decreases (Theorem 1.1 there); decreasing limits of plurisubharmonic functions are plurisubharmonic or identically \(-\infty\) (Proposition 1.2 there). Composition with holomorphic maps preserves plurisubharmonicity.

## 1. A removable singularity lemma

**Lemma 1.1.** Let \(\Omega\subseteq\mathbb C^N\) be open, \(\varphi\) holomorphic on \(\Omega\) and not identically zero on any component, and \(u\) a continuous real function on \(\Omega\) that is plurisubharmonic on \(\Omega\setminus\{\varphi=0\}\). Then \(u\) is plurisubharmonic on \(\Omega\).

**Proof.** It suffices to show that the restriction of \(u\) to every complex line is subharmonic, that is, for every affine map \(\ell(\zeta)=a+\zeta c\) and every closed disk \(\Delta\) in \(\ell^{-1}(\Omega)\), \(u\circ\ell\) is at most the harmonic extension of its boundary values on \(\Delta\).

*Lines not inside the zero set.* If \(\varphi\circ\ell\) is not identically zero on the component containing \(\Delta\), its zeros in \(\Delta\) are finitely many points \(\zeta_1,\dots,\zeta_k\), and \(u\circ\ell\) is subharmonic near \(\Delta\) except at these points. Let \(H\) be harmonic near \(\Delta\) with \(u\circ\ell\le H\) on \(\partial\Delta\), and \(\varepsilon>0\). The function \(w=u\circ\ell-H+\varepsilon\sum_i\log(|\zeta-\zeta_i|/R)\), with \(R\) the diameter of \(\Delta\), is subharmonic on \(\Delta\) minus the points, at most \(0\) on \(\partial\Delta\), and tends to \(-\infty\) at each \(\zeta_i\). By the maximum principle \(w\le0\) on \(\Delta\) minus the points. Letting \(\varepsilon\to0\) gives \(u\circ\ell\le H\) there, and at the points by continuity.

*Lines inside the zero set.* If \(\varphi\circ\ell\equiv0\) near \(\Delta\), choose vectors \(t\to0\) such that \(\varphi\circ\ell_t\not\equiv0\) for \(\ell_t(\zeta)=a+t+\zeta c\); they exist because the zero set of \(\varphi\) has no interior, while the lines \(\ell_t(\Delta)\) for \(t\) in a small ball fill an open set. By the first case each \(u\circ\ell_t\) satisfies the submean inequality on circles in \(\Delta\), and \(u\circ\ell_t\to u\circ\ell\) uniformly on \(\Delta\) by continuity of \(u\). The submean inequalities pass to the limit. \(\blacksquare\)

## 2. Traces along the power maps

Let \(G\) be any holomorphic vector bundle of rank \(r\ge1\) on \(S=\mathbb P^1\times\mathbb P^1\), and \(F=G^\vee\). Suppose that for an unbounded sequence of integers \(m\) the bundle \(f_m^*G\otimes P\) has a smooth strictly Griffiths-positive metric. Its dual metric \(\|\cdot\|_m\) lives on
\[
(f_m^*G\otimes P)^\vee=f_m^*F\otimes P^{-1},
\]
and its squared norm is plurisubharmonic on the total space by the dual norm criterion (Proposition 3.1 of Hermitian metrics and Griffiths positivity). Fix holomorphic isomorphisms \(f_m^*P^{-1}\cong P^{-m}\).

**The trace.** Let \(t\) be a nonvanishing holomorphic section of \(P^{-1}\) over an open set \(U\subseteq S\). For \(x\in U\) and \(v\in F_x\) put
\[
\begin{aligned}
q_{m,t}(x,v)&=\frac1{m^2}\sum_{y\in f_m^{-1}(x)}\sigma(y),\\
\sigma(y)&=\bigl\|v\otimes(f_m^*t)^{1/m}(y)\bigr\|_{m,y}^2 ,
\end{aligned}
\]
where the sum runs over the \(m^2\) preimages counted with multiplicity, \(v\) is viewed in \((f_m^*F)_y=F_x\), and \((f_m^*t)^{1/m}\) is a local \(m\)th root near \(y\) of the section \(f_m^*t\) of \(f_m^*P^{-1}\cong P^{-m}\): in a local frame \(e\) of \(P^{-1}\) near \(y\), \(f_m^*t=\eta\,e^m\) with \(\eta\) holomorphic and nonvanishing, and \(\exp(\frac1m\log\eta)\,e\) is a root. Two roots differ by an \(m\)th root of unity, which does not change the squared norm. So \(q_{m,t}\) is well defined, and on each fiber it is a positive definite Hermitian quadratic form in \(v\).

**Plurisubharmonicity.** Off the four coordinate lines \(\{z_0z_1=0\}\times\mathbb P^1\) and \(\mathbb P^1\times\{w_0w_1=0\}\), over which \(f_m\) is branched, the local inverse branches \(y(x)\) of \(f_m\) are holomorphic, and each summand is the composite of the plurisubharmonic squared norm with the holomorphic map \((x,v)\mapsto(y(x),v\otimes(f_m^*t)^{1/m}(y(x)))\) into the total space of \(f_m^*F\otimes P^{-1}\). So \(q_{m,t}\) is plurisubharmonic there. The unordered family of the roots of \(y^m=x\), counted with multiplicity, varies continuously with \(x\), also where roots coalesce; so \(q_{m,t}\) is continuous on the total space of \(F|_U\). In an affine chart of the total space, the preimage of the branch locus is contained in the zero set of a holomorphic function that is not identically zero (the product of the two affine coordinates of the base that vanish on the coordinate lines in the chart). By Lemma 1.1, \(q_{m,t}\) is plurisubharmonic on the total space of \(F|_U\).

**The frame law.** If \(t'=gt\) with \(g\) holomorphic and nonvanishing, then \(f_m^*t'=(g\circ f_m)f_m^*t\), the roots differ by a factor \(g(x)^{1/m}\), and
\[
q_{m,t'}(x,v)=|g(x)|^{2/m}\,q_{m,t}(x,v) .
\]

## 3. Normalization and a measurable limit

Choose smooth Hermitian metrics \(|\cdot|_0\) on \(F\) and on \(P^{-1}\). By the frame law,
\[
N_m(x,v)=q_{m,t}(x,v)\,|t(x)|_0^{-2/m}
\]
does not depend on \(t\), so it is a continuous function on the total space of \(F\), positive definite and quadratic on each fiber. Multiplying the dual metric \(\|\cdot\|_m\) by a positive constant changes neither the curvature nor the plurisubharmonicity, so we may assume, using the compactness of the unit sphere bundle of \(|\cdot|_0\),
\[
\max\{N_m(x,v):x\in S,\ |v|_0=1\}=1 .
\]
By homogeneity,
\[
0\le q_{m,t}(x,v)\le|t(x)|_0^{2/m}\,|v|_0^2 .
\]

**A weak limit.** Over a chart \(U\) with a holomorphic frame of \(F\), write \(q_{m,t}(x,v)=v^*H_m(x)v\) with continuous positive definite matrices \(H_m\). On every compact subset of \(U\) the \(H_m\) are uniformly bounded, since \(|t|_0^{2/m}\le\max(1,\max|t|_0^2)\) there. Countably many charts with frames and sections \(t\) cover \(S\), each exhausted by countably many compact sets \(K\). A bounded sequence in the Hilbert space \(L^2(K)\) has a weakly convergent subsequence (Exercise 4, with Theorems 3.1 and 7.2, of [Weak topologies, Tychonoff, Banach–Alaoglu, Mazur, bipolars, Krein–Milman and Eberlein–Šmulian](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian), course *Foundations of von Neumann algebras*). A diagonal subsequence gives, on every chart, weak limits \(H\) of the coefficient matrices, that is, limits against every square-integrable test matrix on every compact set. Pairing with nonnegative test functions shows that the limits satisfy the same bounds; testing \(c^*Hc\) for \(c\in(\mathbb Q+i\mathbb Q)^r\) shows that \(H\) is Hermitian and positive semidefinite outside one null set.

**The transition law.** Let \(v=T(x)w\) be a holomorphic change of the frame of \(F\) and \(t'=gt\). Then the coefficient matrices satisfy \(H'_m=|g|^{2/m}T^*H_mT\). On a compact subset \(K\) of the overlap, \(\sup_K\bigl||g|^{2/m}-1\bigr|\to0\), and the \(H_m\) are uniformly bounded there; so in the limit the factor disappears, and \(H'=T^*HT\) almost everywhere. The measurable limits form a measurable field of positive semidefinite Hermitian forms on \(F\), with the untwisted transition law.

## 4. The limit does not vanish

Choose \((x_m,v_m)\) with \(|v_m|_0=1\) and \(N_m(x_m,v_m)=1\). After a further subsequence, \((x_m,v_m)\to(x_*,v_*)\) in the compact unit sphere bundle; the weak limits are unchanged. In one chart around \(x_*\) with a frame of \(F\) and a section \(t\), let \(c_m\to c\) be the coordinate vectors of \(v_m\), so \(c\ne0\). With a bound \(\|H_m\|\le C\) near \(x_*\),
\[
\begin{aligned}
&\bigl|c^*H_m(x_m)c-c_m^*H_m(x_m)c_m\bigr|\\
&\quad\le C\,|c-c_m|\,(|c|+|c_m|)\to0 ,
\end{aligned}
\]
while \(c_m^*H_m(x_m)c_m=|t(x_m)|_0^{2/m}\to1\). The function \(u_m(x)=c^*H_m(x)c=q_{m,t}(x,c)\) is plurisubharmonic, as the composite of \(q_{m,t}\) with the holomorphic section \(x\mapsto(x,c)\), and \(u_m(x_m)\ge\frac12\) for large \(m\). Choose \(\varrho>0\) with the ball \(B(x_*,4\varrho)\) inside the chart, and a smooth function \(\chi\ge0\) equal to one on \(B(x_*,2\varrho)\) and supported in \(B(x_*,3\varrho)\). For large \(m\), \(B(x_m,\varrho)\subseteq B(x_*,2\varrho)\), and the submean inequality gives
\[
\begin{aligned}
\int\chi\,c^*H_mc\,dx&\ge\int_{B(x_m,\varrho)}u_m\,dx\\
&\ge\tfrac12\operatorname{Vol}B(0,\varrho) .
\end{aligned}
\]
The left side tends to \(\int\chi\,c^*Hc\,dx\), so \(H\) is not zero as a measurable form.

## 5. A representative that is quadratic on every fiber

Pointwise limits can lose plurisubharmonicity. In one base variable, the trace of \((1+|y|^2)|v|^2\) along \(x=y^m\) is \((1+|x|^{2/m})|v|^2\), whose pointwise limit is \(|v|^2\) at \(x=0\) and \(2|v|^2\) elsewhere; the plurisubharmonic representative is \(2|v|^2\) everywhere (Exercise 6.1). The representative is recovered by convolution.

Work in a chart \(U\subseteq\mathbb C^2\) of the base with a frame of \(F\). Let \(\rho\ge0\) be a smooth radial function on \(\mathbb C^2\) supported in the unit ball with integral one, \(\rho_\delta(y)=\delta^{-4}\rho(y/\delta)\), and on the set of points at distance more than \(\delta\) from the complement of \(U\) put
\[
H_\delta=H*\rho_\delta,\qquad q_\delta(x,v)=v^*H_\delta(x)v .
\]

*Each \(q_\delta\) is plurisubharmonic.* The functions \(q_{m,\delta}(x,v)=\int q_{m,t}(x-y,v)\rho_\delta(y)\,dy\) are plurisubharmonic in \((x,v)\): each translate \((x,v)\mapsto(x-y,v)\) is holomorphic, and the average has nonnegative weights. As \(m\to\infty\), the coefficients of \(q_{m,\delta}\) and all their derivatives converge at every point to those of \(q_\delta\), because they are pairings of \(H_m\) with fixed translated derivatives of \(\rho_\delta\). So the complex Hessians converge, and \(q_\delta\) is smooth and plurisubharmonic, with \(0\le q_\delta(x,v)\le C|v|^2\) on smaller sets.

*Monotonicity.* For a subharmonic function \(w\) on a ball of \(\mathbb R^4\), polar coordinates express \((w*\rho_\delta)(x)\) as \(|S^3|\int_0^1M_w(x,\delta s)\,\phi(s)s^3\,ds\), where \(\rho(y)=\phi(|y|)\) and \(M_w(x,r)\) is the mean of \(w\) on the sphere of radius \(r\) about \(x\), nondecreasing in \(r\). So \(w*\rho_\delta\) is nondecreasing in \(\delta\). Apply this to \(w(x)=q_{m,t}(x,v)\) for fixed \(v\), and let \(m\to\infty\) at two fixed radii: \(H_{\delta_1}(x)\le H_{\delta_2}(x)\) for \(\delta_1<\delta_2\), as Hermitian forms.

*The limit.* As \(\delta\downarrow0\), \(q_\delta\) decreases to a function \(q_U\ge0\), which is plurisubharmonic (Proposition 1.2 of the lesson on complex-line positivity) and finite. At every point \(x\), the entries of \(H_\delta(x)\) converge: they are determined by finitely many values of the quadratic form,
\[
\begin{aligned}
2\operatorname{Re}(H_\delta)_{jk}&=q_\delta(x,e_j+e_k)\\
&\quad-q_\delta(x,e_j)-q_\delta(x,e_k),\\
2\operatorname{Im}(H_\delta)_{jk}&=q_\delta(x,e_j)+q_\delta(x,e_k)\\
&\quad-q_\delta(x,e_j+ie_k),
\end{aligned}
\]
each of which converges. So \(H_\delta(x)\to\widehat H_U(x)\), a positive semidefinite Hermitian matrix, and \(q_U(x,v)=v^*\widehat H_U(x)v\) for every \(v\). At almost every \(x\), \(\widehat H_U(x)=H(x)\), by the convergence of averages at Lebesgue points.

*Gluing.* On an overlap of two charts, the two functions \(q_U\) agree at almost every point of the total space: their matrices agree almost everywhere by the transition law, and Fubini's theorem passes this to the total space. Both are plurisubharmonic and locally bounded, and a plurisubharmonic function is determined by its values almost everywhere, being the limit of its averages over small balls (Theorem 1.1 of the lesson on complex-line positivity). So they agree everywhere.

**Proposition 5.1** (quadratic limit; [OpenAI-GP, Proposition 4.1]). Let \(G\) be a holomorphic vector bundle of positive rank on \(S\), \(F=G^\vee\), and suppose that \(f_m^*G\otimes P\) has a smooth strictly Griffiths-positive metric for infinitely many \(m\). Then there is a function \(q\colon F\to[0,\infty)\), plurisubharmonic on the total space and not identically zero, such that for every \(x\in S\) there is a positive semidefinite Hermitian form \(H_x\) on \(F_x\) with \(q(x,v)=H_x(v,v)\) for all \(v\in F_x\).

**Proof.** Sections 2 to 5: the glued function \(q\) is plurisubharmonic, quadratic on every fiber with a positive semidefinite form, and represents the measurable limit almost everywhere; by Section 4 that limit is not zero, so \(q\not\equiv0\). \(\blacksquare\)

No convergence of restrictions to a curve is claimed. The next lesson uses only this single, everywhere-defined function.

## 6. Exercises

**6.1.** Verify the example of Section 5: the trace of \((1+|y|^2)|v|^2\) along \(x=y^m\) in one variable, its pointwise limit, and its plurisubharmonic representative.

**6.2.** Let a line bundle over a domain in \(\mathbb C\) have a smooth metric with squared norm \(e^{-\varphi(z)}|w|^2\) in a holomorphic frame. Show that the squared norm is plurisubharmonic on the total space exactly when \(-\varphi\) is subharmonic.

**6.3.** Show that a nonnegative plurisubharmonic function that vanishes almost everywhere vanishes everywhere.

**6.4.** Prove the polarization identities of Section 5 for a Hermitian matrix \(H\) and the form \(q(v)=v^*Hv\).

**6.5.** Show that for a subharmonic function \(w\), the spherical means \(M_w(x,r)\) are nondecreasing in \(r\), using the submean inequality and the maximum principle.

## 7. Solutions

**6.1.** The preimages of \(x\ne0\) are the \(m\) roots \(y\) with \(|y|^2=|x|^{2/m}\), so the trace, normalized by \(1/m\), is \((1+|x|^{2/m})|v|^2\). For \(x\ne0\), \(|x|^{2/m}\to1\), and at \(x=0\) the value is \(|v|^2\): the pointwise limit is \(2|v|^2\) off \(0\) and \(|v|^2\) at \(0\). It is not upper semicontinuous at \(0\), so it is not subharmonic. Its averages over small disks are \(2|v|^2\), and the plurisubharmonic representative, the limit of these averages, is \(2|v|^2\) everywhere.

**6.2.** The function \(e^{-\varphi(z)}|w|^2\) has, at a point with \(w=1\) after scaling, the complex Hessian \(\begin{pmatrix}(e^{-\varphi})_{z\bar z}&(e^{-\varphi})_z\\ (e^{-\varphi})_{\bar z}&e^{-\varphi}\end{pmatrix}\) in the variables \((z,w)\); at points with \(w\ne1\) it is the same up to a positive factor and a linear change of variables. It is positive semidefinite exactly when its determinant is nonnegative (the lower right entry is positive), that is, when \(e^{-\varphi}(e^{-\varphi})_{z\bar z}-|(e^{-\varphi})_z|^2\ge0\). Dividing by \(e^{-2\varphi}\), this is \((\log e^{-\varphi})_{z\bar z}=-\varphi_{z\bar z}\ge0\).

**6.3.** By the submean inequality, the value at each point is at most the average over small balls, which is zero; and the value is nonnegative.

**6.4.** \(q(e_j+e_k)=H_{jj}+H_{kk}+2\operatorname{Re}H_{jk}\), and \(q(e_j+ie_k)=H_{jj}+H_{kk}+2\operatorname{Re}(iH_{jk})\), which is \(H_{jj}+H_{kk}-2\operatorname{Im}H_{jk}\), with \(H_{jk}=e_j^*He_k\).

**6.5.** Let \(r_1<r_2\) and \(h\) be the harmonic function on the ball of radius \(r_2\) equal to \(w\) on its boundary (after approximating \(w\) from above by continuous functions). Then \(w\le h\) inside, so \(M_w(x,r_1)\le M_h(x,r_1)=h(x)\) and \(h(x)=M_h(x,r_2)=M_w(x,r_2)\), using the mean value property of harmonic functions.

## References

- [OpenAI-GP] OpenAI, *Ample rank-two bundles on the quadric surface without Griffiths-positive metrics*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026
