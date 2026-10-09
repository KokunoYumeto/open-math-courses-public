# Cuts and a flat cubic

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson provides the two tools of the proof in [A stopped walk and the cotype of ℓ₁](a-stopped-walk-and-the-cotype-of-l1.md) [OpenAI-C, Sections 2 and 3]. First, finitely many points of \(\ell_1\) are written as *weighted cuts*: binary vectors \(z_i\) indexed by subsets of the points, with weights, such that \(\ell_1\)-distances become weighted Hamming distances, and with an affine map back into \(\ell_1\) that does not increase distances (Lemma 1.1). Since a weighted Hamming distance between binary vectors is also the square of a weighted Euclidean distance, squared \(\ell_1\)-distances become fourth powers of Hilbert distances. Second, the cubic \(\phi(r)=3r^2-2r^3\), applied to each coordinate of \([0,1]\)-valued vectors, is *flat* at the binary points: its derivative vanishes at \(0\) and \(1\). Lemma 2.1 bounds the squared size of its increments by the second-order remainder of a fourth-power Hilbert potential, and Lemma 3.1 sums these bounds along a harmonic function of a Markov chain, where the first-order terms cancel.

We use the finite Markov chains of [Markov chains and metric Markov cotype](markov-chains-and-metric-markov-cotype.md), Section 1.

## 1. Cuts

The real space \(\ell_1\) consists of the real sequences \(x=(x(k))_{k\ge1}\) with \(\|x\|_1=\sum_k|x(k)|<\infty\). For a finite set \(\mathcal B\) and positive weights \((w_B)_{B\in\mathcal B}\), write for \(u\in\mathbb R^{\mathcal B}\)
\[
\|u\|_{1,w}=\sum_{B\in\mathcal B}w_B|u_B|,\qquad\|u\|_H^2=\sum_{B\in\mathcal B}w_Bu_B^2,\qquad\langle u,u'\rangle_H=\sum_Bw_Bu_Bu'_B.
\]
For binary vectors \(z,z'\in\{0,1\}^{\mathcal B}\), \(|z_B-z'_B|=(z_B-z'_B)^2\), so \(\|z-z'\|_{1,w}=\|z-z'\|_H^2\).

**Lemma 1.1** (cut representation). Let \(x_1,\dots,x_n\in\ell_1\), not all equal. There are a finite set \(\mathcal B\) of nonempty proper subsets of \([n]\), positive weights \(w_B\), the binary vectors \(z_i=(\mathbf 1_{i\in B})_{B\in\mathcal B}\), and an affine map \(T:\mathbb R^{\mathcal B}\to\ell_1\) such that
\[
T(z_i)=x_i,\qquad\|x_i-x_j\|_1=\|z_i-z_j\|_{1,w}=\|z_i-z_j\|_H^2,\qquad\|T(u)-T(u')\|_1\le\|u-u'\|_{1,w}.\tag{1.1}
\]

**Proof.** Let \(v(k)=\min_ix_i(k)\) and, for each nonempty proper \(B\subset[n]\),
\[
b_B(k)=\Bigl(\min_{i\in B}x_i(k)-\max_{i\notin B}x_i(k)\Bigr)_+,
\]
where \(r_+=\max\{r,0\}\). Since \(|v(k)|\le\sum_i|x_i(k)|\) and \(0\le b_B(k)\le2\sum_i|x_i(k)|\), \(v\) and \(b_B\) lie in \(\ell_1\). Let \(\mathcal B\) be the set of \(B\) with \(w_B=\|b_B\|_1>0\), and \(T(u)=v+\sum_{B\in\mathcal B}u_Bb_B\).

Fix \(k\), and let \(\alpha_1<\dots<\alpha_m\) be the distinct values among \(x_1(k),\dots,x_n(k)\). If \(B\) is not of the form \(\{i:x_i(k)\ge\alpha\}\), some \(i\in B\) and \(j\notin B\) have \(x_i(k)\le x_j(k)\), and then \(b_B(k)=0\). The sets \(B_r=\{i:x_i(k)\ge\alpha_{r+1}\}\), \(1\le r<m\), have \(b_{B_r}(k)=\alpha_{r+1}-\alpha_r>0\), so they belong to \(\mathcal B\); they are the only \(B\) with \(b_B(k)\neq0\), and they are nested. Hence
\[
T(z_i)(k)=\alpha_1+\sum_{r:\,i\in B_r}(\alpha_{r+1}-\alpha_r)=x_i(k),
\]
the sum running over the gaps below \(x_i(k)\). If \(x_i(k)\ge x_j(k)\), every \(B_r\) containing \(j\) contains \(i\), so all nonzero terms of \(\sum_B(z_i(B)-z_j(B))b_B(k)\) have the same sign, and \(|x_i(k)-x_j(k)|=\sum_B|z_i(B)-z_j(B)|\,b_B(k)\). Summing over \(k\), \(\|x_i-x_j\|_1=\sum_B|z_i(B)-z_j(B)|w_B\). Finally \(\|T(u)-T(u')\|_1=\|\sum_B(u_B-u'_B)b_B\|_1\le\sum_B|u_B-u'_B|\,w_B\). \(\square\)

The map \(T\) takes values in the whole space \(\ell_1\), not only in the span of the data; this is used in the next lesson, where new points are built as \(T\) of non-binary vectors.

## 2. A flat cubic

Fix \(\mathcal B\) and \(w\) as in Section 1, let \(Q=[0,1]^{\mathcal B}\), and let
\[
\phi(r)=3r^2-2r^3\quad(0\le r\le1),\qquad\Phi(u)=(\phi(u_B))_{B\in\mathcal B}\quad(u\in Q).
\]
Then \(\phi(0)=0\), \(\phi(1)=1\), \(\phi\) is increasing, \(\Phi(Q)\subseteq Q\), and \(\Phi\) fixes the binary vectors. Also \(\phi(h)=3h^2(1-h)+h^3\) is the probability that at least two of three independent events of probability \(h\) occur.

**Lemma 2.1** (flatness; OpenAI). Let \(u,u'\in Q\) and \(e\in\{0,1\}^{\mathcal B}\), and put \(a=u-e\), \(\delta=u'-u\) and \(F_e(u)=\|u-e\|_H^4\). Then
\[
\|\Phi(u')-\Phi(u)\|_{1,w}^2\le108\Bigl(F_e(u')-F_e(u)-4\|a\|_H^2\langle a,\delta\rangle_H\Bigr).\tag{2.1}
\]

**Proof.** For \(d\in\{0,1\}\) and \(r\in[0,1]\), \(|\phi'(r)|=6r(1-r)\le6|r-d|\). With \(d=e_B\), integrating along the segment from \(u_B\) to \(u'_B\),
\[
|\phi(u'_B)-\phi(u_B)|\le6|\delta_B|\int_0^1|a_B+s\delta_B|\,ds\le6|a_B||\delta_B|+3\delta_B^2.
\]
Summing with the weights and using the Cauchy–Schwarz inequality, \(\|\Phi(u')-\Phi(u)\|_{1,w}\le6\|a\|_H\|\delta\|_H+3\|\delta\|_H^2\). Let \(R\) be the bracket in (2.1). Expanding \(\|a+\delta\|_H^4=(\|a\|_H^2+2\langle a,\delta\rangle_H+\|\delta\|_H^2)^2\),
\[
R=2\|a\|_H^2\|\delta\|_H^2+\bigl(2\langle a,\delta\rangle_H+\|\delta\|_H^2\bigr)^2.\tag{2.2}
\]
So \(\|a\|_H^2\|\delta\|_H^2\le R/2\), and
\[
\|\delta\|_H^4\le2\bigl(2\langle a,\delta\rangle_H+\|\delta\|_H^2\bigr)^2+8\langle a,\delta\rangle_H^2\le2\bigl(2\langle a,\delta\rangle_H+\|\delta\|_H^2\bigr)^2+8\|a\|_H^2\|\delta\|_H^2\le4R.
\]
Therefore \(\|\Phi(u')-\Phi(u)\|_{1,w}^2\le72\|a\|_H^2\|\delta\|_H^2+18\|\delta\|_H^4\le36R+72R=108R\). \(\square\)

The bracket in (2.1) is the potential \(F_e\) minus its linear approximation at \(u\). For the identity map in place of \(\Phi\), no such bound holds near a binary point (Exercise 4.3): the flatness of \(\phi\) at \(0\) and \(1\) is what makes the increments of \(\Phi\) quadratically small there.

## 3. Summing along a harmonic function

Let \((\omega_m)_{m\ge0}\) be a Markov chain on a finite set \(\Sigma\), with transition probabilities \(P(\sigma,\sigma')\) and any initial law. A function \(f:\Sigma\to Q\) is *harmonic* if \(\sum_{\sigma'}P(\sigma,\sigma')f(\sigma')=f(\sigma)\) for every \(\sigma\).

**Lemma 3.1** (telescoping). Let \(f\) be harmonic, \(E\colon\Sigma\to\{0,1\}^{\mathcal B}\) any function, \(M_m=f(\omega_m)\) and \(e=E(\omega_0)\). Then for every \(L\ge1\)
\[
\sum_{m=0}^{L-1}\mathbb E\|\Phi(M_{m+1})-\Phi(M_m)\|_{1,w}^2\le108\bigl(\mathbb E\|M_L-e\|_H^4-\mathbb E\|M_0-e\|_H^4\bigr).
\]

**Proof.** Apply Lemma 2.1 with \(u=M_m\), \(u'=M_{m+1}\) and take expectations. Summing over the paths, \(\mathbb P(\omega_0=\sigma_0,\omega_m=\sigma,\omega_{m+1}=\sigma')=\mathbb P(\omega_0=\sigma_0,\omega_m=\sigma)\,P(\sigma,\sigma')\). So with \(g(\sigma_0,\sigma)=4\|f(\sigma)-E(\sigma_0)\|_H^2\,(f(\sigma)-E(\sigma_0))\),
\[
\mathbb E\bigl[\langle g(\omega_0,\omega_m),M_{m+1}-M_m\rangle_H\bigr]=\sum_{\sigma_0,\sigma}\mathbb P(\omega_0=\sigma_0,\omega_m=\sigma)\Bigl\langle g(\sigma_0,\sigma),\sum_{\sigma'}P(\sigma,\sigma')f(\sigma')-f(\sigma)\Bigr\rangle_H=0.
\]
The remaining terms telescope. \(\square\)

The centre \(e\) may depend on the initial state; in the next lesson it is the binary vector of the starting point of the walk.

## 4. Exercises

**Exercise 4.1** (easy). Work out Lemma 1.1 for two points \(x_1\neq x_2\): which subsets occur, with which weights?

**Exercise 4.2** (easy). Check that \(\phi'(0)=\phi'(1)=0\), that \(\phi\) maps \([0,1]\) onto itself, and that \(\phi(h)\) is the probability that at least two of three independent events of probability \(h\) occur.

**Exercise 4.3** (medium). Show that (2.1) fails for every constant if \(\Phi\) is replaced by the identity: take one coordinate with weight \(1\), \(e=0\), \(u=0\) and \(u'=\varepsilon\).

**Exercise 4.4** (easy). Verify (2.2).

## 5. Solutions

**4.1.** Only \(B=\{1\}\) and \(B=\{2\}\), with \(b_{\{1\}}=(x_1-x_2)_+\) and \(b_{\{2\}}=(x_2-x_1)_+\); one of them may have weight \(0\) and be omitted. Then \(z_1=(1,0)\), \(z_2=(0,1)\) (on the subsets present), and \(\|x_1-x_2\|_1=w_{\{1\}}+w_{\{2\}}\).

**4.2.** \(\phi'(r)=6r(1-r)\geq0\), with \(\phi(0)=0\), \(\phi(1)=1\). Exactly two of three occur with probability \(3h^2(1-h)\), all three with probability \(h^3\), and \(3h^2(1-h)+h^3=3h^2-2h^3\).

**4.3.** With these choices \(a=0\), \(\delta=\varepsilon\), the bracket is \(\varepsilon^4\), while \(\|u'-u\|_{1,w}^2=\varepsilon^2\). The ratio \(\varepsilon^{-2}\) is unbounded. For \(\Phi\), \(\phi(\varepsilon)^2=(3\varepsilon^2-2\varepsilon^3)^2\le9\varepsilon^4\).

**4.4.** \(F_e(u')=\|a+\delta\|_H^4=\|a\|_H^4+2\|a\|_H^2(2\langle a,\delta\rangle_H+\|\delta\|_H^2)+(2\langle a,\delta\rangle_H+\|\delta\|_H^2)^2\); subtract \(F_e(u)=\|a\|_H^4\) and \(4\|a\|_H^2\langle a,\delta\rangle_H\).

## References

- [OpenAI-C] OpenAI, *Metric Markov cotype two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
