# Second out-neighborhoods and minimal counterexamples

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In a directed graph, a vertex \(v\) reaches its out-neighbors in one step and some further vertices in two steps. Seymour's second neighborhood conjecture asserts that in every finite oriented graph some vertex reaches at least as many new vertices in the second step as in the first. For tournaments the statement was posed by Dean and Latka and proved by Fisher; Havet and Thomassé gave a second proof by median orders. For general oriented graphs, Chen, Shen and Yuster proved that some vertex satisfies \(|N_2^+(v)|\ge\gamma|N_1^+(v)|\) with \(\gamma\approx0.657\), and Huang and Peng improved the constant [HP]; Kaneko and Locke settled the case of minimum out-degree at most \(6\), and Sadhukhan, Sandeep and Sen the case of minimum out-degree \(7\) [SSS]. Seacrest studied the same inequality for sets of vertices and for arc-weighted graphs [Sea19, Sea12], and Sullivan collected the related questions around the Caccetta–Häggkvist conjecture [Sul]. This course presents OpenAI's proof of the full conjecture [OpenAI-SN]:

**Theorem** (OpenAI 2026; Theorem 3.1 of [The extremal argument and its consequences](the-extremal-argument-and-its-consequences.md)). Every nonempty finite oriented graph has a vertex \(v\) with \(|N_1^+(v)|\le|N_2^+(v)|\).

The proof has three parts. This lesson shows that a counterexample with the fewest vertices, and then the fewest arcs, satisfies a strict inequality for every nonempty proper set of vertices (Proposition 3.3); the arc-deletion argument adapts the proof of Seacrest's Lemma 4 [Sea19]. [Blowing up by transitive tournaments](blowing-up-by-transitive-tournaments.md) replaces each vertex by a large transitive tournament and obtains a graph whose image operator grows in a strictly concave way on every nonempty proper set. [Ranks, matchings and pruning](ranks-matchings-and-pruning.md) proves a deletion bound for two families of ordered pairs by linear algebra over generic coefficients, and [The extremal argument and its consequences](the-extremal-argument-and-its-consequences.md) uses that bound to show that strictly concave growth is impossible. The last lesson also derives the weighted forms of the conjecture and its consequences for directed triangles.

## 1. Oriented graphs and their neighborhoods

An *oriented graph* \(D\) consists of a finite vertex set \(V(D)\) and a set \(A(D)\) of *arcs*, which are ordered pairs \((x,y)\) of distinct vertices, such that \((x,y)\) and \((y,x)\) are never both arcs. We write \(x\to y\) when \((x,y)\in A(D)\). Thus an oriented graph has no loops and no pair of opposite arcs; a *tournament* is an oriented graph in which every pair of distinct vertices is joined by an arc in one direction.

For a set \(S\subseteq V(D)\), the *image* of \(S\) is
\[
F(S)=F_D(S)=\{y\in V(D):x\to y\text{ for some }x\in S\},
\]
and \(F^2(S)=F(F(S))\) is the set of endpoints of directed walks of length two starting in \(S\). The image operator is monotone, \(F(S\cup T)=F(S)\cup F(T)\), and \(F(\varnothing)=\varnothing\). Note that \(F(S)\) may meet \(S\).

For a vertex \(v\), the *first out-neighborhood* is \(N_1^+(v)=F(\{v\})\), and the *second out-neighborhood* \(N_2^+(v)\) is the set of vertices at directed distance exactly two from \(v\): the vertices \(w\ne v\) with \(w\notin N_1^+(v)\) for which some \(u\) satisfies \(v\to u\to w\). The *out-degree* and *in-degree* of \(v\) are \(d^+(v)=|N_1^+(v)|\) and \(d^-(v)=|\{u:u\to v\}|\). A vertex with out-degree \(0\) is a *sink*.

**Lemma 1.1.** In an oriented graph, \(v\notin F^2(\{v\})\) for every vertex \(v\), and therefore
\[
N_2^+(v)=F^2(\{v\})\setminus F(\{v\}).
\]

*Proof.* A walk \(v\to u\to v\) would make both \((v,u)\) and \((u,v)\) arcs. Hence the condition \(w\ne v\) in the definition of \(N_2^+(v)\) is automatic for \(w\in F^2(\{v\})\). \(\square\)

**Example 1.2.** (a) A sink \(v\) satisfies \(|N_1^+(v)|=0\le|N_2^+(v)|\). In particular, every oriented graph with a sink satisfies the conclusion of the theorem, and so does every transitive tournament, whose last vertex is a sink.

(b) In the directed cycle on \(\mathbb Z/k\), \(k\ge3\), with arcs \(x\to x+1\), every vertex has \(N_1^+(x)=\{x+1\}\) and \(N_2^+(x)=\{x+2\}\), so equality holds everywhere.

(c) In the tournament on \(\mathbb Z/7\) with \(x\to x+a\) for \(a\in\{1,2,4\}\), every vertex has out-degree \(3\). From \(0\), the walks of length two end in \(\{2,3,5,4,6,1\}\), so \(N_2^+(0)=\{3,5,6\}\) and again equality holds. Equality at every vertex is therefore possible in a graph without sinks.

(d) The hypothesis that \(D\) has no pair of opposite arcs cannot be dropped. In the complete directed graph on \(n\ge2\) vertices with both arcs between every pair, every vertex reaches all others in one step, so \(|N_1^+(v)|=n-1\) and \(N_2^+(v)=\varnothing\).

## 2. Minimal counterexamples

Call a nonempty oriented graph \(D\) a *counterexample* if \(|N_1^+(v)|>|N_2^+(v)|\) for every \(v\in V(D)\). A *minimal counterexample* is a counterexample with the fewest vertices among all counterexamples, and with the fewest arcs among the counterexamples with that number of vertices. If a counterexample exists, a minimal one exists, because the numbers of vertices and arcs are nonnegative integers.

A set \(C\subseteq V(D)\) is *closed* if \(F(C)\subseteq C\), that is, no arc leaves \(C\). The induced oriented graph \(D[C]\) has vertex set \(C\) and the arcs of \(D\) with both ends in \(C\).

**Lemma 2.1.** If \(C\subseteq V(D)\) is closed and \(v\in C\), then \(v\) has the same first and second out-neighborhoods in \(D[C]\) as in \(D\).

*Proof.* Every out-neighbor of \(v\) lies in \(F(C)\subseteq C\), so \(N_1^+(v)\) is the same in both graphs. Every walk \(v\to u\to w\) in \(D\) has \(u\in C\) and then \(w\in C\), so it is a walk in \(D[C]\); conversely every walk in \(D[C]\) is a walk in \(D\). Hence the sets \(F^2(\{v\})\) agree as well, and Lemma 1.1 gives the claim for \(N_2^+(v)\). \(\square\)

A digraph is *strongly connected* if every vertex can be reached from every other vertex by a directed walk. Write \(x\leadsto y\) if \(y\) can be reached from \(x\) by a directed walk, possibly of length zero. The *strong components* are the classes of the equivalence relation "\(x\leadsto y\) and \(y\leadsto x\)".

**Lemma 2.2.** Every nonempty finite oriented graph has a closed strong component.

*Proof.* Start with any component \(K_0\). If \(K_i\) is not closed, there is an arc from \(K_i\) to a vertex of another component \(K_{i+1}\). Every vertex of \(K_{i+1}\) is then reachable from every vertex of \(K_0,\dots,K_i\). The components \(K_0,K_1,\dots\) are pairwise distinct: if \(K_{i+1}=K_j\) with \(j\le i\), then every vertex of \(K_i\) would be reachable from \(K_{i+1}=K_j\), which is reachable from \(K_i\), so \(K_i\) and \(K_{i+1}\) would be one component. As there are finitely many components, the sequence stops at a closed component. \(\square\)

**Lemma 2.3.** A minimal counterexample \(D\) has at least two vertices, is strongly connected, and every vertex of \(D\) has an in-neighbor.

*Proof.* By Example 1.2(a), \(D\) has no sink; a graph with one vertex consists of a sink, so \(|V(D)|\ge2\). Let \(C\) be a closed strong component (Lemma 2.2). By Lemma 2.1, every vertex of \(D[C]\) has the same neighborhoods as in \(D\), so \(D[C]\) is a counterexample. If \(C\ne V(D)\), it has fewer vertices than \(D\), which is impossible; hence \(C=V(D)\) and \(D\) is strongly connected. Finally, a vertex \(v\) is reached by a walk from another vertex, and the last arc of such a walk enters \(v\). \(\square\)

## 3. The subset deficit

For a minimal counterexample, the defining inequality \(|N_1^+(v)|>|N_2^+(v)|\) for single vertices propagates to all nonempty proper sets of vertices. The tool is arc deletion: deleting arcs produces a graph with fewer arcs, which therefore is not a counterexample, and the vertex that witnesses this must have lost out-neighbors.

Throughout this section \(D\) is a minimal counterexample, \(F=F_D\), and \(S\) is a fixed set with \(\varnothing\ne S\subsetneq V(D)\). Put
\[
I=F(S)\cap S,\qquad E=F(S)\setminus S,\qquad g(T)=\bigl|F(T)\setminus(I\cup T)\bigr|\quad(T\subseteq E).
\]
Since \(D\) is strongly connected (Lemma 2.3), some arc leaves \(S\), so \(E\ne\varnothing\). Note that \(I\subseteq S\), \(E\cap S=\varnothing\), and \(g(\varnothing)=0\).

For \(T\subsetneq E\), let \(D_T\) be the oriented graph obtained from \(D\) by deleting all arcs from \(S\) to \(E\setminus T\). Every vertex of \(E\setminus T\ne\varnothing\) lies in \(F(S)\), so at least one arc is deleted. Write \(N_{1,T}^+\), \(N_{2,T}^+\) and \(F_T\) for neighborhoods and images in \(D_T\).

**Lemma 3.1.** Let \(T\subsetneq E\). There is a vertex \(v\in S\) such that \(Q=F(\{v\})\cap(E\setminus T)\) is nonempty and
\[
g(T\cup Q)-g(T)\le|Q|+|N_2^+(v)|-|N_1^+(v)|\le|Q|-1 .
\]

*Proof.* The graph \(D_T\) has the same vertices as \(D\) and fewer arcs, so it is not a counterexample: some vertex \(v\) satisfies \(|N_{1,T}^+(v)|\le|N_{2,T}^+(v)|\).

*The vertex \(v\) has lost out-neighbors.* Suppose that \(N_{1,T}^+(v)=N_1^+(v)\). Deleting arcs only removes walks, so \(F_T^2(\{v\})\subseteq F^2(\{v\})\), and Lemma 1.1 gives \(N_{2,T}^+(v)\subseteq N_2^+(v)\). Then \(|N_1^+(v)|=|N_{1,T}^+(v)|\le|N_{2,T}^+(v)|\le|N_2^+(v)|\), contrary to \(D\) being a counterexample. Hence \(v\) is the tail of a deleted arc, so \(v\in S\), and the out-neighbors it loses are exactly the vertices of \(Q=F(\{v\})\cap(E\setminus T)\), which is therefore nonempty. Since \(v\in S\), we have \(F(\{v\})\subseteq F(S)=I\cup T\cup(E\setminus T)\), so
\[
N_1^+(v)\subseteq I\cup T\cup Q,\qquad N_{1,T}^+(v)=N_1^+(v)\setminus Q\subseteq I\cup T. \tag{3.1}
\]

*Where the walks of \(D_T\) end.* Let \(v\to u\to w\) be a walk in \(D_T\). By (3.1), \(u\in I\cup T\). If \(u\in I\subseteq S\), the arc \(u\to w\) survived the deletion, so \(w\in F(S)\setminus(E\setminus T)=I\cup T\). If \(u\in T\), then \(w\in F(T)\). Therefore
\[
F_T^2(\{v\})\subseteq I\cup T\cup F(T). \tag{3.2}
\]

*Gained second neighbors.* Let \(w\in N_{2,T}^+(v)\setminus N_2^+(v)\). The walk of length two from \(v\) to \(w\) in \(D_T\) is also a walk in \(D\), and \(w\notin N_2^+(v)\), so Lemma 1.1 forces \(w\in N_1^+(v)\). As \(w\notin N_{1,T}^+(v)\), (3.1) gives \(w\in Q\). By (3.2), and because \(Q\) is disjoint from \(I\cup T\), we get \(w\in Q\cap F(T)\). Hence at most \(|Q\cap F(T)|\) vertices are gained.

*Lost second neighbors.* Let
\[
C=F(Q)\setminus\bigl(I\cup T\cup Q\cup F(T)\bigr).
\]
Every \(c\in C\) is the end of a walk \(v\to q\to c\) in \(D\) with \(q\in Q\), and \(c\notin N_1^+(v)\) by (3.1). By Lemma 1.1, \(C\subseteq N_2^+(v)\). By (3.2), no vertex of \(C\) lies in \(F_T^2(\{v\})\). Hence all of \(C\) is lost.

Combining the two counts with the choice of \(v\),
\[
|N_1^+(v)|-|Q|=|N_{1,T}^+(v)|\le|N_{2,T}^+(v)|\le|N_2^+(v)|-|C|+|Q\cap F(T)|. \tag{3.3}
\]

*The increment of \(g\).* Since \(F(T\cup Q)=F(T)\cup F(Q)\),
\[
F(T\cup Q)\setminus(I\cup T\cup Q)=\Bigl(\bigl(F(T)\setminus(I\cup T)\bigr)\setminus Q\Bigr)\cup C,
\]
and the two sets on the right are disjoint, because \(C\) avoids \(F(T)\). The set removed from \(F(T)\setminus(I\cup T)\) is \(Q\cap F(T)\), since \(Q\) avoids \(I\cup T\). Therefore
\[
g(T\cup Q)-g(T)=|C|-|Q\cap F(T)|,
\]
and (3.3) gives \(g(T\cup Q)-g(T)\le|Q|+|N_2^+(v)|-|N_1^+(v)|\). The last quantity is at most \(|Q|-1\) because \(|N_2^+(v)|<|N_1^+(v)|\) are integers. \(\square\)

**Proposition 3.2.** With \(S\), \(I\), \(E\) and \(g\) as above, \(g(E)\le|E|-1\).

*Proof.* Put \(T_0=\varnothing\). While \(T_k\ne E\), Lemma 3.1 supplies a nonempty \(Q_k\subseteq E\setminus T_k\) with \(g(T_k\cup Q_k)-g(T_k)\le|Q_k|-1\); set \(T_{k+1}=T_k\cup Q_k\). Each step is applied to the graph \(D_{T_k}\) obtained from the original \(D\), so Lemma 3.1 applies every time. The sets \(T_k\) strictly increase inside the finite set \(E\), so the process reaches \(T_r=E\) after \(r\ge1\) steps, because \(E\ne\varnothing\). Summing the increments and using \(g(\varnothing)=0\),
\[
g(E)\le\sum_{k<r}\bigl(|Q_k|-1\bigr)=|E|-r\le|E|-1.\qquad\square
\]

**Proposition 3.3** (Subset deficit). Let \(D\) be a minimal counterexample. Then every vertex of \(D\) has an in-neighbor, and
\[
\bigl|F^2(S)\setminus F(S)\bigr|<\bigl|F(S)\setminus S\bigr|\qquad\text{for every }\varnothing\ne S\subsetneq V(D).
\]

*Proof.* The first claim is Lemma 2.3. For the inequality, use the notation of this section. Since \(F(S)=I\cup E\) and \(F(I)\subseteq F(S)\) (because \(I\subseteq S\)),
\[
F^2(S)\setminus F(S)=\bigl(F(I)\cup F(E)\bigr)\setminus(I\cup E)=F(E)\setminus(I\cup E),
\]
whose size is \(g(E)\). Proposition 3.2 gives \(g(E)<|E|=|F(S)\setminus S|\). \(\square\)

For a single vertex \(S=\{v\}\) of a minimal counterexample, Proposition 3.3 reads \(|F^2(\{v\})\setminus F(\{v\})|<|F(\{v\})|\), which is the defining inequality \(|N_2^+(v)|<|N_1^+(v)|\) by Lemma 1.1. The proposition extends it to all nonempty proper sets; for \(S=V(D)\) both sides vanish, because \(F(V(D))=V(D)\).

## 4. Exercises

**4.1.** Show that every tournament on at most four vertices has a vertex \(v\) with \(|N_1^+(v)|\le|N_2^+(v)|\). (Use Example 1.2(a) and consider the strong tournaments.)

**4.2.** In the directed cycle on \(\mathbb Z/3\), compute both sides of the inequality of Proposition 3.3 for \(S=\{0\}\) and \(S=\{0,1\}\). Which strict inequalities fail?

**4.3.** Show that the minimality in Lemma 2.3 can be weakened: a counterexample with the fewest vertices (with no condition on arcs) is already strongly connected.

**4.4.** Let \(D\) be an oriented graph and \(S\subseteq V(D)\). Show that \(F^2(S)\setminus F(S)\) can contain vertices of \(S\), and give an example with \(S\cap(F^2(S)\setminus F(S))\neq\varnothing\).

**4.5.** In Lemma 3.1, the vertex \(v\) found for \(D_T\) depends on \(T\). Explain why the proof of Proposition 3.2 nevertheless needs only that each \(D_{T_k}\) has fewer arcs than \(D\), and not any relation between the graphs \(D_{T_k}\) for different \(k\).

## 5. Solutions

**4.1.** A tournament that is not strongly connected has a closed strong component \(C\) (Lemma 2.2) with \(C\ne V\), and a vertex that satisfies the inequality inside \(D[C]\) satisfies it in \(D\) by Lemma 2.1; arguing by induction on the number of vertices, it suffices to treat strong tournaments. A one-vertex tournament is a sink, and there is no strong tournament on two vertices. The strong tournament on three vertices is the directed triangle, where equality holds (Example 1.2(b)). In a strong tournament on four vertices every vertex has an in-neighbor and an out-neighbor, so every out-degree is \(1\) or \(2\); the out-degrees sum to \(6\), so they are \(1,1,2,2\), and some vertex \(v\) has out-degree \(1\). Its out-neighbor \(u\) has an out-neighbor other than \(v\) (since \(v\to u\)), and that vertex is not an out-neighbor of \(v\); so \(|N_2^+(v)|\ge1=|N_1^+(v)|\).

**4.2.** For \(S=\{0\}\): \(F(S)=\{1\}\), \(F^2(S)=\{2\}\), so both sides equal \(1\) and the strict inequality fails. For \(S=\{0,1\}\): \(F(S)=\{1,2\}\), \(F^2(S)=\{2,0\}\), so \(|F^2(S)\setminus F(S)|=1=|F(S)\setminus S|\), and the strict inequality fails again. This agrees with Example 1.2(b): the directed triangle is not a counterexample.

**4.3.** The proof of strong connectivity in Lemma 2.3 used only that \(D[C]\) is a counterexample with fewer vertices when \(C\ne V(D)\). It did not use the number of arcs.

**4.4.** In the directed triangle on \(\mathbb Z/3\) with \(S=\{0,1\}\) (Exercise 4.2), \(F^2(S)\setminus F(S)=\{0\}\subseteq S\). Unlike second neighborhoods of single vertices (Lemma 1.1), images of sets can return to the set.

**4.5.** Each step applies the minimality of \(D\) to the single graph \(D_{T_k}\), which has the same vertex set as \(D\) and fewer arcs. The estimate of Lemma 3.1 concerns the function \(g\), which is defined from the original graph \(D\) alone. The graphs \(D_{T_k}\) serve only to find the vertex \(v\) and the set \(Q_k\), so no comparison between them is needed.

## References

- [OpenAI-SN] OpenAI, *A proof of Seymour's second-neighborhood conjecture*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf
- [Sea19] T. Seacrest, *Seymour's second neighborhood conjecture for subsets of vertices*, 2018–2019. https://arxiv.org/abs/1808.06293
- [Sea12] T. Seacrest, *The arc-weighted version of the second neighborhood conjecture*, Journal of Graph Theory (2015); preprint 2012. https://arxiv.org/abs/1212.1883
- [BBKS] J. N. Brantner, G. Brockman, B. Kay and E. E. Snively, *Contributions to Seymour's second neighborhood conjecture*, Involve 2 (2009); preprint 2008. https://arxiv.org/abs/0808.0946
- [HP] H. Huang and F. Peng, *An improved bound on Seymour's second neighborhood conjecture*, 2024. https://arxiv.org/abs/2412.20234
- [SSS] A. Sadhukhan, R. B. Sandeep and S. Sen, *A proof of Seymour's second neighborhood conjecture for oriented graphs with minimum out-degree equal to 7*, 2026. https://arxiv.org/abs/2606.30588
- [Sul] B. D. Sullivan, *A summary of problems and results related to the Caccetta–Häggkvist conjecture*, 2006. https://arxiv.org/abs/math/0605646
