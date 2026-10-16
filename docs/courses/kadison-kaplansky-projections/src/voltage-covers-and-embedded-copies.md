# Voltage covers and embedded copies

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group of the course is defined by a graphical presentation whose relator graphs are the components of a *voltage cover* \(P\) of the tower \(Y\): a vertex of \(P\) is a vertex of \(Y\) together with an element of a torsion-free group \(F\), and each edge changes that element by its *voltage*. Under a girth condition on \(P\), which a later lesson establishes for suitable random voltages, every component of \(P\) embeds in the Cayley graph. The argument is the diagram argument of [Graphical presentations and coned diagrams](course:irrational-trace-and-baum-connes/graphical-presentations-and-coned-diagrams), with one new feature: relators are attached to actual closed walks in \(P\), and two faces may be merged only when their walks are aligned by a deck transformation [OpenAI-KK, Sections 7.1 and 7.2].

- The input (Section 1).
- Voltage covers (Section 2).
- The presentation and the label maps (Section 3).
- Diagrams with source walks (Section 4).
- Reduction rules (Section 5).
- Short arcs and the Euler count (Section 6).
- Embeddings and indexed copies (Section 7).

## 1. The input

The geometric lessons use only the following properties of the tower \(Y\) of [Pruning and recovery of long paths](pruning-and-recovery-of-long-paths.md), Proposition 4.1. It is a countable graph of maximum degree at most \(6D\), with an integer *layer* function that changes by at most one along an edge. Its oriented labels are folded, and positive labels and formal inverses are disjoint alphabets. A nonbacktracking path that begins in layer \(i\) and has length at least \(L_i=100H_i/\log_2d\) is determined, including its position in \(Y\), by its word. Refining the labels by additional tags preserves both properties. Along a walk of length at most \(aH_i/\log_2d\) from layer \(i\), every layer \(j\) met satisfies \(|H_j/H_i-1|\le a/\log_2d\) (Lemma 1.1 of [Streams, slots and slot evaluations](streams-slots-and-slot-evaluations.md)), and \(L_i>2\).

## 2. Voltage covers

Let \(F\) be a countable torsion-free group. Give each positive edge \(e\) of \(Y\) a *voltage* \(z_e\in F\), and its reverse the voltage \(z_e^{-1}\). The *voltage cover* \(P\) has the vertices \((v,f)\), \(v\in V(Y)\), \(f\in F\), and over each oriented edge \(e:v\to v'\) of \(Y\) the oriented edges
\[
(v,f)\longrightarrow(v',fz_e),\qquad f\in F .
\]
Labels, layers and positive orientations are pulled back from \(Y\), so \(P\) is folded and the projection \(P\to Y\) is a label-preserving covering map. The *deck transformations* \(\delta_a(v,f)=(v,af)\), \(a\in F\), are label-preserving automorphisms of \(P\). The deck group acts freely on vertices, and transitively on the lifts of every base vertex, hence on the lifts of every walk of \(Y\), since a lift is determined by its first vertex. It may move one component of \(P\) to another.

The *holonomy* of a closed walk \(e_1\cdots e_n\) of \(Y\) is \(z_{e_1}\cdots z_{e_n}\); a lift starting at \((v,f)\) ends at \((v,fz_{e_1}\cdots z_{e_n})\), so it is closed exactly when the holonomy is trivial, whatever \(f\) is.

**The girth condition (2.1).** For an absolute constant \(C_*\), fixed in the next lesson, no nonempty cyclically nonbacktracking closed walk in \(P\) based in layer \(i\) has length at most \(C_*H_i/\log_2d\).

## 3. The presentation and the label maps

Let \(S\) be the finite set of positive labels and \(R_P\) the set of the words of all closed walks in \(P\), and put
\[
\Gamma=\langle S\mid R_P\rangle,\qquad X=\operatorname{Cay}(\Gamma,S) .
\]
The Cayley graph is *formal*: its positive edges are the pairs \((h,\sigma)\), \(h\in\Gamma\), \(\sigma\in S\), from \(h\) to \(h\sigma\), with label \(\sigma\), and distinct pairs are distinct edges even if their ends coincide. Left translations preserve labels.

For a component \(C\) of \(P\), a vertex \(v_0\in C\) and \(h\in\Gamma\), there is exactly one label-preserving map \(\phi:C\to X\) with \(\phi(v_0)=h\): the image of the end of a walk from \(v_0\) is \(h\) times the value of its word, which does not depend on the walk because two walks with the same ends form a closed walk, whose word is a relator. These *label maps* are not yet known to be injective.

**Theorem 3.1** (geometric conclusion; OpenAI [OpenAI-KK, Theorem 7.1]). There are absolute constants \(C_*,C_\bullet\) such that for large \(\ell\), under the girth condition (2.1):

1. every label map \(\phi:C\to X\) is injective on vertices and edges;
2. the *indexed copies*, the pairs \((C,\phi)\) modulo \((C,\phi)\sim(\delta_aC,\phi\delta_a^{-1})\), \(a\in F\), admit a well-order and in each copy \(Q\) a ball \(B(Q)\) of its own graph such that every vertex that \(Q\) shares with an earlier copy lies in \(B(Q)\); the edges of \(Q\) with at least one end in \(B(Q)\) form a forest; and \(|V(B(Q))|\le2^{C_\bullet H_i}\) for every vertex of \(B(Q)\) over layer \(i\);
3. the sets \(D_Q\), the vertices of \(Q\) not in earlier copies, are pairwise disjoint, and deleting all edges of every \(Q\) with both ends in \(D_Q\) leaves a forest in \(X\);
4. \(\Gamma\) is torsion-free.

None of the constants depends on \(F\), the voltages, the number of components of \(P\) or \(|S|\).

This lesson proves statement 1. The next lesson proves statements 2 and 3, and [Torsion-freeness](torsion-freeness.md) proves statement 4.

## 4. Diagrams with source walks

We use van Kampen diagrams and plane maps as stated in (VK) and (MAP) of [Graphical presentations and coned diagrams](course:irrational-trace-and-baum-connes/graphical-presentations-and-coned-diagrams), Section 3: a word trivial in \(\Gamma\) has a diagram whose bounded faces read relators, at most \(N\) of them if the word is a product of \(N\) conjugates of relators; conversely the exterior word is a product of conjugates of the face words; a diagram has a unique label-preserving map to \(X\) from any base point; and the surgeries of deleting an edge between two faces, cutting along a bridge and contracting an edge behave as described there. These statements are proved in the course [Van Kampen diagrams](course:van-kampen-diagrams/plane-maps): Propositions 2.1, 2.2 and 2.3 of its lesson Plane maps and Theorems 3.1, 4.1 and 5.1 of its lesson [Van Kampen's lemma](course:van-kampen-diagrams/van-kampens-lemma).

In the diagrams of this course, every bounded face \(f\) carries a *source walk*: a closed walk in \(P\) whose word is the contour word of \(f\), read from a vertex in a direction. Equal words are never identified with equal walks. Two incidences of an edge \(e\) of a diagram, on two faces or on a face and an adjustable side, are *aligned* if, read in the same direction, their source edges in \(P\) differ by a deck transformation. If the two incidences of an edge on two distinct bounded faces are aligned, deleting \(e\) merges the faces, and the two source walks, after applying the deck transformation to one of them, splice into a closed walk in \(P\) that reads the merged contour; this is again a relator, because all closed walks of \(P\) are relators, including those with backtracks.

**Two minimization problems.** (a) *Injectivity failures.* Suppose some label map identifies two distinct vertices of its component. Among all label maps, all pairs of distinct source vertices with equal images, all walks in \(P\) between them and all diagrams for the image of the walk as a closed word in \(X\), choose one that minimizes first the number \(J\) of bounded faces and then the number of edges. The exterior has one *adjustable side*: the source walk, with its endpoints in \(P\) required to be distinct but allowed to vary, and one marked vertex where it begins and ends.

(b) *Loops in the coned graph.* Once the label maps are injective, let \(\widehat X\) be \(X\) with one new vertex \(c_Q\), the *center*, for every indexed copy \(Q\), joined by one edge, a *spoke*, to every vertex of \(Q\). A closed walk in \(\widehat X\) starting at a group vertex is divided into *sides*: each edge of \(X\) is a *fixed* side, and each passage \(x\to c_Q\to y\) is an *adjustable* side, to be inflated to a source walk in the component of \(Q\) from the source of \(x\) to that of \(y\). All side breaks are marked, so \(m\) sides give at most \(m\) marked vertices. Among all diagrams of all inflations, minimize \(J\) and then the number of edges.

## 5. Reduction rules

**Lemma 5.1** (reduction rules; [OpenAI-KK, Lemma 7.2]). In a minimal diagram of either problem:

1. no bounded face has a freely trivial word;
2. no edge between two distinct bounded faces has aligned incidences, and no edge between a bounded face and an adjustable side has aligned incidences;
3. no unmarked vertex has degree one, and no bridge has both its incidences on one bounded face.

*Proof.* (1) A freely trivial face word can be omitted from the expression of the exterior word as a product of conjugates of face words, and (VK) gives a diagram of the same exterior with fewer bounded faces; the source walks of the remaining faces are kept.

(2) For two distinct bounded faces, delete the edge and splice the aligned source walks as above. A bounded face adjacent to an adjustable side along an edge with aligned incidences is absorbed into that side: replace the traversal of the edge in the side by the rest of the contour of the face, with the source walk of the face moved by the aligning deck transformation; the endpoints of the side are unchanged. In both cases \(J\) decreases.

(3) At an unmarked vertex of degree one, the contour turns back along the same edge; by foldedness this is a backtrack of the assigned source walk, inside one adjustable side if the corner is exterior, since a break would be marked. Erasing the leaf keeps all assignments and lowers the number of edges. If a bridge has both incidences on a bounded face \(f\), cutting it splits the diagram into two parts, and the exterior contour with its marked positions lies in one of them; the contour of \(f\) makes one excursion through the other part, along the bridge and back. The other part, with the bridge as a stem, is a diagram for the word of that excursion with fewer than \(J\) faces. The two ends of the source excursion have equal images; in problem (b) the label maps are injective, so these ends coincide, and in problem (a), if they were distinct, the excursion and its diagram would be an injectivity failure with fewer faces, against minimality. So the source excursion is closed, and it can be removed from the source walk of \(f\), together with the bridge and the other part. The number of faces does not increase and the number of edges decreases. \(\square\)

## 6. Short arcs and the Euler count

Suppress every unmarked vertex of degree two in a minimal diagram. The resulting edges are *arcs*; an arc remembers its edge path and its length, and loops are allowed. Along an arc the incidence on each of its two sides is constant: a bounded face, or one side of the exterior.

**Lemma 6.1** (short arcs; [OpenAI-KK, Lemma 7.3]). Let \(C_*\ge10^4\) and \(\ell\) be large. In a minimal diagram:

1. every arc incident with a bounded face has length less than \(L_i\), read from an end in layer \(i\), on each of its two assignments, also when the other incidence is an adjustable side;
2. every bounded face has at least twenty arc incidences;
3. if \(b\) is the number of arcs, \(J\) the number of bounded faces and \(m\) the number of marked vertices, then
\[
\begin{gathered}
b\le3J+3m-3,\\
20J\le2b,\\
b\le6m .
\end{gathered}\tag{6.1}
\]

*Proof.* (1) An arc of length at least three has a freely reduced word: otherwise two consecutive edges with cancelling labels meet at an unmarked vertex of degree two, their outer ends are distinct, and contracting both identifies the outer ends, which have the same image; by foldedness the pair is a backtrack in every assigned source walk, so the contraction keeps all assignments and lowers the number of edges. An arc with an incidence on a fixed side has length one. Otherwise the arc has two source assignments, by Lemma 5.1(3) not on the same bounded face. If it had length at least \(L_i\) on one of them, its word would determine its projected nonbacktracking path in \(Y\), so both assignments would project to the same path, and their lifts would differ by a deck transformation: the incidences would be aligned, against Lemma 5.1(2). Arcs of length at most two are shorter than \(L_i>2\).

(2) Suppose a bounded face has fewer than twenty arc incidences. Let \(a\) be the length of its longest arc and \(i\) the layer of an end of that arc. Its perimeter is at most \(19a<20L_i=2000H_i/\log_2d\), so every layer \(j\) on the face has \(H_j\ge H_i/2\) for large \(\ell\). The face word is not freely trivial by Lemma 5.1(1). Cancelling backtracks in the source walk of the face, and then around its base point, gives by foldedness a nonempty cyclically nonbacktracking closed walk in \(P\), based in some layer \(j\), of length less than \(2000H_i/\log_2d\le4000H_j/\log_2d\), which is less than \(C_*H_j/\log_2d\), contradicting (2.1).

(3) Let \(v\) be the number of vertices after suppression. The suppressed diagram is a connected plane graph with \(J+1\) faces, so Euler's formula gives \(b=v+J-1\). Unmarked vertices have degree at least three, so \(2b\ge3(v-m)\), which gives the first inequality. Each arc has two incidences, so (2) gives \(20J\le2b\). Together, \(14J\le6m-6\) and \(b\le\frac{30}7(m-1)\le6m\). A diagram consisting of one marked vertex satisfies (6.1) as well. \(\square\)

## 7. Embeddings and indexed copies

**Proposition 7.1** (embeddings; [OpenAI-KK, Proposition 7.4]). Every label map \(C\to X\) is injective on vertices and on formal edges.

*Proof.* Suppose an injectivity failure exists, and take a minimal diagram of problem (a), with \(m=1\). By (6.1), \(20J\le2b\le6J\), so \(J=0\): the diagram is a tree, and its exterior word, the word of the source walk, is freely trivial. In a folded graph a walk with freely trivial word returns to its start: successive cancelling pairs are backtracks. So the two source endpoints coincide, a contradiction.

Two oriented source edges with the same image have the same initial image and the same label; by injectivity on vertices their initial vertices coincide, and by foldedness so do the edges. \(\square\)

An *indexed copy* is a pair \((C,\phi)\) of a component and a label map, modulo \((C,\phi)\sim(\delta_aC,\phi\delta_a^{-1})\), \(a\in F\). It remembers its source component and its source vertices up to deck alignment, in addition to its image, which is an embedded subgraph of \(X\) isomorphic to \(C\).

**Lemma 7.2** (distinct copies). If walks in two indexed copies have the same word, are aligned, and have the same image at one point, the two indexed copies are equal. Consequently, an arc shared by the assignments of two different copies is shorter than \(L_i\) on either of them.

*Proof.* After moving one representative by the aligning deck transformation, the two label maps agree at one vertex of the same component, and by uniqueness of label maps they agree everywhere. For the second statement, an arc of length at least \(L_i\) on one assignment would, as in Lemma 6.1(1), make the two assignments aligned with equal images. \(\square\)

## 8. Exercises

**8.1** (easy). Let \(Y\) be a single loop edge \(e\) at a vertex \(v\) and \(F=\mathbb Z\) with \(z_e=1\). Describe \(P\), its components and the deck action.

**8.2** (easy). Show that the holonomy of a closed walk is changed by conjugation when the base point is moved along the walk, so that triviality of holonomy does not depend on the base point.

**8.3** (medium). In Lemma 5.1(3), explain why in problem (a) the minimization is taken over all injectivity failures and not only over diagrams of one fixed pair of source vertices.

**8.4** (medium). Check the inequality \(b\le\frac{30}7(m-1)\) from the first two inequalities of (6.1), and show that it forces \(J=0\) when \(m=1\).

## 9. Solutions

**8.1.** The vertices are \((v,n)\), \(n\in\mathbb Z\), with edges \((v,n)\to(v,n+1)\): one bi-infinite line, a single component. The deck transformation \(\delta_a\) shifts it by \(a\).

**8.2.** If the walk is \(e_1\cdots e_n\) with holonomy \(z_1\cdots z_n\), starting at the end of \(e_1\) gives \(z_2\cdots z_nz_1=z_1^{-1}(z_1\cdots z_n)z_1\).

**8.3.** The excursion cut off by a bridge is itself an injectivity failure, possibly between a different pair of source vertices; only the global minimality excludes it, by its smaller number of faces.

**8.4.** From \(20J\le2b\le2(3J+3m-3)\), \(14J\le6(m-1)\); then
\[
\begin{aligned}
b&\le3J+3(m-1)\\
&\le\frac97(m-1)+3(m-1)\\
&=\frac{30}7(m-1) .
\end{aligned}
\]
For \(m=1\) this gives \(J=0\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 7.1 and 7.2, Theorem 7.1, Lemmas 7.2 and 7.3, Proposition 7.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
