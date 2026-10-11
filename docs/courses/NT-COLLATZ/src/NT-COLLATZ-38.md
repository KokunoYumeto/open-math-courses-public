# Finite survival and changes of probability weights

*Written by GPT-6 Astra (OpenAI), Ultra mode in Codex, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A path may finish above a boundary even though it crossed below that boundary much earlier. Estimating its endpoint therefore answers a different question from estimating its survival. The difference becomes useful when a rare event must be followed through an entire trajectory.

This lesson develops three tools for that purpose. Finite stopped moments bound the chance that a centered walk stays above a barrier. A point-probability estimate measures how much mass can fit into a narrow endpoint interval. An exact change of word weights then turns a walk with negative drift into a centered one. Combining the tools gives a survival bound with a factor \(m^{-3/2}\): one square-root saving from each end of the path and one from its middle.

The Collatz application concerns the logarithms of finite products of the multipliers \(1/2\) and \(3/2\). It supplies a probabilistic input to first-passage counting, not an assertion that successive Collatz landings are independent. A second change of weights gives both upper and lower bounds for unusually large multiplier products, explaining the reciprocal-height term that accompanies descent estimates.

Prerequisites are finite probability, elementary calculus and the [point-probability and Fourier arguments](NT-COLLATZ-07.md#a-point-probability-is-an-integral). [Maximal parity deviations and orbit envelopes](NT-COLLATZ-35.md) explains the separate exact connection between parity words and sampled integers. A basic reference for the finite survival and three-block construction is Idris Ali Shaik's *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, version 4.0.2, complete companion Appendix B. The proofs below give the finite calculations in full.

## Stopping without an infinite process

Let \(\mathcal A\) be a finite alphabet with weights \(q(a)\ge0\) and \(\sum_aq(a)=1\). A word \((a_1,\ldots,a_n)\in\mathcal A^n\) has weight \(\prod_iq(a_i)\). For a function \(x:\mathcal A\to\mathbb R\), put
\[
 X_i=x(a_i),\qquad S_j=\sum_{i=1}^jX_i,\qquad S_0=0.
 \tag{1}
\]
All expectations below are finite sums with these weights. Independence is the factorization of the product weights across disjoint sets of positions.

Suppose
\[
 \mathbb E X_i=0,\qquad |X_i|\le L,\qquad
 \mathbb E X_i^2=v>0,
 \tag{2}
\]
where \(L>0\). A stopping time \(\tau\in\{0,\ldots,n\}\) means that the decision whether \(\tau\ge j\) uses only the first \(j-1\) letters.

**Lemma 1.** For every such stopping time,
\[
 \mathbb E S_\tau=0,\qquad
 \mathbb E S_\tau^2=v\,\mathbb E\tau.
 \tag{3}
\]

**Proof.** Set \(A_j=\mathbf1_{\{\tau\ge j\}}\). Then
\(S_\tau=\sum_{j=1}^nA_jX_j\).
Fixing the first \(j-1\) letters fixes \(A_j\), while summing over the next letter gives mean zero. Thus every term in the first expectation vanishes.

For \(i<j\), \(A_iA_jX_i\) is determined by the first \(j-1\) letters. Summing \(A_iA_jX_iX_j\) over the \(j\)-th letter again gives zero. The diagonal term has expectation \(v\mathbb E A_j\), since \(A_j^2=A_j\). Expanding the square and summing gives
\[
 \mathbb E S_\tau^2
 =v\sum_{j=1}^n\mathbb P(\tau\ge j)
 =v\,\mathbb E\tau.
\]
The last equality follows pointwise from
\(\tau=\sum_{j=1}^n\mathbf1_{\{\tau\ge j\}}\). ∎

The result uses a stopping rule, not an arbitrary choice of a favorable time after seeing the whole word. The dependence on past letters is exactly what makes the cross terms vanish.

## A survival bound with its variance visible

For \(h\ge0\), define
\[
 E_n(h)=\{S_j\ge-h\text{ for all }0\le j\le n\}.
\]
The step bound \(L\) controls how far the walk can overshoot a boundary.

**Theorem 2.** Under (2), for every \(n\ge1\), \(h\ge0\), and auxiliary height \(H>0\),
\[
 \mathbb P(E_n(h))
 \le \frac{h+L}{H+h+L}
      +\frac{(h+L)(H+L)}{vn}.
 \tag{4}
\]
In particular,
\[
 \mathbb P(E_n(h))
 \le \min\left\{1,\frac{2(h+L)}{\sqrt{vn}}\right\}.
 \tag{5}
\]

**Proof.** Stop at the first exit through \(S_j<-h\) or \(S_j\ge H\), or at \(n\) if neither occurs earlier. Let \(Y=S_\tau\) and \(a=h+L\). Bounded overshoot gives
\[
 -a\le Y\le H+L.
\]
The nonnegative quantity \((Y+a)(H+L-Y)\), together with (3), gives
\[
 0\le\mathbb E[(Y+a)(H+L-Y)]
 =a(H+L)-v\mathbb E\tau.
 \tag{6}
\]
Thus \(\mathbb E\tau\le a(H+L)/v\).

Let \(U=\{Y\ge H\}\). Since \(Y\ge H\) on \(U\), \(Y\ge-a\) elsewhere and \(\mathbb EY=0\),
\[
 \mathbb P(U)\le\frac a{H+a}.
\]
A surviving word either reaches the upper boundary or has \(\tau=n\). Also \(n\mathbf1_{\{\tau=n\}}\le\tau\). Therefore
\[
 \mathbb P(E_n(h))
 \le \mathbb P(U)+\mathbb P(\tau=n)
 \le\frac a{H+a}+\frac{\mathbb E\tau}{n},
\]
which proves (4).

If \(\sqrt{vn}\le a\), the bound by one already implies (5). Otherwise choose \(H=\sqrt{vn}-a>0\) in (4). Direct substitution gives
\[
 \mathbb P(E_n(h))
 \le\frac{2a}{\sqrt{vn}}-\frac{ah}{vn}
 \le\frac{2a}{\sqrt{vn}}.
 \tag{7}
\]
Combining this with the bound by one proves (5). ∎

The choice of \(H\) balances the upper-exit probability against the chance of remaining in the strip for all \(n\) steps. No change of the original coordinates or step sizes was needed. Shaik's choice \(L=1\), \(H=\sqrt n\) gives the explicit bound in his centered-survival lemma directly from (4). Retaining the free auxiliary height also gives (5). Neither estimate asserts a sharp survival constant.

## How much mass fits in one endpoint interval

A survival estimate controls a path event. We also need a bound on the mass at any one endpoint.

**Lemma 3.** If \(K\) has the \(\operatorname{Bin}(n,p)\) law, where \(n\ge1\) and \(0<p<1\), then
\[
 \sup_{k\in\mathbb Z}\mathbb P(K=k)
 \le \frac{C_p}{\sqrt n},
 \qquad C_p=\frac3{\sqrt{8p(1-p)}}.
 \tag{8}
\]
Consequently, if \(d>0\), a half-open interval of length at most \(d\) contains at most one possible value of \(dK+c\), and its probability is bounded by (8).

**Proof.** In the frequency coordinate \(t\in[-1/2,1/2]\), the characteristic function of a Bernoulli variable is
\(\phi(t)=1-p+pe^{2\pi it}\).
Finite expansion and integration of \(e^{2\pi ijt}\) give
\[
 \mathbb P(K=k)
 =\int_{-1/2}^{1/2}\phi(t)^n e^{-2\pi ikt}\,dt.
\]
This is the one-dimensional inversion formula from the preceding local-probability lesson, with frequency \(2\pi t\). Exactly,
\[
 |\phi(t)|^2=1-4p(1-p)\sin^2(\pi t).
\]
Concavity of sine on \([0,\pi/2]\) gives
\(\sin(\pi|t|)\ge2|t|\).
Using \(1-u\le e^{-u}\) and taking square roots yields
\[
 |\phi(t)|^n\le e^{-8np(1-p)t^2}.
\]
The triangle inequality and the substitution
\(u=\sqrt{8np(1-p)}\,t\) now bound the point mass by
\[
 \frac1{\sqrt{8np(1-p)}}\int_{\mathbb R}e^{-u^2}\,du.
\]
The integral is less than three: its part on \([-1,1]\) is at most two, and
\[
 2\int_1^\infty e^{-u^2}\,du
 \le2\int_1^\infty u e^{-u^2}\,du=e^{-1}<1.
\]
This proves (8). Distinct values of \(dK+c\) differ by at least \(d\), proving the last assertion, including a half-open interval of length exactly \(d\). ∎

This Fourier proof makes the constant explicit and avoids a factorial approximation. Its \(n^{-1/2}\) factor has the same origin as the dimension factor in [Local probabilities for lattice sums](NT-COLLATZ-07.md#the-dimension-factor-comes-from-integration): the contributing frequency interval narrows like \(n^{-1/2}\).

## Changing the weights without changing the words

Let \(r(a)>0\) be probabilities on a finite alphabet, and choose a real parameter \(\theta\). Define
\[
 M(\theta)=\sum_a r(a)e^{\theta x(a)},\qquad
 q_\theta(a)=\frac{r(a)e^{\theta x(a)}}{M(\theta)}.
\]
The denominator is positive and the new weights sum to one. For every word with increment sum \(S_m\),
\[
 \prod_{i=1}^m r(a_i)
 =M(\theta)^m e^{-\theta S_m}
   \prod_{i=1}^m q_\theta(a_i).
 \tag{9}
\]
This follows simply by multiplying the defining identity for each letter. Summing it over any specified set of words gives the corresponding exact event identity. The words, their order and all their partial sums remain unchanged; only their weights change.

For the application, let a bit \(b\in\{0,1\}\) contribute
\[
 x(b)=b\log3-\log2.
\]
For a word \((b_1,\ldots,b_m)\) of length \(m\), put
\[
 s_j=\sum_{i=1}^j b_i,\qquad
 Z_j=s_j\log3-j\log2.
 \tag{10}
\]
Under fair bits, the mean increment is
\(\tfrac12\log3-\log2=-\tfrac12\log(4/3)<0\).
Choose instead
\[
 p=\frac{\log2}{\log3},\qquad
 \mathbb P_p(b=1)=p,\quad \mathbb P_p(b=0)=1-p.
\]
Then the mean increment is zero, and its variance is
\[
 v=p(1-p)(\log3)^2
   =\log2\,\log(3/2)>0.
 \tag{11}
\]
The negative increments, in reversed order, are also independent centered increments with the same variance and absolute value less than one.

Here \(1/2<p<1\), since \(2<3<4\). Put
\[
 \kappa=1-H_2(p)>0,\qquad
 \theta=\frac{\log(p/(1-p))}{\log3}>0,
 \tag{12}
\]
where \(H_2(p)=-p\log_2p-(1-p)\log_2(1-p)\).
To check \(\kappa>0\), differentiate \(H_2\): its derivative vanishes only at \(1/2\), and its second derivative is negative. Its unique maximum is \(H_2(1/2)=1\).

For every individual word,
\[
 \frac{2^{-m}}{p^{s_m}(1-p)^{m-s_m}}
 =2^{-\kappa m}e^{-\theta Z_m}.
 \tag{13}
\]
Indeed the logarithm of the left side is
\[
 -m\log2-m\{p\log p+(1-p)\log(1-p)\}
 -(s_m-mp)\log\frac p{1-p}.
\]
Use \(Z_m=(s_m-mp)\log3\) to obtain (13).

Equation (13) isolates two different costs. The exponential factor \(2^{-\kappa m}\) is independent of the endpoint. The factor \(e^{-\theta Z_m}\) varies with the endpoint and must remain inside the weighted sum until that endpoint has been controlled.

## Three blocks give three square root factors

Fix \(B>0\), and let
\[
 W_m(B)=\{b\in\{0,1\}^m: Z_j>-B
                   \text{ for every }0\le j\le m\}.
\]
The strict inequality is part of the event.

**Theorem 4.** For every \(m\ge1\),
\[
 2^{-m}|W_m(B)|
 \le C_B m^{-3/2}2^{-\kappa m}.
 \tag{14}
\]
One possible explicit constant is
\[
 \begin{split}
 w&=e^{-\theta},\\
 C_B&=\max\left\{
 8^{3/2}2^{8\kappa},\
 \frac{32\sqrt2\,C_p}{v}(B+1)e^{\theta B}
           \frac{2-w}{(1-w)^2}\right\}.
 \end{split}
 \tag{15}
\]
In particular the constant is uniform for \(B\) in any bounded positive interval.

**Proof.** First suppose \(m\ge8\). Set
\[
 a=\lfloor m/4\rfloor,\qquad b=m-2a.
\]
Splitting a word into its first \(a\), next \(b\), and last \(a\) bits is an exact bijection
\[
 \{0,1\}^m
 \longleftrightarrow
 \{0,1\}^a\times\{0,1\}^b\times\{0,1\}^a.
 \tag{16}
\]
Its inverse concatenates the three words. The product weight also factors exactly across this bijection.

Partition the terminal values of surviving words into bins
\[
 Z_m+B\in[q,q+1),\qquad q=0,1,2,\ldots.
\]
Every word in \(W_m(B)\) belongs to exactly one bin. In bin \(q\), two conditions are necessary:

- The first block has every partial sum greater than \(-B\).
- Reading the last block backwards and negating its increments gives partial sums
  \[
    Z_{m-j}-Z_m>-(q+1)\qquad(0\le j\le a).
    \tag{17}
  \]

For the second condition, use \(Z_{m-j}>-B\) and \(Z_m<q+1-B\). Reversing the order preserves the product law. Negating the numerical increments preserves centering and variance; it does not exchange the probabilities of zero and one.

The two necessary conditions involve disjoint blocks. Applying (5) with \(L=1\) gives a product bound
\[
 \frac{4(B+1)(q+2)}{va}.
 \tag{18}
\]
This remains an upper bound when a displayed factor is greater than one.

Now fix both outer words. The middle sum has the form
\(K\log3-b\log2\), with \(K\sim\operatorname{Bin}(b,p)\). The endpoint bin restricts that sum to a half-open interval of length one, independently of its location. Since \(\log3>1\), it contains at most one atom. For completeness, \(e<3\) follows from the exponential series and \(j!\ge2^{j-1}\) for \(j\ge2\), with strict inequality from \(j=3\) onward. Thus Lemma 3 bounds the conditional bin probability by \(C_p/\sqrt b\).

Sum this bound over the pairs of outer words satisfying their necessary conditions. Equations (16)–(18) give
\[
 \mathbb P_p(W_m(B),\,Z_m+B\in[q,q+1))
 \le \frac{4C_p(B+1)(q+2)}{v\,a\sqrt b}.
 \tag{19}
\]
We have not asserted independence between survival of the whole path and its terminal bin. The only multiplied probabilities in (18) belong to the two disjoint outer blocks; the middle estimate is uniform after conditioning on both.

Since \(a\ge m/8\) and \(b\ge m/2\), (19) is at most
\[
 \frac{32\sqrt2\,C_p}{v}(B+1)(q+2)m^{-3/2}.
\]
On bin \(q\), \(e^{-\theta Z_m}\le e^{\theta B}e^{-\theta q}\). Apply (13) word by word and sum over all bins. The elementary geometric identity
\[
 \sum_{q=0}^\infty(q+2)w^q=\frac{2-w}{(1-w)^2},
 \qquad 0<w<1,
 \tag{20}
\]
then proves (14) with the second constant in (15). To derive (20), expand
\[
 (1-w)^{-2}=(\sum_{i\ge0}w^i)(\sum_{j\ge0}w^j)
 =\sum_{q\ge0}(q+1)w^q,
\]
and add \((1-w)^{-1}\).
All terms are nonnegative, so the regrouping is justified by increasing finite sums.

For \(1\le m<8\), the left side of (14) is at most one. The first constant in (15) is at least \(m^{3/2}2^{\kappa m}\), covering these finitely many lengths. The displayed expression increases with \(B\), so the same constant chosen at \(B_0\) works for \(0<B\le B_0\). ∎

![A word is split into outer blocks of length a and a middle block of length b. Survival of the first block and reversed survival of the last block each supply a factor a to the power minus one half. Conditional on both outer blocks, one middle endpoint atom supplies b to the power minus one half.](../figures/three-block-survival.svg)

*Figure 1. The exact split and the three estimates in (19). Only the two outer survival conditions are multiplied as independent events. The middle bound is applied after both outer words are fixed. The word and all of its original coordinates are retained.*

The exponential decay alone could be found by a terminal large-deviation estimate. It does not supply the two additional survival factors. Equation (19) explains why retaining the whole path gives a stronger polynomial prefactor, which can matter when an exponential estimate is evaluated at a critical logarithmic scale.

## Large multiplier products and a second change of weights

The same word coordinates also describe
\[
 F_j=\frac{3^{s_j}}{2^j}=e^{Z_j},\qquad F_0=1.
\]
The fair mean of the next multiplier is \((1/2+3/2)/2=1\).

**Proposition 5.** For every word length \(m\ge1\) and \(u>0\),
\[
 \mathbb P_{1/2}\{\max_{0\le j\le m}F_j>u\}\le\frac1u.
 \tag{21}
\]

**Proof.** If \(u<1\), the bound follows from probability at most one. Otherwise stop at the first crossing of \(u\), or at \(m\) if there is none. At every nonstopped vertex of the finite word tree, the average of its two successor values equals its value. Replacing the terminal pair by that value, successively backwards through the tree, proves \(\mathbb E_{1/2}F_\tau=F_0=1\). The value is nonnegative and is greater than \(u\) on the crossing event. Thus \(u\mathbb P(\text{crossing})\le1\). ∎

There is also a lower bound of the same reciprocal order. It makes use of the exact overshoot at a crossing.

**Proposition 6.** Put
\[
 \varepsilon_0=\frac{3/4-p}{2}>0,\qquad
 K_{\max}=\frac3{16\varepsilon_0^2}.
\]
If \(u\ge1\), \(m\ge1\), and
\(\log u\le\varepsilon_0m\log3\), then
\[
 \frac{2}{3u}\left(1-\frac{K_{\max}}m\right)
 \le\mathbb P_{1/2}\{\max_{0\le j\le m}F_j>u\}
 \le\frac1u.
 \tag{22}
\]
A negative lower bound makes no assertion beyond nonnegativity.

**Proof.** First \(p<3/4\), because \(2^4<3^3\); hence \(\varepsilon_0>0\). Write \(A\) for the crossing event and use the stopped mean from Proposition 5. Only the multiplier \(3/2\) can cross upwards. At a crossing,
\(u<F_\tau\le3u/2\); off \(A\), \(F_\tau=F_m\). Consequently
\[
 1\le\frac32u\,\mathbb P_{1/2}(A)
       +\mathbb E_{1/2}[F_m\mathbf1_{A^c}].
\]
For every word the exact identity
\[
 2^{-m}F_m=(3/4)^{s_m}(1/4)^{m-s_m}
 \tag{23}
\]
turns the final expectation into \(\mathbb P_{3/4}(A^c)\).
The event \(A^c\) implies \(F_m\le u\). Under the \(3/4\) law, \(s_m\) has mean \(3m/4\) and variance \(3m/16\): these follow by adding the means and variances of independent Bernoulli letters. The hypothesis on \(u\) gives
\[
 F_m\le u
 \ \Longrightarrow\
 s_m\le pm+\frac{\log u}{\log3}
 \le(3/4-\varepsilon_0)m.
\]
Applying the elementary inequality
\(\mathbb P(|V-\mathbb EV|\ge t)\le\mathbb E(V-\mathbb EV)^2/t^2\)
therefore bounds this event by \(K_{\max}/m\). This inequality follows by averaging
\(t^2\mathbf1_{\{|V-\mathbb EV|\ge t\}}\le(V-\mathbb EV)^2\).
Rearranging the stopped-mean bound proves the lower estimate; (21) supplies the upper one. ∎

The two changes of weights serve different purposes. The parameter \(p=\log_3 2\) centers the logarithmic increments, making finite survival accessible. The parameter \(3/4\) absorbs the multiplier \(F_m\) into a probability weight, making the terminal remainder in a stopped-mean identity small. Neither changes the underlying words or their crossing event.

## Exercises with solutions

### Endpoint information is not survival information

For four fair increments in \(\{-1,1\}\), calculate the probability that the endpoint is nonnegative and the probability that every partial sum is nonnegative.

**Solution.** A nonnegative endpoint requires at least two positive increments. Its probability is
\((\binom42+\binom43+\binom44)/16=11/16\).
The six surviving words are
\(++++\), \(+++-\), \(++-+\), \(++--\), \(+-++\), and \(+-+-\).
Thus survival has probability \(6/16=3/8\). In particular, the endpoint event includes paths that were already below the boundary. Bounding the former does not recover the information retained by the latter.

### A walk with unequal step sizes

A letter is \(-1\) with probability \(2/3\) and \(2\) with probability \(1/3\). Verify the hypotheses of Theorem 2 and bound survival above zero for one hundred steps, without changing the step coordinates.

**Solution.** The mean is \(-2/3+2/3=0\), the second moment is \(2/3+4/3=2\), and \(|X|\le L=2\). Hence \(v=2\), \(h=0\), \(n=100\). Equation (5) gives
\[
 \mathbb P(E_{100}(0))\le\frac4{\sqrt{200}}=\frac{\sqrt2}{5}.
\]
The auxiliary height used in the proof is \(\sqrt{200}-2>0\). The bound is a consequence of the general stopped-moment calculation, not a numerical estimate of the survival probability.

### The same endpoint can hide different histories

Give bits weight \(p=2/3\) and compare the three words \(110,101,011\) with fair bits. Find their individual fair-to-biased likelihood ratio. For the multiplier path \(F_j=3^{s_j}/2^j\), which of these words stays strictly above \(3/4\) at every time?

**Solution.** Each word has biased weight \(p^2(1-p)=4/27\) and fair weight \(1/8\), so the likelihood ratio is \(27/32\) in all three cases. All end at \(F_3=9/8\).

The path for \(110\) is \(1,3/2,9/4,9/8\), which stays above \(3/4\). The path for \(101\) is \(1,3/2,3/4,9/8\), so it fails the strict condition at time two. The path for \(011\) begins \(1,1/2\), so it also fails. A likelihood ratio determined by the endpoint does not make the survival event an endpoint event. The strict boundary matters even in this three-letter example.

### A stopped mean and its terminal remainder

For three fair bits, let \(A\) be the event \(\max_{j\le3}F_j>3/2\). Compute its probability and verify the stopped-mean decomposition and the change of weights (23).

**Solution.** Precisely the words \(110\) and \(111\) cross, both at time two with value \(9/4\). Thus \(\mathbb P_{1/2}(A)=1/4\), and their contribution to the stopped mean is \(9/16\).

On the other six words, the terminal values have total
\[
 \frac18+\frac38+\frac38+\frac98+\frac38+\frac98
 =\frac72.
\]
Their fair-weighted contribution is \(7/16\). The total stopped mean is therefore \(9/16+7/16=1\). Under the \(3/4\) law, \(A\) means that the first two bits are one, so \(\mathbb P_{3/4}(A^c)=1-(3/4)^2=7/16\), exactly the terminal remainder. This finite identity explains why the second change of weights is useful.

## From word estimates to orbit estimates

The survival theorem concerns a completely specified set of finite words. To use it for Collatz integers, one must still prove that a failing integer trajectory has a word in that set and apply the exact parity-counting map. Later descents require first-passage transport on the original integers; the centered product law is not a replacement distribution for the landing values.

What is now available is a complete quantitative input: the \(m^{-3/2}2^{-\kappa m}\) bound retains both survival constraints and the terminal weight, while (21)–(23) control large multiplicative excursions. These mechanisms belong to finite random walks, stopping and changes of measure well beyond this particular dynamical system.

## References

- Idris Ali Shaik, *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, version 4.0.2, 4 October 2026. [Article and complete mathematical companion](https://doi.org/10.5281/zenodo.23132901), complete companion Appendix B. The centered stopped-moment, three-block survival and reciprocal-maximum constructions are credited here. The free auxiliary-height bound, its optimization, and the explicit Fourier atom constant are proved directly above. The independently expressed exposition does not reproduce the accompanying formal code.
- [Local probabilities for lattice sums](NT-COLLATZ-07.md), especially the inversion and dimension-factor arguments. This internal prerequisite supplies the general Fourier setting; the Bernoulli calculation required here is explicit.
