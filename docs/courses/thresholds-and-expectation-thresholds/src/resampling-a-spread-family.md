# Resampling a spread family

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the second Kahn–Kalai conjecture repeatedly meets the following situation. A probability law on subsets of a finite set \(X\) is given, and a random set \(W\) of small density \(\rho\) should contain one of its sets. In a single step this is hopeless: a fixed set of size \(m\) lies inside \(W\) with probability \(\rho^m\). The step proved in this lesson makes partial progress instead. With high probability, one sample of \(W\) selects a set \(A_b\) of the law and leaves only the *fragment* \(A_b\setminus W\), of at most half the size, still to be covered; the fragments are again spread, so the step can be repeated. The selection plants a set from the law into \(W\) and resamples it from the posterior distribution; this construction is due to Mossel, Niles-Weed, Sun and Zadik [MNSZ-2]. Theorem 3.1 is the version used by OpenAI [OpenAI-KK2] in [Covering a probability tree](covering-a-probability-tree.md); its second part bounds how much the selection changes the law of \(W\) outside the selected set.

We use the notation \(\mu_\rho\) of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md): \(W\sim\mu_\rho\) contains each element of \(X\) independently with probability \(\rho\).

## 1. Spread laws

**Definition 1.1.** An *indexed family* on a finite set \(X\) consists of a finite index set \(B\), *labels* \(A_b\subseteq X\) for \(b\in B\), and *weights* \(\nu_b>0\) with \(\sum_b\nu_b=1\). Different indices may carry the same label, and labels may be empty. We write \(c\sim\nu\) for a random index with \(\mathbb P(c=b)=\nu_b\). For \(a>0\), the family is *\(a\)-spread* if
\[
\mathbb P_{c\sim\nu}(J\subseteq A_c)\le a^{|J|}\qquad\text{for every nonempty }J\subseteq X.\tag{1.1}
\]

For \(0<a<1\), the product law \(\mu_a\), indexed by all subsets of \(X\), satisfies \(\mu_a(J\subseteq W)=a^{|J|}\); so it is \(a\)-spread, with equality. A spread law behaves like a product law as far as containing a fixed set is concerned, although all its sets may have the same size:

**Lemma 1.2.** Let \(1\le k\le N=|X|\), and let \(\nu\) be the uniform law on the \(k\)-element subsets of \(X\). Then \(\nu\) is \(\frac kN\)-spread.

**Proof.** For \(|J|=j\le k\), \(\mathbb P(J\subseteq A)=\binom{N-j}{k-j}\big/\binom Nk=\prod_{i=0}^{j-1}\frac{k-i}{N-i}\le\bigl(\frac kN\bigr)^j\), since \(\frac{k-i}{N-i}\le\frac kN\) when \(k\le N\). For \(j>k\) the probability is \(0\). \(\square\)

**Lemma 1.3** (overlaps). Let the family be \(a\)-spread, let \(b\in B\) with \(|A_b|\le m\), and let \(c\sim\nu\). For every integer \(0\le r\le m\),
\[
\mathbb P\bigl(|A_c\cap A_b|=r\bigr)\le\binom mr\,a^r.
\]

**Proof.** For \(r=0\) the right side is \(1\). For \(r\ge1\), the event implies \(J\subseteq A_c\) for the \(r\)-element set \(J=A_c\cap A_b\subseteq A_b\). A union bound over the \(\binom{|A_b|}r\le\binom mr\) subsets \(J\subseteq A_b\) of size \(r\), together with (1.1), gives the claim. \(\square\)

## 2. The planted transition

Fix an indexed family on \(X\) and a number \(0<\rho<1\). Given a set \(W\subseteq X\), the *transition* is the following random experiment.

1. Draw a *source* \(c\sim\nu\), and put \(Y=W\cup A_c\).
2. Draw a *target* \(b\in B\) with conditional probabilities
\[
\pi_Y(b)=\frac{\nu_b\,\rho^{-|A_b|}\,\mathbf 1\{A_b\subseteq Y\}}{Z(Y)},\qquad Z(Y)=\sum_{d\in B}\nu_d\,\rho^{-|A_d|}\,\mathbf 1\{A_d\subseteq Y\}.\tag{2.1}
\]
3. Record the *fragment* \(T=A_b\setminus W\).

The normalization is positive, since \(A_c\subseteq Y\) gives \(Z(Y)\ge\nu_c\rho^{-|A_c|}>0\).

**Lemma 2.1.** For every \(W\) and every source and target that occur with positive probability:

1. \(T\subseteq A_c\cap A_b\) and \(A_b\subseteq W\cup T\);
2. the probabilities of the source–target pairs, the value of \(Z(Y)\), and the fragments \(A_b\setminus W\) depend on \(W\) only through \(W\cap\bigcup_{d\in B}A_d\).

**Proof.** (1) A target satisfies \(A_b\subseteq Y=W\cup A_c\), so \(T=A_b\setminus W\subseteq A_c\); and \(T\subseteq A_b\subseteq W\cup T\). (2) The indicator \(\mathbf 1\{A_d\subseteq W\cup A_c\}\) depends only on \(W\cap A_d\), and \(A_b\setminus W\) only on \(W\cap A_b\). \(\square\)

The first inclusion keeps fragments spread: a fragment lies inside the source, and the source has law \(\nu\) whatever \(W\) is. The second inclusion recovers the target from \(W\) and the fragment.

The posterior interpretation of (2.1) appears when \(W\) is random. Let \(W\sim\mu_\rho\) be independent of the source. Then \(Y\) is a random set in which a member of the family has been *planted*, and the target is a fresh sample of the planted index given \(Y\):

**Lemma 2.2** (planting). Let \(W\sim\mu_\rho\) be independent of \(c\sim\nu\), and \(Y=W\cup A_c\). For all \(y\subseteq X\) and \(d\in B\),
\[
\mathbb P(c=d,\ Y=y)=\nu_d\,\rho^{-|A_d|}\,\mathbf 1\{A_d\subseteq y\}\,\mu_\rho(y),\qquad\mathbb P(Y=y)=Z(y)\,\mu_\rho(y).\tag{2.2}
\]
Hence the conditional law of the source given \(Y=y\) is \(\pi_y\), and, given \(Y\), the source and the target are independent with this common law. Moreover \(\mathbb P(Z(Y)<\theta)\le\theta\) for every \(\theta>0\).

**Proof.** For fixed \(d\), the equality \(W\cup A_d=y\) holds exactly when \(A_d\subseteq y\) and \(W\setminus A_d=y\setminus A_d\), while \(W\cap A_d\) is arbitrary. So its probability is \(\rho^{|y|-|A_d|}(1-\rho)^{|X\setminus y|}=\rho^{-|A_d|}\mu_\rho(y)\) when \(A_d\subseteq y\), and \(0\) otherwise. Multiplying by \(\nu_d\) and summing over \(d\) gives (2.2). Dividing, the conditional law of \(c\) given \(Y=y\) is \(\pi_y\); the target is drawn from \(\pi_Y\) independently of \(c\) given \(Y\). Finally \(\mathbb P(Z(Y)<\theta)=\sum_y\mu_\rho(y)Z(y)\mathbf 1\{Z(y)<\theta\}\le\theta\). \(\square\)

For a fixed set \(W\), only the source is guaranteed to have law \(\nu\); the target can have a different law (Exercise 4.4).

## 3. Local resampling

**Theorem 3.1** (local resampling; OpenAI). Let the indexed family be \(a\)-spread, let \(m\) be a positive integer with \(|A_b|\le m\) for every \(b\in B\), and let \(0<\rho<1\) with \(a\le\mathrm e^{-50}\rho\). Let \(W\sim\mu_\rho\) be independent of the source, and run the transition. The outcome is a *local failure* if \(Z(Y)<\mathrm e^{-10m}\) or \(|T|>m/2\). Then:

1. \(\mathbb P(\text{local failure})\le\mathrm e^{-9m}\);
2. for every \(b\in B\) and every function \(f\ge0\) of \(W\) that depends only on \(W\setminus A_b\),
\[
\mathbb E\bigl[\mathbf 1\{\text{target}=b,\ Z(Y)\ge\mathrm e^{-10m}\}\,f(W)\bigr]\le\mathrm e^{11m}\,\nu_b\,\mathbb Ef(W).
\]

Part 2 compares the event that the target is \(b\) with an event of probability \(\nu_b\) independent of the coordinates of \(W\) outside \(A_b\): up to the factor \(\mathrm e^{11m}\), conditioning on it does not distort those coordinates. In [Covering a probability tree](covering-a-probability-tree.md), \(f\) is computed from the part of a tree below the arc labelled \(A_b\).

**Proof.** Write \(\theta=\mathrm e^{-10m}\). On the event \(Z(Y)\ge\theta\), the target probability (2.1) is at most \(\theta^{-1}\nu_b\rho^{-|A_b|}\mathbf 1\{A_b\subseteq W\cup A_c\}\). For fixed \(c\) and \(b\), the condition \(A_b\subseteq W\cup A_c\) says \(A_b\setminus A_c\subseteq W\); this event depends only on \(W\cap A_b\) and has probability \(\rho^{|A_b\setminus A_c|}\). Note that \(\rho^{-|A_b|}\rho^{|A_b\setminus A_c|}=\rho^{-|A_b\cap A_c|}\).

(1) If the target \(b\) has \(|T|>m/2\), then \(|A_c\cap A_b|\ge|T|>m/2\) by Lemma 2.1(1). Hence
\[
\mathbb P\bigl(Z(Y)\ge\theta,\ |T|>\tfrac m2\bigr)\le\theta^{-1}\sum_{b,c}\nu_b\,\nu_c\,\rho^{-|A_b\cap A_c|}\,\mathbf 1\bigl\{|A_b\cap A_c|>\tfrac m2\bigr\}.
\]
For fixed \(b\), Lemma 1.3 bounds the sum over \(c\) by \(\sum_{r>m/2}\binom mr(a/\rho)^r\le2^m\mathrm e^{-25m}\), because \(a/\rho\le\mathrm e^{-50}\) and \(r>m/2\). Summing over \(b\) with the weights \(\nu_b\), and adding \(\mathbb P(Z(Y)<\theta)\le\theta\) from Lemma 2.2,
\[
\mathbb P(\text{local failure})\le\mathrm e^{-10m}+\mathrm e^{10m}\,2^m\,\mathrm e^{-25m}=\mathrm e^{-9m}\bigl(\mathrm e^{-m}+\mathrm e^{-(6-\log2)m}\bigr)\le\mathrm e^{-9m},
\]
since \(m\ge1\) and \(\mathrm e^{-1}+\mathrm e^{-(6-\log2)}<1\).

(2) The function \(f(W)\) depends only on \(W\setminus A_b\), and the event \(A_b\setminus A_c\subseteq W\) only on \(W\cap A_b\); under \(\mu_\rho\) they are independent. Hence
\[
\mathbb E\bigl[\mathbf 1\{\text{target}=b,\ Z(Y)\ge\theta\}f(W)\bigr]\le\theta^{-1}\nu_b\sum_c\nu_c\,\rho^{-|A_b|}\,\mathbb E\bigl[\mathbf 1\{A_b\setminus A_c\subseteq W\}f(W)\bigr]=\theta^{-1}\nu_b\,\mathbb Ef(W)\sum_c\nu_c\,\rho^{-|A_b\cap A_c|}.
\]
By Lemma 1.3 the last sum is at most \(\sum_{r=0}^m\binom mr(a/\rho)^r=(1+a/\rho)^m\le\mathrm e^m\). \(\square\)

## 4. Exercises

**Exercise 4.1** (easy). Show that an \(a\)-spread family satisfies \(\mathbb E|A_c|\le a|X|\). Deduce that if all labels have exactly \(k\) elements, then \(|X|\ge k/a\).

**Exercise 4.2** (easy). Let the family consist of a single label \(A\) with \(|A|=m\ge1\). Describe the transition, show that \(Z(Y)=\rho^{-m}\), and show that \(|T|\) has the binomial law with parameters \(m\) and \(1-\rho\). Which hypothesis of Theorem 3.1 fails?

**Exercise 4.3** (easy). In the proof of Theorem 3.1(2), where is the hypothesis on \(f\) used? Why does the event \(\{A_b\setminus A_c\subseteq W\}\) depend only on \(W\cap A_b\)?

**Exercise 4.4** (medium). Show that if \(W\sim\mu_\rho\), independent of the source, then the target has law \(\nu\). Show by an example that for a fixed set \(W\) the law of the target can differ from \(\nu\).

## 5. Solutions

**4.1.** \(\mathbb E|A_c|=\sum_{x\in X}\mathbb P(x\in A_c)\le a|X|\) by (1.1) with \(J=\{x\}\). If every label has \(k\) elements, \(k\le a|X|\).

**4.2.** The source and the target are always the single index, \(Y=W\cup A\), \(Z(Y)=\rho^{-m}\ge1\), and \(T=A\setminus W\) contains each element of \(A\) independently with probability \(1-\rho\). The family is \(a\)-spread only for \(a\ge1\), because \(J=A\) gives \(\mathbb P(A\subseteq A)=1\); so \(a\le\mathrm e^{-50}\rho\) fails. Indeed \(|T|>m/2\) has probability close to \(1\) when \(\rho\) is small.

**4.3.** It is used in the equality \(\mathbb E[\mathbf 1\{A_b\setminus A_c\subseteq W\}f(W)]=\rho^{|A_b\setminus A_c|}\,\mathbb Ef(W)\), which needs independence of the two factors. The event involves only the elements of \(A_b\setminus A_c\subseteq A_b\).

**4.4.** By Lemma 2.2, given \(Y\) the target has the same conditional law as the source; averaging over \(Y\), it has the law of the source, which is \(\nu\). For a fixed \(W\), let \(X=\{1,2\}\), \(A_1=\{1\}\), \(A_2=\{2\}\), \(\nu_1=\nu_2=\frac12\) and \(W=\{1\}\). If the source is \(1\), then \(Y=\{1\}\) and the target is \(1\). If the source is \(2\), then \(Y=\{1,2\}\), \(Z(Y)=\rho^{-1}\), and the target is \(1\) or \(2\) with probability \(\frac12\) each. So the target is \(1\) with probability \(\frac34\).

## References

- [OpenAI-KK2] OpenAI, *The second Kahn–Kalai conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026
- [MNSZ-2] E. Mossel, J. Niles-Weed, N. Sun and I. Zadik, *A second moment proof of the spread lemma*, 2022; published as *A Bayesian proof of the spread lemma*, Random Structures & Algorithms 66 (2025). https://arxiv.org/abs/2209.11347
