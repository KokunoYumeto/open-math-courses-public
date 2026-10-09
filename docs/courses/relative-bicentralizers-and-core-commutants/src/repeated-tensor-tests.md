# Repeated tensor tests

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the central identity \(U=D\): the comparison contraction \(U=L^*R\) between the two relative products equals the unitary \(D=\exp(iX\otimes Y)\) [OAI, Theorem 6.2]. Consequently \(R=LD\): multiplying \(x\in N\) and \(a\in\mathrm B\) in the order \(xa\) is the same as multiplying in the order \(ax\) after letting the bicentralizer flow act on \(a\) by the modular energy of \(x\) (Corollary 1.2). For eigenoperators this is the relation \(xa=\gamma_h(a)x\); the theorem extends it to all of \(N\), whose elements in general have no point spectrum.

The proof is by contradiction and uses only the uniform estimate of the previous lesson. If \(U\ne D\), the average \(G=(U+D)/2\) strictly decreases norms on some vectors. One builds long words \(W_{s_m}G_mW_{-s_m}\cdots W_{s_1}G_1W_{-s_1}\) with random inputs \(e^{i(t-r_j)X}h\) and random shifts \(s_j\). At step \(j\) the current vector meets the region where \(G\) loses norm with probability of order \(1/j\), while the time-averaged estimate keeps the propagated vectors close to the ideal ones, which can be computed exactly. The expected losses form a divergent series, but their total cannot exceed the initial norm.

We use: the setting, Proposition 2.2, Lemma 3.1 and the notation of [The two relative products](the-two-relative-products.md); Proposition 1.1, Lemma 2.1 and Lemma 3.1 of [A uniform energy estimate](a-uniform-energy-estimate.md); the spectral theorem for commuting self-adjoint operators and Fubini's theorem.

## 1. The theorem

We keep the setting of the two previous lessons: \(N\) a factor of type III₁ with separable predual, \(N\subset M\) with expectation, \(M\) with separable predual, \(H=L^2(N,\varphi)\), \(K=L^2(\mathrm B,\bar\varphi)\), the modular generator \(X\) on \(H\), the flow \(W_s=e^{isY}\) on \(K\), the isometries \(R,L\colon H\otimes K\to L^2(M,\bar\varphi)\), \(U=L^*R\) and \(D=\exp(iX\otimes Y)\).

**Theorem 1.1** (OpenAI). \(U=D\).

**Corollary 1.2.** \(R=LD\). In particular \(R\) and \(L\) have the same range, and for \(x\in N\) and \(a\in\mathrm B\), \(xa\Omega=L(D(x\Omega\otimes a\Omega))\).

**Proof of Corollary 1.2.** For \(\psi\in H\otimes K\), since \(R\), \(L\) are isometries and \(D\) is unitary,
\[
\|R\psi-LD\psi\|^2=2\|\psi\|^2-2\operatorname{Re}\langle L^*R\psi,D\psi\rangle=2\|\psi\|^2-2\|D\psi\|^2=0 .\qquad\square
\]

The proof of Theorem 1.1 uses one more lemma about the joint spectral calculus.

**Lemma 1.3** (fibrewise lower bound). Let \(\mathcal K_1,\mathcal K_2\) be Hilbert spaces, \(A\) a self-adjoint operator on \(\mathcal K_1\), \(T\) a bounded operator on \(\mathcal K_2\otimes K\), \(w\in\mathcal K_2\), \(\eta\in K\), \(J\) a compact interval and \(c\ge0\) with \(\|T(w\otimes W_s\eta)\|\ge c\) for all \(s\in J\). Let \(\Theta=\exp(iA\otimes Y)\), acting on \(\mathcal K_1\otimes K\), and for \(\Xi\in\mathcal K_1\) let \(\Theta(\Xi\otimes\eta)[w]\in\mathcal K_1\otimes\mathcal K_2\otimes K\) denote the vector obtained by inserting \(w\) as the middle tensor factor. Then
\[
\big\|(1\otimes T)(E_A(J)\otimes1\otimes1)\,\Theta(\Xi\otimes\eta)[w]\big\|\ge c\,\|E_A(J)\Xi\|.
\]

**Proof.** Let \(\tau>0\), partition \(J\) into finitely many intervals \(J_i\) of length at most \(\tau\), and choose \(s_i\in J_i\). The operator \(1\otimes T\) commutes with \(E_A(J_i)\otimes1\otimes1\), so the vectors \((1\otimes T)(E_A(J_i)\otimes1\otimes1)\Theta(\Xi\otimes\eta)[w]\) are orthogonal. On the range of \(E_A(J_i)\), the product spectral measure gives
\[
\big\|\Theta(E_A(J_i)\Xi\otimes\eta)-E_A(J_i)\Xi\otimes W_{s_i}\eta\big\|^2=\int_{J_i}\|(W_{u}-W_{s_i})\eta\|^2\,d\nu(u)\le\omega(\tau)^2\,\|E_A(J_i)\Xi\|^2,
\]
where \(\nu\) is the spectral measure of \(A\) at \(\Xi\) and \(\omega(\tau)=\sup_{|u|\le\tau}\|W_u\eta-\eta\|\). Since \((1\otimes T)(E_A(J_i)\Xi\otimes w\otimes W_{s_i}\eta)=E_A(J_i)\Xi\otimes T(w\otimes W_{s_i}\eta)\) has norm at least \(c\|E_A(J_i)\Xi\|\),
\[
\big\|(1\otimes T)(E_A(J_i)\otimes1\otimes1)\Theta(\Xi\otimes\eta)[w]\big\|\ge\big(c-\|T\|\,\|w\|\,\omega(\tau)\big)\|E_A(J_i)\Xi\| .
\]
Summing the squares over \(i\) and letting \(\tau\to0\) proves the lemma, because \(\omega(\tau)\to0\). \(\square\)

## 2. Proof of Theorem 1.1

Suppose that \(U\ne D\).

*A local gap.* For \(l>0\), the vectors of \(H\) with \(X\)-spectral support in \([-l,l]\) form a subspace \(H_l\), and \(\bigcup_lH_l\) is dense in \(H\). The span of the vectors \(h\otimes\eta\) with \(h\in\bigcup_lH_l\) and \(\eta\in K\) is dense in \(H\otimes K\), so there are \(l>0\) and unit vectors \(h\in H_l\), \(\eta\in K\) with \((U-D)(h\otimes\eta)\ne0\). The map \((t',s')\mapsto(U-D)(e^{it'X}h\otimes W_{s'}\eta)\) is norm continuous, so there are \(c>0\) and \(0<b\le1\) with
\[
\|(U-D)(e^{it'X}h\otimes W_{s'}\eta)\|\ge c\qquad(|t'|\le b,\ |s'|\le b).
\tag{2.1}
\]
Fix this \(\eta\). By Proposition 1.1 of the previous lesson choose \(\delta>0\) with \(\epsilon:=\epsilon_\eta(\delta)<c/8\), let \(p_\delta\) be the density of Lemma 3.1 there, and choose \(A\ge1\) with \(\int_{-A}^Ap_\delta\ge3/4\).

*The random experiment.* Fix \(m\ge1\) and put \(B_j=b+1+jl\) and
\[
a_j=\frac b{2A}\cdot\frac b{B_j}\qquad(1\le j\le m).
\]
On a product probability space take independent random variables \(t\) with density \(p_\delta\), \(r_1,\ldots,r_m\) uniform on \([-2A,2A]\), and \(s_1,\ldots,s_m\) with \(s_j\) uniform on \([-B_j,B_j]\). Put \(h_j=e^{i(t-r_j)X}h\), a unit vector of \(H\). For a vector \(\Psi\in H^{\otimes(j-1)}\otimes K\) write \(\Psi[h_j]\in H^{\otimes j}\otimes K\) for the vector obtained by inserting \(h_j\) as the \(j\)-th factor of \(H\); this is isometric in \(\Psi\). Define \(\zeta_0=\chi_0=\eta\) and, for \(1\le j\le m\),
\[
\zeta_j=W_{s_j}G_jW_{-s_j}\big(\zeta_{j-1}[h_j]\big),\qquad\chi_j=W_{s_j}D_jW_{-s_j}\big(\chi_{j-1}[h_j]\big)=D_j\big(\chi_{j-1}[h_j]\big),
\]
where \(G_j=(U_j+D_j)/2\) and the last equality holds because \(D_j\) commutes with every \(W_s\). All these vectors depend continuously on the parameters. By Lemma 3.1 of the lesson on the two relative products, \(\chi_k=\exp(iS_k\otimes Y)\big(\bigotimes_{j\le k}h_j\otimes\eta\big)\).

*The propagated error.* Fix \(k\le m\) and all parameters except \(t\). Then \(\bigotimes_{j\le k}h_j=e^{itS_k}\xi_k\) with the unit vector \(\xi_k=\bigotimes_{j\le k}e^{-ir_jX}h\), and
\[
\zeta_k=W_{s_k}G_kW_{s_{k-1}-s_k}G_{k-1}\cdots W_{s_1-s_2}G_1W_{-s_1}\big(e^{itS_k}\xi_k\otimes\eta\big),
\]
an averaged word whose shifts add up to \(0\), with ideal word \(\exp(iS_k\otimes Y)\); its value at the same vector is \(\chi_k\). Lemma 3.1 of the previous lesson gives \(\int\|\zeta_k-\chi_k\|^2p_\delta(t)\,dt\le\epsilon^2\), and integrating over the remaining parameters,
\[
\mathbb E\|\zeta_k-\chi_k\|^2\le\epsilon^2 .
\tag{2.2}
\]

*The loss at one step.* Fix \(j=k+1\le m\) and put
\[
v=W_{-s_j}\big(\zeta_k[h_j]\big),\qquad v_0=W_{-s_j}\big(\chi_k[h_j]\big).
\]
Then \(\|v\|=\|\zeta_k\|\) and \(\|\zeta_j\|=\|G_jv\|\). Since \(U_j\) is a contraction and \(D_j\) unitary, the parallelogram law gives
\[
\|v\|^2-\|G_jv\|^2\ge\tfrac14\|(U_j-D_j)v\|^2 .
\tag{2.3}
\]
Let \(Q\) be the random projection \(1_{\{|t-r_j|\le b\}}\,E_{S_k}([s_j-b,s_j+b])\), acting on the first \(k\) factors of \(H\); for \(k=0\) read \(S_0=0\). It commutes with \(U_j\), \(D_j\) and every \(W_s\), so \(\|(U_j-D_j)v\|\ge\|(U_j-D_j)Qv\|\). We claim
\[
\mathbb E\|(U_j-D_j)Qv_0\|^2\ge\tfrac34c^2a_j,\qquad\mathbb E\|(U_j-D_j)Q(v-v_0)\|^2\le4\epsilon^2a_j .
\tag{2.4}
\]

*The first inequality.* Fix \(t\), \(r_1,\ldots,r_k\) and \(r_j\), and let \(\Xi=e^{itS_k}\xi_k\). Since \(W_{-s_j}\exp(iS_k\otimes Y)=\exp(i(S_k-s_j)\otimes Y)\), we have \(v_0=\Theta(\Xi\otimes\eta)[h_j]\) with \(\Theta=\exp(iA\otimes Y)\) and \(A=S_k-s_j\). If \(|t-r_j|\le b\), then by (2.1) \(\|(U_j-D_j)(h_j\otimes W_s\eta)\|\ge c\) for \(|s|\le b\), and Lemma 1.3 with \(J=[-b,b]\) gives
\[
\|(U_j-D_j)Qv_0\|^2\ge c^2\,\|E_{S_k}([s_j-b,s_j+b])\xi_k\|^2 ,
\]
because \(e^{itS_k}\) commutes with the spectral projections of \(S_k\). Each factor \(e^{-ir_iX}h\) lies in \(H_l\), so the spectral measure \(\nu_k\) of \(S_k\) at \(\xi_k\) is a probability measure on \([-kl,kl]\). For \(|e|\le kl\) the interval \([e-b,e+b]\) lies in \([-B_j,B_j]\), so the probability over \(s_j\) that \(|e-s_j|\le b\) equals \(b/B_j\). By Fubini's theorem the mean over \(s_j\) of \(\|E_{S_k}([s_j-b,s_j+b])\xi_k\|^2=\nu_k([s_j-b,s_j+b])\) is \(b/B_j\). If \(|t|\le A\), then \([t-b,t+b]\subset[-2A,2A]\) and the probability over \(r_j\) that \(|t-r_j|\le b\) is \(b/(2A)\). The variables \(r_j,s_j\) are independent of each other and of \(t\) and the past, and \(|t|\le A\) has probability at least \(3/4\); this proves the first inequality.

*The second inequality.* Fix \(t\) and the parameters of the first \(k\) steps, so that \(\Psi=\zeta_k-\chi_k\) is fixed. The unitary \(W_{-s_j}\) commutes with \(Q\) and inserting the unit vector \(h_j\) is isometric, so \(\|Q(v-v_0)\|^2=1_{\{|t-r_j|\le b\}}\|(E_{S_k}([s_j-b,s_j+b])\otimes1)\Psi\|^2\). For every real \(e\), the probability over \(s_j\) that \(|e-s_j|\le b\) is at most \(b/B_j\), so by Fubini's theorem for the spectral measure of \(S_k\otimes1\) at \(\Psi\), the mean over \(s_j\) is at most \((b/B_j)\|\Psi\|^2\). For every \(t\) the probability over \(r_j\) that \(|t-r_j|\le b\) is at most \(b/(2A)\). Hence the mean over \(r_j,s_j\) of \(\|Q(v-v_0)\|^2\) is at most \(a_j\|\zeta_k-\chi_k\|^2\), and by (2.2) \(\mathbb E\|Q(v-v_0)\|^2\le a_j\epsilon^2\). Finally \(\|U_j-D_j\|\le2\).

*The contradiction.* By the triangle inequality in the Hilbert space of square-integrable random vectors, (2.4) gives
\[
\big(\mathbb E\|(U_j-D_j)Qv\|^2\big)^{1/2}\ge\Big(\tfrac{\sqrt3}2c-2\epsilon\Big)\sqrt{a_j}>\tfrac c2\sqrt{a_j},
\]
because \(\epsilon<c/8\). By (2.3), the expected loss \(\mathbb E\big(\|\zeta_{j-1}\|^2-\|\zeta_j\|^2\big)=\mathbb E\big(\|v\|^2-\|G_jv\|^2\big)\) at step \(j\) is at least \(c^2a_j/16\). The losses telescope: \(\sum_{j=1}^m\big(\|\zeta_{j-1}\|^2-\|\zeta_j\|^2\big)=1-\|\zeta_m\|^2\le1\). Hence \(\frac{c^2}{16}\sum_{j=1}^ma_j\le1\) for every \(m\). But
\[
\sum_{j=1}^ma_j=\frac{b^2}{2A}\sum_{j=1}^m\frac1{b+1+jl}\longrightarrow\infty\qquad(m\to\infty),
\]
a contradiction. Hence \(U=D\). \(\square\)

The divergence of \(\sum_ja_j\) is the reason for letting the range of the shifts grow linearly: the ideal energy after \(k\) steps can be anywhere in \([-kl,kl]\), and the shift must be able to reach it.

## 3. Exercises

**Exercise 3.1.** Show that \(U=D\) implies \(D(y\otimes1)D^*=L^*yL\) for \(y\in N\) acting on \(H\), and \(L^*bL=1\otimes b\) for \(b\in\mathrm B\) acting on \(K\).

**Exercise 3.2.** Let \(x\in N\) with \(x\Omega\) in the spectral subspace of \(X\) for an interval \([h-\delta,h+\delta]\), and \(a\in\mathrm B\). Show that \(\|xa\Omega-\gamma_h(a)x\Omega\|\le\sup_{|u|\le\delta}\|W_ua\Omega-a\Omega\|\,\|x\Omega\|\).

**Exercise 3.3.** Where does the proof of Theorem 1.1 use that \(N\) is a factor of type III₁?

## 4. Solutions

**3.1.** For \(y\in N\), \(yR(x\Omega\otimes a\Omega)=R(yx\Omega\otimes a\Omega)\), so \(yR=R(y\otimes1)\). With \(R=LD\), \(yLD=LD(y\otimes1)\), so \(L^*yL=D(y\otimes1)D^*\), using \(L^*L=1\). For \(b\in\mathrm B\), \(bL(x\Omega\otimes a\Omega)=bax\Omega=L(x\Omega\otimes ba\Omega)\), so \(bL=L(1\otimes b)\) and \(L^*bL=1\otimes b\).

**3.2.** By Corollary 1.2, \(xa\Omega=L(D(x\Omega\otimes a\Omega))\), and \(\gamma_h(a)x\Omega=L(x\Omega\otimes W_ha\Omega)=L(\exp(ih(1\otimes Y))(x\Omega\otimes a\Omega))\). Since \(L\) is isometric, the difference has norm \(\|(\exp(iX\otimes Y)-\exp(ih\,1\otimes Y))(x\Omega\otimes a\Omega)\|\), which by the product spectral measure equals \(\big(\int\|(W_u-W_h)a\Omega\|^2d\nu(u)\big)^{1/2}\) with \(\nu\) the spectral measure of \(X\) at \(x\Omega\), supported in \([h-\delta,h+\delta]\).

**3.3.** Directly, nowhere. It enters through the previous lessons: the relative bicentralizer flow and the shift maps \(\theta_q\) need admissible families of approximate eigenoperators, which exist because \(N\) is a factor of type III₁; and the isometry of \(R\) and \(L\) uses \(E_{\mathrm B}(x)=\varphi(x)1\) for \(x\in N\), which is the triviality of the bicentralizer of \(N\).

## References

- [OAI] OpenAI, Expected amenable subalgebras preserving core commutants (September 23, 2026), OpenAI Math Release preprint. https://github.com/openai/math/blob/main/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf
