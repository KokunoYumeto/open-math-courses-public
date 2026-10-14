# Thin diagrams and hyperbolicity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The strict angle excess at the original vertices of \(K\) makes reduced diagrams uniformly thin. Angular Gauss–Bonnet bounds the number of vertices mapping to original vertices inside a simple geodesic polygon of a reduced diagram; since every triangle of the barycentric subdivision has such a corner, no point of the polygon is far from its boundary, and a level arc turns this into thinness of geodesic triangles (Lemma 1.1). A form of the classical stability lemma compares paths whose subarcs are not much longer than the distance of their endpoints with shortest paths (Lemma 2.1). Expanding the sides of a triangle in a Cayley graph into loops of \(K\) and filling the result by a reduced diagram then shows that \(\pi_1(K)\) is word-hyperbolic (Proposition 3.2). This is part 3 of the triangle complex criterion, Theorem 2.1 of [Triangle complexes and their links](triangle-complexes-and-their-links.md).

- Thin reduced diagrams (Lemma 1.1).
- Stability of paths with controlled subarcs (Lemma 2.1).
- Edge paths in diagrams and word-hyperbolicity (Lemma 3.1, Proposition 3.2).

The lesson follows [OpenAI-RF, Section 4]. It uses the facts on polygons of [Polygons and plane graphs](polygons-and-plane-graphs.md), the reduced fillings of [Reduced planar fillings](reduced-planar-fillings.md) and the angle estimates of [Angular curvature, closed paths and torsion](angular-curvature-closed-paths-and-torsion.md). Throughout, \(K\) is a connected finite Euclidean triangle complex satisfying the hypothesis of the criterion with \(\eta>0\), and \(S\) is its barycentric subdivision. A triangle of \(S\) corresponds to a chain of a vertex, an edge and a triangle of \(K\), so exactly one of its corners is an original vertex of \(K\).

## 1. Thin reduced diagrams

Let \(\Delta\) be a reduced diagram, in the sense of Section 2 of the previous lesson, with its diagram map to \(S\). Its intrinsic metric \(d_\Delta\) is defined as in Section 4 of the first lesson, and Lemma 4.1 there, whose proof applies to such finite complexes, shows that \(\Delta\) is a compact geodesic metric space and that local geodesics consist of finitely many straight pieces in cells. All distances in this section are measured by \(d_\Delta\) in the whole diagram. By Lemma 2.1 of the previous lesson, the angle sum \(\theta_y\) at an interior vertex \(y\) is at least \(2\pi\), and at least \(2\pi+\eta\) if \(y\) maps to an original vertex of \(K\).

*Diagrams in the plane.* We identify the cells of \(\Delta\) with their images piecewise linearly, that is, linearly on the pieces of a subdivision into convex polygons; compositions of such maps are again piecewise linear. Each edge, a polygonal arc, is parametrized in this way by its image segment. A triangle of \(\Delta\) is a bounded face whose frontier is the simple polygon formed by its three edges; it is open and connected, and its closure adds only points of that polygon, so it is a component of the complement of the polygon, namely its inside. By Theorem 2.4 of [Polygons and plane graphs](polygons-and-plane-graphs.md), its closure is mapped piecewise linearly onto a convex polygon, and coning from interior points, as in Lemma 2.3 there, extends the parametrization of the three edges to a piecewise linear homeomorphism from the image triangle onto the closed triangle of \(\Delta\). A path made of finitely many straight pieces in cells of \(\Delta\) is then a polygonal path in the plane.

**Lemma 1.1** (thin diagrams; [OpenAI-RF, Lemma 4.1]). Choose \(M>0\) larger than the diameter of every triangle of \(S\), and put
\[
A=M+\frac{2\pi M}\eta,\qquad\delta=10(A+1).
\]
Every geodesic triangle in every reduced diagram is \(\delta\)-thin.

*Proof.* Let \(p\) be a point of one side \(\sigma_1\) of a geodesic triangle in \(\Delta\), and let \(U\) be the union of the other two sides \(\sigma_2\) and \(\sigma_3\). If \(p\in U\) there is nothing to prove, so let \(p\notin U\).

*The polygon.* Shortest paths are injective. The parameters of \(\sigma_1\) mapped outside the compact set \(U\) form an open set; let \((s_a,s_b)\) be its component containing the parameter of \(p\). The endpoints of \(\sigma_1\) are corners of the triangle and lie in \(U\), so \(a=\sigma_1(s_a)\) and \(b=\sigma_1(s_b)\) lie in \(U\), and the arc \([a,b]\) of \(\sigma_1\) between them meets \(U\) only in \(a\) and \(b\). Join \(a\) to \(b\) in \(U\) by a simple path \(Q\) as follows. If \(\sigma_2\) or \(\sigma_3\) contains both points, let \(Q\) be its subarc between them. Otherwise, say, \(a\in\sigma_2\) and \(b\in\sigma_3\). Let \(c\) be the common corner of \(\sigma_2\) and \(\sigma_3\), follow \(\sigma_2\) from \(a\) towards \(c\) up to its first point \(w\) on the subarc of \(\sigma_3\) from \(b\) to \(c\), and let \(Q\) consist of the subarc of \(\sigma_2\) from \(a\) to \(w\) and the subarc of \(\sigma_3\) from \(w\) to \(b\); by the choice of \(w\) they meet only in \(w\). Then
\[
\Pi=[a,b]\cup Q
\]
is a simple closed curve made of at most three subarcs of shortest paths, with *corners* \(a\), \(b\) and possibly \(w\). It consists of finitely many straight pieces, so it is a simple polygon in the plane. The complement of \(\Delta\) in the plane is its unbounded face, which is connected, unbounded and disjoint from \(\Pi\), hence outside \(\Pi\). So the closure \(\Omega\) of the inside of \(\Pi\) lies in \(\Delta\).

*Triangulating the disk.* If \(\Pi\) lies in one closed triangle \(\tau\) of \(\Delta\), then so does \(\Omega\), since the outside of \(\tau\) is connected, unbounded and disjoint from \(\Pi\); triangulate \(\Omega\) by diagonals of \(\Pi\) (Theorem 2.4 of [Polygons and plane graphs](polygons-and-plane-graphs.md)). Otherwise, in each closed triangle \(\tau\) the set \(\Pi\cap\tau\) consists of finitely many segments and points, and each component of \(\Pi\) minus \(\partial\tau\) inside \(\tau\) is an open polygonal arc ending at two distinct points of \(\partial\tau\), since \(\Pi\) does not lie in \(\tau\). Mark as vertices the corners of \(\tau\), the endpoints of the segments of \(\Pi\cap\tau\) and its isolated points. On an edge of \(\Delta\) these are the endpoints of the edge and the points where \(\Pi\) meets it in an isolated point, starts or stops running along it, or bends; so the two triangles at an edge mark the same points on it. Add the arcs of \(\Pi\) inside \(\tau\) to \(\partial\tau\) one at a time: each runs through one face of what has been drawn, which by induction is the inside of a simple polygon, and is a cross-cut of that polygon. By Lemma 2.2 of [Polygons and plane graphs](polygons-and-plane-graphs.md), \(\tau\) is cut into closures of insides of simple polygons, which we triangulate by diagonals (Theorem 2.4 there). Diagonals add no vertices, so the triangulations of adjacent triangles fit together along common edges.

In both cases the triangles inside \(\Pi\), with their edges and vertices, form a planar diagram \(\Omega'\) whose triangles carry the Euclidean metrics of the triangles of \(\Delta\) containing them. Its underlying set is \(\Omega\): a point inside \(\Pi\) has a neighbourhood in \(\Delta\), which is not contained in the finitely many edges, so the point lies in a closed triangle of \(\Delta\), hence in a triangle of \(\Omega'\). The unbounded face of \(\Omega'\) is the outside of \(\Pi\), so its exterior walk runs once around \(\Pi\): \(n_y=1\) for the vertices \(y\) on \(\Pi\) and \(n_y=0\) for those inside. The vertices inside \(\Pi\) are vertices of \(\Delta\), and their angle sums in \(\Omega'\) and in \(\Delta\) agree, since near such a vertex all its triangles in \(\Delta\) lie inside \(\Pi\) and are subdivided.

*Few original vertices inside.* Let \(n\) be the number of vertices of \(\Delta\) inside \(\Pi\) that map to original vertices of \(K\). A vertex \(y\) of \(\Delta\) inside \(\Pi\) has a neighbourhood in the plane inside \(\Pi\), hence in \(\Delta\); so no sector at \(y\) lies in the unbounded face of \(\Delta\), \(y\) is an interior vertex of \(\Delta\), and \(\theta_y\ge2\pi\), with \(\theta_y\ge2\pi+\eta\) for the \(n\) counted vertices. At a vertex \(y\) of \(\Omega'\) on \(\Pi\) other than a corner, the triangles at \(y\) form a chain from one edge of \(\Pi\) at \(y\) to the other (Lemma 2.1 of the previous lesson, part 2), which unfolds isometrically into a planar sector of angle \(\theta_y\). If \(\theta_y<\pi\), the chord of this sector between the points at a small distance \(r\) from \(y\) on the two edges has length \(2r\sin(\theta_y/2)<2r\), and maps to a path in \(\Delta\) of the same length between two points of one shortest path at distance \(2r\), which is impossible. So \(\theta_y\ge\pi\) at these vertices. In the angular Gauss–Bonnet formula, Lemma 1.1 of the previous lesson, applied to \(\Omega'\), the summand \((2-n_y)\pi-\theta_y\) is therefore at most \(-\eta\) at the \(n\) counted vertices, at most \(0\) at the other vertices except the corners, and at most \(\pi\) at each of the at most three corners. Hence
\[
2\pi\le3\pi-n\eta,\qquad n\le\frac\pi\eta .
\]

*The inradius.* For \(x\in\Omega\) put \(f(x)=d_\Delta(x,\Pi)\); \(f\) is \(1\)-Lipschitz. A point \(x\) inside \(\Pi\) lies in a closed triangle of \(\Delta\); join it within this triangle by a straight segment to the corner that maps to an original vertex. The segment has length less than \(M\). If it meets \(\Pi\), then \(f(x)<M\). Otherwise it is a connected set off \(\Pi\) containing \(x\), so it stays inside \(\Pi\), and it ends at one of the \(n\) counted vertices. So every \(x\in\Omega\) with \(f(x)>M\) lies within distance \(M\) of one of these vertices \(v_1,\dots,v_n\), and then \(|f(x)-f(v_i)|<M\) for some \(i\). As \(f\) is continuous on the connected compact set \(\Omega\) and vanishes on \(\Pi\), its values form an interval \([0,F]\). If \(F>M\), the interval \((M,F]\) is covered by \(n\) intervals of length \(2M\), so \(F\le M+2Mn\). In all cases, for every \(x\in\Omega\),
\[
d_\Delta(x,\Pi)\le M+2Mn\le A .
\]

*A level arc.* Suppose that \(R=d_\Delta(p,Q)\) is larger than \(\delta\). Refine \(\Omega'\): add \(p\), \(a\) and \(b\) as vertices, joining each new vertex to the opposite corner of the triangle at its edge of \(\Pi\), and then halve all triangles repeatedly, cutting each into four by the midpoints of its sides, until every triangle has diameter less than \(1\). Let \(h\) be the function on \(\Omega\) that is linear on each triangle and equals \(d_\Delta(p,\cdot)\) at the vertices. A point \(x\) of a triangle with vertices \(u_1,u_2,u_3\) is a weighted mean of them with weights \(\mu_i\), and \(h(x)=\sum_i\mu_i\,d_\Delta(p,u_i)\); since \(|d_\Delta(p,u_i)-d_\Delta(p,x)|\le d_\Delta(u_i,x)<1\), we get
\[
|h(x)-d_\Delta(p,x)|<1\qquad(x\in\Omega).
\]
On \([a,b]\), a union of edges whose bends are vertices, \(d_\Delta(p,\cdot)\) is the arclength from \(p\), which is linear on each edge; so \(h=d_\Delta(p,\cdot)\) there. On \(Q\), \(h>R-1>2R/3\). Choose \(t\in(R/3,2R/3)\) different from the values of \(h\) at the vertices. Along each of the arcs from \(p\) to \(a\) and from \(p\) to \(b\), \(h\) increases strictly from \(0\) to at least \(R\), because \(a,b\in Q\). So the level set \(h^{-1}(t)\) meets \(\Pi\) in exactly two points, \(x_a\) between \(a\) and \(p\) and \(x_b\) between \(p\) and \(b\), neither of them a vertex.

In each triangle, \(h^{-1}(t)\) is empty or a segment joining interior points of two of its edges. An edge inside \(\Pi\) lies on two triangles of the refinement, and an edge on \(\Pi\) on one. So \(h^{-1}(t)\) is a finite graph whose vertices, its points on edges, have valence \(2\), except \(x_a\) and \(x_b\), which have valence \(1\). Its components are therefore closed curves and arcs, and \(x_a\), \(x_b\) are the two ends of one arc \(\gamma\subset\Omega\). For \(y\in\gamma\) we have \(|d_\Delta(p,y)-t|<1\), so
\[
\frac R3-1<d_\Delta(p,y)<\frac{2R}3+1,
\]
and \(d_\Delta(y,Q)\ge R-d_\Delta(p,y)\), which is larger than \(R/3-1>A\). By the inradius bound, a point \(z\) of \(\Pi\) nearest to \(y\) satisfies \(d_\Delta(y,z)\le A\), so \(z\) lies on \([a,b]\).

Along \(\gamma\), the function \(d_\Delta(a,\cdot)\) passes from \(d_\Delta(a,x_a)<d_\Delta(a,p)\) to \(d_\Delta(a,x_b)>d_\Delta(a,p)\). Choose \(y\in\gamma\) with \(d_\Delta(a,y)=d_\Delta(a,p)\), and \(z\in[a,b]\) as above. Since \([a,b]\) is a shortest path, distances along it are differences of distances from \(a\):
\[
\begin{aligned}
d_\Delta(z,p)&=|d_\Delta(a,z)-d_\Delta(a,y)|\\
&\le d_\Delta(z,y)\le A .
\end{aligned}
\]
Hence \(d_\Delta(p,y)\le2A\). But \(R>10(A+1)\) gives \(R/3-1>2A\), so \(d_\Delta(p,y)>2A\). This contradiction shows that \(d_\Delta(p,U)\le d_\Delta(p,Q)\le\delta\). \(\blacksquare\)

## 2. Stability of controlled paths

The *length* \(\operatorname{len}\) of a path is defined by partitions, as in Section 4 of the first lesson.

**Lemma 2.1** (stability; [OpenAI-RF, Lemma 4.2]). Let \(X\) be a geodesic metric space whose geodesic triangles are all \(\delta\)-thin, and let \(\lambda\ge1\) and \(C\ge0\). Put
\[
R_0=1+32\lambda\delta,
\]
\[
D=R_0+\lambda(2R_0+8\delta)+C .
\]
Let \(\sigma\) be a rectifiable path such that for all parameters \(u\le v\)
\[
\operatorname{len}(\sigma|_{[u,v]})\le\lambda\,d(\sigma(u),\sigma(v))+C,
\]
and let \(J\) be a shortest path with the same endpoints. Then every point of \(\sigma\) is within \(D\) of \(J\), and every point of \(J\) is within \(2D\) of \(\sigma\). Consequently, three such paths forming a closed triangle are \((3D+\delta)\)-thin: every point of each is within \(3D+\delta\) of the union of the other two.

*Proof.* *Projections.* Every point has a nearest point on the compact set \(J\). Let \(x\), \(y\) satisfy \(d(x,J)\ge R_0\), \(d(y,J)\ge R_0\) and \(d(x,y)\le R_0/2\), and let \(x'\), \(y'\) be nearest points on \(J\). We show \(d(x',y')\le8\delta\). Choose shortest paths \([x,x']\), \([x,y]\), \([y,y']\), \([x',y]\), and let \([x',y']\) be the subarc of \(J\). A point \(z\) of \([x',y']\) is within \(\delta\) of \([y,y']\cup[x',y]\), by the triangle \(x'y'y\), and a point of \([x',y]\) is within \(\delta\) of \([x,y]\cup[x,x']\), by the triangle \(x'yx\). So \(z\) is within \(2\delta\) of a point \(w\) of \([x,x']\cup[x,y]\cup[y,y']\). The point \(w\) cannot lie on \([x,y]\), since then
\[
R_0\le d(x,z)\le d(x,y)+2\delta\le\frac{R_0}2+2\delta,
\]
contrary to \(R_0>4\delta\). If \(w\in[x,x']\), then \(d(x,x')\le d(x,z)\le d(x,w)+2\delta\), because \(x'\) is nearest, while \(d(x,x')=d(x,w)+d(w,x')\), because \(w\) lies on a shortest path from \(x\) to \(x'\); so \(d(w,x')\le2\delta\) and \(d(z,x')\le4\delta\). Likewise, if \(w\in[y,y']\), then \(d(z,y')\le4\delta\). So every point of \([x',y']\) is within \(4\delta\) of \(x'\) or of \(y'\), and the midpoint gives \(d(x',y')\le8\delta\).

*Excursions.* The choice of \(R_0\) gives \(R_0>4\delta\) and \(16\lambda\delta/R_0<1/2\). The parameters at which \(\sigma\) is farther than \(R_0\) from \(J\) form an open set; on each of its components \((u_1,u_2)\), an *excursion*, the distance to \(J\) equals \(R_0\) at both ends, since the endpoints of \(\sigma\) lie on \(J\). Let \(H\) be the length of \(\sigma\) on \([u_1,u_2]\), and cut \([u_1,u_2]\) into \(k\le1+2H/R_0\) pieces on which \(\sigma\) has length at most \(R_0/2\). Consecutive cut points have distance at most \(R_0/2\) and distance at least \(R_0\) from \(J\). By the projection estimate, chosen nearest points of \(\sigma(u_1)\) and \(\sigma(u_2)\) are within \(8\delta k\) of each other, so
\[
d(\sigma(u_1),\sigma(u_2))\le2R_0+8\delta k .
\]
The hypothesis on \(\sigma|_{[u_1,u_2]}\) gives
\[
\begin{aligned}
H&\le\lambda(2R_0+8\delta)+C\\
&\quad+16\lambda\delta H/R_0 ,
\end{aligned}
\]
and since \(16\lambda\delta/R_0<1/2\), \(H\le2\lambda(2R_0+8\delta)+2C\). A point of \(\sigma\) on \([u_1,u_2]\) is within arclength \(H/2\) of \(\sigma(u_1)\) or \(\sigma(u_2)\), so its distance from \(J\) is at most \(R_0+H/2\le D\). The other points of \(\sigma\) are within \(R_0\) of \(J\).

*The reverse inclusion.* Let \(s\) be the common initial point of \(\sigma\) and \(J\), and \(q\in J\). As the parameter runs, \(d(s,\sigma(\cdot))\) passes continuously from \(0\) to the length of \(J\), so some point \(x\) of \(\sigma\) has \(d(s,x)=d(s,q)\). Let \(x'\) be a nearest point of \(J\) to \(x\); then \(d(x,x')\le D\). Distances along \(J\) are differences of distances from \(s\), so
\[
\begin{aligned}
d(q,x')&=|d(s,x)-d(s,x')|\\
&\le d(x,x')\le D,
\end{aligned}
\]
and \(d(q,x)\le2D\).

*Triangles.* Replace each of the three paths by a shortest path with the same endpoints. A point of one path is within \(D\) of its shortest path, whose points are within \(\delta\) of the other two shortest paths, whose points are within \(2D\) of the corresponding paths. \(\blacksquare\)

## 3. Word-hyperbolicity

Let \(\ell_*\) be the smallest edge length in \(S\), and \(\omega_*\) the smallest angle of a triangle of \(S\), or \(\pi\) if there is none. The *edge distance* of two vertices of a connected graph is the smallest number of edges of an edge path between them.

**Lemma 3.1** (edge paths in diagrams). For vertices \(u\), \(v\) of a planar diagram \(\Delta\) with a diagram map to \(S\), the edge distance of \(u\) and \(v\) is at most \(B_1\,d_\Delta(u,v)\), where
\[
B_1=\frac1{\ell_*\sin(\omega_*/2)} .
\]

*Proof.* Let \(\varepsilon>0\), and take a path from \(u\) to \(v\) made of finitely many straight segments in cells, of length less than \(d_\Delta(u,v)+\varepsilon\). Cut the segments at their intersections with the edges, so that each segment lies in an edge, or lies in a closed triangle and meets its boundary at most in its endpoints. A maximal run of consecutive segments of the second kind in one triangle \(\tau\), joined at points inside \(\tau\), starts and ends on \(\partial\tau\), since \(u\) and \(v\) are vertices; replace the run by the straight segment between its endpoints \(x\) and \(y\), which is at most as long. If \(x\) and \(y\) lie on a common side of \(\tau\), this segment lies in that side. Otherwise they lie on two sides meeting at a corner \(z\) at an angle \(\omega\ge\omega_*\); replace the segment by the route through \(z\). With \(a=|x-z|\) and \(b=|y-z|\), the law of cosines gives
\[
\begin{aligned}
&|x-y|^2-(a+b)^2\sin^2\tfrac\omega2\\
&\quad=\tfrac12(1+\cos\omega)(a-b)^2\ge0,
\end{aligned}
\]
so the route has length \(a+b\le|x-y|/\sin(\omega_*/2)\). Now the path consists of segments in edges and has length at most \((d_\Delta(u,v)+\varepsilon)/\sin(\omega_*/2)\). Between two consecutive visits to vertices it stays in one edge; either it returns to the vertex it left, and we delete this part, or it crosses the edge, with length at least \(\ell_*\). The crossings, in order, form an edge path from \(u\) to \(v\) with at most \(B_1(d_\Delta(u,v)+\varepsilon)\) edges. Since \(\varepsilon\) is arbitrary, the lemma follows. \(\blacksquare\)

**Proposition 3.2** (word-hyperbolicity; [OpenAI-RF, Proposition 4.3]). The group \(\pi_1(K)\) is word-hyperbolic.

*Proof.* *Generators.* Fix a vertex \(o\) of \(S\) and a spanning tree of the graph of \(S\), and let \(\rho_v\) be the tree path from \(o\) to a vertex \(v\). Write \(G=\pi_1(S,o)=\pi_1(K,o)\). For an oriented edge \(e\) from \(u\) to \(v\), let \(g_e\in G\) be the class of \(\rho_ue\rho_v^{-1}\); the reversed edge gives \(g_e^{-1}\). Inserting \(\rho_v^{-1}\rho_v\) at the intermediate vertices of an edge loop \(e_1\cdots e_r\) at \(o\) shows
\[
[e_1\cdots e_r]=g_{e_1}\cdots g_{e_r}.
\]
Every loop at \(o\) is homotopic to an edge loop (Lemma 2.1 of [Reduced planar fillings](reduced-planar-fillings.md)), so the nonidentity elements \(g_e\) form a finite symmetric generating set \(\Sigma\) of \(G\), and an edge loop at \(o\) with \(r\) edges represents an element of word length at most \(r\). If \(\Sigma\) is empty, \(G\) is trivial and hyperbolic. Otherwise choose for each \(s\in\Sigma\) an edge loop \(\kappa_s\) at \(o\) representing \(s\), and let \(B_2\) be the largest of their lengths. Let \(\delta\) be as in Lemma 1.1, put \(\lambda=\max\{1,B_1B_2\}\) and \(C=2\lambda B_2\), let \(D\) be as in Lemma 2.1, and put \(T=3D+\delta\).

*Expanded triangles.* Consider a geodesic triangle in \(\operatorname{Cay}(G,\Sigma)\) whose corners are group elements. Its sides are edge paths; reading their labels once around the triangle gives letters \(s_1,\dots,s_N\in\Sigma\) and group vertices \(h_0,\dots,h_N=h_0\) with \(h_j=h_{j-1}s_j\). If \(N=0\), the triangle is a point. Otherwise the concatenation \(c=\kappa_{s_1}\cdots\kappa_{s_N}\) is a nonempty edge loop at \(o\) representing \(s_1\cdots s_N=1\), and Theorem 2.3 of [Reduced planar fillings](reduced-planar-fillings.md) gives a reduced diagram \(\Delta\) whose exterior walk maps to \(c\). The \(j\)-th *mark* is the visit of the exterior walk at the end of \(\kappa_{s_j}\); its vertex \(u_j\) maps to \(o\), and \(h_j\) is its *group label*. Traversed at unit speed, the exterior walk splits at the marks of the three corners into paths \(\sigma_1\), \(\sigma_2\), \(\sigma_3\) in \(\Delta\), the expansions of the three sides; between consecutive marks it has length at most \(B_2\).

*Marks and word distance.* For any two marks,
\[
d_\Sigma(h_j,h_k)\le B_1\,d_\Delta(u_j,u_k).
\]
Indeed, let \(j<k\), and take an edge path \(\pi\) from \(u_j\) to \(u_k\) with at most \(B_1d_\Delta(u_j,u_k)\) edges (Lemma 3.1). With the part of the exterior walk from the \(j\)-th to the \(k\)-th mark it forms a closed edge walk in \(\Delta\), which is nullhomotopic in \(\Delta\) (Lemma 1.2 of [Reduced planar fillings](reduced-planar-fillings.md)). Its image in \(S\) is nullhomotopic, so the image of \(\pi\), an edge loop at \(o\), represents the same element as \(\kappa_{s_{j+1}}\cdots\kappa_{s_k}\), namely \(h_j^{-1}h_k\). Its word length is at most the number of edges of \(\pi\). In particular, marks at the same vertex of \(\Delta\) have the same group label.

*Controlled sides.* Between two marks on one side, the number of letters is the word distance of their labels, since the side is a shortest path in the Cayley graph. So the part of the expanded side between them has length at most \(B_2\,d_\Sigma(h_j,h_k)\le B_1B_2\,d_\Delta(u_j,u_k)\). For a subarc of \(\sigma_i\) from \(x\) to \(y\), let \(u\) be the last mark at or before \(x\) and \(v\) the first mark at or after \(y\). The parts from \(u\) to \(x\) and from \(y\) to \(v\) lie in single expanded letters, so \(d_\Delta(u,x)\le B_2\) and \(d_\Delta(y,v)\le B_2\), and
\[
\begin{aligned}
\operatorname{len}(x\text{ to }y)&\le\lambda\,d_\Delta(u,v)\\
&\le\lambda\,d_\Delta(x,y)+C .
\end{aligned}
\]
The geodesic triangles of \(\Delta\) are \(\delta\)-thin by Lemma 1.1, so Lemma 2.1, applied in \(X=\Delta\), shows that every point of each \(\sigma_i\) is within \(T\) of the union of the other two.

*Triangles with corners at group elements.* Let \(h_j\) be a group vertex on one side. Its mark on the corresponding path \(\sigma_i\) is within \(T\) of a point of another path \(\sigma_{i'}\), hence within \(T+B_2\) of a mark \(u_k\) on \(\sigma_{i'}\), whose label \(h_k\) is a group vertex on the corresponding other side. By the mark inequality, \(d_\Sigma(h_j,h_k)\le B_1(T+B_2)\). Every point of a side is within \(1/2\) of a group vertex of that side. So geodesic triangles with corners at group elements are \(H\)-thin, where
\[
H=B_1(T+B_2)+1 .
\]

*Arbitrary triangles.* A geodesic polygon with \(m\ge3\) sides and corners \(p_1,\dots,p_m\) at group elements is \((m-2)H\)-thin, also with constant sides or repeated corners. After relabelling, consider a point on the side from \(p_m\) to \(p_1\); draw shortest paths from \(p_1\) to \(p_{m-1},\dots,p_3\), and apply \(H\)-thinness to the triangles \(p_1p_{m-1}p_m\), \(p_1p_{m-2}p_{m-1}\), and so on: each step reaches a side of the polygon or the next diagonal, and the last triangle \(p_1p_2p_3\) has only polygon sides besides its diagonal.

Now let a geodesic triangle have arbitrary corners \(x_1\), \(x_2\), \(x_3\) and sides \(\gamma_1\), \(\gamma_2\), \(\gamma_3\), with \(\gamma_i\) from \(x_i\) to \(x_{i+1}\), indices modulo \(3\). On each side keep the part \(\gamma_i'\) between its first and last group vertex; if \(\gamma_i\) contains no group vertex, it lies in one edge, and \(\gamma_i'\) is the constant path at an endpoint of that edge. Each \(\gamma_i'\) lies within \(1\) of \(\gamma_i\), and the parts of \(\gamma_i\) outside \(\gamma_i'\) lie within \(1\) of \(x_i\) or \(x_{i+1}\). The end of \(\gamma_i'\) and the start of \(\gamma_{i+1}'\) are within \(1\) of \(x_{i+1}\), hence at distance at most \(2\); join them by a shortest path \(\beta_{i+1}\). The six paths \(\gamma_1',\beta_2,\gamma_2',\beta_3,\gamma_3',\beta_1\) form a geodesic hexagon with corners at group elements, which is \(4H\)-thin.

Consider a point of \(\gamma_1\). If it lies outside \(\gamma_1'\), it is within \(1\) of \(x_1\in\gamma_3\) or of \(x_2\in\gamma_2\). If it lies on \(\gamma_1'\), it is within \(4H\) of a point \(z\) of another side of the hexagon. If \(z\) lies on \(\gamma_2'\) or \(\gamma_3'\), it is within \(1\) of \(\gamma_2\) or \(\gamma_3\). If \(z\) lies on \(\beta_{i+1}\), a path of length at most \(2\), it is within \(1\) of an endpoint and so within \(2\) of the corner \(x_{i+1}\), and each corner lies on \(\gamma_2\) or \(\gamma_3\). Hence every geodesic triangle in \(\operatorname{Cay}(G,\Sigma)\) is \((4H+2)\)-thin, and \(G\) is word-hyperbolic. \(\blacksquare\)

Together with Propositions 2.2 and 3.1 of [Angular curvature, closed paths and torsion](angular-curvature-closed-paths-and-torsion.md), this proves the triangle complex criterion, Theorem 2.1 of the first lesson.

## 4. Exercises

**4.1.** In the Euclidean plane, show that the midpoint of one side of an equilateral triangle with side length \(L\) has distance \(\sqrt3L/4\) from the union of the other two sides. Which estimate in the proof of Lemma 1.1 needs \(\eta>0\)?

**4.2.** Show that the factor \(1/\sin(\omega/2)\) in the proof of Lemma 3.1 cannot be improved.

**4.3.** Show that two shortest paths with the same endpoints in a reduced diagram lie within \(\delta\) of each other.

**4.4.** Let \(X\) be a geodesic metric space whose geodesic triangles are \(\delta\)-thin. Show that every geodesic quadrilateral in \(X\) is \(2\delta\)-thin.

**4.5.** In the proof of Proposition 3.2, show that two different marks on one side of the Cayley triangle are never at the same vertex of \(\Delta\).

## 5. Solutions

**4.1.** Let the side be \([x_1,x_2]\) with midpoint \(m\). The nearest point of the side \([x_2,x_3]\) to \(m\) is the foot of the perpendicular, at distance \(\frac L2\sin\frac\pi3=\sqrt3L/4\), and by symmetry the same holds for \([x_3,x_1]\). As \(L\) grows, the plane has no uniform thinness constant. In the proof of Lemma 1.1, the bound \(n\le\pi/\eta\) on the vertices with excess inside the polygon, and with it the inradius bound, needs \(\eta>0\).

**4.2.** For \(a=b\) the identity in the proof gives \(|x-y|=2a\sin(\omega/2)\), while the route through \(z\) has length \(2a\).

**4.3.** The two paths and the constant path at their common endpoint \(y\) form a geodesic triangle. By Lemma 1.1, each point of one path is within \(\delta\) of the other path or of \(y\), which lies on the other path.

**4.4.** Draw a diagonal. A point of a side lies on one of the two triangles and is within \(\delta\) of another side of the quadrilateral or of a point of the diagonal; that point is within \(\delta\) of the two sides of the other triangle.

**4.5.** Two marks on one side have labels \(h_j\ne h_k\), since the side is a shortest path; so \(d_\Sigma(h_j,h_k)\ge1\), and the mark inequality gives \(d_\Delta(u_j,u_k)>0\).

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
