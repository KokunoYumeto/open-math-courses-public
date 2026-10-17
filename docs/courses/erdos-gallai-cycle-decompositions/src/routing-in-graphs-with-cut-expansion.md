# Routing in graphs with cut expansion

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

In the proof of the cycle decomposition theorem, paths are closed into cycles and the cycles of smaller graphs are lifted to the original graph. Both operations need many connecting paths at once: short, pairwise edge-disjoint, avoiding prescribed vertices, and with disjoint inner vertices whenever several of them become parts of one cycle. This lesson proves that a graph with good cut expansion supplies all of them simultaneously. The proof encodes paths as hypergraph edges and applies Haxell's condition from [Disjoint representatives in hypergraphs](disjoint-representatives-in-hypergraphs.md); the method of encoding and of verifying the condition by ball growth is that of Bucić and Montgomery [BM, Section 2].

All logarithms are to base two.

## 1. Cut expansion

For a graph \(P\) and \(U\subseteq V(P)\), let \(\partial_PU\) be the set of edges with one end in \(U\) and the other outside \(U\).

**Definition 1.1.** A graph \(P\) of order \(r\) has *cut expansion at least \(h\)* if
\[
|\partial_PU|\ge h\min\{|U|,\,r-|U|\}
\]
for every \(U\subseteq V(P)\).

**Lemma 1.2.** Let \(P\) have order \(r\ge2\) and cut expansion at least \(h>0\). Then every vertex has degree at least \(h\), so \(h\le r-1<r\), and \(P\) is connected.

*Proof.* For \(U=\{v\}\) the definition gives \(d_P(v)\ge h\); a vertex of a simple graph has at most \(r-1\) neighbours. If \(P\) were disconnected, a component \(U\) would have \(\partial_PU=\varnothing\) although \(\min\{|U|,r-|U|\}\ge1\). \(\square\)

## 2. Demands, teams and the routing theorem

A *demand* \(p\) asks for a path between two distinct vertices \(x_p,y_p\), its *ends*. Demands are indexed, so several demands may ask for the same pair. A vertex occurs in at most \(k\) demands if it is an end of at most \(k\) of them. A partition of the demands into *teams* is given; \(c(p)\) denotes the team of \(p\). Each demand also carries a set \(Z_p\) of *forbidden* vertices, which its path must avoid as inner vertices; \(Z_p\) may contain \(x_p\) or \(y_p\).

**Theorem 2.1** (routing). Let \(P\) be a graph of order \(r\ge2\) with cut expansion at least \(h>0\), and put
\[
\begin{gathered}
g=\Bigl\lceil\frac{8r}h\log(2r)\Bigr\rceil,\\
\ell=2g\bigl(1+\lceil\log r\rceil\bigr).
\end{gathered}
\]
Let \(\mathcal D\) be a finite set of demands in \(P\), in which every vertex occurs in at most \(k\ge1\) demands. Let the teams have at most \(b\ge1\) demands each, and let every forbidden set have at most \(z\ge0\) vertices. If
\[
h\ge128\bigl(\ell^2(k+b)+z\bigr),
\]
then there are paths \(Q_p\) from \(x_p\) to \(y_p\), one for every \(p\in\mathcal D\), such that:

1. each \(Q_p\) has length at most \(\ell\) and no inner vertex in \(Z_p\);
2. the paths \(Q_p\) are pairwise edge-disjoint;
3. paths of the same team have pairwise disjoint sets of inner vertices.

The proof of [OpenAI-EG] obtains the same conclusion under \(h\ge64(\ell^2(k+b)+z)\), using the sharper hypergraph condition of Aharoni and Haxell. The constant plays no role in the later lessons: in every application, \(h\) exceeds \(\ell^2(k+b)+z\) by a positive power of the scale.

**Corollary 2.2** (length of the paths). Under the hypotheses of Theorem 2.1,
\[
\ell\le108\,\frac rh\,(\log r)^2 .
\]

*Proof.* By Lemma 1.2, \(h<r\), and \(r\ge2\). Hence \(\frac rh\log(2r)\ge1\), and
\[
g\le\frac{8r}h\log(2r)+1\le\frac{9r}h\log(2r).
\]
Also \(\log(2r)=1+\log r\le2\log r\) and \(1+\lceil\log r\rceil\le2+\log r\le3\log r\). Multiplying, \(\ell\le2\cdot\frac{9r}h\cdot2\log r\cdot3\log r\). \(\square\)

## 3. Proof of Theorem 2.1

If \(\mathcal D\) is empty there is nothing to prove; let it be nonempty.

**3.1. Paths as hypergraph edges.** Take as ground set the disjoint union of \(E(P)\) and the *tokens* \((v,c)\), where \(v\in V(P)\) and \(c\) is a team. To a path \(Q\) serving demand \(p\) assign the set \(R_p(Q)\) consisting of the edges of \(Q\) and the tokens \((v,c(p))\) of the inner vertices \(v\) of \(Q\). A path of length \(t\ge1\) has \(t\) edges and \(t-1\) inner vertices, so \(|R_p(Q)|=2t-1\). Let \(\mathcal H_p\) be the hypergraph of all sets \(R_p(Q)\), where \(Q\) runs over the paths from \(x_p\) to \(y_p\) of length at most \(\ell\) with no inner vertex in \(Z_p\). Its edges have at most \(2\ell-1\) elements.

Disjoint representatives of \((\mathcal H_p)_{p\in\mathcal D}\) give paths with the three required properties: disjointness of the edge parts gives (2), and two paths of the same team \(c\) sharing an inner vertex \(v\) would share the token \((v,c)\), which gives (3). Property (1) holds by the definition of \(\mathcal H_p\).

By Theorem 1.1 of [Disjoint representatives in hypergraphs](disjoint-representatives-in-hypergraphs.md) with \(s=2\ell-1\), it suffices to show: for every nonempty \(I\subseteq\mathcal D\), the hypergraph \(\bigcup_{p\in I}\mathcal H_p\) has a matching with more than \((4\ell-3)(|I|-1)\) edges. Suppose this fails for some nonempty \(I\), and let \(\mathcal M\) be a matching of \(\bigcup_{p\in I}\mathcal H_p\) with the largest number of edges. Then
\[
|\mathcal M|\le(4\ell-3)(|I|-1)<4\ell|I| .
\]
We derive a contradiction.

**3.2. What the matching uses.** Let \(F\subseteq E(P)\) be the set of graph edges occurring in members of \(\mathcal M\), and for every team \(c\) let \(Y_c\) be the set of vertices \(v\) such that the token \((v,c)\) occurs in a member of \(\mathcal M\). A member of \(\mathcal M\) contains at most \(\ell\) graph edges and at most \(\ell-1\) tokens, so
\[
|F|<4\ell^2|I|,\qquad\sum_c|Y_c|<4\ell^2|I| .
\]
These bounds count every member of \(\mathcal M\), whichever demand it serves.

For a team \(c\) let \(m_c\le b\) be the number of demands of \(I\) in \(c\). Then
\[
\sum_{p\in I}|Y_{c(p)}|=\sum_cm_c|Y_c|<4b\ell^2|I| .
\]
Let \(I_1\) be the set of \(p\in I\) with \(|Y_{c(p)}|\le8b\ell^2\). Each demand of \(I\setminus I_1\) contributes more than \(8b\ell^2\) to the last sum, so \(|I\setminus I_1|<|I|/2\) and \(|I_1|>|I|/2\).

Choose a set \(I_2\subseteq I_1\) of demands whose end pairs are pairwise disjoint, maximal under inclusion. Every demand of \(I_1\) shares an end with some demand of \(I_2\). The two ends of a demand of \(I_2\) are ends of at most \(2k\) demands in total, so \(|I_1|\le2k|I_2|\) and
\[
|I_2|>\frac{|I|}{4k}.
\]
Finally, every demand has two ends and every vertex is an end of at most \(k\) demands, so
\[
2|I|\le kr .
\]

**3.3. A small ball at one end of each selected demand.** For \(p\in I_2\) put
\[
W_p=(Z_p\cup Y_{c(p)})\setminus\{x_p,y_p\},
\]
and let \(P_p\) arise from \(P\) by deleting the edges of \(F\) and then the vertices of \(W_p\). Both ends of \(p\) are vertices of \(P_p\). The hypothesis gives \(128(\ell^2(k+b)+z)\ge4z+32b\ell^2\), so
\[
|W_p|\le z+8b\ell^2\le\frac h4 .
\]
Put \(T=\ell/2=g(1+\lceil\log r\rceil)\), an integer, and write \(\mathrm{Ball}_{P_p}(v,t)\) for the set of vertices at distance at most \(t\) from \(v\) in \(P_p\).

Suppose that both \(\mathrm{Ball}_{P_p}(x_p,T)\) and \(\mathrm{Ball}_{P_p}(y_p,T)\) have more than \(r/2\) vertices. Then they share a vertex, and there is a walk from \(x_p\) to \(y_p\) in \(P_p\) of length at most \(2T=\ell\). Deleting closed subwalks gives a path \(Q\) of length at most \(\ell\). It uses no edge of \(F\). Its inner vertices differ from \(x_p\) and \(y_p\) and are vertices of \(P_p\), so they avoid \(Z_p\) and \(Y_{c(p)}\). Therefore \(R_p(Q)\) is an edge of \(\mathcal H_p\) whose graph edges are not in \(F\) and whose tokens \((v,c(p))\) have \(v\notin Y_{c(p)}\): it is disjoint from every member of \(\mathcal M\). Adding it to \(\mathcal M\) gives a larger matching of \(\bigcup_{p\in I}\mathcal H_p\), which is impossible.

So for every \(p\in I_2\) we can choose an end \(s_p\in\{x_p,y_p\}\) with
\[
|\mathrm{Ball}_{P_p}(s_p,T)|\le\frac r2 .
\]
Let \(S\) be the set of these *roots*. They are distinct, since the end pairs in \(I_2\) are disjoint; for \(s\in S\) write \(p(s)\) for the demand with \(s=s_{p(s)}\). Thus \(|S|=|I_2|\).

**3.4. Growing unions of balls.** For a nonempty \(A\subseteq S\) and an integer \(t\ge0\) put
\[
B_t(A)=\bigcup_{s\in A}\mathrm{Ball}_{P_{p(s)}}(s,t).
\]
Each ball is taken in the graph of its own root.

**Lemma 3.1** (growth). If \(0<|B_t(A)|\le r/2\) and \(|F|\le h|B_t(A)|/4\), then
\[
|B_{t+1}(A)|\ge\Bigl(1+\frac h{2r}\Bigr)|B_t(A)| .
\]

*Proof.* Write \(B=B_t(A)\), and for every \(v\in B\) choose a root \(s(v)\in A\) with \(v\in\mathrm{Ball}_{P_{p(s(v))}}(s(v),t)\). Let \(vw\) be an edge of \(P\) with \(v\in B\) and \(w\notin B\). If \(vw\notin F\) and \(w\notin W_{p(s(v))}\), then \(vw\) is an edge of \(P_{p(s(v))}\), so \(w\in B_{t+1}(A)\setminus B\). At a fixed \(v\), at most \(|W_{p(s(v))}|\le h/4\) boundary edges end in that forbidden set, because \(P\) is simple. Since \(|B|\le r/2\), cut expansion gives \(|\partial_PB|\ge h|B|\). So at least
\[
h|B|-\frac h4|B|-|F|\ge\frac h2|B|
\]
boundary edges lead to vertices of \(B_{t+1}(A)\setminus B\). A vertex receives at most \(r\) of them, so at least \(h|B|/(2r)\) new vertices are reached. \(\square\)

**Lemma 3.2** (growth over \(g\) steps). If \(|B_t(A)|\ge1\) and \(|F|\le h|B_t(A)|/4\), then \(|B_{t+g}(A)|>r/2\).

*Proof.* The sets \(B_t(A)\) increase with \(t\). If \(|B_t(A)|>r/2\), we are done. Otherwise suppose \(|B_{t+g}(A)|\le r/2\). Then every \(t'\) with \(t\le t'<t+g\) satisfies \(|B_t(A)|\le|B_{t'}(A)|\le r/2\), so Lemma 3.1 applies at each of these \(g\) steps, and
\[
|B_{t+g}(A)|\ge\Bigl(1+\frac h{2r}\Bigr)^g .
\]
For \(0\le u\le1\), concavity gives \(\log(1+u)\ge u\). With \(u=h/(2r)<1\) and \(g\ge8(r/h)\log(2r)\),
\[
\Bigl(1+\frac h{2r}\Bigr)^g\ge2^{gh/(2r)}\ge(2r)^4>\frac r2 ,
\]
a contradiction. \(\square\)

**3.5. Halving the roots.** First, \(B_0(S)=S\), and
\[
|F|<4\ell^2|I|<16k\ell^2|S|\le\frac h4|S|,
\]
since \(h\ge128k\ell^2\). By Lemma 3.2, \(|B_g(S)|>r/2\).

Let \(A\subseteq S\) have \(|A|\ge2\) and \(|B_t(A)|>r/2\) for some \(t\). Split \(A\) into two nonempty halves whose sizes differ by at most one. Their unions of balls of radius \(t\) together form \(B_t(A)\), so one half \(A'\) has \(|B_t(A')|>r/4\), and \(|A'|\le\lceil|A|/2\rceil\). By the endpoint count \(2|I|\le kr\),
\[
\begin{aligned}
|F|&<4\ell^2|I|\le2k\ell^2r\\
&\le\frac{hr}{64}<\frac h4|B_t(A')| ,
\end{aligned}
\]
using \(h\ge128k\ell^2\). Lemma 3.2 gives \(|B_{t+g}(A')|>r/2\).

Start with \(A=S\) at radius \(g\) and repeat the halving until one root remains. After \(j\) halvings at most \(\lceil|S|/2^j\rceil\) roots remain, so at most \(\lceil\log|S|\rceil\) halvings are needed. Since \(|S|\le r\), the final single root \(s\) satisfies
\[
\bigl|\mathrm{Ball}_{P_{p(s)}}(s,t^*)\bigr|>\frac r2
\]
for some \(t^*\le g(1+\lceil\log r\rceil)=T\). As balls grow with the radius, this contradicts the choice of the root \(s\) in Section 3.3.

So the matching condition holds for every nonempty \(I\), and Haxell's condition gives disjoint representatives. Their paths satisfy (1)–(3). \(\square\)

## 4. Exercises

**4.1** (easy). Show that the complete graph on \(r\) vertices has cut expansion at least \(r/2\).

**4.2** (medium). Let \(P\) have order \(r\ge2\) and cut expansion at least \(h>0\). Show that any two vertices of \(P\) are joined by a path of length at most \(2\lceil(r/h)\log r\rceil\).

**4.3** (medium). Show that if the tokens are omitted from the encoding of Section 3.1, the same argument still yields pairwise edge-disjoint paths of length at most \(\ell\), but two paths of one team may share inner vertices. Give an example of a cycle formed from paths of one team that fails to be a cycle when two of them share an inner vertex.

**4.4** (medium). Where does the proof use that \(P\) is simple? Point to both places.

## 5. Solutions

**4.1.** For \(U\) with \(u\) vertices, \(|\partial U|=u(r-u)\). This is the product of \(\min\{u,r-u\}\) and \(\max\{u,r-u\}\), and the larger of \(u\) and \(r-u\) is at least \(r/2\).

**4.2.** For a vertex \(v\), let \(B_t\) be its ball of radius \(t\). If \(|B_t|\le r/2\), the boundary of \(B_t\) has at least \(h|B_t|\) edges, and a vertex outside receives at most \(r\) of them, so \(|B_{t+1}|\ge(1+h/r)|B_t|\ge2^{h/r}|B_t|\), using \(\log(1+u)\ge u\) for \(0\le u\le1\). Put \(t_0=\lceil(r/h)\log r\rceil\). If \(|B_{t_0}|\le r/2\), all smaller balls are at most as large, and \(|B_{t_0}|\ge2^{t_0h/r}\ge r\), a contradiction. So the balls of radius \(t_0\) around any two vertices have more than \(r/2\) vertices each and meet, which gives a walk, and hence a path, of length at most \(2t_0\).

**4.3.** Without tokens, the hypergraph edges are the edge sets of the paths, with at most \(\ell\) elements; the same proof with \(Y_c=\varnothing\) works and gives edge-disjoint paths. Example: let a closed walk consist of a path from \(v_1\) to \(u_2\), a connecting path from \(u_2\) to \(v_2\), a path from \(v_2\) to \(u_1\) and a connecting path from \(u_1\) to \(v_1\), where the two connecting paths form one team. If they share an inner vertex, the closed walk visits it twice and is not a cycle.

**4.4.** In Lemma 1.2 (a vertex has at most \(r-1\) neighbours) and in Lemma 3.1 (a vertex \(v\) has at most one edge to each forbidden vertex, so at most \(|W_{p(s(v))}|\) boundary edges at \(v\) end in the forbidden set, and a new vertex receives at most \(r\) boundary edges).

## References

- [OpenAI-EG] OpenAI, *A linear cycle-and-edge decomposition of every graph*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026
- [BM] M. Bucić and R. Montgomery, *Towards the Erdős–Gallai cycle decomposition conjecture*, Advances in Mathematics 437 (2024), 109434; arXiv:2211.07689. https://arxiv.org/abs/2211.07689
