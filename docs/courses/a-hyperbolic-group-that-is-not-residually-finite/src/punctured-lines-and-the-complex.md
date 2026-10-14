# Punctured lines and the complex

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group of this course is the fundamental group of a finite triangle complex \(K\) with three vertices. Its edges and triangles are indexed by an incidence structure of punctured affine lines over a finite field: many lines, each with a marked point removed, such that the incidence graph has no short cycles while almost every point lies on many lines. This lesson constructs the incidence structure (Lemma 1.2), the complex (Section 2), checks the link condition of the triangle complex criterion (Lemma 3.1), and proves that certain words of length four, the rectangular words, are nontrivial in the fundamental group (Proposition 4.2). The next lesson, [The rank obstruction](the-rank-obstruction.md), shows that every homomorphism to a finite group kills one of them.

- Punctured lines with few short cycles (Lemma 1.2).
- Blocks and the complex (Section 2).
- The links (Lemma 3.1).
- The group and its rectangular words (Proposition 4.2).

The lesson follows [OpenAI-RF, Sections 2.2 and 2.3]. It uses the triangle complex criterion, Theorem 2.1 of [Triangle complexes and their links](triangle-complexes-and-their-links.md), proved in the lessons before this one.

## 1. Punctured lines with few short cycles

Fix the integers and the constant
\[
h=20,\qquad c=100^{-h},
\]
and an integer \(r\ge1\) with \(cr\ge100\). For a prime \(q\), put \(P=\mathbb F_q^h\), \(m=q^h\), and choose a subset \(S\subset\mathbb F_q\) with \(|S|=\lfloor q/100\rfloor\). Statements "for large \(q\)" refer to primes \(q\) beyond a bound that depends only on \(h\) and \(r\).

An *affine line* in \(P\) is a set \(\{a+sd:s\in\mathbb F_q\}\) with \(d\ne0\); it has \(q\) points, and its *direction* is the one-dimensional subspace \(\mathbb F_qd\). There are
\[
J=\frac{q^h-1}{q-1}\ge q^{h-1}
\]
directions, and two distinct points lie on exactly one line.

**Lemma 1.1** (two inequalities of probability). Let \(X\ge0\) be a random variable with finitely many values, and \(a>0\). Then \(\Pr(X\ge a)\le\mathbb EX/a\) (Markov). If \(X\) is a sum of independent indicator variables with mean \(\mu\) and \(0\le s<\mu\), then \(\Pr(X\le\mu-s)\le\mu/s^2\) for \(s>0\) (Chebyshev).

*Proof.* \(a\,\mathbf 1_{X\ge a}\le X\); take expectations. For the second, the variance of a sum of independent indicators with probabilities \(p_k\) is \(\sum_kp_k(1-p_k)\le\mu\), and Markov's inequality for \((X-\mu)^2\) gives \(\Pr(|X-\mu|\ge s)\le\operatorname{Var}X/s^2\le\mu/s^2\). \(\blacksquare\)

**Lemma 1.2** ([OpenAI-RF, Lemma 2.2]). For all large primes \(q\) there are affine lines \(\ell_i\subset P\), indexed by a finite set \(I\) of size \(N\), with distinct marked points \(a_i\in S^h\cap\ell_i\), and a set \(E\subset P\), such that:

1. the bipartite graph on \(P\sqcup I\), with an edge between \(z\) and \(i\) when \(z\in\ell_i\setminus\{a_i\}\), has no cycle of length at most \(12\);
2. \(|I(z)|\ge4r^2\) for \(z\notin E\), where
\[
I(z)=\{i\in I:z\in\ell_i\setminus\{a_i\}\};
\]
3. \(N/m\to c\) and \(|E|/m\to0\) as \(q\to\infty\).

In particular, for large \(q\) these data can be chosen with
\[
q>r,\qquad\frac{Nr}4>2m+r|E|.
\]

The graph in (1) is the *incidence graph of the punctured lines*; a cycle in it alternates between points and labels.

*Proof.* *Random lines.* Use every point \(a\in S^h\) as a mark, and choose for it a direction uniformly at random, independently for different marks; let \(\ell_a\) be the line through \(a\) with that direction. For a fixed \(z\in P\) and a mark \(a\ne z\), the event \(z\in\ell_a\) is the event that the chosen direction is that of \(z-a\), of probability \(1/J\). So the degree \(X_z=|I(z)|\) of \(z\) is a sum of independent indicators with mean
\[
\mu_z=\frac{|S|^h-[z\in S^h]}J .
\]
Since \(|S|^h=(c+o(1))q^h\) and \(J=(1+o(1))q^{h-1}\), \(\mu_z=(c+o(1))q\) uniformly in \(z\). For large \(q\), \(\mu_z\ge8r^2\), and Lemma 1.1 with \(s=\mu_z-4r^2\ge\mu_z/2\) gives
\[
\begin{aligned}
\Pr\bigl(X_z<4r^2\bigr)&\le\frac{\mu_z}{(\mu_z/2)^2}\\
&=\frac4{\mu_z}=O(q^{-1}).
\end{aligned}
\]
So the expected number of points of degree less than \(4r^2\) is \(O(m/q)\), and by Markov's inequality, with probability tending to \(1\), there are at most \(mq^{-1/2}\) of them.

*Short cycles.* Let \(2\le s\le6\). A cycle of length \(2s\) passes through distinct points \(z_1,\dots,z_s\) and distinct marks \(a_1,\dots,a_s\) with \(z_t,z_{t+1}\in\ell_{a_t}\) (indices modulo \(s\)). There are at most \(m^s\) choices of the points. The line through \(z_t\) and \(z_{t+1}\) is determined, and the mark \(a_t\) is one of its at most \(q\) points; so there are at most \(q^s\) choices of the marks. For distinct marks, the probability that all \(s\) chosen directions are the prescribed ones is \(J^{-s}\), by independence. So the expected number of such cycles is at most
\[
m^sq^sJ^{-s}\le q^{hs}q^sq^{-(h-1)s}=q^{2s}.
\]
Summing over \(s\le6\), the expected number of cycles of length at most \(12\) is at most \(5q^{12}\), and by Markov's inequality it is at most \(q^{13}\) with probability tending to \(1\).

*Deletion.* For large \(q\), choose an outcome with both properties. Delete every mark that lies on a cycle of length at most \(12\): at most \(6q^{13}\) marks. Let \(I\) be the remaining marks, with their lines, and let \(E\) consist of the points of degree less than \(4r^2\) before the deletion and of all points of the deleted lines. Deleting labels creates no cycle, so (1) holds. A point outside \(E\) lies on no deleted line, so its degree is unchanged, at least \(4r^2\): (2) holds. Finally
\[
\begin{gathered}
|E|\le mq^{-1/2}+6q^{14}=o(m),\\
N\ge|S|^h-6q^{13}=(c+o(1))m,
\end{gathered}
\]
because \(m=q^{20}\); and \(N\le|S|^h\). This proves (3).

For the last assertion, as \(q\to\infty\), \(\frac{Nr}{4m}\to\frac{cr}4\ge25\), while \(\frac{2m+r|E|}m\to2\). \(\blacksquare\)

From now on the data of Lemma 1.2 are fixed, for one prime \(q\) that also satisfies the last two inequalities. Nothing chosen later changes \(q\) or these data.

## 2. Blocks and the complex

**Blocks.** Let \(z\notin E\) and \(d=|I(z)|\ge4r^2\). Choose \(n_2\in[r,2r-1]\) with \(n_2\equiv d\pmod r\), and put \(n_1=(d-(r+1)n_2)/r\). Then \(n_1\) is an integer and
\[
\begin{aligned}
n_1&\ge\frac{4r^2-(r+1)(2r-1)}r\\
&=\frac{2r^2-r+1}r\ge r .
\end{aligned}
\]
Partition \(I(z)\) into two *blocks* of sizes \(rn_1\) and \((r+1)n_2\). Write \(|I_b|=s_bt_b\) for a block \(b\), with \((s_b,t_b)=(r,n_1)\) and \((r+1,n_2)\) respectively; so \(s_b,t_b\ge r\). Blocks at different points are different blocks, and \(p(b)\) denotes the point of \(b\). Points of \(E\) get no blocks. For each block fix a bijection
\[
\begin{gathered}
I_b\to\mathbb Z/s_b\times\mathbb Z/t_b,\\
i\mapsto\bigl(\alpha_b(i),\beta_b(i)\bigr).
\end{gathered}
\]
A label \(i\) lies in at most one block at each point, and in a block at every point of \(\ell_i\setminus(\{a_i\}\cup E)\).

**The complex.** Let \([r]=\{0,\dots,r-1\}\). The complex \(K\) has three vertices \(O\), \(V\), \(W\), and the edges
\[
\begin{gathered}
x_{iuv}\colon V\to W\quad(i\in I,\ u,v\in[r]),\\
L_{b,u,j}\colon O\to V\quad(u\in[r],\ j\in\mathbb Z/s_b),\\
R_{b,v,k}\colon O\to W\quad(v\in[r],\ k\in\mathbb Z/t_b).
\end{gathered}
\]
For every block \(b\), every \(i\in I_b\) and all \(u,v\in[r]\), attach a triangle with the sides
\[
x_{iuv},\qquad L_{b,u,\alpha_b(i)+v},\qquad R_{b,v,\beta_b(i)+u},
\]
whose oriented boundary runs from \(O\) along \(L\) to \(V\), along \(x\) to \(W\), and back along \(R\). All triangles have one fixed Euclidean shape with the angles
\[
\frac{3\pi}5\ \text{at}\ O,\qquad\frac\pi5\ \text{at}\ V,\qquad\frac\pi5\ \text{at}\ W ;
\]
so every edge \(x\) has one length, every edge \(L\) or \(R\) another, and the gluings are isometric. The three vertices of each triangle are distinct, so closed cells embed, and \(K\) is a connected finite Euclidean triangle complex in the sense of the first lesson (there are points outside \(E\), hence blocks, and every edge lies in a triangle or joins \(O\), \(V\), \(W\)).

The larger angle at \(O\) will control the short cycles in the link of \(O\); the smaller angles at \(V\) and \(W\) are paired with the large girth of the incidence graph.

## 3. The links

**Lemma 3.1** ([OpenAI-RF, Lemma 2.3]). The complex \(K\) satisfies the hypothesis of the triangle complex criterion with \(\eta=2\pi/5\). At \(V\), and at \(W\), the link distance between two different directions of edges \(x_{iuv}\) with the same label \(i\) is at least \(14\pi/5\), or infinite.

*Proof.* *The link of \(O\).* Its vertices are the directions of the edges \(L_{b,u,j}\) and \(R_{b,v,k}\), and each triangle contributes one link edge of length \(3\pi/5\), joining \(L_{b,u,\alpha_b(i)+v}\) to \(R_{b,v,\beta_b(i)+u}\). For fixed \(b,u,v,j,k\), the equations
\[
\alpha_b(i)=j-v,\qquad\beta_b(i)=k-u
\]
have exactly one solution \(i\in I_b\). So, for each block, every \(L_{b,\cdot,\cdot}\)-direction is joined to every \(R_{b,\cdot,\cdot}\)-direction by exactly one link edge, and there are no other link edges. The link of \(O\) is a disjoint union of complete bipartite graphs without multiple edges, so every nonempty cyclically reduced closed walk in it has at least four edges and angular length at least \(12\pi/5=2\pi+2\pi/5\).

*The link of \(V\).* Its vertices are the directions of the edges \(x_{iuv}\) and \(L_{b,u,j}\); the triangle \((b,i,u,v)\) contributes a link edge of length \(\pi/5\) joining \(x_{iuv}\) to \(L_{b,u,\alpha_b(i)+v}\). Map the link to the incidence graph of Lemma 1.2: send \(x_{iuv}\) to \(i\), \(L_{b,u,j}\) to \(p(b)\), and the link edge of \((b,i,u,v)\) to the incidence edge between \(p(b)\) and \(i\), which exists because \(i\in I_b\subset I(p(b))\). This map is injective on the link edges at each link vertex. At \(x_{iuv}\), the incident link edges are given by the blocks \(b\) containing \(i\), at most one at each point, so their images, the edges between \(p(b)\) and \(i\), are different. At \(L_{b,u,j}\), the incident link edges are given by the pairs \((i,v)\) with \(i\in I_b\), \(v\in[r]\) and \(\alpha_b(i)+v=j\); for a given \(i\), this determines \(v\) modulo \(s_b\), hence uniquely in \([r]\), because \(s_b\ge r\). So different incident link edges have different labels \(i\), and different images.

A reduced walk in the link therefore maps to a walk in the incidence graph without immediate reversals, and a cyclically reduced closed walk maps to a cyclically reduced closed walk. A nonempty cyclically reduced closed walk in a graph contains a cycle: take a shortest closed subwalk of positive length; it has length at least three, since length one is a loop and length two a reversal, and it repeats no vertex. The incidence graph is bipartite without cycles of length at most \(12\), so this cycle, and the walk, has at least \(14\) edges, of angular length at least \(14\pi/5>2\pi+2\pi/5\).

*The link of \(W\)* is treated in the same way, with the edges \(R_{b,v,k}\), \(k=\beta_b(i)+u\), and \(t_b\ge r\).

*Same-label directions.* Let a reduced link path at \(V\) join \(x_{iuv}\) to \(x_{iu'v'}\) with \((u,v)\ne(u',v')\). It has positive length, and its image is a walk from \(i\) to \(i\) without reversals at its interior vertices; it may reverse at the closing point. A shortest closed subwalk of positive length is again a cycle: its middle vertices are interior vertices of the walk. So the path has at least \(14\) edges and length at least \(14\pi/5\). A shortest link path between two vertices is reduced, so the link distance is at least \(14\pi/5\), or infinite if there is no path. The same holds at \(W\). \(\blacksquare\)

Excluding cycles of length at most \(10\) would already give the link condition (Exercise 5.3); the stronger bound at same-label directions is used only for the turns in Proposition 4.2, where any bound \(\ge\pi\) suffices.

## 4. The group and its rectangular words

Let \(G=\pi_1(K,O)\). By the triangle complex criterion and Lemma 3.1, \(G\) is torsion-free and word-hyperbolic.

Choose an edge path \(\tau_X\) from \(O\) to each vertex \(X\), with \(\tau_O\) constant. For an oriented edge \(e\) from \(X\) to \(Y\), let \(g_e\in G\) be the class of the loop \(\tau_Xe\tau_Y^{-1}\), and write \(g_{iuv}=g_{x_{iuv}}\). Products are taken in path order.

**Lemma 4.1** (the triangle relations). For every block \(b\), every \(i\in I_b\) and all \(u,v\in[r]\),
\[
g_{iuv}=g_{L_{b,u,\alpha_b(i)+v}}^{-1}\,g_{R_{b,v,\beta_b(i)+u}} .
\]

*Proof.* For the triangle with these sides, the loop \(L\,x\,R^{-1}\) bounds the triangle, so it is nullhomotopic. Inserting \(\tau_V^{-1}\tau_V\) and \(\tau_W^{-1}\tau_W\) gives \(g_Lg_xg_R^{-1}=1\). \(\blacksquare\)

**Proposition 4.2** (rectangular words; [OpenAI-RF, Section 2.3]). For every \(i\in I\) and all \(u\ne u'\), \(v\ne v'\) in \([r]\),
\[
g_{iuv}\,g_{iu'v}^{-1}\,g_{iu'v'}\,g_{iuv'}^{-1}\ne1 .
\]

*Proof.* The connecting paths cancel, so the word is conjugate to the class of the closed edge path
\[
x_{iuv}\,x_{iu'v}^{-1}\,x_{iu'v'}\,x_{iuv'}^{-1}
\]
from \(V\) through \(W\), \(V\), \(W\) back to \(V\). Its four turns compare, in a link at \(W\) or at \(V\), the directions of two different edges with label \(i\): at \(W\) the edges \(x_{iuv}\) and \(x_{iu'v}\) (as \(u\ne u'\)), at \(V\) the edges \(x_{iu'v}\) and \(x_{iu'v'}\), at \(W\) the edges \(x_{iu'v'}\) and \(x_{iuv'}\), and at the closing point \(V\) the edges \(x_{iuv'}\) and \(x_{iuv}\). By Lemma 3.1 each turn has link distance at least \(14\pi/5\ge\pi\), and by the closed-path part of the triangle complex criterion the path is not nullhomotopic. \(\blacksquare\)

These elements are the *rectangular words*; let \(\mathcal R\subset G\) be the finite set of them. For \(u=u'\) or \(v=v'\) the same expression is the identity, so the rectangles with two distinct rows and two distinct columns are exactly the nontrivial ones.

## 5. Exercises

**5.1.** For \(r=2\) and \(d=16\), find \(n_1\), \(n_2\) and the two block shapes \((s_b,t_b)\).

**5.2.** Show that the link of \(O\) restricted to one block is the complete bipartite graph with \(rs_b\) and \(rt_b\) vertices, by counting its edges.

**5.3.** Show that, without cycles of length at most \(10\) in the incidence graph, the links of \(V\) and \(W\) would still satisfy the hypothesis of the criterion with \(\eta=2\pi/5\).

**5.4.** Show that \(\mu_z=(c+o(1))q\) uniformly in \(z\) in the proof of Lemma 1.2.

**5.5.** Show that \(g_{iuv}g_{iu'v}^{-1}g_{iu'v'}g_{iuv'}^{-1}=1\) when \(u=u'\) or \(v=v'\).

## 6. Solutions

**5.1.** \(n_2\in\{2,3\}\) with \(n_2\equiv16\equiv0\pmod2\) gives \(n_2=2\), and \(n_1=(16-3\cdot2)/2=5\). The blocks have sizes \(10=2\cdot5\) and \(6=3\cdot2\), with \((s_b,t_b)=(2,5)\) and \((3,2)\).

**5.2.** The triangles of the block are indexed by \((i,u,v)\) with \(i\in I_b\), so there are \(r^2s_bt_b=(rs_b)(rt_b)\) link edges at \(O\) from this block, and by the proof of Lemma 3.1 at most one between any \(L\)- and \(R\)-direction. So every pair is joined exactly once.

**5.3.** The incidence graph is bipartite, so its cycles have even length; without cycles of length at most \(10\), they have length at least \(12\), and the argument of Lemma 3.1 gives angular length at least \(12\pi/5=2\pi+2\pi/5\).

**5.4.** \(|S|^h-1\le|S|^h-[z\in S^h]\le|S|^h\) and \(\bigl(q/100-1\bigr)^h\le|S|^h\le(q/100)^h\), so \(|S|^h=(c+o(1))q^h\); and \(q^{h-1}\le J\le q^h/(q-1)\), so \(J=(1+o(1))q^{h-1}\).

**5.5.** For \(u=u'\) the word is \(g_{iuv}g_{iuv}^{-1}g_{iuv'}g_{iuv'}^{-1}=1\); for \(v=v'\) it is \(g_{iuv}g_{iu'v}^{-1}g_{iu'v}g_{iuv}^{-1}=1\).

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Sections 2.2 and 2.3. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
