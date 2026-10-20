# The final contradiction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves Theorem 5.1 of Lesson 1, and with it Ostmann's conjecture (Theorem 1.1 of Lesson 1). Two bounds for the final amplitude \(\eta_k\) of Lesson 14 are played against each other. From below, the transfers propagate the lower bound \(|\eta_0|\ge e^{-B_*m}\) once their diagonals are controlled (Proposition 2.2). From above, the amplitude does not change when the bulk values are permuted among the bulk positions, so it can be averaged over all \((rm)!\) arrangements. By the comparison estimates of Lesson 14, two random arrangements almost always correlate very little: most pairs have few overlap components (Lemma 1.1). The averaged amplitude is therefore small, provided the common regular factor has a controlled norm (Proposition 3.1). For a large fixed depth \(k\) and then large \(L\), the upper bound falls below the lower bound.

**Prerequisites.** [*A positive statistic and its binary-tree transfers*](a-positive-statistic-and-its-binary-tree-transfers.md); [*The signed and norm comparisons*](the-signed-and-norm-comparisons.md); [*Supports, a progression estimate and the giants*](supports-a-progression-estimate-and-the-giants.md), Lemma 2.1.

All parameters, priors and zero conventions are those of Lesson 14. The constants written \(C\) in costs \(Crm\) do not depend on \(k\) or on the gap constants. Limits are taken with all constants and \(k\) fixed, and then \(L\to\infty\).

## 1. Counting bad arrangements

At level \(l\) put \(r=2^l\). Call a pair of arrangements of the \(rm\) bulk variables *bad* if it is not covered by the signed comparison (6.2) of Lesson 14: for \(l=0,1\) every pair is bad, and for \(l\ge2\) a bad pair has more than \(3r/4\) components in its overlap graph. Arrangements distinguish all bulk positions and all sampled bulk variables, so they are indexed by permutations even before any distinctness condition.

**Lemma 1.1** ([OpenAI-013, (9.1) and (9.2)]). For each fixed first arrangement, the number of bad second arrangements is at most
\[
\begin{aligned}
&N_{\rm bad}(r,m)\\
&\quad \le(m!)^r\exp\Bigl(\bigl(\tfrac14\log r+C\bigr)rm\\
&\qquad +O_k(1)\Bigr),\quad(1.1)
\end{aligned}
\]
and consequently
\[
\begin{aligned}
&\frac{N_{\rm bad}(r,m)}{(rm)!}\le\exp\Bigl(\bigl(-\tfrac34\log r\\
&\qquad +C\bigr)rm+O_k(1)\Bigr).\quad(1.2)
\end{aligned}
\]

*Proof.* Let \(l\ge2\). In a component of the overlap graph, let \(a_i\) be its number of leaves on either side; the two numbers agree, because every vertex has degree \(m\) and the component's edges can be counted from either side. With \(t>3r/4\) components,
\[
\begin{gathered}
\sum_{i=1}^ta_i=r,\\
\sum_{i=1}^t(a_i-1)=r-t<\frac r4 .
\end{gathered}
\]
There are only \(e^{O_k(1)}\) ways to choose and pair the partitions of the two leaf sets into components. Once they are fixed, the \(a_im\) variables incident to the \(i\)-th component can be assigned to its \(a_im\) slots on the second side in at most \((a_im)!\) ways. For \(1\le a\le r\),
\[
\begin{gathered}
\begin{aligned}
a\log a&=(a-1)\log a+\log a\\
&\le(a-1)(\log r+1),
\end{aligned}\\
(am)!\le(m!)^aa^{am},
\end{gathered}
\]
the second because a multinomial coefficient \((am)!/(m!)^a\) is at most the sum \(a^{am}\) of all multinomial coefficients with \(a\) parts. Hence
\[
\begin{aligned}
\prod_i(a_im)!&\le(m!)^r\exp\Bigl(m\sum_ia_i\log a_i\Bigr)\\
&\le(m!)^r\\
&\quad \exp\Bigl(\tfrac14(\log r+1)rm\Bigr),
\end{aligned}
\]
which gives (1.1). For \(r=1,2\), the bound \((rm)!\le(m!)^rr^{rm}\) gives (1.1) after enlarging \(C\). For (1.2), use \(m!\le m^m\) and \((rm)!\ge(rm/e)^{rm}\), so \((m!)^r/(rm)!\le(e/r)^{rm}\). \(\square\)

In a diagonal, the matchings of the nonbulk slots have only \(e^{O_k(1)}\) possibilities, since their number is fixed once \(k\) is.

## 2. The diagonals and the order of the constants

Let \(\mathcal D_j\) be the nonnegative diagonal of step \(j\), before the factor \(e^{c_g}\) of Proposition 5.1 of Lesson 14. At this step the compared amplitudes have level \(j-1\) and \(r_j=2^{j-1}\) leaves.

**Lemma 2.1** (the diagonal [OpenAI-013, (9.4)]). For \(1\le j\le k\),
\[
\begin{aligned}
\mathcal D_j&\le\exp\Bigl(-\Delta_j+r_j\bigl\{\Delta_0+\bigl(\log z\\
&\quad +\tfrac14\log r_j+C\bigr)m\bigr\}\\
&\quad +o_k(m)\Bigr)\\
&\quad +\exp(-\omega_k(m)).\quad(2.1)
\end{aligned}
\]

*Proof.* *Bad matchings.* For a bad matching, use \(|A^{(1)}\overline{A^{(2)}}|\le\frac12(|A^{(1)}|^2+|A^{(2)}|^2)\) on their common support. In each of the two squares, extract the point probability of the *other* ordered tuple. On the common support it is at most \(C_He^{-T_H+O_k(1)}\), with \(C_H\le L^{-r_jm}e^{Cr_jm+O_k(1)}\) by (5.4) of Lesson 14. The retained tuple is then summed with its own priors; this order works for both squares, also when a matching exchanges positions with different cell priors. The external integer measure and the weight \(u\) contribute \(e^{G+r_jw_j}\), and with \(e^{-T_H}\) this gives \(e^{-\Delta_j}\), by (4.1) of Lesson 14. The other archimedean factors are \(e^{O_k(1)}\). The one-assignment estimate (6.1) of Lesson 14, followed by (1.1), bounds the bad part by
\[
\begin{aligned}
&e^{-\Delta_j}L^{-r_jm}(m!)^{r_j}\exp\Bigl(r_j\Delta_0\\
&\quad +\bigl(\tfrac14\log r_j+C\bigr)r_jm+o_k(m)\Bigr),
\end{aligned}
\]
and \(L^{-r_jm}(m!)^{r_j}\le(m/L)^{r_jm}\le e^{r_jm\log z}\), since \(m\le zL\).

*Good matchings.* Every other matching satisfies (6.2) of Lesson 14, with its archimedean factor. After extracting the probabilities, the number and size of these terms cost at most \(\exp(O_k(m))\), for instance \((r_jm)!L^{-r_jm}\)\(\le\exp(r_jm\log(r_jm/L))\)\(=\exp(O_k(m))\). Their total is \(\exp(-\omega_k(m))\), where \(\omega_k(m)/m\to\infty\). \(\square\)

**The order of the constants.** The constant \(B_s\) has been chosen large enough for Proposition 3.1 of Lesson 14, whose \(B_*\) does not depend on the later gap constants or on \(k\). Write \(Z_G\) and \(c_g=\log Z_G^{-1}\le0.91L\) as in (1.5) of Lesson 14. Fix
\[
B=B_*+3 .
\tag{2.2}
\]
Choose \(B_z\ge9\), and then \(B_D\) with
\[
B_D\ge B_s+2B+C+6,
\tag{2.3}
\]
where \(C\) dominates the uniform constant in (2.1). These constants are fixed before \(k\). Substituting (1.1) of Lesson 14, the exponent of the first term of (2.1), divided by \(r_jm\), is
\[
\begin{aligned}
&B_s-B_D+(9-B_z)\log z\\
&\quad -\tfrac3{20}\log r_j+C+o_k(1),\quad(2.4)
\end{aligned}
\]
using \(\Delta_j/(r_jm)=B_D+B_z\log z+0.4\log r_j\), \(\Delta_0/m=B_s+8\log z\), and \(\frac14-0.4=-\frac3{20}\). By (2.3), (2.4) is at most \(-2B-6+o_k(1)\). So for every sufficiently large fixed \(k\) and then large \(L\), uniformly for \(1\le j\le k\),
\[
\begin{aligned}
&\mathcal D_j\\
&\quad \le\exp\bigl(-(2B+3)r_jm\bigr).\quad(2.5)
\end{aligned}
\]
The depth \(k\) is chosen in Section 4; it is required already to be so large that, with \(m=k^4L+O(1)\),
\[
\frac{c_g+\log2}m\le\frac2{k^4}<1
\tag{2.6}
\]
for all large \(L\).

**Proposition 2.2** (the lower bound [OpenAI-013, (9.11)]). For large \(L\),
\[
\begin{gathered}
\begin{aligned}
-\log|\eta_j|&\le2^jB_*m\\
&\quad +(2^j-1)(c_g+\log2)\\
&<B2^jm
\end{aligned}\\
(0\le j\le k).\quad(2.7)
\end{gathered}
\]

*Proof.* By Proposition 5.1 of Lesson 14, \(e^{-c_g}|\eta_{j-1}|^2\le\mathcal D_j+\eta_j\le\mathcal D_j+|\eta_j|\). If \(|\eta_{j-1}|\ge e^{-Br_jm}\), then (2.5) and (2.6) give \(\mathcal D_j\le\frac12e^{-c_g}|\eta_{j-1}|^2\), because \(e^{-3r_jm}\le\frac12e^{-c_g}\). Hence
\[
|\eta_j|\ge\tfrac12e^{-c_g}|\eta_{j-1}|^2 .
\tag{2.8}
\]
Induct on \(j\). For \(j=0\), (2.7) is Proposition 3.1 of Lesson 14. If (2.7) holds at \(j-1\), its right inequality gives the hypothesis \(|\eta_{j-1}|\ge e^{-Br_jm}\), so (2.8) holds, and
\[
\begin{aligned}
-\log|\eta_j|&\le(c_g+\log2)\\
&\quad +2\bigl(2^{j-1}B_*m\\
&\quad +(2^{j-1}-1)(c_g+\log2)\bigr)\\
&=2^jB_*m\\
&\quad +(2^j-1)(c_g+\log2).
\end{aligned}
\]
By (2.6), this is less than \(2^jm(B_*+2/k^4)<B2^jm\). \(\square\)

The reserve is inherited from the initial estimate rather than spent afresh at each step: the loss \(c_g+\log2\) per step doubles along with everything else, and stays below one unit of \(B\) in total.

## 3. The norm of the common regular transform

At the final level \(r=2^k\). Recall from (4.2) of Lesson 14 that \(\eta_k=\mathbb E\sum_sG_R(s/d)A_k(s)\), where \(G_R\) is the product of the regular transforms of the final list.

**Proposition 3.1** ([OpenAI-013, (9.12)]). With an absolute implied constant, for large \(L\),
\[
\begin{aligned}
&\mathbb E_{\mathbf d,\mathcal I_k}\sum_{0<|s|\le V_k}|G_R(s/d)|^2\\
&\quad \ll V_k .\quad(3.1)
\end{aligned}
\]
Only the distinctness and coprimality conventions of \(G_R\) are used; the bins and the history conditions belong to the coefficients.

*Proof.* Fix \(s\), the spectator list \(\mathbf d\), the actual regular small primes, and one of the two giant primes, \(q\); configurations with a repeated regular small prime, or one dividing \(d\), give zero. Let \(C\) be the squarefree product of the remaining regular small primes and \(p\) the other giant. Both giant transforms have modulus at most \(1\); dropping them, the remaining factor is
\[
\begin{gathered}
F(p\bmod C),\\
F(a)=\prod_{\ell\mid C}\bigl|g_\ell(a_\ell a^{-1}\bmod\ell)\bigr|^2,\\
a_\ell=\frac s{dq(C/\ell)}\bmod\ell .\quad(3.2)
\end{gathered}
\]
All \(a_\ell\) are units: the retained primes are distinct and coprime to \(d\), and \(0<|s|\le V_k\) is smaller than every prime. The condition \(p\ne q\) can be dropped, since the expression stays nonnegative and defined. Every prime \(p\) of the giant cell is a unit modulo \(C\).

*Exact averages.* As \(a\) runs over \(U_C=(\mathbb Z/C)^\times\), the arguments \(a_\ell a^{-1}\bmod\ell\) are, by the Chinese remainder theorem, independent and uniform on the nonzero residues. Since \(g_\ell(0)=0\) and \(\ell^{-1}\sum_x|g_\ell(x)|^2=1\),
\[
\begin{gathered}
\sum_{a\in U_C}F(a)=C,\\
\begin{aligned}
&\frac1{\varphi(C)}\sum_{a\in U_C}F(a)=\prod_{\ell\mid C}\frac\ell{\ell-1}\\
&\quad =1+o_k(1),
\end{aligned}\quad(3.3)
\end{gathered}
\]
because there are \(O_k(m)\) factors, each prime being at least \(\exp(e^{0.004L})\). No pointwise bound on the \(g_\ell\) is used.

*The prime average.* The size bounds give \(\log C=O_k(h+me^{0.006L})\le e^{0.012L}\), so Lemma 2.1 of Lesson 15 with the giant row applies to the modulus \(C\). With \(\varepsilon_L=\exp(-c\exp(0.018L))\), splitting the support of \(\varphi(t-G)\) into intervals of length at most \(1\) and summing by parts gives, uniformly for \(a\in U_C\),
\[
\begin{aligned}
&\sum_{\substack{p\ \text{prime}\\p\equiv a\ (C)}}\frac{\varphi(\log p-G)}p\\
&\quad =\frac1{\varphi(C)}\int\frac{\varphi(t-G)}t\bigl(1\\
&\qquad -\chi_*(a)e^{(\beta_*-1)t}\bigr)dt\\
&\qquad +O(\varepsilon_L),\quad(3.4)
\end{aligned}
\]
the exceptional term being absent if there is no exceptional character or its conductor does not divide \(C\). In any case \(0\le1-\chi_*(a)e^{(\beta_*-1)t}\le2\); this pointwise bound suffices even if the exceptional character correlates with \(F\). Multiply (3.4) by \(F(a)\ge0\), sum over \(a\in U_C\), and divide by \(Z_G\). The exact sum (3.3) both bounds the main term and sums the errors:
\[
\begin{aligned}
&\mathbb E_pF(p\bmod C)\le2\frac C{\varphi(C)}\\
&\qquad \cdot\frac{\int\varphi(t-G)\,dt/t}{Z_G}\\
&\qquad +O\bigl(Z_G^{-1}C\varepsilon_L\bigr)\\
&\quad =2+o_k(1),\quad(3.5)
\end{aligned}
\]
since the integral divided by \(Z_G\) is \(1+o(1)\), \(Z_G^{-1}=e^{O(L)}\), \(\log C\le e^{0.012L}\), and \(\varepsilon_L=\exp(-ce^{0.018L})\). All estimates are uniform in \(s\), \(\mathbf d\), \(q\) and the retained small primes. Averaging these and summing over at most \(2V_k\) frequencies proves (3.1). \(\square\)

## 4. Symmetrization and the contradiction

Let \(\mathfrak S_{rm}\) permute the values in the \(rm\) bulk positions of the final list, keeping every other position fixed. The bulk priors are identical, including their deletions, so their joint law is invariant under this action. The common factor \(G_R(s/d)\) is invariant too: the product \(R\), its set of prime factors, the transform attached to each bulk prime value, and every argument \(s/(d(R/\ell))\) are unchanged, and so are its distinctness and coprimality conventions. Put
\[
\begin{aligned}
A_{\rm sym}(s)&=\frac1{(rm)!}\sum_{\pi\in\mathfrak S_{rm}}A_k^\pi(s),\quad(4.1)
\end{aligned}
\]
where \(A_k^\pi\) has its bulk values placed according to \(\pi\). Changing variables separately for each permutation in (4.2) of Lesson 14,
\[
\eta_k=\mathbb E\sum_{0<|s|\le V_k}G_R(s/d)\,A_{\rm sym}(s).
\]
The bins and the history conditions stay inside each \(A_k^\pi\); they need not be invariant. By Cauchy–Schwarz and Proposition 3.1,
\[
\begin{aligned}
|\eta_k|^2&\le\Bigl(\mathbb E\sum_s|G_R(s/d)|^2\Bigr)\\
&\quad \Bigl(\mathbb E\sum_s|A_{\rm sym}(s)|^2\Bigr)\\
&\ll V_k\,\mathbb E\sum_s|A_{\rm sym}(s)|^2 .\quad(4.2)
\end{aligned}
\]

**The averaged coefficient.** Expand \(\mathbb E\sum_s|A_{\rm sym}(s)|^2\) into ordered pairs of permutations. A bad pair contributes at most \(\exp(r(\Delta_0+Cm)+o_k(m))\) in absolute value, by Cauchy–Schwarz and two applications of (6.1) of Lesson 14, and the bad pairs form at most the fraction (1.2) of all pairs. Every other pair satisfies (6.2) of Lesson 14 uniformly, so their average is at most \(\exp(-\omega_k(m))\). With \(V_k=e^{E_k}\),
\[
\begin{aligned}
|\eta_k|^2&\ll e^{E_k}\Bigl[\exp\Bigl(r\bigl\{\Delta_0\\
&\quad +\bigl(-\tfrac34\log r+C\bigr)m\bigr\}\\
&\quad +o_k(m)\Bigr)\\
&\quad +\exp(-\omega_k(m))\Bigr].\quad(4.3)
\end{aligned}
\]

**The frequency budget.** With \(r_j=2^{j-1}\),
\[
\begin{gathered}
\sum_{j=1}^kr_j=r-1,\\
\begin{aligned}
&\sum_{j=1}^kr_j\log r_j\\
&\quad =r\log r-2r\log2+2\log2,
\end{aligned}
\end{gathered}
\]
the second from \(\sum_{i=0}^{k-1}i2^i=(k-2)2^k+2\). By (1.1) of Lesson 14 they give
\[
\begin{aligned}
\frac{E_k}{rm}&\le\frac25\log r+B_D+B_s\\
&\quad +(B_z+8)\log z\\
&\quad +o_k(1).\quad(4.4)
\end{aligned}
\]
Since \(\Delta_0/m=B_s+8\log z\), the logarithm of the first term on the right of (4.3), divided by \(rm\), is at most
\[
\begin{aligned}
&-\frac7{20}\log r+B_D+2B_s\\
&\quad +(B_z+16)\log z+C\\
&\quad +o_k(1).\quad(4.5)
\end{aligned}
\]

**Choosing the depth.** All constants in (4.5) other than \(k\) are fixed. Choose \(k\) so large, also satisfying (2.6), that (4.5) without its \(o_k(1)\) is less than \(-2B-4\). This is possible because \(\log r=k\log2\) grows linearly in \(k\), while \(\log z=4\log k\). Then take \(L\) large. The first term of (4.3) is at most \(\exp(-(2B+3)rm)\), after absorbing the absolute implied constant. The second is \(\exp(O_k(m)-\omega_k(m))\), since \(E_k=O_k(m)\), which is also smaller than \(\exp(-(2B+3)rm)\) for large \(L\). So
\[
|\eta_k|^2\le\exp\bigl(-(2B+1)rm\bigr)
\]
for large \(L\). But (2.7) with \(j=k\) gives \(|\eta_k|^2\ge\exp(-2Brm)\). This contradiction shows that the standing assumption of Lesson 1 is impossible: no two infinite subsets of \(\mathbb N_0\) have a sumset whose symmetric difference with the primes is finite. This proves Theorem 5.1 of Lesson 1, and with Lemma 4.1 of Lesson 1, Ostmann's conjecture. \(\square\)

## 5. The proof as a whole

**The order of choices.** The proof of Theorem 5.1 of Lesson 1 fixes, in this order:

1. the sets \(A,B\), the threshold \(N\), and \(N_*\) (Lesson 1);
2. for the final argument: \(B_s\) (Proposition 3.1 of Lesson 14), hence \(B_*\) and \(B=B_*+3\); then \(B_z\ge9\) and \(B_D\) by (2.3);
3. the depth \(k\), large enough for (2.5), (2.6) and (4.5);
4. finally \(L\to\infty\), which determines \(h\), \(m\), \(G_0\), \(G\), \(X\) and all priors.

The earlier propositions (Theorem 1.1 of Lesson 3, Theorem 1.1 of Lesson 7, Theorem 6.1 of Lesson 9, Theorem 1.1 of Lesson 10, Lemma 1.2 of Lesson 12) are proved separately by their own contradictions, each with its own parameters.

**Where each hypothesis enters.**

- *Exclusion* (every large element of \(A+B\) is prime) makes the residues of the large elements of \(A\) and of \(-B\) disjoint modulo every prime, which defines the supports \(S_p\) (Lesson 1). It is used again in Lessons 2 and 6, in the form that a difference of a large element of \(A\) and an element of \(-B\) has no small prime factor.
- *Coverage* (every large prime lies in \(A+B\)) gives the lower bounds for \(A(x)\) and \(B(x)\) (Lesson 2) and, decisively, the supply of nonsparse transforms (Lessons 10–11), where every large prime must be a difference \(a-d\).
- The supports are *flat*: they correlate with no translated multiplicative character (Lessons 3–9). This is a consequence of exclusion through collision stability, the quadratic large sieve and the transfer argument.

**What the proof does not give.** The argument establishes no structure theorem for sets with large sieve restrictions, such as the inverse sieve conjecture of Green and Harper, and it gives no explicit bound: the constants come from compactness arguments and from Siegel's theorem, which is ineffective. It shows only that the assumed decomposition leads to two incompatible estimates for one amplitude.

## 6. Exercises

**6.1.** Verify \(\sum_{i=0}^{k-1}i2^i=(k-2)2^k+2\), and deduce the formula for \(\sum_jr_j\log r_j\).

**6.2.** In Lemma 1.1, check that \((am)!\le(m!)^aa^{am}\) for \(a=2\), \(m=2\), and find the case of equality for \(a=1\).

**6.3.** Verify the computation (2.4): \(\frac14\log r_j-0.4\log r_j=-\frac3{20}\log r_j\), and the combination of the \(\log z\) terms.

**6.4.** Explain why the depth \(k\) must be fixed before \(L\to\infty\), and could not be allowed to grow with \(L\) in this argument.

## 7. Solutions

**6.1.** By induction: for \(k=1\) both sides are \(0\). If true for \(k\), then \(\sum_{i=0}^{k}i2^i=(k-2)2^k+2+k2^k\)\(=(2k-2)2^k+2\)\(=(k-1)2^{k+1}+2\). With \(r_j=2^{j-1}\) and \(r=2^k\), \(\sum_{j=1}^kr_j\log r_j\)\(=\log2\sum_{i=0}^{k-1}i2^i\)\(=\log2\,((k-2)2^k+2)\)\(=r\log r-2r\log2+2\log2\).

**6.2.** For \(a=m=2\): \((4)!=24\le(2!)^2\cdot2^4=64\). For \(a=1\): \((m)!\le m!\cdot1\), always an equality.

**6.3.** \(-\Delta_j/(r_jm)\)\(=-(B_D+B_z\log z+0.4\log r_j)\), and \(\{\Delta_0\)\(+(\log z+\frac14\log r_j+C)m\}/m\)\(=B_s+8\log z+\log z+\frac14\log r_j+C\). The sum has \(\log z\) coefficient \(9-B_z\) and \(\log r_j\) coefficient \(\frac14-\frac25=-\frac3{20}\).

**6.4.** Many estimates have errors \(o_k(m)\) or bounds \(e^{O_k(1)}\) whose dependence on \(k\) is not controlled: the number of histories and equality patterns, the derivative bounds \(\exp(O_k(m))\), and the tree comparison constant \(C_l\). They are negligible only because \(k\) is fixed while \(L\to\infty\). The choice of \(k\) itself is made from constants independent of \(k\), as in (2.3) and (4.5).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 9: counting bad arrangements (9.1)–(9.2), diagonal bounds and the order of parameter choices (9.3)–(9.11), the norm of the common regular transform (9.12)–(9.16), and symmetrization and contradiction (9.17)–(9.21). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
