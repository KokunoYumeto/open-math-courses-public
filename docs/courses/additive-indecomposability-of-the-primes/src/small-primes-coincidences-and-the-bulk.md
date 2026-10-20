# Small primes, coincidences and the bulk

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

After Lesson 15 the two top giants are ideal: each is a real logarithmic coordinate together with a uniform residue modulo \(M_*=c_{\rm sm}dQ_f\prod_bb^2\). By the Chinese remainder theorem, these residues split into independent coordinates modulo each factor. This lesson integrates them out at all the small primes. At the regular small primes \(c_{\rm sm}\) the integral is an explicit constant (Lemma 1.1). At an internal compensation prime \(b\), every occurrence of \(b\) imposes a linear congruence on the two giants, and the integral is a *line probability* \(1/(b-1)\), \(1/b\) or \(0\) (Lemma 1.2). For the signed comparison, these probabilities must not depend on accidental congruences among the bulk primes; a polynomial identity test shows that they almost never do (Section 2). After that, nothing ties the bulk primes to any modulus except the spectators and \(Q_f\), and the bulk primes themselves can be made ideal (Proposition 3.1).

**Prerequisites.** [*Supports, a progression estimate and the giants*](supports-a-progression-estimate-and-the-giants.md); [*Anchor codes and decorrelation of higher characters*](anchor-codes-and-decorrelation-of-higher-characters.md), Lemma 1.1.

The notation of Lessons 14 and 15 is in force.

## 1. Integrating the giant coordinates at the small primes

In the ideal giant distribution the Chinese remainder theorem separates the coordinates modulo \(c_{\rm sm}\), \(d\), \(Q_f\) and the \(b^2\), and a surviving exceptional correction uses only the \(Q_f\) coordinate (Lemma 3.1 of Lesson 15).

**Lemma 1.1** (the regular small primes [OpenAI-013, (8.18)]). Integrating the giant coordinates modulo \(c_{\rm sm}\) multiplies the expression by
\[
\begin{aligned}
&\frac{\varphi(c_{\rm sm})}{c_{\rm sm}}\prod_{\ell\mid H_{\rm sm}}\frac\ell{\ell-1}\\
&\quad =\prod_{\ell\mid u_{\rm out}}\Bigl(1-\frac1\ell\Bigr)\quad(1.1)
\end{aligned}
\]
in the diagonal environment, where \(u_{\rm out}\) is the actual outer compensation product of type \(j\), and by \(1\) in the final environment. In particular the factor is at most \(1\) and does not depend on the bulk values.

*Proof.* In the diagonal environment \(x_-\) is already a unit modulo \(c_{\rm sm}\), and \(x_+\) must be restricted from all classes to the units, at the cost \(\varphi(c_{\rm sm})/c_{\rm sm}\). At \(\ell\mid H_{\rm sm}\), the argument of \(g_\ell\) in the factor \(\mathcal G\) of (5.3) of Lesson 14 is a fixed unit divided by \(x_+x_-\), which is uniform on the units once both giants are uniform units. Since \(g_\ell(0)=0\) and \(\mathbb E_a|g_\ell(a)|^2=1\), the average of \(|g_\ell|^2\) over the units is \(\ell/(\ell-1)\). The coordinates at different \(\ell\) are independent. Since \(c_{\rm sm}=H_{\rm sm}u_{\rm out}\) at the top of the diagonal environment, the product is (1.1). In the final environment \(\mathcal G=1\) and both giants are primes, already units. By Lemma 1.1 of Lesson 15, no other condition uses the giant coordinates modulo the actual regular small primes. \(\square\)

**The internal primes.** Fix a distinct internal sampled prime \(b\). Each occurrence of \(b\) requires a numerator \(N=vH_--wH_+\), at the node where \(b\) was sampled, to vanish modulo \(b\).

**Lemma 1.2** (linear forms). Each such numerator is a nonzero linear form in \((x_+,x_-)\) modulo \(b\), whose coefficients are rational expressions in the other small primes (regular or internal) and the fixed frequencies; no variable of the compensation type of \(b\) occurs in it. The same holds modulo \(b^2\), and across the two histories.

*Proof.* Along the path from the top to the node, each substitution (4.4) of Lesson 14 keeps one current giant and replaces the other by \(p=(vX_-C_-M_--wX_+C_+M_+)/(su)\), a combination of the two with unit coefficients; so each step is an invertible linear map modulo \(b\), and even modulo \(b^2\). The compensation vectors restored at the ancestors have types different from that of \(b\), which has not yet been reached on the way down, and the current numerator does not involve the current \(\mathbf u\). The numerator itself is the row \((-wC_+M_+,\,vC_-M_-)\), with unit entries, applied to the current pair. \(\square\)

Collect the forms of all occurrences of \(b\). If they have rank \(2\) modulo \(b\), they have no common solution with \(x_-\) a unit. If they have rank \(1\), their common line \(\alpha x_++\beta x_-\equiv0\) has probability
\[
\begin{cases}
(b-1)^{-1},&\begin{aligned}&\text{both giants prime}\\&\text{and }\alpha\beta\not\equiv0,\end{aligned}\\
b^{-1},&\begin{aligned}&x_+\text{ external}\\&\text{and }\alpha\not\equiv0,\end{aligned}\\
0,&\text{otherwise}.
\end{cases}\quad(1.2)
\]
In the second case, each of the \(b-1\) unit values of \(x_-\) determines one of the \(b\) values of \(x_+\). By the Chinese remainder theorem these probabilities multiply over the distinct \(b\).

**The second-order exclusions.** Given a solution modulo \(b\) on the line, the conditions \(N\not\equiv0\pmod{b^2}\) of (1.3) of Lesson 15 remove at most a proportion \(1/b\) of the uniform lifts to \(b^2\) for each occurrence: on the lifts, \(N/b\bmod b\) is a nonconstant affine function, because some coefficient of the form is a unit. A union bound over the occurrences gives a relative loss \(O_k(1/b)\).

**Lemma 1.3** (representative domination [OpenAI-013, (8.20)]). For a prime \(b\) in a compensation log cell, every occurrence prior \(\mu_i\) satisfies \(b\mu_i(b)\le e^{CL}\), with \(C\) independent of \(k\) for large \(L\). After integrating the line conditions, the joint measure of the internal samples, weighted by \(\prod_bb^{n_b}\), is dominated by independent *representative* priors, one occurrence prior for each distinct \(b\), times
\[
\exp(CkrL).
\tag{1.3}
\]
The distinctness of the representatives can be discarded for this upper bound.

*Proof.* The cell normalizations are at most \(e^{CL}\), since the cell centres are \(O_k(e^{0.01L})\). Choosing the first occurrence as representative,
\[
\begin{aligned}
&\Bigl(\prod_{i=1}^{n_b}\mu_i(b)\Bigr)\frac{b^{n_b}}{b-1}\\
&\quad =\mu_1(b)\,\frac b{b-1}\prod_{i\ge2}b\mu_i(b)\\
&\quad \le2\mu_1(b)e^{C(n_b-1)L},
\end{aligned}
\]
and \(\sum_b(n_b-1)=O(kr)\). The external case is the same, since \(1/b\le1/(b-1)\). \(\square\)

**Dropping the exclusions.** After Lemma 1.1, the remaining large pointwise factor is the spectator product: there are \(2r\) leaf transforms at each spectator, each at most \(\sqrt q\) in absolute value, so its logarithm is at most
\[
O_k\bigl(me^{0.001L}\bigr).
\tag{1.4}
\]
Every internal \(b\) has \(\log b\asymp_ke^{0.01L}\). So the relative losses \(O_k(1/b)\), multiplied by (1.3), (1.4) and all costs \(\exp(O_k(m))\), are negligible, and all the conditions \(N\not\equiv0\pmod{b^2}\) are dropped from here on.

## 2. Removing arithmetic coincidences

For the signed comparison, the line probabilities must not depend on accidental congruences among the bulk primes. Fix the equality pattern of the internal samples, and regard the representatives and the actual small primes as independent formal variables. For each \(b\), the rank and feasibility in (1.2) are decided by finitely many tests: whether a coefficient of a form vanishes, and whether a \(2\times2\) minor of two forms vanishes. Clear the denominators of these tests, which are units modulo \(b\). The result is a set of integer polynomials in the fixed frequencies and the formal variables, with no spectator variable and no variable of the type of \(b\).

**Degrees and sizes.** Each coefficient arising in a reversal is the product of the small slots of a subtree and a frequency, and a path has at most \(k\) substitutions; clearing ancestor denominators and forming a minor keeps the degree \(O_k(m)\). The same induction shows that, whenever an evaluation is nonzero,
\[
\log|P|\le e^{0.012L}
\tag{2.1}
\]
for large \(L\): the total degree is \(O_k(m)\), the small-prime logarithms are \(O_k(e^{0.01L})\), and the frequency coefficients have logarithm \(O_k(m)\).

**Proposition 2.1** (symbolic line factors [OpenAI-013, (8.24)]). Replace each test by the question whether its polynomial vanishes identically over \(\mathbb Q\). Under the domination of Lemma 1.3, this changes the expressions by
\[
O\bigl(\exp(-e^{0.002L})\bigr).
\tag{2.2}
\]

*Proof.* *Accidental zeros.* All variables occurring are at least of bulk size, so each has largest atom at most \(\exp(-ce^{0.004L})\). By Lemma 1.1 of Lesson 9, a polynomial that does not vanish identically has an exact zero with probability at most \(O_k(m)\exp(-ce^{0.004L})\).

*Accidental divisibility by \(b\).* If the evaluation is nonzero, (2.1) shows that it has at most \(e^{O(L)}\) prime divisors. The representative \(b\) is independent of the evaluation, since its whole type is absent from the polynomial, and its largest atom is at most \(\exp(-c_ke^{0.01L}+O(L))\); so \(b\) divides the evaluation with negligible probability. A polynomial that vanishes identically vanishes modulo \(b\) identically, because the cleared denominators are units.

*Totals.* For these bounds, discard the other support conditions and use the representative domination. Both the original and the replaced line factors are at most \(1/(b-1)\), so the domination applies to their difference. There are \(O_k(1)\) tests; multiplying by (1.4) and the costs \(\exp(O_k(m))\) gives (2.2). \(\square\)

**Integrating the line conditions.** For the signed estimate (6.2) of Lesson 14, the integral of the giant coordinates modulo each internal \(b\) is the symbolic rank and feasibility flag times the corresponding scalar of (1.2). The flags depend only on the formal pattern and the frequencies, not on the sampled bulk values. No other factor uses the giant coordinates at \(b\) once the \(b^2\) exclusions are removed, so this removes every dependence on the bulk residues modulo the internal primes.

For the norm estimate (6.1) of Lesson 14 there is a simpler nonnegative bound: take absolute values in the expansion, replace every line probability by \(1/(b-1)\), and use Lemma 1.3. The flags are discarded; they do not remain as conditions on the bulk variables.

**Bulk distinctness.** In the simplified expressions, the distinctness of the actual bulk samples can be removed as well. There are \(rm=O_k(m)\) such samples, and their collision probability under independent priors is at most the number of pairs times the largest point mass. With (1.3) and (1.4), the error is again bounded by (2.2). Spectator distinctness, and the conditions involving only nonbulk variables, are kept.

## 3. Joint idealization of the bulk variables

What depends on the actual bulk values is either smooth in their logarithmic coordinates or a condition modulo \(dQ_f\); no condition on their residues modulo internal primes or modulo regular small primes remains. Moreover
\[
\begin{aligned}
\log(dQ_f)&=O_k(me^{0.001L})\\
&<e^{0.0012L}.\quad(3.1)
\end{aligned}
\]

**Proposition 3.1** (ideal bulk [OpenAI-013, (8.27)]). Replace the \(rm\) bulk priors by their real harmonic densities times independent uniform unit residues modulo \(dQ_f\), keeping the possible exceptional corrections of Lemma 2.1 of Lesson 15 with the bulk row. This changes each comparison expression by
\[
O\bigl(\exp(-e^{0.00125L})\bigr),
\tag{3.2}
\]
uniformly in the frequency histories and the equality patterns.

*Proof.* The bulk range \(e^{0.004L}\le\log p\le e^{0.006L}\) lies strictly inside the range \([e^{0.0039L},e^{0.007L}]\) of the bulk row, and its harmonic normalization is of order \(L\). If a deleted prime lies in the bulk range, removing its single atom costs a negligible amount by the largest-atom bound, so the formula for all primes may be used with the given normalization.

Partition each bulk logarithmic range with mesh \(\eta_b=\exp(-e^{0.0014L})\). The joint boxes and joint residue classes number at most
\[
\begin{aligned}
&\exp\Bigl(O_k\bigl(m(e^{0.0014L}+L\\
&\quad +\log(dQ_f))\bigr)\Bigr).\quad(3.3)
\end{aligned}
\]
Freeze the smooth weight on each box; by (1.3) and (1.4) its remaining total or pointwise cost is \(\exp(O_k(me^{0.001L}))\), and the derivative bounds of Section 1 of Lesson 15 make the freezing error at most
\[
\begin{aligned}
&\exp\bigl(-e^{0.0014L}+O_k(me^{0.001L})\\
&\quad +O_k(m)\bigr).
\end{aligned}
\]
On each box and joint class, the actual and ideal masses of the product of the \(rm\) coordinates differ by at most the sum over the coordinates of the single-coordinate errors of Lemma 2.1 of Lesson 15 (bulk row, \(\delta'=0.0016\)) times bounded masses of the others. Summed over all boxes and classes, the interval errors are at most
\[
\begin{aligned}
&\exp\Bigl(-ce^{0.0016L}+O_k\\
&\quad \bigl(m(e^{0.0014L}+L+e^{0.0012L})\bigr)\\
&\quad +O_k(me^{0.001L})\Bigr).
\end{aligned}
\]
Since \(m=O_k(L)\), both are \(O(\exp(-e^{0.00125L}))\). The bounded masses of the other coordinates add only \(\exp(O_k(m))\). In the main term the real distributions are integrated as measures; the box count multiplies only the approximation errors.

For fixed \(k\) there are \(\exp(O_k(m))\) frequency histories, since each frequency is at most \(\exp(O_k(m))\) and there are \(O_k(1)\) nodes, and \(O_k(1)\) equality patterns. So (4.4) of Lesson 15, (2.2) and (3.2) remain negligible after the sums over histories and patterns. \(\square\)

After Proposition 3.1, the surviving exceptional multipliers are functions of the real and \(Q_f\) coordinates only, at most \(2\) per sampled prime; and the bulk residues modulo \(d\) are independent uniform units, entering only through the spectator product (1.4) of Lesson 15. Lesson 17 uses exactly this.

## 4. Exercises

**4.1.** In (1.2), verify the second case: if \(x_-\) is a uniform unit and \(x_+\) a uniform residue modulo \(b\), independent, and \(\alpha\not\equiv0\), then \(\Pr(\alpha x_++\beta x_-\equiv0)=1/b\).

**4.2.** Show that for a prime \(\ell\) and a function \(g\) on \(\mathbb F_\ell\) with \(g(0)=0\) and \(\mathbb E_{a\in\mathbb F_\ell}|g(a)|^2=1\), the average of \(|g|^2\) over the units is \(\ell/(\ell-1)\).

**4.3.** Give an example of two linear forms in \((x_+,x_-)\) modulo \(b\) with unit coefficients whose \(2\times2\) minor vanishes modulo \(b\) but not over \(\mathbb Q\), and explain why Proposition 2.1 makes such accidents negligible.

**4.4.** Let \(n\) independent variables take each value with probability at most \(\alpha\). Show that the probability that two of them coincide is at most \(\binom n2\alpha\).

## 5. Solutions

**4.1.** For each unit \(x_-\), the congruence determines \(x_+\equiv-\beta x_-/\alpha\), one residue out of \(b\). Averaging over \(x_-\) gives \(1/b\).

**4.2.** \(\sum_{a\in\mathbb F_\ell}|g(a)|^2=\ell\) and \(g(0)=0\), so the sum over the \(\ell-1\) units is \(\ell\), and the average is \(\ell/(\ell-1)\).

**4.3.** With variables \(c_1,c_2\) standing for small primes, take the forms \(c_1x_++x_-\) and \(c_2x_++x_-\); the minor is \(c_1-c_2\), not zero as a polynomial, but zero modulo \(b\) when \(c_1\equiv c_2\pmod b\). The polynomial \(c_1-c_2\) does not involve the type of \(b\); for a nonzero value \(c_1-c_2\) it has few prime divisors, and the independent prime \(b\) divides it with probability at most (number of divisors) times its largest atom, which is negligible; the value \(0\) itself has probability at most the largest atom of \(c_2\).

**4.4.** For each of the \(\binom n2\) pairs, condition on one variable; the other equals it with probability at most \(\alpha\). Apply the union bound.

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Sections 8.4–8.6: integration of the actual and internal small-prime coordinates (8.18)–(8.21), removing arithmetic coincidences in the line conditions (8.22)–(8.24), and joint idealization of the bulk variables (8.25)–(8.27). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
