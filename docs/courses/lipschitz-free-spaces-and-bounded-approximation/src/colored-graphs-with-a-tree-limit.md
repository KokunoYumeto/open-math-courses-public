# Colored graphs with a tree limit

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson constructs, for a given integer \(p\ge1\), the bounded metric space \(M_p\) and its finite set of anchors \(A_p\) of the theorem on blocks. The points of \(M_p\) are the vertices of a sequence of finite graphs of a fixed large degree, with colored vertices, and finitely many further points, the anchors. The graphs are chosen so that small neighbourhoods of most vertices look like the neighbourhoods in a regular tree whose vertices are colored independently and uniformly. Each vertex gets a *label*: the list of its distances to the color classes, cut off at a fixed height. Vertices with the same label are joined to the same anchor by a long edge. This makes the space bounded, while small balls stay inside one graph.

- Multigraphs, incidences, balls and their types (Section 1).
- Regular multigraphs from random permutations; their balls are trees with high probability (Lemma 2.2).
- A fixed sequence of colored graphs whose local statistics converge to those of the colored tree (Proposition 2.4).
- The parameters (Section 3) and the block (Section 4).
- The geometry of the block (Proposition 5.1).

The lesson follows [OpenAI-LF, Section 3]. It is independent of the first two lessons of the course: it uses only finite graphs, finite probability (uniform random permutations, independence, Chebyshev's inequality) and metric spaces.

## 1. Multigraphs, balls and types

A *multigraph* has a set of vertices and a set of *edge instances*. Every edge instance has two *oriented incidences*, \(e\) and its *reverse* \(\bar e\). An incidence \(e\) has an initial vertex \(x\) and a terminal vertex \(y\); we write \(e\colon x\to y\), and then \(\bar e\colon y\to x\). Different edge instances may join the same two vertices (*parallel edges*), and an edge instance may have \(x=y\) (a *loop*); a loop still has two different incidences. Let \(\mathcal D(x)\) be the set of the incidences with the initial vertex \(x\). The multigraph is \(\Delta\)-*regular* if \(|\mathcal D(x)|=\Delta\) for every vertex \(x\). So a loop at \(x\) counts twice in the degree of \(x\).

A *walk* of length \(t\) is a sequence \(x_0,e_1,x_1,\dots,e_t,x_t\) with \(e_s\colon x_{s-1}\to x_s\). It is *nonbacktracking* if \(e_{s+1}\ne\bar e_s\) for all \(s\): no step reverses the step before it. A nonbacktracking walk may visit a vertex several times.

The *graph distance* of two vertices is the smallest length of a walk between them, and \(+\infty\) if there is none. For a vertex \(x\) and \(r\ge0\) the *ball* \(B_r(x)\) is the multigraph formed by the vertices at a graph distance of at most \(r\) from \(x\) and all edge instances between them, with \(x\) marked as the root. If the vertices carry colors, the ball carries them too. The *type* of a ball is its isomorphism class as a rooted colored multigraph.

**Lemma 1.1.** In a \(\Delta\)-regular multigraph with \(\Delta\ge2\), there are exactly \(\Delta^t\) walks of length \(t\) from a given vertex, and at most \(\Delta^{s+1}\) vertices at a graph distance of at most \(s\) from it.

**Proof.** Each step of a walk can be chosen in \(\Delta\) ways. A vertex at a distance of at most \(s\) is the end of a walk of some length \(t\le s\); so there are at most \(1+\Delta+\dots+\Delta^s\le\Delta^{s+1}\) of them. \(\blacksquare\)

Fix an even integer \(\Delta\ge4\) and a number \(k\ge1\) of colors. By Lemma 1.1 a ball of radius \(r\) in a \(\Delta\)-regular multigraph has a bounded number of vertices and of edge instances. So there are only finitely many types of balls of radius \(r\) with colors in \(\{1,\dots,k\}\); let \(\mathcal T_r\) be the set of these types.

The \(\Delta\)-*regular tree* is the infinite tree in which every vertex has \(\Delta\) neighbours. Its ball of radius \(r\) is a finite tree: the root has \(\Delta\) children, and every other vertex at a depth less than \(r\) has \(\Delta-1\) children. A ball in a multigraph is a *tree ball* if it is isomorphic, as a rooted multigraph, to this tree. Color the vertices of the tree ball of radius \(r\) independently and uniformly with the colors \(1,\dots,k\). For \(\tau\in\mathcal T_r\) let \(q_\tau\) be the probability that the colored tree ball has the type \(\tau\). So \(\sum_{\tau\in\mathcal T_r}q_\tau=1\), and \(q_\tau=0\) for the types that are not trees.

## 2. Graphs from permutations

Let \(V\) be a set of \(N\) vertices and let \(\sigma_1,\dots,\sigma_{\Delta/2}\) be permutations of \(V\). They define a multigraph \(G(\sigma)\) on \(V\): for every \(a\in\{1,\dots,\Delta/2\}\) and every \(v\in V\) there is one edge instance, with one incidence from \(v\) to \(\sigma_a(v)\) and its reverse from \(\sigma_a(v)\) to \(v\). A vertex \(x\) is the initial vertex of the \(\Delta/2\) incidences to the vertices \(\sigma_a(x)\) and of the \(\Delta/2\) incidences to the vertices \(\sigma_a^{-1}(x)\). So \(G(\sigma)\) is \(\Delta\)-regular. A fixed point of \(\sigma_a\) gives a loop, and a cycle of length two of \(\sigma_a\) gives two parallel edges.

Now let the permutations be random: independent, each uniform among the \(N!\) permutations of \(V\). Let the colors of the vertices be independent and uniform in \(\{1,\dots,k\}\), and independent of the permutations.

**Lemma 2.1** (one more value). Let \(\sigma\) be a uniform random permutation of \(V\). Let \(u_1,\dots,u_s\in V\) be different, let \(w_1,\dots,w_s\in V\) be different, and let \(\mathcal A\) be the event that \(\sigma(u_i)=w_i\) for all \(i\). For \(u\notin\{u_1,\dots,u_s\}\), conditionally on \(\mathcal A\) the vertex \(\sigma(u)\) is uniform on the \(N-s\) vertices outside \(\{w_1,\dots,w_s\}\). For \(w\notin\{w_1,\dots,w_s\}\), conditionally on \(\mathcal A\) the vertex \(\sigma^{-1}(w)\) is uniform on the \(N-s\) vertices outside \(\{u_1,\dots,u_s\}\).

**Proof.** There are \((N-s)!\) permutations in \(\mathcal A\). For each admissible value \(w'\) of \(\sigma(u)\), exactly \((N-s-1)!\) of them have \(\sigma(u)=w'\). The second statement is the first for \(\sigma^{-1}\). \(\blacksquare\)

For \(r\ge0\) put
\[
C=2\,\bigl(1+\Delta+\Delta^2+\dots+\Delta^{r+1}\bigr) ;
\]
we write \(C(\Delta,r)\) for this number when the dependence matters.

**Lemma 2.2** (exploration). Let \(N>C\) and let \(v_1\ne v_2\) be vertices. With a probability of at least \(1-C^2/(N-C)\), the balls \(B_r(v_1)\) and \(B_r(v_2)\) of \(G(\sigma)\) are tree balls and have no vertex in common.

**Proof.** We reveal the permutations step by step. At every moment some vertices are *known*; each known vertex has a *depth* and belongs to one of the two roots. At the start \(v_1\) and \(v_2\) are known, with depth \(0\). The known vertices of depth at most \(r\) are treated in the order in which they became known. To treat a vertex \(u\) means to go through its \(\Delta\) *questions*: for each \(a\), "what is \(\sigma_a(u)\)?" and "what is \(\sigma_a^{-1}(u)\)?". If the answer follows from an answer given before, nothing is done. This happens exactly when \(u\) became known as the answer to the opposite question at another vertex. Otherwise the question is *fresh*, and its answer \(w\) is revealed. If \(w\) is a known vertex, we say that a *collision* occurs, and the procedure stops. If not, \(w\) becomes known, with the depth of \(u\) plus one and the root of \(u\).

*The probability of a collision.* For each root there are at most \(\Delta^t\) known vertices of depth \(t\), for \(t\le r+1\). So at every moment there are at most \(C\) known vertices, at most \(C\) fresh questions have been asked, and for each \(\sigma_a\) at most \(C\) values have been revealed. Consider the moment before a fresh question about \(\sigma_a\). The answers given so far form an event of the kind in Lemma 2.1 for each of the permutations, and the permutations are independent. By Lemma 2.1 the answer is uniform on a set of at least \(N-C\) vertices, of which at most \(C\) are known. So the conditional probability of a collision at this question is at most \(C/(N-C)\). There are at most \(C\) fresh questions. So the probability that a collision occurs is at most \(C^2/(N-C)\).

*Without a collision.* Assume that the procedure ends without a collision. Let \(u\) be a known vertex of depth at most \(r\). One of its \(\Delta\) incidences leads to the vertex at which \(u\) was found, its *parent*, unless \(u\) is a root. Each other incidence belongs to a fresh question, whose answer was a new vertex, a *child* of \(u\). In particular \(u\) has no loop and no parallel edges, and the \(\Delta\) incidences at \(u\) lead to \(\Delta\) different vertices. So the known vertices with the revealed edges form two trees with the roots \(v_1\) and \(v_2\), without common vertices, in which a root has \(\Delta\) children and every other vertex of depth at most \(r\) has \(\Delta-1\) children.

The graph distance from \(v_1\) to a known vertex of its tree is its depth, and the vertices at a graph distance of at most \(r+1\) from \(v_1\) are exactly the vertices of its tree. This follows by induction on the distance \(t\le r+1\): a vertex at the distance \(t\) has a neighbour at the distance \(t-1\le r\); that neighbour is known with the depth \(t-1\), all its incidences lead to its parent and its children, and so the vertex is one of these and has a depth of at most \(t\); the depth is at least the distance because the tree gives a walk. Finally, every edge instance between two vertices at a distance of at most \(r\) from \(v_1\) is an edge of the tree, because all incidences at these vertices are tree edges. So \(B_r(v_1)\) is the tree cut at the depth \(r\), a tree ball. The same holds for \(v_2\), and the two balls have no common vertex. \(\blacksquare\)

For a type \(\tau\in\mathcal T_r\) let \(X_{\tau,N}\) be the fraction of the vertices \(v\) of the random colored multigraph for which \(B_r(v)\) has the type \(\tau\).

**Lemma 2.3.** For \(N>C\) and every \(\tau\in\mathcal T_r\),
\[
\mathbb E\,(X_{\tau,N}-q_\tau)^2\le\frac1N+\frac{3C^2}{N-C} .
\]

**Proof.** Write \(q=q_\tau\) and \(\varepsilon=C^2/(N-C)\), and let \(I_v\) be \(1\) if \(B_r(v)\) has the type \(\tau\) and \(0\) otherwise. The colors are independent of the permutations. For a fixed choice of the permutations for which \(B_r(v)\) is a tree ball, the probability over the colors that \(I_v=1\) is \(q\), by the definition of \(q\). For a fixed choice for which \(B_r(v)\) and \(B_r(w)\) are tree balls without a common vertex, the colors in the two balls are independent, and the probability that \(I_v=I_w=1\) is \(q^2\). By Lemma 2.2 the permutations are of these kinds with a probability of at least \(1-\varepsilon\). On the remaining event the conditional probabilities lie between \(0\) and \(1\). Hence, for \(v\ne w\),
\[
|\mathbb E\,I_v-q|\le\varepsilon,\qquad|\mathbb E\,I_vI_w-q^2|\le\varepsilon .
\]
Now \(X_{\tau,N}-q=\frac1N\sum_v(I_v-q)\), so
\[
\begin{aligned}
&\mathbb E\,(X_{\tau,N}-q)^2\\
&\qquad=\frac1{N^2}\sum_{v,w}\mathbb E\,(I_v-q)(I_w-q) .
\end{aligned}
\]
The \(N\) terms with \(v=w\) are at most \(1\). For \(v\ne w\),
\[
\begin{aligned}
&\mathbb E\,(I_v-q)(I_w-q)\\
&\quad=(\mathbb E\,I_vI_w-q^2)-q\,(\mathbb E\,I_v-q)\\
&\qquad-q\,(\mathbb E\,I_w-q) ,
\end{aligned}
\]
which is at most \(3\varepsilon\) in absolute value. \(\blacksquare\)

**Proposition 2.4** (a sequence with a colored tree limit). Let \(\Delta\ge4\) be even and \(k\ge1\). There is a sequence \(G_1,G_2,\dots\) of finite nonempty \(\Delta\)-regular multigraphs with vertex colors in \(\{1,\dots,k\}\) such that for every \(r\ge0\) and every \(\tau\in\mathcal T_r\) the fraction of the vertices \(x\) of \(G_m\) for which \(B_r(x)\) has the type \(\tau\) converges to \(q_\tau\) as \(m\to\infty\).

**Proof.** Fix \(m\ge1\). The set \(\mathcal T_0\cup\dots\cup\mathcal T_m\) is finite; let \(n_m\) be its size. By Lemma 2.3 and Chebyshev's inequality, for a type \(\tau\) of radius \(r\le m\),
\[
\begin{aligned}
&\mathbb P\bigl(|X_{\tau,N}-q_\tau|\ge\tfrac1m\bigr)\\
&\qquad\le m^2\Bigl(\frac1N+\frac{3C^2}{N-C}\Bigr) ,
\end{aligned}
\]
with \(C=C(\Delta,r)\le C(\Delta,m)\). The right side tends to \(0\) as \(N\to\infty\). Choose \(N=N_m\) so large that it is less than \(1/n_m\) for all these types, and \(N_m>N_{m-1}\). Then with positive probability \(|X_{\tau,N}-q_\tau|<1/m\) for all types of radius at most \(m\) at once. Let \(G_m\) be one colored multigraph \(G(\sigma)\) on \(N_m\) vertices with this property. For a fixed type \(\tau\) of radius \(r\), the error is less than \(1/m\) for all \(m\ge r\). \(\blacksquare\)

The sequence \(G_m\) is a fixed sequence of graphs: the random choice was used only to show that such graphs exist.

**Corollary 2.5.** Let \(r\ge0\) and let \(\mathcal S\subseteq\mathcal T_r\) be a set of types. The fraction of the vertices \(x\) of \(G_m\) for which the type of \(B_r(x)\) lies in \(\mathcal S\) converges to \(\sum_{\tau\in\mathcal S}q_\tau\), the probability that the colored tree ball has a type in \(\mathcal S\).

**Proof.** A finite sum of convergent sequences. \(\blacksquare\)

A property of a vertex that can be read off from the colored ball \(B_r(x)\) up to isomorphism is a set of types. So for every such property the fraction of the vertices of \(G_m\) that have it converges to the probability that the root of the colored tree has it.

## 3. The parameters

Fix an integer \(p\ge1\): the bound for the norm of the operators that the block is to defeat. Put
\[
\begin{gathered}
L=10p,\qquad R=3L=30p,\\
K=10p\,(R+1),\qquad D=K+2L+5,\\
B=4R+D,\qquad V=1+4pB .
\end{gathered}
\]
Choose an even integer \(\Delta\ge4\) with \(\Delta>20V\), put
\[
Q=\Delta^{2L+1},\qquad H=\Delta^{D+1} ,
\]
and choose an integer \(k>2\Delta QH\).

**Lemma 3.1.** 1. \(B=300p^2+150p+5\), the number \(B_p\) of the theorem on blocks.

2. \(R>2L\) and \(L\le K\).

3. \((2pR+1)/K\le\tfrac15\).

4. \(K+2L+1=D-4\).

5. \(V/\Delta<\tfrac1{20}\) and \(\Delta QH/k<\tfrac12\).

**Proof.** \(K=300p^2+10p\) and \(D=300p^2+30p+5\); so \(B=120p+D\) is the number in part 1. Part 3 says \(5(60p^2+1)\le300p^2+10p\), that is, \(5\le10p\). The rest is immediate. \(\blacksquare\)

The roles of the numbers, in the proof of the theorem on blocks in the next two lessons: \(L\) is the height of the test functions; \(R\) is the length of the edges to the anchors, longer than \(2L\) so that balls of radius \(2L\) do not reach an anchor; \(K\) is the width of the bumps, large so that their slope \(L/K\) is small; \(D\) is the height at which the labels are cut off; \(B\) bounds the diameter; \(V\) bounds the total variation of certain signed measures; \(\Delta\) is the degree, large compared with \(V\); \(Q\) bounds the size of balls of radius \(2L\); \(H\) bounds the number of label coordinates below \(D\); and \(k\) is the number of colors, large compared with \(\Delta QH\).

By Proposition 2.4 there is a sequence \(G_1,G_2,\dots\) of finite nonempty \(\Delta\)-regular multigraphs with vertex colors in \(\{1,\dots,k\}\) and with a colored tree limit. Fix such a sequence, with disjoint vertex sets. All these choices depend only on \(p\).

## 4. The block

The vertices of the graphs \(G_m\) are called *source vertices*, and their edges *source edges*.

*Labels.* For a source vertex \(x\) of \(G_m\) and a color \(i\) let \(\varrho_i(x)\) be the graph distance in \(G_m\) from \(x\) to the nearest vertex of color \(i\), and \(+\infty\) if no vertex of color \(i\) lies in the component of \(x\). Put
\[
h_i(x)=\min\{D,\ \varrho_i(x)\} .
\]
The *label* of \(x\) is the vector \(h(x)\) with the coordinates \(h_1(x),\dots,h_k(x)\). It lies in \(\{0,\dots,D\}^k\).

*Anchors.* Let \(\mathcal H\) be the set of the labels of all source vertices. It is finite, with at most \((D+1)^k\) elements. For every \(v\in\mathcal H\) add one new point \(a_v\), an *anchor*, and give it the label \(h(a_v)=v\). For a source vertex \(x\) let \(a(x)=a_{h(x)}\).

*Edges and lengths.* Form a graph with lengths on the set \(M_p\) of all source vertices and all anchors:

- every source edge is kept, with the length \(1\);
- every source vertex \(x\) is joined to its anchor \(a(x)\) by an *attachment edge* of length \(R\);
- any two different anchors \(a_v,a_w\) are joined by an *anchor edge* of length \(2R+\|v-w\|_\infty\).

Here \(\|v-w\|_\infty=\max_i|v_i-w_i|\). Let \(d_p(u,u')\) be the smallest total length of a path from \(u\) to \(u'\) in this graph, and \(0\) for \(u=u'\). Let \(A_p\) be the set of the anchors, and choose one anchor as the base point \(o\).

So two source vertices with the same label, also from different graphs \(G_m\), are joined through their common anchor by a path of length \(2R\). Paths through the anchors can be much shorter than paths inside a graph \(G_m\).

## 5. The geometry of the block

**Proposition 5.1.** 1. \(d_p\) is a metric on \(M_p\) with integer values, so \(d_p(u,u')\ge1\) for \(u\ne u'\). The set \(M_p\) is countably infinite and has a diameter of at most \(B\). The set \(A_p\) is finite. The two ends of a source edge have a distance of at most \(1\).

2. \(\|h(u)-h(u')\|_\infty\le d_p(u,u')\) for all \(u,u'\in M_p\). If a source vertex \(x\) has the color \(i\), then \(h_i(x)=0\). For every source vertex, \(h(a(x))=h(x)\).

3. For every source vertex \(x\) and every anchor \(a\): \(d_p(x,a)\ge R\), and \(d_p(x,a(x))=R\).

4. Every closed ball of radius \(2L\) in \(M_p\) has at most \(Q\) points. For every \(t\in M_p\) at most \(H\) coordinates of \(h(t)\) are less than \(D\).

**Proof.** *Part 1.* All lengths are positive integers. Any two points are joined by a path: a source vertex is joined to its anchor, and all anchors are joined to each other. So for \(u\ne u'\) the lengths of the paths from \(u\) to \(u'\) form a nonempty set of positive integers, which has a smallest element. Symmetry and the triangle inequality follow by reversing and joining paths. The union of the infinitely many nonempty finite graphs \(G_m\) is countably infinite, and finitely many anchors are added.

For the diameter note that \(\|v-w\|_\infty\le D\) for two labels. Two source vertices with different anchors are joined by two attachment edges and one anchor edge, of total length at most \(R+(2R+D)+R=B\). With the same anchor the length is \(2R\). A source vertex and an anchor are joined by a path of length at most \(R+2R+D\), and two anchors by an edge of length at most \(2R+D\). A source edge is itself a path of length \(1\) between its ends.

*Part 2.* Let two source vertices \(x,y\) be joined by a source edge, and let \(i\) be a color. If a vertex of color \(i\) lies in their component, the graph distances of \(x\) and \(y\) to the color class differ by at most \(1\), and cutting off at \(D\) keeps this. Otherwise both coordinates are \(D\). So \(\|h(x)-h(y)\|_\infty\le1\), the length of the edge. Along an attachment edge the labels agree. Along an anchor edge the labels differ by \(\|v-w\|_\infty\), which is less than its length. Adding these inequalities along a shortest path gives the first claim. The second and third hold by the definitions.

*Part 3.* A path from \(x\) to an anchor reaches the set of anchors for the first time along an attachment edge, of length \(R\). The edge from \(x\) to \(a(x)\) has the length \(R\).

*Part 4.* Every edge that is not a source edge has a length of at least \(R>2L\). So a shortest path of length at most \(2L\) uses only source edges. Hence the closed ball of radius \(2L\) around an anchor is one point, and the closed ball of radius \(2L\) around a source vertex of \(G_m\) is contained in the set of the vertices of \(G_m\) at a graph distance of at most \(2L\) from it. By Lemma 1.1 this set has at most \(\Delta^{2L+1}=Q\) elements.

Let \(x\) be a source vertex and \(h_i(x)<D\). Then there is a vertex of color \(i\) at a graph distance of at most \(D-1\) from \(x\). For different colors these vertices are different. By Lemma 1.1 there are at most \(\Delta^D\le H\) such colors. An anchor has the label of a source vertex. \(\blacksquare\)

Two consequences are used in the next lesson. First, for every point \(t\) of \(M_p\) there are at most \(Q\) points within the distance \(2L\). Secondly, let a source vertex \(x\) have the color \(i\) and let \(\|h(x)-h(t)\|_\infty<D\) for a point \(t\). Then \(h_i(t)<D\), because \(h_i(x)=0\). So a point \(t\) restricts the colors of those source vertices whose labels are close to its label to a set of at most \(H\) colors out of \(k\).

## 6. Exercises

**6.1.** Compute \(L,R,K,D,B,V\) for \(p=1\), the smallest admissible \(\Delta\), and the exponents of \(\Delta\) in \(Q\), \(H\) and in the bound for \(k\).

**6.2.** Show that in the random multigraph \(G(\sigma)\) the mean number of loops is \(\Delta/2\).

**6.3.** For \(r=1\), compute the probability that in the colored \(\Delta\)-regular tree the root has the color \(1\) and no neighbour of the root has the color \(1\). To what does Corollary 2.5 apply here?

**6.4.** Let \(x,y\) be source vertices with \(d_p(x,y)\le2L\). Show that \(x\) and \(y\) lie in the same graph \(G_m\) and that \(d_p(x,y)\) is their graph distance in \(G_m\).

**6.5.** Show that every label in \(\mathcal H\) has at least \(k-H\) coordinates equal to \(D\).

## 7. Solutions

**6.1.** \(L=10\), \(R=30\), \(K=310\), \(D=335\), \(B=455\), \(V=1821\). The condition \(\Delta>20V=36420\) with \(\Delta\) even gives \(\Delta=36422\). Further \(Q=\Delta^{21}\), \(H=\Delta^{336}\), and \(k>2\Delta^{358}\). The sizes of the graphs \(G_m\) that the proof uses are larger still. The block is an object whose existence is proved; it is not meant to be computed.

**6.2.** A loop is a fixed point of some \(\sigma_a\). A uniform permutation fixes a given vertex with the probability \(1/N\), so its mean number of fixed points is \(1\). There are \(\Delta/2\) permutations.

**6.3.** The root and its \(\Delta\) neighbours are \(\Delta+1\) different vertices with independent uniform colors. The probability is \(\frac1k\,(1-\frac1k)^\Delta\). The property is a set of types in \(\mathcal T_1\); by Corollary 2.5 the fraction of the vertices of \(G_m\) with this property converges to this number.

**6.4.** A shortest path from \(x\) to \(y\) has a length of at most \(2L<R\), so it uses only source edges, as in the proof of part 4. So it is a walk in one graph \(G_m\), and its length is at least the graph distance. Every walk in \(G_m\) is a path in the graph with lengths, so \(d_p(x,y)\) is at most the graph distance.

**6.5.** By part 4 of Proposition 5.1 at most \(H\) coordinates are less than \(D\), and all coordinates are at most \(D\).

## References

- [OpenAI-LF] OpenAI, *A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces*, OpenAI Math Release preprint, 26 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026
