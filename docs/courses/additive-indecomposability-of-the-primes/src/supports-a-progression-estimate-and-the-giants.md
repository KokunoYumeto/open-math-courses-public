# Supports, a progression estimate and the giants

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lessons 15–17 prove the comparison estimates of Proposition 6.1 of Lesson 14. The difficulty is arithmetic. A coefficient \(A_l\) involves many prime variables: two giants at the top, internal compensation primes sampled at every node, bulk primes, and the shared spectators. They interact through integrality conditions (each restored pivot \(p=(vH_--wH_+)/(su)\) must be an integer), coprimality conditions, and the transforms \(g_q\) at the spectators. The plan is to replace the prime variables, one family at a time, by *ideal* variables: a real logarithmic coordinate together with an independent uniform unit residue modulo a suitable modulus. Once the bulk primes are ideal, their residues modulo each spectator are independent uniform units, and the finite-field tree comparison applies.

This lesson describes the support exactly by residue conditions (Section 1), proves a prime-progression estimate in short logarithmic intervals that keeps the possible exceptional zero explicitly (Lemma 2.1), arranges that the exceptional character can only involve a harmless modulus (Section 3), and replaces the two top giants by ideal variables (Proposition 4.1).

**Prerequisites.** [*A positive statistic and its binary-tree transfers*](a-positive-statistic-and-its-binary-tree-transfers.md); [*Diagrams, densities and cycles over a finite field*](diagrams-densities-and-cycles-over-a-finite-field.md), Section 1; [*The prime mean and a supply of nonsparse transforms*](the-prime-mean-and-a-supply-of-nonsparse-transforms.md), Lemma 1.1; [*The least prime in a progression: Linnik's theorem*](course:NT-DIRL/NT-DIRL-17), Section 1; [*Counting zeros and the explicit formula for ψ(x, χ)*](course:NT-DIRL/NT-DIRL-08), Theorem 1.1.

Throughout Lessons 15–17 all constants of the construction and the depth \(k\) are fixed, and \(L\to\infty\). The notation, priors, templates and support conventions are those of Lesson 14. At comparison level \(l\) put \(r=2^l\). Both environments of Proposition 6.1 of Lesson 14 are treated; in the diagonal environment the positive giant is the external integer variable. All estimates are uniform in the assignments being compared and in the frequency histories.

## 1. Histories, supports and real weights

**The samples.** Expand the two amplitudes of a comparison into their frequency histories; for the norm estimate (6.1) of Lesson 14, use the same assignment in both. At level \(t\ge1\) a history has \(2^{l-t}\) nodes, and each node samples a compensation vector of \(4\cdot2^{t-1}\) entries. So the two histories contain \(O(kr)\) internal prime samples, each counted once, at the node where it is sampled. Partition these samples according to their *equality pattern*; there are \(O_k(1)\) patterns. Entries of one compensation vector are distinct, and the size ranges of different types are disjoint, so equality is possible only between samples of the same type. For each distinct internal sampled prime \(b\), let \(n_b\) be its multiplicity in the pattern. The product of the node weights \(u\) of (4.5) of Lesson 14 is then
\[
\prod_bb^{n_b}.
\]

**The top data.** Write \(x_+,x_-\) for the two top giants. The negative giant \(x_-\) is an actual prime in both environments; \(x_+\) is a prime in the final environment and an external positive integer in the diagonal environment. Let \(d\) be the product of the \(m\) distinct spectator primes, and \(c_{\rm sm}\) the product of the distinct actual regular small primes at the top (all nongiant regular primes of the top list). The internal samples are disjoint from these by their types. Define
\[
\begin{gathered}
R_f=\prod_\nu|\nu|,\\
Q_f=R_f^{k+2},\\
\log Q_f=O_k(m),\quad(1.1)
\end{gathered}
\]
where the product runs over every frequency of the two histories, with repetition. Every small prime exceeds every frequency, hence is coprime to \(Q_f\).

At a *reversing node*, where the recursion (4.4) of Lesson 14 restores a pivot, write the two current giant entries as \(X_+,X_-\) and factor the child products as
\[
\begin{gathered}
H_+=X_+C_+M_+,\\
H_-=X_-C_-M_-,\quad(1.2)
\end{gathered}
\]
where \(M_\pm\) are the products of the bulk slots of the two child subtrees, and \(C_\pm\) contain their other regular small factors, which may include compensation samples restored at earlier reversals on the path. By (4.4) of Lesson 14 and induction down the tree, every current giant is a rational linear form in \((x_+,x_-)\).

**Lemma 1.1** (an exhaustive residue description). Assume that the top giants are coprime and that both are units modulo \(c_{\rm sm}d\). Then, together with positivity and the real cutoffs, the following tests describe exactly the support of the recursive evaluation over the integers:

1. modulo frequency factors: \(s\mid N\) at every node, where \(N=vH_--wH_+\), and all giant–frequency unit conditions; these are determined by the top and small coordinates modulo \(Q_f\);
2. for each prime \(b\) of the compensation vector \(\mathbf u\) at a node,
\[
\begin{gathered}
N\equiv0\pmod b,\\
N\not\equiv0\pmod{b^2};\quad(1.3)
\end{gathered}
\]
3. the top giants are units modulo \(c_{\rm sm}d\), and at each spectator \(q\mid d\) the zero convention of the diagrams of Lesson 12 applies whenever an inserted giant vanishes modulo \(q\).

*Proof.* Suppose a current state is pairwise coprime, and consider its reversal, with \(p=N/(su)\). Every prime factor of \(H_+\) is coprime to \(H_-\) and to \(v\): for an actual small prime by size, and for a giant factor by the giant–frequency unit conditions. So \(N\equiv vH_-\) is a unit at every prime factor of \(H_+\), and likewise at those of \(H_-\). If \(p\) is an integer, then \(N=sup\), so \(p\) and \(u\) are coprime to every inherited slot of \(H_+H_-\); in particular a new compensation sample cannot divide an inherited giant. To obtain a pairwise coprime child state it remains only that \(p\) be a unit modulo its own \(u\) and modulo \(d\).

The entries of \(\mathbf u\) are distinct and coprime to \(s\), so (1.3) at each \(b\mid u\) is exactly the requirement that \(u\mid N\) and that \(p\) be a unit modulo \(b\). Ancestor denominators involve other compensation types and frequencies, which are units even modulo \(b^2\), so (1.3) can be computed from the rational expressions in the top giants. Division by a node frequency loses at most one factor \(R_f\) of precision, the \(u\)'s are units modulo \(Q_f\), and there are at most \(k\) successive divisions, so (1.1) leaves enough precision for every test in item 1. Given that the ancestors are already evaluated integrally, items 1 and 2 give divisibility by the coprime factors \(s\) and \(u\), and the coprimality argument above passes the support to the children. Induction down the tree proves the assertion. \(\square\)

**The spectator factors.** At a spectator \(q\mid d\) put \(D'=d/q\). By (1.2), the order of the child giants, and (4.4) of Lesson 14, the spectator factors of a history at \(q\) are exactly the value of a diagram of Lesson 12: a leaf with list \((p,\mathbf u,H_\pm)\) has the spectator argument \(s/(D'puH_\pm)\), which is the argument \(y_{n,\pm}\) of (1.2) of Lesson 12; the bulk products are the leaf variables, the other regular small factors are the constants \(C\), and the consistency condition holds. Denote the two tree values by \(W_{1,q},W_{2,q}\). Their combined spectator factor is
\[
\prod_{q\mid d}W_{1,q}\,\overline{W_{2,q}} .
\tag{1.4}
\]
The zero convention of the diagrams incorporates exactly the inserted-giant unit tests at \(q\).

**Real weights.** Let \(\Xi\) be the product of all smooth real factors of the two histories, including \(K_{\rm ar}\) when present but excluding \(\prod_bb^{n_b}\). Define it for real positive top and small variables using (4.4) of Lesson 14 over \(\mathbb R\), and set the contribution to zero if an inserted \(p\) is not positive. This is a smooth extension, because \(\varphi(\log p-G)\) already vanishes for \(p<e^{G-1}\). Role indicators of counterparts involving nonbulk slots are kept as restrictions on those variables; all bulk priors and role ranges coincide, so no indicator cuts a bulk logarithmic coordinate.

Each history has \(r\) leaf factors (4.3) of Lesson 14. On their common support the modulus in each has logarithm \(\log X+\Delta_0+O_k(1)\), by the giant cutoffs, the small-prime ranges and both sum bins at that leaf. Hence
\[
|\Xi|\le e^{-r\Delta_0+O_k(1)}.
\tag{1.5}
\]
Its first derivatives in the logarithmic coordinates of the top giants and of the bulk slots are at most \(\exp(O_k(m))\). For the possible cancellation in \(N=vH_--wH_+\), use (4.1) of Lesson 14 in each subtree: at a node of level \(j\), each of \(|vH_-|\) and \(|wH_+|\), divided by \(|s|up\), is at most \(\exp(\Delta_j+E_{j-1}+O_k(1))\); the depth is at most \(k\), so repeated logarithmic differentiation along a path costs \(\exp(O_k(m))\). The other cutoffs, the bounded Fourier arguments in the leaf factors, and \(K_{\rm ar}\) obey the same bound. These bounds extend across the support boundaries, because a nonpositive inserted value lies outside the giant cutoff, where the extension is zero. The actual prior ranges serve as integration domains, so no further discontinuous indicator is needed.

## 2. A progression estimate retaining the exceptional term

Two rows of parameters are used:
\[
\begin{gathered}
\begin{array}{c|ccc}
&a_0&a_1&\mu\\\hline
\text{giant}&0.049&0.95&0.012\\
\text{bulk}&0.0039&0.007&0.0012
\end{array}\\
\begin{array}{c|ccc}
&\delta&\delta'&\theta\\\hline
\text{giant}&0.015&0.018&0.022\\
\text{bulk}&0.0014&0.0016&0.0018
\end{array}\quad(2.1)
\end{gathered}
\]

**Lemma 2.1** (prime progressions in short logarithmic intervals [OpenAI-013, Lemma 8.1]). Fix a row of (2.1). There is at most one primitive real character \(\chi_*\), of conductor at most \(\exp(e^{\mu L})\), with an associated real zero \(\beta_*<1\), such that the following holds. If \(\log M_*\le e^{\mu L}\), \((a,M_*)=1\), and \(I\) is an interval of length at most \(1\) inside \([e^{a_0L},e^{a_1L}]\), then
\[
\begin{aligned}
&\sum_{\substack{p\ \text{prime},\ \log p\in I\\p\equiv a\ (M_*)}}\frac1p
=\frac1{\varphi(M_*)}\int_I\bigl(1\\
&\qquad -\chi_*(a)e^{(\beta_*-1)t}\bigr)\frac{dt}t\\
&\qquad +O\bigl(\exp(-ce^{\delta'L})\bigr).\quad(2.2)
\end{aligned}
\]
The exceptional term is omitted if \(\chi_*\) does not exist or its conductor does not divide \(M_*\). The implied constant is absolute for the fixed row, and the multiplier in the integral lies in \([0,2]\).

*Proof.* *Zeros.* Put \(Q=\exp(e^{\mu L})\) and \(S=\exp(e^{\theta L})\ge Q\). By [*The least prime in a progression: Linnik's theorem*](course:NT-DIRL/NT-DIRL-17), (1.1), applied with the parameter \(S\), all zeros of all primitive \(L\)-functions of conductor at most \(S\) with \(|\Im\rho|\le S\) satisfy \(1-\Re\rho\ge a_0/\log(2S)\ge c_0e^{-\theta L}\), except possibly one simple real zero of a real character. Let \(\chi_*\) be that character if it exists and has conductor at most \(Q\), with \(\beta_*\) its zero. The zero count \(N(T,\chi)\ll T\log(q(T+2))\) is [*Counting zeros and the explicit formula for ψ(x, χ)*](course:NT-DIRL/NT-DIRL-08), Theorem 1.1.

*Smoothing.* Let \(t_0\) be the left endpoint of \(I\), \(y=e^{t_0}\), and \(\epsilon=\exp(-e^{\delta'L})\). Sandwich the indicator of the corresponding interval in the variable \(u=n/y\) between smooth nonnegative functions \(f_-\le f_+\) supported in \([\frac12,4]\), with \(\int(f_+-f_-)\,du=O(\epsilon)\) and \(\|f_\pm^{(j)}\|_\infty\ll_j\epsilon^{-j}\); if the interval is shorter than \(\epsilon\), take \(f_-=0\). For either function put
\[
\begin{gathered}
F(u)=\frac{f(u)}{u\log(yu)},\\
\mathcal MF(s)=\int_0^\infty F(u)u^{s-1}du .
\end{gathered}
\]
For a prime \(n=p\), \(\Lambda(p)F(p/y)/y=f(p/y)/p\).

*Explicit formula.* For a primitive \(\chi\), the argument of Lemma 1.1 of Lesson 11 (Mellin inversion and a shift to \(\Re s=-\frac12\)) gives
\[
\begin{aligned}
&\frac1y\sum_n\Lambda(n)\chi(n)F(n/y)\\
&\quad =\mathbf 1_{\chi=1}\int_0^\infty F(u)\,du\\
&\qquad -\sum_\rho y^{\rho-1}\mathcal MF(\rho)\\
&\qquad +O\bigl(y^{-1+o(1)}\bigr).\quad(2.3)
\end{aligned}
\]
Here the shifted integral is at most a fixed power of \(\epsilon^{-1}\) times \(y^{-3/2}\log(q+2)\), and a residue at \(0\) costs \(y^{-1}\) times such a factor; since \(a_0>\delta'\), these are \(O(y^{-1+o(1)})\). On \(0\le\Re s\le1\), integration by parts gives
\[
\begin{gathered}
|\mathcal MF(s)|\ll1,\\
\begin{aligned}
|\mathcal MF(s)|&\ll_j\epsilon^{-O(j)}(1+|\Im s|)^{-j}.
\end{aligned}\quad(2.4)
\end{gathered}
\]
The nonexceptional zeros of height at most \(S\) contribute at most
\[
\exp\bigl(-c_0e^{(a_0-\theta)L}+e^{\theta L}+O(L)\bigr),
\]
because \(|y^{\rho-1}|\le\exp(-c_0e^{-\theta L}t_0)\) and \(t_0\ge e^{a_0L}\). For the giant row \(a_0-\theta=0.027>\theta=0.022>\delta'\), and for the bulk row \(a_0-\theta=0.0021>\theta=0.0018>\delta'\), so this is far smaller than \(\exp(-ce^{\delta'L})\). The zeros above \(S\), by dyadic summation of the zero count and (2.4) with \(j=2\), contribute \(\exp(Ce^{\delta'L}-e^{\theta L}+O(L))\), also sufficient since \(\delta'<\theta\). Prime powers of higher exponent contribute \(y^{-1/2+o(1)}\). Passing from a character modulo \(M_*\) to its primitive character changes only the prime powers of primes dividing \(M_*\), a negligible amount.

*Orthogonality.* Selecting the class \(a\) by the characters modulo \(M_*\), the factor \(1/\varphi(M_*)\) compensates the number of characters, so the total error is the largest single-character error. The exceptional primitive character occurs among the characters modulo \(M_*\) exactly when its conductor divides \(M_*\).

*Main terms.* Under \(u=e^{t-t_0}\), the principal integral becomes \(\int f(e^{t-t_0})\,dt/t\), and the exceptional zero contributes \(-\chi_*(a)\int f(e^{t-t_0})e^{(\beta_*-1)t}\,dt/t\); no factor \(\beta_*\) remains. The density \((1-\chi_*(a)e^{(\beta_*-1)t})/(\varphi(M_*)t)\) is nonnegative and at most \(2/(\varphi(M_*)t)\). So the main integrals of \(f_+\) and \(f_-\) differ by \(O(\epsilon)\), and the pointwise sandwich of the positive prime sum proves (2.2). \(\square\)

The lemma keeps the exceptional zero in the main term instead of bounding it, because nothing excludes a real zero very close to \(1\) for a character of small conductor; the course never needs Siegel's theorem at this point. What matters is that the corrected density is nonnegative and at most twice the principal one, and Section 3 arranges that it depends only on a harmless residue.

## 3. Deleting a prime for each exceptional character

For each row of (2.1), let \(\chi_*\) be the possible exceptional character of Lemma 2.1, determined by \(L\) alone. If its conductor has a prime factor at least
\[
T_*=\exp(e^{0.0004L}),
\tag{3.1}
\]
delete one such prime value from every nongiant prior. This prescribes at most two deletions, the set \(\mathcal E_L\) of Lesson 14.

**Lemma 3.1.** For each of the moduli \(M_*\) used below, if an exceptional conductor divides \(M_*\), then it divides \(Q_f\).

*Proof.* The moduli below are \(c_{\rm sm}dQ_f\prod_bb^2\) and \(dQ_f\). Every prime factor of \(c_{\rm sm}\), \(d\) and the \(b\) is an actual nongiant prime, with \(\log\log p\ge0.0005L\), hence larger than \(T_*\); and every prime factor of \(Q_f\) divides a frequency of size \(\exp(O_k(m))\), hence is smaller than \(T_*\). If the conductor has a prime factor at least \(T_*\), one such prime was deleted from all nongiant priors, so it divides none of the moduli. Otherwise all its prime factors lie in the \(Q_f\) part, and since the parts are coprime and \(Q_f\) contains high powers of its primes, the whole conductor divides \(Q_f\). \(\square\)

So every surviving exceptional correction in (2.2) depends only on the real coordinate and on the residue modulo \(Q_f\). It couples no other coordinate of the Chinese remainder decomposition.

## 4. Idealization of the top giants

**The size budget.** Condition on all actual small primes, including the internal samples of both histories. At fixed frequencies, the regular and internal small-prime products have logarithms
\[
O_k(e^{0.01L})+O_k(me^{0.006L}),
\tag{4.1}
\]
and the spectator products have smaller logarithms. Using the pointwise bounds \(|g_\ell|\le\sqrt\ell\) and \(|\widetilde g_\ell|\le1\), the logarithm of the product of all large weights and pointwise transform bounds, the factors \(\prod_bb^{n_b}\) included, is at most \(e^{0.012L}\) for large \(L\).

**Coprime giants.** The temporary assumption that the two top giants are coprime can be removed, with Lemma 1.1 serving as the extension. In the prime environment the exceptional event is \(x_+=x_-\), of probability at most \(e^{-G+O(L)}\). In the external-integer environment a fixed prime \(x_-\) has \(O(1)\) multiples in the log cell of \(x_+\), of normalized mass \(O(e^{-G})\). After multiplication by the pointwise bound these are harmless, because \(G\ge e^{0.049L}\).

**The modulus.** Put
\[
M_*=c_{\rm sm}\,d\,Q_f\prod_bb^2 .
\tag{4.2}
\]
Its factors are pairwise coprime, and (4.1) gives \(\log M_*\le e^{0.012L}\). The giant log cells lie in \([e^{0.049L},e^{0.95L}]\). Lemma 2.1 with the giant row, with the original cell cutoff and normalization, replaces each top prime by a real logarithmic coordinate and a uniform unit residue modulo \(M_*\), with the principal harmonic density times the correction factor of (2.2). For an external integer, the analogous replacement uses the density
\[
e^{t-G}\varphi(t-G)\,dt
\tag{4.3}
\]
and uniform residues on all classes modulo \(M_*\); counting integers in a progression gives this with error \(e^{-G+O(L)}\) per interval and class. The total ideal mass of each coordinate is bounded, and the normalizing reciprocal of a prime cell costs only \(e^{O(L)}\).

**Proposition 4.1** (the ideal giants [OpenAI-013, (8.17)]). Replacing the two top giants by these ideal coordinates changes each comparison expression by
\[
O\bigl(\exp(-e^{0.013L})\bigr),
\tag{4.4}
\]
uniformly in the conditioned small variables, the frequencies and the assignments.

*Proof.* Partition both log cells with mesh \(\eta_g=\exp(-e^{0.015L})\), and freeze \(\Xi\) on each box. At fixed small variables and frequencies, all other conditions are residue conditions modulo \(M_*\). By the derivative bound, freezing costs at most
\[
\exp\bigl(-e^{0.015L}+O(e^{0.012L})+O_k(m)\bigr),
\]
including the pointwise costs. The number of boxes and of pairs of residue classes has logarithm \(O(e^{0.015L}+e^{0.012L})\). On each box and pair of classes, the two giants are independent, and Lemma 2.1 with the giant row gives the actual mass with absolute error \(O(\exp(-ce^{0.018L}))\). Even summed over all boxes and classes and multiplied by the pointwise bound, these errors total at most
\[
\begin{aligned}
&\exp\bigl(-ce^{0.018L}+O(e^{0.015L})\\
&\quad +O(e^{0.012L})+O_k(m)\bigr).
\end{aligned}
\]
The external-integer errors carry the even stronger factor \(e^{-G}\). Both are \(O(\exp(-e^{0.013L}))\). The exceptional correction factors are part of the measures; they are neither frozen nor differentiated. \(\square\)

The joint treatment matters: the approximation is applied to the joint law of the two giants on each box and class, so no conditional equidistribution of one giant given the other is assumed.

## 5. Exercises

**5.1.** Show that in Lemma 1.1 the condition \(N\not\equiv0\pmod{b^2}\) is equivalent to \(b\nmid p\), given \(s\mid N\), \(u\mid N\), \((b,s)=1\) and \(b^2\nmid u\).

**5.2.** Show that the multiplier \(1-\chi_*(a)e^{(\beta_*-1)t}\) in (2.2) lies in \([0,2]\), and give an example of parameters where it is close to \(0\).

**5.3.** Check the inequalities \(a_0-\theta>\theta>\delta'\) for both rows of (2.1), and explain where each is used.

**5.4.** Let \(x_-\) be a prime with \(\log x_-\in[G-1,G+1]\). Show that the integers \(n\) with \(\log n\in[G-1,G+1]\) divisible by \(x_-\) number at most \(e^2+1\), and that their total mass under the external measure (5.5) of Lesson 14 is \(O(e^{-G})\).

## 6. Solutions

**5.1.** Since \(N=sup\) and \(b\nmid s\), \(b\mid u\) exactly once, \(v_b(N)=1+v_b(p)\). So \(b^2\nmid N\) iff \(v_b(p)=0\).

**5.2.** \(\chi_*(a)\in\{0,\pm1\}\) and \(0<e^{(\beta_*-1)t}\le1\), so the multiplier is between \(1-1=0\) and \(1+1=2\). If \(\chi_*(a)=1\) and \(\beta_*\) is extremely close to \(1\), say \(1-\beta_*\le e^{-2a_1L}\), then \(e^{(\beta_*-1)t}\ge1-o(1)\) for \(t\le e^{a_1L}\), and the multiplier is nearly \(0\): primes in the class \(a\) are then much rarer than expected in the whole range.

**5.3.** Giant: \(0.049-0.022=0.027>0.022>0.018\). Bulk: \(0.0039-0.0018=0.0021\)\(>0.0018>0.0016\). The first inequality makes the low zeros' contribution \(\exp(-c_0e^{(a_0-\theta)L})\) beat the zero count \(e^{e^{\theta L}}\); the second makes the high zeros, beyond \(S=\exp(e^{\theta L})\), beat the smoothing loss \(\epsilon^{-O(1)}=\exp(O(e^{\delta'L}))\).

**5.4.** The multiples \(n=ax_-\) with \(\log n\in[G-1,G+1]\) have \(a\le e^{G+1}/x_-\le e^2\), so there are at most \(e^2+1\) of them. Each has mass \(e^{-G}\varphi(\log n-G)\le e^{-G}\), so the total is \(O(e^{-G})\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Sections 8.1–8.3: histories, supports and real-variable weights (8.1)–(8.6), Lemma 8.1 with (8.7)–(8.12), the deletion (8.13), and the idealization of the top giants (8.14)–(8.17). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
