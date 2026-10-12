# Projection games and the base game

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a projection game two players answer questions, and the answer of the first determines the only accepted answer of the second. In a *2-to-1 game* every answer of the second player is the image of exactly two answers of the first. Khot's 2-to-1 games conjecture with perfect completeness says that it is NP-hard to tell games in which the players can always win from games in which they win with a probability of at most \(\delta\), for every fixed \(\delta>0\). [OpenAI-G] gives a proof.

This lesson defines the games, and builds the game from which the reduction of [OpenAI-G] starts: a game with small value in the bad case and value one in the good case, whose projections are not yet 2-to-1. It rests on two theorems of the theory of probabilistically checkable proofs, which are stated as hypotheses.

- Projection games and their value (Section 1); randomness does not help (Lemma 1.1).
- Repeated games and the hypothesis (PR) (Section 2).
- Formulas with a gap: the hypothesis (PCP) and its normal form (Proposition 3.1).
- The clause-variable game (Lemma 4.1) and the base game (Theorem 5.1).

The lesson follows [OpenAI-G, Sections 1.1 and 2.1]. It needs only finite probability and Boolean formulas.

## 1. Projection games

**Definition.** A *projection game* \(G\) consists of

- two disjoint finite sets \(U\) and \(V\) of *questions*;
- for every question a nonempty finite set of *answers*: \(L_u\) for \(u\in U\) and \(R_v\) for \(v\in V\);
- a nonempty finite set \(\mathcal E\) of *edges* with a probability distribution \(\mu\) on it; every edge \(e\) has two ends \(u(e)\in U\), \(v(e)\in V\) and a map \(\pi_e:L_{u(e)}\to R_{v(e)}\).

Different edges may have the same ends and different maps. A *labeling* chooses an answer \(a(u)\in L_u\) for every \(u\) and \(b(v)\in R_v\) for every \(v\). It *satisfies* the edge \(e\) if \(\pi_e(a(u(e)))=b(v(e))\). The *value* \(\operatorname{val}(G)\) of the game is the largest probability, over the labelings \((a,b)\), of the set of the satisfied edges:
\[
\max_{a,b}\ \mu\bigl\{e:\ \pi_e(a(u(e)))=b(v(e))\bigr\}.
\]
One thinks of two players who cannot communicate: an edge is drawn with the law \(\mu\), the first player sees only \(u(e)\), the second only \(v(e)\), and they win if their answers satisfy the edge.

A *2-to-1 game* has the answer sets \(L_u=\{1,\dots,2q\}\) and \(R_v=\{1,\dots,q\}\) for all questions, for some \(q\ge1\), and every \(\pi_e\) takes every value exactly twice.

**Lemma 1.1.** If the players choose their answers with the help of random numbers that are independent of the edge, their probability of winning is at most \(\operatorname{val}(G)\).

**Proof.** For every value of the random numbers, the answers form a labeling, which wins with a probability of at most \(\operatorname{val}(G)\). The probability of winning is the mean of these probabilities, because the random numbers are independent of the edge. \(\blacksquare\)

**The theorem of [OpenAI-G].** For every rational \(\delta\in(0,1)\) there are an integer \(q\ge2\) and a map, computable in polynomial time, from Boolean formulas in conjunctive normal form with three literals per clause to 2-to-1 games with the answer sets \(\{1,\dots,2q\}\) and \(\{1,\dots,q\}\) and the uniform law on an explicit list of edges, such that a satisfiable formula gives a game of value \(1\) and an unsatisfiable formula a game of value at most \(\delta\).

This lesson does not prove it. It prepares the starting point of the proof.

## 2. Repetition

For \(k\ge1\), the *\(k\)-fold repetition* \(G^{\otimes k}\) is the following projection game. Its edges are the \(k\)-tuples \((e_1,\dots,e_k)\) of edges of \(G\), with the product law. The questions are the \(k\)-tuples of questions, the answers the \(k\)-tuples of answers, and the map of \((e_1,\dots,e_k)\) applies \(\pi_{e_i}\) to the \(i\)-th answer. So the players get \(k\) independent rounds at once and must win all of them.

A labeling of \(G\) that satisfies all edges gives one for \(G^{\otimes k}\), so value \(1\) is preserved. Playing each round with a best labeling of \(G\) shows \(\operatorname{val}(G^{\otimes k})\ge\operatorname{val}(G)^k\). An upper bound is a deep theorem:

**Hypothesis (PR), parallel repetition.** For every projection game \(G\), every \(0<g<1\) and every \(k\ge1\),
if \(\operatorname{val}(G)\le1-g\), then
\[
\operatorname{val}(G^{\otimes k})\le\Bigl(1-\frac{g^2}{16}\Bigr)^k .
\]

According to [OpenAI-G], exponential decay under repetition was first proved by R. Raz, and this bound, which does not depend on the sizes of the answer sets, is a theorem of I. Dinur and D. Steurer (2014). It is not proved in this course.

## 3. Formulas with a gap

A *3-formula* is a list of clauses, each the disjunction of three literals in three different variables. An assignment *violates* a clause if it makes all three literals false.

**Hypothesis (PCP).** There are a finite set \(\Sigma\), an integer \(k_0\ge1\), a number \(\theta>0\), and a map, computable in polynomial time, that sends a Boolean formula \(\varphi\) in conjunctive normal form with three literals per clause to a list of \(N\ge1\) *predicates*: each predicate names at most \(k_0\) variables with values in \(\Sigma\) and a set of accepted tuples of values. If \(\varphi\) is satisfiable, some assignment of values is accepted by all predicates. If \(\varphi\) is not satisfiable, every assignment is rejected by at least \(\theta N\) of the predicates.

This is a form of the PCP theorem with perfect completeness. According to [OpenAI-G] the theorem goes back to Arora and Safra and to Arora, Lund, Motwani, Sudan and Szegedy, and this form is in I. Dinur's proof (2007). It is not proved in this course.

**Proposition 3.1.** Assume (PCP). There are a number \(\gamma_0>0\) and a map, computable in polynomial time, from formulas \(\varphi\) as above to 3-formulas \(\Psi\) with at least one clause, such that \(\Psi\) is satisfiable if \(\varphi\) is, and every assignment violates at least a fraction \(\gamma_0\) of the clauses of \(\Psi\) if \(\varphi\) is not satisfiable.

**Proof.** *Bits.* Fix a one-to-one coding of the elements of \(\Sigma\) by words of \(m\) bits, and a default element of \(\Sigma\). Replace every variable by \(m\) Boolean variables, and every predicate by the Boolean predicate that accepts if all its blocks are code words and the decoded values are accepted. An accepted assignment gives an accepted Boolean assignment. Conversely, decode a Boolean assignment, reading every block that is not a code word as the default element. If the old predicate rejects the decoded values, the new one rejects the Boolean assignment: either a block is not a code word, or all are and the decoded values are rejected. So in the bad case every Boolean assignment is rejected by at least \(\theta N\) predicates. Each new predicate depends on at most \(w=k_0m\) variables.

*Clauses.* A Boolean predicate on \(k\le w\) variables is the conjunction of the clauses that exclude exactly one rejected assignment each; there are at most \(2^w\) of them, each with \(k\) literals. (A predicate on no variables that rejects gives the empty clause.)

*Three literals.* A clause \(\ell_1\vee\dots\vee\ell_k\) with \(k\ge4\) is replaced by the \(k-2\) clauses
\[
\begin{gathered}
\ell_1\vee\ell_2\vee y_1,\\
\neg y_j\vee\ell_{j+2}\vee y_{j+1}\quad(1\le j\le k-4),\\
\neg y_{k-3}\vee\ell_{k-1}\vee\ell_k,
\end{gathered}
\]
with new variables \(y_1,\dots,y_{k-3}\) used only here. If all \(\ell_h\) are false, the first clause needs \(y_1\) true, then each middle clause needs the next \(y\) true, and the last clause is violated: some new clause is violated whatever the \(y\) are. If some \(\ell_h\) is true, let \(y_j\) be true exactly if \(\ell_1,\dots,\ell_{j+1}\) are all false; then all the new clauses hold.

After these steps there are at most \(B\,N\) clauses, with \(B=2^w\max\{1,w-2\}\); they are all satisfied by an extension of an accepted assignment; and in the bad case every assignment violates at least \(\theta N\) of them, at least one for each rejecting predicate.

*Three different variables.* Remove the clauses that contain a variable and its negation, and repeated literals in the others. A remaining clause \(C\) on \(k\le3\) different variables is replaced by the \(2^{3-k}\) clauses \(C\vee\pm z_1\vee\dots\vee\pm z_{3-k}\) with all patterns of signs, where the \(z\) are new variables used only here. If \(C\) is true, all of them are true. If \(C\) is false, exactly one of them is false, for every choice of the \(z\). The number of clauses grows at most by the factor \(8\), and every violated clause still gives a violated clause. So \(\gamma_0=\theta/(8B)\) has the stated property. If no clause is left, which cannot happen in the bad case, take one clause on three new variables. \(\blacksquare\)

## 4. The clause-variable game

Let \(\Psi\) be a 3-formula. For a clause \(C\) let \(\mathcal A_C\subset\{0,1\}^3\) be the set of the seven assignments to its three variables, in their order, that do not violate it.

**Definition.** The game \(G_\Psi\): an edge is a pair \((C,h)\) of a clause and a position \(h\in\{1,2,3\}\), with the uniform law. The first player gets the clause \(C\) and answers with an element of \(\mathcal A_C\). The second gets the variable at the position \(h\) of \(C\) and answers with a bit. The map \(\pi_{(C,h)}\) takes the \(h\)-th bit.

**Lemma 4.1.** If \(\Psi\) is satisfiable, \(\operatorname{val}(G_\Psi)=1\). If every assignment violates at least a fraction \(\gamma\) of the clauses, then \(\operatorname{val}(G_\Psi)\le1-\gamma/3\).

**Proof.** A satisfying assignment gives a labeling: the second player answers with the value of the variable, the first with the values of the three variables of the clause, which lie in \(\mathcal A_C\). It satisfies every edge. For the second statement fix a labeling. The answers of the second player are an assignment of the variables. At a clause \(C\) that it violates, the answer of the first player, an element of \(\mathcal A_C\), differs from this assignment in at least one position, and the edge for that position is not satisfied. So at least a fraction \(\gamma\cdot\tfrac13\) of the edges is not satisfied. \(\blacksquare\)

**Lemma 4.2.** For every clause \(C\), the set \(\mathcal A_C\) is mapped onto \(\{0,1\}\) by each of the three positions, and onto \(\{0,1\}^2\) by each pair of two different positions.

**Proof.** Only one of the eight triples is missing from \(\mathcal A_C\), and every pair of values at two positions has two extensions to a triple. \(\blacksquare\)

The maps of \(G_\Psi\) are not 2-to-1: a bit has three or four preimages in \(\mathcal A_C\).

## 5. The base game

**Theorem 5.1.** Assume (PCP) and (PR), and let \(\gamma_0\) be as in Proposition 3.1. For \(\sigma>0\) let \(t\) be an integer with \((1-\gamma_0^2/144)^t\le\sigma\). Then the game \(G_{\mathrm{base}}=G_\Psi^{\otimes t}\), computed from \(\varphi\) in polynomial time, has the value \(1\) if \(\varphi\) is satisfiable and a value of at most \(\sigma\) otherwise. The first player answers with an element of a product of \(t\) sets \(\mathcal A_C\), with \(7^t\) elements, and the second with an element of \(\{0,1\}^t\).

**Proof.** By Proposition 3.1 and Lemma 4.1, \(\operatorname{val}(G_\Psi)\) is \(1\) in the first case and at most \(1-\gamma_0/3\) in the second. Value \(1\) is preserved by repetition, and (PR) with \(g=\gamma_0/3\) gives \((1-\gamma_0^2/144)^t\) in the second case. Since \(t\) is fixed, the game has a size polynomial in the size of \(\Psi\). \(\blacksquare\)

In the repeated game the coordinates of an answer stay separate: if the same variable occurs twice in a question of the second player, the two bits of the answer need not be equal.

The base game has value \(1\) or at most \(\sigma\), as small as one likes, but an answer of the second player has up to \(4^t\) preimages. Repetition lowers the value and raises this number. The construction of [OpenAI-G] turns the base game into a game whose maps have at most two preimages of every answer and whose value is still small in the bad case; its analysis uses a third theorem from the literature, on the expansion of Grassmann graphs (S. Khot, D. Minzer and M. Safra).

## 6. Exercises

**6.1.** Show that \(\operatorname{val}(G^{\otimes k})\ge\operatorname{val}(G)^k\).

**6.2.** Write the clauses that replace \(\ell_1\vee\ell_2\vee\ell_3\vee\ell_4\vee\ell_5\) in the proof of Proposition 3.1, and give the values of the new variables that satisfy them when only \(\ell_4\) is true.

**6.3.** Let \(C\) be the clause \(x_1\vee\neg x_2\vee x_3\). List \(\mathcal A_C\) and the preimages of the two bits under the map of the position \(2\).

**6.4.** Let \(\Psi\) be a 3-formula with \(m\) clauses that is not satisfiable. Show that \(\operatorname{val}(G_\Psi)\le1-\tfrac1{3m}\).

## 7. Solutions

**6.1.** Let \((a,b)\) be a labeling of \(G\) that satisfies edges of total probability \(\operatorname{val}(G)\). In \(G^{\otimes k}\) answer the question \((u_1,\dots,u_k)\) by \((a(u_1),\dots,a(u_k))\), and similarly for the second player. The edge \((e_1,\dots,e_k)\) is satisfied if every \(e_i\) is satisfied by \((a,b)\); the \(e_i\) are independent, so this has the probability \(\operatorname{val}(G)^k\).

**6.2.** With \(k=5\): \(\ell_1\vee\ell_2\vee y_1\), \(\neg y_1\vee\ell_3\vee y_2\), \(\neg y_2\vee\ell_4\vee\ell_5\). If only \(\ell_4\) is true: \(y_1\) is true (since \(\ell_1,\ell_2\) are false) and \(y_2\) is true (since \(\ell_1,\ell_2,\ell_3\) are false). The clauses read: true by \(y_1\); true by \(y_2\); true by \(\ell_4\).

**6.3.** The clause is violated only by \((x_1,x_2,x_3)=(0,1,0)\). So \(\mathcal A_C\) consists of the other seven triples. The bit \(0\) at the position \(2\) has the four preimages \(000,001,100,101\); the bit \(1\) has the three preimages \(011,110,111\).

**6.4.** Every assignment violates at least one clause, a fraction \(\tfrac1m\). Apply Lemma 4.1 with \(\gamma=\tfrac1m\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
