# Chern classes and the Whitney formula

DG-CHAR-09 · Differential geometry foundations

A projective bundle determines characteristic coefficients through one monic relation. Relative cup products prove their direct-sum formula. A second construction begins with the Euler class and successively removes a nonzero vector; it defines Chern classes without a metric. We prove that the constructions agree on paracompact Hausdorff bases, with the integral sign fixed by the complex orientation. The resulting determinant, dual, line-tensor and underlying-real formulas include their bundle and coefficient prerequisites.

Throughout, vector bundles have constant finite rank and bases are Hausdorff. We specify paracompactness wherever it is used. Cohomology is ordinary singular cohomology; groups in negative degrees are zero. The algebra assumes the usual number systems and the axiom of choice. Complex fibre orientations list each basis vector followed by its imaginary multiple. Hermitian metrics are conjugate-linear in the first argument. A smooth manifold is Hausdorff, second countable and without boundary unless stated otherwise.

Earlier programme proofs are in [Local tools for bundles and transport](../../../src/local-tools-for-bundles-and-transport.md), [Integral Thom classes and Euler indices](DG-CHAR-06.md), [Manifold duality and the Euler characteristic](DG-CHAR-07.md), and [Projective bundles, Gysin sequences and line classes](DG-CHAR-08.md). References prefixed DG06 or DG08 name their exact numbered results; labels A–D without those prefixes refer to this chapter. The opening lesson's numeric labels specify its local analytic and linear tools. Every result used is proved here or in those exact earlier programme scopes. The free construction readings at the end are materials for the written arguments.

## 1. Characteristic coefficients and direct sums

### A vanishing product from an open cover

**Lemma A.1 (relative annihilation).** Let \(Y=U\cup W\), where \(U,W\) are open. Let \(R\) be a commutative unital ring. If \(\alpha\in H^a(Y;R)\) restricts to zero on \(U\), and \(\beta\in H^b(Y;R)\) restricts to zero on \(W\), then \(\alpha\smile\beta=0\).

**Proof.** Exactness of the pair sequence, DG06 E.1, supplies lifts
\[
\widetilde\alpha\in H^a(Y,U;R),\qquad
\widetilde\beta\in H^b(Y,W;R).
\]
The relative external product DG06 X.4 lies in
\[
H^{a+b}(Y\times Y,U\times Y\cup Y\times W;R).
\]
The diagonal is a map of pairs
\[
(Y,Y)\longrightarrow
(Y\times Y,U\times Y\cup Y\times W),
\]
because each \(y\) belongs to \(U\) or \(W\). Its pullback is therefore zero: the relative chain complex of \((Y,Y)\) is zero. Forgetting relative conditions commutes with this pullback and with X.4's external product. On absolute cochains the product pulled back along the diagonal is exactly the front/back cup formula, so its image is \(\alpha\smile\beta\). Thus that product is zero. □

### Coefficients of the projective relation

Use the following two settings:
\[
(\mathbb F,R,d)=
(\mathbb R,\mathbb F_2,1)
\quad\hbox{or}\quad
(\mathbb C,\mathbb Z,2).
\tag{A.1}
\]
All bases in this component are Hausdorff, and all ranks are constant and finite. Cup products are those of singular cohomology. In the real case cohomology with \(\mathbb F_2\) is commutative by DG06 X.5; in the complex case its even-degree integral part is commutative by the same sign formula.

For a rank-\(r>0\) bundle \(V\), let \(p:P(V)\to B\) and let \(S\) be its tautological line. Put
\[
z=
\begin{cases}
e_2(S),&\mathbb F=\mathbb R,\\
-e(S_{\mathbb R}),&\mathbb F=\mathbb C.
\end{cases}
\tag{A.2}
\]
The complex orientation in this formula is DG08 R.2's orientation. The real line class equals its orientation-transport class by DG08 Z.3.

**Theorem A.2 (projective characteristic coefficients).** There are unique classes \(a_i(V)\in H^{di}(B;R)\), \(1\leq i\leq r\), such that
\[
z^r+\sum_{i=1}^r p^*a_i(V)\smile z^{r-i}=0.
\tag{A.3}
\]
Set \(a_0(V)=1\) and \(a_i(V)=0\) for \(i>r\). For rank zero use these latter conventions without a projectivization. These classes are natural under pullbacks between Hausdorff bases and invariant under bundle isomorphisms.

In the real setting we write \(w_i(V)=a_i(V)\) and call these the Stiefel–Whitney classes. In the complex setting we temporarily write \(C_i(V)=a_i(V)\). For lines,
\[
w_1(L)=e_2(L),\qquad C_1(L)=e(L_{\mathbb R}).
\tag{A.4}
\]

**Proof.** DG08 M.3 gives the graded \(H^*(B;R)\)-module basis \(1,z,\ldots,z^{r-1}\). In degree \(dr\), expand \(-z^r\) uniquely in this basis. The coefficient of \(z^{r-i}\) has degree \(di\), proving existence, grading and uniqueness in (A.3).

For a map \(f:B'\to B\), the pullback bundle \(f^*V\) has projective bundle canonically isomorphic to the pullback of \(P(V)\). In a bundle chart both spaces have coordinates \((b',\ell)\) with \(\ell\in\mathbb F P^{r-1}\), and the proposed map and inverse are identity coordinate maps. The tautological line likewise pulls back, since its fibre is the represented line. Euler naturality DG06 T.4, with the complex orientation rule where required, therefore pulls \(z\) back to the corresponding \(z'\). Pull (A.3) back to \(P(f^*V)\). Its coefficients become \(f^*a_i(V)\), so uniqueness gives
\[
a_i(f^*V)=f^*a_i(V).
\tag{A.5}
\]
For an isomorphism over \(B\), the induced homeomorphism of projective bundles has the same tautological-line property; the identical uniqueness argument proves invariance. Rank zero is immediate from the conventions.

For a line \(P(L)\to B\) is a homeomorphism: it has one point in every fibre and in product charts is the identity on \(B\). Its tautological line is \(L\). Thus (A.3) is \(z+a_1(L)=0\). In \(\mathbb F_2\) the sign is immaterial, and in the complex case \(z=-e(L_{\mathbb R})\), giving (A.4). Higher line classes are zero by definition. □

### The Whitney formula without a metric

**Theorem A.3 (direct sums and stability).** For real or complex bundles on a Hausdorff base, the projective coefficients satisfy
\[
a_k(V\oplus W)=\sum_{i+j=k}a_i(V)\smile a_j(W).
\tag{A.6}
\]
Consequently their total classes \(a(V)=\sum_{i\geq0}a_i(V)\) satisfy
\[
a(V\oplus W)=a(V)a(W),\qquad
a(\underline{\mathbb F}^{\,s})=1,\qquad
a(V\oplus\underline{\mathbb F}^{\,s})=a(V).
\tag{A.7}
\]

**Proof.** Assume first that \(V,W\) have positive ranks \(r,s\), and put \(Y=P(V\oplus W)\) with projection \(p:Y\to B\). The subbundles \(P(V)\) and \(P(W)\) are disjoint closed subsets of \(Y\). Closedness is checked in a product chart: a line in \(\mathbb F^{r+s}\) belongs to the first summand precisely when all its last \(s\) projection-matrix diagonal entries vanish; these are continuous functions by DG08 R.1. The other summand is treated in the same way.

Let
\[
U=Y\setminus P(W),\qquad W'=Y\setminus P(V).
\tag{A.8}
\]
These opens cover \(Y\). A line in \(U\) has a representative \((v,w)\) with \(v\ne0\). The homotopy
\[
[(v,w)]\longmapsto[(v,(1-t)w)],\qquad 0\leq t\leq1,
\tag{A.9}
\]
stays in \(U\) and is a deformation retraction onto \(P(V)\). It is independent of the chosen nonzero scalar multiple of the representative. To check continuity, in the projection-matrix model its expression is
\[
P\longmapsto
\frac{A_t P A_t^*}{\operatorname{tr}(A_t P A_t^*)},
\qquad
A_t=\operatorname{diag}(I_r,(1-t)I_s).
\]
The denominator is positive on \(U\), including \(t=1\), because the \(V\)-component is nonzero. Thus the formula is continuous in each chart. Bundle transition maps for \(V\oplus W\) are block diagonal and commute with scaling its two summands, so these formulas agree globally. Interchanging the two summands gives a deformation retraction of \(W'\) onto \(P(W)\). Both homotopies preserve the base point.

Let \(z\) denote (A.2) on \(Y\), and form
\[
P_V(z)=\sum_{i=0}^{r}p^*a_i(V)\,z^{r-i},
\qquad
P_W(z)=\sum_{j=0}^{s}p^*a_j(W)\,z^{s-j}.
\tag{A.10}
\]
On \(P(V)\) the tautological line of \(Y\) is its tautological line, so the first polynomial restricts to zero by (A.3). The inclusion \(P(V)\to U\) induces an isomorphism on cohomology, since (A.9) and DG06 K.1 give a homotopy inverse. Therefore \(P_V(z)|_U=0\). Similarly \(P_W(z)|_{W'}=0\).

Lemma A.1 now gives \(P_V(z)P_W(z)=0\). The factors commute when expanding: all complex degrees are even, and in the real case the coefficients are mod two. This is exactly the sign conclusion of DG06 X.5. Hence
\[
0=z^{r+s}+
\sum_{k=1}^{r+s}p^*
 \left(\sum_{i+j=k}a_i(V)a_j(W)\right)z^{r+s-k}.
\tag{A.11}
\]
Uniqueness in A.2 for \(V\oplus W\) identifies each coefficient, proving (A.6).

If one rank is zero, the direct sum is canonically the other bundle and (A.6) reduces to its defining conventions. Thus all ranks are covered. A trivial bundle is pulled back from a vector space over a point. Positive cohomology of a point vanishes by DG06 E.1, so naturality makes its positive classes zero. This proves the middle identity in (A.7), and the other two follow from (A.6). These arguments use no metric or paracompactness. □

### Splitting and the top Euler class

For commuting \(t_1,\ldots,t_r\), define
\[
e_i(t_1,\ldots,t_r)=
\sum_{\substack{J\subset\{1,\ldots,r\}\\|J|=i}}
\prod_{j\in J}t_j,\qquad e_0=1.
\tag{A.12}
\]
The product over a subset may be taken in increasing order; commutativity makes it independent of that order. For \(i>r\) the sum is empty and zero.

**Theorem A.4 (roots, Euler normalization and uniqueness).** Let \(V\) be on a paracompact Hausdorff base. On the flag space \(f:F(V)\to B\) of DG08 M.4 write \(f^*V=L_1\oplus\cdots\oplus L_r\). Then
\[
f^*a_i(V)=e_i(t_1,\ldots,t_r),\qquad t_j=a_1(L_j).
\tag{A.13}
\]
Moreover,
\[
w_r(V)=e_2(V)\quad\hbox{in the real case},\qquad
C_r(V)=e(V_{\mathbb R})\quad\hbox{in the complex case}.
\tag{A.14}
\]
For positive rank these are top-degree classes. For rank zero both sides in (A.14) are the class one with the canonical zero-rank orientation.

On paracompact Hausdorff bases, a natural sequence satisfying the direct-sum formula, rank vanishing, degree-zero normalization and the line normalizations (A.4) is uniquely determined by them.

**Proof.** The flag space is paracompact Hausdorff and its pullback is injective in \(\mathbb F_2\) cohomology for real bundles and in integral cohomology for complex bundles, by DG08 M.4. Apply A.3 successively to the actual line sum. Its total class is
\[
\prod_{j=1}^r(1+t_j).
\]
Expanding by choosing \(t_j\) from exactly \(i\) of the factors gives (A.12) and (A.13), including ranks zero and one.

The top component is \(\prod_jt_j\). In the real case (A.4) identifies its factors with mod-two line Euler classes, and the mod-two sum formula of DG06 T.4 identifies their product with \(e_2(f^*V)\). In the complex case the same theorem applies integrally. The ordered orientation on the underlying real direct sum of complex lines lists each basis vector and its imaginary multiple, precisely the canonical complex orientation of \(f^*V\), by DG08 R.2. Therefore the product is \(e((f^*V)_{\mathbb R})\), with no unspecified sign. Naturality of the Euler class and injectivity of \(f^*\) prove (A.14). The zero-rank normalization is in DG06 T.3–T.4.

For another sequence with the listed properties, its value on each \(L_j\) is \(1+t_j\). Its direct-sum formula and naturality therefore give the same pullbacks (A.13). Injectivity makes its classes equal to ours. This proves uniqueness on the stated category of bases. It does not require a homotopy classification theorem. □

### Inverses in a completed graded ring

**Lemma A.5 (the total-class inverse).** In the product of its nonnegative graded groups, a total class \(a=1+\sum_{i\geq1}a_i\), with \(\deg a_i=di\) in the coefficient setting (A.1), has a unique inverse \(b=1+\sum_{m\geq1}b_m\). It is defined degree by degree by
\[
b_0=1,\qquad b_m=-\sum_{i=1}^{m}a_i b_{m-i}.
\tag{A.15}
\]
If a sum \(V\oplus W\) is trivial, then \(a(W)=a(V)^{-1}\) in this completed ring.

**Proof.** Define multiplication of two sequences by the coefficient rule
\((uv)_m=\sum_{i=0}^m u_i v_{m-i}\). Every such sum is finite. Associativity follows by reindexing the finite sum over triples of nonnegative indices with fixed total; its scalar multiplication is associative by DG06 K.5. The relevant homogeneous elements commute as noted after (A.1), so the product ring is commutative and has unit \((1,0,\ldots)\).

The degree-\(dm\) coefficient of \(ab\), for \(m>0\), is \(b_m+\sum_{i=1}^m a_i b_{m-i}\). Setting it equal to zero forces (A.15). Starting with \(b_0=1\), this recursion supplies each coefficient from the earlier ones, so it proves both existence and uniqueness. Commutativity gives \(ba=ab=1\). The last assertion follows from A.3. On an unbounded cohomology ring the inverse can have infinitely many nonzero components; no finite polynomial inverse is asserted. □
## 2. Chern classes from the Euler class

### The quotient above a nonzero vector

**Lemma B.1 (the tautological quotient).** Let \(V\to B\) be a complex rank-\(r>0\) vector bundle on a Hausdorff base, and let \(V^\times\) be its complement of the zero section, with projection \(\pi\). The pullback \(\pi^*V\) has the nowhere-zero section \(v\mapsto v\). Its span is a trivial line subbundle, and the fibrewise quotient
\[
Q_V=\pi^*V/\mathbb C v
\tag{B.1}
\]
is a complex vector bundle of rank \(r-1\) on \(V^\times\). Its topology is the quotient topology of the pullback total space. This construction commutes with pullback maps and bundle isomorphisms.

**Proof.** The total space of \(V\) is Hausdorff. Points over distinct base points separate by the projection; points in the same fibre separate inside a common product chart. The zero section is closed, since its intersection with every product chart is the inverse image of the closed zero vector. Thus \(V^\times\) is an open Hausdorff space.

In a local frame of \(V\), a point of \(\pi^*V\) is \((b,v,w)\), where \(v\in\mathbb C^r\setminus0\) and \(w\in\mathbb C^r\). Work on the open set \(v_j\ne0\). The class of \(w\) modulo the span of \(v\) has the unique representative with \(j\)-th coordinate zero:
\[
w'=w-\frac{w_j}{v_j}v,\qquad
y_k=w_k-\frac{w_j}{v_j}v_k\quad(k\ne j).
\tag{B.2}
\]
Uniqueness follows because adding \(t v\) changes the \(j\)-th coordinate by \(t v_j\). The coordinates \((y_k)_{k\ne j}\) consequently identify each quotient fibre linearly with \(\mathbb C^{r-1}\). Their inverse sends \(y\) to the class of the vector whose \(j\)-th coordinate is zero and whose other coordinates are \(y_k\).

These are continuous quotient charts, not just fibrewise bijections. Indeed the change of coordinates on the original pullback total space
\[
(b,v,w)\longleftrightarrow
\left(b,v,(y_k)_{k\ne j},t=\frac{w_j}{v_j}\right)
\tag{B.3}
\]
is a homeomorphism. Its inverse is \(w_j=t v_j\) and \(w_k=y_k+t v_k\). Both directions use continuous functions with denominator \(v_j\ne0\). The quotient map in these coordinates is the projection forgetting \(t\), a continuous open surjection: it maps basic open rectangles to open rectangles. Hence it is a quotient map. The preimages of these chart domains are open saturated subsets of the total space. The restriction of a quotient map to an open saturated subset is quotient, because an open inverse image there is open in the whole total space and saturated. Thus the local quotient topologies agree with the global quotient topology.

On overlapping frame and index choices, the coordinate change is obtained by converting a representative to the other vector frame and applying (B.2) there. It is linear in \(y\), continuous in \((b,v)\), and has a continuous inverse given by reversing the two choices. Thus it is an invertible transition matrix and defines the claimed bundle. For \(r=1\) the coordinate list \(y\) is empty and the quotient is the zero bundle.

The map \((v,t)\mapsto t v\) trivializes the span line. Its inverse over \(v_j\ne0\) recovers \(t=w_j/v_j\), proving continuity. These local inverses agree and prove that it is a line subbundle.

For \(f:B'\to B\), the map \((b',v)\mapsto v\) from \((f^*V)^\times\) to \(V^\times\) identifies the pullback fibres and their distinguished vectors. The induced quotient map sends the class of \(w\) to the class of the same \(w\). In the just-constructed charts it is the identity on \(y\) over the base map, so it is the canonical pullback isomorphism. The same coordinate argument works for bundle isomorphisms. □

### The inductive definition and its immediate properties

The real orientation of a complex vector space is the ordered list
\((v_1,iv_1,\ldots,v_r,iv_r)\) from DG08 R.2. Its independence of basis, continuity in bundle charts and compatibility with ordered sums have already been proved there.

**Theorem B.2 (metric-free Chern construction).** Every complex vector bundle \(V\) of constant rank \(r\) on a Hausdorff base has classes \(c_i(V)\in H^{2i}(B;\mathbb Z)\) specified by
\[
c_0(V)=1,\qquad c_i(V)=0\ (i>r),\qquad
c_r(V)=e(V_{\mathbb R})\ (r>0),
\tag{B.4}
\]
and, for \(0<i<r\),
\[
\pi^*c_i(V)=c_i(Q_V).
\tag{B.5}
\]
The equality in (B.5) determines a unique class. For \(r=0\) only the degree-zero class is retained. Write \(c(V)=\sum_{i=0}^r c_i(V)\) for the total Chern class. These classes are natural under pullbacks between Hausdorff bases, invariant under complex bundle isomorphisms, and stable:
\[
c(V\oplus\underline{\mathbb C}^{\,s})=c(V).
\tag{B.6}
\]
For a complex line they equal the Euler-normalized first class in DG08 formula (W.9).

**Proof.** DG08 S.1 applied to the canonically oriented real rank-\(2r\) bundle has segment
\[
H^{q-2r}(B;\mathbb Z)\longrightarrow H^q(B;\mathbb Z)
\xrightarrow{\pi^*}H^q(V^\times;\mathbb Z)
\longrightarrow H^{q-2r+1}(B;\mathbb Z).
\tag{B.7}
\]
If \(q<2r-1\), both outer groups have negative degree and vanish. Exactness makes the middle pullback an isomorphism. For \(0<i<r\), \(q=2i\leq2r-2\) satisfies this bound.

Induct on rank. The rank-zero definition is explicit. Given all lower ranks on Hausdorff bases, B.1 provides \(Q_V\) over the Hausdorff space \(V^\times\), so all \(c_i(Q_V)\) are already defined. The isomorphism just proved gives the unique lower classes (B.5), and the oriented Euler class supplies the top class. This proves existence and uniqueness of the inductively specified sequence, without a metric.

For naturality let \(f:B'\to B\), \(V'=f^*V\), and let \(F:(V')^\times\to V^\times\) be the map of B.1. Then \(\pi F=f\pi'\) and \(Q_{V'}\cong F^*Q_V\). For a lower index, induction and (B.5) give
\[
(\pi')^*f^*c_i(V)
=F^*\pi^*c_i(V)
=F^*c_i(Q_V)
=c_i(Q_{V'}).
\tag{B.8}
\]
Injectivity of \((\pi')^*\) in degree \(2i\) identifies \(f^*c_i(V)\) with \(c_i(V')\). The top class is natural by DG06 T.4 and preservation of the complex orientation. The degree-zero and above-rank conventions are natural as well. A bundle isomorphism gives the same deleted-space square and quotient identification, so the same induction proves isomorphism invariance.

To prove stability, put \(E=V\oplus\underline{\mathbb C}\), of rank \(r+1\). Its deleted total space has the section
\[
s:B\longrightarrow E^\times,\qquad s(b)=(0,1).
\]
The pulled-back quotient \(s^*Q_E\) is \(V\): fibrewise, the class of \((w,t)\) modulo the last coordinate line is identified with \(w\), and these maps and inverses are identity coordinate maps in bundle charts. For \(1\leq i<r+1\), pull (B.5) for \(E\) back by \(s\). Naturality, already proved for the rank-\(r\) quotient, and \(\pi s=\operatorname{id}\) give \(c_i(E)=c_i(V)\). The top class of \(E\) is zero by its nowhere-zero section and DG06 T.4. Classes above rank and the degree-zero class satisfy the same equality by their definitions. This also covers \(r=0\), where the range of lower positive indices is empty. Iterating proves (B.6).

For rank one the top-class definition is precisely \(e(V_{\mathbb R})\), agreeing with DG08 formula (W.9). □

### Paracompactness needed for comparison

**Lemma B.3 (deleted total spaces remain paracompact).** If \(B\) is paracompact Hausdorff and \(V\) has positive finite rank, then \(V^\times\) is paracompact Hausdorff.

**Proof.** Choose a continuous Hermitian metric by DG08 Q.4. Its unit sphere bundle \(S(V)\to B\) is locally trivial with compact Hausdorff fibre \(S^{2r-1}\). To check the local trivializations directly, let \(H(b)\) be the positive Hermitian matrix in a vector frame. The map from the standard unit sphere to the metric unit sphere is
\[
u\longmapsto\frac{u}{\sqrt{u^*H(b)u}}.
\tag{B.9}
\]
It is continuous, with inverse \(v\mapsto v/|v|\); these identities use that the displayed vectors have their indicated unit norms. Positivity keeps both denominators nonzero. The standard sphere is compact by the finite-dimensional closed-bounded compactness theorem in the opening lesson 0.1. Thus DG08 Q.5 makes \(S(V)\) paracompact Hausdorff.

We give the needed product argument explicitly. If \(X\) is paracompact Hausdorff, then \(X\times(0,\infty)\) is paracompact. Let \(\mathcal U\) be any open cover of this product. For \(n\in\mathbb Z\), set
\[
I_n=(2^{n-1},2^{n+1}),\qquad
J_n=[2^{n-2},2^{n+2}].
\tag{B.10}
\]
The intervals \(I_n\) cover \((0,\infty)\), and their closures form a locally finite family there. To see both assertions, the powers \(2^n\) tend to infinity as \(n\to\infty\) because \(2^n\geq n+1\) for \(n\geq0\), by induction; their reciprocals tend to zero. Every positive number therefore lies between consecutive powers and in one of these intervals. Any compact interval \([a,b]\subset(0,\infty)\) meets only finitely many of the closures, by the same bounds.

Each \(X\times J_n\) is paracompact by DG08 Q.5, applied to its projection onto \(X\) with compact interval fibre. Restrict \(\mathcal U\) to this product and choose a locally finite relatively open refinement \(\mathcal R_n\). Restrict every member of \(\mathcal R_n\) to \(X\times I_n\). These restrictions are open in the full product, since \(I_n\) is contained in the interior of \(J_n\). They cover \(X\times I_n\) and refine \(\mathcal U\).

For fixed \(n\), this restricted family is locally finite in the full product. At a point whose interval coordinate is in the interior of \(J_n\), use the local finiteness in \(X\times J_n\). At a point outside the closure of \(I_n\), use an interval neighbourhood disjoint from that closure. These two cases cover the product, because \(\overline{I_n}\subset\operatorname{int}J_n\). Finally, near any interval coordinate only finitely many \(\overline{I_n}\) occur. Intersect neighbourhoods establishing local finiteness for those finitely many families. Their union is a locally finite open refinement of \(\mathcal U\). This proves the product assertion.

Radial normalization gives the homeomorphism
\[
V^\times\longrightarrow S(V)\times(0,\infty),
\qquad
v\longmapsto\left(\frac{v}{\|v\|},\|v\|\right),
\tag{B.11}
\]
with inverse \((u,t)\mapsto tu\). The formulas are continuous in every chart, and all norms in their denominators are positive. Apply the product assertion with \(X=S(V)\). Hausdorffness was proved in B.1. □

### Agreement with the projective classes

**Theorem B.4 (integral Whitney formula and projective relation).** On a paracompact Hausdorff base,
\[
c_i(V)=C_i(V)
\tag{B.12}
\]
for all indices. In particular,
\[
c(V\oplus W)=c(V)c(W),\qquad
z^r+\sum_{i=1}^r p^*c_i(V)\,z^{r-i}=0,
\qquad z=-c_1(S).
\tag{B.13}
\]
The projective relation is asserted only for positive rank; the direct-sum identity includes rank zero. On a full flag, \(c_i(V)\) pulls back to the \(i\)-th elementary symmetric polynomial in the actual line first classes. These classes are the unique natural, rank-vanishing, Whitney-multiplicative sequence with \(c_0=1\) and the specified complex-line Euler normalization.

**Proof.** Induct on rank on the category of paracompact Hausdorff bases. Rank zero agrees by convention, and rank one agrees by A.4 and the top-class definition (B.4). For general positive rank, A.4 identifies the top projective coefficient with \(e(V_{\mathbb R})=c_r(V)\).

For \(0<i<r\), work over \(V^\times\), which is paracompact by B.3. The pulled-back Hermitian metric gives the orthogonal complement of the span of \(v\) by DG08 Q.4. The quotient map from that complement to \(Q_V\) is a bundle isomorphism: fibrewise its inverse takes the class of \(w\) to
\[
w-\frac{h(v,w)}{h(v,v)}v.
\tag{B.14}
\]
The metric is conjugate-linear in its first argument and linear in its second. Therefore (B.14) is complex linear in \(w\), annihilates the change \(w\mapsto w+\lambda v\), and lies in the orthogonal complement. It is continuous in B.1's quotient charts; each chart permits a continuous representative \(w\), and the result is independent of that choice. Together with the trivial span line this yields an actual bundle isomorphism
\[
\pi^*V\cong\underline{\mathbb C}\oplus Q_V.
\tag{B.15}
\]
Naturality and stability of the projective coefficients in A.2–A.3 give \(\pi^*C_i(V)=C_i(Q_V)\). Induction applies to \(Q_V\) over its paracompact Hausdorff base, so the latter is \(c_i(Q_V)\). Equation (B.5) and injectivity in (B.7) then give \(C_i(V)=c_i(V)\).

The rank, zero and above-rank cases have already been addressed, completing the induction. Substituting (B.12) into A.3 and A.13 proves (B.13) and the root formula. The projective generator in the complex case is \(-e(S_{\mathbb R})=-c_1(S)\) by the rank-one definition. The uniqueness statement is precisely A.4 in the complex coefficient setting. All metric choices were used only to prove equality with the already metric-free definition. □

### Conjugation before choosing a metric

**Theorem B.5 (conjugation on every Hausdorff base).** For a complex rank-\(r\) bundle, let \(\overline V\) have the same underlying real bundle with scalar action \(\lambda\cdot_{\overline V}v=\overline\lambda\,v\). Then
\[
c_i(\overline V)=(-1)^i c_i(V)
\tag{B.16}
\]
on every Hausdorff base.

**Proof.** In a vector chart, use conjugates of the original complex coordinates for \(\overline V\). If the original coordinate change is \(A(b)\), the new one is \(\overline{A(b)}\), continuous and invertible; their cocycle identities give the conjugate bundle. The identity on underlying real total spaces is continuous in both directions, because coordinate conjugation is a real homeomorphism.

A positive real basis for \(V_{\mathbb R}\) is \((v_1,iv_1,\ldots,v_r,iv_r)\). The corresponding complex orientation of \(\overline V\) is \((v_1,-iv_1,\ldots,v_r,-iv_r)\). Its sign relative to the former is \((-1)^r\), by the determinant permutation formula DG06 L.1. Euler orientation change DG06 T.4 therefore gives (B.16) for \(i=r>0\).

The deleted total spaces agree as real spaces. The complex line spanned by \(v\) is also the same subset in either scalar convention, and its quotient for \(\overline V\) is canonically the conjugate of \(Q_V\). This identification is continuous in the quotient charts of B.1: conjugate all their scalar coordinates, and (B.2) becomes the conjugate formula.

Induct on rank. For a lower positive index, the induction hypothesis and (B.5) give
\[
\pi^*c_i(\overline V)
=c_i(\overline{Q_V})
=(-1)^i c_i(Q_V)
=\pi^*\bigl((-1)^ic_i(V)\bigr).
\]
Injectivity of \(\pi^*\) in that degree proves (B.16). The degree-zero and above-rank assertions follow from their conventions, which also settle rank zero. No metric or paracompactness was used. □
## 3. Bundle operations and the real comparison

### Continuous bundles for the algebraic operations

**Lemma C.1 (dual, determinant and tensor charts).** A complex rank-\(r\) bundle \(V\) on a Hausdorff base has a dual bundle \(V^*\), a determinant line \(\det_{\mathbb C}V\), and, for a complex line \(L\), a rank-\(r\) tensor bundle \(V\otimes L\). These constructions commute with pullback. They have canonical identifications
\[
\det_{\mathbb C}(L_1\oplus\cdots\oplus L_r)
\cong L_1\otimes\cdots\otimes L_r,
\tag{C.1}
\]
and
\[
(L_1\oplus\cdots\oplus L_r)\otimes L
\cong\bigoplus_{j=1}^r(L_j\otimes L).
\tag{C.2}
\]
For rank zero the determinant line is the trivial complex line and the tensor bundle is the zero bundle. If \(V\) has a continuous Hermitian metric, there is a complex-linear bundle isomorphism
\[
\overline V\longrightarrow V^*,\qquad
v\longmapsto\bigl(w\mapsto h(v,w)\bigr),
\tag{C.3}
\]
where \(h\) is conjugate-linear in the first argument.

**Proof.** In a vector frame, a linear functional is specified by its values on the \(r\) basis vectors, by finite-dimensional basis expansion from the opening lesson 0.2. If vector coordinates change by \(A\), the column of functional coefficients changes by \((A^{-1})^{\mathsf T}\), because the scalar evaluation must stay fixed. Matrix inversion is continuous by the opening lesson 0.4, applied to underlying real matrices as in DG08 Q.4. Thus these are continuous invertible transition matrices with the required cocycle law. The open-chart gluing proof in DG08 I.2, with fibre \(\mathbb C^r\), gives the dual bundle.

For clarity, the determinant fibre is the one-dimensional vector space generated by formal symbols \(v_1\wedge\cdots\wedge v_r\), subject to multilinearity in each entry and the rule that a repeated pair of entries gives zero. One concrete construction is the free vector space on ordered \(r\)-tuples, quotiented by these relations. A zero tuple in one entry gives zero by linearity. Replacing two slots by the same sum \(u+v\) and expanding shows that interchanging those slots changes the sign. Expansion in a basis \(e_1,\ldots,e_r\) therefore expresses every symbol as
\[
v_1\wedge\cdots\wedge v_r
=\det[v_1\ \cdots\ v_r]\,
 (e_1\wedge\cdots\wedge e_r).
\tag{C.4}
\]
Terms with repeated basis indices vanish; the remaining terms are the permutations with exactly their determinant signs. The coordinate determinant itself is an alternating multilinear function, by DG06 L.1, so it descends to a functional on this quotient and takes the displayed basis symbol to one. Thus that symbol is nonzero and the fibre has dimension exactly one. A vector coordinate change by \(A\) changes its scalar determinant coordinate by \(\det A\), by the determinant multiplication identity in L.1. These nonzero continuous scalar transitions define the determinant line. They describe its intrinsic fibre just constructed, so different vector frames give the same bundle. In rank zero use \(\mathbb C\) with its distinguished generator one.

For the tensor product of a vector space with a line, elementary tensors span the quotient by bilinear relations. If \(e_1,\ldots,e_r\) is a vector basis and \(\ell\ne0\) a line vector, they are spanned by \(e_j\otimes\ell\). They are linearly independent: for each \(j\), the bilinear function \((\sum a_ke_k,t\ell)\mapsto a_jt\) descends to a linear functional which is one on the \(j\)-th basis candidate and zero on all the others. Hence it is a basis. If the vector transition is \(A\) and the line transition is \(g\), the tensor transition is \(gA\). These matrices are continuous, invertible and satisfy the cocycle law. They define the tensor bundle by the same gluing argument.

The map in (C.1) sends the tensor of \(r\) vectors, one from each line in the listed order, to their wedge in the ordered direct sum. Multilinearity makes it well-defined on the tensor product. In line frames it takes the scalar product coordinate to the determinant coordinate, hence is an isomorphism with continuous inverse. The tensor product of finitely many lines may be parenthesized successively; the coordinate product description shows that changing parentheses gives the canonical same scalar-coordinate map. For (C.2), send \((v_1,\ldots,v_r)\otimes \ell\) to \((v_1\otimes\ell,\ldots,v_r\otimes\ell)\) and extend linearly. The basis description shows it is a fibre isomorphism. It and its inverse are identity maps on the \(r\) scalar coordinates in common frames, so both are continuous.

A pullback replaces each transition matrix or scalar by its composition with the base map. Taking inverse transpose, determinant, or multiplication by a scalar commutes with this composition. The natural fibre identifications therefore have identity coordinate maps and give the claimed pullback isomorphisms.

Finally (C.3) is complex linear for the conjugate scalar structure: multiplication of \(v\) there by \(\lambda\) is multiplication of the original \(v\) by \(\overline\lambda\), and \(h(\overline\lambda v,w)=\lambda h(v,w)\). Positivity implies injectivity: if \(h(v,w)=0\) for all \(w\), choose \(w=v\). Both fibres have dimension \(r\), so the map is bijective by basis extension, opening lesson 0.2. In coordinates \(h(v,w)=\overline v^{\mathsf T}H(b)w\), the map from the conjugate coordinates \(\overline v\) to the functional column has matrix \(H(b)^{\mathsf T}\). This is continuous with continuous inverse by matrix inversion. It proves the bundle assertion, including the unique map between zero bundles when \(r=0\). □

### Integral identities

**Theorem C.2 (determinants, duals and line tensors).** On a paracompact Hausdorff base,
\[
c_1(V)=c_1(\det_{\mathbb C}V),\qquad
c_i(V^*)=(-1)^i c_i(V).
\tag{C.5}
\]
If \(L\) is a complex line, \(\ell=c_1(L)\), and \(0\leq k\leq r=\operatorname{rank}V\), then
\[
c_k(V\otimes L)
=\sum_{i=0}^k
\binom{r-i}{k-i}\,c_i(V)\,\ell^{k-i}.
\tag{C.6}
\]
The total Chern class has the completed inverse of A.5. In particular \(c(V)c(W)=1\) when \(V\oplus W\) is trivial.

**Proof.** Choose the complex flag map \(f:F(V)\to B\) of DG08 M.4. It is injective on integral cohomology, and \(f^*V=\bigoplus_j L_j\) on a paracompact Hausdorff flag space. Put \(t_j=c_1(L_j)\). By C.1, the pulled-back determinant is the tensor product of these lines. The line tensor formula DG08 W.3, applied successively, gives first class \(\sum_j t_j\). By B.4 this is \(f^*c_1(V)\). Naturality of determinant and Chern classes and injectivity prove the first equality in (C.5).

For the dual equality, choose a Hermitian metric by DG08 Q.4. The actual isomorphism (C.3), invariance of Chern classes B.2 and the conjugation formula B.5 give
\[
c_i(V^*)=c_i(\overline V)=(-1)^i c_i(V).
\]
For rank zero the determinant is trivial and all positive Chern classes vanish, so both assertions hold there as well.

Pull the tensor bundle back to the same flag. By (C.2) it splits into the lines \(L_j\otimes f^*L\), whose first classes are \(t_j+f^*\ell\) by DG08 W.3. B.4 expresses its \(k\)-th class as \(e_k(t_1+f^*\ell,\ldots,t_r+f^*\ell)\).

Expand this elementary symmetric expression by choosing a \(k\)-element subset of indices, then choosing which of its factors contribute their \(t_j\) rather than \(f^*\ell\). Fix the chosen \(i\)-element subset contributing roots. There are exactly \(\binom{r-i}{k-i}\) ways to choose the other \(k-i\) indices from the remaining \(r-i\). Here the binomial coefficient is the number of subsets of that size; no division inside the cohomology ring is involved. Grouping this finite sum gives
\[
e_k(t_1+f^*\ell,\ldots,t_r+f^*\ell)
=\sum_{i=0}^k\binom{r-i}{k-i}
 e_i(t_1,\ldots,t_r)(f^*\ell)^{k-i}.
\tag{C.7}
\]
All factors have even degree, so the rearrangements introduce no sign, by DG06 X.5. The right side is the pullback of (C.6) by B.4 and naturality. Integral injectivity proves (C.6) downstairs. If \(r=k=0\), both sides are the degree-zero class one.

The final assertions are A.5 and B.4: their recursion uses the even-degree Chern classes, and the Whitney formula gives \(c(V)c(W)=c(V\oplus W)=1\) for a trivial sum. This is a coefficientwise identity in the completed graded ring even when the base has unbounded cohomology. □

### The complete real comparison

Write \(\rho_2\) for the cohomology map induced by reduction of integer cochains modulo two. It commutes with pullback and cup products because both are defined by integer face and evaluation formulas.

**Theorem C.3 (underlying real Stiefel–Whitney classes).** For a complex bundle \(V\) on a paracompact Hausdorff base,
\[
w_{2i}(V_{\mathbb R})=\rho_2c_i(V),\qquad
w_{2i+1}(V_{\mathbb R})=0
\tag{C.8}
\]
for every nonnegative index.

**Proof.** First consider a complex line \(L\). DG08 I.4 gives a continuous map \(g:B\to\mathbb CP^\infty\) and a line-bundle isomorphism \(L\cong g^*\gamma\), where \(\gamma\) is the infinite tautological line. Its underlying real plane pulls back in the same manner, as is seen in its real coordinate charts.

The class \(w_1(\gamma_{\mathbb R})\) is defined by A.2: that construction required only a Hausdorff base, and DG08 I.1 proves this condition for \(\mathbb CP^\infty\). But
\[
H^1(\mathbb CP^\infty;\mathbb F_2)=0
\]
by DG08 I.3, so this class is zero. Naturality in A.2 implies \(w_1(L_{\mathbb R})=0\). This argument makes no paracompactness claim about \(\mathbb CP^\infty\).

By A.4, \(w_2(L_{\mathbb R})=e_2(L_{\mathbb R})\). The integral Thom class of this canonically oriented plane reduces to its mod-two Thom class: its restrictions to fibres are the coefficient images of the integral positive generator, hence the nonzero mod-two generators. Uniqueness of the Thom class in DG06 T.3 proves the equality of the classes themselves. Pulling them back along the zero section, with the relative condition forgotten, gives
\[
e_2(L_{\mathbb R})=\rho_2 e(L_{\mathbb R})
=\rho_2c_1(L).
\tag{C.9}
\]
The rank convention in A.2 makes all higher real classes of this plane zero. Its total Stiefel–Whitney class is therefore \(1+\rho_2c_1(L)\).

For general \(V\), pull back by the complex flag map \(f:F(V)\to B\). DG08 M.4 is injective with every abelian coefficient group in the complex case, in particular with \(\mathbb F_2\). The pulled-back complex bundle is an actual line sum, so its underlying real bundle is the corresponding direct sum of planes. The real Whitney formula A.3 and the line calculation yield
\[
f^*w(V_{\mathbb R})=
\prod_{j=1}^r\bigl(1+\rho_2c_1(L_j)\bigr).
\tag{C.10}
\]
Every positive factor has degree two. The odd components of this product are zero, and its degree-\(2i\) component is
\(\rho_2 e_i(c_1(L_1),\ldots,c_1(L_r))\).
By B.4 and commutation of \(\rho_2\) with pullback this is \(f^*\rho_2c_i(V)\). Mod-two injectivity proves (C.8). The empty product is one, so this includes rank zero, degree zero and all above-rank indices. □
## 4. Integral evaluation of the top class

### Fundamental classes with their local signs

**Corollary D.1 (oriented compact-support classes).** Let \(M\) be a smooth Hausdorff second-countable oriented \(d\)-manifold without boundary. For each compact \(K\subset M\) there is a unique class
\[
[M]_K\in H_d(M,M\setminus K;\mathbb Z)
\tag{D.1}
\]
restricting to the positive orientation generator at every point of \(K\). Point restrictions detect this degree, and
\[
H_j(M,M\setminus K;\mathbb Z)=0\qquad(j>d).
\tag{D.2}
\]
If \(M\) is compact, \([M]_M=[M]\) is its absolute fundamental class. The classes are compatible under restriction to smaller compact supports.

**Proof.** The positive local generator and its sign under an invertible linear change were constructed in DG06 O.1–O.2. O.3 proves that a smooth coordinate change acts by the sign of its derivative, so the given orientation identifies these generators in overlapping oriented charts. O.4 proves their local coherence and constructs the compatible classes (D.1), using the complete compact-set gluing theorem E.8. Detection by points and the vanishing (D.2), for every compact support, are precisely E.7. Its proof first treats finite unions of convex chart sets by E.6 and then uses finite-chain support to treat general compact sets, so no triangulation or finite-cell hypothesis on \(K\) is needed. These are earlier programme results with the same manifold and coefficient hypotheses. For compact \(M\), the relative complement is empty, giving its absolute class; compatibility is O.4's uniqueness argument. □

### Zeros and the Euler number

**Theorem D.2 (isolated zeros and top Chern evaluation).** Let \(E\to M\) be an oriented real rank-\(d\) bundle over a compact oriented smooth \(d\)-manifold without boundary, where \(d>0\). For a continuous section \(s\) with isolated zeros, define the index at a zero \(x\) by pulling the fibre Thom class back to the local pair and evaluating on the positive base local generator. Then there are finitely many zeros and
\[
\langle e(E),[M]\rangle
=\sum_{s(x)=0}\operatorname{ind}_x(s).
\tag{D.3}
\]
If \(E\) and \(s\) are smooth near \(x\) and the local coefficient derivative \(D s_x\) is invertible, this index is \(\operatorname{sgn}\det_{\mathbb R}(D s_x)\), computed in oriented base and bundle frames.

In particular, for a complex rank-\(r>0\) bundle on a compact oriented smooth \(2r\)-manifold, with its canonical fibre orientation,
\[
\langle c_r(V),[M]\rangle
=\sum_{s(x)=0}\operatorname{ind}_x(s).
\tag{D.4}
\]

**Proof.** The zero set \(Z\) is closed, as follows in each bundle chart from continuity of its coefficient map, and hence is compact. Its isolated-point neighbourhoods cover it; compactness gives a finite subcover, proving finiteness.

The continuous section is a map of pairs \((M,M\setminus Z)\to(E,E^\times)\). Thus it pulls the integral Thom class of DG06 T.3 back to
\(\alpha\in H^d(M,M\setminus Z;\mathbb Z)\).
Forgetting relative conditions gives \(e(E)\): scalar multiplication \(s\mapsto t s\) is a homotopy to the zero section, and homotopy invariance is DG06 K.1.

Choose disjoint oriented coordinate neighbourhoods of the finitely many zeros. Excision DG06 E.2 and the disjoint-simplex decomposition proved in N.2 identify homology relative to \(M\setminus Z\) with the direct sum of local homology groups at these points. By D.1 the image of \([M]\) has the positive generator in each summand. Evaluating \(\alpha\) on this direct sum gives the sum of its evaluations on those generators, which by definition are the indices. Naturality of the evaluation pairing under the map from absolute to relative chains now gives (D.3). This is N.2's complete relative-pullback calculation; each step just listed uses only continuity of the section. If there are no zeros, DG06 T.4 gives zero Euler class and the sum is empty.

For a nondegenerate smooth zero, DG06 N.1 identifies the same local Thom-pullback index with the real determinant sign, using the local inverse theorem and O.3's oriented local generator. Its proof also checks invariance under oriented frame and base-coordinate changes. Thus it applies with exactly the sign convention used here. Finally B.2 defines \(c_r(V)=e(V_{\mathbb R})\) on every Hausdorff base, giving (D.4).

For completeness, the dimension-zero version is read directly on points. A compact zero-dimensional manifold has finitely many points, its oriented fundamental class is the sum of its signed point generators, and the canonically oriented zero bundle has Euler class one. Its evaluation is the sum of those point signs. With the canonical positive point orientations it is the number of points. □
## Free construction sources

- Allen Hatcher, free author [*Vector Bundles and K-Theory*, version 2.2](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), printed pages 79–83: projective characteristic coefficients, the relative-cup proof of the Whitney formula, splitting and the real-complex comparison. The local proofs use the already established arbitrary Hausdorff-base projective module theorem and supply the open-cover deformation, relative product and coefficient normalization.
- José Perea, freely posted [MTH 7375 Lecture 18, 18 November 2024](https://www.joperea.com/s/MTH-7375-FS24-Lecture-18.pdf), PDF pages 2–7: top Chern Euler normalization, conjugation and duals, the lower-rank Gysin construction and its metric-free quotient alternative. The chapter gives all quotient charts, pullback comparisons and deleted-space paracompactness proofs, with its stated Hermitian convention.

The exact earlier programme proofs supply the Thom, Gysin, projective, flag, line, fundamental-class and index arguments cited in the text. Their human construction sources remain credited in those lessons.

Original exposition: GPT-6 Astra (OpenAI), October 2026, CC0 1.0. Human construction sources are credited above. No source prose, diagrams or source PDFs are reproduced.
