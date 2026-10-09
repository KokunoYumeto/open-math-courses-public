# Six and ten labels

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Supports at equality](supports-at-equality.md) showed that an admissible map on the lines of \(\mathbb R^k\) with \(N_k\) labels has a support complex whose facets have \(k\) labels and form a cycle modulo two. This lesson turns that information into a contradiction for \(k=4\), \(N_4=10\), by finite combinatorics. For \(k=3\) the triangles of a six-label complex form a rigid configuration, a *six-label triangle system* (Section 1). In a ten-label complex, the six labels outside each tetrahedron carry such a system, and moving from a tetrahedron to a neighbouring one transports these systems along transpositions of labels; the rigidity of six-label systems then forces the tetrahedra into a block pattern that cannot close up (Section 2). Section 3 assembles the counterexample to Borsuk's conjecture in dimension nine and in every higher dimension.

Notation is that of [Supports at equality](supports-at-equality.md). A face with three labels is a *triangle*, one with four labels a *tetrahedron*. For a finite set \(C\), \(\binom C3\) is the set of its three-element subsets.

## 1. Six labels

**Definition 1.1.** A **six-label triangle system** on a set \(C\) with six elements is a set \(\mathcal T\subseteq\binom C3\) such that

1. for every \(T\in\binom C3\), exactly one of \(T\) and \(C\setminus T\) belongs to \(\mathcal T\);
2. every pair of elements of \(C\) lies in exactly two members of \(\mathcal T\).

The image of a six-label triangle system under a bijection \(C\to C'\) is a six-label triangle system on \(C'\). For \(a\in C\), the *link graph* of \(\mathcal T\) at \(a\) has vertex set \(C\setminus\{a\}\) and an edge \(\{u,v\}\) whenever \(\{a,u,v\}\in\mathcal T\).

**Lemma 1.2.** Let \(f:\mathbb P(\mathbb R^3)\to\Delta^5\) be admissible. Then the triangles of its support complex form a six-label triangle system on \([6]\).

*Proof.* Here \(m=6=N_3\). By Theorem 2.1 and Theorem 3.3 of [Supports at equality](supports-at-equality.md), the facets are triangles and every pair of labels lies in a positive even number of triangles; by Proposition 1.1 there, every pair is a face, so it lies in at least two triangles. Two complementary triples \(T\) and \([6]\setminus T\) cannot both be triangles: if \(x\) and \(y\) witness them, a line orthogonal to both \(x\) and \(y\) exists in \(\mathbb R^3\), and by admissibility its support is disjoint from \(S(x)\cup S(y)=[6]\), which is impossible. So there are at most ten triangles, one from each complementary pair. Counting pairs of labels in triangles, there are at least \(2\cdot15/3=10\) triangles. Hence there are exactly ten, one from each complementary pair, and every pair lies in exactly two. \(\square\)

**Lemma 1.3.** Let \(\mathcal T\) be a six-label triangle system on \(C\).

1. Every link graph is a cycle of length five.
2. Every four-element subset of \(C\) contains a member of \(\mathcal T\), but not all four of its three-element subsets belong to \(\mathcal T\).
3. If \(a\ne b\) in \(C\) and \(R\subseteq C\setminus\{a,b\}\) has three elements, then the link graphs at \(a\) and at \(b\), restricted to \(R\), are different. In particular, no transposition of two elements of \(C\) maps \(\mathcal T\) to itself.
4. The members of \(\mathcal T\) contained in any five-element subset of \(C\) determine \(\mathcal T\).

*Proof.* (1) By condition 2, every vertex of a link graph has degree two, so the graph is a disjoint union of cycles, each of length at least three. On five vertices this leaves a single five-cycle.

(2) Let \(A\subseteq C\) have four elements and \(a\in A\). Three vertices of a five-cycle always include two adjacent ones (otherwise each of the three would be followed by a vertex outside the set, and the cycle would have at least six vertices). So the link at \(a\) has an edge \(\{u,v\}\) inside \(A\setminus\{a\}\), and \(\{a,u,v\}\in\mathcal T\). If all four triples of \(A\) were in \(\mathcal T\), the link at \(a\) would contain a triangle on \(A\setminus\{a\}\), which a five-cycle does not.

(3) Name the elements \(C=\{a,b,c,d,e,g\}\) so that the two members of \(\mathcal T\) containing \(\{a,b\}\) are \(\{a,b,c\}\) and \(\{a,b,d\}\). In the five-cycle at \(a\), the neighbours of \(b\) are \(c\) and \(d\); deleting \(b\) leaves a path through \(c,d,e,g\) with ends \(c\) and \(d\), whose middle edge is \(\{e,g\}\). Its two end edges form one of the matchings
\[
M_1=\bigl\{\{c,e\},\{d,g\}\bigr\},\qquad M_2=\bigl\{\{c,g\},\{d,e\}\bigr\}.
\]
The same holds for the link at \(b\), whose neighbours of \(a\) are also \(c\) and \(d\). The two links use different matchings: if the link at \(a\) uses \(M_1\), then \(\{a,c,e\},\{a,d,g\}\in\mathcal T\), so their complements \(\{b,d,g\},\{b,c,e\}\notin\mathcal T\), and the link at \(b\) contains neither \(\{d,g\}\) nor \(\{c,e\}\); it uses \(M_2\). The restrictions of the two links to \(\{c,d,e,g\}\) are the paths \(\{e,g\}\cup M_1\) and \(\{e,g\}\cup M_2\), which differ exactly in the four-cycle \(M_1\cup M_2\). Any three vertices of a four-cycle contain one of its edges, so the restrictions to any three-element \(R\subseteq\{c,d,e,g\}\) differ. A transposition \((a\ b)\) preserving \(\mathcal T\) would map the link at \(a\) onto the link at \(b\) and fix \(R\) pointwise, making the restrictions equal.

(4) Let \(z\) be the element outside the five-element subset. A triple containing \(z\) has its complement inside the subset, and by condition 1 its membership is the opposite of the complement's. \(\square\)

## 2. Ten labels

In this section \(f:\mathbb P(\mathbb R^4)\to\Delta^9\) is admissible, and \(K\) is its support complex. By Corollary 1.2 of [Supports at equality](supports-at-equality.md) every label is used, so \(m=10=N_4\), and Theorems 2.1 and 3.3 there apply: \(K\) is pure of dimension three (every face lies in a tetrahedron, and the facets are the tetrahedra), and every triangle lies in a positive even number of tetrahedra. For a tetrahedron \(S\) put \(C_S=[10]\setminus S\), a set of six labels, and let \(\mathcal T_S\) be the set of triangles of \(K\) contained in \(C_S\).

**Lemma 2.1** (Facet complements). For every tetrahedron \(S\), \(\mathcal T_S\) is a six-label triangle system on \(C_S\). No two tetrahedra of \(K\) are disjoint, and every four labels of \(C_S\) contain a triangle of \(K\).

*Proof.* Let \(x\) witness \(S\), so \(S(x)=S\). Lines of \(x^\perp\cong\mathbb R^3\) use only labels in \(C_S\), and at least \(N_3=6\) labels occur there (Corollary 1.2 there), so all six occur, and the restriction of \(f\) is an admissible map \(\mathbb P(x^\perp)\to\Delta_{C_S}\cong\Delta^5\). By Lemma 1.2 its triangles form a six-label triangle system \(\mathcal T'\subseteq\mathcal T_S\). If some \(T\in\mathcal T_S\) were not in \(\mathcal T'\), then \(C_S\setminus T\in\mathcal T'\), and \(T\), \(C_S\setminus T\) and \(S\) would all be faces of \(K\); a line orthogonal to witnesses of all three exists in \(\mathbb R^4\), and its support would avoid \(S\cup T\cup(C_S\setminus T)=[10]\), which is impossible. So \(\mathcal T_S=\mathcal T'\). A tetrahedron disjoint from \(S\) would be a four-element subset of \(C_S\) all of whose triples are triangles, contradicting Lemma 1.3(2), which also gives the last claim. \(\square\)

**Lemma 2.2** (Transport; two tetrahedra per triangle). (a) If \(S\) and \(S'=(S\setminus\{a\})\cup\{b\}\) are tetrahedra, then the transposition \((a\ b)\) maps \(\mathcal T_S\) onto \(\mathcal T_{S'}\).

(b) Every triangle of \(K\) lies in exactly two tetrahedra.

*Proof.* (a) \(C_S\) contains \(b\), \(C_{S'}\) contains \(a\), and \(Q=C_S\setminus\{b\}=C_{S'}\setminus\{a\}\) has five elements. The transposition maps \(C_S\) onto \(C_{S'}\), fixes \(Q\) pointwise, and maps \(\mathcal T_S\) to a six-label triangle system on \(C_{S'}\) whose members inside \(Q\) are those of \(\mathcal T_S\), namely the triangles of \(K\) inside \(Q\). These are also the members of \(\mathcal T_{S'}\) inside \(Q\), so the two systems agree by Lemma 1.3(4).

(b) Suppose a triangle \(T\) lies in three tetrahedra \(T\cup\{a\}\), \(T\cup\{b\}\), \(T\cup\{c\}\), and put \(R=[10]\setminus(T\cup\{a,b,c\})\), a set of four labels. By (a), the transpositions \((a\ b)\), \((b\ c)\), \((c\ a)\) carry \(\mathcal T_{T\cup\{a\}}\) to \(\mathcal T_{T\cup\{b\}}\), then to \(\mathcal T_{T\cup\{c\}}\), then back to \(\mathcal T_{T\cup\{a\}}\). The composite \((c\ a)(b\ c)(a\ b)\) fixes \(R\) and exchanges \(b\) and \(c\), so the transposition \((b\ c)\) of \(C_{T\cup\{a\}}=R\cup\{b,c\}\) preserves \(\mathcal T_{T\cup\{a\}}\), contradicting Lemma 1.3(3). So at most two tetrahedra contain \(T\), and the number is positive and even. \(\square\)

For an edge \(D\) of \(K\), the **link** of \(D\) is the graph whose vertices are the labels \(v\notin D\) with \(D\cup\{v\}\) a triangle, and whose edges are the pairs \(\{v,w\}\) with \(D\cup\{v,w\}\) a tetrahedron.

**Lemma 2.3** (Short links). Every connected component of the link of an edge is a cycle of length three or four.

*Proof.* If \(D\cup\{v,w\}\) is a tetrahedron, \(D\cup\{w\}\) is a triangle, so edges join vertices of the link. By Lemma 2.2(b) every vertex has degree two, so every component is a cycle. Suppose the link contains a path \(v_0,v_1,v_2,v_3,v_4\) on five distinct vertices, and let \(R\) be the three labels outside \(D\cup\{v_0,\dots,v_4\}\). The tetrahedra \(S_j=D\cup\{v_j,v_{j+1}\}\), \(j=0,\dots,3\), satisfy \(S_{j+1}=(S_j\setminus\{v_j\})\cup\{v_{j+2}\}\), so by Lemma 2.2(a) the composite \(\pi=(v_2\ v_4)(v_1\ v_3)(v_0\ v_2)\) maps \(\mathcal T_{S_0}\) onto \(\mathcal T_{S_3}\). It fixes \(R\) and sends \(v_4\) to \(v_2\). For \(r,s\in R\), therefore, \(\{v_4,r,s\}\in\mathcal T_{S_0}\) if and only if \(\{v_2,r,s\}\in\mathcal T_{S_3}\). The triple \(\{v_2,r,s\}\) lies in both \(C_{S_0}=R\cup\{v_2,v_3,v_4\}\) and \(C_{S_3}=R\cup\{v_0,v_1,v_2\}\), so its membership in either system is its membership in \(K\). Hence the link graphs of \(\mathcal T_{S_0}\) at \(v_4\) and at \(v_2\) agree on \(R\), contradicting Lemma 1.3(3). A cycle of length at least five contains such a path. \(\square\)

**Lemma 2.4** (Partner blocks). Let \(S\) be a tetrahedron. For \(v\in S\) let \(p(v)\) be the label such that \((S\setminus\{v\})\cup\{p(v)\}\) is the second tetrahedron containing the triangle \(S\setminus\{v\}\) (Lemma 2.2(b)). For each value \(y\) of \(p\) put \(B_y=p^{-1}(y)\cup\{y\}\). Then:

(a) \(p(v)\notin S\); the blocks \(B_y\) are pairwise disjoint, have at least two elements, contain \(S\) in their union, and \(\sum_y(|B_y|-1)=4\);

(b) for every choice of one element \(q_y\in B_y\) in each block, \(\bigcup_y(B_y\setminus\{q_y\})\) is a tetrahedron;

(c) every tetrahedron of \(K\) contains at least two elements of some block.

*Proof.* (a) The second tetrahedron is not \(S\), so \(p(v)\ne v\), and \(p(v)\notin S\setminus\{v\}\) because the union has four elements. Disjointness and the sizes are immediate, and \(\sum_y|p^{-1}(y)|=|S|=4\).

*Exchanges keep the blocks.* Let \(v\in S\), \(a=p(v)\), \(S'=(S\setminus\{v\})\cup\{a\}\), and let \(p'\) be the partner map of \(S'\). The triangle \(S'\setminus\{a\}=S\setminus\{v\}\) lies in \(S'\) and \(S\), so \(p'(a)=v\). Let \(w\in S\setminus\{v\}\), \(D=S\setminus\{v,w\}\) and \(b=p(w)\). The link of the edge \(D\) contains the edges \(\{v,w\}\) (from \(S\)), \(\{w,a\}\) (from \(S'\)) and \(\{v,b\}\) (from \((S\setminus\{w\})\cup\{b\}\)). If \(a=b\), these three edges form a triangle, which is a whole component because degrees are two; so the tetrahedra containing \(D\cup\{a\}=S'\setminus\{w\}\) are \(S'\) and \(D\cup\{a,v\}\), and \(p'(w)=v\). If \(a\ne b\), the edges form the path \(a,w,v,b\) on four distinct vertices, and by Lemma 2.3 its component is the four-cycle closed by the edge \(\{a,b\}\); so \(D\cup\{a,b\}\) is a tetrahedron containing \(S'\setminus\{w\}\), and \(p'(w)=b=p(w)\). Thus \(p'(w)=v\) if \(p(w)=a\) and \(p'(w)=p(w)\) otherwise. The block of \(S'\) indexed by \(v\) is \(\{a\}\cup(p^{-1}(a)\setminus\{v\})\cup\{v\}=B_a\), and every other block is unchanged.

(b) \(S\) contains \(p^{-1}(y)=B_y\setminus\{y\}\) and not \(y\), so \(S=\bigcup_y(B_y\setminus\{y\})\): it omits one element from each block. Every tetrahedron \(T\) obtained from \(S\) by exchanges has the same blocks and omits exactly one element \(q\) of each block \(B\), its index there. To change the omitted element of \(B\) from \(q\) to \(u\in B\setminus\{q\}\), note that \(u\in T\) and the partner of \(u\) for \(T\) is \(q\), so \((T\setminus\{u\})\cup\{q\}\) is a tetrahedron; it omits \(u\) from \(B\) and the same elements as \(T\) from the other blocks. Changing one block at a time reaches every choice.

(c) If a tetrahedron \(T\) met every block in at most one element, choose \(q_y\) to be that element when it exists and arbitrary otherwise. The tetrahedron \(\bigcup_y(B_y\setminus\{q_y\})\) of (b) is disjoint from \(T\), contradicting Lemma 2.1. \(\square\)

**Theorem 2.5.** There is no admissible map \(\mathbb P(\mathbb R^4)\to\Delta^9\).

*Proof.* Suppose \(f\) is one, and fix a tetrahedron \(S\) with its blocks. Let \(t\) be the number of blocks and \(R\) the set of labels outside all blocks. The blocks contain \(\sum_y|B_y|=4+t\) labels, so \(1\le t\le4\) and \(|R|=6-t\).

If \(t=4\), each block has two elements and \(S\) contains exactly one element of each, contradicting Lemma 2.4(c). So \(t\le3\) and \(|R|\ge3\).

No triangle lies in \(R\): it would lie in a tetrahedron, whose fourth label is the only one that can belong to a block, against Lemma 2.4(c). But \(R\) is disjoint from \(S\), so \(R\subseteq C_S\), and every four labels of \(C_S\) contain a triangle (Lemma 2.1). Hence \(|R|\le3\), so \(t=3\), \(|R|=3\), and the block sizes are \(3,2,2\).

The six labels of \(C_S\) are those of \(R\) and the three labels \(y\) omitted by \(S\), one in each block. Choose distinct \(r,s\in R\). In the six-label system \(\mathcal T_S\), the pair \(\{r,s\}\) lies in two triangles \(\{r,s,z_1\}\), \(\{r,s,z_2\}\) with \(z_1\ne z_2\). Since \(R\) contains no triangle, \(z_1\) and \(z_2\) are omitted labels of two different blocks, and as only one block has three elements, one of them, say \(z\), lies in a block \(B\) with two elements. A tetrahedron containing the triangle \(\{r,s,z\}\) must contain two elements of some block (Lemma 2.4(c)); as \(r,s\) lie in no block, its fourth label is the other element of \(B\). So at most one tetrahedron contains \(\{r,s,z\}\), contradicting Lemma 2.2(b). \(\square\)

## 3. The counterexample

**Theorem 3.1** (OpenAI 2026). The set \(X_4=\{uu^{\mathsf T}:u\in\mathbb R^4,\|u\|=1\}\), in the nine-dimensional Euclidean space of symmetric \(4\times4\) matrices of trace one with the Frobenius distance, is compact, has diameter \(\sqrt2\), and cannot be covered by ten subsets of diameter less than \(\sqrt2\). So Borsuk's conjecture fails in dimension nine.

*Proof.* Compactness and the diameter are Lemma 1.1 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md). A cover by ten subsets of smaller diameter would give an admissible map \(\mathbb P(\mathbb R^4)\to\Delta^9\) (Lemma 2.3 there), which does not exist by Theorem 2.5. \(\square\)

**Corollary 3.2.** For every \(d\ge9\) there is a compact set of diameter \(\sqrt2\) in \(\mathbb R^d\) that cannot be covered by \(d+1\) subsets of smaller diameter.

*Proof.* For \(d=9\) this is Theorem 3.1. Let \(d=9+s\) with \(s\ge1\). Translate \(X_4\) to \(Y=\{P-\frac14I:P\in X_4\}\) in the nine-dimensional space of symmetric matrices of trace zero; then \(\|y\|_F^2=1-\frac12+\frac14=\frac34\) for \(y\in Y\). The matrix \(I_s+\frac14\mathbf 1\mathbf 1^{\mathsf T}\) is positive definite, so it is the Gram matrix of vectors \(v_1,\dots,v_s\in\mathbb R^s\); they have \(|v_i|^2=\frac54\) and \(|v_i-v_j|^2=\frac54+\frac54-\frac12=2\) for \(i\ne j\). In \(\mathbb R^9\oplus\mathbb R^s\), the compact set
\[
Z=(Y\times\{0\})\cup\{(0,v_i):1\le i\le s\}
\]
has diameter \(\sqrt2\): each new point is at distance \(\sqrt{\frac34+\frac54}=\sqrt2\) from every point of \(Y\times\{0\}\) and from every other new point. A subset of \(Z\) of diameter less than \(\sqrt2\) containing a new point contains no other point of \(Z\). So a cover of \(Z\) by \(d+1=10+s\) such subsets leaves at most ten of them to cover \(Y\times\{0\}\), contradicting Theorem 3.1. \(\square\)

The proof does not determine the smallest dimension in which Borsuk's conjecture fails, which lies between four and nine, nor the exact number of smaller-diameter pieces needed for \(X_4\).

## 4. Exercises

**4.1.** Show that the ten triples \(\{1,2,3\},\{1,3,4\},\{1,4,5\},\{1,5,6\},\{1,2,6\},\{2,3,5\},\{3,4,6\},\{2,4,5\},\{3,5,6\},\{2,4,6\}\) form a six-label triangle system on \([6]\) (they are the triangles of the six-vertex triangulation of the projective plane), and find the link graph at \(1\).

**4.2.** Show that there are exactly twelve six-label triangle systems on \([6]\). (Show that the system is determined by the link at \(1\), a five-cycle on \(\{2,\dots,6\}\), and that each of the twelve five-cycles occurs.)

**4.3.** In Lemma 2.4, describe the blocks when all four partners coincide (\(t=1\)). Why does the proof of Theorem 2.5 not need to treat this case separately?

**4.4.** Check the distances in Corollary 3.2 for \(s=1\) directly: give \(v_1\) and verify that \(Z\subset\mathbb R^{10}\) has diameter \(\sqrt2\).

## 5. Solutions

**4.1.** The complements of the listed triples are \(\{4,5,6\},\{2,5,6\},\{2,3,6\},\{2,3,4\},\{3,4,5\},\{1,4,6\},\{1,2,5\},\{1,3,6\},\{1,2,4\},\{1,3,5\}\), none of which is listed, and together the twenty triples are all of \(\binom{[6]}3\). Each pair occurs in exactly two listed triples; for instance \(\{1,2\}\) in \(\{1,2,3\}\) and \(\{1,2,6\}\). The link at \(1\) has edges \(\{2,3\},\{3,4\},\{4,5\},\{5,6\},\{6,2\}\): the five-cycle \(2,3,4,5,6\).

**4.2.** The members containing \(1\) are given by the link at \(1\), and every other triple is the complement of a triple containing \(1\), so by condition 1 the link determines the system. There are \(4!/2=12\) five-cycles on the five labels \(2,\dots,6\). Relabelling the system of 4.1 by a permutation of \(\{2,\dots,6\}\) produces every five-cycle as the link at \(1\), and the resulting system satisfies conditions 1 and 2 because relabelling preserves them.

**4.3.** If \(t=1\), all four elements of \(S\) have the same partner \(y\), and \(B_y=S\cup\{y\}\) has five elements. Then \(|R|=5\ge4\), and the proof of Theorem 2.5 rules out \(|R|\ge4\) in general: a set of four labels of \(R\subseteq C_S\) contains a triangle, while \(R\) contains none.

**4.4.** \(v_1\in\mathbb R\) with \(v_1^2=\frac54\), say \(v_1=\frac{\sqrt5}2\). For \(y\in Y\), \(|(y,0)-(0,v_1)|^2=\frac34+\frac54=2\), and distances within \(Y\times\{0\}\) are at most \(\sqrt2\) by Lemma 1.1 of [Diameter covers and admissible maps](diameter-covers-and-admissible-maps.md).

## References

- [OpenAI-B9] OpenAI, *A nine-dimensional counterexample to Borsuk's covering assertion*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
- [Bon] A. V. Bondarenko, *On Borsuk's conjecture for two-distance sets*, Discrete & Computational Geometry 51 (2014). https://arxiv.org/abs/1305.2584
- [Kal] G. Kalai, *Some old and new problems in combinatorial geometry I: around Borsuk's problem*, Surveys in Combinatorics 2015. https://arxiv.org/abs/1505.04952
