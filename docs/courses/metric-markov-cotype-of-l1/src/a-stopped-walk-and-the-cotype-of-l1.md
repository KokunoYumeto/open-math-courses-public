# A stopped walk and the cotype of ℓ₁

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves OpenAI's theorem [OpenAI-C, Sections 4 and 5]:

**Theorem 3.1** (OpenAI). The real space \(\ell_1\) has metric Markov cotype two with \(N_2(\ell_1)\le12\sqrt{21}\). More precisely, inequality (2.1) of [Markov chains and metric Markov cotype](markov-chains-and-metric-markov-cotype.md) holds in \(\ell_1\) with \(C^2=3024\) for every stochastic matrix \(A\) and every stationary probability vector \(\pi\), reversible or not.

Given data \(x_1,\dots,x_n\in\ell_1\), write them through cuts as binary vectors \(z_i\) (Lemma 1.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md)). Average the \(z_j\) over the endpoint \(j\) of the walk from \(i\) stopped after a geometric number of steps with mean \(t\); this gives vectors \(h_i\) in the cube \(Q\). The new points are \(y_i=T(\Phi(h_i))\), where \(\Phi\) is the flat cubic and \(T\) maps back into \(\ell_1\). A walk that is killed with probability \(\frac1{t+1}\) at each step carries the values \(h_i\) while alive and \(z_i\) once dead; these values form a martingale. Its squared jumps, measured after applying \(\Phi\), add up exactly to the left-hand side of the cotype inequality for the \(y_i\) (Lemma 2.1), and Lemma 3.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md) bounds them by the displacement of the data at the killing time, which Lemma 3.1 of [Markov chains and metric Markov cotype](markov-chains-and-metric-markov-cotype.md) compares with the right-hand side.

We use Section 1, Definition 2.1 and Lemma 3.1 of [Markov chains and metric Markov cotype](markov-chains-and-metric-markov-cotype.md), and Lemmas 1.1, 2.1 and 3.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md).

## 1. The new points

Fix \(n,t\ge1\), a stochastic matrix \(A\) on \([n]\) with a stationary probability vector \(\pi\), and \(x_1,\dots,x_n\in\ell_1\). If all \(x_i\) are equal, put \(y_i=x_i\); both sides of the cotype inequality vanish. Otherwise take \(\mathcal B\), \(w\), \(z_i\) and \(T\) from Lemma 1.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md), let \(p=\frac1{t+1}\), \(q=1-p\), and
\[
h_i=p\sum_{s=0}^\infty q^s\sum_j(A^s)_{ij}\,z_j\in Q,\qquad y_i=T(\Phi(h_i))\in\ell_1.\tag{1.1}
\]
The weights \(pq^s(A^s)_{ij}\) are nonnegative with total \(1\), so \(h_i\) is a convex combination of binary vectors and lies in \(Q=[0,1]^{\mathcal B}\). Separating the term \(s=0\),
\[
h_i=p\,z_i+q\sum_ja_{ij}h_j.\tag{1.2}
\]
Equivalently \(h_i=\sum_jG_{ij}z_j\) with \(G=p\sum_sq^sA^s=p(I-qA)^{-1}\): \(G_{ij}\) is the probability that the walk from \(i\), stopped after a geometric number of steps of mean \(t\), ends at \(j\).

## 2. A killed walk

Let \(\Sigma=\{\mathsf a,\mathsf d\}\times[n]\) (alive or dead, with an index). From \((\mathsf a,i)\) the chain moves to \((\mathsf d,i)\) with probability \(p\) and to \((\mathsf a,j)\) with probability \(qa_{ij}\); the dead states are absorbing. Start at \((\mathsf a,i)\) with probability \(\pi_i\), and let \(f(\mathsf a,i)=h_i\), \(f(\mathsf d,i)=z_i\). By (1.2), \(f\) is harmonic. Let \(\omega_m\) be the state at time \(m\), \(M_m=f(\omega_m)\), and \(e=z_i\) when \(\omega_0=(\mathsf a,i)\).

By induction on \(m\), using \(\pi A=\pi\), \(\mathbb P(\omega_m=(\mathsf a,i))=q^m\pi_i\). Since \(\Phi(z_i)=z_i\) and dead states do not move,
\[
\mathbb E\|\Phi(M_{m+1})-\Phi(M_m)\|_{1,w}^2=q^m\sum_i\pi_i\Bigl(p\,\|z_i-\Phi(h_i)\|_{1,w}^2+q\sum_ja_{ij}\|\Phi(h_j)-\Phi(h_i)\|_{1,w}^2\Bigr).
\]

**Lemma 2.1** (the jump identity). With
\[
B=\sum_i\pi_i\|z_i-\Phi(h_i)\|_{1,w}^2,\qquad E_A=\sum_{i,j}\pi_ia_{ij}\|\Phi(h_i)-\Phi(h_j)\|_{1,w}^2,
\]
one has \(\sum_{m=0}^\infty\mathbb E\|\Phi(M_{m+1})-\Phi(M_m)\|_{1,w}^2=B+tE_A\).

**Proof.** Sum the display over \(m\): \(\sum_mq^m(pB+qE_A)=B+\frac qpE_A\), and \(\frac qp=t\). \(\square\)

This is why the killing probability is \(\frac1{t+1}\): the expected number of steps taken alive before death is \(t\).

**Lemma 2.2** (the terminal cost). With \(D(s)=\sum_{i,j}\pi_i(A^s)_{ij}\|x_i-x_j\|_1^2\),
\[
B+tE_A\le108\sum_{s=0}^\infty pq^s\,D(s).
\]

**Proof.** By Lemma 3.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md), for every \(L\),
\[
\sum_{m=0}^{L-1}\mathbb E\|\Phi(M_{m+1})-\Phi(M_m)\|_{1,w}^2\le108\,\mathbb E\|M_L-e\|_H^4.
\]
At time \(L\), the chain is dead at index \(j\) after starting at \(i\) with probability \(\sum_{s<L}pq^s\pi_i(A^s)_{ij}\), and then \(\|M_L-e\|_H^4=\|z_j-z_i\|_H^4=\|x_j-x_i\|_1^2\) by (1.1) of that lesson. It is alive with probability \(q^L\), and \(\|M_L-e\|_H^4\le(\sum_Bw_B)^2\) always. Hence \(\mathbb E\|M_L-e\|_H^4\le\sum_{s<L}pq^sD(s)+q^L(\sum_Bw_B)^2\). Let \(L\to\infty\) and use Lemma 2.1. \(\square\)

## 3. The theorem

**Proof of Theorem 3.1.** Lemma 1.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md) gives \(T(z_i)=x_i\) and \(\|T(u)-T(u')\|_1\le\|u-u'\|_{1,w}\), so
\[
\|x_i-y_i\|_1\le\|z_i-\Phi(h_i)\|_{1,w},\qquad\|y_i-y_j\|_1\le\|\Phi(h_i)-\Phi(h_j)\|_{1,w}.
\]
Therefore, by Lemma 2.2 and Lemma 3.1 of [Markov chains and metric Markov cotype](markov-chains-and-metric-markov-cotype.md) (applied to the stationary chain with transitions \(A\) and initial law \(\pi\)),
\[
\sum_i\pi_i\|x_i-y_i\|_1^2+t\sum_{i,j}\pi_ia_{ij}\|y_i-y_j\|_1^2\le B+tE_A\le108\cdot28\,W,
\]
where \(W=\frac1t\sum_{s=1}^tD(s)=\sum_{i,j}\pi_i\bigl(\frac1t\sum_{s=1}^tA^s\bigr)_{ij}\|x_i-x_j\|_1^2\). This is the cotype inequality with \(C^2=3024=(12\sqrt{21})^2\). \(\square\)

Reversibility was not used, only \(\pi A=\pi\).

## 4. Expected medians

For real sequences \(x,x',x''\), let \(\operatorname{med}(x,x',x'')\) be the coordinatewise median; it lies in \(\ell_1\) if they do, being at most \(|x|+|x'|+|x''|\) in absolute value.

**Proposition 4.1** (OpenAI). For each \(i\), let \(J_1,J_2,J_3\) be independent random indices with \(\mathbb P(J_a=j)=G_{ij}\). Then
\[
y_i=\mathbb E\,\operatorname{med}(x_{J_1},x_{J_2},x_{J_3}).
\]
In particular the points \(y_i\) do not depend on the cut representation.

**Proof.** Fix a coordinate \(k\). As in the proof of Lemma 1.1 of [Cuts and a flat cubic](cuts-and-a-flat-cubic.md), \(x_j(k)=v(k)+\sum_Bz_j(B)b_B(k)\), where the \(B\) with \(b_B(k)>0\) are the nested sets \(\{j:x_j(k)\ge\alpha\}\) for the thresholds \(\alpha\) between consecutive values. The median of three numbers is at least \(\alpha\) exactly when at least two of them are; hence
\[
\operatorname{med}(x_{J_1},x_{J_2},x_{J_3})(k)=v(k)+\sum_Bb_B(k)\,\mathbf 1\bigl[\#\{a:J_a\in B\}\ge2\bigr].
\]
Each \(J_a\) lies in \(B\) with probability \(\sum_jG_{ij}z_j(B)=h_i(B)\), independently, so the indicator has expectation \(\phi(h_i(B))\) (Section 2 of that lesson). The expectation is a finite average, and \(v+\sum_Bb_B\,\phi(h_i(B))=T(\Phi(h_i))=y_i\). \(\square\)

So the new point at \(i\) is obtained by running three independent walks from \(i\), stopping each at an independent geometric time of mean \(t\), and taking the expected coordinatewise median of the three endpoints' data. A linear average of the endpoints would not do: Ball's linear form of Markov cotype fails for \(\ell_1\) [MN, Section 1].

## 5. Complex scalars and Lipschitz extension

**Corollary 5.1.** The complex space \(\ell_1(\mathbb C)\) has metric Markov cotype two with \(N_2(\ell_1(\mathbb C))\le12\sqrt{42}\).

**Proof.** The real-linear bijection \(J:\ell_1(\mathbb C)\to\ell_1\), \(Jx=(\operatorname{Re}x(1),\operatorname{Im}x(1),\operatorname{Re}x(2),\dots)\), satisfies \(\|x\|_1\le\|Jx\|_1\le\sqrt2\,\|x\|_1\), because \(|z|\le|\operatorname{Re}z|+|\operatorname{Im}z|\le\sqrt2|z|\). Apply Theorem 3.1 to the points \(Jx_i\) and pull the new points back by \(J^{-1}\): the left side of the cotype inequality can only decrease, and the right side grows by at most the factor \(2\). \(\square\)

**Remark.** Mendel and Naor proved, extending Ball's theorem, that Lipschitz maps from a space of Markov type two into a dual Banach space of metric Markov cotype two extend with a bounded loss [MN, Corollary 1.13]. Since Hilbert spaces have Markov type two and \(\ell_1\) is the dual of \(c_0\), Theorem 3.1 gives a universal \(K\) such that every Lipschitz map from a subset of a Hilbert space into \(\ell_1\) extends to the whole space with Lipschitz constant at most \(K\) times the original, which answers Ball's extension question for this target [OpenAI-C, Section 5]. The extension theorem itself is not proved in this course.

## 6. Exercises

**Exercise 6.1** (easy). Derive (1.2) from (1.1), and show that \(G=p(I-qA)^{-1}\) is a stochastic matrix with \(\pi G=\pi\).

**Exercise 6.2** (medium). Take the real line \(\ell_1^1=\mathbb R\), \(n=2\), \(\pi=(\frac12,\frac12)\), \(A=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), \(x_1=0\), \(x_2=1\). Compute \(G\), \(h_i\) and \(y_i\), and check the cotype inequality directly.

**Exercise 6.3** (easy). Check the formula \(\mathbb P(\omega_m=(\mathsf a,i))=q^m\pi_i\) by induction.

**Exercise 6.4** (medium). Show that for data on the real line, \(y_i\) is the expected median of three independent stopped-walk endpoints, and compute it when \(G_{i\cdot}\) puts mass \(g\) on a point with value \(0\) and \(1-g\) on a point with value \(1\).

## 7. Solutions

**6.1.** The term \(s=0\) of (1.1) is \(pz_i\); the remaining terms are \(q\sum_ja_{ij}\bigl(p\sum_{s\ge0}q^s(A^sz)_j\bigr)\). For \(G\): its entries are nonnegative, \(G\mathbf 1=p\sum_sq^s\mathbf 1=\mathbf 1\), and \(\pi G=p\sum_sq^s\pi A^s=\pi\).

**6.2.** Since \(A^2=I\), \(G=\frac p{1-q^2}I+\frac{pq}{1-q^2}A\), so \(G_{11}=G_{22}=\frac{t+1}{2t+1}\) and \(G_{12}=G_{21}=\frac t{2t+1}\). There is one cut, \(B=\{2\}\), with weight \(1\); \(z_1=0\), \(z_2=1\) and \(T(u)=u\). Hence \(h_1=\frac12-\epsilon\) and \(h_2=\frac12+\epsilon\) with \(\epsilon=\frac1{2(2t+1)}\), and since \(\phi(\frac12+r)=\frac12+\frac32r-2r^3\), \(y_1=1-y_2=\frac12-\frac32\epsilon+2\epsilon^3\). The left side of the cotype inequality is \(y_1^2+t(y_2-y_1)^2\le\frac14+9t\epsilon^2\le\frac14+\frac9{16t}\), while \(W\ge\frac12\), so the right side is at least \(1512\).

**6.3.** For \(m=0\) it is the initial law. Alive states at time \(m+1\) come only from alive states at time \(m\), so \(\mathbb P(\omega_{m+1}=(\mathsf a,j))=\sum_iq^m\pi_i\,qa_{ij}=q^{m+1}(\pi A)_j=q^{m+1}\pi_j\).

**6.4.** On the real line the coordinatewise median is the median, and Proposition 4.1 applies. If the endpoint data equal \(0\) with probability \(g\) and \(1\) with probability \(1-g\), the median of three is \(1\) exactly when at least two equal \(1\), so the expected median is \(\phi(1-g)=3(1-g)^2-2(1-g)^3\).

## References

- [MN] M. Mendel and A. Naor, *Spectral calculus and Lipschitz extension for barycentric metric spaces*, Anal. Geom. Metr. Spaces 1 (2013); arXiv:1301.3963. https://arxiv.org/abs/1301.3963
- [OpenAI-C] OpenAI, *Metric Markov cotype two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
