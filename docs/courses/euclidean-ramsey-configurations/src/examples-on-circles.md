# Examples on circles

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

With the classification theorem proved in [Equal endpoints](equal-endpoints.md), whether a finite set is Ramsey becomes a question about its coordinate field. This lesson answers it for several families. Subsets of finite transitive sets are Ramsey; so is every set of at most five points on a circle, which includes kites that embed in no finite transitive set, against a conjecture of Leader, Russell and Walters. On the other side, nine points of a circle in general position, and twelve points forming three rotated squares, are not Ramsey, although they lie on a sphere.

The notation of the first lesson is used: for \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\) with \(s\ge2\) and affine span \(\mathbb R^d\), \(p_i=(1,a_i)\), \(F\) is the field of coordinates, \(B=F\otimes_{\mathbb Q}F\), and the *matrix condition* asks for \(P\in\mathrm{Mat}_{d+1}(B)\) with \((p_i\otimes1)^{\mathsf T}P(1\otimes p_i)=0\) for all \(i\) and \(m_F(P_{\alpha\beta})=\delta_{\alpha\beta}\) for \(1\le\alpha,\beta\le d\). By the classification, it holds exactly for Ramsey sets. A finite set is *transitive* if its distance-preserving permutations act transitively on it, and *subtransitive* if it is congruent to a subset of a finite transitive set.

## 1. Transitive sets

**Corollary 1.1.** Every nonempty subset of a finite transitive set is Ramsey.

*Proof.* Singletons are Ramsey. Let \(A\) have \(s\ge2\) points and affine span \(\mathbb R^d\), and let \(a_i\mapsto y_i\) be a distance-preserving map into a finite transitive set \(Y\subset\mathbb R^n\) with group \(H\) of distance-preserving permutations. For \(h\in H\), the points \(h(y_i)\) form a congruent copy of \(A\), so by Lemma 1.1 of [A colouring obstruction](a-colouring-obstruction.md) there is an affine isometric map \(\mathbb R^d\to\mathbb R^n\) with \(a_i\mapsto h(y_i)\). Let \(w_{hj}\in W=\mathbb R\times\mathbb R^d\) be its \(j\)th coordinate, an affine function with \(e_i(w_{hj})=(h(y_i))_j\); the gradients of \(w_{h1},\dots,w_{hn}\) have Gram matrix \(I_d\). Let \(c_{hj}=((h(y_1))_j,0)\), a constant function, and put
\[
\begin{aligned}
T=\frac1{|H|}\sum_{h\in H}\sum_{j=1}^n\bigl({}&w_{hj}\otimes w_{hj}\\
&-c_{hj}\otimes c_{hj}\bigr).
\end{aligned}
\]
It is symmetric and \(G(T)=I_d\). For each \(i\), the list \((h(y_i))_{h\in H}\) contains every point of \(Y\) exactly \(|H|/|Y|\) times, by transitivity. So \(\sum_{h,j}(h(y_i))_j\otimes(h(y_i))_j\) does not depend on \(i\), and equals \(\sum_{h,j}(h(y_1))_j\otimes(h(y_1))_j\). Hence \((e_i\otimes e_i)(T)=0\), the tensor condition holds, and the classification gives the Ramsey property. \(\square\)

Regular polygons, the vertex sets of regular polytopes, and products of transitive sets are transitive, so all their subsets are Ramsey.

## 2. Quadratic interpolation and five points on a circle

**Proposition 2.1.** Let \(A\subset\mathbb R^d\) lie on a sphere and affinely span \(\mathbb R^d\). If the \(s\) vectors \((p_{i\alpha}p_{i\beta})_{0\le\alpha,\beta\le d}\in F^{(d+1)^2}\) are linearly independent over \(F\), then \(A\) is Ramsey.

*Proof.* Let \(N=(d+1)^2\) and view matrices as vectors in \(F^N\) or \(B^N\). The sphere through \(A\), with centre \(c\) and radius \(\rho\), gives the real matrix \(H\) with spatial block \(I_d\), entries \(-c_\alpha\) at the positions \((0,\alpha)\) and \((\alpha,0)\), and \(\|c\|^2-\rho^2\) at \((0,0)\); it satisfies \(p_i^{\mathsf T}Hp_i=\|a_i-c\|^2-\rho^2=0\) for all \(i\). These requirements are linear equations with coefficients in \(F\); having a real solution, they have a solution \(h\in F^N\) by Gaussian elimination.

Let \(D\in\mathrm{Mat}_{s\times N}(B)\) have the entries \(p_{i\alpha}\otimes p_{i\beta}\), so that the evaluation equations of the matrix condition read \(D\,P=0\). Lift \(h\) to \(b\in B^N\) by \(x\mapsto x\otimes1\). Applying \(m_F\) entrywise to \(D\) gives the matrix of the vectors in the hypothesis, so some \(s\) columns of \(D\) form a square matrix \(M\) with \(\delta=m_F(\det M)=\det m_F(M)\ne0\). Let \(\iota:B^s\to B^N\) put a vector into these columns, so that \(D\iota=M\). With the adjugate, \(M\,\mathrm{adj}(M)=(\det M)I\), so
\[
z=(\det M)\,b-\iota\,\mathrm{adj}(M)\,D\,b
\]
satisfies \(Dz=(\det M)Db-(\det M)Db=0\). Since \(m_F(D)\,h=0\), applying \(m_F\) gives \(m_F(z)=\delta h\). Then \(P=(\delta^{-1}\otimes1)z\) satisfies the matrix condition, since its multiplied spatial block is that of \(h\). \(\square\)

**Corollary 2.2.** Every nonempty set of at most five points on a circle is Ramsey. In particular every cyclic quadrilateral is Ramsey.

*Proof.* Work in the plane of the circle and add points of the circle until there are five, \(a_1,\dots,a_5\). No three points of a circle are collinear. For each \(i\), divide the other four points into two pairs and multiply the equations of the two lines through the pairs; this quadratic polynomial has coefficients in \(F\), vanishes at the other four points, and does not vanish at \(a_i\). So the map that sends a quadratic polynomial \(p^{\mathsf T}Hp\) with coefficients in \(F\) to its values at the five points is onto \(F^5\), and its five rows, which are the vectors of Proposition 2.1, are linearly independent. The five points lie on a circle and span the plane, so they form a Ramsey set, and so does every nonempty subset (Exercise 4.1 of the first lesson). \(\square\)

The interpolation by products of two line equations also appears in the appendix of [Pal], in the proof of its Theorem A.2.

## 3. Kites that embed in no transitive set

Leader, Russell and Walters conjectured that the Ramsey sets are exactly the subtransitive sets [LRW-T], and that the kites below are not Ramsey [LRW-K]. They proved that these kites are not subtransitive; that proof is reproduced here in a form that needs only traces and convexity.

**Lemma 3.1.** Let \(A_1,A_2,A_3\) be orthogonal \(n\times n\) matrices generating a finite group \(\Gamma\), and put
\[
\begin{aligned}
P(\alpha,\beta)=\det\bigl({}&\alpha A_1+\beta A_2\\
&+(1-\alpha-\beta)A_3-I\bigr).
\end{aligned}
\]
(a) \(P\) is a polynomial in \(\alpha,\beta\) whose coefficients are algebraic numbers.
(b) If the only vector fixed by all of \(\Gamma\) is \(0\), then for every real \(\alpha\ne0,1\) the polynomial \(P(\alpha,\cdot)\) is not identically zero.

*Proof.* (a) For an \(n\times n\) matrix \(L\), the coefficients of its characteristic polynomial, and in particular \(\det L\), are polynomials with rational coefficients in \(\mathrm{tr}(L),\mathrm{tr}(L^2),\dots,\mathrm{tr}(L^n)\), by Newton's identities. For \(L=\alpha A_1+\beta A_2+(1-\alpha-\beta)A_3-I\), each \(\mathrm{tr}(L^k)\) is a polynomial in \(\alpha,\beta\) whose coefficients are integer combinations of traces of products of the \(A_j\) and \(I\), that is, of traces of elements of \(\Gamma\). An element of the finite group \(\Gamma\) has finite order, so its complex eigenvalues are roots of unity, and its trace is a sum of roots of unity, an algebraic number.

(b) Fix \(\alpha\ne0,1\). It suffices to find one \(\beta\) for which no \(w\ne0\) satisfies \(Lw=0\), that is,
\[
w=\alpha A_1w+\beta A_2w+(1-\alpha-\beta)A_3w .
\]
The vectors \(A_jw\) have the same length as \(w\). Recall that if a vector \(x\) is a combination \(\sum\lambda_jx_j\) with positive \(\lambda_j\) of vectors with \(\|x_j\|=\|x\|/\sum_j\lambda_j\), then all \(x_j\) equal \(x/\sum_j\lambda_j\), by strict convexity of the Euclidean norm.

- If \(0<\alpha<1\), take \(\beta=(1-\alpha)/2\): \(w\) is a convex combination of \(A_1w,A_2w,A_3w\) with positive weights, so \(A_jw=w\) for all \(j\).
- If \(\alpha<0\), take \(\beta=\alpha\): the equation says that \((1-2\alpha)A_3w\) equals \((-\alpha)A_1w+(-\alpha)A_2w+w\), a combination with positive coefficients adding up to \(1-2\alpha\); so \(A_1w=A_2w=w=A_3w\).
- If \(\alpha>1\), take \(\beta=(1-\alpha)/2<0\): the equation becomes \(\alpha A_1w=w+\frac{\alpha-1}2A_2w+\frac{\alpha-1}2A_3w\), with positive coefficients on the right adding up to \(\alpha\); so \(w=A_2w=A_3w=A_1w\).

In each case \(w\) is fixed by the generators, hence by \(\Gamma\), so \(w=0\). \(\square\)

**Theorem 3.2** (Leader, Russell and Walters [LRW-K]). Let \(x,y,z,w\) be four distinct points on a circle with
\[
w=z+\alpha(x-z)+\beta(y-z),
\]
where \(\alpha\ne1\) and \(\beta\) is transcendental over \(\mathbb Q(\alpha)\). Then \(\{x,y,z,w\}\) is not subtransitive.

*Proof.* Suppose the four points lie in a finite transitive set \(Y\). Translate so that the centroid of \(Y\) is the origin. A distance-preserving permutation of \(Y\) extends to an affine isometry of its affine span (Lemma 1.1 of the second lesson) that fixes the centroid, so the group of such permutations acts on the span \(V\) of \(Y\) by orthogonal maps. Choose elements \(A_1,A_2,A_3\) of it mapping \(w\) to \(x,y,z\), and let \(\Gamma\) be the group they generate. Then
\[
\begin{aligned}
w&=A_3w+\alpha(A_1w-A_3w)\\
&\quad+\beta(A_2w-A_3w).
\end{aligned}
\]
If \(\alpha=0\), the points \(w,z,y\) would be collinear, which is impossible for three distinct points of a circle; so \(\alpha\ne0,1\).

Let \(V_0\) be the subspace of vectors fixed by \(\Gamma\), and \(V_1\) its orthogonal complement, which is invariant, because the maps are orthogonal. Project the relation to \(V_1\). If the projections of \(x,y,z,w\) to \(V_1\) were all equal, the four points would differ only in \(V_0\); but on \(V_0\) the maps \(A_j\) are the identity, so the components in \(V_0\) of \(x=A_1w\), \(y\), \(z\) and \(w\) are equal, and the points would coincide. If the projection \(w_1\) of \(w\) to \(V_1\) were zero, the projections \(A_jw_1\) of \(x,y,z\) would be zero as well; so \(w_1\ne0\). It satisfies the relation with the restrictions of \(A_1,A_2,A_3\) to \(V_1\), which fix no nonzero vector. In an orthonormal basis of \(V_1\), Lemma 3.1 gives a polynomial \(P\) with algebraic coefficients, \(P(\alpha,\beta)=0\), and \(P(\alpha,\cdot)\ne0\). So \(\beta\) is a root of a nonzero polynomial with coefficients algebraic over \(\mathbb Q(\alpha)\), hence algebraic over \(\mathbb Q(\alpha)\), a contradiction. \(\square\)

**Corollary 3.3.** For every transcendental \(a\in(-1,1)\), the kite
\[
\begin{aligned}
K_a=\bigl\{{}&(-1,0),(1,0),\\
&(a,\sqrt{1-a^2}),(a,-\sqrt{1-a^2})\bigr\}
\end{aligned}
\]
is Ramsey and not subtransitive.

*Proof.* It is a cyclic quadrilateral, so it is Ramsey by Corollary 2.2. Take \(z=(-1,0)\), \(y=(1,0)\), \(x=(a,\sigma)\) and \(w=(a,-\sigma)\) with \(\sigma=\sqrt{1-a^2}>0\). Comparing second coordinates in \(w-z=\alpha(x-z)+\beta(y-z)\) gives \(\alpha=-1\), and then the first coordinates give \(\beta=a+1\), which is transcendental over \(\mathbb Q(\alpha)=\mathbb Q\). Theorem 3.2 applies. \(\square\)

So a Ramsey set need not be subtransitive, and the kites \(K_a\) are Ramsey: both conjectures of Leader, Russell and Walters mentioned above fail.

## 4. Nine points on a circle

**Proposition 4.1.** Let \(t_1,\dots,t_9\) be real numbers that are algebraically independent over \(\mathbb Q\), and
\[
a_i=\Bigl(\frac{1-t_i^2}{1+t_i^2},\frac{2t_i}{1+t_i^2}\Bigr)\qquad(1\le i\le9).
\]
These nine points lie on the unit circle and do not form a Ramsey set.

*Proof.* The points are distinct, since \(t_i=(a_i)_2/(1+(a_i)_1)\), and they span the plane. Their coordinate field is \(F=\mathbb Q(t_1,\dots,t_9)\), a field of rational functions. Then \(B=F\otimes F\) is the ring obtained from the polynomial ring \(\mathbb Q[T_1,\dots,T_9,U_1,\dots,U_9]\) by inverting the nonzero polynomials in the \(T\)'s alone and those in the \(U\)'s alone; in particular it is contained in the field \(\mathbb Q(T,U)\) of rational functions in eighteen variables, with \(t_i\otimes1=T_i\) and \(1\otimes t_i=U_i\).

Put \(\pi(t)=\bigl(1,\frac{1-t^2}{1+t^2},\frac{2t}{1+t^2}\bigr)\). The nine evaluation equations of the matrix condition have, over \(\mathbb Q(T,U)\), the \(9\times9\) coefficient matrix \(D\) with rows \(\bigl(\pi_\alpha(T_i)\pi_\beta(U_i)\bigr)_{0\le\alpha,\beta\le2}\). We claim \(\det D\ne0\). Evaluate the rational function \(\det D\) at the point where the nine pairs \((T_i,U_i)\) run through \(\{0,1,-1\}^2\); no denominator vanishes there. The evaluated matrix is the Kronecker product \(C\otimes C\) of
\[
C=\begin{pmatrix}1&1&0\\1&0&1\\1&0&-1\end{pmatrix},\qquad\det C=2,
\]
whose rows are \(\pi(0),\pi(1),\pi(-1)\). Its determinant is \((\det C)^3(\det C)^3=64\ne0\). So \(D\) is invertible over \(\mathbb Q(T,U)\), and the only solution \(P\) of the evaluation equations over \(B\subseteq\mathbb Q(T,U)\) is \(P=0\), whose multiplied spatial block is not \(I_2\). By the classification, the set is not Ramsey. \(\square\)

A seven-point subset of a circle that is not Ramsey had been found earlier, in a paper by Pálvölgyi that attributes its construction and proofs to ChatGPT [Pal]; it disproved the conjecture that every set on a sphere is Ramsey.

## 5. Three rotated squares

**Proposition 5.1.** Let
\[
\begin{gathered}
t=\sum_{m=1}^\infty10^{-m!},\\
u=\frac{1-t^2}{1+t^2},\qquad v=\frac{2t}{1+t^2},
\end{gathered}
\]
let \(Q_0=\{(\pm1,0),(0,\pm1)\}\), \(R_+=\begin{pmatrix}u&-v\\v&u\end{pmatrix}\) and \(R_-=R_+^{\mathsf T}\). Then \(X=R_+Q_0\cup R_-Q_0\cup Q_0\) is a set of twelve points on the unit circle that is not Ramsey.

*Proof.* *The number \(t\).* The partial sums \(t_m=p_m/q_m\), with \(q_m=10^{m!}\), satisfy \(0<t-t_m<2q_m^{-(m+1)}\), since the tail is at most \(10^{-(m+1)!}(1+10^{-1}+10^{-2}+\cdots)\). If \(t\) were algebraic, let \(P\in\mathbb Z[x]\) be irreducible of degree \(d\ge1\) with \(P(t)=0\). Then \(P(t_m)\ne0\) (for \(d=1\) because \(t_m\ne t\), for \(d\ge2\) because \(P\) has no rational root), so \(|P(t_m)|\ge q_m^{-d}\), as \(q_m^dP(t_m)\) is a nonzero integer. With \(C\ge1\) bounding \(|P'|\) on \([0,1]\), \(q_m^{-d}\le|P(t_m)-P(t)|\le2Cq_m^{-(m+1)}\), which fails for large \(m\). So \(t\) is transcendental, and \(0.11<t<0.12\).

*The set.* \(R_\pm\) are the rotations by \(\pm\theta\) with \(\theta=2\arctan t\in(0,\pi/4)\), so the three squares are disjoint and \(X\) has twelve points on the unit circle; \(Q_0\) spans the plane. The coordinates of \(X\) are \(0,\pm1,\pm u,\pm v\), and \(t=v/(1+u)\), so the coordinate field is \(F=\mathbb Q(t)\), a field of rational functions in \(t\).

*A derivation.* On \(F\) define \(\partial=\frac{1+t^2}2\frac d{dt}\). Then \(\partial u=-v\) and \(\partial v=u\), so with \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) we get \(\partial R_+=R_+J\) and \(\partial R_-=-R_-J\). Label the points \(x_{\epsilon,q}=R_\epsilon q\) for \(\epsilon\in\{+,-,0\}\) (with \(R_0=I\)) and \(q\in Q_0\), give them weights \(\beta_{\pm,q}=1\) and \(\beta_{0,q}=-2\), and put \(p=(1,x)\). Using \(\sum_{q\in Q_0}q=0\), \(\sum_{q\in Q_0}qq^{\mathsf T}=2I\), \(RJR^{\mathsf T}=J\) for rotations \(R\), and \(JJ^{\mathsf T}=I\),
\[
\begin{gathered}
\sum_i\beta_ip_ip_i^{\mathsf T}=0,\qquad\sum_i\beta_i(\partial p_i)p_i^{\mathsf T}=0,\\
\sum_i\beta_i(\partial p_i)(\partial p_i)^{\mathsf T}=\begin{pmatrix}0&0\\0&4I\end{pmatrix}.
\end{gathered}
\]
For instance, the spatial block of the first sum is \(2(1+1-2)I=0\); that of the second is \(2J-2J+0=0\); that of the third is \(2I+2I+0=4I\). The other blocks vanish because \(\sum_qq=0\) and \(\partial\) kills constants.

*The obstruction.* The map \(\Phi:F\otimes F\to F\), \(\Phi(a\otimes b)=(\partial a)(\partial b)\), is well defined, since it is bilinear. For \(P\in\mathrm{Mat}_3(B)\) and a pure tensor \(a\otimes b\) in position \((\alpha,\beta)\), the term \(p_{i\alpha}a\otimes b\,p_{i\beta}\) of the evaluation at \(x_i\) has
\[
\begin{aligned}
\Phi={}&ab\,\partial p_{i\alpha}\,\partial p_{i\beta}+a\,\partial b\,\partial p_{i\alpha}\,p_{i\beta}\\
&+\partial a\,b\,p_{i\alpha}\,\partial p_{i\beta}+\partial a\,\partial b\,p_{i\alpha}p_{i\beta}.
\end{aligned}
\]
Summing with the weights \(\beta_i\), the last three terms vanish by the first two identities, and the first gives the third. So
\[
\begin{aligned}
&\sum_i\beta_i\,\Phi\bigl((p_i\otimes1)^{\mathsf T}P(1\otimes p_i)\bigr)\\
&\quad=4\bigl(m_F(P_{11})+m_F(P_{22})\bigr).
\end{aligned}
\]
A matrix satisfying the matrix condition would make the left side \(0\) and the right side \(8\). So \(X\) is not Ramsey. \(\square\)

## 6. Exercises

**6.1** (easy). Show that the vertex set of a regular polygon is transitive. Deduce from Corollary 2.2 that every triangle, that is, every set of three points not on a line, is Ramsey.

**6.2** (medium). Verify \(\partial u=-v\), \(\partial v=u\) and \(\partial R_+=R_+J\) in Proposition 5.1.

**6.3** (medium). Show that the matrix \(C\otimes C\) in Proposition 4.1 has determinant \(64\), using \(\det(X\otimes Y)=(\det X)^3(\det Y)^3\) for \(3\times3\) matrices, or directly from \(C\otimes C=(C\otimes I)(I\otimes C)\).

**6.4** (medium). Let \(a\in(-1,1)\) be algebraic. Show that Corollary 3.3 still makes \(K_a\) Ramsey, and explain why Theorem 3.2 says nothing about subtransitivity in this case.

## 7. Solutions

**6.1.** Rotations by multiples of \(2\pi/m\) about the centre permute the vertices transitively. Three points not on a line lie on their circumscribed circle, and three points of a circle are at most five points of it, so Corollary 2.2 applies. This is the theorem of Frankl and Rödl that all triangles are Ramsey [FR].

**6.2.** \(\frac d{dt}u=\frac{-4t}{(1+t^2)^2}\) and \(\frac d{dt}v=\frac{2(1-t^2)}{(1+t^2)^2}\); multiplying by \(\frac{1+t^2}2\) gives \(-v\) and \(u\). Then \(\partial R_+=\begin{pmatrix}-v&-u\\u&-v\end{pmatrix}\), and \(R_+J=\begin{pmatrix}u&-v\\v&u\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) is the same matrix.

**6.3.** \(C\otimes I\) is block diagonal with three copies of \(C\), and \(I\otimes C\) is a permutation conjugate of it, so each has determinant \(2^3\), and the product has determinant \(2^6=64\).

**6.4.** Corollary 2.2 applies to every cyclic quadrilateral. Theorem 3.2 needs \(\beta=a+1\) transcendental over \(\mathbb Q\); for algebraic \(a\) its hypothesis fails, and indeed some kites with algebraic \(a\), such as the square (\(a=0\)), are transitive.

## References

- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
- [FR] P. Frankl and V. Rödl, *All triangles are Ramsey*, Transactions of the American Mathematical Society 297 (1986), 777–779. https://www.ams.org/journals/tran/1986-297-02/S0002-9947-1986-0854099-6
- [LRW-T] I. Leader, P. A. Russell and M. Walters, *Transitive sets in Euclidean Ramsey theory*, Journal of Combinatorial Theory, Series A 119 (2012), 382–396; arXiv:1012.1350. https://arxiv.org/abs/1012.1350
- [LRW-K] I. Leader, P. A. Russell and M. Walters, *Transitive sets and cyclic quadrilaterals*, Journal of Combinatorics 2 (2011), 457–462; arXiv:1012.5468. https://arxiv.org/abs/1012.5468
- [Pal] D. Pálvölgyi, *A cyclic non-Ramsey heptagon*, arXiv:2609.23327 (2026). https://arxiv.org/abs/2609.23327
