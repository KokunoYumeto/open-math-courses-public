# Realization in a polar product

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson assembles the proof. For a strip body \(K=\{x:|\langle b_j,x\rangle|\le1\}\) and a large integer \(k\), the functions \(f_j(z)=g(\langle b_j,z\rangle)^k\) satisfy the hypotheses of Theorem 4.1, so the domain \(V=\{\sum_j|f_j|^2<1\}\) with the form \(\omega=dd^c(|z|^2+\sum_j|f_j|^2)\) contains balls of every capacity below \(\pi k\). An explicit map, whose momentum coordinates are the slice integrals of [The uniform slice estimate](the-uniform-slice-estimate.md), carries \((V,\omega)\) symplectically into \(\operatorname{int}K\times S\operatorname{int}K^\circ\) with \(S\) close to \(\pi k/4\) (Proposition 7.1). Rescaling gives balls of every capacity below \(4\); the polar approximation of [Polar bodies and the volume product](polar-bodies-and-the-volume-product.md) passes to arbitrary bodies, and volume preservation gives the Mahler inequality. The construction is OpenAI's [OpenAI-SB, Sections 4 and 5].

## 1. Strip bodies

**Proposition 7.1.** Let \(n\ge2\), let \(b_1,\dots,b_m\in\mathbf R^n\) span \(\mathbf R^n\), and let \(K\) be their strip body. For every \(0<c<4\) there is an injective symplectic map \(B^{2n}(c)\to\operatorname{int}K\times\operatorname{int}K^\circ\), a diffeomorphism onto an open subset.

**Proof.** *Step 1: the holomorphic functions.* Let \(F:\mathbb D\to D\) and \(g=F^{-1}\) be the maps of [A planar conformal map](a-planar-conformal-map.md). Write \(\ell_j(z)=\langle b_j,z\rangle=\sum_ib_{ji}z_i\) and
\[
\Omega=\{z\in\mathbf C^n:\ \ell_j(z)\in D\text{ for every }j\}.
\]
This is an open set containing \(0\). The spanning condition makes the complex-linear map \(z\mapsto(\ell_j(z))_j\) injective, so \(|z|\le C_b\max_j|\ell_j(z)|\) for a constant \(C_b\); since \(D\) is bounded, so is \(\Omega\). Neither set depends on \(k\).

For an integer \(k\ge2\) put
\[
\begin{gathered}
f_j=(g\circ\ell_j)^k,\quad\tau=\sum_{j=1}^m|f_j|^2,\\
V=\{z\in\Omega:\tau<1\},\\
\omega=dd^c(|z|^2+\tau).
\end{gathered}
\]
The map \(f=(f_1,\dots,f_m)\) is holomorphic on \(\Omega\). Since \(g\) vanishes only at \(0\), the common zeros of the \(f_j\) are the points with all \(\ell_j(z)=0\), that is, only \(z=0\). Near \(0\), \(|g(\zeta)|\le C|\zeta|\), so \(|f(z)|\le C'|z|^k\). For \(0<s<1\), every point of \(\{\tau\le s\}\) has \(|g(\ell_j(z))|\le s^{1/(2k)}\), that is, \(\ell_j(z)\in F(\{|w|\le s^{1/(2k)}\})\), a compact subset of \(D\), for every \(j\). Hence this sublevel set is bounded, and a limit of a sequence in it has all \(\ell_j\)-values in the same compact subsets of \(D\), so it lies in \(\Omega\) and satisfies \(\tau\le s\). Thus the sublevel sets are compact, and Theorem 4.1 gives, for every \(c'<\pi k\), an injective symplectic map \(E:B^{2n}(c')\to(V,\omega)\).

*Step 2: the realization map.* Write \(z=u+ix\), and for \(z\in V\) put \(v_j=\langle b_j,u\rangle\), \(t_j=\langle b_j,x\rangle\), so that \(\ell_j(z)=v_j+it_j\in D\). Define \(\Phi:V\to\mathbf R^n_q\times\mathbf R^n_p\) by
\[
q=x,\qquad p=-u-\sum_{j=1}^mJ_k(v_j,t_j)\,b_j .
\]
It is smooth by Proposition 6.1. Since \(\omega_0=\sum_ldq_l\wedge dp_l\),
\[
\begin{aligned}
\Phi^*\omega_0&=\sum_ldx_l\wedge(-du_l)\\
&\quad-\sum_jdt_j\wedge dJ_k(v_j,t_j)\\
&=\sum_ldu_l\wedge dx_l\\
&\quad+\sum_j\partial_vJ_k(v_j,t_j)\,dv_j\wedge dt_j,
\end{aligned}
\]
because \(dJ_k(v_j,t_j)=\partial_vJ_k\,dv_j+\partial_tJ_k\,dt_j\) and \(dt_j\wedge dt_j=0\). By Proposition 6.1, \(\partial_vJ_k=k^2|g|^{2k-2}|g'|^2=|(g^k)'|^2\), evaluated at \(\ell_j(z)\); by Lemma 3.8 with \(\phi=g^k\), the \(j\)-th term is \(dd^c|f_j|^2\). Hence
\[
\Phi^*\omega_0=dd^c|z|^2+\sum_jdd^c|f_j|^2=\omega .
\]

The map \(\Phi\) is injective. Equal images have equal \(q\), hence the same \(x\). Let \(u_1,u_2\) be two real parts at this \(x\), with momenta \(p_1,p_2\), and put \(v_{ji}=\langle b_j,u_i\rangle\). Both \(v_{j1}\) and \(v_{j2}\) lie in the horizontal slice of \(D\) at height \(t_j\), an interval on which \(J_k(\cdot,t_j)\) is nondecreasing. Therefore
\[
\begin{aligned}
&\langle p_2-p_1,u_2-u_1\rangle=-|u_2-u_1|^2\\
&\quad-\sum_j\bigl(J_k(v_{j2},t_j)-J_k(v_{j1},t_j)\bigr)\\
&\qquad\cdot(v_{j2}-v_{j1})\\
&\le-|u_2-u_1|^2,
\end{aligned}
\]
and \(p_1=p_2\) forces \(u_1=u_2\). The form \(\omega\) is nondegenerate, so \(D\Phi\) is invertible everywhere (Exercise 7.1), and by Lemma 2.2, \(\Phi\) is a diffeomorphism of \(V\) onto an open set, with \(\Phi^*\omega_0=\omega\).

*Step 3: the momenta lie in a dilate of the polar body.* Every point of \(D\) has imaginary part in \((-1,1)\), so \(|\langle b_j,q\rangle|=|t_j|<1\) for every \(j\), and \(q\in\operatorname{int}K\). For the momenta use the support function \(h_K\): \(h_K(\pm b_j)\le1\) by the definition of \(K\), and \(\operatorname{int}K^\circ=\{h_K<1\}\) by Lemma 1.1. Since \(\Omega\) is bounded, \(h_K(-u)\le C_K\) on \(\Omega\) for a constant \(C_K\) independent of \(k\). By subadditivity and positive homogeneity of \(h_K\), and Proposition 6.1,
\[
\begin{aligned}
\frac{h_K(p)}k&\le\frac{C_K}k+\sum_j\frac{|J_k(v_j,t_j)|}k\\
&\le\frac{C_K}k+\frac\pi4\sum_j|g(\ell_j(z))|^{2k}\\
&\quad+m\varepsilon_k\\
&=\frac{C_K}k+\frac\pi4\tau(z)+m\varepsilon_k .
\end{aligned}
\]
Let \(\eta>0\). Since \(m\) and \(C_K\) do not depend on \(k\) and \(\varepsilon_k\to0\), for all large \(k\) we have \(C_K/k+m\varepsilon_k<\eta\pi/4\); then \(\tau<1\) on \(V\) gives \(h_K(p)<(1+\eta)\pi k/4\), that is,
\[
\begin{aligned}
\Phi(V)&\subseteq\operatorname{int}K\times S\operatorname{int}K^\circ,\\
S&=(1+\eta)\frac{\pi k}4.
\end{aligned} \tag{7.1}
\]

*Step 4: rescaling.* Fix \(0<c<4\), choose \(\eta>0\) with \((1+\eta)c<4\), and then \(k\) so large that (7.1) holds. Then \(Sc<\pi k\), and Step 1 gives an injective symplectic map \(E:B^{2n}(Sc)\to(V,\omega)\). With the rescalings of Lemma 2.4,
\[
\begin{aligned}
&L_S\circ\Phi\circ E\circ D_{\sqrt S}:\\
&\quad B^{2n}(c)\to\operatorname{int}K\times\operatorname{int}K^\circ
\end{aligned}
\]
is injective and smooth, a diffeomorphism onto an open set, and its pullback of \(\omega_0\) is \(D_{\sqrt S}^*E^*\Phi^*L_S^*\omega_0=S^{-1}\cdot S\,\omega_0=\omega_0\). \(\square\)

## 2. The proofs of Theorems B and A

**Proof of Theorem B.** Let \(K\) be an origin-symmetric convex body and \(0<c<4\). Choose \(\alpha>0\) with \(\lambda c<4\), where \(\lambda=1+\alpha\), and let \(K'\) be the strip body of Lemma 1.5: \(K\subseteq K'\subseteq\lambda K\) and \((K')^\circ\subseteq K^\circ\). Proposition 7.1 gives an injective symplectic map
\[
\begin{aligned}
e:B^{2n}(\lambda c)&\to\operatorname{int}K'\times\operatorname{int}(K')^\circ\\
&\subseteq\lambda\operatorname{int}K\times\operatorname{int}K^\circ,
\end{aligned}
\]
the inclusions of interiors following from the inclusions of the bodies. Then \(Q_\lambda\circ e\circ D_{\sqrt\lambda}\) maps \(B^{2n}(c)\) injectively into \(\operatorname{int}K\times\operatorname{int}K^\circ\), and its pullback of \(\omega_0\) is \(\lambda^{-1}\cdot\lambda\,\omega_0=\omega_0\) (Lemma 2.4). \(\square\)

For each capacity \(c<4\) the construction is finite: the choices are made in the order \(\alpha\), then \(K'\) with its \(m\) vectors, then \(\eta\), then \(k\). No limit of embeddings is taken.

**Proof of Theorem A.** For \(n=1\), \(K=[-a,a]\) and \(K^\circ=[-a^{-1},a^{-1}]\), with product of lengths \(4\). Let \(n\ge2\) and \(0<c<4\), and let \(e:B^{2n}(c)\to U_K=\operatorname{int}K\times\operatorname{int}K^\circ\) be the map of Theorem B. By Lemma 2.4,
\[
\begin{aligned}
\frac{c^n}{n!}&=\operatorname{vol}(B^{2n}(c))\\
&=\operatorname{vol}\bigl(e(B^{2n}(c))\bigr)\le\operatorname{vol}(U_K)\\
&=\operatorname{vol}(K)\operatorname{vol}(K^\circ),
\end{aligned}
\]
the last equality by Lemma 1.6 and Fubini's theorem for the indicator function of the product (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 2, 252B](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm)). Letting \(c\uparrow4\) gives Theorem A. \(\square\)

## 3. Exercises

**7.1** (easy). Show that if \(\Phi^*\omega_0=\omega\) and \(\omega\) is nondegenerate at a point, then \(D\Phi\) is invertible there.

**7.2** (medium). For \(n=1\) the construction of Proposition 7.1 also makes sense. With \(m=1\) and \(b_1=1\), so that \(K=[-1,1]\), describe \(\Omega\), \(V\) and \(\Phi\), and check that \(\Phi(V)\) lies in \((-1,1)\times\mathbf R\).

**7.3** (easy). Show that \(h_K(\pm b_j)\le1\) for the strip body \(K\) of \(b_1,\dots,b_m\).

## 4. Solutions

**7.1.** \(\omega=D\Phi^{\mathsf T}J\,D\Phi\) has nonzero determinant, so \(\det D\Phi\ne0\).

**7.2.** \(\Omega=D\), \(V=\{\zeta\in D:|g(\zeta)|<1\}=D\), and \(\Phi(u+ix)=(x,-u-J_k(u,x))\). The first coordinate is the imaginary part of a point of \(D\), so it lies in \((-1,1)\).

**7.3.** For \(x\in K\), \(\langle\pm b_j,x\rangle\le|\langle b_j,x\rangle|\le1\).

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
- [AKO] S. Artstein-Avidan, R. Karasev and Y. Ostrover, *From symplectic measurements to the Mahler conjecture*, Duke Mathematical Journal 163 (2014), 2003–2022; arXiv:1303.4197. https://arxiv.org/abs/1303.4197
