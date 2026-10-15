# Disks, bands and boundary words

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A relation in a group with one added generator \(t\) can be drawn as a planar surface: disks whose boundaries read the relator \(w\) or its inverse, joined in pairs along their occurrences of \(t\) by bands. What is left of the boundary reads words in the coefficient group \(A\). This lesson sets up these surfaces, states the planar boundary theorem that the next lesson proves, and collects the combinatorics the proof uses: the boundary circles as cycles of a permutation, their number, computed from the Euler characteristic, and real "flows" that put a prescribed phase on each boundary circle [OpenAI-K, Section 4.1].

- Word disks and bands (Section 1).
- The planar boundary theorem (Section 2).
- Slots, corners and boundary cycles (Section 3).
- Counting boundary circles (Section 4).
- Flows with prescribed circulation (Section 5).

We use the following standard facts about surfaces in a sphere, the statement (SURF) of [Spherical arrangements and planar intervals](course:torsion-free-group-algebra-with-zero-divisors/spherical-arrangements-and-planar-intervals), Section 3. That statement is made for the disks and arcs of a spherical arrangement, but it uses only their position in the sphere, not their labels, so it applies to the disks and arcs below. It is not proved in the programme; a course proving it is recorded as an open obligation.

**(SURF)** (surfaces in the sphere; [Hatcher, Theorem 2.44, Section 2.2, Corollary 3.45, Proposition 2B.1]). Let \(D_1,\ldots,D_N\), \(N\ge1\), be pairwise disjoint closed disks in an oriented sphere \(S\), and \(\alpha_1,\ldots,\alpha_E\) pairwise disjoint arcs whose interiors lie outside the disks and whose endpoints are distinct points of the disk boundaries. There are pairwise disjoint closed disks \(B_1,\ldots,B_E\), the *bands*, such that \(B_j\) contains \(\alpha_j\) and meets the disks exactly in two short arcs of their boundaries around the endpoints of \(\alpha_j\); the rest of \(\partial B_j\) consists of two arcs, the *sides* of the band. Put \(\Sigma=D_1\cup\cdots\cup D_N\cup B_1\cup\cdots\cup B_E\). Then:

1. The closure of \(S\setminus\Sigma\) is the disjoint union of finitely many compact connected surfaces, the *regions*. Every boundary circle of \(\Sigma\) is a boundary circle of exactly one region, and every boundary circle of a region is one of \(\Sigma\).
2. \(\chi(\Sigma)=N-E\), and the Euler characteristics of the regions add up to \(2-N+E\).
3. A region with \(b\) boundary circles has Euler characteristic \(2-b\).
4. If two compact surfaces in \(S\), oriented by \(S\), meet along an arc of their boundaries and lie on opposite sides of it, their boundary orientations along that arc are opposite.
5. The closure of each component of the complement of a circle in \(S\) is a closed disk.

## 1. Word disks and bands

Fix a group \(A\) and a word
\[
\begin{gathered}
w=t^{s_1}a_1t^{s_2}a_2\cdots t^{s_n}a_n,\\
a_i\in A,\quad s_i\in\{1,-1\},\\
\sum_{i=1}^ns_i=\pm1 ,
\end{gathered}\tag{1.1}
\]
read cyclically; indices are taken modulo \(n\). Thus \(n\) is odd, and coefficients equal to \(1\) are allowed. Every unimodular element of \(A*\langle t\rangle\) is conjugate to a word of this form (Exercise 6.1), and conjugate relators have the same normal closure.

Let \(S\) be an oriented sphere. A *word disk* is a closed disk \(D\subset S\), oriented by \(S\), whose boundary circle, with the induced orientation, carries \(n\) pairwise disjoint closed intervals, the *slots*, separated by \(n\) arcs, the *corners*; each slot is indexed by an \(i\in\{1,\ldots,n\}\) and each corner carries an element of \(A\). It is *positive* if, in the boundary orientation, the slots appear in the order \(1,2,\ldots,n\) and the corner from slot \(i\) to slot \(i+1\) carries \(a_i\); then the boundary reads \(w\). It is *negative* if the slots appear in the order \(n,n-1,\ldots,1\) and the corner from slot \(i+1\) to slot \(i\) carries \(a_i^{-1}\); then the boundary reads
\[
w^{-1}=a_n^{-1}t^{-s_n}a_{n-1}^{-1}t^{-s_{n-1}}\cdots a_1^{-1}t^{-s_1}.
\]
The *traversal sign* of slot \(i\) is \(s_i\) on a positive disk and \(-s_i\) on a negative disk. The sign of a disk and the traversal sign of a slot are different data.

A *disk-and-band surface* for \(w\) consists of finitely many pairwise disjoint word disks in \(S\), at least one, together with pairwise disjoint arcs \(\alpha_1,\ldots,\alpha_E\) whose interiors lie outside the disks, such that every slot contains exactly one endpoint of one arc, in its interior, and the two slots at the ends of each arc have opposite traversal signs. By (SURF) we may take bands around the arcs, and we shrink the slots to the short arcs where the bands meet the disks; this changes no corner label. The surface is
\[
\Sigma=\bigcup_{\text{disks}}D\ \cup\ \bigcup_jB_j .
\]
Its *boundary words* are read along each boundary circle of \(\Sigma\), in its boundary orientation from \(S\): the product of the corner labels met along the way, ignoring the band sides. Changing the starting point conjugates the word, which does not affect whether it is \(1\) in \(A\).

## 2. The planar boundary theorem

**Theorem 2.1** (planar boundary theorem; [OpenAI-K, Theorem 4.1]). Let \(\Sigma\) be a connected disk-and-band surface for a word (1.1). If every boundary word of \(\Sigma\) except possibly one is trivial in \(A\), then the remaining boundary word is trivial as well.

The proof is the subject of [The planar boundary theorem](the-planar-boundary-theorem.md). The rest of this lesson collects what it needs. For a disconnected surface the theorem applies to each component separately, and this is how [From a relation to a planar surface](from-a-relation-to-a-planar-surface.md) uses it. The hypothesis that \(w\) is unimodular enters through the count of disks (Lemma 4.1) and through the fixed-space lemma of [A unitary with a large fixed space](a-unitary-with-a-large-fixed-space.md).

## 3. Slots, corners and boundary cycles

Let \(\Sigma\) be a disk-and-band surface and \(D\) the set of its slots. Define two permutations of \(D\):

- \(\sigma\) sends a slot to the next slot on the same disk, in the boundary orientation;
- \(\theta\) exchanges the two slots at the ends of each band; it is an involution without fixed points.

For a slot \(d\), let \(c_d\in A\) be the label of the corner from \(d\) to \(\sigma d\). By the definition of positive and negative disks,
\[
\begin{array}{c|c|c}
\text{disk}&\sigma\text{ on indices}&c_d\\\hline
+&i\mapsto i+1&a_i\\
-&i+1\mapsto i&a_i^{-1}
\end{array}\tag{3.1}
\]
Each slot is an arc of a disk boundary, traversed in the boundary orientation from its *start* to its *finish*.

**Lemma 3.1** (boundary circles). The boundary circles of \(\Sigma\) correspond to the cycles of the permutation \(\sigma\theta\). For a cycle \(z=(d_1,d_2,\ldots,d_{|z|})\), with \(d_{j+1}=\sigma\theta d_j\), the boundary word of the corresponding circle is
\[
r_z=c_{\theta d_1}c_{\theta d_2}\cdots c_{\theta d_{|z|}} .\tag{3.2}
\]

*Proof.* The boundary of \(\Sigma\) is the union of the corners and the band sides; the slots and the band ends lie inside \(\Sigma\), together with the rest of the disks and bands. Each corner joins the finish of a slot \(d\) to the start of \(\sigma d\), and along it \(\Sigma\) is locally the disk, so the boundary orientation of \(\Sigma\) runs along the corner from \(d\) to \(\sigma d\). Each band side joins an endpoint of one slot to an endpoint of the partner slot. Consider a band joining \(d\) to \(\theta d\) and the side that starts at the start of \(d\). The band lies outside both disks, so along each slot the band and the disk lie on opposite sides of the slot; by (SURF) 4, the boundary orientation of the band runs along the slot \(d\) from its finish to its start, and along \(\theta d\) from its finish to its start. Going around the band boundary in its own orientation, one therefore runs along \(d\) backwards, arrives at the start of \(d\), runs along a side, then along \(\theta d\) backwards from its finish. So the side that starts at the start of \(d\) ends at the finish of \(\theta d\), and the boundary orientation of \(\Sigma\) runs along it in this direction, agreeing with that of the band. Following \(\partial\Sigma\) from the start of a slot \(d\): a band side leads to the finish of \(\theta d\), and the corner \(c_{\theta d}\) leads to the start of \(\sigma\theta d\). Repeating, one returns to the start of \(d\) after one cycle of \(\sigma\theta\), having read (3.2). Every corner and every side is met exactly once in this way, so the cycles correspond to the boundary circles. \(\square\)

## 4. Counting boundary circles

**Lemma 4.1.** Let \(\Sigma\) be a disk-and-band surface for a word (1.1) with \(\sum_is_i=\varepsilon\in\{1,-1\}\).

1. \(\Sigma\) has equally many positive and negative disks, say \(k\) of each, and \(k\ge1\). It has \(2nk\) slots and \(nk\) bands.
2. If \(\Sigma\) is connected and has \(q\) boundary circles, then \(\chi(\Sigma)=2-q\), and
\[
q=nk-2k+2 .\tag{4.1}
\]
In particular \(q\ge1\).

*Proof.* (1) A positive disk has traversal signs adding up to \(\varepsilon\), and a negative disk to \(-\varepsilon\). Every band pairs two slots of opposite traversal signs, so the sum over all slots is \(0\): with \(k_+\) positive and \(k_-\) negative disks, \((k_+-k_-)\varepsilon=0\), so \(k_+=k_-=k\), and \(k\ge1\) because there is at least one disk. Each disk has \(n\) slots and each band uses two of them.

(2) By Lemma 4.2 below and (SURF) 1 and 3, the regions of \(S\setminus\Sigma\) correspond to the \(q\) boundary circles of \(\Sigma\) and each has Euler characteristic \(1\); by (SURF) 2, \(q=2-\chi(\Sigma)\). With \(N=2k\) disks and \(E=nk\) bands, \(\chi(\Sigma)=2k-nk\), which gives (4.1). \(\square\)

**Lemma 4.2** (regions of a connected surface). If \(\Sigma\) is connected, every region of \(S\setminus\Sigma\) has exactly one boundary circle, and it is the closed disk bounded by that circle on the side away from \(\Sigma\). In particular \(\Sigma\) is the complement in \(S\) of the interiors of \(q\) pairwise disjoint closed disks, one for each boundary circle.

*Proof.* Let \(\Omega\) be a region and \(C_1\) one of its boundary circles. By (SURF) 5, the closures of the two components of \(S\setminus C_1\) are closed disks \(D'\) and \(D''\). The surfaces \(\Omega\) and \(\Sigma\) share the boundary circle \(C_1\) and meet only along boundary circles (SURF 1), so near \(C_1\) they lie on opposite sides, say \(\Omega\) in \(D'\). The set \(\Omega\setminus C_1\) is connected and misses \(C_1\), so \(\Omega\subseteq D'\). The set \(\Sigma\cap\operatorname{int}D'\) is open in \(\Sigma\). It is also closed in \(\Sigma\): its closure could only add points of \(C_1\), and near \(C_1\) the side \(D'\) is occupied by \(\Omega\), whose points off its boundary circles are not in \(\Sigma\). It misses \(C_1\subseteq\Sigma\), so it is empty, because \(\Sigma\) is connected. Hence \(\operatorname{int}D'\) is a connected subset of \(S\setminus\Sigma\) that meets \(\Omega\) near \(C_1\); it lies in the component of \(S\setminus\Sigma\) whose closure is \(\Omega\), so \(D'\subseteq\Omega\), and \(\Omega=D'\) is a closed disk with the single boundary circle \(C_1\). \(\square\)

## 5. Flows with prescribed circulation

The proof of the planar boundary theorem puts a small real phase \(\eta_z\) on each boundary circle \(z\), with \(\sum_z\eta_z=0\), and realizes these phases by numbers attached to the slots.

**Lemma 5.1** (flows). Let \(\Sigma\) be connected, and let \((\eta_z)\) be real numbers indexed by the cycles of \(\sigma\theta\), with \(\sum_z\eta_z=0\). There are real numbers \(\gamma_d\), \(d\in D\), with
\[
\begin{gathered}
\gamma_{\theta d}=-\gamma_d\quad(d\in D),\\
\sum_{d\in z}\gamma_d=\eta_z\\
\text{for every cycle }z .
\end{gathered}\tag{5.1}
\]

*Proof.* Form the graph \(\mathcal G\) whose vertices are the cycles of \(\sigma\theta\) and whose edges are the pairs \(\{d,\theta d\}\), joining the cycles of \(d\) and \(\theta d\) (possibly equal). Since \(\Sigma\) is connected, the group generated by \(\sigma\) and \(\theta\) acts transitively on \(D\): slots on one disk are related by powers of \(\sigma\), and the two ends of a band by \(\theta\). This group is generated by \(\sigma\theta\) and \(\theta\) as well, so \(\mathcal G\) is connected. Choose a spanning tree. We assign to each edge \(\{d,\theta d\}\) a number \(\gamma_d=-\gamma_{\theta d}\); the contribution of the edge to a vertex \(z\) is the value on its end in \(z\) (both values, if both ends lie in \(z\)). Put \(\gamma=0\) on edges outside the tree. Proceed by induction on the number of vertices of the tree: if it has one vertex, \(\eta_z=0\) for that vertex and all \(\gamma=0\) work. Otherwise choose a leaf \(z\), joined to the tree by the edge \(\{d,\theta d\}\) with \(d\in z\); put \(\gamma_d=\eta_z\) and \(\gamma_{\theta d}=-\eta_z\), remove the leaf, and replace \(\eta\) at the neighbour \(z'\ni\theta d\) by \(\eta_{z'}+\eta_z\). The new values still add up to \(0\) on the smaller tree, and the induction hypothesis completes the assignment. \(\square\)

## 6. Exercises

**6.1** (medium). Let \(w\in A*\langle t\rangle\) have exponent sum \(\pm1\). Show that some cyclic conjugate of \(w\) has the form (1.1), after writing each power \(t^{e}\) as \(|e|\) letters \(t^{\pm1}\) separated by the coefficient \(1\).

**6.2** (easy). Let \(n=1\) and \(w=ta\). Show that a connected disk-and-band surface consists of one positive and one negative disk joined by one band, that \(q=1\), and that the boundary word is \(aa^{-1}\) up to conjugation, which is trivial. (So the theorem has no content for \(n=1\); compare Exercise 6.1 of [Equations over groups and the Kervaire conjecture](equations-over-groups-and-the-kervaire-conjecture.md).)

**6.3** (medium). Let \(n=3\) and \(w=ta_1ta_2t^{-1}a_3\), and consider one positive disk, with slots \(1^+,2^+,3^+\), and one negative disk, with slots \(1^-,2^-,3^-\). (a) Show that the pairing \(1^+\leftrightarrow1^-\), \(2^+\leftrightarrow2^-\), \(3^+\leftrightarrow3^-\) joins opposite traversal signs, and compute the cycles of \(\sigma\theta\) and the boundary words. (b) Do the same for \(1^+\leftrightarrow2^-\), \(2^+\leftrightarrow1^-\), \(3^+\leftrightarrow3^-\), and deduce from Lemma 4.1 that this pairing cannot be realized by arcs in a sphere.

**6.4** (easy). Show that \(\sum_z|z|=2nk\), where \(|z|\) is the length of the cycle \(z\).

## 7. Solutions

**6.1.** Write \(w=t^{e_1}b_1\cdots t^{e_l}b_l\) cyclically reduced up to conjugation, with \(b_j\in A\) and integers \(e_j\), conjugating so that it starts with a power of \(t\) (possible because \(\sum_je_j=\pm1\ne0\), so some \(e_j\ne0\)). Replace each \(t^{e_j}\) by \(|e_j|\) letters \(t^{\operatorname{sign}e_j}\) separated by the coefficient \(1\). The signs add up to \(\sum_je_j=\pm1\).

**6.2.** A positive disk has one slot with traversal sign \(s_1=\varepsilon\), a negative disk one with \(-\varepsilon\); a band joins opposite signs, so it joins a positive and a negative disk, and connectedness allows only one pair. Then \(q=1-2+2=1\). With \(D=\{d_+,d_-\}\), \(\sigma\) is the identity and \(\theta\) swaps them, so \(\sigma\theta\) is one cycle \((d_+,d_-)\), and \(r=c_{d_-}c_{d_+}=a^{-1}a=1\).

**6.3.** On the positive disk the traversal signs of \(1^+,2^+,3^+\) are \(+1,+1,-1\); on the negative disk those of \(1^-,2^-,3^-\) are \(-1,-1,+1\). By (3.1), \(\sigma\) is \(1^+\mapsto2^+\mapsto3^+\mapsto1^+\) and \(3^-\mapsto2^-\mapsto1^-\mapsto3^-\), and \(c_{1^+}=a_1\), \(c_{2^+}=a_2\), \(c_{3^+}=a_3\), \(c_{2^-}=a_1^{-1}\), \(c_{3^-}=a_2^{-1}\), \(c_{1^-}=a_3^{-1}\).

(a) Each pair joins signs \(+1\) and \(-1\). Then \(\sigma\theta\) has the cycles \((1^+,3^-)\), \((2^+,1^-)\), \((3^+,2^-)\): for instance \(1^+\mapsto\sigma(1^-)=3^-\mapsto\sigma(3^+)=1^+\). So \(q=3=nk-2k+2\), and by (3.2) the words are \(c_{1^-}c_{3^+}=a_3^{-1}a_3\), \(c_{2^-}c_{1^+}=a_1^{-1}a_1\) and \(c_{3^-}c_{2^+}=a_2^{-1}a_2\), all trivial. This surface is realized by a disk and its mirror image, joined across the mirror.

(b) Again each pair joins opposite signs. Now \(\sigma\theta\) is the single cycle \((1^+,1^-,3^+,2^-,2^+,3^-)\), so the surface would have one boundary circle, while a connected surface in a sphere with \(k=1\) and \(n=3\) has \(q=3\) by Lemma 4.1. (Its word, \(a_1^{-1}a_2a_2^{-1}a_1a_3^{-1}a_3\), is trivial too.)

**6.4.** Every slot lies in exactly one cycle of \(\sigma\theta\), and there are \(2nk\) slots.

## References

- [OpenAI-K] OpenAI, *The Kervaire theorem for groups*, OpenAI Math Release preprint, 24 September 2026, Section 4.1. https://github.com/openai/math/tree/main/preprints/The-Kervaire-Theorem-for-Groups-September-24-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
