# Masks, lists and one draw per edge

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The realization theorem of [The model operator and finite tests](the-model-operator-and-finite-tests.md) is proved by drawing, independently on every edge of a block \((i,k)\), one pair \((W,z)\) of a matrix weight and a voltage from a finite distribution whose expectation is close to \(h_i(t)h_k(t)p(t)\) in every fiber. This lesson builds that distribution in three approximations. The projection field \(p(t)\) is replaced by compactly supported coefficient templates at magnitudes on a logarithmic grid, multiplied by smooth scalar masks of the central parameter. The masks are realized by finitely many central powers, through their Fourier series. The second-factor templates, which carry the matrices \(R_\gamma\), are replaced by finite lists, so that only finitely many matrix weights occur: one list for each template used below the layer \(I=H_0\), and one common list from \(I\) on, obtained by factoring through the congruence subgroup \(\Lambda_q\). The lesson ends with the size of the resulting alphabet and the ranges of the voltage coordinates, which the girth argument of the next lesson needs [OpenAI-KK, Sections 9.4 to 9.6].

- Templates on a logarithmic grid (Section 1).
- Masks and their Fourier series (Section 2).
- Finite lists on the second factor (Section 3).
- One draw per edge (Section 4).
- The alphabet and the coordinates of the voltages (Section 5).

The notation of the four preceding lessons is in force. In particular \(L=\bar E_{\mathbb Z}\), \(q=d^{A_*}\), \(\delta=q^{-1}\), \(N=q^{n_{\mathrm f}}\), \(I=H_0\), \(w_i=q^{-1}2^{-\kappa|i|}\), \(M=\lfloor d^{1/32}\rfloor\), and \(W\rho(g)\) stands for \(\rho(g)\otimes W\) on \(\ell^2(F)\otimes\mathbb C^N\), with fibers given by (1.1) of the previous lesson. A target accuracy \(\varepsilon>0\) is fixed; *fixed* constants may depend on it, and all statements hold for large \(\ell\).

## 1. Templates on a logarithmic grid

Let \(J^\flat_\pm\) be smooth compactly supported functions given by Lemma 4.1 of [Schwartz idempotents and lattice projections](schwartz-idempotents-and-lattice-projections.md) for a fixed \(\varepsilon_0>0\), and let \(\varrho\ge1\) be such that both supports lie in the box \(\{|a_w|\le\varrho\}\) of the coordinates of \(\bar E\). For a sign \(\epsilon\), a magnitude \(0<\alpha\le1\) and a family of operators \(U'(\gamma)\), \(\gamma\in L\), put
\[
L_\epsilon(\alpha;U')=\sum_{\gamma\in L}\alpha^{n_{\mathrm f}}J^\flat_\epsilon\bigl(\Delta_{\alpha^{1/m}}\gamma\bigr)\,U'(\gamma) .
\]
The lattice \(\Delta_{\alpha^{1/m}}L\) has mesh at most one and cell volume \(\alpha^{n_{\mathrm f}}\) (Lemma 2.1 of [An affine nilpotent group](an-affine-nilpotent-group.md)), so the coefficient \(\ell^1\) norm of \(L_\epsilon(\alpha;\cdot)\) is at most \(\|J^\flat_\epsilon\|_\infty\) times the volume of the \(1\)-neighbourhood of the box, a fixed constant \(C_\flat\).

Fix a spacing \(s_0>0\), and a smooth \(\psi^0\ge0\) supported in \((-s_0,s_0)\) with \(\sum_{j\in\mathbb Z}\psi^0(v-js_0)=1\) for all \(v\in\mathbb R\); it exists, as in the proof of Lemma 5.1 of [The magnetic factor and the weighted trace](the-magnetic-factor-and-the-weighted-trace.md). For \(\nu,\omega\in\mathbb Z\) and \(0<t<\delta\) put
\[
\begin{aligned}
\psi_\nu(t)&=\psi^0\Bigl(\log_2\frac t\delta-\nu s_0\Bigr),\\
a_\nu&=\delta\,2^{\nu s_0},\\
\theta_\omega(t)&=\psi^0\Bigl(\log_2\frac{\delta-t}\delta-\omega s_0\Bigr),\\
b_\omega&=\delta\,2^{\omega s_0},
\end{aligned}
\]
and \(\psi_\nu=\theta_\omega=0\) off \((0,\delta)\). Then \(\sum_\nu\psi_\nu=\sum_\omega\theta_\omega=1\) on \((0,\delta)\), and on the supports \(|\log(a_\nu/t)|\le s_0\) and \(|\log(b_\omega/(\delta-t))|\le s_0\). Only \(\nu,\omega\le0\) occur, so the magnitudes are at most \(\delta\). For an adjacent pair \((i,k)\) let \(\mathcal T_{ik}\) be the set of pairs \((\nu,\omega)\) such that \(\psi_\nu\theta_\omega\) does not vanish identically on the support of \(h_ih_k\), and put
\[
f_{ik\nu\omega}=h_ih_k\,\psi_\nu\theta_\omega .
\]
Since \(h\) is positive on \([-0.7,0.7]\), at \(b(t)=(i+k)/2\) both \(h_i\) and \(h_k\) are positive, so \(\mathcal T_{ik}\) is not empty.

**Lemma 1.1** (templates; [OpenAI-KK, Section 9.4]). For every \(\varepsilon_1>0\) there are fixed \(\varepsilon_0\) and \(s_0\) such that, for large \(\ell\):

1. \(|\mathcal T_{ik}|\le\mathcal N\) for every adjacent pair \((i,k)\), with \(\mathcal N=(2\kappa/s_0+3)^2\);
2. for \(0<t<\delta\) and every adjacent pair \((i,k)\),
\[
\begin{aligned}
&\Bigl\|h_i(t)h_k(t)p(t)\\
&\quad-\sum_{(\nu,\omega)\in\mathcal T_{ik}}f_{ik\nu\omega}(t)\\
&\qquad\cdot L_+(a_\nu;u_t)\otimes L_-(b_\omega;V_t)\Bigr\|\\
&\quad\le\varepsilon_1 .
\end{aligned}
\]

*Proof.* (1) On the support of \(h_i\), \(|b(t)-i|<1\), and \(\log_2(t/\delta)=-\log_2(1+2^{-\kappa b})\) is a function of \(b\) with derivative between \(0\) and \(\kappa\). So it ranges over an interval of length at most \(2\kappa\), which meets the supports of at most \(2\kappa/s_0+3\) functions \(\psi_\nu\); the same holds for \(\log_2((\delta-t)/\delta)=-\log_2(1+2^{\kappa b})\) and the \(\theta_\omega\).

(2) By Proposition 3.1 of the lesson on Schwartz idempotents, with \(\theta=t\), the element \(K_t=\sum_\gamma t^{n_{\mathrm f}}J_+(\Delta_{t^{1/m}}\gamma)u_t(\gamma)\) satisfies \(\|p_t-K_t\|\le Ct^{1/m}\le C\delta^{1/m}\) and \(\|K_t\|\le C\). For \(t\) in the support of \(\psi_\nu\), Lemma 4.1 of that lesson gives coefficient \(\ell^1\) distance at most \(\varepsilon_0\) for the passage from \(J_+\) to \(J^\flat_+\), and at most \(Cs_0\) for the passage from the magnitude \(t\) to \(a_\nu\); only coefficients change, the unitaries \(u_t(\gamma)\) stay the same. So \(\|K_t-L_+(a_\nu;u_t)\|\le\varepsilon_0+Cs_0\). With \(\theta=t-\delta<0\), the same holds for \(K_{t-\delta}\) and \(J_-\) at magnitude \(\delta-t\), evaluated on \(V_t\); by Lemma 3.1 of [The magnetic factor and the weighted trace](the-magnetic-factor-and-the-weighted-trace.md), \(\|p_{t-\delta}[V_t]-K_{t-\delta}[V_t]\|=\|p_{t-\delta}-K_{t-\delta}\|\), at most \(C\delta^{1/m}\), and for \(t\) in the support of \(\theta_\omega\), \(\|K_{t-\delta}[V_t]-L_-(b_\omega;V_t)\|\le\varepsilon_0+Cs_0\). Writing the difference of two tensor products as a sum of differences in one factor,
\[
\begin{aligned}
&\bigl\|p(t)-L_+(a_\nu;u_t)\otimes L_-(b_\omega;V_t)\bigr\|\\
&\quad\le C\bigl(\delta^{1/m}+\varepsilon_0+s_0\bigr)
\end{aligned}
\]
whenever \(\psi_\nu(t)\theta_\omega(t)\ne0\). The numbers \(\psi_\nu(t)\theta_\omega(t)\ge0\) sum to one, and those with \(h_i(t)h_k(t)\psi_\nu(t)\theta_\omega(t)\ne0\) belong to \(\mathcal T_{ik}\), so the left side of (2) is at most \(h_i(t)h_k(t)\,C(\delta^{1/m}+\varepsilon_0+s_0)\). Choose \(\varepsilon_0\) and \(s_0\) with \(C(\varepsilon_0+s_0)\le\varepsilon_1/2\), and \(\ell\) so large that \(C\delta^{1/m}\le\varepsilon_1/2\). \(\square\)

The fiber of the operator \(\sum_{\gamma}a_\nu^{n_{\mathrm f}}J^\flat_+(\Delta_{a_\nu^{1/m}}\gamma)\rho(\sigma_X(\gamma))\) is \(L_+(a_\nu;u_t)\otimes1\), by (1.1) of the previous lesson, and that of the *lifted template*
\[
\begin{gathered}
\mathcal T(b)\\
=\sum_{v\in L}b^{n_{\mathrm f}}J^\flat_-\bigl(\Delta_{b^{1/m}}v\bigr)\\
\cdot R_v\,\rho(\sigma_Y(v))
\end{gathered}\tag{1.1}
\]
is \(1\otimes L_-(b;V_t)\), because \(R_v\) attached to \(\sigma_Y(v)\) turns \(u_t(v)\) into \(V_t(v)=u_t(v)\otimes R_v\).

## 2. Masks and their Fourier series

For a smooth function \(f\) on \(\mathbb T\) put \(\hat f(n)=\int_{\mathbb T}f(t)\mathbf e(-nt)\,dt\). By (1.1) of the previous lesson, the operator \(\sum_n\hat f(n)\rho(z_0^n)\) acts in the fiber at \(t\) by the scalar \(\sum_n\hat f(n)\mathbf e(nt)\).

**Lemma 2.1** (masks; [OpenAI-KK, Section 9.4]). For every adjacent pair \((i,k)\) and \((\nu,\omega)\in\mathcal T_{ik}\), the mask \(f=f_{ik\nu\omega}\) is smooth on \(\mathbb T\), supported in an interval of length at most \(Cw_i\), and for every \(j\ge0\)
\[
\begin{gathered}
\|f^{(j)}\|_\infty\le C_jw_i^{-j},\\
\|f^{(j)}\|_1\le C_jw_i^{1-j},\\
|\hat f(n)|\le C_jw_i(1+|n|w_i)^{-j} .
\end{gathered}
\]
Consequently \(\sum_n|\hat f(n)|\le C\), and for \(\Theta\ge1\) and \(K_i=\lceil\Theta/w_i\rceil\), the truncation \(f^{\le}(t)=\sum_{|n|\le K_i}\hat f(n)\mathbf e(nt)\) satisfies \(\sup_t|f(t)-f^{\le}(t)|\le C\Theta^{-1}\). The constants depend on \(\kappa\), \(h\), \(\psi^0\) and \(s_0\), not on \(\ell\), \(i\), \(k\), \(\nu\), \(\omega\).

*Proof.* On the support of \(h_i\), \(t=\delta\frac{2^{\kappa b}}{1+2^{\kappa b}}\) and \(\delta-t=\frac\delta{1+2^{\kappa b}}\) with \(|b-i|<1\), so both are at least \(c_\kappa w_i\): one of them is at least \(\delta/2\ge w_i/2\), and the other is comparable to \(\delta2^{-\kappa|b|}\). The \(j\)-th derivative of \(\psi_\nu\) is a combination of derivatives of \(\psi^0\) with products of derivatives of \(\log_2t\), so it is at most \(C_jt^{-j}\); likewise \(|\theta_\omega^{(j)}|\le C_j(\delta-t)^{-j}\). With \(\|h_i^{(j)}\|_\infty\le C_jw_i^{-j}\) (Lemma 5.1 of [The magnetic factor and the weighted trace](the-magnetic-factor-and-the-weighted-trace.md)), \(w_k\ge2^{-\kappa}w_i\) for \(|k-i|\le1\), and the Leibniz rule, \(\|f^{(j)}\|_\infty\le C_jw_i^{-j}\). The support of \(h_i\) is a compact subset of \((0,\delta)\) of length at most \(Cw_i\), which gives smoothness on \(\mathbb T\) and the \(L^1\) bounds.

\(|\hat f(n)|\le\|f\|_1\le Cw_i\), and \(j\) integrations by parts give \(|\hat f(n)|\le\|f^{(j)}\|_1(2\pi|n|)^{-j}\), at most \(C_jw_i^{1-j}|n|^{-j}\). If \(|n|w_i\le1\) the first bound gives the claim, otherwise the second, since then \(|n|w_i\ge\frac12(1+|n|w_i)\). With \(j=2\),
\[
\begin{aligned}
&\sum_nw_i(1+|n|w_i)^{-2}\\
&\quad\le w_i+2\int_0^\infty w_i(1+sw_i)^{-2}\,ds\le3 ,
\end{aligned}
\]
and, the summand being decreasing in \(|n|\),
\[
\begin{aligned}
&\sum_{|n|>K_i}w_i(1+|n|w_i)^{-2}\\
&\quad\le2\int_{K_i}^\infty w_i(1+sw_i)^{-2}\,ds\\
&\quad=\frac2{1+K_iw_i}\le\frac2\Theta .
\end{aligned}
\]
The uniform bound for \(f-f^{\le}\) is this tail, times \(C_2\). \(\square\)

The truncated masks need not vanish off the supports of the masks; only the uniform closeness is used.

## 3. Finite lists on the second factor

The scalar masks vary through infinitely many layers, but the alphabet of matrix weights must be finite. Below the layer \(I\) only \(O(1+\log q)\) second-factor templates occur, each replaced by its own list; from \(I\) on, one common list serves all layers.

**Lemma 3.1** (lists below \(I\); [OpenAI-KK, Section 9.5]). Let \(\mathcal W_<\) be the set of magnitudes \(b_\omega\) with \((\nu,\omega)\in\mathcal T_{ik}\) for some adjacent pair with \(i<I\). Then \(|\mathcal W_<|\le C(1+\log q)\). For every fixed \(\varepsilon_2>0\) and large \(\ell\), there are for each \(b\in\mathcal W_<\) elements \(v_{b,1},\ldots,v_{b,M}\in L\) and scalars \(c_{b,1},\ldots,c_{b,M}\) with \(|c_{b,h}|\le C\) and
\[
\begin{aligned}
&\Bigl\|\frac1M\sum_{h=1}^Mc_{b,h}R_{v_{b,h}}\rho\bigl(\sigma_Y(v_{b,h})\bigr)-\mathcal T(b)\Bigr\|\\
&\quad\le\varepsilon_2 .
\end{aligned}
\]

*Proof.* For \(i<I\) and \(t\) in the support of \(h_i\), \(b(t)<i+1\le I\), so \(\delta\ge\delta-t\ge\delta2^{-\kappa(I+1)}/2\). On the support of \(\theta_\omega\), \(b_\omega\) is within the factor \(e^{s_0}\) of \(\delta-t\), so \(\log_2b_\omega^{-1}\) lies in the interval from \(\log_2q-C\) to \(\log_2q+\kappa(I+1)+C\), which contains at most \((\kappa I+C)/s_0\) grid points. Since \(I=H_0\le h_*\log_2d\) and \(\log_2q=A_*\log_2d\), this is at most \(C(1+\log q)\).

For \(b\in\mathcal W_<\) let \(\mathfrak Q_b\subset L\) be the coordinate rectangle with radius \(\lceil\varrho b^{-w/m}\rceil\) in every coordinate of weight \(w\), and \(n_b=|\mathfrak Q_b|\). It contains every \(v\) with \(J^\flat_-(\Delta_{b^{1/m}}v)\ne0\), and since the weights of the \(2n_{\mathrm f}\) coordinates of \(L\) add up to \(mn_{\mathrm f}\),
\[
\begin{aligned}
n_b&\le\prod_w(2\varrho+3)\,b^{-w/m}\\
&=(2\varrho+3)^{2n_{\mathrm f}}\,b^{-n_{\mathrm f}} .
\end{aligned}
\]
For \(v\) uniform in \(\mathfrak Q_b\), the random operator \(n_bb^{n_{\mathrm f}}J^\flat_-(\Delta_{b^{1/m}}v)R_v\rho(\sigma_Y(v))\) has expectation \(\mathcal T(b)\) and matrix part of norm at most \((2\varrho+3)^{2n_{\mathrm f}}\|J^\flat_-\|_\infty\). Its group coordinates are at most \((\varrho+1)b^{-1}\le Cq2^{\kappa I}\le q^a\) for a fixed \(a\ge n_{\mathrm f}\), because \(2^{\kappa I}\le d^{\kappa h_*}=q^{\kappa h_*/A_*}\). Lemma 5.1 of the previous lesson, applied to these at most \(C(1+\log q)\) distributions, gives the lists. \(\square\)

From \(I\) on, let \(\Lambda=\Lambda_q\), of index \(Q_q=q^{2n_{\mathrm f}}\) in \(L\) (Section 2 of [The magnetic factor and the weighted trace](the-magnetic-factor-and-the-weighted-trace.md)), and \(\mathcal V_q\) the set of elements of \(L\) with all coordinates in \(\{0,\ldots,q-1\}\). Every \(\gamma\in L\) is uniquely \(\gamma=yv\) with \(y\in\Lambda\), \(v\in\mathcal V_q\) (Exercise 6.1), and \(R_y=1\) for \(y\in\Lambda\). Put
\[
\begin{gathered}
C_q=\frac1{Q_q}\sum_{v\in\mathcal V_q}R_v\,\rho(\sigma_Y(v)),\\
\mathcal S(b)=Q_q\sum_{y\in\Lambda}b^{n_{\mathrm f}}J^\flat_-\bigl(\Delta_{b^{1/m}}y\bigr)\rho(\sigma_Y(y)) .
\end{gathered}
\]
By Lemma 5.1 of the previous lesson, applied to the uniform distribution on \(\mathcal V_q\), there are \(v_1,\ldots,v_M\in\mathcal V_q\) with \(\|C_q^M-C_q\|\le\varepsilon_2\), where \(C_q^M=\frac1M\sum_hR_{v_h}\rho(\sigma_Y(v_h))\). This one list serves all layers \(i\ge I\).

**Lemma 3.2** (the subgroup factorization; [OpenAI-KK, Section 9.5]). Let \(\mathcal W_\ge\) be the set of magnitudes \(b_\omega\) with \((\nu,\omega)\in\mathcal T_{ik}\) for some adjacent pair with \(i\ge I\). For large \(\ell\):

1. for every such pair and \(b=b_\omega\),
\[
b^{-1/m}/q\ge2^{2E_0H_i} ;\tag{3.1}
\]
2. the coefficient \(\ell^1\) norms of the \(\mathcal S(b)\), \(b\in\mathcal W_\ge\), are at most a fixed constant, and every fiber of \(\mathcal S(b)C_q\) and of \(\mathcal S(b)C_q^M\) has norm at most a fixed constant;
3. \(\|\mathcal S(b)C_q^M-\mathcal S(b)C_q\|\le C\varepsilon_2\);
4. for \(t\) in the support of \(\theta_\omega\), the fiber of \(\mathcal S(b_\omega)C_q\) at \(t\) is within \(\varepsilon_2\) of \(1\otimes L_-(b_\omega;V_t)\), uniformly in \(\omega\) and \(t\).

*Proof.* (1) For \(i\ge I\) and \(t\) in the support of \(h_i\), \(b(t)>i-1\ge0\), so \(\delta-t\le\delta2^{-\kappa b}\le2^\kappa q^{-1}2^{-\kappa i}\), and \(b_\omega\le e^{s_0}(\delta-t)\). Hence
\[
\begin{aligned}
\log_2\frac{b^{-1/m}}q&\ge\frac\kappa mi\\
&\quad-\Bigl(1-\frac1m\Bigr)A_*\log_2d-C .
\end{aligned}
\]
Since \(i\ge I=H_0>\log_2d\) and \(H_i=H_0+i\le2i\), the right side minus \(2E_0H_i\) is at least \((\kappa/m-A_*-4E_0)i-C\), which is positive for large \(\ell\) by the choice \(\kappa/m>10(E_0+A_*+C_\bullet+1)\).

(2) In coordinates \(\Lambda\) is the set of points of \(L\) with all coordinates divisible by \(q\). With \(\beta=b^{1/m}\), \(\Delta_\beta\Lambda\) is a rectangular lattice with spacing \(q\beta^w\le q\beta\le1\) in weight \(w\), by (3.1), and cell volume \(Q_qb^{n_{\mathrm f}}\). So the coefficient \(\ell^1\) norm \(Q_qb^{n_{\mathrm f}}\sum_{y\in\Lambda}|J^\flat_-(\Delta_\beta y)|\) of \(\mathcal S(b)\) is bounded, as in Section 1. The operators \(C_q\) and \(C_q^M\) are averages of unitaries, and the fiber norms of a product are at most the products of the coefficient \(\ell^1\) norms.

(3) \(\|\mathcal S(b)\|\le C\) and \(\|C_q^M-C_q\|\le\varepsilon_2\).

(4) The factor \(Q_q\) cancels, and
\[
\begin{aligned}
\mathcal S(b)C_q&=\sum_{y\in\Lambda,\,v\in\mathcal V_q}b^{n_{\mathrm f}}J^\flat_-(\Delta_\beta y)\\
&\qquad\cdot R_v\,\rho(\sigma_Y(y))\rho(\sigma_Y(v)) .
\end{aligned}
\]
By (1.1) of the previous lesson and \(R_y=1\), the term acts in the fiber at \(t\) by \(1\otimes V_t(y)V_t(v)\), and by Lemma 3.1 of the lesson on the magnetic factor, \(V_t(y)V_t(v)=\mathbf e(\tau c(y,v))V_t(yv)\) with \(\tau=t-\delta\). Since \((y,v)\mapsto yv\) is a bijection onto \(L\), the fiber is \(1\otimes\sum_\gamma d_\gamma V_t(\gamma)\) with \(d_{yv}=b^{n_{\mathrm f}}J^\flat_-(\Delta_\beta y)\mathbf e(\tau c(y,v))\), to be compared with the coefficients \(b^{n_{\mathrm f}}J^\flat_-(\Delta_\beta(yv))\) of \(L_-(b;V_t)\). By Lemma 2.1 of [An affine nilpotent group](an-affine-nilpotent-group.md), \(\Delta_\beta(yv)=(\Delta_\beta y)(\Delta_\beta v)\) and \(\tau c(y,v)=(\tau/b)\,c(\Delta_\beta y,\Delta_\beta v)\), with \(|\tau|/b\le e^{s_0}\le3\) on the support of \(\theta_\omega\). The coordinates of \(\Delta_\beta v\), \(v\in\mathcal V_q\), are at most \(q\beta\le2^{-2E_0H_i}=:\vartheta\). On the compact \(1\)-neighbourhood \(K_1\) of the support of \(J^\flat_-\), the group law and the cocycle are uniformly continuous, \(c(a,1)=0\), and \(J^\flat_-\) is Lipschitz; so for \(\Delta_\beta y\in K_1\),
\[
\bigl|d_{yv}-b^{n_{\mathrm f}}J^\flat_-(\Delta_\beta(yv))\bigr|\le b^{n_{\mathrm f}}\,\varpi(\vartheta),
\]
with \(\varpi(\vartheta)\to0\) as \(\vartheta\to0\). For \(\Delta_\beta y\notin K_1\) and small \(\vartheta\), both coefficients vanish, since \(\Delta_\beta(yv)\) is then outside the support. The nonzero differences occur at \(\gamma\) with \(\Delta_\beta\gamma\) in a fixed compact set, whose number of points times \(b^{n_{\mathrm f}}\) is bounded. So the coefficient \(\ell^1\) distance, and with it the fiber distance, is at most \(C\varpi(\vartheta)\), which is below \(\varepsilon_2\) for large \(\ell\), uniformly. \(\square\)

## 4. One draw per edge

For an adjacent pair \((i,k)\), fix \(\varrho\) as in Section 1 and define a random pair \((W,z)\in M_N(\mathbb C)\times F\) by the following choices, independent given \((\nu,\omega)\).

1. Choose \((\nu,\omega)\) uniformly in \(\mathcal T_{ik}\) and \(n\) uniformly in \(\{-K_i,\ldots,K_i\}\). Record the scalar \(c_1=|\mathcal T_{ik}|(2K_i+1)\hat f_{ik\nu\omega}(n)\) and the element \(z_0^n\).
2. Choose \(x\) uniformly in the rectangle \(\mathfrak P_\nu\subset L\) with radius \(\lceil\varrho a_\nu^{-w/m}\rceil\) in every coordinate of weight \(w\). Record \(c_2=|\mathfrak P_\nu|\,a_\nu^{n_{\mathrm f}}J^\flat_+(\Delta_{a_\nu^{1/m}}x)\) and \(\sigma_X(x)\).
3. If \(i<I\), choose \(h\) uniformly in \(\{1,\ldots,M\}\); record \(c_3=c_{b_\omega,h}\), the matrix \(R=R_{v_{b_\omega,h}}\) and \(g_3=\sigma_Y(v_{b_\omega,h})\). If \(i\ge I\), choose \(y\) uniformly in the set \(\mathfrak Q^\Lambda_\omega\) of \(y\in\Lambda\) with all coordinates of weight \(w\) at most \(\varrho b_\omega^{-w/m}\), and independently \(h\) uniformly in \(\{1,\ldots,M\}\); record \(c_3=|\mathfrak Q^\Lambda_\omega|\,Q_qb_\omega^{n_{\mathrm f}}J^\flat_-(\Delta_{b_\omega^{1/m}}y)\), the matrix \(R=R_{v_h}\) and \(g_3=\sigma_Y(y)\sigma_Y(v_h)\).

Put \(z=z_0^n\sigma_X(x)g_3\), let \(c^\flat\) be a nearest point to \(c_1c_2c_3\) in a fixed finite set \(G_\varepsilon\) of complex numbers within \(\varepsilon_2\) of every point of the disk of radius \(C_\varepsilon+1\), and \(W=c^\flat R\). The voltage \(z\) is kept even when \(W=0\).

The scalars are bounded: \(|c_1|\le\mathcal N(2\Theta/w_i+3)\,Cw_i\le C\) by Lemma 2.1; \(|c_2|\le C\) as in the proof of Lemma 3.1; \(|c_3|\le C\) by Lemma 3.1 for \(i<I\), and for \(i\ge I\) because, by (3.1), \(|\mathfrak Q^\Lambda_\omega|\le\prod_w(2\varrho+3)b_\omega^{-w/m}/q\), which is \((2\varrho+3)^{2n_{\mathrm f}}(Q_qb_\omega^{n_{\mathrm f}})^{-1}\). This gives the constant \(C_\varepsilon\).

**Proposition 4.1** (the expectation of one draw; [OpenAI-KK, Section 9.6]). For every \(\varepsilon>0\) there are fixed choices of \(\varepsilon_1\), \(\varepsilon_0\), \(s_0\), \(\Theta\), \(\varepsilon_2\) and \(G_\varepsilon\) such that for large \(\ell\) and every adjacent pair \((i,k)\),
\[
\begin{gathered}
\operatorname*{ess\,sup}_t\bigl\|\mathbb E[W\rho(z)](t)\\
-h_i(t)h_k(t)p(t)\bigr\|\le\varepsilon ,
\end{gathered}\tag{4.1}
\]
where \((t)\) denotes the fiber at \(t\), and \(h_ih_kp(t)=0\) for \(t\notin(0,\delta)\).

*Proof.* Choose \(\varepsilon_1=\varepsilon/4\); Lemma 1.1 fixes \(\varepsilon_0\), \(s_0\) and \(\mathcal N\). Then choose \(\Theta\) and \(\varepsilon_2\) so small, in terms of \(\mathcal N\) and the fixed constants, that the bound below is at most \(\varepsilon\).

Let \(X=c_1c_2c_3R\rho(z)\). Since \(R\) and \(\rho(z)\) are unitary, rounding changes \(W\rho(z)\) by at most \(\varepsilon_2\) in norm. As \(\rho\) is a homomorphism, \(R\) commutes with the \(\rho(g)\), and the choices are independent given \((\nu,\omega)\),
\[
\mathbb EX=\sum_{(\nu,\omega)\in\mathcal T_{ik}}F_{\nu\omega}\,\mathcal A_\nu\,\mathcal B_\omega ,
\]
where \(F_{\nu\omega}=\sum_{|n|\le K_i}\hat f_{ik\nu\omega}(n)\rho(z_0^n)\); \(\mathcal A_\nu=\sum_xa_\nu^{n_{\mathrm f}}J^\flat_+(\Delta_{a_\nu^{1/m}}x)\rho(\sigma_X(x))\), because \(\mathfrak P_\nu\) contains every \(x\) with a nonzero coefficient; and \(\mathcal B_\omega\) is the list average of Lemma 3.1 if \(i<I\), and \(\mathcal S(b_\omega)C_q^M\) if \(i\ge I\). In the fiber at \(t\), \(F_{\nu\omega}\) acts by \(f^{\le}(t)\) and \(\mathcal A_\nu\) by \(L_+(a_\nu;u_t)\otimes1\).

The target \(G(t)\), the sum over \(\mathcal T_{ik}\) of \(f(t)\,L_+(a_\nu;u_t)\otimes L_-(b_\omega;V_t)\), is within \(\varepsilon_1\) of \(h_ih_kp(t)\) for \(0<t<\delta\) by Lemma 1.1, and equal to it, namely zero, for other \(t\). For each pair, the fiber difference is
\[
\begin{aligned}
&(f^{\le}-f)(t)\,(L_+\otimes1)\mathcal B_\omega(t)\\
&\quad+f(t)\,(L_+\otimes1)\\
&\qquad\cdot\bigl(\mathcal B_\omega(t)-1\otimes L_-(b_\omega;V_t)\bigr) .
\end{aligned}
\]
The first term is at most \(C\Theta^{-1}\cdot C_\flat\cdot C\), since the fibers of \(\mathcal B_\omega\) are bounded (Lemma 3.1 with \(\|\mathcal T(b)\|\le C_\flat\), and Lemma 3.2(2)). The second term vanishes off the support of \(\theta_\omega\), and on it is at most \(C_\flat\) times \(\varepsilon_2\) (Lemma 3.1, with the fiber of \(\mathcal T(b)\) from Section 1) or \(\varepsilon_2+C\varepsilon_2\) (Lemma 3.2(3) and (4)). Summing over at most \(\mathcal N\) pairs,
\[
\begin{aligned}
&\bigl\|\mathbb E[W\rho(z)](t)-h_ih_kp(t)\bigr\|\\
&\quad\le\varepsilon_2+\mathcal NC\bigl(\Theta^{-1}+\varepsilon_2\bigr)+\frac\varepsilon4
\end{aligned}
\]
for almost every \(t\), which is at most \(\varepsilon\) for the choices made. \(\square\)

## 5. The alphabet and the coordinates of the voltages

**Lemma 5.1** (alphabet and coordinates; [OpenAI-KK, Section 9.6]). For large \(\ell\):

1. the matrices \(W\) that occur form a set of at most \(C(1+\log q)M\) elements, and the pairs of a label of \(Y\) and such a matrix number \(o(dD)\);
2. there is a fixed \(C\) such that for every adjacent pair \((i,k)\) every possible \(z\), and \(z^{-1}\), has all coordinates at most \(2^{CH_i}\) in absolute value;
3. if \(i\le2I\), then \(a_\nu^{-1/m}\ge2^{2E_0H_i}\) for every \((\nu,\omega)\in\mathcal T_{ik}\), and the superdiagonal coordinates \((b_x-1)_{uv}\), \(u<v\), of \(x\) in step 2 are independent and uniform on integer intervals with at least \(2^{E_0H_i}\) points;
4. if \(i\ge I\), the numbers \((b_y-1)_{uv}/q\), \(u<v\), for \(y\) in step 3 are independent and uniform on integer intervals with at least \(2^{E_0H_i}\) points.

*Proof.* (1) The matrices are \(c^\flat R\) with \(c^\flat\in G_\varepsilon\), a fixed finite set, and \(R\) in the lists of Lemma 3.1, at most \(C(1+\log q)\) lists of \(M\) entries, or in the one list of \(C_q^M\). With \(M\le d^{1/32}\) and \(\log q=A_*\log d\), there are at most \(Cd^{1/32}\log d\) matrices. The labels number \(m_\ell\le27K^2d\,2^{r+2}=O(\ell^2d^{11/4})\) by Lemma 4.1 of [Gated permutations and the two towers](gated-permutations-and-the-two-towers.md), since \(2^r=d^{7/4}\) and \(K=320\ell\). The product is \(O(d^{89/32}\ell^3)=o(d^3)=o(dD)\).

(2) By Lemma 2.1, \(|n|\le K_i\le\Theta q2^{\kappa|i|}+1\). On the support of \(h_i\), \(t\) and \(\delta-t\) are at least \(c_\kappa w_i\), so \(a_\nu^{-1},b_\omega^{-1}\le Cq2^{\kappa|i|}\), and the coordinates of \(x\), \(v_{b,h}\) and \(y\) are at most \((\varrho+1)Cq2^{\kappa|i|}\); those of \(v_h\in\mathcal V_q\) are at most \(q\). Since \(\log_2(q2^{\kappa|i|})=A_*\log_2d+\kappa|i|\) is at most \((A_*+\kappa)H_i\), every factor of \(z\) has coordinates at most \(2^{C'H_i}\), and the fixed polynomial laws of multiplication and inversion give the bound \(2^{CH_i}\) for \(z\) and \(z^{-1}\).

(3) On the support of \(h_i\), \(t<\delta\), so \(a_\nu\le e^{s_0}\delta\) and \(\log_2a_\nu^{-1}\ge\log_2q-2\). If \(0\le i\le2I\), then \(H_i\le3H_0\le3h_*\log_2d\), and \(A_*/m>10E_0h_*\) gives
\[
\begin{aligned}
\frac1m\log_2a_\nu^{-1}&\ge10E_0h_*\log_2d-2\\
&\ge\tfrac{10}3E_0H_i-2\ge2E_0H_i .
\end{aligned}
\]
If \(i<0\), then \(b(t)<i+1\le0\) and \(t\le\delta2^{\kappa b}\le2^\kappa q^{-1}2^{-\kappa|i|}\), so \(\log_2a_\nu^{-1}\ge\log_2q+\kappa|i|-\kappa-2\), and with \(\kappa/m>10E_0\) and \(H_i=H_0+|i|\le h_*\log_2d+|i|\),
\[
\begin{aligned}
\frac1m\log_2a_\nu^{-1}&\ge10E_0\bigl(h_*\log_2d+|i|\bigr)-C\\
&\ge2E_0H_i .
\end{aligned}
\]
The coordinate \((b_x-1)_{uv}\) has weight \(v-u\ge1\), so its interval has radius at least \(\varrho a_\nu^{-1/m}\ge2^{2E_0H_i}\); a uniform point of a rectangle has independent uniform coordinates.

(4) The coordinate \((b_y-1)_{uv}\) ranges over the multiples of \(q\) of absolute value at most \(\varrho b_\omega^{-(v-u)/m}\), which number at least \(b_\omega^{-1/m}/q\ge2^{2E_0H_i}\) by (3.1). \(\square\)

The ranges in (3) and (4) overlap: every layer \(i\) is covered by one of them, and the layers from \(I\) to \(2I\) by both.

## 6. Exercises

**6.1** (easy). Show that \(|\mathcal V_q|=Q_q\), and that every \(\gamma\in L\) is uniquely \(yv\) with \(y\in\Lambda\) and \(v\in\mathcal V_q\).

**6.2** (easy). Let \(g\) be smooth with support in \((-1,1)\), \(0<w<\frac12\), and \(f(t)=g((t-\frac12)/w)\) on \(\mathbb T\). Show that \(\hat f(n)=w\,\hat g(nw)\,\mathbf e(-n/2)\), with the Fourier transform \(\hat g(\xi)=\int g(s)\mathbf e(-\xi s)ds\), and deduce bounds of the form in Lemma 2.1.

**6.3** (medium). Show that \(\mathbb E[c_2\rho(\sigma_X(x))]\) in step 2 does not change if \(\mathfrak P_\nu\) is replaced by a larger rectangle with the corresponding count, and that the bound \(|c_2|\le C\) requires the rectangle radius to be of order \(a_\nu^{-w/m}\) in weight \(w\).

**6.4** (medium). Derive \(V_t(y)V_t(v)=\mathbf e((t-\delta)c(y,v))V_t(yv)\) for \(y\in\Lambda_q\) directly from \(\sigma(y)\sigma(v)=(0,1,c(y,v))\sigma(yv)\), the multiplier of \(u_t\), and \(R(0,1,z)=\mathbf e(-\delta z)\).

## 7. Solutions

**6.1.** Reduction modulo \(q\) is a surjective homomorphism \(L\to\bar E_{\mathbb Z/q\mathbb Z}\) with kernel \(\Lambda\), and \(\mathcal V_q\) maps bijectively onto \(\bar E_{\mathbb Z/q\mathbb Z}\), a set of \(q^{2n_{\mathrm f}}\) elements. For \(\gamma\in L\), let \(v\in\mathcal V_q\) have the same reduction; then \(y=\gamma v^{-1}\in\Lambda\). If \(yv=y'v'\), then \(v\) and \(v'\) have the same reduction, so \(v=v'\) and \(y=y'\).

**6.2.**
\[
\begin{aligned}
\hat f(n)&=\int g((t-\tfrac12)/w)\,\mathbf e(-nt)\,dt\\
&=w\int g(s)\,\mathbf e(-n(\tfrac12+ws))\,ds\\
&=w\,\mathbf e(-n/2)\hat g(nw) .
\end{aligned}
\]
Since \(|\hat g(\xi)|\le C_j(1+|\xi|)^{-j}\), \(|\hat f(n)|\le C_jw(1+|n|w)^{-j}\), and \(\sum_n|\hat f(n)|\le C\), as in Lemma 2.1.

**6.3.** The expectation over a rectangle \(\mathfrak P\) of \(|\mathfrak P|a^{n_{\mathrm f}}J^\flat_+(\Delta x)\rho(\sigma_X(x))\) is \(\sum_{x\in\mathfrak P}a^{n_{\mathrm f}}J^\flat_+(\Delta x)\rho(\sigma_X(x))\), which is the same for every rectangle containing the support. The scalar is at most \(|\mathfrak P|a^{n_{\mathrm f}}\|J^\flat_+\|_\infty\); with radii \(\lceil\varrho a^{-w/m}\rceil\) the count is at most \(Ca^{-n_{\mathrm f}}\), while radii larger by a factor \(\lambda\ge1\) in every coordinate multiply it by about \(\lambda^{2n_{\mathrm f}}\).

**6.4.** \(V_t(y)V_t(v)=u_t(y)u_t(v)\otimes R_yR_v\). The first factor is \(\mathbf e(tc(y,v))u_t(yv)\). For the second,
\[
\begin{aligned}
&R(\sigma(y))R(\sigma(v))\\
&\quad=R(\sigma(y)\sigma(v))\\
&\quad=R(0,1,c(y,v))R(\sigma(yv))\\
&\quad=\mathbf e(-\delta c(y,v))R_{yv} .
\end{aligned}
\]
Together, \(\mathbf e((t-\delta)c(y,v))V_t(yv)\); and \(R_y=1\) is not needed for this identity.

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 9.4 to 9.6. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
