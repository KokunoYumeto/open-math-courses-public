# The second Kahn–Kalai conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the theorem stated as Theorem 5.1 in [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), due to OpenAI [OpenAI-KK2]:

**Theorem 3.1** (OpenAI 2026; the second Kahn–Kalai conjecture). For every \(n\ge2\) and every graph \(H\) with \(h\ge1\) edges and at most \(n\) vertices,
\[
p_{\mathrm c}(n,H)\le\min\bigl\{1,\ 2048\,\mathrm e^{50}\,p_{\mathrm E}(n,H)\,(1+\log_2h)\bigr\}\qquad\text{and}\qquad p_{\mathrm c}(n,H)\le6144\,\mathrm e^{50}\,p_{\mathrm E}(n,H)\log_2n.
\]

By Theorem 3.2 of [Covering a probability tree](covering-a-probability-tree.md), it suffices to build a disjoint probability tree on the edge set \(X=\binom{[n]}2\) of \(K_n\) whose path unions are copies of \(H\), whose levels are \(128\,p_{\mathrm E}(n,H)\)-spread, and whose capacities grow by factors of at least \(16\) up to at most \(e(H)\). A tree with one level does not suffice in general. By Exercise 6.5 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), the uniform law on the copies of \(H\) is \((2\mathrm e\,e(H)\,p_{\mathrm E}(n,H))\)-spread, and with this parameter Corollary 4.1 of [Covering a probability tree](covering-a-probability-tree.md) gives only \(p_{\mathrm c}(n,H)=O(e(H)\,p_{\mathrm E}(n,H)\log e(H))\); the factor \(e(H)\) comes from counting the copies of a subgraph inside \(H\). The tree instead builds \(H\) in stages \(\varnothing=H_0\subset H_1\subset\dots\subset H_k=H\), where each \(H_{i-1}\) maximizes a ratio comparing a containment probability with a power of \(\sigma=128\,p_{\mathrm E}(n,H)\). This choice, Tran's spread-link construction [Tran], makes each stage spread conditionally on the previous one and forces \(|H_{i-1}|<|H_i|/17\).

*Conventions.* As in Section 3 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), graphs without isolated vertices are identified with their edge sets, copies are taken on \([n]\), \(M(F)\) is the number of copies of \(F\) on \([n]\), and \(M(I,F)\) the number of copies of \(F\) contained in \(I\). Throughout Sections 1 and 2, \(H\) has \(h\ge1\) edges, at most \(n\) vertices and no isolated vertices, \(q=p_{\mathrm E}(n,H)\), and \(\sigma=128q\).

## 1. A ratio over subgraphs

By Lemma 3.2(2) of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md),
\[
M(S)\,q^{|S|}\ge\tfrac12\qquad\text{for every nonempty }S\subseteq H.\tag{1.1}
\]
For a nonempty \(I\subseteq H\) and \(S\subseteq I\), let \(\mathbf I\) be a uniformly random copy of \(I\) on \([n]\), let \(S_0\) be a copy of \(S\) on \([n]\), and put
\[
R(I,S)=\sigma^{-|S|}\,\mathbb P(S_0\subseteq\mathbf I)=\sigma^{-|S|}\,\frac{M(I,S)}{M(S)};
\]
by Lemma 3.1(3) there, this does not depend on the choice of \(S_0\). In particular \(R(I,\varnothing)=1\).

**Lemma 1.1.** Let \(I\subseteq H\) be nonempty and \(S\subseteq I\) with \(|S|\ge|I|/17\). Then \(R(I,S)<1\). Consequently every maximizer \(S\) of \(R(I,\cdot)\) over the subsets of \(I\) satisfies \(|S|<|I|/17\).

**Proof.** Let \(r=|S|\) and \(h_I=|I|\); then \(r\ge1\). The copies of \(S\) contained in \(I\) are \(r\)-element subsets of \(I\), so \(M(I,S)\le\binom{h_I}r\), and \(M(S)\ge\frac12q^{-r}\) by (1.1). Hence
\[
R(I,S)\le2\binom{h_I}r\Bigl(\frac q\sigma\Bigr)^r=2\binom{h_I}r\,128^{-r}\le2\Bigl(\frac{\mathrm eh_I}{128\,r}\Bigr)^r\le2\Bigl(\frac{17\mathrm e}{128}\Bigr)^r<1,
\]
using \(\binom{h_I}r\le h_I^r/r!\le(\mathrm eh_I/r)^r\) and \(17\mathrm e<64\). A maximizer \(S\) satisfies \(R(I,S)\ge R(I,\varnothing)=1\). \(\square\)

## 2. The hierarchy and the tree

Fix a rule that chooses one maximizer of \(R(I,\cdot)\) for each nonempty \(I\subseteq H\). Starting from \(H\), replace the current nonempty set by its chosen maximizer until the empty set is reached; by Lemma 1.1 the size drops by a factor greater than \(17\) at each step. Numbering the sets obtained in increasing order gives
\[
\varnothing=H_0\subset H_1\subset\dots\subset H_k=H,\qquad|H_{i-1}|<|H_i|/17,\tag{2.1}
\]
with \(k\ge1\), where \(H_{i-1}\) is the chosen maximizer of \(R(H_i,\cdot)\) for \(1\le i\le k\).

**Lemma 2.1** (conditional extensions). Let \(1\le i\le k\), let \(S_0\) be a copy of \(H_{i-1}\) on \([n]\) (so \(S_0=\varnothing\) if \(i=1\)), and let \(\mathbf A=\mathbf I\setminus S_0\), where \(\mathbf I\) is uniformly distributed over the copies of \(H_i\) on \([n]\) that contain \(S_0\). Such copies exist, every value of \(\mathbf A\) has \(|H_i|-|H_{i-1}|\) elements, and
\[
\mathbb P(J\subseteq\mathbf A)\le\sigma^{|J|}\qquad\text{for every nonempty }J\subseteq X.
\]

**Proof.** An isomorphism from \(H_{i-1}\) onto \(S_0\), as a map of vertex sets, extends to an injective map \(V(H_i)\to[n]\), since \(H_i\) has at most \(n\) vertices; the image of \(H_i\) is a copy containing \(S_0\). Every value of \(\mathbf A\) has \(|H_i|-|S_0|\) elements.

Let \(\mathbf I'\) be a uniformly random copy of \(H_i\) on \([n]\); then \(\mathbf I\) has the law of \(\mathbf I'\) conditioned on the event \(S_0\subseteq\mathbf I'\), which has positive probability. If \(J\cap S_0\neq\varnothing\), then \(\mathbb P(J\subseteq\mathbf A)=0\). Otherwise
\[
\mathbb P(J\subseteq\mathbf A)=\frac{\mathbb P(S_0\cup J\subseteq\mathbf I')}{\mathbb P(S_0\subseteq\mathbf I')}.
\]
If the numerator is positive, \(S_0\cup J\) lies in the image of \(H_i\) under some isomorphism \(\psi\) onto a copy, and the preimage \(U=\psi^{-1}(S_0\cup J)\) is a subset of \(H_i\) with \(|S_0|+|J|\) elements of which \(S_0\cup J\) is a copy. Since \(H_{i-1}\) maximizes \(R(H_i,\cdot)\) and \(S_0\) is a copy of \(H_{i-1}\),
\[
\sigma^{-|S_0|-|J|}\,\mathbb P(S_0\cup J\subseteq\mathbf I')=R(H_i,U)\le R(H_i,H_{i-1})=\sigma^{-|S_0|}\,\mathbb P(S_0\subseteq\mathbf I'),
\]
which is the claim. \(\square\)

**Lemma 2.2** (the tree; OpenAI, after Tran). There is a disjoint probability tree on \(X\) with \(k\) levels such that every path union is a copy of \(H\), every level is \(\sigma\)-spread, and the labels of level \(i\) have exactly \(\ell_i=|H_i|-|H_{i-1}|\) elements, where
\[
\ell_1\ge1,\qquad\ell_{i+1}\ge16\,\ell_i\quad(1\le i<k),\qquad\ell_k\le h.
\]

**Proof.** The nodes at depth \(i\) are the sequences \((S^0,S^1,\dots,S^i)\) with \(S^0=\varnothing\), each \(S^j\) a copy of \(H_j\) on \([n]\), and \(S^{j-1}\subseteq S^j\); the root is \((\varnothing)\). For \(i\le k\), the children of a node \((S^0,\dots,S^{i-1})\) are the sequences \((S^0,\dots,S^{i-1},S^i)\), with the uniform law, and the arc to such a child carries the label \(S^i\setminus S^{i-1}\). By Lemma 2.1 every node at depth \(i-1<k\) has children, so all leaves have depth \(k\); the law of the label is that of \(\mathbf A\) in Lemma 2.1 with \(S_0=S^{i-1}\), so level \(i\) is \(\sigma\)-spread and its labels have exactly \(\ell_i\) elements. Along a path, the labels \(S^j\setminus S^{j-1}\) are pairwise disjoint, since for \(j<i\) the label \(S^j\setminus S^{j-1}\) lies in \(S^{i-1}\); their union is \(S^k\), a copy of \(H\). Finally \(\ell_1=|H_1|\ge1\), \(\ell_k\le|H_k|=h\), and by (2.1), \(\ell_{i+1}=|H_{i+1}|-|H_i|>16|H_i|\ge16\,\ell_i\). \(\square\)

The nodes are histories, so the tree is a genuine tree even when different histories end at the same copy.

## 3. The theorem

**Proof of Theorem 3.1.** By Lemma 3.2(4) of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md) we may assume that \(H\) has no isolated vertices, and by Lemma 3.2(3) there, \(q=p_{\mathrm E}(n,H)>0\). The tree of Lemma 2.2 satisfies the hypotheses of Theorem 3.2 of [Covering a probability tree](covering-a-probability-tree.md) with spread \(\sigma=128q\) and capacities \(\ell_i\). Since \(16\cdot128=2048\) and \(\ell_k\le h\),
\[
r=\min\bigl\{1,\ 16\,\mathrm e^{50}\sigma(1+\log_2\ell_k)\bigr\}\le\min\bigl\{1,\ 2048\,\mathrm e^{50}q(1+\log_2h)\bigr\},
\]
and the edge set of \(G(n,r)\) contains the union of some path, a copy of \(H\), with probability at least \(\frac23\). Hence \(p_{\mathrm c}(n,H)\le r\), which is the first bound. For the second, \(h\le\binom n2<n^2\) and \(n\ge2\) give \(1+\log_2h<1+2\log_2n\le3\log_2n\), and \(3\cdot2048=6144\). \(\square\)

**Corollary 3.2** (perfect matchings). For every even \(n\ge16\),
\[
\frac{\log n}{3n}<p_{\mathrm c}(n,\mathrm{PM}_n)\le2048\,\mathrm e^{52}\,\frac{\log_2n}n.
\]

**Proof.** The lower bound is Proposition 4.3 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md). For the upper bound, \(p_{\mathrm E}(n,\mathrm{PM}_n)\le\mathrm e^2/n\) by Proposition 4.2 there, and \(1+\log_2(n/2)=\log_2n\). \(\square\)

So for perfect matchings, and likewise for Hamilton cycles (Exercise 4.4), the ratio \(p_{\mathrm c}/p_{\mathrm E}\) is of order \(\log n\), and Theorem 3.1 is sharp up to the value of the constant.

The maximization of \(R\) and the conditional spread bound (Lemmas 1.1 and 2.1) are Tran's construction [Tran], whose conditioning step has antecedents in work of Lovett, Solomon and Zhang and of Alweiss, Lovett, Wu and Zhang [ALWZ]. The planted transition is due to Mossel, Niles-Weed, Sun and Zadik [MNSZ-2]. Tran proposed a coupling conjecture that would pay the logarithmic sampling cost only once along such a chain of conditional extensions. OpenAI's tree reduction obtains the required containment bound directly, with one random set serving all levels of the tree at once [OpenAI-KK2].

## 4. Exercises

**Exercise 4.1** (easy). For \(H=K_2\) and \(n\ge2\), show that the hierarchy has \(k=1\) and that the tree of Lemma 2.2 is the uniform law on the \(\binom n2\) edges.

**Exercise 4.2** (easy). Show that the number \(k\) of levels satisfies \(k<1+\log_{17}h\) when \(h\ge2\), and \(k=1\) when \(h\le17\).

**Exercise 4.3** (easy). Let \(1\le i\le k\), let \(\mathbf I\) be a uniformly random copy of \(H_i\) on \([n]\), and let \(S_0\) be a copy of \(H_{i-1}\). Show that \(\mathbb P(S_0\subseteq\mathbf I)\ge\sigma^{|H_{i-1}|-|S'|}\,\mathbb P(S_0'\subseteq\mathbf I)\) for every \(S'\subseteq H_i\) and every copy \(S_0'\) of \(S'\), and deduce that \(\mathbb P(S_0\subseteq\mathbf I)\ge\sigma^{|H_{i-1}|}\).

**Exercise 4.4** (medium). Let \(n\ge3\) and let \(C_n\) be the cycle through all \(n\) vertices. Show that \(p_{\mathrm E}(n,C_n)\le\mathrm e^2/n\). Deduce that \(\frac{\log n}{3n}<p_{\mathrm c}(n,C_n)\le2048\,\mathrm e^{52}(1+\log_2n)/n\) for \(n\ge16\).

## 5. Solutions

**4.1.** Here \(q=p_{\mathrm E}(n,K_2)=1/(2\binom n2)\), so \(\sigma=64/\binom n2\), and \(R(K_2,K_2)=\sigma^{-1}\big/\binom n2=\frac1{64}<1=R(K_2,\varnothing)\). So \(H_0=\varnothing\), \(H_1=K_2\), and the root has one child for each edge, with the uniform law. Each edge lies in the label with probability \(1/\binom n2\le\sigma\).

**4.2.** By (2.1), \(|H_1|\ge1\) and \(|H_i|>17|H_{i-1}|\), so \(h=|H_k|>17^{k-1}\) when \(k\ge2\), that is, \(k<1+\log_{17}h\). If \(h\le17\), then \(k\ge2\) would give \(h>17\); so \(k=1\). (Directly: Lemma 1.1 makes \(\varnothing\) the only maximizer for \(h\le17\), since every nonempty \(S\subseteq H\) has \(|S|\ge1\ge h/17\).)

**4.3.** For a copy \(S_0'\) of \(S'\subseteq H_i\), the maximality of \(H_{i-1}\) gives \(\sigma^{-|H_{i-1}|}\mathbb P(S_0\subseteq\mathbf I)=R(H_i,H_{i-1})\ge R(H_i,S')=\sigma^{-|S'|}\mathbb P(S_0'\subseteq\mathbf I)\), which rearranges to the inequality. Taking \(S'=\varnothing\), with \(S_0'=\varnothing\), gives \(\mathbb P(S_0\subseteq\mathbf I)\ge\sigma^{|H_{i-1}|}\).

**4.4.** The nonempty edge subsets of \(C_n\) are \(C_n\) itself and the linear forests \(F\) with \(c\ge1\) paths and \(j\ge c\) edges, which have \(j+c\le n\) vertices. An automorphism of \(F\) permutes its paths, mapping each to one of the same length, and acts on each path as the identity or the reversal; so \(|\operatorname{Aut}F|\le c!\,2^c\le(2c)^c\). With Lemmas 3.1(1) and 4.1 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md),
\[
M(F)\Bigl(\frac{\mathrm e^2}n\Bigr)^j\ge\frac{(n/\mathrm e)^{j+c}\,\mathrm e^{2j}}{(2c)^c\,n^j}=\Bigl(\frac n{2c}\Bigr)^c\mathrm e^{j-c}\ge1,
\]
since every path has at least two vertices, so that \(2c\le j+c\le n\), and \(j\ge c\). For the cycle, \(|\operatorname{Aut}C_n|=2n\), and \(M(C_n)(\mathrm e^2/n)^n\ge(n/\mathrm e)^n\mathrm e^{2n}/(2n\cdot n^n)=\mathrm e^n/(2n)\ge\frac12\). So every condition of Lemma 3.2(2) there holds at \(p=\mathrm e^2/n\) when \(\mathrm e^2/n\le1\), and the bound is trivial otherwise. Theorem 3.1 with \(h=n\) gives the upper bound. A graph containing a Hamilton cycle on \([n]\) has no isolated vertex, so Proposition 4.3 there gives \(\mathbb P(N(G(n,p),C_n)>0)<\frac12\) at \(p=\frac{\log n}{3n}\), and as in its proof \(p_{\mathrm c}(n,C_n)>\frac{\log n}{3n}\).

## References

- [OpenAI-KK2] OpenAI, *The second Kahn–Kalai conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026
- [Tran] T. Tran, *Fractional expectation thresholds and the "second" Kahn–Kalai conjecture*, 2026. https://arxiv.org/abs/2609.20546
- [MNSZ-2] E. Mossel, J. Niles-Weed, N. Sun and I. Zadik, *A second moment proof of the spread lemma*, 2022; published as *A Bayesian proof of the spread lemma*, Random Structures & Algorithms 66 (2025). https://arxiv.org/abs/2209.11347
- [ALWZ] R. Alweiss, S. Lovett, K. Wu and J. Zhang, *Improved bounds for the sunflower lemma*, Annals of Mathematics 194 (2021), 795–815. https://arxiv.org/abs/1908.08483
