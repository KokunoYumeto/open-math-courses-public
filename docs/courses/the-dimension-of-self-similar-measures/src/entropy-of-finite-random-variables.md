# Entropy of finite random variables

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The entropy of a random variable with finitely many values measures, in bits, how uncertain its value is. This lesson proves the rules for computing with entropies that the course uses throughout: the chain rule, the effect of conditioning, mutual information, mixtures, and two estimates for the entropy of a biased coin. In September 2026 OpenAI released a proof of a formula for the dimension of self-similar measures on the line [OpenAI-S]; its argument is a calculation with entropies at different scales, and these rules are its arithmetic.

- Entropy is at most the logarithm of the number of values, with equality for the uniform law (Proposition 1.2).
- The chain rule \(H(Y,Z)=H(Y)+H(Z\mid Y)\), and conditioning does not increase entropy (Proposition 2.1).
- Mutual information is not negative, obeys a chain rule, and does not increase under functions (Proposition 3.1).
- The entropy of a mixture lies between the mean of the entropies and that mean plus the entropy of the weights (Proposition 4.1).
- Two estimates for the binary entropy (Lemmas 5.1 and 5.2).

The lesson uses only finite sums and the inequality \(\ln x\le x-1\). All logarithms in this course are to the base \(2\), written \(\log\); \(\ln\) is the natural logarithm.

## 1. Entropy

A *law* on a finite set \(A\) is a family \(p=(p_a)_{a\in A}\) of numbers \(p_a\ge0\) with sum \(1\). Its *entropy* is
\[
H(p)=-\sum_{a\in A}p_a\log p_a,
\]
where \(0\log0\) is read as \(0\). For a random variable \(Z\) with finitely many values, \(H(Z)\) is the entropy of its law \(p_z=\mathbb P(Z=z)\). Each term \(-p_a\log p_a\) is at least \(0\), so \(H\ge0\).

**Lemma 1.1.** Let \(p,q\) be laws on a finite set \(A\) such that \(q_a>0\) whenever \(p_a>0\). Then
\[
\sum_{a:\,p_a>0}p_a\log\frac{p_a}{q_a}\ \ge\ 0,
\]
with equality only if \(p=q\).

**Proof.** For \(x>0\), \(\ln x\le x-1\), with equality only for \(x=1\). So
\[
\sum_{a:\,p_a>0}p_a\ln\frac{q_a}{p_a}\le\sum_{a:\,p_a>0}(q_a-p_a)\le0 .
\]
If both inequalities are equalities, then \(q_a=p_a\) where \(p_a>0\), and the sum of these \(q_a\) is \(1\), so \(q_a=0=p_a\) elsewhere. \(\blacksquare\)

**Proposition 1.2.** If \(Z\) takes at most \(N\) values, then \(0\le H(Z)\le\log N\). \(H(Z)=0\) exactly if \(Z\) is constant with probability one, and \(H(Z)=\log N\) exactly if \(Z\) takes \(N\) values with probability \(\tfrac1N\) each.

**Proof.** A sum of terms \(-p\log p\ge0\) vanishes only if every \(p\) is \(0\) or \(1\). For the upper bound apply Lemma 1.1 with \(q_a=\tfrac1N\) on a set of \(N\) elements that contains the values: \(\sum p_a\log(Np_a)\ge0\) is \(\log N-H(Z)\ge0\). \(\blacksquare\)

## 2. Conditional entropy

Let \(Y,Z\) be random variables with finitely many values on one probability space. The pair \((Y,Z)\) is again such a variable, and \(H(Y,Z)\) is its entropy. For a value \(y\) with \(\mathbb P(Y=y)>0\), let \(H(Z\mid Y=y)\) be the entropy of the conditional law of \(Z\) given \(Y=y\). The *conditional entropy* is the mean
\[
\begin{aligned}
&H(Z\mid Y)\\
&\quad=\sum_{y}\mathbb P(Y=y)\,H(Z\mid Y=y).
\end{aligned}
\]

**Proposition 2.1.** For random variables \(W,Y,Z\) with finitely many values and a function \(f\):

1. \(H(Y,Z)=H(Y)+H(Z\mid Y)\);
2. \(0\le H(Z\mid Y)\le H(Z)\); the first is an equality exactly if \(Z\) is a function of \(Y\) with probability one, the second exactly if \(Y\) and \(Z\) are independent;
3. \(H(f(Z))\le H(Z)\) and \(H(f(Z)\mid Y)\le H(Z\mid Y)\);
4. \(H(Z\mid Y,W)\le H(Z\mid Y)\).

**Proof.** Write \(p(y,z)\), \(p(y)\), \(p(z)\) for the probabilities and \(p(z\mid y)=p(y,z)/p(y)\).

(1) Since \(p(y,z)=p(y)\,p(z\mid y)\),
\[
\begin{aligned}
&-\sum p(y,z)\log p(y,z)\\
&\quad=-\sum p(y,z)\log p(y)\\
&\qquad-\sum p(y,z)\log p(z\mid y),
\end{aligned}
\]
and the two sums on the right are \(H(Y)\) and \(H(Z\mid Y)\).

(2) \(H(Z\mid Y)\) is a mean of entropies, so it is at least \(0\), and it is \(0\) exactly if every conditional law is concentrated on one value. By (1),
\[
\begin{aligned}
&H(Z)-H(Z\mid Y)\\
&\quad=H(Y)+H(Z)-H(Y,Z)\\
&\quad=\sum p(y,z)\log\frac{p(y,z)}{p(y)p(z)},
\end{aligned}
\]
which is at least \(0\) by Lemma 1.1 for the laws \(p(y,z)\) and \(p(y)p(z)\) on the set of pairs, with equality exactly if they coincide.

(3) The pair \((Z,f(Z))\) has the same law as \(Z\) up to renaming the values, so by (1) \(H(Z)=H(f(Z))+H(Z\mid f(Z))\), which is at least \(H(f(Z))\). The second statement is the first for the conditional laws given \(Y=y\), averaged.

(4) Apply (2) to the conditional laws given \(Y=y\) and average. \(\blacksquare\)

Rule (1), applied repeatedly, is the *chain rule*:
\[
\begin{aligned}
&H(Z_1,\dots,Z_n)\\
&\quad=\sum_iH(Z_i\mid Z_1,\dots,Z_{i-1}).
\end{aligned}
\]
With (2) it gives \(H(Z_1,\dots,Z_n)\le\sum_iH(Z_i)\), with equality for independent variables.

## 3. Mutual information

The *mutual information* of \(Z\) and \(Y\), and its conditional version, are
\[
\begin{aligned}
I(Z;Y)&=H(Z)-H(Z\mid Y),\\
I(Z;Y\mid W)&=H(Z\mid W)\\
&\quad-H(Z\mid Y,W).
\end{aligned}
\]

**Proposition 3.1.**

1. \(I(Z;Y)\) equals \(H(Z)+H(Y)-H(Z,Y)\); in particular \(I(Z;Y)=I(Y;Z)\). Both \(I(Z;Y)\) and \(I(Z;Y\mid W)\) are at least \(0\).
2. \(I(Z;Y)\le H(Z)\).
3. \(I(J;(Z,W))\) is the sum of \(I(J;W)\) and \(I(J;Z\mid W)\).
4. \(I(J;f(Z))\le I(J;Z)\), and \(I(J;Z)\le I(J;Z\mid W)+H(W)\).

**Proof.** (1) and (2) are Proposition 2.1 (1), (2) and (4). (3) Both sides are \(H(J)-H(J\mid Z,W)\), after cancelling \(H(J\mid W)\). (4) By (3),
\[
\begin{aligned}
I(J;Z)&=I(J;(Z,f(Z)))\\
&=I(J;f(Z))+I(J;Z\mid f(Z))\\
&\ge I(J;f(Z)).
\end{aligned}
\]
And \(I(J;Z)\le I(J;(Z,W))\), which is \(I(J;W)+I(J;Z\mid W)\), where \(I(J;W)\le H(W)\) by (2) and the symmetry. \(\blacksquare\)

The number \(I(J;Z)\) measures how much the observation of \(Z\) reduces the uncertainty about \(J\). Rule (4) says that a function of the observation cannot tell more than the observation.

## 4. Mixtures

**Proposition 4.1.** Let \(P_1,\dots,P_n\) be laws on a finite set and \(\lambda=(\lambda_1,\dots,\lambda_n)\) a law on the indices. Then
\[
\begin{gathered}
\sum_i\lambda_iH(P_i)\ \le\ H\Bigl(\sum_i\lambda_iP_i\Bigr),\\
H\Bigl(\sum_i\lambda_iP_i\Bigr)\ \le\ \sum_i\lambda_iH(P_i)+H(\lambda).
\end{gathered}
\]

**Proof.** Let \(Y\) have the law \(\lambda\), and let \(Z\) have the conditional law \(P_i\) given \(Y=i\). Then the law of \(Z\) is the mixture, and \(H(Z\mid Y)=\sum_i\lambda_iH(P_i)\). By Proposition 2.1, \(H(Z\mid Y)\le H(Z)\le H(Y,Z)\), and \(H(Y,Z)=H(Y)+H(Z\mid Y)\). \(\blacksquare\)

The first inequality says that the entropy is a concave function of the law.

## 5. The entropy of a coin

For \(0\le u\le1\) let \(h_2(u)=-u\log u-(1-u)\log(1-u)\), the entropy of a variable with two values of probabilities \(u\) and \(1-u\). It is continuous, \(h_2(0)=h_2(1)=0\) and \(h_2(\tfrac12)=1\).

**Lemma 5.1.** \(h_2(u)\le3\sqrt u\) for \(0\le u\le1\).

**Proof.** The function \(-\sqrt u\,\ln u\) on \((0,1]\) has its maximum \(2/e\) at \(u=e^{-2}\), so \(-u\log u\le\tfrac{2}{e\ln2}\sqrt u<1.07\sqrt u\). And \(-\ln(1-u)\le u/(1-u)\), so \(-(1-u)\log(1-u)\le u/\ln2<1.45\sqrt u\). \(\blacksquare\)

**Lemma 5.2.** For \(a,b\in[0,1]\),
\[
\begin{aligned}
&h_2\bigl(\tfrac{a+b}2\bigr)-\tfrac12h_2(a)-\tfrac12h_2(b)\\
&\quad\ge\frac{(a-b)^2}{2\ln2}.
\end{aligned}
\]

**Proof.** On \((0,1)\), \(h_2''(u)=-1/(\ln2\cdot u(1-u))\le-4/\ln2\). So \(k(u)=h_2(u)+\tfrac{2}{\ln2}u^2\) has \(k''\le0\) and is concave on \([0,1]\). Hence \(k(\tfrac{a+b}2)\ge\tfrac12k(a)+\tfrac12k(b)\), and the left side of the lemma is at least
\[
\begin{aligned}
&\frac2{\ln2}\Bigl(\frac{a^2+b^2}2-\frac{(a+b)^2}4\Bigr)\\
&\quad=\frac{(a-b)^2}{2\ln2}.
\end{aligned}
\]
\(\blacksquare\)

The left side of Lemma 5.2 is a mutual information: if \(J\) is a fair coin and \(Z\) is a variable with two values that is \(1\) with probability \(a\) when \(J=0\) and with probability \(b\) when \(J=1\), then \(I(J;Z)=H(Z)-H(Z\mid J)\) is this expression. So two coins whose biases differ by \(|a-b|\) can be told apart at least to the extent \((a-b)^2/(2\ln2)\) bits.

## 6. Exercises

**6.1.** Let \(Z\) be uniform on a set of \(N\) elements and \(Y=f(Z)\). Show that \(H(Z\mid Y)=\sum_y\tfrac{N_y}N\log N_y\), where \(N_y\) is the number of elements with \(f=y\).

**6.2.** Give an example of three variables with \(I(Z;Y\mid W)>I(Z;Y)\), and one with \(I(Z;Y\mid W)<I(Z;Y)\).

**6.3.** Let \(E\) be an event of probability \(q\), and \(Z,Y\) variables with finitely many values such that \(Z\) takes at most \(N\) values and, outside \(E\), \(Z\) is a function of \(Y\). Show that \(H(Z\mid Y)\le h_2(q)+q\log N\).

**6.4.** Show that \(H(Y+Z)\ge H(Z)\) for independent real random variables with finitely many values, and that equality holds if \(Y\) is constant.

## 7. Solutions

**6.1.** Given \(Y=y\), \(Z\) is uniform on \(N_y\) elements, with entropy \(\log N_y\), and \(\mathbb P(Y=y)=N_y/N\).

**6.2.** Let \(Y,Z\) be independent fair coins with values \(0,1\) and \(W=Y+Z\) modulo \(2\). Then \(I(Z;Y)=0\), and given \(W\), \(Z\) is determined by \(Y\), so \(I(Z;Y\mid W)=H(Z\mid W)=1\). For the other direction let \(Y=Z=W\) be one fair coin: \(I(Z;Y)=1\) and \(I(Z;Y\mid W)=0\).

**6.3.** Let \(F\) be the indicator of \(E\). By Proposition 2.1,
\[
\begin{aligned}
H(Z\mid Y)&\le H(Z,F\mid Y)\\
&=H(F\mid Y)+H(Z\mid Y,F)\\
&\le h_2(q)+H(Z\mid Y,F).
\end{aligned}
\]
Given \(F=0\) and \(Y\), \(Z\) is determined, so these conditional entropies vanish; given \(F=1\) and \(Y=y\) the entropy is at most \(\log N\). The mean is at most \(q\log N\).

**6.4.** By Proposition 2.1 (2) and (3), \(H(Y+Z)\ge H(Y+Z\mid Y)\), and given \(Y=y\) the variable \(y+Z\) has the same entropy as \(Z\), by independence. So \(H(Y+Z\mid Y)=H(Z)\). If \(Y\) is constant, \(Y+Z\) is \(Z\) with the values renamed.

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
