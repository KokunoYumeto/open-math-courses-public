# Passing to three-dimensional space

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Corollary 3.1 of [One tile with a cyclic finite coordinate](one-tile-with-a-cyclic-finite-coordinate.md) gives a tile \(F\) in \(\Gamma=\mathbb Z^2\times\mathbb Z/Q\mathbb Z\) with no fully periodic tiling set. Since \(\Gamma\) is a quotient of \(\mathbb Z^3\), this lesson builds from \(F\) a finite tile \(T\subset\mathbb Z^3\) with the same property, and shows that the union \(\Omega\) of the unit cubes with lower corners in \(T\) has no fully periodic tiling of \(\mathbb R^3\), even with arbitrary real translations [OpenAI-PT, Section 7]. This proves Theorem 4.1 of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md). The tile is assembled from two shapes with a large common part, a scattered set of cubes with prescribed residues modulo a large integer \(m\), and one marked cube, which the second shape moves along the kernel of \(\mathbb Z^3\to\Gamma\). In a periodic tiling, the common parts force the pieces onto a grid, and the marked cubes force invariance along the kernel, so the tiling descends to \(\Gamma\). Reductions from quotients of \(\mathbb Z^d\) to \(\mathbb Z^d\) were given by Meyerovitch, Sanadhya and Solomon [Meyerovitch–Sanadhya–Solomon 2025, Theorem 1.1], building on rigid tiles of Greenfeld and Tao [Greenfeld–Tao 2023, Lemma 9.3], and real translations are also controlled by a rigid tile in [Greenfeld–Tao 2024, Theorem 2.1 and Lemma 2.2]; the argument below proves both statements directly for one tile and its thickening.

- A residue transversal with many differences (Section 1).
- The tile (Section 2).
- Existence of a tiling (Section 3).
- Rigidity for real translations (Section 4).
- Kernel invariance and descent (Section 5).

We use multiplicities, Lemma 1.2, Lemma 3.2 and Proposition 3.3 of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md), and from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) (Fremlin, *Measure Theory*, Volume 1) countable additivity ([112C](https://www1.essex.ac.uk/maths/people/fremlin/chap11.pdf)), Borel sets and the measure of boxes ([115G](https://www1.essex.ac.uk/maths/people/fremlin/chap11.pdf)), and translation invariance ([134A](https://www1.essex.ac.uk/maths/people/fremlin/chap13.pdf)). Probabilities in Section 1 are proportions of a finite number of equally likely cases. In this lesson \(m\) denotes an integer, and Lebesgue measure on \(\mathbb R^3\) is written \(\operatorname{vol}\).

Let
\[
\begin{aligned}&\pi\colon\mathbb Z^3\to\Gamma,\\&\pi(a_1,a_2,a_3)=(a_1,a_2,a_3\bmod Q),\end{aligned}
\]
and \(w=(0,0,Q)\), so \(\ker\pi=\mathbb Zw\). By Lemma 1.2(1) of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md) we may translate \(F\) so that \(0\in F\). Choose a finite set \(U\subset\mathbb Z^3\) containing \(0\) on which \(\pi\) is a bijection onto \(F\), for instance by taking the third coordinate of each lift in \(\{0,\ldots,Q-1\}\). Then
\[
\begin{aligned}U\cap\ker\pi&=\{0\},\\ w&\notin U .\end{aligned}\tag{0.1}
\]

## 1. A residue transversal with many differences

For an integer \(m\ge2\) a *transversal* modulo \(m\) is a set \(\{t(v):v\in\{0,\ldots,m-1\}^3\}\subset\mathbb Z^3\) with \(t(v)\equiv v\pmod m\); it has exactly one point in every residue class of \(\mathbb Z^3\) modulo \(m\). The point \(t(0)\) will be the *marked point*.

**Lemma 1.1** (rigid representatives; [OpenAI-PT, Lemma 7.1]). There are an integer \(m\ge2\) and a transversal \(T_0=\{t(v)\}\) modulo \(m\) such that \(T_*=T_0\setminus\{t(0)\}\) satisfies
\[
T_*-T_*\supseteq X_m ,\tag{1.1}
\]
where \(X_m\) is the set of \(d\in\mathbb Z^3\) with \(\|d\|_\infty\le m\) and \(d\notin m\mathbb Z^3\).

*Proof.* Let \(m\ge2\). Choose independently and uniformly, for every residue \(v\in\{0,\ldots,m-1\}^3\), a vector \(h_v\in\{-2,-1,0,1,2\}^3\), and put \(t(v)=v+mh_v\). Fix \(d\in X_m\). Translation by \(d\bmod m\) is a permutation of \((\mathbb Z/m\mathbb Z)^3\) without fixed points, since \(d\notin m\mathbb Z^3\). A cycle of length \(L\ge2\) of this permutation contains \(\lfloor L/2\rfloor\ge L/3\) disjoint pairs of successive elements, so there are at least \(m^3/3\) disjoint pairs of residues \((u,v)\) with \(v-u\equiv d\pmod m\). Discarding the pair that contains the residue \(0\), if any, leaves at least \(k_m=\lfloor m^3/3\rfloor-1\) pairs with both residues nonzero.

For such a pair, with \(u,v\) taken in \(\{0,\ldots,m-1\}^3\), the equation \(t(v)-t(u)=d\) says
\[
h_v-h_u=\frac{d-(v-u)}m .
\]
The right side is an integer vector, and its coordinates have absolute value at most \((2m-1)/m<2\), so they lie in \(\{-1,0,1\}\). Two independent uniform elements of \(\{-2,\ldots,2\}\) have a prescribed difference \(\epsilon\in\{-1,0,1\}\) with probability \((5-|\epsilon|)/25\ge4/25\). So the pair realizes \(d\) with probability at least \(c=(4/25)^3\), and these events are independent for the disjoint pairs. The probability that no pair realizes \(d\) is at most \((1-c)^{k_m}\). There are at most \((2m+1)^3\) vectors \(d\), so (1.1) fails with probability at most
\[
(2m+1)^3(1-c)^{k_m},
\]
which tends to \(0\) as \(m\to\infty\). Choose \(m\ge2\) for which it is less than \(1\), and a successful choice of the \(h_v\). Every realizing pair avoids the residue \(0\), so it lies in \(T_*\). \(\square\)

## 2. The tile

Fix \(m\) and \(T_0\) as in Lemma 1.1, and move the marked point along the kernel:
\[
T_1=T_*\cup\{t(0)+mw\}.
\]
Both \(T_0\) and \(T_1\) are transversals modulo \(m\), with the same common part \(T_*\). The tile is
\[
\begin{aligned}T={}&T_1\\&\cup\bigcup_{u\in U\setminus\{0\}}\bigl(mu+T_0\bigr),\end{aligned}\tag{2.1}
\]
and its thickening is \(\Omega=T+[0,1]^3\).

**Lemma 2.1** (the tile). The union in (2.1) is disjoint, and \(\#T=\#U\cdot m^3\).

*Proof.* Two equal points have the same residue \(v\) modulo \(m\). For \(v\ne0\) they are \(mu+t(v)\) and \(mu'+t(v)\) with \(u,u'\in U\) (the points of \(T_*\subseteq T_1\) being the case \(u=0\)), so \(u=u'\). For \(v=0\) the points are \(mu+t(0)\), \(u\in U\setminus\{0\}\), and \(mw+t(0)\), which are distinct by (0.1). \(\square\)

Put \(\Omega_\iota=T_\iota+[0,1]^3\) for \(\iota=0,1\) and \(\Omega_*=T_*+[0,1]^3\). Closed unit cubes with distinct integer lower corners meet only on their boundaries, which are null by 115G; so by 112C and 134A
\[
\begin{aligned}\operatorname{vol}\Omega_0&=\operatorname{vol}\Omega_1=m^3,\\ \operatorname{vol}\Omega_*&=m^3-1 .\end{aligned}
\]
By (2.1), \(\Omega=\Omega_1\cup\bigcup_{u\ne0}(mu+\Omega_0)\), the pieces meeting only on boundaries. A translate \(c+T_\iota\) or \(c+\Omega_\iota\) with \(c\in\mathbb R^3\) is a *constituent* of *type* \(\iota\) with *center* \(c\).

## 3. Existence of a tiling

**Proposition 3.1** (existence; [OpenAI-PT, Proposition 7.2]). The set \(T\) tiles \(\mathbb Z^3\), and \(\Omega\) tiles \(\mathbb R^3\) almost everywhere.

*Proof.* Let \(A\oplus F=\Gamma\) and \(B=\pi^{-1}(A)\). Then \(B+w=B\). Also \(B\oplus U=\mathbb Z^3\): for \(g\in\mathbb Z^3\), \(\pi(g)\) has one expression \(\alpha+f\) with \(\alpha\in A\) and \(f\in F\); then \(f=\pi(u)\) for exactly one \(u\in U\), and \(g-u\in B\). Conversely, if \(g=b+u\) with \(b\in B\), \(u\in U\), then \(\pi(g)=\pi(b)+\pi(u)\) is such an expression, so \(\pi(u)\), hence \(u\), and then \(b\) are determined.

Consider the copies \(mb+T\), \(b\in B\). Their constituents have the centers \(m(b+u)\), \(b\in B\), \(u\in U\), of type \(1\) for \(u=0\) and type \(0\) otherwise. Since \(B\oplus U=\mathbb Z^3\), every point of \(m\mathbb Z^3\) is exactly one center, and the centers of type \(1\) are the points of \(mB\). Let \(x\in\mathbb Z^3\) have residue \(v\) modulo \(m\). If \(v\ne0\), the constituents covering \(x\) use points of \(T_*\), common to both types; since every residue class has exactly one point of \(T_0\), \(x\) is covered exactly once, from the center \(x-t(v)\). If \(v=0\), write \(x=t(0)+ma\) with \(a\in\mathbb Z^3\). It is covered by the center \(ma\) if that center has type \(0\), that is, if \(a\notin B\), and by the center \(m(a-w)\) if that center has type \(1\), that is, if \(a-w\in B\). Since \(B+w=B\), exactly one of these holds. So \(mB\oplus T=\mathbb Z^3\), and Proposition 3.3 of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md) gives \(mB\oplus\Omega=\mathbb R^3\) almost everywhere. \(\square\)

## 4. Rigidity for real translations

**Lemma 4.1** (rounding in the closed box; [OpenAI-PT, Lemma 7.3]). Let \(m\ge2\), and let \(\delta\in\mathbb R^3\) with \(\|\delta\|_\infty\le m\) and \(\delta\notin m\mathbb Z^3\). There is \(d\in\mathbb Z^3\setminus m\mathbb Z^3\) with
\[
\|d\|_\infty\le m,\qquad\|\delta-d\|_\infty<1 .
\]

*Proof.* If \(\delta\) is integral, take \(d=\delta\). Otherwise keep the integer coordinates of \(\delta\) and round each other coordinate down or up. A noninteger coordinate lies strictly between \(-m\) and \(m\), so both roundings lie in \([-m,m]\) and differ from it by less than \(1\). Two consecutive integers are not both multiples of \(m\ge2\), so in one noninteger coordinate we can choose a rounding that is not a multiple of \(m\); then \(d\notin m\mathbb Z^3\). \(\square\)

Two closed unit cubes \(y+[0,1]^3\) and \(y'+[0,1]^3\) with \(\|y'-y\|_\infty<1\) intersect in a box with sides \(1-|y'_i-y_i|>0\), which has positive volume by 115G.

**Lemma 4.2** (a periodic assembly has grid centers; [OpenAI-PT, Lemma 7.4]). Let \(C\subset\mathbb R^3\) and \(\iota\colon C\to\{0,1\}\) be such that the constituents \(c+\Omega_{\iota(c)}\), \(c\in C\), tile \(\mathbb R^3\) almost everywhere: the points that lie in no constituent or in more than one form a null set. Suppose that \(C+\Lambda=C\) and \(\iota(c+\lambda)=\iota(c)\) for a lattice \(\Lambda\) of full rank. Then \(C=c_0+m\mathbb Z^3\) for some \(c_0\in\mathbb R^3\).

*Proof.* *Nearby centers.* Let \(c\ne c'\) in \(C\) with \(\|c'-c\|_\infty\le m\). We claim \(c'-c\in m\mathbb Z^3\). Otherwise Lemma 4.1 gives \(d\in\mathbb Z^3\setminus m\mathbb Z^3\) with \(\|d\|_\infty\le m\) and \(\|(c'-c)-d\|_\infty<1\), and by (1.1) \(d=t-t'\) with \(t,t'\in T_*\). The unit cubes \(c+t+[0,1]^3\) and \(c'+t'+[0,1]^3\) belong to the constituents at \(c\) and \(c'\), whatever their types, and their lower corners differ by \((c'-c)-d\). So they intersect in a set of positive volume, which is covered twice, a contradiction.

*Separation.* A nonzero vector of \(m\mathbb Z^3\) has sup norm at least \(m\), so distinct centers satisfy \(\|c'-c\|_\infty\ge m\). The open cubes \(c+(-m/2,m/2)^3\) are therefore pairwise disjoint, and a box of side \(R\) contains at most \(\bigl((R+m)/m\bigr)^3\) centers, by comparing volumes. So every bounded set contains finitely many centers, and \(C\) is countable.

*The auxiliary cubes cover almost everything.* Let \(\Lambda=\mathbb Zb_1+\mathbb Zb_2+\mathbb Zb_3\) with a basis \(b_1,b_2,b_3\) of \(\mathbb R^3\), and \(P=\{\sum_is_ib_i:0\le s_i<1\}\). Every \(x\in\mathbb R^3\) is \(\sum_is_ib_i\) for unique real \(s_i\), so \(x\in P+\lambda\) for exactly one \(\lambda\in\Lambda\), namely \(\lambda=\sum_i\lfloor s_i\rfloor b_i\): the translates \(P+\lambda\) partition \(\mathbb R^3\). The set \(P\) is bounded and is the image of a half-open box under a linear homeomorphism, so it is a Borel set of finite measure. Every orbit \(c+\Lambda\subseteq C\) meets \(P\) in exactly one point, and \(C\cap P\) is finite, so there are finitely many orbits, with representatives \(c_1,\ldots,c_r\in P\).

Let \(N\) be the set of points lying in no constituent or in more than one; it is a Borel set, since the number of constituents containing a point is a countable sum of indicator functions of closed sets, and it is null. The set \(P\setminus N\) is the disjoint union of its intersections with the constituents, so, writing \(\Omega^{(j)}=\Omega_{\iota(c_j)}\) and summing over \(1\le j\le r\) and \(\lambda\in\Lambda\), 112C and 134A give
\[
\begin{aligned}\operatorname{vol}P&=\sum_{j,\lambda}\operatorname{vol}\bigl(P\cap(c_j+\lambda+\Omega^{(j)})\bigr)\\&=\sum_{j,\lambda}\operatorname{vol}\bigl((P-\lambda)\cap(c_j+\Omega^{(j)})\bigr)\\&=\sum_{j=1}^r\operatorname{vol}\Omega^{(j)}=rm^3,\end{aligned}
\]
the third equality because the sets \(P-\lambda\) partition \(\mathbb R^3\). Now let \(Q_c=c+[-m/2,m/2]^3\) for \(c\in C\), of volume \(m^3\). These cubes have disjoint interiors, so they meet only on their null boundaries, and the same computation gives \(\operatorname{vol}(P\cap Y)=rm^3=\operatorname{vol}P\) for \(Y=\bigcup_{c\in C}Q_c\). So \(P\setminus Y\) is null. Since \(Y+\Lambda=Y\), the set \(\mathbb R^3\setminus Y\) is the disjoint union of the translates \((P\setminus Y)+\lambda\), and it is null.

*The auxiliary cubes cover everything.* A point \(x\notin Y\) has only finitely many cubes \(Q_c\) within sup distance \(1\), each closed and not containing \(x\), so some open ball around \(x\) misses all of them, hence misses \(Y\). An open ball has positive volume, so \(Y=\mathbb R^3\).

*All centers lie in one coset of \(m\mathbb Z^3\).* Let \(c,c'\in C\) and \(\gamma(s)=c+s(c'-c)\) for \(s\in[0,1]\). Let \(S_1\) be the set of \(s\) such that \(\gamma(s)\in Q_d\) for some \(d\in C\cap(c+m\mathbb Z^3)\), and \(S_2\) the set of \(s\) such that \(\gamma(s)\in Q_d\) for some \(d\in C\setminus(c+m\mathbb Z^3)\). Only finitely many cubes meet the segment, so \(S_1\) and \(S_2\) are closed, and \(S_1\cup S_2=[0,1]\) because \(Y=\mathbb R^3\). They are disjoint: a point in \(Q_d\cap Q_{d'}\) gives \(\|d-d'\|_\infty\le m\), so \(d-d'\in m\mathbb Z^3\) by the first step, and \(d,d'\) lie in the same coset. Now \(0\in S_1\). If \(S_2\) were nonempty, its least element \(s_0\) would be positive, all \(s<s_0\) would lie in \(S_1\), and since \(S_1\) is closed, \(s_0\in S_1\cap S_2\), which is impossible. So \(1\in S_1\): \(c'\in Q_d\) for some \(d\in c+m\mathbb Z^3\), and either \(c'=d\) or \(c'-d\in m\mathbb Z^3\) by the first step. Hence \(C\subseteq c+m\mathbb Z^3\).

*No point of the coset is missing.* If \(g\in(c+m\mathbb Z^3)\setminus C\), the interior of \(g+[-m/2,m/2]^3\) is disjoint from \(Q_d\) for every \(d\in c+m\mathbb Z^3\) with \(d\ne g\), since some coordinate of \(d-g\) has absolute value at least \(m\). So that interior misses \(Y=\mathbb R^3\), which is absurd. Hence \(C=c+m\mathbb Z^3\). \(\square\)

## 5. Kernel invariance and descent

**Proposition 5.1** (no fully periodic tiling; [OpenAI-PT, Proposition 7.5]). No tiling set \(\mathcal A\) with \(\mathcal A\oplus\Omega=\mathbb R^3\) almost everywhere is invariant under a lattice of full rank.

*Proof.* Suppose \(\mathcal A\oplus\Omega=\mathbb R^3\) almost everywhere and \(\mathcal A+\Lambda=\mathcal A\) for a lattice \(\Lambda\) of full rank.

*Countability.* Fix \(t_0\in T\). For distinct \(a,a'\in\mathcal A\) with \(\|a-a'\|_\infty<1\), the cubes \(a+t_0+[0,1]^3\subseteq a+\Omega\) and \(a'+t_0+[0,1]^3\subseteq a'+\Omega\) would overlap in positive volume, covered twice. So distinct points of \(\mathcal A\) have sup distance at least \(1\), every box \(z+[0,1)^3\), \(z\in\mathbb Z^3\), contains at most one of them, and \(\mathcal A\) is countable.

*Constituents.* By (2.1) each copy \(a+\Omega\) is the union of the constituent of type \(1\) at \(a\) and the constituents of type \(0\) at \(a+mu\), \(u\in U\setminus\{0\}\), which meet only on the boundaries of countably many unit cubes. So all these constituents together tile \(\mathbb R^3\) almost everywhere. Two of them cannot have the same center, since both would contain the translate of \(\Omega_*\) by that center, which has positive volume. So the map
\[
\begin{aligned}&\mathcal A\times U\to C,\\&(a,u)\mapsto a+mu,\end{aligned}\tag{5.1}
\]
onto the set \(C\) of centers is a bijection, the centers of type \(1\) are exactly the points of \(\mathcal A\), and \(C+\Lambda=C\) with types preserved.

*Grid.* By Lemma 4.2, \(C=c_0+m\mathbb Z^3\). Replacing \(\mathcal A\) by \(\mathcal A-c_0\), which is again a tiling set by 134A, with the same lattice of periods, we may assume \(C=m\mathbb Z^3\). Then \(\mathcal A\subseteq m\mathbb Z^3\), so \(\mathcal A=mB'\) for a set \(B'\subseteq\mathbb Z^3\), and dividing (5.1) by \(m\) gives
\[
B'\oplus U=\mathbb Z^3 .\tag{5.2}
\]
For \(a\in\mathbb Z^3\) let \(b(a)=1\) if \(a\in B'\) and \(b(a)=0\) otherwise; it is the type of the center \(ma\).

*Kernel invariance.* Let \(a\in\mathbb Z^3\) and let \(o\) be the open unit cube with lower corner \(t(0)+ma\). All constituent cubes are closed unit cubes with integer lower corners, and such a cube meets \(o\) only if its lower corner is \(t(0)+ma\). The constituent at the center \(mc\) of type \(\iota\) has this cube exactly when \(t(0)+ma-mc\in T_\iota\). This point has residue \(0\) modulo \(m\), and the points of \(T_\iota\) with residue \(0\) are \(t(0)\) for \(\iota=0\) and \(t(0)+mw\) for \(\iota=1\). So exactly two constituents can cover \(o\): the one at \(ma\), if it has type \(0\), and the one at \(m(a-w)\), if it has type \(1\). The number of constituents covering the points of \(o\) is
\[
\bigl(1-b(a)\bigr)+b(a-w),
\]
and since \(o\) has positive volume, it equals \(1\). So \(b(a)=b(a-w)\) for every \(a\), that is,
\[
B'+w=B'.\tag{5.3}
\]

*Full periodicity of \(B'\).* The set \(\mathcal A\) is nonempty, since the translates of \(\Omega\) cover almost all of \(\mathbb R^3\). For \(a_0\in\mathcal A\) and \(\lambda\in\Lambda\), both \(a_0\) and \(a_0+\lambda\) lie in \(m\mathbb Z^3\), so \(\lambda\in m\mathbb Z^3\). Hence \(L=m^{-1}\Lambda\) is a subgroup of \(\mathbb Z^3\) containing the three linearly independent vectors \(m^{-1}b_i\), so it has finite index in \(\mathbb Z^3\) by Lemma 3.2(2) of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md), and \(B'+L=m^{-1}(\mathcal A+\Lambda)=B'\).

*Descent.* Let \(\gamma\in\Gamma\) with a lift \(g\in\mathbb Z^3\), and \(u\in U\). If \(g-u\in B'\), then \(\gamma=\pi(g-u)+\pi(u)\) with \(\pi(g-u)\in\pi(B')\). Conversely, if \(\gamma=\pi(b_0)+\pi(u)\) with \(b_0\in B'\), then \(g-u-b_0\in\ker\pi=\mathbb Zw\), and (5.3) gives \(g-u\in B'\). By (5.2) exactly one \(u\in U\) has \(g-u\in B'\), and \(\pi\) is injective on \(U\), so \(\gamma\) has exactly one expression \(\alpha+f\) with \(\alpha\in\pi(B')\) and \(f\in\pi(U)=F\):
\[
\pi(B')\oplus F=\Gamma .
\]
This tiling set is fully periodic: \(\pi(L)\) preserves it, and \(\pi(L)\) has finite index in \(\Gamma\) because \(\pi\) induces a surjection \(\mathbb Z^3/L\to\Gamma/\pi(L)\). This contradicts Corollary 3.1 of [One tile with a cyclic finite coordinate](one-tile-with-a-cyclic-finite-coordinate.md). \(\square\)

*Proof of Theorem 4.1 of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md).* The finite nonempty set \(T\) of (2.1) tiles \(\mathbb Z^3\), and \(\Omega\) tiles \(\mathbb R^3\) almost everywhere, by Proposition 3.1. No tiling set of \(\Omega\) is invariant under a lattice of full rank, by Proposition 5.1; this is part 2. If a tiling set \(A\) of \(T\) were invariant under a subgroup of finite index of \(\mathbb Z^3\), Proposition 3.3 of [Tilings of abelian groups and periodicity](tilings-of-abelian-groups-and-periodicity.md) would make it a fully periodic tiling set of \(\Omega\), which Proposition 5.1 excludes; this is part 1. \(\square\)

**Remark 5.2** (finite selection; [OpenAI-PT, Remark 7.6]). Every choice in the construction is a terminating finite search: the primes by trial division, the partition of Lemma 1.1 of [One tile with a cyclic finite coordinate](one-tile-with-a-cyclic-finite-coordinate.md) and the transversal of Lemma 1.1 above by exhaustive search, since the probability bounds guarantee that a suitable choice exists; the tiling tests are statements about maps between finite sets. So the tile \(T\) is determined by a finite computation, although no practical bound on its size is claimed. Its size is \(\#T=\#U\cdot m^3=qMm^3\), with \(q\) and \(M\) as in Corollary 3.1 of [One tile with a cyclic finite coordinate](one-tile-with-a-cyclic-finite-coordinate.md). The infinite tiling of Proposition 3.1 is described through the last-nonzero-digit function \(f\) of [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md).

## 6. Exercises

**6.1.** Find the least \(m\ge2\) for which \((2m+1)^3\bigl(1-(4/25)^3\bigr)^{\lfloor m^3/3\rfloor-1}<1\).

**6.2.** Let \(y,y'\in\mathbb R^3\). Show that \((y+[0,1]^3)\cap(y'+[0,1]^3)\) has volume \(\prod_i\max(0,1-|y_i-y'_i|)\).

**6.3.** In the proof of Proposition 3.1, show that the copies \(mb+T\), \(b\in B\), would not tile \(\mathbb Z^3\) if the marked point were moved to \(t(0)+mv\) for some \(v\in\mathbb Z^3\) with \(v\notin\ker\pi\) and \(B+v\ne B\).

**6.4.** Show that the conclusion of Lemma 4.2 can fail without the difference property (1.1): find a periodic almost-everywhere tiling of \(\mathbb R^3\) by translates of the cube \([0,m]^3\) whose set of lower corners is not contained in any translate of \(m\mathbb Z^3\).

**6.5.** Show that a set \(C\subset\mathbb R^3\) whose points have pairwise sup distance at least \(m\) meets a box of side \(R\) in at most \(\bigl((R+m)/m\bigr)^3\) points.

## 7. Solutions

**6.1.** With \(c=(4/25)^3=64/15625\) and \(k_m=\lfloor m^3/3\rfloor-1\), the bound is about \(5.01\) at \(m=19\) (\(k_m=2285\)), \(1.22\) at \(m=20\) (\(k_m=2665\)) and \(0.25\) at \(m=21\) (\(k_m=3086\)), and it is larger than \(1\) for all \(m\le20\). So the least \(m\) is \(21\). Lemma 1.1 only needs some \(m\); a transversal with (1.1) may exist for smaller \(m\).

**6.2.** The intersection is the box \(\prod_i[\max(y_i,y'_i),\min(y_i,y'_i)+1]\) when \(|y_i-y'_i|\le1\) for all \(i\), and empty otherwise; its sides are \(1-|y_i-y'_i|\), and 115G gives the volume.

**6.3.** The points of residue \(0\) modulo \(m\) are \(x=t(0)+ma\). The center \(ma\) covers \(x\) if it has type \(0\), that is, if \(a\notin B\), and the center \(m(a-v)\) covers it if it has type \(1\), that is, if \(a-v\in B\); no other center can. Since \(B+v\ne B\), there is an \(a\) for which exactly one of the statements \(a\in B\) and \(a-v\in B\) is true. If \(a\notin B\) and \(a-v\in B\), the point \(x\) is covered twice; if \(a\in B\) and \(a-v\notin B\), it is not covered.

**6.4.** The cube \([0,m]^3\) is \(\Omega_0\) for the transversal \(\{0,\ldots,m-1\}^3\), which does not satisfy (1.1): the vector \((m,1,0)\) is not a difference of two of its points. Take the lower corners \((mk+\tfrac m2\epsilon_r,\,mr,\,ml)\), \(k,r,l\in\mathbb Z\), where \(\epsilon_r=1\) for odd \(r\) and \(\epsilon_r=0\) for even \(r\). For fixed \(r\) and \(l\), these cubes tile the bar \(\mathbb R\times[mr,m(r+1)]\times[ml,m(l+1)]\), overlapping only on faces, so they tile \(\mathbb R^3\) almost everywhere. The set of corners is invariant under the lattice generated by \((m,0,0)\), \((0,2m,0)\) and \((0,0,m)\), and the corners \((0,0,0)\) and \((m/2,m,0)\) differ by a vector outside \(m\mathbb Z^3\).

**6.5.** The open cubes \(c+(-m/2,m/2)^3\), \(c\in C\), are pairwise disjoint. Those with \(c\) in a box of side \(R\) lie in a box of side \(R+m\), so their number times \(m^3\) is at most \((R+m)^3\).

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026
- [Meyerovitch–Sanadhya–Solomon 2025] T. Meyerovitch, S. Sanadhya, Y. Solomon, *A note on reduction of tiling problems*, Israel J. Math. 267 (2025), 421–435. https://arxiv.org/abs/2211.07140
- [Greenfeld–Tao 2023] R. Greenfeld, T. Tao, *Undecidable translational tilings with only two tiles, or one nonabelian tile*, Discrete Comput. Geom. 70 (2023), 1652–1706. https://arxiv.org/abs/2108.07902
- [Greenfeld–Tao 2024] R. Greenfeld, T. Tao, *A counterexample to the periodic tiling conjecture*, Ann. of Math. 200 (2024), 301–363. https://arxiv.org/abs/2211.15847
