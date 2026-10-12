# Block types and pairs at fine scales

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let a self-similar measure have a dimension \(d\) with \(d\chi<h\): smaller than the entropy rate of the walk of maps allows. Then the maps composed from \(n\) blocks of symbols carry more entropy than the measure can show at the scale that corresponds to them. This lesson proves that this entropy sits in pairs of translations that are very close to each other: the finite laws of these translations have a total pair capacity of the order \(n\) at scales finer than \(2^{-An}\), for a suitable number \(A\).

The tool is the pair bound for a finite law. It needs laws whose sets of \(k\)-fold sums are small. For this the blocks are conditioned on their *types*, the numbers of occurrences of each symbol. The type of a block fixes its slope, and then the translations of composed maps are sums of terms from fixed finite sets.

- The parameters \(b\), \(A\), \(A'\), \(\gamma\) (Section 1).
- Blocks, types, and the laws \(\nu_\kappa\) of the translations for given types (Lemmas 2.1, 2.2, 3.1).
- Conditioning on the types keeps the entropy (Proposition 4.1).
- Pair capacity of the order \(n\) in a finite range of scales (Theorem 5.1).

The lesson follows [OpenAI-S, Section 4]. According to [OpenAI-S], conditioning on the types of blocks goes back to work of Galicer, Saglietti, Shmerkin and Yavicoli. The lesson uses [The pair bound for a finite law](the-pair-bound-for-a-finite-law.md), [The random walk of maps and the upper bound for the dimension](the-random-walk-of-maps-and-the-upper-bound.md) and [The one-bit deficit of a self-similar measure](the-one-bit-deficit.md).

## 1. The assumption and the parameters

Throughout the lesson, \(\varphi_i(x)=r_ix+t_i\), \(i\in\Lambda\), are maps with \(0<|r_i|<1\), \(p\) is a law on \(\Lambda\) with all \(p_i>0\), and \(\mu\) is the self-similar measure. The numbers \(h\) and \(\chi\) are those of the lesson on the random walk of maps. We assume that \(\mu\) is exact dimensional with the dimension \(d\), and that
\[
d\chi<h. \tag{1}
\]
By Theorem 3.3 of that lesson, \(d\chi\le h\) always holds. The dimension formula, Theorem 5.1 of the lesson [Disjoint windows and the dimension formula](disjoint-windows-and-the-dimension-formula.md), says that (1) is possible only for \(d=1\).

Let \(m\) be the number of elements of \(\Lambda\). By (1), \(h>0\); so \(m\ge2\), since for a single map \(G_n\) is constant. Choose a number \(\alpha>\chi\) with \(d\alpha<h\), and then an integer \(b\ge1\) with
\[
m\log(b+1)<b\,(h-d\alpha).
\]
Such a \(b\) exists because \(\log(b+1)/b\to0\). Put
\[
\begin{gathered}
A=b\alpha,\qquad A'=\frac{b(\chi+\alpha)}2,\\
h_b=bh-m\log(b+1),\\
\gamma=h_b-dA .
\end{gathered}
\]
Then
\[
b\chi<A'<A,\qquad\gamma>0 .
\]
For instance, for \(m=3\), \(h=\log3\), \(\chi=1\), \(d=1\) one can take \(\alpha=1.3\); the smallest \(b\) is then \(64\), with \(A=83.2\), \(A'=73.6\) and \(\gamma\approx0.17\).

## 2. Blocks and types

A *block* is a word \(w\in\Lambda^b\). Its *type* is the family \(\kappa=(\kappa_i)_{i\in\Lambda}\), where \(\kappa_i\) is the number of the places of \(w\) at which the symbol \(i\) stands. The types are the families of integers \(\kappa_i\ge0\) with the sum \(b\); there are at most \((b+1)^m\) of them. For a type \(\kappa\) let \(N_\kappa\) be the number of the blocks of the type \(\kappa\). Each of them has the probability \(\prod_ip_i^{\kappa_i}\), so the probability that a random block has the type \(\kappa\) is
\[
q_\kappa=N_\kappa\prod_ip_i^{\kappa_i}.
\]
Each block of the type \(\kappa\) has the same slope, with its sign:
\[
r(\kappa)=\prod_ir_i^{\kappa_i}.
\]
For a tuple \(\kappa=(\kappa_0,\dots,\kappa_{n-1})\) of types let
\[
\begin{gathered}
R_j(\kappa)=\prod_{h<j}r(\kappa_h)\quad(0\le j\le n),\\
\sigma_j(\kappa)=-\log|R_j(\kappa)|,\qquad q_\kappa=\prod_{h<n}q_{\kappa_h},
\end{gathered}
\]
with \(R_0(\kappa)=1\) and \(\sigma_0(\kappa)=0\). In this lesson the letter \(R\) always denotes these products; the bound for the support of \(\mu\), which the lesson on the one-bit deficit calls \(R_0\), is not used here.

**Lemma 2.1.** Let \(w_0,\dots,w_{n-1}\) be blocks with the types \(\kappa_0,\dots,\kappa_{n-1}\). Then, with \(R_h=R_h(\kappa)\),
\[
\begin{aligned}
&\varphi_{w_0\cdots w_{n-1}}(x)\\
&\quad=R_n\,x+\sum_{h=0}^{n-1}R_h\,\varphi_{w_h}(0).
\end{aligned}
\]

**Proof.** For \(n=1\) this is \(\varphi_{w_0}(x)=r(\kappa_0)x+\varphi_{w_0}(0)\). For the step, \(\varphi_{w_0\cdots w_{n-1}}=\varphi_{w_0\cdots w_{n-2}}\circ\varphi_{w_{n-1}}\); insert \(\varphi_{w_{n-1}}(x)=r(\kappa_{n-1})x+\varphi_{w_{n-1}}(0)\) into the formula for \(n-1\) blocks. \(\blacksquare\)

So among the compositions of \(n\) blocks with given types, a map is determined by its translation.

Let \(I_1,I_2,\dots\) be independent with the law \(p\). The random blocks
\[
W_h=I_{hb+1}\cdots I_{hb+b},\qquad h=0,1,2,\dots
\]
are independent. Let \(\omega_h\) be the type of \(W_h\), and \(\Omega_n=(\omega_0,\dots,\omega_{n-1})\). The \(\omega_h\) are independent with the law \(q\). We write \(R_j\) and \(\sigma_j\) for \(R_j(\Omega_j)\) and \(\sigma_j(\Omega_j)\). The number \(\sigma_j\) is a sum of \(j\) independent variables \(-\log|r(\omega_h)|\). Each of these is the sum of \(-\log|r_i|\) over the \(b\) symbols of a block, so it has the mean \(b\chi\) and finitely many values.

**Lemma 2.2.** Given \(\Omega_n=\kappa\), the blocks \(W_0,\dots,W_{n-1}\) are independent, and \(W_h\) is uniform on the \(N_{\kappa_h}\) blocks of the type \(\kappa_h\).

**Proof.** For blocks \(w_h\) of the types \(\kappa_h\), the probability that \(W_h=w_h\) for all \(h<n\) is the product of the numbers \(\prod_ip_i^{\kappa_{h,i}}\), and the probability that \(\Omega_n=\kappa\) is the product of the numbers \(N_{\kappa_h}\prod_ip_i^{\kappa_{h,i}}\). The quotient is \(\prod_h1/N_{\kappa_h}\). \(\blacksquare\)

## 3. The laws of the translations

**Definition.** For a tuple \(\kappa\) of \(n\) types, \(\nu_\kappa\) is the law of
\[
\sum_{h=0}^{n-1}R_h(\kappa)\,\varphi_{W_h}(0),
\]
where the \(W_h\) are independent and \(W_h\) is uniform on the blocks of the type \(\kappa_h\).

The law \(\nu_\kappa\) has a finite support with at most \(m^{bn}\) points. By Lemmas 2.1 and 2.2, \(\nu_\kappa\) is the conditional law, given \(\Omega_n=\kappa\), of the translation \(G_{bn}(0)\) of the map \(G_{bn}=\varphi_{W_0\cdots W_{n-1}}\), whose slope is then \(R_n(\kappa)\).

For a real \(u\ne0\) and a law \(\lambda\), let \(\mathsf D_u\lambda\) be the law of \(uX\), where \(X\) has the law \(\lambda\). The sign of \(u\) matters.

**Lemma 3.1.** For every \(n\ge1\),
\[
\mu=\sum_\kappa q_\kappa\,\bigl(\nu_\kappa*\mathsf D_{R_n(\kappa)}\mu\bigr),
\]
where the sum is over the tuples of \(n\) types.

**Proof.** Let \(X'\) have the law \(\mu\) and be independent of the symbols. By Lemma 3.1 of the lesson on the random walk of maps, \(G_{bn}(X')\) has the law \(\mu\). By Lemma 2.1,
\[
G_{bn}(X')=\sum_{h<n}R_h\,\varphi_{W_h}(0)+R_n\,X' .
\]
Given \(\Omega_n=\kappa\), the sum has the law \(\nu_\kappa\) and is independent of \(X'\), and \(R_n=R_n(\kappa)\). So the conditional law of \(G_{bn}(X')\) is \(\nu_\kappa*\mathsf D_{R_n(\kappa)}\mu\), and the event has the probability \(q_\kappa\). \(\blacksquare\)

## 4. Conditioning on the types keeps the entropy

For \(n\ge1\) let
\[
\begin{gathered}
\rho_n=2^{-\lceil An\rceil},\qquad a_n=\lceil An\rceil-1,\\
E_n=\{\sigma_n\le A'n\}.
\end{gathered}
\]
The event \(E_n\) is determined by \(\Omega_n\). Means over the types are written with \(\mathbb E\); for example \(\mathbb E\,H(\nu_{\Omega_n})=\sum_\kappa q_\kappa H(\nu_\kappa)\).

**Proposition 4.1.**

1. \(\mathbb E\,H(\nu_{\Omega_n})=H(G_{bn}\mid\Omega_n)\ge n\,h_b\) for all \(n\ge1\).
2. \(\mathbb E\,H^0_s(\nu_{\Omega_n})\le H^0_s(\mu)+1\) for all \(n\ge1\) and \(s>0\).
3. Let \(\varepsilon=\gamma/4\). There is an \(n_0\) such that for all \(n\ge n_0\)
\[
\mathbb E\Bigl[\mathbf 1_{E_n}\bigl(H(\nu_{\Omega_n})-H^0_{\rho_n}(\nu_{\Omega_n})\bigr)\Bigr]\ge\varepsilon n .
\]

**Proof.** (1) Given \(\Omega_n=\kappa\), the map \(G_{bn}\) has the slope \(R_n(\kappa)\), and its translation has the law \(\nu_\kappa\). So the conditional entropy of \(G_{bn}\) given \(\Omega_n=\kappa\) is \(H(\nu_\kappa)\), and the mean is \(H(G_{bn}\mid\Omega_n)\). By the rules of entropy,
\[
\begin{aligned}
H(G_{bn})&\le H(\Omega_n,G_{bn})\\
&=H(\Omega_n)+H(G_{bn}\mid\Omega_n).
\end{aligned}
\]
Here \(H(G_{bn})\ge bn\,h\), because \(h\) is the infimum of the numbers \(H(G_k)/k\) (Proposition 1.2 of the lesson on the random walk of maps). And \(H(\Omega_n)=nH(\omega_0)\le nm\log(b+1)\), because there are at most \((b+1)^m\) types. This inequality does not need that \(\Omega_n\) is a function of \(G_{bn}\); in general it is not, see Exercise 6.2.

(2) Fix \(\kappa\), and let \(\lambda_\kappa=\nu_\kappa*\mathsf D_{R_n(\kappa)}\mu\). It is the law of \(S+U\), where \(S\) has the law \(\nu_\kappa\) and \(U\) is a bounded variable independent of \(S\), with a law \(P_U\). So the law of the label \(\lfloor(S+U)/s\rfloor\) is the mean, over the values \(u\) of \(U\), of the laws of the labels \(\lfloor(S+u)/s\rfloor\). These are laws on a common finite set, and they depend measurably on \(u\). The entropy is a continuous concave function of a law on a finite set (Proposition 4.1 of the lesson on entropy of finite random variables), so by Lemma 2.2 of the lesson on entropy at a scale
\[
\begin{aligned}
H^0_s(\lambda_\kappa)&\ge\int H^0_s(S+u)\,dP_U(u)\\
&\ge H^0_s(\nu_\kappa)-1 ,
\end{aligned}
\]
where the last step is the bound \(|H^0_s(S+u)-H^0_s(S)|\le1\) of Proposition 1.3 of that lesson. By Lemma 3.1, \(\mu\) is the mixture of the \(\lambda_\kappa\) with the weights \(q_\kappa\), and the entropy of the label is concave:
\[
\begin{aligned}
H^0_s(\mu)&\ge\sum_\kappa q_\kappa\,H^0_s(\lambda_\kappa)\\
&\ge\sum_\kappa q_\kappa\,H^0_s(\nu_\kappa)-1 .
\end{aligned}
\]

(3) Let \(V_\kappa=H(\nu_\kappa)-H^0_{\rho_n}(\nu_\kappa)\). The label is a function of the point, and \(\nu_\kappa\) has at most \(m^{bn}\) points, so
\[
0\le V_\kappa\le H(\nu_\kappa)\le bn\log m .
\]
Let \(\eta=\gamma/(4A)\). By Proposition 2.2 of the lesson on the one-bit deficit, for all large \(n\)
\[
\begin{aligned}
H^0_{\rho_n}(\mu)&\le(d+\eta)\log\frac1{\rho_n}\\
&\le(d+\eta)(An+1).
\end{aligned}
\]
With (1) and (2), and \(h_b-dA=\gamma\), \(\eta A=\gamma/4\),
\[
\begin{aligned}
\mathbb E\,V_{\Omega_n}&\ge n\,h_b-(d+\eta)(An+1)-1\\
&=\tfrac34\gamma\,n-(d+\eta+1),
\end{aligned}
\]
which is at least \(\tfrac12\gamma n\) for large \(n\). The variable \(\sigma_n\) is a sum of \(n\) independent variables with the mean \(b\chi<A'\) and a common variance \(v\). As in Lemma 1.3 of the lesson on the random walk of maps,
\[
\begin{aligned}
\mathbb P(E_n^c)&=\mathbb P\bigl(\sigma_n-nb\chi>n(A'-b\chi)\bigr)\\
&\le\frac v{n\,(A'-b\chi)^2},
\end{aligned}
\]
which tends to \(0\). So for large \(n\)
\[
\mathbb E\bigl[\mathbf 1_{E_n^c}V_{\Omega_n}\bigr]\le bn\log m\cdot\mathbb P(E_n^c)\le\tfrac14\gamma\,n ,
\]
and the mean of \(\mathbf 1_{E_n}V_{\Omega_n}\) is at least \(\tfrac12\gamma n-\tfrac14\gamma n\). \(\blacksquare\)

Statement (3) is the place where the assumption (1) enters. The exact entropy of the translations is at least \(nh_b\), while their cells of length \(\rho_n\approx2^{-An}\) can show at most about \(dAn\), the entropy of \(\mu\) at this scale. The difference \(\gamma n\) is hidden inside the cells.

## 5. Pairs in a finite range of scales

**Lemma 5.1.** Let \(\kappa\) be a tuple of \(n\) types, \(F\) the support of \(\nu_\kappa\), and \(k\ge1\). Then
\[
\log|kF|\le n\,m^b\log(k+1).
\]

**Proof.** Let \(\mathcal D\) be the set of the numbers \(\varphi_w(0)\), \(w\in\Lambda^b\); it has at most \(m^b\) elements. A sum of \(k\) elements of \(\mathcal D\) is determined by the number of times each element occurs, a number between \(0\) and \(k\). So the set \(k\mathcal D\) of these sums has at most \((k+1)^{m^b}\) elements. Every point of \(F\) is a sum \(\sum_{h<n}R_h(\kappa)x_h\) with \(x_h\in\mathcal D\). A sum of \(k\) points of \(F\) is therefore \(\sum_{h<n}R_h(\kappa)y_h\) with \(y_h\in k\mathcal D\), and there are at most \(|k\mathcal D|^n\) such numbers. \(\blacksquare\)

The lemma would fail without the types: the slopes \(R_h\) would vary with the words, and the sums could not be collected block by block.

**Theorem 5.1 (pair capacity in bands).** There are a number \(c>0\) and an integer \(n_0\) such that for every \(n\ge n_0\) there is an integer \(B_n\ge a_n\) with
\[
\mathbb E\Bigl[\mathbf 1_{E_n}\sum_{\ell=a_n}^{B_n}c_\ell(\nu_{\Omega_n})\Bigr]\ge c\,n .
\]

**Proof.** Let \(\varepsilon\) and \(n_0\) be as in Proposition 4.1 (3). Choose an integer \(k\ge1\) with
\[
m^b\log(k+1)<\frac{k\varepsilon}2 .
\]
Let \(n\ge n_0\) and \(\kappa\) a tuple of \(n\) types. The pair bound, Theorem 1.1 of the lesson on the pair bound for a finite law, for \(\nu_\kappa\) and \(\rho=\rho_n\), together with Lemma 5.1, gives
\[
\begin{aligned}
&C_k\sum_{\ell:\,2^{-\ell}\le2\rho_n}c_\ell(\nu_\kappa)\\
&\quad\ge k\,V_\kappa-n\,m^b\log(k+1),
\end{aligned}
\]
with \(V_\kappa\) as in the proof of Proposition 4.1. Since \(2\rho_n=2^{-a_n}\), the sum is over the \(\ell\ge a_n\). Multiply by \(\mathbf 1_{E_n}\) and take the mean over the types. By Proposition 4.1 (3),
\[
\begin{aligned}
&C_k\,\mathbb E\Bigl[\mathbf 1_{E_n}\sum_{\ell\ge a_n}c_\ell(\nu_{\Omega_n})\Bigr]\\
&\quad\ge k\varepsilon n-n\,m^b\log(k+1)\ \ge\ \frac{k\varepsilon n}2 .
\end{aligned}
\]
There are finitely many tuples of \(n\) types, and each \(\nu_\kappa\) has only finitely many pair capacities different from \(0\). Let \(B_n\ge a_n\) be an integer such that \(c_\ell(\nu_\kappa)=0\) for all \(\ell>B_n\) and all these \(\kappa\). Then the sum over \(\ell\ge a_n\) is the sum from \(a_n\) to \(B_n\), and the theorem holds with \(c=k\varepsilon/(2C_k)\). \(\blacksquare\)

The numbers \(b\), \(A\), \(A'\), \(c\), \(n_0\) do not depend on \(n\). Nothing is said about the size of \(B_n\): the pairs may lie at scales far below \(2^{-An}\). The pairs counted in the theorem have sizes below \(2^{1-a_n}\le4\cdot2^{-An}\), while on the event \(E_n\) the maps of \(n\) blocks contract by \(|R_n|\ge2^{-A'n}\) only. So the two points of a pair are much closer to each other than the size of the copies of \(\mu\) that the maps of \(n\) blocks attach to them (Exercise 6.4).

## 6. Exercises

**6.1.** Let \(\Lambda=\{0,1,2\}\) and \(b=2\). List the types with their numbers \(N_\kappa\) and probabilities \(q_\kappa\), and check that the \(q_\kappa\) add up to \(1\).

**6.2.** For the maps \(\tfrac x3\), \(\tfrac x3+1\), \(\tfrac x3+3\) with the weights \(\tfrac13\) and \(b=2\), \(n=1\): compute the laws \(\nu_\kappa\), and \(H(G_2\mid\Omega_1)\), \(H(G_2)\), \(H(\Omega_1)\). Show that \(\Omega_1\) is not a function of \(G_2\).

**6.3.** Let all the ratios be equal, \(r_i=r\). Show that the type of a block is not needed in Lemma 5.1: the support \(F\) of the law of \(G_{bn}(0)\) satisfies \(\log|kF|\le n\,m^b\log(k+1)\).

**6.4.** Show that \(2^{-\ell}\le2\rho_n\) exactly if \(\ell\ge a_n\). Show that on the event \(E_n\) a pair with \(2^{-\ell}\le|x-y|<2^{1-\ell}\) and \(\ell\ge a_n\) satisfies \(|x-y|\le4\cdot2^{-(A-A')n}\,|R_n|\).

## 7. Solutions

**6.1.** With \(\kappa=(\kappa_0,\kappa_1,\kappa_2)\): the types \((2,0,0)\), \((0,2,0)\), \((0,0,2)\) have \(N_\kappa=1\) and \(q_\kappa=p_i^2\); the types \((1,1,0)\), \((1,0,1)\), \((0,1,1)\) have \(N_\kappa=2\) and \(q_\kappa=2p_ip_j\). The sum is \((p_0+p_1+p_2)^2=1\).

**6.2.** With \(t_0=0\), \(t_1=1\), \(t_2=3\), the block \(ij\) has the translation \(t_i+t_j/3\). The three types with one block give unit masses at \(0\), \(\tfrac43\), \(4\). The type of the blocks \(01,10\) gives the uniform law on \(\{\tfrac13,1\}\); the type of \(02,20\) the uniform law on \(\{1,3\}\); the type of \(12,21\) the uniform law on \(\{2,\tfrac{10}3\}\). So \(H(G_2\mid\Omega_1)=3\cdot\tfrac29\cdot1=\tfrac23\). By Example 3.5 of the lesson on the random walk of maps, \(H(G_2)=\log9-\tfrac29\). The types have the probabilities \(\tfrac19\) (three times) and \(\tfrac29\) (three times), so \(H(\Omega_1)=\log9-\tfrac69\). The inequality \(H(G_2\mid\Omega_1)\ge H(G_2)-H(\Omega_1)\) from the proof of Proposition 4.1 (1) reads \(\tfrac23\ge\tfrac49\). The blocks \(10\) and \(02\) give the same map \(\tfrac x9+1\) and have different types, so the map does not determine the type.

**6.3.** Every map of \(j\) blocks has the slope \(r^{bj}\), so by the computation of Lemma 2.1, \(G_{bn}(0)=\sum_{h<n}r^{bh}\varphi_{W_h}(0)\) for all words. The proof of Lemma 5.1 applies with \(R_h=r^{bh}\).

**6.4.** \(2\rho_n=2^{1-\lceil An\rceil}=2^{-a_n}\), and \(2^{-\ell}\le2^{-a_n}\) exactly if \(\ell\ge a_n\). For such a pair, \(|x-y|<2^{1-\ell}\le2^{1-a_n}\), and \(2^{1-a_n}=2^{2-\lceil An\rceil}\le4\cdot2^{-An}\). On \(E_n\), \(|R_n|=2^{-\sigma_n}\ge2^{-A'n}\), so \(2^{-An}\le2^{-(A-A')n}|R_n|\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
