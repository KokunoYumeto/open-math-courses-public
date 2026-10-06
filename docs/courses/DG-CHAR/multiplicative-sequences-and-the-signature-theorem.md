# Multiplicative sequences and the signature theorem

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0.*

The signature can be measured from a rational intersection matrix, while Pontryagin numbers come from the tangent bundle. This chapter asks how those two computations can recover one another. We first establish the form and boundary arguments that make signature a bordism invariant. We then calibrate a degree-eight characteristic polynomial on two different manifolds, and use that calculation to motivate the general construction of multiplicative sequences. The formal power series and projective coefficient proof finally turn the calibration into a theorem in every dimension.

The algebraic classification is proved over every commutative coefficient ring, including rings with zero divisors. Manifold genera and signature comparison use rational Pontryagin classes, with integral orientation and boundary signs fixed by the earlier chapters. The all-dimensional product proof accounts for alternating middle forms as well as symmetric ones. These distinctions explain which conclusions follow from a matrix, which follow from bordism, and which require the universal polynomial construction.

The exact prerequisites are [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md), Sections1–2, for compact-support duality and perfect closed pairings; [The oriented cobordism ring](the-oriented-cobordism-ring.md), Section1, for the full collar proof; [Chern classes](chern-classes-and-the-integral-universal-ring.md), Lemma5.1, for integer relative fundamental classes and their boundary sign; [Thom and Euler classes](thom-classes-and-euler-classes.md), for singular products, relative excision and coefficient theorems; [Characteristic numbers](characteristic-numbers-and-projective-product-independence.md), Sections2–5, for integral symmetric classes, product evaluations and boundary vanishing; [Pontryagin classes](pontryagin-classes-and-oriented-universal-cohomology.md), for rational Whitney and projective tangent classes; and [Rational oriented bordism](rational-oriented-bordism-and-projective-generators.md), for the full polynomial-basis theorem. The coefficient rings and orientation conventions in these prerequisites fix those used below.

This is the signature portion of the multiplicative-sequence lesson. Its continuation, [Odd-prime reduced powers and the Wu classes](odd-prime-reduced-powers-and-wu-classes.md), constructs the operations and proves the precise Wu polynomial and homotopy theorem. These two chapters supply the complete signature, multiplicative-sequence and odd-prime teaching. No independent AI review is claimed.

## A. The algebra behind the signature

Throughout this section vector spaces are finite dimensional over \(\mathbb Q\). A bilinear form \(b:V\times V\to\mathbb Q\) is nondegenerate if \(v\mapsto b(v,-)\) is an isomorphism to \(V^*\). For a symmetric nondegenerate form, its signature will count positive diagonal coefficients minus negative ones. We first prove that this is independent of the chosen diagonalization and record the exact vanishing mechanism needed for a boundary.

### A.1. Diagonalization and its invariant counts

**Lemma A.1.** A nondegenerate symmetric form has a basis in which its matrix is diagonal with nonzero rational entries. The numbers of positive and negative diagonal entries are invariant under change of basis.

**Proof.** If \(V\ne0\), some \(v\) has \(b(v,v)\ne0\). Otherwise polarization would give
\[
2b(u,v)=b(u+v,u+v)-b(u,u)-b(v,v)=0
\]
for every \(u,v\), contradicting nondegeneracy. Put \(a=b(v,v)\). Each \(x\) decomposes uniquely as
\[
x=\frac{b(x,v)}a v+\left(x-\frac{b(x,v)}a v\right),
\qquad V=\mathbb Qv\mathbin{\perp}v^\perp.
\tag{A.1}
\]
The second summand is nondegenerate: a vector there orthogonal to it is also orthogonal to \(v\), and hence to all of \(V\). Induction diagonalizes that summand and gives the first assertion, including the zero-dimensional case with its empty diagonal.

Extend scalars to \(\mathbb R\). For a diagonalization with \(p\) positive and \(q\) negative coefficients, its positive-coordinate subspace is positive definite of dimension \(p\). Any positive definite subspace has zero intersection with the negative-coordinate subspace; projection to the positive coordinates is consequently injective on it, giving dimension at most \(p\). Thus \(p\) is the maximum possible dimension of a positive definite subspace, defined without reference to a basis. The identical argument gives \(q\) as the maximum dimension of a negative definite subspace. Both are invariant. ∎

Define \(\operatorname{sign}(b)=p-q\). The proof gives
\[
\operatorname{sign}(b\perp c)=\operatorname{sign}(b)+\operatorname{sign}(c),
\qquad \operatorname{sign}(-b)=-\operatorname{sign}(b).
\tag{A.2}
\]
Indeed concatenate the diagonal bases, or negate every diagonal coefficient. An isometry of forms preserves the signature by Lemma A.1.

### A.2. An isotropic half cancels the entire signature

For a subspace \(L\subset V\), set \(L^\perp=\{v:b(v,L)=0\}\). Restriction of functionals gives a surjection \(V\to L^*\): extend a functional from a basis of \(L\) to one of \(V\), then use nondegeneracy. Its kernel is \(L^\perp\), so
\[
\dim L^\perp=\dim V-\dim L.
\tag{A.3}
\]
Call \(L\) isotropic when \(b(L,L)=0\). It then lies in \(L^\perp\), and (A.3) gives \(2\dim L\leq\dim V\).

**Lemma A.2 — Isotropic-half vanishing.** If a nondegenerate symmetric form has an isotropic subspace of half its dimension, its signature is zero. In particular this holds when \(L=L^\perp\).

**Proof.** Let \(l_1,\ldots,l_h\) be a basis of that subspace. The preceding surjection gives vectors \(w_j\) with \(b(l_i,w_j)=\delta_{ij}\). Put \(a_{ij}=b(w_i,w_j)\) and
\[
v_i=w_i-\frac12\sum_k a_{ki}l_k.
\tag{A.4}
\]
The symmetry of \(a\) gives \(b(v_i,v_j)=a_{ij}-a_{ij}/2-a_{ji}/2=0\), while \(b(l_i,v_j)=\delta_{ij}\). The \(2h\) vectors \(l_i,v_i\) are independent: pairing a relation with each \(l_j\) kills the \(v_j\) coefficients, and then the \(l_i\) basis kills the rest. Their number is \(\dim V\), so they form a basis, with matrix
\[
\begin{pmatrix}0&I_h\\I_h&0\end{pmatrix}.
\tag{A.5}
\]
The vectors \(l_i+v_i,l_i-v_i\) diagonalize this into \(h\) coefficients2 and \(h\) coefficients\(-2\); all cross pairings are zero. Its signature is therefore zero. If \(L=L^\perp\), (A.3) supplies the required half dimension. ∎

For example, a perfect pairing between two summands of equal dimension, with zero pairing within each, has this form after choosing dual bases. An off-diagonal sign or a nonsingular off-diagonal matrix does not change its zero signature: the first summand is still an isotropic half.

### A.3. Alternating and tensor-product forms

**Lemma A.3.** Every nondegenerate alternating form has even dimension and a basis consisting of pairs \(e_i,f_i\) with \(b(e_i,f_j)=\delta_{ij}\), \(b(e_i,e_j)=b(f_i,f_j)=0\). In particular it has an isotropic half-dimensional subspace.

**Proof.** Choose nonzero \(e\). Nondegeneracy gives \(f\) with \(b(e,f)\ne0\), and rescale \(f\) to make that value1. Alternation makes the matrix on their span \(\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), which is nonsingular. Subtract the uniquely determined components in this span from any vector to put it in its orthogonal complement. This gives a direct orthogonal sum with nondegenerate complement, exactly as in (A.1). Repeat. Each step removes two dimensions, and the zero-dimensional last space terminates the induction. The span of all the \(e_i\) is the asserted isotropic half. ∎

If \(b,c\) are symmetric nondegenerate forms, their tensor form is defined on simple tensors by
\[
(b\otimes c)(u\otimes x,v\otimes y)=b(u,v)c(x,y).
\tag{A.6}
\]
Diagonal bases prove nondegeneracy and show that positive products occur for the two equal-sign pairs and negative products for the two opposite-sign pairs. Hence
\[
\operatorname{sign}(b\otimes c)=\operatorname{sign}(b)\operatorname{sign}(c).
\tag{A.7}
\]
If instead both forms are alternating and nondegenerate, (A.6) is symmetric and nondegenerate. Nondegeneracy follows, for example, from the tensor product of the two invertible matrices. If \(L\) is an isotropic half for the first alternating form, \(L\otimes W\) is an isotropic half for their tensor form. Lemma A.2 makes its signature zero. The same conclusion holds for the negative of that tensor form, as may arise from a cohomological product sign. These facts will handle all dimensions in the product formula for manifold signatures.

## B. Relative duality and the boundary pairing

Let \(W\) be a compact smooth oriented \(d\)-manifold, \(M=\partial W\) with its outward-normal-first orientation, and \(U=W\setminus M\). Empty boundaries and disconnected manifolds are allowed. The [cobordism chapter](the-oriented-cobordism-ring.md), Theorem1.1, supplies the full smooth collar. The [Chern chapter](chern-classes-and-the-integral-universal-ring.md), Lemma5.1, supplies the relative fundamental class with \(\partial[W,M]=[M]\). The [manifold chapter](manifold-duality-the-diagonal-and-wu-classes.md), Sections1–2, supplies compact-support Poincaré duality on \(U\), including the right-cap formula and its naturality. We now prove the precise relative comparison needed for a boundary signature.

### B.1. Relative cohomology as compact support on the interior

**Lemma B.1.** There are natural identifications
\[
H^r(W,M;R)\cong H_c^r(U;R),\qquad
H_j(U;R)\cong H_j(W;R),
\tag{B.1}
\]
for every commutative coefficient ring \(R\). They identify right cap with \([W,M]\) with compact-support cap on \(U\).

**Proof.** Use a collar \(M\times[0,1)\subset W\), with \(M\) at height zero. For \(0<a<1/2\), put
\[
A_a=M\times[0,a),\qquad K_a=W\setminus A_a.
\tag{B.2}
\]
The set \(A_a\) is open in \(W\); it retracts to \(M\) by shrinking the height. Its complement \(K_a\) is compact and lies in \(U\). These compact sets are cofinal as \(a\) decreases to zero: any compact subset of \(U\) avoids some collar of height \(a\), by compactness and the fact that the collar heights of points approaching \(M\) tend to zero.

The long exact sequences of the two pairs and the height retraction give an isomorphism
\[
H^r(W,A_a;R)\xrightarrow{\cong}H^r(W,M;R).
\tag{B.3}
\]
It is induced by the identity on \(W\) and the inclusion \(M\subset A_a\); on the neighbouring absolute groups it is the identity and the collar equivalence, so exactness and the five lemma give the isomorphism. Removing \(M\), whose closure lies inside the open \(A_a\), is excision for this pair. It gives
\[
H^r(W,A_a;R)\cong H^r(U,A_a\setminus M;R)
=H^r(U,U\setminus K_a;R).
\tag{B.4}
\]
The excision map in cohomology is justified by the previously proved small-chain deformation equivalence, not by assuming that dualizing an arbitrary homology isomorphism suffices. Both maps in (B.3)–(B.4) commute with decreasing the collar size. Passing to the cofinal filtered direct limit, with the compact-support definition of manifold (1.2), proves the first identification in (B.1).

For the second, choose a smooth nonnegative cutoff \(\chi(t)\) equal to one near zero and zero for \(t\geq1/2\), with values at most one. Choose \(0<\varepsilon<1/4\), and move a collar point by
\[
(x,t)\longmapsto(x,t+s\varepsilon\chi(t)),\qquad0\leq s\leq1,
\tag{B.5}
\]
fixing the complement of the collar. This is continuous and joins the identity to a map \(W\to U\); its heights stay below one and are positive at time one. On \(U\), the entire homotopy stays in \(U\). Thus inclusion \(U\to W\) and that last map are homotopy inverses, proving the homology comparison. If the boundary is empty, both assertions in (B.1) reduce to compact-support cohomology on the compact \(W=U\) and the identity.

To verify cap compatibility, represent a relative cohomology class by a cocycle \(b\) vanishing on all simplices in \(A_a\), using (B.3), and represent \([W,M]\) by a finite relative cycle \(c\). Subdivide \(c\) for the open cover \(A_a,U\), with the small-chain homotopy preserving its boundary subcomplex. Its pieces in \(A_a\) have zero right cap, since their evaluated terminal faces lie in \(A_a\). The remaining pieces lie in \(U\), and their sum has boundary in \(U\cap A_a\). Their local interior values on \(K_a\) are the positive orientation values of \([W,M]\). The compact-set uniqueness theorem consequently identifies their relative class with \(\mu_{K_a}\). Capping those pieces with the restriction of \(b\) is exactly the compact-support duality map on \(U\); inclusion in \(W\) gives \(R_b c\). The prism identity shows that subdivision and changes of these representatives do not change the resulting class. This proves the final assertion. ∎

### B.2. Both Poincaré–Lefschetz maps

**Theorem B.2 — Relative duality in the needed generality.** For oriented compact \(W\), right cap with its relative fundamental class induces
\[
D_{\mathrm{rel}}:H^r(W,M;R)\xrightarrow{\cong}H_{d-r}(W;R)
\tag{B.6}
\]
for every commutative coefficient ring \(R\). Its integer homology groups are finitely generated and vanish above dimension \(d\). Over \(\mathbb Q\), right cap also induces
\[
D_{\mathrm{abs}}:H^r(W;\mathbb Q)\xrightarrow{\cong}H_{d-r}(W,M;\mathbb Q),
\tag{B.7}
\]
and the pairing
\[
H^{d-r}(W,M;\mathbb Q)\times H^r(W;\mathbb Q)\longrightarrow\mathbb Q,
\qquad (y,a)\longmapsto\langle y\smile a,[W,M]\rangle
\tag{B.8}
\]
is perfect.

**Proof.** Compact-support duality on \(U\), composed with the two identifications of Lemma B.1, is an isomorphism. Its cap compatibility identifies it with (B.6), proving the first assertion.

Choose a finite integer relative fundamental cycle \(c\). The cap of a relative cocycle with \(c\) is an absolute cycle: the right-cap boundary formula has \(R_b\partial c=0\) because \(b\) vanishes on boundary simplices, and \(\delta b=0\). In each degree all these caps belong to the subgroup generated by the finitely many front faces of the simplices of \(c\). The subgroup of its cycles is finitely generated, by the proved subgroup theorem for finite-rank free abelian groups. Surjectivity in (B.6) makes homology a quotient of that subgroup, so it is finitely generated. Negative cohomological degrees in (B.6) give zero homology above \(d\).

The boundary \(M\) has finitely generated homology by the closed-manifold theorem. The pair sequence then makes every \(H_j(W,M;\mathbb Z)\) finitely generated as well: it is an extension of a quotient of \(H_j(W)\) by a subgroup of \(H_{j-1}(M)\), and subgroups and quotients of finitely generated abelian groups are finitely generated. Consequently all rational groups used below are finite dimensional.

The rational coefficient theorem identifies \(H^r(W;\mathbb Q)\) with the dual of \(H_r(W;\mathbb Q)\). Combine this with (B.6) in degree \(d-r\). The cap-evaluation identity is
\[
\langle a,R_y c\rangle=\langle a\smile y,c\rangle.
\tag{B.9}
\]
It makes the pairing with factor order \(a,y\) perfect. Graded commutativity changes its order by the fixed sign \((-1)^{r(d-r)}\), so (B.8) is perfect too.

For absolute cocycle \(a\), \(R_a c\) is a relative cycle, since \(R_a\partial c\) lies in \(M\). Changes of the cocycle or relative fundamental representative give relative boundaries by the same right-cap formula. Thus (B.7) is well defined, and its evaluation against \(y\in H^{d-r}(W,M;\mathbb Q)\) is precisely \(\langle y\smile a,c\rangle\). Relative rational cohomology is the dual of relative rational homology; its finite dimension and the perfect pairing (B.8) therefore show that (B.7) is an isomorphism. This proves the asserted absolute map, rather than only equality of dimensions. ∎

### B.3. Restriction and the connecting map are adjoint

Now take \(d=2m+1\), so \(M\) has dimension \(2m\). Let \(i:M\to W\) be inclusion and \(\delta:H^m(M;\mathbb Q)\to H^{m+1}(W,M;\mathbb Q)\) the cohomology connecting map.

**Lemma B.3.** For \(x\in H^m(M;\mathbb Q)\) and \(a\in H^m(W;\mathbb Q)\),
\[
\langle\delta x\smile a,[W,M]\rangle
=\langle x\smile i^*a,[M]\rangle.
\tag{B.10}
\]

**Proof.** Represent \(x\) by a cocycle on \(M\) and extend it to a cochain \(X\) on \(W\), setting any still unspecified simplex values to zero. This is possible because the singular simplices of \(M\) form a subset of the singular-simplex basis of \(W\). Its coboundary vanishes on \(M\), represents \(\delta x\), and is a relative cocycle. For an absolute cocycle \(A\) representing \(a\), the cochain product identity gives
\[
\delta(X\smile A)=\delta X\smile A,
\]
since \(\delta A=0\). Evaluate this identity on a relative fundamental cycle \(c\) with \(\partial c\) in \(M\). Cochain evaluation on a boundary yields
\[
\langle\delta X\smile A,c\rangle
=\langle X\smile A,\partial c\rangle.
\]
The right side evaluates \(x\smile i^*a\) on the boundary fundamental class, because \([\partial c]=[M]\) with the outward convention already proved. This is (B.10), with its sign fixed by that convention. ∎

**Proposition B.4 — The boundary's isotropic half.** For the perfect middle pairing
\[
b_M(x,y)=\langle x\smile y,[M]\rangle
\quad\text{on }H^m(M;\mathbb Q),
\tag{B.11}
\]
the subspace \(L=\operatorname{im}(i^*:H^m(W;\mathbb Q)\to H^m(M;\mathbb Q))\) satisfies \(L=L^\perp\).

**Proof.** If \(x=i^*b\), exactness gives \(\delta x=0\), so (B.10) gives \(b_M(x,i^*a)=0\) for every \(a\). Thus \(L\subset L^\perp\). Conversely if \(x\) is orthogonal to all of \(L\), (B.10) says that \(\delta x\) pairs to zero with every \(a\in H^m(W;\mathbb Q)\). Theorem B.2's perfect pairing, with relative degree \(m+1\) and absolute degree \(m\), forces \(\delta x=0\). The pair sequence then gives \(x\in\operatorname{im}i^*=L\). Hence \(L^\perp\subset L\). Closed-manifold Poincaré duality makes (B.11) nondegenerate, and (A.3) therefore gives \(\dim L=\tfrac12\dim H^m(M;\mathbb Q)\). When \(m\) is even the form is symmetric, and Lemma A.2 proves that its signature is zero. ∎

No assertion that every boundary class extends to \(W\) was needed. The extendable classes are exactly this isotropic half, determined through the actual connecting map and its perfect adjoint pairing.

## C. The signature as a bordism homomorphism

For a smooth closed oriented manifold \(M^{4k}\), \(k\geq0\), define
\[
\sigma(M)=\operatorname{sign}\left(
H^{2k}(M;\mathbb Q),\quad
(x,y)\longmapsto\langle x\smile y,[M]\rangle\right).
\tag{C.1}
\]
The closed-manifold duality theorem makes this a finite-dimensional nondegenerate form. Its degree \(2k\) is even, so the form is symmetric by graded commutativity. Section A proves that the signature is well defined. For dimensions not divisible by four, set \(\sigma(M)=0\). In dimension zero use the signed-point fundamental class; its form has one diagonal coefficient equal to the point's sign, so its signature is the signed count.

### C.1. Additivity, reversal and boundaries

**Theorem C.1 — The three bordism properties.** For smooth closed oriented manifolds,
\[
\sigma(M\sqcup N)=\sigma(M)+\sigma(N),\qquad
\sigma(-M)=-\sigma(M),
\tag{C.2}
\]
and an oriented boundary has signature zero. Also
\[
\sigma(M\times N)=\sigma(M)\sigma(N)
\tag{C.3}
\]
with the ordered product orientation, in every pair of dimensions.

**Proof of sums, reversal and boundaries.** Cohomology and the fundamental class of a finite disjoint union split over its components. The middle form is their orthogonal direct sum: cup products supported on different components are zero. Equation (A.2) gives sum additivity. Reversing the orientation negates \([M]\) and hence the entire form, so (A.2) gives the second equality. In nonmultiple-of-four dimensions these assertions also hold by the zero convention.

If \(M^{4k}=\partial W^{4k+1}\), put \(m=2k\) in Proposition B.4. The restriction image from \(W\) is an isotropic half in this exact middle form, and Lemma A.2 gives zero signature. The proof includes \(k=0\): the form on boundary points has equally many positive and negative diagonal coefficients. When the boundary dimension is not divisible by four its signature is zero by definition. This proves boundary vanishing in every degree.

### C.2. The full product proof

**Proof of the product property.** Let \(a=\dim M\), \(b=\dim N\). If \(a+b\) is not divisible by four, the left side of (C.3) is zero. At least one of \(a,b\) is then not divisible by four, making the right side zero as well. Suppose now \(a+b=4k\) and put \(h=2k\).

The full singular-chain product equivalence and field Künneth theorem proved in the Thom/Euler chapter give
\[
H^h(M\times N;\mathbb Q)=
\bigoplus_{i+j=h}H^i(M;\mathbb Q)\otimes H^j(N;\mathbb Q).
\tag{C.4}
\]
The product fundamental-class convention was proved in the manifold chapter. The cup/external-product sign on simple classes is
\[
(x\times y)\smile(x'\times y')
=(-1)^{j i'}(x\smile x')\times(y\smile y'),
\tag{C.5}
\]
where \(|y|=j\), \(|x'|=i'\). This is the sign already supplied by the earlier chain cross/cup proof. Evaluation can be nonzero only when \(i+i'=a\) and \(j+j'=b\).

Thus the summand indexed by \((i,j)\) pairs only with the summand indexed by \((a-i,b-j)\). These indices still sum to \(h\) and define an involution on (C.4). For a two-element orbit, both individual summands have zero self-pairing and pair perfectly with one another, by the two factor duality pairings and (C.5). Their direct sum is nondegenerate with an isotropic half, so Lemma A.2 gives zero signature. Distinct orbits are orthogonal.

There is a fixed orbit exactly when \(a,b\) are both even; its index is \((a/2,b/2)\). If either dimension is odd there is none, so all of the middle form has signature zero, agreeing with the right side of (C.3).

If \(a,b\) are even, their sum divisible by four makes them either both divisible by four or both congruent to two modulo four. In the first case, their middle degrees are even and the sign \((-1)^{(a/2)(b/2)}\) in (C.5) is positive. The remaining fixed summand has exactly the tensor product of the two symmetric middle forms. Formula (A.7) makes its signature \(\sigma(M)\sigma(N)\), proving (C.3) in that case.

In the second case, both factor middle degrees are odd. Graded commutativity makes their nondegenerate forms alternating, and the sign in (C.5) is negative. Their tensor form, with this sign, has signature zero by Lemma A.3 and its tensor-product consequence. Both factor signatures have been defined to be zero in those dimensions, so (C.3) holds here too. All cases, including zero-dimensional factors, are now covered. ∎

Together the three properties give a unital ring homomorphism
\[
\sigma:\Omega_*\longrightarrow\mathbb Z,
\tag{C.6}
\]
extended additively over finite sums of degrees. It is a homomorphism of ordinary rings; its target is not being assigned the source's degree grading. Boundary vanishing makes it independent of the representative. The positive point maps to one. Tensoring gives a unital \(\mathbb Q\)-algebra homomorphism \(\Omega_*\otimes\mathbb Q\to\mathbb Q\). In particular, any torsion bordism class has signature zero, since a positive integer times its signature would be zero in \(\mathbb Z\).

### C.3. Homotopy invariance and projective values

**Proposition C.2.** An orientation-preserving homotopy equivalence between smooth closed oriented manifolds preserves signature. Also
\[
\sigma(\mathbb {CP}^{2k})=1\quad(k\geq0).
\tag{C.7}
\]

**Proof.** A homotopy equivalence induces an isomorphism of the rational cohomology rings. Orientation preservation means that it carries the source fundamental class to the target fundamental class. Naturality of cup products and evaluation therefore makes its cohomology isomorphism an isometry of the middle forms. Lemma A.1 preserves signature under that isometry. The zero convention handles other dimensions.

For \(\mathbb {CP}^{2k}\), the integral projective-ring and positive-evaluation proof in the Chern chapter gives the degree-two generator \(x\) with \(\langle x^{2k},[\mathbb {CP}^{2k}]\rangle=1\). Its rational middle cohomology is generated by \(x^k\), whose square has that evaluation. Thus its one-by-one middle matrix is \((1)\), proving (C.7). For \(k=0\) this is the positive point. ∎

It follows already that the signature of every projective product \(P_I\) from the rational-bordism chapter is one. The polynomial-basis theorem then determines the signature of any rational bordism class by summing its projective-product coefficients.

For a four-manifold this and rational formula (K.10) give
\[
\sigma(M^4)=\frac{p_1[M]}3.
\tag{C.8}
\]
Since signature is an integer by its definition, this proves divisibility of \(p_1[M]\) by three. For an eight-manifold with \(u=p_1^2[M]\), \(v=p_2[M]\), summing the coefficients in rational (K.12) gives
\[
\sigma(M^8)=\frac{u-2v}{5}+\frac{5v-2u}{9}
=\frac{7v-u}{45}.
\tag{C.9}
\]
Thus \(7p_2[M]-p_1^2[M]\) is divisible by45. These are the first two signature polynomials, obtained directly from the already proved rational bordism basis. The next section will identify every degree with the multiplicative sequence defined by the formal \(L\)-series.

### Calibrating a polynomial with two experiments

The degree-eight case explains why one projective example is not enough to identify a characteristic polynomial. Write a candidate as
\[
P[M]=\alpha p_1^2[M]+\beta p_2[M].
\]
The complete projective tangent and product calculations in the earlier chapters give

| Manifold, with complex orientation | \(p_1^2[M]\) | \(p_2[M]\) | Signature |
| --- | --- | --- | --- |
| \(\mathbb {CP}^4\) | \(25\) | \(10\) | \(1\) |
| \(\mathbb {CP}^2\times\mathbb {CP}^2\) | \(18\) | \(9\) | \(1\) |

For the first row, \(p=(1+x^2)^5\) and \(\langle x^4,[\mathbb {CP}^4]\rangle=1\). For the second, \(p_1=3x^2+3y^2\), \(p_2=9x^2y^2\), and \(\langle x^2y^2,[\mathbb {CP}^2\times\mathbb {CP}^2]\rangle=1\); the pure fourth powers vanish on their four-dimensional factors. The signature values follow from Proposition C.2 and the complete product proof.

Requiring the candidate to agree with those signatures gives
\[
25\alpha+10\beta=1,\qquad18\alpha+9\beta=1.
\]
The determinant is \(45\), so the unique solution over \(\mathbb Q\) is
\[
\alpha=-\frac1{45},\qquad\beta=\frac7{45}.
\tag{P.1}
\]
The rational-bordism theorem proves that these two projective products span the entire degree-eight rational bordism group. Both signature and the two Pontryagin numbers are linear on that group; their agreement on a basis therefore proves the formula for every closed oriented eight-manifold. Torsion contributes zero to each rational characteristic number and to signature. This is the reason the two experiments suffice; their numerical agreement alone would not establish a theorem for all manifolds.

There is a useful zero-signature check on \(S^4\times S^4\). Its middle cohomology has basis \(u,v\), pulled back from the two positive sphere generators. Their squares vanish and \(\langle uv,[S^4\times S^4]\rangle=1\), so the middle matrix is
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The vectors \(u+v,u-v\) have diagonal values \(2,-2\), giving signature zero. The radial normal vector on \(S^4\subset\mathbb R^5\) gives \(TS^4\oplus\varepsilon^1\cong\varepsilon^5\); the product tangent bundle is likewise stably trivial. Thus both Pontryagin numbers in (P.1) are zero, and the polynomial agrees with the middle-form computation. The vanishing here comes from a balanced form, not from vanishing middle cohomology.

The next part supplies the universal multiplicative-polynomial construction. Its role is to identify one compatible sequence in every degree, rather than solving an unrelated linear system in each dimension. The final formal residue calculation verifies its value on every projective generator and completes that all-dimensional comparison.

## D. Multiplicative sequences from a power series

Let \(A\) be a commutative ring with unit. A weight-graded \(A\)-algebra here is commutative in the ordinary sense, with no sign in its multiplication; the characteristic-class application uses degrees divisible by four, so this convention agrees with cup multiplication. Its degree completion consists of sequences, with multiplication by the finite convolution in each degree. In particular \(1+a_1+a_2+\cdots\) is invertible by recursively solving for its inverse coefficients.

A **multiplicative sequence** consists of polynomials \(K_n(a_1,\ldots,a_n)\), homogeneous of weight \(n\) when \(a_j\) has weight \(j\), with \(K_0=1\), such that
\[
K(ab)=K(a)K(b),\qquad K(a)=1+\sum_{n\geq1}K_n(a_1,\ldots,a_n),
\tag{D.1}
\]
for all such completed units in every weight-graded commutative \(A\)-algebra.

### D.1. Existence and uniqueness, over an arbitrary coefficient ring

**Theorem D.1 — Classification of multiplicative sequences.** Given
\[
f(t)=1+f_1t+f_2t^2+\cdots\in A[[t]],
\tag{D.2}
\]
there is a unique multiplicative sequence with \(K(1+t)=f(t)\) when \(t\) has weight one. If \(s_I\) is the stable integral monomial symmetric polynomial from the characteristic-number chapter, its formula is
\[
K_n(a_1,\ldots,a_n)=\sum_{I\vdash n}f_I s_I(a_1,\ldots,a_n),
\qquad f_I=\prod_{j\in I}f_j.
\tag{D.3}
\]
Each repeated part contributes its repeated factor to this product, and each distinct monomial in an orbit sum occurs once.

**Proof.** For variables \(t_1,\ldots,t_N\) of weight one, expansion gives
\[
\prod_{j=1}^N f(t_j)=\sum_I f_I m_I(t_1,\ldots,t_N).
\tag{D.4}
\]
Indeed each term chooses one exponent on each variable. The multiset of its positive exponents determines its partition \(I\) and its coefficient is exactly \(f_I\). Repeated exponents do not introduce extra copies of the same monomial. In every fixed weight only finitely many terms occur. The full integral symmetric-polynomial theorem, and the stable orbit-sum proof in characteristic-number Lemma2.1, express its weight-\(n\) part as (D.3) with \(a_i=e_i(t)\). Those integer polynomial identities may be evaluated in any \(A\); no division by a stabilizer or coefficient is needed.

For two disjoint root lists \(t,u\), multiply the products in (D.4). Their elementary sequences convolve, exactly as the coefficients of
\(\prod(1+t_j z)\prod(1+u_j z)\). Thus the root identity gives the weight-\(n\) part of (D.1). Choose each root list with at least \(n\) variables. The two lists' elementary symmetric functions through degree \(n\) are algebraically independent over \(A\): the proved monomial/elementary basis theorem over \(\mathbb Z\), extended coefficientwise to \(A\), shows that a polynomial relation has every coefficient zero. Hence the root identity is an identity in the independent variables \(a_i,b_i\). It can be substituted in every weight-graded commutative \(A\)-algebra, proving existence and full multiplicativity. With just one root, (D.4) gives \(K(1+t)=f(t)\).

For uniqueness, apply any sequence satisfying (D.1) to
\(a=\prod_{j=1}^N(1+t_j)\). Multiplicativity forces its value to be \(\prod_j f(t_j)\). Algebraic independence of the elementary functions for \(N\geq n\) forces each polynomial \(K_n\) to equal (D.3). This proves uniqueness over \(A\), including rings with zero divisors. ∎

For example, using the integral symmetric formulas already proved,
\[
K_1=f_1a_1,\qquad
K_2=f_2(a_1^2-2a_2)+f_1^2a_2,
\tag{D.5}
\]
and
\[
K_3=f_3(a_1^3-3a_1a_2+3a_3)
+f_2f_1(a_1a_2-3a_3)+f_1^3a_3.
\tag{D.6}
\]
The monomial-symmetric description gives both a direct construction and the coefficients needed for calculations.

**Coefficient reciprocity.** The same sequence has the second universal formula
\[
K_n(a_1,\ldots,a_n)=\sum_{I\vdash n}s_I(f_1,\ldots,f_n)a_I,
\qquad a_I=\prod_{j\in I}a_j.
\]
Here the arguments of \(s_I\) are elementary-symmetric coordinates, just as in (D.3). Thus each coefficient of an ordinary characteristic monomial can be read from one symmetric polynomial in the coefficients of the defining series.

To prove the formula without assuming that elements of \(A\) have roots, work first over \(\mathbb Z\) with two independent lists \(u_1,\ldots,u_N\) and \(t_1,\ldots,t_M\), where \(N,M\geq n\). Substitute \(f_i=e_i(u)\) and \(a_i=e_i(t)\), and use the finite series \(f(z)=\prod_j(1+u_jz)\). The root construction (D.4) becomes
\[
\prod_{i=1}^{M}f(t_i)=\prod_{i=1}^{M}\prod_{j=1}^{N}(1+u_jt_i).
\]
Group instead by the variables \(u_j\). For a fixed \(j\), the coefficient of \(u_j^r\) in its factors is \(e_r(t)=a_r\). In degree \(n\) in each list, grouping the positive exponents into a partition \(I\) therefore gives \(m_I(u)a_I\), with every distinct exponent placement counted once. Since \(m_I(u)=s_I(e_1(u),\ldots,e_n(u))\), this gives the displayed reciprocity identity after substitution. Elementary-symmetric coordinates in each list are algebraically independent over \(\mathbb Z\), so the identity already holds in the independent symbols \(f_1,\ldots,f_n,a_1,\ldots,a_n\). Finally substitute these symbols in any commutative \(A\). Coefficients beyond \(n\) never enter, so the argument covers infinite defining series and rings with zero divisors. For example, the coefficients of \(a_1^2\) and \(a_2\) are respectively \(f_2\) and \(f_1^2-2f_2\), in agreement with (D.5). ∎

### D.2. A genus is a ring homomorphism

Now take \(A=\mathbb Q\). For a closed oriented \(4n\)-manifold define the genus
\[
K[M]=\langle K_n(p_1(TM),\ldots,p_n(TM)),[M]\rangle,
\tag{D.7}
\]
and set it to zero in dimensions not divisible by four. In degree zero it is the signed count. All polynomials use tangent Pontryagin classes; the weight corresponds to one quarter of the cohomological degree.

**Theorem D.2 — Genus homomorphism.** This defines a unital ring homomorphism \(\Omega_*\to\mathbb Q\), and hence a \(\mathbb Q\)-algebra homomorphism \(\Omega_*\otimes\mathbb Q\to\mathbb Q\).

**Proof.** Additivity and orientation reversal follow by evaluating on component fundamental classes. Each positive-degree value is a rational linear combination of Pontryagin numbers, whose boundary vanishing was proved integrally. Degree zero uses the signed-count boundary proof. Thus the value depends only on the bordism class.

For a product, the tangent bundle is the sum of the pulled-back tangent bundles. The integral two-torsion difference in the Pontryagin Whitney formula vanishes after rational coefficient change, so (D.1) gives
\[
K(p(T(M\times N)))=K(p(TM))\times K(p(TN)).
\tag{D.8}
\]
If both dimensions are divisible by four, evaluation in the product top degree takes the top component in each factor. The proved product fundamental-class formula then gives \(K[M\times N]=K[M]K[N]\); every degree in question is even and the product sign is positive. If either dimension is not divisible by four, no class of degree divisible by four can have that factor's top degree. The same expansion has zero product evaluation whenever the total dimension is divisible by four, and the genus's zero convention handles the other total dimensions. Both sides are again equal. The positive point has value \(K_0=1\). This proves the ordinary unital ring homomorphism and its rational extension. ∎

**The converse: prescribing a rational genus.** Let \(B\) be any commutative \(\mathbb Q\)-algebra with unit. Every unital \(\mathbb Q\)-algebra homomorphism
\[
\varphi:\Omega_*\otimes\mathbb Q\longrightarrow B
\]
comes from a unique series \(f(t)\in1+tB[[t]]\) by evaluating its multiplicative sequence on tangent Pontryagin classes. This includes the usual case \(B=\mathbb Q\); no integral-domain hypothesis is needed.

First, the genus construction works over \(B\). In dimension \(4n\), express \(K_n\) as a finite \(B\)-linear combination of Pontryagin monomials, evaluate each monomial's rational number, and multiply by its coefficient in \(B\). The rational boundary identities and universal product identities used in Theorem D.2 remain identities after this coefficient substitution. Their finite sums prove boundary invariance and multiplicativity over \(B\), including products with a factor of dimension not divisible by four. The signed count and unit in degree zero give a unital homomorphism.

Write \(g_n=\varphi[\mathbb {CP}^{2n}]\) for \(n\geq1\). The exact projective tangent formula and (D.4) give
\[
K[\mathbb {CP}^{2n}]=[t^n]f(t)^{2n+1}
=(2n+1)f_n+R_n(f_1,\ldots,f_{n-1}),
\]
where \(R_n\) is an integer polynomial. Indeed the terms containing \(f_nt^n\) choose it in exactly one of the \(2n+1\) factors, while every other contribution has only smaller positive exponents. Since \(2n+1\) is a unit in every \(\mathbb Q\)-algebra, recursively set
\[
f_n=\frac{g_n-R_n(f_1,\ldots,f_{n-1})}{2n+1}.
\]
This defines a unique infinite series; each step uses only the previously defined finite list. Its genus equals \(\varphi\) on every projective generator and on the positive point. The proved polynomial description of rational oriented bordism then makes the two homomorphisms equal on all products and finite linear combinations. The same recursion proves uniqueness. In particular a unital homomorphism \(\Omega_*\to\mathbb Q\) extends uniquely to rational bordism and is obtained this way: its extension sends \(x\otimes q\) to \(q\varphi(x)\), so torsion is killed and the tensor relations are respected. ∎

## E. The formal L-series and the signature theorem

All power series and residues below are formal over \(\mathbb Q\). They require no analytic convergence or complex-integration theorem.

Define the even series
\[
\frac{s\cosh s}{\sinh s}=\frac{s}{\tanh s}
=f_L(s^2),
\qquad
f_L(t)=1+\frac t3-\frac{t^2}{45}+\frac{2t^3}{945}+\cdots.
\tag{E.1}
\]
Here \(\sinh s=s(1+s^2/6+\cdots)\) and \(\cosh s=1+s^2/2+\cdots\), using their factorial-coefficient definitions. After cancelling \(s\), division by the even unit series uniquely defines \(f_L\). Let \(L_n\) be its multiplicative sequence from Theorem D.1. Substituting the first coefficients in (D.5)–(D.6) gives
\[
L_1=\frac{p_1}{3},\qquad
L_2=\frac{7p_2-p_1^2}{45},\qquad
L_3=\frac{62p_3-13p_1p_2+2p_1^3}{945}.
\tag{E.2}
\]
For instance the coefficient of \(p_2\) in \(L_2\) is \(2/45+1/9=7/45\), retaining the repeated-root convention of (D.3).

### E.1. A formal change of variable for a coefficient

For a formal Laurent series with only finitely many negative powers, define \(\operatorname{Res}_s g(s)\,ds\) to be its coefficient of \(s^{-1}\).

**Lemma E.1 — Formal residue substitution.** If \(u(s)=s+O(s^2)\), then
\[
\operatorname{Res}_s g(u(s))u'(s)\,ds
=\operatorname{Res}_u g(u)\,du.
\tag{E.3}
\]

**Proof.** For a monomial \(g(u)=u^j\) with \(j\ne-1\), its substituted expression is the derivative of \(u(s)^{j+1}/(j+1)\). A derivative of a Laurent series has zero residue: the only possible source, its constant term, differentiates to zero. For \(j=-1\), write \(u(s)=s v(s)\), where \(v\) is a unit power series. Then \(u'/u=s^{-1}+v'/v\), and the second summand is a power series, so its residue is one. This proves the monomial assertion. The negative part of \(g\) is finite; its nonnegative part, after substitution and multiplication by \(u'\), has no negative powers at all. Linearity therefore proves (E.3) for the stated series without an infinite negative-power interchange. ∎

### E.2. All projective L-genera are one

**Proposition E.2.** For every \(k\geq0\), \(L[\mathbb {CP}^{2k}]=1\).

**Proof.** With the positive projective generator \(x\), the earlier exact tangent computation gives \(p(T\mathbb {CP}^{2k})=(1+x^2)^{2k+1}\), truncated in the projective ring. The root identity of Theorem D.1 gives
\[
L(p(T\mathbb {CP}^{2k}))=f_L(x^2)^{2k+1}
=\left(\frac{x}{\tanh x}\right)^{2k+1}.
\tag{E.4}
\]
Positive top evaluation makes its genus the coefficient of \(x^{2k}\). Thus it is
\[
\operatorname{Res}_x\frac{dx}{(\tanh x)^{2k+1}}.
\tag{E.5}
\]
Let \(u=\tanh x\). It has linear term \(x\) and hence a unique inverse series, found recursively by solving each coefficient after the first. Differentiating the quotient of the formal sinh and cosh series gives \(u'=1-u^2\). The identity \(\cosh^2x-\sinh^2x=1\) used here follows from their expressions in \(\exp(x),\exp(-x)\), whose product is one by the binomial coefficient identity in every positive degree. All divisions are by unit series after the leading power of \(x\) has been separated.

Apply (E.3) to
\(g(u)=u^{-(2k+1)}(1-u^2)^{-1}\). Its substituted differential is precisely (E.5), so that residue equals
\[
\operatorname{Res}_u \frac{u^{-(2k+1)}}{1-u^2}\,du
=[u^{2k}]\sum_{j\geq0}u^{2j}=1.
\tag{E.6}
\]
This includes \(k=0\), also represented by the positive point. ∎

### E.3. The theorem in every dimension

**Theorem E.3 — Hirzebruch signature theorem.** For every smooth closed oriented \(4k\)-manifold, possibly disconnected,
\[
\sigma(M)=\left\langle L_k(p_1(TM),\ldots,p_k(TM)),[M]\right\rangle.
\tag{E.7}
\]
Consequently its L-genus is an integer and depends only on its oriented homotopy type.

**Proof.** Theorem C.1 makes signature a unital algebra homomorphism on \(\Omega_*\otimes\mathbb Q\). Theorem D.2 does the same for the L-genus. The rational-bordism chapter proves that this algebra is freely generated by the classes \([\mathbb {CP}^{2i}]\), \(i\geq1\), with the positive point as unit. On each generator, Proposition C.2 and Proposition E.2 make both values equal to one. Unital algebra homomorphisms agreeing on every polynomial generator agree on every monomial and every finite linear combination. Hence they agree on all rational bordism classes, proving (E.7). Its integrality follows from the signature definition, and its oriented homotopy invariance follows from Proposition C.2. ∎

**Signatures of projective fibrations.** Let \(\pi:E\to B\) be a smooth bundle with fibre \(\mathbb {CP}^n\), \(n\geq0\), and structure group \(\operatorname{PGL}(n+1,\mathbb C)\). Suppose \(B\) is smooth, closed and oriented, and orient \(E\) by the base orientation followed by the fibre's complex orientation. Then
\[
\sigma(E)=\sigma(B)\sigma(\mathbb {CP}^n).
\]
Disconnected bases and total spaces are permitted. The structure group need not lift to a vector-bundle structure group. For an empty base both sides are zero; assume it is nonempty in the following proof.

The vertical tangent bundle \(T_\pi E\) is complex because all transition maps are complex projective transformations. The projective tangent calculation makes
\(h=c_1(T_\pi E)/(n+1)\in H^2(E;\mathbb Q)\) restrict to the positive projective generator. Hence
\[
H^q(E;\mathbb Q)=\bigoplus_{i=0}^{n}\pi^*H^{q-2i}(B;\mathbb Q)h^i.
\]
The module proof needs only the local product and these global fibre-basis classes. Over a trivializing open set, the vertical tangent bundle is the pullback of the fibre tangent bundle, so \(h\) is its positive fibre generator. The chain-product equivalence and finite free fibre cohomology make the displayed map an isomorphism there. Choose a finite trivializing cover of compact \(B\). Every finite intersection is contained in a trivializing open set. The small-chain Mayer–Vietoris sequences commute with the displayed maps; induction on the cover, with the same induction for its intersections with the last member, and the five lemma give the global isomorphism. This is the full gluing argument of the earlier projective-bundle module theorem, and uses no vector-bundle lift.

Write \(b=\dim B\). For a top-degree base class \(\beta\),
\[
\langle\pi^*\beta\,h^n,[E]\rangle=\langle\beta,[B]\rangle.
\]
Check this first on a local orientation generator supported in a base ball. Its inverse image is a product with the fibre, and the positive fibre class has \(n\)-th power evaluating to one. The product fundamental-class convention gives the stated sign. Such local generators span the top cohomology on each component, proving the formula.

If \(b+2n\) is not divisible by four, the total signature and at least one factor on the right are zero. Otherwise write \(b+2n=4k\) and equip \(V=H^{2k}(E;\mathbb Q)\) with its nondegenerate middle form. Let \(F^rV\) be the sum of the displayed terms of base degree at least \(r\). Products of base degrees summing to more than \(b\) vanish, so \(F^rV\) is orthogonal to \(F^{b-r+1}V\). A term of base degree \(s\) has fibre exponent \(i=(2k-s)/2\); its complementary base degree \(b-s\) has exponent \(n-i\). Both are allowed together or both absent. Poincaré duality gives equal dimensions of these complementary terms. Summing gives \(\dim F^rV+\dim F^{b-r+1}V=\dim V\), and therefore
\[
(F^rV)^\perp=F^{b-r+1}V.
\]
Here \(b\) is even. Thus \(L=F^{b/2+1}V\) is isotropic and \(L^\perp=F^{b/2}V\).

A symmetric form has the signature of \(L^\perp/L\) for any isotropic \(L\). Indeed the quotient is nondegenerate since \((L^\perp)^\perp=L\). A lift \(W\subset L^\perp\) of its basis has that nondegenerate form, so \(V=W\oplus W^\perp\). The complement contains \(L\) and has dimension \(2\dim L\); Lemma A.2 makes its signature zero. This proves the reduction. In our filtration the quotient has base degree \(b/2\) and would require fibre exponent \(n/2\). If \(n\) is odd it is absent and the total signature is zero. If \(n\) is even it is \(H^{b/2}(B;\mathbb Q)h^{n/2}\), with exactly the base pairing by the top-degree normalization. In this case \(b\) is divisible by four and the total signature is \(\sigma(B)\). These are precisely the two values of \(\sigma(\mathbb {CP}^n)\). The formulas include \(n=0\) and empty manifolds. ∎

**Signatures represented by degree-two classes.** Let \(M^{4k+2}\) be smooth, closed and oriented, \(k\geq0\). Every \(x\in H^2(M;\mathbb Z)\) is represented by the oriented zero set of a transverse section of a smooth complex line bundle with first Chern class \(x\). Its signature depends only on \(x\); call it \(\tau(x)\). More generally, transverse sections of the direct sum of line bundles for \(x_1,\ldots,x_r\) have a common zero set whose signature depends only on the classes; call it \(\tau(x_1,\ldots,x_r)\). If the real normal rank \(2r\) exceeds the manifold dimension, the transverse zero set is empty and the value is zero. Then
\[
\tau(x+y)=\tau(x)+\tau(y)-\tau(x,y,x+y).
\]

For empty \(M\) the assertion is immediate. Otherwise first supply line-bundle existence. Its unit-scalar quotient is \(\mathbb {CP}^\infty\). To verify contractibility upstairs over \(\mathbb C\), let \(T\) insert a zero first coordinate. The homotopy \(((1-t)v+tTv)/\|(1-t)v+tTv\|\) joins \(v\) to \(Tv\): for \(t>0\), the coordinate after the last nonzero coordinate of \(v\) prevents the denominator from vanishing, and at \(t=0\) it is one. The homotopy \(\cos(\pi t/2)Tv+\sin(\pi t/2)e_1\) then joins \(Tv\) to \(e_1\); the summands are perpendicular. Each finite sphere stage times the compact parameter interval maps continuously into a finite stage, and the compact-product direct-limit lemma proves joint continuity. Thus the infinite unit sphere is contractible. The projection has the disk-parameter homotopy lifting property: the projection-path transport proof identifies the image lines of a homotopy of orthogonal projections with their initial lines, fixing time zero; normalize the transported initial unit vectors. Compact parameter images lie in finite projective stages, so that proof and the compact-product topology apply. The proof of the fibration homotopy sequence uses exactly these disk lifts. Contractibility upstairs and the circle covering \(\mathbb R\to S^1\) thus give \(\pi_2(\mathbb {CP}^\infty)=\mathbb Z\) and all other positive homotopy groups zero. The tautological first Chern class evaluates to minus one on the positive projective line, hence is a normalized generator after choosing this sign for \(\pi_2\). Here is the needed integral representation argument on a CW complex \(X\). Represent the desired class by a cellular degree-two integer cocycle \(a\). Send the one-skeleton to the basepoint, and map each two-cell modulo its boundary to a sphere representing its integer \(a(e)\) in the normalized \(\pi_2\). For a three-cell, its attaching sphere then has target Hurewicz class \(a(\partial e)=0\): these are precisely its oriented cellular incidence coefficients. The first Hurewicz isomorphism in the simply connected target makes it null homotopic, so extend over that cell. Every later attaching sphere has dimension at least three and extends since that target homotopy group is zero. The CW characteristic topology makes all extensions continuous, including infinitely many cells. The pullback first Chern class has the prescribed two-cell values, hence is \(a\) by the proved cellular/singular comparison. This proves existence over \(\mathbb Z\); it does not infer it from the earlier mod-two representation theorem.

The finite-domination proof gives maps \(a:M\to K\), \(b:K\to M\) to and from a finite CW complex, with \(ba\simeq\mathrm{id}_M\). Represent \(b^*x\) on \(K\) and compose its classifying map with \(a\). Its pullback class is \(x\), and its compact image lies in a finite projective stage. Replace it by a smooth homotopic map as follows. Embed that finite projective manifold in Euclidean space and take a smooth tubular retraction. A finite smooth partition-of-unity average of nearby image points uniformly approximates the continuous map. Choose the error smaller than the distance of the compact image to the complement of the tubular neighbourhood. Retracting this average gives a smooth map; retracting its straight-line homotopy with the original map proves homotopy. The smooth pullback tautological line is the desired bundle.

A finite chart cover and subordinate smooth functions give finitely many global sections spanning each fibre. Adding their real linear combinations to a section gives a finite-parameter family whose parameter derivative surjects onto the fibre. Parametric transversality supplies a transverse section. For a sum of lines take spanning sections in each summand. Apply the same argument to every partial sum; each has a measure-zero set of bad parameters by Sard's theorem. Avoid their finite union. This also makes the successive codimension-two intersections transverse. Orient the normal bundle by the ordered complex line orientations.

Let \(Y\) be this common zero set and \(i:Y\hookrightarrow M\). Transversality identifies its normal bundle with \(\bigoplus_jL_j|_Y\), so
\[
TY\oplus\bigoplus_j(L_j)_{\mathbb R}|_Y\cong TM|_Y.
\]
For every complementary-degree rational class \(\alpha\), the Thom normalization gives
\[
\langle i^*\alpha,[Y]\rangle
=\langle\alpha\,x_1\cdots x_r,[M]\rangle.
\]
Indeed the relative pullback Thom class lies in \(H^{2r}(M,M-Y;\mathbb Z)\). Its image in absolute cohomology is the Euler class \(x_1\cdots x_r\), because the section is homotopic to the zero section after passing to absolute cohomology. Excision in the tubular neighbourhood of its transverse zeros identifies cap with this class with \([Y]\): the normal derivative preserves the chosen normal orientation, and the Thom generator caps the normal disk to its positive centre. The product convention and uniqueness of local fundamental classes give the global evaluation, also for disconnected zero sets.

The real bundle of a complex line has Pontryagin series \(1+x_j^2\). Rational Whitney multiplication and the tangent-normal identity give
\[
L(TY)=i^*L(TM)\prod_j\frac{\tanh x_j}{x_j}.
\]
Each quotient is a formal unit series; it does not divide by the cohomology class \(x_j\). The signature theorem on \(Y\), followed by the evaluation formula, gives
\[
\tau(x_1,\ldots,x_r)
=\big\langle L(TM)\prod_j\tanh x_j,[M]\big\rangle.
\]
The top-degree component is understood. If \(\dim Y\) is not divisible by four, this component is zero because its degrees are congruent to \(2r\) modulo four whereas \(\dim M=4k+2\). If \(2r>\dim M\) it is zero as well. In other cases the signature theorem proves it directly. This proves representative independence and symmetry in the list: exchanging two real rank-two normal factors has sign \((-1)^4=1\).

Finally put \(A=\tanh x\), \(B=\tanh y\), \(C=\tanh(x+y)\). The formal exponential identity gives \(C(1+AB)=A+B\), hence \(C=A+B-ABC\); the denominator has constant term one. Positive-degree classes are nilpotent on \(M\), so substitute these identities degree by degree. Multiply by \(L(TM)\), evaluate, and apply the common-zero formula to \(x,y,x+y\). This proves the addition law. ∎

For example, let \(x\) be the positive generator on \(\mathbb {CP}^3\). Here \(L(TM)=1+4x^2/3\) and \(\tanh(mx)=mx-m^3x^3/3\), so \(\tau(mx)=(4m-m^3)/3\). Thus \(\tau(x)=1\) and \(\tau(2x)=0\). The triple formula gives \(\tau(x,x,2x)=2\) from its leading product \(2x^3\). The addition law reads \(0=1+1-2\), exhibiting the correction term explicitly.


### E.4. The A-hat sequence as a comparison

Another series is
\[
f_{\widehat A}(t)=\frac{\sqrt t/2}{\sinh(\sqrt t/2)}
=1-\frac t{24}+\frac{7t^2}{5760}+\cdots.
\tag{E.8}
\]
It is defined formally by cancelling the leading power and dividing the resulting even unit series, just as in (E.1). Theorem D.1 yields
\[
\widehat A_1=-\frac{p_1}{24},\qquad
\widehat A_2=\frac{7p_1^2-4p_2}{5760}.
\tag{E.9}
\]
The genus theorem gives a rational bordism homomorphism. For example, \(\widehat A[\mathbb {CP}^2]=-1/8\), while \(\widehat A[\mathbb {CP}^4]=3/128\), using the previously computed Pontryagin numbers. Thus this genus is not generally an integer on all oriented manifolds. Additional spin and index-theoretic conclusions require the corresponding further hypotheses and proofs; only the formal multiplicative sequence and these checked values are asserted here.

## F. Exercises with complete solutions

**Exercise F.1 — Easy: the first two L-polynomials.** Divide the defining even series through weight two, and use the monomial-symmetric formula to compute \(L_1,L_2\).

**Solution.** The defining quotient is
\[
\frac{1+t/2+t^2/24+O(t^3)}{1+t/6+t^2/120+O(t^3)}.
\]
Write it as \(1+a t+b t^2+O(t^3)\). Multiplication by the denominator gives \(a+1/6=1/2\), hence \(a=1/3\), and \(b+a/6+1/120=1/24\), hence \(b=-1/45\). Formula (D.5) then gives \(L_1=p_1/3\) and
\[
L_2=-\frac{p_1^2-2p_2}{45}+\frac{p_2}{9}
=\frac{7p_2-p_1^2}{45}.
\]
The \(f_1^2\) term corresponds to the partition \((1,1)\), whose orbit sum is \(e_2\); it occurs once, so no extra factor two enters. ∎

**Exercise F.2 — Medium: a boundary with six middle classes.** Suppose \(M=\partial W\) is four-dimensional and \(\dim H^2(M;\mathbb Q)=6\). Determine the dimension of the extendable subspace and the positive/negative indices of its intersection form. Explain why one cannot conclude that every class extends.

**Solution.** Proposition B.4 identifies the restriction image \(L\) with its orthogonal complement. Nondegeneracy and (A.3) give \(\dim L=3\). Choose its basis and dual partners; the correction (A.4) makes the partners isotropic as well. The resulting Gram matrix is (A.5) with \(h=3\), so it has three positive and three negative coefficients. In particular the signature is zero. The restriction image has dimension three, strictly below six, so exactly this subspace extends; the remaining classes have nonzero connecting class in \(H^3(W,M;\mathbb Q)\). Merely knowing that a form is isotropic on some subspace would not suffice; the perfect relative pairing is what proves its half dimension. ∎

**Exercise F.3 — Medium: integral restrictions from rational formulas.** Obtain integral divisibility conditions on the Pontryagin numbers of closed oriented manifolds in dimensions four and eight. Check them on \(\mathbb {CP}^2\), \(\mathbb {CP}^4\) and \(\mathbb {CP}^2\times\mathbb {CP}^2\), and under orientation reversal.

**Solution.** Signature counts diagonal signs, so is an integer. Equations (C.8)–(C.9) therefore give
\[
3\mid p_1[M^4],\qquad
45\mid 7p_2[M^8]-p_1^2[M^8].
\]
For \(\mathbb {CP}^2\), its number3 gives signature1. For \(\mathbb {CP}^4\), its numbers \((u,v)=(25,10)\) give \((70-25)/45=1\). For the product, \((18,9)\) gives \((63-18)/45=1\), also the product of its two factor signatures. Orientation reversal negates the fundamental class, so it negates both top number evaluations, including \(p_1^2[M]\), and the signature. The divisibility assertions are preserved. This does not negate the cohomology class \(p_1^2\); it negates its evaluation. ∎

**Exercise F.4 — Hard: the proof from rational bordism.** Use the proved polynomial bordism ring and the projective coefficient identity to show the equality of signature and L-genus for every oriented closed manifold. Account for torsion and for degree zero.

**Solution.** The boundary and full product proofs make signature an ordinary unital ring homomorphism to \(\mathbb Z\), hence an algebra homomorphism on rational bordism to \(\mathbb Q\). The multiplicative-sequence and genus proofs make the L-genus another such algebra homomorphism. On each generator \([\mathbb {CP}^{2i}]\), the middle form is \((1)\) and the formal residue calculation (E.5)–(E.6) gives L-genus1. Hence the two homomorphisms agree on generators, on their products, and on every finite rational sum of those products. The rational-bordism polynomial theorem says these sums exhaust the algebra, proving equality.

Each integral manifold maps into that rational algebra. A torsion bordism class maps to zero there; its signature is zero because \(\mathbb Z\) has no torsion, and its L-genus is zero because \(\mathbb Q\) has none. Thus no integral torsion contribution was lost. The positive point is the unit, and both homomorphisms take it to one; signed zero-manifolds are covered by linearity. The other degrees give zero by the definitions. This proves the theorem with all these cases retained. ∎

**Exercise F.5 — Medium: six middle classes on a four-torus.** Let \(T^4\) have its ordered product orientation. Using the four degree-one circle generators \(a,b,c,d\), give three orthogonal middle-form blocks and compute its signature.

**Solution.** The circle computation and field product theorem give \(H^*(T^4;\mathbb Q)=\Lambda(a,b,c,d)\), with \(\langle abcd,[T^4]\rangle=1\). Its degree-two basis can be grouped as
\[
(ab,cd),\qquad(ac,bd),\qquad(ad,bc).
\]
Only complementary pairs have nonzero products. Their evaluations are respectively1, \(-1\), and1: the middle exchange in \(acbd\) has one transposition, while \(adbc\) has two. Degree-two classes commute, so the three Gram blocks are \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), \(\left(\begin{smallmatrix}0&-1\\-1&0\end{smallmatrix}\right)\), and the first block again. Each has one positive and one negative coefficient; the total signature is zero. This also verifies \(\sigma(T^2\times T^2)=\sigma(T^2)^2=0\), including a product whose individual dimensions are two modulo four. ∎

**Exercise F.6 — Medium: compare the A-hat genus.** Compute its first two polynomials from (E.8), then its values on \(\mathbb {CP}^2\), \(\mathbb {CP}^4\) and \(\mathbb {CP}^2\times\mathbb {CP}^2\). Verify multiplicativity on the last example and state the integrality conclusion these examples allow.

**Solution.** The denominator after cancelling the leading term is \(1+t/24+t^2/1920+O(t^3)\). Its inverse has coefficients \(-1/24\) and \(1/576-1/1920=7/5760\). Formula (D.5) therefore gives
\[
\widehat A_1=-\frac{p_1}{24},\qquad
\widehat A_2=\frac{7(p_1^2-2p_2)}{5760}+\frac{p_2}{576}
=\frac{7p_1^2-4p_2}{5760}.
\]
The previously computed numbers give \(-1/8\) on \(\mathbb {CP}^2\), \((175-40)/5760=3/128\) on \(\mathbb {CP}^4\), and \((126-36)/5760=1/64\) on the product. The latter equals \((-1/8)^2\), as multiplicativity requires. These examples disprove integrality on all closed oriented manifolds. They do not address additional spin hypotheses or an index theorem, which have not been assumed. ∎

This closes the signature and multiplicative-sequence portion. Continue with [Odd-prime reduced powers and the Wu classes](odd-prime-reduced-powers-and-wu-classes.md) for the complete operation construction and the exact Wu polynomial and homotopy-invariance theorem.

## Sources and scope

Friedrich Hirzebruch, [*On Steenrod's Reduced Powers, the Index of Inertia, and the Todd Genus*](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063884/) (1953), Sections1 and3, introduces the multiplicative sequences and announces the signature formula. John Milnor's [*Lectures on Characteristic Classes*, with notes by James Stasheff](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf) (Spring1957), ChapterXV, Sections1–2, gives the polynomial construction and the projective-generator argument. The coefficient reciprocity and converse genus statements there are supplied above with complete proofs, including their stated coefficient generality and the extension of the converse to any commutative rational algebra. The form algebra, relative boundary duality, full product proof and formal residue substitution are proved here using the earlier course results. The AI wrote the calibration examples, exposition and solved exercises. The companion [Odd-prime reduced powers and the Wu classes](DG-CHAR-14B.html) develops the operation construction and Wu polynomial theorem. The projective-fibration and codimension-two addition formulas of its signature section are proved above; its broader almost-complex Todd-genus assertions require their additional arguments.
