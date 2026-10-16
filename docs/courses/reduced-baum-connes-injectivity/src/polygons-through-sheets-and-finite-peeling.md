# Polygons through sheets and finite peeling

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Different sheets of the Cayley graph can meet, and the analytic part of the course needs to know how much. A closed walk that passes through \(k\) distinct sheets is a *polygon* with sides in the sheets; its reduced filling has short boundary arcs, and its boundary carries at most \(4k-6\) of them. So a polygon cannot have many long sides. From this, every finite family of sheets can be *peeled*: some sheet meets all the others inside one small ball, or at a single private vertex, and the edges at such a set form a forest. Peeling orders the family so that each sheet meets the later ones only in such an allowed set. The next lesson turns this into cycle coordinates and disjoint analytic domains [OpenAI-BCI, Section 6.5 and Section 7.1, Lemmas 6.5, 7.1 and 7.2].

- The exterior-arc bound (Section 1).
- Allowed removed sets (Section 2).
- Finite peeling (Section 3).

The setting of [The private completion and the graphical group](the-private-completion-and-the-graphical-group.md) is in force: the graphical group \(\Gamma\), its formal right Cayley graph \(\mathcal C\), the sheets with their source graphs and scales \(m_Q\), comparison paths, the constant \(L=1.003\), \(a\le10^{-6}\), and (2.2)-(2.4) there. We use (VK) and (MAP) through Lemma 3.1 of that lesson.

## 1. The exterior-arc bound

Contact vertices of a polygon must stay fixed while its sides are reduced; this is what the intrinsic distances of the next sections need.

**Lemma 1.1** (the exterior-arc bound; [OpenAI-BCI, Lemma 6.5]). Let \(Q_1,\ldots,Q_k\) be distinct sheets, \(k\ge2\), and let \(g_i\in Q_i\cap Q_{i+1}\), indices modulo \(k\); contacts may coincide. Choose a source path in \(Q_i\) from \(g_{i-1}\) to \(g_i\) for each \(i\). There are a finite diagram and a choice of such paths, with all the prescribed endpoints \(g_i\) fixed, such that:

1. each side is immersed; after keeping all junction vertices and suppressing the other vertices of degree two, every *arc* has two different projected occurrences in \(X\), each immersed, without private edges and of length less than \(Lm_Q(v)\) at its initial point; each nonconstant side is the concatenation of its arc occurrences on the unbounded face;
2. every bounded face has at least seven arc incidences;
3. if \(B\) is the number of arc incidences on the unbounded face, a bridge on it counted twice, then
\[
B\le4k-6 .\tag{1.1}
\]

A diagram without edges has \(B=0\), and then all sides are constant. In particular, a nonconstant side never ends at a private vertex, and a side whose endpoints have intrinsic distance greater than \(3.014\,m_Q(v)\), at its initial endpoint \(v\), has at least four arc incidences.

*Proof.* The concatenation of the chosen sheet paths is a closed walk of the Cayley graph, so its word is trivial in \(\Gamma\), and Lemma 3.1 of the previous lesson gives a diagram. Over all choices with the prescribed contacts fixed, minimize lexicographically the filling cost, the total length of the sides and the number of edges. Keep every boundary vertex carrying a junction; there are at most \(k\) such vertices.

The reductions at the beginning of the proof of Lemma 4.1 of the previous lesson apply unchanged: bounded source faces are nonempty and cyclically immersed, and each side is immersed. Coincident projected edges between two bounded faces are merged after deck alignment, lowering the filling cost. A bridge with both sides on one bounded face is removed as there; here no injectivity question arises, since the excursion has a trivial word by the cut-off component, and Lemma 4.1 of the previous lesson makes it close. The component containing the unbounded face keeps all marked contacts.

If a bounded face and a side have coincident projected occurrences along an edge, align the closed face walk to the side and replace the one step of the side by the complementary face path; its two source endpoints are the old ones, so both prescribed endpoints of the side stay fixed. Deleting the separating edge absorbs the face and lowers the filling cost, which is impossible.

It remains to treat edges with the unbounded face on both sides; such an edge is a bridge. If its two traversals lie in one side, the part of that side between them is an excursion without a junction inside it, whose endpoints are the same Cayley vertex, hence the same source vertex by Proposition 5.1 of the previous lesson. Delete the excursion, the bridge and the cut-off component: no prescribed junction is lost, the filling cost does not increase and the total side length decreases, which contradicts minimality. If the two traversals lie in different sides, their sheets are distinct, and coincident projected occurrences would, after deck alignment, agree at a vertex, which by the rigidity observation after Proposition 5.1 of the previous lesson would identify the two sheets. So these projected occurrences differ too.

Suppress every unmarked vertex of degree two. An unmarked vertex of degree one would force a backtrack in a side or a bounded face, so unmarked vertices have degree at least three, and marked vertices degree at least one when edges exist. Face and side incidences are constant along each arc: a side changes only at a marked vertex, and a face changes only at a branching. Both occurrences of an arc lie in immersed source paths and, by the reductions, have different projections; Lemma 2.1(5) of the previous lesson gives the assertions of (1). As in that lesson, (2.2)-(2.4) there give at least seven arcs on every bounded face.

For (3), let \(f\) be the number of bounded faces and \(V,E\) the numbers of vertices and edges of the compressed graph, when edges exist. Euler's formula and the degree bounds give
\[
\begin{gathered}
E=V+f-1,\qquad2E\ge3V-2k,\\
E\le3f+2k-3 .
\end{gathered}
\]
Every edge has two face sides, so \(2E-B=\sum_F\deg(F)\ge6f\) over the bounded faces, and \(B\le2E-6f\le4k-6\). If the diagram has no edges, all marked vertices coincide and every side is constant.

Every edge at a private source vertex is private. A nonconstant side ending at a private vertex would have a first or last arc containing a private edge, which (1) excludes. Finally, by (2.4) of the previous lesson a side of at most three arcs has length less than \(3.014\,m_Q(v)\) at its initial endpoint. \(\square\)

## 2. Allowed removed sets

The sheets are embedded, their stabilizers are conjugates of \(\mathsf H\), and every private vertex has only private edges. After enlarging the fixed degree constant to absorb the six added edge ends, the maximum degree in a sheet is \(\Delta\le K_{b,\epsilon}D\). On each sheet,
\[
\begin{gathered}
|m_Q(u)-m_Q(v)|\\
\le a\,d_Q(u,v),\\
a\le10^{-6},\quad m_Q\ge10^6 ,
\end{gathered}\tag{2.1}
\]
with \(m_i=H_i/\log_2q\) at an old vertex of layer \(i\). Put \(\kappa=3.014\). A path made of at most three comparison arcs and starting at \(v\) has length less than \(L(1+(1+La)+(1+La)^2)m_Q(v)\), which is less than \(3.010\,m_Q(v)<\kappa\,m_Q(v)\).

For a vertex set \(B\) of a sheet \(Q\), let \(\operatorname{Star}_Q(B)\) be the subgraph of all edges of \(Q\) with at least one endpoint in \(B\), together with their endpoints.

**Lemma 2.1** (allowed removed sets; [OpenAI-BCI, Lemma 7.1]). For an old vertex \(v\) of a sheet \(Q\) put
\[
\begin{aligned}
B_Q(v)=\{w\in V(Q):{}&d_Q(v,w)\\
&\le\lfloor\kappa\,m_Q(v)\rfloor\} .
\end{aligned}
\]
Then \(\operatorname{Star}_Q(B_Q(v))\) is a forest, and so is \(\operatorname{Star}_Q(\{w\})\) for a private vertex \(w\); so is the star of the empty set. After increasing \(s\) as the order of parameters allows, if \(B_Q(v)\) contains an old vertex of layer \(i\), then
\[
|B_Q(v)|\le2^{10H_i} .\tag{2.2}
\]
A private singleton contains no old vertex.

*Proof.* Let \(m=m_Q(v)\) and \(R=\lfloor\kappa m\rfloor\). Every vertex of the ball is joined to \(v\) by a shortest path inside the ball; choosing for each vertex a predecessor at distance one less gives a spanning tree of the ball. An edge of the ball outside this tree, together with tree paths, would contain a simple cycle of length at most \(2R+1\); an outside vertex with two edges into the ball would give a simple cycle of length at most \(2R+2\), also with parallel edges. Such a cycle has a vertex \(u\) in the ball, where \(m_Q(u)\ge m-aR\ge(1-\kappa a)m\), and its length would be at most \(2R+2<6.03(1-\kappa a)m\), because the difference is at least \((0.002-6.03\kappa\cdot10^{-6})10^6-2>0\). This contradicts the girth bound, Lemma 2.1(4) of the previous lesson. So the ball is a tree and every outside vertex has at most one edge into it: the star is a tree with additional leaves. The star of a singleton is a star: a loop or a repeated neighbor would be a cycle of length one or two.

The degree constant is fixed before \(s\), and \(\log_2D=0.60005s\), so \(\log_2(\Delta+1)\le0.61s\) may be arranged. The ball has at most \((\Delta+1)^{R+1}\) vertices. If it contains an old vertex of layer \(i\), (2.1) gives \(m\le m_i/(1-\kappa a)\), so
\[
\begin{aligned}
&\log_2|B_Q(v)|\le\Bigl(\frac{\kappa\,m_i}{1-\kappa a}+1\Bigr)0.61s\\
&\quad=H_i\Bigl(\frac{0.61\kappa}{0.50005(1-\kappa a)}\\
&\qquad\quad+\frac{0.61}{0.50005\,m_i}\Bigr)<4H_i .\qquad\square
\end{aligned}
\]

For an allowed removed set \(R_Q\) (empty, an old-centered ball \(B_Q(v)\), or a private singleton) write \(D_Q=V(Q)\setminus R_Q\). For a finite family \(\mathcal F\) of sheets, the *contact set* of \(Q\in\mathcal F\) is
\[
I_{\mathcal F}(Q)=V(Q)\cap\bigcup_{Q'\in\mathcal F\setminus\{Q\}}V(Q') .
\]
It need not be finite, and since comparison arcs avoid private edges but not private vertices, a contact may be a single private vertex.

## 3. Finite peeling

**Lemma 3.1** (finite peeling; [OpenAI-BCI, Lemma 7.2]). Every nonempty finite family \(\mathcal F\) of sheets has a sheet \(Q\) whose contact set \(I_{\mathcal F}(Q)\) is empty, or contained in \(B_Q(v)\) for some old contact \(v\), or a single private vertex. Consequently \(\mathcal F\) can be ordered \(Q_1,\ldots,Q_n\), with allowed removed sets \(R_j\) of these three kinds, such that
\[
V(Q_j)\cap\bigcup_{l>j}V(Q_l)\subseteq R_j .\tag{3.1}
\]

*Proof.* Suppose no sheet has one of the three properties; then every sheet has a contact. Build a walk through the sheets: enter a sheet at a contact \(u\); if \(u\) is old, choose a contact \(w\notin B_Q(u)\), at intrinsic distance greater than \(\kappa m_Q(u)\) from \(u\); if \(u\) is private, choose any contact \(w\ne u\), which exists because the contact set is not that private singleton. Move at \(w\) to another sheet containing it and repeat. The family is finite and consecutive sheets differ, so a sheet eventually repeats. At the first repetition, keep the \(k\ge2\) distinct sheets visited in between and close the walk inside the repeated sheet. This polygon has \(k-1\) chosen nonconstant sides; only the closing side is unrestricted.

Apply Lemma 1.1 with all these contacts fixed. If a chosen side has a private endpoint, every replacement path with the same distinct endpoints begins or ends with a private edge, while every arc of the reduced side is a comparison arc without private edges; this is impossible. Otherwise all \(k-1\) chosen sides have old endpoints at intrinsic distance greater than \(\kappa m_Q(u)\), so each needs at least four arc incidences on the unbounded face, by the last assertion of Lemma 1.1. That gives at least \(4(k-1)>4k-6\) of them, contradicting (1.1). The closing side was not needed to be long or nonconstant.

Remove the sheet found, with its whole contact ball, its private singleton or the empty set as removed set, and apply the same argument to the remaining family. This gives the order and (3.1). \(\square\)

## 4. Exercises

**Exercise 4.1.** Show that for \(k=2\) Lemma 1.1 gives \(B\le2\), and deduce that two distinct sheets with two contacts at intrinsic distance greater than \(3.014\,m_Q\) in one of them cannot exist.

**Exercise 4.2.** Check the inequality \(6.03(1-\kappa a)m>2\kappa m+2\) for \(\kappa=3.014\), \(a=10^{-6}\) and \(m\ge10^6\).

**Exercise 4.3.** Why does peeling allow a private singleton as a removed set, instead of always a ball around an old vertex?

## 5. Solutions

**4.1.** With \(k=2\), \(B\le4\cdot2-6=2\). If two sheets met at contacts \(g_1,g_2\) at intrinsic distance greater than \(3.014\,m_Q\) in \(Q_1\), the side in \(Q_1\) from \(g_2\) to \(g_1\) would need at least four arc incidences, more than \(2\).

**4.2.** \(6.03(1-3.014\cdot10^{-6})=6.0299818\ldots\), and \(2\kappa=6.028\); the difference \(0.0019818\ldots\) times \(m\ge10^6\) exceeds \(2\).

**4.3.** Comparison arcs contain no private edges, but two sheets may share a single private vertex, through which no comparison arc passes. Such a contact cannot be put inside a ball around an old contact in general, but a single private vertex has a star, its two private edges, which is a forest, and removing it costs nothing in the analytic estimates, since private vertices carry no old coordinates.

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 6.5 and 7.1, Lemmas 6.5, 7.1 and 7.2. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
