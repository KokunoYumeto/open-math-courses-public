# The cube complex and its universal cover

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A right-angled Artin group acts freely on a contractible cube complex: the universal cover of a union of coordinate subtori of a torus, one subtorus for each clique of the commutation graph. This complex was used by Bestvina and Brady to study the kernels of height homomorphisms [OpenAI-EG, Lemma 4.3]. This lesson constructs it, describes its cubes, and proves that it is contractible. The contractibility gives the upper bound \(\operatorname{gd}G\le3\) of the main theorem, and the acyclicity is the starting point for the level complex of the next lesson. The proof of acyclicity is algebraic: the cellular chains form a complex of free modules over the group ring, and deleting one vertex of the commutation graph gives a short exact sequence of complexes whose connecting map is the boundary map of a tree, by the splitting of [Right-angled Artin groups and residual finiteness](right-angled-artin-groups-and-residual-finiteness.md).

- The torus complex (Section 1).
- The universal cover and its cubes (Section 2).
- The cube complex of chains (Section 3).
- Acyclicity (Section 4).
- Contractibility (Section 5).

We use: from [Right-angled Artin groups and residual finiteness](right-angled-artin-groups-and-residual-finiteness.md), Lemma 1.1 (retractions) and Lemma 2.1 (splitting); the Hurewicz theorem, [Explicit CW models and the first Hurewicz map, Theorem 4.1](course:CG-S6/cw-models-and-the-first-hurewicz-map), and Whitehead's theorem, [Homotopy fibres and the Serre spectral sequence, Section B.4](course:DG-CHAR/DG-CHAR-13B); and the facts (PI1) and (COV) on fundamental groups and covering spaces stated in [Cone pictures and asphericity](course:torsion-free-group-algebra-with-zero-divisors/cone-pictures-and-asphericity), Section 2. The following standard fact is also used without proof; a course proving it is recorded as an open obligation of this course.

**(CUBE)** (cellular homology of cube complexes; [Hatcher, Theorem 2.35 and the cellular boundary formula of Section 2.2; Proposition 1.26]).

1. Let \(Y\) be a CW complex whose \(k\)-cells are given with characteristic maps from the cube \([0,1]^k\), such that the restriction of the characteristic map of every \(k\)-cell \(c\) to each face \(\{x_i=\epsilon\}\) is a characteristic map of a \((k-1)\)-cell \(c_{i,\epsilon}\), composed with the affine identification of the face with \([0,1]^{k-1}\) that keeps the order of the remaining coordinates. Then the singular homology of \(Y\) is the homology of the chain complex \(C_*(Y)\), with \(C_k\) free abelian on the \(k\)-cells and
\[
\partial c=\sum_{i=1}^k(-1)^{i+1}\bigl(c_{i,1}-c_{i,0}\bigr).
\]
2. Attaching cells of dimension at least three to a path-connected CW complex does not change its fundamental group.
3. Let \(\widetilde Y\to Y\) be the universal cover of a connected CW complex and \(G\) a subgroup of \(\pi_1(Y)\), acting on \(\widetilde Y\) by deck transformations. Then \(\widetilde Y/G\) is a CW complex whose cells are the \(G\)-orbits of the cells of \(\widetilde Y\), the quotient map \(\widetilde Y\to\widetilde Y/G\) is a universal cover, and \(\pi_1(\widetilde Y/G)\cong G\) [Hatcher, Propositions 1.36 and 1.40].

## 1. The torus complex

Let \(\Theta\) be a commutation graph with vertex set \(V\), and choose a total order on \(V\). A *clique* is a set of pairwise adjacent vertices, the empty set included; write \(K_k\) for the set of cliques with \(k\) elements. For a flag complex \(L\) the cliques of its \(1\)-skeleton are exactly the vertex sets of the simplices of \(L\), together with \(\varnothing\).

Let \(S^1=[0,1]/\{0\sim1\}\) with base point \(0\), and let \(T=(S^1)^V\) be the torus. For a clique \(\sigma\), the *coordinate subtorus* \(T_\sigma\) consists of the points whose coordinates outside \(\sigma\) are \(0\). The *torus complex* is
\[
S_\Theta=\bigcup_{\sigma\text{ a clique}}T_\sigma\subseteq T .
\]
It is a CW complex with one \(k\)-cell \(c_\sigma\) for every \(\sigma\in K_k\): the characteristic map \([0,1]^\sigma\to T_\sigma\) is the quotient map, the coordinates ordered as in \(V\). Its faces \(\{x_q=0\}\) and \(\{x_q=1\}\) are both mapped by the characteristic map of \(c_{\sigma\setminus q}\). The complex has one vertex, an edge loop \(c_{\{q\}}\) for every \(q\in V\), and a square for every edge \(\{q,r\}\) of \(\Theta\), attached along the commutator \(a_qa_ra_q^{-1}a_r^{-1}\) of the edge loops. By (PI1) and (CUBE 2),
\[
\pi_1(S_\Theta)\cong A_\Theta ,
\]
the class of the loop \(c_{\{q\}}\) corresponding to \(a_q\). If \(\Theta\) is the \(1\)-skeleton of a flag complex \(L\) of dimension two, the cliques have at most three elements, \(S_\Theta\) has dimension three, and we write \(S_L=S_\Theta\).

## 2. The universal cover and its cubes

Let \(p\colon E\to S_\Theta\) be the universal cover, with a vertex \(\tilde o\) over the vertex \(o\), and let \(P=A_\Theta\) act by deck transformations (COV 1). The fibre over \(o\) is \(\{g\tilde o:g\in P\}\), and we identify the vertex \(g\tilde o\) with \(g\in P\).

**Lemma 2.1** (the cubes of \(E\)). For every \(g\in P\) and every clique \(\sigma\), the characteristic map of \(c_\sigma\) has exactly one lift \(\chi_{g,\sigma}\colon[0,1]^\sigma\to E\) sending the corner \(0\) to \(g\), and the cells of \(E\) are the images of these lifts, each cell arising from exactly one pair \((g,\sigma)\). The lift \(\chi_{g,\sigma}\) sends the corner with coordinates \(1\) exactly on \(\tau\subseteq\sigma\) to the vertex
\[
g\prod_{q\in\tau}a_q ,
\]
and its restrictions to the faces \(\{x_q=0\}\) and \(\{x_q=1\}\) are \(\chi_{g,\sigma\setminus q}\) and \(\chi_{ga_q,\sigma\setminus q}\).

*Proof.* The cube is simply connected and locally path connected, so lifts exist and are determined by the image of one point (COV 2). By (COV 1) the cells of \(E\) are the lifts of the cells of \(S_\Theta\), and the deck group permutes the lifts of each cell freely and transitively; since \(g\mapsto\chi_{g,\sigma}(0)=g\) is a bijection from \(P\) to the fibre, each lift arises from exactly one \(g\). An edge of the cube in the direction \(q\) is mapped onto the loop \(c_{\{q\}}\), whose lift starting at \(h\) ends at \(ha_q\): the lift starting at \(\tilde o\) ends at \(a_q\tilde o\) by the definition of the deck action, and applying the deck transformation \(h\) gives the lift starting at \(h\). Following the edges of the cube from \(0\) to the corner of \(\tau\) gives the vertex \(g\prod_{q\in\tau}a_q\); the order does not matter, since the \(a_q\), \(q\in\sigma\), commute. The restrictions to the faces are lifts of the characteristic maps of \(c_{\sigma\setminus q}\) starting at \(g\) and at \(ga_q\), and by uniqueness of lifts they are \(\chi_{g,\sigma\setminus q}\) and \(\chi_{ga_q,\sigma\setminus q}\). \(\square\)

**Lemma 2.2** (geometry of the cubes). Every \(\chi_{g,\sigma}\) is injective, two cubes that meet intersect in a common face, every vertex lies in finitely many cubes, and \(E\) has dimension equal to the largest size of a clique.

*Proof.* Let \(\mathrm{ab}\colon P\to\mathbb Z^V\) be the abelianization map. The corners of \(\chi_{g,\sigma}\) are sent to \(\mathrm{ab}(g)+\sum_{q\in\tau}e_q\), which are distinct for distinct \(\tau\), so the \(2^{|\sigma|}\) corners are distinct vertices. The faces of the cube are the cells \(\chi_{h,\tau}\) with \(h=g\prod_{q\in\rho}a_q\) for disjoint \(\rho,\tau\subseteq\sigma\); distinct faces have distinct pairs \((h,\tau)\), as the abelianization of \(h\) determines \(\rho\). Distinct faces are therefore distinct cells, and the open faces of the cube are mapped injectively, so \(\chi_{g,\sigma}\) is injective.

Let two cubes \(\chi_{g,\sigma}\) and \(\chi_{g',\sigma'}\) have a common point. The image of a cube is the disjoint union of the open cells of its faces, so the common point lies in an open cell that is a face of both cubes, and the two cubes have a common vertex \(v\). Seen from \(v\), the corners of the first cube are \(v\prod_{q\in\alpha}a_q^{\epsilon_q}\) for subsets \(\alpha\) of \(\sigma\) and fixed signs \(\epsilon_q\), and those of the second are \(v\prod_{q\in\alpha'}a_q^{\epsilon'_q}\), \(\alpha'\subseteq\sigma'\). By abelianization, a common corner arises from \(\alpha=\alpha'\subseteq\{q\in\sigma\cap\sigma':\epsilon_q=\epsilon'_q\}\). These corners form one common face of the two cubes, namely the face at \(v\) spanned by the directions \(q\in\sigma\cap\sigma'\) with \(\epsilon_q=\epsilon'_q\), by uniqueness of lifts (Lemma 2.1). It contains every common vertex, and every common cell is a face of both cubes with all its vertices in it, hence a face of it. So the intersection is this face.

At a vertex there are finitely many cubes, one for each clique \(\sigma\) and each choice of signs, since the vertex determines the corner \(0\) of a cube from \(\sigma\) and the signs. The dimension statement holds because the \(k\)-cells correspond to the \(k\)-cliques. \(\square\)

## 3. The cube complex of chains

By Lemmas 2.1 and 2.2 and (CUBE 1), the singular homology of \(E\) is the homology of its cellular chain complex. The group \(P\) acts on the chains on the left, freely on the cells, so each \(C_k(E)\) is a free left module over \(\Lambda=\mathbb ZP\) with basis the cells \(e_\sigma=\chi_{1,\sigma}\), \(\sigma\in K_k\); the cell \(\chi_{g,\sigma}\) is \(ge_\sigma\). For \(\sigma=\{q_1<\cdots<q_k\}\), (CUBE 1) and Lemma 2.1 give
\[
\partial e_\sigma=\sum_{i=1}^k(-1)^{i+1}(a_{q_i}-1)\,e_{\sigma\setminus q_i}.\tag{3.1}
\]
Write \(\mathcal C(\Theta)\) for the complex of free \(\mathbb ZA_\Theta\)-modules \(\mathcal C_k(\Theta)=(\mathbb ZA_\Theta)^{(K_k)}\) with the boundary (3.1), augmented by \(\varepsilon\colon\mathcal C_0(\Theta)=\mathbb ZA_\Theta\to\mathbb Z\), the sum of the coefficients. So \(E\) is acyclic exactly when the augmented complex \(\mathcal C(\Theta)\to\mathbb Z\) is exact.

## 4. Acyclicity

**Lemma 4.1** (trees from free groups). Let \(F\) be a free group on a set \(B\). The graph with vertex set \(F\) and an edge from \(w\) to \(wb\) for every \(w\in F\) and \(b\in B\) is a tree: its cellular chain complex \(\mathbb Z^{(\text{edges})}\to\mathbb Z^{(F)}\) has kernel \(0\), and its cokernel is \(\mathbb Z\) through the sum of the coefficients.

*Proof.* Write each \(w\) as a reduced word and let \(|w|\) be its length. The two ends of an edge differ by one letter \(b^{\pm1}\), so their lengths differ by exactly \(1\): appending a letter to a reduced word either lengthens it or cancels its last letter. Every vertex \(w\ne1\) is joined to the vertex obtained by deleting its last letter, and only to it among the vertices of smaller length, so each edge is the *parent edge* of exactly one of its ends, the longer one, and every vertex other than \(1\) has exactly one parent edge.

*Kernel.* Let \(z\) be a nonzero finitely supported \(1\)-chain with \(\partial z=0\), and let \(w\) be an end of maximal length of the edges in its support. Every edge of the support at \(w\) has its other end shorter, so it is the parent edge of \(w\); the coefficient of \(w\) in \(\partial z\) is \(\pm\) the coefficient of that edge, which is not \(0\). This contradicts \(\partial z=0\).

*Cokernel.* Following parent edges joins every vertex to \(1\), so every vertex is homologous to \(1\) modulo boundaries, and the sum of the coefficients, which vanishes on boundaries, identifies the cokernel with \(\mathbb Z\). \(\square\)

**Theorem 4.2** (acyclicity; [OpenAI-EG, Lemma 4.3]). For every commutation graph \(\Theta\), the augmented complex \(\mathcal C(\Theta)\to\mathbb Z\) is exact. Consequently the universal cover \(E\) of \(S_\Theta\) is acyclic.

*Proof.* By induction on the number of vertices; for the empty graph \(\mathcal C(\Theta)\) is \(\mathbb Z\) in degree \(0\) and the augmentation is the identity. Otherwise let \(q\) be the last vertex in the order, \(t=a_q\), and \(P'\), \(C\subseteq P'\subseteq P\) as in Section 2 of [Right-angled Artin groups and residual finiteness](right-angled-artin-groups-and-residual-finiteness.md), the subgroups generated by the other vertices and by the neighbours \(N(q)\) of \(q\); by Lemma 1.1 there they are the right-angled Artin groups of the full subgraphs, and the induction hypothesis applies to \(\mathcal C(\Theta')\) and \(\mathcal C(N(q))\) for the full subgraphs on \(V'=V\setminus q\) and on \(N(q)\).

*An exact sequence of complexes.* The cliques of \(\Theta\) are the cliques of \(\Theta'\) and the sets \(\sigma\cup\{q\}\) for cliques \(\sigma\) of \(N(q)\). The submodules spanned by the \(e_\sigma\) with \(q\notin\sigma\) form a subcomplex \(\mathcal A\) of \(\mathcal C(\Theta)\), and
\[
\mathcal A\cong\Lambda\otimes_{\mathbb ZP'}\mathcal C(\Theta'),
\]
with the same formula (3.1). In the quotient \(\mathcal B=\mathcal C(\Theta)/\mathcal A\), spanned by the images of the \(e_{\sigma\cup q}\), the last term of (3.1), \(\pm(t-1)e_\sigma\), vanishes, since \(q\) is the largest element of \(\sigma\cup q\); so
\[
\mathcal B_k\cong\bigl(\Lambda\otimes_{\mathbb ZC}\mathcal C(N(q))\bigr)_{k-1},\qquad e_{\sigma\cup q}\mapsto1\otimes e_\sigma ,
\]
again with the formula (3.1). The ring \(\Lambda\) is a free right module over \(\mathbb ZP'\) and over \(\mathbb ZC\), with bases sets of coset representatives, so tensoring preserves exactness. By the induction hypothesis, \(\mathcal A\) has homology \(\Lambda\otimes_{\mathbb ZP'}\mathbb Z=\mathbb Z[P/P']\) in degree \(0\) and none elsewhere, and \(\mathcal B\) has homology \(\Lambda\otimes_{\mathbb ZC}\mathbb Z=\mathbb Z[P/C]\) in degree \(1\) and none elsewhere.

*The long exact sequence.* The short exact sequence \(0\to\mathcal A\to\mathcal C(\Theta)\to\mathcal B\to0\) gives \(H_k(\mathcal C(\Theta))=0\) for \(k\ge2\), and the exact sequence
\[
0\to H_1(\mathcal C(\Theta))\to\mathbb Z[P/C]\xrightarrow{\ \delta\ }\mathbb Z[P/P']\to H_0(\mathcal C(\Theta))\to0 .
\]
The connecting map sends \(gC\), the class of \(ge_{\{q\}}\), to the class of \(\partial(ge_{\{q\}})=g(t-1)e_\varnothing\), that is,
\[
\delta(gC)=gtP'-gP'.
\]
This is the boundary map of the graph \(\mathcal T\) with vertex set \(P/P'\) and an edge from \(gP'\) to \(gtP'\) for every \(gC\in P/C\); it is well defined, since an element \(c\in C\) lies in \(P'\) and commutes with \(t\).

*The graph is a tree.* Let \(\varphi\colon P\to F(P'/C)\rtimes P'\) be the isomorphism of Lemma 2.1 of the lesson on residual finiteness, and write \(\varphi(g)=(w_g,h_g)\). Then \(gP'\mapsto w_g\) is a bijection from \(P/P'\) onto \(F(P'/C)\), with inverse \(w\mapsto\varphi^{-1}(w,1)P'\). Since \(\varphi(gt)=(w_g,h_g)(b_C,1)=(w_g\,b_{h_gC},h_g)\), the edge of \(gC\) joins \(w_g\) to \(w_gb_{h_gC}\), and \(gC\mapsto(w_g,h_gC)\) is a bijection from the edges of \(\mathcal T\) to the pairs (vertex, free generator). So \(\mathcal T\) is the graph of Lemma 4.1 for the free group \(F(P'/C)\) on the symbols \(b_{hC}\), and it is a tree.

By Lemma 4.1, \(\delta\) is injective and its cokernel is \(\mathbb Z\) through the sum of the coefficients. Hence \(H_1(\mathcal C(\Theta))=0\), and \(H_0(\mathcal C(\Theta))\cong\mathbb Z\) through the augmentation, which is the exactness of the augmented complex. \(\square\)

## 5. Contractibility

**Corollary 5.1** (the cube complex is contractible; [OpenAI-EG, Lemma 4.3]). The universal cover \(E\) of \(S_\Theta\) is a contractible, locally finite cube complex on which \(A_\Theta\) acts freely, with quotient \(S_\Theta\). In particular \(\operatorname{gd}A_\Theta\) and the geometric dimension of each of its subgroups are at most the largest size of a clique of \(\Theta\).

*Proof.* \(E\) is simply connected, being a universal cover, and acyclic by Theorem 4.2. By the Hurewicz theorem, applied inductively, a simply connected space with vanishing reduced homology has \(\pi_n(E)=0\) for all \(n\): if \(\pi_i(E)=0\) for \(i<n\), then \(\pi_n(E)\cong H_n(E)=0\). So the map from \(E\) to a point induces isomorphisms on all homotopy groups, and by Whitehead's theorem it is a homotopy equivalence. The deck group acts freely and cellularly, with quotient \(S_\Theta\). For a subgroup \(G\), by (CUBE 3) the quotient \(E/G\) is a CW complex of the same dimension as \(E\), with fundamental group \(G\) and universal cover \(E\), which is contractible; so it is a classifying space for \(G\) in the sense of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md), Section 2. Local finiteness is Lemma 2.2. \(\square\)

For the group \(G=\ker\lambda\) of the main theorem, with \(L\) of dimension two, this gives \(\operatorname{gd}G\le3\).

## 6. Exercises

**6.1** (easy). For \(\Theta\) a single edge \(\{1,2\}\), describe \(S_\Theta\), \(E\) and the complex \(\mathcal C(\Theta)\), and verify (3.1) for the square \(e_{\{1,2\}}\).

**6.2** (easy). Verify \(\partial\partial=0\) for (3.1), using that the \(a_q\), \(q\in\sigma\), commute.

**6.3** (medium). For \(\Theta\) with two vertices and no edge, carry out the proof of Theorem 4.2: identify \(\mathcal A\), \(\mathcal B\), the tree \(\mathcal T\), and check that \(E\) is the tree of Lemma 4.1 for the free group on two generators.

**6.4** (medium). Let \(\Theta\) be complete on \(n\) vertices. Show that \(\mathcal C(\Theta)\) is the Koszul complex of \(\mathbb Z[a_1^{\pm1},\ldots,a_n^{\pm1}]\) for the elements \(a_q-1\), and that Theorem 4.2 gives its exactness.

**6.5** (easy). Show that for a nonempty clique \(\sigma\) the characteristic map of the cell \(c_\sigma\) of \(S_\Theta\) is not injective. Which step of the proof of Lemma 2.2 distinguishes the corners of the lifted cubes in \(E\)?

## 7. Solutions

**6.1.** \(S_\Theta\) is the torus \(T=(S^1)^2\) with one vertex, two edge loops and one square; \(E\) is the plane \(\mathbb R^2\) with the square tiling, vertices \(\mathbb Z^2=A_\Theta\). The complex is \(0\to\Lambda e_{12}\to\Lambda e_1\oplus\Lambda e_2\to\Lambda\to0\) with \(\partial e_1=a_1-1\), \(\partial e_2=a_2-1\), \(\partial e_{12}=(a_1-1)e_2-(a_2-1)e_1\): the face \(x_1=1\) of the square at \(1\) is the edge \(a_1e_2\) and the face \(x_1=0\) is \(e_2\), with sign \((-1)^{1+1}\); the faces \(x_2=1,0\) are \(a_2e_1\) and \(e_1\), with sign \((-1)^{2+1}\).

**6.2.** Applying \(\partial\) to (3.1) gives, for \(i\ne j\), two terms in \(e_{\sigma\setminus\{q_i,q_j\}}\) with coefficients \((a_{q_i}-1)(a_{q_j}-1)\) and \((a_{q_j}-1)(a_{q_i}-1)\). For \(i<j\), removing \(q_i\) first leaves \(q_j\) in position \(j-1\), and removing \(q_j\) first leaves \(q_i\) in position \(i\); the signs are \((-1)^{i+1}(-1)^{j}\) and \((-1)^{j+1}(-1)^{i+1}\), which are opposite, and the coefficients agree since \(a_{q_i}\) and \(a_{q_j}\) commute.

**6.3.** With \(q=2\): \(P'=\langle a_1\rangle\cong\mathbb Z\), \(N(2)=\varnothing\) and \(C=1\). \(\mathcal A=\Lambda\otimes_{\mathbb ZP'}\mathcal C(\{1\})\) is spanned by \(e_\varnothing\) and \(e_1\), and \(\mathcal B\) by the image of \(e_2\). The tree has vertices \(P/\langle a_1\rangle\) and edges \(P\), the edge of \(g\) joining \(g\langle a_1\rangle\) to \(ga_2\langle a_1\rangle\). The space \(E\) itself is a graph with vertices \(P=F(a_1,a_2)\) and edges from \(g\) to \(ga_1\) and to \(ga_2\), the tree of Lemma 4.1.

**6.4.** For the complete graph every subset is a clique, \(A_\Theta=\mathbb Z^n\), and \(\Lambda=\mathbb Z[a_1^{\pm1},\ldots,a_n^{\pm1}]\). The modules \(\Lambda^{(K_k)}\) with basis \(e_\sigma\), \(|\sigma|=k\), and the boundary (3.1) are the exterior powers \(\Lambda\otimes\bigwedge^k\mathbb Z^n\) with the Koszul differential \(e_{q_1}\wedge\cdots\wedge e_{q_k}\mapsto\sum_i(-1)^{i+1}(a_{q_i}-1)e_{q_1}\wedge\cdots\widehat{e_{q_i}}\cdots\wedge e_{q_k}\). Theorem 4.2 says that it is a resolution of \(\mathbb Z=\Lambda/(a_1-1,\ldots,a_n-1)\).

**6.5.** All the coordinates of the corners of \([0,1]^\sigma\) are \(0\) or \(1\), which are identified in \(S^1\), so all \(2^{|\sigma|}\ge2\) corners are mapped to the single vertex. In \(E\) the corners of \(\chi_{g,\sigma}\) are the vertices \(g\prod_{q\in\tau}a_q\), and the abelianization map \(P\to\mathbb Z^V\) separates them.

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 4.2. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
