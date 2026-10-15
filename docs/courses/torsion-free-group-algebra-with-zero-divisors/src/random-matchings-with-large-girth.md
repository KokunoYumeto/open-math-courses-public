# Random matchings with large girth

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

With the types of [Projective planes and prescribed types](projective-planes-and-prescribed-types.md) fixed, the edges of the two graphs are chosen at random: for every pair of inverse letters, the vertices that must carry the letter are matched with those that must carry its inverse [OpenAI-KZ, Section 2.3]. This lesson conditions the random graphs on having no short cycles, proves that conditioning in this way keeps the probability of any prescribed set of edges as small as in a uniform matching, and shows that the components of the graphs have small diameter. These are the probabilistic inputs for [The bounded-pattern estimate](the-bounded-pattern-estimate.md) and for [Planar separation and the absence of arrangements](planar-separation-and-the-absence-of-arrangements.md).

- The matching model (Section 1).
- Girth conditioning by switchings (Section 2).
- The probability of prescribed edges (Section 3).
- Small diameter (Section 4).

We keep \(q=128\), \(v=16513\), \(p=129/16513\), the alphabet \(T\) with \(\#T=16516\), the sides \(A,B\) of \(n\) vertices with their types \(S_x\), the sets \(Y_t=\{x\in Y:t\in S_x\}\) with \(\#Y_t=np\), and \(d_*=132\). The number \(n\) runs through the multiples of \(2v^2\). Probabilities are proportions of finite sets of equally likely outcomes, and *with high probability* means with probability tending to \(1\) as \(n\to\infty\). We write \(\log\) for the natural logarithm.

## 1. The matching model

For each side \(Y\in\{A,B\}\) and each pair \(\{t,\bar t\}\) of inverse letters, choose a bijection \(Y_t\to Y_{\bar t}\) uniformly at random, independently for all pairs and both sides. A matched pair \(x\mapsto y\) becomes an edge between \(x\) and \(y\) that carries \(t\) from \(x\) to \(y\) and \(\bar t\) from \(y\) to \(x\); the inverse bijection \(Y_{\bar t}\to Y_t\) describes the same edges. The resulting labelled graphs are \(\Gamma_A\) and \(\Gamma_B\), and \(\Gamma=\Gamma_A\sqcup\Gamma_B\).

Every vertex \(x\) has exactly one outgoing edge with each letter of \(S_x\) and none with other letters, so \(\Gamma\) is immersed and the outgoing letters of \(x\) are exactly its type. Degrees lie between \(q+1\) and \(d_*\). A *prescription* is a requirement that a given vertex \(x\) be matched to a given vertex \(y\) with a given letter \(t\) from \(x\) to \(y\); a prescription and its reverse, \(y\) to \(x\) with \(\bar t\), are counted as one.

The *girth* of a graph is the length of its shortest cycle, where a loop is a cycle of length \(1\) and two edges with the same ends form a cycle of length \(2\). Fix a constant \(c>0\) with
\[
\begin{aligned}c\log\frac{2\#T}p&<1,\\ 2c\log d_*&<1;\end{aligned}\tag{1.1}
\]
for instance \(c=1/100\). Put \(L=\lfloor c\log n\rfloor\).

## 2. Girth conditioning by switchings

An edge is *bad* if it lies on a cycle of length less than \(L\).

**Lemma 2.1** (switching; [OpenAI-KZ, Lemma 2.2]). For all sufficiently large \(n\) there is a tuple of matchings for which \(\Gamma\) has girth at least \(L\).

*Proof.* *Few bad edges in a uniform tuple.* A simple cycle of length \(k\) is described by its side (\(2\) choices), its vertices in order (at most \(n^k\)) and the letters of its edges (at most \((\#T)^k\)), so there are at most \(2n^k(\#T)^k\) descriptions. Its \(k\) edges are \(k\) distinct prescriptions. The probability that \(k\) given distinct prescriptions all hold is at most \(\prod_{i<k}(np-i)^{-1}\le(np-k)^{-k}\): given that some prescriptions of the same bijection hold, the conditional probability of another is \(1/(np-i)\) when \(i\) of them concern the same bijection, and prescriptions of different bijections are independent. So the expected number of bad edges is at most
\[
\begin{aligned}&\sum_{k<L}k\cdot2n^k(\#T)^k(np-k)^{-k}\\&\quad\le2\sum_{k<L}k\Bigl(\frac{2\#T}p\Bigr)^k,\end{aligned}
\]
using \(np-k\ge np/2\) for \(k<L\) and large \(n\). By (1.1), \((2\#T/p)^L\le n^{1-\gamma}\) for some \(\gamma>0\), so the sum is at most \(2L^2n^{1-\gamma}\), which is \(o(n)\). Choose a tuple with \(o(n)\) bad edges.

*Removing bad edges.* Let \(xy\) be a bad edge, carrying \(t\) from \(x\) to \(y\). On the same side there are \(np\) edges carrying \(t\) in some direction. Choose one, \(uz\) with \(t\) from \(u\) to \(z\), that is not bad and whose ends are at distance greater than \(2L\) from \(x\) and \(y\). Bad edges exclude \(o(n)\) choices. At most \(2\sum_{j\le2L}d_*^j\le4d_*^{2L}\) vertices lie within distance \(2L\) of \(x\) or \(y\), and each of them is an end of at most two edges carrying \(t\), so the distance condition excludes at most \(8d_*^{2L}\) choices; by (1.1), \(d_*^{2L}\le n^{2c\log d_*}=o(n)\). So for large \(n\) a choice exists.

Replace the edges \(xy\) and \(uz\) by \(xz\) and \(uy\), both carrying \(t\) from the first vertex to the second. This changes two matched pairs of one bijection into two others, so the result is again a tuple of matchings, with the same types. Suppose the new graph had a cycle \(Z\) of length less than \(L\) through a new edge. If \(Z\) uses exactly one new edge, say \(xz\), the rest of \(Z\) is a path of old edges from \(x\) to \(z\) of length less than \(L\); but \(z\) has distance more than \(2L\) from \(x\). The case of \(uy\) is the same. If \(Z\) uses both new edges, removing them leaves two paths of old edges whose ends pair up the four vertices either as \(\{x,u\},\{y,z\}\) or as \(\{x,y\},\{u,z\}\). The first is excluded by the distances again. In the second, the old path from \(u\) to \(z\) has length less than \(L\) and does not use the edge \(uz\), so together with \(uz\) it contains a cycle through \(uz\) of length less than \(L\), and \(uz\) would be bad. This covers also \(x=y\), when the path from \(x\) to \(y\) has length \(0\).

So the switch creates no cycle of length less than \(L\). It removes the bad edge \(xy\), the other removed edge \(uz\) was not bad, the new edges are not bad, and no old edge becomes bad. The number of bad edges decreases. Repeating the switch yields a tuple without bad edges, that is, of girth at least \(L\). \(\square\)

From now on, *probability* refers to the uniform distribution on the tuples of matchings with \(\operatorname{girth}(\Gamma)\ge L\).

## 3. The probability of prescribed edges

**Lemma 3.1** (prescriptions; [OpenAI-KZ, Lemma 2.2]). Put \(r_n=8d_*^{2L}\), which is \(o(n)\) by (1.1). The following holds for all sufficiently large \(n\). Let \(\Omega_s\) be the set of tuples of girth at least \(L\) in which \(s\) given prescriptions hold, and suppose \(\Omega_s\ne\varnothing\). For a further prescription \(xy\), not among the given ones in either direction, the proportion of \(\Omega_s\) in which \(xy\) holds is at most
\[
\frac1{np-s-r_n}
\]
whenever the denominator is positive.

*Proof.* Let \(\Omega_{s,xy}\subseteq\Omega_s\) be the set of tuples in which \(xy\) also holds, with \(t\) from \(x\) to \(y\). For a tuple in \(\Omega_{s,xy}\), call an edge \(uz\) of the same side carrying \(t\) from \(u\) to \(z\) *admissible* if it is not one of the given prescriptions and its ends have distance greater than \(2L\) from \(x\) and \(y\). At most \(s\) edges are excluded by the prescriptions and, as in the proof of Lemma 2.1, at most \(r_n\) by the distance condition, so there are at least \(np-s-r_n\) admissible edges. Switch \(xy,uz\) to \(xz,uy\) as in the proof of Lemma 2.1. Since the tuple has no bad edges at all, the same argument shows that the switch creates no cycle of length less than \(L\); and the given prescriptions are untouched. So every pair (tuple in \(\Omega_{s,xy}\), admissible edge) gives a tuple in \(\Omega_s\).

This map is injective: from the output and the prescription \(xy\), the vertex \(z\) is the current partner of \(x\) under the bijection of \(t\), and \(u\) is the current vertex matched to \(y\); switching back restores the input and identifies the admissible edge. Hence
\[
\#\Omega_{s,xy}\cdot(np-s-r_n)\le\#\Omega_s,
\]
which is the assertion. \(\square\)

Applying Lemma 3.1 one prescription at a time gives, for every feasible set of \(E\) distinct prescriptions with \(E=O(L)\),
\[
\begin{aligned}&\Pr(\text{all hold})\\&\quad\le\prod_{s<E}\frac1{np-s-r_n}\\&\quad=(np)^{-E}e^{o(L)},\end{aligned}\tag{3.1}
\]
since \(np-s-r_n=np(1-o(1))\) uniformly for \(s<E\). Only the uniform bound of Lemma 3.1 is used; no independence after conditioning is claimed.

## 4. Small diameter

**Lemma 4.1** (diameter; [OpenAI-KZ, Lemma 2.3]). There is a constant \(D_0\) such that, with high probability, every connected component of \(\Gamma\) has diameter at most \(D_0L\).

*Proof.* Fix \(\rho>0\), small enough as specified below. Call a set \(Z\) of vertices on one side *expanding* if \(Z\) together with its neighbours has at least \(2\#Z\) vertices. We show that with high probability every set of \(k\) vertices, \(1\le k\le\rho n\), on either side is expanding.

Suppose a set \(Z\) of \(k\) vertices is not expanding. Choose a set \(U\supseteq Z\) of exactly \(2k\) vertices of the same side containing \(Z\) and all its neighbours. Every edge at a vertex of \(Z\) has both ends in \(U\). Each vertex of \(Z\) has at least \(q+1=129\) incident edges, and an edge is counted at most twice, so \(U\) carries at least \(r=\lceil129k/2\rceil\) distinct edges, that is, \(r\) distinct prescriptions among its vertices; note \(64.5\le r/k\le65\). There are at most \(\binom n{2k}\le(C_1n/k)^{2k}\) sets \(U\), and at most \((2k)^2\#T\) prescriptions inside \(U\), so at most \(\binom{(2k)^2\#T}r\le(C_1k)^r\) ways to choose \(r\) of them, for a constant \(C_1\). Choose \(\rho\) so small that \(r\le np/3\) whenever \(k\le\rho n\); then \(np-s-r_n\ge np/2\) for \(s<r\) and large \(n\), and by Lemma 3.1 the \(r\) prescriptions hold with probability at most \((2/(np))^r\). The probability that some set of size \(k\) on either side is not expanding is therefore at most
\[
\begin{aligned}
&2\Bigl(\frac{C_1n}k\Bigr)^{2k}(C_1k)^r\Bigl(\frac2{np}\Bigr)^r\\
&\quad\le\Bigl(C_2\Bigl(\frac kn\Bigr)^{62.5}\Bigr)^k
\end{aligned}
\]
for a constant \(C_2\), since \(r-2k\ge62.5k\) and \(r\le65k\). Make \(\rho\) smaller so that \(C_2\rho^{62.5}<\frac12\). For \(k\le\sqrt n\) the terms are at most \((C_2n^{-31.25})^k\), with sum \(O(n^{-31.25})\); for \(\sqrt n<k\le\rho n\) they are at most \(2^{-k}\), with sum at most \(n2^{-\sqrt n}\). Both tend to \(0\).

On the event that all these sets are expanding, the ball of radius \(j\) around any vertex has at least \(\min(2^j,\rho n)\) vertices, so within \(R=\lceil\log_2(\rho n)\rceil+1\) steps every ball has more than \(\rho n\) vertices, and \(R=O(\log n)=O(L)\). Let \(P\) be a shortest path between two vertices of one component, and take vertices on \(P\) at mutual distances \(2R+1\) along \(P\). Their balls of radius \(R\) are disjoint, since \(P\) is a shortest path, and each has more than \(\rho n\) of the \(n\) vertices of the side. So there are fewer than \(1/\rho+1\) such vertices, and \(P\) has length less than \((2R+1)(1/\rho+1)\), which is at most \(D_0L\) for a constant \(D_0\). \(\square\)

## 5. Exercises

**5.1.** Check that \(c=1/100\) satisfies (1.1).

**5.2.** Show that a uniformly random bijection between two sets of size \(m\) satisfies \(i\) given distinct prescriptions with probability \(\frac{(m-i)!}{m!}\), and deduce the bound \((m-i)^{-i}\) used in the proof of Lemma 2.1.

**5.3.** In the switching of Lemma 2.1, explain why the new tuple still gives every vertex its prescribed type.

**5.4.** Show that in a graph of girth at least \(L\) with all degrees at least \(3\), the ball of radius \(j<L/2\) around a vertex is a tree with at least \(3\cdot2^{j-1}\) vertices at distance exactly \(j\).

**5.5.** In the proof of Lemma 4.1, check that a set \(Z\) of \(k\) vertices that is not expanding yields at least \(\lceil129k/2\rceil\) distinct edges inside a set of \(2k\) vertices.

## 6. Solutions

**5.1.** \(\#T=16516\) and \(p=129/16513\), so \(2\#T/p\approx4.23\cdot10^6\) and \(\frac1{100}\log(4.23\cdot10^6)\approx0.153<1\); \(\frac2{100}\log132\approx0.098<1\).

**5.2.** A uniform bijection is one of \(m!\) equally likely ones, and those satisfying \(i\) consistent prescriptions number \((m-i)!\). Then \(\frac{(m-i)!}{m!}=\prod_{j<i}\frac1{m-j}\le(m-i)^{-i}\).

**5.3.** The switch keeps \(x\) and \(u\) as the vertices carrying \(t\) outward and \(y\) and \(z\) as the vertices carrying \(\bar t\) outward; it only changes which of them are matched. No other edge changes.

**5.4.** Two paths from the centre to a vertex at distance \(j<L/2\) would give a cycle of length at most \(2j<L\). So the ball is a tree. The centre has at least \(3\) neighbours, and every other vertex of the tree has at least \(2\) neighbours farther out.

**5.5.** All edges at vertices of \(Z\) end in \(Z\cup N(Z)\subseteq U\). Counting edges at vertices of \(Z\) with multiplicity gives at least \(129k\), and an edge with both ends in \(Z\) is counted twice.

## References

- [OpenAI-KZ] OpenAI, *A Torsion-Free Group Algebra with Zero Divisors*, OpenAI Math Release preprint, 23 September 2026, Section 2.3. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Group-Algebra-with-Zero-Divisors-September-23-2026
