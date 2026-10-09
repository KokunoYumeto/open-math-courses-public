# Diameter covers and admissible maps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a bounded set \(Y\) of positive diameter in a Euclidean space, let \(b(Y)\) be the least number of subsets of diameter strictly less than \(\operatorname{diam}Y\) that cover \(Y\). Borsuk asked in 1933 whether \(b(Y)\le d+1\) for every such \(Y\subset\mathbb R^d\). The \(d+1\) vertices of a regular simplex show that \(d+1\) sets can be necessary, and the answer is yes in dimensions at most three. Kahn and Kalai showed in 1993 that it is no in high dimensions [KK]; later constructions lowered the dimension of a counterexample to \(65\) [Bon], \(64\) [JB] and \(63\) [Gri]. A survey of the problem is [Kal]. This course proves the following theorem.

**Theorem** (OpenAI 2026; Theorem 3.1 and Corollary 3.2 of [Six and ten labels](six-and-ten-labels.md)). The compact set
\[
X_4=\{uu^{\mathsf T}:u\in\mathbb R^4,\ \|u\|=1\}
\]
of rank-one orthogonal projections of \(\mathbb R^4\) lies in the nine-dimensional affine space of symmetric \(4\times4\) matrices of trace one. With the Frobenius distance it has diameter \(\sqrt2\), and it cannot be covered by ten subsets of diameter less than \(\sqrt2\). For every \(d\ge9\) there is a compact subset of \(\mathbb R^d\) that cannot be covered by \(d+1\) subsets of smaller diameter.

The set \(X_4\) is a copy of real projective three-space, and two of its points are at distance \(\sqrt2\) exactly when the corresponding lines are orthogonal. The proof turns a cover by small sets into a smooth map from projective space to a simplex whose positive coordinates never overlap on orthogonal lines (this lesson), extends that map to an odd map between spheres of symmetric matrices ([An odd map on symmetric matrices](an-odd-map-on-symmetric-matrices.md)), and uses degree modulo two ([Regular values and degree modulo two](regular-values-and-degree-modulo-two.md), [Double covers and odd maps](double-covers-and-odd-maps.md)) to show that, with the smallest possible number of labels, the supports of the map form a closed combinatorial cycle ([Supports at equality](supports-at-equality.md)). For ten labels on \(\mathbb R^4\) such a cycle cannot exist ([Six and ten labels](six-and-ten-labels.md)). The projector model of lines is classical; Conway, Hardin and Sloane use it for packings of subspaces [CHS], and Kalai describes it in connection with the Kahn–Kalai construction [Kal].

We use the core courses [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20) and [Point-Set Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C90): compactness, continuity, and smooth maps between Euclidean spaces. Smooth partitions of unity come from [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport), Theorem 3.1.

## 1. Lines and projectors

Let \(V\) be a Euclidean space of dimension \(k\ge2\), and let \(\operatorname{Sym}(V)\) be the space of symmetric operators on \(V\) with the inner product \(\langle A,B\rangle_F=\operatorname{tr}(AB)\) and norm \(\|A\|_F=\operatorname{tr}(A^2)^{1/2}\). Its dimension is
\[
N_k=\frac{k(k+1)}2 .
\]
For a line \(x\subset V\) and a unit vector \(u\in x\), the operator \(P_x=uu^{\mathsf T}\), \(v\mapsto\langle u,v\rangle u\), is the orthogonal projection onto \(x\); it does not change when \(u\) is replaced by \(-u\). We write \(\mathbb P(V)\) for the set of lines of \(V\) and
\[
X_k=\{P_x:x\in\mathbb P(V)\}\subset\operatorname{Sym}(V).
\]

**Lemma 1.1** (Projector geometry). (a) The map \(x\mapsto P_x\) is injective, and \(X_k\) is compact and lies in the affine hyperplane \(\{A:\operatorname{tr}A=1\}\), a Euclidean space of dimension \(N_k-1\).

(b) If \(u,v\) are unit vectors spanning lines \(x,y\), then
\[
\|P_x-P_y\|_F^2=2-2\langle u,v\rangle^2 . \tag{1.1}
\]
In particular \(\operatorname{diam}X_k=\sqrt2\), and \(\|P_x-P_y\|_F=\sqrt2\) exactly when \(x\perp y\).

*Proof.* (a) The range of \(P_x\) is \(x\), so \(P_x\) determines \(x\). The set \(X_k\) is the image of the compact unit sphere of \(V\) under the continuous map \(u\mapsto uu^{\mathsf T}\), hence compact, and \(\operatorname{tr}(uu^{\mathsf T})=\|u\|^2=1\). (b) \(\operatorname{tr}(P_x^2)=\operatorname{tr}P_x=1\), and \(\operatorname{tr}(P_xP_y)=\operatorname{tr}(uu^{\mathsf T}vv^{\mathsf T})=\langle u,v\rangle^2\); expand \(\operatorname{tr}((P_x-P_y)^2)\). The right side of (1.1) is at most \(2\), with equality exactly when \(\langle u,v\rangle=0\), and orthogonal lines exist since \(k\ge2\). \(\square\)

We identify \(\mathbb P(V)\) with \(X_k\) and give it the subspace topology; it is then compact, Hausdorff and second countable. Fix an orthonormal basis \(e_1,\dots,e_k\) of \(V\) and write \(u_i=\langle u,e_i\rangle\). For each \(i\), let \(U_i\) be the set of lines not orthogonal to \(e_i\), and define
\[
\varphi_i:U_i\to\mathbb R^{k-1},\qquad\varphi_i([u])=\Bigl(\frac{u_j}{u_i}\Bigr)_{j\ne i},
\]
where \([u]\) denotes the line spanned by \(u\ne0\). In terms of the projector, \(U_i=\{P:P_{ii}>0\}\) and \(\varphi_i(P)=(P_{ij}/P_{ii})_{j\ne i}\), so \(U_i\) is open and \(\varphi_i\) is continuous. Its inverse sends \(w\) to \(uu^{\mathsf T}\), where \(u\) is the unit vector in the direction of the vector with \(i\)-th coordinate \(1\) and the other coordinates \(w\); it is continuous, so \(\varphi_i\) is a homeomorphism onto \(\mathbb R^{k-1}\). The sets \(U_i\) cover \(\mathbb P(V)\), and on \(\varphi_i(U_i\cap U_j)\) the transition map \(\varphi_j\circ\varphi_i^{-1}\) sends \(w\) to the ratios \(u_l/u_j\) of the coordinates of \((w\text{ with }1\text{ inserted at }i)\), a rational map with nonvanishing denominator, hence smooth. So the charts \(\varphi_i\) make \(\mathbb P(V)\) a compact smooth manifold of dimension \(k-1\), the *projective space* of \(V\). Charts from another orthonormal basis are smooth with respect to these, because ratios of linear forms are smooth where the denominator does not vanish; so the smooth structure does not depend on the basis. For \(V=\mathbb R^k\) we write \(\mathbb{RP}^{k-1}\).

The map \(V\setminus\{0\}\to\mathbb P(V)\), \(v\mapsto[v]\), is smooth: in the chart \(\varphi_i\) it is \(v\mapsto(v_j/v_i)_{j\ne i}\) on \(\{v_i\ne0\}\). If \(W\subseteq V\) is a subspace of dimension \(r\ge1\), the inclusion \(\mathbb P(W)\to\mathbb P(V)\) is smooth (use an orthonormal basis of \(V\) extending one of \(W\)), and \(\mathbb P(W)\) is a copy of \(\mathbb{RP}^{r-1}\).

## 2. From covers to admissible maps

Write \([m]=\{1,\dots,m\}\) and \(\Delta^{m-1}=\{t\in\mathbb R^m:t_i\ge0,\ \sum_it_i=1\}\).

**Definition 2.1.** A map \(f=(f_1,\dots,f_m):\mathbb P(V)\to\mathbb R^m\) is **admissible** if it is smooth, takes values in \(\Delta^{m-1}\), and its *supports*
\[
S(x)=\{i\in[m]:f_i(x)>0\}
\]
satisfy
\[
x\perp y\quad\Longrightarrow\quad S(x)\cap S(y)=\varnothing . \tag{2.1}
\]
The elements of \([m]\) are called *labels*. Since \(\sum_if_i(x)=1\), every support is nonempty.

**Lemma 2.2** (Restriction). Let \(f:\mathbb P(V)\to\Delta^{m-1}\) be admissible and \(W\subseteq V\) a subspace of dimension at least one. Then \(f|_{\mathbb P(W)}\) is admissible. If \(J\subseteq[m]\) contains every label used on \(\mathbb P(W)\), the coordinates in \(J\) form an admissible map \(\mathbb P(W)\to\Delta_J\), where \(\Delta_J\cong\Delta^{|J|-1}\) is the face of \(\Delta^{m-1}\) spanned by the unit vectors \(e_j\), \(j\in J\).

*Proof.* The restriction of a smooth map to \(\mathbb P(W)\) is smooth because the inclusion is smooth, and orthogonal lines of \(W\) are orthogonal in \(V\). The omitted coordinates vanish on \(\mathbb P(W)\), so the remaining ones still sum to one. \(\square\)

**Lemma 2.3** (From a cover to an admissible map). If \(X_k\) is covered by \(m\) subsets of diameter less than \(\sqrt2\), then there is an admissible map \(f:\mathbb P(V)\to\Delta^{m-1}\).

*Proof.* Let the subsets be \(A_1,\dots,A_m\); empty ones are allowed. For nonempty \(A_i\) put \(d_i=\operatorname{diam}A_i<\sqrt2\) and \(\varepsilon_i=(\sqrt2-d_i)/4\), and let \(O_i\) be the set of \(P\in X_k\) with \(\|P-Q\|_F<\varepsilon_i\) for some \(Q\in A_i\); put \(O_i=\varnothing\) if \(A_i=\varnothing\). Each \(O_i\) is open in \(X_k\), and the \(O_i\) cover \(X_k\). If \(P,P'\in O_i\), choose \(Q,Q'\in A_i\) within \(\varepsilon_i\) of them; then
\[
\|P-P'\|_F<2\varepsilon_i+d_i=\frac{\sqrt2+d_i}2<\sqrt2 .
\]
Regard the \(O_i\) as an open cover of \(\mathbb P(V)\). By Theorem 3.1 of [Local tools for bundles and transport](course:DG-FND/local-tools-for-bundles-and-transport) there is a locally finite smooth partition of unity \((h_j)_{j\in\mathcal J}\) subordinate to it: \(h_j\ge0\), \(\sum_jh_j=1\), and the support of each \(h_j\) lies in some \(O_{i(j)}\). Put \(f_i=\sum_{i(j)=i}h_j\), a locally finite sum of smooth functions, hence smooth; then \(f_i\ge0\), \(\sum_if_i=1\), and \(f_i(x)>0\) implies \(x\in O_i\). If \(x\perp y\) and \(i\in S(x)\cap S(y)\), then \(P_x,P_y\in O_i\) are at distance less than \(\sqrt2\), contradicting Lemma 1.1(b). \(\square\)

The strict inequality \(\operatorname{diam}A_i<\sqrt2\) is what makes the open enlargements \(O_i\) still avoid orthogonal pairs. A covering by sets that merely contain no orthogonal pair need not have this margin, and the smooth map would not exist in general.

## 3. The support complex

**Definition 3.1.** The **support complex** of an admissible map \(f\) is the family \(K\) of subsets \(I\subseteq[m]\) such that \(I\subseteq S(x)\) for some line \(x\). Its elements are called *faces*; a face with \(j+1\) labels has *dimension* \(j\). A **facet** is a face contained in no larger face. A *witness* of a face \(I\) is a line \(x\) with \(I\subseteq S(x)\).

A subset of a face is a face, so \(K\) is a finite simplicial complex on the label set. Its *geometric realization* is the union \(|K|\subseteq\Delta^{m-1}\) of the closed faces \(\Delta_I\), \(I\in K\). Every value \(f(x)\) lies in \(\Delta_{S(x)}\subseteq|K|\), so \(f\) is a continuous map \(\mathbb P(V)\to|K|\). Every facet \(I\) has a witness with \(S(x)=I\) exactly: a witness has \(I\subseteq S(x)\in K\), and maximality gives equality.

**Lemma 3.2.** Let \(f\) be admissible and \(I\in K\) a facet. On the open set
\[
U_I=\{x\in\mathbb P(V):f_i(x)>0\text{ for all }i\in I\}
\]
the support is exactly \(I\). If \(x_0\) is a witness of \(I\), then every line in \(x_0^\perp\) uses only labels outside \(I\), and \(U_I\) does not meet \(\mathbb P(x_0^\perp)\).

*Proof.* For \(x\in U_I\), \(S(x)\supseteq I\) is a face, so \(S(x)=I\) by maximality. A line \(y\perp x_0\) has \(S(y)\cap S(x_0)=\varnothing\) by (2.1), and \(S(x_0)\supseteq I\); so \(y\notin U_I\). \(\square\)

These two facts drive the counting arguments of [Supports at equality](supports-at-equality.md): on \(U_I\) the map \(f\) behaves like a map into the open face of \(I\), and orthogonal complements of witnesses only see the complementary labels.

## 4. Exercises

**4.1.** Show that for lines at angle \(\theta\in[0,\pi/2]\), \(\|P_x-P_y\|_F=\sqrt2\sin\theta\).

**4.2.** For \(k=4\), show that the map from trace-one symmetric \(4\times4\) matrices to \(\mathbb R^9\),
\[
A\mapsto\Bigl(\tfrac{a_{11}-a_{22}}{\sqrt2},\ \tfrac{a_{11}+a_{22}-2a_{33}}{\sqrt6},\ \tfrac{a_{11}+a_{22}+a_{33}-3a_{44}}{\sqrt{12}},\ \sqrt2a_{12},\sqrt2a_{13},\sqrt2a_{14},\sqrt2a_{23},\sqrt2a_{24},\sqrt2a_{34}\Bigr),
\]
preserves distances. So \(X_4\) is isometric to a compact subset of \(\mathbb R^9\).

**4.3.** Show that \(X_2\) is a circle of radius \(1/\sqrt2\) in the plane of trace-one symmetric \(2\times2\) matrices, and that \(b(X_2)=3\).

**4.4.** Let \(f:\mathbb P(V)\to\Delta^{m-1}\) be admissible and \(x\in\mathbb P(V)\). Show that \(|S(x)|\le m-1\) when \(k\ge2\), and that the restriction of \(f\) to \(\mathbb P(x^\perp)\) uses no label of \(S(x)\).

## 5. Solutions

**4.1.** For unit vectors with \(\langle u,v\rangle=\cos\theta\), (1.1) gives \(2-2\cos^2\theta=2\sin^2\theta\).

**4.2.** The difference of two trace-one matrices has trace zero, so it suffices to check that the map, applied to a symmetric \(D\) with \(\operatorname{tr}D=0\), preserves the norm. The off-diagonal entries contribute \(2\sum_{i<j}d_{ij}^2\) to \(\|D\|_F^2\), matching the squares of the last six coordinates. The vectors \((1,-1,0,0)/\sqrt2\), \((1,1,-2,0)/\sqrt6\) and \((1,1,1,-3)/\sqrt{12}\) form an orthonormal basis of the trace-zero diagonal vectors, so the first three coordinates are the coordinates of \((d_{11},\dots,d_{44})\) in that basis and their squares sum to \(\sum_id_{ii}^2\).

**4.3.** For \(u=(\cos t,\sin t)\), \(uu^{\mathsf T}=\frac12I+\frac12R_{2t}\), where \(R_\theta\) is the symmetric matrix with rows \((\cos\theta,\sin\theta)\) and \((\sin\theta,-\cos\theta)\), of Frobenius norm \(\sqrt2\); so \(X_2\) is the circle of radius \(\frac{\sqrt2}2\) about \(\frac12I\), traced once as \(2t\) runs over a period. Three arcs of \(120^\circ\) have diameter \(\sqrt3/\sqrt2<\sqrt2\). Suppose \(X_2=A\cup B\) with both diameters less than \(\sqrt2\); the closures \(\bar A,\bar B\) have the same diameters and still cover. Neither closure contains a pair of antipodal points of the circle. If \(P\in\bar A\cap\bar B\), its antipode lies in neither set, which is impossible. So \(\bar A,\bar B\) are disjoint closed sets covering the connected circle, and one of them is empty; the other is the whole circle, of diameter \(\sqrt2\). Hence \(b(X_2)=3\).

**4.4.** There is a line \(y\perp x\) because \(k\ge2\), and \(S(y)\) is nonempty and disjoint from \(S(x)\), so \(S(x)\ne[m]\). Every line of \(x^\perp\) is orthogonal to \(x\), so (2.1) applies.

## References

- [OpenAI-B9] OpenAI, *A nine-dimensional counterexample to Borsuk's covering assertion*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
- [KK] J. Kahn and G. Kalai, *A counterexample to Borsuk's conjecture*, Bulletin of the AMS 29 (1993). https://arxiv.org/abs/math/9307229
- [Bon] A. V. Bondarenko, *On Borsuk's conjecture for two-distance sets*, Discrete & Computational Geometry 51 (2014). https://arxiv.org/abs/1305.2584
- [JB] T. Jenrich and A. E. Brouwer, *A 64-dimensional counterexample to Borsuk's conjecture*, Electronic Journal of Combinatorics 21(4) (2014), P4.29. https://doi.org/10.37236/4069
- [Gri] M. Grinsztajn, *A 63-dimensional counterexample to Borsuk's conjecture*, author's repository, 2026. https://github.com/maaxgrin/borsuk-63-counterexample
- [Kal] G. Kalai, *Some old and new problems in combinatorial geometry I: around Borsuk's problem*, Surveys in Combinatorics 2015. https://arxiv.org/abs/1505.04952
- [CHS] J. H. Conway, R. H. Hardin and N. J. A. Sloane, *Packing lines, planes, etc.: packings in Grassmannian spaces*, Experimental Mathematics 5 (1996). https://arxiv.org/abs/math/0208004
