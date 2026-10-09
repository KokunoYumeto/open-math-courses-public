# Ranks, matchings and pruning

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves a deletion bound for two families of ordered pairs that may conflict with each other (Theorem 3.1). It is the combinatorial engine of [The extremal argument and its consequences](the-extremal-argument-and-its-consequences.md), and it holds for every finite binary relation: no orientation, transitivity or other assumption is used. The proof bounds a maximum matching in an auxiliary bipartite graph by comparing ranks of four matrices with generic coefficients, and then turns the matching into a vertex cover by König's theorem [Kőn]. The link between matchings and ranks of matrices with indeterminate entries goes back to Edmonds [Edm]. Sections 1 and 2 prove the facts about matchings and generic ranks that are used; Section 3 proves the theorem.

## 1. Matchings and vertex covers

A *bipartite graph* \(\Gamma\) has a finite vertex set split into a left part \(\mathcal V_L\) and a right part \(\mathcal V_R\), and edges joining a left vertex to a right vertex. A *matching* is a set of edges without common endpoints; a vertex is *matched* by it if it lies on one of its edges. A *vertex cover* is a set \(K\) of vertices containing at least one endpoint of every edge. Since the edges of a matching are disjoint, every vertex cover has at least as many vertices as every matching has edges.

Given a matching \(\mathcal M\), an *augmenting path* is a path whose first and last vertices are unmatched and whose edges alternate between edges outside \(\mathcal M\) and edges of \(\mathcal M\), beginning and ending outside \(\mathcal M\). Replacing the \(\mathcal M\)-edges of an augmenting path by its other edges produces a matching with one more edge.

**Lemma 1.1** (Berge). If a matching \(\mathcal M\) of \(\Gamma\) is not of maximum size, then \(\Gamma\) contains an augmenting path for \(\mathcal M\).

*Proof.* Let \(\mathcal M'\) be a larger matching, and consider the edges lying in exactly one of \(\mathcal M,\mathcal M'\). Every vertex lies on at most one edge of each, so in this set of edges every vertex has degree at most \(2\), and the components are paths and cycles whose edges alternate between \(\mathcal M'\) and \(\mathcal M\). Cycles have equally many edges of both kinds. Since \(\mathcal M'\) is larger, some path component \(P\) has more edges of \(\mathcal M'\) than of \(\mathcal M\); it begins and ends with \(\mathcal M'\)-edges. An end vertex \(x\) of \(P\) is unmatched by \(\mathcal M\): an \(\mathcal M\)-edge at \(x\) is not the \(\mathcal M'\)-edge of \(P\) at \(x\) (that edge lies outside \(\mathcal M\)), so it would also belong to the symmetric difference, and \(x\) would not be an end of \(P\). Hence \(P\) is an augmenting path for \(\mathcal M\). \(\square\)

**Theorem 1.2** (König). Let \(\mathcal M\) be a maximum matching of \(\Gamma\). Let \(W_L\subseteq\mathcal V_L\) and \(W_R\subseteq\mathcal V_R\) be the vertices reachable from unmatched left vertices by walks that use edges outside \(\mathcal M\) from left to right and edges of \(\mathcal M\) from right to left, the starting vertices included. Then
\[
K=(\mathcal V_L\setminus W_L)\cup W_R
\]
is a vertex cover with \(|K|=|\mathcal M|\), and \(K\) contains no vertex unmatched by \(\mathcal M\); in particular, \(K\) contains no isolated vertex.

*Proof.* A vertex of \(W_R\) is matched. Indeed, a shortest walk of the described kind reaching a vertex is a path, because a repeated vertex would allow a shorter walk obeying the same rules; a path from an unmatched left vertex to an unmatched right vertex would be augmenting, and augmenting along it would enlarge the maximum matching \(\mathcal M\). If \(y\in W_R\), its partner is in \(W_L\) by the rules of the walk. A matched left vertex \(x\) is not a starting vertex and can be entered only along its \(\mathcal M\)-edge, so \(x\in W_L\) implies that its partner is in \(W_R\). Hence every edge of \(\mathcal M\) has both ends reached or both unreached, and exactly one end in \(K\): the right end if they are reached, the left end otherwise.

Unmatched left vertices lie in \(W_L\), and unmatched right vertices are not in \(W_R\), so \(K\) consists of exactly one end of each edge of \(\mathcal M\), and \(|K|=|\mathcal M|\). An isolated vertex is unmatched, so it is not in \(K\).

Let \(xy\) be an edge with \(x\) left and \(y\) right. If \(x\notin W_L\), then \(x\in K\). If \(x\in W_L\) and \(xy\notin\mathcal M\), the walk continues to \(y\), so \(y\in W_R\subseteq K\). If \(x\in W_L\) and \(xy\in\mathcal M\), both ends are reached and \(y\in K\). \(\square\)

## 2. Generic ranks

For finite sets \(I,J\), a real matrix \(M=(M_{ij})_{i\in I,\,j\in J}\) is *supported* on \(T\subseteq I\times J\) if \(M_{ij}=0\) for \((i,j)\notin T\); entries in \(T\) may vanish. A *matching* in \(T\) is a subset of \(T\) in which no two positions share a row or a column. A square submatrix with no rows has determinant \(1\).

**Lemma 2.1.** If \(M\) is supported on \(T\) and the square submatrix with rows \(I'\) and columns \(J'\) has nonzero determinant, then \(T\) contains a matching between \(I'\) and \(J'\). Consequently \(\operatorname{rank}M\) is at most the largest size of a matching in \(T\).

*Proof.* Some term \(\pm\prod_{i\in I'}M_{i\sigma(i)}\) of the determinant, with \(\sigma:I'\to J'\) bijective, is nonzero; then \(\{(i,\sigma(i))\}\) is a matching in \(T\). The rank is the largest size of a square submatrix with nonzero determinant. \(\square\)

**Lemma 2.2.** A nonzero real polynomial in finitely many variables takes a nonzero value at some real point.

*Proof.* By induction on the number \(r\) of variables. For \(r=0\) the polynomial is a nonzero constant. For \(r\ge1\), write \(P=\sum_kP_k(x_1,\dots,x_{r-1})x_r^k\) with some \(P_k\ne0\), choose \((x_1,\dots,x_{r-1})\) with \(P_k\ne0\) there, and then choose \(x_r\) outside the finitely many roots of the resulting nonzero polynomial in \(x_r\). \(\square\)

A *pattern matrix* is a square matrix each of whose entries is either \(0\) or a variable, such that no variable occurs at two different positions.

**Lemma 2.3.** (a) If the positions of the variables in a pattern matrix contain a perfect matching, its determinant is a nonzero polynomial.

(b) Let \(M\) be a square matrix of polynomials which, after permuting its rows and columns, is block diagonal with square diagonal blocks, each a pattern matrix satisfying (a). Then \(\det M\) is a nonzero polynomial, even if a variable occurs in several blocks.

*Proof.* (a) In the Leibniz expansion, each permutation whose positions all carry variables contributes \(\pm\) the product of those variables, and all other permutations contribute \(0\). The set of positions determines the permutation, and distinct positions carry distinct variables, so different permutations contribute different monomials, with coefficients \(\pm1\). These cannot cancel, and the perfect matching provides at least one of them. (b) The determinant is the product of the block determinants, up to sign, and a product of nonzero polynomials is nonzero. \(\square\)

**Lemma 2.4** (Kernels at maximum rank). Let \(T\subseteq I\times J\), and let the real matrix \(D\) have the largest rank among all real matrices supported on \(T\). If \(x\in\ker D\), \(y\in\ker D^{\mathsf T}\) and \((s,j)\in T\), then \(x_jy_s=0\).

*Proof.* Suppose \(x_jy_s\ne0\). For a real \(\tau\ne0\), the matrix \(D_\tau=D+\tau e_se_j^{\mathsf T}\) is supported on \(T\), and \(D_\tau x=\tau x_je_s\), so \(e_s\in\operatorname{im}D_\tau\). For every \(w\), \(Dw=D_\tau w-\tau w_je_s\in\operatorname{im}D_\tau\), so \(\operatorname{im}D\subseteq\operatorname{im}D_\tau\). But \(y\) is orthogonal to \(\operatorname{im}D\) and \(y_s\ne0\), so \(e_s\notin\operatorname{im}D\). Thus \(\operatorname{rank}D_\tau>\operatorname{rank}D\), contrary to the choice of \(D\). \(\square\)

## 3. The pruning theorem

Let \(X\) be a finite set with an arbitrary binary relation, written \(x\to y\). Let \(\mathcal R,\mathcal C\subseteq X\times X\). Members of \(\mathcal R\) are called *left members* and members of \(\mathcal C\) *right members*; a pair lying in both sets gives two different members, one on each side.

A left member \((p,j)\) *covers* the points \((i,j)\) with \(p\to i\), and a right member \((i,s)\) covers the points \((i,j)\) with \(s\to j\). Thus left members cover points in their own column and right members in their own row. A left member \((p,j)\) and a right member \((i,s)\) *conflict* if they cover a common point; that point can only be \((i,j)\), so they conflict exactly when
\[
p\to i\qquad\text{and}\qquad s\to j .
\]
For a conflict, call \((i,j)\) its *shared point* and \((p,s)\) its *opposite point*, and let
\[
Z=\{\text{shared points of conflicts}\},\qquad H=\{\text{opposite points of conflicts}\}.
\]

**Theorem 3.1** (Pruning). There are \(\mathcal R'\subseteq\mathcal R\) and \(\mathcal C'\subseteq\mathcal C\) such that no member of \(\mathcal R'\) conflicts with a member of \(\mathcal C'\), every member of \(\mathcal R\cup\mathcal C\) that conflicts with nothing is kept, and
\[
|\mathcal R\setminus\mathcal R'|+|\mathcal C\setminus\mathcal C'|\le|H|+\bigl|\{z\in Z:z\text{ is covered by no member of }\mathcal R'\cup\mathcal C'\}\bigr| . \tag{3.1}
\]

If there are no conflicts, keeping everything works, because \(Z=H=\varnothing\). The proof occupies the rest of this section.

### 3.1. The auxiliary graph

Let \(Z_L\) and \(Z_R\) be two disjoint copies of \(Z\), with copies \(z_L\in Z_L\), \(z_R\in Z_R\) of \(z\in Z\). Let \(\Gamma\) be the bipartite graph with left part \(\mathcal V_L=\mathcal R\sqcup Z_L\) and right part \(\mathcal V_R=\mathcal C\sqcup Z_R\), and with three kinds of edges:

- \(rc\) for every conflicting pair \(r\in\mathcal R\), \(c\in\mathcal C\);
- \(rz_R\) whenever the left member \(r\) covers \(z\in Z\);
- \(z_Lc\) whenever the right member \(c\) covers \(z\in Z\).

There are no edges between \(Z_L\) and \(Z_R\). A conflict between \(r=(p,j)\) and \(c=(i,s)\) with shared point \(z=(i,j)\) produces the path \(z_L,\,c,\,r,\,z_R\). Vertices in \(\mathcal R\sqcup\mathcal C\) are called *original*.

**Lemma 3.2.** A member that conflicts with nothing is an isolated vertex of \(\Gamma\).

*Proof.* Such a member has no edge of the first kind. Suppose the left member \(r=(p,j)\) covers a point \(z=(i,j)\in Z\), so \(p\to i\). Since \(z\) is the shared point of some conflict, some right member \((i,s)\) has \(s\to j\), and then \(r\) conflicts with \((i,s)\). The argument for right members is symmetric. \(\square\)

**Lemma 3.3.** Suppose \(\Gamma\) has a vertex cover \(K\) with \(|K|\le|Z|+|H|\) that contains no isolated vertex. Delete the original members lying in \(K\). The remaining families \(\mathcal R'\), \(\mathcal C'\) satisfy the conclusions of Theorem 3.1.

*Proof.* Every conflict is an edge, and one of its ends was deleted, so no conflict remains. Members without conflicts are isolated (Lemma 3.2), hence not in \(K\), hence kept. Let \(q\) be the number of points of \(Z\) covered by no kept member. Each of the other \(|Z|-q\) points \(z\) is covered by a kept member, which is joined by an edge to a copy of \(z\); that member is not in \(K\), so the copy is. Distinct points have distinct copies, so \(K\) contains at least \(|Z|-q\) copies, and the number of deleted members is
\[
|K\cap(\mathcal R\sqcup\mathcal C)|\le|K|-(|Z|-q)\le|H|+q.\qquad\square
\]

By Theorem 1.2, it remains to prove that every matching of \(\Gamma\) has at most \(|Z|+|H|\) edges.

### 3.2. A well-chosen maximum matching

Among the maximum matchings of \(\Gamma\), choose \(\mathcal M\) with the fewest edges between two original vertices. Let \(k\) be the number of such edges, let \(\alpha\) be the set of edges of \(\mathcal M\) between \(\mathcal R\) and \(Z_R\), and \(\beta\) the set between \(Z_L\) and \(\mathcal C\); put \(\ell=|\alpha|\), \(t=|\beta|\), so \(|\mathcal M|=k+\ell+t\). Let \(\Gamma_\alpha\) be the subgraph formed by \(\mathcal R\), \(Z_R\) and the edges between them, and \(\Gamma_\beta\) the subgraph formed by \(Z_L\), \(\mathcal C\) and the edges between them.

**Lemma 3.4.** \(\alpha\) is a maximum matching of \(\Gamma_\alpha\), and \(\beta\) is a maximum matching of \(\Gamma_\beta\).

*Proof.* If not, Lemma 1.1 gives an augmenting path \(P\) for \(\alpha\) in \(\Gamma_\alpha\), from an \(\alpha\)-unmatched \(r\in\mathcal R\) to an \(\alpha\)-unmatched \(z_R\in Z_R\). In \(\Gamma\), the vertex \(z_R\) has neighbors only in \(\mathcal R\), so it is unmatched by \(\mathcal M\). The inner vertices of \(P\) are matched by \(\alpha\subseteq\mathcal M\) along \(P\). If \(r\) is unmatched by \(\mathcal M\), then \(P\) is augmenting for \(\mathcal M\), contradicting maximality. Otherwise \(r\) is matched by an edge \(rc\) of \(\mathcal M\) with \(c\in\mathcal C\), since its \(\mathcal M\)-edge is not in \(\alpha\). Removing \(rc\) and then augmenting along \(P\) gives a maximum matching with fewer edges between original vertices, contradicting the choice of \(\mathcal M\). The argument for \(\beta\) is the same with the sides exchanged. \(\square\)

Let \(R_\alpha\subseteq\mathcal R\) and \(C_\beta\subseteq\mathcal C\) be the original vertices matched by \(\alpha\) and \(\beta\). The ends of the \(k\) original edges of \(\mathcal M\) lie outside \(R_\alpha\) and \(C_\beta\).

### 3.3. Four matrices

For every pair \((x,y)\) with \(x\to y\), introduce two variables \(a_{xy}\) and \(b_{xy}\); put \(a_{xy}=b_{xy}=0\) when \(x\not\to y\). For a real value of each variable, define four matrices
\[
L\in\mathbb R^{Z\times\mathcal R},\qquad N\in\mathbb R^{\mathcal C\times Z},\qquad B\in\mathbb R^{H\times\mathcal R},\qquad A\in\mathbb R^{\mathcal C\times H}
\]
by
\[
L_{(i,j),(p,j)}=a_{pi},\qquad N_{(i,s),(i,j)}=b_{sj},\qquad B_{(p,s),(p,j)}=b_{sj},\qquad A_{(i,s),(p,s)}=a_{pi},
\]
with all entries not of the displayed form equal to \(0\). Thus \(L\) and \(A\) move the first coordinate forward along an arrow \(p\to i\), and \(N\) and \(B\) move the second coordinate backward along an arrow \(s\to j\). As linear maps, \(L,B\) are defined on \(\mathbb R^{\mathcal R}\) and \(N,A\) take values in \(\mathbb R^{\mathcal C}\).

**Lemma 3.5.** \(NL=AB\) for every choice of values.

*Proof.* Fix a column \((p,j)\in\mathcal R\) and a row \((i,s)\in\mathcal C\). In \((NL)_{(i,s),(p,j)}=\sum_{z\in Z}N_{(i,s),z}L_{z,(p,j)}\), a nonzero term needs \(z\) to have first coordinate \(i\) and second coordinate \(j\), so the sum is \(b_{sj}a_{pi}\) if \((i,j)\in Z\) and \(0\) otherwise. Likewise \((AB)_{(i,s),(p,j)}\) is \(a_{pi}b_{sj}\) if \((p,s)\in H\) and \(0\) otherwise. If the two members conflict, then \((i,j)\in Z\) and \((p,s)\in H\), and both entries equal \(a_{pi}b_{sj}\). If they do not conflict, \(p\not\to i\) or \(s\not\to j\), and \(a_{pi}b_{sj}=0\), so both entries vanish. \(\square\)

**Lemma 3.6.** Suppose that, for some choice of values, \(\operatorname{rank}L\ge\ell\), \(\operatorname{rank}N\ge t\) and \(\dim\ker A\ge k\). Then \(|\mathcal M|\le|Z|+|H|\).

*Proof.* Using rank–nullity for \(A\) and \(N\), and \(NL=AB\),
\[
|H|=\dim\ker A+\operatorname{rank}A\ge k+\operatorname{rank}(AB)=k+\operatorname{rank}(NL)\ge k+\operatorname{rank}L-\dim\ker N\ge k+\ell-(|Z|-t),
\]
because \(\operatorname{rank}(NL)=\dim\operatorname{im}L-\dim(\operatorname{im}L\cap\ker N)\). Hence \(k+\ell+t\le|Z|+|H|\). \(\square\)

### 3.4. Choosing the values

Two families of submatrices are needed.

*Supports of \(L\) and \(N\).* The entry \(L_{(i,j),(p,j)}\) can be nonzero only if \(p\to i\), that is, only if \((p,j)\) covers \((i,j)\); so \(L\) is supported on the edges of \(\Gamma_\alpha\), and by Lemmas 2.1 and 3.4, \(\operatorname{rank}L\le\ell\) for all values. Grouping rows and columns by their second coordinate makes \(L\) block diagonal, and within the block of a fixed \(j\) the entry at row \((i,j)\) and column \((p,j)\) is the variable \(a_{pi}\), different positions carrying different variables. The edges of \(\alpha\) join vertices in the same block, so the square submatrix of \(L\) with the rows and columns matched by \(\alpha\) satisfies Lemma 2.3(b), and its determinant \(\Lambda\) is a nonzero polynomial. In the same way, \(N^{\mathsf T}\) is supported on the edges of \(\Gamma_\beta\), so \(\operatorname{rank}N\le t\); grouping by the first coordinate \(i\), the square submatrix of \(N^{\mathsf T}\) on the vertices matched by \(\beta\) has a nonzero determinant polynomial \(\Upsilon\).

*Local matrices.* For every pair \((p,i)\) with \(p\to i\), let \(J_p=\{j:(p,j)\in\mathcal R\}\), \(S_i=\{s:(i,s)\in\mathcal C\}\), and
\[
D^{p,i}=(b_{sj})_{s\in S_i,\,j\in J_p},\qquad T^{p,i}=\{(s,j)\in S_i\times J_p:s\to j\}.
\]
The matrix \(D^{p,i}\) is supported on \(T^{p,i}\), and its entries at the positions of \(T^{p,i}\) are distinct variables, so every real matrix supported on \(T^{p,i}\) is a value of \(D^{p,i}\). Let \(\rho_{p,i}\) be the largest rank of such a matrix, and choose a \(\rho_{p,i}\times\rho_{p,i}\) submatrix whose determinant is nonzero at some value; that determinant \(\Delta_{p,i}\) is then a nonzero polynomial (the empty determinant \(1\) if \(\rho_{p,i}=0\)).

The product \(\Lambda\,\Upsilon\prod_{p\to i}\Delta_{p,i}\) is a nonzero polynomial in all the variables, because a product of nonzero polynomials is nonzero. By Lemma 2.2, we fix real values at which it does not vanish. At these values:

- \(\operatorname{rank}L=\ell\), and the columns of \(L\) indexed by \(R_\alpha\) form a basis of \(\operatorname{im}L\) (they are independent because \(\Lambda\ne0\), and there are \(\ell\ge\operatorname{rank}L\) of them);
- \(\operatorname{rank}N^{\mathsf T}=t\), and the columns of \(N^{\mathsf T}\) indexed by \(C_\beta\) form a basis of \(\operatorname{im}N^{\mathsf T}\);
- every \(D^{p,i}\) has the largest rank \(\rho_{p,i}\) among the real matrices supported on \(T^{p,i}\).

### 3.5. The kernels of \(B\) and \(N^{\mathsf T}\)

**Lemma 3.7.** At the fixed values, for every \(u\in\ker B\subseteq\mathbb R^{\mathcal R}\), every \(v\in\ker N^{\mathsf T}\subseteq\mathbb R^{\mathcal C}\) and every conflict between \((p,j)\in\mathcal R\) and \((i,s)\in\mathcal C\),
\[
u_{(p,j)}\,v_{(i,s)}=0 .
\]

*Proof.* Fix the pair \((p,i)\) of the conflict; then \(p\to i\). Let \(x=(u_{(p,j')})_{j'\in J_p}\) and \(y=(v_{(i,s')})_{s'\in S_i}\).

For \(s'\in S_i\), consider \(\sum_{j'\in J_p}b_{s'j'}x_{j'}\). If some \(j'\in J_p\) has \(s'\to j'\), then \((p,j')\) and \((i,s')\) conflict, so \((p,s')\in H\), and the sum is the \((p,s')\)-coordinate of \(Bu=0\), because the only columns of \(B\) in the row \((p,s')\) with nonzero entries are members \((p,j')\). If no such \(j'\) exists, every term vanishes. Hence \(D^{p,i}x=0\).

For \(j'\in J_p\), consider \(\sum_{s'\in S_i}b_{s'j'}y_{s'}\). If some \(s'\in S_i\) has \(s'\to j'\), the same conflict shows \((i,j')\in Z\), and the sum is the \((i,j')\)-coordinate of \(N^{\mathsf T}v=0\). Otherwise every term vanishes. Hence \((D^{p,i})^{\mathsf T}y=0\).

Since \(s\to j\), the position \((s,j)\) lies in \(T^{p,i}\), and Lemma 2.4 gives \(x_jy_s=0\). \(\square\)

Lemma 2.4 is applied to the single matrix \(D^{p,i}\) at the fixed values; the perturbation in its proof is only an argument and changes nothing.

### 3.6. The kernel of \(A\) and the end of the proof

Let \(r_1c_1,\dots,r_kc_k\) be the edges of \(\mathcal M\) between original vertices, with \(r_m\in\mathcal R\) and \(c_m\in\mathcal C\); each is a conflict. Since \(r_m\notin R_\alpha\) and the columns indexed by \(R_\alpha\) span \(\operatorname{im}L\), there is a vector
\[
u^m=e_{r_m}+\sum_{a\in R_\alpha}\lambda^m_ae_a\in\ker L .
\]
Likewise, since \(c_m\notin C_\beta\), there is \(v^m=e_{c_m}+\sum_{b\in C_\beta}\mu^m_be_b\in\ker N^{\mathsf T}\). The vector \(u^m\) has coordinate \(1\) at \(r_m\) and \(0\) at the other \(r_{m'}\), because \(R_\alpha\) contains none of them.

**Lemma 3.8.** The vectors \(Bu^1,\dots,Bu^k\) are linearly independent and lie in \(\ker A\). Hence \(\dim\ker A\ge k\).

*Proof.* By Lemma 3.5, \(ABu^m=NLu^m=0\). Every \(u\in\ker B\) satisfies \(u_{r_m}=u_{r_m}v^m_{c_m}=0\) by Lemma 3.7, applied to the conflict \(r_mc_m\). If \(\sum_m\theta_mBu^m=0\), then \(u=\sum_m\theta_mu^m\in\ker B\), and its coordinate at \(r_m\) is \(\theta_m\), so every \(\theta_m=0\). \(\square\)

*Proof of Theorem 3.1.* At the fixed values, \(\operatorname{rank}L=\ell\), \(\operatorname{rank}N=\operatorname{rank}N^{\mathsf T}=t\), and \(\dim\ker A\ge k\) by Lemma 3.8. Lemma 3.6 gives \(|\mathcal M|\le|Z|+|H|\). Theorem 1.2 provides a vertex cover \(K\) with \(|K|=|\mathcal M|\) and no isolated vertices, and Lemma 3.3 turns it into the required families. \(\square\)

## 4. Exercises

**4.1.** Let \(X=\{1,2\}\) with \(1\to2\) and \(2\to1\), \(\mathcal R=\{(1,1)\}\) and \(\mathcal C=\{(2,2)\}\). Find \(Z\), \(H\), the graph \(\Gamma\) and a maximum matching, and check that (3.1) is attained with equality by every valid choice of \(\mathcal R'\), \(\mathcal C'\).

**4.2.** Let \(X=\{p,s,i_1,i_2,j_1,j_2\}\) with the four arrows \(p\to i_1\), \(p\to i_2\), \(s\to j_1\), \(s\to j_2\), let \(\mathcal R=\{(p,j_1),(p,j_2)\}\) and \(\mathcal C=\{(i_1,s),(i_2,s)\}\). Show that every pair of a left and a right member conflicts, that \(|H|=1\) and \(|Z|=4\), and that every conflict-free choice deletes at least two members. Show that a choice deleting exactly two members leaves every point of \(Z\) covered, and conclude that the last term of (3.1) cannot be omitted.

**4.3.** Show that the hypothesis "largest rank on \(T\)" in Lemma 2.4 cannot be dropped: give a \(2\times2\) matrix \(D\) supported on \(T=\{1,2\}\times\{1,2\}\), vectors \(x\in\ker D\), \(y\in\ker D^{\mathsf T}\) and a position \((s,j)\) with \(x_jy_s\ne0\).

**4.4.** Show that \(\operatorname{rank}L\le\ell\) and \(\operatorname{rank}N\le t\) for every choice of values, so that the first two hypotheses of Lemma 3.6 can only hold with equality.

## 5. Solutions

**4.1.** The members \((1,1)\) and \((2,2)\) conflict, since \(1\to2\) and \(2\to1\); the shared point is \((2,1)\) and the opposite point \((1,2)\), so \(|Z|=|H|=1\). The left member covers \((2,1)\) and so does the right member, so \(\Gamma\) is the path \(z_L,\,c,\,r,\,z_R\), with maximum matching \(\{z_Lc,\,rz_R\}\) of size \(2=|Z|+|H|\). A conflict-free choice must delete \(r\) or \(c\); keeping one of them leaves \((2,1)\) covered, so the right side of (3.1) is \(1\) and exactly one member is deleted. Deleting both gives \(2\le1+1\), again with equality.

**4.2.** For \((p,j_a)\) and \((i_b,s)\): \(p\to i_b\) and \(s\to j_a\), so all four pairs conflict. The shared points are the four points \((i_b,j_a)\), and every opposite point is \((p,s)\). The conflicts form a complete bipartite graph between two left and two right members, and a conflict-free choice must delete both members on one side. If both right members are deleted, the left member \((p,j_a)\) covers \((i_1,j_a)\) and \((i_2,j_a)\), so all of \(Z\) is covered; symmetrically if both left members are deleted. For such a choice the right side of (3.1) without its last term would be \(|H|=1<2\). The construction of the proof yields here a cover containing all four original members, with \(4\le1+4\).

**4.3.** Take \(D=0\), \(x=e_1\), \(y=e_1\) and \((s,j)=(1,1)\). Here \(x_1y_1=1\). Adding \(\tau e_1e_1^{\mathsf T}\) raises the rank, as in the proof.

**4.4.** This is Lemma 2.1 applied to the supports of \(L\) and \(N^{\mathsf T}\), which consist of edges of \(\Gamma_\alpha\) and \(\Gamma_\beta\), together with Lemma 3.4: the largest matchings of these subgraphs have \(\ell\) and \(t\) edges.

## References

- [OpenAI-SN] OpenAI, *A proof of Seymour's second-neighborhood conjecture*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-proof-of-Seymours-second-neighborhood-conjecture-September-23-2026/paper.pdf
- [Edm] J. Edmonds, *Systems of distinct representatives and linear algebra*, Journal of Research of the National Bureau of Standards 71B (1967), 241–245. https://nvlpubs.nist.gov/nistpubs/jres/71B/jresv71Bn4p241_A1b.pdf
- [Kőn] D. Kőnig, *Gráfok és mátrixok*, Matematikai és Fizikai Lapok 38 (1931); the whole volume is freely available. https://real-j.mtak.hu/7307/
