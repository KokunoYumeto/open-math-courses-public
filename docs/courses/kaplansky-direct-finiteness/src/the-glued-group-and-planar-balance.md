# The glued group and planar balance

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The counterexample is built from many copies of the finite group \(\mathbb F_\ell^2\), one for each point of a finite incidence system, glued along their lines according to the incidences. Gluing finite groups along subgroups can collapse them: relations in one copy combined with relations in another may force elements to become trivial. This lesson proves that no collapse happens when the incidence graph has girth at least \(12\). An equality \(s=1\) in the glued group is turned into a planar graph with weights that balance at all vertices but one; a minimal such graph has high vertex degrees and long faces, which contradicts Euler's formula.

- Incidence systems and the criterion (Section 1).
- The glued group (Section 2).
- Plane graphs (Section 3).
- The embedding lemma (Section 4).

## 1. Incidence systems and the criterion

An *incidence system* is a finite set \(V\) of *points* with a finite family \(\mathcal F\) of nonempty subsets of \(V\), the *lines*. Its *incidence graph* is the bipartite graph with one vertex for each point, one for each line, and an edge between \(v\) and \(f\) whenever \(v\in f\). The *girth* of a graph is the length of its shortest cycle, and is infinite for a forest. Since the incidence graph is bipartite, its cycles have even length; girth at least \(12\) excludes cycles of lengths \(4\), \(6\), \(8\) and \(10\). In particular two distinct lines share at most one point.

Lessons 3 to 5 prove the following criterion, which reduces the counterexample to finite data.

**Theorem 1.1** (incidence criterion; [OpenAI-DF2, Theorem 3.1]). Let \(\ell\) be an odd prime and \(K\) a finite field of characteristic two containing a primitive \(\ell\)-th root of unity \(\zeta\); put \(\kappa=\ell^2\). Let \((V,\mathcal F)\) be an incidence system with \(t=|V|\) points, in which every point lies on exactly \(\ell+1\) lines and whose incidence graph has girth at least \(12\). Suppose that an integer \(m\) and column vectors \(x_v\in K^m\), \(v\in V\), satisfy
\[
0<m<t\le m\kappa ,
\]
\[
\begin{gathered}
\sum_{v\in V}x_vx_v^{\mathsf T}=-I_m,\\
\sum_{v\in f}x_vx_v^{\mathsf T}=0\quad(f\in\mathcal F).
\end{gathered}
\]
Then there are a finitely presented group \(G\) containing an element of order \(\ell\) and \(a,b\in K[G]\) with \(ab=1\) and \(ba\ne1\).

The transpose \(x^{\mathsf T}\) is the plain transpose; no conjugation is involved. Since \(K\) has characteristic two, \(-I_m=I_m\); the sign is kept because the same identities make sense in any characteristic. This lesson uses only the regularity and the girth; the vectors enter in [Subgroup averages and character twists](subgroup-averages-and-character-twists.md).

## 2. The glued group

Fix an incidence system \((V,\mathcal F)\) in which every point lies on exactly \(\ell+1\) lines, \(\ell\) an odd prime. For each point \(v\) let \(K_v^0\) be a copy of the additive group \(\mathbb F_\ell^2\), and for each line \(f\) let \(L_f^0\) be a copy of \(\mathbb F_\ell\). The group \(\mathbb F_\ell^2\) has exactly \(\ell+1\) one-dimensional subspaces, its *lines through \(0\)*, and they cover it, meeting pairwise only in \(0\). For each point \(v\), choose injective homomorphisms
\[
\iota_{vf}:L_f^0\to K_v^0\qquad(f\ni v)
\]
whose images are the \(\ell+1\) distinct lines through \(0\), one for each line \(f\) through \(v\). Then every nonzero element of \(K_v^0\) is \(\iota_{vf}(c)\) for exactly one \(f\ni v\) and one \(c\ne0\).

**Definition 2.1.** The *glued group* \(N\) has one generator \(s_{f,c}\) for each line \(f\) and each \(0\ne c\in L_f^0\). A *signed word* \(s_{f_1,c_1}^{\varepsilon_1}\cdots s_{f_k,c_k}^{\varepsilon_k}\), \(\varepsilon_i=\pm1\), is a *defining relator* if some point \(v\) lies on every \(f_i\) and
\[
\sum_{i=1}^k\varepsilon_i\,\iota_{vf_i}(c_i)=0\quad\text{in }K_v^0 .
\]
\(N\) is the group with these generators and relators.

For each point \(v\) define \(\theta_v:K_v^0\to N\) by \(\theta_v(0)=1\) and \(\theta_v(\iota_{vf}(c))=s_{f,c}\) for \(c\ne0\). It is a homomorphism: for \(x,y\in K_v^0\), the word for \(\theta_v(x)\theta_v(y)\theta_v(x+y)^{-1}\), with the letters for zero elements omitted, is a defining relator at \(v\).

**Lemma 2.2.** The relators of length at most three define \(N\); in particular \(N\) is finitely presented.

*Proof.* The relators of length at most three include \(\theta_v(x)\theta_v(y)\theta_v(x+y)^{-1}\) and \(\theta_v(x)\theta_v(-x)\) for all \(v\) and \(x,y\in K_v^0\). In the group they define, each letter \(s_{f_i,c_i}^{\varepsilon_i}\) of a relator at \(v\) equals \(\theta_v(\varepsilon_i\iota_{vf_i}(c_i))\), and the product of these equals \(\theta_v\) of the sum, which is \(\theta_v(0)=1\). So every defining relator follows from the short ones. There are finitely many generators, hence finitely many words of length at most three. \(\square\)

The full list of relators is kept because it makes the planar argument below simpler.

## 3. Plane graphs

A *plane graph* is a finite connected graph, possibly with several edges between the same two vertices but without loops, drawn in the sphere without crossings. Each edge gives two *darts*, its two orientations. Around each vertex the incident darts have a cyclic order, and the darts leaving the vertex are *consecutive* if one follows the other in this order. We use the following standard facts, which are not proved in the programme.

**(PLANE)** ([Erickson, Sections 9.4, 9.5, 10.4 and 10.6]; [Diestel, Theorem 4.2.9]; Euler's formula also in [Discrete Mathematics](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B10): Levin, *Discrete Mathematics: An Open Introduction*, Section 4.3). Let \(\Gamma\) be a plane graph with \(n\) vertices, \(E\) edges and \(F\) faces (the components of the complement of the drawing).

1. Every dart \(d\) lies on the boundary of exactly one face, the face to its left. The *boundary walk* of a face visits its darts in a cycle, and after a dart \(d\) entering a vertex \(x\) comes the dart that leaves \(x\) along the edge next to the edge of \(d\) in the cyclic order at \(x\). The lengths of the boundary walks add up to \(2E\). A boundary walk traverses an edge and immediately returns along it only at a vertex of degree one.
2. (Euler's formula) \(n-E+F=2\).
3. If a vertex \(x\) has consecutive edges to two distinct vertices \(y_1\) and \(y_2\), a new edge from \(y_1\) to \(y_2\) can be drawn along these two edges, inside the face that contains the corner at \(x\) between them, and contracting this new edge, that is, identifying \(y_1\) with \(y_2\), gives again a plane graph.

The bipartite graphs below have *black* and *white* vertices, and every edge joins a black vertex to a white one.

## 4. The embedding lemma

**Lemma 4.1** ([OpenAI-DF2, Lemma 3.2]). If the incidence graph of \((V,\mathcal F)\) has girth at least \(12\), then every \(\theta_v:K_v^0\to N\) is injective.

*Proof.* Every nonzero element of \(K_v^0\) maps to a single generator, so it suffices to show that no generator \(s_{f,c}\) is trivial in \(N\). Suppose that \(s_{f,c}=1\) for some \(f\) and \(c\ne0\).

*From words to a plane graph.* Consider the equivalence relation on signed words generated by inserting or deleting a defining relator as a contiguous block. Every pair \(s_{g,y}s_{g,y}^{-1}\) and \(s_{g,y}^{-1}s_{g,y}\) is a defining relator, because the line \(g\) has a point. So the classes form a group under concatenation, with the universal property of the presentation, and two words are equal in \(N\) exactly when they are equivalent. Hence there are words \(w_0=s_{f,c},w_1,\ldots,w_T\), with \(w_T\) empty, each obtained from the previous one by inserting or deleting one defining relator as a block.

Write each \(w_j\) on the horizontal line at height \(j\), one point for each letter. Between heights \(j\) and \(j+1\), join the letters that persist by disjoint monotone curves, in their order. If a block is inserted, put a new *black* vertex at height \(j+\tfrac12\) in the gap where the block appears and join it to each new letter; if a block is deleted, put the black vertex in the gap where the block disappears and join it to each deleted letter. Because the block is contiguous, this star occupies one gap between the persisting curves, and the drawing has no crossings. Label the black vertex by a point \(v\) at which the relator has sum zero.

Every letter \(s_{g,y}^\varepsilon\) other than the first one is created at a black vertex and deleted at a black vertex, and its curve from creation to deletion is subdivided by a new *white* vertex labelled \(g\). Give the edge towards the creation vertex the weight \(\varepsilon y\in L_g^0\) and the edge towards the deletion vertex the weight \(-\varepsilon y\). The first letter \(s_{f,c}\) is not created; its curve starts at a white vertex labelled \(f\), which we call *exceptional*, and the edge from it to the deletion vertex gets the weight \(-c\).

Each edge joins a black vertex labelled \(v\) to a white vertex labelled \(g\) with \(v\in g\), and has a nonzero weight \(\omega\in L_g^0\). Write \(i(a)\) for the white label of an edge \(a\). The weights *balance*, at each black vertex \(x\), labelled \(v\), and at each white vertex \(y\) other than the exceptional one:
\[
\begin{aligned}
&\sum_{a\ni x}\iota_{v\,i(a)}\bigl(\omega(a)\bigr)=0,\\
&\sum_{a\ni y}\omega(a)=0,
\end{aligned}\tag{4.1}
\]
At a creation vertex the first sum is the sum of the inserted relator at \(v\), which is zero, and at a deletion vertex it is its negative. An ordinary white vertex has two edges with opposite weights. The exceptional white vertex has the single weight \(-c\ne0\), so its sum is nonzero. Keep the connected component of the exceptional vertex; it is a plane graph with these properties.

*A minimal graph.* Consider all plane graphs that are bipartite with black labels in \(V\), white labels in \(\mathcal F\), edges only between \(v\) and \(g\) with \(v\in g\), nonzero weights \(\omega(a)\in L^0_{i(a)}\), the balances (4.1), and exactly one white vertex, the exceptional one, whose sum \(\sum_{a\ni y}\omega(a)\) is nonzero. They need not come from words. Choose one, \(\Gamma\), with the least number of vertices and, among those, the least number of edges. The exceptional vertex has nonzero sum, so it has an edge.

*No parallel edges.* Two edges between the same black vertex \(x\), labelled \(v\), and white vertex \(y\), labelled \(g\), have weights in \(L_g^0\) and the same map \(\iota_{vg}\) at \(x\). Replace them by one edge with the sum of the weights, or delete both if the sum is zero, and keep the component of the exceptional vertex. Additivity keeps every balance and the exceptional sum, and the new graph is smaller. So \(\Gamma\) has no parallel edges.

*Consecutive neighbours have distinct labels.* Let \(x\) have degree at least two, with consecutive edges to \(y_1\) and \(y_2\). These are distinct vertices, since there are no parallel edges, and they have the same colour. If they had the same label, (PLANE)(3) would let us identify them. The result is again a plane graph of the comparison class: edges keep their weights and their other endpoints, the merged vertex has as balance the sum of the two balances, computed in the same group with the same maps \(\iota\) because the labels agree, and at most one of the two was exceptional, so the exceptional sum stays nonzero. It has fewer vertices than \(\Gamma\), which is impossible. So consecutive neighbours of every vertex of degree at least two have distinct labels.

*Degrees.* An ordinary white vertex of degree one would have a single nonzero weight with sum zero, which is impossible. A black vertex of degree one would have \(\iota_{v\,i(a)}(\omega(a))=0\) with \(\omega(a)\ne0\), impossible since \(\iota\) is injective. A black vertex of degree two has two consecutive neighbours, with distinct labels \(g_1\ne g_2\); its balance says that two nonzero vectors on the distinct lines \(\iota_{vg_1}(L^0_{g_1})\) and \(\iota_{vg_2}(L^0_{g_2})\) of \(K_v^0\) add to zero, which is impossible. So every black vertex has degree at least \(3\), every ordinary white vertex degree at least \(2\), and the exceptional vertex degree at least \(1\).

*Faces.* Map each vertex of \(\Gamma\) to its label; edges then map to edges of the incidence graph, and a boundary walk of a face maps to a closed walk in the incidence graph. At each turn of the boundary walk through a vertex of degree at least two, the walk arrives along one edge and leaves along the next edge in the cyclic order (PLANE)(1); the other endpoints of these two edges have distinct labels, so the image walk does not immediately return along the edge it came from. A turn through a vertex of degree one occurs only at the exceptional vertex, and only in the one face whose boundary contains its edge on both sides. Every other face therefore maps to a nonempty closed walk without immediate returns, including at the closing turn; such a walk contains a cycle (Exercise 5.3), so its length is at least the girth, \(12\).

*Counting.* Let \(n_b\), \(n_w\), \(n_f\) be the numbers of black vertices, white vertices and faces, and \(E\) the number of edges. Every edge has one black and one white end, so the degree bounds give \(3n_b\le E\) and \(2(n_w-1)+1\le E\). By (PLANE)(1), the boundary walks have total length \(2E\), and all faces but at most one have length at least \(12\), so \(12(n_f-1)\le2E\). Hence
\[
\begin{aligned}
n_b+n_w+n_f&\le\frac E3+\frac{E+1}2+\frac E6+1\\
&=E+\frac32 ,
\end{aligned}
\]
whereas Euler's formula (PLANE)(2) gives \(n_b+n_w+n_f=E+2\). This contradiction shows that \(s_{f,c}\ne1\). \(\square\)

From now on \(K_v\) denotes the image \(\theta_v(K_v^0)\le N\), a subgroup isomorphic to \(\mathbb F_\ell^2\), and \(L_f\) the subgroup \(\{1\}\cup\{s_{f,c}:c\ne0\}\), isomorphic to \(\mathbb F_\ell\) through any point of \(f\). For every \(v\in f\), \(L_f\) is the same subgroup of \(K_v\): it is generated by the shared generators \(s_{f,c}\). The \(\ell+1\) subgroups \(L_f\), \(f\ni v\), are the lines through the identity of \(K_v\), and they cover \(K_v\) and meet pairwise only in \(1\). Nothing is claimed about intersections of different \(K_v\).

## 5. Exercises

**5.1** (easy). Show that in Definition 2.1 the defining relators at a point \(v\) are exactly the words in the generators \(s_{f,c}\), \(f\ni v\), whose image under the homomorphism from the free group to \(K_v^0\) sending \(s_{f,c}\) to \(\iota_{vf}(c)\) is zero.

**5.2** (easy). Show that the girth of a bipartite incidence graph is at least \(6\) exactly when two distinct lines share at most one point.

**5.3** (medium). Let \(W=(z_0,z_1,\ldots,z_L=z_0)\), \(L\ge1\), be a closed walk in a graph without loops such that \(z_{j+1}\ne z_{j-1}\) for all \(j\), indices modulo \(L\). Show that \(W\) contains a cycle, and that \(L\) is at least the girth.

**5.4** (medium). Find a plane graph with two black vertices labelled \(v\), each of degree two with both neighbours labelled by the same line, that satisfies the balances (4.1), and explain why the minimal graph \(\Gamma\) cannot contain such a configuration around a vertex.

## 6. Solutions

**5.1.** A word in the letters \(s_{f,c}^{\pm1}\) with \(f\ni v\) is mapped to \(\sum_i\varepsilon_i\iota_{vf_i}(c_i)\); the defining condition at \(v\) is that this sum is zero.

**5.2.** A cycle of length \(4\) in the incidence graph is \(v,f,w,g\) with \(v\ne w\) and \(f\ne g\), both points on both lines; cycles have even length at least \(4\). So the girth is at least \(6\) exactly when no two distinct lines share two points.

**5.3.** Among all pairs \(j<j'\) with \(z_j=z_{j'}\) and \(0<j'-j\le L\), choose one with \(j'-j\) minimal. Then \(z_j,\ldots,z_{j'-1}\) are distinct. If \(j'-j\ge3\), they form a cycle. The value \(j'-j=1\) would mean an edge from a vertex to itself, a loop. If \(j'-j=2\), then \(z_{j+2}=z_j\), contradicting \(z_{j+2}\ne z_j\). So a cycle occurs, with length at most \(L\), hence \(L\) is at least the girth.

**5.4.** Take black vertices \(x_1,x_2\) labelled \(v\), white vertices \(y_1,y_2\) labelled \(g\ni v\), and edges \(x_1y_1\) and \(x_2y_2\) with weight \(\omega\), and \(x_1y_2\) and \(x_2y_1\) with weight \(-\omega\), \(\omega\ne0\). At each black vertex the balance is \(\iota_{vg}(\omega)-\iota_{vg}(\omega)=0\), at each white vertex \(\omega-\omega=0\), and the square is a plane graph. Around \(x_1\), the consecutive neighbours \(y_1\), \(y_2\) have the same label, so they could be identified, giving a smaller graph; the minimal graph has no such vertex.

## References

- [OpenAI-DF2] OpenAI, *A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two*, OpenAI Math Release preprint, 23 September 2026, Section 3 (Theorem 3.1 and Lemma 3.2). https://github.com/openai/math/tree/main/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026
- [Erickson] J. Erickson, *Computational Topology*, lecture notes, University of Illinois, 2023, Chapter 9 (Planar graphs: Sections 9.4 and 9.5, faces and rotation systems) and Chapter 10 (Sections 10.4 and 10.6: contraction in planar maps, Euler's formula), on the author's page. https://jeffe.cs.illinois.edu/teaching/comptop/2023/schedule.html
- [Diestel] R. Diestel, *Graph Theory*, 5th edition, free preview of Chapter 4 on the author's page, Theorem 4.2.9 (Euler's formula). https://www.math.uni-hamburg.de/home/diestel/books/graph.theory/preview/Ch4.pdf
