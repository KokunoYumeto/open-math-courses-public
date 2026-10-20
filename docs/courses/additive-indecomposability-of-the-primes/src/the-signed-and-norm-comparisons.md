# The signed and norm comparisons

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the comparison estimates, Proposition 6.1 of Lesson 14. After Lessons 15 and 16, every comparison expression has been reduced, up to negligible errors, to an integral in which the top giants and the bulk primes are ideal: real logarithmic coordinates, independent uniform residues modulo the spectator product \(d\), and residues modulo the frequency modulus \(Q_f\). The only factor that sees the bulk residues modulo \(d\) is the product of the tree values at the spectators.

For the *signed* comparison (6.2) of Lesson 14, the two assignments couple the bulk residues at each spectator only through products over the components of the overlap graph. When there are at most \(3r/4\) components, this is exactly the setting of the finite-field tree comparison, so the correlation at each spectator tends to zero, and the \(m\) spectators are independent (Proposition 2.2). For the *norm* estimate (6.1) of Lesson 14, positivity allows crude bounds at the spectators. The work is in the frequency sums: each node's integrality condition fixes the square of a bulk product modulo a divisor of its frequency, and summing the resulting probabilities over all frequencies costs only the factor \(e^{r\Delta_0}\) allowed by (6.1) (Proposition 3.3).

**Prerequisites.** [*Small primes, coincidences and the bulk*](small-primes-coincidences-and-the-bulk.md); [*Diagrams, densities and cycles over a finite field*](diagrams-densities-and-cycles-over-a-finite-field.md), Lemma 1.2 and Proposition 2.1.

The notation of Lessons 14–16 is in force.

## 1. The law of the bulk residues at a spectator

Condition, in the main expression left after Proposition 3.1 of Lesson 16, on the real coordinates, the \(Q_f\) coordinates, the values of all nonbulk primes, and the residues of the top giants. Then the residues of the bulk primes modulo \(d\) are independent uniform units, and by the Chinese remainder theorem their reductions modulo the different spectators \(q\mid d\) are independent.

Fix a spectator \(q\). For each of the two assignments, the leaf variables of its diagram at \(q\) are the products of the bulk residues in each leaf.

**Lemma 1.1** (the coupling of the leaf products [OpenAI-013, Section 8.7]). In each assignment, the \(r\) leaf products are independent uniform units modulo \(q\). Jointly, the \(2r\) leaf products of the two assignments are uniform on the subgroup of \(U^r\times U^r\) defined as follows: for every connected component of the overlap graph, the product of the leaf products of the first assignment over the component's left vertices equals the product of those of the second assignment over its right vertices.

*Proof.* Each leaf uses a disjoint nonempty set of bulk slots, so the leaf products of one assignment are independent uniform units. Regard every bulk slot, with its uniform unit value, as an edge of the overlap multigraph, joining its leaf in the first assignment to its leaf in the second; its value enters the product at both endpoints. The map from edge values to vertex products is a homomorphism of finite abelian groups. Its image lies in the stated subgroup, because in each component both sides equal the product of the component's edge values. Conversely, given vertex products satisfying the relation in every component, choose a spanning tree of each component and set the edges outside the trees to \(1\); then repeatedly remove a vertex of degree one in the remaining tree and give its tree edge the value its prescribed product requires. The last vertex of each component is then satisfied by the relation. So the image is the whole subgroup, and a homomorphism of finite groups carries the uniform distribution to the uniform distribution on its image. \(\square\)

## 2. The signed comparison

The diagrams at the spectator \(q\) satisfy the hypotheses of Lesson 12. Their frequencies and nonbulk constants are units modulo \(q\); the parent and child relations are those of (1.2) of Lesson 12, by the identification of Section 1 of Lesson 15; and the zero convention of the diagrams encodes the inserted-giant unit conditions at \(q\). The transform is \(g=g_q\), with \(g_q(0)=0\) and \(\mathbb E|g_q|^2=1\), and its correlation parameter \(\epsilon_q\) of (1.1) of Lesson 12 is at most
\[
\max_{\chi,a}\Bigl|\mathbb E_{v\in\mathbb F_q}g_q(v)\chi(v)e_q(av)\Bigr|,
\]
which tends to zero uniformly on the spectator subset chosen in Lesson 14, by Theorem 6.1 of Lesson 9.

**Lemma 2.1.** If \(l\ge2\) and the overlap graph has at most \(3r/4\) components, then, uniformly in the conditioned data, the absolute correlation \(|\mathbb E\,W_{1,q}\overline{W_{2,q}}|\) at every spectator \(q\) is at most \(\epsilon_k(L)\), where \(\epsilon_k(L)\to0\) as \(L\to\infty\).

*Proof.* By Lemma 1.1, the leaf variables have exactly the coupled law of Lemma 1.2 of Lesson 12, with the components of the overlap graph as the paired sets, and \(b\le3r/4\). That lemma bounds the correlation by \(C_l(\epsilon_q+q^{-1/4})\). The spectator primes satisfy \(\log\log q\ge0.0005L\), so \(q^{-1/4}\to0\), and \(\epsilon_q\to0\) uniformly. \(\square\)

**Proposition 2.2** (the signed comparison [OpenAI-013, (7.18)]). Under the hypotheses of (6.2) of Lesson 14,
\[
\begin{aligned}
&\Bigl|\mathbb E\sum_s\mathcal G\,K_{\rm ar}\,A^{(1)}_l(s)\\
&\qquad \overline{A^{(2)}_l(s)}\Bigr|\le\epsilon_k(L)^m\exp(O_k(m))\\
&\qquad +O\bigl(\exp(-e^{0.00125L})\bigr)\\
&\quad =\exp(-\omega_k(m)),
\end{aligned}
\]
with \(\omega_k(m)/m\to\infty\).

*Proof.* After the reductions of Lessons 15 and 16, the expression equals, up to the errors (4.4) of Lesson 15, (2.2) and (3.2) of Lesson 16, an integral over the conditioned data of the expectation over the bulk residues modulo \(d\) of the spectator product (1.4) of Lesson 15. By independence over the spectators, this expectation is the product over \(q\mid d\) of the correlations of Lemma 2.1, hence at most \(\epsilon_k(L)^m\) in absolute value. The integral over the conditioned data costs at most \(\exp(O_k(m))\): this covers the representative domination (1.3) of Lesson 16, the bounded masses, the factor \(|\Xi|\le e^{-r\Delta_0}\) of (1.5) of Lesson 15 against the leaf frequency count, and the sums over histories, which number \(\exp(O_k(m))\). Since \(\epsilon_k(L)\to0\), \(\epsilon_k(L)^me^{O_k(m)}=\exp(-\omega_k(m))\); and \(m=O_k(L)\), so \(\exp(-e^{0.00125L})\) is also \(\exp(-\omega_k(m))\). \(\square\)

This is where the spectators do their work. They are shared by all leaves of both assignments, so each spectator sees the whole binary tree; the tree comparison turns the few-component hypothesis into decorrelation at each spectator; and the number \(m\) of spectators, proportional to the number of bulk variables per leaf, makes the total decorrelation beat the combinatorial factor of order \(e^{O(m)}\) from everything else.

## 3. The norm comparison

For (6.1) of Lesson 14 the two histories use the same assignment, and only an upper bound is needed.

**Crude bounds.** At the spectators, (1.4) of Lesson 12 and Cauchy–Schwarz bound the expectation of the absolute product of the two tree values by \(3^r\) at each spectator, hence by \(3^{rm}\) in total. Keep the frequency divisibility conditions, and discard the exceptional multipliers at a cost \(2^{rm+O(1)}\). For the upper bound, the bulk coordinates modulo \(Q_f\) are then independent uniform units.

**Exposure.** The two histories use the same assignment, so their bulk slots split into the same subtrees. Expose the product of all bulk slots, and then, going down from the root, the product over one child subtree at each split. Conditionally on a parent product, the product \(M_+\) of one child is uniform on the units modulo \(Q_f\), and \(M_-\) is determined by \(M_+M_-\): this is the product map on two disjoint collections of independent uniform units. The ancestor pivots of both histories depend only on splits already exposed and are known with the precision provided by (1.1) of Lesson 15. The support conditions are evaluated under this Haar measure, without first conditioning on the validity of the complete histories: all frequencies are fixed at the outset, the unit conditions of a current giant against later frequencies depend only on exposed data, the conditions on a newly created pivot are evaluated after the split that creates it, and conditions on later pivots are deferred to their own splits or discarded. So the conditions kept at earlier splits never select an unexposed split.

**Lemma 3.1** (one split [OpenAI-013, (8.28)–(8.30)]). At a node with frequency \(s\) and child frequencies \(v,w\) in one history, and \(s',v',w'\) in the other, the conditional probability that both integrality conditions hold at the split is at most
\[
\begin{gathered}
\frac{\exp(o_k(m))}{[a,a']},\\
a=\frac{|s|}{(v,w,s)},\\
a'=\frac{|s'|}{(v',w',s')},
\end{gathered}
\]
where \([a,a']\) is the least common multiple.

*Proof.* The support requires \(X_\pm C_\pm\) to be units modulo the node frequency; if this fails, the branch contributes zero. Otherwise integrality is the congruence
\[
vX_-C_-M_-\equiv wX_+C_+M_+\pmod{|s|}.
\]
All factors other than \(v,w\) are units, and congruent integers have the same greatest common divisor with \(s\), so the congruence forces \((v,s)=(w,s)\), which then equals \(g=(v,w,s)\). Dividing by \(g\), both frequency coefficients become units modulo \(a=|s|/g\). Substituting \(M_-=M/M_+\) with the known parent product \(M\), the congruence fixes \(M_+^2\) to a specified unit modulo \(a\). The other history fixes \(M_+^2\) modulo \(a'\). A unit has at most two square roots modulo an odd prime power and at most four modulo a power of \(2\), so the two congruences have at most \(2^{\omega([a,a'])+1}\) common solutions modulo \([a,a']\), or none. The reduction of \(M_+\) modulo \([a,a']\), a divisor of \(Q_f\), is uniform on the units, so the probability is at most \(2^{\omega(n)+1}/\varphi(n)\) with \(n=[a,a']\le\exp(O_k(m))\). The divisor bounds of Section 5 of Lesson 8 give \(2^{\omega(n)+1}n/\varphi(n)=\exp(o_k(m))\). \(\square\)

All earlier conditions are measurable with respect to the earlier exposed products, so these conditional bounds multiply along the tree; failed conditions contribute zero and do not affect the upper bound.

**Lemma 3.2** (the lcm sum [OpenAI-013, (8.31)]). For \(V\ge1\),
\[
\sum_{a,a'\le V}\frac1{[a,a']}\ll(1+\log V)^3 .
\]

*Proof.* Write \(a=du\) and \(a'=du'\) with \(d=(a,a')\) and \((u,u')=1\); then \([a,a']=duu'\). Dropping the coprimality condition, the sum is at most \(\sum_{d\le V}\frac1d\bigl(\sum_{u\le V/d}\frac1u\bigr)^2\ll(1+\log V)^3\). \(\square\)

**Proposition 3.3** (the norm comparison [OpenAI-013, (7.17)]). Under the hypotheses of (6.1) of Lesson 14,
\[
\begin{aligned}
&\mathbb E\sum_{0<|s|\le V_l}\mathcal G\,|A_l(s)|^2\\
&\quad \le\exp\bigl(r(\Delta_0+Cm)+o_k(m)\bigr),
\end{aligned}
\]
with \(C\) independent of large \(k\) and of the gap constants.

*Proof.* *The internal frequencies.* With the child frequencies \(v,w\) fixed, every \(s\) giving a prescribed value \(a=|s|/(v,w,s)\) has the form \(s=\pm ag\) with \(g\mid(v,w)\), so it has multiplicity at most \(2\tau((v,w))\); the same holds in the other history. These greatest common divisors and all frequencies are at most \(\exp(O_k(m))\), so by Lemmas 3.1 and 3.2 each pair of internal frequencies, summed with its children fixed, contributes a factor \(\exp(o_k(m))\). Drop the equality of the two root frequencies if necessary, since only an upper bound is needed; sum the root pair first with its children fixed, and proceed down the tree.

*The leaves.* Only the \(2r\) leaf frequencies remain, with at most \((2V_0)^{2r}\) choices. With \(|\Xi|\le e^{-r\Delta_0+O_k(1)}\) from (1.5) of Lesson 15 and \(E_0=\Delta_0+\sqrt m\),
\[
\begin{aligned}
&(2V_0)^{2r}e^{-r\Delta_0+O_k(1)}\\
&\quad =\exp\bigl(r\Delta_0+o_k(m)\bigr).
\end{aligned}
\]

*The other losses.* The spectator bound \(3^{rm}\), the exceptional multipliers \(2^{rm+O(1)}\), the bounded masses, the representative domination (1.3) of Lesson 16, and the \(O_k(1)\) equality patterns all fit into \(\exp(Crm+o_k(m))\). The constant is absolute: the number of internal samples is \(O(kr)\), so (1.3) of Lesson 16 costs \(\exp(CkrL)\), and \(kL/m\asymp k^{-3}\). Constants depending on \(k\) but not proportional to \(m\) are absorbed into \(o_k(m)\). In the diagonal environment, \(\mathcal G\) contributed the factor (1.1) of Lesson 16, at most \(1\). Adding the negligible approximation errors of Lessons 15 and 16 proves the bound. \(\square\)

Propositions 2.2 and 3.3 together prove Proposition 6.1 of Lesson 14. \(\square\)

## 4. Exercises

**4.1.** Let \(G\) be a finite abelian group and \(\phi\colon G^E\to G^V\) the map sending edge values of a connected bipartite multigraph with vertex classes \(V_1\sqcup V_2=V\) to the vertex products. Show that the image of \(\phi\) has index \(|G|\) in \(G^V\) when \(E\ne\emptyset\).

**4.2.** Show that for every positive integer \(n\), \(n/\varphi(n)\le2^{\omega(n)}\), and give the case of equality.

**4.3.** Let \(a\) be an odd prime power and \(c\) a unit modulo \(a\). Show that \(x^2\equiv c\pmod a\) has at most two solutions, and give an example modulo \(8\) with four.

**4.4.** Show that \(\sum_{d\mid n}1\le n^{O(1/\log\log n)}\) implies \(2^{\omega(n)}=\exp(o(\log n))\), and deduce \(2^{\omega(n)}=\exp(o_k(m))\) for \(n\le\exp(O_k(m))\).

## 5. Solutions

**4.1.** By the spanning-tree argument of Lemma 1.1, the image is the subgroup defined by the single relation \(\prod_{v\in V_1}x_v=\prod_{v\in V_2}x_v\), which is the kernel of the surjective homomorphism \(x\mapsto\prod_{V_1}x_v\prod_{V_2}x_v^{-1}\) from \(G^V\) onto \(G\). So its index is \(|G|\).

**4.2.** \(n/\varphi(n)=\prod_{p\mid n}(1-1/p)^{-1}\), and each factor is at most \(2\), with equality only at \(p=2\). So equality holds exactly for \(n\) a power of \(2\), including \(n=1\).

**4.3.** The units modulo an odd prime power form a cyclic group of even order, in which \(x\mapsto x^2\) has kernel \(\{\pm1\}\), so each square has exactly two roots. Modulo \(8\), \(x^2\equiv1\) has the four solutions \(1,3,5,7\).

**4.4.** \(2^{\omega(n)}\le\tau(n)\), the number of divisors. If \(\tau(n)\le n^{C/\log\log n}\), then \(\log2^{\omega(n)}\le C\log n/\log\log n=o(\log n)\). For \(n\le\exp(O_k(m))\), \(\log n=O_k(m)\), so \(2^{\omega(n)}=\exp(o_k(m))\).

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Sections 8.7–8.8: the signed comparison, the norm comparison and the frequency sums, (8.28)–(8.32). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
