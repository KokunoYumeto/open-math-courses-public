# One tile with a cyclic finite coordinate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Theorem 6.2 of [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md) gives finitely many tiles in \(\mathbb Z^2\times V\), \(V\) cyclic, whose equations have a common solution but no fully periodic one. This lesson replaces the finitely many equations by one [OpenAI-PT, Section 6]. A new coordinate \(\mathbb Z/q\mathbb Z\) is added and partitioned into \(s\) sets, one for each equation, and the stacked tile is the union of the products of the tiles with these sets. If each set meets all of its own translates, the stacked tile tiles exactly when the system has a common solution, and periodicity passes in both directions. Choosing \(q\) prime and coprime to \(\#V\) keeps the finite factor \(V\times\mathbb Z/q\mathbb Z\) cyclic. The construction is a version of the stacking of Greenfeld and Tao [Greenfeld–Tao 2024, Theorem 3.1 and Lemma 3.2; Greenfeld–Tao 2023, Theorem 1.15].

- A partition with full difference sets (Section 1).
- Stacking (Section 2).
- One tile with a cyclic coordinate (Section 3).

Tilings, multiplicities and full periodicity are as in [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md). From the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30) (Judson, *Abstract Algebra: Theory and Applications*) we use that there are infinitely many primes ([Theorem 2.2.6](https://judsonbooks.org/aata-files/aata-html/integers-section-division-algorithm.html)) and that \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\cong\mathbb Z/mn\mathbb Z\) for coprime \(m,n\) ([Theorem 9.2.9](https://judsonbooks.org/aata-files/aata-html/isomorph-section-direct-products.html)). Probabilities in Section 1 are those of the uniform distribution on a finite set, that is, proportions of a finite number of cases.

## 1. A partition with full difference sets

For subsets \(E,E'\) of a group we write \(E-E'=\{e-e':e\in E,\ e'\in E'\}\).

**Lemma 1.1** (a partition with full difference sets; [OpenAI-PT, Lemma 6.1]). For every integer \(s\ge1\) and every finite set of primes there is a prime \(q\) outside that set and a partition
\[
\mathbb Z/q\mathbb Z=E_1\sqcup\cdots\sqcup E_s
\]
into nonempty sets with \(E_\nu-E_\nu=\mathbb Z/q\mathbb Z\) for every \(\nu\).

*Proof.* For \(s=1\), \(E_1=\mathbb Z/q\mathbb Z\) works for every prime \(q\). Let \(s\ge2\) and let \(q\) be an odd prime. Color the \(q\) elements of \(\mathbb Z/q\mathbb Z\) with \(s\) colors, all \(s^q\) colorings being equally likely; then the colors of different elements are independent and uniform. Fix a color \(\nu\) and \(d\ne0\) in \(\mathbb Z/q\mathbb Z\). Since \(q\) is prime, \(0,d,2d,\ldots,(q-1)d\) are the \(q\) distinct elements of \(\mathbb Z/q\mathbb Z\), so the \((q-1)/2\) pairs
\[
\begin{gathered}(0,d),\ (2d,3d),\ \ldots,\\ \bigl((q-3)d,(q-2)d\bigr)\end{gathered}
\]
are disjoint, and in each the second element minus the first is \(d\). A pair has color \(\nu\) at both ends with probability \(s^{-2}\), independently for the disjoint pairs. If \(d\notin E_\nu-E_\nu\), where \(E_\nu\) is the set of elements of color \(\nu\), no pair has color \(\nu\) at both ends, which has probability \((1-s^{-2})^{(q-1)/2}\). By the union bound over the \(s\) colors and the \(q-1\) nonzero \(d\), the probability that some color misses some nonzero difference is at most
\[
s(q-1)(1-s^{-2})^{(q-1)/2}.
\]
For fixed \(s\) this tends to \(0\) as \(q\to\infty\), since \(1-s^{-2}<1\). There are infinitely many primes, so we can choose an odd prime \(q\) outside the given set for which the bound is less than \(1\), and then a coloring for which every color realizes every nonzero difference. Every color class is then nonempty, so it also realizes the difference \(0\). \(\square\)

## 2. Stacking

**Proposition 2.1** (stacking and periodicity; [OpenAI-PT, Proposition 6.2]). Let \(H\) be an abelian group, \(F_1,\ldots,F_s\subseteq H\) finite and nonempty, and \(\mathbb Z/q\mathbb Z=E_1\sqcup\cdots\sqcup E_s\) a partition as in Lemma 1.1. Put
\[
F^{\rm st}=\bigcup_{\nu=1}^s\bigl(F_\nu\times E_\nu\bigr)\subseteq H\times\mathbb Z/q\mathbb Z .
\]

1. The system \(A\oplus F_\nu=H\), \(1\le\nu\le s\), has a common solution exactly when \(F^{\rm st}\) tiles \(H\times\mathbb Z/q\mathbb Z\).
2. A fully periodic common solution gives a fully periodic tiling set of \(F^{\rm st}\), and a fully periodic tiling set of \(F^{\rm st}\) gives a fully periodic common solution.

*Proof.* The union defining \(F^{\rm st}\) is disjoint, since the \(E_\nu\) are.

*From a common solution to a tiling.* Let \(A\) be a common solution and \((g,t)\in H\times\mathbb Z/q\mathbb Z\). A representation \((g,t)=(a,0)+(f,e)\) with \(a\in A\) and \((f,e)\in F_\mu\times E_\mu\) needs \(e=t\), so \(\mu\) is the unique \(\nu\) with \(t\in E_\nu\), and then \(g=a+f\) with \(f\in F_\nu\), which has exactly one solution. So \((A\times\{0\})\oplus F^{\rm st}=H\times\mathbb Z/q\mathbb Z\). If \(A+\Lambda=A\) with \([H:\Lambda]<\infty\), then \(\Lambda\times\{0\}\) has finite index \([H:\Lambda]\cdot q\) and preserves \(A\times\{0\}\).

*From a tiling to a common solution.* Let \(B\oplus F^{\rm st}=H\times\mathbb Z/q\mathbb Z\) and fix \(g\in H\). A *contribution of color \(\nu\)* to the fibre \(\{g\}\times\mathbb Z/q\mathbb Z\) is a pair \(\bigl((a,t),f\bigr)\) with \((a,t)\in B\), \(f\in F_\nu\) and \(a+f=g\); it covers the points \((g,t+e)\), \(e\in E_\nu\), that is, the set \(\{g\}\times(t+E_\nu)\). Two distinct contributions of the same color cannot both occur: if \(\bigl((a,t),f\bigr)\) and \(\bigl((a',t'),f'\bigr)\) are contributions of color \(\nu\), then \(t'-t\in\mathbb Z/q\mathbb Z=E_\nu-E_\nu\), say \(t'-t=e-e'\), so the point \((g,t+e)=(g,t'+e')\) has the representations \((a,t)+(f,e)\) and \((a',t')+(f',e')\), which must coincide. Let \(n_\nu(g)\in\{0,1\}\) be the number of contributions of color \(\nu\). Every point of the fibre is covered exactly once, and every representation of such a point belongs to exactly one contribution, so
\[
\sum_{\nu=1}^sn_\nu(g)\,\#E_\nu=q=\sum_{\nu=1}^s\#E_\nu .
\]
Since every \(\#E_\nu\) is positive and \(n_\nu(g)\le1\), every \(n_\nu(g)=1\).

Let \(\operatorname{pr}\colon H\times\mathbb Z/q\mathbb Z\to H\) be the projection. It is injective on \(B\): if \((a,t)\ne(a,t')\) were both in \(B\), then with any \(f\in F_1\) they would give two distinct contributions of color \(1\) at \(g=a+f\). Put \(A=\operatorname{pr}(B)\). The contributions of color \(\nu\) at \(g\) correspond to the pairs \((a,f)\in A\times F_\nu\) with \(a+f=g\), so \(r_{A,F_\nu}(g)=n_\nu(g)=1\). Thus \(A\oplus F_\nu=H\) for every \(\nu\).

If moreover \(B+\Pi=B\) for a subgroup \(\Pi\) of finite index in \(H\times\mathbb Z/q\mathbb Z\), then \(A+\operatorname{pr}(\Pi)=\operatorname{pr}(B+\Pi)=A\), and \(\operatorname{pr}(\Pi)\) has finite index in \(H\), because the map \((H\times\mathbb Z/q\mathbb Z)/\Pi\to H/\operatorname{pr}(\Pi)\) induced by \(\operatorname{pr}\) is surjective. \(\square\)

## 3. One tile with a cyclic coordinate

**Corollary 3.1** (one tile with a cyclic finite coordinate; [OpenAI-PT, Corollary 6.3]). There are a positive integer \(Q\) and a finite nonempty set \(F\subseteq\Gamma=\mathbb Z^2\times\mathbb Z/Q\mathbb Z\) such that \(F\) tiles \(\Gamma\), but no tiling set of \(F\) is invariant under a subgroup of finite index of \(\Gamma\). Moreover \(\#F=qM\), where \(M\) is the common size of the tiles of the system and \(q\) is a prime.

*Proof.* Take the system \(F_1,\ldots,F_s\subseteq G=\mathbb Z^2\times V\) of Theorem 6.2 of [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md), and by Lemma 1.1 a prime \(q\nmid\#V\) with a partition of \(\mathbb Z/q\mathbb Z\) as there. By Proposition 2.1, the stacked tile \(F^{\rm st}\subseteq G\times\mathbb Z/q\mathbb Z=\mathbb Z^2\times(V\times\mathbb Z/q\mathbb Z)\) tiles, since the system has a common solution, and has no fully periodic tiling set, since a fully periodic tiling set would give a fully periodic common solution. The group \(V\) is cyclic of order coprime to \(q\), so \(V\times\mathbb Z/q\mathbb Z\) is cyclic of order \(Q=q\,\#V\) by Theorem 9.2.9 of Judson. Transport \(F^{\rm st}\) by an isomorphism \(\mathbb Z^2\times V\times\mathbb Z/q\mathbb Z\cong\mathbb Z^2\times\mathbb Z/Q\mathbb Z\) that is the identity on \(\mathbb Z^2\); by Lemma 1.2(1) of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md) this keeps both properties. Every tile of the system has \(M=\#H_0\) elements, so \(\#F=\sum_\nu M\,\#E_\nu=qM\). \(\square\)

The group \(\Gamma=\mathbb Z^2\times\mathbb Z/Q\mathbb Z\) is the quotient of \(\mathbb Z^3\) by the subgroup generated by \((0,0,Q)\). The last lesson, [Passing to three-dimensional space](passing-to-three-dimensional-space.md), lifts \(F\) to a tile of \(\mathbb Z^3\) and of \(\mathbb R^3\).

## 4. Exercises

**4.1.** Show that \(\{0,1,3\}\) and \(\{2,4,5,6\}\) form a partition of \(\mathbb Z/7\mathbb Z\) with full difference sets.

**4.2.** Find the least odd prime \(q\) with \(2(q-1)(3/4)^{(q-1)/2}<1\), the bound of Lemma 1.1 for \(s=2\). Compare with Exercise 4.1.

**4.3.** Let \(E\subseteq\mathbb Z/q\mathbb Z\) with \(E-E=\mathbb Z/q\mathbb Z\). Show that \(\#E(\#E-1)\ge q-1\) and \(\#E>\sqrt q\). Deduce that a partition as in Lemma 1.1 has \(s<\sqrt q\).

**4.4.** Let \(s=1\). Show directly that \(B\oplus(F_1\times\mathbb Z/q\mathbb Z)=H\times\mathbb Z/q\mathbb Z\) holds exactly when \(\operatorname{pr}\) is injective on \(B\) and \(\operatorname{pr}(B)\oplus F_1=H\).

**4.5.** Explain where the proof of Corollary 3.1 uses that \(q\) does not divide \(\#V\), and what would be lost for \(q\mid\#V\).

## 5. Solutions

**4.1.** The differences of distinct elements of \(\{0,1,3\}\) are \(\pm1,\pm2,\pm3\), which are all nonzero residues modulo \(7\). For \(\{2,4,5,6\}\): \(4-2=2\), \(5-2=3\), \(6-2=4\), \(5-4=1\), and their negatives \(5,4,3,6\) give all nonzero residues. Both sets contain the difference \(0\).

**4.2.** For \(q=23\): \(44\cdot(3/4)^{11}\approx1.86\). For \(q=29\): \(56\cdot(3/4)^{14}\approx0.998<1\). The primes \(q\le23\) all give values larger than \(1\), so \(q=29\) is the least. Exercise 4.1 shows that partitions exist for smaller \(q\): the union bound is crude.

**4.3.** Each nonzero element of \(\mathbb Z/q\mathbb Z\) is \(e-e'\) for an ordered pair of distinct elements of \(E\), and there are \(\#E(\#E-1)\) such pairs, so \(\#E(\#E-1)\ge q-1\). If \(\#E\le\sqrt q\), then \(\#E(\#E-1)\le\sqrt q(\sqrt q-1)\), and \(\sqrt q(\sqrt q-1)=q-\sqrt q<q-1\), a contradiction; so \(\#E>\sqrt q\). For a partition as in Lemma 1.1 this gives \(q=\sum_\nu\#E_\nu>s\sqrt q\), that is, \(s<\sqrt q\).

**4.4.** For \(s=1\), every point of a fibre \(\{g\}\times\mathbb Z/q\mathbb Z\) covered by \((a,t)+(f,e)\) comes from the contribution \(\bigl((a,t),f\bigr)\), which covers the whole fibre. So the fibre is covered exactly once exactly when exactly one pair \(\bigl((a,t),f\bigr)\) has \((a,t)\in B\), \(f\in F_1\) and \(a+f=g\). If \(\operatorname{pr}\) is injective on \(B\), this number is \(r_{\operatorname{pr}(B),F_1}(g)\). Conversely, if \((a,t)\ne(a,t')\) are in \(B\), they give two such pairs at \(g=a+f\) for any \(f\in F_1\).

**4.5.** It is used to make \(V\times\mathbb Z/q\mathbb Z\) cyclic. If \(q\mid\#V\), then \(\#V\cdot(v,t)=0\) for every \(v\in V\) and \(t\in\mathbb Z/q\mathbb Z\), while the group has \(q\,\#V>\#V\) elements; so no element generates it, and it is not cyclic. Then \(\mathbb Z^2\times V\times\mathbb Z/q\mathbb Z\) is not isomorphic to any group \(\mathbb Z^2\times\mathbb Z/Q\mathbb Z\), the kind of quotient of \(\mathbb Z^3\) that the last lesson needs: an isomorphism would map the elements of finite order, which form \(\{0\}\times V\times\mathbb Z/q\mathbb Z\), onto the elements of finite order \(\{0\}\times\mathbb Z/Q\mathbb Z\), which form a cyclic group.

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026
- [Greenfeld–Tao 2023] R. Greenfeld, T. Tao, *Undecidable translational tilings with only two tiles, or one nonabelian tile*, Discrete Comput. Geom. 70 (2023), 1652–1706. https://arxiv.org/abs/2108.07902
- [Greenfeld–Tao 2024] R. Greenfeld, T. Tao, *A counterexample to the periodic tiling conjecture*, Ann. of Math. 200 (2024), 301–363. https://arxiv.org/abs/2211.15847
