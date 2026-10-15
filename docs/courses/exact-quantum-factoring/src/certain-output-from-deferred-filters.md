# Certain output from deferred filters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

One step of amplitude amplification [BHMT 2002, Section 2] turns a success probability of exactly \(\frac14\) into certainty (Lemma 4.1 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md)). Mosca and Zalka used this for exact Fourier transforms, reducing a known success probability to \(\frac14\) [Mosca–Zalka 2004, Section 2.1], and they noted that the success probability must be known in advance although it may depend on the unknown instance. The process of [Factoring with verifiable auxiliary data](factoring-with-verifiable-auxiliary-data.md) has such instance-dependent probabilities: each of its transitions has a good output with a probability \(s\ge1-2^{-2n}\) that is computed from the data \(\mathcal D(N)\), which are known only after a completed run. This lesson uses the data after they have been generated [OpenAI-EQF, Section 5]. Every transition is first corrected to the same passing probability \(z\), so that a run passes all its \(L\) transitions with the known probability \(z^L\); a second correction brings the probability to exactly \(\frac14\); and one amplification step gives the factorization with certainty. This proves Theorem 5.1 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md).

- Equalizing one transition (Section 1).
- Filters computed after completion (Section 2).
- A known quarter of success (Section 3).
- Proof of the theorem (Section 4).

We keep the notation of the previous lesson: for an input \(N\ge2\), \(n=\max\{128,\lfloor\log_2N\rfloor+1\}\), \(B=2^n\), \(K=n^5\), \(L=n^{10}\) and \(W=n(K+1)\). To *retain* an event with a dyadic probability \(q\) means, as in Section 3 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md), to append a flag that is \(1\) with probability exactly \(q\) and to require it for success.

## 1. Equalizing one transition

**Lemma 1.1** (dyadic completion; [OpenAI-EQF, Lemma 5.1]). Let \(W\ge0\) and \(t\ge1\) be integers, \(\delta=2^{-t}\), and consider a transition with outputs in \(\{0,1\}^W\), a set of good outputs that it returns with a dyadic probability \(0<s\le1\), and a good output \(y_0\). Let \(z\) be a dyadic rational with
\[
0<z\le A:=(1-\delta)s ,
\]
put \(E=W+t+2\), and
\[
\begin{gathered}C=2^{-E}\Bigl\lfloor2^E\frac zA\Bigr\rfloor,\\ R=z-CA .\end{gathered}\tag{1.1}
\]
With probability \(1-\delta\) run the transition, require a good output and retain with probability \(C\); otherwise, with probability \(\delta\), guess a uniform output \(y\in\{0,1\}^W\), require \(y=y_0\) and retain with probability \(R2^W/\delta\). Then \(C\) and \(R2^W/\delta\) are dyadic rationals in \([0,1]\), and the probability of passing is exactly \(z\).

*Proof.* Since \(z/A\le1\), \(0\le C\le1\). Rounding down gives \(0\le z/A-C<2^{-E}\), so
\[
\begin{aligned}0\le R&=A\Bigl(\frac zA-C\Bigr)\\&<A\,2^{-E}\le2^{-E},\\ 0\le\frac{R2^W}\delta&<2^{-E+W+t}=\frac14 .\end{aligned}
\]
The ordinary branch passes with probability \((1-\delta)\,s\,C=AC\), and the guessing branch with probability \(\delta\cdot2^{-W}\cdot R2^W/\delta=R\). The sum is \(AC+R=z\). The number \(z/A\) need not be dyadic, but \(\lfloor2^Ez/A\rfloor\) is an integer division of integers; \(C\), \(R\) and \(R2^W/\delta\) are dyadic. \(\square\)

The ordinary branch alone cannot pass with probability exactly \(z\), since \(z/A\) need not be dyadic (Exercise 5.2). The remainder \(R\) left by rounding down is supplied by the rare guessing branch, which passes only on the one string \(y_0\). This string need not be known when the guess is made, because the test can be applied later.

## 2. Filters computed after completion

Put
\[
\begin{gathered}\delta=2^{-2n},\quad z=1-2^{-n},\\ E=W+2n+2 .\end{gathered}\tag{2.1}
\]
For every transition of a run of the process, Proposition 4.1(2) of [Factoring with verifiable auxiliary data](factoring-with-verifiable-auxiliary-data.md) gives \(s\ge1-2^{-2n}\). With \(\varepsilon=2^{-n}\),
\[
\begin{aligned}(1-\delta)s&\ge(1-\varepsilon^2)^2\\&=1-\varepsilon+\bigl(\varepsilon-2\varepsilon^2+\varepsilon^4\bigr)\\&>1-\varepsilon=z ,\end{aligned}
\]
since \(\varepsilon\le\frac12\). So the hypothesis \(z\le A\) of Lemma 1.1 holds at every transition, with \(t=2n\).

*The preparation.* Run the controller of the process. Whenever it requests a transition, which we call a *slot*, record its input; then with \(2n\) fair coins choose the guessing branch with probability \(\delta\) (all coins zero) and the ordinary branch otherwise; in the ordinary branch run the transition, in the guessing branch draw a uniform string \(y\in\{0,1\}^W\); record the branch and the output, which the controller reads in the usual way; and draw a fresh uniform string \(u\) of \(T_0=E+2n+(n+10)K\) bits for the filter of this slot, read as an integer in \([0,2^{T_0})\). The controller cannot distinguish a guessed output from a returned one; a malformed output makes it abort, and a divisor is used only after it has been checked.

When the controller stops, or aborts, the preparation does the following. If the controller aborted, or the verifier of Proposition 4.1(1) rejects its record, the success flag is \(0\). Otherwise the record is \(\mathcal D(N)\), and for every slot the preparation computes from \(\mathcal D(N)\) and the recorded input the good outputs, the canonical output \(y_0\) and the probability \(s\) (Proposition 4.1(2)), and then \(C\) and \(R\) by (1.1). The slot *passes* if it was ordinary with a good output and \(u<C\,2^{T_0}\), or a guess with \(y=y_0\) and \(u<(R2^W/\delta)\,2^{T_0}\). The success flag is \(1\) if all \(L\) slots pass. The output register receives the prime factorization of \(N\) from the root of the record.

**Proposition 2.1** (known probability; [OpenAI-EQF, Proposition 5.2]). The preparation has success probability exactly
\[
p_*=\bigl(1-2^{-n}\bigr)^{n^{10}} ,
\]
and on success its output is the prime factorization of \(N\). It is a procedure of the kind in Lemma 3.2 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md), with a polynomial bound on its steps and storage; so it is a polynomial-size uniform circuit over \(\mathcal G\) with the same distribution of its classical data, whose inverse is a circuit over \(\mathcal G\). The number \(p_*>\frac12\) is a dyadic rational of polynomial bit length, computed before the preparation runs.

*Proof.* *An event defined with the true data.* For the analysis only, fix the true data \(\mathcal D(N)\). Let \(\mathsf A\) be the following event of a run: the controller requests \(L\) slots, and each slot \(i\) passes the test of the preparation computed with \(\mathcal D(N)\) and the recorded input of slot \(i\), immediately when slot \(i\) has been recorded, with the same branch, output and string \(u\). These tests only mark the event; they do not change the run.

*Its probability.* Fix \(0\le i<L\) and a record of the first \(i\) slots (inputs, branches, outputs and strings \(u\)) on which these \(i\) slots pass; such records are disjoint events. A slot passes only with a good output, \(y_0\) being good. So the outputs \(y_1,\ldots,y_i\) are good, and extending them by canonical outputs gives a sequence as in Proposition 4.1(3) of [Factoring with verifiable auxiliary data](factoring-with-verifiable-auxiliary-data.md); along it the controller does not abort and requests \(L\) slots. What the controller does before its next request depends only on \(y_1,\ldots,y_i\), so on the given record it requests slot \(i+1\), with an input determined by the record. Slot \(i+1\) works on fresh registers, so by Lemma 3.3 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md), on this record its output is good with probability exactly \(s\), even though older registers may be entangled with each other. Its branch coins, its guess and its string \(u\) are fresh, and \(u<q\,2^{T_0}\) has probability \(q\) for a dyadic \(q\) with denominator dividing \(2^{T_0}\). By Lemma 1.1, slot \(i+1\) passes with probability exactly \(z\) on this record. By induction on \(i\), \(\Pr(\mathsf A)=z^L=p_*\).

*\(\mathsf A\) is the success event.* Suppose \(\mathsf A\) holds. Then all outputs are good, and by Proposition 4.1(3) the controller does not abort and stops with \(\mathcal D(N)\), which the verifier accepts. The deferred tests then use the true data, and they are the tests of \(\mathsf A\), with the same outputs and strings \(u\); so the success flag is \(1\). Conversely, if the success flag is \(1\), the controller did not abort and the verifier accepted its record, which is therefore \(\mathcal D(N)\) by Proposition 4.1(1). So the deferred tests are those of \(\mathsf A\), and \(\mathsf A\) holds. The two events coincide on every run, so the success probability is \(p_*\). The computation of \(\Pr(\mathsf A)\) never conditions on the completion of the run, and the preparation never uses data that it has not generated and verified.

*The circuit.* Every step of the preparation is a gate of \(\mathcal G\) chosen by classical data, a measurement, or a polynomial-time classical computation; the order trials are such procedures by [An order trial with prescribed probability](an-order-trial-with-prescribed-probability.md). By Proposition 4.1(3) the controller's work is polynomial for every sequence of outputs, the \(L\) transitions have polynomial size, and the verifier and the computations of \(s\), \(y_0\), \(C\) and \(R\) are polynomial. Since \(s\) has a denominator dividing \(2^{(n+10)K}\) (Lemma 5.1 of [Factoring with verifiable auxiliary data](factoring-with-verifiable-auxiliary-data.md)), \(A=(1-\delta)s\) has one dividing \(2^{2n+(n+10)K}\), so \(C\), \(R\) and \(R2^W/\delta\) have denominators dividing \(2^{T_0}\). Lemma 3.2 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md) gives the circuit; as the success flag is a function of the classical data, its probability is \(p_*\).

*The number \(p_*\).* \(p_*=(2^n-1)^{n^{10}}/2^{n^{11}}\) is computed exactly by integer powering. By Bernoulli's inequality, \(p_*\ge1-n^{10}2^{-n}\). At \(n=128\) the subtracted term is \(2^{70-128}=2^{-58}\), and \(x^{10}2^{-x}\) decreases for \(x\ge128\), since the derivative of its logarithm is \(10/x-\ln2<0\). So \(p_*>\frac12\). \(\square\)

There is no exception for runs that finish early: a run that completes after \(t\) list and order transitions has \(L-t\) dummy slots, each with \(s=1\) and the zero string as \(y_0\), and each of them passes with probability \(z\) as well. For \(N=2\) all slots are dummy slots, while a prime root \(N>2\) first generates the occurrence tree of \(N-1\).

## 3. A known quarter of success

Encode a prime factorization of \(N\) by \(n\) entries of \(n\) bits: the primes in nondecreasing order with multiplicity, followed by zeros. Put \(J=n^2\). Since \(N<2^n\), \(N\) has fewer than \(n\) prime factors with multiplicity, each less than \(2^n\), so exactly one \(J\)-bit string, the *valid* one, encodes the factorization of \(N\). For an arbitrary \(J\)-bit string, the primality test of [A deterministic primality test](a-deterministic-primality-test.md) for the nonzero entries, the order of the entries and the product of the entries decide in polynomial time whether it is valid; the product of \(n\) entries has at most \(n^2\) bits.

**Lemma 3.1** (a quarter of success; [OpenAI-EQF, Lemma 5.3]). There is a polynomial-size uniform circuit \(V_N\) over \(\mathcal G\), whose inverse is a circuit over \(\mathcal G\), such that for \(\psi=V_N|0\rangle\) the success flag is \(1\) with probability exactly \(\frac14\), and every computational basis state with success flag \(1\) that occurs in \(\psi\) holds the valid string in the output register.

*Proof.* With one fair coin choose one of two branches. In the first, run the preparation of Proposition 2.1 and retain its success with probability
\[
c_*=2^{-(J+2)}\Bigl\lfloor\frac{2^{J+2}}{2p_*}\Bigr\rfloor .
\]
In the second, guess a uniform \(J\)-bit string, require it to be valid, and retain with probability \(2^{J+1}e\), where
\[
e=\frac14-\frac{p_*c_*}2 .
\]
As \(\frac12<p_*\le1\), \(\frac1{2p_*}<1\) and \(0\le c_*\le1\). Rounding down gives \(0\le\frac1{2p_*}-c_*<2^{-(J+2)}\), so
\[
\begin{aligned}0\le e&=\frac{p_*}2\Bigl(\frac1{2p_*}-c_*\Bigr)\\&<p_*\,2^{-(J+3)},\\ 0\le2^{J+1}e&<\frac{p_*}4\le\frac14 .\end{aligned}
\]
Both retention probabilities are dyadic rationals of polynomial bit length. The first branch succeeds with probability \(\frac12p_*c_*\), and the second with probability \(\frac12\cdot2^{-J}\cdot2^{J+1}e=e\), since exactly one string is valid. The total is \(\frac12p_*c_*+e=\frac14\). On success the output register holds the valid string: in the first branch by Proposition 2.1, in the second because the guess is the valid string. All records and work registers are kept, and Lemma 3.2 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md) gives \(V_N\) and its inverse. \(\square\)

## 4. Proof of the theorem

*Proof of Theorem 5.1 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md).* Let \(N\ge2\) have \(\ell\) bits. Then \(n=\max\{128,\ell\}\), and all the parameters above depend only on \(\ell\). Let \(V_N\) be the circuit of Lemma 3.1, \(\psi=V_N|0\rangle\), and \(\Pi\) the projection onto the states with success flag \(1\), so that \(\|\Pi\psi\|^2=\frac14\). Apply the sign \(I-2\Pi\) and then the reflection \(2|\psi\rangle\langle\psi|-I=V_N(2|0\rangle\langle0|-I)V_N^{-1}\). By Lemma 4.1 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md), the result is the unit vector \(2\Pi\psi\). It is a combination of the basis states with success flag \(1\) that occur in \(\psi\), so by Lemma 3.1 a measurement of the output register returns the valid string, the prime factorization of \(N\), with probability one.

The sign \(I-2\Pi\) is the sign of a bit test, and \(2|0\rangle\langle0|-I\) is \(-1\) times the sign of the test that all qubits of the work registers are zero; both are circuits over \(\mathcal G\) by Lemma 2.3(1) of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md), and the factor \(-1\) changes no probability. For inputs of \(\ell\) bits, the circuit holds the input in its input qubits, which only control the operations and are never changed, and the reflection acts on the work registers. Inverting \(V_N\) also returns all its records and work registers to zero, so nothing needs to be erased separately. The circuit consists of three copies of \(V_N\) or its inverse and two signs, so it has polynomial size and is written down in polynomial time from \(\ell\). No rotation by a computed angle and no repetition until success occurs. \(\square\)

## 5. Exercises

**5.1.** In Lemma 1.1 take \(W=1\), \(t=1\), \(s=\frac34\) and \(z=\frac14\). Compute \(A\), \(E\), \(C\), \(R\) and the two retention probabilities, and check that the probability of passing is \(\frac14\).

**5.2.** In Exercise 5.1 the quotient \(z/A\) is \(\frac23\). Why can the ordinary branch not simply be retained with probability \(z/A\)?

**5.3.** Show that \((1-\varepsilon^2)^2\ge1-\varepsilon\) for \(0\le\varepsilon\le\frac12\).

**5.4.** Describe the runs of the preparation of Proposition 2.1 for \(N=2\), and compute the probability that a given slot passes.

**5.5.** Carry out the construction of Lemma 3.1 with the values \(p_*=\frac34\) and \(J=2\) in place of the true ones: compute \(c_*\), \(e\) and the two branch contributions.

## 6. Solutions

**5.1.** \(A=\frac12\cdot\frac34=\frac38\), \(E=1+1+2=4\), \(z/A=\frac23\), \(C=\frac1{16}\lfloor\frac{32}3\rfloor=\frac{10}{16}=\frac58\), \(R=\frac14-\frac58\cdot\frac38=\frac{16-15}{64}=\frac1{64}\), and the guess is retained with probability \(R2^W/\delta=\frac1{64}\cdot2\cdot2=\frac1{16}\le\frac14\). The ordinary branch passes with probability \(AC=\frac{15}{64}\) and the guess with probability \(\frac12\cdot\frac12\cdot\frac1{16}=\frac1{64}\), in total \(\frac{16}{64}=\frac14\).

**5.2.** The probability of an outcome of a circuit over \(\mathcal G\) applied to a basis state is a dyadic rational (Exercise 6.1 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md)), and \(\frac23\) is not dyadic.

**5.3.** \((1-\varepsilon^2)^2-(1-\varepsilon)=\varepsilon-2\varepsilon^2+\varepsilon^4\), and this equals \(\varepsilon(1-2\varepsilon)+\varepsilon^4\ge0\).

**5.4.** \(\mathcal D(2)\) is a single node, as \(2\) is prime, so the controller requests no list or order transitions and all \(L\) slots are dummy slots, with \(s=1\) and \(y_0\) the zero string. A slot passes with probability \((1-\delta)C+R=z\), and the run succeeds with probability \(z^L=p_*\).

**5.5.** \(\frac1{2p_*}=\frac23\), \(c_*=\frac1{16}\lfloor\frac{32}3\rfloor=\frac58\), \(e=\frac14-\frac12\cdot\frac34\cdot\frac58=\frac1{64}\), and the guess is retained with probability \(2^{J+1}e=\frac18\). The first branch contributes \(\frac12\cdot\frac34\cdot\frac58=\frac{15}{64}\), the second \(e=\frac1{64}\), in total \(\frac14\).

## References

- [OpenAI-EQF] OpenAI, *Exact quantum factoring over a fixed finite gate set*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
- [Mosca–Zalka 2004] M. Mosca, C. Zalka, *Exact quantum Fourier transforms and discrete logarithm algorithms*, Int. J. Quantum Inf. 2 (2004), no. 1, 91–100. https://arxiv.org/abs/quant-ph/0301093
- [BHMT 2002] G. Brassard, P. Høyer, M. Mosca, A. Tapp, *Quantum amplitude amplification and estimation*, Contemp. Math. 305 (2002), 53–74. https://arxiv.org/abs/quant-ph/0005055
