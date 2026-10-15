# The level complex and its acyclicity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(L\) be a finite flag complex with vertex set \(V\), \(P=A_L\) its right-angled Artin group, \(\lambda\colon P\to\mathbb Z\) the height homomorphism with \(\lambda(a_q)=1\), and \(G=\ker\lambda\). The height extends affinely over the cube complex \(E\) of [The cube complex and its universal cover](the-cube-complex-and-its-universal-cover.md), and \(G\) acts on its zero level \(X=\lambda^{-1}(0)\). Bestvina and Brady showed that the levels have the homology of a point when \(L\) is acyclic; Davis's book explains their method [Davis, Section 11.6]. This lesson proves this for the zero level, describes \(X\) as a two-dimensional simplicial complex when \(L\) has dimension two, and reads off a finite alphabet \(S\) and a finite list \(\mathcal D\) of words whose chains form a basis of the cycle module, the input of the comparison theorem [OpenAI-EG, Section 4.3 and Proposition 4.5].

- The chain triangulation and heights (Section 1).
- Ascending and descending links (Section 2).
- The half spaces (Section 3).
- The level (Section 4).
- The group and its cycle basis (Section 5).

We use: from [The cube complex and its universal cover](the-cube-complex-and-its-universal-cover.md), Lemmas 2.1 and 2.2 (the cubes \(\chi_{g,\sigma}\) of \(E\)), Theorem 4.2 and Corollary 5.1; from [Right-angled Artin groups and residual finiteness](right-angled-artin-groups-and-residual-finiteness.md), Theorem 4.1; from [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md), Corollary 3.3 and the remark after Lemma 2.2; from [Aligned presentations of the cycle module](aligned-presentations-of-the-cycle-module.md), the generator graph and chains of words (Section 1); and the homotopy invariance of singular homology [Fomberg, Theorem 1.13 and Corollary 1.14] from the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60). The following standard facts are used without proof; a course proving them is recorded as an open obligation of this course.

**(SIMP)** (simplicial and polyhedral complexes; [Hatcher, Theorem 2.27, Proposition 3.33, Section 2.1 on barycentric subdivision, and the Mayer–Vietoris sequence of Section 2.2]).

1. The simplicial homology of a simplicial complex, finite or not, and of a pair of a complex and a subcomplex, agrees with the singular homology of the realizations.
2. If a space is the union of an increasing sequence of subcomplexes \(K_0\subseteq K_1\subseteq\cdots\), every singular cycle lies in some \(K_n\), and every singular cycle of \(K_n\) that bounds in the union bounds in some \(K_m\), \(m\ge n\).
3. The barycentric subdivision of a finite simplicial complex, the order complex of its poset of nonempty simplices, is homeomorphic to it.
4. Convex polytopes glued along common faces, such that every face of a polytope is a polytope of the family and two polytopes meet in a common face, form a CW complex with the same underlying space. If such a complex is the union of two subcomplexes \(A\) and \(B\) with \(A\cap B\ne\varnothing\), there is an exact Mayer–Vietoris sequence
\[
\begin{aligned}
\cdots&\to\widetilde H_k(A\cap B)\\
&\to\widetilde H_k(A)\oplus\widetilde H_k(B)\\
&\to\widetilde H_k(A\cup B)\\
&\to\widetilde H_{k-1}(A\cap B)\to\cdots .
\end{aligned}
\]

## 1. The chain triangulation and heights

On the cube \(\chi_{g,\sigma}\), with coordinates \(x\in[0,1]^\sigma\), put
\[
\begin{aligned}
&\lambda\bigl(\chi_{g,\sigma}(x)\bigr)\\
&\quad=\lambda(g)+\sum_{q\in\sigma}x_q .
\end{aligned}\tag{1.1}
\]
On the face \(\{x_q=1\}\), which is \(\chi_{ga_q,\sigma\setminus q}\), the formula for that cube gives \(\lambda(g)+1+\sum_{r\ne q}x_r\), the same value; on \(\{x_q=0\}\) it is clear. So (1.1) defines a continuous map \(\lambda\colon E\to\mathbb R\) extending the height on the vertices, and \(\lambda(hx)=\lambda(h)+\lambda(x)\) for \(h\in P\). In particular \(G\) preserves every level \(\lambda^{-1}(c)\).

For a finite set \(\sigma\), the *chain triangulation* of \([0,1]^\sigma\) has as simplices the convex hulls of the indicator vectors \(\mathbf 1_{\tau_0},\ldots,\mathbf 1_{\tau_m}\) of the chains \(\tau_0\subsetneq\tau_1\subsetneq\cdots\subsetneq\tau_m\) of subsets of \(\sigma\).

**Lemma 1.1** (the chain triangulation). These simplices triangulate the cube: every \(x\in[0,1]^\sigma\) lies in the relative interior of exactly one of them, and the simplices contained in a face \(\{x_q=\epsilon\}\) form the chain triangulation of that face.

*Proof.* Let \(1\ge c_1>c_2>\cdots>c_m>0\) be the distinct nonzero values of the coordinates of \(x\), \(c_0=1\), \(c_{m+1}=0\), and \(\tau_j=\{q:x_q\ge c_j\}\) for \(1\le j\le m\), with \(\tau_0=\varnothing\) if \(c_1<1\). Then
\[
x=(1-c_1)\mathbf 1_\varnothing+\sum_{j=1}^m(c_j-c_{j+1})\mathbf 1_{\tau_j}
\]
(the first term omitted if \(c_1=1\)), a convex combination with positive weights of the corners of the chain of the \(\tau_j\); conversely, positive weights on a chain determine the coordinates and hence the chain, so this simplex is the only one containing \(x\) in its relative interior. A simplex lies in the face \(\{x_q=\epsilon\}\) exactly when all sets of its chain contain \(q\) (for \(\epsilon=1\)) or none does (for \(\epsilon=0\)), and these chains correspond to the chains of subsets of \(\sigma\setminus q\). \(\square\)

**Lemma 1.2** (the triangulation of \(E\)). Transporting the chain triangulations by the maps \(\chi_{g,\sigma}\) makes \(E\) a locally finite simplicial complex \(T\) with vertex set \(P\). Its simplices are the sets
\[
\begin{aligned}
&\Bigl\{v,\ v\prod_{q\in\tau_1}a_q,\ \ldots,\\
&\qquad v\prod_{q\in\tau_m}a_q\Bigr\},\\
&\varnothing\ne\tau_1\subsetneq\cdots\subsetneq\tau_m\\
&\qquad\text{a chain of cliques},
\end{aligned}\tag{1.2}
\]
and the heights of the vertices of a simplex are pairwise distinct: they are \(\lambda(v)<\lambda(v)+|\tau_1|<\cdots<\lambda(v)+|\tau_m|\).

*Proof.* By Lemma 2.1 of the lesson on the cube complex, the triangulation of a face of \(\chi_{g,\sigma}\) by Lemma 1.1 is the chain triangulation of the corresponding cube, so the triangulations agree on common faces, and by Lemma 2.2 there two cubes meet in a common face. A simplex in the cube \(\chi_{g,\sigma}\) has vertices \(g\prod_{q\in\tau_j}a_q\) for a chain \(\tau_0\subsetneq\cdots\subsetneq\tau_m\) of subsets of \(\sigma\); with \(v=g\prod_{q\in\tau_0}a_q\) this is (1.2) with the cliques \(\tau_j\setminus\tau_0\). Conversely, a set (1.2) lies in the cube \(\chi_{v,\tau_m}\). Local finiteness follows from Lemma 2.2 there. \(\square\)

## 2. Ascending and descending links

For a vertex \(v\) of \(T\), the *ascending link* \(\operatorname{Asc}(v)\) is the simplicial complex whose simplices are the simplices \(\Delta\) of \(T\) such that \(\Delta\cup\{v\}\) is a simplex and every vertex of \(\Delta\) has height greater than \(\lambda(v)\); the *descending link* \(\operatorname{Desc}(v)\) is defined with heights less than \(\lambda(v)\).

**Lemma 2.1** (the links are copies of \(L\)). For every vertex \(v\), \(\operatorname{Asc}(v)\) and \(\operatorname{Desc}(v)\) are isomorphic to the barycentric subdivision of \(L\): the vertex \(v\prod_{q\in\tau}a_q\) of \(\operatorname{Asc}(v)\) corresponds to the simplex \(\tau\) of \(L\), and \(v\prod_{q\in\tau}a_q^{-1}\) of \(\operatorname{Desc}(v)\) to \(\tau\).

*Proof.* Let \(w\) be a vertex of \(\operatorname{Asc}(v)\). The edge \(\{v,w\}\) is of the form (1.2) with \(v\) the vertex of smaller height, so \(w=v\prod_{q\in\tau}a_q\) for a nonempty clique \(\tau\), the vertex set of a simplex of \(L\) since \(L\) is flag; \(\tau\) is unique, since the abelianization map \(P\to\mathbb Z^V\) recovers it. Vertices \(w_j=v\prod_{q\in\tau_j}a_q\), \(1\le j\le m\), span together with \(v\) a simplex of \(T\) exactly when the \(\tau_j\) form a chain: if they do, this is (1.2); if \(\{v,w_1,\ldots,w_m\}\) is a simplex, it has the form (1.2) with \(v\), the vertex of least height, in the first place, and by uniqueness the sets of that chain are the \(\tau_j\). So \(\operatorname{Asc}(v)\) is the order complex of the poset of nonempty simplices of \(L\), its barycentric subdivision. For \(\operatorname{Desc}(v)\), the vertices are \(v\prod_{q\in\tau}a_q^{-1}\), the lowest vertices of the simplices (1.2) whose highest vertex is \(v\), and the same argument applies. \(\square\)

By (SIMP 3), if \(L\) is acyclic, so are all ascending and descending links.

## 3. The half spaces

From now on \(L\) is acyclic and nonempty. For \(n\ge0\) let \(K_n\) be the full subcomplex of \(T\) spanned by the vertices of height at least \(-n\), and \(K^-_n\) the one spanned by the vertices of height at most \(n\).

**Lemma 3.1** (adding a height). For \(n\ge0\), the inclusion \(K_n\subseteq K_{n+1}\) induces isomorphisms on homology.

*Proof.* A simplex of \(K_{n+1}\) not in \(K_n\) contains a vertex \(p\) of height \(-n-1\), and only one, since the heights in a simplex are distinct (Lemma 1.2); its other vertices have greater heights, so the simplex is the join of \(p\) with a simplex of \(\operatorname{Asc}(p)\) or with \(\varnothing\). Hence the relative simplicial chain complex is a direct sum over the vertices \(p\) of height \(-n-1\),
\[
\begin{aligned}
&C_*(K_{n+1},K_n)\\
&\quad\cong\bigoplus_pC_*\bigl(p*\operatorname{Asc}(p),\operatorname{Asc}(p)\bigr),
\end{aligned}
\]
where \(p*\operatorname{Asc}(p)\) is the cone. The cone is contractible, so the exact sequence of the pair gives \(H_k(p*\operatorname{Asc}(p),\operatorname{Asc}(p))\cong\widetilde H_{k-1}(\operatorname{Asc}(p))=0\) by Lemma 2.1. So \(H_*(K_{n+1},K_n)=0\), and the exact sequence of the pair \((K_{n+1},K_n)\) gives the claim, by (SIMP 1). There may be infinitely many vertices of height \(-n-1\); the direct sum takes care of them. \(\square\)

**Lemma 3.2.** \(K_0\) and \(K_0^-\) are acyclic.

*Proof.* Every vertex has finite height, so \(T=\bigcup_nK_n\). By Lemma 3.1, \(\widetilde H_*(K_0)\to\widetilde H_*(K_n)\) is an isomorphism for every \(n\), and by (SIMP 2) a cycle of \(K_0\) that bounds in \(E\) bounds in some \(K_n\), hence in \(K_0\). Since \(E\) is acyclic (Theorem 4.2 of the lesson on the cube complex), every cycle of \(K_0\) bounds, and \(\widetilde H_*(K_0)=0\). The same argument with descending links applies to \(K_0^-\). \(\square\)

**Lemma 3.3** (retraction of the half spaces). The half space \(E_+=\lambda^{-1}([0,\infty))\) deformation retracts onto \(K_0\), and \(E_-=\lambda^{-1}((-\infty,0])\) onto \(K_0^-\). So both are acyclic.

*Proof.* Let \(x\in E_+\) lie in a simplex of \(T\) with vertices \(v_i\), \(x=\sum_it_iv_i\) with \(t_i\ge0\), \(\sum t_i=1\). Since \(\lambda\) is affine on the simplex, \(0\le\lambda(x)=\sum t_i\lambda(v_i)\), so some \(v_i\) with \(t_i>0\) has \(\lambda(v_i)\ge0\). Put
\[
R(x)=\frac{\sum_{\lambda(v_i)\ge0}t_iv_i}{\sum_{\lambda(v_i)\ge0}t_i},
\]
a point of the face of the simplex spanned by its vertices of height at least \(0\), which lies in \(K_0\). The formula does not depend on the simplex chosen for \(x\), since passing to a face only removes vertices with \(t_i=0\). The homotopy \(H(x,s)=(1-s)x+sR(x)\) stays in the simplex, and in \(E_+\), since \(\lambda\) is affine there and \(\lambda(x),\lambda(R(x))\ge0\). It fixes \(K_0\) pointwise, is continuous on each simplex, and so is continuous on \(E_+\) by local finiteness. So \(K_0\) is a deformation retract of \(E_+\), and \(E_+\) is acyclic by Lemma 3.2 and the homotopy invariance of singular homology. The same holds for \(E_-\) and \(K_0^-\). \(\square\)

## 4. The level

The integer levels cut every cube \(\chi_{g,\sigma}\) into the convex polytopes \(\{x\in[0,1]^\sigma:m\le\sum_qx_q\le m+1\}\), \(m\in\mathbb Z\); with their faces, which include the *integer slices* \(\{x\in[0,1]^\sigma:\sum_qx_q=m\}\), they form a family of convex polytopes as in (SIMP 4), compatible on the faces of the cubes, because (1.1) is compatible. In the resulting CW structure on \(E\), the half spaces \(E_+\), \(E_-\) and the level
\[
X=\lambda^{-1}(0)=E_+\cap E_-
\]
are subcomplexes.

**Theorem 4.1** (the level is acyclic; [OpenAI-EG, Lemma 4.4]). If \(L\) is a nonempty acyclic flag complex, then \(X\) is nonempty, connected and acyclic.

*Proof.* \(X\) contains the vertex \(1\). By (SIMP 4), the Mayer–Vietoris sequence of \(E=E_+\cup E_-\) gives exact sequences
\[
\begin{aligned}
\widetilde H_{k+1}(E)&\to\widetilde H_k(X)\\
&\to\widetilde H_k(E_+)\oplus\widetilde H_k(E_-),
\end{aligned}
\]
whose outer terms vanish by Theorem 4.2 of the lesson on the cube complex and by Lemma 3.3. So \(\widetilde H_k(X)=0\) for all \(k\), and \(\widetilde H_0(X)=0\) says that \(X\) is connected. \(\square\)

The level is not claimed to be simply connected, and for the complex \(L\) of the counterexample it is not: Bestvina and Brady proved that \(G\) is finitely presented only if \(L\) is simply connected [Davis, Theorem 11.6.2], and the complex \(L\) of the lesson [An acyclic seed with quaternion monodromy](an-acyclic-seed-with-quaternion-monodromy.md) has a nontrivial fundamental group.

**The cells of the level.** Now let \(L\) have dimension at most two, so that the cubes have dimension at most three. In \([0,1]^k\), the integer slice \(\sum x_q=m\) is a corner for \(m\in\{0,k\}\), the diagonal from \((1,0)\) to \((0,1)\) for \(k=2\), \(m=1\), the triangle with vertices \(e_1,e_2,e_3\) for \(k=3\), \(m=1\), and the triangle with vertices \(e_1+e_2,\ e_1+e_3,\ e_2+e_3\) for \(k=3\), \(m=2\). The slice of \(\chi_{g,\sigma}\) at level \(0\) is the slice \(m=-\lambda(g)\). So:

**Lemma 4.2** (the cells of \(X\)). \(X\) is a two-dimensional simplicial complex whose vertices are the elements of \(G\). For every edge \(\{q,r\}\) of \(L\) and every \(g\in P\) with \(\lambda(g)=-1\) there is an edge \(\{ga_q,ga_r\}\); for every triangle \(\{q,r,s\}\) of \(L\) there is a triangle \(\{ga_q,ga_r,ga_s\}\) for every \(g\) with \(\lambda(g)=-1\), and a triangle \(\{ga_qa_r,ga_qa_s,ga_ra_s\}\) for every \(g\) with \(\lambda(g)=-2\). There are no other cells.

*Proof.* The cells of \(X\) are the slices at level \(0\) of the cubes of \(E\), listed above. They are simplices with vertices at height \(0\), embedded since the cubes are (Lemma 2.2 of the lesson on the cube complex); the slice of a face of a cube is a face of the slice, and two slices meet in the slice of the common face of their cubes, so they form a simplicial complex. It has dimension two if \(L\) has a triangle, and in any case at most two. \(\square\)

## 5. The group and its cycle basis

Order the vertex set \(V\) of \(L\). For every edge \(\{q,r\}\) of \(L\) with \(q<r\) introduce a letter \(s_{qr}\) with value \(a_q^{-1}a_r\in G\), and let \(S\) be the set of these letters. For every triangle \(\{q,r,s\}\) of \(L\) with \(q<r<s\), introduce the two words
\[
\begin{aligned}
z_{qrs}&=s_{qr}\,s_{rs}\,s_{qs}^{-1},\\
z'_{qrs}&=s_{rs}\,s_{qr}\,s_{qs}^{-1},
\end{aligned}\tag{5.1}
\]
and let \(\mathcal D\) be the list of these words. Dicks and Leary gave presentations of \(G\) whose generators are the directed edges of \(L\), the edge from \(q\) to \(r\) standing for \(a_qa_r^{-1}\), and in which every triangle of \(L\) contributes two relators of length three; they remark that the group defined by these relators and the relators \(e\bar e\) of length two arises in the work of Bestvina and Brady as the fundamental group of a level set [Dicks–Leary, Theorem 1, Proposition 2 and the remark after Corollary 3]. Since \(a_q\) and \(a_r\) commute, the value of \(s_{qr}\) is that of the edge from \(r\) to \(q\).

**Proposition 5.1** (the group and its cycle basis; [OpenAI-EG, Proposition 4.5]). Let \(L\) be a finite acyclic flag complex of dimension two. Then:

1. \(G\) is countable, finitely generated by the values of \(S\), residually finite, \(\operatorname{cd}G=2\) and \(\operatorname{gd}G\le3\);
2. \(G\) acts freely on \(X\), with finitely many orbits of cells and one orbit of vertices;
3. the words of \(\mathcal D\) have value \(1\) in \(G\), and for \(\Lambda=\mathbb ZG\) the sequence
\[
\begin{aligned}
&0\to\Lambda^{(\mathcal D)}\xrightarrow{\ \partial_2\ }\Lambda^{(S)}\\
&\qquad\xrightarrow{\ \partial_1\ }\Lambda\to\mathbb Z\to0,\\
&\partial_1(e_s)=\bar s-1,\quad\partial_2(e_z)=[z],
\end{aligned}
\]
is exact. In particular the chains \([z]\), \(z\in\mathcal D\), form a \(\Lambda\)-basis of the cycle module of the generator graph of \(S\).

*Proof.* *The action.* The group \(G\subseteq P\) acts on \(E\) by deck transformations and preserves \(X\). An element fixing a cell of \(X\) maps the unique cube in whose interior the relative interior of that cell lies to itself; deck transformations permute the cubes freely (Lemma 2.1 of the lesson on the cube complex), so the element is \(1\). The vertices of \(X\) are the elements of \(G\), permuted transitively by left multiplication. For each clique \(\sigma\) and each \(m\), the cubes \(\chi_{g,\sigma}\) with \(\lambda(g)=-m\) form one \(G\)-orbit, since \(G\) acts transitively on \(\lambda^{-1}(-m)\); so the cells of \(X\) fall into finitely many orbits, one for each edge of \(L\) and two for each triangle, by Lemma 4.2.

*The generator graph.* The edge \(\{a_q^{-1}a_q,\ a_q^{-1}a_r\}=\{1,\ a_q^{-1}a_r\}\) of the orbit of \(\{q,r\}\), oriented from the \(q\)-end to the \(r\)-end, starts at \(1\) and ends at \(a_q^{-1}a_r\), the value of \(s_{qr}\); its translates are the edges from \(h\) to \(ha_q^{-1}a_r\), \(h\in G\). So the \(1\)-skeleton of \(X\), with these orientations, is the generator graph of \(S\) over \(G\). It is connected by Theorem 4.1, so the values of \(S\) generate \(G\).

*The triangles.* For \(g=a_q^{-1}\), the triangle \(\{ga_q,ga_r,ga_s\}=\{1,\ a_q^{-1}a_r,\ a_q^{-1}a_s\}\) has the boundary path from \(1\) along \(s_{qr}\) to \(a_q^{-1}a_r\), along \(s_{rs}\) (from \(ga_r\) to \(ga_r\cdot a_r^{-1}a_s=ga_s\)) to \(a_q^{-1}a_s\), and backwards along \(s_{qs}\) to \(1\): this is the word \(z_{qrs}\). For \(g=a_q^{-1}a_r^{-1}\), the triangle \(\{ga_qa_r,ga_qa_s,ga_ra_s\}=\{1,\ a_r^{-1}a_s,\ a_q^{-1}a_s\}\) (the generators of a triangle of \(L\) commute) has the boundary path along \(s_{rs}\), then along \(s_{qr}\) (from \(ga_sa_q\) to \(ga_sa_r\)), then backwards along \(s_{qs}\) (from \(ga_ra_q\) to \(ga_ra_s\)): this is the word \(z'_{qrs}\). So each orbit of triangles has a representative whose boundary, read from \(1\), is the corresponding word of \(\mathcal D\), and these words have value \(1\).

*Exactness.* With the orientations and representatives just chosen, the simplicial chain complex of \(X\) is the displayed complex: \(C_0=\Lambda\), \(C_1=\Lambda^{(S)}\) with \(\partial_1(he_s)=h\bar s-h\), and \(C_2=\Lambda^{(\mathcal D)}\), the boundary of the triangle of \(z\) being the chain \([z]\) of its boundary path. By Theorem 4.1 and (SIMP 1) the augmented complex is exact, including at \(\Lambda^{(\mathcal D)}\), since \(X\) has no cells of dimension three and \(H_2(X)=0\).

*Dimensions.* The exact sequence is a free resolution of length two, so \(\operatorname{cd}G\le2\) (the remark after Lemma 2.2 of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md)). For a triangle \(\{q,r,s\}\) of \(L\), the commuting elements \(a_q,a_r,a_s\) generate a subgroup isomorphic to \(\mathbb Z^3\), the map from \(\mathbb Z^3\) being injective after abelianization; its intersection with \(G\) is the kernel of \((x,y,z)\mapsto x+y+z\), isomorphic to \(\mathbb Z^2\). So \(\operatorname{cd}G\ge2\) by Corollary 3.3 of that lesson. Residual finiteness is Theorem 4.1 of [Right-angled Artin groups and residual finiteness](right-angled-artin-groups-and-residual-finiteness.md), and \(\operatorname{gd}G\le3\) is Corollary 5.1 of the lesson on the cube complex. \(P\) is finitely generated, hence countable, and so is \(G\). \(\square\)

The same kernels are studied for general Artin groups, whose Salvetti complexes generalize the torus complex. Flores Martínez computed the Euler characteristics of the Bestvina–Brady kernels of the Artin groups of spherical type, through their action on non-integer levels of the universal cover of the Salvetti complex and discrete Morse theory, and extended the computation to Artin groups satisfying the \(K(\pi,1)\)-conjecture whose nerves are rationally acyclic [Flores Martínez 2026]. Among right-angled Artin groups only the free abelian ones are of spherical type.

## 6. Exercises

**6.1** (easy). Let \(L\) be a single triangle \(\{1,2,3\}\). Show that \(P=\mathbb Z^3\), that \(X\) is the plane \(x_1+x_2+x_3=0\) in \(\mathbb R^3\) tiled by triangles, and write down \(S\) and \(\mathcal D\).

**6.2** (easy). For \(L\) a single triangle, verify directly that \([z_{123}]\) and \([z'_{123}]\) form a basis of the cycle module, using that \(G\cong\mathbb Z^2\) has the resolution of Lemma 3.2 of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md).

**6.3** (medium). Let \(L\) consist of two points, so that it is not acyclic. Show that \(P=F(a_1,a_2)\), that \(X\) is the discrete set \(G\) with no edges, and that \(G\) is free of infinite rank. Which step of the proof of Theorem 4.1 fails?

**6.4** (medium). Show that the ascending link of a vertex of \(T\) in the triangulation of the square \([0,1]^2\) (one square, \(L\) a single edge) is a path with three vertices, the barycentric subdivision of an edge.

## 7. Solutions

**6.1.** \(L\) is a clique, so \(P=\mathbb Z^3\), \(E=\mathbb R^3\) with the unit cubes, and \(\lambda(x)=x_1+x_2+x_3\). The level is the plane; the cubes of initial height \(-1\) and \(-2\) cut it in triangles of the two types of Lemma 4.2, which tile it. \(S=\{s_{12},s_{23},s_{13}\}\) with values \(a_1^{-1}a_2,\ a_2^{-1}a_3,\ a_1^{-1}a_3\), and \(\mathcal D=\{s_{12}s_{23}s_{13}^{-1},\ s_{23}s_{12}s_{13}^{-1}\}\).

**6.2.** Write \(u=a_1^{-1}a_2\) and \(w=a_2^{-1}a_3\); then \(G=\langle u,w\rangle\cong\mathbb Z^2\) and \(\bar s_{13}=uw\). Let \(e_{12},e_{23},e_{13}\) be the basis of \(\Lambda^{(S)}\). By Lemma 1.1 of the lesson on aligned presentations, \([z_{123}]=e_{12}+ue_{23}-e_{13}\) and \([z'_{123}]=e_{23}+we_{12}-e_{13}\). Put \(f=e_{13}-e_{12}-ue_{23}\); then \(e_{12},e_{23},f\) is again a basis, and \(\partial_1f=(uw-1)-(u-1)-u(w-1)=0\). So the cycle module is \(\Lambda f\oplus Z'\), where \(Z'\) is the cycle module of the generator graph of the two letters \(s_{12},s_{23}\) with values \(u,w\). By Lemma 3.2 of [Cohomological and geometric dimension](cohomological-and-geometric-dimension.md) and Exercise 5.2 of the lesson on aligned presentations, \(Z'\) is free on \(c=(1-w)e_{12}+(u-1)e_{23}\). Now \([z_{123}]=-f\) and \([z'_{123}]-[z_{123}]=(w-1)e_{12}+(1-u)e_{23}=-c\), so the two chains are obtained from the basis \(f,c\) of the cycle module by an invertible triangular change, and form a basis.

**6.3.** With two isolated vertices and no edge, \(P=F(a_1,a_2)\), \(E\) is the tree of Lemma 4.1 of the lesson on the cube complex, and every edge of \(E\) runs from a height \(h\) to the height \(h+1\); so the level \(\lambda^{-1}(0)\) consists of the vertices of height \(0\), the elements of \(G\), with no edges. The group \(G\) is free of infinite rank, with basis the elements \(a_1^na_2a_1^{-n-1}\), \(n\in\mathbb Z\) (the Reidemeister–Schreier method with the transversal \(a_1^n\)). The step that fails is Lemma 3.1: the ascending links are two points, whose reduced homology \(\widetilde H_0\) is \(\mathbb Z\), so adding a height changes the homology; correspondingly \(\widetilde H_0(X)\ne0\).

**6.4.** In the square with vertices \(00,10,01,11\) the chain triangulation has the diagonal from \(00\) to \(11\). The ascending link of \(00\) consists of the vertices \(10\), \(01\), \(11\) and the edges \(\{10,11\}\) and \(\{01,11\}\), corresponding to the chains \(\{1\}\subsetneq\{1,2\}\) and \(\{2\}\subsetneq\{1,2\}\): a path with middle vertex \(11\), the barycentric subdivision of the edge \(\{1,2\}\) of \(L\), whose barycentre corresponds to \(\{1,2\}\).

## References

- [OpenAI-EG] OpenAI, *A finitely generated counterexample to the Eilenberg–Ganea conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 4.2 and 4.3. https://github.com/openai/math/tree/main/preprints/A-finitely-generated-counterexample-to-the-Eilenberg-Ganea-conjecture-September-23-2026
- [Davis] M. W. Davis, *The Geometry and Topology of Coxeter Groups*, Princeton University Press, 2008; first edition on the author's page, Section 11.6 and Theorem 11.6.2. https://people.math.osu.edu/davis.12/davisbook.pdf
- [Dicks–Leary] W. Dicks and I. J. Leary, *Presentations for subgroups of Artin groups*, Proceedings of the American Mathematical Society 127 (1999); arXiv:1210.6585, Theorem 1 and Proposition 2. https://arxiv.org/abs/1210.6585
- [Flores Martínez 2026] E. Flores Martínez, *The Euler characteristic of spherical Bestvina–Brady kernels*, arXiv:2610.19203 (October 2026). https://arxiv.org/abs/2610.19203
- [Hatcher] A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002; free edition on the author's page. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
