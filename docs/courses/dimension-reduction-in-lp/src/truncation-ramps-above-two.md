# Truncation ramps and exponents above two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the upper bound of Theorem 5.1 of [Finite subsets of L_p](finite-subsets-of-lp.md) for \(2<p<\infty\), and with it the whole theorem [OpenAI-LP, Section 7 and Appendix B]. For \(p>2\) the measure \(\nu\) of [Signed Poisson sums and exponents below two](signed-poisson-sums-below-two.md) has finite second moment only at large sizes, so instead of a heavy-tailed sum we use overlapping truncations of the homogeneous increments \(v\): a *ramp* that counts each size with a multiplicity rising from \(1\) to \(\ell\) and falling back (Section 1). Its \(p\)-energy grows like \(\ell^{p+1}\), while projecting it onto normalized gradients costs only \(O(H^{p-2}\ell)\) in \(p\)-th power (Section 2). Sampling the projected ramp by a signed Poisson sum keeps the \(p\)-th moments up to a factor arbitrarily close to \(1\) (Sections 3 and 4), and truncation on a rare event gives the bounded gradient (Section 5). Moment bounds of this kind for sums of independent variables go back to Rosenthal; the version with leading constant close to \(1\) is proved here.

Notation is as in the previous lessons: points in \(\ell_p^m\), pairs \(E\), normalized gradients \(V\), \(H=4\log(2n)\), the measure \(\nu\) on \(\Omega\) with the increments \(v\) and the identity (1.1) there, and signed Poisson sums. Fix \(p>2\) and \(0<\eta<\frac16\), and put \(\gamma=1-\frac2p\). Given a probability vector \(\lambda\) with positive entries, take \(\sigma\ge\lambda/2\) and \(P=P(\sigma)\) from Lemma 2.1 of [Electrical flows and a weighted projection](electrical-flows-and-a-weighted-projection.md), and let \(\rho=\sigma\otimes\nu\) on \(E\times\Omega\): for a map \(G\colon\Omega\to\mathbb R^E\), \(\|G\|_{L^q(\rho)}^q=\sum_e\sigma_e\int|G_e|^q\,d\nu\). The projection \(P\) acts on the values of \(G\).

## 1. A ramp of truncations

For \(a>0\) let \(v_{\le a}\) have coordinates \(v_e\mathbf 1_{\{|v_e|\le a\}}\), and \(v_{>a}=v-v_{\le a}\). For an integer \(\ell\ge1\) let
\[
u=\sum_{k=0}^{\ell-1}\bigl(v_{\le2^{k+\ell}}-v_{\le2^k}\bigr),\qquad Z=Pu .
\]
Thus \(u_e=v_e\) times the number of \(k\in\{0,\dots,\ell-1\}\) with \(2^k<|v_e|\le2^{k+\ell}\). On the size intervals \((2^j,2^{j+1}]\), \(j=0,\dots,2\ell-2\), this multiplicity is \(1,2,\dots,\ell,\dots,2,1\), and it is \(0\) for \(|v_e|\le1\) and \(|v_e|>2^{2\ell-1}\).

**Lemma 1.1.** For every pair \(e\),
\[
\int|u_e|^p\,d\nu=b:=p\log2\Bigl(\ell^p+2\sum_{j=1}^{\ell-1}j^p\Bigr),\qquad c_p\ell^{p+1}\le b\le C_p\ell^{p+1},\qquad\int|u_e|^2\,d\nu\le C_p .
\]
In particular \(b\ge p\log2>1\), and \(b\) depends only on \(p\) and \(\ell\).

**Proof.** By (1.1) of [Signed Poisson sums and exponents below two](signed-poisson-sums-below-two.md), a size interval \((2^j,2^{j+1}]\) with multiplicity \(\mu\) contributes \(\mu^pp\int_{2^j}^{2^{j+1}}u^pu^{-p-1}\,du=\mu^pp\log2\); this gives \(b\), and \(\sum_{j<\ell}j^p\) is between constant multiples of \(\ell^{p+1}\). By (1.1) again, \(\int|v_e|^2\mathbf 1_{\{|v_e|>a\}}\,d\nu=\frac p{p-2}a^{2-p}\), so the triangle inequality in \(L^2(\nu)\) gives \(\bigl(\int|u_e|^2\,d\nu\bigr)^{1/2}\le\sum_{k<\ell}\bigl(\frac p{p-2}\bigr)^{1/2}2^{(1-p/2)k}\le C_p\). \(\square\)

**Lemma 1.2.** \(\|Z\|_{L^2(\rho)}^2\le C_p\), \(\int|Z_e|^2\,d\nu\le C_pH^2\) for every \(e\), and \(|Z_e(\omega)|\le H2^{2\ell}\) for all \(e\) and \(\omega\).

**Proof.** \(P\) does not increase \(\|\cdot\|_{2,\sigma}\), so \(\|Z\|_{L^2(\rho)}\le\|u\|_{L^2(\rho)}\le C_p^{1/2}\) by Lemma 1.1. Next \(\bigl(\int|Z_e|^2\,d\nu\bigr)^{1/2}\le\sum_f|P_{ef}|\bigl(\int|u_f|^2\,d\nu\bigr)^{1/2}\le HC_p^{1/2}\). Finally each term of \(u\) has absolute value at most \(2^{k+\ell}\), so \(|u_f|<2^{2\ell}\), and the row sums of \(P\) are at most \(H\). \(\square\)

## 2. The projection error

**Lemma 2.1** (OpenAI). \(\|Z-u\|_{L^p(\rho)}^p\le C_pH^{p-2}(\ell+1)\).

**Proof.** For \(0\le k<2\ell\) let \(A_k=(P-I)v_{\le2^k}\). Since \(Pv=v\) pointwise, \(A_k=-(P-I)v_{>2^k}\). The row sums of \(P-I\) are at most \(H+1\le2H\), and \(I-P\) does not increase \(\|\cdot\|_{2,\sigma}\); with the tail integral of Lemma 1.1's proof,
\[
\|A_k\|_\infty\le2H2^k,\qquad\|A_k\|_{L^2(\rho)}\le\|v_{>2^k}\|_{L^2(\rho)}=\Bigl(\frac p{p-2}\Bigr)^{1/2}2^{(1-p/2)k}.
\]
Moreover \(Z-u=(P-I)u=\sum_{k=\ell}^{2\ell-1}A_k-\sum_{k=0}^{\ell-1}A_k\). Summing, \(\|Z-u\|_{L^2(\rho)}\le C_p\) and \(\|Z-u\|_\infty\le4H2^{2\ell}\).

For \(\tau\ge16H\), split the sum into the terms with \(2^k\le\tau/(16H)\), whose sup norms add up to at most \(4H\cdot\tau/(16H)=\tau/4\), and the others, whose \(L^2(\rho)\) norms add up to at most \(C_p(\tau/H)^{1-p/2}\) because \(1-p/2<0\). By Chebyshev's inequality,
\[
\rho(|Z-u|>\tau)\le\rho\bigl(|\text{other terms}|>\tfrac\tau2\bigr)\le C_pH^{p-2}\tau^{-p}\quad(\tau\ge16H),\qquad\rho(|Z-u|>\tau)\le C_p\tau^{-2}\quad(\tau>0),
\]
and \(\rho(|Z-u|>\tau)=0\) for \(\tau\ge4H2^{2\ell}\). Hence
\[
\|Z-u\|_{L^p(\rho)}^p=\int_0^\infty p\tau^{p-1}\rho(|Z-u|>\tau)\,d\tau\le C_p\int_0^{16H}\tau^{p-3}\,d\tau+C_pH^{p-2}\int_{16H}^{4H2^{2\ell}}\frac{d\tau}\tau\le C_pH^{p-2}(\ell+1). \qquad\square
\]

**Corollary 2.2.** \(\sum_e\sigma_e\bigl|\int|Z_e|^p\,d\nu-b\bigr|\le p\,\|Z-u\|_{L^p(\rho)}\bigl(b^{1/p}+\|Z-u\|_{L^p(\rho)}\bigr)^{p-1}\), and \(\|Z-u\|_{L^p(\rho)}\le C_pH^\gamma\ell^{-1}b^{1/p}\).

**Proof.** Pointwise, \(\bigl||Z_e|^p-|u_e|^p\bigr|\le p|Z_e-u_e|\bigl(|u_e|+|Z_e-u_e|\bigr)^{p-1}\) by the mean value theorem. Integrate against \(\rho\), use \(\int|u_e|^p\,d\nu=b\) for every \(e\), Hölder's inequality with exponents \(p\) and \(\frac p{p-1}\), and \(\|u\|_{L^p(\rho)}=b^{1/p}\). The second bound follows from Lemmas 2.1 and 1.1: \(\bigl(C_pH^{p-2}(\ell+1)\bigr)^{1/p}/(c_p\ell^{p+1})^{1/p}\le C_pH^{(p-2)/p}\ell^{-1}\). \(\square\)

## 3. Moments of signed Poisson sums

**Lemma 3.1** (nearly additive moments; OpenAI). Let \(q>2\) and \(\epsilon>0\). For a bounded real \(h\) on a region of finite \(\nu\)-measure and its signed Poisson sum \(S\),
\[
\int|h|^q\,d\nu\le\mathbb E|S|^q\le(1+\epsilon)\int|h|^q\,d\nu+C_{q,\epsilon}\Bigl(\int h^2\,d\nu\Bigr)^{q/2}.
\]

**Proof.** *Independent symmetric sums.* Let \(X_1,\dots,X_N\) be independent symmetric random variables with finite \(q\)-th moments and \(S_j=X_1+\dots+X_j\). For real \(a,b\),
\[
|a|^q+|b|^q\le\tfrac12\bigl(|a+b|^q+|a-b|^q\bigr)\le|a|^q+(1+\epsilon')|b|^q+C_{q,\epsilon'}|a|^{q-2}b^2 .\tag{3.1}
\]
For the left inequality, convexity of \(x\mapsto x^{q/2}\) gives \(\frac12(|a+b|^q+|a-b|^q)\ge(a^2+b^2)^{q/2}\ge|a|^q+|b|^q\). For the right one we may take \(a\neq0\) and divide by \(|a|^q\); with \(t=b/a\), the function \(\phi(t)=\frac12(|1+t|^q+|1-t|^q)\) is twice continuously differentiable with \(\phi(0)=1\) and \(\phi'(0)=0\), so \(\phi(t)\le1+Ct^2\) for \(|t|\le\frac12\); \(\phi(t)/|t|^q\to1\) as \(|t|\to\infty\), so \(\phi(t)\le(1+\epsilon')|t|^q\) for \(|t|\ge t_0\); and on \(\frac12\le|t|\le t_0\), \(\phi(t)\le4\max\phi\cdot t^2\). Since \(X_j\) is symmetric and independent of \(S_{j-1}\),
\[
\mathbb E|S_j|^q=\tfrac12\mathbb E\bigl(|S_{j-1}+X_j|^q+|S_{j-1}-X_j|^q\bigr).
\]
The left half of (3.1) gives \(\mathbb E|S_j|^q\ge\mathbb E|S_{j-1}|^q+\mathbb E|X_j|^q\); hence \(\mathbb E|S_N|^q\ge\sum_j\mathbb E|X_j|^q\), and \(\mathbb E|S_j|^q\le M:=\mathbb E|S_N|^q\) for all \(j\). The right half and Hölder's inequality give
\[
\mathbb E|S_j|^q\le\mathbb E|S_{j-1}|^q+(1+\epsilon')\mathbb E|X_j|^q+C_{q,\epsilon'}M^{1-2/q}\,\mathbb EX_j^2 .
\]
Summing over \(j\) and using Young's inequality \(C_{q,\epsilon'}M^{1-2/q}V\le\theta M+C_{q,\epsilon',\theta}V^{q/2}\),
\[
(1-\theta)M\le(1+\epsilon')\sum_j\mathbb E|X_j|^q+C_{q,\epsilon',\theta}\Bigl(\sum_j\mathbb EX_j^2\Bigr)^{q/2}.
\]
Choose \(\epsilon',\theta\) with \((1+\epsilon')/(1-\theta)\le1+\epsilon\).

*Poisson sums.* Let \(\nu(R)=\kappa\) be the measure of the region, and for an integer \(m'>\kappa\) let \(X_j=\xi_j\varepsilon_jh(\omega_j)\), \(j\le m'\), with independent \(\xi_j\in\{0,1\}\) of mean \(\kappa/m'\), signs \(\varepsilon_j\), and points \(\omega_j\) of law \(\nu|_R/\kappa\). These are independent and symmetric, with \(\sum_j\mathbb E|X_j|^q=\int|h|^q\,d\nu\) and \(\sum_j\mathbb EX_j^2=\int h^2\,d\nu\), so their sum \(S'\) satisfies both bounds. Now \(S'\) has the law of \(\sum_{j\le\beta}\varepsilon_jh(\omega_j)\) with \(\beta\) binomial of parameters \(m',\kappa/m'\), independent of the sequence \((\varepsilon_j,\omega_j)\), while \(S\) is the same sum with a Poisson variable \(N\) of mean \(\kappa\) in place of \(\beta\). The binomial probabilities converge to the Poisson ones as \(m'\to\infty\), so \(\delta_{m'}=\frac12\sum_k|\mathbb P(\beta=k)-\mathbb P(N=k)|\to0\), and \(\beta\) and \(N\) can be coupled with \(\mathbb P(\beta\neq N)=\delta_{m'}\) (put the common mass \(\min\{\mathbb P(\beta=k),\mathbb P(N=k)\}\) on the diagonal). Then, with \(\|h\|_\infty=s\),
\[
\bigl|\mathbb E|S|^q-\mathbb E|S'|^q\bigr|\le s^q\,\mathbb E\bigl[(N^q+\beta^q)\mathbf 1_{\{\beta\neq N\}}\bigr]\le s^q\bigl(\mathbb E(N^q+\beta^q)^2\bigr)^{1/2}\delta_{m'}^{1/2}\to0,
\]
because \(\mathbb Ee^{\beta}=(1+\frac\kappa{m'}(e-1))^{m'}\le e^{\kappa(e-1)}\) bounds the moments of \(\beta\) uniformly in \(m'\). Letting \(m'\to\infty\) proves the lemma. \(\square\)

## 4. Poisson sampling of the projected ramp

The map \(u\), hence \(Z\), vanishes outside \(\mathcal S=\{\omega:\max_e|v_e(\omega)|>1\}\), which has \(\nu(\mathcal S)\le|E|\). Let \(W\) be the signed Poisson sum of \(Z\) on \(\mathcal S\); it lies in \(V\) almost surely. Write \(m_e=\int|Z_e|^p\,d\nu\) and \(a_e=\int|Z_e|^2\,d\nu\).

**Lemma 4.1.** There is \(L\ge1\), depending only on \(p\) and \(\eta\), such that for \(\ell=\lceil LH^\gamma\rceil\)
\[
\sum_e\sigma_e\bigl|\mathbb E|W_e|^p-b\bigr|\le\frac{\eta b}4 .
\]

**Proof.** By Corollary 2.2, \(\|Z-u\|_{L^p(\rho)}\le C_pL^{-1}b^{1/p}\), so for \(L\) large the first bound of Corollary 2.2 gives \(\sum_e\sigma_e|m_e-b|\le\frac{\eta b}8\), and in particular \(\sum_e\sigma_em_e\le(1+\frac\eta8)b\). By Lemma 3.1 with \(q=p\) and \(\epsilon=\eta/32\), applied to each coordinate \(Z_e\) (the sum of the coordinate is the coordinate of the sum),
\[
0\le\mathbb E|W_e|^p-m_e\le\epsilon m_e+C_{p,\eta}a_e^{p/2}.
\]
Averaging, \(\epsilon\sum_e\sigma_em_e\le\frac{\eta b}{16}\). By Lemma 1.2, \(\sum_e\sigma_ea_e^{p/2}\le(\max_ea_e)^{p/2-1}\sum_e\sigma_ea_e\le C_pH^{p-2}\), and by Lemma 1.1, \(H^{p-2}/b\le C_pH^{p-2}\ell^{-p-1}\le C_pL^{-p-1}H^{p-2-\gamma(p+1)}=C_pL^{-p-1}H^{-\gamma}\le C_pL^{-p-1}\). Enlarging \(L\), \(C_{p,\eta}\sum_e\sigma_ea_e^{p/2}\le\frac{\eta b}{16}\). Adding the three contributions gives \(\frac\eta8b+\frac\eta{16}b+\frac\eta{16}b=\frac\eta4b\). \(\square\)

## 5. A bounded random gradient

Fix \(L\) as in Lemma 4.1, \(\ell=\lceil LH^\gamma\rceil\), and let \(J=C_p'H2^{2\ell}\ge1\) with \(C_p'\) chosen so that \(J\ge\sup|Z|\) and \(J^2\ge\max_ea_e\) (Lemma 1.2). By Lemma 2.2 of [Signed Poisson sums and exponents below two](signed-poisson-sums-below-two.md), and \(\cosh s-1\le C_0s^2\) for \(|s|\le1\),
\[
\mathbb Ee^{\pm W_e/J}=\exp\Bigl(\int\bigl(\cosh(Z_e/J)-1\bigr)\,d\nu\Bigr)\le e^{C_0a_e/J^2}\le e^{C_0},
\]
so \(\mathbb P(|W_e|>Jz)\le2e^{C_0-z}\) for \(z\ge0\), and \(\mathbb E|W_e|^{2p}\le C_pJ^{2p}\). Let
\[
K=8J\log(2n),\qquad\mathcal B=\{\max_e|W_e|>K\},\qquad F=W\mathbf 1_{\mathcal B^c}.
\]
Then \(F\in V\), \(\|F\|_\infty\le K\), and \(\mathbb P(\mathcal B)\le|E|\cdot2e^{C_0}(2n)^{-8}\le Cn^{-6}\). By the Cauchy–Schwarz inequality, for every pair,
\[
0\le\mathbb E|W_e|^p-\mathbb E|F_e|^p=\mathbb E\bigl[|W_e|^p\mathbf 1_{\mathcal B}\bigr]\le\bigl(\mathbb E|W_e|^{2p}\bigr)^{1/2}\mathbb P(\mathcal B)^{1/2}\le C_pJ^pn^{-3}.\tag{5.1}
\]

**Proposition 5.1** (OpenAI). Let \(p>2\) and \(0<\eta<\frac16\). There is \(n_0\), depending only on \(p\) and \(\eta\), such that for \(n\ge n_0\) the numbers \(b\) of Lemma 1.1 (with \(\ell=\lceil LH^\gamma\rceil\)) and \(K\) above satisfy \(b\ge1\), \(\log K\le C_{p,\eta}(\log n)^{1-2/p}\), and for every \(n\) distinct points of every \(\ell_p^m\) and every \(\lambda\) the gradient \(F\) satisfies (3.1) of [Weighted moments and sampling](weighted-moments-and-sampling.md).

**Proof.** \(\log J=\log C_p'+\log H+2\ell\log2\le C_{p,\eta}H^\gamma\), which is small compared with \(\log n\) because \(\gamma<1\); so the right side of (5.1) tends to \(0\) uniformly in the points and in \(\lambda\), and is at most \(\frac{\eta}4\le\frac{\eta b}4\) for \(n\ge n_0\). With Lemma 4.1, \(\sum_e\sigma_e\bigl|\mathbb E|F_e|^p-b\bigr|\le\frac{\eta b}2\), hence (3.1) since \(\lambda\le2\sigma\). Finally \(\log K=\log8+\log J+\log\log(2n)\le C_{p,\eta}(\log n)^{1-2/p}\). The numbers \(b\) and \(K\) depend only on \(p\), \(\eta\) and \(n\). \(\square\)

With Proposition 4.1 of [Weighted moments and sampling](weighted-moments-and-sampling.md) and Proposition 4.2 of [Signed Poisson sums and exponents below two](signed-poisson-sums-below-two.md), this proves the upper bound of Theorem 5.1 for all \(1<p<\infty\), \(p\neq2\), and so the whole theorem:

**Theorem 5.1** (OpenAI 2026). For \(1<p<\infty\), \(p\neq2\), and \(D>1\): \(\frac{\log n}{\log(1+2D)}\le d_p(n,D)\le\exp\bigl(C_{p,D}(\log n)^{\gamma(p)}\bigr)\), with \(\gamma(p)=2-p\) for \(p<2\) and \(\gamma(p)=1-\frac2p\) for \(p>2\); and \(\lfloor\frac{n-1}4\rfloor^2\le d_p(n,1)\le\binom n2\) for \(n\ge9\).

## 6. Exercises

**Exercise 6.1** (easy). For \(\ell=4\), list the multiplicities of the ramp on \((2^j,2^{j+1}]\), \(j=0,\dots,6\), and compute \(b\).

**Exercise 6.2** (easy). Show that \(\int|v_e|^2\mathbf 1_{\{|v_e|>a\}}\,d\nu=\frac p{p-2}a^{2-p}\) for \(p>2\), and that \(\int|v_e|^2\mathbf 1_{\{|v_e|\le1\}}\,d\nu=\infty\).

**Exercise 6.3** (medium). For independent symmetric \(X_1,\dots,X_N\) with finite fourth moments and \(S=\sum_jX_j\), show that \(\mathbb ES^4=\sum_j\mathbb EX_j^4+3\bigl[(\sum_j\mathbb EX_j^2)^2-\sum_j(\mathbb EX_j^2)^2\bigr]\). Deduce the bound of the first part of the proof of Lemma 3.1 for \(q=4\) with leading constant \(1\) and second constant \(3\).

**Exercise 6.4** (medium). Explain the choice \(\ell\approx LH^\gamma\): what goes wrong if \(\ell\) is fixed, and what if \(\ell\) is of order \(\log n\)?

## 7. Solutions

**6.1.** The multiplicities are \(1,2,3,4,3,2,1\), so \(b=p\log2\,(1+2^p+3^p+4^p+3^p+2^p+1)=p\log2\,(4^p+2\cdot3^p+2\cdot2^p+2)\).

**6.2.** By (1.1), the first is \(p\int_a^\infty u^{2-p-1}\,du=\frac p{p-2}a^{2-p}\), and the second is \(p\int_0^1u^{1-p}\,du=\infty\) since \(p\ge2\).

**6.3.** Expanding \(S^4\), every product containing some \(X_j\) to an odd power has expectation \(0\) by symmetry and independence. What remains is \(\sum_j\mathbb EX_j^4+6\sum_{j<k}\mathbb EX_j^2\,\mathbb EX_k^2\), and \(2\sum_{j<k}\mathbb EX_j^2\mathbb EX_k^2=(\sum_j\mathbb EX_j^2)^2-\sum_j(\mathbb EX_j^2)^2\). Hence \(\sum_j\mathbb EX_j^4\le\mathbb ES^4\le\sum_j\mathbb EX_j^4+3(\sum_j\mathbb EX_j^2)^2\). For general \(q>2\) no such exact expansion exists, which is why the proof works with (3.1).

**6.4.** The relative projection error is about \(H^\gamma/\ell\) (Corollary 2.2), so a fixed \(\ell\) gives an error that grows with \(n\). The size bound is about \(J\approx H2^{2\ell}\), and the dimension grows like \(K^{2p}\), so \(\ell\) of order \(\log n\) would give polynomial dimension. The choice \(\ell\approx LH^\gamma\) makes the error a small constant and keeps \(\log K\) of order \((\log n)^\gamma\).

## References

- [OpenAI-LP] OpenAI, *Subpolynomial dimension reduction in L_p*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/Subpolynomial-dimension-reduction-in-Lp-September-23-2026
