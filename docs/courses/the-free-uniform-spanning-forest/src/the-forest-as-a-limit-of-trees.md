# The forest as a limit of trees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An infinite connected graph has no uniform spanning tree in the literal sense, because there are infinitely many spanning trees. This lesson constructs the natural substitute: take the uniform spanning trees of larger and larger finite connected subgraphs, and pass to the limit. The limit exists, does not depend on the subgraphs chosen, and is described by determinants. It is a random set of edges without cycles, the *free uniform spanning forest*.

- For the uniform spanning tree \(T\) of a finite connected graph, the probability that a set \(F\) of edges is contained in \(T\) is a determinant, \(\det(K_{e,f})_{e,f\in F}\) (Theorem 1.2).
- The matrix \(K\) is the orthogonal projection onto the orthogonal complement of the space of circulations, which is spanned by the cycles (Proposition 2.1, Lemma 2.2).
- Along an increasing sequence of finite subgraphs that exhausts an infinite graph, these matrices converge entry by entry, to a limit that does not depend on the sequence (Proposition 3.1).
- So the laws of the uniform spanning trees converge to a probability measure on the sets of edges of the infinite graph, with the same determinant formula (Theorem 4.1).

The lesson follows [OpenAI-F, Section 2, the proposition on the free exhaustion limit]. The construction is classical: according to [OpenAI-F, Section 1], R. Pemantle constructed such limits on the integer lattices, and I. Benjamini, R. Lyons, Y. Peres and O. Schramm developed the theory for general graphs. The lesson continues [Weighted spanning trees](weighted-spanning-trees.md). It uses orthogonal projections onto closed subspaces of the space \(\ell^2\) (core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20)) and the fact that a probability measure on a countable product of finite sets is determined by its values on cylinders (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)).

## 1. Inclusion probabilities as determinants

Let \(H\) be a finite connected graph with at least two vertices, with directions of the edges, a vertex \(v_0\) and the reduced incidence vectors \(a_f\), as in the lesson on weighted spanning trees. Let \(A\) be the matrix with the columns \(a_f\), \(f\in E(H)\). For the weights \(1\) the reduced Laplacian is \(L=AA^{\mathsf T}\), and it is invertible. Let \(T\) be the uniform spanning tree of \(H\), and
\[
K_H=A^{\mathsf T}(AA^{\mathsf T})^{-1}A,
\]
a square matrix with rows and columns indexed by the edges; its entries are \(K_H(e,f)=a_e^{\mathsf T}L^{-1}a_f\). For a set \(F\) of edges, \((K_H)_F\) is the matrix of the entries with both indices in \(F\).

**Lemma 1.1.** Let \(U\) be a matrix with \(r\) rows and \(k\) columns and \(V\) a matrix with \(k\) rows and \(r\) columns. Then \(\det(I_r+UV)=\det(I_k+VU)\).

**Proof.** The block matrix \(\begin{pmatrix}I_r&-U\\V&I_k\end{pmatrix}\) is equal to both products
\[
\begin{gathered}
\begin{pmatrix}I_r&0\\V&I_k\end{pmatrix}\begin{pmatrix}I_r&-U\\0&I_k+VU\end{pmatrix},\\
\begin{pmatrix}I_r+UV&-U\\0&I_k\end{pmatrix}\begin{pmatrix}I_r&0\\V&I_k\end{pmatrix}.
\end{gathered}
\]
The determinant of a block triangular matrix is the product of the determinants of its diagonal blocks. So the first product has the determinant \(\det(I_k+VU)\) and the second \(\det(I_r+UV)\). \(\blacksquare\)

**Theorem 1.2.** For every set \(F\) of edges of \(H\),
\[
\mathbb P(F\subseteq T)=\det(K_H)_F .
\]
For the empty set both sides are \(1\).

**Proof.** Let \(z_e\), \(e\in F\), be real numbers larger than \(-1\), and give the edges \(e\in F\) the weights \(1+z_e\) and all other edges the weight \(1\). The weight of a spanning tree \(T_0\) is then the product of \(1+z_e\xi_e(T_0)\) over \(e\in F\), where \(\xi_e\) is the indicator of \(e\). So the weighted number of spanning trees, divided by their number, is \(\mathbb E\prod_{e\in F}(1+z_e\xi_e)\). By the matrix-tree theorem (Theorem 3.1 of the lesson on weighted spanning trees) the weighted number is \(\det(L+A_FD_zA_F^{\mathsf T})\), where \(A_F\) consists of the columns of \(A\) in \(F\) and \(D_z\) is the diagonal matrix of the \(z_e\). Dividing by \(\det L\) and using Lemma 1.1,
\[
\begin{aligned}
&\mathbb E\prod_{e\in F}(1+z_e\xi_e)\\
&\quad=\det\bigl(I+L^{-1}A_FD_zA_F^{\mathsf T}\bigr)\\
&\quad=\det\bigl(I_F+D_zA_F^{\mathsf T}L^{-1}A_F\bigr)\\
&\quad=\det\bigl(I_F+D_z(K_H)_F\bigr).
\end{aligned}
\]
Both sides are polynomials in the \(z_e\), so the identity holds for all real \(z_e\). Compare the coefficients of the product of all \(z_e\), \(e\in F\). On the left it is \(\mathbb E\prod_{e\in F}\xi_e=\mathbb P(F\subseteq T)\). On the right, the row \(e\) of the matrix is the row \(e\) of the identity plus \(z_e\) times the row \(e\) of \((K_H)_F\); the determinant is linear in each row, and the term containing all the \(z_e\) is their product times \(\det(K_H)_F\). \(\blacksquare\)

For one edge this is \(\mathbb P(e\in T)=K_H(e,e)\), and for two edges the probability \(\mathbb P(e,f\in T)\) is \(K_H(e,e)K_H(f,f)-K_H(e,f)^2\), in agreement with Proposition 4.2 of the lesson on weighted spanning trees. A set \(F\) with more than \(|V|-1\) elements is contained in no spanning tree; the determinant is then \(0\).

## 2. The projection and the cycles

A vector \(x\in\mathbb R^{E(H)}\) is a *circulation* if \(Ax=0\), that is \(\sum_fx_fa_f=0\). In words: if \(x_f\) is read as a flow along \(f\) in its direction, the flow into every vertex equals the flow out of it. This holds at \(v_0\) as well, because it holds at all other vertices and every edge contributes \(+1\) and \(-1\) to the total. Let \(C_H\) be the space of the circulations.

**Proposition 2.1.** The matrix \(K_H\) is symmetric, \(K_H^2=K_H\), and \(K_Hx=0\) exactly for \(x\in C_H\). So \(K_H\) is the orthogonal projection of \(\mathbb R^{E(H)}\) onto the orthogonal complement of \(C_H\):
\[
K_H=I-P_{C_H},
\]
where \(P_{C_H}\) is the orthogonal projection onto \(C_H\).

**Proof.** \(K_H\) is symmetric because \(L\) is, and \(K_H^2=A^{\mathsf T}L^{-1}(AA^{\mathsf T})L^{-1}A=K_H\). If \(Ax=0\) then \(K_Hx=0\). If \(K_Hx=0\), then \(0=AK_Hx=(AA^{\mathsf T})L^{-1}Ax=Ax\).

A symmetric matrix \(K\) with \(K^2=K\) is the orthogonal projection onto the orthogonal complement of its kernel: for every \(x\), the vector \(x-Kx\) lies in the kernel, because \(K(x-Kx)=0\), and \(Kx\) is orthogonal to every \(y\) in the kernel, because \(\langle Kx,y\rangle=\langle x,Ky\rangle=0\). \(\blacksquare\)

In particular \(C_H\) and \(K_H\) do not depend on the vertex \(v_0\). If the direction of an edge \(e\) is reversed, \(a_e\) changes its sign, and so do the entries \(K_H(e,f)\) and \(K_H(f,e)\) for \(f\ne e\); the determinants \(\det(K_H)_F\) do not change.

A cycle of \(H\), traversed in one of its two senses, defines a *cycle flow*: the vector that is \(+1\) on the edges of the cycle traversed in their direction, \(-1\) on the others, and \(0\) outside the cycle. It is a circulation (proof of Lemma 1.1 of the lesson on weighted spanning trees).

**Lemma 2.2.** The space \(C_H\) is spanned by the cycle flows.

**Proof.** Fix a spanning tree \(T_0\). For an edge \(f\notin T_0\) the graph with the edges \(T_0\cup\{f\}\) contains exactly one cycle, and it passes through \(f\); let \(\gamma_f\) be its cycle flow with the value \(+1\) on \(f\). Let \(x\in C_H\), and \(y=x-\sum_{f\notin T_0}x_f\gamma_f\). Then \(y\) is a circulation that vanishes outside \(T_0\). At a leaf of the tree only one edge of \(T_0\) is present, so \(y\) vanishes on it. Removing this leaf and its edge and repeating shows \(y=0\). \(\blacksquare\)

## 3. Exhaustions of an infinite graph

Let \(G\) be an infinite connected graph in which every vertex lies on finitely many edges, with vertex set \(V\) and edge set \(E\); \(E\) is countable. Fix a direction for every edge. Let \(\ell^2(E)\) be the Hilbert space of the real functions \(x\) on \(E\) with \(\sum_ex_e^2<\infty\), with the scalar product \(\langle x,y\rangle=\sum_ex_ey_e\), and let \(\delta_e\) be the function that is \(1\) at \(e\) and \(0\) elsewhere. A function on the edges of a finite subgraph is regarded as an element of \(\ell^2(E)\), with the value \(0\) on the other edges.

An *exhaustion* of \(G\) is a sequence \(H_1\subseteq H_2\subseteq\cdots\) of finite connected subgraphs with at least two vertices whose edge sets have the union \(E\). Exhaustions exist: for a fixed vertex \(o\), let \(H_n\) consist of the vertices at distance at most \(n\) from \(o\) and all edges of \(G\) between them. The subgraphs of an exhaustion need not contain all edges of \(G\) between their vertices. Let \(C_n=C_{H_n}\subseteq\ell^2(E)\) and \(K_n=K_{H_n}\); by Proposition 2.1, as an operator on \(\ell^2(E)\),
\[
K_n=Q_n-P_{C_n},
\]
where \(Q_n\) sets the coordinates outside \(E(H_n)\) to \(0\). A circulation of \(H_n\) is a circulation of \(H_{n+1}\), because at the vertices of \(H_n\) the new edges carry the value \(0\), and at the new vertices all values are \(0\). So \(C_1\subseteq C_2\subseteq\cdots\). Let \(C\) be the closure of the union of the \(C_n\) in \(\ell^2(E)\). Every cycle of \(G\) has finitely many edges and so lies in some \(H_n\); with Lemma 2.2, \(C\) is the closed linear span of the cycle flows of all cycles of \(G\). In particular \(C\) does not depend on the exhaustion. Let
\[
K=I-P_C,\qquad K(e,f)=\langle K\delta_f,\delta_e\rangle .
\]

**Proposition 3.1.** For every \(x\in\ell^2(E)\), \(P_{C_n}x\to P_Cx\) in \(\ell^2(E)\). Consequently \(K_n(e,f)\to K(e,f)\) for all edges \(e,f\).

**Proof.** Let \(m\ge n\). Since \(C_n\subseteq C_m\), the vector \(P_{C_m}x-P_{C_n}x\) is orthogonal to \(C_n\): for \(c\in C_n\), both \(\langle P_{C_m}x,c\rangle\) and \(\langle P_{C_n}x,c\rangle\) are equal to \(\langle x,c\rangle\). In particular it is orthogonal to \(P_{C_n}x\), so
\[
\begin{aligned}
&\|P_{C_m}x-P_{C_n}x\|^2\\
&\quad=\|P_{C_m}x\|^2-\|P_{C_n}x\|^2 .
\end{aligned}
\]
The numbers \(\|P_{C_n}x\|^2\) increase with \(n\) and are at most \(\|x\|^2\), so they converge, and \((P_{C_n}x)\) is a Cauchy sequence. Let \(y\) be its limit; it lies in \(C\). For every \(n\) and \(m\ge n\), \(x-P_{C_m}x\) is orthogonal to \(C_n\); hence \(x-y\) is orthogonal to every \(C_n\), and so to \(C\). Therefore \(y=P_Cx\).

For the second statement, \(K_n(e,f)=\langle Q_n\delta_f-P_{C_n}\delta_f,\delta_e\rangle\), and \(Q_n\delta_f=\delta_f\) as soon as \(f\in E(H_n)\). \(\blacksquare\)

## 4. The limit law

A set of edges of \(G\) is identified with its indicator function, an element of \(\{0,1\}^E\). On this product we use the \(\sigma\)-algebra generated by the coordinates. For disjoint finite sets \(A,B\subseteq E\) the *cylinder* \([A,B]\) is the set of the \(\omega\subseteq E\) with \(A\subseteq\omega\) and \(B\cap\omega=\emptyset\). Let \(\mu_n\) be the law of the uniform spanning tree of \(H_n\), as a random subset of \(E\).

**Theorem 4.1.** Let \(G\) be an infinite connected graph in which every vertex lies on finitely many edges.

1. There is exactly one probability measure \(\mu\) on \(\{0,1\}^E\) with
\[
\mu(\{\omega:F\subseteq\omega\})=\det K_F
\]
for every finite \(F\subseteq E\), where \(K_F=(K(e,f))_{e,f\in F}\).
2. For every exhaustion and all disjoint finite \(A,B\subseteq E\), \(\mu_n([A,B])\to\mu([A,B])\).
3. With probability one for \(\mu\), the random set of edges contains no cycle.
4. The measure \(\mu\) does not depend on the directions of the edges, and an isomorphism of graphs \(G\to G'\) carries the measure of \(G\) to the measure of \(G'\).

**Proof.** *Limits of cylinder probabilities.* Let \(A,B\) be disjoint and finite, and \(n\) so large that \(A\cup B\subseteq E(H_n)\). With the indicators \(\xi_e\) of the edges, the indicator of the cylinder \([A,B]\) is \(\prod_{a\in A}\xi_a\prod_{b\in B}(1-\xi_b)\). Expanding the second product into a sum over the subsets \(J\subseteq B\) and using Theorem 1.2,
\[
\mu_n([A,B])=\sum_{J\subseteq B}(-1)^{|J|}\det(K_n)_{A\cup J}.
\]
By Proposition 3.1 every determinant converges to \(\det K_{A\cup J}\). So \(\rho(A,B)=\lim_n\mu_n([A,B])\) exists. These numbers are nonnegative, \(\rho(\emptyset,\emptyset)=1\), and for an edge \(e\notin A\cup B\)
\[
\begin{aligned}
\rho(A,B)&=\rho(A\cup\{e\},B)\\
&\quad+\rho(A,B\cup\{e\}),
\end{aligned}
\]
because this holds for \(\mu_n\).

*Construction of \(\mu\).* Enumerate the edges as \(e_1,e_2,\dots\). For a word \(w\in\{0,1\}^j\) let \(\rho(w)=\rho(A_w,B_w)\), where \(A_w\) is the set of the \(e_i\) with \(w_i=1\) and \(B_w\) the set of the \(e_i\) with \(w_i=0\), \(i\le j\). Then \(\rho(w)=\rho(w0)+\rho(w1)\), and the empty word has \(\rho=1\). Define intervals \(I_w\subseteq[0,1)\), closed on the left and open on the right, of the lengths \(\rho(w)\): \(I_w=[0,1)\) for the empty word, and \(I_{w0}\), \(I_{w1}\) are the left and the right part of \(I_w\). For each \(j\) the intervals of the words of length \(j\) are disjoint with union \([0,1)\). So every \(u\in[0,1)\) lies in exactly one \(I_w\) for each length, these words extend one another, and they define an infinite word \(\Phi(u)\in\{0,1\}^E\). The inverse image under \(\Phi\) of the set of the \(\omega\) that begin with \(w\) is \(I_w\). So \(\Phi\) is measurable, and the image \(\mu\) of the Lebesgue measure under \(\Phi\) gives the mass \(\rho(w)\) to this set. Adding over the words of a sufficient length gives \(\mu([A,B])=\rho(A,B)\) for all disjoint finite \(A,B\). This proves (2), and with \(B=\emptyset\) the formula in (1).

*Uniqueness.* If \(\mu'\) satisfies (1), the same expansion gives \(\mu'([A,B])=\sum_J(-1)^{|J|}\det K_{A\cup J}\), which is \(\mu([A,B])\). The cylinders, together with the empty set, are closed under finite intersections and generate the \(\sigma\)-algebra, so \(\mu'=\mu\).

(3) Let \(F\) be the edge set of a cycle of \(G\). For large \(n\), \(F\subseteq E(H_n)\) and \(\mu_n([F,\emptyset])=0\), because a tree contains no cycle. So \(\mu([F,\emptyset])=0\). There are countably many cycles.

(4) Reverse the directions of some edges, and let \(s_e=-1\) for these edges and \(s_e=+1\) for the others. Every cycle flow is multiplied coordinate by coordinate by the signs \(s_e\). This is an operator on \(\ell^2(E)\) that preserves the scalar product, so it maps \(C\) onto the space \(C\) for the new directions, and \(K(e,f)\) is replaced by \(s_es_fK(e,f)\). This multiplies \(\det K_F\) by \(\prod_{e\in F}s_e^2=1\). An isomorphism of graphs maps cycles to cycles, hence the space \(C\) of \(G\) to that of \(G'\), and \(K\) to the corresponding operator, if the directions are transported as well. \(\blacksquare\)

Statement (2) says that the probability of every event that depends on finitely many edges converges, because such an event is a finite disjoint union of cylinders.

**Definition 4.2.** The measure \(\mu\) of Theorem 4.1 is the *free uniform spanning forest* of \(G\), written \(\mathsf{FUSF}_G\).

The word free refers to the exhaustion by subgraphs with their own spanning trees, without any identification of vertices at the boundary. The limit has no cycles; it need not be connected, which is why it is called a forest. Connectedness plays no role in this course.

**Example 4.3.** If \(G\) is a tree, for example the path that is infinite in both directions, there are no cycles, \(C=0\) and \(K=I\). So \(\det K_F=1\) for every finite \(F\): the free uniform spanning forest is the whole graph, with probability one.

**Example 4.4.** Let \(G\) be a triangle with an infinite path attached at each of its three vertices. The only cycle is the triangle, so \(C\) is spanned by one cycle flow \(\gamma\), with \(\|\gamma\|^2=3\). Direct the triangle cyclically. For edges \(e,f\) of the triangle, \(K(e,f)\) is the entry of the matrix of Exercise 5.1. For an edge \(e\) of a path, \(K(e,e)=1\) and \(K(e,f)=0\) for all \(f\ne e\). So for a finite set \(F\), \(\det K_F\) is the determinant for the edges of \(F\) in the triangle. By the uniqueness in Theorem 4.1, the free uniform spanning forest consists of all edges of the three paths and two edges of the triangle, each of the three pairs with probability \(\tfrac13\). This agrees with the finite subgraphs: a spanning tree of the triangle with three finite paths contains all edges of the paths and two edges of the triangle.

## 5. Exercises

**5.1.** For the triangle with a cyclic choice of directions, compute \(K_H\) from Proposition 2.1 and check Theorem 1.2 for all sets \(F\).

**5.2.** Let \(H\subseteq H'\) be finite connected graphs and \(e\) an edge of \(H\). Show that the probability that \(e\) belongs to the uniform spanning tree of \(H'\) is at most the probability that it belongs to the uniform spanning tree of \(H\).

**5.3.** Show that \(0\le K(e,e)\le1\) and \(|K(e,f)|\le1\) for all edges, and that \(\mathsf{FUSF}_G\) gives two different edges a covariance that is not positive.

**5.4.** Derive the formula \(\det(I+xy^{\mathsf T})=1+y^{\mathsf T}x\) for vectors \(x,y\) from Lemma 1.1.

## 6. Solutions

**5.1.** The space \(C_H\) is spanned by the cycle flow \(\gamma=(1,1,1)\). The projection onto it is the matrix with all entries \(\tfrac13\), so \(K_H\) has the diagonal entries \(\tfrac23\) and the other entries \(-\tfrac13\). One edge: \(\tfrac23\). Two edges: \(\tfrac49-\tfrac19=\tfrac13\). Three edges: the determinant is \(0\), because the rows add up to zero. The triangle has three spanning trees, each with two edges; each edge is in two of them, each pair of edges is one of them, and no tree has three edges.

**5.2.** By Theorem 1.2 and Proposition 2.1 the probability for \(H\) is \(K_H(e,e)=1-\|P_{C_H}\delta_e\|^2\). Since \(C_H\subseteq C_{H'}\), \(\|P_{C_H}\delta_e\|\le\|P_{C_{H'}}\delta_e\|\).

**5.3.** \(K\) is an orthogonal projection, so \(K(e,e)=\|K\delta_e\|^2\in[0,1]\) and \(|K(e,f)|=|\langle K\delta_f,K\delta_e\rangle|\le1\). By Theorem 4.1 the probability that both \(e\) and \(f\) are present is \(K(e,e)K(f,f)-K(e,f)^2\), so the covariance of the two indicators is \(-K(e,f)^2\le0\).

**5.4.** Take \(r\) the number of coordinates, \(k=1\), \(U=x\) as a column and \(V=y^{\mathsf T}\) as a row. Then \(I_r+UV=I+xy^{\mathsf T}\), and \(I_1+VU\) is the number \(1+y^{\mathsf T}x\).

## References

- [OpenAI-F] OpenAI, *The free uniform spanning forest is a factor of IID*, OpenAI Math Release preprint, 25 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026
