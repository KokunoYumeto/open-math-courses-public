# Disjoint windows and the dimension formula

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the dimension formula for self-similar measures on the line, from the results of the earlier lessons of the course:
\[
d=\min\Bigl\{1,\frac h\chi\Bigr\}.
\]
The upper bound is known. Suppose that \(d<1\) and \(d\chi<h\). Then the maps of \(n\) blocks carry pair capacity of the order \(n\) at fine scales, and every pair raises the entropy of the measure in a window of scales by a fixed amount, because the one-bit deficit of a measure of dimension less than one is bounded below. The entropy in a window of scales is bounded. The proof arranges many such gains, for many block lengths, so that at each scale they come from disjoint stretches of blocks and add up to at most the bound, while their number is as large as one likes. This is a contradiction.

- The laws of the tails and the entropy in a window of scales (Lemmas 2.1 and 2.2).
- The gain from the pairs of a stretch of blocks (Proposition 3.1).
- Retained windows are disjoint (Lemma 4.1).
- The dimension formula (Theorem 5.1) and the case without exact overlaps (Corollaries 6.2 and 6.3).

The lesson follows [OpenAI-S, Sections 5 and 6]. It uses the results of all the earlier lessons of the course, above all [Block types and pairs at fine scales](block-types-and-pairs-at-fine-scales.md), [The gain from a pair of points](the-gain-from-a-pair-of-points.md) and [The one-bit deficit of a self-similar measure](the-one-bit-deficit.md).

## 1. The setting

Let \(\mu\) be the self-similar measure of the maps \(\varphi_i(x)=r_ix+t_i\), \(0<|r_i|<1\), with the weights \(p_i>0\). Assume that \(\mu\) is exact dimensional with the dimension \(d\), and, in Sections 1 to 4 and in the proof of Theorem 5.1, that
\[
d<1\qquad\text{and}\qquad d\chi<h .
\]
The second assumption is the assumption (1) of the lesson on block types. We use the notation of that lesson: the block length \(b\), the numbers \(A'<A\), the types \(\omega_0,\omega_1,\dots\) of the blocks \(W_0,W_1,\dots\), the products \(R_j\) and \(\sigma_j=-\log|R_j|\), the laws \(\nu_\kappa\), the numbers \(a_n=\lceil An\rceil-1\), and the numbers \(c>0\), \(n_0\) and \(B_n\ge a_n\) of Theorem 5.1 of that lesson. For integers \(j\ge0\), \(n\ge1\) write
\[
\omega[j,j+n)=(\omega_j,\dots,\omega_{j+n-1}),
\]
and let \(\Gamma_{j,n}\) be the pair capacity of the stretch of blocks \(j,\dots,j+n-1\) in the range from \(a_n\) to \(B_n\), counted only if the stretch does not contract too much:
\[
\begin{aligned}
\Gamma_{j,n}&=\mathbf 1_{\{\sigma_{j+n}-\sigma_j\le A'n\}}\\
&\quad\times\sum_{\ell=a_n}^{B_n}c_\ell\bigl(\nu_{\omega[j,j+n)}\bigr).
\end{aligned}
\]
The tuple \(\omega[j,j+n)\) has the same law as \(\Omega_n=\omega[0,n)\), so Theorem 5.1 of that lesson says, for \(n\ge n_0\),
\[
\mathbb E\,\Gamma_{j,n}\ge c\,n. \tag{2}
\]
Three more constants are needed. Let
\[
D=\max_\kappa\bigl(-\log|r(\kappa)|\bigr),
\]
the maximum over the types; so \(0<\sigma_{j+1}-\sigma_j\le D\) and \(\sigma_j\le Dj\). By Theorem 3.5 of the lesson on the one-bit deficit, which uses \(d<1\),
\[
\delta=\inf_{v>0}\Delta_v(\mu)>0 .
\]
Fix an integer \(M>4\) with \(5/M<\delta/2\).

## 2. Tails and the entropy in a window

Fix an integer \(N\ge1\), the number of blocks that are considered. For a tuple \(\kappa\) of \(n\) types let \(\lambda_\kappa=\nu_\kappa*\mathsf D_{R_n(\kappa)}\mu\), and for the empty tuple let \(\lambda_\kappa=\mu\). For \(0\le j\le N\) the *tail law* is
\[
\tau_j=\mathsf D_{R_j}\,\lambda_{\omega[j,N)} .
\]
It is a bounded law that depends on the types \(\Omega_N\). In words: \(\tau_j\) is the law of the part of the random point of \(\mu\) that comes from the blocks \(j,\dots,N-1\) and from everything after them, when the types of the blocks \(0,\dots,N-1\) are known.

**Lemma 2.1.** Let \(0\le j\) and \(j+n\le N\) with \(n\ge1\).

1. \(\tau_j=\bigl(\mathsf D_{R_j}\nu_{\omega[j,j+n)}\bigr)*\tau_{j+n}\).
2. The mean of \(\tau_j\) over the types \(\omega_j,\dots,\omega_{N-1}\), with \(\Omega_j\) fixed, is \(\mathsf D_{R_j}\mu\).

**Proof.** (1) Let \(\kappa=\omega[j,N)\), and number its types \(\kappa_j,\dots,\kappa_{N-1}\). Let \(W_h\) be independent, uniform on the blocks of the type \(\kappa_h\), and \(X'\) independent of them with the law \(\mu\). With \(P_h=\prod_{j\le i<h}r(\kappa_i)=R_h/R_j\), the law \(\lambda_\kappa\) is the law of
\[
\begin{aligned}
&\sum_{h=j}^{j+n-1}P_h\,\varphi_{W_h}(0)+P_{j+n}\,Z,\\
&Z=\sum_{h=j+n}^{N-1}\frac{P_h}{P_{j+n}}\,\varphi_{W_h}(0)+\frac{P_N}{P_{j+n}}X'.
\end{aligned}
\]
The first sum has the law \(\nu_{\omega[j,j+n)}\). The variable \(Z\) has the law \(\lambda_{\omega[j+n,N)}\) and is independent of the first sum. Multiply by \(R_j\) and note \(R_jP_{j+n}=R_{j+n}\).

(2) By Lemma 3.1 of the lesson on block types, the mean of \(\lambda_\kappa\) over the tuples \(\kappa\) of \(N-j\) types, with the weights \(q_\kappa\), is \(\mu\). The types \(\omega_j,\dots,\omega_{N-1}\) are independent of \(\Omega_j\), and \(R_j\) is determined by \(\Omega_j\). \(\blacksquare\)

For an integer \(L\ge1\) let \(\varrho=2^{-L}\), and let
\[
g_j=G_{\varrho/M,\,M\varrho}(\tau_j)\qquad(0\le j\le N).
\]
This is the entropy of the tail between the scales \(M\varrho\) and \(\varrho/M\), a window around the scale \(\varrho\). It depends on \(L\) and on the types.

**Lemma 2.2.** \(0\le g_j\le2\log M\), and \(g_j\ge g_{j+1}\) for \(j<N\).

**Proof.** The ratio of the two scales is the integer \(M^2\), so the first statement is Proposition 2.1 of the lesson on entropy at a scale. By Lemma 2.1 (1) with \(n=1\), \(\tau_j\) is the law of a sum of two independent bounded variables, one of them with the law \(\tau_{j+1}\); so the second statement is Proposition 2.4 (2) of that lesson. \(\blacksquare\)

## 3. The gain from the pairs of a stretch of blocks

**Proposition 3.1.** Let \(j\ge0\), \(n\ge1\) with \(j+n\le N\), and \(L\ge1\). Then the mean of \(g_j-g_{j+n}\) over the types \(\omega_{j+n},\dots,\omega_{N-1}\), with \(\Omega_{j+n}\) fixed, satisfies
\[
\begin{aligned}
&\mathbb E\bigl[g_j-g_{j+n}\bigm|\Omega_{j+n}\bigr]\\
&\quad\ge\frac\delta2\;c_{L-\lceil\sigma_j\rceil}\bigl(\nu_{\omega[j,j+n)}\bigr).
\end{aligned}
\]

**Proof.** Fix \(\Omega_{j+n}\). Then \(\nu=\nu_{\omega[j,j+n)}\), \(R_j\), \(R_{j+n}\) and \(\ell=L-\lceil\sigma_j\rceil\) are fixed. Choose a feasible family of weights \(w_e\) on the pairs \(e=\{x,y\}\) of points of the support of \(\nu\) with \(2^{-\ell}\le|x-y|<2^{1-\ell}\), with \(\sum_ew_e=c_\ell(\nu)\).

The law \(\mathsf D_{R_j}\nu\) gives the point \(R_jx\) the mass \(\nu(\{x\})\). So the same weights, on the pairs \(\{R_jx,R_jy\}\), satisfy the condition of Theorem 2.3 of the lesson on the gain from a pair of points for the law \(\mathsf D_{R_j}\nu\). The size of such a pair is \(v_e=|R_j|\,|x-y|\), and
\[
\begin{aligned}
\frac{v_e}\varrho&=2^{L-\sigma_j}\,|x-y|\\
&\in\bigl[2^{\lceil\sigma_j\rceil-\sigma_j},\,2^{1+\lceil\sigma_j\rceil-\sigma_j}\bigr),
\end{aligned}
\]
an interval that lies in \([1,4)\).
Let \(s=\varrho/M\) and \(t=M\varrho\). Since \(M>4\), \(s<v_e<t\), and
\[
\frac s{v_e}+\frac{v_e}t\le\frac1M+\frac4M=\frac5M .
\]
By Lemma 2.1 (1), \(\tau_j=(\mathsf D_{R_j}\nu)*\tau_{j+n}\). Theorem 2.3 of that lesson, with \(t=M^2s\), gives
\[
g_j-g_{j+n}\ \ge\ \sum_ew_e\Bigl(\Delta_{v_e}(\tau_{j+n})-\frac5M\Bigr).
\]
Now take the mean over the types \(\omega_{j+n},\dots,\omega_{N-1}\). The \(w_e\) and \(v_e\) do not depend on them. By Lemma 2.1 (2) the mean of the laws \(\tau_{j+n}\) is \(\mathsf D_{R_{j+n}}\mu\). By Proposition 2.4 (3) of the lesson on entropy at a scale, the mean of the deficits is at least the deficit of the mean, and by Lemma 1.1 of that lesson a change of scale of the law is a change of the scale of the grid:
\[
\begin{aligned}
&\mathbb E\bigl[\Delta_{v_e}(\tau_{j+n})\bigm|\Omega_{j+n}\bigr]\\
&\quad\ge\Delta_{v_e}\bigl(\mathsf D_{R_{j+n}}\mu\bigr)\\
&\quad=\Delta_{v_e/|R_{j+n}|}(\mu)\ \ge\ \delta .
\end{aligned}
\]
So the mean of \(g_j-g_{j+n}\) is at least \(\sum_ew_e(\delta-\tfrac5M)\ge\tfrac\delta2\,c_\ell(\nu)\). \(\blacksquare\)

A single tail law \(\tau_{j+n}\), for given types, need not have a deficit bounded below. The proof uses the bound for \(\mu\) itself, and for this it averages over the types after the stretch: their mean is a copy of \(\mu\).

## 4. Disjoint windows

Let \(Q\ge1\) be an integer. Choose integers \(n_0\le n_1<n_2<\dots<n_Q\) one after the other such that \(a_{n_i}\ge1\) and, for all \(h<i\),
\[
a_{n_i}-A'n_i-1>B_{n_h}. \tag{3}
\]
This is possible, because the earlier numbers \(B_{n_h}\) are known when \(n_i\) is chosen, and \(a_n-A'n-1\ge(A-A')\,n-2\), which tends to infinity with \(n\).
No bound for the size of \(B_n\) is needed. The integers \(\ell\) with \(a_{n_i}\le\ell\le B_{n_i}\) form the *band* \(i\). By (3) the bands are disjoint, and a band with a larger \(i\) consists of larger \(\ell\), that is, of finer scales.

Choose an even integer \(T\) with \(T/2>B_{n_i}\) for all \(i\). For each band let \(J_i\) be the set of the numbers \(k\,n_i\), where \(k\) is an integer with \(0\le k\le T/(2Dn_i)\), and let \(N\) be at least \(j+n_i\) for all \(i\) and all \(j\in J_i\). For \(L\in\{1,\dots,T\}\), \(1\le i\le Q\) and \(j\in J_i\), the *window* \([j,j+n_i)\) of block indices is *retained* for \(L\) if
\[
\begin{gathered}
\sigma_{j+n_i}-\sigma_j\le A'n_i\quad\text{and}\\
a_{n_i}\le L-\lceil\sigma_j\rceil\le B_{n_i}.
\end{gathered}
\]
This is an event \(\mathcal A_{i,j,L}\) that is determined by \(\Omega_{j+n_i}\).

**Lemma 4.1.** For all types and every \(L\in\{1,\dots,T\}\), the windows retained for \(L\) are pairwise disjoint, and
\[
\sum_{i=1}^Q\sum_{j\in J_i}\mathbf 1_{\mathcal A_{i,j,L}}\,\bigl(g_j-g_{j+n_i}\bigr)\le2\log M .
\]

**Proof.** Let \(x_j=L-\lceil\sigma_j\rceil\). Since \(\sigma_j\) increases with \(j\), \(x_j\) does not increase. Let the window \([j,j+n_i)\) of the band \(i\) be retained. Then
\[
\begin{aligned}
\lceil\sigma_{j+n_i}\rceil-\lceil\sigma_j\rceil&\le\sigma_{j+n_i}-\sigma_j+1\\
&\le A'n_i+1,
\end{aligned}
\]
so \(x_{j+n_i}\ge a_{n_i}-A'n_i-1\). Let \([k,k+n_h)\) be a retained window of a band \(h<i\). Then \(x_k\le B_{n_h}\), and by (3)
\[
x_{j+n_i}>B_{n_h}\ge x_k .
\]
Because \(x\) does not increase, \(k>j+n_i\): the window of the finer band ends before the window of the coarser band begins. Two different windows of the same band begin at different multiples of their length \(n_i\), so they are disjoint as well.

If no window is retained, the sum in the statement is \(0\). Otherwise list the retained windows in their order as \([u_1,v_1),\dots,[u_P,v_P)\) with \(v_z\le u_{z+1}\). By Lemma 2.2, \(g_{v_z}\ge g_{u_{z+1}}\), so
\[
\sum_{z=1}^P\bigl(g_{u_z}-g_{v_z}\bigr)\le g_{u_1}-g_{v_P}\le2\log M .
\]
\(\blacksquare\)

So at one scale \(\varrho=2^{-L}\) the retained windows share one bounded amount of entropy. The condition \(a_{n_i}\le L-\lceil\sigma_j\rceil\le B_{n_i}\) says that the pairs of the band \(i\) in the stretch of blocks beginning at \(j\), contracted by \(R_j\), have sizes near \(\varrho\); these are the pairs that Proposition 3.1 uses.

## 5. The dimension formula

**Theorem 5.1.** Let \(\mu\) be a self-similar measure on the line, for maps \(\varphi_i(x)=r_ix+t_i\) with \(0<|r_i|<1\) and weights \(p_i>0\), that is exact dimensional with the dimension \(d\). Then
\[
d=\min\Bigl\{1,\frac h\chi\Bigr\},
\]
where \(h\) is the entropy rate of the walk of maps and \(\chi=-\sum_ip_i\log|r_i|\). Under the hypothesis (ED) of the lesson on the one-bit deficit this holds for every self-similar measure on the line.

**Proof.** By Theorem 3.3 of the lesson on the random walk of maps, \(d\le\min\{1,h/\chi\}\). If the inequality is strict, then \(d<1\) and \(d\chi<h\), the assumptions of Section 1. We show that then every integer \(Q\ge1\) satisfies
\[
Q\le\frac{8D\log M}{\delta\,c}. \tag{4}
\]
The right side was fixed before \(Q\), so this is impossible, and the theorem follows.

Let \(Q\) be given, and choose the \(n_i\), \(T\), \(J_i\) and \(N\) as in Section 4. Take the mean over the types in Lemma 4.1 and sum over \(L=1,\dots,T\):
\[
\begin{aligned}
&2T\log M\\
&\quad\ge\sum_{i,j,L}\mathbb E\bigl[\mathbf 1_{\mathcal A_{i,j,L}}\,(g_j-g_{j+n_i})\bigr],
\end{aligned}
\]
where the sum is over \(1\le i\le Q\), \(j\in J_i\) and \(1\le L\le T\).
The event \(\mathcal A_{i,j,L}\) is determined by \(\Omega_{j+n_i}\). So in each term one may first take the mean over the later types, and Proposition 3.1 gives
\[
\begin{aligned}
&\mathbb E\bigl[\mathbf 1_{\mathcal A_{i,j,L}}\,(g_j-g_{j+n_i})\bigr]\\
&\quad\ge\frac\delta2\,\mathbb E\Bigl[\mathbf 1_{\mathcal A_{i,j,L}}\;c_{L-\lceil\sigma_j\rceil}\bigl(\nu_{\omega[j,j+n_i)}\bigr)\Bigr].
\end{aligned}
\]
Fix \(i\) and \(j\in J_i\). Since \(\sigma_j\le Dj\le T/2\) and \(T/2\) is an integer, \(0\le\lceil\sigma_j\rceil\le T/2\). For every \(\ell\) with \(a_{n_i}\le\ell\le B_{n_i}\) the number \(L=\ell+\lceil\sigma_j\rceil\) satisfies \(1\le L<T\), because \(a_{n_i}\ge1\) and \(B_{n_i}<T/2\). So as \(L\) runs through \(1,\dots,T\), the number \(L-\lceil\sigma_j\rceil\) takes every value of the band \(i\) exactly once, and
\[
\sum_{L=1}^T\mathbf 1_{\mathcal A_{i,j,L}}\;c_{L-\lceil\sigma_j\rceil}\bigl(\nu_{\omega[j,j+n_i)}\bigr)=\Gamma_{j,n_i}.
\]
By (2) the mean of the right side is at least \(c\,n_i\). The set \(J_i\) has at least \(T/(2Dn_i)\) elements. Together,
\[
\begin{aligned}
2T\log M&\ge\frac\delta2\sum_{i=1}^Q|J_i|\,c\,n_i\\
&\ge\frac\delta2\cdot Q\cdot\frac T{2D}\cdot c ,
\end{aligned}
\]
which is (4). \(\blacksquare\)

Every band contributes the same amount \(\delta cT/(4D)\), whatever its block length \(n_i\) is: a longer block has fewer starting points in \(J_i\) and more pair capacity for each. The bound \(2T\log M\) does not grow with the number of bands, because of Lemma 4.1.

## 6. Without exact overlaps

**Lemma 6.1.** If \(\varphi_u=\varphi_v\) for two different nonempty words \(u,v\), of any lengths, then there are two different words of the same length that give the same map.

**Proof.** The word \(u\) is not a beginning of \(v\): if \(v=uw\) with a nonempty word \(w\), then \(\varphi_u\circ\varphi_w=\varphi_u\), and since \(\varphi_u\) is one-to-one, \(\varphi_w\) is the identity; but its slope has an absolute value less than \(1\). In the same way \(v\) is not a beginning of \(u\). Now \(\varphi_{uv}=\varphi_u\circ\varphi_v\) and \(\varphi_{vu}=\varphi_v\circ\varphi_u\) are the same map, the square of \(\varphi_u=\varphi_v\). The words \(uv\) and \(vu\) have the same length. If they were equal, then the shorter of \(u,v\) would be a beginning of the other, or \(u=v\). \(\blacksquare\)

So the absence of exact overlaps, defined for words of the same length, means that different words never give the same map.

**Corollary 6.2.** Let \(\mu\) be as in Theorem 5.1, and let the maps have no exact overlaps. Then
\[
d=\min\Bigl\{1,\frac{H(p)}\chi\Bigr\}.
\]

**Proof.** By Proposition 1.2 of the lesson on the random walk of maps, \(h=H(p)\). \(\blacksquare\)

**Corollary 6.3.** Let \(0<\lambda<1\), and let \(\mu\) be the self-similar measure of maps \(x\mapsto\lambda x+t_i\), \(i\in\Lambda\), with weights \(p_i>0\). If \(\mu\) is exact dimensional with the dimension \(d\) and the maps have no exact overlaps, then
\[
d=\min\Bigl\{1,\frac{H(p)}{\log(1/\lambda)}\Bigr\}.
\]
This holds in particular for three maps \(\lambda x\), \(\lambda x+1\), \(\lambda x+t\) without exact overlaps and all weights \(p_0,p_1,p_2>0\).

**Proof.** Here \(\chi=\log(1/\lambda)\). \(\blacksquare\)

**Example 6.4.** For the maps \(\lambda x\) and \(\lambda x+1\), the word \(i_1\cdots i_n\) gives the map \(\lambda^nx+\sum_k\lambda^{k-1}i_k\). So there is an exact overlap exactly if \(\lambda\) is a root of a polynomial, not identically zero, with coefficients in \(\{-1,0,1\}\). For every other \(\lambda\in[\tfrac12,1)\) and the weights \(\tfrac12\), Corollary 6.3 gives \(d=1\) under the hypothesis (ED). For the maps \(\tfrac x3\), \(\tfrac x3+1\), \(\tfrac x3+3\) with equal weights, which have an exact overlap, Theorem 5.1 gives \(d=h/\log3\) under the same hypothesis, and \(h<1.3607\) by Example 3.5 of the lesson on the random walk of maps.

[OpenAI-S, Section 6] also deduces that the attractor of maps without exact overlaps has the Hausdorff dimension \(\min\{1,s_*\}\), where \(\sum_i|r_i|^{s_*}=1\). This statement about sets needs the Hausdorff dimension and is not part of the course.

## 7. Exercises

**7.1.** In the proof of Proposition 3.1 the ratio \(R_j\) may be negative. Check that the family of pairs \(\{R_jx,R_jy\}\) with the weights \(w_e\) is feasible for \(\mathsf D_{R_j}\nu\), and say where the proof of Proposition 3.1 uses the absolute value \(|R_j|\) and where the sign is kept.

**7.2.** Let \(Q=2\), \(A=2\), \(A'=1\), so that \(a_n=2n-1\), and let \(B_{n_1}=a_{n_1}+5\) for \(n_1=2\). Find the smallest \(n_2\) allowed by (3).

**7.3.** Show that \(H(G_n)\le n\log m\) and \(\chi\ge\log(1/r_{\max})\), and deduce from Theorem 5.1 that \(d<1\) whenever \(m\,r_{\max}<1\).

**7.4.** Let \(\lambda=\tfrac{\sqrt5-1}2\), so that \(\lambda^2+\lambda=1\). Find two different words of the same length that give the same map for \(\lambda x\) and \(\lambda x+1\).

## 8. Solutions

**7.1.** The law \(\mathsf D_{R_j}\nu\) has the mass \(\nu(\{x\})\) at \(R_jx\), and \(x\mapsto R_jx\) is one-to-one. So \(\tfrac12\sum_{e\ni x}w_e\le\nu(\{x\})\) is the same condition for the pairs \(\{R_jx,R_jy\}\) at the point \(R_jx\). The absolute value is used for the sizes \(v_e=|R_j||x-y|\) and for the change of scale \(\Delta_{v}(\mathsf D_u\mu)=\Delta_{v/|u|}(\mu)\). The sign is kept in the laws \(\mathsf D_{R_j}\nu\) and \(\tau_j\); Theorem 2.3 of the lesson on the gain from a pair of points holds for every law with a feasible family of pairs.

**7.2.** \(a_2=3\) and \(B_2=8\). Condition (3) is \(2n_2-1-n_2-1>8\), that is, \(n_2>10\). The smallest value is \(n_2=11\), with \(a_{11}=21\).

**7.3.** \(G_n\) is a function of a word of length \(n\), which takes \(m^n\) values, so \(H(G_n)\le n\log m\) and \(h\le\log m\). Every \(-\log|r_i|\) is at least \(\log(1/r_{\max})\), so \(\chi\ge\log(1/r_{\max})\). Then \(h/\chi\le\log m/\log(1/r_{\max})\), which is less than \(1\) exactly if \(m<1/r_{\max}\). For this conclusion the upper bound, Theorem 3.3 of the lesson on the random walk of maps, is enough.

**7.4.** The word \(i_1i_2i_3\) gives the translation \(i_1+\lambda i_2+\lambda^2i_3\). The words \(100\) and \(011\) give \(1\) and \(\lambda+\lambda^2=1\), with the same slope \(\lambda^3\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
