# Weighted spanning trees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Choose a spanning tree of a finite connected graph at random, with probability proportional to the product of positive weights on its edges. How does the probability that a given edge belongs to the tree change when the weights are changed? This lesson proves a bound that depends neither on the graph nor on the weights: if the logarithms of all weights change by at most \(\varepsilon\), then every such probability changes by at most \(\varepsilon/2\). In September 2026 OpenAI released a proof that the free uniform spanning forest of every infinite connected graph is a factor of independent labels [OpenAI-F]; this bound is the estimate on which that proof rests.

- The weighted number of spanning trees is the determinant of the reduced weighted Laplacian (Theorem 3.1); the proof uses the formula of Cauchy and Binet (Lemma 2.1).
- The probability \(p_e\) that an edge \(e\) is in the tree, and the covariances of the indicators of two edges, are given by the inverse of this matrix (Proposition 4.2). The covariance of two different edges is never positive.
- Because every spanning tree has the same number of edges, the absolute values of the covariances of one edge with all edges add up to \(2p_e(1-p_e)\le\tfrac12\) (Theorem 5.1). This gives the bound for changes of the weights (Corollary 5.2).

The lesson follows [OpenAI-F, Section 2, the lemma on the response of weighted trees]; the determinant formulas are classical and go back to G. Kirchhoff. The lesson uses determinants and inverse matrices (core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40)).

## 1. Graphs, trees and incidence vectors

Let \(H\) be a finite graph with vertex set \(V\) and edge set \(E\); an edge is a set of two different vertices. A *cycle* is a closed walk of at least three edges that visits no vertex twice. A graph without cycles is a *forest*, and a connected forest is a *tree*. A *spanning tree* of \(H\) is a set \(T\subseteq E\) such that the graph \((V,T)\) is a tree. Let \(\mathcal T(H)\) be the set of the spanning trees of \(H\); it is not empty if \(H\) is connected. We use two standard facts.

- A tree with at least two vertices has at least two *leaves*, vertices that lie on exactly one edge: the two ends of a longest path are leaves.
- A tree with \(v\) vertices has \(v-1\) edges, by induction, removing a leaf with its edge. Hence a forest with \(v\) vertices and \(c\) connected components has \(v-c\) edges, and a forest \((V,F)\) with \(|F|=|V|-1\) is a tree.

Let \(H\) be connected with at least two vertices, and \(r=|V|-1\). Choose for every edge one of its two directions, and fix a vertex \(v_0\). For an edge \(f\) directed from \(u\) to \(w\), let \(a_f\) be the vector with a coordinate for every vertex other than \(v_0\), which is \(+1\) at \(w\), \(-1\) at \(u\), and \(0\) elsewhere; the coordinate of \(v_0\), if \(u\) or \(w\) is \(v_0\), is left out. These are the *reduced incidence vectors*; they have \(r\) coordinates.

**Lemma 1.1.** Let \(F\subseteq E\) with \(|F|=r\). The determinant of the matrix with the columns \(a_f\), \(f\in F\), is \(+1\) or \(-1\) if \(F\) is a spanning tree, and \(0\) otherwise.

**Proof.** If \(F\) is not a spanning tree, the graph \((V,F)\) is not a tree, so by the second fact it contains a cycle. Go once around the cycle and add the vectors \(a_f\) of its edges, with the sign \(+\) if the edge is traversed in its direction and \(-\) otherwise. Each vertex of the cycle is entered once and left once, so the sum is \(0\). The columns are linearly dependent, and the determinant is \(0\).

Let \(F\) be a spanning tree. We use induction on \(r\). For \(r=1\) the matrix has the one entry \(\pm1\). For \(r\ge2\) the tree has a leaf \(u\ne v_0\). The row of \(u\) has exactly one entry different from \(0\), namely \(\pm1\) in the column of the edge \(f_0\) at \(u\). Expanding the determinant along this row gives \(\pm\) the determinant of the matrix for the tree \(F\setminus\{f_0\}\) on \(V\setminus\{u\}\), with the same vertex \(v_0\). \(\blacksquare\)

## 2. The formula of Cauchy and Binet

**Lemma 2.1.** Let \(A\) be a matrix with \(r\) rows and \(n\) columns and \(B\) a matrix with \(n\) rows and \(r\) columns. For a set \(F\) of \(r\) column indices let \(A_F\) be the square matrix of the columns of \(A\) with index in \(F\), and \(B^F\) the square matrix of the rows of \(B\) with index in \(F\). Then
\[
\det(AB)=\sum_{|F|=r}\det(A_F)\,\det(B^F).
\]

**Proof.** Let \(A_1,\dots,A_n\) be the columns of \(A\). The column \(k\) of \(AB\) is \(\sum_jb_{jk}A_j\). The determinant is linear in each column, so
\[
\begin{aligned}
&\det(AB)\\
&\ =\sum_{j_1,\dots,j_r}b_{j_11}\cdots b_{j_rr}\,\det(A_{j_1},\dots,A_{j_r}).
\end{aligned}
\]
The terms in which two of the indices are equal vanish. In the others, \(j_1,\dots,j_r\) are the elements of a set \(F\) in some order, that is \(j_k=\sigma(k)\) for a bijection \(\sigma\) from \(\{1,\dots,r\}\) to \(F\); and \(\det(A_{\sigma(1)},\dots,A_{\sigma(r)})\) is \(\det(A_F)\) times the sign of the permutation that sorts the indices. Summing over \(\sigma\) for fixed \(F\) gives \(\det(A_F)\) times the sum that defines \(\det(B^F)\). \(\blacksquare\)

## 3. The matrix-tree theorem

Give every edge \(f\) a weight \(c_f>0\). The *reduced weighted Laplacian* is the symmetric matrix with \(r\) rows and columns
\[
L=\sum_{f\in E}c_f\,a_fa_f^{\mathsf T},
\]
where \(a_fa_f^{\mathsf T}\) is the matrix with the entries \((a_f)_x(a_f)_y\).

**Theorem 3.1.** \(\det L=\sum_{T\in\mathcal T(H)}\prod_{f\in T}c_f\). In particular \(\det L>0\).

**Proof.** Let \(A\) be the matrix with the columns \(a_f\), \(f\in E\), and \(B\) the matrix with the rows \(c_fa_f^{\mathsf T}\). Then \(L=AB\), and \(\det(B^F)=\det(A_F)\prod_{f\in F}c_f\). By Lemma 2.1,
\[
\det L=\sum_{|F|=r}\det(A_F)^2\prod_{f\in F}c_f,
\]
and by Lemma 1.1, \(\det(A_F)^2\) is \(1\) if \(F\) is a spanning tree and \(0\) otherwise. A connected graph has a spanning tree, so the sum is positive. \(\blacksquare\)

We write \(Z\) for this number, the *weighted number of spanning trees*. Neither \(Z\) nor the results below depend on the choice of the directions and of \(v_0\): the right side of Theorem 3.1 does not.

## 4. The random spanning tree

For \(h\in\mathbb R^E\) let \(c_f=e^{h_f}\). Let \(T\) be a random spanning tree with
\[
\begin{gathered}
\mathbb P_h(T=T_0)=\frac1{Z(h)}\prod_{f\in T_0}c_f,\\
Z(h)=\sum_{T_0\in\mathcal T(H)}\ \prod_{f\in T_0}c_f .
\end{gathered}
\]
For \(h=0\) this is the *uniform spanning tree*. Let \(\xi_e\) be \(1\) if \(e\in T\) and \(0\) otherwise, and \(p_e(h)=\mathbb E_h\xi_e\) the probability that \(e\) belongs to \(T\). The covariance of two random variables is \(\operatorname{Cov}(X,Y)=\mathbb E(XY)-\mathbb E X\,\mathbb E Y\).

**Lemma 4.1.** For all edges \(e,f\),
\[
\begin{gathered}
\frac{\partial\log Z}{\partial h_e}=p_e,\\
\frac{\partial p_e}{\partial h_f}=\operatorname{Cov}_h(\xi_e,\xi_f).
\end{gathered}
\]

**Proof.** The weight \(W(T_0)=\exp(\sum_{f\in T_0}h_f)\) has the derivative \(\xi_e(T_0)W(T_0)\) with respect to \(h_e\). So
\[
\frac{\partial Z}{\partial h_e}=\sum_{T_0}\xi_e(T_0)\,W(T_0)=Z\,p_e .
\]
Differentiating \(p_e=Z^{-1}\sum_{T_0}\xi_e(T_0)W(T_0)\) with respect to \(h_f\) gives \(\mathbb E_h(\xi_e\xi_f)-p_ep_f\). \(\blacksquare\)

**Proposition 4.2.** Let \(L=L(h)\) be the reduced weighted Laplacian for the weights \(c_f=e^{h_f}\). Then

1. \(p_e=c_e\,a_e^{\mathsf T}L^{-1}a_e\) for every edge \(e\);
2. for all edges \(e\ne f\),
\[
\begin{aligned}
\operatorname{Cov}_h(\xi_e,\xi_f)&=-c_ec_f\,\bigl(a_e^{\mathsf T}L^{-1}a_f\bigr)^2\\
&\le0 .
\end{aligned}
\]

**Proof.** (1) For vectors \(x,y\) with \(r\) coordinates, \(\det(I+xy^{\mathsf T})=1+y^{\mathsf T}x\): this is clear for \(x=0\); otherwise, in a basis that starts with \(x\), the map \(z\mapsto z+x\,(y^{\mathsf T}z)\) has a triangular matrix with the diagonal entries \(1+y^{\mathsf T}x,1,\dots,1\). Hence for a real number \(\delta\)
\[
\begin{aligned}
&\det(L+\delta\,a_ea_e^{\mathsf T})\\
&\quad=\det L\cdot\bigl(1+\delta\,a_e^{\mathsf T}L^{-1}a_e\bigr).
\end{aligned}
\]
The left side is, by Theorem 3.1, the weighted number of spanning trees when the weight \(c_e\) is replaced by \(c_e+\delta\). So \(\partial Z/\partial c_e=Z\,a_e^{\mathsf T}L^{-1}a_e\), and by Lemma 4.1
\[
\begin{aligned}
p_e=\frac{\partial\log Z}{\partial h_e}&=c_e\,\frac{\partial\log Z}{\partial c_e}\\
&=c_e\,a_e^{\mathsf T}L^{-1}a_e .
\end{aligned}
\]

(2) The entries of \(L^{-1}\) are quotients of polynomials in the weights, so they are differentiable. Differentiating \(LL^{-1}=I\) with respect to \(h_f\), where \(\partial L/\partial h_f=c_fa_fa_f^{\mathsf T}\), gives
\[
\frac{\partial L^{-1}}{\partial h_f}=-c_f\,L^{-1}a_fa_f^{\mathsf T}L^{-1}.
\]
For \(f\ne e\) the factor \(c_e\) in (1) does not depend on \(h_f\), so by Lemma 4.1
\[
\begin{aligned}
&\operatorname{Cov}_h(\xi_e,\xi_f)=\frac{\partial p_e}{\partial h_f}\\
&\quad=-c_ec_f\,(a_e^{\mathsf T}L^{-1}a_f)(a_f^{\mathsf T}L^{-1}a_e),
\end{aligned}
\]
and the two factors in brackets are equal because \(L^{-1}\) is symmetric. \(\blacksquare\)

So the presence of one edge in the random spanning tree makes the presence of every other edge less likely, or leaves it unchanged, for all weights.

## 5. The response identity

**Theorem 5.1.** For every \(h\in\mathbb R^E\) and every edge \(e\),
\[
\sum_{f\in E}\Bigl|\frac{\partial p_e}{\partial h_f}\Bigr|=2\,p_e(1-p_e)\le\frac12 .
\]

**Proof.** Every spanning tree has exactly \(r\) edges, so \(\sum_f\xi_f=r\) is constant, and
\[
\begin{aligned}
\sum_{f\in E}\operatorname{Cov}_h(\xi_e,\xi_f)&=\operatorname{Cov}_h\Bigl(\xi_e,\sum_f\xi_f\Bigr)\\
&=0 .
\end{aligned}
\]
The term with \(f=e\) is the variance \(p_e-p_e^2\). The other terms are not positive by Proposition 4.2, so the sum of their absolute values is \(p_e(1-p_e)\). With Lemma 4.1 the sum of all absolute values is \(2p_e(1-p_e)\), and \(p(1-p)\le\tfrac14\) for \(0\le p\le1\). \(\blacksquare\)

**Corollary 5.2.** For all \(h,h'\in\mathbb R^E\) and every edge \(e\),
\[
|p_e(h)-p_e(h')|\le\frac12\max_{f\in E}|h_f-h'_f| .
\]

**Proof.** Let \(\varphi(\tau)=p_e(h+\tau(h'-h))\) for \(0\le\tau\le1\). Then \(\varphi'(\tau)\) is the sum of \(\tfrac{\partial p_e}{\partial h_f}\,(h'_f-h_f)\) over \(f\), taken at the point \(h+\tau(h'-h)\). By Theorem 5.1 its absolute value is at most \(\tfrac12\max_f|h'_f-h_f|\), and \(p_e(h')-p_e(h)=\int_0^1\varphi'(\tau)\,d\tau\). \(\blacksquare\)

The constant \(\tfrac12\) does not depend on the graph, on the number of edges, or on the weights. For an edge \(e\) whose removal disconnects the graph, \(p_e=1\) and all the derivatives vanish. The same bound holds if only some of the \(h_f\) are changed, with the maximum over those edges.

**Example 5.3.** Let \(H\) be a triangle with the edges \(1,2,3\) and the weights \(c_1,c_2,c_3\). The spanning trees are the three pairs of edges, so \(Z=c_1c_2+c_1c_3+c_2c_3\) and \(p_1=c_1(c_2+c_3)/Z\). For equal weights \(p_1=\tfrac23\), the probability that both edges \(1\) and \(2\) are in the tree is \(\tfrac13\), and \(\operatorname{Cov}(\xi_1,\xi_2)=\tfrac13-\tfrac49=-\tfrac19\). The sum of the absolute values in Theorem 5.1 is \(\tfrac29+\tfrac19+\tfrac19=\tfrac49\), which is \(2\cdot\tfrac23\cdot\tfrac13\).

## 6. Exercises

**6.1.** Let \(H\) be a cycle with \(n\ge3\) edges, with equal weights. Compute \(p_e\) and the covariances, and check Theorem 5.1.

**6.2.** For the triangle with the weights \(c_1,c_2,c_3\), compute \(L\) for a choice of directions and of \(v_0\), and check Theorem 3.1 and Proposition 4.2(1) for the edge \(1\).

**6.3.** Let a random subset of \(E\) contain each edge independently with probability \(\tfrac12\). Compute the sum of the absolute values of the covariances of the indicator of one edge with those of all edges, and compare it with \(2p(1-p)\). Give a random subset of \(E\) for which this sum is \(|E|/4\). Which two properties of spanning trees does the proof of Theorem 5.1 use?

**6.4.** Let \(e\) be an edge of \(H\) and \(h'\) obtained from \(h\) by adding a number \(s\) to \(h_e\) only. Show that \(p_e(h')\) is \(\dfrac{p\,e^s}{1-p+p\,e^s}\) with \(p=p_e(h)\), and compare the derivative at \(s=0\) with Theorem 5.1.

## 7. Solutions

**6.1.** The spanning trees are the \(n\) sets of \(n-1\) edges. So \(p_e=\tfrac{n-1}n\), and for \(e\ne f\) the probability that both are in the tree is \(\tfrac{n-2}n\). The covariance is \(\tfrac{n-2}n-\tfrac{(n-1)^2}{n^2}=-\tfrac1{n^2}\). The sum of the absolute values is \(\tfrac{n-1}{n^2}+\tfrac{n-1}{n^2}\), the first term from \(f=e\) and the second from the other \(n-1\) edges. This is \(2\cdot\tfrac{n-1}n\cdot\tfrac1n\).

**6.2.** Let the vertices be \(v_0,v_1,v_2\), the edge \(1\) from \(v_0\) to \(v_1\), the edge \(2\) from \(v_1\) to \(v_2\), the edge \(3\) from \(v_2\) to \(v_0\). In the coordinates \((v_1,v_2)\): \(a_1=(1,0)\), \(a_2=(-1,1)\), \(a_3=(0,-1)\). So
\[
L=\begin{pmatrix}c_1+c_2&-c_2\\-c_2&c_2+c_3\end{pmatrix},
\]
with \(\det L=c_1c_2+c_1c_3+c_2c_3\). The entry of \(L^{-1}\) at the place \((v_1,v_1)\) is \((c_2+c_3)/\det L\), so \(c_1a_1^{\mathsf T}L^{-1}a_1=c_1(c_2+c_3)/Z=p_1\).

**6.3.** For independent edges all covariances of different edges are \(0\), and the variance is \(\tfrac14\). So the sum is \(\tfrac14\), while \(2p(1-p)=\tfrac12\): the identity of Theorem 5.1 fails, because the number of chosen edges is not constant. For the second question take the random set that is empty or all of \(E\), each with probability \(\tfrac12\): every covariance is \(\tfrac14\), and the sum is \(|E|/4\). The proof of Theorem 5.1 uses that the covariances of different edges are not positive, and that the number of edges of the random set is constant.

**6.4.** Let \(Z_1\) be the weighted number of the spanning trees that contain \(e\) and \(Z_0\) that of the others, for \(h\); so \(p=Z_1/(Z_0+Z_1)\). For \(h'\), \(Z_1\) is multiplied by \(e^s\) and \(Z_0\) is unchanged, so \(p_e(h')=Z_1e^s/(Z_0+Z_1e^s)\); dividing by \(Z_0+Z_1\) gives the formula. Its derivative at \(s=0\) is \(p(1-p)\), the term with \(f=e\) in Theorem 5.1.

## References

- [OpenAI-F] OpenAI, *The free uniform spanning forest is a factor of IID*, OpenAI Math Release preprint, 25 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/The-free-uniform-spanning-forest-is-a-factor-of-IID-September-25-2026
