# The lower bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the theorem of [Depth-three circuits and the square-root barrier](depth-three-circuits-and-the-square-root-barrier.md): the language \(L\) of [An explicit language](an-explicit-language.md) needs depth-three circuits with more than \(2^{A\sqrt n}\) gates, for every constant \(A\) and every large \(n\). The restriction bound and the hard slices are combined first: a hard slice has small correlation with every CNF of width about \(\sqrt d\). Then a small circuit is shown to accept too few inputs.

The order of choices is: first \(A\); then constants \(B\) and \(b\) depending on \(A\); then \(n\) large. The language and its algorithm were fixed before all of them.

## 1. Parameters

Fix \(A>0\) and put
\[
\begin{gathered}
d=\lfloor n/5\rfloor,\qquad s=3A,\\
B=64(s+1),\qquad p=\frac B{\sqrt d},\\
m_0=B\sqrt d,\qquad k=\bigl\lceil3(s+1)\sqrt d\,\bigr\rceil .
\end{gathered}
\]
All statements below hold for \(n\) large enough, how large depending on \(A\). In particular \(d\geq64\), \(0<p\leq\frac12\), and \(n\leq5d+4\leq9d\), so that
\[
2^{A\sqrt n}\leq2^{3A\sqrt d}=2^{s\sqrt d}. \tag{1.1}
\]
The numbers \(k\) and \(1/p\) are both of order \(\sqrt d\), so \(pk\) is bounded:
\[
\begin{gathered}
\frac{2pk}{1-p}\leq4pk\leq Q,\\
Q=4B\,[\,3(s+1)+1\,],
\end{gathered}
\]
because \(k\leq3(s+1)\sqrt d+1\leq[3(s+1)+1]\sqrt d\).

**Lemma 1.1.** There is an integer \(b\geq1\), depending only on \(A\), such that the number \(\theta\) of the restriction bound, for these \(k\) and \(p\) and this \(b\), satisfies \(\theta\leq\frac12\).

*Proof.* The series \(\sum_\ell Q^\ell/\ell!\) converges (from \(\ell+1\geq2Q\) on, each term is at most half the previous one), so there is \(b\geq1\) with \(\sum_{\ell>b}Q^\ell/\ell!\leq\frac12\). With \(\binom k\ell\leq k^\ell/\ell!\) (Exercise 6.5 of [Path weights and backward counting](path-weights-and-backward-counting.md)),
\[
\begin{aligned}
\theta&=\sum_{\ell=b+1}^{k}\binom k\ell\Bigl(\frac{2p}{1-p}\Bigr)^{\ell}\\
&\leq\sum_{\ell>b}\frac1{\ell!}\Bigl(\frac{2pk}{1-p}\Bigr)^{\ell}\\
&\leq\sum_{\ell>b}\frac{Q^\ell}{\ell!}\leq\frac12. \qquad\square
\end{aligned}
\]

This is the only place where \(A\) influences the width \(b\).

## 2. A hard slice against wide CNFs

Apply Proposition 1.1 of [Hard slices](hard-slices.md) with this \(b\) and \(B\): for large \(n\) there is a setting of the parameter bits whose slice has sign \(g:\{0,1\}^d\to\{-1,1\}\) with the following property. Call a restriction \((T,\rho)\) *good* if it is not exceptional, that is, if \(|T|\in[\frac{m_0}2,2m_0]\) and \(\operatorname{corr}_b(g_{T,\rho})\leq2^{-|T|/8}\). Then
\[
\Pr[(T,\rho)\text{ is not good}]\leq4\cdot2^{-m_0/16},
\]
and on a good restriction \(\operatorname{corr}_b(g_{T,\rho})\leq2^{-m_0/16}\). Fix this setting.

**Proposition 2.1.** For every CNF \(H\) of width at most \(k\) on the \(d\) data variables,
\[
\bigl|\mathbb E_xg(x)H(x)\bigr|\leq6\cdot2^{-m_0/16}.
\]

*Proof.* By Lemma 4.1 of the first lesson (averaging over restrictions),
\[
\bigl|\mathbb E_xgH\bigr|\leq\mathbb E_{T,\rho}\bigl|\mathbb E_zg_{T,\rho}H_{T,\rho}\bigr| .
\]
By the restriction bound (Lemma 1.1 of [A finite expansion of a restricted CNF](a-finite-expansion-of-a-restricted-cnf.md)) and Lemma 1.1 above, there are numbers \(W(H,T,\rho)\geq0\) with \(\mathbb EW\leq1/(1-\theta)\leq2\) and
\[
\bigl|\mathbb E_zg_{T,\rho}H_{T,\rho}\bigr|\leq W(H,T,\rho)\operatorname{corr}_b(g_{T,\rho})
\]
for every restriction. On a good restriction the right side is at most \(2^{-m_0/16}W\). On any restriction the left side is at most \(1\), because \(g\) is a sign and \(H\) an indicator. Therefore
\[
\begin{aligned}
\bigl|\mathbb E_xgH\bigr|&\leq2^{-m_0/16}\,\mathbb E\bigl[W\,\mathbf 1_{\text{good}}\bigr]\\
&\qquad+\Pr[\text{not good}]\\
&\leq2\cdot2^{-m_0/16}+4\cdot2^{-m_0/16}.
\end{aligned}
\]
This is the claim. \(\square\)

Two remarks on the logic. The weight \(W\) and the event that the restriction is good may depend on each other in any way; the proof bounds \(W\mathbf 1_{\text{good}}\leq W\) and uses only \(\mathbb EW\leq2\). And the slice was fixed before \(H\): goodness of a restriction controls all CNFs of width \(b\) at once, and the restriction bound is applied to each \(H\) separately, so one slice serves for every \(H\).

**Corollary 2.2.** For \(n\) large, the slice accepts at least a quarter of the inputs: \(\Pr_x[g(x)=1]\geq\frac14\).

*Proof.* The constant true function is a CNF of width at most \(k\) (with no clauses). So \(|\mathbb Eg|\leq6\cdot2^{-m_0/16}\), which is less than \(\frac12\) for large \(n\), and \(\Pr[g=1]=\frac12(1+\mathbb Eg)\geq\frac14\). \(\square\)

## 3. A small circuit accepts too little

**Proposition 3.1.** Let an OR–AND–OR circuit with \(S\) gates compute the slice of Section 2 exactly, as a function of the \(d\) data variables. Then
\[
\Pr_x[g(x)=1]\leq6S\cdot2^{-m_0/16}+S^2\,2^{-k}.
\]

*Proof.* Remove the gates from which no path leads to the output; then every middle gate feeds the top gate. There are at most \(S\) middle gates, and each computes a CNF with at most \(S\) clauses, one for each bottom gate wired to it (Exercise 6.5 of the first lesson). Normalize the clauses: drop clauses that are always true, and drop a middle gate that has a false clause, since it computes \(0\).

Let \(H\) be the CNF of a remaining middle gate, and let \(H'\) be \(H\) without its clauses of width greater than \(k\). Then \(H'\geq H\), and \(H'\) has width at most \(k\). A clause of width \(\ell>k\) is violated on a fraction \(2^{-\ell}\leq2^{-k}\) of the cube, and \(H'-H\) is \(1\) only where a deleted clause is violated, so
\[
\mathbb E(H'-H)\leq S\,2^{-k}.
\]
Every input accepted by \(H\) is accepted by the top gate, which computes the slice. So \(H=1\) implies \(g=1\), that is, \(gH=H\) pointwise. With Proposition 2.1 applied to \(H'\),
\[
\begin{aligned}
\mathbb EH&=\mathbb E(gH)\\
&=\mathbb E(gH')-\mathbb E\bigl(g(H'-H)\bigr)\\
&\leq6\cdot2^{-m_0/16}+S\,2^{-k}.
\end{aligned}
\]
The accepted set of the circuit is the union of the accepted sets of its middle gates. Summing over at most \(S\) gates gives the claim. \(\square\)

The proof counts *all* gates: the number of middle gates bounds the number of CNFs, and the number of bottom gates bounds the clauses of each CNF, hence the cost of deleting the wide ones. A CNF with few clauses but large width, and an OR of many narrow CNFs, are both expensive in this count.

## 4. Proof of the theorem

**Theorem 4.1 (OpenAI, 2026).** Let \(f_n\) be the membership function of \(L\) on \(\{0,1\}^n\). For every \(A>0\) there is \(N_A\) such that \(S_3(f_n)>2^{A\sqrt n}\) for all \(n\geq N_A\). The language \(L\) is decided in polynomial time.

*Proof.* Polynomial time is Proposition 3.1 of [An explicit language](an-explicit-language.md). Fix \(A\) and let \(n\) be large. Suppose an OR–AND–OR circuit with \(S\leq2^{A\sqrt n}\) gates computes \(f_n\). Substitute the parameter bits fixed in Section 2, and arbitrary constants for the unused bits, into its inputs: bottom gates then read data literals and constants, the number of gates does not grow, and the circuit computes the slice. By Corollary 2.2, Proposition 3.1 and (1.1),
\[
\begin{aligned}
\frac14\leq\Pr[g=1]&\leq6\cdot2^{s\sqrt d-m_0/16}\\
&\qquad+2^{2s\sqrt d-k}.
\end{aligned}
\]
Now \(m_0/16=4(s+1)\sqrt d\) and \(k\geq3(s+1)\sqrt d\), so the right side is at most
\[
6\cdot2^{-(3s+4)\sqrt d}+2^{-(s+3)\sqrt d},
\]
which tends to \(0\) as \(n\to\infty\). This is a contradiction for large \(n\). \(\square\)

This is Theorem 2.1 of the first lesson: \(\log_2S_3(f_n)/\sqrt n\) exceeds every constant \(A\) from \(N_A\) on, so it tends to infinity.

## 5. What the proof gives and what it does not

**Where the square root sits.** The restriction leaves about \(m_0=B\sqrt d\) variables live, and CNFs are truncated at width \(k\approx3(s+1)\sqrt d\). The two scales are tied together: the restriction bound needs \(pk\) bounded, so \(p\) is of order \(1/k\), and then the number of live variables \(pd\) is of order \(d/k\). The gain \(2^{-m_0/16}\) from the hard slice and the truncation loss \(2^{-k}\) are balanced when \(k\) and \(d/k\) are both of order \(\sqrt d\). Raising the constant \(A\) is paid for by a larger constant \(B\) and a larger width \(b\), and by a larger threshold \(N_A\); nothing else changes. The constants are large: for \(A=1\) the proof takes \(B=256\) and \(Q=13312\), a width \(b\) of about \(36{,}000\) is needed in Lemma 1.1, and the constant \(M(b,\frac18)\) of the sparse partition for such a width is far larger still. The proof makes no attempt to keep \(N_A\) small.

**No fixed larger exponent.** The proof does not give a bound \(2^{n^{1/2+\varepsilon}}\) for a fixed \(\varepsilon>0\). In the proof of the hard slices the constants \(b\) and \(B\) must be fixed before \(d\) grows: the amount of independence \(t\approx d^{1/6}\) has to beat the number \(2^{O(m\log m)}\) of sparse tests with a constant \(M(b,\frac18)\), and \(M\) grows quickly with \(b\). Whether an explicit function needs depth-three circuits of size \(2^{n^{1/2+\varepsilon}}\) is not settled by this theorem.

**Formal verification.** OpenAI's release contains a Lean formalization of the theorem in the form stated here: one polynomial-time language, a Turing machine with an explicit time bound, total gate count with unrestricted fan-in and sharing, and the bound for every \(A\) at all large lengths.

## 6. Exercises

**6.1.** Check the arithmetic at the end of the proof of Theorem 4.1: with \(S\leq2^{s\sqrt d}\), show \(6S2^{-m_0/16}\leq6\cdot2^{-(3s+4)\sqrt d}\) and \(S^22^{-k}\leq2^{-(s+3)\sqrt d}\).

**6.2.** Why is the truncation at width \(k\) needed at all? What goes wrong if Proposition 2.1 is applied to a CNF of unbounded width?

**6.3.** Proposition 3.1 uses that the circuit computes the slice *exactly*. Where? Show that the argument still works if the circuit only computes a function \(f'\) with \(f'\leq f\) and \(\Pr[f'=1]\geq\frac18\).

**6.4.** The parity function on \(d\) variables has depth-three circuits of size \(2^{O(\sqrt d)}\). Which step of the proof must therefore fail for parity in place of the slice?

**6.5.** Show that the theorem implies: for every \(A\), every OR–AND–OR circuit for \(f_n\) with \(n\geq N_A\) has more than \(2^{A\sqrt n}\) *bottom or middle* gates, up to one gate.

## 7. Solutions

**6.1.** \(m_0/16=64(s+1)\sqrt d/16\), which is \(4(s+1)\sqrt d\), so \(S2^{-m_0/16}\leq2^{(s-4s-4)\sqrt d}=2^{-(3s+4)\sqrt d}\). And \(k\geq3(s+1)\sqrt d\) gives \(S^22^{-k}\leq2^{(2s-3s-3)\sqrt d}=2^{-(s+3)\sqrt d}\).

**6.2.** The restriction bound needs \(\theta<1\), and \(\theta\) contains the terms \(\binom k\ell(2p/(1-p))^\ell\) up to \(\ell=k\). With \(p\) of order \(1/\sqrt d\), this requires \(k\) of order at most \(\sqrt d\). For wider CNFs the expected weight \(W\) is not bounded. The truncation trades width for the error \(S2^{-k}\) per gate.

**6.3.** It is used for \(gH=H\) (every input accepted by a middle gate is accepted by the slice) and for the accepted set of the slice being the union over the middle gates. If the circuit computes \(f'\leq f\), then \(gH=H\) still holds for its middle gates, and summing gives \(\Pr[f'=1]\leq6S2^{-m_0/16}+S^22^{-k}\), which contradicts \(\Pr[f'=1]\geq\frac18\) for large \(n\) in the same way.

**6.4.** The hard-slice property (Proposition 1.1 of [Hard slices](hard-slices.md)) fails for parity. After a restriction, the sign of parity is, up to a constant sign, the parity of the \(m\) live variables. Split the live variables into \(\lceil m/b\rceil\) blocks of at most \(b\) variables, and let \(J\) say that every block has even parity. Each block condition is a CNF of width at most \(b\) (one clause for each odd assignment of the block), so \(J\in\mathcal C_b(T)\); it accepts a fraction \(2^{-\lceil m/b\rceil}\) of the cube, and the parity is constant on the accepted set. So \(\operatorname{corr}_b\geq2^{-\lceil m/b\rceil}\), which is larger than \(2^{-m/8}\) when \(b\geq9\) and \(m>72\). The width \(b\) of Lemma 1.1 is much larger than \(9\): since \(Q^\ell/\ell!\geq1\) for \(\ell\leq Q\), the condition \(\sum_{\ell>b}Q^\ell/\ell!\leq\frac12\) forces \(b\geq Q\geq1024\). The other steps (the restriction bound and Proposition 3.1) hold for every function.

**6.5.** The top gate is one gate, so a circuit with \(S\) gates has \(S-1\) bottom and middle gates. If these numbered at most \(2^{A\sqrt n}-1\), the circuit would have at most \(2^{A\sqrt n}\) gates, contradicting the theorem.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization of the same paper. https://github.com/openai/math/blob/main/lean/docs/112.md
