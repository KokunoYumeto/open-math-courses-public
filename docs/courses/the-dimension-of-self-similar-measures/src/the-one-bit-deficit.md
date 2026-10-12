# The one-bit deficit of a self-similar measure

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Halving the scale can add at most one bit to the entropy of a law on the line. The *one-bit deficit* \(\Delta_v=1-(\mathcal H_v-\mathcal H_{2v})\) measures how far the law is from gaining the full bit between the scales \(2v\) and \(v\). For the uniform law on an interval the deficit tends to \(0\) at small scales. This lesson proves that for a self-similar measure of dimension less than one the opposite holds: the deficit is bounded below by a positive constant at all scales at once. The proof of [OpenAI-S] uses this constant to turn every pair of nearby points in the support into a definite gain of entropy.

- Self-similar measures: existence, uniqueness, and the decomposition along stopped words (Proposition 1.2, Lemma 1.3).
- Exact dimensionality, a named hypothesis (ED), and its consequence for the entropy at small scales (Proposition 2.2).
- A small deficit at one scale forces almost full entropy between the scales \(v\) and \(Kv\) (Proposition 3.3).
- Uniform nonsaturation (Theorem 3.5).

The lesson follows [OpenAI-S, Section 2, the lemmas on entropy and dimension and on uniform nonsaturation]; according to [OpenAI-S], the nonsaturation property was proved for Bernoulli convolutions by E. Breuillard and P. Varjú. The lesson continues [Entropy at a scale](entropy-at-a-scale.md) and uses [Entropy of finite random variables](entropy-of-finite-random-variables.md).

## 1. Self-similar measures

Let \(\Lambda\) be a finite nonempty set, and for \(i\in\Lambda\) let \(\varphi_i(x)=r_ix+t_i\) with real \(t_i\) and \(0<|r_i|<1\). Let \(p=(p_i)_{i\in\Lambda}\) be a law on \(\Lambda\) with all \(p_i>0\). Put
\[
\begin{gathered}
r_{\max}=\max_i|r_i|,\qquad a_*=\min_i|r_i|,\\
T_0=\max_i|t_i|,\qquad R_0=\frac{T_0}{1-r_{\max}}.
\end{gathered}
\]
For a word \(w=i_1\cdots i_n\) let \(\varphi_w=\varphi_{i_1}\circ\dots\circ\varphi_{i_n}\), \(r_w=r_{i_1}\cdots r_{i_n}\) and \(p_w=p_{i_1}\cdots p_{i_n}\); so \(\varphi_w(x)=r_wx+\varphi_w(0)\).

**Lemma 1.1.** For every sequence \(i=(i_1,i_2,\dots)\) of elements of \(\Lambda\) the limit \(\pi(i)=\lim_n\varphi_{i_1\cdots i_n}(0)\) exists, \(|\pi(i)|\le R_0\), and for all real \(x\)
\[
|\varphi_{i_1\cdots i_n}(x)-\pi(i)|\le r_{\max}^n\,(|x|+R_0).
\]

**Proof.** \(\varphi_{i_1\cdots i_n}(0)=\sum_{k=1}^nr_{i_1\cdots i_{k-1}}t_{i_k}\), and the terms are at most \(T_0r_{\max}^{k-1}\) in absolute value. So the series converges, its sum is at most \(R_0\), and the remainder after \(n\) terms is at most \(r_{\max}^nR_0\). Finally \(|\varphi_w(x)-\varphi_w(0)|=|r_w||x|\). \(\blacksquare\)

**Proposition 1.2.** Let \(I_1,I_2,\dots\) be independent with the law \(p\), and \(\mu\) the law of \(\pi(I_1,I_2,\dots)\). Then \(\mu\) is a bounded law, \(\mu([-R_0,R_0])=1\), and it is the only Borel probability measure on \(\mathbb R\) with
\[
\mu=\sum_{i\in\Lambda}p_i\,(\varphi_i)_*\mu,
\]
where \((\varphi_i)_*\mu\) is the law of \(\varphi_i(X)\) for \(X\) with the law \(\mu\).

**Proof.** Since \(\varphi_{i_1}\) is continuous, \(\pi(i_1,i_2,\dots)=\varphi_{i_1}(\pi(i_2,i_3,\dots))\). The sequence \((I_2,I_3,\dots)\) is independent of \(I_1\) and has the same law as \((I_1,I_2,\dots)\). So given \(I_1=i\) the law of \(\pi(I)\) is \((\varphi_i)_*\mu\); this is the equation. Let \(\nu\) be any solution. Applying the equation \(n\) times gives \(\nu=\sum_{|w|=n}p_w(\varphi_w)_*\nu\), so for a bounded continuous function \(f\),
\[
\int f\,d\nu=\mathbb E\int f\bigl(\varphi_{I_1\cdots I_n}(x)\bigr)\,d\nu(x).
\]
By Lemma 1.1 the integrand tends to \(f(\pi(I))\) for every \(x\) and every sequence, and it is bounded. By dominated convergence \(\int f\,d\nu=\mathbb Ef(\pi(I))=\int f\,d\mu\). So \(\nu=\mu\). \(\blacksquare\)

The measure \(\mu\) is the *self-similar measure* of the maps \(\varphi_i\) and the weights \(p_i\). Different indices may give the same map.

**Lemma 1.3.** Let \(0<\varrho<1\), and let \(\mathcal W_\varrho\) be the set of the words \(w=i_1\cdots i_n\), \(n\ge1\), with \(|r_w|\le\varrho<|r_{i_1\cdots i_{n-1}}|\). Then \(\mathcal W_\varrho\) is finite, \(\varrho a_*<|r_w|\le\varrho\) for \(w\in\mathcal W_\varrho\), \(\sum_{w\in\mathcal W_\varrho}p_w=1\), and
\[
\mu=\sum_{w\in\mathcal W_\varrho}p_w\,(\varphi_w)_*\mu .
\]

**Proof.** Every sequence \(i\) has exactly one prefix in \(\mathcal W_\varrho\): the shortest prefix with \(|r|\le\varrho\). Its length is at most \(n_0\), where \(r_{\max}^{n_0}\le\varrho\); so the set is finite. Its last factor has absolute value at least \(a_*\), which gives \(|r_w|>\varrho a_*\). The events that \(I\) begins with \(w\), for \(w\in\mathcal W_\varrho\), are disjoint, cover the sample space, and have the probabilities \(p_w\). On the event for a word \(w\) of length \(n\), \(\pi(I)=\varphi_w(\pi(I_{n+1},I_{n+2},\dots))\), and the sequence \((I_{n+1},\dots)\) is independent of \((I_1,\dots,I_n)\) with the law of \(I\). So the conditional law of \(\pi(I)\) on this event is \((\varphi_w)_*\mu\). \(\blacksquare\)

## 2. Exact dimensionality and entropy at small scales

**Definition 2.1.** A Borel probability measure \(\nu\) on \(\mathbb R\) is *exact dimensional with the dimension \(d\)* if for \(\nu\)-almost every \(x\)
\[
\lim_{\varrho\to0}\frac{\log\nu((x-\varrho,x+\varrho))}{\log\varrho}=d .
\]

So the mass of a small interval around a typical point behaves like the power \(d\) of its length. For the uniform law on an interval \(d=1\), and for a law with finitely many atoms \(d=0\).

**Hypothesis (ED).** Every self-similar measure in the sense of Section 1 is exact dimensional.

According to [OpenAI-S, Section 1], this is a theorem of D.-J. Feng and H. Hu (2009), which holds without any separation assumption, for ratios of both signs and for repeated maps. It is not proved in this course. It is the only statement about self-similar measures that the course takes from outside.

**Proposition 2.2.** Let \(\nu\) be a bounded law that is exact dimensional with the dimension \(d\). Then
\[
\limsup_{s\to0}\frac{\max\{\mathcal H_s(\nu),H^0_s(\nu)\}}{\log(1/s)}\le d .
\]

**Proof.** Let \(\eta>0\) and \(\nu([-R,R])=1\). For \(n\ge1\) let \(E_n\) be the set of the \(x\) with \(\nu((x-\varrho,x+\varrho))\ge\varrho^{d+\eta}\) for all rational \(\varrho\in(0,\tfrac1n)\). It is a Borel set, because the mass of an open interval of fixed length is a lower semicontinuous function of its centre. The inequality then holds for all real \(\varrho\in(0,\tfrac1n)\): take rational \(\varrho'<\varrho\) tending to \(\varrho\). The sets \(E_n\) increase, and by Definition 2.1 their union has full measure, since \(\log\varrho<0\). Choose \(n\) with \(\nu(E_n)\ge1-\eta\), and let \(E=E_n\), \(\varrho_0=\tfrac1n\).

Take a grid of length \(s<2\varrho_0\) with any shift, and choose a point of \(E\) in every cell that meets \(E\). Two chosen points whose cell labels differ by a multiple of \(3\) have a distance larger than \(2s\), so the open intervals of radius \(\tfrac s2\) around the chosen points of one residue class are disjoint. Each has mass at least \((s/2)^{d+\eta}\). So each class has at most \((2/s)^{d+\eta}\) points, and at most \(3(2/s)^{d+\eta}\) cells meet \(E\). At most \(2R/s+2\) cells meet \([-R,R]\).

Let \(X\) have the law \(\nu\), \(F\) its cell label, and \(Y\) the indicator of \(X\in E\). Then
\[
\begin{aligned}
H(F)&\le H(Y)+H(F\mid Y)\\
&\le1+\log\bigl(3(2/s)^{d+\eta}\bigr)\\
&\quad+\eta\log\bigl(2R/s+2\bigr).
\end{aligned}
\]
For \(s<1\) this is at most \((d+2\eta)\log(1/s)+C\) with a number \(C\) that does not depend on \(s\) and the shift. So the same bound holds for \(\mathcal H_s(\nu)\) and \(H^0_s(\nu)\). Divide by \(\log(1/s)\), let \(s\to0\), and then \(\eta\to0\). \(\blacksquare\)

## 3. Uniform nonsaturation

For laws \(p,q\) on the integers with finitely many values let \(\|p-q\|=\max_B|p(B)-q(B)|\), the maximum over all sets \(B\) of integers; it is equal to \(\sum_j(p_j-q_j)_+\), where \(x_+=\max\{x,0\}\). For a law \(p\) let \(Tp\) be its translate by one step, \((Tp)_j=p_{j-1}\). Then \(\|T^ip-p\|\le i\,\|Tp-p\|\) by the triangle inequality.

**Lemma 3.1.** Let \(F\) be a random variable with finitely many integer values and the law \(p\), and \(J\) an independent fair bit. Then
\[
\|p-Tp\|^2\le2\ln2\cdot I(J;F+J).
\]

**Proof.** Let \(B\) be a set of integers and \(Z\) the indicator of \(F+J\in B\). Given \(J=0\), \(Z=1\) with the probability \(a=p(B)\); given \(J=1\), with the probability \(b=Tp(B)\). By Proposition 3.1 of the lesson on entropy of finite random variables, \(I(J;F+J)\ge I(J;Z)\). And \(I(J;Z)\) is \(h_2(\tfrac{a+b}2)-\tfrac12h_2(a)-\tfrac12h_2(b)\), which is at least \((a-b)^2/(2\ln2)\) by Lemma 5.2 of that lesson. \(\blacksquare\)

**Lemma 3.2.** Let \(F\) be as in Lemma 3.1, \(K\ge2\) an integer, and \(U\) independent of \(F\) and uniform on \(\{0,\dots,K-1\}\). Then
\[
\begin{aligned}
&I(U;F+U)\\
&\quad\le\frac{K(K-1)}2\,\|p-Tp\|\,\log K .
\end{aligned}
\]

**Proof.** Given \(U=i\), the variable \(Z=F+U\) has the law \(T^ip\). Let \(m_j=\min_{0\le i<K}(T^ip)_j\) and \(m=\sum_jm_j\). Since \(p_j-m_j\) is the largest of the numbers \(p_j-(T^ip)_j\),
\[
\begin{aligned}
1-m&=\sum_j(p_j-m_j)\\
&\le\sum_{i=1}^{K-1}\|p-T^ip\|\\
&\le\frac{K(K-1)}2\|p-Tp\| .
\end{aligned}
\]
Let \(W\) be a random variable with the values \(0,1\) such that, given \(U=i\) and \(Z=j\), \(W=1\) with the probability \(m_j/(T^ip)_j\). Then the probability of \(W=1\) and \(Z=j\) given \(U=i\) is \(m_j\), for every \(i\). So \(W\) is independent of \(U\), with \(\mathbb P(W=1)=m\), and given \(W=1\) the law of \(Z\) does not depend on \(U\). By Proposition 3.1 of the lesson on entropy of finite random variables,
\[
\begin{aligned}
I(U;Z)&\le I(U;(Z,W))\\
&=I(U;W)+I(U;Z\mid W).
\end{aligned}
\]
Here \(I(U;W)=0\), the part of \(I(U;Z\mid W)\) for \(W=1\) vanishes, and the part for \(W=0\) is at most \((1-m)\log K\), because \(U\) has \(K\) values. \(\blacksquare\)

**Proposition 3.3.** Let \(X\) be a bounded variable, \(v>0\) and \(K\ge2\) an integer. Then
\[
\begin{aligned}
&\log K-G_{v,Kv}(X)\\
&\quad\le\frac{K(K-1)}2\,\log K\,\sqrt{2\ln2\cdot\Delta_v(X)} .
\end{aligned}
\]

**Proof.** Let \(F_u=\lfloor X/v+u\rfloor\) with the law \(p_u\). By Corollary 3.2 of the lesson on entropy at a scale, the left side is \(\int_0^1I(U;F_u+U)\,du\), and \(\Delta_v(X)=\int_0^1I(J;F_u+J)\,du\). By Lemmas 3.2 and 3.1 and the inequality of Cauchy and Schwarz,
\[
\begin{aligned}
&\int_0^1I(U;F_u+U)\,du\\
&\quad\le c_K\int_0^1\sqrt{2\ln2\cdot I(J;F_u+J)}\,du\\
&\quad\le c_K\sqrt{2\ln2\cdot\Delta_v(X)},
\end{aligned}
\]
with \(c_K=\tfrac12K(K-1)\log K\). \(\blacksquare\)

So if the deficit at the scale \(v\) is small, then the law gains almost the maximal entropy \(\log K\) between the scales \(Kv\) and \(v\), for every fixed \(K\).

**Lemma 3.4.** Let \(\mu\) be a self-similar measure, \(K\ge1\) an integer and \(0<s<v\). Then
\[
\begin{gathered}
G_{s,Ks}(\mu)\ge G_{v,Kv}(\mu)-C_*,\\
C_*=\log\bigl(\tfrac1{a_*}+2\bigr)+1 .
\end{gathered}
\]

**Proof.** By Lemma 1.3 with \(\varrho=s/v\), \(\mu\) is a finite mixture of the laws \((\varphi_w)_*\mu\), \(w\in\mathcal W_\varrho\). By Proposition 2.4 and Lemma 1.1 of the lesson on entropy at a scale,
\[
\begin{aligned}
G_{s,Ks}(\mu)&\ge\sum_wp_w\,G_{s,Ks}\bigl((\varphi_w)_*\mu\bigr)\\
&=\sum_wp_w\,G_{z_w,Kz_w}(\mu),
\end{aligned}
\]
where \(z_w=s/|r_w|\) lies in \([v,v/a_*)\). For such \(z\), by Proposition 1.3 of that lesson, \(\mathcal H_z(\mu)\ge\mathcal H_v(\mu)-\log(z/v+2)\) and \(\mathcal H_{Kz}(\mu)\le\mathcal H_{Kv}(\mu)+1\). So \(G_{z,Kz}(\mu)\ge G_{v,Kv}(\mu)-C_*\). \(\blacksquare\)

**Theorem 3.5 (uniform nonsaturation).** Let \(\mu\) be a self-similar measure that is exact dimensional with a dimension \(d<1\). Then
\[
\delta=\inf_{v>0}\Delta_v(\mu)>0 .
\]

**Proof.** Suppose that \(\Delta_{v_n}(\mu)\to0\) for some numbers \(v_n>0\). Choose an integer \(K\ge2\) with \((1-d)\log K>C_*+2\). By Proposition 3.3, \(G_{v_n,Kv_n}(\mu)\to\log K\); choose \(v=v_n\) with \(G_{v,Kv}(\mu)>\log K-1\). By Lemma 3.4, for every \(0<s<v\),
\[
\begin{gathered}
G_{s,Ks}(\mu)>\beta,\\
\beta=\log K-C_*-1>d\log K .
\end{gathered}
\]
Let \(s_k=vK^{-k}\). Then
\[
\begin{aligned}
&\mathcal H_{s_k}(\mu)-\mathcal H_v(\mu)\\
&\quad=\sum_{j=1}^kG_{vK^{-j},vK^{-j+1}}(\mu)>k\beta,
\end{aligned}
\]
while \(\log(1/s_k)=k\log K+\log(1/v)\). So \(\mathcal H_{s_k}(\mu)/\log(1/s_k)\) has a lower limit of at least \(\beta/\log K>d\) as \(k\to\infty\). This contradicts Proposition 2.2. \(\blacksquare\)

The theorem needs no separation of the maps and no assumption on the signs of the ratios. It uses the self-similarity through Lemma 1.3 only: the measure at the scale \(s\) is a mixture of copies of itself at scales between \(v\) and \(v/a_*\).

**Example 3.6.** For the maps \(x/3\) and \(x/3+\tfrac23\) with the weights \(\tfrac12\), \(\mu\) is the Cantor measure. It is exact dimensional with \(d=\log2/\log3\): the open interval of radius \(3^{-k}\) around a point of the Cantor set has a mass between \(2^{-k}\) and \(2^{1-k}\), because it contains the interval of the \(k\)-th step of the construction through the point and meets at most two such intervals. A numerical evaluation of \(\Delta_v(\mu)\) at thirty scales between \(3^{-5}\) and \(\tfrac23\) gives values between \(0.36\) and \(0.40\). For the uniform law on \([0,1)\), which is the self-similar measure of the maps \(x/2\) and \(x/2+\tfrac12\) and has \(d=1\), \(\Delta_{1/(2n)}=1/(4n\ln2)\) tends to \(0\) (Exercise 4.2 of the lesson on entropy at a scale).

## 4. Exercises

**4.1.** Show that the self-similar measure of a single map \(\varphi(x)=rx+t\) is the unit mass at its fixed point, and that for it \(\Delta_v=1\) for all \(v\).

**4.2.** Show that \(\|p-q\|\) is equal to \(\sum_j(p_j-q_j)_+\) and to \(\tfrac12\sum_j|p_j-q_j|\), for laws \(p,q\) on a finite set.

**4.3.** In Lemma 3.2, compute both sides for \(K=2\) and the law \(p\) with \(p_0=p_1=\tfrac12\).

**4.4.** Let \(\nu\) be the uniform law on \([0,1)\). Show directly that it is exact dimensional with \(d=1\), and that the bound of Proposition 2.2 is attained.

## 5. Solutions

**4.1.** The fixed point is \(x_0=t/(1-r)\), and the unit mass at \(x_0\) satisfies the equation of Proposition 1.2, which has only one solution. A constant has \(\mathcal H_s=0\) for all \(s\), so \(G_{v,2v}=0\) and \(\Delta_v=1\).

**4.2.** The set \(B\) of the \(j\) with \(p_j>q_j\) maximizes \(p(B)-q(B)\), with the value \(\sum_j(p_j-q_j)_+\); exchanging \(p\) and \(q\) gives \(\sum_j(q_j-p_j)_+\) for the maximum of \(q(B)-p(B)\). The two sums are equal, because \(\sum_j(p_j-q_j)=0\), and their sum is \(\sum_j|p_j-q_j|\).

**4.3.** \(Tp\) has the masses \(\tfrac12\) at \(1,2\), so \(\|p-Tp\|=\tfrac12\) and the right side is \(\tfrac12\). The law of \(F+U\) has the masses \(\tfrac14,\tfrac12,\tfrac14\), so \(H(F+U)=\tfrac32\) and \(I(U;F+U)=H(F+U)-H(F)=\tfrac12\). Both sides are equal.

**4.4.** For \(0<x<1\) and small \(\varrho\), \(\nu((x-\varrho,x+\varrho))=2\varrho\), and \(\log(2\varrho)/\log\varrho\to1\). By Exercise 4.2 of the lesson on entropy at a scale, \(\mathcal H_{1/n}(\nu)=\log n+\tfrac1{2n\ln2}\), so \(\mathcal H_s(\nu)/\log(1/s)\to1\) along \(s=\tfrac1n\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
