# Splitting a graph at a scale

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of the cycle decomposition theorem looks at a graph at a sequence of decreasing *scales* \(D\). At one scale, a graph of average degree at most \(D\) is treated in two operations. First, a few long cycles are removed, and the remaining edges are distributed over *boxes*: vertex sets of order at most \(D^{1.02}\) that may overlap, but whose orders add up to only slightly more than the order of the graph. Second, inside every box, vertex-disjoint *pieces* of cut expansion \(D^{0.90}\) are extracted; what remains in the box has average degree at most \(D^{0.95}\) and is passed to the next scale. This lesson proves that both operations are possible. The overlapping split adapts the expander splitting of Bucić and Montgomery [BM, Section 3], and the extraction of pieces uses the small-side charging of Conlon, Fox and Sudakov [CFS, Section 3].

All logarithms are to base two. Cut expansion is defined in [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md), Definition 1.1. For a vertex set \(U\) of a graph \(H\), write \(N_H(U)\) for the set of vertices adjacent to some vertex of \(U\); the *external neighbours* of \(U\) are the vertices of \(N_H(U)\setminus U\).

## 1. A long cycle from vertex expansion

**Lemma 1.1** (vertex expansion gives a long cycle). Put \(\varepsilon=1/32\). For every sufficiently large integer \(u\), with \(\alpha=\varepsilon/\log^2u\), the following holds. If a graph \(H\) of order \(u\) satisfies
\[
|N_H(U)\setminus U|\ge\alpha|U|
\]
for every \(U\subseteq V(H)\) with \(0<|U|\le u/2\), then \(H\) contains a cycle of length greater than
\[
q(u)=\frac{\alpha^2u}{100}=\frac{\varepsilon^2u}{100\log^4u}.
\]

*Proof.* Take \(u\) so large that \(q(u)\ge1\); also \(\alpha\le1\). The graph \(H\) is connected: otherwise its smallest component has between \(1\) and \(u/2\) vertices and no external neighbours.

*Depth-first search.* At every moment the vertices are divided into *unexplored* vertices, vertices on a *stack*, and *finished* vertices. Initially the stack holds one vertex and all others are unexplored. In each step, if the top vertex of the stack has an unexplored neighbour, push one such neighbour onto the stack; otherwise remove the top vertex and mark it finished. Every pushed vertex is adjacent to the previous top, so the stack, read from bottom to top, is a path. No edge joins a finished vertex to an unexplored one: when a vertex is finished it has no unexplored neighbour, and the unexplored set only shrinks afterwards. If the stack became empty while unexplored vertices remained, connectivity would give an edge between a finished and an unexplored vertex; so the search ends with all vertices finished.

The number of unexplored vertices minus the number of finished vertices starts at \(u-1\), ends at \(-u\), and decreases by exactly one in every step. So at some moment both numbers equal the same integer \(t\). The stack then holds \(L=u-2t\) vertices, forming a path \(\Pi\). If \(t\ge u/3\), the unexplored set has \(t\) vertices, \(0<t\le u/2\), and all its external neighbours lie on \(\Pi\); so \(L\ge\alpha t\ge\alpha u/3\). If \(t<u/3\), then \(L>u/3\ge\alpha u/3\). In both cases
\[
L\ge\frac{\alpha u}3 .
\]

*Three segments.* Write \(q=q(u)\) and \(j=\lfloor q\rfloor\ge1\). Then
\[
j+1\le2q=\frac{\alpha^2u}{50}\le\frac{\alpha u}6\le\frac L2 .
\]
Divide \(\Pi\) into three consecutive segments \(X,J,Z\) with \(|J|=j\), distributing the other \(L-j\) vertices as evenly as possible. Then \(X\) and \(Z\) each have at least \(\lfloor(L-j)/2\rfloor\ge(L-j-1)/2\ge L/4\) vertices, the last step because \(L\ge2j+2\).

Suppose \(H-J\) contains a path from \(X\) to \(Z\), and take a shortest one, from \(x\in X\) to \(z\in Z\). Its inner vertices avoid \(X\) and \(Z\), since a shorter path between the two sets would otherwise exist, and they avoid \(J\). So it meets \(\Pi\) only at \(x\) and \(z\), and together with the segment of \(\Pi\) between \(x\) and \(z\) it forms a cycle. That segment contains all \(j\) vertices of \(J\) and has at least \(j+1\) edges, and the connecting path has at least one; the cycle has at least \(j+2>q\) edges.

Otherwise \(X\) and \(Z\), each connected along \(\Pi\), lie in different components of \(H-J\). Let \(C\) be the component containing \(X\), let \(C'\) be the union of the other components, which contains \(Z\), and let \(A\) be the smaller of \(C\) and \(C'\). Then
\[
\begin{gathered}
\frac L4\le|A|\le\frac{u-j}2\le\frac u2,\\
N_H(A)\setminus A\subseteq J .
\end{gathered}
\]
The hypothesis gives
\[
j\ge\alpha|A|\ge\frac{\alpha L}4\ge\frac{\alpha^2u}{12}>q\ge j,
\]
a contradiction. \(\square\)

## 2. The splitting lemma

**Lemma 2.1** (splitting at a scale). There is an absolute constant \(D_{\rm sp}\) such that for every real \(D\ge D_{\rm sp}\) and every graph \(G\) on a nonempty vertex set of order \(N\) with average degree at most \(D\), the following two operations can be carried out one after the other.

1. Remove a family \(\mathcal C\) of edge-disjoint cycles, each of length at least \(D^{1.01}\), with
\[
|\mathcal C|\le\frac N{2D^{0.01}} .
\]
Partition the remaining edges into graphs \(G_Y\) on an indexed family \(\mathcal Y\) of vertex sets, the *boxes*, such that
\[
\begin{gathered}
\bigcup_{Y\in\mathcal Y}Y=V(G),\\
1\le|Y|\le D^{1.02},\\
\sum_{Y\in\mathcal Y}|Y|\le\Bigl(1+\frac2{\log D}\Bigr)N .
\end{gathered}
\]
Each \(G_Y\) has vertex set \(Y\) and carries only its assigned edges; boxes may overlap.
2. Put \(\sigma=D^{0.90}\). For every box \(Y\), partition \(E(G_Y)\) into the edge sets of a family \(\mathcal R_Y\) of graphs \(R\), the *pieces*, and a graph \(H_Y\) on \(Y\), the *residual*. The pieces have pairwise disjoint vertex sets contained in \(Y\), cut expansion at least \(\sigma\), and order
\[
\sigma\le|V(R)|\le D^{1.02},
\]
and the residual satisfies
\[
\frac{2|E(H_Y)|}{|Y|}\le D^{0.95}.
\]

So the cycles of \(\mathcal C\), the pieces and the residuals together partition \(E(G)\).

*Proof.* The lower bounds imposed on \(D\) below are absolute, and \(D_{\rm sp}\) is chosen to satisfy all of them.

*Long cycles.* Choose a maximal family \(\mathcal C\) of edge-disjoint cycles of length at least \(D^{1.01}\). They use at least \(|\mathcal C|D^{1.01}\) of the at most \(ND/2\) edges, which gives the bound on \(|\mathcal C|\). Delete their edges and keep all vertices. By maximality the remaining graph has no cycle of length at least \(D^{1.01}\), and neither has any subgraph of it formed below.

*Sparse external neighbourhoods.* Put \(T=D^{1.02}\). We claim that every graph \(H\) formed below, of order \(u>T\), has a nonempty vertex set \(U\) with
\[
|U|\le\frac u2,\qquad|N_H(U)\setminus U|<\frac{\varepsilon|U|}{\log^2u}.
\]
Otherwise Lemma 1.1 gives a cycle of length greater than \(q(u)\). The function \(x/\log^4x\) increases for \(\ln x>4\), as differentiation shows, and
\[
\frac{q(T)}{D^{1.01}}=\frac{\varepsilon^2}{100\cdot1.02^4}\cdot\frac{D^{0.01}}{\log^4D}
\]
tends to infinity with \(D\). Choose \(D_{\rm sp}\) so large that \(T\) lies in the range of Lemma 1.1, \(\ln T>4\) and \(q(T)>D^{1.01}\). Then \(q(u)>D^{1.01}\) for all \(u>T\), and the long cycle is impossible.

*Overlapping splits.* For such a set \(U\) put \(B=N_H(U)\setminus U\) and form two *children* with vertex sets
\[
V_1=U\cup B,\qquad V_2=V(H)\setminus U .
\]
Assign to the first child every edge of \(H\) with both ends in \(V_1\), and to the second child every other edge. An edge at a vertex of \(U\) has both ends in \(U\cup B\), so every edge of the second child has both ends in \(V_2\). The children's vertex sets cover \(V(H)\) and meet exactly in \(B\), and their edge sets partition \(E(H)\). Isolated vertices of the children are kept.

Write \(s=|U|\), \(b=|B|\), \(u_1=s+b\) and \(u_2=u-s\). Then \(1\le s\le u/2\) and \(b<\varepsilon s/\log^2u\le s/2\), so
\[
\begin{gathered}
1\le u_1\le\frac{3u}4,\qquad1\le u_2<u,\\
u_1+u_2=u+b\le u+\frac{\varepsilon u_1}{\log^2u}.
\end{gathered}
\]
Split every graph of order greater than \(T\), starting with the remaining graph on \(V(G)\). Child orders are positive integers smaller than the parent order, so the binary tree of splits is finite. Its leaves are the boxes, with the graphs \(G_Y\) formed by their assigned edges. The cover property at every split gives \(\bigcup_YY=V(G)\), and the boxes have order at most \(T\).

*The total order of the boxes.* For real \(x\ge1\) put
\[
\begin{aligned}
f(x)&=1+\frac1{\log(T/2)}\\
&\quad-\frac1{\log\max\{x,T/2\}} .
\end{aligned}
\]
For \(T\ge4\) the function \(f\) is nondecreasing, and \(1\le f\le1+1/\log(T/2)\le2\). At a split of a graph of order \(u>T\), put \(M=\max\{u_1,T/2\}\); then \(2\le M\le3u/4\), and
\[
\begin{aligned}
f(u)-f(u_1)&=\frac1{\log M}-\frac1{\log u}\\
&=\frac{\log(u/M)}{\log M\,\log u}\\
&\ge\frac{\log(4/3)}{\log^2u}.
\end{aligned}
\]
Also \(f(u_2)\le f(u)\). Therefore
\[
\begin{aligned}
&u_1f(u_1)+u_2f(u_2)\\
&\quad\le(u_1+u_2)f(u)-\frac{u_1\log(4/3)}{\log^2u}\\
&\quad\le uf(u)+\frac{u_1(\varepsilon f(u)-\log(4/3))}{\log^2u}\\
&\quad\le uf(u),
\end{aligned}
\]
since \(\varepsilon f(u)\le1/16<\log(4/3)\). Applying this at every split of the tree, from the leaves upwards, and using \(f\ge1\),
\[
\begin{aligned}
\sum_{Y}|Y|&\le\sum_Y|Y|f(|Y|)\le Nf(N)\\
&\le N\Bigl(1+\frac1{\log(T/2)}\Bigr).
\end{aligned}
\]
This also holds if \(N\le T\), when the tree is a single box. Finally \(1/\log(T/2)=1/(1.02\log D-1)\), which is at most \(2/\log D\) for \(D\ge4\). This proves the first operation.

*Pieces.* Fix a box \(Y\), write \(y=|Y|\), and start with \(G_Y\). As long as some current graph, on a vertex set \(A\) with \(|A|\ge2\), fails to have cut expansion \(\sigma\), choose a partition \(A=A_1\cup A_2\) into nonempty sets whose cut has fewer than \(\sigma\min\{|A_1|,|A_2|\}\) edges. Put these cut edges into \(H_Y\), and continue separately with the edges inside \(A_1\) and inside \(A_2\). Orders decrease, so the procedure stops, and the final vertex sets partition \(Y\). The final graphs on at least two vertices are the pieces; each has cut expansion at least \(\sigma\). By Lemma 1.2 of [Routing in graphs with cut expansion](routing-in-graphs-with-cut-expansion.md), a piece of order \(r\) has \(r-1\ge\sigma\), so \(\sigma\le r\le y\le D^{1.02}\). Final single vertices carry no edges. Every edge not put into \(H_Y\) ends in exactly one final graph, so the pieces and \(H_Y\) partition \(E(G_Y)\); the residual \(H_Y\) is taken on all of \(Y\).

To bound \(|E(H_Y)|\), charge the cut edges of each split equally to the vertices of a smaller side. Each charged vertex receives less than \(\sigma\) at that split. Whenever a vertex is charged, the current set containing it shrinks at least by half, so a vertex is charged at most \(\log y\) times. The cut edges of different splits are distinct, because later splits use only edges inside an earlier child. Hence
\[
|E(H_Y)|\le\sigma y\log y,
\]
and, for \(1\le y\le D^{1.02}\) and \(D\) large,
\[
\frac{2|E(H_Y)|}y\le2.04D^{0.90}\log D\le D^{0.95}.
\]
\(\square\)

**Remark 2.2.** If both operations are repeated on the residuals, the boxes descending from a fixed box cover all its vertices: every split covers its parent, and every residual \(H_Y\) keeps the whole vertex set \(Y\), whichever of its edges were removed as cycles or pieces.

## 3. Exercises

**3.1** (easy). Show that in Lemma 1.1 the hypothesis cannot be dropped: a star with \(u\) vertices has no cycle at all. Which sets \(U\) violate the hypothesis?

**3.2** (medium). Let \(H\) be a graph whose longest cycle has length at most \(m\). Show that \(H\) has a vertex set \(U\) with \(0<|U|\le|V(H)|/2\) and \(|N_H(U)\setminus U|<\alpha|U|\) whenever \(m\le q(|V(H)|)\) and \(|V(H)|\) is large.

**3.3** (easy). Show that the inequality \(u_1f(u_1)+u_2f(u_2)\le uf(u)\) is strict at every split.

**3.4** (easy). Show that the pieces produced in a box have order at least \(\sigma+1\).

## 4. Solutions

**3.1.** In a star with centre \(c\), a set \(U\) of \(\lfloor u/2\rfloor\) leaves has the single external neighbour \(c\). The hypothesis would require at least \(\alpha\lfloor u/2\rfloor\) external neighbours, and \(\alpha u/2=u/(64\log^2u)\) exceeds one for large \(u\).

**3.2.** This is the contrapositive of Lemma 1.1: if every such \(U\) had at least \(\alpha|U|\) external neighbours, \(H\) would contain a cycle longer than \(q(|V(H)|)\ge m\).

**3.3.** The last step of the chain drops the term \(u_1(\varepsilon f(u)-\log(4/3))/\log^2u\). It is negative, because \(u_1\ge1\) and \(\varepsilon f(u)\le1/16<\log(4/3)\).

**3.4.** By Lemma 1.2 of the routing lesson, every vertex of a piece of order \(r\ge2\) has at least \(\sigma\) neighbours, and a vertex has at most \(r-1\) neighbours, so \(r\ge\sigma+1\).

## References

- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
- [CFS] D. Conlon, J. Fox and B. Sudakov, *Cycle packing*, Random Structures & Algorithms 45 (2014), 608–626; arXiv:1310.0632. https://arxiv.org/abs/1310.0632
