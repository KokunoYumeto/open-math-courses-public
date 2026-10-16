# Graphical presentations and coned diagrams

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group \(\Gamma\) of the construction is defined by a *graphical presentation*: the generators label the edges of finite graphs \(\Theta_i\), and every closed walk in these graphs becomes a relation. The Cayley graph \(X\) of \(\Gamma\) then contains translated copies of the graphs \(\Theta_i\). Joining every vertex of a copy to a new center gives the *coned graph* \(\widehat X\), whose geometry controls everything later in the course. This lesson sets up these objects and proves the basic counting estimate for van Kampen diagrams of closed walks in \(\widehat X\): in a minimal diagram, faces are long, the arcs where different copies meet are short, and there are few faces and arcs [OpenAI-IT, Section 2.1]. The next lesson, [Thin triangles and simultaneous overlaps](thin-triangles-and-simultaneous-overlaps.md), draws the geometric consequences.

- Labelled graphs and the group \(\Gamma\) (Section 1).
- Copies and the coned graph (Section 2).
- Diagrams (Section 3).
- Fillings with adjustable sides (Section 4).
- Short arcs and their number (Section 5).

## 1. Labelled graphs and the group \(\Gamma\)

Graphs may have loops and multiple edges unless they are called *simple*. Every edge has two *orientations*; an oriented edge \(e\) has a reverse \(\bar e\). A *walk* is a finite sequence of oriented edges, each ending where the next begins; its *length* is the number of edges. It *backtracks* if some oriented edge is followed by its reverse, and it is a *simple path* if its vertices are pairwise distinct.

**Standing hypotheses.** Throughout this lesson and the next one:

- **(H1)** \(d\ge3\), and \(\Theta_1,\Theta_2,\ldots\) are pairwise disjoint finite connected simple \(d\)-regular graphs; \(\sigma_i\) is the girth of \(\Theta_i\), the length of its shortest cycle.
- **(H2)** \(S\) is a finite set, \(S^{\pm1}=S\cup\{s^{-1}:s\in S\}\) its set of letters and their formal inverses, and every oriented edge \(e\) of every \(\Theta_i\) carries a label \(\ell(e)\in S^{\pm1}\) with \(\ell(\bar e)=\ell(e)^{-1}\). The labelling is *reduced*: distinct oriented edges leaving the same vertex have distinct labels.
- **(H3)** \(\lambda\) is a number with \(0<\lambda\le\frac1{12}\) and \(\lambda\sigma_i>3\) for all \(i\).
- **(H4)** (uniqueness of long paths) If a simple path of length at least \(\lambda\sigma_i\) in \(\Theta_i\) and a simple path in some \(\Theta_j\) have the same label, they are the same path.
- **(H5)** (embedding) The maps \(\phi_i\) of Lemma 2.1 below are isometric on vertices.

The label of a walk is the word of the labels of its edges. Lesson [Labelled expanders and cycle spaces](labelled-expanders-and-cycle-spaces.md) produces data satisfying all five hypotheses.

**Lemma 1.1** (walks below the girth). Let \(\Theta\) be a simple graph of girth \(\sigma\) with a reduced labelling.

1. A nonempty closed walk without backtracking has length at least \(\sigma\). A walk without backtracking of length less than \(\sigma\) is a simple path.
2. Two consecutive letters of the label of a walk cancel, \(\ell(e_{j+1})=\ell(e_j)^{-1}\), exactly when \(e_{j+1}=\bar e_j\). Hence the label of a walk without backtracking is a freely reduced word, and a closed walk of length less than \(\sigma\) has a freely trivial label.

*Proof.* (1) Let \(v_0,v_1,\ldots,v_k\) be the vertices of a walk without backtracking, and suppose two of them coincide; take \(j\) smallest with \(v_j=v_i\) for some \(i<j\). The vertices \(v_i,\ldots,v_{j-1}\) are distinct. Since \(\Theta\) is simple, \(j-i=1\) would be a loop and \(j-i=2\) would be a backtrack, so \(j-i\ge3\) and \(v_i,\ldots,v_j\) is a cycle; hence \(k\ge j-i\ge\sigma\). A nonempty closed walk has \(v_k=v_0\), and a walk of length less than \(\sigma\) has no repeated vertex.

(2) The oriented edges \(e_{j+1}\) and \(\bar e_j\) both leave the endpoint of \(e_j\), and \(\ell(\bar e_j)=\ell(e_j)^{-1}\); since the labelling is reduced, their labels agree only if they are equal. Deleting backtracks from a closed walk of length less than \(\sigma\), one pair at a time, deletes cancelling pairs of letters and ends with a closed walk without backtracking of length less than \(\sigma\), which is empty by (1). \(\square\)

Let \(R\) be the set of labels of all closed walks in all the graphs \(\Theta_i\), and
\[
\Gamma=\langle S\mid R\rangle .
\]
The set \(R\) is closed under inversion and cyclic permutation of words, since these correspond to reversing and rotating closed walks. Let \(X\) be the *Cayley graph* of \(\Gamma\): its vertices are the elements of \(\Gamma\), and for every \(h\in\Gamma\) and \(s\in S\) there is one edge from \(h\) to \(hs\) with label \(s\), whose reverse has label \(s^{-1}\). That \(X\) is simple when \(\lambda<\frac1{12}\) is proved in the next lesson (Proposition 1.2 there); the arguments of this lesson do not use it. From each vertex \(h\) and for each letter \(a\in S^{\pm1}\) exactly one oriented edge leaves \(h\) with label \(a\), and it ends at \(ha\). So for every \(h\in\Gamma\) and every word \(w\) there is exactly one walk in \(X\) from \(h\) with label \(w\); it ends at \(h\bar w\), where \(\bar w\) is the value of \(w\) in \(\Gamma\), and it is closed exactly when \(\bar w=1\). We call this *determinism*. A *label-preserving map* between labelled graphs maps vertices to vertices and oriented edges to oriented edges with the same label, compatibly with endpoints and reversal.

## 2. Copies and the coned graph

**Lemma 2.1.** For each \(i\) fix a vertex \(o_i\) of \(\Theta_i\). There is exactly one label-preserving map \(\phi_i:\Theta_i\to X\) with \(\phi_i(o_i)=1\); it sends a vertex \(v\) to the value in \(\Gamma\) of the label of any walk from \(o_i\) to \(v\).

*Proof.* Two walks from \(o_i\) to \(v\) give a closed walk, the first followed by the reverse of the second, whose label is in \(R\); so their labels have the same value. An edge \(e\) from \(v\) to \(v'\) with label \(a\) satisfies \(\phi_i(v')=\phi_i(v)a\), so it can be sent to the edge of \(X\) from \(\phi_i(v)\) with label \(a\). Uniqueness follows from connectedness and determinism. \(\square\)

Hypothesis (H5) says that \(d_X(\phi_i(v),\phi_i(v'))=d_{\Theta_i}(v,v')\) for all vertices \(v,v'\) of \(\Theta_i\), where \(d\) denotes the graph distance. Then \(\phi_i\) is injective on vertices, and also on edges, because \(\Theta_i\) is simple.

Left multiplication by \(g\in\Gamma\) is a label-preserving automorphism of \(X\). For \(g\in\Gamma\) and \(i\ge1\), the *copy* \(P=P_{g,i}\) is the image of \(\psi_P=g\phi_i:\Theta_i\to X\), a subgraph of \(X\) isomorphic to \(\Theta_i\) through \(\psi_P\); the pair \((g,i)\) is its *index*, and we put \(\sigma(P)=\sigma_i\). We write \(d_P\) for the graph distance of \(P\) itself, the *intrinsic* distance; by (H5), \(d_X(x,y)=d_P(x,y)\) for vertices \(x,y\) of \(P\). The labelling of \(P\) inherited from \(X\) is reduced, by (H2). Distinct indices give distinct copies:

**Lemma 2.2** (distinct copies; [OpenAI-IT, Lemma 2.1]). Let \(P\) and \(Q\) be copies with different indices. No walk in \(X\) of length at least \(\lambda\sigma(P)\) is a simple path in both \(P\) and \(Q\). In particular, \(P\) and \(Q\) are different subgraphs of \(X\).

*Proof.* Let \(P=P_{g,i}\), \(Q=P_{g',j}\), and suppose a walk \(\pi\) of length at least \(\lambda\sigma_i\) is a simple path in \(P\) and in \(Q\). Its preimages \(\psi_P^{-1}(\pi)\) in \(\Theta_i\) and \(\psi_Q^{-1}(\pi)\) in \(\Theta_j\) are simple paths with the label of \(\pi\). By (H4) they are the same path, so \(i=j\) and they have the same first vertex \(v\). Then \(g\phi_i(v)=g'\phi_i(v)\) is the first vertex of \(\pi\), so \(g=g'\), a contradiction.

For the last statement: a walk without backtracking of length \(\lceil\lambda\sigma_i\rceil<\sigma_i\) in \(\Theta_i\) exists because \(d\ge2\), and it is a simple path by Lemma 1.1. Its image is a simple path in \(P\); if \(Q=P\) as subgraphs, it would also be a simple path in \(Q\). \(\square\)

**The coned graph.** Let \(\widehat X\) be the graph obtained from \(X\) by adding, for every copy \(P\), a new vertex \(c_P\), the *center* of \(P\), joined by one edge to every vertex of \(P\). The vertices of \(X\) are the *group vertices* of \(\widehat X\). All edges have length one, and \(d_{\widehat X}\) is the graph distance of \(\widehat X\); it is a geodesic metric on the vertices, whether or not \(\widehat X\) is locally finite. Two group vertices of the same copy have distance at most two, through its center.

## 3. Diagrams

The following two standard statements are not proved in the programme; they are recorded as open obligations of this course.

**(VK)** (van Kampen diagrams; [Bridson, Definition 4.1.1, Proposition 4.1.2, Theorem 4.2.2 and Section 4.3]). Let \(\langle S\mid R\rangle\) be a presentation of a group, possibly infinite, with \(R\) closed under inversion and cyclic permutation. A *diagram* for a word \(w\) in \(S^{\pm1}\) is a finite connected plane graph \(D\) whose oriented edges are labelled by \(S^{\pm1}\), reversal inverting labels, together with a *base vertex* on the boundary of the unbounded face, such that the boundary walk of the unbounded face, read from the base vertex, has label \(w\), and the boundary walk of every bounded face, read from a suitable vertex in a suitable direction, has label in \(R\).

1. If \(w\) is, in the free group on \(S\), a product of \(N\) conjugates of words in \(R\), then \(w\) has a diagram with at most \(N\) bounded faces. In particular, every word that is trivial in the group has a diagram.
2. Conversely, in a diagram, the boundary walk of the unbounded face is, in the fundamental group of the graph \(D\) at the base vertex, a product of conjugates of the boundary walks of the bounded faces, one for each bounded face. In particular its label is, in the free group, a product of conjugates of their labels. (Bridson's proof applies with every edge of \(D\) labelled by itself.)
3. For every vertex \(h\) of the Cayley graph there is exactly one label-preserving map from a diagram to the Cayley graph that sends the base vertex to \(h\).

**(MAP)** (plane maps; [Erickson, Sections 9.4, 9.5, 10.2, 10.4 and 10.6]). Let \(D\) be a finite connected plane graph, loops and multiple edges allowed, with \(V\) vertices, \(E\) edges and \(F\) bounded faces.

1. Each side of each edge lies on exactly one face. The boundary walk of a face runs along all the edge sides on that face; the lengths of all the boundary walks add up to \(2E\), and a boundary walk follows an edge by its reverse only at a vertex of degree one. Euler's formula reads \(V-E+F=1\).
2. If the two sides of an edge \(e\) lie on different faces, then \(D\setminus e\) is connected, and its faces are those of \(D\), except that the two faces at \(e\) become one face, whose boundary walk is obtained by cutting the two boundary walks at \(e\) and joining them.
3. If the two sides of an edge \(e\) lie on the same face \(f\), then \(D\setminus e\) has two components, and the boundary walk of \(f\) runs along \(e\), then through one component, \(D_2\), then back along \(e\), then through the other, \(D_1\). If \(f\) is bounded, \(D_1\) is the component containing the boundary walk of the unbounded face; if \(f\) is unbounded, either component may be called \(D_1\). Then \(D_1\) is a connected plane graph whose faces are the faces of \(D\) whose boundary walks lie in \(D_1\), together with \(f\), whose boundary walk is shortened by deleting \(e\), the part in \(D_2\) and the reverse of \(e\); its unbounded face is the unbounded face of \(D\), shortened in this way if \(f\) is unbounded.
4. Contracting an edge that is not a loop gives a connected plane graph with the same faces, whose boundary walks are those of \(D\) with that edge deleted.

## 4. Fillings with adjustable sides

**Closed walks with sides.** Consider a nonempty closed walk \(W\) in \(\widehat X\) that starts at a group vertex and is divided into \(m\ge1\) consecutive *sides*. Each side is either a *generator side*, one oriented edge of \(X\), or a *center passage*, two edges \(x\to c_P\to y\) through the center of a copy \(P\), its *assigned copy*. An *inflation* of \(W\) replaces each center passage \(x\to c_P\to y\) by some walk in \(P\) from \(x\) to \(y\), possibly empty if \(x=y\). An inflation is a closed walk in \(X\).

**Definition 4.1.** A *filling* of \(W\) consists of a diagram \(D\) over \(\langle S\mid R\rangle\), the label-preserving map \(\kappa:D\to X\) of (VK)3 sending the base vertex to the first vertex of \(W\), \(m\) marked positions on the boundary walk of the unbounded face, and an assigned copy \(Q_f\) for every bounded face \(f\), such that:

1. the boundary walk of the unbounded face, the *exterior walk*, is cut at the marked positions into \(m\) consecutive pieces, the *sides of \(D\)*; the \(k\)-th piece maps under \(\kappa\) onto the \(k\)-th side of \(W\) if that is a generator side, and onto a walk in the assigned copy from \(x\) to \(y\) if it is a center passage \(x\to c_P\to y\), the *adjustable* sides;
2. \(\kappa\) maps the boundary walk of every bounded face \(f\) to a closed walk in \(Q_f\).

The first marked position is at the base vertex. The vertices of \(D\) at the marked positions are the *marked vertices*; there are at most \(m\) of them, although the exterior walk may pass through a marked vertex at other positions as well.

**Lemma 4.2.** Every closed walk with sides has a filling.

*Proof.* Choose any inflation \(W'\). Its label \(w\) is trivial in \(\Gamma\), because \(W'\) is a closed walk in \(X\), so (VK)1 gives a diagram for \(w\), and (VK)3 the map \(\kappa\). By determinism, \(\kappa\) maps the exterior walk onto \(W'\), and we mark the positions where the sides of \(W'\) begin. A bounded face \(f\), read from a vertex \(u\) in a suitable direction, has a label \(r\in R\), the label of a closed walk \(\gamma\) in some \(\Theta_i\) from a vertex \(v\). Put \(g=\kappa(u)\phi_i(v)^{-1}\). The walk \(g\phi_i(\gamma)\) in \(X\) starts at \(\kappa(u)\) and has label \(r\); by determinism it is the image of the boundary walk of \(f\). It lies in \(P_{g,i}\), and we put \(Q_f=P_{g,i}\). \(\square\)

A filling is *minimal* if it has the smallest number \(F\) of bounded faces among all fillings of \(W\), with any inflation, and the smallest number of edges among fillings with \(F\) bounded faces. Minimal fillings exist by Lemma 4.2.

**Lemma 4.3** (minimal fillings). In a minimal filling of a closed walk with sides:

1. no bounded face has a freely trivial label, and every bounded face \(f\) has a boundary walk of length at least \(\sigma(Q_f)\);
2. no edge has its two sides on two different bounded faces with the same assigned copy;
3. no edge has one side on a bounded face \(f\) and the other side on an adjustable side of \(D\) whose assigned copy is \(Q_f\);
4. every vertex of degree one is marked;
5. no edge has both sides on the same bounded face.

*Proof.* In each case we produce a filling with fewer bounded faces, or with as many bounded faces and fewer edges.

(1) Suppose a bounded face has a freely trivial label. By (VK)2 the label \(w\) of the exterior walk is a product of conjugates of the labels of the bounded faces, one for each; omitting the trivial factor writes \(w\) as a product of \(F-1\) conjugates of words in \(R\), and (VK)1 gives a diagram for \(w\) with at most \(F-1\) bounded faces. By determinism its exterior walk maps onto the same inflation, and the proof of Lemma 4.2 assigns copies to its faces. This filling has fewer faces. For the second statement: by (2) of Definition 4.1 and the isomorphism \(\psi_{Q_f}\), the boundary walk of \(f\) corresponds to a closed walk in \(\Theta_i\) with the same label, which by Lemma 1.1 is freely trivial if its length is less than \(\sigma_i=\sigma(Q_f)\).

(2) Let the two sides of an edge \(e\) lie on bounded faces \(f_1\ne f_2\) with \(Q_{f_1}=Q_{f_2}=Q\). By (MAP)2, deleting \(e\) leaves a connected plane graph in which \(f_1\) and \(f_2\) are merged into one face whose boundary walk consists of the remaining edges of the two boundary walks; \(\kappa\) maps it to a closed walk in \(Q\), whose label is the label of a closed walk in \(\Theta_i\) and so lies in \(R\). The exterior walk is unchanged, and we assign \(Q\) to the merged face. This filling has one bounded face fewer.

(3) Let \(e\) have one side on a bounded face \(f\) and the other on the exterior walk, at a position inside an adjustable side with assigned copy \(Q_f\). By (MAP)2, deleting \(e\) merges \(f\) into the unbounded face; in the exterior walk, the occurrence of \(e\) is replaced by the rest of the boundary walk of \(f\). Since this occurrence lies inside one side, which maps into \(Q_f\), as does the boundary walk of \(f\), the new piece is a walk in \(Q_f\) with the same endpoints. The other sides and the marked positions are unchanged. This filling has one bounded face fewer.

(4) Let \(u\) be an unmarked vertex of degree one, with edge \(e\). Its two sides lie on one face, whose boundary walk runs along \(e\) to \(u\) and immediately back. If this is a bounded face, contracting \(e\) by (MAP)4 deletes this backtrack from its boundary walk, which still maps to a closed walk in the assigned copy. If it is the unbounded face, the two positions next to \(u\) in the exterior walk belong to the same side, because \(u\) is unmarked; this side is adjustable, since a generator side is a single edge whose ends are marked, and deleting the backtrack leaves a walk in its copy with the same endpoints. In both cases the number of edges drops and nothing else changes.

(5) Let both sides of \(e\) lie on one bounded face \(f\). By (MAP)3, \(D\setminus e\) has two components, and the exterior walk, which does not use \(e\), lies in one of them, \(D_1\). Keep \(D_1\) with its faces as described in (MAP)3: the boundary walk of \(f\) loses \(e\), its part in the other component and the reverse of \(e\), and still maps to a closed walk in \(Q_f\). The exterior walk and the marked positions are unchanged, the number of bounded faces does not increase, and the number of edges drops. \(\square\)

## 5. Short arcs and their number

Fix a minimal filling. Suppress every unmarked vertex of degree two, joining its two edges into one: the resulting edges are the *arcs*, each with the *length* of the edge path it replaces, and we write \(b\) for their number. Loop arcs are allowed. Along an arc, the faces on its two sides do not change; on the exterior, the side of \(D\) changes only at marked vertices, which are never suppressed. So each arc has two *incidences*, each a bounded face or a side of \(D\).

**Lemma 5.1** (short arcs and their number; [OpenAI-IT, Lemma 2.2]). In a minimal filling of a closed walk with \(m\) sides:

1. every bounded face \(f\) has a boundary walk of length at least \(\sigma(Q_f)\), and every arc incident to \(f\) has length less than \(\lambda\sigma(Q_f)\);
2. an arc whose two incidences have different assigned copies \(Q\ne Q'\), bounded faces or adjustable sides, has length less than \(\lambda\sigma(Q)\) and less than \(\lambda\sigma(Q')\); an arc with an incidence on a generator side has length one;
3. the number \(F\) of bounded faces and the number \(b\) of arcs satisfy

\[
\begin{gathered}
\Bigl(\frac1\lambda-6\Bigr)F\le6m-6,\\
F\le m-1,\\
b\le6m .
\end{gathered}\tag{5.1}
\]

*Proof.* (2) An arc with an incidence on a generator side lies inside that side, which is one edge. Consider an arc with incidences of different assigned copies \(Q\ne Q'\), of length at least three. Its label is freely reduced. Otherwise two consecutive edges \(e_1\), \(e_2\) of the arc have cancelling labels; their middle vertex is unmarked of degree two, and their outer endpoints are distinct vertices of \(D\), because the inner vertices of an arc are distinct and differ from its ends. Contracting \(e_1\) and then \(e_2\) by (MAP)4 identifies the three vertices, which is compatible with \(\kappa\) because the outer endpoints have the same image, and deletes from the two incident boundary walks a pair of steps that \(\kappa\) maps to an edge of \(X\) and its reverse. The images remain walks in the same copies with the same endpoints, and the result is a filling with as many faces and fewer edges, which is impossible.

So \(\kappa\) maps the arc to a walk in \(X\) without backtracking, by Lemma 1.1(2) applied in \(Q\). Suppose its length is at least \(\lambda\sigma(Q)\). Its first \(\lceil\lambda\sigma(Q)\rceil\) edges form a walk without backtracking in \(Q\) of length less than \(\sigma(Q)\), which is a simple path in \(Q\) by Lemma 1.1(1). Its vertices are distinct vertices of \(X\), so it is also a simple path in \(Q'\), which contains the image of the arc. This contradicts Lemma 2.2. Arcs of length at most two are shorter than \(\lambda\sigma(Q)\), since \(\lambda\sigma(Q)>3\).

(1) The first statement is Lemma 4.3(1). Let an arc be incident to \(f\). Its other incidence is not \(f\) itself, by Lemma 4.3(5); not a bounded face or an adjustable side with copy \(Q_f\), by Lemma 4.3(2) and (3). So it is a bounded face or an adjustable side with a different copy, or a generator side, and (2) applies.

(3) Let \(v_D\) be the number of vertices after suppression. Euler's formula (MAP)1 is unchanged by suppression: \(v_D-b+F=1\). Every unmarked vertex has degree at least three, by Lemma 4.3(4) and the suppression, and there are at most \(m\) marked vertices; so \(2b\ge3(v_D-m)\), and therefore
\[
b\le3F+3m-3 .
\]
By (1), a bounded face \(f\) has a boundary walk of length at least \(\sigma(Q_f)\) made of arcs of length less than \(\lambda\sigma(Q_f)\), so it has more than \(1/\lambda\) arc incidences. Every arc has two incidences, so
\[
\frac F\lambda\le2b\le6F+6m-6 ,
\]
which is the first inequality of (5.1). Since \(\frac1\lambda-6\ge6\), it gives \(F\le m-1\), and then \(b\le3(m-1)+3m-3\le6m\). \(\square\)

The constants do not depend on the graphs \(\Theta_i\), the alphabet \(S\) or \(\lambda\le\frac1{12}\); this uniformity is what the next lesson uses.

## 6. Exercises

**6.1** (easy). Let \(\Theta\) be a cycle of length \(5\) with its edges labelled \(a,b,a,b,c\) in order around the cycle. Is this labelling reduced? Write down the relators it contributes and the group \(\langle a,b,c\mid R\rangle\) when \(\Theta\) is the only graph.

**6.2** (easy). Let \(h\in\Gamma\) and \(i\ge1\). Show that the copies of type \(i\) that contain the vertex \(h\) are exactly the copies \(P_{h\phi_i(v)^{-1},i}\) for the vertices \(v\) of \(\Theta_i\), and that these are \(|\operatorname{Vert}(\Theta_i)|\) different copies.

**6.3** (medium). In a minimal filling of a closed walk with \(m=1\) side, show that there are no bounded faces. Deduce that a closed walk in \(\widehat X\) consisting of one center passage \(x\to c_P\to x\) has a filling by a single vertex, and that no edge of \(X\) is a loop.

**6.4** (medium). Let \(\gamma\) be a cycle of length \(\sigma_i\) in \(\Theta_i\), and let \(W\) be its image in \(X\), cut into \(\sigma_i\) generator sides. Show that a minimal filling of \(W\) has exactly one bounded face, and check the inequalities (5.1) for it.

## 7. Solutions

**6.1.** The edges leaving a vertex of the cycle are the two edges at it, read away from it. At the vertex between the two edges labelled \(a\) and \(b\), the outgoing labels are \(a^{-1}\) and \(b\), distinct; checking all five vertices, the outgoing pairs are \(\{c^{-1},a\}\), \(\{a^{-1},b\}\), \(\{b^{-1},a\}\), \(\{a^{-1},b\}\), \(\{b^{-1},c\}\), so the labelling is reduced. A closed walk from a vertex \(v\) of the cycle is, after deleting backtracks, a power of the cycle read from \(v\), so its label is freely equal to a power of a cyclic conjugate of \(ababc\). The group is \(\langle a,b,c\mid ababc\rangle\), which is free on \(a\) and \(b\), with \(c=(abab)^{-1}\).

**6.2.** \(h\in P_{g,i}\) means \(h=g\phi_i(v)\) for a vertex \(v\) of \(\Theta_i\), that is \(g=h\phi_i(v)^{-1}\). Distinct vertices \(v\) give distinct elements \(g\), because \(\phi_i\) is injective on vertices by (H5), so they give distinct indices, and by Lemma 2.2 distinct copies.

**6.3.** By (5.1), \(F\le m-1=0\), so a minimal filling is a tree. For \(W=x\to c_P\to x\), the empty inflation gives the filling by the single vertex \(x\). If an edge of \(X\) were a loop at \(h\), the closed walk consisting of this one generator side would have a minimal filling by a tree whose exterior walk maps onto a single edge; but the exterior walk of a tree runs along every edge twice and has even length, so it cannot consist of one edge.

**6.4.** The cycle \(\gamma\) has no backtracking, also cyclically, so the label of \(W\) is a nonempty cyclically reduced word, and it is not freely trivial. A filling without bounded faces is a tree, whose exterior label is freely trivial by (VK)2; so every filling has a bounded face. The cycle drawn in the plane, with its bounded face assigned to the copy containing \(W\), is a filling with one bounded face. So \(F=1\). In any filling with one bounded face \(f\), the label of \(W\) is freely conjugate to that of \(f\) by (VK)2, so the boundary walk of \(f\) has length at least \(\sigma_i\), and by (MAP)1 the number \(E\) of edges satisfies \(2E=\sigma_i+|\partial f|\ge2\sigma_i\); so the drawn cycle is a minimal filling. In it all \(\sigma_i\) vertices are marked, \(b=\sigma_i\), and (5.1) reads \(\frac1\lambda-6\le6\sigma_i-6\), \(1\le\sigma_i-1\) and \(\sigma_i\le6\sigma_i\); the first holds because \(\sigma_i>3/\lambda\).

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Section 2.1, Lemmas 2.1 and 2.2. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
- [Bridson] M. R. Bridson, *The geometry of the word problem*, in: Invitations to Geometry and Topology, Oxford University Press, 2002; on the author's page, Definition 4.1.1, Proposition 4.1.2, Theorem 4.2.2 and Section 4.3. https://people.maths.ox.ac.uk/bridson/papers/bfs/bfs.pdf
- [Erickson] J. Erickson, *Computational Topology*, lecture notes, University of Illinois, 2023, Chapter 9 (Sections 9.4 and 9.5) and Chapter 10 (Sections 10.2, 10.4 and 10.6), on the author's page. https://jeffe.cs.illinois.edu/teaching/comptop/2023/schedule.html
