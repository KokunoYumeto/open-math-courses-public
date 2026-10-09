# The Hankel test

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof of the free corner estimate [OpenAI-288, Section 5]. The two free symmetries \(d\in D\) and \(s\in A_0\) of the previous lesson generate a copy of the group algebra of the infinite dihedral group, and its corner by \(p=\frac12(1+d)\) consists of even functions of the Haar unitary \(w=ds\); this corner is free from \(pDp\). Compressing a function supported on a narrow arc to the small projection \(e\le p\) produces an element \(h\in e\mathcal Le\) of norm of order \(u=2t\). Its compression to the subspace built from orthogonal copies of \(L^2(A_0)\) is \(u\) times a Toeplitz operator plus a Hankel operator tensored with \(L_s\), and only the Hankel part sees the commutator with \(L_s\). For a narrow arc the Hankel matrix has norm at least \(1/\pi^2\), whatever the width of the arc. Comparing with the upper bound of the previous lesson, the factor \(u\) cancels.

We keep the standing hypotheses and notation of [Invariant tensors and the word structure](invariant-tensors-and-the-word-structure.md) and of [Propagation from small corners](propagation-from-small-corners.md): \(e\le p\) in \(D\), \(d=2p-1\), \(w=ds\), \(u=2t=\tau_p(e)\) with \(\tau_p=2\tau|_{p\mathcal Lp}\), the isometries \(U_k\), the subspace \(\mathcal K\), the inclusion \(\iota\) and \(J=I\otimes B_0\). We use [Words in free subalgebras](words-in-free-subalgebras.md) (Theorem 1.3, Lemmas 2.1 and 2.2), and the Borel functional calculus of a self-adjoint operator with the spectral measure of a vector, [Theorem 3.1 and Proposition 2.1 of The spectral theorem for bounded self-adjoint operators](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators#OA-FND-ST-03). We write \(m\) for the normalized Haar measure on the unit circle \(\mathbb T\).

## 1. The dihedral corner

Let \(\mathcal C=W^*(d,s)\). The subalgebras \(W^*(d)=\mathbb C1+\mathbb Cd\) and \(W^*(s)=\mathbb C1+\mathbb Cs\) of \(D\) and \(A_0\) are free, with one-dimensional centred parts spanned by the unit vectors \(d\) and \(s\).

**Lemma 1.1** (the dihedral algebra).

1. The vectors \(w^l\) and \(w^ld\), \(l\in\mathbb Z\), form an orthonormal basis of \(L^2(\mathcal C)\). In particular \(w\) is a Haar unitary, and \(dwd=w^{-1}\).
2. For \(l\in\mathbb Z\), \(pw^lp=pw^ldp=\frac12(w^l+w^{-l})p\).
3. The linear span of \(\{pw^lp:l\ge0\}\) is dense in \(L^2(p\mathcal Cp)\), and the centred elements of this span are the combinations of \(pw^lp\), \(l\ge1\).
4. \(pDp\) and \(p\mathcal Cp\) are free subalgebras of \((p\mathcal Lp,\tau_p)\).

**Proof.** (1) By Theorem 1.3 of the free words lesson, \(1\) and the alternating words in \(d\) and \(s\) form an orthonormal basis of \(L^2(\mathcal C)\). Since \(d^2=s^2=1\), these words are \((ds)^l=w^l\), \((sd)^l=w^{-l}\), \((ds)^ld=w^ld\) and \((sd)^{l-1}s=w^{-l}d\) for \(l\ge1\), together with \(d=w^0d\) and \(1=w^0\). For \(l\ne0\), \(w^l\) is a nonempty alternating word, so \(\tau(w^l)=0\). Finally \(dwd=d\,ds\,d=sd=w^{-1}\).

(2) Since \(dw^ld=w^{-l}\), we have \(dw^l=w^{-l}d\), and \(\frac14(1+d)w^l(1+d)=\frac14(w^l+w^{-l}+w^ld+w^{-l}d)=\frac12(w^l+w^{-l})\cdot\frac12(1+d)\). Also \(dp=p\), so \(pw^ldp=pw^lp\).

(3) Every element \(y\) of \(p\mathcal Cp\) is a vector of \(L^2(\mathcal C)\), hence an \(L^2\)-limit of finite combinations \(X_n\) of the basis vectors in (1). Left and right multiplication by \(p\) are bounded on \(L^2\), so \(pX_np\to pyp=y\), and by (2) each \(pX_np\) lies in the span of the \(pw^lp\), \(l\ge0\). For \(l\ge1\), \(\tau_p(pw^lp)=2\tau(w^lp)=\tau(w^l)+\tau(w^ld)=0\) by (1), because \(w^l\) and \(w^ld\) are basis vectors orthogonal to \(1\); and \(pw^0p=p\) has \(\tau_p(p)=1\). So a combination is centred exactly when the coefficient of \(p\) vanishes.

(4) Let \(a_1,\dots,a_j\in pDp\) be centred for \(\tau_p\); then \(\tau(a_i)=0\) and \(a_id=a_ipd=a_ip=a_i\). For \(l_1,\dots,l_j\ge1\), absorbing the projections \(p\) into the \(a_i\) and using traciality,
\[
\tau_p\big(a_1pw^{l_1}p\,a_2pw^{l_2}p\cdots a_jpw^{l_j}p\big)=2\tau\big(a_1w^{l_1}a_2w^{l_2}\cdots a_jw^{l_j}\big)=2\tau\big(a_1s(ds)^{l_1-1}\,a_2s(ds)^{l_2-1}\cdots a_js(ds)^{l_j-1}\big),
\]
because \(a_iw^{l}=a_ids(ds)^{l-1}=a_is(ds)^{l-1}\). The last product is a centred alternating word in \(D\) and \(A_0\) (each block \(s(ds)^{l-1}\) begins and ends with \(s\)), so the trace is \(0\). By (3), every centred element of \(p\mathcal Cp\) is an \(L^2\)-limit of centred combinations of the \(pw^lp\), \(l\ge1\). The trace of a product is continuous in each factor for the \(L^2\)-norm when the other factors are fixed and bounded, since \(|\tau(XYZ)|\le\|ZX\|\,\|Y\|_2\); replacing the factors from \(p\mathcal Cp\) one at a time extends the vanishing to all alternating products \(a_1c_1\cdots a_jc_j\) with centred \(a_i\in pDp\) and \(c_i\in p\mathcal Cp\). Products of odd length have both ends in the same algebra; move one end next to the other by traciality, split their product into its scalar and centred parts, and use the even case together with induction on the length. Products of even length beginning in \(p\mathcal Cp\) are rotated into the treated form. \(\square\)

Let \(c=\frac12(w+w^*)\), a self-adjoint element of \(\mathcal C\) with \(\|c\|\le1\). Since \(dwd=w^{-1}\), \(c\) commutes with \(d\) and \(p\), and so does \(g(c)\) for every bounded Borel function \(g\) on \([-1,1]\).

**Lemma 1.2** (even functions of \(w\)). Let \(g\) be a bounded Borel function on \([-1,1]\). Then \(g(c)\in\mathcal C\), \(b=g(c)p\in p\mathcal Cp\), \(\|b\|\le\sup|g|\), and for every \(l\in\mathbb Z\)
\[
\tau(g(c)w^l)=\int_{\mathbb T}g(\operatorname{Re}z)\,z^l\,dm(z),\qquad \tau(g(c)w^ld)=0 .
\tag{1.1}
\]
Consequently \(\tau_p(b)=\int g(\operatorname{Re}z)\,dm\) and \(\|b\|_{2,\tau_p}^2=\int|g(\operatorname{Re}z)|^2\,dm\).

**Proof.** The functional calculus of \(c\) lies in the von Neumann algebra \(W^*(c)\subseteq\mathcal C\) and has norm at most \(\sup|g|\). For a polynomial \(g\), (1.1) follows by expanding \(c=\frac12(w+w^{-1})\) and using Lemma 1.1(1): \(\tau(w^k)=\delta_{k,0}\) and \(\tau(w^kd)=0\), while \(\int z^k\,dm=\delta_{k,0}\). Let \(\nu\) be the spectral measure of the vector \(1\in L^2(\mathcal L)\) for \(c\), so that \(\|f(c)1\|_2^2=\int|f|^2d\nu\) for bounded Borel \(f\). By the polynomial case, \(\int P\,d\nu=\tau(P(c))=\int P(\operatorname{Re}z)\,dm\) for all polynomials \(P\), so \(\nu\) is the image of \(m\) under \(z\mapsto\operatorname{Re}z\) (a finite measure on \([-1,1]\) is determined by its moments, by Weierstrass approximation). Choose polynomials \(P_n\to g\) in \(L^2(\nu)\). Then \(\|g(c)-P_n(c)\|_2\to0\), and both sides of (1.1) are continuous for this convergence: the left side because \(\tau(Yw^l)=\langle Y,w^{-l}\rangle\), the right side because \(\int|g-P_n|^2(\operatorname{Re}z)\,dm=\int|g-P_n|^2\,d\nu\). The same applies to \(\tau(g(c)w^ld)\). Finally \(\tau_p(b)=2\tau(g(c)\frac12(1+d))=\tau(g(c))+\tau(g(c)d)\), and \(\|b\|_{2,\tau_p}^2=\tau_p(|g|^2(c)p)\) is computed in the same way. \(\square\)

## 2. Free compression

**Lemma 2.1.** Let \(b=b^*\in p\mathcal Cp\) with \(\tau_p(b)=0\). Then
\[
E_{\mathcal C}(ebe)=u^2b,\qquad \|ebe\|\le2\sqrt u\,\|b\|_{2,\tau_p}+u\|b\| ,
\tag{2.1}
\]
where \(E_{\mathcal C}\) is the trace-preserving conditional expectation of \(\mathcal L\) onto \(\mathcal C\).

**Proof.** Put \(\mathcal A=pDp\), \(\mathcal Z=p\mathcal Cp\) and \(a=e-up\in\mathcal A\), so \(\tau_p(a)=0\). Since \(p\in\mathcal C\), bimodularity shows that \(E_{\mathcal C}(ebe)=E_{\mathcal C}(p\,ebe\,p)\) lies in \(\mathcal Z\), and on \(p\mathcal Lp\) the map \(E_{\mathcal C}\) is the \(\tau_p\)-preserving expectation \(E_{\mathcal Z}\) onto \(\mathcal Z\). Expand
\[
ebe=u^2b+u(ab+ba)+aba .
\]
By freeness (Lemma 1.1(4)), \(\tau_p(zab)=\tau_p(a\,bz)=0\) and \(\tau_p(zba)=0\) for \(z\in\mathcal Z\) (write \(bz\) as scalar plus centred part), so \(E_{\mathcal Z}(ab)=E_{\mathcal Z}(ba)=0\). For \(z=z^\circ+\tau_p(z)p\in\mathcal Z\), \(\tau_p(z^\circ aba)=0\) since \(z^\circ aba\) is a centred alternating word, and \(\tau_p(aba)=\tau_p(ba^2)=\tau_p(b)\tau_p(a^2)=0\). So \(E_{\mathcal Z}(aba)=0\), proving the first identity.

For the norm, work in \(H_c=L^2(W^*(\mathcal A,\mathcal Z),\tau_p)\), a faithful representation of \(W^*(\mathcal A,\mathcal Z)\subseteq p\mathcal Lp\), so operator norms there are algebra norms. By Lemma 2.1 of the free words lesson, \(H_c=L^2(\mathcal A)\otimes\mathcal F_0\), where \(\mathcal F_0\) is the closed span of \(p\) and the words beginning with a centred letter of \(\mathcal Z\), and \(L_e=\lambda(e)\otimes I\). The projection \(\Pi\) onto the closed span of the words beginning with a centred letter of \(\mathcal Z\) is \(|p\rangle\langle p|\otimes Q_0\), with \(Q_0\) the projection of \(\mathcal F_0\) onto the orthogonal complement of \(\mathbb Cp\). Hence
\[
\|L_e\Pi\|=\|\Pi L_e\|\le\|ep\|_{2,\tau_p}=\sqrt{\tau_p(e)}=\sqrt u .
\tag{2.2}
\]
Let \(T=L_b\) on \(H_c\); we split it into its creation, diagonal and annihilation parts [Ricard-Xu]. Because \(b\) is centred, on \(p\) and on the words beginning with a centred letter of \(\mathcal A\) it prefixes the letter \(b\); so \((1-\Pi)T(1-\Pi)=0\) and \(\|\Pi T(1-\Pi)\|\le\|b\|_{2,\tau_p}\). Since \(T\) is self-adjoint, also \(\|(1-\Pi)T\Pi\|\le\|b\|_{2,\tau_p}\), and \(\|\Pi T\Pi\|\le\|b\|\). Using \(\|L_e\|\le1\) and (2.2),
\[
\|ebe\|=\|L_eTL_e\|\le\|L_e\Pi T(1-\Pi)L_e\|+\|L_e(1-\Pi)T\Pi L_e\|+\|L_e\Pi T\Pi L_e\|\le2\sqrt u\,\|b\|_{2,\tau_p}+u\|b\| .\qquad\square
\]

## 3. Toeplitz and Hankel coefficients

Let \(g\) be a real bounded Borel function on \([-1,1]\) with \(\int g(\operatorname{Re}z)\,dm=0\), and put
\[
b_g=g(c)p,\qquad h=eb_ge\in e\mathcal Le,\qquad \gamma_l=\int_{\mathbb T}g(\operatorname{Re}z)\,z^l\,dm(z)\quad(l\in\mathbb Z).
\]
By Lemma 1.2, \(b_g\) is self-adjoint, lies in \(p\mathcal Cp\) and has \(\tau_p(b_g)=0\); the numbers \(\gamma_l\) are real and \(\gamma_{-l}=\gamma_l\).

**Proposition 3.1.** For \(j,k\ge0\),
\[
U_j^*L_hU_k=u\big(\gamma_{j-k}I_B+\gamma_{j+k+1}L_s|_B\big).
\tag{3.1}
\]
Consequently
\[
\iota^*L_h\iota=u\big(T_g\otimes I_B+H_g\otimes L_s|_B\big),\qquad \big\|[J,\iota^*L_h\iota]\big\|=u\,\|H_g\|\,\big\|[B_0,L_s|_B]\big\|,
\tag{3.2}
\]
where \(T_g=(\gamma_{j-k})_{j,k\ge0}\) and \(H_g=(\gamma_{j+k+1})_{j,k\ge0}\) are bounded operators on \(\ell^2(\mathbb N_0)\) of norm at most \(\sup|g|\).

**Proof.** For \(v,z\in A_0\), since \(eh=he=h\) and \(U_kv=t^{-1/2}ew^{-k}v\),
\[
\langle L_hU_kv,U_jz\rangle=t^{-1}\tau(z^*w^jhw^{-k}v)=\big\langle t^{-1}E_{A_0}(w^jhw^{-k})\,v,\,z\big\rangle .
\]
The element \(w^jhw^{-k}\) lies in the von Neumann algebra generated by \(D\) and \(W^*(s)\), so Lemma 2.2 of the free words lesson gives \(E_{A_0}(w^jhw^{-k})=E_{W^*(s)}(w^jhw^{-k})=E_{W^*(s)}E_{\mathcal C}(w^jhw^{-k})\), the last step because \(W^*(s)\subseteq\mathcal C\). By Lemma 2.1 and bimodularity, \(E_{\mathcal C}(w^jhw^{-k})=u^2w^jb_gw^{-k}\). Since \(g(c)\) commutes with \(w\), and \(dw^{-k}=w^kd\) and \(d=ws\),
\[
w^jb_gw^{-k}=g(c)\,w^jpw^{-k}=\tfrac12g(c)\big(w^{j-k}+w^{j+k}d\big)=\tfrac12g(c)\big(w^{j-k}+w^{j+k+1}s\big).
\]
The space \(L^2(W^*(s))\) has the orthonormal basis \(1,s\). By (1.1), \(\tau(g(c)w^l)=\gamma_l\), and \(\langle g(c)w^l,s\rangle=\tau(g(c)w^ls)=\tau(g(c)w^{l-1}d)=0\), using \(s=dw\) and \(w^ld=dw^{-l}\). Hence \(E_{W^*(s)}(g(c)w^l)=\gamma_l1\) and, by bimodularity, \(E_{W^*(s)}(g(c)w^ls)=\gamma_ls\). Therefore
\[
t^{-1}E_{A_0}(w^jhw^{-k})=\frac{u^2}{2t}\big(\gamma_{j-k}1+\gamma_{j+k+1}s\big)=u\big(\gamma_{j-k}1+\gamma_{j+k+1}s\big),
\]
which gives (3.1) on \(A_0\), hence on \(B\) by density.

Let \(M_f\) be multiplication by \(f(z)=g(\operatorname{Re}z)\) on \(L^2(\mathbb T,m)\), of norm at most \(\sup|g|\), and decompose \(L^2(\mathbb T,m)\supseteq\mathcal H_-\oplus\mathcal H_+\) with orthonormal bases \(z^{-j}\) (\(j\ge0\)) and \(z^{k+1}\) (\(k\ge0\)). Then \(\langle M_fz^{-k},z^{-j}\rangle=\gamma_{j-k}\) and \(\langle M_fz^{k+1},z^{-j}\rangle=\gamma_{j+k+1}\), so \(T_g\) and \(H_g\) are blocks of \(M_f\), of norm at most \(\sup|g|\). The matrix of \(\iota^*L_h\iota\) with respect to \(\mathcal K=\bigoplus_kU_kB\) has entries (3.1), which is the first identity of (3.2) on finitely supported vectors, and by continuity everywhere. Since \(J=I\otimes B_0\) commutes with \(T_g\otimes I_B\), \([J,\iota^*L_h\iota]=uH_g\otimes[B_0,L_s|_B]\), and the norm of a tensor product of operators is the product of the norms. \(\square\)

## 4. Proof of the free corner estimate

**Proof of Theorem 1.1 of the word structure lesson.** By Lemma 3.1 there, we may assume that \(G\) commutes with all \(W_u\), and by Corollary 7.2 there it suffices to show \(\|[B_0,L_s|_B]\|\le c_1\varepsilon\).

Put \(\theta=u/4=1/(2N)\in(0,\frac14]\) and \(g(x)=\mathbf 1_{[\cos\theta,1]}(x)-\theta/\pi\) on \([-1,1]\). For \(z=e^{i\alpha}\), \(-\pi<\alpha\le\pi\), we have \(g(\operatorname{Re}z)=\mathbf 1_{[-\theta,\theta]}(\alpha)-\theta/\pi\), a real function of mean zero. By Lemma 1.2, \(\|b_g\|\le1\) and
\[
\|b_g\|_{2,\tau_p}^2=\int|g(\operatorname{Re}z)|^2\,dm=\frac\theta\pi\Big(1-\frac\theta\pi\Big)\le u .
\]
Lemma 2.1 gives
\[
\|h\|=\|eb_ge\|\le2\sqrt u\cdot\sqrt u+u=3u .
\tag{4.1}
\]
For \(l\ge1\), \(\gamma_l=\frac1{2\pi}\int_{-\theta}^{\theta}e^{il\alpha}\,d\alpha=\frac{\sin(l\theta)}{\pi l}\). If \(0\le j,k<N\), then \(1\le j+k+1\le2N-1\) and \((j+k+1)\theta<1<\frac\pi2\). The concavity of \(\sin\) on \([0,\frac\pi2]\) gives \(\sin x\ge\frac{2x}\pi\) there, so
\[
(H_g)_{jk}=\gamma_{j+k+1}\ge\frac{2\theta}{\pi^2}\qquad(0\le j,k<N).
\]
Testing \(H_g\) on the unit vector \(N^{-1/2}(1,\dots,1,0,0,\dots)\) with \(N\) leading ones,
\[
\|H_g\|\ge\frac1N\sum_{j,k<N}\gamma_{j+k+1}\ge\frac{2\theta N}{\pi^2}=\frac1{\pi^2}.
\tag{4.2}
\]
Combine (3.2), Lemma 3.1 of the propagation lesson and (4.1):
\[
\frac u{\pi^2}\big\|[B_0,L_s|_B]\big\|\le u\|H_g\|\,\big\|[B_0,L_s|_B]\big\|=\big\|[J,\iota^*L_h\iota]\big\|\le(1+4c_0)\varepsilon\|h\|\le3u(1+4c_0)\varepsilon .
\]
Dividing by \(u>0\) gives \(\|[B_0,L_s|_B]\|\le3\pi^2(1+4c_0)\varepsilon=c_1\varepsilon\). \(\square\)

The upper bound for \(\|h\|\) and the lower bound for the Hankel part are both proportional to \(u\), the relative size of the corner, and the factor \(u\) cancels. This is where the estimate becomes independent of the corner, and therefore, in the next lesson, independent of the matrix size.

## 5. Exercises

**Exercise 5.1.** Show that \(\gamma_0=0\), \(\gamma_{-l}=\gamma_l\) and \(\gamma_l=\sin(l\theta)/(\pi l)\) for the function \(g\) of Section 4, and that \(\sum_l\gamma_l^2=\frac\theta\pi(1-\frac\theta\pi)\).

**Exercise 5.2.** Take \(g(x)=2x\), so \(g(\operatorname{Re}z)=z+z^{-1}\). Compute \(\gamma_l\), \(T_g\) and \(H_g\), and write \(\iota^*L_h\iota\) explicitly.

**Exercise 5.3.** Show that \(c=\frac12(w+w^*)\) commutes with \(d\), and that \(pcp=cp=\frac12(w+w^{-1})p\).

**Exercise 5.4.** Prove \(\sin x\ge2x/\pi\) for \(0\le x\le\pi/2\).

## 6. Solutions

**Solution 5.1.** \(\gamma_0=\int g(\operatorname{Re}z)\,dm=\frac{2\theta}{2\pi}-\frac\theta\pi=0\). The function \(\alpha\mapsto g(\cos\alpha)\) is even and real, so \(\gamma_{-l}=\overline{\gamma_l}=\gamma_l\). For \(l\ge1\) the constant \(-\theta/\pi\) contributes nothing, and \(\frac1{2\pi}\int_{-\theta}^\theta e^{il\alpha}d\alpha=\frac{\sin l\theta}{\pi l}\). The \(\gamma_l\) are the Fourier coefficients of \(f(z)=g(\operatorname{Re}z)\), so Parseval gives \(\sum_l\gamma_l^2=\int f^2\,dm=\frac\theta\pi(1-\frac\theta\pi)^2+(1-\frac\theta\pi)\frac{\theta^2}{\pi^2}=\frac\theta\pi(1-\frac\theta\pi)\).

**Solution 5.2.** \(\gamma_{\pm1}=1\) and all other \(\gamma_l=0\). So \(T_g\) is the sum of the unilateral shift and its adjoint, and \(H_g\) has the single entry \((H_g)_{00}=\gamma_1=1\). Hence \(\iota^*L_h\iota=u\big((S+S^*)\otimes I_B+|e_0\rangle\langle e_0|\otimes L_s|_B\big)\) with \(S\) the shift: the element \(h\) moves between neighbouring word levels, and \(L_s\) appears only at level zero.

**Solution 5.3.** \(dcd=\frac12(dwd+dw^*d)=\frac12(w^{-1}+w)=c\), so \(c\) commutes with \(d\) and with \(p\). By Lemma 1.1(2) with \(l=1\), \(pwp=\frac12(w+w^{-1})p=cp\), and \(pcp=cp\) since \(c\) commutes with \(p\).

**Solution 5.4.** \(\sin\) is concave on \([0,\frac\pi2]\), so it lies above the chord joining \((0,0)\) and \((\frac\pi2,1)\), which is \(x\mapsto2x/\pi\).

## References

- [OpenAI-288] OpenAI, Kadison's similarity theorem through uniform derivation estimates, preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026
- [Ricard-Xu] É. Ricard, Q. Xu, Khintchine type inequalities for reduced free products and applications, Journal für die reine und angewandte Mathematik 599 (2006), 27–59 (the decomposition of the left action of a letter into creation, diagonal and annihilation parts). https://arxiv.org/abs/math/0505302
