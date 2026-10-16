# Schubert cells and universal Grassmannian cohomology

*Written and self-checked by GPT-6 Astra (OpenAI), at Ultra, October 2026. New exposition: CC0 1.0.*

We construct real and complex Grassmannians from explicit cells, then derive their additive homology and the corresponding cohomology bounds. We also prove the separation and paracompactness facts needed when these spaces are used as bundle bases. All infinite spaces below carry the final topology of their finite-dimensional stages.

Read [DG-CHAR-03 A.1](DG-CHAR-03.md#proposition-a-1) for the projection model of a Grassmannian, [DG-CHAR-03 B.1](DG-CHAR-03.md#lemma-b-1) for products of compact exhaustions, [DG-CHAR-03 E.1](DG-CHAR-03.md#lemma-e-1) for compact subsets of CW complexes, and [DG-CHAR-03 E.2](DG-CHAR-03.md#lemma-e-2) for quotient maps times an interval. The chain proofs used below are [DG-CHAR-06 K.1](DG-CHAR-06.md#lemma-k-1), [DG-CHAR-06 E.1](DG-CHAR-06.md#lemma-e-1), [DG-CHAR-06 E.2](DG-CHAR-06.md#theorem-e-2) and [DG-CHAR-06 E.5](DG-CHAR-06.md#lemma-e-5): homotopy, exact sequences, excision and sphere groups. The coefficient theorem is [DG-CHAR-06 U.3](DG-CHAR-06.md#theorem-u-3).

## A. Explicit Schubert disks

Write \(\mathbb F=\mathbb R\) or \(\mathbb C\), and put \(c=\dim_{\mathbb R}\mathbb F\), so \(c=1\) or \(2\). In \(\mathbb F^m\) let \(F_k=\operatorname{span}(e_1,\ldots,e_k)\). For a rank-\(r\) plane \(V\), the integer \(\dim(V\cap F_k)\) increases by zero or one at each step. Indeed, the \(k\)-th coordinate induces an injection of \((V\cap F_k)/(V\cap F_{k-1})\) into \(\mathbb F\). Its \(r\) increases occur at a unique symbol
\[
 \sigma=(\sigma_1<\cdots<\sigma_r),\qquad
 1\leq\sigma_1,\quad \sigma_r\leq m.
\tag{A1}
\]
Let \(e(\sigma)\) be the set of planes with that symbol, and put \(d(\sigma)=\sum_{j=1}^r(\sigma_j-j)\). When \(r=0\), the empty symbol describes the single point \(G_0(\mathbb F^m)\).

**Lemma A.1 (a continuous rotation).** If \(e,u\) are unit vectors and \(e^*u=u^*e=s\in[0,1]\), set
\[
 K=ue^*-eu^*,\qquad
 R_e(u)=I+K+\frac{K^2}{1+s}.
\tag{A2}
\]
This is orthogonal over \(\mathbb R\), unitary over \(\mathbb C\), maps \(e\) to \(u\), and fixes the orthogonal complement of their span. It depends continuously on \(u\), including at \(u=e\).

**Proof.** If \(q=(1-s^2)^{1/2}>0\), put \(w=(u-se)/q\). The vectors \(e,w\) are orthonormal. On their span, in this order, direct application to the two basis vectors gives
\[
 K=\begin{pmatrix}0&-q\\q&0\end{pmatrix},
 \qquad
 R_e(u)=\begin{pmatrix}s&-q\\q&s\end{pmatrix}.
\tag{A3}
\]
Here \(1-q^2/(1+s)=s\). The columns of the second matrix are orthonormal and its first column represents \(se+qw=u\). The entries are real, so the same computation is valid with conjugate transpose in the complex case. On the orthogonal complement \(K\) is zero and \(R_e(u)\) is the identity.

If \(q=0\), then \(s=1\), and \(\|u-e\|^2=2-2s=0\), so \(u=e\) and (A2) is the identity. Formula (A2), whose denominator is at least one, proves continuity without choosing \(w\) near this case. Square roots are continuous on the nonnegative reals: for \(a,b\geq0\), the identity for their difference gives \(|\sqrt a-\sqrt b|\leq\sqrt{|a-b|}\), and the latter tends to zero with \(|a-b|\). Existence and elementary norm properties are [Local tools 0.0](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). □

**Proposition A.2 (characteristic maps).** There is a continuous map from a closed disk of real dimension \(c\,d(\sigma)\) into \(G_r(\mathbb F^m)\) whose interior maps homeomorphically onto \(e(\sigma)\). Its boundary maps into cells \(e(\tau)\) with \(\tau_j\leq\sigma_j\) for all \(j\) and \(d(\tau)<d(\sigma)\). These maps are compatible with increasing \(m\).

**Proof.** Define
\[
 \begin{aligned}
 W_j&=F_{\sigma_j}\cap
   \operatorname{span}(e_{\sigma_1},\ldots,e_{\sigma_{j-1}})^\perp,\\
 D_j&=\{z\in W_j\cap e_{\sigma_j}^{\perp}:\|z\|\leq1\},\\
 u_j(z)&=z+\sqrt{1-\|z\|^2}\,e_{\sigma_j}.
 \end{aligned}
\tag{A4}
\]
The space \(W_j\) has \(\mathbb F\)-dimension \(\sigma_j-j+1\), so \(D_j\) is a real disk of dimension \(c(\sigma_j-j)\). Its map \(u_j\) parametrizes the unit vectors in \(W_j\) whose \(\sigma_j\)-th coordinate is real and nonnegative. The inverse forgets that last coordinate.

On the product \(D_\sigma=\prod_{j=1}^rD_j\) set
\[
 O_0=I,\qquad
 O_j=O_{j-1}R_{e_{\sigma_j}}(u_j),\qquad
 v_j=O_{j-1}u_j.
\tag{A5}
\]
The new rotation fixes the earlier coordinate vectors \(e_{\sigma_l}\), \(l<j\), because both \(u_j\) and \(e_{\sigma_j}\) are orthogonal to them. It also fixes everything orthogonal to \(F_{\sigma_j}\). Induction gives \(O_je_{\sigma_l}=v_l\) for \(l\leq j\), with these vectors orthonormal, and \(v_j\in F_{\sigma_j}\). The earlier rotations act inside smaller flag spaces, so they fix \(e_{\sigma_j}\) and preserve its coordinate. Consequently the \(\sigma_j\)-th coordinate of \(v_j\) is \(\sqrt{1-\|z_j\|^2}\).

Define \(\Phi_\sigma\) to be their span. It is continuous in the projection topology, because its projection matrix is
\[
 P_\sigma=\sum_{j=1}^r v_jv_j^*.
\tag{A6}
\]
The projection model and its topology are [DG-CHAR-03 A.1](DG-CHAR-03.md#proposition-a-1). All formulas remain valid on the closed product.

On the product of disk interiors, each pivot coordinate is positive. The plane then has symbol exactly \(\sigma\). To check this rather than only an inequality, take a nonzero linear combination of the \(v_j\) and its largest index with nonzero coefficient. Its coordinate at that index's pivot is nonzero, because earlier vectors lie in smaller flag spaces. It cannot lie below that pivot. This identifies all its flag intersection dimensions.

Conversely a plane in \(e(\sigma)\) has a unique orthonormal basis \(v_1,\ldots,v_r\) with \(v_j\in V\cap F_{\sigma_j}\) and positive real pivot coordinate. Inductively the orthogonal complement of the earlier \(j-1\) vectors in the \(j\)-dimensional intersection is a line. Its pivot coordinate is nonzero, since a zero coordinate would put it in \(V\cap F_{\sigma_j-1}\), which already has dimension \(j-1\). Dividing a nonzero vector on that line by its norm and choosing its sign or complex phase makes the coordinate positive, uniquely. Orthogonal complements and normalization in finite dimensions are established in [DG-CHAR-03 A.1](DG-CHAR-03.md#proposition-a-1).

Recover the disk parameters in order. Given the previous \(O_{j-1}\), put \(u_j=O_{j-1}^{-1}v_j\). The earlier rotations preserve \(F_{\sigma_j}\), fix the later pivot coordinate, and send earlier pivot vectors to the preceding \(v_l\). Thus \(u_j\in W_j\), is a unit vector with positive pivot coordinate, and has the form (A4) for exactly one \(z_j\) with norm less than one. This proves bijectivity of the interior map.

The boundary lies outside \(e(\sigma)\). If \(\|z_j\|=1\), the vectors \(v_1,\ldots,v_j\) all lie in \(F_{\sigma_j-1}\). Every image plane, including every boundary image, has at least \(j\) independent vectors in \(F_{\sigma_j}\), so its actual symbol satisfies \(\tau_j\leq\sigma_j\). The preceding boundary condition makes at least one inequality strict. Hence \(d(\tau)<d(\sigma)\).

This also proves inverse continuity on the interior. If \(A\) is closed in the parameter interior, its closure \(\overline A\) in \(D_\sigma\) is compact by [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and finite product compactness, proved in [DG-CHAR-03 B.1](DG-CHAR-03.md#lemma-b-1). Its image is compact and therefore closed in the Hausdorff Grassmannian. Since no boundary point maps into \(e(\sigma)\),
\(\Phi_\sigma(\overline A)\cap e(\sigma)=\Phi_\sigma(A)\).
Thus the interior bijection is closed onto the cell and its inverse is continuous.

Finally \(D_\sigma\) is a disk, not just a product of disks. Omit zero-dimensional factors and identify the remaining direct sum with a real Euclidean space. Let \(h(z)=\max_j\|z_j\|\). If there are \(s\) factors, then
\[
 h(z)\leq\|z\|\leq\sqrt{s}\,h(z).
\tag{A7}
\]
The map from the Euclidean unit disk to \(D_\sigma\) is
\(z\mapsto z\|z\|/h(z)\) for \(z\ne0\), and zero at zero. Its inverse is \(y\mapsto yh(y)/\|y\|\). These maps are continuous away from zero, inverse by direct substitution, and continuous at zero by (A7). They carry interiors to interiors and boundaries to boundaries. If there are no positive-dimensional factors, the product is one point. Composing with this map gives the stated characteristic disk. All rotations and vectors involve only the first \(\sigma_r\) coordinates, so adjoining ambient zero coordinates leaves the construction unchanged. □

**Theorem A.3 (finite and infinite CW structures).** The cells \(e(\sigma)\) and the maps of A.2 give a finite CW structure on \(G_r(\mathbb F^m)\). Their compatible union gives a Hausdorff closure-finite CW structure on \(G_r(\mathbb F^\infty)\), with its specified final topology.

**Proof.** There are finitely many symbols in dimension \(m\). Let \(X^a\) be the union of cells of real dimension at most \(a\), and let \(X^{-1}=\varnothing\). By A.2, \(X^a\) is the union of the images of the finitely many characteristic disks of dimension at most \(a\): each such image contains its interior cell and has boundary in lower dimensions. It is therefore compact. Every cell closure is precisely its characteristic image. One inclusion follows because this image is closed and contains the cell. For the reverse inclusion, each point of a parameter disk is a limit of interior points, for example by multiplying its coordinates by numbers tending to one from below, and continuity puts its image in the cell closure. The zero-dimensional case is immediate.

Attach all dimension-\(a\) disks to \(X^{a-1}\) by their boundary maps. The resulting quotient is compact, being a quotient of a finite disjoint union of compact spaces. It maps continuously and bijectively to \(X^a\): disk interiors map homeomorphically to distinct cells, and every boundary point was identified with its image in the previous skeleton. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism, as proved in [DG-CHAR-03 B.2](DG-CHAR-03.md#lemma-b-2). Induction proves the finite CW attachment statement.

In the infinite union a cell and its entire characteristic image lie in the finite stage with \(m=\sigma_r\). Each finite stage is a subcomplex, because its symbols are exactly those with \(\sigma_r\leq m\), and A.2's boundary symbols still satisfy that inequality. This proves closure finiteness. A set is closed in the union precisely when its intersections with all finite Grassmannians are closed. By the finite attachment topology just proved, this is equivalent to its inverse image in every characteristic disk being closed. Hence the given topology is the CW weak topology. Hausdorffness and the finite-stage embeddings are [DG-CHAR-03 B.2](DG-CHAR-03.md#lemma-b-2). For \(r=0\), the whole construction is the one-point CW complex. □

**Corollary A.4 (the partition count).** Real cells of dimension \(q\) are counted by partitions of \(q\) with at most \(r\) rows, each of length at most \(m-r\). Complex cells have twice the partition size as their real dimension. In the infinite Grassmannian there is no row-length bound; in each dimension there are only finitely many cells.

**Proof.** For a symbol set
\[
 \lambda_j=\sigma_{r+1-j}-(r+1-j),\qquad 1\leq j\leq r.
\tag{A8}
\]
Strict increase of the \(\sigma_i\) says that \(\sigma_i-i\) is nondecreasing. Thus \(\lambda_1\geq\cdots\geq\lambda_r\geq0\), and \(\lambda_1\leq m-r\). Their sum is \(d(\sigma)\). Conversely such a tuple gives the symbol \(\sigma_i=i+\lambda_{r+1-i}\), so the correspondence is bijective. A.2 gives the real dimension \(c\,d(\sigma)\).

If the partition size is \(q\), each of its at most \(r\) entries lies between zero and \(q\). There are at most \((q+1)^r\) possible tuples, proving finiteness without the row-length restriction. Also \(\sigma_r\leq r+q\), so all these cells and their closures already occur in that finite stage. For \(G_2(\mathbb R^4)\), the six symbols \((1,2),(1,3),(1,4),(2,3),(2,4),(3,4)\) have dimensions \(0,1,2,2,3,4\); for \(\mathbb C\) these dimensions double. When \(r=0\), only the partition of zero occurs. □

## B. From cells to singular homology

The coefficient ring \(R\) in this part is \(\mathbb Z\) or a field. Singular chains have finite support, and all groups in negative degrees are zero. The proofs of homotopy invariance, exact sequences and excision in [DG-CHAR-06 K.1](DG-CHAR-06.md#lemma-k-1), [DG-CHAR-06 E.1](DG-CHAR-06.md#lemma-e-1) and [DG-CHAR-06 E.2](DG-CHAR-06.md#theorem-e-2) apply with these coefficients: their chain formulas are integer formulas, and their relative chain groups are quotients by the indicated simplex submodules.

**Lemma B.1 (the relative group of an attachment).** Suppose a Hausdorff space \(X\) is obtained from \(Y\) by attaching finitely many \(q\)-dimensional disks, with the quotient topology. Then
\[
 H_j(X,Y;R)=
 \begin{cases}
 \displaystyle\bigoplus_{\text{attached }q\text{-disks}}R,&j=q,\\
 0,&j\ne q.
 \end{cases}
\tag{B1}
\]
For \(R=\mathbb Z\), choose a generator of \(H_q(D^q,S^{q-1};\mathbb Z)\) on each oriented disk. Its characteristic map sends that generator to the indicated summand generator. These identifications agree for inclusions that keep the characteristic disks.

**Proof.** First take \(q\geq1\). Write \(p\) for the quotient map from \(Y\) disjoint union the closed disks. The preimage of \(Y\) is the \(Y\)-component together with the disk boundaries, so it is closed; the quotient criterion makes \(Y\) closed in \(X\).

Let \(U\) consist of \(Y\) and the images of the outer collars
\[
 \{x\in D^q:\|x\|>1/2\}.
\tag{B2}
\]
It is open, since its inverse image under \(p\) is open in every component. It deformation retracts to \(Y\). On each collar use the radial homotopy
\[
 x\longmapsto
 \frac{(1-t)\|x\|+t}{\|x\|}\,x,\qquad 0\leq t\leq1,
\tag{B3}
\]
followed by the characteristic map, and fix \(Y\). This fixes boundary points, so the formulas agree on all attaching identifications. The restriction \(p^{-1}(U)\to U\) is a quotient map: for a subset of the open set \(U\), its open inverse image in \(p^{-1}(U)\) is open in the full domain, and the original quotient criterion applies. By [DG-CHAR-03 E.2](DG-CHAR-03.md#lemma-e-2) its product with the interval is also a quotient. Thus (B3) descends to a continuous homotopy, not merely a pointwise deformation.

The resulting relative chain homotopy makes \(H_*(U,Y;R)=0\), by [DG-CHAR-06 K.1](DG-CHAR-06.md#lemma-k-1). The short exact sequence of complexes
\[
 \begin{aligned}
 0\longrightarrow C_*(U;R)/C_*(Y;R)
 &\longrightarrow C_*(X;R)/C_*(Y;R)\\
 &\longrightarrow C_*(X;R)/C_*(U;R)
 \longrightarrow0
 \end{aligned}
\tag{B4}
\]
and [DG-CHAR-06 E.1](DG-CHAR-06.md#lemma-e-1) therefore give \(H_*(X,Y;R)\cong H_*(X,U;R)\). Excision removes \(Y\) from the latter pair, since its closure is contained in the open set \(U\):
\[
 H_*(X,U;R)\cong H_*(X\setminus Y,U\setminus Y;R).
\tag{B5}
\]
The pair on the right is the disjoint union, over the disks, of
\[
 (\{x:\|x\|<1\},\ \{x:1/2<\|x\|<1\}).
\tag{B6}
\]
Indeed, away from the attaching boundaries the quotient makes no identifications and restricts to the disjoint union of the disk interiors with their original topology.

The chain complex of this disjoint union is the direct sum of the component chain complexes: a singular simplex, whose domain is connected, lies in one of the open-and-closed components. Boundary maps keep that component, and cycles and boundaries are computed componentwise. In (B6) the open ball is contractible by scalar multiplication toward zero, and the annulus deformation retracts to the radius-\(3/4\) sphere by interpolating the radius with \(3/4\). The long exact pair sequence and the sphere groups of [DG-CHAR-06 E.5](DG-CHAR-06.md#lemma-e-5) give one copy of \(R\) in degree \(q\) and zero elsewhere. More explicitly, for positive degrees the pair groups are the reduced homology of that sphere shifted by one; in degree zero the map from the annulus's \(H_0\) onto the ball's \(H_0\) is onto, so the relative group is zero. When \(q=1\), the annulus has two components, and the kernel of \(R\oplus R\to R\), \((a,b)\mapsto a+b\), is the required copy of \(R\).

To check the claimed generators, apply the same comparison to a single closed disk. Its collar (B2) deformation retracts to its boundary, so
\[
 \begin{aligned}
 H_q(D^q,S^{q-1};R)
 &\cong H_q(D^q,\{\|x\|>1/2\};R)\\
 &\cong H_q(\{\|x\|<1\},\{1/2<\|x\|<1\};R).
 \end{aligned}
\tag{B7}
\]
The last is excision of the boundary; its closure lies in the relative interior of the collar. Naturality of the pair sequences and excision maps makes (B7) commute with the characteristic map into (B4)–(B6). Thus a disk generator goes to exactly its own summand generator, and inclusions preserving the disk preserve this generator.

For \(q=0\), the attached points have empty boundary and \(X\) is the disjoint union of \(Y\) and those points. The relative chain complex is the direct sum of their point complexes, which have \(H_0=R\) and other homology zero by [DG-CHAR-06 K.1](DG-CHAR-06.md#lemma-k-1). This proves the formula and its generator assertion in every case. □

**Theorem B.2 (cellular homology with its comparison map).** Let \(X\) be a finite CW complex, or a Hausdorff closure-finite CW complex with finitely many cells in each dimension and the weak topology of its characteristic disks. Put
\[
 C_q^{\mathrm{cell}}(X;R)=H_q(X^q,X^{q-1};R),
 \qquad X^{-1}=\varnothing.
\tag{B8}
\]
For \(q\geq1\) define \(d_q\) as the composite of the pair boundary and relativization:
\[
 C_q^{\mathrm{cell}}
 \xrightarrow{\partial_q}H_{q-1}(X^{q-1};R)
 \xrightarrow{j_{q-1}}C_{q-1}^{\mathrm{cell}},
 \qquad d_0=0.
\tag{B9}
\]
Then \(d_{q-1}d_q=0\), and
\[
 H_q(X;R)\cong
 \ker d_q/\operatorname{im}d_{q+1}.
\tag{B10}
\]
The comparison is natural for cellular maps. A subcomplex inclusion induces the inclusion of the corresponding cell generators when their disk generators are chosen consistently.

**Proof.** Each finite-dimensional skeleton here is a finite CW complex. Apply B.1 to successive skeletal attachments. Starting with the discrete zero-skeleton, their long exact pair sequences show by induction that
\[
 H_j(X^a;R)=0\quad(j>a).
\tag{B11}
\]
For the induction step with \(j>a\), both \(H_j(X^{a-1};R)\) and \(H_j(X^a,X^{a-1};R)\) vanish, so exactness gives the assertion. The same sequences show that \(H_j(X^{a-1};R)\to H_j(X^a;R)\) is an isomorphism when \(j<a-1\), because the two adjacent relative groups, in degrees \(j+1\) and \(j\), vanish.

The composite \(d_{q-1}d_q\) contains the two consecutive maps
\[
 H_{q-1}(X^{q-1};R)\longrightarrow
 H_{q-1}(X^{q-1},X^{q-2};R)\longrightarrow
 H_{q-2}(X^{q-2};R)
\tag{B12}
\]
in one exact sequence, hence is zero. The case \(q=1\) follows from \(d_0=0\).

By (B11), the map
\[
 j_q:H_q(X^q;R)\longrightarrow C_q^{\mathrm{cell}}
\tag{B13}
\]
is injective, since the preceding \(H_q(X^{q-1};R)\) vanishes. For \(q\geq1\), the same argument makes \(j_{q-1}\) injective. Exactness of the pair \((X^q,X^{q-1})\) therefore identifies the image of (B13) with \(\ker d_q\). For \(q=0\), \(j_0\) is the identity identification of the zero-skeleton homology with \(C_0^{\mathrm{cell}}\), giving the same conclusion.

The sequence of \((X^{q+1},X^q)\) gives
\[
 H_q(X^{q+1};R)
 \cong H_q(X^q;R)/\operatorname{im}\partial_{q+1},
\tag{B14}
\]
since its degree-\(q\) relative group is zero. Under the injection \(j_q\), the denominator maps onto \(\operatorname{im}d_{q+1}\). Thus \(j_q\) induces (B10) with \(X^{q+1}\) in place of \(X\). All later attachments have dimension at least \(q+2\) and induce isomorphisms in degree \(q\), by the earlier vanishing argument. This proves the result for finite complexes, including complexes of dimension below \(q+1\), whose later skeleta repeat.

For an infinite complex, every finite singular chain has compact image: its finitely many simplices are compact by [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), and finite unions of their continuous images are compact. [DG-CHAR-03 E.1](DG-CHAR-03.md#lemma-e-1) places this image in a finite subcomplex, hence in some finite-dimensional skeleton. Every \(q\)-cycle in \(X\) is consequently represented in a skeleton and, using the already established isomorphisms after \(X^{q+1}\), is homologous to one in \(X^{q+1}\). If a cycle there bounds in \(X\), a finite bounding chain lies in some later skeleton; the same isomorphisms show it already bounds in \(X^{q+1}\). This proves directly that \(H_q(X^{q+1};R)\to H_q(X;R)\) is an isomorphism, completing (B10) without an unproved passage-to-limit assertion.

A cellular map carries \(X^a\) into the corresponding target skeleton. It therefore induces commuting maps on every pair sequence used in (B9), (B13) and (B14). These prove naturality of the induced quotient comparison. For a subcomplex inclusion, B.1 identifies each disk generator with the same characteristic disk in the larger complex. This is exactly the stated inclusion on the cellular chain groups. □

**Corollary B.3 (Grassmannian homology and additive cohomology).** Let \(p_{r,m}(q)\) count partitions of \(q\) with at most \(r\) rows and row lengths at most \(m-r\), and let \(p_r(q)\) count partitions with at most \(r\) rows and no length bound. For finite or infinite real Grassmannians,
\[
 \begin{aligned}
 \dim_{\mathbb F_2}H^q(G_r(\mathbb R^m);\mathbb F_2)&\leq p_{r,m}(q),\\
 \dim_{\mathbb F_2}H^q(G_r(\mathbb R^\infty);\mathbb F_2)&\leq p_r(q).
 \end{aligned}
\tag{B15}
\]
For complex Grassmannians, integral homology and cohomology vanish in odd degrees, and in degree \(2q\) both are free abelian of rank \(p_{r,m}(q)\), or \(p_r(q)\) in the infinite case.

**Proof.** A.3 and A.4 put these spaces within the hypotheses of B.2 and identify their cell counts. Over \(\mathbb F_2\), the homology of a finite-dimensional cellular chain group has dimension at most that chain group's dimension: its cycles form a subspace, and quotienting by boundaries can only decrease dimension, by basis extension. Field evaluation, proved for arbitrary chain complexes after [DG-CHAR-06 U.3](DG-CHAR-06.md#theorem-u-3), identifies singular cohomology with the full linear dual of singular homology. The latter has finite dimension here, so it and its dual have the same dimension, using a basis and its coordinate functionals. This gives (B15).

For the complex spaces all cells have even real dimension. Every cellular differential is zero, since either its source or its target is an odd-degree group and therefore zero. The integral homology is consequently free with one generator for each even-dimensional cell, by B.2. In each degree there are finitely many such generators. Apply the natural coefficient sequence of [DG-CHAR-06 U.3](DG-CHAR-06.md#theorem-u-3) with coefficient group \(\mathbb Z\). Its \(\operatorname{Ext}\) term vanishes whenever the preceding homology group is free, as that theorem proves using a free presentation. Thus evaluation identifies cohomology with the integral dual of homology in every degree, giving the asserted groups.

These are additive statements. They do not yet identify a cup-product generator with a characteristic class, or determine the real Grassmannian's differentials. □

## C. Paracompactness of the countable limits

We use the definitions and proofs in [DG-CHAR-08 Q.1](DG-CHAR-08.md#lemma-q-1) and [DG-CHAR-08 Q.2](DG-CHAR-08.md#lemma-q-2): normality separates disjoint closed sets, paracompactness means that every open cover has a locally finite open refinement, and normal spaces have continuous functions separating disjoint closed sets. The next proof supplies the extension step needed here.

**Lemma C.1 (bounded extension).** Let \(K\) be compact Hausdorff, \(A\subset K\) closed and \(h:A\to[-M,M]\) continuous, with \(M\geq0\). There is a continuous extension \(f:K\to[-M,M]\). In particular a function from \(A\) to \([0,1]\) extends to one from \(K\) to \([0,1]\).

**Proof.** Compact Hausdorff spaces are paracompact, since every open cover has a finite subcover, and are therefore normal by [DG-CHAR-08 Q.1](DG-CHAR-08.md#lemma-q-1). The case \(M=0\) has the zero extension. For \(M>0\), the sets
\[
 A_-=\{x\in A:h(x)\leq-M/3\},\qquad
 A_+=\{x\in A:h(x)\geq M/3\}
\tag{C1}
\]
are disjoint and closed in \(K\), because they are closed in the closed subset \(A\). By [DG-CHAR-08 Q.2](DG-CHAR-08.md#lemma-q-2) there is a continuous \(u:K\to[0,1]\), zero on \(A_-\) and one on \(A_+\). Put \(g=(M/3)(2u-1)\). Then \(|g|\leq M/3\) everywhere, and on \(A\),
\[
 |h-g|\leq 2M/3.
\tag{C2}
\]
On the two end sets \(g\) has the appropriate constant endpoint value, giving this bound directly; between them both \(|h|\) and \(|g|\) are at most \(M/3\).

Repeat this construction on the residual. More precisely set \(h_0=h\), \(M_n=M(2/3)^n\), choose \(g_n\) extending an approximation with \(|g_n|\leq M_n/3\), and put \(h_{n+1}=h_n-g_n|_A\). The same estimate gives \(|h_n|\leq M_n\) by induction. The series
\[
 f=\sum_{n=0}^{\infty}g_n
\tag{C3}
\]
converges uniformly, since the tail is bounded by the tail of the geometric series \(\sum M_n/3=M\); real completeness is [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). It is continuous on the possibly nonmetrizable space \(K\): at a point, choose a partial sum whose uniform tail is less than \(\epsilon/3\), and then a neighborhood on which that finite sum varies by less than \(\epsilon/3\). The two tails and this finite variation bound the variation of \(f\) by \(\epsilon\). Its absolute value is at most \(M\), and the residual estimate tending to zero shows \(f|_A=h\). Empty \(A\) is allowed; the same construction, or the zero function, suffices.

For \(h:A\to[0,1]\), apply the result with \(M=1\) to \(2h-1\) and transform its extension back by \(f\mapsto(f+1)/2\). This preserves the interval bound. □

**Theorem C.2 (paracompactness of compact-stage limits).** Let \(X=\bigcup_{n\geq1}K_n\) be Hausdorff, with the final topology of nested compact Hausdorff subspaces and closed inclusions. Then \(X\) is normal, Lindelöf and paracompact. Every finite product of such spaces has the same properties. In particular these conclusions apply to the infinite real and complex Grassmannians and projective spaces, and their finite products.

**Proof.** First let \(A,B\) be disjoint closed subsets of \(X\). Construct compatible continuous functions \(f_n:K_n\to[0,1]\), zero on \(A\cap K_n\) and one on \(B\cap K_n\). On \(K_1\) this is [DG-CHAR-08 Q.2](DG-CHAR-08.md#lemma-q-2), since compact Hausdorff spaces are normal as in C.1. Given \(f_n\), prescribe a function on the closed subset
\[
 K_n\ \cup\ (A\cap K_{n+1})\ \cup\ (B\cap K_{n+1})
 \quad\text{of }K_{n+1}
\tag{C4}
\]
by \(f_n\), zero and one, respectively. The definitions agree on overlaps. The prescription is continuous by finite closed-set pasting: the inverse image of a closed subset of \([0,1]\) is a finite union of sets closed in the three closed pieces, hence closed in their union. Lemma C.1 extends it to \(f_{n+1}\).

The compatible functions define \(f:X\to[0,1]\). It is continuous, since every stage restriction is continuous and openness is tested on stages. The disjoint open sets \(f^{-1}([0,1/3))\) and \(f^{-1}((2/3,1])\) contain \(A\) and \(B\). This proves normality. Since \(X\) is Hausdorff, singleton sets are closed, so normality also gives the regular shrinking property: for \(x\in U\) open, separate \(\{x\}\) and \(X\setminus U\) by disjoint open sets \(V,O\). Then \(x\in V\subset\overline V\subset U\), because the open set \(O\) containing \(X\setminus U\) misses \(\overline V\).

The space is Lindelöf, meaning that every open cover has a countable subcover. For each compact \(K_n\) choose finitely many members of the cover that cover it, then take their union over \(n\). This is a countable family covering \(X\).

To prove paracompactness directly, start with any open cover \(\mathcal U\). For every \(x\), regularity gives an open \(V_x\ni x\) whose closure lies in some assigned \(U_x\in\mathcal U\). Lindelöfness gives a countable subcover \(V_1,V_2,\ldots\) of these neighborhoods, with \(\overline V_n\subset U_n\in\mathcal U\). If this subcover is finite the same argument below uses that finite list. Define
\[
 W_n=U_n\setminus\bigcup_{k<n}\overline V_k.
\tag{C5}
\]
Each \(W_n\) is open and refines the original cover. They cover \(X\): at a point choose the least index \(n\) for which it lies in \(\overline V_n\); then it lies in \(U_n\) and in none of the earlier closed sets, hence in \(W_n\). They are locally finite: choose \(V_k\) containing a given point; this neighborhood meets none of the \(W_n\) with \(n>k\). This constructs the required locally finite open refinement.

By [DG-CHAR-03 B.1](DG-CHAR-03.md#lemma-b-1), the ordinary product of two such spaces has the final topology of the products of corresponding stages. Those stages are compact Hausdorff, and their inclusions are closed embeddings: the complements of products of closed subsets are unions of the open sets where at least one coordinate leaves the subset. The whole product is Hausdorff by coordinate separation. Induction proves the finite-product assertion, to which the preceding proof applies.

The finite Grassmannians are compact Hausdorff and embedded as closed stages in the Hausdorff infinite Grassmannian by [DG-CHAR-03 A.1](DG-CHAR-03.md#proposition-a-1) and [DG-CHAR-03 B.2](DG-CHAR-03.md#lemma-b-2). Projective spaces are the rank-one cases by [DG-CHAR-03 D.1](DG-CHAR-03.md#example-d-1). Thus all the named spaces satisfy the hypotheses. No countability condition on the compact stages themselves has been used. □

## D. The symmetric-polynomial calculation

This is the algebraic count that accompanies the partition count of cells. It is valid over coefficient rings with torsion and with zero divisors.

**Theorem D.1 (symmetric polynomials over a ring).** For a commutative ring \(R\) with identity, let \(e_j(t_1,\ldots,t_r)\) be the sum of the products of \(j\) distinct variables. Then
\[
 R[t_1,\ldots,t_r]^{S_r}=R[e_1,\ldots,e_r],
\tag{D1}
\]
and the substitution \(R[z_1,\ldots,z_r]\to R[t_1,\ldots,t_r]\), \(z_j\mapsto e_j\), is injective. The number of its monomials of weighted degree \(q\), with \(\deg z_j=j\), is \(p_r(q)\).

**Proof.** The general-ring result is also proved in [Characteristic classes B.1](../../../src/characteristic-classes-and-the-weil-homomorphism.md#lemma-b-1); we give the leading-term calculation here. Order monomials lexicographically with \(t_1>\cdots>t_r\). The leading monomial of \(e_j\) is \(t_1\cdots t_j\), with coefficient one. Lexicographic order is preserved by adding an exponent vector to both sides of a strict inequality. Hence a product of these monic leading terms is the leading term of the product. For
\(\prod_{j=1}^r e_j^{m_j}\), its exponents are
\[
 a_k=\sum_{j=k}^r m_j,\qquad
 m_k=a_k-a_{k+1},\qquad a_{r+1}=0.
\tag{D2}
\]
Thus distinct tuples \(m\) have distinct leading exponent vectors. In a nonzero finite polynomial relation in the \(e_j\), choose the largest such exponent vector among terms with nonzero coefficients. Its coefficient survives unchanged, because that substituted monomial has leading coefficient one and every other substituted term has strictly smaller leading exponent. This proves injectivity, including when \(R\) has zero divisors.

For generation, split a symmetric polynomial into homogeneous pieces. In a nonzero piece, let \(c\,t_1^{a_1}\cdots t_r^{a_r}\) be the leading term, with \(c\ne0\). Symmetry forces \(a_1\geq\cdots\geq a_r\): if adjacent exponents increase, swapping those variables produces a larger monomial with the same nonzero coefficient. Subtract
\[
 c\,e_1^{a_1-a_2}e_2^{a_2-a_3}\cdots
       e_{r-1}^{a_{r-1}-a_r}e_r^{a_r}.
\tag{D3}
\]
This removes the leading term, preserves symmetry and preserves total degree, since \(\deg e_j=j\). There are only finitely many monomials of that total degree. Repeating therefore terminates, expressing the piece, and then the original polynomial, in the \(e_j\). No coefficient was divided.

Finally the nonnegative tuple \(m_1,\ldots,m_r\) of weighted degree \(\sum j m_j=q\) corresponds by (D2) to the partition
\((a_1\geq\cdots\geq a_r\geq0)\) with sum \(q\). The inverse differences in (D2) prove bijectivity, giving \(p_r(q)\). For \(r=0\) both rings are \(R\), and only degree zero has a monomial. For the zero ring the substitution is the unique map between zero rings and is injective; the monomial count is the same combinatorial count of exponent tuples. □

## Further reading

Allen Hatcher, [*Vector Bundles and K-Theory*, author version 2.2, November 2017](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), printed pages 32–36, especially Proposition 1.17 on Schubert cells and Proposition 1.19 on paracompactness. The rotation, boundary, inverse-continuity and bounded-extension arguments needed here are supplied above.

Allen Hatcher, [*Algebraic Topology*, author-hosted Chapter 2](https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf), printed pages 137–140, Lemma 2.34 and Theorem 2.35. The cellular comparison above starts with the explicit collar and excision proof of the relative attachment groups.
