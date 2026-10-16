# The private completion and the graphical group

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The covering graph of the pruned tower, with its sampled voltages, is now turned into a group. First a *private completion* adds long paths and two loops, each edge with its own new letter, so that the covering graph becomes connected while its local girth and the uniqueness of long words survive. Then the labels of all closed walks of the covering graph are imposed as relators. The group \(\Gamma\) obtained in this way contains the covering graph as an embedded subgraph of its Cayley graph, and its deck group \(\mathsf H\) as a subgroup; the translates of the embedded copy are the *sheets* used in the rest of the course. The proof is a curvature argument on a minimal diagram: coincident projected edges can be cancelled, all other boundary arcs are short by the uniqueness of long words, so every face has at least seven arcs, which Euler's formula forbids [OpenAI-BCI, Sections 6.1-6.4, Lemmas 6.1-6.3, Proposition 6.4].

- Conventions and inputs (Section 1).
- The private completion (Section 2).
- The graphical group and its diagrams (Section 3).
- Null-labelled paths close (Section 4).
- The graphical realization (Section 5).

The method goes back to Gromov's graphical small cancellation, as expounded by Ollivier [Oll] and developed by Gruber [Gru]; the form here, with a varying scale, bridges and private letters, is proved in full below, using the statements (VK) on van Kampen diagrams and (MAP) on plane maps, as stated in Section 3 of [Graphical presentations and coned diagrams](course:irrational-trace-and-baum-connes/graphical-presentations-and-coned-diagrams#3-diagrams) and proved in the course [Van Kampen diagrams](course:van-kampen-diagrams/van-kampens-lemma).

## 1. Conventions and inputs

An edge of a labelled graph has a positive orientation and one formal letter; traversing it backwards reads the inverse letter. A labelling is *folded* if at each vertex each signed letter is read on at most one outgoing edge end. In a folded graph a path is determined by its initial vertex and its word. Words are read in traversal order. The *formal right Cayley graph* of a group \(\Gamma\) with alphabet \(S\) has one positive edge \((g,\sigma):g\to g\sigma\) for every \(g\in\Gamma\) and \(\sigma\in S\); these are distinct cells even when their endpoints coincide with those of another edge. Left translation by elements of \(\Gamma\) preserves all labelled oriented cells. A path is *immersed* if it has no immediate reversal; in a folded graph this means that its word is freely reduced.

Write \(X_{\rm o}\) for the pruned old graph with its refined alphabet \(S_{\rm o}\) and voltages \(h_e\in\mathsf H\) on positive edges, \(h_{\bar e}=h_e^{-1}\), chosen by Proposition 1.1 of [Polynomial avoidance, norm tests and moments](polynomial-avoidance-norm-tests-and-moments.md). Throughout this lesson and the next three,
\[
\begin{gathered}
a=\frac b{\log_2q}\le10^{-6},\\
L=1.003,\qquad m_{\min}\ge10^6 ,
\end{gathered}
\]
and the *scale* of an old vertex of height \(i\) is \(m(v)=m_i\). The inputs from the preceding lessons are:

1. \(X_{\rm o}\) is countable, folded and locally finite, of maximum degree at most \(K_{b,\epsilon}D\); its edges join equal or consecutive heights, so \(|m(v)-m(w)|\le a\) on every edge.
2. If an immersed old path starts at \(v\) and its word has two different occurrences in \(X_{\rm o}\), its length is less than \(Lm(v)\). This applies to either occurrence and to the reversed paths.
3. In the covering graph of \(X_{\rm o}\), every simple cycle \(C\) satisfies \(|C|>6.03\,m(v)\) at every vertex \(v\) of \(C\).

The second statement is Proposition 5.1(4) of [Auxiliary incidences, deletions and recovery](auxiliary-incidences-deletions-and-recovery.md), kept under deletion and refinement of labels: a word of length at least \(\lceil1.002m(v)\rceil\) occurs only once, and \(\lceil1.002m\rceil<1.003m\) for \(m\ge10^6\). The third is Proposition 1.1(1) of the lesson on polynomial avoidance, since a simple cycle is cyclically reduced.

## 2. The private completion

**Lemma 2.1** (private completion; [OpenAI-BCI, Lemma 6.1]). There are a connected, countable, folded labelled graph \(X\) containing \(X_{\rm o}\) as its *old* subgraph and an extension of the voltages to \(X\) with the following properties.

1. Each added edge has its own new positive letter, used on no other edge. Every new vertex has degree two and only new incident edges. The maximum degree is at most \(K_{b,\epsilon}D+6\).
2. The scale \(m\) extends to the new vertices, stays at least \(m_{\min}\), and satisfies \(|m(v)-m(w)|\le a\) on every edge.
3. The covering graph \(\widetilde X\), with edges \((v,h)\to(w,hh_e)\) over \(e:v\to w\), is connected, and its deck group is \(\mathsf H\) acting by \(f\cdot(v,h)=(v,fh)\).
4. Every simple cycle \(C\) of \(\widetilde X\) satisfies \(|C|>6.03m(v)\) at every vertex \(v\) of \(C\).
5. If two paths in \(\widetilde X\) have the same word and their projections to \(X\) differ, neither contains a new (*private*) edge; if moreover they are immersed and start at \(v,w\), their common length is less than both \(Lm(v)\) and \(Lm(w)\).

The scale on \(\widetilde X\) is the pull-back of the scale on \(X\).

*Proof.* Choose an old vertex in each component of \(X_{\rm o}\), enumerate the components, and join the chosen vertices in a chain (finite if there are finitely many components) by new subdivided paths. For a joining path with endpoints \(v,w\), choose its number \(n\) of edges with
\[
\begin{aligned}
n&\ge20\,m(v),\\
n&\ge20\,m(w),\\
n&\ge\frac{|m(v)-m(w)|}a,
\end{aligned}\tag{2.1}
\]
interpolate \(m\) linearly along it, and give its edges the identity voltage. At one old vertex \(v_*\) attach two subdivided loops, each with at least \(20m(v_*)\) edges and \(m=m(v_*)\) on their new vertices, with voltages whose ordered products along the loops are \(x\) and \(y\): for instance the identity on all edges but one, traversed positively, which carries \(x\), respectively \(y\). Every new edge gets a new letter, which keeps the labelling folded. The chain adds at most two edge ends at an old vertex and the loops four at \(v_*\); the new vertices have degree two. This proves (1) and (2).

The completed base graph is connected. A path from \(v_*\) to a vertex \(v\) has some voltage \(h_0\); preceding it by loops at \(v_*\) multiplies its voltage on the left by any word in \(x,y\), hence by any element of \(\mathsf H\), so every lift \((v,h)\) is reached from \((v_*,1)\). The left action is free on vertices and transitive on fibers, which gives (3).

A simple cycle of \(\widetilde X\) that uses a private edge must traverse the whole lift of a joining path or of a loop, because private interior vertices have degree two. Let \(v\) be an old endpoint of that lifted path and \(\ell\) the length of the cycle. Then \(\ell\ge20m(v)\), and every vertex \(w\) of the cycle has \(m(w)\le m(v)+a\ell\), so
\[
\begin{aligned}
6.03\,m(w)&\le6.03\Bigl(\frac1{20}+a\Bigr)\ell\\
&<0.302\,\ell<\ell .
\end{aligned}
\]
A simple cycle using only old edges satisfies (4) by input 3. In particular \(\widetilde X\) has no loops and no cycles of length two.

A private letter in a common word identifies its unique base edge, and foldedness then propagates the equality of the two projected paths forwards and backwards from that edge, even for paths that are not immersed. So two occurrences with different projections contain no private edge; if they are immersed they consist of old edges, and input 2 gives the bound at both initial vertices, and at the terminal vertices for the reversed paths. \(\square\)

**Two consequences.** Every nonempty cyclically immersed closed walk \(W\) of \(\widetilde X\) based at \(v\), simple or not, satisfies
\[
|W|>\frac{6.03}{1+6.03a}\,m(v) .\tag{2.2}
\]
Indeed its support is not a tree, so it contains a simple cycle, through a vertex \(w\) at distance at most \(|W|\) from \(v\); then \(|W|>6.03m(w)\ge6.03(m(v)-a|W|)\). Next, if \(j\) immersed *comparison paths* follow each other, each of length less than \(Lm\) at its own initial point, their total length is at most
\[
L\sum_{t=0}^{j-1}(1+La)^t\,m(v) ,\tag{2.3}
\]
by induction, since the \(t\)-th path starts at distance at most \(L\sum_{u<t}(1+La)^um(v)\) from \(v\), where \(m\le(1+La)^tm(v)\). For \(a\le10^{-6}\),
\[
\begin{gathered}
L\sum_{t=0}^2(1+La)^t\\
<3.009004<3.014,\\
L\sum_{t=0}^5(1+La)^t\\
<6.018016<\frac{6.03}{1+6.03a}.
\end{gathered}\tag{2.4}
\]

## 3. The graphical group and its diagrams

Let \(S=S_{\rm o}\sqcup S_{\rm p}\), with \(S_{\rm p}\) the countable private alphabet, write \(\operatorname{lab}(C)\) for the word read along an oriented path \(C\), and define
\[
\begin{gathered}
\Gamma=\bigl\langle S\bigm|\operatorname{lab}(C)=1\\
\text{for every finite closed}\\
\text{walk }C\text{ of }\widetilde X\bigr\rangle .
\end{gathered}\tag{3.1}
\]
The set of relators is closed under inversion and cyclic permutation, since reversed and rotated closed walks are closed walks. Each relator occurrence below keeps an actual closed walk reading it, its *source walk*; two occurrences of the same word may have different source walks.

A *diagram* for a word \(w\), in the sense of (VK), is a finite connected plane graph with oriented labelled edges and a base vertex on the boundary of the unbounded face, whose unbounded face reads \(w\) and whose bounded faces read relators. Here every bounded face is also given a source walk in \(\widetilde X\) reading its boundary walk. The *perimeter* of a face counts edge sides, so a bridge inside a face counts twice; the *filling cost* is the sum of the perimeters of the bounded faces. A one-vertex graph without edges is allowed.

**Lemma 3.1** (diagrams for the graphical presentation). If a finite word \(w\) is trivial in \(\Gamma\), it has a diagram. Conversely, the word of the unbounded face of a diagram is, in the free group, a product of conjugates of the words of its bounded faces, one for each face; so every closed walk in a diagram reads a word trivial in \(\Gamma\), and the labelled one-skeleton of a diagram has a unique label-preserving map to the formal Cayley graph sending a chosen vertex to a chosen element.

*Proof.* This is (VK)(1)-(3), that is, Theorems 3.1, 4.1 and 5.1 of [Van Kampen's lemma](course:van-kampen-diagrams/van-kampens-lemma), with source walks attached to the faces: a face reads a relator, that is, the label of a closed walk of \(\widetilde X\), possibly rotated or reversed, and the rotated or reversed walk reads it. That every closed walk in a diagram reads a word trivial in \(\Gamma\) is Theorem 5.1 there; the label-preserving map from a chosen vertex follows by Lemma 4.3 of [Words, free groups and Cayley graphs](course:van-kampen-diagrams/words-free-groups-and-cayley-graphs). \(\square\)

From (MAP), that is, Propositions 2.1 and 2.2 of [Plane maps](course:van-kampen-diagrams/plane-maps), we use: an edge has the same face on both sides if and only if it is a bridge; removing a bridge separates the graph into two components; and between its two traversals the boundary walk of the face runs along the boundary walk of one of the components.

## 4. Null-labelled paths close

**Lemma 4.1** (closure of a null-labelled source path; [OpenAI-BCI, Lemma 6.3]). A path in \(\widetilde X\) whose word is trivial in \(\Gamma\) has equal initial and terminal vertices.

*Proof.* Suppose not. Among all such source paths with distinct endpoints, and all diagrams for their words, minimize first the filling cost \(c\), then the length of the path, and then the number of edges of the diagram; all are nonnegative integers. The boundary walk of the unbounded face is the given path, read from the base vertex, the *marked join*. The minimal counterexample is chosen globally, among all paths; this is used in the bridge step.

*Faces and the exterior path are reduced.* Each bounded face may be assumed to have a nonempty, cyclically immersed source walk. Indeed, in the free-group expression of Lemma 3.1, foldedness turns a free cancellation in a source walk into an actual edge reversal: a freely trivial face word can be omitted from the expression, and otherwise its backtracks and its cyclic conjugating tail can be deleted, the tail being absorbed into the conjugator. The remaining word is read on a closed source walk of smaller perimeter, and Lemma 3.1 gives a diagram for the unchanged exterior word with smaller filling cost. In the same way the exterior source path is immersed: deleting a backtrack keeps its endpoints, does not increase the least filling cost and shortens it.

*Coincident projections are excluded.* For an edge of the diagram incident to a bounded face, compare its two source occurrences, oriented to read the same letter.

First, if two different bounded faces project their common edge to the same edge of \(X\), a unique deck transformation aligns the two lifted edges. Delete this edge of the diagram; it is not a bridge, so the graph stays connected and the two faces merge. Splice their aligned closed source walks, omitting the two opposite traversals of the edge: the new source walk is closed, and its perimeter is the sum of the two minus two. Other shared edges may now occur twice on the new boundary walk. The new diagram has smaller filling cost, a contradiction.

Second, suppose an edge has the same bounded face \(F\) on both sides; it is a bridge. The unbounded face, with its marked join, lies on one side of it; let \(D_1\) be the other component after deleting the bridge. In the source walk of \(F\), the excursion into \(D_1\) is a subpath \(\chi\) reading the bridge, the boundary walk of \(D_1\) and the reverse bridge. All bounded faces of \(D_1\) are former faces other than \(F\), so Lemma 3.1 shows that \(\operatorname{lab}(\chi)\) is trivial in \(\Gamma\), with a filling of cost less than \(c\), since the positive perimeter of \(F\) is missing. If the endpoints of \(\chi\) differed, \(\chi\) would be a counterexample of smaller filling cost; so they agree. Delete this excursion from the source walk of \(F\), the bridge and \(D_1\): the source walk of \(F\) still closes, the exterior path is unchanged, and the filling cost drops by at least the two bridge sides. This is impossible. The two projected occurrences of the bridge need not coincide for this argument.

Third, if a bounded face and the exterior path project their common edge to the same edge of \(X\), align their lifts by a deck transformation. Replace this step of the exterior path by the complementary path of the face, oriented to have the same lifted endpoints, and delete the shared edge, absorbing the face into the unbounded face. The endpoints of the exterior path stay distinct, and the filling cost drops. Again a contradiction.

*Arcs.* Keep the marked join and suppress all other vertices of degree two. There is no other vertex of degree one: it would force an immediate reversal in a cyclically immersed face walk or in the immersed exterior path. The resulting edges, the *arcs*, have constant face incidences and constant exterior incidence along their interiors. An arc incident to a bounded face reads an immersed word on both of its occurrences, and by the preceding step their projections differ; by Lemma 2.1(5) its length is less than \(Lm\) at the initial point of either occurrence.

Every bounded face has at least seven arc incidences: otherwise its nonempty cyclically immersed closed source walk would be a concatenation of at most six comparison paths, of total length less than \(6.018016\,m(v)\) by (2.3) and (2.4), contradicting (2.2).

If there were no bounded face, the diagram would be a tree; a nonempty finite tree has at least two leaves, while only the marked join may have degree one, and the empty diagram has the empty word, whose path has equal endpoints. So there is a bounded face. Let \(V,E,F\) be the numbers of vertices, edges and faces (including the unbounded one) of the compressed graph; suppression is defined also for a single cycle, because the marked join is kept. By Euler's formula \(V-E+F=2\) and \(2E=\sum_v\deg(v)\),
\[
\begin{gathered}
6F-2E\\
=12+2\sum_v(\deg(v)-3)\\
\ge8 ,
\end{gathered}\tag{4.1}
\]
since only the marked join may have degree below three, and it has degree at least one. On the other hand \(\sum_f\deg(f)=2E\), so \(6F-2E=\sum_f(6-\deg(f))\); each bounded face contributes at most \(-1\), and the unbounded face at most \(6\). The sum is less than \(8\), a contradiction. \(\square\)

The marked join is the reason for the constant \(8\) instead of \(12\).

## 5. The graphical realization

**Proposition 5.1** (graphical realization; [OpenAI-BCI, Proposition 6.4]). There is an injective map \(j:\widetilde X\to\operatorname{Cay}(\Gamma,S)\) on vertices and on formal oriented edges, preserving labels and sending \((v_*,1)\) to the identity. The elements over \(v_*\) define an injective homomorphism \(\phi:\mathsf H\to\Gamma\), \(\phi(f)=j(v_*,f)\), and with \(t_v=j(v,1)\),
\[
j(v,h)=\phi(h)\,t_v .\tag{5.1}
\]
Every label-preserving automorphism of \(\widetilde X\) is a deck transformation. Consequently the distinct translates \(gj(\widetilde X)\), the *sheets*, are indexed by \(\Gamma/\phi(\mathsf H)\), and the stabilizer of \(gj(\widetilde X)\) under left translation is \(g\phi(\mathsf H)g^{-1}\).

*Proof.* Send a vertex of \(\widetilde X\) to the element represented by the word of any path from \((v_*,1)\) to it. Two such paths differ by a closed walk, whose word is a relator, so this is well defined. If two vertices have the same image, a path between them has a word trivial in \(\Gamma\), and Lemma 4.1 shows that they are equal. Edges with the same image have the same initial image and the same signed letter; their initial vertices agree by injectivity, and the edges by foldedness.

A path from \((v_*,1)\) to \((v_*,f_1)\), followed by the deck translate by \(f_1\) of a path from \((v_*,1)\) to \((v_*,f_2)\), ends at \((v_*,f_1f_2)\) and reads the product of the two words; so \(\phi(f_1f_2)=\phi(f_1)\phi(f_2)\), and \(\phi\) is injective because \(j\) is. In the same way, following a path to \((v_*,h)\) and then the translate by \(h\) of a path to \((v,1)\) gives (5.1); more generally \(j(fu)=\phi(f)j(u)\) for \(u\in\widetilde X\).

Fix a private positive base edge; its letter appears on no other base edge. A label-preserving automorphism of \(\widetilde X\) sends a chosen lift of this edge to a lift of the same base edge; composing with a deck transformation, it fixes the initial vertex of that lift. An automorphism of a connected folded labelled graph fixing one vertex fixes every path from it, hence everything. So every automorphism is a deck transformation. If a left translation by \(g\) preserves \(j(\widetilde X)\), its restriction, transported by \(j\), is a label-preserving automorphism of \(\widetilde X\), hence multiplication by some \(f\); evaluating at \((v_*,1)\) gives \(g=\phi(f)\). Conversely every \(\phi(f)\) preserves the image by (5.1). The remaining assertions follow by conjugation and translation. \(\square\)

From now on \(\mathsf H\) is identified with \(\phi(\mathsf H)\le\Gamma\). Each sheet carries its *source* vertices and edges and its scale \(m_Q\), independent of the representative \(g\) of its coset: changing \(g\) within \(g\mathsf H\) changes the parametrization of the source vertices and edges by a deck transformation, which preserves base vertices and scales. Two source-parametrized sheet maps that agree at one source vertex after deck alignment agree everywhere, by connectedness and label propagation. So two different sheets meeting at a vertex never have the same projected base vertex there, and a common nonconstant path of two different sheets always has different projected occurrences. This does not exclude isolated contacts at private vertices.

## 6. Exercises

**Exercise 6.1.** Show that without the two loops at \(v_*\) the covering graph of the completed graph need not be connected, and identify its components.

**Exercise 6.2.** Verify the numbers in (2.4): compute \(L(1+(1+La)+(1+La)^2)\) and \(6.03/(1+6.03a)\) for \(a=10^{-6}\).

**Exercise 6.3.** In the proof of Lemma 4.1, where is it used that a private edge is never part of a comparison arc?

**Exercise 6.4.** Show that in (4.1) the inequality \(\ge8\) can be an equality, and explain why the argument still works.

## 7. Solutions

**6.1.** Without the loops, a closed base walk at \(v_*\) has holonomy in the subgroup \(\mathsf H_0\) generated by the holonomies of closed walks of the old graph and of the chain, which may be proper; the component of \((v_*,1)\) then contains only the lifts \((v,h)\) with \(h\in\mathsf H_0h_v\), and the components correspond to the cosets \(\mathsf H_0\backslash\mathsf H\). The loops force \(\mathsf H_0=\mathsf H\).

**6.2.** \(La=1.003\cdot10^{-6}\); \(L(3+3La+(La)^2)\) equals \(3.009+3.018\cdot10^{-6}+\ldots\), which is less than \(3.009004\). For six terms, \(L(6+15La+\ldots)\) equals \(6.018+1.509\cdot10^{-5}+\ldots\), which is less than \(6.018016\). And \(6.03/(1+6.03\cdot10^{-6})=6.0299636\ldots\).

**6.3.** In the step on arcs: an arc incident to a bounded face has two occurrences with different projections, and Lemma 2.1(5) says such occurrences contain no private edge, so their length bound comes from the old uniqueness of long words; a private edge would make the two projections equal.

**6.4.** Equality holds when every vertex other than the marked join has degree three and the join has degree one. The contradiction comes from the other side: \(\sum_f(6-\deg f)\le6-1=5<8\) whenever a bounded face exists, so even equality in (4.1) is impossible.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 6.1-6.4, Lemmas 6.1-6.3, Proposition 6.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
- [Oll] Y. Ollivier, *On a small cancellation theorem of Gromov*, Bull. Belg. Math. Soc. 13 (2006), Sections 2-3; arXiv:math/0310022. https://arxiv.org/abs/math/0310022
- [Gru] D. Gruber, *Groups with graphical C(6) and C(7) small cancellation presentations*, Trans. Amer. Math. Soc. 367 (2015), Definition 1.3 and Lemma 4.1; arXiv:1210.0178. https://arxiv.org/abs/1210.0178
