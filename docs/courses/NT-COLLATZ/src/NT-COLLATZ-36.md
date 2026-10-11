# Exceptional sets and stopped orbit chains

*Written by GPT-6 Astra (OpenAI), Ultra mode in Codex, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An estimate can say that most inputs behave well without saying that the next input along a trajectory behaves well. A deterministic map may concentrate many starting points on a small exceptional set. Repeatedly applying an almost-everywhere statement therefore requires a counting argument, not an assumption that successive inputs are sampled independently.

This lesson proves that argument for a chain of first passages. It combines the [reverse fibre bounds](NT-COLLATZ-34.md#counting-preimages-of-an-arbitrary-landing-set) with the [controlled orbit envelopes](NT-COLLATZ-35.md#retaining-the-prefactor-uniformly-as-the-tolerance-shrinks). The same construction retains the trajectory's elapsed time and greatest height. At the end, summation over dyadic intervals turns the finite estimates into quantitative natural-density statements. The reusable ideas are preimage counting, stopping at the first failed test, telescoping a decreasing size parameter, and summing near the final scale.

A basic reference for this construction is Idris Ali Shaik's *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, Sections 4–5 and 7. His decreasing-threshold construction supplies the connection between the local orbit estimate and the global count. The finite constants, endpoint exchange and retained entropy prefactor below follow from the internal proofs in the preceding lessons. The references at the end give attribution; the mathematical dependencies needed here are supplied in the course.

## Small sets and their preimages

Let \(f:A\to Z\) be a map of finite sets. If every fibre \(f^{-1}(\{z\})\) has at most \(L\) elements, then
\[
 |f^{-1}(B)|=\sum_{z\in B}|f^{-1}(\{z\})|\le L|B|
 \quad(B\subseteq Z).
 \tag{1}
\]
The equality follows because distinct fibres are disjoint. If a source is recorded by a time \(h\in S\) and a landing \(y\in B\), apply (1) to the map into \(S\times B\). A bound \(L\) on each time-and-landing fibre gives \(|S|L|B|\).

Restriction of the source to a subset chosen by its earlier behaviour cannot enlarge a fibre. This simple observation is what allows (1) to be used at a first failed test. The sources reaching that test have already passed earlier tests, but no new distributional assertion is needed.

For example, a map from one hundred points onto ten points could have ninety-one points in one fibre and one point in each remaining fibre. A one-point exceptional subset of the target then has preimage of size ninety-one, not ten. The size of the target alone does not control the size of its preimage.

## Controlled prefixes and decreasing thresholds

Throughout this lesson the shortcut map is
\[
 T(n)=
 \begin{cases}
 n/2,&n\ \text{even},\\
 (3n+1)/2,&n\ \text{odd},
 \end{cases}
 \qquad n\in\mathbb N_{>0}.
\]
Write
\[
 \lambda=\log_2 3,\quad a_0=\lambda/2,\quad
 g=1-a_0,\quad \rho=\sqrt3/2=2^{-g},\quad \ell=\log2,
 \qquad I_m=[2^m,2^{m+1})\cap\mathbb N .
 \tag{2}
\]
Here and below \(\log\) is the natural logarithm. The binary rank of \(n\) is \(m(n)=\lfloor\log_2 n\rfloor\).

For \(\eta>0\), define the set of inputs with controlled prefixes by
\[
 W_\eta=\{n:\rho^k n^{1-\eta}\le T^k(n)\le
                  \rho^k n^{1+\eta}\quad
                 (0\le k\le m(n))\}.
 \tag{3}
\]
This is a finite test for each input. Its two sides constrain the trajectory around a prescribed rate of decrease; membership is sufficient for the passages used below, not necessary for descent.

Choose
\[
 a_0<r<1,\qquad 0<\eta<r-a_0.
 \tag{4}
\]
In particular \(\eta<g<a_0\). Fix an integer \(M_0\ge2\) large enough that
\[
 rM_0\ge1,\qquad
 (r-a_0-\eta)M_0\ge2+\eta,\qquad
 r\,2^{M_0}\ge2(M_0+2).
 \tag{5}
\]
Such an integer exists. The first two conditions are linear with positive coefficients. For the third, the ratio of consecutive values of \((m+2)/2^m\) is \((m+3)/(2m+4)\le2/3\) for \(m\ge1\), so those values tend geometrically to zero. Once (5) holds, all three conditions hold at every larger rank.

The [finite descent argument](NT-COLLATZ-35.md#why-a-prefix-estimate-gives-a-finite-descent) proves that from every \(x\in W_\eta\cap I_m\), \(m\ge M_0\), the first passage to \(2^q\), where \(q=\lfloor rm\rfloor\), has a time \(1\le h\le m\) and a landing
\[
 2^{q-1}<y\le2^q.
 \tag{6}
\]
Indeed the upper envelope at time \(m\) gives
\(T^m(x)<2^{(a_0+\eta)m+1+\eta}\le2^{rm-1}\le2^q\).
The start exceeds the threshold, and \(T(v)\ge v/2\) proves the lower landing bound. The entire block has height at most \(x^{1+\eta}\).

For integers \(M\ge L\ge M_0\), construct a stopped chain from \(n\in I_M\). At a checkpoint \(n_i\) of rank \(m_i\), stop successfully if \(m_i<L\). Otherwise stop with failure if \(n_i\notin W_\eta\). If neither stopping rule applies, execute the actual first passage to \(2^{q_i}\), \(q_i=\lfloor rm_i\rfloor\), and call its landing \(n_{i+1}\). Denote by \(G_{M,L}\) the starts for which this procedure stops successfully.

Every executed block is a segment of the original trajectory. By (6),
\[
 m_{i+1}\le q_i\le r m_i<m_i.
 \tag{7}
\]
Thus the procedure terminates after finitely many blocks, whether or not it succeeds.

![An initial failed test is counted in the source shell. Otherwise certified blocks lead to a first failed landing in a specified band, or to success below the terminal rank. The first failed landing is reached through successful blocks; it is not itself assumed controlled.](../figures/stopped-chain.svg)

*Figure 1. The first-failure decomposition used in Theorem 3. The arrows denote actual first passages. Counting a failed landing uses the original source, its cumulative time and its landing value, not a newly sampled integer.*

## Exchanging the shell endpoints exactly

The input shell \(I_{q-1}\) includes \(2^{q-1}\) and excludes \(2^q\); the landing band in (6) does the reverse. A bound obtained by merely adding the upper endpoint loses one integer. For this particular test, the removed endpoint has exactly the same status.

**Lemma 1.** Put \(B_q=(2^{q-1},2^q]\cap W_\eta^c\), with \(0<\eta<a_0\). For \(q\ge2\),
\[
 |B_q|=|I_{q-1}\setminus W_\eta|.
 \tag{8}
\]
For \(q=1\), \(B_1=\{2\}\) whereas \(I_0\setminus W_\eta\) is empty.

**Proof.** If \(m\ge1\), then \(T^m(2^m)=1\), but the lower envelope required in (3) at time \(m\) equals
\[
 \rho^m(2^m)^{1-\eta}=2^{(a_0-\eta)m}>1.
\]
Consequently every positive power of two fails the test. The integer \(1\) passes, since its only required time is zero.

For \(q\ge2\), define \(\phi:I_{q-1}\setminus W_\eta\to B_q\) by \(\phi(2^{q-1})=2^q\) and \(\phi(x)=x\) on all other inputs. Both exceptional endpoints belong to the indicated complements. The inverse sends \(2^q\) back to \(2^{q-1}\) and fixes every interior point. This proves (8) and the assertion at \(q=1\). ∎

These powers of two reach \(1\) rapidly. Their failure of the two-sided test is caused by decreasing *faster* than its lower envelope permits. Thus an exceptional input for this proof method is not evidence of an orbit that fails to descend.

We shall use the fixed-tolerance estimate proved in [Maximal parity deviations and orbit envelopes](NT-COLLATZ-35.md#retaining-the-prefactor-uniformly-as-the-tolerance-shrinks):
\[
 |I_m\setminus W_\eta|
 \le C_\eta^*\,2^m(m+1)^{-1/2}e^{-bm},
 \qquad b=I(\eta/\lambda),\quad 0<b<\ell,
 \tag{9}
\]
where
\[
 I(u)=(1/2+u)\log(1+2u)+(1/2-u)\log(1-2u).
\]
The preceding lesson defines \(C_\eta^*\) explicitly and proves (9) at every \(m\ge0\). From (8),
\[
 \frac{|B_q|}{2^q}\le Kq^{-1/2}e^{-bq},
 \qquad K=\tfrac12 C_\eta^*e^b,\quad q\ge2.
 \tag{10}
\]
No additional \(2^{-q}\) term is needed. The bijection in Lemma 1 is only a counting bijection; it makes no assertion that the two endpoints have conjugate trajectories.

## Pulling back the first failed test

**Lemma 2.** Every successful chain from \(n\in I_M\) has an actual shortcut time \(h\ge1\) and landing \(y<2^L\), with
\[
 h<\frac M{1-r},\qquad
 \max_{0\le t\le h}T^t(n)\le n^{1+\eta}.
 \tag{11}
\]
The same time and height bounds hold through any generated first failed checkpoint.

**Proof.** The ranks in (7) satisfy \(m_i\le r^iM\). Each executed block has duration at most \(m_i\), so their finite total is strictly less than the infinite sum \(M\sum_{i\ge0}r^i=M/(1-r)\). Checkpoint values strictly decrease. Each block's height is at most \(n_i^{1+\eta}\le n^{1+\eta}\), including its endpoint. The same proof applies if the last landing fails its next test: every block actually executed before it was controlled. On success the final rank is less than \(L\), which gives \(y<2^L\). ∎

**Theorem 3.** Put
\[
 H_M=\left\lceil\frac M{1-r}\right\rceil-1,\qquad
 A_r=\frac12+\frac2r,\qquad
 C_1=\frac{\sqrt2 A_rK}{(1-r)(1-e^{-b})^2}.
\]
For all \(M\ge L\ge M_0\), the failure proportion satisfies
\[
\begin{aligned}
 \frac{|I_M\setminus G_{M,L}|}{2^M}
 &\le \frac{C_\eta^*e^{-bM}}{\sqrt{M+1}}\\
 &\quad+H_MK\sum_{q=L}^{M-1}
 \left(2^{q-M}+\frac{4(q+2)}{3r}\right)q^{-1/2}e^{-bq}\\
 &\le \frac{C_\eta^*e^{-bM}}{\sqrt{M+1}}
       +C_1M\sqrt{L+1}e^{-bL}.
\end{aligned}
\tag{12}
\]
An empty sum, including when \(L=M\), is zero.

**Proof.** Failure at the initial checkpoint costs the first term by (9). Any later first failure has a generating threshold \(2^q\), with \(L\le q<M\), and a landing in \(B_q\). All blocks preceding this landing are controlled. Decreasing thresholds imply that their concatenation is the original source's *direct* first passage to \(2^q\): before each earlier crossing the state exceeds its larger threshold, hence also the final threshold.

The [decreasing-rank transport theorem](NT-COLLATZ-34.md#decreasing-thresholds-suppress-earlier-loss), equation (19), applies to these original sources. Its scaled reverse loss is less than \(D_q=2(q+2)/(3r)\). Condition (5) gives \(D_q/2^q\le1/3\) for every \(q\ge L\). The possible cumulative times are positive integers strictly below \(M/(1-r)\). Their containing set has exactly \(H_M\) elements, including the case when \(M/(1-r)\) is an integer.

The transport theorem therefore bounds the fraction of sources at a given \(q\) by
\[
 H_M\frac{|B_q|}{2^q}
       \left(2^{q-M}+\frac{4(q+2)}{3r}\right).
\]
Use (10) and sum over \(q\). Multiple possible tags can only make this union bound larger; there is no assumption of independent tests or uniform landings.

For the second inequality, \(q<M\) and \(q\ge1\) give
\[
 2^{q-M}+\frac{4(q+2)}{3r}\le A_r(q+1),
 \qquad \frac{q+1}{\sqrt q}\le\sqrt{2(q+1)}.
\]
For \(0<z<1\), writing \(q=L+j\) gives
\[
 \sum_{q=L}^\infty\sqrt{q+1}\,z^q
 \le\sqrt{L+1}\,z^L\sum_{j=0}^\infty(j+1)z^j
 =\frac{\sqrt{L+1}\,z^L}{(1-z)^2}.
 \tag{13}
\]
Here \(\sqrt{1+j/(L+1)}\le j+1\); the last sum follows by multiplying two convergent geometric series and grouping pairs of indices with sum \(j\). Apply (13) at \(z=e^{-b}\) and use \(H_M<M/(1-r)\). ∎

The factor \(M\) pays for possible cumulative times. The factor \(\sqrt{L+1}\) comes from multiplying a linear rank-dependent fibre bound by the inverse square-root factor in (10). These are different mechanisms. Removing either factor would require further mathematics about that mechanism, not merely a change of notation.

## Retaining the rank removed in the clock

The bound \(M/(1-r)\) forgets how far the chain needed to descend. A telescope retains the terminal rank.

**Proposition 4.** Suppose a successful chain executes blocks numbered \(0,\ldots,j\). Its same elapsed time satisfies
\[
 gh<M-rL+\frac{\eta M}{1-r}+(1+\eta)j+3+\eta,
 \qquad
 j\le\frac{\log(M/L)}{\log(1/r)}.
 \tag{14}
\]

**Proof.** Immediately before the first passage in block \(i\), its state exceeds \(2^{q_i}\). The envelope and \(n_i<2^{m_i+1}\) imply
\[
 2^{q_i}<T^{h_i-1}(n_i)
 <2^{-g(h_i-1)+(1+\eta)(m_i+1)}.
\]
Since \(g<1\), it follows that
\(gh_i<(1+\eta)(m_i+1)-q_i+1\).

For \(1\le i\le j\), the checkpoint \(n_i\) passes its test. By Lemma 1 it cannot be the upper endpoint \(2^{q_{i-1}}\). All other integers in its landing band have rank \(q_{i-1}-1\). Hence
\[
 m_i=q_{i-1}-1,\qquad
 \sum_{i=0}^j(m_i-q_i)=M-q_j-j.
 \tag{15}
\]
Summing the individual time inequalities and using
\(\sum_i m_i<M/(1-r)\) gives
\(gh<M-q_j+\eta M/(1-r)+(1+\eta)j+2+\eta\).
The final parent has rank \(m_j\ge L\), so \(q_j\ge rL-1\). Also \(L\le m_j\le r^jM\). These prove both parts of (14). ∎

This distinction matters when \(L\) is a positive fraction of \(M\). In that case the subtraction \(rL\) has the same order as \(M\), while the number of blocks stays bounded in terms of \(r\) and that fraction.

There is also information about the other clocks on this very path. Let \(s\) count its odd shortcut inputs. The [reverse product identity](NT-COLLATZ-34.md#recovering-the-same-passage-in-the-other-clocks) has the form
\[
 n=\frac{2^h y}{3^s}P,\qquad 0<P\le1.
\]
Since \(n\ge2^M\) and \(y<2^L\), this gives
\[
 s<\frac{h-M+L}{\lambda}.
 \tag{16}
\]
Each odd shortcut transition inserts one extra state in the ordinary map \(C\), so the ordinary time to this same \(y\) is exactly \(h+s\). Each inserted state is \(2T(x)\), and consequently the ordinary height is at most \(2n^{1+\eta}\).

If the original input is odd, complete the last descending string of even values from \(y\) to its odd part \(u=y/2^{\nu_2(y)}\). The odd-return time to \(u\) is \(s\), and \(u\le y\). The ordinary time to \(u\), however, is \(h+s+\nu_2(y)\). Thus the three clocks describe one underlying orbit, but the odd-return endpoint need not equal the shortcut endpoint. Equation (16) preserves the distinction.

## Summing without losing the exponential rate

A shell estimate becomes a statement for all integers up to \(X\) by counting complete shells, including the one containing \(X\). Splitting the sum halfway can unnecessarily weaken the exponential constant. The following elementary estimate avoids that loss.

**Lemma 5.** Let \(0<\sigma<1\), \(p\ge0\) and \(d>0\). Suppose a set \(E\subseteq\mathbb N_{>0}\) satisfies
\[
 |E\cap I_M|\le C\,2^M M^p e^{-dM^\sigma}
\]
at every sufficiently large integer \(M\). Then
\[
 |E\cap[1,X]|
 =O\!\left(X(\log X)^p
       \exp\{-d\ell^{-\sigma}(\log X)^\sigma\}\right).
 \tag{17}
\]
The implied constant depends only on the fixed parameters and the finite startup.

**Proof.** Choose \(0<\theta<\ell\). For an integer \(N_0\ge1\) large enough, \(d\sigma N_0^{\sigma-1}\le\theta\), and the shell estimate holds for \(M\ge N_0\). Let \(J=\lfloor\log_2X\rfloor\). For \(N_0\le M\le J\),
\[
 d(J^\sigma-M^\sigma)
 =\int_M^Jd\sigma t^{\sigma-1}\,dt\le\theta(J-M).
\]
Also \(M^p\le J^p\). The contribution of these shells is at most
\[
 C2^J J^p e^{-dJ^\sigma}
       \sum_{j=0}^{J-N_0}(e^\theta/2)^j
 \le\frac{C2^J J^p e^{-dJ^\sigma}}{1-e^\theta/2}.
\]
Smaller integers contribute at most \(2^{N_0}-1\).

Put \(t=\log X/\ell\). For \(J\ge1\), \(0\le t-J<1\) and
\(t^\sigma-J^\sigma\le\sigma J^{\sigma-1}\le\sigma\).
Therefore \(e^{-dJ^\sigma}\le e^{d\sigma}e^{-dt^\sigma}\), \(J^p\le t^p\), and \(2^J\le X\). The resulting main expression tends to infinity because \(t-dt^\sigma/\ell\) tends to infinity; it absorbs the finite startup. This proves (17) with the same coefficient \(d\ell^{-\sigma}\). ∎

## Quantitative descent on the same controlled path

Theorem 3 can now be used with two different terminal scales. Keep \(r,\eta\) fixed as in (4), and write \(D=b/\ell\in(0,1)\).

**Corollary 6.** For each \(0<\sigma<1\), there is a set \(G_\sigma\) such that
\[
 |[1,X]\setminus G_\sigma|
 =O\!\left(X(\log X)^{1+\sigma/2}
              e^{-D(\log X)^\sigma}\right).
 \tag{18}
\]
For every sufficiently large \(n\in G_\sigma\), the same path from Lemma 2 reaches a value below \(\exp((\log n)^\sigma)\), within fewer than
\(\log n/((1-r)\ell)\) shortcut steps, and with shortcut height at most \(n^{1+\eta}\).

For each \(0<\alpha<1\), a set \(G_\alpha\) satisfies
\[
 |[1,X]\setminus G_\alpha|
 =O\!\left(X^{1-\alpha D}(\log X)^{3/2}\right).
 \tag{19}
\]
For its sufficiently large inputs the same path reaches a value below \(n^\alpha\), obeys (11), (14) and (16), and has height at most \(n^{1+\eta}\). Both sets have natural density one.

**Proof.** In shell \(I_M\), choose respectively
\(L_M=\lfloor\ell^{\sigma-1}M^\sigma\rfloor\) or \(L_M=\lfloor\alpha M\rfloor\), and use \(G_{M,L_M}\). Both lie between \(M_0\) and \(M\) once \(M\) is sufficiently large. Put no small inputs into the resulting sets; their finite number is absorbed by the bounds.

For the first choice, \(\ell L_M\le(\ell M)^\sigma\le(\log n)^\sigma\). Since the landing is strictly below \(2^{L_M}\), it meets the stated target. The floor costs at most a factor \(e^b\) in \(e^{-bL_M}\), and \(\sqrt{L_M+1}=O(M^{\sigma/2})\). Thus (12) gives a failure proportion
\(O(M^{1+\sigma/2}e^{-b\ell^{\sigma-1}M^\sigma})\).
The initial term in (12) is smaller for all sufficiently large \(M\), since \(M^\sigma=o(M)\). Lemma 5 proves (18), because
\(b\ell^{\sigma-1}\ell^{-\sigma}=D\).

For the second choice, \(2^{L_M}\le2^{\alpha M}\le n^\alpha\), and (12) gives shell failure count
\(O(2^{(1-\alpha D)M}M^{3/2})\).
Since \(1-\alpha D>0\), summing through \(J\) bounds this by a constant times \(2^{(1-\alpha D)J}J^{3/2}\): write \(M=J-j\), bound \(M^{3/2}\le J^{3/2}\), and sum \(2^{-(1-\alpha D)j}\). This is (19). The time and height statements are inherited from the very same successful chains, not from an intersection of unrelated existential conclusions. Dividing (18) and (19) by \(X\) gives limits zero. ∎

For a desired ordinary-height allowance \(n^{1+\beta}\), choose \(\eta<\beta\) as well as (4). Then \(2n^{1+\eta}\le n^{1+\beta}\) for \(n\ge2^{1/(\beta-\eta)}\). The exceptional estimates and the clock conversions still concern these same paths.

## Exercises with solutions

### Counting is not preservation of uniform sampling

Let \(A=\{1,\ldots,12\}\), \(Z=\{a,b,c,d\}\), and suppose a map has fibre sizes \(6,3,2,1\), in that order. Compute the preimage of \(B=\{d\}\) and the largest possible preimage of a two-point target. Compare the latter with a uniform-target guess and the maximum-fibre bound.

**Solution.** The first preimage has one element. The largest two-point preimage is the union of the \(a\) and \(b\) fibres, of size nine. The uniform guess would be \(12\cdot2/4=6\), which is false for that target. The maximum-fibre estimate gives \(6\cdot2=12\), which is valid but larger than nine. Retaining separate fibre sizes gives the exact answer. Thus an improved transport estimate can come from more precise fibre information, not from assuming better sampling.

### The first endpoint exchange

For \(0<\eta<a_0\), explain why the exchange at rank \(q=1\) has a correction and why the exchanges at all ranks \(q\ge2\) do not. What happens if \(W_\eta\) is replaced by a set \(S\) that contains the lower endpoint and excludes the upper one?

**Solution.** At \(q=1\), the input shell is \(\{1\}\) and the landing band is \(\{2\}\). The first point passes its time-zero test; the second fails its lower test at time one. Hence the complementary counts are zero and one. For \(q\ge2\), both exchanged powers fail, and the explicit bijection in Lemma 1 applies. For the arbitrary set \(S\), the general identity is
\[
 |(2^{q-1},2^q]\setminus S|
 =|[2^{q-1},2^q)\setminus S|
  -\mathbf1_{\{2^{q-1}\notin S\}}
  +\mathbf1_{\{2^q\notin S\}}.
\]
Under the stated memberships the count increases by one. The endpoint saving cannot be transferred to arbitrary targets without checking their memberships.

### Telescoping a two-block rank sequence

Take \(r=7/8\), \(M=64\) and \(L=48\). Suppose a successful chain has two controlled parent checkpoints and the first landing is not a power of two. Determine their ranks and thresholds, and verify (15). Why is this arithmetic not an existence proof for an orbit with those two blocks?

**Solution.** The first threshold rank is \(q_0=\lfloor(7/8)64\rfloor=56\). The next controlled checkpoint has rank \(m_1=55\). Its threshold rank is \(q_1=\lfloor(7/8)55\rfloor=48\). Success after that block requires its landing to have rank \(47\), not \(48\), since \(L=48\). Thus
\((64-56)+(55-48)=15=64-48-1\), as (15) states for \(j=1\).
These are necessary rank relations for the specified chain. They neither choose integer landings in the bands nor establish their membership in \(W_\eta\), and therefore do not construct such an orbit.

### Reading the power in the exceptional count

Take \(L_M=\lfloor M/3\rfloor\). Derive the power of \(X\) and the logarithmic factor in the global failure count. Would deleting the boundary correction alone change either exponent?

**Solution.** In (12), the later-failure term is
\(O(M^{3/2}e^{-bM/3})\); the floor contributes only a fixed factor. Multiplying by the shell size gives \(O(2^{(1-D/3)M}M^{3/2})\), and the positive geometric exponent gives
\(O(X^{1-D/3}(\log X)^{3/2})\).
The initial failure is smaller. A retained dyadic boundary correction would contribute \(O(M^2 2^{-M/3})\) as a fraction of the shell. Since \(b<\ell\), that term is smaller than the entropy term for sufficiently large \(M\). Removing it improves the finite estimate, not the two exponents just derived.

## What the synthesis establishes

The local prefix theorem and the deterministic fibre theorem supply different information. One counts where a test fails; the other counts how many original inputs can arrive at a specified failed landing. Stopping at the first failure lets them work together without independent sampling. The resulting quantitative conclusions retain a single path, its terminal size, elapsed time and height.

The entropy rate, square-root prefactor, rank-dependent fibre count and clock telescope remain visible in the final estimates. That makes both the strength of the conclusions and the work of each technique inspectable. Natural density one concerns a proportion of initial integers; none of these statements asserts descent for every initial integer.

## References

- Idris Ali Shaik, *Polylogarithmic Descent for Almost All Collatz Orbits in Natural Density*, version 3.2.4, 27 August 2026, Sections 4–5 and 7, Appendix A. [Preprint](https://doi.org/10.5281/zenodo.22130385). The [formal source at the fixed revision](https://github.com/shaikidris/FirstPassageLinearTransport/tree/ef3410843bf58d69f771f5ba2c0571d54b54da59/lean/FirstPassageLinearTransport) distinguishes the finite transport envelope, the actual first-failure construction and the global assembly.

