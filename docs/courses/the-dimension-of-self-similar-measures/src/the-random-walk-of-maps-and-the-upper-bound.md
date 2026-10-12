# The random walk of maps and the upper bound for the dimension

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A self-similar measure is built by composing maps chosen at random. After \(n\) steps the composed map \(G_n\) has contracted by about \(2^{-n\chi}\), and it carries the entropy \(H(G_n)\), which is about \(nh\). Different words may give the same map, and \(h\) counts maps, not words. This lesson defines the two numbers \(h\) and \(\chi\) and proves that the dimension \(d\) of the measure satisfies
\[
d\le\min\Bigl\{1,\frac h\chi\Bigr\}.
\]
The dimension formula of [OpenAI-S] says that this is an equality.

- The entropy rate \(h\) of the walk of maps and the exponent \(\chi\) (Proposition 1.2).
- For an exact-dimensional law, the entropy at the scale \(s\) is \((d+o(1))\log(1/s)\) (Proposition 2.1).
- The upper bound (Theorem 3.3), with an example in which exact overlaps lower the dimension.

The lesson follows [OpenAI-S, Section 1]. There the upper bound is proved with coverings and Hausdorff dimension; here it is proved with entropies at a scale. The lesson continues [The one-bit deficit of a self-similar measure](the-one-bit-deficit.md), whose notation for self-similar measures it uses, and uses [Entropy at a scale](entropy-at-a-scale.md) and [Entropy of finite random variables](entropy-of-finite-random-variables.md).

## 1. The walk of maps

Let \(\varphi_i(x)=r_ix+t_i\), \(i\in\Lambda\), with \(0<|r_i|<1\), let \(p\) be a law on \(\Lambda\) with all \(p_i>0\), and \(\mu\) the self-similar measure, as in Section 1 of the lesson on the one-bit deficit. Let \(I_1,I_2,\dots\) be independent with the law \(p\), and
\[
G_n=\varphi_{I_1}\circ\dots\circ\varphi_{I_n}.
\]
This is a random variable with values in the finite set of the maps \(\varphi_w\), \(w\in\Lambda^n\); a map \(x\mapsto rx+t\) is given by the pair \((r,t)\). The probability that \(G_n\) is the map \(g\) is the sum of the \(p_w\) over the words \(w\) with \(\varphi_w=g\). An *exact overlap* is an equality \(\varphi_u=\varphi_v\) for two different words of the same length.

**Lemma 1.1.** Let \(a_1,a_2,\dots\) be real numbers with \(a_n\ge0\) and \(a_{n+m}\le a_n+a_m\) for all \(n,m\ge1\). Then \(a_n/n\) converges to \(\inf_{k\ge1}a_k/k\).

**Proof.** Fix \(k\), and let \(c\) be the largest of \(a_1,\dots,a_k\). Write \(n>k\) as \(n=qk+j\) with an integer \(q\ge1\) and \(1\le j\le k\). Then \(a_n\le q\,a_k+a_j\le\tfrac nk\,a_k+c\), so \(a_n/n\le a_k/k+c/n\). Hence the upper limit of \(a_n/n\) is at most \(a_k/k\), for every \(k\), and the lower limit is at least the infimum. \(\blacksquare\)

**Proposition 1.2.** The limit
\[
h=\lim_{n\to\infty}\frac{H(G_n)}n=\inf_{n\ge1}\frac{H(G_n)}n
\]
exists, and \(0\le h\le H(p)\). If there are no exact overlaps, then \(H(G_n)=nH(p)\) for all \(n\) and \(h=H(p)\).

**Proof.** \(G_{n+m}=G_n\circ G'\), where \(G'=\varphi_{I_{n+1}}\circ\dots\circ\varphi_{I_{n+m}}\) is independent of \(G_n\) and has the law of \(G_m\). So \(G_{n+m}\) is a function of the pair \((G_n,G')\), and by Proposition 2.1 of the lesson on entropy of finite random variables
\[
\begin{aligned}
H(G_{n+m})&\le H(G_n,G')\\
&=H(G_n)+H(G_m).
\end{aligned}
\]
Lemma 1.1 gives the limit. \(G_1\) is a function of \(I_1\), so \(h\le H(G_1)\le H(p)\). Without exact overlaps, \(G_n\) and the word \(I_1\cdots I_n\) determine each other, and the word has the entropy \(nH(p)\). \(\blacksquare\)

The number \(h\) is the *entropy rate of the walk of maps*. The second number is the *exponent*
\[
\chi=-\sum_{i\in\Lambda}p_i\log|r_i|>0 .
\]
The slope of \(G_n\) is \(r_{I_1}\cdots r_{I_n}\), so \(-\log\) of its absolute value is a sum of \(n\) independent terms with the mean \(\chi\).

**Lemma 1.3.** Let \(\sigma^2=\sum_ip_i(\log|r_i|+\chi)^2\). For every \(\varepsilon>0\) and \(n\ge1\), the slope \(r_{G_n}\) of \(G_n\) satisfies
\[
\mathbb P\bigl(|r_{G_n}|>2^{-n(\chi-\varepsilon)}\bigr)\le\frac{\sigma^2}{n\varepsilon^2}.
\]

**Proof.** Let \(\xi_k=-\log|r_{I_k}|-\chi\) and \(S=\xi_1+\dots+\xi_n\). The \(\xi_k\) are independent with the mean \(0\), so \(\mathbb E\,\xi_k\xi_l=0\) for \(k\ne l\) and \(\mathbb ES^2=n\sigma^2\). The event in the statement is \(S<-n\varepsilon\). On it \(S^2>n^2\varepsilon^2\), so its probability is at most \(\mathbb ES^2/(n^2\varepsilon^2)\). \(\blacksquare\)

## 2. Entropy and dimension

Proposition 2.2 of the lesson on the one-bit deficit bounds the entropy at small scales of an exact-dimensional law from above. The same number is a lower bound.

**Proposition 2.1.** Let \(\nu\) be a bounded law that is exact dimensional with the dimension \(d\). Then
\[
\liminf_{s\to0}\frac{\min\{\mathcal H_s(\nu),H^0_s(\nu)\}}{\log(1/s)}\ge d .
\]
Together with the upper bound, \(\mathcal H_s(\nu)/\log(1/s)\) and \(H^0_s(\nu)/\log(1/s)\) converge to \(d\) as \(s\to0\). In particular \(0\le d\le1\).

**Proof.** The mass of an interval is at most \(1\), so \(d\ge0\) by the definition. If \(d=0\) the first statement holds because entropies are not negative. Let \(d>0\) and \(0<\eta<d\). For \(n\ge1\) let \(E_n\) be the set of the \(x\) with \(\nu((x-\varrho,x+\varrho))\le\varrho^{d-\eta}\) for all rational \(\varrho\in(0,\tfrac1n)\). It is a Borel set, because the mass of an open interval of fixed length is a lower semicontinuous function of its centre. The inequality then holds for all real \(\varrho\in(0,\tfrac1n)\): take rational \(\varrho'>\varrho\) tending to \(\varrho\). The sets \(E_n\) increase, and by the definition of exact dimensionality their union has full measure, since \(\log\varrho<0\). Choose \(n\) with \(\nu(E_n)\ge1-\eta\).

Take a grid of a length \(s<\tfrac1n\) with any shift. A cell \(C\) that contains a point \(x\) of \(E_n\) lies in \((x-s,x+s)\), so \(\nu(C)\le s^{d-\eta}\) and \(\log(1/\nu(C))\ge(d-\eta)\log(1/s)\). The cells that meet \(E_n\) have a total mass of at least \(\nu(E_n)\). So the entropy of the label is
\[
\begin{aligned}
&\sum_C\nu(C)\log\frac1{\nu(C)}\\
&\quad\ge(d-\eta)\log\frac1s\sum_{C\cap E_n\ne\emptyset}\nu(C)\\
&\quad\ge(1-\eta)(d-\eta)\log\frac1s .
\end{aligned}
\]
This holds for every shift, hence for \(\mathcal H_s(\nu)\) and \(H^0_s(\nu)\). Divide by \(\log(1/s)\), let \(s\to0\), and then \(\eta\to0\). For the last statement, \(H^0_s(\nu)\le\log(2R/s+2)\) if \(\nu([-R,R])=1\), and this divided by \(\log(1/s)\) tends to \(1\). \(\blacksquare\)

## 3. The upper bound

**Lemma 3.1.** For every \(n\ge1\),
\[
\mu=\sum_{w\in\Lambda^n}p_w\,(\varphi_w)_*\mu .
\]
So if \(X'\) has the law \(\mu\) and is independent of \(I_1,\dots,I_n\), then \(G_n(X')\) has the law \(\mu\).

**Proof.** For \(n=1\) this is the equation of Proposition 1.2 of the lesson on the one-bit deficit. If it holds for \(n\), insert the equation for \(n=1\) into each term: \((\varphi_w)_*\mu=\sum_ip_i(\varphi_w\circ\varphi_i)_*\mu\). Given \(I_1\cdots I_n=w\), the variable \(G_n(X')=\varphi_w(X')\) has the law \((\varphi_w)_*\mu\). \(\blacksquare\)

**Lemma 3.2.** For every \(n\ge1\) and \(s>0\),
\[
\begin{aligned}
H^0_s(\mu)&\le H(G_n)+\log(2R_0+2)\\
&\quad+\mathbb P\bigl(|r_{G_n}|>s\bigr)\,\log\bigl(2R_0/s+2\bigr).
\end{aligned}
\]

**Proof.** Let \(X=G_n(X')\) as in Lemma 3.1 and \(Z=\lfloor X/s\rfloor\). Then
\[
\begin{aligned}
H^0_s(\mu)=H(Z)&\le H(G_n,Z)\\
&=H(G_n)+H(Z\mid G_n).
\end{aligned}
\]
Given \(G_n=g\), the variable \(X\) lies in the image of \([-R_0,R_0]\) under \(g\), an interval of the length \(2R_0|r_g|\). An interval of the length \(\lambda\) meets at most \(\lambda/s+2\) cells of the length \(s\). If \(|r_g|\le s\), this is at most \(2R_0+2\); in every case \(|r_g|<1\) and it is at most \(2R_0/s+2\). So the conditional entropy of \(Z\) given \(G_n=g\) is at most \(\log(2R_0+2)\) in the first case and at most \(\log(2R_0/s+2)\) in general. The mean over \(g\) is \(H(Z\mid G_n)\), and it is at most \(\log(2R_0+2)\) plus \(\log(2R_0/s+2)\) times the probability that \(|r_{G_n}|>s\). \(\blacksquare\)

**Theorem 3.3 (upper bound).** Let \(\mu\) be a self-similar measure that is exact dimensional with the dimension \(d\). Then
\[
d\le\min\Bigl\{1,\frac h\chi\Bigr\}.
\]

**Proof.** \(d\le1\) by Proposition 2.1. Let \(0<\varepsilon<\chi\) and \(s_n=2^{-n(\chi-\varepsilon)}\), so that \(\log(1/s_n)=n(\chi-\varepsilon)\) and \(s_n\to0\). Since \(s_n\le1\), the number \(\log(2R_0/s_n+2)\) is at most \(\log(2R_0+2)+n(\chi-\varepsilon)\). By Lemmas 3.2 and 1.3,
\[
\begin{aligned}
H^0_{s_n}(\mu)&\le H(G_n)+2\log(2R_0+2)\\
&\quad+\frac{\sigma^2}{n\varepsilon^2}\,n(\chi-\varepsilon).
\end{aligned}
\]
Divide by \(n(\chi-\varepsilon)\) and let \(n\to\infty\). The left side has a lower limit of at least \(d\), by Proposition 2.1. On the right, \(H(G_n)/n\to h\), and the other two terms, divided by \(n\), tend to \(0\). So \(d\le h/(\chi-\varepsilon)\) for every \(\varepsilon\), and \(d\le h/\chi\). \(\blacksquare\)

**Example 3.4.** For the two maps \(x/3\) and \(x/3+\tfrac23\) with the weights \(\tfrac12\) there are no exact overlaps, so \(h=1\), and \(\chi=\log3\). The Cantor measure has \(d=\log2/\log3=h/\chi\) (Example 3.6 of the lesson on the one-bit deficit). For the maps \(x/2\) and \(x/2+\tfrac12\) with the weights \(\tfrac12\), \(h=\chi=1\), and \(\mu\) is the uniform law on \([0,1)\) with \(d=1\). In both cases the bound is an equality.

**Example 3.5.** Let \(\varphi_0(x)=\tfrac x3\), \(\varphi_1(x)=\tfrac x3+1\), \(\varphi_2(x)=\tfrac x3+3\), with the weights \(\tfrac13\). Then
\[
\varphi_1\circ\varphi_0(x)=\frac x9+1=\varphi_0\circ\varphi_2(x),
\]
an exact overlap. The nine words of length \(2\) give eight maps, one of them with the probability \(\tfrac29\), so \(H(G_2)=\log9-\tfrac29\) and
\[
h\le\frac{H(G_2)}2=\log3-\frac19 .
\]
With \(\chi=\log3\), Theorem 3.3 gives \(d\le1-\tfrac1{9\log3}<0.93\) under the hypothesis (ED), while \(H(p)/\chi=1\). An enumeration of the words of length \(n\le9\) finds \(3,8,21,55,144,377,987,2584,6765\) different maps and \(H(G_9)/9<1.3607\), so \(d<0.8585\).

**The dimension formula.** The main theorem of [OpenAI-S] is the equality \(d=\min\{1,h/\chi\}\) for every self-similar measure on the line, with no assumption on the maps besides \(0<|r_i|<1\). By Theorem 3.3 it is equivalent to the statement that the two inequalities
\[
d<1,\qquad d\chi<h
\]
do not hold together. This is proved in the lesson [Disjoint windows and the dimension formula](disjoint-windows-and-the-dimension-formula.md). [OpenAI-S] states the formula for the Hausdorff dimension of \(\mu\), the infimum of the Hausdorff dimensions of the Borel sets of positive measure, and notes that for an exact-dimensional measure this number is \(d\). The course works with \(d\) and does not use Hausdorff dimension.

## 4. Exercises

**4.1.** Give a sequence as in Lemma 1.1 for which \(a_n/n\) is not monotone.

**4.2.** For the maps of Example 3.5 with arbitrary weights \(p_0,p_1,p_2>0\), show that
\[
\begin{aligned}
H(G_2)&=2H(p)\\
&\quad-p_0(p_1+p_2)\,h_2\Bigl(\frac{p_1}{p_1+p_2}\Bigr).
\end{aligned}
\]

**4.3.** Let \(\varphi_t(x)=\tfrac x2+t\) for \(t\in\{0,1,2\}\), with any weights. Show that at most \(2^{n+1}-1\) different maps \(\varphi_w\) have the length \(n\), and that \(h\le1=\chi\).

**4.4.** Let all the ratios be equal: \(r_i=r\) for all \(i\). Show without Lemma 1.3 that \(H^0_{|r|^n}(\mu)\le H(G_n)+\log(2R_0+2)\), and deduce Theorem 3.3 for this case.

## 5. Solutions

**4.1.** Let \(a_n=1\) for odd \(n\) and \(a_n=2\) for even \(n\). A sum \(a_n+a_m\) is at least \(2\), so \(a_{n+m}\le a_n+a_m\). And \(a_3/3=\tfrac13<\tfrac12=a_4/4\), while \(a_n/n\to0\).

**4.2.** \(\varphi_i\circ\varphi_j(x)=\tfrac x9+t_i+\tfrac{t_j}3\) with \(t_0=0\), \(t_1=1\), \(t_2=3\). The nine numbers \(t_i+t_j/3\) are \(0,\tfrac13,1,1,\tfrac43,2,3,\tfrac{10}3,4\); only the words \(02\) and \(10\) give the same map. The word of length \(2\) has the entropy \(2H(p)\). Passing from the word to the map merges the two words of the probabilities \(p_0p_2\) and \(p_1p_0\) into one value. By the chain rule the entropy drops by the entropy of the word given the map, which is the probability \(p_0(p_1+p_2)\) of this value times \(h_2\) of the conditional probability \(p_1/(p_1+p_2)\).

**4.3.** \(\varphi_w(x)=2^{-n}x+\sum_{k=1}^n2^{-(k-1)}t_{i_k}\), and the sum is \(2^{-(n-1)}\) times an integer between \(0\) and \(2(2^n-1)\). So there are at most \(2^{n+1}-1\) maps, \(H(G_n)\le n+1\) and \(h\le1\). Here \(\chi=\log2=1\).

**4.4.** Every map of length \(n\) has the slope \(r^n\), so \(\mathbb P(|r_{G_n}|>|r|^n)=0\), and Lemma 3.2 with \(s=|r|^n\) gives the inequality. Divide by \(\log(1/s)=n\chi\), where \(\chi=-\log|r|\), and let \(n\to\infty\): by Proposition 2.1 the left side has a lower limit of at least \(d\), and the right side tends to \(h/\chi\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Section 1. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
