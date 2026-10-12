# Component labels and annular depth

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[A continuum without cut points and its graph](a-continuum-without-cut-points-and-its-graph.md) describes a compact connected space \(L\) without cut points, a group \(H\), and a graph \(K\) whose vertices accumulate on \(L\). Paths of \(K\) stay near a point of \(L\) when their ends are near it. In the next lesson such paths are pushed towards \(L\), and for this some vertices of the graph have to be removed. This lesson prepares two tools.

- *Component labels.* When a set of vertices is removed, the remaining graph falls into components. Near a point of \(L\) at which the removed vertices do not accumulate, all remaining vertices lie in one component, and this component depends on the point in a locally constant way (Theorem 2.1). At a removed vertex that lies in \(L\) this uses the vanishing of the first Čech cohomology of \(L\).
- *Annular depth.* There is a family of pairs of disjoint closed sets, called annuli, that is invariant under \(H\), in which only finitely many members have two large sides, and which nests arbitrarily often around every point of \(L\) (Theorem 3.2). Counting nested annuli between a set and a point gives an invariant depth, which is finite between group elements and large near \(L\) (Theorem 4.1).

The lesson follows Section 8 of [OpenAI-S]; systems of annuli of this kind were introduced by Bowditch [Bowditch 3]. It uses the lesson named above and the extension of locally constant maps across a point from [First Čech cohomology of a compact metric space](course:continua-arcs-and-cut-points/first-cech-cohomology-of-a-compact-metric-space).

## 1. The setting

We use the following data and properties. They hold in the two cases of the lesson on a continuum without cut points and its graph (Theorem 2.1 there); from here on only this list is used.

- (S1) \((Y,\rho)\) is a compact metric space, the disjoint union of a group \(H\) and a set \(L\). The points of \(H\) are isolated in \(Y\) and dense in \(Y\). The group \(H\) acts on \(Y\) by homeomorphisms that extend left multiplication on \(H\) and map \(L\) to itself. The space \(L\) is compact and connected, has more than one point and no cut point.
- (S2) If \((h_n)\) is a sequence in \(H\) with \(h_n\to a\in L\) and \(h_n^{-1}\to b\in L\), then for every closed set \(C\subseteq Y\setminus\{b\}\) and every open set \(U\subseteq Y\) containing \(a\), \(h_n(C)\subseteq U\) for all but finitely many \(n\).
- (S3) \(K\) is a connected graph with vertex set \(I\subseteq Y\); \(H\) maps \(I\) to itself and edges to edges, with finitely many orbits of vertices and of edges. Either \(I=H\) or \(I\subseteq L\). Every point of \(L\) is the limit of a sequence of pairwise distinct points of \(I\).
- (S4) For every \(w\in I\): \(\rho(hw,h)\to0\) as \(h\to\infty\) in \(H\).
- (S5) For every \(x\in L\) and every neighbourhood \(W\) of \(x\) in \(Y\) there is a neighbourhood \(V\) of \(x\) in \(Y\) such that any two points of \(I\cap V\) are joined by a path in \(K\) all of whose points lie in \(W\).
- (S6) If \(I\subseteq L\), then for every \(p\in I\) there is \(h\in H\) of infinite order with \(hp=p\) and \(h^jz\to p\) as \(j\to\infty\) for every \(z\in L\).
- (S7) \(\check H^1(L;k)=0\), where \(k\) is the group with two elements \(0,1\).

By (S1), a sequence of pairwise distinct elements of \(H\) has a subsequence \((h_n)\) such that \(h_n\) and \(h_n^{-1}\) converge to points of \(L\): limits in the compact space \(Y\) exist, and a limit of distinct points is not an isolated point. Since \(L\) is connected with more than one point, no point of \(L\) is isolated in \(L\). Balls \(B(y,r)\) are open balls of \(Y\).

## 2. Component labels

For a set \(D\subseteq Y\) let \(D'\) be the set of limits of sequences of pairwise distinct points of \(D\). It is closed.

Let \(T\subseteq I\) be a set of vertices, the *allowed* vertices; the vertices in \(I\setminus T\) are *deleted*. Let \(K[T]\) be the graph on \(T\) whose edges are the edges of \(K\) with both ends in \(T\); its *components* are the classes of the relation "joined by a path in \(K[T]\)". Let
\[
\Omega_T=L\setminus(I\setminus T)' .
\]
This is the open subset of \(L\) of the points at which deleted vertices do not accumulate.

**Theorem 2.1.** Let \(T\subseteq I\) and \(x\in\Omega_T\).

1. \(x\) is the limit of a sequence of pairwise distinct allowed vertices.
2. There is exactly one component \(Q_T(x)\) of \(K[T]\) such that all allowed vertices in some neighbourhood of \(x\) in \(Y\) belong to \(Q_T(x)\).
3. The map \(x\mapsto Q_T(x)\) is locally constant on \(\Omega_T\).
4. If \(x\) is itself an allowed vertex, then \(x\in Q_T(x)\).

**Proof.** There is a neighbourhood \(W\) of \(x\) in \(Y\) that contains no deleted vertex other than possibly \(x\): otherwise there would be deleted vertices different from \(x\) at distance less than \(1/n\) from \(x\) for every \(n\), and \(x\) would lie in \((I\setminus T)'\). By (S3), \(x\) is the limit of a sequence of distinct points of \(I\); those in \(W\) other than \(x\) are allowed. This proves (1). It also shows that at most one component can have the property in (2).

*Case 1: \(x\) is not a deleted vertex.* Then \(W\) contains no deleted vertex. By (S5) there is an open neighbourhood \(V\subseteq W\) of \(x\) such that any two points of \(I\cap V\) are joined by a path of \(K\) inside \(W\). Such a path consists of allowed vertices, so it is a path of \(K[T]\). Hence all allowed vertices in \(V\) lie in one component, which is \(Q_T(x)\); if \(x\) is an allowed vertex, it is one of them. For \(y\in V\cap L\), the point \(y\) lies in \(\Omega_T\) and is not a deleted vertex, and the allowed vertices near \(y\) lie in \(V\); so \(Q_T(y)=Q_T(x)\).

*Case 2: \(x\) is a deleted vertex.* Then \(I\subseteq L\), by (S3). Let \(V=W\cap L\), which we may take open in \(L\). Every \(y\in V\setminus\{x\}\) lies in \(\Omega_T\) and is not a deleted vertex, so by Case 1 the map \(q\) from \(V\setminus\{x\}\) to the set of components of \(K[T]\),
\[
q(y)=Q_T(y),
\]
is defined and locally constant. We show that \(q\) is constant on \(V_0\setminus\{x\}\) for some neighbourhood \(V_0\subseteq V\) of \(x\) in \(L\).

For every map \(c\) from the set of components to \(k\), the map \(c\circ q\) is locally constant on \(V\setminus\{x\}\). Since \(L\setminus\{x\}\) is connected and \(\check H^1(L;k)=0\), it extends to a locally constant map on \(V\) (Corollary 4.5 of the lesson on Čech cohomology). So:

> (E) for every \(c\), the map \(c\circ q\) is constant on \(V_c\setminus\{x\}\) for some neighbourhood \(V_c\) of \(x\).

Call a component *recurrent* if it is a value of \(q\) in every neighbourhood of \(x\).

If two different components are recurrent, let \(c\) be \(0\) on one and \(1\) on the other; this contradicts (E).

If no component is recurrent, we choose points \(y_1,y_2,\dots\) of \(V\setminus\{x\}\) converging to \(x\) with pairwise different values of \(q\): when \(y_1,\dots,y_n\) are chosen, each of their values is absent from some neighbourhood of \(x\), and \(y_{n+1}\) is taken in the intersection of these neighbourhoods with the ball of radius \(1/n\) around \(x\), which contains points of \(L\) other than \(x\). Let \(c\) be \(0\) on \(q(y_n)\) for even \(n\) and \(1\) on all other components; this contradicts (E).

So exactly one component \(A\) is recurrent. If \(q\) took values other than \(A\) in every neighbourhood of \(x\), the map \(c\) that is \(0\) on \(A\) and \(1\) elsewhere would contradict (E). Hence \(q=A\) on \(V_0\setminus\{x\}\) for some neighbourhood \(V_0\) of \(x\) in \(L\).

Every allowed vertex \(t\in V_0\) is a point of \(L\) other than \(x\), and by Case 1 it lies in \(Q_T(t)=q(t)=A\). All allowed vertices lie in \(L\), so the allowed vertices in a neighbourhood of \(x\) in \(Y\) whose trace on \(L\) is \(V_0\) belong to \(A\). So \(Q_T(x)=A\), and \(Q_T=A\) on \(V_0\). \(\blacksquare\)

## 3. A system of annuli

An *annulus* is an ordered pair \(\sigma=(\sigma^-,\sigma^+)\) of disjoint closed subsets of \(Y\), its *sides*, such that each side meets \(L\) and \(\sigma^-\cup\sigma^+\ne Y\). For annuli \(\sigma,\tau\) write
\[
\sigma<\tau\quad\Longleftrightarrow\quad\sigma^+\cup\tau^-=Y .
\]

**Lemma 3.1.**

1. If \(\sigma<\tau\), then \(\sigma^-\subseteq\tau^-\) and \(\tau^+\subseteq\sigma^+\).
2. The relation \(<\) is transitive, and \(\sigma<\sigma\) never holds. So the annuli of a *chain* \(\sigma_1<\sigma_2<\dots<\sigma_n\) are pairwise different.
3. The image \(g\sigma=(g\sigma^-,g\sigma^+)\) of an annulus under \(g\in H\) and its *reversal* \((\sigma^+,\sigma^-)\) are annuli, and \(\sigma<\tau\) implies \(g\sigma<g\tau\).

**Proof.** (1) \(\sigma^-\) is disjoint from \(\sigma^+\), so it lies in \(\tau^-\); likewise \(\tau^+\), disjoint from \(\tau^-\), lies in \(\sigma^+\). (2) If \(\sigma<\tau<\upsilon\), then \(\sigma^+\cup\upsilon^-\supseteq\sigma^+\cup\tau^-=Y\) by (1). And \(\sigma^+\cup\sigma^-\ne Y\). (3) \(g\) is a homeomorphism of \(Y\) that maps \(L\) to itself. \(\blacksquare\)

A chain \(\sigma_1<\dots<\sigma_n\) *goes from \(F\) to \(E\)*, for subsets \(F,E\) of \(Y\), if \(F\subseteq\sigma_1^-\) and \(E\subseteq\sigma_n^+\). Its *length* is \(n\).

**Theorem 3.2.** There is a set \(\mathcal A\) of annuli, mapped to itself by \(H\) and by reversal, such that:

1. for every \(\delta>0\), only finitely many annuli of \(\mathcal A\) have both sides of diameter at least \(\delta\);
2. for every closed set \(F\subseteq Y\), every \(x\in L\setminus F\) and every \(n\ge1\), there is a chain of length \(n\) in \(\mathcal A\) from \(F\) to a neighbourhood of \(x\) in \(Y\).

**Proof.** *Step 1: a consequence of (S2).* For all \(r,\varepsilon>0\), all but finitely many \(g\in H\) have a point \(b_g\in L\) such that
\[
\operatorname{diam}g\bigl(Y\setminus B(b_g,r)\bigr)<\varepsilon .
\]
Otherwise there are pairwise distinct \(g_n\) without such a point. Pass to a subsequence with \(g_n\to a\in L\) and \(g_n^{-1}\to b\in L\). By (S2), with the closed set \(Y\setminus B(b,r)\) and the ball of radius \(\varepsilon/3\) around \(a\), the point \(b\) serves as \(b_{g_n}\) for large \(n\).

*Step 2: the annuli.* Choose numbers \(r_1>r_2>\dots\) tending to \(0\), all smaller than a third of the diameter of \(L\), and let \(\varepsilon_i=2^{-i}\). Let \(E_i\subseteq H\) be the finite set of exceptions in Step 1 for \(r=r_i/4\) and \(\varepsilon=\varepsilon_i\). The finitely many maps in \(E_i\) are uniformly continuous on \(Y\), so there is \(s_i\) with \(0<s_i<r_i/4\) such that the image under each \(g\in E_i\) of each closed ball of radius \(s_i\) has diameter less than \(\varepsilon_i\). Choose finitely many points \(y_{ij}\in L\) such that the balls \(B(y_{ij},s_i/2)\) cover \(L\), and let \(\sigma_{ij}\) be the pair
\[
\begin{gathered}
\sigma_{ij}^-=Y\setminus B(y_{ij},r_i),\\
\sigma_{ij}^+=\{y\mid\rho(y,y_{ij})\le s_i\}.
\end{gathered}
\]
The two sides are closed and disjoint, and any point of one has distance more than \(3r_i/4\) from any point of the other. The side \(\sigma_{ij}^+\) contains \(y_{ij}\in L\). The side \(\sigma_{ij}^-\) meets \(L\): if \(u,v\in L\) have the largest possible distance, one of them has distance at least half the diameter of \(L\) from \(y_{ij}\), which is more than \(r_i\). The two sides do not cover \(Y\): otherwise their traces on \(L\) would be two disjoint nonempty closed sets covering the connected space \(L\). So \(\sigma_{ij}\) is an annulus.

Let \(\mathcal A\) be the set of all annuli \(g\sigma_{ij}\), \(g\in H\), and their reversals. It is mapped to itself by \(H\) and by reversal.

*Step 3: one side is small.* Every annulus \(g\sigma_{ij}\) has a side of diameter less than \(\varepsilon_i\). For \(g\in E_i\) it is \(g\sigma_{ij}^+\), by the choice of \(s_i\). For \(g\notin E_i\): the ball \(B(b_g,r_i/4)\) has diameter at most \(r_i/2\), so it cannot meet both sides of \(\sigma_{ij}\); the side that it does not meet lies in \(Y\setminus B(b_g,r_i/4)\), and its image under \(g\) has diameter less than \(\varepsilon_i\).

*Step 4: proof of (1).* Let \(\delta>0\). By Step 3 an annulus \(g\sigma_{ij}\) or its reversal with both sides of diameter at least \(\delta\) has \(\varepsilon_i\ge\delta\), which leaves finitely many pairs \((i,j)\). Fix one of them and write \(\sigma=\sigma_{ij}\). Suppose there are infinitely many different annuli \(g\sigma\) with both sides of diameter at least \(\delta\). Choose pairwise distinct \(g_n\) giving such annuli, and a subsequence with \(g_n\to a\in L\) and \(g_n^{-1}\to b\in L\). One of the two disjoint closed sides of \(\sigma\) does not contain \(b\), and by (S2) the diameter of its images under \(g_n\) tends to \(0\). This is a contradiction.

*Step 5: proof of (2).* Let \(F\) be closed and \(x\in L\setminus F\). Choose \(i\) so large that \(r_i+s_i/2\) is smaller than the distance from \(x\) to \(F\), if \(F\) is not empty, and \(j\) with \(\rho(x,y_{ij})<s_i/2\). Then \(F\subseteq\sigma_{ij}^-\), and \(\sigma_{ij}^+\) contains the ball \(B(x,s_i/2)\). This is a chain of length one.

Suppose a chain from \(F\) is given whose last annulus \(\sigma\) has \(B(x,\eta)\subseteq\sigma^+\). Choose \(i'\) with \(r_{i'}+s_{i'}/2<\eta\) and \(j'\) with \(\rho(x,y_{i'j'})<s_{i'}/2\), and let \(\tau=\sigma_{i'j'}\). Then \(B(y_{i'j'},r_{i'})\subseteq B(x,\eta)\subseteq\sigma^+\), so \(\sigma^+\cup\tau^-=Y\): the chain is prolonged by \(\tau\), and \(\tau^+\) contains a ball around \(x\). Repeating this gives chains of every length. \(\blacksquare\)

## 4. Annular depth

Fix a set \(\mathcal A\) as in Theorem 3.2. For \(F\subseteq Y\) and \(v\in Y\) let \(D(F,v)\) be the largest \(n\) such that there is a chain of length \(n\) in \(\mathcal A\) from \(F\) to \(\{v\}\); it is \(0\) if there is no such chain, and \(\infty\) if there are chains of every length. For a point \(u\) we write \(D(u,v)\) for \(D(\{u\},v)\).

**Theorem 4.1.**

1. \(D(gF,gv)=D(F,v)\) for all \(g\in H\).
2. If \(F\) contains a point of \(H\) and \(v\in H\), then \(D(F,v)\) is finite.
3. If \(F\) is closed, \(x\in L\setminus F\) and \(N\ge1\), there is a neighbourhood \(V_N\) of \(x\) in \(Y\) with \(D(F,v)\ge N\) for all \(v\in V_N\).
4. If \(F\subseteq F'\), then \(D(F',v)\le D(F,v)\).

**Proof.** (1) \(g\) maps chains from \(F\) to \(\{v\}\) to chains from \(gF\) to \(\{gv\}\), and \(g^{-1}\) maps them back (Lemma 3.1(3)).

(2) Let \(h\in F\cap H\). The points \(h\) and \(v\) are not in the closed set \(L\); let \(\delta>0\) be smaller than their distances from \(L\). Let \(\sigma_1<\dots<\sigma_n\) be a chain from \(F\) to \(\{v\}\). By Lemma 3.1(1), \(h\in\sigma_1^-\subseteq\sigma_i^-\) and \(v\in\sigma_n^+\subseteq\sigma_i^+\) for every \(i\). Each side also meets \(L\), so both sides of every \(\sigma_i\) have diameter at least \(\delta\). By Theorem 3.2(1) there are finitely many such annuli, and the annuli of a chain are pairwise different. So \(n\) is bounded.

(3) By Theorem 3.2(2) there is a chain of length \(N\) from \(F\) to a neighbourhood \(V_N\) of \(x\); it goes from \(F\) to \(\{v\}\) for every \(v\in V_N\).

(4) A chain from \(F'\) to \(\{v\}\) goes from \(F\) to \(\{v\}\). \(\blacksquare\)

## 5. Exercises

**5.1.** Let \(L\) be a circle and \(x\in L\). Give a locally constant map on \(V\setminus\{x\}\), for a small open arc \(V\) around \(x\), that does not extend to a locally constant map on \(V\). Which assumption of this lesson fails for the circle?

**5.2.** Show that in Theorem 2.1 the set \(\Omega_T\) contains every point of \(L\) if \(I\setminus T\) is finite.

**5.3.** Show that \(D(F,v)\ge1\) implies \(v\notin F\), and that \(D(u,v)=D(v,u)\) for points \(u,v\in Y\). Which property of the set \(\mathcal A\) is used for the second statement?

**5.4.** Let \(u\in H\). Show that \(D(u,v)\to\infty\) as \(v\in H\) tends to infinity.

## 6. Solutions

**5.1.** The set \(V\setminus\{x\}\) consists of two open arcs; the map that is \(0\) on one and \(1\) on the other is locally constant and has no locally constant extension to \(V\). The circle is connected without cut points and has dimension one, but its first Čech cohomology with coefficients in \(k\) is not zero (Corollary 4.3 of the lesson on Čech cohomology), so (S7) fails.

**5.2.** A finite set has no sequence of pairwise distinct points, so \((I\setminus T)'\) is empty.

**5.3.** If \(F\subseteq\sigma_1^-\) and \(v\in\sigma_n^+\subseteq\sigma_1^+\), then \(v\notin F\), because the sides of \(\sigma_1\) are disjoint. For the symmetry, let \(\sigma_1<\dots<\sigma_n\) be a chain from \(\{u\}\) to \(\{v\}\), and let \(\bar\sigma_i\) be the reversal of \(\sigma_i\). Then \(\bar\sigma_n<\dots<\bar\sigma_1\): indeed \(\bar\sigma_{i+1}^+\cup\bar\sigma_i^-=\sigma_{i+1}^-\cup\sigma_i^+=Y\). This chain goes from \(\{v\}\) to \(\{u\}\), and it lies in \(\mathcal A\) because \(\mathcal A\) is mapped to itself by reversal; this is the property used. So \(D(v,u)\ge D(u,v)\), and equality follows by symmetry.

**5.4.** Suppose not: there are \(N\) and pairwise distinct \(v_n\in H\) with \(D(u,v_n)<N\). A subsequence converges to a point \(x\in L\), and \(x\notin\{u\}\). By Theorem 4.1(3), \(D(u,v)\ge N\) for all \(v\) near \(x\), a contradiction.

## References

- [OpenAI-S] OpenAI, *The Singer conjecture in dimension four*, OpenAI Math Release preprint, 25 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/The-Singer-conjecture-in-dimension-four-September-25-2026
- [Bowditch 3] B. H. Bowditch, *A topological characterisation of hyperbolic groups*, Journal of the American Mathematical Society 11 (1998), Sections 6 and 7. Author's version: http://homepages.warwick.ac.uk/~masgak/papers/bhb-topchar.pdf
