# Physical states and good positions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The minor sum \(\mathcal Q_Y^{\rm min}\) of [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md) counts solutions of \(bmn-ars=b-a\) with a signed weight. This lesson writes it as a matrix coefficient \(\langle f,\mathcal Tg\rangle\) of an operator \(\mathcal T\) acting on functions of *states*: a primitive lattice point \(P\) together with ordered lists of marks dividing its first coordinate. The integer \(bmn-ars\) becomes the determinant of the lattice points \(P=(Dbm,s)\) and \(Q=(Dar,n)\), divided by a product \(D\) of auxiliary marks shared by both, the *pads*. The pads serve two purposes. Shared marks force the two lattice points into a common sublattice, which later produces cancellation on a balanced box; and averaging over pads costs nothing, because their harmonic weights add up to one. The lesson also defines the good positions, at which two Diophantine conditions hold that the later lessons need, and proves that the pads can be removed from the pairing at negligible cost.

**Prerequisites.** [*Cauchy's inequality and the determinant equation*](cauchys-inequality-and-the-determinant-equation.md), Sections 4–6; [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md), Lemma 1.2.

## 1. Parameters and the physical box

Fix \(Y\) in the range (2.1) of Lesson 7 and the exponent \(A_0\) of the major arcs \(\mathfrak M\). Recall

\[
\begin{gathered}
J=\lfloor L^{0.01}\rfloor,\qquad M=J+1,\\
R=\lceil L^{0.5}/2\rceil,\qquad N=2R .
\end{gathered}
\]

A **pad list** is a choice of \(J\) primes \(p_{i,1},\dots,p_{i,J}\in\mathcal P_i\) for each group \(i\), ordered within each group; its **pad product** is \(D=\prod_{i,h}p_{i,h}\). Since \(\log D\le2JKL^{0.2}\le2KL^{0.21}\), the pad products lie in at most \(3KL^{0.21}\) dyadic intervals \([d_0,2d_0)\) with \(d_0\) a power of two. Fix such a \(d_0\) and put

\[
\begin{gathered}
H=d_0Y,\qquad U=HH_m,\qquad V=H_n,\\
\Omega=[U,16U]\times[V,2V].\quad(1.1)
\end{gathered}
\]

Then \(\log H\le5KL^{0.21}\), so \(H=x^{o(1)}\), and \(UV=d_0YX\).

## 2. States and the edge operator

A **position** is a primitive integer vector \(P=(P_1,P_2)\in\Omega\). A **physical state** is a pair \((P,\mathbf p)\) where \(P\) is a position and \(\mathbf p=(\mathbf p_1,\dots,\mathbf p_K)\) consists of ordered lists \(\mathbf p_i=(p_{i,1},\dots,p_{i,M})\) of \(M\) *distinct* primes of \(\mathcal P_i\), all dividing \(P_1\). The states form a finite set. Let \(\mathcal H\) be the space of complex functions on states with the inner product of the measure

\[
\begin{gathered}
\sigma(P,\mathbf p)=\prod_{i=1}^KV_i^{-M}.\quad(2.1)
\end{gathered}
\]

The **symmetrization** \(\mathcal S\) averages a function over the \((M!)^K\) reorderings of the lists. It is the orthogonal projection onto functions symmetric in each list, because \(\sigma\) is invariant under reordering.

Fix the damping parameter \(\varkappa=1/4\). For an integer \(h\ge1\), \(\omega(h)\) counts the marks of \(h\) as in Lesson 1; at a state, \(\omega(P_1)-KM\ge0\) counts the marks of \(P_1\) that are not in the lists.

**The edge rule.** Given a source state \((P,\mathbf p)\), a target state \((Q,\mathbf p')\) is reached by an edge if, in every group \(i\),

1. the first \(J\) slots are **copied**: \(p'_{i,h}=p_{i,h}\) for \(h\le J\);
2. the last slot of the target, \(p'_{i,M}\), is a prime of \(\mathcal P_i\) different from all of \(p_{i,1},\dots,p_{i,M}\).

The copied primes are the **shared labels**, with product \(D\); the source's last slots have product \(b\), and the target's last slots have product \(a\), the **unshared labels**. Condition 2 is the **cross-edge ban**: all unshared labels are distinct from each other and from all shared labels. An edge carries the multiplier

\[
\begin{aligned}
&\mathcal K=\frac{d_0}D\,\eta\Bigl(\frac bY\Bigr)\eta\Bigl(\frac aY\Bigr)\psi\Bigl(\frac tY\Bigr)\\
&\ \times\Bigl\{\mathbf 1_{t=b-a}-\int_{\mathfrak M}e\bigl(\theta(t-b+a)\bigr)d\theta\Bigr\}\\
&\ \times\varkappa^{(\omega(P_1)-KM)/2+(\omega(Q_1)-KM)/2},\quad(2.2)
\end{aligned}
\]

where \(t=\det(P,Q)/D\); the multiplier is zero unless \(D\in[d_0,2d_0)\) and \(t\) is an integer. Here \(\eta\) and \(\psi\) are the cutoffs of Lesson 7. The **edge operator** is

\[
\begin{gathered}
(\mathcal T\phi)(P,\mathbf p)\\
=\sum_{(Q,\mathbf p')}\Bigl(\prod_{i=1}^KV_i^{-1}\Bigr)\mathcal K\,\phi(Q,\mathbf p'),\quad(2.3)
\end{gathered}
\]

the sum over all targets of \((P,\mathbf p)\). Each new slot is thus weighted by \(V_i^{-1}\), and target positions by counting measure.

**Lemma 2.1 (the adjoint).** The adjoint \(\mathcal T^*\) with respect to \(\sigma\) is given by the reversed rule: from a state \((Q,\mathbf p')\), copy the first \(J\) slots, choose a new last slot in each group different from all labels of \(\mathbf p'\), weight it by \(V_i^{-1}\), and multiply by \(\overline{\mathcal K}\), with \(\mathcal K\) evaluated at the pair \((P,Q)\) in its original order.

**Proof.** In \(\langle\phi,\mathcal T\psi\rangle\) every pair of states joined by an edge carries the weight \(\sigma\prod_iV_i^{-1}=\prod_iV_i^{-(M+1)}\) times \(\mathcal K\). The relation "joined by an edge" is symmetric under exchanging the roles of the two last slots, because the ban is symmetric and the copied slots coincide. Hence \(\langle\phi,\mathcal T\psi\rangle=\langle\mathcal T^*\phi,\psi\rangle\) with the stated \(\mathcal T^*\). \(\square\)

In the reversed edge the dropped labels are those of \(a\) and the new ones those of \(b\), and \(\det(Q,P)/D=-t\); so the indicator becomes \(\mathbf 1_{-t=a-b}\), of the same shape.

## 3. Good positions

For a position \(P\), complete it to an integer matrix \(\begin{pmatrix}P_1&W_1\\P_2&W_2\end{pmatrix}\) of determinant one, and put \(r_P=W_1/P_1\bmod1\). Another completion replaces \(W\) by \(W+jP\) and changes \(r_P\) by the integer \(j\), so \(r_P\in\mathbb R/\mathbb Z\) is well defined.

At a state \((P,\mathbf p)\), an **omission product** is the product of the lists after one label is omitted in every group; there are \(M^K\) of them. Only those in \([d_0,2d_0)\) are used.

**Definition 3.1.** A state \((P,\mathbf p)\) is **good** if both tests hold:

- **(G1)** for every omission product \(D\in[d_0,2d_0)\) and every integer \(1\le l\le Y^{0.2}\), \(\|lDr_P\|>Y^{-0.7}\);
- **(G2)** for every nonempty set \(I\) of groups, with \(i_*=\max I\): let \(T_f\) be the product of independent primes \(p_i\in\mathcal P_i\), \(i\notin I\), drawn with the harmonic laws \(\mu_i\). Then, except for draws of total probability at most \(\exp(-\frac14L^{a_{i_*}})\), the points \(DZT_fr_P\in\mathbb R/\mathbb Z\) are at mutual distance at least \(100\exp(-L^{a_{i_*}})\) for all pairs \((D,Z)\), \((D',Z')\) with \(DZ\ne D'Z'\). Here \(D\) runs over the omission products in \([d_0,2d_0)\), and \(Z\) over the products of one prime from each group in \(I\setminus\{i_*\}\).

Both tests depend on the lists only as sets, so the projection \(\mathcal G\) onto good states (multiplication by their indicator) commutes with \(\mathcal S\). Test (G1) keeps the lattices of Lesson 14 from becoming thin; test (G2) is used in Lesson 15 to show that a remembered prime can be retrieved for only one choice of omitted labels.

**Lemma 3.2 (most ratios are good).** For fixed lists and large \(x\), the set of \(r\in\mathbb R/\mathbb Z\) for which a state with these lists and \(r_P=r\) fails (G1) or (G2) has measure at most \(\exp(-cL^{0.1})\), with an absolute \(c>0\).

**Proof.** For a nonzero integer \(n\), the set \(\{r:\|nr\|\le\epsilon\}\) has measure \(2\epsilon\) when \(\epsilon\le\frac12\), because \(r\mapsto nr\) maps \(\mathbb R/\mathbb Z\) onto itself \(|n|\) to one and preserves measure.

(G1): there are at most \(M^K\) products \(D\) and \(Y^{0.2}\) values of \(l\), so the failing set has measure at most \(2M^KY^{0.2}Y^{-0.7}=2M^KY^{-0.5}\). By (2.1) of Lesson 7, \(Y\ge\exp(L^{0.1}-2)\), while \(M^K=\exp(O(\log L))\).

(G2): fix \(I\) and \(T_f\). The number of integers \(DZ\) is at most \(M^K\prod_{i\in I\setminus\{i_*\}}|\mathcal P_i|\le\exp(o(L^{a_{i_*}}))\), because \(|\mathcal P_i|\le\exp(2L^{a_i})\) and \(a_i<a_{i_*}\) for these \(i\). For two of them with \(DZ\ne D'Z'\), the integer \((DZ-D'Z')T_f\) is nonzero, and the separation fails on a set of measure at most \(200e^{-L^{a_{i_*}}}\). Hence the failing set \(E(T_f)\) has measure at most \(\exp(-L^{a_{i_*}}+o(L^{a_{i_*}}))\). Let \(\Pi(r)\) be the probability over \(T_f\) that \(r\in E(T_f)\). Then \(\int\Pi(r)\,dr\le\exp(-L^{a_{i_*}}+o(L^{a_{i_*}}))\), and by Markov's inequality the set where \(\Pi(r)>\exp(-\frac14L^{a_{i_*}})\) has measure at most \(\exp(-\frac34L^{a_{i_*}}+o(L^{a_{i_*}}))\). There are \(2^K-1\) sets \(I\), and \(a_{i_*}>0.1\). \(\square\)

The operator used in the moment is

\[
\begin{gathered}
\mathcal A=\mathcal G\mathcal S\mathcal T\mathcal S\mathcal G .\quad(3.1)
\end{gathered}
\]

## 4. Endpoint vectors and the lift

For a positive integer \(n\), let \(G(n)\) be its largest divisor composed of group primes. Define functions on states by

\[
\begin{gathered}
f(P,\mathbf p)=\overline{\alpha_{P_1/G(P_1)}}\,\beta_{P_2},\\
g(P,\mathbf p)=\overline{\alpha_{P_1/G(P_1)}}\,\beta_{P_2},\quad(4.1)
\end{gathered}
\]

when \(G(P_1)\) is squarefree with exactly \(M\) prime factors in every group, and \(f=g=0\) otherwise. On their support the lists at \(P\) are orderings of the primes of \(G(P_1)\), so \(f\) and \(g\) do not depend on the order and \(\mathcal Sf=f\), \(\mathcal Sg=g\). (They are equal; two names make the formulas below easier to read.)

**Lemma 4.1 (the lift).** Let \((P,\mathbf p)\) be in the support of \(f\), and \((Q,\mathbf p')\) a target of it in the support of \(g\), with \(\mathcal K\ne0\). Write \(D,b,a\) for the shared and unshared products. Then

\[
\begin{gathered}
P=(Dbm,s),\qquad Q=(Dar,n),\\
\frac{\det(P,Q)}D=bmn-ars,\quad(4.2)
\end{gathered}
\]

where \(m=P_1/G(P_1)\), \(s=P_2\), \(r=Q_1/G(Q_1)\), \(n=Q_2\), and \(f(P,\mathbf p)\) and \(g(Q,\mathbf p')\) involve \(\alpha_m,\beta_s\) and \(\alpha_r,\beta_n\). The damping factor in (2.2) equals \(1\). Conversely, for every choice of an ordered pad list with \(D\in[d_0,2d_0)\), of marking products \(a,b\in[Y,4Y]\), and of \(m,n,r,s\) in the supports of \(\alpha,\beta\), such that all primes of the pads, \(a\) and \(b\) are distinct and \(\psi((bmn-ars)/Y)\ne0\), the vectors \((Dbm,s)\) and \((Dar,n)\) are primitive and lie in \(\Omega\).

**Proof.** On the support of \(f\), \(G(P_1)\) has exactly the \(KM\) primes of the lists, which split into the shared ones (product \(D\)) and the last slots (product \(b\)); so \(P_1=Dbm\). Likewise \(Q_1=Dar\), since the target list consists of the shared primes and the new last slots. Then \(\det(P,Q)=Dbm\,n-s\,Dar\). The coefficients \(\alpha\) are supported on rough integers, so \(m\) and \(r\) have no marks, and \(\omega(P_1)=\omega(Q_1)=KM\).

For the converse, the ranges are clear: \(Dbm\in[d_0YH_m,16d_0YH_m]\). Suppose a prime \(\ell\) divides \(Dbm\) and \(s\). Since \(s\) is rough, \(\ell>W\), so \(\ell\) does not divide \(Db\), whose primes are group primes, and hence \(\ell\mid m\). Then \(\ell\) divides \(t=bmn-ars\). But \(|t|\le5Y<W<\ell\) on the support of \(\psi\), so \(t=0\), that is \(bmn=ars\). A prime of \(b\) is then a group prime dividing \(ars\); it does not divide \(a\) (all labels are distinct) nor \(r,s\) (rough). This is impossible because \(b>1\). The same argument applies to \((Dar,n)\). Finally, every prime of \(D,a,b\) divides the first coordinates as required, so the lists are admissible. \(\square\)

**Lemma 4.2 (norms of the endpoint vectors).** \(\sup|f|,\sup|g|\le L^{2C}\) and \(\|f\|^2,\|g\|^2\le32L^{4C}UV\).

**Proof.** The first bound is clear. For the second, fix an ordered choice of lists with product \(G\) and distinct entries in each group. The positions \(P\in\Omega\) with \(G\mid P_1\) number at most \((16U/G)(V+1)\le32UV/G\). Summing over the lists with the measure \(\prod_iV_i^{-M}\),

\[
\begin{gathered}
\|f\|^2\le32L^{4C}UV\\
\times\prod_{i=1}^K\Bigl(V_i^{-M}\Bigl(\sum_{p\in\mathcal P_i}\frac1p\Bigr)^M\Bigr)\\
=32L^{4C}UV. \ \square
\end{gathered}
\]

The bound has no factor depending on \(K\) or \(J\): the measure (2.1) is chosen so that the harmonic sums cancel exactly.

## 5. The pairing and the pads

**Proposition 5.1 (the pairing identity).** Let \(\Pi(a,b)\) be the probability that \(J\) independent draws from \(\mu_i\) in every group are distinct from each other and from the primes of \(a\) and \(b\). Then

\[
\begin{gathered}
\sum_{d_0}\frac{\langle f,\mathcal Tg\rangle}{d_0}=\frac1{(V_1\cdots V_K)^2}\\
\times\sum_{(a,b)=1}\Pi(a,b)\,\eta\Bigl(\frac aY\Bigr)\eta\Bigl(\frac bY\Bigr)\\
\times\sum_{m,n,r,s}\alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s}\\
\times\mathcal K^{\rm min}(bmn-ars;a,b),\quad(5.1)
\end{gathered}
\]

the outer sum over powers of two \(d_0\), where \(\mathcal K^{\rm min}(t;a,b)\)\(=\psi(t/Y)\int_{\mathbb T\setminus\mathfrak M}e(\theta(t-b+a))\,d\theta\).

**Proof.** Expand \(\langle f,\mathcal Tg\rangle=\sum\sigma\,\overline{f}\,\prod_iV_i^{-1}\mathcal K\,g\). By Lemma 4.1, the nonzero terms correspond bijectively to the data listed there: an ordered list at \(P\) is the same as an ordered pad list followed by the primes of \(b\), and the target adds the primes of \(a\). The ban makes \(a\) and \(b\) coprime. The weight of a term is

\[
\begin{gathered}
\prod_iV_i^{-(M+1)}\frac{d_0}D\\
=d_0\prod_{i,h}\mu_i(p_{i,h})\cdot\prod_iV_i^{-2},
\end{gathered}
\]

because \(M+1=J+2\) and \(\prod_{i,h}\mu_i(p_{i,h})=D^{-1}\prod_iV_i^{-J}\). The factor \(\overline f g\) is \(\alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s}\), and \(\psi(t/Y)\{\mathbf 1_{t=b-a}-\int_{\mathfrak M}\}=\mathcal K^{\rm min}\) by (5.4) of Lesson 7. Dividing by \(d_0\) and summing over the dyads, every ordered pad list occurs exactly once, and the sum of \(\prod\mu_i(p_{i,h})\) over the admissible pad lists is \(\Pi(a,b)\). \(\square\)

**Corollary 5.2 (stripping the pads).** For every fixed \(A\),

\[
\begin{gathered}
\Bigl|\sum_{d_0}\frac{\langle f,\mathcal Tg\rangle}{d_0}-\mathcal Q_Y^{\rm min}\Bigr|\\
\ll_AXYL^{-A}.\quad(5.2)
\end{gathered}
\]

**Proof.** The minor sum \(\mathcal Q_Y^{\rm min}\) is (5.1) with \(\Pi(a,b)\) replaced by \(1\). By a union bound over pairs of pad draws in the same group and over coincidences of a pad with one of the two primes of \(a\) and \(b\) in its group, \(1-\Pi(a,b)\)\(\le K(J^2+2J)\max_{i,p}\mu_i(p)\)\(\le6KM^2e^{-L^{0.1}}\), by Lemma 1.2 of Lesson 2; two independent draws from \(\mu_i\) coincide with probability \(\sum_p\mu_i(p)^2\le\max_p\mu_i(p)\). Split \(\mathcal K^{\rm min}=\mathbf 1_{t=b-a}-\mathcal H_{\mathfrak M}\). For coprime \(a,b\) the first part is the indicator of Lemma 4.1 of Lesson 7, and the absolute bounds (6.1) and (6.2) of Lemma 6.1 there bound the two parts by \(O(XYL^{C_2+3A_0})\). Multiplying by \(6KM^2e^{-L^{0.1}}\) gives (5.2). \(\square\)

So the minor estimate of Lesson 7 follows from a bound for \(\langle f,\mathcal Tg\rangle\) uniform in the \(O(L^{0.21})\) dyads \(d_0\). Lesson 9 bounds \(\langle f,\mathcal Ag\rangle\), and [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md) shows that the good-state projections in \(\mathcal A\) change the pairing by a negligible amount.

## 6. Exercises

**8.1.** Show that \(r_P\) is independent of the completion and that \(r_{-P}=r_P\).

**8.2.** Show that \(\mathcal S\) is self-adjoint and idempotent on \(\mathcal H\).

**8.3.** In Lemma 4.1, explain why primitivity of \((Dbm,s)\) would fail without the cutoff \(\psi(t/Y)\) if one allowed \(t=0\) with \(bmn=ars\), and why the ban excludes this.

**8.4.** Compute the total weight \(\sum\prod_{i,h}\mu_i(p_{i,h})\) over all ordered pad lists, without any distinctness condition, and compare with \(\Pi(a,b)\).

**8.5.** Show that a state with \(\mathcal K\ne0\) on some outgoing edge has \(\eta(b/Y)\ne0\), and deduce that its first coordinate is at least \(d_0Y\) times the product of its non-label part.

## 7. Solutions

**8.1.** Two completions \(W,W'\) of \(P\) satisfy \(\det(P,W-W')=0\), so \(W-W'=jP\) for an integer \(j\), because \(P\) is primitive; then \(W_1'/P_1=W_1/P_1-j\). For \(-P\), the matrix with columns \(-P,-W\) has determinant one, and \((-W_1)/(-P_1)=W_1/P_1\).

**8.2.** The measure \(\sigma\) is constant, and a reordering \(\pi\) is a bijection of states, so \(\langle\phi\circ\pi,\psi\rangle=\langle\phi,\psi\circ\pi^{-1}\rangle\). Averaging over the group of reorderings gives \(\mathcal S^*=\mathcal S\), and \(\mathcal S^2=\mathcal S\) because the average of an average over a group is the same average.

**8.3.** If \(t=0\), a common large prime \(\ell\) of \(m\) and \(s\) is not excluded by the argument, since \(\ell\mid t\) gives no information. The relation \(bmn=ars\) cannot hold because the primes of \(b\) would have to divide \(a\), which the ban forbids.

**8.4.** Each draw has total mass \(1\), so the total weight is \(1\). The admissible lists form a subset of probability \(\Pi(a,b)\), which differs from \(1\) by \(O(KM^2e^{-L^{0.1}})\).

**8.5.** By (2.2), \(\mathcal K\ne0\) forces \(\eta(b/Y)\ne0\), so \(b\ge Y\). The first coordinate is divisible by the product of all list primes, \(Db\ge d_0Y\), and by its non-label part.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 3.2 and Section 4.9. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
