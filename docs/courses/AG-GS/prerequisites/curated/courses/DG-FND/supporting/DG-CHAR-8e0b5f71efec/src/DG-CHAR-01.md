# Vector bundles and their constructions

*Written and self-checked by GPT-6 Astra (OpenAI), at Ultra, October 2026. New exposition dedicated to the public domain under CC0.*

A bundle gives linear coordinates over small open sets. This chapter explains how those coordinates fit together, how a continuous family of linear maps determines subbundles, and how a metric turns an inclusion into a direct-sum decomposition. The same constructions produce the normal bundle of an immersion and a finite-dimensional ambient bundle over a compact base.

Throughout, \(\mathbb F\) is \(\mathbb R\) or \(\mathbb C\). The base \(X\) is an arbitrary topological space until an additional hypothesis is stated. Write \(\varepsilon_X^r=X\times\mathbb F^r\). A rank-\(r\) **vector bundle** is a continuous map \(p:E\to X\), with a vector-space structure on each fibre \(E_x=p^{-1}(x)\), admitting an open cover and homeomorphisms
\[
\phi_\alpha:p^{-1}(U_\alpha)\longrightarrow U_\alpha\times\mathbb F^r
\]
over \(U_\alpha\) whose restrictions to fibres are linear isomorphisms. Ranks may instead be locally constant: all assertions below apply on the open subsets of a fixed rank. No connectedness of those subsets is needed.

The real scalar, norm, finite-basis and calculus results used below are proved in [Local tools 0.0](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), [Local tools 0.2](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), [Local tools 0.3](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and [Local tools 0.4](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). The complex basis-exchange argument is identical: replacing a spanning-list vector by one having a nonzero coefficient in that position requires only division by that coefficient. Thus \(r\) independent vectors in \(\mathbb C^r\) also form a basis. Complex matrix inversion can be treated as real matrix inversion on real and imaginary parts: the inverse commutes with multiplication by \(i\) because the original map does. This observation transfers the local inversion and smooth inversion results of [Local tools 0.4](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) to complex matrices.

## A. Coordinates, maps and frames

**Lemma A.1 (cocycles and inversion).** Bundle charts have continuous transition matrices \(g_{\beta\alpha}:U_\alpha\cap U_\beta\to GL_r(\mathbb F)\) satisfying
\[
\phi_\beta\phi_\alpha^{-1}(x,v)=(x,g_{\beta\alpha}(x)v),
\qquad g_{\gamma\beta}g_{\beta\alpha}=g_{\gamma\alpha}.
\tag{A.1}
\]
Conversely, continuous invertible matrices on an open cover satisfying (A.1), with \(g_{\alpha\alpha}=I\), define a bundle. A continuous fibrewise linear isomorphism between bundles over the identity of a base has a continuous inverse. For smooth matrices and charts these assertions hold smoothly.

**Proof.** Evaluate the fibre part of \(\phi_\beta\phi_\alpha^{-1}\) at each standard basis vector. Its \(r\) resulting columns are continuous, giving \(g_{\beta\alpha}\); the chart composition identity gives (A.1). In particular \(g_{\alpha\beta}=g_{\beta\alpha}^{-1}\). Conversely, on the disjoint union of the \(U_\alpha\times\mathbb F^r\), identify
\[
(x,v)_\alpha\sim(x,g_{\beta\alpha}(x)v)_\beta.
\]
Identity, inverse and composition in (A.1) prove that this is an equivalence relation. Give the quotient \(E\) its quotient topology. The quotient map is open. Indeed the saturation of an open subset of one chart has open intersection with each other chart, since the transition map on the open overlap is a homeomorphism. Its inverse is the transition map in the opposite direction. Taking unions proves the claim for an arbitrary open subset of the disjoint union.

The map \(U_\alpha\times\mathbb F^r\to E\) is injective and open onto its image; that image is exactly \(p^{-1}(U_\alpha)\), which is open. It is therefore a homeomorphism to this image. The projection \(p\) is continuous because its composite with the quotient map is the continuous projection in every summand. Transporting the vector operations through a chart is independent of that chart by the linear transitions. This proves the bundle assertion, even when \(X\) is not Hausdorff.

Let \(T:E\to F\) cover the identity and be linear and invertible in every fibre. On a common trivializing open set it has the form \((x,v)\mapsto(x,A(x)v)\), with continuous matrix entries by evaluation on basis vectors. Inversion is continuous on \(GL_r(\mathbb F)\) by the local inverse-matrix argument specified above. Thus \((x,w)\mapsto(x,A(x)^{-1}w)\) is continuous in each pair of charts. These local inverses agree because they are the inverse of the same fibre map. This proves the assertion globally.

For smooth bundles, the same gluing maps are smooth diffeomorphisms on overlaps. Matrix inversion is smooth by [Local tools 0.4](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) (or its derivative formula there), so the last argument is smooth as well. When a Hausdorff second-countable smooth base is specified, the total space is Hausdorff: different base points are separated below, and points over one base point are separated in a chart. A countable trivializing subcover exists: for each member of a countable basis contained in a trivializing open, select one such open; every point belongs to a selected open. Product bases in these countably many charts give second countability of the total space. Thus the smooth gluing has the usual manifold topology. □

A **bundle map over \(f:X\to Y\)** is a continuous map \(T:E\to F\) with \(p_FT=fp_E\), linear in each fibre. Unless the base map is the identity, “invertible in each fibre” does not assert that \(T\) is a homeomorphism of total spaces. Part B identifies precisely the bundle to which it gives an isomorphism.

**Theorem A.2 (sections and the frame criterion).** A rank-\(r\) bundle is isomorphic to \(\varepsilon_X^r\) if and only if it has \(r\) continuous sections that form a basis in every fibre.

**Proof.** A section is a continuous \(s:X\to E\) with \(ps=\operatorname{id}_X\). In charts the zero section is \(x\mapsto(x,0)\), fibrewise addition is ordinary addition, and scalar multiplication is ordinary multiplication; these descriptions prove continuity of all three operations. They also prove that, for sections \(s_1,\ldots,s_r\), the map
\[
A:X\times\mathbb F^r\longrightarrow E,\qquad
A(x,(a_j))=\sum_{j=1}^r a_js_j(x)
\tag{A.2}
\]
is continuous. If the sections are a basis, it is a fibrewise isomorphism, hence a bundle isomorphism by A.1. Conversely, the images of the constant coordinate sections under a trivialization inverse are the required sections. For rank zero both bundles are the zero bundle and the empty frame works. In particular, a line bundle is trivial precisely when it has a nowhere-zero section. □

**Proposition A.3 (the tautological real line and the Möbius seam).** The tautological real line on \(\mathbb {RP}^n\) is nontrivial for \(n\geq1\). For \(n=1\) it is the bundle
\[
([0,\pi]\times\mathbb R)/((0,t)\sim(\pi,-t))
\tag{A.3}
\]
over the circle obtained by identifying the two endpoints of \([0,\pi]\).

**Proof.** [DG-CHAR-08 R.1](DG-CHAR-08.md#lemma-r-1) constructs the projective quotient topology and its coordinate charts. The total space here is the subspace of \(\mathbb {RP}^n\times\mathbb R^{n+1}\) consisting of \((\ell,v)\) with \(v\in\ell\). On the open set where coordinate \(j\) of a representing vector is nonzero, let \(w_j(\ell)\) be its unique representative with coordinate \(j\) equal to one. The map \((\ell,t)\mapsto(\ell,tw_j(\ell))\) is a bundle chart inverse; its inverse takes the \(j\)-th coordinate of \(v\). Both are continuous by those projective charts.

Suppose \(s\) were a nowhere-zero section. On the unit sphere write
\[
s([x])=t(x)x,\qquad t(x)=\langle s([x]),x\rangle.
\]
This is a continuous real function, and \(t(-x)=-t(x)\). There is an explicit path from \(x\) to \(-x\) in \(S^n\). Choose a vector not in \(\mathbb Rx\), subtract its projection onto \(x\), and normalize to a unit \(w\perp x\). Such a vector exists because \(n+1\geq2\). Normalize the segments \((1-u)x+uw\) and \((1-u)w-u x\), for \(0\leq u\leq1\), and concatenate them. Their norms never vanish, by orthogonality. Along this path the intermediate value theorem, [Local tools 0.0](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), gives a zero of \(t\), a contradiction. Apply A.2.

For the last assertion put \(e_\theta=(\cos\theta,\sin\theta)\), with cosine and sine the real and imaginary parts of the circle exponential. The circle parametrization, its period and the identity \(e_{\theta+\pi}=-e_\theta\) are proved in [Connections and parallel transport E.1](../../../src/connections-and-parallel-transport.md#lemma-e-1). Hence \(\theta\mapsto[e_\theta]\) is a continuous bijection from the endpoint quotient of \([0,\pi]\) to \(\mathbb {RP}^1\). It is a homeomorphism: the source is compact and the target Hausdorff, so images of closed subsets are compact and closed, as proved in [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). The map
\[
(\theta,t)\longmapsto([e_\theta],t e_\theta)
\tag{A.4}
\]
respects exactly the identifications in (A.3). It induces a continuous fibrewise linear bijection to the tautological line. Here is a direct local check of its inverse at the seam, so no compactness of the total space is presumed. On a small interval \(-\delta<u<\delta\), represent the base line by \(e_u\). For \(u\geq0\) the corresponding quotient coordinates are \((u,t)\); for \(u\leq0\) they are \((\pi+u,-t)\). These formulas agree at \(u=0\) in the quotient, and on the two closed half-intervals they are continuous. The finite closed-set pasting rule follows by taking preimages of closed sets, so they give a continuous map on the whole interval times \(\mathbb R\). Its inverse recovers the base coordinate \(u\) and the coefficient along \(e_u\). Away from the seam the usual angle interval does the same. Thus (A.4) is locally an isomorphism and globally a bundle isomorphism. □

## B. Pullbacks and fibrewise algebra

**Theorem B.1 (pullback and its universal description).** If \(f:X\to Y\) is continuous and \(p:F\to Y\) is a bundle, then
\[
f^*F=\{(x,v)\in X\times F:f(x)=p(v)\}\longrightarrow X
\tag{B.1}
\]
is a bundle in its subspace topology. A bundle map \(T:E\to F\) over \(f\) that is an isomorphism in every fibre identifies \(E\) with \(f^*F\). Pullback respects identity maps, composition and restriction.

**Proof.** If \(\phi:p^{-1}(U)\to U\times\mathbb F^r\) is a chart with fibre coordinate \(\phi_2\), the pullback chart is
\[
(x,v)\longmapsto(x,\phi_2(v))
\quad\hbox{on } f^{-1}(U),
\]
with inverse \((x,a)\mapsto(x,\phi^{-1}(f(x),a))\). Both are continuous in the indicated subspaces. They establish local triviality without any separation assumption on \(X,Y\).

For the claimed identification use \(v\mapsto(p_E(v),T(v))\). This is continuous into the product and has image in (B.1), so it is continuous into the subspace. It is a fibrewise isomorphism over \(X\); A.1 supplies its inverse. More generally, this formula gives the unique map into the pullback compatible with both projections, because both its coordinates are prescribed.

For \(g:Z\to X\), the mutually inverse maps
\[
(z,(g(z),v))\longleftrightarrow(z,v)
\]
identify \(g^*(f^*F)\) with \((f\circ g)^*F\); their continuity follows from the product coordinates. Likewise \((x,v)\mapsto v\) identifies \(\operatorname{id}_X^*E\) with \(E\). For an inclusion \(A\subset X\), the same map identifies the pullback with \(p^{-1}(A)\), with their subspace topologies and restricted charts. A constant map \(f(x)=y\) gives \(X\times F_y\), a trivial bundle after any basis of \(F_y\) is chosen. □

**Theorem B.2 (algebraic constructions).** Direct sum, tensor product, dual, Hom, conjugation over \(\mathbb C\), exterior powers and determinant define vector bundles. Their topologies are independent of the chosen trivializations. They commute naturally with pullback. The same holds for any finite-dimensional construction on vector spaces and isomorphisms whose induced matrix maps are continuous and preserve composition and identity.

**Proof.** First give explicit finite-dimensional models, including the facts that ensure continuity. On \(\mathbb F^r\oplus\mathbb F^s\) use concatenated coordinates. Model the tensor product by a vector space with basis \(e_i\otimes f_j\); put \(v\otimes w=\sum_{ij}v_iw_j(e_i\otimes f_j)\). Every bilinear map has a unique linear extension from this model because its values on those basis tensors determine it. This proves the tensor product's universal property. The matrix of \(A\otimes B\) has entries \(A_{ki}B_{\ell j}\), and applying maps to pure tensors proves
\[
(A'\otimes B')(A\otimes B)=(A'A)\otimes(B'B).
\]
The dual has the coordinate functionals as a basis; a change \(v\mapsto Av\) changes dual coordinates by \(A^{-\mathsf T}\). A linear map with matrix \(M\) from the first space to the second changes to \(BMA^{-1}\). The conjugate space \(\overline V\) has the same additive group, with \(\lambda\cdot_{\overline V}v=\overline\lambda v\); conjugating the coordinates makes its transition matrix \(\overline A\).

For \(0\leq k\leq r\), model \(\Lambda^k\mathbb F^r\) with basis \(e_{i_1}\wedge\cdots\wedge e_{i_k}\), \(i_1<\cdots<i_k\). Define \(v_1\wedge\cdots\wedge v_k\) by giving its coordinate on this basis as the corresponding \(k\)-row determinant of \([v_1\ \cdots\ v_k]\). These coordinates are alternating and multilinear. Conversely, expand any alternating multilinear map on basis vectors: repeated indices vanish, and rearranging distinct indices supplies the permutation sign, so this model has the required universal property. The determinant argument [DG-CHAR-06 L.1](DG-CHAR-06.md#lemma-l-1) works over \(\mathbb C\) as well: the permutation expansion, multilinearity and basis exchange are unchanged, and \(2\ne0\). A linear map \(A\) consequently induces \(\Lambda^k A\) by applying \(A\) to each factor. Applying two maps to pure wedges, which span the model, proves the composition rule. Its matrix entries are minors of \(A\), hence polynomials. Set \(\Lambda^0 V=\mathbb F\), and set \(\Lambda^k V=0\) for \(k>r\). The determinant line is \(\det V=\Lambda^rV\); its transition is multiplication by \(\det A\), including rank zero.

Choose common trivializing open sets for the input bundles by intersecting their covers. On each overlap their transition matrices \(A,B\) therefore induce
\[
\begin{array}{c|c}
\text{construction}&\text{transition}\\ \hline
E\oplus F&\operatorname{diag}(A,B)\\
E\otimes F&A\otimes B\\
E^*&A^{-\mathsf T}\\
\operatorname{Hom}(E,F)&M\mapsto BMA^{-1}\\
\overline E&\overline A\\
\Lambda^kE&\Lambda^kA\\
\det E&\det A .
\end{array}
\tag{B.2}
\]
They are continuous and invertible, with inverse obtained from \(A^{-1},B^{-1}\), and the composition identities prove the cocycle condition. A.1 constructs the bundles. The same argument applies to a construction in the final sentence of the theorem; “continuous” there means continuity of the induced map on the matrix spaces in any fixed bases of its finite-dimensional outputs.

Equivalently, take the disjoint union of the intrinsic fibrewise constructions and use these model coordinates as charts. If a different frame is used, the coordinate change is the same continuous induced matrix map. Thus either family of charts defines the same topology; passage to intersections proves this for different open covers. For the direct sum this topology is also the subspace topology on \(E\times_X F\), since both give the same local product coordinates.

For completeness, the usual tensor isomorphisms really are continuous bundle maps. On pure tensors the maps are \(v\otimes w\mapsto w\otimes v\), \((u\otimes v)\otimes w\mapsto u\otimes(v\otimes w)\), \(a\otimes v\mapsto av\), and \(u\otimes(v,w)\mapsto(u\otimes v,u\otimes w)\). Their explicit inverses use the opposite rearrangements; their matrices in the model bases are constant. The coordinate-functional map \(E^*\otimes F\to\operatorname{Hom}(E,F)\) sends \(\lambda\otimes w\) to \(v\mapsto\lambda(v)w\); basis tensors go to the matrix units, so it too is an isomorphism. These maps agree under all frame changes by their formulas and are continuous.

Finally, over \(x\in X\), both the pullback of a construction and the construction of pullbacks have exactly the same model applied to \(E_{f(x)},F_{f(x)}\). This identification is the identity in the pulled-back local coordinates; it is therefore a continuous isomorphism. Smoothness of all these statements follows from the same polynomial and smooth-inverse formulas when the inputs are smooth. □

**Theorem B.3 (partitions with controlled support).** A paracompact Hausdorff space is regular and normal, admits continuous separating functions for disjoint closed sets, and has a continuous partition of unity subordinate to every open cover. For a finite cover \(U_1,\ldots,U_m\), the partition can be taken as \(m\) functions \(\rho_j\), with
\[
0\leq\rho_j\leq1,\qquad
\sum_{j=1}^m\rho_j=1,\qquad
\operatorname{supp}\rho_j\subset U_j.
\tag{B.3}
\]

**Proof.** Here paracompact means that each open cover has a locally finite open refinement, and support means closure of the nonzero set. [DG-CHAR-08 Q.1](DG-CHAR-08.md#lemma-q-1) proves regularity, normality and refinements whose closures are subordinate, starting from precisely this definition. [DG-CHAR-08 Q.2](DG-CHAR-08.md#lemma-q-2) proves the continuous separating-function theorem by nested dyadic opens, including the sublevel and superlevel continuity checks. In particular, for closed \(A\subset O\) open, apply that theorem to \(A,X\setminus O\) and subtract its function from one to obtain a function equal to one on \(A\) and zero off \(O\). [DG-CHAR-08 Q.3](DG-CHAR-08.md#theorem-q-3) then proves the locally finite subordinate-partition theorem from those two results. These earlier proofs apply to arbitrary paracompact Hausdorff spaces and arbitrary, possibly uncountable, covers.

To obtain the last assertion, take that locally finite partition \((\lambda_\alpha)\), assign each support to one \(U_j\), and set \(\rho_j=\sum_{\alpha\text{ assigned to }j}\lambda_\alpha\). Each sum is locally finite and hence continuous, and the sum of all \(\rho_j\) is one. The union of the supports in any one group is closed: near any point only finitely many supports occur, so a point outside their union has a neighbourhood disjoint from the whole union. This union is contained in \(U_j\) and contains the nonzero set of \(\rho_j\), so it contains its closure. That proves the support inclusion in (B.3). Finally, compact Hausdorff spaces are paracompact because a finite subcover is a locally finite refinement of any open cover. All these conclusions therefore apply to compact Hausdorff bases. □

## C. Constant rank, metrics and stabilization

A **subbundle** \(S\subset E\) has the subspace topology, vector subspaces as fibres, and its restricted projection is a vector bundle. A constant dimension alone will be used only together with the continuous local frames or matrices supplied below.

**Lemma C.1 (image and kernel at constant rank).** Let \(T:E\to F\) be a continuous bundle map over \(X\), of constant rank \(k\) locally on \(X\). Then its image and kernel, with their subspace topologies, are subbundles. Their ranks are \(k\) and \(\operatorname{rank}E-k\). The corresponding statement holds smoothly.

**Proof.** Work in charts with an \(s\)-by-\(r\) matrix \(A(x)\), and fix \(x_0\). If \(k=0\), \(A\) is identically zero near \(x_0\), and both assertions are immediate. If \(k>0\), choose a nonzero \(k\)-by-\(k\) minor at \(x_0\). Such a minor exists as follows. Select \(k\) independent columns spanning the image. On their \(k\)-dimensional span the coordinate functionals span the dual, since a vector on which all coordinates vanish is zero; successive basis exchange selects \(k\) independent such restrictions. The associated square coordinate matrix is invertible. This gives the required minor. Its determinant is continuous and nonzero on a smaller neighbourhood. Permuting rows and columns by fixed permutations, write there
\[
A=\begin{pmatrix}B&C\\D&G\end{pmatrix},\qquad B\in GL_k(\mathbb F).
\tag{C.1}
\]
Every remaining column is a linear combination of the first \(k\) columns, because the rank is \(k\). Comparing its first \(k\) entries determines that combination as \(B^{-1}\) times those entries. Hence
\[
G=DB^{-1}C.
\tag{C.2}
\]
The image is the graph \(y\mapsto DB^{-1}y\), \(y\in\mathbb F^k\), inside the target chart. Projection onto its first \(k\) coordinates is a continuous inverse to this parametrization, so this is a subbundle chart in the subspace topology. The kernel is the graph
\[
z\longmapsto(-B^{-1}Cz,z),\qquad z\in\mathbb F^{r-k},
\tag{C.3}
\]
with inverse projection onto the last \(r-k\) coordinates. Formula (C.2) checks that these vectors annihilate both block rows, and the first block row forces exactly (C.3). Thus this also is a subbundle chart. The formulas include the full-rank edge cases, with the corresponding zero-dimensional factors omitted. They are smooth if the input matrix is smooth, proving that assertion.

The rank assumption is necessary. Multiplication by \(x\) as an endomorphism of the trivial real line over \(\mathbb R\) has image of dimension zero at \(0\) and one elsewhere; its kernel has the opposite dimensions. Neither is a vector bundle near \(0\), because dimensions in a bundle chart are locally constant. □

**Theorem C.2 (metrics, projections and splitting).** Every finite-rank real or complex bundle on a paracompact Hausdorff base has a continuous positive definite metric. Given any such metric and any subbundle \(S\subset E\), its orthogonal complement is a subbundle and
\[
S\oplus S^\perp\longrightarrow E,\qquad (v,w)\longmapsto v+w
\tag{C.4}
\]
is an isomorphism. Every fibrewise exact sequence of bundles
\[
0\longrightarrow S\overset{i}{\longrightarrow}E
\overset{q}{\longrightarrow}Q\longrightarrow0
\tag{C.5}
\]
on that base splits.

**Proof.** Pull back the standard coordinate inner product through each trivialization to get local metrics \(h_\alpha\). Take B.3's locally finite partition \(\lambda_\alpha\) subordinate to these trivializations, allowing repeated use of a chart. Define
\[
h_x(v,w)=\sum_\alpha\lambda_\alpha(x)h_{\alpha,x}(v,w).
\tag{C.6}
\]
Each summand extends by zero off its chart. At a base point outside that chart, the closed support of its coefficient is absent on a neighbourhood, which proves continuity of the extension even if the local metric grows near the chart boundary. The sum is locally finite and therefore continuous in every bundle chart. It is symmetric bilinear in the real case and Hermitian, conjugate-linear in the first variable, in the complex case. For \(v\ne0\), some \(\lambda_\alpha(x)>0\), and every contributing \(h_\alpha(v,v)>0\). Hence \(h(v,v)>0\).

Write a local frame of \(S\), expressed in coordinates of \(E\), as the columns of an \(r\)-by-\(k\) matrix \(T\). Write \(h(v,w)=v^*Hw\), where star denotes transpose or conjugate transpose. The matrix \(T^*HT\) is invertible: a nonzero \(a\) has \(Ta\ne0\), so \(a^*T^*HTa>0\), and a square matrix with zero kernel is invertible by basis exchange. The orthogonal projection onto \(S\) is
\[
P=T(T^*HT)^{-1}T^*H.
\tag{C.7}
\]
Indeed multiplication gives \(PT=T\), \(P^2=P\), and \(T^*H(v-Pv)=0\). These equations prove that \(Pv\in S\) and \(v-Pv\in S^\perp\). Their intersection is zero, since a vector perpendicular to itself has zero squared length. They also prove uniqueness of the orthogonal decomposition, so the formulas agree in different frames. In ranks \(k=0,r\), take \(P=0,I\), respectively.

The kernel of \(P\) is \(S^\perp\), and \(P\) is continuous of rank \(k\). C.1 gives its subbundle charts. Equivalently, at \(x_0\) choose constant ambient vectors \(z_1,\ldots,z_{r-k}\) completing the frame of \(S_{x_0}\); then the vectors \((I-P(x))z_j\), together with that frame, form an invertible matrix near \(x_0\). They give a local frame of the complement. The inverse of (C.4) is \(v\mapsto(Pv,(I-P)v)\), continuous in charts.

In (C.5), C.1 and A.1 identify \(S\) with the image of \(i\), a subbundle of \(E\). Choose the metric just constructed on \(E\). The restriction \(q|_{S^\perp}\) has zero kernel and is onto: if \(q(v)=u\), replace \(v\) by its orthogonal-complement component, which has the same image. It is therefore an isomorphism by A.1. Its inverse followed by inclusion gives a right inverse of \(q\), and identifies \(E\) with \(S\oplus Q\). This choice depends on the metric; exactness alone has not selected a distinguished splitting. □

**Theorem C.3 (a finite ambient bundle).** A rank-\(r\) bundle over a compact Hausdorff space embeds as a subbundle of \(\varepsilon_X^N\) for some finite \(N\), and there is a bundle \(F\) with \(E\oplus F\cong\varepsilon_X^N\).

**Proof.** Choose a finite trivializing cover \(U_1,\ldots,U_m\) by compactness and a partition \(\rho_1,\ldots,\rho_m\) as in B.3. If \(a_j(v)\) is the fibre coordinate in chart \(j\), define
\[
J:E\longrightarrow X\times(\mathbb F^r)^m,\qquad
J(v)=\bigl(p(v),(\rho_j(p(v))a_j(v))_{j=1}^m\bigr),
\tag{C.8}
\]
where the \(j\)-th component is zero off \(U_j\). The support argument in C.2 proves that each component is continuous. At any \(x\), some \(\rho_j(x)>0\); the corresponding coordinate is an invertible scalar multiple of a chart coordinate. Thus \(J_x\) is injective.

C.1 makes its image a subbundle of rank \(r\). The induced map \(E\to\operatorname{im}J\) is continuous in the subspace topology, fibrewise invertible and hence an isomorphism by A.1. Inclusion of that image into the ambient bundle makes \(J\) an embedding of total spaces. Give the ambient bundle its usual metric and set \(F=(\operatorname{im}J)^\perp\). C.2 supplies the isomorphism with \(\varepsilon_X^{mr}\). This is a finite stabilization, with no uniform choice of the integer \(m\) asserted across different bases or bundles.

For a locally constant rank on a compact base, the rank takes only finitely many values: its open constant-value subsets cover the base and admit a finite subcover. The same construction on these finitely many open-and-closed subsets, padding ambient coordinates by zeros to a common finite \(N\), gives the corresponding statement without a global constant-rank assumption. □

## D. Smooth bundles in geometry

**Theorem D.1 (tangents, normals and products).** On a Hausdorff second-countable smooth manifold, smooth vector bundles admit smooth positive definite metrics. If \(f:M\to N\) is a smooth immersion, then
\[
f^*TN\cong TM\oplus\nu_f
\tag{D.1}
\]
for a smooth normal bundle \(\nu_f\), after identifying \(TM\) with its image under \(df\). Also
\[
T(M\times N)\cong \pi_M^*TM\oplus\pi_N^*TN.
\tag{D.2}
\]

**Proof.** [Local tools 3.1](../../../src/local-tools-for-bundles-and-transport.md#3-smooth-weights-with-controlled-support) proves smooth partitions of unity on these manifolds; its proof includes the compact-exhaustion and locally finite atlas constructions and the flat smooth cutoff in [Local tools 0.5](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Apply that partition theorem to bundle trivializations. The sum (C.6) is now locally a finite sum of smooth forms, and its extensions by zero are smooth because their coefficients vanish on a neighbourhood of every point outside their supporting chart. This gives the metric; (C.7) and C.1 give smooth complements.

To specify the tangent bundle construction, a tangent vector at \(x\) is a velocity of a smooth curve through \(x\), where two curves agree if their coordinate derivatives agree in one chart. The chain rule, [Local tools 0.3](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), makes this an equivalence independent of that chart. Every coordinate vector is realized by the inverse-chart image of a short straight line. Thus velocities form a vector space with a basis of coordinate velocities. On overlapping charts their coordinate change is the derivative of the coordinate change, an invertible smooth Jacobian. The chain rule supplies (A.1), so A.1 glues these coordinates into \(TM\). For \(f\), the same chain rule shows that \(df_x\) acts on a velocity by the coordinate derivative matrix of \(f\). It therefore defines a smooth map \(TM\to f^*TN\) over the identity.

An immersion means that these matrices are injective at every point. C.1 gives their image as a subbundle; A.1 identifies it with \(TM\). Equip \(f^*TN\) with a smooth metric, for example the pullback of one on \(TN\), and use its orthogonal complement as \(\nu_f\). The smooth version of C.2 proves (D.1). If \(f\) is an embedding, this is the usual splitting of the ambient tangent bundle restricted to the embedded submanifold; the proof needs only immersion.

For a product chart, a curve has velocity \((v,w)\) exactly when its two component curves have velocities \(v,w\). The maps \(d\pi_M,d\pi_N\) consequently give a fibrewise isomorphism in (D.2); its inverse in product coordinates concatenates the two velocity lists. Both maps are smooth and agree on chart overlaps by the chain rule. □

**Example D.2 (spheres and stable triviality).** For \(S^n\subset\mathbb R^{n+1}\),
\[
TS^n=\{(x,v):|x|=1,\ \langle x,v\rangle=0\},
\qquad TS^n\oplus\varepsilon_{S^n}^1\cong\varepsilon_{S^n}^{n+1}.
\tag{D.3}
\]
Odd-dimensional spheres have a smooth nowhere-zero tangent field. Stable triviality does not imply triviality.

**Proof.** The smooth sphere charts are constructed in [DG-CHAR-06 E.5](DG-CHAR-06.md#lemma-e-5). A curve on the sphere has \(\langle x,v\rangle=0\) by differentiating its squared norm. Conversely, for \(v\perp x\), the curve \((x+tv)/|x+tv|\) has velocity \(v\) at zero. This identifies its tangent fibre with \(x^\perp\). The identification is smooth in sphere charts and has a smooth inverse on the bundle image by C.1 and A.1. Its normal line has the global unit section \(x\mapsto x\). The stabilization and its inverse are explicitly
\[
(x,v,t)\longmapsto(x,v+tx),\qquad
(x,w)\longmapsto
\bigl(x,w-\langle w,x\rangle x,\langle w,x\rangle\bigr).
\tag{D.4}
\]
Both formulas are smooth and direct substitution proves that they are inverses.

If \(n=2m-1\), put \(J(a,b)=(-b,a)\) on each of the \(m\) ambient coordinate planes. Then \(\langle x,Jx\rangle=0\) and \(|Jx|=|x|=1\). Thus \(x\mapsto Jx\) is a smooth nowhere-zero tangent field. For \(S^1\) this single vector is a frame and A.2 trivializes \(TS^1\). For higher odd dimensions it establishes a single section, without asserting a full frame.

In contrast, [DG-CHAR-06 N.5](DG-CHAR-06.md#corollary-n-5) proves \(e(TS^2)=2a\ne0\) and proves that \(S^2\) has no continuous nowhere-zero tangent field. A.2 therefore shows that \(TS^2\) is not trivial, while (D.4) makes it stably trivial. For \(n=0\), the tangent bundle has zero-dimensional fibres and (D.4) still holds on the two-point sphere. □

## E. Exercises with solutions

**Exercise E.1 (the tensor square of the Möbius line).** Construct a nowhere-zero section of \(L\otimes L\) for the Möbius line \(L\). Determine whether it supplies a trivialization of \(L\).

**Proof.** In A.3's interval coordinates put \(e_\theta=(\cos\theta,\sin\theta)\). The tensor \(e_\theta\otimes e_\theta\) is unchanged at the seam, since both factors change sign. The tensor transition is the product of the two signs by B.2. Thus this formula descends to a continuous section of \(L\otimes L\), and it is nonzero everywhere in a local tensor basis. A.2 trivializes the tensor square. It does not trivialize \(L\): A.3 proves the latter is nontrivial. □

**Exercise E.2 (independent sections).** Let \(s_1,\ldots,s_k\) be pointwise independent sections of a metric bundle \(E\). Construct its trivial rank-\(k\) summand and the orthogonal projection onto it.

**Proof.** Formula (A.2), with \(k\) columns, defines an injective bundle map \(T:\varepsilon_X^k\to E\). It has constant rank; C.1 gives its image as a subbundle, and A.1 identifies the image with \(\varepsilon_X^k\). In any frame of \(E\), let \(H\) be its metric matrix and let \(T\) also denote the matrix of these sections. Formula (C.7),
\[
P=T(T^*HT)^{-1}T^*H,
\]
is the desired continuous projection. Its intrinsic characterization as the orthogonal projection proves agreement on overlaps. C.2 gives \(E\cong\varepsilon_X^k\oplus(\operatorname{im}T)^\perp\). This conclusion uses the given metric and needs no paracompactness assumption. □

**Exercise E.3 (metric and dual).** Specify the identification with the dual supplied by a real or Hermitian metric.

**Proof.** Send \(v\) to the functional \(w\mapsto h(v,w)\). Over \(\mathbb R\) this is linear in both variables, and over \(\mathbb C\) it is linear in \(w\) and conjugate-linear in \(v\). A vector in its kernel has \(h(v,v)=0\), so \(v=0\). Equal finite dimensions give surjectivity. Its coordinate matrix is continuous because \(H\) is continuous. It is therefore an isomorphism \(E\cong E^*\) over \(\mathbb R\), and an isomorphism \(\overline E\cong E^*\) over \(\mathbb C\): scalar multiplication by \(\lambda\) in \(\overline E\) is multiplication by \(\overline\lambda\) in \(E\), so the two conjugations cancel. A.1 proves continuity of both inverses. The complex statement does not identify \(E\) itself linearly with its dual. □

**Exercise E.4 (finite generators).** On a compact Hausdorff base, produce finitely many global sections spanning every fibre and deduce stabilization by a surjection.

**Proof.** Choose the finite cover and partition of C.3, and a frame \(e_{j1},\ldots,e_{jr}\) on each \(U_j\). Extend \(s_{ja}=\rho_je_{ja}\) by zero outside \(U_j\). The closed support condition proves continuity, as in C.2. At any \(x\), some \(\rho_j(x)>0\), so the \(r\) sections with that \(j\) form a basis of \(E_x\). All \(mr\) sections therefore define a surjective bundle map \(A:\varepsilon_X^{mr}\to E\). C.1 makes \(K=\ker A\) a subbundle. With the standard metric on the source, \(A|_{K^\perp}\) is injective, and it is onto because removing a vector's component in \(K\) does not change its image. A.1 identifies \(K^\perp\) with \(E\), and C.2 gives \(\varepsilon_X^{mr}\cong K\oplus E\). Thus the same finite stabilization can be obtained from spanning sections rather than an embedding. □

**Exercise E.5 (nearby projections).** Let \(P,Q\) be orthogonal projections of the same rank on \(\mathbb F^N\), with operator norm \(\|P-Q\|<1\). Prove that \(Q:\operatorname{im}P\to\operatorname{im}Q\) is an isomorphism, and give the continuous-bundle version.

**Proof.** The operator norm is the supremum of \(|Av|\) over unit vectors; hence \(|Av|\leq\|A\||v|\), by scaling, including \(v=0\). If \(v=Pv\) and \(Qv=0\), then
\[
|v|=|(P-Q)v|\leq\|P-Q\|\,|v|.
\]
Since \(1-\|P-Q\|>0\), this forces \(v=0\). Thus the indicated map is injective. Its source and target have the same finite dimension, so it is onto.

For continuous orthogonal-projection fields on \(X\times\mathbb F^N\), their ranks are locally constant: the trace is continuous and is the rank. To justify the latter identity, decompose the vector space into image and kernel of an idempotent; in a basis formed from those subspaces its matrix is \(\operatorname{diag}(I_k,0)\). Trace is invariant under change of basis, since direct finite index summation gives \(\operatorname{tr}(AB)=\operatorname{tr}(BA)\). Thus the trace is the integer \(k\), and a continuous integer-valued function is locally constant by an interval of radius less than \(1/2\). C.1 now makes both images subbundles. If their ranks agree pointwise and \(\|P(x)-Q(x)\|<1\) at every \(x\), restriction of \(Q\) is a continuous fibrewise isomorphism; A.1 gives a continuous inverse. No uniform gap below one over the whole base is required.

Sharpness is visible on \(\mathbb F^2\): let \(P=\operatorname{diag}(1,0)\) and \(Q=\operatorname{diag}(0,1)\). Then \(P-Q=\operatorname{diag}(1,-1)\) preserves the norm, so its operator norm is one, while \(Q|_{\operatorname{im}P}=0\). □

## Further reading

Allen Hatcher, [*Vector Bundles and K-Theory*, version 2.2, November 2017](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Chapter 1, especially pages 6–15 for bundle coordinates, sections, sums, metrics and tensor constructions, and pages 18–19 for pullbacks. This is the freely accessible author version. The proofs used in this chapter are given above or in the exact earlier programme results linked in the text.
