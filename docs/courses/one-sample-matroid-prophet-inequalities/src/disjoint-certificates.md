# Disjoint certificates

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves a self-contained statement about independent random bits, used in the sixth lesson, [Reverse exposure and safe samples](reverse-exposure-and-safe-samples.md). A procedure reads independent bits one at a time, choosing each next bit from what it has seen. It groups its reads into *transactions*, and it may call a transaction a success only when the bits found equal to one *within that transaction alone* already force a fixed increasing event. If that event fails with probability \(\delta\), the expected number of successes is at most \(\log(1/\delta)\), however cleverly the procedure adapts. The proof follows a single potential through the whole run.

Throughout, \(\log\) is the natural logarithm.

## 1. Bits, increasing events and certificates

Let \(V_0\) be a finite set of *coordinates*, and let \((\xi_e)_{e\in V_0}\) be independent bits with \(\Pr(\xi_e=1)=q_e\in[0,1]\). Identify a vector of bits with the set of coordinates where it equals one. An event \(\mathcal A\subseteq2^{V_0}\) is *increasing* if every superset of a member is a member. A set \(I\subseteq V_0\) is a *positive certificate* for \(\mathcal A\) if \(I\in\mathcal A\): setting the bits on \(I\) to one forces \(\mathcal A\), whatever the other bits are.

An *adaptive procedure* reads the bits one at a time. Before each read it chooses the next coordinate, never one already read, as a function of the transcript so far (the coordinates read and their values), and possibly of an auxiliary seed independent of the bits. In the same way it decides when to stop and how to divide its reads into consecutive *transactions*. We assume a deterministic bound on the number of transactions; the number of reads is at most \(|V_0|\).

**Lemma 1.1 (fresh bits).** Conditional on the auxiliary seed and on any transcript of positive probability, the unread bits are independent and have their original laws.

*Proof.* Condition on the seed. For a transcript reading \(e_1,\ldots,e_j\) with values \(x_1,\ldots,x_j\), the event that this transcript occurs is \(\{\xi_{e_1}=x_1,\ldots,\xi_{e_j}=x_j\}\), because each \(e_i\) is determined by the earlier values. This event involves only the read coordinates, which are fixed by the transcript, so it is independent of the bits outside \(\{e_1,\ldots,e_j\}\). \(\square\)

## 2. The certificate bound

**Lemma 2.1 (disjoint certificates).** Let \(\mathcal A\subseteq2^{V_0}\) be increasing, with failure probability \(\delta=\Pr(\xi\notin\mathcal A)>0\). Consider an adaptive procedure as above that declares a transaction *successful* only if the coordinates read in that transaction with value one form a positive certificate for \(\mathcal A\). Then the number \(N_{\mathrm{succ}}\) of successful transactions satisfies
\[
\mathbb E[N_{\mathrm{succ}}]\leq\log\frac1\delta.\tag{2.1}
\]

*Proof.* Condition on the auxiliary seed throughout. For disjoint sets \(V,I\subseteq V_0\) let \(\varphi_I(V)\) be the probability that \(\mathcal A\) fails when the bits on \(V\) are independent with their original laws, the bits on \(I\) equal one, and all other bits equal zero; write \(\varphi(V)=\varphi_\varnothing(V)\). Then:

- \(\varphi(V_0)=\delta\), and \(\varphi(V)\leq1\);
- \(\varphi(V\setminus\{e\})\geq\varphi(V)\), because \(\mathcal A\) is increasing and \(e\) is set to zero instead of being random; hence \(\varphi(V)\geq\delta>0\) for every \(V\subseteq V_0\);
- \(\varphi_I(V)\leq\varphi(V)\), for the same reason, and \(\varphi_I(V)=0\) when \(I\in\mathcal A\);
- for \(e\in V\) and \(V'=V\setminus\{e\}\), conditioning on the bit \(e\) gives
\[
\begin{aligned}
&\varphi_I(V)\\
&\quad=(1-q_e)\,\varphi_I(V')\\
&\qquad+q_e\,\varphi_{I\cup\{e\}}(V').
\end{aligned}\tag{2.2}
\]

During the run let \(V\) be the set of unread coordinates and \(I\) the set of coordinates read in the current transaction with value one; at the start of every transaction \(I=\varnothing\). Consider the quantity
\[
Z=\frac{\varphi_I(V)}{\varphi(V)}\in[0,1],
\]
which equals one at the start of each transaction and zero at the end of a successful one.

Suppose the next read is \(e\), let \(V'=V\setminus\{e\}\), and let \(Z'\) be the value after the read. By Lemma 1.1 the bit \(e\) equals one with conditional probability \(q_e\) given the current transcript \(\mathcal T\). So the numerator of \(Z'\) has conditional expectation \(\varphi_I(V)\) by (2.2), and
\[
\mathbb E[Z'\mid\mathcal T]=\frac{\varphi_I(V)}{\varphi(V')}=Z\,\frac{\varphi(V)}{\varphi(V')}.
\]
With \(\ell(V)=\log\varphi(V)\), \(x=\ell(V')-\ell(V)\geq0\) and \(0\leq Z\leq1\), and using \(1-e^{-x}\leq x\),
\[
\begin{aligned}
&\mathbb E[Z-Z'\mid\mathcal T]\\
&\quad=Z\bigl(1-e^{-x}\bigr)\\
&\quad\leq\ell(V')-\ell(V).
\end{aligned}\tag{2.3}
\]

For a transaction, its success indicator is at most \(1-Z_{\mathrm{end}}\), where \(Z_{\mathrm{end}}\) is the value of \(Z\) at its end: a success ends with \(Z=0\), and otherwise \(1-Z_{\mathrm{end}}\geq0\). Since \(Z\) starts the transaction at one, \(1-Z_{\mathrm{end}}\) is the sum of the decrements \(Z-Z'\) over the reads of that transaction. There are at most \(|V_0|\) reads in total; writing the sum over all potential reads with indicators of their occurrence, which are determined by the transcript before the read, and taking expectations read by read with (2.3), we obtain
\[
\mathbb E[N_{\mathrm{succ}}]\leq\mathbb E\sum_{\text{reads}}\bigl(\ell(V')-\ell(V)\bigr).
\]
The right side telescopes along the whole run, across transactions, because \(V\) only shrinks and is not reset: it equals \(\mathbb E[\log\varphi(V_{\mathrm{final}})]-\log\varphi(V_0)\leq0-\log\delta\). \(\square\)

The proof never uses which coordinates were read in earlier transactions, only that they are no longer available. A success "spends" failure probability: it requires bits that, by themselves, would rule out failure, and since the reads of different transactions are disjoint, the procedure cannot reuse the same lucky bits.

## 3. How the lemma will be used

In the sixth lesson the coordinates are the guard bits of the labels of several weight groups, read backwards in auxiliary time. A fixed label leaves a nominal flat at some step of this reverse computation; each step that does *not* remove it will turn out to certify, with the bits read at that step alone, a fixed increasing event whose failure probability is not small. Lemma 2.1 then bounds the expected number of such steps by a logarithm, and so shows that the label cannot survive many steps in which its chance of leaving is small.

## 4. Exercises

**4.1.** Let \(\mathcal A\) be the event that at least one of the bits is one, and let the procedure read the bits one at a time, each read forming one transaction, declared successful when the bit is one. Compute both sides of (2.1) and check the inequality directly.

**4.2.** Show by an example that the bound fails if a transaction may be declared successful using positive bits read in earlier transactions.

**4.3.** Prove that \(\varphi(V\setminus\{e\})\geq\varphi(V)\) and \(\varphi_I(V)\leq\varphi(V)\) from the definition of an increasing event.

**4.4.** For one coordinate with \(\Pr(\xi_e=1)=q\) and \(\mathcal A=\{\{e\}\}\), what is the largest possible expected number of successes, and how does it compare with \(\log(1/\delta)\)?

**4.5.** Where does the proof use that the number of transactions is bounded?

## 5. Solutions

**4.1.** Here \(\delta=\prod_e(1-q_e)\), and the expected number of successes is \(\sum_eq_e\). Since \(q\leq-\log(1-q)\) for \(0\leq q<1\), \(\sum_eq_e\leq\sum_e\log\frac1{1-q_e}=\log\frac1\delta\). (If some \(q_e=1\), then \(\delta=0\) and the lemma does not apply.)

**4.2.** With one coordinate \(e\), \(q_e=q\), and \(\mathcal A=\{\{e\}\}\): read \(e\) in the first transaction; then open many empty transactions and declare each successful if \(\xi_e=1\). The expected number of successes is \(Nq\) for \(N\) transactions, unbounded in \(N\), while \(\log(1/\delta)=\log\frac1{1-q}\).

**4.3.** Setting the bit of \(e\) to zero instead of drawing it can only move the bit vector out of \(\mathcal A\) (removing an element from a set never creates membership in an increasing family), so failure becomes more likely. Forcing the bits of \(I\) to one can only move the vector into \(\mathcal A\).

**4.4.** At most one success is possible, with probability \(q\); and \(\delta=1-q\), so \(q\leq\log\frac1{1-q}\), with near equality for small \(q\).

**4.5.** Only to justify writing the total as a finite sum of terms whose expectations are taken one at a time; with at most \(|V_0|\) reads and boundedly many transactions, the sums are finite and no limit argument for stopping times is needed. Transactions without reads have \(Z_{\mathrm{end}}=1\) and cannot succeed, since \(\varnothing\in\mathcal A\) would force \(\delta=0\).

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Section 4.2. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
