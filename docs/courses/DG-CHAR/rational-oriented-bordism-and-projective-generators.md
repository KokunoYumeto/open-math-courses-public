# Rational oriented bordism and projective generators

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0.*

The Pontryagin–Thom construction has identified bordism with homotopy classes. Its rational comparison with homology now determines the rank. Independent Pontryagin-number computations then identify a projective-space basis and the entire rational oriented bordism ring. We keep the finite-stage bounds explicit and distinguish rational equality from an integral relation with a possible torsion remainder.

The exact prerequisites are [Schubert cells](schubert-cells-and-grassmannian-cohomology.md), Theorem1.1 and Section2, for characteristic disks and cellular homology; [Classifying maps](grassmannians-and-classifying-maps.md), Theorem8.3, for lifted CW covers; [The geometric Thom construction](thom-spaces-and-the-pontryagin-thom-construction.md), Theorems C.1–C.2, I.1 and K.1 and Sections D, I and J, for Thom cells, homology and the full correspondence; [Homotopy fibres](homotopy-fibres-and-the-serre-spectral-sequence.md), Section B, for relative homotopy and cell bounds; and [Rational homotopy](rational-homotopy-and-the-hurewicz-range.md), Lemma F.1, Theorem F.8 and Corollary H.5, for finite generation and the finite Thom comparison. The [Pontryagin chapter](pontryagin-classes-and-oriented-universal-cohomology.md), Theorem5.1, supplies the universal rational ring. [Characteristic numbers](characteristic-numbers-and-projective-product-independence.md), Theorem4.2 and Proposition5.1, supplies projective independence and boundary vanishing. [The oriented cobordism ring](the-oriented-cobordism-ring.md) supplies the group, product and signed-point conventions.

Sections J–L continue Sections F–I of the rational-homotopy companion. References to the geometric chapter name it explicitly, since it has its own section letters. This is the concluding rational portion of the Thom-space lesson. Six original exercises have complete solutions.

## J. Finite stages and the rational bordism rank

The geometric construction turns a based map into a closed manifold. The rational homotopy estimate turns its homotopy class into a homology class with finite error. We now put both constructions in the same finite space, keeping track of the two independent dimension bounds.

For integers \(k\geq1\) and \(p\geq0\), write
\[
B_{k,p}=\widetilde G_k(\mathbb R^{k+p}),\qquad
\xi_{k,p}=\widetilde\gamma_k|_{B_{k,p}},\qquad
T_{k,p}=T(\xi_{k,p}).
\tag{J.1}
\]
The tilde records a chosen orientation on each plane. These are the orientation double covers of the finite real Grassmannians, with their canonical oriented bundles. Their increasing unions are \(BSO(k)\), \(\widetilde\gamma_k\) and \(MSO(k)\). All Thom spaces have their collapsed point as basepoint. The finite bases are compact smooth manifolds and finite CW complexes, as proved in the geometric chapter, Lemma D.2. For \(p\geq1\) the oriented base is connected, by the explicit rotation argument in the Pontryagin chapter, Section3. When \(p=0\) it consists of the two orientations of \(\mathbb R^k\); we will not mistake those two points for a connected stage.

### J.1. The cell bound for a finite Grassmannian

**Lemma J.1 — The missing-cell bound.** For each \(k\geq1\), the inclusion \(B_{k,p}\subset BSO(k)\) is a CW-subcomplex inclusion with no relative cells below dimension \(p+1\). Its canonical Thom inclusion \(T_{k,p}\subset MSO(k)\) has no relative cells below dimension \(k+p+1\). Consequently
\[
H_i(BSO(k),B_{k,p};\mathbb Z)=0\quad(0\leq i\leq p),
\tag{J.2}
\]
and, for \(j\geq2\), the Thom inclusion induces an isomorphism on \(\pi_j\) whenever \(j<k+p\), and a surjection when \(j=k+p\).

**Proof.** The Schubert chapter, Theorem1.1, gives actual compatible characteristic disks. Its real cells are indexed by partitions \(\lambda\) with at most \(k\) rows; the cell dimension is \(|\lambda|\). The finite stage \(G_k(\mathbb R^{k+p})\) consists exactly of the cells with \(\lambda_1\leq p\). A missing cell has \(\lambda_1\geq p+1\), and hence dimension at least \(p+1\). Boundary symbols decrease coordinatewise, so those finite cells and their full attaching images form a subcomplex.

The general-cover theorem in the classifying-map chapter, Theorem8.3, gives the lifted CW structure on the orientation cover. Every characteristic disk has two lifts, each of the same dimension. Restricting the cover to the finite subcomplex gives exactly \(B_{k,p}\). Thus the same lower bound holds for the relative oriented cells. Its relative cellular chain groups through degree \(p\) are zero, proving (J.2) by the cellular/singular comparison already proved in the Schubert chapter. That comparison applies to these pairs: both chain complexes are quotients of the respective subcomplex inclusions, and the skeletal relative-disk argument is natural for them. There are finitely many cells in each dimension even in the infinite space, with two lifts per Schubert cell.

The Thom-cell theorem in the geometric chapter, Theorem C.1, shifts the dimension of every base cell by \(k\) and introduces just the common basepoint. Its characteristic maps restrict to those over the finite base. Thus a missing Thom cell has dimension at least \(k+p+1\).

The homotopy foundation companion, Section B.2, proves that a CW pair with no relative cells through dimension \(d\) has zero relative homotopy groups through \(d\), using full cellular approximation. Apply it here with \(d=k+p\). Its exact relative sequence (B.4) gives an isomorphism on \(\pi_j\) when both adjacent relative groups, in dimensions \(j+1\) and \(j\), vanish. This is \(j<k+p\). When \(j=k+p\), vanishing of the latter relative group still gives surjectivity. These are statements about the actual inclusion maps, rather than only group ranks. ∎

For homology, the pair sequence and (J.2) similarly give
\[
H_i(B_{k,p};\mathbb Z)\xrightarrow{\cong}H_i(BSO(k);\mathbb Z)
\quad (i<p),
\tag{J.3}
\]
and surjectivity when \(i=p\). In degree zero with \(p\geq1\), the same pair sequence applies and the spaces are connected. Thus it also gives the asserted degree-zero isomorphism. The stronger choice \(p\geq n+1\) will make both (J.3) in degree \(n\) and the Thom homotopy comparison in degree \(n+k\) isomorphisms. The weaker \(p=n\) gives only the surjections established by these cell bounds.

### J.2. The finite Pontryagin–Thom isomorphism

Denote transverse inverse image for the finite canonical bundle by
\[
\tau_{k,p}:\pi_{n+k}(T_{k,p})\longrightarrow\Omega_n.
\tag{J.4}
\]
Here \(\Omega_n\) is the group of smooth closed oriented \(n\)-manifolds under disjoint union modulo smooth oriented bordism. The geometric chapter, Theorem G.3, proves that this is a homomorphism with the tangent-first normal convention. Its Theorem K.1 proves the universal isomorphism
\(\tau_{k,\infty}:\pi_{n+k}(MSO(k))\to\Omega_n\) for \(k>n+1\), including the collapse inverse and relative embeddings.

**Theorem J.2 — A finite target that computes bordism.** If
\[
n\geq0,\qquad k>n+1,\qquad p\geq n+1,
\tag{J.5}
\]
then (J.4) is an isomorphism.

**Proof.** Put \(j=n+k\). The bound on \(p\) gives \(j<k+p\), so Lemma J.1 makes
\[
\pi_{n+k}(T_{k,p})\longrightarrow\pi_{n+k}(MSO(k))
\tag{J.6}
\]
an isomorphism. The bound on \(k\) makes the universal map \(\tau_{k,\infty}\) an isomorphism by the full geometric theorem. Their composite is exactly \(\tau_{k,p}\). Indeed a map in the finite stage has the same zero-section inverse image after inclusion in the universal space; the canonical bundle inclusion is the identity on its normal quotient and retains its orientation. The common-finite-carrier argument in geometric Section I proves that these constructions agree on homotopy classes. Thus (J.4) is the composite of two isomorphisms. ∎

This proof does not replace the finite stage by an unspecified limit. It shows that the explicit stage in (J.5) already has all the homotopy information needed in the degree under discussion. In particular the finite Thom homotopy group is finitely generated: it is simply connected for \(k\geq2\), is a finite CW complex, and the rational companion's Theorem F.8 proves finite generation of its homotopy groups. Hence \(\Omega_n\) is finitely generated under (J.5), before computing its rank.

### J.3. Stabilization is the identity on bordism

Adding a fixed last positive vector gives a base map
\(B_{k,p}\to B_{k+1,p}\) whose pulled-back bundle is \(\xi_{k,p}\oplus\varepsilon^1\), oriented in that order. The geometric chapter, Section D, proves the homeomorphism \(T(\xi\oplus\varepsilon^1)=\Sigma T(\xi)\) and the induced Thom map. Suspending based sphere maps therefore gives
\[
s_{k,p}:\pi_{n+k}(T_{k,p})\longrightarrow
\pi_{n+k+1}(T_{k+1,p}).
\tag{J.7}
\]

**Proposition J.3 — Stable finite-stage comparison.** Under (J.5),
\[
\tau_{k+1,p}s_{k,p}=\tau_{k,p},
\tag{J.8}
\]
and \(s_{k,p}\) is an isomorphism. Increasing \(p\), while retaining \(p\geq n+1\), also induces an isomorphism in degree \(n+k\) commuting with the bordism identifications.

**Proof.** Choose a transverse representative \(f:S^{n+k}\to T_{k,p}\). View \(S^{n+k}\wedge S^1\) as the one-point compactification of \(\mathbb R^{n+k}\times\mathbb R\), with the last coordinate positive. Near the zero inverse image of the suspended map, use the product-disk model of the Thom homeomorphism. Its total-vector form is
\[
(x,t)\longmapsto (f_E(x),t),
\tag{J.9}
\]
where \(f_E\) is the smooth noncollapsed total-vector representative of \(f\). Choose the product-disk to round-disk homeomorphism to be the identity near zero, as detailed below. The inverse image is exactly \(M\times\{0\}\), with \(M=f^{-1}(B_{k,p})\), since its normal components vanish precisely when those of \(f\) and the last coordinate vanish. The derivative is transverse near this inverse image, with old normal quotient followed by the positive last line.

The source orientation is old ambient orientation followed by that line. The target bundle orientation is old normal orientation followed by the same line. Cancelling the last positive line from the tangent-first rule leaves exactly the old orientation on \(M\). For a representative smooth throughout its noncollapsed region, first use geometric Lemma J.2 to put \(f\) in its exact normal germ. The suspended map then agrees near \(M\times\{0\}\) with the smooth collapse for its normal injection \(\alpha\oplus\operatorname{id}_{\mathbb R}\). Geometric Section I constructs that collapse in this finite target. Both maps have precisely this zero set and agree on a neighbourhood, so geometric Lemma J.1 makes them based homotopic. This avoids requiring the disk homeomorphism to be smooth far from zero. The collapse has the oriented inverse image \([M]\), proving (J.8). Values at the smash basepoint lie at the collapsed point and cannot add zero inverse images. This comparison takes place entirely in the finite canonical stages.

Both inverse-image maps in (J.8) are isomorphisms by Theorem J.2, so \(s_{k,p}\) is their composite inverse followed by the other map and is an isomorphism. For \(p\)-increase, the finite-stage inclusion also retains the zero inverse image and its normal orientation. Theorem J.2 gives the same argument. ∎

Here is the promised disk comparison. In a unit direction \(u=(v,t)\), the product disk has radial boundary \(R(u)=1/\max\{\|v\|,|t|\}\), with \(1\leq R(u)\leq\sqrt2\). Send a radius \(r\leq1/2\) to itself, and a radius \(1/2\leq r\leq R(u)\) to \(1/2+(r-1/2)/(2R(u)-1)\). These strictly increasing functions are continuous in the direction, join at the inner radius and end at one. Their inverses are continuous as well. Thus the map is a fibrewise homeomorphism, identity on the smaller round disk and carrying product boundary to round boundary. It leaves (J.9) literally unchanged near zero. The same quotient-product proofs used for geometric (D.2) show that it induces the stated Thom/smash homeomorphism.

### J.4. The comparison with universal homology

**Theorem J.4 — Bordism and normal universal homology with finite error.** Let
\[
n\geq0,\qquad k>\max\{2,n+1\},\qquad p\geq n+1.
\tag{J.10}
\]
There is a homomorphism
\[
\Theta_{k,p}:\Omega_n
\xrightarrow{\ \tau_{k,p}^{-1}\ }\pi_{n+k}(T_{k,p})
\xrightarrow{\ h\ }H_{n+k}(T_{k,p};\mathbb Z)
\xrightarrow{\ \operatorname{Th}^{-1}\ }H_n(B_{k,p};\mathbb Z)
\xrightarrow{\ j_*\ }H_n(BSO(k);\mathbb Z)
\tag{J.11}
\]
with finite kernel and finite cokernel. Its rationalization is an isomorphism. Both its source and target are finitely generated abelian groups.

**Proof.** The first arrow is an isomorphism by Theorem J.2. The two middle arrows have finite kernel and cokernel by the rational companion's Corollary H.5: \(B_{k,p}\) is finite, \(\xi_{k,p}\) is oriented of rank \(k>2\), and \(n<k-1\). Its Thom isomorphism uses the positive bundle orientation already fixed. The last arrow is an integral isomorphism by (J.3) and \(p\geq n+1\). Thus composing the end isomorphisms with the middle finite-error map gives the asserted finite kernel and cokernel, and tensor exactness gives the rational isomorphism.

The finite base has finitely generated homology. The finite Thom complex has finitely generated homotopy in this degree by Theorem F.8, so Theorem J.2 gives finite generation of \(\Omega_n\). Finally (J.3) identifies universal homology in degree \(n\) with finite-base homology. This proves the finite-generation assertions without inferring them from rational ranks alone. ∎

The geometric definition classifies a **normal** bundle. Pontryagin numbers below use the **tangent** bundle. We do not identify these two bundles or equate their Pontryagin classes. The role of (J.11) is to compute the rational dimension; the separately proved tangent Pontryagin numbers will supply independent linear functionals on that dimension.

**Normal and tangent number coordinates.** For a smooth closed oriented manifold of dimension \(4r\), the vectors of stable normal and tangent Pontryagin numbers are related by an invertible integer matrix depending only on \(r\). The same matrix gives the inverse conversion. Consequently one vector vanishes exactly when the other does. For \(r=0\), both vectors have the single empty-product coordinate, the signed count of points.

**Proof.** An embedding gives a normal bundle \(\nu\) with \(TM\oplus\nu\) trivial. Stabilizing the embedding changes neither bundle's Pontryagin classes. The rational Whitney formula in the Pontryagin chapter gives
\[
p(TM)p(\nu)=1\quad\text{in }H^*(M;\mathbb Q).
\tag{J.11a}
\]
We use rational classes here because the integral Whitney formula can have a two-torsion error.

To compute the inverse universally, assign weight \(i\) to the variable \(P_i\) in \(\mathbb Z[P_1,P_2,\ldots]\). Put \(Q_0=1\) and recursively define
\[
Q_j=-\sum_{i=1}^{j}P_iQ_{j-i}\quad(j\geq1).
\tag{J.11b}
\]
The coefficient of \(t^j\) in
\((1+\sum_{i\geq1}P_it^i)(1+\sum_{i\geq1}Q_it^i)\)
is zero for every \(j>0\). Thus the second series is the formal inverse of the first. Every \(Q_j\) is an integer polynomial of weight \(j\), and substitution \(P_j\mapsto Q_j\) defines a weight-preserving ring homomorphism \(\sigma\). Applying it twice inverts a series twice. Uniqueness of the recursively determined inverse implies \(\sigma^2=\operatorname{id}\).

The monomials \(P_I\), indexed by partitions \(I\vdash r\), form a finite integer basis of the weight-\(r\) part. Write \(\sigma(P_I)=\sum_{J\vdash r}a_{IJ}P_J\). The matrix \(A_r=(a_{IJ})\) is integral and \(A_r^2=I\), so its determinant is \(\pm1\). Substituting \(P_j=p_j(TM)\) in (J.11b) and using (J.11a) gives \(p_j(\nu)=Q_j(p(TM))\) rationally. Evaluation on \([M]\) therefore gives the normal number vector as \(A_r\) times the tangent vector. Both sides are integers; equality after their inclusion in \(\mathbb Q\) is equality in \(\mathbb Z\). This proves the integer conversion even though (J.11a) was used only rationally. Applying \(A_r\) again proves the inverse conversion and the vanishing equivalence. In weight zero \(\sigma(1)=1\), giving the stated signed-count coordinate. ∎

For example \(Q_1=-P_1\) and \(Q_2=P_1^2-P_2\). In dimension eight, if \(u=\langle p_1(TM)^2,[M]\rangle\) and \(v=\langle p_2(TM),[M]\rangle\), the corresponding normal vector is \((u,u-v)\). The projective computations in the characteristic-number chapter give tangent vectors \((25,10)\) and \((18,9)\) for \(\mathbb {CP}^4\) and \(\mathbb {CP}^2\times\mathbb {CP}^2\); their normal vectors are \((25,15)\) and \((18,9)\). The normal matrix has determinant \(-45\), so either convention proves independence. These number coordinates are distinct from the coefficients in a chosen projective-product basis; the latter require the matrix inversion in Section K.4.

### J.5. Thom's finite generation and rank theorem

Let \(\mathfrak p(r)\) be the number of partitions of the nonnegative integer \(r\), with \(\mathfrak p(0)=1\). For example \(\mathfrak p(1)=1\), \(\mathfrak p(2)=2\), and \(\mathfrak p(3)=3\).

**Theorem J.5 — Rational rank of oriented bordism (MS18.8).** For every \(n\geq0\), \(\Omega_n\) is a finitely generated abelian group. Its rank is
\[
\operatorname{rank}\Omega_n=
\begin{cases}
\mathfrak p(r),&n=4r,\\
0,&4\nmid n.
\end{cases}
\tag{J.12}
\]
In particular \(\Omega_n\) is finite when \(4\nmid n\).

**Proof.** Choose \(k,p\) satisfying (J.10). Theorem J.4 has already proved finite generation and identifies the rank with \(\dim_{\mathbb Q}H_n(BSO(k);\mathbb Q)\).

The Pontryagin chapter's full universal-ring proof, Theorem5.1 with coefficients \(\mathbb Q\), gives
\[
H^*(BSO(2m+1);\mathbb Q)=\mathbb Q[p_1,\ldots,p_m],
\tag{J.13}
\]
and
\[
H^*(BSO(2m);\mathbb Q)=\mathbb Q[p_1,\ldots,p_{m-1},e],
\qquad |p_i|=4i,\quad |e|=2m.
\tag{J.14}
\]
In (J.14), \(p_m=e^2\). Since \(k>n+1\), the Euler generator, when present, has degree \(k>n\) and contributes no monomial to degree \(n\). Every \(p_i\) that can occur in that degree has \(4i\leq n<k\), and is among the displayed polynomial generators. Thus degree \(n\) is zero unless \(n=4r\); in degree \(4r\) its monomial basis is
\[
\{p_{i_1}\cdots p_{i_q}: (i_1,\ldots,i_q)\vdash r\}.
\tag{J.15}
\]
The empty monomial is included for \(r=0\).

The proved rational coefficient theorem gives \(H^n(BSO(k);\mathbb Q)=\operatorname{Hom}_{\mathbb Q}(H_n(BSO(k);\mathbb Q),\mathbb Q)\). The latter homology is finite dimensional by (J.3), so its dimension equals that of its dual. The basis count in (J.15) and Theorem J.4 give (J.12). A finitely generated abelian group of rational rank zero is finite by the explicit decomposition in rational Lemma F.1. This proves the final assertion. ∎

The proof controls all finite errors without computing their orders. In particular it does not give the complete integral torsion of \(\Omega_n\), nor assert that every integral number vector is realizable. Its rank conclusion is exact because the finite-stage Pontryagin–Thom and rational Hurewicz comparisons are actual isomorphisms in the needed senses.

## K. Projective generators and the torsion criterion

For a partition \(I=(i_1,\ldots,i_q)\) of \(r\), put
\[
P_I=\mathbb {CP}^{2i_1}\times\cdots\times\mathbb {CP}^{2i_q},
\tag{K.1}
\]
with each factor's complex orientation and the ordered product orientation. Its real dimension is \(4r\). Permuting the factors preserves that orientation because their real dimensions are even. The empty product \(P_{\varnothing}\) is the positive point, the multiplicative unit in \(\Omega_0\).

The characteristic-number chapter, Theorem4.2, proves that the square matrix
\[
\mathcal P_r=(p_J[P_I])_{J,I\vdash r}
\tag{K.2}
\]
is nonsingular over \(\mathbb Q\). Its complete proof changes integrally from elementary Pontryagin monomials to monomial symmetric classes \(s_J(p)\). The product formula has coefficient one for each distinct split of a partition; a nonzero entry requires refinement. In a partition ordering by length the resulting matrix is triangular, and its diagonal entries are products of the nonzero numbers
\(s_j(p)[\mathbb {CP}^{2j}]=2j+1\). The integral change of basis is invertible, so (K.2) is nonsingular too. This recalls the actual mechanism in the earlier proof; no independence of bordism generators is assumed here.

### K.1. The rational polynomial ring

**Theorem K.1 — Rational oriented bordism (MS18.9).** The graded map
\[
\Phi:\mathbb Q[z_1,z_2,z_3,\ldots]\longrightarrow
\Omega_*\otimes\mathbb Q,
\qquad |z_i|=4i,\quad z_i\longmapsto[\mathbb {CP}^{2i}]\otimes1,
\tag{K.3}
\]
is an isomorphism of graded algebras. In degree \(4r\), the classes \([P_I]\otimes1\), \(I\vdash r\), are a basis. The other positive degrees are zero.

**Proof.** The earlier cobordism-ring chapter proves that products and sums are well defined, that the signed point is the unit, and that the product has sign \((-1)^{mn}\) under exchange of degree-\(m\) and degree-\(n\) factors. The degrees \(4i\) are even, so these chosen classes commute and define (K.3) on every polynomial, whose monomials and sums are finite.

Pontryagin numbers are additive and vanish on boundaries by the full proof in characteristic-number Proposition5.1. They therefore define integer homomorphisms \(\Omega_{4r}\to\mathbb Z\), and rational linear functionals after tensoring. If
\[
\sum_{I\vdash r}a_I([P_I]\otimes1)=0,
\tag{K.4}
\]
apply all of them. The coefficient vector then satisfies \(\mathcal P_r a=0\). Nonsingularity of (K.2) forces every \(a_I=0\). The \(\mathfrak p(r)\) projective products are independent. Theorem J.5 says the whole degree has dimension \(\mathfrak p(r)\), so these products also span.

For degree zero the empty product represents the positive point and \(\Omega_0=\mathbb Z\), as proved by the signed interval-boundary calculation in the cobordism chapter. Thus (K.3) is an isomorphism in degree zero too. In degrees not divisible by four the polynomial algebra is zero and Theorem J.5 makes the rational target zero. The map is therefore an isomorphism in every degree. An element of a graded polynomial algebra, and of the direct-sum graded bordism group, has only finitely many homogeneous components, so the degreewise conclusion proves both global injectivity and surjectivity. ∎

**Corollary K.2 — Complete rational detection by tangent numbers.** For \(r\geq1\), the map
\[
\mathcal N_r:\Omega_{4r}\otimes\mathbb Q\longrightarrow
\mathbb Q^{\mathfrak p(r)},\qquad
[M]\otimes1\longmapsto (p_I[M])_{I\vdash r},
\tag{K.5}
\]
is an isomorphism. For \(r=0\), use the empty characteristic product \(1\); its number is the signed number of points, and the analogous map is an isomorphism to \(\mathbb Q\).

**Proof.** Theorem K.1 gives the projective basis. On that basis the map has exactly the nonsingular matrix (K.2). Its inverse matrix over \(\mathbb Q\) supplies an inverse linear map. In degree zero its matrix is the one-by-one matrix \((1)\). ∎

The integer image of the number map can be a proper lattice. Corollary K.2 makes no claim that every integer vector in its target arises from a manifold, nor that an integral bordism class with zero numbers must be zero.

### K.2. When a positive multiple bounds

We first spell out the exact algebraic meaning of a rationally zero class. The fraction description in rational Section F.1 shows, for any abelian group \(A\),
\[
a\otimes1=0\text{ in }A\otimes\mathbb Q
\quad\Longleftrightarrow\quad
Na=0\text{ in }A\text{ for some integer }N>0.
\tag{K.6}
\]
Indeed the left side says that the fraction \(a/1\) equals the zero fraction. The common-denominator equivalence means exactly that a nonzero positive integer kills the numerator. Conversely such an integer can be inverted over \(\mathbb Q\), giving zero. This does not require finite generation.

**Theorem K.3 — Positive-multiple bounding criterion (MS18.10).** Let \(M\) be a smooth closed oriented \(n\)-manifold, possibly disconnected, with \(n\geq0\). A disjoint union of some positive number of copies of \(M\) is an oriented boundary if and only if all its top-degree Pontryagin numbers vanish. When \(4\nmid n\) there are no such positive-degree numbers, and the condition is automatic. In dimension zero, “all” includes the empty-product number, the signed count of points.

**Proof: necessity.** For \(n=4r>0\), if \(N[M]=0\) in \(\Omega_n\), the additivity and boundary theorem give
\[
N p_I[M]=p_I[\underbrace{M\sqcup\cdots\sqcup M}_{N\text{ copies}}]=0.
\tag{K.7}
\]
These are integers, so every \(p_I[M]\) is zero. For \(n=0\) the identical argument applies to the signed count, which is the proved identification \(\Omega_0=\mathbb Z\). The degrees not divisible by four have no top-degree Pontryagin monomials, so necessity is vacuous there.

**Proof: sufficiency.** If \(n=4r\), Corollary K.2 makes zero numbers equivalent to \([M]\otimes1=0\). Formula (K.6) then gives \(N[M]=0\) for some \(N>0\). By the definition of oriented bordism, this says exactly that the disjoint union of those \(N\) copies, with their given orientations, is the outward-oriented boundary of a compact oriented \((n+1)\)-manifold. The dimension-zero argument is included through the empty-product coordinate. If \(4\nmid n\), Theorem J.5 says \(\Omega_n\) is finite; the order of \([M]\), or one if it is zero, gives the same conclusion. ∎

This criterion detects torsion, rather than the precise integral zero class. Determining when \(M\) itself bounds needs further information about integral torsion. We have not asserted an order or structure for that torsion.

### K.3. An integral relation after a positive multiplier

**Corollary K.4 — Projective products after a multiplier.** For every smooth closed oriented \(n\)-manifold \(M\), there is an integer \(N>0\) and an integral linear combination of the projective products (K.1) of dimension \(n\) such that
\[
N[M]=\sum_{I\vdash r}b_I[P_I]\quad\text{in }\Omega_{4r}
\quad\text{if }n=4r.
\tag{K.8}
\]
When \(4\nmid n\), the corresponding assertion is \(N[M]=0\). Negative coefficients mean copies with reversed orientation; a zero coefficient contributes no copy. For \(n=0\), the right side uses the signed point.

**Proof.** For \(n=4r\), expand \([M]\otimes1\) in Theorem K.1's basis, say with coefficients \(a_I\in\mathbb Q\). Choose a positive common denominator \(D\), so \(D a_I\) are integers. Then
\[
u=D[M]-\sum_{I\vdash r}(D a_I)[P_I]
\tag{K.9}
\]
is an integral bordism class with \(u\otimes1=0\). By (K.6), a positive integer \(t\) kills \(u\). Multiply (K.9) by \(t\), putting \(N=tD\) and \(b_I=tD a_I\), to get (K.8). This extra torsion multiplier is necessary for the stated proof: clearing denominators alone establishes only a relation modulo torsion. For dimensions not divisible by four use Theorem J.5's finite group. Degree zero could also be handled directly by its signed-count isomorphism. ∎

Because an integral combination is represented by an actual disjoint union with orientation reversals, (K.8) is an actual smooth oriented cobordism statement. It is not merely equality of characteristic-number vectors. This proves the assigned projective-combination consequence as well as the source's distinct positive-multiple bounding criterion.

### K.4. Explicit coefficients in dimensions four and eight

In real dimension four the sole projective generator is \(\mathbb {CP}^2\), whose number is \(p_1=3\). Thus
\[
[M^4]\otimes1=\frac{p_1[M]}3[\mathbb {CP}^2]\otimes1.
\tag{K.10}
\]
Reversing orientation negates both sides' coordinates. This is a rational bordism computation. Divisibility of \(p_1[M]\) by three will follow from the signature theorem; it is not needed or inferred here.

In real dimension eight use the ordered basis \(\mathbb {CP}^4\), \(\mathbb {CP}^2\times\mathbb {CP}^2\). The earlier characteristic-number chapter computed the exact matrix
\[
\begin{pmatrix}25&18\\10&9\end{pmatrix},\qquad \det=45,
\tag{K.11}
\]
with rows \(p_1^2,p_2\). Writing \(u=p_1^2[M]\), \(v=p_2[M]\), solve this matrix equation to obtain
\[
[M]\otimes1=
\frac{u-2v}{5}[\mathbb {CP}^4]\otimes1
+\frac{5v-2u}{9}[\mathbb {CP}^2\times\mathbb {CP}^2]\otimes1.
\tag{K.12}
\]
For a single \(\mathbb {CP}^4\), its vector \((25,10)\) gives coefficients \((1,0)\); for the product, \((18,9)\) gives \((0,1)\). Multiplying by45 clears both denominators:
\[
45[M]-9(u-2v)[\mathbb {CP}^4]
-5(5v-2u)[\mathbb {CP}^2\times\mathbb {CP}^2]
\tag{K.13}
\]
is a torsion class. A further positive multiplier kills it, yielding an integral relation of the kind (K.8). Claiming that (K.13) itself is zero would discard the integral error that the argument has explicitly retained.

In dimensions one, two and three the rational group is zero. This conclusion alone gives no integral group orders and does not determine whether any particular integral group is zero.

## L. Exercises with complete solutions

**Exercise L.1 — Easy: choose a sufficient finite stage.** Use the proved bounds to choose the smallest allowed \(k,p\) in Theorem J.4 for \(n=8\). Identify its Thom homotopy degree and check the strict Hurewicz inequality. Explain precisely what the same cell bounds give if \(p=8\). Also choose a sufficient stage for \(n=0\).

**Solution.** The conditions are \(k>\max\{2,9\}\) and \(p\geq9\), so the smallest allowed integers are \(k=10,p=9\). The finite group is
\[
\pi_{18}(T_{10,9})\cong\Omega_8.
\]
The Hurewicz bound is \(18<2\cdot10-1=19\), exactly the required strict inequality. The first omitted Thom cell has dimension \(k+p+1=20\), so the relative groups in dimensions18 and19 vanish. The first omitted base cell has dimension10, so relative homology in degrees8 and9 vanishes. These give both isomorphisms used in Theorem J.4.

For \(p=8\), the first omitted Thom cell has dimension19, so the argument vanishes only through relative dimension18. Its exact sequence proves surjectivity on \(\pi_{18}\), without proving injectivity because relative \(\pi_{19}\) has not been controlled. The first omitted base cell has dimension9, likewise proving surjectivity on \(H_8\) without the degree-nine vanishing that would give injectivity. This does not assert either map actually fails to be injective; it states the limit of these particular bounds.

For \(n=0\), choose \(k=3,p=1\). Its degree is3, and \(3<5\) is the Hurewicz inequality. The finite oriented base is connected, whereas \(p=0\) would give the two oriented full planes. Its \(H_0=\mathbb Z\) and the comparison agree with the signed-point identification \(\Omega_0=\mathbb Z\). ∎

**Exercise L.2 — Easy: partitions and ranks.** Compute the rational ranks in real dimensions12,18 and20. Give bases in the nonzero degrees and state the integral conclusions actually obtained in dimension18.

**Solution.** The partitions of3 are \((3),(2,1),(1,1,1)\). Hence the degree-twelve rational group has basis
\[
[\mathbb {CP}^6],\quad[\mathbb {CP}^4\times\mathbb {CP}^2],
\quad[(\mathbb {CP}^2)^3],
\]
where each class in this display is rationalized. Its rank is3. Dimension18 is not divisible by four; its rank is zero, and Theorem J.5 gives a finite integral group. It does not specify its order, exponent or whether it is zero.

The partitions of5 are
\[
(5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1).
\]
Thus the rank in dimension20 is7, and the corresponding basis consists of
\(\mathbb {CP}^{10}\), \(\mathbb {CP}^{8}\times\mathbb {CP}^{2}\), \(\mathbb {CP}^{6}\times\mathbb {CP}^{4}\), \(\mathbb {CP}^{6}\times(\mathbb {CP}^{2})^2\), \((\mathbb {CP}^{4})^2\times\mathbb {CP}^{2}\), \(\mathbb {CP}^{4}\times(\mathbb {CP}^{2})^3\), and \((\mathbb {CP}^{2})^5\). The finite partition list includes every possibility: distinguish the largest part5,4,3,2 or1, and partition the remaining weight into parts no larger than it. ∎

**Exercise L.3 — Medium: invert the dimension-eight number matrix.** Derive (K.12). Check it on the oriented disjoint union of two copies of \(\mathbb {CP}^4\) and one orientation-reversed copy of \(\mathbb {CP}^2\times\mathbb {CP}^2\). For an arbitrary eight-manifold, identify the precise residual class after multiplying its rational formula by45.

**Solution.** If the two rational coefficients are \(A,B\), the two numbers give
\[
25A+18B=u,\qquad10A+9B=v.
\]
Subtracting twice the second equation from the first gives \(5A=u-2v\). Taking five times the second minus twice the first gives \(9B=5v-2u\). The determinant45 is nonzero, so these are the unique solution (K.12).

The specified disjoint union has \(u=50-18=32\) and \(v=20-9=11\), because orientation reversal negates both evaluations. The two formulas return \(A=2\) and \(B=-1\), as its actual integral construction requires.

For a general \(M\), the residual class is exactly (K.13). Its rationalization is zero, so (K.6) makes it torsion. Its numbers are zero as well, by the two displayed equations. Neither observation gives its integral order or establishes that it is already zero. Multiplying it by its positive order gives the integral bordism relation. ∎

**Exercise L.4 — Medium: the zero-dimensional exception to a careless criterion.** Explain why omitting the empty-product number would make Theorem K.3 false in dimension zero. Determine when a signed finite set has a positive multiple that bounds, and construct its bordism in the bounding case.

**Solution.** A positive point has no positive-degree Pontryagin numbers, but its class is1 in \(\Omega_0=\mathbb Z\), so no positive multiple is zero. The missing coordinate is \(\langle1,[M]\rangle\), the signed count.

If \(M\) has \(a\) positive and \(b\) negative points, a positive multiple bounds exactly when \(N(a-b)=0\) for some \(N>0\), hence exactly when \(a=b\). In that case pair each positive point with one negative point. Give each interval the increasing-coordinate orientation, whose outward boundary is its positive terminal point and negative initial point, and identify these endpoints with the pair. The disjoint union of these intervals is already an oriented bordism with boundary \(M\). Thus \(N=1\) suffices in this dimension when the complete number coordinate vanishes. ∎

**Exercise L.5 — Medium: Euler data and Pontryagin torsion detection.** Show that \(S^4\times\mathbb {CP}^2\) has zero Pontryagin numbers, while its Euler number is6. Give a direct oriented bounding manifold. Explain why this example is compatible with Theorem K.3.

**Solution.** The stable triviality \(TS^4\oplus\varepsilon^1=\varepsilon^5\) gives \(p(TS^4)=1\). If \(x\) is the positive degree-two generator on \(\mathbb {CP}^2\), its Pontryagin class is \(1+3x^2\), with \(x^3=0\). The product formula on these torsion-free cohomology groups therefore gives \(p_1=3x^2\) and \(p_2=0\). Its \(p_1^2\) is zero since \(x^4=0\). Thus both top-degree numbers vanish.

The earlier Euler-evaluation and cohomological product proofs give Euler characteristic \(\chi(S^4)\chi(\mathbb {CP}^2)=2\cdot3=6\), equal to its Euler number. It is the actual oriented boundary of \(D^5\times\mathbb {CP}^2\), with its disk-first product orientation. Along the boundary, the disk's outward normal followed by \(TS^4\) and then the projective tangent orientation gives the ambient product orientation, so the induced boundary is the desired product orientation. There is just the disk boundary, and no additional corner.

Theorem K.3 concerns stable Pontryagin numbers, which vanish on boundaries. The Euler class is not stable under adjoining the boundary normal line. Its nonzero evaluation therefore supplies no contradiction. This example has an explicit integral bounding manifold, a stronger conclusion than the rational criterion alone provides. ∎

**Exercise L.6 — Hard: recover the rank from the source's surjectivity route.** Using only finite-target surjectivity in geometric Theorem I.1, the finite Thom comparison of rational Corollary H.5, finite-stage homology stabilization, and projective-product independence, prove Theorem J.5. Then justify the rational polynomial algebra conclusion. Explain where the full finite Pontryagin–Thom isomorphism improves this route.

**Solution.** Choose \(k>\max\{2,n+1\}\) and \(p\geq n+1\). Geometric I.1 gives a surjection
\(\pi_{n+k}(T_{k,p})\to\Omega_n\), since its weaker conditions \(k>n,p\geq n\) are satisfied. The domain is finitely generated by its finite simply connected CW structure and Theorem F.8, so its quotient \(\Omega_n\) is finitely generated. The finite Thom comparison makes the domain's rational rank equal to that of \(H_n(B_{k,p};\mathbb Z)\). By (J.3) and the universal rational ring, this rank is \(\mathfrak p(r)\) for \(n=4r\), and zero otherwise. Exactness of rational tensoring preserves the surjection, giving this as an upper bound for the rank of \(\Omega_n\).

For \(n=4r\), a rational relation among the \(\mathfrak p(r)\) projective products would give a zero linear combination of their Pontryagin-number columns. The independently proved nonsingularity of (K.2) makes every coefficient zero. Thus those products give the matching lower bound. In degree zero use the positive point and its nonzero signed count. This proves the rank equality. In other degrees finite generation and rank zero imply finiteness, proving all of Theorem J.5.

The matching dimension and independence make the projective products a basis in every degree divisible by four. Ordinary polynomial monomials in the classes of \(\mathbb {CP}^{2i}\) are exactly those products. Their multiplication agrees with the bordism product, whose even-dimensional generators commute. The other rational degrees vanish, and the point gives the unit. This proves the graded polynomial isomorphism, rather than only an additive basis assertion.

The full finite isomorphism of Theorem J.2 gives equality of rational dimensions already from its homotopy/homology comparison. The surjectivity route needed projective independence to obtain that equality. Both routes still need projective independence to identify these particular polynomial generators and to prove complete rational detection by tangent Pontryagin numbers. Neither route determines the remaining integral torsion. ∎

## Sources and scope

René Thom's [*Quelques propriétés globales des variétés différentiables*](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/thomcob.pdf) (1954) gives the original bordism classification, rational polynomial ring and positive-multiple consequences. Its use of normal characteristic numbers is compatible with the tangent convention by the proved conversion above.

Dan Freed's [*Bordism: Old and New*, Lecture12](https://people.math.harvard.edu/~dafr/M392C-2012/Notes/lecture12.pdf) (2012) develops the rational bordism calculation and the projective-space generators. Haynes Miller's [*Algebraic Topology II*, Lecture40](https://ocw.mit.edu/courses/18-906-algebraic-topology-ii-spring-2020/e8a061a73ca1a451df8809c7a7fbc846_MIT18_906S20_notes.pdf) (2020) describes the normal characteristic-number map and the positive-multiple bounding consequence. The finite-stage comparison here supplies explicit dimension bounds; the full symmetric-polynomial proof in the characteristic-number chapter supplies independence in every degree. The normal-to-tangent conversion above explains the two number conventions. Exercise L.6 gives a second rank proof using finite-target surjectivity and independence. The teaching, proofs, computations and exercises here are independently written.

The exact own proofs used are the Schubert characteristic disks and cellular/singular comparison, general-cover theorem, geometric Thom cells and full Pontryagin–Thom construction, rational finite Thom comparison, universal oriented cohomology ring, and nonsingular projective number matrices. Their stated coefficient and connectivity hypotheses have been retained. This completes the rational bordism portion of the Thom-space lesson. Integral torsion structure, the signature theorem, combinatorial Pontryagin invariance, exotic spheres and Chern–Weil theory belong to later developments.
