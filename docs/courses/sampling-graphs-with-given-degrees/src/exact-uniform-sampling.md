# Exact uniform sampling

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The mixing theorem of [The switch chain](the-switch-chain.md) and [Disjoint pair resamplings](disjoint-pair-resamplings.md) says that after polynomially many steps the switch chain is close to uniform. This lesson removes the remaining error and proves:

**Theorem 4.1** (OpenAI 2026). There is a randomized algorithm that, given a graphical vector \(d=(d_1,\dots,d_n)\), uses unbiased random bits, stops with probability one, and outputs a graph that is *exactly* uniformly distributed on the set \(\Omega_d\) of simple graphs on \(\{1,\dots,n\}\) in which vertex \(i\) has degree \(d_i\). Its expected number of bit operations is bounded by a fixed polynomial in the length of the binary encoding of \(d\).

The construction is a rare residual mixture, a method of Göbel, Liu, Manurangsi and Pappik [GLMP]: most of the time, output the state of the switch chain after many steps, whose law \(p\) is extremely close to uniform; on a branch of tiny probability \(\delta\), compute \(p\) exactly by brute force and sample from the law that corrects it. The brute-force branch takes exponential time, but its probability is so small that it adds only a bounded amount to the expected running time. OpenAI carried this out for the switch chain with explicit constants [OpenAI-SW, Section 8]. The expected running time is polynomial; no bound is claimed for every execution.

Throughout, \(n\ge4\) except in Step 0 of the algorithm, and \(\Omega_d\), \(\pi_d\), \(P_d\), \(\gamma_0=\bigl[24n^2\binom n4\bigr]^{-1}\) are as in [The switch chain](the-switch-chain.md).

## 1. Residual mixtures

**Lemma 1.1.** Let \(\pi\) and \(p\) be probability measures on a finite set and \(0<\delta<1\), and suppose that \((1-\delta)p\le\pi\) pointwise. Then
\[
r=\frac{\pi-(1-\delta)p}{\delta}
\]
is a probability measure and \((1-\delta)p+\delta r=\pi\). If \((1-\delta)p(x)>\pi(x)\) for some \(x\), no probability measure \(r\) satisfies \((1-\delta)p+\delta r=\pi\).

**Proof.** The hypothesis gives \(r\ge0\), and \(\sum r=(1-(1-\delta))/\delta=1\); the identity is the definition of \(r\). Conversely, \((1-\delta)p(x)+\delta r(x)\ge(1-\delta)p(x)>\pi(x)\) for every probability measure \(r\). \(\square\)

So the sampler needs a law \(p\) that it can sample from quickly and that satisfies \((1-\delta)p\le\pi_d\), and an exact description of \(r\) on the rare branch.

## 2. Parameters

For \(n\ge4\) let
\[
B=\binom n2,\qquad q=12\binom n4,\qquad D=4B+10,\qquad\delta=2^{-D},\qquad t=\bigl\lceil\gamma_0^{-1}(B+2D+2)\bigr\rceil ,
\]
and let \(M=|\Omega_d|\le2^B\). All these numbers except \(M\) are computed from \(n\) in polynomial time, and \(D=O(n^2)\), \(t=O(n^8)\). Let \(G_0\in\Omega_d\) be the graph of the greedy prescription of Lemma 3.1 of [The switch chain](the-switch-chain.md), and let
\[
p_G=P_d^t(G_0,G)\qquad(G\in\Omega_d)
\]
be the law of the chain after \(t\) steps from \(G_0\).

**Lemma 2.1.** \((1-\delta)\,p_G\le\frac1M\) for every \(G\in\Omega_d\).

**Proof.** If \(M=1\), then \(p_G=1\). Let \(M>1\). By the mixing theorem, the eigenvalues of \(P_d\) on functions with mean zero lie in \([0,1-\gamma_0]\), so Lemma 1.1 of [The switch chain](the-switch-chain.md) gives
\[
\|p-\pi_d\|_{\mathrm{TV}}\le\tfrac12\sqrt M\,\mathrm e^{-\gamma_0t}\le\tfrac12\,2^{B/2}\,\mathrm e^{-(B+2D+2)}\le2^{-2D}=\delta^2,
\]
where the last step uses \(2<\mathrm e\) (Exercise 5.3). Hence \(p_G\le\frac1M+\delta^2\) for every \(G\). Since \(D\ge B\), we have \(\delta\le2^{-B}\le\frac1M\), so \((1-\delta)\delta^2\le\delta^2\le\frac{\delta}M\) and
\[
(1-\delta)p_G\le\frac{1-\delta}M+(1-\delta)\delta^2\le\frac{1-\delta}M+\frac\delta M=\frac1M .\qquad\square
\]

## 3. The law of the chain in integers

**Lemma 3.1.** The matrix \(A=qP_d\) on \(\Omega_d\) has nonnegative integer entries and row sums \(q\): \(A(G,G')=1\) for switch neighbours \(G\neq G'\), \(A(G,G')=0\) for other \(G'\neq G\), and \(A(G,G)\) is \(q\) minus the number of switch neighbours of \(G\). Let \(a^{(0)}\) be the indicator vector of \(G_0\) and \(a^{(s+1)}=a^{(s)}A\). Then \(a^{(s)}\) has nonnegative integer entries with sum \(q^s\), and
\[
p_G=\frac{a^{(t)}_G}{q^t}.
\]

**Proof.** Lemma 2.1 of [The switch chain](the-switch-chain.md) gives \(qP_d(G,G')=1\) for switch neighbours and \(0\) for other \(G'\neq G\); the diagonal entry of a row of \(P_d\) is \(1\) minus the others, so \(A(G,G)=q-\#\{\text{switch neighbours of }G\}\), an integer, and it is nonnegative because \(P_d(G,G)\ge0\). Induction on \(s\) gives integrality and \(\sum_Ga^{(s)}_G=q^s\), and \(a^{(s)}=q^s\,P_d^s(G_0,\cdot)\). \(\square\)

In particular every entry of \(a^{(s)}\) is at most \(q^s\) and has \(O(s\log q)\) bits.

## 4. The algorithm

*Uniform integers.* To draw a uniform element of \(\{0,\dots,K-1\}\) for an integer \(K\ge1\), let \(k=\lceil\log_2K\rceil\), read \(k\) fresh random bits as an integer \(y\in\{0,\dots,2^k-1\}\), output \(y\) if \(y<K\), and otherwise repeat. Every attempt succeeds with probability \(K/2^k>\frac12\), so the output is exactly uniform, the procedure stops with probability one, and the expected number of attempts is less than \(2\) (Exercise 5.2).

*Steps of the chain.* One step of \(P_d\) uses one bit to decide whether to stay, and otherwise a uniform integer in \(\{0,\dots,6\binom n4-1\}\), which is decoded into a four-element set \(S\) (by its index in the lexicographic order) and an ordered pair \((F,F')\) of different perfect matchings of \(S\). Testing the four edges and updating the adjacency matrix takes polynomial time.

**The sampler.** Input: a graphical vector \(d=(d_1,\dots,d_n)\).

0. If \(n<4\), list the at most \(2^3\) graphs on \(\{1,\dots,n\}\), keep those with degree vector \(d\), and output a uniform one.
1. Compute \(B,q,D,t\) and the graph \(G_0\) of the greedy prescription.
2. Read \(D\) fresh random bits. If they are not all zero, run \(t\) steps of \(P_d\) from \(G_0\) and output the final graph.
3. If all \(D\) bits are zero: list the \(2^B\) graphs on \(\{1,\dots,n\}\), keep those with degree vector \(d\) (this computes \(M\)), compute \(a=a^{(t)}\) by Lemma 3.1, form the integers
\[
w_G=2^Dq^t-M(2^D-1)\,a_G\qquad(G\in\Omega_d),\tag{4.1}
\]
draw a uniform integer \(y\in\{0,\dots,Mq^t-1\}\), and output the graph \(G\) whose interval in the list of cumulative sums of the \(w_G\) contains \(y\).

**Theorem 4.1** (OpenAI 2026). The sampler outputs an exactly uniform element of \(\Omega_d\), stops with probability one, and its expected number of bit operations is at most a fixed polynomial in \(n\), hence in the length of the input.

**Proof.** *Correctness.* For \(n<4\) this is clear. For \(n\ge4\), the branch of step 2 is taken with probability \(1-\delta\) and outputs a graph with law \(p\). On the branch of step 3, the weights (4.1) satisfy
\[
\frac{w_G}{Mq^t}=\frac{2^D}M-(2^D-1)p_G=\frac{\frac1M-(1-\delta)p_G}{\delta},
\]
which is nonnegative by Lemma 2.1, and \(\sum_Gw_G=Mq^t\) because \(\sum_Ga_G=q^t\). So step 3 outputs a graph with law \(r=(\pi_d-(1-\delta)p)/\delta\), and by Lemma 1.1 the output of the sampler has law \((1-\delta)p+\delta r=\pi_d\).

*Termination.* Each branch performs finitely many uniform-integer draws, each of which stops with probability one, and otherwise finitely many deterministic operations.

*Expected cost.* Steps 0–2 cost polynomially many bit operations in expectation: \(t=O(n^8)\) steps of the chain, each with expected polynomial cost. In step 3, listing the graphs and testing their degrees costs \(2^B\operatorname{poly}(n)\); the propagation of Lemma 3.1 performs at most \(tM^2\le t\,2^{2B}\) multiplications and additions of integers with \(O(t\log q)\) bits; the weights have \(O(D+t\log q+B)\) bits; and the final draw and search cost \(M\operatorname{poly}(n)\) in expectation. So step 3 costs at most \(2^{2B}\operatorname{poly}(n)\) in expectation, and it is executed with probability \(\delta=2^{-4B-10}\). Its contribution to the expected cost is at most \(2^{-2B-10}\operatorname{poly}(n)\le\operatorname{poly}(n)\). The input lists \(n\) numbers, so its length is at least \(n\). \(\square\)

The correction branch takes exponential time when it occurs, and the uniform-integer draws have unbounded running time with tiny probability; the theorem bounds the expectation only.

## 5. Exercises

**Exercise 5.1** (easy). Why must the random bits used after the branch decision be fresh, rather than include the \(D\) bits that decided the branch?

**Exercise 5.2** (easy). Show that the uniform-integer procedure of Section 4 outputs each element of \(\{0,\dots,K-1\}\) with probability exactly \(1/K\), and that its expected number of attempts is \(2^k/K<2\) when \(K\) is not a power of two.

**Exercise 5.3** (easy). Show that \(\frac12\,2^{B/2}\mathrm e^{-(B+2D+2)}\le2^{-2D}\) for all \(B,D\ge0\).

**Exercise 5.4** (medium). Let \(n=4\) and \(d=(1,1,1,1)\). Compute \(P_d^t(G_0,\cdot)\) for every \(t\), and check Lemma 2.1 directly for the value of \(t\) used by the sampler.

## 6. Solutions

**5.1.** The output law is the mixture \((1-\delta)p+\delta r\) only if, on each branch, the remaining computation has the law it would have unconditionally. Given the branch, the \(D\) bits are not uniform: on the branch of step 2 they are known not to be all zero, and on the branch of step 3 they are all zero. Bits reused from them would bias the chain's moves or the final draw; fresh bits are independent of the branch decision.

**5.2.** Each attempt produces a uniform \(y\in\{0,\dots,2^k-1\}\); conditioned on \(y<K\) it is uniform on \(\{0,\dots,K-1\}\), and the attempts are independent, so the output is uniform. The number of attempts is geometric with success probability \(K/2^k\), which exceeds \(\frac12\) because \(2^{k-1}<K\) when \(K\) is not a power of two; its mean is \(2^k/K<2\).

**5.3.** The inequality is \(2^{B/2+2D-1}\le\mathrm e^{B+2D+2}\). Since \(B/2+2D-1\le B+2D+2\) and \(2<\mathrm e\), the left side is at most \(2^{B+2D+2}\le\mathrm e^{B+2D+2}\).

**5.4.** Here \(\Omega_d\) consists of the three perfect matchings, \(P_d(G,G)=\frac56\) and \(P_d(G,G')=\frac1{12}\) for \(G\neq G'\), and \(P_d\) acts by \(\frac34\) on functions with mean zero. Hence \(P_d^t(G_0,G_0)=\frac13+\frac23\bigl(\frac34\bigr)^t\) and \(P_d^t(G_0,G)=\frac13-\frac13\bigl(\frac34\bigr)^t\) for \(G\neq G_0\). The sampler uses \(B=6\), \(D=34\), \(\gamma_0^{-1}=384\) and \(t=384\cdot76=29184\). Lemma 2.1 asks for \((1-\delta)\bigl(\frac13+\frac23(\frac34)^t\bigr)\le\frac13\), that is, \(2(1-\delta)(\frac34)^t\le\delta=2^{-34}\), which holds because \((\frac34)^{29184}<2^{-12000}\).

## References

- [OpenAI-SW] OpenAI, *Polynomial mixing of the switch chain for every graphical degree sequence*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026
- [GLMP] A. Göbel, J. Liu, P. Manurangsi and M. Pappik, *Perfect sampling from rapidly mixing Markov chains*, 2024. https://arxiv.org/abs/2410.00882
