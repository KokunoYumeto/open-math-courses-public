# Universal covers and cellular chains

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The universal cover of a connected cell complex is again a cell complex: its cells are the lifts of the cells of the base, and the fundamental group of the base acts on it by deck transformations, permuting the lifts of every cell freely and transitively. Its cellular chains are therefore free modules over the group ring, and its homology is computed from the attaching maps of the base. This lesson collects these facts in the form in which the courses of the programme on group rings and classifying spaces use them: the universal cover and its deck group, the lifting criterion, covers for normal subgroups, the lifting of homotopy equivalences, the boundary formula for cells attached along closed walks, and the cellular chain complex of the universal cover of a presentation complex, the Cayley complex.

- Universal covers of cell complexes (Section 1).
- Lifting maps (Section 2).
- Covers for normal subgroups (Section 3).
- Homotopy equivalences (Section 4).
- Cellular chains (Section 5).
- The Cayley complex of a presentation (Section 6).

Cell complexes, walks and presentation complexes are as in [Cell complexes and homotopy equivalences](cell-complexes-and-homotopy-equivalences.md) and [Fundamental groups of graphs and two-complexes](fundamental-groups-of-graphs-and-two-complexes.md); the results of the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) listed in Section 1 of the latter lesson are used freely. In addition we use from that course: the *homotopy lifting property* [Algebraic Topology, Lecture 9, Corollary 9.4]: for a covering \(p\colon Z\to X\), a homotopy \(H\colon I\times F\to X\) from any space \(F\), and a lift of \(H_0\), there is exactly one lift of \(H\) extending it; *uniqueness of lifts* [Lecture 17, Lemma 17.1]: two lifts of a map from a path-connected space that agree at one point are equal; the *transport* bijections \(\gamma_*\colon p^{-1}(\gamma(0))\to p^{-1}(\gamma(1))\), \(z\mapsto\) the end of the lift of \(\gamma\) from \(z\), with \((\gamma*\eta)_*=\eta_*\gamma_*\) [Lecture 5, Corollary 5.3, and Lecture 7, Lemma 7.1]; the *universal cover* [Lecture 16, Proposition 16.2], the *quotient of a covering by a fibrewise action* [Lecture 16, Proposition 16.1] and the *realization of subgroups* [Lecture 16, Corollary 16.1].

## 1. Universal covers of cell complexes

A *deck transformation* of a covering \(p\colon Z\to X\) is a homeomorphism \(L\colon Z\to Z\) with \(pL=p\).

**Theorem 1.1.** Let \(X\) be a connected cell complex, \(x_0\) a vertex and \(G=\pi_1(X,x_0)\).

1. There is a covering \(p\colon\widetilde X\to X\) with \(\widetilde X\) simply connected. Fix \(\tilde x_0\in p^{-1}(x_0)\).
2. For every \(g\in G\) there is exactly one deck transformation \(L_g\) with \(L_g(\tilde x_0)=\tilde x_0\cdot g\). Then \(L_{gh}=L_gL_h\) and \(L_1=\mathrm{id}\); the action of \(G\) is free, transitive on every fibre of \(p\), and every deck transformation is some \(L_g\).
3. \(\widetilde X\) is a cell complex whose cells are the lifts of the cells of \(X\): for every cell \(\alpha\) of \(X\) and every point \(z\) over \(\Phi_\alpha(0)\) there is exactly one map \(\widetilde\Phi\colon D_\alpha\to\widetilde X\) with \(p\widetilde\Phi=\Phi_\alpha\) and \(\widetilde\Phi(0)=z\), and these maps are the characteristic maps of \(\widetilde X\), with skeleta \(\widetilde X^n=p^{-1}(X^n)\). Every \(L_g\) maps lifts to lifts, \(\widetilde\Phi\mapsto L_g\widetilde\Phi\), and \(G\) permutes the lifts of each cell freely and transitively.
4. For \(n\ge2\), \(p_*\colon\pi_n(\widetilde X,\tilde x_0)\to\pi_n(X,x_0)\) is an isomorphism.

*Proof.* By [Fundamental groups of graphs and two-complexes, Corollary 3.4](fundamental-groups-of-graphs-and-two-complexes.md) the graph \(X^1\) is connected, hence path-connected, and so is \(X\), by [Cell complexes and homotopy equivalences, Exercise 6.5](cell-complexes-and-homotopy-equivalences.md). Every point of \(X\) has a basis of path-connected open neighbourhoods \(N\) in which every loop is null-homotopic in \(N\) (Section 1 of that lesson); for two paths \(\gamma,\eta\) in \(N\) with the same ends, \(\gamma*\bar\eta\) is null-homotopic, so \(\gamma\) and \(\eta\) are homotopic. So \(X\) is semilocally simply connected in the sense of [Algebraic Topology, Lecture 6, Definition 6.2], and [Lecture 16, Proposition 16.2] gives a simply connected covering, the space of classes \([\lambda]\) of paths from \(x_0\), with \(\tilde x_0\) the class of the constant path, on which \(G\) acts continuously, freely and fibrewise from the left by \([\gamma]\cdot[\lambda]=[\gamma*\lambda]\). The lift of a loop \(\gamma\) from \(\tilde x_0\) is \(t\mapsto[\gamma_t]\), \(\gamma_t(s)=\gamma(ts)\), so the action of \([\gamma]\) sends \(\tilde x_0\) to \([\gamma]=\tilde x_0\cdot[\gamma]\); call this deck transformation \(L_{[\gamma]}\). A deck transformation is a lift of \(p\) through \(p\), so it is determined by its value at \(\tilde x_0\) [Lecture 17, Lemma 17.1]; this gives the uniqueness, \(L_{gh}=L_gL_h\) and \(L_1=\mathrm{id}\). If \(L_g(z)=z\) for some \(z\), then \(L_g=\mathrm{id}\) by the same uniqueness, so \(\tilde x_0\cdot g=\tilde x_0\) and \(g=1\), because \(g\mapsto\tilde x_0\cdot g\) is a bijection onto \(p^{-1}(x_0)\) [Lecture 10, Corollary 10.1]; for the same reason every deck transformation \(L\), which maps \(\tilde x_0\) to some \(\tilde x_0\cdot g\), equals \(L_g\), and \(G\) acts transitively on \(p^{-1}(x_0)\). For a path \(\delta\) from \(x_0\) to \(x\), the transport \(\delta_*\) is a bijection from \(p^{-1}(x_0)\) onto \(p^{-1}(x)\) commuting with every \(L_g\), since \(L_g\) maps lifts of \(\delta\) to lifts of \(\delta\); so the action is transitive on every fibre.

Parts 3 and 4 are [Grassmannians and classifying maps, Theorem 8.3 and its proof](course:DG-CHAR/DG-CHAR-03), which constructs the cell structure of an arbitrary covering of a CW complex from the lifts of the characteristic maps, proves that its weak topology is the topology of the covering, and proves the isomorphisms on \(\pi_n\) for \(n\ge2\). A lift of \(\Phi_\alpha\) is unique once its value at \(0\) is given, by [Lecture 17, Lemma 17.1]. The map \(L_g\widetilde\Phi\) is a lift of \(\Phi_\alpha\) with value \(L_g(z)\) at \(0\). The lifts of \(\alpha\) correspond to the points of the fibre over \(\Phi_\alpha(0)\), on which \(G\) acts freely and transitively. \(\square\)

## 2. Lifting maps

**Proposition 2.1** (lifting criterion). Let \(p\colon Z\to X\) be a covering, \(z_0\in Z\), \(x_0=p(z_0)\), and let \(F\) be a path-connected and locally path-connected space, \(y_0\in F\), and \(f\colon F\to X\) a map with \(f(y_0)=x_0\). There is a lift \(\tilde f\colon F\to Z\) of \(f\) with \(\tilde f(y_0)=z_0\) exactly when \(f_*\pi_1(F,y_0)\subseteq p_*\pi_1(Z,z_0)\). The lift is then unique.

*Proof.* If \(\tilde f\) exists, then \(f_*=p_*\tilde f_*\). Conversely, suppose the inclusion holds. For \(y\in F\) choose a path \(\beta\) from \(y_0\) to \(y\) and put \(\tilde f(y)=(f\beta)_*(z_0)\), the end of the lift of \(f\circ\beta\) from \(z_0\). For another path \(\beta'\) the class of the loop \(f\circ(\beta*\bar\beta')\) lies in \(p_*\pi_1(Z,z_0)\), so it is the class of \(p\circ\delta\) for a loop \(\delta\) at \(z_0\); the lift of \(p\delta\) from \(z_0\) is \(\delta\), which is closed. Hence \((f\bar\beta')_*(f\beta)_*\) fixes \(z_0\), and \((f\beta)_*(z_0)=(f\beta')_*(z_0)\): \(\tilde f\) is well defined, \(p\tilde f=f\), and \(\tilde f(y_0)=z_0\). For continuity at \(y\), let \(W\) be an open neighbourhood of \(f(y)\) over which \(p\) is trivial, \(\widetilde W\) the sheet over \(W\) containing \(\tilde f(y)\), and \(V\) a path-connected open neighbourhood of \(y\) with \(f(V)\subseteq W\). For \(y'\in V\) and a path \(\beta''\) in \(V\) from \(y\) to \(y'\), the path \((p|_{\widetilde W})^{-1}\circ f\circ\beta''\) lifts \(f\beta''\) from \(\tilde f(y)\), so \(\tilde f(y')=(p|_{\widetilde W})^{-1}(f(y'))\). Thus \(\tilde f\) agrees on \(V\) with the continuous map \((p|_{\widetilde W})^{-1}\circ f\). Uniqueness is [Algebraic Topology, Lecture 17, Lemma 17.1]. \(\square\)

**Proposition 2.2.** Let \(p\colon Z\to X\) be a covering and \(F\) a connected space. Two lifts of a map \(f\colon F\to X\) that agree at one point are equal.

*Proof.* Let \(\tilde f_1,\tilde f_2\) be lifts and \(y\in F\). Choose an open neighbourhood \(W\) of \(f(y)\) and a homeomorphism \(p^{-1}(W)\cong W\times S\) over \(W\) with \(S\) discrete. On the open set \(f^{-1}(W)\) the second coordinates of \(\tilde f_1\) and \(\tilde f_2\) are continuous maps to \(S\), hence constant near \(y\). So near \(y\) the two lifts agree if they agree at \(y\), and differ if they differ at \(y\). The set where they agree is open and closed and nonempty, hence all of \(F\). \(\square\)

**Corollary 2.3.** Let \(p\colon Z\to X\) be a covering. Every map from a simply connected, locally path-connected space \(F\) to \(X\) lifts to \(Z\), with a prescribed value over the image of a prescribed point, and the lift is unique. This applies to every simply connected cell complex, in particular to spheres \(S^m\) with \(m\ge2\) and to disks. \(\square\)

## 3. Covers for normal subgroups

**Proposition 3.1.** Let \(X\) be a connected cell complex, \(x_0\) a vertex, \(G=\pi_1(X,x_0)\), and \(N\) a subgroup of \(G\). Let \(X_N=N\backslash\widetilde X\) be the space of orbits of \(N\) acting by deck transformations, with the quotient map \(q\colon\widetilde X\to X_N\), the map \(p_N\colon X_N\to X\) with \(p_Nq=p\), and \(x_N=q(\tilde x_0)\).

1. \(p_N\) and \(q\) are coverings, so \(q\) is a universal covering of the path-connected space \(X_N\), and \((p_N)_*\) maps \(\pi_1(X_N,x_N)\) isomorphically onto \(N\).
2. \(X_N\) is a cell complex whose cells are the lifts of the cells of \(X\) through \(p_N\); \(q\) maps the lifts through \(p\) onto them, and two lifts through \(p\) have the same image exactly when they lie in one orbit of \(N\).
3. If \(N\) is normal, then \(G/N\) acts on \(X_N\) by the deck transformations \(\bar L_{gN}\) with \(\bar L_{gN}q=qL_g\), freely, transitively on every fibre of \(p_N\), and freely and transitively on the lifts of every cell.
4. A map \(f\colon F\to X\) from a path-connected, locally path-connected space, for instance a connected cell complex, with \(f(y_0)=x_0\), lifts to a map \(F\to X_N\) with \(y_0\mapsto x_N\) exactly when \(f_*\pi_1(F,y_0)\subseteq N\).

*Proof.* 1. The action of \(N\) is a fibrewise action of a discrete group in the sense of [Algebraic Topology, Lecture 16, Definition 16.1], and \(X\) is semilocally simply connected (proof of Theorem 1.1); so \(p_N\) is a covering and \(q\) a covering map [Lecture 16, Proposition 16.1]. \(X_N=q(\widetilde X)\) is path-connected, \(\widetilde X\) is simply connected, \((p_N)_*\pi_1(X_N,x_N)=N\) by [Lecture 16, Corollary 16.1], and \((p_N)_*\) is injective [Lecture 9, Corollary 9.1].

2. This is [Grassmannians and classifying maps, Theorem 8.3](course:DG-CHAR/DG-CHAR-03) for the covering \(p_N\). For a lift \(\widetilde\Phi\) of \(\Phi_\alpha\) through \(p\), the map \(q\widetilde\Phi\) is a lift through \(p_N\). Two lifts through \(p\) with the same image under \(q\) take values in one \(N\)-orbit at \(0\), so one is the image of the other under some \(L_n\), \(n\in N\), by uniqueness of lifts; conversely \(qL_n=q\).

3. If \(q(z)=q(z')\), then \(z'=L_n(z)\) with \(n\in N\), and \(qL_gz'=qL_{gng^{-1}}L_gz=qL_gz\) since \(gng^{-1}\in N\); so \(\bar L_{gN}\) is well defined, and continuous because \(q\) is a covering map, hence open and a quotient map. It is a deck transformation with inverse \(\bar L_{g^{-1}N}\). The fibre of \(p_N\) over \(x\) is the set of \(N\)-orbits in \(p^{-1}(x)\), on which \(G/N\) acts transitively because \(G\) acts transitively on \(p^{-1}(x)\). If \(\bar L_{gN}\) fixes \(q(z)\), then \(L_g(z)=L_n(z)\) for some \(n\in N\), so \(g=n\) because \(G\) acts freely. The lifts of a cell through \(p_N\) correspond to the points of a fibre.

4. Proposition 2.1 with \(Z=X_N\) and part 1. \(\square\)

**Proposition 3.2.** Let \(p\colon Z\to X\) be a covering of a cell complex, with the cells of Theorem 1.1 or Proposition 3.1.

1. For every subcomplex \(A\) of \(X\), \(p^{-1}(A)\) is a subcomplex of \(Z\): the union of the lifts of the cells of \(A\).
2. If \(X\) is the realization of a simplicial complex \(M\), with the open simplices as cells, then \(Z\) is the realization of a simplicial complex \(\widetilde M\) whose vertices are the points over the vertices of \(M\) and whose simplices are the vertex sets of the lifts of the closed simplices; \(p\) maps every closed simplex of \(\widetilde M\) homeomorphically and affinely onto a closed simplex of \(M\).

*Proof.* 1. \(p^{-1}(A)\) is closed, and it is the union of the open cells of \(Z\) lying over open cells of \(A\).

2. A lift \(\tilde\sigma\) of a closed simplex \(|\sigma|\) is injective, since \(p\tilde\sigma\) is, and for a face \(\rho\) of \(\sigma\) its restriction is a lift of \(|\rho|\). Let two lifts \(\tilde\sigma,\tilde\tau\) of closed simplices meet in a point \(z\). Then \(p(z)\) lies in \(|\sigma|\cap|\tau|=|\rho|\) with \(\rho=\sigma\cap\tau\), so \(z\) lies on the restriction of \(\tilde\sigma\) to \(|\rho|\) and on the restriction of \(\tilde\tau\) to \(|\rho|\); these are lifts of \(|\rho|\) that agree at \(z\), hence equal by uniqueness of lifts. Every point of the intersection lies on this common lift, so the intersection of two lifted simplices is a common face. In particular a lifted simplex is determined by its vertices, which are distinct, and the vertex sets of lifted simplices form a simplicial complex \(\widetilde M\). The map from \(|\widetilde M|\) to \(Z\) that sends each closed simplex affinely onto its lift is a bijection; it is a homeomorphism, because in both spaces a set is closed exactly when it meets every closed simplex in a closed set. \(\square\)

## 4. Homotopy equivalences

**Proposition 4.1.** Let \(h\colon X\to Y\) be a homotopy equivalence of connected cell complexes, \(x_0\) a vertex of \(X\) and \(y_0=h(x_0)\). Then \(h_*\colon\pi_1(X,x_0)\to\pi_1(Y,y_0)\) is an isomorphism. For universal covers \(p\colon\widetilde X\to X\), \(p'\colon\widetilde Y\to Y\) and points \(\tilde x_0,\tilde y_0\) over \(x_0,y_0\), the lift \(\tilde h\colon\widetilde X\to\widetilde Y\) of \(hp\) with \(\tilde h(\tilde x_0)=\tilde y_0\) is a homotopy equivalence, and \(\tilde hL_g=L'_{h_*g}\tilde h\) for all \(g\in\pi_1(X,x_0)\).

*Proof.* \(h_*\) is an isomorphism by [Algebraic Topology, Lecture 18, Proposition 18.2]. The lift \(\tilde h\) exists by Corollary 2.3, since \(\widetilde X\) is a simply connected cell complex. Let \(k\) be a homotopy inverse of \(h\), \(\tilde k\) a lift of \(kp'\), and \(H\) a homotopy from \(kh\) to \(\mathrm{id}_X\). Lift the homotopy \(H\circ(p\times\mathrm{id}_I)\) starting at \(\tilde k\tilde h\), a lift of \(khp\) [Lecture 9, Corollary 9.4]. Its end is a lift of \(p\) through \(p\); it agrees at \(\tilde x_0\) with some \(L_g\), since \(G\) acts transitively on \(p^{-1}(x_0)\), and so it equals \(L_g\) by uniqueness of lifts. So \(L_g^{-1}\tilde k\) is a left homotopy inverse of \(\tilde h\). In the same way \(\tilde h\tilde k\simeq L'_{g'}\) for some \(g'\), and \(\tilde kL'^{-1}_{g'}\) is a right homotopy inverse. A map with a left homotopy inverse \(a\) and a right homotopy inverse \(b\) is a homotopy equivalence, because \(a\simeq a\tilde hb\simeq b\). For the equivariance, \(\tilde hL_g\) and \(L'_{h_*g}\tilde h\) are lifts of \(hp\). If \(\gamma\) represents \(g\) and \(\tilde\gamma\) is its lift from \(\tilde x_0\), then \(\tilde h\tilde\gamma\) is the lift of \(h\gamma\) from \(\tilde y_0\), which ends at \(\tilde y_0\cdot h_*g=L'_{h_*g}(\tilde y_0)\); so the two lifts agree at \(\tilde x_0\), and they are equal. \(\square\)

## 5. Cellular chains

For a cell complex \(X\), the *cellular chain complex* has \(C_n(X)=H_n(X^n,X^{n-1})\), with \(X^{-1}=\varnothing\), and the differential \(d_n=\rho_{n-1}\delta_n\), where \(\delta_n\colon H_n(X^n,X^{n-1})\to H_{n-1}(X^{n-1})\) is the connecting map and \(\rho_{n-1}\) is the map of pairs from \(H_{n-1}(X^{n-1})\) to \(H_{n-1}(X^{n-1},X^{n-2})\). Homology is singular homology with integer coefficients. We use from the core course [Algebraic Topology, Fomberg component 7]: the group \(C_n(X)\) is free abelian with one generator \((\Phi_\alpha)_*[D^n,\partial D^n]\) for each \(n\)-cell, given a choice of generator \([D^n,\partial D^n]\) of \(H_n(D^n,\partial D^n)\cong\mathbb Z\), an orientation of the cell; \(d_{n-1}d_n=0\); and the homology of \(C_*(X)\) is naturally isomorphic to \(H_*(X)\), for arbitrary cell complexes, naturally with respect to maps that send every skeleton into the corresponding skeleton (the cellular homology theorem, (14.1) and (14.2) there); and \(H_k(X^m)=0\) for \(k>m\) (the lemma on the homology of skeleta there). The proof of the incidence formula there, (15.3), shows that \(\delta_n\) maps the generator \((\Phi_\alpha)_*[D^n,\partial D^n]\) to \((\varphi_\alpha)_*\partial[D^n,\partial D^n]\), where \(\partial\colon H_n(D^n,\partial D^n)\to H_{n-1}(\partial D^n)\) is the connecting map of the pair.

**Lemma 5.1** (paths as chains). Regard paths as singular \(1\)-simplices. Let \(\gamma,\eta\) be paths with \(\gamma(1)=\eta(0)\).

1. \(\gamma*\eta-\gamma-\eta\) is a boundary.
2. If \(\gamma\) and \(\gamma'\) are homotopic, then \(\gamma-\gamma'\) is a boundary.
3. A constant \(1\)-simplex and \(\gamma+\bar\gamma\) are boundaries.

*Proof.* 1. Let \(\Delta^2\) have the vertices \(v_0,v_1,v_2\), and put \(\sigma=(\gamma*\eta)\circ\pi\) with the affine map \(\pi(t_0v_0+t_1v_1+t_2v_2)=\frac12t_1+t_2\). On the edges \([v_0,v_1]\), \([v_1,v_2]\), \([v_0,v_2]\), in their linear parametrizations, \(\sigma\) is \(\gamma\), \(\eta\) and \(\gamma*\eta\), so \(\partial\sigma=\eta-\gamma*\eta+\gamma\).

2. Let \(K\colon I\times I\to X\) be a homotopy with \(K(t,0)=\gamma(t)\), \(K(t,1)=\gamma'(t)\) and \(K(0,s)\), \(K(1,s)\) constant, and let \(\delta(u)=K(u,u)\). The composites of \(K\) with the affine maps of \(\Delta^2\) onto the triangles with the vertices \((0,0),(1,0),(1,1)\) and \((0,0),(0,1),(1,1)\) have the boundaries \(c-\delta+\gamma\) and \(\gamma'-\delta+c'\), with constant simplices \(c,c'\). So \(\gamma-\gamma'\) is a boundary plus \(c'-c\).

3. The constant \(2\)-simplex at a point has as boundary the constant \(1\)-simplex there. By parts 1 and 2, \(\gamma+\bar\gamma\) differs by a boundary from \(\gamma*\bar\gamma\), which is homotopic to a constant path. \(\square\)

Orient every edge \(e\) by its characteristic map \(\Phi_e\colon I\to X\), so that its generator is the class of the singular simplex \(\Phi_e\), a relative cycle. The loop \(\omega(t)=(\cos2\pi t,\sin2\pi t)\) is a singular \(1\)-cycle of \(\partial D^2\), and its class generates \(H_1(\partial D^2)\cong\mathbb Z\): by [Frame fields and primary obstructions, Lemma E.1](course:DG-CHAR/DG-CHAR-08B), for a path-connected space the map sending the class of a loop to the class of the loop as a singular cycle is an isomorphism from the abelianized fundamental group onto \(H_1\), and the class of \(\omega\) generates \(\pi_1(\partial D^2)\). Orient every \(2\)-cell \(\alpha\) by the generator of \(H_2(D^2,\partial D^2)\) whose connecting image is the class of \(\omega\).

**Proposition 5.2** (cellular boundaries). Let \(X\) be a cell complex with these orientations.

1. The boundary of an edge \(e\) is \(\Phi_e(1)-\Phi_e(0)\).
2. If the \(2\)-cell \(\alpha\) is attached along the closed walk \((e_1^{\epsilon_1},\ldots,e_r^{\epsilon_r})\), with \(\epsilon_j=\pm1\), then
\[
d_2\alpha=\sum_{j=1}^r\epsilon_j\,e_j ;
\]
if it is attached along an empty walk, then \(d_2\alpha=0\).
3. Let \(n\ge1\), let \(Z\) be a cell complex of dimension at most \(n-1\), and let \(X\) be obtained from \(Z\) by attaching \(n\)-cells. The map \(\rho_{n-1}\colon H_{n-1}(Z)\to C_{n-1}(Z)\) is injective, with image the cycles of \(C_*(Z)\), and the boundary of an \(n\)-cell \(\alpha\) is the cycle \(\rho_{n-1}\bigl((\varphi_\alpha)_*\partial[D^n,\partial D^n]\bigr)\), which represents the image of the class of \(\partial D^n\) under the attaching map.

*Proof.* 1. The connecting map sends the class of the relative cycle \(\Phi_e\) to the class of its boundary \(\Phi_e(1)-\Phi_e(0)\) in \(H_0(X^0)=C_0(X)\).

2. By (15.3) of [Algebraic Topology, Fomberg component 7] and the choice of orientation, \(\delta_2\alpha\) is the class of the singular cycle \(\varphi_\alpha\circ\omega=|c|\) in \(H_1(X^1)\). By [Fundamental groups of graphs and two-complexes, Lemma 2.1](fundamental-groups-of-graphs-and-two-complexes.md), \(|c|\) is homotopic to the iterated concatenation of the paths of its darts, and by Lemma 5.1 it differs by a boundary from the sum of these paths; the path of \(e^+\) is \(\Phi_e\), and the path of \(e^-\) is \(\bar\Phi_e\), which differs from \(-\Phi_e\) by a boundary. Applying \(\rho_1\) gives the formula. For an empty walk, \(\varphi_\alpha\circ\omega\) is constant, a boundary by Lemma 5.1.

3. Here \(X^{n-1}=Z\). By (15.3) there, \(\delta_n\alpha=(\varphi_\alpha)_*\partial[D^n,\partial D^n]\) in \(H_{n-1}(Z)\). In the exact sequence of the pair \((Z,Z^{n-2})\), the group \(H_{n-1}(Z^{n-2})\) vanishes, so \(\rho_{n-1}\) is injective with image the kernel of the connecting map \(\delta_{n-1}\). Since \(\rho_{n-2}\) is injective for the same reason, this kernel is the kernel of \(d_{n-1}=\rho_{n-2}\delta_{n-1}\), the group of cycles. \(\square\)

**Proposition 5.3** (chains of covers). Let \(X\) be a connected cell complex, \(G=\pi_1(X,x_0)\), and \(p\colon\widetilde X\to X\) the universal cover with the cells of Theorem 1.1, each lift \(\widetilde\Phi\) oriented by the orientation of the cell below it.

1. Every \(L_g\) maps each skeleton of \(\widetilde X\) onto itself, and the induced chain maps make \(C_*(\widetilde X)\) a complex of left \(\mathbb ZG\)-modules, with \(g\cdot\widetilde\Phi=L_g\widetilde\Phi\) on generators. Each \(C_n(\widetilde X)\) is a free \(\mathbb ZG\)-module with basis one chosen lift of each \(n\)-cell of \(X\), and \(d\) is \(\mathbb ZG\)-linear.
2. A lift of a \(2\)-cell attached along the closed walk \(c\) is attached along the lift of \(c\) from its initial vertex, a closed walk of \(\widetilde X^1\); its boundary is given by Proposition 5.2 in \(\widetilde X\), with the lifted darts in place of the darts of \(c\).
3. The augmentation \(\varepsilon\colon C_0(\widetilde X)\to\mathbb Z\), sending every vertex to \(1\), is \(\mathbb ZG\)-linear for the trivial action on \(\mathbb Z\); since \(\widetilde X\) is connected, the sequence \(C_1(\widetilde X)\to C_0(\widetilde X)\to\mathbb Z\to0\) is exact, and the kernel of \(\varepsilon\) is the image of \(d_1\).

The same holds for the covers \(X_N\) of Proposition 3.1 with \(G/N\) in place of \(G\).

*Proof.* 1. A deck transformation maps lifts of cells to lifts of cells of the same dimension, hence skeleta onto skeleta, and so induces maps of the pairs \((\widetilde X^n,\widetilde X^{n-1})\) commuting with the connecting maps and the maps of pairs, that is, chain maps. On generators, \((L_g)_*(\widetilde\Phi)_*[D,\partial D]=(L_g\widetilde\Phi)_*[D,\partial D]\), the generator of the lift \(L_g\widetilde\Phi\) with the same orientation. The generators of \(C_n(\widetilde X)\) are permuted freely by \(G\), with one orbit for each \(n\)-cell of \(X\) (Theorem 1.1), so \(C_n(\widetilde X)\) is free over \(\mathbb ZG\) on one generator from each orbit, and the chain maps are the \(\mathbb ZG\)-linearity of \(d\).

2. The attaching map of the lift \(\widetilde\Phi\) is \(\widetilde\Phi|_{\partial D^2}\), a lift of \(\varphi_\alpha\); so \(\widetilde\Phi\circ\omega\) lifts \(|c|\). By unique path lifting it is the concatenation of the lifts of the paths of the darts of \(c\), and the lift of \(\Phi_e\) is the characteristic map of a lifted edge; so it is the path of a closed walk of lifted darts.

3. Vertices go to vertices under \(L_g\). The cellular homology theorem identifies \(C_0/\operatorname{im}d_1\) with \(H_0(\widetilde X)\), which is \(\mathbb Z\) for a path-connected space, the class of every vertex being the generator; so \(\varepsilon\) induces this isomorphism and \(\ker\varepsilon=\operatorname{im}d_1\). For \(X_N\) the same arguments apply with Proposition 3.1. \(\square\)

**Proposition 5.4** (subcomplexes). Let \(A\) be a connected subcomplex of a connected cell complex \(X\), \(a_0\) a vertex of \(A\), \(\iota\colon\pi_1(A,a_0)\to\pi_1(X,a_0)\) the map induced by the inclusion, and \(p_A\colon\widetilde A\to A\), \(p\colon\widetilde X\to X\) universal covers with points \(\tilde a_0,\tilde x_0\) over \(a_0\).

1. There is exactly one map \(\psi\colon\widetilde A\to\widetilde X\) with \(p\psi=p_A\) and \(\psi(\tilde a_0)=\tilde x_0\). It satisfies \(\psi L^A_h=L_{\iota(h)}\psi\) for all \(h\in\pi_1(A,a_0)\), and for every lift \(\widetilde\Phi\) of a cell of \(A\), the map \(\psi\widetilde\Phi\) is a lift of the same cell to \(\widetilde X\).
2. \(\psi\) induces a chain map \(\psi_*\colon C_*(\widetilde A)\to C_*(\widetilde X)\) with \(\psi_*(hc)=\iota(h)\psi_*(c)\), sending the generator of \(\widetilde\Phi\) to the generator of \(\psi\widetilde\Phi\). Hence, if \(d\widetilde\Phi_\alpha=\sum_\beta\lambda^A_{\alpha\beta}\widetilde\Phi_\beta\) in \(C_*(\widetilde A)\), with \(\lambda^A_{\alpha\beta}\in\mathbb Z\pi_1(A,a_0)\), then \(d(\psi\widetilde\Phi_\alpha)=\sum_\beta\iota(\lambda^A_{\alpha\beta})\,\psi\widetilde\Phi_\beta\) in \(C_*(\widetilde X)\).

*Proof.* 1. The space \(\widetilde A\) is a simply connected cell complex, so \(\psi\) exists and is unique by Corollary 2.3, applied to \(p_A\) followed by the inclusion of \(A\) in \(X\). The maps \(\psi L^A_h\) and \(L_{\iota(h)}\psi\) are lifts of the same map. If \(\gamma\) is a loop in \(A\) representing \(h\) and \(\tilde\gamma\) its lift from \(\tilde a_0\), then \(\psi\tilde\gamma\) is the lift of \(\gamma\) from \(\tilde x_0\), which ends at \(\tilde x_0\cdot\iota(h)\); so both lifts take the value \(L_{\iota(h)}(\tilde x_0)\) at \(\tilde a_0\), and they are equal. Finally \(p\psi\widetilde\Phi=p_A\widetilde\Phi\) is the characteristic map of the cell.

2. By part 1 and Theorem 1.1, \(\psi\) maps each skeleton of \(\widetilde A\) into the corresponding skeleton of \(\widetilde X\), so it induces a chain map of cellular chains; on generators it is \(\psi_*(\widetilde\Phi)_*[D,\partial D]=(\psi\widetilde\Phi)_*[D,\partial D]\). The equivariance follows from part 1, and the formula for \(d(\psi\widetilde\Phi_\alpha)\) is \(\psi_*\) applied to \(d\widetilde\Phi_\alpha\). \(\square\)

In particular, if \(\widetilde X\) is contractible, then all its reduced homology groups vanish, by the homotopy invariance of singular homology [Algebraic Topology, Fomberg, Theorem 1.13 and Corollary 1.14], and the augmented complex \(\cdots\to C_1(\widetilde X)\to C_0(\widetilde X)\to\mathbb Z\to0\) is a free resolution of \(\mathbb Z\) over \(\mathbb ZG\). The degree-one part of [Frame fields and primary obstructions, Lemma E.1](course:DG-CHAR/DG-CHAR-08B) gives \(H_1(X)\cong\pi_1(X,x_0)^{\mathrm{ab}}\) for every connected cell complex \(X\).

## 6. The Cayley complex of a presentation

Let \(G=\langle A\mid R\rangle\), let \(K=K(A,R)\) be the presentation complex, and identify \(\pi_1(K,o)\) with \(G\) by [Fundamental groups of graphs and two-complexes, Corollary 4.2](fundamental-groups-of-graphs-and-two-complexes.md), so that \(a\in A\) corresponds to the class of the loop \(\Phi_{\ell_a}\). For a word \(w\), let \(\overline w\) be its image in \(G\).

**Proposition 6.1** (the Cayley complex). Let \(p\colon\widetilde K\to K\) be the universal cover and \(\tilde o\) a point over \(o\). Identify the vertex \(\tilde o\cdot g=L_g(\tilde o)\) with \(g\in G\).

1. The lift of the loop \(\ell_a\) from the vertex \(g\) ends at \(g\,\overline a\); so \(\widetilde K^1\) is the Cayley graph of \(G\) with respect to \(A\) as in [Words, free groups and Cayley graphs, Definition 4.1](course:van-kampen-diagrams/words-free-groups-and-cayley-graphs), with the edge \(g\tilde e_a\) from \(g\) to \(g\overline a\), and \(L_h\) acts on vertices by \(g\mapsto hg\).
2. For each \(g\in G\) and \(r\in R\) there is exactly one lift of the cell of \(r\) whose initial vertex is \(g\); it is attached along the closed walk from \(g\) whose label is \(r\).
3. Let \(\tilde v=1\), \(\tilde e_a\) the edge from \(1\) to \(\overline a\), and \(\tilde c_r\) the lift of the cell of \(r\) at \(1\). For \(r=a_1^{\epsilon_1}\cdots a_k^{\epsilon_k}\) and \(g_j=\overline{a_1^{\epsilon_1}\cdots a_j^{\epsilon_j}}\),
\[
\begin{gathered}
d_1\tilde e_a=(\overline a-1)\,\tilde v,\\
d_2\tilde c_r=\sum_{\epsilon_j=1}g_{j-1}\tilde e_{a_j}-\sum_{\epsilon_j=-1}g_j\tilde e_{a_j}.
\end{gathered}
\]
4. The sequence of left \(\mathbb ZG\)-modules
\[
\mathbb ZG^{(R)}\xrightarrow{d_2}\mathbb ZG^{(A)}\xrightarrow{d_1}\mathbb ZG\xrightarrow{\varepsilon}\mathbb Z\to0
\]
is exact, and the kernel of \(d_2\) is \(H_2(\widetilde K)\), which is isomorphic to \(\pi_2(K,o)\).

*Proof.* 1. The lift of \(\Phi_{\ell_a}\) from \(\tilde o\cdot g\) ends at \(\tilde o\cdot g\overline a\), by the definition of the right action; it is the characteristic map of a lifted edge (Theorem 1.1). \(L_h(\tilde o\cdot g)=L_hL_g(\tilde o)=\tilde o\cdot hg\). The edges of \(\widetilde K\) are the lifts of the loops, one for each pair \((g,a)\), which is the description of the Cayley graph.

2. A lift of the characteristic map of the cell of \(r\) is determined by its value at the boundary point \(\omega(0)\), which lies over \(o\), and every value over \(o\) occurs, by Corollary 2.3; so the lifts correspond to the vertices of \(\widetilde K\). By Proposition 5.3 the lift with initial vertex \(g\) is attached along the lift from \(g\) of the walk reading \(r\), which is the walk from \(g\) with label \(r\) in the Cayley graph [Words, free groups and Cayley graphs, Lemma 4.2](course:van-kampen-diagrams/words-free-groups-and-cayley-graphs). It is closed because \(\overline r=1\).

3. By Proposition 5.2, \(d_1\tilde e_a=\overline a\,\tilde v-\tilde v\). The walk from \(1\) reading \(r\) passes through the vertices \(g_0=1,g_1,\ldots,g_k=1\). Its \(j\)-th dart is the edge \(g_{j-1}\tilde e_{a_j}\), traversed forwards, if \(\epsilon_j=1\), and the edge \(g_j\tilde e_{a_j}\), from \(g_j\) to \(g_j\overline{a_j}=g_{j-1}\), traversed backwards, if \(\epsilon_j=-1\). Proposition 5.2 gives the formula.

4. The exactness at \(\mathbb ZG\) and \(\mathbb Z\) is Proposition 5.3. Exactness at \(\mathbb ZG^{(A)}\) means \(H_1(\widetilde K)=0\), which holds because \(\widetilde K\) is simply connected and \(H_1\) is the abelianized fundamental group. Since \(\widetilde K\) has no cells of dimension three, \(H_2(\widetilde K)=\ker d_2\). By the Hurewicz theorem [Frame fields and primary obstructions, Lemma E.1](course:DG-CHAR/DG-CHAR-08B) for the simply connected space \(\widetilde K\), \(\pi_2(\widetilde K)\cong H_2(\widetilde K)\), and \(\pi_2(\widetilde K)\cong\pi_2(K)\) by Theorem 1.1. \(\square\)

The coefficient of \(\tilde e_a\) in \(d_2\tilde c_r\) is the *Fox derivative* \(\partial r/\partial a\), mapped to \(\mathbb ZG\).

## 7. Exercises

**7.1.** Let \(K=K(\{a\},\varnothing)\), a circle. Describe \(\widetilde K\), the action of \(G\cong\mathbb Z\), and the complex \(C_*(\widetilde K)\) over \(\mathbb ZG=\mathbb Z[a,a^{-1}]\).

**7.2.** For \(G=\langle a,b\mid aba^{-1}b^{-1}\rangle\), compute \(d_2\tilde c_r\) and show that \(\ker d_2=0\).

**7.3.** For \(G=\langle a\mid a^n\rangle\), \(n\ge2\), show that \(d_2\tilde c_r=(1+a+\cdots+a^{n-1})\tilde e_a\) and that \(\pi_2(K)\) is free abelian of rank \(n-1\).

**7.4.** Show that the map \(\partial D^2\to\partial D^2\), \(\omega(t)\mapsto\omega(2t)\), lifts through the covering \(\omega(t)\mapsto\omega(2t)\) and does not lift through \(\omega(t)\mapsto\omega(3t)\).

**7.5.** Let \(X\) be a connected cell complex with universal cover \(\widetilde X\) and \(G=\pi_1(X)\). Show that the complex \(\mathbb Z\otimes_{\mathbb ZG}C_*(\widetilde X)\) is isomorphic to \(C_*(X)\), so that its homology is \(H_*(X)\).

## 8. Solutions

**7.1.** \(\widetilde K\) is the real line with the vertices \(a^m\), \(m\in\mathbb Z\), and the edges from \(a^m\) to \(a^{m+1}\); \(L_{a^k}\) translates by \(k\). There are no \(2\)-cells; \(C_1=C_0=\mathbb ZG\), with \(d_1\tilde e_a=(a-1)\tilde v\), and \(0\to\mathbb ZG\xrightarrow{a-1}\mathbb ZG\to\mathbb Z\to0\) is exact.

**7.2.** For \(r=aba^{-1}b^{-1}\): \(g_0=1\), \(g_1=a\), \(g_2=ab\), \(g_3=aba^{-1}=b\), \(g_4=1\). The forward darts contribute \(\tilde e_a+a\tilde e_b\), the backward darts \(-b\tilde e_a-\tilde e_b\), so \(d_2\tilde c_r=(1-b)\tilde e_a+(a-1)\tilde e_b\). Since \(\mathbb ZG=\mathbb Z[a^{\pm1},b^{\pm1}]\) is a domain and \(a-1\ne0\), \(x\mapsto x\,d_2\tilde c_r\) is injective, so \(\ker d_2=0\).

**7.3.** For \(r=a^n\) all darts are forward, with \(g_{j-1}=a^{j-1}\), so \(d_2\tilde c_r=(1+a+\cdots+a^{n-1})\tilde e_a\). An element \(x=\sum_ix_ia^i\) of \(\mathbb ZG\) satisfies \(x(1+\cdots+a^{n-1})=0\) exactly when \(\sum_ix_i=0\), so \(\ker d_2\) is the augmentation ideal, free abelian with basis \(a^i-1\), \(1\le i\le n-1\). By Proposition 6.1, \(\pi_2(K)\cong\ker d_2\).

**7.4.** Let \(f(\omega(t))=\omega(2t)\). With base points \(\omega(0)\), \(f_*\) maps \(\pi_1\cong\mathbb Z\) onto \(2\mathbb Z\), the image of the covering \(\omega(t)\mapsto\omega(2t)\), and \(2\mathbb Z\not\subseteq3\mathbb Z\), the image of \(\omega(t)\mapsto\omega(3t)\). Proposition 2.1 applies.

**7.5.** Write \(C=C_*(\widetilde X)\). By Proposition 5.3, \(\mathbb Z\otimes_{\mathbb ZG}C_n\) is free abelian with one generator for each \(n\)-cell of \(X\), the image of any of its lifts. The covering \(p\) maps skeleta into skeleta, so it induces a chain map \(C\to C_*(X)\), which sends the generator of a lift to the generator of the cell below it. Since \(pL_g=p\), this chain map factors through \(\mathbb Z\otimes_{\mathbb ZG}C\), and the factored map sends a basis to a basis. So it is an isomorphism of complexes, and the homology is \(H_*(X)\) by the cellular homology theorem.

## References

- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Section 1.3 (covering spaces, the lifting criterion, Propositions 1.33, 1.34 and 1.39, Cayley complexes), Section 2.2 (cellular homology and the cellular boundary formula) and Section 4.1 (Proposition 4.1), on the author's page. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
