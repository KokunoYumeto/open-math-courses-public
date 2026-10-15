# Depth-three circuits and the square-root barrier

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Boolean circuit of depth three is an OR of ANDs of ORs of literals: an OR of CNFs. The classical lower bounds for explicit functions in this model, starting with Håstad's bound for parity, all have the form \(2^{c\sqrt n}\) for a constant \(c\). This course proves OpenAI's theorem (2026) that one explicit language, decidable in polynomial time, needs more than \(2^{A\sqrt n}\) gates for *every* constant \(A\), at every sufficiently large input length. This lesson fixes the model and the basic notions (clauses, correlation with CNFs, random restrictions) and outlines the proof.

## 1. Circuits of depth three

A *literal* is a variable \(x_i\) or its negation. An *OR–AND–OR circuit* on \(n\) inputs has three layers of gates. *Bottom* gates are OR gates reading literals and possibly the constants \(0\) and \(1\); *middle* gates are AND gates reading bottom gates; the *top* gate is an OR gate reading middle gates. Fan-in and fan-out are unrestricted, so a bottom gate may feed several middle gates, and gates of fan-in one are allowed. Negations of inputs are free. The circuit computes \(f:\{0,1\}^n\to\{0,1\}\) if its top gate outputs \(f(x)\) on every input \(x\).

Each middle gate computes a *CNF*, a conjunction of *clauses*, each clause being an OR of literals. So a depth-three circuit computes an OR of CNFs. Write
\[
S_3(f)
\]
for the least *total* number of AND and OR gates in an OR–AND–OR circuit computing \(f\): the bottom gates, the middle gates and the top gate all count.

The total count matters. Every Boolean function is a single CNF (Exercise 6.1), so the number of middle gates alone says nothing; the cost of a CNF lies in its clauses, which are bottom gates. In particular \(S_3(f)\leq2^n+2\) for every \(f\).

## 2. The theorem

**Theorem 2.1 (OpenAI, 2026).** There are a language \(L\subseteq\{0,1\}^*\), a deterministic Turing machine deciding \(L\), and positive integers \(C\) and \(a\), such that the machine runs in time at most \(C(n+1)^a\) on every input of length \(n\), and the membership functions \(f_n\) of \(L\) on \(\{0,1\}^n\) satisfy
\[
\lim_{n\to\infty}\frac{\log_2S_3(f_n)}{\sqrt n}=\infty.
\]
Equivalently, for every real \(A>0\) there is \(N_A\) with \(S_3(f_n)>2^{A\sqrt n}\) for all \(n\geq N_A\).

The order of the quantifiers is the point. The language and its algorithm are fixed first; only then is the constant \(A\) chosen, and the bound holds at *every* large length, not just infinitely many.

**What was known.** Håstad's random restrictions and switching lemma gave the bound \(2^{\Omega(\sqrt n)}\) for parity (1989). Håstad, Jukna and Pudlák improved the constants with a top-down argument; Korten extended top-down proofs for parity to every constant depth [Korten 2026, Theorem 3]. Paturi, Pudlák and Zane showed, with their satisfiability coding lemma, that parity needs \(\Omega(n^{1/4}2^{\sqrt n})\) gates, which matches the upper bound up to a constant factor; so parity itself cannot go beyond the square-root scale. Neither can majority, long a candidate for stronger bounds: Lecomte and Ramakrishnan constructed, for every symmetric function and every constant depth \(d\), circuits of size \(2^{O(n^{1/(d-1)})}\), in particular OR–AND–OR circuits of size \(2^{O(\sqrt n)}\), with a construction found by GPT-6 Astra [Lecomte–Ramakrishnan 2026, Theorem 1]. So a language as in Theorem 2.1 cannot be symmetric. Paturi, Pudlák, Saks and Zane obtained the exponent \((\pi/\sqrt6)\sqrt n\) for membership in suitable codes. When the bottom gates have fan-in at most two, Paturi, Saks and Zane proved bounds \(2^{n-o(n)}\), and Gurumukhani, Paturi, Pudlák, Saks and Talebanfard obtained exponential bounds for bottom fan-in three; with bounded bottom fan-in the number of middle CNFs is itself a useful measure, which it is not in general. Making the ratio of the exponent to \(\sqrt n\) unbounded for an explicit function was open. A bound \(2^{n^{1/2+\varepsilon}}\) for a fixed \(\varepsilon>0\), asked for by Håstad, Jukna and Pudlák, would be stronger; the theorem does not give it.

## 3. Clauses, CNFs and correlation

Fix a finite set \(V\) of coordinates; the cube \(\{0,1\}^V\) carries the uniform probability measure, and expectations without a named measure refer to it. A predicate is identified with its \(0/1\) indicator. The *sign* of a predicate is \(+1\) where it holds and \(-1\) elsewhere.

A clause containing a variable and its negation, or the constant \(1\), is always true and can be removed from a CNF. Every other clause, after repeated literals and the constant \(0\) are dropped, is either the *false clause* (no literals) or uses distinct variables, its *scope*; its *width* is the size of the scope, and the false clause has width \(0\). A clause of width \(\ell\) is violated on exactly one assignment to its scope, hence on a fraction \(2^{-\ell}\) of the cube. The empty CNF is the constant true function.

For an integer \(b\geq1\), let \(\mathcal C_b(V)\) be the set of indicators of CNFs on \(\{0,1\}^V\) all of whose clauses have width at most \(b\), with no bound on the number of clauses. It contains both constant functions. For \(G:\{0,1\}^V\to\mathbb R\) put
\[
\operatorname{corr}_b(G)=\max_{J\in\mathcal C_b(V)}\bigl|\mathbb E_zG(z)J(z)\bigr|.
\]
The maximum exists because there are finitely many clauses of width at most \(b\), and repeating a clause does not change a CNF. Taking \(J=1\) shows \(\operatorname{corr}_b(G)\geq|\mathbb EG|\).

## 4. Random restrictions

Let \(0<p<1\). A *\(p\)-random restriction* of \([d]=\{1,\ldots,d\}\) is drawn in two stages: each coordinate is put into the *live set* \(T\) independently with probability \(p\), and then \(\rho\) is a uniform assignment to \([d]\setminus T\), independent of \(T\). For \(G:\{0,1\}^d\to\mathbb R\), the *restricted function* \(G_{T,\rho}\) on \(\{0,1\}^T\) is \(G\) with the coordinates outside \(T\) fixed by \(\rho\).

**Lemma 4.1 (averaging over restrictions).** For all \(G,H:\{0,1\}^d\to\mathbb R\),
\[
\mathbb E_xG(x)H(x)=\mathbb E_{T,\rho}\,\mathbb E_zG_{T,\rho}(z)H_{T,\rho}(z).
\]

*Proof.* For a fixed live set \(T\), the pair \((\rho,z)\) of a uniform assignment outside \(T\) and a uniform assignment on \(T\) is a uniform point of \(\{0,1\}^d\). So the inner average over \(\rho\) and \(z\) equals \(\mathbb E_xG(x)H(x)\) for every \(T\), and averaging over \(T\) changes nothing. \(\square\)

Restricting a CNF of width at most \(k\) gives a CNF of width at most \(k\) on \(\{0,1\}^T\): substituting constants into a clause either makes it true or removes literals. The number of clauses need not drop, and a random restriction need not make *every* clause narrow; the next two lessons deal with this.

A *cylinder* in \(\{0,1\}^T\) prescribes a pattern on a set \(U\subseteq T\) and leaves \(T\setminus U\) free. Its indicator is a conjunction of \(|U|\) clauses of width one, so it lies in \(\mathcal C_1(T)\), and its measure is \(2^{-|U|}\).

## 5. The plan of the proof

1. **Restriction bound** ([A finite expansion of a restricted CNF](a-finite-expansion-of-a-restricted-cnf.md) and [Path weights and backward counting](path-weights-and-backward-counting.md)). Let \(H\) be a CNF of width at most \(k\) and let \(p\) be small compared with \(1/k\). After a \(p\)-random restriction, \(H_{T,\rho}\) is a signed combination of CNFs of a constant width \(b\), whose total coefficient mass has expectation at most \(2\), *whatever the number of clauses of \(H\)*. So small correlation with all width-\(b\) CNFs on most restrictions gives small correlation with all width-\(k\) CNFs.
2. **Sparse partition** ([Sunflowers and a disjoint sparse partition](sunflowers-and-a-disjoint-sparse-partition.md)). A CNF of width at most \(b\) on \(m\) variables is a sum of at most \(2^{m/8}\) CNFs with disjoint supports, each of width at most \(b\) and with at most \(Mm\) clauses. There are few such sparse CNFs, so they can be controlled one at a time and then all together.
3. **An explicit language and hard slices** ([An explicit language](an-explicit-language.md) and [Hard slices](hard-slices.md)). The language evaluates a polynomial at a linear hash of its data bits, both given by further input bits. A random choice of these bits makes the data function nearly uncorrelated with every sparse CNF on most restrictions, because hashing and interpolation produce limited-independent signs.
4. **The lower bound** ([The lower bound](the-lower-bound.md)). A circuit with \(S\) gates has at most \(S\) middle CNFs with at most \(S\) clauses each. Clauses wider than \(k\approx\sqrt n\) can be deleted at total cost \(S^22^{-k}\). Each truncated middle CNF accepts only a tiny fraction of the cube, while the hard slice accepts about half of it.

## 6. Exercises

**6.1.** Show that every \(f:\{0,1\}^n\to\{0,1\}\) is computed by a single CNF, and deduce \(S_3(f)\leq2^n+2\).

**6.2.** Let \(f\) be parity, \(f(x)=x_1+\cdots+x_n\bmod2\). Show that every clause of a CNF computing \(f\) has width \(n\), and that such a CNF has at least \(2^{n-1}\) clauses.

**6.3.** Show that restricting a CNF can leave the number of clauses unchanged, by giving a CNF of width two with \(N\) clauses whose restriction by a fixed \((T,\rho)\) still has \(N\) clauses of width two.

**6.4.** In Lemma 4.1, the live set \(T\) and the assignment \(\rho\) are chosen in two stages. Show that the identity also holds conditionally on \(T\), for every fixed \(T\).

**6.5.** Show that an OR–AND–OR circuit with \(S\) gates has at most \(S\) middle gates, and that each of them computes a CNF with at most \(S\) clauses, even when bottom gates are shared.

## 7. Solutions

**6.1.** For every \(y\) with \(f(y)=0\), take the clause of width \(n\) violated exactly at \(y\). The conjunction of these clauses is \(f\). A circuit uses one bottom gate per clause, one middle gate and one top gate: at most \(2^n+2\) gates.

**6.2.** Let a clause of a CNF for parity miss the variable \(x_i\). Take an assignment violating the clause, and set \(x_i\) so that the parity is odd. This input is accepted but violates a clause of the CNF, a contradiction. So every clause has width \(n\) and rejects exactly one input; the \(2^{n-1}\) inputs of even parity need \(2^{n-1}\) different clauses.

**6.3.** Take \(H=\bigwedge_{i=1}^N(x_{2i-1}\vee x_{2i})\) on \(d=2N\) coordinates and \(T=[d]\). Nothing is fixed, and all \(N\) clauses keep width two. With a random live set, a clause keeps both its variables with probability \(p^2\), so a large \(N\) leaves many wide clauses.

**6.4.** For fixed \(T\), \((\rho,z)\) is uniform on \(\{0,1\}^{[d]\setminus T}\times\{0,1\}^T\), which is the uniform measure on \(\{0,1\}^d\); so \(\mathbb E_{\rho}\mathbb E_zG_{T,\rho}H_{T,\rho}=\mathbb E_xGH\).

**6.5.** Middle gates are among the \(S\) gates. A middle gate is the AND of the bottom gates wired to it; several wires from the same bottom gate compute the same clause and can be merged, so its clauses are distinct bottom gates, at most \(S\) of them.

## References

- [OpenAI-P] OpenAI, *Beyond the Square-Root Exponent for Depth-Three Boolean Circuits*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026
- [OpenAI-Lean] OpenAI Math Release, scope of the Lean formalization of the same paper. https://github.com/openai/math/blob/main/lean/docs/112.md
- [Lecomte–Ramakrishnan 2026] V. Lecomte and P. Ramakrishnan, *Optimal shallow circuits for Majority*, arXiv:2609.34029 (September 2026), Theorem 1. https://arxiv.org/abs/2609.34029
- [Korten 2026] O. Korten, *Top-down lower bounds for all depths*, arXiv:2609.38677 (September 2026), Theorem 3. https://arxiv.org/abs/2609.38677
- J. Håstad (1989), J. Håstad, S. Jukna and P. Pudlák (1995), R. Paturi, P. Pudlák and F. Zane (1999), R. Paturi, P. Pudlák, M. E. Saks and F. Zane (2005), R. Paturi, M. E. Saks and F. Zane (2000), and A. Gurumukhani, R. Paturi, P. Pudlák, M. Saks and N. Talebanfard (2024) are named for credit; the course does not use their results.
