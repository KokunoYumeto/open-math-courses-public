# A tournament with probabilistic comparisons

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Among \(m\) candidates there may be one that beats every other candidate in a comparison, with high probability. The comparisons between the other candidates may have any probabilities. This lesson shows how a quantum algorithm finds such a dominant candidate with about \(\sqrt m\) comparisons, and applies this to the function \(F_{k,m}\): the candidates are the columns, a winner is dominant, and the candidates found are checked by a quantum search among the local tests. The result is \(Q(F_{k,m})\le C_k\sqrt m\,(\log_2m)^4\).

- Weights, pivots, and the halving of the total weight (Lemmas 1.1 and 1.2).
- The tournament (Proposition 2.1).
- The comparison of two columns; a winner is dominant (Lemma 3.1).
- Checking a candidate (Lemma 4.1).
- The quantum algorithm for \(F_{k,m}\) (Theorem 5.1).

The lesson follows [OpenAI-Q, Sections 3.2 and 3.3]. It uses the function \(F_{k,m}\) and its local tests from [Query complexity and a function with outward pointers](query-complexity-and-a-function-with-outward-pointers.md), the model and the two rules for probabilities from [The quantum query model](the-quantum-query-model.md), and amplification and the address circuit \(\mathrm{Adr}_\varepsilon\) from [Amplitude amplification and the Forrelation test](amplitude-amplification-and-the-forrelation-test.md).

## 1. Weights and pivots

Let \(m\ge2\), and let \(a_{ij}\), \(1\le i,j\le m\), be real numbers with
\[
\begin{gathered}
0\le a_{ij}\le1,\qquad a_{ii}=0,\\
a_{ij}+a_{ji}=1\quad\text{for }i\ne j .
\end{gathered}
\]
We read \(a_{ij}\) as the probability that the candidate \(i\) defeats the candidate \(j\) in a comparison.

**The ideal process.** Every candidate has a *weight* \(w_i\ge0\); at the start all weights are \(1\). Let \(W=\sum_iw_i\). A *step* does the following if \(W>0\): it chooses a *pivot* \(p\) with the probability \(w_p/W\), appends it to a list, and replaces every weight \(w_i\) by \(w_ia_{ip}\). If \(W=0\), the step does nothing. After the pivots \(p_1,\dots,p_t\) the weight of \(i\) is
\[
w_i=\prod_{b=1}^ta_{ip_b},
\]
the probability that \(i\) defeats all pivots in independent comparisons. A pivot has the weight \(0\) from then on, because \(a_{pp}=0\).

**Lemma 1.1.** Let \(W\) be the total weight before a step and \(W'\) the total weight after it. Then the conditional mean of \(W'\), given the weights before the step, is at most \(W/2\). So after \(T\) steps the mean of the total weight is at most \(m/2^T\).

**Proof.** For \(W>0\) the conditional mean is
\[
\begin{aligned}
&\sum_p\frac{w_p}W\sum_iw_ia_{ip}\\
&\quad=\frac1W\sum_{i<p}w_iw_p\,(a_{ip}+a_{pi})\\
&\quad=\frac{W^2-\sum_iw_i^2}{2W}\le\frac W2 ,
\end{aligned}
\]
because the terms with \(i=p\) are \(0\) and \(\sum_{i<p}w_iw_p=\tfrac12(W^2-\sum_iw_i^2)\). For \(W=0\) both sides are \(0\). The second statement follows by induction, since the mean of a conditional mean is the mean. \(\blacksquare\)

The proof uses only \(a_{ij}+a_{ji}=1\). No order among the candidates is assumed: \(i\) may defeat \(j\), \(j\) defeat \(k\) and \(k\) defeat \(i\), and the probabilities may be anything between \(0\) and \(1\).

**Lemma 1.2.** Let \(T\ge1\) and \(0<\varepsilon\le\tfrac1{2T}\). Let \(i_*\) be a candidate with \(a_{i_*j}\ge1-\varepsilon\) for all \(j\ne i_*\). Then:

1. as long as \(i_*\) is not a pivot, its weight is at least \(\tfrac12\) during the first \(T\) steps;
2. the probability that \(i_*\) is not among the first \(T\) pivots is at most \(2m/2^T\).

**Proof.** 1: after \(t\le T\) pivots different from \(i_*\) the weight of \(i_*\) is at least \((1-\varepsilon)^t\ge1-T\varepsilon\ge\tfrac12\). 2: if \(i_*\) is not among the pivots, the total weight after \(T\) steps is at least \(\tfrac12\). By Lemma 1.1 and Markov's inequality this has a probability of at most \(2m/2^T\). \(\blacksquare\)

So a dominant candidate is chosen as a pivot within about \(\log_2m\) steps: as long as it is not chosen, it keeps its weight, while the total weight is halved on average at each step.

## 2. The tournament

A *comparison* is a query circuit \(\mathrm{Cmp}\) that is controlled by two registers with the labels \(\{1,\dots,m\}\) and acts on further registers, one of which is a bit called the *result*; the further registers start in \(|0\rangle\). For \(i,j\) let \(a_{ij}\) be the probability that the result is \(1\) after \(\mathrm{Cmp}\) is applied to \(|i\rangle|j\rangle|0\rangle\). These numbers depend on the input \(x\).

**Proposition 2.1** ([OpenAI-Q]). Let \(m\ge2\),
\[
T=\lceil\log_2(1000m)\rceil,\qquad\varepsilon=\frac1{1000T}.
\]
Let \(\mathrm{Cmp}\) be a comparison with at most \(c\) queries such that for every input the numbers \(a_{ij}\) satisfy \(a_{ij}+a_{ji}=1\) for \(i\ne j\) and \(a_{ii}=0\). There is a procedure with at most
\[
63\,c\,\sqrt m\;T^2\log_2(1000T)
\]
queries on every path that returns a list of at most \(T\) candidates, such that for every input: if a candidate \(i_*\) satisfies \(a_{i_*j}\ge1-\varepsilon\) for all \(j\ne i_*\), the list contains \(i_*\) with a probability of at least
\[
1-\frac{2m}{2^T}-T\varepsilon\ \ge\ 1-\frac3{1000}.
\]

**Proof.** *The preparation for given pivots.* Let \(p_1,\dots,p_t\) be candidates, \(0\le t<T\). The preparation \(A=A_{p_1,\dots,p_t}\) has a *candidate register* with the labels \(\{1,\dots,m\}\), \(t\) groups of registers for comparisons, and a success bit. It prepares \(m^{-1/2}\sum_i|i\rangle\) in the candidate register. For \(b=1,\dots,t\) it applies \(\mathrm{Cmp}\) to the candidate register, a register in the state \(|p_b\rangle\), and the \(b\)-th group. Then a permutation map sets the success bit to \(1\) if all \(t\) results are \(1\). It has at most \(ct\) queries.

All this is controlled by the candidate register, and the groups are separate. By the two rules for probabilities, a measurement of the candidate register and the success bit gives the candidate \(i\) together with success with the probability
\[
\frac1m\prod_{b=1}^ta_{ip_b}=\frac{w_i}m ,
\]
where \(w_i\) is the weight of \(i\) in the ideal process after the pivots \(p_1,\dots,p_t\). So the success probability of \(A\) is \(W/m\), and if \(W>0\), a measurement of the candidate register in the successful state gives \(i\) with the probability \(w_i/W\). This is the distribution of the next pivot of the ideal process.

*The procedure.* Start with the empty list. For \(t=0,1,\dots,T-1\): apply the amplification of Lemma 1.2 of the lesson on amplification to \(A_{p_1,\dots,p_t}\), with \(\gamma=\tfrac1{2m}\) and \(\eta=\varepsilon\). If it ends with failure, return the list. If it ends with success, measure the candidate register, call the outcome \(p_{t+1}\), and append it to the list.

*Comparison with the ideal process.* Let \(h=(p_1,\dots,p_t)\) be a sequence without \(i_*\), with \(t<T\). By Lemma 1.2 the weight of \(i_*\) after \(h\) is at least \(\tfrac12\), so the success probability of \(A_h\) is at least \(\tfrac1{2m}=\gamma\). So, if the procedure has produced \(h\): the amplification fails with a probability \(\phi(h)\le\varepsilon\); and by property 3 of amplification the next pivot is \(p\) with the probability \((1-\phi(h))\,w_p/W\).

Hence, by induction on \(t\): the probability that the procedure produces a list that begins with a given sequence \(h\) without \(i_*\) is at most the probability that the ideal process begins with \(h\). With \(t=T\) and Lemma 1.2: the probability that the procedure makes \(T\) pivots, none of them \(i_*\), is at most \(2m/2^T\).

The other way to miss \(i_*\) is that an amplification fails after a sequence \(h\) without \(i_*\). For each of the \(T\) stages this has a probability of at most \(\varepsilon\). Together the probability that the list does not contain \(i_*\) is at most \(2m/2^T+T\varepsilon\), and \(2m/2^T\le\tfrac2{1000}\), \(T\varepsilon=\tfrac1{1000}\).

*Queries.* The stage \(t\) makes at most \(88\,ct\,\sqrt{2m}\,\log_2(1/\varepsilon)\) queries, and \(\sum_{t<T}t\le T^2/2\). \(\blacksquare\)

The proposition holds for every input, whether a dominant candidate exists or not; if there is none, the procedure still returns some list within the same number of queries. Property 3 of amplification is essential: the pivots must have exactly the distribution given by the weights, although the weights are never computed. They are probabilities of events inside the superposition.

## 3. Comparing two columns

Fix \(k\ge2\) and a power of four \(m\ge4\), and let \(\ell,r,S,K\) be as in the first lesson. Let \(T\) and \(\varepsilon\) be as in Proposition 2.1. The input \(x\) of \(F_{k,m}\) is arbitrary.

**The comparison.** Let \(i\ne j\) be the contents of the two control registers, and let \(i_1<i_2\) be these two columns in increasing order.

1. Apply \(\mathrm{Adr}_\varepsilon\) for the column \(i_1\) to an address register \(s^{(1)}\), and for the column \(i_2\) to a separate address register \(s^{(2)}\).
2. Read the pointer \(p_{i_1,s^{(1)},i_2}\) from the cell \(B_{i_1,s^{(1)}}\) into a register \(\pi^{(1)}\), by \(\ell\) read queries; their positions are functions of \(i_1,i_2\), the address register and the number of the bit. In the same way read \(p_{i_2,s^{(2)},i_1}\) into a register \(\pi^{(2)}\).
3. Read the bit \(X_{i_2}[\pi^{(1)}]\) into a register \(e_1\) and the bit \(X_{i_1}[\pi^{(2)}]\) into a register \(e_2\). We say that \(i_1\) *disqualifies* \(i_2\) if \(e_1=0\): the pointer of \(i_1\) shows a zero of \(X_{i_2}\). In the same way \(i_2\) disqualifies \(i_1\) if \(e_2=0\).
4. The *victor* is the column that disqualifies the other, if exactly one does; otherwise it is \(i_1\). A permutation map sets the result to \(1\) if the victor is \(i\).

For \(i=j\) the circuit does nothing, and the result is \(0\). The circuit has
\[
c=2\,r\,c_k\log_2(r/\varepsilon)+2\ell+2
\]
queries. For \(i\ne j\) the circuits for \((i,j)\) and \((j,i)\) differ only in the last map, which asks whether the victor is \(i\) or \(j\). So \(a_{ij}+a_{ji}=1\) for every input.

**Lemma 3.1.** If the column \(i_*\) is a winner of the input \(x\), then \(a_{i_*j}\ge1-\varepsilon\) for all \(j\ne i_*\).

**Proof.** Steps 2 to 4 are controlled by the two address registers. By Rule 6.1 the result is distributed as if the address registers were measured after step 1 and steps 2 to 4 were carried out for the addresses found.

Whatever address is found for \(j\), the pointer of that cell of \(j\) toward \(i_*\) shows a bit of \(X_{i_*}\), and all these bits are \(1\). So \(j\) does not disqualify \(i_*\).

All \(P(A_{i_*,h})\) are defined. So with a probability of at least \(1-\varepsilon\) the address found for \(i_*\) is the true address \(s_{i_*}\). Then the pointer \(p_{i_*,s_{i_*},j}\) shows a zero of \(X_j\), by the definition of a winner, and \(i_*\) disqualifies \(j\). Then exactly one of the two disqualifies the other, and the victor is \(i_*\). \(\blacksquare\)

The lemma needs nothing about the column \(j\): its strings \(A_{j,h}\) may lie outside the domain of the Forrelation function, and its cells may contain anything. This is the purpose of the outward direction of the pointers. For two columns that are both not winners, the numbers \(a_{ij}\) can have any values.

## 4. Checking a candidate

**Lemma 4.1.** There is a procedure that, for a given column \(i\), ends with *accept* or *reject*, makes at most
\[
r\,c_k\log_2(r/\varepsilon)+88\,(\ell+1)\sqrt K\,\log_2(1/\varepsilon)
\]
queries on every path, and has the following properties for every input: if \(i\) is a winner, it accepts with a probability of at least \(1-\varepsilon\); if \(i\) is not a winner, it accepts with a probability of at most \(\varepsilon\).

**Proof.** *The procedure.* Apply \(\mathrm{Adr}_\varepsilon\) to \(|i\rangle|0\rangle\) and measure the address register; let \(s\) be the outcome. Let \(A_{i,s}\) be the following preparation: prepare \(K^{-1/2}\sum_\tau|\tau\rangle\) in a register with the labels \(\{1,\dots,K\}\), the numbers of the tests for \((i,s)\); carry out the test with the number \(\tau\) in superposition; set the success bit to \(1\) if the test fails. Each test is a decision tree with at most \(\ell+1\) queries, so by Lemma 5.1 of the lesson on the model \(A_{i,s}\) has at most \(\ell+1\) queries. Its success probability is the number of the failing tests divided by \(K\). Apply the amplification to \(A_{i,s}\) with \(\gamma=\tfrac1K\) and \(\eta=\varepsilon\). If it ends with success, reject; if it ends with failure, accept.

*A winner.* With a probability of at least \(1-\varepsilon\), \(s\) is the true address. Then all tests pass (Lemma 6.1 of the first lesson), the success probability of \(A_{i,s}\) is \(0\), the amplification ends with failure, and the procedure accepts.

*Not a winner.* For every address \(s\) some test fails (Corollary 6.2 of the first lesson). So the success probability is at least \(\tfrac1K\), the amplification ends with failure with a probability of at most \(\varepsilon\), and otherwise the procedure rejects. \(\blacksquare\)

The amplification here is a search: among \(K\) tests one that fails is found with about \(\sqrt K\) evaluations of tests. This is where the quantum algorithm gains the second factor \(\sqrt m\) against a classical check of all \(K\ge m\) tests.

## 5. The quantum algorithm

**Theorem 5.1** ([OpenAI-Q]). For every \(k\ge2\) there is a number \(C_k\) such that for all powers of four \(m\ge4\)
\[
Q(F_{k,m})\le C_k\,\sqrt m\,(\log_2m)^4 .
\]

**Proof.** *The algorithm.* Run the procedure of Proposition 2.1 with the comparison of Section 3. For every candidate of the list run the procedure of Lemma 4.1. Output \(1\) if a candidate is accepted, and \(0\) otherwise.

*Inputs with \(F_{k,m}(x)=0\).* No column is a winner. Each of the at most \(T\) candidates is accepted with a probability of at most \(\varepsilon\). The output is \(1\) with a probability of at most \(T\varepsilon=\tfrac1{1000}\).

*Inputs with \(F_{k,m}(x)=1\).* Let \(i_*\) be the winner. By Lemma 3.1 and Proposition 2.1 the list contains \(i_*\) with a probability of at least \(1-\tfrac3{1000}\), and then \(i_*\) is accepted with a probability of at least \(1-\varepsilon\). The output is \(0\) with a probability of at most \(\tfrac4{1000}\).

*Queries.* Write \(\ell=\log_2m\ge2\). Then \(T\le\ell+11\), \(r\le20\ell+1\), \(\tfrac1\varepsilon=1000T\), and \(K\le C_k''\,m\,\ell^3\). In the following, \(O(\cdot)\) hides factors that depend on \(k\) only. We have \(\log_2(1/\varepsilon)=O(\log_2\ell)\) and \(\log_2(r/\varepsilon)=O(\log_2\ell)\), so \(c=O(\ell\log_2\ell)\). The tournament makes
\[
O\bigl(c\,\sqrt m\,T^2\log_2\ell\bigr)=O\bigl(\sqrt m\,\ell^3(\log_2\ell)^2\bigr)
\]
queries. The checks make
\[
\begin{aligned}
&T\cdot O\bigl(\ell\log_2\ell+\ell\sqrt{m\ell^3}\,\log_2\ell\bigr)\\
&\quad=O\bigl(\sqrt m\,\ell^{7/2}\log_2\ell\bigr)
\end{aligned}
\]
queries. Since \((\log_2\ell)^2\le4\ell\), both are \(O(\sqrt m\,\ell^4)\).

*The model.* The algorithm is a measuring algorithm with read queries. By Lemma 4.1 and Theorem 3.2 of the lesson on the model there is a query algorithm with the same number of queries and the same probabilities of the outputs. Its error is at most \(\tfrac4{1000}<\tfrac13\). \(\blacksquare\)

With \(\ell=\log_2m\), the proof gives
\[
Q(F_{k,m})=O\bigl(\sqrt m\,\ell^{7/2}\log_2\ell\bigr),
\]
with a factor that depends on \(k\); it contains the factor \(2^{10k}\) of the Forrelation test. The exponent of the logarithm does not depend on \(k\).

**Where the exponent comes from.** The quantum algorithm needs about \(\sqrt m\) queries: about \(\sqrt m\) comparisons in the tournament, each at the cost of a power of \(\log m\), and then about \(\sqrt m\) tests for each of a few candidates. A randomized algorithm needs about \(m^{2-1/k}\) queries, by the next lesson: it must spend about \(m^{1-1/k}\) queries in a column to learn its address, and it must do this in a fixed fraction of the \(m\) columns. The ratio of the two exponents is \((2-\tfrac1k)/\tfrac12=4-\tfrac2k\).

## 6. Exercises

**6.1.** Let \(m=2\) and \(a_{12}=a\). Compute the mean of the total weight after one step of the ideal process, and compare with Lemma 1.1.

**6.2.** Let all \(a_{ij}\) be \(0\) or \(1\) (a tournament in the usual sense). Describe the weights after the pivots \(p_1,\dots,p_t\). What does Lemma 1.1 say about the number of the candidates that have defeated all pivots?

**6.3.** In the comparison of Section 3, the smaller column is the victor when neither or both columns disqualify the other. Why is some fixed rule needed for these cases, and why does the choice not matter for Lemma 3.1?

**6.4.** Compute \(T\), \(\varepsilon\) and \(r\) for \(m=2^{20}\).

**6.5.** Show that on inputs with \(F_{k,m}(x)=0\) the error bound of the algorithm does not use any property of the tournament.

## 7. Solutions

**6.1.** The pivot is \(1\) or \(2\) with the probability \(\tfrac12\) each. After the pivot \(1\) the weights are \((0,a_{21})=(0,1-a)\); after the pivot \(2\) they are \((a,0)\). The mean of the total weight is \(\tfrac12(1-a)+\tfrac12a=\tfrac12\). Lemma 1.1 gives \(\tfrac{W^2-\sum w_i^2}{2W}=\tfrac{4-2}4=\tfrac12\), with equality.

**6.2.** The weight of \(i\) is \(1\) if \(i\) has defeated all pivots, and \(0\) otherwise. The total weight is the number of the candidates that have defeated all pivots. The pivot is chosen uniformly among them, and by Lemma 1.1 their number is at most halved on average at each step; more precisely its conditional mean is \(\tfrac{W-1}2\).

**6.3.** The numbers must satisfy \(a_{ij}+a_{ji}=1\) for every input, so in every case exactly one of the two columns must be the victor, and the same one for \((i,j)\) and \((j,i)\). In Lemma 3.1 these cases occur for the winner \(i_*\) only when its address is decoded wrongly, which has a probability of at most \(\varepsilon\).

**6.4.** \(T=\lceil\log_2(1000\cdot2^{20})\rceil=\lceil29.97\rceil=30\), \(\varepsilon=\tfrac1{30000}\), \(r=400\).

**6.5.** On such inputs every candidate of the list, whatever the list is, is accepted with a probability of at most \(\varepsilon\) by Lemma 4.1, and the list has at most \(T\) entries by construction.

## References

- [OpenAI-Q] OpenAI, *A Nearly Quartic Separation Between Randomized and Quantum Query Complexity*, OpenAI Math Release preprint, 5 October 2026, Sections 3.2 and 3.3. https://github.com/openai/math/tree/main/preprints/A-Nearly-Quartic-Separation-Between-Randomized-and-Quantum-Query-Complexity-October-5-2026
