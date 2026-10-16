# Group algebras and zero divisors

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group algebra \(K[G]\) of a group \(G\) over a field \(K\) consists of the finite formal sums of group elements with coefficients in \(K\). If \(G\) has an element of finite order larger than one, \(K[G]\) has zero divisors. Kaplansky's zero-divisor conjecture asked whether removing this obstruction suffices: whether \(K[G]\) has no zero divisors when \(G\) is torsion-free. OpenAI disproved it in 2026 [OpenAI-KZ]: there are a finitely presented torsion-free group \(G\), which even has a finite two-dimensional classifying space, and nonzero elements \(\alpha,\beta\in\mathbb F_2[G]\) with \(\alpha\beta=0\). OpenAI's release contains a formalization of this statement in Lean [OpenAI-KZ-Lean]. This course proves the theorem. This lesson introduces group algebras and unique products, proves the cancellation mechanism that produces the zero divisors, and lays out the rest of the proof.

- Group algebras (Section 1).
- Unique products (Section 2).
- The cancellation mechanism (Section 3).
- The theorem and the plan of the course (Section 4).

## 1. Group algebras

Let \(G\) be a group, written multiplicatively with identity \(1\), and \(K\) a field.

**Definition 1.1.** The *group algebra* \(K[G]\) is the set of functions \(a\colon G\to K\) with finite *support* \(\operatorname{supp}a=\{g:a(g)\ne0\}\), written as finite sums \(a=\sum_ga(g)\,g\). Addition is pointwise, and multiplication extends the group law bilinearly:
\[
(ab)(g)=\sum_{hk=g}a(h)\,b(k) .
\]
A *zero divisor* is a nonzero \(a\) for which \(ab=0\) for some nonzero \(b\).

The sum defining \((ab)(g)\) is finite, since \(h\) runs over the support of \(a\) and then \(k=h^{-1}g\). Over \(\mathbb F_2=\{0,1\}\) an element is a finite subset of \(G\), and \((ab)(g)\) is the number of expressions \(g=hk\) with \(h\in\operatorname{supp}a\), \(k\in\operatorname{supp}b\), counted modulo \(2\).

**Lemma 1.2** (torsion gives zero divisors). If \(g\in G\) has finite order \(m>1\), then
\[
(1-g)\sum_{i=0}^{m-1}g^i=1-g^m=0
\]
in \(K[G]\), and both factors are nonzero.

*Proof.* Expand the product; the terms \(g,\ldots,g^{m-1}\) cancel in pairs. The first factor is nonzero because \(g\ne1\), and the second because \(1,g,\ldots,g^{m-1}\) are distinct. \(\square\)

A group is *torsion-free* if \(1\) is its only element of finite order.

**Conjecture 1.3** (zero-divisor conjecture). If \(G\) is torsion-free and \(K\) is a field, then \(K[G]\) has no zero divisors.

The conjecture was formulated by Higman in his thesis of 1940 and was posed by Kaplansky as Problem 6 of a conference report in 1957; the introduction of [Gardam 2021] records this history and the related *unit conjecture*, which predicts that every unit of \(K[G]\) is a nonzero multiple of a group element. The unit conjecture implies the zero-divisor conjecture for each group algebra, and Gardam disproved the unit conjecture with an explicit unit in \(\mathbb F_2[P]\) for a torsion-free group \(P\) [Gardam 2021, Theorem A]. Gardam's introduction also lists positive results for the zero-divisor conjecture, for example for elementary amenable groups. A nontrivial unit is not a zero divisor, so [Gardam 2021] does not settle Conjecture 1.3.

## 2. Unique products

**Definition 2.1.** A group \(G\) has the *unique-product property* if for all finite nonempty sets \(P,Q\subseteq G\) some element of \(PQ=\{pq:p\in P,\ q\in Q\}\) has exactly one expression \(pq\) with \(p\in P\) and \(q\in Q\).

**Proposition 2.2.** If \(G\) has the unique-product property, then \(K[G]\) has no zero divisors for any field \(K\).

*Proof.* Let \(a,b\ne0\) and put \(P=\operatorname{supp}a\), \(Q=\operatorname{supp}b\). If \(g=pq\) is a unique product, then \((ab)(g)=a(p)\,b(q)\ne0\). \(\square\)

A group with the unique-product property is torsion-free, by Lemma 1.2 and Proposition 2.2. The converse fails: Rips and Segev constructed torsion-free groups without the unique-product property, and Steenbock gave a treatment of their construction by graphical small cancellation [Steenbock 2015]. Gardam announced that a torsion-free lattice of type \(\widetilde A_2\) with two generators fails the unique-product property; Mian and Siddique proved this with an explicit pair of subsets of \(32\) and \(28\) elements, checked by the Lean proof assistant, taking torsion-freeness from Gardam [Mian–Siddique 2026]. A failure of unique products does not by itself give a zero divisor: over \(\mathbb F_2\) every product coefficient must vanish, which requires *even* numbers of expressions, not merely more than one. The construction of this course arranges these parities by a counting argument.

## 3. The cancellation mechanism

A *signed alphabet* is a finite set \(T\) with a fixed-point-free involution \(t\mapsto\bar t\); the letter \(\bar t\) is the *inverse* of \(t\). A *labelled graph* over \(T\) is a finite graph \(\Gamma\), possibly with several edges between two vertices, in which every edge, read in either direction, carries a letter, with the two directions of an edge carrying inverse letters. An edge read in one direction is an *oriented edge*; its letter is read from its initial to its terminal vertex. For a vertex \(x\) let \(S_x\subseteq T\) be the set of letters of the oriented edges starting at \(x\), the *outgoing letters* of \(x\). The labelled graph is *immersed* if at every vertex the outgoing oriented edges carry distinct letters, so that at \(x\) there is exactly one oriented edge with letter \(t\) for each \(t\in S_x\).

A *path* is a sequence of oriented edges, each starting where the previous one ends; it is *closed* if it ends where it starts. Now let \(G\) be a group and \(\varphi\colon T\to G\) a map with \(\varphi(\bar t)=\varphi(t)^{-1}\). The *label* of a path with letters \(t_1,\ldots,t_k\) is
\[
\varphi(t_1)\varphi(t_2)\cdots\varphi(t_k)\in G,
\]
and the empty path at a vertex has label \(1\).

**Lemma 3.1** (handshakes). In a finite graph in which every vertex has odd degree, a loop at a vertex counting \(2\) towards its degree, every connected component has an even number of vertices.

*Proof.* In a component the sum of the degrees is twice the number of edges, an even number, and a sum of odd numbers is even exactly when it has an even number of terms. \(\square\)

**Proposition 3.2** (zero divisors from two labelled graphs; [OpenAI-KZ, Section 6]). Let \(\Gamma_A\) and \(\Gamma_B\) be connected immersed labelled graphs over \(T\), with vertex sets \(A'\) and \(B'\), and let \(x_A\in A'\), \(x_B\in B'\). Let \(\varphi\colon T\to G\) be as above, and suppose that every closed path in \(\Gamma_A\) or \(\Gamma_B\) has label \(1\). For \(x\in A'\) let \(g_x\) be the label of a path from \(x_A\) to \(x\), and for \(y\in B'\) let \(h_y\) be the label of a path from \(x_B\) to \(y\). Suppose that \(\#(S_x\cap S_y)\) is odd for all \(x\in A'\) and \(y\in B'\). Then the elements
\[
\alpha=\sum_{x\in A'}g_x,\qquad\beta=\sum_{y\in B'}h_y^{-1}
\]
of \(\mathbb F_2[G]\) satisfy \(\alpha\beta=0\). If moreover \(g_x\ne1\) for every \(x\ne x_A\) and \(h_y\ne1\) for every \(y\ne x_B\), then \(\alpha\ne0\) and \(\beta\ne0\).

*Proof.* The labels \(g_x\) and \(h_y\) do not depend on the chosen paths: if \(P\) and \(P'\) are paths from \(x_A\) to \(x\), then \(P\) followed by the reverse of \(P'\) is a closed path, so the label of \(P\) times the inverse of the label of \(P'\) is \(1\). In \(\mathbb F_2[G]\),
\[
\alpha\beta=\sum_{(x,y)\in A'\times B'}g_xh_y^{-1},
\]
where equal group elements are added with coefficients in \(\mathbb F_2\).

Form a graph \(\Theta\) on the vertex set \(A'\times B'\) as follows. A *step* from \((x,y)\) is a letter \(t\in S_x\cap S_y\); it leads to \((x',y')\), where \(x'\) and \(y'\) are the ends of the oriented edges with letter \(t\) starting at \(x\) and at \(y\). The step \(\bar t\) from \((x',y')\) leads back to \((x,y)\), along the same two edges read backwards; call it the reverse step. Steps and their reverse steps come in pairs, and each pair is one edge of \(\Theta\). An edge whose two steps both start at \((x,y)\) is a loop, and it counts \(2\) towards the degree. So the degree of \((x,y)\) is the number of steps from it, \(\#(S_x\cap S_y)\), an odd number. By Lemma 3.1, every component of \(\Theta\) has an even number of vertices. Along an edge of \(\Theta\),
\[
g_{x'}h_{y'}^{-1}=\bigl(g_x\varphi(t)\bigr)\bigl(h_y\varphi(t)\bigr)^{-1}=g_xh_y^{-1},
\]
so \(g_xh_y^{-1}\) is constant on each component. Grouping the sum by components, each component contributes an even multiple of one group element, which is \(0\) in \(\mathbb F_2[G]\). Hence \(\alpha\beta=0\).

Under the additional assumption, \(x_A\) is the only vertex of \(A'\) with \(g_x=1\), so the coefficient of \(1\) in \(\alpha\) is \(1\), and \(\alpha\ne0\); in the same way \(\beta\ne0\). \(\square\)

The proposition needs no assertion about whether two vertices other than the root have equal labels. It reduces the theorem to three tasks: to find graphs whose outgoing letter sets have odd intersections, to find a group in which all closed paths have trivial label while root paths do not, and to make that group torsion-free.

## 4. The theorem and the plan of the course

**Theorem 4.1** (OpenAI [OpenAI-KZ, Theorem 1.1]). There are a finitely presented torsion-free group \(G\) and nonzero elements \(\alpha,\beta\in\mathbb F_2[G]\) with \(\alpha\beta=0\). Moreover, \(G\) has a finite two-dimensional classifying space.

Ivanov extended the theorem to every odd prime \(p\) [Ivanov 2026, Theorem 1.1 and Corollary 1.2]: there is a finitely presented torsion-free group \(G_p\) with a finite two-dimensional classifying space and nonzero \(\alpha,\beta\in\mathbb F_p[G_p]\) with \(\alpha\beta=0\). So the zero-divisor conjecture fails over every field of positive characteristic; over fields of characteristic zero it remains open. His proof replaces the parity cancellation of Proposition 3.2 by a signed cancellation, Exercise 5.6 below, uses the projective plane over \(\mathbb F_{p^3}\) with \(p\) extra letters in place of the alphabet of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md), and keeps the geometric part of the argument of this course [Ivanov 2026, Sections 1.3, 1.4 and 6]. His appendix records a line-by-line check of that part, with six points that deserve a clarifying sentence; the lessons treat each of them explicitly.

Kaplansky's direct-finiteness conjecture fails as well: over a finite field of characteristic two there are a finitely presented group and elements \(a,b\) of its group algebra with \(ab=1\) and \(ba\ne1\), and a torsion-free example over \(\mathbb F_2\) adapts the graph-and-cone method of this course. The course [Kaplansky's direct-finiteness conjecture](course:kaplansky-direct-finiteness/directly-finite-group-algebras) proves the first of these and explains why the group cannot be sofic. Kaplansky's idempotent conjecture, by contrast, holds over every commutative domain of characteristic zero: the group ring of a torsion-free group has no idempotents other than \(0\) and \(1\) ([The Bass trace conjecture for group rings](course:bass-trace-conjecture/traces-of-projective-modules)). An idempotent \(e\ne0,1\) would give zero divisors, as \(e(1-e)=0\), so the zero-divisor conjecture over a field would imply the idempotent conjecture over that field; the proof in characteristic zero goes through traces instead. In the reduced group \(C^*\)-algebra of a torsion-free group, however, there can be projections other than \(0\) and \(1\): the course [A torsion-free counterexample to the Kadison–Kaplansky conjecture](course:kadison-kaplansky-projections/the-conjecture-and-scalar-compression) proves OpenAI's construction of one with trace strictly between \(0\) and \(\frac12\).

The group is built from two labelled graphs \(\Gamma_A,\Gamma_B\) over a signed alphabet \(T\). Let \(F\) be the *rose* over \(T\): one vertex and one loop for each pair \(\{t,\bar t\}\), the loop read in one direction carrying \(t\) and in the other \(\bar t\). An immersed labelled graph maps to \(F\) by sending every vertex to the vertex and every edge to the loop with its letters. Attach to \(F\), along this map, a cone on each component of \(\Gamma_A\) and of \(\Gamma_B\), and let \(G\) be the fundamental group of the resulting two-dimensional complex \(X\). In \(G\), the label of every closed path in the graphs is trivial, since the path is null-homotopic in its cone. Proposition 3.2 then needs two safeguards:

1. *Root separation:* every path from \(x_A\) or \(x_B\) to a different vertex of its graph has a nontrivial label in \(G\).
2. *Torsion-freeness:* \(G\) is torsion-free. This follows from the asphericity of \(X\), that is, \(\pi_2(X)=0\).

Both follow from the absence of certain planar configurations of paths in the graphs. The graphs are chosen at random, with prescribed outgoing letter sets that have odd intersections and with a decay estimate for the frequencies of words, and the configurations are excluded with high probability. The lessons are:

1. This lesson.
2. [Projective planes and prescribed types](projective-planes-and-prescribed-types.md): the alphabet from a finite projective plane, the prescribed outgoing letter sets with odd intersections, turn weights and a decay estimate for squared word weights.
3. [Random matchings with large girth](random-matchings-with-large-girth.md): the random graphs, conditioning on large girth by switchings, the probability of prescribed edges, and a bound on diameters.
4. [Image graphs and multiplicity stages](image-graphs-and-multiplicity-stages.md), [Aligned blocks and word counts](aligned-blocks-and-word-counts.md) and [The bounded-pattern estimate](the-bounded-pattern-estimate.md): with high probability no system of a bounded number of paths of total length comparable to \(\log n\) is almost completely paired by comparisons of its words.
5. [Spherical arrangements and planar intervals](spherical-arrangements-and-planar-intervals.md) and [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md): every planar pairing configuration on a sphere, of any size, contains such a bounded system.
6. [Cone pictures and asphericity](cone-pictures-and-asphericity.md): a failure of asphericity or of root separation would give such a planar configuration.
7. [Torsion-freeness and the zero divisors](torsion-freeness-and-the-zero-divisors.md): the group is torsion-free, and Theorem 4.1 follows.

## 5. Exercises

**5.1.** Let \(G=\mathbb Z\), written multiplicatively with generator \(z\). Show directly that \(\mathbb F_2[G]\) has no zero divisors, by looking at the largest powers of \(z\) in the supports.

**5.2.** Show that \(\mathbb Z^d\) has the unique-product property. *Hint.* Order \(\mathbb Z^d\) lexicographically.

**5.3.** Show that if every vertex of \(\Gamma_A\) and of \(\Gamma_B\) has a set of outgoing letters closed under \(t\mapsto\bar t\), for instance if both graphs have a single vertex, then every \(\#(S_x\cap S_y)\) is even, so Proposition 3.2 cannot apply.

**5.4.** Show directly from Definition 2.1 that a group with an element of finite order larger than one does not have the unique-product property.

**5.5.** Show that over \(\mathbb F_2\), if \(G\) is torsion-free and \(\alpha\beta=0\) with \(\alpha,\beta\ne0\), then \(\operatorname{supp}\alpha\) and \(\operatorname{supp}\beta\) each have at least two elements.

**5.6** (signed cancellation; [Ivanov 2026, Lemma 2.2]). In the situation of Proposition 3.2, drop the parity assumption and let \(p\) be a prime. Suppose that \(\Gamma_A\) is bipartite, with a sign \(\epsilon\colon A'\to\{\pm1\}\) that changes along every edge, and that \(\#(S_x\cap S_y)\equiv d\pmod p\) for all \(x\in A'\), \(y\in B'\), with \(p\nmid d\). Show that \(\alpha=\sum_{x\in A'}\epsilon(x)g_x\) and \(\beta=\sum_{y\in B'}h_y^{-1}\) satisfy \(\alpha\beta=0\) in \(\mathbb F_p[G]\).

## 6. Solutions

**5.1.** Let \(a,b\ne0\) with largest exponents \(m\) and \(m'\) in their supports. The coefficient of \(z^{m+m'}\) in \(ab\) comes only from \(z^m\cdot z^{m'}\), so it is \(1\).

**5.2.** For finite nonempty \(P,Q\subseteq\mathbb Z^d\), let \(p\) and \(q\) be the lexicographically largest elements. If \(p'+q'=p+q\) with \(p'\in P\), \(q'\in Q\), then \(p'\le p\) and \(q'\le q\); the lexicographic order is compatible with addition, so \(p'+q'\le p+q\) with equality only if \(p'=p\) and \(q'=q\).

**5.3.** If \(S_x\) and \(S_y\) are closed under \(t\mapsto\bar t\), so is \(S_x\cap S_y\). The involution has no fixed points, so it splits \(S_x\cap S_y\) into pairs \(\{t,\bar t\}\), and the number of elements is even. At a single vertex every edge is a loop, which contributes both \(t\) and \(\bar t\) to the outgoing letters.

**5.4.** Let \(g\) have order \(m>1\) and take \(P=Q=\{1,g,\ldots,g^{m-1}\}\), a subgroup. Then \(PQ=P\), and every element \(g^k\) of it has the \(m\ge2\) expressions \(g^i\cdot g^{k-i}\), \(0\le i<m\). So no element of \(PQ\) has a unique expression.

**5.5.** If \(\operatorname{supp}\alpha=\{g\}\), then \(\alpha=g\) is a unit, with inverse \(g^{-1}\), and \(\alpha\beta=0\) gives \(\beta=g^{-1}\alpha\beta=0\). The same argument applies to \(\beta\).

**5.6.** As in the proof of Proposition 3.2, \(\alpha\beta=\sum_{(x,y)}\epsilon(x)g_xh_y^{-1}\), and \(g_xh_y^{-1}\) is constant on every component \(C\) of \(\Theta\); so it suffices that \(\sum_{(x,y)\in C}\epsilon(x)\equiv0\pmod p\). An edge of \(\Theta\) joins \((x,y)\) to \((x',y')\) with \(x,x'\) adjacent in \(\Gamma_A\), so \(\epsilon(x')=-\epsilon(x)\), and \(\Theta\) has no loops. Summing \(\epsilon\) over the two ends of every edge gives \(\sum_{(x,y)\in C}\epsilon(x)\deg(x,y)=0\). Since \(\deg(x,y)=\#(S_x\cap S_y)\equiv d\), this gives \(d\sum_{(x,y)\in C}\epsilon(x)\equiv0\), and \(p\nmid d\).

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
- [OpenAI-KZ-Lean] OpenAI, Lean formalization of the counterexample to Kaplansky's zero-divisor conjecture, OpenAI Math Release, scope note `lean/docs/196.md`. https://github.com/openai/math/blob/main/lean/docs/196.md
- [Gardam 2021] G. Gardam, *A counterexample to the unit conjecture for group rings*, Ann. of Math. 194 (2021), 967–979. https://arxiv.org/abs/2102.11818
- [Steenbock 2015] M. Steenbock, *Rips–Segev torsion-free groups without the unique product property*, J. Algebra 438 (2015), 337–378. https://arxiv.org/abs/1307.0981
- [Ivanov 2026] S. V. Ivanov, *Zero divisors in group algebras of torsion-free groups in odd characteristic*, arXiv:2610.17662, 13 October 2026. https://arxiv.org/abs/2610.17662
- [Mian–Siddique 2026] I. Mian and S. Siddique, *A machine-checked proof that Gardam's \(\widetilde A_2\) lattice does not have unique products*, arXiv:2609.22380, September 2026. https://arxiv.org/abs/2609.22380
