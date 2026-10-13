# Amplitude amplification and the Forrelation test

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Suppose a quantum computation succeeds with a small probability \(p\), and success is marked by a bit. Repeating it about \(1/p\) times finds a success. Amplitude amplification finds one with about \(1/\sqrt p\) repetitions. This lesson proves it in the form needed later: the state that is obtained in the case of success is always the same state, whatever the number of repetitions was. The lesson also gives the quantum algorithm for the Forrelation function, which needs a number of queries that does not depend on the length \(m\), and the algorithm that computes the address of a column.

- A rotation in a plane (Lemma 1.1).
- Amplification with a fixed successful state (Lemma 1.2).
- The Forrelation test: success probability \(\Phi^2\) with \(2k\) queries (Lemma 2.1).
- The value of the Forrelation function with error \(\eta\) (Lemma 2.2).
- The address of a column (Lemma 2.3).

The lesson follows [OpenAI-Q, Lemma 2.1(2) and Section 3.1]. It uses query circuits, read and phase queries, and the two rules for probabilities from [The quantum query model](the-quantum-query-model.md), and the Forrelation function from [Query complexity and a function with outward pointers](query-complexity-and-a-function-with-outward-pointers.md).

## 1. Amplification

**Definition.** A *preparation* is a query circuit \(A\) on some registers, one of which has the labels \(\{0,1\}\) and is called the *success bit*. All registers start in the basis state \(|0\rangle\). For an input \(x\) put
\[
\varphi=A|0\rangle=\varphi_1+\varphi_0,
\]
where \(\varphi_1\) is the part of \(\varphi\) with the success bit \(1\) and \(\varphi_0\) the part with the success bit \(0\). The *success probability* is \(p=\|\varphi_1\|^2\). If \(p>0\), the *successful state* is \(g=\varphi_1/\|\varphi_1\|\).

So \(p\) is the probability that a measurement of the success bit gives \(1\), and \(g\) is the state after this outcome. Both depend on \(x\).

Let \(S\) be the map that multiplies the basis states with the success bit \(1\) by \(-1\) and leaves the others unchanged, and let \(S_0\) be the map that leaves \(|0\rangle\) unchanged and multiplies all other basis states by \(-1\). Both are unitary and do not depend on \(x\). Put
\[
G=A\,S_0\,A^{-1}\,S .
\]
If \(A\) has \(c\) queries, \(G\) is a query circuit with \(2c\) queries.

**Lemma 1.1.** Let \(0<p<1\). Let \(b=\varphi_0/\|\varphi_0\|\) and \(0<\theta<\tfrac\pi2\) with \(\sin\theta=\sqrt p\), so that \(\varphi=\sin\theta\,g+\cos\theta\,b\). Then for all integers \(l\ge0\),
\[
\begin{aligned}
G^l\varphi={}&\sin((2l+1)\theta)\,g\\
&+\cos((2l+1)\theta)\,b .
\end{aligned}
\]

**Proof.** \(S_0\psi=2\langle|0\rangle,\psi\rangle|0\rangle-\psi\), so
\[
A\,S_0\,A^{-1}\psi=2\langle\varphi,\psi\rangle\,\varphi-\psi ,
\]
because \(\langle|0\rangle,A^{-1}\psi\rangle=\langle A|0\rangle,\psi\rangle\). Also \(Sg=-g\) and \(Sb=b\). Hence
\[
\begin{aligned}
Gg&=-2\sin\theta\,\varphi+g\\
&=\cos2\theta\,g-\sin2\theta\,b,\\
Gb&=2\cos\theta\,\varphi-b\\
&=\sin2\theta\,g+\cos2\theta\,b .
\end{aligned}
\]
So \(G\) maps \(\sin\alpha\,g+\cos\alpha\,b\) to \(\sin(\alpha+2\theta)\,g+\cos(\alpha+2\theta)\,b\), by the addition formulas. Start with \(\alpha=\theta\). \(\blacksquare\)

In the plane of \(g\) and \(b\), the map \(G\) is a rotation by the angle \(2\theta\). Each application moves the state toward \(g\) by this angle, until it passes \(g\). The part with the success bit \(1\) is always a multiple of the same vector \(g\).

**Lemma 1.2** (amplification). Let \(A\) be a preparation with \(c\) queries, and let \(0<\gamma\le\tfrac12\) and \(0<\eta<\tfrac12\). There is a procedure with at most
\[
88\,c\,\gamma^{-1/2}\log_2(1/\eta)
\]
queries on every path that ends with *success* or with *failure* and has the following properties, for every input.

1. If \(p=0\), it ends with failure.
2. If \(p\ge\gamma\), it ends with failure with a probability of at most \(\eta\).
3. If it ends with success, it holds registers in the state \(g\), up to a factor of absolute value \(1\): if these registers are then measured, the probability of success together with the outcome \(\beta\) is the probability of success times \(|g_\beta|^2\).

**Proof.** Put \(M=\lceil10/\sqrt\gamma\rceil\) and \(N=\lceil\log(1/\eta)/\log(40/31)\rceil\).

*The procedure.* Make at most \(N\) *trials*. A trial uses new registers in the state \(|0\rangle\). It chooses an integer \(l\) at random: with the probability \(\tfrac12\) it takes \(l=0\), and with the probability \(\tfrac12\) it takes \(l\) uniformly from \(\{0,\dots,M-1\}\). It applies \(G^lA\) and measures the success bit. If the outcome is \(1\), the procedure ends with success and holds the registers of this trial. If all \(N\) trials give \(0\), it ends with failure.

*The state.* Let \(0<p<1\). By Lemma 1.1 a trial with the number \(l\) gives the outcome \(1\) with the probability \(\sin^2((2l+1)\theta)\), and then the state of its registers is \(g\) or \(-g\). For \(p=1\) we have \(\varphi=g\), \(G\varphi=-\varphi\), and every trial succeeds with the state \(\pm g\). For \(p=0\) we have \(\varphi=\varphi_0\), \(G\varphi=\varphi\), and no trial succeeds. This proves 1 and 3: the registers of the earlier trials are separate from those of the successful one, so they do not influence its measurement (Rule 6.2 of the lesson on the model).

*The probability of a trial.* Let \(\gamma\le p\), and let \(\pi\) be the probability that one trial succeeds. If \(p\ge\tfrac12\), the choice \(l=0\) alone gives \(\pi\ge\tfrac12p\ge\tfrac14\). Let \(p<\tfrac12\). Then
\[
\sin2\theta=2\sqrt{p(1-p)}\ge\sqrt{2p}\ge\sqrt\gamma .
\]
From
\[
\begin{aligned}
&2\sin2\theta\cos((4l+2)\theta)\\
&\quad=\sin((4l+4)\theta)-\sin(4l\theta)
\end{aligned}
\]
we get \(\sum_{l=0}^{M-1}\cos((4l+2)\theta)=\frac{\sin(4M\theta)}{2\sin2\theta}\), and so
\[
\begin{aligned}
&\frac1M\sum_{l=0}^{M-1}\sin^2((2l+1)\theta)\\
&\quad=\frac12-\frac{\sin(4M\theta)}{4M\sin2\theta}\\
&\quad\ge\frac12-\frac1{4M\sqrt\gamma}\ge\frac{19}{40}.
\end{aligned}
\]
So \(\pi\ge\tfrac12\cdot\tfrac{19}{40}\). In both cases \(\pi\ge\tfrac9{40}\).

*Failure.* The trials use separate registers and separate random choices, so they are independent, and all \(N\) fail with the probability \((1-\pi)^N\le(31/40)^N\le\eta\). This is 2.

*Queries.* A trial makes at most \(c+2c(M-1)\le2cM\) queries. Since \(\gamma\le\tfrac12\) and \(\eta<\tfrac12\), \(M\le11/\sqrt\gamma\) and \(N\le4\log_2(1/\eta)\). \(\blacksquare\)

Two points of the lemma are used later. The bound for the queries holds on every path and for every \(p\), also when \(p\) is positive and smaller than \(\gamma\); in that case nothing is said about the probability of failure. And property 3 holds for every \(p>0\): whenever the procedure succeeds, the state is \(g\). Amplification changes how often a sample is obtained, not how the sample is distributed.

## 2. The Forrelation test

Let \(k\ge2\) and \(m=2^\ell\). Let the strings \(z_1,\dots,z_k\in\{0,1\}^m\) be parts of the input \(x\): the bit of \(z_h\) at the position \(a\in\{0,1\}^\ell\) is the input bit at the position \(\mathrm{loc}(h,a)\). Recall
\[
\Phi=u^{\mathsf T}D_{z_1}HD_{z_2}H\cdots HD_{z_k}u .
\]

**Lemma 2.1** (the test). There is a preparation with \(2k\) queries whose success probability is \(\Phi(z_1,\dots,z_k)^2\).

**Proof.** Use a register with the labels \(\{0,1\}^\ell\) and a success bit. The matrix \(H\) is real and orthogonal, so it defines a unitary map of the register, and \(H|0\dots0\rangle=u\). The phase query with the function \(a\mapsto\mathrm{loc}(h,a)\) is the map \(D_{z_h}\). Apply to \(|0\dots0\rangle\), in this order,
\[
H,\ D_{z_k},\ H,\ D_{z_{k-1}},\ \dots,\ H,\ D_{z_1},\ H .
\]
The result is \(H\xi\) with \(\xi=D_{z_1}H\cdots HD_{z_k}u\). Its entry at the label \(0\dots0\) is
\[
\langle e_0,H\xi\rangle=\langle He_0,\xi\rangle=\langle u,\xi\rangle=\Phi,
\]
because \(H\) is symmetric and \(He_0=u\). Last, a permutation map sets the success bit to \(1\) if the register contains \(0\dots0\). There are \(k\) phase queries, each of two queries by Lemma 4.2 of the lesson on the model. \(\blacksquare\)

If \(P(z_1,\dots,z_k)=1\), the success probability is at least \(\delta^2\); if \(P=0\), it is at most \(\delta^2/4\), with \(\delta=2^{-5k}\). The two cases are told apart by repeating the test. The number of queries of one test does not depend on \(m\).

**Lemma 2.2.** Let \(0<\eta<\tfrac12\). There is a query circuit with at most
\[
c_k\log_2(1/\eta),\qquad c_k=384\,k\,2^{10k},
\]
queries and with a register with the labels \(\{0,1\}\), the *answer bit*, such that: if \(P(z_1,\dots,z_k)\) is defined, a measurement of the answer bit gives \(P(z_1,\dots,z_k)\) with a probability of at least \(1-\eta\).

**Proof.** *A block.* Put \(N_0=64\cdot2^{10k}=64/\delta^2\). A block consists of \(N_0\) tests of Lemma 2.1 in separate registers, and a permutation map that sets a *block bit* to \(1\) if at least \(40\) of the \(N_0\) success bits are \(1\). By the two rules for probabilities, the block bit is distributed as follows: let \(Y\) be the number of successes in \(N_0\) independent trials with the success probability \(p=\Phi^2\); the block bit is \(1\) if \(Y\ge40\). The mean of \(Y\) is \(N_0p\), and its variance is \(N_0p(1-p)\le N_0p\).

If \(P=1\), then \(N_0p\ge64\), so \(40\le\tfrac58N_0p\), and by Chebyshev's inequality
\[
\Pr(Y<40)\le\frac{N_0p}{(\tfrac38N_0p)^2}=\frac{64}{9N_0p}\le\frac19 .
\]
If \(P=0\), then \(N_0p\le16\), and
\[
\Pr(Y\ge40)\le\frac{16}{24^2}=\frac1{36}.
\]
So the block bit differs from \(P\) with a probability of at most \(\tfrac19\).

*Majority.* Put \(r_0=\lceil\log(1/\eta)/\log(3/2)\rceil\). Use \(r_0\) blocks in separate registers, and a permutation map that sets the answer bit to \(1\) if more than half of the block bits are \(1\). The answer is wrong only if at least \(r_0/2\) of the block bits are wrong. The block bits are independent, so this has a probability of at most
\[
\sum_{j\ge r_0/2}\binom{r_0}j\Bigl(\frac19\Bigr)^j\le2^{r_0}\,3^{-r_0}\le\eta .
\]

*Queries.* \(2k\cdot N_0\cdot r_0\), and \(r_0\le3\log_2(1/\eta)\). \(\blacksquare\)

Outside the domain of \(P\) the circuit still produces an answer bit, with some distribution. No measurement is made inside the circuit, and all registers are kept. So the circuit can be applied to a superposition and can be inverted.

The lemma is applied to the strings \(A_{i,h}\) of the function \(F_{k,m}\). The column \(i\) and the number \(h\) are then contents of registers, and the function \(\mathrm{loc}\) of the phase queries depends on them: \(\mathrm{loc}(i,h,h',a)\) is the position of the bit \(a\) of the \(h'\)-th string of \(A_{i,h}\). The circuit is then controlled by these registers.

**Lemma 2.3** (the address of a column). Let \(0<\varepsilon<\tfrac12\). There is a query circuit \(\mathrm{Adr}_\varepsilon\) with at most
\[
r\,c_k\log_2(r/\varepsilon)
\]
queries, controlled by a register with the labels \(\{1,\dots,m\}\), the *column register*, and with an *address register* with the labels \(\{0,1\}^r\), such that for every column \(i\): if \(P(A_{i,h})\) is defined for all \(h\), a measurement of the address register after \(\mathrm{Adr}_\varepsilon|i\rangle|0\rangle\) gives the true address \(s_i\) with a probability of at least \(1-\varepsilon\).

**Proof.** For \(h=1,\dots,r\) apply the circuit of Lemma 2.2 for the strings of \(A_{i,h}\), with \(\eta=\varepsilon/r\), in separate registers; its answer bit is the bit \(h\) of the address register. The probability that some bit is wrong is at most \(r\cdot\varepsilon/r\). \(\blacksquare\)

For a column in which some \(P(A_{i,h})\) is not defined, \(\mathrm{Adr}_\varepsilon\) still produces addresses, with some distribution. The algorithm of the next lesson cannot know whether an address is meaningful. It does not need to: a wrong address leads to a cell that fails the tests.

## 3. Exercises

**3.1.** Let \(p=\tfrac14\). Show that one application of \(G\) gives a state with the success probability \(1\).

**3.2.** Let \(p=\sin^2\theta\) be small. About how many applications of \(G\) bring the success probability close to \(1\)? Compare with the number of repetitions of \(A\) alone that are needed for one success on average.

**3.3.** Check the identity \(\tfrac1M\sum_{l<M}\sin^2((2l+1)\theta)=\tfrac12-\tfrac{\sin(4M\theta)}{4M\sin2\theta}\) for \(M=1\).

**3.4.** For \(k=2\), \(m=4\), \(z_1=0000\), \(z_2=0110\), find the success probability of the test of Lemma 2.1. (Use Exercise 7.3 of the first lesson.)

**3.5.** How many blocks does Lemma 2.2 use for \(\eta=2^{-20}\), and how many tests in all for \(k=2\)?

## 4. Solutions

**3.1.** \(\sin\theta=\tfrac12\), \(\theta=\tfrac\pi6\), and \(G\varphi=\sin(3\theta)g+\cos(3\theta)b=g\).

**3.2.** The success probability after \(l\) applications is \(\sin^2((2l+1)\theta)\), which is close to \(1\) for \((2l+1)\theta\) close to \(\tfrac\pi2\), that is \(l\) about \(\tfrac\pi{4\theta}\), about \(\tfrac\pi{4\sqrt p}\). Repeating \(A\) alone needs \(1/p\) repetitions on average. If \(p\) is not known, a fixed \(l\) may overshoot; this is why Lemma 1.2 chooses \(l\) at random.

**3.3.** For \(M=1\) the left side is \(\sin^2\theta\). The right side is \(\tfrac12-\tfrac{\sin4\theta}{4\sin2\theta}=\tfrac12-\tfrac{\cos2\theta}2=\sin^2\theta\).

**3.4.** \(\Phi=\tfrac12\), so the success probability is \(\tfrac14\).

**3.5.** \(r_0=\lceil20/\log_2(3/2)\rceil=\lceil34.2\rceil=35\) blocks; each has \(N_0=64\cdot2^{20}\) tests, so there are \(35\cdot64\cdot2^{20}\), about \(2.3\cdot10^9\), tests. The number does not depend on \(m\).

## References

- [OpenAI-Q] OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, OpenAI Math Release preprint, 5 October 2026, Sections 2.1 and 3.1. https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026
