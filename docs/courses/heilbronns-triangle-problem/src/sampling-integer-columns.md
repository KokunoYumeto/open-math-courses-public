# Sampling integer columns

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson combines the two residue constructions, [A determinant obstruction from field norms](a-determinant-obstruction-from-field-norms.md) with [Residue matrices and their orbits](residue-matrices-and-their-orbits.md) at the main modulus \(h\), and [A cap at an auxiliary prime](a-cap-at-an-auxiliary-prime.md) at \(q\). By the Chinese remainder theorem it lifts them to integer columns in a large box. The result is an exact formula: the probability that three samples form a given integer matrix is a weight times an explicit factor. With it, the probability of a *bad* triple, three distinct projected points with a determinant of absolute value at most \(\tau\), becomes a weighted lattice count. For nonzero determinants [Counting lattice matrices](counting-lattice-matrices.md) bounds that count; determinant zero is treated in the next lesson. The outcome is a bound of order \((\log N)^2h/(N^3r^d)\): the factor \(r^{-d}\) comes from the coincidence of labels that a small determinant requires.

## 1. The sampling rule

Keep the parameters of the previous lessons: the prime \(r\), \(d=41\), \(K=\mathbb F_{r^d}\), \(k\), \(L=r^{10}\), the prime \(B\), \(h=B^k\), \(\tau=\lfloor B^{k-1}/2\rfloor\); the prime \(q\) with \(h^{100}<q\leq2h^{100}\), \(H=h^2\), the cap \(S\) with \(s=|S|\). Since \(q>h\geq B\), \(q\) and \(h\) are coprime. Put
\[
N=(hq)^{10},\qquad\mathcal B=\bigl([0,N)^2\times[N,2N)\bigr)\cap\mathbb Z^3,\qquad\pi(u)=\Bigl(\frac{u_1}{u_3},\frac{u_2}{u_3}\Bigr)\in[0,1)^2 .
\]

*Shared choices.* Choose \(G_h\) uniformly in \(\mathrm{SL}_3(\mathbb Z/h\mathbb Z)\), and, independently, \((a,G_q)\) as in the previous lesson, which determines \(V\).

*Samples.* Given the shared choices, each sample \(u\in\mathcal B\) is drawn independently as follows: (1) draw a label and a digit column \(c\), with fresh independent digits, and require \(u\equiv G_hc\pmod h\); (2) draw \(u\bmod q\) uniformly from \(V\); (3) draw \(u\) uniformly among the points of \(\mathcal B\) with these two residues.

Since \(hq\) divides \(N\), every interval \([0,N)\) and \([N,2N)\) contains exactly \(N/(hq)\) integers of each residue class modulo \(hq\); by the Chinese remainder theorem every pair of residues has exactly \((N/(hq))^3\) lifts in \(\mathcal B\). So step (3) is always possible. Different samples are independent only *given* the shared choices; all estimates below keep the shared choices fixed until the end.

**Lemma 1.1 (proportional pairs).** For two samples \(u,v\),
\[
\Pr\bigl(\pi(u)=\pi(v)\bigr)\leq C\,(hq)^6N^{-3}
\]
for an absolute constant \(C\).

*Proof.* \(\pi(u)=\pi(v)\) exactly when \(u,v\) are proportional (Exercise 5.4 of the first lesson). Every \(u\in\mathcal B\) is a positive integer multiple of a unique primitive vector \(z\) with \(z_3>0\), and \(z\) has at most \(\sqrt6N/|z|\) multiples in \(\mathcal B\) (all points of \(\mathcal B\) have length less than \(\sqrt6N\)). So the ordered proportional pairs in \(\mathcal B^2\) number at most
\[
\sum_{0<|z|\leq\sqrt6N}\frac{6N^2}{|z|^2}\leq C'N^3,
\]
since the integer vectors with \(Y\leq|z|<2Y\) number at most \(125Y^3\) and contribute at most \(125Y\cdot6N^2\), and the dyadic \(Y\leq\sqrt6N\) add up to at most \(2\sqrt6N\). Given the residues of \(u\) and \(v\) at both moduli, the two lifts are independent and uniform on \((N/(hq))^3\) points each; so the conditional probability is at most \(C'N^3(hq)^6/N^6\). \(\square\)

## 2. An exact lifting identity

For three samples write \(A=(u^{(1)},u^{(2)},u^{(3)})\) for the integer matrix of the columns and \(C=(c^{(1)},c^{(2)},c^{(3)})\) for the matrix of their digit columns (before multiplication by \(G_h\)). For fixed \(C\), Lemma 1.1 of the fourth lesson gives \(D,E\), \(I=DE\) and the row lattice \(\Lambda=\Lambda_C\), and Lemma 2.1 there the orbit \(\mathcal O=\mathcal O_C\). Let \(W\) be the weight of the previous lesson.

**Lemma 2.1 (lifting identity).** Given the three labels and the digit matrix \(C\), for every set \(\mathcal E\) of integer matrices with columns in \(\mathcal B\),
\[
\begin{aligned}
&\Pr(A\in\mathcal E\mid C,\text{labels})\\
&=\frac{h^9}{N^9|\mathcal O|}\sum_{\substack{A\in\mathcal E\\ A\bmod h\in\mathcal O}}W(A).
\end{aligned}\tag{2.1}
\]

*Proof.* The matrix \(G_hC\) is uniform on \(\mathcal O\) (Lemma 2.1 of the fourth lesson). Independently, the ordered triple of residues modulo \(q\) equals that of a given \(A\) with probability \(W(A)/q^9\) ((3.2) of the previous lesson). Given both residue triples, \(A\) is one of the \((N/(hq))^9\) equally likely lifts. So a fixed \(A\) with \(A\bmod h\in\mathcal O\) has probability
\[
\frac1{|\mathcal O|}\cdot\frac{W(A)}{q^9}\cdot\Bigl(\frac{hq}N\Bigr)^9=\frac{h^9W(A)}{N^9|\mathcal O|},
\]
and other matrices have probability zero. Sum over \(\mathcal E\). \(\square\)

Call a triple of samples *bad* if its three projected points are pairwise distinct and \(|\det A|\leq\tau\). All matrices of \(\mathcal O\) have determinant \(\det C\) modulo \(h\) (Lemma 2.1 of the fourth lesson); since \(2\tau<h\), at most one integer \(t\in[-\tau,\tau]\) is the determinant of a bad triple with \(A\bmod h\in\mathcal O\), and if the labels are distinct there is none (Lemma 3.2 of the third lesson).

## 3. The weighted count

**Proposition 3.1 (weighted count at a fixed determinant).** There is a constant \(C\), depending only on the fixed parameters \(d\) and \(k\), with the following property. Fix a digit matrix \(C\), with row lattice \(\Lambda\) of index \(I\) and orbit \(\mathcal O\). For an integer \(t\) with \(|t|\leq\tau\) let \(\mathcal A_t\) be the set of integer matrices \(A\) with columns in \(\mathcal B\), pairwise distinct projected columns, \(A\bmod h\in\mathcal O\) and \(\det A=t\). Then
\[
\sum_{A\in\mathcal A_t}W(A)\leq C\,\bigl(\log(2N)\bigr)^2\frac{N^6}{I^2}.
\]

*Proof.* Every row of a matrix \(A\) with \(A\bmod h\in\mathcal O\) lies in \(\Lambda\), because the rows of \(A\bmod h\) lie in the row span of \(C\); and rows have length less than \(4N\).

*Case \(t\neq0\).* Since \(0<|t|\leq\tau<q\), the matrix \(A\bmod q\) has rank three; its columns are then affinely independent, and \(W(A)\leq C_1\) (Proposition 3.1 of the previous lesson). The lattice \(\Lambda\) contains \(E\mathbb Z^3\), so its successive lengths are at most \(E\leq h<4N\). Proposition 5.1 of the second lesson, with \(X=4N\), bounds the number of such \(A\) by \(C_2(\log(8N))^2(4N)^6/I^2\).

*Case \(t=0\).* Proposition 1.1 of the next lesson gives the stronger bound \(C_3\log(2N)N^6/I^2\) for the sum of \(W(A)\) over all integer matrices with columns in \(\mathcal B\), rows in \(\Lambda\), determinant zero and pairwise distinct projected columns; \(\mathcal A_0\) is a subset. \(\square\)

**Corollary 3.2 (probability of a bad triple).** For three samples,
\[
\Pr(\text{the triple is bad})\leq C\,\bigl(\log(2N)\bigr)^2\frac h{N^3r^d}.
\]

*Proof.* Condition on the labels and on \(C\). If the labels are distinct, the conditional probability is zero. Otherwise only one value \(t\) is possible, and (2.1), Proposition 3.1 and the orbit bound \(|\mathcal O|\geq\frac{21}{64}h^8/(D^3E^2)\) give
\[
\Pr(\text{bad}\mid C,\text{labels})\leq\frac{h^9}{N^9}\cdot\frac{64D^3E^2}{21h^8}\cdot C\bigl(\log(2N)\bigr)^2\frac{N^6}{D^2E^2}=C'\bigl(\log(2N)\bigr)^2\frac{hD}{N^3}.
\]
Let \(F\) be the event that two labels coincide. Averaging, \(\Pr(\text{bad})\leq C'(\log(2N))^2\frac h{N^3}\mathbb E[D\mathbf 1_F]\), and \(\mathbb E[D\mathbf 1_F]\leq6r^{-d}\) by Corollary 3.2 of the fourth lesson, which holds for every fixed triple of labels, repeated or not. \(\square\)

## 4. Exercises

**4.1.** Show that the number of integer points of \(\mathcal B\) in a fixed residue class modulo \(hq\) is exactly \((N/(hq))^3\).

**4.2.** In Lemma 1.1, where is it used that the third coordinates are positive?

**4.3.** Show that \(\sum W(A)\), over all integer matrices \(A\) with columns in \(\mathcal B\) and \(A\bmod h\in\mathcal O\), equals \(N^9|\mathcal O|/h^9\), and explain why this is consistent with (2.1) for \(\mathcal E=\mathcal B^3\).

**4.4.** Why does a bad triple with distinct labels have probability zero, while a triple with distinct labels can still have three collinear projected points? (Look at the definition of "bad".)

**4.5.** Compare the bound of Corollary 3.2 with the bound \((hq)^6/N^3\) of Lemma 1.1 for \(N=(hq)^{10}\).

## 5. Solutions

**4.1.** \([0,N)\) and \([N,2N)\) are intervals of \(N\) consecutive integers, a multiple of \(hq\); each contains \(N/(hq)\) integers of each class modulo \(hq\). A residue class of \(\mathbb Z^3\) modulo \(hq\) is a product of three classes.

**4.2.** Positivity makes proportional vectors positive multiples of one primitive vector with \(z_3>0\), and gives the equivalence of equal projections with proportionality.

**4.3.** Summing (2.1) over all \(A\) gives probability one: \(\sum_{A\bmod h\in\mathcal O}W(A)=N^9|\mathcal O|/h^9\). Directly: there are \(|\mathcal O|(N/h)^9\) matrices \(A\) with \(A\bmod h\in\mathcal O\) and columns in \(\mathcal B\), and the average of \(W\) over residues modulo \(q\) is \((q^3/s)^3\Pr(\text{all in }V)\) averaged over all residue triples, which equals one, since \(\sum_{\text{triples}}\Pr(\text{all three in }V)=s^3\).

**4.4.** A bad triple needs \(|\det A|\leq\tau\); with distinct labels \(\det A\) represents a residue with no representative in \([-\tau,\tau]\). Collinear projections mean \(\det A=0\), which is in \([-\tau,\tau]\); so with distinct labels they cannot occur either.

**4.5.** Lemma 1.1 gives \((hq)^{-24}\), Corollary 3.2 about \((\log N)^2h\,r^{-d}(hq)^{-30}\); both are tiny compared with the numbers of pairs and triples among \(n\approx r\sqrt{N^3/\tau}\) samples divided by \(n\), which is what the deletion argument of the last lesson needs.

## References

- [OpenAI-H] OpenAI, *A power improvement in the Heilbronn triangle lower bound*, OpenAI Math Release preprint, 25 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/A-power-improvement-in-the-Heilbronn-triangle-lower-bound-September-25-2026
