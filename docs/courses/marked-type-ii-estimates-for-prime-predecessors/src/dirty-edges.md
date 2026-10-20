# Dirty edges

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An edge is **dirty** if it stores a label or promotes a particle. Its signed kernel need not cancel, and the absolute bounds of [*Truncation, adjoints and absolute bounds*](truncation-adjoints-and-absolute-bounds.md) give only a power of \(L\). This lesson shows that every dirty piece is nevertheless small, by a weighted Schur test in which one of the two sides is small and the other is bounded *without* the factor \(B^K\) that counts choices of particles. The smallness has two sources. For the raw part \(\mathbf 1_{t=b-a}\), a promoted prime determines the target modulo itself, and test (G2) of the good positions then allows only one choice of the labels omitted at the source; the source symmetrization makes that choice cost \(M^{-K}\). For the comparison part, a promoted prime imposes one linear congruence on the lattice box of the clean analysis, which is satisfied by a proportion \(O(1/p+Y^{-0.1})\) of its points.

**Prerequisites.** [*Truncation, adjoints and absolute bounds*](truncation-adjoints-and-absolute-bounds.md); [*Clean edges and the lattice box*](clean-edges-and-the-lattice-box.md), Lemmas 2.1 and 3.1; [*Physical states and good positions*](physical-states-and-good-positions.md), Definition 3.1 and the cross-edge ban; [*Lifespans and the memory space*](lifespans-and-the-memory-space.md), Section 3.

We split \(\mathcal E_j\) into pieces \((S,I)\), where \(S\) is the set of groups that store and \(I\) the set of groups that promote (Lemma 2.4 of Lesson 13), and each piece into its **raw part**, with multiplier \((d_0/D)\eta\eta\psi\,\mathbf 1_{t=b-a}\), and its **comparison part**, with multiplier \(-(d_0/D)\eta\eta\psi\int_{\mathfrak M}e(\theta(t-b+a))\,d\theta\). The dirty pieces are those with \((S,I)\ne(\varnothing,\varnothing)\); there are \(4^K-1\) of them. All row and column sums are weighted by \(h=8^{k_{\rm tot}}\) as in Lesson 13, and \(C_K\) denotes constants depending only on \(K\).

## 1. Raw pieces without promotion

**Lemma 1.1.** For a piece with \(I=\varnothing\), the weighted raw row sum is at most \(C_K\).

**Proof.** Fix the source state. The source symmetrization averages over the reorderings, each of which fixes \(D\) and \(b\). The fresh labels in all groups have total mass at most \(2^K\); for each of them, \(j_1=\det(z,z')=D(b-a)\) is fixed, and by (4.1) of Lesson 13 there are at most \(17\) targets. Storing in the groups of \(S\) multiplies the weight by \(8^{|S|}\), there are no choices of indices, the factors \(\rho\) are at most \(1\), and the multiplier is at most \(2\). \(\square\)

The point is that no factor \(B\) appears: storing creates particles but never chooses among them.

## 2. Raw pieces with promotion

**Lemma 2.1 (the anchor congruence).** Let \(I\ne\varnothing\) and \(i_*=\max I\). Fix the source state, the index of the particle \((p_*,\lambda_*)\) promoted in group \(i_*\), and the fresh labels of the groups outside \(I\), with product \(T_f\). Let \(Z\) be the product of the primes promoted in the groups of \(I\setminus\{i_*\}\), and let \(P_{\rm full}\) be the product of all labels of the source state. In the raw part, every target satisfies

\[
\begin{gathered}
\det(z,z')=P_{\rm full}-Dp_*ZT_f,\quad(2.1)
\end{gathered}
\]

and there is a residue \(h_*\) modulo \(p_*\), depending only on the source state and on \((p_*,\lambda_*)\), such that

\[
\begin{gathered}
\Bigl\|DZT_f\,r_{gz}-\frac{P_{\rm full}r_z^*+h_*}{p_*}\Bigr\|\\
\le\frac{16}{p_*}.\quad(2.2)
\end{gathered}
\]

**Proof.** The target's last slots have product \(a=p_*ZT_f\), and \(Db=P_{\rm full}\); this is (2.1). By the cross-edge ban, \(p_*\) is not a label of the source, so \(p_*\nmid P_{\rm full}\) and \(j_1=\det(z,z')\equiv P_{\rm full}\not\equiv0\pmod{p_*}\). Write \(z'=j_1w_z+hz\) as in (4.1) of Lesson 13. Modulo \(p_*\) the vector \(z'\) has the nonzero coordinate \(j_1\) along \(w_z\), so its line is determined by \(h\bmod p_*\), and different residues of \(h\) give different lines. The promotion requires \([z']_{p_*}=\lambda_*\), which therefore holds for at most one residue \(h\equiv h_*\pmod{p_*}\); since \(j_1\equiv P_{\rm full}\), this residue depends only on \(P_{\rm full}\bmod p_*\), \(\lambda_*\) and the source position. Write \(h=h_*+p_*k\). The box condition \(|h+j_1r_z^*|\le16\) and (2.1) give

\[
\begin{gathered}
\Bigl|k+\frac{h_*+P_{\rm full}r_z^*}{p_*}-DZT_fr_z^*\Bigr|\le\frac{16}{p_*},
\end{gathered}
\]

and \(DZT_fr^*_z\equiv DZT_fr_{gz}\pmod1\) because \(r_z^*\) is a lift of \(r_{gz}\). \(\square\)

**Lemma 2.2 (one omission tuple).** In the situation of Lemma 2.1, suppose the source state is good and \(T_f\) is not in the exceptional set of test (G2) for the set \(I\). Then at most one pair \((D,Z)\), with \(D\) an omission product of the source in \([d_0,2d_0)\) and \(Z\) a product of one prime from each group of \(I\setminus\{i_*\}\), satisfies (2.2). In particular the labels omitted at the source, and the primes promoted in the groups of \(I\setminus\{i_*\}\), are determined.

**Proof.** By (2.2) the point \(DZT_fr_{gz}\) lies in an arc of length \(32/p_*\le32e^{-L^{a_{i_*}}}\), since \(p_*\in\mathcal P_{i_*}\). Test (G2) separates the points belonging to different integers \(DZ\) by \(100e^{-L^{a_{i_*}}}\), so the integer \(DZ\) is determined. The primes of \(D\) are labels of the source, and those of \(Z\) are not, by the ban; so \(DZ\) determines \(D\) and \(Z\). Since the lists of the source have distinct entries, \(D\) determines which label was omitted in each group, and since the bands are disjoint, \(Z\) determines its prime in each group. \(\square\)

**Lemma 2.3.** For a piece with \(I\ne\varnothing\), the weighted raw row sum is at most

\[
\begin{aligned}
\varepsilon_K&=C_K\bigl(BM^{-K}\\
&\quad+B^Ke^{-L^{0.1}/4}\bigr).\quad(2.3)
\end{aligned}
\]

**Proof.** Fix the source state; it is good, since the edge imposes goodness. Sum over the at most \(B\) indices of a particle \((p_*,\lambda_*)\) of group \(i_*\), and integrate over the fresh labels \(T_f\) of the groups outside \(I\). The law of \(T_f\) under the measures \(\nu_i\) is at most \(1.01^K\) times its law under the \(\mu_i\) (Lemma 2.1 of Lesson 12), so the exceptional set of (G2) has \(\nu\)-mass at most \(1.01^Ke^{-L^{a_{i_*}}/4}\le2^Ke^{-L^{0.1}/4}\).

*Non-exceptional \(T_f\).* By Lemma 2.2 at most one omission tuple is possible. The source symmetrization is an average over reorderings, and the probability that a uniformly random reordering puts a prescribed label of each group in the last slot is \(M^{-K}\). The promoted primes \(Z\) are determined, so \(j_1\) is determined by (2.1), and there are at most \(17\) targets. At a target, in each group \(i\in I\setminus\{i_*\}\) we must choose one of the old particles hitting \(z'\); if \(n_i\) of them hit, the choice costs \(n_i\), and the \(n_i-1\) particles left in memory pay \(\rho^{n_i-1}\) in step 3 of the edge. Since \(\sup_{n\ge1}n\rho^{n-1}\le2\) for \(\rho=\frac34\), each such group costs at most \(2\), whatever the repetitions among prime values and anchors. Stores, the coefficients \(1/V_i\le2\), the weight ratio \(8^{|S|-|I|}\le8^K\), the fresh masses and the multiplier contribute \(C_K\). This gives \(C_KBM^{-K}\).

*Exceptional \(T_f\).* Use the crude count: at most \(B^K\) indices in all promoted groups, at most \(17\) targets for each choice of labels, and the remaining factors bounded in the same way. This gives \(C_KB^Ke^{-L^{0.1}/4}\). \(\square\)

**Proposition 2.4 (raw dirty pieces).** If \(K\) is large enough that \(\varepsilon_K\le1\), the raw parts of all dirty pieces of \(\mathcal E_j\) together have norm at most \(C_K\sqrt{\varepsilon_K}\) on \(\mathscr H_B\). In particular, since \(B\le2L^2\) and \(M\ge L^{0.01}\),

\[
\begin{gathered}
\|\text{raw dirty part of }\mathcal E_j\|\\
\le C_KL^{1-0.005K}+O(e^{-L^{0.1}/9}).\quad(2.4)
\end{gathered}
\]

**Proof.** By Lemma 2.4 of Lesson 13, the column sums of a piece \((S,I)\) are the row sums of the piece \((I,S)\) of the reversed edge. The reversed edge has the same structure: its raw equation reads \(\det(z',z)=Da-Db\), which is again the full product of its source minus \(D\) times the unshared product of its target, it obeys the ban, and it requires both of its endpoints to be good. So Lemmas 1.1 and 2.3 apply to it. The resulting table of weighted row and column sums is

| \(S\) | \(I\) | row | column |
|---|---|---|---|
| \(\varnothing\) | nonempty | \(\varepsilon_K\) | \(C_K\) |
| nonempty | \(\varnothing\) | \(C_K\) | \(\varepsilon_K\) |
| nonempty | nonempty | \(\varepsilon_K\) | \(\varepsilon_K\) |

Lemma 2.1 of Lesson 13 bounds each piece by \(\sqrt{C_K\varepsilon_K}\), and there are fewer than \(4^K\) pieces. Finally \(\sqrt{BM^{-K}}\le\sqrt2\,L^{1-0.005K}\). \(\square\)

The bounded entry opposite each small entry is what makes this work: the crude bound \(L^{C_e}\) of Lesson 13, which contains \(B^K\), never meets the factor \(M^{-K}\). Raising \(K\) by \(200\) gains one power of \(L\), while all other dependence on \(K\) is a constant factor.

## 3. Comparison pieces

**Lemma 3.1 (a line in a box).** Let \(p\) be a prime, \(\ell(c_1,c_2)=\alpha c_1+\beta c_2\) a linear form with \((\alpha,\beta)\not\equiv(0,0)\pmod p\), and \(A',B'\ge1\). The number of integer points with \(|c_1|\le A'\), \(|c_2|\le B'\) and \(\ell(c)\equiv0\pmod p\) is at most \(9(A'B'/p+\max(A',B'))\).

**Proof.** If \(\beta\not\equiv0\), then for each \(c_1\) the condition fixes \(c_2\) modulo \(p\), leaving at most \(2B'/p+1\) values, and there are at most \(2A'+1\) values of \(c_1\). If \(\beta\equiv0\), then \(\alpha\not\equiv0\) and the roles are exchanged. \(\square\)

**Lemma 3.2.** For a piece with \(I\ne\varnothing\), the weighted row sum of the comparison part is at most

\[
\begin{aligned}
\zeta_K&=C_KL^{3A_0}B^K\\
&\quad\times\bigl(e^{-L^{0.1}}+Y^{-0.1}\bigr).\quad(3.1)
\end{aligned}
\]

**Proof.** Fix the source state (good), a reordering, hence \(D\), and the indices of all promoted particles (at most \(B^K\) choices). Let \((p,\lambda)\) be the particle promoted in some group of \(I\). The multiplier is at most \(4L^{3A_0}/Y\) by (5.2) of Lesson 7, and it vanishes unless \(D\mid\det(z,z')\) and \(|\det(z,z')|\le10H\). So the target lies in a block of the source in the sense of Lesson 14: in the lattice \(\Lambda\) of Lemma 2.1 there, within at most \(5123\) cells, and by Lemma 3.1 there it corresponds to an integer point of a box with sides \(A',B'\), \(A'B'\le C_0Y\) and \(A',B'\ge Y^{0.1}\). The coordinate map from such points to \(z'\) is an integer linear map of determinant \(\pm D\), and \(p\nmid D\) by the ban, so the map is invertible modulo \(p\), and the condition \([z']_p=\lambda\) becomes \(\ell(c)\equiv0\pmod p\) for a linear form \(\ell\not\equiv0\). By Lemma 3.1 there are at most \(9C_0Y(1/p+Y^{-0.1})\) such targets in each cell shift. With \(p\ge e^{L^{0.1}}\), the fresh masses, stores, coefficients and weight ratios contributing \(C_K\), and the multiplier \(4L^{3A_0}/Y\), this gives (3.1). \(\square\)

**Proposition 3.3 (comparison dirty pieces).** The comparison parts of all dirty pieces of \(\mathcal E_j\) together have norm \(O_A(L^{-A})\) on \(\mathscr H_B\), for every fixed \(A\).

**Proof.** For a piece with \(I\ne\varnothing\), the row sum is at most \(\zeta_K\) by Lemma 3.2 and the column sum at most \(L^{C_e}\) by Lemma 4.1 of Lesson 13. For \(I=\varnothing\) and \(S\ne\varnothing\), the column sum is the row sum of the reversed piece \((\varnothing,S)\), which is at most \(\zeta_K\), and the row sum at most \(L^{C_e}\). Lemma 2.1 of Lesson 13 gives the norm bound \(\sqrt{\zeta_KL^{C_e}}\) for each piece, and \(\zeta_K\) is smaller than every power of \(L^{-1}\), because \(e^{-L^{0.1}}\) and \(Y^{-0.1}\le e^{-0.1L^{0.1}+0.2}\) are. \(\square\)

## 4. The signed bound for one step

**Theorem 4.1 (contraction of every edge).** Fix \(G>0\). Choose \(A_0\ge G+3\), and then \(K\) with \(0.005K>G+2\). For large \(x\) and every \(j\),

\[
\begin{gathered}
\|\mathcal E_j\|_{\mathscr H_B\to\mathscr H_B}\le L^{-G}.\quad(4.1)
\end{gathered}
\]

**Proof.** Write \(\mathcal E_j\) as its clean piece plus the raw and comparison parts of the dirty pieces. By Theorem 5.1 of Lesson 14 with \(G+1\) in place of \(G\), the clean piece has norm at most \(L^{-G-1}\). By Proposition 2.4 the raw dirty part has norm at most \(C_KL^{1-0.005K}+O(e^{-L^{0.1}/9})\le L^{-G-1}\) for large \(x\), and by Proposition 3.3 the comparison dirty part has norm at most \(L^{-G-1}\). Since \(3L^{-G-1}\le L^{-G}\), (4.1) follows. \(\square\)

The exponent condition on \(A_0\) depends only on \(G\), and the condition on \(K\) only on \(G\); the crude exponent \(C_e(K,A_0)\) of Lesson 13 entered only through the comparison pieces, where it is beaten by \(\zeta_K\). This is why \(K\) can be chosen after \(A_0\) and independently of the band exponents.

## 5. Exercises

**15.1.** Show that \(\sup_{n\ge1}n\rho^{n-1}=\frac{27}{16}\) for \(\rho=\frac34\).

**15.2.** In Lemma 2.1, show that if \(\lambda_*=[z]_{p_*}\), no target satisfies the promotion condition.

**15.3.** Show that \(BM^{-K}\le2L^{2-0.01K}\) and determine the least \(K\) for which (2.4) gives \(L^{-5}\) up to constants.

**15.4.** Show that the map from the coordinates \((c_1,c_2)\) of Lemma 3.1 of Lesson 14 to \(z'\) is an integer linear map of determinant \(\pm D\).

**15.5.** Explain why the argument of Lemma 2.3 needs the *largest* index \(i_*\) of \(I\) in test (G2), rather than an arbitrary element of \(I\).

## 6. Solutions

**15.1.** \(n\rho^{n-1}\) increases while \((n+1)\rho^n\ge n\rho^{n-1}\), that is while \(\rho\ge n/(n+1)\), that is for \(n\le3\). The values at \(n=3\) and \(n=4\) are both \(3\cdot\frac9{16}=4\cdot\frac{27}{64}=\frac{27}{16}\), which is the maximum.

**15.2.** Modulo \(p_*\), \(z'=j_1w_z+hz\) has nonzero coordinate along \(w_z\), so it is never a multiple of \(z\); its line differs from \([z]_{p_*}\).

**15.3.** \(B=\lceil L^2\rceil\le2L^2\) and \(M=\lfloor L^{0.01}\rfloor+1\ge L^{0.01}\). For \(L^{1-0.005K}\le L^{-5}\) one needs \(0.005K\ge6\), that is \(K\ge1200\).

**15.4.** The basis \(z_*,Dw_*\) of \(\Lambda\) has determinant \(D\det(z_*,w_*)=D\), and the coordinates \((c_1,c_2)\) differ from \((h,l)\) by an element of \(\mathrm{SL}_2(\mathbb Z)\).

**15.5.** Test (G2) controls the products \(DZ\) where \(Z\) runs over the primes of the groups of \(I\setminus\{i_*\}\); the number of such products must be \(\exp(o(L^{a_{i_*}}))\) for the separation \(100e^{-L^{a_{i_*}}}\) to be achievable for most ratios (Lemma 3.2 of Lesson 8). This holds when every other group of \(I\) has a smaller band exponent, that is when \(i_*\) is the largest index. The arc in (2.2) has length \(32/p_*\) with \(p_*\) in the band of \(i_*\), which matches the separation scale.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Sections 4.6 and 4.7. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
