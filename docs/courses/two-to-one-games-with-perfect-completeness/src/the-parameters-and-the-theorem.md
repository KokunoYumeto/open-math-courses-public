# The parameters and the theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The lessons on the proof of soundness derived a contradiction from a labeling that satisfies the test with a probability of at least \(\varepsilon\), under a list of conditions on the parameters of the game: the depth of the tree, the numbers of rows, the numbers of products in the sampler, the number of repetitions in the base game, and the numbers of children. This lesson shows that all the conditions can be met at the same time. The order of the choices matters. The numbers of rows are chosen from the root downwards, because the row number at a level must be large in terms of the agreement probabilities of all higher levels. Then the number of repetitions is chosen, and at the end the numbers of children from the leaves upwards, because the bounds at a level depend on the numbers of children below it. This is possible because the bounds of the inverse theorem and of the list of heavy characters contain no dimension.

The game obtained in this way has perfect completeness, constraints with at most two preimages, and a value below \(\varepsilon\) for a formula that is not satisfiable. Two elementary steps turn it into a 2-to-1 game with the uniform law on a list of edges. This proves the theorem of [OpenAI-G] from the three hypotheses of the course.

- The conditions (Section 1) and the choice of the parameters (Proposition 2.1).
- Soundness (Theorem 3.1).
- Maps that are exactly 2-to-1 (Proposition 4.1).
- Equal weights and the size of the game (Propositions 5.1 and 5.2).
- The theorem (Theorem 6.1).

The lesson follows [OpenAI-G, Section 8]. It uses the results of all earlier lessons of the course: [Projection games and the base game](projection-games-and-the-base-game.md), [Matrices, slices and the inverse theorem](matrices-slices-and-the-inverse-theorem.md), [The tree of function spaces and the questions](the-tree-of-function-spaces-and-the-questions.md), [Folding and the law of the tests](folding-and-the-law-of-the-tests.md), [Changing the law of the tests](changing-the-law-of-the-tests.md), [Two accepted levels and the upper response](two-accepted-levels-and-the-upper-response.md), [The heavy list and the two decoders](the-heavy-list-and-the-two-decoders.md), [From tested rank to full rank](from-tested-rank-to-full-rank.md) and [Clean children and repetition](clean-children-and-repetition.md).

## 1. The conditions

The game of the lesson on folding has the parameters \(t\), \(d\), \(n_p\), \(\ell_p\), \(R_p\) for \(1\le p\le d\). Let \(0<\varepsilon<1\), and assume the hypothesis (GE). The following numbers were defined in the lessons on the proof of soundness.

*Numbers that depend only on \(\varepsilon\):*
\[
c=\frac{\varepsilon^2}2,\qquad\kappa=\frac c2,\qquad\eta=\frac{c^2}{32},
\]
the numbers \(\alpha\le1\), \(r\), \(\ell_0\) of Lemma 4.2 of the lesson on matrices and slices for \(\eta\), and \(\rho=\kappa\alpha/4\).

*Numbers that depend on \(\varepsilon\) and on the row number \(\ell_j\) of a level \(j\ge2\):*
\[
\begin{gathered}
h_{0,j}=2^{-r\ell_j},\qquad g_{0,j}=\frac{\eta^2}4\,h_{0,j}^2,\\
b_{0,j}=\frac{\kappa\alpha}4\,g_{0,j},\qquad\tau_j=\frac\rho4\,h_{0,j},\\
\gamma_j=b_{0,j}\cdot2^{-\ell_j}\cdot\frac{\tau_j^2}2\cdot2^{-r},
\end{gathered}
\]
the numbers \(\alpha'_j\le1\), \(r'_j\), \(\ell'_{0,j}\) of the inverse theorem (Theorem 4.1 of the lesson on matrices and slices) for \(\eta'_j=\gamma_j^2/8\), and integers \(m_j\ge1\), \(s_j\ge1\) with
\[
\begin{gathered}
\bigl[1+(2^{m_j}-1)^2\bigr]\,2^{-m_j^2}<\frac{\alpha'_j}2,\\
2^{\,m_j-(s_j-2r'_j)}<\frac{\alpha'_j}2 .
\end{gathered}
\]
Such integers exist: the first expression tends to \(0\) as \(m_j\) grows, and then \(s_j\) is taken large.

*Bounds that depend on the numbers of children.* For a level \(p\) let \(T^*_p=T_p+\prod_{h=p+1}^dc_h+1\). For every pair \(i<j\), the numbers of calls at \(D_i\) and at \(D_j\) that the lessons use are at most \(T^*_i\) and \(T^*_j\). Let \(L^*_p\) be the bound \(L_p\) of the lesson on changing the law for \(T^*_p\) calls, and \(p_{0,p}\) the number \(p_0\) of the lesson on clean children for the level \(p\). Both depend on \(t\), on the numbers \(\ell_k\) and \(R_k\), and on the numbers \(n_k\) with \(k<p\). They do not depend on \(n_p\), on the \(n_k\) with \(k>p\), or on the formula. A bound \(L_p\) for more calls is also a bound for fewer calls.

**The conditions.** With \(\beta_p=n_p^{-2/3}\), \(\omega=\min_j\alpha g_{0,j}/16\) and \(\gamma_*=\min_j\gamma_j\), where the minima are over \(2\le j\le d\):

- (P1) \(d\varepsilon\ge4\);
- (P2) for every level \(j\): \(\ell_j\ge\ell_0\) and \(2^{-(\ell_j-r)}<\rho/8\);
- (P3) for every pair \(i<j\): \(\ell_i\ge\max\{\ell'_{0,j},\,2m_j+r'_j\}\);
- (P4) \(R_p\ge6\) for every level \(p\), and \((\tfrac78)^{R_j}\le\min\{h_{0,j}/2,\tau_j^2/2\}\) for \(j\ge2\);
- (P5) with \(s=\max_js_j\): for every Boolean formula \(\varphi\) that is not satisfiable, the base game \(G_\Psi^{\otimes t}\) of the 3-formula \(\Psi\) of Proposition 3.1 of the lesson on projection games has a value of less than \(1/(2s^2)\);
- (P6) for every level \(p\): \(n_p\ge2\), and with \(L=L^*_p\), \(\beta=\beta_p\):
\[
\begin{gathered}
\frac12\sqrt{\frac L{n_p}}\le\frac\omega3,\\
\frac12\sqrt{(1+\beta^2L)^{n_p}-1}\\
\le\min\Bigl\{\frac\omega3,\frac{\gamma_*^2}{64}\Bigr\},\\
\frac{2\beta L}{1-\beta}\le\frac{\gamma_*^2}{64},\\
n_p^{1/3}>\frac{64}{p_{0,p}}\log\frac4{\gamma_*}.
\end{gathered}
\]

## 2. The choice of the parameters

**Proposition 2.1.** Assume (GE), (PCP) and (PR). For every \(0<\varepsilon<1\) there are parameters \(t,d,n_p,\ell_p,R_p\) that satisfy (P1) to (P6).

**Proof.** The parameters are chosen in the following order.

1. Let \(d\) be an integer with \(d\varepsilon\ge4\). The numbers \(c,\kappa,\eta,\alpha,r,\ell_0,\rho\) are then defined.
2. For \(j=d,d-1,\dots,1\) in this order: the numbers \(\ell'_{0,k},m_k,r'_k\) with \(k>j\) are already defined. Choose \(\ell_j\) so large that (P2) holds for \(j\) and (P3) holds for the pairs \(j<k\). For \(j\ge2\) this defines \(h_{0,j},g_{0,j},b_{0,j},\tau_j,\gamma_j\); choose \(R_j\) by (P4), then \(\alpha'_j,r'_j,\ell'_{0,j}\), then \(m_j\), then \(s_j\). For \(j=1\) let \(R_1=6\).
3. Let \(s=\max_js_j\). Choose \(t\) with \((1-\gamma_0^2/144)^t<1/(2s^2)\), where \(\gamma_0\) is the number of Proposition 3.1 of the lesson on projection games. By Theorem 5.1 of that lesson, (P5) holds.
4. For \(p=1,2,\dots,d\) in this order: the numbers \(L^*_p\) and \(p_{0,p}\) depend only on numbers that are already chosen. The three expressions on the left sides of the first three conditions of (P6) tend to \(0\) as \(n_p\to\infty\); for the second one, \((1+n^{-4/3}L)^n\le\exp(Ln^{-1/3})\). The fourth condition is a lower bound for \(n_p\). Choose \(n_p\) so large that (P6) holds.

No choice changes a number on which an earlier choice was based. In step 2 this holds because the numbers \(\alpha,r,\ell_0\) and \(\alpha'_j,r'_j,\ell'_{0,j}\) of the inverse theorem depend only on its threshold, not on the space \(H\) or on the number of values of the table, and because \(\gamma_j\) contains no dimension. So the numbers of step 2 do not depend on \(t\) or on the numbers of children, although these determine the dimensions of all function spaces. In step 4 it holds because \(L^*_p\) and \(p_{0,p}\) do not depend on the \(n_k\) with \(k\ge p\). \(\blacksquare\)

The conditions of the lessons hold with the common number \(s\) in place of \(s_j\): the condition \(2^{\,m_j-(s-2r'_j)}<\alpha'_j/2\) remains true when \(s\) grows.

## 3. Soundness

**Theorem 3.1.** Assume (GE) and (PR). Let \(0<\varepsilon<1\), let the parameters satisfy (P1) to (P4) and (P6), and let \(\Psi\) be a 3-formula whose base game \(G_\Psi^{\otimes t}\) has a value of less than \(1/(2s^2)\). Then the game of the lesson on folding for \(\Psi\) has a value of less than \(\varepsilon\).

**Proof.** Suppose that a labeling of all keys satisfies the test with a probability of at least \(\varepsilon\).

*Two levels.* By (P1) and Lemma 1.1 of the lesson on two accepted levels, there are levels \(i<j\) with \(\mathbb P(\operatorname{Acc}_i\cap\operatorname{Acc}_j)\ge3\varepsilon^2/4\). Fix them.

*The comparison errors.* The numbers \(\delta_i\) and \(\delta_{ij}\) of that lesson are formed with bounds \(L_i\), \(L_j\) for at most \(T^*_i\) and \(T^*_j\) calls. By (P6) for the levels \(i\) and \(j\),
\[
\delta_{ij}\le\frac\omega3+\frac\omega3+\frac\omega3\le\frac{\alpha g_{0,j}}{16}.
\]

*The decoders.* By (P2), (P4) and this bound, Proposition 3.1 of the lesson on the heavy list applies: the bilinear forms of the two decoders agree on the projected space with a probability of at least \(\gamma_j\) under \(\mathbb P_i\).

*Bounded rank.* By (P3) for the pair \(i<j\), by the choice of \(m_j\) and \(s\ge s_j\), and by (P6) for the level \(i\), Proposition 1.1 of the lesson on tested rank applies with \(\gamma=\gamma_j\ge\gamma_*\). So the event \(\mathcal L\), that the forms agree and the left form has a rank of at most \(s\), has \(\mathbb P_i(\mathcal L)\ge\gamma_j/2\).

*The upper bound.* The base game has a value of less than \(1/(2s^2)\). By Proposition 5.1 of the lesson on clean children and the last condition of (P6),
\[
\mathbb P_i(\mathcal L)\le\exp\Bigl(-\frac{p_{0,i}}{64}\,n_i^{1/3}\Bigr)<\frac{\gamma_*}4\le\frac{\gamma_j}4 .
\]
This contradicts the lower bound. \(\blacksquare\)

A game whose questions are only the keys that occur in tests is covered by the theorem: a labeling of these keys is extended to all keys in an arbitrary way, and the probability that it satisfies the test does not change.

## 4. Maps that are exactly 2-to-1

In the game of the lesson on folding the answer sets depend on the question, and a label on the right has one or two preimages. The next statement repairs this. Let \(G\) be a projection game in which every answer of the second player has at most two preimages under every map \(\pi_e\). Let every \(L_u\) have at most \(L_{\max}\) elements and every \(R_v\) at most \(R_{\max}\), and let \(\delta>0\).

**The completed game.** Choose an integer \(q\) with
\[
q\ge\max\{2,R_{\max}\},\qquad2q-L_{\max}\ge\frac6\delta ,
\]
and for every question a one-to-one map of its answer set into \(\{1,\dots,2q\}\) for \(u\in U\), into \(\{1,\dots,q\}\) for \(v\in V\). We regard the answer sets as subsets; their elements are the *legal* answers. A *completion* of an edge \(e\) is a map \(\widehat\pi:\{1,\dots,2q\}\to\{1,\dots,q\}\) that takes every value exactly twice and is equal to \(\pi_e\) on the legal answers of \(u(e)\). The game \(\widehat G\) has the questions of \(G\), the answer sets \(\{1,\dots,2q\}\) and \(\{1,\dots,q\}\), and for every edge \(e\) of \(G\) and every completion \(\widehat\pi\) of \(e\) one edge with the map \(\widehat\pi\); its probability is the probability of \(e\) divided by the number of the completions of \(e\).

**Proposition 4.1.** The game \(\widehat G\) is a 2-to-1 game with weights. If a labeling of \(G\) satisfies all edges, it satisfies all edges of \(\widehat G\). And
\[
\operatorname{val}(\widehat G)\le\operatorname{val}(G)+\frac\delta3 .
\]

**Proof.** *Completions exist.* For \(b\in\{1,\dots,q\}\) let \(c_b\in\{0,1,2\}\) be \(2\) minus the number of the legal preimages of \(b\) under \(\pi_e\); an answer \(b\) that is not legal has no legal preimage. The sum of the \(c_b\) is \(2q\) minus the number of the legal answers on the left, which is the number \(N\) of the answers on the left that are not legal. A completion sends exactly \(c_b\) of these \(N\) answers to \(b\), for every \(b\); there are such maps. By the choice of \(q\), \(N\ge2q-L_{\max}\ge6/\delta\).

*Completeness.* A completion is equal to \(\pi_e\) on the legal answers.

*Soundness.* Fix a labeling of \(\widehat G\), with the answers \(x(u)\) and \(y(v)\). Consider an edge \(e\) of \(G\) with the ends \(u,v\), and a uniform completion \(\widehat\pi\) of it.

- If \(x(u)\) and \(y(v)\) are legal, the edge is satisfied exactly if \(\pi_e(x(u))=y(v)\).
- If \(x(u)\) is legal and \(y(v)\) is not, it is not satisfied, because \(\widehat\pi(x(u))=\pi_e(x(u))\) is legal.
- If \(x(u)\) is not legal: a permutation of the answers that are not legal maps completions to completions. So \(\widehat\pi(a)\) has the same law for all \(N\) such answers \(a\), and since \(c_b\) of them are sent to \(b\), the probability that \(\widehat\pi(x(u))=y(v)\) is \(c_{y(v)}/N\le2/N\le\delta/3\).

Define a labeling of \(G\) by keeping the legal answers and replacing every other answer by a legal one. In the first case it satisfies \(e\) exactly if the labeling of \(\widehat G\) satisfies the completed edges of \(e\). So the labeling of \(\widehat G\) wins with a probability of at most \(\operatorname{val}(G)+\delta/3\). \(\blacksquare\)

## 5. Equal weights and the size of the game

**Proposition 5.1.** Let \(G\) be a projection game with \(M\) edges of positive rational probabilities \(w_1,\dots,w_M\), and \(\delta>0\). Let \(K=\lceil3M/\delta\rceil\), let \(k_a=\lfloor Kw_a\rfloor\), and add \(1\) to \(k_a\) for the first \(K-\sum_a\lfloor Kw_a\rfloor\) edges. Let \(G'\) be the game with \(k_a\) copies of the edge number \(a\) and the uniform law on the \(K\) copies. Then for every labeling the probabilities of winning in \(G\) and in \(G'\) differ by at most \(\delta/3\), and a labeling that satisfies all edges of \(G\) satisfies all edges of \(G'\).

**Proof.** The numbers \(\lfloor Kw_a\rfloor\) have a sum in \((K-M,K]\), so less than \(M\) edges get an additional copy, and \(\sum_ak_a=K\). Every \(k_a/K\) differs from \(w_a\) by at most \(1/K\). So the probabilities of every set of edges under the two laws differ by at most \(M/K\le\delta/3\). The game \(G'\) has no edges other than copies of edges of \(G\). \(\blacksquare\)

**Proposition 5.2.** Fix the parameters \(t,d,n_p,\ell_p,R_p\). There is a procedure that computes, from a 3-formula \(\Psi\) with \(N\) clauses, the list of the tests of positive probability of the game of the lesson on folding, each with its two keys, its map between the labels and its rational probability, in a time that is bounded by a polynomial in the size of \(\Psi\). The numbers of labels at the keys are bounded by a number that depends only on the parameters.

**Proof.** Let \(n\) be the number of the leaves of the tree. A family \(E\) is a choice of \(t\) clauses at each leaf: there are \(N^{tn}\) families, each with the probability \(N^{-tn}\). For a fixed \(E\), the set \(\Omega(E)\) has at most \(7^{tn}\) points, and the spaces \(H_D(E)\) are spaces of functions on such sets. So the path, the uniform functions, the calls of the sampler, the arrays, the level \(p\) and the vector \(a_p\) range over sets whose sizes are bounded in terms of the parameters, with rational probabilities whose denominators are bounded in the same way. For each outcome, the joint function and the function with one bit removed are tables on \(\Omega(E)\); their keys, the labels, the restored values and the map of the constraint are computed by going through these tables. The names of the clauses and variables in the types of the keys have a length that is polynomial in the size of \(\Psi\). The number of labels at a key is at most \(7^{tn}\). \(\blacksquare\)

## 6. The theorem

**Theorem 6.1.** Assume (PCP), (PR) and (GE). For every rational \(\delta\in(0,1)\) there are an integer \(q\ge2\) and a map, computable in polynomial time, from Boolean formulas \(\varphi\) in conjunctive normal form with three literals per clause to 2-to-1 games with the answer sets \(\{1,\dots,2q\}\) and \(\{1,\dots,q\}\) and the uniform law on an explicit list of edges, such that the game of a satisfiable formula has the value \(1\) and the game of a formula that is not satisfiable has a value of at most \(\delta\).

**Proof.** Let \(\varepsilon=\delta/3\), and take parameters as in Proposition 2.1. Let \(\Psi\) be the 3-formula of Proposition 3.1 of the lesson on projection games for \(\varphi\), computed in polynomial time, and \(G_1\) the game of the lesson on folding for \(\Psi\), restricted to the keys and tests of the list of Proposition 5.2.

*The game \(G_1\).* By Lemma 5.1 of the lesson on the tree of function spaces, every label on the right has at most two preimages. If \(\varphi\) is satisfiable, so is \(\Psi\), and by the proposition on perfect completeness of the lesson on the tree of function spaces (its Proposition 5.2) a labeling satisfies every constraint. If \(\varphi\) is not satisfiable, the base game of \(\Psi\) has a value of less than \(1/(2s^2)\) by (P5), and by Theorem 3.1 the game \(G_1\) has a value of less than \(\varepsilon\).

*The game \(G_2\).* The answer sets of \(G_1\) have at most \(7^{tn}\) elements. Take \(q\) as in Section 4 for \(L_{\max}=R_{\max}=7^{tn}\) and \(\delta\); it depends only on \(\delta\) and the parameters. Order the labels at every key by a fixed rule, which gives the maps into \(\{1,\dots,2q\}\) and \(\{1,\dots,q\}\). Let \(G_2=\widehat{G_1}\). By Proposition 4.1 it is a 2-to-1 game with weights; its value is \(1\) with a labeling that satisfies all edges in the first case, and less than \(\varepsilon+\delta/3\) in the second. The number of the completions of an edge is bounded in terms of \(q\), so the list of the edges of \(G_2\) with their probabilities is computed in polynomial time.

*The game \(G_3\).* Apply Proposition 5.1 to \(G_2\) and \(\delta\). The game \(G_3=G_2'\) has the uniform law on a list of \(K\) edges, where \(K\) is at most \(3/\delta\) times the number of the edges of \(G_2\), plus one. Its value is \(1\) in the first case and at most
\[
\varepsilon+\frac\delta3+\frac\delta3=\delta
\]
in the second. \(\blacksquare\)

Since it is NP-hard to decide whether a formula \(\varphi\) of this kind is satisfiable, the theorem says: under the three hypotheses it is NP-hard, for every \(\delta>0\), to tell 2-to-1 games of value \(1\) from 2-to-1 games of value at most \(\delta\).

**What the course proves.** The theorem is proved here from three statements that are named and not proved in the course: the hypothesis (PCP), a theorem on probabilistically checkable proofs with perfect completeness; the hypothesis (PR), parallel repetition for projection games; and the hypothesis (GE), on the expansion of Grassmann graphs. According to [OpenAI-G] all three are theorems in the literature. Every other step, from the construction of the game to the choice of the parameters, is proved in the lessons of the course. The parameters are constants for a fixed \(\delta\); the course gives no bound for them, and the degree of the polynomial that bounds the size of the game grows with them.

**4-to-1 games.** Fei, Minzer and Wang proved, by a different construction, Khot's conjecture for 4-to-1 games with perfect completeness: for every \(\varepsilon>0\) there is an integer \(r\) such that it is NP-hard to tell 4-to-1 games with answer sets of size at most \(r\) and value \(1\) from those of value at most \(\varepsilon\) [FMW, Theorem 1.6]. In their definition every constraint of a \(d\)-to-1 game is a union of products \(\Sigma_{L,i}\times\{b_i\}\) over a partition of the left answer set into blocks of size exactly \(d\) [FMW, Definitions 1.1 and 1.3]. Their construction has three steps: an outer test built from quadratic equations, which gives perfect completeness, a middle test with low-rank checks, and an inner test that combines the Grassmann encoding with a low-rank variant of it [FMW, Section 1.3]. With known reductions they deduce hardness results for colorings of 3-colorable graphs [FMW, Corollaries 1.7 and 1.9]; the course [Large independent sets in three-colorable graphs](course:large-independent-sets-in-three-colorable-graphs/label-cover-and-the-graph-of-the-reduction) compares them with its Theorem 1.1.

## 7. Exercises

**7.1.** Let \(\delta=\tfrac3{10}\). Compute \(\varepsilon\), the smallest \(d\) with (P1), and \(c,\kappa,\eta\).

**7.2.** Why is \(t\) chosen after the numbers \(\ell_j\) and before the numbers \(n_p\)? Name one number that depends on \(t\) and enters a condition on \(n_p\).

**7.3.** Let \(q=3\), let the legal answers on the left be \(1,2,3\) and on the right \(1,2\), and \(\pi(1)=\pi(2)=1\), \(\pi(3)=2\). Compute the numbers \(c_b\) and \(N\), list the completions, and compute the probability that a uniform completion sends the answer \(4\) to \(3\).

**7.4.** Apply Proposition 5.1 to the probabilities \(\tfrac12,\tfrac13,\tfrac16\) with \(K=5\), ignoring the rule for \(K\). Compute the numbers \(k_a\) and the largest difference of the probabilities of a set of edges.

**7.5.** In Proposition 4.1, why does the bound for an answer that is not legal hold for every labeling, although the labeling may depend on the questions?

## 8. Solutions

**7.1.** \(\varepsilon=\tfrac1{10}\), \(d=40\), \(c=\tfrac1{200}\), \(\kappa=\tfrac1{400}\), \(\eta=\tfrac1{1280000}\).

**7.2.** The number \(t\) must make the value of the base game smaller than \(1/(2s^2)\), and \(s\) is known only when all \(\ell_j\) are chosen. The bounds \(L^*_p\) and the numbers \(p_{0,p}\) depend on \(t\): they contain the sizes and dimensions of spaces of functions on products of answer sets of the base game. They enter (P6).

**7.3.** \(c_1=0\), \(c_2=1\), \(c_3=2\), and \(N=3\): the answers \(4,5,6\) are not legal. A completion sends one of them to \(2\) and the other two to \(3\): there are three completions. The answer \(4\) is sent to \(3\) by two of them: the probability is \(\tfrac23=c_3/N\).

**7.4.** \(\lfloor\tfrac52\rfloor=2\), \(\lfloor\tfrac53\rfloor=1\), \(\lfloor\tfrac56\rfloor=0\), with the sum \(3\); the first two edges get one more copy: \(k=(3,2,0)\). The differences \(k_a/K-w_a\) are \(\tfrac1{10},\tfrac1{15},-\tfrac16\). The largest difference for a set of edges is \(\tfrac16\), for the third edge or for the first two together. The third edge has no copy in the new game.

**7.5.** The labeling is fixed before the completion is drawn: the completions of an edge are different edges between the same two questions, and the labeling gives one answer at each question. For fixed answers \(x(u)\), \(y(v)\) the fraction of the completions that send \(x(u)\) to \(y(v)\) is at most \(2/N\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
- [FMW] Y. Fei, D. Minzer and S. Wang, *On the hardness of 4-to-1 games with perfect completeness*, arXiv:2610.12378 (October 2026). https://arxiv.org/abs/2610.12378
