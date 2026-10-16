# Grassmannians and classifying maps

*Written and self-checked by GPT-6 Astra (OpenAI), at Ultra, October 2026. New exposition: CC0 1.0.*

Let \(\mathbb F\) mean \(\mathbb R\) or \(\mathbb C\), with its usual inner product. Bundles have finite, fixed rank; their bases need not be countable or metrizable. We construct a universal rank-\(r\) bundle and prove that its pullbacks classify bundles over every paracompact Hausdorff base. The topology on the universal space is specified below.

The bundle coordinate, inverse and pullback results are [DG-CHAR-01 A.1](DG-CHAR-01.md#lemma-a-1) and [DG-CHAR-01 B.1](DG-CHAR-01.md#theorem-b-1). The partition theorem is [DG-CHAR-01 B.3](DG-CHAR-01.md#theorem-b-3), including its arbitrary paracompact Hausdorff version. Finite-dimensional estimates, compactness and smooth matrix inversion are proved in [Local tools 0.0](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations) and [Local tools 0.4](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations); determinant identities are [DG-CHAR-06 L.1](DG-CHAR-06.md#lemma-l-1). These results, and the exact further prerequisites linked in the proofs, are the programme inputs.

## A. Finite Grassmannians

**Proposition A.1 (projection and graph coordinates).** For \(0\leq r\leq N\), let
\[
 G_r(\mathbb F^N)=
 \{P\in M_N(\mathbb F):P^*=P,\ P^2=P,\ \operatorname{tr}P=r\}.
\tag{A1}
\]
With its matrix topology this is a compact smooth manifold. Its real dimension is \(r(N-r)\) for \(\mathbb R\), and \(2r(N-r)\) for \(\mathbb C\). It parametrizes \(r\)-dimensional subspaces. At the point represented by a plane \(V\), its tangent space is canonically \(\operatorname{Hom}_{\mathbb F}(V,V^\perp)\). It also has the quotient topology of independent \(r\)-frames modulo change of basis.

**Proof.** An idempotent splits the vector space as its image and kernel: \(x=Px+(x-Px)\), and the intersection is zero. Self-adjointness makes these summands orthogonal. In a basis of the two summands its matrix is \(\operatorname{diag}(I,0)\); the trace is unchanged by basis change because \(\operatorname{tr}(AB)=\operatorname{tr}(BA)\), as expansion of the two finite sums shows. Thus its image has dimension \(r\). Conversely every plane has a unique orthogonal projection. For completeness, an orthonormal basis of a finite-dimensional subspace is obtained by successively subtracting the components along the previously obtained orthonormal vectors and dividing the remaining nonzero vector by its norm. Extending this procedure gives the orthogonal complement and its projection.

The equations (A1) are closed conditions on matrix entries. Orthogonality gives
\(\|x\|^2=\|Px\|^2+\|x-Px\|^2\), so \(\|P\|\leq1\). In particular every entry has absolute value at most one. Closed bounded subsets of a finite-dimensional real space are compact by [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations); complex matrices are regarded as real coordinates here.

If the columns of \(A:\mathbb F^r\to\mathbb F^N\) are independent, the Gram matrix \(A^*A\) is invertible: a vector in its kernel has
\(\|Au\|^2=u^*A^*Au=0\), hence is zero. Direct multiplication shows that
\[
 P_A=A(A^*A)^{-1}A^*
\tag{A2}
\]
is self-adjoint, idempotent and the identity on the image of \(A\). It is therefore the projection onto that image. Replacing \(A\) by \(AC\), with \(C\) invertible, leaves (A2) unchanged, using
\((C^*A^*AC)^{-1}=C^{-1}(A^*A)^{-1}(C^*)^{-1}\).

Fix a plane \(V\), and write matrices in the decomposition \(V\oplus V^\perp\). For another plane \(W\), set \(B=\pi_V|_W\). Its adjoint is \(B^*=P_W|_V\), since the two inner products agree on \(W\) and \(V\). Hence the upper-left block of \(P_W\) is \(BB^*\). It is invertible precisely when \(B\) is an isomorphism. Indeed, \(\ker BB^*=\ker B^*\) by the squared-norm identity; and in equal finite dimensions surjectivity, injectivity and invertibility are equivalent. Thus the condition is open, given by a nonzero determinant of a block of \(P_W\). Denote this open set by \(U_V\).

Every \(W\in U_V\) is uniquely the graph of a map \(T:V\to V^\perp\). Formula (A2) gives its projection:
\[
 P(T)=
 \begin{pmatrix}I\\T\end{pmatrix}
 (I+T^*T)^{-1}
 \begin{pmatrix}I&T^*\end{pmatrix}.
\tag{A3}
\]
The inverse chart is the lower-left block of \(P\) multiplied by the inverse of its upper-left block. Both directions are continuous and smooth in real coordinates, by [Local tools 0.4](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). On overlaps the same block formula composed with a fixed orthogonal change of coordinates gives a smooth transition. These charts cover, since \(V\in U_V\), and have the asserted dimension. The matrix subspace is Hausdorff and second countable: intersections with balls having rational centers and radii form a countable base. Thus these are manifold charts with the usual separation and countability properties.

At \(T=0\), the derivative of (A3) in direction \(S\) is
\[
 dP_0(S)=\begin{pmatrix}0&S^*\\S&0\end{pmatrix}.
\tag{A4}
\]
The inverse chart recovers \(S\), so this is an isomorphism from \(\operatorname{Hom}_{\mathbb F}(V,V^\perp)\) onto the tangent space. Both (A3) and (A4) use only the fixed ambient inner product and the subspace \(V\), and consequently this identification does not depend on bases.

Finally (A2) is a continuous surjection from the open set of independent frames, with fibres exactly the change-of-basis orbits. On \(U_V\) choose an orthonormal basis of \(V\); the frame with columns \(\binom I T\) in this basis is a continuous section. A set whose inverse image in the frame space is open therefore has open intersection with every \(U_V\), and is open. This proves the claimed quotient topology. The same argument includes \(r=0,N\), when the Grassmannian is a point. □

**Theorem A.2 (finite tautological bundle).** The subspace
\[
 \gamma_r^N=\{(P,v)\in G_r(\mathbb F^N)\times\mathbb F^N:Pv=v\}
\tag{A5}
\]
is a rank-\(r\) bundle. Its complementary bundle has fibre \(\ker P\), and their direct sum is the constant bundle \(\varepsilon^N\). Every continuous bundle map \(J:E\to B\times\mathbb F^N\) that is injective on each fibre determines a continuous map \(f_J:B\to G_r(\mathbb F^N)\) and an isomorphism \(E\cong f_J^*\gamma_r^N\).

**Proof.** Over \(U_V\) the map
\[
 (P,u)\longmapsto(P,u+T(P)u),\qquad u\in V,
\tag{A6}
\]
is a continuous trivialization of (A5). Its inverse sends \((P,v)\) to \((P,\pi_Vv)\). These maps are inverse because \(P\) represents the graph of \(T(P)\). Their formulas also prove smooth local triviality. The map \(P\mapsto I-P\) is a continuous smooth involution from \(G_r(\mathbb F^N)\) to \(G_{N-r}(\mathbb F^N)\). Pulling back the latter tautological bundle gives the complementary one. Addition identifies their sum with the constant bundle; its inverse is \(v\mapsto(Pv,(I-P)v)\).

In a local frame of \(E\), the columns of \(J\) form a continuous independent matrix \(A(b)\). Formula (A2) defines \(f_J(b)\) continuously, and its change-of-basis invariance makes the definitions agree on overlaps. The map \(v\mapsto(b,Jv)\) into the pullback is continuous and is a linear isomorphism on each fibre. Its inverse is continuous by the coordinate inversion result [DG-CHAR-01 A.1](DG-CHAR-01.md#lemma-a-1); the pullback is a bundle by [DG-CHAR-01 B.1](DG-CHAR-01.md#theorem-b-1). This proves the assertion on arbitrary bases. □

## B. The topology of finite-support vectors

**Lemma B.1 (products of compact exhaustions).** Suppose \(X=\bigcup_nK_n\) and \(Y=\bigcup_nL_n\) have the final topologies of nested compact Hausdorff subspaces with closed inclusions. Thus a set is open in \(X\) exactly when its intersection with every \(K_n\) is open there, and likewise for \(Y\). The product topology on \(X\times Y\) is the final topology of \(K_n\times L_n\).

**Proof.** First recall the finite compactness facts we need. A compact Hausdorff space is paracompact, since every open cover has a finite subcover, which is a locally finite refinement. It is regular and normal by [DG-CHAR-08 Q.1](DG-CHAR-08.md#lemma-q-1). In particular a compact subset of an open set has an open neighborhood whose compact closure stays in that set: choose a smaller neighborhood with closure inside the open set at each point and then take a finite union.

The product of two compact spaces is compact. To check this directly, refine an open cover of \(K\times L\) by rectangles. For fixed \(x\), finitely many rectangles cover \(\{x\}\times L\); intersect their first-coordinate neighborhoods to obtain \(U_x\) such that \(U_x\times L\) is covered by those finitely many original cover members. Finitely many \(U_x\) cover \(K\), giving a finite subcover of the product. Products of Hausdorff spaces are Hausdorff by separating a coordinate in which two points differ.

We also use a rectangle enlargement fact. If \(A\times B\) is a product of compact subsets contained in an open subset \(O\) of a product, then there are open \(U\supset A\), \(V\supset B\) with \(U\times V\subset O\). For fixed \(a\), finitely many rectangles in \(O\) cover \(\{a\}\times B\); intersect the first factors and unite the second factors. This gives \(U_a\ni a\), \(V_a\supset B\) with \(U_a\times V_a\subset O\). Cover \(A\) by finitely many \(U_a\), and use their union and the intersection of the corresponding \(V_a\).

Every product-open set is stage-open, because the inclusions are continuous. Conversely let \(W\subset X\times Y\) be stage-open and let \((x,y)\in W\cap(K_m\times L_m)\). Regularity supplies compact neighborhoods \(A_m\ni x\), \(B_m\ni y\) in these stages with \(A_m\times B_m\subset W\). Inductively, regard \(A_n,B_n\) as compact subsets of the next stages. The enlargement fact and regularity give compact neighborhoods
\[
 A_n\subset\operatorname{int}_{K_{n+1}}A_{n+1},
 \qquad
 B_n\subset\operatorname{int}_{L_{n+1}}B_{n+1},
 \qquad A_{n+1}\times B_{n+1}\subset W.
\tag{B1}
\]
Put \(U=\bigcup_{n\geq m}A_n\), \(V=\bigcup_{n\geq m}B_n\). These unions are open in their final topologies. Indeed, if \(z\in U\cap K_j\), choose \(n\) with \(z\in A_n\) and then \(k\geq n,j,m\). A neighborhood of \(z\) in \(K_{k+1}\) lies in \(A_{k+1}\) by (B1); its intersection with \(K_j\) is an open neighborhood contained in \(U\cap K_j\). The same proof applies to \(V\). Nestedness gives \(U\times V\subset W\). Hence \(W\) is product-open. □

**Lemma B.2 (operations and frames in the direct limit).** Give
\[
 \mathbb F^\infty=\bigcup_{N\geq1}\mathbb F^N,\qquad
 G_r(\mathbb F^\infty)=\bigcup_{N\geq\max(r,1)}G_r(\mathbb F^N)
\tag{B2}
\]
their final topologies, where inclusions append zero coordinates, or extend a projection by zero. Both spaces are Hausdorff, their finite stages are embedded and closed, and finite products and products with \([0,1]\) have the corresponding compact-stage final topologies. Addition, scalar multiplication, coordinate shifts, inner products and projection evaluation are jointly continuous. The map from independent \(r\)-tuples in \((\mathbb F^\infty)^r\) to their span in \(G_r(\mathbb F^\infty)\) is continuous.

**Proof.** A map out of a final space is continuous if and only if its restrictions to all stages are continuous, since openness of inverse images is tested on the stages. The same is true on an open subset \(U\): a set open in every \(U\cap K_n\) is open in \(K_n\), because \(U\cap K_n\) is open there, and hence is open in the full final space.

Each vector coordinate and each projection matrix entry is continuous by the first observation. These functions separate points, proving Hausdorffness. A finite vector stage is closed, since it is the intersection of the zero sets of the later coordinates. Its induced topology is Euclidean: inclusion is continuous, and projection to the first \(N\) coordinates restricts to its inverse. For a finite Grassmannian stage, A.1 gives compactness. A compact subset of a Hausdorff space is closed: for a point outside it, separate that point from each of its points, use finitely many of the neighborhoods on the compact set, and intersect the corresponding neighborhoods of the outside point. The same argument shows that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism onto its image, by applying closedness to compact closed subsets. This proves the assertion for the Grassmannian inclusions.

Let \(D_n\) be the closed ball of radius \(n\) in \(\mathbb F^n\). The final topology of these compact sets on \(\mathbb F^\infty\) is exactly its specified topology. One direction follows by restriction. For the other, if \(A\cap D_n\) is closed for every \(n\), fix \(N\) and \(x\in\mathbb F^N\setminus A\). Choose \(n\geq N\) with \(n>\|x\|\). A neighborhood of \(x\) in \(D_n\) misses \(A\), and its intersection with the interior radius-\(n\) ball of \(\mathbb F^N\) is a neighborhood in \(\mathbb F^N\) missing \(A\). Thus \(A\cap\mathbb F^N\) is closed. Lemma B.1 now applies to the \(D_n\), the compact Grassmannians, scalar balls and a constant interval stage. Iterating it proves the finite-product assertions.

Addition and scalar multiplication restrict on every compact product stage to the usual operations in a finite-dimensional vector space, followed by its continuous inclusion. The same is true of each fixed coordinate shift \(e_i\mapsto e_{2i}\) or \(e_i\mapsto e_{2i-1}\). Inner products restrict to finite sums of products of coordinates. Finally
\[
 (P,v)\longmapsto Pv
\tag{B3}
\]
restricts on \(G_r(\mathbb F^n)\times D_n\) to ordinary matrix evaluation into \(\mathbb F^n\). The product result proves all these joint continuity statements.

For \(r\) vectors \(v_1,\ldots,v_r\), their Gram determinant is continuous by joint continuity of the inner product. It is nonzero precisely when the vectors are independent: the Gram matrix has kernel consisting of the coefficients of zero linear combinations, by the squared-norm calculation in A.1. Thus the independent-frame locus is open in the product. Restricted to a compact product stage, its span map is (A2) into a finite Grassmannian, and is continuous. The open-subset observation at the start of the proof gives continuity on the full independent-frame locus. No local bound on the coordinate support of a general continuous family of frames is required.

In either direct limit, every compact subset is contained in a finite coordinate stage. Otherwise select points in it whose least possible stage indices strictly increase. Each finite stage meets the selected set in finitely many points, so every subset of the selected set is closed in every stage and hence in the full space. The selected set is closed in the compact subset and therefore compact, but its induced topology is discrete: all its subsets are closed and hence also open. The cover by singletons has no finite subcover, a contradiction.

These are finite-support direct limits. Their topology is not the norm topology inherited from square-summable sequences: for example
\(\{v:\sum_{i\geq1}i^2|v_i|^2<1\}\) is open in every finite stage, hence open here, but contains no norm ball about zero, as the vectors \(2e_i/i\) show. □

**Theorem B.3 (the universal tautological bundle).** The subspace
\[
 \gamma_r=\{(P,v)\in G_r(\mathbb F^\infty)\times\mathbb F^\infty:Pv=v\}
\tag{B4}
\]
is a locally trivial rank-\(r\) bundle. Its restriction to \(G_r(\mathbb F^N)\) is \(\gamma_r^N\).

**Proof.** Fix a plane \(V\) contained in a finite coordinate stage. For any finite-support projection \(P\), put
\[
 A_V(P)=\pi_VP|_V,\qquad
 U_V=\{P:\det A_V(P)\ne0\}.
\tag{B5}
\]
The determinant is continuous stage by stage, so \(U_V\) is open in the direct limit. The argument with \(BB^*\) in A.1, performed in a finite stage containing \(V\) and \(\operatorname{im}P\), shows that \(\pi_V:\operatorname{im}P\to V\) is an isomorphism exactly on \(U_V\). Its inverse is
\[
 u\longmapsto P A_V(P)^{-1}u.
\tag{B6}
\]
Indeed this vector lies in \(\operatorname{im}P\), and its projection to \(V\) is \(u\).

The map (B6) is jointly continuous in \((P,u)\in U_V\times V\). The product \(G_r(\mathbb F^\infty)\times V\) has the compact-stage final topology by B.1, and \(U_V\times V\) is open in it. On each stage (B6) is smooth matrix inversion and multiplication, with values in a single finite vector stage. Therefore B.2's open-subset criterion applies. This proves that
\((P,u)\mapsto(P,PA_V(P)^{-1}u)\) is a continuous map into the actual subspace (B4). Its inverse is \((P,v)\mapsto(P,\pi_Vv)\), continuous because \(\pi_V\) is continuous on every finite vector stage. The \(U_V\) cover, since the plane of any point can itself be chosen as \(V\). They give the claimed bundle charts.

Over \(G_r(\mathbb F^N)\), a vector fixed by \(P\) lies in \(\mathbb F^N\). Both finite stages carry their original subspace topologies by B.2, so the restricted total space, as well as its charts, is precisely (A5). □

## C. Classification over paracompact Hausdorff spaces

**Theorem C.1 (countable trivializations and existence).** Let \(E\to B\) be a rank-\(r\) real or complex bundle over a paracompact Hausdorff space. There is a countable locally finite trivializing open cover of \(B\), and a continuous map \(f:B\to G_r(\mathbb F^\infty)\) with \(E\cong f^*\gamma_r\). If \(B\) is compact, the map and the bundle embedding can be taken in a finite coordinate stage.

**Proof.** The countable-trivialization construction and the subordinate countable partition are proved in [DG-CHAR-08 Q.6](DG-CHAR-08.md#lemma-q-6). We recall its sets to verify the additional local-finiteness assertion about the cover itself. Start with a locally finite partition \((\lambda_\beta)\) subordinate to arbitrary trivializing neighborhoods; its existence, with supports contained in those neighborhoods, is [DG-CHAR-01 B.3](DG-CHAR-01.md#theorem-b-3). For each nonempty finite set \(S\) of indices put
\[
 V_S=\left\{b:
 \min_{\beta\in S}\lambda_\beta(b)>0,\quad
 \min_{\beta\in S}\lambda_\beta(b)>
       \sup_{\gamma\notin S}\lambda_\gamma(b)\right\}.
\tag{C1}
\]
The supremum includes zero; local finiteness makes it locally the maximum of finitely many functions and zero, hence continuous. These sets are open. If \(|S|=|T|\) and \(S\ne T\), choose one index in each of \(S\setminus T\) and \(T\setminus S\); membership in both sets would give two contradictory strict inequalities between their values. Thus \(V_k=\bigcup_{|S|=k}V_S\) is a disjoint union of open sets. For each \(S\), choosing an index in \(S\) places \(V_S\) inside its trivializing neighborhood. The resulting trivializations, all of rank \(r\), combine to a trivialization on \(V_k\).

The sets \(V_k\), \(k\geq1\), cover \(B\): at a point take \(S\) to be its nonempty finite set of positive partition coordinates. They form a locally finite cover. Near any given point only finitely many of the supports of \(\lambda_\beta\) meet a neighborhood, say those of an index set \(F\). If \(V_S\) meets that neighborhood then \(S\subset F\), so only \(k\leq|F|\) can occur. This is local finiteness of the countable cover, even when the original index set is uncountable.

There is a locally finite partition \((\mu_k)\) with \(\operatorname{supp}\mu_k\subset V_k\). To see the support detail, apply [DG-CHAR-01 B.3](DG-CHAR-01.md#theorem-b-3) to this cover and assign each resulting function to a containing \(V_k\). Sum all functions assigned to \(k\). The sums are locally finite and continuous; the unions of their supports are closed, because a locally finite union of closed sets is closed, as proved in [DG-CHAR-08 Q.1](DG-CHAR-08.md#lemma-q-1). Thus each grouped support still lies in \(V_k\), and the grouped family is locally finite.

Let \(\phi_k:E|_{V_k}\to\mathbb F^r\) be the fibre coordinate in the chosen trivialization. Extend \(\mu_k\phi_k\) by zero outside \(V_k\) and define, using successive blocks of \(r\) coordinates,
\[
 J(v)=\bigl(\mu_1(b)\phi_1(v),\mu_2(b)\phi_2(v),\ldots\bigr),
 \qquad v\in E_b.
\tag{C2}
\]
Each zero extension is continuous: outside \(V_k\) there is a neighborhood missing the closed support of \(\mu_k\), where the extension is zero. Near any base point only finitely many blocks occur, so (C2) locally maps continuously into one finite vector stage and hence into \(\mathbb F^\infty\). At least one \(\mu_k(b)\) is positive, proving fibrewise injectivity.

In any local frame of \(E\), the \(r\) columns of \(J\) form a continuous independent frame. Lemma B.2 makes its span \(f(b)\) continuous. The map \(v\mapsto(b,Jv)\) is a continuous fibrewise isomorphism to \(f^*\gamma_r\); B.3 and [DG-CHAR-01 B.1](DG-CHAR-01.md#theorem-b-1) make this a bundle, and [DG-CHAR-01 A.1](DG-CHAR-01.md#lemma-a-1) makes the inverse continuous.

If \(B\) is compact, the local finiteness neighborhoods of the grouped partition have a finite subcover. Only finitely many indices meet their union, so only finitely many blocks in (C2) occur anywhere. This gives the last assertion. Empty sets in the cover may be discarded; for \(r=0\) the zero bundle and the constant classifying map give the conclusion directly. □

**Theorem C.2 (homotopy of bundle injections).** For any base space \(B\), let \(J_0,J_1:E\to\mathbb F^\infty\) be continuous maps which are linear and injective on each fibre of a fixed finite-rank bundle. There is a jointly continuous family of such injections joining them, and hence a homotopy between their span maps \(B\to G_r(\mathbb F^\infty)\).

**Proof.** Index coordinates starting with \(1\), and define \(S_e e_i=e_{2i}\), \(S_o e_i=e_{2i-1}\). The linear map
\[
 L_e(t)=(1-t)I+tS_e,\qquad 0\leq t\leq1,
\tag{C3}
\]
is injective. For a nonzero finite-support vector \(v\), let \(m\) be its last nonzero index. At \(t>0\), coordinate \(2m\) of \(L_e(t)v\) is \(tv_m\ne0\); at \(t=0\) the map is the identity. The same proof applies to \(L_o(t)=(1-t)I+tS_o\) when \(m>1\), using coordinate \(2m-1\). When \(m=1\), \(S_o\) fixes the vector, so injectivity again holds.

First use \(L_e(t)J_0\) to reach \(S_eJ_0\). Next use
\[
 K_t=(1-t)S_eJ_0+tS_oJ_1 .
\tag{C4}
\]
For \(0<t<1\), the two summands have disjoint even and odd coordinate supports. If \(K_t(v)=0\), each summand vanishes, and injectivity of \(J_0\) gives \(v=0\). At the endpoints there is one injection. Finally reverse \(L_o(t)J_1\) to reach \(J_1\). Rescale these three paths to the three successive thirds of the parameter interval.

Every displayed map is jointly continuous on \(E\times[0,1]\), by the continuous vector operations in B.2. The three pieces agree at their endpoints, so their concatenation is continuous: the inverse image of a closed set is the finite union of sets closed in the three closed parameter strips, hence closed in the whole product. It is linear and injective on every fibre at every time.

In a local frame, evaluate this family on the continuous frame sections. The columns form a jointly continuous map \(B\times[0,1]\) locally into the independent-frame locus of \((\mathbb F^\infty)^r\). Its span is continuous by B.2. The span does not depend on the local frame, so these maps glue to the required homotopy. This argument applies to arbitrary continuous injections, not only to the locally finite coordinate construction of C.1. □

**Lemma C.3 (transport along a projection homotopy).** If \(B\) is paracompact Hausdorff and \(H:B\times[0,1]\to G_r(\mathbb F^\infty)\) is continuous, the pullbacks of \(\gamma_r\) by \(H(\,\cdot\,,0)\) and \(H(\,\cdot\,,1)\) are isomorphic.

**Proof.** A finite-support matrix acts on finite-support vectors. Give these matrices the operator norm
\[
 \|A\|=\sup_{\|v\|=1,\ v\in\mathbb F^\infty}\|Av\|.
\tag{C5}
\]
If all entries of \(A\) occur in its first \(N\) rows and columns, this is exactly the ordinary norm on \(\mathbb F^N\): later coordinates do not contribute to the output and cannot increase the supremum. The triangle inequality and homogeneity follow pointwise and then by taking suprema. In a fixed finite stage the bound
\(\|A\|\leq(\sum_{i,j}|A_{ij}|^2)^{1/2}\), from the finite Cauchy–Schwarz inequality of [Local tools 0.0](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations), proves continuity in the matrix entries; also
\(|\|A\|-\|B\||\leq\|A-B\|\).
Consequently the map from the direct-limit Grassmannian to this normed matrix space is continuous, because its restriction to every finite stage is continuous. No completed ambient vector space is needed.

Write \(P(b,t)=H(b,t)\). For each \(b_0\) there are an open neighborhood \(V\) and a number \(d_V>0\) such that
\[
 \|P(b,s)-P(b,t)\|<1
 \quad\text{if } b\in V,\quad |s-t|\leq d_V.
\tag{C6}
\]
Here are the uniformity details. The continuous map \(t\mapsto P(b_0,t)\) on the compact interval is uniformly continuous by [Local tools 0.1](../../../src/local-tools-for-bundles-and-transport.md#0-analytic-and-linear-foundations). Choose a positive bound \(d_V\) smaller than half a uniform-continuity threshold so that \(|s-t|\leq d_V\) gives norm variation less than \(1/4\) at \(b_0\). The function
\((b,t)\mapsto\|P(b,t)-P(b_0,t)\|\) is continuous and zero on \(\{b_0\}\times[0,1]\). Each point of that compact slice has a product neighborhood on which it is less than \(1/4\); finitely many interval factors cover the interval. Intersect their base neighborhoods to obtain \(V\) on which the bound holds for every time. The triangle inequality now makes the left side of (C6) less than \(3/4\).

Use [DG-CHAR-01 B.3](DG-CHAR-01.md#theorem-b-3) to choose a locally finite partition \((\rho_a)\) subordinate to neighborhoods \(V_a\) of this kind, and set
\[
 \delta(b)=\sum_a\rho_a(b)\min(d_{V_a},1)>0,\qquad
 t_j(b)=\min(j\delta(b),1),\quad j=0,1,\ldots .
\tag{C7}
\]
Both functions are continuous. At a fixed point only finitely many weights are positive, so \(\delta(b)\) is at most the largest of their bounds \(\min(d_{V_a},1)\). The neighborhood giving that largest bound contains \(b\), and (C6) is therefore valid whenever \(|s-t|\leq\delta(b)\).

For consecutive times, use the linear map
\[
 P(b,t_{j+1}(b)):
 \operatorname{im}P(b,t_j(b))
 \longrightarrow \operatorname{im}P(b,t_{j+1}(b)).
\tag{C8}
\]
It is an isomorphism by [DG-CHAR-01 E.5](DG-CHAR-01.md#exercise-e-5): if a vector \(v\) in the first image were killed by the next projection, then
\(\|v\|\leq\|P(b,t_j)-P(b,t_{j+1})\|\|v\|<\|v\|\)
unless \(v=0\); equal finite ranks give surjectivity. This proof works in any common finite coordinate stage and uses exactly the norm (C5).

Compose (C8) until \(t_j=1\). Further factors are the identity on the final image, so the product stabilizes. Near any given base point the positive continuous function \(\delta\) has a positive lower bound. A single integer \(j\) thus suffices on that neighborhood, and there the transport is a finite composition. Each factor is continuous as a map on the relevant total spaces: \(b\mapsto P(b,t_j(b))\) is continuous into the direct-limit Grassmannian, and projection evaluation is jointly continuous by B.2. The locally finite-length products agree where neighborhoods overlap, since extra endpoint projections act as the identity. They therefore define a continuous bundle map from the time-zero pullback to the time-one pullback, into their actual subspace total spaces from B.3. It is a fibrewise isomorphism, so [DG-CHAR-01 A.1](DG-CHAR-01.md#lemma-a-1) proves continuity of its inverse. No uniform step count on all of \(B\) has been assumed. □

**Theorem C.4 (natural bundle classification).** For every paracompact Hausdorff \(B\), pullback induces a natural bijection
\[
 [B,G_r(\mathbb F^\infty)]
 \ \longrightarrow\
 \{\text{rank-}r\ \mathbb F\text{-bundles on }B\}/\cong .
\tag{C9}
\]
The brackets on the left mean unbased homotopy classes of continuous maps.

**Proof.** By B.3 and [DG-CHAR-01 B.1](DG-CHAR-01.md#theorem-b-1) every map gives a bundle. Lemma C.3 shows that homotopic maps give isomorphic bundles, so (C9) is well defined. Theorem C.1 proves surjectivity.

For injectivity, suppose the pullbacks by \(f_0,f_1\) are isomorphic and identify them with one bundle \(E\). Projection from either pullback to the vector coordinate of (B4) gives a continuous fibrewise injection \(J_i:E\to\mathbb F^\infty\) whose span is exactly \(f_i\). Theorem C.2 supplies a homotopy from \(f_0\) to \(f_1\). Thus (C9) is injective.

If \(g:B'\to B\) is a continuous map between paracompact Hausdorff spaces, the isomorphism
\((f\circ g)^*\gamma_r\cong g^*(f^*\gamma_r)\) is the pullback-composition isomorphism of [DG-CHAR-01 B.1](DG-CHAR-01.md#theorem-b-1), explicitly sending the same vector over \(g(b')\) to the corresponding vector over \(b'\). Precomposing a homotopy by \(g\times1\) gives a homotopy. These observations prove naturality.

For a compact Hausdorff base all bundles come from finite Grassmannians by C.1. Every homotopy between two such classifying maps takes values in one finite stage: \(B\times[0,1]\) is compact by B.1, and compact subsets of the direct-limit Grassmannian lie in a finite stage by B.2. Thus finite-stage classifying maps classify compact-base bundles up to homotopy after enlarging the ambient dimension. For \(r=0\) both sides have one element; if \(B\) is empty the same convention applies. □

## D. Projective spaces and Gauss maps

**Example D.1 (line, tangent and normal classifying maps).** In rank one the construction recovers real and complex projective space and its tautological line. The Gauss map of a smooth immersion classifies both its tangent bundle and its normal bundle. For the unit sphere the tangent projection is \(I-xx^{\mathsf T}\), and adjoining the normal line trivializes its tangent bundle.

**Proof.** A line spanned by a nonzero vector \(z\in\mathbb F^N\) has projection
\[
 P_z=\frac{zz^*}{z^*z}.
\tag{D1}
\]
Replacing \(z\) by a nonzero scalar multiple leaves this unchanged, and every rank-one projection occurs. Proposition A.1 identifies the quotient topology by scalar changes with the Grassmannian topology. Thus \(G_1(\mathbb R^N)=\mathbb {RP}^{N-1}\) and \(G_1(\mathbb C^N)=\mathbb {CP}^{N-1}\) as topological and smooth spaces.

Their inclusions into the infinite Grassmannian classify their tautological lines, by B.3. The infinite tautological line agrees with the earlier programme construction [DG-CHAR-08 I.2](DG-CHAR-08.md#lemma-i-2), including its topology: on the open set \(P_{jj}>0\), the vector with \(j\)-th coordinate \(t\) in the line is \(tPe_j/P_{jj}\). Hence its \(k\)-th coordinate is \(tP_{kj}/P_{jj}\), exactly the transition formula of that construction. Formula (B6) proves continuity of this chart into the subspace total space, and the \(j\)-th coordinate is its continuous inverse. Thus the chartwise identification is a bundle isomorphism.

Now let \(f:M^r\to\mathbb R^N\) be an immersion. Its differential is fibrewise injective. In a coordinate chart \(x_1,\ldots,x_r\) on \(M\), the columns of its derivative matrix \(A(x)\) are independent and smooth. Formula (A2) therefore gives a smooth map
\[
 g_f:M\to G_r(\mathbb R^N),\qquad
 g_f(x)=df_x(T_xM).
\tag{D2}
\]
Changing coordinates changes only the basis of the image, so the formula agrees on overlaps. The bundle map \(df\) identifies \(TM\) with \(g_f^*\gamma_r^N\), by A.2. Its orthogonal complement is the normal bundle of [DG-CHAR-01 D.1](DG-CHAR-01.md#theorem-d-1); it is the pullback of the complementary bundle in A.2. This works for immersions even if their images intersect themselves, since the plane is assigned to the point of \(M\), not to an unlabelled image point.

For \(S^n\subset\mathbb R^{n+1}\), the tangent space at \(x\) is \(x^\perp\), as proved in [DG-CHAR-01 D.2](DG-CHAR-01.md#example-d-2). Its projection is \(I-xx^{\mathsf T}\); direct multiplication uses \(x^{\mathsf T}x=1\) to verify idempotence and image \(x^\perp\). The normal line has the global unit section \(x\). The isomorphism
\[
 T_xS^n\oplus\mathbb R\longrightarrow\mathbb R^{n+1},
 \qquad (v,a)\longmapsto v+ax
\tag{D3}
\]
has inverse \(w\mapsto(w-(x\cdot w)x,x\cdot w)\), continuous and smooth in \(x,w\). Thus \(TS^n\oplus\varepsilon^1\cong\varepsilon^{n+1}\), whether or not \(TS^n\) itself is trivial. □

## E. Two facts about attaching spaces

These facts are useful when a base is given by cells. The classification theorem above does not require a cellular structure on either the base or the Grassmannian.

**Lemma E.1 (compact subsets of a CW complex).** Let \(X\) be a Hausdorff CW complex with closure-finite cells and the weak topology of its characteristic disks. Every compact subset meets only finitely many open cells and is contained in a finite subcomplex.

**Proof.** Here a characteristic map sends a closed disk onto a cell closure, with its interior homeomorphic to the open cell and its boundary in lower-dimensional cells. Closure-finite means that each cell closure meets only finitely many open cells. The weak topology means that a subset is closed precisely when its inverse image under every characteristic map is closed in the disk.

If a compact subset \(K\) meets infinitely many open cells, choose points \(x_1,x_2,\ldots\) in \(K\) in distinct cells. Any characteristic disk has image in a single cell closure, so that image meets only finitely many of the \(x_i\). For every subset \(A\) of the selected points, its inverse image in that disk is therefore a finite union of inverse images of singleton points. These are closed, because \(X\) is Hausdorff and the characteristic map is continuous. By the weak topology every such \(A\) is closed in \(X\).

In particular the selected set \(S=\{x_i:i\geq1\}\) is closed in \(K\), hence compact: an open cover of a closed subset extends to a cover of \(K\) by adding its open complement. Moreover all subsets of \(S\) are closed, and their complements are therefore open, so \(S\) is discrete. The singleton open cover contradicts its compactness.

Only finitely many cells thus meet \(K\). Take their closures and adjoin all cells met by their boundaries, then repeat for the newly added cells. Each step branches only finitely by closure-finiteness; along any branch the dimension strictly decreases, starting below the finite maximum of the original dimensions. The process terminates with finitely many cells whose characteristic boundaries lie in their union. Their union is a finite subcomplex containing \(K\). □

**Lemma E.2 (a quotient times an interval).** If \(q:Y\to Z\) is a surjective quotient map and \(I=[0,1]\), then \(q\times1:Y\times I\to Z\times I\) is a quotient map.

**Proof.** This product map is a continuous surjection. Suppose the inverse image \(O\) of \(W\subset Z\times I\) is open. For each \(z\), choose \(y\) with \(q(y)=z\). The slice
\(W_z=\{t:(z,t)\in W\}\) equals \(\{t:(y,t)\in O\}\), hence is open in \(I\).

For a compact subinterval \(J\subset I\) define
\[
 U_J=\{z:\{z\}\times J\subset W\}.
\tag{E1}
\]
Its inverse image under \(q\) is open. Indeed, for \(y\) in that inverse image, the whole slice \(\{y\}\times J\) lies in the open set \(O\). Cover it by finitely many product neighborhoods contained in \(O\), whose interval factors cover \(J\). Intersecting their \(Y\)-factors gives a neighborhood \(N\ni y\) with \(N\times J\subset O\), so \(N\subset q^{-1}(U_J)\). Since \(q\) is a quotient map, \(U_J\) is open in \(Z\).

For \((z,t)\in W\), choose a closed subinterval \(J\subset W_z\) with \(t\in\operatorname{int}_I J\); such an interval exists because \(W_z\) is open, including when \(t=0\) or \(1\). Then \(U_J\times\operatorname{int}_I J\) is an open neighborhood of \((z,t)\) contained in \(W\). Thus \(W\) is open and the product is a quotient map.

Consequently homotopies defined on pieces of an attaching quotient, continuous on the disjoint union times \(I\) and agreeing on the identifications at every time, descend continuously to the quotient times \(I\). This is precisely the quotient criterion just proved. □

## Further reading

Allen Hatcher, [*Vector Bundles and K-Theory*, author version 2.2, November 2017](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Sections 1.1–1.2, particularly the universal bundle construction and Theorem 1.16. The proofs above include the direct-limit continuity and variable-step projection arguments needed for arbitrary paracompact Hausdorff bases.

Allen Hatcher, [*Algebraic Topology*, expanded appendix, author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/ATapp.pdf), Proposition A.1, for compact containment in CW complexes.
