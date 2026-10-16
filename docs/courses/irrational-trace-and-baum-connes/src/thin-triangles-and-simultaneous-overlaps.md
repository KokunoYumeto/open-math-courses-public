# Thin triangles and simultaneous overlaps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The counting of arcs in minimal fillings, Lemma 5.1 of [Graphical presentations and coned diagrams](graphical-presentations-and-coned-diagrams.md), has two geometric consequences for the coned graph \(\widehat X\). A walk between two vertices of a copy \(P\) that avoids the center of \(P\) forces them to be intrinsically close in \(P\), at distance proportional to the length of the walk times \(\lambda\sigma(P)\). And closed walks in \(\widehat X\) have linear fillings by short loops, so geodesic triangles are thin, with the constant \(D_0=10^6\), which depends on nothing at all. Together they give the key geometric statement of the construction [OpenAI-IT, Lemma 2.4]: seen from any root, all the overlaps of a copy \(P\) with the copies whose centers are no farther from the root lie in one intrinsic ball of \(P\) of radius about \(\lambda\sigma(P)\).

- Avoidance and simplicity (Section 1).
- Linear fillings and thin triangles (Section 2).
- Simultaneous overlaps (Section 3).

The standing hypotheses (H1) to (H5) and the notation of [Graphical presentations and coned diagrams](graphical-presentations-and-coned-diagrams.md) are in force: the graphs \(\Theta_i\), the group \(\Gamma\), its Cayley graph \(X\), the copies \(P\) with their intrinsic distances \(d_P\), the coned graph \(\widehat X\), closed walks with sides and their minimal fillings. Distances without subscript are distances in \(\widehat X\).

## 1. Avoidance and simplicity

A walk in \(\widehat X\) between group vertices visits centers only in two-edge passages \(y\to c_Q\to z\), because the neighbours of a center are group vertices. So such a walk, closed up, is a closed walk with sides: its edges between group vertices are generator sides, and its visits to centers are center passages.

**Proposition 1.1** (avoidance; [OpenAI-IT, Proposition 2.3(i)]). Let \(P\) be a copy and \(x,a\) vertices of \(P\). If a walk in \(\widehat X\) of length \(L\) from \(x\) to \(a\) does not visit \(c_P\), then
\[
d_P(x,a)\le12(L+1)\lambda\sigma(P).
\]

*Proof.* Close the walk by the center passage \(a\to c_P\to x\), the *designated side*. The result is a closed walk with \(m\le L+1\) sides, because the walk has at most \(L\) generator sides and center passages together; no side other than the designated one passes through \(c_P\). Take a minimal filling, with \(b\le6m\) arcs by Lemma 5.1 of the previous lesson. The designated side of the diagram is a walk from \(a\) to \(x\) made of whole arcs, because its ends are marked; its image under \(\kappa\) is a walk in \(P\) from \(a\) to \(x\).

We show that every arc on the designated side has length less than \(\lambda\sigma(P)\). Its other incidence is one of the following.

- A bounded face. Its copy is not \(P\), by Lemma 4.3(3) of the previous lesson, and Lemma 5.1(2) there applies.
- Another side of the diagram. A generator side gives an arc of length one, less than \(\lambda\sigma(P)\); an adjustable side passes through a center \(c_Q\) with \(Q\ne P\), and Lemma 5.1(2) applies.
- The designated side itself. This is impossible. All edges of such an arc have the unbounded face on both sides; take one of them, \(e\). The designated side runs along \(e\) at two positions, and since it is a contiguous piece of the exterior walk, the part of the exterior walk between these two positions lies inside the designated side and contains no side break. By (MAP)3, applied with \(D_1\) the component of \(D\setminus e\) that contains the base vertex (which sits at a side break, hence outside this part), deleting \(e\) and the other component gives a diagram whose exterior walk is the old one with \(e\), the part between the two positions and the reverse of \(e\) deleted. Only the designated side has changed; it is still a walk in \(P\) from \(a\) to \(x\), possibly empty. The number of bounded faces does not increase and the number of edges drops, against minimality.

The designated side is made of at most \(2b\le12m\le12(L+1)\) arc occurrences, each of length less than \(\lambda\sigma(P)\). Its image is a walk in \(P\) from \(a\) to \(x\) of length at most \(12(L+1)\lambda\sigma(P)\), which proves the bound; the empty walk is included. \(\square\)

**Proposition 1.2** (simplicity; [OpenAI-IT, Proposition 2.3(ii)]). If \(\lambda<\frac1{12}\), the graph \(X\) is simple: it has no loops, and no two edges join the same pair of vertices. In particular no generator has order two in \(\Gamma\), and distinct letters of \(S^{\pm1}\) have distinct values.

*Proof.* Let \(W\) be a closed walk in \(X\) of length one or two without backtracking, cut into generator sides, so \(m\le2\). By (5.1) of the previous lesson, \((\frac1\lambda-6)F\le6m-6\le6\) with \(\frac1\lambda-6>6\), so a minimal filling has \(F=0\): its diagram is a tree, and the label of \(W\) is freely trivial by (VK)2. But a walk of length one or two without backtracking has a nonempty freely reduced label, because cancelling consecutive letters in \(X\) correspond to backtracks, by determinism. So no such closed walk exists. A loop would be one, a pair of edges joining the same two vertices would give one, and so would a generator \(s\) with \(s^2=1\) (the walk \(h\to hs\to hs^2\)) or two letters with the same value. \(\square\)

## 2. Linear fillings and thin triangles

Short fillings give thin triangles. The *chain* of a walk is the sum of its oriented edges, with the convention that an oriented edge plus its reverse is zero; it does not change when a backtrack is inserted or removed, so homotopic closed walks have the same chain. Lemma 2.1 of [Thin triangles, overlap balls and the residual forest](course:kadison-kaplansky-projections/thin-triangles-overlap-balls-and-the-residual-forest) proves, by integrating a discrete one-form around a loop: *in a connected graph with unit edges in which the chain of every closed walk of length \(n\) is a sum of at most \(12n\) chains of closed walks of length at most four, every geodesic triangle is \(10^6\)-thin*, that is, every vertex on one side lies within distance \(10^6\) of a vertex on one of the other two sides. No local finiteness is assumed. The general statement, with \(Kn\) conjugates of closed walks of length at most \(M\), is [Belolipetsky–Paula, Teorema 8.22].

**Lemma 2.1** (short fillings; [OpenAI-IT, proof of Proposition 2.3]). Every closed walk in \(\widehat X\) of length \(n\ge1\) is, in the fundamental group of \(\widehat X\) at its first vertex, a product of at most \(12n\) conjugates of closed walks of length at most four.

*Proof.* If the walk starts at a center, it is conjugate, by its first edge, to its rotation starting at the next vertex, a group vertex; so we may assume that it starts at a group vertex. It is then a closed walk \(W\) with \(m\le n\) sides, as in Section 1. Take a minimal filling \((D,\kappa)\), with \(F\le m-1\) and \(b\le6m\) arcs.

For every arc choose a *standard path* in \(\widehat X\) between the images of its ends, compatibly with reversal: if the arc has an incidence on a generator side, it is a single edge, and its standard path is the image of that edge; otherwise choose one of its incidences, with assigned copy \(Q\), and take the two-edge path through \(c_Q\), which joins the images of the ends because the arc maps into \(Q\). Sending every vertex of \(D\) that survives the suppression to its image under \(\kappa\), and every arc to its standard path, gives a continuous map from \(D\) to \(\widehat X\), and so a homomorphism of fundamental groups.

*A bounded face.* Let \(f\) have copy \(P=Q_f\) and boundary walk made of arc occurrences \(A_1,\ldots,A_k\), from \(x_j\) to \(x_{j+1}\) (indices modulo \(k\)), all mapping into \(P\). The closed walk \(x_1\to c_P\to x_2\to\cdots\to c_P\to x_1\), which passes through \(c_P\) between consecutive points, reduces to the empty walk by cancelling backtracks. The standard path of \(A_j\) differs from \(x_j\to c_P\to x_{j+1}\) by a closed walk of length at most four (the standard path followed by \(x_{j+1}\to c_P\to x_j\)), which is trivial if the standard path already passes through \(c_P\). So the image of the boundary walk of \(f\) is a product of at most \(k\) conjugates of closed walks of length at most four.

*An adjustable side.* Let a side \(x\to c_P\to y\) of \(W\) be inflated in \(D\) to arc occurrences \(A_1,\ldots,A_k\) from \(x=x_1\) to \(y=x_{k+1}\) in \(P\). The walk \(x_1\to c_P\to x_2\to\cdots\to c_P\to x_{k+1}\), which passes through \(c_P\) between consecutive points, reduces to the passage \(x\to c_P\to y\); if \(k=0\), the passage \(x\to c_P\to x\) is itself a backtrack. As for a bounded face, replacing each standard path by the path through \(c_P\) costs at most \(k\) conjugates of closed walks of length at most four.

*Generator sides* are their own standard paths.

By (VK)2, the exterior walk of \(D\) is, in the fundamental group of \(D\), a product of conjugates of the boundary walks of the bounded faces; mapping by the standard paths, the standard image of the exterior walk is a product of conjugates of the standard images of the faces. Combining with the two comparisons above, \(W\) is a product of conjugates of closed walks of length at most four, at most one for each arc incidence on a bounded face or an adjustable side. There are at most \(2b\le12m\le12n\) such incidences. \(\square\)

**Proposition 2.2** (thin triangles; [OpenAI-IT, Proposition 2.3]). There is an integer \(D_0\ge1\), which depends on none of the data \(\Theta_i\), \(S\), \(\lambda\), such that for every geodesic triangle in \(\widehat X\) with vertices at vertices of \(\widehat X\), every vertex on one side lies within distance \(D_0\) of a vertex on one of the other two sides.

*Proof.* By Lemma 2.1, every closed walk of length \(n\) in \(\widehat X\) is homotopic to a product of at most \(12n\) conjugates \(g_jr_jg_j^{-1}\) of closed walks \(r_j\) of length at most four. The chain of a product is the sum of the chains, and the chains of \(g_j\) and \(g_j^{-1}\) cancel, so the chain of the walk is the sum of the chains of the \(r_j\). Lemma 2.1 of [Thin triangles, overlap balls and the residual forest](course:kadison-kaplansky-projections/thin-triangles-overlap-balls-and-the-residual-forest) applies with \(D_0=10^6\). \(\square\)

## 3. Simultaneous overlaps

Fix the constants
\[
\begin{gathered}
t=D_0+3,\\
L_0=2+2t+2D_0 .
\end{gathered}\tag{3.1}
\]

**Lemma 3.1** (simultaneous overlaps; [OpenAI-IT, Lemma 2.4]). Let \(R\) be a vertex of \(\widehat X\), \(P\) a copy with \(c_P\ne R\), and \(\gamma\) a geodesic from \(c_P\) to \(R\), whose first vertex after \(c_P\) is a vertex \(a\) of \(P\). Let \(B_P\) be the set of vertices \(y\) of \(P\) with \(d_P(y,a)\le r_P\), where
\[
r_P=\bigl\lfloor12(L_0+1)\lambda\sigma(P)\bigr\rfloor .\tag{3.2}
\]
Then every vertex shared by \(P\) and a copy \(Q\ne P\) with \(d(c_Q,R)\le d(c_P,R)\) lies in \(B_P\).

*Proof.* Write \(A=c_P\) and \(B=c_Q\), and let \(x\) be a vertex of \(P\cap Q\). Centers are not adjacent, so \(A,x,B\) is a geodesic of length two. Choose a geodesic \(\gamma'\) from \(B\) to \(R\). It does not pass through \(A\): otherwise \(d(B,R)=2+d(A,R)\), which is larger than \(d(A,R)\ge d(B,R)\). We find a walk from \(x\) to \(a\) of length at most \(L_0\) that avoids \(A\).

*If \(d(A,R)\ge t\),* let \(z\) be the vertex of \(\gamma\) at distance \(t\) from \(A\). Consider the geodesic triangle with sides \(A,x,B\), then \(\gamma'\), then \(\gamma\) backwards. The distance from \(z\) to each of \(A\), \(x\), \(B\) is at least \(t-2>D_0\), so by Proposition 2.2 there is a vertex \(y\) on \(\gamma'\) with \(d(y,z)\le D_0\). A shortest walk from \(y\) to \(z\) avoids \(A\), because \(d(A,z)=t>D_0\). Go from \(x\) to \(B\), along \(\gamma'\) to \(y\), along the shortest walk to \(z\), and back along \(\gamma\) to \(a\). This avoids \(A\). Since \(d(B,A)=2\), \(d(A,z)=t\) and \(d(z,y)\le D_0\), the triangle inequality gives \(d(B,y)\le2+t+D_0\), so the length of this walk is at most
\[
1+(2+t+D_0)+D_0+(t-1)=L_0 .
\]

*If \(d(A,R)<t\),* go from \(x\) to \(B\), along \(\gamma'\) to \(R\), and back along \(\gamma\) to \(a\). This avoids \(A\), and its length is \(1+d(B,R)+d(A,R)-1\), which is at most \(2d(A,R)<2t\le L_0\).

In both cases Proposition 1.1 gives \(d_P(x,a)\le12(L_0+1)\lambda\sigma(P)\), and since \(d_P(x,a)\) is an integer, \(d_P(x,a)\le r_P\). \(\square\)

The vertex \(a\), and with it the ball \(B_P\), depends only on \(R\), \(P\) and the geodesic \(\gamma\), not on \(Q\) or \(x\). This is what makes the bound *simultaneous*: one small ball contains the intersections of \(P\) with all the copies whose centers are no farther from \(R\). If \(\lambda\) is chosen so small that \(12(L_0+1)\lambda\le\frac1{16}\), as in the next lesson, then \(r_P\le\sigma(P)/16\).

## 4. Exercises

**4.1** (easy). Show that two vertices of a copy \(P\) at intrinsic distance \(k\) have distance \(\min(k,2)\) in \(\widehat X\).

**4.2** (medium). Let \(P\ne Q\) be copies sharing a vertex \(x\). Apply Lemma 3.1 with \(R=x\): show that \(d(c_P,x)=d(c_Q,x)=1\), and deduce that \(P\cap Q\) is contained in the intrinsic ball of radius \(r_P\) about \(x\) in \(P\).

**4.3** (medium). Show that in a graph of girth \(\sigma\), the vertices at distance at most \(r\) from a vertex \(x\), with all the edges between them, form a tree when \(2r+1<\sigma\). Deduce that if \(P\ne Q\) are copies with \(2r_P+1<\sigma(P)\), the vertices of \(P\cap Q\) with the edges of \(P\) between them form a forest.

**4.4** (easy). Check the arithmetic \(1+(2+t+D_0)+D_0+(t-1)=L_0\) and \(2t\le L_0\) for \(t=D_0+3\) and \(L_0=2+2t+2D_0\).

## 5. Solutions

**4.1.** Distinct vertices of \(P\) have \(\widehat X\)-distance at most two through \(c_P\). If they are adjacent in \(P\), their distance is one. If \(k\ge2\), they are not adjacent in \(X\), because \(d_X=d_P\) on \(P\) by (H5), and not equal, so their distance is two.

**4.2.** \(x\) is adjacent to both centers, so \(d(c_P,x)=d(c_Q,x)=1\), and \(c_P\ne x\). A geodesic from \(c_P\) to \(R=x\) is the single edge, so \(a=x\). Lemma 3.1 applies because \(d(c_Q,R)\le d(c_P,R)\), and puts every vertex of \(P\cap Q\) in the ball of radius \(r_P\) about \(x\).

**4.3.** Choose for every vertex \(u\) of the ball a shortest path from \(x\); it stays in the ball, and these paths can be chosen to form a tree \(T\) (breadth-first search). If an edge between two vertices \(u,v\) of the ball is not in \(T\), it closes with the tree paths from \(u\) and \(v\) to their last common vertex a cycle of length at most \(d(x,u)+d(x,v)+1\le2r+1<\sigma\), which is impossible. So the ball with all its edges is \(T\). By Exercise 4.2, \(P\cap Q\) lies in the ball of radius \(r_P\) about a vertex \(x\) of \(P\cap Q\); the edges of \(P\) between vertices of \(P\cap Q\) are edges of this tree, so they form a forest.

**4.4.** Collecting terms,
\[
\begin{aligned}
&1+(2+t+D_0)+D_0+(t-1)\\
&\quad=2+2t+2D_0=L_0 ,
\end{aligned}
\]
and \(L_0-2t=2+2D_0>0\).

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Section 2, Proposition 2.3 and Lemma 2.4. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
- [Belolipetsky–Paula] M. Belolipetsky and G. Teixeira Paula, *Introdução à Teoria Geométrica de Grupos*, arXiv:2409.17797, Section 8.2, Teoremas 8.18 e 8.22 (in Portuguese). https://arxiv.org/abs/2409.17797
