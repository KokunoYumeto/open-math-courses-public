# Retaining information through Fourier cancellation

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

An average can be small because two large contributions cancel. If a subsequent calculation keeps those contributions separate, the small average no longer answers its question. This happens when an arithmetic argument needs both a random affine offset and the total number of divisions by two. Averaging over the total too early can remove exactly the information needed to recover the starting integer.

We prove a way to retain that information. A nonnegative bound for a conditional Fourier average controls the sum of the absolute contributions at every possible value of an observed statistic. Applied to the paired geometric variables from the preceding lessons, it gives Fourier decay with the total valuation still visible. We then prove Allikvere's sum-conditioned Fourier estimate, using an elementary lower bound for the probability of a specified total. Finally, an exact convolution identity extends the argument to characters that see only a shorter initial block.

The general subjects are conditional probability, complex measures and harmonic analysis. The arithmetic application is one ingredient of the transition from Tao's logarithmic-density method to uniform-input first-passage arguments. Basic references are Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Section 7, and Allikvere's *Almost all Collatz orbits attain almost bounded values in natural density*, Theorem 3.1. The mechanism of paired cancellation is Tao's; its sum-conditioned application is Allikvere's. The joint-statistic formulation proved below makes the information retained by that argument explicit.

We use the [conditional pairing calculation](NT-COLLATZ-09.md#pairing-waiting-times-before-taking-absolute-values), the [occupation estimate](NT-COLLATZ-11.md#fourier-decay-for-random-affine-offsets), and elementary binomial coefficients. The preceding lessons provide the complete renewal argument underlying the occupation estimate. No local limit theorem is needed for the probability bound proved here.

## Why changing the sampling law needs more information

For a positive odd integer \(N\), write
\[
S(N)=\frac{3N+1}{2^{v_2(3N+1)}}.
\]
Along a word of \(r\) actual returns, let \(a_i\) be the successive positive valuations and put \(s_j=a_1+\cdots+a_j\), with \(s_0=0\). Repeated substitution gives
\[
S^r(N)=\frac{3^rN+b_r}{2^{s_r}},
\qquad b_r=\sum_{i=1}^r3^{r-i}2^{s_{i-1}}.
\tag{1}
\]
Indeed, the numerator satisfies \(b_{j+1}=3b_j+2^{s_j}\), starting at \(b_0=0\). Thus the endpoint \(M=S^r(N)\), together with the word, recovers
\[
N=\frac{2^{s_r}M-b_r}{3^r}.
\tag{2}
\]
The total \(s_r\) affects both the inverse scale and its integer congruence. An offset distribution in which this total has already been averaged away cannot by itself evaluate all inverse-fibre counts.

The difference between uniform and logarithmic sampling can be seen without dynamics. Fix \(\alpha>1\), let \(y\to\infty\), and choose \(h=h(y)\to\infty\) with \(h=o(\log y)\). Among odd integers in \([y,y^\alpha]\), consider those in the upper interval
\[
[y^\alpha e^{-h},y^\alpha].
\]
Its uniform probability tends to one: each odd-integer interval count differs from half its length by at most two, and the ratio of the lengths tends to one. Its logarithmic probability tends to zero. To see this, the integral comparison for the decreasing function \(1/t\) along the odd progression gives
\[
\sum_{\substack{a\leq n\leq b\\n\text{ odd}}}\frac1n
=\frac12\log(b/a)+O(1/a).
\]
Apply this first to the upper interval and then to the whole interval. Their ratio is
\[
\frac{h}{(\alpha-1)\log y}+o(1)=o(1).
\]
The lower endpoint of the upper interval exceeds \(y\) eventually because \(h=o(\log y)\). Consequently, an event negligible for one of these sampling laws can have almost full mass for the other. The required change of sampling must be proved within the arithmetic formula, not inferred by renaming its density.

## Cancellation before and after an observation

Work on a countable probability space. Let \(Y\) be a complex random variable with \(|Y|\leq1\), and let \(R\) be a countable-valued observation. For \(\mathbb P(R=r)>0\), define
\[
m(r)=\frac{\mathbb E[Y\mathbf1_{R=r}]}{\mathbb P(R=r)}.
\]
This is the conditional average of \(Y\) on that fibre. Suppose a nonnegative function \(Z=z(R)\) satisfies \(|m(R)|\leq Z\) and \(\mathbb EZ<\infty\). A statistic \(T=t(R)\) can be read from \(R\); it may discard some of its information.

**Theorem 1 (Retaining an observed statistic).** For every bounded complex function \(H=h(R)\),
\[
|\mathbb E(HY)|\leq\mathbb E(|H|Z).
\tag{3}
\]
For the complex masses
\(\nu(t)=\mathbb E[Y\mathbf1_{T=t}]\), one has
\[
\sum_t|\nu(t)|\leq\mathbb EZ.
\tag{4}
\]
In particular, whenever \(\mathbb P(T=t)>0\),
\[
|\mathbb E(Y\mid T=t)|
\leq\frac{\mathbb E[Z\mathbf1_{T=t}]}{\mathbb P(T=t)}.
\tag{5}
\]

**Proof.** Regroup the absolutely convergent expectation by the values of \(R\):
\[
\mathbb E(HY)=\sum_r h(r)m(r)\mathbb P(R=r).
\]
Its absolute value is at most \(\sum_r|h(r)|z(r)\mathbb P(R=r)\), proving (3). Apply (3) with \(H=\mathbf1_{T=t}\). Summing the resulting inequalities over the disjoint fibres of \(T\) gives (4), since a sum of nonnegative terms may be regrouped by its fibres. Division by the positive fibre mass proves (5). ∎

There is no factor equal to the number of possible values of \(T\), even if this number is infinite. The same single random variable \(Z\) bounds all the fibres, and each outcome contributes to exactly one of them.

The norm in (4) describes exactly what can happen when one reweights the retained statistic:
\[
\sum_t|\nu(t)|
=\sup_{|u(t)|\leq1}|\mathbb E[u(T)Y]|.
\tag{6}
\]
The triangle inequality proves the upper bound. For equality choose \(u(t)=\overline{\nu(t)}/|\nu(t)|\) when \(\nu(t)\ne0\), and zero otherwise. Absolute convergence follows from \(\sum_t|\nu(t)|\leq\mathbb E|Y|\leq1\). Thus this statistic-dependent choice is permitted and makes each nonzero summand positive real.

By contrast, \(|\mathbb EY|\) corresponds only to \(u=1\). For a fair sign \(Y\in\{-1,1\}\), take \(T=R=Y\). Then \(\mathbb EY=0\), but both conditional averages have modulus one and \(\sum_t|\nu(t)|=1\). The observation has exposed cancellation that the unconditional expectation concealed.

## A retained total in the affine offset model

Let \(A_1,\ldots,A_n\) be independent, with
\(\mathbb P(A_i=a)=2^{-a}\) for positive integers \(a\). Put
\[
S_i=A_1+\cdots+A_i,
\qquad X_n=\sum_{i=1}^n3^{i-1}2^{-S_i}.
\tag{7}
\]
Here \(X_n\) is a rational number whose denominator is a power of two. Its reduction modulo \(3^n\) uses the inverse of two in \(\mathbb Z/3^n\mathbb Z\), as constructed in the [character lesson](NT-COLLATZ-09.md#characters-on-fractions-with-powers-of-two-as-denominators). For \(3\nmid\xi\), write
\[
\chi_{n,\xi}(x)
=\exp\left(-\frac{2\pi i\xi(x\bmod3^n)}{3^n}\right).
\]

The forward offset in (1) is \(2^{-s_r}b_r\). Reversing a word turns it into (7): if \(c_j=a_{r-j+1}\), then
\[
\sum_{j=1}^r3^{j-1}2^{-(c_1+\cdots+c_j)}
=\sum_{i=1}^r3^{r-i}2^{s_{i-1}-s_r}.
\]
Reversal is an involution and preserves the total and the word's probability \(2^{-s_r}\). It therefore identifies the **joint random laws** of offset and total in the two orientations, including after a total is specified. No reversal of an actual deterministic trajectory is asserted.

Let \(m=\lfloor n/2\rfloor\), \(B_j=A_{2j-1}+A_{2j}\), and \(U_j=B_1+\cdots+B_j\). The observation \(R\) consists of all \(B_j\) and, when \(n\) is odd, also the final variable \(A_n\). Both parities now make \(S_n\) a function of \(R\).

Given \(R\), the within-pair variables \(A_{2j}\) are independent, each uniform on \(1,\ldots,B_j-1\). Indeed, every split of a fixed pair sum has probability \(2^{-B_j}\), so division by \((B_j-1)2^{-B_j}\) makes its conditional probability \(1/(B_j-1)\). Multiplication over the independent original pairs gives the conditional product law. The odd leftover has already been fixed by the observation.

With \(c_j=3^{2j-2}2^{-U_j}\), direct grouping of (7) gives
\[
X_n=\sum_{j=1}^m c_j(2^{A_{2j}}+3)+V,
\tag{8}
\]
where \(V=0\) for even \(n\), and \(V=3^{n-1}2^{-U_m-A_n}\) for odd \(n\). Hence
\[
\mathbb E(\chi_{n,\xi}(X_n)\mid R)
=\chi_{n,\xi}(V)\prod_{j=1}^m
\frac1{B_j-1}\sum_{a=1}^{B_j-1}\chi_{n,\xi}(c_j(2^a+3)).
\tag{9}
\]
The factor \(\chi_{n,\xi}(V)\) has modulus one. In particular, the odd case does not average a supposedly independent leftover after conditioning on its total.

Use the fixed small \(\varepsilon>0\) from the [weighted renewal proof](NT-COLLATZ-11.md#fourier-decay-for-random-affine-offsets). Let \(\theta(j,l)\in(-1/2,1/2]\) satisfy
\[
e^{-2\pi i\theta(j,l)}
=\chi_{n,\xi}(3^{2j-2}2^{1-l}).
\]
When \(B_j=3\), its factor in (9) is the average of \(\chi_{n,\xi}(5c_j)\) and \(\chi_{n,\xi}(7c_j)\). Its modulus is
\(|\cos(\pi\theta(j,U_j))|\). The [cosine estimate](NT-COLLATZ-09.md#a-phase-that-measures-the-cancellation) bounds this by \(e^{-\varepsilon^3}\) if \(|\theta(j,U_j)|>\varepsilon\). All other factors have modulus at most one. Define
\[
J=\#\{j\leq m:B_j=3,\ |\theta(j,U_j)|>\varepsilon\},
\qquad Z_{n,\xi}=e^{-\varepsilon^3J}.
\tag{10}
\]
Then the modulus of (9) is at most \(Z_{n,\xi}\), a nonnegative function of the observation.

The occupation theorem proved in the preceding lessons supplies, for each \(D>0\),
\[
\mathbb EZ_{n,\xi}\leq C_D n^{-D},
\qquad 3\nmid\xi.
\tag{11}
\]
Here is the exact connection to that theorem. The marked-block identity in the [phase lesson](NT-COLLATZ-09.md#from-pair-indices-to-a-renewal-occupation-count) identifies \(J\) with the renewal count in a strip of width \(m\). Corollary 5 of [Weighted renewal estimates and Fourier decay](NT-COLLATZ-11.md#fourier-decay-for-random-affine-offsets), immediately preceding the linked section, bounds its exponential moment by a constant times \(m^{-D}\). The phase geometry and fixed right margin used there apply to every primitive \(\xi\) at the present modulus. Since \(m\geq n/3\) for \(n\geq2\), this yields (11); enlarge the constant for \(n=1\). Importantly, that proof bounds the positive expectation in (11), not merely the final unconditional Fourier coefficient.

**Theorem 2 (Fourier decay with the total retained).** For every \(D>0\),
\[
\sum_{s\geq n}
\left|\mathbb E\bigl[\chi_{n,\xi}(X_n)\mathbf1_{S_n=s}\bigr]\right|
\leq C_D n^{-D},\qquad 3\nmid\xi.
\tag{12}
\]
The same constant bounds
\(|\mathbb E[h(S_n)\chi_{n,\xi}(X_n)]|\) whenever \(|h(s)|\leq1\).

**Proof.** Apply Theorem 1 with \(Y=\chi_{n,\xi}(X_n)\), the observation just defined, \(T=S_n\), and the majorant (10). Equations (4), (6) and (11) give the conclusions. ∎

This is a joint estimate: the complex contribution of each total is kept separately before taking its absolute value. It is stronger information than cancellation after all totals have been combined. It is not yet a bound for the full distance between two spatial probability distributions; that further step must also handle the number and order of the Fourier characters.

## The probability cost of fixing the total

For \(s\geq n\), the number of positive \(n\)-tuples with sum \(s\) is \(\binom{s-1}{n-1}\): place \(n-1\) separators in the \(s-1\) spaces between \(s\) consecutive marks. Each tuple has probability \(2^{-s}\). Consequently
\[
p_n(s):=\mathbb P(S_n=s)=\binom{s-1}{n-1}2^{-s}.
\tag{13}
\]
Conditioning on a total makes its positive compositions uniformly distributed. Their coordinates are generally dependent because their sum is fixed.

**Lemma 3 (An elementary moderate-window lower bound).** For \(n\geq2\) and integers \(|d|\leq n/2\),
\[
p_n(2n+d)\geq
\frac1{2(2n+1)}
\exp\left(-\frac{d^2+3|d|}{n}\right).
\tag{14}
\]
In particular, for each fixed \(C>0\) and all sufficiently large \(n\),
\[
p_n(s)\geq\frac1{6e}n^{-1-C^2}
\quad\text{if }|s-2n|\leq C\sqrt{n\log n}.
\tag{15}
\]

**Proof.** The largest coefficient in \((1+1)^{2n}\) is \(\binom{2n}{n}\). This follows from the ratio of consecutive coefficients, \((2n-j)/(j+1)\), which crosses one at the centre. Since the \(2n+1\) coefficients sum to \(4^n\),
\[
p_n(2n)=\tfrac12\binom{2n}{n}4^{-n}
\geq\frac1{2(2n+1)}.
\]
The exact adjacent ratio is
\[
\frac{p_n(s+1)}{p_n(s)}=\frac{s}{2(s-n+1)}.
\tag{16}
\]
For \(d\geq0\), multiply (16) at \(s=2n+i\), \(0\leq i<d\). Each ratio is \(1-x_i\), where
\[
x_i=\frac{i+2}{2n+2i+2}\leq\frac12.
\]
For \(0\leq x\leq1/2\), integration of \(1/(1-t)\leq2\) gives \(\log(1-x)\geq-2x\). Hence
\[
\log\frac{p_n(2n+d)}{p_n(2n)}
\geq-\sum_{i=0}^{d-1}\frac{i+2}{n}
=-\frac{d^2+3d}{2n}.
\]
For \(d=-h<0\), use the reverse ratios
\[
\frac{p_n(2n-i-1)}{p_n(2n-i)}
=1-\frac{i-1}{2n-i-1},\qquad 0\leq i<h.
\]
The first ratio exceeds one and the second equals one. For the others, \(h\leq n/2\) makes the fraction lie in \([0,1/2]\) and its denominator at least \(n\). The same logarithm inequality gives a total loss at most
\(2\sum_{i=0}^{h-1}i/n=h(h-1)/n\). Both sides imply (14), including \(d=0\).

In the window of (15), eventually \(|d|\leq n/2\), and
\[
\frac{d^2+3|d|}{n}
\leq C^2\log n+3C\sqrt{\frac{\log n}{n}}
\leq C^2\log n+1.
\]
Also \(2(2n+1)\leq6n\). Substitution in (14) proves (15). ∎

The bound is designed to give a polynomial lower bound, not the sharp Gaussian shape. Allikvere obtains the sharper size \(n^{-1/2-C^2/4}\) by a local estimate. For preservation of arbitrary-power decay, either lower bound suffices. The elementary argument avoids needing that sharper asymptotic for this particular theorem; it does not replace local estimates in later kernel calculations.

**Theorem 4 (Allikvere's sum-conditioned Fourier decay).** Fix \(A,C>0\). There is a constant \(K_{A,C}\) such that, for every \(n\geq1\), every \(3\nmid\xi\), and every integer \(s\geq n\) with \(|s-2n|\leq C\sqrt{n\log n}\),
\[
\left|\mathbb E\bigl(\chi_{n,\xi}(X_n)\mid S_n=s\bigr)\right|
\leq K_{A,C}n^{-A}.
\tag{17}
\]

*Reference:* Allikvere, Theorem 3.1; Tao's positive-majorant estimate supplies its Fourier input.

**Proof.** A single term of (12) is at most \(C_Dn^{-D}\). Divide by (15). This gives at most \(6eC_Dn^{1+C^2-D}\) for all sufficiently large \(n\). Choose \(D=A+2+C^2\). For the finitely many smaller \(n\), every conditional character average is at most one; enlarge the constant to cover their values of \(n^A\). The constant is independent of \(s\) and \(\xi\). ∎

Not every possible total permits this conclusion. At \(s=n\), the only composition is \((1,\ldots,1)\), so the conditional offset is deterministic and every character average has modulus one. For large \(n\), this total lies outside the stated window. Its exact probability is \(2^{-n}\), too small to be paid for by an arbitrary fixed inverse power of \(n\).

For a small numerical example, take \(n=2,s=3\). The words \((1,2)\) and \((2,1)\) each have conditional probability \(1/2\); their offsets modulo nine are two and four. For \(\xi=1\), the conditional Fourier average is
\[
\tfrac12(e^{-4\pi i/9}+e^{-8\pi i/9}),
\]
with modulus \(|\cos(2\pi/9)|\). The total's probability is \(p_2(3)=1/4\), so the unnormalized contribution to (12) is one quarter of this average. Keeping that factor is essential when summing over totals.

## Shorter character orders and an independent tail

A nonzero character of \(\mathbb Z/3^n\mathbb Z\) has order \(3^k\) for a unique \(1\leq k\leq n\). Its index can be written \(\xi=3^{n-k}\eta\), with \(3\nmid\eta\). Terms of (7) with \(i>k\) vanish after reduction modulo \(3^k\); therefore, for each realised word,
\[
\chi_{n,\xi}(X_n)=\chi_{k,\eta}(X_k).
\tag{18}
\]
The total still includes the discarded coordinates. Define
\[
\nu_{n,k,\eta}(s)
=\mathbb E[\chi_{k,\eta}(X_k)\mathbf1_{S_n=s}].
\]
Use \(p_0(0)=1\), \(p_0(t)=0\) for \(t\ne0\), and set \(p_j(t)=0\) outside the support in (13).

**Proposition 5 (Convolution in the retained coordinate).** One has
\[
\nu_{n,k,\eta}(s)
=\sum_t\nu_{k,k,\eta}(t)p_{n-k}(s-t),
\tag{19}
\]
and, for every \(D>0\),
\[
\sum_s|\nu_{n,k,\eta}(s)|\leq C_D k^{-D}.
\tag{20}
\]

**Proof.** Before imposing \(S_n=s\), the initial \(k\) variables and the remaining \(n-k\) variables are independent. Split by \(S_k=t\). The tail total has law \(p_{n-k}\), proving (19) with its actual probability weights. Its total mass is one. The triangle inequality, followed by nonnegative regrouping, gives
\[
\sum_s|\nu_{n,k,\eta}(s)|
\leq\sum_t|\nu_{k,k,\eta}(t)|\sum_s p_{n-k}(s-t).
\]
The inner sum is one, and Theorem 2 at length \(k\) gives (20). The convention for \(p_0\) includes \(k=n\) without a separate limit. ∎

The independence used here precedes conditioning. It does not claim that the initial word and tail remain independent after their combined total is fixed. Formula (19) is the precise replacement for that false claim.

**Corollary 6 (Growing character orders under conditioning).** Fix \(A,C>0\) and \(0<\delta\leq1\). Uniformly for \(n^\delta\leq k\leq n\), \(3\nmid\eta\), and admissible \(s\) in the window of Theorem 4,
\[
\left|\mathbb E\bigl(\chi_{k,\eta}(X_k)\mid S_n=s\bigr)\right|
\leq K_{A,C,\delta}n^{-A}.
\tag{21}
\]

**Proof.** Divide the single-mass estimate from (20) by (15). Since \(k\geq n^\delta\), the result is at most \(6eC_D n^{1+C^2-\delta D}\). Take \(D=(A+2+C^2)/\delta\) and absorb the finitely many smaller \(n\) into the constant. ∎

This consequence is about a family of individual character averages, with its character-order threshold explicit. There are exponentially many characters at modulus \(3^n\). Summing their bounds without further structure would not give a useful probability-distance estimate. The [quotient Fourier estimate](NT-COLLATZ-05.md#what-a-quotient-observation-forgets) and arithmetic separation provide that additional structure; retaining the total through those steps is the next mathematical task.

## Exercises with solutions

### 1 A statistic that conceals half the cancellation

Let \(Y\) take the values \(1,i,-1,-i\), each with probability \(1/4\). Define \(T=0\) on the first two values and \(T=1\) on the last two. Compute the unconditional expectation, the two complex masses \(\nu(t)\), and the norm in (6). Find a weight attaining that norm.

**Solution.** The unconditional expectation is zero. The masses are \((1+i)/4\) and \(-(1+i)/4\), so their absolute values sum to \(1/\sqrt2\). The weights \(u(0)=(1-i)/\sqrt2\) and \(u(1)=-(1-i)/\sqrt2\) make each weighted mass \(\sqrt2/4\), attaining the sum. The statistic retains less than the full value of \(Y\), but more than its unconditional average.

### 2 A complete conditional offset distribution

For \(n=2\) and \(S_2=4\), list the positive words, their probabilities before and after conditioning, and their offsets modulo nine. Compute the primitive Fourier average at \(\xi=1\).

**Solution.** The words are \((1,3),(2,2),(3,1)\). Each has probability \(1/16\), so \(p_2(4)=3/16\), and each conditional probability is \(1/3\). Since \(2^{-1}=5\), \(2^{-2}=7\), \(2^{-3}=8\), and \(2^{-4}=4\) modulo nine, their offsets \(2^{-A_1}+3\cdot2^{-4}\) are eight, one and two. The average is
\[
\frac{e^{-16\pi i/9}+e^{-2\pi i/9}+e^{-4\pi i/9}}3.
\]
Multiplication by \(3/16\) gives its unnormalized complex mass. The distribution on these three residues is the result of conditioning, not the unconditional offset law.

### 3 What an odd leftover does

Take \(n=3\), and condition on \(B_1=3\) and \(A_3=2\). Determine the two possible words and their offsets modulo 27. Verify (9), and explain why averaging a fresh \(A_3\) here would be wrong.

**Solution.** The words are \((1,2,2)\) and \((2,1,2)\), with conditional probability \(1/2\). Their common total is five. Modulo 27, \(2^{-1}=14\), \(2^{-2}=7\), \(2^{-3}=17\), and \(2^{-5}=11\). The common last summand is \(9\cdot11=18\) modulo 27, and the middle summand is \(3\cdot17=24\). The offsets are therefore two and twenty-two. Formula (9) averages the two pair contributions and multiplies by the fixed character of eighteen. The event being conditioned on already specifies \(A_3=2\); averaging an independent replacement changes the conditional law.

### 4 Paying for a growing observation

Suppose a retained complex measure satisfies \(\sum_s|\nu_k(s)|\leq C_D k^{-D}\) for every \(D>0\). Let \(q\) be any probability mass function on the integers, and suppose the event used for conditioning has probability at least \(c n^{-b}\). Prove a decay bound when \(k\geq n^\delta\), and determine what changes if the only available estimate has one fixed exponent \(D_0\).

**Solution.** The same regrouping as in Proposition 5 proves \(\|\nu_k*q\|_1\leq\|\nu_k\|_1\). A single conditioned mass has modulus at most \(c^{-1}C_D n^{b-\delta D}\). Choosing \(D>(A+b)/\delta\) gives any prescribed decay \(O(n^{-A})\). With only \(D_0\), the conclusion is the specific bound \(O(n^{b-\delta D_0})\); it tends to zero by this estimate only if \(\delta D_0>b\). Failure of that inequality says the estimate is insufficient, not that cancellation is absent.

## References

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12; [arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7), Section 7.1 and Proposition 7.3. Paired cancellation and the positive renewal majorant.
- Jaan Allikvere, *Almost all Collatz orbits attain almost bounded values in natural density*, version 2, [Zenodo 21499244](https://doi.org/10.5281/zenodo.21499244), Theorem 3.1 and Section 2's fixed-total probability estimate. The conditioned Fourier theorem is proved above from the complete internal renewal argument.
- [Conditional cancellation and arithmetic phase geometry](NT-COLLATZ-09.md) and [Weighted renewal estimates and Fourier decay](NT-COLLATZ-11.md), for the exact majorant and its full decay proof.
