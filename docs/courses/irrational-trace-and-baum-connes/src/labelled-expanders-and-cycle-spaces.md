# Labelled expanders and cycle spaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The graphs \(\Theta_i\) of the construction are expanders of large girth, and they are labelled by Osajda's theorem so that the standing hypotheses (H1) to (H5) of [Graphical presentations and coned diagrams](graphical-presentations-and-coned-diagrams.md) hold. This lesson makes these choices, in an order in which no constant depends on a later one, and records the properties used later: a spectral gap and edge expansion, small tree-like balls, and code dimensions \(k_i\) with growing gaps [OpenAI-IT, Proposition 3.1]. It then proves that the space of finite cycles of the Cayley graph \(X\) is the direct sum of the cycle spaces of the copies [OpenAI-IT, Lemma 3.2], the first consequence of the simultaneous overlap bound of [Thin triangles and simultaneous overlaps](thin-triangles-and-simultaneous-overlaps.md).

- Expansion and balls in regular graphs (Section 1).
- The choice of data (Section 2).
- Cycle spaces (Section 3).

The following two standard results are not proved in the programme; they are recorded as open obligations of this course.

**(EXP)** (expanders of logarithmic girth; [Lubotzky, Theorem 2.21 and the paragraph after it, Propositions 1.3 and 1.5]). For a prime \(p\ge5\), let \(Y_p\) be the Cayley graph of \(\mathrm{SL}_2(\mathbb F_p)\) with respect to \(A^{\pm1},B^{\pm1}\), where \(A=\begin{pmatrix}1&3\\0&1\end{pmatrix}\) and \(B=\begin{pmatrix}1&0\\3&1\end{pmatrix}\). There are constants \(\tau>0\) and \(\rho>0\) such that every \(Y_p\) is a connected simple \(4\)-regular graph with \(p(p^2-1)\) vertices and girth at least \(\tau\log p\), and \(4I-\operatorname{Adj}_{Y_p}\ge\rho I\) on the orthogonal complement of the constant functions in \(\ell^2\) of its vertex set.

**(OSA)** (Osajda's labelling theorem; [Osajda, Theorem 2.7, Lemma 3.1 and Theorem 3.2]). Let \(\Theta_1,\Theta_2,\ldots\) be pairwise disjoint finite connected graphs of degree at most \(D\), with girths \(\sigma_i\to\infty\), and suppose that \(\operatorname{diam}\Theta_i\le A\sigma_i\) for a constant \(A\). Let \(0<\lambda\le\frac1{24}\) with \(1<\lfloor\lambda\sigma_i\rfloor<\lfloor\lambda\sigma_{i+1}\rfloor\) for all \(i\). Then there are a finite set \(S\) and a reduced labelling of the oriented edges of all the \(\Theta_i\) by \(S^{\pm1}\) such that: no label of a path without backtracking of length at least \(\lambda\sigma_i\) in \(\Theta_i\) is the label of another path without backtracking in any \(\Theta_j\); and for the group \(\Gamma\) defined by the labels of all closed walks, every map \(\phi_i:\Theta_i\to X\) of Lemma 2.1 of the lesson on graphical presentations is isometric on vertices.

## 1. Expansion and balls in regular graphs

Let \(Y\) be a finite connected simple \(d\)-regular graph with \(n\) vertices. For a set \(W\) of vertices, \(\partial W\) is the set of edges with one end in \(W\) and one outside. On \(\ell^2\) of the vertex set,
\[
\begin{aligned}
&\langle(dI-\operatorname{Adj})f,f\rangle\\
&\quad=\sum_{\{x,y\}}|f(x)-f(y)|^2 ,
\end{aligned}\tag{1.1}
\]
the sum over the edges, because every vertex has \(d\) edges.

**Lemma 1.1** (expansion from a gap). If \(dI-\operatorname{Adj}\ge\rho I\) on the orthogonal complement of the constants, then \(|\partial W|\ge\kappa\min\{|W|,n-|W|\}\) for every \(W\), with \(\kappa=\rho/2\).

*Proof.* Let \(w=|W|\) and \(f=\mathbf1_W-\frac wn\mathbf1\), which is orthogonal to the constants. Then \(\|f\|^2=w(1-\frac wn)^2+(n-w)\frac{w^2}{n^2}\), which equals \(\frac{w(n-w)}n\), and by (1.1) its energy is \(|\partial W|\), since \(f(x)-f(y)=\pm1\) on boundary edges and \(0\) on the others. So \(|\partial W|\ge\rho\,\frac{w(n-w)}n\ge\frac\rho2\min\{w,n-w\}\), because \(\max\{w,n-w\}\ge\frac n2\). \(\square\)

**Lemma 1.2** (logarithmic diameter). If \(|\partial W|\ge\kappa\min\{|W|,n-|W|\}\) for all \(W\), then \(\operatorname{diam}Y\le2\bigl(\log n/\log(1+\kappa/d)+1\bigr)\).

*Proof.* Let \(B_r(x)\) be the ball of radius \(r\) about a vertex \(x\). If \(|B_r(x)|\le n/2\), every boundary edge of \(B_r(x)\) ends in \(B_{r+1}(x)\setminus B_r(x)\), and each such vertex receives at most \(d\) of them, so \(|B_{r+1}(x)|\ge(1+\kappa/d)|B_r(x)|\). Hence \(|B_r(x)|>n/2\) for \(r=r_0=\lceil\log n/\log(1+\kappa/d)\rceil\). Two balls of radius \(r_0\) each containing more than half of the vertices meet, so any two vertices have distance at most \(2r_0\). \(\square\)

**Lemma 1.3** (tree balls). Let \(Y\) have girth \(\sigma\), and let \(r\ge0\) be an integer with \(2r+1<\sigma\). For every vertex \(x\), the ball \(B_r(x)\) with all the edges of \(Y\) between its vertices is a tree, and it has
\[
1+d\sum_{j=0}^{r-1}(d-1)^j
\]
vertices. Consequently \(n\ge1+d\sum_{j=0}^{r'-1}(d-1)^j\) for \(r'=\lfloor(\sigma-2)/2\rfloor\).

*Proof.* Choose shortest paths from \(x\) to the vertices of the ball that form a tree \(T\) (breadth-first search); they stay in the ball. An edge between two vertices \(u,v\) of the ball outside \(T\) would close, with the tree paths from \(u\) and \(v\) back to their last common vertex, a cycle of length at most \(d(x,u)+d(x,v)+1\le2r+1<\sigma\). So the ball with its edges is \(T\). In \(T\), each vertex at distance \(j<r\) from \(x\) has all its \(d\) neighbours in the ball, one of them its parent unless \(j=0\); so there are \(d(d-1)^{j-1}\) vertices at distance \(j\) for \(1\le j\le r\). The radius \(r'\) satisfies \(2r'+1\le\sigma-1\). \(\square\)

For fixed \(d\ge3\) the quotient
\[
Q_d(\sigma)=\frac{1+d\sum_{j=0}^{\lfloor\sigma/16\rfloor-1}(d-1)^j}{1+d\sum_{j=0}^{\lfloor(\sigma-2)/2\rfloor-1}(d-1)^j}
\]
tends to \(0\) as \(\sigma\to\infty\), because the numerator is at most \(3(d-1)^{\sigma/16}\) and the denominator at least \((d-1)^{(\sigma-4)/2}\). So in a \(d\)-regular graph of large girth, balls of radius \(\sigma/16\) are trees containing a small proportion of all vertices.

## 2. The choice of data

The constants are chosen in this order.

| Choice | Requirement |
|---|---|
| \(D_0,t,L_0\) | universal, from Proposition 2.2 and (3.1) of the lesson on thin triangles |
| \(\lambda\) | \(0<\lambda<\frac1{24}\) and \(12(L_0+1)\lambda\le\frac1{16}\) |
| \(d,\rho,\kappa,\eta,c\) | \(d=4\) and \(\rho\) from (EXP); \(\kappa=\rho/2\); \(\eta=\frac1{100}\); \(c=\frac\eta2\min\{\kappa,1\}\) |
| \((\Theta_i)\) | a subsequence of the \(Y_p\), Proposition 2.1 |
| \(S\) | one finite alphabet, from (OSA) |
| \(p\), codes | in [Codes and the lamp module](codes-and-the-lamp-module.md) |

**Proposition 2.1** (the data; [OpenAI-IT, Proposition 3.1]). There are graphs \(\Theta_1,\Theta_2,\ldots\) with a labelling over a finite set \(S\) that satisfy the standing hypotheses (H1) to (H5) with \(d=4\) and the \(\lambda\) above, and moreover, with \(n_i=|\operatorname{Vert}(\Theta_i)|\), \(k_i=\lfloor n_i/2\rfloor\) and \(\sigma_i\) the girth:

1. \(dI-\operatorname{Adj}_{\Theta_i}\ge\rho I\) on the orthogonal complement of the constants, and \(|\partial W|\ge\kappa\min\{|W|,n_i-|W|\}\) for every vertex set \(W\) of \(\Theta_i\);
2. \(n_i>100\), \(\sigma_i>\max\{16,20/c\}\), \(\lambda\sigma_i>3\), and \(1<\lfloor\lambda\sigma_i\rfloor<\lfloor\lambda\sigma_{i+1}\rfloor\);
3. every ball of radius at most \(\sigma_i/16\) in \(\Theta_i\), with all the edges between its vertices, is a tree with fewer than \(\eta n_i\) vertices;
4. \(k_1<k_2<\cdots\) and \(k_{i+1}-k_i\to\infty\).

Consequently, for every copy \(P\) and every ball \(B_P\) of Lemma 3.1 of the lesson on thin triangles, \(r_P\le\sigma(P)/16\), and \(B_P\) with the edges of \(P\) between its vertices is a tree with fewer than \(\eta|P|\) vertices.

*Proof.* By (EXP), the graphs \(Y_p\) are connected simple \(4\)-regular graphs with gap \(\rho\) off the constants, so Lemma 1.1 gives property 1 for each of them. Their numbers of vertices \(n_p=p(p^2-1)<p^3\) and their girths \(\sigma_p\ge\tau\log p>\frac\tau3\log n_p\) tend to infinity. By Lemma 1.2, \(\operatorname{diam}Y_p\le C\log n_p\le\frac{3C}\tau\sigma_p\) for a constant \(C\) depending only on \(\kappa\) and \(d\).

Choose primes \(p_1<p_2<\cdots\) inductively, each so large that \(Y_{p_i}\) has more than \(100\) vertices, girth greater than \(\max\{16,20/c,3/\lambda\}\), and \(Q_4(\sigma)<\eta\) for its girth \(\sigma\) (possible because \(Q_4(\sigma)\to0\)); and also so large that \(\lfloor\lambda\sigma_{p_i}\rfloor>\lfloor\lambda\sigma_{p_{i-1}}\rfloor\) and \(k_i-k_{i-1}\ge i\), where \(k_i=\lfloor n_{p_i}/2\rfloor\). Let \(\Theta_i\) be disjoint copies of the graphs \(Y_{p_i}\). Properties 1, 2 and 4 hold by construction, with \(1<\lfloor\lambda\sigma_1\rfloor\) because \(\lambda\sigma_1>3\). For property 3, a ball of radius \(r\le\sigma_i/16\) satisfies \(2r+1<\sigma_i\), since \(\sigma_i>16\); by Lemma 1.3 it is a tree, and its size divided by \(n_i\) is at most \(Q_4(\sigma_i)\), which is less than \(\eta\).

The sequence \((\Theta_i)\) satisfies the hypotheses of (OSA) with \(D=4\), \(A=3C/\tau\) and our \(\lambda\le\frac1{24}\). (OSA) gives the labelling over a finite set \(S\): it is reduced, which is (H2); its uniqueness statement for paths without backtracking contains (H4), because simple paths do not backtrack; and it gives (H5). (H1) and (H3) hold by construction.

Finally, \(r_P=\lfloor12(L_0+1)\lambda\sigma(P)\rfloor\le\sigma(P)/16\) by the choice of \(\lambda\), and \(B_P\) is the ball of radius \(r_P\) in \(P\cong\Theta_i\), so property 3 applies. \(\square\)

In the rest of the course all these data are fixed, together with \(\Gamma\), its Cayley graph \(X\) and the coned graph \(\widehat X\). Since \(\lambda<\frac1{12}\), \(X\) is simple (Proposition 1.2 of the lesson on thin triangles), and we identify an edge of \(X\) with the pair of its ends.

## 3. Cycle spaces

For a graph \(Y\), let \(Z_1(Y;\mathbb F_2)\) be the space of *finite cycles*: finite sets of edges in which every vertex has even degree, added by symmetric difference. A copy \(P\) is a subgraph of \(X\), so \(Z_1(P;\mathbb F_2)\subseteq Z_1(X;\mathbb F_2)\).

**Lemma 3.1** (direct sum of copy cycles; [OpenAI-IT, Lemma 3.2]). Every finite cycle of \(X\) is a sum of finite cycles of copies, and a sum of nonzero finite cycles of finitely many distinct copies is never zero:
\[
\begin{aligned}
&Z_1(X;\mathbb F_2)\\
&\quad=\bigoplus_PZ_1(P;\mathbb F_2).
\end{aligned}\tag{3.1}
\]

*Proof.* *Spanning.* A finite cycle is a sum of edge sets of closed walks: each component of its edges has only even degrees and so carries a closed walk using each of its edges once. Let \(c\) be a closed walk in \(X\), with a diagram \(D\) and the map \(\kappa\) of Lemma 4.2 of the lesson on graphical presentations, which sends every bounded face into a copy. By (MAP)1 every edge of \(D\) has its two sides on faces, so the sum modulo two of the edge sets of all face boundary walks, the unbounded one included, is zero. Hence the edge set of the exterior walk is, modulo two, the sum of the edge sets of the bounded faces, and applying \(\kappa\) gives the edge set of \(c\), modulo two, as a sum of edge sets of closed walks in copies, each a finite cycle of its copy.

*Independence.* Suppose \(z_1+\cdots+z_N=0\) with \(z_j\in Z_1(P_j;\mathbb F_2)\) nonzero for distinct copies \(P_1,\ldots,P_N\), \(N\ge1\). Fix a group vertex \(R\) and let \(P\) be one of the \(P_j\) whose center is farthest from \(R\), with cycle \(z\). By Lemma 3.1 of the lesson on thin triangles, every vertex that \(P\) shares with another \(P_j\) lies in the ball \(B_P\). Every edge of \(z\) occurs in some other \(z_j\), since the sum is zero; so both its ends lie in \(P\cap P_j\subseteq B_P\), and it is an edge of the tree that \(B_P\) spans in \(P\) (Proposition 2.1). So \(z\) is a nonempty set of edges of a tree with even degrees everywhere, which is impossible: a nonempty finite subgraph of a tree has a vertex of degree one. \(\square\)

The decomposition is algebraic: the coordinate \(\operatorname{pr}_P(z)\) of a cycle \(z\) in the summand of a copy \(P\) is in general not the set of edges of \(z\) that lie in \(P\), and it can contain edges that are not in \(z\). The next lessons use (3.1) through these coordinate projections \(\operatorname{pr}_P\).

## 4. Exercises

**4.1** (easy). For the cycle graph \(C_n\) (\(d=2\)), compute \(|\partial W|\) for an arc \(W\) of \(w\) consecutive vertices, and show that no inequality \(|\partial W|\ge\kappa\min\{w,n-w\}\) with \(\kappa>0\) independent of \(n\) can hold.

**4.2** (easy). For \(d=4\), show that a tree ball of radius \(r\) has \(2\cdot3^r-1\) vertices.

**4.3** (medium). In the *theta graph*, two vertices joined by three disjoint paths \(\pi_1,\pi_2,\pi_3\), let \(C_{ij}\) be the cycle \(\pi_i\cup\pi_j\). Show that \(C_{12}+C_{23}+C_{13}=0\), so the three cycle spaces do not form a direct sum, although any two of the cycles meet in a path. Which hypothesis of the independence argument fails?

**4.4** (medium). Let \(Y\) be \(d\)-regular with \(|\partial W|\ge\kappa\min\{|W|,n-|W|\}\) for every vertex set \(W\). Show that the number of vertices at distance exactly \(r+1\) from \(x\) is at least \(\frac\kappa d|B_r(x)|\) while \(|B_r(x)|\le n/2\).

## 5. Solutions

**4.1.** An arc has exactly two boundary edges when \(0<w<n\). For \(w=\lfloor n/2\rfloor\), the inequality would require \(2\ge\kappa\lfloor n/2\rfloor\), false for large \(n\).

**4.2.** \(1+4\sum_{j=0}^{r-1}3^j=1+4\cdot\frac{3^r-1}2\), which is \(2\cdot3^r-1\).

**4.3.** Every edge of \(\pi_1\), \(\pi_2\), \(\pi_3\) lies in exactly two of the three cycles, so the sum is zero. With any root, take the cycle \(C\) chosen as farthest; its intersection with the union of the other two is all of \(C\), not contained in a tree. The pairwise intersections are small, but no single tree contains all the overlaps of one cycle with the others; Lemma 3.1 of the lesson on thin triangles provides exactly such a simultaneous bound.

**4.4.** Each boundary edge of \(B_r(x)\) joins a vertex of \(B_r(x)\) to a vertex at distance \(r+1\), and each vertex at distance \(r+1\) is the end of at most \(d\) such edges. So their number is at least \(|\partial B_r(x)|/d\ge\frac\kappa d|B_r(x)|\).

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Section 3, Proposition 3.1 and Lemma 3.2. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
- [Lubotzky] A. Lubotzky, *Expander graphs in pure and applied mathematics*, Bulletin of the American Mathematical Society 49 (2012); arXiv:1105.2389, Definitions 1.1 and 1.2, Propositions 1.3 and 1.5, Theorem 2.21. https://arxiv.org/abs/1105.2389
- [Osajda] D. Osajda, *Small cancellation labellings of some infinite graphs and applications*, Acta Mathematica 225 (2020); arXiv:1406.5015, Section 2, Theorem 2.7, Lemma 3.1 and Theorem 3.2. https://arxiv.org/abs/1406.5015
