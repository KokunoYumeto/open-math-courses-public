# Entropy at a scale

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A probability law on the line, looked at through a grid of intervals of length \(s\), becomes a law on the cells, and this law has an entropy. It tells how many bits are needed to say in which cell a random point lies. The entropy depends a little on the position of the grid; averaging over all positions removes this and gives a quantity \(\mathcal H_s\) with exact rules. The differences \(\mathcal H_s-\mathcal H_t\) measure the information between two scales. This lesson defines these quantities and proves their rules. They are the language of the proof of [OpenAI-S].

- The averaged entropy \(\mathcal H_s\) does not change under translations, and scaling the law by \(a\) changes the scale to \(s/|a|\) (Lemma 1.1).
- Entropies for two grids are compared by counting how many cells of one meet a cell of the other (Lemma 1.2, Proposition 1.3).
- If \(t/s=N\) is an integer, \(\mathcal H_s-\mathcal H_t\) is a mean of conditional entropies; it lies between \(0\) and \(\log N\), is concave in the law, and does not decrease under convolution (Propositions 2.1 and 2.4).
- Adding an independent uniform choice among \(K\) steps of length \(v\) changes the scale from \(v\) to \(Kv\) (Proposition 3.1). So \(1-(\mathcal H_v-\mathcal H_{2v})\) is the information that the cell of \(X+vJ\) gives about a fair bit \(J\) (Corollary 3.2).

The lesson follows [OpenAI-S, Section 2, the lemma on the entropy calculus], which attributes these identities to P. Varjú. The proofs here use sums over cells only; no densities are needed. The lesson continues [Entropy of finite random variables](entropy-of-finite-random-variables.md) and uses the Lebesgue integral of bounded functions on an interval (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)).

## 1. Grids

A *bounded law* is a Borel probability measure \(\nu\) on \(\mathbb R\) with \(\nu([-R,R])=1\) for some \(R\). We also say that a random variable \(X\) with this law is bounded, and write the quantities below with \(X\) or with \(\nu\).

Let \(s>0\) and \(0\le u<1\). The *grid* of length \(s\) with the shift \(u\) consists of the cells \([(j-u)s,(j+1-u)s)\), \(j\in\mathbb Z\). The point \(x\) lies in the cell with the label \(\lfloor x/s+u\rfloor\). For a bounded variable \(X\) the label \(\lfloor X/s+u\rfloor\) takes at most \(2R/s+2\) values. Let
\[
\begin{gathered}
H_{s,u}(X)=H\bigl(\lfloor X/s+u\rfloor\bigr),\\
H^0_s(X)=H_{s,0}(X),\\
\mathcal H_s(X)=\int_0^1H_{s,u}(X)\,du .
\end{gathered}
\]
The integral exists: the probability of the cell \(j\) is a difference of two values of the nondecreasing function \(x\mapsto\nu((-\infty,x))\) at points that depend linearly on \(u\), so it is a Borel function of \(u\); and \(H_{s,u}\) is a finite sum of the continuous function \(-p\log p\) of these probabilities, bounded by \(\log(2R/s+2)\).

**Lemma 1.1.** For a bounded variable \(X\), real \(b\) and \(a\ne0\),
\[
\begin{gathered}
\mathcal H_s(X+b)=\mathcal H_s(X),\\
\mathcal H_s(aX)=\mathcal H_{s/|a|}(X).
\end{gathered}
\]

**Proof.** \(\lfloor(X+b)/s+u\rfloor=\lfloor X/s+u'\rfloor+k\), where \(u+b/s=u'+k\) with \(0\le u'<1\) and an integer \(k\). Adding the constant \(k\) to a label does not change the entropy, and \(u'\) runs through \([0,1)\) once, with the same length element, when \(u\) does. For \(a>0\), \(\lfloor aX/s+u\rfloor=\lfloor X/(s/a)+u\rfloor\). It remains to treat \(a=-1\). If \(X/s-u\) is not an integer, then \(\lfloor-X/s+u\rfloor=-\lfloor X/s-u\rfloor-1\), a one-to-one function of the label \(\lfloor X/s+(1-u)\rfloor=\lfloor X/s-u\rfloor+1\). The probability that \(X/s-u\) is an integer is not zero for at most countably many \(u\), because \(X\) has at most countably many atoms. So \(H_{s,u}(-X)=H_{s,1-u}(X)\) for all but countably many \(u\), and the integrals agree. \(\blacksquare\)

**Lemma 1.2.** Let \(Z\) and \(Z'\) be random variables with finitely many values such that, for every value \(z\) of \(Z\), the variable \(Z'\) takes at most \(m\) values on the event \(Z=z\). Then \(H(Z')\le H(Z)+\log m\).

**Proof.** \(H(Z')\le H(Z,Z')\), and \(H(Z,Z')=H(Z)+H(Z'\mid Z)\), where each conditional law of \(Z'\) has at most \(m\) values. \(\blacksquare\)

**Proposition 1.3.** Let \(X\) be bounded and \(z\ge s>0\). Then
\[
\begin{gathered}
\mathcal H_s(X)-\log\bigl(\tfrac zs+2\bigr)\le\mathcal H_z(X),\\
\mathcal H_z(X)\le\mathcal H_s(X)+1 .
\end{gathered}
\]
Moreover \(|\mathcal H_s(X)-H^0_s(X)|\le1\) and \(|H^0_s(X+b)-H^0_s(X)|\le1\) for real \(b\).

**Proof.** Take a grid of length \(s\) and a grid of length \(z\), with any shifts. A cell of the first is an interval of length \(s\le z\), so it meets at most two cells of the second. A cell of the second, of length \(z\), meets at most \(z/s+2\) cells of the first. By Lemma 1.2, for all shifts \(u,u'\),
\[
\begin{gathered}
H_{z,u'}(X)\le H_{s,u}(X)+1,\\
H_{s,u}(X)\le H_{z,u'}(X)+\log\bigl(\tfrac zs+2\bigr).
\end{gathered}
\]
Integrating over \(u\) and \(u'\) gives the first statement. For \(z=s\) the first line, with \(u'=0\) or \(u=0\), gives \(|\mathcal H_s-H^0_s|\le1\). The label of \(X+b\) in the grid with the shift \(0\) is the label of \(X\) in a grid of the same length with another shift, up to a constant; so the last statement is again the first line with \(z=s\). \(\blacksquare\)

## 2. Two scales with an integer ratio

For \(s,t>0\) let
\[
\begin{gathered}
G_{s,t}(X)=\mathcal H_s(X)-\mathcal H_t(X),\\
\Delta_s(X)=1-G_{s,2s}(X).
\end{gathered}
\]

**Proposition 2.1.** Let \(N\ge1\) be an integer, \(X\) bounded, and \(F_u=\lfloor X/s+u\rfloor\). Then
\[
\begin{aligned}
&G_{s,Ns}(X)\\
&\ =\frac1N\sum_{e=0}^{N-1}\int_0^1H\Bigl(F_u\Bigm|\Bigl\lfloor\frac{F_u+e}N\Bigr\rfloor\Bigr)\,du ,
\end{aligned}
\]
and \(0\le G_{s,Ns}(X)\le\log N\). In particular \(0\le\Delta_s(X)\le1\).

**Proof.** For an integer \(e\) with \(0\le e<N\) and \(0\le u<1\), the number \(u'=(u+e)/N\) lies in \([0,1)\), and
\[
\begin{aligned}
\Bigl\lfloor\frac X{Ns}+u'\Bigr\rfloor&=\Bigl\lfloor\frac{X/s+u+e}N\Bigr\rfloor\\
&=\Bigl\lfloor\frac{F_u+e}N\Bigr\rfloor,
\end{aligned}
\]
because \(\lfloor y/N\rfloor=\lfloor\lfloor y\rfloor/N\rfloor\) for real \(y\) and \(\lfloor X/s+u+e\rfloor=F_u+e\). As \(u\) runs through \([0,1)\) and \(e\) through \(0,\dots,N-1\), \(u'\) runs through \([0,1)\) once, and \(du'=du/N\). So
\[
\begin{aligned}
&\mathcal H_{Ns}(X)\\
&\ =\frac1N\sum_{e=0}^{N-1}\int_0^1H\Bigl(\Bigl\lfloor\frac{F_u+e}N\Bigr\rfloor\Bigr)\,du .
\end{aligned}
\]
The coarse label is a function of \(F_u\), so by the chain rule \(H(F_u)\) minus its entropy is the conditional entropy in the statement. Given the coarse label, \(F_u\) takes at most \(N\) values. \(\blacksquare\)

In words: the cells of a grid of length \(Ns\) are unions of \(N\) consecutive cells of a grid of length \(s\), and \(G_{s,Ns}\) is the mean, over the positions of both grids, of the uncertainty about the fine cell when the coarse cell is known.

A family \((\nu_\omega)\) of laws on a common interval \([-R,R]\), indexed by the points \(\omega\) of a probability space \((\Omega,\mathbb P)\), is *measurable* if \(\omega\mapsto\nu_\omega(B)\) is measurable for every interval \(B\). Its *mean* is the law \(\nu(B)=\int\nu_\omega(B)\,d\mathbb P(\omega)\). A finite mixture \(\sum_i\lambda_i\nu_i\) is the case of a finite set \(\Omega\).

**Lemma 2.2.** Let \(A\) be a finite set and \(\Psi\) a continuous concave function on the set of the laws on \(A\). Let \(p\) be a measurable map from a probability space to this set. Then \(\Psi\bigl(\int p\,d\mathbb P\bigr)\ge\int\Psi(p)\,d\mathbb P\).

**Proof.** For a map \(p\) with finitely many values this is the concavity of \(\Psi\), applied repeatedly. In general, let \(n\ge1\), and divide the set of the laws, a bounded subset of \(\mathbb R^A\), into finitely many convex Borel pieces of diameter at most \(1/n\), for example by cubes. For a piece \(Q\) with \(\mathbb P(p\in Q)>0\) let \(p_Q\) be the mean of \(p\) on the event \(p\in Q\); it is a law on \(A\), and its distance to every point of \(Q\) is at most \(1/n\), because it lies in the closure of the convex set \(Q\). Let \(p_n=p_Q\) on the event \(p\in Q\). Then \(\int p_n=\int p\), and \(p_n\) has finitely many values, so \(\Psi(\int p)\ge\int\Psi(p_n)\). Since \(|p_n-p|\le1/n\) and \(\Psi\) is uniformly continuous, \(\int\Psi(p_n)\to\int\Psi(p)\). \(\blacksquare\)

**Lemma 2.3.** Let \(A\) be a finite set and \(c\) a function on \(A\). For a law \(p\) on \(A\), let \(\Psi(p)=H(F\mid c(F))\), where \(F\) has the law \(p\). Then \(\Psi\) is continuous and concave.

**Proof.** \(\Psi(p)=H(F)-H(c(F))\) is a finite sum of terms \(\pm\,q\log q\) in which \(q\) is a sum of coordinates of \(p\); so it is continuous. Let \(p=\lambda p_1+(1-\lambda)p_2\). Let \(Y\) be \(1\) with probability \(\lambda\) and \(2\) otherwise, and let \(F\) have the law \(p_i\) given \(Y=i\). Then \(F\) has the law \(p\), and by Proposition 2.1 (4) of the lesson on entropy of finite random variables, \(H(F\mid c(F))\ge H(F\mid c(F),Y)\), and the right side is \(\lambda\Psi(p_1)+(1-\lambda)\Psi(p_2)\). \(\blacksquare\)

**Proposition 2.4.** Let \(N\ge1\) be an integer and \(s>0\).

1. If \(\nu\) is the mean of a measurable family \((\nu_\omega)\) of laws on \([-R,R]\), then
\[
G_{s,Ns}(\nu)\ \ge\ \int G_{s,Ns}(\nu_\omega)\,d\mathbb P(\omega).
\]
2. If \(X\) and \(Y\) are independent bounded variables, then \(G_{s,Ns}(X+Y)\ge G_{s,Ns}(X)\).
3. Under the assumption of (1), \(\Delta_s(\nu)\le\int\Delta_s(\nu_\omega)\,d\mathbb P(\omega)\).

**Proof.** (1) Fix \(u\) and \(e\). Let \(A\) be the finite set of the labels of the cells of the grid of length \(s\) with the shift \(u\) that meet \([-R,R]\), and \(c(j)=\lfloor(j+e)/N\rfloor\). The law \(p_\omega\) of the label under \(\nu_\omega\) is a measurable map to the laws on \(A\), and its mean is the law of the label under \(\nu\). Let \(p\) be this mean and \(\Psi\) the function of Lemma 2.3. By Lemmas 2.2 and 2.3,
\[
\Psi(p)\ \ge\ \int\Psi(p_\omega)\,d\mathbb P(\omega).
\]
Here \(\Psi(p)\) is the conditional entropy \(H(F_u\mid\lfloor(F_u+e)/N\rfloor)\) computed for \(\nu\), and \(\Psi(p_\omega)\) is the same for \(\nu_\omega\). The integrand is not negative and is a measurable function of \((u,\omega)\): the probabilities of the cells are differences of values of \((x,\omega)\mapsto\nu_\omega((-\infty,x))\), which is nondecreasing and continuous from the left in \(x\) and measurable in \(\omega\), hence measurable in both. Integrate over \(u\), exchange the two integrals, and take the mean over \(e\). By Proposition 2.1 this is (1).

(2) The law of \(X+Y\) is the mean of the laws of \(X+y\), where \(y\) is distributed as \(Y\); this family is measurable and lives on a common bounded interval. By (1), \(G_{s,Ns}(X+Y)\ge\int G_{s,Ns}(X+y)\,d\mathbb P_Y(y)\), and by Lemma 1.1 every \(G_{s,Ns}(X+y)\) is \(G_{s,Ns}(X)\).

(3) is (1) for \(N=2\). \(\blacksquare\)

The integer ratio is essential in Proposition 2.4: the proof uses that the coarse cell is a function of the fine cell.

## 3. Uniform steps

**Proposition 3.1.** Let \(X\) be bounded, \(v>0\), \(K\ge1\) an integer, and \(U\) a random variable that is independent of \(X\) and uniform on \(\{0,1,\dots,K-1\}\). Then
\[
\mathcal H_v(X+vU)=\mathcal H_{Kv}(X)+\log K .
\]

**Proof.** Fix \(u\), let \(F=\lfloor X/v+u\rfloor\) and \(p_j=\mathbb P(F=j)\). The label of \(X+vU\) in the grid of length \(v\) with the shift \(u\) is \(F+U\), and
\[
\begin{gathered}
\mathbb P(F+U=j)=\frac1K\,P_j,\\
P_j=p_j+p_{j-1}+\dots+p_{j-K+1}.
\end{gathered}
\]
So, since \(\sum_jP_j=K\),
\[
\begin{aligned}
H(F+U)&=-\sum_j\frac{P_j}K\log\frac{P_j}K\\
&=\log K-\frac1K\sum_jP_j\log P_j .
\end{aligned}
\]
On the other hand, for \(0\le e<K\) the label \(\lfloor(F+e)/K\rfloor\) has the value \(i\) with the probability \(P_{iK+K-1-e}\), the sum of the \(p_j\) with \(iK\le j+e<iK+K\). As \(i\) runs through the integers and \(e\) through \(0,\dots,K-1\), the index \(iK+K-1-e\) runs through all integers once. So
\[
\begin{aligned}
&\frac1K\sum_{e=0}^{K-1}H\Bigl(\Bigl\lfloor\frac{F+e}K\Bigr\rfloor\Bigr)\\
&\quad=-\frac1K\sum_jP_j\log P_j .
\end{aligned}
\]
Hence \(H(F+U)\) is \(\log K\) plus this mean. Integrate over \(u\): the left side gives \(\mathcal H_v(X+vU)\), and the right side gives \(\log K+\mathcal H_{Kv}(X)\) by the formula for \(\mathcal H_{Ns}\) in the proof of Proposition 2.1. \(\blacksquare\)

**Corollary 3.2.** In the situation of Proposition 3.1, with \(F_u=\lfloor X/v+u\rfloor\),
\[
\begin{aligned}
&\log K-G_{v,Kv}(X)\\
&\quad=\int_0^1I\bigl(U;F_u+U\bigr)\,du .
\end{aligned}
\]
In particular, for a fair bit \(J\) independent of \(X\), with the values \(0\) and \(1\),
\[
\begin{aligned}
\Delta_v(X)&=\mathcal H_v(X+vJ)-\mathcal H_v(X)\\
&=\int_0^1I\bigl(J;F_u+J\bigr)\,du .
\end{aligned}
\]

**Proof.** By Proposition 3.1, \(\log K-G_{v,Kv}(X)\) equals \(\mathcal H_v(X+vU)-\mathcal H_v(X)\). For fixed \(u\), \(H(F_u)=H(F_u+U\mid U)\), because \(F_u\) and \(U\) are independent and adding a constant does not change the entropy; so \(H(F_u+U)-H(F_u)\) is \(I(U;F_u+U)\). \(\blacksquare\)

So \(\Delta_v(X)\) is small exactly if the cell of \(X+vJ\), at the scale \(v\), tells almost nothing about \(J\): the law of \(X\) looks almost the same as its translate by \(v\), seen through grids of length \(v\). And \(\Delta_v(X)=1\) means that \(J\) can be read off, for almost every position of the grid.

**Example 3.3.** Let \(X\) be constant. Then \(\mathcal H_s(X)=0\) for all \(s\), \(G_{s,t}=0\) and \(\Delta_v(X)=1\). Let \(X\) be uniform on an interval of length \(\ell\), and \(s\) small against \(\ell\). A grid of length \(s\) has about \(\ell/s\) cells of probability \(s/\ell\) each, so \(\mathcal H_s(X)\) is \(\log(\ell/s)\) up to an error that tends to \(0\) with \(s/\ell\). Then \(G_{s,2s}\) is close to \(1\) and \(\Delta_s(X)\) is close to \(0\).

## 4. Exercises

**4.1.** Let \(X\) take the values \(0\) and \(d>0\) with probability \(\tfrac12\) each. Show that \(\mathcal H_s(X)=\min\{1,d/s\}\), and compute \(\Delta_v(X)\) for \(v\ge d\).

**4.2.** Let \(X\) be uniform on \([0,1)\) and \(n\) a positive integer. Show that \(\mathcal H_{1/n}(X)=\log n+\tfrac1{2n\ln2}\), and compute \(\Delta_{1/(2n)}(X)\).

**4.3.** Show that \(G_{s,N_1N_2s}=G_{s,N_1s}+G_{N_1s,N_1N_2s}\), and deduce that \(G_{s,2^ks}(X)\ge k-\sum_{i<k}\Delta_{2^is}(X)\).

**4.4.** Verify Proposition 3.1 and Corollary 3.2 directly for the variable \(X\) of Exercise 4.1 with \(v=d\) and \(K=2\).

## 5. Solutions

**4.1.** The two points lie in one cell exactly if no boundary of the grid falls in \((0,d]\). For \(s\le d\) an interval of length \(d\) always contains a boundary, so the label takes two values with probability \(\tfrac12\) each, and \(\mathcal H_s(X)=1\). For \(s>d\) a boundary falls in \((0,d]\) for a set of shifts of measure \(d/s\), and otherwise the label is constant; so \(\mathcal H_s(X)=d/s\). For \(v\ge d\): \(G_{v,2v}=\tfrac dv-\tfrac d{2v}=\tfrac d{2v}\) and \(\Delta_v=1-\tfrac d{2v}\). In particular \(\Delta_d=\tfrac12\).

**4.2.** A grid of length \(\tfrac1n\) cuts \([0,1)\) into \(n-1\) cells of probability \(\tfrac1n\) and two end pieces of probabilities \(\tfrac an\) and \(\tfrac{1-a}n\), where \(a\) runs through \([0,1)\) uniformly as the shift does. With \(\phi(p)=-p\log p\), \(\phi(\tfrac an)+\phi(\tfrac{1-a}n)=\tfrac1n\log n+\tfrac1nh_2(a)\), so the entropy is \(\log n+\tfrac1nh_2(a)\). The mean of \(h_2\) over \([0,1]\) is \(2\int_0^1(-a\log a)\,da=\tfrac1{2\ln2}\). Hence \(G_{1/(2n),1/n}=1+\tfrac1{4n\ln2}-\tfrac1{2n\ln2}\) and \(\Delta_{1/(2n)}=\tfrac1{4n\ln2}\).

**4.3.** The first identity is the definition. By induction \(G_{s,2^ks}=\sum_{i<k}G_{2^is,2^{i+1}s}\), and the terms are \(1-\Delta_{2^is}\); so the stated inequality is an equality.

**4.4.** The variable \(X+dJ\) takes the values \(0,d,2d\) with the probabilities \(\tfrac14,\tfrac12,\tfrac14\). Every grid of length \(d\) separates them, so \(\mathcal H_d(X+dJ)=\tfrac32\). By Exercise 4.1, \(\mathcal H_{2d}(X)=\tfrac12\), and \(\tfrac12+\log2=\tfrac32\). For the corollary: \(F_u\) takes two consecutive values with probability \(\tfrac12\), so \(H(F_u+J)-H(F_u)=\tfrac32-1=\tfrac12\) for every \(u\), which is \(\Delta_d(X)\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
