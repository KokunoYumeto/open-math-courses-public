# Embedding sparse graphs in random graphs

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Graph decompositions at the expectation threshold](graph-decompositions-at-the-expectation-threshold.md) splits a graph \(H\) into a bounded number of pieces, each of which appears in \(G(n,p)\) once \(p\) is a constant multiple of the integral expectation threshold of \(H\). This lesson proves the three embedding results used there, following OpenAI [OpenAI-GD]:

- **Proposition 4.1** (neighbourhood transfer): bipartite pieces between a small vertex set \(Y\) and its complement, whose edges lie in a *typical* graph, embed in a slightly denser random graph with \(Y\) fixed;
- **Proposition 5.1**: graphs of small degeneracy and maximum degree at most \(n^{2/3}\), on at most \(n/4\) non-isolated vertices, embed at every density allowed by their degeneracy;
- **Proposition 6.1**: star forests on at most \(n/100\) non-isolated vertices embed at a constant multiple of their own expectation threshold.

The first is new; the other two adapt the degeneracy splitting and centre-testing arguments of Ascoli, He, Park and Talagrand [AHPT]. The tools are Hoeffding's inequality, Hall's theorem, the Paley–Zygmund inequality and a compression lemma for families of small sets (Lemma 3.1).

## 1. Thresholds of graphs

All graphs are finite and simple, and copies need not be induced. For a graph \(J\) on at most \(n\) vertices let
\[
p_{\mathrm c}(J;n)=\min\{p\in[0,1]:\mathbb P(G(n,p)\text{ contains a copy of }J)\ge\tfrac12\},
\]
and \(p_{\mathrm c}(J;n)=0\) if \(J\) has no edge; for graphs with an edge this is \(p_{\mathrm c}(n,J)\) of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), and the minimum exists by Lemma 3.2 there. Let \(\mathcal F_J\) be the family of edge sets on \([n]\) that contain a copy of \(J\), and let \(q(J;n)\) be the largest \(p\in[0,1]\) for which \(\mathcal F_J\) has a cover of cost at most \(\frac12\), with \(q(J;n)=0\) if \(J\) has no edge. The largest value exists because there are finitely many covers, each with a continuous nondecreasing cost; \(q(J;n)=q(\mathcal F_J)\) is the integral expectation threshold. If \(J\subseteq H\), then \(\mathcal F_H\subseteq\mathcal F_J\), every cover of \(\mathcal F_J\) covers \(\mathcal F_H\), and
\[
q(J;n)\le q(H;n),\qquad p_{\mathrm c}(J;n)\le p_{\mathrm c}(H;n).\tag{1.1}
\]
Isolated vertices do not matter: a copy of the rest of \(J\) extends to a copy of \(J\) because \(J\) has at most \(n\) vertices. Write \(V_+(J)\) for the set of vertices of positive degree.

The *degeneracy* \(\operatorname{degen}(H)\) is the largest minimum degree of a nonempty subgraph of \(H\). If \(d=\operatorname{degen}(H)\), removing a vertex of degree at most \(d\) repeatedly and placing it last gives an order of the vertices in which every vertex has at most \(d\) earlier neighbours; counting each edge at its later endpoint gives
\[
|E(J)|\le d\,|V(J)|\qquad\text{for every subgraph }J\subseteq H.\tag{1.2}
\]
Conversely, if some order has at most \(d'\) earlier neighbours at every vertex, the last vertex of any subgraph in this order has degree at most \(d'\), so \(\operatorname{degen}(H)\le d'\).

**Lemma 1.1.** If \(H\) has an edge, at most \(n\) vertices and degeneracy \(d\), then
\[
q(H;n)\ge\frac1{n(n-1)}\qquad\text{and}\qquad q(H;n)\ge\tfrac12\,n^{-2/d}.
\]

**Proof.** The single edges cover \(\mathcal F_H\), at cost \(\binom n2p\), which is \(\frac12\) at \(p=1/(n(n-1))\). For the second bound take a subgraph \(F\) of minimum degree \(d\), with \(v\le n\) vertices and \(a\ge dv/2\ge1\) edges. Its copies cover \(\mathcal F_H\), and there are at most \(n^v\) of them, so the cost at \(p_0=2^{-1/a}n^{-v/a}\in(0,1)\) is at most \(n^vp_0^a=\frac12\). Finally \(p_0\ge\frac12n^{-2/d}\), since \(2^{-1/a}\ge\frac12\) and \(v/a\le2/d\). \(\square\)

## 2. Probabilistic tools

We use Hoeffding's inequality in the form of Theorem 2.2 of [Concentration and the discrete cube](course:the-gaussian-moat-problem/concentration-and-the-discrete-cube#2-hoeffding-s-inequality): if \(Z_1,\dots,Z_m\) are independent with values in \([0,1]\) and \(S=\sum_jZ_j\), then \(\mathbb P(S-\mathbb ES\ge t)\le\mathrm e^{-2t^2/m}\) for \(t\ge0\); applied to \(1-Z_j\), also \(\mathbb P(S-\mathbb ES\le-t)\le\mathrm e^{-2t^2/m}\). We use Hall's theorem in the form of Lemma 2.1 of [Contracting averages and sparse assignments](course:amenability-and-unitarizability/contracting-averages-and-sparse-assignments#2-hall-s-theorem-and-its-countable-form): if every vertex \(x\) of a finite set \(X\) has a set \(N(x)\) of admissible images and \(|\bigcup_{x\in F}N(x)|\ge|F|\) for every \(F\subseteq X\), there is an injective choice of admissible images for all of \(X\).

**Lemma 2.1** (Paley–Zygmund). Let \(Z\ge0\) with \(0<\mathbb EZ^2<\infty\), and \(0\le\theta\le1\). Then \(\mathbb P(Z>\theta\,\mathbb EZ)\ge(1-\theta)^2(\mathbb EZ)^2/\mathbb EZ^2\).

**Proof.** \(\mathbb EZ=\mathbb E[Z\mathbf 1\{Z\le\theta\mathbb EZ\}]+\mathbb E[Z\mathbf 1\{Z>\theta\mathbb EZ\}]\le\theta\,\mathbb EZ+(\mathbb EZ^2)^{1/2}\,\mathbb P(Z>\theta\mathbb EZ)^{1/2}\) by the Cauchy–Schwarz inequality. \(\square\)

## 3. Compressing requirements

For a family \(\mathcal Q\) of subsets of a finite set \(Y\), a set \(S\subseteq Y\) *satisfies* \(\mathcal Q\) if it contains a member of \(\mathcal Q\). For \(r\in(0,1)\) let
\[
f_{\mathcal Q}(S)=\mathbb P(S\cup Z\text{ satisfies }\mathcal Q),\qquad Z\sim\mu_r\text{ on }Y.\tag{3.1}
\]
The function \(f_{\mathcal Q}\) is nondecreasing in \(S\).

**Lemma 3.1** (compression after a random extension; OpenAI). Let \(Y\) be finite, \(r\in(0,1)\) and \(s\ge1\) an integer. For every nonempty family \(\mathcal R\) of subsets \(T\subseteq Y\) with \(1\le|T|\le s\) there is a nonempty \(\mathcal Q\subseteq\mathcal R\) with \(|\mathcal Q|\le\lceil2r^{-s}\rceil\) such that \(f_{\mathcal Q}(S)\ge\frac12\) for every \(S\) that satisfies \(\mathcal R\).

**Proof.** Start with \(\mathcal Q=\varnothing\). While some \(T\in\mathcal R\) has \(\mathbb P(Z\text{ satisfies }\mathcal Q\mid Z\supseteq T)<\frac12\), add such a \(T\) to \(\mathcal Q\). Each addition increases \(\mathbb P(Z\text{ satisfies }\mathcal Q)\) by \(\mathbb P(Z\supseteq T,\ Z\text{ does not satisfy }\mathcal Q)>\frac12r^{|T|}\ge\frac12r^s\), so there are fewer than \(2r^{-s}\) additions; a set once added is never chosen again, since then the conditional probability is \(1\). The first step adds a set, because \(\mathcal R\neq\varnothing\) and \(Z\) never satisfies the empty family. At the end, \(\mathbb P(Z\text{ satisfies }\mathcal Q\mid Z\supseteq T)\ge\frac12\) for every \(T\in\mathcal R\). Given \(Z\supseteq T\), the set \(Z\) has the law of \(T\cup Z'\) with \(Z'\sim\mu_r\), so \(f_{\mathcal Q}(T)\ge\frac12\), and \(f_{\mathcal Q}(S)\ge f_{\mathcal Q}(T)\) for \(S\supseteq T\). \(\square\)

## 4. Neighbourhood transfer

Throughout this section and the next, \(\log\) is the natural logarithm, \(k_0=2^{75}\), and the parameters satisfy
\[
0<r<1,\qquad s\ge1\text{ an integer},\qquad s\le10\log n,\qquad r^s\ge n^{-1/100}.\tag{4.1}
\]

**Proposition 4.1** (neighbourhood transfer; OpenAI). There is an absolute integer \(N_1\) such that for every \(n\ge N_1\) and all \(r,s\) satisfying (4.1) there is a family \(\mathcal D=\mathcal D(n,r,s)\) of graphs on \([n]\) with \(\mu_r(\mathcal D)\ge1-\frac1{k_0}\) and the following property. Let \(Y\subseteq[n]\) with \(|Y|\le n^{2/3}\), and let \(J\) be a graph with vertices in \([n]\) such that every edge of \(J\) joins \(Y\) to \([n]\setminus Y\), \(E(J)\subseteq E(G)\) for some \(G\in\mathcal D\), at most \(n/8\) vertices outside \(Y\) have positive degree in \(J\), and all those degrees are at most \(s\). Then
\[
p_{\mathrm c}(J;n)\le r_*:=1-(1-r)^{32}\le32r.
\]

Here \(\mu_r\) is the law of the edge set of \(G(n,r)\). The family \(\mathcal D\) does not depend on \(Y\) or \(J\); this is what allows the pieces in [Graph decompositions at the expectation threshold](graph-decompositions-at-the-expectation-threshold.md) to be chosen after \(\mathcal D\).

**Proof.** *Tests.* A *test* is a pair \((Y,\mathcal Q)\) with \(Y\subseteq[n]\), \(|Y|\le n^{2/3}\), and \(\mathcal Q\) a nonempty family of sets \(T\subseteq Y\) with \(1\le|T|\le s\) and \(|\mathcal Q|\le\lceil2r^{-s}\rceil\). Let \(m=n-|Y|\), \(\tau=1-(1-r)^2\), and let \(x(\mathcal Q)\) and \(x_*(\mathcal Q)\) be the probabilities that a \(\mu_\tau\)-random and a \(\mu_{r_*}\)-random subset of \(Y\) satisfy \(\mathcal Q\). Both are at least \(r^s\ge n^{-1/100}\), because each contains a fixed \(T\in\mathcal Q\) with probability at least \(r^{|T|}\). Let \(\mathcal D\) be the set of graphs \(G\) on \([n]\) such that for every test
\[
\sum_{w\in[n]\setminus Y}f_{\mathcal Q}\bigl(N_G(w)\cap Y\bigr)\le2x(\mathcal Q)\,m.\tag{4.2}
\]
Say that a graph \(G_*\) is *rich* if for every test
\[
\bigl|\{a\in[n]\setminus Y:N_{G_*}(a)\cap Y\text{ satisfies }\mathcal Q\}\bigr|\ge\tfrac34x_*(\mathcal Q)\,m.\tag{4.3}
\]

*Concentration.* Fix a test. For \(G\sim G(n,r)\), the sets \(N_G(w)\cap Y\), \(w\notin Y\), are independent \(\mu_r\)-random subsets of \(Y\), since they are determined by disjoint sets of edges. So the summands in (4.2) are independent, lie in \([0,1]\), and have mean \(x(\mathcal Q)\): by Lemma 1.2 of [Random sets, covers and expectation thresholds](random-sets-covers-and-expectation-thresholds.md), the union of \(N_G(w)\cap Y\) and an independent \(\mu_r\)-random set has law \(\mu_\tau\). For \(n\ge8\), \(m\ge n/2\). Hoeffding's inequality with \(t=x(\mathcal Q)m\) bounds the probability that (4.2) fails by \(\exp(-2x(\mathcal Q)^2m)\le\exp(-n^{98/100})\). Likewise, for \(G_*\sim G(n,r_*)\), the indicators in (4.3) are independent with mean \(x_*(\mathcal Q)\), and (4.3) fails with probability at most \(\exp(-x_*(\mathcal Q)^2m/8)\le\exp(-n^{98/100}/16)\).

*Counting tests.* There are at most \((n^{2/3}+1)n^{n^{2/3}}\le n^{n^{2/3}+1}\) sets \(Y\). Given \(Y\), there are at most \((n+1)^s\) sets \(T\) and \(|\mathcal Q|\le\lceil2r^{-s}\rceil\le2n^{1/100}+1\), so at most \((n+2)^{s(2n^{1/100}+1)}\) families \(\mathcal Q\). The logarithm of the number of tests is therefore at most
\[
(n^{2/3}+1)\log n+10\log n\,(2n^{1/100}+1)\log(n+2),
\]
which is smaller than \(n^{98/100}/32\) for large \(n\). Choose \(N_1\ge8\) so that for \(n\ge N_1\) the number of tests times \(\exp(-n^{98/100}/16)\) is at most \(\frac1{k_0}\). Then \(\mu_r(\mathcal D)\ge1-\frac1{k_0}\), and \(G(n,r_*)\) is rich with probability at least \(1-\frac1{k_0}\ge\frac12\).

*Amplification.* A \(\mu_{r_*}\)-random set is the union of \(16\) independent \(\mu_\tau\)-random sets, as \(1-(1-\tau)^{16}=r_*\). Satisfying \(\mathcal Q\) is preserved by enlarging the set, so
\[
x_*(\mathcal Q)\ge1-\bigl(1-x(\mathcal Q)\bigr)^{16}.\tag{4.4}
\]

*Hall's condition.* Let \(Y\), \(J\) and \(G\in\mathcal D\) be as in the statement, and let \(G_*\) be rich. Let \(W\) be the set of vertices of \(J\) outside \(Y\) of positive degree, and call \(a\in[n]\setminus Y\) *usable* for \(w\in W\) if \(N_J(w)\subseteq N_{G_*}(a)\). Let \(\varnothing\neq U\subseteq W\), \(\mathcal R=\{N_J(w):w\in U\}\), and let \(\mathcal Q\subseteq\mathcal R\) be given by Lemma 3.1; \((Y,\mathcal Q)\) is a test. For \(w\in U\), \(N_G(w)\cap Y\supseteq N_J(w)\), so \(f_{\mathcal Q}(N_G(w)\cap Y)\ge\frac12\), and (4.2) gives
\[
\tfrac12|U|\le\sum_{w\in U}f_{\mathcal Q}(N_G(w)\cap Y)\le2x\,m,\qquad x=x(\mathcal Q).
\]
Every vertex \(a\) counted in (4.3) contains some \(N_J(w)\), \(w\in U\), in its neighbourhood, so it is usable for that \(w\). If \(x\le\frac1{16}\), (4.4) and \(1-\mathrm e^{-y}\ge y/2\) for \(0\le y\le1\) give \(x_*\ge1-\mathrm e^{-16x}\ge8x\), so there are at least \(6xm\ge|U|\) usable vertices for \(U\). If \(x>\frac1{16}\), then \(x_*\ge1-\mathrm e^{-1}\), and there are at least \(\frac34(1-\mathrm e^{-1})\frac n2>\frac n8\ge|U|\) of them. By Hall's theorem there is an injective map \(\phi\colon W\to[n]\setminus Y\) with \(\phi(w)\) usable for \(w\).

*The embedding.* Map each vertex of \(J\) in \(Y\) to itself, each \(w\in W\) to \(\phi(w)\), and the remaining vertices of \(J\), which are isolated, injectively to unused vertices. Every edge \(yw\) of \(J\), \(y\in Y\), \(w\in W\), goes to the edge \(y\phi(w)\) of \(G_*\). So \(G(n,r_*)\) contains a copy of \(J\) with probability at least \(\frac12\), and \(p_{\mathrm c}(J;n)\le r_*\). Finally \(r_*\le32r\) by the union bound. \(\square\)

## 5. Bounded degeneracy and maximum degree

**Proposition 5.1** (OpenAI). There is an absolute integer \(N_2\) such that for \(n\ge N_2\) and \(r,s\) satisfying (4.1), every graph \(J\) with at most \(n\) vertices, \(|V_+(J)|\le n/4\), \(\operatorname{degen}(J)\le s\) and maximum degree \(\Delta(J)\le n^{2/3}\) has \(p_{\mathrm c}(J;n)\le r\).

**Proof.** We may delete isolated vertices and assume that \(J\) has an edge.

*Layers.* In a subgraph \(J'\) of \(J\) with \(m'\ge1\) vertices, (1.2) gives average degree at most \(2s\), so at least \(m'/2\) vertices have degree at most \(4s\) in \(J'\). Among them a greedy choice gives an independent set of at least \(m'/(2(4s+1))\ge m'/(10s)\) vertices. Take such a set as the last layer, delete it, and repeat with the rest. This gives layers \(L_1,\dots,L_t\), each independent, numbered so that \(L_t\) was chosen first; the number of vertices drops by a factor \(1-\frac1{10s}\) at each step, so \(t\le10s\log n+1\le101(\log n)^2\) for \(n\ge3\). A vertex of \(L_j\) had degree at most \(4s\) in the graph remaining when \(L_j\) was chosen, which contains \(L_1\cup\dots\cup L_{j-1}\); so it has at most \(4s\) *earlier* neighbours, those in earlier layers.

*Bins.* Let \(b=\lfloor n/(4t)\rfloor\), and choose disjoint sets \(B_1,\dots,B_t\subseteq[n]\) with \(|B_j|=|L_j|+b\); their total size is at most \(n/4+tb\le n/2\).

*Embedding layer by layer.* Embed \(L_1,L_2,\dots\) in turn, \(L_j\) into \(B_j\). At step \(j\), expose the edges of \(G(n,r)\) between \(B_j\) and the images of the earlier layers, which lie in \(B_1\cup\dots\cup B_{j-1}\). These edges were not exposed before, so given the past they are independent with probability \(r\). Call \(a\in B_j\) usable for \(v\in L_j\) if \(a\) is adjacent to the images of all earlier neighbours of \(v\). An injective choice of usable images for all of \(L_j\) extends the embedding, since \(L_j\) is independent.

*Hall's condition at one layer.* Let \(U\subseteq L_j\), \(|U|=u\ge1\). The *requirement* of \(v\in U\) is the set of images of its earlier neighbours, of size at most \(4s\). An image lies in at most \(\Delta=\Delta(J)\) requirements, so each requirement meets at most \(4s\Delta\) others, and \(U\) contains a set \(I\) of at least \(u/(1+4s\Delta)\) vertices with pairwise disjoint requirements. If Hall's condition fails for \(U\), there is \(W\subseteq B_j\) with \(|W|=u-1\) such that no vertex of \(B_j\setminus W\), a set of at least \(b\) vertices, is usable for a vertex of \(I\). For fixed \(U\) and \(W\), the events "\(a\) is usable for \(v\)", \(a\in B_j\setminus W\), \(v\in I\), involve disjoint sets of edges and each has probability at least \(r^{4s}\); so this happens with probability at most
\[
(1-r^{4s})^{b|I|}\le\exp\Bigl(-\frac{b\,u\,r^{4s}}{1+4s\Delta}\Bigr).
\]
(If a vertex of \(I\) has no earlier neighbour, every vertex is usable for it and the event is impossible.) By (4.1), \(r^{4s}\ge n^{-4/100}\), \(b\ge n/(500(\log n)^2)\) and \(1+4s\Delta\le1+40\log n\,n^{2/3}\) for large \(n\), so
\[
\frac{b\,r^{4s}}{1+4s\Delta}\ge c\,\frac{n^{1-4/100-2/3}}{(\log n)^3}=c\,\frac{n^{22/75}}{(\log n)^3}\ge5\log n
\]
for an absolute \(c>0\) and all large \(n\). There are at most \(n^{2u}\) pairs \((U,W)\) with \(|U|=u\). Given the past, Hall's condition fails at step \(j\) with probability at most \(\sum_{u\ge1}n^{2u}n^{-5u}\le2n^{-3}\), and at some step with probability at most \(202(\log n)^2n^{-3}\). Choose \(N_2\) so that this is at most \(\frac12\) for \(n\ge N_2\). With probability at least \(\frac12\), Hall's theorem embeds every layer, and every edge of \(J\), which joins a vertex to an earlier neighbour, goes to an edge of \(G(n,r)\). \(\square\)

## 6. Small star forests

A *star forest* is a graph whose components with an edge are stars.

**Proposition 6.1** (OpenAI, after Ascoli, He, Park and Talagrand). Let \(A=400\,\mathrm e^4\). There is an absolute integer \(N_3\) such that for every \(n\ge N_3\) and every star forest \(J\) on at most \(n\) vertices with \(|V_+(J)|\le n/100\),
\[
p_{\mathrm c}(J;n)\le2A\,q(J;n),\qquad\text{and}\qquad p_{\mathrm c}(J;n)\le A\,q(J;n)\ \text{ if }q(J;n)<\tfrac1{2A}.
\]

**Proof.** We may assume that \(J\) has an edge; then \(q_J=q(J;n)>0\) by Lemma 1.1. If \(q_J\ge\frac1{2A}\), the first bound is trivial. Let \(q_J<\frac1{2A}\) and \(p=Aq_J<\frac12\).

*Lower bounds for \(q_J\).* For \(\ell\ge1\) let \(m_\ell\) be the number of components of \(J\) with exactly \(\ell\) leaves (a single edge counts as a star with one leaf). If \(m=m_\ell>0\), the copies of \(m\) disjoint stars with \(\ell\) leaves cover \(\mathcal F_J\). Their number is at most \(C_\ell=n^{m(\ell+1)}/((\ell!)^mm!)\), because the automorphism group of \(m\) disjoint \(\ell\)-leaf stars has at least \((\ell!)^mm!\) elements, and \(C_\ell\ge1\), because at least one copy exists. At \(p_\ell=(2C_\ell)^{-1/(m\ell)}\in(0,1)\) this cover costs at most \(\frac12\), so \(q_J\ge p_\ell\), that is,
\[
q_J^{\ell}\ge\frac{\ell!}{n^{\ell+1}}\Bigl(\frac{m!}2\Bigr)^{1/m}\ge\frac{\ell!}{n^{\ell+1}}\cdot\frac{m_\ell}{2\mathrm e},\tag{6.1}
\]
using \(m!\ge(m/\mathrm e)^m\) and \(2^{-1/m}\ge\frac12\).

*Centre testing.* Split \([n]\) into a centre bin of \(\lfloor n/2\rfloor\) vertices and a leaf bin of the others. Process the stars of \(J\) one at a time. For a star with \(\ell\) leaves, test unused centres one after another until one has at least \(\ell\) neighbours among the unused leaf vertices in \(G(n,p)\); map the centre of the star to it and the leaves to \(\ell\) of those neighbours. Every tested centre is discarded afterwards. At most \(n/100\) leaf vertices are ever used, so at least \(b'=\lfloor n/3\rfloor\) remain unused. The edges from an untested centre to the leaf bin have not been examined, while the set of unused leaf vertices depends only on earlier tests; so given the past, a test succeeds with probability at least \(u_\ell=\mathbb P(\operatorname{Bin}(b',p)\ge\ell)\).

To count tests, add infinitely many auxiliary centres with independent edges to the leaf bin; the process agrees with the actual one until the centre bin is exhausted. Let \(T\) be the number of tests needed for all stars. The expected number of tests for one star with \(\ell\) leaves is at most \(1/u_\ell\), so \(\mathbb ET\le\sum_\ell m_\ell/u_\ell\).

*Bounds for \(u_\ell\).* Let \(\mu=b'p\). If \(\mu\ge2\ell\), then \(\mu\ge2\), \(\mathbb E\operatorname{Bin}(b',p)^2\le\mu^2+\mu\), and Lemma 2.1 with \(\theta=\frac12\) gives \(u_\ell\ge\mathbb P(\operatorname{Bin}(b',p)>\mu/2)\ge\frac14\cdot\frac{\mu^2}{\mu^2+\mu}\ge\frac16\). If \(\mu<2\ell\), use \(\ell\le n/100\), \(b'-\ell+1\ge n/4\), and \(\log(1-p)\ge-2p\) for \(p\le\frac12\):
\[
u_\ell\ge\binom{b'}\ell p^\ell(1-p)^{b'}\ge\frac{(n/4)^\ell p^\ell}{\ell!}\,\mathrm e^{-4\ell}\ge\Bigl(\frac{A}{4\mathrm e^4}\Bigr)^\ell\frac{m_\ell}{2\mathrm en}=100^\ell\,\frac{m_\ell}{2\mathrm en},
\]
by (6.1) and \(p^\ell=A^\ell q_J^\ell\).

*Conclusion.* \(J\) has at most \(n/200\) stars. Hence
\[
\mathbb ET\le6\cdot\frac n{200}+2\mathrm en\sum_{\ell\ge1}100^{-\ell}=\Bigl(\frac3{100}+\frac{2\mathrm e}{99}\Bigr)n<\frac n8,
\]
and by Markov's inequality \(T\le\lfloor n/2\rfloor\) with probability at least \(\frac34\). On this event only actual centres are used, and the stars of \(J\) are embedded disjointly in \(G(n,p)\); isolated vertices go to unused vertices. So \(p_{\mathrm c}(J;n)\le p=Aq_J\). \(\square\)

## 7. Exercises

**Exercise 7.1** (easy). Show that a star forest with \(\ell\) leaves in each of its \(m\) stars, \(\ell\ge2\), has exactly \((\ell!)^mm!\) automorphisms when isolated vertices are removed, and that \(m\) disjoint edges have \(2^mm!\).

**Exercise 7.2** (easy). Show that \(1-\mathrm e^{-y}\ge y/2\) for \(0\le y\le1\), and that \(\frac34(1-\mathrm e^{-1})\cdot\frac12>\frac18\).

**Exercise 7.3** (medium). Show that the greedy procedure in a graph of maximum degree \(D\) on \(m\) vertices (choose a vertex, delete it and its neighbours, repeat) gives an independent set of at least \(m/(D+1)\) vertices. Deduce that in Proposition 5.1 the number of layers satisfies \(t\le10s\log n+1\).

**Exercise 7.4** (medium). Show that the conclusion of Lemma 3.1 can fail for every subfamily of size \(1\): give \(Y\), \(r\), \(s\) and \(\mathcal R\) such that no single \(T\in\mathcal R\) has \(f_{\{T\}}(T')\ge\frac12\) for all \(T'\in\mathcal R\).

## 8. Solutions

**7.1.** An automorphism maps centres to centres (the vertices of degree \(\ell\ge2\)), so it permutes the \(m\) stars and, inside each star, permutes the \(\ell\) leaves; all such maps are automorphisms. For a single edge both endpoints can be exchanged, giving \(2^mm!\).

**7.2.** The function \(1-\mathrm e^{-y}-y/2\) vanishes at \(0\), increases while \(\mathrm e^{-y}>\frac12\), and is positive at \(1\) since \(1-\mathrm e^{-1}>0.63\); so it is nonnegative on \([0,1]\). Also \(\frac38(1-\mathrm e^{-1})>0.237>0.125\).

**7.3.** Each chosen vertex deletes at most \(D+1\) vertices, so at least \(m/(D+1)\) vertices are chosen. In the proof of Proposition 5.1, each step keeps at most a fraction \(1-\frac1{10s}\le\mathrm e^{-1/(10s)}\) of the vertices, so after \(t'\) steps fewer than \(n\,\mathrm e^{-t'/(10s)}\) remain, which is less than \(1\) when \(t'\ge10s\log n\); hence \(t\le10s\log n+1\).

**7.4.** Let \(Y=\{1,\dots,6\}\), \(r=\frac1{10}\), \(s=1\), \(\mathcal R=\{\{1\},\dots,\{6\}\}\). For \(T=\{i\}\) and \(T'=\{j\}\), \(j\neq i\), \(f_{\{T\}}(T')=\mathbb P(i\in Z)=\frac1{10}<\frac12\).

## References

- [OpenAI-GD] OpenAI, *Graph decompositions at the integral expectation threshold*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/Graph-Decompositions-at-the-Integral-Expectation-Threshold-October-5-2026
- [AHPT] R. Ascoli, X. He, J. Park and M. Talagrand, *A reformulation of the discrete convexity conjecture via k-thresholds*, 2026. https://arxiv.org/abs/2608.11183
