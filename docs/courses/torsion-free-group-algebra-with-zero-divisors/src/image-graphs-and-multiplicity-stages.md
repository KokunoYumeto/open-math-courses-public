# Image graphs and multiplicity stages

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The geometric safeguards of the construction, root separation and torsion-freeness, will both be reduced to one probabilistic statement: with high probability the random graphs carry no system of a bounded number of paths, of total length comparable to \(\log n\), whose positions are almost all paired by comparisons of their words. This lesson states that bounded-pattern estimate and begins its proof [OpenAI-KZ, Section 3]. The proof continues in [Aligned blocks and word counts](aligned-blocks-and-word-counts.md) and ends in [The bounded-pattern estimate](the-bounded-pattern-estimate.md). Here we show that the image of such a system in the graph consists of boundedly many long chains, that every edge is traversed boundedly often, and that sorting the edges by how often they are traversed gives stages whose vertex and edge counts balance.

- Systems of paths and the estimate (Section 1).
- The image graph has bounded cycle rank (Section 2).
- Chains and multiplicities (Section 3).
- Patterns (Section 4).
- Multiplicity stages (Section 5).

We work with the random graph \(\Gamma=\Gamma_A\sqcup\Gamma_B\) of [Random matchings with large girth](random-matchings-with-large-girth.md), conditioned on girth at least \(L=\lfloor c\log n\rfloor\), with the two vertices \(x_A\in A\) and \(x_B\in B\) chosen in advance. A path is *immersed* if it never traverses an edge and immediately the same edge back; a closed path is *cyclically immersed* if moreover its last and first edges do not form such a reversal. Since \(\Gamma\) is immersed, the letters of an immersed path never contain a cancelling turn.

## 1. Systems of paths and the estimate

**Definition 1.1** (systems). A *system* is a finite family of paths in \(\Gamma\) of positive length, all closed and cyclically immersed, except possibly one immersed path, the *interval path*, which starts at \(x_A\) or \(x_B\) and need not be closed. The positions on each path are numbered from \(1\) to its length, a closed path being read from a chosen starting vertex. An *occurrence* is a pair (path, position); different occurrences may traverse the same edge. The *total length* \(H\) is the number of occurrences.

An *interval* is a set of consecutive positions on one path. An *interval pair* consists of two disjoint intervals of equal length with a bijection between them that either preserves or reverses the order of positions; an order-preserving pair must carry equal letters at corresponding positions, and an order-reversing pair must carry inverse letters at corresponding positions. A *pairing* of the system is a family of interval pairs whose intervals are pairwise disjoint; occurrences outside all its intervals are *unpaired*, and \(b\) denotes their number. The pairing satisfies the *reduction condition* if
\[
\begin{aligned}&\text{paired occurrences}\\&\text{traverse distinct}\\&\text{edges of }\Gamma.\end{aligned}\tag{1.1}
\]

**Proposition 1.2** (bounded-pattern estimate; [OpenAI-KZ, Proposition 3.1]). There is a constant \(\varepsilon>0\), depending only on the types and the turn weights, with the following property. For all fixed integers \(K\ge1\), \(I\ge0\) and every fixed real \(C\ge1\), the probability that \(\Gamma\) carries a system of at most \(K\) paths, with total length \(L\le H\le CL\), and a pairing satisfying (1.1) with at most \(I\) interval pairs and \(b\le\varepsilon H\) unpaired occurrences, tends to \(0\) as \(n\to\infty\).

The order of the quantifiers matters: \(\varepsilon\) is chosen first, and only then \(K\), \(C\) and \(I\). In [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md) the bounds \(K,C,I\) are chosen depending on \(\varepsilon\).

From now on \(K,C,I\) are fixed, and implicit constants may depend on them; \(\varepsilon\) will be fixed at the end of the proof independently of them. All \(o(\cdot)\) estimates are uniform over the systems with these bounds.

## 2. The image graph has bounded cycle rank

The *image graph* \(\Delta\) of a system is the subgraph of \(\Gamma\) formed by the edges traversed by its paths and their ends. It has at most \(H\le CL\) edges and, as a subgraph of \(\Gamma\), girth at least \(L\). The *cycle rank* of a finite graph is \(\beta=E-V+c\), where \(E,V,c\) are its numbers of edges, vertices and components; it is the number of independent cycles, and it is \(0\) exactly for forests.

**Lemma 2.1** (bounded cycle rank). The cycle rank of \(\Delta\) is bounded by a constant depending only on \(C\). The graph \(\Delta\) has at most two vertices of degree \(1\), and its vertices of degree at least \(3\), together with their degrees, are bounded in number by a constant depending only on \(C\).

*Proof.* Repeatedly delete a vertex of degree \(1\) together with its edge, and delete isolated vertices. Each deletion keeps the cycle rank, and the result, the *core*, has minimum degree at least \(2\) where it is nonempty. Components of the core that are cycles have at least \(L\) edges each, so there are at most \(C\) of them. In the other components, suppress the vertices of degree \(2\): replace each maximal path through such vertices by one edge whose *length* is the number of edges it replaces. The result is a multigraph \(\Xi\), possibly with loops and parallel edges, of minimum degree at least \(3\), with \(r\) edges of total length at most \(CL\).

Suppose \(r>0\). Consider a random walk on \(\Xi\) that starts on one of its \(2r\) directed edges chosen uniformly, and at every step continues along one of the \(\deg(z)-1\ge2\) directed edges leaving the current vertex \(z\) other than the reverse of the edge just traversed, chosen uniformly. The uniform distribution on directed edges is stationary: a directed edge leaving \(z\) has \(\deg(z)-1\) possible predecessors, each of which leads to it with probability \(1/(\deg(z)-1)\), so it receives total probability \(\frac1{2r}\). Hence each step of the walk is a uniformly distributed directed edge, of expected length \(\frac1r\sum_e\operatorname{length}(e)\le CL/r\), and a walk of \(k\) steps has expected total length at most \(kCL/r\). By Markov's inequality, walks of total length at most \(2kCL/r\) have probability at least \(\frac12\). A single walk of \(k\) steps has probability at most \(\frac1{2r}2^{-(k-1)}\), so there are at least \(r2^{k-1}\) such short walks.

Choose \(k\) as the least integer with \(r2^{k-1}>(2r)^2\); then \(k\le\log_2r+4\). Since \(\Xi\) has fewer than \(2r\) vertices, two distinct short walks start at the same vertex and end at the same vertex. Expanding their edges into paths of \(\Delta\) gives two distinct paths between the same two vertices, each without immediate reversals. In a forest there is only one such path between two vertices, so their union contains a cycle, of length at most \(4kCL/r\). Since the girth is at least \(L\), \(r\le4Ck\le4C(\log_2r+4)\), and \(r\) is bounded by a constant depending only on \(C\). The cycle rank of \(\Delta\) equals that of the core, which is at most \(C+r\).

A closed cyclically immersed path cannot pass through a vertex of degree \(1\) of \(\Delta\), since it would have to turn back there; an immersed interval path can do so only at its two ends. So \(\Delta\) has at most two vertices of degree \(1\), and no isolated vertices. Summing \(\deg(z)-2\) over all vertices gives \(2E-2V=2\beta-2c\), so
\[
\begin{aligned}&\sum_{\deg(z)\ge3}(\deg(z)-2)\\&\quad=2\beta-2c+\#\{z:\deg(z)=1\}\\&\quad\le2\beta+2,\end{aligned}
\]
which bounds the number of vertices of degree at least \(3\) and their degrees. \(\square\)

## 3. Chains and multiplicities

*Mark* the starting vertices of all paths of the system, the end of the interval path, and all vertices of \(\Delta\) of degree different from \(2\). There are boundedly many marks, by Lemma 2.1. A *chain* is a path in \(\Delta\) between two marks, possibly equal, whose interior vertices are unmarked; the unmarked vertices have degree \(2\), so \(\Delta\) is the union of its chains, which meet only at marks.

**Lemma 3.1** (chains). The number of chains is bounded, every path of the system traverses whole chains, and the number \(m_e\) of occurrences traversing an edge \(e\) is constant along each chain and satisfies
\[
\begin{aligned}m_e&\le2\Bigl(\frac HL+K\Bigr)\\&\le2(C+K).\end{aligned}\tag{3.1}
\]

*Proof.* Every component of \(\Delta\) contains the starting vertex of some path, so a component that is a cycle contains a mark, and every chain has marked ends. In the multigraph whose vertices are the marks and whose edges are the chains, the degree of a mark is its degree in \(\Delta\), which is bounded; so the number of chains is bounded. A path enters a chain at a mark, cannot stop at an unmarked vertex, and cannot turn back there by immersion, so it traverses the chain to its other end; hence every edge of a chain is traversed the same number of times.

If one path traverses the same edge in the same direction at two positions \(i<j\), the part of the path from position \(i\) up to position \(j-1\) is a closed path without immediate reversals, of positive length. Such a closed path is not contained in a forest, since in a tree a path without immediate reversals never returns to its start, so it contains a cycle and \(j-i\ge L\). Hence a path of length \(h\) traverses a given edge in a given direction at most \(h/L+1\) times. Summing over the at most \(K\) paths and the two directions gives \(m_e\le2(H/L+K)\). \(\square\)

## 4. Patterns

The *unlabelled pattern* of a system with a pairing records:

- the multigraph of marks and chains, with the length of each chain and the side, \(A\) or \(B\), of each component;
- for each path, the sequence of chains it traverses, with directions; which path, if any, is the interval path, and whether it starts at \(x_A\) or at \(x_B\);
- for each interval pair, the paths and positions of its two intervals and whether it preserves or reverses order.

It records neither the names of the vertices of \(\Gamma\) nor the letters. Conversely, a *realization* of a pattern is an injective map of the abstract graph of marks and chains into \(\Gamma\), on the prescribed sides, such that the prescribed paths and interval pairs form a system with a pairing satisfying (1.1) and the comparisons of letters. Injectivity on vertices and edges holds because \(\Delta\) is the actual image of the system. The pattern determines all interval positions and the numbers \(m_e\), and whether (1.1) can hold; we keep only patterns for which it can.

**Lemma 4.1** (few patterns). The number of unlabelled patterns of systems with at most \(K\) paths, total length at most \(CL\) and at most \(I\) interval pairs is bounded by a polynomial in \(L\).

*Proof.* The multigraph of marks and chains, the sides, the chain sequences of the paths and the choices of the interval path have boundedly many possibilities, by Lemmas 2.1 and 3.1. The chain lengths and the interval positions are boundedly many integers between \(0\) and \(CL\). \(\square\)

## 5. Multiplicity stages

Let \(m_*=\max_em_e\). For \(1\le j\le m_*\) let \(\Delta_j\) be the subgraph of \(\Delta\) formed by the edges with \(m_e\ge j\) and their ends, with \(E_j\) edges and \(V_j\) vertices. Every chain lies entirely in \(\Delta_j\) or entirely outside it. Let \(\iota=1\) if the system has an interval path and \(\iota=0\) otherwise.

**Lemma 5.1** (stage counts; [OpenAI-KZ, Section 3]).
\[
\begin{aligned}\sum_{j=1}^{m_*}E_j&=H,\\\sum_{j=1}^{m_*}V_j&\le H+\iota.\end{aligned}\tag{5.1}
\]

*Proof.* An edge \(e\) lies in \(\Delta_j\) for exactly \(m_e\) values of \(j\), and \(\sum_em_e=H\). A vertex \(z\) lies in \(\Delta_j\) for exactly \(M_z=\max_{e\ni z}m_e\) values of \(j\), so \(\sum_jV_j=\sum_zM_z\). Each occurrence of an edge at \(z\), that is, each time a path traverses an edge \(e\) at its end \(z\), is an *incidence* of \(e\) at \(z\); there are \(m_e\) incidences of \(e\) at each of its ends. Except at the two ends of the interval path, a path that arrives at \(z\) along one edge leaves along another, different by immersion, and the cyclic immersion of closed paths gives the same at their starting vertex. So all incidences at \(z\), except the \(a(z)\) incidences at the ends of the interval path, are paired by passages through \(z\) between incidences on distinct edges. The incidences of an edge \(e\ni z\) with \(m_e=M_z\) are therefore, except for at most \(a(z)\) of them, paired with incidences of other edges at \(z\), and
\[
2M_z\le\sum_{e\ni z}m_e+a(z).
\]
Summing over \(z\), each edge is counted at its two ends and \(\sum_za(z)=2\iota\), so \(2\sum_zM_z\le2H+2\iota\). \(\square\)

Put \(k_1=\iota\) and \(k_j=0\) for \(j>1\). By (5.1),
\[
\sum_{j=1}^{m_*}\bigl(V_j-E_j-k_j\bigr)\le0.\tag{5.2}
\]
In [The bounded-pattern estimate](the-bounded-pattern-estimate.md), the exponent \(V_j-E_j-k_j\) is the power of \(n\) in the expected number of realizations of stage \(j\): every vertex brings a factor of about \(n\) choices, every edge a probability of about \(1/n\), and in stage \(1\) the starting vertex of the interval path is prescribed. Inequality (5.2) says that the powers of \(n\) do not grow across the stages; the decay must then come from the letters, which are studied in [Aligned blocks and word counts](aligned-blocks-and-word-counts.md). Counting only the distinct edges of \(\Delta\), instead of the stages, would lose this balance.

## 6. Exercises

**6.1.** Show that deleting a vertex of degree \(1\) with its edge, or an isolated vertex, does not change the cycle rank.

**6.2.** In the proof of Lemma 2.1, check that the least \(k\) with \(r2^{k-1}>4r^2\) satisfies \(k\le\log_2r+4\), and deduce an explicit bound for \(r\) when \(C=1\).

**6.3.** Give an example of a system of two closed paths in a graph of large girth with total length \(H\) and an edge traversed \(4\) times.

**6.4.** Show by an example that \(\sum_jV_j\) can be smaller than \(H\).

**6.5.** For a single closed cyclically immersed path that traverses a cycle of \(\Delta\) exactly once, compute \(m_*\), \(E_1\), \(V_1\) and both sides of (5.1).

## 7. Solutions

**6.1.** Deleting a vertex of degree \(1\) and its edge lowers \(E\) and \(V\) by \(1\) and keeps \(c\). Deleting an isolated vertex lowers \(V\) and \(c\) by \(1\) and keeps \(E\).

**6.2.** The condition \(r2^{k-1}>4r^2\) means \(k>\log_2r+3\), so the least such \(k\) is at most \(\log_2r+4\). For \(C=1\), \(r\le4(\log_2r+4)\) holds for \(r=36\) (\(36\le36.7\)) and fails for every \(r\ge37\), since \(4(\log_2 37+4)\approx36.8<37\) and \(r-4\log_2r\) increases for \(r\ge6\). So \(r\le36\).

**6.3.** Let \(Z\) be a cycle of length \(L'\ge L\). The closed path that runs twice around \(Z\) is cyclically immersed and traverses every edge of \(Z\) twice in the same direction. Two copies of it form a system of two paths with \(H=4L'\) in which every edge of \(Z\) is traversed \(4\) times; the bound (3.1) gives \(2(4+2)=12\).

**6.4.** Take a graph made of three chains \(Q_1,Q_2,Q_3\) of lengths \(\ell_1,\ell_2,\ell_3\) between two vertices \(u,w\), and the three closed paths that run around \(Q_1\cup Q_2\), \(Q_2\cup Q_3\) and \(Q_3\cup Q_1\). Every edge has \(m_e=2\), so \(H=2(\ell_1+\ell_2+\ell_3)\). Every vertex has \(M_z=2\), and there are \(\ell_1+\ell_2+\ell_3-1\) vertices, so \(\sum_jV_j=H-2<H\). At \(u\) the three incidence counts are \(2,2,2\), and \(2M_u=4<6\).

**6.5.** \(m_*=1\), \(E_1=V_1=L'\), the length of the cycle, and \(H=L'\); so \(\sum E_j=H\) and \(\sum V_j=H\le H+0\).

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
