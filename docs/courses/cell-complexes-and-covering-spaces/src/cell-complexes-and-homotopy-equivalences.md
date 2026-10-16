# Cell complexes and homotopy equivalences

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A cell complex is built from a discrete set of points by attaching disks of increasing dimension. This lesson fixes the conventions of the course and proves the facts about cell complexes that the following lessons use: complexes built by attaching cells are Hausdorff, so that the results on CW complexes proved in the course on characteristic classes apply to them; collapsing a contractible subcomplex and changing attaching maps by homotopies do not change the homotopy type; trees are contractible, and every connected graph contains a spanning tree; and a finite two-dimensional complex whose cells are attached along closed walks can be triangulated, so that simplicial approximation applies to maps into it.

- Cell complexes (Section 1).
- Collapsing a contractible subcomplex (Section 2).
- Attaching cells along homotopic maps (Section 3).
- Graphs and trees (Section 4).
- Triangulations and simplicial approximation (Section 5).

The results of the course are used in the lessons [Cone pictures and asphericity](course:torsion-free-group-algebra-with-zero-divisors/cone-pictures-and-asphericity) and [Torsion-freeness and the zero divisors](course:torsion-free-group-algebra-with-zero-divisors/torsion-freeness-and-the-zero-divisors) on a torsion-free group algebra with zero divisors, [Cohomological and geometric dimension](course:eilenberg-ganea-counterexample/cohomological-and-geometric-dimension) and [Aligned presentations of the cycle module](course:eilenberg-ganea-counterexample/aligned-presentations-of-the-cycle-module) on the Eilenberg–Ganea problem, [Wall's D(2) problem and twisted homology](course:a-counterexample-to-walls-d2-problem/walls-d2-problem-and-twisted-homology), [From a relation to a planar surface](course:the-kervaire-conjecture/from-a-relation-to-a-planar-surface) on the Kervaire conjecture, and [From a kernel relation to a solution](course:nonsingular-systems-over-groups/from-a-kernel-relation-to-a-solution) on nonsingular systems of equations over groups.

Throughout, \(I=[0,1]\), \(D^n\) is the closed unit ball of \(\mathbb R^n\) and \(S^{n-1}\) its boundary sphere; a point of \(D^n\) is written \(ru\) with \(0\le r\le1\) and \(u\in S^{n-1}\). A *homotopy* is a map \(H\colon Y\times I\to W\), and \(H_t=H(\cdot,t)\); it is *constant on* a set \(A\subseteq Y\) if \(H_t(a)=H_0(a)\) for all \(a\in A\) and all \(t\). A map \(f\colon Y\to W\) is a *homotopy equivalence* if there is a map \(g\colon W\to Y\) with \(gf\simeq\mathrm{id}_Y\) and \(fg\simeq\mathrm{id}_W\). A space is *contractible* if its identity is homotopic to a constant map.

## 1. Cell complexes

**Definition 1.1.** A *cell complex* is a space \(X\) with subspaces \(X^0\subseteq X^1\subseteq\cdots\), its *skeleta*, such that:

1. \(X^0\) is a discrete space; its points are the *vertices*.
2. For \(n\ge1\), \(X^n\) is obtained from \(X^{n-1}\) by attaching \(n\)-disks: there are copies \(D^n_\alpha\) of \(D^n\), indexed by a set \(J_n\), and maps \(\varphi_\alpha\colon\partial D^n_\alpha\to X^{n-1}\), and \(X^n\) is the quotient of the disjoint union of \(X^{n-1}\) and the disks \(D^n_\alpha\) by the identifications \(x\sim\varphi_\alpha(x)\) for \(x\in\partial D^n_\alpha\).
3. \(X\) is the union of the \(X^n\), and a subset of \(X\) is closed exactly when its intersection with every \(X^n\) is closed in \(X^n\).

The maps \(\varphi_\alpha\) are the *attaching maps*. The *characteristic map* \(\Phi_\alpha\colon D^n_\alpha\to X\) is induced by the inclusion of \(D^n_\alpha\); it is injective on the interior of the disk, whose image \(e_\alpha\) is an *open \(n\)-cell*, and \(\Phi_\alpha(D^n_\alpha)\) is the *closed cell*. For a vertex \(v\) put \(D^0=\{0\}\) and \(\Phi_v(0)=v\). The space \(X\) is the disjoint union of its open cells. It has *dimension* at most \(n\) if \(X=X^n\), and it is *finite* if it has finitely many cells. A *graph* is a cell complex of dimension at most one; its \(1\)-cells are its *edges*.

The map from \(X^{n-1}\) to \(X^n\) is a closed embedding: a closed set \(C\subseteq X^{n-1}\) has the closed saturated preimage \(C\sqcup\bigsqcup_\alpha\varphi_\alpha^{-1}(C)\). By induction over \(n\) and condition 3, a set \(C\subseteq X\) is closed exactly when \(\Phi_\alpha^{-1}(C)\) is closed for every cell \(\alpha\) of every dimension; in other words, the map onto \(X\) from the disjoint union of all disks \(D_\alpha\) is a quotient map. So a map from \(X\) to a space is continuous exactly when its composites with all characteristic maps are continuous. The product of a quotient map with \(I\) is a quotient map [Grassmannians and classifying maps, Section 7, the paragraph after Lemma 7.1](course:DG-CHAR/DG-CHAR-03). Hence a homotopy \(X\times I\to W\) is continuous exactly when its composites with all maps \(\Phi_\alpha\times\mathrm{id}_I\) are continuous; the homotopies below are shown to be continuous in this way.

**Lemma 1.2.** Every cell complex \(X\) is Hausdorff, and every closed cell of \(X\) meets only finitely many open cells. So \(X\) is a CW complex in the sense of [Grassmannians and classifying maps, Section 7](course:DG-CHAR/DG-CHAR-03): Hausdorff, closure-finite, and with the weak topology of its characteristic maps.

*Proof.* *Collars.* For an open set \(U\subseteq X^{n-1}\) let \(U^+\subseteq X^n\) be the union of \(U\) and the sets
\[
\Phi_\alpha\bigl(\{ru:\ u\in\varphi_\alpha^{-1}(U),\ r>\tfrac12\}\bigr)
\]
over the \(n\)-cells \(\alpha\). The preimage of \(U^+\) under \(\Phi_\alpha\) is the set displayed in the parentheses, which is open in \(D^n_\alpha\), and \(U^+\cap X^{n-1}=U\); so \(U^+\) is open in \(X^n\). If \(U\cap V=\varnothing\), then \(U^+\cap V^+=\varnothing\), because the sets \(\varphi_\alpha^{-1}(U)\) and \(\varphi_\alpha^{-1}(V)\) are disjoint.

*The skeleta.* The discrete space \(X^0\) is Hausdorff. Suppose that \(X^{n-1}\) is Hausdorff, and let \(x\ne y\) be points of \(X^n\). If both lie in \(X^{n-1}\), separate them there by open sets \(U,V\); then \(U^+\) and \(V^+\) separate them in \(X^n\). If \(x=\Phi_\alpha(r_0u_0)\) with \(r_0<1\) lies in an open \(n\)-cell and \(y\in X^{n-1}\), let \(B\) be the image of the open ball of radius \((1-r_0)/2\) about \(r_0u_0\), and let \(W\) be the union of \(X^{n-1}\) and the sets \(\Phi_\beta(\{ru:r>(1+r_0)/2\})\) over all \(n\)-cells \(\beta\). Both sets are open in \(X^n\), as their preimages under the characteristic maps show; they contain \(x\) and \(y\), and they are disjoint. Two points of open \(n\)-cells have disjoint neighbourhoods that are images of small open balls. So \(X^n\) is Hausdorff.

*The whole complex.* Let \(x,y\in X^m\) be separated by open sets \(U_m,V_m\) of \(X^m\), and put \(U_{k+1}=U_k^+\) and \(V_{k+1}=V_k^+\) for \(k\ge m\). Since \(U_{k+1}\cap X^k=U_k\), the union \(U\) of the \(U_k\) meets every \(X^k\) in an open set, so it is open in \(X\); likewise the union \(V\) of the \(V_k\), and \(U\cap V=\varnothing\).

*Closure-finiteness.* Suppose that \(X^{n-1}\) is closure-finite. Then it is a CW complex in the sense of [Grassmannians and classifying maps, Section 7](course:DG-CHAR/DG-CHAR-03), and by Lemma 7.1 there the compact set \(\varphi_\alpha(\partial D^n_\alpha)\) meets only finitely many open cells. The closed cell \(\Phi_\alpha(D^n_\alpha)\) is the union of \(e_\alpha\) and this set. By induction over \(n\), every closed cell meets only finitely many open cells. \(\square\)

Consequently the facts proved in [Grassmannians and classifying maps, Section 7](course:DG-CHAR/DG-CHAR-03) hold for cell complexes: *every compact subset lies in a finite subcomplex* (Lemma 7.1 there), and *every point has a basis of path-connected open neighbourhoods \(U\) in which every loop is null-homotopic in \(U\)* (Lemma 7.2 there). In particular cell complexes are locally path-connected.

A *subcomplex* of \(X\) is a closed set \(A\subseteq X\) that is a union of open cells. It contains the closed cell of each of its cells, since a closed cell is compact, hence closed by Lemma 1.2, and is the closure of the open cell. With these cells \(A\) is a cell complex with skeleta \(A\cap X^n\), and its topology as a subspace of \(X\) is the one of Definition 1.1: by induction over \(n\), a set that is closed in the latter topology meets every \(X^n\) in a closed set, because an \(n\)-cell of \(X\) outside \(A\) meets \(A\) only in the image of its boundary sphere. A *subgraph* of a graph is a subcomplex. We use the *homotopy extension property* proved in [Frame fields and primary obstructions, Section E, the paragraph after (E.1)](course:DG-CHAR/DG-CHAR-08B): *if \(A\) is a subcomplex of a cell complex \(X\), every map from \(X\times\{0\}\cup A\times I\) to a space \(W\) extends to a map \(X\times I\to W\).*

## 2. Collapsing a contractible subcomplex

Let \(A\) be a nonempty subcomplex of a cell complex \(Y\). The space \(Y/A\) arises from \(Y\) by identifying \(A\) to one point \(\ast\), with the quotient topology; let \(q\colon Y\to Y/A\) be the quotient map.

**Proposition 2.1.** Let \(A\) be a nonempty subcomplex of a cell complex \(Y\).

1. \(Y/A\) is a cell complex whose vertices are \(\ast\) and the vertices of \(Y\) outside \(A\), and whose \(n\)-cells, for \(n\ge1\), are the images of the \(n\)-cells of \(Y\) outside \(A\), with the characteristic maps \(q\circ\Phi_\alpha\).
2. If \(A\) is contractible, then \(q\) is a homotopy equivalence. More precisely, there are a map \(g\colon Y/A\to Y\), a homotopy from \(gq\) to \(\mathrm{id}_Y\) that maps \(A\) into \(A\) at all times, and a homotopy from \(qg\) to \(\mathrm{id}_{Y/A}\) that fixes \(\ast\) at all times.

*Proof.* 1. Let \(Z\) be the set \(Y/A\) with the following structure: \(Z^0\) consists of \(\ast\) and the vertices outside \(A\), and \(Z^n\) is obtained from \(Z^{n-1}\) by attaching the \(n\)-cells \(\alpha\) of \(Y\) outside \(A\) along \(q\circ\varphi_\alpha\), which maps into \(q(Y^{n-1})=Z^{n-1}\). This is a cell complex whose underlying set is \(Y/A\) and whose characteristic maps are the maps \(q\circ\Phi_\alpha\) for the cells \(\alpha\) outside \(A\). By Section 1, a set \(C\) is closed in \(Z\) exactly when all sets \((q\Phi_\alpha)^{-1}(C)\) with \(\alpha\) outside \(A\) are closed. It is closed in the quotient topology exactly when \(q^{-1}(C)\) is closed in \(Y\), that is, when \(\Phi_\beta^{-1}(q^{-1}(C))\) is closed for every cell \(\beta\) of \(Y\). For \(\beta\) in \(A\) the map \(q\Phi_\beta\) is constant, so this preimage is empty or all of \(D_\beta\). Hence the two topologies agree.

2. Let \(c\colon A\times I\to A\) be a homotopy with \(c_0=\mathrm{id}_A\) and \(c_1\) constant. By the homotopy extension property there is a homotopy \(H\colon Y\times I\to Y\) with \(H_0=\mathrm{id}_Y\) and \(H_t=c_t\) on \(A\); in particular \(H_t(A)\subseteq A\). Since \(H_1\) is constant on \(A\), \(H_1=g\circ q\) for a unique function \(g\colon Y/A\to Y\), continuous because \(q\) is a quotient map; and \(H\) runs from \(\mathrm{id}_Y\) to \(gq\). The maps \(q\circ H_t\) send \(A\) to \(\ast\), so \(q\circ H=K\circ(q\times\mathrm{id}_I)\) for a function \(K\colon(Y/A)\times I\to Y/A\), continuous because \(q\times\mathrm{id}_I\) is a quotient map (Section 1). From \(K_0\circ q=q\) and \(K_1\circ q=qH_1=qgq\) we get \(K_0=\mathrm{id}_{Y/A}\) and \(K_1=qg\), and \(K_t(\ast)=\ast\). \(\square\)

## 3. Attaching cells along homotopic maps

For a space \(W\) and maps \(f_\alpha\colon S^{n-1}\to W\), \(\alpha\in J\), write \(W\cup_f\bigsqcup_\alpha D^n_\alpha\) for the quotient of \(W\sqcup\bigsqcup_\alpha D^n_\alpha\) by the identifications \(u\sim f_\alpha(u)\) for \(u\in\partial D^n_\alpha\), and \(\Phi_\alpha\) for the map induced by \(D^n_\alpha\).

**Proposition 3.1.** Let \(n\ge1\), let \(W\) be a space, and for each \(\alpha\in J\) let \(f_\alpha,f'_\alpha\colon S^{n-1}\to W\) be homotopic maps. Put \(Y=W\cup_f\bigsqcup_\alpha D^n_\alpha\) and \(Y'=W\cup_{f'}\bigsqcup_\alpha D^n_\alpha\). There are maps \(\phi\colon Y\to Y'\) and \(\psi\colon Y'\to Y\), both the identity on \(W\), with \(\psi\phi\simeq\mathrm{id}_Y\) and \(\phi\psi\simeq\mathrm{id}_{Y'}\) by homotopies that are constant on \(W\). In particular \(Y\) and \(Y'\) are homotopy equivalent.

*Proof.* Choose homotopies \(H^\alpha\colon S^{n-1}\times I\to W\) with \(H^\alpha_0=f_\alpha\) and \(H^\alpha_1=f'_\alpha\), and write \(\Phi_\alpha,\Phi'_\alpha\) for the maps of the disks into \(Y\) and \(Y'\). Define \(\phi\) as the identity on \(W\) and on the disks by
\[
\phi(\Phi_\alpha(ru))=
\begin{cases}
\Phi'_\alpha(2ru),&r\le\tfrac12,\\
H^\alpha(u,2-2r),&r\ge\tfrac12.
\end{cases}
\]
At \(r=\frac12\) both lines give \(f'_\alpha(u)\), and at \(r=1\) the second line gives \(f_\alpha(u)\), the point of \(W\) identified with \(u\); so \(\phi\) is well defined and continuous. Define \(\psi\) as the identity on \(W\) and by \(\psi(\Phi'_\alpha(ru))=\Phi_\alpha(2ru)\) for \(r\le\frac12\) and \(\psi(\Phi'_\alpha(ru))=H^\alpha(u,2r-1)\) for \(r\ge\frac12\). On the disks,
\[
\psi\phi(\Phi_\alpha(ru))=
\begin{cases}
\Phi_\alpha(4ru),&r\le\tfrac14,\\
H^\alpha(u,\tau(r)),&r\ge\tfrac14,
\end{cases}
\]
where \(\tau(r)=4r-1\) for \(\frac14\le r\le\frac12\) and \(\tau(r)=2-2r\) for \(\frac12\le r\le1\). A first homotopy replaces \(\tau(r)\) by \((1-s)\tau(r)\), \(0\le s\le1\). It is continuous, because \(\tau(\frac14)=\tau(1)=0\) and \(H^\alpha(u,0)=f_\alpha(u)=\Phi_\alpha(u)\), and it is constant on \(W\). At \(s=1\) it gives \(\Phi_\alpha\circ\rho_0\), where
\[
\rho_s(ru)=\min\{(4-3s)r,\,1\}\,u .
\]
A second homotopy \(\Phi_\alpha\circ\rho_s\), \(0\le s\le1\), ends at \(\Phi_\alpha\), and it is constant on \(W\) because every \(\rho_s\) fixes \(\partial D^n\). Joined, and extended by the identity of \(W\), the two homotopies are continuous on \(Y\times I\), since the product of the quotient map \(W\sqcup\bigsqcup_\alpha D^n_\alpha\to Y\) with \(I\) is a quotient map (Section 1). So \(\psi\phi\simeq\mathrm{id}_Y\). The same argument with \(f\) and \(f'\) exchanged gives \(\phi\psi\simeq\mathrm{id}_{Y'}\). \(\square\)

If \(W\) is a cell complex of dimension at most \(n-1\), then \(Y\) and \(Y'\) are cell complexes with \(W\) as their \((n-1)\)-skeleton.

## 4. Graphs and trees

Let \(Y\) be a graph, and choose for each edge \(e\) a characteristic map \(\Phi_e\colon I\to Y\), with \(I\) in place of \(D^1\). The edge has two *darts*: \(e^+\), running from \(\Phi_e(0)\) to \(\Phi_e(1)\), and \(e^-\), running back; the *tail* of a dart is the vertex where it starts, and \(\theta\) exchanges the two darts of each edge. With these darts \(Y\) is a graph in the sense of [Words, free groups and Cayley graphs, Section 3](course:van-kampen-diagrams/words-free-groups-and-cayley-graphs), and we use the *walks*, *backtracks*, *homotopy of walks*, *reduced walks*, *cycles* and *trees* defined there. Conversely, a graph given by darts is the set of darts of a cell complex of dimension one, its *realization*, which has one edge for each pair \(\{d,\theta d\}\), attached at the tail and the head of one of the two darts. A graph is *connected* if any two vertices are joined by a walk.

The *path* of a walk \(c=(d_1,\ldots,d_k)\) with \(k\ge1\) is the path \(|c|\colon I\to Y\) that traverses \(d_j\) during the interval \([\frac{j-1}k,\frac jk]\):
\[
|c|(t)=
\begin{cases}
\Phi_{e_j}(kt-j+1),&d_j=e_j^+,\\
\Phi_{e_j}(j-kt),&d_j=e_j^-.
\end{cases}
\]
The path of the empty walk at a vertex is the constant path there.

**Lemma 4.1.** A nonempty graph is path-connected exactly when it is connected. Let \(T\) be a tree and \(v_0\) a vertex of \(T\). Every vertex \(u\) of \(T\) is the end of exactly one reduced walk \(c_u\) from \(v_0\). For every edge of \(T\), with darts \(d\) from \(u\) to \(w\) and \(\theta d\) from \(w\) to \(u\), exactly one of the equations \(c_w=c_u\,d\) and \(c_u=c_w\,\theta d\) holds.

*Proof.* If \(Y\) is connected, the paths of walks join any two vertices, and every point of an edge is joined to an endpoint inside the closed edge. Conversely, let \(C\) be the set of vertices joined to a vertex \(v_0\) by walks; an edge with one endpoint in \(C\) has both endpoints in \(C\). The union of \(C\) and the edges at \(C\), and the union of the remaining cells, are disjoint subcomplexes covering \(Y\), so both are closed; a path from \(v_0\) stays in the first, since \(I\) is connected. So a path-connected graph is connected.

Let \(T\) be a tree. A walk from \(v_0\) to \(u\) exists because \(T\) is connected, and it is homotopic to a reduced walk by [Words, free groups and Cayley graphs, Lemma 3.1](course:van-kampen-diagrams/words-free-groups-and-cayley-graphs). If \(c\) and \(c'\) are reduced walks from \(v_0\) to \(u\), and \(\bar c'\) is the reverse of \(c'\), then the closed walk \(c\,\bar c'\) is homotopic to the empty walk by Lemma 3.3 there, so \(c\simeq c\,\bar c'c'\simeq c'\), and \(c=c'\) by the uniqueness in Lemma 3.1 there. For the edge, \(c_u\,d\) is a walk from \(v_0\) to \(w\). If \(c_u\) does not end with \(\theta d\), this walk is reduced, and \(c_w=c_u\,d\). If \(c_u=c'\,\theta d\), then \(c'\) is a reduced walk from \(v_0\) to \(w\), so \(c_w=c'\) and \(c_u=c_w\,\theta d\). The two equations cannot both hold, since the first makes \(c_w\) longer than \(c_u\) and the second shorter. \(\square\)

A tree has no loops, since a loop is a cycle. For an edge of a tree with \(c_w=c_u\,d\), the vertex \(u\) is the *parent* and \(w\) the *child*; we choose \(\Phi_e\) so that \(\Phi_e(0)\) is the parent and \(\Phi_e(1)\) the child.

**Proposition 4.2** (trees are contractible). Let \(T\) be a tree and \(v_0\) a vertex. There is a homotopy \(H\colon T\times I\to T\) from \(\mathrm{id}_T\) to the constant map with value \(v_0\) such that \(H_t(v_0)=v_0\) for all \(t\).

*Proof.* For an edge \(e\) with parent \(u\) and child \(w\), let \(k\) be the length of \(c_u\), so that \(c_w=c_u\,e^+\) has length \(k+1\), and let \(\Omega_e\colon[0,k+1]\to T\) traverse \(c_w\) at unit speed, \(\Omega_e(\sigma)=|c_w|(\sigma/(k+1))\). Put
\[
H(\Phi_e(s),t)=\Omega_e\bigl((1-t)(k+s)\bigr)
\]
for \(s,t\in I\), and \(H(v_0,t)=v_0\). At \(s=0\) the formula gives \(\Omega_e((1-t)k)\), which depends only on \(c_u\), since \(\Omega_e\) traverses \(c_u\) at unit speed on \([0,k]\); it agrees with the value of the formula at \(s=1\) for the edge whose child is \(u\), and with \(v_0\) if \(u=v_0\). So \(H\) is well defined, and it is continuous on every closed edge times \(I\), hence on \(T\times I\) (Section 1). Since \(\Omega_e(k+s)=\Phi_e(s)\), \(H_0\) is the identity, and \(H_1\) is constant with value \(\Omega_e(0)=v_0\). \(\square\)

**Lemma 4.3** (spanning trees). Every nonempty connected graph \(Y\) contains a subgraph that is a tree and contains all vertices of \(Y\), a *spanning tree*.

*Proof.* Order the subgraphs of \(Y\) that are trees by inclusion. The union of a chain of trees is a tree: two of its vertices lie in a common member and are joined by a walk there, and a cycle, which has finitely many edges, would lie in one member. A single vertex is a tree, so by Zorn's lemma there is a maximal tree \(T\). If a vertex of \(Y\) were outside \(T\), a walk from a vertex of \(T\) to it would contain a dart \(d\) from a vertex of \(T\) to a vertex \(w\) outside \(T\). Adding \(w\) and the edge of \(d\) to \(T\) gives a connected subgraph in which \(w\) has degree one. A cycle has degree two at each of its vertices, so it cannot pass through \(w\), and every cycle of the larger subgraph lies in \(T\); there is none. This contradicts the maximality of \(T\). \(\square\)

**Corollary 4.4.** Let \(T\) be a tree contained in the \(1\)-skeleton of a cell complex \(Y\). Then \(q\colon Y\to Y/T\) is a homotopy equivalence, and \(Y/T\) is a cell complex with one vertex for \(T\) and one cell for every cell of \(Y\) outside \(T\). If \(T\) contains all vertices of \(Y\), then \(Y/T\) has exactly one vertex, and its edges are the images of the edges of \(Y\) outside \(T\).

*Proof.* \(T\) is a subgraph of \(Y^1\), hence closed in \(Y^1\) and in \(Y\), and a union of open cells; so it is a subcomplex of \(Y\), contractible by Proposition 4.2. Apply Proposition 2.1. \(\square\)

## 5. Triangulations and simplicial approximation

A *simplicial complex* \(M\) is a set of vertices together with a set of nonempty finite subsets, the *simplices*, that contains every one-element set and every nonempty subset of a simplex. Its *realization* \(|M|\) is the set of functions \(x\) from the vertices to \([0,1]\) whose support is a simplex and whose values add up to \(1\); the closed simplex of \(\sigma\) consists of the \(x\) supported in \(\sigma\), with the topology of the standard simplex, and a subset of \(|M|\) is closed exactly when it meets every closed simplex in a closed set. With the open simplices as cells, \(|M|\) is a cell complex. The *carrier* of a point \(x\) is its support, the simplex whose open simplex contains \(x\). A map between realizations is *simplicial* if it maps vertices to vertices, the vertices of each simplex to the vertices of a simplex, and is affine on every closed simplex.

Let \(Y\) be a cell complex of dimension at most two, and let \(\omega\colon I\to\partial D^2\), \(\omega(t)=(\cos2\pi t,\sin2\pi t)\). A \(2\)-cell \(\alpha\) is *attached along* the closed walk \(c\) of length \(r\ge1\) in the graph \(Y^1\) if \(\varphi_\alpha(\omega(t))=|c|(t)\) for all \(t\in I\), and *along the empty walk at a vertex* \(v\) if \(\varphi_\alpha\) is constant with value \(v\).

**Proposition 5.1** (triangulating two-complexes). Let \(Y\) be a finite cell complex of dimension at most two whose \(2\)-cells are attached along closed walks. There are a finite simplicial complex \(K\), a subcomplex \(L\) and a homeomorphism \(h\colon|K|\to Y\) with \(h(|L|)=Y^1\), such that \(L\) arises from \(Y^1\) by dividing every edge into three edges and \(h\) maps these three edges affinely onto the thirds \(\Phi_e([0,\frac13])\), \(\Phi_e([\frac13,\frac23])\), \(\Phi_e([\frac23,1])\).

*Proof.* *The complex.* The vertices of \(K\) are the vertices of \(Y\); two vertices \(e_1,e_2\) for every edge \(e\); for every \(2\)-cell \(\alpha\) attached along a closed walk of length \(r\ge1\), a vertex \(o_\alpha\) and vertices \(q_{\alpha,1},\ldots,q_{\alpha,3r}\); and for every \(2\)-cell \(\alpha\) attached along an empty walk at a vertex \(v\), three vertices \(a_\alpha,b_\alpha,z_\alpha\). The edges of \(L\) are \(\{\Phi_e(0),e_1\}\), \(\{e_1,e_2\}\) and \(\{e_2,\Phi_e(1)\}\) for every edge \(e\); since \(e_1\) and \(e_2\) are new vertices, \(L\) has no loops and no two edges with the same endpoints. A closed walk \(c\) of length \(r\) in \(Y^1\) gives a closed walk of length \(3r\) in \(L\), each dart of \(c\) replaced by three; let \(p_0,p_1,\ldots,p_{3r}=p_0\) be its vertices. For \(\alpha\) attached along \(c\), with indices of the \(q_{\alpha,j}\) taken modulo \(3r\), the simplices of \(K\) include the triangles
\[
\begin{gathered}
\{p_{j-1},p_j,q_{\alpha,j}\},\qquad\{p_{j-1},q_{\alpha,j-1},q_{\alpha,j}\},\\
\{o_\alpha,q_{\alpha,j-1},q_{\alpha,j}\},\qquad 1\le j\le3r .
\end{gathered}
\]
For \(\alpha\) attached at \(v\), they include the four triangles of the tetrahedron \(\{v,a_\alpha,b_\alpha,z_\alpha\}\). The simplices of \(K\) are these triangles, the simplices of \(L\), and all nonempty subsets of these.

*A polygon for each cell.* For \(\alpha\) attached along a walk of length \(r\ge1\), let \(P_\alpha\subseteq\mathbb R^2\) be the convex polygon with the vertices \(P_j=\omega(j/3r)\), and put \(Q_j=\frac12P_j\), with indices modulo \(3r\). The polygon is the union of the \(3r\) triangles \([0,P_{j-1},P_j]\); the segment \([Q_{j-1},Q_j]\), parallel to \([P_{j-1},P_j]\), divides each of them into the triangle \([0,Q_{j-1},Q_j]\) and a trapezoid, which the diagonal \([P_{j-1},Q_j]\) divides into the triangles \([P_{j-1},P_j,Q_j]\) and \([P_{j-1},Q_{j-1},Q_j]\). This triangulates \(P_\alpha\). The assignment \(P_j\mapsto p_j\), \(Q_j\mapsto q_{\alpha,j}\), \(0\mapsto o_\alpha\), affine on triangles, maps \(P_\alpha\) onto the union of the closed simplices of \(\alpha\). It is injective off the boundary of the polygon: every simplex of the triangulation not contained in the boundary has a vertex \(Q_j\) or \(0\), and two such simplices have different vertex sets in \(K\). Indeed the vertices \(q_{\alpha,j}\) and \(o_\alpha\) are distinct, so the only possible coincidence is between the edges \([P_{j-1},Q_j]\) and \([P_j,Q_j]\), which would require \(p_{j-1}=p_j\); but \(p_{j-1}\) and \(p_j\) are the ends of an edge of \(L\), which has no loops. So \(|K|\) is obtained from \(|L|\) by gluing each polygon \(P_\alpha\) along the map of its boundary that sends the side \([P_{j-1},P_j]\) affinely onto the edge \(\{p_{j-1},p_j\}\), and by gluing a tetrahedron boundary at \(v\) for each cell attached along an empty walk; a continuous bijection from the compact glued space onto the Hausdorff space \(|K|\) is a homeomorphism.

*The homeomorphism.* Let \(h\) map \(|L|\) onto \(Y^1\) by the affine maps of the statement; it is a homeomorphism. Let \(\beta_\alpha\colon\partial P_\alpha\to\partial D^2\) send the point of the side \([P_{j-1},P_j]\) with affine parameter \(\lambda\) to \(\omega((j-1+\lambda)/3r)\), and extend it to a homeomorphism \(\psi_\alpha\colon P_\alpha\to D^2\) by \(\psi_\alpha(sb)=s\,\beta_\alpha(b)\) for \(b\in\partial P_\alpha\) and \(0\le s\le1\). Put \(h=\Phi_\alpha\circ\psi_\alpha\) on \(P_\alpha\). On the side \([P_{j-1},P_j]\) this is \(|c|\) at the time \((j-1+\lambda)/3r\), which traverses, at the affine parameter \(\lambda\), the third of a dart of \(c\) that corresponds to the edge \(\{p_{j-1},p_j\}\) of \(L\); so it agrees with \(h\) on \(|L|\). For a cell attached along an empty walk at \(v\), let \(h\) map the tetrahedron boundary homeomorphically onto \(\Phi_\alpha(D^2)\), which is a sphere because \(\partial D^2\) is mapped to the point \(v\), with \(v\) mapped to \(v\). The resulting map \(h\colon|K|\to Y\) is continuous and bijective, from a compact space onto a space that is Hausdorff by Lemma 1.2, hence a homeomorphism. \(\square\)

**Proposition 5.2** (simplicial approximation). Let \(K\) be a finite simplicial complex, \(M\) a simplicial complex and \(f\colon|K|\to|M|\) a map. For some iterated barycentric subdivision \(K'\) of \(K\) there is a simplicial map \(g\colon|K'|\to|M|\) such that \(g(x)\) lies in the closed simplex of the carrier of \(f(x)\) for every \(x\), and the homotopy \(H_t(x)=(1-t)f(x)+tg(x)\) from \(f\) to \(g\) moves every point inside that closed simplex. In particular, if \(f(x)\) lies in the realization of a subcomplex \(N\) of \(M\), then \(H_t(x)\in|N|\) for all \(t\).

*Proof.* The compact set \(f(|K|)\) lies in a finite subcomplex \(M_0\) of \(M\) (Section 1). By the proof of [Frame fields and primary obstructions, Lemma A.1](course:DG-CHAR/DG-CHAR-08B), applied to \(f\colon|K|\to|M_0|\), there are an iterated barycentric subdivision \(K'\) and, for every vertex \(v\) of \(K'\), a vertex \(g(v)\) of \(M_0\) such that \(f\) maps the closed star of \(v\) into the open star of \(g(v)\), the set of points \(y\) with \(y(g(v))>0\); and \(g\) extends to a simplicial map. Let \(x\) lie in the open simplex of \(K'\) with vertices \(v_0,\ldots,v_m\). Then \(x\) lies in the closed star of every \(v_j\), so \(f(x)(g(v_j))>0\) for all \(j\): every \(g(v_j)\) is a vertex of the carrier \(\sigma\) of \(f(x)\). Since \(g(x)\) is a convex combination of the \(g(v_j)\), it lies in the closed simplex of \(\sigma\), and so does the segment from \(f(x)\) to \(g(x)\). The realization of the finite complex \(M_0\) is a subspace of the Euclidean space of functions on its vertices, in which the formula for \(H\) is continuous; so \(H\) is continuous. A subcomplex \(N\) with \(f(x)\in|N|\) contains the carrier of \(f(x)\), hence its closed simplex. \(\square\)

## 6. Exercises

**6.1.** Let \(W\) be a path-connected space, \(w_0\in W\), and let \(f\colon S^{n-1}\to W\) be null-homotopic. Show that \(W\cup_fD^n\) is homotopy equivalent to the space obtained from \(W\) and the sphere \(D^n/\partial D^n\) by identifying \(w_0\) with the point \(\partial D^n/\partial D^n\).

**6.2.** Let \(Y\) be the graph with two vertices \(u,w\) and three edges \(e,f,g\) from \(u\) to \(w\). Show that the subgraph consisting of \(u\), \(w\) and \(e\) is a spanning tree and that \(Y\) is homotopy equivalent to a graph with one vertex and two loops. Is the subgraph consisting of \(u,w,e,f\) a tree?

**6.3.** Show that a finite tree with \(V\) vertices has \(V-1\) edges.

**6.4.** Let \(Y\) have one vertex, two edges \(a,b\) and one \(2\)-cell attached along the closed walk \((a^+,b^+,a^-,b^-)\). Count the vertices, edges and triangles of the simplicial complex \(K\) of Proposition 5.1, and check that their alternating sum is \(0\).

**6.5.** Show that a cell complex whose \(1\)-skeleton is path-connected is path-connected.

## 7. Solutions

**6.1.** The map \(f\) is homotopic to a constant map with some value \(w_1\). A path \(\gamma\) from \(w_1\) to \(w_0\) gives the homotopy \((u,t)\mapsto\gamma(t)\) from this constant map to the constant map \(f'\) with value \(w_0\). By Proposition 3.1, \(W\cup_fD^n\simeq W\cup_{f'}D^n\). In \(W\cup_{f'}D^n\) the whole boundary sphere is identified with \(w_0\), so this space is \(W\) with the sphere \(D^n/\partial D^n\) attached at \(w_0\).

**6.2.** The subgraph \(\{u,w,e\}\) is connected and has no cycle, since its only edge is not a loop; it contains both vertices. By Corollary 4.4, \(Y\) is homotopy equivalent to \(Y/T\), which has one vertex and the two loops \(f,g\). The subgraph \(\{u,w,e,f\}\) is not a tree: the two edges \(e,f\) joining \(u\) and \(w\) form a cycle.

**6.3.** Choose a vertex \(v_0\). By Lemma 4.1 every edge has exactly one child, and every vertex \(w\ne v_0\) is the child of exactly one edge, the edge of the last dart of \(c_w\). So the edges correspond to the vertices other than \(v_0\).

**6.4.** \(L\) has \(1+2\cdot2=5\) vertices and \(3\cdot2=6\) edges. The walk has length \(r=4\), so the cell contributes \(o_\alpha\) and \(12\) vertices \(q_{\alpha,i}\), \(36\) triangles, and the edges \(\{p_{i-1},q_{\alpha,i}\}\), \(\{p_i,q_{\alpha,i}\}\), \(\{q_{\alpha,i},q_{\alpha,i+1}\}\), \(\{o_\alpha,q_{\alpha,i}\}\): \(48\) new edges; the \(12\) sides of the polygon are edges of \(L\). So \(K\) has \(18\) vertices, \(54\) edges and \(36\) triangles, and \(18-54+36=0\).

**6.5.** Let \(v_0\) be a vertex. By induction over \(n\), every point of \(X^n\) is joined to \(v_0\) by a path: for \(n=1\) by hypothesis; a point \(\Phi_\alpha(ru)\) of an \(n\)-cell, \(n\ge2\), is joined by the path \(t\mapsto\Phi_\alpha((r+t(1-r))u)\) to the point \(\varphi_\alpha(u)\) of \(X^{n-1}\).

## References

- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Chapter 0 (Propositions 0.16 to 0.18 on homotopy extension, collapsing subcomplexes and attaching maps), Section 1.A (Proposition 1A.1 on maximal trees), the Appendix (topology of cell complexes) and Section 2.C (Theorem 2C.1, simplicial approximation), on the author's page. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
